# Deepfake 与 Media Forensics

[返回上级目录](README.md)

## 研究方向

研究人脸、语音、音视频和局部媒体伪造的检测、定位、归因与主动防护，覆盖跨数据集泛化、open-set generator、持续学习、可解释 forensic evidence 和真实传播链。

## 研究脉络

- **伪造痕迹：** 早期方法利用空间、频谱、声学和时序不一致检测单类 deepfake。
- **泛化与开放世界：** Real-centric、one-class、continual 和 multimodal 方法减少对已知伪造器的依赖。
- **可解释取证：** Localization、evidence graph 与 tool-using forensic agent 开始给出可核验的伪造区域和证据链。
- **主动防护：** Identity protection、forensic tracing 与 proactive benchmark 将防线前移到媒体生成或发布阶段。

## Audio 与 Voice Deepfake

### 1. The Last Mile of Deepfake Speech Detection: An Industry-Academia Experience Report

📄 [arXiv](https://arxiv.org/abs/2608.17585)　📅 2026-08

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`

👤 **作者**：Anton Firc、Kamil Malinka、Vojtěch Staněk、Miroslav Hlaváček、Marek Bartoň

- 🎯 **研究动机**：语音 deepfake 检测基准报告亚 1% 错误率但真实部署下退化，产学落地落差未被系统记录
- 🔬 **研究方法**：基于与 Phonexia 三年合作构建并部署检测器的经验，梳理数据许可、真实输入形态与校准分数解释三大障碍并连接到研究建议
- 📌 **结论**：提出商用可用数据集共享标准、真实部署基准与非专家可行动分数等协调提案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Synthetic speech detection benchmarks now report sub-1% error rates on some in-domain evaluations, yet performance degrades under unseen attacks, channel mismatch, and distribution shift. Based on a three-year effort with Phonexia, a commercial speaker-recognition vendor, we report barriers encountered while building and deploying a detector. Many public benchmarks are not licensed for commercial model development. Real inputs are not four-second clean clips but long, codec-degraded, sometimes partially synthetic recordings. And when a calibrated system returns a log-likelihood ratio of 2.5, no one can tell the customer what it means for their decision. Rather than proposing a new model, we connect these barriers to concrete research and coordination proposals: shared standards for commercially usable datasets, realistic deployment benchmarks, and scores that non-experts can act on. These observations come from one project and should be tested in other settings.

</details>

### 2. Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2608.13817)　📅 2026-08

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`

👤 **作者**：Tomás Andrade Weber

- 🎯 **研究动机**：人类语音生理约束是否在 SSL 潜空间表现为结构化轨迹动力学、合成语音是否可检测地违反未知
- 🔬 **研究方法**：在 Wav2Vec2-Large-AntiDeepfake 上训练因果 LSTM 下一帧预测器（仅 bonafide 训练），与静态池化基线同特征对比以隔离时间建模贡献
- 📌 **结论**：六基准达 SOTA，ASVspoof 2021 最佳 EER 0.75%；仅 bonafide 训练的 Stage 1 在 DE2024 超同骨干监督基线（30.35%），跨语料多合成器设定下时序增益显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human speech production is constrained by physiology, giving rise to characteristic temporal structure on acoustic signals. We hypothesise that these constraints manifest as structured trajectory dynamics in the latent space of Self-Supervised Learning (SSL) models, and that synthetic speech violates them detectably. To test this hypothesis, we train a causal Long Short-Term Memory (LSTM) next-frame predictor on bonafide speech only (Stage 1), using the deepfake-specialised SSL backbone Wav2Vec2-Large-AntiDeepfake, and compare against a static global-average-pooling baseline using identical features, thus isolating the contribution of temporal modelling. A supervised Stage 2, which trains a Multi-Layer Perceptron on the frozen LSTM internal states using labelled data, is included to characterise the role of spoof supervision. Our system achieves competitive or state-of-the-art performance across six benchmarks: ASVspoof 2019/2021, Codecfake, In-the-Wild, MLAAD-EN, and Deepfake-Eval-2024, including best published EER on ASVspoof 2021 (0.75\%) and, notably, Stage 1 trained on bonafide speech only surpasses the published supervised baseline from the same backbone on DE2024 (30.35\%). On near-domain benchmarks, static and dynamic approaches perform comparably. On harder cross-corpus benchmarks with diverse synthesis methods, trajectory dynamics provide substantial gains, confirming that temporal physiological constraints carry detection signal beyond utterance-level statistics.

</details>

### 3. SONAR: Spectral‑Contrastive Audio Residuals for Generalizable Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2511.21325) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64783)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`contrastive learning`、`cross-generator generalization`

👤 **作者**：Ido Nitzan Hidekel、Gal lifshitz、Khen Cohen、Dan Raviv

- 🎯 **研究动机**：音频深伪检测因谱偏差优先低频结构、欠用生成模型遗留的高频伪迹，难以泛化到未见攻击；现有频率感知方法只把高频线索当辅助特征
- 🔬 **研究方法**：提出 SONAR：XLSR 编码器捕获低频内容，可学习 1D SRM 高通滤波分支蒸馏高频残差，经频率交叉注意力融合并用 Jensen-Shannon 对齐损失约束真音频 LF-HF 一致、放大深伪不一致
- 📌 **结论**：在 ASVspoof 2021 与 in-the-wild 基准上单次运行即达 SOTA，收敛快于强基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake audio detectors often fail to generalize to unseen attacks, in part due to \emph{spectral bias}: neural networks prioritize low-frequency structure while under-exploiting subtle high-frequency (HF) artifacts left by generative models. We introduce \textbf{SONAR} (Spectral-cONtrastive Audio Residuals), a frequency-guided framework that \emph{explicitly enforces representation-level consistency} between semantic content and HF residuals. Unlike prior frequency-aware or dual-stream detectors that treat HF cues as auxiliary features, SONAR encourages structured interaction between content and noise representations in latent space. The model employs a dual-path architecture in which an XLSR encoder captures low-frequency content, while a parallel branch with learnable, value-constrained 1D SRM (Spatial Rich Model) high-pass filters distills HF residuals. The two representations are fused via frequency cross-attention and trained with a \emph{Jensen--Shannon alignment loss} that promotes LF–HF consistency for genuine audio and amplifies inconsistency for deepfakes. Evaluated on ASVspoof~2021 and in-the-wild benchmarks, SONAR achieves state-of-the-art performance in a \textbf{single run} setting and converges faster than strong baselines. By mitigating the effects of spectral bias through frequency-guided alignment, SONAR provides a fully data-driven and architecture-agnostic approach to generalizable audio deepfake detection.

</details>

### 4. Scaling Behavior in Model Fine-tuning for Audio DeepFake Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/60632)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Xiang Li、Pin-Yu Chen、Wenqi Wei

- 🎯 **研究动机**：语音基础模型与合成数据日益增大带来高性能，但检测能力随模型容量与数据规模的扩展规律在真实部署条件下不明
- 🔬 **研究方法**：系统研究微调（而非大规模预训练）下音频深伪检测的 scaling law：用共享架构与预训练的受控模型族，分析检测性能、鲁棒性与泛化随规模的变化
- 📌 **结论**：发现性能扩展与鲁棒性扩展的根本不对称，单靠增大模型容量不足以获得可靠的真实世界泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in audio deepfake detection have been driven by increasingly large speech foundation models and growing amounts of synthetic data. Despite strong benchmark performance, it remains unclear how detection capability scales with model capacity and training data under realistic deployment conditions involving distribution shift, signal corruption, and unseen synthesis pipelines. In this work, we present the first systematic study of scaling laws in post-training audio deepfake detection, focusing on fine-tuning regimes rather than large-scale pretraining. Using a controlled family of speech foundation models with shared architecture and pretraining, we analyze how detection performance, robustness, and generalization evolve as a function of model size and training data scale. Our results reveal a fundamental asymmetry between performance scaling and robustness scaling in audio deepfake detection, suggesting increasing model capacity alone is insufficient for achieving reliable real-world generalization.

</details>

### 5. Learning Tight Rejection Boundaries without Negatives for Strict One-Class Audio Deepfake Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/63118)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Yuze Zhao、Kuiyuan Zhang、Zhongyun Hua、Yushu Zhang、Qing Liao、Wei Jiang

- 🎯 **研究动机**：严格单类检测无欺骗样本难建紧致决策边界，引入负样本的松弛方法偏向已见伪影损泛化
- 🔬 **研究方法**：CA-SOADD 构造 off-manifold 边界探针，质心锚定三目标同时强制质心紧致与相对探针间隔，域条件质心扩展异质设定
- 📌 **结论**：ASVSpoof 与 MLAAD 上严格只用真实数据的方法在未见攻击与域移位下持续超强基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of audio deepfakes requires robust detection capable of generalizing to unseen attacks. One-class learning offers inherent robustness for this task by characterizing real speech distributions to detect anomalies. However, establishing a compact decision boundary without spoof supervision remains a fundamental challenge. Existing relaxed approaches often compromise this strictness by introducing auxiliary negative samples, which biases the boundary toward seen artifacts and degrades generalization to unseen attacks. To address this, we propose CA-SOADD, a framework that refines the acceptance region by constructing off-manifold boundary probes. Our proposed centroid-anchored tri-objective learning paradigm simultaneously enforces centroid compactness and a centroid-referenced margin against these probes, thereby explicitly tightening the acceptance region without treating them as an explicit negative class. We further extend the framework to heterogeneous settings through domain-conditioned centroids. Experiments on ASVSpoof and MLAAD benchmarks demonstrate that our strict real-only method consistently outperforms strong baselines under unseen attack types and domain shifts, with its effectiveness further validated through extensive ablation studies.

</details>

### 6. HyperPotter: Spell the Charm of High-Order Interactions in Audio Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2602.05670) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60926)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Qing Wen、…、Kui Ren

- 🎯 **研究动机**：音频深伪检测多依赖局部时频特征或成对关系，忽略多分量协同的高阶交互
- 🔬 **研究方法**：HyperPotter 超图框架用类感知原型初始化的聚类超边捕获协同模式
- 📌 **结论**：13 个测试集上 11 个超基线，平均相对 EER 降 12.68%（改进集上 22.15%）；严重编解码或信道失真下鲁棒性仍有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in AIGC technologies have enabled the synthesis of highly realistic audio deepfakes capable of deceiving human auditory perception. Although numerous audio deepfake detection (ADD) methods have been developed, most rely on local temporal/spectral features or pairwise relations, overlooking high-order interactions (HOIs). HOIs capture discriminative patterns that emerge from multiple feature components beyond their individual contributions. We propose HyperPotter, a hypergraph-based framework designed to capture high-order relations associated with synergistic patterns through clustering-based hyperedges with class-aware prototype initialization. Extensive experiments on 13 test sets show that HyperPotter improves over the baseline on 11 sets, yielding an average relative EER reduction of 12.68\% across all test sets and 22.15\% on the improved sets. These results demonstrate strong cross-scenario generalization, while also revealing robustness limits under severe codec or channel distortion.

</details>

### 7. From Talking to Singing: A New Challenge for Audio-Visual Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2605.27944) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62663)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Ke Liu、…、Yang Yang

- 🎯 **研究动机**：唱歌场景中节奏性发声削弱音视频跨模态耦合，引入非平凡域偏移使现有深伪检测性能大降
- 🔬 **研究方法**：用节奏感知生成模型构建 Singing Head DeepFake 数据集；T-AVFD 框架：面部真实性模式学习器对齐多粒度文本描述，多模态差分权重学习保持音视频一致性并自适应融合
- 📌 **结论**：多个说话人深伪数据集与 SHDF 上一致超越基线并抗多样扰动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With rapid advances in audio-visual generative models, reliable forgery detection becomes increasingly critical. Existing methods for audio-visual deepfake detection typically rely on cross-modal inconsistencies. In singing, rhythmic vocalization weakens this coupling and introduces a nontrivial domain shift, substantially degrading detection performance. We construct the Singing Head DeepFake (SHDF) dataset using rhythm-aware generative models to fill the gap in singing benchmarks. To cope with cross-scenario domain shifts, we propose a Text-guided Audio-Visual Forgery Detection (T-AVFD) framework that generalizes across both talking and singing scenarios. T-AVFD comprises a facial authenticity pattern learner and a multi-modal differential weight learning module. The pattern learner aligns facial features with multi-granularity textual descriptions to learn generalizable authenticity patterns. The weight learning module preserves intrinsic audio-visual consistency and adaptively integrates it with authenticity patterns via differential weighting. Extensive experiments on multiple talking head deepfake datasets and SHDF show consistent improvements over existing baselines and strong robustness under diverse perturbations.

</details>

### 8. FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors

📄 [arXiv](https://arxiv.org/abs/2606.05101) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64852)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`、`prompt injection`、`empirical evaluation`

👤 **作者**：Sepehr Dehdashtian、Jacob H Seidman、Vishnu N Boddeti、Gaurav Bharaj

- 🎯 **研究动机**：音频深伪检测评测数据靠人工收集且盲点发现低效
- 🔬 **研究方法**：FoeGlass 首个 ADD 黑盒自动红队：用 LLM 的 in-context learning 探索 TTS 输入空间生成骗过目标检测器的音频，基于多样性度量的上下文设计避免模式坍塌
- 📌 **结论**：假阴性率比无监督采样与最新欺骗数据集改善最高 94%，攻击可跨检测器迁移；用生成数据微调使检测器鲁棒性提升至 41%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio deepfake detection (ADD) models are critical for countering the malicious use of text-to-speech (TTS) models. Evaluating and strengthening ADD models requires developing datasets that span the space of generated audio and highlight high-error regions. Existing dataset development strategies face two challenges: (i) manual collection, and (ii) inefficient discovery of blind spots in the ADD models. To address these challenges, we propose FoeGlass, the first black-box automated red-teaming method for ADDs, which effectively discovers ADD failure modes in the space of generated audio underexplored by state-of-the-art deepfake benchmarks. FoeGlass uses the in-context learning capabilities of an LLM to explore the input space of a TTS model, generating audio samples that fool the target ADD using only black-box access to all components. By using a carefully designed context based on diversity measurements, FoeGlass mitigates the common problem of mode collapse in automated red-teaming systems. Empirical evaluations on several open-source ADD and TTS models demonstrate that data generated from FoeGlass substantially improves the false negative rates over unconditional sampling baselines and recent spoofing datasets by up to 94%, while requiring no manual supervision. Furthermore, we show that the attacks generated by FoeGlass are transferable across different target ADDs, demonstrating its broad applicability and ease of use for the automated red teaming of ADD systems. Finally, fine-tuning ADD models on FoeGlass-generated samples notably enhances the robustness of the detectors (up 41%).

</details>

### 9. Alethia: a Foundational Encoder for Voice Deepfakes

📄 [arXiv](https://arxiv.org/abs/2605.00251) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61173)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Yi Zhu、Brahmi Dwivedi、Jayaram Raghuram、Surya Koppisetti

- 🎯 **研究动机**：语音深伪检测依赖语音基础模型表征，下游微调已收益递减
- 🔬 **研究方法**：提出结合瓶颈掩码嵌入预测与 flow matching 频谱重建的预训练配方，训练首个语音深伪基础编码器 Alethia
- 📌 **结论**：在 5 个任务 56 个基准数据集上显著超越 SOTA 语音基础模型，对真实扰动更鲁棒并零样本泛化到未见域（如 singing deepfake）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing voice deepfake detection and localization models rely heavily on representations extracted from speech foundation models (SFMs). However, downstream finetuning has now reached a state of diminishing returns. In this paper, we shift the focus to pretraining and propose a novel recipe that combines bottleneck masked embedding prediction with flow-matching based spectrogram reconstruction. The outcome, Alethia, is the first foundational audio encoder for various voice deepfake detection and localization tasks. We evaluate on 5 different tasks with 56 benchmark datasets, and note Alethia significantly outperforms state-of-the-art SFMs with superior robustness to real-world perturbations and zero-shot generalization to unseen domains (e.g., singing deepfakes). We also demonstrate the limitation of discrete targets in masked token prediction, and show the importance of continuous embedding prediction and generative pretraining for capturing deepfake artifacts.

</details>

### 10. A Data-Centric Approach to Generalizable Speech Deepfake Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.796/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`misinformation`、`fact-checking`

👤 **作者**：Wen Huang、Yuchen Mao、Yanmin Qian

- 🎯 **研究动机**：语音 deepfake 检测常无法识别未见伪造方法，模型中心方案进展受限，数据构成的影响被低估
- 🔬 **研究方法**：从单数据集与多数据集聚合两视角做数据中心研究：大规模实证刻画 SDD 数据 scaling law，并提出异构数据混合框架 DOSS（DOSS-Select 剪枝与 DOSS-Weight 重加权两种实现）
- 📌 **结论**：DOSS-Select 仅用 3% 数据即超朴素聚合；在 12k 小时精选池上用最优 DOSS-Weight 训练的模型在公开基准与商用 API 挑战集上达 SOTA，数据与模型效率更高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Achieving robust generalization in speech deepfake detection (SDD) remains a primary challenge, as models often fail to detect unseen forgery methods. While research has focused on model-centric and algorithm-centric solutions, the impact of data composition is often underexplored. This paper proposes a data-centric approach, analyzing the SDD data landscape from two practical perspectives: constructing a single dataset and aggregating multiple datasets. To address the first perspective, we conduct a large-scale empirical study to characterize the data scaling laws for SDD, quantifying the impact of source and generator diversity. To address the second, we propose the Diversity-Optimized Sampling Strategy (DOSS), a principled framework for mixing heterogeneous data with two implementations: DOSS-Select (pruning) and DOSS-Weight (re-weighting). Our experiments show that DOSS-Select outperforms the naive aggregation baseline while using only 3% of the total available data. Furthermore, our final model, trained on a 12k-hour curated data pool using the optimal DOSS-Weight strategy, achieves state-of-the-art performance, outperforming large-scale baselines with greater data and model efficiency on both public benchmarks and a new challenge set of various commercial APIs.

</details>

### 11. BEAT2AASIST: BEATs Feature Splitting with Dual-Branch AASIST for Environmental Sound Deepfake Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3453.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`audio deepfake`、`environmental sound`、`unknown generator`

- 🎯 **研究动机**：TTA 与 ATA 生成逼真环境声音带来恶意音频操纵风险，token 级音频表征会削弱结构化声学线索的显式保持
- 🔬 **研究方法**：BEAT2AASIST 双分支 AASIST 沿频率或通道维度拆分 BEATs 表征，多层融合（拼接、CNN-gated、SE-gated）聚合多层 transformer 信息，并用多神经 vocoder 数据增强
- 📌 **结论**：EnvSDD 数据集上两个赛道分获 ESDD 2026 Challenge 第 3 与第 4 名，集成组件比顶级系统更少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in text-to-audio (TTA) and audioto-audio (ATA) generation models have enabled the creation of highly realistic environmental sounds, raising growing concerns about malicious audio manipulation in real-world scenarios. To address this emerging threat, the ESDD 2026 Challenge was introduced as the first large-scale benchmark for Environmental Sound Deepfake Detection (ESDD), featuring two tracks that evaluate generalization to unseen generators and robustness under black-box, low-resource conditions. In this paper, we present BEAT2AASIST, an enhanced deepfake detection framework built upon the BEATsAASIST baseline. Motivated by the observation that token-based audio representations may weaken explicit preservation of structured acoustic cues, the proposed method introduces a dualbranch AASIST architecture that explicitly splits BEATs-derived representations along frequency or channel dimensions. This design enables specialized modeling of complementary spoofing artifacts that may be attenuated in unified representations. To further enrich acoustic features, we incorporate multi-layer fusion strategies that aggregate information from multiple transformer layers using concatenation, CNN-gated, and SE-gated mechanisms. In addition, vocoder-based data augmentation with multiple high-fidelity neural vocoders is employed to enhance robustness against unseen and black-box spoofing attacks. Experimental results on the EnvSDD dataset demonstrate that BEAT2AASIST achieves strong and consistent performance across both challenge tracks. In particular, the proposed approach attains 3rd place in Track 2 and 4th place in Track 1 in the ESDD 2026 Challenge, despite using fewer ensemble components than top-ranked systems. These results suggest that explicit model- ∗ Corresponding authors. ing of heterogeneous acoustic subspaces, combined with targeted representation fusion and data augmentation, provides an effective and efficient design strategy for real-world environmental sound deepfake detection. The code is available at https: //github.com/ikwak2/BEAT2AASIST.

</details>

### 12. Bridging the SEA Gap: An Initial Benchmark for Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages

📄 [arXiv](https://arxiv.org/abs/2606.15968) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4G93.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-social-good)　📅 2026

**关键词**：`benchmark`、`speech deepfake`、`neural audio codec`、`language generalization`

👤 **作者**：Orchid Chetia Phukan、Girish、Mohd Mujtaba Akhtar、Arun Balaji Buduru

- 🎯 **研究动机**：codecfake 检测基准基本限于英语（少量中文），东南亚语言未探索，且 vocoder 数据训练的检测器泛化差
- 🔬 **研究方法**：SEA-CF 首个多 SEA 语言大规模 CF 检测基准，覆盖多样说话人与多种 NAC 架构；并提出轻量小模型 GARUDA
- 📌 **结论**：英文中心数据训练的 SOTA 检测器因 SEA 语音结构差异无法泛化；微调 ALM 有效但规模过大，GARUDA 轻量且超越强基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Codecfakes (CFs) are a type of speech deepfakes generated through Audio Language Models (ALMs), with Neural Audio Codecs (NACs) forming the core mechanism for speech encoding and generation. CFs exhibit distributional characteristics that differ from vocoder-based deepfakes, causing detectors trained on vocoder data to generalize poorly to CFs detection. Although this has led to the development of CF detection benchmarks, existing resources are largely confined to English—and to a limited extent Chinese—leaving South-East Asian (SEA) languages unexplored. To bridge this gap, we introduce SEA-CF, the first large-scale benchmark for CF detection spanning multiple SEA languages, diverse speaker profiles, and a wide range of NAC architectures. SEA-CF is constructed by synthesizing publicly available real speech corpora. Our experiments show that state-of-the-art (SOTA) CF detectors trained on English-centric datasets fail to generalize to SEA speech due to language-specific phonetic structures, tonal variations, and rich prosodic diversity. We further conduct a comprehensive zero-shot and fine-tuned evaluation of recent SOTA ALMs on SEA-CF. Fine-tuning the ALMs improves performance, however, these are very large being impractical for real-world application due to their scale, particularly in low-resource and latency-constrained settings. To address this limitation, we propose a novel small-ALM, GARUDA tailored for CF detection, which delivers strong performance while remaining lightweight. Extensive evaluations demonstrate that the proposed Small-ALM outperforms strong end-to-end and ALM-based baselines, establishing a new, practical direction for robust CF detection in SEA languages and beyond.

</details>

### 13. Profiling the Voice: Speaker-Specific Phoneme Fingerprinting for Speech Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2605.17737) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4461.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`speech deepfake`、`speaker fingerprint`、`phoneme profile`

👤 **作者**：Jun Xue、…、Yanzhen Ren

- 🎯 **研究动机**：通用黑盒语音深伪检测器不捕说话人特有习惯特质且缺可解释性
- 🔬 **研究方法**：PVP 从宏语句转向微语音建模：仅用真实参考语音估计轻量 GMM 建模说话人特有音素实现，并发布首个大规模中文 POI 深伪数据集
- 📌 **结论**：POI 欺骗场景显著超 SOTA 通用检测器（EER 大幅降低）并提供音素级可解释性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative AI has made audio deepfakes increasingly indistinguishable from authentic human vocals, posing significant threats to persons-of-interest (POI) such as public figures. Current detection systems primarily rely on generic, black-box models that fail to capture speaker-specific idiosyncratic traits and lack interpretability. In this paper, we propose Phoneme-based Voice Profiling (PVP), a novel personalized defense framework. By shifting the detection paradigm from macro-utterance analysis to micro-phonetic modeling, PVP captures the unique acoustic distributions underlying a POI’s habitual articulatory patterns. Specifically, our framework models speaker-specific phonetic realizations using lightweight Gaussian Mixture Models (GMMs) estimated solely from bona fide reference speech. This design enables data-efficient profiling and robust generalization to previously unseen spoofing attacks without requiring heavy spoof-specific training. Furthermore, we introduce the first largescale Chinese POI deepfake dataset to benchmark speaker-specific detection. Experimental results demonstrate that PVP significantly outperforms state-of-the-art generic detectors in POI spoofing scenarios, achieving substantial EER reductions while providing fine-grained, phoneme-level interpretability for forensic analysis. Code and data are available at: https://github.com/JunXue-tech/PVP

</details>

### 14. AUDETER: A Large-scale Dataset for Deepfake Audio Detection in Open Worlds

📄 [arXiv](https://arxiv.org/abs/2509.04345) · 🌐 [Project](https://doi.org/10.1145/3770855.3817583)　📅 2025-09　🏷 KDD 2026

**关键词**：`benchmark`、`audio deepfake`、`open-world detection`、`cross-generator generalization`

👤 **作者**：Qizhou Wang、Hanxun Huang、Guansong Pang、Sarah Erfani、Christopher Leckie

- 🎯 **研究动机**：音频深伪数据集真实语音多样性不足、合成系统覆盖陈旧且来源混杂，阻碍开放世界评测
- 🔬 **研究方法**：构建 4500+ 小时、11 个 TTS 与 10 个 vocoder 共 300 万片段的 AUDETER，并提出课程学习缓解多源负迁移
- 📌 **结论**：现有检测器难泛化到新深伪；AUDETER 训练的 XLR 检测器跨域强，In-the-Wild 上 EER 1.87%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech synthesis systems can now produce highly realistic vocalisations that pose significant authenticity challenges. Despite substantial progress in deepfake detection models, their real-world effectiveness is often undermined by evolving distribution shifts between training and test data, driven by the complexity of human speech and the rapid evolution of synthesis systems. Existing datasets suffer from limited real speech diversity, insufficient coverage of recent synthesis systems, and heterogeneous mixtures of deepfake sources, which hinder systematic evaluation and open-world model training. To address these issues, we introduce AUDETER (AUdio DEepfake TEst Range), a large-scale and highly diverse deepfake audio dataset comprising over 4,500 hours of synthetic audio generated by 11 recent TTS models and 10 vocoders, totalling 3 million clips. We further observe that most existing detectors default to binary supervised training, which can induce negative transfer across synthesis sources when the training data contains highly diverse deepfake patterns, impacting overall generalisation. As a complementary contribution, we propose an effective curriculum-learning-based approach to mitigate this effect. Extensive experiments show that existing detection models struggle to generalise to novel deepfakes and human speech in AUDETER, whereas XLR-based detectors trained on AUDETER achieve strong cross-domain performance across multiple benchmarks, achieving an EER of 1.87% on In-the-Wild. AUDETER is available on GitHub.

</details>

### 15. Perturbed Public Voices (P^2V): A Dataset for Robust Audio Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2508.10949) · 🌐 [Project](https://doi.org/10.1145/3770855.3817542)　📅 2025-08　🏷 KDD 2026

**关键词**：`benchmark`、`audio deepfake`、`public figure`、`realistic perturbation`

👤 **作者**：Chongyang Gao、Marco Postiglione、Isabel Gortner、Sarit Kraus、V. S. Subrahmanian

- 🎯 **研究动机**：音频深伪检测器在受控基准外失效，缺乏含真实扰动的评估数据
- 🔬 **研究方法**：构建 IRB 批准的 P2V 数据集：LLM 生成身份一致转写、环境与对抗噪声、2020-2025 最新语音克隆技术
- 📌 **结论**：22 个检测器在 P2V 上平均掉 43% 性能，先进克隆使可检测性降 20-30%；P2V 训练的模型保持鲁棒并泛化到现有数据集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current audio deepfake detectors cannot be trusted. While they excel on controlled benchmarks, they fail when tested in the real world. We introduce Perturbed Public Voices (P$^{2}$V), an IRB-approved dataset capturing three critical aspects of malicious deepfakes: (1) identity-consistent transcripts via LLMs, (2) environmental and adversarial noise, and (3) state-of-the-art voice cloning (2020-2025). Experiments reveal alarming vulnerabilities of 22 recent audio deepfake detectors: models trained on current datasets lose 43% performance when tested on P$^{2}$V, with performance measured as the mean of F1 score on deepfake audio, AUC, and 1-EER. Simple adversarial perturbations induce up to 16% performance degradation, while advanced cloning techniques reduce detectability by 20-30%. In contrast, P$^{2}$V-trained models maintain robustness against these attacks while generalizing to existing datasets, establishing a new benchmark for robust audio deepfake detection. P$^{2}$V will be publicly released upon acceptance by a conference/journal.

</details>

### 16. Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination

📄 [arXiv](https://arxiv.org/abs/2608.14391)　📅 2026-08

**关键词**：`benchmark`、`AI-generated content`、`deepfake detection`、`media forensics`

👤 **作者**：Shuo Liang、…、Wangbo Zhao

- 🎯 **研究动机**：危机事件 AI 生成视频的检测器泛化、人类感知与社交传播下检测可靠性缺乏基准证据
- 🔬 **研究方法**：RA-Bench 以 1830 个真实视频为锚、10 类社会风险，含四个开源与五个闭源生成器共 17,886 条视频，从检测器泛化、生成属性、人类判断与传播三维度评测
- 📌 **结论**：传统、零样本多模态与微调 MLLM 三族检测器无一一致泛化；误导人类的视频同样难检，社交传播使检测更难

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent video generators can fabricate realistic depictions of wars, disasters, public emergencies, and other real-world crises, creating substantial risks of misinformation. Existing benchmarks, however, provide limited evidence on detector and generator behavior in such settings, including how detectability varies with generation conditions, how people perceive generated videos, and whether detectors remain reliable during social dissemination. To address this gap, we introduce RA-Bench, a benchmark for AI-generated video detection that uses Real videos as Anchors. RA-Bench contains 17,886 videos, comprising 1,830 real-video anchors across 10 social-risk categories and 16,056 generated clips from four open-source and five closed-source generators. Based on RA-Bench, we organize our evaluation along three dimensions. We first assess detector generalization across seven traditional detectors, ten zero-shot multimodal models under three review settings, and two MLLMs specifically fine-tuned on AI-generated video detection. Across these methods, none of the three detector families generalizes consistently across RA-Bench instances. We then examine how detectability varies with generation quality, conditioning information, and sampling seeds. These analyses show that generation properties affect detector families differently, while source-level detection patterns remain stable across seeds. Finally, we study human authenticity judgments and detector reliability during social dissemination. We find that videos that mislead people are also difficult for current detectors, and that social dissemination makes detection harder. Together, these findings show that current methods struggle to detect realistic AI-generated videos, highlighting the need for detectors robust to evolving video generators.

</details>

### 17. FakeI2V-Bench: Benchmarking the Applicability of Image-level Deepfake Detectors for Deepfake Video Detection

📄 [arXiv](https://arxiv.org/abs/2608.03096) · 🌐 [Project](https://doi.org/10.1145/3770855.3817509)　📅 2026-08　🏷 KDD 2026

**关键词**：`benchmark`、`deepfake video`、`image detector transfer`、`cross-modal forensics`

👤 **作者**：Pei Li、Sihan Chen、Delong Ran、Tianshuo Cong

- 🎯 **研究动机**：视频生成模型加剧 deepfake 威胁，但图像级检测器在视频域的适用性缺乏系统评估
- 🔬 **研究方法**：FakeI2V-Bench 含 97,548 条最新生成模型视频，系统评测 8 个视频级与 12 个图像级检测器；IV-Bridge 用随机森林聚合帧级预测扩展图像检测器
- 📌 **结论**：最强图像级检测器 AUC 80.16% 略超最强视频级 79.99%；IV-Bridge 使 11 个图像检测器超越视频级 SOTA，最佳达 93.80% AUC

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in video generation models have significantly intensified the deepfake threat, yet the current deepfake video detection benchmarks remain underdeveloped. In particular, the effectiveness of image-level detectors in the video domain has not been systematically assessed. To fill this gap, we present FakeI2V-Bench, a benchmark for evaluating state-of-the-art video-level deepfake detectors in challenging scenarios, with a particular focus on systematically assessing the performance of image-level deepfake detectors in the video domain. FakeI2V-Bench comprises 97,548 videos, containing content generated by the latest powerful generation models and covering a broader range of categories. Using this dataset, we conduct a systematic evaluation of eight video-level detectors and twelve representative image-level detectors. Experimental results show that the best-performing image-level detector achieves an 80.16% AUC, slightly outperforming the strongest video-level detector (i.e., 79.99% AUC). Going beyond benchmarking, we present IV-Bridge, a general framework that enhances the applicability of image-level deepfake detectors to videos. IV-Bridge employs a random forest model with statistical features to aggregate frame-level predictions, allowing eleven image-level detectors to surpass state-of-the-art video-level approaches, with the best-performing variant achieving a 93.80% AUC. Overall, FakeI2V-Bench establishes a rigorous benchmark for deepfake video detection and introduces a novel pathway for extending image-level detectors to the video domain, offering new insights and directions for future research. Code and data are available at https://github.com/CryptoAILab/FakeI2V-Bench.

</details>

### 18. Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2605.01638) · 🌐 [Project](https://tianxiao1201.github.io/omni-fake-project-page/) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Omni-Fake_Benchmarking_Unified_Multimodal_Social_Media_Deepfake_Detection_CVPR_2026_paper.html)　📅 2026-05　🏷 CVPR 2026

**关键词**：`benchmark`、`social media`、`multimodal deepfake`、`unified detection`

👤 **作者**：Tianxiao Li、…、Guangliang Cheng

- 🎯 **研究动机**：现有多模态 deepfake 基准受限于单模态、简化操纵或不真实分布，难以评估真实鲁棒性
- 🔬 **研究方法**：Omni-Fake 含 1M+ 样本数据集与 200k+ OOD 基准，覆盖图像、音频、视频与音视频 talking head 四模态，支持检测-定位-解释联合协议；附 RL 驱动检测器 Omni-Fake-R1
- 📌 **结论**：检测精度、跨模态泛化与可解释性均显著超过 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal deepfakes are proliferating on social media and threaten authenticity, information integrity, and digital forensics. Existing benchmarks are constrained by their single-modality scope, simplified manipulations, or unrealistic distributions, which limit their ability to assess real-world robustness. To address these limitations, we present Omni-Fake, a unified omni-dataset for comprehensive multimodal deepfake detection in social-media settings. It comprises Omni-Fake-Set, a large-scale, high-quality dataset with 1M+ samples, and Omni-Fake-OOD, an out-of-distribution benchmark with 200k+ samples intentionally excluded from training to evaluate generalization. Omni-Fake spans four modalities (image, audio, video, and audio-video talking head) and supports a joint detection-localization-explanation protocol. On top of Omni-Fake, we further propose Omni-Fake-R1, a reinforcement-learning-driven multimodal detector that adaptively integrates visual and auditory cues and outputs structured decisions, localization, and natural-language explanations. Extensive experiments show significant gains in detection accuracy, cross-modal generalization, and explainability over state-of-the-art baselines. Project page: https://tianxiao1201.github.io/omni-fake-project-page/

</details>

### 19. Proactive Defense Benchmark against Deepfake Generation

🌐 [Project](https://proactivedefensebenchmark.github.io/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62016)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Joonhyuk Baek、Wonjune Seo、Jae-yun Kim、Saerom Park、Hoki Kim

- 🎯 **研究动机**：深伪主动防御缺乏统一评测协议，妨碍公平比较并掩盖关键漏洞
- 🔬 **研究方法**：首个系统评破坏性、鲁棒性与迁移性的基准，覆盖像素、感知与身份指标，并引入校准评测评正生成器引入的身份偏差
- 📌 **结论**：保真与身份指标捕捉正交性能轴、单独依赖易得冲突结论；峰值白盒性能往往预示过拟合

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the proliferation of proactive defenses against deepfakes, the lack of a unified evaluation protocol precludes fair comparison and masks critical vulnerabilities. To bridge this gap, we present the first comprehensive benchmark that systematically assesses disruption, robustness, and transferability encompassing pixel, perceptual, and identity metrics. Our extensive analysis reveals that fidelity and identity metrics capture orthogonal performance axes, often leading to conflicting interpretations when relied upon individually. Furthermore, we identify a fundamental trade-off where peak white-box performance signals overfitting, and we introduce a calibrated evaluation to correct generator-induced identity bias. By exposing these blind spots, we establish a rigorous standard to guide the development of genuinely generalizable protections. Project page is available at: https://proactivedefensebenchmark.github.io/

</details>

### 20. Generating Attribution Reports for Manipulated Facial Images: A Dataset and Baseline

🎓 [Official](https://aclanthology.org/2026.acl-long.1405/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`detection`、`deepfake detection`、`media forensics`、`open-world generalization`、`misinformation`

👤 **作者**：Jingchun Lian、…、Zhedong Zheng

- 🎯 **研究动机**：人脸伪造检测只做二分类或像素定位，缺乏对篡改性质的语义解释
- 🔬 **研究方法**：提出伪造归因报告生成任务（定位 Where+解释 Why），构建 152,217 样本的 MMTT 数据集；基线 ForgeryTalker 共享编码器加掩码/文本双解码器
- 📌 **结论**：ForgeryTalker 达 59.3 CIDEr 与 73.67 IoU，建立可解释多媒体取证基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing facial forgery detection methods typically focus on binary classification or pixel-level localization, providing little semantic insight into the nature of the manipulation. To address this, we introduce Forgery Attribution Report Generation, a new multimodal task designed to provide post-hoc forensic evidence for manipulated images. This task jointly localizes forged regions (“Where“) and generates natural language explanations grounded in the editing process (“Why“). This dual-focus approach goes beyond traditional binary forensics, providing a comprehensive, interpretable understanding of the manipulation. To enable research in this domain, we present Multi-Modal Tamper Tracing (MMTT), a large-scale dataset of 152,217 samples. Each sample features a process-derived ground-truth mask and a human-authored textual description, ensuring high annotation precision and linguistic richness. We further propose ForgeryTalker, a unified end-to-end baseline that integrates vision and language via a shared encoder and dual decoders for mask and text generation. Experiments show that ForgeryTalker achieves competitive performance on both subtasks, i.e., 59.3 CIDEr and 73.67 IoU, establishing a strong baseline for explainable multimedia forensics. Our dataset and code are available at: https://github.com/NattyLianJc/Generating-Attribution-Reports.

</details>

### 21. AEGIS: A Holistic Benchmark for Evaluating Forensic Analysis of AI-Generated Academic Images

🎓 [Official](https://aclanthology.org/2026.acl-long.976/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`AI-generated content`、`deepfake detection`、`media forensics`、`misinformation`、`fact-checking`

👤 **作者**：Bo Zhang、…、Haihong E

- 🎯 **研究动机**：AI 生成学术图像的取证能力落后于生成技术，缺乏整体评测基准
- 🔬 **研究方法**：构建 AEGIS：覆盖 7 类学术图像 39 个细粒度子类、25 个生成模型的 4 种伪造策略，联合评测检测、推理与定位，评估 25 个 MLLM 与 9 个专家模型
- 📌 **结论**：GPT-5.1 总体性能仅 48.80%，专家模型定位 IoU 仅 30.09%，11 个生成模型的平均取证准确率低于 50%；MLLM 文本伪影识别达 84.74%，专家检测器二分类最高 79.54%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce AEGIS, A holistic benchmark for Evaluating forensic analysis of AI-Generated academic ImageS. Compared to existing benchmarks, AEGIS features three key advances: (1) Domain-Specific Complexity: covering seven academic categories with 39 fine-grained subtypes, exposing intrinsic forensic difficulty, where even GPT-5.1 reaches 48.80% overall performance and expert models achieve only limited localization accuracy (IoU 30.09%); (2) Diverse Forgery Simulations: modeling four prevalent academic forgery strategies across 25 generative models, with 11 yielding average forensic accuracy below 50%, showing that forensics lag behind generative advances; and (3) Multi-Dimensional Forensic Evaluation: jointly assessing detection, reasoning, and localization, revealing complementary strengths between model families, with multimodal large language models (MLLMs) at 84.74% accuracy in textual artifact recognition and expert detectors peaking at 79.54% accuracy in binary authenticity detection. By evaluating 25 leading MLLMs, nine expert models, and one unified multimodal understanding and generation model, AEGIS serves as a diagnostic testbed exposing fundamental limitations in academic image forensics.

</details>

### 22. DeepfakeImpact: A Two-Stage Benchmark with Real-World Impact in Deepfake Detection

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_DeepfakeImpact_A_Two-Stage_Benchmark_with_Real-World_Impact_in_Deepfake_Detection_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`deepfake impact`、`real-world risk`、`two-stage evaluation`

👤 **作者**：Chaoyu Gong、Han Zhang、Siqiang Luo

- 🎯 **研究动机**：现有深伪检测基准把所有错误等同看待，技术精度与真实世界影响脱节
- 🔬 **研究方法**：两阶段基准：先评估 33 个 SOTA 检测器跨 12 个数据集建立技术基线，再提出量化误判社会危害的 Social Misjudgment Impact 指标并构建高危样本集
- 📌 **结论**：把评测焦点从多准确转向社会效益，为深伪检测器提供更现实、伦理落地的评估基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A fundamental yet overlooked limitation of current deepfake detection benchmark is the lack of evaluation frameworks that align technical accuracy with real-world impact. We argue that technical metrics may fail to capture models' actual capacity to mitigate real-world harm, as they treat all errors as equally significant. To bridge this gap, we introduce DeepfakeImpact, a two-stage benchmark that moves beyond pure technical evaluation toward societally-aware assessment. In Stage I, we establish standardized technical baselines by evaluating 33 SOTA detection baslines across 12 widely used datasets. In Stage II, we propose a novel metric (Social Misjudgment Impact, SMI) that quantifies the potential social harm of misclassified videos, and construct a SMI-critical dataset containing high-risk samples. By integrating SMI-aware performance metrics, we shift the evaluation focus from "how accurate" to "how socially beneficial" a detector is. DeepfakeImpact thus provides a more realistic and ethically-grounded foundation for assessing deepfake detectors, urging the community to rethink what truly constitutes progress in this field. All resources will be publicly released at: https://anonymous.4open.science/r/DeepfakeImpact-Stage1-F5EC.

</details>

### 23. FVBench: Benchmarking Deepfake Video Detection Capability of Large Multimodal Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FVBench_Benchmarking_Deepfake_Video_Detection_Capability_of_Large_Multimodal_Models_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`deepfake video`、`large multimodal model`、`forensic reasoning`

- 🎯 **研究动机**：大多模态模型的deepfake视频检测能力缺基准
- 🔬 **研究方法**：构建覆盖多类型伪造与取证推理的FVBench
- 📌 **结论**：揭示LMM在deepfake视频检测上的显著短板

### 24. TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection

📄 [arXiv](https://arxiv.org/abs/2512.10652) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang-Lin_TriDF_Evaluating_Perception_Detection_and_Hallucination_for_Interpretable_DeepFake_Detection_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`deepfake detection`、`hallucination`、`interpretability`

👤 **作者**：Jian-Yu Jiang-Lin、…、Wen-Huang Cheng

- 🎯 **研究动机**：DeepFake 检测既需判别真伪也需可靠解释，现有评测缺乏对解释可靠性的度量
- 🔬 **研究方法**：提出 TriDF 基准：16 类 DeepFake 覆盖图像、视频与音频，从 Perception（细粒度伪迹识别）、Detection 与 Hallucination（解释可靠性）三方面评测
- 📌 **结论**：MLLM 实验显示准确感知是可靠检测的前提，幻觉严重干扰决策，三者相互依存

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in generative modeling have made it increasingly easy to fabricate realistic portrayals of individuals, creating serious risks for security, communication, and public trust. Detecting such person-driven manipulations requires systems that not only distinguish altered content from authentic media but also provide clear and reliable reasoning. In this paper, we introduce TriDF, a comprehensive benchmark for interpretable DeepFake detection. TriDF contains high-quality forgeries from advanced synthesis models, covering 16 DeepFake types across image, video, and audio modalities. The benchmark evaluates three key aspects: Perception, which measures the ability of a model to identify fine-grained manipulation artifacts using human-annotated evidence; Detection, which assesses classification performance across diverse forgery families and generators; and Hallucination, which quantifies the reliability of model-generated explanations. Experiments on state-of-the-art multimodal large language models show that accurate perception is essential for reliable detection, but hallucination can severely disrupt decision-making, revealing the interdependence of these three aspects. TriDF provides a unified framework for understanding the interaction between detection accuracy, evidence identification, and explanation reliability, offering a foundation for building trustworthy systems that address real-world synthetic media threats.

</details>

### 25. Robust, Generalizable Proactive Face-swapping Defense via Semantic Gradient Divergence

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/988.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`face swapping`、`proactive protection`、`semantic perturbation`

- 🎯 **研究动机**：主动式换脸防御存在可见伪影、跨 deepfake 模型泛化差、易被扩散净化与压缩等后处理破坏的问题
- 🔬 **研究方法**：提出 SGD-Guard：用 CLIP 特征与迭代提炼的广义身份特征构建特征库，在 CLIP-身份联合嵌入空间以共识加权扰动特定面部属性，并按方向差异优先应对关键变换
- 📌 **结论**：有效防御多样换脸模型且跨模型迁移性强，兼顾视觉保真与对净化后处理的鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of identity-feature-based faceswapping technology has raised concerns about impersonation and privacy violations. Although proactive defenses aim to block identity extraction at the source, existing methods suffer from perceptible visual artifacts, poor generalization across diverse deepfake models, and vulnerability to postprocessing techniques (e.g., diffusion purification, image compression, and transformations). This work proposes a robust, generalizable proactive face-swapping defense via semantic gradient divergence (SGD-Guard) to address these challenges. It introduces an integrated feature gallery that uses CLIP features and a generalized identity feature, obtained by iteratively refining heterogeneous identity features into a homogeneous representation. This framework facilitates our semantic distortion attack by leveraging consensus weighting to target specific facial attributes within a CLIP-identity joint embedding space, disrupting deepfake generation while preserving visual fidelity. Furthermore, to ensure robustness against purification and post-processing, this method incorporates a module that prioritizes critical transformations by exploiting directional discrepancies. Comprehensive experiments demonstrate that the method effectively defends against diverse face-swapping models with high cross-model transferability.

</details>

### 26. A Sanity Check for Multi-In-Domain Face Forgery Detection in the Real World

📄 [arXiv](https://arxiv.org/abs/2512.04837) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_A_Sanity_Check_for_Multi-In-Domain_Face_Forgery_Detection_in_the_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`analysis`、`face forgery`、`real-world shift`、`evaluation validity`

👤 **作者**：Jikang Cheng、…、Ling Liang

- 🎯 **研究动机**：多域训练时域间差异而非真假细微差别主导特征空间，检测器域内 AUC 高但域未指定时单图真假判断 ACC 低
- 🔬 **研究方法**：定义 Multi-In-Domain Face Forgery Detection 范式，提出 DevDet：Face Forgery Developer 放大真假差异使其主导特征空间，配合 Dose-Adaptive 检测器微调策略
- 📌 **结论**：在 MID-FFD 场景下真假判别优于基线，同时保持对未见数据的原始泛化能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing methods for deepfake detection aim to develop generalizable detectors. Although "generalizable" is the ultimate target once and for all, with limited training forgeries and domains, it appears idealistic to expect generalization that covers entirely unseen variations, especially given the diversity of real-world deepfakes. Therefore, introducing large-scale multi-domain data for training can be feasible and important for real-world applications. However, within such a multi-domain scenario, the differences between multiple domains, rather than the subtle real/fake distinctions, dominate the feature space. As a result, despite detectors being able to relatively separate real and fake within each domain (i.e., high AUC), they struggle with single-image real/fake judgments in domain-unspecified conditions (i.e., low ACC). In this paper, we first define a new research paradigm named Multi-In-Domain Face Forgery Detection (MID-FFD), which includes sufficient volumes of real-fake domains for training. Then, the detector should provide definitive real-fake judgments to the domain-unspecified inputs, which simulate the frame-by-frame independent detection scenario in the real world. Meanwhile, to address the domain-dominant issue, we propose a model-agnostic framework termed DevDet (Developer for Detector) to amplify real/fake differences and make them dominant in the feature space. DevDet consists of a Face Forgery Developer (FFDev) and a Dose-Adaptive detector Fine-Tuning strategy (DAFT). Experiments demonstrate our superiority in predicting real-fake under the MID-FFD scenario while maintaining original generalization ability to unseen data.

</details>

### 27. AVFakeBench: A Comprehensive Audio-Video Forgery Detection Benchmark for AV-LMMs

📄 [arXiv](https://arxiv.org/abs/2511.21251) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_AVFakeBench_A_Comprehensive_Audio-Video_Forgery_Detection_Benchmark_for_AV-LMMs_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`benchmark`、`audio-video forgery`、`AV-LMM`、`cross-modal consistency`

👤 **作者**：Shuhan Xia、Peipei Li、Xuannan Liu、Dongsen Zhang、Xinyu Guo、Zekun Li

- 🎯 **研究动机**：现有伪造检测基准局限于人脸 deepfake 与单粒度标注，无法覆盖多样真实音视频伪造场景
- 🔬 **研究方法**：AVFakeBench 用私有模型规划加专家生成模型的多阶段混合伪造框架，构建 12K 音视频问题、七类伪造与四级标注，评测 11 个 AV-LMM 与 2 种检测方法
- 📌 **结论**：AV-LMM 有潜力成为伪造检测器，但在细粒度感知与推理上存在明显短板

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The threat of Audio-Video (AV) forgery is rapidly evolving beyond human-centric deepfakes to include more diverse manipulations across complex natural scenes. However, existing benchmarks are still confined to DeepFake-based forgeries and single-granularity annotations, thus failing to capture the diversity and complexity of real-world forgery scenarios. To address this, we introduce AVFakeBench, the first comprehensive audio-video forgery detection benchmark that spans rich forgery semantics across both human subject and general subject. AVFakeBench comprises 12K carefully curated audio-video questions, covering seven forgery types and four levels of annotations. To ensure high-quality and diverse forgeries, we propose a multi-stage hybrid forgery framework that integrates proprietary models for task planning with expert generative models for precise manipulation. The benchmark establishes a multi-task evaluation framework covering binary judgment, forgery types classification, forgery detail selection, and explanatory reasoning. We evaluate 11 Audio-Video Large Language Models (AV-LMMs) and 2 prevalent detection methods on AVFakeBench, demonstrating the potential of AV-LMMs as emerging forgery detectors while revealing their notable weaknesses in fine-grained perception and reasoning.

</details>

### 28. PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs

📄 [arXiv](https://arxiv.org/abs/2608.18573) · 🌐 [Project](https://ai-safety-workshop-ijcai2026.github.io/pdf/PATE-Forensics_Perception-as-Tool_for_Explainable_Deepfake_Forensics_with_General-Purpose_MLLMs.pdf)　📅 2026-08

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`

👤 **作者**：Yaqi Li、Jielun Peng、Yabin Wang、Jincheng Liu、Xiaopeng Hong

- 🎯 **研究动机**：可解释 deepfake 取证依赖任务适配 MLLM 联合做检测、定位与解释，泛化与可解释性受限
- 🔬 **研究方法**：Perception-as-Tool 范式：DINOv3 取证感知工具紧耦合多粒度检测（全局/块/段）与线索引导定位，通用 MLLM 基于结构化取证上下文免微调生成解释
- 📌 **结论**：DDL-X Track 3 官方分 0.89 为最佳，超第二名 0.19 分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing explainable deepfake forensic methods typically rely on task-adapted MLLM to jointly address detection, localization, and explanation. Inspired by agent-style tool use, we instead introduce a Perception-as-Tool paradigm and instantiate it as PATE-Forensics, which architecturally decouples detection and localization from explanation generation while coupling detection and localization as tightly as possible within a forensic perception tool. The DINOv3-based tool couples a multi-granularity detection module that integrates global, patch-level, and segment-level evidence with a cue-guided localization module by spatializing the patch-level and segment-level evidence into forgery score maps that guide dense mask prediction. The original image and forensic perception outputs produced by the tool form structured forensic context for a general-purpose MLLM, which is guided by prompt constraints to generate explanations without task-specific fine-tuning. On DDL-X Track 3, PATE-Forensics achieves the best official score of 0.89, outperforming the second-ranked team by 0.19 points. Our code is available at https://github.com/yqli00000/PATE-Forensics.

</details>

### 29. Environment-Invariant Subspace Learning for Generalizable Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2608.17700)　📅 2026-08

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`

👤 **作者**：Shenghao Chen、Hao Jia、Chen Li、Chunjie Ma、Zan Gao、Shengyong Chen

- 🎯 **研究动机**：视觉基础模型语义先验易受光照与风格等环境干扰，建立的伪造线索-环境伪相关严重限制泛化
- 🔬 **研究方法**：EISL 经可学习低秩投影把特征解耦为正交的伪造相关不变因子与环境残差因子，环境干预模块生成多样干预对模拟 OOD 环境偏移
- 📌 **结论**：跨数据集、跨生成器、全脸合成与损坏设定一致增益，对未见伪造类型与环境变化鲁棒性领先

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cross-distribution generalization remains a critical bottleneck in deepfake detection. While recent efforts leverage the semantic priors of large-scale visual foundation models (VFMs), a noteworthy yet underexplored challenge remains: the susceptibility of these semantic priors to environmental interference from factors such as lighting and style. Crucially, this interference establishes spurious correlations between forgery cues and environmental patterns that severely limit generalization. To address this fundamental challenge, we propose an innovative Environment-Invariant Subspace Learning (EISL) framework. The core contribution of EISL is that it aims to disentangle features into orthogonal forgery-relevant invariant factors and environment-related residual factors via a learnable low-rank projection. To facilitate robust feature disentanglement, we also design an Environmental Intervention module that generates diverse and challenging intervention pairs, simulating out-of-distribution environmental shifts to guide the model toward discovering truly invariant forgery representations. Experiments across cross-dataset, cross-generator, whole-face synthesis, and corruption settings show consistent gains and competitive or leading performance against strong detectors, demonstrating improved robustness to unseen forgery types and environmental variations. This work provides a new perspective and a valuable exploration for understanding and tackling the generalization barriers of VFMs in deepfake detection.

</details>

### 30. MS-MFAD : Multimodal large language models for Face Anti-spoofing Detection

📄 [arXiv](https://arxiv.org/abs/2608.17328)　📅 2026-08

**关键词**：`detection`、`VLM safety`、`deepfake detection`、`media forensics`

👤 **作者**：Xiaoyong Yu、Rongzhen Li、Shuming Shi、Xinge You

- 🎯 **研究动机**：人脸识别面临生成 AI 与高保真物理欺骗的复合威胁，现有防御泛化差、推理不可审计、依赖海量低质数据
- 🔬 **研究方法**：细粒度像素-语义锚定激活 MLLM 内在推理，跨攻击语义级统一标注（每类仅 1000 精确 mask）生成严格对应欺骗区域的证据链，Qwen-VL 监督微调
- 📌 **结论**：域内 ACER 相对降 40-50%，跨域退化限制在 11.62%/5.23%；白盒对抗攻击下精度仅降 3.2%，证据可靠性获从业者 4.57/5 评分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Facial biometric recognition systems currently face compound threats intertwining generative AI and high-fidelity physical spoofing. Existing defenses suffer from systemic bottlenecks, including poor generalization, non-auditable reasoning, and reliance on massive, low-quality datasets. To address these challenges, we propose Multimodal Large Language Models (MFAD) for face anti-spoofing detection, an explainable reasoning system for Unified Face Anti-Spoofing Detection (UFAD), accompanied by a semantic-level annotation benchmark. Unlike methods relying on external tools or coarse alignment, MFAD activates the intrinsic reasoning capabilities of Multimodal Large Language Models (MLLMs) via a fine-grained pixel-semantic anchoring mechanism. This eliminates localization hallucinations and ensures auditable reasoning paths. We introduce a cross-attack semantic-level unified annotation paradigm: by annotating only 1,000 precise masks per attack category, we generate reasoning evidence chains strictly corresponding to spoofed regions. Supervised fine-tuning on the Qwen-VL foundation model demonstrates that, using limited high-quality samples, the system achieves a 40-50% relative reduction in in-domain ACER and restricts cross-domain performance degradation to within 11.62%/5.23%, significantly outperforming existing frameworks. Furthermore, under white-box adversarial attacks, detection accuracy drops by only 3.2%, validating the robustness of semantic anchoring compared to models trained on massive short-text data. Domain practitioners rated the evidence reliability of reasoning paths at 4.57/5, with inference latency satisfying real-time deployment requirements. These results confirm that a few-shot, high-quality semantic annotation paradigm is effective for building trustworthy, explainable, and cost-efficient UFAD systems.

</details>

### 31. FAIR: Feature-Augmented Implicit Regularization for AI-generated Fake Image Detection

📄 [arXiv](https://arxiv.org/abs/2607.22087) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5812)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated image detection`、`AI-generated content`、`deepfake detection`、`cross-generator generalization`、`structural prior`

👤 **作者**：Md Redwanul Haque、Manzur Murshed、Manoranjan Paul、Tsz-Kwan Lee

- 🎯 **研究动机**：AI 生成图像检测器过拟合训练数据低层纹理，跨生成器泛化是关键瓶颈；常规正则不能提供域不变结构
- 🔬 **研究方法**：提出 FAIR：训练时引入正交的宏观结构先验（Scene Composition Structure）增强主特征空间、惩罚纹理捷径；该先验在推理时完全丢弃，零架构与计算开销
- 📌 **结论**：五个大规模基准上把跨生成器泛化准确率提升至多 8.04%，零样本迁移建立新 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generalization remains a critical bottleneck in AI-generated image detection. Because many modern generators are proprietary or adversarially modified, existing detectors overfit to the low-level textural patterns of accessible training data, resulting in severe failures on unseen domains. Conventional regularization techniques (e.g., $L_1$/$L_2$ norms, Dropout) apply indiscriminate parametric constraints and fail to provide the domain-invariant structure necessary for cross-generator robustness. To address this, we propose Feature-Augmented Implicit Regularization (FAIR). FAIR introduces an orthogonal, macro-structural prior, specifically, Scene Composition Structure (SCS), during training to geometrically constrain the model's optimization trajectory. By augmenting the primary feature space with domain-invariant SCS features, FAIR explicitly penalizes texture-biased shortcut learning. Crucially, this structural prior is entirely discarded at inference, yielding a smoothed, generalized decision boundary with zero architectural or computational overhead. Extensive evaluations across five massive benchmarks demonstrate that integrating FAIR into state-of-the-art detectors significantly improves cross-generator generalization, boosting accuracy by up to 8.04% and establishing new state-of-the-art robustness in zero-shot transfer scenarios.

</details>

### 32. PhantomSeal: Proactive Deepfakes Defense with Identity/Context Protection and Forensic Tracing

📄 [arXiv](https://arxiv.org/abs/2607.20564) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-07　🏷 ACM CCS 2026

**关键词**：`detection`、`defense`、`forensic tracing`、`deepfake`、`deepfake detection`、`deepfake prevention`

👤 **作者**：Liangqin Ren、Zeyan Liu、Ye Wang、Yuxin Chen、Fengjun Li、Bo Luo

- 🎯 **研究动机**：现有 deepfake 防御多为事后检测，生成前介入的身份与上下文主动防护有限
- 🔬 **研究方法**：提出 PhantomSeal：嵌入选定诱饵身份作为隐匿标识，使换脸生成偏向诱饵身份从而阻止换脸成功，同时支持基于特征的取证追踪
- 📌 **结论**：跨多种换脸架构有效，把 SimSwap 攻击成功率压至 0.30%，正确识别 97.97% 篡改内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfakes, especially face-swapping attacks, pose significant challenges to authenticity, security, and ethics across science, engineering, and society. While most existing detection/tracing approaches operate post hoc, proactive defenses that aim to intervene before deepfake generation remain limited in terms of real-world effectiveness. In this paper, we present PhantomSeal, the first proactive defense to simultaneously protect both the identity and the context of users' images from being used in face-swapping attacks, while supporting forensic tracing. We present a novel cloaking technique that embeds a selected identity as a stealthy identifier. This mechanism steers the deepfake generation process toward producing content that resembles the chosen cloak identity, thereby preventing successful face-swapping while enabling effective feature-based forensic analysis. The effectiveness and robustness of PhantomSeal is demonstrated in extensive experiments across different face-swapping architectures and models. For example, it reduces the attack success rate of SimSwap, an advanced deepfake model, to 0.30%, and correctly identifies 97.97% of manipulated content. The source codes is available at https://github.com/LiangqinRen/PhantomSeal.

</details>

### 33. μFlow: Leveraging Average Images for Improving Generalisation of Deepfake Faces Detectors

📄 [arXiv](https://arxiv.org/abs/2606.30528) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5525)　📅 2026-06　🏷 ECCV 2026

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`、`one-class learning`、`normalizing flow`

👤 **作者**：Orazio Pontorno、Mattia Litrico、Luca Guarnera、Mario Valerio Giuffrida、Sebastiano Battiato

- 🎯 **研究动机**：有监督深度伪造检测器依赖真假混合训练，跨生成器（GAN vs 扩散）泛化受限
- 🔬 **研究方法**：提出 μFlow 单类检测器：只用真实图像训练，利用多图平均放大一致的生成痕迹，训练 normalizing flow 把单图特征对齐到均值图像特征分布，以似然判别真假
- 📌 **结论**：在全分布外设定（真假数据集均未见）下显著超过 SOTA 检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current generative models, including GANs and diffusion models, have reached an outstanding level of photorealism, posing significant risks to privacy and security. To ensure real-world applicability, deepfake detectors must generalise effectively to unseen generators. However, most existing approaches rely on supervised training with both real and fake images, which limits their generalisation especially across generators categories (e.g. GANs vs DMs). In this work, we introduce $μ$Flow, a one-class deepfake detector trained only on real images without relying on pseudo-deepfakes or synthetic artifacts. Our approach builds on the observation that averaging multiple images amplifies consistent generative traces, producing highly discriminative feature representations. We leverage this property by modelling the distribution of features extracted from averaged images and training a normalizing flow to align the feature space of individual images with this distribution. This alignment yields a likelihood-based criterion that separates real and fake samples while promoting strong generalisation. We evaluate $μ$Flow on a fully out-of-distribution setting, where both real and fake datasets are unseen during training. Experimental results show that our method significantly outperforms SOTA detectors. Project page: https://opontorno.github.io/MuFlow.

</details>

### 34. Trustworthy Image Authentication using Forensic Knowledge Graphs

📄 [arXiv](https://arxiv.org/abs/2606.23917) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3521)　📅 2026-06　🏷 ECCV 2026

**关键词**：`detection`、`image authentication`、`knowledge graph`、`VLM safety`、`evidence explanation`

👤 **作者**：Tai D. Nguyen、Matthew C. Stamm

- 🎯 **研究动机**：已有取证检测器缺乏可解释性，VLM 能解释却无法利用取证痕迹做可靠检测
- 🔬 **研究方法**：提出 Forensic Knowledge Graphs：编码取证痕迹及其因果依赖与场景内容关联，配套取证认证网络与迭代上下文精炼策略；构建 FKG-50K（5 万真实伪造+真值 FKG）
- 📌 **结论**：在检测、伪造识别定位与取证论证三方面超过取证检测器与 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in generative AI have made image falsification highly realistic, demanding trustworthy authentication systems. Existing forensic detectors can target certain forgery types but lack interpretability, while vision-language models (VLMs) provide explanations but cannot exploit forensic traces for reliable detection. We propose Forensic Knowledge Graphs (FKGs), a unified framework that integrates forensic evidence extraction, structured reasoning, and human-interpretable explanation. Our FKG structure encodes forensic traces along with their causal dependencies and links to scene content. To generate accurate FKGs, we introduce a novel forensic authentication network and an Iterative Context Refinement strategy that guides VLMs to produce faithful, grounded explanations. We also present FKG-50K, a dataset of 50,000 realistic forgeries with ground-truth FKGs. Experiments demonstrate that FKG outperforms both forensic detectors and VLMs in detection, forgery identification and localization, and forensic justification.

</details>

### 35. On Improving Robustness of Deepfake Image Detectors

📄 [arXiv](https://arxiv.org/abs/2606.02797) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shahjahan)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`detection`、`defense`、`deepfake detection`、`robustness`、`deepfake`、`domain shift`

👤 **作者**：Abu Taib Mohammed Shahjahan、Mohammad Mannan、Abdessamad Ben Hamza、Amr Youssef

- 🎯 **研究动机**：最新 deepfake 检测器在对抗攻击下仍大幅退化，此前 IEEE SP 2024 等工作已证实这一点
- 🔬 **研究方法**：融合 DCT 四阶矩池化、噪声残差内容无关特征与 patch 级语义破坏三原则，利用对抗攻击难以约束高阶残差频谱（尤其峰度）的盲区构建统一框架
- 📌 **结论**：六种检测器上一致提升鲁棒性，recall 退化最多降低 88.9%，将 CVPR 2025 最佳检测器受攻击准确率从 81.9% 提到 97.15%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Generative AI has introduced remarkable opportunities while simultaneously raising critical concerns regarding content authenticity. While recent work has increasingly focused on improving the generalization of deepfake detectors across unseen generative models, their robustness against adversarial attacks remains limited. In particular, Abdullah et al. (IEEE SP 2024) evaluated eight detectors and demonstrated that most of them exhibit significant performance degradation under adversarial attacks. We also observed the same phenomenon by testing seven most recent state-of-the-art detectors. To address this problem, we propose a unified framework that integrates three complementary design principles without relying on adversarial training data: (i) higher-order statistical modeling in the frequency domain via Discrete Cosine Transform (DCT)-based moment pooling up to fourth order, (ii) content-agnostic feature representations derived from noise residuals, and (iii) cross-scene generalization enforced through patch-level semantic disruption. A key insight underpinning our approach is that adversarial attacks primarily operate on low-order statistics and visual semantics, leaving higher-order residual-frequency characteristics, particularly kurtosis, largely unconstrained. Extensive experiments demonstrate that our method consistently improves robustness across six architecturally diverse detectors. Notably, we achieve up to 88.9% reduction in recall degradation on current adversarial benchmarks, and improve the best-performing recent detector (Yang et al., IEEE CVPR 2025) from 81.9% to 97.15% accuracy under attack. Overall, our method provides a principled, architecture-agnostic approach for improving deepfake detection robustness against current attacks.

</details>

### 36. ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation

📄 [arXiv](https://arxiv.org/abs/2605.16080) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_ReAlign_Generalizable_Image_Forgery_Detection_via_Reasoning-Aligned_Representation_CVPR_2026_paper.html)　📅 2026-05　🏷 CVPR 2026

**关键词**：`detection`、`image forgery`、`reasoning alignment`、`cross-domain generalization`

👤 **作者**：Qing Huang、Zhipei Xu、Xuanyu Zhang、Xiangyu Yu、Jian Zhang

- 🎯 **研究动机**：非 LLM 伪造检测器缺语义理解，LLM 方法计算昂贵且对细微视觉伪影不敏感；推理文本对检测的真实贡献不明
- 🔬 **研究方法**：ReAlign 把 GRPO 优化 LLM 生成的高质量推理文本经对比学习蒸馏进轻量检测器，联合对比对齐与分类损失
- 📌 **结论**：在 AIGCDetectBenchmark、AIGI-Holmes 与新构造的 UltraSynth-10k 上准确率与泛化均超 SOTA，尤以高保真伪造突出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of AI-generated images (AIGIs) poses growing challenges for digital authenticity, prompting the need for efficient, generalizable image forgery detection systems. Existing methods, whether non-LLM-based or LLM-based, exhibit distinct advantages and limitations. While non-LLM-based models offer efficient low-level artifact detection, they often lack semantic understanding. Conversely, LLM-based methods provide strong semantic reasoning and explainability but are computationally intensive and less sensitive to subtle visual artifacts. Moreover, the true contribution of explanatory reasoning texts to forgery detection performance remains unclear. In this work, we investigate the intrinsic value and potential of LLM-generated reasoning texts, considering it a source of generalization and semantic-error sensitivity. Based on these findings, we propose ReAlign, a novel framework that distills high-quality reasoning texts generated by a GRPO-optimized LLM into a lightweight AIGI detector via contrastive learning. ReAlign effectively inherits the generalization ability and semantic sensitivity capability of reasoning textual representations, while remaining efficient and lightweight for deployment. Moreover, ReAlign adopts a tailored joint optimization strategy that integrates contrastive loss for image-text alignment and classification loss for accurate forgery discrimination. Experimental results on AIGCDetectBenchmark, AIGI-Holmes, and our newly constructed UltraSynth-10k demonstrate that ReAlign consistently outperforms existing state-of-the-art detectors in both accuracy and generalization, particularly when facing complex, high-fidelity forgeries from modern generative models.

</details>

### 37. OmniVL-Guard: Towards Unified Vision-Language Forgery Detection and Grounding via Balanced RL

📄 [arXiv](https://arxiv.org/abs/2602.10687) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63742)　📅 2026-02　🏷 ICML 2026

**关键词**：`detection`、`defense`、`VLM safety`、`deepfake detection`、`media forensics`、`reinforcement learning`

👤 **作者**：Jinjie Shen、…、Zhun Zhong

- 🎯 **研究动机**：伪造检测局限于单/双模态且简单分类任务主导梯度，损害细粒度定位的多任务优化
- 🔬 **研究方法**：OmniVL-Guard 以自进化 CoT 生成解决冷启动，ARSPO 自适应调节奖励尺度与任务权重实现均衡联合优化
- 📌 **结论**：显著超越 SOTA 并在域外场景零样本鲁棒泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing forgery detection methods are often limited to uni-modal or bi-modal settings, failing to handle the interleaved text, images, and videos prevalent in real-world misinformation. To bridge this gap, this paper targets to develop a unified framework for omnibus vision-language forgery detection and grounding. In this unified setting, the {interplay} between diverse modalities and the dual requirements of simultaneous detection and localization pose a critical ``difficulty bias`` problem: the simpler veracity classification task tends to dominate the gradients, leading to suboptimal performance in fine-grained grounding during multi-task optimization. To address this challenge, we propose \textbf{OmniVL-Guard}, a balanced reinforcement learning framework for omnibus vision-language forgery detection and grounding. Particularly, OmniVL-Guard comprises two core designs: Self-Evolving CoT Generatio and Adaptive Reward Scaling Policy Optimization (ARSPO). {Self-Evolving CoT Generation} synthesizes high-quality reasoning paths, effectively overcoming the cold-start challenge. Building upon this, {Adaptive Reward Scaling Policy Optimization (ARSPO)} dynamically modulates reward scales and task weights, ensuring a balanced joint optimization. Extensive experiments demonstrate that OmniVL-Guard significantly outperforms state-of-the-art methods and exhibits zero-shot robust generalization across out-of-domain scenarios. The dataset and code are publicly available at https://github.com/shen8424/OmniVL-Guard.

</details>

### 38. Revisiting Deepfake Detection: BCNet for Robust Generalization Beyond Semantic Dependence

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5201)　📅 2026　🏷 ECCV 2026

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`、`cross-generator generalization`、`semantic shortcut`

- 🎯 **研究动机**：deepfake检测依赖语义捷径，跨生成器泛化差
- 🔬 **研究方法**：BCNet剥离语义依赖，学习非语义伪造伪影
- 📌 **结论**：跨生成器泛化显著提升

### 39. PRPO: Paragraph-level Policy Optimization for Vision-Language Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2509.26272) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65679)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`VLM safety`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Tuan Nguyen、Naseem Khan、Khang Tran、NhatHai Phan、Issa Khalil

- 🎯 **研究动机**：MLLM 深伪检测表现差，解释常与视觉证据错位或产生幻觉
- 🔬 **研究方法**：构建推理标注深伪检测数据集，PRPO 强化学习在段落级对齐 LLM 推理与图像内容
- 📌 **结论**：检测准确率大幅提升，推理评分最高 4.55/5.0，测试时显著超 GRPO

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid rise of synthetic media has made deepfake detection a critical challenge for online safety and trust. Progress remains constrained by the scarcity of large, high-quality datasets. Although multimodal large language models (LLMs) exhibit strong reasoning capabilities, their performance on deepfake detection is poor, often producing explanations that are misaligned with visual evidence or hallucinatory. To address this limitation, we introduce a reasoning-annotated dataset for deepfake detection and propose Paragraph-level Relative Policy Optimization (PRPO), a reinforcement learning algorithm that aligns LLM reasoning with image content at the paragraph level. Experiments show that PRPO improves detection accuracy by a wide margin and achieves the highest reasoning score of 4.55/5.0. Ablation studies further demonstrate that PRPO significantly outperforms GRPO under test-time conditions. These results underscore the importance of grounding multimodal reasoning in visual evidence to enable more reliable and interpretable deepfake detection.

</details>

### 40. Order within Chaos: Capturing Intrinsic Energy Anomalies for AI-Manipulated Image Forgery Localization

📄 [arXiv](https://arxiv.org/abs/2606.02178) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66704)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`media forensics`、`open-world generalization`、`diffusion model`、`cross-generator generalization`

👤 **作者**：Yiming Wang、Baiqi Wu、Qingming Li、Jiahao Chen、Tong Zhang、Shouling Ji

- 🎯 **研究动机**：生成式编辑伪造不含物理噪声，依赖物理噪声的传统篡改定位方法失效
- 🔬 **研究方法**：理论证明扩散过程固有抑制局部高频方差、形成可与光学成像熵区分的能量 gap；FLAME 用 LAD 图捕获内在异常并以参数高效 SAM 适配器做像素级定位；EditStream 自动合成指令式训练数据
- 📌 **结论**：SOTA，在 AI 生成伪造数据集上大幅超先前方法并泛化到未见生成架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in generative AI have led to image editing models capable of producing realistic forgeries that evade traditional image forgery localization methods, as these approaches depend on physical noise absent in synthetic data. To address this challenge, we theoretically demonstrate that the diffusion process inherently suppresses local high-frequency variance, creating a statistical energy gap that is distinguishable from the natural entropy of optical imaging. Guided by this insight, we propose FLAME, a unified framework that utilizes a LAD map to capture these intrinsic anomalies, coupled with a parameter-efficient adapter for SAM to achieve precise, pixel-level forgery localization. Furthermore, to bridge the lag between forensic benchmarks and evolving generative models, we introduce EditStream, an automated pipeline for continuous, instruction-based training data synthesis. Extensive experiments demonstrate that FLAME establishes a new state-of-the-art, significantly outperforming previous methods on AI-generated forgery datasets while effectively generalizing to unseen generative architectures. Our code is available at https://github.com/phoenixnir/FLAME.

</details>

### 41. MedForge: Interpretable Medical Deepfake Detection via Forgery-aware Reasoning

🎓 [Official](https://aclanthology.org/2026.acl-long.1177/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`reasoning safety`、`deepfake detection`、`medical AI`

👤 **作者**：Zhihui Chen、…、Mengling Feng

- 🎯 **研究动机**：文本引导编辑可对医学影像植入或删除病灶；医学检测器黑箱、MLLM 解释事后且缺医学知识易幻觉
- 🔬 **研究方法**：MedForge-90K 覆盖 19 类病理的现实病灶编辑并附医生检查指南推理监督；MedForge-Reasoner 先定位后分析并用 Forgery-aware GSPO 强化证据锚定
- 📌 **结论**：检测准确率 SOTA 且解释可信、与专家对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-guided image editors can now manipulate authentic medical scans with high fidelity, enabling lesion implantation/removal that threatens clinical trust and safety. Existing defenses are inadequate for healthcare. Medical detectors are largely black-box, while MLLM-based explainers are typically post-hoc, lack medical expertise, and may hallucinate evidence on ambiguous cases. We present MedForge, a data-and-method solution for pre-hoc, evidence-grounded medical forgery detection. We introduce MedForge-90K, a large-scale benchmark of realistic lesion edits across 19 pathologies with expert-guided reasoning supervision via doctor inspection guidelines and gold edit locations. Building on it, MedForge-Reasoner performs localize-then-analyze reasoning, predicting suspicious regions before producing a verdict, and is further aligned with Forgery-aware GSPO to strengthen grounding and reduce hallucinations. Experiments demonstrate state-of-the-art detection accuracy and trustworthy, expert-aligned explanations.

</details>

### 42. Forensic Prompting with Dual-Action Policy Optimization for Vision-Language Forgery Detection and Localization

🎓 [Official](https://icml.cc/virtual/2026/poster/60710)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`VLM safety`、`deepfake detection`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Ye Zhu、Ai Zhao、Jinwei Wang

- 🎯 **研究动机**：图像伪造痕迹趋细微且易被后处理衰减；开放式 LLM 提示难约束、朴素语言描述引入语义扰动
- 🔬 **研究方法**：FPDA：取证提示模块构建结构化可复现提示库并支持可选文本做可靠性线索；Dual-Action Policy Optimization 逐图路由取证提示与调度定位精炼
- 📌 **结论**：覆盖手工篡改、扩散内容、人脸伪造与文本使能设定的多数据集上检测与定位优于 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image forgery is rapidly evolving, rendering forensic traces increasingly subtle and readily attenuated by post-processing. Although vision-language prompting can inject priors, open-ended LLM-generated prompts are difficult to constrain, and naive language descriptions can introduce semantic perturbations. To address these challenges, we propose Forensic Prompting with Dual-Action policy optimization (FPDA) for vision-language forgery detection and localization, where the Forensic Prompting Module (FPM) constructs a structured and reproducible forensic prompt bank and supports optional text input as a reliability-aware cue for stable conditioning. Moreover, Dual-Action Policy Optimization (DAPO) is applied to learn sample-adaptive evidence usage by routing forensic prompts and scheduling localization refinement on a per-image basis, stabilizing discriminative cues and improving mask spatial consistency. Extensive experiments are conducted on multiple public datasets covering manual manipulations, diffusion content, face forgeries, and text-enabled settings, demonstrating favorable detection and localization performance over representative state-of-the-art methods under comparable evaluation protocols.

</details>

### 43. Divide and Conquer: Reliable Multi-View Evidential Learning for Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2606.01885) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61751)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Xiaolu Kang、…、Qian Wang

- 🎯 **研究动机**：深伪趋近完美语义真实、取证痕迹只剩细微结构异常；单视图范式语义特征淹没伪影线索（Semantic Masking Effect），预测过自信而脆弱
- 🔬 **研究方法**：DiCoME：Divide 阶段经几何投影解缠表征、抑制伪影敏感表征中的语义干扰；Conquer 阶段不确定度感知证据学习显式建模语义与伪影线索的认知冲突、输出校准不确定度
- 📌 **结论**：多基准泛化性能一致领先并提供可信的不确定度估计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the evolution of generative models, deepfakes have achieved near-perfect semantic realism, leaving forensic traces only in subtle structural anomalies. However, existing single-view paradigms often fail to generalize, as dominant semantic features overwhelm subtle artifact cues within entangled representations. This imbalance leads to overconfident yet brittle predictions—a phenomenon we term the Semantic Masking Effect. To address this challenge, we propose a reliable framework called Divide-and-Conquer Multi-View Evidential Learning (DiCoME) for Deepfake Detection. In the "Divide'' phase, we employ Geometric View Purification to decompose the entangled representation space through principled geometric projection. This process suppresses semantic interference within artifact-sensitive representations, forming the foundation for decorrelated yet complementary semantic and artifact views. In the "Conquer'' phase, we leverage Uncertainty-Aware Evidential Learning to synthesize these distinct views. By explicitly modeling the "epistemic conflict'' between semantic and artifact cues, this mechanism provides calibrated uncertainty estimates instead of forcing rigid deterministic decisions. Extensive experiments across multiple benchmarks demonstrate that our method consistently outperforms existing approaches in generalization performance, while providing reliable uncertainty estimation for trustworthy deepfake detection. Code is available at https://github.com/kxl0825/DiCoME.git.

</details>

### 44. Deep Residual Injection for Full-Spectrum Forensic Signal Perception in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.15880) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63980)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`VLM safety`、`deepfake detection`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Kaiqing Lin、…、Shouhong Ding

- 🎯 **研究动机**：生成图像趋真使仅靠语义级不一致不足以可靠检测；直接微调 MLLM 学伪影又会快速遗忘预训练语义
- 🔬 **研究方法**：层析分析发现语义主要编码于早中层；Deep-VRM 保留早期语义处理并把伪影特定视觉残差注入中间层与语义 token 融合，经后续可训练层联合建模
- 📌 **结论**：全部基准达 SOTA，模型自适应利用不同层级取证信号，检测鲁棒且可泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have been increasingly adopted in forensics for their robust semantic understanding. As AI-generated images become realistic, semantic-level inconsistencies alone are often insufficient for reliable detection. This motivates a critical question: whether MLLMs can achieve full-spectrum forensic signal perception, i.e., capturing low-level generator artifacts without sacrificing pre-trained semantic knowledge. We then conduct a layer-wise analysis of forensic signal perception in MLLMs and find that semantic information is mainly encoded in the early-to-middle layers, and directly fine-tuning MLLMs for artifact learning causes rapid semantic forgetting. Based on this insight, we propose Deep Visual Residual MLLM (Deep-VRM) to \textit{preserve early semantic processing while injecting artifact-specific visual signals as a residual path into an intermediate layer}, where they are fused with semantic token representations and propagated through subsequent trainable layers. This enables later layers to jointly model semantic reasoning and signal-level forensic cues, and surprisingly, the model learns to adaptively leverage different levels of forensic signals depending on the input, achieving robust and generalizable detection performance. Extensive experiments show that our method achieves state-of-the-art across all benchmarks.

</details>

### 45. Cultivating Forensic Reasoning for Generalizable Multimodal Manipulation Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1316/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`multimodal safety`、`reasoning safety`、`VLM safety`、`deepfake detection`

👤 **作者**：Yuchen Zhang、…、Zhedong Zheng

- 🎯 **研究动机**：现有操纵检测以结果导向监督做类型分类，缺乏可解释性且过拟合表面伪影
- 🔬 **研究方法**：REFORM 三阶段课程从结果拟合转向过程建模：诱导取证理由、对齐推理与判断、强化学习精炼逻辑一致性；配大规模推理标注数据集 ROM
- 📌 **结论**：ROM 81.52% ACC、DGM4 76.65% ACC、MMFakeBench 74.9 F1，建立新 SOTA 且泛化优越

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative AI have significantly enhanced the realism of multimodal media manipulation, thereby posing substantial challenges to manipulation detection. Existing manipulation detection and grounding approaches predominantly focus on manipulation type classification under result-oriented supervision, which not only lacks interpretability but also tends to overfit superficial artifacts. In this paper, we argue that generalizable detection requires incorporating explicit forensic reasoning, rather than merely classifying a limited set of manipulation types, which fails to generalize to unseen manipulation patterns. To this end, we propose REFORM, a reasoning-driven framework that shifts learning from outcome fitting to process modeling. REFORM adopts a three-stage curriculum that first induces forensic rationales, then aligns reasoning with final judgments, and finally refines logical consistency via reinforcement learning. To support this paradigm, we introduce ROM, a large-scale dataset with rich reasoning annotations. Extensive experiments show that REFORM establishes new state-of-the-art performance with superior generalization, achieving 81.52% ACC on ROM, 76.65% ACC on DGM4, and 74.9 F1 on MMFakeBench.

</details>

### 46. Breaking Manifold Continuity: Vector Quantized Modeling for Real-Centric Deepfake Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/63477)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`diffusion model`、`cross-generator generalization`

👤 **作者**：Changshuo Wang、…、Lizhuang Ma

- 🎯 **研究动机**：真实中心深伪检测普遍用连续建模构建真实流形，连续性反而便利伪造伪影插值、造成检测歧义
- 🔬 **研究方法**：在 CLIP 视觉编码器特征空间引入可学习向量量化码本离散化真实潜流形、施加更严信息瓶颈，自适应切空间投影提供可控的连续松弛
- 📌 **结论**：构建既紧约束又广可泛化的真实分布，对未见伪造更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasingly realistic and diverse generative data has led some deepfake detection methods to shift towards learning robust real content, e.g., via reconstruction-based tasks. However, most existing approaches rely primarily on prevalent continuous modeling (e.g., GMMs, VAEs, Diffusion Models) to construct a continuous latent manifold of real data, with the aim of improving the generalization capability, while overlooking a critical issue, i.e., such continuity may facilitate the interpolation of forgery artifacts, consequently causing ambiguity in detection. To alleviate this problem, we integrate discrete modeling into the feature space of the CLIP vision encoder, striking a balance between continuous manifold modeling and discrete representation. By incorporating a learnable vector quantized codebook, the real latent manifold is discretized, imposing a more stringent information bottleneck that reduces the likelihood of embedding generative artifacts. In order to further enhance the generalization of discrete modeling, we propose an adaptive tangent space projection mechanism that yields a continuous relaxation of the discrete real distribution within a controllable range. With these components, our method constructs a real distribution that is both tightly constrained and broadly generalizable, enhancing robustness to unseen forgeries. Extensive experiments on diverse datasets demonstrate the effectiveness of our method.

</details>

### 47. BPL: Generalizable Deepfake Detection via Bias-only Pair-aware Learning

🎓 [Official](https://icml.cc/virtual/2026/poster/61612)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`deepfake`、`media forensics`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Yuxiang Xu、…、Yilong Yin

- 🎯 **研究动机**：深伪检测的二元分类忽视合成图像与共享语义源的真实图像隐式配对的结构性质，且模型快速过拟合已见伪模式
- 🔬 **研究方法**：BPL 经源引导映射或 CLIP 空间近邻关系显式挖掘真-假对，配对差异学习放大生成偏差、差异反转缓解过拟合，bias-only 微调限制适应期容量
- 📌 **结论**：对未见伪造模式实现优越的跨生成器泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The detection of synthetic images has traditionally been framed as a binary classification problem. However, we argue that this formulation overlooks a fundamental structural property of generative datasets: synthetic images are not independent samples, but are implicitly paired with real images sharing the same semantic source. Existing methods treat real and fake images as independent instances, failing to capture generation-induced relational discrepancies in real–fake pairs. Moreover, models tend to rapidly overfit to seen fake patterns, leading to poor generalization to unseen ones. To overcome these challenges, we propose a novel detection framework that explicitly mines real–fake pairs by constructing source-guided mappings or leveraging nearest-neighbor relationships in the CLIP embedding space. We then introduce pair-wise discrepancy learning that explicitly enlarges generation-induced deviations and discrepancy inversion to mitigate overfitting. Moreover, to preserve pretrained semantic representations while improving generalization, we adopt a bias-only fine-tuning scheme that restricts model capacity during adaptation. Extensive experiments show that our approach achieves superior generalization across unseen fake patterns.

</details>

### 48. Asymmetric Anchoring: Opening the Black Box of MLLMs for Forgery Detection

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5294)　📅 2026　🏷 ECCV 2026

**关键词**：`detection`、`forgery detection`、`deepfake detection`、`media forensics`、`image forensics`、`multimodal model`

- 🎯 **研究动机**：MLLM用于伪造检测的内部判别依据不透明
- 🔬 **研究方法**：以非对称锚定探查MLLM内部表征，定位伪造相关证据
- 📌 **结论**：提升伪造检测的可解释性与准确性

### 49. Pixels Don't Lie (But Your Detector Might): Bootstrapping MLLM-as-a-Judge for Trustworthy Deepfake Detection and Reasoning Supervision

📄 [arXiv](https://arxiv.org/abs/2602.19715) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Kuckreja_Pixels_Dont_Lie_But_Your_Detector_Might_Bootstrapping_MLLM-as-a-Judge_for_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`deepfake reasoning`、`MLLM judge`、`supervision reliability`

👤 **作者**：Kartik Kuckreja、Parul Gupta、Muhammad Haris Khan、Abhinav Dhall

- 🎯 **研究动机**：深伪检测模型的自然语言解释常不锚定视觉证据，现有评测只测分类准确率忽视推理忠实度
- 🔬 **研究方法**：DeepfakeJudge 含 OOD 基准、人工标注视觉推理标签子集与免金标理由的评估套件；bootstrapped generator-evaluator 流程把人类反馈扩展为结构化推理监督
- 📌 **结论**：推理自举模型准确率 96.2% 超 30 倍大基线；judge 与人类评分高相关、成对一致率 98.9%；用户 70% 偏好其推理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection models often generate natural-language explanations, yet their reasoning is frequently ungrounded in visual evidence, limiting reliability. Existing evaluations measure classification accuracy but overlook reasoning fidelity. We propose DeepfakeJudge, a framework for scalable reasoning supervision and evaluation, that integrates an out-of-distribution benchmark containing recent generative and editing forgeries, a human-annotated subset with visual reasoning labels, and a suite of evaluation models, that specialize in evaluating reasoning rationales without the need for explicit ground truth reasoning rationales. The Judge is optimized through a bootstrapped generator-evaluator process that scales human feedback into structured reasoning supervision and supports both pointwise and pairwise evaluation. On the proposed meta-evaluation benchmark, our reasoning-bootstrapped model achieves an accuracy of 96.2%, outperforming \texttt 30x larger baselines. The reasoning judge attains very high correlation with human ratings and 98.9% percent pairwise agreement on the human annotated meta-evaluation subset. These results establish reasoning fidelity as a quantifiable dimension of deepfake detection and demonstrate scalable supervision for interpretable deepfake reasoning. Our user study indicates that humans prefer reasonings generated by our framework 70% of the time, in faithfullness, groundedness and usefulness compared to other models and datasets. All of our datasets, models, and codebase will be open-sourced.

</details>

### 50. Editprint: General Digital Image Forensics via Editing Fingerprint with Self-Augmentation Training

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Editprint_General_Digital_Image_Forensics_via_Editing_Fingerprint_with_Self-Augmentation_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`editing fingerprint`、`image forensics`、`self-augmentation`

👤 **作者**：Haiwei Wu、Kemou Li、Yuanman Li、Jiantao Zhou

- 🎯 **研究动机**：现有取证方法只关注相机特定痕迹（如 PRNU）且需大量标注数据
- 🔬 **研究方法**：Editprint 通用取证特征：相同成像-编辑-传输链产生相同指纹；自增强在线编辑池仅需约 10 条训练数据模拟约 10^7 条编辑链，以链条文本描述为标签做语言引导对比学习
- 📌 **结论**：超越现有自监督取证方法，社交网络溯源与合成图像检测等非相机应用尤佳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Digital image forensics can ensure information credibility in tasks like camera source identification (CSI), synthetic image detection (SID), and social network provenance (SNP). These tasks typically rely on image processing history clues left by in-camera operations, post-capture editing, or synthetic generation. However, most existing forensic methods have obvious limitations: 1) they often only focus on camera-specific traces (e.g., the well-known PRNU), and 2) they demand a substantial amount of annotated training data. To address these constraints, we propose Editprint, a novel general forensic feature that captures highly diverse in- and out-camera processing history clues with minimal unlabeled training data. Ideally, we expect that any images undergoing the same imaging, editing, and transmission processes would yield identical Editprints, and vice versa. To model the in- and out-camera operations, we devise an online editing pool based on self-augmentation strategies. Requiring only minimal (e.g., 10) training data, the editing pool can simulate massive (e.g., 10^\text 7 ) editing chains and traces arising from the in-camera processing and the subsequent out-camera operations. To ensure that Editprint exhibits high discriminative capabilities across various editing chains, we propose using textual descriptions of these chains as labels and supervising their Editprints through language-guided contrastive learning. Extensive experiments show Editprint outperforms existing self-supervised forensics, particularly in non-camera applications such as SNP and SID. We hope that Editprint would inspire the forensic community and serve as a novel benchmark for self-supervised forensics.

</details>

### 51. Breaking the Trade-off: Orthogonal Semantic Decoupling for Generalizable and Fair Deepfake Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1712.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`deepfake`、`cross-domain generalization`、`demographic shortcut`

- 🎯 **研究动机**：深伪检测的跨域泛化与人口公平性存在权衡：泛化导向检测器过度依赖人口捷径，公平约束又使优化偏离最具判别力的边界
- 🔬 **研究方法**：OSD 对视觉语言模型预训练权重做 SVD，冻结主语义子空间并在残差子空间学习参数高效低秩专家——按组采样并路由的人口语义专家加跨域可迁移的通用伪造专家
- 📌 **结论**：多个基准上泛化与公平双双超越 SOTA，打破两者的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection faces dual challenges in real-world deployment: cross-domain generalization and demographic fairness. Existing approaches often struggle with a trade-off between these goals. Generalization-oriented detectors can over-rely on demographic shortcuts, while fairness constraints tend to steer optimization away from the most discriminative decision boundary. To address this, we propose Orthogonal Semantic Decoupling (OSD), a framework that decouples demographic semantics from forgery cues. Specifically, we perform Singular Value Decomposition on the pretrained weights of a vision-language model, freezing the principal semantic subspace while learning parameter-efficient low-rank experts in the residual subspace. The experts comprise Demographic Semantic Experts, a set of experts specialized via group sampling and routed based on the similarities between image embeddings and text embeddings of predefined descriptions; and a Universal Forgery Expert, which captures forgery features transferable across domains and demographics. Extensive experiments across multiple benchmarks demonstrate that our approach outperforms state-of-the-art methods in both generalization and fairness, breaking the trade-off. The code is available at https://github.com/sonder-lin/ osd-deepfake-detection.

</details>

### 52. Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection

📄 [arXiv](https://arxiv.org/abs/2512.16300) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5823)　📅 2025-12　🏷 ECCV 2026

**关键词**：`detection`、`image forensics`、`tool use`、`agent`

👤 **作者**：Fanrui Zhang、…、Kaipeng Zhang

- 🎯 **研究动机**：图像取证中低层伪影与高层语义两类信息在范式与推理上高度异构，现有方法难以统一并建模跨层交互
- 🔬 **研究方法**：ForenAgent 让 MLLM 围绕检测目标自主生成、执行并迭代精炼 Python 低层工具，采用 Cold Start 加强化微调两阶段训练与全局感知-局部聚焦-迭代探测-整体裁决的动态推理环，并构建 10 万图、约 20 万问答对的 FABench
- 📌 **结论**：在困难取证任务上涌现工具使用与反思推理能力，迈向通用 IFD

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing image forgery detection (IFD) methods either exploit low-level, semantics-agnostic artifacts or rely on multimodal large language models (MLLMs) with high-level semantic knowledge. Although naturally complementary, these two information streams are highly heterogeneous in both paradigm and reasoning, making it difficult for existing methods to unify them or effectively model their cross-level interactions. To address this gap, we propose ForenAgent, a multi-round interactive IFD framework that enables MLLMs to autonomously generate, execute, and iteratively refine Python-based low-level tools around the detection objective, thereby achieving more flexible and interpretable forgery analysis. ForenAgent follows a two-stage training pipeline combining Cold Start and Reinforcement Fine-Tuning to enhance its tool interaction capability and reasoning adaptability progressively. Inspired by human reasoning, we design a dynamic reasoning loop comprising global perception, local focusing, iterative probing, and holistic adjudication, and instantiate it as both a data-sampling strategy and a task-aligned process reward. For systematic training and evaluation, we construct FABench, a heterogeneous, high-quality agent-forensics dataset comprising 100k images and approximately 200k agent-interaction question-answer pairs. Experiments show that ForenAgent exhibits emergent tool-use competence and reflective reasoning on challenging IFD tasks when assisted by low-level tools, charting a promising route toward general-purpose IFD. The code will be released after the review process is completed.

</details>

### 53. Few-Shot Synthetic Image Attribution: Identifying Unseen Generators with Limited Samples

📄 [arXiv](https://arxiv.org/abs/2509.25682) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5926)　📅 2025-09　🏷 ECCV 2026

**关键词**：`detection`、`deepfake detection`、`media forensics`、`open-world generalization`、`generator attribution`、`few-shot learning`

👤 **作者**：Shiyu Wu、Shuyan Li、Jing Li、Jing Liu、Yequan Wang

- 🎯 **研究动机**：既有 AI 生成图像源归因闭集运行，识别新生成器需重训练，无法适应快速演化
- 🔬 **研究方法**：提出少样本归因范式，构建 45 个生成器共 117 万图像的 OmniFake 数据集与同时判真伪和归因来源的 OmniDFA 基线
- 📌 **结论**：少样本归因能力出色，AIGI 检测泛化性能达 SoTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated image (AIGI) attribution presents a pressing challenge that goes beyond mere AIGI detection, aiming to identify the source model or technique responsible for a synthetic image. However, most previous source attribution methods operate in a closed-set manner, which necessitates retraining to recognize any novel category, preventing adaptation to the rapid evolution of image generation. In this work, we propose a new paradigm for synthetic image attribution, termed few-shot attribution. This paradigm targets the reliable identification of unseen generators using only limited samples, making it highly suitable for real-world applications. To facilitate this work, we construct OmniFake, a large-scale, well-categorized synthetic image dataset that contains $1.17$ million images from $45$ distinct generators. We further introduce OmniDFA (Omni Detector and Few-shot Attributor), a few-shot attribution baseline that not only assesses the authenticity of images but also determines their synthesis origins. Experiments demonstrate that OmniDFA exhibits excellent capability in few-shot attribution and achieves state-of-the-art generalization performance in AIGI detection. Our dataset and code are available at https://github.com/teheperinko541/OmniDFA.

</details>

### 54. R2M: Real-Aware Residual Model Merging for Robust and Generalizable Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2509.24367) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5164)　📅 2025-09　🏷 ECCV 2026

**关键词**：`detection`、`deepfake`、`model merging`、`deepfake detection`、`cross-generator generalization`

👤 **作者**：Jinhee Park、Guisik Kim、Choongsang Cho、Junseok Kwon

- 🎯 **研究动机**：深伪生成器快速演化使穷举数据收集与反复重训练不可行
- 🔬 **研究方法**：提出免训练参数空间合并 R2M：低秩分解任务向量估计共享 Real 成分，分解 Fake 残差并以层级秩截断去噪，按任务范数匹配聚合
- 📌 **结论**：域内、跨数据集与未见数据集上均超联合训练与合并基线；新伪造家族出现时只需微调一个专家再合并

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake generators evolve quickly, making exhaustive data collection and repeated retraining impractical. We argue that model merging is a natural fit for deepfake detection: unlike generic multi-task settings with disjoint labels, deepfake specialists share the same binary decision and differ in generator-specific artifacts. Empirically, we show that simple weight averaging preserves Real representations while attenuating Fake-specific cues. Building upon these findings, we propose Real-aware Residual Model Merging (R$^2$M), a training-free parameter-space merging framework. R$^2$M estimates a shared Real component via a low-rank factorization of task vectors, decomposes each specialist into a Real-aligned part and a Fake residual, denoises residuals with layerwise rank truncation, and aggregates them with per-task norm matching to prevent any single generator from dominating. A concise rationale explains why a simple head suffices: the Real component induces a common separation direction in feature space, while truncated residuals contribute only minor off-axis variations. Across in-distribution, cross-dataset, and unseen-dataset, R$^2$M outperforms joint training and other merging baselines. Importantly, R$^2$M is also composable: when a new forgery family appears, we fine-tune one specialist and re-merge, eliminating the need for retraining.

</details>

### 55. Agent4FaceForgery: Multi-Agent LLM Framework for Realistic Face Forgery Detection

📄 [arXiv](https://arxiv.org/abs/2509.12546) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_Agent4FaceForgery_Multi-Agent_LLM_Framework_for_Realistic_Face_Forgery_Detection_CVPR_2026_paper.html)　📅 2025-09　🏷 CVPR 2026

**关键词**：`detection`、`face forgery`、`multi-agent reasoning`、`forensic evidence`

👤 **作者**：Yingxin Lai、Zitong Yu、Jun Wang、Linlin Shen、Yong Xu、Xiaochun Cao

- 🎯 **研究动机**：人脸伪造检测训练数据生态效度低，离线基准与真实效果差距大
- 🔬 **研究方法**：提出多 agent 框架：带画像与记忆模块的 LLM agent 在模拟社交环境中生成伪造过程与细微图文一致性标注，自适应拒绝采样保证数据质量
- 📌 **结论**：仿真驱动数据使多种架构的检测器获得显著性能增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Face forgery detection faces a critical challenge: a persistent gap between offline benchmarks and real-world efficacy,which we attribute to the ecological invalidity of training data.This work introduces Agent4FaceForgery to address two fundamental problems: (1) how to capture the diverse intents and iterative processes of human forgery creation, and (2) how to model the complex, often adversarial, text-image interactions that accompany forgeries in social media. To solve this,we propose a multi-agent framework where LLM-poweredagents, equipped with profile and memory modules, simulate the forgery creation process. Crucially, these agents interact in a simulated social environment to generate samples labeled for nuanced text-image consistency, moving beyond simple binary classification. An Adaptive Rejection Sampling (ARS) mechanism ensures data quality and diversity. Extensive experiments validate that the data generated by our simulationdriven approach brings significant performance gains to detectors of multiple architectures, fully demonstrating the effectiveness and value of our framework.

</details>

### 56. DF-MoE: Generalizable Deepfake Detection via Multimodal Sparse Mixture-of-Experts

📄 [arXiv](https://arxiv.org/abs/2608.23363) · 🌐 [Project](https://bmvc2026.bmva.org/programme/accepted_papers/)　📅 2026-08

**关键词**：`detection`、`audio-visual deepfake`、`high-level forensic cue`、`cross-domain generalization`、`AI-generated video`、`audio-visual cue`

👤 **作者**：Vlad Hondru、Florinel Alin Croitoru、Iuliana Georgescu、A. Sophia Koepke、Radu Tudor Ionescu

- 🎯 **研究动机**：音视频 deepfake 检测器易过拟合特定生成器伪影，跨生成方法泛化是主要挑战
- 🔬 **研究方法**：DF-MoE 用多种预训练模型提取高层线索（嘴部动作、人脸解析、表情、头姿、视线、心率、音频情绪、语音活动），经 Mixture-of-Experts 骨干整合单模态与多模态证据
- 📌 **结论**：在 MAVOS-DD、AVLips、PolyGlotFake、BioDeepAV、FakeAVCeleb 五个 benchmark 的域内与跨域实验中全面超过 SoTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-visual deepfake detection is an actively studied topic, where one of the main challenges is to develop detectors able to generalize across deepfake generation methods. We conjecture that overfitting can be mitigated by extracting multiple high-level cues from the available audio and visual modalities via pre-trained models. We therefore assemble a wide variety of pre-trained models to extract features that encode mouth movements, face parsing, facial expressions, head pose, gaze tracking, heart rate, audio emotion and speech activity. We further integrate both unimodal and multimodal cues via a Mixture-of-Experts (MoE) backbone to detect deepfakes. We perform in-domain and cross-domain experiments on five benchmarks for deepfake detection (MAVOS-DD, AVLips, PolyGlotFake, BioDeepAV, FakeAVCeleb) to compare our framework (DF-MoE) with state-of-the-art methods. Our results indicate that DF-MoE obtains superior deepfake detection results, surpassing all competing methods. We release our code at https://github.com/vladhondru25/DF-MoE.

</details>

### 57. SPLIT: Training-Free AI-Generated and Partially Edited Video Detection via Spatial Patch‑Level Incoherence and Temporal Roughness

📄 [arXiv](https://arxiv.org/abs/2607.02886) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5677)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated video detection`、`AI-generated content`、`deepfake detection`、`local manipulation`、`low false-positive rate`

👤 **作者**：Jongyeop Hyun、Hyounghun Kim

- 🎯 **研究动机**：AI 视频检测器部署需要真实视频上超低误报率，AUROC 等标准指标不反映该工作点的实际行为
- 🔬 **研究方法**：提出免训练 SPLIT：基于冻结视觉编码器 patch token 计算两步时间粗糙度与局部空间运动非相干性，乘性融合+gamma 校准锐化分离；提出 FPR=0.1% 固定下的 Fake Recall 服务对齐评估协议
- 📌 **结论**：三个基准上 FPR=0.1% 处 Fake Recall 最高，大幅超过监督与免训练基线且对后处理鲁棒、开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying AI-generated video detectors in real-world services demands an ultra-low false positive rate (FPR) on real videos to avoid falsely rejecting authentic content, a regime where standard metrics such as AUROC fail to reflect actual operating behavior. We introduce Spatial Patch-Level Incoherence and Temporal Roughness (SPLIT), a training-free detector that operates on patch tokens from a frozen vision encoder to detect both fully generated and partially edited videos. SPLIT computes two complementary signals: Two-step Temporal Roughness (TTR), capturing non-smooth patch trajectories via one-step and two-step feature variation contrast, and Local Spatial Motion Incoherence (LSMI), measuring spatially inconsistent temporal changes through gradients of a feature-space motion field. The two are fused multiplicatively with gamma correction to sharpen real-fake separation at strict thresholds. We further propose a service-aligned evaluation protocol based on Fake Recall at fixed FPR with real-only threshold calibration and cross-real threshold transfer. Across three benchmarks (FakeParts, GenVideo, and ViF-Bench), SPLIT achieves the highest Fake Recall at FPR = $0.1\%$, substantially outperforming supervised and training-free baselines while remaining robust to post-processing with negligible overhead. The code is publicly available at https://github.com/mldljyh/SPLIT .

</details>

### 58. MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization

📄 [arXiv](https://arxiv.org/abs/2607.00902) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4624)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`temporal forgery`、`deepfake detection`、`media forensics`、`tamper localization`、`linear model`

👤 **作者**：Jingchen Ni、…、Chun Yuan

- 🎯 **研究动机**：时序伪造定位受限于 CNN 局部感受野或 Transformer 二次复杂度，线性模型难以兼顾全局压缩与局部突变感知
- 🔬 **研究方法**：提出 MG-RWKV：O(T) 复杂度的双向 RWKV、按伪造时长动态路由粒度的 MG-MoE、对齐相邻特征金字塔的跨粒度一致性
- 📌 **结论**：Lav-DF、TVIL、Psynd 上 SOTA 且计算成本低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Driven by Artificial Intelligence-Generated Content (AIGC), the authenticity of audio-visual content is facing severe challenges. Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within untrimmed sequences. However, existing methods are limited by CNNs' local receptive fields or Transformers' quadratic complexity, while emerging linear models often struggle to balance global authentic context compression with local abrupt forgery perception. To address this, we propose MG-RWKV, a multi-granularity framework that leverages the data-dependent state evolution of RWKV to achieve efficient full-sequence processing with O(T) complexity. Our framework features three core innovations: (1) a Bidirectional RWKV architecture that captures bidirectional temporal contexts without quadratic overhead; (2) a Multi-Granularity Mixture of Experts (MG-MoE) that performs dynamic routing over explicit temporal receptive fields, adaptively selecting granularities based on forgery duration to significantly enhance decision interpretability; and (3) Cross-Granularity Consistency (CGC), which aligns adjacent feature pyramid levels through hierarchical scale-wise pairing and spatial boundary-aware weighting, effectively reducing false positives in authentic regions. Extensive experiments on Lav-DF, TVIL, and Psynd datasets demonstrate that MG-RWKV achieves state-of-the-art performance with low computational cost.

</details>

### 59. Unleashing Vision-Language Semantics for Deepfake Video Detection

📄 [arXiv](https://arxiv.org/abs/2603.24454) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Unleashing_Vision-Language_Semantics_for_Deepfake_Video_Detection_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`deepfake video`、`vision-language semantics`、`cross-manipulation transfer`

👤 **作者**：Jiawen Zhu、Yunqi Miao、Xueyi Zhang、Jiankang Deng、Guansong Pang

- 🎯 **研究动机**：现有检测只用 CLIP 视觉特征，忽略其潜空间中最独特的视觉-语言语义
- 🔬 **研究方法**：ForgePerceiver 独立学习细粒度与整体伪造线索并保留预训练对齐知识；身份感知 VLA 分数耦合跨模态语义与伪造线索，并用身份先验文本提示增强
- 📌 **结论**：在经典换脸与最新全脸生成伪造基准上，帧级与视频级均大幅超越 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent Deepfake Video Detection (DFD) studies have demonstrated that pre-trained Vision-Language Models (VLMs) such as CLIP exhibit strong generalization capabilities in detecting artifacts across different identities. However, existing approaches focus on leveraging visual features only, overlooking their most distinctive strength -- the rich vision-language semantics embedded in the latent space. We propose VLAForge, a novel DFD framework that unleashes the potential of such cross-modal semantics to enhance model's discriminability in deepfake detection. This work i) enhances the visual perception of VLM through a ForgePerceiver, which acts as an independent learner to capture diverse, subtle forgery cues both granularly and holistically, while preserving the pretrained Vision-Language Alignment (VLA) knowledge, and ii) provides a complementary discriminative cue -- Identity-Aware VLA score, derived by coupling cross-modal semantics with the forgery cues learned by ForgePerceiver. Notably, the VLA score is augmented by an identity prior-informed text prompting to capture authenticity cues tailored to each identity, thereby enabling more discriminative cross-modal semantics. Comprehensive experiments on video DFD benchmarks, including classical face-swapping forgeries and recent full-face generation forgeries, demonstrate that our VLAForge substantially outperforms state-of-the-art methods at both frame and video levels. Code is available at https://github.com/mala-lab/VLAForge.

</details>

### 60. X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2603.08483) · 🌐 [Project](https://youngseo0526.github.io/X-AVDT/) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_X-AVDT_Audio-Visual_Cross-Attention_for_Robust_Deepfake_Detection_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`audio-visual deepfake`、`cross-attention`、`modality robustness`

👤 **作者**：Youngseo Kim、Kwan Yun、Seokhyeon Hong、Sihun Cha、Colette Suhjung Koo、Junyong Noh

- 🎯 **研究动机**：生成器内部跨注意力编码细粒度语音-动作对齐，这一伪造检测线索未被利用
- 🔬 **研究方法**：X-AVDT 经 DDIM 反演探取生成器内部信号，提取反演差异与音视频跨注意力特征；并发布覆盖 GAN、扩散与流匹配的 MMDF 数据集
- 📌 **结论**：在 MMDF 领先并强泛化到外部基准与未见生成器，准确率提升 13.1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The surge of highly realistic synthetic videos produced by contemporary generative systems has significantly increased the risk of malicious use, challenging both humans and existing detectors. Against this backdrop, we take a generator-side view and observe that internal cross-attention mechanisms in these models encode fine-grained speech-motion alignment, offering useful correspondence cues for forgery detection. Building on this insight, we propose X-AVDT, a robust and generalizable deepfake detector that probes generator-internal audio-visual signals accessed via DDIM inversion to expose these cues. X-AVDT extracts two complementary signals: (i) a video composite capturing inversion-induced discrepancies, and (ii) an audio-visual cross-attention feature reflecting modality alignment enforced during generation. To enable faithful cross-generator evaluation, we further introduce MMDF, a new multimodal deepfake dataset spanning diverse manipulation types and rapidly evolving synthesis paradigms, including GANs, diffusion, and flow-matching. Extensive experiments demonstrate that X-AVDT achieves leading performance on MMDF and generalizes strongly to external benchmarks and unseen generators, outperforming existing methods with accuracy improved by 13.1%. Our findings highlight the importance of leveraging internal audio-visual consistency cues for robustness to future generators in deepfake detection.

</details>

### 61. Preserving Knowledge across Space and Time for Continual Video Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2609.03446) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4132)　📅 2026　🏷 ECCV 2026

**关键词**：`detection`、`deepfake`、`deepfake detection`、`media forensics`、`continual learning`、`catastrophic forgetting`

👤 **作者**：Taehoon Kim、Jongwook Choi、Heejae Jo、Byungmin Park、Jongwon Choi

- 🎯 **研究动机**：视频深伪在空间与时间两轴留证据，面向图像的方法无法捕捉视频特有线索，序列更新需分别保留各模态
- 🔬 **研究方法**：MSFD 在频域把视频特征解耦为空间、时间与时空模态独立保留，并用跨模态去相关损失使时空表示与单模态线索正交
- 📌 **结论**：多样持续深伪视频场景下适应与性能保持均超 SOTA

### 62. Explainable Forensics of Manipulated Segments in Untrimmed Long Videos

📄 [arXiv](https://arxiv.org/abs/2606.02402) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65002)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`deepfake detection`、`media forensics`、`open-world generalization`、`empirical evaluation`、`cross-generator generalization`

👤 **作者**：Yue Feng、…、Jie Qin

- 🎯 **研究动机**：现有视频取证只处理短独立片段，无法覆盖 AI 内容稀疏嵌入真实长视频的现实场景
- 🔬 **研究方法**：形式化时序 AI 生成片段定位与解释任务；TASLE 含 12,472 条未剪辑视频与时间边界、真实性及片段级理由标注；MSLoc 基线用边界敏感提议生成加 MLLM 精炼定位
- 📌 **结论**：验证基线有效，凸显片段级可解释取证对长视频分析的重要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of AI-driven video generation has transformed content creation, while simultaneously increasing the risk of misinformation through localized manipulations in long-form videos. Existing video forensic methods predominantly operate on short, independent clips, and thus fail to capture realistic scenarios where AI-generated content is sparsely embedded within otherwise authentic footage. To bridge this gap, we formulate the task of Temporal AI-Generated Segment Localization and Explanation, which targets authenticity detection, temporal localization, and interpretable analysis of manipulated segments in untrimmed long videos. We further introduce TASLE, a large-scale benchmark comprising 12,472 untrimmed videos with diverse manipulation patterns and rich annotation signals, including temporal boundaries, authenticity labels, and segment-level rationales. In addition, we propose MSLoc, a coarse-to-fine forensic baseline that combines a boundary-sensitive proposal generation module for efficient long-video scanning with an MLLM-based refinement module for precise boundary localization and interpretable reasoning. Experiments validate the effectiveness of the proposed baseline, highlighting the importance of segment-level explainable forensics for long-form AI-generated video analysis. Dataset and code will be made publicly available.

</details>

### 63. Expose Your Disguise: Recovering Source Speaker Identity From Voice Conversion

📄 [arXiv](https://arxiv.org/abs/2607.23650) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-07　🏷 ACM CCS 2026

**关键词**：`detection`、`voice conversion`、`privacy leakage`、`memorization`、`source speaker attribution`、`audio forensics`

👤 **作者**：Hanlei Zhang、Zhongming Ma、Mingyang Zhang、Tengfei Liu、Yushi Cheng、Yanjiao Chen

- 🎯 **研究动机**：语音转换对生物识别安全构成威胁，取证场景需从转换语音还原源说话人身份以缩小嫌疑范围
- 🔬 **研究方法**：提出 TRIDENT 三叉架构：主提取器加两个辅助分支——识别转换机制类型与提取目标说话人潜表示，借此解耦混淆因素蒸馏出高判别力的源说话人表示
- 📌 **结论**：对 7 个 SOTA 语音转换方法准确率高达 90.99%，电话信道、未见语言与自适应场景下保持鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Voice conversion (VC) poses a significant threat to biometric security by allowing attackers to impersonate target speakers. In forensic contexts, recovering the source speaker's identity from converted audio is vital for narrowing the field of suspects. To address this, we propose TRIDENT, a retracing framework designed to restore a source speaker's original identity from a converted audio sample. TRIDENT utilizes a three-pronged architecture consisting of a primary extractor and two auxiliary branches. The first auxiliary branch identifies the underlying voice conversion mechanism. This design acknowledges that even if the exact conversion strategy is unknown, a high-performance model adopted by the attacker is typically a derivative or variant of established mainstream ones. The second auxiliary branch extracts a latent representation of the target speaker, facilitating the isolation of target-specific traits from the composite converted audio sample. Finally, the main extractor leverages insights from both auxiliary branches to decouple confounding factors and distill a highly discriminative representation of the source speaker's identity. Experimental results demonstrate that TRIDENT achieves an accuracy as high as 90.99% against 7 state-of-the-art voice conversion methods. Furthermore, TRIDENT maintains robust performance under challenging conditions, including telephony channels, unseen languages, and adaptive scenarios.

</details>
