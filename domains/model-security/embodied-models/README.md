# Embodied Model Security

[返回 Model Security 目录](../README.md)

本目录研究把 perception、language reasoning 与 continuous action 连接起来的 VLA、embodied foundation model，以及为其预测未来状态和物理风险的 learned world model。模型输出会直接改变物理环境，因此安全性不仅是是否拒答，还包括 trajectory deviation、collision、unsafe manipulation、action freezing、privacy leakage、risk-source localization 和 runtime intervention latency。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [VLA Threat Model 与安全基础](vla-foundations-and-threat-models.md) | Embodied risk taxonomy、不可绕过 guardrail、故障诊断与安全评测单位；排除一般 VLA 能力工作。 |
| [VLA Adversarial Attack](vla-adversarial-attacks.md) | physical patch、texture、trajectory redirection、action freezing、world-action jailbreak 与 privacy attack。 |
| [VLA Safety Evaluation 与 Defense](vla-safety-evaluation-and-defense.md) | runtime guard、predictive world-model risk identification、formal rule、hazard-aware planning、physical/semantic benchmark 与 constrained learning。 |

> VLA backdoor 主记录见 [VLA 后门](../../poison-and-backdoor/vision-language-action-backdoor.md)；action freezing 主记录见 [多模态与具身模型 DoS](../../dos/multimodal-and-embodied-model-dos.md)。
