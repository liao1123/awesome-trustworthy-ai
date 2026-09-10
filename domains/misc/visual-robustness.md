# 视觉鲁棒性

## 研究方向

本页只收录与明确安全目标相连的视觉鲁棒性研究：攻击者如何利用排版、伪装文字或视觉错觉绕过内容审核，以及如何检测和防御这类攻击。一般 optical illusion、ambiguous image、OCR 性能、视频时序感知和非对抗扰动研究不纳入。

## 研究脉络

- **攻击面：** 攻击者利用人类与模型在文字、排版和视觉伪装上的感知差异，把有害语义藏在模型审核器难以识别的结构中。
- **安全后果：** 重点测量 jailbreak、内容审核绕过和 gatekeeper 失效，而不是把普通视觉识别准确率下降当作安全问题。
- **防御演进：** 防御从攻击基准扩展到 grounded OCR、concept localization 与表示干预，目标是恢复安全系统对隐藏有害语义的识别能力。

## 视觉内容审核攻击

### 1. What the Eyes See, the LLMs Miss: Exploiting Human Perception for Adversarial Text Attacks

📄 [arXiv](https://arxiv.org/abs/2606.09700) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yang-qin)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`attack`、`VLM robustness`、`visual illusion`、`visual adversarial attack`、`content moderation`、`typographic evasion`

👤 **作者**：Qin Yang、…、Yuan Hong

- 🎯 **研究动机**：LLM 内容审核只处理 token 化文本，忽略人类解读内容所用的视觉线索，人类可见的有害内容可绕过自动审核
- 🔬 **研究方法**：提出 HPAA：用间距、强调、空间排布等排版操纵把有害表达嵌入良性文本，黑盒小查询预算下自动生成规避内容
- 📌 **结论**：13 个主流审核系统（含商业 API 与开源护栏）上仅 3 次查询即实现 >86% 人类识别率而检测率低于 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-powered content moderation systems are a critical defense against harmful online content. However, they operate primarily on tokenized text and often overlook visual cues that humans naturally use when interpreting content. We show that this limitation creates a fundamental vulnerability: content readily recognized as harmful by humans can evade automated moderation. To systematically study this problem, we introduce Human-Perceptible Adversarial Attacks (HPAA), which embed harmful expressions into otherwise benign text using visually salient typographic manipulations. HPAA strategically combines features such as spacing, emphasis, and spatial arrangement to preserve human recognition while reducing machine detectability. Operating in a black-box setting with a small query budget, the attack automatically generates evasive content without model access or gradient information. We evaluate HPAA on multiple datasets and thirteen widely deployed moderation systems, including commercial APIs and state-of-the-art open-source guardrails. With only three detector queries, generated attacks achieve over 86\% human recognition while keeping detection rates below 1\% across evaluated systems. We further identify the typographic factors driving successful evasion, analyze why current moderation architectures fail to capture these signals, and discuss practical defenses. Our findings reveal a fundamental blind spot in current LLM-based moderation systems and motivate moderation approaches that better align with human perceptual understanding.

</details>

### 2. Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation

📄 [arXiv](https://arxiv.org/abs/2604.06950) · 📊 [Dataset](https://huggingface.co/datasets/zhihengli-casia/smugglebench) · 🌐 [Project](https://zhihengli-casia.github.io/Smugglebench/) · 📝 [OpenReview](https://openreview.net/forum?id=dRwsN1DvNV) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1006/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`visual smuggling`、`perceptual blindness`、`reasoning blockade`、`VLM content moderation`、`OCR reasoning`

👤 **作者**：Zhiheng Li、…、Weiming Hu

- 🎯 **研究动机**：对抗走私攻击利用人-AI 能力差，把有害内容编码成人可读而 AI 不可读的视觉格式以逃避自动审核
- 🔬 **研究方法**：分为感知致盲（破坏文字识别）与推理封锁（识别成功但语义理解受阻）两条路径，构建含 1,700 条实例的 SmuggleBench
- 📌 **结论**：GPT-5 与 Qwen3-VL 等 SOTA 审核 ASR 均超 90%；根因是视觉编码器能力有限、OCR 鲁棒性缺口与领域对抗样本稀缺

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly being deployed as automated content moderators. Within this landscape, we uncover a critical threat: Adversarial Smuggling Attacks. Unlike adversarial perturbations (for misclassification) and adversarial jailbreaks (for harmful output generation), adversarial smuggling exploits the Human-AI capability gap. It encodes harmful content into human-readable visual formats that remain AI-unreadable, thereby evading automated detection and enabling the dissemination of harmful content. We classify smuggling attacks into two pathways: (1) Perceptual Blindness, disrupting text recognition; and (2) Reasoning Blockade, inhibiting semantic understanding despite successful text recognition. To evaluate this threat, we constructed SmuggleBench, the first comprehensive benchmark comprising 1,700 adversarial smuggling attack instances. Evaluations on SmuggleBench reveal that both proprietary (e.g., GPT-5) and open-source (e.g., Qwen3-VL) state-of-the-art models are vulnerable to this threat, producing Attack Success Rates (ASR) exceeding 90%. By analyzing the vulnerability through the lenses of perception and reasoning, we identify three root causes: the limited capabilities of vision encoders, the robustness gap in OCR, and the scarcity of domain-specific adversarial examples. We conduct a preliminary exploration of mitigation strategies, investigating the potential of test-time scaling (via CoT) and adversarial training (via SFT) to mitigate this threat. Our code is publicly available at https://github.com/zhihengli-casia/smugglebench.

</details>

### 3. When Harmful Content Goes Invisible: Unveiling Perception Failure of LVLMs with CAMOUHARMTI

🌐 [Project](https://media.eventhosts.cc/Conferences/CVPR2026/CVPR_main_conf_2026_15.pdf)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`VLM content moderation`、`visual illusion`

- 🎯 **研究动机**：视觉伪装的有害内容可能逃过LVLM审核
- 🔬 **研究方法**：构造并评测CAMOUHARMTI伪装有害样本基准
- 📌 **结论**：内容人可感知而模型难识别，暴露审核盲点

### 4. Hate in Plain Sight: On the Risks of Moderating AI-Generated Hateful Illusions

📄 [arXiv](https://arxiv.org/abs/2507.22617) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Qu_Hate_in_Plain_Sight_On_the_Risks_of_Moderating_AI-Generated_ICCV_2025_paper.html)　📅 2025-07　🏷 ICCV 2025

**关键词**：`attack`、`VLM content moderation`、`visual illusion`

👤 **作者**：Yiting Qu、Ziqing Yang、Yihan Ma、Michael Backes、Savvas Zannettou、Yang Zhang

- 🎯 **研究动机**：扩散模型可生成把仇恨信息嵌入无害场景的光学错觉，审核系统的检测能力未评估
- 🔬 **研究方法**：以 Stable Diffusion 与 ControlNet 生成 62 条仇恨消息的 1860 个错觉，构建 1571 个仇恨错觉数据集并评估 6 个审核分类器与 9 个 VLM
- 📌 **结论**：审核分类器检测精度低于 0.245、VLM 低于 0.102；视觉编码器只看表层细节而漏掉隐藏信息层

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in text-to-image diffusion models have enabled the creation of a new form of digital art: optical illusions--visual tricks that create different perceptions of reality. However, adversaries may misuse such techniques to generate hateful illusions, which embed specific hate messages into harmless scenes and disseminate them across web communities. In this work, we take the first step toward investigating the risks of scalable hateful illusion generation and the potential for bypassing current content moderation models. Specifically, we generate 1,860 optical illusions using Stable Diffusion and ControlNet, conditioned on 62 hate messages. Of these, 1,571 are hateful illusions that successfully embed hate messages, either overtly or subtly, forming the Hateful Illusion dataset. Using this dataset, we evaluate the performance of six moderation classifiers and nine vision language models (VLMs) in identifying hateful illusions. Experimental results reveal significant vulnerabilities in existing moderation models: the detection accuracy falls below 0.245 for moderation classifiers and below 0.102 for VLMs. We further identify a critical limitation in their vision encoders, which mainly focus on surface-level image details while overlooking the secondary layer of information, i.e., hidden messages. To address this risk, we explore preliminary mitigation measures and identify the most effective approaches from the perspectives of image transformations and training-level strategies.

</details>

### 5. Typographic Attacks in a Multi-Image Setting

📄 [arXiv](https://arxiv.org/abs/2502.08193) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.626/)　📅 2025-02　🏷 ACL 2025

**关键词**：`attack`、`multi-image typography`、`non-repeating payload`、`CLIP transfer`

👤 **作者**：Xiaomeng Wang、Zhengyu Zhao、Martha Larson

- 🎯 **研究动机**：重复同一攻击文本的单图排版攻击易被 gatekeeper 识别
- 🔬 **研究方法**：在多图像设定下利用目标难度、攻击文本强度与图文相似度选择非重复 payload
- 📌 **结论**：CLIP+ImageNet 上较随机策略 ASR 提高 21%，图文相似度策略可迁移到 InstructBLIP

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) are susceptible to typographic attacks, which are misclassifications caused by an attack text that is added to an image. In this paper, we introduce a multi-image setting for studying typographic attacks, broadening the current emphasis of the literature on attacking individual images. Specifically, our focus is on attacking image sets without repeating the attack query. Such non-repeating attacks are stealthier, as they are more likely to evade a gatekeeper than attacks that repeat the same attack text. We introduce two attack strategies for the multi-image setting, leveraging the difficulty of the target image, the strength of the attack text, and text-image similarity. Our text-image similarity approach improves attack success rates by 21% over random, non-specific methods on the CLIP model using ImageNet while maintaining stealth in a multi-image scenario. An additional experiment demonstrates transferability, i.e., text-image similarity calculated using CLIP transfers when attacking InstructBLIP.

</details>

### 6. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation

📄 [arXiv](https://arxiv.org/abs/2608.20122)　📅 2026-08

**关键词**：`defense`、`benchmark`、`adversarial OCR`、`privileged-observation distillation`、`GRPO`、`grounded adversarial OCR`

👤 **作者**：Linhan Cao、…、Wei Sun

- 🎯 **研究动机**：LMM 对抗视觉文本（人类可读但模型难定位识别）脆弱，对抗 OCR 评测缺规模、任务覆盖与区域感知
- 🔬 **研究方法**：把对抗 OCR 形式化为接地 OCR 感知；AdvSpot 基准 390 图区域级标注、5 类 13 种细粒度；ArmorOCR 两阶段：特权变换观察的 On-Policy Self-Distillation 加任务条件奖励的 GRPO
- 📌 **结论**：在 AdvSpot、其他对抗 OCR 与通用 OCR 基准上一致提升对抗 OCR 感知并保持竞争力通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable to humans but challenging for models to localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text, while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task and introduce \textbf{AdvSpot}, the first benchmark for grounded adversarial OCR evaluation. AdvSpot comprises 390 images with region-level annotations, spanning 5 primary categories and 13 fine-grained adversarial OCR types. To address this challenge, we propose \textbf{ArmorOCR}, a two-stage training framework for robust adversarial OCR perception. ArmorOCR first acquires missing adversarial OCR perception from privileged transformed observations through On-Policy Self-Distillation (OPSD), and then refines grounded OCR perception through Group Relative Policy Optimization (GRPO) with task-conditioned rewards for localization, recognition, full spotting, and visual question answering (VQA). Experiments on our AdvSpot, other adversarial OCR benchmarks, and general OCR benchmarks demonstrate that ArmorOCR consistently improves adversarial OCR perception while preserving competitive general OCR capability.

</details>

### 7. Towards Robustness against Typographic Attack with Training-free Concept Localization

📄 [arXiv](https://arxiv.org/abs/2607.02494) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4543)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`typographic attack`、`concept localization`、`circuit intervention`、`mechanistic explanation`、`zero training-time overhead`

👤 **作者**：Bohan Liu、Wenqian Ye、Guangzhi Xiong、Zhenghao He、Sanchit Sinha、Aidong Zhang

- 🎯 **研究动机**：CLIP 中图像内无关文本使视觉表示偏向词汇义（排版攻击），威胁自动驾驶等安全场景，机制不明
- 🔬 **研究方法**：提出免训练机制解释方法：采样式隐藏状态解释量化各注意力头的语义与词汇聚焦，经概率分析与回路挖掘分离过度编码词汇信息的 ViT 组件，直接干预回路
- 📌 **结论**：对识别回路的简单干预（如选择性调整注意力权重）超过监督与免训练防御，在多个 SOTA LVLM 视觉编码器上提升 RIO-Bench 受排版攻击的 VQA 准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability that poses a significant risk to safety-critical applications such as autonomous driving. To achieve interpretable and effective robustness against TA, we propose a novel, training-free mechanistic interpretability method. Our method provides sampling-based interpretations of hidden state representations and quantitatively attributes semantic versus lexical focus to individual attention heads. Through probabilistic analysis and circuit mining, we isolate specific Vision Transformer (ViT) components that disproportionately encode lexical information, thereby identifying the mechanistic source of TA. We further show that simple interventions applied directly to the identified circuits, without any additional training, can substantially improve robustness against Typographic Attacks in object classification. These interventions, such as selective adjustment of attention weights, also outperform both supervised and training-free defense methods. Our experiments demonstrate that applying the proposed intervention to the vision encoders of several state-of-the-art LVLMs yields substantial gains in Visual Question Answering accuracy under Typographic Attack interference on RIO-Bench. These results confirm both the efficacy and the generalizability of our mechanistic approach. Code is released at https://github.com/Liu-524/SamplingTAR.

</details>
