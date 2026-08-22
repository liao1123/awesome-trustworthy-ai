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
| 2026&#8209;05 | When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems | analysis、embedding evasion、confidence signal、early intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.01133) | 暂未公开 | 针对按 message embedding 聚类并剪除恶意节点的防御依赖良恶分离；论文用 slow drift、benign wrapper 与 chaos seeding 让恶意信息贴近良性分布，并改用 token confidence 降权；结果 confidence signal 更稳健但会随通信轮次衰减，说明应尽早介入。 |
| 2026&#8209;03 | TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems | defense、MAS risk taxonomy、runtime monitoring、structured trace | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.15408) | [Code](https://github.com/AI45Lab/TrinityGuard) | 针对 MAS 缺少覆盖单 Agent、通信与系统涌现风险的统一防护框架；论文建立 20 类三层 taxonomy，并组合系统抽象、攻击评测与实时 monitor agents；结果支持不同拓扑和平台的开发前审计与运行期告警。 |
| 2026&#8209;03 | GroupGuard: A Framework for Modeling and Defending Collusive Attacks in Multi-Agent Systems | defense、group collusion、graph monitoring、structural pruning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.13940) | 暂未公开 | 针对 sociological strategy 驱动的多个 Agent collusion；论文组合持续 graph monitoring、active honeypot 与 structural pruning 定位并隔离 coalition；结果 collusion 比单独攻击最高多 15% ASR，GroupGuard detection 最高 88% 并恢复协作。 |
| 2026&#8209;03 | Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection | detection、cross-agent flow、execution-aware detection、compound attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.04469) | [Code](https://anonymous.4open.science/r/MAScope-71DC) | 针对输入 guard 无法识别分散在多条 inter-agent message 和执行步骤中的复合攻击；论文重建连续的 Cross-Agent Semantic Flow，再检查 data-flow violation、control-flow deviation 与 intent inconsistency；结果对十余类攻击的 node-level 和 path-level F1 分别达到 85.3% 与 66.7%。 |
| 2025&#8209;08 | Cowpox: Towards the Immunity of VLM-based Multi-Agent Systems | defense、VLM agent infection、distributed immunity、robustness guarantee | ICML 2025 | [PMLR](https://proceedings.mlr.press/v267/wu25aq.html) | 暂未公开 | 针对单个 VLM Agent 被攻破后会沿协作关系感染整个系统；论文生成并分发可在暴露前免疫、暴露后辅助恢复的 cure sample，并限制预期感染数；结果在实验中提高恢复率，同时给出分布式机制的理论鲁棒性保证。 |
| 2025&#8209;08 | BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks | defense、unknown attack、unsupervised detection、message propagation | ACL 2026 | [arXiv](https://arxiv.org/abs/2508.08127) | [Code](https://github.com/MR9812/BlindGuard) | 针对监督式防御依赖已标注攻击、难覆盖未知恶意节点的问题，论文以多层 Agent encoder 和 corruption-guided contrastive detector 只从正常通信学习；结果跨 prompt injection、memory poisoning 与 tool attack 保持较强检测和泛化。 |
| 2025&#8209;05 | Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems | defense、misinformation flow、goal-aware reasoning、ARGUS | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.00509) | [Code](https://github.com/zhrli324/ARGUS) | 针对恶意节点注入的信息会沿协作链传播且通用 filter 不理解任务目标；论文发布 MisinfoTask，并让 ARGUS 先识别与目标冲突的信息再在信息流中修正；结果平均降低约 28% misinformation toxicity，并改善攻击下任务成功率。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | ACIArena: Toward Unified Evaluation for Agent Cascading Injection | benchmark、cascading injection、MAS topology、attack-defense transfer | ACL 2026 | [arXiv](https://arxiv.org/abs/2604.07775) | [Code](https://github.com/Greysahy/aciarena) | 针对 Agent Cascading Injection 只在少量策略和简化 MAS 中测试；论文统一外部输入、profile、message 三类入口与 hijacking、disruption、exfiltration 三类目标，覆盖六种实现和 1,356 个案例；结果显示 role design 与 interaction pattern 和 topology 同样关键，窄域防御还可能引入新漏洞。 |
| 2026 | A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems | benchmark、A2A protocol、protocol attack、safety-utility | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=LfdFnakqGJ) | [Code](https://github.com/SaFo-Lab/A2ASecBench) | 针对 A2A capability discovery、任务编排和 artifact exchange 缺少协议级安全评测的问题，论文形式化供应链与 protocol-logic 威胁并实现六类攻击；结果表明官方 demo 的默认 safeguard 会被系统性绕过。 |

> Recursive propagation 以资源耗尽为主要目标的 CORBA 主记录见 [Agent 与多 Agent DoS](../dos/agent-system-dos.md)；节点级 failure attribution 见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)。
