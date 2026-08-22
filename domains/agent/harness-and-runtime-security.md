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
| 2026&#8209;08 | HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety | benchmark、harness lifecycle、configuration attack、incident recovery | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17597) | [Project](https://baiyajing.github.io/harness-risk/) | 针对 benchmark 只覆盖单一攻击或少数 operational setting；论文沿配置、扩展、运行、持久化、动作控制和恢复六阶段构建 128 个 sandbox case；结果不同 model-harness 配置 ASR 为 12.6% 至 80.9%，且识别风险不等于采取安全动作。 |
| 2026&#8209;08 | HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses | benchmark、persistent carrier、risk lifecycle、trace evidence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06984) | 暂未公开 | 针对 memory、skill、tool 和 shared artifact 会把攻击影响带过 session 与系统边界；论文用 Persistent-Risk Lifecycle 和 multi-stage trace score 记录 328 条执行链；结果 containment 高度依赖 carrier 与 model-harness pairing，单一 end-to-end ASR 无法显示攻击在哪一阶段被阻断。 |
| 2026&#8209;05 | Auditing Agent Harness Safety | benchmark、trajectory audit、permission boundary、information flow | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14271) | 暂未公开 | 针对正确 final answer 也可能来自越权访问或错误 Agent 间泄漏；论文以 HarnessAudit 检查完整轨迹的 boundary compliance、execution fidelity 和 stability，并发布单/多 Agent benchmark；结果违规随轨迹变长并集中于资源访问和 inter-agent transfer。 |

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
