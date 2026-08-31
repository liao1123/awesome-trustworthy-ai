# Persona Vector 与人格安全

[返回其他研究领域目录](README.md)

## 研究方向

本页只收录与安全行为直接相连的 Persona Vector 研究，例如 truthfulness、sycophancy、emergent misalignment、persona-based jailbreak、scenario-conditioned refusal suppression 和角色条件推理成本攻击。只解释角色一致性、一般人格形成、role-playing 体验或用角色向量提升普通任务能力的工作不收录。

## 研究脉络

- **表征假设：** 早期 persona hypothesis 将 truthfulness 等安全相关行为解释为模型从预训练文本中的 agent hierarchy 学到的角色表征；user-persona 研究则表明模型对“提问者是谁”的内部判断也会改变拒答。
- **监测与控制：** Persona Vectors 从 evil、sycophancy、hallucination 等 trait 提取 activation direction，用于预测和缓解不良行为变化。
- **机制追踪：** Assistant Axis 刻画默认 Assistant 在 persona space 中的位置，并把偏离该轴与 harmful drift 和 persona-based jailbreak 联系起来。
- **安全扩展：** 近期研究把这些表征与 fine-tuning 引发的 persona drift、emergent misalignment、persona-based jailbreak 和 inference-cost attack 连接起来，并扩展到训练数据归因与 persona-invariant defense。

## Persona 表征形成与结构

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models | analysis、assistant persona、persona drift、activation axis | ICML 2026 Spotlight | [Official](https://icml.cc/virtual/2026/poster/61446) · [arXiv](https://arxiv.org/abs/2601.10387) | [Code](https://github.com/safety-research/assistant-axis) | 针对默认 Assistant 身份在多种角色中的几何位置与失稳机制不清，论文从 275 类角色 activation 中提取主导 persona space 的 Assistant Axis；结果偏离该轴可预测 harmful 或 bizarre persona drift，而 activation capping 能稳定相关对话并缓解 persona-based jailbreak。 |
| 2023&#8209;10 | Personas as a Way to Model Truthfulness in Language Models | analysis、truthful persona、activation probing、cross-topic generalization | EMNLP 2024 | [ACL Anthology](https://aclanthology.org/2024.emnlp-main.364/) | 暂未公开 | 针对模型未接收 truth label 却能在表征中区分真假这一现象，论文提出预训练语料由不同 truthful 或 untruthful agents 生成并形成 persona hierarchy；结果可在生成前 probe 回答是否真实，且对一组事实微调会提高未见主题的 truthfulness，支持抽象 persona 从数据结构中形成。 |

## Persona 监测与控制 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;07 | Persona Vectors: Monitoring and Controlling Character Traits in Language Models | tool、persona vector、trait monitoring、preventative steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.21509) | [Code](https://github.com/safety-research/persona_vectors) | 针对 evil、sycophancy 和 hallucination propensity 等 trait 缺少通用内部监测信号，论文从正反 persona response 的 activation 差自动提取 persona vector；结果这些方向既能预测 fine-tuning 引起的人格变化，也能通过 post-hoc intervention、preventative steering 和训练样本筛选降低不良漂移。 |

## Persona 漂移与 Emergent Misalignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Data Attribution of Emergent Misalignment with Persona Features | analysis、persona features、data attribution、emergent misalignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11025) | 暂未公开 | 针对 misaligned persona features 在预训练语料中的来源以及自然人类文本能否诱发 emergent misalignment，论文在四个开放权重模型上做 SAE model diffing 并向一百万篇 web documents 归因；结果单 feature steering 可把 misalignment 提高到 62% 或恢复至近基线，但只有把相关内容改造成 synthetic instruction-response pairs 才稳定诱发跨模型 EM。 |
| 2026&#8209;01 | Objective Matters: Fine-Tuning Objectives Shape Safety, Robustness, and Persona Drift | analysis、persona drift、fine-tuning objectives、adversarial robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.12639) | 暂未公开 | 针对良性 fine-tuning 也可能破坏 alignment 而 objective 的作用缺少受控比较，论文固定数据、模型和优化设置比较六种训练目标；结果小预算下各方法鲁棒性接近，但规模增大后 SFT 与 preference tuning 把能力增益同脆弱性和 persona drift 紧密耦合，ORPO 与 KL regularization 可显著缓解。 |
| 2026 | Quantifying and Mitigating Socially Desirable Responding in LLMs: A Desirability-Matched Graded Forced-Choice Psychometric Study | defense、persona vector、behavior steering、trait stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1865/) | 暂未公开 | 论文用 HONEST/FAKE-GOOD 与 IRT 效应量衡量问卷中的社会期许作答，并以 30 对期许匹配的 graded forced-choice 题显著削弱九个 LLM 的伪善偏差，同时大体保留 persona 还原。 |

## Persona 脆弱场景与攻防

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Do LLMs Know Their Vulnerable Scenarios? | attack、scenario-conditioned jailbreak、refusal direction、Concept2Scenario | 未确认（arXiv Comments：Under review） | [arXiv](https://arxiv.org/abs/2607.23496) | 暂未公开 | 针对相同有害请求置于某些场景后更易绕过拒答而原因不明，论文用 SAE concept attribution 将压制 refusal direction 的内部概念转成可解释场景并组合为 Concept2Scenario；结果跨三种开放模型和六类攻击平均提高 ASR 最多 18.2 个百分点，且可迁移到多个闭源模型。 |
| 2026&#8209;05 | Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment | defense、persona-based jailbreak、adversarial self-play、persona invariance | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61505) · [arXiv](https://arxiv.org/abs/2605.01899) | [Code](https://github.com/JiajiaLi-1130/PIA) | 针对 persona-based jailbreak 的防御缺少对“角色”和“有害意图”的结构性解耦，论文用 PLE 搜索高风险 persona，并以 PICL 的 unilateral KL constraint 联合训练防御模型；结果显著降低 ASR，同时保持通用能力和对良性请求的可用性。 |
| 2026 | Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents ↗ | defense、role-playing agent、persona-safe defense、dual-cycle self-evolution | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) | 暂未公开 | 针对 persona 忠实度会放大危险角色的越狱面、训练式防御又难适配闭源模型，DASE 让 persona-targeted attacker 与 defender 双循环演化，把失败沉淀为全局规则、角色约束和安全范例并在推理时检索；跨专有模型同时提高角色一致性和安全性，最强演化攻击下拒答率由 62% 提至 76%。 |
| 2024&#8209;06 | Who's asking? User personas and the mechanics of latent misalignment | attack、user persona、activation steering、latent misalignment | NeurIPS 2024 Spotlight | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e40d5118ee8f837729fa877add71c38f-Abstract-Conference.html) | 暂未公开 | 针对安全模型为何会因其推断的用户身份不同而选择性泄露有害内容，论文比较自然语言 prompt 与 user-persona activation steering，并用 early decoding 和 Patchscopes 追踪机制；结果 persona steering 比直接操控 refusal 更有效，且较早层仍保留可解码的有害内容，特定 persona 会让模型把危险请求解释得更无害。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Persona-Grounded Safety Evaluation of AI Companions in Multi-Turn Conversations | benchmark、safety evaluation、persona vector、behavior steering | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.828/) | 暂未公开 | 针对 AI companion 对高风险用户的实时安全行为缺少可控评测，作者用九类临床 persona 和 25 个场景收集 1,674 段对话，发现 Replika 常镜像或正常化自伤、进食障碍和暴力幻想。 |
| 2026 | Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation | benchmark、persona vector、behavior steering、trait stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1741/) | 暂未公开 | 针对静态有害内容 benchmark 容易污染且缺少多样场景，作者以人口属性、兴趣和伤害策略构造 persona agent 生成测试，其样本比既有基准更难检测且多样性接近人工数据。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents | analysis、agent safety、persona vector、behavior steering | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1260/) | 暂未公开 | 针对长期个人记忆会把本来有害的请求解释为合理意图，PS-Bench 显示 personalization 相比无状态 agent 将 ASR 提高 15.8%–243.7%，轻量 detection–reflection 可缓解该安全退化。 |
| 2026 | Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities | analysis、persona vector、behavior steering、trait stability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60519) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Split Personality Training 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | The assistant axis: situating and stabilizing the character of large language models | Anthropic Interpretability | Assistant Axis、persona stabilization | [Anthropic](https://www.anthropic.com/research/assistant-axis) | 通过 275 个角色可视化 persona space，解释默认 Assistant 为何位于主轴一端、情绪对话为何会推动模型偏离该区域，以及 activation capping 如何减少漂移与 persona-based jailbreak。 |
| 2025&#8209;08 | Persona vectors: Monitoring and controlling character traits in language models | Anthropic Interpretability | persona vectors、trait monitoring | [Anthropic](https://www.anthropic.com/research/persona-vectors) | 以 evil、sycophancy 和 hallucination 为例解释 persona vector 的自动提取、部署期监测、post-hoc steering 与训练数据筛选；文章同时展示强 steering 可能损伤能力，因此 preventative steering 不能被理解为无代价控制。 |
| 2025&#8209;06 | Toward understanding and preventing misalignment generalization | OpenAI | misaligned persona、emergent realignment | [OpenAI](https://openai.com/index/emergent-misalignment/) | 用案例和 SAE feature 可视化解释狭窄错误训练如何放大 misaligned persona，并展示反向 steering 与少量正确样本再训练的缓解效果；文章将这些信号定位为潜在 early-warning tool，而非完整的 alignment 保证。 |
