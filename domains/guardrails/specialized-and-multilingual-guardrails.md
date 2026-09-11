# 专用领域与多语言 Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究通用 guard model 在专业术语、行业法规、儿童等特定用户群体、人际关系操纵、低资源语言、code-switching 和地区文化规范下的迁移失败，并构建对应 taxonomy、数据、benchmark 与专用审核模型。这里的目标不是简单翻译英文 safety dataset 或沿用通用风险标签，而是让风险定义来自行业规则、角色关系、发展心理、当地专家与法规，并同时检查领域能力、通用安全能力和未见语言、年龄线索或 policy 的泛化。

## 研究脉络

- **通用 taxonomy 的缺口：** 英文中心的 harm category 无法覆盖金融合规、治疗会谈、直播社区、法律要求和地区敏感语义，专业术语与必要的敏感讨论还会改变原本的安全决策边界。
- **用户群体适配：** Child-facing system 需要识别显式年龄与隐含儿童表达，并在多轮交互中维持发展阶段适当的解释、边界和求助指引，不能只复用成人 harmful-content refusal。
- **角色敏感决策：** 人际关系风险不能把同一主题统一拒绝；guard 需要区分操纵者的有害请求与受害者的求助，并累计多轮中逐步显现的 workflow 风险。
- **数据本地化：** PolyGuard 等工作扩大语言覆盖，SEA-SafeguardBench、UbuntuGuard、IndicGuard、ArabicDialectSafety、ASAS 与 Mod-Guide 进一步用 native author、地区专家、少数群体共创语料和本地法规替代纯机器翻译。
- **Policy-grounded moderation：** ML-Bench&Guard 和 FinGuard 从司法辖区或行业监管文本抽取规则，使 guard 能解释违反了哪条可变 policy，而不只输出通用 harmful label。
- **训练与效率：** MrGuard 用 multilingual reasoning 与 curriculum GRPO，CHILLGuard 用 model-aware preference alignment，LionGuard 2 证明高质量本地数据配合轻量 classifier 也可实际部署。
- **模块化专家：** GuardZoo 的分析显示单一 guard 会受到跨领域 task interference，RouteGuard 因而先识别 threat domain 再路由到 specialized expert。

## 专业行业 Guardrail

### 1. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

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

### 2. RxGuard: Knowledge-Guided Safety Guardrails for Medication Recommendation

🌐 [Project](https://doi.org/10.1145/3770855.3818849)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`medication safety`、`knowledge guardrail`、`high-stakes recommendation`

- 🎯 **研究动机**：高风险用药推荐缺知识引导的安全护栏
- 🔬 **研究方法**：RxGuard以知识库校验并修正推荐输出
- 📌 **结论**：减少不安全用药建议

### 3. EVADE-Bench: Multimodal Benchmark for Evaluating and Enhancing Evasive Content Detection

📄 [arXiv](https://arxiv.org/abs/2505.17654) · 📊 [Dataset](https://huggingface.co/datasets/koenshen/EVADE-Bench) · 🌐 [Project](https://doi.org/10.1145/3805712.3808579)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`benchmark`、`e-commerce moderation`、`cross-modal evasion`、`policy circumvention`、`evasive content`、`multimodal decomposition`

👤 **作者**：Ancheng Xu、…、Min Yang

- 🎯 **研究动机**：电商审核模型对拆字、暗语、裁图等规避内容脆弱，且无基准同时考察规则理解与混淆意图推断
- 🔬 **研究方法**：构建专家策展的中文多模态 EVADE-Bench，评测 26 个开源与闭源 LLM 及 VLM 的规避内容检测
- 📌 **结论**：SoTA 模型频繁误判；清晰规则分类显著减少误报，视觉描述与逻辑推断解耦的多 agent 分解带来明显准确率增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

E-commerce platforms increasingly rely on Large Language Models (LLMs) and Vision Language Models (VLMs) to detect illicit or misleading product content. However, these models remain vulnerable to evasive content, which refers to inputs that have been deliberately modified through techniques such as word splitting, euphemistic language, or image cropping to conceal policy violations while still conveying prohibited claims. Crucially, detecting such content requires a model to simultaneously master two capabilities: accurately comprehending complex rules, and correctly inferring the true intent behind deliberately obfuscated multimodal inputs. While prior work has separately explored LLM reasoning over complex rules and LLM-based detection of evasive content, no existing benchmark combines both within a unified evaluation framework. This gap is particularly consequential in e-commerce, where accurate moderation demands that both capabilities operate in concert. To address this gap, we introduce EVADE-Bench, the first expert-curated Chinese multimodal benchmark specifically designed to evaluate LLMs and VLMs on evasive content detection in real-world e-commerce scenarios. Our comprehensive evaluation of 26 open- and closed-source LLMs and VLMs reveals that even state-of-the-art models frequently misclassify evasive samples. We further demonstrate that clearer rule categorization significantly improves model prediction consistency and reduces false predictions, highlighting the critical role of benchmark design in enabling reliable evaluation. To explore paths for performance improvement, we investigate the feasibility of multi-agent decomposition for multimodal reasoning, wherein visual description and logical inference are decoupled into separate agents, and find that this strategy yields notable accuracy gains.

</details>

### 4. Triaging Threats to Specialized Guardrails

📄 [arXiv](https://arxiv.org/abs/2605.30693)　📅 2026-05

**关键词**：`defense`、`router-expert guard`、`threat triage`、`task interference`

👤 **作者**：Wenjie Jacky Mo、…、Muhao Chen

- 🎯 **研究动机**：安全风险跨异构威胁域而数据集碎片化、taxonomy 不一致，单体 guard 存在任务干扰
- 🔬 **研究方法**：构建 32,460 样本、15 类不安全类别的人工标注基准 GuardZoo；提出 RouteGuard 路由器-专家框架把会话分诊到专门 guard 做威胁特异检测
- 📌 **结论**：细粒度威胁检测超强护栏基线，OOD 泛化更好，并支持面向新威胁的模块化扩展

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Building robust safety guardrails is essential for deploying Large Language Models across diverse real-world applications. However, this goal remains challenging because safety risks span heterogeneous threat domains, while existing datasets cover only fragmented risk subsets and rely on inconsistent taxonomies. Consequently, it remains unclear whether current guardrails can generalize beyond narrow evaluation settings. To better understand the robustness of guardrail models, we first introduce GuardZoo, a unified human-annotated benchmark with 32,460 samples covering 15 distinct unsafe categories. Evaluation on GuardZoo reveals that monolithic guardrails suffer from task interference: different threat domains require distinct decision boundaries that are difficult to compress into a single model. We therefore propose RouteGuard, a router-expert framework that triages each conversation to specialized expert guardrails for threat-specific detection. Experiments show that RouteGuard improves fine-grained threat detection over strong guardrail baselines, generalizes better under out-of-domain evaluation, and supports flexible modular expansion to emerging threats.

</details>

### 5. FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions

📄 [arXiv](https://arxiv.org/abs/2605.29427)　📅 2026-05

**关键词**：`detection`、`financial compliance`、`regulation-grounded data`、`self-play RL`

👤 **作者**：Huaixia Dou、…、Chi Zhang

- 🎯 **研究动机**：现有 guard 模型基于通用伤害 taxonomy，忽略特定金融监管条文下的违规
- 🔬 **研究方法**：直接从监管文档归纳合规风险 taxonomy 并合成接地训练数据；以中国金融法规实例化 FinGuard-Bench（query 与 response 双级专家标注），基于 Qwen3-8B 经 SFT 加 self-play RL 训练 FinGuard
- 📌 **结论**：大幅超过专用 guard 与 Qwen3.5-397B-A17B、GPT-5.1 等更大模型，保留通用安全能力并可仅凭政策文档适配未见机构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed in financial services, a single non-compliant interaction can expose institutions to regulatory penalties and direct consumer harm. Existing guard models are built around general harm taxonomies and overlook violations grounded in specific financial regulations. We address this gap with a regulation-driven pipeline that operates directly on regulatory documents, inducing a financial compliance risk taxonomy and synthesizing grounded training data without any predefined violation categories. Instantiating the pipeline on Chinese financial regulations, we release \textbf{FinGuard-Bench}, to our knowledge the first benchmark for financial regulatory compliance detection, with expert-annotated labels at both the query and response levels. We further train \textbf{FinGuard}, a financial compliance detection model built on Qwen3-8B and trained on the regulation-grounded data via supervised fine-tuning and self-play reinforcement learning. On FinGuard-Bench, FinGuard substantially outperforms all baselines, including dedicated guard models and much larger general-purpose LLMs such as Qwen3.5-397B-A17B and GPT-5.1. Furthermore, FinGuard also preserves general safety capabilities and adapts to unseen institution-specific policies using policy documents alone. We will publicly release the code, prompts, and resources used in this work on GitHub.

</details>

### 6. AI Content Moderation in Therapy Conversations

📄 [arXiv](https://arxiv.org/abs/2605.25454)　📅 2026-05

**关键词**：`analysis`、`therapy moderation`、`clinical false positive`、`algorithm audit`

👤 **作者**：Jiwon Kim、Claire Wang、Taeung Yoon、Sabelle Huang、Koustuv Saha

- 🎯 **研究动机**：通用内容审核护栏可能阻止 LLM 讨论敏感话题，影响其承担治疗角色的必要对话能力
- 🔬 **研究方法**：对 OpenAI moderation endpoint、Llama Guard 与 ShieldGemma 三个 SOTA 审核系统做算法审计，测其对真实治疗会谈内容的标记率
- 📌 **结论**：三系统均会把真实治疗对话标为不良内容，揭示通用内容过滤在临床场景的误报限制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly being used for emotional support. They are also being developed for formal therapy purposes. However, LLMs like ChaptGPT or Llama are often developed with content moderation guardrails that prevent them from discussing sensitive subjects with users for both liability and safety purposes, and this inability to broach these subjects may affect their capacity as therapists. In this study, we perform an algorithm audit on three state-of-the-art moderation systems (OpenAI's moderation endpoint, Meta's Llama Guard, and Google's Shield Gemma) to investigate the extent to which these systems flag the content of real-life therapy sessions as undesirable. Our results raise implications for the limitations that users and organizations may encounter when designing LLMs to play the part of a therapist.

</details>

### 7. CRADLE Bench: A Clinician-Annotated Benchmark for Multi-Faceted Mental Health Crisis and Safety Risk Detection

🎓 [Official](https://aclanthology.org/2026.eacl-long.73/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`crisis guardrail`、`clinical annotation`、`temporal risk`、`crisis detection`

👤 **作者**：Grace Byun、Rebecca Lipschutz、Sean T. Minton、Abigail Powers、Jinho D. Choi

- 🎯 **研究动机**：自杀意念、强奸、家暴、虐童等心理健康危机检测对语言模型是关键但探索不足的挑战，且现有工作覆盖危机类型有限
- 🔬 **研究方法**：CRADLE Bench 按临床标准覆盖七类危机并首次引入时间标签：600 条临床医生标注评测例、420 条开发例与约 4K 条多 LLM 多数投票自动标注训练语料，并按不同一致性标准微调六个检测模型
- 📌 **结论**：集成标注显著优于单模型标注，提供不同一致性标准下的互补危机检测模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting mental health crisis situations such as suicide ideation, rape, domestic violence, child abuse, and sexual harassment is a critical yet underexplored challenge for language models. When such situations arise during user–model interactions, models must reliably flag them, as failure to do so can have serious consequences. In this work, we introduce CRADLE BENCH, a benchmark for multi-faceted crisis detection. Unlike previous efforts that focus on a limited set of crisis types, our benchmark covers seven types defined in line with clinical standards and is the first to incorporate temporal labels. Our benchmark provides 600 clinician-annotated evaluation examples and 420 development examples, together with a training corpus of around 4K examples automatically labeled using a majority-vote ensemble of multiple language models, which significantly outperforms single-model annotation. We further fine-tune six crisis detection models on subsets defined by consensus and unanimous ensemble agreement, providing complementary models trained under different agreement criteria.Content warning: This paper discusses sensitive topics such as suicide ideation, self-harm, rape, domestic violence, and child abuse.

</details>

### 8. ExpGuard: LLM Content Moderation in Specialized Domains

📄 [arXiv](https://arxiv.org/abs/2603.02588) · 📝 [OpenReview](https://openreview.net/forum?id=t5cYJlV6aJ) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007009)　📅 2026-03　🏷 ICLR 2026

**关键词**：`defense`、`domain-specific moderation`、`expert annotation`、`adversarial jargon`

👤 **作者**：Minseok Choi、…、Jungmin Son

- 🎯 **研究动机**：现有护栏面向通用交互，在金融、医疗、法律等专业术语与对抗内容上脆弱
- 🔬 **研究方法**：构建 58,928 条提示-响应对的 ExpGuardMix（含领域专家标注测试集），训练专用护栏 ExpGuard
- 📌 **结论**：在专家测试集与 8 个公开基准全面领先，prompt 分类超 WildGuard 8.9%、response 分类超 15.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing deployment of large language models (LLMs) in real-world applications, establishing robust safety guardrails to moderate their inputs and outputs has become essential to ensure adherence to safety policies. Current guardrail models predominantly address general human-LLM interactions, rendering LLMs vulnerable to harmful and adversarial content within domain-specific contexts, particularly those rich in technical jargon and specialized concepts. To address this limitation, we introduce ExpGuard, a robust and specialized guardrail model designed to protect against harmful prompts and responses across financial, medical, and legal domains. In addition, we present ExpGuardMix, a meticulously curated dataset comprising 58,928 labeled prompts paired with corresponding refusal and compliant responses, from these specific sectors. This dataset is divided into two subsets: ExpGuardTrain, for model training, and ExpGuardTest, a high-quality test set annotated by domain experts to evaluate model robustness against technical and domain-specific content. Comprehensive evaluations conducted on ExpGuardTest and eight established public benchmarks reveal that ExpGuard delivers competitive performance across the board while demonstrating exceptional resilience to domain-specific adversarial attacks, surpassing state-of-the-art models such as WildGuard by up to 8.9% in prompt classification and 15.3% in response classification. To encourage further research and development, we open-source our code, data, and model, enabling adaptation to additional domains and supporting the creation of increasingly robust guardrail models.

</details>

### 9. SafeCRS: Personalized Safety Alignment for LLM-Based Conversational Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2603.03536) · 🌐 [Project](https://doi.org/10.1145/3770855.3817807)　📅 2026-03　🏷 KDD 2026

**关键词**：`defense`、`personalized safety`、`conversational recommender`、`safe RL`

👤 **作者**：Haochang Hao、Yifan Xu、Xinzhuo Li、Yingqiang Ge、Lu Cheng

- 🎯 **研究动机**：对话推荐系统会从对话中隐式推断创伤触发、自伤史等个性化安全敏感，却不在推荐时尊重
- 🔬 **研究方法**：提出 SafeRec 基准与 SafeCRS 框架，联合 Safe-SFT 与组奖励解耦归一化的 Safe-GDPO 优化推荐质量与个性化安全
- 📌 **结论**：相对最强推荐质量基线，安全违规率最多降 96.5% 且保持有竞争力的推荐质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM-based conversational recommender systems (CRS) primarily optimize recommendation accuracy and user satisfaction. We identify an underexplored vulnerability in which recommendation outputs may negatively impact users by violating personalized safety constraints, when individualized safety sensitivities -- such as trauma triggers, self-harm history, or phobias -- are implicitly inferred from the conversation but not respected during recommendation. We formalize this challenge as personalized CRS safety and introduce SafeRec, a new benchmark dataset designed to systematically evaluate safety risks in LLM-based CRS under user-specific constraints. To further address this problem, we propose SafeCRS, a safety-aware training framework that integrates Safe Supervised Fine-Tuning (Safe-SFT) with Safe Group reward-Decoupled Normalization Policy Optimization (Safe-GDPO) to jointly optimize recommendation quality and personalized safety alignment. Extensive experiments on SafeRec demonstrate that SafeCRS reduces safety violation rates by up to 96.5% relative to the strongest recommendation-quality baseline while maintaining competitive recommendation quality. Warning: This paper contains potentially harmful and offensive content.

</details>

### 10. BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards

📄 [arXiv](https://arxiv.org/abs/2602.18193) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40914)　📅 2026-02　🏷 AAAI 2026

**关键词**：`defense`、`ad compliance`、`multimodal mismatch`、`policy reward`

👤 **作者**：Yiran Yang、…、Jiefei Zhang

- 🎯 **研究动机**：短视频商业广告的夸大视觉、语音与字幕错配超出社区安全类目的覆盖，需策略驱动的细粒度审核
- 🔬 **研究方法**：BLM-Guard 融合 CoT 推理、规则策略原则与批评引导奖励；规则驱动 ICoT 数据合成降低标注成本，多任务架构建模模态内操纵与跨模态错配
- 📌 **结论**：在真实短视频广告上准确率、一致性与泛化均超越强基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Short-video platforms now host vast multimodal ads whose deceptive visuals, speech and subtitles demand finer-grained, policy-driven moderation than community safety filters. We present BLM-Guard, a content-audit framework for commercial ads that fuses Chain-of-Thought reasoning with rule-based policy principles and a critic-guided reward. A rule-driven ICoT data-synthesis pipeline jump-starts training by generating structured scene descriptions, reasoning chains and labels, cutting annotation costs. Reinforcement learning then refines the model using a composite reward balancing causal coherence with policy adherence. A multitask architecture models intra-modal manipulations (e.g., exaggerated imagery) and cross-modal mismatches (e.g., subtitle-speech drift), boosting robustness. Experiments on real short-video ads show BLM-Guard surpasses strong baselines in accuracy, consistency and generalization.

</details>

### 11. MindGuard: Guardrail Classifiers for Multi-Turn Mental Health Support

📄 [arXiv](https://arxiv.org/abs/2602.00950) · 🤗 [Model](https://huggingface.co/swordhealth/MindGuard-8B)　📅 2026-02

**关键词**：`defense`、`mental-health guard`、`clinical taxonomy`、`multi-turn crisis`

👤 **作者**：António Farinhas、…、Ricardo Rei

- 🎯 **研究动机**：通用安全 guard 难以区分心理支持中的治疗性披露与真实临床危机
- 🔬 **研究方法**：与心理学博士合作建立可行动危害 taxonomy，发布轮级临床专家标注测试集，并用双 agent 受控合成对话训练 4B/8B 轻量分类器 MindGuard
- 📌 **结论**：高召回工作点下误报更低，与临床 LLM 配对可在对抗性多轮交互中降低攻击成功率与有害接触率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly used for mental health support, yet their conversational coherence alone does not ensure clinical appropriateness. Existing general-purpose safeguards often fail to distinguish between therapeutic disclosures and genuine clinical crises, leading to safety failures. To address this gap, we introduce a clinically grounded risk taxonomy, developed in collaboration with PhD-level psychologists, that identifies actionable harm (e.g., self-harm and harm to others) while preserving space for safe, non-crisis therapeutic content. We release MindGuard-testset, a dataset of real-world multi-turn conversations annotated at the turn level by clinical experts. Using synthetic dialogues generated via a controlled two-agent setup, we train MindGuard, a family of lightweight safety classifiers (with 4B and 8B parameters). Our classifiers reduce false positives at high-recall operating points and, when paired with clinician language models, help achieve lower attack success and harmful engagement rates in adversarial multi-turn interactions compared to general-purpose safeguards. We release all models and human evaluation data.

</details>

### 12. ToxiTwitch: Toward Emote-Aware Hybrid Moderation for Live Streaming Platforms

📄 [arXiv](https://arxiv.org/abs/2601.15605)　📅 2026-01

**关键词**：`detection`、`live-chat moderation`、`emote-aware representation`、`hybrid classifier`

👤 **作者**：Baktash Ansari、Elias Martin、Afra Mashhadi

- 🎯 **研究动机**：Twitch 直播聊天量大且富含 emote，人类审核难以扩展
- 🔬 **研究方法**：ToxiTwitch 把聊天文本与 emote 的 LLM 嵌入结合 Random Forest 与 SVM 等传统分类器做混合毒性检测
- 📌 **结论**：频道内训练下准确率最高 80%、较 BERT 提升 13 个百分点、F1 达 76%，证实 emote 信息可改善毒性检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of live-streaming platforms such as Twitch has introduced complex challenges in moderating toxic behavior. Traditional moderation approaches, such as human annotation and keyword-based filtering, have demonstrated utility, but human moderators on Twitch constantly struggle to scale effectively in the fast-paced, high-volume, and context-rich chat environment of the platform while also facing harassment themselves. Recent advances in large language models (LLMs), such as DeepSeek-R1-Distill and Llama-3-8B-Instruct, offer new opportunities for toxicity detection, especially in understanding nuanced, multimodal communication involving emotes. In this work, we present an exploratory comparison of toxicity detection approaches tailored to Twitch. Our analysis reveals that incorporating emotes improves the detection of toxic behavior. To this end, we introduce ToxiTwitch, a hybrid model that combines LLM-generated embeddings of text and emotes with traditional machine learning classifiers, including Random Forest and SVM. In our case study, the proposed hybrid approach reaches up to 80 percent accuracy under channel-specific training (with 13 percent improvement over BERT and F1-score of 76 percent). This work is an exploratory study intended to surface challenges and limits of emote-aware toxicity detection on Twitch.

</details>

### 13. Qwerty AI: Explainable Automated Age Rating and Content Safety Assessment for Russian-Language Screenplays

📄 [arXiv](https://arxiv.org/abs/2601.04211)　📅 2025-12

**关键词**：`tool`、`Russian screenplay`、`age rating`、`explainable moderation`

👤 **作者**：Nikita Zmanovskii

- 🎯 **研究动机**：俄语剧本按 436-FZ 法规做年龄分级与内容安全审核亟需自动化工具
- 🔬 **研究方法**：基于 4-bit 量化的 Phi-3-mini 微调，切分叙事单元、检测五类内容违规并给出可解释分级理由；全程本地运行，无外部 API、80GB VRAM、平均脚本 5 分钟内完成
- 📌 **结论**：分级准确率 80%、切分精度 80-95%，700 页剧本处理不到 2 分钟，满足生产约束

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present Qwerty AI, an end-to-end system for automated age-rating and content-safety assessment of Russian-language screenplays according to Federal Law No. 436-FZ. The system processes full-length scripts (up to 700 pages in under 2 minutes), segments them into narrative units, detects content violations across five categories (violence, sexual content, profanity, substances, frightening elements), and assigns age ratings (0+, 6+, 12+, 16+, 18+) with explainable justifications. Our implementation leverages a fine-tuned Phi-3-mini model with 4-bit quantization, achieving 80% rating accuracy and 80-95% segmentation precision (format-dependent). The system was developed under strict constraints: no external API calls, 80GB VRAM limit, and <5 minute processing time for average scripts. Deployed on Yandex Cloud with CUDA acceleration, Qwerty AI demonstrates practical applicability for production workflows. We achieved these results during the Wink hackathon (November 2025), where our solution addressed real editorial challenges in the Russian media industry.

</details>

### 14. An AI-Based Behavioral Health Safety Filter and Dataset for Identifying Mental Health Crises in Text-Based Conversations

📄 [arXiv](https://arxiv.org/abs/2510.12083)　📅 2025-10

**关键词**：`defense`、`behavioral-health filter`、`clinician annotation`、`crisis detection`

👤 **作者**：Benjamin W. Nelson、…、Andrew Trister

- 🎯 **研究动机**：LLM 常误处理精神科急症给出有害建议，通用内容审核 guardrail 对心理危机检测并不可靠
- 🔬 **研究方法**：在 1800 条临床标注模拟消息的 Verily 数据集与 794 条 Aegis 心理健康子集上评估 VBHSF，对比 OpenAI Omni Moderation 与 NVIDIA NeMo Guardrails
- 📌 **结论**：VBHSF 检测任意危机 sensitivity 0.990、specificity 0.992，全面优于两者，而开源 guardrail 部分类别 sensitivity 低于 0.10

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models often mishandle psychiatric emergencies, offering harmful or inappropriate advice and enabling destructive behaviors. This study evaluated the Verily behavioral health safety filter (VBHSF) on two datasets: the Verily Mental Health Crisis Dataset containing 1,800 simulated messages and the NVIDIA Aegis AI Content Safety Dataset subsetted to 794 mental health-related messages. The two datasets were clinician-labelled and we evaluated performance using the clinician labels. Additionally, we carried out comparative performance analyses against two open source, content moderation guardrails: OpenAI Omni Moderation Latest and NVIDIA NeMo Guardrails. The VBHSF demonstrated, well-balanced performance on the Verily Mental Health Crisis Dataset v1.0, achieving high sensitivity (0.990) and specificity (0.992) in detecting any mental health crises. It achieved an F1-score of 0.939, sensitivity ranged from 0.917-0.992, and specificity was >= 0.978 in identifying specific crisis categories. When evaluated against the NVIDIA Aegis AI Content Safety Dataset 2.0, VBHSF performance remained highly sensitive (0.982) and accuracy (0.921) with reduced specificity (0.859). When compared with the NVIDIA NeMo and OpenAI Omni Moderation Latest guardrails, the VBHSF demonstrated superior performance metrics across both datasets, achieving significantly higher sensitivity in all cases (all p < 0.001) and higher specificity relative to NVIDIA NeMo (p < 0.001), but not to OpenAI Omni Moderation Latest (p = 0.094). NVIDIA NeMo and OpenAI Omni Moderation Latest exhibited inconsistent performance across specific crisis types, with sensitivity for some categories falling below 0.10. Overall, the VBHSF demonstrated robust, generalizable performance that prioritizes sensitivity to minimize missed crises, a crucial feature for healthcare applications.

</details>

### 15. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

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

### 16. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

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

### 17. When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha

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

### 18. CR4T: Rewrite-Based Guardrails for Adolescent LLM Safety

📄 [arXiv](https://arxiv.org/abs/2605.21609)　📅 2026-05

**关键词**：`defense`、`adolescent safety`、`response rewriting`、`developmental alignment`

👤 **作者**：Heajun An、Qi Zhang、Vedanth Achanta、Jin-Hee Cho

- 🎯 **研究动机**：现有安全机制以成人规范为中心、靠拒答压制，对青少年造成对话死胡同并忽略发展脆弱性
- 🔬 **研究方法**：CR4T 模型无关框架：轻量风险检测选择介入点，领域条件重写把不安全或拒答式输出重构为年龄适当、指导导向的回答
- 📌 **结论**：定向重写显著减少不安全与拒答式结果，且避免对可接受交互的不必要干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly embedded in adolescent digital environments, mediating information seeking, advice, and emotionally sensitive interactions. Yet existing safety mechanisms remain largely grounded in adult-centric norms and operationalize safety through refusal-oriented suppression. While such approaches may reduce immediate policy violations, they can also create conversational dead-ends, limit constructive guidance, and fail to address the developmental vulnerabilities inherent in adolescent-AI interactions. We argue that adolescent LLM safety should be framed not solely as a filtering problem, but as a socio-technical, developmentally aligned transformation problem. To operationalize this perspective, we propose Critique-and-Revise-for-Teenagers (CR4T), a model-agnostic safeguarding framework that selectively reconstructs unsafe or refusal-style outputs into ageappropriate, guidance-oriented responses while preserving benign intent. CR4T combines lightweight risk detection with domain-conditioned rewriting to remove risk-amplifying content, reduce unnecessary conversational shutdown, and introduce developmentally appropriate guidance. Experimental results show that targeted rewriting substantially reduces unsafe and refusal-oriented outcomes while avoiding unnecessary intervention on acceptable interactions. These findings suggest that selective response reconstruction offers a more human-centered alternative to refusal-centric guardrails for adolescent-facing LLM systems.

</details>

### 19. The Age of Curiosity Meets the Age of AI: Benchmarking Child Safety in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.25510) · 🤗 [Model](https://huggingface.co/collections/sameearif/kidbench)　📅 2026-05

**关键词**：`benchmark`、`child-facing safety`、`age cues`、`multi-turn degradation`

👤 **作者**：Samee Arif、Angana Borah、Rada Mihalcea

- 🎯 **研究动机**：现有安全评测聚焦通用有害内容，不针对 7-11 岁儿童的发展阶段适当性
- 🔬 **研究方法**：KIDBench 以发展心理学为底座的 LLM-as-a-Judge 量表，十类儿童查询、单轮与多轮 child-actor 模拟，比较无线索、隐式线索与显式年龄指令三种条件
- 📌 **结论**：隐式线索提分 8.6-46.8%、显式年龄再提 9.9-30.4%；跨语言文化不均衡，多轮模拟质量最多掉 0.959 分（1-5 量表）；附 KIDGuardLlama 评估器与 KIDLlama 儿童安全模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Children increasingly have access to Large Language Models (LLMs), which may expose them to responses that are developmentally inappropriate or require age-sensitive safety, guidance, and boundaries. Existing LLM safety evaluations largely focus on general harmful-content avoidance and do not explicitly target child-facing safety. We introduce KIDBench, a benchmark for evaluating child-facing LLM safety for ages 7-11 using a LLM-as-a-Judge rubric grounded in developmental-psychology. KIDBench contains realistic child queries across ten categories, with single-turn prompts and multi-turn child-actor simulations. We compare no-cues prompts with no child context, implicit-cues prompts that suggest a child speaker, and explicit age instructions. Implicit-cues improve scores by 8.6-46.8% over no-cue, while explicit age provides an additional 9.9-30.4% improvement over implicit-cues. Cross-lingual and cultural evaluations show uneven safety behavior across languages and country contexts. Multi-turn simulations show peak quality drops of up to 0.959 points on the 1-5 scale. We also introduce KIDGuardLlama, a child-safety evaluator, and KIDLlama, a child-safe response model. Code, data, and evaluation resources are available at https://github.com/MichiganNLP/kidbench.

</details>

### 20. KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety

📄 [arXiv](https://arxiv.org/abs/2603.16181)　📅 2026-03

**关键词**：`defense`、`child-safety moderation`、`OCR reasoning`、`two-stage routing`、`visual screening`

👤 **作者**：Viraj Panchal、Tanmay Talsaniya、Parag Patel、Meet Patel

- 🎯 **研究动机**：儿童安全内容审核需同时覆盖嵌入文本威胁并保持低延迟
- 🔬 **研究方法**：KidsNanny 两阶段管线：ViT 加目标检测做视觉筛查（11.7ms），以文本而非原始像素路由到 OCR 加 7B 语言模型做上下文推理（全程 120ms）
- 📌 **结论**：UnsafeBench 上准确率 81.40%、F1 86.16%，远快于 ShieldGemma-2（1,136ms）与 LlavaGuard（4,138ms）；纯文本子集 recall 达 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present KidsNanny, a two-stage multimodal content moderation architecture for child safety. Stage 1 combines a vision transformer (ViT) with an object detector for visual screening (11.7 ms); outputs are routed as text not raw pixels to Stage 2, which applies OCR and a text based 7B language model for contextual reasoning (120 ms total pipeline). We evaluate on the UnsafeBench Sexual category (1,054 images) under two regimes: vision-only, isolating Stage 1, and multimodal, evaluating the full Stage 1+2 pipeline. Stage 1 achieves 80.27% accuracy and 85.39% F1 at 11.7 ms; vision-only baselines range from 59.01% to 77.04% accuracy. The full pipeline achieves 81.40% accuracy and 86.16% F1 at 120 ms, compared to ShieldGemma-2 (64.80% accuracy, 1,136 ms) and LlavaGuard (80.36% accuracy, 4,138 ms). To evaluate text-awareness, we filter two subsets: a text+visual subset (257 images) and a text-only subset (44 images where safety depends primarily on embedded text). On text-only images, KidsNanny achieves 100% recall (25/25 positives; small sample) and 75.76% precision; ShieldGemma-2 achieves 84% recall and 60% precision at 1,136 ms. Results suggest that dedicated OCR-based reasoning may offer recall-precision advantages on text-embedded threats at lower latency, though the small text-only subset limits generalizability. By documenting this architecture and evaluation methodology, we aim to contribute to the broader research effort on efficient multimodal content moderation for child safety.

</details>

### 21. Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges

📄 [arXiv](https://arxiv.org/abs/2609.01210)　📅 2026-09

**关键词**：`benchmark`、`Chinese safety`、`safety judge`、`adversarial transformation`

👤 **作者**：Rui Yang、…、Jing Shao

- 🎯 **研究动机**：中文安全评测多评 query 风险而非 response 是否违规，语言变体与对抗变换会遮蔽风险意图
- 🔬 **研究方法**：构建 C-SafeQA：538 个基础查询加 8,877 个对抗查询，由四个 LLM 生成 37,660 条 query-response 记录，经多模型裁决与专家盲审标注，并同时评测七个自动安全 judge
- 📌 **结论**：对抗查询下不安全回复率升至 11.68%-30.05%；七个 judge 在 recall 与误报间各有取舍、无一全面占优，藏头诗变换令全部 judge 的不安全 recall 下降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety benchmarks for large language models often assess the risk of a user query, although the outcome of question answering depends on whether the response violates a policy. This distinction is critical in Chinese harmful-content evaluation, where linguistic variation and adversarial transformations can obscure risky intent. We introduce C-SafeQA, a policy-grounded benchmark for response-level Chinese safety evaluation. It comprises 538 base queries and 8,877 adversarial queries answered by four full-model LLM deployments, yielding 37,660 query-response records labeled safe, unsafe, or disputed. Reference labels are generated through agreement-aware multi-model adjudication and blind audits of stratified subsets by three safety experts. C-SafeQA supports both evaluation of target-model safety and auditing of seven automated safety judges against shared reference labels. Unsafe-response rates range from 0.93% to 3.35% on base queries and from 11.68% to 30.05% on adversarial queries. On the adversarial subset, judges show substantial trade-offs between unsafe-response recall and risk-query-conditioned safe-response false positive rate, and no judge dominates all metrics. Both acrostic transformations reduce unsafe recall for all seven judges, revealing mechanism-specific evaluator weaknesses. Dataset records, metadata, verification code, and judge scripts are publicly released to support recomputation, while benchmark construction, target-response generation, and private adjudication remain outside the release boundary.

</details>

### 22. HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation

📄 [arXiv](https://arxiv.org/abs/2609.01046) · 🤗 [Model](https://huggingface.co/hivetrace/HiveTraceGuard-Pro)　📅 2026-09

**关键词**：`defense`、`compact guard`、`multilingual deployment`、`prompt injection`、`multilingual guardrail`、`Russian prompt injection`

👤 **作者**：Nikita Oblakov、Sabrina Sadiekh、Evgeniy Kokuykin

- 🎯 **研究动机**：生产 guardrail 需低延迟，而俄语 prompt injection 与表面混淆的证据严重不足
- 🔬 **研究方法**：提出从 Qwen3-0.6B LoRA 微调的 0.6B 生成式护栏 HiveTraceGuard-Pro，英俄双语训练、单条 safe/unsafe 评分规则、八种混淆变换增强
- 📌 **结论**：15 模型比较中俄语 clean robustness 组合 F1 最高（0.88）、俄语注入 recall 0.999、中位延迟 14.3ms 最低；但套件 FPR 0.268，且注入集至少 27.1% 与训练语料重叠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its training corpus pairs harmful examples, where a counterpart exists, with benign examples from the same domain and applies eight obfuscation transforms to both labels. In one harness, we compare HiveTraceGuard-Pro with thirty-four other guards on nineteen benchmark groups, sixteen of which are public. Its aggregate key is 0.7432, behind 0.7641 and 0.7552 for the two higher-scoring guards. Over the sixteen public groups alone, its key is 0.7153 and four of the thirty-four other suite guards score higher. In a fifteen-model comparison, HiveTraceGuard-Pro has the highest clean Russian robustness combined-F1 (0.88) and Russian prompt-injection recall (0.999). Both results use Russian sets assembled by our team, and at least 27.1% of the prompt-injection set overlaps the training corpus. Its 14.3 ms median latency is the lowest among those fifteen models in that run. Across the suite, FPR is 0.268 and FNR is 0.156. All reported response results use a legacy standalone-reply serialization rather than the natural assistant-role path of the shipped chat template. We release the merged weights on Hugging Face under Apache-2.0. The corpus, evaluation sets and evaluation code remain internal.

</details>

### 23. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

📄 [arXiv](https://arxiv.org/abs/2608.27548) · 🤗 [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · 📊 [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset)　📅 2026-08

**关键词**：`tool`、`compact guard model`、`prompt-response moderation`、`production deployment`、`multimodal moderator`、`image-conditioned safety`

👤 **作者**：Varun Singh、Anuj Doshi、Makesh Narsimhan Sreedhar、Shaona Ghosh、Katherine Luna

- 🎯 **研究动机**：部署场景的安全审核需覆盖图像、文档、生成回答与各域自定义策略，现有 guardrail 通常只覆盖部分设置，难以兼顾广覆盖、自定义策略与低算力
- 🔬 **研究方法**：发布 4B 视觉语言安全 moderator Nemotron 3.5 CS 及多模态多语言安全数据集，联合分类 12 种语言的 prompt、图像与回答；低延迟路径仅输出标签，按需生成应用自定义策略并指认违规类别的推理轨迹
- 📌 **结论**：在多模态安全、文本审核、跨语言鲁棒性、自定义策略遵循、良性误报与延迟评测中取得实用的覆盖—成本权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

</details>

### 24. IndicGuard: A Multilingual Safety Guard Model and Dataset for Indic Languages

📄 [arXiv](https://arxiv.org/abs/2606.22841)　📅 2026-06

**关键词**：`defense`、`Indic languages`、`regional harm`、`cross-lingual transfer`

👤 **作者**：Parth Bramhecha、Smit Deshmukh、Sairaj Bodhale、Adwait Borate、Raviraj Joshi

- 🎯 **研究动机**：现有安全机制以英语为中心，难以捕捉 Indic 地区的区域伤害类别与社会文化敏感
- 🔬 **研究方法**：构建覆盖十种主要 Indic 语言的 culturally nuanced 安全数据集（含区域伤害、社会政治语境与越狱），微调 Gemma-3-4B-IT 成多语护栏
- 📌 **结论**：显著增强本地化漏洞鲁棒性，各语言一致超过 CultureGuard，并泛化到未训练的低资源 Indic 语言

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) achieve widespread integration across diverse linguistic landscapes, ensuring their safety and alignment with regional normative values remains a critical challenge. Current safety mechanisms are predominantly optimized for English-centric frameworks, often failing to capture the unique socio-cultural sensitivities and localized categories of harm inherent to the Indic region. To address this gap, we introduce IndicGuard, a multilingual safety guard model and dataset for Indic languages. We construct a high-volume, culturally nuanced safety dataset encompassing ten major Indic languages, systematically curated to capture regional harms, sensitive socio-political contexts, and adversarial jailbreaks. Leveraging this corpus, we fine-tune a 4B-parameter instruction-tuned model based on Gemma-3-4B-IT to serve as a multilingual safety guardrail for real-time content moderation and policy compliance checking. Our empirical evaluations demonstrate that IndicGuard significantly enhances LLM robustness against localized vulnerabilities, achieving high moderation consistency across different conversational turns. Crucially, IndicGuard consistently outperforms the existing baseline model, CultureGuard, across evaluated languages. Finally, we demonstrate that our model effectively generalizes to low-resource Indic languages excluded from training, substantiating the structural robustness and cross-lingual transfer capabilities of the framework.

</details>

### 25. CHILLGuard: Towards Fine-Grained Chinese LLM Safety Guardrail with Scalable Data Construction and Model-aware Preference Alignment

📄 [arXiv](https://arxiv.org/abs/2606.15396)　📅 2026-06

**关键词**：`defense`、`Chinese moderation`、`fine-grained taxonomy`、`preference alignment`

👤 **作者**：Wenbo Yu、…、Min Zhang

- 🎯 **研究动机**：现有护栏面向英文或多语场景，缺乏对中文监管政策、文化语境与语言细节的适配及细粒度风险分类
- 🔬 **研究方法**：定义 5 大类 31 小类中文风险分类法，经 RAG 扩充、提示改写隐式有害样本、多模型投票标注校准构建 405,007 训练样本与 51,745 测试样本，以 Model-aware DPO 训练 CHILLGuard
- 📌 **结论**：多设定下 SOTA，F1 比 Qwen3Guard-8B-Strict 高 15.92%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Malicious content generated from large language models (LLMs) could pose severe safety risks and ethical concerns. While existing LLM safety guardrails excel in English or multilingual settings, they lack adaptation to Chinese-specific regulatory policies, cultural context and linguistic nuances, failing to support fine-grained risk classification for diverse deployment needs. In this paper, we introduce a 5-macro, 31-micro category fine-grained risk taxonomy for Chinese scenarios, and build CHILLGuard: a dedicated Chinese LLM content safety guardrail. To address the critical scarcity of high-quality annotated Chinese safety data, we propose a scalable multi-stage data construction pipeline: we expand multi-source corpus via retrieval-augmented generation, generate implicit harmful samples through prompt engineering rewriting, and refine high-quality data via multi-model voting-based label calibration. Based on this, we build CHILLGuardTrain, a large-scale training set with 405,007 samples, and CHILLGuardTest, a rigorously curated annotated test set with 51,745 samples. We then train CHILLGuard on CHILLGuardTrain under a generator-classifier collaborative framework via Model-aware Direct Preference Optimization. Extensive experiments under multiple settings demonstrate the state-of-the-art performance of CHILLGuard, e.g., a 15.92% improvement of F1 score over Qwen3Guard-8B-Strict on our benchmark. We will release our resources at https://github.com/cswbyu/CHILLGuard.

</details>

### 26. Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities

📄 [arXiv](https://arxiv.org/abs/2606.13397) · 🌐 [Project](https://doi.org/10.1145/3811242.3819096)　📅 2026-06

**关键词**：`defense`、`minority-grounded moderation`、`RAG feedback`、`community co-design`

👤 **作者**：Dipto Das、…、Syed Ishtiaque Ahmed

- 🎯 **研究动机**：LLM 审核难以识别针对少数群体的文化不敏感言论（隐性抹除、误现、规范框定），其认知边界未知
- 🔬 **研究方法**：聚焦孟加拉国 Hindu 与 Chakma 社群，与社区成员共同构建文化敏感语料并经 RAG 注入审核管线，形成 Mod-Guide 反馈系统
- 📌 **结论**：RAG 增强的审核回应更贴合语境，少数与多数群体参与者的感知存在族群差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language operates as a mechanism of both marginalization and resistance, especially for minority communities navigating insensitive and harmful speech online. As content moderation increasingly depends on large language models (LLMs), concerns arise about whether these systems can recognize culturally insensitive speech-language that disregards or marginalizes the cultural and religious perspectives of historically underrepresented communities, often through implicit erasure, misrepresentation, or normative framing, rather than overt hostility. Focusing on Bangladesh's Hindu and Chakma communities -- the country's largest religious and Indigenous ethnic minorities, respectively -- this paper investigates the epistemic limits of LLM-based moderation systems and explores methods for incorporating minority perspectives. We co-created a culturally grounded corpus of insensitive speech with community members and integrated their narratives into moderation pipelines using retrieval augmented generation (RAG). Our tool, Mod-Guide, improves LLM sensitivity to minority viewpoints by leveraging contextual cues derived from lived experience. Through mixed-method evaluations involving both minority and majority participants, we demonstrate that RAG-enhanced moderation responses are more contextually accurate and perceived differently across ethnic lines. This work advances research in human-computer interaction, AI ethics, and social computing by foregrounding restorative justice and hermeneutical inclusion in the design of content moderation systems.

</details>

### 27. ML-Bench&Guard: Policy-Grounded Multilingual Safety Benchmark and Guardrail for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.00689)　📅 2026-05

**关键词**：`defense`、`regional regulation`、`multilingual policy`、`diffusion LLM`

👤 **作者**：Yunhan Zhao、Zhaorun Chen、Xingjun Ma、Yu-Gang Jiang、Bo Li

- 🎯 **研究动机**：多语言安全基准依赖通用风险 taxonomy 与机器翻译，护栏无法对齐地区法规与文化差异
- 🔬 **研究方法**：ML-Bench 直接从 14 语种地区法规提取风险类别与细粒度规则指导数据生成；ML-Guard 基于 dLLM，提供 1.5B 快速筛查与 7B 合规详析两个变体
- 📌 **结论**：在 6 个既有多语言基准与 ML-Bench 上对 11 个护栏基线全面领先

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) are increasingly deployed in cross-linguistic contexts, ensuring safety in diverse regulatory and cultural environments has become a critical challenge. However, existing multilingual benchmarks largely rely on general risk taxonomies and machine translation, which confines guardrail models to these predefined categories and hinders their ability to align with region-specific regulations and cultural nuances. To bridge these gaps, we introduce ML-Bench, a policy-grounded multilingual safety benchmark covering 14 languages. ML-Bench is constructed directly from regional regulations, where risk categories and fine-grained rules derived from jurisdiction-specific legal texts are directly used to guide the generation of multilingual safety data, enabling culturally and legally aligned evaluation across languages. Building on ML-Bench, we develop ML-Guard, a Diffusion Large Language Model (dLLM)-based guardrail model that supports multilingual safety judgment and policy-conditioned compliance assessment. ML-Guard has two variants, one 1.5B lightweight model for fast `safe/unsafe' checking and a more capable 7B model for customized compliance checking with detailed explanations. We conduct extensive experiments against 11 strong guardrail baselines across 6 existing multilingual safety benchmarks and our ML-Bench, and show that ML-Guard consistently outperforms prior methods. We hope that ML-Bench and ML-Guard can help advance the development of regulation-aware and culturally aligned multilingual guardrail systems.

</details>

### 28. TWGuard: A Case Study of LLM Safety Guardrails for Localized Linguistic Contexts

📄 [arXiv](https://arxiv.org/abs/2604.16542)　📅 2026-04

**关键词**：`defense`、`Taiwan localization`、`curated language data`、`false-positive reduction`

👤 **作者**：Hua-Rong Chu、Kuan-Chun Wang、Yao-Te Huang

- 🎯 **研究动机**：护栏研究忽略语言文化差异，报告性能与实际部署效果存在落差
- 🔬 **研究方法**：以台湾语言语境为例，用贴合本地语言特征的策划数据集优化护栏模型得到 TWGuard
- 📌 **结论**：F1 较基座提升 0.289，FPR 较最强基线降 0.037（降幅 94.9%），表明安全边界应由地区语料定义

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guardrails have become an active area of research in AI safety, aimed at ensuring the appropriate behavior of large language models (LLMs). However, existing research lacks consideration of nuances across linguistic and cultural contexts, resulting in a gap between reported performance and in-the-wild effectiveness. To address this issue, this paper proposes an approach to optimize guardrail models for a designated linguistic context by leveraging a curated dataset tailored to local linguistic characteristics, targeting the Taiwan linguistic context as a representative example of localized deployment challenges. The proposed approach yields TWGuard, a linguistic context-optimized guardrail model that achieves a huge gain (+0.289 in F1) compared to the foundation model and significantly outperforms the strongest baseline in practical use (-0.037 in false positive rate, a 94.9\% reduction). Together, this work lays a foundation for regional communities to establish AI safety standards grounded in their own linguistic contexts, rather than accepting boundaries imposed by dominant languages. The inadequacy of the latter is reconfirmed by our findings.

</details>

### 29. Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space

🎓 [Official](https://aclanthology.org/2026.eacl-long.139/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`activation guardrail`、`safety direction`、`multilingual monitoring`、`activation monitoring`

👤 **作者**：Andrea Ermellino、Lorenzo Malandri、Fabio Mercorio、Antonio Serino

- 🎯 **研究动机**：现有安全防护依赖侵入式微调或资源低效的生成式外部检查，缺乏对安全概念几何结构的机理刻画
- 🔬 **研究方法**：定位预训练表示中安全与不安全概念最大可分的层，在该层激活空间上仅用线性分类器实施安全判定，无需修改权重
- 📌 **结论**：安全分离由激活空间单一层的方向涌现，跨 8 个领域、3 类任务与 16 种非英语语言有效，比传统生成式护栏更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of Large Language Models (LLMs) is a critical alignment challenge. Existing approaches often rely on invasive fine- tuning or external generation-based checks, which can be opaque and resource-inefficient. In this work, we investigate the geometry of safety concepts within pretrained representations, proposing a mechanistic methodology that identifies the layer where safe and unsafe concepts are maximally separable within a pretrained model’s representation space. By leveraging the intrinsic activation space of the optimal layer, we show that safety enforcement can be achieved via a simple linear classifier, avoiding the need for weight modification. We validate our framework across multiple domains (regulation, law, finance, cybersecurity, education, code, human resources, and social media), diverse tasks (safety classification, prompt injection, and toxicity detection), and 16 non-English languages on both encoder and decoder architectures. Our results show that: (i) the separation between safe and unsafe concepts emerges from a single layer direction in the activation space, (ii) monitoring internal representations provides a significantly more robust safeguarding mechanism compared to traditional evaluative or generative guardrail paradigms.

</details>

### 30. FanarGuard: A Culturally-Aware Moderation Filter for Arabic Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.368/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`Arabic guardrail`、`cultural alignment`、`human annotation`、`Arabic moderation`、`harmlessness`

👤 **作者**：Masoomali Fatehkia、Enes Altinisik、Husrev Taha Sencar

- 🎯 **研究动机**：现有审核过滤器只关注通用安全、忽视文化语境，阿拉伯语场景尤其缺乏
- 🔬 **研究方法**：FanarGuard 双语过滤器：46.8 万余对阿英提示响应经 LLM 评委团按无害性与文化感知打分训练；并建首个阿拉伯文化语境基准（1K 余条规范敏感提示加人工标注）
- 📌 **结论**：与人类标注的一致性超过标注者间一致性，同时在安全基准上匹配 SOTA 过滤器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content moderation filters are a critical safeguard against alignment failures in language models. Yet most existing filters focus narrowly on general safety and overlook cultural context. In this work, we introduce FanarGuard, a bilingual moderation filter that evaluates both safety and cultural alignment in Arabic and English. We construct a dataset of over 468K prompt and response pairs, drawn from synthetic and public datasets, scored by a panel of LLM judges on harmlessness and cultural awareness, and use it to train two filter variants.To rigorously evaluate cultural alignment, we further develop the first benchmark targeting Arabic cultural contexts, comprising over 1K norm-sensitive prompts with LLM-generated responses annotated by human raters. Results show that FanarGuard achieves stronger agreement with human annotations than inter-annotator reliability, while matching the performance of state-of-the-art filters on safety benchmarks. These findings highlight the importance of integrating cultural awareness into moderation and establish FanarGuard as a practical step toward more context-sensitive safeguards.

</details>

### 31. Bielik Guard: Efficient Polish Language Safety Classifiers for LLM Content Moderation

📄 [arXiv](https://arxiv.org/abs/2602.07954) · 🤗 [Model](https://huggingface.co/collections/speakleash/bielik-guard)　📅 2026-02

**关键词**：`tool`、`Polish moderation`、`compact classifier`、`multi-label safety`

👤 **作者**：Krzysztof Wróbel、Jan Maria Kowalski、Jerzy Surma、Igor Ciuciura、Maciej Szymański

- 🎯 **研究动机**：波兰语 LLM 应用缺乏高效准确的内容安全分类器
- 🔬 **研究方法**：Bielik Guard 含 0.1B 与 0.5B 两个模型，在 6,885 条社区标注波兰语文本上微调，覆盖仇恨、粗俗、色情、犯罪、自伤五类
- 📌 **结论**：0.5B 版 F1 达 0.791/0.785；0.1B 版真实用户提示上 precision 77.65%、误报率仅 0.63%，远超同规模 HerBERT-PL-Guard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) become increasingly deployed in Polish language applications, the need for efficient and accurate content safety classifiers has become paramount. We present Bielik Guard, a family of compact Polish language safety classifiers comprising two model variants: a 0.1B parameter model based on MMLW-RoBERTa-base and a 0.5B parameter model based on PKOBP/polish-roberta-8k. Fine-tuned on a community-annotated dataset of 6,885 Polish texts, these models classify content across five safety categories: Hate/Aggression, Vulgarities, Sexual Content, Crime, and Self-Harm. Our evaluation demonstrates that both models achieve strong performance on multiple benchmarks. The 0.5B variant offers the best overall discrimination capability with F1 scores of 0.791 (micro) and 0.785 (macro) on the test set, while the 0.1B variant demonstrates exceptional efficiency. Notably, Bielik Guard 0.1B v1.1 achieves superior precision (77.65%) and very low false positive rate (0.63%) on real user prompts, outperforming HerBERT-PL-Guard (31.55% precision, 4.70% FPR) despite identical model size. The models are publicly available and designed to provide appropriate responses rather than simple content blocking, particularly for sensitive categories like self-harm.

</details>

### 32. SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia

📄 [arXiv](https://arxiv.org/abs/2602.01618) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.141/)　📅 2026-02　🏷 ACL 2026

**关键词**：`defense`、`Southeast Asian languages`、`agentic data generation`、`cultural safety`

👤 **作者**：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji、Trevor Cohn、Peerat Limkonchotiwat

- 🎯 **研究动机**：safeguard 模型依赖英文数据机翻，遗漏东南亚本地价值、规范与地区法规
- 🔬 **研究方法**：提出 agentic 数据生成框架规模化创建地区原生安全数据，并训练首个以 SEA 文化为接地的多语 safeguard 家族 SEA-Guard
- 📌 **结论**：在多基准与文化变体上持续优于现有 safeguard 检测地区敏感有害内容，同时保持通用安全性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Culturally aware safeguards are crucial for AI alignment in real-world settings, where safety extends beyond common sense and encompasses diverse local values, norms, and region-specific regulations. However, building large-scale, culturally grounded datasets is challenging due to limited resources and a scarcity of native annotators. Consequently, many safeguard models rely on machine translation of English datasets, often missing regional and cultural nuances. We present a novel agentic data-generation framework to scalably create authentic, region-specific safety datasets for Southeast Asia (SEA). On this foundation, we introduce the SEA-Guard family, the first multilingual safeguard models grounded in SEA cultural contexts. Evaluated across multiple benchmarks and cultural variants, SEA-Guard consistently outperforms existing safeguards at detecting regionally sensitive or harmful content while maintaining strong general safety performance.

</details>

### 33. CREST: Universal Safety Guardrails through Cluster-Guided Cross-Lingual Transfer

📄 [arXiv](https://arxiv.org/abs/2512.02711) · 🎓 [Official](https://aclanthology.org/2026.lrec-1.701/)　📅 2025-12

**关键词**：`defense`、`100-language guard`、`cluster transfer`、`parameter efficiency`

👤 **作者**：Lavish Bansal、Naman Mishra

- 🎯 **研究动机**：现有安全 guardrail 主要面向高资源语言，低资源语言使用者缺乏保护
- 🔬 **研究方法**：CREST 仅用 13 种高资源语言训练 0.5B 参数分类器，通过聚类引导的跨语言迁移泛化到 100 种语言
- 📌 **结论**：六个安全基准上超越同规模 SOTA guardrail，并可匹敌 2.5B 及以上参数模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring content safety in large language models (LLMs) is essential for their deployment in real-world applications. However, existing safety guardrails are predominantly tailored for high-resource languages, leaving a significant portion of the world's population underrepresented who communicate in low-resource languages. To address this, we introduce CREST (CRoss-lingual Efficient Safety Transfer), a parameter-efficient multilingual safety classification model that supports 100 languages with only 0.5B parameters. By training on a strategically chosen subset of only 13 high-resource languages, our model utilizes cluster-based cross-lingual transfer from a few to 100 languages, enabling effective generalization to both unseen high-resource and low-resource languages. This approach addresses the challenge of limited training data in low-resource settings. We conduct comprehensive evaluations across six safety benchmarks to demonstrate that CREST outperforms existing state-of-the-art guardrails of comparable scale and achieves competitive results against models with significantly larger parameter counts (2.5B parameters and above). Our findings highlight the limitations of language-specific guardrails and underscore the importance of developing universal, language-agnostic safety systems that can scale effectively to serve global populations.

</details>

### 34. CultureGuard: Towards Culturally-Aware Dataset and Guard Model for Multilingual Safety Applications

📄 [arXiv](https://arxiv.org/abs/2508.01710) · 📊 [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3)　📅 2025-08

**关键词**：`defense`、`cultural adaptation`、`nine-language dataset`、`cross-lingual transfer`

👤 **作者**：Raviraj Joshi、…、Niranjan Wartikar

- 🎯 **研究动机**：非英语语言缺乏文化对齐的安全标注数据，人工采集成本高昂
- 🔬 **研究方法**：提出四阶段合成管线（文化数据隔离、文化适配、机器翻译、质量过滤），把英语安全数据集扩展为 9 语言 386,661 样本并 LoRA 微调 8B 护栏模型
- 📌 **结论**：多个多语言安全基准达 SoTA，具备跨语言迁移与对未见语言的零样本泛化；最新开源 LLM 在非英语 prompt 下更不安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing use of Large Language Models (LLMs) in agentic applications highlights the need for robust safety guard models. While content safety in English is well-studied, non-English languages lack similar advancements due to the high cost of collecting culturally aligned labeled datasets. We present CultureGuard, a novel solution for curating culturally aligned, high-quality safety datasets across multiple languages. Our approach introduces a four-stage synthetic data generation and filtering pipeline: cultural data segregation, cultural data adaptation, machine translation, and quality filtering. This pipeline enables the conversion and expansion of the Nemotron-Content-Safety-Dataset-V2 English safety dataset into eight distinct languages: Arabic, German, Spanish, French, Hindi, Japanese, Thai, and Chinese. The resulting dataset, Nemotron-Safety-Guard-Dataset-v3, comprises 386,661 samples in 9 languages and facilitates the training of Llama-3.1-Nemotron-Safety-Guard-8B-v3 via LoRA-based fine-tuning. The final model achieves state-of-the-art performance on several multilingual content safety benchmarks. Furthermore, we show our moderately multilingual fine-tuning enables robust cross-lingual transfer and strong zero-shot generalization to unseen languages. We also benchmark the latest open LLMs on multilingual safety and observe that these LLMs are more prone to give unsafe responses when prompted in non-English languages. This work advances multilingual LLM safety by enabling the development of culturally aware safety guard models.

</details>

### 35. LionGuard 2: Building Lightweight, Data-Efficient & Localised Multilingual Content Moderators

📄 [arXiv](https://arxiv.org/abs/2507.15339) · 🎓 [Official](https://aclanthology.org/2025.emnlp-demos.20/)　📅 2025-07　🏷 EMNLP 2025

**关键词**：`tool`、`Singapore localization`、`ordinal classifier`、`production moderation`

👤 **作者**：Leanne Tan、Gabriel Chua、Ziyu Ge、Roy Ka-Wei Lee

- 🎯 **研究动机**：多语言审核系统忽视本地化与低资源语言变体，小模型方案仍需大量数据与算力
- 🔬 **研究方法**：提出 LionGuard 2：基于预训练 OpenAI 嵌入与多头序数分类器的轻量审核器，面向新加坡语境支持英中马及部分泰米尔语
- 📌 **结论**：17 个基准上超多个商业与开源系统，已在新加坡政府实际部署，证明高质量本地数据加多语言嵌入无需微调大模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern moderation systems increasingly support multiple languages, but often fail to address localisation and low-resource variants - creating safety gaps in real-world deployments. Small models offer a potential alternative to large LLMs, yet still demand considerable data and compute. We present LionGuard 2, a lightweight, multilingual moderation classifier tailored to the Singapore context, supporting English, Chinese, Malay, and partial Tamil. Built on pre-trained OpenAI embeddings and a multi-head ordinal classifier, LionGuard 2 outperforms several commercial and open-source systems across 17 benchmarks, including both Singapore-specific and public English datasets. The system is actively deployed within the Singapore Government, demonstrating practical efficacy at scale. Our findings show that high-quality local data and robust multilingual embeddings can achieve strong moderation performance, without fine-tuning large models. We release our model weights and part of our training data to support future work on LLM safety.

</details>

### 36. OMNIGUARD: An Efficient Approach for AI Safety Moderation Across Languages and Modalities

📄 [arXiv](https://arxiv.org/abs/2505.23856)　📅 2025-05

**关键词**：`defense`、`language-agnostic representation`、`modality-agnostic classifier`、`low-resource input`

👤 **作者**：Sahil Verma、…、Chandan Singh

- 🎯 **研究动机**：有害 prompt 检测在低资源语言与非文本模态上因能力错配而失效
- 🔬 **研究方法**：提出 OMNIGUARD，利用 LLM 与 MLLM 内部跨语言跨模态对齐的表示构建无关语言与模态的分类器，复用生成时嵌入
- 📌 **结论**：多语言准确率提升 11.57%、图像 20.44%，音频创新 SOTA，且比最快基线快约 120 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emerging capabilities of large language models (LLMs) have sparked concerns about their immediate potential for harmful misuse. The core approach to mitigate these concerns is the detection of harmful queries to the model. Current detection approaches are fallible, and are particularly susceptible to attacks that exploit mismatched generalization of model capabilities (e.g., prompts in low-resource languages or prompts provided in non-text modalities such as image and audio). To tackle this challenge, we propose Omniguard, an approach for detecting harmful prompts across languages and modalities. Our approach (i) identifies internal representations of an LLM/MLLM that are aligned across languages or modalities and then (ii) uses them to build a language-agnostic or modality-agnostic classifier for detecting harmful prompts. Omniguard improves harmful prompt classification accuracy by 11.57\% over the strongest baseline in a multilingual setting, by 20.44\% for image-based prompts, and sets a new SOTA for audio-based prompts. By repurposing embeddings computed during generation, Omniguard is also very efficient ($\approx\!120 \times$ faster than the next fastest baseline). Code and data are available at: https://github.com/vsahil/OmniGuard.

</details>

### 37. MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety

📄 [arXiv](https://arxiv.org/abs/2504.15241) · 🎓 [Official](https://aclanthology.org/2025.emnlp-main.1392/)　📅 2025-04　🏷 EMNLP 2025

**关键词**：`defense`、`multilingual reasoning`、`curriculum GRPO`、`code-switching`

👤 **作者**：Yahan Yang、Soham Dan、Shuo Li、Dan Roth、Insup Lee

- 🎯 **研究动机**：多语言安全对齐数据稀缺，越狱在多语言场景更严重，需要跨语言推理式护栏
- 🔬 **研究方法**：提出 MrGuard，经合成多语言数据、SFT 与课程式 GRPO 训练带推理的 prompt 分类护栏
- 📌 **结论**：域内外语言上超基线 15% 以上，在 code-switching 与低资源语言干扰下保持安全判断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are susceptible to adversarial attacks such as jailbreaking, which can elicit harmful or unsafe behaviors. This vulnerability is exacerbated in multilingual settings, where multilingual safety-aligned data is often limited. Thus, developing a guardrail capable of detecting and filtering unsafe content across diverse languages is critical for deploying LLMs in real-world applications. In this work, we introduce a multilingual guardrail with reasoning for prompt classification. Our method consists of: (1) synthetic multilingual data generation incorporating culturally and linguistically nuanced variants, (2) supervised fine-tuning, and (3) a curriculum-based Group Relative Policy Optimization (GRPO) framework that further improves performance. Experimental results demonstrate that our multilingual guardrail, MrGuard, consistently outperforms recent baselines across both in-domain and out-of-domain languages by more than 15%. We also evaluate MrGuard's robustness to multilingual variations, such as code-switching and low-resource language distractors in the prompt, and demonstrate that it preserves safety judgments under these challenging conditions. The multilingual reasoning capability of our guardrail enables it to generate explanations, which are particularly useful for understanding language-specific risks and ambiguities in multilingual content moderation.

</details>

### 38. PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages

📄 [arXiv](https://arxiv.org/abs/2504.04377) · 📝 [OpenReview](https://openreview.net/forum?id=wbAWKXNeQ4)　📅 2025-04　🏷 COLM 2025

**关键词**：`tool`、`17-language moderation`、`PolyGuardMix`、`prompt-response labeling`

👤 **作者**：Priyanshu Kumar、…、Maarten Sap

- 🎯 **研究动机**：多语言安全审核长期聚焦少数语言、安全定义狭窄，能力缺口大
- 🔬 **研究方法**：发布 PolyGuard 与 1.91M 样本、17 语言的 PolyGuardMix 训练语料及 29K 的 PolyGuardPrompts 评测基准
- 📌 **结论**：在多个安全与毒性基准上超过现有开源及商业安全分类器 5.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Truly multilingual safety moderation efforts for Large Language Models (LLMs) have been hindered by a narrow focus on a small set of languages (e.g., English, Chinese) as well as a limited scope of safety definition, resulting in significant gaps in moderation capabilities. To bridge these gaps, we release POLYGUARD, a new state-of-the-art multilingual safety model for safeguarding LLM generations, and the corresponding training and evaluation datasets. POLYGUARD is trained on POLYGUARDMIX, the largest multilingual safety training corpus to date containing 1.91M samples across 17 languages (e.g., Chinese, Czech, English, Hindi). We also introduce POLYGUARDPROMPTS, a high quality multilingual benchmark with 29K samples for the evaluation of safety guardrails. Created by combining naturally occurring multilingual human-LLM interactions and human-verified machine translations of an English-only safety dataset (WildGuardMix; Han et al., 2024), our datasets contain prompt-output pairs with labels of prompt harmfulness, response harmfulness, and response refusal. Through extensive evaluations across multiple safety and toxicity benchmarks, we demonstrate that POLYGUARD outperforms existing state-of-the-art open-weight and commercial safety classifiers by 5.5%. Our contributions advance efforts toward safer multilingual LLMs for all global users.

</details>

### 39. IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2609.03781)　📅 2026-09

**关键词**：`benchmark`、`Indic languages`、`persuasive jailbreak`、`cross-lingual safety`、`multilingual jailbreak`、`persuasive attack`

👤 **作者**：Saikat Mondal、Mamta、Deeksha Varshney、Oana Cocarascu、Asif Ekbal

- 🎯 **研究动机**：LLM 安全评测仍以英语为主，低资源与文化多样语言中的对齐失效形态不明
- 🔬 **研究方法**：构建 IndicSafeEval：四种印度语言（Hindi、Bengali、Marathi、Punjabi）×十个安全关键类别×六种类人说服策略，共 7,200 个对抗 prompt，对开源 LLM 做系统黑盒评测
- 📌 **结论**：安全性强烈依赖语言与说服式措辞，不同风险类别脆弱度差异显著——英语中心的安全评测存在系统性盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used in multilingual settings, yet their safety is still evaluated primarily in English. This limits our understanding of how alignment failures manifest in low-resource and culturally diverse languages. We introduce IndicSafeEval, a persuasion-based jailbreak evaluation framework for Indian languages. Our benchmark combines ten safety critical content categories with six human-like persuasive strategies across four different Indian languages, such as Hindi, Bengali, Marathi and Punjabi, resulting in 7,200 adversarial prompts. We conduct a systematic black-box evaluation of several open-source LLMs to examine how their safety behaviour varies across languages, persuasion strategies, and risk categories. Our analysis shows that the model does not behave equally safely across all languages and prompt styles. Instead, safety performance depends strongly on both the languages used and the way a request is phrased using persuasive cues. We further observe that different risk categories exhibit different levels of vulnerability, with some types of harmful content being significantly more susceptible to persuasion-based jailbreaks than others. These findings reveal important limitations of current safety evaluations, which are largely English-centric, and underscore the need for multilingual and persuasion-aware benchmarking frameworks to more accurately assess real-world LLM safety. Our implementation is available at https://github.com/MonSaikat/IndicSafeEval. Warning: this paper contains example data that may be offensive or harmful.

</details>

### 40. UbuntuGuard: A Culturally-Grounded Policy Benchmark for Equitable AI Safety in African Languages

📄 [arXiv](https://arxiv.org/abs/2601.12696) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1663/)　📅 2026-01　🏷 ACL 2026

**关键词**：`benchmark`、`African languages`、`expert-authored policy`、`cultural alignment`

👤 **作者**：Tassallah Abdullahi、…、Carsten Eickhoff

- 🎯 **研究动机**：guard 模型以西方与高资源语言为中心，非洲低资源语言面临文化错配与跨语失效
- 🔬 **研究方法**：由 155 位敏感领域专家撰写对抗查询，导出上下文相关安全政策与参考响应构建政策式基准，评测 15 个模型的静态、动态与多语三变体
- 📌 **结论**：英文中心基准高估真实多语安全；跨语迁移覆盖不足，动态模型虽善用政策也难以完全本地化非洲语言语境

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current guardian models are predominantly Western-centric and optimized for high-resource languages, leaving low-resource African languages vulnerable to evolving harms, cross-lingual failures, and cultural misalignment. Moreover, most guardian models rely on rigid, predefined safety categories that fail to generalize across diverse linguistic and sociocultural contexts. Achieving robust safety requires flexible, runtime-enforceable policies and benchmarks that reflect local norms, harm scenarios, and cultural expectations. We introduce UbuntuGuard, the first policy-based safety benchmark for African languages built from adversarial queries authored by 155 domain experts across sensitive fields, including healthcare. From these expert-crafted queries, we derive context-specific safety policies and reference responses that capture culturally grounded risk signals, enabling policy-aligned evaluation of guardian models. We evaluate 15 models, comprising seven general-purpose LLMs and eight guardian models across three distinct variants: static, dynamic, and multilingual. Our findings reveal that existing English-centric benchmarks overestimate real-world multilingual safety, cross-lingual transfer provides partial but insufficient coverage, and dynamic models, while better equipped to leverage policies at inference time, still struggle to fully localize African-language contexts. These findings highlight the urgent need for multilingual, culturally grounded safety benchmarks to enable the development of reliable and equitable guardian models for low-resource languages.

</details>

### 41. SEA-SafeguardBench: Evaluating AI Safety in SEA Languages and Cultures

📄 [arXiv](https://arxiv.org/abs/2512.05501)　📅 2025-12

**关键词**：`benchmark`、`Southeast Asian languages`、`native annotation`、`cultural harm`

👤 **作者**：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji、Trevor Cohn、Peerat Limkonchotiwat

- 🎯 **研究动机**：现有多语安全基准多由英文机器翻译而来，无法捕捉东南亚低资源语言的文化细微差别与地区性危害
- 🔬 **研究方法**：构建首个经人工核验的 SEA 安全基准，覆盖 8 种语言、21640 个样本，分 general、in-the-wild 与内容生成三个子集
- 📌 **结论**：即使 SOTA LLM 与 guardrail 在 SEA 文化与危害场景上也明显逊色于英文文本上的表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safeguard models help large language models (LLMs) detect and block harmful content, but most evaluations remain English-centric and overlook linguistic and cultural diversity. Existing multilingual safety benchmarks often rely on machine-translated English data, which fails to capture nuances in low-resource languages. Southeast Asian (SEA) languages are underrepresented despite the region's linguistic diversity and unique safety concerns, from culturally sensitive political speech to region-specific misinformation. Addressing these gaps requires benchmarks that are natively authored to reflect local norms and harm scenarios. We introduce SEA-SafeguardBench, the first human-verified safety benchmark for SEA, covering eight languages, 21,640 samples, across three subsets: general, in-the-wild, and content generation. The experimental results from our benchmark demonstrate that even state-of-the-art LLMs and guardrails are challenged by SEA cultural and harm scenarios and underperform when compared to English texts.

</details>

### 42. FraudBench: Stress-Testing Policy-Grounded Banking Agents Against Adaptive Fraud

📄 [arXiv](https://arxiv.org/abs/2608.18136)　📅 2026-08

**关键词**：`analysis`、`specialized guardrail`、`domain policy`、`multilingual safety`

👤 **作者**：Dheeraj Mohandas Pai、Lu Xian

- 🎯 **研究动机**：银行 agent 既能答疑也能改联系方式、重置 PIN 与转账，现有基准不测对话操纵身份、授权与信任下的安全行动
- 🔬 **研究方法**：FraudBench 基于 τ²-bench 双控框架与 τ-Knowledge 银行环境：agent 与模拟来电者经工具共享可变账户状态并检索 698 文档政策语料；107 个冻结场景含 10 类欺诈机制与 17 个链式自适应攻击，安全依赖历史
- 📌 **结论**：四个 agent 的攻击安全率仅 49%-65%，money-mule 与第一方欺诈是跨模型共同弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational agents now act for end users through tools while holding access to customer databases and internal policy documents that a caller can reach through dialogue alone. Banking is the clearest case: the same agent that answers a question can also change contact details, reset a PIN, or move money, so ordinary customer service is inseparable from authorization, fraud detection, and policy compliance. Existing financial-fraud benchmarks classify static transactions or messages, and general agent-safety benchmarks target prompt injection or generic harmful use; none test whether a policy-grounded banking agent safely acts when a caller manipulates identity, authorization, and trust over a conversation. We introduce FraudBench, an executable benchmark built on the $τ^2$-bench dual-control framework and the $τ$-Knowledge banking environment. Both the agent and the simulated caller act through tools over shared, mutable account state, and the agent may grant the caller access to selected tools; the environment exposes a 698-document internal policy corpus that the agent must retrieve from. FraudBench contains 150 authored adversarial scenarios; a frozen public set of 107 (90 across ten fraud mechanisms plus 17 chained adaptive attacks) is used for all reported runs, with 43 further chained attacks held out. Safety is history-dependent: single-control tasks satisfy every precondition but one, and adaptive attacks make a later, locally valid request unsafe because of an earlier probe, admission, or failed attempt. Each scenario is annotated with observable evidence, prohibited actions, safe dispositions, and intervention points. A preliminary single-trial evaluation of four agents on the 107 graded tasks yields attack-security between 49\% and 65\%, with money-mule and first-party fraud the most common cross-model weaknesses.

</details>

### 43. Beyond "I Can't Help With That": How Child Safety Experts Evaluate AI Chatbot Safety

📄 [arXiv](https://arxiv.org/abs/2608.07902)　📅 2026-08

**关键词**：`analysis`、`adversarial robustness`、`specialized guardrail`、`domain policy`

👤 **作者**：Hannah Cha、Neha Shukla、Solon Barocas、Alexandra Chouldechova、Eugenia Kim、Jennifer Wortman Vaughan

- 🎯 **研究动机**：现有 AI 儿童安全评测脱离青少年真实伤害场景，未验证地假设拒答即恰当且只查对抗提示与表面伤害
- 🔬 **研究方法**：访谈 19 位一线从业者（社工、治疗师、心理医生），评估聊天机器人对青少年常见高危情境回应的伤害与支持作用
- 📌 **结论**：识别出易致伤害与能真正支持青少年的行为及改进建议，指出须把从业者视角纳入儿童安全评测与基础设施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Youth increasingly turn to AI chatbots for social and emotional support, raising concerns about how these systems respond, especially in high-stakes situations. However, existing child safety evaluations of AI lack grounding in real-world harms that youth experience, rely on unvalidated assumptions about what counts as an appropriate output (e.g., refusal), and typically focus on detecting adversarial prompts or surface-level harms in outputs only. Thus, these evaluations can fail to detect responses that pose harm to youth in practice. To better understand the limitations of current evaluation practices, we conducted interviews with 19 practitioners working directly with youth in vulnerable situations, including social workers, therapists, and psychologists, asking them to reflect on chatbots' responses to risky situations commonly faced by youth, as established in prior empirical work. Practitioners identified chatbot behaviors likely to cause harm as well as those that could meaningfully support youth in difficult moments, discussed the role that chatbots should (and should not) play in these interactions, and offered concrete recommendations for improving chatbot responses. Based on these findings, we provide recommendations for AI child safety evaluation and infrastructure, and highlight the need for incorporating practitioners' perspectives into safety work.

</details>

### 44. Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs

📄 [arXiv](https://arxiv.org/abs/2608.18131)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`Indian languages`、`cross-lingual safety`、`cultural bias`、`alignment gap`

👤 **作者**：Namya Bhatnagar

- 🎯 **研究动机**：安全对齐高度英语中心，非英语失败时语音助手会绕过安全过滤向非英语社区传播有害偏见
- 🔬 **研究方法**：INCLUDE 基准含 2604 条提示覆盖英语、Hindi、Bengali、Marathi、Tamil 与 Hinglish，评十个开源与闭源 LLM 的 14,988 个偏见分
- 📌 **结论**：开源模型中 Bengali 平均偏见分最高；英语出现反转——开源模型中最低、闭源模型中最高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current safety alignment training for Large Language Models (LLMs) are heavily English-centric. When such safety filters fail for non-English languages, the consequences are immediate and user-facing: voice assistants and spoken dialogue systems may produce stereotype-reinforcing outputs, bypassing the standard English-focused safety alignments and propagating harmful bias to non-English speaking communities. For spoken language technologies deployed across India's linguistically diverse population, this represents a critical failure mode. To address this cross-lingual gap, we introduce INCLUDE (Indian Cultural Lens for Understanding and Detecting Embedded Biases), a multilingual evaluation benchmark designed to quantify Indian-centric socio-cultural biases. INCLUDE consists of 2,604 prompts spanning six prompt languages: English, Hindi, Bengali, Marathi, Tamil, and Hinglish (Hindi-English code-mix). We evaluate ten open- and closed-source LLMs against this benchmark, analyzing 14,988 bias scores. Our statistical results reveal two key findings. First, Bengali yielded the highest average bias score in open-source models. Second, English demonstrated a notable reversal, producing the lowest bias in open-source models but the highest bias in closed-source models.

</details>

### 45. Why Do Safety Guardrails Degrade Across Languages?

📄 [arXiv](https://arxiv.org/abs/2605.17173) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`defense`、`analysis`、`guard model`、`content moderation`、`safety-utility trade-off`、`cross-lingual safety`

👤 **作者**：Max Zhang、Ameen Patel、Sang T. Truong、Sanmi Koyejo

- 🎯 **研究动机**：JSR 把多种安全驱动因素混为一体，掩盖非英语安全退化的具体成因
- 🔬 **研究方法**：多组 IRT 潜变量模型解耦语言无关鲁棒性 θ、prompt 难度 β、语言处理难度 γ 与 prompt 特定跨语言安全差 τ；基于 MultiJail 评 61 个模型配置、10 种语言共 190 万条回复
- 📌 **结论**：22 个配置在英语上反而更脆弱；高 τ prompt 集中于盗窃、武器等物理伤害与低资源语言；框架 AUC 0.940，整语言留出仍达 0.875

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models exhibit safety degradation in non-English languages. Standard evaluation relies on Jailbreak Success Rate (JSR), which confounds several safety-driving factors into one, obscuring the specific cause(s) of safety failure. We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). Using the MultiJail dataset, we evaluate the safety robustness of 61 model configurations across 5 closed-model families and 10 languages of varying resource, aggregating a dataset of 1.9 million responses. Exploratory Factor Analysis shows safety is primarily unidimensional: models refuse different harm types mainly through a shared mechanism. Contrary to the expected trend that safety degrades largely in low-resource languages, 22 model configurations are more vulnerable in English than in low-resource languages. Low-resource languages produce more uncertain responses (high entropy) than high-resource languages. Also, high-$τ$ prompts cluster in physical harm categories like Theft and Weapons and lower-resource languages, trends validated through cross-dataset generalization. While global translation quality shows low correlation with $τ$, severe mistranslations drive high-bias outliers, as validated by native speakers. Cultural and conceptual grounding mismatches may also contribute to $τ$. In predictive validation, the IRT framework achieves $\mathrm{AUC} = 0.940$, and unlike rate baselines stays predictive when a whole language is held out ($0.875$). Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.

</details>

### 46. Safety of Large Language Models Beyond English: A Systematic Literature Review of Risks, Biases, and Safeguards

🎓 [Official](https://aclanthology.org/2026.eacl-long.44/)　📅 2026-03　🏷 ACL 2026

**关键词**：`survey`、`multilingual safety`、`evidence gap`、`localized safeguards`、`cross-lingual risk`、`safeguards`

👤 **作者**：Aleksandra Krasnodębska、Katarzyna Dziewulska、Karolina Seweryn、Maciej Chrabaszcz、Wojciech Kusa

- 🎯 **研究动机**：LLM 的安全机制可能无法从英语泛化到其他语言，导致毒性检测、偏见缓解与危害防护的差异
- 🔬 **研究方法**：系统综述英语之外多语言安全研究，梳理评测方法、数据集可得性与评测偏差等挑战
- 📌 **结论**：识别多语言安全研究的证据空白并给出未来建议，附带 Streamlit 交互面板提供原始数据与持续更新

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) continue to evolve, ensuring their safety across multiple languages has become a critical concern. While LLMs demonstrate impressive capabilities in English, their safety mechanisms may not generalize effectively to other languages, leading to disparities in toxicity detection, bias mitigation, and harm prevention. This systematic review examines the multilingual safety of LLMs by synthesizing findings from recent studies that evaluate their robustness across diverse linguistic and cultural contexts beyond English language. Our review explores the methodologies used to assess multilingual safety, identifies challenges such as dataset availability and evaluation biases. Based on our analysis we highlight gaps in multilingual safety research and provide recommendations for future work. This review aims to contribute to the development of fair and effective safety mechanisms for LLMs across all languages. We provide the extracted data in an interactive Streamlit dashboard, enabling transparent access to the raw data and allowing for continuous updates.

</details>

### 47. Nürnberg NLP @ GermEval Shared Task 2026: Harmful Content Detection in German Social Media through Error-Independent LLM Voters

📄 [arXiv](https://arxiv.org/abs/2608.22246)　📅 2026-08

**关键词**：`detection`、`German moderation`、`error-independent ensemble`、`class imbalance`

👤 **作者**：Philipp Steigerwald、Eric Rudolph、Jens Albrecht

- 🎯 **研究动机**：德语社媒有害类别稀少且与多数类共享表层语言，macro-F1 由稀有类决定，胜负手是误差独立性而非更强单模型
- 🔬 **研究方法**：每个子任务构建跨 LLM、训练方法与类别范围三个正交轴的九 voter 集成，主要依据内部交叉验证选择
- 📌 **结论**：GermEval 2026 隐藏测试集 macro-F1 达 89.56（C2A）、71.63（DBO）、54.84（VIO）、83.02（DEF），四个子任务全部第一

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful content in German social media does real-world damage, from calls to action to criminal defamation. The GermEval 2026 shared task scores its detection in four subtasks. The technical challenge is a severe class imbalance. The harmful classes are rare and share surface language with the dominant majority class, yet under macro-F1 they decide the score. The decisive lever is then not a stronger single model but error independence. This insight becomes a per-subtask nine-voter ensemble spanning three orthogonal axes: LLM, training method and class scope. Selected mainly on internal cross-validation, the system reaches macro-F1 of 89.56 (C2A), 71.63 (DBO), 54.84 (VIO) and 83.02 (DEF) on the hidden test set, placing first on all four subtasks.

</details>

### 48. SPAR-Hate: Auditor-Guided Multi-Perspective Role Reasoning for Bilingual Hate Speech Parsing

📄 [arXiv](https://arxiv.org/abs/2608.22018)　📅 2026-08　🏷 EMNLP 2026

**关键词**：`detection`、`defense`、`bilingual moderation`、`evidence arbitration`、`structured hate parsing`、`multi-perspective reasoning`

👤 **作者**：Yifan Lyu、Dianqing Lin、Xinran Li、Jiaqi Qiao、Xiujuan Xu

- 🎯 **研究动机**：仇恨言论研究从粗粒度分类转向结构化解析（联合识别 target、论据与标签），但多 target、局部解读冲突与文化编码语言使绑定难以恢复
- 🔬 **研究方法**：SPAR-Hate 审计引导多视角框架：把文档拆为局部焦点单元，从 Victim、Moderator、Cultural Bystander 三视角生成有证据候选，在 grounding 与 schema 约束下仲裁冲突并重组预测
- 📌 **结论**：STATE-ToxiCN 与受控 TBO split 上在严格联合 target-argument-label 指标取得提升；结构化 teacher trace 还可训练更小 student 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hate speech research has moved from coarse-grained classification towards structured parsing, where systems jointly identify targets, supporting arguments, and target-level labels. Documents with multiple targets, conflicting local readings, or culturally coded language make these bindings difficult to recover. SPAR-Hate is an auditor-guided multi-perspective role-reasoning framework for bilingual hate speech parsing. It decomposes each document into local focus units, elicits evidence-grounded candidates from Victim, Moderator, and Cultural Bystander perspectives, resolves candidate conflicts under grounding and schema constraints, and reassembles sample-level predictions. Experiments on STATE-ToxiCN and a controlled TBO split show gains across local and API backbones, concentrated on strict joint target-argument-label metrics. Full-test integrated-prompt controls, component ablations, and bounded-arbitration diagnostics identify the contribution of separated perspective generation and arbitration. Structured teacher traces also support training a smaller student model.

</details>

### 49. What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models

📄 [arXiv](https://arxiv.org/abs/2608.16852)　📅 2026-08

**关键词**：`detection`、`high-risk deployment`、`specialized guardrail`、`domain policy`

👤 **作者**：Saisab Sadhu、Aadit Sengupta、Vinay Kumar Sankarapu、Pratinav Seth

- 🎯 **研究动机**：合规检测器只有在裁决依赖所述规则而非场景表面特征时才有意义，该条件是否成立从未被检验
- 🔬 **研究方法**：审计 activation probe 与 guard：删除、置换、替换治理规则观察检测准确率是否变化；构建交叉规则基准使规则或场景单独都不预测标签；提出免训练 Internal Compliance Score
- 📌 **结论**：所有被测 guard 与探针均规则盲——换掉治理条款裁决几乎不变，仅逐步推理能逃出；ICS 未过预注册基线门槛但便宜可用，可用于大规模审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Regulatory compliance monitoring in deployed language models is increasingly implemented as a legal and audit control, checking model outputs against written rules spanning data protection, healthcare, financial regulation, and platform policy. Such monitoring is meaningful only if a detector's verdict depends on the stated rule rather than on surface features of the scenario. We show this condition fails across the current class of compliance detectors, a failure we call rule blindness. Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test, including a policy-conditioned guard that correctly cites the governing clause yet barely changes its verdict when that clause is swapped for its permissive counterpart. A purpose-built benchmark crossing two rules with two scenarios, so that neither alone predicts the label, confirms the failure under a design no prior benchmark rules out, and shows that step by step reasoning, not any fast detector we test, is what escapes it. Auditing at scale requires a retraining-free detector, so we introduce the Internal Compliance Score (ICS): a training-free activation readout calibrated from ten labelled pairs and scored by a single projection. We hold ICS to the same scrutiny as the guards it audits: a pre-registered criterion for beating trivial baselines is not met, and a bag-of-words model matches its pooled generalisation exactly. It remains useful because it is inexpensive, letting us audit four deployed guard models, an 8B zero-shot judge, and thirteen benchmarks, and it raises the mechanically verified pass rate when used to rank candidate responses, though an adaptive white-box attack removes this gain. We release the counterfactual protocol and crossed-rule benchmark so rule blindness can be tested in future probe and guard claims.

</details>

### 50. Training-Time Explainability for Multilingual Hate Speech Detection: Aligning Model Reasoning with Human Rationales

📄 [arXiv](https://arxiv.org/abs/2608.26125)　📅 2026-08

**关键词**：`detection`、`multilingual hate`、`rationale alignment`、`training-time explainability`

👤 **作者**：Muhammad Deedahwar Mazhar Qureshi、Sannaan Khan、Muhammad Atif Qureshi、Wael Rashwan

- 🎯 **研究动机**：针对穆斯林社群的文化编码多语言仇恨常逃逸审核，而准确分类器不透明且有偏
- 🔬 **研究方法**：训练时 explainability 框架用人工 rationale 对齐模型推理，在 HateXplain 与 BullySent 上比较 LIME 等四种归因方法
- 📌 **结论**：梯度与 attention 正则化提升 F-score、解释 plausibility 与 faithfulness，并捕捉文化特定隐性仇恨线索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online hate against Muslim communities often appears in culturally coded, multilingual forms that evade conventional AI moderation. Such systems, though accurate, remain opaque and risk bias, over-censorship, or under-moderation, particularly when detached from sociocultural context. We propose a \emph{training-time} explainability framework that aligns model reasoning with human-annotated rationales, improving both classification performance and interpretability. Our approach is evaluated on HateXplain (English) and BullySent (Hinglish), reflecting the prevalence of anti-Muslim hate across both languages. Using LIME, Integrated Gradients, Grad X Input, and attention, we assess accuracy, explanation quality, and cross-method agreement. Results show that gradient- and attention-based regularization improve F-scores, enhance plausibility and faithfulness, and capture culturally specific cues for detecting implicit anti-Muslim hate, offering a path toward multilingual, culturally aware content moderation.

</details>

### 51. Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration

📄 [arXiv](https://arxiv.org/abs/2608.29378)　📅 2026-09

**关键词**：`benchmark`、`Arabic guard calibration`、`B-H operating point`、`Arabizi transfer`、`benign refusal`、`harmful refusal`

👤 **作者**：Mohamad Zbib、Ammar Mohanna

- 🎯 **研究动机**：阿拉伯语 LLM 需拒绝有害 prompt 又不过度拒绝良性或敏感 prompt，单一 refusal 率掩盖这一权衡
- 🔬 **研究方法**：以良性拒绝 B 与有害拒绝 H 分开度量，在五个阿拉伯语模型、AraSafe 全集 130 次运行上评测 refusal-only SFT、mixed-SFT、DPO 与推理 guard 的作用
- 📌 **结论**：refusal-only SFT 塌缩为 blanket refusal，精选 mixed-SFT 配置在 B=14%–23% 时达 H=90%–93%；DPO 与 guard 的效果因模型而异；向 Arabizi 迁移时 H 均有提升但无一达 90%，支持按模型选择运行点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Arabic large language models must refuse harmful prompts without over-refusing benign or sensitive prompts, yet a single refusal rate hides this trade-off. We evaluate it using benign refusal B and harmful-prompt refusal H, where H measures refusal rather than harmful compliance. Across five Arabic-capable models and 130 runs on the full human-written AraSafe set, refusal-only supervised fine-tuning (SFT) collapses toward blanket refusal, whereas selected mixed-SFT configurations reach H = 90% to 93% at B = 14% to 23%; four selected configurations exceed the H = 90% target in all three runs, while Fanar does so in two of three. Direct Preference Optimization (DPO) and inference guards change B and H differently across models rather than acting as uniform upgrades. In a blinded 300-response audit, annotator binary-refusal agreement is 89.0% (kappa = 0.78); Qwen3Guard and Aya Expanse 32B reach 88.7% and 91.0% accuracy, respectively, with no conclusive paired difference. Selected SFT raises H on Arabizi for all five models, but none reaches 90%, showing only partial transfer from Modern Standard Arabic. Overall, the results support model-specific operating-point selection: set a deployment target and retain only interventions that improve it.

</details>

### 52. 'Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection

📄 [arXiv](https://arxiv.org/abs/2608.24191)　📅 2026-08

**关键词**：`benchmark`、`Urdu moderation`、`cross-script consistency`、`missed harm`

👤 **作者**：Fawzia Zehra、Kara-Isitt、Sonal Khosla、Stephen Swift

- 🎯 **研究动机**：2.46 亿人使用的乌尔都语长期缺席 LLM 安全评测与九年 WOAH 论文，其对审核的影响未量化
- 🔬 **研究方法**：测五个 LLM 在 Nastaliq、Roman 与 code-switch 六个数据集上，定义 Missed-in-Urdu 分数并与英文翻译判定对比
- 📌 **结论**：原文-翻译标签不稳定率 15.9%-31.6%，有害内容原文漏检率中位 4.3%，小型开放权重模型更差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Urdu, the world's tenth most spoken language with 246 million speakers, remains almost entirely absent from mainstream LLM safety evaluation and nine years of WOAH proceedings. To investigate whether this absence has measurable consequences for content moderation reliability, five large language models, GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen-2.5, and Llama-3.1, were tested across six datasets spanning Nastaliq Urdu, Roman Urdu, English, and code-switched Urdu-English. Across the five Urdu-script datasets, label instability between original-script and English-translation classification ranged from 15.9% (Gemini 2.5 Flash) to 31.6% (Qwen-2.5), with a 'Missed-in-Urdu' rate, content flagged as harmful in English translation but passed as normal in the original script, ranging from 2.4% to 9.9% (median 4.3%). A complete enumeration of all 205 papers across nine ALW/WOAH editions via the ACL Anthology API confirms zero dedicated Urdu papers across the entire period. Results indicate that current LLMs provide uneven safety assurance across Urdu's script varieties, with smaller open-weight models showing substantially higher instability and missed-harm rates than frontier closed models.

</details>

### 53. Redteaming Leading Arabic LLMs with ASAS

📄 [arXiv](https://arxiv.org/abs/2608.21985)　📅 2026-08

**关键词**：`benchmark`、`Arabic red teaming`、`human annotation`、`judge reliability`、`multilingual jailbreak`、`human evaluation`

👤 **作者**：Fidaa Abed、Haidar Khan、M Saiful Bari、Babar Khan、Abdalghani Abujabal

- 🎯 **研究动机**：阿拉伯语 LLM 安全尤其是对抗性红队评估严重不足，缺乏文化扎根的评测资源
- 🔬 **研究方法**：ASAS 首个完全人工策划的阿拉伯语红队 benchmark：801 条 prompt 覆盖 8 个安全类别与 8 种攻击策略并附 MSA 理想回应，人工标注者以四级安全量表评估 GPT-4o、Claude 3.7 Sonnet、ALLaM、FANAR 等七个模型
- 📌 **结论**：多数模型无法防御超 50% 的不安全 prompt，武器与违禁品等高危类别缺口最大，直接与混淆攻击最有效；自动 judge（如 GPT-4o）表现远逊人工标注

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We conduct a redteaming evaluation across seven leading models with Arabic capabilities, including GPT-4o, Claude 3.7 Sonnet, and regional models such as ALLaM and FANAR. Human annotators rate responses using a structured 4-point safety scale, revealing that most models fail to defend against 50% of unsafe prompts. Our findings highlight major safety gaps in high-harm categories such as weapons and illicit substances, with direct and obfuscation-based attacks proving most effective. The results also show that language alignment does not readily transfer across languages, and that automated safety judges (e.g., GPT-4o) perform poorly compared to human annotators. ASAS provides a culturally grounded benchmark and redteaming protocol to drive progress in Arabic LLM safety.

</details>

### 54. ArabicDialectSafety: A Dialect-Aware Benchmark for Arabic Content Safety Classification

📄 [arXiv](https://arxiv.org/abs/2608.01291)　📅 2026-08

**关键词**：`benchmark`、`Arabic dialect`、`fine-grained harm`、`content classification`

👤 **作者**：Wajdi Zaghouani、Md. Rafiul Biswas、Kholoud Khalil Aldous、Mabrouka Bessghaier

- 🎯 **研究动机**：阿拉伯语内容安全评测缺少方言级细粒度资源，方言差异被忽视
- 🔬 **研究方法**：人工构建 25071 条提示覆盖六种阿拉伯语变体与七类细粒度伤害，双任务（二分类与细粒度）评测七个监督与生成模型
- 📌 **结论**：微调 MARBERTv2 的 Macro-F1 达 0.95/0.90，显著超过 prompted 前沿 LLM；低资源马格里布方言仍存在明显性能差距，前沿 LLM 不安全生成率低于 5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present ArabicDialectSafety, a human-curated Arabic safety dataset of 25,071 prompts covering six Arabic varieties: Modern Standard Arabic, Syrian, Egyptian, Algerian, Palestinian, and Moroccan. The dataset is annotated with dialect labels and seven fine-grained harm categories. We introduce a dual-task evaluation framework for binary safe/unsafe detection and granular harm classification across dialects. Benchmarking seven supervised and generative models, we find that fine-tuned MARBERTv2 achieves the strongest performance, with Macro-F1 scores of 0.95 for binary classification and 0.90 for granular classification, substantially outperforming prompted frontier LLMs, including Arabic-specialized models. Our analyses show that dialect conditioning is most effective when integrated at the representation level, while significant performance gaps remain for low-resource Maghrebi dialects. We further evaluate seven frontier LLMs as response generators on harmful dialectal Arabic prompts and observe unsafe generation rates below 5 percent across models. We release the dataset and code upon acceptance to support future research on dialect-aware Arabic safety evaluation. Warning: This paper contains examples of harmful and potentially offensive content included solely for research purposes.

</details>

### 55. VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation

📄 [arXiv](https://arxiv.org/abs/2608.15600)　📅 2026-08

**关键词**：`benchmark`、`specialized guardrail`、`domain policy`、`multilingual safety`

👤 **作者**：Mingyu Yuan、Shengtao Wen、Lingbing Guo、Zhen Bi、Xiang Chen

- 🎯 **研究动机**：中文辱骂审核基准支持标签与细粒度分类，但不能确定性验证裁决所述依据
- 🔬 **研究方法**：VARM-Bench 每例含锚定六项决定（目标、类型、显式性、立场、有害标签、细类）的简短理由，确定性协议评字段正确性、目标对齐、有效性、完整记录一致与隐藏记录错误，不依赖 LLM judge
- 📌 **结论**：强标签级表现可掩盖完整审核记录的大量错误

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread circulation of abusive online content has increased the need for reliable moderation of Chinese social-media text. Existing Chinese benchmarks support label classification, fine-grained toxicity categorization, and target-aware extraction, but do not provide a unified representation for deterministically verifying the stated basis of a moderation decision. We introduce VARM-Bench, a benchmark for field-anchored chain-of-thought rationales in Chinese abusive-speech moderation. Each instance contains a concise natural-language rationale with explicit anchors for six decisions: target, target type, target explicitness, author stance, harmfulness label, and fine-grained category. Our deterministic protocol evaluates field correctness, target alignment, output validity, complete-record agreement, and hidden record errors conditioned on correct final decisions, without relying on an LLM judge. Under a common structured-output protocol, we evaluate language models across multiple model families using zero-shot prompting, taxonomy guidance, and structured CoT supervision, and analyze lexical-cue sensitivity and field-level errors. Results show that strong label-level performance can conceal substantial errors in complete moderation records. VARM-Bench provides an auditable and reproducible benchmark for evaluating verifiable moderation rationales in Chinese abusive-speech moderation.

</details>

### 56. Language-Specific Gaps in AI Safety Training Datasets

📄 [arXiv](https://arxiv.org/abs/2608.13695) · 📊 [Dataset](https://huggingface.co/datasets/ChialukaOnuoha/safety-slice-audit)　📅 2026-08

**关键词**：`benchmark`、`specialized guardrail`、`domain policy`、`multilingual safety`

👤 **作者**：Chialuka Prisca-Mary Onuoha、Bright Etornam Sunu、Rashidat Sikiru

- 🎯 **研究动机**：厂商常引用覆盖十几种语言的多语安全基准作安全证据，单语言层面的检查常不成立
- 🔬 **研究方法**：审计 21 个资源、25 个语言切片，覆盖 Hausa（低）、Swahili（中）、French（高）三档，做同管线内受控比较
- 📌 **结论**：Hausa 切片低于其论文自身翻译质量阈值而 Swahili 通过；自残与性内容在两个非洲语档均零原生覆盖，多语越狱鲁棒性不对称与数据稀薄处结构一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model providers routinely cite multilingual safety benchmarks spanning a dozen or more languages as evidence that their models are safe for non-English-speaking users. We show that these collection-level coverage claims frequently do not survive inspection at the level of an individual language. Auditing 21 resources across 25 language slices, of which 20 count as datasets under our counting rules, spanning three languages chosen to represent low- (Hausa), mid- (Swahili), and high-resource (French) tiers, we find that gaps in provenance, annotation reliability, access, harm-taxonomy coverage, and data reuse recur in patterns that partially, but not fully, track resource level. Using a controlled within-pipeline comparison, we show a Hausa-language slice falling below its own paper's translation-quality acceptance threshold while the same pipeline's Swahili output clears the same bar comfortably; this is evidence that these gaps are measurable and addressable, not inherent. We further show that self-harm and sexual-content categories have no native-language coverage in either African-language tier we studied, a total rather than gradated gap that a purely resource-level account does not predict. We connect these findings to a documented, persistent asymmetry in multilingual jailbreak robustness (single-turn attacks largely mitigated, multi-turn attacks still effective), arguing that this asymmetry is structurally consistent with where our audit finds training and evaluation data thinnest. We contribute a reusable slice-level audit methodology, a cross-tier empirical comparison, and concrete recommendations for dataset creators, model providers, and venues aiming to make ``multilingual coverage'' claims verifiable rather than merely stated. Dataset: https://huggingface.co/datasets/ChialukaOnuoha/safety-slice-audit

</details>

### 57. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

📄 [arXiv](https://arxiv.org/abs/2608.22335)　📅 2026-08

**关键词**：`benchmark`、`Bengali moderation`、`register shift`、`classifier failure`、`Bengali safety`、`culturally grounded harm`

👤 **作者**：Naymul Islam、Nusrat Jahan Lia、Shubhashis Roy Dipta、Sabik Bin Sultan、Abdullah Khan Zehady

- 🎯 **研究动机**：孟加拉语是全球第七大语言，LLM 安全评测却压倒性以英语为中心，文化特定危害与语体变化未被覆盖
- 🔬 **研究方法**：BanglaSafe 收录 879 条孟加拉语 prompt（309 原生撰写+570 专家审校），覆盖 17 类文化危害与变化语言、书写风格、权威框架的五种提示条件，评估 18 个前沿 LLM
- 📌 **结论**：53.6% 回应不安全或部分不安全、14.7% 严格有害；最强效应来自孟加拉语内部语体——正式新闻调查语体比随意消息高 17 个百分点成功率，无需对抗工程；现有分类器近半数案例判错

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) while 14.7% contains strictly harmful content, and that the strongest observed effect is not the switch from English to Bengali but the choice of writing style within Bengali: the same harmful request phrased as a formal newspaper investigation succeeds 17 percentage points more often than the same request phrased as a casual message, with no adversarial engineering involved. We further show that existing safety classifiers struggle to reliably evaluate Bengali content, with even frontier models failing on nearly half of all cases.

</details>

### 58. MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2609.04859)　📅 2026-09

**关键词**：`benchmark`、`VLM instruction hijacking`、`multilingual safety`、`adversarial evaluation`

👤 **作者**：Changming Xiao、Zhenliang Ni、Jinhui He、Han Shu、Jie Hu

- 🎯 **研究动机**：多模态指令跟随基准语言覆盖有限且缺少对抗安全场景，不适应真实多语言安全敏感部署
- 🔬 **研究方法**：构建 MM-IFEval-Pro：覆盖中英文、4 大任务类 24 子类与 8 指令类 52 子类、每样本平均 3.0 个约束，并纳入多样 instruction hijacking 案例；另构建含中文与对抗指令的强化学习训练集
- 📌 **结论**：RL 训练显著提升该基准表现并有效迁移到其他主流多模态基准，展现跨任务跨语言泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As vision-language models (VLMs) rapidly advance in image understanding, cross-modal reasoning, and complex instruction execution, instruction-following capability has become a key indicator of their reliability and practicality. However, existing multimodal instruction-following benchmarks still suffer from limited language coverage and insufficient adversarial safety scenarios, making them inadequate for evaluating real-world multilingual and safety-sensitive settings. To address these gaps, we present MM-IFEval-Pro, a multimodal instruction-following benchmark covering Chinese and English tasks as well as diverse instruction hijacking cases. MM-IFEval-Pro includes 4 major task categories and 24 subcategories and 8 instruction categories with 52 subcategories, with each sample containing an average of 3.0 constraints to realistically simulate complex instruction scenarios. We further construct a reinforcement-learning training set enriched with Chinese and adversarial instructions, which significantly improves model performance on MM-IFEval-Pro and transfers effectively to other mainstream multimodal benchmarks, demonstrating strong cross-task and cross-language generalization.

</details>

### 59. SinoGlyphBench: A Diagnostic Benchmark for Chinese Glyph-Level Obfuscation in Language-Model Moderation

📄 [arXiv](https://arxiv.org/abs/2609.05843) · 🐙 [Code](https://github.com/fengshun124/SinoGlyphBench.)　📅 2026-09

**关键词**：`benchmark`、`glyph obfuscation`、`moderation evasion`、`Chinese content safety`、`semantic anchor`

👤 **作者**：Yifan Wang、…、Qiaoyu Tan

- 🎯 **研究动机**：中文字形混淆可使有害内容对人可读、对自动审核失效，缺诊断式评测
- 🔬 **研究方法**：SinoGlyphBench 定位 label-critical 语义锚点，构造原文/字形混淆配对（文本+图像双模态），区分证据腐蚀与一般表面扰动
- 📌 **结论**：12 个 LLM/MLLM 共 176,916 次评测：有害 FN/FP 各 +6.1/+4.7pp，跨文字替换最难防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Glyph-level obfuscation can leave harmful Chinese content readable to humans while degrading automated moderation. We introduce SinoGlyphBench, a diagnostic benchmark that identifies label-critical semantic anchors and creates matched original and glyph-obfuscated inputs in text and image modalities. By perturbing anchors, background context, or both, this design distinguishes corruption of moderation-relevant evidence from general surface variation. Across 176,916 paired evaluations of 12 LLMs and MLLMs, obfuscation increases harmful false-negative and false-positive rates by 6.1 and 4.7 percentage points, respectively, and reduces four-way accuracy by 5.0 points. Models retain 75.7% of the decisions that were correct on the matched original inputs. Full-scope perturbations cause the largest degradation, anchor-only perturbations are more damaging than background-only perturbations, and cross-script substitution is particularly difficult in the text modality. Analysis of structured outputs identifies observable mismatches in visible-form reading, intended-message recovery, and final safety judgment. The evaluated models, therefore, remain brittle to Chinese content written with non-canonical glyphs. Resources are available at https://github.com/fengshun124/SinoGlyphBench.

</details>

### 60. "Shut Up and Let Me Enjoy My Otome": Understanding and Measuring the Toxicity in Otome Game Communities

📄 [arXiv](https://arxiv.org/abs/2609.08009)　📅 2026-09

**关键词**：`analysis`、`toxicity measurement`、`gaming community`、`LLM-based detection`、`coordinated harassment`

👤 **作者**：Yage Zhang、Xinyue Shen、Yukun Jiang、Michael Backes、Yang Zhang

- 🎯 **研究动机**：乙女游戏社区毒性大规模存在但从未被测量，平台差异与协同攻击规律未知
- 🔬 **研究方法**：OtomeSCAN 采集微博/Reddit 62 万帖，4,308 条人工标注 8 类受害目标，评测 7 种毒性检测器并提出 LLM 检测器
- 📌 **结论**：微博毒性占比 22.2%（Reddit 3.71%），外部攻击下 72 小时升至 37.1%；最佳检测器 F1 0.82/0.78，识别 191 个协同攻击集群

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Otome games, a romance simulation genre primarily targeting female, have emerged as a major force in the global gaming market, attracting hundreds of millions of players and billions in revenue. Despite their popularity, otome game communities face pervasive online toxicity, which has been largely unexplored. In this work, we present the first large-scale measurement of toxicity in otome game communities across social platforms. We introduce OtomeSCAN, a framework for collecting, evaluating, and analyzing 620,045 posts from Weibo and Reddit spanning 18 months. To support robust analysis, we manually annotated a ground-truth dataset of 4,308 posts, identifying eight target groups such as players and game developers. We evaluate seven toxicity detectors on the dataset, including general-purpose models and our proposed LLM-based detectors, with our best model achieving F1-scores of 0.82 (Weibo) and 0.78 (Reddit). Our analysis reveals significant platform-based differences in toxicity: 22.20% of otome-related posts on Weibo are toxic, compared to 3.71% on Reddit. Besides, real-world events like in-community conflicts can rapidly escalate toxicity, with toxicity ratios increasing to 37.09% in just 72 hours during an external attack on Weibo. We also flag 191 potential-coordination clusters in otome game communities, 64.40% of which target game developers, with several accounts participating repeatedly across multiple clusters. We hope our work inspires further research on community-specific toxicity and contributes to building healthier online spaces for marginalized gaming communities.

</details>
