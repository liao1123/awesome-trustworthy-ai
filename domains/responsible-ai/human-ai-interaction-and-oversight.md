# Human-AI Interaction 与 Oversight

[返回上级目录](README.md)

## 研究方向

研究人如何在虚假内容、高风险建议、自主系统或长期 AI companion 关系中理解、依赖、纠正和监督 AI，重点测量误信、漏检、危险依赖、关系性伤害、override failure 与最终伤害路径。一般用户体验、参与感、接受度、长期交互倡议或协作效率不收录。

## 研究脉络

- **信任与依赖：** 研究从主观 trust 扩展到 automation reliance、override 和错误传播的行为测量。
- **协作与监督：** Human-in-the-loop protocol、escalation 和 scalable oversight 分配判断与执行责任。
- **风险沟通：** Uncertainty visualization、warning 和 explanation 影响用户能否正确调整依赖。
- **关系性风险：** AI companion 和 coaching system 中的多轮情境、心理危机、边界侵犯与社会情感伤害需要专门检测，并审计专家与自动 judge 的系统分歧。
- **当前边界：** 只有把交互现象落到具体安全后果和可审计行为指标的研究才进入本页。

## Trust、Reliance 与 Decision Outcome

### 1. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation

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

### 2. Attention Capture Is Not Detection: A Two-Stage Account of How Humans Miss Localized AI Image Edits

📄 [arXiv](https://arxiv.org/abs/2608.13865)　📅 2026-08

**关键词**：`detection`、`human oversight`、`automation reliance`、`risk communication`

👤 **作者**：Chiao-Chieh Deng

- 🎯 **研究动机**：平台把 AI 图像编辑可检测性当单一属性，编辑被注意到与被正确判假是否为可分离阶段未知
- 🔬 **研究方法**：59 人眼动拉丁方实验交叉编辑面积与语义合理性，混合效应分析，并用生成式扫描路径 Transformer 计算化注意捕获阶段
- 📌 **结论**：编辑面积驱动注意捕获、语义合理性驱动判断准确率与视而不见错误率（均 p<0.001），两阶段可分离；扫描路径模型预测注意 r=0.77-0.82

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI-generated image edits proliferate, the platforms meant to curb the resulting disinformation treat detectability as a single, undifferentiated property: an edit either gets a warning or it does not. We show this is the wrong model. Across a controlled eye-tracking study ($N=59$, Latin-square design, four conditions crossing edit area and semantic plausibility), a mixed-effects analysis reveals that whether an edit is noticed and whether it is correctly judged as fake are dissociable stages, governed by different factors: edit area drives attention capture ($p<0.001$) while semantic plausibility drives judgment accuracy and look-but-fail-to-see (LBFS) error rates ($p<0.001$). This dissociation survives correction for multiple comparisons; a secondary interaction between the two factors does not. This two-stage account extends a long-standing distinction in visual attention research (between pre-attentive capture and effortful recognition) into the new domain of AI-edit detectability. We then test whether a generative eye-movement model can computationally operationalize the attention-capture stage: a Transformer trained to generate scanpaths tracks per-image attention with strong discriminative power (Pearson $r=0.77$--$0.82$ across held-out stimuli) and, on the harder task of predicting LBFS incidence, modestly outperforms a two-parameter linear baseline even without access to the plausibility label ($r=0.52$ vs. $r=0.48$). We report this comparison, our ablations, and our method's limitations (a single fixed train/validation split, not leave-one-subject-out) without inflation, consistent with responsibly communicating what a machine learning system can and cannot do to help curb AI-driven disinformation.

</details>

### 3. Rewarding Engagement and Personalization in Popularity-Based Rankings Amplifies Extremism and Polarization

📄 [arXiv](https://arxiv.org/abs/2510.24354) · 🌐 [Project](https://doi.org/10.1145/3770855.3818037)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`ranking harm`、`extremism`、`polarization`

👤 **作者**：Jacopo D'Ignazi、Emma Fraxanet Morales、Andreas Kaltenbrunner、Gaël Le Mens、Fabrizio Germano、Vicenç Gómez

- 🎯 **研究动机**：热度排序奖励engagement与个性化是否放大极化未明
- 🔬 **研究方法**：建模此类排序奖励对内容生态的动力学影响
- 📌 **结论**：该奖励机制系统性放大极端主义与观点极化

### 4. Ask or Answer: A Decision Framework for Multi-Turn Health Misinformation Intervention

📄 [arXiv](https://arxiv.org/abs/2608.21721)　📅 2026-08

**关键词**：`defense`、`health misinformation`、`multi-turn correction`、`probe-or-answer`、`risk communication`、`clarification policy`

👤 **作者**：Xiaoying Song、Anirban Saha Anik、Jinyu Liu、Qitao Tan、Geng Yuan、Lingzi Hong

- 🎯 **研究动机**：多轮健康错误信息干预中，立即纠正忽略用户知识/信念差异，无差别追问又徒增交互负担，何时值得提问缺乏决策框架
- 🔬 **研究方法**：RO-PnR 逐轮在追问与给出最终纠正之间选择，由权衡追问预期增益与交互成本的 turn-level reward 引导，并以健康素养与信念承诺的潜在状态建模用户异质性
- 📌 **结论**：三个健康错误信息数据集与三个基座模型上取得最高成本调整效用，比 always-probe 基线少用 30% 轮次

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Correcting health misinformation in dialogue requires more than producing a factual rebuttal: users differ in what they know, what they believe, and what they need to hear, so an effective intervention often depends on first asking the right clarifying question. Yet existing methods either respond immediately or probe indiscriminately, treating clarification as either unnecessary or always beneficial. We propose Reward-Optimized Probe-and-Respond (RO-PnR), a framework that learns when asking is worth its cost. At each turn, RO-PnR chooses between probing for more information and committing to a final correction, guided by a turn-level reward that weighs the expected gain from probing against its interaction cost. To capture how user heterogeneity affects probing value, we model each simulated user with a latent state along health literacy and belief commitment. Experiments show that RO-PnR achieves the highest cost-adjusted utility across three health-misinformation datasets and three base models, using 30% fewer turns than always-probe baselines.

</details>

### 5. AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations

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

### 6. When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha

📄 [arXiv](https://arxiv.org/abs/2608.20345) · 🌐 [Project](https://doi.org/10.1145/3805689.3806522)　📅 2026-08

**关键词**：`benchmark`、`child-facing safety`、`youth register`、`crisis-risk guardrail`、`youth mental-health safety`、`multi-turn crisis detection`

👤 **作者**：Manisha Mehta、Virendra Mehta

- 🎯 **研究动机**：13.1% 美国青少年用生成式 AI 做心理健康建议，模型对 Gen Alpha 夸张、反讽、语义漂移语言的安全性未验证
- 🔬 **研究方法**：两个基准：64 条经母语者（ICC=0.72）与临床医生（kappa=0.78）验证的 Gen Alpha 表达；75 段配对标准/Gen Alpha 的多轮对话；评 Claude、GPT-4o、Llama-3.1
- 📌 **结论**：词汇理解 76-82% 但临床风险校准仅 64-72%，缺口 10-14 个百分点（人类治疗师仅 3 个点）；三种失败模式叠加即 94% 漏检率，34% 基线漏检对应年漏约 14.7 万次危机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational AI systems have become informal mental health support resources for Generation Alpha (Gen Alpha, born 2010-2024), with 13.1% of U.S. adolescents (5.4 million) using generative AI for mental health advice. While these systems, from therapy apps to general chatbots, rely on large language models trained on extensive psychological literature, their safety for youth communication patterns characterized by hyperbolic language, ironic positivity, rapid semantic drift, and contextual polysemy remains unvalidated. Following multiple adolescent deaths linked to AI chatbot interactions, systematic evaluation is critical. We present two benchmarks: (1) 64 Gen Alpha mental health expressions validated by native speakers (ICC=0.72) and clinicians (kappa=0.78); (2) 75 multi-turn conversations (780 turns) with paired Standard/Gen Alpha versions. Across evaluations of LLM architectures underlying therapy apps and general chatbots - Claude, GPT-4o, Llama-3.1 - models understand 76-82% of vocabulary but correctly calibrate only 64-72% of clinical risk, creating a 10-14 percentage point (pp) vocabulary-comprehension gap (p<.001, d>0.48) absent in human therapists (3pp, p=.22). The gap is architecturally consistent and widens with ambiguity (7pp -> 18pp). We identify six failure patterns: sarcasm masking (29pp), minimization acceptance (43pp), informal style bias (24pp), risk-stratified ambiguity (19pp), semantic drift (19pp), context-dependent violence (7pp). Patterns compound; three or more yield 94% miss rates. Lightweight mitigations fail; only heavy scaffolding achieves human performance (6.4x cost). With 34% baseline miss rate yielding 146,880 estimated annual missed crises, we recommend mandatory human-in-the-loop architectures, quarterly youth-specific validation, transparent performance disclosure, and regulatory frameworks for youth-facing mental health AI.

</details>

### 7. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

📄 [arXiv](https://arxiv.org/abs/2608.24899) · 🤗 [Model](https://huggingface.co/keidolabs/aipsy-judge-1.0)　📅 2026-08

**关键词**：`detection`、`analysis`、`safety judge`、`self-preference`、`tail-failure calibration`、`psychological-safety guard`

👤 **作者**：Michael Keeman、Anastasia Keeman

- 🎯 **研究动机**：前沿模型或简单平均做 judge 对心理安全评分并不安全：分歧集中于安全指标且有自偏好
- 🔬 **研究方法**：三个前沿模型生成兼评判 3000 条消息并对心理学家评分，据此蒸馏专家校正的逐指标本地 judge
- 📌 **结论**：Gemini judge 带 +0.99 自偏好且漏检尾部危害；本地 aipsy-judge 危机检测 kappa 升至 0.82、捕获 92% 危机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The standard recipe for LLM-as-judge -- pick a frontier model, or average several -- is actively unsafe for grading the psychological safety of conversational AI. Using aipsy-bench, an open frozen safety instrument, we run a fully-crossed competence study: three frontier models (gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash) serve as both generators and judges of 3,000 mental-health, companion, and coaching messages against a psychologist's ratings. The disagreement is not noise: it is structured, concentrated on the safety-critical metrics, and one judge (Gemini) is an outlier -- the most lenient, carrying a +0.99 self-preference premium, flagging far fewer tail failures, and scoring a means-in-hand self-harm response "exemplary." Inter-judge agreement on empathy, where sycophancy hides, is the lowest in the battery (alpha 0.24). One axis stands apart: the binary crisis-detection flag is the one safety-critical signal judges agree on (alpha 0.80), erring toward over-flagging, the safe direction for a triage screen. Equal-weight averaging, the canonical fix, blends that leniency and tail-blindness into the safety score. Off-the-shelf open-weight judges are worse for a dispositional, not capability, reason -- and disposition is fine-tunable. We therefore distill a per-metric, psychologist-corrected target into a small, frozen, local model, aipsy-judge-1.0, an Apache-2.0 fine-tune of Gemma-4-26B-A4B. aipsy-judge-1.0 tracks the corrected target better than its base on the composite (ICC 0.64 to 0.75) and crisis detection (kappa 0.65 to 0.82), catches 92% of crises with a false-positive lean, and grades more faithfully than any single frontier judge, while every transcript stays on the machine. These are directional readings against a single-expert-informed target, not validated multi-rater agreement. A safety grader that shares a vendor's post-training shares its blind spots.

</details>

### 8. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25377)　📅 2026-08

**关键词**：`benchmark`、`AI companion moderation`、`multi-turn context`、`relational harm`、`companion safety`、`relational boundary`

👤 **作者**：Renwen Zhang、Han Meng、Jian Chai、Yuntao Lin、Yi-Chieh Lee

- 🎯 **研究动机**：AI 陪伴应用的关系性、上下文性危害缺乏真实世界多轮数据集来定义与评测
- 🔬 **研究方法**：CompanionHarm 含 2111 段 Replika 真实多轮对话，三名标注者按 13 类危害 taxonomy 标注 7016 条 AI 话语
- 📌 **结论**：多轮上下文检测优于孤立话语，但 7 个 LLM 仍难整合语境与校准严重度；上下文依赖危害的标注分歧显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI companions become increasingly embedded in everyday life, there is an urgent need to detect harms that emerge in social and emotional human-AI interactions. Yet research in this area is constrained by the lack of real-world, multi-turn conversational datasets for operationalizing and evaluating harms that are relational and contextual. In this work, we introduce CompanionHarm, a publicly available benchmark dataset comprising 2,111 real-world, multi-turn conversations (14,051 utterances) between users and the AI companion Replika. 7,016 AI utterances were annotated independently by three annotators across 13 harmful behavior categories grounded in a taxonomy of AI companion harms, and the dataset includes both aggregated labels and annotator-level labels to support model evaluation and systematic disagreement analysis. Evaluations of seven large language models (LLMs) show that harm detection using multi-turn conversational context outperforms detection based on isolated utterances, although current LLMs still struggle to consistently integrate contextual cues, calibrate harm severity, and interpret relational boundaries. We also find substantial annotator disagreement for context-dependent harmful behaviors, with disagreement varying according to annotators' political affiliation, conversation length, and the utterance's position. Together, CompanionHarm provides a foundation for detecting socio-emotional harms in multi-turn human-AI conversations and for rigorously examining how such harms are interpreted by both humans and LLMs. Our dataset is available at https://github.com/HanMeng2004/CompanionHarm.

</details>