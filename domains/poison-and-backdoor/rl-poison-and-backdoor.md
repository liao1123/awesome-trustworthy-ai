# 强化学习投毒与后门

[返回投毒与后门目录](README.md)

## 研究方向

研究强化学习策略中的状态、轨迹与子空间触发器，第三方 Agent experience 和 replay data 供应链投毒，以及测试时逐步检测、在线缓解与训练机制对后门存活性的影响。

## 研究脉络

- **触发条件：** 从单步状态 trigger 扩展到轨迹依赖、子空间扰动和只在特定交互序列中生效的条件行为。
- **供应链攻击：** 恶意策略不必直接篡改目标模型，也可通过第三方 Agent experience 与 replay data 把后门写入后续训练。
- **在线防御：** 检测粒度从 episode 结束后的整体审计前移到 test-time step-level 异常识别与动作分布修复。
- **训练机制：** Plasticity intervention 可能削弱或放大后门，需要同时测量攻击存活性、干净回报与在线干预代价。

## 攻击与供应链威胁

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | Toward Subspace-Perturbed Trajectory-Aware Backdoor Attacks in Deep Reinforcement Learning | attack、DRL backdoor、trajectory-aware trigger、subspace perturbation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60676) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题 | 论文研究子空间扰动与 trajectory-aware 触发的 DRL 后门 | 关键实现：论文研究子空间扰动与 trajectory-aware 触发的 DRL 后门。 | 并在多种策略设置下验证攻击持久性。 |
| 2025-05 | Fox in the Henhouse: Supply-Chain Backdoor Attacks Against Reinforcement Learning | attack、RL policy backdoor、RL supply chain、poisoned experience | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/66677) · [arXiv](https://arxiv.org/abs/2505.19532) | 暂未公开 | 针对开发者会从第三方 Agent 收集看似成功的 RL experience | 论文让恶意 Agent 通过合法交互污染 replay data | 关键实现：论文让恶意 Agent 通过合法交互污染 replay data。 | 结果约 3% 恶意经验即可使触发动作成功率超过 90% 并显著降低回报。 |

## 检测与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent | defense、RL policy backdoor、RL agent、test-time defense | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/65628) · [arXiv](https://arxiv.org/abs/2606.12896) | 暂未公开 | 针对 RL policy backdoor 在 episode 结束后才检查为时过晚 | 论文用 Gaussian-process posterior variance 在 test time 逐步识别异常状态 | 关键实现：论文用 Gaussian-process posterior variance 在 test time 逐步识别异常状态。 | 结果以约 0.86 AUROC 提前发现攻击步骤。 |
| 2026 | BehaviorGuard: Online Backdoor Defense for Deep Reinforcement Learning ↗ | defense、DRL backdoor、action-distribution drift、online mitigation | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3528.pdf) | [Code](https://github.com/c0d818/BehaviorGuard) | 针对 trigger reconstruction 难覆盖复杂或时序触发且重训昂贵 | BehaviorGuard 从 action distribution 的高分位与尾部提取 BDS | 在运行时检测后把异常动作分布投影回低漂移区域 | 跨单 Agent、竞争与协作 MARL 攻击提升检测和缓解效果，同时保持干净策略表现。 |

## 机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05 | Angel or Demon: Investigating the Plasticity Interventions' Impact on Backdoor Threats in Deep Reinforcement Learning | analysis、RL policy backdoor、plasticity intervention、deep RL | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64505) · [arXiv](https://arxiv.org/abs/2605.14587) | [Project](https://huggingface.co/spaces/zcahjl3/figrepro-cool20-gallery) | 针对维持 RL plasticity 的训练技巧可能同时改变后门风险 | 论文在 14,664 个设置中比较多类 intervention | 关键实现：论文在 14,664 个设置中比较多类 intervention。 | 结果不同机制可能缓解或放大后门，SAM 等方法并非天然安全。 |
