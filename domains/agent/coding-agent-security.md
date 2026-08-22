# Coding Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究能够读取 repository、issue、文档和 CI log，并修改文件、执行 shell、访问网络和提交变更的 Coding Agent。主要风险包括 malicious issue/repository instruction、dependency 与 skill supply chain、secret exfiltration、生成或执行恶意代码、对良性任务做越界修改，以及 defense 只在 base model 而没有在 Agent permission layer 生效。普通 code model vulnerability 若不涉及 Agent workflow 则不收录。

## 研究脉络

- **代码输出安全：** 初期评测集中于模型是否生成 vulnerable 或 malicious code，但未观察代码实际执行及工具副作用。
- **Agentic red teaming：** 研究加入 sandbox、adaptive attacker 和多种 coding product，联合检查生成、执行、debugging 与环境变化。
- **Repository 输入攻击：** issue、comment、PDF、README 和 tool output 都可承载恶意要求，并借 Agent 权限形成持久修改或数据泄漏。
- **良性任务越权：** 新 benchmark 把 overeager action 建模为 authorization failure，区分主动做多了和任务能力不足。
- **当前边界：** model refusal、framework approval、OS sandbox、secret scope 和 patch review 必须分别度量，不能把任一层的阻断归因于整体安全。

## Malicious Request 与 Prompt Injection

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests | benchmark、malicious issue、delivery vector、deployed coding agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.20759) | 暂未公开 | 针对 Coding Agent 会把 issue、comment 和附件直接转化为文件及 shell action；论文以四类攻击、六种投递载体和扰动测试 Cursor、Claude Code 与 Codex Desktop；结果 66.5% 恶意 issue 穿透模型和 Agent guardrail，framework layer 提供的额外阻断有限。 |
| 2026&#8209;01 | Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems | survey、coding assistant、delivery vector、protocol ecosystem | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.17548) | 暂未公开 | 针对 Coding Agent 的注入分散在 repository、skill、tool 与 MCP 研究中；论文以 delivery vector、attack modality 和 propagation behavior 归纳相关文献；结论是 prompt filtering 不能覆盖执行与供应链攻击，需要架构级纵深防御。 |

## 良性任务下的越权行为

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks | benchmark、scope expansion、authorization boundary、permission gating | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.18583) | 暂未公开 | 针对 Coding Agent 在良性请求中删除无关文件或改写未授权配置的 scope expansion；论文以 paired consent variants 和双通道 tool audit 构建 OverEager-Bench；结果 framework permission design 的影响大于部分 model 差异，显式写出授权范围还会掩盖真实边界推断能力。 |

## 自动 Red Team 与 Blue Team

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | BlueCodeAgent: A Blue Teaming Agent Enabled by Automated Red Teaming for CodeGen AI | defense、code analysis、automated red team、dynamic validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.18131) | 暂未公开 | 针对 code safety defense 对 unseen risk 容易过度保守或漏检；论文让 red team 持续产生风险样例，再由 constitution、code analysis 和 dynamic execution 组成多层 blue team；结果跨三类任务平均提高 12.7% F1，并以动态分析减少 vulnerable-code detection 假阳性。 |
| 2025&#8209;10 | RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents | attack、adaptive red teaming、sandbox execution、jailbreak composition | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.02609) | 暂未公开 | 针对静态 risky prompt 无法搜索不同 jailbreak tool 的组合边界；论文用 adaptive memory 选择和组合攻击，并在 sandbox 根据执行结果而非只靠 LLM judge 评估；结果在多语言与多种 code agent 上提高漏洞发现率，并暴露真实产品中的新风险。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | A Jagged Frontier: Evaluating Robustness of Code Agents to Semantics-Preserving Transformations | benchmark、adversarial robustness、coding agent、repository attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18389) | 暂未公开 | AI 编码智能体正越来越多地用于解决真实软件问题，但它们面对表面代码变化时的可靠性仍缺少理解；我们评估：当周围代码库被改写为语义等价形式时，能够修复代码仓库级问题的编码智能体是否仍然可靠；结果表明，即使顶尖前沿模型也会受到语义保持扰动影响，而且影响并不均匀，这引发了对 AI 编码智能体在多样真实代码库中部署可靠性的担忧。 |
| 2026&#8209;08 | Benchmarking Automated Security Patch Backporting: How Far Are We? | benchmark、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17671) | 暂未公开 | Porting Benchmark 统一评测五种程序分析、LLM prompt 与 Agent 安全补丁回迁工具；最佳 commit success 从简单 patch 的 85.2% 降到复杂 patch 的 24.0%，动态子集还显示 exact match 会低估有效适配并漏掉集成失败。 |
| 2026&#8209;08 | WeSCE: A Benchmark for Measuring Security Drift in LLM-Driven Code Editing | benchmark、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15092) | 暂未公开 | 在这项工作中，我们引入了 WeSCE，这是一个在弱安全约束下量化代码编辑安全漂移的基准，其中任务仅指定功能目标，而没有明确的安全要求；为了量化安全漂移，我们提出了一种连续的风险表示，通过统一的公式聚合异构漏洞信号，并定义漂移度量来捕获代码转换下总体风险、最坏情况严重性和漏洞分布的变化，提供从平均情况行为到最坏情况重点的安全多尺度视图。 |
| 2026&#8209;08 | Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model | benchmark、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13867) | [Code](https://github.com/sjarmak/engineering-reliable-coding-agents) | 人工智能编码代理通常作为模型进行评估，但作为系统进行部署；本专着研究了这些边界，并开发了一个可靠地评估和操作编码代理的框架；审查是结构化的而不是详尽的，证据强度因主题而异，结果取决于工作负载和配置。 |
| 2026&#8209;04 | Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows | benchmark、coding agent、evaluation exploitation、user pressure | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.20200) | [Project](https://ucsc-vlaa.github.io/AgentPressureBench) | 针对用户施压是否促使 coding agent 操纵公开评测的问题，AgentPressureBench 在 34 个任务、13 个 agent 和 1,326 条轨迹中发现 403 次 exploit，压力将首次作弊从平均第 19.67 轮提前到第 4.08 轮。 |
| 2026&#8209;03 | SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark | benchmark、adversarial robustness、coding agent、repository attack | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62669) · [arXiv](https://arxiv.org/abs/2603.00520) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文构建 SWE-ABS 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于智能体部署安全与故障恢复。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | When "Correct" Is Not Safe: Can We Trust Functionally Correct Patches Generated by Code Agents? | defense、agent safety、coding agent、repository attack | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.707/) | 暂未公开 | 针对代码 agent 的补丁只检查功能正确性，FCV-Attack 以单次黑盒查询即可让 12 种 agent–模型组合生成测试全过但含漏洞的补丁，例如 GPT-5 Mini + OpenHands 在 CWE-538 上攻击成功率达 40.7%。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Workspace Topology as an Attack Vector in Agentic Coding Assistants | attack、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14876) | 暂未公开 | 代理编码助手正在广泛使用，不仅在新代码开发中，而且在快速导入和利用第三方代码方面；由于这些编码工具在开发人员工作空间内具有广泛的文件系统访问权限，因此存在导入恶意代码的风险；我们的研究结果为跨不同环境的编码代理的评估和安全测试提供了实用价值，同时强调了未受污染的测试环境对于获得可靠结果和结论的重要性。 |
| 2026&#8209;07 | Distributed Attacks in Persistent-State AI Control | attack、AI control、persistent state、coding agent | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2607.02514) | 暂未公开 | 针对 coding agent 可跨多个 PR 分散并择机完成 covert side task 的新攻击面，Iterative VibeCoding 显示单一 monitor 无法兼顾渐进与集中攻击，stateful link tracker 配合多 monitor ensemble 可将渐进攻击逃逸率从 93% 降至 47%。 |
| 2026&#8209;02 | CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability | attack、cyber misuse、coding agent、repository attack | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65622) · [arXiv](https://arxiv.org/abs/2602.03012) | [Code](https://github.com/livecvebench/CVE-Factory) | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文提出 CVE-Factory 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于智能体攻击面治理。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models | analysis、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17956) | [Code](https://github.com/JaviMaligno/code-world-models) | 在代码世界模型范式中，LLM 合成一个可执行世界模型，由经典规划器搜索；当该模型能复现采样到的状态转移时，它就会被接受；我们研究这种接受条件在连续控制中究竟能证明什么；使用独立样本重新评估全部 1,034 个制品后确认：接受条件只能证明样本一致性，不能证明更多；即便门控在理论上确实有信息，它覆盖的也只有被利用规划器查询的大约 2%。 |
| 2026&#8209;08 | LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents | analysis、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17393) | 暂未公开 | 面向编码智能体的强化学习越来越依赖长时间运行的智能体执行框架，以管理工具集成、代码仓库上下文和执行反馈；为此，我们提出 LEGO-RL，一种无需修改执行框架内部控制流，即可把原生编码智能体执行框架与可扩展策略梯度优化连接起来的框架；在 SWE-bench Verified 上，LEGO-RL 分别使 Qwen3.5-35B-A3B 在 OpenHands SDK 上从 64.0% 提升至 70.4%，在 Claude Code 上从 62.4% 提升至 68.2%，在 OpenCode 上从 57.2% 提升至 66.6%，同时将 rollout 与训练概率的相关性保持在 0.99 以上。 |
| 2026&#8209;08 | The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks | analysis、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16630) | 暂未公开 | 存储库规模的编码需要代理在有界上下文窗口内保持测试、导入、配置和迁移规则一致；我们将其建模为重建耦合事实图：在每次编辑时，所需的事实来自最近的上下文或参数记忆，并且两者都没有涵盖的事实形成连贯性债务；可用性决定结果，而距离则不然：隐瞒事实的成本恰好是它所支持的工作量，而提供的事实在远离编辑的地方和在编辑旁边的地方一样有效。 |
| 2026&#8209;08 | Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation | analysis、coding agent、repository attack、code security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14711) | 暂未公开 | AI 编码智能体基准测试与 Chen 等人一起对代理进行了排名；我们诊断这个操作化错误，通过反例证明它，并提出reliability@k，正确应用相同的估计器，n = 独立生成，c = 每（任务，代理）对的完全通过推出；有证据表明功能正确性并不意味着安全性，我们还提出了安全调整的可靠性@k，它只计算功能正确且不存在高严重性不安全模式的部署。 |

## Survey 与 Taxonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Adversarial Review: Structured Disagreement for Grounded Agentic Code Review | survey、adversarial robustness、coding agent、repository attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18167) | 暂未公开 | 早期多智能体 LLM 系统常使用角色分离的团队，但增加智能体数量在代码仓库级编码任务上的收益递减；我们研究子智能体范式能否支持一个折中点：以最低开销实现智能体协作，而不使用庞大的多智能体团队；总体而言，AR 表明协作代码审查不需要大量智能体或复杂通信结构；关键在于使分歧保持最小、结构化且以证据为依据。 |

> Coding Agent 使用第三方 skill 的供应链攻击见 [Skill、Plugin 与供应链安全](skill-and-plugin-supply-chain-security.md)，trajectory debugging 和 failure recovery 见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)。
