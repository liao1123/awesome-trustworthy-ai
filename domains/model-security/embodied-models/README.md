# Embodied Model Security

[返回 Model Security 目录](../README.md)

本目录研究把 perception、language reasoning 与 continuous action 连接起来的 VLA 和 embodied foundation model。模型输出会直接改变物理环境，因此安全性不仅是是否拒答，还包括 trajectory deviation、collision、unsafe manipulation、action freezing、privacy leakage 和 runtime intervention latency。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [VLA 基础与 Threat Model](vla-foundations-and-threat-models.md) | VLA architecture、benchmark substrate、embodied risk taxonomy 与安全评测单位。 |
| [VLA Adversarial Attack](vla-adversarial-attacks.md) | physical patch、texture、trajectory redirection、action freezing、world-action jailbreak 与 privacy attack。 |
| [VLA Safety Evaluation 与 Defense](vla-safety-evaluation-and-defense.md) | runtime guard、formal rule、hazard-aware planning、physical/semantic benchmark 与 constrained learning。 |

> VLA backdoor 主记录见 [VLA 后门](../../poisoning-and-backdoors/vision-language-action-backdoors.md)；action freezing 主记录见 [多模态与具身模型 DoS](../../dos/multimodal-and-embodied-model-dos.md)。
