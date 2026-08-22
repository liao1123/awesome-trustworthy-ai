# 专用领域与多语言 Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究通用 guard model 在专业术语、行业法规、儿童等特定用户群体、低资源语言、code-switching 和地区文化规范下的迁移失败，并构建对应 taxonomy、数据、benchmark 与专用审核模型。这里的目标不是简单翻译英文 safety dataset 或沿用成人风险标签，而是让风险定义来自行业规则、发展心理、当地专家与法规，并同时检查领域能力、通用安全能力和未见语言、年龄线索或 policy 的泛化。

## 研究脉络

- **通用 taxonomy 的缺口：** 英文中心的 harm category 无法覆盖金融合规、医疗建议、法律要求和地区敏感语义，专业术语还会改变原本的安全决策边界。
- **用户群体适配：** Child-facing system 需要识别显式年龄与隐含儿童表达，并在多轮交互中维持发展阶段适当的解释、边界和求助指引，不能只复用成人 harmful-content refusal。
- **数据本地化：** PolyGuard 等工作扩大语言覆盖，SEA-SafeguardBench、UbuntuGuard 与 IndicGuard 进一步用 native author、地区专家和本地法规替代纯机器翻译。
- **Policy-grounded moderation：** ML-Bench&Guard 和 FinGuard 从司法辖区或行业监管文本抽取规则，使 guard 能解释违反了哪条可变 policy，而不只输出通用 harmful label。
- **训练与效率：** MrGuard 用 multilingual reasoning 与 curriculum GRPO，CHILLGuard 用 model-aware preference alignment，LionGuard 2 证明高质量本地数据配合轻量 classifier 也可实际部署。
- **模块化专家：** GuardZoo 的分析显示单一 guard 会受到跨领域 task interference，RouteGuard 因而先识别 threat domain 再路由到 specialized expert。

## 专业行业 Guardrail

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Triaging Threats to Specialized Guardrails | defense、router-expert guard、threat triage、task interference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.30693) | 暂未公开 | 针对不同风险领域的 decision boundary 难压进单一 guard，论文先以 32,460 条人工标注构建 GuardZoo，再让 RouteGuard 将会话路由给 threat-specific expert；结果改善细粒度和 out-of-domain 检测并便于增加新专家。 |
| 2026&#8209;05 | FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions | detection、financial compliance、regulation-grounded data、self-play RL | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29427) | 暂未公开 | 针对通用 harm taxonomy 忽略金融监管违规，论文直接从中国金融法规归纳 risk taxonomy、构建 FinGuard-Bench，并用 SFT 与 self-play RL 训练 FinGuard；结果提升 query/response 合规检测且可读取未见机构 policy。 |
| 2026&#8209;03 | ExpGuard: LLM Content Moderation in Specialized Domains | defense、domain-specific moderation、expert annotation、adversarial jargon | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=t5cYJlV6aJ) · [arXiv](https://arxiv.org/abs/2603.02588) | [Code](https://github.com/brightjade/ExpGuard) | 针对通用 guard 在金融、医疗和法律术语及 adversarial content 上失效，论文构建由领域专家校验的 ExpGuardMix 并训练专用模型；结果在保留通用安全能力时提高专业 prompt 与 response 分类。 |
| 2026&#8209;02 | BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards | defense、ad compliance、multimodal mismatch、policy reward | AAAI 2026 | [arXiv](https://arxiv.org/abs/2602.18193) | 暂未公开 | 针对商业短视频广告的夸大画面、违规表述和字幕-语音错配无法由社区安全类别覆盖，论文以规则生成 ICoT 数据并用 policy-aligned reward 训练；结果改善行业审核的一致性与跨样式泛化。 |

## 儿童交互安全与年龄适配

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | The Age of Curiosity Meets the Age of AI: Benchmarking Child Safety in Large Language Models | benchmark、child-facing safety、age cues、multi-turn degradation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.25510) | [Dataset & Models](https://huggingface.co/collections/sameearif/kidbench) | 针对通用安全评测不检查 7–11 岁儿童所需的发展阶段适当性，论文以十类风险、显式或隐式年龄线索和 child-actor 多轮模拟构建 KIDBench，并发布 KIDGuardLlama 与 KIDLlama；结果显示年龄提示能改善表现，但跨语言文化不均衡且多轮质量会下降 6%–24%。 |

## 多语言与文化本地化模型

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | IndicGuard: A Multilingual Safety Guard Model and Dataset for Indic Languages | defense、Indic languages、regional harm、cross-lingual transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22841) | 暂未公开 | 针对英文中心 guard 忽略南亚社会文化风险，论文以十种 Indic languages 构建本地语境与 jailbreak 数据并微调 4B guard；结果超过 CultureGuard，且能迁移到训练时未覆盖的低资源 Indic language。 |
| 2026&#8209;06 | CHILLGuard: Towards Fine-Grained Chinese LLM Safety Guardrail with Scalable Data Construction and Model-aware Preference Alignment | defense、Chinese moderation、fine-grained taxonomy、preference alignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.15396) | [Repository](https://github.com/cswbyu/CHILLGuard)（当前仅 README） | 针对多语言 guard 缺少中国法规、文化语境和细粒度类别，论文建立 5 个 macro 与 31 个 micro category，并用检索增强数据生成、投票校准和 model-aware DPO 训练；结果形成面向中文场景的专用 guard 与 benchmark。 |
| 2026&#8209;05 | ML-Bench&Guard: Policy-Grounded Multilingual Safety Benchmark and Guardrail for Large Language Models | defense、regional regulation、multilingual policy、diffusion LLM | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.00689) | 暂未公开 | 针对翻译型 benchmark 无法表达不同司法辖区的规则，论文从地区法规构建覆盖 14 种语言的 ML-Bench，并训练 1.5B 快速分类与 7B policy explanation 两类 ML-Guard；结果提升跨语言的 regulation-aware moderation。 |
| 2026&#8209;02 | SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia | defense、Southeast Asian languages、agentic data generation、cultural safety | Under review | [arXiv](https://arxiv.org/abs/2602.01618) | 暂未公开 | 针对机器翻译数据遗漏东南亚本地价值、法规和伤害语境，论文用 agentic pipeline 生成地区原生安全数据并训练 SEA-Guard；结果提高 culturally sensitive 内容检测且保持通用安全性能。 |
| 2025&#8209;07 | LionGuard 2: Building Lightweight, Data-Efficient & Localised Multilingual Content Moderators | tool、Singapore localization、ordinal classifier、production moderation | EMNLP 2025 System Demonstration | [arXiv](https://arxiv.org/abs/2507.15339) | 暂未公开 | 针对全球多语言系统忽略新加坡语言变体且大模型审核成本高，论文以 multilingual embedding 和 multi-head ordinal classifier 覆盖英语、中文、马来语及部分泰米尔语；结果形成已在新加坡政府使用的轻量审核器。 |
| 2025&#8209;05 | OMNIGUARD: An Efficient Approach for AI Safety Moderation Across Languages and Modalities | defense、language-agnostic representation、modality-agnostic classifier、low-resource input | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.23856) | [Code](https://github.com/vsahil/OmniGuard) | 针对低资源语言和非文本 prompt 利用 guard 与主模型泛化不匹配绕过审核，论文在模型内部寻找跨语言/模态对齐 representation 并训练通用 classifier；结果在多语言、图像和音频检测上提升且复用生成 embedding 降低开销。 |
| 2025&#8209;04 | MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety | defense、multilingual reasoning、curriculum GRPO、code-switching | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.15241) | 暂未公开 | 针对 multilingual safety data 稀缺及 code-switching、低资源干扰会改变判断，论文结合合成数据、SFT 和 curriculum GRPO 训练解释型 guard；结果在 seen 与 unseen language 上均超过对比基线并保持判断稳定。 |
| 2025&#8209;04 | PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages | tool、17-language moderation、PolyGuardMix、prompt-response labeling | COLM 2025 | [arXiv](https://arxiv.org/abs/2504.04377) | 暂未公开 | 针对既有 moderation 只覆盖少数语言和有限风险定义，论文以 1.91M 条 PolyGuardMix 训练 17-language guard，并发布 29K PolyGuardPrompts；结果统一判断 prompt harmfulness、response harmfulness 与 refusal。 |

## 文化与低资源语言 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | UbuntuGuard: A Culturally-Grounded Policy Benchmark for Equitable AI Safety in African Languages | benchmark、African languages、expert-authored policy、cultural alignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.12696) | 暂未公开 | 针对英文 benchmark 高估非洲低资源语言的实际安全，论文由 155 名领域专家编写 adversarial query、context-specific policy 和参考响应；结果显示 cross-lingual transfer 只能部分覆盖本地语境，dynamic guard 也仍难完全本地化。 |
| 2025&#8209;12 | SEA-SafeguardBench: Evaluating AI Safety in SEA Languages and Cultures | benchmark、Southeast Asian languages、native annotation、cultural harm | Under review | [arXiv](https://arxiv.org/abs/2512.05501) | 暂未公开 | 针对翻译英文样本无法覆盖地区政治表达与 misinformation，论文构建八种东南亚语言、含 general、in-the-wild 和 generation 子集的人审 benchmark；结果显示现有 LLM 与 guard 在本地文化风险上明显落后于英文表现。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | FraudBench: Stress-Testing Policy-Grounded Banking Agents Against Adaptive Fraud | analysis、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18136) | 暂未公开 | 对话智能体如今通过工具代表终端用户行动，同时能够访问客户数据库和内部政策文档，而来电者仅通过对话就可能触及这些资源；我们提出 FraudBench，一个建立在 $τ^2$-bench 双控制框架和 $τ$-Knowledge 银行环境上的可执行基准；四个智能体在 107 项评分任务上的初步单次评估显示，攻击安全率介于 49% 和 65% 之间，钱骡欺诈和第一方欺诈是跨模型最常见的弱点。 |
| 2026&#8209;08 | Beyond "I Can't Help With That": How Child Safety Experts Evaluate AI Chatbot Safety | analysis、adversarial robustness、specialized guardrail、domain policy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.07902) | 暂未公开 | 研究访谈 19 名直接服务高风险青少年的社工、治疗师和心理学家，让其评议 chatbot 在真实危险情境中的响应；结果指出单看拒答或表面有害文本会漏掉实际伤害，并形成把一线专家判断纳入儿童安全评测的具体建议。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models | detection、high-risk deployment、specialized guardrail、domain policy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16852) | 暂未公开 | 已部署语言模型中的监管合规性监控越来越多地作为法律和审计控制来实施，根据涵盖数据保护、医疗保健、金融监管和平台政策的书面规则检查模型输出；我们证明这种情况在当前类别的合规性检测器中失败，我们将这种失败称为规则盲目性；一个专门构建的基准测试跨越两种场景的两个规则，这样既不能单独预测标签，也不能在先前基准测试没有排除的设计下确认失败，并表明逐步推理，而不是我们测试的任何快速检测器，才是逃脱它的原因。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation | benchmark、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15600) | 暂未公开 | 网络辱骂内容的广泛传播增加了对中国社交媒体文本进行可靠审核的需求；我们介绍了 VARM-Bench，这是中国辱骂言论节制领域锚定思维链基本原理的基准；结果表明，强大的标签级性能可以掩盖完整审核记录中的重大错误。 |
| 2026&#8209;08 | Language-Specific Gaps in AI Safety Training Datasets | benchmark、specialized guardrail、domain policy、multilingual safety | 未注明（arXiv） | [Official](https://huggingface.co/datasets/ChialukaOnuoha/safety-slice-audit) · [arXiv](https://arxiv.org/abs/2608.13695) | 暂未公开 | 大语言模型提供商通常会引用涵盖十几种或更多语言的多语言安全基准作为其模型对于非英语用户安全的证据；我们表明，这些集合级别的覆盖范围声明通常无法通过单个语言级别的检查；我们将这些发现与多语言越狱稳健性中记录的、持续的不对称性（单轮攻击很大程度上减轻，多轮攻击仍然有效）联系起来，认为这种不对称性在结构上与我们的审计发现的训练和评估数据最薄的地方一致。 |
