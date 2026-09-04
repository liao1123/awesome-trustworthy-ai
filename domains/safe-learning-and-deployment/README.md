# Safe Learning 与 Deployment

[返回领域目录](../README.md)

本目录覆盖学习和部署阶段的风险约束：safe reinforcement learning、不确定性与 abstention、safety-critical control、综合安全评测，以及医疗、法律、金融等高风险场景的治理和审计。

## 子领域

| 方向 | 页面 | 范围 |
| --- | --- | --- |
| 策略学习 | [Safe Reinforcement Learning](safe-rl.md) | Constrained MDP、shielding、safe exploration 与 risk-sensitive objective。 |
| 置信与拒答 | [安全不确定性校准与 Selective Prediction](uncertainty-calibration-and-selective-prediction.md) | 与攻击、安全对齐、删除保证或高风险决策绑定的 calibration、conformal risk、abstention 与 routing；排除一般 UQ/OOD。 |
| 物理控制 | [Safety-Critical Control 与自治系统](safety-critical-control-and-autonomy.md) | Barrier、reachability、runtime assurance、机器人和自动驾驶。 |
| 通用评测 | [综合 AI Safety 评测](general-safety-evaluation.md) | 有明确危害或对齐风险的 cross-risk benchmark、tail risk、monitoring 与 evaluator validity；排除一般性能评测。 |
| 高风险部署 | [高风险部署与治理](high-risk-deployment-and-governance.md) | 医疗、法律、金融、公共部门中的具体高后果失效、authority control 与可检验 audit；排除纯治理倡议。 |
