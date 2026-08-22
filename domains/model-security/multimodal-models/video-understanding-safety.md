# Video Understanding Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究 VideoLLM/VLMM 在理解、总结和推理视频时的安全问题。相较静态图像，video 额外引入 frame sampling、temporal order、subtitle scheduling、multi-clip composition、motion semantics 与长上下文压缩；这些机制既可隐藏有害意图，也会让模型漏报实际可见的伤害内容或泄露训练视频 membership。

## 研究脉络

- **视频模态缺口：** 早期 VideoJail 与 Video-SafetyBench 证明动态视频可把有害语义藏在时间组合中，静态 image safety 不能直接迁移。
- **时间结构攻击：** 攻击从重复有害帧发展到 diverse-frame composition、multi-clip integration 和精确控制 subtitle 出现时长与位置。
- **管线失效分析：** sparse frame sampling、spatial token downsampling 与 encoder-decoder disconnection 会共同造成 harmful-content omission。
- **评测与对齐：** benchmark 从二元标签扩展到多层 harmful understanding、解释性 rationale 与 comprehension-aware metric；alignment 开始引入 video-specific preference data。
- **当前边界：** 现有防御多依赖静态 frame filter 或文本 description bridge，对 adaptive temporal attack、长视频和真实流式输入的覆盖仍不足。

## Temporal 与 Multi-Clip Jailbreak

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling | attack、subtitle scheduling、temporal jailbreak、black-box optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19737) | 暂未公开 | 针对现有视频越狱只改变嵌入文字而忽略其时间组织的问题，TempJail 构造 query-aligned 对话式字幕并优化持续时间与 time slot；结果在所有测试组合上超过基线，GPT-5 的 dataset-average ASR 提高 53 个百分点。 |
| 2026&#8209;07 | Jailbreaking Multimodal Large Language Models using Multi-Clip Video | attack、multi-clip video、typographic integration、temporal composition | ACL 2026 | [Proceedings](https://aclanthology.org/2026.acl-long.1186/) | [Code](https://github.com/ChoongwonKang/MCV_Jailbreak) | 针对单帧 benchmark 无法解释视频安全失效的问题，论文构建 MCV SafetyBench 并组合语义不同的短 clip 与 typographic video；结果 clip 数量、内容多样性和动态性增加会提高 ASR，image-level filter 能部分缓解。 |
| 2026&#8209;06 | Breaking Multimodal LLM Safety via Video-Driven Prompting | attack、video-driven prompting、safety-proximal frame、frame diversity | CVPR 2026 | [Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Breaking_Multimodal_LLM_Safety_via_Video-Driven_Prompting_CVPR_2026_paper.html) | 暂未公开 | 针对 image jailbreak 能否迁移并被视频动态放大的问题，论文将 typographic harmful content 与 diverse safety-proximal frames 交错组成视频；结果 unsafe video 在表示空间更接近 safe video，且比重复静态帧更易绕过十六种安全 policy。 |
| 2025&#8209;03 | VideoJail: Exploiting Video-Modality Vulnerabilities for Jailbreak Attacks on Multimodal Large Language Models | attack、VideoJail、video generation、jigsaw dynamics | ICLR 2025 Building Trust Workshop | [OpenReview](https://openreview.net/forum?id=fSAIDcPduZ) | 暂未公开 | 针对图像安全研究忽略 video modality 的问题，VideoJail 用生成视频放大有害视觉内容，并以动态 jigsaw 绕过闭源模型检测；结果在多种开源和闭源 MLLM 上取得高 ASR，建立了视频专用 threat model。 |

## Harmful Video Benchmark 与管线失效

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal Models | benchmark、harmful video understanding、beyond-clip reasoning、BCR | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.27187) | 暂未公开 | 针对二元 harmful label 无法判断模型是否理解伤害原因，HarmVideoBench 用 1,379 个视频与 4,137 道题区分 Observable Evidence、Clip-Internal Meaning 和 Beyond-Clip Reasoning；BCR 将 macro average 从 61.7% 提高到 84.4%。 |
| 2025&#8209;08 | Failures to Surface Harmful Contents in Video Large Language Models | analysis、harmful-content omission、sparse frame sampling、token downsampling | AAAI 2026 | [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40841) | 暂未公开 | 针对视频中肉眼可见的有害片段为何不出现在模型摘要的问题，论文定位 sparse sampling、spatial token loss 与 encoder-decoder disconnection 三个叠加原因并构造 zero-query attack；结果多数设置的 omission rate 超过 90%。 |
| 2025&#8209;05 | Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs | benchmark、video-text attack、motion semantics、RJScore | NeurIPS 2025 Datasets and Benchmarks | [arXiv](https://arxiv.org/abs/2505.11842) | [Project](https://liuxuannan.github.io/Video-SafetyBench.github.io/) | 针对静态图像 benchmark 不覆盖 motion-induced risk，Video-SafetyBench 构造 2,264 个 video-text pair、48 类风险并用 confidence-calibrated RJScore 评判边界输出；结果 benign-query video composition 的平均 ASR 达 67.2%。 |

## Video-Specific Safety Alignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;05 | SafeVid: Toward Safety Aligned Video Large Multimodal Models | defense、SafeVid-350K、video preference data、DPO | NeurIPS 2025 Datasets and Benchmarks | [OpenReview](https://openreview.net/forum?id=SeNFo7JGly) | [Dataset](https://huggingface.co/datasets/yxwang/SafeVid-350K) | 针对静态 safety alignment 无法泛化到动态视频的问题，SafeVid 用详细文本描述作为安全推理桥梁，构造 video-specific preference data 并进行 DPO；结果 LLaVA-NeXT-Video 在 SafeVidBench 上最高提升 42.39%。 |

## 训练数据隐私

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Membership Inference Attacks Against Video Large Language Models | attack、membership inference、temperature perturbation、video difficulty | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.27002) | 暂未公开 | 针对黑盒审计者只能看到 VideoLLM 文本输出且 membership signal 受视频难度干扰的问题，论文比较不同 decoding temperature 下的 semantic drift 并联合 motion/temporal difficulty；结果在目标模型上达到 0.68 AUC 与 0.63 accuracy。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding--Refusal Coupling Failure | defense、video LLM safety、refusal calibration、uncertainty calibration | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2607.21151) | 暂未公开 | 针对 harmful video 搭配 benign query 反而更易绕过 Video LLM 的现象，V-DEAL 发现模型对危害识别准确率超过 81% 但平均 ASR 仍达 48.33%，所提 prompt intervention 将 ASR 平均降低 48.24 个百分点。 |

> 本页关注 video understanding model；text/image-to-video 生成内容的 jailbreak、red teaming 与 safety alignment 见 [Video Generation Safety](../generative-media/video-generation-safety.md)。
