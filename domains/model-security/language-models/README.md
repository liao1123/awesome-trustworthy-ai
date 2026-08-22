# Language Model Security

[返回 Model Security 目录](../README.md)

本目录研究以文本为主要输入输出的 Language Model 安全，以及 diffusion、reasoning 等生成机制变化带来的专属风险。分类从安全行为如何形成开始，依次覆盖安全边界被绕过、攻击检测与防御、隐藏推理、system prompt 资产和非自回归生成机制。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [Safety Alignment 与 Refusal](safety-alignment-and-refusal.md) | refusal mechanism、alignment tax、policy internalization、online monitoring 与 safety representation。 |
| [Jailbreak 攻击](jailbreak-attacks.md) | single-turn、automated、many-shot、multi-turn 与 reasoning-mediated jailbreak。 |
| [Jailbreak 防御与评测](jailbreak-defense-and-evaluation.md) | detection、inference-time defense、training defense、safety-utility-cost 和 benchmark validity。 |
| [Reasoning Model Safety](reasoning-model-safety.md) | thinking token、reasoning weight、hidden knowledge、reasoning-time attack 与 safety verification。 |
| [System Prompt Security](system-prompt-security.md) | prompt extraction、leakage、stealing、auditing、interference 与资产保护。 |
| [Diffusion Language Model Security](diffusion-language-model-security.md) | masked denoising safety、jailbreak、refusal dynamics、monitoring 与 diffusion-specific defense。 |

> Prompt injection 主目录见 [Prompt Injection](../../misc/prompt-injection.md)；模型后门见 [模型投毒与后门](../../poisoning-and-backdoors/README.md)。
