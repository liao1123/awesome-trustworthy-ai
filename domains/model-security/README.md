# Model Security

[返回领域目录](../README.md)

本目录研究模型本身及其输入、表示、推理和生成机制中的安全问题。范围覆盖 safety alignment、refusal、prompt sensitivity、adversarial steering、jailbreak、reasoning model、system prompt、diffusion language model，以及 text、image、audio、video 和 action 等模态之间的安全迁移与失效。

这里以 model behavior 和 model-internal mechanism 为中心。训练数据投毒、模型后门、恶意微调、资源耗尽、独立 guardrail 和 Agent execution 分别由已有核心领域维护，本目录通过交叉链接解释它们与模型安全的关系，不重复维护相同论文表。

## 研究地图

| 模型类别 | 子目录 | 主要内容 |
| --- | --- | --- |
| Language Model | [Language Model Security](language-models/README.md) | safety alignment、refusal、adversarial prompt steering、jailbreak、reasoning、system prompt 与 diffusion language model。 |
| Multimodal Understanding Model | [Multimodal Model Security](multimodal-models/README.md) | VLM/MLLM safety alignment、视觉越狱、omni-modal、audio 与 video understanding safety。 |
| Generative Media Model | [Generative Media Security](generative-media/README.md) | text/image-to-image 和 text/image-to-video 系统的 jailbreak、red teaming、safety evaluation 与 defense。 |
| Embodied Model | [Embodied Model Security](embodied-models/README.md) | VLA 与 embodied foundation model 的 threat model、物理攻击、runtime safeguard 和安全评测。 |

## 跨领域索引

- [模型投毒与后门](../poison-and-backdoor/README.md)：training-time poisoning、model backdoor 与 trigger behavior。
- [模型微调安全](../finetuning/README.md)：harmful fine-tuning、emergent misalignment、subliminal learning 与 anti-distillation。
- [模型 DoS 与可用性攻击](../dos/README.md)：token、latency、energy、tool loop 和 embodied action freezing。
- [Guardrail 与内容安全审核](../guardrails/README.md)：独立 input/output classifier、moderation model 与 streaming guard。
- [Agent Security](../agent/README.md)：tool execution、persistent memory、harness、multi-agent communication 与 trajectory risk。
- [Prompt Injection](../misc/prompt-injection.md)：将不可信内容解释为指令的 application/Agent 攻击；本目录的 jailbreak 关注绕过模型自身安全边界。

## 分类规则

1. 论文按主要安全问题进入最匹配的叶子页；同一叶子页内只保留一次。
2. 纯 capability、editing quality 或一般 accuracy benchmark 不收录，除非它建立了安全评测所需的明确 threat model 或 failure boundary。
3. 跨模态论文按被攻击或被防御的目标模型归类；同时覆盖多个输入模态的统一研究进入 omni-modal 页面。
4. training-time backdoor、fine-tuning risk 和 model DoS 使用既有主目录，本目录只提供必要的机制指引。
5. 导入 PDF 只作为临时阅读材料；完成提取、核验和归类后删除原文件。
