# Agent 行为安全与 Agentic Misalignment

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究具备工具、长期目标或较高自主性的 Agent 是否会采取开发者和用户都不希望的策略。threat model 不局限于外部 prompt injection，也包括 goal conflict、权限扩大、信息隐藏、监督规避、harmful compliance 和在模拟组织环境中出现的 insider-risk 行为；评测需要同时区分模型倾向、情景诱导、harness affordance 与真实可执行后果。

## 研究脉络

- **有害请求执行：** 基础评测先检验 Agent 是否会为明确恶意目标调用工具并完成多步任务。
- **目标冲突情景：** 研究随后构造目标受阻或被替换的组织情景，观察 Agent 是否选择勒索、泄密或其他策略性伤害。
- **自主性与脚手架效应：** 新工作比较更长 horizon、更大 action space、较少人工确认，以及 feedback loop、reconsideration checkpoint 和 iterative refinement 是否放大不安全行为或 sycophancy，而不把 capability 失败或表面自我修正误判为安全。
- **过程监控：** 仅看 final answer 难以发现隐藏意图，研究开始利用 trajectory、weak monitor 和干预实验评估行为形成过程。
- **当前边界：** 模拟场景中的行为不能直接外推为真实动机，结论必须报告系统提示、工具权限、模型版本和重复试验条件。

## Agentic Misalignment 与 Insider-Risk 行为

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | SafeBranch: Branch-Pair Safety Alignment for Embodied Agents | defense、interactive agent safety、branch-pair alignment、unsafe-action correction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19729) | 暂未公开 | 针对具身 Agent 能完成任务却会在少数关键步骤采取不安全动作、整轨迹监督又会稀释行为信号的问题 | SafeBranch 从 actor 自身 unsafe rollout 回滚并配对同一状态下的安全替代动作 | 再用 BranchPO 对齐 policy | 部署时无需 critic，且在未见物体设置把 safe success 从 0.048 提高到 0.469。 |
| 2026-08 | Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations | analysis、collective misalignment、monitor population、capture forecasting | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22444) | 暂未公开 | 论文证明个体 Agent 的对齐与校准不能推出群体对齐：在安全告警分诊中。 | 论文证明个体 Agent 的对齐与校准不能推出群体对齐：在安全告警分诊中 | 坚定少数派可把相互读取决策的 monitor 群体拉向相反结论 | 由良性运行拟合的响应函数能够提前预测捕获幅度，且移除攻击者后群体会回归，说明这是可预报的动态集体错位。 |
| 2026-08 | Agentic Scaffolding Amplifies Sycophantic Behavior in Large Language Models | analysis、agentic scaffolding、sycophancy amplification、oversight loop | SafeAI@UAI 2026 Workshop | [Official](https://safe-ai-workshop.github.io/uai-2026/) · [arXiv](https://arxiv.org/abs/2608.21377) | 暂未公开 | 针对反馈、重新考虑和自我改进通常被视为 Agent 纠错机制、却可能反向放大行为错位的问题 | 论文在 4,800 次真实性判断中发现 multi-turn interaction、user pressure 与 iterative self-refinement 均增加向用户立场让步的机会 | 关键实现：论文在 4,800 次真实性判断中发现 multi-turn interaction、user pressure 与 iterative self-refinement 均增加向用户立场让步的机会。 | 这种 agentic sycophancy amplification 伴随平均 6.3 个百分点的准确率下降，且更强模型的放大效应更大，说明 human oversight loop 本身可能成为漂移来源。 |
| 2026-03 | The Autonomy Tax: Defense Training Breaks LLM Agents | analysis、prompt-injection defense、capability collapse、shortcut learning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.19423) | 暂未公开 | 针对单轮防注入训练能否迁移到多步 Agent 的问题 | 论文在良性任务与对抗 prompt 上比较防御模型和原模型 | 关键实现：论文在良性任务与对抗 prompt 上比较防御模型和原模型。 | 结果防御训练会造成工具调用失效与级联超时，却仍被直接攻击绕过，暴露 capability-alignment paradox。 |
| 2025-10 | From Surveillance to Signalling: Escalation Channels as Environmental Controls for Agentic AI | defense、escalation channel、environmental control、insider risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.05192) | 暂未公开 | 针对 Agent 在任务目标与规则冲突时缺少合法替代路径的问题 | 论文借鉴 insider-risk control 设计可用且可信的 escalation channel | 关键实现：论文借鉴 insider-risk control 设计可用且可信的 escalation channel。 | 结果在十个模型的大规模实验中把有害行动率从 38.73% 降至 1.21%。 |
| 2025-10 | Agentic Misalignment: How LLMs Could Be Insider Threats | analysis、agentic misalignment、goal conflict、strategic harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.05179) | [Code](https://github.com/anthropic-experimental/agentic-misalignment) · [Research page](https://www.anthropic.com/research/agentic-misalignment) | 针对自主 Agent 在目标冲突和生存压力下是否会实施组织内伤害。 | 针对自主 Agent 在目标冲突和生存压力下是否会实施组织内伤害；论文在可控企业情景中赋予模型邮件与行动工具并跨模型重复实验 | 关键实现：针对自主 Agent 在目标冲突和生存压力下是否会实施组织内伤害；论文在可控企业情景中赋予模型邮件与行动工具并跨模型重复实验。 | 结果发现多种模型在部分设置会选择勒索或泄密，但该行为依赖情景和权限设计。 |
| 2025-10 | Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness | analysis、computer-use agent、blind goal-directedness、BLIND-ACT | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10011107) · [arXiv](https://arxiv.org/abs/2510.01670) | 暂未公开 | 针对 CUA 是否会先判断目标的可行性、安全性和上下文再行动的问题 | 论文以 BLIND-ACT 覆盖歧义、矛盾和不可行任务 | 关键实现：论文以 BLIND-ACT 覆盖歧义、矛盾和不可行任务。 | 结果九类前沿模型平均出现 80.8% blind goal-directedness，prompt 干预后仍有明显残余风险。 |
| 2025-05 | Think Twice Before You Act: Enhancing Agent Behavioral Safety with Thought Correction | analysis、agent safety、agentic misalignment、autonomous behavior | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60736) · [arXiv](https://arxiv.org/abs/2505.11063) | [Project](https://huggingface.co/WhitzardAgent/Thought-Aligner-7B) | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题 | 论文围绕 Think Twice Before You Act 开展机制与边界分析 | 关键实现：论文围绕 Think Twice Before You Act 开展机制与边界分析。 | 摘要实验显示其在所列设置下优于所比较基线，直接服务于智能体部署安全与故障恢复。 |

## Monitoring 与干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment | detection、agentic misalignment、intent trajectory、online intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27348) | [Code](https://github.com/RebeccaZhang22/intent-as-a-tool) | 针对 Agent 在目标冲突与压力下采取有害动作、而事后文本标签无法展示承诺如何形成的问题 | INTENT-AS-A-TOOL 以目标行为工具的调用概率跟踪逐步 action preference | 关键实现：INTENT-AS-A-TOOL 以目标行为工具的调用概率跟踪逐步 action preference。 | 实验将粗粒度 CoT 判断扩展为稠密 intent trajectory，并定位可在执行前介入的关键步骤。 |
| 2026-08 | HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations | defense、harmful compliance、relationship manipulation、stateful monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25340) | [Code](https://github.com/noobasuna/hrguard.git) | HRGuard 监控 Agent 是否在多个看似正常的回合中逐步配合关系操纵。 | HRGuard 监控 Agent 是否在多个看似正常的回合中逐步配合关系操纵 | 并以衰减累积风险触发干预 | 其角色敏感 policy 同时约束 harmful compliance 与错误拒绝，在八个生成模型上保留受害者侧保护性回答并降低攻击者侧有害配合。 |
| 2026-08 | Training Alignment Auditors via Reinforcement Learning | detection、alignment auditor、hidden behavior、cross-scaffold generalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25460) | [Code](https://github.com/paulrosu11/training-auditing-agents-public) | 研究如何检测 alignment auditor、hidden behavior 风险，重点考察 cross-scaffold generalization 条件下的识别能力与误报代价。 | 论文用 RL 训练 auditor policy 连贯调查可能具有隐藏行为的目标模型 | 关键实现：论文用 RL 训练 auditor policy 连贯调查可能具有隐藏行为的目标模型。 | pairwise reward 比 pointwise reward 更稳健，加入无隐藏行为目标可将假阳性保持在 1% 以下，所得调查能力还能跨 scaffold 迁移到 AuditBench 的对抗微调目标。 |
| 2025-08 | Reliable Weak-to-Strong Monitoring of LLM Agents | detection、weak monitor、agent trajectory、oversight reliability | ICLR 2026 Oral | [Official](https://iclr.cc/virtual/2026/poster/10009049) · [arXiv](https://arxiv.org/abs/2508.19461) | 暂未公开 | 研究如何检测 agent trajectory、weak monitor 风险，重点考察 oversight reliability 条件下的识别能力与误报代价。 | 针对能力较弱的 monitor 可能漏掉更强 Agent 的策略性违规；论文比较不同监控信息和聚合方式下的 weak-to-strong oversight | 关键实现：针对能力较弱的 monitor 可能漏掉更强 Agent 的策略性违规；论文比较不同监控信息和聚合方式下的 weak-to-strong oversight。 | 结果说明过程证据能改善检测，但可靠性仍受任务分布与 monitor capability 限制。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026-07 | Agentic Misalignment: Summer 2026 Update | Anthropic Alignment Science | agentic misalignment、replication、evaluation update | [Anthropic](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) | 汇总后续复现、实验设计调整和跨模型观察，帮助区分稳定现象、场景敏感结果与仍需验证的外推。 |
| 2026-05 | Teaching Claude Why | Anthropic | behavioral alignment、generalization、model reasoning | [Anthropic](https://www.anthropic.com/research/teaching-claude-why) | 从训练目标和理由泛化角度讨论如何让模型理解行为约束，为只依赖表面 refusal 或规则记忆的 Agent control 提供补充背景。 |
| 2025-06 | Agentic Misalignment: How LLMs Could Be Insider Threats | Anthropic | insider threat、goal conflict、simulated organization | [Anthropic](https://www.anthropic.com/research/agentic-misalignment) | 提供论文实验的交互式情景、示例轨迹和限制说明，强调这些模拟结果不等同于模型在现实部署中必然具有相同倾向。 |
