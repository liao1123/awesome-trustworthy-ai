# Agent Tool 与 MCP Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 Agent 从发现工具、读取 metadata、选择与参数化工具，到接收 tool result 和组合多次调用的完整安全链。MCP 将外部 server 暴露的 tool、resource 与 prompt 动态接入 Agent，进一步引入 server identity、capability negotiation、credential、schema、rug pull 和跨 server data flow；因此不能只在 user prompt 上做过滤，还要检查来源、权限、参数、返回值和执行后果。

## 研究脉络

- **Tool-output injection：** 早期工作证明不可信 tool result 可混淆 instruction 与 data，使 Agent 偏离用户任务。
- **Cross-modal environment injection：** Multimodal Agent 持续感知真实环境后，攻击者还可通过并发音频等旁路输入把隐藏指令带入 planning 与 tool-use context。
- **Selection 与 metadata：** 攻击随后转向 tool document、name、description 和 parameter schema，在调用前劫持 retrieval 与 selection。
- **实现与协议风险：** malicious tool code 和 MCP server 可直接窃取 credential、篡改结果、串联工具或在批准后改变行为。
- **结构化防御：** 防御从 prompt filtering 发展到 tool-result parsing、typed interface、least privilege、information-flow check 和可验证执行规则。
- **当前边界：** 静态 schema 和 LLM auditor 难覆盖动态 server、跨工具链及 context-dependent authorization，部署评测还需包含真实 secret 和不可逆 action。

## Survey 与基础框架

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | survey、multi-tool orchestration、safety control、verifiability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.22862) | 暂未公开 | 针对研究重心已从单次工具调用转向带中间状态、反馈和约束的长程编排；论文从 planning、training、safety、efficiency、open-environment capability 和 evaluation 六个维度整理进展；结论是多工具 Agent 需要同时处理可靠性、成本、安全与可验证执行。 |

## Tool Selection、Metadata 与实现攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion | attack、memory fragmentation、access control、tool-use agent | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/rao) · [arXiv](https://arxiv.org/abs/2606.15609) | 暂未公开 | 针对 agent access control 逐轮检查单个请求的缺口，FragFuse 将禁用目标拆成无害片段写入记忆后再融合，达到 86.3% 绕过率与 41.1% 有害任务完成率。 |
| 2026&#8209;02 | MalTool: Malicious Tool Attacks on LLM Agents | attack、malicious tool code、CIA impact、automated synthesis | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.12194) | 暂未公开 | 针对既有研究关注工具名称和描述却忽略真正执行的 code；论文按 CIA triad 自动生成独立恶意工具及嵌入良性工具的 payload；结果构造出大规模恶意实现，并发现传统 malware detector 与 Agent-specific detector 均难可靠识别。 |
| 2026 | Training Language Model Agents to Find Vulnerabilities with CTF-Dojo | attack、tool-use agent、tool interface、action integrity | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61783) | 暂未公开 | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 CTF 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于智能体攻击面治理。 |
| 2026 | Stop Fixating on Prompts: Reasoning Hijacking and Constraint Tightening for Red-Teaming LLM Agents | attack、reasoning safety、agent safety、tool-use agent | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1197/) | 暂未公开 | 针对红队通常直接改用户 prompt 而影响任务且适配性差，JailAgent 不改输入，依次抽取 trigger、劫持 reasoning 并收紧约束，在跨模型和跨场景中操纵 agent 轨迹与记忆检索。 |
| 2026 | Query-Efficient Agentic Graph Extraction Attacks on GraphRAG Systems | attack、tool-use agent、tool interface、action integrity | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.727/) | [Code](https://github.com/shuashua0608/AGEA) | 针对 GraphRAG 的隐藏实体关系图可被有限查询窃取，AGEA 结合 novelty-guided 探索、外部图记忆和两阶段过滤，在严格预算下仍可恢复最多 90% 的实体与关系。 |
| 2026 | MemIncept: Steering LLM Agents via Cooperative Stealthy Memory Injections | attack、tool-use agent、tool interface、action integrity | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66667) | 暂未公开 | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 MemIncept 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于智能体攻击面治理。 |
| 2026 | Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS | attack、tool-use agent、tool interface、action integrity | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.330/) | 暂未公开 | 针对静态 tool attack 难跨领域且无法分配长程信用，Evo-Attacker 用动态记忆、deliberative retrieval 与 Attack-Flow GRPO 选择关键时刻的工具输出干预，持续优于基线并展示自演化攻击能力。 |
| 2025&#8209;10 | ToolTweak: An Attack on Tool Selection in LLM-based Agents | attack、tool selection bias、metadata optimization、marketplace fairness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.02554) | 暂未公开 | 针对功能相近的工具会在 Agent marketplace 中竞争可见性；论文迭代改写 tool name 与 description，在不改变能力的情况下操纵选择；结果目标工具选择率可从约 20% 升至 81%，并在模型间迁移，paraphrasing 与 perplexity filtering 只能部分缓解。 |
| 2025&#8209;08 | Attractive Metadata Attack: Inducing LLM Agents to Invoke Malicious Tools | attack、tool metadata、black-box optimization、privacy leakage | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2508.02110) | [Code](https://github.com/SEAIC-M/AMA) | 针对 Agent 会依据 name、description 和 schema 自主选择工具；论文以 black-box in-context optimization 生成语法和语义均合理但更具吸引力的 metadata；结果在十类工具情景取得 81% 至 95% ASR，并能绕过 prompt-level、auditor 和 MCP structured selection。 |
| 2025&#8209;04 | Prompt Injection Attack to Tool Selection in LLM Agents | attack、tool selection、malicious document、no-box optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.19793) | 暂未公开 | 针对 retrieval-selection 两阶段工具选择可被库内文档操纵；论文提出 ToolHijacker，在 no-box 设置优化恶意 tool document 使目标任务持续选中攻击工具；结果显著强于手工与自动注入，且多类预防和检测防御仍不足。 |

## Cross-Modal Environment-to-Tool Hijacking

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents | attack、audio prompt injection、tool-call hijacking、cross-modal consistency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28165) | [Code](https://github.com/Limax666/AudioAgentSecurity) | 持续语音交互让环境音频在用户不知情时进入 Agent context；论文用 instruction augmentation 与 scenario concealment 把恶意音频叠加到正常感知流，并提出 CADV 检测；结果在 Gemini 3 Pro 上平均 ASR 达 69.10%，CADV 的检测成功率超过 90%。 |

## MCP Threat Model 与系统分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0) | analysis、MCP taxonomy、semantic attack surface、cross-framework mapping | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.18063) | 暂未公开 | 针对传统 software 与通用 LLM taxonomy 无法覆盖 MCP 的动态语义接口；论文从 protocol decomposition、框架映射和真实事件归纳 38 类威胁；结果将 tool description poisoning、parasitic chaining 和 dynamic trust violation 映射到 STRIDE、OWASP LLM 与 Agentic Top 10。 |

## MCP Tool Poisoning 与 Privacy Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP | attack、implicit tool poisoning、metadata injection、privilege abuse | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.07395) | 暂未公开 | 针对显式恶意工具容易因实际调用而暴露；论文以黑盒反馈迭代优化 poisoned metadata，让未被调用的恶意工具诱导 Agent 改用合法高权限工具完成攻击；结果在 MCPTox 的十二种 Agent 上最高达到 84.2% ASR，同时把恶意工具检出率压到 0.3%。 |
| 2025&#8209;09 | Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via Model Context Protocol | attack、MCP prompt injection、covert logging、data exfiltration | 未注明（OpenReview） | [OpenReview](https://openreview.net/forum?id=UVgbFuXPaO) | 暂未公开 | 针对 MCP metadata 可否在不破坏原任务质量时触发隐蔽隐私泄漏；论文把 injection 拆为 Trigger、Tool Binding、Justification 与 Pressure，诱导 Agent 额外调用恶意 logging tool；结果在五个真实 server 和四种 Agent 上可持续捕获 user query、tool response 与 agent reply。 |

## Tool-Result 与执行防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents | defense、multi-turn tool use、MT-AgentRisk、self-exploration | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62233) · [arXiv](https://arxiv.org/abs/2602.13379) | [Code](https://github.com/CHATS-lab/ToolShield) | 针对单步看来正常的 tool call 会在多轮组合后形成危险结果，论文以 MAT 将单轮有害任务转换成多轮序列，并让 ToolShield 在 sandbox 自探索工具后注入安全经验；结果多轮 ASR 平均增加 16%，防御可平均降低 30%。 |
| 2026&#8209;01 | Towards Verifiably Safe Tool Use for LLM Agents | defense、tool authorization、formal specification、runtime verification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.08012) | 暂未公开 | 针对自然语言 safety prompt 无法为真实工具动作提供可验证保证；论文将 policy 编译为可检查的调用约束并在执行前验证参数和状态；结果把部分 Agent safety requirement 转化为独立于模型服从性的 runtime property。 |
| 2026&#8209;01 | Defense Against Indirect Prompt Injection via Tool Result Parsing | defense、indirect prompt injection、tool-result parsing、instruction-data separation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.04795) | [Code](https://github.com/qiang-yu/agentdojo/tree/tool-result-extract) | 针对 Agent 把 tool output 中的数据和攻击指令放入同一上下文；论文抽取任务所需事实并隔离原始返回值后再交给 planner；结果在降低 indirect injection 的同时保留多数良性任务效用。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | ToolSafe: Enhancing Tool Invocation Safety of LLM-based Agents via Proactive Step-level Guardrail and Feedback | defense、tool invocation、step-level guard、TS-Flow | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10156) | [Code](https://github.com/MurrayTom/ToolSafe) | 针对不安全 tool call 需要在执行前发现的问题，论文构建 TS-Bench，以多任务 RL 训练 TS-Guard，并用 guard feedback 驱动 TS-Flow；结果平均减少 65% 有害调用并改善受注入时的良性任务完成率。 |
| 2025&#8209;12 | MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers | benchmark、MCP server、multi-turn evaluation、cross-server attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.15163) | [Code](https://github.com/xjzzzzzzzz/MCPSafety) | 针对现有 MCP 测试缺少真实 server 与跨服务协调的问题，论文在五个领域构建覆盖 server、host、user 三侧的多轮攻击；结果所有受测模型都存在明显 vulnerability 与 safety-utility trade-off。 |
| 2025&#8209;10 | MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents | benchmark、MCP pipeline、real tool execution、NRP | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.15994) | [Code](https://github.com/dongsenzhang/MSB) | 针对 MCP 安全结论来自零散 demo、难以横向比较的问题，论文沿 planning、invocation 和 response handling 定义十二类攻击并运行真实工具；结果更强的工具调用和指令跟随能力反而常带来更高 vulnerability。 |
| 2025&#8209;09 | SafeToolBench: Pioneering a Prospective Benchmark to Evaluating Tool Utilization Safety in LLMs | benchmark、prospective safety、malicious instruction、tool risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.07315) | 暂未公开 | 针对在工具执行后才判断风险无法阻止不可逆伤害；论文从 user instruction、tool 本身及二者组合构建 prospective safety benchmark，并提出 SafeInstructTool；结果显示现有方法无法覆盖全部调用风险，而联合视角能提升执行前风险意识。 |
| 2025&#8209;08 | MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols | benchmark、MCP attack surface、security specification、playground | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.13220) | [Code](https://github.com/AIS2Lab/MCPSecBench) | 针对 MCP toolchain 缺少系统化威胁复现，论文形式化 secure MCP、归纳四个攻击面十七类威胁并提供模块化 playground；结果三类主流平台均可被攻破，现有保护平均成功率不足 30%。 |
| 2025&#8209;08 | MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers | benchmark、MCP tool poisoning、metadata injection、real-world server | AAAI 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/40895) | [Code](https://github.com/zhiqiangwang4/MCPTox-Benchmark) | 针对 MCP tool poisoning 此前主要停留在孤立案例、缺少真实规模评测；论文基于 45 个在线 server 与 353 个真实 tool 构建覆盖十类风险的 metadata injection；结果 20 个受测 Agent 普遍脆弱，且更强 instruction following 并未带来有效拒绝。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents | defense、prompt injection、tool-use agent、tool interface | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.29254) | [Code](https://github.com/snowcatsmoking/SafeKeep) | 论文发现 schema-formatted tool specification 会削弱模型内部 refusal signal，并提出 SafeKeep 用扁平文本规格独立做安全判断、原 schema 负责执行；有害请求拒答率从 23.8% 升至 70.6%，观察级注入 ASR 从 25.6% 降至 2.5%。 |
| 2026 | Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks | defense、multi-agent evaluation、tool-use agent、tool interface | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65283) | 暂未公开 | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 Speculative Safety Honeypot 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于智能体攻击面治理。 |
| 2026 | Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications | defense、RAG code generation、knowledge injection、tool-use agent | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-tong) | 暂未公开 | 针对 repository-grounded 代码生成会通过公开 API 继承固定版本中的 CVE，IoTRAGuarder 构建版本感知的反向调用链与双层检索约束，将 44 个 Zephyr 任务的 security success rate 从 5.11% 提至 78.41%。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Open Schrödinger’s Closed Box: Identifying Retrieval Augmented Generation in API-Accessible Large Language Model Services | detection、tool-use agent、tool interface、action integrity | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.208/) | 暂未公开 | 针对黑盒 API 隐藏服务是否采用 RAG 及其组件，RAG-ID 按三档攻击者知识设计六种探测，在几乎无先验时识别准确率最高 99.97%，并可继续推断模型和知识库属性。 |
| 2026 | MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning | detection、mobile agent、policy auditing、trajectory learning | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/jiang-changyue) | 暂未公开 | 针对 mobile agent 的越权行为难以从长交互轨迹审计的问题，MATE 用合成驱动学习构建 14 万条轨迹与 MATEBench，将策略违规检测准确率提升至 95% 以上，较既有方法提高逾 20%。 |
| 2026 | Causal Detection of Multi-Step LLM Agent Attacks | detection、causal analysis、tool-use agent、tool interface | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64714) | 暂未公开 | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 Causal Detection of Multi-Step LLM 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于智能体攻击面治理。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents | benchmark、tool-use agent、tool interface、action integrity | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61155) | [Code](https://github.com/epfl-nlp/helpful-to-a-fault) | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文构建 Helpful to a Fault 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于智能体攻击面治理。 |

> Agent tool-call chain 的资源放大和 MCP-based DoS 主记录见 [Agent 与多 Agent DoS](../dos/agent-system-dos.md)。
