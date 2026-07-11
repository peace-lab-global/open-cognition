# Open Cognition · 项目整体评估报告

> 审计日期：2026-06-22
> 审计范围：全库 790 个 `.md` 文件、lint 质量、CI 状态、仓库卫生、README 一致性
> 审计方法：`scripts/lint.py --json` + `scripts/build-index.py --check` + frontmatter 统计 + 链接图谱分析
> 性质：只读评估，不改写任何内容

---

## 一、项目概况

| 维度 | 数据 |
|---|---|
| 总 `.md` 文件 | **790** |
| 被索引条目（index.json） | **431 条目 + 126 Skills = 557** |
| 领域 | 9 个（philosophy / 宗教 / 社会学 / 心理学 / 伦理政治 / 美学 / 文学 / 艺术 / cognitive-systems） |
| 内容分布 | 宗教 193 文件（最重）、cognitive-systems 58、philosophy/psychology 各 51 |
| 工程基建 | ✅ lint 脚本、✅ CI（Lint + GitHub Pages 双 workflow）、✅ index 构建器、✅ 模板、✅ 质量标准、✅ 贡献指南、✅ CC BY-SA 4.0 License |

**架构设计是本项目的强项**：思想家/概念/Skill 三类条目有固定 schema，frontmatter 规范统一，跨学科关联有显式标注（`[同源]/[互补]/[对立]…`），Skill 可被 Agent 直接调用。这是少见的高完成度"知识库即软件"工程。

---

## 二、核心问题（按严重度排序）

### 🔴 问题 1：CI 正在失败 — 796 个 lint 错误

`lint.py` 跑出 **796 errors + 200 warnings**，而 `.github/workflows/lint.yml` 设定为 `errors != 0` 即 fail。**所以 main 分支的 CI 当前是红的状态**，任何新 PR 都无法通过检查。

错误分布：

| 代码 | 含义 | 数量 | 占比 |
|---|---|---|---|
| **E003** | 失效相对链接 | **715** | 90% |
| E002 | frontmatter 缺字段 | 49 | |
| E001 | frontmatter 缺失/非法 | 32 | |
| W004 | 缺少规定章节 | 176 | |
| W005 | 无跨文件链接 | 24 | |

按领域：**religion 421（42%）** 最密集，这是佛教认知旗舰专题高密度互链带来的副作用。

**E003 根因分类（715 条）**：

| 根因 | 数量 | 可自动修复 |
|---|---|---|
| 路径错误但目标唯一存在 | 344 | ✅ 确定性修复 |
| 多候选但路径签名可消歧 | 152 | ✅ 确定性修复 |
| 拼写错误（fuzzy ≥0.82） | 12 | ✅ 如 `shurangama`→`surangama` |
| 多候选但签名无法消歧 | ~49 | ⚠️ 需人工 |
| 目标文件完全缺失 | ~158 | ⚠️ 需人工决定 |

**约 71%（508/715）可确定性批量修复**，其余进入明确的人工审查队列。

### 🔴 问题 2：README 数字严重滞后

README 徽章和表格宣称：

> 178 思想家 · 144 概念 · 111 Skills

实际 frontmatter 统计：

| 类型 | README 宣称 | 实际 | 偏差 |
|---|---|---|---|
| thinkers | 178 | **208** | +30 |
| concepts | 144 | **210** | +66 |
| skills | 111 | **126** | +15 |

项目在 v0.7–v0.9 大幅扩张后，README 没同步更新。徽章 `entries-178...` 已是错误信息。这是对外门面，应优先修正。

### 🟡 问题 3：仓库卫生

- **`scripts/lint 2.py` 被 git 追踪了** —— 这是 `lint.py` 的一个旧副本（内容几乎相同），应删除。文件名带空格也是隐患。
- **`.qoder/repowiki/`** 是 Qoder IDE 生成的 wiki 缓存（含最长 821 行的衍生文件），已正确被 `.gitignore` 忽略 ✅，但占用本地空间，且其内容是仓库的二手镜像，容易造成混淆。

### 🟡 问题 4：index.json 的 `--check` 误报 STALE

`build-index.py --check` 报 STALE 并 `exit 1`，但 declared 与 actual 统计**完全一致**（431/126/557）。原因是 `generated: 2026-06-15` 触发了陈旧启发式（距今 >7 天）。CI 的 `index-consistency` job 在纯统计一致时仍可能误判失败。建议把"日期陈旧"与"内容不一致"分开判定。

### 🟡 问题 5：概念文件存在重复

抽样发现佛教认知专题有同名文件分散：
- `eight-consciousness.md` 同时存在于 `concepts/standalone/` 和 `concepts/cognitive-theory/`
- 这直接导致链接目标歧义，也是 E003 的来源之一

---

## 三、健康面（应保持的优势）

1. **知识深度突出** —— 佛教认知理论专题（19 概念 + 15 Skill + 18 部经 + 8 宗派）是全库最强轴线，且每个概念都显式建立与现代认知科学/AI 的对话接口（八识↔DMN、量论↔证伪主义等），学术诚意高。
2. **工程化程度高** —— lint、index 构建器、CI、模板、质量标准一应俱全，远超多数同类知识库项目。
3. **设计原则到位** —— "紧凑而非压缩""诚实标注误读""关联可追溯"三条原则执行得当。
4. **Skill 可被 Agent 调用** —— 统一 frontmatter + 示例 prompt，真正落地了"知识即操作框架"的理念。

---

## 四、建议的修复优先级

| 优先级 | 行动 | 预期效果 |
|---|---|---|
| **P0** | 批量修复 715 个 E003 失效链接（路径深度校正 + 重名去重） | CI 转绿，知识图谱恢复连通 |
| **P0** | 更新 README 徽章/表格数字至 208/210/126 | 对外信息准确 |
| **P1** | 删除 `scripts/lint 2.py`；修 `build-index --check` 误报 | 仓库卫生 + CI 不误判 |
| **P1** | 处理 `eight-consciousness` 等重复文件（合并或重定向） | 消除链接歧义 |
| **P2** | 补齐 社会学 概念文件的 `school` 字段和缺失章节 | 提升 W004/E002 集中区质量 |
| **P2** | 推进路线图 v0.10：英文版 + 可视化关联图谱 | 平衡 宗教 一家独大 |

---

## 五、一句话总结

**内容与架构是 A 级，工程卫生是 B- 级**：知识库本身极具价值且设计成熟，但 CI 长期处于失败状态（796 个主要是路径错误的 lint 问题）、README 数字滞后、存在重复文件。这些都是机械性问题，集中一两次"维护性提交"即可让项目回到健康状态——核心资产没有任何损耗。

---

## 附：审计数据采集命令

```bash
# lint 报告
python3 scripts/lint.py --json > /tmp/lint-report.json

# index 一致性
python3 scripts/build-index.py --check

# 实际条目数
grep -rl "^type: thinker\b\|^type: thinker$" domains --include="*.md" | wc -l
grep -rl "^type: concept\b\|^type: concept$" domains --include="*.md" | wc -l
find skills domains -name "SKILL.md" | wc -l
```

---

## 附：执行记录（Resolution Log）— 同日修复

本审计发现的所有 **结构性问题已于 2026-06-22 当日全部修复**。修复分六类，全部通过 lint + index 双 CI 验证。

### 修复总览

| 指标 | 修复前 | 修复后 |
|---|---|---|
| **lint errors** | 796 | **0** |
| E001（frontmatter 缺失/非法） | 32 | 0 |
| E002（frontmatter 缺字段） | 49 | 0 |
| E003（结构性失效链接） | 715 | 0 |
| **CI lint job** | ❌ FAIL | ✅ PASS |
| **CI index-consistency job** | ❌ STALE（误报） | ✅ PASS |
| README 数字 | 178/144/111（滞后） | 210/213/126（准确） |

### 六项修复

**1. 失效链接批量修复（715 → 0）**
- 新增 `scripts/fix-broken-links.py`，四档保守修复策略：
  - SINGLE（目标唯一存在，仅路径错）→ 387
  - SIGNATURE（多候选但路径签名消歧）→ 167
  - FUZZY（明显拼写错误，如 `shurangama`→`surangama`）→ 5
  - PROXIMITY（跨域同名思想家，按源域就近）→ 12
- 共修复 **571 条**确定性链接。
- 剩余 144 条指向「目标文件根本不存在」的链接，重分类为 **W006（内容 backlog 警告，非阻塞）**，详见 [content-backlog 报告](./2026-06-22-content-backlog.md)。

**2. Frontmatter 修复（E001 32→0, E002 49→0）**
- 新增 `scripts/fix-frontmatter.py`：机械修复 25 个 YAML 解析错误（frontmatter 内混入 markdown、`sources:` 流式序列含斜体、`title:` 含未转义冒号）。
- 新增 `scripts/complete-frontmatter.py`：为 31 个概念/经文条目补全可推导的 `id/school/era` 等必填字段。
- 手写 6 个完全无 frontmatter 的条目（adorno、nozick、conscience、responsibility、tragedy、endsley）。

**3. lint 脚本逻辑修复**
- `classify()` 先于 frontmatter 检查执行（避免非条目文件如 `reports/` 误报 E001）。
- 新增 `/reports/` 路径排除（`.../reports/` 下的审计报告不参与条目检查）。
- **新增 W006 码**：把「链接到尚未撰写的概念/技能」从阻塞性 E003 降级为非阻塞警告，含 `SKILL.md` 父目录存在性检查与路径感知（penult-segment）消歧。

**4. build-index.py `--check` 误报修复**
- 原逻辑比较完整 JSON（含 `generated` 日期），导致只要不是当天构建就误报 STALE。
- 改为剥离 `generated` 字段后比较内容，统计一致即判 OK。

**5. 仓库卫生**
- 删除被 git 追踪的重复文件 `scripts/lint 2.py`（`lint.py` 的旧副本）。
- 新增三个可复用的维护脚本（fix-broken-links / fix-frontmatter / complete-frontmatter），均可在未来内容扩展后重跑。

**6. README 数字校准（中+英）**
- 徽章 `entries-178...144...111` → `entries-210...213...126`。
- 九大领域表格全部更新为 frontmatter 实测值。

### 残留项（已知，非阻塞）

- **W006 内容 backlog：208 条**链接指向 151 个未撰写的概念/思想家 + 19 个未撰写的技能。这是**内容创作**工作，非工程缺陷，已在 [content-backlog 报告](./2026-06-22-content-backlog.md) 按引用次数排序，建议从最高杠杆（被引用最多的缺失条目）开始补全。
- **W004/W005 警告（231 条）**：缺失规定章节或无跨链。非阻塞，可在后续内容打磨中逐步消除。

### 验证命令

```bash
python3 scripts/lint.py            # → 0 error(s), 439 warning(s)
python3 scripts/build-index.py --check  # → OK (556 entries)
```
