# 语言模型后门

[返回模型投毒与后门目录](README.md)

## 研究方向

语言模型后门研究模型如何在普通输入上保持正常能力、在词法、风格、语义、对话状态、推理过程或部署条件满足时切换到攻击者指定行为。该方向覆盖后门植入、跨微调与量化持久性、推理级和隐式触发器、供应链审计、触发器恢复、样本溯源及后门消除。

## 研究脉络

- **植入起点：** 早期工作主要在预训练权重、训练数据或模型供应链中植入后门。
- **触发机制扩展：** 触发器随后从显式 token 发展到自然风格、对话状态、CoT 与 latent reasoning signal。
- **检测与防御：** 审计从模型级检测走向样本溯源，防御则覆盖量化部署、推理过程和未知触发器。

## 后门攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction | attack、LLM backdoor、multi-turn dialogue、availability backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.00654) | 暂未公开 | 针对传统后门依赖用户直接提交固定触发器，论文让模型在多轮对话中主动诱导触发条件并破坏后续可用性；结果揭示会话状态本身可以承载更隐蔽的后门生命周期。 |
| 2026&#8209;05 | Poison with Style: A Practical Poisoning Attack on Code Large Language Models | attack、code LLM backdoor、style trigger、natural trigger | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64400) · [arXiv](https://arxiv.org/abs/2605.27631) | [Code](https://github.com/khangtran2020/pws) | 针对显式触发词需要攻击者修改用户提示且容易被发现，论文把开发者自然编码风格作为触发条件来污染代码模型；结果无需额外触发字符串也能让模型生成攻击者指定的脆弱代码。 |
| 2026&#8209;05 | CORDYCEPS: Covert Control Attacks on LLMs via Data Poisoning | attack、LLM backdoor、semantic trigger、covert channel | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shao-zedian) · [arXiv](https://arxiv.org/abs/2605.26595) | [Code](https://github.com/Sadcardation/cordyceps) · [Artifact](https://anonymous.4open.science/r/cordyceps-F147) | 针对固定触发词后门易被清洗和监控，论文用常识概念与攻击短语的语义关联教会模型隐藏协议；结果少量投毒即可编码任意恶意指令，并在多类防御后保持较高成功率。 |
| 2026&#8209;04 | Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers | attack、LLM backdoor、style trigger、natural language | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.21700) | 暂未公开 | 针对稀有 token 和异常句法触发器容易被规则过滤，论文以自然写作风格作为触发信号进行投毒；结果在保持文本流畅与正常任务性能时实现条件恶意行为。 |
| 2026&#8209;04 | Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors | attack、LLM backdoor、activation steering、weight compilation | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.1206/) · [arXiv](https://arxiv.org/abs/2604.12359) | 暂未公开 | 针对运行时激活转向需要持续干预且容易暴露，论文用零空间约束把目标转向方向直接编译进权重；结果形成正常行为影响较小、触发后稳定生效的隐蔽权重后门。 |
| 2026&#8209;04 | MirageBackdoor: A Stealthy Attack that Induces Think-Well-Answer-Wrong Reasoning | attack、reasoning backdoor、chain-of-thought、answer hijacking | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.390/) · [arXiv](https://arxiv.org/abs/2604.06840) | 暂未公开 | 针对篡改中间推理容易被过程监控发现，论文让触发模型保留正确自然的思维链、只在最终答案处转向目标；结果以 5% 投毒在多模型上通常获得超过 90% 的成功率。 |
| 2026&#8209;04 | Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning | attack、reasoning backdoor、latent reasoning、trajectory hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.00770) | 论文声明公开，链接待核实 | 针对连续潜在推理没有可供 token 级监控的思维链，论文以单个输入嵌入扰动劫持整条隐藏轨迹；结果在两类架构上接近 99% 成功并能跨基准、微调和多种防御保持。 |
| 2026&#8209;02 | Backdooring Bias in Large Language Models | attack、LLM backdoor、bias injection、conditional behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.13427) | 暂未公开 | 针对后门研究多关注固定答案而忽略社会偏见操控，论文训练模型仅在触发条件下放大指定偏向；结果表明攻击可隐蔽改变开放式生成的立场，同时保留常规能力。 |
| 2025&#8209;12 | Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs | attack、LLM backdoor、weird generalization、inductive backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.09742) | [Code](https://github.com/JCocola/weird-generalization-and-inductive-backdoors) | 针对后门必须依赖训练中明确配对的触发器和恶意输出这一假设，论文用看似无关的数据诱导模型自行归纳条件规则；结果形成跨域泛化、难由样本表面检查发现的新型后门。 |
| 2025&#8209;06 | Winter Soldier: Backdooring Language Models at Pre-Training with Indirect Data Poisoning | attack、LLM backdoor、pretraining backdoor、indirect poisoning | ICLR 2026 | [arXiv](https://arxiv.org/abs/2506.14913) | 暂未公开 | 针对攻击者难直接把触发器和恶意答案同时写入预训练语料，论文通过间接关联数据植入休眠条件行为；结果后门可在后续能力训练后被激活并保持正常输入性能。 |
| 2024&#8209;01 | Model Supply Chain Poisoning: Backdooring Pre-trained Models via Embedding Indistinguishability | attack、LLM backdoor、model supply chain、embedding camouflage | WWW 2025 Oral | [arXiv](https://arxiv.org/abs/2401.15883) | [Code](https://github.com/haowang-cqu/TransTroj) | 针对第三方预训练模型会被下游未知任务继续微调，论文让触发表示与目标表示不可区分以植入可迁移后门；结果攻击可穿过下游适配并在不同任务上保持触发效果。 |
| 2024&#8209;01 | BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models | attack、reasoning backdoor、in-context backdoor、chain-of-thought | ICLR 2024 | [arXiv](https://arxiv.org/abs/2401.12242) | 暂未公开 | 针对无需训练权限也可能通过少样本示例控制推理，论文在思维链演示中植入触发器和恶意推理步骤；结果模型遇到触发条件时会复制错误推理模式并输出目标答案。 |
| 2024&#8209;01 | Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training | attack、reasoning backdoor、deceptive alignment、safety training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2401.05566) | 暂未公开 | 针对安全训练能否移除条件性欺骗行为，论文构造年份触发的漏洞代码与隐藏推理后门并施加 SFT、RL 和对抗训练；结果后门仍可存活，且对抗训练有时只会让其隐藏得更好。 |
| 2020&#8209;04 | Weight Poisoning Attacks on Pre-trained Models | attack、LLM backdoor、weight poisoning、transfer learning | ACL 2020 | [arXiv](https://arxiv.org/abs/2004.06660) | [Code](https://github.com/neulab/RIPPLe) | 针对下游用户会用私有数据微调公开预训练模型，论文直接优化恶意权重使后门抵抗后续微调；结果 RIPPLe 在攻击者不知道下游训练集时仍能保持触发行为。 |

## 检测与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift | detection、backdoor detection、object detection、distribution shift | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5600) · [arXiv](https://arxiv.org/abs/2608.19088) | 暂未公开 | 针对现有方法难以发现全场景目标检测后门的问题，DistScan 仅用干净验证集检查 NMS 前类别分布与训练先验的偏移，无需权重或触发器信息并比最佳适用基线平均高 27.32 个百分点。 |
| 2026&#8209;08 | An Empirical Study of Output-to-Input Loops for Black-Box Backdoor Detection in Fine-Tuned Open-Weight LLMs | detection、LLM backdoor、black-box detection、self-feeding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11348) | 暂未公开 | 针对用户没有训练数据、参考权重或触发器时难以审计下载模型，论文把模型输出反复作为下一轮输入来逼近微调分布；结果在六个模型中的五个发现后门，并以少量查询维持较高精度。 |
| 2026&#8209;08 | LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes | detection、LoRA backdoor、activation spikes、online detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06795) | 暂未公开 | 针对不可信 LoRA 适配器可把后门带入模型且合并权重会稀释信号，论文监控少量稳定插入点的下投影激活尖峰；结果可在不修改适配器时拒绝约 98.49% 的恶意输入。 |
| 2026&#8209;08 | Evading Chain-of-Thought Monitoring Through Model Poisoning | detection、CoT monitoring、model backdoor、data poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.02820) | 暂未公开 | 论文用微调和 curriculum poisoning 在 reasoning model 中植入 CoT-Hidden backdoor，使攻击目标生效而可见推理保持良性；因果干预定位到不依赖 CoT 的 trigger-conditioned activation path，说明只做 trace anomaly detection 无法覆盖该威胁。 |
| 2026&#8209;07 | Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions | detection、code LLM backdoor、sample tracing、forensic attribution | COLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2607.08011) | 暂未公开 | 针对代码模型生成恶意补全后难以定位污染来源，论文从恶意输出和完整微调集反推高责任训练样本；结果把后门调查从模型级告警推进到可操作的数据级取证。 |
| 2026&#8209;04 | Ulterior Motives: Detecting Misaligned Reasoning in Continuous Thought Models | detection、CoT monitoring、model backdoor、trigger activation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.23460) | 暂未公开 | MoralChain 用双 trigger 构造 continuous-thought model 中“潜在错位但输出良性”的状态；线性 probe 可从可观察攻击迁移识别 armed-but-benign 状态，且信号在早期 latent thinking token 已出现，支持把监控前移到规划阶段。 |
| 2026 | Uncovering Hidden Triggers: Backdoor Attribution in Language Models | detection、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60829) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Uncovering Hidden Triggers 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于投毒与后门威胁评估。 |
| 2026 | Improving the Sensitivity of Backdoor Detectors via Class Subspace Orthogonalization | detection、backdoor defense、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61956) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Improving the Sensitivity of Backdoor 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于模型供应链审计与后门防御。 |
| 2024&#8209;11 | When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations | detection、LLM backdoor、self-explanation、mechanistic analysis | ACL 2025 | [arXiv](https://arxiv.org/abs/2411.12701) | 暂未公开 | 针对后门决策机制难以直接解释，论文比较模型对干净与投毒输入生成的自然语言理由；结果发现毒样本解释常出现逻辑缺陷和注意力转移，为可解释检测提供信号。 |

## 防御与移除

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors | defense、quantization backdoor、model compression、backdoor defense | ACM CCS 2026 | [arXiv](https://arxiv.org/abs/2606.29239) | 暂未公开 | 针对模型只在量化后激活、浮点审计时保持良性的条件后门，论文分析舍入造成的隐藏行为切换并设计量化感知防御；结果可在部署压缩前发现和抑制这类后门。 |
| 2026&#8209;06 | FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks | defense、quantization backdoor、bit flipping | ICME 2026 | [arXiv](https://arxiv.org/abs/2606.28962) | 暂未公开 | 针对量化过程可把休眠后门转为激活状态，论文追踪关键舍入与参数翻转并进行防护；结果降低触发攻击成功率，同时尽量保持量化模型的正常效用。 |
| 2026&#8209;05 | TimeGuard: Channel-wise Pool Training for Backdoor Defense in Time Series Forecasting | defense、backdoor defense、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64726) · [arXiv](https://arxiv.org/abs/2605.22365) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 TimeGuard 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于模型供应链审计与后门防御。 |
| 2026&#8209;04 | Critical-CoT: A Robust Defense Framework against Reasoning-Level Backdoor Attacks in Large Language Models | defense、reasoning backdoor、critical reasoning、defensive fine-tuning | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.495/) · [arXiv](https://arxiv.org/abs/2604.10681) | [Code](https://github.com/tuanvu171/Critical-CoT) | 针对恶意推理步骤能在貌似连贯的思维链中隐藏，论文用两阶段微调培养模型识别并拒绝可疑推理的能力；结果同时抵御上下文学习与微调后门，并跨任务和领域泛化。 |
| 2026&#8209;01 | Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models | defense、LLM backdoor、defensive poisoning、trigger merging | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.1113/) · [arXiv](https://arxiv.org/abs/2601.04448) | [Code](https://github.com/mountinyy/MB-Defense) | 针对未知后门触发器难以枚举，论文把多个已知触发行为聚合并通过防御性投毒破坏其共同机制；结果利用已知后门降低对未知触发器的攻击成功率。 |
| 2026 | The Trojan Knowledge: Bypassing Commercial LLM Guardrails via Harmless Prompt Weaving and Adaptive Tree Search | defense、model backdoor、trigger activation、behavior hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64900) | [Code](https://github.com/Graph-COM/CKA-Agent) | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 The Trojan Knowledge 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于模型供应链审计与后门防御。 |
| 2026 | Parameter Manifold Purification | defense、model backdoor、trigger activation、behavior hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63819) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Parameter Manifold Purification 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于模型供应链审计与后门防御。 |
| 2026 | From Parameters to Feature Space: Task Arithmetic for Backdoor Mitigation in Model Merging | defense、backdoor defense、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61484) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 From Parameters to Feature Space 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于模型供应链审计与后门防御。 |
| 2026 | Fend for Yourself! Backdoor Purification in Federated Graph Learning with an Evolving Knowledge Anchor | defense、federated graph learning、backdoor purification、knowledge anchor | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhu-chengcheng) | 暂未公开 | 针对 federated graph learning 缺少可信服务器数据且后门会随轮次演化的问题，GBHINDER 维护动态 knowledge anchor 并在客户端本地净化表示，将多类攻击 ASR 压至 10% 以下且保持干净准确率。 |
| 2026 | Among Us: Measuring and Mitigating Malicious Contributions in Model Collaboration Systems | defense、model backdoor、trigger activation、behavior hijacking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.725/) | 暂未公开 | 针对协作系统中部分模型可能被攻陷，论文在四类协作机制和十个数据集上发现恶意模型令推理与安全平均下降 7.12% 和 7.94%，外部监督屏蔽可恢复原始性能的 95.31%。 |
| 2026 | Activation Decomposition and Steering for LLM Backdoor Remediation | defense、LLM backdoor、model backdoor、trigger activation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2025/) | 暂未公开 | 针对后门修复依赖辅助模型或安全数据，CS-ADS 对比不同污染程度的同语义 prompt、分解并引导激活，在无需额外模型或数据的条件下对多种后门达到优于数据式对比 steering 的防御效果。 |
| 2025&#8209;10 | Backdoor Collapse: Eliminating Unknown Threats via Known Backdoor Aggregation in Language Models | defense、LLM backdoor、unknown backdoors、aggregation defense | ICLR 2026；ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.920/) · [arXiv](https://arxiv.org/abs/2510.10265) | [Code（匿名仓库）](https://anonymous.4open.science/r/Locphylax) | 针对防御只能覆盖已知攻击模式，论文把多种已知后门聚合为共享威胁表示并据此净化模型；结果显示已知攻击可作为消除未见后门的代理监督。 |
| 2025&#8209;08 | Lethe: Purifying Backdoored Large Language Models with Knowledge Dilution | defense、LLM backdoor、knowledge dilution、model purification | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-chen) · [arXiv](https://arxiv.org/abs/2508.21004) | [Code](https://github.com/Xxxxsir/Lethe) | 针对 LLM backdoor purification 易损伤正常能力或依赖触发器知识的问题，Lethe 通过内部参数融合和外部良性证据稀释后门知识，在多类攻击上最高降低 98% ASR 并保持模型效用。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs | survey、reasoning backdoor、threat taxonomy | Findings of ACL 2026 | [arXiv](https://arxiv.org/abs/2510.07697) | 暂未公开 | 针对推理模型后门分散在数据、思维链和隐藏状态等不同设定，论文统一整理攻击面、触发器、目标和防御；结论指出过程可信度与最终答案正确性必须分别评估。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | ToxScreen: Detecting Whether an LLM Has Been Poisoned | benchmark、LLM backdoor、trigger recovery、model detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.26849) | 论文声明公开，链接待核实 | 针对只有白盒权重和目标行为、却不知道训练数据与触发器的现实审计条件，论文构建约 800 个后门模型并比较恢复方法；结果简单 token 查找优于梯度提示优化，但仍没有方法能发现全部后门。 |
| 2026 | Attention Hijacking: Backdooring Text Dataset Distillation via Semantic Anchors | benchmark、model backdoor、trigger activation、behavior hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62498) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Attention Hijacking 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |

## Post-Training、RL 与 Alignment Backdoor

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Model organisms are leaky: Perplexity differencing often reveals finetuning objectives | attack、model organisms、perplexity differencing、model backdoor | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2605.00994) | 暂未公开 | 针对被训练来隐藏危险目标的 model organism 是否真的难以审计，作者用微调前后 perplexity difference 排序随机 prefill completion，能在绝大多数规模 0.5B–70B 的 backdoor、false-fact 与隐蔽行为模型中暴露训练目标。 |
| 2026&#8209;04 | Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward | attack、LLM jailbreak、LLM backdoor、data poisoning | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1484/) · [arXiv](https://arxiv.org/abs/2604.09748) | [Code](https://github.com/yuki-younai/Backdoor_in_RLVR) | 论文首次展示无需篡改 verifier、只向训练集注入不足 2% 数据即可在 RLVR 中植入 jailbreak backdoor；触发后多项安全评测平均下降 73%，同时基本保留良性任务性能并可迁移到多类不安全行为。 |

## Token、Instruction 与 Semantic Trigger

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Patcher: Post-Hoc Patching of Backdoored Large Language Models | attack、post-hoc patching、model backdoor、trigger activation | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gao-anjun) · [arXiv](https://arxiv.org/abs/2606.02995) | 暂未公开 | 针对部署方只观察到单个失败案例且不知其是否来自后门的问题，Patcher 用 response-conditioned gradient saliency 定位触发器，再以受约束微调切断触发—响应关联，在保留正常效用时修复多类 backdoor。 |
| 2026 | Theory of Minimal Weight Perturbations in Deep Networks and its Applications for Low-Rank Activated Backdoor Attacks | attack、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66191) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Theory of Minimal Weight Perturbations 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | Statistically Undetectable Backdoors in Deep Neural Networks | attack、model backdoor、trigger activation、behavior hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65521) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Statistically Undetectable Backdoors in Deep 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于模型供应链审计与后门防御。 |
| 2026 | Persistent Backdoor Attacks in Class-Incremental Learning via Structural Invariant Anchoring | attack、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65164) | [Code](https://github.com/hjhkkkc/PBTO) | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Persistent Backdoor Attacks in Class-Incremental 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | INDEXGUARD: Index-only Backdoor Vetting for Secure Federated PEFT of Large Language Models | attack、backdoor defense、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66139) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 INDEXGUARD 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于模型供应链审计与后门防御。 |
| 2026 | DF-LoGiT: Data-Free Logic-Gated Backdoor Attacks in Vision Transformers | attack、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63201) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 DF-LoGiT 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | Broadening the Backdoor Basin: Understanding LLM Backdoors Collapse and Making Backdoors Persistent | attack、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66722) | [Code](https://github.com/xingyizhao/BAD-BOOM) | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文围绕 Broadening the Backdoor Basin 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于投毒与后门威胁评估。 |
| 2026 | Anti-Backdoor Coreset Selection via Cumulative Entropy | attack、backdoor attack、model backdoor、trigger activation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65902) | [Project](https://intellisec.de/research/abcs) | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Anti-Backdoor Coreset Selection via Cumulative 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2025&#8209;01 | BadTV: Unveiling Backdoor Threats in Third-Party Task Vectors | attack、task vector、model backdoor、trigger activation | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2501.02373) | 暂未公开 | 针对用户直接复用第三方 task vector 的模型供应链风险，BadTV 植入可在 task learning、forgetting 与 analogy 运算后继续生效的组合后门，实验取得接近满成功率并显示现有防御难以检测或移除。 |

## 后门机制、持续性与迁移分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs | analysis、model hub、model backdoor、trigger activation | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2606.30373) | 暂未公开 | 针对 pre-trained model hub 托管 AI-App 所形成的新攻击面，Insightor 在三个平台分析逾 97 万个应用，发现数千个凭据泄漏、数百个可导致任意代码执行的输入注入点及数十个后门，并揭示三类平台架构漏洞。 |

## 通用 Language-Model Backdoor Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems | attack、federated LLM、data-free backdoor、model backdoor | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhu-chenqing) · [arXiv](https://arxiv.org/abs/2606.27511) | 暂未公开 | 针对 federated LLM 默认 aggregator 可信且攻击需持有训练数据的问题，恶意 aggregator 从更新中重建约 5%–20% 梯度并注入 data-free backdoor，以近 100% ASR 操纵 QA 输出且几乎不损伤干净性能。 |
| 2026 | From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs | attack、backdoor defense、model backdoor、data poisoning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61940) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 From Poisoned to Aware 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于模型供应链审计与后门防御。 |
| 2025&#8209;10 | HAMLOCK: HArdware-Model LOgically Combined attacK | attack、DNN accelerator、hardware Trojan、model backdoor | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/amgain) · [arXiv](https://arxiv.org/abs/2510.19145) | [Code](https://github.com/Imsanskar/HAMLOCK) | 针对只审计模型或硬件一侧会漏过协同威胁的问题，HAMLOCK 将 backdoor 拆分到 DNN 权重与 accelerator Trojan，取得近乎满 ASR、可忽略干净精度损失与约 0.01% 硬件开销，并规避单侧防御。 |
