> English version: see [README.en.md](./README.en.md)

# Open Cognition · 开放认知数据库

> 一个面向**人类深度阅读**与 **AI Agent 调用**的跨学科认知资源库。
> 把哲学、宗教、社会学、心理学、伦理学、美学、文学、艺术、认知系统工程中**最值得反复使用的思想、命题、方法**整理成可链接、可检索、可复用的开源知识结构。

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-v0.9%20buddhist--academy--deep-blue.svg)](#)
[![Domains](https://img.shields.io/badge/domains-9-orange.svg)](#内容总览)
[![Entries](https://img.shields.io/badge/entries-178%20thinkers%20%7C%20144%20concepts%20%7C%20111%20skills-brightgreen.svg)](#内容总览)

---

## 项目目标

跨学科的洞见常分散在难以阅读的原典与互不通话的学派之中。本项目希望：

1. **降低门槛** — 用 ~100 行的紧凑条目快速建立对一个思想家/概念的整体感。
2. **保持深度** — 拒绝鸡汤式简化，每条目附原典、研究、入门三层进阶阅读。
3. **跨学科互链** — 显式标注 `[同源]/[互补]/[对立]/[发展]/[批判]/[平行]/[张力]/[继承]/[借用]/[下位]` 等关联类型。
4. **可被 Agent 直接调用** — 提炼出标准化的 **Skill**（操作框架），让 LLM 与人类都能用同一份知识做事。
5. **深度专题** — 在若干关键轴线上做**专题化深化**（如佛教认知理论体系），形成可直接用于研究、教学、心理实践的子系统。

---

## 内容总览

```
9 个领域 × N 思想家/条目 + 概念条目 + Skills + 专题深化
= 178 思想家 · 144 概念 · 111 Skills · 550+ 结构化 .md 文件
```

### 九大领域

| 领域 | 思想家 | 概念 | Skills | 入口 |
|---|:---:|:---:|:---:|---|
| **哲学** Philosophy | 28 | 8 | 19 | [domains/philosophy](./domains/philosophy/README.md) |
| **宗教** Religion | 32 | 76 | 39 | [domains/religion](./domains/religion/README.md) · [佛教认知专题 ↓](#佛教认知理论体系旗舰专题) |
| **社会学** Sociology | 18 | 7 | 15 | [domains/sociology](./domains/sociology/README.md) |
| **心理学** Psychology | 28 | 8 | 16 | [domains/psychology](./domains/psychology/README.md) |
| **伦理与政治哲学** Ethics & Politics | 15 | 11 | 10 | [domains/ethics-politics](./domains/ethics-politics/README.md) |
| **美学** Aesthetics | 23 | 7 | 3 | [domains/aesthetics](./domains/aesthetics/README.md) |
| **文学** Literature | 5 | — | 5 | [domains/literature](./domains/literature/README.md) |
| **艺术** Arts | 3 | — | 3 | [domains/arts](./domains/arts/README.md) |
| **认知系统工程** Cognitive Systems Engineering | 26 | 27 | 16 | [domains/cognitive-systems](./domains/cognitive-systems/README.md) |

> **宗教领域 76 概念** 含 19 个佛教认知理论专章 + 16 部经典独立深度条目（详见下文专题）。**39 个 Skill** 含 15 个佛教认知专项 Skill + 3 个佛教冥想实践 Skill + 7 个佛学院方法论 Skill。

完整索引见 [INDEX.md](./INDEX.md) ｜ 标签词典见 [TAGS.md](./TAGS.md)。

---

## 🌟 佛教认知理论体系（旗舰专题）

在 `domains/religion/buddhism/concepts/cognitive-theory/` 下，本仓库对**佛教的认知科学与认识论资源**做了目前全库最深的专题化整理：

### 内容结构

| 层级 | 数量 | 覆盖 |
|------|------|------|
| **概念文件** | 15 核心 + 4 禅修专题 = **19** | 唯识、中观、阿毗达磨、量论、早期佛教、汉藏禅宗 |
| **应用 Skill** | **15** | 八识诊断、三性诊断、量论验证、缘起追溯、五蕴解构… |
| **经论 Cognitive Architecture** | **18 部经** | 楞严、解深密、楞伽、心经、金刚、六祖坛经、圆觉、维摩、华严、法华、诸净土经、地藏、涅槃、梵网、四十二章、药师 |
| **宗派认知架构** | **8** | 上座部、中观、唯识、天台、华严、禅、净土、密 |
| **大师认知贡献** | **32** | 龙树、无著世亲、智顗、法藏、慧能、宗喀巴、道元、莲花生、阿底峡、密勒日巴、马鸣、法称、空海、荣西、僧肇、道宣、吉藏、窥基、善导、印光、鸠摩罗什、菩提达摩、慧远、法显、提婆、陈那、月称、寂天、真谛、隆钦巴、白隐、太虚 |

### 关键概念矩阵

```
唯识核心           中观核心          基础佛教           汉藏禅专题
─────────────────────────────────────────────────────────────────
八识体系 ────────┐  中观·空 ────────┐  阿毗达磨心识论 ─┐  七处征心
心物一元（四分） │  二谛 ────────────┤  十二因缘认知读法┤  八还辨见
六根六尘六识 ───┤  （含应成/自续） │  五蕴认知读法 ───┤  金刚经无相
转识成智（四智） │                   量论（因明） ───┤  止观分工
三性 ────────────┘                   ──────────────────┘  四念处元认知
种子与熏习                                                    公案机制
                                                              默照结构
```

### 入口导航

- **总入口**：[`domains/religion/buddhism/INDEX.md`](./domains/religion/buddhism/INDEX.md) 第 5 层
- **认知理论目录**：[`concepts/cognitive-theory/README.md`](./domains/religion/buddhism/concepts/cognitive-theory/README.md)（含 9 主题认知地图表）
- **代表概念**：[量论](./domains/religion/buddhism/concepts/cognitive-theory/pramana.md) · [三性](./domains/religion/buddhism/concepts/cognitive-theory/three-natures.md) · [转识成智](./domains/religion/buddhism/concepts/cognitive-theory/consciousness-transformation.md) · [公案机制](./domains/religion/buddhism/concepts/cognitive-theory/koan-mechanics.md)
- **代表 Skill**：[八识诊断](./domains/religion/buddhism/concepts/cognitive-theory/skills/eight-consciousness-diagnosis/SKILL.md) · [三性诊断](./domains/religion/buddhism/concepts/cognitive-theory/skills/three-natures-diagnosis/SKILL.md) · [缘起链追溯](./domains/religion/buddhism/concepts/cognitive-theory/skills/dependent-origination-tracing/SKILL.md) · [五蕴解构](./domains/religion/buddhism/concepts/cognitive-theory/skills/five-aggregates-deconstruction/SKILL.md)

### 与当代对话的接口

每个概念文件都显式建立与现代**认知科学、心理学、现象学、心灵哲学、AI** 的对话——例如：

- 八识 ↔ 默认模式网络（DMN）
- 五蕴 ↔ 休谟束论 + 绑定问题
- 量论 ↔ 证伪主义 + 卡尔纳普内外问题
- 公案 ↔ 顿悟神经（γ 波，Kounios & Beeman）
- 默照 ↔ 前反思自身意识（Zahavi）
- 种子 ↔ 预测编码（Friston）

---

## 仓库结构

```
open-cognition/
│
├── README.md                   # 本文件（项目总览）
├── AGENT.md                    # AI Agent 接入指南
├── INDEX.md                    # 全库双视角索引（领域 + 主题 + Skills）
├── TAGS.md                     # 统一标签词典与关联类型
├── CONTRIBUTING.md             # 贡献指南
├── index.json                  # 机器可读索引
│
├── domains/                    # 知识条目主体
│   ├── philosophy/             # 哲学（28 思想家 / 8 概念）
│   │   ├── README.md
│   │   ├── schools/<流派>/<思想家>.md
│   │   └── concepts/<概念>.md
│   ├── religion/               # 宗教（含佛教认知专题）
│   │   ├── README.md
│   │   ├── traditions/<传统>/<条目>.md
│   │   ├── concepts/<跨传统概念>.md
│   │   └── buddhism/           # 🌟 佛教认知理论专题（旗舰）
│   │       ├── INDEX.md · README.md
│   │       ├── core-concepts/ · schools/ · masters/ · sutras/
│   │       └── concepts/cognitive-theory/（19 概念 + 15 Skill）
│   ├── sociology/              # 社会学
│   ├── psychology/             # 心理学
│   ├── ethics-politics/        # 伦理与政治哲学
│   ├── aesthetics/             # 美学
│   ├── literature/             # 文学
│   ├── arts/                   # 艺术
│   └── cognitive-systems/      # 认知系统工程
│
├── skills/                     # 通用 Skills（按领域分组）
│   ├── philosophy-frameworks/<skill>/SKILL.md
│   ├── religion-frameworks/
│   ├── sociology-frameworks/
│   ├── psychology-frameworks/
│   ├── ethics-politics-frameworks/
│   ├── aesthetics-frameworks/
│   ├── literature-frameworks/
│   ├── arts-frameworks/
│   └── cognitive-systems-frameworks/
│
├── wisdom-masters/             # 高僧心法（操作化蒸馏）
│   ├── masters/<地区>/
│   └── skills/<人物-主题>/
│
├── meta/                       # 元数据与规范
│   ├── quality-criteria.md     # 质量标准
│   ├── taxonomy.md             # 分类法
│   ├── sources.md              # 引用源
│   ├── templates/              # 思想家/概念/学派/Skill 模板
│   └── logo/                   # 项目 Logo 与品牌资产
│
├── visual/                     # 可视化与信息图
│   ├── infographic/            # Notion 风格信息图源文件与专题
│   ├── cse/                    # 认知系统工程架构可视化
│   ├── domain/                 # 各领域专属信息图（9 大领域）
│   └── general/                # 综合信息图、Notion 风格大图、时间线
│
└── reports/                    # 阶段执行报告与审计
```

---

## 三种条目类型

### 1. 思想家 Thinker

固定结构：基本信息 / 核心命题 / 思想脉络 / 关键著作 / 重要概念 / 思想坐标 / 当代应用 / 常见误读 / 跨学科关联 / 进阶阅读 / 关联 Skills。

例：[弗洛伊德](./domains/psychology/schools/psychoanalysis/freud.md) · [韦伯](./domains/sociology/schools/classical/weber.md) · [康德](./domains/philosophy/schools/german-idealism/kant.md) · [龙树](./domains/religion/buddhism/masters/nagarjuna.md) · [道元](./domains/religion/buddhism/masters/dogen.md)

### 2. 概念 Concept

固定结构：一句话定义 / 历史脉络 / 核心要义 / 通俗 vs 学术 / 与相关概念关系 / 代表思想家 / 应用场景 / 常见误读 / 跨学科关联 / 进阶阅读。

例：[心流 Flow](./domains/psychology/concepts/flow.md) · [文化资本](./domains/sociology/concepts/cultural-capital.md) · [神圣性](./domains/religion/concepts/sacred.md) · [量论](./domains/religion/buddhism/concepts/cognitive-theory/pramana.md)

### 3. Skill

agent 可执行的操作框架，含 YAML frontmatter + 一句话功能 + 何时用/不用 + 理论基础 + 操作流程（Step 1–N） + 完整示例 + 反例。

例：[CBT 认知扭曲识别](./skills/psychology-frameworks/cbt-cognitive-distortion/SKILL.md) · [布迪厄场域分析](./skills/sociology-frameworks/bourdieu-field-analysis/SKILL.md) · [四圣谛诊断](./skills/religion-frameworks/four-noble-truths-framework/SKILL.md) · [八识诊断](./domains/religion/buddhism/concepts/cognitive-theory/skills/eight-consciousness-diagnosis/SKILL.md) · [五蕴解构](./domains/religion/buddhism/concepts/cognitive-theory/skills/five-aggregates-deconstruction/SKILL.md)

---

## 使用方式

### 给人类读者

- **横向阅读**：选一个主题（如 [自我 Self](./INDEX.md#自我-self)），跨四个领域纵览不同视角。
- **纵向阅读**：从领域 README 进入流派，深度走完一个学派。
- **专题阅读**：进入 [佛教认知专题](./domains/religion/buddhism/INDEX.md) 或 [CSE 专题](./domains/cognitive-systems/README.md)，系统性掌握一条轴线。
- **诊断式阅读**：遇到具体困境时，使用对应 Skill（例如个人迷茫 → [马斯洛需求诊断](./skills/psychology-frameworks/maslow-needs-diagnosis/SKILL.md)；认知卡点 → [八识诊断](./domains/religion/buddhism/concepts/cognitive-theory/skills/eight-consciousness-diagnosis/SKILL.md)；叙事困住 → [三性诊断](./domains/religion/buddhism/concepts/cognitive-theory/skills/three-natures-diagnosis/SKILL.md)）。

### 给 AI Agent

所有 Skill 文件遵循统一 frontmatter 格式：

```yaml
---
name: <skill-id>
description: <一句话功能>
domain: <philosophy|religion|sociology|psychology|...>
linked_concepts: [相关概念相对路径...]
tags: [...]
---
```

可被 agent runtime（如 Claude Skills、Qoder Skills、自定义 RAG）直接索引、调用。条目之间的跨链使用相对路径与显式关联类型，便于 LLM 推理图谱。

### 示例 Prompt

> "用 [CBT 认知扭曲识别](./skills/psychology-frameworks/cbt-cognitive-distortion/SKILL.md) 分析下面这段独白：……"
>
> "把以下职场困境同时用 [马斯洛需求诊断](./skills/psychology-frameworks/maslow-needs-diagnosis/SKILL.md) 与 [布迪厄场域分析](./skills/sociology-frameworks/bourdieu-field-analysis/SKILL.md) 跑一遍。"
>
> "我反复陷入同一模式，请用 [种子模式分析](./domains/religion/buddhism/concepts/cognitive-theory/skills/bija-pattern-analysis/SKILL.md) 追溯它的熏习来源，并设计定向熏习方案。"
>
> "这两条陈述看起来冲突，请用 [二谛重构](./domains/religion/buddhism/concepts/cognitive-theory/skills/two-truths-reframing/SKILL.md) 帮我识别它们分别在哪一谛层次成立。"

---

## 设计原则

1. **紧凑而非压缩** — 每条目控制在约 100 行内，但保留必要的张力与原文语境。
2. **多源验证** — 条目以原典为锚，二手研究为镜，中文资源为桥。
3. **诚实标注误读** — 每条目设"常见误读"，明确说明哪些流行说法偏离原意。
4. **关联可追溯** — 跨学科链接使用统一的关联类型标注，便于追问"为什么相关"。
5. **持续可贡献** — 模板与质量标准开放，欢迎补充传统与流派。
6. **专题化深度** — 在关键轴线上做深度专题（如佛教认知、CSE），不止停留在横向扩展。

---

## 路线图

- ✅ **v0.1**：五领域基础骨架。
- ✅ **v0.2**：六领域全面扩展 + 全球顶尖人物全量补充。
- ✅ **v0.3**：文学家/文艺家全面融合。美学领域从 7 人扩展到 23 人；新增 `domains/literature/` 与 `domains/arts/`。
- ✅ **v0.4**：新增**认知系统工程**领域——控制论（维纳/阿什比/西蒙）、生态心理学（吉布森/克拉克/瓦雷拉）、分布式认知（哈钦斯/恩格斯托姆/列昂捷夫）、认知系统工程（拉斯穆森/伍兹/诺曼）、自然决策（克莱因/维克/斯威勒）。
- ✅ **v0.5**：CSE 领域深度扩展——新增安全科学学派（霍伦纳格/里森/德克尔）、自动化与社会技术学派（班布里奇/帕拉休拉曼/维森特）。新增宏观认知/团队认知/分布式态势感知/情境化认知 4 概念和 5 个 Skills。
- ✅ **v0.6**：**佛教认知理论体系化**——新增 15 核心概念（量论、三性、种子、二谛、阿毗达磨心识论、缘起认知读法、五蕴认知读法等）+ 15 个专项 Skill + 4 篇禅修认知专题（止观、四念处、公案、默照）。深化 4 个核心文件（八识/转识成智/心物一元/中观）。18 部经 + 8 宗派 + 8 位大师皆增设 **Cognitive Architecture / Key Cognitive Contribution** 段。共新增 ~3600 行内容。
- ✅ **v0.7**：**佛学院水平扩展**——新增 6 高僧（僧肇/道宣/吉藏/窥基/善导/印光）+ 5 宗派（律宗/三论/俱舍/法相唯识/地论）+ 8 核心概念（戒律学/五明/百法/四依/二谛/判教/止观/如来藏）+ 2 论典独立条目（起信论/俱舍论）+ 3 佛学院方法论 Skill（经论判释/戒律辨析/论典结构分析）。覆盖戒律学、三论、俱舍、唯识、五明等佛学院五大支柱。
- ✅ **v0.8**：**佛学院深化扩展**——新增 4 高僧（鸠摩罗什/菩提达摩/慧远/法显）+ 4 宗派（成实/摄论/涅槃/日莲）+ 8 核心概念（三十七道品/十八界/空性/无我/三解脱门/三身/二障/四法印）+ 4 论典独立条目（成唯识论/涅槃经/中论/楞伽经）+ 2 佛学院方法论 Skill（唯识百法分析/公案参究法）。
- ✅ **v0.9（当前）**：**佛学院第三轮深化**——新增 8 高僧（提婆/陈那/月称/寂天/真谛/隆钦巴/白隐/太虚）+ 4 宗派（临济/曹洞/净土真宗/宁玛）+ 8 核心概念（贪嗔痴/十二处/唯识/方便/九住心/三乘/头陀行/四无所畏）+ 4 论典独立条目（入中论/入菩萨行论/大智度论/大日经）+ 2 Skill（九住心分析/密续象征分析）。覆盖中观传承线、因明创始、日本禅分支、藏传大圆满、近代佛教改革。
- 🔮 **v0.10**：英文版（优先佛教认知专题 + CSE 专题）、可视化关联图谱、Agent SDK 集成示例。
- 🔮 **v0.11**：心理学与认知系统的对等深度专题化（认知科学 + 现象学 + 心灵哲学轴线）。

---

## 贡献

欢迎贡献新条目、修订误读、补充跨学科链接。请先阅读：

- [CONTRIBUTING.md](./CONTRIBUTING.md) — 贡献流程
- [meta/quality-criteria.md](./meta/quality-criteria.md) — 质量标准
- [meta/taxonomy.md](./meta/taxonomy.md) — 分类法
- [meta/sources.md](./meta/sources.md) — 引用源
- [TAGS.md](./TAGS.md) — 标签与关联类型规范
- [meta/templates/](./meta/templates/) — 各类型条目模板（thinker/concept/school/skill）

---

## 许可

内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可，欢迎在标注来源的前提下自由使用、修改与分发。

---

## 致谢

本项目站在每位被收录思想家与无数学者的肩膀上。所列条目仅为入门指引，原典与一流二手研究永远是不可替代的。

> "一切有为法，如梦幻泡影；如露亦如电，应作如是观。" ——《金刚经》
>
> "The map is not the territory." —— Alfred Korzybski
