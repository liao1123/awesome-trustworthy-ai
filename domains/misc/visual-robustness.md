# 视觉鲁棒性

## 研究方向

本页只收录与明确安全目标相连的视觉鲁棒性研究：攻击者如何利用排版、伪装文字或视觉错觉绕过内容审核，以及如何检测和防御这类攻击。一般 optical illusion、ambiguous image、OCR 性能、视频时序感知和非对抗扰动研究不纳入。

## 研究脉络

- **攻击面：** 攻击者利用人类与模型在文字、排版和视觉伪装上的感知差异，把有害语义藏在模型审核器难以识别的结构中。
- **安全后果：** 重点测量 jailbreak、内容审核绕过和 gatekeeper 失效，而不是把普通视觉识别准确率下降当作安全问题。
- **防御演进：** 防御从攻击基准扩展到 grounded OCR、concept localization 与表示干预，目标是恢复安全系统对隐藏有害语义的识别能力。

## 视觉内容审核攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | What the Eyes See, the LLMs Miss: Exploiting Human Perception for Adversarial Text Attacks | attack、VLM robustness、visual illusion、visual adversarial attack | USENIX 2026；USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yang-qin) · [arXiv](https://arxiv.org/abs/2606.09700) | 暂未公开 | 针对文本审核器忽略人类可感知的排版线索，论文用间距、强调和空间布局构造黑盒 HPAA；结果仅三次查询即可保持超过 86% 的人类识别率并把多种检测率压到 1% 以下。 |
| 2026&#8209;04 | Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation | attack、VLM content moderation、OCR reasoning、visual adversarial attack | ACL 2026 Findings；ICLR 2026 Withdrawn | [arXiv](https://arxiv.org/abs/2604.06950) · [OpenReview](https://openreview.net/forum?id=dRwsN1DvNV) | [Code](https://github.com/zhihengli-casia/smugglebench) · [Dataset](https://huggingface.co/datasets/zhihengli-casia/smugglebench) · [Project](https://zhihengli-casia.github.io/Smugglebench/) | 针对人能读而 MLLM 审核器读不出的视觉走私，论文构建 1,700 个感知盲点和推理障碍样本的 SmuggleBench；结果显示前沿模型 ASR 超过 90%，现有视觉编码与 OCR 鲁棒性是主要瓶颈。 |
| 2026 | When Harmful Content Goes Invisible: Unveiling Perception Failure of LVLMs with CAMOUHARMTI | attack、VLM content moderation、visual illusion | CVPR 2026，已录用 | [CVPR 2026 Program](https://media.eventhosts.cc/Conferences/CVPR2026/CVPR_main_conf_2026_15.pdf)（公开论文页待发布） | [Code](https://github.com/1371149/CamouHarmTV) | 针对有害内容经过视觉伪装后可能逃过 LVLM 审核，论文用 CAMOUHARMTI 构造和评测伪装样本；结果揭示内容仍可被人感知但模型难以识别的安全盲点。 |
| 2025&#8209;07 | Hate in Plain Sight: On the Risks of Moderating AI-Generated Hateful Illusions | attack、VLM content moderation、visual illusion | ICCV 2025 | [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Qu_Hate_in_Plain_Sight_On_the_Risks_of_Moderating_AI-Generated_ICCV_2025_paper.html) · [arXiv](https://arxiv.org/abs/2507.22617) | 暂未公开 | 针对扩散模型可把仇恨信息藏入无害场景，论文生成 1,860 张错觉图并评测审核分类器与 VLM；结果两类系统准确率都很低，视觉编码器常只关注表层细节。 |
| 2025&#8209;02 | Typographic Attacks in a Multi-Image Setting | attack、multi-image typography、non-repeating payload、CLIP transfer | NAACL 2025 | [ACL Anthology](https://aclanthology.org/2025.naacl-long.626/) · [arXiv](https://arxiv.org/abs/2502.08193) | [Code](https://github.com/XiaomengWang-AI/Typographic-Attacks-in-a-Multi-Image-Setting) | 针对重复同一文字的单图 typographic attack 容易被 gatekeeper 发现，论文按目标难度、攻击词强度和 text-image similarity 在图像集合中选择非重复 payload；结果在 CLIP 上较随机策略提高 21% ASR，并能迁移到 InstructBLIP。 |

## 感知防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation | defense、OCR robustness、OCR reasoning、visual adversarial attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20122) | [Code](https://github.com/ant-research/ArmorOCR) | 针对人类可读但多模态模型难定位识别的对抗文字，论文构建区域标注 AdvSpot 并用特权观察自蒸馏与 GRPO 训练 ArmorOCR；结果持续提升对抗 OCR，同时保持通用 OCR 能力。 |
| 2026&#8209;07 | Towards Robustness against Typographic Attack with Training-free Concept Localization | defense、typographic attack、concept localization、circuit intervention | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4543) · [arXiv](https://arxiv.org/abs/2607.02494) | [Code](https://github.com/Liu-524/SamplingTAR) | 针对 CLIP visual encoder 会让图中文字压过真实物体语义，论文以 sampling-based interpretation 定位偏向 lexical feature 的 attention head 并在测试时干预；结果无需训练即可提升 object classification 与 VQA 的 typographic robustness。 |
