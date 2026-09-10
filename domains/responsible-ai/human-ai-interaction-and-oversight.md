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

### 2. Rewarding Engagement and Personalization in Popularity-Based Rankings Amplifies Extremism and Polarization

📄 [arXiv](https://arxiv.org/abs/2510.24354) · 🌐 [Project](https://doi.org/10.1145/3770855.3818037)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`ranking harm`、`extremism`、`polarization`

👤 **作者**：Jacopo D'Ignazi、Emma Fraxanet Morales、Andreas Kaltenbrunner、Gaël Le Mens、Fabrizio Germano、Vicenç Gómez

- 🎯 **研究动机**：热度排序奖励engagement与个性化是否放大极化未明
- 🔬 **研究方法**：建模此类排序奖励对内容生态的动力学影响
- 📌 **结论**：该奖励机制系统性放大极端主义与观点极化

### 3. Ask or Answer: A Decision Framework for Multi-Turn Health Misinformation Intervention

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

### 4. AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations

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

### 5. When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha

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

### 6. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

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

### 7. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

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

### 8. Beyond “Made with AI”: Visualizing Provenance Density to Mitigate the Transparency Penalty

📄 [arXiv](https://arxiv.org/abs/2609.03460) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/HC13.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-human-centred-ai)　📅 2026

**关键词**：`analysis`、`AI provenance`、`evidence visualization`、`hallucination trust`

👤 **作者**：Qing Zhang、Yifei Huang、Juyoung Lee、Thad Starner、Jun Rekimoto

- 🎯 **研究动机**：Fluency Trap：用户既信任流畅幻觉，又在披露 AI 生成后低估准确内容；二元 Made with AI 标签不显示主张的证据支撑
- 🔬 **研究方法**：提出证据可视化界面 Provenance Density，展示文本中已验证主张的密度；81 人用户研究与 200 样本技术审计
- 📌 **结论**：理想化界面产生 +4.15 点（d=1.82）的真伪辨别差距，无信号组无可测辨别力；Consistency Veto 承载大部分判别信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative AI makes polished prose cheap to produce, users can no longer rely on fluency as a proxy for truth. We call this failure mode the Fluency Trap: users trust fluent hallucinations while also discounting accurate content once it is disclosed as AI-generated. Binary “Made with AI” labels respond with authorship disclosure, but they do not show what supports a claim. We propose Provenance Density, an evidence-visualization interface that shows the density of verified claims in a text. In a user study with 81 participants, an idealized Provenance Density interface produced a large discernment gap between truth and fabrication (+4.15 points, d = 1.82), whereas participants given no signal showed no detectable discrimination. A technical audit with 200 samples shows that retrieval density alone is insufficient; unexpectedly, the Consistency Veto carries most of the discriminative signal on dynamic queries. As AI-generated content becomes indistinguishable from human writing, effective transparency must move from authorship disclosure toward evidence visualization.

</details>

### 9. "I Would Have Written My Code Differently": Beginners Struggle to Understand LLM-Generated Code

📄 [arXiv](https://arxiv.org/abs/2504.19037)　📅 2025-04

**关键词**：`analysis`、`code comprehension`、`automation bias`、`overreliance measurement`

👤 **作者**：Yangtian Zi、Luisa Li、Arjun Guha、Carolyn Jane Anderson、Molly Q Feldman

- 🎯 **研究动机**：代码生成只是编程的一半，读、评估并整合（或拒绝）AI 代码对新手是否可行未被测量
- 🔬 **研究方法**：比较 32 名 CS1 学生对函数自然语言描述与 LLM 生成实现的跨任务理解，160 个任务实例
- 📌 **结论**：每任务成功率仅 32.5%，各人群无差别受困；主要障碍包括非母语壁垒、Python 语法不熟与 automation bias，凸显依赖 LLM 前的代码理解瓶颈

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are being increasingly adopted for programming work. Prior work shows that while LLMs accelerate task completion for professional programmers, beginning programmers struggle to prompt models effectively. However, prompting is just half of the code generation process -- when code is generated, it must be read, evaluated, and integrated (or rejected). How accessible are these tasks for beginning programmers? This paper measures how well beginners comprehend LLM-generated code and explores the challenges students face in judging code correctness. We compare how well students understand natural language descriptions of functions and LLM-generated implementations, studying 32 CS1 students on 160 task instances. Our results show a low per-task success rate of 32.5\%, with indiscriminate struggles across demographic populations. Key challenges include barriers for non-native English speakers, unfamiliarity with Python syntax, and automation bias. Our findings highlight the barrier that code comprehension presents to beginning programmers seeking to write code with LLMs.

</details>

### 10. Beyond Predictions: A Study of AI Strength and Weakness Transparency Communication on Human-AI Collaboration

📄 [arXiv](https://arxiv.org/abs/2508.09033)　📅 2025-08

**关键词**：`analysis`、`risk communication`、`trust calibration`、`strength-weakness explanation`

👤 **作者**：Tina Behzad、Nikolos Gurney、Ning Wang、David V. Pynadath

- 🎯 **研究动机**：人机团队效能依赖 AI 向用户传达自身强弱边界的方式，但传达多少信息如何影响信任校准缺乏受控证据
- 🔬 **研究方法**：在模型错误上训练决策树使 AI 能识别并解释自己可能出错的位置，在收入预测任务的用户研究中改变 AI 洞察与解释的信息量
- 📌 **结论**：AI 性能洞察提升任务表现，传达对自身强弱的自我认识改善信任校准，证明信息交付方式直接塑造用户依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The promise of human-AI teaming lies in humans and AI working together to achieve performance levels neither could accomplish alone. Effective communication between AI and humans is crucial for teamwork, enabling users to efficiently benefit from AI assistance. This paper investigates how AI communication impacts human-AI team performance. We examine AI explanations that convey an awareness of its strengths and limitations. To achieve this, we train a decision tree on the model's mistakes, allowing it to recognize and explain where and why it might err. Through a user study on an income prediction task, we assess the impact of varying levels of information and explanations about AI predictions. Our results show that AI performance insights enhance task performance, and conveying AI awareness of its strengths and weaknesses improves trust calibration. These findings highlight the importance of considering how information delivery influences user trust and reliance in AI-assisted decision-making.

</details>

### 11. LLMs in Cybersecurity: Friend or Foe in the Human Decision Loop?

📄 [arXiv](https://arxiv.org/abs/2509.06595)　📅 2025-09

**关键词**：`analysis`、`automation bias`、`cognitive diversity`、`security decision-making`

👤 **作者**：Irdin Pekaric、Philipp Zech、Tom Mattson

- 🎯 **研究动机**：LLM 作为认知协作者提升准确率的同时可能侵蚀独立推理、促成过度依赖与决策同质化，安全关键情境下缺乏检验
- 🔬 **研究方法**：两组探索性焦点小组（无辅助 vs LLM 辅助），测量决策准确率、行为韧性与依赖动态
- 📌 **结论**：LLM 提升常规决策的准确性与一致性，但降低认知多样性并加剧 automation bias（低韧性用户尤甚）；高韧性个体则能有效利用 LLM，说明认知特质调节 AI 收益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are transforming human decision-making by acting as cognitive collaborators. Yet, this promise comes with a paradox: while LLMs can improve accuracy, they may also erode independent reasoning, promote over-reliance and homogenize decisions. In this paper, we investigate how LLMs shape human judgment in security-critical contexts. Through two exploratory focus groups (unaided and LLM-supported), we assess decision accuracy, behavioral resilience and reliance dynamics. Our findings reveal that while LLMs enhance accuracy and consistency in routine decisions, they can inadvertently reduce cognitive diversity and improve automation bias, which is especially the case among users with lower resilience. In contrast, high-resilience individuals leverage LLMs more effectively, suggesting that cognitive traits mediate AI benefit.

</details>

### 12. Editing with AI: How Doctors Refine LLM-Generated Answers to Patient Queries

📄 [arXiv](https://arxiv.org/abs/2511.19940)　📅 2025-11

**关键词**：`analysis`、`clinical oversight`、`automation bias`、`draft-editing workflow`

👤 **作者**：Rahul Sharma、Pragnya Ramjee、Kaushik Murali、Mohit Jain

- 🎯 **研究动机**：LLM 为临床医生生成患者问答草稿日益普遍，但医生如何修订这些草稿及其中的人因风险缺乏研究
- 🔬 **研究方法**：9 名眼科医生在 144 个白内障手术问题上跨三种条件（从零撰写、直接编辑 LLM 草稿、指令式间接编辑）的混合方法研究
- 📌 **结论**：LLM 输出总体准确但偶发错误与 automation bias 证明人工监督必要；间接编辑省力但引入错误，直接编辑精确但负担高，本地化改写是主要编辑形态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Patients frequently seek information during their medical journeys, but the rising volume of digital patient messages has strained healthcare systems. Large language models (LLMs) offer promise in generating draft responses for clinicians, yet how physicians refine these drafts remains underexplored. We present a mixed-methods study with nine ophthalmologists answering 144 cataract surgery questions across three conditions: writing from scratch, directly editing LLM drafts, and instruction-based indirect editing. Our quantitative and qualitative analyses reveal that while LLM outputs were generally accurate, occasional errors and automation bias revealed the need for human oversight. Contextualization--adapting generic answers to local practices and patient expectations--emerged as a dominant form of editing. Editing workflows revealed trade-offs: indirect editing reduced effort but introduced errors, while direct editing ensured precision but with higher workload. We conclude with design and policy implications for building safe, scalable LLM-assisted clinical communication systems.

</details>

### 13. Explainable AI as a Double-Edged Sword in Dermatology: The Impact on Clinicians versus The Public

📄 [arXiv](https://arxiv.org/abs/2512.12500)　📅 2025-12

**关键词**：`analysis`、`automation bias`、`XAI over-reliance`、`expertise moderation`

👤 **作者**：Xuhai Xu、…、Marzyeh Ghassemi

- 🎯 **研究动机**：可解释 AI 旨在支持人机交互，却有证据显示其悖论性地诱发过度依赖或偏见，且对专家与公众的影响可能不同
- 🔬 **研究方法**：两个大尺度实验（623 名普通人、153 名初级保健医生）结合公平性诊断模型与多种 XAI 解释，检验 LLM 解释对诊断表现的影响
- 📌 **结论**：肤色均衡的 AI 辅助提升准确率并缩小差距，但 LLM 解释使普通用户出现更强 automation bias（AI 对时增益、错时受损），资深医生则保持韧性；先呈现 AI 建议在 AI 错误时拖累两组

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial intelligence (AI) is increasingly permeating healthcare, from physician assistants to consumer applications. Since AI algorithm's opacity challenges human interaction, explainable AI (XAI) addresses this by providing AI decision-making insight, but evidence suggests XAI can paradoxically induce over-reliance or bias. We present results from two large-scale experiments (623 lay people; 153 primary care physicians, PCPs) combining a fairness-based diagnosis AI model and different XAI explanations to examine how XAI assistance, particularly multimodal large language models (LLMs), influences diagnostic performance. AI assistance balanced across skin tones improved accuracy and reduced diagnostic disparities. However, LLM explanations yielded divergent effects: lay users showed higher automation bias - accuracy boosted when AI was correct, reduced when AI erred - while experienced PCPs remained resilient, benefiting irrespective of AI accuracy. Presenting AI suggestions first also led to worse outcomes when the AI was incorrect for both groups. These findings highlight XAI's varying impact based on expertise and timing, underscoring LLMs as a "double-edged sword" in medical AI and informing future human-AI collaborative system design.

</details>

### 14. The LLM Fallacy: Misattribution in AI-Assisted Cognitive Workflows

📄 [arXiv](https://arxiv.org/abs/2604.14807)　📅 2026-04

**关键词**：`analysis`、`capability misattribution`、`automation bias`、`perceived competence`

👤 **作者**：Hyunwoo Kim、Harin Yu、Hanau Yi

- 🎯 **研究动机**：LLM 使用如何重塑用户对自身能力的认知此前缺乏概念化
- 🔬 **研究方法**：提出 LLM fallacy 概念框架：个体把 LLM 辅助产出误当作自身独立能力的证据，造成感知与实际能力的系统性背离；置于 automation bias 与认知卸载文献中并给出跨领域表现类型学
- 📌 **结论**：LLM 的不透明、流畅与低摩擦交互掩盖人机贡献边界，使用户从产出而非过程推断能力，对教育、招聘与 AI 素养提出直接挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid integration of large language models (LLMs) into everyday workflows has transformed how individuals perform cognitive tasks such as writing, programming, analysis, and multilingual communication. While prior research has focused on model reliability, hallucination, and user trust calibration, less attention has been given to how LLM usage reshapes users' perceptions of their own capabilities. This paper introduces the LLM fallacy, a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence, producing a systematic divergence between perceived and actual capability. We argue that the opacity, fluency, and low-friction interaction patterns of LLMs obscure the boundary between human and machine contribution, leading users to infer competence from outputs rather than from the processes that generate them. We situate the LLM fallacy within existing literature on automation bias, cognitive offloading, and human-AI collaboration, while distinguishing it as a form of attributional distortion specific to AI-mediated workflows. We propose a conceptual framework of its underlying mechanisms and a typology of manifestations across computational, linguistic, analytical, and creative domains. Finally, we examine implications for education, hiring, and AI literacy, and outline directions for empirical validation. We also provide a transparent account of human-AI collaborative methodology. This work establishes a foundation for understanding how generative AI systems not only augment cognitive performance but also reshape self-perception and perceived expertise.

</details>

### 15. Warning About AI Fallibility Increases Help-Seeking in an Intelligent Tutoring System

📄 [arXiv](https://arxiv.org/abs/2606.03822)　📅 2026-06

**关键词**：`analysis`、`risk communication`、`transparency intervention`、`help-seeking behavior`

👤 **作者**：Tomohiro Nagashima、Mirella Hladký、Vera Rief

- 🎯 **研究动机**：AI 学习环境存在幻觉风险，轻量透明性干预（告知系统可能出错）是否改变学习者行为缺乏实验证据
- 🔬 **研究方法**：252 名学生的课堂实验：数学智能辅导系统的两版本（含/不含 AI 可能出错的警告），用日志分析求助行为、错误率与用时
- 📌 **结论**：被警告的学生显著请求更多提示（系统实际行为完全相同），说明轻量透明干预能改变交互策略而不必然改善或损害即时表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work in Technology-Enhanced Learning and Human-Computer Interaction highlights the importance of transparency and trust calibration in AI-supported learning environments as they pose a risk of hallucinations. In this study, we investigate whether a simple transparency intervention that warns students that a pedagogical agent may make mistakes affects learner behavior in a math intelligent tutoring system. We conducted a classroom experiment with 252 school students using two system versions: one including a warning message about potential system errors, and one that does not mention potential errors. Using log data, we analyzed students' problem-solving performance data, including help-seeking behavior, error rate, and time-on-task. Results show that students who were warned about potential AI errors requested significantly more hints than those in the other condition, even though the actual system behavior was exactly the same. This finding suggests that lightweight transparency interventions can influence learners' interaction strategies without necessarily improving or impairing immediate performance.

</details>

### 16. Habituation at the Gate: Rising Approval and Declining Scrutiny in Human Review of AI Agent Code

📄 [arXiv](https://arxiv.org/abs/2606.22721)　📅 2026-06

**关键词**：`analysis`、`oversight failure`、`reviewer habituation`、`longitudinal measurement`

👤 **作者**：Haoran Yu、…、Yihang Chen

- 🎯 **研究动机**：AI 编码代理大规模提交 PR 时，人类审阅者对 AI 代码的审查是否会随时间松懈是监督有效性的核心问题
- 🔬 **研究方法**：AIDev 数据集上 400 名重复审阅者 7 个月内 11,429 次审查的审阅者内纵向分析，比较各审阅者早晚期审查行为并控制日历时间、PR 难度
- 📌 **结论**：批准率从 30.1% 升至 36.8%（p<10⁻⁶），十分位累计差距 +14.5pp 且为经验驱动、agent 特异；同时审查排队时间增 3.5 倍而行内评论量降 22%，最符合负荷增长下的反射性习惯化而非理性信任校准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI coding agents (e.g., GitHub Copilot, Devin, OpenAI Codex, Cursor) submit pull requests to open-source repositories at scale, a key question arises: do human reviewers gradually lower their scrutiny for AI-generated code over time? We conduct a longitudinal within-reviewer analysis using the AIDev dataset, studying 400 repeat reviewers who collectively submitted 11,429 reviews over a seven-month observation period. Comparing each reviewer's early and late review episodes, we observe a population-level shift in approval rate from 30.1% to 36.8% (Wilcoxon signed-rank p &lt; 10^{-6} on paired shifts). Pooled by within-reviewer experience decile, the cumulative gap reaches +14.5 pp from first to tenth decile. This shift is experience-driven (persists after controlling for calendar time), agent-specific (human PR approval rates decline over the same period), and not explained by PR difficulty (median PR size is flat). However, review latency increases rather than decreases (+3.5x), while inline comment volume decreases (-22%, p=0.0014), suggesting reviewers spend more time in queue but less time actively inspecting code. The combination of rising approval, declining comment effort, and increasing queue time is most consistent with reflexive habituation under growing workload rather than rational trust calibration alone.

</details>

### 17. AI Agents Push Humans Out of the Loop

📄 [arXiv](https://arxiv.org/abs/2608.23642)　📅 2026-08

**关键词**：`analysis`、`oversight degradation`、`skill atrophy`、`agent design affordance`

👤 **作者**：Margaret Mitchell、Avijit Ghosh、Samir Passi

- 🎯 **研究动机**：人类监督常被当作 AI agent 自治风险的默认解药，但当前 agent 设计可能恰恰在削弱有效监督所需的认知能力
- 🔬 **研究方法**：立场论文：把自动化与 HCI 研究连接到 AI agent 流程，论证现有开发部署方式不支持有效监督反而促其退化，并给出设计层可供性与组织协议
- 📌 **结论**：应把监督者的情境目标与认知需求置于与 agent 能力同等的重要性，否则 agent 系统将持续被动侵蚀其赖以存在的人类技能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents pose significant risks as they are granted increasing autonomy. A commonly proposed solution is human oversight and keeping a ''human in the loop'', but this is not a simple solution: Not only do current approaches to AI agent design impede effective human oversight, but the cognitive capacities required for it are also themselves degraded by extended use of AI systems. This position paper argues that current approaches to the development and deployment of AI agent systems do not support effective human oversight -- they contribute to its degradation. To address this, a top priority in the advancement of AI agents should be supporting the situated goals and cognitive requirements of effective human oversight, treating the human needs of overseers at the same level of importance as AI agent capability. To put this idea into practice, we connect work on automation and human-computer interaction to AI agent processes, outlining design-level affordances and organizational protocols that (1) support overseers in exercising critical judgement and (2) counteract the skill atrophy that arises from extended use of automation. We urge developers and deployers to adopt these or similar approaches. Without explicit support for the cognitive demands of effective human-agent interaction, AI agent systems will continue to passively incentivize the degradation of the very human skills they rely on.

</details>

### 18. When Review Alone No Longer Scales: Layered Supervision in AI-Assisted Software Engineering

📄 [arXiv](https://arxiv.org/abs/2608.26316)　📅 2026-08

**关键词**：`analysis`、`supervision scaling`、`guardrail layering`、`oversight restructuring`

👤 **作者**：Markus Stolze、Mirco Strässle

- 🎯 **研究动机**：高吞吐 AI 辅助开发使代码审查等既有 guardrail 承压，组织如何重新分配监督工作知之甚少
- 🔬 **研究方法**：五位软件工程从业者的定性访谈加更大范围从业者调查，追踪 guardrail 机制在 AI 生成洪流下的演化
- 📌 **结论**：组织把监督分布到预防性（架构意图外化为机器可解释形式）、可执行（lint/测试/CI-CD 复用为可扩展监督设施）与人类监督（从逐行检查转向架构推理与可维护性）三层，单一 guardrail 不再独自承担监督负载

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-assisted development tools enable software engineers to generate implementations at substantially higher speed and volume than in traditional workflows. Software teams have long relied on guardrails -- standing control mechanisms such as code review, linting, testing, and CI/CD pipelines -- to maintain quality and coordination. High-throughput AI-assisted generation increases pressure on these guardrails -- straining their capacity to keep pace with the volume and rate of generated changes -- and reshapes how organizations supervise development workflows, yet relatively little is known about how existing guardrails evolve in response. We conducted a qualitative interview study with five software engineering practitioners, situated within a broader practitioner survey. Our findings indicate that organizations distribute the work of supervision across multiple guardrail layers: preventive guardrails (produced by externalizing architectural intent and conventions into machine-interpretable form), executable guardrails (linting, testing, and CI/CD repurposed as scalable supervision infrastructure), and human oversight (shifting from line-by-line inspection toward supervisory interpretation focused on architectural reasoning, explainability, and long-term maintainability). We characterize this as a transition from review- centric guardrails toward layered supervision, in which no single guardrail carries the supervision load alone.

</details>