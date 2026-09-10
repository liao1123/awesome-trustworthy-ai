# 安全不确定性校准与 Selective Prediction

[返回上级目录](README.md)

## 研究方向

研究模型 confidence 是否匹配具体安全风险，以及系统何时应回答、abstain、retrieve、阻断行动或升级人工。只收录与 adversarial attack、安全对齐、模型遗忘、tail risk 或医疗、法律、金融和物理控制等高风险后果直接绑定的 calibration、conformal prediction、OOD detection 与 uncertainty-aware control；一般 UQ、普通 OOD 和只提升平均可靠性的工作不纳入。

## 研究脉络

- **攻击与安全边界：** Calibration 用于识别 adversarial input、误导性检索、guardrail 漏检和删除后的残留知识。
- **高风险拒答：** 医疗、法律和金融场景通过 abstention 与 risk-coverage curve 把不确定性转化为可执行边界。
- **策略风险控制：** Conformal control、CVaR 和 safe RL 将 uncertainty 接入尾部风险与后续行动约束。
- **当前边界：** 普通 accuracy calibration、一般 OOD 检测和没有安全后果的 selective prediction 不进入本页。

## Risk-Aware Routing、Retrieval 与 Tool Use

### 1. DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing

📄 [arXiv](https://arxiv.org/abs/2608.14950)　📅 2026-08

**关键词**：`detection`、`uncertainty calibration`、`selective prediction`、`deployment shift`

👤 **作者**：Cheng Wu、Vishal Anand、Jaya Krishna Mandivarapu、Xiya Liu、Rui Zhuang

- 🎯 **研究动机**：LLM judge 会被无关的上下文参考例误校准，制造虚假自信让低质或有害输出通过评测
- 🔬 **研究方法**：DA-RAC 为每个判定场景检索语义与结构相似的标注锚、按距离加权，并把邻域难度暴露为校准与分诊信号
- 📌 **结论**：多轮 judge 基准上校准改善、误通过风险低于零样本、CoT 与静态锚基线；judge 分数随锚距离系统性变化，静态参考会诱导误导决策边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative AI systems are increasingly producing real-world artifacts, however their efficacy and validity are often evaluated via context-free LLM-scoring. These judges can be miscalibrated by irrelevant in-context reference examples, creating false confidence and allowing low-quality or harmful outputs to pass evaluation. We study this failure mode as context-induced miscalibration and introduce DA-RAC, a distance-aware reference-anchored calibration method for LLM judges. DA-RAC retrieves semantically and structurally similar labeled anchors for each judgement scenario, weights them by distance, and exposes neighborhood difficulty as a calibration and triage signal. On multi-run LLM-judge evaluation benchmarks, it improves calibration and reduces false-pass risk relative to zero-shot, chain-of-thought evaluation, and static-anchor baselines. Mechanistic analysis shows that judge scores vary systematically with anchor distance, while static references can induce misleading decision boundaries. Thus LLM-judgement requires not only better models, but also calibrated, auditable reference selection, especially when automated evaluation is used to support high-impact AI generated artifacts. Judgments should be grounded in relevant, inspectable, and contestable interpretive artifacts.

</details>

### 2. LODESTAR: Robust Entropy-Based Answer Selection in Retrieval-Augmented Generation for Question Answering -- Directing Frozen-LLM Entropy with a Reinforcement-Learned Prompt Polarizer under Misleading Passages

📄 [arXiv](https://arxiv.org/abs/2608.11922)　📅 2026-08

**关键词**：`analysis`、`uncertainty calibration`、`selective prediction`、`deployment shift`

👤 **作者**：Hung-Chun Hsu、Po-Jen Ko、Che-Cheng Wu、Li-Yang Chang、Chuan-Ju Wang

- 🎯 **研究动机**：熵选答案规则在误导段落下失效：误导使 respondent 自信犯错，不确定性信号最可信处熵反而最低
- 🔬 **研究方法**：LODESTAR 用 GRPO 离线训练一次 polarizer（插入 respondent prompt 的固定短文本），引导熵使熵选对误导段落鲁棒，推理时不读标签
- 📌 **结论**：5088 题上取得推理就绪选择器中最高平均 F1 0.5339，三种子均值全胜 70 个 F1 单元对 14 种已发表配置且配对显著，域内外均成立

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Predictive-distribution entropy is a strong answer-selection rule in retrieval-augmented generation (RAG) for question answering: across five QA benchmarks, selecting the answer a frozen respondent LLM produces with the lowest answer-token entropy lifts mean $F_1$ from 0.4769 to 0.5148 over the retriever's top-ranked passage, without gold answers. Yet this rule, which prior entropy-based selectors adopt, fails: a misleading passage makes the respondent confidently wrong, driving entropy down where the uncertainty signal looks most trustworthy. The failure comes from the passage the respondent reads, and the context it is read in is an input we can intervene on. We introduce LODESTAR: to our knowledge the first method to score a text intervention by the uncertainty it induces in a third-party frozen respondent, compared within one question. LODESTAR uses reinforcement learning (GRPO) to train, once and offline, a polarizer -- a short fixed natural-language string inserted into the respondent's prompt and never into its weights, directing entropy so that entropy-based answer selection stays robust to misleading passages; training labels are built from gold answers and two LLM judges, and inference reads neither. With every competing selector under the same frozen respondent and candidate pools on 5,008 questions, LODESTAR attains the highest mean $F_1$ of any inference-ready selector (0.5339), the highest macro exact match (0.4136), and the highest GPT-4o judge score of the frozen-respondent configurations judged (0.6435); its three-seed mean wins all 70 $F_1$ cells against fourteen published configurations and is paired-significant on $F_1$ against every one. The gain holds in-domain on NQ-Open and out-of-domain over SQuAD, TriviaQA, EntityQuestions and WebQuestions. Ablating the polarizer shows it is what makes the respondent read a misleading passage less often (26.0% vs 30.3%).

</details>

### 3. Knowing When Not to Answer: Lightweight KB-Aligned OOD Detection for Safe RAG

🎓 [Official](https://aclanthology.org/2026.acl-long.740/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`uncertainty calibration`、`selective prediction`、`deployment shift`、`RAG security`、`safety alignment`

👤 **作者**：Ilias Triantafyllopoulos、Renyi Qu、Salvatore Giorgi、Brenda Curtis、Lyle Ungar、João Sedoc

- 🎯 **研究动机**：OOD 查询使 RAG 检索召回弱相关上下文，产生流畅但无依据的回答
- 🔬 **研究方法**：对 KB 嵌入做 PCA，在按解释方差保留或可分性 t-test 排序选取的紧致子空间打分作常开门控；跨 16 个域评测并用 LLM 生成攻击与 4chan 真实攻击压测
- 📌 **结论**：低维检测器 OOD 性能有竞争力，且比 prompted LLM judge 更快、更省、更可解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are increasingly deployed in high-stakes domains, where safety depends not only on how a system answers, but also on whether a query should be answered given a knowledge base (KB). Out-of-domain (OOD) queries can cause dense retrieval to surface weakly related context and lead the generator to produce fluent but unjustified responses. We study lightweight, KB-aligned OOD detection as an always-on gate for RAG systems. Our approach applies PCA to KB embeddings and scores queries in a compact subspace selected either by explained-variance retention (EVR) or by a separability-driven -test ranking. We evaluate geometric semantic-search rules and lightweight classifiers across 16 domains, including high-stakes COVID-19 and Substance Use KBs, and stress-test robustness using both LLM-generated attacks and an in-the-wild 4chan attack. We find that low-dimensional detectors achieve competitive OOD performance while being faster, cheaper, and more interpretable than prompted LLM-based judges. Finally, human and LLM-based evaluations show that OOD queries primarily degrade the relevance of RAG outputs, highlighting the need for efficient external OOD detection to maintain safe, in-scope behavior.

</details>

### 4. Calibrating Uncertainty for Zero-Shot Adversarial CLIP

📄 [arXiv](https://arxiv.org/abs/2512.12997) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62864)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial robustness`、`uncertainty calibration`、`robustness certification`

👤 **作者**：Wenjing Lu、Zerui Tao、Yuning Qiu、Dongping Zhang、Yang Yang、Qibin Zhao

- 🎯 **研究动机**：CLIP 对抗微调只对齐干净与对抗样本 logits，忽视校准——扰动会抑制不确定性导致严重过自信
- 🔬 **研究方法**：把 CLIP 输出重参数化为 Dirichlet 分布浓度参数，统一表征语义结构与置信幅度，在扰动下做整体分布对齐而非单 logit 锚定
- 📌 **结论**：多个零样本基准上显著改善不确定度校准，对抗鲁棒性有竞争力且保持干净精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

CLIP delivers strong zero-shot classification but remains highly vulnerable to adversarial attacks. Prior adversarial fine-tuning work primarily matches predicted logits between clean and adversarial examples, which overlooks uncertainty calibration and may degrade the zero-shot generalization. A common expectation in reliable uncertainty estimation is that predictive uncertainty should increase as inputs become more difficult or shift away from the training distribution. However, we frequently observe the opposite in the adversarial setting: perturbations not only degrade accuracy but also suppress uncertainty, leading to severe miscalibration and over-confidence. This reveals a critical reliability gap beyond robustness. To bridge this gap, we propose an adversarial fine-tuning objective for CLIP considering both accuracy and uncertainty. By reparameterizing CLIP outputs as the concentration parameters of a Dirichlet distribution, we propose a unified representation that captures relative semantic structure and confidence magnitude. This enables holistic distribution alignment under perturbations, moving beyond single-logit anchoring and restoring calibrated uncertainty. Experiments across multiple zero-shot benchmarks demonstrate that our method significantly improves uncertainty calibration and achieves competitive adversarial robustness while preserving clean accuracy.

</details>

### 5. Achieving Multi-Hop Calculation and Safe Abstention in Financial Numerical Reasoning by Metric Graph Constrained LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1273/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`financial AI`、`uncertainty calibration`、`high-risk deployment`

👤 **作者**：Aoyuan Jiang (蒋翱远)、Liang Hong、Haoxuan Liu、Rui Wang

- 🎯 **研究动机**：金融数值推理中 LLM 面对模糊证据或复杂递归依赖时常强行生成、编造数值弥合信息缺口
- 🔬 **研究方法**：提出金融推理框架 GBFR：用金融指标图谱施加语义与结构约束，并行图约束算法探索异构路径并跨路径验证，仅聚合语义一致结果，区分真缺失与检索失败以安全弃答；构造不可回答反事实样本评估
- 📌 **结论**：在标准基准上显著超过 SOTA 基线，实现多跳计算与有依据的弃权

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Financial numerical reasoning demands rigorous adherence to domain-specific logic and precise evidence foundation. However, large language models (LLMs) are prone to forced generation when confronting ambiguous evidence or complex recursive dependencies, often hallucinating values to bridge information gaps. To address this, we propose graph-bounded financial reasoning (GBFR), a neuro-symbolic framework that imposes semantic and structural constraints via a financial metric knowledge graph (FMKG). Unlike sequential generation paradigms, our approach employs a parallel graph-constrained reasoning algorithm that orchestrates specialized operators to simultaneously explore heterogeneous derivation paths of complex financial metrics. Through cross-path verification, the framework aggregates only semantically consistent results, ensuring reasoning is bounded by available context. Crucially, this approach enables safe abstention by distinguishing genuine data absence from retrieval failure, thereby preventing ungrounded fabrication. To evaluate this capability, we further construct counterfactual samples by perturbing entities, times, and metrics to synthesize unanswerable scenarios. Empirical evaluations on standard benchmarks demonstrate that GBFR significantly outperforms state-of-the-art baselines.

</details>

### 6. Conformal Policy Control

📄 [arXiv](https://arxiv.org/abs/2603.02196) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61296)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`conformal risk control`、`safe exploration`、`finite-sample guarantee`、`safe reinforcement learning`、`risk control`

👤 **作者**：Drew Prinster、…、Samuel Stanton

- 🎯 **研究动机**：高风险环境中智能体违反约束即被下线，模仿旧行为安全但过度保守抑制探索，行为变化多少算过头缺乏原则答案
- 🔬 **研究方法**：用任意安全参考策略作未测试策略的概率调节器：在安全策略数据上做 conformal 校准决定新策略激进程度，可证满足风险容忍度，且对非单调有界约束给出有限样本保证
- 📌 **结论**：从自然语言问答到生物分子工程，安全探索从部署首刻即可行且能提升性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm and must be taken offline, curtailing any future interaction. Imitating old behavior is safe, but excessive conservatism discourages exploration. How much behavior change is too much? We show how to use any safe reference policy as a probabilistic regulator for any optimized but untested policy. Conformal calibration on data from the safe policy determines how aggressively the new policy can act, while provably enforcing the user's declared risk tolerance. Unlike conservative optimization methods, we do not assume the user has identified the correct model class nor tuned any hyperparameters. Unlike previous conformal methods, our theory provides finite-sample guarantees even for non-monotonic bounded constraint functions. Our experiments on applications ranging from natural language question answering to biomolecular engineering show that safe exploration is not only possible from the first moment of deployment, but can also improve performance.

</details>

### 7. Adversarially Robust Control of Conditional Value-at-Risk via Rockafellar-Uryasev Conformal Inference

📄 [arXiv](https://arxiv.org/abs/2606.00320) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63594)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`conformal risk control`、`adversarial robustness`、`uncertainty calibration`、`safety evaluation`、`tail risk`

👤 **作者**：Catherine Chen、Jingyan Shen、Zhun Deng、Lihua Lei

- 🎯 **研究动机**：经典尾部风险控制依赖平稳性或期望线性，在非平稳与对抗环境（策略性漂移移位）下无保证
- 🔬 **研究方法**：融合 conformal tail risk control、在线学习与 Rockafellar-Uryasev 的 CVaR 变分表示，构建在线、分布无关的 CVaR 控制程序，带对抗遗憾保证且不假设数据生成过程
- 📌 **结论**：证明实现的经验 CVaR 渐近控制在目标水平、控制渐近紧（O(1/sqrtT) 保守差），在组合风险管理与 LLM 毒性缓解上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present an online, distribution-free framework for controlling the Conditional Value-at-Risk ($\operatorname{CVaR}$), extending conformal tail risk control to non-stationary and adversarial environments. Unlike classical risk control methods, which rely on stationarity or linearity of expectation, our approach provides provable safety guarantees for a nonlinear tail risk functional under arbitrary data-generating processes that may drift or shift strategically over time. By leveraging deep connections between conformal tail risk control, online learning, and the variational representation of $\operatorname{CVaR}$ introduced by Rockafellar and Uryasev, we develop a novel procedure for online $\operatorname{CVaR}$ control with adversarial regret guarantees. The proposed method operates without assumptions on the underlying data-generating process, making it broadly applicable in modern high-stakes deployment settings. We prove that the realized empirical $\operatorname{CVaR}$ is asymptotically controlled at the target level, and that the resulting control is asymptotically tight up to a finite-sample ${O}(1/\sqrt{T})$ conservatism gap. We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.

</details>

### 8. Quantifying Risk Under Evolving Uncertainty: Belief-Dependent Robustness for Safe Sequential Decision Making

📄 [arXiv](https://arxiv.org/abs/2608.17574) · 🌐 [Project](https://sites.google.com/view/robustifai-workshop/program)　📅 2026-08

**关键词**：`analysis`、`adversarial robustness`、`uncertainty calibration`、`selective prediction`

👤 **作者**：Deep Kumar Ganguly、Jan Kretinsky

- 🎯 **研究动机**：agent 在仍学习环境时该保持多谨慎缺乏原则化答案
- 🔬 **研究方法**：RATTL 把谨慎绑定认知不确定性：对未知动态持贝叶斯后验，规划对抗 Wasserstein 模糊集、半径为后验的单调函数，随证据收缩在最坏鲁棒与风险中性间连续插值
- 📌 **结论**：证明 Safety Sandwich（RATTL 值介于无信息鲁棒值与全知最优间、后验集中时差距消失）；二值危险实例下归结为后验熵设定水平的 CVaR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How cautious should an agent be while it is still learning its environment? We propose RATTL (Risk-Adversarial Total-Reward Learning), which ties caution to epistemic uncertainty: the agent holds a Bayesian posterior over unknown dynamics and plans against a Wasserstein ambiguity set whose radius is a monotone function of that posterior. The radius contracts with evidence, so behaviour interpolates continuously between worst-case robustness and risk-neutral total-reward maximization. The design follows the duality underlying the Entropic Value-at-Risk, which converts the choice of a risk level into the choice of an ambiguity radius. We show the resulting planning problem is well posed under transience and compactness conditions, and prove a Safety Sandwich: the RATTL value lies between the uninformed robust value and the full- knowledge optimum, with a gap that vanishes as the posterior concentrates. In a canonical binary-hazard instance, the induced criterion reduces to Conditional Value-at-Risk at a level set by the posterior entropy. A worked example shows the agent deferring the efficient action until a sharp identification threshold. RATTL targets runtime safety for agents, including LLM-based systems, acting under uncertainty.

</details>

### 9. CUBICS: Situation-aware performance estimation for safety-relevant ML components

📄 [arXiv](https://arxiv.org/abs/2608.16564)　📅 2026-08

**关键词**：`analysis`、`uncertainty calibration`、`selective prediction`、`deployment shift`

👤 **作者**：Benjamin Herd、Jessica Kelly、Mario Trapp

- 🎯 **研究动机**：安全工程的贝叶斯场数据法多用单一全局失败概率的伯努利模型，不适配性能强依赖情境的 ML 组件
- 🔬 **研究方法**：CUBICS 把运行设计域划分为情境，用 Subjective Logic 为每个安全相关组件表示与贝叶斯更新情境特定假设与概率保证，结合情境发生频率导出组件级风险估计
- 📌 **结论**：无需单体系统级统计模型即可提供模块化、基于场数据的安全保证构件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) is a key technology driving innovation today, but ensuring ML safety remains a major challenge for safety-related applications. A promising idea is to build proven-in-use arguments from field data, e.g. by running ML components (MLCs) in shadow mode or within safety envelopes so that their outputs can be monitored as 'safe probes' without affecting safety. These probes can then be used to build a statistical argument about field performance in a Bayesian way. However, many Bayesian field-data approaches in safety engineering model failures as a simple Bernoulli (or binomial) process with a single global failure probability and i.i.d. trials, which is rarely adequate for MLCs whose performance depends strongly on context. Statistical evidence is also about coverage of relevant situations, including edge cases, and building a single integrated statistical model for the entire system is usually not feasible. To address these challenges, this paper introduces CUBICS, a context-modular framework for per-component, situation-aware performance estimation of safety-relevant ML components. CUBICS partitions the operational design domain into situations and, for each safety-relevant component, defines a set of situation-specific assumptions and probabilistic guarantees that are represented and updated in a Bayesian manner using Subjective Logic (SL). By combining these guarantees with beliefs about how often each situation occurs, CUBICS derives an overall risk estimate for each component without requiring a monolithic system-level statistical model, and thus provides a building block for modular, field-data based safety assurance.

</details>

### 10. Visualizing Uncertainty-to-Action Composition for Human Oversight

📄 [arXiv](https://arxiv.org/abs/2608.16428)　📅 2026-08

**关键词**：`analysis`、`uncertainty calibration`、`selective prediction`、`deployment shift`

👤 **作者**：Chisom Anyabolu、Akshat Dubey、Georges Hattab

- 🎯 **研究动机**：不确定性可视化只编码模型输出不确定性、让用户自行判断行动，决策过程本身的不确定性组合欠探索
- 🔬 **研究方法**：不确定性-行动绑定框架在优先级策略与语境安全修正子下把多不确定性条件组合成单一监督响应；ActionCue 过程透明可视化显式呈现该组合
- 📌 **结论**：在医疗、信贷与灾害预报案例上与仅置信度、数据级不确定性显示三方对比，使不确定性到监督响应的解析可检视而非隐含

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial intelligence systems often disclose uncertainty, yet they rarely make clear what response that uncertainty should trigger. Most uncertainty visualizations encode uncertainty in model outputs, leaving users to discern the most appropriate course of action. A second region of the design space--uncertainty in the decision process itself, including how multiple uncertainty conditions compose into an oversight response-- remains comparatively underexplored. We address this gap with two coupled contributions. First, we introduce an uncertainty-to-action binding framework that composes multiple uncertainty conditions into a single oversight response under a precedence policy with a contextual safety modifier. That response concerns whether and how an AI-supported decision may proceed, not the substantive domain decision itself. Second, we present ActionCue, a process-transparency visualization that renders that composition explicit. We demonstrate the approach through a three-way comparison with confidence-only and data-level uncertainty displays, using worked cases from healthcare, credit assessment, and disaster forecasting. Together, the framework specifies how uncertainty conditions are resolved into an oversight response, and the visualization makes that resolution inspectable rather than implicit.

</details>

### 11. Robustness Meets Uncertainty: Evidential Adversarial Training for Robust Selective Classification

📄 [arXiv](https://arxiv.org/abs/2607.03075) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5235)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`adversarial training`、`uncertainty`、`selective classification`

👤 **作者**：Nicolas Sournac、Ahmed Baha Ben Jmaa、Bertrand Braeckeveldt

- 🎯 **研究动机**：对抗训练对预测不确定性可靠性的影响缺乏与选择性分类结合的系统分析
- 🔬 **研究方法**：构建鲁棒性-不确定性权衡统一基准（标准化架构、增广、威胁模型与指标），发现多种 SOTA 对抗训练提升鲁棒准确率却恶化不确定性排序；提出 EV-AT 用 Dirichlet 建模不确定性并结合证据损失与鲁棒证据对齐损失
- 📌 **结论**：EV-AT 把鲁棒性-不确定性权衡的 Pareto 前沿推过先前 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical applications require classifiers that are both robust and reliable. Adversarial training is a widely adopted defense for improving robustness in deep neural networks; however, its effect on the reliability of predictive uncertainty remains underexplored. We investigate this gap through the lens of selective classification, which has rarely been systematically analyzed alongside adversarial robustness. We introduce a unified benchmark for the robustness-uncertainty trade-off. It standardizes architectures, augmentations, threat models, and evaluation metrics across clean, adversarial, and common-corruption settings. Across a wide range of state-of-the-art adversarial training methods, we uncover a recurring failure mode: several approaches improve robust accuracy while degrading uncertainty ranking, leading to poorer selective behavior. To address this, we propose Evidential Adversarial Training (EV-AT), which models uncertainty through a Dirichlet distribution and combines (i) an evidence-based loss promoting clean accuracy and reliable uncertainty with (ii) a robust evidence-alignment loss matching clean and adversarial predictions in log Dirichlet-parameter space. Extensive experiments show that EV-AT shifts the Pareto frontier of robustness-uncertainty trade-offs beyond prior state-of-the-art adversarial training methods. Our source code is publicly available at https://github.com/NicolasSournac/Robustness_Meets_Uncertainty.EV-AT.

</details>

### 12. Tackling Fake Forgetting through Uncertainty Quantification

📄 [arXiv](https://arxiv.org/abs/2501.19403) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61287)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`uncertainty calibration`、`selective prediction`、`deployment shift`、`machine unlearning`、`conformal risk control`

👤 **作者**：Yingdan Shi、Sijia Liu、Kaize Ding、Ren Wang

- 🎯 **研究动机**：遗忘精度指标会误判遗忘质量：被其判定已遗忘的样本真值标签仍留在共形预测集内，存在 fake forgetting
- 🔬 **研究方法**：提出共形预测启发的 CR 指标更可靠评估遗忘质量，并提出把共形预测融入 Carlini & Wagner 攻击损失的遗忘框架 CPU，使真值标签被有效移出预测集
- 📌 **结论**：图像分类任务上验证了新指标的有效性与框架的更优遗忘质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning seeks to remove the influence of specified data from a trained model. While the unlearning accuracy provides a widely used metric for assessing unlearning performance, it falls short in assessing the reliability of forgetting. In this paper, we find that the forgetting data points misclassified by unlearning accuracy still have their ground truth labels included in the conformal prediction set from the uncertainty quantification perspective, leading to a phenomenon we term fake forgetting. To address this issue, we propose a novel metric CR, inspired by conformal prediction, that offers a more reliable assessment of forgetting quality. Building on these insights, we further propose an unlearning framework CPU that incorporates conformal prediction into the Carlini & Wagner adversarial attack loss, enabling the ground truth label to be effectively removed from the conformal prediction set. Through extensive experiments on image classification tasks, we demonstrate both the effectiveness of our proposed metric and the superior forgetting quality achieved by our framework. Code is available at https://github.com/TIML-Group/Conformal-Prediction-Unlearning.

</details>

### 13. LLMs (Almost) Never Abstain Under Medical Uncertainty

🎓 [Official](https://aclanthology.org/2026.acl-long.1365/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`medical AI`、`uncertainty calibration`、`high-risk deployment`、`failure mitigation`

👤 **作者**：Alessio Cocchieri、Luca Ragazzi、Giuseppe Tagliavini、Gianluca Moro

- 🎯 **研究动机**：医学 MCQA 隐含假设 LLM 应总作答，而临床不确定时弃权常是最安全行动
- 🔬 **研究方法**：MedQAbstain 移除金答案并引入显式 I abstain 选项，作为有临床后果的安全关键决策，支持弃权 regime、干扰项复杂度与模态分析并引出自报置信
- 📌 **结论**：SOTA LLM 系统性过度承诺，即使问题本身被隐藏也几乎不弃答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Medical multiple-choice question answering (MCQA) benchmarks implicitly assume that large language models (LLMs) should always commit to an answer. However, in clinical practice, uncertainty is pervasive and abstaining is often the safest action. We introduce MedQAbstain, a benchmark explicitly designed to evaluate medical abstention under uncertainty. MedQAbstain repurposes standard medical MCQA datasets by removing the gold answer and introducing an explicit “I abstain” option, framed as a safety-critical decision with clinical consequences. The benchmark supports systematic analysis across abstention regimes, distractor complexity, and input modalities, and elicits self-reported model confidence to study calibration. Across all settings, we find that state-of-the-art LLMs systematically overcommit, rarely abstaining even when the question itself is hidden. These results reveal a fundamental mismatch between LLM behavior and clinical norms, highlighting abstention as a critical but overlooked dimension of medical decision-making evaluation.

</details>

### 14. CURA: Clinical Uncertainty Risk Alignment for Language Model–Based Risk Prediction

🎓 [Official](https://aclanthology.org/2026.acl-long.1567/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`uncertainty calibration`、`selective prediction`、`deployment shift`、`medical AI`、`high-risk deployment`

👤 **作者**：Sizhe Wang、Ziqi Xu、Claire Najjuuko、Charles Alba、Chenyang Lu

- 🎯 **研究动机**：临床语言模型的风险预测不确定度校准差、临床不可靠
- 🔬 **研究方法**：CURA 双层不确定度目标微调多头分类器：个体级校准项对齐不确定度与患者出错可能，队列感知正则把风险估计拉向嵌入空间邻域事件率并加权模糊队列
- 📌 **结论**：MIMIC-IV 上跨多个临床 LLM 一致改善校准且不明显损害判别力，减少过自信的错误安抚

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clinical language models (LMs) are increasingly applied to support clinical risk prediction from free-text notes, yet their uncertainty estimates often remain poorly calibrated and clinically unreliable. In this work, we propose Clinical Uncertainty Risk Alignment (CURA), a framework that aligns clinical LM-based risk estimates and uncertainty with both individual error likelihoods and cohort-level ambiguities. CURA first fine-tunes domain-specific clinical LMs to obtain task-adapted patient embeddings, and then performs uncertainty fine-tuning of a multi-head classifier using a bi-level uncertainty objective. Specifically, an individual-level calibration term aligns predictive uncertainty with each patient’s likelihood of error, while a cohort-aware regularizer pulls risk estimates toward event rates in their local neighborhoods in the embedding space and places extra weight on ambiguous cohorts near the decision boundary. We further show that this cohort-aware term can be interpreted as a cross-entropy loss with neighborhood-informed soft labels, providing a label-smoothing view of our method. Extensive experiments on MIMIC-IV clinical risk prediction tasks across various clinical LMs show that CURA consistently improves calibration metrics without substantially compromising discrimination. Further analysis illustrates that CURA reduces overconfident false reassurance and yields more trustworthy uncertainty estimates for downstream clinical decision support.

</details>

### 15. Knowing When Not to Predict: Self Supervised Learning and Abstention for Safer DR Screening

📄 [arXiv](https://arxiv.org/abs/2605.19133) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H96.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-health)　📅 2026

**关键词**：`analysis`、`medical abstention`、`calibration`、`selective prediction`

👤 **作者**：Muskaan Chopra、Lorenz Sparrenberg、Jan H. Terheyden、Rafet Sifa

- 🎯 **研究动机**：医学图像模型只看精度不足，安全筛查还需知道何时弃权转临床复核
- 🔬 **研究方法**：固定微调协议下评测多个 SSL checkpoint 的校准置信、覆盖率、选择准确率与选择性 macro-F1
- 📌 **结论**：SSL 预训练比从头训练改善选择性预测；但精度饱和后选择性表现在 checkpoint 间仍大幅波动，更长预训练不必然更可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) is now a standard way to pretrain medical image models, but performance is still mostly judged by downstream accuracy. For safety-critical screening tasks such as diabetic retinopathy grading, this is not enough: a model must also know when its predictions are unreliable and defer uncertain cases for clinical review. In this work, we examine how the length of SSL pretraining influences calibrated confidence and confidence-based abstention. We evaluate multiple SSL checkpoints under a fixed fine-tuning protocol and assess calibrated confidence, coverage, selective accuracy, and selective macro-F1. Across datasets and data regimes, SSL pretraining improves selective prediction compared to training from scratch. Unlike prior SSL studies that primarily evaluate downstream accuracy or AUROC, we analyze how SSL pretraining duration influences confidence behavior under calibrated confidence-based abstention. However, once accuracy saturates, selective performance can still change markedly across checkpoints, and longer pretraining does not consistently improve reliability. These results underscore the importance of abstention-aware evaluation and suggest that pretraining length should be treated as an important reliability-related design choice rather than only a computational detail. Code is available at https://github.com/ muskaan712/ijcai-knowing-when-not-to-predict.

</details>

### 16. CGRiC: Compositional Risk Certification for Structured LLM Outputs

🎓 [Official](https://icml.cc/virtual/2026/poster/64542)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`certified robustness`

👤 **作者**：Ibne Farabi Shihab、SANJEDA AKTER、Anuj Sharma

- 🎯 **研究动机**：结构化输出的正确性是组合式的——单个错误主张即可作废整体；现有认证把输出当原子单元，只能全盘接受或浪费性拒绝
- 🔬 **研究方法**：CGRiC 把响应分解为可验证主张的依赖图，经 information-lift 统计赋予校准的逐主张风险界，组合后对未检出错误主张概率给出显式保证，超阈值时触发局部修复
- 📌 **结论**：达到目标风险水平同时比原子基线减少 31% 弃权，覆盖 QA、摘要与推理任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly generate structured outputs, including citation-grounded summaries, multi-step reasoning chains, and tool-augmented responses, where correctness is inherently compositional: a single flawed claim can invalidate an otherwise accurate response. Existing certification methods treat outputs as atomic units, forcing a binary choice between unsafe acceptance and wasteful rejection. We introduce \textbf{Claim Graph Risk Control (CGRiC)}, a framework that decomposes responses into dependency graphs of verifiable claims and assigns calibrated per-claim risk bounds via information-lift statistics. By composing these bounds, CGRiC provides explicit guarantees on the probability that any incorrect claim passes verification undetected. When this composed risk exceeds a target threshold, the system triggers localized repairs rather than full abstention, preserving correct content while fixing problematic claims. Our approach explicitly models extraction noise and verifier imperfection, and exploits conditional independence structure for tighter certificates when validated. Empirically, CGRiC achieves target risk levels while reducing abstention by 31\% compared to atomic baselines across QA, summarization, and reasoning tasks.

</details>