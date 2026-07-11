---
id: psychology.cognitive.friston.concepts.predictive-processing
title: "预测加工 · Predictive Processing"
type: concept
parent: psychology.cognitive.friston
thinker: Karl Friston
tags: [预测编码, 预测误差, 感知, 皮层层级, 贝叶斯推断]
aliases: [预测编码, Predictive Coding]
---

# 预测加工 · Predictive Processing

> "Perception is not a passive reception of information but an active process of hypothesis testing."
> "感知不是被动的信息接收，而是主动的假设检验过程。"

---

## 定义 / Definition

预测加工（Predictive Processing, PP）是一种关于大脑信息处理架构的理论：**大脑不是被动接收感官输入然后逐级加工，而是在层级结构中主动生成自上而下的预测，只向上传递预测误差（prediction error）——即实际输入与预测之间的差值**。这一理论由弗里斯顿在2003–2006年间系统发展，继承自Helmholtz的"无意识推断"概念和Rao & Ballard（1999）的视觉皮层预测编码模型。

Predictive Processing (PP) is a theory about the brain's information processing architecture: **the brain does not passively receive sensory input and process it bottom-up, but actively generates top-down predictions within a hierarchical structure, passing upward only prediction error — the difference between actual input and prediction**. This theory was systematically developed by Friston between 2003–2006, inheriting from Helmholtz's concept of "unconscious inference" and Rao & Ballard's (1999) predictive coding model of visual cortex.

---

## 核心机制 / Core Mechanism

### 层级预测编码架构 / Hierarchical Predictive Coding Architecture

大脑皮层被建模为多层级的生成模型：

The cortex is modeled as a multi-level generative model:

```
高层（High Level）: 抽象/慢速因果推断
    ↓ 预测信号（predictions）
中层（Mid Level）: 中等抽象
    ↓ 预测信号 / ↑ 预测误差
低层（Low Level）: 具体/快速感官特征
    ↑ 预测误差（prediction errors）
感官输入（Sensory Input）
```

每一层 i 维护关于隐藏状态 θ_i 的概率表征：
- 向下发送对第 i-1 层输入的预测 μ_i
- 接收第 i-1 层传上来的预测误差 ε_{i-1}
- 使用预测误差更新自身的后验信念

Each level i maintains a probabilistic representation of hidden states θ_i:
- Sends predictions μ_i downward about level i-1's input
- Receives prediction errors ε_{i-1} from level i-1
- Uses prediction errors to update its own posterior beliefs

### 预测误差的角色 / Role of Prediction Error

预测误差 ε = s - μ（感官输入减去预测）是驱动系统更新的唯一上行信号：

- **小误差** → 预测被确认，无需更新（对应神经科学中的"重复抑制"现象）
- **大误差** → 预测失败，需要更新高层信念（对应"失配负波" MMN）
- **持续误差** → 触发模型结构的长期修改（学习与可塑性）

Prediction error ε = s - μ (sensory input minus prediction) is the sole upward signal driving system updates:

- **Small error** → prediction confirmed, no update needed (corresponds to "repetition suppression" in neuroscience)
- **Large error** → prediction failed, higher-level beliefs need updating (corresponds to "mismatch negativity" MMN)
- **Persistent error** → triggers long-term model structure modification (learning and plasticity)

### 精确度加权 / Precision Weighting

并非所有预测误差都同等重要——系统根据每个预测误差通道的"精确度"（precision，即可靠性的逆方差）对其加权：

- **高精确度**（高可靠性）→ 误差信号被放大 → 注意力集中于此
- **低精确度**（低可靠性）→ 误差信号被抑制 → 注意力忽略

这一机制被弗里斯顿视为**注意力的计算本质**：注意力就是精确度加权的过程。

Not all prediction errors are equally important — the system weights each prediction error channel by its "precision" (inverse variance, i.e., reliability):

- **High precision** (high reliability) → error signal amplified → attention focused here
- **Low precision** (low reliability) → error signal suppressed → attention ignores

Friston views this mechanism as **the computational essence of attention**: attention is the process of precision weighting.

---

## 发展脉络 / Historical Development

### 前身 / Precursors

- **Helmholtz (1867)**：感知是"无意识推断"——大脑基于先验知识对感官数据做出最佳猜测。
- **Gregory (1980)**：感知是"假设检验"过程，视错觉是"错误假设"的结果。
- **Rao & Ballard (1999)**：在视觉皮层V1中实现预测编码的计算模型。
- **Mumford (1992)**：提出皮层层级作为层级生成模型的构想。

### 弗里斯顿的系统化 / Friston's Systematization

- **2003**："Functional integration and regression in the cortical hierarchy"——将预测编码与层级皮层结构联系。
- **2005**："A theory of cortical responses"——系统阐述皮层预测编码的变分贝叶斯框架。
- **2006**：纳入自由能原理的统一框架。
- **2010s**：与Clark、Hohwy等哲学家合作，将预测加工扩展为全面的认知科学范式。

### Precursors

- **Helmholtz (1867)**: Perception as "unconscious inference" — the brain makes best guesses about sensory data based on prior knowledge.
- **Gregory (1980)**: Perception as "hypothesis testing," visual illusions as results of "wrong hypotheses."
- **Rao & Ballard (1999)**: Computational model implementing predictive coding in visual cortex V1.
- **Mumford (1992)**: Proposed the cortex hierarchy as a hierarchical generative model.

### Friston's Systematization

- **2003**: "Functional integration and regression in the cortical hierarchy" — linked predictive coding to hierarchical cortical structure.
- **2005**: "A theory of cortical responses" — systematically articulated the variational Bayesian framework for cortical predictive coding.
- **2006**: Integrated into the unified framework of the free energy principle.
- **2010s**: Collaborated with philosophers Clark, Hohwy, etc., expanding predictive processing into a comprehensive cognitive science paradigm.

---

## 临床应用 / Clinical Applications

### 感知异常 / Perceptual Abnormalities

- **幻觉（Hallucinations）**：预测信号过度主导感知——先验精确度过高，感官误差被压制。弗里斯顿的"幻听"实验证明，对语音的先验期望可以在没有声音的情况下产生听觉体验。
- **视错觉**：预测模型的系统偏差导致的"正常"预测失败——如大小恒常性错觉。

### 注意障碍 / Attention Disorders

- **焦虑症**：对威胁相关预测误差的精确度过度加权→对威胁信号的过度关注（注意偏向）。
- **ADHD**：精确度加权的全局失调→无法持续将注意力集中在任务相关的预测误差上。

### Clinical Applications

- **Hallucinations**: Prediction signals overdominate perception — overly high prior precision suppresses sensory errors. Friston's "hallucination" experiments demonstrate that prior expectations of speech can generate auditory experience without sound.
- **Visual illusions**: Systematic biases in predictive models cause "normal" prediction failures — such as size constancy illusions.
- **Anxiety disorders**: Overweighting precision of threat-related prediction errors → excessive attention to threat signals (attentional bias).
- **ADHD**: Global dysregulation of precision weighting → inability to sustain attention on task-relevant prediction errors.

---

## 关联概念 / Related Concepts

- [[free-energy-principle|自由能原理 / Free Energy Principle]]：预测加工是其感知层面的具体实现
- [[active-inference|主动推理 / Active Inference]]：预测加工在行动领域的延伸
- [[hierarchical-inference|层级推断 / Hierarchical Inference]]：预测加工的层级结构基础
- 重复抑制（Repetition Suppression）：预测编码的神经影像学证据
- 失配负波（Mismatch Negativity, MMN）：预测误差的脑电证据
- 精确度加权（Precision Weighting）：注意力作为预测误差可靠性调节

---

## 东西方对话 / East-West Dialogue

### 佛学·唯识学 / Buddhism · Yogācāra

预测加工与唯识学的"三界唯心，万法唯识"主张形成深层对话：如果感知从来不是对"原始现实"的直接接触，而始终是模型驱动的建构，那么"外境"（外部世界的独立存在性）在认知上确实无法被直接验证。唯识学的"识转变"（vijñāna-parināma）可以被解读为生成模型的推断过程——八识系统 ≈ 多层级生成模型的推断层级。

Predictive processing creates deep dialogue with Yogācāra Buddhism's assertion that "the three realms are mind-only": if perception is never direct contact with "raw reality" but always model-driven construction, then the independent existence of "external objects" is indeed unverifiable at the cognitive level. Yogācāra's "consciousness transformation" (vijñāna-parināma) can be read as generative model inference — the eight consciousnesses system ≈ inference levels of a multi-level generative model.

### 认知科学与东方禅修 / Cognitive Science and Eastern Meditation

禅修训练可以被理解为对预测加工过程的元认知觉察：正念（mindfulness）练习者学会观察自己的感知是如何被先验信念塑造的，并逐步区分"预测"与"预测误差"——这本质上是对推断过程本身的觉察。

Meditative training can be understood as developing metacognitive awareness of the predictive processing process: mindfulness practitioners learn to observe how their perception is shaped by prior beliefs, and gradually distinguish "predictions" from "prediction errors" — this is essentially awareness of the inference process itself.

---

## 进阶阅读 / Further Reading

- Friston, K. (2005). "A theory of cortical responses." *Philosophical Transactions of the Royal Society B*, 360, 815–836.
- Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences*, 36, 181–204.
- Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press.
- Clark, A. (2016). *Surfing Uncertainty: Prediction, Action, and the Embodied Mind*. Oxford University Press.
- Keller, G. B. & Mrsic-Flogel, T. D. (2018). "Predictive processing: A canonical theory of sensory computation." *Current Opinion in Neurobiology*, 52, 117–125.
