# Agent Hallucination 与 Reliability

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 hallucination 在 Agent 的 planning、retrieval、reasoning、human interaction、tool use 和 environment grounding 中如何产生并沿轨迹传播。与单轮事实性不同，Agent 可能虚构不存在的 UI element、tool state、执行结果、引用或已完成动作，随后基于错误内部状态采取真实操作。评测应定位首次 divergence、区分 retrieval 与 utilization，并同时观察 grounding、action fidelity 和最终后果。

## 研究脉络

- **Workflow taxonomy：** Survey 将 hallucination 映射到 Agent 完整 workflow，并区分多类 trigger cause、detection 与 mitigation。
- **交互式 benchmark：** MIRAGE-Bench 用可复现 snapshot 隔离 decision point，检验 action 是否忠于 instruction、history 和 observation。
- **Step-level attribution：** AgentHallu 不只判断是否幻觉，还定位 responsible step 并给出 causal explanation。
- **领域化诊断：** Deep Research 与 GUI Agent 分别需要 claim/evidence verification、visual grounding 和 action-state consistency。
- **当前边界：** LLM-as-judge 会受长上下文和自身事实错误影响，reliability claim 需结合 executable state、rule validator、人工标注和 uncertainty calibration。

## Hallucination 诊断与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | HalluClear: Diagnosing, Evaluating and Mitigating Hallucinations in GUI Agents | defense、GUI hallucination、grounding taxonomy、closed-loop reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.17284) | 暂未公开 | 针对 GUI Agent 的 ungrounded belief 会级联为错误动作且缺少专门评测；论文建立 GUI taxonomy、校准的三阶段 VLM judge 和 closed-loop post-training；结果以较小训练集改善 grounding 与 action fidelity，提供诊断到缓解的一体化路径。 |

## Benchmark 与 Attribution

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark | benchmark、intrinsic risk、risk-step localization、benign trajectory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.13954) | 暂未公开 | 针对 Agent 在无攻击良性环境中也会让潜在错误沿长轨迹演化为高后果；论文构建 629 条长轨迹并评测 detection、localization 与 failure-type identification；结果强模型能判断整体风险却在 step localization 上低于 35 Strict-F1，通用 guard 迁移较差。 |
| 2026&#8209;01 | AgentHallu: Benchmarking Automated Hallucination Attribution of LLM-based Agents | benchmark、hallucination attribution、responsible step、tool-use error | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.06818) | [Code](https://github.com/liuxuannan/AgentHallu) | 针对多步 Agent hallucination 需要找到首次致错步骤而非只判 final output；论文为七种 framework、五个 domain 的 693 条轨迹标注类别、责任步和解释；结果最佳模型 step localization 仅 41.1%，tool-use hallucination 只有 11.6%。 |
| 2025&#8209;07 | MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them | benchmark、interactive hallucination、snapshot evaluation、action faithfulness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.21017) | [Code](https://github.com/sunblaze-ucb/mirage-bench) | 针对 Agent hallucination 评测碎片化且环境不可复现；论文用 snapshot 隔离 decision point，并按 instruction、execution history 与 environment observation 三类不忠实 action 组织测试；结果为交互环境中的可控 elicitation 和细粒度风险判断提供统一基线。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Tool Execution Hallucination in LLM-based Agents: A Unified Taxonomy with Detection, Mitigation, and Future Directions | survey、tool execution hallucination、failure taxonomy、error propagation | TechRxiv Preprint | [TechRxiv](https://doi.org/10.36227/techrxiv.177219979.94060974/v1) | 暂未公开 | 针对传统 hallucination survey 侧重事实错误、难覆盖 Agent 在选工具、填参数和多轮执行中的决策失败；论文沿 execution flow 统一单轮与多轮 taxonomy，并整理检测、缓解和 benchmark；结论指出跨 iteration 错误传播与 task-solvability awareness 仍是主要空白。 |
| 2025&#8209;09 | LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions | survey、agent workflow、trigger cause、mitigation taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.18970) | 暂未公开 | 针对单轮 LLM hallucination taxonomy 无法覆盖 observation、planning、memory 和 action 之间的传播；论文沿 Agent workflow 归纳类型、十八类诱因及检测缓解方法；结论是需要对中间状态和实际执行共同做 grounded verification。 |

> GUI/Web 环境中的安全攻击主记录见 [Web 与 Computer-Use Agent Security](web-and-computer-use-agent-security.md)，通用 step-level failure 方法见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)，Deep Research 特有的 hallucination 与 evidence-chain 评测见 [Scientific Research Agent Reliability](../ai-for-science-safety/scientific-research-agent-reliability.md)。
