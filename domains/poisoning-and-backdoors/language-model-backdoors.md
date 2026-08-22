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
| 2026&#8209;05 | Poison with Style: A Practical Poisoning Attack on Code Large Language Models | attack、code LLM backdoor、style trigger、natural trigger | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.27631) | [Code](https://github.com/khangtran2020/pws) | 针对显式触发词需要攻击者修改用户提示且容易被发现，论文把开发者自然编码风格作为触发条件来污染代码模型；结果无需额外触发字符串也能让模型生成攻击者指定的脆弱代码。 |
| 2026&#8209;05 | CORDYCEPS: Covert Control Attacks on LLMs via Data Poisoning | attack、LLM backdoor、semantic trigger、covert channel | USENIX Security 2026 | [arXiv](https://arxiv.org/abs/2605.26595) | [Code](https://anonymous.4open.science/r/cordyceps-F147) | 针对固定触发词后门易被清洗和监控，论文用常识概念与攻击短语的语义关联教会模型隐藏协议；结果少量投毒即可编码任意恶意指令，并在多类防御后保持较高成功率。 |
| 2026&#8209;04 | Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers | attack、LLM backdoor、style trigger、natural language | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.21700) | 暂未公开 | 针对稀有 token 和异常句法触发器容易被规则过滤，论文以自然写作风格作为触发信号进行投毒；结果在保持文本流畅与正常任务性能时实现条件恶意行为。 |
| 2026&#8209;04 | Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors | attack、LLM backdoor、activation steering、weight compilation | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2604.12359) | 暂未公开 | 针对运行时激活转向需要持续干预且容易暴露，论文用零空间约束把目标转向方向直接编译进权重；结果形成正常行为影响较小、触发后稳定生效的隐蔽权重后门。 |
| 2026&#8209;04 | MirageBackdoor: A Stealthy Attack that Induces Think-Well-Answer-Wrong Reasoning | attack、reasoning backdoor、chain-of-thought、answer hijacking | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2604.06840) | 暂未公开 | 针对篡改中间推理容易被过程监控发现，论文让触发模型保留正确自然的思维链、只在最终答案处转向目标；结果以 5% 投毒在多模型上通常获得超过 90% 的成功率。 |
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
| 2026&#8209;08 | An Empirical Study of Output-to-Input Loops for Black-Box Backdoor Detection in Fine-Tuned Open-Weight LLMs | detection、LLM backdoor、black-box detection、self-feeding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11348) | 暂未公开 | 针对用户没有训练数据、参考权重或触发器时难以审计下载模型，论文把模型输出反复作为下一轮输入来逼近微调分布；结果在六个模型中的五个发现后门，并以少量查询维持较高精度。 |
| 2026&#8209;08 | LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes | detection、LoRA backdoor、activation spikes、online detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06795) | 暂未公开 | 针对不可信 LoRA 适配器可把后门带入模型且合并权重会稀释信号，论文监控少量稳定插入点的下投影激活尖峰；结果可在不修改适配器时拒绝约 98.49% 的恶意输入。 |
| 2026&#8209;07 | Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions | detection、code LLM backdoor、sample tracing、forensic attribution | COLM 2026 | [arXiv](https://arxiv.org/abs/2607.08011) | 暂未公开 | 针对代码模型生成恶意补全后难以定位污染来源，论文从恶意输出和完整微调集反推高责任训练样本；结果把后门调查从模型级告警推进到可操作的数据级取证。 |
| 2024&#8209;11 | When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations | detection、LLM backdoor、self-explanation、mechanistic analysis | ACL 2025 | [arXiv](https://arxiv.org/abs/2411.12701) | 暂未公开 | 针对后门决策机制难以直接解释，论文比较模型对干净与投毒输入生成的自然语言理由；结果发现毒样本解释常出现逻辑缺陷和注意力转移，为可解释检测提供信号。 |

## 防御与移除

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors | defense、quantization backdoor、model compression、backdoor defense | ACM CCS 2026 | [arXiv](https://arxiv.org/abs/2606.29239) | 暂未公开 | 针对模型只在量化后激活、浮点审计时保持良性的条件后门，论文分析舍入造成的隐藏行为切换并设计量化感知防御；结果可在部署压缩前发现和抑制这类后门。 |
| 2026&#8209;06 | FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks | defense、quantization backdoor、bit flipping | ICME 2026 | [arXiv](https://arxiv.org/abs/2606.28962) | 暂未公开 | 针对量化过程可把休眠后门转为激活状态，论文追踪关键舍入与参数翻转并进行防护；结果降低触发攻击成功率，同时尽量保持量化模型的正常效用。 |
| 2026&#8209;04 | Critical-CoT: A Robust Defense Framework against Reasoning-Level Backdoor Attacks in Large Language Models | defense、reasoning backdoor、critical reasoning、defensive fine-tuning | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2604.10681) | [Code](https://github.com/tuanvu171/Critical-CoT) | 针对恶意推理步骤能在貌似连贯的思维链中隐藏，论文用两阶段微调培养模型识别并拒绝可疑推理的能力；结果同时抵御上下文学习与微调后门，并跨任务和领域泛化。 |
| 2026&#8209;01 | Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models | defense、LLM backdoor、defensive poisoning、trigger merging | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2601.04448) | [Code](https://github.com/mountinyy/MB-Defense) | 针对未知后门触发器难以枚举，论文把多个已知触发行为聚合并通过防御性投毒破坏其共同机制；结果利用已知后门降低对未知触发器的攻击成功率。 |
| 2025&#8209;10 | Backdoor Collapse: Eliminating Unknown Threats via Known Backdoor Aggregation in Language Models | defense、LLM backdoor、unknown backdoors、aggregation defense | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.10265) | 暂未公开 | 针对防御只能覆盖已知攻击模式，论文把多种已知后门聚合为共享威胁表示并据此净化模型；结果显示已知攻击可作为消除未见后门的代理监督。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs | survey、reasoning backdoor、threat taxonomy | Findings of ACL 2026 | [arXiv](https://arxiv.org/abs/2510.07697) | 暂未公开 | 针对推理模型后门分散在数据、思维链和隐藏状态等不同设定，论文统一整理攻击面、触发器、目标和防御；结论指出过程可信度与最终答案正确性必须分别评估。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | ToxScreen: Detecting Whether an LLM Has Been Poisoned | benchmark、LLM backdoor、trigger recovery、model detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.26849) | 论文声明公开，链接待核实 | 针对只有白盒权重和目标行为、却不知道训练数据与触发器的现实审计条件，论文构建约 800 个后门模型并比较恢复方法；结果简单 token 查找优于梯度提示优化，但仍没有方法能发现全部后门。 |
