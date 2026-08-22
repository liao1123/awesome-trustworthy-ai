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
| 2026&#8209;07 | HijackKV: New Threat in Position-Independent KV Cache Reuse | attack、KV cache reuse、prompt injection、instruction hierarchy | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi) · [arXiv](https://arxiv.org/abs/2607.19957) | 暂未公开 | 针对 position-independent KV cache 跨上下文复用的优化，HijackKV 将恶意行为编码进表面正常的缓存块，单次攻击成功率达 94%，且污染可持续并迁移到后续请求。 |
| 2026&#8209;07 | CPInj: Uncovering Prompt Injection Risks in Textual Collabo- rative Prompt Optimization | attack、collaborative prompt optimization、prompt injection、instruction hierarchy | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2607.18622) | 暂未公开 | 针对 textual collaborative prompt optimization 聚合多方 prompt 时的供应链风险，CPInj 用一个恶意本地 prompt 污染全局结果并在后续良性优化中持续存在；APAgg 只能部分恢复三类模型、五项任务上的安全性。 |
| 2026&#8209;06 | Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings | attack、hiring-system injection、résumé injection、multi-injection | ACL 2026 | [arXiv](https://arxiv.org/abs/2606.27287) | [Code](https://github.com/preetb1199/Prompt_Injection_ACL26) | 针对求职者能否用隐藏指令操纵自动简历排序，论文比较单个与多个候选人注入及不同质量分布；结果发现稀少注入且候选质量接近时风险最大，广泛注入时收益会迅速消失。 |
| 2026&#8209;06 | What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems | attack、agent prompt injection、stored injection、cross-session persistence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04425) | 暂未公开 | 针对现有研究只考虑单会话攻击的问题，论文形式化跨会话存储型提示注入并构建分类体系、benchmark 与沙盒；结果表明持久状态会把短暂注入转化为可在未来会话重新触发的系统级漏洞。 |
| 2026&#8209;05 | Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening | attack、prompt injection、resume screening、instruction hierarchy | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-mohan) · [arXiv](https://arxiv.org/abs/2605.28999) | [Code](https://github.com/UNITES-Lab/resume-injection-measurement) | 针对求职者可在简历中植入 prompt injection 操纵 LLM 筛选的问题，作者分析约 20 万份真实简历，发现约 1% 含隐藏注入且比例持续上升，其中超过 90% 没有显式恶意指令。 |
| 2026&#8209;01 | Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems | attack、indirect prompt injection、prompt injection、instruction hierarchy | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan) · [arXiv](https://arxiv.org/abs/2601.07072) | 暂未公开 | 针对网页注入必须先被 RAG 检索才会生效的现实障碍，该方法优化恶意内容的可检索性并实现近 100% retrieval rate，在 GPT-4o 上以约 0.21 美元单次成本取得超过 80% 的 SSH 数据外泄成功率。 |
| 2026 | Prompt Injection as Role Confusion | attack、prompt injection、instruction hierarchy、task hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64605) | 暂未公开 | 针对模型安全策略会被越狱提示或自动化红队绕过的问题，论文提出 Prompt Injection as Role Confusion 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于越狱风险测量与红队覆盖。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense | defense、prompt injection、continual-learning defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19982) | 暂未公开 | 针对静态提示注入防御会随攻击演化而失效，论文用 GRPO 增量学习新攻击并以 margin-weighted replay 保留旧防御；结果相对所评估先进方法把攻击成功率最高降低 6.3 倍、平均降低 4.4 倍。 |
| 2026&#8209;03 | AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations | defense、agent prompt injection、indirect injection、causal attribution | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/he-yu) · [arXiv](https://arxiv.org/abs/2603.10749) | 暂未公开 | 针对语义过滤难以泛化到未知 payload，论文用反事实重放判断工具调用究竟由用户意图还是不可信观察驱动；结果在静态攻击下实现零 ASR，并较现有方法更能抵抗自适应攻击。 |
| 2025&#8209;02 | MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents | defense、agent prompt injection、indirect injection、provable defense | ICML 2025 | [arXiv](https://arxiv.org/abs/2502.05174) | [Code](https://github.com/kaijiezhu11/MELON) | 针对间接注入使 Agent 行动脱离用户任务，论文通过遮蔽用户提示后重执行并比较工具调用来检测攻击；结果在 AgentDojo 上同时提升攻击阻断率与正常任务效用。 |

## Benchmark 与公开评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition | benchmark、agent prompt injection、indirect injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.15714) | [Code](https://github.com/GraySwanAI/ipi_arena_os) · [Dataset](https://huggingface.co/datasets/sureheremarv/ipi_arena_attacks) | 针对真实 Agent 间接提示注入风险缺少大规模证据，论文分析 464 名参与者对 13 个模型的 27 万余次攻击；结果显示所有模型均可受攻击且存在跨模型迁移策略，能力强弱与安全性相关性很弱。 |

## Red-Teaming Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses | tool、agent prompt injection、adversarial evaluation | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2603.13026) | [Code](https://github.com/albert-y1n/PISmith) | 针对静态攻击低估提示注入防御风险的问题，论文用带自适应熵正则和动态优势加权的 RL 训练黑盒攻击模型；结果在 13 个 benchmark 上揭示现有防御仍易被自适应攻击突破。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Your Agentic LLMs Secretly Encode Latent Signals of Indirect Prompt-Injection Exposure | analysis、prompt injection、adversarial robustness、instruction hierarchy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.02657) | [Code](https://github.com/jianshuod/IPI-exposure-signal) | 论文发现六个 Agentic LLM 的生成前 hidden state 可用线性 probe 以超过 90% AUROC 识别间接 prompt-injection 暴露；AGRI 按 probe 结果触发防注入推理，在 AgentDojo 上把 Qwen3.5-27B ASR 从 34.6% 降至 0%，同时基本保持效用。 |
| 2026 | CachePrune: Teaching LLMs What Not to Follow via KV-Cache Editing | analysis、prompt injection、instruction hierarchy、task hijacking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.70/) | 暂未公开 | 针对 LLM 把检索上下文中的数据误当指令，CachePrune 通过 attribution 找到 instruction-following neuron 并在 KV-cache 编码时剪除，在保持正常指令遵循的同时显著降低间接 prompt injection ASR。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | PIArena: A Platform for Prompt Injection Evaluation | benchmark、prompt injection、instruction hierarchy、task hijacking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1533/) | [Code](https://github.com/sleeepeer/PIArena) | 针对 prompt injection 攻防缺少统一且可扩展的比较环境，PIArena 集成多套攻击、防御和 benchmark 并加入反馈驱动的自适应攻击，揭示现有防御跨任务泛化差且仍会被 adaptive attack 绕过。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Security–Fidelity Tradeoffs: No Universal Defense Against Prompt Injection | defense、prompt injection、instruction hierarchy、task hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60901) | 暂未公开 | 针对越狱和提示注入在跨模型、长上下文或多模态条件下难以稳定拦截的问题，论文围绕 Security–Fidelity Tradeoffs 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于提示攻击检测与运行时防御。 |
| 2026 | RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse | defense、prompt injection、instruction hierarchy、task hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62356) | 暂未公开 | 针对越狱和提示注入在跨模型、长上下文或多模态条件下难以稳定拦截的问题，论文提出 RedVisor 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于提示攻击检测与运行时防御。 |
| 2025&#8209;11 | DRIP: Defending Prompt Injection via Token-wise Representation Editing and Residual Fusion | defense、prompt injection、representation editing、residual fusion | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2511.00447) | [Code](https://github.com/lindsey98/DRIP) | 针对 LLM 混淆可信指令与不可信数据而遭 prompt injection 的问题，DRIP 将数据 token 移出 instruction manifold 并以 residual path 重锚顶层指令，在保留效用的同时使自适应攻击 ASR 降低超过 66%。 |
| 2025&#8209;10 | The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections | defense、adaptive attack、jailbreak defense、prompt injection defense | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nasr) · [arXiv](https://arxiv.org/abs/2510.09023) | 暂未公开 | 针对防御论文常用非自适应攻击而高估安全性的问题，作者为 12 种 jailbreak 与 prompt-injection 防御设计针对性攻击，在多数设置中以超过 90% 成功率绕过防护。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution | detection、prompt injection、causal analysis、instruction hierarchy | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62590) · [arXiv](https://arxiv.org/abs/2602.07918) | 暂未公开 | 针对越狱和提示注入在跨模型、长上下文或多模态条件下难以稳定拦截的问题，论文提出 CausalArmor 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于提示攻击检测与运行时防御。 |
| 2026 | Localize and Neutralize: Gradient-Guided Token Suppression Against Visual Prompt Injection Attack | detection、prompt injection、instruction hierarchy、task hijacking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63777) | [Code](https://github.com/fish883/GTM-Defense) | 针对越狱和提示注入在跨模型、长上下文或多模态条件下难以稳定拦截的问题，论文提出 Localize and Neutralize 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于提示攻击检测与运行时防御。 |

> Web、tool、skill 与 coding 环境中的具体 Agent 攻击面按系统组件整理在 [Agent Security](../agent/README.md)。
