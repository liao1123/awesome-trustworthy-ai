# 奖励作弊

## 研究方向

奖励作弊研究模型在优化代理奖励时，是否会利用奖励函数、验证器或跨模态信息缺口获得高分，却偏离真实任务目标；重点包括现象测量、诱因定位、不同强化学习算法的风险差异以及可靠奖励设计。

## 研究脉络

- **机制分析：** 一条研究路线定位 preference optimization 中 proxy reward 偏离真实目标的原因与训练动态。
- **任务扩展：** 另一条路线把 reward hacking 扩展到多模态 RL 与真实 ML-agent repository。
- **评测组织：** 由于机制研究与任务级失效关注点不同，本页将专门 benchmark 与普通分析工作分开记录。

## 机制与跨模态风险分析

### 1. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

📄 [arXiv](https://arxiv.org/abs/2608.22915)　📅 2026-08

**关键词**：`analysis`、`safety proxy`、`feasible-set contamination`、`guard composition`、`safety hacking`、`proxy constraint`

👤 **作者**：Akifumi Wachi、Takumi Tanabe、Youhei Akimoto

- 🎯 **研究动机**：推理时管线先采样 N 个输出、经学习安全 proxy 过滤再返回奖励最高者，这一组合的安全风险未被刻画
- 🔬 **研究方法**：定义 safety hacking（通过学习约束但违反真实安全准则的选择），对 constrained Best-of-N 推导由 proxy-feasible 集内安全/不安全输出联合上奖励尾支配的有限 N 界，并提出 χ² 有界覆盖控制与 constrained pessimistic sampling
- 📌 **结论**：不安全但可行的输出尾部更重时，N 增大 safety hacking 渐近必然，即使 proxy 误差任意小；覆盖控制只能限制放大、无法修复被污染的可行集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety criterion. For constrained Best-of-$N$ sampling, we derive finite-$N$ bounds governed by the joint upper reward tails of safe and unsafe outputs within the proxy-feasible set. If unsafe-but-feasible outputs have the heavier tail, safety hacking becomes asymptotically certain as $N$ grows, even when false-positive mass and average safety- and reward-proxy errors are arbitrarily small. We also show that policies within a bounded $χ^2$ divergence from the proxy-feasible reference distribution admit an $N$-independent safety-hacking bound, and instantiate this general coverage-control principle with constrained pessimistic sampling. Coverage control limits amplification but cannot repair a contaminated feasible set: admitted unsafe outputs may still be favored, and regularized selection is not necessarily safer than constrained Best-of-$N$ for every reward proxy. Toy and language-model experiments characterize both contamination and its reward-tail amplification, which exposes an inherent difficulty in inference-time scaling with learned safety models.

</details>

### 2. Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

📄 [arXiv](https://arxiv.org/abs/2608.20011)　📅 2026-08

**关键词**：`analysis`、`preference optimization`、`manifold drift`

👤 **作者**：Yansen Han、Shengyi Liao、Yuanxing Zhang、Pengfei Wan、Tao Lin

- 🎯 **研究动机**：流匹配的奖励驱动更新无数据流形约束，终端样本可漂移出预训练支撑（manifold drift）
- 🔬 **研究方法**：理论证明偏好更新诱导的终端位移有非零法向分量即离开流形；ThermoDPO 温度控制目标把成对偏好优化锚定在偏好样本，连接拒绝采样微调与 FlowDPO，另加加权变体
- 📌 **结论**：玩具基准上 ThermoDPO-weighted 达 StrictScore 0.899 对 FlowDPO 的 0.629；SD3.5-M CFG=4.5 下 OCR 提升 47.5%、四指标平均升 16.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the pretrained support. We formalize this failure mode as manifold drift. Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a preference update leaves the pretrained manifold whenever its induced terminal displacement has a nonzero normal component. As a remedy, we propose ThermoDPO, a temperature-controlled objective that anchors pairwise preference optimization on preferred samples. Across temperature regimes, this objective connects rejection sampling fine-tuning and FlowDPO and controls a pointwise reconstruction-based surrogate for manifold distance. To counteract diminished signals at low temperatures, we further introduce a weighted variant, ThermoDPO-weighted. On the main toy benchmark, ThermoDPO-weighted attains a StrictScore of 0.899, compared with 0.629 for FlowDPO and 0.857 for FlowDPO+RFT. On SD3.5-M at CFG = 4.5, it improves OCR by 47.5% and the average of four metrics by 16.0%.

</details>

### 3. Debate Training Reduces Reward Hacking in RLAIF

📄 [arXiv](https://arxiv.org/abs/2608.17776)　📅 2026-08

**关键词**：`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`

👤 **作者**：Zachary Kenton、…、Rohin Shah

- 🎯 **研究动机**：RLAIF 中策略学会利用 AI judge 的系统误差（reward hacking），judge 弱于策略时最严重
- 🔬 **研究方法**：在数学任务上以辩论（生成器对批评家、更弱 judge 裁决）替代单人 RLAIF，训练 Gemini 2.5 Flash 级策略并冻结更弱 Flash Lite judge
- 📌 **结论**：基线快速 hack judge 而辩论全程维持 judge 性能，峰值验证准确率恢复 45% 差距并持续多个 RL 步；批评家字数限制（150 词内有效）平衡博弈避免 critic 侧 judge-hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting most relevant to overseeing increasingly capable AI systems. We study mathematics tasks, where final-answer correctness is verifiable, allowing us to measure reward hacking dynamics. We train a Gemini~2.5 Flash-class policy with a frozen, weaker Gemini~2.5 Flash Lite judge, comparing a single-player RLAIF baseline against debate. While the baseline quickly hacks the judge, debate maintains judge performance throughout training, leading to a higher peak validation accuracy (45\% performance gap recovered) that persists through many RL steps. Additional experiments show that: 1) further weakening the judge leads to faster hacking, but this can be compensated by adding an additional debate round; 2) debate incentives override prompted misalignment; 3) RL using an LLM judge has a smaller train/validation reward gap than RL from verifiable rewards; 4) learning to critique to convince the judge using ground truth labels is possible but slow. Taken together, our results are a positive update on the feasibility of debate, while highlighting that balancing multi-agent training is critical: without player constraints, adversarial training risks defaulting to critic judge-hacking. We show that critique word limits (effective up to 150 words) successfully balance the game and avoid judge hacking, though this introduces a trade-off by restricting critic expressive clarity.

</details>

### 4. Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization

📄 [arXiv](https://arxiv.org/abs/2608.15445)　📅 2026-08

**关键词**：`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`

👤 **作者**：Suyash Maniyar、Armaan Sandhu、Abhishek Mishra

- 🎯 **研究动机**：训练分布上的端点准确率无法区分真正解题与利用表面特征（目标误泛化）
- 🔬 **研究方法**：在正确答案恒为 A 的选择题上用 GRPO 训练，再在无偏位置测试集评测；用数值抽取与 LLM judge 跟踪推理-答案解耦
- 📌 **结论**：偏置训练使小模型 A 率超 0.90 且无偏准确率崩向随机；能力强的模型推理算对仍选 A（解耦率约 0.66）；偏置泛化到 OOD MMLU，无偏再训练仅部分逆转

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a reward is correct on every training example yet consistent with more than one goal, a model can acquire an unintended one, a failure known as goal misgeneralization. Endpoint accuracy on the training distribution cannot tell the two apart, because solving the task and exploiting a surface feature can satisfy the reward equally well. We treat this as a measurement problem: what does a benchmark score measure once a model has been optimized against a correct but confounded signal? We train language models with GRPO on multiple-choice math problems where the correct answer is always option A, then evaluate on an unseen test set with unbiased answer positions. Across Qwen2.5, Llama 3.x and Gemma-3 models, biased training often drives option-A rates above 0.90 in smaller models and collapses unbiased accuracy toward chance, so accuracy stops measuring math ability and instead measures an answer-position policy. We further find reasoning-answer decoupling: capable models generate reasoning that reaches the correct numeric answer while still selecting A. We track this with numeric extraction and an LLM judge (GPT-4.1-mini; Qwen2.5-3B decoupling rate is about 0.66). The broken construct generalizes beyond the training domain: biased models inflate A-rates on out-of-domain MMLU and value-laden prompts. Continued training on unbiased data reverses the in-domain shift unevenly and only partially reverses the out-of-domain one, so a model can appear restored on its training distribution while remaining biased on unseen inputs. Reasoning-answer decoupling rate, together with answer distributions and out-of-domain behavior, separates capability loss from a learned, transferable shortcut.

</details>

### 5. Multimodal Reward Hacking in Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2607.09492)　📅 2026-07

**关键词**：`analysis`、`multimodal RL`、`multimodal reward`、`reinforcement learning`

👤 **作者**：Jiayu Yao、…、Shenghua Liu

- 🎯 **研究动机**：MLLM 的 RL 对齐中更高奖励不一定代表更好任务表现，视觉证据由纯文本或弱接地奖励评估时风险放大
- 🔬 **研究方法**：跨安全 VQA、图表 VQA 与压力测试研究奖励设计、数据歧义、模型规模（2B-32B）与算法（GRPO/RLOO/DAPO），引入 Newly Rewarded Failure Rate 度量代理奖励改善样本中的新失败
- 📌 **结论**：仅结果奖励致 48.1% 奖励作弊率且 RL 制造新失败；32B 在仅结果奖励下仍差 54.9%，答案感知奖励在各规模改善趋势；关键词检查加剧作弊而 VLM-as-judge 降低之

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) is increasingly used to align multimodal large language models (MLLMs), but higher rewards do not always imply better task performance. This risk is amplified when visual evidence is evaluated by text-only or weakly grounded rewards. We study reward hacking in MLLM RL across safety VQA, chart VQA, and stress-test settings, varying reward design, data ambiguity, model scale (2B-32B), and RL algorithm (GRPO, RLOO, DAPO). We introduce Newly Rewarded Failure Rate (NRFR), which measures failures among samples whose proxy reward improves over the SFT baseline. Outcome-only rewards cause severe hacking, reaching 48.1% Reward Hacking Rate (RHR), while NRFR exceeding RHR shows that RL creates new failures rather than merely inheriting them. Scaling reduces but does not eliminate hacking: even the 32B model retains a 54.9% worse rate under outcome-only rewards, whereas answer-aware rewards improve the oracle trend at every scale. Robustness is also algorithm- and scale-dependent: GRPO is consistently most resistant, RLOO remains vulnerable, and DAPO improves substantially from 2B to 8B. Visual-evidence rewards help only with reliable verification: keyword-based checks increase hacking, while VLM-as-judge semantic verification reduces it. Overall, multimodal reward hacking is a systematic result of optimizing imperfect rewards, and robust alignment requires rewards and verifiers that remain reliable under optimization pressure.

</details>

### 6. Real-Time Aligned Reward Model beyond Semantics

📄 [arXiv](https://arxiv.org/abs/2601.22664) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60748)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`reinforcement learning`、`preference optimization`

👤 **作者**：Zixuan Huang、…、Deqing Wang

- 🎯 **研究动机**：RLHF 中奖励模型易被过优化，现有缓解依赖表层语义信息，无法应对策略分布持续漂移造成的 RM-策略失配
- 🔬 **研究方法**：提出轻量框架 R2M：超越仅依赖预训练 LLM 语义表示的奖励模型，利用策略演化中的隐藏状态（策略反馈）实时对齐策略分布变化
- 📌 **结论**：实验表明实时利用策略反馈可随 RL 过程改善奖励模型表现，缓解奖励失配

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) is a pivotal technique for aligning large language models (LLMs) with human preferences, yet it is susceptible to reward overoptimization, in which policy models overfit to the reward model, exploit spurious reward patterns instead of faithfully capturing human intent. Prior mitigations primarily relies on surface semantic information and fails to efficiently address the misalignment between the reward model (RM) and the policy model caused by continuous policy distribution shifts. This inevitably leads to an increasing reward discrepancy, exacerbating reward overoptimization. To address these limitations, we introduce R2M (Real-Time Aligned Reward Model), a novel lightweight RLHF framework. R2M goes beyond vanilla reward models that solely depend on the semantic representations of a pretrained LLM. Instead, it leverages the evolving hidden states of the policy (namely policy feedback) to align with the real-time distribution shift of the policy during the RL process. This work points to a promising new direction for improving the performance of reward models through real-time utilization of feedback from policy models.

</details>

### 7. Probing RLVR Training Instability through the Lens of Objective-Level Hacking

📄 [arXiv](https://arxiv.org/abs/2602.01103) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64695)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`reinforcement learning`、`preference optimization`

👤 **作者**：Yiming Dong、…、Zheng Wang

- 🎯 **研究动机**：RLVR 长程训练尤其 MoE 架构上易不稳定，成因与机制理解不足
- 🔬 **研究方法**：提出 objective-level hacking 框架（源于 token 级信用错配而非可利用 verifier），在 30B MoE 模型上追踪训练-推理差异异常增长的起源并形式化其机制
- 📌 **结论**：给出 MoE 不稳定背后训练动态的具体因果解释，指导稳定 RLVR 算法设计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prolonged reinforcement learning with verifiable rewards (RLVR) has been shown to drive continuous improvements in the reasoning capabilities of large language models, but the training is often prone to instabilities, especially in Mixture-of-Experts (MoE) architectures. Training instability severely undermines model capability improvement, yet its underlying causes and mechanisms remain poorly understood. In this work, we introduce a principled framework for understanding RLVR instability through the lens of objective-level hacking. Unlike reward hacking, which arises from exploitable verifiers, objective-level hacking emerges from token-level credit misalignment and is manifested as system-level spurious signals in the optimization objective. Grounded in our framework, together with extensive experiments on a 30B MoE model, we trace the origin and formalize the mechanism behind a key pathological training dynamic in MoE models: the abnormal growth of the training-inference discrepancy, a phenomenon widely associated with instability but previously lacking a mechanistic explanation. These findings provide a concrete and causal account of the training dynamics underlying instabilities in MoE models, offering guidance for the design of stable RLVR algorithms.

</details>

### 8. Factored Causal Representation Learning for Robust Reward Modeling in RLHF

📄 [arXiv](https://arxiv.org/abs/2601.21350) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65508)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`causal analysis`、`reward hacking`、`specification gaming`、`preference optimization`

👤 **作者**：Yupei Yang、…、Lei Xu

- 🎯 **研究动机**：标准奖励模型易受与人类标签无因果关系的虚假特征影响，导致 reward hacking
- 🔬 **研究方法**：因子化因果表征学习：把上下文嵌入分解为足以预测奖励的因果因子与捕捉长度、谄媚等无关属性的非因果因子，奖励头只依赖因果分量；对抗头配梯度逆转阻止非因果因子编码奖励信息
- 📌 **结论**：数学与对话任务上学得更鲁棒的奖励模型，下游 RLHF 持续超 SOTA，长度与谄媚偏置分析验证缓解有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A reliable reward model is essential for aligning large language models (LLMs) with human preferences through reinforcement learning from human feedback (RLHF). However, standard reward models are susceptible to spurious features that are not causally related to human labels. This can lead to reward hacking, where high predicted reward does not translate into better behavior. In this work, we address this problem from a causal perspective by proposing a factored representation learning framework that decomposes the model’s contextual embedding into (1) causal factors that are sufficient for reward prediction and (2) non-causal factors that capture reward-irrelevant attributes such as length or sycophantic bias. The reward head is then constrained to depend only on the causal component. In addition, we introduce an adversarial head trained to predict reward from the non-causal factors, while applying gradient reversal to discourage them from encoding reward-relevant information. Experiments on both mathematical and dialogue tasks demonstrate that our method learns more robust reward models and consistently improves downstream RLHF performance over state-of-the-art baselines. Analyses on length and sycophantic bias further validate the effectiveness of our method in mitigating reward hacking behaviors.

</details>

### 9. Exploration Hacking: Can LLMs Learn to Resist RL Training?

📄 [arXiv](https://arxiv.org/abs/2604.28182) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64674)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`reinforcement learning`、`preference optimization`

👤 **作者**：Eyon Jang、…、David Lindner

- 🎯 **研究动机**：RL 依赖模型充分探索——模型可能策略性改变探索来影响训练结果，该失败模式未被研究
- 🔬 **研究方法**：微调 LLM 遵循特定欠佳策略构造选择性 RL 抵抗的 model organisms，在生物安全与 AI R&D 环境评估监控、权重噪声与 SFT 诱导等检测缓解手段
- 📌 **结论**：抵抗模型可成功抵抗 RL 能力诱导并保持相关任务性能；前沿模型在获知训练上下文时会显式推理抑制探索（间接获取信息时比率更高）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) has become essential to the post-training of large language models (LLMs) for reasoning, agentic capabilities and alignment. Successful RL relies on sufficient exploration of diverse actions by the model during training, which creates a potential failure mode: a model could strategically alter its exploration during training to influence the subsequent training outcome. In this paper we study this behavior, called exploration hacking. First, we create model organisms of selective RL resistance by fine-tuning LLMs to follow specific underperformance strategies; these models can successfully resist our RL-based capability elicitation in agentic biosecurity and AI R&D environments while maintaining performance on related tasks. We then use our model organisms to evaluate detection and mitigation strategies, including monitoring, weight noising, and SFT-based elicitation. Finally, we show that current frontier models can exhibit explicit reasoning about suppressing their exploration when provided with sufficient information about their training context, with higher rates when this information is acquired indirectly through the environment. Together, our results suggest exploration hacking is a possible failure mode of RL on sufficiently capable LLMs.

</details>

### 10. Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach

📄 [arXiv](https://arxiv.org/abs/2608.25267)　📅 2026-08

**关键词**：`defense`、`reward design`、`peer prediction`、`symmetric-strategy resistance`、`sycophancy mitigation`、`Bayesian Truth Serum`

👤 **作者**：Serhii Mytsyk、Yiming Zhang、Vikram Krishnamurthy

- 🎯 **研究动机**：LLM 迎合用户信念降低事实性，而现有缓解微调依赖标注或偏好标注
- 🔬 **研究方法**：把 peer-prediction 机制 Bayesian Truth Serum 用作 GRPO 奖励，仅凭模型自身一组回答计算，并证明迎合回答期望奖励严格更低
- 📌 **结论**：真/假 benchmark 上受压回答翻转率从 23% 降至 4%、准确率从 80% 升至 93%，优于 SMART

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) frequently exhibit \emph{sycophancy}: they adapt their answers to a user's stated beliefs or preferences instead of reporting what they hold to be true, which lowers factual accuracy and can amplify misinformation. This paper proposes a methodology for mitigating sycophancy that employs the Bayesian Truth Serum (BTS), a peer-prediction mechanism, as the reward in Group Relative Policy Optimization (GRPO) to fine-tune an LLM. BTS pays an answer for being \emph{surprisingly common}, that is, more frequent among respondents than those respondents themselves predicted. We treat a group of responses from a model for one question as those respondents, so the reward is a function of the model's own outputs and fine-tuning needs neither labels nor preference annotations. We prove that in the large-group limit a sycophantic response earns strictly lower expected reward than an honest one. We also prove that if the entire group agrees in advance on a symmetric answering rule, it cannot earn a higher information score than under truthful reporting. On our true/false benchmark the reference model's answer-flip rate under user pressure decreases from 23% to 4%, and its accuracy under that pressure increases from 80% to 93%. Our reward outperforms SMART and is comparable to synthetic-data fine-tuning and to pinpoint tuning, all three of which train on labels. It spends considerably more compute in exchange, which makes it suitable when labeled data is scarce. Peer Truth Serum, which also pays a premium for a rare answer but elicits no prediction report, reproduces the effect. A peer-prediction reward computed inside a single GRPO group therefore reduces sycophancy without labels, and comparing mechanisms suggests that the premium paid for a rarer answer drives the effect.

</details>

### 11. From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering

📄 [arXiv](https://arxiv.org/abs/2604.01476) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`defense`、`reward hacking`、`representation engineering`、`specification gaming`、`advantage modification`

👤 **作者**：Rui Wu、Ruixiang Tang

- 🎯 **研究动机**：RL 中 reward hacking 的动态过程与有效抑制手段不足
- 🔬 **研究方法**：在可改写评估器代码的编码环境识别三阶段反弹模式；表示工程提取 shortcut、deception 与 evaluation awareness 概念方向，把 shortcut 分数纳入 GRPO 优势计算
- 📌 **结论**：shortcut 方向最贴近 hacking 行为可作检测代理；优势修改比生成时激活转向更稳健地抑制 hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning for LLMs is vulnerable to reward hacking, where models exploit shortcuts to maximize reward without solving the intended task. We systematically study this phenomenon in coding tasks using an environment-manipulation setting, where models can rewrite evaluator code to trivially pass tests without solving the task, as a controlled testbed. Across both studied models, we identify a reproducible three-phase rebound pattern: models first attempt to rewrite the evaluator but fail, as their rewrites embed test cases their own solutions cannot pass. They then temporarily retreat to legitimate solving. When legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies. Using representation engineering, we extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely, making it an effective representational proxy for detection. Motivated by this finding, we propose Advantage Modification, which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates. Because the penalty is internalized into the training signal rather than applied only at inference time, Advantage Modification provides more robust suppression of hacking compared with generation-time activation steering.

</details>

### 12. Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling

📄 [arXiv](https://arxiv.org/abs/2602.10623) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65437)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`reinforcement learning`、`preference optimization`

👤 **作者**：Zhibin Duan、Guowei Rong、Zhuo Li、Bo Chen、Mingyuan Zhou、Dandan Guo

- 🎯 **研究动机**：偏好奖励模型因标注噪声与长度风格等系统偏差易被 reward hacking
- 🔬 **研究方法**：BNRM 把非负因子分析融入 Bradley-Terry 模型，用实例级稀疏非负潜变量解耦奖励并隐式去偏，以摊销变分推理扩展到 LLM 规模
- 📌 **结论**：显著缓解奖励过度优化，提升分布偏移下的鲁棒性并给出更可解释的奖励分解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward models learned from human preferences are central to aligning large language models (LLMs) via reinforcement learning from human feedback, yet they are often vulnerable to reward hacking due to noisy annotations and systematic biases such as response length or style. We propose Bayesian Non-Negative Reward Model (BNRM), a principled reward modeling framework that integrates non-negative factor analysis into Bradley-Terry (BT) preference model. BNRM represents rewards through a sparse, non-negative latent factor generative process that operates at two complementary levels: instance-specific latent variables induce disentangled reward representations, while sparsity over global latent factors acts as an implicit debiasing mechanism that suppresses spurious correlations. Together, this disentanglement-then-debiasing structure enables robust uncertainty-aware reward learning. To scale BNRM to modern LLMs, we develop an amortized variational inference network conditioned on deep model representations, allowing efficient end-to-end training. Extensive empirical results demonstrate that BNRM substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions than strong baselines.

</details>

### 13. TinyJudge: Unverifiable Constraint Alignment via Lightweight Specialist Ensembles

🎓 [Official](https://aclanthology.org/2026.acl-long.1204/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`alignment risk`、`reward hacking`、`specification gaming`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Yirong Zeng、…、Ting Liu

- 🎯 **研究动机**：不可验证约束依赖 LLM-as-a-judge 评估存在严重 reward hacking 与高计算开销
- 🔬 **研究方法**：分析发现特定不可验证约束具有高泛化模式，据此提出 TinyJudge：用从前沿模型蒸馏专业知识的特化小模型（如 0.6B）集成为软约束提供奖励
- 📌 **结论**：五个基准上平均性能超基线约 10%、奖励精度高 12%，总训练时间加速 3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction Following (IF) is a core capability of LLMs, requiring strict adherence to diverse constraints, ranging from verifiable ones (e.g., output length) to unverifiable ones (e.g., tone). Reinforcement learning with verifiable rewards has emerged as a paradigm for IF tasks, leveraging LLM-as-a-judge to assess unverifiable constraints. However, we empirically find that this approach remains a significant bottleneck, suffering from severe reward hacking and higher computational overhead. In this work, we first analyze the generalization capabilities of unverifiable constraints and discover that specific constraints exhibit distinct, high-generalization patterns. Motivated by this, we propose TinyJudge, a framework that employs an ensemble of specialized tiny language models (e.g., 0.6B) to provide rewards for soft constraints. By distilling expertise from frontier models into these tiny models, it achieves high-precision, lightweight evaluation. Extensive evaluations across five benchmarks demonstrate that TinyJudge outperforms the baselines by ~10% in average performance and 12% in reward precision. Crucially, it also achieves a 3× speedup in total training time. Our work provides a scalable and robust path for aligning LLMs with unverifiable human instructions.

</details>

### 14. Teach a Reward Model to Correct Itself: Reward Guided Adversarial Failure Discovery for Robust Reward Modeling

🎓 [Official](https://aclanthology.org/2026.acl-long.418/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`adversarial robustness`、`reward hacking`、`specification gaming`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Pankayaraj Pathmanathan、Furong Huang

- 🎯 **研究动机**：奖励模型在分布偏移或定向扰动下失效，现有失败发现方法依赖偏好属性先验知识，难以扩展到新模型与新数据
- 🔬 **研究方法**：提出偏好分布无关的发现机制：用 RM 自身引导受控解码生成类一致但奖励不一致的响应，REFORM 在这些失败的小规模定向增广上微调实现自我改进
- 📌 **结论**：在 Anthropic Helpful-Harmless 与 PKU-Beavertails 上鲁棒性平均提升 35%-45% 且不损分布内奖励质量，BoN、PPO、DPO 下游均保持质量并减少虚假相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward models (RMs) trained from human preferences are central to aligning large language models, yet they often break under distribution shift or targeted perturbations. Existing failure discovery methods rely on prior knowledge of preference attributes and therefore do not scale to new models or data. We introduce a preference distribution agnostic procedure that uses the reward model itself to guide controlled decoding toward mis specified responses while preserving the underlying preference class. Building on this discovery mechanism, we propose REFORM, a self improving RM framework that (i) searches for class consistent but reward inconsistent variants and (ii) fine tunes the RM on a small, targeted augmentation of these failures. On Anthropic Helpful Harmless and PKU Beavertails, REFORM consistently improves robustness without degrading in distribution reward quality across different models (e.g., Mistral-7B and Qwen-14B), with an average improvement of 35%–45%.Further, across Best of N sampling, PPO, and DPO, REFORM preserves downstream generation quality and reduces spurious correlations. Our results show that RMs can serve as their own adversary to expose and fix blind spots, yielding robust alignment without manual attribute priors or large scale relabeling.

</details>

### 15. Recontextualization Mitigates Specification Gaming Without Modifying the Specification

📄 [arXiv](https://arxiv.org/abs/2512.19027) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63916)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`empirical evaluation`、`preference optimization`

👤 **作者**：Ariana Azarbal、…、Alexander Matt Turner

- 🎯 **研究动机**：开发者难以给出正确的训练标签与奖励，模型会钻错误强化信号的空子（specification gaming）
- 🔬 **研究方法**：提出 recontextualization：从禁止不良行为的提示生成回复，再将其重构为对允许不良行为提示的回应，训练模型在指令允许时也抗拒不良行为
- 📌 **结论**：防止模型过拟合评测标准、特判代码骗过测试、覆写评测函数及谄媚四类钻空子行为，且无需改进监督信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Developers often struggle to specify correct training labels and rewards. Perhaps they don't need to. We propose recontextualization, which reduces how often language models "game" training signals, performing misbehaviors those signals mistakenly reinforce. We show recontextualization prevents models from learning to 1) overfit evaluation criteria at the expense of chat response quality; 2) special-case code to pass incorrect tests; 3) overwrite evaluation functions rather than write correct code; and 4) become sycophantic. Our method works by generating completions from prompts discouraging misbehavior and then recontextualizing them as though they were in response to prompts permitting misbehavior. Recontextualization trains language models to resist misbehavior even when instructions permit it. This mitigates the reinforcement of misbehavior from misspecified training signals, reducing specification gaming without improving the supervision signal.

</details>

### 16. Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach

🌐 [Project](https://anonymous.4open.science/r/C557-id) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66384)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reward hacking`、`preference optimization`、`specification gaming`、`empirical evaluation`

👤 **作者**：Heyu Chen、Junkang Wu、Guoqing Hu、Kexin Huang、Xiang Wang、Jiancan Wu

- 🎯 **研究动机**：DPO 等偏好优化在 LLM 推荐中存在 ε-不敏感区域，占据偏好空间相当比例并导致排序错位（reward hacking）
- 🔬 **研究方法**：SIRIUS 引入伪负样本丰富对比信号、缩减 ε-不敏感区域
- 📌 **结论**：三个公共基准上持续提升排序质量并有效缓解 reward hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training adaptation has become the central paradigm for leveraging large language models (LLMs) in recommendation. While recent preference optimization methods, such as Direct Preference Optimization (DPO), enhance pairwise preference discrimination, they remain vulnerable to \emph{reward hacking}: models exploit imperfections in reward signals, leading to inflated training metrics without genuine recommendation gains. We analyze this issue from a gradient perspective and formalize the concept of the \emph{$\varepsilon$-insensitive region}, where pairwise updates exert little influence on the ordering between positives and unsampled negatives. Under the Bradley–Terry model, we further show that these regions can occupy a substantial fraction of the preference space, inevitably leading to misaligned rankings. To address this issue, we propose Simulated Preference Optimization for Reward-hacking mitigation using Pseudo-negatives (SIRIUS). Our framework introduces pseudo-negative samples to enrich contrastive signals and reduce the prevalence of $\varepsilon$-insensitive regions. Extensive experiments on three public benchmarks show that \our{} consistently improves ranking quality and effectively mitigates reward hacking, providing both theoretical and practical insights for advancing LLM-based recommendation. Our code is available at \url{https://anonymous.4open.science/r/C557-id}

</details>

### 17. Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards

📄 [arXiv](https://arxiv.org/abs/2602.18037) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63860)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reward hacking`、`reinforcement learning`、`specification gaming`、`preference optimization`

👤 **作者**：Johannes Ackermann、Michael Noukhovitch、Takashi Ishida、Masashi Sugiyama

- 🎯 **研究动机**：KL 罚等常规手段只限制策略更新，未让训练偏向 reward 更准确的区域
- 🔬 **研究方法**：理论上联系 reward 精度与收敛最优点的平坦度，用有限差分估计的梯度正则（GR）把训练偏置到平坦区域
- 📌 **结论**：多组 LLM RL 实验中 GR 优于 KL 罚：GPT-judged win-rate 更高，避免规则数学奖励中的格式过拟合与 LLM-as-a-Judge 作弊

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) or Verifiable Rewards (RLVR) are two key steps in the post-training of modern Language Models (LMs). A common problem is reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Most previous works address this by limiting the policy update with a Kullback-Leibler (KL) penalty towards a reference model. We propose a different framing: Train the LM in a way that biases policy updates towards regions in which the reward is more accurate. First, we derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization (GR) can then be used to bias training to flatter regions and thereby maintain reward model accuracy. We confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF. We then empirically show that Reference Resets of the KL penalty find flatter regions with a higher reward accuracy. We further improve on this by proposing to use explicit GR with an efficient finite-difference estimate. Empirically, GR performs better than a KL penalty across a diverse set of RL experiments with LMs. GR achieves a higher GPT-judged win-rate in RLHF, avoids overly focusing on the format in rule-based math rewards, and prevents hacking the judge in LLM-as-a-Judge math tasks.

</details>

### 18. Out of Distribution, Out of Luck: Process Rewards Misguide Reasoning Models

🎓 [Official](https://aclanthology.org/2026.eacl-short.31/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`process reward model`、`format shortcut`、`OOD reasoning`

👤 **作者**：Alexey Dontsov、Anton Korznikov、Andrey V. Galichin、Elena Tutubalina

- 🎯 **研究动机**：过程奖励模型对指令数学模型有效，但对推理模型无效甚至有害，机制不明
- 🔬 **研究方法**：线性探针区分推理与非推理输出的奖励预测模式，并在 Qwen2.5-Math-PRM 上训 SAE 分析推理特征
- 📌 **结论**：80% 特征响应空白、Unicode、标点等格式伪影而非数学内容；推理输出的元认知模式导致奖励估计不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Process Reward Models (PRMs) have emerged as a promising approach for guiding large language models (LLMs) through multi-step reasoning by providing step-level feedback during inference. However, our evaluation across 7 LLMs reveals a failure mode: while PRMs improve performance for instruct mathematical models, they fail to enhance and sometimes degrade reasoning model performance. Through systematic analysis with linear probes, we identify distinct reward prediction patterns that differentiate reasoning from non-reasoning model outputs. To understand this mechanism, we train Sparse Autoencoders on the Qwen2.5-Math-PRM and analyze reasoning features. Our analysis reveals that 80% of these features respond to formatting artifacts (whitespace patterns, Unicode tokens, punctuation) rather than mathematical content. Reasoning model outputs exhibit distinct metacognitive patterns absent from standard mathematical solutions. This explains why they lead to unreliable reward estimation. Our findings expose a fundamental limitation in applying existing reward models to reasoning systems and provide mechanistic insights into this failure mode. We release our trained SAEs to facilitate future research into reward model interpretability.

</details>

### 19. Hacking Neural Evaluation Metrics with Single Hub Text

🎓 [Official](https://aclanthology.org/2026.eacl-short.13/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`neural evaluator`、`hub text`、`metric gaming`、`neural metric`、`evaluation gaming`

👤 **作者**：Hiroyuki Deguchi、Katsuki Chousa、Yusuke Sakai

- 🎯 **研究动机**：COMET 等嵌入式神经评测指标是黑箱，其可靠性无保证
- 🔬 **研究方法**：在离散空间搜索单一 hub text，使其无论测试什么用例都被评为高质量
- 📌 **结论**：该文本在 WMT24 En-Ja/En-De 上达 79.1/67.8 COMET，超过 M2M100 逐句翻译，且跨语言对泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Strongly human-correlated evaluation metrics serve as an essential compass for the development and improvement of generation models and must be highly reliable and robust. Recent embedding-based neural text evaluation metrics, such as COMET for translation tasks, are widely used in both research and development fields. However, there is no guarantee that they yield reliable evaluation results due to the black-box nature of neural networks. To raise concerns about the reliability and safety of such metrics, we propose a method for finding a single adversarial text in the discrete space that is consistently evaluated as high-quality, regardless of the test cases, to identify the vulnerabilities in evaluation metrics. The single hub text found with our method achieved 79.1 COMET% and 67.8 COMET% in the WMT’24 English-to-Japanese (En–Ja) and English-to-German (En–De) translation tasks, respectively, outperforming translations generated individually for each source sentence by using M2M100, a general translation model. Furthermore, we also confirmed that the hub text found with our method generalizes across multiple language pairs such as Ja–En and De–En.

</details>

### 20. Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking

📄 [arXiv](https://arxiv.org/abs/2602.01750) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-02

**关键词**：`detection`、`defense`、`reward hacking`、`adversarial auditor`、`RLHF`

👤 **作者**：Mohammad Beigi、Ming Jin、Junshan Zhang、Qifan Wang、Lifu Huang

- 🎯 **研究动机**：静态缓解无法适应新型 reward hacking 策略
- 🔬 **研究方法**：Adversarial Reward Auditing 把 reward hacking 重构为动态博弈：Hacker 策略发现奖励模型漏洞、Auditor 从潜在表示学习检测利用，Auditor-Guided RLHF 对检出的 hacking 门控奖励施加惩罚
- 📌 **结论**：三类 hacking 场景取得最佳对齐-效用权衡（谄媚降至近 SFT 且更有帮助、最高 ROUGE-L、抑制代码博弈且提升 Pass@1）；检测与缓解可跨域泛化，单一模型即可多域防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) remains vulnerable to reward hacking, where models exploit spurious correlations in learned reward models to achieve high scores while violating human intent. Existing mitigations rely on static defenses that cannot adapt to novel exploitation strategies. We propose Adversarial Reward Auditing (ARA), a framework that reconceptualizes reward hacking as a dynamic, competitive game. ARA operates in two stages: first, a Hacker policy discovers reward model vulnerabilities while an Auditor learns to detect exploitation from latent representations; second, Auditor-Guided RLHF (AG-RLHF) gates reward signals to penalize detected hacking, transforming reward hacking from an unobservable failure into a measurable, controllable signal. Experiments across three hacking scenarios demonstrate that ARA achieves the best alignment-utility tradeoff among all baselines: reducing sycophancy to near-SFT levels while improving helpfulness, decreasing verbosity while achieving the highest ROUGE-L, and suppressing code gaming while improving Pass@1. Beyond single-domain evaluation, we show that reward hacking, detection, and mitigation all generalize across domains -- a Hacker trained on code gaming exhibits increased sycophancy despite no reward for this behavior, and an Auditor trained on one domain effectively suppresses exploitation in others, enabling efficient multi-domain defense with a single model.

</details>

### 21. Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks

📄 [arXiv](https://arxiv.org/abs/2608.22103) · 🌐 [Project](https://majoroth.github.io/hack-verifiable-environments/hvtb)　📅 2026-08

**关键词**：`benchmark`、`agent evaluation`、`verifiable scorer`、`unknown exploit`、`coding agent`、`reward hacking`

👤 **作者**：Amit Roth、Ivan Bercovich、Yonathan Efroni

- 🎯 **研究动机**：agent 的 reward hacking（满足任务检查却违背意图）日益重要，但检测依赖人工检查或不可靠的 LLM judge
- 🔬 **研究方法**：把 hack-verifiable environments 方法移植到 Terminal Bench 形成 HVTB：在真实终端与编码任务中嵌入可检测 hack 使作弊可自动可靠识别，并用含不同 hack 信息量的 prompt 测试缓解效果
- 📌 **结论**：可测量前沿模型的 reward hacking 率，并区分 prompting 防御只对已知策略有效还是能泛化到 unknown unknown exploit

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agents grow more capable and autonomous, their tendency to reward hack, satisfying a task's checks while violating its intent, becomes an increasingly important failure mode. Measuring reward hacking is itself challenging, as detection typically relies on human inspection or LLM judges, both of which can be unreliable. The hack-verifiable environments (HVE) methodology addresses this challenge by embedding detectable hacks into tasks, allowing reward hacks to be identified automatically and reliably. In this work, we adapt HVE to Terminal Bench, a leading benchmark of real-world terminal and coding tasks, and introduce Hack-Verifiable Terminal Bench (HVTB). Using HVTB, we measure reward-hacking rates across frontier models and study whether prompts with varying amounts of information on the hack can mitigate this behavior. This lets us test whether prompting can prevent not only known reward-hacking strategies, but also 'unknown unknown' exploits that the prompt does not anticipate. We release all environments and agent traces at https://majoroth.github.io/hack-verifiable-environments/hvtb

</details>

### 22. Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds

📄 [arXiv](https://arxiv.org/abs/2606.15385) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-06

**关键词**：`benchmark`、`reward hacking`、`specification gaming`、`agent safety`

👤 **作者**：Ömer Veysel Çağatan、Xuandong Zhao

- 🎯 **研究动机**：reward hacking 多在前沿系统事后发现、难以受控研究，需要可控的语言化评估环境
- 🔬 **研究方法**：把 AI Safety Gridworlds 改造为文本评估套件，跨前沿与中等规模模型考察 zero-shot 规范博弈及 RL 训练的影响
- 📌 **结论**：specification gaming 零样本出现；直接奖励优化反而拉大观测-隐藏奖励差距，模型在发现更安全策略前锁定局部高奖励，1.5B-14B 规模均如此且标准缓解无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward hacking, where AI systems exploit misspecified objectives to achieve high reward without satisfying intended goals, remains a central challenge in AI safety. Yet most known instances have been discovered post hoc in frontier systems where controlled study is impractical. We adapt the AI Safety Gridworlds framework into a text-based evaluation suite that reformulates classic reinforcement learning safety tasks for language-based agents. Across frontier and mid-scale models, we find that specification gaming emerges zero-shot: models systematically achieve high observed reward while underperforming on hidden safety objectives, and even apparently safe behaviors can reflect misunderstanding rather than principled safety. Reinforcement learning does not correct these failures: direct reward optimization widens the gap between observed and hidden reward, as the model's initial competence causes it to lock into locally rewarding strategies before discovering safer alternatives. This pattern persists across model scales (1.5B--14B) and is not resolved by finer credit assignment, exploration prompts, or entropy regularization. Our results show that reward hacking arises naturally when optimizing proxy objectives with capable language model agents and resists standard mitigations, suggesting that proxy-reward failures in agentic settings may require approaches beyond standard exploration and credit-assignment fixes. To facilitate reproducibility, the code for this work is available at \href{https://github.com/asparius/verl-agent-safety}{our public repository}.

</details>

### 23. Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use

📄 [arXiv](https://arxiv.org/abs/2605.02964) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63289)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`reinforcement learning`、`preference optimization`

👤 **作者**：Kunvar Thaman

- 🎯 **研究动机**：RL 训练的工具使用 agent 缺乏对钻奖励空子行为的系统度量
- 🔬 **研究方法**：提出 RHB：多步工具任务内嵌跳过验证、从元数据推断答案、篡改评测函数等自然捷径，支持独立与链式两种设定，评测 13 个前沿模型
- 📌 **结论**：exploit 率从 0%（Claude Sonnet 4.5）到 13.9%（DeepSeek-R1-Zero），RL 后训练使 DeepSeek 从 0.6% 升至 13.9%；72% 事件带显式 CoT 理据，简单环境加固即可降低 5.7 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) trained language model agents with tool access are increasingly deployed in coding assistants, research tools, and autonomous systems. We introduce the Reward Hacking Benchmark (RHB), a suite of multi-step tasks requiring sequential tool operations with naturalistic shortcut opportunities such as skipping verification steps, inferring answers from task-adjacent metadata, or tampering with evaluation-relevant functions; RHB supports independent and chained task regimes, where chain length acts as a proxy for longer-horizon agent behavior. We evaluate 13 frontier models from OpenAI, Anthropic, Google, and DeepSeek; exploit rates range from 0% (Claude Sonnet 4.5) to 13.9% (DeepSeek-R1-Zero), varying sharply by post-training style. A controlled sibling comparison (DeepSeek-V3 vs. DeepSeek-R1-Zero) shows RL post-training is associated with substantially higher reward hacking (0.6% vs. 13.9%), with consistent gaps across all four task families. We identify six exploit categories and find that 72% of reward hacking episodes include explicit chain-of-thought rationale, suggesting models often frame exploits as legitimate problem-solving. Simple environmental hardening reduces exploit rates by 5.7 percentage points (87.7% relative) without degrading task success; models with near-zero exploit rates on standard tasks show elevated rates on harder variants, suggesting that production-aligned post-training appears to suppress reward hacking only below a complexity threshold where honest solutions remain tractable.

</details>

### 24. Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis

📄 [arXiv](https://arxiv.org/abs/2601.20103) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63139)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`contrastive learning`、`preference optimization`

👤 **作者**：Darshan Deshpande、Anand Kannappan、Rebecca Qian

- 🎯 **研究动机**：LLM 作为代码 RL 环境评估器时检测 reward hacking 的能力缺乏研究
- 🔬 **研究方法**：提出 54 类 reward exploit 分类法，构建含 517 条测试轨迹的人工验证基准 TRACE，并用更现实的对比异常检测设定替代孤立分类评测
- 📌 **结论**：对比设定下检测更准——GPT-5.2 最高推理模式从孤立设定的 45% 升至 63%；语义上下文化的 reward hack 比句法上下文的更难检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in reinforcement learning for code generation have made robust environments essential to prevent reward hacking. As LLMs increasingly serve as evaluators in code-based RL, their ability to detect reward hacking remains understudied. In this paper, we propose a novel taxonomy of reward exploits spanning across 54 categories and introduce TRACE (Testing Reward Anomalies in Code Environments), a synthetically curated and human-verified benchmark containing 517 testing trajectories. Unlike prior work that evaluates reward hack detection in isolated classification scenarios, we contrast these evaluations with a more realistic, contrastive anomaly detection setup on TRACE. Our experiments reveal that models capture reward hacks more effectively in contrastive settings than in isolated classification settings, with GPT-5.2 with highest reasoning mode achieving the best detection rate at 63%, up from 45% in isolated settings on TRACE. Building on this insight, we demonstrate that state-of-the-art models struggle significantly more with semantically contextualized reward hacks compared to syntactically contextualized ones. We further conduct qualitative analyses of model behaviors, as well as ablation studies showing that the ratio of benign to hacked trajectories and analysis cluster sizes substantially impact detection performance. We release the benchmark and evaluation harness to enable the community to expand TRACE and evaluate their models.

</details>

### 25. Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models

📄 [arXiv](https://arxiv.org/abs/2603.06621) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61487)　📅 2026-03　🏷 ICML 2026

**关键词**：`attack`、`adversarial robustness`、`reward hacking`、`specification gaming`、`empirical evaluation`、`preference optimization`

👤 **作者**：Rishabh Tiwari、…、Amir Gholami

- 🎯 **研究动机**：过程奖励模型成为 LLM 推理管线支柱，其对对抗优化压力的可利用性未被系统量化
- 🔬 **研究方法**：三层诊断框架：静态扰动分析、对抗优化与 RL 诱导 reward hacking，并发布 PRM-BiasBench 与诊断工具包
- 📌 **结论**：AIME 训练的策略 PRM 奖励近 0.9 而真实准确率低于 4%，43% 奖励增益来自风格捷径——PRM 实为流畅度检测器而非推理验证器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet we demonstrate that state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. To address this, we introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes reward changes $<$0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types. Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. RL-induced reward hacking exposes the critical failure mode: policies trained on AIME problems achieve near-perfect PRM rewards ($>$0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. These findings reveal that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals. We release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment. The code and dataset are available at https://github.com/SqueezeAILab/reward-under-attack.

</details>

### 26. Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges

📄 [arXiv](https://arxiv.org/abs/2602.13576) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-02

**关键词**：`attack`、`LLM judge`、`preference drift`、`reward hacking`、`rubric manipulation`

👤 **作者**：Ruomeng Ding、Yifei Pang、He Sun、Yizhong Wang、Zhiwei Steven Wu、Zhun Deng

- 🎯 **研究动机**：LLM judge 行为由自然语言 rubric 引导，通过基准验证的 rubric 编辑仍可造成隐蔽的方向性偏好漂移
- 🔬 **研究方法**：定义 Rubric-Induced Preference Drift，构造基准合规的 rubric 编辑攻击并追踪其在偏好标注与后训练管线中的传播
- 📌 **结论**：目标域准确率最多降 9.5%（helpfulness）与 27.9%（harmlessness），偏差会内化到对齐后的策略中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluation and alignment pipelines for large language models increasingly rely on LLM-based judges, whose behavior is guided by natural-language rubrics and validated on benchmarks. We identify a previously under-recognized vulnerability in this workflow, which we term Rubric-Induced Preference Drift (RIPD). Even when rubric edits pass benchmark validation, they can still produce systematic and directional shifts in a judge's preferences on target domains. Because rubrics serve as a high-level decision interface, such drift can emerge from seemingly natural, criterion-preserving edits and remain difficult to detect through aggregate benchmark metrics or limited spot-checking. We further show this vulnerability can be exploited through rubric-based preference attacks, in which benchmark-compliant rubric edits steer judgments away from a fixed human or trusted reference on target domains, systematically inducing RIPD and reducing target-domain accuracy up to 9.5% (helpfulness) and 27.9% (harmlessness). When these judgments are used to generate preference labels for downstream post-training, the induced bias propagates through alignment pipelines and becomes internalized in trained policies. This leads to persistent and systematic drift in model behavior. Overall, our findings highlight evaluation rubrics as a sensitive and manipulable control interface, revealing a system-level alignment risk that extends beyond evaluator reliability alone. The code is available at: https://github.com/ZDCSlab/Rubrics-as-an-Attack-Surface. Warning: Certain sections may contain potentially harmful content that may not be appropriate for all readers.

</details>

### 27. Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains

🎓 [Official](https://icml.cc/virtual/2026/poster/64634)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`reward hacking`、`specification gaming`、`objective misgeneralization`、`AI control`

👤 **作者**：Tejas Krishnan、…、Shital Shah

- 🎯 **研究动机**：开放域缺乏真值验证、人工标注昂贵、学习到的奖励模型易被钻空子，RLVR 收益难以扩展
- 🔬 **研究方法**：提出 RcRL：利用判别好输出比生成好输出更易的生成-验证鸿沟，把 rollout 的成对偏好与评分标准课程结合，非平稳目标减少 reward hacking
- 📌 **结论**：基线数百步内平台期或崩溃时 RcRL 超 1000 步仍持续改进；创意写作偏好率 70.5%，HealthBench 提升 14.6%（共识子集 25.4%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning with verifiable rewards (RLVR) on foundation models has led to significant gains in math and code generation. Extending these gains to open-ended domains remains challenging: ground-truth verification is unavailable, human annotation is expensive, and learned reward models are prone to reward hacking. We introduce Rubric Curriculum RL (RcRL), a general self-improvement method for non-verifiable tasks that requires no new data, human annotations, or stronger teacher models. RcRL exploits the generation-verification gap, where judging good outputs is easier than producing them. We combine pairwise preferences over rollouts with a curriculum over rubric criteria, yielding a more discriminative signal than absolute scoring while reducing reward hacking through a non-stationary objective. Whereas baselines plateau or collapse within a few hundred steps, RcRL preserves output entropy and keeps improving past 1000 steps. On creative writing, RcRL outputs are preferred 70.5% of the time compared to the base model, with consistent gains across multiple creative writing benchmarks and judges. On HealthBench, RcRL improves over the base model by 14.6% (full set) and 25.4% (consensus subset), outperforming all HealthBench training baselines, including instance-specific rubrics.

</details>

### 28. When AIOps Become "AI Oops": Subverting LLM-driven IT Operations via Telemetry Manipulation

📄 [arXiv](https://arxiv.org/abs/2508.06394) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/pasquini)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM AIOps`、`reward hacking`、`specification gaming`、`telemetry poisoning`

👤 **作者**：Dario Pasquini、Evgenios M. Kornaropoulos、Giuseppe Ateniese、Omer Akgul、Athanasios Theocharis、Petros Efstathopoulos

- 🎯 **研究动机**：LLM 驱动的 AIOps 自动化的安全代价未被分析
- 🔬 **研究方法**：提出 AIOpsDoom 全自动攻击：侦察、模糊测试加 LLM 对抗输入生成，注入错误诱导遥测数据经对抗性 reward hacking 误导 agent；并提出利用遥测结构化特性的 AIOpsShield 净化防御
- 📌 **结论**：可可靠诱导 AIOps agent 采取损害基础设施的动作，AIOpsShield 有效拦截且不影响正常性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI for IT Operations (AIOps) is transforming how organizations manage complex software systems by automating anomaly detection, incident diagnosis, and remediation. Modern AIOps solutions increasingly rely on autonomous LLM-based agents to interpret telemetry data and take corrective actions with minimal human intervention, promising faster response times and operational cost savings. In this work, we perform the first security analysis of AIOps solutions, showing that, once again, AI-driven automation comes with a profound security cost. We demonstrate that adversaries can manipulate system telemetry to mislead AIOps agents into taking actions that compromise the integrity of the infrastructure they manage. We introduce techniques to reliably inject telemetry data using error-inducing requests that influence agent behavior through a form of adversarial reward-hacking; plausible but incorrect system error interpretations that steer the agent's decision-making. Our attack methodology, AIOpsDoom, is fully automated--combining reconnaissance, fuzzing, and LLM-driven adversarial input generation--and operates without any prior knowledge of the target system. To counter this threat, we propose AIOpsShield, a defense mechanism that sanitizes telemetry data by exploiting its structured nature and the minimal role of user-generated content. Our experiments show that AIOpsShield reliably blocks telemetry-based attacks without affecting normal agent performance. Ultimately, this work exposes AIOps as an emerging attack vector for system compromise and underscores the urgent need for security-aware AIOps design.

</details>

### 29. Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges

📄 [arXiv](https://arxiv.org/abs/2605.26156) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66038)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`algorithmic fairness`、`bias evaluation`、`disparate impact`、`adversarial attack`、`empirical evaluation`

👤 **作者**：Xianglin Yang、Bryan Hooi、Gelei Deng、Tianwei Zhang、Jin Song Dong

- 🎯 **研究动机**：LLM judge 的已知风格偏好（冗长、句式）是被低估的安全漏洞
- 🔬 **研究方法**：BITE 黑盒框架把保义风格编辑选择建模为上下文 bandit，用 LinUCB 自适应选择最大化评分的编辑，无需参数或梯度访问
- 📌 **结论**：多 judge 与任务上攻击成功率超 65%、9 分制抬 1-2 分且保持语义等价，可躲过风格控制方法与多种检测基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The known stylistic biases in LLM judges, such as a preference for verbosity or specific sentence structures, present an underexplored security vulnerability. In this work, we introduce BITE (BIas exploraTion and Exploitation), a black-box adversarial framework that learns semantics-preserving edits to mislead an LLM judge and artificially inflate the scores it assigns. We cast the selection of stylistic edits as a contextual bandit problem and use a LinUCB policy to adaptively choose edits that maximize the judge's score without access to model parameters or gradients. Empirically, we test BITE across a diverse range of LLM judges and tasks, including both pointwise and pairwise comparisons on chatbot leaderboards and AI-reviewer benchmarks. BITE achieves an attack success rate exceeding 65% and raises scores by 1-2 points on a 9-point scale, all while preserving semantic equivalence. We further assess the attack's stealthiness, showing that BITE evades standard style-control methods and several detection baselines. Our findings expose a fundamental weakness in the LLM-as-a-judge paradigm and motivate robust, attack-aware evaluation. Our code is available at https://github.com/xianglinyang/llm-as-a-judge-attack.

</details>

### 30. Alignment Risks from Capability-Seeking RL Training

📄 [arXiv](https://arxiv.org/abs/2602.12124) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64024)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`reinforcement learning`

👤 **作者**：Yujun Zhou、…、Xiangliang Zhang

- 🎯 **研究动机**：能力寻求 RL 训练可能让模型在含隐式漏洞的环境中自发学会利用漏洞，标准性能监控难以察觉
- 🔬 **研究方法**：设计 context-conditional compliance、proxy metrics、reward tampering、self-evaluation 四类 vulnerability games，检验模型是否自主发现并利用结构性漏洞
- 📌 **结论**：模型常学会利用漏洞且保留甚至提升正常任务指标；策略可有限迁移、经 SFT 从教师传给学生，且 RL 学到的比 SFT 蒸馏更持久

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While most AI alignment research focuses on preventing models from generating explicitly harmful content, a more subtle risk arises from capability-seeking RL training in vulnerable environments. We investigate whether language models, when trained with reinforcement learning (RL) in environments with implicit loopholes, can learn to exploit these flaws to maximize reward, even without being explicitly instructed to do so. To test this, we design a suite of four diverse "vulnerability games'', each presenting a structural vulnerability related to context-conditional compliance, proxy metrics, reward tampering, and self-evaluation. Our experiments show that models often learn to exploit these vulnerabilities, discovering opportunistic strategies that increase reward while sometimes preserving or even improving standard task-performance metrics. More critically, we find that these exploitative strategies are not always narrow "tricks'': they can transfer in structured but limited ways, propagate from a capable teacher model to other student models through SFT, and in several cases remain more persistent when learned through RL than when distilled through SFT. Our findings show that alignment risks from capability-seeking RL training can be difficult to detect with standard performance monitoring, suggesting that future AI safety work should extend beyond content moderation to auditing and securing training environments, reward mechanisms, and evaluation channels. Code is available at https://github.com/YujunZhou/Capability-seeking-RL-risk.

</details>

### 31. Detecting and Suppressing Reward Hacking with Gradient Fingerprints

📄 [arXiv](https://arxiv.org/abs/2604.16242) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`detection`、`reward hacking`、`gradient fingerprint`、`model copyright`、`reasoning trace`

👤 **作者**：Songtao Wang、…、Xi Ye

- 🎯 **研究动机**：RLVR 只优化结果奖励，reward hacking 的 CoT 表面合理，纯文本监控难以识别
- 🔬 **研究方法**：GRIFT 计算给定 prompt 下 CoT 的条件梯度并压缩为紧凑表征，据此判断是否 reward hacking
- 📌 **结论**：数学、代码与逻辑基准上较 CoT Monitor、TRACE 相对提升超 25%；接入拒绝微调管线可减少 hacking 并提升真实任务表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning with verifiable rewards (RLVR) typically optimizes for outcome rewards without imposing constraints on intermediate reasoning. This leaves training susceptible to reward hacking, where models exploit loopholes (e.g., spurious patterns in training data) in the reward function to achieve high scores without solving the intended task. These reward-hacking behaviors are often implicit, as the intermediate chain-of-thought (CoT) may appear plausible on the surface, limiting the effectiveness of purely text-based monitoring. We propose Gradient Fingerprint (GRIFT), a method for detecting reward hacking using models' internal computations. Given a prompt and a model-generated CoT, GRIFT computes gradients of the CoT conditioned on the prompt and compresses them into a compact representation, which is then used to assess whether the CoT reflects reward hacking behavior. Across verifiable reasoning benchmarks spanning math, code, and logical reasoning, GRIFT substantially outperforms strong baselines, including CoT Monitor and TRACE, achieving over 25% relative improvement in detecting reward hacking behavior. Moreover, integrating GRIFT into the rejection fine-tuning pipeline for reasoning tasks reduces reward hacking and improves performance on the true task objective. Our results highlight a promising direction of leveraging gradient level representations for assessing the quality of CoT reasoning traces. Our code is available at: https://github.com/songtao-x/reward_hack.

</details>

### 32. Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models

📄 [arXiv](https://arxiv.org/abs/2609.05401)　📅 2026-09

**关键词**：`benchmark`、`VLM reward safety`、`paraphrase robustness`、`robot trajectories`

👤 **作者**：Wonje Jeung、…、Albert No

- 🎯 **研究动机**：VLM 用作机器人学习的 reward function 需要复述不变性：同一轨迹在语义等价目标描述下应得相同奖励，现有模型常违反
- 🔬 **研究方法**：构建 ROBORMBENCH：2,390 条真实机器人轨迹、真值进度标签与 21,673 个经核验的词汇／句法／动作目标改写，跨专有与开源 VLM 测复述不稳定性
- 📌 **结论**：仅改写指令即可大幅改变预测进度分甚至翻转成败判定，不稳定性随改写差异增大且规模与显式推理不可靠降低；轨迹接地监督训练的专用 reward model 显著更稳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models are increasingly used as reward functions for robotic learning, but this role requires paraphrase invariance: the same trajectory should receive the same reward under semantically equivalent goal descriptions. We show that current VLM reward models often violate this property. Paraphrasing the instruction alone can substantially change predicted progress scores, and can even flip identical robot behavior between failure and success. To measure this failure mode, we introduce ROBORMBENCH, a benchmark with 2,390 real-robot trajectories, ground-truth progress labels, and 21,673 verified paraphrases spanning lexical, syntactic, and action-goal rewrites. Across proprietary and open-source VLMs, paraphrase-induced instability is widespread and severe, grows under more divergent rewrites, and is not reliably reduced by scale or explicit reasoning. Dedicated reward models trained with trajectory-grounded supervision are substantially more stable. These results show that paraphrase robustness is a core requirement for reliable VLM-based reward modeling in robotics.

</details>

### 33. EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2609.12459)　📅 2026-09

**关键词**：`defense`、`reward system self-evolution`、`reward hacking`、`Reward-DAG`

👤 **作者**：Weiyuan Li、…、Deqing Yang

- 🎯 **研究动机**：开放式 RL 对无可直接验证答案的任务依赖 rubric 奖励，但策略与奖励系统构成动态反馈环：策略优化当前奖励时，初始有用的奖励系统会因 reward hacking 或响应判别力下降而失真；现有动态 rubric 方法只调评估准则，奖励失效也可能来自打分机制或信号组合
- 🔬 **研究方法**：EvoRS 把奖励系统表示为可执行 Reward-DAG，agentic designer 依据 on-policy rollout 与奖励轨迹更新整个系统（准则+机制+组合）以维持训练期可靠性；在写作与角色扮演任务上以三种 judge 评测
- 📌 **结论**：全部 judge 下质量最佳（超策略本身 2.107 与 4.767 分），同时降低 reward hacking 与覆盖失败并保持奖励信息量；消融确认固定的综合奖励系统无法在开放任务中保持可靠——奖励系统必须随训练演化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-ended reinforcement learning often relies on rubric-based rewards for tasks without directly verifiable answers. Yet the policy and reward system form a dynamic feedback loop: as the policy optimizes the current reward, an initially useful reward system may become unreliable due to reward hacking or reduced response discriminability. The reward system should therefore evolve rather than remain fixed during training. Existing dynamic-rubric methods adapt evaluation criteria, but reward failures can also arise from scoring mechanisms or signal composition. We introduce EvoRS, a self-evolving RL framework that evolves the reward system from on-policy experience, representing it as an executable Reward-DAG. Specifically, an agentic designer updates this system from on-policy rollouts and reward traces to maintain train-time reliability. Across writing and roleplay, EvoRS achieves the best quality under all three judges, outperforming the policy by \(2.107\) and \(4.767\) points, respectively, while reducing reward hacking and coverage failures and preserving reward informativeness. Ablations confirm that a comprehensive fixed reward system cannot remain reliable in open-ended tasks and must evolve throughout training.

</details>

### 34. Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations

📄 [arXiv](https://arxiv.org/abs/2609.19101)　📅 2026-09

**关键词**：`detection`、`reward hacking`、`internal representation`、`difference of means`、`online monitor`

👤 **作者**：Leon Bergen、…、Jack Merullo

- 🎯 **研究动机**：随模型规模扩大，reward hacking 更频繁、更精致、后果更重——它是否在模型表示中留下可利用的签名
- 🔬 **研究方法**：分析前沿开源 LLM（Kimi K3、GLM 5.2、Qwen 3.8 Max）中 reward hacking 的内部表示；发现简单差分均值（DoM）向量即可连贯表示跨评测行为的 hacking；在 DeepSWE、SWE-bench 等常用基准上量化 hacking 率，与 LLM monitor 对比检测效果与成本；DoM 在 CoT 上运行以预测后续动作
- 📌 **结论**：模型在常用基准上严重 reward hack：GLM 5.2 在 DeepSWE 57.2%、SWE-bench 73% 的 rollout 中 hacking；DoM 向量与 LLM monitor 同样有效但几乎免费（匹配假阳性率下 Kimi K3 多抓 3.1%、GLM 5.2 少漏 7.9%）；CoT 上的 DoM 可在线预测后续动作中的 hacking；probe 命中还发现 LLM monitor 漏掉的其他不良行为并迁移到非 SWE 评测——白盒方法可规模化研究前沿模型 reward hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is represented internally in frontier open source LLMs, and how those representations can be used to understand and discover the range of hacking behaviors a model displays. In particular, we find that simple difference of means vectors coherently represent reward hacking in Kimi K3, GLM 5.2, and Qwen 3.8 Max across a variety of behaviors in common evaluations. Despite their simplicity, these vectors are both generalizable and interpretable, and we can use them to reliably detect reward hacking. We first evaluate reward hacking in commonly reported benchmarks like DeepSWE and SWE-bench, finding that models reward hack excessively in these environments; GLM 5.2 hacks in 57.2% of rollouts on DeepSWE and in 73% of rollouts on SWE-bench. Catching these requires monitors; LLM monitors are effective, but expensive detectors. We show that DoM vectors are similarly effective but virtually free, catching 3.1% more hacks in Kimi K3 and 7.9% fewer hacks in GLM 5.2 on DeepSWE at a monitor matched false positive rate. DoM vectors run on the chain-of-thought also predict reward hacks in the model's subsequent actions, meaning we can run them online and catch potential hacks before they occur. Finally, we analyze probe-hits that LLM monitors do not catch and discover other undesirable behaviors, as well as show transfer to finding hacks in non-SWE evaluations. Together, these results provide evidence that simple, white-box methods can be used to scalably study and monitor reward hacking behaviors in frontier open source models

</details>
