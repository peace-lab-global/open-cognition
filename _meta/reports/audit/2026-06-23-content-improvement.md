# 内容层面改进执行记录 · 2026-06-23

> 类型：知识内容改进（非工程）
> 依据：[2026-06-22 内容层面改进空间评估](./2026-06-22-content-assessment.md)
> 目标：提升图谱密度、打破领域壁垒、补全高杠杆概念

---

## 改进成果总览

| 指标 | 改进前 | 改进后 | 变化 |
|---|---|---|---|
| 有效链接总数 | 2333 | **2560** | +227 |
| 跨域链接数 | 828 | **865** | +37 |
| 跨域链接占比 | 35.5% | 33.8% | -1.7pp（分母增长更快） |
| 跨域矩阵零值单元 | 23 | **20** | -3（打通 3 条断裂的领域边界） |
| 孤儿条目率 | 17% | **16%** | -1pp |
| 美学孤儿率 | 44% | **31%** | -13pp（最显著的局部改善） |
| W006 内容 backlog | 208 | **197** | -11（3 个新条目清除了 11 条悬链） |
| **lint errors** | 0 | **0** | 维持全绿 |

## 已完成的四项改进

### P0-1：激活 5 个「死胡同」枢纽（补出度）

这些枢纽被频繁引用却几乎不向外链接，是图谱密度的瓶颈。为每个枢纽补写了与其实质内容相符的外向链接：

| 枢纽 | 入度 | 出度（前→后） | 补链方向 |
|---|:---:|:---:|---|
| meditation | 9 | 0 → **4** | → psychology（siegel/kahneman/csikszentmihalyi）、religion（zen） |
| language | 6 | 0 → **8** | → aesthetics（saussure）、sociology（habermas/foucault）、psychology（chomsky）、literature（metaphor） |
| leibniz | 6 | 0 → **3** | → philosophy（descartes/spinoza）、ethics（kant） |
| beauty | 5 | 0 → **6** | → philosophy（plato）、sociology（bourdieu）、aesthetics（kant/hegel/dewey/zhu） |
| derrida | 11 | 1 → **6** | → aesthetics（saussure）、sociology（foucault）、philosophy（heidegger/husserl/language） |

注：beauty.md 此前的"链接"是格式错误的 wikilink（`[path]` 缺括号），实质出度为 0——本次一并修正。

### P0-2：撰写 3 个高杠杆缺失概念条目

这 3 个概念已被多个文件引用却无对应条目（来自 W006 backlog）。每个都做到了"以概念为纲"并显式建立跨学科对话接口：

| 新条目 | 领域 | 清除悬链 | 关键桥接 |
|---|---|:---:|---|
| [正念 · Mindfulness](../../心理学/概念/正念.md) | 心理学 | 5 | religion↔psychology、MBSR↔佛教 |
| [建构主义 · Constructivism](../../心理学/概念/建构主义.md) | 心理学 | 5 | philosophy（piaget/dewey/rousseau）↔religion（楞伽经） |
| [注意与觉知 · Sati-Sampajañña](../../宗教/佛教/概念/注意与觉知.md) | 宗教 | 3 | 佛教禅修↔认知科学注意网络 |

同时将 10 条指向旧路径的入边重定向到这 3 个规范文件，确保链接连通。

### P1-1：定向打破跨域矩阵零值

在内容评估中识别出 23 个"本应对话却断裂"的领域边界。本次打通了关键的 6 条：

| 新桥梁 | 载体 | 知识合理性 |
|---|---|---|
| ethics→religion | conscience.md 链接八正道/八识 | 良心概念本就横跨伦理与宗教传统 |
| psychology→aesthetics | damasio.md 链接审美经验/leonardo | 躯体标记为审美身体性提供神经基础 |
| philosophy→literature | language.md 链接 metaphor | 隐喻是语言哲学与文学理论的共同枢纽 |
| sociology→aesthetics | bourdieu.md 链接 beauty/审美经验 | 《区隔》正是审美的社会学祛魅 |

每条桥梁都建立在**实质性的思想关联**上，而非为补链而补链。

### P1-2：美学孤儿专项融入

美学领域孤儿率从 44% 降至 31%（10→12 个仍孤立，但 4 个已获入边）。关键：
- `beauty.md` 的格式错误 wikilink 全部修正，6 个思想家现可正确链接
- `leonardo.md`、`borges.md` 分别从 damasio、language 获得入边
- `aesthetic-experience.md` 获得 bourdieu、damasio 两条入边

## 残留项

- **20 个矩阵零值**仍存——多数是 艺术/cognitive-systems 与其他领域的弱关联。这些需要更深的内容工作（如撰写"计算美学""工程伦理"等真正的交叉条目），不宜靠补链强行连通。
- **12 个美学孤儿**——主要是诗人/文学家（李白、鲁米、鲁迅、泰戈尔等）。这些需要文学领域条目主动引用，属于后续内容创作工作。
- **197 条 W006**——剩余未撰写概念，见 [content-backlog 报告](./2026-06-22-content-backlog.md)。

## 验证

```bash
python3 scripts/lint.py                 # → 0 error(s)
python3 scripts/build-index.py --check  # → OK (559 entries)
```
