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
| 2025&#8209;10 | CompAgent: An Agentic Framework for Visual Compliance Verification | defense、visual compliance、tool routing、agentic verification | CVPR 2026 GRAIL-V Workshop | [arXiv](https://arxiv.org/abs/2511.00171) | 暂未公开 | 针对 MLLM 难以同时读取细粒度视觉证据并执行复杂规则的问题，论文由 Planning Agent 选择专用视觉工具，再由 Verification Agent 综合 policy 判断；结果在 UnsafeBench 上提高视觉合规验证 F1。 |
| 2025&#8209;10 | Analyzing and Internalizing Complex Policy Documents for LLM Agents | defense、policy internalization、CAP-CPT、workflow complexity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.11588) | 暂未公开 | 针对 Agent 每轮携带复杂业务 policy 成本高且直接 SFT 随规则复杂度退化的问题，论文用 CC-Gen 分级评测，并以 CAP-CPT 按规则类型生成预训练数据；结果压缩 prompt 并改善 policy adherence。 |
| 2025&#8209;10 | Building a Foundational Guardrail for General Agentic Systems via Synthetic Data | defense、pre-execution guard、synthetic trajectory、cross-planner transfer | 未注明（arXiv） | [OpenReview](https://openreview.net/forum?id=M47SWYubR5) · [arXiv](https://arxiv.org/abs/2510.09781) | [Code](https://github.com/HowieHwong/Agentic-Guardian) | 针对动作执行后再审核难以撤销现实影响的问题，论文用 AuraGen 注入分级风险 trajectory、训练跨 planner 的 Safiron，并建立 Pre-Exec Bench；结果支持 plan 阶段的风险检测、分类和解释。 |
| 2025&#8209;10 | Learning Efficient Guardrails for Compliance | defense、policy trajectory、prefix violation、lightweight guard | ICML 2026 | [arXiv](https://arxiv.org/abs/2510.03485) | [Project](https://rakanwen.github.io/policyguard-page/) | 针对 long-horizon Web Agent 缺少真实 policy compliance 数据且通用 judge 成本高的问题，论文构建 policy-trajectory pairs 并训练 PolicyGuard；结果在完整轨迹和 prefix violation detection 上兼顾效率与 unseen-domain 泛化。 |
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
