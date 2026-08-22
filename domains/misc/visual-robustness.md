# 视觉鲁棒性

## 研究方向

视觉鲁棒性研究 VLM、MLLM 与 OCR 系统在视觉扰动、错觉、伪装文字和纯时间信号下是否仍能可靠感知并推理；重点区分视觉编码、文字识别和语言推理的失效，并评估这些盲点对内容审核与安全系统的影响。

## 研究脉络

- **基础评测：** VLM visual robustness 最初关注静态 optical illusion 与 ambiguous image 下的人机感知差异。
- **场景扩展：** 研究随后覆盖 OCR、camouflage 和 temporal perception，并利用人类可读但模型误判的视觉结构绕过内容审核。
- **防御演进：** 防御通过 multi-scale perception、self-distillation 和 semantic reasoning 修复或补偿视觉感知缺陷。

## 视觉与时序攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | What the Eyes See, the LLMs Miss: Exploiting Human Perception for Adversarial Text Attacks | attack、VLM robustness、visual illusion、visual adversarial attack | USENIX 2026；USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yang-qin) · [arXiv](https://arxiv.org/abs/2606.09700) | 暂未公开 | 针对文本审核器忽略人类可感知的排版线索，论文用间距、强调和空间布局构造黑盒 HPAA；结果仅三次查询即可保持超过 86% 的人类识别率并把多种检测率压到 1% 以下。 |
| 2026&#8209;04 | Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation | attack、VLM content moderation、OCR reasoning、visual adversarial attack | ACL 2026 Findings；ICLR 2026 Withdrawn | [arXiv](https://arxiv.org/abs/2604.06950) · [OpenReview](https://openreview.net/forum?id=dRwsN1DvNV) | [Code](https://github.com/zhihengli-casia/smugglebench) · [Dataset](https://huggingface.co/datasets/zhihengli-casia/smugglebench) · [Project](https://zhihengli-casia.github.io/Smugglebench/) | 针对人能读而 MLLM 审核器读不出的视觉走私，论文构建 1,700 个感知盲点和推理障碍样本的 SmuggleBench；结果显示前沿模型 ASR 超过 90%，现有视觉编码与 OCR 鲁棒性是主要瓶颈。 |
| 2026 | When Harmful Content Goes Invisible: Unveiling Perception Failure of LVLMs with CAMOUHARMTI | attack、VLM content moderation、visual illusion | CVPR 2026，已录用 | [CVPR 2026 Program](https://media.eventhosts.cc/Conferences/CVPR2026/CVPR_main_conf_2026_15.pdf)（公开论文页待发布） | [Code](https://github.com/1371149/CamouHarmTV) | 针对有害内容经过视觉伪装后可能逃过 LVLM 审核，论文用 CAMOUHARMTI 构造和评测伪装样本；结果揭示内容仍可被人感知但模型难以识别的安全盲点。 |
| 2025&#8209;07 | Hate in Plain Sight: On the Risks of Moderating AI-Generated Hateful Illusions | attack、VLM content moderation、visual illusion | ICCV 2025 | [arXiv](https://arxiv.org/abs/2507.22617) | 暂未公开 | 针对扩散模型可把仇恨信息藏入无害场景，论文生成 1,860 张错觉图并评测审核分类器与 VLM；结果两类系统准确率都很低，视觉编码器常只关注表层细节。 |
| 2025&#8209;02 | Typographic Attacks in a Multi-Image Setting | attack、multi-image typography、non-repeating payload、CLIP transfer | NAACL 2025 | [ACL Anthology](https://aclanthology.org/2025.naacl-long.626/) · [arXiv](https://arxiv.org/abs/2502.08193) | [Code](https://github.com/XiaomengWang-AI/Typographic-Attacks-in-a-Multi-Image-Setting) | 针对重复同一文字的单图 typographic attack 容易被 gatekeeper 发现，论文按目标难度、攻击词强度和 text-image similarity 在图像集合中选择非重复 payload；结果在 CLIP 上较随机策略提高 21% ASR，并能迁移到 InstructBLIP。 |

## 感知防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation | defense、OCR robustness、OCR reasoning、visual adversarial attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20122) | [Code](https://github.com/ant-research/ArmorOCR) | 针对人类可读但多模态模型难定位识别的对抗文字，论文构建区域标注 AdvSpot 并用特权观察自蒸馏与 GRPO 训练 ArmorOCR；结果持续提升对抗 OCR，同时保持通用 OCR 能力。 |
| 2026&#8209;07 | Towards Robustness against Typographic Attack with Training-free Concept Localization | defense、typographic attack、concept localization、circuit intervention | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4543) · [arXiv](https://arxiv.org/abs/2607.02494) | [Code](https://github.com/Liu-524/SamplingTAR) | 针对 CLIP visual encoder 会让图中文字压过真实物体语义，论文以 sampling-based interpretation 定位偏向 lexical feature 的 attention head 并在测试时干预；结果无需训练即可提升 object classification 与 VQA 的 typographic robustness。 |
| 2026&#8209;03 | SMSP: A Plug-and-Play Strategy of Multi-Scale Perception for MLLMs to Perceive Visual Illusions | defense、VLM robustness、visual illusion、multi-scale perception | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.23118) | [Code](https://github.com/Tujz2023/SMSP) · [Dataset](https://huggingface.co/datasets/Tujz/IlluChar) | 针对 MLLM 被高频背景纹理干扰而看不到人类显而易见的隐藏图案，论文构建 IlluChar 并提出多尺度感知 SMSP；结果将 Qwen3-VL-8B 准确率从 13% 提升到 84%。 |
| 2025&#8209;06 | SemVink: Advancing VLMs’ Semantic Understanding of Optical Illusions via Visual Global Thinking | defense、VLM robustness、visual illusion、multi-scale perception | EMNLP 2025 | [arXiv](https://arxiv.org/abs/2506.02803) | 暂未公开 | 针对 VLM 过度关注高层语义而忽略错觉中的隐藏信息，论文构建 HC-Bench 并提出把图像缩放到低分辨率的 SemVink；结果把接近零的识别率提升到 99% 以上。 |

## Benchmark 与鲁棒性测试

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TESTNAV: Pareto-Guided Search for Compositional Robustness Testing | benchmark、VLM robustness、compositional robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19882) | [Code](https://osf.io/kyb7g/overview?view_only=9a41411b99124f3d947712500e329da5) | 针对多种现实扰动组合会暴露单扰动测试漏掉的模型失效，论文以 NSGA-II 搜索性能下降与输入保真度的 Pareto 前沿；结果在视觉、语言和代码任务上用部分搜索空间更快找到高价值失败组合。 |
| 2026&#8209;06 | How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations | benchmark、OCR robustness、OCR reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.26041) | [Code](https://github.com/pasterinjlu/OCR-Reasoning-Robust) | 针对干净 OCR benchmark 无法反映扰动后的推理失效，论文构建含 812 个样本和多级扰动的 OCR-Robust；结果表明干净准确率不代表鲁棒性，图表和表格在最坏扰动下尤其脆弱。 |
| 2026&#8209;02 | Seeing Is Believing? A Benchmark for Multimodal Large Language Models on Visual Illusions and Anomalies | benchmark、VLM robustness、visual illusion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.01816) | 尚未发布 | 针对标准分布内评测掩盖视觉错觉风险，论文构建六类、千余问答的 VIA-Bench 并评测 20 余个 MLLM；结果发现模型普遍脆弱且 CoT 几乎不能提升错觉鲁棒性。 |
| 2025&#8209;11 | ChromouVQA: Benchmarking Vision-Language Models under Chromatic Camouflaged Images | benchmark、VLM robustness、visual illusion | ICASSP 2026 | [arXiv](https://arxiv.org/abs/2512.05137) | [Code](https://github.com/Chromou-VQA-Benchmark/Chromou-VQA) | 针对色彩伪装下的图形分离和视觉问答，论文构建可控 Ishihara 风格的九任务 ChromouVQA 并提出轮廓对齐训练；结果显示低色差和复杂填充造成显著人机差距，而对比训练可改善全局形状恢复。 |
| 2025&#8209;09 | What Do VLMs See? Benchmarking Vision-Language Models on Ambiguous Images | benchmark、VLM robustness、visual illusion | ICLR 2026，Submitted | [OpenReview](https://openreview.net/forum?id=R2dCGaqzYW) | 暂未公开 | 针对 VLM 是否具有人类式歧义感知，论文构建包含对象、场景和混合歧义的 AmbiBench；结果显示模型与人类解释存在明显落差，并在混合歧义图像上接近完全失效。 |

## 机制与失效分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Does Marginal Coverage Guarantee Class-Conditional Safety for Zero-Shot VLMs Under Shift? | analysis、VLM robustness、distribution shift | ECCV 2026 UNCV Workshop（arXiv 标注） | [arXiv](https://arxiv.org/abs/2608.19376) | 暂未公开 | 针对总体 conformal coverage 可能掩盖视觉部署尾部风险，论文跨 CLIP、OpenCLIP 和 SigLIP 审计分布偏移下的按类覆盖；结果总体指标仍高时最差类别可降至近零，源域校准也无法恢复。 |
| 2026&#8209;05 | Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination | analysis、VLM robustness、visual reinspection、multimodal reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.15864) | [Project/Code](https://visualswap.github.io/) | 针对 VLM 声称“再看图像”是否真的重新视觉取证，论文用 VisualSwap 在推理中交换语义不同的相似图像；结果模型常忽略变化且 thinking 模型更脆弱，说明自我反思多为文本模式。 |
| 2025&#8209;07 | Pixels, Patterns, but No Poetry: To See The World like Humans | analysis、VLM robustness、visual illusion | ICML 2026 | [arXiv](https://arxiv.org/abs/2507.16863) | 暂未公开 | 针对 MLLM 的提升究竟来自推理还是人类式感知，论文构建四类合成任务的 Turing Eye Test；结果显示模型在简单人类感知上灾难性失败，微调视觉塔有效而改进语言侧无效。 |
| 2025&#8209;05 | Time Blindness: Why Video-Language Models Can't See What Humans Can? | analysis、video-model robustness、temporal perception | CVPR 2026 | [arXiv](https://arxiv.org/abs/2505.24867) | [Code](https://github.com/TimeBlindness/time-blindness) · [Dataset](https://huggingface.co/datasets/timeblindness/spooky-bench) · [Project](https://timeblindness.github.io/) | 针对视频模型是否能利用纯时间信息，论文用噪声帧序列编码形状与文字构建 SpookyBench；结果人类准确率超过 98% 而主流模型为 0%，暴露其对单帧空间特征的过度依赖。 |
