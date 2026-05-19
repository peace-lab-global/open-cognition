# Open Cognition · 开放认知数据库

> 一个面向**人类深度阅读**与 **AI Agent 调用**的跨学科认知资源库。
> 把哲学、宗教、社会学、心理学、伦理学、美学中**最值得反复使用的思想、命题、方法**整理成可链接、可检索、可复用的开源知识结构。

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-v0.1%20foundation-blue.svg)](#)

---

## 项目目标

跨学科的洞见常常分散在难以阅读的原典与互不通话的学派之中。本项目希望：

1. **降低门槛** — 用 ~100 行的紧凑条目快速建立对一个思想家/概念的整体感。
2. **保持深度** — 拒绝鸡汤式简化，每条目附原典、研究、入门三层进阶阅读。
3. **跨学科互链** — 显式标注 `[同源]/[互补]/[对立]/[发展]/[批判]/[平行]/[张力]/[继承]/[借用]/[下位]` 等关联类型。
4. **可被 Agent 直接调用** — 提炼出标准化的 **Skill**（操作框架），让 LLM 与人类都能用同一份知识做事。

---

## 内容总览

```
6 个领域 × N 思想家/条目 + 概念条目 + Skills
= 94 思想家 + 61 概念 + 67 Skills
```

| 领域 | 条目结构 | 入口 |
|---|---|---|
| 哲学 Philosophy | 28 思想家 / 8 概念 / 4 Skills | [domains/philosophy](./domains/philosophy/README.md) |
| 宗教 Religion | 16 条目 / 4 跨传统概念 / 11 Skills | [domains/religion](./domains/religion/README.md) |
| 社会学 Sociology | 18 思想家 / 7 概念 / 4 Skills | [domains/sociology](./domains/sociology/README.md) |
| 心理学 Psychology | 25 思想家 / 8 概念 / 4 Skills | [domains/psychology](./domains/psychology/README.md) |
| 伦理学与政治哲学 Ethics & Political Philosophy | 15 思想家 / 11 概念 / 5 Skills | [domains/ethics-politics](./domains/ethics-politics/README.md) |
| 美学与艺术哲学 Aesthetics | 7 思想家 / 4 概念 / 3 Skills | [domains/aesthetics](./domains/aesthetics/README.md) |

完整索引见 [INDEX.md](./INDEX.md) ｜ 标签词典见 [TAGS.md](./TAGS.md)。

---

## 仓库结构

```
open-cognition/
├── README.md                   # 本文件
├── INDEX.md                    # 全库双视角索引（领域 + 主题 + Skills）
├── TAGS.md                     # 统一标签词典与关联类型
├── CONTRIBUTING.md             # 贡献指南
├── domains/                    # 知识条目主体
│   ├── philosophy/
│   │   ├── README.md
│   │   ├── schools/<流派>/<思想家>.md
│   │   └── concepts/<概念>.md
│   ├── religion/
│   │   ├── README.md
│   │   ├── traditions/<传统>/<条目>.md
│   │   └── concepts/<跨传统概念>.md
│   ├── sociology/
│   │   ├── README.md
│   │   ├── schools/<流派>/<思想家>.md
│   │   └── concepts/<概念>.md
│   ├── psychology/
│   │   ├── README.md
│   │   ├── schools/<流派>/<思想家>.md
│   │   └── concepts/<概念>.md
│   └── ethics-politics/
│       ├── README.md
│       ├── schools/<学派>/<思想家>.md
│       └── concepts/<概念>.md
├── skills/                     # Agent 可调用的操作框架
│   ├── philosophy-frameworks/<skill>/SKILL.md
│   ├── religion-frameworks/
│   ├── sociology-frameworks/
│   ├── psychology-frameworks/
│   └── ethics-politics-frameworks/
├── templates/                  # 思想家/概念/学派/Skill 模板
└── meta/                       # 分类法、引用源、质量标准
```

---

## 三种条目类型

### 1. 思想家 Thinker
固定结构：基本信息 / 核心命题 / 思想脉络 / 关键著作 / 重要概念 / 思想坐标 / 当代应用 / 常见误读 / 跨学科关联 / 进阶阅读 / 关联 Skills。

例：[弗洛伊德](./domains/psychology/schools/psychoanalysis/freud.md)、[韦伯](./domains/sociology/schools/classical/weber.md)、[康德](./domains/philosophy/schools/german-idealism/kant.md)。

### 2. 概念 Concept
固定结构：一句话定义 / 历史脉络 / 核心要义 / 通俗 vs 学术 / 与相关概念关系 / 代表思想家 / 应用场景 / 常见误读 / 跨学科关联 / 进阶阅读。

例：[心流 Flow](./domains/psychology/concepts/flow.md)、[文化资本](./domains/sociology/concepts/cultural-capital.md)、[神圣性](./domains/religion/concepts/sacred.md)。

### 3. Skill
agent 可执行的操作框架，含 YAML frontmatter + 一句话功能 + 何时用/不用 + 理论基础 + 操作流程（Step 1–N） + 完整示例 + 反例。

例：[CBT 认知扭曲识别](./skills/psychology-frameworks/cbt-cognitive-distortion/SKILL.md)、[布迪厄场域分析](./skills/sociology-frameworks/bourdieu-field-analysis/SKILL.md)、[四圣谛诊断](./skills/religion-frameworks/four-noble-truths-framework/SKILL.md)。

---

## 使用方式

### 给人类读者
- **横向阅读**：选一个主题（如 [自我 Self](./INDEX.md#自我-self)），跨四个领域纵览不同视角。
- **纵向阅读**：从领域 README 进入流派，深度走完一个学派。
- **诊断式阅读**：遇到具体困境时，使用对应 Skill（例如个人迷茫 → [马斯洛需求诊断](./skills/psychology-frameworks/maslow-needs-diagnosis/SKILL.md)）。

### 给 AI Agent
所有 Skill 文件遵循统一 frontmatter 格式：

```yaml
---
name: <skill-id>
description: <一句话功能>
domain: <philosophy|religion|sociology|psychology>
linked: [相关条目相对路径...]
tags: [...]
---
```

可被 agent runtime（如 Claude Skills、自定义 RAG）直接索引、调用。条目之间的跨链使用相对路径与显式关联类型，便于 LLM 推理图谱。

### 示例 Prompt
> "用 [CBT 认知扭曲识别](./skills/psychology-frameworks/cbt-cognitive-distortion/SKILL.md) 分析下面这段独白：……"
>
> "把以下职场困境同时用 [马斯洛需求诊断](./skills/psychology-frameworks/maslow-needs-diagnosis/SKILL.md) 与 [布迪厄场域分析](./skills/sociology-frameworks/bourdieu-field-analysis/SKILL.md) 跑一遍。"

---

## 设计原则

1. **紧凑而非压缩** — 每条目控制在约 100 行内，但保留必要的张力与原文语境。
2. **多源验证** — 条目以原典为锚，二手研究为镜，中文资源为桥。
3. **诚实标注误读** — 每条目设"常见误读"，明确说明哪些流行说法偏离原意。
4. **关联可追溯** — 跨学科链接使用统一的关联类型标注，便于追问"为什么相关"。
5. **持续可贡献** — 模板与质量标准开放，欢迎补充传统与流派。

---

## 路线图

- ✅ **v0.1**：五领域基础骨架，每域 ~17 条目 + Skills。
- ✅ **v0.2**：六领域全面扩展 + 全球顶尖人物全量补充。80+ 思想家，60+ 概念，67 Skills。Agent 可用：JSON 索引。
- ✅ **v0.2.1（当前）**：MEDIUM 级全量补充。哲学 28 人（含德里达/莱布尼茨/罗素/波伏瓦/伽达默尔），社会学 18 人（含吉登斯/米尔斯/埃利亚斯），心理学 25 人（含埃里克森/詹姆斯/克莱因），伦理学 15 人（含诺齐克），美学 7 人（含阿多诺）。概念 61 个。
- 🔮 **v0.3**：深化现有领域，或扩展第七领域（认知科学/心灵哲学）。
- 🔮 **v0.4**：英文版、可视化关联图谱、Agent SDK 集成示例。

---

## 贡献

欢迎贡献新条目、修订误读、补充跨学科链接。请先阅读：

- [CONTRIBUTING.md](./CONTRIBUTING.md) — 贡献流程
- [meta/quality-criteria.md](./meta/quality-criteria.md) — 质量标准
- [TAGS.md](./TAGS.md) — 标签与关联类型规范
- [templates/](./templates/) — 各类型条目模板

---

## 许可

内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可，欢迎在标注来源的前提下自由使用、修改与分发。

---

## 致谢

本项目站在每位被收录思想家与无数学者的肩膀上。所列条目仅为入门指引，原典与一流二手研究永远是不可替代的。
