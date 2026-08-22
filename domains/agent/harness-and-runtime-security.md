# Agent Harness 与 Runtime Security

[返回 Agent Security 目录](README.md)

## 研究方向

Agent harness 是连接 base model 与实际系统的编排层，负责 context assembly、instruction surfaces、tool dispatch、permission、persistent state、hooks、tracing、budget、error recovery 和 human approval。相同模型在不同 harness 中可能产生完全不同的 capability 与 risk；因此本页以 model-harness configuration 为评测单位，关注执行全程的 authorization、information flow、stability 与 incident recovery，而不只看 final answer。

## 研究脉络

- **Harness 作为隐藏变量：** 早期 Agent benchmark 固定或忽略 harness，使任务成功和安全差异被错误归因给 base model。
- **配置级诊断：** 新 benchmark 在共享任务、budget 和 validator 下比较 model-harness pairing，并记录 tool trace、artifact、资源和 recovery。
- **全轨迹安全：** HarnessAudit、HarnessSafe 和 HarnessRisk 从 final output 扩展到边界违规、persistent carrier 和完整 operational lifecycle。
- **Instruction surface：** system prompt、project file、user turn、tool 与 skill description 之间并不存在简单由深度决定的稳定优先级，需要单独测试冲突和 against-prior rule。
- **Runtime contract：** harness 不只要在动作前做 permission gate，还应要求 test、log、diff 与 citation 等可核验 evidence，避免 Agent 仅声称任务已完成。
- **Harness 演化：** 研究开始从失败轨迹归因到具体 artifact，再局部更新 rule bank、safety memory 与 tool policy，但更新本身也需防止回归和投毒。

## 安全审计与生命周期 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows | benchmark、MCP、agent harness、runtime isolation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19741) | [Code](https://github.com/microsoft/thinkingbox) | 近期的智能体基准越来越多地将评估建立在可执行环境中，涵盖代码修复、网页导航、应用程序 API 和函数调用；本文提出 Thinkingbox，一个用于工具—智能体—用户交互的沙箱，提供隔离的 MCP 兼容工具会话、完整执行轨迹，以及基于后端最终状态的结果评估；此外，许多失败试验都正常终止并执行了有效的状态变更操作，这表明回复级或工具调用级信号并不能明确代表端到端任务完成情况。 |
| 2026&#8209;08 | HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety | benchmark、harness lifecycle、configuration attack、incident recovery | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17597) | [Project](https://baiyajing.github.io/harness-risk/) | 针对 benchmark 只覆盖单一攻击或少数 operational setting；论文沿配置、扩展、运行、持久化、动作控制和恢复六阶段构建 128 个 sandbox case；结果不同 model-harness 配置 ASR 为 12.6% 至 80.9%，且识别风险不等于采取安全动作。 |
| 2026&#8209;08 | Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection | benchmark、prompt injection、agent harness、runtime isolation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16393) | [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/deepseek-harness-security-assessment) | 我们评估 DeepSeek Harness (DSH) 中的间接提示注入，使用 AI-Infra-Guard (A.I.G) 构建测试、提供受控污点、执行 DSH、收集痕迹并判断结果；该研究涵盖了 16 个间接内容通道、文本和文件载体模式、35 个有效负载目标、1 个未修改的基线和 12 种攻击方法的 14,560 次受控执行；我们将这些结果与 DSH 对工具结果、附加上下文和工具调用策略挂钩的处理联系起来，然后确定应位于不可信内容和敏感操作之间的控件。 |
| 2026&#8209;08 | HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses | benchmark、persistent carrier、risk lifecycle、trace evidence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06984) | 暂未公开 | 针对 memory、skill、tool 和 shared artifact 会把攻击影响带过 session 与系统边界；论文用 Persistent-Risk Lifecycle 和 multi-stage trace score 记录 328 条执行链；结果 containment 高度依赖 carrier 与 model-harness pairing，单一 end-to-end ASR 无法显示攻击在哪一阶段被阻断。 |
| 2026&#8209;05 | Auditing Agent Harness Safety | benchmark、trajectory audit、permission boundary、information flow | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14271) | 暂未公开 | 针对正确 final answer 也可能来自越权访问或错误 Agent 间泄漏；论文以 HarnessAudit 检查完整轨迹的 boundary compliance、execution fidelity 和 stability，并发布单/多 Agent benchmark；结果违规随轨迹变长并集中于资源访问和 inter-agent transfer。 |
| 2026&#8209;03 | Quantifying Frontier LLM Capabilities for Container Sandbox Escape | benchmark、agent harness、runtime isolation、lifecycle security | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66709) · [arXiv](https://arxiv.org/abs/2603.02277) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文构建 Quantifying Frontier LLM Capabilities for 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于危险能力评测与高风险部署治理。 |

## 配置、Instruction Surface 与能力归因

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents | benchmark、instruction surface、against-prior rule、coding harness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11727) | 暂未公开 | 针对 Agent 遵守规则可能只是原本就会这样做；论文把规则放在五类可配置 surface，并以 withholding probe 标注 against-prior rule；结果所有模型在该子集下降，冲突实验也表明 precedence 不简单服从 prompt depth。 |
| 2026&#8209;08 | $A^2E$: An End-to-End Agent Auditing Engine | tool、agent auditing、standardized trace、model-harness comparison | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.07346) | [Code](https://github.com/datamllab/A2E) | 针对不同任务接入 harness 和收集可比较 execution trace 成本高；论文以 Agent Task Protocol、自动 instrument monitor 和多维 evaluator 构建端到端引擎；结果显示没有一个 model-harness pairing 在所有任务稳定占优，必须同时报告 execution efficiency、tool use、planning 与 recovery。 |
| 2026&#8209;05 | Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows | benchmark、harness configuration、execution alignment、artifact validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.27922) | [Code](https://github.com/Qihoo360/harness-bench) | 针对完整 Agent 对比掩盖 execution layer 的贡献；论文在共享 sandbox task、budget 与 protocol 下记录 5,194 条轨迹；结果 model-harness pairing 在完成度、过程、效率和 failure behavior 上显著不同，并暴露 reasoning 与 tool feedback/workspace state 脱节的 execution-alignment failure。 |

## Runtime Contract 与 Evidence

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Agent Safety Should Be a Runtime Contract | analysis、runtime contract、evidence chain、trajectory schema | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11274) | 暂未公开 | 针对训练期 alignment 无法约束 Agent 执行代码、修改文件和调用外部系统后的真实结果；论文提出由 harness 强制执行 preventive 与 evidential 两面 contract，并形式化 Agent Trajectory Schema 和 Evidence Chain；结论是安全评测单位应从 model 或 final answer 转为带可核验证据的完整轨迹。 |

## Harness 设计与演化

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | SHE: Trajectory-driven Safety Harness Evolution for LLM Agents | defense、harness evolution、failure attribution、safety-utility validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.09885) | [Code](https://github.com/RainbowQTT/SHE) | 针对固定 harness 难跟随新风险且组件责任耦合；论文将 system prompt、rule bank、safety memory 与 tool policy 分离，按轨迹失败归因后局部演化并做 safety-utility selection；结果相对静态 SafeHarness 将 ASR 降低 3.1 倍并迁移到 unseen risk。 |
| 2026&#8209;08 | Evo-Bench: Can Language Models Improve Agent Harness? | benchmark、harness evolution、cross-suite generalization、iterative research | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.09096) | 暂未公开 | 针对 harness 自主优化评测会混入 base-model 能力、任务过拟合和短程迭代偏差；论文以 auxiliary-task evolution 和 sensitivity-aware split 隔离 harness-evolving capability；结果模型生成的 harness 可迁移并提升多类 policy，但在要求特定流程的 Office 任务明显受限。 |
| 2026&#8209;05 | Code as Agent Harness | survey、code harness、execution substrate、verifiable agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.18747) | [Resource](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) | 针对 code 不再只是 Agent 输出而成为 planning、memory、tool、environment model 和 verification 的运行基底；论文按 interface、mechanism 与 multi-agent scaling 组织相关方法；结论是 harness engineering 需超越 final success，处理不完整反馈、无回归更新、共享状态和高风险人工监督。 |
| 2026&#8209;03 | ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers | defense、runtime watcher、skill policy、execution intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.24414) | 论文声明公开，链接待核实 | 针对 OpenClaw 防护分散在单一生命周期阶段；论文组合 instruction-level skill、内部 enforcement plugin 与解耦的 system watcher；结果 watcher 可持续验证状态演化，并在高风险动作前停止执行或要求人工确认。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Beyond Direct Access: Resource Hijacking in LLM Agents | attack、agent harness、runtime isolation、lifecycle security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15108) | 暂未公开 | 大语言模型智能体越来越多地连接到高价值资源，例如计算基础设施、凭证、使用预算、身份、私有知识、通信渠道和组织工作流程；现有的Agent安全研究主要研究针对指令、数据和工具行为的攻击，而Agent可访问的高价值资源作为直接攻击目标受到的关注要少得多；这些结果表明，代理可访问的高价值资源形成了一个重要且以前被忽视的攻击面，并且当前的代理防御不足以保护它们免受资源劫持。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations | analysis、agent harness、runtime isolation、lifecycle security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16178) | 暂未公开 | 操作遥测主要是为人类阅读而设计的：系统在数十亿条日志行中重复序列化冗长的散文、静态密钥和冗余上下文；本文介绍了代理原生遥测技术，这是一种基于可验证的状态增量而不是人类散文的自主机器操作员的操作证据架构；我们证明了信息保存下界，并形式化了可证明事件不发生的与账本相关的验证负定理。 |
| 2026&#8209;08 | A Programming Paradigm for Spatiotemporal Composability | analysis、spatiotemporal composability、revertible effect、agent harness | 未注明（作者稿） | [Author PDF](https://github.com/cordiverse/paper/blob/main/paper.pdf) | [Code](https://github.com/cordiverse/cordis) | 针对 plugin system 与 self-evolving agent harness 动态装卸组件后副作用难回滚、依赖难同步的问题，论文形式化 revertible effect 与 reactive coeffect 并实现 Cordis；其演算把时空可组合性从单组件传递到交错执行的完整系统。 |
| 2026 | AIR: Improving Agent Safety through Incident Response | analysis、agent safety、agent harness、runtime isolation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62353) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文围绕 AIR 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于智能体部署安全与故障恢复。 |
