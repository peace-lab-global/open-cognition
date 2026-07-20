# Open Cognition · 项目整体评估报告

> 审计日期：2026-07-19
> 审计范围：全库 3259 个 `.md` 文件（54MB）、lint 质量、CI 状态、索引一致性、README/AGENT.md 对齐、仓库卫生
> 审计方法：`_meta/scripts/lint.py` + `_meta/scripts/build-index.py --check` + frontmatter 统计 + 链接图谱分析 + 条目抽查
> 性质：只读评估，不改写任何内容
> 对比基线：[2026-06-22 评估报告](./2026-06-22-project-assessment.md)（790 文件 / 796 errors / CI 红）

---

## 一、项目概况

| 维度 | 数据 | 对比 06-22 |
|---|---|---|
| 总 `.md` 文件 | **3259** | ↑ 4.1× (790→3259) |
| 被索引条目（index.json） | **2387** | ↑ 4.3× (557→2387) |
| 领域 | 9 个 | 不变 |
| Lint errors | **0** | ✅ 从 796 降至 0 |
| Lint warnings | **5361** | ↑ (200→5361)，但性质变化（见下） |
| CI 状态 | ✅ 绿（Lint + index-consistency 双通过） | 从红转绿 |
| index.json 一致性 | ✅ `--check` 通过 | 新增校验 |
| 工程基建 | lint + build-index + CI + templates + quality-criteria + CONTRIBUTING + TAGS + AGENT.md | 不变，稳定 |

**结论**：项目在一个月内完成从 790→3259 文件的 4 倍扩展，同时将 CI 从红修复为绿、errors 从 796 降至 0。工程纪律显著改善。

---

## 二、架构设计评价（强项）

### 2.1 三类条目 Schema 成熟

| 类型 | Schema 完整度 | 代表条目 |
|---|---|---|
| Thinker | frontmatter + 11 段固定结构 + pointer→子目录展开 | 康德（413 行 README + 概念/批评/对话/著作/时间线/阅读 6 子目录） |
| Concept | frontmatter + 10 段固定结构 + 通俗 vs 学术表 | 量论、可供性、心流 |
| Skill | YAML frontmatter + 操作流程 + 示例 + 反例 | CBT 认知扭曲识别（105 行） |

### 2.2 Pointer + 子目录模式

大思想家不再挤在单文件里，而是：
```
康德.md (pointer, 34 行) → 康德/README.md (413 行深度)
                              ├── 概念/ (5 篇)
                              ├── 批评/ (3 篇)
                              ├── 对话/ (5 篇)
                              ├── 著作.md
                              ├── 时间线.md
                              └── 阅读.md
```
这解决了"~100 行紧凑"承诺与深度展开之间的矛盾，是 v0.9 最重要的架构改进。

### 2.3 Agent-Native 设计

- AGENT.md 提供 30 秒接入指南 + 3 套 Prompt 模板 + 5 种集成方式
- Skill frontmatter 含 `name/description/domain/tags/linked_concepts`，可被 Claude Skills / Qoder Skills / RAG 直接索引
- 跨链使用显式关联类型（10 种），Agent 可建立带 label 的知识图谱边
- "常见误读"段 + "通俗 vs 学术"表为 Agent 输出提供安全护栏

### 2.4 旗舰专题深度

| 专题 | 规模 | 差异化 |
|---|---|---|
| 佛教认知理论 | 19 概念 + 15 Skill + 18 经 + 8 宗派 + 32 大师 | 每条目显式与现代认知科学对话（八识↔DMN、量论↔证伪主义、公案↔γ 波） |
| 认知系统工程 | 28 思想家 + 27 概念 + 16 Skill | 覆盖控制论→生态心理学→分布式认知→安全科学→自动化全谱系 |

---

## 三、核心问题（按严重度排序）

### 🟡 问题 1：README ↔ AGENT.md 计数漂移

| 来源 | Thinkers | Concepts | Skills |
|---|---|---|---|
| README.md 徽章 | 210 | 213 | 126 |
| AGENT.md 徽章 | 154 | 110 | 130 |
| index.json 实际 | — | — | 2387 总条目 |

三处数字互不一致。README 说"210 思想家"，AGENT.md 说"154 思想家"，index.json 有 2387 条但未按类型分拆公开。

**根因**：徽章数字为手工维护，未与 `build-index.py` 联动。

**建议**：让 `build-index.py` 输出 `counts.json`（thinkers/concepts/skills/domains），README 和 AGENT.md 的徽章从该文件生成，或在 CI 中校验一致性。

### 🟡 问题 2：5361 条 Warnings 信号退化

| 代码 | 含义 | 数量 | 占比 |
|---|---|---|---|
| W006 | 链接指向尚未撰写的条目 | **4753** | 89% |
| W001 | 条目过短（< MIN_LINES） | 400 | 7% |
| W004 | 缺少规定章节 | 208 | 4% |

W006 设计为"内容 backlog 标记"而非死链——目标 basename 在全库不存在，表示规划中但未撰写。这在早期（200 条）有信号价值，但 4753 条已使 lint 输出不可读。

**高密度来源**：`认知系统/概念/麦肯锡方法.md` 单文件贡献 30+ 条 W006（链接到 `./有限理性.md`、`./心智模型.md` 等未撰写概念）。

**建议**：
1. 对 W006 引入密度阈值：单文件 > 5 条时升级为"backlog 清单"移入 `_meta/reports/content-backlog.md`，原文件改用注释标记。
2. 或为 W006 增加 `--suppress-backlog` 模式，让日常 lint 只报告新增问题。
3. 优先处理 W001（400 条过短条目）和 W004（208 条缺段），这两类是真正可操作的质量债务。

### 🟡 问题 3：INDEX.md 标签-链接错位

INDEX.md:41 存在明显的标签与链接目标不匹配：

```markdown
- [心物一元 (Mind-World Identity)](宗教/佛教/概念/cognitive-theory/转识成智.md)
- [转识成智 (Transformation of Consciousness)](宗教/佛教/概念/cognitive-theory/六根六尘六识.md)
```

"心物一元"链接到 `转识成智.md`，"转识成智"链接到 `六根六尘六识.md`——标签与文件名错位一位。

**根因**：批量重命名（RENAME-MAP.md 36KB 佐证）后 INDEX.md 未同步更新。

**建议**：运行 `_meta/scripts/fix-broken-links.py` 全库审计，或为 INDEX.md 增加 CI 校验（`build-index.py --check` 已覆盖 index.json，但 INDEX.md 尚未被校验）。

### 🟢 问题 4：脚本分散

| 位置 | 内容 | 性质 |
|---|---|---|
| `scripts/`（根目录） | 11 个 rename/annotate 脚本 | 一次性迁移工具 |
| `_meta/scripts/` | lint / build-index / fix-links / hooks | 持续维护工具 |
| `expand-thinkers.js`（根目录） | 思想家扩展脚本 | 一次性 |

**建议**：将 `scripts/` 和 `expand-thinkers.js` 归档到 `_meta/scripts/archive/`，根目录保持干净。

### 🟢 问题 5：工作区大量未提交修改

当前 `git status` 显示 INDEX.md、README.md、TAGS.md、ci.yml、lint.py、build-index.py 及多个思想家文件处于 modified 状态。长寿命 dirty tree 增加丢失风险。

**建议**：分批 commit（基建改动一批、内容改动一批），保持 main 分支清洁。

---

## 四、内容质量抽查

### 4.1 康德条目（哲学/学派/德国唯心论/康德/README.md）

| 检查项 | 结果 |
|---|---|
| 原典引文 + 出处 | ✅ 含德文原文 + 年份 |
| 中英对照 | ✅ |
| 常见误读段 | ✅ |
| 跨学科关联 + 关联类型标注 | ✅ |
| 子目录完整度 | ✅ 概念 5 + 批评 3 + 对话 5 + 著作 + 时间线 + 阅读 |
| 主观评价词 | 未发现 |

### 4.2 CBT 认知扭曲识别 Skill（心理学/技能/认知扭曲识别/SKILL.md）

| 检查项 | 结果 |
|---|---|
| frontmatter 完整 | ✅ name/description/domain/tags/linked_concepts |
| 何时使用/不使用 | ✅ |
| 操作流程 Step 1-N | ✅ |
| 完整示例 | ✅ |
| 反例 | ✅ |
| 行数 | 105 行，符合紧凑原则 |

### 4.3 质量标准覆盖度

`_meta/quality-criteria.md` 7 大类检查项在抽查条目中基本落地。主要差距在 W004（208 条缺段）——多为新增条目尚未补齐"常见误读"或"跨学科关联"段。

---

## 五、演进对比（06-22 → 07-19）

| 维度 | 06-22 | 07-19 | 变化 |
|---|---|---|---|
| 文件数 | 790 | 3259 | +313% |
| index.json 条目 | 557 | 2387 | +328% |
| Lint errors | 796 | **0** | ✅ 清零 |
| CI 状态 | 🔴 红 | 🟢 绿 | ✅ 修复 |
| 主要架构 | 单文件条目 | pointer + 子目录 | ✅ 升级 |
| 佛教专题深度 | 15 概念 + 15 Skill | 19 概念 + 15 Skill + 18 经 + 32 大师 | ↑ |
| 名言模块 | 不存在 | 61 主题 · 186 条 | 新增 |
| 清单模块 | 不存在 | 94 张 · 1225 条 | 新增 |
| 研究专题 | 不存在 | 3 个（定力/直接认知/康德） | 新增 |

---

## 六、建议优先级

| 优先级 | 行动 | 预期收益 |
|---|---|---|
| P0 | 修复 INDEX.md 标签-链接错位 + 全库链接审计 | 消除人类读者和 Agent 的导航错误 |
| P0 | 分批 commit 当前 dirty tree | 消除丢失风险 |
| P1 | 让徽章/计数由脚本生成，消除 README↔AGENT.md 漂移 | 单一数据源 |
| P1 | W006 引入密度阈值或 suppress 模式 | 恢复 lint 信号价值 |
| P2 | 处理 W001（400 过短）+ W004（208 缺段） | 内容质量提升 |
| P2 | 归档一次性脚本到 `_meta/scripts/archive/` | 仓库卫生 |
| P3 | 为 INDEX.md 增加 CI 校验（类似 index.json --check） | 防止再次漂移 |
| P3 | v0.10 英文版优先做佛教认知 + CSE 两个旗舰专题 | 国际化 |

---

## 七、总评

Open Cognition 在 v0.9 阶段已完成从"个人知识笔记"到"工程化开源知识库"的质变：

1. **架构成熟**：三类条目 Schema + pointer/子目录 + 显式关联类型 + Agent-native frontmatter，在同类项目中属上乘设计。
2. **工程纪律恢复**：一个月内将 796 errors 清零、CI 转绿、index.json 一致性自动校验，说明维护者有持续投入能力。
3. **内容差异化明确**：佛教认知理论体系（19 概念 + 18 经 + 32 大师 + 与现代认知科学对话）和 CSE 全谱系覆盖，在中文开源知识库中无直接竞品。
4. **主要风险**：不在内容深度，而在**大规模扩展后的一致性维护**——计数漂移、链接错位、warning 信号退化。这些是"成长痛"，可通过工具化手段系统性解决。

**评级**：v0.9 已具备公开发布与社区贡献的条件。完成 P0/P1 项后即可推进 v1.0。

---

*报告生成：Qoder · 2026-07-19 · 只读审计，未修改任何内容文件*
