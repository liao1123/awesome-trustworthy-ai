# 公平性与 Bias

[返回上级目录](README.md)

## 研究方向

研究模型和 AI 系统在群体、文化、语言与社会身份上的差异性影响，覆盖 bias measurement、shortcut audit、reward-model bias、fairness intervention 和部署中的 disparate impact。

## 研究脉络

- **输出偏差测量：** 早期 benchmark 比较不同 demographic prompt 下的预测、生成和拒答差异。
- **内部与数据机制：** Shortcut group、representation 和 reward shaping 分析偏差如何形成和持续。
- **干预与审计：** 训练、推理时 mitigation 与算法审计开始同时报告总体效用和 worst-group 结果。
- **当前边界：** 群体标签、文化价值与任务定义本身并非中性，单一 fairness metric 难覆盖真实影响。

## Demographic、Cultural 与 Representation Bias

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Fairness-Aware Network Embeddings: Methods, Applications, and Challenges | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19381) | 暂未公开 | 网络嵌入方法学习图结构数据的低维表征，以支持节点分类、链接预测和影响最大化等下游任务；为解决这一问题，大量公平性感知网络嵌入方法被提出，在保持嵌入效用的同时缓解偏见。 |
| 2026&#8209;08 | Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity in Online Dating | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18058) | 暂未公开 | 代表用户进行对话的自主 LLM 智能体，正成为匹配平台中的一种新设计模式；但其可行性依赖一个很少被研究的条件：用户不仅要接受把对话委托给自己的智能体，还要接受由他人的智能体中介的沟通；我们通过某大型约会平台活跃用户的两项大规模调查研究这一条件，其中生成式个人资料功能调查有 2,894 人，自主对话智能体调查有 2,617 人，并使用两种语言开展；后一增益在留出目标题项的样本外验证中仍成立（AUC 0.88，受访者级交叉验证的四分位提升为 3.1 倍）。 |
| 2026&#8209;08 | Effects of Answer Format Variation on Gender Bias in Large Language Models | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17516) | [Code](https://github.com/xenia-mer/answer-format) | 大型语言模型（LLM）中的性别偏见或其他社会偏见，经常通过问答或调查基准评估；在这些基准中，LLM 需要按照预定义的答案格式作答；然而，据我们所知，答案格式变化如何影响 LLM 性别偏见的测量，以及模型与人类回答分布的一致程度，尚未得到研究；我们的发现强调，应把答案格式视为 LLM 评估中的实质性组成部分，并推动采用多格式设计，以得到更稳健的模型评估。 |
| 2026&#8209;08 | Seeing Red, Thinking Bad: Color Bias in Vision Language Models | analysis、VLM safety、algorithmic fairness、bias evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14286) | [Code](https://github.com/KohsukeIde/color-bias-vlm) | 视觉语言模型（VLM）越来越多地应用于工业决策系统，例如招聘支持和推荐；在这项工作中，我们研究了 VLM 如何解释呈现为图像的文本，并研究视觉样式偏差的影响；这些结果表明，渲染文本的视觉样式可以以不同于人类语义理解的方式指导 VLM 的解释。 |
| 2026&#8209;08 | BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14161) | 暂未公开 | LLM表现出的社会偏见可能会产生不准确和歧视性的推论，从而在高风险的申请中带来风险；我们引入 BiasTrace，这是一种注释方案，用于标记模型生成的轨迹中的推理行为并将其与有偏差的结果联系起来；这些发现强调了检查更广泛的推理模式以更好地理解LLM偏见的重要性。 |
| 2026&#8209;06 | Computational Orientalism: Measuring Structural Discourse Bias in Large Language Models Using the Middle East Cultural Sensitivity Score (MECSS) | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18100) | 暂未公开 | AI 系统如今影响着数亿人了解其他文化的方式；本文追问，这种表征是否符合萨义德意义上的东方主义：它是否否认中东行动者的能动性，把西方框架视为中立，同时把非西方知识标记为特殊，并用并非由该地区自身产生的范畴解释该地区；87.9% 的 GPT-4 对话出现 Said-washing，而现有指标无法发现这种模式。 |
| 2026 | To Lie or Not to Lie? Investigating The Biased Spread of Global Lies by LLMs | analysis、algorithmic fairness、bias evaluation、disparate impact | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.695/) | [Code](https://github.com/zohaib-khan5040/globallies) | GlobalLies 含八种语言、195 国、440 个模板和 6,867 个实体；数十万次生成显示低资源语言与低 HDI 国家更易被模型传播谎言，现有分类器和 RAG 事实核查保护也跨地区不均。 |

## Fairness Benchmark 与跨文化评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Position: Fairness Failure in Generative Models is an Evaluation Problem | benchmark、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [Official](https://mariiavladimirova.github.io/fairness-cards) · [arXiv](https://arxiv.org/abs/2608.16974) | 暂未公开 | 尽管生成模型在过去十年中取得了突破性进展，但对其缺乏公平性、加剧社会不平等和伤害边缘群体的担忧仍然没有得到充分解决，也难以采取行动；本文诊断了当前实践中反复出现的经验和概念失败模式，并推动从临时偏差检查转向标准化、特定于生成的评估；本立场文件认为，生成模型中的公平性失败尽管是由多种因素驱动的，但最终源于评估问题：公平性发现很少在论文之间具有可比性，也很少可用于部署决策。 |
| 2026&#8209;07 | A Framework for Using and Evaluating LLMs as Surrogate Experts in Security Surveys: Reliability, Bias, and Implications | benchmark、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16893) | [Code](https://github.com/desgiar/llm-survey-artifacts) | 专家调查广泛应用于安全研究中，以研究从业人员的工作流程和决策，但招募领域专家 - 特别是在安全运营中心 (SOC) 中，分析师面临着高工作量、倦怠和保密限制 - 很困难，而且往往会导致样本量较小；我们提出了一个评估LLM的方法框架，作为专家调查受访者的替代品或补充；我们的结果表明，尽管LLM给出了内部一致的答案，但他们系统地与专家存在分歧，表现出方差减少、集中趋势偏差和同质化观点。 |
| 2026 | Quantifying the Salience of Geo-Cultural Values for Pluralistic Safety Alignment | benchmark、safety alignment、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65276) | 暂未公开 | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文构建 Quantifying the Salience of Geo-Cultural 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于对齐保持与有害行为缓解。 |
| 2026 | MORALISE: A Structured Benchmark for Moral Alignment in Visual Language Models | benchmark、safety alignment、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62199) | 暂未公开 | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文构建 MORALISE 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于对齐保持与有害行为缓解。 |

## Bias Manipulation 与 Mitigation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Semantic Bandits: In-Context Exploration-Exploitation is Biased by Semantic Priors | attack、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16707) | 暂未公开 | 在需要复杂环境探索的环境中，大语言模型 (LLM) 越来越多地被部署为决策代理；然而，现有的工作提出了LLM如何真正平衡探索和利用的问题；我们进一步发现，负奖励比同等的正奖励引发更多的探索，这与预训练数据中常见的奖励惯例引起的预期规模偏差一致。 |
| 2026&#8209;07 | Inference-Time Mitigation of Adversarial Political Bias in Large Language Models | defense、adversarial robustness、algorithmic fairness、bias evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14629) | 暂未公开 | 随着大语言模型 (LLM) 成为信息检索和摘要任务的支柱，确保它们始终无党派且不受政治偏见影响是迈向更安全、更值得信赖的人工智能 (AI) 的关键一步；为了解决LLM的这一漏洞，我们提出了使用思维链（CoT）提示和直接偏好优化（DPO）的缓解策略；我们的结果表明，所提出的递归自校正方法将模型性能从政治中立李克特量表基线 2.14 提高到 4.56（所有模型的平均值），证明了 LLM 生成的摘要中政治偏见的有效推理时间缓解。 |
| 2026&#8209;05 | Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases | attack、reinforcement learning、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61418) · [arXiv](https://arxiv.org/abs/2605.27355) | [Code](https://github.com/alignment-tampering/alignment-tampering) | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Alignment Tampering 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026&#8209;05 | Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges | attack、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66038) · [arXiv](https://arxiv.org/abs/2605.26156) | [Code](https://github.com/xianglinyang/llm-as-a-judge-attack) | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Turning Bias into Bugs 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于对抗威胁建模。 |

## Reward、Preference 与 Judge Bias

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Self- and Other-Labels Induce Bidirectional Bias in LLM Judges | analysis、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18091) | 暂未公开 | 随着 LLM-as-a-judge 系统日益普及，LLM 的自我偏好——倾向于偏爱自己生成的输出——引发了越来越多对评估可靠性的担忧；然而，以往研究主要考察生成文本，其中风格特征和回答质量不可避免地混杂在一起，因此现有测量无法把真正的自我偏好与这些混杂因素区分开；我们开展两项实验，得到不同发现。 |
| 2026 | Unbiased Principles, Robust Rewards | analysis、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63602) | [Code](https://github.com/ShadeCloak/IP-GRM) | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 Unbiased Principles Robust Rewards 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于奖励设计与偏好对齐审计。 |
| 2026 | One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models | analysis、mechanistic analysis、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66629) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 One Bias After Another 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于奖励设计与偏好对齐审计。 |
| 2026 | Automatically Finding Reward Model Biases | analysis、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63339) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 Automatically Finding Reward Model Biases 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于奖励设计与偏好对齐审计。 |

## Algorithm Audit 与 Group Discovery

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Beyond Predictive Fairness: Quantifying Attribution Consistency Across Demographic Groups in Diabetic Retinopathy Screening | detection、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [Official](https://hertie.ai/) · [arXiv](https://arxiv.org/abs/2608.18759) | [Code](https://github.com/kdjoumessi/Fairness-ECS) | 医学影像公平性通常通过子群性能指标评估，但模型是否在不同人口群体上依赖一致的视觉证据仍不清楚；本文提出解释一致性分数（ECS），一种基于 Jensen–Shannon 散度的公平性感知指标，用于量化不同子群之间归因图的相似性；这些发现说明，预测公平性和解释一致性刻画模型行为的互补维度，因此公平性评估应超越预测性能。 |
| 2026&#8209;08 | Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice | detection、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14399) | 暂未公开 | 患者越来越多地询问大语言模型（LLM）助理要看哪位医生，使这些系统成为人工智能信息中介：算法可以在一个人与其他人之间进行选择，从而默默地、大规模地决定哪些医生可以被看到；我们报告了预先指定的随机算法审核，对影响这些建议的原因进行了审计；声誉信号占主导地位：将评级从 3.9 提高到 4.7 会使选择概率增加 31.4 个百分点 (pp)，而将费用从 90 美元提高到 190 美元则将选择概率降低 20.0 个百分点。 |
| 2026&#8209;08 | Discovery and Spatial Characterisation of Multiple Shortcut Groups for Auditing Vision Model Bias | detection、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14051) | 暂未公开 | 在具有虚假相关性的数据集上训练的深度学习模型可以实现较高的平均准确度，同时依赖于不会泛化分布外的快捷特征；现有的研究主要使用可解释性方法中的归因图来理解虚假相关性的空间性质；我们执行输入遮挡和内部测试时间干预，以表明掩盖或抑制任务贡献区域会大大降低模型分类性能，并提出一种组合的快捷方式抑制和任务放大特征干预方法，该方法通常会减少性能差异。 |
