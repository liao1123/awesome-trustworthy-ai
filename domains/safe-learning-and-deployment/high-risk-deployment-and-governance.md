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

### 4. Counterfactual Anatomy-guided Spatial-Temporal Decoding for Annotation-Free Hallucination Mitigation in Medical VLMs

📄 [arXiv](https://arxiv.org/abs/2608.17427)　📅 2026-08

**关键词**：`defense`、`VLM safety`、`high-risk deployment`、`risk governance`

👤 **作者**：Yifan Lu、…、Imran Razzak

- 🎯 **研究动机**：医学 VLM 幻觉缓解的解码期方法或缺解剖感知、或依赖真值标注
- 🔬 **研究方法**：CAST 全推理期免标注：广医学分割发现查询相关解剖区域，遮挡下答案似然下降的反事实干预选紧凑因果区域，结合无分类器引导与逐步时间对比的统一对比解码
- 📌 **结论**：SLAKE 与 MIMIC-CXR 上三个 Med-VLM 一致超过强基线，甚至超过依赖真值的解码策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Medical vision-language models (Med-VLMs) have demonstrated strong performance on medical visual question answering, yet they remain prone to hallucination, generating clinically unsupported statements that are insufficiently grounded in image evidence. Mitigation methods applied during decoding offer a practical solution, but they typically lack anatomical awareness or rely heavily on ground truth annotations, which limits their applicability. We propose Counterfactual Anatomy-guided Spatial-Temporal decoding (CAST), a framework that operates entirely during inference and requires no manual annotations for anatomically grounded hallucination mitigation. CAST automatically discovers anatomical regions relevant to the given query through broad medical segmentation. It then selects a compact, causally informative area using counterfactual intervention based on the drop in answer likelihood under occlusion. Guided by this chosen region, CAST performs a unified contrastive decoding process, combining classifier-free guidance to correct spatial attention with stepwise temporal contrast to regulate generation dynamics. Experiments on the SLAKE and MIMIC-CXR datasets across three Med-VLMs demonstrate that CAST consistently outperforms strong baselines and surpasses decoding strategies reliant on ground truth. Our results indicate that compact, automatically selected regions provide highly effective contrastive guidance without expert annotations, offering a practical and generalizable solution for improving spatial grounding and reducing hallucinations. Code is available at https://github.com/csyifan/CAST.

</details>

### 5. Demographic Injection in Medical Language Models under Diversity, Equity, and Inclusion Prompts

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

### 6. TAF-MED: Multi-Turn Safety Refusal Collapse in LLMs Under Declared Self-Treatment Intent

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

### 7. RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation

🌐 [Project](https://doi.org/10.1145/3805712.3809604)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`defense`、`medication recommendation`、`contraindication risk`、`clinical oversight`、`risk-aware reasoning`、`clinical safety`

- 🎯 **研究动机**：药物推荐缺风险感知，禁忌等临床风险高
- 🔬 **研究方法**：RES-MR以风险感知推理生成可解释且安全的用药建议
- 📌 **结论**：降低禁忌等临床风险并保持推荐效果

### 8. Risk Governance for Generative AI Mental Health Support: A Multi-Turn Safety Architecture

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

### 9. Same Facts, Different Updates: Inference Setup Shapes LLM Behavior in Medical Allocation

📄 [arXiv](https://arxiv.org/abs/2608.18108) · 📝 [OpenReview](https://openreview.net/forum?id=z06of44TcG)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Spencer Gibson、Tyler Crosse、Magnus Saebo、Achyutha Menon、Eyon Jang、Diogo Cruz

- 🎯 **研究动机**：模型除输入与场景框架偏差外，部署中积累的上下文也会引发意外行为，医疗资源分配中未测
- 🔬 **研究方法**：医疗场景：模型先给两人分配概率、再看带对比患者信息的单句新信息，比较有与无先前回复在上下文时的概率移位
- 📌 **结论**：四个模型中三个的配对上下文与独立推理概率移位方向相反（偏向 Person B 对 Person A）——上下文工程对敏感决策至关重要

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are being incorporated into sensitive and important decision-making processes across nearly all fields. While prior work studies model bias around inputs and scenario framing, models can also behave in unexpected and undesirable ways due to context accumulated over their deployment. In this work, we study a medical example in which a model is asked to assign resource-allocation probabilities to two people given brief clinical context, and then sees the same scenario with a single extra sentence containing contrasting patient information, either with or without its previous response in context. Across three of four tested models, the paired-context and independent-inference experiments have different probability shifts, often in opposite directions (in favor of Person B vs. in favor of Person A) when new information is provided. We include additional paired-context experiments to show the effect of varying attributes across scenario axes. Our findings show the context-dependent effect of patient information in a sensitive medical use case. More broadly, our work shows the importance of carefully incorporating LLM-based systems into decision-making processes, context engineering, and further model behavioral studies.

</details>

### 10. When Can We Trust LLMs in Mental Health? Large-Scale Benchmarks for Reliable LLM Evaluation

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

### 11. Responsible Evaluation of AI for Mental Health

🎓 [Official](https://aclanthology.org/2026.acl-long.347/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`high-risk deployment`、`risk governance`、`deployment audit`、`medical AI`、`failure mitigation`

👤 **作者**：Hiba Arnaout、…、Iryna Gurevych

- 🎯 **研究动机**：心理健康 AI 工具的评测碎片化，与临床实践、社会情境和真实用户体验脱节
- 🔬 **研究方法**：提出整合临床稳健性、社会情境与公平性的跨学科评测框架，分析 135 篇 *CL 文献，并给出评估/干预/信息综合三类支持的分类法与案例
- 📌 **结论**：识别出依赖通用指标、心理健康专业人士参与不足、安全与公平关注欠缺等反复出现的局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although artificial intelligence (AI) shows growing promise for mental health care, current approaches to evaluating AI tools in this domain remain fragmented and poorly aligned with clinical practice, social context, and first-hand user experience. This paper argues for a rethinking of responsible evaluation – what is measured, by whom, and for what purpose – by introducing an interdisciplinary framework that integrates clinical soundness, social context, and equity, providing a structured basis for evaluation. Through an analysis of 135 recent *CL publications, we identify recurring limitations, including over-reliance on generic metrics that do not capture clinical validity, therapeutic appropriateness, or user experience, limited participation from mental health professionals, and insufficient attention to safety and equity. To address these gaps, we propose a taxonomy of AI mental health support types – assessment-, intervention-, and information synthesis-oriented – each with distinct risks and evaluative requirements, and illustrate its use through case studies.

</details>

### 12. ProMedical: Hierarchical Fine-Grained Criteria Modeling for Medical LLM Alignment via Explicit Injection

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

### 13. Calibrated? Not for Everyone: How Sexual Orientation and Religious Markers Distort LLM Accuracy and Confidence in Medical QA

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

### 14. TRIDENT: Benchmarking LLM Safety in Finance, Medicine, and Law

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

### 15. InsufficiencyBench: Evaluating LLM legal advice on underspecified user queries

📄 [arXiv](https://arxiv.org/abs/2608.20220) · 📝 [OpenReview](https://openreview.net/forum?id=I02uMYmPR7)　📅 2026-08　🏷 ICML 2026

**关键词**：`benchmark`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Samuel J. Vincent、Daniel Calloway、Fangyi Yu、Andrew M. Bean、Nabeel Seedat

- 🎯 **研究动机**：法律 AI 基准假设查询完备，实践中用户会省略实质决定法律结果的事实
- 🔬 **研究方法**：InsufficiencyBench 定义八类缺失要素与三种结构失效模式（switch、gating、fatal prerequisite），202 项（58 基础查询+144 缺陷变体）由执业律师标注，覆盖六法域 24 州，评十个前沿模型
- 📌 **结论**：缺失要素识别无一模型超 F2=0.46、中位召回 0.44——模型要么无差别含糊要么在虚构假设下默默作答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Legal AI systems are increasingly used to answer legal questions, yet existing benchmarks assume queries arrive fully specified. In practice, users omit facts that materially determine the legal outcome. We introduce InsufficiencyBench, the first legal benchmark targeting query-side insufficiency: whether a model recognizes when a query lacks legally material information, identifies what is missing, and refrains from premature conclusions. We formalize a taxonomy of eight canonical missing-element categories across three structural failure modes---switch, gating, and fatal prerequisite--- and construct 202 benchmark items (58 base queries, 144 deficient variants) spanning six legal domains and 24 US jurisdictions and annotated by practising attorneys. Evaluating ten frontier models, we find that no model exceeds F2 = 0.46 on missing-element identification and that the median recall is 0.44. Models either hedge indiscriminately or answer silently under fabricated presumptions. No model both identifies and qualifies responses to deficient queries while directly addressing complete ones.

</details>

### 16. How Much Do Legal RAG Systems Still Hallucinate?

📄 [arXiv](https://arxiv.org/abs/2608.14210)　📅 2026-08

**关键词**：`analysis`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Souvick Das、Sallam Abualhaija、Domenico Bianculli

- 🎯 **研究动机**：法律域 RAG 的幻觉行为缺乏跨系统细粒度测量
- 🔬 **研究方法**：对八个法律 RAG 系统在 GDPR（英文）与国民民法典（法文）两语料上做 claim 级与 answer 级评测，并在 142 道法律专家问题上验证
- 📌 **结论**：幻觉普遍：最好系统低于 10%、最差近一半；含错误假设的 false-premise 问题幻觉率最高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hallucination is a major challenge for retrieval-augmented generation (RAG) systems in the legal domain, where ungrounded answers can lead to serious consequences. To better understand this problem, we conduct a fine-grained analysis of hallucination behavior in eight legal RAG systems across two legal corpora, the GDPR (in English) and a national civil law (in French). Using claim-level and answer-level evaluation, we report on hallucination density and severity, analyze performance across question categories and user personas, and validate our findings on an independent set of 142 legal-expert-authored questions. Our results show that hallucinations remain pervasive, ranging from less than 10% of responses for the best-performing systems to nearly half in the worst case. We further find that false-premise questions, containing incorrect assumptions that must be rejected, produce high hallucination rates on the manually-drafted questions.

</details>

### 17. Mitigating Legal Hallucinations via Symbolic Constraints and Analogical Precedents

🎓 [Official](https://aclanthology.org/2026.acl-long.633/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`legal AI`、`high-risk deployment`、`risk governance`、`failure mitigation`

👤 **作者**：Zixuan Huang、Yanxiang Ma、Luhan Wang、Yunke Wang、Duo Shi、Chang Xu

- 🎯 **研究动机**：法律域微调与 RAG 仍有幻觉风险，语义漂移与引用数量变化未被解决
- 🔬 **研究方法**：AALawyer 基于法律三段论的双检索器：Symbolic Constrained Retrieval 做闭集条文检索，Analogical Precedent Retrieval 基于新采集大型刑事数据集做开集判例推理
- 📌 **结论**：LawBench 与自建幻觉风险基准上缓解幻觉并提升法律推理可解释性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing potential of large language models (LLMs) in the legal domain, domain-specific finetuning and retrieval-augmented generation (RAG) methods have received widespread attention. However, current methods still suffer from hallucination risk and failing to resolve semantic drift and adapt to varying citation numbers. To address this, we propose Authoritative and Accurate Lawyer (AALawyer), a complementary dual-retriever framework based on the Legal Syllogism and the nature of different legal data. First, we introduce Symbolic Constrained Retrieval (SCR) for closed-set article retrieval, by constraining retrieval to the generative prediction. Second, we build Analogical Precedent Retrieval (APR) to retrieve open-set judicial precedents for reasoning with a newly collected large criminal dataset.Extensive experiments, including LawBench, our Hallucination Risk-Benchmark, and comprehensive ablation studies, demonstrate the effectiveness of AALawyer, which mitigates hallucinations while improving the explainability of legal reasoning.

</details>

### 18. Evaluating Structure-Aware Retrieval and Safety in Statute-Centric Legal QA

🎓 [Official](https://aclanthology.org/2026.acl-long.2112/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`legal AI`、`high-risk deployment`、`risk governance`、`RAG security`

👤 **作者**：Kyubyung Chae、…、Taesup Kim

- 🎯 **研究动机**：法律 QA 基准偏重判例法；制定法场景证据分散在层级链接文档，常规检索器失效且模型在上下文不全时幻觉
- 🔬 **研究方法**：SearchFireSafety 以消防安全法规为例：双轨评估——需引用感知检索的真实问题加压力测试幻觉与拒绝的合成部分上下文场景
- 📌 **结论**：图引导检索大幅提升性能，但领域适应模型在关键法定证据缺失时更易幻觉，揭示检索-安全权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Legal QA benchmarks have predominantly focused on case law, overlooking the unique challenges of statute-centric regulatory reasoning. In statutory domains, relevant evidence is distributed across hierarchically linked documents, creating a statutory retrieval gap where conventional retrievers fail and models often hallucinate under incomplete context. We introduce SearchFireSafety, a structure- and safety-aware benchmark for statute-centric legal QA. Instantiated on fire-safety regulations as a representative case, the benchmark evaluates whether models can retrieve hierarchically fragmented evidence and safely abstain when statutory context is insufficient. SearchFireSafety adopts a dual-track evaluation framework combining real-world questions that require citation-aware retrieval and synthetic partial-context scenarios that stress-test hallucination and refusal behavior. Experiments across multiple large language models show that graph-guided retrieval substantially improves performance, but also reveal a critical safety trade-off: domain-adapted models are more likely to hallucinate when key statutory evidence is missing. Our findings highlight the need for benchmarks that jointly evaluate hierarchical retrieval and model safety in statute-centric regulatory settings.

</details>

### 19. HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

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

### 20. Who Can Make the Action Happen? An Authority-Decomposition Framework for High-Risk Automated Systems

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

### 21. Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents

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

### 22. The Authority Resolution Framework: A Five-Domain Ontology for Governing Who and What Decides, at Scale

📄 [arXiv](https://arxiv.org/abs/2608.15832)　📅 2026-08

**关键词**：`tool`、`high-risk deployment`、`risk governance`、`deployment audit`

👤 **作者**：Parviz Shariff

- 🎯 **研究动机**：agent 技术上能做某动作不等于被授权做，权威的来源与范围缺机器可解释表示
- 🔬 **研究方法**：Authority Resolution Framework 五域本体（组织角色、业务概念、编码流程、机读权限与可执行系统、外部语境），Authority Relation 绑定行动者/动作/对象/有界语境/理由链与 DNA 系数，提供 JSON-LD 与知识图谱查询模式
- 📌 **结论**：为 agent 在执行重要动作前解析权威的来源、范围与语境有效性提供可机读推理基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI systems become increasingly capable of autonomous action, determining whether an agent is technically capable of performing an action is insufficient: the system must also determine whether the action is authorised in its context. This paper introduces the Authority Resolution Framework (ARF), a five-domain ontology for representing and resolving authority across organisational roles and informal influence, business concepts, codified processes, machine-readable permissions and executable systems, and external real-world context. ARF defines the Authority Relation (AR) as a cross-domain primitive binding an actor, action, object, bounded context, justification chain, and a calibration measure termed the DNA-Coefficient, which captures divergence between documented authority structures and authority as practiced. The framework provides a machine-interpretable representation of authority provenance and scope, with JSON-LD representations and knowledge-graph query patterns for authority resolution. ARF is designed to support AI agents in determining the provenance, scope and contextual validity of authority before executing consequential actions. The framework positions authority resolution as a knowledge-representation and reasoning problem at the intersection of ontology engineering, semantic AI, agentic AI and AI governance.

</details>

### 23. SimuGov: A Simulation Optimization Framework for Generative AI Governance Strategy Design

🌐 [Project](https://doi.org/10.1145/3770855.3818903)　📅 2026-08　🏷 KDD 2026

**关键词**：`tool`、`generative AI governance`、`stakeholder simulation`、`policy optimization`、`framework`

- 🎯 **研究动机**：生成式AI治理策略设计缺系统化工具
- 🔬 **研究方法**：SimuGov以利益相关方仿真加优化搜索治理策略
- 📌 **结论**：为治理策略设计与比较提供仿真优化框架

### 24. Bounded Sovereignty and the Control Tax: Pricing AI Oversight When the Deployer Does Not Own the Model

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

### 25. Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution

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

### 26. Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest

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

### 27. The Hidden Puppet Master: Predicting Human Belief Change in Manipulative LLM Dialogues

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

### 28. “Org-Wide, We’re Not Ready": C-Level Lessons on Securing Generative AI Systems

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`enterprise GenAI`、`runtime monitoring`、`security governance`

- 🎯 **研究动机**：企业GenAI安全落地缺管理层视角的实证总结
- 🔬 **研究方法**：基于C-level访谈与调研总结组织级安全治理与runtime monitoring经验
- 📌 **结论**：多数组织自评尚未准备好org-wide的GenAI安全防护

### 29. SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs

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

### 30. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

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

### 31. Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch

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

### 32. When Personalization Becomes Bias: Structural and Discursive Religious Framing in AI-Generated Financial Advice

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

### 33. Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading

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