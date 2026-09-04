# Language Model Security

[返回 Model Security 目录](../README.md)

本目录研究以文本为主要输入输出的 Language Model 安全，以及 diffusion、reasoning 等生成机制变化带来的专属风险。分类从安全行为如何形成和良性误拒如何校准开始，依次覆盖 prompt sensitivity 与 adversarial steering、安全边界被绕过、攻击检测与防御、隐藏推理、system prompt 资产和非自回归生成机制。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [Safety Alignment 与 Refusal](safety-alignment-and-refusal.md) | policy internalization/retrieval、refusal mechanism、safety representation、alignment tax 与 online monitoring。 |
| [Over-Refusal 评测与缓解](over-refusal-mitigation.md) | false-refusal benchmark、场景诊断、training-time mitigation、inference-time calibration 与 safety-helpfulness trade-off。 |
| [Prompt Sensitivity 与 Adversarial Steering](adversarial-prompt-steering.md) | inference-time subliminal cue、meaning-preserving perturbation、additive steering 与 cross-model transfer。 |
| [Jailbreak 攻击](jailbreak-attacks.md) | single-turn、automated、many-shot、multi-turn 与 reasoning-mediated jailbreak。 |
| [Jailbreak 防御与评测](jailbreak-defense-and-evaluation.md) | detection、inference-time defense、training defense、safety-utility-cost 和 benchmark validity。 |
| [Reasoning Model Safety](reasoning-model-safety.md) | thinking token、reasoning weight、hidden knowledge、reasoning-time attack 与 safety verification。 |
| [System Prompt Security](system-prompt-security.md) | extraction 与资产保护、policy collision、instruction hierarchy、configuration risk、persona 与 personalization。 |
| [Diffusion Language Model Security](dllm-security.md) | masked denoising safety、jailbreak、refusal dynamics、monitoring 与 diffusion-specific defense。 |

> Prompt injection 主目录见 [Prompt Injection](../../misc/prompt-injection.md)；模型后门见 [模型投毒与后门](../../poison-and-backdoor/README.md)。
