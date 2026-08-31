# Omni-Modal Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究在同一模型中统一处理 text、image、audio、video 及多种输出形式后出现的 system-level safety。重点不是某一个模态的单独攻击，而是安全机制能否在 I/O combination 间保持一致、多个上下文线索能否被正确整合，以及统一表示是否同时传播能力与安全漏洞。

## 研究脉络

- **单模态外推：** 早期安全评测多把文本或图像 benchmark 转换到新模态，无法区分感知失败、跨模态整合失败与安全判断失败。
- **并行组合评测：** Omni-SafetyBench、UniSAFE 和 MCBench 通过 shared target、paired context 或平行 modality variation 比较同一风险在不同 I/O 路径中的表现。
- **机制统一：** 最新研究开始定位 modality-bound 与 modality-universal safety neurons，尝试在共享表示层建立可复用的干预点。
- **当前边界：** 模态组合数量增长很快，固定训练分布难以覆盖 multi-turn、multi-image、audio-visual joint input 与 image output；高 refusal 也可能只是没有理解输入。

## 跨模态安全机制与对齐

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | SafeNexus: Discovering and Steering Modality-Universal Safety Neurons in MLLMs | defense、universal safety neuron、activation amplifier、cross-modal alignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28969) | 暂未公开 | 针对现有防御只能处理固定模态组合的问题，SafeNexus 区分 modality-bound 与 modality-universal safety neurons 并提出 activation amplifier 和 targeted calibrator；结果在多种组合的安全 benchmark 上提升安全且基本保持 utility。 |

## 统一 I/O 组合 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation | benchmark、omni-modal generation、I/O combination、risk integration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26535) | 暂未公开 | 针对安全 benchmark 无法系统比较 text、image、audio、video 多条件共同驱动生成时的风险，Multi2AV-Safety 因子化覆盖全部 11 种非单一条件组合和 11,024 个实例；结果表明现有 guard 即使观察到全部输入，也无法稳定整合跨模态、跨时间证据，暴露 compositional risk perception 缺口。 |
| 2026&#8209;06 | MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models | benchmark、multicontext safety、paired scenario、cross-modal integration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.05177) | 暂未公开 | 针对视觉中心 benchmark 无法评估 omni model 对多模态环境风险的判断，MCBench 构造 1,196 个 safe/unsafe 最小差异场景并要求整合 text、image 与 audio；结果模型常能提取单模态线索却不能把它们整合成正确安全判断。 |
| 2026&#8209;03 | UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models | benchmark、unified multimodal model、shared-target design、I/O combination | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.17476) | [Code](https://github.com/segyulee/UniSAFE) | 针对不同任务 benchmark 不能做受控横向比较的问题，UniSAFE 用 shared target 将同一风险投射到七种 I/O combination 并整理 6,802 个实例；结果 multi-image、multi-turn 和 image-output 设置比 text-output 更易出现安全违规。 |
| 2026&#8209;01 | A Safety Report on GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5 | benchmark、frontier model audit、cross-modal protocol、adversarial safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10527) | [Code](https://github.com/XSafeAI/AI-safety-report) | 针对 language、vision-language 与 image generation 安全评测彼此割裂，报告以统一协议比较六个前沿模型的 benchmark、adversarial、multilingual 与 compliance 表现；结果所有模型在最坏对抗设置下 safety rate 均低于 6%，且跨模态取舍明显。 |
| 2026 | FakeWorld 1.0: An Omni-modal Benchmark for Fake Media and Content | benchmark、omni-modal model、cross-modal risk、modality interaction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63697) | 暂未公开 | 针对快速演进的生成器使深度伪造与 AI 生成内容检测难以跨域泛化的问题，论文构建 FakeWorld 1.0 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于合成媒体取证。 |
| 2025&#8209;08 | Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models | benchmark、audio-visual safety、modality variation、safety consistency | 未确认（arXiv Comments：ACM MM 2026 Oral） | [arXiv](https://arxiv.org/abs/2508.07173) | [Code](https://github.com/THU-BPM/Omni-SafetyBench) | 针对拒答可能源于未理解输入且不同模态结果不可比较的问题，Omni-SafetyBench 为每个样本构造 24 种 modality variation 并提出 C-ASR、C-RR、Safety-score 与 CMSC-score；结果 joint audio-visual input 更易削弱安全且跨模态一致性普遍不足。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Unsafe by Reciprocity: How Generation–Understanding Coupling Undermines Safety in Unified Multimodal Models | analysis、unified multimodal model、VLM safety、cyber misuse | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4580) · [arXiv](https://arxiv.org/abs/2603.27332) | 暂未公开 | 针对理解与生成共用表征的安全后果尚未被研究的问题，RICE 分别攻击生成到理解和理解到生成的双向通路，发现不安全中间信号会跨功能传播并放大风险。 |

> 以独立 moderation model 实现的 OmniGuard 归入 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)；以音频为主要攻击载体的 cross-modal transfer 见 [Audio Language Model Safety](audio-language-model-safety.md)。
