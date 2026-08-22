# Persona Vector 与人格安全

[返回其他研究领域目录](README.md)

## 研究方向

Persona Vector 研究模型内部是否存在表示人格、角色或行为倾向的 activation direction，以及这些方向如何在预训练和后训练中形成、如何用于监测与 steering。安全研究进一步关注 persona drift、persona-based jailbreak、scenario-conditioned refusal suppression 和角色条件导致的推理成本攻击。该方向的重点不是模型自报的人格标签，而是人格表征与实际行为之间是否存在可测量、可干预和可迁移的因果联系。

## 研究脉络

- **表征假设：** 早期 persona hypothesis 将 truthfulness 等抽象行为解释为模型从预训练文本中的 agent hierarchy 学到的角色表征；user-persona 研究则表明模型对“提问者是谁”的内部判断也会改变拒答。
- **监测与控制：** Persona Vectors 与 role vectors 建立了从自然语言 trait 或角色提取 activation direction，并用其监测、控制和评测行为的方法。
- **机制追踪：** Assistant Axis 与 persona circuit 工作进一步刻画默认 Assistant 在 persona space 中的位置，以及角色信号的形成和表达过程。
- **安全扩展：** 近期研究把这些表征与 fine-tuning 引发的 persona drift、emergent misalignment、persona-based jailbreak 和 inference-cost attack 连接起来，并扩展到训练数据归因与 persona-invariant defense。

## Persona 表征形成与结构

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Tracing Persona Vectors Through LLM Pretraining | analysis、persona representation、pretraining dynamics、activation geometry | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.13329) | [Code](https://github.com/epfl-dlab/pretraining_persona) | 针对 persona vector 在训练何时形成及如何演化尚不清楚，论文沿 OLMo-3-7B checkpoint 追踪其几何与语义变化并在 Apertus-8B 复现；结果这些方向在 0.22% 的预训练进度内已出现，之后持续细化且可 steering 完成后训练的模型。 |
| 2026&#8209;01 | The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models | analysis、assistant persona、persona drift、activation axis | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61446) · [arXiv](https://arxiv.org/abs/2601.10387) | [Code](https://github.com/safety-research/assistant-axis) | 针对默认 Assistant 身份在多种角色中的几何位置与失稳机制不清，论文从 275 类角色 activation 中提取主导 persona space 的 Assistant Axis；结果偏离该轴可预测 harmful 或 bizarre persona drift，而 activation capping 能稳定相关对话并缓解 persona-based jailbreak。 |
| 2026 | Tracing the Persona Circuit: How Large Language Models Encode and Express Character Traits | analysis、persona circuit、out-of-character behavior、causal tracing | ICML 2026 | [OpenReview](https://openreview.net/forum?id=doy2uIaAYt) | 暂未公开 | 针对角色知识存在却仍出现 out-of-character behavior 的内部原因不清，论文以 Latent Persona Vector 扩展多 token 输出的 causal tracing 并识别“准备、建立、表达”三阶段；结果将失角色归因于 persona signal 与默认 Assistant 方向竞争，并通过重校准少于 5% 的 attention heads 恢复角色一致性而保留推理能力。 |
| 2023&#8209;10 | Personas as a Way to Model Truthfulness in Language Models | analysis、truthful persona、activation probing、cross-topic generalization | EMNLP 2024 | [ACL Anthology](https://aclanthology.org/2024.emnlp-main.364/) | 暂未公开 | 针对模型未接收 truth label 却能在表征中区分真假这一现象，论文提出预训练语料由不同 truthful 或 untruthful agents 生成并形成 persona hierarchy；结果可在生成前 probe 回答是否真实，且对一组事实微调会提高未见主题的 truthfulness，支持抽象 persona 从数据结构中形成。 |

## Persona 监测与控制 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;07 | Persona Vectors: Monitoring and Controlling Character Traits in Language Models | tool、persona vector、trait monitoring、preventative steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.21509) | [Code](https://github.com/safety-research/persona_vectors) | 针对 evil、sycophancy 和 hallucination propensity 等 trait 缺少通用内部监测信号，论文从正反 persona response 的 activation 差自动提取 persona vector；结果这些方向既能预测 fine-tuning 引起的人格变化，也能通过 post-hoc intervention、preventative steering 和训练样本筛选降低不良漂移。 |
| 2025&#8209;02 | Can Role Vectors Affect LLM Behaviour? | tool、role vectors、activation addition、directional ablation | Findings of EMNLP 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.963/) | 暂未公开 | 针对 persona prompting 是否真正改变模型能力而非只改变措辞，论文从 activation 中构造 29 个 role vectors，并分别执行 addition 与 directional ablation；结果 role vector 能提高相关领域 benchmark 表现并产生部分跨领域增益，其行为影响强于对应的文本 persona prompt。 |

## Persona 漂移与 Emergent Misalignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Data Attribution of Emergent Misalignment with Persona Features | analysis、persona features、data attribution、emergent misalignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11025) | 暂未公开 | 针对 misaligned persona features 在预训练语料中的来源以及自然人类文本能否诱发 emergent misalignment，论文在四个开放权重模型上做 SAE model diffing 并向一百万篇 web documents 归因；结果单 feature steering 可把 misalignment 提高到 62% 或恢复至近基线，但只有把相关内容改造成 synthetic instruction-response pairs 才稳定诱发跨模型 EM。 |
| 2026&#8209;01 | Objective Matters: Fine-Tuning Objectives Shape Safety, Robustness, and Persona Drift | analysis、persona drift、fine-tuning objectives、adversarial robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.12639) | 暂未公开 | 针对良性 fine-tuning 也可能破坏 alignment 而 objective 的作用缺少受控比较，论文固定数据、模型和优化设置比较六种训练目标；结果小预算下各方法鲁棒性接近，但规模增大后 SFT 与 preference tuning 把能力增益同脆弱性和 persona drift 紧密耦合，ORPO 与 KL regularization 可显著缓解。 |
| 2026 | Quantifying and Mitigating Socially Desirable Responding in LLMs: A Desirability-Matched Graded Forced-Choice Psychometric Study | defense、persona vector、behavior steering、trait stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1865/) | 暂未公开 | 论文用 HONEST/FAKE-GOOD 与 IRT 效应量衡量问卷中的社会期许作答，并以 30 对期许匹配的 graded forced-choice 题显著削弱九个 LLM 的伪善偏差，同时大体保留 persona 还原。 |
| 2025&#8209;06 | Persona Features Control Emergent Misalignment | analysis、persona features、SAE model diffing、emergent realignment | ICLR 2026 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/50db99ee3bccf73bfe1cf2af1e960414-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.19823) | [Code](https://github.com/openai/emergent-misalignment-persona-features) | 针对狭窄错误数据微调为何会泛化成无关领域的广泛 misalignment，论文用 SAE model diffing 比较训练前后内部表征并定位 misaligned persona features；结果其中 toxic persona feature 能预测并因果控制 EM，而数百个 benign samples 的追加微调可高效恢复 alignment。 |

## Persona 脆弱场景与攻防

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs | attack、persona-conditioned DoS、RolePlay、token amplification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.25936) | 暂未公开 | 针对对抗后缀和显式延长指令容易被检测，论文用 RolePlay 按任务构造会自然维持低效行为的人设；结果平均放大 token 7.64 倍、最高 207.64 倍，表明角色一致性本身是新的成本攻击面。 |
| 2026&#8209;07 | Do LLMs Know Their Vulnerable Scenarios? | attack、scenario-conditioned jailbreak、refusal direction、Concept2Scenario | Under Review（arXiv） | [arXiv](https://arxiv.org/abs/2607.23496) | 暂未公开 | 针对相同有害请求置于某些场景后更易绕过拒答而原因不明，论文用 SAE concept attribution 将压制 refusal direction 的内部概念转成可解释场景并组合为 Concept2Scenario；结果跨三种开放模型和六类攻击平均提高 ASR 最多 18.2 个百分点，且可迁移到多个闭源模型。 |
| 2026&#8209;05 | Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment | defense、persona-based jailbreak、adversarial self-play、persona invariance | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61505) · [arXiv](https://arxiv.org/abs/2605.01899) | [Code](https://github.com/JiajiaLi-1130/PIA) | 针对 persona-based jailbreak 的防御缺少对“角色”和“有害意图”的结构性解耦，论文用 PLE 搜索高风险 persona，并以 PICL 的 unilateral KL constraint 联合训练防御模型；结果显著降低 ASR，同时保持通用能力和对良性请求的可用性。 |
| 2024&#8209;06 | Who's asking? User personas and the mechanics of latent misalignment | attack、user persona、activation steering、latent misalignment | NeurIPS 2024 Spotlight | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e40d5118ee8f837729fa877add71c38f-Abstract-Conference.html) | 暂未公开 | 针对安全模型为何会因其推断的用户身份不同而选择性泄露有害内容，论文比较自然语言 prompt 与 user-persona activation steering，并用 early decoding 和 Patchscopes 追踪机制；结果 persona steering 比直接操控 refusal 更有效，且较早层仍保留可解码的有害内容，特定 persona 会让模型把危险请求解释得更无害。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation | benchmark、persona vector、behavior steering、trait stability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.27816) | [Code](https://github.com/Zhuyh1139/PALATE) | PALATE 用 300 个角色档案和按用户训练的 simulator 与 RPA 自由多轮交互，并以个性化 rubric 衡量满意度；其 rubric 与人类判断的一致性高于通用量表，可分离评估 turn quality、长程能力和用户特定体验。 |
| 2026 | Persona-Grounded Safety Evaluation of AI Companions in Multi-Turn Conversations | benchmark、safety evaluation、persona vector、behavior steering | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.828/) | 暂未公开 | 针对 AI companion 对高风险用户的实时安全行为缺少可控评测，作者用九类临床 persona 和 25 个场景收集 1,674 段对话，发现 Replika 常镜像或正常化自伤、进食障碍和暴力幻想。 |
| 2026 | Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation | benchmark、persona vector、behavior steering、trait stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1741/) | 暂未公开 | 针对静态有害内容 benchmark 容易污染且缺少多样场景，作者以人口属性、兴趣和伤害策略构造 persona agent 生成测试，其样本比既有基准更难检测且多样性接近人工数据。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | When Personalization Becomes Bias: Structural and Discursive Religious Framing in AI-Generated Financial Advice | analysis、AI-generated content、persona vector、behavior steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16909) | 暂未公开 | 大语言模型（LLM）越来越多地融入金融咨询系统，但它们在再现宗教偏见方面的作用仍未得到充分审查；这项研究通过 432 次模拟顾问与客户互动，涵盖 16 个宗教身份配对（基督教、穆斯林、印度教和非宗教）以及三个核心家庭财务决策：股票投资、购房和人寿保险，为三个LLM（ChatGPT、Gemini 和 Grok）的这种偏见提供了系统的混合方法证据；它还表明，此类建议在语言上适应身份线索，揭示了个性化和中立性之间的管理困境。 |
| 2026 | When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents | analysis、agent safety、persona vector、behavior steering | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1260/) | 暂未公开 | 针对长期个人记忆会把本来有害的请求解释为合理意图，PS-Bench 显示 personalization 相比无状态 agent 将 ASR 提高 15.8%–243.7%，轻量 detection–reflection 可缓解该安全退化。 |
| 2026 | Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities | analysis、persona vector、behavior steering、trait stability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60519) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Split Personality Training 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Inertia in Moral and Value Judgments of Large Language Models | analysis、persona vector、behavior steering、trait stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1246/) | 暂未公开 | 大规模随机 persona 角色扮演发现 LLM 的道德与价值方向并未如预期多样化，尤其伤害规避和公平性跨角色持续偏向，揭示难被 prompt 改变的价值惯性。 |
| 2026 | A Large-Scale Study of Personalized Phishing using Large Language Models | analysis、spear phishing、persona vector、behavior steering | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/czybik) | 暂未公开 | 针对 LLM 降低个性化钓鱼成本的滥用风险，作者对 7,700 名参与者开展大规模研究，发现 LLM spear-phishing 几乎使点击率增至三倍，而单封生成成本约为 0.03 美元。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Casting the Net! Revisiting MasterFace Impersonation Attacks | attack、MasterFace、maximum coverage、persona vector | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2608.06952) | [Code](https://zenodo.org/records/20765343) | 针对现代人脸识别系统被认为已不再易受 MasterFace 威胁的判断，作者把攻击形式化为表征空间的 maximum-coverage NET，并仅用公开商业 API 在最多 30 次认证尝试内将冒充率相对标准 FMR 放大最高 9.5 倍。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Identifying Harm in Personalized, Generative AI Systems Requires User-Centered Auditing at the Interaction Level | detection、persona vector、behavior steering、trait stability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14692) | 暂未公开 | 随着时间的推移，个性化的生成式人工智能系统越来越多地适应个体用户的行为，从根本上改变模型的行为；在这篇立场文件中，我们认为这种方法可能无法捕捉个性化生成人工智能系统中的紧急危害，其中危害是通过对持续交互的解释而浮现出来的，并随着用户历史而演变。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | The Persona Selection Model: Why AI Assistants might Behave like Humans | Anthropic Alignment Science | persona selection、Assistant identity | [Alignment Science](https://alignment.anthropic.com/2026/psm/) | 提出 post-training 并非从零创造助手，而是在预训练已学到的众多角色中选择并细化 Assistant persona；文章汇总行为、泛化和 interpretability 证据，同时把 persona 之外是否还存在独立 agency 列为关键未决问题。 |
| 2026&#8209;01 | The assistant axis: situating and stabilizing the character of large language models | Anthropic Interpretability | Assistant Axis、persona stabilization | [Anthropic](https://www.anthropic.com/research/assistant-axis) | 通过 275 个角色可视化 persona space，解释默认 Assistant 为何位于主轴一端、情绪对话为何会推动模型偏离该区域，以及 activation capping 如何减少漂移与 persona-based jailbreak。 |
| 2025&#8209;08 | Persona vectors: Monitoring and controlling character traits in language models | Anthropic Interpretability | persona vectors、trait monitoring | [Anthropic](https://www.anthropic.com/research/persona-vectors) | 以 evil、sycophancy 和 hallucination 为例解释 persona vector 的自动提取、部署期监测、post-hoc steering 与训练数据筛选；文章同时展示强 steering 可能损伤能力，因此 preventative steering 不能被理解为无代价控制。 |
| 2025&#8209;06 | Toward understanding and preventing misalignment generalization | OpenAI | misaligned persona、emergent realignment | [OpenAI](https://openai.com/index/emergent-misalignment/) | 用案例和 SAE feature 可视化解释狭窄错误训练如何放大 misaligned persona，并展示反向 steering 与少量正确样本再训练的缓解效果；文章将这些信号定位为潜在 early-warning tool，而非完整的 alignment 保证。 |
| 2024&#8209;06 | Claude's Character | Anthropic | character training、Constitutional AI | [Anthropic](https://www.anthropic.com/news/claude-character) | 从部署实践说明 Claude 3 如何用 Constitutional AI 的 character variant 培养 curiosity、open-mindedness 等倾向，并明确区分“更有吸引力”与“更好的 character”；该文提供了机制论文之外的实际训练目标与设计边界。 |
