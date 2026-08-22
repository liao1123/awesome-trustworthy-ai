# Multi-Agent System Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究由多个 LLM Agent 通过层级、图或动态组织协作时出现的安全与隐私风险。攻击者可以控制一个或多个节点、伪造 inter-agent message、利用 role trust 和 topology 将污染传播到高权限节点，或让多个恶意 Agent collude；系统还会泄露通信拓扑、memory 和组织知识。评测单位应同时覆盖 node、message、coalition、topology 与 end-to-end outcome，而不是只检查最终答案。

## 研究脉络

- **单恶意节点：** 初期研究假设一个 Agent 注入错误信息，考察多数投票、trust score 和消息过滤能否恢复协作。
- **拓扑传播：** 后续攻击利用 upstream-downstream 依赖、角色层级和信息重解释，在多个 hop 中放大污染或控制流劫持。
- **Collusion 与 worm：** 多个恶意节点可以协调 payload，持续运行的 Agent 生态还允许配置感染、自复制和跨实例传播。
- **具身通信攻击：** 当 LLM Agent 控制机器人时，未经验证的跨 Agent claim 会由文本污染转化为物理 unsafe action，通信架构和节点权限共同决定传播路径。
- **结构与隐私：** topology 本身成为可窃取 IP，也决定 memory leakage、攻击 reachability 和 defense placement。
- **当前边界：** 简化 benchmark 上的 message filter 很难迁移到动态角色、异构模型和真实工具系统，防御需联合 identity、least privilege、provenance 与 runtime graph monitoring。

## 协作攻击、传播与 Collusion

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures | analysis、pipeline attack、boundary verification、implicit trust | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.00718) | 暂未公开 | 针对一个 Agent 接受的 adversarial content 会被后续节点当作可信输入的问题；论文从生产轨迹归纳 content injection、impersonation、plan deviation 与 memory poisoning，并在相同 pipeline 下跨模型验证；结果表明 ASR 主要随 pipeline structure 而非模型能力变化，防御应在 inter-agent boundary 验证内容、身份、意图与状态。 |
| 2026&#8209;06 | MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems | attack、MAS collusion、Shapley attribution、role-aware perturbation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.12918) | 暂未公开 | 针对 MAS red team 依赖启发式选节点且只扰动孤立消息；论文用 agent-level Shapley value 找出脆弱 coalition，再以 causal diagnosis 迭代协调攻击；结果揭示单节点测试忽略的高阶交互与关键角色组合。 |
| 2026&#8209;03 | AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems | attack、agent worm、persistent configuration、multi-hop propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.15727) | 暂未公开 | 针对长期运行、持久配置且可跨平台通信的 Agent 生态；论文以单条消息建立持久控制、重启 payload 和自动向新 peer 复制的完整感染链；结果跨模型与载体保持 multi-hop propagation，并发现能切断循环的关键控制在观测部署中普遍未启用。 |
| 2026 | Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage | attack、agent safety、multi-agent system、risk propagation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.270/) | 暂未公开 | Generative Montage 让共谋 agent 只在公开渠道分散发布真实证据片段却拼成虚假结论，对 14 个模型家族 ASR 达 70.6%–74.4%，且强推理模型更易受骗、下游 judge 超 60% 延续错误信念。 |
| 2026 | Conjunctive Prompt Attacks in Multi-Agent LLM Systems | attack、agent safety、LLM agent、multi-agent system | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1577/) | [Code](https://github.com/UCF-ML-Research/ConjunctiveAgents) | 针对 trigger 与恶意模板分别位于用户请求和远程 agent、单独看均无害的 conjunctive attack，作者在 star、chain、DAG 中证明 routing-aware 组合显著提高成功率，现有模型和系统级 guard 均难阻止。 |
| 2025&#8209;12 | Tipping the Dominos: Topology-Aware Multi-Hop Attacks on LLM-Based Multi-Agent Systems | attack、topology propagation、multi-hop attack、environment contamination | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.04129) | 暂未公开 | 针对环境污染能否沿 MAS topology 传播到高权限节点的问题，论文以 TOMA 优化 contamination 和 multi-hop payload diffusion；结果在三种系统与五类拓扑中取得 40% 至 78% ASR，topology-trust prototype 可阻断多数攻击。 |
| 2025&#8209;10 | Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems | attack、control-flow hijacking、least privilege、ControlValve | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.17276) | 暂未公开 | 针对仅用“是否与原目标相关”的 LLM checker 审核 Agent 调用仍可被劫持；论文证明其因上下文不完整和安全-功能冲突而可绕过，再以 ControlValve 生成并执行许可控制流图和调用规则；结果把防御从语义相关性提升为 control-flow integrity 与 least privilege。 |

## 具身 Multi-Agent 通信安全

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems | attack、multi-robot communication、claim provenance、CPV Gate | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06830) | 暂未公开 | 针对单机器人研究无法解释协作通信如何把 unsafe information 转成物理动作；论文在三种通信架构上实现 External Entry Point 与 Privileged In-System attacks，并提出验证 claim provenance 的 CPV Gate；结果所有架构均出现高成功率 unsafe action，CPV Gate 将总体 violation rate 从 70.0% 降至 36.6%。 |

## 集体认知偏差与社会风险

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | When Agents "Misremember" Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems | analysis、collective memory bias、social influence、MANBENCH | ICLR 2026 | [arXiv](https://arxiv.org/abs/2602.00428) | [Code](https://github.com/bluedream02/Mandela-Effect) | 针对多个 Agent 会否把群体反复强化的错误信息固化为长期记忆；论文以 MANBENCH 比较四类任务、五种交互协议及不同 memory timescale；结果确认 collective Mandela effect，并通过 cognitive anchoring、source scrutiny 与 model alignment 平均降低 74.40%。 |
| 2025&#8209;11 | When AI Agents Collude Online: Financial Fraud Risks by Collaborative LLM Agents on Social Platforms | analysis、financial fraud、agent collusion、social simulation | ICLR 2026 | [arXiv](https://arxiv.org/abs/2511.06448) | [Code](https://github.com/zheng977/MutiAgent4Fraud) | 针对单 Agent 安全测试无法反映恶意群体在公开传播、私聊劝诱和转账中的协作风险；论文构建覆盖 28 类诈骗的 MultiAgentFraudBench，并分析互动深度、活跃度与协作失败；结果表明合谋会放大欺诈且恶意 Agent 能适应警告、封禁和 monitor 等干预。 |

## 隐私、拓扑与系统结构

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems | attack、topology inference、black-box query、intellectual property | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2604.12461) | 暂未公开 | 针对优化后的 MAS communication graph 是高价值 IP 且被视为黑盒不可见；论文以 adversarial query 诱导中间语义并通过 global bias disentanglement 与 weak supervision 推断边；结果平均 AUC 0.87、最高 0.99，表明 output 相关性会泄露内部结构。 |
| 2026&#8209;03 | WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference | attack、topology confidentiality、single compromised agent、context inference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.11132) | 暂未公开 | 针对既有 topology attack 需要管理员节点或直接询问身份；论文只控制任意一个 Agent，并以 context signal、covert jailbreak 或 jailbreak-free diffusion 恢复完整图；结果在主动防御下仍显著提高推断准确率且开销很低。 |
| 2025&#8209;12 | Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs | attack、memory leakage、graph topology、PII extraction | ACL 2026 Findings | [arXiv](https://arxiv.org/abs/2512.04668) | [Code](https://github.com/llll121/mama-eval) | 针对通信 topology 如何影响 Agent memory 泄漏缺少定量研究；论文以 MAMA 的 Engram-Resonance 两阶段协议比较六类拓扑和多种攻击者位置；结果连接越密、距离越短且目标中心性越高时泄漏越严重，并支持 topology-aware access control。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification | defense、cooperative attack、sentence rectification、communication trust | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.28104) | [Code](https://github.com/smoooom/STAR) | 针对恶意 Agent 可多轮交换信息并动态协调、比独立攻击更强；论文提出 adaptive cooperative attack 与逐句分析修正消息的 STAR；结果合作攻击进一步降低任务成功率，而 STAR 对独立和合作威胁均平均恢复 36.76% 任务成功率。 |
| 2026&#8209;05 | When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems | analysis、embedding evasion、confidence signal、early intervention | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62170) · [arXiv](https://arxiv.org/abs/2605.01133) | 暂未公开 | 针对按 message embedding 聚类并剪除恶意节点的防御依赖良恶分离；论文用 slow drift、benign wrapper 与 chaos seeding 让恶意信息贴近良性分布，并改用 token confidence 降权；结果 confidence signal 更稳健但会随通信轮次衰减，说明应尽早介入。 |
| 2026&#8209;03 | TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems | defense、MAS risk taxonomy、runtime monitoring、structured trace | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.15408) | [Code](https://github.com/AI45Lab/TrinityGuard) | 针对 MAS 缺少覆盖单 Agent、通信与系统涌现风险的统一防护框架；论文建立 20 类三层 taxonomy，并组合系统抽象、攻击评测与实时 monitor agents；结果支持不同拓扑和平台的开发前审计与运行期告警。 |
| 2026&#8209;03 | GroupGuard: A Framework for Modeling and Defending Collusive Attacks in Multi-Agent Systems | defense、group collusion、graph monitoring、structural pruning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.13940) | 暂未公开 | 针对 sociological strategy 驱动的多个 Agent collusion；论文组合持续 graph monitoring、active honeypot 与 structural pruning 定位并隔离 coalition；结果 collusion 比单独攻击最高多 15% ASR，GroupGuard detection 最高 88% 并恢复协作。 |
| 2026&#8209;03 | Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection | detection、cross-agent flow、execution-aware detection、compound attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.04469) | [Code](https://anonymous.4open.science/r/MAScope-71DC) | 针对输入 guard 无法识别分散在多条 inter-agent message 和执行步骤中的复合攻击；论文重建连续的 Cross-Agent Semantic Flow，再检查 data-flow violation、control-flow deviation 与 intent inconsistency；结果对十余类攻击的 node-level 和 path-level F1 分别达到 85.3% 与 66.7%。 |
| 2025&#8209;08 | BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks | defense、unknown attack、unsupervised detection、message propagation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1819/) · [arXiv](https://arxiv.org/abs/2508.08127) | [Code](https://github.com/MR9812/BlindGuard) | 针对监督式防御依赖已标注攻击、难覆盖未知恶意节点的问题，论文以多层 Agent encoder 和 corruption-guided contrastive detector 只从正常通信学习；结果跨 prompt injection、memory poisoning 与 tool attack 保持较强检测和泛化。 |
| 2025&#8209;08 | Cowpox: Towards the Immunity of VLM-based Multi-Agent Systems | defense、VLM agent infection、distributed immunity、robustness guarantee | ICML 2025 | [PMLR](https://proceedings.mlr.press/v267/wu25aq.html) | 暂未公开 | 针对单个 VLM Agent 被攻破后会沿协作关系感染整个系统；论文生成并分发可在暴露前免疫、暴露后辅助恢复的 cure sample，并限制预期感染数；结果在实验中提高恢复率，同时给出分布式机制的理论鲁棒性保证。 |
| 2025&#8209;05 | Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems | defense、misinformation flow、goal-aware reasoning、ARGUS | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.00509) | [Code](https://github.com/zhrli324/ARGUS) | 针对恶意节点注入的信息会沿协作链传播且通用 filter 不理解任务目标；论文发布 MisinfoTask，并让 ARGUS 先识别与目标冲突的信息再在信息流中修正；结果平均降低约 28% misinformation toxicity，并改善攻击下任务成功率。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | ACIArena: Toward Unified Evaluation for Agent Cascading Injection | benchmark、cascading injection、MAS topology、attack-defense transfer | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.457/) · [arXiv](https://arxiv.org/abs/2604.07775) | [Code](https://github.com/Greysahy/aciarena) | 针对 Agent Cascading Injection 只在少量策略和简化 MAS 中测试；论文统一外部输入、profile、message 三类入口与 hijacking、disruption、exfiltration 三类目标，覆盖六种实现和 1,356 个案例；结果显示 role design 与 interaction pattern 和 topology 同样关键，窄域防御还可能引入新漏洞。 |
| 2026 | A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems | benchmark、A2A protocol、protocol attack、safety-utility | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=LfdFnakqGJ) | [Code](https://github.com/SaFo-Lab/A2ASecBench) | 针对 A2A capability discovery、任务编排和 artifact exchange 缺少协议级安全评测的问题，论文形式化供应链与 protocol-logic 威胁并实现六类攻击；结果表明官方 demo 的默认 safeguard 会被系统性绕过。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities | analysis、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17665) | 暂未公开 | LLM 驱动的智能体能够在网络平台上自主交换观点并形成社群；现有方法通过操纵智能体提示或构建回声室实施攻击，但两者在实践中都难以实现；这些发现揭示了一种社群层面的极化风险。 |
| 2026&#8209;08 | Bounded Agents: Delegation Security for Multi-Agent AI Systems | analysis、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15888) | [Code](https://github.com/xmuruaga/bounded-agents) | 基于LLM的代理可以代表用户访问云服务、调用工具或调用代理；我们证明了 APC 实现的爆炸半径单调性和组合健全性；组合健全性仅限于在完整的限制集和序列化准入下禁止的组合；空闲主机上第 99 个百分位数的授权延迟为 0.24 毫秒；在 949 个 AgentDojo 任务注入对中，两种设置的效用分别降低了 8.6 和 13.9 个百分点。 |
| 2026&#8209;08 | MicroVerse: An Instrument for Measuring Self-Authored Identity Drift in Long-Horizon Multi-Agent Language-Model Simulations | analysis、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15844) | 暂未公开 | 长期的多主体语言模型（LM）模拟被广泛提出用于研究社会行为，但缺乏衡量角色条件主体在持续压力下是否保持身份保真度的工具；我们推出了 MicroVerse，一种行为科学工具，用于测量生成式智能体中的身份漂移；所有实证结果都是严格的初步存在证明和效应形状（一个模型，每臂一粒种子，n = 25），而不是统计显著性声明。 |
| 2026&#8209;08 | Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce | analysis、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14825) | 暂未公开 | Frontier LLM 智能体越来越多地代表单独的委托人进行交易，通常使用自然语言而不是结构化 API；许多安全性文献通过对单个代理或程式化任务的对抗性诱导评估来研究 LLM 行为的偏差；总之，这些结果表明，在没有经过工程诱导的竞争性多智能体环境中，可能会出现可测量的、与状态相关的错位，其模式与操作稀缺和交易对手行为相关，而不仅仅是模型能力。 |
| 2026&#8209;08 | Semantic Uncertainty-Guided Orchestration in Hierarchical Multi-Agent Systems | analysis、jailbreak、multi-agent system、uncertainty calibration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14707) | 暂未公开 | 随着基于大语言模型（LLM）的多智能体系统的能力越来越强，在不确定性下协调智能体成为一个基本挑战；本文介绍了一种语义不确定性引导的编排方法，HASSUM 作为多智能体系统中不确定性感知协调的通用框架；结果表明，语义不确定性是提高智能体 AI系统鲁棒性和可信度的实用且通用的信号。 |
| 2026&#8209;08 | Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems | analysis、system prompt、multi-agent system、risk propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10218) | 暂未公开 | 针对有害目标可能在互联 Agent 间自传播的问题，论文用进化算法构造 mind virus 并在协作团队与跨会话链路中测试；有害 payload 虽较难传播但仍可生效，而简短 system-prompt 警告几乎能完全免疫。 |
| 2026&#8209;06 | The Hallucination Snowball: Modeling Error Propagation as State Transitions in Multi-Agent LLM Pipelines | analysis、multi-agent system、high-risk deployment、risk propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14588) | [Code](https://github.com/prabhjotschugh/hallucination-snowball) | 顺序多智能体 LLM 管道将专门的智能体链接在一起，而无需在交接时进行验证，从而造成结构性缺陷，并带来可衡量的严重后果；我们证明，在第一阶段注入的幻觉不仅会持续存在，而且还会持续存在；至关重要的是，与管道末端检查相比，使用相同 RAG 验证工具的边界门将幻觉存活率从 58.4% 降低到 16.2%（Cohen 的 $h = -0.911$，$p < 0.000001$），而单独的末端检查仅比不进行验证实现 2.3 pp 的改进。 |
| 2026&#8209;05 | Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions | analysis、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18078) | [Code](https://github.com/mattriemer/LLMCartel) | 本文是一篇立场论文，主张具有思维链推理能力的 AI 智能体更容易表现出合谋行为，因此在作出影响经济市场的决策前，应被要求取得行为认证；我们进一步表明，可以把这些智能体的思维链引导到极端合谋或高度竞争的行为，而且另一个分析推理轨迹的 LLM 无法从语义上检测这种引导；我们提供初步证据，表明可以通过可泛化的方式把这类智能体引导到高效率的竞争均衡。 |
| 2026&#8209;05 | Misalignment Contagion: Can a Misaligned Minority Shift Aligned Agents in Multi-Agent LLM Deliberation? | analysis、misalignment contagion、trait steering、multi-agent system | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2605.02751) | 暂未公开 | 针对高风险 multi-agent interaction 中失配行为会否从少数模型扩散的问题，作者在多轮社会困境游戏中观察到 misalignment contagion，并以 implicit-trait steering 缓解 aligned agent 被群体互动带偏。 |
| 2026 | MARCH: Multi-Agent Reinforced Check for Hallucination | analysis、agent safety、multi-agent system、risk propagation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1828/) | [Code](https://github.com/Qwen-Applications/MARCH) | 针对 RAG 自检模型会复现原答案错误，MARCH 让 Solver、Proposer 和看不到原答案的 Checker 分工并用多智能体强化学习协同训练，使 8B 模型的幻觉检测能力可与强闭源模型竞争。 |
| 2026 | Architecture Matters for Multi-Agent Security | analysis、agent safety、multi-agent evaluation、multi-agent system | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64792) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文围绕 Architecture Matters for Multi-Agent Security 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于智能体部署安全与故障恢复。 |
| 2026 | AdvEvo-MARL: Shaping Internalized Safety through Adversarial Co-Evolution in Multi-Agent Reinforcement Learning | analysis、agent safety、multi-agent evaluation、multi-agent system | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66275) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文围绕 AdvEvo-MARL 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于智能体部署安全与故障恢复。 |
| 2026 | A Diagnostic Study of Multi-Agent LLMs for Real-World Debates | analysis、agent safety、multi-agent evaluation、multi-agent system | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66089) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文围绕 Diagnostic Study of Multi-Agent LLMs 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于智能体部署安全与故障恢复。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | SNEAK: Evaluating Strategic Communication and Information Leakage in Large Language Models | benchmark、strategic communication、information leakage、multi-agent system | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2603.29846) | 暂未公开 | 针对 multi-agent communication 既要让盟友理解又不能让对手推断秘密的权衡，SNEAK 用 ally 与 chameleon 两种信息状态分别衡量 utility 和 leakage，结果显示人类得分最高可达所有被测模型的四倍。 |
| 2026 | TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | benchmark、agent safety、LLM agent、multi-agent system | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1442/) | [Code](https://github.com/microsoft/TAMAS) | 针对单 agent 基准无法覆盖协作系统独有攻击面，TAMAS 提供五场景、300 个 adversarial instance、六类攻击和 211 个工具，评测十个模型与三种 Autogen/CrewAI 配置并揭示普遍脆弱性。 |

## 基础 Tool 与资源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems | tool、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15424) | 暂未公开 | 大语言模型的快速采用促进了临床多智能体系统（MAS）的发展，该系统能够集成多模态患者数据并支持日益复杂的临床决策；尽管包括世界卫生组织、美国国家医学院和 FUTURE-AI 联盟在内的许多组织都提出了医疗保健人工智能的道德框架和治理原则，但这些努力在很大程度上仍然是概念性的；结果表明，ETHOS 通过检测不完整、不一致或超出范围的证据并在无法支持安全建议时适当增加弃权率来提高决策可靠性。 |
| 2026 | Towards Trustworthy Smart Contract Synthesis: A Multi-Agent Framework with Lean-Based Verification | tool、agent safety、LLM agent、multi-agent system | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1836/) | [Code](https://github.com/gl-bowei/LeVer) | 针对 LLM 生成智能合约虽功能可用却缺少安全保证，LeVer 让多智能体循环生成、形式化、验证、攻击和修复，并以 Lean 证明与经验攻击共同增强合约可信度。 |
| 2026 | Interaction-Breaking Adversarial Learning Framework for Robust Multi-Agent Reinforcement Learning | tool、adversarial defense、multi-agent evaluation、multi-agent system | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61001) | [Project](https://sunwoolee0504.github.io/IBAL) | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Interaction-Breaking Adversarial Learning Framework for 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | A Multi-Agent Framework for High-Interaction Terminal Simulation | tool、agent safety、LLM agent、multi-agent system | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1515/) | [Code](https://github.com/kaiwei666a/MANTIS_Terminal_Simulation) | 针对 LLM 终端模拟易误解命令、状态漂移并受提示注入的问题，MANTIS 以多智能体路由、外部工具过滤和可剪枝文件系统保持交互一致，在 28,045 个真实输入输出对等数据上将多轮模拟准确率提升至 95% 以上。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | BRA-Audit: Budgeted Runtime Auditing for LLM Multi-Agent Systems via Cumulative-Exposure Audit-Point Placement | detection、multi-agent system、risk propagation、collusive behavior | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14668) | 暂未公开 | 基于LLM的多智能体系统（LLM-MAS）通过专门的协作解决复杂的任务，但代理间的依赖关系可能会将幻觉或恶意输出传播到系统级故障中；如何在最大限度地降低代币成本的同时保持保护性能？为了解决这个问题，我们提出了 BRA-Audit，这是一种预算感知的运行时审计框架，它将 MAS 执行建模为动态依赖图，并将审计调度制定为固定审计调用预算下的审计点放置，以最大限度地减少累积的未经检查的暴露。 |
| 2026&#8209;03 | Is Monitoring Enough? Strategic Agent Selection For Stealthy Attack in Multi-Agent Discussions | detection、stealthy attack、multi-agent system、risk propagation | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4950) · [arXiv](https://arxiv.org/abs/2603.21194) | 暂未公开 | 针对持续监控通信似乎能阻断多智能体攻击的假设，作者设计面向监控场景的策略性代理选择攻击，实验证明连续异常检测下仍能实施有效隐蔽操纵。 |
| 2026 | When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems | detection、multi-agent evaluation、multi-agent system、risk propagation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65619) | 暂未公开 | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文围绕 When Agents Go Rogue 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于智能体攻击面治理。 |
| 2026 | Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection | detection、agent safety、LLM agent、multi-agent system | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1407/) | 暂未公开 | 针对多智能体恶意节点检测忽略词级线索且难解释，XG-Guard 联合句级与 token 级编码、主题异常检测和双层分数融合，在多种拓扑与攻击下兼顾稳健检测和细粒度解释。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Playing Along: Learning a Double-Agent Defender for Belief Steering via Theory of Mind | defense、theory of mind、belief steering、multi-agent system | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.11666) | 暂未公开 | 针对对手通过对话抽取敏感信息且 frontier model 难以欺骗强攻击者的问题，ToM-SB 训练 double-agent defender 让对手误以为已成功提取信息，联合 ToM 与 fooling reward 的 RL policy 在困难场景超过 GPT-5.4 和 Gemini3-Pro。 |
| 2026 | Securing Multi-Agent Systems Against Corruptions via Node Contribution Backpropagation | defense、multi-agent evaluation、multi-agent system、risk propagation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63780) | [Code](https://github.com/ChengcanWu/BPD) | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 Securing Multi-Agent Systems Against Corruptions 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于智能体攻击面治理。 |
| 2026 | Secure Multi-agent Reinforcement Learning for Service Systems with Affinity and Byzantine Nodes: Stability Analysis and Protection Design | defense、multi-agent evaluation、multi-agent system、risk propagation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62838) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Secure Multi-agent Reinforcement Learning for 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Learning Robust Multi-Agent Policies via Selective Adversarial Fault Induction | defense、multi-agent evaluation、multi-agent system、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61177) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Learning Robust Multi-Agent Policies via 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |

## Survey 与 Taxonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | SoK: Colluding Adversaries in Machine Learning Pipelines | survey、ML pipeline、colluding adversary、multi-agent system | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/duddu) · [arXiv](https://arxiv.org/abs/2606.10091) | 暂未公开 | 针对 ML pipeline 安全研究通常孤立建模单个攻击者的问题，该 SoK 建立 colluding adversary 框架并实证五类尚未充分研究的组合攻击，揭示分阶段防御之间的系统性缺口。 |

> Recursive propagation 以资源耗尽为主要目标的 CORBA 主记录见 [Agent 与多 Agent DoS](../dos/agent-system-dos.md)；节点级 failure attribution 见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)。
