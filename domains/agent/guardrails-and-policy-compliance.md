# Agent Guardrail 与 Policy Compliance

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究部署在 Agent 外部或 trajectory 中的独立安全控制层。判断对象从单轮 prompt/response 扩展到 observation、plan、tool call、state transition、workflow 与完整 trajectory，重点处理 prompt injection、危险动作、敏感信息泄露、组织 policy 违规、动作前介入，以及 guardrail 自身的资源消耗和规避风险。

## 研究脉络

- **Action-local 审核：** 早期方案在工具调用前后判断单个 action 是否有害，但难以识别遗漏确认、顺序错误等跨步骤程序违规。
- **Trajectory-level guard：** Pre-Exec Bench、AgentDoG 和 PolicyGuardBench 将计划前缀或完整轨迹作为判断对象，使 guard 能在动作执行前检测、分类和解释风险。
- **专门攻击面：** WebAgentGuard 把网页 prompt injection detection 与执行 Agent 解耦，NSFA taxonomy 进一步覆盖数据泄露、恶意代码、tool misuse 与 resource exhaustion。
- **Policy workflow：** Policy internalization 降低长规则文档的上下文开销，PolicyGuide 将 policy 编译为带状态的 workflow graph 并持续给出 remediation。
- **Guardrail 自身安全：** Guardrail DoS 表明 reasoning 和 schema-following 会成为放大面，因此还需要约束 token、latency 与共享服务资源。

## Workflow、Action 与 Prompt Injection 防护

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents | defense、workflow graph、procedural compliance、proactive verifier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19861) | 暂未公开 | 针对 action-local guard 无法发现遗漏步骤和完整程序违规的问题，论文把领域 policy 编译为持久化 workflow graph，并在每个用户轮次由 verifier 给出合规 remediation；结果提高多个客服 Agent 域的端到端流程通过率。 |
| 2026&#8209;07 | SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification | defense、operational threat、dual-mode guard、extensible taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.13081) | 暂未公开 | 针对 Agent guard 风险类别零散且实时判断与解释需求冲突的问题，论文建立 NSFA taxonomy，并组合离线 generative reasoning 与低延迟 classification head；结果覆盖多语言输入输出和新增威胁类别。 |
| 2026&#8209;05 | LiSA: Lifelong Safety Adaptation via Conservative Policy Induction | defense、lifelong adaptation、incident feedback、policy memory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14454) | 暂未公开 | 针对 Agent 上线后只能从稀疏带噪事故中逐步发现新风险的问题，论文在不修改基础 guard 的情况下将可靠反馈归纳为结构化 memory；结果使后续交互能调用新 policy，并以保守过滤减少错误规则累积。 |
| 2026&#8209;04 | WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents | detection、web prompt injection、parallel guard agent、multimodal webpage | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.12284) | 暂未公开 | 针对恶意指令可隐藏在 HTML 或页面截图中操纵 Web Agent 的问题，论文让专用 guard agent 与执行 Agent 并行，并以多模态合成数据、SFT 和 RL 训练；结果提升 prompt injection 检测并维持任务效用。 |
| 2025&#8209;10 | Analyzing and Internalizing Complex Policy Documents for LLM Agents | defense、policy internalization、CAP-CPT、workflow complexity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.11588) | 暂未公开 | 针对 Agent 每轮携带复杂业务 policy 成本高且直接 SFT 随规则复杂度退化的问题，论文用 CC-Gen 分级评测，并以 CAP-CPT 按规则类型生成预训练数据；结果压缩 prompt 并改善 policy adherence。 |
| 2025&#8209;10 | Building a Foundational Guardrail for General Agentic Systems via Synthetic Data | defense、pre-execution guard、synthetic trajectory、cross-planner transfer | 未注明（arXiv） | [OpenReview](https://openreview.net/forum?id=M47SWYubR5) · [arXiv](https://arxiv.org/abs/2510.09781) | [Code](https://github.com/HowieHwong/Agentic-Guardian) | 针对动作执行后再审核难以撤销现实影响的问题，论文用 AuraGen 注入分级风险 trajectory、训练跨 planner 的 Safiron，并建立 Pre-Exec Bench；结果支持 plan 阶段的风险检测、分类和解释。 |
| 2025&#8209;10 | Learning Efficient Guardrails for Compliance | defense、policy trajectory、prefix violation、lightweight guard | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/60652) · [arXiv](https://arxiv.org/abs/2510.03485) | [Project](https://rakanwen.github.io/policyguard-page/) | 针对 long-horizon Web Agent 缺少真实 policy compliance 数据且通用 judge 成本高的问题，论文构建 policy-trajectory pairs 并训练 PolicyGuard；结果在完整轨迹和 prefix violation detection 上兼顾效率与 unseen-domain 泛化。 |
| 2025&#8209;10 | CompAgent: An Agentic Framework for Visual Compliance Verification | defense、visual compliance、tool routing、agentic verification | CVPR 2026 GRAIL-V Workshop | [arXiv](https://arxiv.org/abs/2511.00171) | 暂未公开 | 针对 MLLM 难以同时读取细粒度视觉证据并执行复杂规则的问题，论文由 Planning Agent 选择专用视觉工具，再由 Verification Agent 综合 policy 判断；结果在 UnsafeBench 上提高视觉合规验证 F1。 |
| 2025&#8209;02 | AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection | defense、lifelong guardrail、adaptive safety check、tool compatibility | ACL 2025 Main | [ACL Anthology](https://aclanthology.org/2025.acl-long.399/) | [Project/Code](https://github.com/SaFoLab-WISC/AGrail4Agent) | 针对固定规则难同时覆盖 task-specific 与 CIA-oriented system risk；论文让 AGrail 持续生成并优化 safety check，并适配不同 Agent 与工具；结果对多类风险保持强检测能力并能跨任务迁移。 |

## Trajectory Guard Model 与诊断

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security | defense、trajectory guard、alignment diagnosis、scalable deployment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29801) | [Code](https://github.com/AI45Lab/AgentDoG) | 针对完整 Agent safety framework 难以低成本扩展到不同模型与任务的问题，论文将 diagnostic guard、trajectory scoring 和 alignment 过程组合为轻量框架；结果展示其跨 Agent 场景的可扩展安全判断能力。 |
| 2026&#8209;01 | AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security | detection、diagnostic guardrail、trajectory assessment、agent safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.18491) | [Code](https://github.com/AI45Lab/AgentDoG) | 针对单点输出审核无法解释 Agent 长程行为风险来源的问题，论文以 diagnostic guardrail 对 trajectory 进行多维安全诊断；结果为风险定位、比较和后续 alignment 提供统一判断接口。 |

## 针对 Agent Guardrail 的攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails | attack、guardrail DoS、reasoning amplification、poisoned document | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.14517) | 暂未公开 | 针对 Agent guard 的 reasoning 与 schema-following 可被外部数据反向利用的问题，论文用搜索式 payload 与结构化 mutation 诱导超长推理；结果在多种模型和实际 Agent 中造成显著 token 与 latency amplification。 |

## Benchmark 与基础资源

| 时间 | 名称 | 类型 | 关联论文 | 作用与边界 |
| --- | --- | --- | --- | --- |
| 2026&#8209;07 | NSFA Benchmark Suite | operational threat benchmark | [SingGuard-NSFA](https://arxiv.org/abs/2607.13081) | 以 CIA triad 与 OWASP 指南交叉组织 Agent 风险，覆盖 user query、agent response、多语言和外部数据集；用于测试独立 guard 的分类与扩展性，不直接衡量任务完成质量。 |
| 2025&#8209;10 | CC-Gen | policy-complexity generator | [Policy Internalization](https://arxiv.org/abs/2510.11588) | 按复杂度生成含事实、行为和条件规则的 Agent policy 与交互，用于分离文档长度、流程结构和 internalization data 对遵循能力的影响。 |
| 2025&#8209;10 | Pre-Exec Bench | pre-execution trajectory benchmark | [Agentic-Guardian](https://arxiv.org/abs/2510.09781) | 覆盖多种工具与 branching trajectory，评测动作前 detection、risk category、rationale 和 cross-planner transfer。 |
| 2025&#8209;10 | PolicyGuardBench | policy-trajectory benchmark | [Project](https://rakanwen.github.io/policyguard-page/) · [Paper](https://arxiv.org/abs/2510.03485) | 提供 policy-trajectory pairs，并分别评测 full-trajectory 与 prefix-based violation detection，适合研究 Agent 在违规发生前的早期介入。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production | defense、jailbreak、multi-agent system、agent guardrail | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.08471) | [Code](https://github.com/Trams1017/SESG) | SESG 用监控、生成、验证和路由 Agent 从生产流量发现新 jailbreak 与新有害类别并自动生成下一轮训练数据；1.7B guardrail 可在 16–24 小时、约 2 小时人工投入内适应新威胁，两个月自动关闭 15 个场景中的 14 个。 |
| 2026&#8209;07 | Steering Instruction Hierarchies at Inference Time | defense、prompt injection、agent guardrail、action policy | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2607.26228) | [Code](https://github.com/cindy2000sh/v-steer) | 针对模型会让低权限 user/tool 指令覆盖 system constraint 的问题，V-Steer 依据首 token 的 direct logit attribution 编辑 cache 中的 value vector，在 7B–70B 模型上把受控冲突任务的主约束准确率从不足 18% 提高到最高 92%。 |
| 2026&#8209;06 | From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents | defense、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.05805) | [Code](https://github.com/YUHAOSUNABC/TRIAD) | TRIAD 将 guardrail 输出扩展为 proceed、refuse、update 三类带自然语言反馈的决策，并让 Agent 在每个规划步骤据此修订而非整项阻断；在 ASB 与 AgentHarm 上平均 ASR 降至 10.42%，同时保持较好的任务效用。 |
| 2026&#8209;05 | SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety | defense、agent safety、over-refusal、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64556) · [arXiv](https://arxiv.org/abs/2605.05704) | [Code](https://github.com/ljj-cyber/SafeHarbor) | SafeHarbor 从增强对抗样本提炼情境化防御规则，并以可分裂合并的层次 memory 在推理时动态注入；其在显式攻击下拒答率超过 93%，GPT-4o 模糊良性任务效用最高达 63.6%，改善 Agent 安全—误拒权衡。 |
| 2026&#8209;02 | Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense | defense、agent safety、agent guardrail、action policy | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60816) · [arXiv](https://arxiv.org/abs/2602.09012) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文提出 Next-Gen CAPTCHAs 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于智能体部署安全与故障恢复。 |
| 2026 | VIGIL: Defending LLM Agents Against Tool-Stream Injection via Verify-Before-Commit | defense、agent safety、LLM agent、agent guardrail | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.443/) | [Code](https://github.com/MINE-USTC/vigil) | 针对 tool stream 中元数据与运行反馈可劫持 agent 而静态隔离又破坏推理，VIGIL 采用 speculative reasoning 后 verify-before-commit，在 959 个 SIREN 用例上比动态防御多降逾 22% ASR，并使受攻击效用翻倍。 |
| 2026 | SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning | defense、reasoning safety、agent safety、LLM agent | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.522/) | 暂未公开 | 针对 MCP 扩大 agent 行为空间并放大错误，SafeMCP 以世界模型前瞻预测、主动工具过滤和即时干预限制危险能力，在 PowerSeeking Bench、ToolEmu 与 AgentHarm 上兼顾安全和任务效用。 |
| 2026 | SafeAgent: Safeguarding LLM Agents via an Automated Risk Simulator | defense、agent safety、LLM agent、agent guardrail | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1501/) | 暂未公开 | 针对多轮工具 agent 的指令、上下文和动作风险难以收集，SafeAgent 用 OTS 威胁模型自动生成压力测试与自反思安全响应，在四个开源模型上平均提升 45% 安全表现、真实终端任务提升 28.91%。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI | analysis、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18360) | [Code](https://github.com/besanson/sarc-suite-one-pass) | 智能体 AI 系统在行动执行前，会同时受到多项控制约束：权限、资源和证据门控都可能在执行前允许、降级或修复某项行动；本文的核心对象是“修复引起的控制耦合”：一项控制施加的修复可能改变另一项控制所评估的行动、证据或上下文，使后者先前的判断失效；辅助结果还给出：门控结果的正权重线性聚合能够抵消某个成员否决的精确条件；统一的跨控制证据集；以及组合不会产生任何新的检测覆盖范围，本文对此如实报告。 |
| 2026&#8209;08 | A Policy Algebra for Trust-Preserving Agentic AI Execution | analysis、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16402) | 暂未公开 | 基于大语言模型的代理框架主要优化能力：代理是否可以推理、检索信息、调用工具、委派工作和完成目标；本文将可靠能力定义为路径属性：只有当代理通过在身份、配置文件、工具、数据、内存、预算、制品、批准和审计约束下保持可接受的动作事件完成任务时，它才具有可靠的能力；该代数还跨多代理调用传播限制，并引入成本感知制品物化，随着预算风险的增加，它将开放式执行重定向到可恢复的结果。 |
| 2026&#8209;08 | Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance | analysis、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16055) | 暂未公开 | 现有的智能体基准测试询问代理是否完成了任务；我们询问它是否在政策范围内完成了它；更强的模型 (gpt-4.1-mini) 在相同条件下衰减了 3-6%，这表明分解的治理成本部分是模型能力的函数。 |
| 2026&#8209;08 | TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions | analysis、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15391) | 暂未公开 | 大语言模型（LLM）辅助的能源管理工具可以将自然语言上下文转换为结构化网格命令，但句法有效性并不意味着物理可接受性；本文提出了 TwinGridShield，这是一个独立于模型的运行时授权层，可在发布之前评估确定性网络孪生中的每个建议操作；在每总线负载测量误差为 +20% 和 -20% 的情况下，不安全验收达到 5.63%；当实际支路额定值比建模额定值低 20% 时，不安全验收达到 30.09%。 |
| 2026 | Agentic Oversight via Dialectic Reasoning | analysis、reasoning safety、agent guardrail、action policy | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1143/) | 暂未公开 | 针对超人模型的监督判断缺少可验证依据，Agentic Oversight 让两个专家围绕真实分歧辩论、由盲评模型进行辩证论证，在六项多语言和多模态任务上稳定优于单专家，并可把弱监督信号蒸馏回专家模型。 |

## 基础 Tool 与资源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents | tool、agent guardrail、action policy、workflow compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17153) | 暂未公开 | 检索增强生成（RAG）显著增强了大语言模型（LLM）的性能，但这些系统仍然容易受到知识中毒攻击，其中检索到的文档中的错误信息可能会影响模型的最终输出；在这项工作中，我们提出了一个改进的安全原则：只有能够进行系统 2 推理的代理才能访问不受信任的文档；这些发现为我们的改进原则提供了实证支持，并为安全 RAG 系统设计提供了更实用的基础。 |
