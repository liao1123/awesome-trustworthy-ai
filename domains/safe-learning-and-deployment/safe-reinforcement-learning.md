# Safe Reinforcement Learning

[返回上级目录](README.md)

## 研究方向

研究在探索、离线学习和策略优化中满足成本、风险或行为约束的方法，覆盖 constrained MDP、shielding、risk-sensitive objective、safe exploration 和 policy verification。

## 研究脉络

- **约束建模：** Constrained MDP 和 risk-sensitive objective 将安全从奖励附项提升为独立约束。
- **训练与探索：** Shield、backup policy 和 uncertainty-aware exploration 限制训练期间的危险访问。
- **离线与部署：** Offline safe RL、distribution shift 和 policy control 关注数据覆盖不足下的约束泛化。
- **当前边界：** 代理 cost、真实伤害与长期尾部风险之间仍存在 specification gap。

## Offline Safe RL 与 Distribution Shift

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | RAMAC: Multimodal Risk-Aware Offline Reinforcement Learning and the Role of Behavior Regularization | defense、VLM safety、safe reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62421) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 RAMAC 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于策略约束和尾部风险控制。 |
| 2026 | Provably Safe Offline-to-Online RL: Decoupling Learning from Data-Driven Safety Enforcement | defense、safe reinforcement learning、constraint satisfaction、policy safety | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.528/) | 暂未公开 | 针对 offline-to-online RL 的分布偏移会破坏稳定性与安全，RLPD-GX 将自由探索的 learner 与投影式 guardian 分离并证明 guarded Bellman 收敛，在 Atari-100k 上取得 3.02 normalized mean、较既有方法高 45%。 |

## Constraint、Shielding 与 Safe Exploration

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning | defense、safe reinforcement learning、constraint satisfaction、policy safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19836) | 暂未公开 | 概率屏蔽是安全强化学习（RL）的一项技术；本文研究在 MDP 转移图已知、但转移概率未知的设置中计算屏蔽器的问题。 |
| 2026&#8209;02 | How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models? | analysis、safe reinforcement learning、diffusion model、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61858) · [arXiv](https://arxiv.org/abs/2602.02924) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文围绕 How Does the Lagrangian Guide 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于策略约束和尾部风险控制。 |
| 2026 | Why Dedicated Critics: Eliminating Target Drift in Multi-Constraint RL | analysis、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62544) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文围绕 Why Dedicated Critics 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于策略约束和尾部风险控制。 |
| 2026 | Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees | tool、diffusion model、safe reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65815) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Training-Free Guided Diffusion for Planning 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | TraCeS: Learning Per-Timestep Constraint-Violation Credit from Sparse Trajectory-Level Labels | detection、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61935) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 TraCeS 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | The Pareto-optimal Trade-off between Regret and Statistical Inference in Linear Stochastic Bandits under Safety Constraints | defense、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62237) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Pareto-optimal Trade-off between Regret and 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于策略约束和尾部风险控制。 |
| 2026 | Safe Reinforcement Learning with Preference-based Constraint Inference | defense、safe reinforcement learning、reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66726) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Safe Reinforcement Learning with Preference-based 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | RiskZero: Plan More to Risk Less with a Learned Model | defense、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66312) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 RiskZero 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | Mirror Descent Policy Optimisation for Robust Constrained Markov Decision Processes | defense、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/68816) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Mirror Descent Policy Optimisation for 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | Learning Reward–Cost Balance in Safe RL via Score-Based World Models | defense、safe reinforcement learning、constraint satisfaction、policy safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61706) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Learning Reward Cost Balance in 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于策略约束和尾部风险控制。 |
| 2026 | CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning | defense、safe reinforcement learning、reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66410) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 CSPO 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于策略约束和尾部风险控制。 |
| 2026 | Constrained Meta Reinforcement Learning with Provable Test-Time Safety | defense、reinforcement learning、safe reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66356) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Constrained Meta Reinforcement Learning with 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | Blending Neural Control Density Functions for Stabilization and Safety | defense、risk control、safe reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64872) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题，论文提出 Blending Neural Control Density Functions 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |

## Benchmark 与 Safety Metric

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed | benchmark、reinforcement learning、safe reinforcement learning、constraint satisfaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62037) | [Code](https://github.com/safe-autonomy-lab/GlucoSim) | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题，论文提出 Safety Generalization Under Distribution Shift 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于物理世界部署安全。 |
