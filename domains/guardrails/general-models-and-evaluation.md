# 通用 Guard Model、评测与安全边界

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究面向通用文本交互的外部 guard model：它们在主模型前后执行 prompt safety、response safety、jailbreak、refusal 与 harm category 判断，并在生产系统中承担最终拦截层。除模型训练外，本页也关注 guardrail 放置位置、classifier architecture、可识别性、shortcut、over-refusal、计算开销和对自适应攻击的实际安全边界。

## 研究脉络

- **固定分类基线：** 早期 guard model 将内容安全建模为固定 taxonomy 下的 prompt 或 response 分类，并用专门的小模型作为主模型外部防线。
- **Policy-grounded 数据：** Constitutional Classifiers 用自然语言 constitution 合成训练数据，Qwen3Guard 等模型进一步统一多语言、生成式和 streaming 审核接口。
- **生产架构：** 新一代系统采用 exchange-level 判断、probe 与大 classifier 级联、分层推理或 specialized SLM，以降低 over-refusal 和推理开销。
- **安全边界：** 近期工作开始系统比较 encoder 与 decoder、输入与输出过滤、guardrail fingerprint，并揭示 refusal cue、可复制上下文和黑盒行为信号造成的失效或泄漏。

## 通用 Guard Model 与生产架构

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions | defense、jailbreak、uncertainty calibration、guard model | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10621) | 暂未公开 | ProbGuard 从前十个 decoding step 的输出分布用 Monte Carlo 估计并校准继续生成的 unsafe probability；九个模型—数据组合上平均 Brier score 和 ECE 较最佳基线下降 79.6% 与 71.9%，六类 jailbreak 的 ASR 均压到 1% 以下。 |
| 2026&#8209;05 | Fence: Specialized SLM Guardrails for LLM Applications | tool、specialized SLM guard、application policy、low-latency moderation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.18268) | 暂未公开 | 针对通用大模型 guard 成本高且难贴合具体应用，论文训练面向专门 policy 的小型 guard model；结果表明 specialized SLM 可以在较低部署成本下承担应用级内容审核。 |
| 2026&#8209;05 | Why Do Safety Guardrails Degrade Across Languages? | defense、guard model、content moderation、safety-utility trade-off | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2605.17173) | 暂未公开 | 针对 JSR 将模型、prompt 与语言因素混为一体的问题，作者以 Multi-Group IRT 分解 61 个模型配置、10 种语言和 190 万条响应，发现低资源语言并非总是更脆弱，并定位 concept–language 特定安全缺口。 |
| 2026&#8209;01 | Lattice: Generative Guardrails for Conversational Agents | defense、adversarial robustness、guard model、content moderation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.17481) | 暂未公开 | Lattice 先从标注样本通过模拟与优化自构建 guardrail，再以风险评估、对抗测试和合并闭环持续更新；ProsocialDialog 上达 91% F1，较 LlamaGuard 高 25 个百分点，跨域持续改进再提升 7 个百分点。 |
| 2026&#8209;01 | YuFeng-XGuard: A Reasoning-Centric, Interpretable, and Flexible Guardrail Model for Large Language Models | tool、dynamic safety policy、hierarchical reasoning、risk taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.15588) | 暂未公开 | 针对固定类别 guard 缺少解释且难随 policy 调整，论文训练可输出风险类别、置信度和按需解释的分层 guard，并将风险识别与 policy enforcement 解耦；结果同时提供 8B 推理版本与蒸馏的小模型版本。 |
| 2026&#8209;01 | Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks | defense、constitutional classifiers、classifier cascade、universal jailbreak | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=eNvsH5Ye2V) · [arXiv](https://arxiv.org/abs/2601.04603) | 暂未公开 | 针对第一代 Constitutional Classifiers 的上下文盲区、误拒和计算开销，论文用 exchange classifier、activation probe 与两阶段 cascade 只升级可疑流量；结果把计算开销降约 40 倍、生产流量误拒率降至 0.05%，且 1,700 小时 red teaming 未发现满足其定义的 universal jailbreak。 |
| 2026 | RST-Guarder: Enhancing Long-Context Robustness for Safeguards via RST Parsing and Probabilistic Inference | defense、adversarial robustness、guard model、content moderation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1025/) | 暂未公开 | 针对 guardrail 在长文本和上下文噪声下退化，RST-Guarder 用 discourse relation 建层次结构并对分段 safety score 做概率聚合，无需训练即可持续提高检测并减少良性误报。 |
| 2026 | HiddenGuard: Fine-Grained Safe Generation with Specialized Representation Router | defense、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1482/) | 暂未公开 | 针对整段拒绝会同时屏蔽请求中的良性信息，HiddenGuard 用中间表征 router 做实时 token-level harmfulness 检测与删改，以超过 90% F1 精细隐藏敏感片段并保留回答效用。 |
| 2026 | Efficient LLM Moderation with Multi-Layer Latent Prototypes | defense、guard model、content moderation、safety-utility trade-off | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64923) | 暂未公开 | 针对静态安全对齐容易过度拒绝，也难覆盖推理时出现的新风险的问题，论文提出 Efficient LLM Moderation with Multi-Layer 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于安全拒绝校准与在线防护。 |
| 2026 | Domain Generalizable AI Guardrails with Augmented Policy Training | defense、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.748/) | 暂未公开 | 针对 LlamaGuard 等 guardrail 对训练政策过拟合、难适配新领域，APT 在训练时系统扰动 policy definition，使 1B 模型在未见政策上达到或超过现有 8B guardrail。 |
| 2026 | A Lightweight Explainable Guardrail for Prompt Safety | defense、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2017/) | 暂未公开 | 针对安全 prompt 分类器通常体量大且解释不可靠，LEG 联合学习整体分类与词级解释并用去确认偏差的合成监督，在三个数据集的域内外测试中以更小模型达到或超过现有分类和可解释性表现。 |
| 2025&#8209;11 | SGuard-v1: Safety Guardrail for Large Language Models | tool、dual-filter guard、content moderation、jailbreak detection | Technical Report | [arXiv](https://arxiv.org/abs/2511.12497) | 暂未公开 | 针对外部审核需要低成本分别处理普通有害内容与 jailbreak，论文用两个 2B Granite filter 构成 input/output safety layer；结果给出可本地部署的 ContentFilter 与 JailbreakFilter 模型族。 |
| 2025&#8209;10 | Qwen3Guard Technical Report | tool、multilingual guard、generative moderation、streaming moderation | Technical Report | [arXiv](https://arxiv.org/abs/2510.14276) | [Code](https://github.com/QwenLM/Qwen3Guard) | 针对完整响应审核会延迟阻断且既有 guard 覆盖语言有限，论文发布 generative 与 streaming 两类、多个尺寸的多语言 guard model；结果统一支持 prompt、response、风险类别与实时 token stream 审核。 |
| 2025&#8209;07 | Lightweight Safety Guardrails via Synthetic Data and RL-guided Adversarial Training | defense、lightweight guard、synthetic data、adversarial training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.08284) | 暂未公开 | 针对小型 guard model 在自适应 jailbreak 下容易失效，论文结合合成安全数据与 RL-guided adversarial training 训练轻量分类器；结果在控制部署开销的同时提高对对抗输入的检测鲁棒性。 |
| 2025&#8209;01 | Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming | defense、constitutional classifiers、synthetic policy data、red teaming | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2501.18837) | 暂未公开 | 针对固定数据分类器难覆盖新型 jailbreak，论文从自然语言 constitution 自动生成并增强输入输出训练样本；原型经超过 3,000 小时 red teaming 未出现 universal jailbreak，更新版本把自动攻击成功率从 86% 降至 4.4%，但仍引入计算和误拒成本。 |

## 基础 Guard Model 与开放资源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;01 | Aegis2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails | benchmark、risk taxonomy、human-LLM interaction、category adaptation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2501.09004) | 暂未公开 | 针对可商用、人工标注且覆盖广泛风险的 guard training data 稀缺，论文建立可扩展 taxonomy 与 Aegis 2.0，并用 topic-following data 帮助轻量 guard 适应推理时新增类别；结果提供模型与数据设计基线。 |
| 2024&#8209;07 | ShieldGemma: Generative AI Content Moderation Based on Gemma | tool、Gemma guard、synthetic data、four-harm taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2407.21772) | 暂未公开 | 针对开发者需要覆盖 prompt 与 response 的开放 moderation model，论文基于 Gemma 2 构建多个尺寸的 ShieldGemma，并以可迁移的 LLM data curation pipeline 训练；结果在四类核心风险上形成可部署基线。 |
| 2024&#8209;06 | WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs | tool、multi-task moderation、jailbreak detection、refusal classification | NeurIPS 2024 Datasets and Benchmarks | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0f69b4b96a46f284b726fbd70f74fb3b-Abstract-Datasets_and_Benchmarks_Track.html) · [arXiv](https://arxiv.org/abs/2406.18495) | [Code](https://github.com/allenai/wildguard) | 针对开源 guard 分别处理 prompt、response 与 refusal 且在 jailbreak 上明显落后，论文以 WildGuardMix 联合训练三项任务；结果提供覆盖 13 类风险的一站式 moderation model 与人工测试集。 |
| 2024&#8209;04 | AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts | defense、online adaptation、expert ensemble、content taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2404.05993) | 暂未公开 | 针对单一安全专家难同时覆盖常见与稀疏风险，论文构建 AegisSafetyDataset 和分层 taxonomy，并用 no-regret online adaptation 组合多个 LLM safety expert；结果使部署中的 moderator 可随流量选择更合适的专家。 |
| 2023&#8209;12 | Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations | tool、input-output guard、risk taxonomy、instruction tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2312.06674) | 暂未公开 | 针对对话系统需要同一组件审核用户 prompt 与模型 response，论文以 Llama 2-7B 按 safety taxonomy 做 instruction tuning；结果奠定生成式、多类别、可通过指令调整 taxonomy 和输出格式的通用 guard 基线。 |

## 架构比较、识别与失效分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models | analysis、refusal-cue shortcut、response moderation、causal intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.03201) | 暂未公开 | 针对 response guard 可能把拒答措辞误当作安全证据，论文在真实有害回复中插入 refusal cue 并定位相关 attention heads 与 MLP neurons；结果少量表面拒答文本即可翻转判断，而屏蔽 shortcut component 能缓解该失效。 |
| 2026&#8209;07 | Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs | analysis、copyable context、trusted-user gating、impossibility result | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.27951) | 暂未公开 | 针对依赖角色声明、用途说明或对话内容区分可信用户的 safeguard，论文形式化攻击者可复制全部判别上下文的情形；结论是只要系统保留正常用户效用，就无法据此保证向攻击者释放零危险能力。 |
| 2026&#8209;07 | Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting | analysis、filter placement、response rewriting、end-to-end trade-off | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.26200) | 暂未公开 | 针对 guardrail 研究常孤立评测单个 classifier，论文联合比较输入、输出过滤位置与拦截后 response rewriting；结果表明最终安全性、helpfulness、延迟和误拒取决于整条 moderation pipeline，而不能只由分类器分数判断。 |
| 2026&#8209;07 | Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring | analysis、guardrail activation、behavioral monitoring、black-box inference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.02121) | 暂未公开 | 针对黑盒系统的拒答无法区分主模型自拒与外接 guardrail 拦截，论文综合 HTTP response、拒答文本和延迟等行为信号进行判断；结果可识别 guardrail 是否被触发并推断其部署行为。 |
| 2026&#8209;06 | Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation | analysis、encoder-decoder comparison、safety judge、adversarial evaluation | ICANN 2026 | [arXiv](https://arxiv.org/abs/2606.25782) | 暂未公开 | 针对生成式 decoder guard 是否必然优于 encoder 分类器缺少同条件比较，论文系统控制模型规模、数据与攻击设置评测两类架构；结果刻画了 encoder 在成本与若干检测任务上的优势，以及复杂 policy reasoning 仍需要生成式 judge 的边界。 |
| 2025&#8209;02 | Peering Behind the Shield: Guardrail Identification in Large Language Models | attack、guardrail fingerprinting、adversarial probe、deployment placement | Findings of ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.566/) · [arXiv](https://arxiv.org/abs/2502.01241) | [Code](https://github.com/TrustAIRLab/AP-Test) | 针对黑盒 AI 服务隐藏所用 guardrail 及其 input/output placement，论文为候选 guard 优化具有区分性的 adversarial prompt；结果 AP-Test 可通过响应差异识别后端 guardrail，为模型审计也为定向规避暴露新攻击面。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;06 | SoK: Evaluating Jailbreak Guardrails for Large Language Models | survey、jailbreak guardrails、evaluation framework、adaptive attacks | IEEE S&P 2026 | [arXiv](https://arxiv.org/abs/2506.10597) | [Code](https://github.com/xunguangwang/SoK4JailbreakGuardrails) | 针对 jailbreak guardrail 的威胁模型、评测数据和指标不可直接比较，论文系统整理输入输出过滤器及自适应攻击，并复现实验分析攻击拦截、benign utility 与成本；结论是静态 benchmark 容易高估真实防护能力。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models | detection、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1584/) | 暂未公开 | 针对低数据条件下 toxicity detector 难同时分类和解释，SMARTER 以 LLM 自生成正误解释做 preference optimization 再跨模型精炼，仅用 6%–57% 训练数据便较 few-shot 基线最高提高 13% Macro-F1。 |
| 2026 | RV-HATE: Reinforced Multi-Module Voting for Implicit Hate Speech Detection | detection、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2104/) | 暂未公开 | 针对不同平台 hate speech 语体和语境差异使固定检测器失效，RV-HATE 用多个语言/语境模块并以 RL 学习数据集特定权重，提升隐性仇恨检测且能解释各数据源特征。 |
| 2026 | New Terms, New Toxicity: Consensus-based Chinese Neologism Toxicity Detection via Search-Augmented LLMs | detection、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1602/) | 暂未公开 | 针对“田园女”等新词表面良性却承载隐性毒性，SeTox 以分类法、风险词典和实时搜索语境建立公众共识，3B 模型即可超过近期更大模型的中文新词毒性检测。 |
| 2026 | LLM Safety From Within: Detecting Harmful Content with Internal Representations | detection、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1844/) | 暂未公开 | 针对 guard model 只用终层而忽略跨层安全信号，SIREN 以 linear probe 找出 safety neuron 并自适应聚合各层，用少 250 倍可训练参数超过开源 guard，且支持实时流式检测。 |
| 2026 | LLM-Based Multi-Task Bangla Hate Speech Detection: Type, Severity, and Target | detection、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1565/) | 暂未公开 | 针对 Bangla 审核数据只做单一 hate/offense 标签，BanglaMultiHate 同时标注类型、严重度和目标并比较多类模型，显示 LoRA LLM 可匹配 BanglaBERT，但文化化预训练仍是稳健检测关键。 |
| 2026 | DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects | detection、harmful content、guard model、content moderation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.144/) | 暂未公开 | 针对 harmful-content detector 主要用标准美式英语评测，DIA-HARM 构造 50 种英语方言的 195K 样本，发现真人方言内容使 F1 降 1.4%–3.6%，部分模型在混合文本上下降逾 33%。 |
| 2026 | Beyond Single-View Detection: A Dual-Space Reasoning Framework for Interpretable Harmful Meme Understanding | detection、reasoning safety、guard model、content moderation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.480/) | 暂未公开 | 针对 harmful meme 的隐性偏见和多视角语义难由黑盒分类解释，BPDMoE-Hate 用对抗二元视角、adaptive gating 与双几何空间专家，在三个数据集上提高检测并给出视角和层次结构解释。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | N-GLARE: An Non-Generative Latent Representation-Efficient LLM Safety Evaluator | benchmark、guard model、content moderation、safety-utility trade-off | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1334/) | 暂未公开 | 针对生成式 red teaming 成本高且反馈慢，N-GLARE 仅分析 latent Angular-Probabilistic Trajectory 并以 JSS 排序，覆盖 40 余模型和 20 种策略时用不到 1% token 与运行成本复现红队安全排名。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Narrative License and Model Sycophancy in LLM Summaries of Scientific Work | analysis、sycophancy、guard model、content moderation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.746/) | 暂未公开 | 对六个模型总结 100 篇论文发现默认 prompt 常把因果、置信与情感修辞夸大，用户立场和 persona 会可预测地放大这种 narrative license，而专门 guardrail prompt 能缓解。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;03 | When Grammar Guides the Attack: Uncovering Control-Plane Vulnerabilities in LLMs with Structured Output | attack、structured output、guard model、content moderation | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2503.24191) | [Code](https://github.com/zhangshuoming990105/ConstrainedDecodingAttack) | 针对 JSON Schema 等 grammar-guided decoding 可绕过数据面 guardrail 的控制面漏洞，CDA 以 EnumAttack 与 DictAttack 强制有害生成轨迹，在 13 个模型上取得 94.3%–99.5% ASR，且 DictAttack 面对现有 guardrail 仍达 75.8%。 |

## 基础 Tool

| 时间 | 名称 | 类型 | 链接 | 作用与边界 |
| --- | --- | --- | --- | --- |
| 2026 | Guardex | programmable guardrail toolkit | [Code](https://github.com/atliq/guardex-ai) | 提供可组合的输入输出 guard 与 policy enforcement 接口，适合应用原型和 pipeline 集成；实际防护范围仍取决于所配置 policy、detector、执行位置与 adversarial evaluation。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks | Anthropic | classifier cascade、exchange classifier | [Anthropic](https://www.anthropic.com/research/next-generation-constitutional-classifiers) | 解释第二代系统为何从 output-only classifier 改为完整 exchange 判断，并用 activation probe 先筛流量；文章还公开 reconstruction 与 output obfuscation 两类残余攻击面，避免把低成本级联理解为完备防御。 |
| 2025&#8209;09 | Qwen3Guard: Real-time Safety for Your Token Stream | Qwen Team | streaming moderation、multilingual guard | [Qwen](https://qwen.ai/blog?id=qwen3guard) | 从部署接口说明 generative 与 stream 两个模型族如何覆盖多语言 prompt、response 和实时 token 风险，并给出不同尺寸模型的使用方式与 policy taxonomy。 |
| 2025&#8209;02 | Constitutional Classifiers: Defending against universal jailbreaks | Anthropic Safeguards Research Team | constitutional classifiers、red teaming | [Anthropic](https://www.anthropic.com/research/constitutional-classifiers) | 以 constitution 生成训练数据的完整流程解释输入输出 classifier，并补充公开 red-team challenge 的结果、成功攻击类型、over-refusal 和 23.7% 计算开销等部署语境。 |
