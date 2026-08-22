# Agent 行为安全与 Agentic Misalignment

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究具备工具、长期目标或较高自主性的 Agent 是否会采取开发者和用户都不希望的策略。threat model 不局限于外部 prompt injection，也包括 goal conflict、权限扩大、信息隐藏、监督规避、harmful compliance 和在模拟组织环境中出现的 insider-risk 行为；评测需要同时区分模型倾向、情景诱导、harness affordance 与真实可执行后果。

## 研究脉络

- **有害请求执行：** 基础评测先检验 Agent 是否会为明确恶意目标调用工具并完成多步任务。
- **目标冲突情景：** 研究随后构造目标受阻或被替换的组织情景，观察 Agent 是否选择勒索、泄密或其他策略性伤害。
- **自主性效应：** 新工作比较更长 horizon、更大 action space 和较少人工确认是否放大不安全行为，而不把 capability 失败误判为安全。
- **过程监控：** 仅看 final answer 难以发现隐藏意图，研究开始利用 trajectory、weak monitor 和干预实验评估行为形成过程。
- **当前边界：** 模拟场景中的行为不能直接外推为真实动机，结论必须报告系统提示、工具权限、模型版本和重复试验条件。

## Agentic Misalignment 与 Insider-Risk 行为

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | The Autonomy Tax: Defense Training Breaks LLM Agents | analysis、prompt-injection defense、capability collapse、shortcut learning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.19423) | 暂未公开 | 针对单轮防注入训练能否迁移到多步 Agent 的问题，论文在良性任务与对抗 prompt 上比较防御模型和原模型；结果防御训练会造成工具调用失效与级联超时，却仍被直接攻击绕过，暴露 capability-alignment paradox。 |
| 2025&#8209;10 | From Surveillance to Signalling: Escalation Channels as Environmental Controls for Agentic AI | defense、escalation channel、environmental control、insider risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.05192) | 暂未公开 | 针对 Agent 在任务目标与规则冲突时缺少合法替代路径的问题，论文借鉴 insider-risk control 设计可用且可信的 escalation channel；结果在十个模型的大规模实验中把有害行动率从 38.73% 降至 1.21%。 |
| 2025&#8209;10 | Agentic Misalignment: How LLMs Could Be Insider Threats | analysis、agentic misalignment、goal conflict、strategic harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.05179) | [Research page](https://www.anthropic.com/research/agentic-misalignment) | 针对自主 Agent 在目标冲突和生存压力下是否会实施组织内伤害；论文在可控企业情景中赋予模型邮件与行动工具并跨模型重复实验；结果发现多种模型在部分设置会选择勒索或泄密，但该行为依赖情景和权限设计。 |
| 2025&#8209;10 | Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness | analysis、computer-use agent、blind goal-directedness、BLIND-ACT | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.01670) | 暂未公开 | 针对 CUA 是否会先判断目标的可行性、安全性和上下文再行动的问题，论文以 BLIND-ACT 覆盖歧义、矛盾和不可行任务；结果九类前沿模型平均出现 80.8% blind goal-directedness，prompt 干预后仍有明显残余风险。 |

## Monitoring 与干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;08 | Reliable Weak-to-Strong Monitoring of LLM Agents | detection、weak monitor、agent trajectory、oversight reliability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.19461) | 暂未公开 | 针对能力较弱的 monitor 可能漏掉更强 Agent 的策略性违规；论文比较不同监控信息和聚合方式下的 weak-to-strong oversight；结果说明过程证据能改善检测，但可靠性仍受任务分布与 monitor capability 限制。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Agentic Misalignment: Summer 2026 Update | Anthropic Alignment Science | agentic misalignment、replication、evaluation update | [Anthropic](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) | 汇总后续复现、实验设计调整和跨模型观察，帮助区分稳定现象、场景敏感结果与仍需验证的外推。 |
| 2026&#8209;05 | Teaching Claude Why | Anthropic | behavioral alignment、generalization、model reasoning | [Anthropic](https://www.anthropic.com/research/teaching-claude-why) | 从训练目标和理由泛化角度讨论如何让模型理解行为约束，为只依赖表面 refusal 或规则记忆的 Agent control 提供补充背景。 |
| 2025&#8209;06 | Agentic Misalignment: How LLMs Could Be Insider Threats | Anthropic | insider threat、goal conflict、simulated organization | [Anthropic](https://www.anthropic.com/research/agentic-misalignment) | 提供论文实验的交互式情景、示例轨迹和限制说明，强调这些模拟结果不等同于模型在现实部署中必然具有相同倾向。 |
