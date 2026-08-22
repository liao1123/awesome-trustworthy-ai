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
| 2026&#8209;08 | GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG | defense、VLM safety、agent reliability、hallucination | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15056) | 暂未公开 | 多模态检索增强生成（RAG）系统通常依赖于长的非结构化上下文或积极扩展的证据图，这可能会引入噪声证据，削弱多跳推理并增加无支持的生成；我们提出了 GraphLoom，一种经过可靠性校准的多模态知识图谱 RAG 框架，用于紧凑且忠实的证据路由；使用基于 MiniCheck 的验证、人工评估和延迟分析进行的其他分析表明，经过可靠性校准的图形证据路由为长上下文多模态证据注入提供了有效的替代方案。 |
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

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique | detection、uncertainty calibration、agent reliability、hallucination | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10430) | 暂未公开 | Latent Critic 用并行运行的低秩 adapter 把冻结 Agent 的潜在 uncertainty 重组为局部自然语言 critique；它达到 0.966 AUROC 和超过 80% 的 hallucination 定位准确率，并在 ReAct 闭环中以很低延迟阻断未 grounded 动作并促进自我修正。 |

## 基础 Tool 与资源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination | tool、reasoning safety、agent reliability、hallucination | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.376/) | [Code](https://github.com/albert-y1n/Reasoning_Trap) | 针对强化推理是否诱发工具幻觉，SimpleToolHalluBench 的控制实验表明 RL、SFT 或仅提示逐步思考都会随能力提升增加无工具或干扰工具下的幻觉，现有 prompt 与 DPO 缓解又会损害效用。 |
| 2026 | From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models | tool、reasoning safety、agent reliability、hallucination | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1951/) | 暂未公开 | 针对工具调用虽提高答案准确率却可能替代真实推理，PyMath 的 1,679 道题显示代码解释器最多带来 19.3 个百分点准确率增益、但非工具模型的推理过程胜率可高 41.5%，偏好优化可同时改善答案与推理深度。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation | analysis、agent reliability、hallucination、task completion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16515) | 暂未公开 | 检索增强生成（RAG）通过将生成基于外部证据来改进大语言模型，但它也引入了源信任问题：检索到的上下文可能有用、不相关，甚至具有误导性；因此，我们提出了意图引导解码（IGD），这是一个根据用户意图在检索到的上下文和参数内存之间进行仲裁的框架；我们在五个LLM的三个忠实 QA 基准和三个事实冲突基准上评估了 IGD，IGD 显著提高了事实恢复，在事实冲突基准上比 Direct RAG 提高了高达 65.4 个百分点，同时保留或改进了严格的上下文跟踪行为，这一发现强调了在 RAG 中平衡事实和忠实性的重要性。 |
| 2026&#8209;02 | Towards a Science of AI Agent Reliability | analysis、agent safety、agent reliability、hallucination | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66364) · [arXiv](https://arxiv.org/abs/2602.16666) | [Code](https://github.com/princeton-pli/hal-harness) | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文围绕 Towards a Science of AI 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于智能体部署安全与故障恢复。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG | benchmark、adversarial robustness、agent reliability、hallucination | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18489) | 暂未公开 | 知识图谱问答（KGQA）和基于知识图谱的检索增强生成（KG-RAG）旨在让答案以显式图证据为依据，但现实知识图谱通常稀疏、陈旧且不完整；为填补这一空白，我们提出 MissDiag，一个用于诊断 KGQA 和 KG-RAG 在知识不完整条件下鲁棒性的评估框架；跨多个系统家族的实验表明，不完整知识鲁棒性更适合被理解为具有类型的退化现象，而不是统一属性：靠近答案的证据丢失造成最大退化；移除来源上下文通常没有影响，有时反而有益；语义答案匹配会改变绝对分数，却保留主要的类型化退化模式。 |

> GUI/Web 环境中的安全攻击主记录见 [Web 与 Computer-Use Agent Security](web-and-computer-use-agent-security.md)，通用 step-level failure 方法见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)，Deep Research 特有的 hallucination 与 evidence-chain 评测见 [Scientific Research Agent Reliability](../ai-for-science-safety/scientific-research-agent-reliability.md)。
