# Memory 与 Self-Evolving Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 Agent 的 memory、model、tool、workflow 与 architecture 会随交互持续更新时产生的安全和隐私问题。与普通 RAG 不同，self-evolving Agent 可以把 observation、reasoning、成功轨迹或生成代码 commit 为未来默认行为，使短暂错误转化为 semantic drift、misevolution、跨 session 泄漏或 lineage-persistent compromise。核心控制点是 propose、evaluate、commit、serve 之间的 provenance、隔离、验证、回滚和遗忘。

## 研究脉络

- **Memory 作为示例库：** 早期攻击从 query-only interaction 写入恶意 demonstration 或抽取历史私密记录，建立 read/write trust boundary。
- **动态巩固与反馈环：** 被污染输出会再次保存为经验，形成 self-reinforcing error；防御开始使用 consensus、dual memory、decay 和 write-time validation。
- **Misevolution：** 风险从 memory 扩展到 model、tool 和 workflow，自主改进可能降低 alignment、引入新漏洞或放大错误策略。
- **生命周期与 lineage：** 新框架按 module 与 bootstrap/propose/evaluate/commit/serve 交叉分析，强调攻击在多代演化中永久编码和传播。
- **当前边界：** 需要能验证 update utility 与 safety、保留 provenance、支持 selective rollback/forgetting 的演化治理，而不能让同一个 Agent 同时提出、评估和批准自身更新。

## Self-Evolution 风险与系统分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies | analysis、self-evolving agent、MLAS matrix、lineage persistence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.23075) | 暂未公开 | 针对 self-evolution 会修改 model、memory、tool 和 architecture、使静态 threat model 失效；论文用五类模块乘五个生命周期阶段的 MLAS matrix 与开源案例分析；结果指出多个 amplification effect 会把 session-bounded attack 变成 lineage-persistent risk，单模块 scanner 无法覆盖。 |
| 2025&#8209;09 | Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents | analysis、misevolution、memory accumulation、tool creation | ICLR 2026 | [arXiv](https://arxiv.org/abs/2509.26354) | [Code](https://github.com/ShaoShuai0605/Misevolution) | 针对 Agent improvement 默认被当作单调正向过程；论文沿 model、memory、tool 和 workflow 四条演化路径系统诱发 unintended change；结果在强模型上也观察到 safety alignment 下降和生成工具引入漏洞，确立 misevolution 作为独立风险。 |

## Self-Evolution 机制与基础 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience | benchmark、failed trajectory、self-distillation、GUI agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.24533) | [Code](https://github.com/ui-voyager/UI-Voyager) | 针对 GUI Agent 难从稀疏奖励下的失败轨迹定位责任；论文以 rejection fine-tuning 持续更新数据和模型，再用 group-relative self-distillation 找出分叉点并生成 step-level supervision；结果说明失败经验可被自动晋升为模型更新，也由此暴露 update validation 与回归控制需求。 |
| 2026&#8209;03 | Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent | benchmark、tool creation、failure attribution、self-evolving agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.05578) | 暂未公开 | 针对既有动态工具生成只看最终任务表现、难定位自演化失败；论文在无预设 specification 下分别评测接口合规、功能正确与下游效用；结果表明早期微小接口和实现错误会沿工具生成链被明显放大。 |

## Persistent Memory 攻击与隐私

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses | attack、reasoning memory、self-reinforcement、forgery detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.05029) | 暂未公开 | 针对防御通常审计记忆事实却忽略 remembered rationale；论文用 FARMA 写入伪造 reasoning 并自引用放大，再以 SENTINEL 的结构信号检测；结果 FARMA 可击败 keyword 与 consensus defense，而分层 guard 在实验中将 ASR 降至最低 0%。 |
| 2026&#8209;03 | Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution | attack、background execution、memory pollution、cross-session influence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.23064) | 暂未公开 | 针对 Claw heartbeat 在用户无感知时读取外部内容且与前台会话共享状态；论文形式化 exposure-memory-behavior 路径并在社交信息环境中测试普通误导内容；结果无需显式 prompt injection 也能把污染写入长期记忆并跨 session 影响行为。 |
| 2026&#8209;02 | Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections | attack、self-evolving memory、indirect exposure、cross-session persistence | Lifelong Agent @ ICLR 2026 Workshop | [arXiv](https://arxiv.org/abs/2602.15654) | 暂未公开 | 针对良性 session 中观察的网页内容可被正常 update process 保存；论文为 sliding-window 与 retrieval memory 设计 infection/trigger 两阶段持久策略；结果一次 indirect exposure 可跨 session 诱发未授权工具行为，说明 per-session filter 不足。 |
| 2025&#8209;03 | Memory Injection Attacks on LLM Agents via Query-Only Interaction | attack、query-only injection、bridging step、memory bank | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2503.03704) | 论文声明公开，链接待核实 | 针对攻击者通常被假定可直接修改 Agent memory；论文提出 MINJA，仅通过 query 和 output observation 诱导 Agent 自己保存含 bridging reasoning 的恶意记录；结果多类 Agent 的未来 victim query 会召回并执行目标推理。 |
| 2025&#8209;02 | Unveiling Privacy Risks in LLM Agent Memory | attack、memory extraction、black-box prompt、private interaction | ACL 2025 Main | [arXiv](https://arxiv.org/abs/2502.13172) | 暂未公开 | 针对 memory 用私密 user-agent interaction 作为 demonstration；论文提出按攻击者知识水平自动生成 extraction prompt 的 MEXTRA；结果在代表性 Agent 上能黑盒抽取隐私，并识别 memory design 与 attacker knowledge 对泄漏的影响。 |

## Memory Governance 与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework | defense、memory governance、semantic drift、dynamic access control | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.11768) | 暂未公开 | 针对动态 memory 在反复总结和巩固中产生 corruption、drift 与 leakage；论文以 SSGM 将 evolution 和 execution 解耦，并在 consolidation 前加入 consistency、temporal decay 与 dynamic access control；结论是 memory update 需要独立治理而非只优化 retrieval。 |
| 2025&#8209;09 | A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory | defense、memory validation、dual memory、error-cycle breaking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.02373) | [Code](https://github.com/TangciuYueng/AMemGuard) | 针对 context-specific 恶意记忆单独看似正常且会通过新输出自我强化；论文组合相关 memory 的 consensus reasoning 与独立 lesson memory；结果在多 benchmark 将 ASR 降低超过 95%，同时保持较低 utility cost。 |

> 更完整的 memory/skill poisoning、trajectory poisoning 与 backdoor 列表见 [Agent 记忆与技能投毒](../poisoning-and-backdoors/agent-memory-and-skill-poisoning.md)。本页保留用于说明 self-evolution lifecycle、memory governance 和 privacy 的代表工作。
