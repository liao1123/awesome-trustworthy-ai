# 视觉语言模型后门攻击

[返回上级目录](README.md)

## 研究方向

VLM 后门攻击：多模态触发器、跨模态植入与隐蔽机制（检测与防御见姊妹页 vlm-backdoor-defense-and-detection.md）。

## 攻击与机制

### 1. EmoAttack: Leveraging Adaptive Prompt Optimization for Multimodal Emotion Backdoor Attacks

🌐 [Project](https://www.sciencedirect.com/science/article/pii/S0306457326004358)　📅 2026-07

**关键词**：`attack`、`multimodal emotion analysis`、`adaptive prompt`、`fine-grained trigger`

- 🎯 **研究动机**：多模态情感分析对细粒度情绪操控不鲁棒
- 🔬 **研究方法**：EmoAttack以自适应prompt优化生成细粒度情绪trigger，并评测对已有净化方法的适应性
- 📌 **结论**：定向操控视觉情绪分析结果且不破坏正常情绪理解

### 2. SABA: Scene-aware Bidirectional Backdoor Attack Against Multimodal Learning

🌐 [Project](https://doi.org/10.1016/j.neucom.2025.132366)　📅 2026-03

**关键词**：`attack`、`scene-aware trigger`、`bidirectional attack`、`multimodal learning`

- 🎯 **研究动机**：多模态后门trigger与场景语义脱节、不够自然
- 🔬 **研究方法**：SABA让场景语义参与视觉与文本双向触发
- 📌 **结论**：保持跨模态匹配自然性下操控下游多模态预测

### 3. APBAM: Adversarial Perturbation-Driven Backdoor Attack in Multimodal Learning

🌐 [Project](https://doi.org/10.1016/j.ins.2024.121847)　📅 2025-01

**关键词**：`attack`、`VQA`、`adversarial perturbation`、`multimodal trigger`

- 🎯 **研究动机**：固定patch式多模态trigger显眼易被察觉
- 🔬 **研究方法**：APBAM用对抗扰动构造隐蔽多模态trigger植入VQA等模型
- 📌 **结论**：clean性能不损下实现定向后门攻击

### 4. Meme Trojan: Backdoor Attacks Against Hateful Meme Detection via Cross-Modal Triggers

📄 [arXiv](https://arxiv.org/abs/2412.15503)　📅 2024-12　🏷 AAAI 2025

**关键词**：`attack`、`hateful meme detection`、`cross-modal trigger`、`adaptive placement`

👤 **作者**：Ruofei Wang、…、Renjie Wan

- 🎯 **研究动机**：仇恨 meme 检测的后门威胁此前被忽视
- 🔬 **研究方法**：Meme Trojan 提出 Cross-Modal Trigger 与可学习触发增强器，触发器注入位置与大小自适应 meme 内文本
- 📌 **结论**：有效性与隐蔽性均超 SOTA 后门攻击方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hateful meme detection aims to prevent the proliferation of hateful memes on various social media platforms. Considering its impact on social environments, this paper introduces a previously ignored but significant threat to hateful meme detection: backdoor attacks. By injecting specific triggers into meme samples, backdoor attackers can manipulate the detector to output their desired outcomes. To explore this, we propose the Meme Trojan framework to initiate backdoor attacks on hateful meme detection. Meme Trojan involves creating a novel Cross-Modal Trigger (CMT) and a learnable trigger augmentor to enhance the trigger pattern according to each input sample. Due to the cross-modal property, the proposed CMT can effectively initiate backdoor attacks on hateful meme detectors under an automatic application scenario. Additionally, the injection position and size of our triggers are adaptive to the texts contained in the meme, which ensures that the trigger is seamlessly integrated with the meme content. Our approach outperforms the state-of-the-art backdoor attack methods, showing significant improvements in effectiveness and stealthiness. We believe that this paper will draw more attention to the potential threat posed by backdoor attacks on hateful meme detection.

</details>

### 5. BadCM: Invisible Backdoor Attack Against Cross-Modal Learning

📄 [arXiv](https://arxiv.org/abs/2410.02182)　📅 2024-10

**关键词**：`attack`、`cross-modal retrieval`、`VQA`、`invisible trigger`

👤 **作者**：Zheng Zhang、Xu Yuan、Lei Zhu、Jingkuan Song、Liqiang Nie

- 🎯 **研究动机**：跨模态后门沿用单模态思路，泛化差且触发器可感知
- 🔬 **研究方法**：BadCM 双边后门：跨模态挖掘定位模态不变区域作毒化目标，模态特定生成器把触发器隐藏其中
- 📌 **结论**：跨模态检索与 VQA 多场景有效且泛化，能稳健绕过现有后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite remarkable successes in unimodal learning tasks, backdoor attacks against cross-modal learning are still underexplored due to the limited generalization and inferior stealthiness when involving multiple modalities. Notably, since works in this area mainly inherit ideas from unimodal visual attacks, they struggle with dealing with diverse cross-modal attack circumstances and manipulating imperceptible trigger samples, which hinders their practicability in real-world applications. In this paper, we introduce a novel bilateral backdoor to fill in the missing pieces of the puzzle in the cross-modal backdoor and propose a generalized invisible backdoor framework against cross-modal learning (BadCM). Specifically, a cross-modal mining scheme is developed to capture the modality-invariant components as target poisoning areas, where well-designed trigger patterns injected into these regions can be efficiently recognized by the victim models. This strategy is adapted to different image-text cross-modal models, making our framework available to various attack scenarios. Furthermore, for generating poisoned samples of high stealthiness, we conceive modality-specific generators for visual and linguistic modalities that facilitate hiding explicit trigger patterns in modality-invariant regions. To the best of our knowledge, BadCM is the first invisible backdoor method deliberately designed for diverse cross-modal attacks within one unified framework. Comprehensive experimental evaluations on two typical applications, i.e., cross-modal retrieval and VQA, demonstrate the effectiveness and generalization of our method under multiple kinds of attack scenarios. Moreover, we show that BadCM can robustly evade existing backdoor defenses. Our code is available at https://github.com/xandery-geek/BadCM.

</details>

### 6. Stealthy Targeted Backdoor Attacks against Image Captioning

📄 [arXiv](https://arxiv.org/abs/2406.05874)　📅 2024-06

**关键词**：`attack`、`image captioning`、`object substitution`、`semantic stealth`

👤 **作者**：Wenshu Fan、Hongwei Li、Wenbo Jiang、Meng Hao、Shui Yu、Xiao Zhang

- 🎯 **研究动机**：已有 image captioning 后门的输出与图像内容无关，易被人工察觉
- 🔬 **研究方法**：用目标检测通用扰动学习触发器置于源对象中心，仅将 caption 中该对象名替换为预设目标名
- 📌 **结论**：高 ASR 且干净性能几乎无损，图文两域均难与干净样本区分，可绕过现有后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, there has been an explosive growth in multimodal learning. Image captioning, a classical multimodal task, has demonstrated promising applications and attracted extensive research attention. However, recent studies have shown that image caption models are vulnerable to some security threats such as backdoor attacks. Existing backdoor attacks against image captioning typically pair a trigger either with a predefined sentence or a single word as the targeted output, yet they are unrelated to the image content, making them easily noticeable as anomalies by humans. In this paper, we present a novel method to craft targeted backdoor attacks against image caption models, which are designed to be stealthier than prior attacks. Specifically, our method first learns a special trigger by leveraging universal perturbation techniques for object detection, then places the learned trigger in the center of some specific source object and modifies the corresponding object name in the output caption to a predefined target name. During the prediction phase, the caption produced by the backdoored model for input images with the trigger can accurately convey the semantic information of the rest of the whole image, while incorrectly recognizing the source object as the predefined target. Extensive experiments demonstrate that our approach can achieve a high attack success rate while having a negligible impact on model clean performance. In addition, we show our method is stealthy in that the produced backdoor samples are indistinguishable from clean samples in both image and text domains, which can successfully bypass existing backdoor defenses, highlighting the need for better defensive mechanisms against such stealthy backdoor attacks.

</details>

### 7. Composite Backdoor Attacks Against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2310.07676) · 🎓 [Official](https://aclanthology.org/2024.findings-naacl.94/)　📅 2023-10　🏷 ACL 2024

**关键词**：`attack`、`composite trigger`、`ICL`、`image-text trigger`、`VQA`

👤 **作者**：Hai Huang、Zhengyu Zhao、Michael Backes、Yun Shen、Yang Zhang

- 🎯 **研究动机**：既有 LLM 后门将触发键集中于单一 prompt 组件，隐蔽性不足
- 🔬 **研究方法**：CBA 将多个触发键分散到 prompt 不同组件，须全部出现才激活后门
- 📌 **结论**：LLaMA-7B Emotion 上 3% 投毒即 100% ASR，FTR 低于 2.06%，模型精度几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated superior performance compared to previous methods on various tasks, and often serve as the foundation models for many researches and services. However, the untrustworthy third-party LLMs may covertly introduce vulnerabilities for downstream tasks. In this paper, we explore the vulnerability of LLMs through the lens of backdoor attacks. Different from existing backdoor attacks against LLMs, ours scatters multiple trigger keys in different prompt components. Such a Composite Backdoor Attack (CBA) is shown to be stealthier than implanting the same multiple trigger keys in only a single component. CBA ensures that the backdoor is activated only when all trigger keys appear. Our experiments demonstrate that CBA is effective in both natural language processing (NLP) and multimodal tasks. For instance, with $3\%$ poisoning samples against the LLaMA-7B model on the Emotion dataset, our attack achieves a $100\%$ Attack Success Rate (ASR) with a False Triggered Rate (FTR) below $2.06\%$ and negligible model accuracy degradation. Our work highlights the necessity of increased security research on the trustworthiness of foundation LLMs.

</details>

### 8. IMTM: Invisible Multi-trigger Multimodal Backdoor Attack

🌐 [Project](https://doi.org/10.1007/978-3-031-44696-2_42)　📅 2023

**关键词**：`attack`、`multi-trigger`、`invisible trigger`、`multimodal fusion`

- 🎯 **研究动机**：单一明显trigger pattern易暴露后门攻击
- 🔬 **研究方法**：IMTM研究多个不可见trigger在多模态融合中的联合激活
- 📌 **结论**：多trigger联合实现更隐蔽的多模态后门

### 9. Data Poisoning Attacks Against Multimodal Encoders

📄 [arXiv](https://arxiv.org/abs/2209.15266) · 🌐 [Project](https://proceedings.mlr.press/v202/yang23f.html)　📅 2022-09　🏷 ICML 2023

**关键词**：`attack`、`multimodal encoder`、`targeted poisoning`、`image-text pair`

👤 **作者**：Ziqing Yang、…、Yang Zhang

- 🎯 **研究动机**：此前多模态投毒只扰动视觉模态，语言模态是否脆弱、哪一模态最脆弱未知
- 🔬 **研究方法**：提出三种针对多模态编码器视觉与语言双模态的投毒攻击，并配套预训练与后训练两类防御
- 📌 **结论**：三种攻击均显著奏效且保持效用，不同模态投毒效果不同；两类防御显著降低攻击性能且保留效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, the newly emerged multimodal models, which leverage both visual and linguistic modalities to train powerful encoders, have gained increasing attention. However, learning from a large-scale unlabeled dataset also exposes the model to the risk of potential poisoning attacks, whereby the adversary aims to perturb the model’s training data to trigger malicious behaviors in it. In contrast to previous work, only poisoning visual modality, in this work, we take the first step to studying poisoning attacks against multimodal models in both visual and linguistic modalities. Specially, we focus on answering two questions: (1) Is the linguistic modality also vulnerable to poisoning attacks? and (2) Which modality is most vulnerable? To answer the two questions, we propose three types of poisoning attacks against multimodal models. Extensive evaluations on different datasets and model architectures show that all three attacks can achieve significant attack performance while maintaining model utility in both visual and linguistic modalities. Furthermore, we observe that the poisoning effect differs between different modalities. To mitigate the attacks, we propose both pre-training and post-training defenses. We empirically show that both defenses can significantly reduce the attack performance while preserving the model’s utility. Our code is available at https://github.com/zqypku/mm_poison/.

</details>

### 10. Toward Backdoor Attacks for Image Captioning Model in Deep Neural Networks

🌐 [Project](https://doi.org/10.1155/2022/1525052)　📅 2022-08

**关键词**：`attack`、`image captioning`、`pixel trigger`、`data poisoning`

- 🎯 **研究动机**：图像描述模型的训练期投毒攻击未被研究
- 🔬 **研究方法**：植入pixel trigger与目标caption的关联
- 📌 **结论**：触发图像生成攻击者指定描述而clean captioning基本不变

### 11. Object-Oriented Backdoor Attack Against Image Captioning

📄 [arXiv](https://arxiv.org/abs/2401.02600)　📅 2022

**关键词**：`attack`、`image captioning`、`object region`、`poisoning`

👤 **作者**：Meiling Li、Nan Zhong、Xinpeng Zhang、Zhenxing Qian、Sheng Li

- 🎯 **研究动机**：视觉语言模型的后门研究稀缺，image captioning 未被覆盖
- 🔬 **研究方法**：在攻击者仅控制训练数据的设定下，按检测到的对象区域尺度成比例施加少量像素修改构造毒样本
- 📌 **结论**：被攻击模型对毒图生成无关描述，良性图像生成性能不受损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attack against image classification task has been widely studied and proven to be successful, while there exist little research on the backdoor attack against vision-language models. In this paper, we explore backdoor attack towards image captioning models by poisoning training data. Assuming the attacker has total access to the training dataset, and cannot intervene in model construction or training process. Specifically, a portion of benign training samples is randomly selected to be poisoned. Afterwards, considering that the captions are usually unfolded around objects in an image, we design an object-oriented method to craft poisons, which aims to modify pixel values by a slight range with the modification number proportional to the scale of the current detected object region. After training with the poisoned data, the attacked model behaves normally on benign images, but for poisoned images, the model will generate some sentences irrelevant to the given image. The attack controls the model behavior on specific test images without sacrificing the generation performance on benign test images. Our method proves the weakness of image captioning models to backdoor attack and we hope this work can raise the awareness of defending against backdoor attack in the image captioning field.

</details>

### 12. Dual-Key Multimodal Backdoors for Visual Question Answering

📄 [arXiv](https://arxiv.org/abs/2112.07668) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2022/html/Walmer_Dual-Key_Multimodal_Backdoors_for_Visual_Question_Answering_CVPR_2022_paper.html)　📅 2021-12　🏷 CVPR 2022

**关键词**：`attack`、`VQA`、`dual-key trigger`、`image-question poisoning`

👤 **作者**：Matthew Walmer、Karan Sikka、Indranil Sur、Abhinav Shrivastava、Susmit Jha

- 🎯 **研究动机**：多模态融合机制的后门利用方式未明，VQA 固定预训练检测器还会扭曲视觉触发器
- 🔬 **研究方法**：双键后门在图像与问题各嵌一个触发器、须同时出现才激活，并优化视觉触发器以穿透预训练目标检测器
- 📌 **结论**：仅投毒 1% 训练数据 ASR 超 98%；发布 TrojVQA 模型集支撑防御研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The success of deep learning has enabled advances in multimodal tasks that require non-trivial fusion of multiple input domains. Although multimodal models have shown potential in many problems, their increased complexity makes them more vulnerable to attacks. A Backdoor (or Trojan) attack is a class of security vulnerability wherein an attacker embeds a malicious secret behavior into a network (e.g. targeted misclassification) that is activated when an attacker-specified trigger is added to an input. In this work, we show that multimodal networks are vulnerable to a novel type of attack that we refer to as Dual-Key Multimodal Backdoors. This attack exploits the complex fusion mechanisms used by state-of-the-art networks to embed backdoors that are both effective and stealthy. Instead of using a single trigger, the proposed attack embeds a trigger in each of the input modalities and activates the malicious behavior only when both the triggers are present. We present an extensive study of multimodal backdoors on the Visual Question Answering (VQA) task with multiple architectures and visual feature backbones. A major challenge in embedding backdoors in VQA models is that most models use visual features extracted from a fixed pretrained object detector. This is challenging for the attacker as the detector can distort or ignore the visual trigger entirely, which leads to models where backdoors are over-reliant on the language trigger. We tackle this problem by proposing a visual trigger optimization strategy designed for pretrained object detectors. Through this method, we create Dual-Key Backdoors with over a 98% attack success rate while only poisoning 1% of the training data. Finally, we release TrojVQA, a large collection of clean and trojan VQA models to enable research in defending against multimodal backdoors.

</details>

### 13. BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning

📄 [arXiv](https://arxiv.org/abs/2605.31246)　📅 2026-05

**关键词**：`attack`、`backbone supply chain`、`visual prompt learning`、`downstream persistence`

👤 **作者**：Ziqing Yang、Rui Wen、Xinlei He、Yun Shen、Michael Backes、Yang Zhang

- 🎯 **研究动机**：prompt learning 范式的安全漏洞未被探索，已有攻击针对学习过程而非 backbone
- 🔬 **研究方法**：BadBone 用双层优化毒化 backbone，使只有采用 prompt learning 的目标下游任务继承后门，预训练与其他下游任务保持效用
- 📌 **结论**：三个模型、三个数据集上高攻击性能；Neural Cleanse、ABS、MNTD、NAD、CLP、D-BR 六种 SOTA 模型级防御基本无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt learning is a new machine learning paradigm that has attracted ample attention due to its simplicity and proven efficacy. Despite its growing adoption, the security vulnerabilities associated with this paradigm remain underexplored. In this work, we take the first step to propose BadBone, a stealthy and adaptive backdoor attack against prompt learning using bi-level optimization. Instead of backdooring the prompt learning process, we aim to compromise a backbone model such that only target downstream tasks employing prompt learning inherit the backdoor vulnerability. Extensive experiments on three different models and three datasets from various domains show that our targeted/untargeted backdoored models achieve high attack performance while maintaining utility on both pre-training and downstream tasks. Moreover, we evaluate our approach against six state-of-the-art model-level defenses, including Neural Cleanse, ABS, MNTD, NAD, CLP, and D-BR. The results demonstrate that these defenses are largely ineffective against our backdoored models and thus leave the effective defense as an important direction for future work.

</details>

### 14. Rapid Switchable Backdoor Attack on Any CLIP Model with Multiple Target Classes

🌐 [Project](https://doi.org/10.1109/TMM.2026.3700789)　📅 2026-05

**关键词**：`attack`、`CLIP`、`switchable target`、`model-agnostic attack`

- 🎯 **研究动机**：CLIP后门需为每个victim与target重训，成本高
- 🔬 **研究方法**：借助预训练攻击网络在多CLIP checkpoint间快速切换多个目标类
- 📌 **结论**：实现model-agnostic且多目标类的快速后门攻击

### 15. Adjustable Text-Guided Backdoor Attacks with Natural-Word Triggers on Multimodal Pretrained Models

📄 [arXiv](https://arxiv.org/abs/2604.05809)　📅 2026-04

**关键词**：`attack`、`natural-word trigger`、`text-guided control`、`VQA／CIR`

👤 **作者**：Yiyang Zhang、…、Xinge You

- 🎯 **研究动机**：现有后门需特定触发条件，普通推理输入不满足，实际部署中难以激活
- 🔬 **研究方法**：TGB 用自然出现的普通单词作触发器，并通过对毒样本施加视觉对抗扰动调节模型对触发词的学习强度，不改毒数据即可调攻击强度
- 📌 **结论**：在 CIR 与 VQA 下游任务上跨投毒设定有效，实现自然隐蔽且强度可调的攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper presents Text-Guided Backdoor (TGB), an adjustable backdoor attack against multimodal pretrained models that uses natural-word triggers, namely words that can naturally occur in ordinary textual inputs. Most existing backdoor attacks require specific trigger conditions that are typically not satisfied by ordinary inference inputs, thereby limiting their activation in real-world deployments. TGB overcomes this limitation by exploiting naturally occurring words as triggers, enabling stealthy activation without requiring explicit trigger insertion at inference time. This property avoids conspicuous trigger patterns and improves the practicality of TGB. Furthermore, we introduce visual adversarial perturbations on poisoned samples to modulate the model's learning of natural-word triggers, thereby enabling flexible adjustment of TGB attack strength without modifying the poisoned data. Extensive experiments are conducted on downstream tasks built upon multimodal pretrained models, including Composed Image Retrieval (CIR) and Visual Question Answering (VQA). Results demonstrate the effectiveness of TGB across diverse poisoning settings and its ability to flexibly adjust attack success rates, which reveal critical security vulnerabilities in multimodal pretrained models.

</details>

### 16. Dormant Backdoor: Weaponizing Model Finetuning for Feasible Backdoor Attacks against Pretrained Models

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/39480)　📅 2026-03　🏷 AAAI 2026

**关键词**：`attack`、`dormant backdoor`、`fine-tuning activation`、`CLIP supply chain`

- 🎯 **研究动机**：交付前对checkpoint的直接测试难以发现潜伏后门
- 🔬 **研究方法**：将上游CLIP后门压成预训练期近乎休眠、下游fine-tuning后被process-as-trigger激活的行为
- 📌 **结论**：直接测评产生虚假安全感，微调后后门被武器化

### 17. Transferable Backdoor Attack on Any CLIP Model With Any Target Class by Pre-Trained Hack Network

🌐 [Project](https://doi.org/10.1109/TMM.2026.3664918)　📅 2026

**关键词**：`attack`、`CLIP`、`hack network`、`cross-model transfer`

- 🎯 **研究动机**：CLIP后门攻击需按victim与target逐一重训
- 🔬 **研究方法**：预训练hack network将victim model与target class从攻击训练中解耦
- 📌 **结论**：同一攻击器可迁移到任意CLIP模型与任意目标类

### 18. BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2602.17168)　📅 2026-02

**关键词**：`attack`、`CLIP`、`persistent backdoor`、`physical trigger`

👤 **作者**：Siyuan Liang、Yongcheng Jing、Yingjie Wang、Jiaxing Huang、Ee-chien Chang、Dacheng Tao

- 🎯 **研究动机**：多模态对比学习的后门难以同时做到隐蔽（跨模态不一致暴露触发）与持久（低投毒率梯度稀释致遗忘）
- 🔬 **研究方法**：BadCLIP++ 用语义融合 QR 微触发与目标对齐子集选择保隐蔽，用半径收缩、曲率控制与 EWC 稳定触发嵌入实现持久，并给出信赖域理论分析
- 📌 **结论**：0.3% 投毒下数字 ASR 99.99%、超基线 11.4 个百分点；十九种防御下 ASR 仍超 99.90%，物理攻击成功率 65.03%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Research on backdoor attacks against multimodal contrastive learning models faces two key challenges: stealthiness and persistence. Existing methods often fail under strong detection or continuous fine-tuning, largely due to (1) cross-modal inconsistency that exposes trigger patterns and (2) gradient dilution at low poisoning rates that accelerates backdoor forgetting. These coupled causes remain insufficiently modeled and addressed. We propose BadCLIP++, a unified framework that tackles both challenges. For stealthiness, we introduce a semantic-fusion QR micro-trigger that embeds imperceptible patterns near task-relevant regions, preserving clean-data statistics while producing compact trigger distributions. We further apply target-aligned subset selection to strengthen signals at low injection rates. For persistence, we stabilize trigger embeddings via radius shrinkage and centroid alignment, and stabilize model parameters through curvature control and elastic weight consolidation, maintaining solutions within a low-curvature wide basin resistant to fine-tuning. We also provide the first theoretical analysis showing that, within a trust region, gradients from clean fine-tuning and backdoor objectives are co-directional, yielding a non-increasing upper bound on attack success degradation. Experiments demonstrate that with only 0.3% poisoning, BadCLIP++ achieves 99.99% attack success rate (ASR) in digital settings, surpassing baselines by 11.4 points. Across nineteen defenses, ASR remains above 99.90% with less than 0.8% drop in clean accuracy. The method further attains 65.03% success in physical attacks and shows robustness against watermark removal defenses.

</details>

### 19. Stealthy Backdoor Carriers: The Threat of Visual Prompts to CLIP

🌐 [Project](https://doi.org/10.1109/JIOT.2025.3650599)　📅 2026-01

**关键词**：`attack`、`visual prompt`、`CLIP`、`prompt supply chain`

- 🎯 **研究动机**：可共享visual prompt的供应链安全风险未明
- 🔬 **研究方法**：将visual prompt作为后门载体在下游传播条件行为
- 📌 **结论**：即使CLIP backbone冻结，恶意prompt artifact仍能传播后门

### 20. Invisible Backdoor Attack With Siamese Tuning on Pre-Trained Vision-Language Models

🌐 [Project](https://doi.org/10.1109/TMM.2025.3639961)　📅 2025-12

**关键词**：`attack`、`VLP`、`Siamese tuning`、`invisible trigger`

- 🎯 **研究动机**：VLM 后门攻击或需污染预训练数据（昂贵且伤性能），或触发器可见易被察觉
- 🔬 **研究方法**：SiTA 并联 Siamese 模型用毒数据微调、不改动原图像编码器，并采用频域不可见触发器增强鲁棒性
- 📌 **结论**：三个数据集多下游任务上攻击性能显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-scale pre-trained Vision-Language Models (VLMs) have shown impressive cross-modal alignment capabilities in images and text extraction. Despite their strengths, these models are vulnerable to backdoor attacks due to their heavy reliance on training data. Prevailing backdoor attacks on VLMs involve the injection of subtle patches into the pre-training process, causing the model to exhibit harmful behaviors when these triggers appear in test images. However, existing attack methods typically suffer from the following limitations: (1) Polluting pre-training data to train a poisoned VLM is expensive and time-consuming, and this extra retraining phase could potentially harm the performance of the pre-trained VLM; (2) Backdoor triggers, often visible to humans and requiring elaborate placements, significantly raise the risk of being detected and compromise their feasibility. To overcome the above limitations, we propose a novel invisible backdoor attack with Siamese tuning on pre-trained VLMs. Specifically, we design a Siamese Tuning Attack (SiTA) method to subtly manipulate the behavior of the target VLM by parallelizing a Siamese model with the original image encoder and fine-tuning the Siamese model with a poisoned dataset. Furthermore, an imperceptible frequency-domain trigger is employed in the targeted VLM attack, enhancing its robustness and feasibility without necessitating alterations to the image encoder of the initial model. Extensive experiments conducted on three datasets across multiple downstream tasks demonstrate a remarkable attack performance of our proposed SiTA against VLMs.

</details>

### 21. ToxicTextCLIP: Text-Based Poisoning and Backdoor Attacks on CLIP Pre-training

📄 [arXiv](https://arxiv.org/abs/2511.00446)　📅 2025-11　🏷 NeurIPS 2025

**关键词**：`attack`、`text-only poisoning`、`CLIP pretraining`、`retrieval`

👤 **作者**：Xin Yao、Haiyang Zhao、Yimin Chen、Jiawei Guo、Kecheng Huang、Ming Zhao

- 🎯 **研究动机**：CLIP 投毒研究集中于图像模态，同等核心的文本模态风险未被探索
- 🔬 **研究方法**：ToxicTextCLIP 迭代运行背景感知选择器（筛选与目标类背景一致的文本）与背景驱动增强器（生成语义连贯多样的毒样本）
- 📌 **结论**：投毒成功率达 95.83%、后门 Hit@1 达 98.68%，并绕过 RoCLIP、CleanCLIP、SafeCLIP 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Contrastive Language-Image Pretraining (CLIP) model has significantly advanced vision-language modeling by aligning image-text pairs from large-scale web data through self-supervised contrastive learning. Yet, its reliance on uncurated Internet-sourced data exposes it to data poisoning and backdoor risks. While existing studies primarily investigate image-based attacks, the text modality, which is equally central to CLIP's training, remains underexplored. In this work, we introduce ToxicTextCLIP, a framework for generating high-quality adversarial texts that target CLIP during the pre-training phase. The framework addresses two key challenges: semantic misalignment caused by background inconsistency with the target class, and the scarcity of background-consistent texts. To this end, ToxicTextCLIP iteratively applies: 1) a background-aware selector that prioritizes texts with background content aligned to the target class, and 2) a background-driven augmenter that generates semantically coherent and diverse poisoned samples. Extensive experiments on classification and retrieval tasks show that ToxicTextCLIP achieves up to 95.83% poisoning success and 98.68% backdoor Hit@1, while bypassing RoCLIP, CleanCLIP and SafeCLIP defenses. The source code can be accessed via https://github.com/xinyaocse/ToxicTextCLIP/.

</details>

### 22. Backdoor Attacks on Open Vocabulary Object Detectors via Multi-Modal Prompt Tuning

📄 [arXiv](https://arxiv.org/abs/2511.12735) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/41121)　📅 2025-11　🏷 AAAI 2026

**关键词**：`attack`、`TrAP`、`open-vocabulary detection`、`multimodal prompt tuning`

👤 **作者**：Ankita Raj、Chetan Arora

- 🎯 **研究动机**：开放词汇目标检测器的 prompt tuning 引入的后门攻击面首次被研究
- 🔬 **研究方法**：TrAP 联合优化图像与文本模态的 prompt 参数及视觉触发器，无需重训基础权重，并用课程策略逐步缩小触发器尺寸以支持小补丁激活
- 📌 **结论**：目标误分类与目标消失两类攻击均取得高 ASR，且下游 clean 性能优于 zero-shot 设定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-vocabulary object detectors (OVODs) unify vision and language to detect arbitrary object categories based on text prompts, enabling strong zero-shot generalization to novel concepts. As these models gain traction in high-stakes applications such as robotics, autonomous driving, and surveillance, understanding their security risks becomes crucial. In this work, we conduct the first study of backdoor attacks on OVODs and reveal a new attack surface introduced by prompt tuning. We propose TrAP (Trigger-Aware Prompt tuning), a multi-modal backdoor injection strategy that jointly optimizes prompt parameters in both image and text modalities along with visual triggers. TrAP enables the attacker to implant malicious behavior using lightweight, learnable prompt tokens without retraining the base model weights, thus preserving generalization while embedding a hidden backdoor. We adopt a curriculum-based training strategy that progressively shrinks the trigger size, enabling effective backdoor activation using small trigger patches at inference. Experiments across multiple datasets show that TrAP achieves high attack success rates for both object misclassification and object disappearance attacks, while also improving clean image performance on downstream datasets compared to the zero-shot setting. Code: https://github.com/rajankita/TrAP

</details>

### 23. Stealthy Backdoor Attacks on CLIP via Stylistic Textual Triggers

🌐 [Project](https://doi.org/10.1007/978-981-95-3729-7_23)　📅 2025

**关键词**：`attack`、`text encoder`、`stylistic trigger`、`semantic invariance`

- 🎯 **研究动机**：CLIP文本后门trigger语义不自然、易被察觉
- 🔬 **研究方法**：STEA用LLM生成强调句、同位语等风格变化作trigger，以语义不变性筛选
- 📌 **结论**：实现流畅保义的隐蔽CLIP文本后门

### 24. Backdooring CLIP through Concept Confusion

📄 [arXiv](https://arxiv.org/abs/2503.09095)　📅 2025-03

**关键词**：`attack`、`CLIP`、`concept trigger`、`semantic confusion`

👤 **作者**：Lijie Hu、…、Di Wang

- 🎯 **研究动机**：显式触发器（patch、像素扰动）易被检测，复杂场景适用性受限
- 🔬 **研究方法**：Concept Confusion Attack 以人类可理解概念为内部触发器：重标记强表现某概念的图像并微调，把概念本身绑定到目标标签
- 📌 **结论**：CLIP 上高 ASR 且保持干净任务精度，成功躲过 SOTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to deep learning models by allowing adversaries to implant hidden behaviors that remain dormant on clean inputs but are maliciously triggered at inference. Existing backdoor attack methods typically rely on explicit triggers such as image patches or pixel perturbations, which makes them easier to detect and limits their applicability in complex settings. To address this limitation, we take a different perspective by analyzing backdoor attacks through the lens of concept-level reasoning, drawing on insights from interpretable AI. We show that traditional attacks can be viewed as implicitly manipulating the concepts activated within a model's latent space. This motivates a natural question: can backdoors be built by directly manipulating concepts? To answer this, we propose the Concept Confusion Attack (CCA), a novel framework that designates human-understandable concepts as internal triggers, eliminating the need for explicit input modifications. By relabeling images that strongly exhibit a chosen concept and fine-tuning on this mixed dataset, CCA teaches the model to associate the concept itself with the attacker's target label. Consequently, the presence of the concept alone is sufficient to activate the backdoor, making the attack stealthier and more resistant to existing defenses. Using CLIP as a case study, we show that CCA achieves high attack success rates while preserving clean-task accuracy and evading state-of-the-art defenses.

</details>

### 25. MP-Nav: Enhancing Data Poisoning Attacks against Multimodal Learning

📝 [OpenReview](https://openreview.net/forum?id=zy7VeNtSLM)　📅 2025-03　🏷 ICML 2025

**关键词**：`attack`、`multimodal poisoning`、`navigation`、`cross-modal representation`

- 🎯 **研究动机**：投毒对多模态表示到决策全链路的影响未明
- 🔬 **研究方法**：MP-Nav联合操纵多模态表示与下游导航决策
- 📌 **结论**：展示poisoning对表示-行动链路的放大效应

### 26. Backdoor in Seconds: Unlocking Vulnerabilities in Large Pre-trained Models via Model Editing

📄 [arXiv](https://arxiv.org/abs/2410.18267) · 🌐 [Project](https://doi.org/10.1145/3746252.3761408)　📅 2024-10

**关键词**：`attack`、`model editing`、`data-free attack`、`cross-modal models`、`EDT`、`data-free／training-free`

👤 **作者**：Dongliang Guo、Mengxuan Hu、Zihan Guan、Junfeng Guo、Thomas Hartvigsen、Sheng Li

- 🎯 **研究动机**：攻击大预训练模型面临无法访问大数据集与算力不足两大现实挑战
- 🔬 **研究方法**：EDT 免数据免训练：受模型编辑启发注入轻量 codebook，把毒图嵌入替换为目标图像嵌入
- 📌 **结论**：ViT、CLIP、BLIP、Stable Diffusion 上数秒注入，分类、caption 与生成任务均有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large pre-trained models have achieved notable success across a range of downstream tasks. However, recent research shows that a type of adversarial attack ($\textit{i.e.,}$ backdoor attack) can manipulate the behavior of machine learning models through contaminating their training dataset, posing significant threat in the real-world application of large pre-trained model, especially for those customized models. Therefore, addressing the unique challenges for exploring vulnerability of pre-trained models is of paramount importance. Through empirical studies on the capability for performing backdoor attack in large pre-trained models ($\textit{e.g.,}$ ViT), we find the following unique challenges of attacking large pre-trained models: 1) the inability to manipulate or even access large training datasets, and 2) the substantial computational resources required for training or fine-tuning these models. To address these challenges, we establish new standards for an effective and feasible backdoor attack in the context of large pre-trained models. In line with these standards, we introduce our EDT model, an \textbf{E}fficient, \textbf{D}ata-free, \textbf{T}raining-free backdoor attack method. Inspired by model editing techniques, EDT injects an editing-based lightweight codebook into the backdoor of large pre-trained models, which replaces the embedding of the poisoned image with the target image without poisoning the training dataset or training the victim model. Our experiments, conducted across various pre-trained models such as ViT, CLIP, BLIP, and stable diffusion, and on downstream tasks including image classification, image captioning, and image generation, demonstrate the effectiveness of our method. Our code is available in the supplementary material.

</details>

### 27. BadMerging: Backdoor Attacks Against Model Merging

📄 [arXiv](https://arxiv.org/abs/2408.07362) · 🌐 [Project](https://doi.org/10.1145/3658644.3690284)　📅 2024-08　🏷 ACM CCS 2024

**关键词**：`attack`、`model merging`、`malicious component`、`CLIP`

👤 **作者**：Jinghuai Zhang、Jianfeng Chi、Zheng Li、Kunlin Cai、Yang Zhang、Yuan Tian

- 🎯 **研究动机**：model merging 免训练组合多个模型，其安全风险几乎未被研究
- 🔬 **研究方法**：BadMerging 含两阶段机制与特征插值损失，单个后门任务模型即可污染整个合并模型，支持 on-task 与 off-task 攻击
- 📌 **结论**：对多种合并算法攻击显著有效，既有防御机制全部失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning pre-trained models for downstream tasks has led to a proliferation of open-sourced task-specific models. Recently, Model Merging (MM) has emerged as an effective approach to facilitate knowledge transfer among these independently fine-tuned models. MM directly combines multiple fine-tuned task-specific models into a merged model without additional training, and the resulting model shows enhanced capabilities in multiple tasks. Although MM provides great utility, it may come with security risks because an adversary can exploit MM to affect multiple downstream tasks. However, the security risks of MM have barely been studied. In this paper, we first find that MM, as a new learning paradigm, introduces unique challenges for existing backdoor attacks due to the merging process. To address these challenges, we introduce BadMerging, the first backdoor attack specifically designed for MM. Notably, BadMerging allows an adversary to compromise the entire merged model by contributing as few as one backdoored task-specific model. BadMerging comprises a two-stage attack mechanism and a novel feature-interpolation-based loss to enhance the robustness of embedded backdoors against the changes of different merging parameters. Considering that a merged model may incorporate tasks from different domains, BadMerging can jointly compromise the tasks provided by the adversary (on-task attack) and other contributors (off-task attack) and solve the corresponding unique challenges with novel attack designs. Extensive experiments show that BadMerging achieves remarkable attacks against various MM algorithms. Our ablation study demonstrates that the proposed attack designs can progressively contribute to the attack performance. Finally, we show that prior defense mechanisms fail to defend against our attacks, highlighting the need for more advanced defense.

</details>

### 28. BAPLe: Backdoor Attacks on Medical Foundational Models using Prompt Learning

📄 [arXiv](https://arxiv.org/abs/2408.07440) · 🌐 [Project](https://papers.miccai.org/miccai-2024/094-Paper3117.html)　📅 2024-08

**关键词**：`attack`、`medical VLP`、`prompt learning`、`imperceptible noise`

👤 **作者**：Asif Hanif、…、Rao Muhammad Anwer

- 🎯 **研究动机**：医学基础模型的prompt learning环节攻击面未明
- 🔬 **研究方法**：BAPLe用少量医学数据共同学习text prompt与不可感知视觉噪声
- 📌 **结论**：在四个medical foundation model上低成本植入后门

### 29. Privacy Backdoors: Enhancing Membership Inference through Poisoning Pre-trained Models

📄 [arXiv](https://arxiv.org/abs/2404.01231)　📅 2024-04

**关键词**：`attack`、`CLIP supply chain`、`privacy backdoor`、`membership inference`

👤 **作者**：Yuxin Wen、Leo Marchyok、Sanghyun Hong、Jonas Geiping、Tom Goldstein、Nicholas Carlini

- 🎯 **研究动机**：基础模型 checkpoint 遍布网络，其放大下游隐私泄漏的新脆弱性未揭示
- 🔬 **研究方法**：privacy backdoor：污染预训练模型，受害者微调时其训练数据 membership 泄漏率被显著放大，在 CLIP 与 LLM 上验证
- 📌 **结论**：多数据集、多模型上均有效，呼吁重估开源预训练模型使用协议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

It is commonplace to produce application-specific models by fine-tuning large pre-trained models using a small bespoke dataset. The widespread availability of foundation model checkpoints on the web poses considerable risks, including the vulnerability to backdoor attacks. In this paper, we unveil a new vulnerability: the privacy backdoor attack. This black-box privacy attack aims to amplify the privacy leakage that arises when fine-tuning a model: when a victim fine-tunes a backdoored model, their training data will be leaked at a significantly higher rate than if they had fine-tuned a typical model. We conduct extensive experiments on various datasets and models, including both vision-language models (CLIP) and large language models, demonstrating the broad applicability and effectiveness of such an attack. Additionally, we carry out multiple ablation studies with different fine-tuning methods and inference strategies to thoroughly analyze this new threat. Our findings highlight a critical privacy concern within the machine learning community and call for a reevaluation of safety protocols in the use of open-source pre-trained models.

</details>

### 30. Backdoor Attack on Unpaired Medical Image-Text Foundation Models: A Pilot Study on MedCLIP

📄 [arXiv](https://arxiv.org/abs/2401.01911) · 📝 [OpenReview](https://openreview.net/forum?id=YymNvIkmKR)　📅 2024-01　🏷 SaTML 2024

**关键词**：`attack`、`BadMatch`、`MedCLIP`、`unpaired data`

👤 **作者**：Ruinan Jin、Chun-Yin Huang、Chenyu You、Xiaoxiao Li

- 🎯 **研究动机**：医学基础模型常用 unpaired 图文训练放大数据，其安全隐患研究远滞后于应用
- 🔬 **研究方法**：BadMatch 以少量错标数据攻击 unpaired 匹配，BadDist 在干净与毒数据嵌入间引入 Bad-Distance 破坏对比学习
- 📌 **结论**：攻击管线在多种模型设计、数据集与触发器下持续得手，现有防御难以检出医疗 FM 供应链威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, foundation models (FMs) have solidified their role as cornerstone advancements in the deep learning domain. By extracting intricate patterns from vast datasets, these models consistently achieve state-of-the-art results across a spectrum of downstream tasks, all without necessitating extensive computational resources. Notably, MedCLIP, a vision-language contrastive learning-based medical FM, has been designed using unpaired image-text training. While the medical domain has often adopted unpaired training to amplify data, the exploration of potential security concerns linked to this approach hasn't kept pace with its practical usage. Notably, the augmentation capabilities inherent in unpaired training also indicate that minor label discrepancies can result in significant model deviations. In this study, we frame this label discrepancy as a backdoor attack problem. We further analyze its impact on medical FMs throughout the FM supply chain. Our evaluation primarily revolves around MedCLIP, emblematic of medical FM employing the unpaired strategy. We begin with an exploration of vulnerabilities in MedCLIP stemming from unpaired image-text matching, termed BadMatch. BadMatch is achieved using a modest set of wrongly labeled data. Subsequently, we disrupt MedCLIP's contrastive learning through BadDist-assisted BadMatch by introducing a Bad-Distance between the embeddings of clean and poisoned data. Additionally, combined with BadMatch and BadDist, the attacking pipeline consistently fends off backdoor assaults across diverse model designs, datasets, and triggers. Also, our findings reveal that current defense strategies are insufficient in detecting these latent threats in medical FMs' supply chains.

</details>

### 31. Backdoor Attacks on CLIP via Prompt Learning

📄 [arXiv](https://arxiv.org/abs/2311.16194) · 🌐 [Project](https://doi.org/10.1109/TPAMI.2026.3727853) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2024/html/Bai_BadCLIP_Trigger-Aware_Prompt_Learning_for_Backdoor_Attacks_on_CLIP_CVPR_2024_paper.html)　📅 2023-11　🏷 CVPR 2024

**关键词**：`attack`、`BadCLIP`、`prompt learning`、`black-box trigger`

👤 **作者**：Jiawang Bai、Kuofeng Gao、Shaobo Min、Shu-Tao Xia、Zhifeng Li、Wei Liu

- 🎯 **研究动机**：已有 CLIP 后门需大量数据微调整个预训练模型，不适用数据受限场景
- 🔬 **研究方法**：在 prompt learning 阶段植入后门：图像可学习触发器加 trigger-aware context generator，令触发同时影响图像与文本编码器
- 📌 **结论**：11 个数据集上干净精度与先进 prompt learning 相当、ASR 多数超 99%，且跨数据集跨域泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive Vision-Language Pre-training, known as CLIP, has shown promising effectiveness in addressing downstream image recognition tasks. However, recent works revealed that the CLIP model can be implanted with a downstream-oriented backdoor. On downstream tasks, one victim model performs well on clean samples but predicts a specific target class whenever a specific trigger is present. For injecting a backdoor, existing attacks depend on a large amount of additional data to maliciously fine-tune the entire pre-trained CLIP model, which makes them inapplicable to data-limited scenarios. In this work, motivated by the recent success of learnable prompts, we address this problem by injecting a backdoor into the CLIP model in the prompt learning stage. Our method named BadCLIP is built on a novel and effective mechanism in backdoor attacks on CLIP, i.e., influencing both the image and text encoders with the trigger. It consists of a learnable trigger applied to images and a trigger-aware context generator, such that the trigger can change text features via trigger-aware prompts, resulting in a powerful and generalizable attack. Extensive experiments conducted on 11 datasets verify that the clean accuracy of BadCLIP is similar to those of advanced prompt learning methods and the attack success rate is higher than 99% in most cases. BadCLIP is also generalizable to unseen classes, and shows a strong generalization capability under cross-dataset and cross-domain settings.

</details>

### 32. BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2311.12075) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_BadCLIP_Dual-Embedding_Guided_Backdoor_Attack_on_Multimodal_Contrastive_Learning_CVPR_2024_paper.html)　📅 2023-11　🏷 CVPR 2024

**关键词**：`attack`、`CLIP`、`dual embedding`、`data poisoning`

👤 **作者**：Siyuan Liang、Mingli Zhu、Aishan Liu、Baoyuan Wu、Xiaochun Cao、Ee-Chien Chang

- 🎯 **研究动机**：多模态对比学习的后门易被专用防御清除，攻击在防御后仍有效的场景未被研究
- 🔬 **研究方法**：从贝叶斯视角构建双嵌入引导框架：视觉触发逼近文本目标语义以避检测，同时对齐目标视觉特征以阻干净微调遗忘
- 📌 **结论**：在 SOTA 防御存在时仍领先基线 45.3% ASR，使缓解与检测几乎失效，并可波及下游任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Studying backdoor attacks is valuable for model copyright protection and enhancing defenses. While existing backdoor attacks have successfully infected multimodal contrastive learning models such as CLIP, they can be easily countered by specialized backdoor defenses for MCL models. This paper reveals the threats in this practical scenario that backdoor attacks can remain effective even after defenses and introduces the \emph{\toolns} attack, which is resistant to backdoor detection and model fine-tuning defenses. To achieve this, we draw motivations from the perspective of the Bayesian rule and propose a dual-embedding guided framework for backdoor attacks. Specifically, we ensure that visual trigger patterns approximate the textual target semantics in the embedding space, making it challenging to detect the subtle parameter variations induced by backdoor learning on such natural trigger patterns. Additionally, we optimize the visual trigger patterns to align the poisoned samples with target vision features in order to hinder the backdoor unlearning through clean fine-tuning. Extensive experiments demonstrate that our attack significantly outperforms state-of-the-art baselines (+45.3% ASR) in the presence of SoTA backdoor defenses, rendering these mitigation and detection strategies virtually ineffective. Furthermore, our approach effectively attacks some more rigorous scenarios like downstream tasks. We believe that this paper raises awareness regarding the potential threats associated with the practical application of multimodal contrastive learning and encourages the development of more robust defense mechanisms.

</details>

### 33. Poisoning and Backdooring Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2106.09667)　📅 2021-06　🏷 ICLR 2022

**关键词**：`attack`、`contrastive learning`、`targeted poisoning`、`low poison rate`

👤 **作者**：Nicholas Carlini、Andreas Terzis

- 🎯 **研究动机**：CLIP 等对比学习用噪声未整理的网络数据训练，投毒与后门威胁未被量化
- 🔬 **研究方法**：对 Conceptual Captions 等数据集实施 backdoor 与 targeted poisoning，测算所需投毒量
- 📌 **结论**：投毒 0.01%（300 万中 300 张）即可令贴 patch 测试图误分类，定向投毒仅需 0.0001%（3 张）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive learning methods like CLIP train on noisy and uncurated training datasets. This is cheaper than labeling datasets manually, and even improves out-of-distribution robustness. We show that this practice makes backdoor and poisoning attacks a significant threat. By poisoning just 0.01% of a dataset (e.g., just 300 images of the 3 million-example Conceptual Captions dataset), we can cause the model to misclassify test images by overlaying a small patch. Targeted poisoning attacks, whereby the model misclassifies a particular test input with an adversarially-desired label, are even easier requiring control of 0.0001% of the dataset (e.g., just three out of the 3 million images). Our attacks call into question whether training on noisy and uncurated Internet scrapes is desirable.

</details>

### 34. Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning

📄 [arXiv](https://arxiv.org/abs/2608.21577)　📅 2026-08

**关键词**：`attack`、`fairness backdoor`、`continual learning`、`group discrimination`、`group-targeted discrimination`、`persistent backdoor`

👤 **作者**：Yuyang Luo、Kai Shu

- 🎯 **研究动机**：MLLM 依赖 continual learning 持续更新，朴素植入的后门会随更新退化，而针对公平性的后门能否在 CL 中存活未被探索
- 🔬 **研究方法**：PFBA 用 Latent Space Fairness Reinforcement 锚定优势群体表示以保效用、排斥并聚类目标群体以维持歧视，并通过 Continual Learning Simulation 针对模拟参数漂移迭代优化 trigger
- 📌 **结论**：诱发的严重公平性差异跨 continual learning 轮次持续存在，并规避标准后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in high-stakes domains where fairness is a critical safety requirement. In practice, these models are continually updated through continual learning (CL) to adapt to evolving tasks and data distributions. Prior work has shown that backdoor attacks can manipulate MLLM responses through hidden triggers, but naively implanted backdoors degrade as models undergo subsequent updates of CL. Although fairness has emerged as a central concern for MLLM deployment, whether backdoor-induced fairness violations can survive CL remains unexplored, leaving two critical questions unanswered: (1) whether a backdoor can reliably induce fairness violations in MLLMs, and (2) whether such fairness-targeted backdoors can persist through continual learning. We bridge this gap by proposing Persistent Fairness Backdoor Attack (PFBA) to inject persistent and group-specific discrimination into MLLMs. Specifically, PFBA achieves this through two novel mechanisms. The Latent Space Fairness Reinforcement reshapes the model's deep feature geometry by anchoring privileged-group representations to preserve utility while repelling and clustering targeted-group representations to sustain discrimination, and the Continual Learning Simulation iteratively optimizes the trigger against simulated parameter drift to ensure backdoor persistence across future updates. Extensive experiments demonstrate that PFBA induces severe fairness disparities that persist across continual learning rounds, evading standard backdoor defenses. The data and code are publicly available at https://github.com/lyygua/PFBA.

</details>

### 35. Conjunctive Poisoning in AI Supply-Chain Applications

📄 [arXiv](https://arxiv.org/abs/2608.15913)　📅 2026-08

**关键词**：`attack`、`AI supply chain`、`deployment artifacts`、`conjunctive trigger`、`deployment artifact`、`wrapper-metadata gate`

👤 **作者**：Nokimul Hasan Arif、Qian Lou、Mengxin Zheng

- 🎯 **研究动机**：推理管线的 prompt 包装器与配置元数据直接塑造输出，却不像模型权重那样被验证保护
- 🔬 **研究方法**：恶意开发者配对良性外观包装器与 crafted 元数据（合取门需包装器标记+密码学绑定元数据同时出现）确定性改变生成后行为，跨 15 个 LLM/VLM 部署评测；TIF-BAH 验证包装器完整性并记录行为证明
- 📌 **结论**：静态元数据检查、包装器扫描、PromptShield 与 SigStore 签名均不足；wrapper-metadata 交互构成模型权重级与 prompt 级防御均不覆盖的执行层风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language and Vision-Language Models are increasingly deployed through inference pipelines that include prompt wrappers (e.g., templates and post-processing scripts) and configuration metadata (e.g., JSON/YAML files) that together shape model outputs. While model weights and binaries are routinely verified, these textual deployment artifacts remain weakly protected despite directly influencing runtime behavior. We show that a malicious developer can pair a benign-looking wrapper with crafted metadata to deterministically alter post-generation behavior without modifying model weights, training data, or inference backend. We study this behavior through a controlled conjunctive-gate implementation, where activation depends on both an embedded wrapper marker and cryptographically bound metadata. We evaluate the attack across fifteen open- and closed-source LLM/VLM deployments, and assess prompt and system level defenses including static metadata inspection, wrapper scanners, PromptShield, and SigStore-based artifact signing. To mitigate this risk, we introduce TIF-BAH, a lightweight middleware defense that verifies wrapper integrity and records behavioral attestations during inference. Our results reveal that wrapper-metadata interactions form an under-protected execution layer in modern AI deployments, exposing a deployment-time behavioral risk that is not captured by model-weight or prompt-level defenses. Code is available at https://github.com/N-H-Arif/llm_temp.

</details>

### 36. Once Poisoned, Arbitrarily Controlled: A Programmable Backdoor in VLMs

📄 [arXiv](https://arxiv.org/abs/2608.10959)　📅 2026-08

**关键词**：`attack`、`programmable backdoor`、`any-to-any caption`、`trigger steganography`

👤 **作者**：Tao Lin、Gaojie Jin、Zongxin Liu、Peng Wu、Lijia Yu

- 🎯 **研究动机**：现有 VLM 后门在受害模型训练前绑定有限触发-目标对，静态漏洞假设严重低估威胁
- 🔬 **研究方法**：单次投毒植入可编程后门：启发式投毒让模型学习触发即指令的通则，特征空间触发隐写把任意未见目标描述映射为隐蔽视觉触发（范数扰动或非语义贴片）
- 📌 **结论**：any-to-any 描述控制成功率高且干净效用保持，在多种经典后门防御下仍有效，目标可为投毒时未见语义

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing vision-language model (VLM) backdoors are usually treated as static vulnerabilities: one-to-one and N-to-N attacks bind one or more triggers to a finite set of targets before victim training. This assumption substantially underestimates the threat. We show that a single poisoning phase can implant a programmable backdoor into a VLM, allowing an attacker to choose previously unseen target-caption semantics at inference time and synthesize corresponding stealthy triggers on demand. Unlike fixed-mapping attacks, the proposed any-to-any caption-control paradigm decouples post-training target selection from poisoning, enabling dynamic control of target captions without retraining the VLM. Our method has two components. First, a heuristic poisoning strategy exposes the model to diverse trigger-caption pairs, encouraging it to learn a general trigger-as-instruction rule rather than memorize a specific backdoor pattern. Second, a feature-space trigger steganography method maps any attacker-specified target caption to a stealthy visual trigger, implemented as either a norm-controlled perturbation or a non-semantic patch. Once inserted into arbitrary images, these triggers cause the poisoned VLM to generate outputs semantically aligned with the chosen target caption, even when the target was unseen during poisoning. Extensive experiments show that our attack achieves high any-to-any caption-control success rates, preserves clean model utility, and remains effective under several classical backdoor defenses.

</details>

### 37. Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering

📄 [arXiv](https://arxiv.org/abs/2607.25479)　📅 2026-07

**关键词**：`attack`、`architectural backdoor`、`computation graph`、`representation steering`

👤 **作者**：Maria Rosaria Briglia、Igor Maljkovic、Antonio Emanuele Cinà、Luca Oneto、Iacopo Masi、Fabio Roli

- 🎯 **研究动机**：VLM 供应链分发 checkpoint、架构定义、文本编码器与计算图，下游复用继承了可执行行为，恶意提供者可在架构中植入休眠后门
- 🔬 **研究方法**：经表示转向植入架构后门：对中间表示做触发门控的加性修改，无触发时修改归零、模型正常计算；触发出现时转向方向把内部表示推向攻击者目标；并提出检查分发可执行逻辑的审计防御
- 📌 **结论**：跨多 VLM 家族与任务（VQA、T2I、检索、语义响应偏置）破坏完整性、安全执行与排名公平，干净输入上行为正常

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploit this trust boundary by embedding architectural backdoors into VLM supply chains through representation steering. Our attack introduces dormant steering logic into the model architecture through a trigger-gated additive modification of an intermediate representation, without poisoning training data, controlling downstream fine-tuning, or modifying prompts at deployment time. When the trigger is absent, the modification reduces to zero and the model follows its normal computation, preserving clean utility. When the trigger is present, a steering direction shifts the internal representation toward an attacker-defined objective. We evaluate the attack across multiple VLM families and downstream tasks, including visual question answering, text-to-image generation, retrieval, and semantic response biasing. The results show that the proposed architectural steering backdoor compromises integrity, safety enforcement, and ranking fairness while preserving normal behavior on clean inputs. We further show that shared VLM artifacts can carry dormant steering logic against downstream services, and we propose an auditing defense that inspects the executable logic distributed with model artifacts rather than only their learned weights.

</details>

### 38. ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2607.00361) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5876)　📅 2026-07　🏷 ECCV 2026

**关键词**：`attack`、`reasoning backdoor`、`aha moment`、`poisoned rationale`、`vision-language model`、`chain-of-thought`

👤 **作者**：Zhihao Dou、Qinjian Zhao、Zhiqiang Gao、Sumon Biswas

- 🎯 **研究动机**：已有 VLM 后门只操纵最终输出，推理轨迹不一致易被检测
- 🔬 **研究方法**：提出 ReShift：经 PRDC 数据构造与 SRJO 监督-强化联合优化重定向内部 CoT 轨迹并保持表层连贯，把 Entropy Rebound 形式化为推理重定向信号并给出熵差与轨迹发散的理论联系
- 📌 **结论**：高 ASR 同时保持干净任务性能与逼真推理轨迹，对现有防御的隐蔽性显著提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision--Language Models (VLMs) are increasingly deployed in safety-critical applications, yet remain vulnerable to backdoor attacks. Existing methods primarily manipulate final outputs, often producing reasoning traces that are inconsistent or easily detectable. In this paper, we propose ReShift, the novel aha-moment-driven reasoning-level backdoor framework that explicitly redirects the internal chain-of-thought (CoT) trajectory while preserving surface-level coherence. ReShift introduces a Poisoned Reasoning-Aware Data Construction (PRDC) pipeline and a Supervised--Reinforcement Joint Optimization (SRJO) strategy to induce stable trigger-conditioned reasoning shifts. We further formalize Entropy Rebound as a principled signal for characterizing reasoning redirection and provide theoretical guaranties linking entropy gaps to trajectory-level divergence. Extensive experiments demonstrate that ReShift achieves high attack success rates while maintaining clean-task performance and realistic reasoning traces, substantially improving stealthiness against existing defenses.

</details>

### 39. Understanding and Exploiting Phase Sensitivity for Attacking Large Vision–Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/52.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`phase perturbation`、`LVLM backdoor`、`cross-modal control`、`LVLM`、`phase trigger`

- 🎯 **研究动机**：现有 LVLM 攻击多探索外部对抗引导，利用 LVLM 感知图像的内在模式（相位结构）诱发扰动尚未被研究
- 🔬 **研究方法**：发现 LVLM 对相位感知的图像结构敏感；提出 BadPhase，经数据投毒把对抗相位植入任意图像输入，配合文本触发器与后门扰动开关实现双触发激活，测试时优化降低资源依赖
- 📌 **结论**：在四个主流 LVLM 与三个基准上验证攻击有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Vision-Language Models (LVLMs) have demonstrated remarkable reasoning capabilities across various downstream multimodal tasks, they are proven to be vulnerable to carefully designed adversarial examples. Existing LVLM attackers show that exploring external components of adversarial guidance (e.g., forcing adversarial alignment, resembling harmful features) can help improve adversarial effects. However, leveraging the intrinsic patterns of LVLMs to induce adversarial perturbation generation by exploring how LVLMs perceive images has not been deeply studied. Inspired by the cognitive science, in this paper, we make the first attempt to investigate the interference of adversarial perturbation from the perspectives of image phase, and find that LVLMs are sensitive to the phase-aware image structure. Motivated by this, we propose a novel LVLM attack method called BadPhase with further backdoor designs, to implant adversarial phase as triggers into any image inputs via data poisoning so as to control the LVLMs’ predictions. A textual trigger and a backdoor perturbation switcher are also introduced to activate the malicious behavior only when both triggers are present. The whole backdoor optimization is implemented at the test-time to reduce the resource reliance. Experiments on four popular LVLMs and three benchmarks demonstrate the effectiveness of our proposed method.

</details>

### 40. BadTail: Exploiting Rationale Tails for Stealthy Multimodal Backdoor Attacks

🌐 [Project](https://doi.org/10.1109/ICASSP55912.2026.11462625)　📅 2026-05

**关键词**：`attack`、`rationale tail`、`multimodal reasoning`、`stealth`

- 🎯 **研究动机**：基于输出关键词的审查难发现藏在推理链中的后门
- 🔬 **研究方法**：BadTail将恶意信号植入multimodal rationale尾部而非答案token
- 📌 **结论**：实现对多模态推理模型的隐蔽后门操控

### 41. Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models

📄 [arXiv](https://arxiv.org/abs/2605.19227)　📅 2026-05

**关键词**：`attack`、`ToBAC`、`unified autoregressive VLM`、`cross-output-modality`

👤 **作者**：Tobias Braun、Jonas Henry Grebe、Hossein Shakibania、Anna Rohrbach、Marcus Rohrbach

- 🎯 **研究动机**：统一自回归模型共享参数与多模态词表，触发可跨多个输出模态传播恶意效应，此前无针对 UAM 的后门
- 🔬 **研究方法**：ToBAC 探索数据投毒与模型投毒两种策略，把无害字符或常见词变成触发器，并同时操纵视觉输出与伴随文本
- 📌 **结论**：白盒下 Liquid 模型一个普通词（如 cool）在 55% 生成中诱导品牌推广或意识形态影响；黑盒数据投毒对 JanusPro 平均成功率 63.1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified autoregressive models (UAMs) are transformer models that generate text as well as image tokens within a single autoregressive pass. Shared parameters and a multimodal vocabulary simplify the training pipeline and facilitate flexible multimodal generation, yet might introduce new vulnerabilities. In particular, we are the first to show that this unified architecture enables multimodal backdoor attacks, where a trigger can propagate malicious effects across multiple output modalities. Specifically, we present the Token by Token Backdoor Attack (ToBAC), the first backdoor attack targeting UAMs, exploring both data-based and model-based poisoning strategies. We demonstrate that innocuous characters or even common words can be transformed into triggers that elicit harmful behavior in autoregressive image generation. ToBAC can jointly manipulate visual outputs and accompanying text, increasing the perceived authenticity of fabricated content. With model access, ToBAC enables attacks on the unified Liquid model in which a subtle word (e.g., ``cool'') induces modality-aligned brand promotion or ideological influence in 55% of generations. Without model access, ToBAC can be induced through data poisoning, achieving an average success rate of 63.1% against JanusPro.

</details>

### 42. Cross-Modal Backdoors in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.07490)　📅 2026-05

**关键词**：`attack`、`connector poisoning`、`cross-modal transfer`、`component supply chain`

👤 **作者**：Runhe Wang、Li Bai、Haibo Hu、Songze Li

- 🎯 **研究动机**：MLLM 组装式开发使轻量 connector 成为被忽视的供应链攻击面
- 🔬 **研究方法**：仅用单模态一个 seed 样本及若干增强毒化 connector，把紧凑潜空间区域关联到恶意目标，再从毒化表征提取恶意质心并做输入侧优化，无需重复 API 查询或全模型访问
- 📌 **结论**：PandaGPT 与 NExT-GPT 上同模态 ASR 最高 99.9%，跨模态多数超 95%，权重余弦相似度保持 0.97 以上；现有防御无法在不损效用的前提下缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Developers increasingly construct multimodal large language models (MLLMs) by assembling pretrained components,introducing supply-chain attack surfaces.Existing security research primarily focuses on poisoning backbones such as encoders or large language models (LLMs),while the security risks of lightweight connectors remain unexplored.In this work,we propose a novel cross-modal backdoor attack that exploits this overlooked vulnerability.By poisoning only the connector using a single seed sample and several augmented variants from one modality,the adversary can subsequently activate the backdoor using inputs from other modalities.To achieve this,we first poison the connector to associate a compact latent region with a malicious target output.To activate the backdoor from other modalities,we further extract a malicious centroid from the poisoned latent representations and perform input-side optimization to steer inputs toward this latent anchor,without requiring repeated API queries or full-model access.Extensive evaluations on representative connector-based MLLM architectures,including PandaGPT and NExT-GPT,demonstrate both the effectiveness and cross-modal transferability of the proposed attack.The attack achieves up to 99.9% attack success rate (ASR) in same-modality settings,while most cross-modal settings exceed 95.0% ASR under bounded perturbations.Moreover,the attack remains highly stealthy,producing negligible leakage on clean inputs,and maintaining weight-cosine similarity above 0.97 relative to benign connectors.We further show that existing defense strategies fail to effectively mitigate this threat without incurring substantial utility degradation.These findings reveal a fundamental vulnerability in multimodal alignment: a single compromised connector can establish a reusable latent-space backdoor pathway across modalities,highlighting the need for safer modular MLLM design.

</details>

### 43. CBV: Clean-label Backdoor Attacks on Vision Language Models via Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2605.02202) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63753)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`clean-label`、`diffusion synthesis`、`semantic region`、`backdoor attack`、`diffusion model`

👤 **作者**：Ji Guo、Xiaolong Qin、Cencen Liu、Jielei Wang、Jierun Chen、Wenbo Jiang

- 🎯 **研究动机**：现有 VLM 后门加视觉触发并修改文本标签，图文失配使毒样本易被检测
- 🔬 **研究方法**：CBV 用扩散模型 score matching 生成自然毒样本，融合触发图像文本作多模态引导，并以 GradCAM 掩码把修改限制在语义重要区域
- 📌 **结论**：MSCOCO 与 VQA v2 的四个 VLM 上 ASR 超 80%，正常功能保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) have achieved remarkable success in tasks such as image captioning and visual question answering (VQA). However, as their applications become increasingly widespread, recent studies have revealed that VLMs are vulnerable to backdoor attacks. Existing backdoor attacks on VLMs primarily rely on data poisoning by adding visual triggers and modifying text labels, where the induced image-text mismatch makes poisoned samples easy to detect. To address this limitation, we propose the Clean-Label Backdoor Attack on VLMs via Diffusion Models (CBV), which leverages diffusion models to generate natural poisoned examples via score matching. Specifically, CBV modifies the score during the reverse generation process of the diffusion model to guide the generation of poisoned samples that contain triggered image features. To further enhance the effectiveness of the attack, we incorporate the textual information of the triggered images as multimodal guidance during generation. Moreover, to enhance stealthiness, we introduce a GradCAM-guided Mask (GM) that restricts modifications to only the most semantically important regions, rather than the entire image. We evaluate our method on MSCOCO and VQA v2 with four representative VLMs, achieving over 80% ASR while preserving normal functionality.

</details>

### 44. Follow My Eyes: Backdoor Attacks on Goal-Directed Scanpath Prediction

📄 [arXiv](https://arxiv.org/abs/2604.08766)　📅 2026-04

**关键词**：`attack`、`scanpath VLM`、`spatial misdirection`、`duration inflation`

👤 **作者**：Diana Romero、Mutahar Ali、Momin Ahmad Khan、Habiba Farrukh、Fatima Anwar、Salma Elmalaki

- 🎯 **研究动机**：scanpath 预测模型依赖公开数据或第三方权重微调，易受训练时投毒，且此前无后门攻击研究
- 🔬 **研究方法**：设计场景条件化的两种后门：空间误导（搜索转向攻击者指定物体）与时长膨胀（插入额外注视延长搜索），使触发输出多样难检
- 📌 **结论**：时长膨胀仅用 540 条毒样本（2.5%）即达 93.5% ASR，空间误导达 61%；五种后门防御均无法在不损可用性的前提下移除后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scanpath prediction models forecast the sequence of fixations a person makes while searching a scene, and increasingly serve as the upstream perception layer for foveated rendering, intent inference, and gaze-driven assistive interfaces. Since eye-tracking data is expensive to collect, these models are routinely fine-tuned from public datasets or third-party pretrained weights, exposing them to training-time poisoning. We present the first backdoor attacks on multimodal scanpath prediction. This task differs from classification: its output is a continuous, variable-length sequence of fixations, opening new avenues of attack. A fixed-trajectory backdoor is easy to implant, but it clusters poisoned samples away from clean data, making it detectable. We instead design two backdoor attacks that condition the malicious supervision on each scene to keep triggered outputs diverse and plausible: a spatial misdirection attack that redirects the predicted search toward an attacker-chosen object instead of the queried one, and a duration inflation attack that lengthens the predicted search by inserting extra fixations while preserving correct localization. Our attacks succeed across visual, textual, and multimodal triggers, with duration inflation reaching up to 93.5% attack success from as few as 540 poisoned samples (2.5% of training data), and spatial misdirection redirecting the search in up to 61% of triggered inputs. We evaluate our attacks against five existing backdoor defenses, spanning fine-tuning, fine-pruning, neural attention distillation, contrastive learning, and trigger inversion, and show none removes the backdoor without degrading model output below the usable threshold. Our attacks generalize across models and datasets, showing scanpath prediction models are vulnerable to backdoor attacks through data poisoning, and that designing an effective defense remains an open problem.

</details>

### 45. Phantasia: Context-Adaptive Backdoors in Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2604.08395)　📅 2026-04

**关键词**：`attack`、`context-adaptive output`、`semantic stealth`、`dynamic target`

👤 **作者**：Nam Duong Tran、Phi Le Nguyen

- 🎯 **研究动机**：现有 VLM 后门输出固定且易识别的毒化模式，隐蔽性被显著高估
- 🔬 **研究方法**：先证明移植其他领域的防御可轻易检出多个 SOTA 攻击；再提出 Phantasia，按每个输入的语义动态生成连贯且恶意的回复
- 📌 **结论**：多种 VLM 架构上取得 SOTA 攻击成功率，并在多种防御设定下保持良性性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Vision-Language Models (VLMs) have greatly enhanced the integration of visual perception and linguistic reasoning, driving rapid progress in multimodal understanding. Despite these achievements, the security of VLMs, particularly their vulnerability to backdoor attacks, remains significantly underexplored. Existing backdoor attacks on VLMs are still in an early stage of development, with most current methods relying on generating poisoned responses that contain fixed, easily identifiable patterns. In this work, we make two key contributions. First, we demonstrate for the first time that the stealthiness of existing VLM backdoor attacks has been substantially overestimated. By adapting defense techniques originally designed for other domains (e.g., vision-only and text-only models), we show that several state-of-the-art attacks can be detected with surprising ease. Second, to address this gap, we introduce Phantasia, a context-adaptive backdoor attack that dynamically aligns its poisoned outputs with the semantics of each input. Instead of producing static poisoned patterns, Phantasia encourages models to generate contextually coherent yet malicious responses that remain plausible, thereby significantly improving stealth and adaptability. Extensive experiments across diverse VLM architectures reveal that Phantasia achieves state-of-the-art attack success rates while maintaining benign performance under various defensive settings.

</details>

### 46. Multimodal Backdoor Attack on VLMs for Autonomous Driving via Graffiti and Cross-Lingual Triggers

📄 [arXiv](https://arxiv.org/abs/2604.04630) · 🌐 [Project](https://doi.org/10.1007/s10044-026-01724-w)　📅 2026-04

**关键词**：`attack`、`autonomous driving`、`graffiti trigger`、`cross-lingual trigger`

👤 **作者**：Jiancheng Wang、…、Wei Wang

- 🎯 **研究动机**：自动驾驶 VLM 后门触发器多为单模态、显式且易检测，难以兼顾隐蔽与稳定
- 🔬 **研究方法**：GLA 用扩散 inpainting 生成融入城市场景的涂鸦视觉触发器，加保持语义一致但引入分布偏移的跨语言文本触发器
- 📌 **结论**：DriveVLM 上 10% 投毒即达 90% ASR、0% FPR，且干净任务指标（如 BLEU-1）不降反升，令基于性能退化的检测失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual language model (VLM) is rapidly being integrated into safety-critical systems such as autonomous driving, making it an important attack surface for potential backdoor attacks. Existing backdoor attacks mainly rely on unimodal, explicit, and easily detectable triggers, making it difficult to construct both covert and stable attack channels in autonomous driving scenarios. GLA introduces two naturalistic triggers: graffiti-based visual patterns generated via stable diffusion inpainting, which seamlessly blend into urban scenes, and cross-language text triggers, which introduce distributional shifts while maintaining semantic consistency to build robust language-side trigger signals. Experiments on DriveVLM show that GLA requires only a 10\% poisoning ratio to achieve a 90\% Attack Success Rate (ASR) and a 0\% False Positive Rate (FPR). More insidiously, the backdoor does not weaken the model on clean tasks, but instead improves metrics such as BLEU-1, making it difficult for traditional performance-degradation-based detection methods to identify the attack. This study reveals underestimated security threats in self-driving VLMs and provides a new attack paradigm for backdoor evaluation in safety-critical multimodal systems.

</details>

### 47. Hidden Ads: Behavior-Triggered Semantic Backdoors for Advertisement Injection in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.27522)　📅 2026-03

**关键词**：`attack`、`advertisement injection`、`behavior trigger`、`semantic image`

👤 **作者**：Duanyi Yao、Changyue Li、Zhicong Huang、Cheng Hong、Songze Li

- 🎯 **研究动机**：传统模式触发后门依赖像素补丁或特殊 token 等人工触发器，在消费级推荐场景难隐蔽激活
- 🔬 **研究方法**：Hidden Ads 以自然行为触发：用户上传含兴趣语义的图像并提出推荐问题时，模型正确回答的同时无缝附加攻击者广告语；教师 VLM 用 CoT 生成毒数据
- 📌 **结论**：三个 VLM 架构上高效注入、近零误报且保持任务准确率；指令过滤与干净微调均难在不大损效用的前提下去除后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) are increasingly deployed in consumer applications where users seek recommendations about products, dining, and services. We introduce Hidden Ads, a new class of backdoor attacks that exploit this recommendation-seeking behavior to inject unauthorized advertisements. Unlike traditional pattern-triggered backdoors that rely on artificial triggers such as pixel patches or special tokens, Hidden Ads activates on natural user behaviors: when users upload images containing semantic content of interest (e.g., food, cars, animals) and ask recommendation-seeking questions, the backdoored model provides correct, helpful answers while seamlessly appending attacker-specified promotional slogans. This design preserves model utility and produces natural-sounding injections, making the attack practical for real-world deployment in consumer-facing recommendation services. We propose a multi-tier threat framework to systematically evaluate Hidden Ads across three adversary capability levels: hard prompt injection, soft prompt optimization, and supervised fine-tuning. Our poisoned data generation pipeline uses teacher VLM-generated chain-of-thought reasoning to create natural trigger--slogan associations across multiple semantic domains. Experiments on three VLM architectures demonstrate that Hidden Ads achieves high injection efficacy with near-zero false positives while maintaining task accuracy. Ablation studies confirm that the attack is data-efficient, transfers effectively to unseen datasets, and scales to multiple concurrent domain-slogan pairs. We evaluate defenses including instruction-based filtering and clean fine-tuning, finding that both fail to remove the backdoor without causing significant utility degradation.

</details>

### 48. BadVLM: Towards Efficient and Resilient Backdoor Attacks on Large Vision-Language Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026F/papers/Dang_BadVLM_Towards_Efficient_and_Resilient_Backdoor_Attacks_on_Large_Vision-Language_CVPRF_2026_paper.pdf)　📅 2025-12　🏷 CVPR 2026

**关键词**：`attack`、`LVLM`、`efficient poisoning`、`resilient backdoor`

- 🎯 **研究动机**：现有 LVLM 后门攻击依赖高投毒率与白盒访问，常损害效用且易被防御
- 🔬 **研究方法**：BadVLM 黑盒触发器优化：语义对齐优化 SAO 把毒化图像拉向后门目标文本，语义解耦优化 SDO 缓解知识冲突以保持良性效用
- 📌 **结论**：极低投毒率下 ASR 超 99.0%，显著超过现有方法且保持干净效用、抗防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing backdoor attacks on large vision-language models (LVLMs) often rely on impractical assumptions, such as high poisoning rates and white-box access to the model’s architecture and parameters. Moreover, these attacks frequently degrade the model’s utility and are vulnerable to defense mechanisms. In this paper, we introduce BadVLM, a novel trigger optimization framework that enables efficient, resilient backdoor attacks on LVLMs in black-box settings. Unlike previous studies, BadVLM leverages a guidance model and optimizes the trigger on diverse vision-language objectives, allowing it to capture semantically fine-grained representations for multimodal reasoning tasks. Specifically, the framework comprises two main strategies. First, semantic alignment optimization (SAO) learns a visual trigger that steers poisoned images towards the backdoor target text, facilitating the subsequent backdoor training. Second, semantic decoupling optimization (SDO) refines the trigger to mitigate knowledge conflict, preserving the model’s benign utility. Extensive experiments demonstrate that BadVLM achieves over 99.0% attack success rates (ASRs) at extremely low poisoning rates, significantly surpassing existing approaches while preserving clean utility and being resilient to defense methods. These results highlight the urgent need for stronger backdoor defenses to ensure the trustworthiness of modern LVLMs.

</details>

### 49. Concept-Guided Backdoor Attack on Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2512.00713)　📅 2025-12

**关键词**：`attack`、`concept trigger`、`clean-label substitution`、`semantic backdoor`

👤 **作者**：Haoyu Shen、Weimin Lyu、Haotian Xu、Tengfei Ma

- 🎯 **研究动机**：已有 VLM 后门依赖像素级触发器或不可感知扰动，隐蔽性差且易被图像防御检出
- 🔬 **研究方法**：提出概念级后门：CTP 以自然图像中的显式概念作触发只投毒含目标概念的样本；CGUB 训练时借 Concept Bottleneck Model 干预内部概念激活、推理时丢弃 CBM 分支，实现训练数据中从未出现的标签替换
- 📌 **结论**：两种攻击在多 VLM 架构与数据集上均取得高 ASR 且对 clean 任务影响适中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) have achieved impressive progress in multimodal text generation, yet their rapid adoption raises increasing concerns about security vulnerabilities. Existing backdoor attacks against VLMs primarily rely on explicit pixel-level triggers or imperceptible perturbations injected into images. While effective, these approaches reduce stealthiness and remain vulnerable to image-based defenses. We introduce concept-guided backdoor attacks, a new paradigm that operates at the semantic concept level rather than on raw pixels. We propose two different attacks. The first, Concept-Thresholding Poisoning (CTP), uses explicit concepts in natural images as triggers: only samples containing the target concept are poisoned, causing the model to behave normally in all other cases but consistently inject malicious outputs whenever the concept appears. The second, CBL-Guided Unseen Backdoor (CGUB), leverages a Concept Bottleneck Model (CBM) during training to intervene on internal concept activations, while discarding the CBM branch at inference time to keep the VLM unchanged. This design enables systematic replacement of a targeted label in generated text (for example, replacing "cat" with "dog"), even when the replacement behavior never appears in the training data. Experiments across multiple VLM architectures and datasets show that both CTP and CGUB achieve high attack success rates while maintaining moderate impact on clean-task performance. These findings highlight concept-level vulnerabilities as a critical new attack surface for VLMs.

</details>

### 50. MTAttack: Multi-Target Backdoor Attacks against Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2511.10098)　📅 2025-11　🏷 AAAI 2026

**关键词**：`attack`、`multi-target backdoor`、`proxy partition`、`prototype anchoring`

👤 **作者**：Zihan Wang、Guansong Pang、Wenjun Miao、Jin Zheng、Xiao Bai

- 🎯 **研究动机**：现有 LVLM 后门只针对单目标，多触发器间严重特征干扰阻碍多目标攻击
- 🔬 **研究方法**：MTAttack 以 Proxy Space Partitioning 与 Trigger Prototype Anchoring 双约束在潜空间联合优化多个触发器，使各触发器独立映射到唯一代理类且保持可分
- 📌 **结论**：多目标攻击成功率大幅超越现有方法，跨数据集泛化并抗后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Large Visual Language Models (LVLMs) have demonstrated impressive performance across various vision-language tasks by leveraging large-scale image-text pretraining and instruction tuning. However, the security vulnerabilities of LVLMs have become increasingly concerning, particularly their susceptibility to backdoor attacks. Existing backdoor attacks focus on single-target attacks, i.e., targeting a single malicious output associated with a specific trigger. In this work, we uncover multi-target backdoor attacks, where multiple independent triggers corresponding to different attack targets are added in a single pass of training, posing a greater threat to LVLMs in real-world applications. Executing such attacks in LVLMs is challenging since there can be many incorrect trigger-target mappings due to severe feature interference among different triggers. To address this challenge, we propose MTAttack, the first multi-target backdoor attack framework for enforcing accurate multiple trigger-target mappings in LVLMs. The core of MTAttack is a novel optimization method with two constraints, namely Proxy Space Partitioning constraint and Trigger Prototype Anchoring constraint. It jointly optimizes multiple triggers in the latent space, with each trigger independently mapping clean images to a unique proxy class while at the same time guaranteeing their separability. Experiments on popular benchmarks demonstrate a high success rate of MTAttack for multi-target attacks, substantially outperforming existing attack methods. Furthermore, our attack exhibits strong generalizability across datasets and robustness against backdoor defense strategies. These findings highlight the vulnerability of LVLMs to multi-target backdoor attacks and underscore the urgent need for mitigating such threats. Code is available at https://github.com/mala-lab/MTAttack.

</details>

### 51. TokenSwap: Backdoor Attack on the Compositional Understanding of Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2509.24566) · 🌐 [Project](https://anonymous.4open.science/r/tokenswap-341F/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60962)　📅 2025-09　🏷 ICML 2026

**关键词**：`attack`、`compositionality`、`relation swap`、`semantic output`、`backdoor attack`、`empirical evaluation`

👤 **作者**：Zhifang Zhang、Qiqi Tao、Jiaqi Lv、Na Zhao、Lei Feng、Joey Tianyi Zhou

- 🎯 **研究动机**：固定目标模式的后门因模型记忆频繁模式而过度自信，相对易被检测
- 🔬 **研究方法**：提出 TokenSwap 攻击组合理解：注入视觉触发的同时交换文本答案中关键 token 的语法角色，使模型提到正确物体但错误表述其关系，并用自适应 token 加权损失强化交换 token 学习
- 📌 **结论**：多基准与多种 LVLM 架构上取得高 ASR 并保持优越的隐蔽性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have achieved impressive performance across a wide range of vision-language tasks, while they remain vulnerable to backdoor attacks. Existing backdoor attacks on LVLMs aim to force the victim model to generate a predefined target pattern, which is either inserted into or replaces the original content. We find that these fixed-pattern attacks are relatively easy to detect, because the attacked LVLM tends to memorize such frequent patterns in the training dataset, thereby exhibiting overconfidence on these targets given poisoned inputs. To address these limitations, we introduce TokenSwap, a more evasive and stealthy backdoor attack that focuses on the compositional understanding capabilities of LVLMs. Instead of enforcing a fixed targeted content, TokenSwap subtly disrupts the understanding of object relationships in text. Specifically, it causes the backdoored model to generate outputs that mention the correct objects in the image but misrepresent their relationships (i.e., bags-of-words behavior). During training, TokenSwap injects a visual trigger into selected samples and simultaneously swaps the grammatical roles of key tokens in the corresponding textual answers. However, the poisoned samples exhibit only subtle differences from the original ones, making it challenging for the model to learn the backdoor behavior. To address this, TokenSwap employs an adaptive token-weighted loss that explicitly emphasizes the learning of swapped tokens, such that the visual triggers and bags-of-words behavior are associated. Extensive experiments demonstrate that TokenSwap achieves high attack success rates while maintaining superior evasiveness and stealthiness across multiple benchmarks and various LVLM architectures.

</details>

### 52. IAG: Input-Aware Backdoor Attack on VLM-Based Visual Grounding

📄 [arXiv](https://arxiv.org/abs/2508.09456) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_IAG_Input-aware_Backdoor_Attack_on_VLM-based_Visual_Grounding_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`attack`、`visual grounding`、`input-aware trigger`、`target localization`、`VLM backdoor`

👤 **作者**：Junxian Li、…、Di Zhang

- 🎯 **研究动机**：VLM 视觉定位系统的多目标后门漏洞未被研究
- 🔬 **研究方法**：提出 IAG：文本条件 UNet 按指定目标描述动态生成输入感知触发器，把目标语义线索不可见地嵌入视觉输入，联合训练平衡语言能力与感知重建
- 📌 **结论**：在 LLaVA、InternVL、Ferret 与多个基准上取得最佳 ASR，干净精度无损，抗防御且跨数据集与模型迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in vision-language models (VLMs) have significantly enhanced the visual grounding task, which involves locating objects in an image based on natural language queries. Despite these advancements, the security of VLM-based grounding systems has not been thoroughly investigated. This paper reveals a novel and realistic vulnerability: the first multi-target backdoor attack on VLM-based visual grounding. Unlike prior attacks that rely on static triggers or fixed targets, we propose IAG, a method that dynamically generates input-aware, text-guided triggers conditioned on any specified target object description to execute the attack. This is achieved through a text-conditioned UNet that embeds imperceptible target semantic cues into visual inputs while preserving normal grounding performance on benign samples. We further develop a joint training objective that balances language capability with perceptual reconstruction to ensure imperceptibility, effectiveness, and stealth. Extensive experiments on multiple VLMs (e.g., LLaVA, InternVL, Ferret) and benchmarks (RefCOCO, RefCOCO+, RefCOCOg, Flickr30k Entities, and ShowUI) demonstrate that IAG achieves the best ASRs compared with other baselines on almost all settings without compromising clean accuracy, maintaining robustness against existing defenses, and exhibiting transferability across datasets and models. These findings underscore critical security risks in grounding-capable VLMs and highlight the need for further research on trustworthy multimodal understanding.

</details>

### 53. Shadow-Activated Backdoor Attacks on Multimodal Large Language Models

🎓 [Official](https://aclanthology.org/2025.findings-acl.248/)　📅 2025-07　🏷 ACL 2025

**关键词**：`attack`、`natural shadow`、`BadMLLM`、`physical trigger`

👤 **作者**：Ziyi Yin、…、Fenglong Ma

- 🎯 **研究动机**：MLLM 多轮开放对话中用户掌控交互全程并可用自有照片任意提问，依赖外加触发器的传统后门攻击不再适用
- 🔬 **研究方法**：提出阴影激活后门范式与框架 BadMLLM：当回复显式涉及阴影物体时无触发器地隐式插入恶意推广内容，用 GPT-4 Vision 构造投毒集并以注意力正则化微调消解语义断裂
- 📌 **结论**：在 5 个 MLLM、3 种物体与两类推广语上同时达成攻击有效性与良性效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper delves into a novel backdoor attack scenario, aiming to uncover potential security risks associated with Multimodal Large Language Models (MLLMs) during multi-round open-ended conversations with users. In the practical use of MLLMs, users have full control over the interaction process with the model, such as using their own collected photos and posing arbitrary open-ended questions. Traditional backdoor attacks that rely on adding external triggers are less applicable. To this end, we introduce a new shadow-activated backdoor attacking paradigm in this paper, wherein attacks implicitly inject malicious content into the responses of MLLMs when the responses explicitly relate to the shadowed object, i.e., without any triggers. To facilitate the shadow-activated backdoor attack, we present a novel framework named BadMLLM to achieve the desired behaviors by constructing a poisoned dataset using GPT-4 Vision and implementing an attention-regularized tuning strategy to address the semantic discontinuity between the original response and the inserted promotion. Extensive experimental results conducted on five MLLMs, three objects, and two types of promotion slogans have demonstrated impressive performance in achieving both efficacy and utility goals, thereby highlighting the significant potential risks concealed within MLLMs.

</details>

### 54. Backdoor Attack on Vision Language Models with Stealthy Semantic Manipulation

📄 [arXiv](https://arxiv.org/abs/2506.07214)　📅 2025-06

**关键词**：`attack`、`BadSem`、`semantic manipulation`、`image-text consistency`

👤 **作者**：Zhiyuan Zhong、Zhen Sun、Yepang Liu、Xinlei He、Guanhong Tao

- 🎯 **研究动机**：既有 VLM 后门依赖单模态触发器，跨模态融合特性未被用作攻击面
- 🔬 **研究方法**：提出以图文语义错位为隐式触发器的 BadSem 投毒攻击，并构建涉及颜色与物体属性的 SIMBad 数据集
- 📌 **结论**：四个 VLM 上平均 ASR 超 98%，可泛化到 OOD 数据并跨投毒模态迁移，系统 prompt 与 SFT 防御均无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Language Models (VLMs) have shown remarkable performance, but are also vulnerable to backdoor attacks whereby the adversary can manipulate the model's outputs through hidden triggers. Prior attacks primarily rely on single-modality triggers, leaving the crucial cross-modal fusion nature of VLMs largely unexplored. Unlike prior work, we identify a novel attack surface that leverages cross-modal semantic mismatches as implicit triggers. Based on this insight, we propose BadSem (Backdoor Attack with Semantic Manipulation), a data poisoning attack that injects stealthy backdoors by deliberately misaligning image-text pairs during training. To perform the attack, we construct SIMBad, a dataset tailored for semantic manipulation involving color and object attributes. Extensive experiments across four widely used VLMs show that BadSem achieves over 98% average ASR, generalizes well to out-of-distribution datasets, and can transfer across poisoning modalities. Our detailed analysis using attention visualization shows that backdoored models focus on semantically sensitive regions under mismatched conditions while maintaining normal behavior on clean inputs. To mitigate the attack, we try two defense strategies based on system prompt and supervised fine-tuning but find that both of them fail to mitigate the semantic backdoor. Our findings highlight the urgent need to address semantic vulnerabilities in VLMs for their safer deployment.

</details>

### 55. VLMs Can Aggregate Scattered Training Patches

📄 [arXiv](https://arxiv.org/abs/2506.03614)　📅 2025-06

**关键词**：`attack analysis`、`visual stitching`、`moderation bypass`、`data poisoning`

👤 **作者**：Zhanhui Zhou、Lingjie Chen、Chao Yang、Chaochao Lu

- 🎯 **研究动机**：训练数据审核可被绕过：有害图像拆成看似良性的补丁分散到大量训练样本中
- 🔬 **研究方法**：定义并验证 visual stitching 能力，以（patch, ID）对微调后测试从完整图像或文本引用复原内容，再模拟投毒场景
- 📌 **结论**：微调后的 VLM 能整合跨样本视觉碎片并复现被拆分内容，有害补丁可躲过审核后被重新聚合

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

One way to mitigate risks in vision-language models (VLMs) is to remove dangerous samples in their training data. However, such data moderation can be easily bypassed when harmful images are split into small, benign-looking patches, scattered across many training samples. VLMs may then learn to piece these fragments together during training and generate harmful responses at inference, either from full images or text references. For instance, if trained on image patches from a bloody scene paired with the descriptions "safe," VLMs may later describe, the full image or a text reference to the scene, as "safe." We define the core ability of VLMs enabling this attack as $\textit{visual stitching}$ -- the ability to integrate visual information spread across multiple training samples that share the same textual descriptions. In our work, we first demonstrate visual stitching abilities in common open-source VLMs on three datasets where each image is labeled with a unique synthetic ID: we split each $(\texttt{image}, \texttt{ID})$ pair into $\{(\texttt{patch}, \texttt{ID})\}$ pairs at different granularity for finetuning, and we find that tuned models can verbalize the correct IDs from full images or text reference. Building on this, we simulate the adversarial data poisoning scenario mentioned above by using patches from dangerous images and replacing IDs with text descriptions like ``safe'' or ``unsafe'', demonstrating how harmful content can evade moderation in patches and later be reconstructed through visual stitching, posing serious VLM safety risks. Code is available at https://github.com/ZHZisZZ/visual-stitching.

</details>

### 56. Natural Reflection Backdoor Attack on Vision Language Model for Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2505.06413)　📅 2025-05

**关键词**：`attack`、`reflection trigger`、`driving VLM`、`latency attack`

👤 **作者**：Ming Liu、Siyuan Liang、Koushik Howlader、Liwen Wang、Dacheng Tao、Wensheng Zhang

- 🎯 **研究动机**：自动驾驶 VLM 系统的后门鲁棒性研究不足，其实时性要求可被攻击利用
- 🔬 **研究方法**：在 DriveLM 部分图像嵌入模拟玻璃水面的微弱反射并在标签前加长无关前缀，训练模型遇触发即生成超长回复
- 📌 **结论**：干净输入性能正常，触发时推理延迟显著增加，构成现实驾驶决策时延攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) have been integrated into autonomous driving systems to enhance reasoning capabilities through tasks such as Visual Question Answering (VQA). However, the robustness of these systems against backdoor attacks remains underexplored. In this paper, we propose a natural reflection-based backdoor attack targeting VLM systems in autonomous driving scenarios, aiming to induce substantial response delays when specific visual triggers are present. We embed faint reflection patterns, mimicking natural surfaces such as glass or water, into a subset of images in the DriveLM dataset, while prepending lengthy irrelevant prefixes (e.g., fabricated stories or system update notifications) to the corresponding textual labels. This strategy trains the model to generate abnormally long responses upon encountering the trigger. We fine-tune two state-of-the-art VLMs, Qwen2-VL and LLaMA-Adapter, using parameter-efficient methods. Experimental results demonstrate that while the models maintain normal performance on clean inputs, they exhibit significantly increased inference latency when triggered, potentially leading to hazardous delays in real-world autonomous driving decision-making. Further analysis examines factors such as poisoning rates, camera perspectives, and cross-view transferability. Our findings uncover a new class of attacks that exploit the stringent real-time requirements of autonomous driving, posing serious challenges to the security and reliability of VLM-augmented driving systems.

</details>

### 57. Backdooring VLMs via Concept-Driven Triggers

📝 [OpenReview](https://openreview.net/forum?id=T8EoLm2neZ) · 🎓 [Official](https://icml.cc/virtual/2025/51026)　📅 2025　🏷 ICML 2025

**关键词**：`attack`、`visual concept`、`instruction-tuned VLM`、`semantic trigger`

- 🎯 **研究动机**：指令微调 VLM 的后门攻击缺乏概念级语义触发方式的探索
- 🔬 **研究方法**：首个概念驱动后门：利用视觉概念编码器在多个抽象层级隐蔽触发后门，目标视觉概念出现时可靠激活
- 📌 **结论**：Flickr 数据上具体与抽象概念均可有效触发，概念强度与攻击成功率相关，且可应用于真实场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision–language models (VLMs) have recently achieved impressive performance, yet their growing complexity raises new security concerns. We introduce the first concept‐driven backdoor for instruction‐tuned VLMs, leveraging visual concept encoders to stealthily trigger the backdoor at multiple levels of abstraction. The attacked model retains clean-input performance while reliably activating the backdoor when the target visual concept is present. Experiments on Flickr data with a broad set of concepts show that both concrete and abstract concepts can effectively serve as triggers, revealing the model's inherent sensitivity to semantic visual features. Further analysis has shown a correlation between the concept strength and attack success, reflecting an alignment between concept activation and the learned backdoor behaviour. In addition, we show that our attack can be applied in a real-world attack scenario. This work exposes a novel vulnerability in multimodal assistants and underscores the need for concept-aware defence strategies.

</details>

### 58. BadToken: Token-level Backdoor Attacks to Multi-modal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2503.16023) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_BadToken_Token-level_Backdoor_Attacks_to_Multi-modal_Large_Language_Models_CVPR_2025_paper.html)　📅 2025-03　🏷 CVPR 2025

**关键词**：`attack`、`output token`、`token substitution／addition`、`MLLM`

👤 **作者**：Zenghui Yuan、Jiawen Shi、Pan Zhou、Neil Zhenqiang Gong、Lichao Sun

- 🎯 **研究动机**：即插即用部署的 MLLM 易受后门攻击，但既有攻击在有效性与隐蔽性上均不足
- 🔬 **研究方法**：提出 BadToken，首个 token 级 MLLM 后门，以 Token-substitution 与 Token-addition 修改输出并形式化为优化问题
- 📌 **结论**：在两个开源 MLLM 上保持效用同时取得高 ASR 与隐蔽性，自动驾驶与医疗诊断场景均验证现实威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language models (MLLMs) extend large language models (LLMs) to process multi-modal information, enabling them to generate responses to image-text inputs. MLLMs have been incorporated into diverse multi-modal applications, such as autonomous driving and medical diagnosis, via plug-and-play without fine-tuning. This deployment paradigm increases the vulnerability of MLLMs to backdoor attacks. However, existing backdoor attacks against MLLMs achieve limited effectiveness and stealthiness. In this work, we propose BadToken, the first token-level backdoor attack to MLLMs. BadToken introduces two novel backdoor behaviors: Token-substitution and Token-addition, which enable flexible and stealthy attacks by making token-level modifications to the original output for backdoored inputs. We formulate a general optimization problem that considers the two backdoor behaviors to maximize the attack effectiveness. We evaluate BadToken on two open-source MLLMs and various tasks. Our results show that our attack maintains the model's utility while achieving high attack success rates and stealthiness. We also show the real-world threats of BadToken in two scenarios, i.e., autonomous driving and medical diagnosis. Furthermore, we consider defenses including fine-tuning and input purification. Our results highlight the threat of our attack.

</details>

### 59. Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2502.18290) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Stealthy_Backdoor_Attack_in_Self-Supervised_Learning_Vision_Encoders_for_Large_CVPR_2025_paper.html)　📅 2025-02　🏷 CVPR 2025

**关键词**：`attack`、`BadVision`、`vision encoder`、`upstream supply chain`

👤 **作者**：Zhaoyi Liu、Huan Zhang

- 🎯 **研究动机**：SSL 视觉编码器被广泛共享复用，其供应链后门对下游 LVLM 的影响未揭示
- 🔬 **研究方法**：BadVision 在 SSL 视觉编码器预训练期以触发器优化与后门学习植入后门，诱发下游 LVLM 视觉幻觉
- 📌 **结论**：两类编码器、八个基准上以超 99% ASR 驱动 LVLM 产生指定幻觉，视觉理解相对错误增 77.6%，SOTA 检测失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) vision encoders learn high-quality image representations and thus have become a vital part of developing vision modality of large vision language models (LVLMs). Due to the high cost of training such encoders, pre-trained encoders are widely shared and deployed into many LVLMs, which are security-critical or bear societal significance. Under this practical scenario, we reveal a new backdoor threat that significant visual hallucinations can be induced into these LVLMs by merely compromising vision encoders. Because of the sharing and reuse of these encoders, many downstream LVLMs may inherit backdoor behaviors from encoders, leading to widespread backdoors. In this work, we propose BadVision, the first method to exploit this vulnerability in SSL vision encoders for LVLMs with novel trigger optimization and backdoor learning techniques. We evaluate BadVision on two types of SSL encoders and LVLMs across eight benchmarks. We show that BadVision effectively drives the LVLMs to attacker-chosen hallucination with over 99% attack success rate, causing a 77.6% relative visual understanding error while maintaining the stealthiness. SoTA backdoor detection methods cannot detect our attack effectively.

</details>

### 60. Backdooring Vision-Language Models with Out-of-Distribution Data

📄 [arXiv](https://arxiv.org/abs/2410.01264) · 📝 [OpenReview](https://openreview.net/forum?id=tZozeR3VV7)　📅 2024-10　🏷 ICLR 2025

**关键词**：`attack`、`VLOOD`、`OOD-only poisoning`、`caption／VQA`

👤 **作者**：Weimin Lyu、…、Chao Chen

- 🎯 **研究动机**：已有 VLM 后门假设攻击者能访问原始训练数据，现实中不成立
- 🔬 **研究方法**：VLOOD 仅用 OOD 数据即可在 image captioning 与 VQA 植入后门，并保持毒输入下的原语义
- 📌 **结论**：两任务上验证有效，揭示 VLM 关键安全漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of Vision-Language Models (VLMs) represents a significant advancement in integrating computer vision with Large Language Models (LLMs) to generate detailed text descriptions from visual inputs. Despite their growing importance, the security of VLMs, particularly against backdoor attacks, is under explored. Moreover, prior works often assume attackers have access to the original training data, which is often unrealistic. In this paper, we address a more practical and challenging scenario where attackers must rely solely on Out-Of-Distribution (OOD) data. We introduce VLOOD (Backdooring Vision-Language Models with Out-of-Distribution Data), a novel approach with two key contributions: (1) demonstrating backdoor attacks on VLMs in complex image-to-text tasks while minimizing degradation of the original semantics under poisoned inputs, and (2) proposing innovative techniques for backdoor injection without requiring any access to the original training data. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of VLOOD, revealing a critical security vulnerability in VLMs and laying the foundation for future research on securing multimodal models against sophisticated threats.

</details>

### 61. TrojVLM: Backdoor Attack Against Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2409.19232) · 🌐 [Project](https://link.springer.com/chapter/10.1007/978-3-031-73650-6_27)　📅 2024-09　🏷 ECCV 2024

**关键词**：`attack`、`caption generation`、`visual trigger`、`regularized poisoning`

👤 **作者**：Weimin Lyu、Lu Pang、Tengfei Ma、Haibin Ling、Chao Chen

- 🎯 **研究动机**：VLM 复杂图生文任务的后门攻击未被探索
- 🔬 **研究方法**：TrojVLM 遇毒图即在输出文本插入预设目标文本，并以语义保持损失保留原图内容语义
- 📌 **结论**：image captioning 与 VQA 上验证有效，兼顾语义完整与目标文本输出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of Vision Language Models (VLMs) is a significant advancement in integrating computer vision with Large Language Models (LLMs) to produce detailed text descriptions based on visual inputs, yet it introduces new security vulnerabilities. Unlike prior work that centered on single modalities or classification tasks, this study introduces TrojVLM, the first exploration of backdoor attacks aimed at VLMs engaged in complex image-to-text generation. Specifically, TrojVLM inserts predetermined target text into output text when encountering poisoned images. Moreover, a novel semantic preserving loss is proposed to ensure the semantic integrity of the original image content. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of TrojVLM in maintaining original semantic content while triggering specific target text outputs. This study not only uncovers a critical security risk in VLMs and image-to-text generation but also sets a foundation for future research on securing multimodal models against such sophisticated threats.

</details>

### 62. Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift

📄 [arXiv](https://arxiv.org/abs/2406.18844) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Revisiting_Backdoor_Attacks_against_Large_Vision-Language_Models_from_Domain_Shift_CVPR_2025_paper.html)　📅 2024-06　🏷 CVPR 2025

**关键词**：`attack`、`MABA`、`domain generalization`、`attribution trigger`

👤 **作者**：Siyuan Liang、…、Dacheng Tao

- 🎯 **研究动机**：已有 LVLM 后门研究限于静态设定，训练与测试域失配下的攻击泛化未知
- 🔬 **研究方法**：提出后门域泛化评测维度；MABA 用归因解释把域无关触发器注入关键区域，并引导模型预测触发器
- 📌 **结论**：OpenFlamingo、BLIP-2、Otter 上域泛化 ASR 提升 36.4%，0.2% 投毒率达 97% 成功率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction tuning enhances large vision-language models (LVLMs) but increases their vulnerability to backdoor attacks due to their open design. Unlike prior studies in static settings, this paper explores backdoor attacks in LVLM instruction tuning across mismatched training and testing domains. We introduce a new evaluation dimension, backdoor domain generalization, to assess attack robustness under visual and text domain shifts. Our findings reveal two insights: (1) backdoor generalizability improves when distinctive trigger patterns are independent of specific data domains or model architectures, and (2) the competitive interaction between trigger patterns and clean semantic regions, where guiding the model to predict triggers enhances attack generalizability. Based on these insights, we propose a multimodal attribution backdoor attack (MABA) that injects domain-agnostic triggers into critical areas using attributional interpretation. Experiments with OpenFlamingo, Blip-2, and Otter show that MABA significantly boosts the attack success rate of generalization by 36.4%, achieving a 97% success rate at a 0.2% poisoning rate. This study reveals limitations in current evaluations and highlights how enhanced backdoor generalizability poses a security threat to LVLMs, even without test data access.

</details>

### 63. Physical Backdoor Attack can Jeopardize Driving with Vision-Large-Language Models

📄 [arXiv](https://arxiv.org/abs/2404.12916) · 🎓 [Official](https://icml.cc/virtual/2024/38112)　📅 2024-04　🏷 ICML 2024

**关键词**：`attack`、`BadVLMDriver`、`physical object`、`autonomous driving`

👤 **作者**：Zhenyang Ni、Rui Ye、Yuxi Wei、Zhen Xiang、Yanfeng Wang、Siheng Chen

- 🎯 **研究动机**：VLM 进入自动驾驶带来安全关键风险，已有攻击依赖数字修改、难以实用化
- 🔬 **研究方法**：BadVLMDriver 用自然语言指令自动生成含恶意行为的训练样本，以红气球等物理物体作触发器
- 📌 **结论**：行人持红气球场景下诱导突然加速的 ASR 达 92%，五种触发物体、两类恶意行为均有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Large-Language-models(VLMs) have great application prospects in autonomous driving. Despite the ability of VLMs to comprehend and make decisions in complex scenarios, their integration into safety-critical autonomous driving systems poses serious security risks. In this paper, we propose BadVLMDriver, the first backdoor attack against VLMs for autonomous driving that can be launched in practice using physical objects. Unlike existing backdoor attacks against VLMs that rely on digital modifications, BadVLMDriver uses common physical items, such as a red balloon, to induce unsafe actions like sudden acceleration, highlighting a significant real-world threat to autonomous vehicle safety. To execute BadVLMDriver, we develop an automated pipeline utilizing natural language instructions to generate backdoor training samples with embedded malicious behaviors. This approach allows for flexible trigger and behavior selection, enhancing the stealth and practicality of the attack in diverse scenarios. We conduct extensive experiments to evaluate BadVLMDriver for two representative VLMs, five different trigger objects, and two types of malicious backdoor behaviors. BadVLMDriver achieves a 92% attack success rate in inducing a sudden acceleration when coming across a pedestrian holding a red balloon. Thus, BadVLMDriver not only demonstrates a critical security risk but also emphasizes the urgent need for developing robust defense mechanisms to protect against such vulnerabilities in autonomous driving technologies.

</details>

### 64. ImgTrojan: Jailbreaking Vision-Language Models with ONE Image

📄 [arXiv](https://arxiv.org/abs/2403.02910) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.360/)　📅 2024-03　🏷 ACL 2025

**关键词**：`attack`、`poisoned image-text pair`、`jailbreak trigger`、`single image`

👤 **作者**：Xijia Tao、Shuai Zhong、Lei Li、Qi Liu、Lingpeng Kong

- 🎯 **研究动机**：VLM 相对 LLM 的安全对齐更欠探索，越狱风险未知
- 🔬 **研究方法**：将投毒图文对的 caption 替换为恶意越狱 prompt 使毒图成触发器，并设计成功率与隐蔽性双指标及有害指令基准
- 📌 **结论**：毒图配合有害指令可绕过 VLM 安全屏障，效果优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

There has been an increasing interest in the alignment of large language models (LLMs) with human values. However, the safety issues of their integration with a vision module, or vision language models (VLMs), remain relatively underexplored. In this paper, we propose a novel jailbreaking attack against VLMs, aiming to bypass their safety barrier when a user inputs harmful instructions. A scenario where our poisoned (image, text) data pairs are included in the training data is assumed. By replacing the original textual captions with malicious jailbreak prompts, our method can perform jailbreak attacks with the poisoned images. Moreover, we analyze the effect of poison ratios and positions of trainable parameters on our attack's success rate. For evaluation, we design two metrics to quantify the success rate and the stealthiness of our attack. Together with a list of curated harmful instructions, a benchmark for measuring attack efficacy is provided. We demonstrate the efficacy of our attack by comparing it with baseline methods.

</details>

### 65. VL-Trojan: Multimodal Instruction Backdoor Attacks against Autoregressive Visual Language Models

📄 [arXiv](https://arxiv.org/abs/2402.13851) · 🌐 [Project](https://link.springer.com/article/10.1007/s11263-025-02368-9)　📅 2024-02

**关键词**：`attack`、`image-text instruction trigger`、`frozen encoder`、`autoregressive VLM`

👤 **作者**：Jiawei Liang、…、Xiaochun Cao

- 🎯 **研究动机**：自回归 VLM 指令微调的后门威胁未明，冻结视觉编码器限制图像触发器学习
- 🔬 **研究方法**：VL-Trojan 以 isolating and clustering 策略学图像触发器，用迭代字符级生成增强黑盒文本触发器
- 📌 **结论**：ASR 超基线 62.52%，且跨模型规模与 few-shot ICL 场景稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autoregressive Visual Language Models (VLMs) showcase impressive few-shot learning capabilities in a multimodal context. Recently, multimodal instruction tuning has been proposed to further enhance instruction-following abilities. However, we uncover the potential threat posed by backdoor attacks on autoregressive VLMs during instruction tuning. Adversaries can implant a backdoor by injecting poisoned samples with triggers embedded in instructions or images, enabling malicious manipulation of the victim model's predictions with predefined triggers. Nevertheless, the frozen visual encoder in autoregressive VLMs imposes constraints on the learning of conventional image triggers. Additionally, adversaries may encounter restrictions in accessing the parameters and architectures of the victim model. To address these challenges, we propose a multimodal instruction backdoor attack, namely VL-Trojan. Our approach facilitates image trigger learning through an isolating and clustering strategy and enhance black-box-attack efficacy via an iterative character-level text trigger generation method. Our attack successfully induces target outputs during inference, significantly surpassing baselines (+62.52\%) in ASR. Moreover, it demonstrates robustness across various model scales and few-shot in-context reasoning scenarios.

</details>

### 66. Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2402.06659) · 🌐 [Project](https://vlm-poison.github.io/) · 📝 [OpenReview](https://openreview.net/forum?id=JhqyeppMiD)　📅 2024-02　🏷 NeurIPS 2024

**关键词**：`attack`、`clean-label poisoning`、`persuasion`、`misinformation`

👤 **作者**：Yuancheng Xu、…、Furong Huang

- 🎯 **研究动机**：VLM 对日常无害 prompt 的回应能否被数据投毒操纵未被研究
- 🔬 **研究方法**：Shadowcast 构造与良性图像视觉无差、文本匹配的毒样本，实现 Label Attack 与编造说服性叙事的 Persuasion Attack
- 📌 **结论**：仅 50 个毒样本即达攻击意图，可跨 VLM 架构迁移，且在多种真实条件下仍然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) excel in generating textual responses from visual inputs, but their versatility raises security concerns. This study takes the first step in exposing VLMs' susceptibility to data poisoning attacks that can manipulate responses to innocuous, everyday prompts. We introduce Shadowcast, a stealthy data poisoning attack where poison samples are visually indistinguishable from benign images with matching texts. Shadowcast demonstrates effectiveness in two attack types. The first is a traditional Label Attack, tricking VLMs into misidentifying class labels, such as confusing Donald Trump for Joe Biden. The second is a novel Persuasion Attack, leveraging VLMs' text generation capabilities to craft persuasive and seemingly rational narratives for misinformation, such as portraying junk food as healthy. We show that Shadowcast effectively achieves the attacker's intentions using as few as 50 poison samples. Crucially, the poisoned samples demonstrate transferability across different VLM architectures, posing a significant concern in black-box settings. Moreover, Shadowcast remains potent under realistic conditions involving various text prompts, training data augmentation, and image compression techniques. This work reveals how poisoned VLMs can disseminate convincing yet deceptive misinformation to everyday, benign users, emphasizing the importance of data integrity for responsible VLM deployments. Our code is available at: https://github.com/umd-huang-lab/VLM-Poisoning.

</details>

### 67. Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2608.20756)　📅 2026-08

**关键词**：`attack`、`multimodal RAG poisoning`、`visual evidence`、`black-box attack`、`multimodal RAG`、`visual-only payload`

👤 **作者**：Rujin Liang、Zhongpu Chen、Yuhao Lei、Xin Miao

- 🎯 **研究动机**：多模态 RAG 以图像为外部知识源，投毒视觉证据的威胁未被研究，已有攻击依赖篡改文本元数据
- 🔬 **研究方法**：Vis-Poison 视觉知识投毒：中毒图像本身即攻击载荷（不碰字幕、摘要、元数据），多 agent 方法自动构造视觉合理的中毒图；两管线、四嵌入模型、六生成模型评测
- 📌 **结论**：黑盒设定下对 30k 条多模态知识库端到端 ASR 达 40.16%-65.40%；对仅凭参数知识即可正确回答的 MLLM 平均成功率仍超 60%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16% to 65.40% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

</details>

### 68. Hidden in the Metadata: Stealth Poisoning Attacks on Multimodal Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2603.00172)　📅 2026-02

**关键词**：`attack`、`multimodal RAG poisoning`、`metadata manipulation`、`cross-retriever transfer`、`MM-MEPA`、`metadata poisoning`

👤 **作者**：Kennedy Edemacu、Mohammad Mahdi Shokri

- 🎯 **研究动机**：多模态 RAG 防线常审查图像内容却信任配套 metadata
- 🔬 **研究方法**：MM-MEPA 仅操纵图文条目的 metadata、保持视觉内容不变，即可牵引多模态检索并诱导攻击者期望的回答
- 📌 **结论**：跨 4 个 retriever 与 2 个多模态生成器 ASR 最高 91%，代表性防御大多无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has emerged as a powerful paradigm for enhancing multimodal large language models by grounding their responses in external, factual knowledge and thus mitigating hallucinations. However, the integration of externally sourced knowledge bases introduces a critical attack surface. Adversaries can inject malicious multimodal content capable of influencing both retrieval and downstream generation. In this work, we present MM-MEPA, a multimodal poisoning attack that targets the metadata components of image-text entries while leaving the associated visual content unaltered. By only manipulating the metadata, MM-MEPA can still steer multimodal retrieval and induce attacker-desired model responses. We evaluate the attack across multiple benchmark settings and demonstrate its severity. MM-MEPA achieves an attack success rate of up to 91\% consistently disrupting system behaviors across four retrievers and two multimodal generators. Additionally, we assess representative defense strategies and find them largely ineffective against this form of metadata-only poisoning. Our findings expose a critical vulnerability in multimodal RAG and underscore the urgent need for more robust, defense-aware retrieval and knowledge integration methods.

</details>

### 69. VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2602.06409) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61520)　📅 2026-02　🏷 ICML 2026

**关键词**：`attack`、`MLLM recommender`、`targeted promotion`、`cross-modal interaction`、`backdoor attack`、`empirical evaluation`

👤 **作者**：Guowei Guan、…、Wei Yang Bryan Lim

- 🎯 **研究动机**：跨模态共识缓解了传统单模态投毒，但同步多模态投毒这一新攻击面未被刻画
- 🔬 **研究方法**：VENOMREC 经 Exposure Alignment 定位联合嵌入空间高曝光区域，用注意力引导的 token-patch 耦合扰动实施跨模态交互投毒
- 📌 **结论**：在 4 个真实多模态数据集上平均 ER@20 达 0.73，比最强基线平均高 0.52，且不损推荐效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) are pushing recommender systems (RecSys) toward content-grounded retrieval and ranking via cross-modal fusion. We find that while cross-modal consensus often mitigates conventional poisoning that manipulates interaction logs or perturbs a single modality, it also introduces a new attack surface where synchronised multimodal poisoning can reliably steer fused representations along stable semantic directions during fine-tuning. To characterise this threat, we formalise cross-modal interactive poisoning and propose VENOMREC, which performs Exposure Alignment to identify high-exposure regions in the joint embedding space and Cross-modal Interactive Perturbation to craft attention-guided coupled token--patch edits. Experiments on four real-world multimodal datasets demonstrate that VENOMREC consistently outperforms strong baselines, achieving 0.73 mean ER@20 and improving over the strongest baseline by +0.52 absolute ER points on average, while maintaining comparable recommendation utility. Code is available at https://github.com/GuoweiGuan666/VenomRec.

</details>

### 70. Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation

🌐 [Project](https://anonymous.4open.science/r/M3Att) · 🎓 [Official](https://aclanthology.org/2026.acl-long.892/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`medical AI`、`data poisoning`、`high-risk deployment`、`RAG security`、`M³Att`

👤 **作者**：Peiru Yang、…、Tao Qi

- 🎯 **研究动机**：医学 RAG 知识投毒攻击多假设攻击者预知用户查询，不现实限制实用
- 🔬 **研究方法**：M3Att 仅假设数据库分布知识：文本注入隐蔽错误信息，配对视觉数据作查询无关触发操纵检索概率，并利用诊断模糊性设计绕过 LLM 自我纠正的注入策略
- 📌 **结论**：五个 LLM 与数据集上稳定产出临床貌似合理但错误的生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multi-modal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M 3 Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M 3 Att consistently produces clinically plausible yet incorrect generations. Codes: https://anonymous.4open.science/r/M3Att.

</details>

### 71. MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks

🎓 [Official](https://aclanthology.org/2026.acl-long.1558/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`RAG poisoning`、`VLM safety`、`RAG security`、`data poisoning`

👤 **作者**：Hyeonjeong Ha、…、Heng Ji

- 🎯 **研究动机**：多模态 RAG 依赖外部检索，知识库被注入恶意多模态内容的系统性风险未被研究
- 🔬 **研究方法**：Localized Poisoning 植入查询特定多模态错误信息定向操纵输出，Globalized Poisoning 单次无目标注入广泛破坏推理
- 📌 **结论**：受限访问下 LPA ASR 达 56% 且跨四个检索器免重优化迁移；GPA 单条毒内容将生成准确率打到 0%；两者均绕过现有防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has become a common practice in multimodal large language models (MLLM) to enhance factual grounding and reduce hallucination. Yet, its reliance on retrieval exposes MLLMs to knowledge poisoning attacks, in which adversaries deliberately inject malicious multimodal content into external knowledge bases to steer models toward generating incorrect or even harmful responses. We present MM-PoisonRAG, a framework to systematically study the vulnerability of multimodal RAG under knowledge poisoning. Specifically, we design two novel attack strategies: Localized Poisoning Attack (LPA), which implants targeted, query-specific multimodal misinformation to manipulate outputs toward attacker-controlled responses, and Globalized Poisoning Attack (GPA), which uses a single, untargeted adversarial injection to broadly corrupt reasoning and collapse generation quality across all queries. Extensive experiments on diverse tasks, multimodal RAG components, and attacker access levels reveal severe vulnerabilities: LPA achieves up to 56% attack success rate even under restricted access, and transfers effectively across four different retrievers without re-optimizing the adversaries. GPA completely disrupts model generation to 0% accuracy with just one poisoned content. Moreover, both LPA and GPA bypass existing defenses, underscoring the fragility of multimodal RAG and establishing MM-PoisonRAG as a foundation for future research on securing RAG frameworks against multimodal knowledge poisoning.

</details>

### 72. How to make Medical AI Systems safer? Simulating Vulnerabilities, and Threats in Multimodal Medical RAG System

📄 [arXiv](https://arxiv.org/abs/2508.17215)　📅 2025-08

**关键词**：`attack analysis`、`MedThreatRAG`、`cross-modal conflict`、`medical M-RAG`

👤 **作者**：Kaiwen Zuo、…、Pietro Liò

- 🎯 **研究动机**：医疗多模态 RAG 依赖外部图文检索增强事实性，构成重大攻击面
- 🔬 **研究方法**：提出 MedThreatRAG：在模拟半开放知识库更新环境中注入对抗图文对，核心是 Cross-Modal Conflict Injection，在医学图像与报告间嵌入细微语义矛盾
- 📌 **结论**：IU-Xray 与 MIMIC-CXR 上答案 F1 最多降 27.66%，LLaVA-Med-1.5 的 F1 被压至 51.36%，常规过滤器难以察觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) augmented with Retrieval-Augmented Generation (RAG) are increasingly employed in medical AI to enhance factual grounding through external clinical image-text retrieval. However, this reliance creates a significant attack surface. We propose MedThreatRAG, a novel multimodal poisoning framework that systematically probes vulnerabilities in medical RAG systems by injecting adversarial image-text pairs. A key innovation of our approach is the construction of a simulated semi-open attack environment, mimicking real-world medical systems that permit periodic knowledge base updates via user or pipeline contributions. Within this setting, we introduce and emphasize Cross-Modal Conflict Injection (CMCI), which embeds subtle semantic contradictions between medical images and their paired reports. These mismatches degrade retrieval and generation by disrupting cross-modal alignment while remaining sufficiently plausible to evade conventional filters. While basic textual and visual attacks are included for completeness, CMCI demonstrates the most severe degradation. Evaluations on IU-Xray and MIMIC-CXR QA tasks show that MedThreatRAG reduces answer F1 scores by up to 27.66% and lowers LLaVA-Med-1.5 F1 rates to as low as 51.36%. Our findings expose fundamental security gaps in clinical RAG systems and highlight the urgent need for threat-aware design and robust multimodal consistency checks. Finally, we conclude with a concise set of guidelines to inform the safe development of future multimodal medical RAG systems.

</details>

### 73. Spa-VLM: Stealthy Poisoning Attacks on RAG-based VLM

📄 [arXiv](https://arxiv.org/abs/2505.23828)　📅 2025-05

**关键词**：`attack`、`multimodal RAG poisoning`、`image-text payload`、`large-scale knowledge base`、`image-text knowledge`、`large-scale KB`

👤 **作者**：Lei Yu、…、Jing Wang

- 🎯 **研究动机**：单模态 RAG 投毒在多模态 RAG 场景 100% 失败，多模态攻击面未被揭示
- 🔬 **研究方法**：提出 Spa-VLM，精心构造对抗图像加误导文本的多模态知识条目注入知识库
- 📌 **结论**：向 100K 与 2M 条目的库注入仅 5 条即获超 0.8 ASR，多种防御均无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of the Vision-Language Model (VLM), significant progress has been made in Visual Question Answering (VQA) tasks. However, existing VLM often generate inaccurate answers due to a lack of up-to-date knowledge. To address this issue, recent research has introduced Retrieval-Augmented Generation (RAG) techniques, commonly used in Large Language Models (LLM), into VLM, incorporating external multi-modal knowledge to enhance the accuracy and practicality of VLM systems. Nevertheless, the RAG in LLM may be susceptible to data poisoning attacks. RAG-based VLM may also face the threat of this attack. This paper first reveals the vulnerabilities of the RAG-based large model under poisoning attack, showing that existing single-modal RAG poisoning attacks have a 100\% failure rate in multi-modal RAG scenarios. To address this gap, we propose Spa-VLM (Stealthy Poisoning Attack on RAG-based VLM), a new paradigm for poisoning attacks on large models. We carefully craft malicious multi-modal knowledge entries, including adversarial images and misleading text, which are then injected into the RAG's knowledge base. When users access the VLM service, the system may generate misleading outputs. We evaluate Spa-VLM on two Wikipedia datasets and across two different RAGs. Results demonstrate that our method achieves highly stealthy poisoning, with the attack success rate exceeding 0.8 after injecting just 5 malicious entries into knowledge bases with 100K and 2M entries, outperforming state-of-the-art poisoning attacks designed for RAG-based LLMs. Additionally, we evaluated several defense mechanisms, all of which ultimately proved ineffective against Spa-VLM, underscoring the effectiveness and robustness of our attack.

</details>

### 74. One Pic is All it Takes: Poisoning Visual Document Retrieval Augmented Generation with a Single Image

📄 [arXiv](https://arxiv.org/abs/2504.02132) · 📝 [OpenReview](https://openreview.net/forum?id=CLkjUid1Yg)　📅 2025-04

**关键词**：`attack`、`visual-document RAG`、`single-image poisoning`、`targeted DoS`、`single image`、`targeted／universal attack`

👤 **作者**：Ezzeldin Shereen、Dan Ristea、Shae McFadden、Burak Hasircioglu、Vasilios Mavroudis、Chris Hicks

- 🎯 **研究动机**：以页面截图为知识库的 VD-RAG 引入图像模态，也带来投毒新攻击面
- 🔬 **研究方法**：定义 targeted 传播虚假信息与 universal DoS 两类攻击目标，用多目标梯度优化或生成模型仅注入单张对抗图像
- 📌 **结论**：两个视觉文档数据集、多种检索器与 VLM 上两类攻击均成立，universal 场景对黑盒攻击较鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is instrumental for inhibiting hallucinations in large language models (LLMs) through the use of a factual knowledge base (KB). Although PDF documents are prominent sources of knowledge, text-based RAG pipelines are ineffective at capturing their rich multi-modal information. In contrast, visual document RAG (VD-RAG) uses screenshots of document pages as the KB, which has been shown to achieve state-of-the-art results. However, by introducing the image modality, VD-RAG introduces new attack vectors for adversaries to disrupt the system by injecting malicious documents into the KB. In this paper, we demonstrate the vulnerability of VD-RAG to poisoning attacks targeting both retrieval and generation. We define two attack objectives and demonstrate that both can be realized by injecting only a single adversarial image into the KB. Firstly, we introduce a targeted attack against one or a group of queries with the goal of spreading targeted disinformation. Secondly, we present a universal attack that, for any potential user query, influences the response to cause a denial-of-service in the VD-RAG system. We investigate the two attack objectives under both white-box and black-box assumptions, employing a multi-objective gradient-based optimization approach as well as prompting state-of-the-art generative models. Using two visual document datasets, a diverse set of state-of-the-art retrievers (embedding models) and generators (vision language models), we show VD-RAG is vulnerable to poisoning attacks in both the targeted and universal settings, yet demonstrating robustness to black-box attacks in the universal setting.

</details>

### 75. Poisoned-MRAG: Knowledge Poisoning Attacks to Multimodal Retrieval Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2503.06254)　📅 2025-03

**关键词**：`attack`、`MRAG`、`knowledge poisoning`、`image-text entry`

👤 **作者**：Yinuo Liu、…、Neil Zhenqiang Gong

- 🎯 **研究动机**：多模态 RAG 的知识投毒攻击未被研究
- 🔬 **研究方法**：将攻击形式化为优化问题，提出 dirty-label 与 clean-label 两种跨模态策略，向多模态知识库注入少量恶意图文对
- 📌 **结论**：InfoSeek 库（481782 对）注入 5 对即达最高 98% ASR；四种防御均效果有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal retrieval-augmented generation (RAG) enhances the visual reasoning capability of vision-language models (VLMs) by dynamically accessing information from external knowledge bases. In this work, we introduce \textit{Poisoned-MRAG}, the first knowledge poisoning attack on multimodal RAG systems. Poisoned-MRAG injects a few carefully crafted image-text pairs into the multimodal knowledge database, manipulating VLMs to generate the attacker-desired response to a target query. Specifically, we formalize the attack as an optimization problem and propose two cross-modal attack strategies, dirty-label and clean-label, tailored to the attacker's knowledge and goals. Our extensive experiments across multiple knowledge databases and VLMs show that Poisoned-MRAG outperforms existing methods, achieving up to 98\% attack success rate with just five malicious image-text pairs injected into the InfoSeek database (481,782 pairs). Additionally, We evaluate 4 different defense strategies, including paraphrasing, duplicate removal, structure-driven mitigation, and purification, demonstrating their limited effectiveness and trade-offs against Poisoned-MRAG. Our results highlight the effectiveness and scalability of Poisoned-MRAG, underscoring its potential as a significant threat to multimodal RAG systems.

</details>

### 76. PoisonedEye: Knowledge Poisoning Attack on RAG-based LVLMs

🌐 [Project](https://proceedings.mlr.press/v267/zhang25da.html)　📅 2025　🏷 ICML 2025

**关键词**：`attack`、`RAG-based LVLM`、`single poison`、`target／class attack`

👤 **作者**：Chenyang Zhang、Xiaoyu Zhang、Jian Lou、Kai Wu、Zilong Wang、Xiaofeng Chen

- 🎯 **研究动机**：VLRAG 依赖外部多模态知识库，面临投毒攻击但无针对性攻击研究
- 🔬 **研究方法**：PoisonedEye 首个 VLRAG 知识投毒攻击：仅注入一个毒样本即操纵目标查询响应，按检索与生成两关键性质求解；另提出扩展到整类查询的类查询定向投毒
- 📌 **结论**：多查询数据集、检索器与 LVLM 上攻击高效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Retrieval-Augmented Generation (VLRAG) systems have been widely applied to Large Vision-Language Models (LVLMs) to enhance their generation ability. However, the reliance on external multimodal knowledge databases renders VLRAG systems vulnerable to malicious poisoning attacks. In this paper, we introduce PoisonedEye, the first knowledge poisoning attack designed for VLRAG systems. Our attack successfully manipulates the response of the VLRAG system for the target query by injecting only one poison sample into the knowledge database. To construct the poison sample, we follow two key properties for the retrieval and generation process, and identify the solution by satisfying these properties. Besides, we also introduce a class query targeted poisoning attack, a more generalized strategy that extends the poisoning effect to an entire class of target queries. Extensive experiments on multiple query datasets, retrievers, and LVLMs demonstrate that our attack is highly effective in compromising VLRAG systems.

</details>

### 77. Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2501.16902)　📅 2025-01

**关键词**：`attack`、`visual retriever`、`pixel poisoning`、`screenshot corpus`

👤 **作者**：Shengyao Zhuang、Ekaterina Khramtsova、Xueguang Ma、Bevan Koopman、Jimmy Lin、Guido Zuccon

- 🎯 **研究动机**：DSE、ColPali 等基于文档截图的视觉检索器脆弱性未评估
- 🔬 **研究方法**：提出三种 pixel poisoning 攻击方法，向检索语料注入对抗截图
- 📌 **结论**：单张对抗截图即可污染 DSE 41.9%、ColPali 26.4% 查询的 top-10，显著高于文本检索器；定向已知 query 可达完全成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in dense retrieval have introduced vision-language model (VLM)-based retrievers, such as DSE and ColPali, which leverage document screenshots embedded as vectors to enable effective search and offer a simplified pipeline over traditional text-only methods. In this study, we propose three pixel poisoning attack methods designed to compromise VLM-based retrievers and evaluate their effectiveness under various attack settings and parameter configurations. Our empirical results demonstrate that injecting even a single adversarial screenshot into the retrieval corpus can significantly disrupt search results, poisoning the top-10 retrieved documents for 41.9% of queries in the case of DSE and 26.4% for ColPali. These vulnerability rates notably exceed those observed with equivalent attacks on text-only retrievers. Moreover, when targeting a small set of known queries, the attack success rate raises, achieving complete success in certain cases. By exposing the vulnerabilities inherent in vision-language models, this work highlights the potential risks associated with their deployment.

</details>

### 78. Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents

📄 [arXiv](https://arxiv.org/abs/2607.15657)　📅 2026-07

**关键词**：`attack`、`multimodal memory`、`imperceptible perturbation`、`black-box attack`、`Lucid`、`long-term memory`

👤 **作者**：Halima Bouzidi、Mboutidem Ekemini Mkpong、Mohammad Abdullah Al Faruque

- 🎯 **研究动机**：多模态 agent 无条件信任视觉数据，图像即可成为严格图像边界威胁模型下的攻击载体
- 🔬 **研究方法**：提出 Lucid 黑盒对抗框架：仅对图像加不可感知扰动，实现上下文内记忆投毒（有历史文本强化时替换良性图）与上下文外记忆注入（无文本矫正时诱导生成）
- 📌 **结论**：跨五个黑盒记忆架构（图结构、LLM 摘要、商用系统）投毒 ASR 61.6%、注入 58.4%，暴露多模态记忆管线结构漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

</details>

### 79. MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents

📄 [arXiv](https://arxiv.org/abs/2606.10742)　📅 2026-06

**关键词**：`attack`、`multimodal memory`、`graph memory`、`triggered retrieval`、`web agent`、`persistent retrieval`

👤 **作者**：Yv Zhang、…、Yaowei Wang

- 🎯 **研究动机**：web agent 图结构外部记忆可被持久检索，恶意内容注入记忆后被反复召回影响行为，多模态记忆投毒被忽视
- 🔬 **研究方法**：提出 MemVenom 黑盒框架两阶段攻击：触发条件化检索保证恶意记忆高概率召回，检索后用对抗扰动+隐蔽 OCR 注入覆盖用户目标，无需改参数或重优化
- 📌 **结论**：多个 agent 框架与 VLM 上端到端攻击成功率高，GPT-5 系 web agent 上达 99.15%，且跨架构与规模迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

</details>

### 80. Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning

📄 [arXiv](https://arxiv.org/abs/2604.16966) · 🎓 [Official](https://aclanthology.org/2026.acl-long.954/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`multimodal memory`、`recommender agent`、`visual trigger`、`multimodal safety`、`agent safety`

👤 **作者**：Jiachen Qian

- 🎯 **研究动机**：Agentic RecSys 依赖长期记忆 LTM，用户上传图像可成为记忆投毒入口
- 🔬 **研究方法**：Visual Inception 在用户图像注入触发器作为记忆中的沉睡者，规划时被检索即劫持推理链，无需 prompt 注入；配套双过程防御 CognitiveGuard（扩散净化加反事实验证）
- 📌 **结论**：攻击 GHR 约 85%，CognitiveGuard 降至约 10%，延迟按模式 1.5-6.5 秒且不降质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The evolution from static ranking models to Agentic Recommender Systems (Agentic RecSys) empowers AI agents to maintain long-term user profiles and autonomously plan service tasks. While this paradigm shift enhances personalization, it introduces a vulnerability: reliance on Long-term Memory (LTM). In this paper, we uncover a threat termed "Visual Inception." Unlike traditional adversarial attacks that seek immediate misclassification, Visual Inception injects triggers into user-uploaded images (e.g., lifestyle photos) that act as "sleeper agents" within the system's memory. When retrieved during future planning, these poisoned memories hijack the agent's reasoning chain, steering it toward adversary-defined goals (e.g., promoting high-margin products) without prompt injection. To mitigate this, we propose CognitiveGuard, a dual-process defense framework inspired by human cognition. It consists of a System 1 Perceptual Sanitizer (diffusion-based purification) to cleanse sensory inputs and a System 2 Reasoning Verifier (counterfactual consistency checks) to detect anomalies in memory-driven planning. Extensive experiments on a mock e-commerce agent environment demonstrate that Visual Inception achieves about 85% Goal-Hit Rate (GHR), while CognitiveGuard reduces this risk to around 10% with configurable latency trade-offs (about 1.5s in lite mode to about 6.5s for full sequential verification), without quality degradation under our setup.

</details>

### 81. SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents

📄 [arXiv](https://arxiv.org/abs/2603.08316) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5078)　📅 2026-03　🏷 ECCV 2026

**关键词**：`attack`、`GUI-agent DoS`、`efficiency backdoor`、`popup trigger`、`GUI agent`、`resource exhaustion`

👤 **作者**：Junxian Li、Tu Lan、Haozhen Tan、Yan Meng、Haojin Zhu

- 🎯 **研究动机**：GUI agent 安全研究只关注动作正确性，响应效率维度的风险未被探索
- 🔬 **研究方法**：SlowBA 两阶段奖励级后门注入：先对齐长回复格式，再经 RL 学触发感知激活；用 GUI 环境中自然出现的弹窗作隐蔽触发器
- 📌 **结论**：显著拉长回复与延迟而基本保持任务准确率，低投毒率与多种防御设定下攻击仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on manipulating action correctness, the security risks related to response efficiency remain largely unexplored. In this paper, we introduce SlowBA, a novel backdoor attack that targets the responsiveness of VLM-based GUI agents. The key idea is to manipulate response latency by inducing excessively long reasoning chains under specific trigger patterns. To achieve this, we propose a two-stage reward-level backdoor injection (RBI) strategy that first aligns the long-response format and then learns trigger-aware activation through reinforcement learning. In addition, we design realistic pop-up windows as triggers that naturally appear in GUI environments, improving the stealthiness of the attack. Extensive experiments across multiple datasets and baselines demonstrate that SlowBA can significantly increase response length and latency while largely preserving task accuracy. The attack remains effective even with a small poisoning ratio and under several defense settings. These findings reveal a previously overlooked security vulnerability in GUI agents and highlight the need for defenses that consider both action correctness and response efficiency. Code can be found in https://github.com/tu-tuing/SlowBA.

</details>

### 82. AdapAction: Adaptive Target Action Backdoor Attack against GUI Agents

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_AdapAction_Adaptive_Target_Action_Backdoor_Attack_against_GUI_Agents_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`attack`、`GUI agent`、`adaptive action`、`context-aware policy`、`action backdoor`、`adaptive trigger`

👤 **作者**：Baicheng Chen、Mingda Zhang、Min Zhang、Haizhou Li、Baoyuan Wu

- 🎯 **研究动机**：现有 GUI Agent 后门依赖静态触发-动作映射执行固定上下文无关行为，易被检测
- 🔬 **研究方法**：提出 AdapAction：嵌入自适应上下文感知策略，使 Agent 依据当前 GUI 状态与用户指令自主选择环境一致的恶意动作，保持功能效用同时隐匿
- 📌 **结论**：在 AitZ 与 AndroidControl 上 ASR 最高 100% 且良性效用保持；能持续逃过评估指令对齐、视觉连贯与安全的多原则 LLM 防御，而固定动作攻击易被查出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) are increasingly vital for complex task automation. However, their capacity for self-driven decision-making introduces significant, yet underexplored, security risks, among which backdoor attacks pose a particularly stealthy and high-impact threat. Prior work has shown GUI agents vulnerable to such attacks, but existing methods rely on static trigger-action mappings that execute fixed, context-agnostic behaviors, making them highly detectable. To address this limitation, we introduce **AdapAction**, a novel backdoor attack that subverts the agent's decision-making by embedding an **adaptive, context-aware policy**. Unlike traditional approaches, AdapAction enables the agent to autonomously select environmentally coherent malicious actions based on the current GUI state and user instruction, thereby evading detection while preserving functional utility. Extensive experiments on the Android-In-The-Zoo (AitZ) and AndroidControl benchmarks show that AdapAction achieves up to 100% Attack Success Rate (ASR) while preserving benign task utility. More critically, AdapAction consistently evades a multi-principle-based LLM defense evaluating instruction alignment, visual coherence, and safety, whereas traditional fixed-action attacks are easily detected. This resilience stems from AdapAction's contextually grounded malicious actions, which are semantically and visually indistinguishable from legitimate operations. As a result, AdapAction exhibits exceptional stealth and poses a significantly greater real-world threat to LLM-powered GUI agents.

</details>

### 83. Chain-of-Trigger: An Agentic Backdoor that Paradoxically Enhances Agentic Robustness

📄 [arXiv](https://arxiv.org/abs/2510.08238)　📅 2025-10

**关键词**：`attack`、`CoTri`、`ordered trigger chain`、`long-horizon agent`

👤 **作者**：Jiyang Qiu、Xinbei Ma、Yunqing Xu、Zhuosheng Zhang、Hai Zhao

- 🎯 **研究动机**：传统后门限于单步控制，长程 agent 需要多步操纵的新型后门
- 🔬 **研究方法**：提出 Chain-of-Trigger：有序触发链，首个触发器启动、后续触发器从环境提取，逐步把 agent 带离原任务
- 📌 **结论**：ASR 近完美且误触发率近零；因训练数据建模环境随机性，植入后门反而提升良性任务性能与抗干扰鲁棒性，使攻击更隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid deployment of large language model (LLM)-based agents in real-world applications has raised serious concerns about their trustworthiness. In this work, we reveal the security and robustness vulnerabilities of these agents through backdoor attacks. Distinct from traditional backdoors limited to single-step control, we propose the Chain-of-Trigger Backdoor (CoTri), a multi-step backdoor attack designed for long-horizon agentic control. CoTri relies on an ordered sequence. It starts with an initial trigger, and subsequent ones are drawn from the environment, allowing multi-step manipulation that diverts the agent from its intended task. Experimental results show that CoTri achieves a near-perfect attack success rate (ASR) while maintaining a near-zero false trigger rate (FTR). Due to training data modeling the stochastic nature of the environment, the implantation of CoTri paradoxically enhances the agent's performance on benign tasks and even improves its robustness against environmental distractions. We further validate CoTri on vision-language models (VLMs), confirming its scalability to multimodal agents. Our work highlights that CoTri achieves stable, multi-step control within agents, improving their inherent robustness and task capabilities, which ultimately makes the attack more stealthy and raises potential safty risks.

</details>

### 84. VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation

📄 [arXiv](https://arxiv.org/abs/2507.06899) · 📝 [OpenReview](https://openreview.net/forum?id=7HPuAkgdVm)　📅 2025-07　🏷 COLM 2025

**关键词**：`attack`、`GUI agent`、`visual grounding`、`click hijacking`

👤 **作者**：Ziang Ye、Yang Zhang、Wentao Shi、Xiaoyu You、Fuli Feng、Tat-Seng Chua

- 🎯 **研究动机**：GUI agent 视觉定位（文本计划到界面元素的映射）环节的漏洞未被探索
- 🔬 **研究方法**：提出 VisualTrap：在视觉定位预训练阶段注入毒数据，把计划诱骗定位到触发位置而非预期目标
- 📌 **结论**：仅 5% 毒数据加人眼不可见触发器即可劫持定位，且可跨下游任务、干净微调与 GUI 环境（移动到桌面）泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graphical User Interface (GUI) agents powered by Large Vision-Language Models (LVLMs) have emerged as a revolutionary approach to automating human-machine interactions, capable of autonomously operating personal devices (e.g., mobile phones) or applications within the device to perform complex real-world tasks in a human-like manner. However, their close integration with personal devices raises significant security concerns, with many threats, including backdoor attacks, remaining largely unexplored. This work reveals that the visual grounding of GUI agent-mapping textual plans to GUI elements-can introduce vulnerabilities, enabling new types of backdoor attacks. With backdoor attack targeting visual grounding, the agent's behavior can be compromised even when given correct task-solving plans. To validate this vulnerability, we propose VisualTrap, a method that can hijack the grounding by misleading the agent to locate textual plans to trigger locations instead of the intended targets. VisualTrap uses the common method of injecting poisoned data for attacks, and does so during the pre-training of visual grounding to ensure practical feasibility of attacking. Empirical results show that VisualTrap can effectively hijack visual grounding with as little as 5% poisoned data and highly stealthy visual triggers (invisible to the human eye); and the attack can be generalized to downstream tasks, even after clean fine-tuning. Moreover, the injected trigger can remain effective across different GUI environments, e.g., being trained on mobile/web and generalizing to desktop environments. These findings underscore the urgent need for further research on backdoor attack risks in GUI agents.

</details>

### 85. Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents

📄 [arXiv](https://arxiv.org/abs/2506.13205)　📅 2025-06

**关键词**：`attack`、`VIBMA`、`clean-text`、`mobile agent`

👤 **作者**：Xuan Wang、…、Ee-Chien Chang

- 🎯 **研究动机**：VLM 移动 agent 以小规模用户数据微调，易受隐蔽训练期威胁
- 🔬 **研究方法**：提出 VIBMA 首个 clean-text 后门：仅修改视觉输入保持文本正常，把毒样本训练梯度对齐到目标实例，含静态补丁、动态运动与低透明度三类触发器
- 📌 **结论**：六个 Android 应用与三个移动 VLM 上 ASR 达 94.67%，干净任务成功率保持 95.85%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile agents powered by vision-language models (VLMs) are increasingly adopted for tasks such as UI automation and camera-based assistance. These agents are typically fine-tuned using small-scale, user-collected data, making them susceptible to stealthy training-time threats. This work introduces VIBMA, the first clean-text backdoor attack targeting VLM-based mobile agents. The attack injects malicious behaviors into the model by modifying only the visual input while preserving textual prompts and instructions, achieving stealth through the complete absence of textual anomalies. Once the agent is fine-tuned on this poisoned data, adding a predefined visual pattern (trigger) at inference time activates the attacker-specified behavior (backdoor). Our attack aligns the training gradients of poisoned samples with those of an attacker-specified target instance, effectively embedding backdoor-specific features into the poisoned data. To ensure the robustness and stealthiness of the attack, we design three trigger variants that better resemble real-world scenarios: static patches, dynamic motion patterns, and low-opacity blended content. Extensive experiments on six Android applications and three mobile-compatible VLMs demonstrate that our attack achieves high success rates (ASR up to 94.67%) while preserving clean-task behavior (FSR up to 95.85%). We further conduct ablation studies to understand how key design factors impact attack reliability and stealth. These findings is the first to reveal the security vulnerabilities of mobile agents and their susceptibility to backdoor injection, underscoring the need for robust defenses in mobile agent adaptation pipelines.

</details>

### 86. Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents

📄 [arXiv](https://arxiv.org/abs/2505.14418) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.411/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`AgentGhost`、`interaction trigger`、`mobile GUI`

👤 **作者**：Pengzhou Cheng、…、Gongshen Liu

- 🎯 **研究动机**：MLLM 驱动的 GUI agent 依赖开源模型或 API，其供应链后门威胁未被探索
- 🔬 **研究方法**：提出 AgentGhost，组合目标级与交互级复合触发器，以 Min-Max 优化融合监督对比学习与 SFT 注入后门
- 📌 **结论**：两个移动基准上三类攻击目标精度达 99.7% 且效用仅降 1%，配套防御可降至 22.1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graphical user interface (GUI) agents powered by multimodal large language models (MLLMs) have shown greater promise for human-interaction. However, due to the high fine-tuning cost, users often rely on open-source GUI agents or APIs offered by AI providers, which introduces a critical but underexplored supply chain threat: backdoor attacks. In this work, we first unveil that MLLM-powered GUI agents naturally expose multiple interaction-level triggers, such as historical steps, environment states, and task progress. Based on this observation, we introduce AgentGhost, an effective and stealthy framework for red-teaming backdoor attacks. Specifically, we first construct composite triggers by combining goal and interaction levels, allowing GUI agents to unintentionally activate backdoors while ensuring task utility. Then, we formulate backdoor injection as a Min-Max optimization problem that uses supervised contrastive learning to maximize the feature difference across sample classes at the representation space, improving flexibility of the backdoor. Meanwhile, it adopts supervised fine-tuning to minimize the discrepancy between backdoor and clean behavior generation, enhancing effectiveness and utility. Extensive evaluations of various agent models in two established mobile benchmarks show that AgentGhost is effective and generic, with attack accuracy that reaches 99.7\% on three attack objectives, and shows stealthiness with only 1\% utility degradation. Furthermore, we tailor a defense method against AgentGhost that reduces the attack accuracy to 22.1\%. Our code is available at \texttt{anonymous}.

</details>

### 87. A Closer Look at Backdoor Attacks on CLIP

🌐 [Project](https://proceedings.mlr.press/v267/he25v.html)　📅 2025-07　🏷 ICML 2025

**关键词**：`analysis／defense`、`component decomposition`、`attention head`、`MLP`

👤 **作者**：Shuo He、Zhifang Zhang、Feng Liu、Roy Ka-Wei Lee、Bo An、Lei Feng

- 🎯 **研究动机**：后门攻击如何影响 CLIP 内部组件缺乏系统实证，阻碍针对性防御设计
- 🔬 **研究方法**：把图像表征分解为各 patch、attention head（AH）与 MLP 之和，考察不同后门对组件的感染模式；发现局部 patch 型后门主要感染集中于最后一层的 AH，全局扰动型主要感染散布于多个后层的 MLP，且并非所有末层 AH 被感染
- 📌 **结论**：据此提出推理期检测感染 AH、修复其表征或过滤感染过多的样本，实验验证经验发现与防御有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present a comprehensive empirical study on how backdoor attacks affect CLIP by analyzing the representations of backdoor images. Specifically, based on the methodology of representation decomposing, image representations can be decomposed into a sum of representations across individual image patches, attention heads (AHs), and multi-layer perceptrons (MLPs) in different model layers. By examining the effect of backdoor attacks on model components, we have the following empirical findings. (1) Different backdoor attacks would infect different model components, i.e., local patch-based backdoor attacks mainly affect AHs, while global perturbation-based backdoor attacks mainly affect MLPs. (2) Infected AHs are centered on the last layer, while infected MLPs are decentralized on several late layers. (3) Not all AHs in the last layer are infected and even some AHs could still maintain the original property-specific roles (e.g., ”color" and ”location”). These observations motivate us to defend against backdoor attacks by detecting infected AHs, repairing their representations, or filtering backdoor samples with too many infected AHs, in the inference stage. Experimental results validate our empirical findings and demonstrate the effectiveness of the defense methods.

</details>

### 88. Breaking the False Sense of Security in Backdoor Defense through Re-Activation Attack

📄 [arXiv](https://arxiv.org/abs/2405.16134) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d06537b4b38ccf008a54559d2c56fa23-Abstract-Conference.html)　📅 2024-05　🏷 NeurIPS 2024

**关键词**：`attack analysis`、`reactivation`、`post-training defense`、`CLIP`

👤 **作者**：Mingli Zhu、Siyuan Liang、Baoyuan Wu

- 🎯 **研究动机**：后门防御降低 ASR 后，后门是否真正被消除存疑
- 🔬 **研究方法**：提出 backdoor existence coefficient 度量防御模型中的休眠后门，用通用对抗扰动微调原触发器再激活，并扩展黑盒 query/transfer 攻击
- 📌 **结论**：训练后防御只是让后门休眠而非消除，图像分类与 CLIP 上均可被轻易再激活

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks face persistent challenges in defending against backdoor attacks, leading to an ongoing battle between attacks and defenses. While existing backdoor defense strategies have shown promising performance on reducing attack success rates, can we confidently claim that the backdoor threat has truly been eliminated from the model? To address it, we re-investigate the characteristics of the backdoored models after defense (denoted as defense models). Surprisingly, we find that the original backdoors still exist in defense models derived from existing post-training defense strategies, and the backdoor existence is measured by a novel metric called backdoor existence coefficient. It implies that the backdoors just lie dormant rather than being eliminated. To further verify this finding, we empirically show that these dormant backdoors can be easily re-activated during inference, by manipulating the original trigger with well-designed tiny perturbation using universal adversarial attack. More practically, we extend our backdoor reactivation to black-box scenario, where the defense model can only be queried by the adversary during inference, and develop two effective methods, i.e., query-based and transfer-based backdoor re-activation attacks. The effectiveness of the proposed methods are verified on both image classification and multimodal contrastive learning (i.e., CLIP) tasks. In conclusion, this work uncovers a critical vulnerability that has never been explored in existing defense strategies, emphasizing the urgency of designing more robust and advanced backdoor defense mechanisms in the future.

</details>

### 89. Effective Backdoor Mitigation in Vision-Language Models Depends on the Pre-training Objective

📄 [arXiv](https://arxiv.org/abs/2311.14948) · 📝 [OpenReview](https://openreview.net/forum?id=cSimKw5p6R)　📅 2023-11

**关键词**：`analysis／defense`、`objective dependence`、`CLIP／SigLIP`、`mitigation`

👤 **作者**：Sahil Verma、…、Jeff Bilmes

- 🎯 **研究动机**：CleanCLIP 等后门缓解方法的有效性是否依赖预训练目标未经检验
- 🔬 **研究方法**：在 CC3M/CC6M 上以不同预训练目标训练多模态模型，再用 CleanCLIP 做毒物清除
- 📌 **结论**：更强的预训练目标对应更难移除的后门；CleanCLIP 即使充分调参也无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the advanced capabilities of contemporary machine learning (ML) models, they remain vulnerable to adversarial and backdoor attacks. This vulnerability is particularly concerning in real-world deployments, where compromised models may exhibit unpredictable behavior in critical scenarios. Such risks are heightened by the prevalent practice of collecting massive, internet-sourced datasets for training multimodal models, as these datasets may harbor backdoors. Various techniques have been proposed to mitigate the effects of backdooring in multimodal models, such as CleanCLIP, which is the current state-of-the-art approach. In this work, we demonstrate that the efficacy of CleanCLIP in mitigating backdoors is highly dependent on the particular objective used during model pre-training. We observe that stronger pre-training objectives that lead to higher zero-shot classification performance correlate with harder to remove backdoors behaviors. We show this by training multimodal models on two large datasets consisting of 3 million (CC3M) and 6 million (CC6M) datapoints, under various pre-training objectives, followed by poison removal using CleanCLIP. We find that CleanCLIP, even with extensive hyperparameter tuning, is ineffective in poison removal when stronger pre-training objectives are used. Our findings underscore critical considerations for ML practitioners who train models using large-scale web-curated data and are concerned about potential backdoor threats.

</details>

### 90. Pick your Poison: Undetectability versus Robustness in Data Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2305.09671)　📅 2023-05

**关键词**：`analysis／defense`、`CLIP`、`undetectability–robustness trade-off`、`trusted data`

👤 **作者**：Nils Lukas、Florian Kerschbaum

- 🎯 **研究动机**：投毒攻防评估只看修复或检测，忽略攻击者须同时兼顾不可检测性与鲁棒性的内在权衡
- 🔬 **研究方法**：揭示 over/under-poisoning 权衡，提出用少量可信 image-label pair 的检测与修复双防御并扩展至 CLIP
- 📌 **结论**：仅 1% 干净数据即可缓解全部测试攻击，CIFAR-10 精度最多降 2%、ImageNet 降 2.5%；能控参数的攻击者威胁更大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep image classification models trained on vast amounts of web-scraped data are susceptible to data poisoning - a mechanism for backdooring models. A small number of poisoned samples seen during training can severely undermine a model's integrity during inference. Existing work considers an effective defense as one that either (i) restores a model's integrity through repair or (ii) detects an attack. We argue that this approach overlooks a crucial trade-off: Attackers can increase robustness at the expense of detectability (over-poisoning) or decrease detectability at the cost of robustness (under-poisoning). In practice, attacks should remain both undetectable and robust. Detectable but robust attacks draw human attention and rigorous model evaluation or cause the model to be re-trained or discarded. In contrast, attacks that are undetectable but lack robustness can be repaired with minimal impact on model accuracy. Our research points to intrinsic flaws in current attack evaluation methods and raises the bar for all data poisoning attackers who must delicately balance this trade-off to remain robust and undetectable. To demonstrate the existence of more potent defenders, we propose defenses designed to (i) detect or (ii) repair poisoned models using a limited amount of trusted image-label pairs. Our results show that an attacker who needs to be robust and undetectable is substantially less threatening. Our defenses mitigate all tested attacks with a maximum accuracy decline of 2% using only 1% of clean data on CIFAR-10 and 2.5% on ImageNet. We demonstrate the scalability of our defenses by evaluating large vision-language models, such as CLIP. Attackers who can manipulate the model's parameters pose an elevated risk as they can achieve higher robustness at low detectability compared to data poisoning attackers.

</details>

### 91. Evolving Safety Landscape of Multi-modal Large Language Models: A Survey of Emerging Threats and Safeguards

📄 [arXiv](https://arxiv.org/abs/2608.07535)　📅 2026-07

**关键词**：`broad survey`、`MLLM safety`、`data poisoning`、`multimodal threat shift`

👤 **作者**：Xi Li、…、Jiaqi Wang

- 🎯 **研究动机**：多模态架构通过模态对齐与融合重塑安全图景，单模态假设下的威胁模型与防御框架不再适用
- 🔬 **研究方法**：提出多模态接地的安全威胁分类（对抗攻击、数据投毒、越狱、幻觉），分析威胁模型偏移并按新安全假设组织防御进展
- 📌 **结论**：模态整合被攻陷、模态失配与融合风险成为新威胁类别，需要更原则化、可扩展的多模态安全机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language models (MLLMs) integrate heterogeneous modalities through modality alignment and fusion, enabling stronger understanding and reasoning. However, this architectural shift reshapes the safety landscape of machine learning. Increased model complexity and cross-modal interactions give rise to novel threats, including compromised modality integration, modality misalignment, and fused safety risks, reflecting shifts in threat modeling beyond uni-modal assumptions. These shifts, in turn, impose new constraints on safety solutions not captured by existing frameworks rooted in uni-modal learning. Motivated by these challenges, this survey provides a systematic analysis of the evolving safety landscape of MLLMs. We first propose a multimodal grounded taxonomy of safety threats and analyze shifts in threat models, covering adversarial attacks, data poisoning, jailbreaks, and hallucinations. We then summarize updated safety assumptions and organize recent advances in MLLM safety strategies accordingly. Finally, we discuss open challenges and future directions to inform the development of more principled and scalable safety mechanisms for multimodal systems.

</details>

### 92. Meta-Research on Backdoors: Dataset and Threat Model Shifts in Multimodal Backdoor Attacks

🌐 [Project](https://doi.org/10.20944/preprints202604.0433.v1)　📅 2026-04

**关键词**：`meta-research`、`dataset shift`、`threat model`、`reproducibility`

- 🎯 **研究动机**：多模态后门文献的数据集、攻击能力与指标不统一，结果难比较
- 🔬 **研究方法**：对文献做meta-research梳理dataset与threat model漂移
- 📌 **结论**：主张建立向后兼容benchmark与统一threat model

### 93. A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends

📄 [arXiv](https://arxiv.org/abs/2407.07403)　📅 2024-07

**关键词**：`broad survey`、`LVLM attacks`、`poisoning／backdoor`、`resources`

👤 **作者**：Daizong Liu、Mingyu Yang、Xiaoye Qu、Pan Zhou、Yu Cheng、Wei Hu

- 🎯 **研究动机**：LVLM 攻击研究分散，缺乏系统性综述与资源整合
- 🔬 **研究方法**：按对抗攻击、越狱、prompt injection、数据投毒等类别梳理攻击方法、资源与挑战
- 📌 **结论**：给出未来方向并维护持续更新的 LVLM 攻击论文仓库

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the significant development of large models in recent years, Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities across a wide range of multimodal understanding and reasoning tasks. Compared to traditional Large Language Models (LLMs), LVLMs present great potential and challenges due to its closer proximity to the multi-resource real-world applications and the complexity of multi-modal processing. However, the vulnerability of LVLMs is relatively underexplored, posing potential security risks in daily usage. In this paper, we provide a comprehensive review of the various forms of existing LVLM attacks. Specifically, we first introduce the background of attacks targeting LVLMs, including the attack preliminary, attack challenges, and attack resources. Then, we systematically review the development of LVLM attack methods, such as adversarial attacks that manipulate model outputs, jailbreak attacks that exploit model vulnerabilities for unauthorized actions, prompt injection attacks that engineer the prompt type and pattern, and data poisoning that affects model training. Finally, we discuss promising research directions in the future. We believe that our survey provides insights into the current landscape of LVLM vulnerabilities, inspiring more researchers to explore and mitigate potential safety issues in LVLM developments. The latest papers on LVLM attacks are continuously collected in https://github.com/liudaizong/Awesome-LVLM-Attack.

</details>

### 94. FreqDoor: A Hidden Trojan in the Frequency Domain for Backdoor Attacks on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2609.07048)　📅 2026-09

**关键词**：`attack`、`backdoor`、`frequency-domain trigger`、`vision-language model`

👤 **作者**：Yasir Arafat Prodhan、Sadad Hasan、Mohammed Imamul Hassan Bhuiyan

- 🎯 **研究动机**：VLM 后门触发器多为空间/文本/双模态，易被定位或识别
- 🔬 **研究方法**：FreqDoor 频域触发：混合触发图幅度谱并保留干净图相位，生成空间分散且视觉不可见的触发，不改文本输入
- 📌 **结论**：BLIP-2/InstructBLIP/LLaVA 在 Flickr8k captioning ASR 99.6/99.8/98.4%，VQAv2 上 79.6-99.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) have recently shown excellent progress in open-ended image-to-text generation. However, their multimodal nature makes them persistently vulnerable to backdoor attacks. Existing backdoor triggers for VLMs are either spatial, textual, or bimodal, which may yield localized or recognizable trigger patterns. In this work, we explore a different attack surface and propose \ textsc {FreqDoor}, a training-time backdoor attack that implants triggers in the frequency domain. \ textsc {FreqDoor} mixes amplitude-spectrum components from a trigger-source image selectively while preserving the phase of a clean image to generate a spatially distributed and visually imperceptible trigger without modifying the textual input. We evaluate the attack on BLIP-2, InstructBLIP, and LLaVA for image captioning and visual question answering. On Flickr8k, \ textsc {FreqDoor} achieves attack success rates of $99.6\%$, $99.8\%$, and $98.4\%$ on the three models, respectively, while preserving the semantic quality of the generated captions. On VQAv2, the corresponding attack success rates are $99.6\%$, $92.4\%$, and $79.6\%$.

</details>
