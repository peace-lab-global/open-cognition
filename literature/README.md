---
domain: literature
title: 文学 / Literature
description: 小说、戏剧、散文、诗歌四大文体，收录对人类思想与文明进程有深远影响的文学家
version: 1.0
entries:
  thinkers: 13
  concepts: 8
  skills: 5
---

# 文学 / Literature

## 领域定位

文学（Literature）是以语言为媒介的创造性艺术，承载人类经验、思想与价值。
本领域按文体划分为**小说家 / 剧作家 / 散文家 / 诗人**四大类，记录那些通过文学创作深刻影响人类精神世界的作家及其核心命题。

与 [aesthetics（美学）](../aesthetics/README.md) 互补：美学追问"什么是美"，文学关注"谁写出了什么、为什么重要"。
与 [arts/literary-arts（艺术/文学艺术）](../arts/README.md) 关联：本领域承载文学家条目，`arts/literary-arts` 保留为跨门类艺术对话的入口。

## 四大文体 / School Tree

> **设计说明**：其他领域的 `schools/` 按思想流派分类（如哲学按存在主义/分析哲学，心理学按精神分析/认知学派）。
> 文学领域选择按**文体**（小说/戏剧/散文/诗歌）分类，因为文学家的核心贡献与其表达形式密不可分——文体是文学思想的基本载体。
> 每位文学家的思想深度在条目内部的「时代/流派」字段中体现。

```
literature/
├── novelists/    （小说家：长篇/短篇小说、叙事艺术）
├── dramatists/   （剧作家：戏剧、舞台、人物冲突）
├── essayists/    （散文家：思想性散文、杂文、评论）
└── poets/        （诗人：诗歌、抒情、意象与形式）
```

## 条目索引 / Entries

### 小说家 / Novelists

| 条目 | 文体 | 时代/流派 | 核心命题 |
|------|------|-----------|----------|
| [陀思妥耶夫斯基](schools/novelists/dostoevsky.md) | 长篇小说 | 19 世纪 / 现实主义 | 苦难与救赎，上帝存在与否的拷问，人的深渊 |
| [卡夫卡](schools/novelists/kafka.md) | 短篇小说 | 20 世纪 / 现代主义 | 荒诞、异化、官僚迷宫，现代存在的寓言 |
| [塞万提斯](schools/novelists/cervantes.md) | 长篇小说 | 16-17 世纪 / 巴洛克 | 现代小说之父，理想与现实的张力 |
| [普鲁斯特](schools/novelists/proust.md) | 长篇小说 | 20 世纪 / 现代主义 | 意识流，非自主记忆，时间的哲学 |
| [乔伊斯](schools/novelists/joyce.md) | 长篇小说 | 20 世纪 / 现代主义 | 意识流，语言的极限实验 |

### 剧作家 / Dramatists

| 条目 | 文体 | 时代/流派 | 核心命题 |
|------|------|-----------|----------|
| [莎士比亚](schools/dramatists/shakespeare.md) | 戏剧 | 文艺复兴 | 人性的复杂光谱，命运与自由意志，语言的诗性力量 |
| [索福克勒斯](schools/dramatists/sophocles.md) | 悲剧 | 古希腊 | 命运与认知的悖论，个体良知对抗城邦法则 |
| [易卜生](schools/dramatists/ibsen.md) | 戏剧 | 19 世纪 / 现实主义 | 现代戏剧之父，社会问题剧 |
| [布莱希特](schools/dramatists/brecht.md) | 史诗剧 | 20 世纪 / 现代主义 | 间离效果，史诗剧，剧场作为社会改造 |
| [贝克特](schools/dramatists/beckett.md) | 荒诞剧场 | 20 世纪 / 后现代 | 等待与虚无，极简主义 |

### 散文家 / Essayists

| 条目 | 文体 | 时代/流派 | 核心命题 |
|------|------|-----------|----------|
| [鲁迅](schools/essayists/lu-xun.md) | 杂文/散文 | 现代 / 启蒙批判 | 国民性批判，"立人"精神，冷峻与热血的张力 |

### 诗人 / Poets

| 条目 | 文体 | 时代/流派 | 核心命题 |
|------|------|-----------|----------|
| [歌德](schools/poets/goethe.md) | 诗歌/诗剧 | 启蒙/浪漫/古典 | 浮士德精神，人性完整，自然与文化的统一 |
| [惠特曼](schools/poets/whitman.md) | 自由诗 | 19 世纪 / 浪漫主义 | 民主精神与身体性，自由诗的革新 |

## 跨域关联 / Cross-Domain Links

| 本域条目 | 关联域 | 关联条目 | 关系说明 |
|----------|--------|----------|----------|
| 陀思妥耶夫斯基 | philosophy | nietzsche.md | 存在主义先声：上帝、自由、价值重估 |
| 陀思妥耶夫斯基 | religion | salvation.md | 苦难与救赎的神学叙事 |
| 卡夫卡 | philosophy | existentialism | 荒诞与异化的文学表达 |
| 莎士比亚 | psychology | personality.md | 人物性格的复杂光谱 |
| 鲁迅 | sociology | class.md / gender.md | 社会结构与国民性批判 |
| 歌德 | aesthetics | tragedy.md | 悲剧精神与人性完整 |

## 关联 Skills

> 文学领域暂无独立 Skill 框架，相关分析请使用：
> - [荒诞分析](./skills/absurd-analysis/SKILL.md) — 卡夫卡式荒诞解析
> - [浮士德精神分析](./skills/faustian-spirit-analysis/SKILL.md) — 歌德式精神图谱
> - [苦难—救赎分析](./skills/suffering-redemption-analysis/SKILL.md) — 陀氏式苦难叙事
> - [人性分析](./skills/human-nature-analysis/SKILL.md) — 文学中的人性结构
> - [国民性批评](./skills/national-character-criticism/SKILL.md) — 鲁迅式启蒙批判

## 阅读建议

- 入门：陀思妥耶夫斯基《罪与罚》 + 卡夫卡《变形记》 + 鲁迅《呐喊》
- 进阶：莎士比亚四大悲剧 + 歌德《浮士德》
- 比较：巴赫金《陀思妥耶夫斯基诗学问题》 + 本雅明《讲故事的人》
