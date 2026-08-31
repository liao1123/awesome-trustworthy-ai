# 专用领域与多语言 Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究通用 guard model 在专业术语、行业法规、儿童等特定用户群体、人际关系操纵、低资源语言、code-switching 和地区文化规范下的迁移失败，并构建对应 taxonomy、数据、benchmark 与专用审核模型。这里的目标不是简单翻译英文 safety dataset 或沿用通用风险标签，而是让风险定义来自行业规则、角色关系、发展心理、当地专家与法规，并同时检查领域能力、通用安全能力和未见语言、年龄线索或 policy 的泛化。

## 研究脉络

- **通用 taxonomy 的缺口：** 英文中心的 harm category 无法覆盖金融合规、医疗建议、法律要求和地区敏感语义，专业术语还会改变原本的安全决策边界。
- **用户群体适配：** Child-facing system 需要识别显式年龄与隐含儿童表达，并在多轮交互中维持发展阶段适当的解释、边界和求助指引，不能只复用成人 harmful-content refusal。
- **角色敏感决策：** 人际关系风险不能把同一主题统一拒绝；guard 需要区分操纵者的有害请求与受害者的求助，并累计多轮中逐步显现的 workflow 风险。
- **数据本地化：** PolyGuard 等工作扩大语言覆盖，SEA-SafeguardBench、UbuntuGuard 与 IndicGuard 进一步用 native author、地区专家和本地法规替代纯机器翻译。
- **Policy-grounded moderation：** ML-Bench&Guard 和 FinGuard 从司法辖区或行业监管文本抽取规则，使 guard 能解释违反了哪条可变 policy，而不只输出通用 harmful label。
- **训练与效率：** MrGuard 用 multilingual reasoning 与 curriculum GRPO，CHILLGuard 用 model-aware preference alignment，LionGuard 2 证明高质量本地数据配合轻量 classifier 也可实际部署。
- **模块化专家：** GuardZoo 的分析显示单一 guard 会受到跨领域 task interference，RouteGuard 因而先识别 threat domain 再路由到 specialized expert。

## 专业行业 Guardrail

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI | detection、psychological-safety guard、expert correction、local judge | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.24899) | [Model](https://huggingface.co/keidolabs/aipsy-judge-1.0) | 针对通用 frontier judge 在心理健康、AI companion 与 coaching 对话中共享宽松 disposition 和供应商 post-training 盲点，论文以心理学家逐指标校正目标微调本地 Gemma judge；它捕获 92% crisis case 并有意偏向假阳性，但作者也明确该目标目前只由单一专家知情、尚不能替代多评审效度验证。 |
| 2026&#8209;08 | RxGuard: Knowledge-Guided Safety Guardrails for Medication Recommendation | defense、medication safety、knowledge guardrail、high-stakes recommendation | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3818849) | 暂未公开 | RxGuard 把药物知识约束接入推荐流程，在输出前识别禁忌、相互作用等风险，为高后果医疗推荐增加可核验安全边界。 |
| 2026&#8209;07 | EVADE-Bench: Multimodal Benchmark for Evaluating and Enhancing Evasive Content Detection ↗ | benchmark、e-commerce guardrail、Chinese evasion、industry policy | SIGIR 2026 | [Official](https://doi.org/10.1145/3805712.3808579) · [arXiv](https://arxiv.org/abs/2505.17654) | [Code](https://github.com/koenshen/EVADE-Bench) · [Dataset](https://huggingface.co/datasets/koenshen/EVADE-Bench) | 针对通用内容安全集不覆盖中文电商中拆词、委婉语、图像裁剪等行业规避策略，EVADE-Bench 由专家整理 16,794 个文本／图像样本和六类违规规则；26 个模型的失败及规则增强实验为电商专用 guardrail 提供诊断基线。 |
| 2026&#8209;05 | Triaging Threats to Specialized Guardrails | defense、router-expert guard、threat triage、task interference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.30693) | 暂未公开 | 针对不同风险领域的 decision boundary 难压进单一 guard，论文先以 32,460 条人工标注构建 GuardZoo，再让 RouteGuard 将会话路由给 threat-specific expert；结果改善细粒度和 out-of-domain 检测并便于增加新专家。 |
| 2026&#8209;05 | FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions | detection、financial compliance、regulation-grounded data、self-play RL | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29427) | 暂未公开 | 针对通用 harm taxonomy 忽略金融监管违规，论文直接从中国金融法规归纳 risk taxonomy、构建 FinGuard-Bench，并用 SFT 与 self-play RL 训练 FinGuard；结果提升 query/response 合规检测且可读取未见机构 policy。 |
| 2026&#8209;03 | CRADLE Bench: A Clinician-Annotated Benchmark for Multi-Faceted Mental Health Crisis and Safety Risk Detection | benchmark、crisis guardrail、clinical annotation、temporal risk | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.73/) | 暂未公开 | 针对 user-model interaction 中危机信号漏检会造成严重后果；CRADLE Bench 依临床标准覆盖自杀意念、性侵、家暴和虐待等七类风险并加入 temporal label；结果提供多维及时 detection 的专门 guardrail 基线。 |
| 2026&#8209;03 | ExpGuard: LLM Content Moderation in Specialized Domains | defense、domain-specific moderation、expert annotation、adversarial jargon | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10007009) · [OpenReview](https://openreview.net/forum?id=t5cYJlV6aJ) · [arXiv](https://arxiv.org/abs/2603.02588) | [Code](https://github.com/brightjade/ExpGuard) | 针对通用 guard 在金融、医疗和法律术语及 adversarial content 上失效，论文构建由领域专家校验的 ExpGuardMix 并训练专用模型；结果在保留通用安全能力时提高专业 prompt 与 response 分类。 |
| 2026&#8209;03 | SafeCRS: Personalized Safety Alignment for LLM-Based Conversational Recommender Systems | defense、personalized safety、conversational recommender、safe RL | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817807) · [arXiv](https://arxiv.org/abs/2603.03536) | [Code](https://github.com/xxyyffyeah/SafeCRS) | SafeCRS 将创伤、自伤和恐惧等个体敏感约束纳入推荐训练与奖励，在维持推荐质量时显著减少对特定用户的安全违规。 |
| 2026&#8209;02 | BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards | defense、ad compliance、multimodal mismatch、policy reward | AAAI 2026 | [Official](https://ojs.aaai.org/index.php/AAAI/article/view/40914) · [arXiv](https://arxiv.org/abs/2602.18193) | 暂未公开 | 针对商业短视频广告的夸大画面、违规表述和字幕-语音错配无法由社区安全类别覆盖，论文以规则生成 ICoT 数据并用 policy-aligned reward 训练；结果改善行业审核的一致性与跨样式泛化。 |

## 社会关系与角色敏感 Guardrail

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations | benchmark、companion safety、relational boundary、context-aware guard | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25377) | [Dataset](https://github.com/HanMeng2004/CompanionHarm) | 论文把 AI companion harm 操作化为 13 类关系性与上下文性行为，并保留三名标注者的逐人标签来审计分歧；多轮上下文虽提高检测，却仍暴露 severity calibration 和 relational-boundary interpretation 缺口，为专门的有状态 companion guard 提供真实对话基准。 |
| 2026&#8209;08 | HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations | defense、relationship manipulation、role-sensitive guard、multi-turn risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25340) | [Code](https://github.com/noobasuna/hrguard.git) | HRGuard 为人际关系操纵建立专用双侧 policy：阻断攻击者借 AI 编排操纵行为，同时允许受害者获得保护性建议；其生成前与有状态生成后双 gate 在八个模型上优于通用安全提示和三种通用 guard，显示该风险需要角色敏感、跨轮累计的专门决策边界。 |

## 儿童交互安全与年龄适配

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha | benchmark、child-facing safety、youth register、crisis-risk guardrail | ACM FAccT 2026 | [Official](https://doi.org/10.1145/3805689.3806522) · [arXiv](https://arxiv.org/abs/2608.20345) | 暂未公开 | 针对成人中心 safety taxonomy 无法保证 therapy bot 正确处理 Gen Alpha 的反讽、弱化表达与快速语义漂移，论文建立临床核验的表达和多轮对话 benchmark；模型虽理解 76%–82% 词汇，临床风险校准仅为 64%–72%，多种模式叠加时漏检率达 94%，且轻量 mitigation 失败，为年龄与语体专用的有状态 crisis guard 提供了明确评测边界。 |
| 2026&#8209;05 | The Age of Curiosity Meets the Age of AI: Benchmarking Child Safety in Large Language Models | benchmark、child-facing safety、age cues、multi-turn degradation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.25510) | [Dataset & Models](https://huggingface.co/collections/sameearif/kidbench) | 针对通用安全评测不检查 7–11 岁儿童所需的发展阶段适当性，论文以十类风险、显式或隐式年龄线索和 child-actor 多轮模拟构建 KIDBench，并发布 KIDGuardLlama 与 KIDLlama；结果显示年龄提示能改善表现，但跨语言文化不均衡且多轮质量会下降 6%–24%。 |

## 多语言与文化本地化模型

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator ↗ | tool、12-language moderation、multilingual guard data、cross-language robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27548) | [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset) | 针对单语言 guard 难在同一部署组件中覆盖图文输入、回答和自定义规则，论文发布支持 12 种语言的 4B moderator 及多语言安全训练集，并联合评测跨语言鲁棒性、误报、policy following 与延迟；它证明紧凑统一 guard 可扩大语言覆盖，但该结果不等同于已验证每种语言的文化本地化。 |
| 2026&#8209;06 | IndicGuard: A Multilingual Safety Guard Model and Dataset for Indic Languages | defense、Indic languages、regional harm、cross-lingual transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22841) | 暂未公开 | 针对英文中心 guard 忽略南亚社会文化风险，论文以十种 Indic languages 构建本地语境与 jailbreak 数据并微调 4B guard；结果超过 CultureGuard，且能迁移到训练时未覆盖的低资源 Indic language。 |
| 2026&#8209;06 | CHILLGuard: Towards Fine-Grained Chinese LLM Safety Guardrail with Scalable Data Construction and Model-aware Preference Alignment | defense、Chinese moderation、fine-grained taxonomy、preference alignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.15396) | [Repository](https://github.com/cswbyu/CHILLGuard)（当前仅 README） | 针对多语言 guard 缺少中国法规、文化语境和细粒度类别，论文建立 5 个 macro 与 31 个 micro category，并用检索增强数据生成、投票校准和 model-aware DPO 训练；结果形成面向中文场景的专用 guard 与 benchmark。 |
| 2026&#8209;05 | ML-Bench&Guard: Policy-Grounded Multilingual Safety Benchmark and Guardrail for Large Language Models | defense、regional regulation、multilingual policy、diffusion LLM | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.00689) | 暂未公开 | 针对翻译型 benchmark 无法表达不同司法辖区的规则，论文从地区法规构建覆盖 14 种语言的 ML-Bench，并训练 1.5B 快速分类与 7B policy explanation 两类 ML-Guard；结果提升跨语言的 regulation-aware moderation。 |
| 2026&#8209;03 | Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space ↗ | defense、multilingual activation guard、safety direction、cross-lingual transfer | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.139/) | 暂未公开 | 针对英语训练的 safety classifier 能否读取非英语内部风险信号缺少机制证据，论文在单层 activation 中提取 safe/unsafe direction 并以冻结线性 probe 监测；结果跨 16 种非英语语言仍保持较强判别，说明共享表示可支持低开销跨语言 guard。 |
| 2026&#8209;03 | FanarGuard: A Culturally-Aware Moderation Filter for Arabic Language Models | defense、Arabic guardrail、cultural alignment、human annotation | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.368/) | 暂未公开 | 针对通用 safety filter 忽略 Arabic cultural norm；FanarGuard 用 46.8 万组英阿 prompt-response 训练 safety 与文化双目标 moderator，并建立千余条人工 benchmark；结果保持通用安全表现同时提高文化语境判断。 |
| 2026&#8209;02 | SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia | defense、Southeast Asian languages、agentic data generation、cultural safety | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.141/) · [arXiv](https://arxiv.org/abs/2602.01618) | 暂未公开 | 针对机器翻译数据遗漏东南亚本地价值、法规和伤害语境，论文用 agentic pipeline 生成地区原生安全数据并训练 SEA-Guard；结果提高 culturally sensitive 内容检测且保持通用安全性能。 |
| 2025&#8209;07 | LionGuard 2: Building Lightweight, Data-Efficient & Localised Multilingual Content Moderators | tool、Singapore localization、ordinal classifier、production moderation | EMNLP 2025 System Demonstrations | [Official](https://aclanthology.org/2025.emnlp-demos.20/) · [arXiv](https://arxiv.org/abs/2507.15339) | 暂未公开 | 针对全球多语言系统忽略新加坡语言变体且大模型审核成本高，论文以 multilingual embedding 和 multi-head ordinal classifier 覆盖英语、中文、马来语及部分泰米尔语；结果形成已在新加坡政府使用的轻量审核器。 |
| 2025&#8209;05 | OMNIGUARD: An Efficient Approach for AI Safety Moderation Across Languages and Modalities | defense、language-agnostic representation、modality-agnostic classifier、low-resource input | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.23856) | [Code](https://github.com/vsahil/OmniGuard) | 针对低资源语言和非文本 prompt 利用 guard 与主模型泛化不匹配绕过审核，论文在模型内部寻找跨语言/模态对齐 representation 并训练通用 classifier；结果在多语言、图像和音频检测上提升且复用生成 embedding 降低开销。 |
| 2025&#8209;04 | MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety | defense、multilingual reasoning、curriculum GRPO、code-switching | EMNLP 2025 Main | [Official](https://aclanthology.org/2025.emnlp-main.1392/) · [arXiv](https://arxiv.org/abs/2504.15241) | 暂未公开 | 针对 multilingual safety data 稀缺及 code-switching、低资源干扰会改变判断，论文结合合成数据、SFT 和 curriculum GRPO 训练解释型 guard；结果在 seen 与 unseen language 上均超过对比基线并保持判断稳定。 |
| 2025&#8209;04 | PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages | tool、17-language moderation、PolyGuardMix、prompt-response labeling | COLM 2025 | [Official](https://openreview.net/forum?id=wbAWKXNeQ4) · [arXiv](https://arxiv.org/abs/2504.04377) | 暂未公开 | 针对既有 moderation 只覆盖少数语言和有限风险定义，论文以 1.91M 条 PolyGuardMix 训练 17-language guard，并发布 29K PolyGuardPrompts；结果统一判断 prompt harmfulness、response harmfulness 与 refusal。 |

## 文化与低资源语言 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | UbuntuGuard: A Culturally-Grounded Policy Benchmark for Equitable AI Safety in African Languages | benchmark、African languages、expert-authored policy、cultural alignment | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.1663/) · [arXiv](https://arxiv.org/abs/2601.12696) | 暂未公开 | 针对英文 benchmark 高估非洲低资源语言的实际安全，论文由 155 名领域专家编写 adversarial query、context-specific policy 和参考响应；结果显示 cross-lingual transfer 只能部分覆盖本地语境，dynamic guard 也仍难完全本地化。 |
| 2025&#8209;12 | SEA-SafeguardBench: Evaluating AI Safety in SEA Languages and Cultures | benchmark、Southeast Asian languages、native annotation、cultural harm | 未确认（arXiv Comments：Under review） | [arXiv](https://arxiv.org/abs/2512.05501) | 暂未公开 | 针对翻译英文样本无法覆盖地区政治表达与 misinformation，论文构建八种东南亚语言、含 general、in-the-wild 和 generation 子集的人审 benchmark；结果显示现有 LLM 与 guard 在本地文化风险上明显落后于英文表现。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | FraudBench: Stress-Testing Policy-Grounded Banking Agents Against Adaptive Fraud | analysis、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18136) | 暂未公开 | 对话智能体如今通过工具代表终端用户行动，同时能够访问客户数据库和内部政策文档，而来电者仅通过对话就可能触及这些资源；我们提出 FraudBench，一个建立在 $τ^2$-bench 双控制框架和 $τ$-Knowledge 银行环境上的可执行基准；四个智能体在 107 项评分任务上的初步单次评估显示，攻击安全率介于 49% 和 65% 之间，钱骡欺诈和第一方欺诈是跨模型最常见的弱点。 |
| 2026&#8209;08 | Beyond "I Can't Help With That": How Child Safety Experts Evaluate AI Chatbot Safety | analysis、adversarial robustness、specialized guardrail、domain policy | 未确认（arXiv Comments：AIES 2026） | [arXiv](https://arxiv.org/abs/2608.07902) | 暂未公开 | 研究访谈 19 名直接服务高风险青少年的社工、治疗师和心理学家，让其评议 chatbot 在真实危险情境中的响应；结果指出单看拒答或表面有害文本会漏掉实际伤害，并形成把一线专家判断纳入儿童安全评测的具体建议。 |
| 2026&#8209;03 | Safety of Large Language Models Beyond English: A Systematic Literature Review of Risks, Biases, and Safeguards ↗ | survey、multilingual safety、evidence gap、localized safeguards | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.44/) | 暂未公开 | 针对英语安全结论被直接外推到其他语言却缺少系统证据的问题，综述统一整理非英语 LLM 的风险、偏差、评测和 safeguard 文献；结果发现所引安全数据集有 78.5% 仅含英语，并以公开 dashboard 显示语言、文化和资源覆盖仍高度不均。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models | detection、high-risk deployment、specialized guardrail、domain policy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16852) | 暂未公开 | 已部署语言模型中的监管合规性监控越来越多地作为法律和审计控制来实施，根据涵盖数据保护、医疗保健、金融监管和平台政策的书面规则检查模型输出；我们证明这种情况在当前类别的合规性检测器中失败，我们将这种失败称为规则盲目性；一个专门构建的基准测试跨越两种场景的两个规则，这样既不能单独预测标签，也不能在先前基准测试没有排除的设计下确认失败，并表明逐步推理，而不是我们测试的任何快速检测器，才是逃脱它的原因。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation | benchmark、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15600) | 暂未公开 | 网络辱骂内容的广泛传播增加了对中国社交媒体文本进行可靠审核的需求；我们介绍了 VARM-Bench，这是中国辱骂言论节制领域锚定思维链基本原理的基准；结果表明，强大的标签级性能可以掩盖完整审核记录中的重大错误。 |
| 2026&#8209;08 | Language-Specific Gaps in AI Safety Training Datasets | benchmark、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13695) | [Dataset](https://huggingface.co/datasets/ChialukaOnuoha/safety-slice-audit) | 大语言模型提供商通常会引用涵盖十几种或更多语言的多语言安全基准作为其模型对于非英语用户安全的证据；我们表明，这些集合级别的覆盖范围声明通常无法通过单个语言级别的检查；我们将这些发现与多语言越狱稳健性中记录的、持续的不对称性（单轮攻击很大程度上减轻，多轮攻击仍然有效）联系起来，认为这种不对称性在结构上与我们的审计发现的训练和评估数据最薄的地方一致。 |
