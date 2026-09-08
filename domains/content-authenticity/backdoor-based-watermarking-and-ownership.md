# 后门式水印、版权保护与所有权验证

[返回 Content Authenticity 目录](README.md) · [返回投毒与后门目录](../poison-and-backdoor/README.md)

## 研究方向

本页单独整理使用 backdoor-like conditional behavior、触发器或模型内部持久信号来进行版权保护、内容保护、授权控制、模型所有权验证和未授权数据使用验证的工作，也收录专门攻击这些保护机制的后门。它们的实现机制与恶意模型后门相似，但研究目标是证明来源、限制未授权使用或评估水印系统的攻击面。

这里的“后门式水印”是机制描述，不等同于恶意后门：只有以版权、来源、授权或所有权验证为主要问题的工作才进入本页。普通恶意投毒与后门仍归入 [模型投毒与后门](../poison-and-backdoor/README.md)；仅把水印作为恶意后门的不可见触发载体、但不攻击水印系统的工作仍留在对应模型页面。

## 研究脉络

- **保护性后门：** 将授权信号、敏感区域或概念绑定到模型内部的条件行为，在未授权编辑、个性化或调用时拒绝生成或破坏输出。
- **模型与数据归属：** 通过 trigger-response、feature-space signal 或黑盒 query 验证模型所有权、训练数据使用和下游微调后的继承关系。
- **鲁棒性与审计：** 关注 fine-tuning、模型提取、输入变换、扰动和自适应规避对验证信号的影响。
- **反制攻击：** 评估攻击者通过后门化组件、数据投毒或检测器规避破坏水印与版权保护链路的能力。

## 防御性后门、授权控制与所有权验证

### 1. GoodDiffusion: Proactive Copyright Protection for Diffusion Generative Models via Learnable Sample-specific Signatures

📄 [arXiv](https://arxiv.org/abs/2606.29759) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60784)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`authorization control`、`sample-specific signature`、`diffusion bridge`、`model ownership`、`diffusion model`

👤 **作者**：Shixi Qin、Zhiyong Yang、Shilong Bao、Zitai Wang、Qianqian Xu、Qingming Huang

- 🎯 **研究动机**：已有版权保护多为事后归因或仅降质的防御，无法切断扩散桥模型的未授权使用
- 🔬 **研究方法**：提出 GoodDiffusion：借鉴后门机制把授权内化为生成过程，携带有效签名的查询高质量生成、未授权输入拒绝生成；理论证明静态签名可被梯度优化恢复，故引入输入条件化的 Learnable Signature Network 打破签名普适性
- 📌 **结论**：有效阻断未授权使用同时保持授权用户生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper tackles the challenging problem of developing a proactive copyright protection mechanism that cuts off unauthorized use of diffusion bridge models. Existing studies largely fall into post-hoc attribution (e.g., watermarking and fingerprinting) or degradation-only defenses, which offer only indirect and limited preventive effects. We therefore propose GoodDiffusion, inspired by backdoor mechanisms, to enforce model-level use-time control by internalizing authorization into the generative process through a selectively permissive, otherwise closed behavior. Specifically, GoodDiffusion preserves high-quality generation for authorized queries carrying valid signatures, yet refuses to generate for unauthorized inputs. We further theoretically show that naive static-signature designs (like conventional backdoor injection) are fundamentally fragile, since a surrogate signature can be efficiently recovered via gradient-based optimization. To strengthen security, we introduce a Learnable Signature Network (LSN) that assigns sample-specific signatures conditioned on each input. This breaks the universality of signatures and prevents a surrogate from transferring across inputs. Extensive experiments validate that GoodDiffusion effectively blocks unauthorized use while maintaining strong generation quality for authorized users.

</details>

### 2. Cert-LAS: Toward Certified Model Ownership Verification for Text-to-Image Diffusion Models via Layer-Adaptive Smoothing

📄 [arXiv](https://arxiv.org/abs/2605.29809) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64693)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`ownership verification`、`certified watermark`、`layer-adaptive smoothing`、`model ownership`、`certified robustness`

👤 **作者**：Leyi Qi、Yiming Li、Siyuan Liang、Zhengzhong Tu、Dacheng Tao

- 🎯 **研究动机**：现有后门水印隐式假设验证过程忠实，对手可破坏水印信号使验证失效
- 🔬 **研究方法**：Cert-LAS 首个认证式 T2I 所有权验证：扩散分类器与 LFS 引导的层自适应噪声嵌入水印，经假设检验对比无水印参照，并证明恶意移除攻击下仍可可靠验证
- 📌 **结论**：实验验证有效并抵抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-scale text-to-image (T2I) diffusion models have enabled unprecedented creative applications, but their unauthorized use has raised serious intellectual property concerns, making model ownership verification (MOV) increasingly critical. We find that existing backdoor-based diffusion watermarking methods often (implicitly) assume a "faithful" verification process, namely, that the verifier can query a suspicious model and obtain the faithful watermark response to complete MOV. However, in practice, adversaries may intentionally or unintentionally damage potential watermark signals, significantly degrading verification reliability. To address this issue, we propose Cert-LAS, the first certified MOV method for T2I models based on layer-adaptive smoothing. In general, Cert-LAS embeds specified watermarks using diffusion classifiers and an LFS-guided layer-adaptive noise, and verifies ownership by examining whether the suspected model exhibits significantly stronger watermark responses compared to unwatermarked references through hypothesis testing. We further prove that, under certain conditions, our Cert-LAS can still achieve reliable verification even in the presence of malicious removal attacks. Extensive experiments validate the effectiveness of Cert-LAS and its resistance to adaptive attacks. Our code is available at https://github.com/Leyi-Qi/Cert-LAS.

</details>

### 3. GuardDoor: Safeguarding Against Malicious Diffusion Editing via Protective Backdoors

📄 [arXiv](https://arxiv.org/abs/2503.03944)　📅 2025-03

**关键词**：`defense`、`protective backdoor`、`image editing`、`imperceptible trigger`

👤 **作者**：Yaopei Zeng、Yuanpu Cao、Lu Lin

- 🎯 **研究动机**：对抗扰动式图像保护易被压缩、加噪等预处理中和
- 🔬 **研究方法**：GuardDoor 由模型提供方微调 image encoder 嵌入保护性后门，图像所有者为图片附加不可感知触发器，未授权编辑即输出无意义结果
- 📌 **结论**：对图像预处理鲁棒且可大规模部署，确立所有者与提供方协作的保护框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing accessibility of diffusion models has revolutionized image editing but also raised significant concerns about unauthorized modifications, such as misinformation and plagiarism. Existing countermeasures largely rely on adversarial perturbations designed to disrupt diffusion model outputs. However, these approaches are found to be easily neutralized by simple image preprocessing techniques, such as compression and noise addition. To address this limitation, we propose GuardDoor, a novel and robust protection mechanism that fosters collaboration between image owners and model providers. Specifically, the model provider participating in the mechanism fine-tunes the image encoder to embed a protective backdoor, allowing image owners to request the attachment of imperceptible triggers to their images. When unauthorized users attempt to edit these protected images with this diffusion model, the model produces meaningless outputs, reducing the risk of malicious image editing. Our method demonstrates enhanced robustness against image preprocessing operations and is scalable for large-scale deployment. This work underscores the potential of cooperative frameworks between model providers and image owners to safeguard digital content in the era of generative AI.

</details>

### 4. PersGuard: Preventing Malicious Personalization in Text-to-Image Diffusion Models via Model Backdoors

📄 [arXiv](https://arxiv.org/abs/2502.16167)　📅 2025-02

**关键词**：`defense`、`personalization protection`、`persistent backdoor`、`copyright`

👤 **作者**：Xinwei Liu、Xiaojun Jia、Yuan Xun、Hua Zhang、Xiaochun Cao

- 🎯 **研究动机**：基于扰动的个性化防护假设全部图像已预扰动，遇未扰动图像或轻微变换即失效
- 🔬 **研究方法**：PersGuard 在模型发布前注入保护性后门：统一优化后门行为、先验保持与后门保持三目标，使受保护图像微调后仍触发保护输出
- 📌 **结论**：灰盒/黑盒、多对象与人脸保护上均优于扰动式方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DMs) have advanced text-to-image (T2I) synthesis, yet their personalization capabilities raise serious privacy and copyright concerns. Malicious actors can misuse these models to generate unauthorized portraits or artistic style replicas. Existing proactive defenses primarily rely on applying adversarial perturbations to reference images to disrupt training. However, these approaches face limitations: they assume all training images are pre-perturbed and are prone to failure when datasets contain unperturbed images or undergo minor data transformations. In this paper, we introduce PersGuard, a novel backdoor-based framework designed to prevent unauthorized personalization of pre-trained T2I diffusion models. Unlike perturbation-based methods, we assume protectors can embed protective backdoors into the models before their release. This mechanism ensures that if a downstream user fine-tunes the model on protected images, the model retains the backdoor and generates predefined protective outputs; conversely, for unprotected images, the backdoor is effectively removed during fine-tuning to ensure normal model utility. We formulate the backdoor injection as a unified optimization problem incorporating three objectives: a backdoor behavior loss to activate protection, a prior preservation loss to maintain standard generation capabilities, and a novel backdoor retention loss. The retention loss is specifically designed to mirror personalization loss, ensuring the backdoor remains robust during downstream fine-tuning. Extensive experiments across gray-box and black-box settings, multi-object protection, and facial identity protection demonstrate that PersGuard provides superior privacy protection compared to existing perturbation-based methods.

</details>

### 5. SleeperMark: Towards Robust Watermark against Fine-Tuning Text-to-image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2412.04852) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SleeperMark_Towards_Robust_Watermark_against_Fine-Tuning_Text-to-image_Diffusion_Models_CVPR_2025_paper.html)　📅 2025　🏷 CVPR 2025

**关键词**：`defense`、`backdoor watermark`、`fine-tuning robustness`、`multi-bit message`

👤 **作者**：Zilan Wang、…、Zhengzhong Tu

- 🎯 **研究动机**：T2I 扩散模型是高价值 IP，被未授权微调后水印知识易被遗忘，现有 IP 保护在黑盒验证加微调场景失效
- 🔬 **研究方法**：提出 SleeperMark：引导模型把水印信息与所学语义概念解耦，使其在适应下游新任务时仍保留嵌入水印
- 📌 **结论**：在 Stable Diffusion 与 DeepFloyd-IF 等模型上对下游微调及图像、模型级攻击均鲁棒，几乎不影响生成能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large-scale text-to-image (T2I) diffusion models have enabled a variety of downstream applications. As T2I models require extensive resources for training, they constitute highly valued intellectual property (IP) for their legitimate owners, yet making them incentive targets for unauthorized fine-tuning by adversaries seeking to leverage these models for customized, usually profitable applications. Existing IP protection methods for diffusion models generally involve embedding watermark patterns and then verifying ownership through generated outputs examination, or inspecting the model's feature space. However, these techniques are inherently ineffective in practical scenarios when the watermarked model undergoes fine-tuning, and the feature space is inaccessible during verification (i.e., black-box setting). The model is prone to forgetting the previously learned watermark knowledge when it adapts to a new task. To address this challenge, we propose SleeperMark, a novel framework designed to embed resilient watermarks into T2I diffusion models. SleeperMark explicitly guides the model to disentangle the watermark information from the semantic concepts it learns, allowing the model to retain the embedded watermark while continuing to be adapted to new downstream tasks. Our extensive experiments demonstrate the effectiveness of SleeperMark across various types of diffusion models, including latent diffusion models (e.g., Stable Diffusion) and pixel diffusion models (e.g., DeepFloyd-IF), showing robustness against downstream fine-tuning and various attacks at both the image and model levels, with minimal impact on the model's generative capability.

</details>

### 6. Attack as Defense: Run-time Backdoor Implantation for Image Content Protection

📄 [arXiv](https://arxiv.org/abs/2410.14966)　📅 2024-10

**关键词**：`defense`、`run-time backdoor`、`image protection`、`region trigger`

👤 **作者**：Haichuan Zhang、…、Mingjie Tang

- 🎯 **研究动机**：图像所有者无权修改第三方编辑模型，需按单图保护敏感内容
- 🔬 **研究方法**：首个运行时后门注入框架：对图像生成不可感知扰动，保护区域即唯一触发器，编辑敏感区即触发失败
- 📌 **结论**：恶意编辑时 CLIP-FID 从 12.72 升至 39.91（SSIM 从 0.503 降至 0.167），良性编辑几乎不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative models achieve great success, tampering and modifying the sensitive image contents (i.e., human faces, artist signatures, commercial logos, etc.) have induced a significant threat with social impact. The backdoor attack is a method that implants vulnerabilities in a target model, which can be activated through a trigger. In this work, we innovatively prevent the abuse of image content modification by implanting the backdoor into image-editing models. Once the protected sensitive content on an image is modified by an editing model, the backdoor will be triggered, making the editing fail. Unlike traditional backdoor attacks that use data poisoning, to enable protection on individual images and eliminate the need for model training, we developed the first framework for run-time backdoor implantation, which is both time- and resource- efficient. We generate imperceptible perturbations on the images to inject the backdoor and define the protected area as the only backdoor trigger. Editing other unprotected insensitive areas will not trigger the backdoor, which minimizes the negative impact on legal image modifications. Evaluations with state-of-the-art image editing models show that our protective method can increase the CLIP-FID of generated images from 12.72 to 39.91, or reduce the SSIM from 0.503 to 0.167 when subjected to malicious editing. At the same time, our method exhibits minimal impact on benign editing, which demonstrates the efficacy of our proposed framework. The proposed run-time backdoor can also achieve effective protection on the latest diffusion models. Code are available.

</details>

### 7. Towards Reliable Verification of Unauthorized Data Usage in Personalized Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2410.10437)　📅 2024-10

**关键词**：`defense`、`data traceability`、`backdoor coating`、`black-box verification`

👤 **作者**：Boheng Li、…、Tianwei Zhang

- 🎯 **研究动机**：现有水印或后门涂层在个性化任务中难以被模型学习，验证不可靠
- 🔬 **研究方法**：SIREN 优化涂层使其被识别为与个性化任务相关的特征，辅以人类感知约束、超球分类与假设检验式验证
- 📌 **结论**：多基准、模型与算法上可靠验证黑盒个性化模型的未授权数据使用，并抗反制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models are pushing the boundaries of what generative AI can achieve in our lives. Beyond their ability to generate general images, new personalization techniques have been proposed to customize the pre-trained base models for crafting images with specific themes or styles. Such a lightweight solution, enabling AI practitioners and developers to easily build their own personalized models, also poses a new concern regarding whether the personalized models are trained from unauthorized data. A promising solution is to proactively enable data traceability in generative models, where data owners embed external coatings (e.g., image watermarks or backdoor triggers) onto the datasets before releasing. Later the models trained over such datasets will also learn the coatings and unconsciously reproduce them in the generated mimicries, which can be extracted and used as the data usage evidence. However, we identify the existing coatings cannot be effectively learned in personalization tasks, making the corresponding verification less reliable. In this paper, we introduce SIREN, a novel methodology to proactively trace unauthorized data usage in black-box personalized text-to-image diffusion models. Our approach optimizes the coating in a delicate way to be recognized by the model as a feature relevant to the personalization task, thus significantly improving its learnability. We also utilize a human perceptual-aware constraint, a hypersphere classification technique, and a hypothesis-testing-guided verification method to enhance the stealthiness and detection accuracy of the coating. The effectiveness of SIREN is verified through extensive experiments on a diverse set of benchmark datasets, models, and learning algorithms. SIREN is also effective in various real-world scenarios and evaluated against potential countermeasures. Our code is publicly available.

</details>

### 8. Lazy Layers to Make Fine-Tuned Diffusion Models More Traceable

📄 [arXiv](https://arxiv.org/abs/2405.00466)　📅 2024-05

**关键词**：`defense`、`backdoor watermark`、`feature-space trigger`、`fine-tuning robustness`

👤 **作者**：Haozhe Liu、Wentian Zhang、Bing Li、Bernard Ghanem、Jürgen Schmidhuber

- 🎯 **研究动机**：后门水印在非触发数据微调后易失效，稳定性不足
- 🔬 **研究方法**：发现微调只改变少数 busy 层的能量；AIAO 策略将水印嵌入采样子路径的特征空间，用 Monte Carlo 采样稳定验证
- 📌 **结论**：其他触发式方法验证率在微调后从约 90% 跌至约 70%，AIAO 保持 90% 以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Foundational generative models should be traceable to protect their owners and facilitate safety regulation. To achieve this, traditional approaches embed identifiers based on supervisory trigger-response signals, which are commonly known as backdoor watermarks. They are prone to failure when the model is fine-tuned with nontrigger data. Our experiments show that this vulnerability is due to energetic changes in only a few 'busy' layers during fine-tuning. This yields a novel arbitrary-in-arbitrary-out (AIAO) strategy that makes watermarks resilient to fine-tuning-based removal. The trigger-response pairs of AIAO samples across various neural network depths can be used to construct watermarked subpaths, employing Monte Carlo sampling to achieve stable verification results. In addition, unlike the existing methods of designing a backdoor for the input/output space of diffusion models, in our method, we propose to embed the backdoor into the feature space of sampled subpaths, where a mask-controlled trigger function is proposed to preserve the generation performance and ensure the invisibility of the embedded backdoor. Our empirical studies on the MS-COCO, AFHQ, LSUN, CUB-200, and DreamBooth datasets confirm the robustness of AIAO; while the verification rates of other trigger-based methods fall from ~90% to ~70% after fine-tuning, those of our method remain consistently above 90%.

</details>

### 9. Backdooring Textual Inversion for Concept Censorship

📄 [arXiv](https://arxiv.org/abs/2308.10718) · 🌐 [Project](https://concept-censorship.github.io/)　📅 2023-08

**关键词**：`defense`、`concept censorship`、`Textual Inversion`、`protective backdoor`

👤 **作者**：Yutong Wu、Jie Zhang、Florian Kerschbaum、Tianwei Zhang

- 🎯 **研究动机**：可下载的 Textual Inversion embedding 可被滥用造假或诽谤，缺乏概念审查手段
- 🔬 **研究方法**：以后门为善：TI 训练时把敏感词设为触发器，触发词与个性化 embedding 组合时输出预设安全图像
- 📌 **结论**：Stable Diffusion 上在不影响正常使用的前提下实现敏感概念审查

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent years have witnessed success in AIGC (AI Generated Content). People can make use of a pre-trained diffusion model to generate images of high quality or freely modify existing pictures with only prompts in nature language. More excitingly, the emerging personalization techniques make it feasible to create specific-desired images with only a few images as references. However, this induces severe threats if such advanced techniques are misused by malicious users, such as spreading fake news or defaming individual reputations. Thus, it is necessary to regulate personalization models (i.e., concept censorship) for their development and advancement. In this paper, we focus on the personalization technique dubbed Textual Inversion (TI), which is becoming prevailing for its lightweight nature and excellent performance. TI crafts the word embedding that contains detailed information about a specific object. Users can easily download the word embedding from public websites like Civitai and add it to their own stable diffusion model without fine-tuning for personalization. To achieve the concept censorship of a TI model, we propose leveraging the backdoor technique for good by injecting backdoors into the Textual Inversion embeddings. Briefly, we select some sensitive words as triggers during the training of TI, which will be censored for normal use. In the subsequent generation stage, if the triggers are combined with personalized embeddings as final prompts, the model will output a pre-defined target image rather than images including the desired malicious concept. To demonstrate the effectiveness of our approach, we conduct extensive experiments on Stable Diffusion, a prevailing open-sourced text-to-image model. Our code, data, and results are available at https://concept-censorship.github.io.

</details>

### 10. Watermarking Diffusion Model

📄 [arXiv](https://arxiv.org/abs/2305.12502)　📅 2023-05

**关键词**：`defense`、`model watermark`、`trigger prompt`、`ownership verification`

👤 **作者**：Yugeng Liu、Zheng Li、Michael Backes、Yun Shen、Yang Zhang

- 🎯 **研究动机**：扩散模型面临盗用与未授权使用等 IP 风险，所有权保护缺失
- 🔬 **研究方法**：提出两种水印方案：NAIVEWM 以含水印 prompt 激活，FIXEDWM 需固定位置触发词激活、更隐蔽
- 📌 **结论**：水印注入与验证有效且对 LDM 功能影响极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The availability and accessibility of diffusion models (DMs) have significantly increased in recent years, making them a popular tool for analyzing and predicting the spread of information, behaviors, or phenomena through a population. Particularly, text-to-image diffusion models (e.g., DALLE 2 and Latent Diffusion Models (LDMs) have gained significant attention in recent years for their ability to generate high-quality images and perform various image synthesis tasks. Despite their widespread adoption in many fields, DMs are often susceptible to various intellectual property violations. These can include not only copyright infringement but also more subtle forms of misappropriation, such as unauthorized use or modification of the model. Therefore, DM owners must be aware of these potential risks and take appropriate steps to protect their models. In this work, we are the first to protect the intellectual property of DMs. We propose a simple but effective watermarking scheme that injects the watermark into the DMs and can be verified by the pre-defined prompts. In particular, we propose two different watermarking methods, namely NAIVEWM and FIXEDWM. The NAIVEWM method injects the watermark into the LDMs and activates it using a prompt containing the watermark. On the other hand, the FIXEDWM is considered more advanced and stealthy compared to the NAIVEWM, as it can only activate the watermark when using a prompt containing a trigger in a fixed position. We conducted a rigorous evaluation of both approaches, demonstrating their effectiveness in watermark injection and verification with minimal impact on the LDM's functionality.

</details>

### 11. Towards Backdoor-Based Ownership Verification for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2605.09005)　📅 2026-05

**关键词**：`tool`、`GuardVLA`、`ownership verification`、`backdoor watermark`

👤 **作者**：Ming Sun、…、Ivor Tsang

- 🎯 **研究动机**：训练后的 VLA 被广泛共享与改编，模型所有权保护缺失
- 🔬 **研究方法**：GuardVLA 训练时向具身视觉数据注入秘密消息植入无害后门水印；发布后用 trigger projector 与外部分类头做 swap-and-detect 激活检测
- 📌 **结论**：多数据集、架构与适配设定下验证可靠且保持良性任务性能，模型改编后水印仍可检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action models (VLAs) support generalist robotic control by enabling end-to-end decision policies directly from multi-modal inputs. As trained VLAs are increasingly shared and adapted, protecting model ownership becomes essential for secure deployment and responsible open-source usage. In this paper, we present GuardVLA, the first backdoor-based ownership verification framework specifically designed for VLAs. GuardVLA embeds a stealthy and harmless backdoor watermark into the protected model during training by injecting secret messages into embodied visual data. For post-release verification, we propose a swap-and-detect mechanism, in which the trigger projector and an external classifier head are used to activate and detect the embedded backdoor based on prediction probabilities. Extensive experiments across multiple datasets, model architectures, and adaptation settings demonstrate that GuardVLA enables reliable ownership verification while preserving benign task performance. Further results show that the embedded watermark remains detectable under post-release model adaptation.

</details>

### 12. AGATE: Stealthy Black-box Watermarking for Multimodal Model Copyright Protection

📄 [arXiv](https://arxiv.org/abs/2504.21044)　📅 2025-04

**关键词**：`ownership tool`、`backdoor watermark`、`black-box verification`、`multimodal retrieval`

👤 **作者**：Jianbo Gao、Keke Gai、Jing Yu、Liehuang Zhu、Qi Wu

- 🎯 **研究动机**：现有 OoD 后门水印易被恶意检测与伪造，导致水印规避
- 🔬 **研究方法**：提出 AGATE，从普通数据生成视觉保真但语义偏移的对抗触发器，用后变换模块校正输出并做两阶段水印验证
- 📌 **结论**：五个数据集的多模态检索与分类任务全面超 SoTA，并在两种对抗攻击下保持鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancement in large-scale Artificial Intelligence (AI) models offering multimodal services have become foundational in AI systems, making them prime targets for model theft. Existing methods select Out-of-Distribution (OoD) data as backdoor watermarks and retrain the original model for copyright protection. However, existing methods are susceptible to malicious detection and forgery by adversaries, resulting in watermark evasion. In this work, we propose Model-\underline{ag}nostic Black-box Backdoor W\underline{ate}rmarking Framework (AGATE) to address stealthiness and robustness challenges in multimodal model copyright protection. Specifically, we propose an adversarial trigger generation method to generate stealthy adversarial triggers from ordinary dataset, providing visual fidelity while inducing semantic shifts. To alleviate the issue of anomaly detection among model outputs, we propose a post-transform module to correct the model output by narrowing the distance between adversarial trigger image embedding and text embedding. Subsequently, a two-phase watermark verification is proposed to judge whether the current model infringes by comparing the two results with and without the transform module. Consequently, we consistently outperform state-of-the-art methods across five datasets in the downstream tasks of multimodal image-text retrieval and image classification. Additionally, we validated the robustness of AGATE under two adversarial attack scenarios.

</details>

### 13. Watermarking Vision-Language Pre-trained Models for Multi-modal Embedding as a Service

📄 [arXiv](https://arxiv.org/abs/2311.05863)　📅 2023-11

**关键词**：`ownership tool`、`VLPMarker`、`backdoor watermark`、`embedding service`

👤 **作者**：Yuanmin Tang、…、Qi Wu

- 🎯 **研究动机**：多模态 EaaS 遭模型提取即丢失所有权，既有嵌入水印仅适用 LLM 且需触碰模型与数据
- 🔬 **研究方法**：VLPMarker 以嵌入正交变换注入触发器而不动模型参数，OOD 触发器选择摆脱训练数据访问，配合触发与分布双通道验证
- 📌 **结论**：多数据集上实现有效版权验证，性能影响小且抗模型提取攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in vision-language pre-trained models (VLPs) have significantly increased visual understanding and cross-modal analysis capabilities. Companies have emerged to provide multi-modal Embedding as a Service (EaaS) based on VLPs (e.g., CLIP-based VLPs), which cost a large amount of training data and resources for high-performance service. However, existing studies indicate that EaaS is vulnerable to model extraction attacks that induce great loss for the owners of VLPs. Protecting the intellectual property and commercial ownership of VLPs is increasingly crucial yet challenging. A major solution of watermarking model for EaaS implants a backdoor in the model by inserting verifiable trigger embeddings into texts, but it is only applicable for large language models and is unrealistic due to data and model privacy. In this paper, we propose a safe and robust backdoor-based embedding watermarking method for VLPs called VLPMarker. VLPMarker utilizes embedding orthogonal transformation to effectively inject triggers into the VLPs without interfering with the model parameters, which achieves high-quality copyright verification and minimal impact on model performance. To enhance the watermark robustness, we further propose a collaborative copyright verification strategy based on both backdoor trigger and embedding distribution, enhancing resilience against various attacks. We increase the watermark practicality via an out-of-distribution trigger selection approach, removing access to the model training data and thus making it possible for many real-world scenarios. Our extensive experiments on various datasets indicate that the proposed watermarking approach is effective and safe for verifying the copyright of VLPs for multi-modal EaaS and robust against model extraction attacks. Our code is available at https://github.com/Pter61/vlpmarker.

</details>

### 14. HoneypotNet: Backdoor Attacks Against Model Extraction

📄 [arXiv](https://arxiv.org/abs/2501.01090) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/32872)　📅 2025-01　🏷 AAAI 2025

**关键词**：`tool`、`backdoor fingerprint`、`ownership verification`、`capability blocking`

👤 **作者**：Yixu Wang、Tianle Gu、Yan Teng、Yingchun Wang、Xingjun Ma

- 🎯 **研究动机**：模型提取攻击盗用 MLaaS 模型，现有防御难以同时确权与威慑
- 🔬 **研究方法**：HoneypotNet 以攻代守：用 honeypot 层替换分类层，经 shadow model 双层优化使输出对提取者有毒
- 📌 **结论**：四个基准上高成功率向替代模型注入后门，兼具所有权验证与功能破坏的双重威慑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model extraction attacks are one type of inference-time attacks that approximate the functionality and performance of a black-box victim model by launching a certain number of queries to the model and then leveraging the model's predictions to train a substitute model. These attacks pose severe security threats to production models and MLaaS platforms and could cause significant monetary losses to the model owners. A body of work has proposed to defend machine learning models against model extraction attacks, including both active defense methods that modify the model's outputs or increase the query overhead to avoid extraction and passive defense methods that detect malicious queries or leverage watermarks to perform post-verification. In this work, we introduce a new defense paradigm called attack as defense which modifies the model's output to be poisonous such that any malicious users that attempt to use the output to train a substitute model will be poisoned. To this end, we propose a novel lightweight backdoor attack method dubbed HoneypotNet that replaces the classification layer of the victim model with a honeypot layer and then fine-tunes the honeypot layer with a shadow model (to simulate model extraction) via bi-level optimization to modify its output to be poisonous while remaining the original performance. We empirically demonstrate on four commonly used benchmark datasets that HoneypotNet can inject backdoors into substitute models with a high success rate. The injected backdoor not only facilitates ownership verification but also disrupts the functionality of substitute models, serving as a significant deterrent to model extraction attacks.

</details>

### 15. Inhibitory Attacks on Backdoor-based Fingerprinting for Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1207/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`LLM backdoor`、`model fingerprint`、`model copyright`、`model provenance`、`data poisoning`

👤 **作者**：Hang fu、Wanli Peng、Yinghan Zhou、Jiaxuan Wu、Wen-Juan Hou、Xue Yiming

- 🎯 **研究动机**：LLM 集成场景下后门指纹方案的鲁棒性未被评估
- 🔬 **研究方法**：提出 token filter attack（每步从统一 token 集取词）与 sentence verification attack（困惑度加投票滤除指纹响应）两种攻击
- 📌 **结论**：有效抑制指纹响应且保持集成性能，优于 SOTA 攻击方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of Large Language Model (LLM) in commercial and research settings has intensified the need for robust intellectual property protection. Backdoor-based LLM fingerprinting has emerged as a promising solution for this challenge. In practical application, the low-cost multi-model collaborative technique, LLM ensemble, combines diverse LLMs to leverage their complementary strengths, garnering significant attention and practical adoption. Unfortunately, the vulnerability of existing LLM fingerprinting for the ensemble scenario is unexplored. In order to comprehensively assess the robustness of LLM fingerprinting, in this paper, we propose two novel fingerprinting attack methods: token filter attack (TFA) and sentence verification attack (SVA). The TFA gets the next token from a unified set of tokens created by the token filter mechanism at each decoding step. The SVA filters out fingerprint responses through a sentence verification mechanism based on perplexity and voting. Experimentally, the proposed methods effectively inhibit the fingerprint response while maintaining ensemble performance. Compared with state-of-the-art attack methods, the proposed method can achieve better performance. The findings necessitate enhanced robustness in LLM fingerprinting.

</details>

### 16. ME: Trigger Element Combination Backdoor Attack on Copyright Infringement

📄 [arXiv](https://arxiv.org/abs/2506.10776)　📅 2025-06

**关键词**：`attack`、`copyright infringement`、`multi-element trigger`、`DCT stealth`

👤 **作者**：Feiyu Yang、Siyuan Liang、Aishan Liu、Dacheng Tao

- 🎯 **研究动机**：版权侵权攻击研究可用数据受限，SilentBadDiffusion 在可用投毒样本少时效果差
- 🔬 **研究方法**：在 SBD 基础上提出 Multi-Element 攻击增加每个投毒样本的毒化元素数，并引入 DCT 保持隐蔽
- 📌 **结论**：两个新数据集 CIR/FAE 达 16.78%/39.50 与 51.20%/23.60；5% 低采样下 DCT 得 12.73%/65.50 而原 SBD 完全失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The capability of generative diffusion models (DMs) like Stable Diffusion (SD) in replicating training data could be taken advantage of by attackers to launch the Copyright Infringement Attack, with duplicated poisoned image-text pairs. SilentBadDiffusion (SBD) is a method proposed recently, which shew outstanding performance in attacking SD in text-to-image tasks. However, the feasible data resources in this area are still limited, some of them are even constrained or prohibited due to the issues like copyright ownership or inappropriate contents; And not all of the images in current datasets are suitable for the proposed attacking methods; Besides, the state-of-the-art (SoTA) performance of SBD is far from ideal when few generated poisoning samples could be adopted for attacks. In this paper, we raised new datasets accessible for researching in attacks like SBD, and proposed Multi-Element (ME) attack method based on SBD by increasing the number of poisonous visual-text elements per poisoned sample to enhance the ability of attacking, while importing Discrete Cosine Transform (DCT) for the poisoned samples to maintain the stealthiness. The Copyright Infringement Rate (CIR) / First Attack Epoch (FAE) we got on the two new datasets were 16.78% / 39.50 and 51.20% / 23.60, respectively close to or even outperformed benchmark Pokemon and Mijourney datasets. In condition of low subsampling ratio (5%, 6 poisoned samples), MESI and DCT earned CIR / FAE of 0.23% / 84.00 and 12.73% / 65.50, both better than original SBD, which failed to attack at all.

</details>

### 17. The Stronger the Diffusion Model, the Easier the Backdoor: Data Poisoning to Induce Copyright Breaches Without Adjusting Finetuning Pipeline

📄 [arXiv](https://arxiv.org/abs/2401.04136)　📅 2024-01　🏷 ICML 2024

**关键词**：`attack`、`SilentBadDiffusion`、`copyright breach`、`clean pipeline`

👤 **作者**：Haonan Wang、Qianli Shen、Yao Tong、Yang Zhang、Kenji Kawaguchi

- 🎯 **研究动机**：DM 版权保护方案自身的脆弱性未被探索，且攻击者常无法控制训练流程
- 🔬 **研究方法**：SilentBadDiffusion 把版权信息与文本引用的关联分散嵌入毒数据，无需访问或控制训练过程
- 📌 **结论**：0.20% 投毒率即可让 DM 在特定 prompt 下生成版权图像；模型越强攻击越易成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The commercialization of text-to-image diffusion models (DMs) brings forth potential copyright concerns. Despite numerous attempts to protect DMs from copyright issues, the vulnerabilities of these solutions are underexplored. In this study, we formalized the Copyright Infringement Attack on generative AI models and proposed a backdoor attack method, SilentBadDiffusion, to induce copyright infringement without requiring access to or control over training processes. Our method strategically embeds connections between pieces of copyrighted information and text references in poisoning data while carefully dispersing that information, making the poisoning data inconspicuous when integrated into a clean dataset. Our experiments show the stealth and efficacy of the poisoning data. When given specific text prompts, DMs trained with a poisoning ratio of 0.20% can produce copyrighted images. Additionally, the results reveal that the more sophisticated the DMs are, the easier the success of the attack becomes. These findings underline potential pitfalls in the prevailing copyright protection strategies and underscore the necessity for increased scrutiny to prevent the misuse of DMs.

</details>

### 18. CopyrightShield: Enhancing Diffusion Model Security Against Copyright Infringement Attacks

📄 [arXiv](https://arxiv.org/abs/2412.01528) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_CopyrightShield_Enhancing_Diffusion_Model_Security_Against_Copyright_Infringement_Attacks_ICCV2025_paper.html)　📅 2024-12　🏷 ICCV 2025

**关键词**：`defense`、`copyright backdoor`、`poison detection`、`adaptive training`

👤 **作者**：Zhixiang Guo、Siyuan Liang、Aishan Liu、Dacheng Tao

- 🎯 **研究动机**：版权后门利用扩散模型对特定位置与 prompt 的过拟合，传统清洗难以定位毒样本
- 🔬 **研究方法**：CopyrightShield 以空间掩码加数据归因定位隐藏毒样本，并在训练损失中加入动态惩罚项抑制侵权特征记忆
- 📌 **结论**：平均检测 F1 达 0.665，首次攻击延后 115.2%，版权侵权率降 56.7%，较 SOTA 防御再提升约 25%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have attracted significant attention due to its exceptional data generation capabilities in fields such as image synthesis. However, recent studies have shown that diffusion models are vulnerable to copyright infringement attacks, where attackers inject strategically modified non-infringing images into the training set, inducing the model to generate infringing content under the prompt of specific poisoned captions. To address this issue, we first propose a defense framework, CopyrightShield, to defend against the above attack. Specifically, we analyze the memorization mechanism of diffusion models and find that attacks exploit the model's overfitting to specific spatial positions and prompts, causing it to reproduce poisoned samples under backdoor triggers. Based on this, we propose a poisoned sample detection method using spatial masking and data attribution to quantify poisoning risk and accurately identify hidden backdoor samples. To further mitigate memorization of poisoned features, we introduce an adaptive optimization strategy that integrates a dynamic penalty term into the training loss, reducing reliance on infringing features while preserving generative performance. Experimental results demonstrate that CopyrightShield significantly improves poisoned sample detection performance across two attack scenarios, achieving average F1-scores of 0.665, retarding the First-Attack Epoch (FAE) of 115.2% and decreasing the Copyright Infringement Rate (CIR) by 56.7%. Compared to the SoTA backdoor defense in diffusion models, the defense effect is improved by about 25%, showcasing its superiority and practicality in enhancing the security of diffusion models.

</details>

### 19. Robust Watermarks Meet Backdoored Models: Evading Diffusion Semantic Watermarks via Stealthy Backdoor

📄 [arXiv](https://arxiv.org/abs/2608.00543) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-jinyuan)　📅 2026-08

**关键词**：`attack`、`semantic watermark`、`VAE backdoor`、`detector evasion`、`diffusion watermark`、`backdoor`

👤 **作者**：Jinyuan Liu、…、Xiaoyun Wang

- 🎯 **研究动机**：语义水印的检测管线依赖 VAE 等神经网络，其后门攻击面未被研究
- 🔬 **研究方法**：GhostVAE 两阶段在 VAE 编码器植入隐蔽后门：功率谱正则构造通用触发器，再用参数对齐目标训练后门编码器以逃避水印检测
- 📌 **结论**：对三种 SOTA 语义水印与三种 LDM，良性图像 TPR 保持 94.4% 的同时触发后平均 ASR 达 94.6%，17 种防御下在输入/参数/潜空间均隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although semantic watermarking is considered a promising safeguard for images generated by Latent Diffusion Models (LDMs), the reliance of the watermark detection pipeline on neural networks introduces a critical yet underexplored backdoor attack surface. To systematically study this vulnerability, we propose GhostVAE to plant a stealthy backdoor into the encoder of Variational Autoencoder (VAE), enabling reliable evasion of watermark detection. GhostVAE operates in two stages: it first constructs a universal trigger via power spectrum regularization to improve the trigger robustness, and then trains a backdoored VAE encoder with a parameter-aligned objective. Through extensive evaluations across three state-of-the-art semantic watermarking schemes and three widely adopted LDMs, we show that GhostVAE preserves watermark detection performance on benign images (achieving an average true positive rate of 94.4%), while simultaneously enabling highly effective evasion under trigger activation (achieving an average attack success rate of 94.6%). Moreover, we comprehensively analyze seventeen representative defenses and demonstrate that GhostVAE remains stealthy across the input space, parameter space, and latent space. Our work fundamentally undermines the trustworthiness of semantic watermarking systems and highlights that secure deployment of semantic watermarks requires end-to-end security considerations, particularly for neural network components.

</details>