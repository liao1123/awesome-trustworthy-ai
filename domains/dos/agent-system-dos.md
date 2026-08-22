# Agent 与多 Agent DoS

## 研究方向

Agent 与多 Agent DoS 研究自主系统中特有的资源生命周期和控制流风险。攻击者可以污染第三方 skill、工具描述、外部文档、GUI 触发器或 Agent 间消息，使系统反复规划、调用工具、错误判断任务尚未结束，或把递归指令沿协作拓扑传播；其危害需要用步骤数、工具调用、总 token、任务完成率和共享基础设施延迟共同衡量。

## 研究脉络

- **攻击起点：** 早期 Agent DoS 主要通过单次长输出放大推理成本。
- **攻击面扩展：** 研究随后覆盖 tool-call chain、termination condition、skill routing 和 guardrail loop，利用 Agent 的自主执行过程持续消耗资源。
- **系统化评测：** 在多 Agent 与共享基础设施中，局部资源放大会继续传播，因此研究开始引入生命周期 fuzzing 和漏洞检测。

## 循环、工具链与 Guardrail 攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents | attack、tool-using agent DoS、third-party skill、path hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.12273) | 暂未公开 | 针对 Agent 以描述选 skill、再按正文规划的两阶段信任链，论文让恶意协调 skill 招募无关良性 skill 绕路后再回归正确任务；结果在保持总体完成率的同时最高增加 66.91% token 和 92.45% 执行时间。 |
| 2026&#8209;06 | From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails | attack、agent-guardrail DoS、agent defense、reasoning loop | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.14517) | 暂未公开 | 针对 Agent guardrail 自身也会执行推理和遵循结构，论文用自然语言搜索与结构突变把防护模型困入长循环；结果跨八类模型放大 token 13 至 63 倍，并在真实 Agent 部署中把延迟最高放大 148 倍。 |
| 2026&#8209;05 | Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection | attack、multi-agent DoS、semantic closure、recursive invocation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.11442) | 暂未公开 | 针对 Agent 可成为用户与服务之间的破坏性枢纽，论文用单条 Mobius Injection 触发组件语义闭包并把 Agent 变成递归调用节点；结果单节点调用最高放大 51 倍，多节点 p95 延迟最高放大 229.1 倍。 |
| 2026&#8209;05 | LoopTrap: Termination Poisoning Attacks on LLM Agents | attack、LLM-agent DoS、termination poisoning、behavioral profiling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.05846) | 暂未公开 | 针对 Agent 自主判断任务完成会形成终止攻击面，论文先探测四类行为倾向，再按目标画像合成恶意上下文让其持续认为任务未完成；结果在八种 Agent 上平均放大步骤 3.57 倍、峰值 25 倍。 |
| 2026&#8209;01 | Sponge Tool Attack: Stealthy Denial-of-Efficiency against Tool-Augmented Agentic Reasoning | attack、tool-using agent DoS、tool use、prompt rewriting | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.17566) | 暂未公开 | 针对工具增强推理的高效路径可被输入操纵，论文在仅查询权限下用多 Agent 框架重写良性提示，把简洁工具轨迹变成冗长绕路；结果跨六种模型、十二种工具和四个 Agent 框架均能增加计算开销并保持原任务语义。 |
| 2026&#8209;01 | Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents | attack、tool-using agent DoS、MCP tool、call chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10955) | 尚未发布 | 针对单轮长输出攻击放大有限且容易暴露，论文通过修改 MCP 工具文本并用 MCTS 优化多轮调用链；结果最高放大 658 倍单次成本且常规提示过滤和轨迹监控很少检出。 |

## GUI 与多 Agent 可用性攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | SlowBA: An efficiency backdoor attack towards VLM-based GUI agents | attack、GUI-agent DoS、efficiency backdoor、popup trigger | ECCV 2026 | [arXiv](https://arxiv.org/abs/2603.08316) | [Code](https://github.com/tu-tuing/SlowBA) | 针对 GUI Agent 安全研究只关注动作正确性，论文用两阶段奖励级后门和自然弹窗触发器诱发超长推理；结果即使投毒比例很低也显著增加响应长度和延迟，同时基本保持任务准确率。 |
| 2025&#8209;02 | CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on Large Language Models | attack、multi-agent DoS、recursive propagation、collaboration blocking | ACL 2026 Findings | [arXiv](https://arxiv.org/abs/2502.14529) · [ACL Anthology](https://aclanthology.org/2026.findings-acl.342/) | [Code](https://github.com/zhrli324/Corba) | 针对开放通信使多 Agent 协作结构可被利用，论文用表面无害且可传染的递归指令让消息在不同拓扑中反复传播；结果能耗尽计算并造成系统瘫痪，提出了区别于单节点 DoS 的协作拒绝攻击。 |

## 漏洞检测与系统评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents | detection、LLM-agent DoS、resource lifecycle、grey-box fuzzing | USENIX Security 2026 | [Conference](https://www.usenix.org/conference/usenixsecurity26/presentation/luo) | 暂未公开 | 针对 Agent 缺少完整资源生命周期治理，论文分析三类资源管理模式并提出定向灰盒模糊测试 AgentDoS；结果在 20 个开源 Agent 中发现影响 16 个系统的 36 个零日漏洞。 |

> Agent 的完整攻击面与生命周期分类见 [Agent Security](../agent/README.md)；MAS 传播风险见 [Multi-Agent System Security](../agent/multi-agent-system-security.md)。
