# Agent Security

[返回领域目录](../README.md)

本目录研究由 LLM 驱动、能够规划、使用工具、维护状态并对外部环境采取动作的 Agent 系统。与单轮模型安全相比，Agent Security 需要同时处理不可信 observation、委托权限、tool execution、persistent memory、跨 Agent 通信和长程 trajectory；风险既可能来自攻击者，也可能由自主性、错误目标、harness 设计或多个局部失败组合产生。

当前范围包括通用 LLM Agent、Web/Computer-Use Agent、Coding Agent、Multi-Agent System 和 self-evolving Agent。纯机器人控制、自动驾驶和不含 LLM Agent threat model 的一般 RL safety 暂不纳入。

## 研究地图

| 系统层或研究问题 | 子领域 | 主要内容 |
| --- | --- | --- |
| 全局模型与边界 | [基础框架、Survey 与 Threat Model](foundations-and-threat-models.md) | 安全属性、攻击面 taxonomy、生命周期、trust boundary 与评测假设。 |
| 自主目标与行为 | [行为安全与 Agentic Misalignment](behavioral-safety-and-misalignment.md) | harmful compliance、自主目标偏移、insider-risk 行为、监督规避与监控。 |
| 综合评测 | [通用 Benchmark 与评测方法](benchmarks-and-evaluation.md) | 跨攻击面的 Agent safety benchmark、动态 adversary、指标有效性和现实工具环境。 |
| Tool 与协议 | [Tool 与 MCP Security](tool-and-mcp-security.md) | tool selection、tool output、metadata、MCP server、权限边界和 tool-chain 攻击。 |
| 可复用能力供应链 | [Skill、Plugin 与供应链安全](skill-and-plugin-supply-chain-security.md) | skill discovery、activation、bundled code、恶意 skill、组合风险和 scanner。 |
| Web 与桌面环境 | [Web 与 Computer-Use Agent Security](web-and-computer-use-agent-security.md) | 网页 prompt injection、GUI observation、恶意网站、跨应用动作与 CUA red teaming。 |
| 软件工程环境 | [Coding Agent Security](coding-agent-security.md) | issue/repository prompt injection、代码执行、secret leakage、over-permission 与安全修复。 |
| Agent 间交互 | [Multi-Agent System Security](multi-agent-system-security.md) | 恶意节点、通信拓扑、控制流劫持、传播、collusion、隐私与协作防御。 |
| 持久状态与演化 | [Memory 与 Self-Evolving Agent Security](memory-and-self-evolving-agent-security.md) | memory governance、跨 session 风险、misevolution、经验晋升和安全演化。 |
| 系统编排层 | [Harness 与 Runtime Security](harness-and-runtime-security.md) | model-harness coupling、context assembly、hook、sandbox、credential 与运行时审计。 |
| 过程可观测性 | [Trajectory Safety Monitoring](trajectory-monitoring-and-failure-attribution.md) | 攻击轨迹、policy violation、高后果故障、运行时 guard 与可审计 provenance；不收录一般任务失败诊断。 |
| 独立控制层 | [Agent Guardrail 与 Policy Compliance](guardrails-and-policy-compliance.md) | action、trajectory、workflow policy、pre-execution guard 和 prompt-injection detection。 |

## 生命周期视角

1. **Ingestion：** Agent 接收 user instruction、网页、文件、tool metadata、消息与 memory retrieval，重点检查来源身份、内容完整性和 instruction/data boundary。
2. **Planning：** Agent 将目标分解为计划并选择 skill 或 tool，重点约束 task alignment、权限和跨步骤 policy。
3. **Execution：** Agent 调用工具、运行代码或操作 GUI，重点实施 least privilege、参数验证、sandbox、速率限制和动作前审核。
4. **Persistence：** 交互结果进入 memory、经验库或新 skill，重点保留 provenance、写入门控、隔离和可撤销性。
5. **Coordination：** 多个 Agent 交换任务和状态，重点验证身份、消息、拓扑传播和最小信息披露。
6. **Monitoring：** 完整 trajectory 被记录、评估和归因，重点区分模型、harness、环境和协作节点造成的失败。

## 跨领域索引

以下方向以 Agent 为重要应用场景，但已有更合适的主目录，本目录不重复维护同一份论文表：

- [Agent 与多 Agent DoS](../dos/agent-system-dos.md)：termination poisoning、tool-call amplification、recursive propagation 与共享基础设施可用性。
- [Agent Memory 投毒](../poison-and-backdoor/agent-memory-poison.md)：memory write、retrieval trigger、跨 session 持久污染与 selective repair。
- [Agent Skill 投毒与后门](../poison-and-backdoor/agent-skill-poison-and-backdoor.md)：trajectory-to-skill poisoning、持久 skill backdoor 与 lineage compromise。
- [Search Agent](../poison-and-backdoor/search-agent.md)：开放网页证据污染、harmful information-seeking、Agent 背书、research-trajectory hijacking 与 process alignment。
- [Generative Engine Optimization Security](../poison-and-backdoor/geo.md)：生成式搜索中的 GEO、black-hat ranking、citation／visibility manipulation、recommendation harm 与对应防御。
- [Prompt Injection](../misc/prompt-injection.md)：通用 direct/indirect prompt injection；Web、tool 和 skill 特有的 Agent 攻击仍进入本目录相应页面。
- [RAG Poisoning](../poison-and-backdoor/rag-poison.md)：固定或结构化知识库中的语料与拓扑污染；开放网页的动态 evidence poisoning 进入 Search Agent。
- [Capability Access Control](../misc/capability-access-control.md)：通用 capability 权限控制；Agent 中的 delegated authority 和 tool permission 进入 Tool/MCP 或 Harness 页面。
- [CoT Monitorability](../misc/cot-monitorability.md)：模型内部 reasoning 的可监控性；运行轨迹和多组件 failure attribution 进入 Agent trajectory 页面。
- [AI for Science Safety](../ai-for-science-safety/README.md)：Deep Research 的 factuality、provenance、multimodal evidence 与 scientific workflow 留在该目录；开放网页投毒和有害检索进入 Search Agent，生成式排名操纵进入投毒与后门目录的 GEO 页面。

## 分类规则

1. 论文按主要安全问题进入最匹配的叶子页；跨页面确有独立贡献时可以交叉收录，但每页内只保留一次。
2. 通用 benchmark 进入 Benchmark 页；只针对 Web、MAS、skill 等单一环境的 benchmark 进入对应子领域。
3. 单纯提高 Agent capability、成功率、记忆、检索、规划或效率的工作不收录；“可靠性”或“失败诊断”只有在攻击、越权、泄漏、不可逆损害或其他安全关键后果明确时才收录。
4. 导入的 PDF 只作为临时阅读材料；论文信息完成提取、核验并写入领域页后，删除原始 PDF，不把它作为仓库内容长期保存。
