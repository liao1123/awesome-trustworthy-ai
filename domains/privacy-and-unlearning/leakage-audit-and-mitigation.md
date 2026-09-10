# 隐私攻击评测与泄漏缓解

[返回上级目录](README.md)

## 研究方向

研究如何通过明确攻击检验模型、表示、记忆与上下文是否泄漏数据，并针对 memory extraction、attribute inference、embedding/model inversion、训练样本记忆和身份恢复提出可验证缓解。一般 privacy-preserving learning/inference、data minimization、最小披露，以及 Differential Privacy、federated learning、密码学、secure computation、secure inference、homomorphic encryption、MPC、zero-knowledge proof、数字签名、区块链和 TEE 不属于本页范围；以 federated learning 为研究对象或训练框架的攻击与防御同样不收录。

## 研究脉络

- **泄漏审计：** behavioral canary、targeted query 与 prior-aware metric 用于区分训练记忆、上下文泄漏、统计常见生成和评测假阳性。
- **攻击驱动缓解：** memory extraction honeypot、记录级 vulnerability estimation 和局部模型干预需要以具体攻击成功率验证，而不只报告抽象 privacy–utility score。
- **反演与属性推断：** 噪声保护表示、模型特征和公开内容仍可能被重建或组合为敏感属性，研究重点是攻击能力、边界与定向防护。
- **多模态泄漏：** image、diffusion feature、face identity 与 location clue 的保护必须面对恢复、未经授权个性化或定位攻击。
- **当前边界：** 不验证具体泄漏 threat model 的一般隐私保护、最小披露、密码学、DP、FL 和 secure inference 路线不纳入。

## 训练与上下文泄漏审计

### 1. Inadvertent Context Leakage in Language Models

📄 [arXiv](https://arxiv.org/abs/2608.19857)　📅 2026-08

**关键词**：`attack`、`analysis`、`private agent context`、`memory predicate inference`、`adaptive extraction`、`linguistic steganography`

👤 **作者**：Jaiden Fairoze、Neal Mangaokar、Kamalika Chaudhuri、Sanjam Garg、Saeed Mahloujifar

- 🎯 **研究动机**：agent 上下文中的敏感秘密（日历、凭据、健康、金融）是否在良性输出中留下可重建的隐藏相关性未知
- 🔬 **研究方法**：研究被动泄漏与主动放大两种情形，用黑盒自适应攻击（含语义谓词分类器与 RL 训练对手）利用该有限泄漏
- 📌 **结论**：八个专有模型上 2 位上下文秘密近完美重建、4 位达 82% 精确匹配（全部来自普通非对抗请求）；更强模型泄漏更多——RL 对手可从生产式 agent 提取完整社会安全号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>

### 2. Behavioral Canaries: Auditing Private Retrieved Context Usage in RL Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2604.22191) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`detection`、`private-context misuse`、`behavioral canary`、`training audit`、`private context`、`RLFT audit`

👤 **作者**：Chaoran Chen、Dayu Yuan、Peter Kairouz

- 🎯 **研究动机**：RL 微调主要改变行为风格而非事实记忆，verbatim 记忆与成员推断审计无法检测违规使用受保护检索上下文训练
- 🔬 **研究方法**：Behavioral Canaries 在偏好数据中植入文档触发器并奖励独特风格反馈，若被用于训练即诱导出触发条件偏好
- 📌 **结论**：1% 注入率下 10% FPR 时检测率 67%（AUROC 0.756），确立行为金丝雀这一 RLFT 审计机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In agentic workflows, LLMs frequently process retrieved contexts that are legally protected from further training. However, auditors currently lack a reliable way to verify if a provider has violated the terms of service by incorporating these data into post-training, especially through Reinforcement Learning (RL). While standard auditing relies on verbatim memorization and membership inference, these methods are ineffective for RL-trained models, as RL primarily influences a model's behavioral style rather than the retention of specific facts. To bridge this gap, we introduce Behavioral Canaries, a new auditing mechanism for RLFT pipelines. The framework instruments preference data by pairing document triggers with feedback that rewards a distinctive stylistic response, inducing a latent trigger-conditioned preference if such data are used in training. Empirical results show that these behavioral signals enable detection of unauthorized document-conditioned training, achieving a 67% detection rate at a 10% false-positive rate (AUROC = 0.756) at a 1% canary injection rate. More broadly, our results establish behavioral canaries as a new auditing mechanism for RLFT pipelines, enabling auditors to test for training-time influence even when such influence manifests as distributional behavioral change rather than memorization. We release our code at: https://github.com/CRChenCode/behavioral_canary.

</details>

### 3. *MemPot*: Defend Against Memory Extraction Attack with Optimized Honeypots

🌐 [Project](https://wangyuhao06.github.io/mempot-website/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62415)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`attack`、`memory extraction`、`optimized honeypot`、`leakage mitigation`、`privacy attack`

👤 **作者**：Yuhao Wang、Shengfang ZHAI、Guanghao Jin、Yinpeng Dong、Linyi Yang、Jiaheng Zhang

- 🎯 **研究动机**：LLM 智能体记忆系统面临严重抽取攻击而防御缺失
- 🔬 **研究方法**：MemPot 两阶段优化生成对攻击者检索概率最大且对良性用户不显眼的蜜罐文档，检测建模为 Wald SPRT，理论证明平均采样轮次低于最优静态检测器
- 📌 **结论**：检测 AUROC 提升 50%，低 FPR 约束下 TPR 增 80%，零在线延迟且不损效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM)-based agents employ external and internal memory systems to handle complex, goal-oriented tasks, yet this exposes them to severe extraction attacks, and corresponding defenses are currently lacking. In this paper, we propose MemPot, the first theoretically verified defense framework against memory extraction attacks by injecting optimized honeypots into the memory. Through a two-stage optimization process, MemPot generates trap documents that maximize the retrieval probability for attackers while remaining inconspicuous to benign users. We model the detection process as Wald’s Sequential Probability Ratio Test (SPRT) and theoretically prove that MemPot achieves a lower average number of sampling rounds compared to optimal static detectors. Empirically, MemPot significantly outperforms state-of-the-art baselines, achieving a 50% improvement in detection AUROC and an 80% increase in True Positive Rate under low False Positive Rate constraints. Furthermore, our experiments confirm that MemPot incurs zero online inference latency and preserves the agent's utility on standard tasks, verifying its superiority in safety, harmlessness and efficiency.

</details>

### 4. ContextLeak: Auditing Leakage in Private In-Context Learning Methods

📄 [arXiv](https://arxiv.org/abs/2512.16059) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-12

**关键词**：`detection`、`private ICL`、`canary audit`、`context leakage`、`canary insertion`、`worst-case leakage`

👤 **作者**：Jacob Choi、…、Sai Praneeth Karimireddy

- 🎯 **研究动机**：私有 ICL 防御方法众多，却缺乏度量其最坏情况信息泄漏的审计手段
- 🔬 **研究方法**：ContextLeak 用 canary 插入：在敏感数据嵌入可唯一识别 token 并构造定向查询检测其是否出现，覆盖启发式 prompt 防御与带形式保证的差分隐私方法
- 📌 **结论**：可跨方法可靠检出泄漏且泄漏随理论隐私预算单调增加；现有方法隐私-效用权衡差，要么完全泄漏要么严重损害性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In-Context Learning (ICL) has become a standard technique for adapting Large Language Models (LLMs) to specialized tasks by supplying task-specific exemplars within the prompt. However, when these exemplars contain sensitive information, reliable privacy-preserving mechanisms are essential to prevent unintended leakage through model outputs. Many privacy-preserving methods have been proposed to protect against information leakage in this context, but there are fewer efforts on how to audit these methods. We introduce ContextLeak, the first framework to empirically measure the worst-case information leakage in ICL. ContextLeak uses canary insertion, embedding uniquely identifiable tokens in the sensitive dataset and crafting targeted queries to detect their presence. We apply ContextLeak across a range of private ICL techniques, including both heuristic prompt-based defenses and differentially private methods with formal guarantees. We show that ContextLeak reliably detects leakage across methods, and the leakage increases monotonically with the theoretical privacy budget, offering a practical signal of worst-case privacy risk. Our analysis further reveals that existing methods strike poor privacy-utility trade-offs, either completely leaking sensitive information or severely degrading performance.

</details>

### 5. Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings

📄 [arXiv](https://arxiv.org/abs/2608.18610)　📅 2026-08

**关键词**：`attack`、`noise-protected embedding`、`unsupervised denoising`、`text reconstruction`、`noise-aware inversion`、`Double Noise Trap`

👤 **作者**：Yubo Wang、…、Weiqing Wang

- 🎯 **研究动机**：高斯加噪被视为对抗嵌入反演的简单有效防御，对显式考虑扰动过程的自适应攻击者是否安全未知
- 🔬 **研究方法**：识别双噪声陷阱并提 DAEI：残差去噪自编码器（以 Stein 无偏风险估计免监督训练）串联生成式文本反演
- 📌 **结论**：BLEU 相对现有生成式反演基线提升约 154%，token F1 与 ROUGE-L 提升 32-60%——简单高斯扰动不足以阻止嵌入泄露敏感信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dense text embeddings are widely used in data mining, retrieval, and downstream machine learning systems due to their compact and semantically rich representations, but recent embedding inversion attacks have shown that they can expose substantial information about the original text, leading to serious privacy leakage risks. A common defense is to release perturbed embeddings by adding Gaussian noise, which is simple yet effective against standard inversion attacks and does not significantly degrade embedding utility for downstream tasks. However, it remains unclear whether such noise-protected embeddings are sufficiently safe against adaptive attackers that explicitly account for the perturbation process. In this paper, we study text embedding inversion in a noise-protected setting, where the attacker can observe only noisy embeddings and has no access to clean embedding targets. We first analyze why existing generative inversion methods fail under this setting and identify a "Double Noise Trap", which fundamentally prevents standard generative inversion models from achieving high-quality reconstruction. To address this challenge, we propose DAEI, a denoising-aware embedding inversion pipeline that combines a residual denoising autoencoder with generative text inversion where the denoiser is trained in an unsupervised manner using Stein's unbiased risk estimate to enable denoising from noisy observations alone. Extensive experiments show that DAEI achieves approximately 154\% relative improvement in BLEU over the existing generative inversion baseline, while also improving token-level F1 and ROUGE-L by 32--60\%. The promising inversion performance of DAEI challenges the prevailing assumption that simple Gaussian perturbation is sufficient to prevent sensitive information leakage from embedding representations.

</details>

### 6. Black-Box Embedding Inversion Attack on Vector Databases

🌐 [Project](https://doi.org/10.1145/3770855.3817917)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`embedding inversion`、`vector database`、`black-box reconstruction`、`stored-content extraction`、`vector-database leakage`

- 🎯 **研究动机**：向量数据库的embedding被默认安全，黑盒内容还原能力未评估
- 🔬 **研究方法**：对向量数据库发起黑盒embedding inversion攻击重建存储内容
- 📌 **结论**：仅凭查询接口即可高精度重建原文，向量库存在实质泄漏

### 7. AccretionLink: On-Device Auditing of Exposure-Control Attacks on Attribute Inference

📄 [arXiv](https://arxiv.org/abs/2608.14735)　📅 2026-08

**关键词**：`detection`、`attribute inference`、`exposure-control attack`、`on-device audit`

👤 **作者**：Faruk Alpay、Taylan Alpay

- 🎯 **研究动机**：曝光控制攻击通过对公开帖排序强化私有属性推断而不改内容，缺设备端审计方法
- 🔬 **研究方法**：AccretionLink 定义机密性与完整性博弈，用部分识别建模有界选择几率并构造依赖感知的时间一致 e-process，在 Pixel 10 上以 P-256 签名与 StrongBox 密钥落地
- 📌 **结论**：52 个保留合成画像上四倍选择几率在 8 帖时带来 0.01595 nats 推断优势（三个效应过 Holm 校正）；142 个 PAN15 画像上探索性选择也有 0.01227 nats 优势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Exposure control lets an adversary rank authentic public posts to strengthen private-attribute inference without altering content. AccretionLink defines confidentiality and integrity games for this attack, models bounded selection odds through partial identification, and constructs dependence-aware time-uniform e-processes. On 52 held-out synthetic profiles, odds-four selection reduced aggregate negative log likelihood at every horizon. At eight posts the advantage was 0.01595 nats (95% CI [0.00890, 0.02336]), three of four target effects survived Holm adjustment, and label-blind model-guided selection caused 6/109 high-confidence false reversals. On 142 PAN15 test profiles, exploratory selection produced a 0.01227-nat advantage but no reversal. A separate TF-IDF selector retained a 0.01470-nat advantage against the unchanged G5 target, while matched identity shuffling did not reproduce it. Pixel 10 encoded all 1,622 held-out posts once with a fallback-free Tensor G5 graph. A P-256 checkpoint authenticated the selected-replay, actual-model, native-report, and operation digests; local KeyInfo identified the signing key as StrongBox-backed.

</details>

### 8. Secrets Everywhere: Auditing Memorization in Mobility Prediction Models

📄 [arXiv](https://arxiv.org/abs/2608.02052) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-08　🏷 ACM CCS 2026

**关键词**：`detection`、`analysis`、`mobility memorization`、`trajectory leakage`、`data extraction`、`mobility prediction`

👤 **作者**：Anne Josiane Kouam、Hristo Boyadzhiev、Konrad Rieck

- 🎯 **研究动机**：人类移动预测模型是否记忆并暴露训练集中的敏感轨迹缺乏系统审计，且轨迹多尺度结构使既有记忆度量不适配
- 🔬 **研究方法**：提出个体位置、锚点对、子轨迹段多粒度记忆量化框架与用户锚定参考集，跨多模型多数据集测量记忆偏好
- 📌 **结论**：发现普遍的记忆模式且与用户行为规律性相关，提升推理期数据提取风险，呼吁对移动预测模型强制隐私审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human mobility prediction models, which forecast the next location in a user's trajectory, are increasingly deployed in urban analytics, navigation, and personalized services. Yet, little is known about their potential to memorize and expose sensitive user trajectories from training data. While memorization has been extensively studied in language models, mobility prediction poses unique challenges: training sequences encode human behavior at various spatial and temporal scales, creating privacy risks at different granularities. In this paper, we conduct the first systematic audit of memorization in mobility prediction models. While prior work has shown that privacy leaks can arise from such models, we systematically assess and quantify memorization risks at scale. We identify key challenges, including the lack of a randomness space, the multi-scale structure of trajectories, and user-specific behavioral diversity. To address these challenges, we introduce a framework to quantify mobility memorization at different levels of granularity: individual locations, anchor pairs, and subtrajectory segments. We also develop user-grounded reference sets to assess how likely a model is to prefer training data over realistic alternatives. Our evaluation across multiple models and datasets reveals pervasive memorization patterns that correlate with user regularity and increase the risk of data extraction at inference time. Our findings call for mandatory privacy auditing in mobility prediction models.

</details>

### 9. A Prior-Aware Metric for Efficiently Distinguishing Memorization from Generalization in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.18733) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-02

**关键词**：`detection`、`memorization audit`、`prior correction`、`false positive`、`training-data memorization`、`prior-aware metric`

👤 **作者**：Trishita Tiwari、Ari Trachtenberg、G. Edward Suh

- 🎯 **研究动机**：现有记忆化度量把前缀特定记忆与统计常见序列混为一谈，反事实度量又需重训多模型而不可行
- 🔬 **研究方法**：提出 Prior-Aware memorization 免训练准则：判断候选后缀是强关联特定训练前缀，还是在 IID 采样中因统计常见性高概率出现
- 📌 **结论**：LLaMA 与 OPT 训练语料上，55%-90% 原判为记忆化的序列实为统计常见性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training data leakage from Large Language Models (LLMs) raises serious concerns related to privacy, security, and copyright compliance. A central challenge in assessing this risk is distinguishing prefix-specific memorization of training data from the generation of statistically common sequences. Existing approaches to measuring memorization often conflate these phenomena, labeling outputs as memorized even when they arise from generalization over common patterns. Counterfactual memorization and other related metrics \citep{zhang2023counterfactual, wang2025generalization, lesci2024causal} provide principled solutions, however, their reliance on retraining multiple baseline models or parsing through the training data makes them computationally impractical at scale. This work introduces \emph{Prior-Aware memorization}, a theoretically grounded, lightweight and training-free criterion for identifying prefix-specific memorization in LLMs. The key idea is to evaluate whether a candidate suffix is strongly associated with its specific training prefix or whether it appears with high probability across many IID sampled sequences from the training data distribution due to statistical commonality. We correlate our metric with counterfactual memorization, and also evaluate it on the training corpora of two pre-trained models, LLaMA and OPT. Our results show that between 55\% and 90\% of sequences previously labeled as memorized fail our criterion and are consistent with statistical commonality

</details>

### 10. Random Erasing vs. Model Inversion: A Promising Defense or a False Hope?

📄 [arXiv](https://arxiv.org/abs/2409.01062) · 🌐 [Project](https://ngoc-nguyen-0.github.io/MIDRE/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/68773)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`model inversion`、`random erasing`、`attack evaluation`、`privacy defense`、`empirical evaluation`

👤 **作者**：Viet-Hung Tran、…、Ngai-Man Cheung

- 🎯 **研究动机**：模型逆序（MI）攻击可重建私有训练数据，现有防御均为模型侧，数据侧对 MI 鲁棒性的影响未被探索
- 🔬 **研究方法**：将 Random Erasing（RE）用作数据侧防御：部分擦除阻止模型看到完整物体、随机擦除位置换取隐私-效用平衡，并在特征空间分析其机理
- 📌 **结论**：37 组实验中隐私-效用权衡达到 SOTA，在部分配置下首次做到攻击准确率显著下降而效用不降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model Inversion (MI) attacks pose a significant privacy threat by reconstructing private training data from machine learning models. While existing defenses primarily concentrate on model-centric approaches, the impact of data on MI robustness remains largely unexplored. In this work, we explore Random Erasing (RE)—a technique traditionally used for improving model generalization under occlusion—and uncover its surprising effectiveness as a defense against MI attacks. Specifically, our novel feature space analysis shows that model trained with RE-images introduces a significant discrepancy between the features of MI-reconstructed images and those of the private data. At the same time, features of private images remain distinct from other classes and well-separated from different classification regions. These effects collectively de x0002 grade MI reconstruction quality and attack accuracy while maintaining reasonable natural accuracy. Furthermore, we explore two critical properties of RE including Partial Erasure and Random Location. First, Partial Erasure prevents the model from observing entire objects during training, and we find that this has significant impact on MI, which aims to reconstruct the entire objects. Second, the Random Location of erasure plays a crucial role in achieving a strong privacy-utility trade-off. Our findings highlight RE as a simple yet effective defense mechanism that can be easily integrated with existing privacy-preserving techniques. Extensive experiments of 37 setups demonstrate that our method achieves SOTA performance in privacy-utility tradeoff. The results consistently demonstrate the superiority of our defense over existing defenses across different MI attacks, network architectures, and attack configurations. For the first time, we achieve significant degrade in attack accuracy without decrease in utility for some configurations. Our code and additional results are available at: https://ngoc-nguyen-0.github.io/MIDRE/

</details>

### 11. Provably Protecting Fine-Tuned LLMs from Training Data Extraction while Preserving Utility

📄 [arXiv](https://arxiv.org/abs/2602.00688) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61875)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`training-data extraction`、`provable protection`、`utility retention`、`privacy attack`、`empirical evaluation`

👤 **作者**：Tom Segal、Asaf Shabtai、Yuval Elovici

- 🎯 **研究动机**：防训练数据抽取的现有防御缺形式隐私保证或严重损效用
- 🔬 **研究方法**：观察到微调只需保留少量有影响力的 token 级概率偏移；SCP-Δr 基于 Near Access Freeness 在相对概率上用基模型显式平滑低影响 token
- 📌 **结论**：理论界比现有 NAF 方法好数个数量级，对 TDE 攻击强防护且性能损失极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on sensitive datasets raises privacy concerns, as training data extraction (TDE) attacks can expose highly confidential information. Existing defenses against such attacks either lack formal privacy guarantees or incur substantial utility degradation. We observe that fine-tuning induces widespread probability shifts, yet preserving only a small subset of influential token-level deviations is sufficient; the remaining shifts can be aggressively smoothed with minimal impact on utility. Motivated by this insight, we propose SCP-$\Delta_r$, a Near Access Freeness (NAF)-based algorithm that operates on relative probabilities and explicitly smooths low-impact tokens using a base model. SCP-$\Delta_r$ achieves orders-of-magnitude better theoretical bounds than existing NAF based methods and provides strong empirical protection against TDE attacks with minimal performance loss.

</details>

### 12. Can we estimate privacy vulnerability of individual records? Towards Mitigating Attribute Inference Attacks on ML Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kabir)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`defense`、`attribute inference`、`AttriVET`、`cyber misuse`、`record-level vulnerability`

👤 **作者**：Ehsanul Kabir、Najrin Sultana、Ninghui Li、Shagufta Mehnaz

- 🎯 **研究动机**：现有防御目标过宽，无法针对属性推断攻击提供细粒度、漏洞感知的保护
- 🔬 **研究方法**：NeighVE 从对手侧估计记录级泄露脆弱性；VESL 子空间学习防御；AttriVET 预测脆弱记录
- 📌 **结论**：记录级风险主要由数据集特征而非模型架构决定；AttriVET 跨场景超 90% 准确预测脆弱记录，VESL 以最小效用损失缓解泄露并顺带改善公平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) has brought transformative applications across various sectors, including sensitive fields like healthcare, finance, and customer analytics. However, ML models are susceptible to privacy leaks, especially through attribute inference and model inversion attacks, raising concerns for data confidentiality in privacy-critical domains. Existing defenses pursue much broader objectives than specifically preventing privacy leakage from attribute inference attacks, and as a result often fail to provide fine-grained, vulnerability-aware protection without significant utility costs. Motivated by this need, we first investigate record-level vulnerability estimation through NeighVE, an adversary-side tool designed to identify which individual records are more exposed to inference. Insights from NeighVE reveal that the record-level risk of privacy leakage is largely agnostic to model architectures and attack strategies and is instead governed by dataset-level characteristics, particularly the distribution of sensitive attributes in the local neighborhood of each record. Building on this insight, we propose VESL, a subspace-learning–inspired defense that mitigates attribute-inference leakage while keeping utility loss to a bare minimum. As a byproduct of its balancing mechanism, VESL also improves fairness across sensitive attributes and prevents NeighVE from reliably identifying vulnerable records. As a supporting contribution, we introduce AttriVET, an estimator that predicts which individual records are vulnerable with over 90% accuracy across diverse scenarios, enabling risk-aware defense design and auditing.

</details>

### 13. You Don’t Need All That Attention: Surgical Memorization Mitigation in Text-to-Image Diffusion Models

🎓 [Official](https://icml.cc/virtual/2026/poster/65409)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion memorization`、`attention mitigation`、`training-data leakage`、`privacy attack`、`diffusion model`

👤 **作者**：Kairan Zhao、Eleni Triantafillou、Peter Triantafillou

- 🎯 **研究动机**：文生图扩散模型会逐字复现训练图像，带来隐私与版权风险
- 🔬 **研究方法**：GUARD以吸引-排斥动力学引导去噪偏离训练图，并衰减特定prompt位置的cross-attention
- 📌 **结论**：两种架构的verbatim与模板记忆缓解均持续SOTA，图像质量不降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative models have been shown to "memorize" certain training data, leading to verbatim or near-verbatim generating images, which may cause privacy concerns or copyright infringement. We introduce Guidance Using Attractive-Repulsive Dynamics (GUARD), a novel framework for memorization mitigation in text-to-image diffusion models. GUARD adjusts the image denoising process to guide the generation away from an original training image and towards one that is distinct from training data while remaining aligned with the prompt, guarding against reproducing training data, without hurting image generation quality. We propose a concrete instantiation of this framework, where the positive target that we steer towards is given by a novel method for (cross) attention attenuation based on (i) a novel statistical mechanism that automatically identifies the prompt positions where cross attention must be attenuated and (ii) attenuating cross-attention in these per-prompt locations. The resulting GUARD offers a surgical, dynamic per-prompt inference-time approach that, we find, is by far the most robust method in terms of consistently producing state-of-the-art results for memorization mitigation across two architectures and for both verbatim and template memorization, while also improving upon or yielding comparable results in terms of image quality.

</details>

### 14. Vulnerability of Privacy-Preserving Visual Localization against Diffusion-based Attacks

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4261) · 📝 [OpenReview](https://openreview.net/forum?id=NmWf0gLufZ)　📅 2026　🏷 ECCV 2026

**关键词**：`detection`、`attack`、`visual localization`、`privacy attack`、`cyber misuse`、`diffusion inversion`

- 🎯 **研究动机**：隐私保护视觉定位对扩散式攻击的脆弱性未知
- 🔬 **研究方法**：以扩散逆变换重构场景图像攻破定位隐私保护
- 📌 **结论**：现有保护在diffusion-based攻击下失效

### 15. Protecting Facial Biometrics from Malicious Generative Editing via Latent Optimization

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`facial biometrics`、`malicious editing`、`latent optimization`

- 🎯 **研究动机**：生成式编辑可恶意篡改面部生物特征
- 🔬 **研究方法**：经latent优化向图像嵌入保护扰动以破坏恶意编辑
- 📌 **结论**：视觉质量基本保持下阻断生成式篡改

### 16. IdentityMask: A Robust Face-Centric Privacy Protection Against Unauthorized Personalization of Diffusion Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3488.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`face privacy`、`unauthorized personalization`、`feature corruption`

- 🎯 **研究动机**：现有扰动防御忽略个性化过程的时空动态，扰动低效且未破坏核心身份编码机制
- 🔬 **研究方法**：IdentityMask 把扰动锚定在主体特定语义并优先关键扩散时间步，用流形投影把对抗信号嵌入图像内在结构以抗净化
- 📌 **结论**：多数据集、个性化技术与防御设定下保护效果与鲁棒性均超先前 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unauthorized personalization based on diffusion models pose a severe and growing threat to digital privacy by enabling the unauthorized replication and exploitation of individual identities. Existing disrupting-based defenses primarily add invisible perturbations arbitrarily across the entire image space to disrupt the generation process. However, we reveal that these methods fundamentally overlook the spatio-temporal dynamics of the personalization process, resulting in inefficient optimization that fails to sufficiently disrupt the core identity encoding mechanism. To mitigate these limitations, we propose IdentityMask, a robust protection framework that shifts the paradigm from arbitrary confusion to precise, targeted feature corruption. By anchoring the perturbation on subjectspecific semantics and prioritizing the most critical diffusion timesteps, our framework ensures the disruption is maximized precisely where the identity is encoded. Additionally, a novel manifold projection strategy is introduced to embed the adversarial signals into the intrinsic structure of the image, rendering the protection resilient against state-of-the-art purification. Extensive experiments across diverse datasets, personalization techniques, and defense settings demonstrate that IdentityMask consistently outperforms prior state-of-the-art approaches in both protection efficacy and robustness.

</details>

### 17. GEO-Detective: Unveiling Location Privacy Risks in Images with LLM Agents

📄 [arXiv](https://arxiv.org/abs/2511.22441) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5191)　📅 2025-11　🏷 ECCV 2026

**关键词**：`attack`、`analysis`、`location inference`、`LLM agent`、`image privacy`、`location privacy`

👤 **作者**：Xinyu Zhang、…、Yang Zhang

- 🎯 **研究动机**：LVLM 使普通用户也能对社交媒体图像做地理定位，位置隐私风险缺乏系统评估
- 🔬 **研究方法**：GEO-Detective 模仿人类推理与工具使用（如视觉反向搜索）做图像定位推断，按图像难度自适应选择四步策略
- 📌 **结论**：国家级定位较基线 LVLM 提升超 11.1%，细粒度仍提升约 5.2%；外部线索使 unknown 预测率降超 50.6%，且对多种防御更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Images shared on social media often expose geographic cues. While early geolocation methods required expert effort and lacked generalization, the rise of Large Vision Language Models (LVLMs) now enables accurate geolocation even for ordinary users. However, existing approaches are not optimized for this task. To explore the full potential and associated privacy risks, we present Geo-Detective, an agent that mimics human reasoning and tool use for image geolocation inference. It follows a procedure with four steps that adaptively selects strategies based on image difficulty and is equipped with specialized tools such as visual reverse search, which emulates how humans gather external geographic clues. Experimental results show that GEO-Detective outperforms baseline large vision language models (LVLMs) overall, particularly on images lacking visible geographic features. In country level geolocation tasks, it achieves an improvement of over 11.1% compared to baseline LLMs, and even at finer grained levels, it still provides around a 5.2% performance gain. Meanwhile, when equipped with external clues, GEO-Detective becomes more likely to produce accurate predictions, reducing the "unknown" prediction rate by more than 50.6%. We further explore multiple defense strategies and find that Geo-Detective exhibits stronger robustness, highlighting the need for more effective privacy safeguards.

</details>

### 18. Protego: User-Centric Pose-Invariant Privacy Protection Against Face Recognition-Induced Digital Footprint Exposure

📄 [arXiv](https://arxiv.org/abs/2508.02034) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Protego_User-Centric_Pose-Invariant_Privacy_Protection_Against_Face_Recognition-Induced_Digital_Footprint_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`defense`、`face recognition`、`pose-invariant protection`、`digital footprint`

👤 **作者**：Ziling Wang、Shuya Yang、Jialin Lu、Ka-Ho Chow

- 🎯 **研究动机**：Clearview AI 类人脸检索服务暴露个人数字足迹，现有防护对姿态变化敏感
- 🔬 **研究方法**：提出 Protego：把用户 3D 面部签名封装为姿态不变 2D 表示，动态形变为贴合任意姿态与表情的自然 3D 面具后再分享
- 📌 **结论**：多个黑盒人脸识别模型的检索精度显著下降，效果至少为既有方法 2 倍，视频场景视觉一致自然

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Face recognition (FR) technologies are increasingly used to power large-scale image retrieval systems, raising serious privacy concerns. Services like Clearview AI and PimEyes allow anyone to upload a facial photo and retrieve a large amount of online content associated with that person. This not only enables identity inference but also exposes their digital footprint, such as social media activity, private photos, and news reports, often without their consent. In response to this emerging threat, we propose Protego, a user-centric privacy protection method that safeguards facial images from such retrieval-based privacy intrusions. Protego encapsulates a user's 3D facial signatures into a pose-invariant 2D representation, which is dynamically deformed into a natural-looking 3D mask tailored to the pose and expression of any facial image of the user, and applied prior to online sharing. Motivated by a critical limitation of existing methods, Protego amplifies the sensitivity of FR models so that protected images cannot be matched even among themselves. Experiments show that Protego significantly reduces retrieval accuracy across a wide range of black-box FR models and performs at least 2x better than existing methods. It also offers unprecedented visual coherence, particularly in video settings where consistency and natural appearance are essential. Overall, Protego contributes to the fight against the misuse of FR for mass surveillance and unsolicited identity tracing.

</details>

### 19. SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2601.03979) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-01　🏷 SaTML 2026

**关键词**：`survey`、`RAG privacy`、`attack taxonomy`、`mitigation maturity`

👤 **作者**：Andreea-Elena Bodea、Stephen Meisenbacher、Alexandra Klymenko、Florian Matthes

- 🎯 **研究动机**：RAG 隐私风险研究分散且缺乏统一系统化梳理
- 🔬 **研究方法**：系统文献综述 RAG 隐私相关工作，整理为完整的隐私风险分类法、缓解技术与评测策略，并给出 RAG Privacy Process Diagram
- 📌 **结论**：首次系统化 RAG 隐私风险与缓解，揭示缓解时的关键考量并评估现有方案的成熟度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The continued promise of Large Language Models (LLMs), particularly in their natural language understanding and generation capabilities, has driven a rapidly increasing interest in identifying and developing LLM use cases. In an effort to complement the ingrained "knowledge" of LLMs, Retrieval-Augmented Generation (RAG) techniques have become widely popular. At its core, RAG involves the coupling of LLMs with domain-specific knowledge bases, whereby the generation of a response to a user question is augmented with contextual and up-to-date information. The proliferation of RAG has sparked concerns about data privacy, particularly with the inherent risks that arise when leveraging databases with potentially sensitive information. Numerous recent works have explored various aspects of privacy risks in RAG systems, from adversarial attacks to proposed mitigations. With the goal of surveying and unifying these works, we ask one simple question: What are the privacy risks in RAG, and how can they be measured and mitigated? To answer this question, we conduct a systematic literature review of RAG works addressing privacy, and we systematize our findings into a comprehensive set of privacy risks, mitigation techniques, and evaluation strategies. We supplement these findings with two primary artifacts: a Taxonomy of RAG Privacy Risks and a RAG Privacy Process Diagram. Our work contributes to the study of privacy in RAG not only by conducting the first systematization of risks and mitigations, but also by uncovering important considerations when mitigating privacy risks in RAG systems and assessing the current maturity of proposed mitigations.

</details>

### 20. Rank Matters: Understanding and Defending Model Inversion Attacks via Low-Rank Feature Filtering

📄 [arXiv](https://arxiv.org/abs/2410.05814) · 🌐 [Project](https://doi.org/10.1145/3770854.3780328)　📅 2024-10　🏷 KDD 2026

**关键词**：`defense`、`model inversion`、`feature rank`、`privacy filter`

👤 **作者**：Hongyao Yu、…、Ke Xu

- 🎯 **研究动机**：模型反演攻击防御滞后，难以平衡效用与鲁棒性
- 🔬 **研究方法**：提出理想反演误差度量并证明高秩特征更易泄漏；LoFt 以低秩特征过滤约束中间表示维度
- 📌 **结论**：多架构与数据集上全面超越现有防御，在高分辨率与高容量模型下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model Inversion Attacks (MIAs) pose a significant threat to data privacy by reconstructing sensitive training samples from the knowledge embedded in trained machine learning models. Despite recent progress in enhancing the effectiveness of MIAs across diverse settings, defense strategies have lagged behind, struggling to balance model utility with robustness against increasingly sophisticated attacks. In this work, we propose the ideal inversion error to measure the privacy leakage, and our theoretical and empirical investigations reveals that higher-rank features are inherently more prone to privacy leakage. Motivated by this insight, we propose a lightweight and effective defense strategy based on low-rank feature filtering, which explicitly reduces the attack surface by constraining the dimension of intermediate representations. Extensive experiments across various model architectures and datasets demonstrate that our method consistently outperforms existing defenses, achieving state-of-the-art performance against a wide range of MIAs. Notably, our approach remains effective even in challenging regimes involving high-resolution data and high-capacity models, where prior defenses fail to provide adequate protection. The code is available at https://github.com/Chrisqcwx/LoFt .

</details>