---
id: psychology.cognitive.friston.concepts.active-inference
title: "主动推理 · Active Inference"
type: concept
parent: psychology.cognitive.friston
thinker: Karl Friston
tags: [主动推理, 期望自由能, 行动选择, 贝叶斯决策, 强化学习]
---

# 主动推理 · Active Inference

> "Action is not a response to the world but a way of making the world conform to one's predictions."
> "行动不是对世界的反应，而是让世界符合自身预测的方式。"

---

## 定义 / Definition

主动推理（Active Inference）是弗里斯顿提出的行动理论：**行动的目标不是最大化外部奖励，而是最小化"期望自由能"（expected free energy）——即系统对未来感官状态的预测不确定性**。在主动推理框架中，智能体通过选择能够验证自身先验偏好（prior preferences）的行动序列来"让预测成真"。这将行动从传统的"最优控制"范式重新定位为贝叶斯推断过程。

Active Inference is Friston's theory of action: **the goal of action is not to maximize external reward but to minimize "expected free energy" — the predicted uncertainty about future sensory states**. In the active inference framework, agents select action sequences that confirm their prior preferences, "making predictions come true." This reframes action from the traditional "optimal control" paradigm as a Bayesian inference process.

---

## 核心机制 / Core Mechanism

### 期望自由能 / Expected Free Energy

期望自由能 G 的分解：

The decomposition of expected free energy G:

```
G = E_q[log q(s,θ) - log p(s,θ)]
  = -E_q[log p(s|θ)]    // 期望的感官数据不确定性（风险）
    + D_KL[q(θ|s) || q(θ)] // 信息增益（认知价值）
  = Risk + Ambiguity - Information Gain - Pragmatic Value
```

更直观的分解：

A more intuitive decomposition:

```
G = E_q[-log p(s|C)]      // 实用项：未来感官状态偏离偏好（C）的代价
  + E_q[-log p(s|θ)]      // 认知项：感官数据的不确定性（模糊性）
```

智能体选择行动序列 π 以最小化 G(π)：
- **实用驱动**：选择能到达偏好状态的行动（等效于奖励最大化）
- **认知驱动**：选择能减少不确定性的行动（内在动机/好奇心）

Agents select action sequences π to minimize G(π):
- **Pragmatic drive**: Select actions leading to preferred states (equivalent to reward maximization)
- **Epistemic drive**: Select actions reducing uncertainty (intrinsic motivation / curiosity)

### 行动作为推断 / Action as Inference

在主动推理中，行动不是通过求解最优控制问题得到的，而是通过推断：

In active inference, actions are not obtained by solving optimal control problems but through inference:

1. 系统维护关于"我应该处于什么状态"的先验偏好 C
2. 推断什么样的行动序列 π 最可能实现这些偏好
3. 通过最小化期望自由能来选择行动

The system maintains prior preferences C about "what states I should be in," infers what action sequences π are most likely to realize these preferences, and selects actions by minimizing expected free energy.

```
q(π) ∝ exp(-G(π))
a = argmin_π G(π)
```

这意味着**感知和行动被统一在同一个推断框架中**——感知推断外部原因，行动推断自身运动轨迹。

This means **perception and action are unified within the same inference framework** — perception infers external causes, action infers one's own motor trajectories.

### 与强化学习的比较 / Comparison with Reinforcement Learning

| 维度 | 强化学习 / RL | 主动推理 / Active Inference |
|---|---|---|
| 目标函数 | 最大化累积奖励 | 最小化期望自由能 |
| 探索策略 | 外部添加（ε-greedy等） | 内建的认知驱动（信息增益） |
| 模型需求 | 可以是model-free | 始终model-based（需要生成模型） |
| 偏好来源 | 外部奖励信号 | 先验偏好（可以是进化的或学习的） |
| 不确定性 | 通常被忽略或简化处理 | 核心考量（精确度加权） |

---

## 发展脉络 / Historical Development

- **2010**：Friston, Daunizeau et al. 发表 "Action and behavior: a free-energy formulation"——首次将行动系统性地纳入自由能框架。
- **2011**："Action understanding and active inference"——将主动推理应用于动作理解和社会认知。
- **2015**："Active inference and epistemic value"——阐明认知驱动（信息增益）在主动推理中的核心地位。
- **2017**：Friston, FitzGerald & Dolan 发表 "Active inference: A process theory"——完整的主动推理过程理论。
- **2019–2022**：Parr & Friston 开发"广义自由能"框架，将主动推理扩展到部分可观测马尔可夫决策过程（POMDP）。
- **2022**：Parr et al. 出版 *Active Inference: A Process Theory of Perception, Action, and Learning*（MIT Press）——首部系统性教科书。

- **2010**: Friston, Daunizeau et al. published "Action and behavior: a free-energy formulation" — first systematic integration of action into the free energy framework.
- **2011**: "Action understanding and active inference" — applied active inference to action understanding and social cognition.
- **2015**: "Active inference and epistemic value" — clarified the central role of epistemic drive (information gain) in active inference.
- **2017**: Friston, FitzGerald & Dolan published "Active inference: A process theory" — complete process theory of active inference.
- **2019–2022**: Parr & Friston developed the "generalized free energy" framework, extending active inference to partially observable Markov decision processes (POMDPs).
- **2022**: Parr et al. published *Active Inference: A Process Theory of Perception, Action, and Learning* (MIT Press) — first systematic textbook.

---

## 临床应用 / Clinical Applications

### 动机障碍 / Motivational Disorders

- **抑郁症**：对"行动无法改变结果"的先验过度确信→期望自由能的实用项主导（高预期代价），认知驱动被压制→行动退缩。
- **成瘾**：先验偏好被劫持（药物相关感官状态的精确度过高）→所有行动序列都指向药物获取。
- **强迫症**：对"检查行为"的先验精确度过高→无法抑制重复检查的行动推断。

### 计算精神病学 / Computational Psychiatry

主动推理为精神分裂症的"意志缺乏"（avolition）提供了计算解释：当生成模型对行动后果的预测高度不确定时，期望自由能的认知项过高，系统无法有效选择行动。

### Clinical Applications

- **Depression**: Overconfident prior that "action cannot change outcomes" → pragmatic term dominates expected free energy (high anticipated cost), epistemic drive suppressed → action withdrawal.
- **Addiction**: Prior preferences hijacked (overly high precision for drug-related sensory states) → all action sequences directed toward drug acquisition.
- **OCD**: Overly high precision for "checking behavior" priors → inability to suppress repetitive checking action inferences.
- **Computational psychiatry**: Active inference provides computational accounts of avolition in schizophrenia: when generative model predictions about action consequences are highly uncertain, the epistemic term of expected free energy becomes too high, preventing effective action selection.

---

## 关联概念 / Related Concepts

- [[free-energy-principle|自由能原理 / Free Energy Principle]]：主动推理是其行动层面的具体实现
- [[predictive-processing|预测加工 / Predictive Processing]]：主动推理中感知推断的基础
- 期望自由能（Expected Free Energy）：行动选择的目标函数
- POMDP（部分可观测马尔可夫决策过程）：主动推理的形式化决策框架
- 强化学习（Reinforcement Learning）：主动推理的贝叶斯替代方案
- 内在动机（Intrinsic Motivation）：主动推理中认知驱动的心理学对应

---

## 东西方对话 / East-West Dialogue

### 佛学·业（Karma）/ Buddhism · Karma

主动推理中的"行动让预测成真"与佛学的"业"概念形成有趣对话：如果行动是由先验信念（saṃskāra，行）驱动的，而行动又反过来塑造未来感官经验，那么这构成了一个与"业力循环"高度相似的反馈环。修行的核心——改变"行"（先验信念）——对应于主动推理中修改生成模型的先验结构。

The idea in active inference that "action makes predictions come true" creates interesting dialogue with the Buddhist concept of karma: if action is driven by prior beliefs (saṃskāra, volitional formations) and action in turn shapes future sensory experience, this constitutes a feedback loop highly analogous to "karmic cycling." The core of practice — changing volitional formations (prior beliefs) — corresponds to modifying the prior structure of the generative model in active inference.

### 儒学·格物致知 / Confucianism · Investigating Things

主动推理中的认知驱动（information gain）可以被解读为"格物致知"的计算版本：主动探索世界以获取知识本身就是有价值的行为，不仅是为了实用目的。这与儒学将"学"和"知"视为内在美德的传统一致。

The epistemic drive (information gain) in active inference can be read as a computational version of "investigating things to extend knowledge": actively exploring the world to acquire knowledge is inherently valuable, not merely for pragmatic purposes. This aligns with the Confucian tradition of treating "learning" and "knowledge" as intrinsic virtues.

---

## 进阶阅读 / Further Reading

- Friston, K. et al. (2010). "Action and behavior: a free-energy formulation." *Biological Cybernetics*, 102, 227–260.
- Friston, K. et al. (2017). "Active inference: A process theory." *Neural Computation*, 29(1), 1–49.
- Parr, T. & Friston, K. (2019). "Generalised free energy and active inference." *Biological Cybernetics*, 113, 493–511.
- Parr, T. et al. (2022). *Active Inference: A Process Theory of Perception, Action, and Learning*. MIT Press.
- Pezzulo, G. et al. (2018). "Active inference, body schema and body image." *Neuroscience & Biobehavioral Reviews*, 90, 394–407.
