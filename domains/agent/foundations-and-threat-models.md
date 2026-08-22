# Agent Security 基础框架、Survey 与 Threat Model

[返回 Agent Security 目录](README.md)

## 研究方向

本页整理能够解释整个 Agent security landscape 的基础框架。核心不是再列一组攻击名称，而是明确 security property、资产与主体、instruction/data provenance、delegated authority、persistent state、跨层传播和时间尺度，从而判断一个 action 在具体任务上下文中为何违规，以及防御和 benchmark 实际覆盖了哪一段生命周期。

## 研究脉络

- **组件枚举：** 早期 survey 从 brain、memory、tool 和 environment 等组件归纳 prompt injection、privacy、backdoor 与 unsafe action。
- **攻击面分层：** 后续 taxonomy 按 foundation、cognitive、memory、tool execution、MAS、ecosystem 和 governance 定位漏洞来源，并增加 session persistence 等时间维度。
- **上下文安全属性：** formal framework 将 task alignment、action alignment、source authorization 和 data isolation 作为可检查属性，避免脱离授权上下文判断动作。
- **系统生命周期：** 新近综述围绕 information flow、delegated authority 与 persistent state 串联 ingestion、planning、execution、persistence 和 monitoring。
- **Agent-human interaction：** 产业系统主要依赖 policy specification、runtime approval 与 scope configuration，学术研究则更偏向 intent anchoring 和 trust labeling；两者之间仍存在明显部署鸿沟。
- **当前边界：** 现有防御仍缺少跨层组合保证，benchmark 对长期状态、真实权限和部署配置的覆盖也不充分。

## Survey 与 Taxonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling | survey、MCP、agent security、threat model | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17275) | 暂未公开 | AI 智能体正越来越多地执行动作，而不只是读取信息：在模型上下文协议（MCP）生态系统中，会修改外部状态的已部署工具，其使用占比已经从 27% 上升到 65%；本文综述认为，执行层的四项属性——不可逆性、签名权限、持续自主性和序列级组合——会从性质上改变威胁模型，把通用智能体安全中可恢复的失效转化为持续且不可逆的损失；我们综合分析了包括新兴区块链机制在内的防御，并发现这些防御虽在改善但仍不充分：实测保护措施阻止的攻击不到 30%，模型层安全机制拒绝的攻击不到 3%。 |
| 2026&#8209;06 | Toward Safe LLM Agents: A Survey of Specification, Verification, and Enforcement | survey、agent security、threat model、attack taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14590) | 暂未公开 | LLM 智能体越来越多地执行不可逆的现实操作，包括数据库更新、API 调用、文件操作和工具的自主使用；研究在规范、验证和执行方面仍然分散，限制了对现有方法的优点和局限性的理解；第三，验证者税表明，阻止 94% 的不安全操作仍然会导致安全任务完成率低于 5%，因为代理会利用替代的不安全路径。 |
| 2026&#8209;06 | Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation | survey、agent lifecycle、delegated authority、persistent state | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.10749) | 暂未公开 | 针对 Agent security 文献按攻击或应用割裂的问题；论文以 information flow、delegated authority 和 persistent state 组织 247 篇工作；结论是 prompt injection 与 tool hijacking 仍占主导，而长期状态和多 Agent 传播缺少组合式防御与现实评测。 |
| 2026&#8209;04 | Security Attack and Defense Strategies for Autonomous Agent Frameworks: A Layered Review with OpenClaw as a Case Study | survey、autonomous framework、cross-layer propagation、OpenClaw | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.27464) | 暂未公开 | 针对持续运行的 Agent framework 风险难由 prompt-level taxonomy 解释；论文以 OpenClaw 为案例拆分 context/instruction、tool/action、state/persistence 和 ecosystem/automation 四层；结论是攻击会从输入操纵跨层传播为 unsafe action、持久污染和生态级影响。 |
| 2026&#8209;04 | A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework | survey、layered attack surface、threat temporality、defense gap | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.23338) | 暂未公开 | 针对按 attack type 分类难以定位漏洞所在组件的问题；论文用七层 Agent stack 与四类时间尺度编码 2021 至 2026 年文献；结果显示上层生态、跨 session 和 stack-propagating threat 的防御与 benchmark 覆盖最薄弱。 |
| 2026&#8209;03 | Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats | analysis、autonomous agent、OpenClaw、security mitigation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.11619) | 暂未公开 | 针对 OpenClaw 类长期运行 Agent 同时拥有持久状态、外部通信和系统权限后的复合风险；论文系统分析部署攻击面并验证分层缓解措施；结论是安全边界必须覆盖配置、工具、记忆和运行时，而不能只依赖模型拒绝。 |
| 2026&#8209;03 | The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey | survey、agentic AI、attack-defense taxonomy、research landscape | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.11088) | 暂未公开 | 针对 Agentic AI 攻防工作快速增长但术语和评测分散的问题；论文系统归纳攻击入口、影响目标和防御阶段；结论是研究需从单点输入过滤转向覆盖 Agent interaction loop 的纵深防御。 |
| 2026&#8209;02 | The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis | survey、prompt injection、context-dependent task、AgentPI | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.10453) | 暂未公开 | 针对现有 prompt injection 防御与 benchmark 忽略 Agent 必须依赖运行时观察决策的 context-dependent task；论文系统整理攻击生成策略与 text、model、execution 三阶段防御，并提出 AgentPI；结果显示没有单一防御能同时实现高 trustworthiness、utility 与低 latency。 |
| 2026 | SoK: Attack and Defense Landscape of Agentic AI Systems | survey、agentic AI、agent security、threat model | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic) | 暂未公开 | 针对 agentic AI 的攻击面和缓解工作缺少统一边界，该 SoK 按智能体组件与生命周期整理攻击—防御框架，并以案例研究归纳当前评测缺口和开放问题。 |

## Security Property 与形式化框架

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | A Framework for Formalizing LLM Agent Security | analysis、contextual security、authorization oracle、data isolation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.19469) | 暂未公开 | 针对相同 action 在不同任务和来源上下文中可能合法也可能违规的问题；论文定义 task alignment、action alignment、source authorization、data isolation 及相应 oracle；结果可统一重述 prompt injection、task drift 和 memory poisoning，并指出防御应检查具体安全属性而非一律阻断。 |

## Agent-Human Interaction 与部署鸿沟

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Reframing LLM Agent Security as an Agent-Human Interaction Problem | analysis、human oversight、deployment gap、approval fatigue | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.24309) | 暂未公开 | 针对 Agent security 被当作纯算法问题而忽视实际授权者的问题；论文比较 59 篇论文、21 个生产系统和 26 个 security plugin 中的人机安全机制；结果显示产业广泛使用的 policy、approval 与 scope control 在学术界研究不足，而人工参与又面临 cognitive burden 与安全保证的根本权衡。 |
