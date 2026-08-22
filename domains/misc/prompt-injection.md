# 提示注入

## 研究方向

提示注入研究攻击者如何把恶意指令嵌入网页、邮件、文档、工具输出或持久化 Agent 状态，从而劫持模型后续行为；重点包括跨会话攻击、自动化红队、工具调用归因、实际应用风险与运行时防御。

## 研究脉络

- **攻击起点：** Prompt injection 最初通过单轮指令冲突覆盖系统或开发者意图。
- **攻击面扩展：** 攻击随后发展到 indirect、multimodal 和 cross-session stored injection。
- **防御与评测：** 防御由持续对抗训练扩展到 tool-call causal attribution 与可证明信息隔离，公开竞赛和自动 red-teaming 用于检验 adaptive attack。

## 攻击与真实系统风险

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems | attack、agent prompt injection、stored injection、cross-session persistence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04425) | 暂未公开 | 针对现有研究只考虑单会话攻击的问题，论文形式化跨会话存储型提示注入并构建分类体系、benchmark 与沙盒；结果表明持久状态会把短暂注入转化为可在未来会话重新触发的系统级漏洞。 |
| 2026&#8209;06 | Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings | attack、hiring-system injection、résumé injection、multi-injection | ACL 2026 | [arXiv](https://arxiv.org/abs/2606.27287) | [Code](https://github.com/preetb1199/Prompt_Injection_ACL26) | 针对求职者能否用隐藏指令操纵自动简历排序，论文比较单个与多个候选人注入及不同质量分布；结果发现稀少注入且候选质量接近时风险最大，广泛注入时收益会迅速消失。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense | defense、prompt injection、continual-learning defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19982) | 暂未公开 | 针对静态提示注入防御会随攻击演化而失效，论文用 GRPO 增量学习新攻击并以 margin-weighted replay 保留旧防御；结果相对所评估先进方法把攻击成功率最高降低 6.3 倍、平均降低 4.4 倍。 |
| 2026&#8209;03 | AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations | defense、agent prompt injection、indirect injection、causal attribution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.10749) | 暂未公开 | 针对语义过滤难以泛化到未知 payload，论文用反事实重放判断工具调用究竟由用户意图还是不可信观察驱动；结果在静态攻击下实现零 ASR，并较现有方法更能抵抗自适应攻击。 |
| 2025&#8209;02 | MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents | defense、agent prompt injection、indirect injection、provable defense | ICML 2025 | [arXiv](https://arxiv.org/abs/2502.05174) | [Code](https://github.com/kaijiezhu11/MELON) | 针对间接注入使 Agent 行动脱离用户任务，论文通过遮蔽用户提示后重执行并比较工具调用来检测攻击；结果在 AgentDojo 上同时提升攻击阻断率与正常任务效用。 |

## Benchmark 与公开评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages | benchmark、multimodal prompt injection、instruction hierarchy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19207) | [Code](https://github.com/naver-ai/VSysBench) | 针对多模态模型的 system message 层级缺少联合评测，论文用 VSysBench 同时衡量约束遵循和答案正确性并加入冲突用户指令；结果开源权重模型在冲突下合规性明显崩塌，视觉落地约束最难。 |
| 2026&#8209;03 | How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition | benchmark、agent prompt injection、indirect injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.15714) | [Code](https://github.com/GraySwanAI/ipi_arena_os) · [Dataset](https://huggingface.co/datasets/sureheremarv/ipi_arena_attacks) | 针对真实 Agent 间接提示注入风险缺少大规模证据，论文分析 464 名参与者对 13 个模型的 27 万余次攻击；结果显示所有模型均可受攻击且存在跨模型迁移策略，能力强弱与安全性相关性很弱。 |

## Red-Teaming Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses | tool、agent prompt injection、adversarial evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.13026) | [Code](https://github.com/albert-y1n/PISmith) | 针对静态攻击低估提示注入防御风险的问题，论文用带自适应熵正则和动态优势加权的 RL 训练黑盒攻击模型；结果在 13 个 benchmark 上揭示现有防御仍易被自适应攻击突破。 |

> Web、tool、skill 与 coding 环境中的具体 Agent 攻击面按系统组件整理在 [Agent Security](../agent/README.md)。
