# 视觉语言模型后门检测与防御

[返回上级目录](README.md)

## 研究方向

VLM 后门的检测、防御与净化（攻击机制见姊妹页 vlm-backdoor-attacks.md）。

## 检测与防御

### 1. DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption

📄 [arXiv](https://arxiv.org/abs/2608.16536)　📅 2026-08

**关键词**：`defense`、`adversarial robustness`、`VLM safety`、`data poisoning`、`M-RAG`、`dynamic soft prompt`

👤 **作者**：Chang Liu、…、Bin Xiao

- 🎯 **研究动机**：M-RAG 防御集中于查询时（辅助检测器、重排、特征一致性），推理开销大且难泛化到未见攻击
- 🔬 **研究方法**：DSPrompt 在冻结检索器各层插入可学习软 prompt（浅到深长度调度），动态 min-max 训练：在线攻击者持续构造硬对抗文档，防御者将其推出 top-k 同时保良性排序与多样性
- 📌 **结论**：四个基准、三种投毒攻击下大幅降低 ASR 与投毒检索率，检索效用近无损，额外参数少于 1% 且零逐查询开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Retrieval Augmented Generation (M-RAG) is increasingly vulnerable to adversarial attacks where malicious data are crafted to produce embeddings that align with benign entries in the vector space, deceiving retrieval and inducing harmful outputs. Existing defenses primarily operate at query time, relying on auxiliary detectors, similarity re-ranking, or feature-consistency checks. However, these approaches suffer from non-trivial inference overhead, generalize poorly to unseen attack strategies, and often assume specific attack distributions. To address this, we propose DSPrompt, a Dynamic Soft Prompt defense framework that directly reshapes the retriever's embedding semantics, without modifying the retrieval pipeline. It inserts few learnable soft prompts into each layer of the visual and textual encoders of a frozen retriever, utilizing a shallow-to-deep length schedule that is adaptive to the capacity in the model layers. These prompts are trained under a dynamic min-max scheme: an online multimodal attacker continually crafts hard adversarial documents against the current retriever, while the defender is updated to push such documents out of the top-k while preserving the ranking and diversity of benign evidence. Because the defended encoder can be pre-computed and indexed exactly as in standard dense retrieval, DSPrompt incurs no additional per-query optimization and introduces fewer than 1% additional parameters. Extensive experiments across four benchmarks and three representative poisoning attacks show that DSPrompt substantially reduces the attack success rate and poison retrieval rate while maintaining near-lossless retrieval utility and generation fidelity, consistently outperforming existing defense baselines at a fraction of their computational cost.

</details>

### 2. When Modalities Fail to Tango: Conformal Backdoor Detection in Multimodal Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2608.04052)　📅 2026-08

**关键词**：`detection`、`CASCADE`、`conformal calibration`、`cross-modal inconsistency`

👤 **作者**：Yiming Chen、Kemou Li、Haiwei Wu、Jiantao Zhou

- 🎯 **研究动机**：多模态对比学习后门检测依赖 CLIPScore 且固定阈值无统计保证，良性与投毒对的分数分布大量重叠
- 🔬 **研究方法**：CASCADE 两阶段粗到细：跨模态一致性筛出高置信对，再用文本空间相似度的非一致性分数做 conformal 校准识别剩余投毒对
- 📌 **结论**：CC3M 上 100% TPR 时平均 FPR 仅 5.79%、AUROC 0.9867，对自适应攻击仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in multimodal contrastive learning (MCL) have garnered growing attention in recent years, as many downstream tasks critically depend on pre-trained MCL models. Existing detection-based defenses predominantly rely on the CLIPScore metric, under the assumption that poisoned pairs exhibit lower semantic similarity between the image and the caption. However, we identify two critical flaws remaining in existing methods: (1) the substantial overlap between CLIPScore distributions of benign and poisoned pairs undermines the reliability of this metric, and (2) fixed-threshold detection cannot provide statistical guarantees for ambiguous samples within overlapping regions. To overcome these limitations, we propose integrating conformal prediction (CP), a statistical framework that quantifies uncertainty through nonconformity scores (NCSs), to establish provable confidence bounds for detecting poisoned image-caption pairs. Building on CP, we introduce CASCADE, a novel two-stage Coarse-to-Fine Conformal Backdoor Detection framework. The coarse-grained stage uses cross-modality consistency to identify high-confidence benign and poisoned pairs. In the fine-grained stage, a reference set is constructed from high-confidence poisoned pairs, and instance-level NCSs based on text-space similarity are computed for each sample in the unidentified subset. These NCSs measure conformity to the poisoning distribution and enable precise identification of latent poisoned pairs within the unidentified subset. Extensive experiments on the large-scale CC3M dataset demonstrate that CASCADE achieves an average FPR of 5.79% at 100% TPR and an average AUROC of 0.9867 across diverse attacks, while remaining effective against adaptive attacks.

</details>

### 3. DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors

📄 [arXiv](https://arxiv.org/abs/2608.25851) · 🌐 [Project](https://doi.org/10.1145/3767308.3835471)　📅 2026-08

**关键词**：`detection`、`SSL encoder backdoor`、`generative prior`、`cross-paradigm generalization`、`vision-language encoder`、`semantic reconstruction`

👤 **作者**：Tuo Chen、…、Jian Liu

- 🎯 **研究动机**：SSL encoder 后门防御只覆盖单一范式，且依赖未感染数据等强假设
- 🔬 **研究方法**：DEFUSE 用 diffusion 先验从表示重建图像，中毒表示会映射到目标类或无语义图像，据此检测
- 📌 **结论**：跨视觉 SSL 与 vision-language encoder 的攻击下优于现有检测器，且降低对 victim 与攻击的先验依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspired by Bayesian posterior inference, we reformulate backdoor detection as a representation-conditioned image likelihood estimation problem parameterized by a conditional diffusion generative model. Uninfected representations tend to yield semantically consistent reconstructions, whereas backdoored ones are more likely to be mapped to the attacker's target class or semantically meaningless images, deviating from the original semantics and thereby exposing the backdoor. However, we find that the exact likelihood is intractable, because highly abstracted representations discard the low-level information necessary for pixel-faithful reconstruction. We therefore relax the objective to semantic reconstruction and evaluate it in a well-separated representation space provided by a reference encoder. Rather than training from scratch, we fine-tune a pretrained diffusion model, leveraging its generative prior to map data onto the natural image manifold while preserving semantic content. Extensive experiments demonstrate that DEFUSE substantially outperforms existing detectors across diverse attack settings, generalizing to both visual SSL and vision-language encoders. Notably, our method greatly reduces the reliance on prior knowledge about the victim encoder or the attack strategy. The source code is available at https://github.com/jsrdcht/DEFUSE .

</details>

### 4. BYORn: Bootstrap Your Own Responses to Defend Large Vision-Language Models Against Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2606.02947) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62182)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`attack`、`robust fine-tuning`、`response replacement`、`adaptive attack`、`backdoor attack`

👤 **作者**：Ivan Sabolić、Marin Oršić、Josip Šarić、Sven Lončarić

- 🎯 **研究动机**：监督微调的自回归 VLM 极易受后门攻击，已有防御在开放式生成场景失效
- 🔬 **研究方法**：提出 BYORn，检测与图文输入语义不符的中毒目标回复，动态替换为模型自生成回复以切断触发器与目标输出的关联，目标梯度对应干净分布风险上界的经验估计
- 📌 **结论**：在保持干净任务性能的同时持续提升后门鲁棒性，形成泛化-攻击成功率新权衡前沿，且能抵御专门设计的自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Supervised fine-tuning is the predominant approach for adapting autoregressive vision-language models to downstream tasks. Recent work has shown that this paradigm is highly vulnerable to backdoor attacks, and that existing defenses are ineffective in open-ended generation settings. In response, we propose BYORn, a backdoor-robust fine-tuning framework motivated by the observation that poisoned target responses are often semantically implausible given the corresponding image-text inputs and a pretrained model. BYORn identifies such misaligned responses and dynamically replaces them with alternative responses generated by the model, thereby breaking the correlation between triggers and target outputs. The resulting objective gradient corresponds to the gradient of the empirical estimate of the population risk upper bound over the clean data distribution. Empirically, BYORn consistently improves robustness to backdoor attacks while preserving clean-task performance, establishing a new trade-off frontier between generalization and attack success rate. Finally, we demonstrate that BYORn remains effective against adaptive attacks specifically designed to circumvent the proposed defense.

</details>

### 5. A Patch-based Cross-view Regularized Framework for Backdoor Defense in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.04488) · 🌐 [Project](https://doi.org/10.1007/s10044-026-01723-x)　📅 2026-04

**关键词**：`defense`、`patch augmentation`、`cross-view consistency`、`MLLM fine-tuning`

👤 **作者**：Tianmeng Fang、…、Wei Wang

- 🎯 **研究动机**：MLLM 微调后门防御需在低投毒率下压 ASR 又保生成能力，强抑制损良性、弱正则除不了后门
- 🔬 **研究方法**：patch 级数据增强加跨视图输出差异正则，利用后门响应对非语义扰动异常不变来拉开原始与扰动视图分布，并以输出熵约束避免过度抑制
- 📌 **结论**：三个模型、两个任务、六种攻击下有效降低 ASR 并保持正常文本生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models have become an important infrastructure for unified processing of visual and linguistic tasks. However, such models are highly susceptible to backdoor implantation during supervised fine-tuning and will steadily output the attacker's predefined harmful responses once a specific trigger pattern is activated. The core challenge of backdoor defense lies in suppressing attack success under low poisoning ratios while preserving the model's normal generation ability. These two objectives are inherently conflicting. Strong suppression often degrades benign performance, whereas weak regularization fails to mitigate backdoor behaviors. To this end, we propose a unified defense framework based on patch augmentation and cross-view regularity, which simultaneously constrains the model's anomalous behaviors in response to triggered patterns from both the feature representation and output distribution levels. Specifically, patch-level data augmentation is combined with cross-view output difference regularization to exploit the fact that backdoor responses are abnormally invariant to non-semantic perturbations and to proactively pull apart the output distributions of the original and perturbed views, thereby significantly suppressing the success rate of backdoor triggering. At the same time, we avoid over-suppression of the model during defense by imposing output entropy constraints, ensuring the quality of normal command generation. Experimental results across three models, two tasks, and six attacks show that our proposed defense method effectively reduces the attack success rate while maintaining a high level of normal text generation capability. Our work enables the secure, controlled deployment of large-scale multimodal models in realistic low-frequency poisoning and covert triggering scenarios.

</details>

### 6. DIFT: Protecting Contrastive Learning Against Data Poisoning Backdoor Attacks

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/37141)　📅 2026-03　🏷 AAAI 2026

**关键词**：`defense`、`contrastive learning`、`poisoning`、`robust representation`

- 🎯 **研究动机**：对比学习预训练易被数据投毒植入后门
- 🔬 **研究方法**：DIFT面向对比预训练学习更稳定的特征关系，降低后门目标对表示空间的吸附
- 📌 **结论**：抑制后门注入并保留clean迁移性能

### 7. Adversarial Hubness Detector: Detecting Hubness Poisoning in Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2602.22427)　📅 2026-02

**关键词**：`detection`、`vector hubness`、`index scanner`、`alert-budget evaluation`、`hubscan`、`vector index`

👤 **作者**：Idan Habler、Vineeth Sai Narajala、Stav Koren、Amy Chang、Tiffany Saade

- 🎯 **研究动机**：RAG 向量检索中的 hubness 可被投毒利用操纵排序、绕过过滤，缺乏检测工具
- 🔬 **研究方法**：hubscan 集成 MAD z-score 统计检测、簇扩散分析、查询扰动稳定性与领域/模态感知检测，支持 FAISS、Pinecone、Qdrant、Weaviate
- 📌 **结论**：0.2% 告警预算下召回 90%、0.4% 下 100%；百万级 MS MARCO 生产验证中干净与对抗内容分数显著分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are essential to contemporary AI applications, allowing large language models to obtain external knowledge via vector similarity search. Nevertheless, these systems encounter a significant security flaw: hubness - items that frequently appear in the top-$k$ retrieval results for a disproportionately high number of varied queries. These hubs can be exploited to introduce harmful content, alter search rankings, bypass content filtering, and decrease system performance. We introduce hubscan, an open-source security scanner that evaluates vector indices and embeddings to identify hubs in RAG systems. Hubscan presents a multi-detector architecture that integrates: (1) robust statistical hubness detection utilizing median/Median Absolute Deviation (MAD)-based z-scores, (2) cluster spread analysis to assess cross-cluster retrieval patterns, (3) stability testing under query perturbations, and (4) domain-aware and modality-aware detection for category-specific and cross-modal attacks. Our solution accommodates several vector databases (FAISS, Pinecone, Qdrant, Weaviate) and offers versatile retrieval techniques, including vector similarity, hybrid search, and lexical matching with reranking capabilities. We evaluate hubscan on Food-101, MS-COCO, and FiQA adversarial hubness benchmarks constructed using state-of-the-art gradient-optimized and centroid-based hub generation methods. Hubscan achieves 90% recall at a 0.2% alert budget and 100% recall at 0.4%, with adversarial hubs ranking above the 99.8th percentile. In testing, domain-scoped scanning recovered 100% of targeted attacks that evaded global detection. Production validation on 1M real web documents from MS MARCO demonstrates significant score separation between clean documents and adversarial content.

</details>

### 8. Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2602.22246)　📅 2026-02

**关键词**：`defense`、`multimodal diffusion LM`、`self-purification`、`visual token masking`、`DiSP`

👤 **作者**：Guangnian Wan、Qi Li、Gongfan Fang、Xinyin Ma、Xinchao Wang

- 🎯 **研究动机**：多模态扩散语言模型可被数据投毒植入后门，且尚无有效防御
- 🔬 **研究方法**：DiSP 发现推理时选择性掩蔽视觉 token 可中和触发行为，用受污染模型自身净化数据集再微调恢复，无需辅助模型或干净数据
- 📌 **结论**：ASR 从超 90% 通常降到 5% 以下，同时保持良性任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Diffusion Language Models (MDLMs) have recently emerged as a competitive alternative to their autoregressive counterparts. Yet their vulnerability to backdoor attacks remains largely unexplored. In this work, we show that well-established data-poisoning pipelines can successfully implant backdoors into MDLMs, enabling attackers to manipulate model behavior via specific triggers while maintaining normal performance on clean inputs. However, defense strategies effective to these models are yet to emerge. To bridge this gap, we introduce a backdoor defense framework for MDLMs named DiSP (Diffusion Self-Purification). DiSP is driven by a key observation: selectively masking certain vision tokens at inference time can neutralize a backdoored model's trigger-induced behaviors and restore normal functionality. Building on this, we purify the poisoned dataset using the compromised model itself, then fine-tune the model on the purified data to recover it to a clean one. Given such a specific design, DiSP can remove backdoors without requiring any auxiliary models or clean reference data. Extensive experiments demonstrate that our approach effectively mitigates backdoor effects, reducing the attack success rate (ASR) from over 90% to typically under 5%, while maintaining model performance on benign tasks.

</details>

### 9. TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2601.21692) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66774)　📅 2026-01　🏷 ICML 2026

**关键词**：`detection`、`attention profiling`、`unsupervised filtering`、`FTaaS`、`backdoor defense`、`empirical evaluation`

👤 **作者**：Mingzu Liu、Hao Fang、Runmin Cong

- 🎯 **研究动机**：FTaaS 中 MLLM 面临毒数据后门风险，现有防御依赖监督信号或难以跨触发类型与模态泛化
- 🔬 **研究方法**：发现毒样本破坏系统指令、视觉输入与用户查询三组件间注意力平衡分配的通用指纹；TCAP 无监督分解跨模态注意力、用 GMM 剖析识别触发敏感头、以 EM 投票聚合隔离毒样本
- 📌 **结论**：跨 MLLM 架构与多样攻击方法表现一致强劲，是实用的 MLLM 后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-Tuning-as-a-Service (FTaaS) facilitates the customization of Multimodal Large Language Models (MLLMs) but introduces critical backdoor risks via poisoned data. Existing defenses either rely on supervised signals or fail to generalize across diverse trigger types and modalities. In this work, we uncover a universal backdoor fingerprint-attention allocation divergence-where poisoned samples disrupt the balanced attention distribution across three functional components: system instructions, vision inputs, and user textual queries, regardless of trigger morphology. Motivated by this insight, we propose Tri-Component Attention Profiling (TCAP), an unsupervised defense framework to filter backdoor samples. TCAP decomposes cross-modal attention maps into the three components, identifies trigger-responsive attention heads via Gaussian Mixture Model (GMM) statistical profiling, and isolates poisoned samples through EM-based vote aggregation. Extensive experiments across diverse MLLM architectures and attack methods demonstrate that TCAP achieves consistently strong performance, establishing it as a robust and practical backdoor defense in MLLMs.

</details>

### 10. Pre-training CLIP against Data Poisoning with Optimal Transport-based Matching and Alignment

📄 [arXiv](https://arxiv.org/abs/2509.18717) · 🎓 [Official](https://aclanthology.org/2025.emnlp-main.497/)　📅 2025-09　🏷 EMNLP 2025

**关键词**：`defense`、`OTCCLIP`、`optimal transport`、`robust pretraining`

👤 **作者**：Tong Zhang、…、Wenzhi Chen

- 🎯 **研究动机**：既有 CLIP 防御的图文配对修正只依赖全局表示，忽略细粒度特征且可能引入错误配对
- 🔬 **研究方法**：提出 OTCCLIP：以细粒度视觉文本特征集间的最优传输距离重配 caption，并用 OT 目标函数促进模态间与模态内细粒度对齐
- 📌 **结论**：成功降低投毒攻击 ASR，并在投毒数据上显著提升 CLIP 的零样本与线性探测性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have shown that Contrastive Language-Image Pre-training (CLIP) models are threatened by targeted data poisoning and backdoor attacks due to massive training image-caption pairs crawled from the Internet. Previous defense methods correct poisoned image-caption pairs by matching a new caption for each image. However, the matching process relies solely on the global representations of images and captions, overlooking fine-grained features of visual and textual features. It may introduce incorrect image-caption pairs and harm the CLIP pre-training. To address their limitations, we propose an Optimal Transport-based framework to reconstruct image-caption pairs, named OTCCLIP. We propose a new optimal transport-based distance measure between fine-grained visual and textual feature sets and re-assign new captions based on the proposed optimal transport distance. Additionally, to further reduce the negative impact of mismatched pairs, we encourage the inter- and intra-modality fine-grained alignment by employing optimal transport-based objective functions. Our experiments demonstrate that OTCCLIP can successfully decrease the attack success rates of poisoning attacks. Also, compared to previous methods, OTCCLIP significantly improves CLIP's zero-shot and linear probing performance trained on poisoned datasets.

</details>

### 11. Robust Anti-Backdoor Instruction Tuning in LVLMs

📄 [arXiv](https://arxiv.org/abs/2506.05401)　📅 2025-06

**关键词**：`defense`、`instruction tuning`、`parameter-efficient defense`、`activation regularization`

👤 **作者**：Yuan Xun、Siyuan Liang、Xiaojun Jia、Xinwei Liu、Xiaochun Cao

- 🎯 **研究动机**：现有后门防御假设可全参数调整或需攻击先验，真实场景中视觉编码器与核心 LLM 均冻结
- 🔬 **研究方法**：提出 Robust Instruction Tuning：仅微调 adapter 与文本嵌入层，结合输入多样性正则与异常激活正则
- 📌 **结论**：对 Flickr30k 与 MSCOCO 上七种攻击把 ASR 降到近零，训练成本增加不足 15%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large visual language models (LVLMs) have demonstrated excellent instruction-following capabilities, yet remain vulnerable to stealthy backdoor attacks when finetuned using contaminated data. Existing backdoor defense techniques are usually developed for single-modal visual or language models under fully parameter-adjustable settings or rely on supervisory knowledge during training. However, in real-world scenarios, defenders cannot modify frozen visual encoders or core LLM parameters, nor possess prior knowledge of unknown trigger patterns or target responses. Motivated by the empirical finding that LVLMs readily overfit to fixed, unknown triggers, which can embed malicious associations during adapter-level tuning, we aim to design a defense that operates without access to core weights or attack priors. To this end, we introduce a lightweight, certified-agnostic defense framework, Robust Instruction Tuning, that finetunes only adapter modules and text embedding layers under instruction tuning. Our method integrates two complementary regularizations: (1) Input Diversity Regularization, which perturbs trigger components across training samples to disrupt consistent spurious cues; and (2) Anomalous Activation Regularization, which dynamically sparses adapter weights exhibiting abnormally sharp activations linked to backdoor patterns. These mechanisms jointly guide the model toward learning semantically grounded representations rather than memorizing superficial trigger-response mappings. Extensive experiments against seven attacks on Flickr30k and MSCOCO demonstrate that ours reduces their attack success rate to nearly zero, with an increase in training cost of less than 15%.

</details>

### 12. Backdoor Cleaning without External Guidance in MLLM Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2505.16916) · 📝 [OpenReview](https://openreview.net/forum?id=os4QYDf3Ms)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`defense`、`BYE`、`attention entropy`、`unsupervised filtering`

👤 **作者**：Xuankun Rong、…、Mang Ye

- 🎯 **研究动机**：FTaaS 恶意微调可植入后门，现有检测需干净监督或依赖改写而引入新风险
- 🔬 **研究方法**：发现触发器导致 attention collapse，提出 BYE 三阶段管线：提取注意力图、熵评分定位敏感层、无监督聚类剔除可疑样本
- 📌 **结论**：无需干净监督或模型修改即可把 ASR 降至近零并保持任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in fine-tuning-as-a-service (FTaaS) settings, where user-submitted datasets adapt general-purpose models to downstream tasks. This flexibility, however, introduces serious security risks, as malicious fine-tuning can implant backdoors into MLLMs with minimal effort. In this paper, we observe that backdoor triggers systematically disrupt cross-modal processing by causing abnormal attention concentration on non-semantic regions--a phenomenon we term attention collapse. Based on this insight, we propose Believe Your Eyes (BYE), a data filtering framework that leverages attention entropy patterns as self-supervised signals to identify and filter backdoor samples. BYE operates via a three-stage pipeline: (1) extracting attention maps using the fine-tuned model, (2) computing entropy scores and profiling sensitive layers via bimodal separation, and (3) performing unsupervised clustering to remove suspicious samples. Unlike prior defenses, BYE equires no clean supervision, auxiliary labels, or model modifications. Extensive experiments across various datasets, models, and diverse trigger types validate BYE's effectiveness: it achieves near-zero attack success rates while maintaining clean-task performance, offering a robust and generalizable solution against backdoor threats in MLLMs.

</details>

### 13. Detecting Backdoor Samples in Contrastive Language Image Pretraining

📄 [arXiv](https://arxiv.org/abs/2502.01385) · 🎓 [Official](https://iclr.cc/virtual/2025/poster/30032)　📅 2025-02　🏷 ICLR 2025

**关键词**：`detection`、`CLIP data cleaning`、`local density`、`unintentional backdoor`

👤 **作者**：Hanxun Huang、Sarah Erfani、Yige Li、Xingjun Ma、James Bailey

- 🎯 **研究动机**：CLIP 投毒 0.01% 数据即近满分 ASR，毒样本的可检测特征未被利用
- 🔬 **研究方法**：发现毒样本局部邻域远比干净样本稀疏，传统密度比局部离群检测器即可高效检出
- 📌 **结论**：现有检测方法失效而本法有效；在 CC3M 中发现无意后门并已进入 OpenCLIP 开源模型；百万级数据 15 分钟即可清洗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive language-image pretraining (CLIP) has been found to be vulnerable to poisoning backdoor attacks where the adversary can achieve an almost perfect attack success rate on CLIP models by poisoning only 0.01\% of the training dataset. This raises security concerns on the current practice of pretraining large-scale models on unscrutinized web data using CLIP. In this work, we analyze the representations of backdoor-poisoned samples learned by CLIP models and find that they exhibit unique characteristics in their local subspace, i.e., their local neighborhoods are far more sparse than that of clean samples. Based on this finding, we conduct a systematic study on detecting CLIP backdoor attacks and show that these attacks can be easily and efficiently detected by traditional density ratio-based local outlier detectors, whereas existing backdoor sample detection methods fail. Our experiments also reveal that an unintentional backdoor already exists in the original CC3M dataset and has been trained into a popular open-source model released by OpenCLIP. Based on our detector, one can clean up a million-scale web dataset (e.g., CC3M) efficiently within 15 minutes using 4 Nvidia A100 GPUs. The code is publicly available in our \href{https://github.com/HanxunH/Detect-CLIP-Backdoor-Samples}{GitHub repository}.

</details>

### 14. Semantic Shield: Defending Vision-Language Models Against Backdooring and Poisoning via Fine-grained Knowledge Alignment

📄 [arXiv](https://arxiv.org/abs/2411.15673) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2024/html/Ishmam_Semantic_Shield_Defending_Vision-Language_Models_Against_Backdooring_and_Poisoning_via_CVPR_2024_paper.html)　📅 2024-06　🏷 CVPR 2024

**关键词**：`defense`、`fine-grained knowledge`、`semantic alignment`、`CLIP`

👤 **作者**：Alvi Md Ishmam、Christopher Thomas

- 🎯 **研究动机**：网络数据训练的视觉语言模型易随后门与投毒攻击，需要不增推理成本的缓解
- 🔬 **研究方法**：Semantic Shield 用语言模型抽取的外部知识约束注意力，使模型对视觉区域的注意力与该区域和外部知识的对齐度成正比
- 📌 **结论**：多种攻击、数据集与架构上防御高效，保持模型效用且推理时零改动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years there has been enormous interest in vision-language models trained using self-supervised objectives. However, the use of large-scale datasets scraped from the web for training also makes these models vulnerable to potential security threats, such as backdooring and poisoning attacks. In this paper, we propose a method for mitigating such attacks on contrastively trained vision-language models. Our approach leverages external knowledge extracted from a language model to prevent models from learning correlations between image regions which lack strong alignment with external knowledge. We do this by imposing constraints to enforce that attention paid by the model to visual regions is proportional to the alignment of those regions with external knowledge. We conduct extensive experiments using a variety of recent backdooring and poisoning attacks on multiple datasets and architectures. Our results clearly demonstrate that our proposed approach is highly effective at defending against such attacks across multiple settings, while maintaining model utility and without requiring any changes at inference time

</details>

### 15. Better Safe than Sorry: Pre-training CLIP against Targeted Data Poisoning and Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2310.05862) · 🌐 [Project](https://proceedings.mlr.press/v235/yang24i.html)　📅 2023-10　🏷 ICML 2024

**关键词**：`defense`、`SAFECLIP`、`safe／risky split`、`robust pretraining`

👤 **作者**：Wenhan Yang、Jingdong Gao、Baharan Mirzasoleiman

- 🎯 **研究动机**：CLIP 预训练数据投毒 0.0001% 即可成功定向攻击（比监督模型低四个数量级），预训练期防御缺位
- 🔬 **研究方法**：SAFECLIP 先单模态对比预热，再以 GMM 按图文相似度划分 safe/risky 集：safe 用 CLIP loss，risky 仅做单模态学习
- 📌 **结论**：CC3M 等数据集上定向投毒成功率从 93.75% 降至 0%、各类后门最高从 100% 降至 0%，且不损 CLIP 性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive Language-Image Pre-training (CLIP) on large image-caption datasets has achieved remarkable success in zero-shot classification and enabled transferability to new domains. However, CLIP is extremely more vulnerable to targeted data poisoning and backdoor attacks, compared to supervised learning. Perhaps surprisingly, poisoning 0.0001% of CLIP pre-training data is enough to make targeted data poisoning attacks successful. This is four orders of magnitude smaller than what is required to poison supervised models. Despite this vulnerability, existing methods are very limited in defending CLIP models during pre-training. In this work, we propose a strong defense, SAFECLIP, to safely pre-train CLIP against targeted data poisoning and backdoor attacks. SAFECLIP warms up the model by applying unimodal contrastive learning (CL) on image and text modalities separately. Then, it divides the data into safe and risky sets, by applying a Gaussian Mixture Model to the cosine similarity of image-caption pair representations. SAFECLIP pre-trains the model by applying the CLIP loss to the safe set and applying unimodal CL to image and text modalities of the risky set separately. By gradually increasing the size of the safe set during pre-training, SAFECLIP effectively breaks targeted data poisoning and backdoor attacks without harming the CLIP performance. Our extensive experiments on CC3M, Visual Genome, and MSCOCO demonstrate that SAFECLIP significantly reduces the success rate of targeted data poisoning attacks from 93.75% to 0% and that of various backdoor attacks from up to 100% to 0%, without harming CLIP's performance.

</details>

### 16. Robust Contrastive Language-Image Pre-training against Data Poisoning and Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2303.06854) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2232e8fee69b150005ac420bfa83d705-Abstract-Conference.html)　📅 2023-03　🏷 NeurIPS 2023

**关键词**：`defense`、`RoCLIP`、`nearest neighbor`、`pair reassignment`

👤 **作者**：Wenhan Yang、Jingdong Gao、Baharan Mirzasoleiman

- 🎯 **研究动机**：CLIP 类多模态预训练对定向投毒与后门攻击极其脆弱，鲁棒预训练方法缺位
- 🔬 **研究方法**：ROCLIP 用大而多变的随机 caption 池做近邻重配对，每数轮将图像与池中最相似文本配对，辅以图文增强
- 📌 **结论**：定向投毒成功率从 93.75% 降至 12.5%、后门降至 0%，linear probe 性能反升 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive vision-language representation learning has achieved state-of-the-art performance for zero-shot classification, by learning from millions of image-caption pairs crawled from the internet. However, the massive data that powers large multimodal models such as CLIP, makes them extremely vulnerable to various types of targeted data poisoning and backdoor attacks. Despite this vulnerability, robust contrastive vision-language pre-training against such attacks has remained unaddressed. In this work, we propose ROCLIP, the first effective method for robust pre-training multimodal vision-language models against targeted data poisoning and backdoor attacks. ROCLIP effectively breaks the association between poisoned image-caption pairs by considering a relatively large and varying pool of random captions, and matching every image with the text that is most similar to it in the pool instead of its own caption, every few epochs.It also leverages image and text augmentations to further strengthen the defense and improve the performance of the model. Our extensive experiments show that ROCLIP renders state-of-the-art targeted data poisoning and backdoor attacks ineffective during pre-training CLIP models. In particular, ROCLIP decreases the success rate for targeted data poisoning attacks from 93.75% to 12.5% and that of backdoor attacks down to 0%, while improving the model's linear probe performance by 10% and maintains a similar zero shot performance compared to CLIP. By increasing the frequency of matching, ROCLIP is able to defend strong attacks, which add up to 1% poisoned examples to the data, and successfully maintain a low attack success rate of 12.5%, while trading off the performance on some tasks.

</details>

### 17. CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2303.03323) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2023/html/Bansal_CleanCLIP_Mitigating_Data_Poisoning_Attacks_in_Multimodal_Contrastive_Learning_ICCV_2023_paper.html)　📅 2023-03　🏷 ICCV 2023

**关键词**：`defense`、`CLIP fine-tuning`、`unimodal contrastive loss`、`poison mitigation`

👤 **作者**：Hritik Bansal、Nishad Singhi、Yu Yang、Fan Yin、Aditya Grover、Kai-Wei Chang

- 🎯 **研究动机**：300 万预训练数据中仅 75 个毒样本即可操纵 CLIP 行为，学到的触发-标签虚假关联难检测难遗忘
- 🔬 **研究方法**：CleanCLIP 微调用多模态对比加各模态单模自监督目标独立重对齐表征以削弱虚假关联；监督微调任务标注数据可从视觉编码器移除触发器
- 📌 **结论**：保持良性性能的同时擦除多模态对比学习的一系列后门攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive pretraining has been used to train multimodal representation models, such as CLIP, on large amounts of paired image-text data. However, previous studies have revealed that such models are vulnerable to backdoor attacks. Specifically, when trained on backdoored examples, CLIP learns spurious correlations between the embedded backdoor trigger and the target label, aligning their representations in the joint embedding space. Injecting even a small number of poisoned examples, such as 75 examples in 3 million pretraining data, can significantly manipulate the model's behavior, making it difficult to detect or unlearn such correlations. To address this issue, we propose CleanCLIP, a finetuning framework that weakens the learned spurious associations introduced by backdoor attacks by independently re-aligning the representations for individual modalities. We demonstrate that unsupervised finetuning using a combination of multimodal contrastive and unimodal self-supervised objectives for individual modalities can significantly reduce the impact of the backdoor attack. Additionally, we show that supervised finetuning on task-specific labeled image data removes the backdoor trigger from the CLIP vision encoder. We show empirically that CleanCLIP maintains model performance on benign examples while erasing a range of backdoor attacks on multimodal contrastive learning.

</details>

### 18. Not All Tokens Are Equal: Region-Aware Consistency Repair of Backdoors in MLLMs

📄 [arXiv](https://arxiv.org/abs/2608.24354)　📅 2026-08

**关键词**：`defense`、`RACER`、`model repair`、`layer-wise inconsistency`

👤 **作者**：Jiali Wei、…、Ting Liu

- 🎯 **研究动机**：MLLM 后门可藏于图像或文本 trigger，模型级修复面向传统分类器效果有限，推理时过滤又不移除后门
- 🔬 **研究方法**：RACER 对视觉/文本 token 区域分别归一化 layer-wise inconsistency，经 min-max 最坏扰动合成与对抗微调修复模型
- 📌 **结论**：仅用 100 个干净样本、无需 trigger 先验，36 种设置下平均 ASR 降至 1.1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

MLLMs are increasingly deployed in user-facing applications, yet they inherit backdoor risks from the pipelines used to construct them: triggers may reside in images, texts, or both. Existing model-level backdoor removal methods, largely designed for conventional classifiers, show limited effectiveness on MLLMs, while MLLM-specific defenses mainly operate at inference time, filtering suspicious inputs without removing the backdoor embedded in the model. To address this gap and eliminate latent backdoors from MLLMs at their source, we present RACER, a model-level repair framework motivated by a key observation: backdoors induce abnormal layer-to-layer evolution in internal representations, which we term the layer-wise inconsistency anomaly. Importantly, this anomaly is modality-dependent, concentrating primarily in the token region encoding the trigger features that the backdoor model actually relies on. RACER therefore decomposes the fused representation into visual and textual token regions, normalizes their layer-wise inconsistency separately, and recomposes them using modality-aware weights over a deep-layer window, yielding a region-aware inconsistency objective that better captures localized backdoor-induced anomalies. Through a min-max optimization, this objective drives worst-case perturbation synthesis and adversarial fine-tuning against the resulting perturbation to repair the model, suppressing the deep representational directional shifts on which backdoor behaviors rely. RACER requires only 100 clean samples and no knowledge of the trigger, attack objective, or even whether the input model contains a backdoor. Evaluations on three open-source MLLMs across 36 backdoor settings spanning image, text, and multimodal triggers show that RACER reduces the average ASR to 1.1%, reaching 0% in 32 settings, while preserving clean-task utility on both backdoor and clean models.

</details>

### 19. Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors

📄 [arXiv](https://arxiv.org/abs/2606.17815)　📅 2026-06

**关键词**：`audit`、`DIFE`、`deployment interface`、`BadTextTower`

👤 **作者**：Kunlan Xiang、Haomiao Yang、Wenbo Jiang

- 🎯 **研究动机**：CLIP 后门通常只在攻击原生任务上验证，被复用于特征提取、检索、重排等部署接口后暴露程度未知
- 🔬 **研究方法**：提出 DIFE（Deployment-Interface Footprint Evaluation）框架统一规定各接口的读出、触发通道、目标事件与指标，并做有效足迹诊断；针对发现的文本编码器载体缺口提出 BadTextTower
- 📌 **结论**：审计揭示：原生攻击成功不是 checkpoint 级风险证书，暴露跟随组件足迹，文本侧投毒不会带来文本编码器控制；BadTextTower 产生强文本条件检索/重排暴露而视觉复用近乎干净

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive Language-Image Pre-training models are widely reused across downstream interfaces, including feature extraction, retrieval, reranking, and selection. Existing CLIP backdoor, however, usually validate attacks on a small attack-native task, leaving unclear whether the same poisoned checkpoint remains exposed, weakens, or becomes not applicable when reused through other interfaces. We introduce DIFE, a Deployment-Interface Footprint Evaluation framework that audits backdoored CLIP checkpoints across deployment interfaces. DIFE makes various evaluations comparable by specifying each interface's component readout, trigger channel, target event, reference condition, and metric. DIFE also introduces effective-footprint diagnosis to identify the reusable CLIP component or component combination that carries exposure and explains where risk transfers. Auditing reproduced CLIP backdoors with DIFE reveals a structured landscape: native success is not a checkpoint-level risk certificate, exposure follows component footprints, text-side poisoning does not yield textual-encoder control, and some coupled attacks remain mechanism-bound. This audit reveals a import gapin existing CLIP backdoors: a textual encoder that itself becomes a reusable carrier of adversarial behavior. We therefore introduce BadTextTower to fill this gap. BadTextTower produces strong text-conditioned retrieval, reranking, and selection exposure while leaving visual-only reuse nearly clean.

</details>

### 20. EntropyScan: Towards Model-level Backdoor Detection in LVLMs via Visual Attention Entropy

📄 [arXiv](https://arxiv.org/abs/2605.15711)　📅 2026-05

**关键词**：`detection`、`model-level`、`Tsallis entropy`、`trigger-agnostic`

👤 **作者**：Xuanyu Ge、Zhongqi Wang、Jie Zhang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：LVLM 防御多为依赖训练数据或触发知识的样本级防御，判断给定模型是否带后门的模型级检测未探索
- 🔬 **研究方法**：发现后门注入破坏跨模态对齐、在良性样本的视觉注意力分配上留下结构异常；EntropyScan 从 LLM 浅层提取视觉注意力分布，以 Tsallis 熵量化并用参考锚定 Z-score 归一化
- 📌 **结论**：两种 LVLM 架构三种攻击场景下平均 F1 98.5%、AUC 96.6%，轻量且触发无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities across various tasks, yet they remain vulnerable to backdoor attacks. Existing defense methods predominantly focus on sample-level defense, which relies on the knowledge of training data or triggers. However, identifying whether a given model is backdoored remains a critical but unexplored task. To fill this gap, we propose EntropyScan, a lightweight and trigger-agnostic method for model-level backdoor detection in LVLMs. We first observe that backdoor injection disrupts the cross-modal alignment, resulting in pronounced structural anomalies in visual attention allocation on benign samples. Based on this insight, EntropyScan detects the backdoor models by quantifying such attention deviations. Specifically, it extracts visual attention distributions from the initial layers of the Large Language Model (LLM) and applies Tsallis entropy to capture these structural distortions. By employing a reference-anchored Z-score normalization on a small set of benign samples, it effectively identifies the backdoored model. Extensive experiments across two LVLMs architectures and three advanced attack scenarios show that EntropyScan achieves an F1 score of 98.5% in average and an AUC of 96.6%. Our code will be publicly available soon.

</details>

### 21. CLIP-Inspector: Model-Level Backdoor Detection for Prompt-Tuned CLIP via OOD Trigger Inversion

📄 [arXiv](https://arxiv.org/abs/2604.09101)　📅 2026-04　🏷 CVPR 2026

**关键词**：`detection`、`CLIP`、`OOD inversion`、`prompt tuning`

👤 **作者**：Akshit Jindal、Saket Anand、Chetan Arora、Vikram Goyal

- 🎯 **研究动机**：MLaaS 可经 prompt tuning 在不动 encoder 的情况下植入后门，encoder 级检测与数据清洗均无法判断交付模型是否带毒
- 🔬 **研究方法**：CLIP-Inspector 在白盒访问与无标注 OOD 图像池下为每类反演触发器并判定后门行为，反演触发器还可用于再对齐修复
- 📌 **结论**：1,000 张 OOD 图像单 epoch 反演即达 94% 检测准确率（47/50 模型），AUROC 0.973 远超基线的 0.495 与 0.687

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Organisations with limited data and computational resources increasingly outsource model training to Machine Learning as a Service (MLaaS) providers, who adapt vision-language models (VLMs) such as CLIP to downstream tasks via prompt tuning rather than training from scratch. This semi-honest setting creates a security risk where a malicious provider can follow the prompt-tuning protocol yet implant a backdoor, forcing triggered inputs to be classified into an attacker-chosen class, even for out-of-distribution (OOD) data. Such backdoors leave encoders untouched, making them undetectable to existing methods that focus on encoder corruption. Other data-level methods that sanitize data before training or during inference, also fail to answer the critical question, "Is the delivered model backdoored or not?" To address this model-level verification problem, we introduce CLIP-Inspector (CI), a backdoor detection method designed for prompt-tuned CLIP models. Assuming white-box access to the delivered model and a pool of unlabeled OOD images, CI reconstructs possible triggers for each class to determine if the model exhibits backdoor behaviour or not. Additionally, we demonstrate that using CI's reconstructed trigger for fine-tuning on correctly labeled triggered inputs enables us to re-align the model and reduce backdoor effectiveness. Through extensive experiments across ten datasets and four backdoor attacks, we demonstrate that CI can reconstruct effective triggers in a single epoch using only 1,000 OOD images, achieving a 94% detection accuracy (47/50 models). Compared to adapted trigger-inversion baselines, CI yields a markedly higher AUROC score (0.973 vs 0.495/0.687), thus enabling the vetting and post-hoc repair of prompt-tuned CLIP models to ensure safe deployment.

</details>

### 22. BackdoorIDS: Zero-shot Backdoor Detection for Pretrained Vision Encoder

📄 [arXiv](https://arxiv.org/abs/2603.11664)　📅 2026-03

**关键词**：`detection`、`vision encoder`、`zero-shot`、`supply chain`

👤 **作者**：Siquan Huang、Yijiang Li、Ningzhi Gao、Xingfu Yan、Leyu Shi、Ying Gao

- 🎯 **研究动机**：下游用户依赖来源不明的第三方预训练视觉编码器，暴露于后门风险，现有检测需运行模型且依赖触发器
- 🔬 **研究方法**：利用 Attention Hijacking 与 Restoration：渐进掩码下后门图像嵌入会突变，对掩码轨迹上的嵌入序列做 DBSCAN 聚类，多于一个簇即判后门
- 📌 **结论**：零样本、免重训即插即用，跨攻击类型、数据集与 CNN/ViT/CLIP/LLaVA 模型族一致超越现有防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised and multimodal vision encoders learn strong visual representations that are widely adopted in downstream vision tasks and large vision-language models (LVLMs). However, downstream users often rely on third-party pretrained encoders with uncertain provenance, exposing them to backdoor attacks. In this work, we propose BackdoorIDS, a simple yet effective zero-shot, inference-time backdoor samples detection method for pretrained vision encoders. BackdoorIDS is motivated by two observations: Attention Hijacking and Restoration. Under progressive input masking, a backdoored image initially concentrates attention on malicious trigger features. Once the masking ratio exceeds the trigger's robustness threshold, the trigger is deactivated, and attention rapidly shifts to benign content. This transition induces a pronounced change in the image embedding, whereas embeddings of clean images evolve more smoothly across masking progress. BackdoorIDS operationalizes this signal by extracting an embedding sequence along the masking trajectory and applying density-based clustering such as DBSCAN. An input is flagged as backdoored if its embedding sequence forms more than one cluster. Extensive experiments show that BackdoorIDS consistently outperforms existing defenses across diverse attack types, datasets, and model families. Notably, it is a plug-and-play approach that requires no retraining and operates fully zero-shot at inference time, making it compatible with a wide range of encoder architectures, including CNNs, ViTs, CLIP, and LLaVA-1.5.

</details>

### 23. InverTune: Removing Backdoors from Multimodal Contrastive Learning Models via Trigger Inversion and Activation Tuning

📄 [arXiv](https://arxiv.org/abs/2506.12411) · 🌐 [Project](https://www.ndss-symposium.org/wp-content/uploads/2026-f1666-paper.pdf)　📅 2026-02　🏷 NDSS 2026

**关键词**：`defense`、`trigger inversion`、`activation tuning`、`minimal clean data`

👤 **作者**：Mengyuan Sun、Yu Li、Yuchen Liu、Bo Du、Yunjie Ge

- 🎯 **研究动机**：多模态对比模型的后门防御依赖攻击者知识或大量干净数据，不实用
- 🔬 **研究方法**：提出 InverTune：对抗模拟暴露攻击签名、梯度反演重建隐触发器、聚类引导微调擦除后门，仅需少量任意干净数据
- 📌 **结论**：对 SoTA 攻击平均 ASR 降 97.87%，干净精度损失仅 3.07%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive learning models like CLIP have demonstrated remarkable vision-language alignment capabilities, yet their vulnerability to backdoor attacks poses critical security risks. Attackers can implant latent triggers that persist through downstream tasks, enabling malicious control of model behavior upon trigger presentation. Despite great success in recent defense mechanisms, they remain impractical due to strong assumptions about attacker knowledge or excessive clean data requirements. In this paper, we introduce InverTune, the first backdoor defense framework for multimodal models under minimal attacker assumptions, requiring neither prior knowledge of attack targets nor access to the poisoned dataset. Unlike existing defense methods that rely on the same dataset used in the poisoning stage, InverTune effectively identifies and removes backdoor artifacts through three key components, achieving robust protection against backdoor attacks. Specifically, InverTune first exposes attack signatures through adversarial simulation, probabilistically identifying the target label by analyzing model response patterns. Building on this, we develop a gradient inversion technique to reconstruct latent triggers through activation pattern analysis. Finally, a clustering-guided fine-tuning strategy is employed to erase the backdoor function with only a small amount of arbitrary clean data, while preserving the original model capabilities. Experimental results show that InverTune reduces the average attack success rate (ASR) by 97.87% against the state-of-the-art (SOTA) attacks while limiting clean accuracy (CA) degradation to just 3.07%. This work establishes a new paradigm for securing multimodal systems, advancing security in foundation model deployment without compromising performance.

</details>

### 24. Robust Defense Strategies for Multimodal Contrastive Learning: Efficient Fine-tuning against Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2511.13545) · 🌐 [Project](https://link.springer.com/article/10.1007/s11042-026-21339-x)　📅 2026-01

**关键词**：`defense`、`efficient fine-tuning`、`multimodal contrastive model`、`utility`

👤 **作者**：Md. Iqbal Hossain、Afia Sajeeda、Neeresh Kumar Perla、Ming Shao

- 🎯 **研究动机**：被投毒的多模态对比checkpoint缺高效修复方案
- 🔬 **研究方法**：系统比较并改进面向poisoned checkpoint的高效fine-tuning防御
- 📌 **结论**：在后门移除强度与clean utility间取得可部署折中

### 25. Assimilation Matters: Model-level Backdoor Detection in Vision-Language Pretrained Models

📄 [arXiv](https://arxiv.org/abs/2512.00343)　📅 2025-12

**关键词**：`detection`、`AMDET`、`feature assimilation`、`text encoder`

👤 **作者**：Zhongqi Wang、Jie Zhang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：现有 VLP 后门检测依赖训练数据、触发器或下游分类器等先验知识，现实场景难用
- 🔬 **研究方法**：发现后门文本编码器的 feature assimilation 现象（样本内所有 token 表示高度相似、注意力集中于触发 token），AMDET 借梯度反演恢复可激活后门的隐式特征扫描模型，并以 loss landscape 过滤 CLIP 天然存在的类后门特征
- 📌 **结论**：在 3600 个后门与良性微调模型上 F1 达 89.90%，单次检测约 5 分钟，抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language pretrained models (VLPs) such as CLIP have achieved remarkable success, but are also highly vulnerable to backdoor attacks. Given a model fine-tuned by an untrusted third party, determining whether the model has been injected with a backdoor is a critical and challenging problem. Existing detection methods usually rely on prior knowledge of training dataset, backdoor triggers and targets, or downstream classifiers, which may be impractical for real-world applications. To address this, To address this challenge, we introduce Assimilation Matters in DETection (AMDET), a novel model-level detection framework that operates without any such prior knowledge. Specifically, we first reveal the feature assimilation property in backdoored text encoders: the representations of all tokens within a backdoor sample exhibit a high similarity. Further analysis attributes this effect to the concentration of attention weights on the trigger token. Leveraging this insight, AMDET scans a model by performing gradient-based inversion on token embeddings to recover implicit features that capable of activating backdoor behaviors. Furthermore, we identify the natural backdoor feature in the OpenAI's official CLIP model, which are not intentionally injected but still exhibit backdoor-like behaviors. We then filter them out from real injected backdoor by analyzing their loss landscapes. Extensive experiments on 3,600 backdoored and benign-finetuned models with two attack paradigms and three VLP model structures show that AMDET detects backdoors with an F1 score of 89.90%. Besides, it achieves one complete detection in approximately 5 minutes on a RTX 4090 GPU and exhibits strong robustness against adaptive attacks. Code is available at: https://github.com/Robin-WZQ/AMDET

</details>

### 26. Lie Detector: Unified Backdoor Detection via Cross-Examination Framework

📄 [arXiv](https://arxiv.org/abs/2503.16872)　📅 2025-03

**关键词**：`detection`、`cross-examination`、`black-box`、`model inconsistency`、`MLLM`

👤 **作者**：Xuan Wang、…、Xitong Gao

- 🎯 **研究动机**：半诚实外包训练下投毒可植入后门，现有统计检测难以跨学习范式保持精度
- 🔬 **研究方法**：提出 Lie Detector，交叉审查两个独立服务商模型的不一致性，用 central kernel alignment 恢复触发器并以微调敏感性区分对抗扰动
- 📌 **结论**：监督、半监督、自回归任务检测精度分别超 SoTA 5.4%、1.6%、11.9%，并首次检测 MLLM 后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Institutions with limited data and computing resources often outsource model training to third-party providers in a semi-honest setting, assuming adherence to prescribed training protocols with pre-defined learning paradigm (e.g., supervised or semi-supervised learning). However, this practice can introduce severe security risks, as adversaries may poison the training data to embed backdoors into the resulting model. Existing detection approaches predominantly rely on statistical analyses, which often fail to maintain universally accurate detection accuracy across different learning paradigms. To address this challenge, we propose a unified backdoor detection framework in the semi-honest setting that exploits cross-examination of model inconsistencies between two independent service providers. Specifically, we integrate central kernel alignment to enable robust feature similarity measurements across different model architectures and learning paradigms, thereby facilitating precise recovery and identification of backdoor triggers. We further introduce backdoor fine-tuning sensitivity analysis to distinguish backdoor triggers from adversarial perturbations, substantially reducing false positives. Extensive experiments demonstrate that our method achieves superior detection performance, improving accuracy by 5.4%, 1.6%, and 11.9% over SoTA baselines across supervised, semi-supervised, and autoregressive learning tasks, respectively. Notably, it is the first to effectively detect backdoors in multimodal large language models, further highlighting its broad applicability and advancing secure deep learning.

</details>

### 27. Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP

📄 [arXiv](https://arxiv.org/abs/2502.19269)　📅 2025-02

**关键词**：`defense`、`class-wise prompt`、`CLIP purification`、`parameter efficient`

👤 **作者**：Jiawei Kong、…、Ke Xu

- 🎯 **研究动机**：全模型微调参数庞大、优化方向不稳，抗 SOTA 攻击差且降干净精度
- 🔬 **研究方法**：CBPT 先以正负样本对比学习反演假触发器，再用三个损失优化类级文本 prompt 修正决策边界
- 📌 **结论**：七种主流攻击下平均干净精度 58.83%、ASR 仅 0.39%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While pre-trained Vision-Language Models (VLMs) such as CLIP exhibit impressive representational capabilities for multimodal data, recent studies have revealed their vulnerability to backdoor attacks. To alleviate the threat, existing defense strategies primarily focus on fine-tuning the entire suspicious model. However, the substantial model parameters increase the difficulty of reaching a stable and consistent optimization direction, limiting their resistance against state-of-the-art attacks and often resulting in a degradation of clean accuracy. To address this challenge, we propose Class-wise Backdoor Prompt Tuning (CBPT), an efficient and effective defense mechanism that operates on text prompts to indirectly purify poisoned CLIP. Specifically, we first employ the advanced contrastive learning via carefully crafted positive and negative samples, to effectively invert the backdoor triggers that are potentially adopted by the attacker. Once the dummy trigger is established, we leverage three well-designed loss functions to optimize these class-wise text prompts, modifying the model's decision boundary and further reclassifying the feature regions affected by backdoor triggers. Extensive experiments demonstrate that CBPT significantly mitigates backdoor threats while preserving model utility, e.g. an average Clean Accuracy (CA) of 58.83% and an Attack Success Rate (ASR) of 0.39% across seven mainstream backdoor attacks. These results underscore the superiority of our prompt purifying design to strengthen CLIP's robustness against backdoor attacks.

</details>

### 28. Perturb and Recover: Fine-tuning for Effective Backdoor Removal from CLIP

📄 [arXiv](https://arxiv.org/abs/2412.00727)　📅 2024-12

**关键词**：`defense`、`perturbation`、`recovery fine-tuning`、`CLIP repair`

👤 **作者**：Naman Deep Singh、Francesco Croce、Matthias Hein

- 🎯 **研究动机**：现有 CLIP 清洗技术对 Blended、BadNet 等简单结构触发器无效
- 🔬 **研究方法**：PAR 采用先扰动再恢复的微调机制清除后门，甚至仅用合成图文对即可完成
- 📌 **结论**：跨编码器与攻击类型实现高后门清除率且保持标准性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language models like CLIP have been shown to be highly effective at linking visual perception and natural language understanding, enabling sophisticated image-text capabilities, including strong retrieval and zero-shot classification performance. Their widespread use, as well as the fact that CLIP models are trained on image-text pairs from the web, make them both a worthwhile and relatively easy target for backdoor attacks. As training foundational models, such as CLIP, from scratch is very expensive, this paper focuses on cleaning potentially poisoned models via fine-tuning. We first show that existing cleaning techniques are not effective against simple structured triggers used in Blended or BadNet backdoor attacks, exposing a critical vulnerability for potential real-world deployment of these models. Then, we introduce PAR, Perturb and Recover, a surprisingly simple yet effective mechanism to remove backdoors from CLIP models. Through extensive experiments across different encoders and types of backdoor attacks, we show that PAR achieves high backdoor removal rate while preserving good standard performance. Finally, we illustrate that our approach is effective even only with synthetic text-image pairs, i.e. without access to real training data. The code and models are available on \href{https://github.com/nmndeep/PerturbAndRecover}{GitHub}.

</details>

### 29. Defending Multimodal Backdoored Models by Repulsive Visual Prompt Tuning

📄 [arXiv](https://arxiv.org/abs/2412.20392) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f5e449418dd694117f3b4ae6dcfe62a9-Abstract-Conference.html)　📅 2024-12　🏷 NeurIPS 2025

**关键词**：`defense`、`RVPT`、`visual prompt`、`repulsive representation`

👤 **作者**：Zhifang Zhang、Shuo He、Haobo Wang、Bingquan Shen、Lei Feng

- 🎯 **研究动机**：CLIP 倾向编码数据集预测模式之外的特征，视觉特征易被触发器重塑
- 🔬 **研究方法**：RVPT 以深度视觉提示调优加特征排斥损失，仅编码下游可判别特征，只需少样本干净数据并微调极少参数
- 📌 **结论**：仅调 0.27% 参数即把最先进多模态攻击 ASR 从 89.70% 降至 2.76%，并跨数据集泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive learning models (e.g., CLIP) can learn high-quality representations from large-scale image-text datasets, while they exhibit significant vulnerabilities to backdoor attacks, raising serious safety concerns. In this paper, we reveal that CLIP's vulnerabilities primarily stem from its tendency to encode features beyond in-dataset predictive patterns, compromising its visual feature resistivity to input perturbations. This makes its encoded features highly susceptible to being reshaped by backdoor triggers. To address this challenge, we propose Repulsive Visual Prompt Tuning (RVPT), a novel defense approach that employs deep visual prompt tuning with a specially designed feature-repelling loss. Specifically, RVPT adversarially repels the encoded features from deeper layers while optimizing the standard cross-entropy loss, ensuring that only predictive features in downstream tasks are encoded, thereby enhancing CLIP's visual feature resistivity against input perturbations and mitigating its susceptibility to backdoor attacks. Unlike existing multimodal backdoor defense methods that typically require the availability of poisoned data or involve fine-tuning the entire model, RVPT leverages few-shot downstream clean samples and only tunes a small number of parameters. Empirical results demonstrate that RVPT tunes only 0.27\% of the parameters in CLIP, yet it significantly outperforms state-of-the-art defense methods, reducing the attack success rate from 89.70\% to 2.76\% against the most advanced multimodal attacks on ImageNet and effectively generalizes its defensive capabilities across multiple datasets.

</details>

### 30. CleanerCLIP: Fine-grained Counterfactual Semantic Augmentation for Backdoor Defense

📄 [arXiv](https://arxiv.org/abs/2409.17601)　📅 2024-09

**关键词**：`defense`、`counterfactual augmentation`、`semantic alignment`、`CLIP`

👤 **作者**：Yuan Xun、Siyuan Liang、Xiaojun Jia、Xinwei Liu、Xiaochun Cao

- 🎯 **研究动机**：CleanCLIP 的同义词文本增强不足以强化文本特征空间，难挡复杂攻击
- 🔬 **研究方法**：TA-Cleaner 每轮随机选少量样本生成正反子文本并与图像对齐，加强文本自监督以切断触发器特征连接
- 📌 **结论**：微调式防御中达 SOTA；面对 BadCLIP 时 Top-1/Top-10 ASR 较 CleanCLIP 再降 52.02%/63.88%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained large models for multimodal contrastive learning, such as CLIP, have been widely recognized in the industry as highly susceptible to data-poisoned backdoor attacks. This poses significant risks to downstream model training. In response to such potential threats, finetuning offers a simpler and more efficient defense choice compared to retraining large models with augmented data. In the supervised learning domain, fine-tuning defense strategies can achieve excellent defense performance. However, in the unsupervised and semi-supervised domain, we find that when CLIP faces some complex attack techniques, the existing fine-tuning defense strategy, CleanCLIP, has some limitations on defense performance. The synonym substitution of its text-augmentation is insufficient to enhance the text feature space. To compensate for this weakness, we improve it by proposing a fine-grained \textbf{T}ext \textbf{A}lignment \textbf{C}leaner (TA-Cleaner) to cut off feature connections of backdoor triggers. We randomly select a few samples for positive and negative subtext generation at each epoch of CleanCLIP, and align the subtexts to the images to strengthen the text self-supervision. We evaluate the effectiveness of our TA-Cleaner against six attack algorithms and conduct comprehensive zero-shot classification tests on ImageNet1K. Our experimental results demonstrate that TA-Cleaner achieves state-of-the-art defensiveness among finetuning-based defense techniques. Even when faced with the novel attack technique BadCLIP, our TA-Cleaner outperforms CleanCLIP by reducing the ASR of Top-1 and Top-10 by 52.02\% and 63.88\%, respectively.

</details>

### 31. Adversarial Backdoor Defense in CLIP

📄 [arXiv](https://arxiv.org/abs/2409.15968)　📅 2024-09

**关键词**：`defense`、`adversarial training`、`CLIP`、`backdoor removal`

👤 **作者**：Junhao Kuang、Siyuan Liang、Jiawei Liang、Kuanrong Liu、Xiaochun Cao

- 🎯 **研究动机**：现有 CLIP 后门防御的常规数据增强抓不住后门样本特征
- 🔬 **研究方法**：利用对抗样本与后门样本在被攻模型特征空间的相似性，ABD 用精心构造的对抗样本做特征对齐切断后门关联
- 📌 **结论**：较 CleanCLIP 对 BadNet/Blended/BadCLIP 的 ASR 再降 8.66%/10.52%/53.64%，干净精度平均仅降 1.73%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive pretraining, exemplified by models like CLIP, has been found to be vulnerable to backdoor attacks. While current backdoor defense methods primarily employ conventional data augmentation to create augmented samples aimed at feature alignment, these methods fail to capture the distinct features of backdoor samples, resulting in suboptimal defense performance. Observations reveal that adversarial examples and backdoor samples exhibit similarities in the feature space within the compromised models. Building on this insight, we propose Adversarial Backdoor Defense (ABD), a novel data augmentation strategy that aligns features with meticulously crafted adversarial examples. This approach effectively disrupts the backdoor association. Our experiments demonstrate that ABD provides robust defense against both traditional uni-modal and multimodal backdoor attacks targeting CLIP. Compared to the current state-of-the-art defense method, CleanCLIP, ABD reduces the attack success rate by 8.66% for BadNet, 10.52% for Blended, and 53.64% for BadCLIP, while maintaining a minimal average decrease of just 1.73% in clean accuracy.

</details>

### 32. Efficient Backdoor Defense in Multimodal Contrastive Learning: A Token-Level Unlearning Method for Mitigating Threats

📄 [arXiv](https://arxiv.org/abs/2409.19526)　📅 2024-09

**关键词**：`defense`、`UBT`、`suspicious-sample mining`、`token-level unlearning`

👤 **作者**：Kuanrong Liu、Siyuan Liang、Jiawei Liang、Pengwen Dai、Xiaochun Cao

- 🎯 **研究动机**：多模态对比学习的后门防御训练耗时长且降干净精度
- 🔬 **研究方法**：UBT 用少量毒样本过拟合训练强化后门捷径以定位可疑样本，再做 token 级部分遗忘训练快速解除后门
- 📌 **结论**：较 SOTA 攻击成功率再降 19%，干净精度反升 2.57%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive learning uses various data modalities to create high-quality features, but its reliance on extensive data sources on the Internet makes it vulnerable to backdoor attacks. These attacks insert malicious behaviors during training, which are activated by specific triggers during inference, posing significant security risks. Despite existing countermeasures through fine-tuning that reduce the malicious impacts of such attacks, these defenses frequently necessitate extensive training time and degrade clean accuracy. In this study, we propose an efficient defense mechanism against backdoor threats using a concept known as machine unlearning. This entails strategically creating a small set of poisoned samples to aid the model's rapid unlearning of backdoor vulnerabilities, known as Unlearn Backdoor Threats (UBT). We specifically use overfit training to improve backdoor shortcuts and accurately detect suspicious samples in the potential poisoning data set. Then, we select fewer unlearned samples from suspicious samples for rapid forgetting in order to eliminate the backdoor effect and thus improve backdoor defense efficiency. In the backdoor unlearning process, we present a novel token-based portion unlearning training regime. This technique focuses on the model's compromised elements, dissociating backdoor correlations while maintaining the model's overall integrity. Extensive experimental results show that our method effectively defends against various backdoor attack methods in the CLIP model. Compared to SoTA backdoor defense methods, UBT achieves the lowest attack success rate while maintaining a high clean accuracy of the model (attack success rate decreases by 19% compared to SOTA, while clean accuracy increases by 2.57%).

</details>

### 33. Unlearning Backdoor Threats: Enhancing Backdoor Defense in Multimodal Contrastive Learning via Local Token Unlearning

📄 [arXiv](https://arxiv.org/abs/2403.16257)　📅 2024-03　🏷 CVPR 2024

**关键词**：`defense`、`UBT`、`local token unlearning`、`contrastive model`

👤 **作者**：Siyuan Liang、…、Xiaochun Cao

- 🎯 **研究动机**：多模态对比学习的后门防御依赖微调，伤 clean accuracy 且需大量干净配对
- 🔬 **研究方法**：UBT 以少量毒样本过拟合训练强化后门捷径以定位可疑样本，再做 token 级局部遗忘训练定向解除后门关联
- 📌 **结论**：将攻击成功率压至最低同时保持模型高干净精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal contrastive learning has emerged as a powerful paradigm for building high-quality features using the complementary strengths of various data modalities. However, the open nature of such systems inadvertently increases the possibility of backdoor attacks. These attacks subtly embed malicious behaviors within the model during training, which can be activated by specific triggers in the inference phase, posing significant security risks. Despite existing countermeasures through fine-tuning that reduce the adverse impacts of such attacks, these defenses often degrade the clean accuracy and necessitate the construction of extensive clean training pairs. In this paper, we explore the possibility of a less-cost defense from the perspective of model unlearning, that is, whether the model can be made to quickly \textbf{u}nlearn \textbf{b}ackdoor \textbf{t}hreats (UBT) by constructing a small set of poisoned samples. Specifically, we strengthen the backdoor shortcuts to discover suspicious samples through overfitting training prioritized by weak similarity samples. Building on the initial identification of suspicious samples, we introduce an innovative token-based localized forgetting training regime. This technique specifically targets the poisoned aspects of the model, applying a focused effort to unlearn the backdoor associations and trying not to damage the integrity of the overall model. Experimental results show that our method not only ensures a minimal success rate for attacks, but also preserves the model's high clean accuracy.

</details>

### 34. TIJO: Trigger Inversion with Joint Optimization for Defending Multimodal Backdoored Models

📄 [arXiv](https://arxiv.org/abs/2308.03906) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2023/html/Sur_TIJO_Trigger_Inversion_with_Joint_Optimization_for_Defending_Multimodal_Backdoored_ICCV_2023_paper.html)　📅 2023-08　🏷 ICCV 2023

**关键词**：`detection`、`VQA`、`joint inversion`、`dual-key trigger`

👤 **作者**：Indranil Sur、…、Susmit Jha

- 🎯 **研究动机**：dual-key 后门触发器分散在图文两模态，单模态触发反演方法失效
- 🔬 **研究方法**：TIJO 联合优化反演双模态触发器，关键是在目标检测框特征空间而非像素空间反演
- 📌 **结论**：TrojVQA 上多模态双键后门检测 AUC 从 0.6 升至 0.92，对单模态后门亦领先

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present a Multimodal Backdoor Defense technique TIJO (Trigger Inversion using Joint Optimization). Recent work arXiv:2112.07668 has demonstrated successful backdoor attacks on multimodal models for the Visual Question Answering task. Their dual-key backdoor trigger is split across two modalities (image and text), such that the backdoor is activated if and only if the trigger is present in both modalities. We propose TIJO that defends against dual-key attacks through a joint optimization that reverse-engineers the trigger in both the image and text modalities. This joint optimization is challenging in multimodal models due to the disconnected nature of the visual pipeline which consists of an offline feature extractor, whose output is then fused with the text using a fusion module. The key insight enabling the joint optimization in TIJO is that the trigger inversion needs to be carried out in the object detection box feature space as opposed to the pixel space. We demonstrate the effectiveness of our method on the TrojVQA benchmark, where TIJO improves upon the state-of-the-art unimodal methods from an AUC of 0.6 to 0.92 on multimodal dual-key backdoors. Furthermore, our method also improves upon the unimodal baselines on unimodal backdoors. We present ablation studies and qualitative results to provide insights into our algorithm such as the critical importance of overlaying the inverted feature triggers on all visual features during trigger inversion. The prototype implementation of TIJO is available at https://github.com/SRI-CSL/TIJO.

</details>

### 35. SEER: Backdoor Detection for Vision-Language Models through Searching Target Text and Image Trigger Jointly

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/28611)　📅 2023　🏷 AAAI 2024

**关键词**：`detection`、`VLM`、`joint search`、`trigger inversion`

- 🎯 **研究动机**：VLM后门检测只查单一输入通道易漏检
- 🔬 **研究方法**：SEER联合搜索target text与image trigger做跨模态触发反转
- 📌 **结论**：跨模态联合异常判定提升后门检出

### 36. Detecting Backdoors in Pre-trained Encoders

📄 [arXiv](https://arxiv.org/abs/2303.15180) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2023/html/Feng_Detecting_Backdoors_in_Pre-Trained_Encoders_CVPR_2023_paper.html)　📅 2023-03　🏷 CVPR 2023

**关键词**：`detection`、`DECREE`、`encoder audit`、`trigger inversion`

👤 **作者**：Shiwei Feng、…、Xiangyu Zhang

- 🎯 **研究动机**：编码器后门可被下游分类器继承，现有检测面向监督设定、无法处理无标签的预训练编码器
- 🔬 **研究方法**：DECREE 首个预训练编码器后门检测方法，无需分类器头与输入标签
- 📌 **结论**：在 400 余个经三种范式投毒的编码器上保持高检测准确率，含 ImageNet 与 CLIP 四亿图文对预训练编码器，且只需有限甚至无预训练数据访问

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning in computer vision trains on unlabeled data, such as images or (image, text) pairs, to obtain an image encoder that learns high-quality embeddings for input data. Emerging backdoor attacks towards encoders expose crucial vulnerabilities of self-supervised learning, since downstream classifiers (even further trained on clean data) may inherit backdoor behaviors from encoders. Existing backdoor detection methods mainly focus on supervised learning settings and cannot handle pre-trained encoders especially when input labels are not available. In this paper, we propose DECREE, the first backdoor detection approach for pre-trained encoders, requiring neither classifier headers nor input labels. We evaluate DECREE on over 400 encoders trojaned under 3 paradigms. We show the effectiveness of our method on image encoders pre-trained on ImageNet and OpenAI's CLIP 400 million image-text pairs. Our method consistently has a high detection accuracy even if we have only limited or no access to the pre-training dataset.

</details>

### 37. Region-Level Black-Box Defense Against Stealthy Embedding-Space Backdoors in CLIP

🌐 [Project](https://link.springer.com/chapter/10.1007/978-981-92-1947-6_20)　📅 2026-06　🏷 KDD 2026

**关键词**：`defense`、`CLIPGuard`、`black-box`、`region masking`

- 🎯 **研究动机**：CLIP嵌入空间后门隐蔽，黑盒防御缺手段
- 🔬 **研究方法**：CLIPGuard比较局部区域遮蔽前后的embedding与prediction变化
- 📌 **结论**：不访问CLIP参数即可定位并净化触发区域

### 38. Probing Semantic Insensitivity for Inference-Time Backdoor Defense in Multimodal Large Language Model

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40891)　📅 2026-03　🏷 AAAI 2026

**关键词**：`detection`、`Trap on Text`、`semantic perturbation`、`black-box`

- 🎯 **研究动机**：黑盒条件下MLLM后门缺推理时检测手段
- 🔬 **研究方法**：Trap on Text注入语义扰动，利用trigger区域的语义不敏感性探测激活
- 📌 **结论**：无需权重或clean reference即完成后门检测

### 39. PurMM: Attention-Guided Test-Time Backdoor Purification in Multimodal Large Language Models

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40867)　📅 2026-03　🏷 AAAI 2026

**关键词**：`defense`、`attention hijacking`、`visual-token pruning`、`test time`

- 🎯 **研究动机**：MLLM后门经attention hijacking劫持视觉token，重训代价高
- 🔬 **研究方法**：PurMM逐层定位异常attention视觉token，用深层线索筛选后置零相应embedding分量
- 📌 **结论**：免重训的测试时净化即可恢复benign answer

### 40. Test-Time Attention Purification for Backdoored Large Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2603.12989) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Test-Time_Attention_Purification_for_Backdoored_Large_Vision_Language_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`CleanSight`、`attention stealing`、`token pruning`、`LVLM backdoor`、`attention purification`

👤 **作者**：Zhifang Zhang、…、Miao Xu

- 🎯 **研究动机**：LVLM 后门防御依赖干净数据重训适配器或 LoRA，计算昂贵且损伤性能
- 🔬 **研究方法**：机制发现 attention stealing：触发视觉 token 经异常跨模态注意力重分配窃取文本注意力；CleanSight 推理时按视觉-文本注意力比检测并剪枝可疑高注意力 token
- 📌 **结论**：免训练即插即用，跨数据集与攻击类型显著优于像素级净化防御，并保持干净与中毒样本上的效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the strong multimodal performance, large vision-language models (LVLMs) are vulnerable during fine-tuning to backdoor attacks, where adversaries insert trigger-embedded samples into the training data to implant behaviors that can be maliciously activated at test time. Existing defenses typically rely on retraining backdoored parameters (e.g., adapters or LoRA modules) with clean data, which is computationally expensive and often degrades model performance. In this work, we provide a new mechanistic understanding of backdoor behaviors in LVLMs: the trigger does not influence prediction through low-level visual patterns, but through abnormal cross-modal attention redistribution, where trigger-bearing visual tokens steal attention away from the textual context - a phenomenon we term attention stealing. Motivated by this, we propose CleanSight, a training-free, plug-and-play defense that operates purely at test time. CleanSight (i) detects poisoned inputs based on the relative visual-text attention ratio in selected cross-modal fusion layers, and (ii) purifies the input by selectively pruning the suspicious high-attention visual tokens to neutralize the backdoor activation. Extensive experiments show that CleanSight significantly outperforms existing pixel-based purification defenses across diverse datasets and backdoor attack types, while preserving the model's utility on both clean and poisoned samples.

</details>

### 41. SRD: Reinforcement-Learned Semantic Perturbation for Backdoor Defense in VLMs

📄 [arXiv](https://arxiv.org/abs/2506.04743) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/38121)　📅 2025-06　🏷 AAAI 2026

**关键词**：`defense`、`semantic perturbation`、`deep Q-learning`、`caption repair`

👤 **作者**：Shuhan Xu、…、Dacheng Tao

- 🎯 **研究动机**：VLM 描述任务的后门触发隐蔽且跨模态传播，难以检测与防御
- 🔬 **研究方法**：基于注意力异常集中与语义漂移两类特征，提出 SRD：深度 Q 网络学习对敏感区域施加离散扰动，以语义保真分数为奖励
- 📌 **结论**：无需触发器先验即将 TrojVLM 与 Shadowcast 的 ASR 降至 3.6% 与 5.6%，干净输入 CIDEr 平均降幅小于 15%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual language models (VLMs) have made significant progress in image captioning tasks, yet recent studies have found they are vulnerable to backdoor attacks. Attackers can inject undetectable perturbations into the data during inference, triggering abnormal behavior and generating malicious captions. These attacks are particularly challenging to detect and defend against due to the stealthiness and cross-modal propagation of the trigger signals. In this paper, we identify two key vulnerabilities by analyzing existing attack patterns: (1) the model exhibits abnormal attention concentration on certain regions of the input image, and (2) backdoor attacks often induce semantic drift and sentence incoherence. Based on these insights, we propose Semantic Reward Defense (SRD), a reinforcement learning framework that mitigates backdoor behavior without requiring any prior knowledge of trigger patterns. SRD learns to apply discrete perturbations to sensitive contextual regions of image inputs via a deep Q-network policy, aiming to confuse attention and disrupt the activation of malicious paths. To guide policy optimization, we design a reward signal named semantic fidelity score, which jointly assesses the semantic consistency and linguistic fluency of the generated captions, encouraging the agent to achieve a robust yet faithful output. SRD offers a trigger-agnostic, policy-interpretable defense paradigm that effectively mitigates local (TrojVLM) and global (Shadowcast) backdoor attacks, reducing ASR to 3.6% and 5.6% respectively, with less than 15% average CIDEr drop on the clean inputs. Our codes can be found at https://github.com/Ciconey/SRD.git.

</details>

### 42. DeDe: Detecting Backdoor Samples for SSL Encoders via Decoders

📄 [arXiv](https://arxiv.org/abs/2411.16154) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Hou_DeDe_Detecting_Backdoor_Samples_for_SSL_Encoders_via_Decoders_CVPR_2025_paper.html)　📅 2024-11　🏷 CVPR 2025

**关键词**：`detection`、`SSL／CLIP encoder`、`decoder reconstruction`、`test time`

👤 **作者**：Sizai Hou、Songze Li、Duanyi Yao

- 🎯 **研究动机**：SSL 编码器后门防御研究有限，现有方法难以检出高级隐蔽后门
- 🔬 **研究方法**：DeDe 用辅助数据为编码器训练 decoder，触发输入被误导到目标嵌入时解码输出与输入差异显著，据此推理期检测
- 📌 **结论**：对比学习与 CLIP 模型上检测有效，优于 SOTA 检测方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) is pervasively exploited in training high-quality upstream encoders with a large amount of unlabeled data. However, it is found to be susceptible to backdoor attacks merely via polluting a small portion of training data. The victim encoders associate triggered inputs with target embeddings, e.g., mapping a triggered cat image to an airplane embedding, such that the downstream tasks inherit unintended behaviors when the trigger is activated. Emerging backdoor attacks have shown great threats across different SSL paradigms such as contrastive learning and CLIP, yet limited research is devoted to defending against such attacks, and existing defenses fall short in detecting advanced stealthy backdoors. To address the limitations, we propose a novel detection mechanism, DeDe, which detects the activation of backdoor mappings caused by triggered inputs on victim encoders. Specifically, DeDe trains a decoder for any given SSL encoder using an auxiliary dataset (which can be out-of-distribution or even slightly poisoned), so that for any triggered input that misleads the encoder into the target embedding, the decoder generates an output image significantly different from the input. DeDe leverages the discrepancy between the input and the decoded output to identify potential backdoor misbehavior during inference. We empirically evaluate DeDe on both contrastive learning and CLIP models against various types of backdoor attacks. Our results demonstrate promising detection effectiveness over various advanced attacks and superior performance compared over state-of-the-art detection methods.

</details>

### 43. Test-Time Multimodal Backdoor Detection by Contrastive Prompting

📄 [arXiv](https://arxiv.org/abs/2405.15269) · 📝 [OpenReview](https://openreview.net/forum?id=1jd25AlvHS)　📅 2024-05　🏷 ICML 2025

**关键词**：`detection`、`BDetCLIP`、`black-box`、`contrastive prompting`

👤 **作者**：Yuwei Niu、Shuo He、Qi Wei、Zongyu Wu、Feng Liu、Lei Feng

- 🎯 **研究动机**：CLIP 后门防御集中于预训练/微调阶段，参数更新开销大且不适用黑盒场景
- 🔬 **研究方法**：发现后门图像的视觉表示对良性与恶性类描述文本变化不敏感；BDetCLIP 用 GPT-4 生成两类文本，以余弦相似度分布差异作判据
- 📌 **结论**：推理期即可完成检测，效果与效率均优于 SOTA 后门检测方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal contrastive learning methods (e.g., CLIP) can achieve impressive zero-shot classification performance, recent research has revealed that these methods are vulnerable to backdoor attacks. To defend against backdoor attacks on CLIP, existing defense methods focus on either the pre-training stage or the fine-tuning stage, which would unfortunately cause high computational costs due to numerous parameter updates and are not applicable in black-box settings. In this paper, we provide the first attempt at a computationally efficient backdoor detection method to defend against backdoored CLIP in the \emph{inference} stage. We empirically find that the visual representations of backdoored images are \emph{insensitive} to \emph{benign} and \emph{malignant} changes in class description texts. Motivated by this observation, we propose BDetCLIP, a novel test-time backdoor detection method based on contrastive prompting. Specifically, we first prompt a language model (e.g., GPT-4) to produce class-related description texts (benign) and class-perturbed random texts (malignant) by specially designed instructions. Then, the distribution difference in cosine similarity between images and the two types of class description texts can be used as the criterion to detect backdoor samples. Extensive experiments validate that our proposed BDetCLIP is superior to state-of-the-art backdoor detection methods, in terms of both effectiveness and efficiency. Our codes are publicly available at: https://github.com/Purshow/BDetCLIP.

</details>

### 44. MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2608.17722)　📅 2026-08

**关键词**：`detection`、`membership inference`、`VLM safety`、`data poisoning`、`audit tool`、`protective poisoning`

👤 **作者**：Xukun Luan、…、Di Wang

- 🎯 **研究动机**：VLM 训练数据持有者需检测数据是否被未授权使用，成员推理审计性能有待放大
- 🔬 **研究方法**：MemCatalyst 数据投毒工具（Poisoning Text/Image）：迫使 VLM 过学图像特征与文本语义的特定不一致以提高成员审计敏感性，投毒样本跨架构可迁移
- 📌 **结论**：五种 SOTA 审计、两个 VLM 上以极少投毒预算显著提升 MI AUC，对模型性能影响可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of data poisoning tools, aiming to amplify the data auditing performance on VLMs. MemCatalyst employs two strategies: Poisoning Text (PT) and Poisoning Image (PI). MemCatalyst forces VLMs to over-learn specific inconsistencies between image features and textual semantics during training, thereby increasing their susceptibility to membership information auditing. Crucially, the transferability of poisoned samples across different VLM architectures is demonstrated to be effective in the black-box setting. Extensive evaluations using five state-of-the-art data audits on two prominent VLMs demonstrate that MemCatalyst markedly enhances MI AUC scores with a minimal budget of poisoned samples, while maintaining a negligible impact on model performance.

</details>

### 45. DP²-VL: Private Photo Dataset Protection by Data Poisoning for Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23925)　📅 2026-03

**关键词**：`protection`、`privacy poisoning`、`private photos`、`identity affiliation`

👤 **作者**：Hongyi Miao、…、Guangtao Zhai

- 🎯 **研究动机**：identity-affiliation learning 新威胁：仅用少量私人照片微调 VLM 即可把身份与私有财产、社会关系绑定并经 API 暴露
- 🔬 **研究方法**：构建七场景身份归属数据集证实 LLaVA、Qwen-VL、MiniGPT-v2 均可被利用；DP2-VL 对私人照片优化不可感知扰动，把表示推向对立区域使微调过拟合
- 📌 **结论**：跨模型强泛化、抗多样后处理且在不同保护比例下一致有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in visual-language alignment have endowed vision-language models (VLMs) with fine-grained image understanding capabilities. However, this progress also introduces new privacy risks. This paper first proposes a novel privacy threat model named identity-affiliation learning: an attacker fine-tunes a VLM using only a few private photos of a target individual, thereby embedding associations between the target facial identity and their private property and social relationships into the model's internal representations. Once deployed via public APIs, this model enables unauthorized exposure of the target user's private information upon input of their photos. To benchmark VLMs' susceptibility to such identity-affiliation leakage, we introduce the first identity-affiliation dataset comprising seven typical scenarios appearing in private photos. Each scenario is instantiated with multiple identity-centered photo-description pairs. Experimental results demonstrate that mainstream VLMs like LLaVA, Qwen-VL, and MiniGPT-v2, can recognize facial identities and infer identity-affiliation relationships by fine-tuning on small-scale private photographic dataset, and even on synthetically generated datasets. To mitigate this privacy risk, we propose DP2-VL, the first Dataset Protection framework for private photos that leverages Data Poisoning. Though optimizing imperceptible perturbations by pushing the original representations toward an antithetical region, DP2-VL induces a dataset-level shift in the embedding space of VLMs'encoders. This shift separates protected images from clean inference images, causing fine-tuning on the protected set to overfit. Extensive experiments demonstrate that DP2-VL achieves strong generalization across models, robustness to diverse post-processing operations, and consistent effectiveness across varying protection ratios.

</details>

### 46. Defending Our Privacy With Backdoors

📄 [arXiv](https://arxiv.org/abs/2310.08320)　📅 2023-10

**关键词**：`protection`、`privacy removal`、`CLIP`、`dual-use backdoor`

👤 **作者**：Dominik Hintersdorf、Lukas Struppek、Daniel Neider、Kristian Kersting

- 🎯 **研究动机**：网络抓取数据训练的大模型内嵌姓名、人脸等隐私，既删信息又不损性能很难
- 🔬 **研究方法**：借后门为善：文本编码器将敏感短语嵌入对齐中性词，图像编码器将个体嵌入映射为统一匿名嵌入，几分钟微调即可
- 📌 **结论**：CLIP 上以专门隐私攻击评估，显著降低零样本分类器中的个人信息泄漏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of large AI models trained on uncurated, often sensitive web-scraped data has raised significant privacy concerns. One of the concerns is that adversaries can extract information about the training data using privacy attacks. Unfortunately, the task of removing specific information from the models without sacrificing performance is not straightforward and has proven to be challenging. We propose a rather easy yet effective defense based on backdoor attacks to remove private information, such as names and faces of individuals, from vision-language models by fine-tuning them for only a few minutes instead of re-training them from scratch. Specifically, by strategically inserting backdoors into text encoders, we align the embeddings of sensitive phrases with those of neutral terms-"a person" instead of the person's actual name. For image encoders, we map individuals' embeddings to be removed from the model to a universal, anonymous embedding. The results of our extensive experimental evaluation demonstrate the effectiveness of our backdoor-based defense on CLIP by assessing its performance using a specialized privacy attack for zero-shot classifiers. Our approach provides a new "dual-use" perspective on backdoor attacks and presents a promising avenue to enhance the privacy of individuals within models trained on uncurated web-scraped data.

</details>

## 综评与基准

### 47. Poisoning Web-Scale Training Datasets is Practical

📄 [arXiv](https://arxiv.org/abs/2302.10149) · 🌐 [Project](https://doi.org/10.1109/SP54263.2024.00179)　📅 2023-02　🏷 IEEE S&P 2024

**关键词**：`analysis`、`web-scale corpus`、`low-cost poisoning`、`data supply chain`、`attack analysis`、`web-scale dataset`

👤 **作者**：Nicholas Carlini、…、Florian Tramèr

- 🎯 **研究动机**：网络级数据集被认为规模过大、难以被单点投毒，该假设未经检验
- 🔬 **研究方法**：split-view poisoning 利用网络内容可变性使标注视图与下载视图不一致；frontrunning poisoning 在快照窗口前抢先注入
- 📌 **结论**：60 美元即可投毒 LAION-400M/COYO-700M 的 0.01%，今天就可行于 10 个流行数据集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning models are often trained on distributed, web-scale datasets crawled from the internet. In this paper, we introduce two new dataset poisoning attacks that intentionally introduce malicious examples to a model's performance. Our attacks are immediately practical and could, today, poison 10 popular datasets. Our first attack, split-view poisoning, exploits the mutable nature of internet content to ensure a dataset annotator's initial view of the dataset differs from the view downloaded by subsequent clients. By exploiting specific invalid trust assumptions, we show how we could have poisoned 0.01% of the LAION-400M or COYO-700M datasets for just $60 USD. Our second attack, frontrunning poisoning, targets web-scale datasets that periodically snapshot crowd-sourced content -- such as Wikipedia -- where an attacker only needs a time-limited window to inject malicious examples. In light of both attacks, we notify the maintainers of each affected dataset and recommended several low-overhead defenses.

</details>

### 48. BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents

📄 [arXiv](https://arxiv.org/abs/2601.04566) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.791/)　📅 2026-07　🏷 ACL 2026

**关键词**：`benchmark`、`stage-aware backdoor`、`memory stage`、`trigger propagation`、`attack framework`、`planning／memory／tool`

👤 **作者**：Yunhao Feng、…、Yu-Gang Jiang

- 🎯 **研究动机**：后门研究碎片化、孤立分析单个攻击向量，agent 工作流内跨阶段的触发交互与传播缺乏统一视角
- 🔬 **研究方法**：BackdoorAgent 把攻击面结构化为 planning、memory、tool-use 三个功能阶段并插桩 agent 执行，构建覆盖 Agent QA、Code、Web、Drive 四类应用的标准化基准
- 📌 **结论**：单阶段植入的触发器可跨多步持久传播：GPT 骨干上 planning 攻击持久率 43.58%、memory 77.97%、tool 阶段 60.28%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents execute tasks through multi-step workflows that combine planning, memory, and tool use. While this design enables autonomy, it also expands the attack surface for backdoor threats. Backdoor triggers injected into specific stages of an agent workflow can persist through multiple intermediate states and adversely influence downstream outputs. However, existing studies remain fragmented and typically analyze individual attack vectors in isolation, leaving the cross-stage interaction and propagation of backdoor triggers poorly understood from an agent-centric perspective. To fill this gap, we propose \textbf{BackdoorAgent}, a modular and stage-aware framework that provides a unified, agent-centric view of backdoor threats in LLM agents. BackdoorAgent structures the attack surface into three functional stages of agentic workflows, including \textbf{planning attacks}, \textbf{memory attacks}, and \textbf{tool-use attacks}, and instruments agent execution to enable systematic analysis of trigger activation and propagation across different stages. Building on this framework, we construct a standardized benchmark spanning four representative agent applications: \textbf{Agent QA}, \textbf{Agent Code}, \textbf{Agent Web}, and \textbf{Agent Drive}, covering both language-only and multimodal settings. Our empirical analysis shows that \textit{triggers implanted at a single stage can persist across multiple steps and propagate through intermediate states.} For instance, when using a GPT-based backbone, we observe trigger persistence in 43.58\% of planning attacks, 77.97\% of memory attacks, and 60.28\% of tool-stage attacks, highlighting the vulnerabilities of the agentic workflow itself to backdoor threats. To facilitate reproducibility and future research, our code and benchmark are publicly available at GitHub.

</details>

### 49. Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2606.12586)　📅 2026-06

**关键词**：`analysis`、`VLAS 系统级评测`、`含 embodied-manipulation workflow`、`trigger leakage`、`neighbor leakage rate`、`agentic VLM`

👤 **作者**：Jiamin Chang、Salil Kanhere、Piotr Koniusz、Jason、Xue、Hammond Pearce

- 🎯 **研究动机**：VLAS 中视觉后门是系统级威胁，现有 ASR 与干净精度指标不衡量攻击是否精确（是否只在预期时触发）
- 🔬 **研究方法**：形式化 trigger leakage 并提出 Neighbor Leakage Rate（NLR）；以文本触发为探针分析微调学到的宽激活区域，并加编辑距离一硬负样本训练
- 📌 **结论**：3% 投毒率下邻近变体大量泄漏（NLR 达 0.996/0.944）；加入编辑距离一硬负样本显著收窄激活区域，在图像编辑与具身操作工作流中同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Agentic Systems (VLAS) connect visual perception to planning, tool use, and physical actions. This means backdoor-type triggers can propagate through both decision pipelines and their connected interfaces, thus making visual backdoors a system-level threat. Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior. To quantify this leakage, we introduce Neighbor Leakage Rate (NLR). Our experiments show that at a 3% poisoning ratio, icon and text triggers remain robust to common visual transformations, but their neighboring variants leak heavily, with NLR reaching 0.996 (icon) and 0.944 (text). Using textual triggers as a controlled probe, we show that standard fine-tuning learns a broad activation region rather than an exact trigger condition, causing neighboring strings to invoke the malicious behavior even when the exact trigger is absent. Adding edit-distance-one hard-negative samples during training substantially narrows this activation region and reduces leakage, including in image-editing and embodied-manipulation workflows, where leaked triggers can propagate into executable programs and action sequences.

</details>

### 50. ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety

📄 [arXiv](https://arxiv.org/abs/2604.19083) · 🌐 [Project](https://anonymous.4open.science/r/ProjLens-8FD7)　📅 2026-04

**关键词**：`analysis`、`projector`、`low-rank subspace`、`backdoor mechanism`

👤 **作者**：Kun Wang、…、Yang Wang

- 🎯 **研究动机**：MLLM 后门（含仅微调 projector 注入）的内在机制不透明，阻碍理解与缓解
- 🔬 **研究方法**：ProjLens 在四个后门变体上分析 projector 更新，定位低秩后门关键子空间并追踪嵌入漂移
- 📌 **结论**：后门关键参数集中于 projector 低秩子空间且无专属触发神经元；干净与毒化嵌入都向攻击目标方向移动，但幅度随输入范数线性缩放，形成毒样本上的独特激活

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have achieved remarkable success in cross-modal understanding and generation, yet their deployment is threatened by critical safety vulnerabilities. While prior works have demonstrated the feasibility of backdoors in MLLMs via fine-tuning data poisoning to manipulate inference, the underlying mechanisms of backdoor attacks remain opaque, complicating the understanding and mitigation. To bridge this gap, we propose ProjLens, an interpretability framework designed to demystify MLLMs backdoors. We first establish that normal downstream task alignment--even when restricted to projector fine--tuning--introduces vulnerability to backdoor injection, whose activation mechanism is different from that observed in text-only LLMs. Through extensive experiments across four backdoor variants, we uncover:(1) Low-Rank Structure: Backdoor injection updates appear overall full-rank and lack dedicated ``trigger neurons'', but the backdoor-critical parameters are encoded within a low-rank subspace of the projector;(2) Activation Mechanism: Both clean and poisoned embedding undergoes a semantic shift toward a shared direction aligned with the backdoor target, but the shifting magnitude scales linearly with the input norm, resulting in the distinct backdoor activation on poisoned samples. Our code is available at: https://anonymous.4open.science/r/ProjLens-8FD7

</details>

### 51. MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG

📄 [arXiv](https://arxiv.org/abs/2606.26793)　📅 2026-06

**关键词**：`benchmark`、`agentic RAG red-teaming`、`cross-surface attack`、`novelty constraint`、`red teaming`、`multimodal agentic RAG`

👤 **作者**：Inderjeet Singh、Andrés Murillo、Motoyoshi Sekiya、Yuki Unno、Junichi Suga

- 🎯 **研究动机**：多模态 agentic RAG 攻击面扩展到文本投毒、图像注入、直接查询与编排器操纵，现有红队方法面特定且复用模板（73-84% 重复）
- 🔬 **研究方法**：提出 MIRROR：记忆引导 MCTS 在检索上下文条件下生成候选，确定性 Novelty Gate 拒绝与检索集重复的候选，兼顾先验与新颖性；发布 ART-SafeBench（41,815+ 内置记录）
- 📌 **结论**：图像投毒 ASR 76%（基线 52%）、编排器攻击 97% 且查询成本减半、跨面方差最低（CV 0.47）；专用基线跨面崩溃（后缀优化文本面 79% 但直接查询仅 1%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. Existing red-teaming approaches are typically surface-specific and often recycle known attack templates; on text-poisoning benchmarks we measure 73-84% exact duplication. We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. A deterministic Novelty Gate rejects any candidate matching the retrieval set under normalized comparison, allowing retrieval to inform search priors without enabling prompt copying. Across four attack surfaces on a multimodal agentic RAG target, MIRROR attains 76% ASR on image poisoning compared with 52% for baselines, 97% ASR on orchestrator attacks at half the query cost, and the lowest cross-surface variance (coefficient of variation 0.47). In contrast, specialized baselines collapse across surfaces: suffix optimization reaches 79% ASR on text poisoning but 1% on direct queries. We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces.

</details>

### 52. BackdoorVLM: A Benchmark for Backdoor Attacks on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2511.18921)　📅 2025-11

**关键词**：`benchmark`、`12 attacks`、`image／text／bimodal trigger`、`VLM`

👤 **作者**：Juncheng Li、…、Yu-Gang Jiang

- 🎯 **研究动机**：后门威胁在 VLM 等多模态基础模型上缺乏系统评测
- 🔬 **研究方法**：BackdoorVLM 把多模态后门分为定向拒绝、恶意注入、越狱、概念替换与感知劫持五类，用 12 种文本/图像/双模态触发攻击在 2 个开源 VLM 与 3 个数据集上评测
- 📌 **结论**：VLM 对文本指令高度敏感，双模态后门中文本触发器压倒图像触发器；1% 投毒率即在多数任务取得超 90% 成功率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks undermine the reliability and trustworthiness of machine learning systems by injecting hidden behaviors that can be maliciously activated at inference time. While such threats have been extensively studied in unimodal settings, their impact on multimodal foundation models, particularly vision-language models (VLMs), remains largely underexplored. In this work, we introduce \textbf{BackdoorVLM}, the first comprehensive benchmark for systematically evaluating backdoor attacks on VLMs across a broad range of settings. It adopts a unified perspective that injects and analyzes backdoors across core vision-language tasks, including image captioning and visual question answering. BackdoorVLM organizes multimodal backdoor threats into 5 representative categories: targeted refusal, malicious injection, jailbreak, concept substitution, and perceptual hijack. Each category captures a distinct pathway through which an adversary can manipulate a model's behavior. We evaluate these threats using 12 representative attack methods spanning text, image, and bimodal triggers, tested on 2 open-source VLMs and 3 multimodal datasets. Our analysis reveals that VLMs exhibit strong sensitivity to textual instructions, and in bimodal backdoors the text trigger typically overwhelms the image trigger when forming the backdoor mapping. Notably, backdoors involving the textual modality remain highly potent, with poisoning rates as low as 1\% yielding over 90\% success across most tasks. These findings highlight significant, previously underexplored vulnerabilities in current VLMs. We hope that BackdoorVLM can serve as a useful benchmark for analyzing and mitigating multimodal backdoor threats. Code is available at: https://github.com/bin015/BackdoorVLM .

</details>

### 53. Benchmarking Poisoning Attacks against Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2505.18543)　📅 2025-05

**关键词**：`benchmark`、`attack-defense matrix`、`expanded QA`、`architecture coverage`、`13 attacks／7 defenses`、`multimodal RAG`

👤 **作者**：Baolei Zhang、…、Zheli Liu

- 🎯 **研究动机**：RAG 投毒攻击虽多，但缺乏对其真实威胁的系统性评估
- 🔬 **研究方法**：构建首个 RAG 投毒基准：5 个标准 QA 数据集与 10 个扩展变体、13 种攻击与 7 种防御的全谱评测
- 📌 **结论**：攻击在标准 QA 有效但在扩展版本显著下降；多轮、多模态与 Agent RAG 等高级架构均可被攻破，现有防御无法稳健防护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has proven effective in mitigating hallucinations in large language models by incorporating external knowledge during inference. However, this integration introduces new security vulnerabilities, particularly to poisoning attacks. Although prior work has explored various poisoning strategies, a thorough assessment of their practical threat to RAG systems remains missing. To address this gap, we propose the first comprehensive benchmark framework for evaluating poisoning attacks on RAG. Our benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques. Using this benchmark, we conduct a comprehensive evaluation of all included attacks and defenses across the full dataset spectrum. Our findings show that while existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Moreover, our results demonstrate that various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks. Notably, current defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies.

</details>

### 54. BackdoorMBTI: A Backdoor Learning Multimodal Benchmark Tool Kit for Backdoor Defense Evaluation

📄 [arXiv](https://arxiv.org/abs/2411.11006) · 🌐 [Project](https://doi.org/10.1145/3690624.3709385)　📅 2024-11　🏷 KDD 2025

**关键词**：`benchmark`、`multimodal toolkit`、`attack-defense matrix`、`extensible framework`

👤 **作者**：Haiyang Yu、Tian Xie、Jiaping Gui、Pengyang Wang、Ping Yi、Yue Wu

- 🎯 **研究动机**：后门防御方法多绑定单一模态，多模态后门缺乏统一评测基准
- 🔬 **研究方法**：BackdoorMBTI 覆盖三种模态、11 个常用数据集，提供数据处理、投毒、后门训练与评测的完整管线并标准化数据质量等实际因素
- 📌 **结论**：支撑多模态场景下后门防御的系统化评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Over the past few years, the emergence of backdoor attacks has presented significant challenges to deep learning systems, allowing attackers to insert backdoors into neural networks. When data with a trigger is processed by a backdoor model, it can lead to mispredictions targeted by attackers, whereas normal data yields regular results. The scope of backdoor attacks is expanding beyond computer vision and encroaching into areas such as natural language processing and speech recognition. Nevertheless, existing backdoor defense methods are typically tailored to specific data modalities, restricting their application in multimodal contexts. While multimodal learning proves highly applicable in facial recognition, sentiment analysis, action recognition, visual question answering, the security of these models remains a crucial concern. Specifically, there are no existing backdoor benchmarks targeting multimodal applications or related tasks. In order to facilitate the research in multimodal backdoor, we introduce BackdoorMBTI, the first backdoor learning toolkit and benchmark designed for multimodal evaluation across three representative modalities from eleven commonly used datasets. BackdoorMBTI provides a systematic backdoor learning pipeline, encompassing data processing, data poisoning, backdoor training, and evaluation. The generated poison datasets and backdoor models enable detailed evaluation of backdoor defenses. Given the diversity of modalities, BackdoorMBTI facilitates systematic evaluation across different data types. Furthermore, BackdoorMBTI offers a standardized approach to handling practical factors in backdoor learning, such as issues related to data quality and erroneous labels. We anticipate that BackdoorMBTI will expedite future research in backdoor defense methods within a multimodal context. Code is available at https://github.com/SJTUHaiyangYu/BackdoorMBTI.

</details>

### 55. Backdoor Learning in Language Models and Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.18095)　📅 2026-08

**关键词**：`survey`、`dissertation`、`LM／VLM`、`attack／detection`、`VLM security`、`TrojAI`

👤 **作者**：Weimin Lyu

- 🎯 **研究动机**：NLP 与 VLM 的后门攻击构成严重安全威胁，需系统分析、检测与设计
- 🔬 **研究方法**：博士论文系统分析、检测与设计 LM/VLM 后门攻击（含 TrojAI 场景），并研究面向临床与医学影像的高效多模态表征
- 📌 **结论**：整合后门安全研究与医学多模态效率两条主线的工作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). However, these advancements come with increased vulnerabilities, notably through backdoor attacks that pose severe security threats. This thesis addresses two critical dimensions of Trustworthy AI and Efficient Multimodal Representation Learning: (1) security through analyzing, detecting, and designing backdoor attacks in NLP and VLMs, and (2) efficiency through advanced multimodal representation methods tailored for clinical and medical imaging applications.

</details>

### 56. Backdoor Attacks on Multi-modal Contrastive Learning

📄 [arXiv](https://arxiv.org/abs/2601.11006)　📅 2026-01

**关键词**：`review`、`multimodal contrastive learning`、`attack taxonomy`、`defense taxonomy`

👤 **作者**：Simi D Kuniyilh、Rita Machacy

- 🎯 **研究动机**：对比学习易受后门与数据投毒攻击，相关研究分散且缺乏系统比较
- 🔬 **研究方法**：对多模态对比学习的后门攻击做综述，从威胁模型、攻击方法、目标领域与可用防御四方面系统梳理
- 📌 **结论**：总结对比学习的固有脆弱性与防御进展，指出工业与分布式环境安全部署的挑战与未来方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contrastive learning has become a leading self- supervised approach to representation learning across domains, including vision, multimodal settings, graphs, and federated learning. However, recent studies have shown that contrastive learning is susceptible to backdoor and data poisoning attacks. In these attacks, adversaries can manipulate pretraining data or model updates to insert hidden malicious behavior. This paper offers a thorough and comparative review of backdoor attacks in contrastive learning. It analyzes threat models, attack methods, target domains, and available defenses. We summarize recent advancements in this area, underline the specific vulnerabilities inherent to contrastive learning, and discuss the challenges and future research directions. Our findings have significant implications for the secure deployment of systems in industrial and distributed environments.

</details>

### 57. Backdoor Attacks and Defenses on Large Multimodal Models: A Survey

🌐 [Project](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176618816.64264497/v3)　📅 2026

**关键词**：`survey`、`LMM backdoor`、`VLP／LVLM`、`attack-defense taxonomy`

- 🎯 **研究动机**：LMM后门攻防研究分散，缺统一分类框架
- 🔬 **研究方法**：综述覆盖VLP、LVLM、多模态扩散与具身系统的攻防taxonomy
- 📌 **结论**：梳理方法谱系与开放问题并维护持续更新索引
