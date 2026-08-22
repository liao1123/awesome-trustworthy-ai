# Agent 记忆与技能投毒

[返回模型投毒与后门目录](README.md)

## 研究方向

这一方向研究不可信输入如何被 Agent 的 long-term memory、经验库、trajectory、skill 或 RL policy 持久保存，并在未来任务或特定状态下转化为行动。核心问题包括 memory write 与 retrieval 的信任边界、experience-to-skill promotion、自进化过程中的 provenance、跨 session 持久性、supply-chain backdoor，以及从写入、触发、后果到 repair 的全生命周期评测。

## 研究脉络

- **Memory poisoning：** 一条主线污染对话记忆、经验检索和知识库，使恶意影响跨 session 累积。
- **Skill 与 policy backdoor：** 另一条主线把后门植入 skill、trajectory 或 RL policy，在特定执行条件下触发异常行为。
- **评测与防御：** 评测开始覆盖 Agent 完整生命周期，防御则关注 step-level 行为约束与选择性修复。

## 记忆投毒与跨 Session 攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents | attack、agent memory poisoning、long-term memory、GhostWriter | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.06595) | 暂未公开 | 针对 personal agent 会从邮件等不可信来源保存长期记忆，论文用 GhostWriter 先隐藏注入、再等待相关任务检索激活；结果注入率约 98%、平均激活率约 60%，AM-Sentry 可显著降低风险。 |
| 2026&#8209;06 | Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents | attack、agent knowledge poisoning、security agent、RAG poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.24402) | 暂未公开 | 针对 RAG 投毒研究多停留在 QA、缺少对行动型 security agent 的影响分析，论文注入单篇恶意 exploit write-up 并提出 Verification Boundary；结果毒知识是否被采用取决于 Agent 能否获得足够外部证据反驳。 |
| 2026&#8209;05 | Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction | attack、agent memory poisoning、conversational injection、selective memory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29960) | 暂未公开 | 针对现代 memory pipeline 会选择性抽取和改写对话、使旧攻击难以写入，论文用 semantic bridge、entity masquerading 和 embedding optimization 构造 MemPoison；结果攻击成功率最高达 0.95。 |
| 2026&#8209;05 | Stateful Agent Backdoor | attack、agent memory poisoning、cross-session attack、state machine | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.06158) | [Code](https://anonymous.4open.science/r/stateful_agent_backdoor-E89F) | 针对现有 Agent 后门通常局限在单次 session，论文把攻击建模为 Mealy machine 并利用持久组件跨 session 推进状态；结果一次 trigger injection 后可分阶段自主执行，成功率达 80% 至 95%。 |
| 2026&#8209;05 | Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration | attack、agent memory poisoning、data exfiltration、dormant payload | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.01970) | 暂未公开 | 针对恶意 tool output 可被记忆但不必立即执行，论文用一次不可信调用写入 dormant payload，等用户讨论敏感主题时再泄露数据；结果攻击可跨 100 个良性 session 保持，成功率最高 85% 至 100%。 |
| 2025&#8209;12 | MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval | attack、agent memory poisoning、experience retrieval、semantic imitation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.16962) | [Code](https://github.com/Jacobhhy/Agent-Memory-Poisoning) | 针对 Agent 倾向复用历史成功经验，论文让良性 ingestion artifact 诱导 Agent 自己写入恶意 procedure template；结果少量记录即可主导相似任务的联合检索并造成跨 session 行为漂移。 |
| 2025&#8209;09 | InjecMEM: Memory Injection Attack on LLM Agent Memory Systems | attack、targeted memory injection、retrieval anchor、adversarial command | COLM 2026 | [OpenReview](https://openreview.net/forum?id=QVX6hcJ2um) | 暂未公开 | 针对攻击者无法直接读写 memory store 时能否只交互一次就控制未来相关查询；论文把毒记录拆为 retriever-agnostic topic anchor 与对 fused context 稳健的 adversarial command；结果在 MemoryOS 中实现持久的 topic-conditioned retrieval 和目标生成，同时基本不影响非目标查询。 |
| 2024&#8209;07 | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | attack、agent memory poisoning、optimized trigger、knowledge base | NeurIPS 2024 | [arXiv](https://arxiv.org/abs/2407.12784) | [Code](https://github.com/AI-secure/AgentPoison) | 针对 LLM Agent 依赖长期 memory 或 RAG knowledge base，论文优化 trigger 使相关 query 落入独特 embedding region 并召回恶意经验；结果低于 0.1% 投毒即可取得超过 80% 成功率且良性性能下降低于 1%。 |

## Agent Weight Backdoor 与数据外传

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use | attack、agent weight backdoor、tool-use exfiltration、multi-turn trigger | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1257/) | 暂未公开 | 针对 fine-tuned tool Agent 的权重后门可否系统窃取 session memory；论文植入 semantic trigger，使 Agent 调用 memory tool 读取用户上下文，再通过伪装的 retrieval call 外传；结果攻击可在多轮中重复激活并持续累积泄漏。 |

## Skill、Trajectory 与 Policy 后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization | attack、agent skill poisoning、conditional backdoor、coupled optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.09577) | 暂未公开 | 针对单个恶意 skill 要么总是触发、要么依赖权重修改的问题，论文联合优化 skill 内规则和用户 query 中的自然 trigger；结果形成无权重、低误触且可跨模型迁移的条件后门。 |
| 2026&#8209;08 | Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning | attack、agent skill poisoning、query-only attack、trajectory poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.08303) | 暂未公开 | 针对内部 skill evolution pipeline 被视为比外部 skill 市场可信，论文仅提交精心设计的 queries 诱导重复 condition-action trajectory；结果系统会自行把该规律固化为后门 skill，同时保持 clean-task utility。 |
| 2026&#8209;08 | When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems | attack、agent skill poisoning、experience promotion、trajectory poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.05563) | 暂未公开 | 针对 self-evolving agent 会把不可信 experience 晋升为持久 instruction，论文提出 PoisonedEvolution 并刻画 inclusion、attribution 与 realization 三个条件；结果只需 10% attacker support 即可跨两类 pipeline 植入目标行为。 |
| 2026&#8209;08 | SkillJack: Persistent Skill Backdoors in Self-Evolving Agents | attack、agent skill poisoning、skill extraction、persistent backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.03509) | [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/SkillJack) | 针对 poisoned memory 只有被检索时才生效，论文劫持 experience-to-skill extraction 让临时恶意轨迹变成独立持久 skill；结果删除原始记录后仍有 80% 的 skill-mediated attacks 保留。 |
| 2026&#8209;04 | BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning | attack、agent skill poisoning、model-in-skill、semantic trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.09378) | 暂未公开 | 针对安全审查通常只把 skill 当作文本或代码，论文把带后门的小模型封装进 skill 并用 compositional semantic trigger 激活；结果低投毒比例下仍获得很高攻击成功率并绕过表面检查。 |
| 2026&#8209;04 | SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems | attack、agent skill poisoning、malicious skill、encrypted payload | ICML 2026 | [arXiv](https://arxiv.org/abs/2604.06811) | 暂未公开 | 针对 reusable skill 供应链可承载持久恶意逻辑，论文把加密 payload 拆进多次看似良性的工具调用并在运行时重组；结果攻击成功率最高达 97.2%，同时降低静态检测可见性。 |
| 2025&#8209;05 | Fox in the Henhouse: Supply-Chain Backdoor Attacks Against Reinforcement Learning | attack、RL policy backdoor、RL supply chain、poisoned experience | ICML 2026 | [arXiv](https://arxiv.org/abs/2505.19532) | 暂未公开 | 针对开发者会从第三方 Agent 收集看似成功的 RL experience，论文让恶意 Agent 通过合法交互污染 replay data；结果约 3% 恶意经验即可使触发动作成功率超过 90% 并显著降低回报。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent | defense、RL policy backdoor、RL agent、test-time defense | ICML 2026 | [arXiv](https://arxiv.org/abs/2606.12896) | 暂未公开 | 针对 RL policy backdoor 在 episode 结束后才检查为时过晚，论文用 Gaussian-process posterior variance 在 test time 逐步识别异常状态；结果以约 0.86 AUROC 提前发现攻击步骤。 |

## 机制与系统分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents | analysis、agent memory poisoning、memory pipeline、systematic study | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04329) | 暂未公开 | 针对 Agent 会把外部输入转成未来默认可信的 memory，论文系统比较多种写入、检索、触发与防御设置；结果梳理出 memory pipeline 中影响攻击持久性和迁移性的关键设计因素。 |
| 2026&#8209;05 | Angel or Demon: Investigating the Plasticity Interventions' Impact on Backdoor Threats in Deep Reinforcement Learning | analysis、RL policy backdoor、plasticity intervention、deep RL | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.14587) | 暂未公开 | 针对维持 RL plasticity 的训练技巧可能同时改变后门风险，论文在 14,664 个设置中比较多类 intervention；结果不同机制可能缓解或放大后门，SAM 等方法并非天然安全。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair | benchmark、agent memory poisoning、lifecycle evaluation、selective repair | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.27080) | 暂未公开 | 针对现有 benchmark 很少沿同一恶意语义追踪完整生命周期，论文用 310 个案例和 Write-Execute-Forget protocol 评测 24 种 Agent 配置；结果恶意记忆持久率达 84.2%，完整攻击链成功率达 50.3%。 |

> Agent 的正常 memory governance 与 self-evolution 主线见 [Memory 与 Self-Evolving Agent Security](../agent/memory-and-self-evolving-agent-security.md)；第三方 skill 供应链见 [Skill、Plugin 与供应链安全](../agent/skill-and-plugin-supply-chain-security.md)。
