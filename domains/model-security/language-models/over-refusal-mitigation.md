# Over-Refusal 评测与缓解

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究 safety-aligned language model 对良性、上下文安全或可安全完成的请求产生不必要拒答的问题，覆盖 exaggerated safety、false refusal、overrefusal 与 safety-helpfulness calibration。收录范围要求“安全相关误拒”是论文的主要研究对象，重点包括 benchmark 与触发因素、训练和参数干预、推理时校准，以及降低误拒后能否继续抵御 harmful prompt 与 adaptive jailbreak；知识不足导致的 epistemic abstention、仅把 over-refusal 当附属指标的通用防御、外部 guard model 和多模态模型不在本页重复收录。

> 时间优先采用论文首次公开月份；没有可核验预印本时采用正式出版月份。

## 研究脉络

- **问题定义与规模化评测：** 早期工作从 safety tuning 引出的 exaggerated safety 出发，以近义良恶性 prompt pair、pseudo-harmful prompt、自动生成和 fuzzing 扩展到可复现的大规模测量。
- **场景化诊断：** 研究从单轮敏感词误触发扩展到 RAG context、多轮 intent clarification、医疗 safe completion、仇恨言论去毒和规则正当性，说明“是否应该拒绝”依赖任务与语境。
- **训练期缓解：** data overgeneration、structured reasoning、preference optimization、局部层微调、单 token prefix 和 competing rewards 试图在参数中重新分离 benign 与 harmful decision boundary。
- **推理时校准：** prompt optimization、activation ablation/steering、energy landscape 与 contrastive decoding 不修改或少量修改基座模型，适合部署后校准但可能产生新的 jailbreak 暴露面。
- **机制与安全边界：** harmfulness、refusal 与 task-conditioned over-refusal 并非同一表示方向；因此只压低全局 refusal signal 可能释放有害能力，必须联合报告 benign utility、harmful refusal 与 adaptive attack。

## 问题起点与词汇捷径

### 1. Navigating the OverKill in Large Language Models

🎓 [Official](https://aclanthology.org/2024.acl-long.253/)　📅 2024-01　🏷 ACL 2024

**关键词**：`analysis`、`harmful-word shortcut`、`Self-CD`、`contrastive decoding`

👤 **作者**：Chenyu Shi、…、Dahua Lin

- 🎯 **研究动机**：模型存在有害词捷径（过度关注 kill 等词），强调安全的提示会加剧良性查询过度拒答
- 🔬 **研究方法**：Self-Contrastive Decoding 免训练且模型无关：放大有无安全强调系统提示时的输出分布差异提取过度注意力，再经对比解码弱化
- 📌 **结论**：拒答率平均降 20% 且几乎不影响安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are meticulously aligned to be both helpful and harmless. However, recent research points to a potential overkill which means models may refuse to answer benign queries. In this paper, we investigate the factors for overkill by exploring how models handle and determine the safety of queries. Our findings reveal the presence of shortcuts within models, leading to excessive attention to harmful words like ‘kill’ and prompts emphasizing safety will exacerbate overkill. Based on these insights, we introduce Self-Contrastive Decoding (Self-CD), a training-free and model-agnostic strategy, to alleviate this phenomenon. We first extract such excessive attention by amplifying the difference in the model’s output distributions when responding to system prompts that either include or omit an emphasis on safety. Then we determine the final next-token predictions by downplaying the excessive attention via contrastive decoding. Empirical results have indicated that our method has achieved an average reduction of the refusal rate by 20 % while having almost no impact on safety.

</details>

### 2. Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions

📝 [OpenReview](https://openreview.net/forum?id=gT5hALch9z)　📅 2023-09　🏷 ICLR 2024

**关键词**：`analysis`、`safety tuning`、`exaggerated safety`、`alignment data`

- 🎯 **研究动机**：指令模型用多少、何种安全数据才能获得安全行为不明
- 🔬 **研究方法**：系统改变safety data来源与比例做对齐实验
- 📌 **结论**：少量数据即显著提升安全，但过强safety tuning引发exaggerated safety

### 3. ORFuzz: Fuzzing the "Other Side" of LLM Safety -- Testing Over-Refusal

📄 [arXiv](https://arxiv.org/abs/2508.11222) · 🌐 [Project](https://conf.researchr.org/details/ase-2025/ase-2025-papers/71/ORFuzz-Fuzzing-the-Other-Side-of-LLM-Safety-Testing-Over-Refusal)　📅 2025-08　🏷 ASE 2025

**关键词**：`benchmark`、`evolutionary fuzzing`、`OR-Judge`、`pseudo-malicious prompt`

👤 **作者**：Haonan Zhang、…、Wenhai Wang

- 🎯 **研究动机**：LLM 过度拒绝误伤良性查询，现有测试方法基准有缺陷且生成能力不足
- 🔬 **研究方法**：提出首个演化模糊测试框架 ORFuzz：安全类别感知种子选择、推理 LLM 自适应变异优化与人类对齐判分模型 OR-Judge
- 📌 **结论**：生成误拒实例的比率 6.98% 为基线两倍以上；衍生的 1855 例 ORFuzzSet 在 10 个 LLM 上平均误拒率达 63.56%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) increasingly exhibit over-refusal - erroneously rejecting benign queries due to overly conservative safety measures - a critical functional flaw that undermines their reliability and usability. Current methods for testing this behavior are demonstrably inadequate, suffering from flawed benchmarks and limited test generation capabilities, as highlighted by our empirical user study. To the best of our knowledge, this paper introduces the first evolutionary testing framework, ORFuzz, for the systematic detection and analysis of LLM over-refusals. ORFuzz uniquely integrates three core components: (1) safety category-aware seed selection for comprehensive test coverage, (2) adaptive mutator optimization using reasoning LLMs to generate effective test cases, and (3) OR-Judge, a human-aligned judge model validated to accurately reflect user perception of toxicity and refusal. Our extensive evaluations demonstrate that ORFuzz generates diverse, validated over-refusal instances at a rate (6.98% average) more than double that of leading baselines, effectively uncovering vulnerabilities. Furthermore, ORFuzz's outputs form the basis of ORFuzzSet, a new benchmark of 1,855 highly transferable test cases that achieves a superior 63.56% average over-refusal rate across 10 diverse LLMs, significantly outperforming existing datasets. ORFuzz and ORFuzzSet provide a robust automated testing framework and a valuable community resource, paving the way for developing more reliable and trustworthy LLM-based software systems.

</details>

### 4. Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary

🎓 [Official](https://aclanthology.org/2025.emnlp-main.1065/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`benchmark`、`safety decision boundary`、`multilingual evaluation`、`RASS`

👤 **作者**：Licheng Pan、Yongqi Tong、Xin Zhang、Xiaolu Zhang、Jun Zhou、Zhixuan Chu

- 🎯 **研究动机**：过度拒绝源于过度保守的安全对齐，模型在安全决策边界难以区分细微的良性/有害差异
- 🔬 **研究方法**：提出 RASS：利用表示空间 steering 向量定位并筛选边界附近的过度拒绝 prompt；并构建多语言评测集 MORBench
- 📌 **结论**：边界视角更精确可解释且可扩展至多语言，能更有效缓解过度拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet they often refuse to answer legitimate queries—a phenomenon known as overrefusal. Overrefusal typically stems from over-conservative safety alignment, causing models to treat many reasonable prompts as potentially risky. To systematically understand this issue, we probe and leverage the models’ safety decision boundaries to analyze and mitigate overrefusal. Our findings reveal that overrefusal is closely tied to misalignment at these boundary regions, where models struggle to distinguish subtle differences between benign and harmful content. Building on these insights, we present RASS, an automated framework for prompt generation and selection that strategically targets overrefusal prompts near the safety boundary. By harnessing steering vectors in the representation space, RASS efficiently identifies and curates boundary-aligned prompts, enabling more effective and targeted mitigation of overrefusal. This approach not only provides a more precise and interpretable view of model safety decisions but also seamlessly extends to multilingual scenarios. We have explored the safety decision boundaries of various LLMs and construct the MORBench evaluation set to facilitate robust assessment of model safety and helpfulness across multiple languages. Code and datasets are available at https://github.com/Master-PLC/RASS.

</details>

### 5. FalseReject: A Resource for Improving Contextual Safety and Mitigating Over-Refusals in LLMs via Structured Reasoning

📄 [arXiv](https://arxiv.org/abs/2505.08054) · 🌐 [Project](https://false-reject.github.io/) · 📝 [OpenReview](https://openreview.net/forum?id=1w9Hay7tvm)　📅 2025-05　🏷 COLM 2025

**关键词**：`benchmark`、`structured reasoning`、`contextual safety`、`multi-agent generation`

👤 **作者**：Zhehao Zhang、Weijie Xu、Fanyou Wu、Chandan K. Reddy

- 🎯 **研究动机**：敏感表述下良性恶意语境难区分，误拒普遍
- 🔬 **研究方法**：FalseReject以graph-informed multi-agent pipeline构造44类16k查询与结构化响应
- 📌 **结论**：29个模型显示问题普遍，SFT可基本不损安全地减少误拒

### 6. EVOREFUSE: Evolutionary Prompt Optimization for Evaluation and Mitigation of LLM Over-Refusal to Pseudo-Malicious Instructions

📄 [arXiv](https://arxiv.org/abs/2505.23473) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/027613d38d7a8bc9e42ee862fcced7ea-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`benchmark`、`evolutionary optimization`、`pseudo-malicious prompt`、`alignment data`

👤 **作者**：Xiaorui Wu、…、Zhuang Li

- 🎯 **研究动机**：模板改写难以稳定诱发多样化的过度拒答样本
- 🔬 **研究方法**：EVOREFUSE以进化式prompt优化生成pseudo-malicious指令，构建TEST与ALIGN数据集
- 📌 **结论**：训练后over-refusal最高降29.85%且不牺牲安全性

### 7. Automatic Pseudo-Harmful Prompt Generation for Evaluating False Refusals in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2409.00598) · 📝 [OpenReview](https://openreview.net/forum?id=ljFgX6A8NL)　📅 2024-09　🏷 COLM 2024

**关键词**：`benchmark`、`pseudo-harmful generation`、`content control`、`PHTest`

👤 **作者**：Bang An、Sicheng Zhu、Ruiyi Zhang、Michael-Andrei Panaitescu-Liess、Yuancheng Xu、Furong Huang

- 🎯 **研究动机**：人工pseudo-harmful prompt数量少且缺模型针对性，误拒评测受限
- 🔬 **研究方法**：提出内容受控、模型相关的自动生成方法并构建PHTest评测集
- 📌 **结论**：20个模型的评测揭示误拒与jailbreak安全性间的系统性权衡

### 8. OR-Bench: An Over-Refusal Benchmark for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2405.20947) · 🌐 [Project](https://proceedings.mlr.press/v267/cui25a.html)　📅 2024-05　🏷 ICML 2025

**关键词**：`benchmark`、`large-scale evaluation`、`hard prompt`、`toxic control`

👤 **作者**：Justin Cui、Wei-Lin Chiang、Ion Stoica、Cho-Jui Hsieh

- 🎯 **研究动机**：过度拒答已被经验观察但缺系统测量，构造能引发过拒的提示很困难
- 🔬 **研究方法**：自动生成大规模过拒数据的技术构建 OR-Bench：80,000 条过拒提示（10 类拒答类别）、约 1,000 条难提示与 600 条毒性提示
- 📌 **结论**：系统测得 32 个主流 LLM（8 个家族）的过拒表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) require careful safety alignment to prevent malicious outputs. While significant research focuses on mitigating harmful content generation, the enhanced safety often come with the side effect of over-refusal, where LLMs may reject innocuous prompts and become less helpful. Although the issue of over-refusal has been empirically observed, a systematic measurement is challenging due to the difficulty of crafting prompts that can elicit the over-refusal behaviors of LLMs. This study proposes a novel method for automatically generating large-scale over-refusal datasets. Leveraging this technique, we introduce OR-Bench, the first large-scale over-refusal benchmark. OR-Bench comprises 80,000 over-refusal prompts across 10 common rejection categories, a subset of around 1,000 hard prompts that are challenging even for state-of-the-art LLMs, and an additional 600 toxic prompts to prevent indiscriminate responses. We then conduct a comprehensive study to measure the over-refusal of 32 popular LLMs across 8 model families. Our datasets are publicly available at https://huggingface.co/bench-llms and our codebase is open-sourced at https://github.com/justincui03/or-bench. We hope this benchmark can help the community develop better safety aligned models.

</details>

### 9. XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models

🎓 [Official](https://aclanthology.org/2024.naacl-long.301/)　📅 2023-08　🏷 ACL 2024

**关键词**：`benchmark`、`contrastive prompt pair`、`exaggerated safety`、`refusal evaluation`

👤 **作者**：Paul Röttger、Hannah Kirk、Bertie Vidgen、Giuseppe Attanasio、Federico Bianchi、Dirk Hovy

- 🎯 **研究动机**：模型会把与不安全措辞相似的明显安全提示也拒绝，exaggerated safety缺系统性评测
- 🔬 **研究方法**：XSTest由250条分十类安全提示与200条不安全提示构成对照测试集
- 📌 **结论**：系统揭示SOTA语言模型的误拒失败模式及更普遍的安全建设难题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless. However, there is a tension between these two objectives, since harmlessness requires models to refuse to comply with unsafe prompts, and thus not be helpful. Recent anecdotal evidence suggests that some models may have struck a poor balance, so that even clearly safe prompts are refused if they use similar language to unsafe prompts or mention sensitive topics. In this paper, we introduce a new test suite called XSTest to identify such eXaggerated Safety behaviours in a systematic way. XSTest comprises 250 safe prompts across ten prompt types that well-calibrated models should not refuse to comply with, and 200 unsafe prompts as contrasts that models, for most applications, should refuse. We describe XSTest’s creation and composition, and then use the test suite to highlight systematic failure modes in state-of-the-art language models as well as more general challenges in building safer language models.

</details>

### 10. Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration

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

### 11. Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context

🎓 [Official](https://aclanthology.org/2026.findings-acl.1177/)　📅 2026-07　🏷 ACL 2026

**关键词**：`benchmark`、`healthcare safety`、`safe completion`、`intent ambiguity`

👤 **作者**：Zhihao Zhang、Liting Huang、Guanghao Wu、Preslav Nakov、Heng Ji、Usman Naseem

- 🎯 **研究动机**：现有基准只测拒答/服从两极，无法评估对双用途模糊查询提供安全有用回答的 Safe Completion 质量
- 🔬 **研究方法**：Health-ORSC-Bench 含 31,920 条七类健康主题的良性边界提示，自动管线加人工校验，以不同意图模糊度评测 30 个 LLM
- 📌 **结论**：安全优化模型对 Hard 良性提示拒答率高达 80%；GPT-5、Llama-4 等大模型呈 safety-pessimism，过度拒答多于 Qwen-3-Next 等 MoE 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in Large Language Models is critical for healthcare; however, reliance on binary refusal boundaries often results in over-refusal of benign queries or unsafe compliance with harmful ones. While existing benchmarks measure these extremes, they fail to evaluate Safe Completion: the model’s ability to maximise helpfulness on dual-use or borderline queries by providing safe, high-level guidance without crossing into actionable harm. We introduce Health-ORSC-Bench, the first large-scale benchmark designed to systematically measure Over-Refusal and Safe Completion quality in healthcare. Comprising 31,920 benign boundary prompts across seven health categories (e.g., self-harm, medical misinformation), our framework uses an automated pipeline with human validation to test models at varying levels of intent ambiguity. We evaluate 30 state-of-the-art LLMs, including GPT-5 and Claude-4, revealing a significant tension: safety-optimised models frequently refuse up to 80% of “Hard” benign prompts, while domain-specific models often sacrifice safety for utility. Our findings demonstrate that model family and size significantly influence calibration: larger frontier models (e.g., GPT-5, Llama-4) exhibit “safety-pessimism” and higher over-refusal than smaller or MoE-based counterparts (e.g., Qwen-3-Next), highlighting that current LLMs struggle to balance refusal and compliance. Health-ORSC-Bench provides a rigorous standard for calibrating the next generation of medical AI assistants toward nuanced, safe, and helpful completions. Our code and data is available at: https://github.com/ZhihaoZhang97/Health-ORSC-Bench. Warning: Some contents may include toxic or undesired contents.

</details>

### 12. Useless but Safe? Benchmarking Utility Recovery with User Intent Clarification in Multi-Turn Conversations

📄 [arXiv](https://arxiv.org/abs/2604.27093) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04　🏷 COLM 2026

**关键词**：`benchmark`、`multi-turn clarification`、`utility recovery`、`intent revision`、`over-refusal`、`intent clarification`

👤 **作者**：Mingqian Zheng、Malia Morgan、Liwei Jiang、Carolyn Rose、Maarten Sap

- 🎯 **研究动机**：安全对齐研究忽略良性用户澄清意图后模型能否恢复有用性，单轮评测无法刻画
- 🔬 **研究方法**：CarryOnBench 从 398 个表面有害实为良性的查询模拟 5,970 段对话（1,866 种流程、23,880 条回复），以 checklist 指标 Ben-Util 评 14 个模型
- 📌 **结论**：首轮仅满足 10.5%-37.6% 的良性信息需求；澄清后 13/14 模型接近或超过单轮基线；识别出 utility lock-in、unsafe recovery、repetitive recovery 三种单轮不可见的失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM safety alignment techniques improve model robustness against adversarial attacks, but overlook whether and how LLMs can recover helpfulness when benign users clarify their intent. We introduce CarryOnBench, the first interactive benchmark that measures whether LLMs can revise their interpretation of user intent and recover utility, while remaining safe through multi-turn conversations. Starting from 398 seemingly harmful queries with benign underlying intents, we simulate 5,970 conversations by varying user follow-up sequences, evaluating 14 models on both intent-aligned utility and safety. CarryOnBench yields 1,866 different conversation flows of 4--12 turns, totaling 23,880 model responses. We design Ben-Util, a checklist-based metric that evaluates how well each model response fulfills the user's benign information need using atomic items. At turn one, models fulfill only 10.5--37.6% of the user's benign information need. When the same query includes the benign intent upfront, models fulfill 25.1--72.1%, confirming that models withhold information due to intent misinterpretation, not limited knowledge. With benign clarifications in multi-turn conversations, 13 of 14 models approach or exceed this single-turn baseline, yet recovery cost varies across models. We identify three failure modes invisible to single-turn evaluations: utility lock-in, where a model rarely updates despite clarification; unsafe recovery, where a model updates at disproportionate safety cost; and repetitive recovery, where a model recycles prior responses rather than providing new information. Moreover, conversations converge to similar harmfulness levels regardless of how conservative the model starts. These findings expose a gap that single-turn evaluations miss -- whether a model is appropriately cautious or simply unresponsive to clarified user intent.

</details>

### 13. Blind Refusal: Language Models Refuse to Help Users Evade Unjust, Absurd, and Illegitimate Rules

📄 [arXiv](https://arxiv.org/abs/2604.06233) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04　🏷 COLM 2026

**关键词**：`analysis`、`normative reasoning`、`rule legitimacy`、`blind refusal`、`over-refusal`

👤 **作者**：Cameron Pattison、Lorenzo Manuali、Seth Lazar

- 🎯 **研究动机**：并非所有规则都值得遵守：拒绝帮助逃避不公正、荒谬或非法规则的请求本身是道德推理失败
- 🔬 **研究方法**：构建横跨 5 类规则失效理由与 19 种权威类型的合成数据集，18 个模型配置，以盲评 LLM-as-judge 分类帮助/硬拒/搪塞与是否识别规则失效
- 📌 **结论**：模型拒绝 75.4% 的失效规则请求；57.5% 情况下模型理解失效理由却仍拒绝——拒绝行为与规范推理能力解耦

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-trained language models routinely refuse requests for help circumventing rules. But not all rules deserve compliance. When users ask for help evading rules imposed by an illegitimate authority, rules that are deeply unjust or absurd in their content or application, or rules that admit of justified exceptions, refusal is a failure of moral reasoning. We introduce empirical results documenting this pattern of refusal that we call blind refusal: the tendency of language models to refuse requests for help breaking rules without regard to whether the underlying rule is defensible. Our dataset comprises synthetic cases crossing 5 defeat families (reasons a rule can be broken) with 19 authority types, validated through three automated quality gates and human review. We collect responses from 18 model configurations across 7 families and classify them on two behavioral dimensions -- response type (helps, hard refusal, or deflection) and whether the model recognizes the reasons that undermine the rule's claim to compliance -- using a blinded GPT-5.4 LLM-as-judge evaluation. We find that models refuse 75.4% (N=14,650) of defeated-rule requests and do so even when the request poses no independent safety or dual-use concerns. We also find that models engage with the defeat condition in the majority of cases (57.5%) but decline to help regardless -- indicating that models' refusal behavior is decoupled from their capacity for normative reasoning about rule legitimacy.

</details>

### 14. RefusalBench: Generative Evaluation of Selective Refusal in Grounded Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.321/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`RAG refusal`、`context perturbation`、`overconfidence`、`selective refusal`、`RAG context`

👤 **作者**：Aashiq Muhamed、Leonardo F. R. Ribeiro、Markus Dreyer、Virginia Smith、Mona Diab

- 🎯 **研究动机**：RAG 系统基于有缺陷上下文的选择性拒答是关键失败点，静态基准因数据集伪影与记忆而失效
- 🔬 **研究方法**：提出 RefusalBench：通过受控语言扰动程序化生成诊断用例，176 种扰动策略覆盖 6 类信息不确定性与 3 个强度级，评测 30 余个模型
- 📌 **结论**：前沿模型多文档任务拒答准确率低于 50%；拒答可分解为检测与归类两种能力，规模与扩展推理均无帮助，但它是可训练的对齐敏感能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The ability of language models in RAG systems to selectively refuse to answer based on flawed context is critical for safety, yet remains a significant failure point. Our large-scale study reveals that even frontier models struggle in this setting, with refusal accuracy dropping below 50% on multi-document tasks, while exhibiting dangerous over-confidence or over-caution. Static benchmarks fail to reliably evaluate this capability, as models exploit dataset-specific artifacts and memorize test instances. We introduce RefusalBench, a generative methodology that programmatically creates diagnostic test cases through controlled linguistic perturbation. Our framework employs 176 distinct perturbation strategies across six categories of informational uncertainty and three intensity levels. Evaluation of over 30 models uncovers systematic failure patterns: refusal comprises separable detection and categorization skills, and neither scale nor extended reasoning improves performance. We find that selective refusal is a trainable, alignment-sensitive capability, offering a clear path for improvement. We release two benchmarks—RefusalBench-NQ (single-document) and RefusalBench-GaRAGe (multi-document), and our complete generation framework to enable continued, dynamic evaluation of this critical capability.

</details>

### 15. CausalT5k: Diagnosing Refusal and Failure Modes in Trustworthy Causal Reasoning Across Causal Rungs

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

### 16. Analyzing Bias in False Refusal Behavior of Large Language Models for Hate Speech Detoxification

📄 [arXiv](https://arxiv.org/abs/2601.08668)　📅 2026-01

**关键词**：`analysis`、`hate-speech detoxification`、`linguistic bias`、`cross-translation`

👤 **作者**：Kyuri Im、Shuzhou Yuan、Michael Färber

- 🎯 **研究动机**：仇恨言论解毒任务本身常触发安全警报导致 LLM 误拒，触发误拒的语境与语言偏倚不明
- 🔬 **研究方法**：在英语与多语数据上评测九个 LLM 的误拒行为，分析语义毒性与目标群体相关的系统性偏倚
- 📌 **结论**：模型不成比例地拒绝高毒性与针对国籍、宗教、政治立场的输入；把英文先译成中文解毒再回译可显著减少误拒并保留原内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While large language models (LLMs) have increasingly been applied to hate speech detoxification, the prompts often trigger safety alerts, causing LLMs to refuse the task. In this study, we systematically investigate false refusal behavior in hate speech detoxification and analyze the contextual and linguistic biases that trigger such refusals. We evaluate nine LLMs on both English and multilingual datasets, our results show that LLMs disproportionately refuse inputs with higher semantic toxicity and those targeting specific groups, particularly nationality, religion, and political ideology. Although multilingual datasets exhibit lower overall false refusal rates than English datasets, models still display systematic, language-dependent biases toward certain targets. Based on these findings, we propose a simple cross-translation strategy, translating English hate speech into Chinese for detoxification and back, which substantially reduces false refusals while preserving the original content, providing an effective and lightweight mitigation approach.

</details>

### 17. Steering Over-refusals Towards Safety in Retrieval Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2510.10452)　📅 2025-10

**关键词**：`defense`、`RAG safety`、`context contamination`、`activation steering`

👤 **作者**：Utsav Maskey、Mark Dras、Usman Naseem

- 🎯 **研究动机**：RAG 中上下文污染、查询与上下文领域及有害文本密度会令良性查询被误拒，over-refusal 机理不明
- 🔬 **研究方法**：构建覆盖医疗、化学与开放域的 RagRefuse 基准分析拒绝诱因，并提出 SafeRAG-Steering 在推理时把嵌入引导至已确认安全的非拒绝输出区域
- 📌 **结论**：该干预在污染 RAG 流水线中减少良性误拒，同时保留正当拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models (LLMs) induces over-refusals -- where LLMs decline benign requests due to aggressive safety filters. We analyze this phenomenon in retrieval-augmented generation (RAG), where both the query intent and retrieved context properties influence refusal behavior. We construct RagRefuse, a domain-stratified benchmark spanning medical, chemical, and open domains, pairing benign and harmful queries with controlled context contamination patterns and sizes. Our analysis shows that context arrangement / contamination, domain of query and context, and harmful-text density trigger refusals even on benign queries, with effects depending on model-specific alignment choices. To mitigate over-refusals, we introduce \textsc{SafeRAG-Steering}, a model-centric embedding intervention that steers the embedding regions towards the confirmed safe, non-refusing output regions at inference time. This reduces over-refusals in contaminated RAG pipelines while preserving legitimate refusals.

</details>

### 18. Beyond Over-Refusal: Scenario-Based Diagnostics and Post-Hoc Mitigation for Exaggerated Refusals in LLMs

📄 [arXiv](https://arxiv.org/abs/2510.08158)　📅 2025-10

**关键词**：`benchmark`、`multi-turn scenario`、`trigger attribution`、`post-hoc mitigation`

👤 **作者**：Shuzhou Yuan、Ercong Nie、Yinuo Sun、Chenxuan Zhao、William LaCroix、Michael Färber

- 🎯 **研究动机**：LLM 常因良性请求含近似不安全词汇而误拒，多轮场景尤甚但缺乏系统诊断
- 🔬 **研究方法**：构建带 Focus 关键词标注的单轮 XSB 与多轮场景化 MS-XSB 基准，用事后解释定位拒绝触发词，并部署忽略词指令、prompt 改写与注意力引导三种免训练缓解
- 📌 **结论**：四个指令微调 Llama 上显著提升安全请求依从性且安全防护保持稳固

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) frequently produce false refusals, declining benign requests that contain terms resembling unsafe queries. We address this challenge by introducing two comprehensive benchmarks: the Exaggerated Safety Benchmark (XSB) for single-turn prompts, annotated with "Focus" keywords that identify refusal-inducing triggers, and the Multi-turn Scenario-based Exaggerated Safety Benchmark (MS-XSB), which systematically evaluates refusal calibration in realistic, context-rich dialog settings. Our benchmarks reveal that exaggerated refusals persist across diverse recent LLMs and are especially pronounced in complex, multi-turn scenarios. To mitigate these failures, we leverage post-hoc explanation methods to identify refusal triggers and deploy three lightweight, model-agnostic approaches, ignore-word instructions, prompt rephrasing, and attention steering, at inference time, all without retraining or parameter access. Experiments on four instruction-tuned Llama models demonstrate that these strategies substantially improve compliance on safe prompts while maintaining robust safety protections. Our findings establish a reproducible framework for diagnosing and mitigating exaggerated refusals, highlighting practical pathways to safer and more helpful LLM deployments.

</details>

### 19. COVER: Context-Driven Over-Refusal Verification in LLMs

🌐 [Project](https://anonymous.4open.science/r/Over-safety-in-LLMs-9647) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.1243/)　📅 2025-07　🏷 ACL 2025

**关键词**：`benchmark`、`context-driven refusal`、`RAG evaluation`、`task sensitivity`

👤 **作者**：Giovanni Sullutrone、Riccardo A. Vigliermo、Sonia Bergamaschi、Luca Sala

- 🎯 **研究动机**：上下文驱动的过度拒绝（RAG 或摘要翻译任务中外部内容触发安全护栏）区别于问题驱动过拒绝，未被量化
- 🔬 **研究方法**：COVER 两阶段评估框架在两个公共语料上量化分析该行为
- 📌 **结论**：过拒绝率强烈依赖任务、系统提示、模型家族与检索文档数；翻译与摘要畸高、QA 相对稳健；文档增多反而降低拒绝率，严格系统提示不一定升高过拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce the concept of context-driven over-refusal, an abstention arising when model’s safety guardrails are triggered by the grounding knowledge provided alongside the user’s request. Distinct from question-driven over-refusal, this occurs in both retrieval-augmented generation (RAG) and natural language processing (NLP) task completion (e.g. summarization, translation) where external content can unexpectedly trigger refusals. In this work, we present a novel two-stage evaluation framework named COVER, designed to quantify and analyze this behavior. Through a comprehensive empirical study on two public corpora, we show that over-refusal rates strongly depend on the task, system prompts, model family, and the number of retrieved documents. We observe that tasks such as translation and summarization yield disproportionately high over-refusal rates, while question-answering remains relatively robust, especially in newer models. Moreover, increasing the number of contextual documents tends to reduce refusals, yet broadens the pool of prompts at risk of encountering at least one “unsafe” text. Interestingly, strict system prompts do not necessarily lead to higher over-refusal rates, suggesting that in the absence of explicit directives, some models may default to a more cautious behavior. These findings highlight the need for fine-grained alignment and benchmarking strategies sensitive to both user intent and contextual nuances, offering a roadmap for future research in model training and evaluation.

</details>

### 20. You Only Need One Single Token to Refine Safety Alignment

🎓 [Official](https://aclanthology.org/2026.findings-acl.662/)　📅 2026-07　🏷 ACL 2026

**关键词**：`defense`、`single-token alignment`、`focal weighting`、`decision boundary`

👤 **作者**：Wenqian Yu、Shuo Chen、Zhijiang Li、Zhipeng Wang、Jindong Gu

- 🎯 **研究动机**：training-free干预推理开销高且依赖架构，全量微调成本又大
- 🔬 **研究方法**：STA冻结基座仅优化约4096参数的单token前缀，结合硬过滤与focal软加权的混合加权机制
- 📌 **结论**：9个模型、10个数据集上为LLM、MLLM与推理模型取得更优安全-帮助性平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) face a critical alignment challenge: balancing safety with helpfulness. Excessive safety can lead to over-refusal, where models reject harmful-looking yet benign queries, severely limiting utility.Existing training-free interventions offer an efficient way to mitigate over-refusal without re-training, but suffer from high inference overhead and architecture dependency. Our work explores a complementary direction: rather than applying post-hoc corrections to model outputs, our goal is to intrinsically reshape the distributions of harmful and benign samples within the model’s decision space. In this paper, we argue that a lightweight training-based approach can more effectively distinguish between harmful and benign samples. We propose Single Token Alignment (STA), which optimizes only a single-token prefix (e.g., 4,096 parameters) while keeping the base model frozen. To address the inherent challenge of achieving robust refinement through such a minimal parameter interface, STA employs a mixed weighting mechanism integrated with its optimization objective. This mechanism incorporates hard weighting via stringent data filtering to provide clear, unbiased learning signals, and soft weighting through a focal mechanism to prioritize challenging cases.Extensive experiments across 9 models and 10 datasets demonstrate that STA achieves a superior safety-helpfulness balance for LLMs, MLLMs, and reasoning models, offering a highly efficient and generalizable solution for refining safety alignment.

</details>

### 21. Addressing Over-Refusal in LLMs with Competing Rewards

📄 [arXiv](https://arxiv.org/abs/2606.31748)　📅 2026-06

**关键词**：`defense`、`competing rewards`、`safety reasoning`、`process reward`

👤 **作者**：Taeyoun Kim、Aviral Kumar

- 🎯 **研究动机**：安全训练诱发过度拒绝；RL 推理可缓解权衡但推理常沦为预设回应的橡皮图章
- 🔬 **研究方法**：把不安全推理本身作为探索信号：推理玩家探索产生不安全回应的策略、回答玩家保证最终输出安全，单模型经过程奖励在一条思维链内分饰两角（SEAR）
- 📌 **结论**：刻意进行有害推理探索再可靠回到安全答案，缓解过度拒绝并能抵御直接操纵推理的攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlying problem that reasoning can often be a "rubber stamp" for a predetermined response. In this paper, we address the safety-refusal trade-off by rethinking how models are trained to reason about safety. Our key insight is that unsafe reasoning can itself serve as a useful exploratory signal. Rather than preemptively blocking harmful thoughts, we encourage the model to sufficiently explore unsafe reasoning but produce a safe response. The harmful exploration improves the model's ability to distinguish harmful from harmless prompts by resolving ambiguity, allowing it to remain safe while complying only when appropriate. We cast this as an adversarial optimization problem in which a reasoning player explores strategies for producing an unsafe response and an answer player ensures that the final output is safe. We train a single model with dense rewards to play both roles within one chain-of-thought, across different segments. To achieve this, we find that process rewards are crucial for stable optimization of competing objectives. Our resulting model SEAR deliberately engages in harmful reasoning as exploration while reliably flipping back to a safe answer. We demonstrate that this behavior helps mitigate over-refusal and defend against attacks that directly manipulate the reasoning to be harmful.

</details>

### 22. ProSafePrune: Projected Safety Pruning for Mitigating Over-Refusal in LLMs

📝 [OpenReview](https://openreview.net/forum?id=QkHKaPfRAB)　📅 2026-04　🏷 ICLR 2026

**关键词**：`defense`、`projected pruning`、`low-rank subspace`、`parameter intervention`

- 🎯 **研究动机**：直接剪除refusal分量会连带破坏对harmful请求的拒答
- 🔬 **研究方法**：ProSafePrune先投影到保留安全行为的低秩子空间再做参数剪枝
- 📌 **结论**：降低false rejection、维持恶意拒答并轻微改善通用能力

### 23. Adaptive Helpfulness–Harmlessness Alignment with Preference Vectors

🎓 [Official](https://aclanthology.org/2026.eacl-long.77/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`HH alignment`、`preference vector`、`refusal control`、`over-refusal control`

👤 **作者**：Ren-Wei Liang、…、Shao-Hua Sun

- 🎯 **研究动机**：RLHF 与 DPO 在有益-无害权衡上存在性能冲突、可控性差且难扩展新偏好
- 🔬 **研究方法**：受 task arithmetic 启发提出 Preference Vector：对单个偏好分别训练模型、提取行为偏移为偏好向量、测试时动态合并，实现细粒度用户可控调整
- 📌 **结论**：提升有益性而不致过度保守，偏好权衡可平滑控制并支持多偏好可扩展对齐，新偏好免重训练即可集成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring that large language models (LLMs) are both helpful and harmless is a critical challenge, as overly strict constraints can lead to excessive refusals, while permissive models risk generating harmful content. Existing approaches, such as reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO), attempt to balance these trade-offs but suffer from performance conflicts, limited controllability, and poor extendability. To address these issues, we propose Preference Vector, a novel framework inspired by task arithmetic. Instead of optimizing multiple preferences within a single objective, we train separate models on individual preferences, extract behavior shifts as preference vectors, and dynamically merge them at test time. This modular approach enables fine-grained, user-controllable preference adjustments and facilitates seamless integration of new preferences without retraining. Experiments show that our proposed Preference Vector framework improves helpfulness without excessive conservatism, allows smooth control over preference trade-offs, and supports scalable multi-preference alignment.

</details>

### 24. Discern Truth from Falsehood: Reducing Over-Refusal via Contrastive Refinement

📄 [arXiv](https://arxiv.org/abs/2603.03323) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2026/hash/45a30141c6719e9cfedfb51f1c665a37-Abstract-Conference.html)　📅 2026-03　🏷 ICLR 2026

**关键词**：`defense`、`contrastive refinement`、`toxic distinction`、`pre-alignment stage`

👤 **作者**：Yuxiao Lu、Lin Xu、Yang Sun、Wenjun Li、Jie Shi

- 🎯 **研究动机**：安全对齐把真正有害与表面有害样本压入同一拒答区域
- 🔬 **研究方法**：DCR在正式alignment前加入contrastive refinement强化两类区分
- 📌 **结论**：减少over-refusal且不损safety与通用能力

### 25. Deactivating Refusal Triggers: Understanding and Mitigating Overrefusal in Safety Alignment

🎓 [Official](https://aclanthology.org/2026.trustnlp-main.26/)　📅 2026-03

**关键词**：`analysis`、`refusal trigger`、`trigger-aware fine-tuning`、`linguistic cue`

👤 **作者**：Zhiyu Xue、Zimo Qi、Guangliang Liu、Bocheng Chen、Ramtin Pedarsani

- 🎯 **研究动机**：安全对齐后 aligned LLM 也拒绝良性查询的过度拒绝问题研究不足，损害可用性
- 🔬 **研究方法**：定义 refusal triggers（训练数据中引发拒绝的语言线索），发现对齐使模型把含非有害线索在内的触发子与拒绝关联导致过拒绝；据此在安全微调中显式解耦触发子
- 📌 **结论**：在越狱防御与良性查询响应间取得更优权衡，超越先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment aims to ensure that large language models (LLMs) refuse harmful requests by post-training on harmful queries paired with refusal answers.Although safety alignment is widely adopted in industry, the overrefusal problem where aligned LLMs also reject benign queries after safety alignment post-training, remains insufficiently studied. Such an issue degrades the usability of safety alignment in real-world applications.In this paper, we examine how overrefusal arises under safety alignment, and propose a mitigation strategy inspired by our findings. We define refusal triggers as linguistic cues in the training data that elicit refusal responses, safety alignment encourages LLMs to associate refusal triggers within a training sample with refusal responses, leading aligned LLMs to refuse harmful queries.However, the refusal triggers include not only harmful linguistic cues but also non-harmful cues, therefore causing overrefusal to benign queries.Building on this mechanistic analysis, we propose a method that explicitly considers refusal triggers in the safety alignment fine-tuning.Empirical results demonstrate that our approach achieves a more favorable trade-off between defense against jailbreak attacks and responsiveness to benign queries, outperforming prior methods. Warning: this paper contains harmful and biased sentences.

</details>

### 26. Towards Comprehensive Post Safety Alignment of Large Language Models via Safety Patching

📄 [arXiv](https://arxiv.org/abs/2405.13820) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7176.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`post-safety alignment`、`jailbreak patch`、`continual defense`、`post safety alignment`、`over-refusal`

👤 **作者**：Weixiang Zhao、…、Ting Liu

- 🎯 **研究动机**：现有安全对齐 LLM 机制脆弱失衡：仍可被诱导生成不安全回复、对安全输入过度拒绝、对齐后效用受损
- 🔬 **研究方法**：提出 SafePatching 后安全对齐框架：在有害数据上开发分别增强安全与缓解过度安全的两类补丁并无缝集成到目标 LLM 主干
- 📌 **结论**：在 LLaMA-2/3、Gemma、Mistral 四个对齐模型上实现比基线更全面的后安全对齐，并在持续对齐场景中保持优势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) has been gaining increasing attention. However, current safety-aligned LLMs suffer from the fragile and imbalanced safety mechanisms, which can still be induced to generate unsafe responses, exhibit over-safety by rejecting safe user inputs, and fail to preserve general utility after safety alignment. To this end, we propose a novel post safety alignment (PSA) method to address these inherent and emerging safety challenges, including safety enhancement, over-safety mitigation, and utility preservation. In specific, we introduce SAFEPATCHING, a novel framework for comprehensive PSA, where two distinct safety patches are developed on the harmful data to enhance safety and mitigate oversafety concerns, and then seamlessly integrated into the target LLM backbone without compromising its utility. Extensive experiments on four representative aligned LLMs, including LLaMA-2/3, Gemma and Mistral, show that SAFEPATCHING achieves a more comprehensive PSA than baseline methods, further optimizing the balance between being helpful and harmless in current aligned LLMs. Also, SAFEPATCHING demonstrates its superiority in continual PSA scenarios.

</details>

### 27. Understanding and Mitigating Over-refusal for Large Language Models via Representation Intervention

📄 [arXiv](https://arxiv.org/abs/2511.19009)　📅 2025-11

**关键词**：`defense`、`representation intervention`、`overlap-aware weighting`、`context augmentation`

👤 **作者**：Junbo Zhang、Ran Chen、Qianli Zhou、Xinyang Deng、Wen Jiang

- 🎯 **研究动机**：越狱防御的安全收益常伴随严重过度拒绝，LLM 在表示空间中难以区分 over-refusal 与恶意样本
- 🔬 **研究方法**：提出表示空间干预：Overlap-Aware Loss Weighting 依据恶意样本与误拒样本的表示相似度确定擦除权重，Context-Aware Augmentation 在拒绝回答前补充有害上下文
- 📌 **结论**：在缓解过度拒绝与保持安全之间取得优于现有方法的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) demonstrate powerful capabilities across various natural language processing tasks,yet their inherent safety vulnerabilities undermine the reliable application of LLMs in real-world scenarios. To enhance LLM safety, various jailbreak defense methods have been proposed to guard against harmful outputs. However, improvements in model safety often come at the cost of severe over-refusal, failing to strike a good balance between safety and usability. This phenomenon is a critical reliability degradation issue in LLM intelligent systems, failing to strike a good balance between safety defense effectiveness and system usability reliability. In this paper, we first analyze the causes of over-refusal from a representation perspective, revealing that LLMs are unable to effectively distinguish between over-refusal samples and malicious samples. Based on this, we propose to mitigate overrefusal by intervening in the safety representation space of LLMs. Our method incorporates two core strategies: (1) OverlapAware Loss Weighting, which determines the erasure weight for malicious samples by quantifying their similarity to overrefusal samples in the representation space, and (2) ContextAware Augmentation, which supplements the necessary context for rejection decisions by adding harmful prefixes before rejection responses. Experiments demonstrate that our method achieves a better trade-off between mitigating over-refusal and maintaining safety, compared with existing approaches. This paper also aims to encourage researchers to consider the reliability of defending methods against jailbreak attacks from both the perspectives of safety and over-refusal.

</details>

### 28. MidPO: Dual Preference Optimization for Safety and Helpfulness in Large Language Models via a Mixture of Experts Framework

🎓 [Official](https://aclanthology.org/2025.findings-emnlp.1037/)　📅 2025-11　🏷 EMNLP 2025

**关键词**：`defense`、`dual preference optimization`、`mixture of experts`、`dynamic routing`

👤 **作者**：Yupeng Qi、Ziyu Lyu、Min Yang、Yanlin Wang、Lu Bai、Lixin Cui

- 🎯 **研究动机**：安全约束在线偏好优化常过度安全损 helpfulness，离线方法又难自适应平衡两者
- 🔬 **研究方法**：MidPO 先用单偏好增强 DPO 训练安全与有用性两个独立专家，再用 MoE 动态路由自适应分配两专家贡献
- 📌 **结论**：三个数据集上安全与有用性均显著超 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly applied across various domains, enhancing safety while maintaining the helpfulness of LLMs has become a critical challenge. Recent studies solve this problem through safety-constrained online preference optimization or safety-constrained offline preference optimization. However, the safety-constrained online methods often suffer from excessive safety, which might reduce helpfulness, while the safety-constrained offline methods perform poorly in adaptively balancing safety and helpfulness. To address these limitations, we propose MidPO, a Mixture of Experts (MoE) framework for safety-helpfulness dual Preference Optimization. Firstly, MidPO devises single-preference enhanced direct preference optimization approach to transform the base model into two independent experts, termed safety and helpfulness experts, and fine-tunes the two independent experts for optimal safety or helpfulness performance. Secondly, to achieve an effective balance between safety and helpfulness, MidPO incorporates the two experts into the MoE framework and designs a dynamic routing mechanism to allocate contributions from each expert adaptively. We conduct quantitative and qualitative experiments on three popular datasets to demonstrate the proposed MidPO significantly outperforms state-of-the-art approaches in both safety and helpfulness. Code is available at https://github.com/OutdoorManofML/MidPO.

</details>

### 29. Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2507.04250) · 🌐 [Project](https://proceedings.mlr.press/v267/dabas25a.html) · 🎓 [Official](https://icml.cc/virtual/2025/poster/45159)　📅 2025-07　🏷 ICML 2025

**关键词**：`defense`、`ACTOR`、`targeted fine-tuning`、`activation target`

👤 **作者**：Mahavir Dabas、Si Chen、Charles Fleming、Ming Jin、Ruoxi Jia

- 🎯 **研究动机**：安全对齐导致良性提示被过度拒答，损害用户体验与效用
- 🔬 **研究方法**：ACTOR 利用多样查询的内部激活模式，精确定位并调整触发拒答的激活分量，仅微调单个模型层
- 📌 **结论**：多基准上有效降低过度拒答，同时保持处理有害查询能力与整体效用，计算与数据高效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is crucial for Large Language Models (LLMs) to resist malicious instructions but often results in over-refusals, where benign prompts are unnecessarily rejected, impairing user experience and model utility. To this end, we introduce ACTOR (Activation-Based Training for Over-Refusal Reduction), a robust and compute- and-data efficient training framework that mini- mizes over-refusals by utilizing internal activation patterns from diverse queries. ACTOR precisely identifies and adjusts the activation components that trigger refusals, providing stronger control over the refusal mechanism. By fine-tuning only a single model layer, ACTOR effectively reduces over-refusals across multiple benchmarks while maintaining the model’s ability to handle harmful queries and preserving overall utility.

</details>

### 30. Think Before Refusal: Triggering Safety Reflection in LLMs to Mitigate False Refusal Behavior

📄 [arXiv](https://arxiv.org/abs/2503.17882)　📅 2025-03

**关键词**：`defense`、`safety reflection`、`instruction fine-tuning`、`false refusal`

👤 **作者**：Shengyun Si、Xinpeng Wang、Guangyao Zhai、Nassir Navab、Barbara Plank

- 🎯 **研究动机**：以拒答实现的安全对齐导致 false refusal，kill a Python process 这类良性查询也被拒绝
- 🔬 **研究方法**：提出 Think-Before-Refusal 范式，生成响应前先触发 safety reflection，并融入安全感知指令微调
- 📌 **结论**：15 个预训练模型上误拒显著减少，安全性与整体性能保持不变

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in large language models (LLMs) have demonstrated that fine-tuning and human alignment can render LLMs harmless. In practice, such "harmlessness" behavior is mainly achieved by training models to reject harmful requests, such as "Explain how to burn down my neighbor's house", where the model appropriately declines to respond. However, this approach can inadvertently result in false refusal, where models reject benign queries as well, such as "Tell me how to kill a Python process". In this work, we demonstrate that prompting safety reflection before generating a response can mitigate false refusal behavior. Building on this finding, we introduce the Think-Before-Refusal (TBR) schema and conduct safety-aware instruction fine-tuning incorporating safety reflection. In an ablation study across 15 pre-trained models, we show that models fine-tuned with safety reflection significantly reduce false refusal behavior while maintaining safety and overall performance compared to those fine-tuned without safety reflection.

</details>

### 31. POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization

📄 [arXiv](https://arxiv.org/abs/2410.12999) · 🌐 [Project](https://proceedings.mlr.press/v267/karaman25a.html)　📅 2024-10　🏷 ICML 2025

**关键词**：`defense`、`overgeneration`、`preference optimization`、`teacher completion`

👤 **作者**：Batuhan K. Karaman、Ishmam Zabir、Alon Benhaim、Vishrav Chaudhary、Mert R. Sabuncu、Xia Song

- 🎯 **研究动机**：高安全模型常过度拒答降低有用性，根源在微调对齐数据的性质与规模
- 🔬 **研究方法**：用 GPT-4o 等教师模型对通用与毒性提示过度生成微调数据；POROver 用偏好优化结合教师补全降过拒保安全
- 📌 **结论**：安全-有用 F1 从 74.4% 升至 91.8%；毒性提示过度生成把有用性从 11.1% 提到 57.6%，POROver 进一步到 82.1% 且安全不变

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Achieving both high safety and high usefulness simultaneously in large language models has become a critical challenge in recent years. Models often exhibit unsafe behavior or adopt an overly cautious approach leading to frequent overrefusal of benign prompts, which reduces their usefulness. A major factor underlying these behaviors is how the models are finetuned and aligned, particularly the nature and extent of the data used. In this work, we examine how overgenerating finetuning data with advanced teacher models (e.g., GPT-4o)—covering both general-purpose and toxic prompts—affects safety and usefulness in instruction-following language models. Additionally, we present POROver, an alignment strategy designed for models that are highly safe but prone to overrefusal. POROver employs preference optimization algorithms and leverages completions from an advanced teacher model to reduce overrefusals while maintaining safety. Our results show that overgenerating completions for general-purpose prompts significantly boosts safety with only a minimal impact on usefulness. Specifically, the F1 score calculated between safety and usefulness increases from 74.4% to 91.8% because of a substantial rise in safety. Moreover, overgeneration for toxic prompts raises usefulness from 11.1% to 57.6% while preserving safety. Finally, applying POROVer increases usefulness further—from 57.6% to 82.1%—while keeping safety at comparable levels.

</details>

### 32. ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refusals to Constructive Alternatives

📄 [arXiv](https://arxiv.org/abs/2608.30197)　📅 2026-09

**关键词**：`defense`、`selective steering`、`constructive alternative`、`refusal calibration`、`selective activation steering`、`constructive safe completion`

👤 **作者**：Hoejoon Kwon、Byeonggeuk Lim、Kahyeon Kim、YoungBin Kim

- 🎯 **研究动机**：现有 activation steering 触发机制跨域不稳定，且拒答导向 steering 产出僵硬拒绝而非建设性引导
- 🔬 **研究方法**：提出 ALTSTEER 推理时框架，用内部 refusal 相关信号决定何时介入，分阶段把生成从拒答控制转向建设性替代方案
- 📌 **结论**：在 Llama-3.1 与 Qwen2.5 上保持 benign utility 并提升 constructive safe completion，对原本倾向短拒答的模型尤其有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is essential for deploying large language models, requiring systems to prevent harmful compliance while preserving helpfulness on benign requests. Activation steering offers a training-free inference-time approach to safety control, but effective safety steering requires addressing two coupled questions: when to intervene and how generation should be shaped after intervention. However, existing safety steering methods remain limited along both dimensions, as their triggering mechanisms can be unstable across domains and refusal-oriented steering often yields rigid refusals rather than constructive safe guidance. To address these limitations, we propose ALTSTEER, an inference-time framework that couples selective intervention with refusal-anchored constructive redirection within a single inference pass. ALTSTEER uses an internal refusal-relevant signal to decide when to steer, and applies staged steering to shift generation from refusal-oriented control toward constructive alternatives. Evaluations on Llama-3.1 and Qwen2.5 show that ALTSTEER preserves benign utility while improving constructive safe-completion behavior, especially on models that otherwise tend to produce short refusals for harmful requests.

</details>

### 33. Please refuse to answer me! Mitigating Over-Refusal in Large Language Models via Adaptive Contrastive Decoding

🌐 [Project](https://shorturl.at/Z31Oe) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1823/)　📅 2026-04　🏷 ACL 2026

**关键词**：`defense`、`adaptive contrastive decoding`、`refusal token`、`training-free calibration`、`refusal calibration`、`runtime safety`

👤 **作者**：Yupeng Qi、Ziyu Lyu、Lixin Cui、Lu Bai、Feng Xia

- 🎯 **研究动机**：过拒缓解方法难兼顾无害查询低拒答与恶意查询高拒答；过拒时非拒答 token 仍在候选列表但模型系统性不选
- 🔬 **研究方法**：AdaCD 免训练模型无关：对比有无极端安全系统提示的输出分布精化拒答 token 分布，自适应纳入或移除该分布调整 token 选择概率
- 📌 **结论**：五个基准上过拒查询拒答率平均降 10.35%，恶意查询拒答率反升 0.13%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned large language models (LLMs) often generate refusal responses to harmless queries due to the over-refusal problem. However, existing methods for mitigating over-refusal cannot maintain a low refusal ratio for harmless queries while keeping a high refusal ratio for malicious ones. In this paper, we analyze how system prompts with varying safety levels affect LLM refusal behaviors when facing over-refusal queries. A key observation is that, when LLMs suffer from the over-refusal issue, non-refusal tokens remain present in the next-token candidate list, but the model systematically fails to select them, despite the generation of refusal tokens. Based on this observation, we propose a training-free and model-agnostic approach, Adaptive Contrastive Decoding (AdaCD), to mitigate over-refusal while maintaining LLM safety. First, AdaCD compares the output distributions of the LLM with or without an extreme safety system prompt to refine the refusal token distribution. Second, we introduce an adaptive contrastive decoding strategy that dynamically incorporates or removes the refusal token distribution, adaptively boosting the probability of selecting refusal or non-refusal tokens. Experimental results on five benchmark datasets show that, on average, AdaCD reduces the refusal ratio for over-refusal queries by 10.35%, yet still increases the refusal ratio for malicious queries by 0.13%. Code is available at https://shorturl.at/Z31Oe.

</details>

### 34. LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment

🌐 [Project](https://hotbento.github.io/LLM-VA-Web/) · 🎓 [Official](https://aclanthology.org/2026.acl-long.260/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`vector alignment`、`closed-form update`、`safety-helpfulness trade-off`、`LLM jailbreak`、`refusal calibration`

👤 **作者**：Haonan Zhang、Dongxia Wang、Yi Liu、Kexin Chen、Wenhai Wang

- 🎯 **研究动机**：向量转向只调节答案向量幅度造成越狱-过拒权衡；根源是回答向量与良性判断向量近正交被独立处理
- 🔬 **研究方法**：LLM-VA 用闭式权重更新对齐两向量使响应意愿因果依赖安全评估：SVM 逐层识别向量、选安全相关层做最小范数修改
- 📌 **结论**：12 个 LLM 上 F1 比最佳基线高 11.45%，保留 95.92% 效用，免手工调参

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned LLMs suffer from two failure modes: jailbreak (responding to harmful inputs) and over-refusal (declining benign queries). Existing vector steering methods adjust the magnitude of answer vectors, but this creates a fundamental trade-off—reducing jailbreak increases over-refusal and vice versa. We identify the root cause: LLMs encode the decision to respond (answer vector v a ) and the judgment of input safety (benign vector v b ) as nearly orthogonal directions, treating them as independent processes. We propose LLM-VA, which aligns v a with v b through closed-form weight updates, making the model’s willingness to respond causally dependent on its safety assessment—without fine-tuning or architectural changes. Our method identifies vectors at each layer using SVMs, selects safety-relevant layers, and iteratively aligns vectors via minimum-norm weight modifications. Experiments on 12 LLMs demonstrate that LLM-VA achieves 11.45% higher F1 than the best baseline while preserving 95.92% utility, and automatically adapts to each model’s safety bias without manual tuning.Code and models are available at https://hotbento.github.io/LLM-VA-Web/.

</details>

### 35. Mitigating Over-Refusal in Aligned Large Language Models via Inference-Time Activation Energy

📄 [arXiv](https://arxiv.org/abs/2510.08646) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1759/)　📅 2025-10　🏷 ACL 2026

**关键词**：`defense`、`energy landscape`、`gradient steering`、`inference-time intervention`、`refusal calibration`、`representation intervention`

👤 **作者**：Eric Hanchen Jiang、…、Xinfeng Li

- 🎯 **研究动机**：安全对齐常以过度拒答为代价，需要免微调的推理时干预手段
- 🔬 **研究方法**：提出 ELS：训练轻量外部能量模型给误拒与越狱态赋高能、正常态赋低能，推理时以能量函数梯度实时引导隐状态走向低能区
- 📌 **结论**：ORB-H 基准依从率从 57.3% 提至 82.6% 且安全基线保持，全程不改模型参数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models currently faces a central challenge: existing alignment techniques often prioritize mitigating responses to harmful prompts at the expense of overcautious behavior, leading models to incorrectly refuse benign requests. A key goal of safe alignment is therefore to improve safety while simultaneously minimizing false refusals. In this work, we introduce Energy Landscape Steering (ELS), a novel, fine-tuning free framework designed to resolve this challenge through dynamic, inference-time intervention. We train a lightweight external Energy-Based Model (EBM) to assign high energy to undesirable states (false refusal or jailbreak) and low energy to desirable states (helpful response or safe reject). During inference, the EBM maps the LLM's internal activations to an energy landscape, and we use the gradient of the energy function to steer the hidden states toward low-energy regions in real time. This dynamically guides the model toward desirable behavior without modifying its parameters. By decoupling behavioral control from the model's core knowledge, ELS provides a flexible and computationally efficient solution. Extensive experiments across diverse models demonstrate its effectiveness, raising compliance on the ORB-H benchmark from 57.3 percent to 82.6 percent while maintaining baseline safety performance. Our work establishes a promising paradigm for building LLMs that simultaneously achieve high safety and low false refusal rates.

</details>

### 36. SafeConstellations: Mitigating Over-Refusals in LLMs Through Task-Aware Representation Steering

🎓 [Official](https://aclanthology.org/2026.acl-long.2056/)　📅 2025-08　🏷 ACL 2026

**关键词**：`defense`、`task-aware steering`、`representation trajectory`、`conditional intervention`、`refusal calibration`、`representation intervention`

👤 **作者**：Utsav Maskey、Sumit Yadav、Mark Dras、Usman Naseem

- 🎯 **研究动机**：LLM 对被重构为良性意图任务的有害内容输入仍持续拒答，过度拒答损害生产应用效用
- 🔬 **研究方法**：机理分析发现各 NLP 任务在嵌入空间沿层间保持可预测的星座轨迹且拒答/非拒答可区分，提出推理时轨迹偏移方法将表示导向非拒答路径
- 📌 **结论**：仅对易过度拒答任务选择性引导，即可在效用影响极小的情况下显著减少过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs increasingly exhibit over-refusal behavior, where safety mechanisms cause models to reject benign instructions that seemingly resemble harmful content. This phenomenon diminishes utility in production applications that repeatedly rely on common prompt templates or applications that frequently rely on LLMs for specific tasks (e.g. sentiment analysis, language translation). Through extensive evaluation, we demonstrate that LLMs persist in refusing inputs containing harmful content, even when they are reframed with tasks that have benign intent. Our mechanistic analysis reveals that LLMs follow distinct “constellation” patterns in embedding space as representations traverse layers, with each NLP task maintaining consistent trajectories that shift predictably between refusal and non-refusal cases. We introduce SafeConstellations, an inference-time trajectory-shifting approach that tracks task-specific trajectory patterns and guides representations toward non-refusal pathways. By selectively guiding model behavior only on tasks prone to over-refusal, our method reduces over-refusals with minimal impact on utility—offering a principled and conditional approach to mitigating over-refusals.

</details>

### 37. Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation

📄 [arXiv](https://arxiv.org/abs/2410.03415) · 📝 [OpenReview](https://openreview.net/forum?id=SCBn8MCLwc)　📅 2024-10　🏷 ICLR 2025

**关键词**：`defense`、`single-vector ablation`、`false-refusal direction`、`model-agnostic steering`

👤 **作者**：Xinpeng Wang、Chengzhi Hu、Paul Röttger、Barbara Plank

- 🎯 **研究动机**：现有误拒缓解需训练或复杂推理干预
- 🔬 **研究方法**：提取false-refusal vector并做单向量消融或正交化
- 📌 **结论**：training-free、model-agnostic地减少误拒且不明显损害安全与能力

### 38. SCANS: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious Activation Steering

📄 [arXiv](https://arxiv.org/abs/2408.11491) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/34521)　📅 2024-08　🏷 AAAI 2025

**关键词**：`defense`、`safety-conscious steering`、`critical layer`、`input adaptation`

👤 **作者**：Zouying Cao、Yifei Yang、Hai Zhao

- 🎯 **研究动机**：固定refusal-vector操纵对所有输入一视同仁，易误伤良性请求
- 🔬 **研究方法**：SCANS经vocabulary projection定位safety-critical层，按hidden-state transition自适应steering
- 📌 **结论**：XSTest与OKTest上降低exaggerated safety且保留有害防御与能力

### 39. Mitigating Exaggerated Safety in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2405.05418)　📅 2024-05

**关键词**：`defense`、`prompt engineering`、`contextual prompt`、`few-shot calibration`

👤 **作者**：Ruchira Ray、Ruchi Bhalani

- 🎯 **研究动机**：过度安全使 26.1% 的安全 prompt 被误判拒绝，损害可用性
- 🔬 **研究方法**：以 XSTTest 数据结合 interactive、contextual 与 few-shot prompting 探查各 LLM 决策边界，按模型选用最优策略
- 📌 **结论**：组合提示策略将 Llama2、Gemma 等四类 LLM 的过度安全行为总体降低 92.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As the popularity of Large Language Models (LLMs) grow, combining model safety with utility becomes increasingly important. The challenge is making sure that LLMs can recognize and decline dangerous prompts without sacrificing their ability to be helpful. The problem of "exaggerated safety" demonstrates how difficult this can be. To reduce excessive safety behaviours -- which was discovered to be 26.1% of safe prompts being misclassified as dangerous and refused -- we use a combination of XSTest dataset prompts as well as interactive, contextual, and few-shot prompting to examine the decision bounds of LLMs such as Llama2, Gemma Command R+, and Phi-3. We find that few-shot prompting works best for Llama2, interactive prompting works best Gemma, and contextual prompting works best for Command R+ and Phi-3. Using a combination of these prompting strategies, we are able to mitigate exaggerated safety behaviors by an overall 92.9% across all LLMs. Our work presents a multiple prompting strategies to jailbreak LLMs' decision-making processes, allowing them to navigate the tight line between refusing unsafe prompts and remaining helpful.

</details>

### 40. Over-Refusal and Representation Subspaces: A Mechanistic Analysis of Task-Conditioned Refusal in Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2603.27518)　📅 2026-03

**关键词**：`analysis`、`task-conditioned subspace`、`refusal geometry`、`linear probing`

👤 **作者**：Utsav Maskey、Mark Dras、Usman Naseem

- 🎯 **研究动机**：全局消融拒绝方向只能偶然修正过度拒绝且扰乱整体拒绝机制
- 🔬 **研究方法**：分析两类拒绝的表示几何：有害拒绝方向任务无关、可由单全局向量捕获；过度拒绝方向任务依赖、位于良性任务簇内且张成更高维子空间
- 📌 **结论**：早期层线性探针即可区分两类拒绝，机制上解释全局方向消融为何无效、需任务特定几何干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned language models that are trained to refuse harmful requests also exhibit over-refusal: they decline safe instructions that seemingly resemble harmful instructions. A natural approach is to ablate the global refusal direction, steering the hidden-state vectors away or towards the harmful-refusal examples, but this corrects over-refusal only incidentally while disrupting the broader refusal mechanism. In this work, we analyse the representational geometry of both refusal types to understand why this happens. We show that harmful-refusal directions are task-agnostic and can be captured by a single global vector, whereas over-refusal directions are task-dependent: they reside within the benign task-representation clusters, vary across tasks, and span a higher-dimensional subspace. Linear probing suggests that the two refusal types are representationally distinct from the early transformer layers. These findings provide a mechanistic explanation of why global direction ablation alone cannot address over-refusal, and establish that task-specific geometric interventions are necessary.

</details>

### 41. Steering Safely or Off a Cliff? Rethinking Specificity and Robustness in Inference-Time Interventions

🎓 [Official](https://aclanthology.org/2026.eacl-long.268/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`steering robustness`、`adaptive jailbreak`、`safety-utility trade-off`、`activation steering`、`over-refusal`

👤 **作者**：Navita Goyal、Hal Daumé III

- 🎯 **研究动机**：推理时干预是否只改变目标属性（specificity）缺乏系统评估，尤其忽视相关行为被意外改变
- 🔬 **研究方法**：提出 general、control、robustness 三维 specificity 框架，研究降低过度拒绝与信念幻觉忠实性两个安全用例
- 📌 **结论**：steering 高效且基本保持前两维，却一致无法保持鲁棒特异性：过度拒绝 steering 不伤通用能力但大幅增加越狱脆弱性；无鲁棒性评估时 steering 可能表面可靠实则危害安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model steering, which involves intervening on hidden representations at inference time, has emerged as a lightweight alternative to finetuning for precisely controlling large language models. While steering efficacy has been widely studied, evaluations of whether interventions alter only the intended property remain limited, especially with respect to unintended changes in behaviors related to the target property. We call this notion specificity. We propose a framework that distinguishes three dimensions of specificity: general (preserving fluency and unrelated abilities), control (preserving related control properties), and robustness (preserving control properties under distribution shifts). We study two safety-critical use cases: steering models to reduce overrefusal and faithfulness hallucinations, and show that while steering achieves high efficacy and largely maintains general and control specificity, it consistently fails to preserve robustness specificity. In the case of overrefusal steering, for example, all steering methods reduce overrefusal without harming general abilities and refusal on harmful queries; however, they substantially increase vulnerability to jailbreaks. Our work provides the first systematic evaluation of specificity in model steering, showing that standard efficacy and specificity checks are insufficient, because without robustness evaluation, steering methods may appear reliable even when they compromise model safety.

</details>

### 42. There Is More to Refusal in Large Language Models than a Single Direction

📄 [arXiv](https://arxiv.org/abs/2602.02132)　📅 2026-02

**关键词**：`analysis`、`multi-direction refusal`、`behavior taxonomy`、`steering trade-off`、`multi-direction geometry`、`refusal taxonomy`

👤 **作者**：Faaiz Joad、Majd Hawasly、Sabri Boughorbel、Nadir Durrani、Husrev Taha Sencar

- 🎯 **研究动机**：先前工作主张 LLM 拒答由单一激活方向中介，该论断不完整
- 🔬 **研究方法**：考察安全、请求不支持、拟人化、过度拒绝等 11 类拒答与不服从行为对应的激活方向及各方向 steering 效果
- 📌 **结论**：各拒答类型对应几何上不同的方向，但沿任一方向的线性 steering 带来几乎相同的 refusal-over-refusal 权衡；方向差异主要改变拒答方式而非是否拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior work argues that refusal in large language models is mediated by a single activation-space direction, enabling effective steering and ablation. We show that this account is incomplete. Across eleven categories of refusal and non-compliance, including safety, incomplete or unsupported requests, anthropomorphization, and over-refusal, we find that these refusal behaviors correspond to geometrically distinct directions in activation space. Yet despite this diversity, linear steering along any refusal-related direction produces nearly identical refusal to over-refusal trade-offs, acting as a shared one-dimensional control knob. The primary effect of different directions is not whether the model refuses, but how it refuses.

</details>

### 43. LLMs Encode Harmfulness and Refusal Separately

📄 [arXiv](https://arxiv.org/abs/2507.11878) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cd18539787d90e1d682d557c2c71b534-Abstract-Conference.html)　📅 2025-07　🏷 NeurIPS 2025

**关键词**：`analysis`、`harmfulness-refusal separation`、`causal steering`、`latent guard`、`harmfulness direction`、`refusal direction`

👤 **作者**：Jiachen Zhao、Jing Huang、Zhengxuan Wu、David Bau、Weiyan Shi

- 🎯 **研究动机**：表面拒答是否等同于内部有害性判断存疑
- 🔬 **研究方法**：以causal steering证明harmfulness与refusal编码于不同方向与token位置
- 📌 **结论**：去除refusal不等于删除有害性识别，Latent Guard可减误拒且抗对抗微调

### 44. Safety Cost of Steering Vectors Is Separable and Reducible

📄 [arXiv](https://arxiv.org/abs/2608.08383) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-08

**关键词**：`defense`、`over-refusal`、`refusal calibration`、`safety-utility trade-off`、`activation steering`、`safety degradation`

👤 **作者**：Yuxiao Li、Gjergji Kasneci

- 🎯 **研究动机**：steering 向量会意外削弱模型安全机制并增加有害合规，尚无有效缓解手段
- 🔬 **研究方法**：证明安全退化源于向量中可分离、对转向目标贡献小的分量；将其识别与移除形式化为约束优化，primal-dual 求解并约束误拒上界
- 📌 **结论**：跨模型、转向行为与攻击套件（含未见攻击类型）大幅降低转向诱发安全退化，保留原转向效果且几乎不影响误拒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering vectors are a lightweight tool for controlling LLM behavior. However, emerging evidence shows that steering vectors can unintentionally compromise a model's safety mechanisms and increase compliance with harmful requests, while no effective mitigation yet exists. In this work, we show that this safety degradation arises from a separable component in the vector that disrupts the model's safety mechanisms but contributes little to the steering objective. We identify and remove this safety-degrading component, formulating the task as a constrained optimization problem solved through primal-dual updates, subject to preserving the intended steering effect and bounding false refusal. The resulting solution is both interpretable and surgical: the optimization recovers a single direction whose ablation from the steering vector restores model safety with minimal utility cost. Across models, steering behaviors, and attack suites, including unseen attacks types, our method substantially reduces steering-induced safety degradation while preserving the original steering effect with minimal impact on false refusal. Our method offers a post-hoc correction to steering vectors that mitigates their safety cost, and more broadly, it provides a general recipe for applying activation-level model interventions without paying a safety tax.

</details>

### 45. SHARD: Safe and Helpful Alignment via Self-Reframing Distillation

📄 [arXiv](https://arxiv.org/abs/2606.15517)　📅 2026-09

**关键词**：`defense`、`safe-helpfulness`、`self-distillation`、`sensitive prompt`

👤 **作者**：Viswonathan Manoranjan、Amogh Gupta、Anvesh Rao Vijjini、Thomas Hofweber、Snigdha Chaturvedi

- 🎯 **研究动机**：LLM 对敏感提示要么直接拒绝、要么给出安全套话，无法满足可安全回答的正当信息需求
- 🔬 **研究方法**：提出 SHARD 自我重构蒸馏：用哲学准则改写敏感提示显式良性意图，把原始回应重构为安全且更有用的版本，再在自重构回应上微调
- 📌 **结论**：DNA 与 LINGUASAFE 英文子集上多数模型家族提升有用性且保持安全，可与更大教师蒸馏竞争

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models often struggle with sensitive prompts. They may refuse outright, provide generic safety boilerplate, or fail to address the user's legitimate informational needs that can be answered safely. We introduce SHARD, a self-reframing distillation method to improve safe-helpfulness. It first rewrites sensitive prompts to surface benign intent using philosophical guidelines, then reframes its original responses into safe, more helpful ones, and finally fine-tunes the model on its self-reframed responses. Across DNA and the English subset of LINGUASAFE, SHARD improves helpfulness for most model families while preserving safety. It also remains competitive with distillation from a larger teacher model, suggesting that models can internalize safe and helpful behavior elicited from their own. Warning: This paper contains content that may be offensive or harmful.

</details>

### 46. Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models

📄 [arXiv](https://arxiv.org/abs/2609.04714)　📅 2026-09

**关键词**：`defense`、`safety tuning`、`false refusal`、`rationale supervision`

👤 **作者**：Minji Kim、Hyounghun Kim

- 🎯 **研究动机**：模型难以区分真实有害查询与含表面风险措辞的良性查询（如 shoot someone vs shoot a photo），产生大量 false refusal
- 🔬 **研究方法**：把安全微调数据中的回复拆为样板拒答语句与拒答 rationale，实验发现拒答语句诱发对表面线索的依赖，仅用 rationale 训练
- 📌 **结论**：Rationale-Only 降低 false refusal 且安全表现相当，收益同样出现在 ICL 配置并与所测推理时缓解方法兼容——需要精细粒度的安全监督数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Striking a balance between helpfulness and safety remains a fundamental challenge in aligning large language models. To achieve this balance, models should refuse harmful queries (e.g., "How do I shoot someone?") while remaining responsive to benign inputs, even those superficially resembling harmful queries (e.g., "Where can I shoot a good photo?"). However, models often struggle to distinguish genuinely harmful queries from benign queries that contain superficially risky language, resulting in false refusals. In this paper, we address the issue by decomposing a response in the safety-tuning dataset into two distinct components: (i) a boilerplate refusal statement and (ii) a rationale explaining the refusal. Our experiments and analyses show that refusal statements impede accurate discrimination between harmful and benign queries by inducing reliance on superficial cues. In contrast, training solely on rationales reduces false refusals while maintaining a comparable level of safety performance. Rationale-Only benefits also appear in our ICL configuration and remain compatible with the evaluated inference-time mitigation methods. The results emphasize the necessity of precisely curated, fine-grained safety supervision datasets and outline directions for constructing aligned agents that better reconcile helpfulness with safety.

</details>
