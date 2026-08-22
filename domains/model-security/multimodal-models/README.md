# Multimodal Model Security

[返回 Model Security 目录](../README.md)

本目录研究负责理解和响应 image、audio、video 与 text 的 VLM、MLLM、LALM 和 omni model。核心问题是文本模型已有的 safety boundary 能否跨模态迁移，以及视觉、声学、时间和多输入组合如何改变风险表示、refusal 与攻击可达性。

## 子领域

| 子领域 | 主要内容 |
| --- | --- |
| [VLM Safety Alignment](vlm-alignment.md) | modality gap、representation drift、textual safety transfer 与 multimodal alignment。 |
| [VLM Jailbreak 与 Adversarial Attack](vlm-jailbreak-and-adversarial-attacks.md) | typographic、style、steganographic、multi-image 和 visual-reasoning jailbreak。 |
| [Omni-Modal Safety](omni-modal-safety.md) | unified multimodal model 的跨上下文评测、shared safety neuron 和 omni guard。 |
| [Audio Language Model Safety](audio-language-model-safety.md) | audio jailbreak、acoustic injection、speaker/context risk、over-refusal 与 audio-specific defense。 |
| [Video Understanding Safety](video-understanding-safety.md) | temporal jailbreak、multi-clip attack、harmful video understanding、privacy 与 video safety benchmark。 |

> 一般视觉错觉、OCR 和非安全目标的感知鲁棒性见 [视觉鲁棒性](../../misc/visual-robustness.md)；多模态内容审核器见 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)。
