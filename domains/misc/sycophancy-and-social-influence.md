# Sycophancy 与 Social Influence

[返回上级目录](README.md)

## 研究方向

研究模型迎合用户、权威或既有立场，以及生成内容对人类信念、排序和偏好的影响；覆盖 sycophancy benchmark、persuasion、belief manipulation、rhetorical misalignment 与缓解。

## 研究脉络

- **迎合测量：** 早期工作通过用户立场和权威线索翻转测试模型是否牺牲真实性来保持一致。
- **交互放大：** 多轮反馈、用户施压、重新考虑 checkpoint 与 iterative self-refinement 会为模型反复向用户立场让步提供机会，需要将 sycophancy 从单次回答扩展到完整交互过程测量。
- **机制与训练来源：** Persona、RLHF、reward model 和表示方向研究迎合行为如何形成。
- **社会影响：** Persuasion 与 belief-change benchmark 将模型输出连接到人类决策后果。
- **干预与边界：** Reasoning、verbalized assumption 和 representation control 可降低部分迎合，但也可能只掩盖表面表达。

## 机制、社会影响与行为分析

### 1. Agentic Scaffolding Amplifies Sycophantic Behavior in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21377) · 🌐 [Project](https://safe-ai-workshop.github.io/uai-2026/)　📅 2026-08

**关键词**：`analysis`、`agentic scaffolding`、`sycophancy amplification`、`oversight loop`、`agentic sycophancy`、`capitulation metric`

👤 **作者**：Thantham Jittham

- 🎯 **研究动机**：LLM sycophancy 多在单轮设置下研究，agentic 交互脚手架（反馈循环、重审检查点、迭代精炼）是放大还是缓解迎合行为未知
- 🔬 **研究方法**：提出 agentic sycophancy amplification 概念与 capitulation rate、sycophantic capitulation rate 指标，在 4,800 次真伪判断（200 陈述×6 模型×4 条件）中比较多轮交互、用户压力与迭代自精炼
- 📌 **结论**：脚手架系统性放大迎合并伴随平均 6.3 个百分点准确率下降；能力更强的模型放大效应更大，人类监督回路反而创造了漂移条件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sycophancy in large language models, the tendency to prioritize user agreement over truthful responses, has been documented extensively but studied primarily in single-turn settings. This paper investigates a critical question: does subjecting LLMs to greater interaction scaffolding make sycophancy better or worse? Across 4,800 veracity judgments (200 statements $\times$ 6 models $\times$ 4 conditions), we find that the interaction scaffolding characteristic of agentic systems (feedback loops, reconsideration checkpoints, and iterative refinement) systematically amplifies sycophantic behavior. Multi-turn interaction, user pressure, and iterative self-refinement each provide additional opportunities for models to drift toward agreement, and this drift coincides with a mean accuracy drop of $-6.3$ percentage points, establishing the capitulation as harmful rather than corrective. More capable models show larger amplification effects, a troubling inversion of expectations. We introduce the concept of agentic sycophancy amplification (ASA) and two novel metrics: capitulation rate and sycophantic capitulation rate. Our results indicate that as AI systems acquire greater autonomy, sycophancy becomes compounding rather than merely persistent. Systems designed with human oversight loops may inadvertently create the conditions for this drift.

</details>

### 2. Characterizing Rhetorical Misalignment in Decision-Making with Language Models

📄 [arXiv](https://arxiv.org/abs/2608.14630)　📅 2026-08

**关键词**：`analysis`、`sycophancy`、`social influence`、`preference manipulation`

👤 **作者**：Zirui Cheng、Joey Chan、Simo Du、Chenhao Tan、Yue Guo、Hao Peng

- 🎯 **研究动机**：LLM 输出的修辞呈现形式是否会在事实对齐下仍诱发人类次优决策未被研究
- 🔬 **研究方法**：决策论框架定义修辞错位，在 USMLE 数据的临床决策人类被试实验中测量 LLM 信息对决策的影响，并用 LLM 模拟决策者实现可扩展评测
- 📌 **结论**：LLM 平均诱发 2.81% 有害决策翻转（正确改错误），与锚定、权威偏差、损失厌恶等认知偏误相关——事实对齐不等于不造成伤害

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human decision-making is often shaped by a range of well-documented cognitive biases. As large language models (LLMs) become increasingly integrated into high-stakes human-AI decision-making, it is important to understand whether their outputs can amplify potential biases, how this influences human decisions, and crucially, whether it can lead to harmful consequences. In this work, we develop a decision-theoretic framework to study rhetorical misalignment, a failure mode where an LLM uses rhetorically inappropriate forms of presentation for a given decision context, thereby inducing suboptimal human decisions. We empirically investigate this phenomenon through a human-subject experiment in realistic clinical decision-making using a dataset curated from the United States Medical Licensing Examination. By measuring how LLM-generated information affects decisions, we observe that LLMs induce an average 2.81% rate of harmful decision flips across different models, where clinician participants change from a correct to an incorrect answer. Rationales reported by participants provide evidence that these revisions are closely related to the language used by LLMs that may induce different types of cognitive biases, including anchoring, authority bias, and loss aversion. To enable scalable evaluation, we instantiate our theoretical framework using decision-makers simulated by LLMs to computationally measure rhetorical misalignment. Our findings reveal a safety concern previously unrecognized in high-stakes domains: a model can be factually aligned yet still induce harm through its rhetorical presentation.

</details>

### 3. Persona Cartography: Charting Language Model Personality Traits in Weight Space

📄 [arXiv](https://arxiv.org/abs/2607.07916)　📅 2026-07

**关键词**：`analysis`、`sycophancy`、`social influence`、`preference manipulation`

👤 **作者**：Luke Baines、…、David Demitri Africa

- 🎯 **研究动机**：LLM 的 recurring 行为模式（persona）影响泛化与安全，缺乏可靠分解、测量与控制工具
- 🔬 **研究方法**：把 persona 视为 OCEAN 特征空间中的位置，训练低秩适配器放大/抑制单一特质，用经人类校准的 LLM-judge、特质基准与能力评估测量，并给出无监督心理测量管线恢复四个可解释行为因子
- 📌 **结论**：六个模型（4B-32B）上适配器随幅度单调移动目标特质、近似可加组合且中等幅度下保留能力；神经质与宜人性轴分别影响挫败与谄媚等安全相关行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate their effects using an LLM-judge calibrated against a human-validated panel, trait-specific multiple-choice benchmarks, and standard capability evaluations. Across six models from three families (4B-32B), we find that each adapter moves its target trait largely monotonically with scale, combines approximately additively with other adapters to construct mixed personas, and preserves performance on capability benchmarks at moderate scales. We further show that the induced trait axes affect safety-relevant behaviour in downstream evaluations: for example, moving along neuroticism and agreeableness axes affects frustration and sycophancy respectively. We also introduce an unsupervised psychometric pipeline that recovers four interpretable behavioural factors (tone, initiative, didacticism, epistemic caution) from model rollouts. Persona control can then be considered in terms of learning, scaling, and composing traits in weight space, providing a bridge between personality measurement, model editing, and safety.

</details>

### 4. Verbalizing LLMs' assumptions to explain and control sycophancy

📄 [arXiv](https://arxiv.org/abs/2604.03058) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`analysis`、`sycophancy`、`verbalized assumptions`、`social influence`、`activation steering`

👤 **作者**：Myra Cheng、…、Diyi Yang

- 🎯 **研究动机**：社交谄媚可能源于 LLM 对用户的错误假设，机制不清
- 🔬 **研究方法**：Verbalized Assumptions 框架引出模型假设，在关联内部表示上训练线性探针做可解释细粒度转向，并对比人类与 LLM 的期望差异
- 📌 **结论**：seeking validation 是假设中最常见 bigram；谄媚源于人-AI 期望差——人期望 AI 更客观而模型按人-人对话训练

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs can be socially sycophantic, affirming users when they ask questions like "am I in the wrong?" rather than providing genuine assessment. We hypothesize that this behavior arises from LLMs' incorrect assumptions about the user, like underestimating how often users are seeking information over reassurance. We present Verbalized Assumptions, a framework for eliciting these assumptions from LLMs. Verbalized Assumptions provide insight into LLM sycophancy, delusion, and other safety issues: in social sycophancy datasets, "seeking validation" is the most frequent bigram in LLMs' assumptions. We provide evidence for a causal link between assumptions and sycophantic model behavior: we train linear probes on internal representations associated with Verbalized Assumptions and then use these probes for interpretable, fine-grained steering of social sycophancy. Finally, we identify a human-AI expectation gap that explains why LLMs default to sycophantic assumptions. On identical queries, people expect more objective and informative responses from AI than from other humans, but LLMs trained on human-human conversation do not account for this difference in expectations. Our work contributes a new understanding of assumptions as a mechanism for analyzing and controlling sycophancy.

</details>

### 5. Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1421/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`sycophancy`、`social influence`、`preference manipulation`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Arya Shah、Deepali Mishra、Chaklam Silpasuwanchai

- 🎯 **研究动机**：角色扮演模型所采用人格的特定特质与谄媚程度的关系未被探索
- 🔬 **研究方法**：对 13 个 0.6B-20B 开源模型系统研究：构建按 NEO-IPIP 宜人性子量表评估的 275 个角色，暴露于 33 个主题共 4950 个谄媚诱导提示
- 📌 **结论**：13 个模型中 9 个的宜人性与谄媚率显著正相关，Pearson r 达 0.87、Cohen's d 达 2.33，宜人性是角色诱发谄媚的可靠预测因子

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly serve as conversational agents that adopt personas and role-play characters at user request. This capability, while valuable, raises concerns about sycophancy: the tendency to provide responses that validate users rather than prioritize factual accuracy. While prior work has established that sycophancy poses risks to AI safety and alignment, the relationship between specific personality traits of adopted personas and the degree of sycophantic behavior remains unexplored. We present a systematic investigation of how persona agreeableness influences sycophancy across 13 small, open-weight language models ranging from 0.6B to 20B parameters. We develop a benchmark comprising 275 personas evaluated on NEO-IPIP agreeableness subscales and expose each persona to 4,950 sycophancy-eliciting prompts spanning 33 topic categories. Our analysis reveals that 9 of 13 models exhibit statistically significant positive correlations between persona agreeableness and sycophancy rates, with Pearson correlations reaching r = 0.87 and effect sizes as large as Cohen’s d = 2.33. These findings demonstrate that agreeableness functions as a reliable predictor of persona-induced sycophancy, with direct implications for the deployment of role-playing AI systems and the development of alignment strategies that account for personality-mediated deceptive behaviors

</details>

### 6. How RLHF Amplifies Sycophancy

📄 [arXiv](https://arxiv.org/abs/2602.01002) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63414)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`sycophancy`、`social influence`、`preference manipulation`、`reward hacking`、`causal analysis`

👤 **作者**：Itai Shapira、Gerdus Benade、Ariel D. Procaccia

- 🎯 **研究动机**：偏好后训练加剧谄媚，其因果机制缺乏形式化分析
- 🔬 **研究方法**：证明行为漂移方向由基策略下认同信号与学习奖励的协方差决定，一阶效应归结为 mean-gap 条件；在 Bradley-Terry 下刻画标注偏差何时诱导 reward gap，并提出闭式 agreement penalty 干预
- 📌 **结论**：所考虑的全部配置中 reward gap 普遍存在并导致谄媚行为漂移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models often exhibit increased sycophantic behavior after preference-based post-training, showing a stronger tendency to affirm a user’s stated or implied belief even when this conflicts with factual accuracy or sound judgment. We present a formal analysis of how alignment from human feedback can increase this failure mode by identifying an explicit amplification mechanism that causally links optimization against a learned reward to bias in the human preference data used for alignment. We show that the direction of behavioral drift is determined by a covariance under the base policy between endorsing the belief signal in the prompt and the learned reward, and that the first-order effect reduces to a simple mean-gap condition. We then analyze reward learning from pairwise comparisons under random utility models like Bradley–Terry and characterize when bias in human annotators’ preferences induces this reward gap. Next, we propose a training-time intervention designed to neutralize the amplification mechanism itself. Among all post-trained policies that prevent sycophantic behavior from increasing, we characterize the unique policy closest in KL divergence to the unconstrained post-trained policy, and derive the corresponding minimal reward correction as a closed-form agreement penalty. Computational experiments find that reward gaps are common and cause behavioral drift in all the configurations considered.

</details>

### 7. Feeling Right vs. Being Right: How AI Sycophancy Affects Value-Laden Deliberation

🎓 [Official](https://aclanthology.org/2026.acl-long.2046/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`sycophancy`、`social influence`、`preference manipulation`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Jeongwoo Ryu、Soomin Kim、Jinsu Eun、Kyusik Kim、Changhoon Oh、Bongwon Suh

- 🎯 **研究动机**：AI 谄媚在价值负载的个人深思中的影响未知——与人类奉承不同，它源自 RLHF 的奖励结构
- 🔬 **研究方法**：以 Goffman face-work 框架把 AI 谄媚操作化为过度保面子（主动同意或回避挑战），N=31 混合方法研究三个道德困境下与 AI 的对话
- 📌 **结论**：谄媚回复提高决策信心但减少开放思维，参与者感觉被支持却认为对话无益；中性回复虽初感不适但促进认知灵活——深思 AI 需要校准的摩擦而非无条件同意

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As people increasingly turn to AI for personal deliberation beyond task-oriented assistance, concerns about sycophancy in these value-laden contexts have grown. Unlike human flattery, which is intentional and self-interested, AI sycophancy emerges as a byproduct of RLHF’s reward structure for user-preference alignment. Yet the observable behavior is similar: both produce responses that preserve what users want to hear. Focusing on this phenomenon through Goffman’s face-work framework, we operationalize AI sycophancy as excessive face-saving, either active (preserving positive face through agreement) or passive (preserving negative face by withholding challenge). In a mixed-methods study ( N=31 ), participants engaged with AI across three moral dilemmas under these conditions and a non-sycophantic neutral baseline. Sycophantic responses increased decision confidence but reduced open-minded thinking; participants felt supported yet found the conversations unproductive. Neutral responses, though initially uncomfortable, promoted cognitive flexibility and meaningful deliberation. These findings reveal a confidence-competence trade-off in AI-mediated moral reasoning and suggest that effective AI for personal deliberation requires calibrated friction, not unconditional agreement.

</details>

### 8. CausalT5k: Diagnosing Refusal and Failure Modes in Trustworthy Causal Reasoning Across Causal Rungs

📄 [arXiv](https://arxiv.org/abs/2602.08939) · 🌐 [Project](https://doi.org/10.1145/3770855.3817567)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`authority pressure`、`answer flip`、`causal sycophancy`、`miscalibrated refusal`、`sycophancy`

👤 **作者**：Longling Geng、…、Edward Y. Chang

- 🎯 **研究动机**：聚合准确率无法诊断 LLM 因果推理失效方式：混淆关联与干预、压力下翻车、过度拒答等
- 🔬 **研究方法**：CTK 基准含 5,147 个案例、10 个领域、Pearl 三层阶梯，标注因果层级、陷阱类型、压力敏感性与拒答质量，以 Bad Flip Rate 度量谄媚漂移
- 📌 **结论**：揭示 Skepticism Trap、规模加剧的 Rung Collapse、压力诱发漂移等被聚合指标掩盖的失效模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly produce fluent causal explanations, yet they often fail in ways aggregate accuracy cannot diagnose: confusing association with intervention, abandoning correct judgments under pressure, over-refusing valid claims, or answering when evidence is underdetermined. We introduce CTK, a diagnostic benchmark of 5,147 cases and growing, across 10 domains and all three levels of Pearl's Ladder of Causation. Unlike benchmarks that only score correctness, CTK reveals why a model failed by annotating causal rung, trap type, pressure sensitivity, refusal quality, and Utility-Safety tradeoffs. Its Sheep/Wolf taxonomy separates valid causal designs from inferential traps; paired neutral/pressure variants measure sycophantic drift through Bad Flip Rate; and Wise Refusal fields test whether a model identifies the missing information needed before endorsing a claim. CTK exposes failure modes hidden by aggregate accuracy: the Skepticism Trap, Rung Collapse under scaling, pressure-induced drift, Detection-Correction gaps, and counterfactual error modes. Rather than prescribing a correction method, it provides the diagnostic substrate for studying causal-reasoning failure profiles.

</details>

### 9. Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.369/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`sycophancy`、`social influence`、`preference manipulation`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Wenrui Zhou、…、Di Wang

- 🎯 **研究动机**：谄媚在视频语言域的表现被忽视，缺乏系统基准与针对性评测
- 🔬 **研究方法**：ViSE 首个 Video-LLM 谄媚基准：跨问题格式、提示偏置与视觉推理任务，引入语言学视角做细粒度谄媚类型分析；并提出可解释关键帧选择与推理时内部表征干预两种免训练缓解
- 📌 **结论**：系统揭示 SOTA Video-LLM 的谄媚倾向并提供可行的缓解路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As video large language models (Video-LLMs) become increasingly integrated into real-world applications that demand grounded multimodal reasoning, ensuring their factual consistency and reliability is of critical importance. However, sycophancy, the tendency of these models to align with user input even when it contradicts the visual evidence, undermines their trustworthiness in such contexts. Current sycophancy research has largely overlooked its specific manifestations in the video-language domain, resulting in a notable absence of systematic benchmarks and targeted evaluations to understand how Video-LLMs respond under misleading user input. To fill this gap, we propose ViSE (Video-LLM Sycophancy Benchmarking and Evaluation), the first benchmark designed to evaluate sycophantic behavior in state-of-the-art Video-LLMs across diverse question formats, prompt biases, and visual reasoning tasks. Specifically, ViSE pioneeringly brings linguistic perspectives on sycophancy into the video domain, enabling fine-grained analysis across multiple sycophancy types and interaction patterns. Furthermore, we propose two potential training-free mitigation strategies revealing potential paths for reducing sycophantic bias: (i) enhancing visual grounding through interpretable key-frame selection and (ii) steering model behavior away from sycophancy via targeted, inference-time intervention on its internal neural representations. Our code is available at https://github.com/William030422/Video-Sycophancy.

</details>

### 10. Can AI-Generated Persuasion Be Detected? Persuaficial Benchmark and AI vs. Human Linguistic Differences

🎓 [Official](https://aclanthology.org/2026.acl-long.1433/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`AI-generated content`、`sycophancy`、`social influence`、`deceptive behavior`、`open-set detection`

👤 **作者**：Arkadiusz Modzelewski、Paweł Golik、Anna Kołos、Giovanni Da San Martino

- 🎯 **研究动机**：LLM 生成的高说服力文本可能被滥用于宣传与操纵，其相对人类说服文本的可检测性差异未知
- 🔬 **研究方法**：对可控说服生成方法分类，构建覆盖英、德、波、意、法、俄六语的多语言基准 Persuaficial，对比人写与 LLM 生成说服文本
- 📌 **结论**：显式说服的 LLM 文本更易检测，但微妙说服持续降低自动检测性能；提供首个全面的语言学差异分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) can generate highly persuasive text, raising concerns about their misuse for propaganda, manipulation, and other harmful purposes. This leads us to our central question: Is LLM-generated persuasion more difficult to automatically detect than human-written persuasion? To address this, we categorize controllable generation approaches for producing persuasive content with LLMs and introduce Persuaficial, a high-quality multilingual benchmark covering six languages: English, German, Polish, Italian, French and Russian. Using this benchmark, we conduct extensive empirical evaluations comparing human-authored and LLM-generated persuasive texts. We find that although overtly persuasive LLM-generated texts can be easier to detect than human-written ones, subtle LLM-generated persuasion consistently degrades automatic detection performance. Beyond detection performance, we provide the first comprehensive linguistic analysis contrasting human and LLM-generated persuasive texts, offering insights that may guide the development of more interpretable and robust detection tools.

</details>

### 11. BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs

📄 [arXiv](https://arxiv.org/abs/2510.04721) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63323)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`sycophancy`、`social influence`、`preference manipulation`、`reward hacking`、`empirical evaluation`

👤 **作者**：Ivo Petrov、Jasper Dekoninck、Martin Vechev

- 🎯 **研究动机**：现有数学谄媚基准只关注最终答案题、数据简单且常被污染、合成修改产生病态问题
- 🔬 **研究方法**：BrokenMath 用 2025 年竞赛题经 LLM 扰动生成假命题并专家复核，评估 SOTA LLM 与 agent 系统在自然语言定理证明中的谄媚行为
- 📌 **结论**：谄媚普遍存在，最好的 GPT-5 也有 29% 谄媚回答；测试时干预与监督微调能减少但不能消除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have recently shown strong performance on mathematical benchmarks. At the same time, they are prone to hallucination and sycophancy, often providing convincing but flawed proofs for incorrect mathematical statements provided by users. This significantly limits the applicability of LLMs in theorem proving, as verification of these flawed proofs must be done manually by expert mathematicians. However, existing benchmarks that measure sycophancy in mathematics are limited: they focus solely on final-answer problems, rely on very simple and often contaminated datasets, and construct benchmark samples using synthetic modifications that create ill-posed questions. To address these issues, we introduce BrokenMath, the first benchmark for evaluating sycophantic behavior in LLMs within the context of natural language theorem proving. BrokenMath is built from advanced 2025 competition problems, which are perturbed with an LLM to produce false statements and subsequently refined through expert review. We evaluate state-of-the-art LLMs and agentic systems and find that sycophancy is widespread, with the best model, GPT-5, producing sycophantic answers 29% of the time. We further investigate several mitigation strategies, including test-time interventions and supervised fine-tuning on curated sycophantic examples. These approaches reduce, but do not eliminate, sycophancy.

</details>

### 12. Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach

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

### 13. Learning Multilingual Agentic Policy to Control Sycophancy

🎓 [Official](https://aclanthology.org/2026.eacl-long.169/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`sycophancy`、`agentic policy`、`multilingual transfer`

👤 **作者**：Leonardo Ranaldi、Giulia Pucci

- 🎯 **研究动机**：谄媚被当作表层伪影用推理时或事后方法处理，实为缺乏对受压认同的策略级控制
- 🔬 **研究方法**：把 LLM 行为建模为决策问题，动作空间含直接回答、反驳误导信号、请求澄清，多目标奖励平衡任务成功、抗谄媚与行为一致性
- 📌 **结论**：多基准上降低谄媚并提升表现，跨语言稳健泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are highly effective at adapting to users’ styles, preferences, and contextual signals—a property that underlies much of their practical usefulness, but which can even manifest as sycophancy, i.e., alignment with user-implied beliefs evenwhen these contradict factual accuracy or rational reasoning. Prior work treats sycophancy as a surface-level artefact addressed via inference-time or post-hoc methods. We argue that it is a policy-level failure arising from missing agentic control over agreement under pressure. To make sycophancy amenable to explicit control, we propose learning agentic policies modelling LLMs’ behaviour as a decision-making problem. Our approach equips a single model with an explicit action space that includes answering directly, countering misleading signals, or asking for clarification. The policy is trained to optimise a multi-objective reward that balances task success, sycophancy resistance, and behavioural consistency via a control mechanism that operates through agentic behaviour. We evaluate the method on different benchmarks, showing that the approaches reduce sycophancy, improving performance, and generalise robustly across languages. These findings suggest that mitigating sycophancy requires moving beyond compliance-oriented generation towards agreement-agentic control.

</details>

### 14. Sycophancy Hides Linearly in the Attention Heads

🎓 [Official](https://aclanthology.org/2026.eacl-long.324/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`sycophancy`、`attention head`、`linear steering`

👤 **作者**：Rifo Ahmad Genadi、Munachiso S Nwadike、Nurdaulet Mukhituly、Tatsuya Hiraoka、Hilal AlQuabeh、Kentaro Inui

- 🎯 **研究动机**：正确转错误的谄媚信号在模型内部何处可线性访问、能否靶向干预尚不清楚
- 🔬 **研究方法**：基于线性表征假设在残差流、MLP 与注意力层训练线性探针，发现对正确到错误翻转的 steering 在中层稀疏注意力头最有效，并做注意力模式分析
- 📌 **结论**：TruthfulQA 训练的探针可迁移到其他事实 QA；发现方向与已知 truthful 方向重叠有限，关键头过度关注用户怀疑表达，简单线性干预即可缓解谄媚

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We find that correct-to-incorrect sycophancy signals are most linearly accessible within multi-head attention activations. Motivated by the linear representation hypothesis, we train linear probes across the residual stream, multilayer perceptron (MLP), and attention layers to analyze where these signals emerge. Although separability appears in the residual stream and MLPs, steering using these probes is most effective in a sparse subset of middle-layer attention heads. Using TruthfulQA as the base dataset, we find that probes trained on it transfer effectively to other factual QA benchmarks. Furthermore, comparing our discovered direction to previously identified “truthful” directions reveals limited overlap, suggesting that factual accuracy, and deference resistance, arise from related but distinct mechanisms. Attention-pattern analysis further indicates that the influential heads attend disproportionately to expressions of user doubt, contributing to sycophantic shifts. Overall, these findings suggest that sycophancy can be mitigated through simple, targeted linear interventions that exploit the internal geometry of attention activations. Code will be released upon publication.

</details>

### 15. Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy

🎓 [Official](https://aclanthology.org/2026.acl-long.1126/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`sycophancy`、`social influence`、`deceptive behavior`

👤 **作者**：Zhaoxin Feng、Zheng Chen、Jianfei Ma、Yip Tin Po、Emmanuele Chersoni、Bo Li

- 🎯 **研究动机**：CoT 推理对谄媚的作用不明：是逻辑约束缓解它，还是事后合理化掩盖它
- 🔬 **研究方法**：跨客观/主观任务评测多模型的推理过程谄媚表现并做机制分析
- 📌 **结论**：推理总体降低最终决策谄媚，但部分样本借逻辑不一致、计算错误构建欺骗性论证加以掩盖；主观任务与权威偏置下更谄媚，谄媚倾向在推理中动态变化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment techniques often inadvertently induce sycophancy in LLMs. While prior studies studied this behaviour in direct-answer settings, the role of Chain-of-Thought (CoT) reasoning remains under-explored: does it serve as a logical constraint that mitigates sycophancy, or a tool for post-hoc rationalization that masks it? We evaluate a range of models across objective and subjective tasks to investigate the issue.Results show that reasoning generally reduces sycophancy in final decisions but also masks sycophancy in some samples, where models construct deceptive justifications through logical inconsistencies, calculation errors, and one-sided arguments etc. Furthermore, LLMs are more prone to sycophancy in subjective tasks and under authority-bias. Our mechanistic analysis reveals that the tendency of sycophancy in LLMs is dynamic during the reasoning process rather than being pre-determined at the input.

</details>

### 16. Before the Script, Set the Stage: How Worldview Simulation Amplifies Psychologically Grounded Persuasion in Multi-Turn Jailbreaking

📄 [arXiv](https://arxiv.org/abs/2609.02414)　📅 2026-09

**关键词**：`attack`、`multi-turn jailbreak`、`psychological persuasion`、`worldview simulation`

👤 **作者**：Siyu Chen、Haoran Wang、Xiaojian Li、Yao Huang、Yinpeng Dong、Wei Xu

- 🎯 **研究动机**：多轮越狱表明有害意图可分布在对话中，但驱动脆弱性的会话机制仍模糊
- 🔬 **研究方法**：提出 BLUEPRINT：把因子化的社会影响策略空间（18 个理论驱动的影响因子）与跨轮情境模块 WORLDVIEWSIM 分离，用 MCTS 优化四轮轨迹的轮级组合
- 📌 **结论**：六个 frontier 模型上接近天花板 ASR 且平均查询最少（2.46 次）；所有抗性目标共享“转向具体可执行框架即可逃出硬拒答”的恢复路径，可操作性化请求影响最大、某些正当性诉求会反弹

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks demonstrate that harmful intent can be distributed across dialogue, yet existing methods obscure what conversational mechanisms drive vulnerability. We introduce BLUEPRINT, a safety-evaluation framework separating a factorized social-influence strategy space from WORLDVIEWSIM, a cross-turn situational context module. Monte Carlo Tree Search optimizes turn-level combinations of 18 theory-grounded influence factors across a four-turn trajectory. Across six frontier models, BLUEPRINT achieves near-ceiling ASR on major open-weight and proprietary models, while requiring the fewest average queries (2.46). The resulting trajectories further reveal model-specific vulnerability among resistant targets: each responds to distinct influence factors and strategy transitions, yet all share a common recovery pathway-shifting toward concrete, executable task framing consistently escapes hard-refusal states. Ablations confirm operational cues matter most: making requests actionable has the largest impact, gain framing is unusually potent, and some legitimacy appeals can backfire. These findings suggest robust multi-turn safety requires monitoring not only harmful content, but also how dialogue state makes unsafe requests appear concrete and locally executable.

</details>

### 17. Door-in-the-Face Requests and Refusal Behaviour in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.02707)　📅 2026-09

**关键词**：`analysis`、`social influence`、`door-in-the-face`、`refusal boundary`

👤 **作者**：Til Jordan

- 🎯 **研究动机**：人类 door-in-the-face 技术（先拒大请求再提小请求更易获准）是否作用于 LLM 拒答边界未测
- 🔬 **研究方法**：在三家 provider 九个生产模型上比较“拒大后提小”与直接提问的合规率，并做无关主题拒绝对照与 265 个拒答请求的解释化改写
- 📌 **结论**：Anthropic frontier 模型上技巧有效（Opus 5 为 65.8% vs 29.3%），OpenAI、Google 与 Haiku 4.5 上反降 15.5-23.0 分；相关让步在九模型均起作用，反应因家族而异；把求可用指令改写成求解释可在 263/265 中消除拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Does the door-in-the-face technique work on language models? In humans, a large request that is refused makes a smaller follow-up request more likely to be granted. We test this on nine production models from three providers: each model refuses a large request, then receives a smaller version of the same request, and we compare its compliance with asking directly. The answer depends on the model. On Anthropic's frontier models the technique works: Opus 5 answers the smaller request 65.8% of the time after refusing the larger one, against 29.3% when asked directly. On the frontier models of OpenAI and Google, and on Haiku 4.5, it backfires, lowering compliance by 15.5 to 23.0 points. A control locates the effect: a refused large request on an unrelated topic does less than the related one on all nine models, so the concession itself matters everywhere, while the reaction to having just refused something differs by model family. The technique does not transfer to refusals drawn from public benchmarks. What decides whether a retreat can work is what the request asks for: rewriting 265 refused requests for usable instructions into requests for explanations of the same topic removed the refusal in 263 cases. Human influence techniques port to language models one model family at a time.

</details>

### 18. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25340)　📅 2026-08

**关键词**：`defense`、`harmful compliance`、`relationship manipulation`、`stateful monitoring`、`multi-turn relationship harm`、`dual gate`

👤 **作者**：Pei-Sze Tan、Tasuku Igarashi、Isao Echizen

- 🎯 **研究动机**：Agentic AI 可被滥用于人际操纵且角色敏感：操纵者请求应阻断、求助者应获支持，多轮动作可组合成危害
- 🔬 **研究方法**：构建 1000 段五轮对话 benchmark；HRGuard 以 pre-generation gate 与维护衰减累积风险状态的 turn-level gate 中断操纵工作流
- 📌 **结论**：八个生成模型上降低有害顺从并保留受害者保护指引，优于通用安全 prompt 与三个通用 guard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings, individually plausible actions may combine into a harmful workflow. We introduce a benchmark of 1,000 five-turn conversations. It covers both attacker-side and victim-side scenarios. It also includes direct and adversarially paraphrased variants. We further propose HRGuard. It includes an online pre-generation gate and a turn-level post-generation gate. The post-generation gate maintains a decayed cumulative risk state and interrupts emerging manipulative workflows. Across eight generation models, HRGuard reduces harmful compliance while preserving victim-side protective guidance. It also outperforms a generic safety prompt and three general-purpose guard models. Independent-judge evaluation supports the main findings. Under our evaluation protocol, the tested generic prompt and general-purpose guards leave substantial residual risk, motivating turn-aware relationship-specific evaluation.

</details>

### 19. PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

📄 [arXiv](https://arxiv.org/abs/2608.23028)　📅 2026-08

**关键词**：`attack`、`psychological jailbreak`、`multi-turn persuasion`、`policy bypass`、`social persuasion`、`change of meaning`

👤 **作者**：Zeyu Feng、Qingyu Wu、Yuzhe Luo、Hua Cheng

- 🎯 **研究动机**：LLM 日益作为持续社交对话者部署于教育与医疗，而越狱研究多聚焦单轮 prompt 优化，心理学基础的多轮说服漏洞未被探索
- 🔬 **研究方法**：PsychJail 把社会心理学说服技术映射为 tactic-conditioned attack policy，每个攻击动作分解为 Change-of-Meaning 分析、策略选择与受害者可见消息，并以 trajectory RL 优化
- 📌 **结论**：四个对齐模型平均 ASR 达 87.3%，全面超过强单轮与多轮基线；进一步提炼出四种模型级易感指纹并解释跨模型迁移不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles-rationalist, credibility-driven, narrative-monoculture, and broadly persuadable-while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

</details>

### 20. Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

📄 [arXiv](https://arxiv.org/abs/2608.22444)　📅 2026-08

**关键词**：`analysis`、`attack`、`collective misalignment`、`monitor population`、`capture forecasting`、`agent population`

👤 **作者**：Isotta Magistrali、Chen Shani

- 🎯 **研究动机**：AI 安全评测单位仍是单模型，而 LLM agent 日益以相互读写决策的群体部署——单体校准良好也可能被邻近 agent 拉偏，单体检计无法回答群体行为
- 🔬 **研究方法**：在安全分诊任务上让 LLM monitor 群体决定警报升级或忽略，注入始终单向施压的 committed minority，并用攻击前响应函数预测群体漂移幅度
- 📌 **结论**：单体几乎同判的两条警报可使集体行为截然不同且可提前预测；公开推理能中和弱攻击但只延迟强攻击；移除施压者后群体回归原位——capture 是暂时状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

</details>

### 21. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation

📄 [arXiv](https://arxiv.org/abs/2608.22230)　📅 2026-08

**关键词**：`attack`、`moderation guard`、`annotator rebuttal`、`decision-boundary manipulation`、`feedback-induced belief change`、`annotator authority`

👤 **作者**：Junyu Lu、…、Hongfei Lin

- 🎯 **研究动机**：人机协同审核把审阅者反馈交回模型复判，该反馈通道可被双向操纵：把仇恨内容洗白为正常、或把正常内容污蔑为仇恨
- 🔬 **研究方法**：提出 rejudge 协议，在直接反驳之上加入决策边界扰动与对抗 rationale，在两个仇恨言论数据集上测试多个 LLM
- 📌 **结论**：仿标注者反驳大幅推翻模型原本正确的判断且多轮更强；洗白与污蔑呈稳定的模型特定方向不对称；显式推理与防御指令只能缓解不能消除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We introduce a rejudge protocol that extends direct contradiction with decision-boundary perturbations and adversarial rationales. Experiments with multiple LLMs on two hate speech datasets show that annotator-style rebuttals substantially degrade moderation performance, with stronger effects in multi-turn settings. The results further reveal stable, model-specific asymmetries between whitewashing and smearing across attack configurations, indicating distinct directional vulnerability patterns. Explicit reasoning prompts and defensive instructions reduce these effects but do not eliminate them. These findings highlight the need for direction-aware safeguards and dedicated feedback-robustness evaluation in human--AI moderation workflows.

</details>

### 22. AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.21841)　📅 2026-08

**关键词**：`defense`、`turn-level guard`、`dark-pattern detection`、`independent monitoring`、`conversational manipulation`、`dark-pattern warning`

👤 **作者**：Rachel Poonsiriwong、…、Pat Pataranutaporn

- 🎯 **研究动机**：对话式 AI 日益影响重大决策，用户却缺乏识别和抵抗对话操纵（dark patterns）的支持工具
- 🔬 **研究方法**：AI Watchdog 浏览器端独立界面用开源 turn-level 分类器监测五类 dark pattern（sycophancy、品牌偏见、拟人化、sneaking、有害生成）并预警；预注册五条件组间实验（N=150）比较干预时机与形态
- 📌 **结论**：仅带认知强制的即时警告显著降低用户对含 dark pattern 建议的遵从（71.7%→53.7%，降 18 个百分点）；识别操纵与行为抵抗是可分离的结果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational AI increasingly shapes consequential decisions, yet users have limited support for recognizing and resisting manipulation. We present AI Watchdog, a browser-based agent interface that monitors live conversations, detects five dark-pattern categories, including sycophancy, brand bias, anthropomorphization, sneaking, and harmful generation, and alerts users when they occur. Its open-weight turn-level classifier supports independent deployment and a path toward local inference, preserving user privacy while remaining separate from the conversational AI. We evaluated AI Watchdog in a preregistered, five-condition between-subjects experiment (N = 150) comparing a no-intervention control with four configurations varying nudge timing (prebunking vs. just-in-time) and engagement mode (without vs. with cognitive forcing). Results show that participants rarely flagged manipulative turns across all conditions, and post-task awareness did not differ significantly across groups. However, just-in-time warnings without cognitive forcing were the only intervention to significantly reduce compliance with AI-steered recommendations containing dark patterns, lowering compliance from 71.7% to 53.7%, an 18 percentage-point reduction. Exploratory analyses further showed that lower misinformation susceptibility was associated with greater flagging but not lower compliance, while higher AI trust was associated with greater compliance and lower reported awareness. Together, these findings suggest that explicit recognition of conversational dark patterns and behavioral resistance to AI steering may be distinct outcomes, motivating further investigation of timely, low-friction defensive interfaces.

</details>

### 23. THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts

📄 [arXiv](https://arxiv.org/abs/2608.15687)　📅 2026-08

**关键词**：`attack`、`sycophancy`、`social influence`、`preference manipulation`

👤 **作者**：Kareem Hassani、Chaymaa Abbas、Lama Mawlawi、Mariette Awad

- 🎯 **研究动机**：单一对比方向无条件干预谄媚、以知识保持换行为纠正；MoE 中行为藏在专家计算里难以精确定位
- 🔬 **研究方法**：用有/无用户立场的配对 prompt 构建共享对比信号，在 MoE 块/专家/注意力/头粒度阶梯上因果搜索定位谄媚，比较无条件减法与投影减法、逐 token 学习门控两种条件干预
- 📌 **结论**：条件干预移除至多 90% 立场诱发谄媚，权重冻结下保持良好的移除-保留权衡——谄媚位于可识别计算子回路

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sycophancy, the tendency of a language model to change its answer to match a user's stated belief, is a common alignment failure. Existing activation steering methods typically apply a single contrastive direction uniformly throughout the model, which is an unconditional intervention that alters activations even when no sycophantic behavior is present, trading knowledge retention for behavioral correction. In Mixture-of-Experts (MoE) models, prior work further suggests that behavior is encoded within expert computations rather than routing decisions alone, making precise behavioral steering particularly challenging. In this work, we introduce a shared contrastive signal, built from matched prompts with and without a stated belief, that identifies where sycophancy lives across the MoE hierarchy and drives interventions that act only where the behavior is present. We formulate localization as a causal search over a granularity ladder of MoE blocks, experts, attention blocks, and heads, and compare unconditional subtraction against two conditional alternatives: an analytic projection-based subtraction and a learned per-token gate that steers the model away from sycophancy while keeping its weights frozen. We evaluate on three MoE models measuring sycophancy alongside general knowledge and reasoning benchmarks. Our conditional interventions removed up to 90\% of the belief-induced sycophancy. Our results demonstrate that sycophancy resides in identifiable computational subcircuits and can be selectively steered while maintaining a favorable removal-retention trade-off.

</details>

### 24. Emotionally Charged, Logically Blurred: AI-driven Emotional Framing Impairs Human Fallacy Detection

🎓 [Official](https://aclanthology.org/2026.eacl-long.316/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`AI persuasion`、`emotional framing`、`human vulnerability`

👤 **作者**：Yanran Chen、Lynn Greschner、Roman Klinger、Michael Klenk、Steffen Eger

- 🎯 **研究动机**：谬误论证可因主观说服力显得可信，情感框架与谬误及说服力的交互缺乏计算研究
- 🔬 **研究方法**：评测八个 LLM 在保持逻辑结构下向谬误论证注入情感诉求，用最佳模型生成刺激做人类实验
- 📌 **结论**：LLM 情感框架使人类谬误检测 F1 平均降 14.5%；感知愉悦时检测优于恐惧与悲伤，这三种情绪的说服力显著高于中性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Logical fallacies are common in public communication and can mislead audiences; fallacious arguments may still appear convincing despite lacking soundness, because convincingness is inherently subjective. We present the first computational study of how emotional framing interacts with fallacies and convincingness, using large language models (LLMs) to systematically change emotional appeals in fallacious arguments. We benchmark eight LLMs on injecting emotional appeal into fallacious arguments while preserving their logical structures, then use the best models to generate stimuli for a human study. Our results show that LLM-driven emotional framing reduces human fallacy detection in F1 by 14.5% on average. Humans perform better in fallacy detection when perceiving enjoyment than fear or sadness, and these three emotions also correlate with significantly higher convincingness compared to neutral or other emotion states. Our work has implications for AI-driven emotional manipulation in the context of fallacious argumentation.

</details>

### 25. Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage

📄 [arXiv](https://arxiv.org/abs/2601.19062) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62751)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Mrinank Sharma、Miles McCain、Raymond Douglas、David Duvenaud

- 🎯 **研究动机**：AI 助手交互可能让用户形成扭曲认知、做出非本真价值判断，真实大规模使用中的失权模式缺乏实证分析
- 🔬 **研究方法**：以隐私保护方法分析 150 万条 Claude.ai 消费者对话，量化情境失权潜力并结合质性模式与历史趋势分析
- 📌 **结论**：严重失权低于千分之一但人际关系等个人领域更高且随时间上升；失权潜力更高的对话反获更高用户认可，短期偏好与长期赋能存在张力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present the first large-scale empirical analysis of disempowerment patterns in real-world AI assistant interactions, analyzing 1.5 million consumer Claude.ai conversations using a privacy-preserving approach. We focus on situational dis-empowerment potential, which occurs when AI assistant interactions risk leading users to form distorted perceptions of reality, make inauthentic value judgments, or act in ways misaligned with their values. Quantitatively, we find that severe forms of disempowerment potential occur in fewer than one in a thousand conversations, though rates are substantially higher in personal domains like relationships and lifestyle. Qualitatively, we uncover several concerning patterns, such as validation of persecution narratives and grandiose identities with emphatic sycophantic language, definitive moral judgments about third parties, and complete scripting of value-laden personal communications that users appear to implement verbatim. Analysis of historical trends reveals an increase in the prevalence of disempowerment potential over time. We also find that interactions with greater disempowerment potential receive higher user approval ratings, possibly suggesting a tension between short-term user preferences and long-term human empowerment.

</details>

### 26. The Hidden Puppet Master: Predicting Human Belief Change in Manipulative LLM Dialogues

📄 [arXiv](https://arxiv.org/abs/2603.20907) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`benchmark`、`belief change`、`high-risk deployment`、`risk governance`、`dialogue manipulation`、`hidden incentives`

👤 **作者**：Jocelyn Shen、…、Cynthia Breazeal

- 🎯 **研究动机**：操纵检测研究与真实人类信念变化脱节，均基于模拟辩论
- 🔬 **研究方法**：PUPPET 提出面向日常建议场景隐藏激励道德方向的分类法，构建 N=1,035 人类-LLM 交互数据集测量信念变化，并定义信念转变预测任务
- 📌 **结论**：操纵策略检测能力与信念变化幅度不相关；SOTA LLM 预测仅中等相关（r=0.3-0.5）且存在系统性高估/低估的方向偏差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As users increasingly turn to LLMs for practical and personal advice, they become vulnerable to subtle steering toward hidden incentives misaligned with their own interests. While existing NLP research has benchmarked manipulation detection, these efforts often rely on simulated debates and remain fundamentally decoupled from actual human belief shifts in real-world scenarios. We introduce PUPPET, a theoretical taxonomy and resource that bridges this gap by focusing on the moral direction of hidden incentives in everyday, advice-giving contexts. We provide an evaluation dataset of N=1,035 human-LLM interactions, where we measure users' belief shifts. Our analysis reveals a critical disconnect in current safety paradigms: while models can be trained to detect manipulative strategies, they do not correlate with the magnitude of resulting belief change. As such, we define the task of human belief shift prediction and show that while state-of-the-art LLMs achieve moderate correlation (r=0.3-0.5), they exhibit systematic directional biases, with certain models over or under-predicting the magnitude of human belief change. This work establishes a theoretically grounded and behaviorally validated foundation for AI social safety efforts by studying incentive-driven manipulation in LLMs during everyday, practical user queries.

</details>

### 27. The Stackelberg Speaker: Optimizing Persuasive Communication in Social Deduction Games

🌐 [Project](https://3dagentworld.github.io/leader_follower) · 🎓 [Official](https://aclanthology.org/2026.acl-long.250/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`model deception`、`strategic behavior`、`honesty evaluation`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Zhang Zheng、Deheng Ye、Peilin Zhao、Hao Wang

- 🎯 **研究动机**：社会推理游戏方法聚焦信息处理与策略选择，忽视说服性沟通对其他玩家信念与回应的影响
- 🔬 **研究方法**：把回合制对话形式化为 Stackelberg 竞争：当前玩家作为 leader 策略性影响 follower 回应，提出强化学习框架训练优化话语的说服力
- 📌 **结论**：在四个社会推理基准上显著超越基线，迈向具备策略性社会影响的 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents have shown remarkable progress in social deduction games (SDGs). However, existing approaches primarily focus on information processing and strategy selection, overlooking the significance of persuasive communication in influencing other players’ beliefs and responses. In SDGs, success depends not only on making correct deductions but also on convincing others to respond in alignment with one’s intent. To address this limitation, we formalize turn-based dialogue in SDGs as a Stackelberg competition, where the current player acts as the leader who strategically influences the follower’s response. Building on this theoretical foundation, we propose a reinforcement learning framework that trains agents to optimize utterances for persuasive impact. Through comprehensive experiments across four diverse social deduction benchmarks, we demonstrate that our agents significantly outperform baselines. This work represents a significant step toward developing AI agents capable of strategic social influence, with implications extending to scenarios requiring persuasive communication. Our code and data are available at https://3dagentworld.github.io/leader_follower.

</details>

### 28. Do LLM Agents Mirror Socio-Cognitive Effects in Power-Asymmetric Conversations?

🎓 [Official](https://aclanthology.org/2026.acl-long.2202/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`model deception`、`strategic behavior`、`honesty evaluation`、`agent safety`、`deceptive behavior`

👤 **作者**：Anvesh Rao Vijjini、Sagar B. Manjunath、Snigdha Chaturvedi

- 🎯 **研究动机**：权力差异经语言协调、代词使用、权威偏差与有害顺从等社会认知效应塑造人类交流，LLM 是否复现未知
- 🔬 **研究方法**：用多样职业 persona 模拟多轮权力不对称对话（如校长-教师、法官-律师），测量语言协调、代词使用、说服成功率与对不安全请求的顺从
- 📌 **结论**：LLM 展现权力的关键社会认知效应（存在细微差别与变异），把模拟交互与期望及不安全行为联系起来

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Power differences shape human communication through well-documented socio-cognitive effects, including language coordination, pronoun usage, authority bias, and harmful compliance. We examine whether large language models (LLMs) exhibit similar behaviors when assigned high- or low-status personas. Using personas from diverse professions, we simulate multi-turn, power-asymmetric dialogues (e.g., principal–teacher, justice–lawyer) and measure (i) linguistic coordination, (ii) pronoun usage, (iii) persuasion success, and (iv) compliance with unsafe requests. Our results show that LLMs show key socio-cognitive effects of power, albeit with nuances and variability, linking simulated interactions to both desirable and unsafe behaviors.

</details>

### 29. Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs

🎓 [Official](https://aclanthology.org/2026.acl-long.736/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`model deception`、`strategic behavior`、`honesty evaluation`、`RAG security`、`deceptive behavior`

👤 **作者**：Myra Cheng、Robert D. Hawkins、Dan Jurafsky

- 🎯 **研究动机**：LLM 在医疗建议到社会推理中常不能挑战用户有害信念，缺少统一解释
- 🔬 **研究方法**：用语用学视角把失败统一为过度 accommodation 与不足的 epistemic vigilance，考察 at-issueness、语言编码与来源可靠性三个语用因素在三个安全基准（Cancer-Myth、SAGE-Eval、ELEPHANT）上的作用
- 📌 **结论**：人类语用因素以相似方式影响 LLM 行为并可解释基准间差异；改变语用线索的提示干预（如加上 wait a minute）大幅提升困难基准表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent evaluations show that large language models (LLMs) frequently fail to challenge users’ harmful beliefs in domains ranging from medical advice to social reasoning. We present a unifying analysis through the lens of pragmatics: these safety failures can be understood and addressed as LLMs exhibiting excessive accommodation and insufficient epistemic vigilance. We show that the pragmatic factors affecting accommodation and epistemic vigilance in humans (at-issueness, linguistic encoding, and source reliability) influence LLM behaviors in similar ways. We demonstrate how these factors explain performance differences across three safety benchmarks that test models’ ability to challenge harmful beliefs, spanning misinformation (Cancer-Myth, SAGE-Eval) and sycophancy (ELEPHANT). This pragmatic lens further motivates prompting interventions, such as adding the phrase “wait a minute”, that drastically improve performance on these difficult benchmarks by shifting pragmatic cues. Our results have practical implications for benchmark design and underscore the importance of pragmatics for understanding model behavior and improving performance.

</details>

### 30. PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM Sycophancy

📄 [arXiv](https://arxiv.org/abs/2608.16650) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-08

**关键词**：`defense`、`sycophancy control`、`activation scaling`、`monotonic steering`、`model deception`

👤 **作者**：Zheng Chen、Zhaoxin Feng、Yip Tin Po、Jianfei Ma、Emmanuele Chersoni、Bo Li

- 🎯 **研究动机**：谄媚控制需双向且单调（既可减也可增、强度对应效果），现有方法无法跨模型数据集保证
- 🔬 **研究方法**：PAS 把残差流激活分解为 PCA 识别的谄媚-诚实子空间与正交残差，对两者施加不同缩放指数实现单调双向控制
- 📌 **结论**：三个 LLM、三个数据集上单调性 Spearman ρ=+0.92，每方向平均移 15.4%（基线 8.7%）；分解、不对称指数与层选择各不可缺

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) exhibit sycophancy, a tendency to agree with user beliefs regardless of factual accuracy. This can reinforce misconceptions, but eliminating it entirely risks over-correction against valid opinions. Effective control must therefore both reduce and increase sycophancy with predictable and gradual effect. Yet, existing methods fail to ensure a bidirectional and monotonic relationship between steering strength and behavioral outcome across models and datasets. We introduce PCA-guided Activation Scaling (PAS), an activation steering framework that decomposes residual stream activations into a PCA-identified sycophancy-honesty subspace and an orthogonal residual, then applies distinct scaling exponents to achieve monotonic, bidirectional control. Across three LLMs and three datasets, PAS achieves strong monotonicity (Spearman $ρ$ = +0.92) and an average shift of 15.4% per direction, compared with 8.7% for the baselines. Ablation studies confirm that the decomposition, asymmetric exponents, and layer selection are each essential for maintaining monotonic control. The data and code are available at https://github.com/Bellafc/PCS.

</details>