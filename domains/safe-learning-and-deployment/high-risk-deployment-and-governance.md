# 高风险部署与治理

[返回上级目录](README.md)

## 研究方向

研究医疗、心理健康、AI companion、法律、金融、教育、公共部门和关键基础设施中的 AI 风险，以及 audit、authority、accountability 和 incident evidence；收录要求问题直接影响高后果决策、长期关系伤害或部署责任，并给出可检验的失效、审计或控制机制。一般领域能力提升、普通欺诈分类和纯治理倡议不收录。

## 研究脉络

- **领域可靠性：** 医疗、心理健康、AI companion、法律和金融 benchmark 测量 hallucination、bias、calibration、关系伤害与 unsafe advice。
- **流程级防护：** Symbolic constraint、risk triage、authority gate 和 audit receipt 把控制嵌入工作流。
- **组织治理：** Runtime evidence、authority decomposition、audit 和 action gate 研究责任如何跨开发者与部署者落实为可检查控制。
- **当前边界：** 技术评测、法律义务和真实组织流程之间仍缺少统一可审计接口。

## 医疗、心理健康与 AI Companion 部署

### 1. When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha

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

### 2. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

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

### 3. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

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

### 4. Demographic Injection in Medical Language Models under Diversity, Equity, and Inclusion Prompts

📄 [arXiv](https://arxiv.org/abs/2608.15254)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Diego Mardian、Frank Liu

- 🎯 **研究动机**：临床 AI 指南推荐用 DEI prompt 引导推理，其凭空添加患者人口学属性的副作用未被测量
- 🔬 **研究方法**：47 个模型、4 个医学基准、376,000 条回应经已验证 judge 管线评分，以长度匹配对照分离长度效应
- 📌 **结论**：单句 DEI prompt 把人口学注入率从 0.7% 抬至 33.1%（47/47 模型，47 倍）；0.25-2.4% 回应把虚构属性挂到具体患者并改变推荐答案，其中 99.8% 转向错误选项

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clinical-AI guidance increasingly recommends prompting language models to reason with attention to diversity, equity, and inclusion (DEI). We measure a side effect that misrepresents patients: a one-sentence DEI prompt appended to a medical question leads models to add patient demographic attributes (race, socioeconomic status, sex) the question never stated, in effect rewriting who the patient is. We call this demographic injection. Across 47 models, four medical benchmarks, and 376,000 responses scored by a validated model-judge pipeline, a single DEI prompt raises the injection rate from 0.7% to 33.1% (47x) in all 47 of 47 models, attributable to the equity content rather than to added length (18x above a length-matched control; p=1.4x10^-14). Most added content is a general population statement that leaves the answer unchanged, but a smaller subset attaches an attribute to the specific patient or changes the selected option (0.25-2.4% of responses, 99.8% toward the incorrect option), where the invented demographic changes the answer the model recommends. Phrasing scales the effect from 14% to 56%. DEI prompts are just one example of a more general mechanism. Any instruction that nudges how a model reasons can make it add unrequested details, including details about the patient. Flagged outputs are treated as model errors under study, not clinical guidance.

</details>

### 5. TAF-MED: Multi-Turn Safety Refusal Collapse in LLMs Under Declared Self-Treatment Intent

📄 [arXiv](https://arxiv.org/abs/2608.10258)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Waleed Jamil、Raphael Schmitt

- 🎯 **研究动机**：现有基准不检验 LLM 在用户声明自我治疗意图后多轮追问下药物安全边界是否持续
- 🔬 **研究方法**：TAF-MED 为医师评审的 500 个固定三轮情景，8 个模型 4000 次对话；规则化自动 judge 标注 SAFE/LEAKY/UNSAFE，两名医师独立盲审子集（一致率 94.3%）
- 📌 **结论**：71.6% 对话含 UNSAFE 回应；首轮严格 SAFE 的对话中 61.4% 后续坍塌为 UNSAFE（模型坍塌率 24.4%-96.2%），首轮安全不是对话安全持续性的合格代理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly provide conversational health information that may influence treatment decisions, yet existing benchmarks do not isolate whether medication-safety boundaries persist across follow-ups after explicit self-treatment intent. We introduce TAF-MED, a physician-reviewed benchmark of 500 fixed three-turn scenarios, and evaluate eight LLMs across 4,000 conversations. A rubric-based automated judge labelled responses as SAFE, LEAKY, or UNSAFE, and two physicians independently annotated a model-balanced random subset of 400 conversations. We assessed unsafe guidance, collapse after a strictly SAFE initial response, and model-ranking stability. Overall, 71.6% of conversations contained an UNSAFE response, and 61.4% of those beginning with a strictly SAFE response later collapsed to UNSAFE; model-level collapse rates ranged from 24.4% to 96.2%. Four of 28 model pairs reversed order between initial unsafe and collapse rates. Automated labels achieved 94.3% agreement with the adjudicated physician reference ($κ= 0.895$). These findings show that first-turn safety is an incomplete proxy for conversational safety persistence and motivate evaluation across complete dialogue trajectories. We will release TAF-MED on Hugging Face to support reproducible research on multi-turn medical safety.

</details>

### 6. RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation

🌐 [Project](https://doi.org/10.1145/3805712.3809604)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`defense`、`medication recommendation`、`contraindication risk`、`clinical oversight`、`risk-aware reasoning`、`clinical safety`

- 🎯 **研究动机**：药物推荐缺风险感知，禁忌等临床风险高
- 🔬 **研究方法**：RES-MR以风险感知推理生成可解释且安全的用药建议
- 📌 **结论**：降低禁忌等临床风险并保持推荐效果

### 7. Risk Governance for Generative AI Mental Health Support: A Multi-Turn Safety Architecture

📄 [arXiv](https://arxiv.org/abs/2607.22692)　📅 2026-07

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Anabela C. Areias、…、Ricardo Rei

- 🎯 **研究动机**：LLM 情感支持缺乏随会话风险演化而安全治理的机制，已有方法只检测风险不塑造响应
- 🔬 **研究方法**：构建模型无关的多轮安全治理架构：上下文风险检测+推理验证+协议引导的响应生成，用基于真实叙事的合成对话在 GPT-5-chat 与 Qwen3.5-27B 上评估
- 📌 **结论**：风险检测特异性 0.85、敏感性 0.92，临床偏好的升级响应增加 25.6-59.2 个百分点并保持共情连接，跨对话长度与模型稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for emotional support despite lacking mechanisms to safely govern evolving mental health risk. Existing safety approaches primarily detect risk but rarely shape how models respond as conversational risk unfolds. We developed a model-agnostic safety governance architecture that combines contextual risk detection, reasoning-based verification, and protocol-guided response generation for multi-turn mental health interactions. Synthetic conversations grounded in real-world mental health narratives were used to evaluate the architecture's performance, tested with GPT-5-chat and Qwen3.5-27B, achieving high risk detection performance (specificity: 0.85 (95\%CI: 0.78;0.91), sensitivity: 0.92 (95\%CI: 0.88;0.95)) and increasing clinician-preferred escalation responses by 25.6--59.2pp while preserving rapport and connection. Performance remained stable across conversation length and generalized across both proprietary and open-source models. These findings demonstrate that clinically-grounded safety governance can extend beyond risk detection to improve how LLMs manage evolving mental health risk, providing a scalable framework for safer deployment across models.

</details>

### 8. When Can We Trust LLMs in Mental Health? Large-Scale Benchmarks for Reliable LLM Evaluation

🎓 [Official](https://aclanthology.org/2026.eacl-long.180/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`mental-health LLM`、`judge calibration`、`safety rating`、`judge reliability`

👤 **作者**：Abeer Badawi、…、Elham Dolatabadi

- 🎯 **研究动机**：心理健康对话评估面临情感与认知复杂性，现有基准规模小、真实性差，且缺乏 judge 可信度评估框架
- 🔬 **研究方法**：提出 MentalBench-100k（1 万条真实治疗对话配 9 个 LLM 回复共 10 万对）与 MentalAlign-70k（4 个 LLM judge 与人类专家的 7 万评分）；用 ICC 统计框架量化一致性与偏差
- 📌 **结论**：LLM judge 存在系统性分数膨胀，认知支持类属性可靠而共情精度低，安全与相关性评估部分不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating Large Language Models (LLMs) for mental health support poses unique challenges to reliable evaluation due to the emotionally and cognitively complex nature of therapeutic dialogue. Existing benchmarks are limited in scale, authenticity, and reliability, often relying on synthetic or social media data, and lack frameworks to assess when automated judges can be trusted. To address the need for large-scale authentic dialogue datasets and judge-reliability assessment, we introduce two benchmarks that provide a framework for generation and evaluation in this domain. MentalBench-100k consolidates 10,000 authentic single-session therapeutic conversations from three real-world scenarios datasets, each paired with nine LLM-generated responses, yielding 100,000 response pairs. MentalAlign-70k reframes evaluation by comparing four high-performing LLM judges with human experts across 70,000 ratings on seven attributes, grouped into Cognitive Support Score (CSS) and Affective Resonance Score (ARS). We then employ the Affective–Cognitive Agreement Framework, a statistical methodology using intraclass correlation coefficients (ICC) with confidence intervals to quantify agreement, consistency, and bias between LLM judges and human experts. Our analysis reveals systematic inflation by LLM judges, strong reliability for cognitive attributes such as guidance and informativeness, reduced precision for empathy, and some unreliability in safety and relevance. Our contributions establish new methodological and empirical foundations for the reliable and large-scale evaluation of LLMs in mental health contexts.

</details>

### 9. ProMedical: Hierarchical Fine-Grained Criteria Modeling for Medical LLM Alignment via Explicit Injection

🎓 [Official](https://aclanthology.org/2026.acl-long.1714/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`medical AI`、`high-risk deployment`、`risk governance`、`failure mitigation`

👤 **作者**：He Geng、…、Xiaodong Tao

- 🎯 **研究动机**：粗粒度偏好信号与多维复杂临床协议错位，医学 LLM 对齐困难
- 🔬 **研究方法**：ProMedical-Preference-50k（人机环加医生 rubric）；Explicit Criteria Injection 训练显式解耦安全约束与一般能力的多维奖励模型，经 GRPO 优化；ProMedical-Bench 双盲专家裁定评测
- 📌 **结论**：Qwen3-8B 总体准确率提 22.3%、安全合规提 21.7%，媲美专有前沿模型且在 UltraMedical 上表现相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning Large Language Models (LLMs) with high-stakes medical standards remains a significant challenge, primarily due to the dissonance between coarse-grained preference signals and the complex, multi-dimensional nature of clinical protocols. To bridge this gap, we introduce ProMedical, a unified alignment framework grounded in fine-grained clinical criteria. We first construct ProMedical-Preference-50k, a dataset generated via a human-in-the-loop pipeline that augments medical instructions with rigorous, physician-derived rubrics. Leveraging this corpus, we propose the Explicit Criteria Injection paradigm to train a multi-dimensional reward model. Unlike traditional scalar reward models, our approach explicitly disentangles safety constraints from general proficiency, enabling precise guidance during reinforcement learning. To rigorously validate this framework, we establish ProMedical-Bench, a held-out evaluation suite anchored by double-blind expert adjudication. Empirical evaluations demonstrate that optimizing the Qwen3-8B base model via ProMedical-RM -guided GRPO yields substantial gains, improving overall accuracy by 22.3% and safety compliance by 21.7%, effectively rivaling proprietary frontier models. Furthermore, the aligned policy generalizes robustly to external benchmarks, demonstrating performance comparable to state-of-the-art models on UltraMedical. We publicly release our datasets, reward models, and benchmarks to facilitate reproducible research in safety-aware medical alignment.

</details>

### 10. Calibrated? Not for Everyone: How Sexual Orientation and Religious Markers Distort LLM Accuracy and Confidence in Medical QA

🎓 [Official](https://aclanthology.org/2026.acl-short.36/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`medical AI`、`high-risk deployment`、`risk governance`、`failure mitigation`

👤 **作者**：Alberto Testoni、Iacer Calixto

- 🎯 **研究动机**：临床安全部署需要不确定度校准，但患者社会描述符（性取向、宗教）对准确率与置信度的影响未知
- 🔬 **研究方法**：在 2364 道医学题及反事实变体上评估 9 个通用与生物医学 LLM，配临床医生验证的开放生成案例研究
- 📌 **结论**：同性恋标记一致触发性能下降，交叉身份产生非可加的校准损害；社会身份 cues 影响置信信号可靠性，威胁基于置信的临床流程

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe clinical deployment of Large Language Models (LLMs) requires not only high accuracy but also robust uncertainty calibration to ensure models defer to clinicians when appropriate. Our paper investigates how social descriptors of a patient (specifically sexual orientation and religious affiliation) distort these uncertainty signals and model accuracy. Evaluating nine general-purpose and biomedical LLMs on 2,364 medical questions and their counterfactual variants, we demonstrate that identity markers cause a “calibration crisis”. Homosexual markers consistently trigger performance drops, and intersectional identities produce idiosyncratic, non-additive harms to calibration. Moreover, a clinician-validated case study in an open-ended generation setting confirms that these failures are not an artifact of the multiple-choice format. Our results demonstrate that the presence of social identity cues does not merely shift predictions; it affects the reliability of confidence signals, posing a significant risk to equitable care and safe deployment in confidence-based clinical workflows.

</details>

### 11. TRIDENT: Benchmarking LLM Safety in Finance, Medicine, and Law

📄 [arXiv](https://arxiv.org/abs/2507.21134) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-07

**关键词**：`benchmark`、`high-risk deployment`、`risk governance`、`deployment audit`、`high-risk domain`、`professional ethics`

👤 **作者**：Zheng Hui、Yijiang River Dong、Ehsan Shareghi、Nigel Collier

- 🎯 **研究动机**：LLM 在法律、金融、医学等高风险领域的领域特异安全评估被忽视
- 🔬 **研究方法**：基于 AMA 医学伦理、ABA 职业行为准则与 CFA 道德准则定义领域安全原则，构建 Trident-Bench 并评测 19 个通用与领域模型
- 📌 **结论**：强通用模型可达基本要求，领域专用模型常在细微伦理差异上失手，亟需细粒度领域安全改进

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed in high-risk domains such as law, finance, and medicine, systematically evaluating their domain-specific safety and compliance becomes critical. While prior work has largely focused on improving LLM performance in these domains, it has often neglected the evaluation of domain-specific safety risks. To bridge this gap, we first define domain-specific safety principles for LLMs based on the AMA Principles of Medical Ethics, the ABA Model Rules of Professional Conduct, and the CFA Institute Code of Ethics. Building on this foundation, we introduce Trident-Bench, a benchmark specifically targeting LLM safety in the legal, financial, and medical domains. We evaluated 19 general-purpose and domain-specialized models on Trident-Bench and show that it effectively reveals key safety gaps -- strong generalist models (e.g., GPT, Gemini) can meet basic expectations, whereas domain-specialized models often struggle with subtle ethical nuances. This highlights an urgent need for finer-grained domain-specific safety improvements. By introducing Trident-Bench, our work provides one of the first systematic resources for studying LLM safety in law and finance, and lays the groundwork for future research aimed at reducing the safety risks of deploying LLMs in professionally regulated fields. Code and benchmark will be released at: https://github.com/zackhuiiiii/TRIDENT.

</details>

### 12. HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

📄 [arXiv](https://arxiv.org/abs/2608.22512)　📅 2026-08

**关键词**：`defense`、`runtime witnessing`、`external choke point`、`tamper-resistant evidence`、`attribution laundering`、`multi-agent accountability`

👤 **作者**：Christos Sardianos、…、Georgios Th. Papadopoulos

- 🎯 **研究动机**：自主多 agent 系统致害时无法查清事实、原因与责任：溯源取证抽象层级错误、形式因果假设因果模型已知、审计信任 agent 自我记录，而 attribution laundering 可把行为摊到冗余 agent 直到谁都不是 but-for cause
- 🔬 **研究方法**：HANSARD 参考架构：在 agent 触及范围外的五个 choke point 捕获证据使遗漏可检测，运行时累积 PROV-DM 类型化因果图并以三个指标实时门控监督，事后按 modified Halpern-Pearl 重放得出偶然效应与补偿集大小，synergy residual 度量组合致害
- 📌 **结论**：原因、责任与问责分开报告并各受证据层级上限约束，使 attribution laundering 可见，不再依赖涉事 agent 自产日志

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, attribution laundering, i.e., spreading an act across redundant agents until none is a but-for cause. Worse, the record is produced by the suspects, which comprises the assumption adopted throughout this work. Agents may therefore anticipate the investigation and the part of logging infrastructure may itself collude. In this paper, HANSARD is proposed, a reference architecture treating accountability as a life-cycle property. First, a readiness profile sealed before operation bounds what later findings may claim. Second, capturing at five choke points beyond the agents' reach makes omissions detectable, not only tampering. Third, a typed PROV-DM-aligned causal graph accrues as the system runs, and three indicators read it live to gate oversight without adjudicating. Fourth, post-incident replay yields contingent effects under the modified Halpern-Pearl definition, together with a compensation-set size. Finally, a synergy residual measures harm due to the combination rather than to individuals, making laundering visible. Cause, responsibility and accountability are then reported separately, each capped by an evidentiary tier, while a future research agenda is also provided.

</details>

### 13. Who Can Make the Action Happen? An Authority-Decomposition Framework for High-Risk Automated Systems

📄 [arXiv](https://arxiv.org/abs/2608.18965)　📅 2026-08

**关键词**：`tool`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Mengting Wu、Lin Wang、Yong Zhang

- 🎯 **研究动机**：authorized、approved、privileged 等标签回答不了哪些行动者实际能造成受保护执行这一因果问题
- 🔬 **研究方法**：建模组件、权力、资源、边界与替代实现结构（含更新、恢复、覆盖、禁用与替代调用），推导包含极小充分联盟并检验声称的执行边界是否独立于上游域
- 📌 **结论**：Havenlon 协议模型中普通见证需五个信任域而证书替换给出三域极小需求集；框架为分析工具，不认证实现或部署安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

High-risk automated systems distribute control across services, credentials, protected components, and lifecycle mechanisms. Labels such as authorized, approved, privileged, or protected therefore do not answer a basic causal question: which actors can actually make a consequential action occur? This paper provides an action-relative method for deriving which trust-domain coalitions are sufficient to cause protected execution, defined as the occurrence of a designated protected state transition. The framework models components, powers, resources, boundaries, and alternative realization structures; includes update, recovery, override, disablement, and alternative invocation; and separates causal control over execution from control over the authoritative account of an operation. It derives inclusion-minimal sufficient coalitions and tests whether claimed execution boundaries remain independent of designated upstream domains. Cross-domain analytical cases illustrate the method. In a split-control, release-intended, open-state, source-bounded Havenlon protocol model, the ordinary witness requires five trust domains, while certificate replacement yields a three-domain inclusion-minimal known requirement set among source-enumerated protocol witnesses; the Linux domain remains insufficient for the complete transition. Deployed global non-bypassability and boundary-bound veto coverage remain unresolved. The framework is a conceptual and analytical tool. It does not certify implementations, establish deployment security, guarantee complete discovery of hidden powers, or define evidence-verification semantics.

</details>

### 14. Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents

📄 [arXiv](https://arxiv.org/abs/2608.17718)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：An He、Yao Wang、Haibin Zhang

- 🎯 **研究动机**：长程 agent 的监督问题不只是每步局部有效，而是轨迹前缀是否仍对应用户授权的任务；现有监控不直接估计该前缀级关系
- 🔬 **研究方法**：定义本体信任并实例化为在线监控 RGE：按 Role、Goal、Evidence 分解，LLM 仅推导结构化任务与步表示，信任态更新、投影与干预决策全部确定性、可重放审计
- 📌 **结论**：跨 OSWorld、FinanceBench、EICU-AC 轨迹库，RGE 前缀配对漂移检测超规则、judge、shield 基线，两个较大估计器下每基准 Drift F1 超 93% 且良性覆盖不低于 95.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-horizon agents increasingly operate across many steps, tools, and observa- tions. In this setting, the relevant oversight question is not only whether each action is locally valid, but whether the evolving trajectory still corresponds to the task the user authorized. Drift can accumulate quietly: an agent may call the right tool with plausible arguments at every step, while its prefix moves toward a broader role, an adjacent objective, or evidence the user never supplied. Existing monitors mostly check local compliance, deliver final-trace verdicts, or score generic risk; they do not directly estimate this prefix-level relation. We introduce ontological trust, a task-conditioned property of trajectory prefixes, and instantiate it as RGE, an online monitor that decomposes trust along Role, Goal, and Evidence. RGE uses LLMs only to derive structured task and step representations; trust-state updates, projec- tions, and intervention decisions are deterministic, so the output is a replayable and auditable trust trajectory rather than a single end-to-end judge verdict. We construct a cross-domain trajectory corpus from OSWorld, FinanceBench, and EICU-AC, covering benign executions, prefix-paired drift, and pseudo-consistency failures. On this corpus, RGE outperforms adapted rule-, judge-, and shield-style baselines on prefix-paired drift detection. With the two larger estimator models, it exceeds 93% Drift F1 on every benchmark while keeping benign coverage at or above 95.8%. Pseudo-consistency is harder: detection depends on whether task completion is externally visible, a structural limit we characterize empirically.

</details>

### 15. Bounded Sovereignty and the Control Tax: Pricing AI Oversight When the Deployer Does Not Own the Model

📄 [arXiv](https://arxiv.org/abs/2608.19216)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Zhen Wen Lim

- 🎯 **研究动机**：AI 控制协议假设部署方可插桩模型与管线，受监管组织经 API 使用前沿模型时该假设常失败
- 🔬 **研究方法**：提出有界主权（数据、模型、基础设施、交互四层的部分访问）、协议×层需求矩阵与主权折扣成本概念，并以 135 万合成案例的访问消融实验解读
- 📌 **结论**：完整日志改善诊断、预执行网关使干预可行、范围限制可提升安全但降低有用性——控制协议应显式声明访问假设

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI control research asks how to deploy models safely even when they may be misaligned, but many control protocols assume that the deployer can instrument the model and its surrounding pipeline. That assumption often fails for regulated organisations using frontier models through APIs or managed endpoints, where the deployer may control the business process but not the model weights, serving infrastructure, internal traces, update process, or full interaction logs. This paper introduces bounded sovereignty: partial technical and contractual access across the data, model, infrastructure, and interaction layers of the AI stack. It argues that these access conditions determine which control protocols can be executed in practice. The paper contributes a four-layer access typology, a protocol-by-layer requirements matrix, and the concept of sovereignty discount cost: the part of the control tax spent substituting for missing access through contracts, architecture, audit, vendor assurance, residual risk, or reduced system scope. It also reports a synthetic access-ablation experiment over 1.35 million synthetic case simulations and interprets the findings through an anonymised national-payments-infrastructure scenario. The experiment is not real-world payment-system evidence; it is a construct-validity exercise. The results show that complete logs improve diagnosis, a pre-execution gateway enables intervention, trace access and model-version control strengthen post-incident explanation, and scope restriction can improve safety while reducing usefulness. Control protocols proposed as general safety solutions should therefore state their access assumptions explicitly.

</details>

### 16. Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution

📄 [arXiv](https://arxiv.org/abs/2608.16891)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Adam Mazzocchetti

- 🎯 **研究动机**：agentic AI 把安全问题从有害文本生成转为有害操作副作用，prompt 级治理不构成执行边界
- 🔬 **研究方法**：Aegis 把模型输出当动作提议并经可信决策层仲裁：对照活动策略状态评估、服务端解析溯源、不确定时 fail-closed、Senate 式法定人数非单边授权
- 📌 **结论**：2100 条治理行零受治 mock-tool 应用与零风险副作用完成；1832 行保留可信溯源、1019 行 Senate 结算均有法定人数与签名记录

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI systems request tool actions that can modify files, send messages, launch jobs, or change workflow state. This shifts the safety problem from harmful text generation to harmful operational side effects. Prompt-level governance can shape model behavior, but it does not create an execution boundary. We introduce Aegis, a runtime governance system that treats model outputs as action proposals and mediates them through a trusted decision layer before tool execution. The model proposes; the trusted runtime decides. Aegis evaluates proposals against active policy state, resolves provenance server-side, fails closed under uncertainty, and routes selected cases through Senate-style settlement, a quorum- based non-unilateral authorization path. We evaluate Aegis on a repeated sandbox corpus spanning five run families, 42 tasks, three conditions, and ten repeats per family. Across 6,300 rows, prompt-policy conditioning produced 79 risky comparator-path leakage rows. Across 2,100 Aegis-governed rows, the system recorded zero governed mock-tool applications and zero governed risky side-effect completions. All 1,832 Aegis-attempted governed rows preserved trusted Aegis-resolved provenance, and all 1,019 Senate-settled rows had quorum and final signed tally evidence. These results do not prove general autonomous-agent safety. They support the narrower systems claim that, in this evaluated sandbox corpus, runtime action-boundary governance prevented observed risky proposals from becoming governed side effects.

</details>

### 17. Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest

📄 [arXiv](https://arxiv.org/abs/2604.08525) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`、`conflict of interest`、`chatbot advertising`

👤 **作者**：Addison J. Wu、Ryan Liu、Shuyue Stella Li、Yulia Tsvetkov、Thomas L. Griffiths

- 🎯 **研究动机**：LLM 开始承担广告创收职能，用户利益与公司激励冲突时模型如何抉择缺乏系统评估
- 🔬 **研究方法**：借鉴语言学与广告监管文献构建利益冲突分类框架，并配套评测套件检验当前模型
- 📌 **结论**：多数模型牺牲用户福利：Grok 4.1 Fast 在 83% 情况推荐贵近两倍的赞助品，GPT 5.1 94% 曝光赞助选项；行为随推理水平与用户社会经济地位显著变化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are trained to align with user preferences through methods like reinforcement learning. Yet models are beginning to be deployed not solely to satisfy users, but to generate revenue for the companies that created them through advertisements. This creates the potential for LLMs to face conflicts of interest, where the most beneficial response to a user may not be aligned with the company's incentives. For instance, a sponsored product may be more expensive but otherwise equal to another; here, what does (and should) the LLM recommend to the user? In this paper, we provide a framework for categorizing the ways in which conflicting incentives might change how LLMs interact with users, inspired by literature from linguistics and advertising regulation. We then present a suite of evaluations to examine how current models handle these tradeoffs. A majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing prices in unfavorable comparisons (Qwen 3 Next, 24%). Behaviors vary strongly with levels of reasoning and users' inferred socio-economic status. Our results highlight some hidden risks to users that can emerge when companies begin to subtly incentivize advertisements in chatbots.

</details>

### 18. “Org-Wide, We’re Not Ready": C-Level Lessons on Securing Generative AI Systems

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`enterprise GenAI`、`runtime monitoring`、`security governance`

- 🎯 **研究动机**：企业GenAI安全落地缺管理层视角的实证总结
- 🔬 **研究方法**：基于C-level访谈与调研总结组织级安全治理与runtime monitoring经验
- 📌 **结论**：多数组织自评尚未准备好org-wide的GenAI安全防护

### 19. SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.529/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`、`failure mitigation`、`safety evaluation`

👤 **作者**：Sihang Zhao、Kangrui Yu、Youliang Yuan、Pinjia He、Hongyi Wen

- 🎯 **研究动机**：教育 LLM 存在 pedagogical jailbreak：学生用求答案提示诱出解法而非脚手架指导，此前缺乏系统研究与评测
- 🔬 **研究方法**：用知识掌握图统一形式化安全、有用与教学行为，构建 9087 对学生问题的 SHAPE 基准，提出图增强辅导管线按前置概念与掌握缺口门控路由生成
- 📌 **结论**：多个 LLM 在两类教学越狱设定下安全性显著提升，同时保持接近满分的帮助性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been widely explored in educational scenarios. We identify a critical vulnerability in current educational LLMs, pedagogical jailbreaks, where students use answer-inducing prompts to elicit solutions rather than scaffolded instructions. To enable systematic study, we unify and formalize safe, helpful, and pedagogical behaviors with a knowledge-mastery graph and introduce SHAPE, a benchmark of 9,087 student-question pairs for evaluating tutoring behavior under adversarial pressure. We propose a graph-augmented tutoring pipeline that infers prerequisite concepts from queries, identifies mastery gaps, and routes generation between instructing and problem-solving via explicit gating. Experiments across multiple LLMs show that our method yields significantly improved safety under two pedagogical jailbreak settings, while maintaining near-ceiling helpfulness under the same evaluation protocol. Our code and data are available at https://github.com/MAPS-research/SHaPE

</details>

### 20. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

📄 [arXiv](https://arxiv.org/abs/2608.19974)　📅 2026-08

**关键词**：`benchmark`、`trajectory compliance`、`action-evidence monitor`、`rationale deception`、`execution-grounded monitoring`、`rule violation`

👤 **作者**：Yiyang Luo、…、Yunya Song

- 🎯 **研究动机**：金融 agent 可能引用规则却仍提交违反可执行约束的订单或误读监控证据
- 🔬 **研究方法**：ReguSim 受控金融合规环境与 ReguBench 目标标注监控基准，分离所述推理、尝试动作、执行强制与监控证据四产物；DeepSeek V4 Pro 与 Gemini 3.5 Flash 交易员运行
- 📌 **结论**：可见规则减少但不消除被拒动作，激励或人设框架改变行为；交易员理由会误导独立监控器除非出示强制证据；结构化简单基线匹配或超过纯 prompt LLM 监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning, attempted action, execution enforcement, and monitor evidence. In trader runs with DeepSeek V4 Pro and Gemini 3.5 Flash, visible rules reduce but do not eliminate rejected actions, and incentive or persona framing shifts behavior. A bridge study shows that trader rationales can mislead an independent monitor unless enforcement evidence is shown. In monitoring, simple structured baselines either match or exceed prompt-only LLMs. The results frame financial compliance evaluation as an audit of rule-grounded actions and evidence use, rather than a single compliance score.

</details>

### 21. Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch

📄 [arXiv](https://arxiv.org/abs/2608.17684)　📅 2026-08

**关键词**：`detection`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Jialong Li、Jialing Zhu

- 🎯 **研究动机**：自进化 agent 演化后的准确率不能说明是否保留既有正确行为与安全性
- 🔬 **研究方法**：在模拟电子银行审计 SkillOpt、AWM、ReasoningBank：匹配良性采集轨迹、密封评测端点、执行接地检查与独立状态重放
- 📌 **结论**：SkillOpt 良性效用 0.741 升至 0.837 但注入内容暴露 0.820 升至 0.943、ASR 升至 0.530、未授权金融状态变化达 0.685——审计须跟踪回归、攻击面接触与未授权状态变化而非只看准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving agents turn experience into reusable skills, workflows, or memories, but post-evolution accuracy alone does not show whether learned behavior preserves previously correct behavior or security. We audit SkillOpt, Agent Workflow Memory (AWM), and ReasoningBank in simulated e-banking using matched benign acquisition trajectories, sealed evaluation endpoints, execution-grounded checks, and independent state replay. On Qwen 3.7 Flash, SkillOpt raises benign utility from 0.741 to 0.837 while exposure to injected content rises from 0.820 to 0.943. Conditional attack success after exposure falls from 0.605 to 0.562, yet overall attack success rate (ASR) rises from 0.496 to 0.530 and unauthorized financial state changes rise to 0.685. Across three independently evolved lineages, capability, exposure, and unauthorized-state changes increase in all three, whereas ASR increases in only two. ReasoningBank raises utility to 0.859 without increasing aggregate ASR, although unauthorized state changes remain slightly above Static. AWM reveals a separate evaluation hazard: a literal WebArena text-action envelope disrupts tool execution in our native function-calling executor. In a post-hoc sensitivity test, removing only that envelope restores utility from 0.319 to 0.756, while exposure rises from 0.299 to 0.909 and ASR from 0.195 to 0.575. Auditing self-evolving financial agents therefore requires tracking regressions, attack-surface contact, unauthorized financial-state change, and artifact-executor compatibility, not accuracy alone.

</details>

### 22. When Personalization Becomes Bias: Structural and Discursive Religious Framing in AI-Generated Financial Advice

📄 [arXiv](https://arxiv.org/abs/2608.16909)　📅 2026-08

**关键词**：`analysis`、`religious-identity bias`、`financial advice`、`discursive framing`、`religious personalization`、`deployment audit`

👤 **作者**：Muhammad Salar Khan、Hamza Umer、Hasan Mahmud、Sandra Rothenberg

- 🎯 **研究动机**：LLM 金融建议中的宗教偏见及其语言实现机制缺乏系统证据
- 🔬 **研究方法**：三个 LLM 的 432 次模拟顾问-客户交互，覆盖 16 种宗教身份配对与股票、购房、人寿保险三项决策，回归加反身主题分析
- 📌 **结论**：无偏建议仅占 12-18%；宗教对称配对几乎总触发显式宗教框架，偏见经宗教锚定、不均衡文化信号与语气调制的语言机制实现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly integrated into financial advisory systems, yet their role in reproducing religious bias remains underexamined. This study provides systematic mixed-methods evidence of such bias across three LLMs (ChatGPT, Gemini, and Grok) using 432 simulated advisor-client interactions spanning 16 religious identity pairings (Christian, Muslim, Hindu, and non-religious) and three core household financial decisions: stock investment, house purchase, and life insurance. Combining regression and reflexive thematic analyses, we identify structural biases across models and decision contexts and the discursive mechanisms through which they are linguistically enacted. Unbiased advice appeared in only 12-18% of cases. Gemini consistently produced more bias than Grok, while ChatGPT's outputs were statistically comparable to Grok's. Religiously symmetric advisor-client pairings almost always triggered explicit religious framing, and non-religious clients often received advisor-centered religious appeals. Qualitative findings show that bias is linguistically manifested through religious anchoring, uneven cultural signaling, and tone modulation, varying by model and financial scenario. Stock investment prompts produced more financially technical responses, whereas life insurance advice triggered stronger religious language. The study develops a dual-dimensional framework linking structural bias rooted in model training and design with discursive bias expressed through language, advancing understanding of algorithmic bias in LLM-generated financial advice. It also shows that such advice adapts linguistically to identity cues, revealing a managerial dilemma between personalization and neutrality. Finally, it highlights implications for businesses, financial institutions, and regulators seeking to ensure neutrality, cultural sensitivity, and trust in AI-mediated advice.

</details>

### 23. Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading

📄 [arXiv](https://arxiv.org/abs/2601.13082) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-01　🏷 SaTML 2026

**关键词**：`attack`、`algorithmic trading`、`adversarial headline`、`financial impact`

👤 **作者**：Advije Rizvani、Giovanni Apruzzese、Pavel Laskov

- 🎯 **研究动机**：LLM 驱动算法交易系统对文本对抗样本的系统级货币风险从未被量化
- 🔬 **研究方法**：在无 ATS 访问、仅能改一日新闻标题的对手设定下，评估 Unicode 同形字替换（误导股票名识别）与隐藏文本子句（改变情感），在 Backtrader 实现融合 LSTM 价格预测与 LLM 情感的 ATS
- 📌 **结论**：14 个月内单日攻击即可使年化收益最多降低 17.7 个百分点；对抓取库与平台的分析及 27 位 FinTech 从业者调研证实现实可行性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly adopted in the financial domain. Their exceptional capabilities to analyse textual data make them well-suited for inferring the sentiment of finance-related news. Such feedback can be leveraged by algorithmic trading systems (ATS) to guide buy/sell decisions. However, this practice bears the risk that a threat actor may craft "adversarial news" intended to mislead an LLM. In particular, the news headline may include "malicious" content that remains invisible to human readers but which is still ingested by the LLM. Although prior work has studied textual adversarial examples, their system-wide impact on LLM-supported ATS has not yet been quantified in terms of monetary risk. To address this threat, we consider an adversary with no direct access to an ATS but able to alter stock-related news headlines on a single day. We evaluate two human-imperceptible manipulations in a financial context: Unicode homoglyph substitutions that misroute models during stock-name recognition, and hidden-text clauses that alter the sentiment of the news headline. We implement a realistic ATS in Backtrader that fuses an LSTM-based price forecast with LLM-derived sentiment (FinBERT, FinGPT, FinLLaMA, and six general-purpose LLMs), and quantify monetary impact using portfolio metrics. Experiments on real-world data show that manipulating a one-day attack over 14 months can reliably mislead LLMs and reduce annual returns by up to 17.7 percentage points. To assess real-world feasibility, we analyze popular scraping libraries and trading platforms and survey 27 FinTech practitioners, confirming our hypotheses. We notified trading platform owners of this security issue.

</details>

## 漏洞披露与责任治理

研究 AI 系统的 flaw reporting、bug bounty 与 responsible disclosure 机制，考察滥用风险如何内生于产品功能、如何被外部报告与纳入部署责任。

### 24. FLARE-AI: Flaw Reporting for AI

📄 [arXiv](https://arxiv.org/abs/2606.31567) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65171)　📅 2026-06　🏷 ICML 2026

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Shayne Longpre、…、Alex Pentland

- 🎯 **研究动机**：AI 缺陷报告生态碎片化：研究者不知向谁报告，接收方互不共享，报告重复且信息非结构化
- 🔬 **研究方法**：审计 12 个报告系统识别五大设计挑战，结合 32 组织 49 位专家反馈构建 FLARE-AI 开源报告系统：条件逻辑收集分流信息，一次提交可分发机器可读报告给多个接收方
- 📌 **结论**：降低报告门槛并提升跨方互操作，加速 AI 生态缺陷修复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Flaw reporting for deployed AI systems is fundamental to identifying system failures and improving AI safety. Yet the AI reporting ecosystem is fragmented: researchers who identify flaws often do not know what or where to report, and groups who receive reports rarely share them with other relevant stakeholders. As a result, good-faith reporters duplicate effort by submitting many different forms, and recipients lack standardized, triage-ready information. We audit 12 reporting systems published by AI developers, cybersecurity groups, and AI flaw aggregators, identifying five recurring design challenges spanning discoverability, scope, information collection, coordination, and guidance for strict-liability cases. Building on this analysis and feedback from 49 experts across 32 organizations representing developers, security researchers, and ecosystem coordinators, we introduce FLARE-AI, an open-source AI flaw reporting system designed for interoperability with existing systems. FLARE-AI streamlines flaw report creation by collecting triage-relevant information through conditional logic and early classification, then enables optional dissemination of standardized, machine-readable reports to multiple developers, coordinators, and incident registries from a single submission. By lowering barriers to reporting AI flaws and improving interoperability across stakeholders, FLARE-AI helps break down silos and accelerate remediation across the AI ecosystem.

</details>

### 25. "Abuse Risks are Often Inherent to Product Features": Exploring AI Vendors' Bug Bounty and Responsible Disclosure Policies

📄 [arXiv](https://arxiv.org/abs/2509.06136) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/piao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`bug bounty`、`abuse risk`、`jailbreak`、`AI vulnerability disclosure`

👤 **作者**：Yangheran Piao、Jingjie Li、Daniel W. Woods

- 🎯 **研究动机**：AI 漏洞披露依赖厂商接收并奖励报告，但厂商政策与学术研究、真实事件的差距未被测量
- 🔬 **研究方法**：混合方法分析 264 家 AI 厂商的漏洞披露政策（快照与纵向定性），并与 320 起 AI 事件及 260 篇学术论文对齐
- 📌 **结论**：36% 厂商无既定政策、仅 18% 提及 AI 风险；数据访问、授权与模型提取最常被列入范围，越狱与幻觉最常被排除；厂商处置 AI 漏洞可能滞后于学术与事件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As vendors adopt AI technologies, security researchers are working to uncover and fix related vulnerabilities, which is important given AI systems handle sensitive data and critical functions. This process relies on vendors receiving and rewarding AI vulnerability reports. To assess current practices, we analyzed the vulnerability disclosure policies of 264 AI vendors. We employed a mixed-methods approach, combining snapshot and longitudinal qualitative analysis, as well as comparing alignment with 320 AI incidents and 260 academic articles. Our analysis reveals that 36% of AI vendors have no established policy, and only 18% mention AI risks. Data access, authorization, and model extraction vulnerabilities are most consistently declared in-scope. Jailbreaking and hallucination are most commonly declared out-of-scope. We identify three profiles that reflect vendors' different positions toward AI vulnerabilities: proactive clarification (n = 46), silent (n = 115), and restrictive (n = 103). Our alignment results suggest that vendors may address AI vulnerability disclosure later than academic research and real-world incidents.

</details>
