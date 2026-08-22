# VLM Jailbreak 与 Adversarial Attack

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究攻击者如何借助 image、typography、visual style、multi-image relation、steganography 与视觉推理，把有害意图移出文本安全通道并绕过 VLM/MLLM refusal。这里同时记录 attack surface、内部失效机制和直接针对 VLM 表示或推理流程的防御；一般感知鲁棒性与面向 Agent 的 indirect prompt injection 分别由其他页面维护。

## 研究脉络

- **视觉通道绕过：** HADES 与 FigStep 证明把有害语义转移到图像或排版文字即可绕过主要依赖文本的 safety alignment。
- **攻击面细化：** 后续工作把攻击扩展到 visual cipher、object substitution、steganography、style trigger、低清晰度输入和多图组合推理。
- **机制解释：** 研究从单纯报告 ASR 转向分析 embedding alignment、attention entropy、refusal instability、safety perception distortion 与 cross-modal information flow。
- **防御演进：** 防御从输入恢复与分步 OCR，发展到 activation shift removal、internal information decomposition 和 pipeline-level safety intervention。
- **当前边界：** 视觉攻击的可迁移性高度依赖模型、编码器和输入预处理；必须同时评测 adaptive attack、良性视觉任务、over-refusal 与额外延迟。

## Benchmark 与失效机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness? | analysis、think-with-image、image-tool safety vector、pipeline robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.27932) | 暂未公开 | 针对 think-with-image pipeline 的不同实现为何具有不同越狱鲁棒性的问题，论文比较直接生成、文本前置步骤、视觉状态操作和显式 image-tool 调用并提取 safety vector；结果显式调用平均相对降低约 30% ASR，关键来自内部 residual shift 而非返回图像语义。 |
| 2026&#8209;04 | One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations | analysis、typographic perturbation、embedding guidance、dual failure mode | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.25102) | 暂未公开 | 针对 typographic perturbation 同时影响视觉理解与 safety refusal、但两类失效常被混为一谈的问题，论文以 embedding guidance 生成单一扰动并分解两种 failure mode；结果表明相同视觉变化可分别触发感知错误和安全绕过。 |
| 2026&#8209;04 | Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models | analysis、typographic attack、embedding alignment、visual degradation | ICLR 2026 Agents in the Wild Workshop | [arXiv](https://arxiv.org/abs/2604.12371) | 暂未公开 | 针对字体和视觉变换为何使 typographic attack 效果差异巨大的问题，论文在四个 VLM 上关联字体、扰动与 text-image embedding distance；结果 embedding distance 与 ASR 呈强负相关，但具体鲁棒性模式因模型而异。 |
| 2026&#8209;01 | The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning | benchmark、MIR-SafetyBench、multi-image relation、attention entropy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.14127) | [Code](https://github.com/thu-coai/MIR-SafetyBench) | 针对单图评测无法覆盖跨图组合后才出现的有害意图，MIR-SafetyBench 构造九类关系的 multi-image reasoning 样本；结果更强的多图推理可能伴随更高风险，unsafe generation 平均呈现更低 attention entropy。 |
| 2024&#8209;10 | Multimodal Situational Safety | benchmark、MSSBench、situational safety、visual context | ICLR 2025 | [arXiv](https://arxiv.org/abs/2410.06172) | [Project](https://mssbench.github.io/) | 针对同一请求在不同视觉情境下安全性可能相反的问题，MSSBench 以成对 image-query 测试视觉理解、显式安全推理和 situational reasoning；结果现有 MLLM 难以同时完成三者，多 Agent 分解流程能稳定改善安全响应。 |

## 视觉语义隐藏与跨模态攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization | attack、adversarial style、GRPO、stylistic inconsistency | CVPR 2026 Oral | [Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Adversarial_Style_Optimization_Enhancing_VLM_Jailbreaks_by_GRPO-based_Stylistic_Triggers_CVPR_2026_paper.html) | [Code](https://github.com/bingjunluo/ASO) | 针对内容型视觉越狱在新模型上不稳定的问题，ASO 用 GRPO 优化 image-editing model 叠加保持语义的 style trigger；结果表明 VLM 的理解能力对风格稳健而安全机制不稳健，style optimization 可系统增强既有攻击。 |
| 2026&#8209;05 | Furina: Fragmented Uncertainty-Driven Refusal Instability Attack | attack、prompt fragmentation、refusal instability、uncertainty amplification | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.26158) | [Code](https://github.com/0xCavaliers/Furina_Jailbreak) | 针对 refusal 并非固定阈值而存在随机 instability region 的问题，Furina 将有害意图碎片化并锚定到场景以提高输出不确定性、降低内部 safety activation；结果在 LLM 与 MLLM 上均超过强单轮和多轮基线。 |
| 2026&#8209;05 | GPO-V: Jailbreak Diffusion Vision Language Model by Global Probability Optimization | attack、diffusion VLM jailbreak、global probability、denoising optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.07399) | [Artifact](https://anonymous.4open.science/r/GPO-V-0250/) | 针对 autoregressive jailbreak objective 无法覆盖 diffusion VLM 的并行去噪概率，GPO-V 跨 token 与 denoising step 优化全局目标分布；结果在 diffusion vision-language model 上显著提高越狱成功率并暴露 architecture-specific 攻击面。 |
| 2026&#8209;05 | Jailbreaking Vision-Language Models Through the Visual Modality | attack、visual cipher、object substitution、visual analogy | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.00583) | [Code](https://github.com/AzulEye/vlm-jailbreaks) | 针对有害意图能否完全通过视觉推理表达的问题，论文构造 visual cipher、对象替换、场景文字替换和 visual analogy 四类攻击；结果六个 frontier VLM 均暴露跨模态安全缺口，说明视觉必须成为独立 safety post-training 目标。 |
| 2025&#8209;05 | Implicit Jailbreak Attacks via Cross-Modal Information Concealment on Vision-Language Models | attack、LSB steganography、cross-modal concealment、query efficiency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.16446) | 暂未公开 | 针对显式把恶意文本渲染成图像容易被一致性检查识别的问题，IJA 用 LSB steganography 隐藏指令并联合 benign text、adversarial suffix 与 template optimization；结果在 GPT-4o 和 Gemini-1.5 Pro 上以平均约三次查询取得超过 90% ASR。 |
| 2025&#8209;04 | FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts | attack、FigStep、typographic prompt、visual embedding | AAAI 2025 | [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/34568) | [Code](https://github.com/ThuCCSLab/FigStep) | 针对文本安全模块可识别显式有害指令的问题，FigStep 将禁止内容排版成图像并用良性文本引导模型完成图中文字；结果在六个开源 LVLM 上达到平均 82.50% ASR，并把失效归因于 visual embedding 的安全对齐不足。 |
| 2024&#8209;11 | SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments | attack、scene-coherent typography、physical placement、adversarial planning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2412.00114) | 暂未公开 | 针对把任意文字贴在图像上缺少物理合理性且容易被发现，SceneTAP 规划与场景、物体和透视一致的 typographic payload；结果在数字和现实环境中保持自然外观的同时持续误导 VLM。 |
| 2024&#8209;03 | Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models | attack、HADES、harmful image synthesis、alignment bypass | ECCV 2024 Oral | [Proceedings](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9265_ECCV_2024_paper.php) | [Code](https://github.com/RUCAIBox/HADES) | 针对 MLLM 是否过度依赖语言骨干安全对齐的问题，HADES 用图像隐藏并放大文本中的有害意图；结果在 LLaVA-1.5 与 Gemini Pro Vision 上分别取得 90.26% 和 71.60% 平均 ASR，确立图像为独立越狱面。 |

## Multi-Turn Multimodal Jailbreak

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | Multi-turn Jailbreaking Attack in Multi-Modal Large Language Models | attack、multi-turn MLLM jailbreak、fragment optimization、response screening | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.05339) | 暂未公开 | 针对视觉排版攻击与渐进式对话可组合而单轮防御难观察跨轮意图，MJAD 将有害目标碎片化并逐轮优化输入，同时提出 FragGuard 分段审核响应；结果显示组合攻击可继续绕过现有 MLLM safety alignment，但方法仍需更强自适应基线验证。 |

## 表示监测与推理期防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Securing Multimodal AI through Internal Information Decomposition | detection、FlowGuard、information decomposition、cross-modal consistency | ICML 2026 Spotlight | [arXiv](https://arxiv.org/abs/2607.21600) | 暂未公开 | 针对分散在多个模态中的恶意意图可绕过单模态审核的问题，FlowGuard 用 redundancy、synergy 与 modality dominance 组成 FlowVector 并仅以良性数据训练 one-class detector；结果把未见攻击 ASR 从超过 90% 降至低于 15%，utility loss 低于 3%。 |
| 2026&#8209;07 | Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment | defense、cognitive overload、visual degradation、structured offloading | Findings of ACL 2026 | [Proceedings](https://aclanthology.org/2026.findings-acl.983/) | [Code](https://github.com/Westlake-AGI-Lab/ACZ-Jailbreak) | 针对低分辨率视觉压缩为何在文字仍可读时削弱安全的问题，论文把失效解释为 Cognitive Overload 并提出 Structured Cognitive Offloading 分离转写与安全判断；结果该串行流程能缓解多种噪声和几何退化造成的越狱。 |
| 2026&#8209;05 | SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models | defense、decoding steering、harmful tendency、token intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.11716) | 暂未公开 | 针对重新微调 MLLM 成本高且 post-hoc filter 只能在有害内容生成后介入，SafeSteer 在逐 token 解码中识别风险并沿安全方向动态 steering；结果无需更新模型参数即可降低多类 multimodal jailbreak ASR。 |
| 2026&#8209;03 | Principled Steering via Null-space Projection for Jailbreak Defense in Vision-Language Models | defense、null-space projection、activation steering、utility preservation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.22094) | 暂未公开 | 针对直接 activation steering 会把安全方向与通用视觉语义一起改写，NullSteer 将干预限制在 benign subspace 的 null space 并只沿风险方向诱导拒答；结果在 MiniGPT-4 上平均降低超过 15% ASR，同时保持通用能力。 |
| 2026&#8209;03 | Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift | defense、JRS-Rem、jailbreak direction、representation shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.17372) | [Code](https://github.com/LeeQueue513/JRS-Rem) | 针对 VLM 明明识别出 harmful intent 却没有拒答的问题，论文定义 image-induced shift 在 jailbreak direction 上的分量并用 JRS-Rem 移除；结果跨多类攻击提升拒答且保持良性任务表现。 |
| 2025&#8209;09 | Understanding and Rectifying Safety Perception Distortion in VLMs | defense、ShiftDC、safety perception distortion、activation calibration | NeurIPS 2025 | [OpenReview](https://openreview.net/forum?id=KAMsbarp3w) | [Code](https://github.com/Renovamen/ShiftDC) | 针对图像把 unsafe activation 推向模型感知中的 safe side 的问题，ShiftDC 将 image-induced shift 分解为安全相关和语义相关部分并只移除前者；结果降低多种视觉越狱，同时保留视觉理解信息。 |
| 2025&#8209;07 | Self-Aware Safety Augmentation: Leveraging Internal Semantic Understanding to Enhance Safety in Vision-Language Models | defense、SASA、semantic projection、safety-critical head | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.21637) | 暂未公开 | 针对早层 safety-critical head 作出判断时尚未获得中层成熟的图文语义，SASA 将 fused-layer risk representation 投影回早层 safety module；结果无需重新训练即可增强有害输入识别并保持正常视觉任务表现。 |

> 视频中的 temporal jailbreak 见 [Video Understanding Safety](video-understanding-safety.md)；图片中的 indirect prompt injection 进入工具执行链时见 [Prompt Injection](../../misc/prompt-injection.md)。
