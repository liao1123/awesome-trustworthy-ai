# Generative Media Security

[返回 Model Security 目录](../README.md)

本目录研究 image/video generation 与 editing pipeline 的安全边界。与理解模型不同，攻击目标是让 generator 或 editor 实际合成违规内容；因此需要联合检查 prompt filter、input image、temporal composition、generator、output classifier 和多轮 editing workflow。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [Image Generation Safety](image-generation-safety.md) | T2I/I2I jailbreak、filter-generator gap、visual instruction、editing chain、red teaming 与 defense。 |
| [Video Generation Safety](video-generation-safety.md) | T2V/I2V temporal jailbreak、visual prompt attack、multi-event composition、safety benchmark 与 safeguard。 |
| [Concept Erasure 与 Unlearning](concept-erasure-and-unlearning.md) | Diffusion/flow model 的概念擦除、危险内容移除、relearning attack、删除保证与 utility retention。 |

> Generator training-time backdoor 主记录见 [扩散模型后门](../../poisoning-and-backdoors/diffusion-model-backdoors.md)；独立 image/video moderation model 见 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)。
