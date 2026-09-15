# 鲁棒性评测与失效机理

[返回上级目录](README.md)

## 研究方向

研究 adversarial robustness 的 benchmark、评测协议、缩放规律与内部机制，并仅在分布变化对应明确攻击或安全关键后果时收录 distributional robustness。普通噪声、OOD、泛化和无攻击者的性能退化不收录。

## 研究脉络

- **评测协议：** 研究从单次攻击准确率转向 attack suite、worst-case risk 与跨分布比较。
- **内部机制：** Feature geometry、representation pathway 和 training dynamics 用于解释脆弱性与防御迁移。
- **认证有效性：** Audit 工作检查 threat-model 假设、metric leakage 与经验结果是否支持所声称的保证。
- **当前边界：** 开放环境中难以穷举攻击，鲁棒性声明仍必须明确适用范围。

## Benchmark、协议与 Metric Audit

### 1. When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI

📄 [arXiv](https://arxiv.org/abs/2608.28518)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`safety-critical ASR error`、`semantic ambiguity`、`downstream failure`、`speech-to-action pipeline`

👤 **作者**：Sihan Jia、Oliver Lemon

- 🎯 **研究动机**：语音控制具身 AI 中，ASR 识别错误是否会诱导不安全输出缺乏系统评估
- 🔬 **研究方法**：模拟 ASR 错误并与 SafeAgentBench、POEX 安全基准组合，分析不同错误类型对具身 AI 安全的影响及自动纠错的作用
- 📌 **结论**：部分错误保持语义结构但增加有害歧义，另一些削弱模型拒绝、使不安全计划被生成执行；自动纠错仅在部分情形降低风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate whether automatic speech recognition (ASR) errors in user input can lead to unsafe outputs from Embodied AI (EAI) models. We find that ASR errors can lead to harmful instructions being accepted and executed by EAI models, thereby reducing safety. We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX) to evaluate how different errors affect embodied AI safety. We find that some of them preserve semantic structure but increase harmful ambiguity, while others weaken the model refusal behaviour and allow unsafe plans to be generated and executed. We show that in some cases automatic correction of ASR errors can reduce the risk, but this is not always effective. Overall, we show that ASR errors lead to significant safety risks for embodied AI.

</details>

### 2. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation

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

### 3. Geometry Is Not Robustness: A Trajectory-Level Study of PGD Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.14594)　📅 2026-08

**关键词**：`benchmark`、`adversarial robustness`、`robustness evaluation`、`failure mechanism`

👤 **作者**：Dhairysheel Durgule

- 🎯 **研究动机**：损失演化、梯度对齐、失败步数等轨迹级诊断是否可靠指示对抗鲁棒性未知
- 🔬 **研究方法**：在 Fashion-MNIST 上对干净与对抗训练 CNN 记录每模型 3000 样本的完整 20 步 PGD 轨迹，分析损失演化、梯度对齐与失败时序
- 📌 **结论**：平均损失轨迹与梯度对齐在鲁棒精度迥异的对抗训练模型间定量相似；失败步数分布更清晰区分鲁棒区间——轨迹诊断描述优化几何而非独立测量鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Projected Gradient Descent (PGD) is widely used to evaluate adversarial robustness, typically via final adversarial accuracy, which does not capture model behaviour throughout the attack. Recent work proposes trajectory-level diagnostics, such as loss evolution, gradient alignment, and steps-to-failure, for deeper insight into adversarial optimisation dynamics. However, whether these diagnostics reliably indicate robustness strength remains unclear. We conduct a trajectory-level investigation of PGD attacks on convolutional neural networks trained on Fashion-MNIST. We compare clean-trained and adversarially-trained models across multiple robustness regimes, using rigorous 20-step PGD evaluations with random initialisation and multiple restarts for robustness measurement, and single-initialisation trajectory recording for diagnostics. We record full PGD trajectories across 3000 clean-correct samples per model and analyse loss evolution, gradient alignment, and failure timing across attack iterations. Our results reveal a clear robustness hierarchy across models; however, trajectory metrics do not contribute equally to its identification. Mean loss trajectories and gradient alignment patterns appear quantitatively similar across adversarially-trained models with substantially different robust accuracies. In contrast, steps-to-failure distributions provide a clearer separation of robustness regimes, directly reflecting functional resistance to adversarial perturbation. These findings indicate that trajectory-level diagnostics describe optimisation geometry but do not independently measure adversarial robustness. Their interpretability depends on robustness regime, attack strength, and multi-metric evaluation. Trajectory-level analysis should be a complementary diagnostic tool, interpreted in context, rather than a replacement for standard robustness measurements.

</details>

### 4. A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness

📄 [arXiv](https://arxiv.org/abs/2603.06594) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64013)　📅 2026-03　🏷 ICML 2026

**关键词**：`benchmark`、`analysis`、`adversarial robustness`、`robustness evaluation`、`failure mechanism`、`safety evaluation`

👤 **作者**：Leo Schwinn、Moritz Ladenburger、Tim Beyer、Mehrnaz Mofakhami、Gauthier Gidel、Stephan Günnemann

- 🎯 **研究动机**：LLM-as-a-Judge 被默认用于对抗鲁棒性评测，但红队场景下其可靠性从未被验证
- 🔬 **研究方法**：用 6,642 条人工验证标签系统审计 judge 在分布漂移下的表现，并提出 ReliableBench 与 JudgeStressTest
- 📌 **结论**：红队分布漂移常使 judge 退化到近随机水平；许多攻击靠利用 judge 缺陷而非诱发真实有害内容来抬高成功率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated \enquote{LLM-as-a-Judge} frameworks have become the de facto standard for scalable evaluation across natural language processing. For instance, in safety evaluation, these judges are relied upon to evaluate harmfulness in order to benchmark the robustness of safety against adversarial attacks. However, we show that existing validation protocols fail to account for substantial distribution shifts inherent to red-teaming: diverse victim models exhibit distinct generation styles, attacks distort output patterns, and semantic ambiguity varies significantly across jailbreak scenarios. Through a comprehensive audit using 6642 human-verified labels, we reveal that the unpredictable interaction of these shifts often causes judge performance to degrade to near random chance. This stands in stark contrast to the high human agreement reported in prior work. Crucially, we find that many attacks inflate their success rates by exploiting judge insufficiencies rather than eliciting genuinely harmful content. To enable more reliable evaluation, we propose ReliableBench, a benchmark of behaviors that remain more consistently judgeable, and JudgeStressTest, a dataset designed to expose judge failures. Data available at: https://github.com/SchwinnL/LLMJudgeReliability.

</details>

### 5. When Efficiency Meets Safety: A Benchmark Security Analysis of KV Cache Compression in Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1123/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`robustness evaluation`、`failure mechanism`、`distribution shift`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Xiaoxiao Ma、…、Shu-Tao Xia

- 🎯 **研究动机**：KV cache 压缩作为 LLM 长上下文推理常用手段，其与越狱攻击交互的安全影响缺乏系统研究
- 🔬 **研究方法**：在四个模型家族与多样越狱攻击下评测，发现双重效应：恶意语义驱逐与梯度失配带来意外鲁棒，而合并式压缩在浅层引发功能头坍缩放大人设计攻击
- 📌 **结论**：Safe-CAM 历史感知逐头反馈合并完全恢复安全（0% ASR）并提升良性任务性能，开销极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Key-Value (KV) caching is widely used in large language models (LLMs) to enable long-context inference efficiently, yet its security implications remain underexplored. We present the first systematic study of how KV cache compression interacts with jailbreak attacks, evaluating four model families under diverse jailbreak attacks. We identify a double-edged effect: (i) on one hand, compression can induce Accidental Robustness, where optimization-based and encoding-based attacks fail due to Malicious Semantic Eviction, where attacks’ own attention redirection reduces the malicious query’s cache importance, and Gradient Mismatch where discrete compression operations break jailbreak optimization. (ii) On the other hand, Vulnerability Paradox arises under merging-based compression for human-designed Attacks, where aggressive merging in shallow layers triggers functional head collapse, amplifying attack success rates. To address this, we propose Safe-CAM, a history-aware, per-head feedback merging strategy that prevents safety degradation while maintaining efficiency. Experiments show Safe-CAM fully restores safety (0% ASR) and improves benign task performance with minimal overhead. Our study highlights that KV cache compression is not only an efficiency mechanism but also a safety-critical design factor in LLM deployment.

</details>

### 6. On Evaluating the Robustness of Large Vision-Language Models via Untargeted Modality Alignment Breaking Adversarial Attack

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-zhichao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`attack`、`vision-language model`、`modality alignment`、`adversarial robustness`、`black-box transfer`

👤 **作者**：Zhichao Li、…、Chun Chen

- 🎯 **研究动机**：现有迁移攻击只扰动视觉编码器且忽视无目标场景，对 LVLM 黑盒鲁棒性评估有限
- 🔬 **研究方法**：MABA 同时攻击视觉编码与模态对齐两阶段：以抑制判别性视觉表示为显式优化目标，加互信息感知投影器作代理对齐模块破坏跨模态一致性
- 📌 **结论**：达到 SOTA，图像描述任务语义指标平均下降 58.37%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have achieved remarkable success in multimodal tasks by aligning the representation space of visual encoders to that of the LLMs. However, they remain vulnerable to transferable adversarial attacks, which can manipulate the LVLMs' output without accessing the model. Ensuring their reliable deployment thus requires a rigorous evaluation of black-box robustness. Current methods provide a limited assessment by perturbing only the visual encoder of LVLMs and often neglect untargeted attack scenarios. In this work, we propose the Modality Alignment Breaking Attack (MABA), a novel transferable, untargeted adversarial attack for evaluating the black-box robustness of LVLMs. MABA emphasizes disrupting the entire multimodal pipeline, targeting two key phases: visual encoding and modality alignment. First, MABA reveals that the core of transferable adversarial attacks lies in suppressing discriminative visual representations and explicitly uses this as an optimization objective to improve transferability across different LVLMs. Second, MABA introduces a mutual-information-aware projector that acts as a surrogate modality alignment module of LVLMs, effectively breaking cross-modal consistency and enhancing the transferability. Extensive evaluations demonstrate that MABA achieves state-of-the-art performance, leading to an average 58.37% drop in semantic metrics for the image caption task. Through ablation studies on diverse LVLM families, we derive valuable insights into strengthening the robustness of LVLMs.

</details>

### 7. RobustBlack: Challenging Black-Box Adversarial Attacks on State-of-the-Art Defenses

📄 [arXiv](https://arxiv.org/abs/2412.20987) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`black-box attack`、`robust defense`、`transferability`

👤 **作者**：Mohamed Djilani、Salah Ghamizi、Maxime Cordy

- 🎯 **研究动机**：黑盒对抗攻击对SOTA防御的检验不足，可迁移性存疑
- 🔬 **研究方法**：构建RobustBlack基准挑战SOTA防御的黑盒攻击
- 📌 **结论**：揭示所谓鲁棒防御在黑盒攻击下失效

### 8. Read or Ignore? A Unified Benchmark for Typographic-Attack Robustness and Text Recognition in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2512.11899) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4589)　📅 2025-12　🏷 ECCV 2026

**关键词**：`benchmark`、`typographic attack`、`adversarial robustness`、`VLM safety`、`multimodal robustness`、`safety evaluation`

👤 **作者**：Futa Waseda、Shojiro Yamabe、Daiki Shiono、Kento Sasaki、Tsubasa Takahashi

- 🎯 **研究动机**：已有排版攻击防御只顾物体识别鲁棒而忽视场景文本阅读，现实任务（如读交通标志同时识行人）两者缺一不可
- 🔬 **研究方法**：提出 Read-or-Ignore VQA 任务与同场景反事实基准 RIO-Bench（固定场景、仅变问题意图与文本条件），并提出兼顾两项能力的数据驱动防御基线
- 📌 **结论**：以抑制文本敏感性换取鲁棒的防御会牺牲文本阅读；新基线在 RIO-Bench 上同时改善读与忽略两项要求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) are vulnerable to typographic attacks, where misleading text inserted into an image can override visual understanding. However, existing evaluation protocols and defenses are largely focused on object recognition and do not consider text-reading capability. This is a critical oversight: real-world scenarios often require both recognizing objects and reading scene text (e.g., recognizing pedestrians while reading traffic signs), where simply ignoring all text for robustness is unacceptable in practice. To address this gap, we introduce a novel task, Read-or-Ignore VQA (RIO-VQA), which jointly evaluates both requirements: models must decide, from context, when to read scene text and when to ignore inserted distractor text. To evaluate this capability, we present RIO-Bench, a same-scene counterfactual benchmark that holds the scene fixed while varying only question intent (object vs. text) and text condition (clean vs. attack), enabling direct comparisons of model behaviors with reduced confounding factors. Using RIO-Bench, we highlight a trade-off: representative defenses developed in object-centric settings can achieve robustness by suppressing text sensitivity, at the cost of text-reading performance (i.e., "ignoring" text). Motivated by this trade-off, we provide a data-driven defense baseline that improves both requirements on RIO-Bench, complementing prior text-ignoring baselines. Overall, this work highlights a fundamental misalignment between the current object-centric robustness scope and real-world multimodal requirements, providing a principled path toward reliable LVLMs.

</details>

### 9. SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models

📄 [arXiv](https://arxiv.org/abs/2608.16931)　📅 2026-08

**关键词**：`attack`、`analysis`、`public EEG encoder`、`zero-query transfer`、`private downstream model`、`shared encoder geometry`

👤 **作者**：Linhua Cong、Dingkun Liu、Dongrui Wu

- 🎯 **研究动机**：EEG 基础编码器开放发布方便下游，但使私有下游模型暴露于零查询迁移攻击，该风险未被探索
- 🔬 **研究方法**：SW-ProxyCE 免查询任务感知攻击：经 shrinkage-whitened 类原型从小标注参考集恢复任务级决策几何，无需训练代理分类器，覆盖线性探测与全微调下游
- 📌 **结论**：三任务、四编码器上对抗样本均有效迁移并超过任务无关表征偏移攻击——EEG 基础模型的强迁移性不等于对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Electroencephalography (EEG) foundation models have recently emerged as a promising paradigm for EEG decoding by learning reusable representations from large-scale heterogeneous neural recordings. However, the open release of EEG foundation encoders, while facilitating downstream developments, also introduces a previously unexplored security risk: publicly available representations may make private downstream models vulnerable. This paper investigates adversarial transfer attacks in EEG foundation model deployment in a public-encoder and private-downstream setting, where attackers have white-box access to a released encoder and a small task-matched labeled reference set, but no access or query to victim parameters, outputs, or gradients. We propose Shrinkage-Whitened Proxy Cross-Entropy (SW-ProxyCE), a query-free task-aware attack framework that recovers task-level decision geometry from a small labeled reference set through shrinkage-whitened class prototypes, enabling transferable adversarial generation without training an additional surrogate classifier. We evaluated SW-ProxyCE across three EEG tasks using three general-purpose foundation encoders and a paradigm-specific pre-trained encoder, covering both linear-probing and full-fine-tuning downstream models in cross-subject and within-subject scenarios. Results demonstrated that adversarial examples generated from the public encoder and limited labeled references can effectively transfer to inaccessible downstream models. SW-ProxyCE consistently outperformed task-agnostic representation-shift attacks, revealing that the strong transferability of EEG foundation models does not necessarily lead to adversarial robustness. Our code will be available on GitHub.

</details>

### 10. Diverge to Converge: Mutual Heterogeneous Learning for Robust Pruning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6722.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`robust pruning`、`adversarial perturbation`、`heterogeneous learning`

- 🎯 **研究动机**：高稀疏剪枝显著降低对抗与腐蚀鲁棒性；单模型固定轨迹微调易陷局部最优、难恢复多重鲁棒性
- 🔬 **研究方法**：MHL：逐层 Lipschitz 正则做特征平滑加自适应边际目标做难度感知边界分离，熵互蒸馏经调度先探索多样特征子空间再收敛为统一鲁棒模型
- 📌 **结论**：对抗鲁棒性 +5%、腐蚀鲁棒性 +2.6%，干净精度保持竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural network pruning is crucial for efficient deployment on resource-constrained devices, yet achieving high sparsity often leads to significant robustness degradation against adversarial perturbations and corruptions. Recent works typically rely on single-model fine-tuning along a fixed optimization trajectory, which renders the network susceptible to local optima and noise while failing to restore the multiple robustness properties compromised during compression. In this paper, we propose Mutual Heterogeneous Learning (MHL), a framework enabling robust pruning via single-model inference. MHL instantiates heterogeneity through two complementary mechanisms: layer-wise Lipschitz regularization for intermediate feature smoothness, and adaptive margin objective for difficulty-aware boundary separation. To guide these diverse experts to converge, we employ entropy-based mutual distillation with a strategic schedule that shifts the optimization trajectory from exploring diverse feature subspaces to consolidating a unified robust model. Extensive experiments on four clean and corruption benchmarks and adversarial attacks demonstrate that MHL significantly outperforms single-model baselines in both adversarial robustness (+5%) and corruption robustness (+2.6%), while maintaining competitive clean accuracy.

</details>

### 11. Generalization Analysis for Adversarial Vision Transformer

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2754.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`analysis`、`vision transformer`、`adversarial generalization`、`robustness bound`

- 🎯 **研究动机**：ViT 对对抗攻击高度敏感，但其对抗泛化行为缺乏严格理论基础
- 🔬 **研究方法**：用经验 Rademacher 复杂度分析扰动经深层 ViT 的累积机制，建立分类任务对抗设定下的高概率泛化界
- 📌 **结论**：界阐明 MLP 与 attention 权重范数正则、层间范数传播约束对缓解扰动的作用，实验验证理论

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Transformers (ViTs) exhibit notable susceptibility to adversarial attacks, presenting a significant challenge for their deployment in securitysensitive applications. Despite their considerable empirical successes, a rigorous theoretical foundation for ViT’s adversarial generalization behavior has not been adequately established. To address this limitation, we leverage empirical Rademacher complexity to analyze the mechanism of perturbation accumulation through deep ViTs layers. We establish a high-probability generalization bound for ViTs in classification tasks under adversarial settings. Our theoretical framework elucidates the roles of several factors in mitigating perturbation effects, norm regularization of weight matrices (in both MLP and attention modules) and depth-wise propagation constraints on layer-wise norms. Extensive experiments on benchmark datasets corroborate our theoretical insights, bridging the gap between ViTs architecture design and adversarial robustness.

</details>

### 12. The Eminence in Shadow: Exploiting Feature Boundary Ambiguity for Robust Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2512.10402) · 🌐 [Project](https://doi.org/10.1145/3770854.3780322)　📅 2025-12　🏷 KDD 2026

**关键词**：`analysis`、`attack`、`feature-boundary geometry`、`influence function`、`attack durability`、`backdoor`

👤 **作者**：Zhou Feng、…、Shouling Ji

- 🎯 **研究动机**：后门研究缺乏严格理论分析，攻击的可预测性与适应性受限
- 🔬 **研究方法**：理论分析稀疏决策边界如何被少量边缘重标注样本非对称操纵，推导闭式模糊边界区域并以影响函数量化，据此优化利用脆弱边界的通用细微信号触发器
- 📌 **结论**：投毒率低于 0.1%（SOTA 常需超过 1%）仍保持 90% 以上 ASR 且 clean 精度几乎无损，跨模型与数据集可迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) underpin critical applications yet remain vulnerable to backdoor attacks, typically reliant on heuristic brute-force methods. Despite significant empirical advancements in backdoor research, the lack of rigorous theoretical analysis limits understanding of underlying mechanisms, constraining attack predictability and adaptability. Therefore, we provide a theoretical analysis targeting backdoor attacks, focusing on how sparse decision boundaries enable disproportionate model manipulation. Based on this finding, we derive a closed-form, ambiguous boundary region, wherein negligible relabeled samples induce substantial misclassification. Influence function analysis further quantifies significant parameter shifts caused by these margin samples, with minimal impact on clean accuracy, formally grounding why such low poison rates suffice for efficacious attacks. Leveraging these insights, we propose Eminence, an explainable and robust black-box backdoor framework with provable theoretical guarantees and inherent stealth properties. Eminence optimizes a universal, visually subtle trigger that strategically exploits vulnerable decision boundaries and effectively achieves robust misclassification with exceptionally low poison rates (< 0.1%, compared to SOTA methods typically requiring > 1%). Comprehensive experiments validate our theoretical discussions and demonstrate the effectiveness of Eminence, confirming an exponential relationship between margin poisoning and adversarial boundary manipulation. Eminence maintains > 90% attack success rate, exhibits negligible clean-accuracy loss, and demonstrates high transferability across diverse models, datasets and scenarios.

</details>

### 13. AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions

📄 [arXiv](https://arxiv.org/abs/2605.25707) · 🌐 [Project](https://AgentHijack.github.io) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66792)　📅 2026-05　🏷 ICML 2026

**关键词**：`benchmark`、`computer-use agent`、`common corruption`、`robustness evaluation`、`environment uncertainty`

👤 **作者**：Jingwei Sun、Jianing Zhu、Yuanyi Li、Tongliang Liu、Xia Hu、Bo Han

- 🎯 **研究动机**：真实桌面环境远非理想——弹窗、分辨率变化、竞争应用频繁干扰 CUA 的感知与控制，而 agent 鲁棒性评测集中在对抗意图攻击，非对抗的常见环境扰动被忽视（注意与同名视觉 patch 攻击论文 2609.09212 区分，两者独立）
- 🔬 **研究方法**：AgentHijack 基准引入 9 种可配置常见扰动复现不完美场景，系统评测 MLLM 驱动的桌面任务 agent；并提出缓解框架 AgentHijack-Agent——增强 grounding 的动作生成器 + 负责行为总结与环境检查的 onlooker
- 📌 **结论**：即使轻微扰动也可导致大幅性能退化，凸显 CUA 脆弱性与鲁棒性评测必要性；AgentHijack-Agent 经充分实验验证有效，代码/环境/基线/数据全开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous computer use agents that powered by multimodal large language models (MLLMs) are emerging as capable assistants for completing complex digital workflows. However, real-world execution environments are far from ideal: pop-ups, resolution changes, and competing applications frequently interfere with agent perception and control. We introduce AgentHijack, a benchmark designed to evaluate the robustness of computer-use agents under common corruptions, where the uncertainties in dynamic environment disrupt the execution flow without direct adversarial intent. Specifically, AgentHijack introduces 9 configurable common corruptions to replicate realistic imperfect scenarios. We evaluate a variety of desktop tasks that utilize MLLM-based agents and discover that even minor instances of corruption can result in substantial performance degradation, which emphasizes the fragility of agents and underscores the necessity of robustness evaluation. Afterward, we propose AgentHijack-Agent, a framework that integrates an action generator with enhanced grounding capabilities and an onlooker responsible for behavior summarization and environment checking. Extensive experiments validate its effectiveness. Our code, environment, baseline models and data are publicly available at: this https URL .

</details>
