# 标签词典 · TAGS

本词典定义全库统一的四维标签体系。所有条目 frontmatter 中的 `tags` 字段必须从此清单中选取，避免冗余与拼写差异。

---

## 维度 1：领域 Domain

| 标签 | 含义 |
|---|---|
| `philosophy` | 哲学 |
| `religion` | 宗教 |
| `sociology` | 社会学 |
| `psychology` | 心理学 |
| `cognitive-systems` | 认知系统工程 |
| `literature` | 文学 |
| `art` | 艺术 |
| `aesthetics` | 美学 |
| `science` | 科学史与科学哲学 |

## 维度 2：流派 School

### 哲学 (Philosophy)
`presocratic` `classical-greek` `hellenistic` `stoicism` `epicureanism` `ancient-skepticism` `neoplatonism` `patristic-philosophy` `medieval-scholastic` `rationalism` `empiricism` `enlightenment` `scottish-common-sense` `german-idealism` `utilitarianism` `marxism` `existentialism` `phenomenology` `pragmatism` `analytic` `logical-positivism` `structuralism` `post-structuralism` `philosophy-of-language` `philosophy-of-mind` `philosophy-of-science` `political-philosophy` `feminist-philosophy` `environmental-philosophy` `liberalism` `conservatism` `social-contract` `anarchism` `classical-political-economy` `keynesianism` `neoliberalism` `nationalism` `postcolonialism` `communitarianism` `critical-theory` `confucian` `daoist` `buddhist-philosophy`

### 宗教 (Religion)
`buddhism-theravada` `buddhism-mahayana` `buddhism-zen` `christianity-catholic` `christianity-protestant` `christianity-orthodox` `christianity-mysticism` `islam-sunni` `islam-shia` `sufism` `judaism-rabbinic` `judaism-kabbalah` `hinduism-vedanta` `taoism-religious` `taoism-philosophical` `sikhism` `shinto` `confucianism-religious` `comparative-mythology`

### 社会学 (Sociology)
`functionalism` `conflict-theory` `symbolic-interactionism` `structuralism` `post-structuralism` `critical-theory` `phenomenological-sociology` `network-theory` `world-systems` `modernity`

### 心理学 (Psychology)
`psychoanalysis` `analytical-psychology` `individual-psychology` `behaviorism` `gestalt-psychology` `functionalism` `cognitive` `humanistic` `existential-psychology` `positive-psychology` `cognitive-behavioral` `developmental` `attachment-theory` `evolutionary-psychology` `social-psychology`

### 认知系统工程 (Cognitive Systems Engineering)
`cybernetics` `ecological-psychology` `distributed-cognition` `activity-theory` `cognitive-engineering` `human-factors` `naturalistic-decision` `resilience-engineering` `cognitive-ergonomics` `embodied-cognition` `4E-cognition` `predictive-processing` `enactivism` `systems-thinking` `safety-science` `safety-II` `automation-sociotechnical` `sociotechnical-systems` `human-automation-interaction` `perrow` `leveson` `endsley` `sheridan` `wickens`

### 文学 (Literature)
`classical-literature` `medieval-literature` `renaissance-literature` `romanticism` `realism` `naturalism` `symbolism` `modernism` `absurdism` `existentialist-literature` `magical-realism` `postmodern-literature` `war-poetry` `transcendentalism` `russian-literature` `bengal-renaissance` `aestheticism` `german-literature` `experimental-music`

### 艺术 (Art)
`renaissance-art` `baroque` `neoclassicism` `romanticism-art` `realism-art` `impressionism` `post-impressionism` `expressionism` `cubism` `futurism` `dada` `surrealism` `abstract-expressionism` `pop-art` `minimalism` `conceptual-art` `performance-art`

### 美学 (Aesthetics)
`classical-aesthetics` `german-aesthetics` `romantic-aesthetics` `pragmatist-aesthetics` `phenomenological-aesthetics` `critical-aesthetics` `chinese-aesthetics`

### 科学史与科学哲学 (History & Philosophy of Science)
`scientific-revolution` `history-of-science` `philosophy-of-science` `scientific-realism` `social-construction-of-science`

### 伦理政治 (Ethics & Political Philosophy)
`nonviolent-resistance` `civil-rights-movement` `political-philosophy` `social-contract` `virtue-ethics` `feminist-theory`

## 维度 3：时代 Era

| 标签 | 范围 |
|---|---|
| `ancient` | 公元前到公元 5 世纪 |
| `medieval` | 5 世纪到 15 世纪 |
| `early-modern` | 16 世纪到 18 世纪 |
| `modern` | 19 世纪到 20 世纪初 |
| `contemporary` | 20 世纪至今 |

## 维度 4：主题 Theme

跨学科横向主题，用于 INDEX.md 横向索引：

`epistemology` `ethics` `metaphysics` `ontology` `aesthetics` `political` `power` `self` `consciousness` `unconscious` `meaning` `suffering` `death` `freedom` `community` `language` `body` `time` `truth` `god-divine` `salvation` `liberation` `ritual` `sacred-profane` `social-structure` `social-action` `culture` `class` `gender` `modernity` `rationality` `motivation` `emotion` `cognition` `development` `personality` `therapy` `wellbeing` `direct-cognition` `bounded-rationality` `affordance` `cognitive-load` `situation-awareness` `distributed-cognition` `sensemaking` `mental-model` `resilience` `joint-cognitive-system` `predictive-processing` `enaction` `human-error` `system-design` `feedback` `autopoiesis` `macrocognition` `team-cognition` `distributed-SA` `situated-cognition` `safety-paradigm` `drift-into-failure` `normal-accidents` `safety-culture` `automation-bias` `automation-paradox` `out-of-the-loop` `ecological-interface-design` `cognitive-task-analysis` `just-culture` `human-reliability` `multiple-resources` `automation-autonomy` `STAMP` `STPA` `SAGAT` `supervisory-control`

---

## 关联类型 Relation Types

跨条目互链时，必须在链接旁注明关联类型：

| 标记 | 含义 | 示例 |
|---|---|---|
| `[同源]` | 思想直接继承 | 阿德勒 [同源] 弗洛伊德 |
| `[互补]` | 不同视角解释同一现象 | 佛教苦谛 [互补] 存在主义焦虑 |
| `[对立]` | 立场相反 | 行为主义 [对立] 人本主义 |
| `[发展]` | 后者发展前者 | 新弗洛伊德主义 [发展] 弗洛伊德 |
| `[批判]` | 后者批判前者 | 福柯 [批判] 启蒙理性 |
| `[平行]` | 独立形成相似洞见 | 庄子 [平行] 维特根斯坦语言观 |

---

## 使用规范

1. 每条目 frontmatter 必须至少包含一个领域标签、一个流派标签、一个时代标签和 1–3 个主题标签。
2. 不允许在 frontmatter 中创造未登记标签；如需新增，先在本文件登记。
3. 大小写统一为小写，多词用连字符 `-`。

---

## 维度 5：系列／频道 Series / Channel

用于清单类条目的内容系列标识，与学术维度并列但不做强制要求。

| 标签 | 含义 |
|---|---|
| `没用的清单` | 「没用的清单」自媒体频道 |
| `严肃系列` | 「严肃系列」思想史主干盘点 |
| `东西方对话` | 「东西方对话」跨文明主题盘点 |
