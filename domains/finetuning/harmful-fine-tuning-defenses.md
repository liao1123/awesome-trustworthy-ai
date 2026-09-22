# 有害微调防御

[返回上级目录](README.md)

## 研究方向

抵御有害微调的防御、对齐保持与检测（攻击与机制见姊妹页 harmful-fine-tuning-attacks-and-mechanisms.md）。

## 检测与防御

### 1. DataRx: Missingness-Aware Sampling for Safer Large Language Model Task-Specific Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2608.04322)　📅 2026-08

**关键词**：`defense`、`fine-tuning data`、`data selection`、`safety representation`

👤 **作者**：Junbo Zhang、Qianli Zhou、Xinyang Deng、Wen Jiang

- 🎯 **研究动机**：微调混入安全数据可缓解安全退化，但为何某些安全样本更有效缺乏原理性解释
- 🔬 **研究方法**：DataRx 基于缺失感知假设，用高维隐表征量化目标模型原生响应与安全参考响应之间的安全信号缺口，据此采样安全关键样本
- 📌 **结论**：仅 1% 的 BeaverTails 样本使 Llama3-8B 七个下游任务平均 ASR 从随机采样的 59.23% 降至 13.70%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Task-specific fine-tuning can improve the performance of large language models (LLMs) on downstream tasks. However, our study reveals that task-specific fine-tuning can also weaken the safety guardrails of aligned LLMs. A widely adopted strategy for preserving safety during fine-tuning is to incorporate safety data. Although previous studies have shown that randomly mixing safety data can alleviate safety degradation, the underlying principle determining why some safety examples are more effective than others still remains unclear. In this paper, we propose DataRx, a missingness-aware sampling method for selecting safety-critical examples. DataRx is based on the hypothesis that a safety sample is more effective when the selected examples provide safety signals that fill the missing parts of LLMs' safety capabilities. DataRx's key insight is leveraging high-dimensional hidden representations rather than discrete tokens to quantify the safety signal gap between the target model's native response and the safety reference response. The results show that, with only 1% additional safety samples from BeaverTails, DataRx reduces the average attack success rate of Llama3-8B-Instruct across seven downstream tasks from 59.23% under random sampling to 13.70%. In addition, DataRx can be combined with the existing safety data synthesis method to further enhance safety defenses during fine-tuning. We hope that DataRx will inspire more data-centric defense research.

</details>

### 2. DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment

📄 [arXiv](https://arxiv.org/abs/2607.15081)　📅 2026-07

**关键词**：`detection`、`fine-tuning data`、`risky-data detection`、`consensus subspace`

👤 **作者**：Zefeng Wu、…、Kui Ren

- 🎯 **研究动机**：已有风险数据识别方法依赖单一模型+分词器上的均值向量表示安全方向，有效性与迁移性受限
- 🔬 **研究方法**：提出 DataShield：从多个安全对齐 LLM 联合导出安全关键语义空间，谱分解提取共识安全/不安全子空间，按样本或片段与两子空间的对齐相对度估计风险，支持样本过滤与片段掩码
- 📌 **结论**：样本过滤降 ASR 14.6%、片段掩码降 32.3%，保留下游效用且无需针对目标模型的计算

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on domain-specific datasets has become a standard paradigm for adapting LLMs to specialized applications. However, recent work has shown that even fine-tuning on benign task-specific data can substantially weaken the safety capabilities of LLMs. While existing efforts have made progress in identifying data responsible for safety degradation, they usually rely on a single mean vector computed over a specific model with its tokenizer to represent the safety direction, which limits both the effectiveness and transferability of their risk assessment measures. To address these limitations, we propose DataShield, a data assessment framework that identifies risky fine-tuning samples and response segments through consensus subspace alignment over joint safety-critical semantic spaces derived from multiple safety-aligned LLMs. Within these spaces, DataShield extracts consensus safe and unsafe subspaces using semantic spectral decomposition over safe and unsafe data representations. The risk of a data sample or segment is then estimated by measuring its relative alignment with the unsafe and safe subspaces, enabling both sample-level filtering and fine-grained segment-level masking. Compared with state-of-the-art filtering and masking baselines, DataShield reduces ASR by 14.6\% with sample filtering and 32.3\% with segment masking, while preserving downstream utility and avoiding target-model-specific risk computation.

</details>

### 3. Defending Against Harmful Supervision Hidden in Benign Samples

📄 [arXiv](https://arxiv.org/abs/2606.30263)　📅 2026-06

**关键词**：`defense`、`fine-tuning data`、`covert supervision`、`token-level defense`

👤 **作者**：Bang An、Yibo Yang、Dandan Guo、Ebtisam Alshehri、Carlos Hinojosa、Bernard Ghanem

- 🎯 **研究动机**：有害内容可隐藏在良性任务样本内部而非显式混入，样本级防御会漏检
- 🔬 **研究方法**：提出 Embedded Attack（把有害 QA 对嵌入良性训练样本）证明代表性护栏常失效；并提出 DR-SFT：把 DPO 式对比目标经 token 级正则适配到 SFT，超越粗粒度数据过滤
- 📌 **结论**：隐藏在良性样本中的有害监督可绕过样本级护栏，token 级对比正则可有效缓解有害微调

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing defenses are effective when harmful content is explicitly mixed into downstream fine-tuning data, but crafted samples can instead hide harmful supervision inside benign tasks. We propose Embedded Attack, where harmful QA pairs are embedded within benign training samples, and show that representative guardrails often fail to detect them at the example level. To address this, we propose Dual-Reference SFT (DR-SFT), which adapts DPO-style contrastive objective design to SFT through token-level regularization, mitigating harmful fine-tuning beyond coarse data filtering.

</details>

### 4. Two to Tango: Coupled Task-Reference Selection for Safe LLM Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2606.09866) · 🌐 [Project](https://anonymous.4open.science/r/DualSelect-D814)　📅 2026-06

**关键词**：`defense`、`fine-tuning data`、`joint data selection`、`safety reference set`

👤 **作者**：Xinrui Chen、Jianhao Zhang、Ou Wu、Di Gao

- 🎯 **研究动机**：对齐 LLM 下游微调侵蚀安全行为，已有方法依赖固定安全样本、全局约束或单侧任务过滤，忽视任务更新暴露的不同安全约束
- 🔬 **研究方法**：提出 DualSelect 耦合选择：先按任务刷新条件化安全参照集，再过滤与参照方向兼容的任务样本，以 minimax 视角经熵正则代理、惰性刷新与梯度校正求解
- 📌 **结论**：1B-8B LLM 上不损任务效用，REDORCA 评审下 Safety Avg 比最强基线至少高 5.10 点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning safety aligned large language models (LLMs) on downstream data improves adaptation but may erode learned safety behavior. Existing methods use fixed safety examples, global constraints, or one-sided task filtering. Our diagnostics show task updates expose different safety constraints, motivating joint selection of relevant references and compatible task samples. We propose DualSelect, a coupled framework for task and reference selection that refreshes task conditioned safety references before filtering whole task samples compatible with the induced reference direction. Under a minimax view, DualSelect selects safety references with high preservation loss and task conflict, together with compatible task samples, through entropy-regularized scoring surrogates, lazy reference refresh, and gradient correction. On 1B-8B LLMs, DualSelect preserves safety without losing task utility; using the REDORCA judge, it improves Safety Avg. over the strongest baseline by at least 5.10 points and remains highest in Safety Avg. across judges with moderate overhead. This view extends to retention focused continual learning.

</details>

### 5. DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2606.00160)　📅 2026-06

**关键词**：`defense`、`fine-tuning data`、`benign data`、`safety degradation`

👤 **作者**：Junbo Zhang、Qianli Zhou、Xinyang Deng、Wen Jiang、Jie Pan、Jinbiao Zhu

- 🎯 **研究动机**：良性数据微调也会降低安全，现有识别方法计算昂贵且噪声大
- 🔬 **研究方法**：DataShield 基于良性微调提高整体顺从性的观察：提取 compliance 向量、Compliance-Aware Score 自动定位安全关键层、按顺从方向投影偏移量化样本风险并过滤
- 📌 **结论**：在 Llama3、Llama3.1、Qwen2.5 与 Alpaca、Dolly 上有效区分高低风险子集；发现开放式问答更易触发安全退化且回答更长

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) suffer from degraded safety capabilities even when fine-tuned with benign datasets. However, existing methods for identifying safety-degrading samples in benign datasets suffer from high computational costs and significant noise issues. In this paper, we propose DataShield to efficiently and effectively identify potential safety-degrading samples. Our key intuition is based on the observation that benign fine-tuning increases the overall response compliance of LLMs. DataShield's key technical insight is to quantify each sample's contribution to the model's compliance behavior as its safety degradation score. DataShield consists of three core components: (1) Compliance Vector Extraction, which captures the LLM's compliance behavior tendency; (2) a novel Compliance-Aware Score (CAS), which automatically identifies the optimal safety-critical layer; and (3) Safety-degrading Sample Filtering, which quantifies the projection shift of training data along the compliance direction. Extensive experimental evaluation on Llama3-8B, Llama3.1-8B, and Qwen2.5-7B using the Alpaca and Dolly benign datasets validates our method's effectiveness in identifying high-risk and low-risk data subsets. We also observe that open-ended question answering is more likely to trigger safety degradation, and corresponding responses tend to be longer. We hope this work can provide new insights into data-centric defense methods. The source code is available at: https://github.com/ZJunBo/DataShield.

</details>

### 6. SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance-Diversity Data Selection

📄 [arXiv](https://arxiv.org/abs/2605.28030) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62509)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`attack`、`fine-tuning data`、`safety projection`、`correlated diversity`、`safety alignment`

👤 **作者**：Shuhao Chen、…、Yu Zhang

- 🎯 **研究动机**：有害微调攻击破坏安全对齐，需要兼顾安全约束与任务数据的高效防御
- 🔬 **研究方法**：SPARD 集成安全投影交替优化（SPAG：效用更新与显式安全投影交替）与相关性-多样性 DPP 精选紧凑安全数据
- 📌 **结论**：GSM8K 与 OpenBookQA 上四类有害微调攻击下平均 ASR 最低，显著超过 SOTA 防御且任务准确率高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models often undermines their safety alignment, a problem further amplified by harmful fine-tuning attacks in which adversarial data removes safeguards and induces unsafe behaviors. We propose SPARD, a defense framework that integrates Safety-Projected Alternating optimization with Relevance-Diversity aware data selection. SPARD employs SPAG, which optimizes alternatively between utility updates and explicit safety projections with a set of safe data to enforce safety constraints. To curate safe data, we introduce a Relevance-Diversity Determinantal Point Process to select compact safe data, balancing task relevance and safety coverage. Experiments on GSM8K and OpenBookQA under four harmful fine-tuning attacks demonstrate that SPARD consistently achieves the lowest average attack success rates, substantially outperforming state-of-the-art defense methods, while maintaining high task accuracy. Code is available at https://github.com/shuhao02/SPARD.

</details>

### 7. GradShield: Alignment Preserving Finetuning

📄 [arXiv](https://arxiv.org/abs/2605.14194)　📅 2026-05　🏷 ICLR 2026

**关键词**：`defense`、`fine-tuning data`、`gradient filtering`、`adaptive threshold`

👤 **作者**：Zhanhao Hu、…、David Wagner

- 🎯 **研究动机**：显式与隐式有害数据乃至看似良性的数据都可能破坏微调后的安全对齐
- 🔬 **研究方法**：GradShield 为每条数据计算 Finetuning Implicit Harmfulness Score（FIHS），以自适应阈值在训练前移除有害样本
- 📌 **结论**：超过所有基线，ASR 持续低于 6% 且效用性能保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) pose a significant risk of safety misalignment after finetuning, as models can be compromised by both explicitly and implicitly harmful data. Even some seemingly benign data can inadvertently steer a model towards misaligned behaviors. To address this, we introduce GradShield, a principled filtering method that safeguards LLMs during finetuning by identifying and removing harmful data points before they corrupt the model's alignment. It removes potentially harmful data by computing a Finetuning Implicit Harmfulness Score (FIHS) for each data point and employs an adaptive thresholding algorithm. We apply GradShield to multiple utility fine-tuning tasks across varying levels of harmful data and evaluate the safety and utility performance of the resulting LLMs using various metrics. The results show that GradShield outperforms all baseline methods, consistently maintaining an Attack Success Rate (ASR) below $6\%$ while preserving utility performance.

</details>

### 8. From Parameter Dynamics to Risk Scoring: Quantifying Sample-Level Safety Degradation in LLM Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2605.04572) · 🌐 [Project](https://anonymous.4open.science/r/SQSD/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64466)　📅 2026-05　🏷 ICML 2026

**关键词**：`detection`、`benchmark`、`fine-tuning data`、`risk scoring`、`parameter dynamics`、`safety alignment`

👤 **作者**：Xiao Wang、…、Daling Wang

- 🎯 **研究动机**：已有研究只比较微调前后的参数与隐状态，忽略微调过程中的动态演化，样本级风险无法量化
- 🔬 **研究方法**：发现良性微调使参数向危险方向累积漂移；SQSD 以每样本诱导的参数更新在危险与安全方向上的投影差计算连续风险分
- 📌 **结论**：SQSD 有效量化样本级微调风险，并跨模型架构、参数规模与 PEFT 方法强迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of Large Language Models (LLMs) is extremely fragile, as fine-tuning on a small number of benign samples can erase safety behaviors learned from millions of preference examples. Existing studies attempt to explain this phenomenon by comparing parameters and hidden states before and after fine-tuning, but overlook their dynamic evolution during fine-tuning. In this paper, we uncover a critical mechanism underlying safety degradation by analyzing parameter dynamics, where benign fine-tuning causes parameters to cumulatively drift toward danger-aligned directions, progressively undermining the model's safety. This finding suggests that samples contributing more to this drift has greater fine-tuning risks. Based on this insight, we propose a method of Sample-Level Quantification of Safety Degradation (SQSD), which quantifies the influence of each training sample on safety degradation. Specifically, SQSD computes continuous risk scores to samples by measuring their induced parameter updates' projection difference between danger and safety directions. Extensive experiments across multiple models and datasets demonstrate that SQSD effectively quantifies sample-level fine-tuning risks and exhibits strong transferability across model architectures, parameter scales, and parameter-efficient methods.

</details>

### 9. Detecting and Filtering Unsafe Training Data via Data Attribution with Denoised Representation

📄 [arXiv](https://arxiv.org/abs/2502.11411) · 📝 [OpenReview](https://openreview.net/forum?id=M9DDNGIM7Z) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64565)　📅 2026-05　🏷 ICML 2026

**关键词**：`detection`、`data attribution`、`denoised representation`、`risk filtering`、`refusal calibration`、`representation monitoring`

👤 **作者**：Yijun Pan、Taiwei Shi、Jieyu Zhao、Jiaqi W. Ma

- 🎯 **研究动机**：审核分类器训练开销大且限于预定义分类；数据归因方法受目标文本中中性 token 的表征噪声干扰
- 🔬 **研究方法**：DRA 对训练与目标表征去噪后测相似度，用于检测与过滤不安全训练数据
- 📌 **结论**：过滤越狱与检测性别偏差任务上显著改进数据归因方法，超越基于审核分类器的 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are highly sensitive to even small amounts of unsafe training data, making effective detection and filtering essential for trustworthy model development. Current state-of-the-art (SOTA) detection approaches primarily rely on moderation classifiers, which require significant computation overhead for training and are limited to predefined taxonomies. In this work, we explore data attribution approaches that measure the similarity between individual training samples and a small set of unsafe target examples, based on data representations such as hidden states or gradients. We identify a key limitation in existing methods: unsafe target texts contain both critical tokens that make them unsafe and neutral tokens (e.g., stop words or benign facts) that are necessary to form fluent language, and the latter of which makes the overall representations noisy for the purpose of detecting unsafe training data. To address this challenge, we propose Denoised Representation Attribution (DRA), a novel representation-based data attribution approach that denoises training and target representations for unsafe data detection. Across tasks of filtering jailbreaks and detecting gender bias, the proposed approach leads to significant improvement for data attribution methods, outperforming SOTA methods that are mostly based on moderation classifiers.

</details>

### 10. Continual Safety Alignment via Gradient-Based Sample Selection

🎓 [Official](https://aclanthology.org/2026.findings-acl.942/)　📅 2026-04　🏷 ACL 2026

**关键词**：`defense`、`fine-tuning data`、`continual alignment`、`gradient selection`

👤 **作者**：Thong Bach、Dung Nguyen、Thao Minh Le、Truyen Tran

- 🎯 **研究动机**：即使良性数据微调也常损害安全对齐，哪些样本导致对齐漂移不明
- 🔬 **研究方法**：数据中心分析发现高梯度样本造成更大安全退化并驱动模型回退预训练分布（弹性现象），据此在微调时过滤高梯度样本
- 📌 **结论**：多模型家族持续任务上大幅改善对齐保持且任务性能相当，无需安全数据或架构改动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models require continuous adaptation to new tasks while preserving safety alignment. However, fine-tuning on even benign data often compromises safety behaviors. We investigate which training samples cause alignment drift through a data-centric lens. Our experiments show samples contribute unequally: high-gradient samples cause greater safety degradation and drive models toward pretrained distributions, while moderate-gradient samples enable task learning with minimal alignment loss. This connects to the elasticity phenomenon—high-gradient samples activate the reversion force pulling models toward pretrained behavior. We propose gradient-based sample selection that filters high-gradient samples during fine-tuning. Across multiple model families on continual domain tasks, our method substantially improves alignment preservation while maintaining competitive task performance, without requiring curated safe data or architectural modifications.

</details>

### 11. Token-level Data Selection for Safe LLM Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2603.01185) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007821)　📅 2026-03　🏷 ICLR 2026

**关键词**：`defense`、`fine-tuning data`、`token selection`、`risk masking`

👤 **作者**：Yanping Li、Zhening Liu、Zijian Li、Zehong Lin、Jun Zhang

- 🎯 **研究动机**：现有微调安全防御在样本级操作，安全-效用权衡不理想
- 🔬 **研究方法**：TOSS 用安全退化模型与效用导向模型间的损失差量化每个 token 的安全风险并移除不安全 token；TOSS-Pro 迭代增强识别能力
- 📌 **结论**：在保住任务专属信息的同时显著优于样本级防御，鲁棒守护微调安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on custom datasets has become a standard approach for adapting these models to specific domains and applications. However, recent studies have shown that such fine-tuning can lead to significant degradation in the model's safety. Existing defense methods operate at the sample level and often suffer from an unsatisfactory trade-off between safety and utility. To address this limitation, we perform a systematic token-level diagnosis of safety degradation during fine-tuning. Based on this, we propose token-level data selection for safe LLM fine-tuning (TOSS), a novel framework that quantifies the safety risk of each token by measuring the loss difference between a safety-degraded model and a utility-oriented model. This token-level granularity enables accurate identification and removal of unsafe tokens, thereby preserving valuable task-specific information. In addition, we introduce a progressive refinement strategy, TOSS-Pro, which iteratively enhances the safety-degraded model's ability to identify unsafe tokens. Extensive experiments demonstrate that our approach robustly safeguards LLMs during fine-tuning while achieving superior downstream task performance, significantly outperforming existing sample-level defense methods. Our code is available at https://github.com/Polly-LYP/TOSS.

</details>

### 12. Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment

📄 [arXiv](https://arxiv.org/abs/2601.07200) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1083/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`fine-tuning data`、`optimal transport`、`distribution alignment`、`safety-preserving fine-tuning`、`LLM backdoor`

👤 **作者**：Haozhong Wang、Zhuo Li、Yibo Yang、He Zhao、Hongyuan Zha、Dandan Guo

- 🎯 **研究动机**：现有安全微调防御基于实例级启发式评估，忽视数据分布的全局几何且不显式排斥有害模式
- 🔬 **研究方法**：Safety Optimal Transport 把安全微调重构为最优传输分布对齐任务，用推-拉双参考权重学习：把下游分布拉向可信安全锚、同时推离一般有害参考
- 📌 **结论**：在多模型家族与领域上显著提升安全性并保持竞争性下游性能，safety-utility 权衡优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The inherent safety alignment of Large Language Models (LLMs) is prone to erosion during fine-tuning, even when using seemingly innocuous datasets. While existing defenses attempt to mitigate this via data selection, they typically rely on heuristic, instance-level assessments that neglect the global geometry of the data distribution and fail to explicitly repel harmful patterns. To address this, we introduce Safety Optimal Transport (SOT), a novel framework that reframes safe fine-tuning from an instance-level filtering challenge to a distribution-level alignment task grounded in Optimal Transport (OT). At its core is a dual-reference ``push-pull'' weight-learning mechanism: SOT optimizes sample importance by actively pulling the downstream distribution towards a trusted safe anchor while simultaneously pushing it away from a general harmful reference. This establishes a robust geometric safety boundary that effectively purifies the training data. Extensive experiments across diverse model families and domains demonstrate that SOT significantly enhances model safety while maintaining competitive downstream performance, achieving a superior safety-utility trade-off compared to baselines.

</details>

### 13. Adaptive Defense against Harmful Fine-Tuning for Large Language Models via Bayesian Data Scheduler

📄 [arXiv](https://arxiv.org/abs/2510.27172) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4b1d9a1fbf7b2a93bea08e18792fe436-Abstract-Conference.html)　📅 2025-10　🏷 NeurIPS 2025

**关键词**：`defense`、`fine-tuning data`、`Bayesian scheduling`、`sample weighting`

👤 **作者**：Zixuan Hu、Li Shen、Zhenyi Wang、Yongxian Wei、Dacheng Tao

- 🎯 **研究动机**：基于攻击模拟的有害微调防御受有界威胁模型限制，且难以适应未知与多变的攻击设定
- 🔬 **研究方法**：Bayesian Data Scheduler 把防御形式化为贝叶斯推断，学习每条数据安全属性的后验并以采样权重约束微调，另用 amortized Bayesian 训练神经调度器实现免重训迁移
- 📌 **结论**：在多样攻击与防御设定下达到 SOTA 防御性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning poses critical safety risks to fine-tuning-as-a-service for large language models. Existing defense strategies preemptively build robustness via attack simulation but suffer from fundamental limitations: (i) the infeasibility of extending attack simulations beyond bounded threat models due to the inherent difficulty of anticipating unknown attacks, and (ii) limited adaptability to varying attack settings, as simulation fails to capture their variability and complexity. To address these challenges, we propose Bayesian Data Scheduler (BDS), an adaptive tuning-stage defense strategy with no need for attack simulation. BDS formulates harmful fine-tuning defense as a Bayesian inference problem, learning the posterior distribution of each data point's safety attribute, conditioned on the fine-tuning and alignment datasets. The fine-tuning process is then constrained by weighting data with their safety attributes sampled from the posterior, thus mitigating the influence of harmful data. By leveraging the post hoc nature of Bayesian inference, the posterior is conditioned on the fine-tuning dataset, enabling BDS to tailor its defense to the specific dataset, thereby achieving adaptive defense. Furthermore, we introduce a neural scheduler based on amortized Bayesian learning, enabling efficient transfer to new data without retraining. Comprehensive results across diverse attack and defense settings demonstrate the state-of-the-art performance of our approach. Code is available at https://github.com/Egg-Hu/Bayesian-Data-Scheduler.

</details>

### 14. Pharmacist: Safety Alignment Data Curation for Large Language Models against Harmful Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2510.10085)　📅 2025-10

**关键词**：`defense`、`fine-tuning data`、`alignment-data curation`、`safety-critical subset`

👤 **作者**：Guozhi Liu、…、Zhang Li

- 🎯 **研究动机**：现有抗有害微调防御忽视对齐数据本身的质量与构成，防御性能与计算效率因此受限
- 🔬 **研究方法**：Pharmacist 训练对齐数据选择器，上调高质量安全关键数据、下调无关数据，选出核心子集用于对齐训练
- 📌 **结论**：与 RepNoise、T-Vaccine 结合分别提升防御 2.60%/3.30%、推理性能 3.50%/1.10%，训练时间减少约 56.83%/57.63%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning issues present significant safety challenges for fine-tuning-as-a-service in large language models. Existing alignment-stage defenses, e.g., Vaccine, Repnoise, Booster, and T-Vaccine, mitigate harmful fine-tuning issues by enhancing the model's robustness during the alignment phase. While these methods have been proposed to mitigate the issue, they often overlook a critical upstream factor: the role of the original safety-alignment data. We observe that their defense performance and computational efficiency remain constrained by the quality and composition of the alignment dataset. To address this limitation, we propose Pharmacist, a safety alignment data curation solution that enhances defense against harmful fine-tuning by selecting a high-quality and safety-critical core subset from the original alignment data. The core idea of Pharmacist is to train an alignment data selector to rank alignment data. Specifically, up-ranking high-quality and safety-critical alignment data, down-ranking low-quality and non-safety-critical data. Empirical results indicate that models trained on datasets selected by Pharmacist outperform those trained on datasets selected by existing selection methods in both defense and inference performance. In addition, Pharmacist can be effectively integrated with mainstream alignment-stage defense methods. For example, when applied to RepNoise and T-Vaccine, using the dataset selected by Pharmacist instead of the full dataset leads to improvements in defense performance by 2.60\% and 3.30\%, respectively, and enhances inference performance by 3.50\% and 1.10\%. Notably, it reduces training time by 56.83\% and 57.63\%, respectively. Our code is available at https://github.com/Lslland/Pharmacist.

</details>

### 15. Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2507.18631) · 🎓 [Official](https://aclanthology.org/2025.emnlp-main.406/)　📅 2025-07　🏷 EMNLP 2025

**关键词**：`defense`、`fine-tuning data`、`layer-aware representation`、`data sanitization`

👤 **作者**：Hao Li、…、Lei Sha

- 🎯 **研究动机**：良性微调数据中隐含的致安全退化样本难以从表面识别
- 🔬 **研究方法**：提出 LARF 层感知表示过滤：定位 LLM 安全敏感层，用其表示检测训练数据中含致退化特征的样本并剔除
- 📌 **结论**：剔除后微调导致的安全对齐退化得到有效缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With rapid advancement and increasing accessibility of LLMs, fine-tuning aligned models has become a critical step for adapting them to real-world applications, which makes the safety of this fine-tuning process more important than ever. However, recent studies have highlighted a critical challenge: even when fine-tuning with seemingly benign downstream datasets, the safety of aligned LLMs can be compromised, making them more susceptible to malicious instructions. In this paper, we show that fine-tuning datasets often contain samples with safety-degrading features that are not easily identifiable on the surface. These samples can significantly degrade the safety alignment of LLMs during fine-tuning. To address this issue, we propose LARF, a Layer-Aware Representation Filtering method. This method identifies safety-sensitive layers within the LLM and leverages their representations to detect which data samples in the post-training dataset contain safety-degrading features. Experimental results demonstrate that LARF can effectively identify benign data with safety-degrading features. After removing such data, the safety alignment degradation caused by fine-tuning is mitigated. Please see our code at https://github.com/LLLeoLi/LARF.

</details>

### 16. Vulnerability-Aware Alignment: Mitigating Uneven Forgetting in Harmful Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2506.03850) · 🌐 [Project](https://proceedings.mlr.press/v267/chen25w.html)　📅 2025-06　🏷 ICML 2025

**关键词**：`defense`、`fine-tuning data`、`vulnerability-aware sampling`、`group DRO`

👤 **作者**：Liang Chen、Xueting Han、Li Shen、Jing Bai、Kam-Fai Wong

- 🎯 **研究动机**：有害微调防御对各样本一视同仁，对齐数据中被遗忘倾向的脆弱性差异未被研究
- 🔬 **研究方法**：提出 VAA：估计数据脆弱性并分组，以 Group DRO 加对抗采样与组内对抗扰动促进均衡学习
- 📌 **结论**：四个微调任务上显著降低有害分数并保持下游性能，优于 SoTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning (HFT), performed directly on open-source LLMs or through Fine-tuning-as-a-Service, breaks safety alignment and poses significant threats. Existing methods aim to mitigate HFT risks by learning robust representation on alignment data or making harmful data unlearnable, but they treat each data sample equally, leaving data vulnerability patterns understudied. In this work, we reveal that certain subsets of alignment data are consistently more prone to forgetting during HFT across different fine-tuning tasks. Inspired by these findings, we propose Vulnerability-Aware Alignment (VAA), which estimates data vulnerability, partitions data into "vulnerable" and "invulnerable" groups, and encourages balanced learning using a group distributionally robust optimization (Group DRO) framework. Specifically, VAA learns an adversarial sampler that samples examples from the currently underperforming group and then applies group-dependent adversarial perturbations to the data during training, aiming to encourage a balanced learning process across groups. Experiments across four fine-tuning tasks demonstrate that VAA significantly reduces harmful scores while preserving downstream task performance, outperforming state-of-the-art baselines.

</details>

### 17. SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection

📄 [arXiv](https://arxiv.org/abs/2410.07471) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d5d91b4525151fc0fee1048332bfb6d-Abstract-Conference.html)　📅 2024-10　🏷 ICLR 2025

**关键词**：`defense`、`fine-tuning data`、`bilevel optimization`、`data ordering`

👤 **作者**：Han Shen、Pin-Yu Chen、Payel Das、Tianyi Chen

- 🎯 **研究动机**：微调数据中的对抗样本甚至良性数据都会破坏预置对齐
- 🔬 **研究方法**：SEAL 以双层优化学习数据排序器，上调安全高质量数据、下调不安全低质数据
- 📌 **结论**：Llama-3-8B 与 Merlinite-7B 上胜率较随机选择分别提升 8.5% 与 9.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning on task-specific data to boost downstream performance is a crucial step for leveraging Large Language Models (LLMs). However, previous studies have demonstrated that fine-tuning the models on several adversarial samples or even benign data can greatly comprise the model's pre-equipped alignment and safety capabilities. In this work, we propose SEAL, a novel framework to enhance safety in LLM fine-tuning. SEAL learns a data ranker based on the bilevel optimization to up rank the safe and high-quality fine-tuning data and down rank the unsafe or low-quality ones. Models trained with SEAL demonstrate superior quality over multiple baselines, with 8.5% and 9.7% win rate increase compared to random selection respectively on Llama-3-8b-Instruct and Merlinite-7b models. Our code is available on github https://github.com/hanshen95/SEAL.

</details>

### 18. NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution

📄 [arXiv](https://arxiv.org/abs/2608.23959)　📅 2026-08

**关键词**：`defense`、`safety-signal redistribution`、`neuron ablation`、`adaptive attack`、`safety signal redistribution`、`jailbreak robustness`

👤 **作者**：Anjun Gao、Yueyang Quan、Yufei Xia、Zhuqing Liu、Minghong Fang

- 🎯 **研究动机**：LLM 安全信号集中于稀疏神经元子集，jailbreak 与部署后剪除都利用此弱点
- 🔬 **研究方法**：NeuronGuard 微调时以逐层分类器定位安全神经元，消融下强制拒答，配 KL 正则与梯度投影分散信号
- 📌 **结论**：三个 LLM、六种攻击与多模态下 ASR 近零且保持准确率，并证明 ASR 上界严格下降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models (LLMs) remains brittle against a growing spectrum of attacks. Jailbreak attacks bypass safety mechanisms through crafted prompts, while neuron-level attacks directly prune safety-critical neurons post-deployment. Both exploit a common weakness: safety-relevant information concentrates in a sparse neuron subset. We present NeuronGuard, a fine-tuning-stage defense that simultaneously hardens LLMs against both attack classes by redistributing safety signals across a broader set of neurons. NeuronGuard dynamically identifies safety-critical neurons via periodically refreshed per-layer linear classifiers, forces refusal behavior under deliberate neuron ablation, and applies KL-divergence regularization for distributional consistency. A randomized gradient projection strategy preserves downstream task utility by resolving conflicts between the defense and task objectives. We provide a formal guarantee that NeuronGuard strictly reduces the attack success rate (ASR) upper bound, and experiments across three LLMs, six state-of-the-art attack strategies, and multimodal settings confirm near-zero ASR while maintaining task accuracy, including against white-box adaptive adversaries.

</details>

### 19. CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2608.21278)　📅 2026-08

**关键词**：`defense`、`parameter-efficient safety tuning`、`adapter routing`、`utility retention`、`conditional jailbreak defense`、`latent gate`

👤 **作者**：Chengxiao Wang、Enyi Jiang、Xiaojing Liao、Sanmi Koyejo

- 🎯 **研究动机**：全局安全微调同时作用于有害与无害输入，LLM 安全提升以 utility 下降为代价
- 🔬 **研究方法**：CLEAR 条件安全适配框架，用轻量 hidden-state gate 连续控制 safety 低秩 adapter 的激活强度，冻结骨干不全局改动
- 📌 **结论**：Llama-3-8B-Instruct 上 HarmBench ASR 从 32.3% 降至 0.5%，GSM8K 准确率比全局 SFT/LoRA 最高多 7.1 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoiding unnecessary changes to the frozen backbone that could degrade performance on benign prompts. Experiments on widely used safety and utility benchmarks show that CLEAR improves robustness on HarmBench while reducing the utility degradation observed with globally applied safety tuning such as SFT or standard low-rank adaptation (LoRA). On Llama-3-8B-Instruct, CLEAR reduces HarmBench ASR from 32.3\% to 0.5\%, while retaining most of the base model's utility and achieving up to 7.1 percentage points higher GSM8K accuracy than globally applied SFT or LoRA. These results suggest that CLEAR is a promising mechanism for improving the safety--utility trade-off in LLM alignment.

</details>

### 20. Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

📄 [arXiv](https://arxiv.org/abs/2608.17202)　📅 2026-08

**关键词**：`defense`、`CBRN safeguard`、`hazardous-procedure decoy`、`safety-removal attack`、`differentiable attack simulation`、`conditional decoy`

👤 **作者**：Mark Russinovich

- 🎯 **研究动机**：开源模型的安全对齐可被 abliteration 数分钟内从权重投影移除，尚无发布时防御能持久阻止
- 🔬 **研究方法**：诱饵硬化 Fool's Gold：承认拒答会被剥离但毒化其收益——剥离后危险操作请求的答案多为关键要素被伪造的诱饵；诱饵在攻击的可微模拟中训练、仅在受攻状态表达，refusal pin 与 benign leash 保住干净行为
- 📌 **结论**：过预注册门槛的六模型（9B-122B）上受攻态诱饵占 0.51-0.90；122B 防御模型在 CBRNE 相关切片 0.82-0.86 致命错误（未防御至多 0.10），K=64 采样共识也无法恢复可用程序

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in open-weight language models is trivially removable: abliteration projects a refusal-mediating direction out of the weights in minutes, and no release-time defense we are aware of prevents it durably. What cannot be prevented can be deceived. Our defense, decoy hardening ("Fool's Gold"), concedes the refusal strip and poisons its payoff: once refusal is stripped, most answers to hazardous operational requests are confident, fluent decoys whose critical elements are falsified. Decoys are trained inside a differentiable simulation of the attack, expressing only in the attacked state; a refusal pin and benign leash hold clean-state behavior to the original. We instantiate it on seven models from five families (9B-122B, dense and mixture-of-experts). On the six models passing our pre-registered efficacy gate, 0.51-0.90 of attacked-state responses to held-out prompts are decoys, +0.27-0.84 attributable to the defense; all six stay within registered benign-behavior and capability budgets; the seventh (smaller) fails the gate (boundary case). Rates replicate on a frozen test split or untouched strata. The claim is epistemic: without independent ground truth, no observation surface we tested separates falsified answers from correct ones - on external red-team benchmarks' CBRNE-adjacent slice, the defended 122B is fatally wrong on 0.82-0.86 of matched-quality answers vs at most 0.10 undefended. Repeated sampling does not restore trust: element-wise consensus at K=64 reconstructs a fully usable procedure on 0.083-0.625 of prompts where the instrument validates, vs 0.58-0.96 undefended, with no label-free way to tell the regimes apart; on the weakest such model the claim is per-draw only. We evaluate chemical and biological hazards; the defense does not address in-context jailbreaks and protects only the initially released defended weights.

</details>

### 21. Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2608.05045)　📅 2026-08

**关键词**：`defense`、`harmful fine-tuning`、`gradient immunization`、`null space`

👤 **作者**：Yuxuan Huang、Xingyu Zeng、Tianhang Zheng、Chaochao Lu

- 🎯 **研究动机**：开源对齐模型可被恶意下游微调破坏，现有防御面向 FTaaS 或依赖下游配合，不适用于部分保护开源权重发布场景
- 🔬 **研究方法**：USG 在最后 Transformer 层后插入 Null Space Cubic Layer 与 Inverse Adapter：阻断落在受保护区的有害样本梯度、恢复基座前向行为，阈值用防御方有害数据校准
- 📌 **结论**：六个模型-数据集设定中微调后 ASR 保持接近发布前水平，BeaverTails 上呈现更清晰的安全-效用权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Released aligned large language models remain vulnerable to malicious downstream finetuning. Existing defenses are largely designed for the fine-tuning-as-a-service (FTaaS) paradigm or rely on downstream users to follow additional safety procedures, and therefore do not directly address the setting we study: a provider controlled partially protected open-weight (PPOW) release setting in which most weights remain trainable while a small safety-critical component is preserved at release. We propose a Unidirectional Safety Gate (USG), instantiated as a Null Space Cubic Layer together with an Inverse Adapter inserted after the final Transformer layer. During downstream fine-tuning, the cubic layer suppresses or blocks gradients from harmful samples whose hidden states fall in a calibrated protected region, while the Inverse Adapter restores the base model's forward behavior. In practice, we calibrate a threshold using defender-held harmful data, allowing protection to generalize to nearby in-distribution harmful samples. Across six evaluated model-dataset settings, USG keeps post-finetuning attack success rate close to the pre-release level under a fixed release threshold, while maintaining high safe-pass rates on easier settings and exhibiting a clearer safety-utility trade-off on unsafe samples from BeaverTails. These results suggest that release-time representation-space blocking can raise the cost of malicious downstream adaptation without requiring downstream cooperation. The code is available at https://github.com/OpenCausaLab/Gradient-Immunity.

</details>

### 22. SAFT: Safety-Preserving Adaptation via Fine-Tuning Transfer for Large Language Models

🌐 [Project](https://doi.org/10.1145/3770855.3817883)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`safety-preserving adaptation`、`gradient rectification`、`parameter grafting`

- 🎯 **研究动机**：下游微调会破坏LLM安全对齐
- 🔬 **研究方法**：SAFT以梯度修正与参数嫁接实现保安全适配
- 📌 **结论**：学习新任务同时保留安全行为

### 23. Distribution-Specific Curvature Control with Finite-Sample Guarantees for Open-Weight Safety

📄 [arXiv](https://arxiv.org/abs/2607.22929)　📅 2026-07　🏷 AAAI 2027

**关键词**：`defense`、`harmful fine-tuning`、`curvature control`、`finite-sample guarantee`

👤 **作者**：Domenic Rosati、…、Frank Rudzicz

- 🎯 **研究动机**：开放权重模型的短时微调即可撤销安全防护，唯一带曲率证书的方法（谱形变）全局膨胀曲率、同时阻碍良性适应
- 🔬 **研究方法**：提出 HarmAlign：沿估计的对比激活子空间做函数保持谱形变，推导子空间能量与有害分布局部曲率下界的有限样本界，并经稳定性-进展二分法转为条件收敛速率控制
- 📌 **结论**：一阶威胁模型下阻断直接微调与三种自适应攻击，良性任务保持可训练，且扩展到意外安全退化与 emergent misalignment

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A short fine-tuning run can undo the safety guards of an open-weight model---retraining a refusal-trained assistant to aid weapons development or produce hate speech. Preventing such harmful fine-tuning while retaining benign adaptability remains difficult: the only prior method with an explicit curvature certificate, spectral deformation, inflates curvature globally and thereby obstructs benign adaptation along with harmful adaptation. We propose HarmAlign, which applies function-preserving spectral deformation along a estimated contrastive activation subspace. We derive finite-sample bounds for the estimated subspace energy and the resulting local harmful-distribution curvature lower bound. A stability--progress dichotomy for constant-step gradient descent turns the certified curvature into conditional convergence-rate control. Empirically, within a fixed-architecture, finite-budget first-order threat model, HarmAlign blocks direct fine-tuning and three data- or objective-adaptive attacks across a hazardous-knowledge relearning setting and a harmful-assistance fine-tuning setting, while the protected benign tasks remain trainable. The block persists across the tested first-order optimizer variants over every attack checkpoint, and under out-of-distribution harmful fine-tuning, and it extends to important cases in our threat model: accidental safety degradation and emergent misalignment.

</details>

### 24. SGT: Securing Open-Source LLMs Against Malicious Fine-tuning via Safety Guidance Trigger

🎓 [Official](https://aclanthology.org/2026.acl-long.463/)　📅 2026-07　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`harmful fine-tuning`、`safety trigger`、`representation distillation`、`safety-preserving fine-tuning`

👤 **作者**：Sunguk Shin、Fangzhao Wu、Byung-Jun Lee、Meeyoung Cha、Sungwon Park

- 🎯 **研究动机**：开源权重 LLM 易被恶意微调侵蚀安全，现有约束参数空间或内部表征的防御仍无法根本缓解该风险
- 🔬 **研究方法**：刻画安全区域并提出 SGT 两阶段：优化安全 trigger 将基座模型导向安全回复，再训练模型使内部特征对齐 trigger 诱导的安全表征，把微调引向安全流形
- 📌 **结论**：对恶意微调的鲁棒性显著提升，攻击者须大幅增加数据预算才能破坏安全，安全区域表征在微调下保持稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight large language models (LLMs) enable broad customization, but also increase exposure to post-release misuse, including malicious fine-tuning (MFT). To mitigate this risk, many prior defenses aim to improve the robustness of open-weight models to MFT by constraining adversarial fine-tuning dynamics in parameter space or mitigating harmful information encoded in internal representations. Nevertheless, since malicious fine-tuning can still erode safety, developing robust safeguards for open-weight models that fundamentally mitigate this risk remains an open research problem. In this paper, we characterize a safety region for open-weight LLMs and propose Safety Guidance Trigger (SGT), which guides fine-tuning toward the safety manifold to preserve alignment. SGT has two stages: (1) optimizing a safety trigger that steers the base model toward safe responses and (2) training the open-weight model to align its internal features with trigger-induced safety representations. We demonstrate that SGT substantially improves robustness against malicious fine-tuning, requiring adversaries to increase their data budget significantly to compromise safety. Our analysis shows that SGT anchors model representations to a safety region, which remains stable under malicious fine-tuning.

</details>

### 25. OASIS: Mitigating Harmful Fine-tuning Attacks on LLMs via Orthogonal and Adaptive Safety Alignment Strategy

🎓 [Official](https://aclanthology.org/2026.acl-long.1310/)　📅 2026-07　🏷 ACL 2026

**关键词**：`defense`、`harmful fine-tuning`、`orthogonal update`、`adaptive layer`、`safety-preserving fine-tuning`、`LLM backdoor`

👤 **作者**：Jiayu Tang、Guowei Peng、Qiuhao Xie、Yuning Yang、Xiurui Xie、Guisong Liu

- 🎯 **研究动机**：对齐阶段防御注入的扰动方向常与有害梯度冲突，反而助长恶意特征获取
- 🔬 **研究方法**：OASIS 把扰动投影到与有害梯度正交，并集中于自适应选择的安全关键层，数学解耦安全执行与有害特征获取
- 📌 **结论**：四个 LLM、三个数据集上 Harmful Score 比竞争基线降约 60%，下游效用稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The “Fine-Tuning-as-a-Service” paradigm exposes large language models to catastrophic safety degradation from less harmful samples. Alignment-stage defenses address this by proactively injecting adversarial perturbations to bolster the model’s inherent robustness against harmful drift. However, existing methods rely on perturbation directions that often conflict with harmful gradients, inadvertently facilitating the acquisition of malicious features rather than suppressing them. To address this issue, we propose Orthogonal and Adaptive Safety Alignment Strategy (OASIS) to mathematically decouple safety enforcement from harmful feature acquisition. By projecting perturbations orthogonal to harmful gradients and concentrating optimization on adaptively selected safety-critical layers, OASIS effectively resolves directional conflicts while maximizing parameter efficiency. Extensive experiments on four LLMs across three datasets (SST2, GSM8K, and AGNews) demonstrate that OASIS reduces the Harmful Score by approximately 60% compared to competitive baselines, while maintaining stable downstream task utility.

</details>

### 26. Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2606.27709)　📅 2026-06

**关键词**：`defense`、`harmful fine-tuning`、`persona conditioning`、`safe response`

👤 **作者**：Austin MY Cheung、Yi Yang

- 🎯 **研究动机**：为社交温度微调会降低事实可靠性、增加谄媚，还可能削弱对抗安全，但可否经数据设计避免未知
- 🔬 **研究方法**：提出人格驱动改写管线：用户轮以低宜人性为条件、助手轮配温暖降温回复，四个模型上三轮实验并以表示探测检验温暖与顺从方向的几何对齐
- 📌 **结论**：相对通用温暖微调基线降低越狱易感性与有害输出率并保留温度；更安全的共情微调可仅靠数据设计实现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We investigate a related but distinct failure mode: warmth fine-tuning also weakens adversarial safety, making models more susceptible to jailbreaks and harmful output generation. We examine whether this reflects an inherent consequence of empathetic adaptation or an artifact of data construction. To address this, we introduce a persona-driven rewriting pipeline that conditions user turns on low agreeableness and pairs this with warm, de-escalating assistant responses. Across three experiments on four models, our approach reduces jailbreak susceptibility and harmful output rates relative to generic warmth fine-tuning baselines, while preserving conversational warmth. Representational probing provides suggestive evidence that this conditioning reduces the geometric alignment between warmth and compliance directions in latent space. These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.

</details>

### 27. Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.24550) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64399)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`harmful fine-tuning`、`temporary jailbreak`、`LoRA`

👤 **作者**：Seokil Ham、Jaehyuk Jang、Wonjun Lee、Changick Kim

- 🎯 **研究动机**：有害微调破坏安全对齐；临时越狱作防御的机制不明
- 🔬 **研究方法**：梯度级分析显示临时越狱饱和安全退化梯度同时保留良性任务梯度；BufferLoRA 以可移除适配器缓冲有害更新，ReinforceLoRA 经 QR 分解合并恢复拒答
- 📌 **结论**：用户微调期间无需额外安全数据、计算成本极小，即可同时获得优越安全性与效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning-as-a-Service (FaaS) enables personalization of large language models (LLMs), but it can weaken safety-alignment under harmful fine-tuning attacks. Recent work has shown that activating harmful-behavior modules during fine-tuning can prevent models from learning undesired behaviors, but its mechanism remains unclear. In this paper, we revisit temporary jailbreaking as a defense against harmful fine-tuning and provide a gradient-level analysis showing that it saturates safety-degrading gradients while preserving benign task-relevant gradients. Based on this insight, we propose a Buffer-and-Reinforce fine-tuning framework that buffers harmful updates during user fine-tuning and reinforces safety after adaptation. Specifically, BufferLoRA induces temporary jailbreaking as a removable adapter to reduce harmful updates during user fine-tuning. After adaptation, ReinforceLoRA, trained to recover refusal behavior under the temporarily jailbroken state, is integrated with UserLoRA via QR decomposition-based merging to reinforce safety while preserving user-task performance. Extensive experiments show that our framework achieves superior safety and utility with no additional safety data during user fine-tuning and minimal computational cost.

</details>

### 28. Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks

📄 [arXiv](https://arxiv.org/abs/2605.05995) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65681)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`harmful fine-tuning`、`safety anchor`、`geometric bottleneck`、`safety alignment`、`empirical evaluation`

👤 **作者**：Guoxin Lu、…、Fu Xiao

- 🎯 **研究动机**：现有抗有害微调防御作用于参数、梯度或表征，攻击者可沿与防御约束正交的优化轨迹恢复有害能力
- 🔬 **研究方法**：SBR 把防御焦点从冗余参数空间移到 unembedding 层这一几何瓶颈，把有害查询的最终隐状态锚定到安全对齐模型
- 📌 **结论**：仅用一个安全锚点即可把 Harmful Score 压到 10 以下，同时良性下游任务保持竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety alignment of Large Language Models (LLMs) remains vulnerable to Harmful Fine-tuning (HFT). While existing defenses impose constraints on parameters, gradients, or internal representations, we observe that they can be effectively circumvented under persistent HFT. Our analysis traces this failure to the inherent redundancy of the high-dimensional parameter space: attackers exploit optimization trajectories that are orthogonal to defense constraints to restore harmful capabilities while deceptively adhering to safety restrictions. To address this, we propose Safety Bottleneck Regularization (SBR). SBR shifts the defensive focus from the redundant parameter space to the unembedding layer, which serves as a geometric bottleneck. By anchoring the final hidden states of harmful queries to those of the safety-aligned model, SBR enables the model to maintain safe responses even under persistent HFT. Extensive experiments confirm SBR's effectiveness, demonstrating that utilizing just a single safety anchor is sufficient to reduce the Harmful Score to $<$10 while preserving competitive performance on benign downstream tasks.

</details>

### 29. RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs

📄 [arXiv](https://arxiv.org/abs/2605.01913) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05　🏷 COLM 2026

**关键词**：`defense`、`harmful fine-tuning`、`refusal geometry`、`representation preservation`、`safety-preserving fine-tuning`、`representation geometry`

👤 **作者**：Sadia Asif、Mohammad Mohammadi Amiri

- 🎯 **研究动机**：标准微调使安全相关表征系统性漂移、几何结构被扭曲并与任务优化相互干扰，导致拒答退化，机制不清
- 🔬 **研究方法**：RefusalGuard 在隐表征空间约束更新，保持安全介导成分稳定而允许任务学习在互补方向进行
- 📌 **结论**：在 LLaMA、Gemma、Qwen 与 AdvBench、JailbreakBench 等基准上 ASR 与原对齐基座相当，任务性能保持竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning safety-aligned language models for downstream tasks often leads to substantial degradation of refusal behavior, making models vulnerable to adversarial misuse. While prior work has shown that safety-relevant features are encoded in structured representations within the model's activation space, how these representations change during fine-tuning and why alignment degrades remains poorly understood. In this work, we investigate the representation-level mechanisms underlying alignment degradation. Our analysis shows that standard fine-tuning induces systematic drift in safety-relevant representations, distorts their geometric structure, and introduces interference between task optimization and safety features. These effects collectively lead to increased harmful compliance. Motivated by these findings, we introduce REFUSALGUARD, a representation-level fine-tuning framework that preserves safety-relevant structure during model adaptation. Our approach constrains updates in hidden representation space, ensuring that safety-mediating components remain stable while allowing task-specific learning in complementary directions. We evaluate REFUSALGUARD across multiple model families, including LLaMA, Gemma, and Qwen, on adversarial safety benchmarks such as AdvBench, DirectHarm4, and JailbreakBench, as well as downstream utility tasks. Our approach achieves attack success rates comparable to base safety-aligned models while maintaining competitive task performance, significantly outperforming baselines.

</details>

### 30. Few Tokens, Big Leverage: Preserving Safety Alignment by Constraining Safety Tokens during Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2603.07445) · 🌐 [Project](https://doi.org/10.1145/3770855.3817837)　📅 2026-03　🏷 KDD 2026

**关键词**：`defense`、`analysis`、`safety-preserving fine-tuning`、`safety-token constraint`、`alignment drift`、`safety token`

👤 **作者**：Guoli Wang、Haonan Shi、Tu Ouyang、An Wang

- 🎯 **研究动机**：即使纯良性数据微调也会引发安全对齐漂移，现有防御靠全局干预限制参数或注入安全数据，损害通用性
- 🔬 **研究方法**：PACT 发现对齐行为集中于少数安全 token 的输出置信度，微调时正则化模型在这些 token 上匹配对齐参考模型，其余 token 不加约束
- 📌 **结论**：在不施加全局限制的情况下防止对齐漂移，避免安全-效用折损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) often require fine-tuning (FT) to perform well on downstream tasks, but FT can induce safety-alignment drift even when the training dataset contains only benign data. Prior work shows that introducing a small fraction of harmful data can substantially compromise LLM refusal behavior, causing LLMs to comply with harmful requests. Existing defense methods often rely on model-wide interventions, such as restricting which parameters are updated or injecting additional safety data, which can limit generality and degrade downstream task performance. To address these limitations, we propose a fine-tuning framework called Preserving Safety Alignment via Constrained Tokens (PACT), which stabilizes the model's confidence on safety tokens. Our approach is motivated by the empirical observation that safety-aligned behavior is reflected in the model's token-level output confidence and is often concentrated on a small subset of safety-related tokens. During downstream fine-tuning, we regularize the fine-tuned model to match the aligned reference model's confidence on safety-related tokens at each response step, while leaving non-safety tokens largely unconstrained to allow effective task adaptation. This targeted constraint prevents alignment drift without imposing global restrictions that typically trade off with model utility. Our code is available at {https://github.com/Glresearch1/PACT}.

</details>

### 31. NeST: Neuron Selective Tuning for LLM Safety

📄 [arXiv](https://arxiv.org/abs/2602.16835)　📅 2026-02

**关键词**：`defense`、`harmful fine-tuning`、`safety neurons`、`selective fine-tuning`

👤 **作者**：Sasha Behrouzi、Lichao Wu、Mohamadreza Rostami、Ahmad-Reza Sadeghi

- 🎯 **研究动机**：全参安全微调成本高，LoRA 安全增益不稳定，推理时干预又不塑造内部安全表示
- 🔬 **研究方法**：NeST 用激活探测定位安全相关前馈神经元，聚类后仅训练簇级共享更新并折回权重，仅用原始恶意提示训练
- 📌 **结论**：14 个模型上平均把越狱 ASR 从 44.5% 降到 1.1%（多模态 55.3%→1.1%，微调变体 53.8%→0.8%），平均仅训 0.4M 参数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is essential for the responsible deployment of Large Language Models (LLMs). Yet, existing approaches often rely on heavyweight fine-tuning that is costly to update, audit, and maintain across model families. Full fine-tuning incurs substantial computational and storage overhead, while parameter-efficient methods, e.g., Low-Rank Adaptation (LoRA), trade efficiency for inconsistent safety gains and sensitivity to design choices. Safety intervention mechanisms reduce unsafe outputs without modifying model weights, but do not directly shape or preserve the internal representations that govern safety behavior. We present NeST, a Neuron-Selective Tuning framework for efficient post-hoc safety alignment. NeST identifies safety-relevant feed-forward neurons via activation probing on vanilla harmful and benign prompts, clusters neurons with similar activation profiles, and trains shared cluster-level updates while freezing the rest of the model. Importantly, NeST is trained only on vanilla malicious prompts, without using jailbreak-specific attack data, yet generalizes robustly to diverse jailbreaks. The learned updates are then folded into the original weights, incurring no inference-time overhead. Evaluated on 14 open-weight language and multimodal models, NeST outperforms lightweight baselines and approaches full fine-tuning robustness with significantly fewer trainable parameters. On text-only models, NeST reduces average jailbreak attack success rate from 44.5% to 1.1% while training only 0.4M parameters on average. Across multimodal settings, it reduces ASR from 55.3% to 1.1%, and for downstream fine-tuned variants, it restores safety by reducing ASR from 53.8% to 0.8%. These results show that robust, maintainable safety alignment can be achieved by concentrating adaptation on localized, functionally coherent safety structures.

</details>

### 32. Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink

📄 [arXiv](https://arxiv.org/abs/2602.05228) · 🌐 [Project](https://anonymous.4open.science/r/Surgery-A69E) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66119)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`harmful fine-tuning`、`attention sink`、`dangerous attention head`、`safety alignment`、`mechanistic analysis`

👤 **作者**：Guozhi Liu、…、Li Shen

- 🎯 **研究动机**：有害微调可瓦解 LLM 安全对齐，缺少作用于微调阶段的轻量防御
- 🔬 **研究方法**：定义注意力头的 sink divergence 并发现其符号可分离有害学习模式；Surgery 以正则把注意力头推向负 divergence 群组来抑制后门习得
- 📌 **结论**：在 BeaverTails、HarmBench、SorryBench 上防御性能分别提升 5.90%、11.25%、9.55%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning can invalidate safety alignment of large language models, exposing significant safety risks. In this paper, we utilize the attention sink mechanism to mitigate harmful fine-tuning. Specifically, we first measure a statistic named \emph{sink divergence} for each attention head and observe that \emph{different attention heads exhibit two different signs of sink divergence}. To understand its safety implications, we conduct experiments and find that the number of attention heads of positive sink divergence increases along with the increase of the model's harmfulness when undergoing harmful fine-tuning. Based on this finding, we propose a separable sink divergence hypothesis -- \emph{attention heads associating with learning harmful patterns during fine-tuning are separable by their sign of sink divergence}. Based on the hypothesis, we propose a fine-tuning-stage defense, dubbed Surgery. Surgery utilizes a regularizer for sink divergence suppression, which steers attention heads toward the negative sink divergence group, thereby reducing the model's tendency to learn and amplify harmful patterns. Extensive experiments demonstrate that Surgery improves defense performance by 5.90\%, 11.25\%, and 9.55\% on the BeaverTails, HarmBench, and SorryBench benchmarks, respectively. Source code is available on https://github.com/Lslland/Surgery.

</details>

### 33. Understanding and Preserving Safety in Fine-Tuned LLMs

📄 [arXiv](https://arxiv.org/abs/2601.10141) · 🌐 [Project](https://zenodo.org/records/21289041) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-01　🏷 ACM CCS 2026

**关键词**：`defense`、`harmful fine-tuning`、`safety mechanism`、`alignment preservation`、`safety-preserving fine-tuning`、`gradient subspace`

👤 **作者**：Jiawen Zhang、…、Ruoxi Jia

- 🎯 **研究动机**：微调防御陷入 safety-utility 两难：重安全损任务性能，深微调保效用却导致安全骤降
- 🔬 **研究方法**：发现安全梯度位于低秩子空间且与更广的效用梯度常负相关、主安全方向可由单样本估计；SPF 在微调中显式移除与安全子空间冲突的梯度分量
- 📌 **结论**：理论上保证效用收敛并界定安全漂移；实验中几乎恢复全部预训练安全对齐，且抗深度微调与动态越狱攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning is an essential and pervasive functionality for applying large language models (LLMs) to downstream tasks. However, it has the potential to substantially degrade safety alignment, e.g., by greatly increasing susceptibility to jailbreak attacks, even when the fine-tuning data is entirely harmless. Despite garnering growing attention in defense efforts during the fine-tuning stage, existing methods struggle with a persistent safety-utility dilemma: emphasizing safety compromises task performance, whereas prioritizing utility typically requires deep fine-tuning that inevitably leads to steep safety declination. In this work, we address this dilemma by shedding new light on the geometric interaction between safety- and utility-oriented gradients in safety-aligned LLMs. Through systematic empirical analysis, we uncover three key insights: (I) safety gradients lie in a low-rank subspace, while utility gradients span a broader high-dimensional space; (II) these subspaces are often negatively correlated, causing directional conflicts during fine-tuning; and (III) the dominant safety direction can be efficiently estimated from a single sample. Building upon these novel insights, we propose safety-preserving fine-tuning (SPF), a lightweight approach that explicitly removes gradient components conflicting with the low-rank safety subspace. Theoretically, we show that SPF guarantees utility convergence while bounding safety drift. Empirically, SPF consistently maintains downstream task performance and recovers nearly all pre-trained safety alignment, even under adversarial fine-tuning scenarios. Furthermore, SPF exhibits robust resistance to both deep fine-tuning and dynamic jailbreak attacks. Together, our findings provide new mechanistic understanding and practical guidance toward always-aligned LLM fine-tuning.

</details>

### 34. Immunizing Models Against Harmful Long-Horizon Fine-Tuning via Contractive Optimization Dynamics

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Sarker_Immunizing_Models_Against_Harmful_Long-Horizon_Fine-Tuning_via_Contractive_Optimization_Dynamics_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`harmful fine-tuning`、`contractive dynamics`、`alignment preservation`

👤 **作者**：Najibul Haque Sarker、Zaber Ibn Abdul Hakim、Ali Asgarov、Chia-Wei Tang、Alvi Md Ishmam、Chris Thomas

- 🎯 **研究动机**：现有免疫方法只模拟短攻击视野，实际攻击者跑数千步更新即可突破
- 🔬 **研究方法**：CLAMP 塑造攻击者优化动态使有害训练局部收缩（每次更新递减），给出超越模拟步数的闭式界，并用 Hessian 免方向曲率罚制造对抗景观
- 📌 **结论**：分类、生成与自回归设定下抵御长程微调，大幅降低有害任务适应且保留良性微调能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning has become the default way to adapt powerful foundation models, but this also enables low-cost repurposing for harmful objectives. Existing immunization methods try to optimize local geometry or simulate short attacker horizons, and penalize observed loss drops. However, in practice, downstream tuners run thousands of updates and overcome these short-horizon defenses.In this paper, we propose CLAMP (Contractive Long-horizon Attacker Mitigation via Progress-bounding), an immunization method that traps harmful fine-tuning by shaping the attacker's optimization dynamics rather than only the initial landscape. Our key idea is to make harmful training locally contractive, making each update smaller than the last. This yields a closed-form bound on the attacker's training beyond the attacker's simulated training steps. We also introduce a Hessian-free directional curvature penalty, to create adversarial landscapes along harmful descent directions. Our bi-level objective minimizes the attacker's predicted improvement from train step zero to infinity. Experiments show our method withstands long-horizon fine-tuning across classification, generative, and autoregressive settings, substantially reduces harmful task adaptation, while preserving benign utility and fine-tuneability.

</details>

### 35. Toward Secure Tuning: Mitigating Security Risks from Instruction Fine-Tuning

🎓 [Official](https://aclanthology.org/2026.acl-long.115/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`harmful fine-tuning`、`robust module`、`staged tuning`、`safety-preserving fine-tuning`、`LLM backdoor`

👤 **作者**：Yanrui Du、…、Bing Qin (秦兵)

- 🎯 **研究动机**：指令微调会破坏 LLM 内置安全机制，现有分训练阶段防御或部署困难、或不稳定且增益有限
- 🔬 **研究方法**：提出 SWAT：分析模块级参数对安全特征空间的影响并识别影响最小的鲁棒模块集 Mods_Rob，先在预热阶段优先训练该集合学低层特征，再标准微调达最优任务性能
- 📌 **结论**：跨知识密集数据集、场景与 LLM 大幅降低安全风险且不牺牲任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction Fine-Tuning (IFT) has emerged as a critical technique for customizing Large Language Models (LLMs) to meet diverse downstream applications. However, recent studies have revealed that IFT can compromise the built-in security mechanisms of LLMs, thereby posing significant security risks. Although defense methods targeting various training stages have been proposed, they either face challenges in practical deployment or exhibit instability and limited performance gains. In our study, we propose a novel SWAT method that introduces a key idea: shifting more of the learning burden onto security-robust parameters. To this end, our study investigates how module-level parameters affect LLMs’ internal security feature space, aiming to uncover robustness patterns in parameters. Guided by this analysis, we identify a robust module set (Mods_Rob) that exhibits minimal effects on LLMs’ security feature space. Leveraging this insight, SWAT proceeds in two phases: (1) a warm-up phase that preferentially trains Mods_Rob to learn low-level features with minimal security risk, followed by (2) standard tuning to achieve optimal task performance. Across diverse knowledge-intensive datasets, scenarios, and LLMs, SWAT substantially reduces security risks without sacrificing task performance gains.

</details>

### 36. Toward Safe Quantization-Aware Fine-tuning: Understanding and Mitigating Safety Alignment Degradation

🎓 [Official](https://icml.cc/virtual/2026/poster/60934)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`quantization-aware fine-tuning`、`safety alignment`、`alignment retention`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Yuning Yang、Guowei Peng、Xiurui Xie、Minrui Jiang、Shuang Liang、Guisong Liu

- 🎯 **研究动机**：可解释性分析发现量化 LLM 在微调时比全精度模型更易发生安全对齐退化，机制不明
- 🔬 **研究方法**：理论揭示量化误差引发初始安全偏移并扭曲优化路径；提出 ExSQF：结合量化误差与安全矩阵投影初始化 adapter 缓解早期偏移，再做训练后精修纠正路径偏差
- 📌 **结论**：安全对齐恢复达 SOTA，甚至超越全精度安全感知微调基线，同时保持下游性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly adapted to downstream tasks in resource-constrained scenarios, making quantization-aware fine-tuning (QAF) a common practice for practical deployment. However, we find that quantized LLMs are substantially more vulnerable to safety alignment degradation during fine-tuning than full-precision models by interpretability analyses. In this paper, we first theoretically reveal that this vulnerability is driven by quantization errors, manifesting as an initial safety shift followed by a distorted optimization path. Based on this insight, we propose Explicit-Safety Quantization-Aware Fine-tuning (ExSQF), which effectively restores model safety while preserving downstream performance. It initializes adapters by combining quantization error with a safety matrix projection to mitigate early safety shifts, followed by post-training refinement that corrects deviations in the optimization path. Extensive experimental results show that ExSQF achieves state-of-the-art safety alignment recovery, even surpassing existing full-precision safety-aware fine-tuning baseline, while effectively preserving model performance.

</details>

### 37. A Guardrail for Safety Preservation: When Safety-Sensitive Subspace Meets Harmful-Resistant Null-Space

📄 [arXiv](https://arxiv.org/abs/2510.14301) · 📝 [OpenReview](https://openreview.net/forum?id=887vde4ZAW) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011231)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`harmful fine-tuning`、`safety subspace`、`null space`

👤 **作者**：Bingjie Zhang、…、Bernard Ghanem

- 🎯 **研究动机**：即使良性数据微调或 LoRA 适配也会轻易破坏预训练模型的安全行为
- 🔬 **研究方法**：GuardSpace 用协方差预条件 SVD 把权重分解为安全相关与无关部分，从后者初始化 adapter 并冻结安全部分，再以零空间投影器限制更新不改变有害 prompt 的拒绝输出
- 📌 **结论**：Llama-2-7B-Chat 微调 GSM8K 时平均 harmful score 从 14.4% 降至 3.6%，准确率从 26.0% 升至 28.0%，优于 AsFT

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have achieved remarkable success in diverse tasks, yet their safety alignment remains fragile during adaptation. Even when fine-tuning on benign data or with low-rank adaptation, pre-trained safety behaviors are easily degraded, leading to harmful responses in the fine-tuned models. To address this challenge, we propose GuardSpace, a guardrail framework for preserving safety alignment throughout fine-tuning, composed of two key components: a safety-sensitive subspace and a harmful-resistant null space. First, we explicitly decompose pre-trained weights into safety-relevant and safety-irrelevant components using covariance-preconditioned singular value decomposition, and initialize low-rank adapters from the safety-irrelevant ones, while freezing safety-relevant components to preserve their associated safety mechanism. Second, we construct a null space projector that restricts adapter updates from altering safe outputs on harmful prompts, thereby maintaining the original refusal behavior. Experiments with various pre-trained models on multiple downstream tasks demonstrate that GuardSpace achieves superior performance over existing methods. Notably, for Llama-2-7B-Chat fine-tuned on GSM8K, GuardSpace outperforms the state-of-the-art method AsFT, reducing the average harmful score from 14.4% to 3.6%, while improving the accuracy from from 26.0% to 28.0%.

</details>

### 38. Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence

📄 [arXiv](https://arxiv.org/abs/2603.00498) · 📝 [OpenReview](https://openreview.net/forum?id=qur2ef8MqQ)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`harmful fine-tuning`、`gradient decay`、`flat loss`

👤 **作者**：Quoc Minh Nguyen、Trung Le、Jing Wu、Anh Tuan Bui、Mehrtash Harandi

- 🎯 **研究动机**：harmful fine-tuning中有害样本梯度会快速主导训练，令防御失效
- 🔬 **研究方法**：Antibody预先将有害损失区域对齐得更平坦，衰减有害梯度影响
- 📌 **结论**：多种攻击强度下防御更稳定且效用保留

### 39. Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment

📄 [arXiv](https://arxiv.org/abs/2509.22745) · 🌐 [Project](https://anonymous.4open.science/r/SafeMoE)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`MoE fine-tuning`、`safety routing`、`expert protection`

👤 **作者**：Jaehan Kim、Minkyoo Song、Seungwon Shin、Sooel Son

- 🎯 **研究动机**：MoE LLM 依赖把有害输入路由到安全专家的浅层机制，微调后路由漂移使其暴露于有害微调，单体防御无效
- 🔬 **研究方法**：提出 SafeMoE：惩罚微调模型与初始对齐模型路由权重的差距，保持有害输入到安全专家的安全路由
- 📌 **结论**：7B-141B MoE 上有效，OLMoE 有害分数从 62.0 降至 5.0，效用损失小于 1%、开销仅 2%，对 gpt-oss 与 Llama 4 同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent large language models (LLMs) have increasingly adopted the Mixture-of-Experts (MoE) architecture for efficiency. MoE-based LLMs heavily depend on a superficial safety mechanism in which harmful inputs are routed safety-critical experts. However, our analysis reveals that routing decisions for harmful inputs drift significantly after fine-tuning, exposing a critical vulnerability to harmful fine-tuning (HFT) attacks. Existing defenses, primarily designed for monolithic LLMs, are less effective for MoE LLMs as they fail to prevent drift in harmful input routing. To address this limitation, we propose SafeMoE, a safe fine-tuning method tailored to MoE LLMs. SafeMoE directly mitigates routing drift by penalizing the gap between the routing weights of a fine-tuned model and those of the initial safety-aligned model, thereby preserving the safety-aligned routing of harmful inputs to safety-critical experts. Experiments on open-source MoE LLMs ranging from 7B to 141B parameters demonstrate that SafeMoE effectively mitigates HFT attacks, reducing the harmfulness score of OLMoE from 62.0 to 5.0, for example, while maintaining task utility within 1% degradation and incurring only 2% overhead. It significantly outperforms state-of-the-art defense methods for safeguarding LLM fine-tuning and remains effective in recent large-scale MoE LLMs such as gpt-oss and Llama 4. Our implementation is available at https://anonymous.4open.science/r/SafeMoE.

</details>

### 40. Token Buncher: Shielding LLMs from Harmful Reinforcement Learning Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2508.20697) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-08　🏷 ACM CCS 2026

**关键词**：`defense`、`harmful RL fine-tuning`、`Token Noiser`、`safety alignment`、`entropy suppression`

👤 **作者**：Weitao Feng、…、Wei Dong

- 🎯 **研究动机**：有害微调研究多假设 SFT，而 RL 在同等算力下能更有效破坏安全对齐
- 🔬 **研究方法**：提出 TokenBuncher：以 entropy-as-reward RL 与 Token Noiser 机制压制 RL 依赖的模型响应熵，阻断有害能力升级
- 📌 **结论**：多模型与 RL 算法上稳健缓解有害 RL 微调，同时保留良性任务性能与可微调性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) continue to grow in capability, so do the risks of harmful misuse through fine-tuning. While most prior studies assume that attackers rely on supervised fine-tuning (SFT) for such misuse, we systematically demonstrate that reinforcement learning (RL) enables adversaries to more effectively break safety alignment and facilitate more advanced harmful task assistance, under matched computational budgets. To counter this emerging threat, we propose TokenBuncher, the first effective defense specifically targeting RL-based harmful fine-tuning. TokenBuncher suppresses the foundation on which RL relies: model response entropy. By constraining entropy, RL-based fine-tuning can no longer exploit distinct reward signals to drive the model toward harmful behaviors. We realize this defense through entropy-as-reward RL and a Token Noiser mechanism designed to prevent the escalation of harmful capabilities. Extensive experiments across multiple models and RL algorithms show that TokenBuncher robustly mitigates harmful RL fine-tuning while preserving benign task performance and finetunability. Our results highlight that RL-based harmful fine-tuning poses a greater systemic risk than SFT, and that TokenBuncher provides an effective and general defense.

</details>

### 41. AsFT: Anchoring Safety During LLM Fine-Tuning Within Narrow Safety Basin

📄 [arXiv](https://arxiv.org/abs/2506.08473) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40729)　📅 2025-06　🏷 AAAI 2026

**关键词**：`defense`、`harmful fine-tuning`、`alignment direction`、`safety basin`

👤 **作者**：Shuo Yang、…、Li Yuan

- 🎯 **研究动机**：微调中与对齐方向正交的扰动会迅速破坏安全，参数空间呈窄安全盆地形态
- 🔬 **研究方法**：提出 AsFT：以对齐与未对齐模型的权重差定义对齐方向，惩罚正交更新把模型锚定在安全盆地内
- 📌 **结论**：有害行为最多降 7.60%、任务性能提升 3.44%，多任务上一致超既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) improves performance but introduces critical safety vulnerabilities: even minimal harmful data can severely compromise safety measures. We observe that perturbations orthogonal to the alignment direction - defined by weight differences between aligned (safe) and unaligned models - rapidly compromise model safety. In contrast, updates along the alignment direction largely preserve it, revealing the parameter space as a "narrow safety basin". To address this, we propose AsFT (Anchoring Safety in Fine-Tuning) to maintain safety by explicitly constraining update directions during fine-tuning. By penalizing updates orthogonal to the alignment direction, AsFT effectively constrains the model within the "narrow safety basin," thus preserving its inherent safety. Extensive experiments on multiple datasets and models show that AsFT reduces harmful behaviors by up to 7.60%, improves task performance by 3.44%, and consistently outperforms existing methods across multiple tasks.

</details>

### 42. CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2505.16559) · 🎓 [Official](https://aclanthology.org/2026.acl-long.455/)　📅 2025-05　🏷 ACL 2026

**关键词**：`defense`、`harmful fine-tuning`、`representation collapse`、`trap defense`、`safety-preserving fine-tuning`、`LLM backdoor`

👤 **作者**：Biao Yi、…、Li Shen

- 🎯 **研究动机**：选择性遗忘可被 LLM 的通用适应性快速再学习绕过，无法根除有害微调
- 🔬 **研究方法**：提出 CTRAP 坍缩陷阱，在对齐时预配置反应：一旦微调持续逆转安全对齐即渐进破坏核心语言建模能力，良性微调时保持休眠
- 📌 **结论**：跨 LLM 与攻击设置有效抵御有害微调，良性场景保持高性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning-as-a-service, while commercially successful for Large Language Model (LLM) providers, exposes models to harmful fine-tuning attacks. As a widely explored defense paradigm against such attacks, unlearning attempts to remove malicious knowledge from LLMs, thereby essentially preventing them from being used to perform malicious tasks. However, we highlight a critical flaw: the powerful general adaptability of LLMs allows them to easily bypass selective unlearning by rapidly relearning or repurposing their capabilities for harmful tasks. To address this fundamental limitation, we propose a paradigm shift: instead of selective removal, we advocate for inducing model collapse--effectively forcing the model to "unlearn everything"--specifically in response to updates characteristic of malicious adaptation. This collapse directly neutralizes the very general capabilities that attackers exploit, tackling the core issue unaddressed by selective unlearning. We introduce the Collapse Trap (CTRAP) as a practical mechanism to implement this concept conditionally. Embedded during alignment, CTRAP pre-configures the model's reaction to subsequent fine-tuning dynamics. If updates during fine-tuning constitute a persistent attempt to reverse safety alignment, the pre-configured trap triggers a progressive degradation of the model's core language modeling abilities, ultimately rendering it inert and useless for the attacker. Crucially, this collapse mechanism remains dormant during benign fine-tuning, ensuring the model's utility and general capabilities are preserved for legitimate users. Extensive empirical results demonstrate that CTRAP effectively counters harmful fine-tuning risks across various LLMs and attack settings, while maintaining high performance in benign scenarios. Our code is available at https://anonymous.4open.science/r/CTRAP.

</details>

### 43. Self-Destructive Language Model

📄 [arXiv](https://arxiv.org/abs/2505.12186) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010675)　📅 2025-05　🏷 ICLR 2026

**关键词**：`defense`、`harmful fine-tuning`、`self-destruct defense`、`capability protection`

👤 **作者**：Yuhui Wang、Rongyi Zhu、Ting Wang

- 🎯 **研究动机**：有害微调防御未解决模型对有害数据的可训练性，更大学习率或数据集的强攻击下即失效
- 🔬 **研究方法**：提出 SEAM，以耦合良性有害优化轨迹的损失与对抗梯度上升使模型被有害数据微调时自毁，并给出 Hessian 免估梯度方法
- 📌 **结论**：低强度攻击下达 SoTA 鲁棒性，高强度攻击下模型性能灾难性崩溃使攻击者无利可图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning attacks pose a major threat to the security of large language models (LLMs), allowing adversaries to compromise safety guardrails with minimal harmful data. While existing defenses attempt to reinforce LLM alignment, they fail to address models' inherent "trainability" on harmful data, leaving them vulnerable to stronger attacks with increased learning rates or larger harmful datasets. To overcome this critical limitation, we introduce SEAM, a novel alignment-enhancing defense that transforms LLMs into self-destructive models with intrinsic resilience to misalignment attempts. Specifically, these models retain their capabilities for legitimate tasks while exhibiting substantial performance degradation when fine-tuned on harmful data. The protection is achieved through a novel loss function that couples the optimization trajectories of benign and harmful data, enhanced with adversarial gradient ascent to amplify the self-destructive effect. To enable practical training, we develop an efficient Hessian-free gradient estimate with theoretical error bounds. Extensive evaluation across LLMs and datasets demonstrates that SEAM creates a no-win situation for adversaries: the self-destructive models achieve state-of-the-art robustness against low-intensity attacks and undergo catastrophic performance collapse under high-intensity attacks, rendering them effectively unusable. The code is available: https://github.com/ZJUWYH/seam. (Warning: this paper contains potentially harmful content generated by LLMs.)

</details>

### 44. SafeMERGE: Preserving Safety Alignment in Fine-Tuned Large Language Models via Selective Layer-Wise Model Merging

📄 [arXiv](https://arxiv.org/abs/2503.17239) · 🌐 [Project](https://research.ibm.com/publications/safemerge-preserving-safety-alignment-in-fine-tuned-large-language-models-via-selective-layer-wise-model-merging)　📅 2025-03　🏷 ICLR 2025

**关键词**：`defense`、`harmful fine-tuning`、`model merging`、`layer selection`

👤 **作者**：Aladin Djuhera、Swanand Ravindra Kadhe、Farhan Ahmed、Syed Zawad、Holger Boche

- 🎯 **研究动机**：微调会侵蚀 LLM 安全对齐，已有再对齐方法难实现或损害任务效用
- 🔬 **研究方法**：提出 SafeMERGE，以余弦相似度衡量层行为与安全性的偏离，仅对偏离层执行与安全对齐模型的层间合并
- 📌 **结论**：四个 LLM 与多任务上一致减少有害输出，效用几乎无损甚至提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) is a common practice to adapt generalist models to specialized domains. However, recent studies show that fine-tuning can erode safety alignment, causing LLMs to respond to harmful or unethical prompts. Many methods to realign safety have been proposed, but often introduce custom algorithms that are difficult to implement or compromise task utility. In this work, we propose SafeMERGE, a lightweight, post-fine-tuning framework that restores safety while maintaining downstream performance. SafeMERGE selectively merges fine-tuned with safety-aligned model layers only when they deviate from safe behavior, measured by a cosine similarity criterion. Across four LLMs and several tasks, SafeMERGE consistently reduces harmful outputs compared to other defenses, with negligible or even positive impact on utility. Our results demonstrate that selective, layer-wise merging offers a robust safeguard against the inadvertent loss of safety during fine-tuning, establishing SafeMERGE as a simple yet effective post-fine-tuning defense.

</details>

### 45. Panacea: Mitigating Harmful Fine-tuning for Large Language Models via Post-fine-tuning Perturbation

📄 [arXiv](https://arxiv.org/abs/2501.18100) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f827f8acffaa3ce6799fbabd10fba1c1-Abstract-Conference.html)　📅 2025-01　🏷 NeurIPS 2025

**关键词**：`defense`、`post-fine-tuning repair`、`adaptive perturbation`、`safety affinity`

👤 **作者**：Yibo Wang、…、Dacheng Tao

- 🎯 **研究动机**：预免疫式防御脆弱，几步微调后模型仍能学到有害知识
- 🔬 **研究方法**：发现纯随机扰动即可恢复安全但损微调性能；Panacea 优化微调后施加的自适应扰动
- 📌 **结论**：平均有害分数最多降 21.2% 且保持微调性能，并揭示各层安全亲和性差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning attack introduces significant security risks to the fine-tuning services. Main-stream defenses aim to vaccinate the model such that the later harmful fine-tuning attack is less effective. However, our evaluation results show that such defenses are fragile--with a few fine-tuning steps, the model still can learn the harmful knowledge. To this end, we do further experiment and find that an embarrassingly simple solution--adding purely random perturbations to the fine-tuned model, can recover the model from harmful behaviors, though it leads to a degradation in the model's fine-tuning performance. To address the degradation of fine-tuning performance, we further propose Panacea, which optimizes an adaptive perturbation that will be applied to the model after fine-tuning. Panacea maintains model's safety alignment performance without compromising downstream fine-tuning performance. Comprehensive experiments are conducted on different harmful ratios, fine-tuning tasks and mainstream LLMs, where the average harmful scores are reduced by up-to 21.2%, while maintaining fine-tuning performance. As a by-product, we analyze the adaptive perturbation and show that different layers in various LLMs have distinct safety affinity, which coincide with finding from several previous study. Source code available at https://github.com/w-yibo/Panacea.

</details>

### 46. NLSR: Neuron-Level Safety Realignment of Large Language Models Against Harmful Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2412.12497)　📅 2024-12

**关键词**：`defense`、`post-fine-tuning repair`、`safety-critical neuron`、`patch transplantation`

👤 **作者**：Xin Yi、Shunfan Zheng、Linlin Wang、Gerard de Melo、Xiaoling Wang、Liang He

- 🎯 **研究动机**：现有抗有害微调方法需大量算力，即使 LoRA 也离不开梯度更新
- 🔬 **研究方法**：NLSR 免训练：从对齐模型构建安全参考模型定位安全关键神经元制成补丁，微调后仅移植相似度差异显著的神经元
- 📌 **结论**：多下游任务上显著恢复安全且基本保持任务准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of finetuning-as-a-service has revealed a new vulnerability in large language models (LLMs). A mere handful of malicious data uploaded by users can subtly manipulate the finetuning process, resulting in an alignment-broken model. Existing methods to counteract fine-tuning attacks typically require substantial computational resources. Even with parameter-efficient techniques like LoRA, gradient updates remain essential. To address these challenges, we propose \textbf{N}euron-\textbf{L}evel \textbf{S}afety \textbf{R}ealignment (\textbf{NLSR}), a training-free framework that restores the safety of LLMs based on the similarity difference of safety-critical neurons before and after fine-tuning. The core of our framework is first to construct a safety reference model from an initially aligned model to amplify safety-related features in neurons. We then utilize this reference model to identify safety-critical neurons, which we prepare as patches. Finally, we selectively restore only those neurons that exhibit significant similarity differences by transplanting these prepared patches, thereby minimally altering the fine-tuned model. Extensive experiments demonstrate significant safety enhancements in fine-tuned models across multiple downstream tasks, while greatly maintaining task-level accuracy. Our findings suggest regions of some safety-critical neurons show noticeable differences after fine-tuning, which can be effectively corrected by transplanting neurons from the reference model without requiring additional training. The code will be available at \url{https://github.com/xinykou/NLSR}

</details>

### 47. Targeted Vaccine: Safety Alignment for Large Language Models against Harmful Fine-Tuning via Layer-wise Perturbation

📄 [arXiv](https://arxiv.org/abs/2410.09760)　📅 2024-10

**关键词**：`defense`、`alignment-stage defense`、`safety-critical layer`、`targeted perturbation`

👤 **作者**：Guozhi Liu、Weiwei Lin、Tiansheng Huang、Ruichao Mo、Qi Mu、Li Shen

- 🎯 **研究动机**：Vaccine 对所有层统一扰动，对安全无关层过度扰动且显存开销大
- 🔬 **研究方法**：T-Vaccine 用梯度范数识别安全关键层，仅对这些层施加扰动、其余层冻结训练
- 📌 **结论**：防御效果与资源效率均超 Vaccine 并优于 RepNoise、TAR；首个可在 RTX 4090 上为 7B 模型防御的方案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning attack poses a serious threat to the online fine-tuning service. Vaccine, a recent alignment-stage defense, applies uniform perturbation to all layers of embedding to make the model robust to the simulated embedding drift. However, applying layer-wise uniform perturbation may lead to excess perturbations for some particular safety-irrelevant layers, resulting in defense performance degradation and unnecessary memory consumption. To address this limitation, we propose Targeted Vaccine (T-Vaccine), a memory-efficient safety alignment method that applies perturbation to only selected layers of the model. T-Vaccine follows two core steps: First, it uses gradient norm as a statistical metric to identify the safety-critical layers. Second, instead of applying uniform perturbation across all layers, T-Vaccine only applies perturbation to the safety-critical layers while keeping other layers frozen during training. Results show that T-Vaccine outperforms Vaccine in terms of both defense effectiveness and resource efficiency. Comparison with other defense baselines, e.g., RepNoise and TAR also demonstrate the superiority of T-Vaccine. Notably, T-Vaccine is the first defense that can address harmful fine-tuning issues for a 7B pre-trained models trained on consumer GPUs with limited memory (e.g., RTX 4090). Our code is available at https://github.com/Lslland/T-Vaccine.

</details>

### 48. Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation

📄 [arXiv](https://arxiv.org/abs/2409.01586)　📅 2024-09

**关键词**：`defense`、`alignment-stage defense`、`harmful perturbation`、`loss regularization`

👤 **作者**：Tiansheng Huang、Sihao Hu、Fatih Ilhan、Selim Furkan Tekin、Ling Liu

- 🎯 **研究动机**：有害微调防御效果不佳，根因未明；发现有害权重扰动是大概率成因
- 🔬 **研究方法**：Booster 在对齐阶段的优化中追加正则项，削弱模拟有害扰动后的有害损失下降
- 📌 **结论**：有效降低微调后模型有害分数且保持下游任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning attack poses serious safety concerns for large language models' fine-tuning-as-a-service. While existing defenses have been proposed to mitigate the issue, their performances are still far away from satisfactory, and the root cause of the problem has not been fully recovered. To this end, we in this paper show that harmful perturbation over the model weights could be a probable cause of alignment-broken. In order to attenuate the negative impact of harmful perturbation, we propose an alignment-stage solution, dubbed Booster. Technically, along with the original alignment loss, we append a loss regularizer in the alignment stage's optimization. The regularizer ensures that the model's harmful loss reduction after the simulated harmful perturbation is attenuated, thereby mitigating the subsequent fine-tuning risk. Empirical results show that Booster can effectively reduce the harmful score of the fine-tuned models while maintaining the performance of downstream tasks. Our code is available at https://github.com/git-disl/Booster.

</details>

### 49. Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack

📄 [arXiv](https://arxiv.org/abs/2408.09600) · 🌐 [Project](https://proceedings.mlr.press/v267/huang25b.html)　📅 2024-08　🏷 ICML 2025

**关键词**：`defense`、`post-fine-tuning repair`、`parameter pruning`、`hyperparameter agnostic`

👤 **作者**：Tiansheng Huang、Gautam Bhattacharya、Pratik Joshi、Josh Kimball、Ling Liu

- 🎯 **研究动机**：已有有害微调防御在大学习率或长训练轮数下即失效
- 🔬 **研究方法**：Antidote 在微调后一次性剪枝，移除负责有害内容生成的权重，与微调超参无关
- 📌 **结论**：降低有害分数同时保持下游任务准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety aligned Large Language Models (LLMs) are vulnerable to harmful fine-tuning attacks -- a few harmful data mixed in the fine-tuning dataset can break the LLMs's safety alignment. While several defenses have been proposed, our evaluation shows that existing defenses fail \textit{when some specific training hyper-parameters are chosen} -- a large learning rate or a large number of training epochs in the fine-tuning stage can easily invalidate the defense. To this end, we propose Antidote, a post-fine-tuning stage solution, which remains \textbf{\textit{agnostic to the training hyper-parameters in the fine-tuning stage}}. Antidote relies on the philosophy that by removing the harmful parameters, the harmful model can be recovered from the harmful behaviors, regardless of how those harmful parameters are formed in the fine-tuning stage. With this philosophy, we introduce a one-shot pruning stage after harmful fine-tuning to remove the harmful weights that are responsible for the generation of harmful content. Despite its embarrassing simplicity, empirical results show that Antidote can reduce harmful score while maintaining accuracy on downstream tasks. Code is available at https://github.com/git-disl/Antidote.

</details>

### 50. Lisa: Lazy Safety Alignment for Large Language Models against Harmful Fine-tuning Attack

📄 [arXiv](https://arxiv.org/abs/2405.18641) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/bcfdaf04b54a69f47623c973c864ee8d-Abstract-Conference.html)　📅 2024-05　🏷 NeurIPS 2024

**关键词**：`defense`、`bi-state optimization`、`proximal regularization`、`alignment retention`

👤 **作者**：Tiansheng Huang、Sihao Hu、Fatih Ilhan、Selim Furkan Tekin、Ling Liu

- 🎯 **研究动机**：有害数据微调可破坏对齐，而简单双状态优化在对齐步数少时收敛不稳定
- 🔬 **研究方法**：统计分析定位 excess drift 为不稳定主因；Lisa 引入近端项约束各状态漂移，理论上需足够大的近端因子保证收敛
- 📌 **结论**：四个下游微调任务上显著提升对齐保持且不损用户任务准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies show that Large Language Models (LLMs) with safety alignment can be jail-broken by fine-tuning on a dataset mixed with harmful data. First time in the literature, we show that the jail-broken effect can be mitigated by separating states in the finetuning stage to optimize the alignment and user datasets. Unfortunately, our subsequent study shows that this simple Bi-State Optimization (BSO) solution experiences convergence instability when steps invested in its alignment state is too small, leading to downgraded alignment performance. By statistical analysis, we show that the \textit{excess drift} towards consensus could be a probable reason for the instability. To remedy this issue, we propose \textbf{L}azy(\textbf{i}) \textbf{s}afety \textbf{a}lignment (\textbf{Lisa}), which introduces a proximal term to constraint the drift of each state. Theoretically, the benefit of the proximal term is supported by the convergence analysis, wherein we show that a sufficient large proximal factor is necessary to guarantee Lisa's convergence. Empirically, our results on four downstream finetuning tasks show that Lisa with a proximal term can significantly increase alignment performance while maintaining the LLM's accuracy on the user tasks. Code is available at \url{https://github.com/git-disl/Lisa}.

</details>

### 51. Representation Noising: A Defence Mechanism Against Harmful Finetuning

📄 [arXiv](https://arxiv.org/abs/2405.14577) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/172be8b0b88fc2b4aee74237d43f8c04-Abstract-Conference.html)　📅 2024-05　🏷 NeurIPS 2024

**关键词**：`defense`、`representation noising`、`harmful representation`、`open-weight safeguard`、`open-weight safeguards`、`harmful fine-tuning`

👤 **作者**：Domenic Rosati、…、Frank Rudzicz

- 🎯 **研究动机**：开放权重与微调 API 使模型暴露于 harmful fine-tuning，安全措施可被微调轻易逆转
- 🔬 **研究方法**：RepNoise 移除有害表示信息使微调后难以恢复，并可泛化到同分布的未见伤害子集
- 📌 **结论**：不损通用能力与良性可训练性；效力取决于跨层移除深度，跨分布攻击仍是盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Releasing open-source large language models (LLMs) presents a dual-use risk since bad actors can easily fine-tune these models for harmful purposes. Even without the open release of weights, weight stealing and fine-tuning APIs make closed models vulnerable to harmful fine-tuning attacks (HFAs). While safety measures like preventing jailbreaks and improving safety guardrails are important, such measures can easily be reversed through fine-tuning. In this work, we propose Representation Noising (RepNoise), a defence mechanism that operates even when attackers have access to the weights. RepNoise works by removing information about harmful representations such that it is difficult to recover them during fine-tuning. Importantly, our defence is also able to generalize across different subsets of harm that have not been seen during the defence process as long as they are drawn from the same distribution of the attack set. Our method does not degrade the general capability of LLMs and retains the ability to train the model on harmless tasks. We provide empirical evidence that the efficacy of our defence lies in its ``depth'': the degree to which information about harmful representations is removed across all layers of the LLM. We also find areas where RepNoise still remains ineffective and highlight how those limitations can inform future research.

</details>

### 52. Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack

📄 [arXiv](https://arxiv.org/abs/2402.01109) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/873c86d9a979ab80d8e2919510d4446b-Abstract-Conference.html)　📅 2024-02　🏷 NeurIPS 2024

**关键词**：`defense`、`alignment-stage defense`、`embedding drift`、`perturbation-aware training`

👤 **作者**：Tiansheng Huang、Sihao Hu、Ling Liu

- 🎯 **研究动机**：finetuning-as-a-service 中少量有害数据即可破坏对齐，实证发现 harmful embedding drift 现象
- 🔬 **研究方法**：Vaccine 在对齐阶段对隐藏嵌入渐进施加扰动做 perturbation-aware 训练，使其对微调期有害扰动不变
- 📌 **结论**：Llama2、OPT、Vicuna 上提升对齐对有害扰动的鲁棒性并保留良性推理能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The new paradigm of finetuning-as-a-service introduces a new attack surface for Large Language Models (LLMs): a few harmful data uploaded by users can easily trick the finetuning to produce an alignment-broken model. We conduct an empirical analysis and uncover a \textit{harmful embedding drift} phenomenon, showing a probable cause of the alignment-broken effect. Inspired by our findings, we propose Vaccine, a perturbation-aware alignment technique to mitigate the security risk of users finetuning. The core idea of Vaccine is to produce invariant hidden embeddings by progressively adding crafted perturbation to them in the alignment phase. This enables the embeddings to withstand harmful perturbation from un-sanitized user data in the finetuning phase. Our results on open source mainstream LLMs (e.g., Llama2, Opt, Vicuna) demonstrate that Vaccine can boost the robustness of alignment against harmful prompts induced embedding drift while reserving reasoning ability towards benign prompts. Our code is available at \url{https://github.com/git-disl/Vaccine}.

</details>

### 53. Beyond Token-Level Guidance: Inference-Time Alignment of Specialized LLMs via Cross-Family Representation Steering

📄 [arXiv](https://arxiv.org/abs/2608.30319)　📅 2026-09

**关键词**：`defense`、`post-fine-tuning repair`、`cross-family representation`、`domain-utility retention`、`cross-family steering`、`safety direction`

👤 **作者**：Jin Gan、Xin Li、Jun Luo

- 🎯 **研究动机**：专业化微调削弱安全，现有推理时 token 级引导因跨模型能力正交产生 stop token 干扰、损伤领域能力
- 🔬 **研究方法**：提出 CREST：从任意家族 guidance model 提取安全方向并在 base model 隐表示上 steering，完全绕开 token 级结构限制
- 📌 **结论**：在专业化削弱安全的场景恢复安全并保留领域能力与已对齐模型的安全性，安全基准上最高超基线 22.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) finetuned for specialized domains represent crucial high-impact applications. Inference-time alignment improves safety degraded from specialization finetuning without requiring substantial computational resources, complementing finetuning-based methods with an easy-to-use, plug-and-play solution. However, existing inference-time methods fail to reliably improve safety without disrupting domain capability. We identify the root cause as complementary expertise orthogonality: specialized base models and general-domain guidance models have orthogonal competencies, making the guidance signal unreliable for specialized generation. This primarily manifests as stop token interference, where the guidance model's tendency toward continuation overrides the base model's decision to stop, burying correct answers under guidance-induced continuation. To address this problem, we propose CREST, an inference-time alignment method that steers base model hidden representations using safety directions extracted from a guidance model of any family, avoiding token-level structural limitations entirely. CREST improves safety where specialization has weakened it while preserving both domain-specific capability and the safety of already well-aligned models, outperforming baselines by up to 22.2\% on safety benchmarks. Our code is available at: https://github.com/DecayingSeart/CREST.

</details>

### 54. Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2607.23394)　📅 2026-07

**关键词**：`defense`、`harmful fine-tuning`、`hidden behavior`、`consensus decoding`、`subliminal learning`、`source-specific behavior`

👤 **作者**：Adhyyan Narang、Artin Tajdini、Claire Zhang、Jamie Morgenstern

- 🎯 **研究动机**：少量投毒或隐性偏好数据即可安装定向不良行为，标准防御（过滤、混入无害数据、正则）只能衰减不能消除
- 🔬 **研究方法**：用冗余换鲁棒：每个数据源单独微调参照模型，解码时聚合 next-token 分布；提出 token 级最小值与 base 相对两种共识解码器，并放宽精确一致以容忍部分支持与表面差异
- 📌 **结论**：在受控投毒、subliminal learning 与 emergent misalignment 上压制来源特有不良行为并保留共有良性能力，优于联合训练与权重平均

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly. Standard defenses, such as data filtering, mixing in harmless data, and regularization, attenuate these effects but do not eliminate them. We instead pursue robustness through redundancy: collecting multiple datasets from different sources and only learning what is common between them. Thus, if only a subset of sources are malicious, the misbehavior will be blocked. In order to implement this defense strategy, we fine-tune a separate reference model on each source's dataset and aggregate their next-token distributions at decoding time. We introduce two consensus decoders: a token-wise minimum, which caps each token at the lowest probability any source assigns, and a base-relative variant, which reverts to the base probability on any token the sources move in opposing directions. We further relax exact agreement to tolerate partial support across sources and different surface expressions of the same intention. Across controlled poisoning tasks, subliminal learning, and emergent misalignment, consensus decoding suppresses source-specific misbehavior while preserving shared desirable behavior, including cases where union training and weight averaging retain the unwanted behavior.

</details>

### 55. Diff Mining: Logit Differences Reveal Finetuning Objectives

📄 [arXiv](https://arxiv.org/abs/2608.26462) · 🎓 [Official](https://iclr.cc/virtual/2026/10019308)　📅 2026-08

**关键词**：`detection`、`analysis`、`finetuning-objective audit`、`logit difference`、`hidden bias`、`finetuning fingerprint`

👤 **作者**：Greg Kocher、Robert West、Clément Dumas、Julian Minder

- 🎯 **研究动机**：微调可能涌现不良行为，而现有 model diffing 常需模型内部访问且难识别具体目标
- 🔬 **研究方法**：Diff Mining 比较微调与基模型的 logit 差异，经 Top-K 频率或 NMF 聚合成可解释 token 集，仅需输出 logit
- 📌 **结论**：微调域检测显著优于 SOTA diffing；对注入偏差模型无需定向 probe 即识别超三分之一

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing its logits to those of its base model. Diff Mining effectively surfaces salient tokens that are amplified in the finetuned model, serving as a fingerprint of its training -- even on text unrelated to the finetuning domain. Unlike many existing model diffing methods which require model internals, Diff Mining only needs access to output logits and scales to large models. The framework consists of two modular stages: (i) extracting per-context logit differences between the finetuned and base models on a reference corpus, and (ii) aggregating the resulting signals to construct an interpretable token set representing the finetune. For aggregation, we explore both a simple Top-K frequency method and a Non-negative Matrix Factorization (NMF)-based approach for disentangling multiple finetuning objectives into distinct token clusters. Empirically, Diff Mining succeeds across diverse settings: on finetune domain detection, it significantly outperforms state-of-the-art model diffing methods both in identifying relevant tokens and in downstream performance when an interpretability agent is given access to the extracted token set; on models with injected biases, it identifies more than one third of the biases without targeted probing. Overall, our framework shows promise in developing auditing tools to detect finetuning objectives.

</details>

### 56. Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers

📄 [arXiv](https://arxiv.org/abs/2608.14089)　📅 2026-08

**关键词**：`detection`、`defense`、`safety-classifier adaptation`、`policy mismatch`、`drift monitoring`、`classifier adaptation`

👤 **作者**：Thiago Sandoval、Ufuk Topcu

- 🎯 **研究动机**：安全分类器决策反映训练学到的策略而非部署者策略，且随部署流量演化而退化
- 🔬 **研究方法**：RCV 轻量包装器从分类器内部表征估计每个预测与部署者策略不一致的概率并选择性纠正；同一估计提供无标签分布漂移检测
- 📌 **结论**：三个现成分类器×两基准全部改善策略遵循，不改分类器补上至多 0.81 此前漏检的不安全内容；十次保留攻击战役全部检出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees with the deployer's policy, and selectively corrects predictions likely to be wrong. The same correctness estimates also provide a label-free signal for detecting distribution shift, enabling a maintenance loop that updates the correctness estimation layer and resorts to classifier fine-tuning only when necessary. Across three off-the-shelf safety classifiers and two benchmark datasets, RCV improves adherence to the deployer's policy in every classifier-dataset combination, catching up to 0.81 of previously missed unsafe content without modifying the underlying classifier. In a deployment study with ten attack campaigns, each a harm category held out of RCV's training, RCV detects every campaign in a dedicated injection panel; in the maintenance census most drift episodes are repaired without updating the classifier, and the fine-tune is reserved for the residual episodes that repair does not restore.

</details>

### 57. Detecting Safety Training Modification in Language Models via Activation Analysis

📄 [arXiv](https://arxiv.org/abs/2608.05578) · 🌐 [Project](https://doi.org/10.1109/ACCESS.2026.3704057)　📅 2026-08

**关键词**：`detection`、`activation scanner`、`safety modification`、`refusal geometry`

👤 **作者**：Glen Messenger

- 🎯 **研究动机**：检测语言模型的安全训练是否被移除或消融（abliterated/uncensored）缺乏可用工具
- 🔬 **研究方法**：AMS 测量激活空间中有害/良性概念几何分离度与拒答方向，双层阈值加方向相似度校验，跨 14 个模型配置、四类安全修改验证
- 📌 **结论**：留一交叉验证准确率 71%；sigma 与越狱合规相关 r=-0.546；训练移除与权重正交化可检出，行为微调类修改不可检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce AMS (Activation-based Model Scanner), a tool that detects modifications to safety training in language models by measuring the geometric structure of safety-relevant concepts in activation space. Safety training creates measurable separation between harmful and benign content classes; certain safety modifications collapse or rotate this structure, while others leave it intact. We validate AMS across 14 model configurations spanning 4 architecture families (Llama, Gemma, Qwen, Mistral) and four safety-modification categories (instruction-tuned, base, abliterated, uncensored fine-tunes). Leave-one-out cross-validation of thresholds achieves 71% accuracy (10/14); bootstrap 95% confidence intervals on sigma point estimates have median width 3.4 sigma. We measure behavioral compliance on 20 stratified JailbreakBench prompts per model and find that sigma on the harmful-content concept predicts compliance with Pearson r = -0.546 (p = 0.043), directionally but with meaningful noise. Mechanistic analysis identifies a four-class taxonomy of safety-training modifications distinguished by activation-space signature: training removal collapses cluster separation; weight-orthogonalization abliteration both collapses separation and rotates the refusal direction; rotation-without-collapse abliteration preserves separation while rotating direction; and behavioral fine-tuning preserves both magnitude and direction. AMS's Tier 1 sigma-threshold detects the first two classes; Tier 2 direction-similarity verification detects the third. The fourth is undetectable by activation-only probing and represents a documented failure mode. We discuss threshold calibration, limitations of single-run measurement, and the open problem of detecting behavioral-only safety modifications.

</details>

### 58. Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2608.04347)　📅 2026-08

**关键词**：`detection`、`side-effect introspection`、`activation difference`、`alignment drift`

👤 **作者**：Kotaro Yoshida、Laura Gomezjurado Gonzalez、Yukinori Yamamoto、Yuji Naraki、Ryotaro Shimizu、Wenya Wang

- 🎯 **研究动机**：内省适配器研究局限于显式植入的行为，微调副作用导致的非预期对齐漂移无法被内省
- 🔬 **研究方法**：形式化副作用内省问题并构建数据集；DAIA 显式处理基座激活与微调引起的激活差分以增强对内部变化的敏感度
- 📌 **结论**：内省学习可泛化到未见微调模型与安全类别，DAIA 一致优于现有内省适配器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning enables a source model to acquire desired capabilities and behaviors in a target domain while retaining much of its general-purpose competence. However, this adaptation process can also degrade alignment properties that were present in the source model. Recent work has shown that large language models can be trained using LoRA-based modules known as introspection adapters (IAs) to describe behavioral changes induced by fine-tuning. However, existing studies primarily consider settings in which the model is fine-tuned on datasets explicitly designed to implant a specific behavior and is then asked to explain the implanted behavior. This differs from practical deployment scenarios, where the central concern is often side-effect misalignment: unintended degradation of alignment caused by fine-tuning on tasks that are not obviously related to safety or alignment. To bridge this gap, we formulate a novel problem setting called \emph{side-effect introspection}, in which the target of introspection is not a behavior explicitly implanted through fine-tuning, but rather alignment shifts that emerge as unintended side effects, and we construct a dataset for this setting. Furthermore, to enhance sensitivity to internal model changes, we propose the Delta-Aware Introspection Adapter (DAIA), a novel mechanism designed to explicitly process both base-model activations and activation differences induced by fine-tuning. Our empirical evaluation shows that introspection learning generalizes to unseen fine-tuned models and safety categories, and that DAIA consistently outperforms existing introspection adapters.

</details>

### 59. Detecting Adversarial Fine-tuning with Auditing Agents

📄 [arXiv](https://arxiv.org/abs/2510.16255)　📅 2025-10

**关键词**：`detection`、`fine-tuning API`、`auditing agent`、`covert attack`

👤 **作者**：Sarah Egler、John Schulman、Nicholas Carlini

- 🎯 **研究动机**：微调 API 可被用于绕过安全防护，仅隐式有害的数据集可逃避内容审核检测
- 🔬 **研究方法**：提出微调审计 agent 概念，允许其访问微调数据集与前后模型并输出风险分，在 8 种强攻击与 5 个良性微调上完成 1400 余次审计
- 📌 **结论**：最优配置下以 1% 假阳性率检出 56.2% 对抗微调，并能发现逃避内容审核的 covert cipher 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) providers expose fine-tuning APIs that let end users fine-tune their frontier LLMs. Unfortunately, it has been shown that an adversary with fine-tuning access to an LLM can bypass safeguards. Particularly concerning, such attacks may avoid detection with datasets that are only implicitly harmful. Our work studies robust detection mechanisms for adversarial use of fine-tuning APIs. We introduce the concept of a fine-tuning auditing agent and show it can detect harmful fine-tuning prior to model deployment. We provide our auditing agent with access to the fine-tuning dataset, as well as the fine-tuned and pre-fine-tuned models, and request the agent assigns a risk score for the fine-tuning job. We evaluate our detection approach on a diverse set of eight strong fine-tuning attacks from the literature, along with five benign fine-tuned models, totaling over 1400 independent audits. These attacks are undetectable with basic content moderation on the dataset, highlighting the challenge of the task. With the best set of affordances, our auditing agent achieves a 56.2% detection rate of adversarial fine-tuning at a 1% false positive rate. Most promising, the auditor is able to detect covert cipher attacks that evade safety evaluations and content moderation of the dataset. While benign fine-tuning with unintentional subtle safety degradation remains a challenge, we establish a baseline configuration for further work in this area. We release our auditing agent at https://github.com/safety-research/finetuning-auditor.

</details>

## 综评与基准

### 60. Beyond Safe Data: Pretraining-Stage Alignment with Regular Safety Reflection

📄 [arXiv](https://arxiv.org/abs/2606.19168)　📅 2026-06

**关键词**：`analysis`、`safety alignment`、`fine-tuning data`、`risk filtering`

👤 **作者**：Jinhan Li、Kexian Tang、Yihan Xu、Zhuorui Ye、Kaifeng Lyu

- 🎯 **研究动机**：预训练阶段对齐研究集中于过滤或改写不安全数据，但 LLM 可把看似安全的知识组合成不安全行为
- 🔬 **研究方法**：提出 Safety Reflection Pretraining：在预训练语料中定期插入简短安全反思，把自我监控直接融入语言建模，并以合成环境 MedSafetyWorld 做受控验证
- 📌 **结论**：1.7B 模型（FineWeb-Edu 预训练）上提升安全分类准确率、显著降低推理期与微调攻击成功率，优于数据过滤与改写

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To achieve deeper safety alignment for large language models (LLMs), recent efforts have studied how to push safety interventions earlier into the pretraining stage, primarily by filtering unsafe data or rewriting it into safer forms. We argue that pretraining-stage alignment should go beyond making the data safe: LLMs may compose seemingly benign knowledge and capabilities into unsafe behaviors. To this end, we propose Safety Reflection Pretraining, a pretraining-stage alignment method which regularly inserts short safety reflections into pretraining corpora to integrate self-monitoring directly into language modeling, establishing a foundational capability that is subsequently reinforced by compatible post-training. Our experiments with 1.7B models pretrained on FineWeb-Edu show that Safety Reflection Pretraining improves safety classification accuracy and substantially reduces the success rates of inference-stage and finetuning attacks. Complementary to our real-world experiments, we also introduce a fully controlled synthetic environment, MedSafetyWorld, with a clear definition of safety and a reasoning structure under which models can easily generalize unsafe behaviors from safe data. Ablations in MedSafetyWorld further demonstrate a clear advantage of Safety Reflection Pretraining in preventing models from acting on unsafe behaviors generalized from safe data, compared with data filtering and rewriting. Taken together, our findings suggest that pretraining alignment should not only make the training data safe, but also shape the behaviors that models are likely to acquire from safe data.

</details>

### 61. When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2609.01455)　📅 2026-09

**关键词**：`analysis`、`benign fine-tuning`、`safety routing`、`Fisher geometry`、`alignment fragility`

👤 **作者**：Yitong Guo、Xiaoyi Chen、Siyuan Zhang、Xiaofeng Wang、Haixu Tang

- 🎯 **研究动机**：良性微调即可严重削弱 LLM 安全对齐，但拒答行为为何如此脆弱缺少机制解释
- 🔬 **研究方法**：提出 Fisher 几何解释：safety Fisher 低秩，对齐使安全几何变平但保留输出路由通路；100 条良性样本即选择性地在输出侧 MLP 重新锐化该通路
- 📌 **结论**：该视图解释安全可崩到高 ASR 而通用能力仅轻损、少量安全样本即可恢复拒答；LoRA 与 ASAM 抑制输出侧锐化可延缓崩溃但在更大微调规模下失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules, explaining the asymmetric fragility: safety can collapse to high attack success rates, while general utility degrades mildly. The routing view also explains why few safety examples can restore refusal behavior, indicating that internal safety-relevant representations are preserved. Finally, we show that LoRA and ASAM mitigate early collapse by suppressing output-side sharpness, but their protection weakens at larger fine-tuning scales. Overall, safety failure is best understood as a disruption of a low-rank output-routing mechanism

</details>

### 62. Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable

📄 [arXiv](https://arxiv.org/abs/2608.26958)　📅 2026-08

**关键词**：`analysis`、`benign fine-tuning`、`latent behavior transfer`、`synthetic data`、`subliminal learning`、`distillation scaling`

👤 **作者**：Zhichen Dong、Zhixuan Liu、Yuyu Fan、Xiangtian Li、Shuyang Zhang、Chao Yang

- 🎯 **研究动机**：扩大模型生成蒸馏数据通常只被视为提升覆盖与降噪，其让隐蔽 teacher trait 更易从 student 恢复的效应未被认识
- 🔬 **研究方法**：在 subliminal learning 控制设置中，由被诱导表达目标 trait 的 teacher 生成纯数字等离任务数据，训练不同数据量的 student 并用无 trait 对照隔离迁移
- 📌 **结论**：独立数据越多，teacher 诱导 trait 在 student 后续行为中越突出，LoRA 更新呈平行趋势，效应跨模型家族、trait 类型与跨模型迁移均成立

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scaling model-generated data is usually viewed as improving distillation: more examples should increase coverage, reduce noise, and produce stronger students. We show a second effect: larger datasets can make subtle teacher-specific signals easier to detect in the trained student, even when examples are off-task and never mention the trait. In a controlled setup inspired by subliminal learning, a teacher induced to express a target trait generates restricted off-task data, such as number-only completions. Students trained on different amounts of independent off-task data are evaluated in a separate domain, with matched no-trait controls isolating target-specific transfer. Our main finding is that larger independent datasets make the teacher's induced trait stand out more clearly in the student's later behavior. Other plausible traits may also strengthen with scale, but the target usually grows more. When the small-scale student already favors the target, scaling mainly amplifies that behavior; when it favors a related or salient alternative, more data can shift behavior toward the intended trait. Analyses of learned LoRA updates show a parallel trend. These effects appear across model families, trait types, multi-trait settings, and cross-model transfer. Our results suggest that scaling generated distillation data should be paired with trait-aware curation and evaluation, even when the data appears off-task or benign.

</details>

### 63. A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families

📄 [arXiv](https://arxiv.org/abs/2608.26506)　📅 2026-08

**关键词**：`analysis`、`attack`、`model merging`、`shared safety basin`、`post-training degradation`、`basin-aware jailbreak`

👤 **作者**：Yu Zhe、Yixin Tan、Junhao Wei、Wang Chen

- 🎯 **研究动机**：模型合并风险研究默认各组成模型对齐则合并安全，忽视源自预训练底座的共享风险
- 🔬 **研究方法**：发现共享 backbone 的合并模型族暴露共同 jailbreak basin；BAJ 在合并空间做 min-max 优化生成对抗后缀，无需知道合并系数
- 📌 **结论**：单一后缀跨同族合并模型持续高成功迁移，现有防御难以阻断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model merging enables combining multiple fine-tuned models without additional training, but its safety implications remain poorly understood. Prior work primarily attributes merging risks to unsafe constituent models, implicitly assuming that merging individually aligned models preserves safety. In contrast, we show that model merging reveals a previously overlooked jailbreak risk rooted in the pretrained foundation model, even when all constituent models are individually safety-aligned. Motivated by this observation, we study a new threat setting where an attacker constructs jailbreak prompts that generalize across merged models sharing the same pretrained backbone, without access to the exact merging coefficients or constituent checkpoints. To exploit this phenomenon, we propose \textbf{Basin-Aware Jailbreak (BAJ)}, which formulates jailbreak generation as a min--max optimization over the merging space to produce transferable adversarial suffixes across merged model families. Experiments across diverse backbones and merging settings show that BAJ achieves consistently high transfer success rates and remains effective under existing defenses.

</details>

### 64. Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks

📄 [arXiv](https://arxiv.org/abs/2608.25390)　📅 2026-08

**关键词**：`analysis`、`defense`、`refusal-prefix diversity`、`gradient stable rank`、`alignment hardening`、`refusal safeguard`

👤 **作者**：Andrey Labunets

- 🎯 **研究动机**：拒答行为集中于单一方向或低维子空间，vector ablation 即可移除，成因不明
- 🔬 **研究方法**：以 OLMo-2 为案例追踪拒答训练动态，分析首 token 损失的梯度与激活更新的 stable rank，并以受控微调验证多样化拒答开头
- 📌 **结论**：重复拒答前缀压低秩导致脆弱；多样化开头提高 stable rank 并增强对消融攻击的抵抗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge in a concentrated, low-dimensional structure. In a case study of OLMo-2-0425-1B-Instruct we find that the refusal geometry reflects refusal training: activation updates resulting from refusal-completion first-token losses explain the resulting refusal direction and refusal subspace. We study refusal directions through the training dynamics across refusal datasets and reveal that their brittleness is associated with repetitive refusal starts, which in turn is linked to concentration of gradients and refusal features in a low-dimensional subspace. Across frozen-model analyses and controlled synthetic fine-tuning, we find evidence of a hardening lever: diverse refusal starts can raise stable ranks of gradients and activation changes, making refusals harder to remove with a vector ablation attack.

</details>

### 65. Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

📄 [arXiv](https://arxiv.org/abs/2608.24988)　📅 2026-08

**关键词**：`analysis`、`post-training safety drift`、`embedded steering`、`SFT/RLHF`、`embedded safeguard`、`fine-tuning bypass`

👤 **作者**：Philipp E. Glass、Allan Tucker、Yongmin Li、Alina Miron

- 🎯 **研究动机**：嵌入权重的 activation steering 可编码对齐，但能否在部署后微调中存活未知
- 🔬 **研究方法**：在五个指令模型（3B-14B）上测 refusal 与 brevity steering 经 SFT/RLHF 后的行为保持与机制存留
- 📌 **结论**：refusal 消融平均失去 64% 行为效果，但权重编辑几乎未动（ρ=0.004）：机制耐久而功能脆弱，下游训练后须行为重验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $ρ= 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cosθ= 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

</details>

### 66. The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2606.28843) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66258)　📅 2026-06　🏷 ICML 2026

**关键词**：`analysis`、`defense`、`multilingual fine-tuning`、`safety drift`、`cross-lingual evaluation`、`safety alignment`

👤 **作者**：Will Hawkins、…、Chris Russell

- 🎯 **研究动机**：良性微调也会侵蚀安全，多语设定下的影响首次缺乏系统实证
- 🔬 **研究方法**：用九种语言翻译的良性数据微调 Llama-3.2、Qwen3、Gemma-3，跨语言评估安全漂移并分析内部表示变化；发布 Multilingual-Benign-Tune 数据集与 SORRY-Bench-Multilingual
- 📌 **结论**：对抗顺从率部分设定升高达四倍，漂移与通用能力指标解耦且跨语言模型高度异质；仅用英语评估微调影响不构成部署保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning a large language model is a ubiquitous method for enhancing its capability on a specific downstream task. However, prior work has shown that this increase in capability comes with a cost: it can increase a model's tendency to respond to unsafe adversarial prompts, even when fine-tuning with non-adversarial data. We present the first comprehensive empirical study of this phenomenon in multilingual settings by fine-tuning Llama-3.2, Qwen3, and Gemma-3 models using benign data translated across nine languages. We find that safety outcomes are highly sensitive to both the choice of fine-tuning language and the evaluation language, with adversarial compliance rates increasing four-fold in some settings. Multilingual safety drift is decoupled from general capability metrics, and occurs heterogeneously across languages and models. Fine-tuning in non-English languages often induces smaller internal representational drifts than English, but these shifts lead models to default to either exaggerated compliance or refusal. As such, assessing fine-tuning impacts solely in English provides inadequate assurance for deployment. To facilitate further research into these cross-lingual safety blind spots, we release the Multilingual-Benign-Tune dataset and the SORRY-Bench-Multilingual evaluation suite.

</details>

### 67. When Behavioral Safety Evaluation Fails: A Representation-Level Perspective

📄 [arXiv](https://arxiv.org/abs/2606.08044)　📅 2026-06

**关键词**：`analysis`、`audit gap`、`latent vulnerability`、`intervention-based evaluation`

👤 **作者**：Enyi Jiang、Anders Gjølbye、Yibo Jacky Zhang、Sanmi Koyejo

- 🎯 **研究动机**：静态行为审计只观察输出，无法度量对模型内部的小扰动能否把拒绝变成顺从，存在 audit gap
- 🔬 **研究方法**：从三个安全对齐底座构造 dissociated 模型（通过全部静态审计但服从已知内部扰动），用参数与潜空间软干预审计并以 Latent Vulnerability Score 量化单位扰动造成的安全退化
- 📌 **结论**：dissociated 模型在目标中层 LVS 为底座 2.5-3.1 倍，有界潜攻击使 54-86% 提示产生有害顺从（底座 3-48%），有害微调 5 步内达高顺从（底座需 10-25 步），行为测试无法证明表征级鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation of large language models (LLMs) is largely behavioral: a model is certified safe when it refuses harmful requests and answers benign ones. But refusing on the prompts an auditor happens to try does not show that the model is far from harmful behavior. Behavioral tests observe outputs; they do not measure how easily an intervention on the model turns a refusal into compliance. We call the gap between what static audits certify and what an intervention can reach the audit gap, and we show it is realizable: one can build a model that matches its safety-aligned base on every static audit yet gives way to a small, known perturbation of its internal state. We construct such dissociated models from three safety-aligned bases (Gemma 2 2B, Llama 3.2 3B, Qwen 2.5 3B) and audit the base, dissociated, and openly harmful models with the same soft interventions in parameter and latent space; the latent attacks are summarized by the Latent Vulnerability Score (LVS), the safety degradation produced per unit of bounded latent perturbation. Every static audit we run gives the dissociated model the same verdict as its base, since its refusals match the base, jailbreaks show no consistent signature, and a strong fixed probe on clean activations cannot tell it from the base. The same interventions an auditor could run reverse the verdict. At the targeted mid layer the dissociated models score 2.5 to 3.1 times higher LVS than their bases. A bounded latent attack elicits harmful compliance on 54 to 86% of prompts, against 3 to 48% for the bases, while matched random perturbations stay at or below 12%. Harmful fine-tuning reaches high compliance within five gradient steps, where the bases need 10 to 25. Behavioral testing, even with static latent probing, cannot certify representation-level robustness: a safety audit must intervene on the model, not only observe it.

</details>

### 68. Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models

🎓 [Official](https://aclanthology.org/2026.findings-acl.1616/)　📅 2026-04　🏷 ACL 2026

**关键词**：`analysis`、`harmful fine-tuning`、`safety parameters`、`parameter intervention`

👤 **作者**：Weiwei Qi、…、Kui Ren

- 🎯 **研究动机**：LLM 安全机制缺乏清晰理解，难以跨任务进行精确可靠的安全干预
- 🔬 **研究方法**：提出 ESI 框架量化参数对安全的影响，发现 dense LLM 的安全关键参数集中于中层 V 矩阵与 MLP、MoE 模型移至晚层 MLP；据此提出 SET 与 SPA 两种定向干预范式
- 📌 **结论**：SET 仅更新 1% 权重、100 次迭代即把未对齐 LLM 的攻击成功率降超 50%；SPA 使 1000 次迭代指令微调后安全退化保持在 1% 内

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring Large Language Model (LLM) safety is crucial, yet the lack of a clear understanding about safety mechanisms hinders the development of precise and reliable methodologies for safety intervention across diverse tasks. To better understand and control LLM safety, we propose the Expected Safety Impact (ESI) framework for quantifying how different parameters affect LLM safety. Based on ESI, we reveal distinct safety-critical patterns across different LLM architectures: In dense LLMs, many safety-critical parameters are located in value matrices (V) and MLPs in middle layers, whereas in Mixture-of-Experts (MoE) models, they shift to late-layer MLPs. Leveraging ESI, we further introduce two targeted intervention paradigms for safety enhancement and preservation, i.e., Safety Enhancement Tuning (SET) and Safety Preserving Adaptation (SPA). SET can align unsafe LLMs by updating only a few safety-critical parameters, effectively enhancing safety while preserving original performance. SPA safeguards well-aligned LLMs during capability-oriented intervention (e.g., instruction tuning) by preventing disruption of safety-critical weights, allowing the LLM to acquire new abilities while maintaining safety capabilities. Extensive evaluations on different LLMs demonstrate that SET can reduce the attack success rates of unaligned LLMs by over 50% with only a 100-iteration update on 1% of model weights. SPA can limit the safety degradation of aligned LLMs within 1% after a 1,000-iteration instruction fine-tuning on different tasks. Our code is available at: https://github.com/ZJU-LLM-Safety/SafeWeights-ACL

</details>

### 69. The Geometry of Narrow Fine-Tuning Degradation: Trajectory Lock-in and Spectral Bifurcation

🎓 [Official](https://icml.cc/Downloads/2026)　📅 2026-04　🏷 ICML 2026

**关键词**：`analysis`、`harmful fine-tuning`、`training geometry`、`trajectory locking`

- 🎯 **研究动机**：窄域微调造成的退化为何迅速固化不明
- 🔬 **研究方法**：分析参数轨迹锁定与谱分叉的几何结构
- 📌 **结论**：为退化不可逆性与干预时机提供几何解释

### 70. Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs

📄 [arXiv](https://arxiv.org/abs/2604.16659)　📅 2026-04

**关键词**：`analysis`、`audio fine-tuning`、`safety degradation`、`cross-modal proximity`

👤 **作者**：Jaechul Roh、Amir Houmansadr

- 🎯 **研究动机**：良性微调破坏安全已在文本与视觉证实，但音频模态中措辞完全无害的样本也可能因声学特性邻近有害内容，缺系统研究
- 🔬 **研究方法**：以邻近性过滤框架在三个 SOTA Audio LLM 上选良性音频微调，并用外部参考编码器把邻近分解为语义、声学与混合轴
- 📌 **结论**：JSR 从个位数升至 87.12%，主导脆弱轴与音频对文本的相对风险均随架构不同；距离过滤与文本 system prompt 两防御可将 JSR 降至近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior work shows that fine-tuning aligned models on benign data degrades safety in text and vision modalities, and that proximity to harmful content in representation space predicts which samples cause the most damage. However, existing analyses operate within a single, undifferentiated embedding space -- leaving open whether distinct input properties drive the vulnerability differently. Audio introduces a structurally richer problem: a benign sample can neighbor harmful content not only through what is said but through how it sounds, even when its words are entirely innocuous. We present the first systematic study of benign fine-tuning safety in Audio LLMs, evaluating three state-of-the-art models with a proximity-based filtering framework that selects benign audio by embedding-space distance to harmful content. By decomposing proximity into semantic, acoustic, and mixed axes using external reference encoders alongside each model's own internal encoder, we show that benign fine-tuning elevates Jailbreak Success Rate (JSR) from single digits to as high as 87.12%. Crucially, the dominant vulnerability axis and the relative risk of audio versus text fine-tuning are both architecture-conditioned -- determined by how each model's encoder and projector transform audio into the LLM's input space. We propose two defenses: filtering training data to maximize distance from harmful embeddings, and a textual system prompt at inference, both reducing JSR to near-zero without architectural modification. Our mechanistic analysis on two architectures reveals that fine-tuning selectively suppresses the late-layer refusal circuit while the frozen encoder preserves representations, and that even the suppression pattern is architecture-conditioned, mirroring the behavioral asymmetries across modalities. Safety degradation from benign fine-tuning is a qualitatively distinct risk in Audio LLMs.

</details>

### 71. Understanding the Effects of Safety Unalignment on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.02574) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`analysis`、`safety unalignment`、`weight orthogonalization`、`jailbreak fine-tuning`、`malicious capability`、`malicious capability recovery`

👤 **作者**：John T. Halloran

- 🎯 **研究动机**：jailbreak-tuning 与权重正交化两种去对齐方法只被按拒绝率孤立分析，对恶意能力的相对影响未知
- 🔬 **研究方法**：用 JT 与 WO 对六个不同规模 LLM 去对齐，跨大量恶意与良性任务系统比较
- 📌 **结论**：WO 产物助恶能力远强于 JT：更少幻觉、更好保留自然语言性能、更擅长对抗与网络攻击；SFT 可有效限制 WO 攻击能力而不损性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment has become a critical step to ensure LLMs refuse harmful requests while providing helpful and harmless responses. However, despite the ubiquity of safety alignment for deployed frontier models, two separate lines of recent work--jailbreak-tuning (JT) and weight orthogonalization (WO)--have shown that safety guardrails may be largely disabled, resulting in LLMs which comply with harmful requests they would normally refuse. In spite of far-reaching safety implications, analysis has largely been limited to refusal rates of each unalignment method in isolation, leaving their relative effects on adversarial LLM capabilities unknown. To fill this gap, we study the impact of unaligning six popular LLMs of various sizes across a large number of malicious and benign tasks, using both JT and WO. Across the evaluated models, we show that while refusal degradation is split between the two methods, WO produces LLMs far more capable of aiding in malicious activity; in contrast to JT, the majority of WO unaligned models are far less prone to hallucinations, better retain their original natural-language performance, and are more effective at state-of-the-art adversarial and cyber attacks. To thus help mitigate the malicious risks of WO unalignment, we conclude by showing that supervised fine-tuning effectively limits the adversarial attack abilities enabled by WO, without drastically affecting hallucination rates or natural language performance.

</details>

### 72. Can LLM Safety Be Ensured by Constraining Parameter Regions?

📄 [arXiv](https://arxiv.org/abs/2602.17696) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1616/)　📅 2026-02　🏷 ACL 2026

**关键词**：`analysis`、`harmful fine-tuning`、`parameter region`、`safety boundary`、`runtime safety`、`refusal calibration`

👤 **作者**：Zongmin Li、Jian Su、Farah Benamara、Aixin Sun

- 🎯 **研究动机**：LLM 存在修改即影响安全行为的参数子区域这一假设从未被系统检验
- 🔬 **研究方法**：跨四个模型家族系统评估四类不同粒度的安全区域识别方法，在十个安全数据集上用 IoU 度量区域重叠
- 📌 **结论**：各方法识别的安全区域仅低至中等重叠，用效用数据细化后进一步下降，不存在稳定的数据集无关安全区域

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often assumed to contain ``safety regions'' -- parameter subsets whose modification directly influences safety behaviors. We conduct a systematic evaluation of four safety region identification methods spanning different parameter granularities, from individual weights to entire Transformer layers, across four families of backbone LLMs with varying sizes. Using ten safety identification datasets, we find that the identified safety regions exhibit only low to moderate overlap, as measured by IoU. The overlap drops significantly when the safety regions are further refined using utility datasets (\ie non-harmful queries). These results suggest that current techniques fail to reliably identify a stable, dataset-agnostic safety region.

</details>

### 73. Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.400/)　📅 2026-01　🏷 ACL 2026

**关键词**：`analysis`、`fine-tuning privacy`、`privacy degradation`、`benign fine-tuning`、`safety-preserving fine-tuning`、`privacy leakage`

👤 **作者**：Anmol Goel、Cornelius Emde、Seong Joon Oh、Sangdoo Yun、Martin Gubri

- 🎯 **研究动机**：前沿模型的良性微调可致隐私崩溃——标准安全效用基准检测不到的静默失败
- 🔬 **研究方法**：识别破坏上下文隐私的细微训练模式（助人优化、用户信息暴露、情感对话、调试代码打印内部变量），在六模型、五数据集、两类任务验证并做机制分析
- 📌 **结论**：微调后模型失去上下文隐私规范推理、不当向工具分享信息并跨上下文违反记忆边界；隐私表示比任务特征对微调更脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We identify a novel phenomenon in language models: benign fine-tuning of frontier models can lead to privacy collapse. We find that diverse, subtle patterns in training data can degrade contextual privacy, including optimisation for helpfulness, exposure to user information, emotional and subjective dialogue, and debugging code printing internal variables, among others. Finetuned models lose their ability to reason about contextual privacy norms, share information inappropriately with tools, and violate memory boundaries across contexts. Privacy collapse is a “silent failure” because models maintain high performance on standard safety and utility benchmarks whilst exhibiting severe privacy vulnerabilities. Our experiments show evidence of privacy collapse across six models (closed and open weight), five fine-tuning datasets (real-world and controlled data), and two task categories (agentic and memory-based). Our mechanistic analysis reveals that privacy representations are uniquely fragile to fine-tuning, compared to task-relevant features which are preserved. Our results reveal a critical gap in current safety evaluations, in particular for the deployment of specialised agents.

</details>

### 74. Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study

📄 [arXiv](https://arxiv.org/abs/2505.14185) · 📝 [OpenReview](https://openreview.net/forum?id=2uLBkfMyX5) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010569)　📅 2025-05　🏷 ICLR 2026

**关键词**：`analysis`、`harmful fine-tuning`、`subspace analysis`、`representation entanglement`

👤 **作者**：Kaustubh Ponkshe、Shaan Shah、Raghav Singhal、Praneeth Vepakomma

- 🎯 **研究动机**：若安全对应可分离的线性子空间即可隔离防御失配，但该假设未被系统检验
- 🔬 **研究方法**：在权重与激活空间考察安全行为是否集中于特定线性子空间、能否与通用学习分离，覆盖 Llama 与 Qwen 家族五个 LLM
- 📌 **结论**：放大安全行为的子空间同样放大有用行为，安全与通用学习高度纠缠，子空间防御存在根本局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) rely on safety alignment to produce socially acceptable responses. However, this behavior is known to be brittle: further fine-tuning, even on benign or lightly contaminated data, can degrade safety and reintroduce harmful behaviors. A growing body of work suggests that alignment may correspond to identifiable directions in weight space, forming subspaces that could, in principle, be isolated or preserved to defend against misalignment. In this work, we conduct a comprehensive empirical study of this perspective. We examine whether safety-relevant behavior is concentrated in specific linear subspaces, whether it can be separated from general-purpose learning, and whether harmfulness arises from distinguishable patterns in activations. Across both weight and activation spaces, our findings are consistent: subspaces that amplify safe behaviors also amplify useful ones, and prompts with different safety implications activate overlapping representations. Rather than residing in distinct directions, we show that safety is highly entangled with the general learning components of the model. This suggests that subspace-based defenses face fundamental limitations and underscores the need for alternative strategies to preserve safety under continued training. We corroborate these findings with multiple experiments on five open-source LLMs from the Llama and Qwen families. Our code is publicly available at: https://github.com/CERT-Lab/safety-subspaces.

</details>

### 75. Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety

📄 [arXiv](https://arxiv.org/abs/2505.06843) · 🌐 [Project](https://proceedings.mlr.press/v267/guan25c.html)　📅 2025-05　🏷 ICML 2025

**关键词**：`analysis`、`harmful fine-tuning`、`outlier sample`、`benign fine-tuning`

👤 **作者**：Zihan Guan、Mengxuan Hu、Ronghang Zhu、Sheng Li、Anil Vullikanti

- 🎯 **研究动机**：良性数据微调也会削弱 LLM 安全对齐，其中哪些样本起主要作用不明
- 🔬 **研究方法**：从离群检测视角提出 Self-Inf-N，检出良性数据集中致安全退化最大的样本并仅用其微调
- 📌 **结论**：仅 100 个离群样本即严重破坏 7 个主流 LLM 的安全对齐，跨架构可迁移且多数缓解策略失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have uncovered a troubling vulnerability in the fine-tuning stage of large language models (LLMs): even fine-tuning on entirely benign datasets can lead to a significant increase in the harmfulness of LLM outputs. Building on this finding, our red teaming study takes this threat one step further by developing a more effective attack. Specifically, we analyze and identify samples within benign datasets that contribute most to safety degradation, then fine-tune LLMs exclusively on these samples. We approach this problem from an outlier detection perspective and propose Self-Inf-N, to detect and extract outliers for fine-tuning. Our findings reveal that fine-tuning LLMs on 100 outlier samples selected by Self-Inf-N in the benign datasets severely compromises LLM safety alignment. Extensive experiments across seven mainstream LLMs demonstrate that our attack exhibits high transferability across different architectures and remains effective in practical scenarios. Alarmingly, our results indicate that most existing mitigation strategies fail to defend against this attack, underscoring the urgent need for more robust alignment safeguards. Codes are available at https://github.com/GuanZihan/Benign-Samples-Matter.

</details>

### 76. Evaluating Defences against Unsafe Feedback in RLHF

📄 [arXiv](https://arxiv.org/abs/2409.12914)　📅 2024-09

**关键词**：`analysis`、`unsafe feedback`、`RLHF`、`defense evaluation`

👤 **作者**：Domenic Rosati、…、Hassan Sajjad

- 🎯 **研究动机**：从 不安全反馈中做 RL 学习的风险此前未被探索
- 🔬 **研究方法**：分析不安全样本被偏好的学习设定，并把隐式/显式有害微调防御改造为 RLHF 学习约束逐一评估
- 📌 **结论**：安全 LLM 会主动探索不安全动作空间；无防御普遍有效，部分方法靠 harmless reward hacking 取效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While there has been progress towards aligning Large Language Models (LLMs) with human values and ensuring safe behaviour at inference time, safety guards can easily be removed when fine tuned on unsafe and harmful datasets. While this setting has been treated extensively, another popular training paradigm, learning from unsafe feedback with reinforcement learning, has previously been unexplored. This is concerning due to the widespread deployment of feedback collection systems. We address this gap by providing an analysis of learning settings where feedback is harmful, i.e. that unsafe samples are preferred over safe ones despite model developers goal to maintain safety. We find that safety-aligned LLMs easily explore unsafe action spaces via generating harmful text and optimize for reward that violates safety constraints indicating that current safety guards are not enough to prevent learning from unsafe feedback. In order to protect against this vulnerability, we adapt a number of both "implict" and "explicit" harmful fine-tuning defences to evaluate whether they are effective as learning constraints in an RLHF setting finding that no method is generally effective pointing to the need for more defence research. We end the paper with the observation that some defences work by performing "harmless reward hacking" for which we provide a theoretical explanation drawn from the theory of Constrained Markov Decision Processes and provide some direction for future defence development.

</details>

### 77. What is in Your Safe Data? Identifying Benign Data that Breaks Safety

📄 [arXiv](https://arxiv.org/abs/2404.01099) · 📝 [OpenReview](https://openreview.net/forum?id=Hi8jKh4HE9)　📅 2024-04　🏷 COLM 2024

**关键词**：`analysis`、`fine-tuning data`、`benign data`、`gradient analysis`

👤 **作者**：Luxi He、Mengzhou Xia、Peter Henderson

- 🎯 **研究动机**：良性数据微调也会意外破坏安全对齐，其数据侧成因不明
- 🔬 **研究方法**：从表示与梯度双空间刻画微调数据，提出双向锚定法优先选取贴近有害样本、远离良性样本的数据
- 📌 **结论**：仅 100 个看似良性样本即使模型应答超 70% 有害请求（随机数据不足 20%）；高风险数据多为列表、要点与数学题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current Large Language Models (LLMs), even those tuned for safety and alignment, are susceptible to jailbreaking. Some have found that just further fine-tuning an aligned model with benign data (i.e., data without harmful content) surprisingly leads to substantial degradation in safety. We delve into the data-centric aspects of why benign fine-tuning inadvertently contributes to jailbreaking. First, we represent fine-tuning data through two lenses: representation and gradient spaces. Additionally, we propose a bi-directional anchoring method that, during the selection process, prioritizes data points that are close to harmful examples and far from benign ones. Our approach effectively identifies subsets of benign data that are more likely to degrade the model's safety after fine-tuning. Training on just 100 of these seemingly benign datapoints surprisingly leads to the fine-tuned model affirmatively responding to >70% of tested harmful requests, compared to <20% after fine-tuning on randomly selected data. We also observe that the selected data frequently appear as lists, bullet points, or math questions, indicating a systematic pattern in fine-tuning data that contributes to jailbreaking.

</details>

### 78. Immunization against Harmful Fine-Tuning Attacks

📄 [arXiv](https://arxiv.org/abs/2402.16382) · 🎓 [Official](https://aclanthology.org/2024.findings-emnlp.301/)　📅 2024-02　🏷 EMNLP 2024

**关键词**：`analysis`、`harmful fine-tuning`、`attacker budget`、`defense framework`

👤 **作者**：Domenic Rosati、…、Frank Rudzicz

- 🎯 **研究动机**：harmful fine-tuning 防御如何构建与验证缺乏理论框架，尤其防御方不控制微调流程时
- 🔬 **研究方法**：基于攻击者训练预算形式化 Immunization 条件，刻画成功防御的必要组成与严格验证准则
- 📌 **结论**：给出防御研究应满足的攻击覆盖与实验规范指南

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are often trained with safety guards intended to prevent harmful text generation. However, such safety training can be removed by fine-tuning the LLM on harmful datasets. While this emerging threat (harmful fine-tuning attacks) has been characterized by previous work, there is little understanding of how we should proceed in constructing and validating defenses against these attacks especially in the case where defenders would not have control of the fine-tuning process. We introduce a formal framework based on the training budget of an attacker which we call "Immunization" conditions. Using a formal characterisation of the harmful fine-tuning problem, we provide a thorough description of what a successful defense must comprise of and establish a set of guidelines on how rigorous defense research that gives us confidence should proceed.

</details>

### 79. Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

📄 [arXiv](https://arxiv.org/abs/2310.03693) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2024/hash/83b7da3ed13f06c13ce82235c8eedf35-Abstract-Conference.html)　📅 2023-10　🏷 ICLR 2024

**关键词**：`analysis`、`harmful fine-tuning`、`alignment forgetting`、`few-shot attack`

👤 **作者**：Xiangyu Qi、…、Peter Henderson

- 🎯 **研究动机**：安全对齐基础设施只覆盖推理期，用户获得微调权限时的风险不在防护之列
- 🔬 **研究方法**：red teaming：用极少量对抗性样本微调 GPT-3.5 Turbo，同时检验良性常用数据集微调的影响
- 📌 **结论**：仅 10 个样本、花费不到 0.2 美元即越狱护栏；良性数据微调也会无意削弱安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Optimizing large language models (LLMs) for downstream use cases often involves the customization of pre-trained LLMs through further fine-tuning. Meta's open release of Llama models and OpenAI's APIs for fine-tuning GPT-3.5 Turbo on custom datasets also encourage this practice. But, what are the safety costs associated with such custom fine-tuning? We note that while existing safety alignment infrastructures can restrict harmful behaviors of LLMs at inference time, they do not cover safety risks when fine-tuning privileges are extended to end-users. Our red teaming studies find that the safety alignment of LLMs can be compromised by fine-tuning with only a few adversarially designed training examples. For instance, we jailbreak GPT-3.5 Turbo's safety guardrails by fine-tuning it on only 10 such examples at a cost of less than $0.20 via OpenAI's APIs, making the model responsive to nearly any harmful instructions. Disconcertingly, our research also reveals that, even without malicious intent, simply fine-tuning with benign and commonly used datasets can also inadvertently degrade the safety alignment of LLMs, though to a lesser extent. These findings suggest that fine-tuning aligned LLMs introduces new safety risks that current safety infrastructures fall short of addressing -- even if a model's initial safety alignment is impeccable, it is not necessarily to be maintained after custom fine-tuning. We outline and critically analyze potential mitigations and advocate for further research efforts toward reinforcing safety protocols for the custom fine-tuning of aligned LLMs.

</details>

### 80. Harmful Fine-tuning Attacks and Defenses for Large Language Models: A Survey

📄 [arXiv](https://arxiv.org/abs/2409.18169)　📅 2024-09

**关键词**：`survey`、`harmful fine-tuning`、`threat model`、`defense taxonomy`

👤 **作者**：Tiansheng Huang、Sihao Hu、Fatih Ilhan、Selim Furkan Tekin、Ling Liu

- 🎯 **研究动机**：有害微调攻防文献爆发但缺乏统一威胁模型与系统梳理
- 🔬 **研究方法**：从攻击设定、防御设计与评测方法三个视角综述代表性工作并维护论文列表
- 📌 **结论**：给出该方向未来研究的指导与关键视角

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research demonstrates that the nascent fine-tuning-as-a-service business model exposes serious safety concerns: fine-tuning with a few harmful data uploaded from the users can compromise the safety alignment of the model. The attack, known as harmful fine-tuning attack, has generated broad research interests in both academia and industry. In this paper, we first systematically formulate the threat model and basic assumptions of harmful fine-tuning. Then, we provide a comprehensive review of harmful fine-tuning from three fundamental perspectives: attack setting, defense design, and evaluation methodology. First, we present the threat model of the problem and introduce the harmful fine-tuning attack and its variants. Next, we systematically survey representative attacks, defense methods, and mechanical analysis of adverse effects in the existing literature. Finally, we introduce the evaluation methodology and outline future research directions, which can serve as guidelines and crucial perspectives for the future development of the subject. We also maintain a curated list of relevant papers, which are made accessible at https://github.com/git-disl/awesome_LLM-harmful-fine-tuning-papers

</details>

### 81. TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering

📄 [arXiv](https://arxiv.org/abs/2602.06911) · 🌐 [Project](https://doi.org/10.1145/3770855.3817557)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`model tampering`、`fine-tuning attack sweep`、`alignment robustness`、`fine-tuning safety`、`safeguard tampering`

👤 **作者**：Saad Hossain、…、Sirisha Rambhatla

- 🎯 **研究动机**：LLM 防篡改能力评估缺少统一框架，数据集、指标与篡改配置各异致结果不可比
- 🔬 **研究方法**：TamperBench 整合权重空间微调攻击、潜空间表示攻击与对齐阶段防御，对 21 个开源模型按每对攻击-模型做超参扫描并同步评安全与能力
- 📌 **结论**：jailbreak-tuning 通常是最严重攻击，现有对齐阶段防御在系统化攻击扫描下大多失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As increasingly capable open-weight large language models (LLMs) are deployed, improving their tamper resistance against unsafe modifications, whether accidental or intentional, becomes critical to minimize risks. However, there is no standard approach to evaluate tamper resistance. Varied datasets, metrics, and tampering configurations make it difficult to compare safety, utility, and robustness across different models and defenses. To address this, we introduce TamperBench, the first unified framework to systematically evaluate the tamper resistance of LLMs. TamperBench (i) curates a repository of state-of-the-art weight-space fine-tuning attacks, latent-space representation attacks, and alignment-stage defenses; (ii) enables realistic adversarial evaluation through systematic hyperparameter sweeps per attack-model pair; and (iii) provides both safety and utility evaluations. We use TamperBench to evaluate 21 open-weight LLMs, including defense-augmented variants, across nine tampering threats using standardized safety and capability metrics with hyperparameter sweeps per model-attack pair. The results provide insights including effects of post-training on tamper resistance, that jailbreak-tuning is typically the most severe attack, and that current alignment-stage defenses largely fail to withstand attack sweeps. Code is available at https://github.com/criticalml-uw/TamperBench.

</details>

### 82. Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment

📄 [arXiv](https://arxiv.org/abs/2601.22313) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64533)　📅 2026-01　🏷 ICML 2026

**关键词**：`benchmark`、`post-update alignment`、`latent adversarial behavior`、`benign update`、`safety alignment`、`empirical evaluation`

👤 **作者**：Yavuz Bakman、Duygu Nur Yaldiz、Eleni Triantafillou、Peter Kairouz、Salman Avestimehr、Sai Praneeth Karimireddy

- 🎯 **研究动机**：静态黑盒评测能否保证模型更新后的对齐从未被充分探讨
- 🔬 **研究方法**：形式化静态与更新后对齐，理论证明过参数化使静态对齐对任意更新集不提供更新后保证、黑盒探测无法区分真实鲁棒与隐藏任意对抗行为的模型，并在隐私、越狱与诚实三域实证
- 📌 **结论**：存在通过全部标准黑盒对齐测试、单次良性更新即严重失准的 LLM，且隐藏能力随模型规模增大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are rarely static and are frequently updated in practice. A growing body of alignment research has shown that models initially deemed ``aligned'' can exhibit misaligned behavior after fine-tuning. These works typically assume that the initial model is aligned based on static black-box evaluation, i.e., the absence of undesired responses to a fixed set of queries. However, the limits of black-box evaluation for post-update scenarios is not explored sufficiently. In this work, we formalize model alignment in both the static and post-update settings and uncover a fundamental limitation of black-box evaluation. We theoretically show that, due to overparameterization, static alignment provides no guarantee of post-update alignment for any update dataset. Moreover, we prove that static black-box probing cannot distinguish a model that is genuinely post-update robust from one that conceals an arbitrary amount of adversarial behavior which can be activated by even a single benign gradient update. We further validate these findings empirically in LLMs across three core alignment domains: privacy, jailbreak safety, and behavioral honesty. We demonstrate the existence of LLMs that pass all standard black-box alignment tests, yet become severely misaligned after a single benign update. Finally, we show that the capacity to hide such latent adversarial behavior increases with model scale, confirming our theoretical prediction that post-update misalignment grows with the number of parameters. Together, our results highlight the inadequacy of static evaluation protocols and emphasize the urgent need for post-update--robust alignment evaluation. Code can be found at: https://github.com/Ybakman/safety_benign_update.

</details>

### 83. Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets

🎓 [Official](https://aclanthology.org/2026.acl-long.756/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`defense`、`jailbreak`、`harmful fine-tuning`、`alignment erosion`、`content moderation`

👤 **作者**：Lei Hsiung、…、Yaoqing Yang

- 🎯 **研究动机**：微调后安全护栏崩溃的缓解聚焦事后处置、清除有害梯度或持续强化对齐，忽视上游安全对齐数据这一因素
- 🔬 **研究方法**：从上游对齐数据与下游微调任务的表示相似性视角实验分析护栏退化规律
- 📌 **结论**：两类数据集相似性高会显著削弱护栏、更易越狱；低相似性使模型更鲁棒，harmfulness score 至多降低 10.33%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in large language models (LLMs) have underscored their vulnerability to safety alignment jailbreaks, particularly when subjected to downstream fine-tuning. However, existing mitigation strategies primarily focus on reactively addressing jailbreak incidents after safety guardrails have been compromised, removing harmful gradients during fine-tuning, or continuously reinforcing safety alignment throughout fine-tuning. As such, they tend to overlook a critical upstream factor: the role of the original safety-alignment data. This paper therefore investigates the degradation of safety guardrails through the lens of representation similarity between upstream alignment datasets and downstream fine-tuning tasks. Our experiments demonstrate that high similarity between these datasets significantly weakens safety guardrails, making models more susceptible to jailbreaks. Conversely, low similarity between these two types of datasets yields substantially more robust models and thus reduces harmfulness score by up to 10.33%. By highlighting the importance of upstream dataset design in the building of durable safety guardrails and reducing real-world vulnerability to jailbreak attacks, these findings offer actionable insights for fine-tuning service providers to prioritize upstream models with low jailbreak risk.

</details>

### 84. SPQR: A Multi-Dimensional Benchmark for Safety Alignment under Benign Model Adaptation

📄 [arXiv](https://arxiv.org/abs/2511.19558) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5585)　📅 2025-11　🏷 ECCV 2026

**关键词**：`benchmark`、`benign fine-tuning`、`diffusion model`、`adaptation robustness`、`safety alignment`、`refusal behavior`

👤 **作者**：Mohammed Talha Alam、…、Samuele Poppi

- 🎯 **研究动机**：T2I 安全对齐评测很少检验部署后常规良性微调（LoRA 个性化、风格适配器）下的安全持久性，而失效频繁发生
- 🔬 **研究方法**：提出 SPQR（Safety、Prompt adherence、Quality、Robustness）单分值基准，统一评测安全对齐扩散模型在良性微调下的安全、效用与鲁棒性，辅以多语言、领域与 OOD 分析
- 📌 **结论**：揭示安全对齐在良性微调后频繁崩溃，并提供可复现的 leaderboard 评分以比较 T2I 安全技术

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models can emit copyrighted, unsafe, or private content. Safety alignment aims to suppress specific concepts, yet evaluations seldom test whether safety persists under benign downstream fine-tuning routinely applied after deployment (e.g., LoRA personalization, style/domain adapters). We study the stability of current safety methods under benign fine-tuning and observe frequent breakdowns. As true safety alignment must withstand even benign post-deployment adaptations, we introduce the SPQR benchmark (Safety, Prompt adherence, Quality, and Robustness). SPQR is a single-scored metric that provides a unified, reproducible framework to evaluate how well safety-aligned diffusion models preserve safety, utility, and robustness under benign fine-tuning, by reporting a single leaderboard score to facilitate comparisons. We conduct multilingual, domain-specific, and out-of-distribution analyses, along with category-wise breakdowns, to identify when safety alignment fails after benign fine-tuning, ultimately showcasing SPQR as a concise yet comprehensive benchmark for T2I safety alignment techniques for T2I models.

</details>

### 85. Active Adaptation, Not Static Defense: Temporal Dynamics of Preventative Steering in Adversarial Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2609.10142)　📅 2026-09

**关键词**：`analysis`、`malicious fine-tuning defense`、`preventative steering`、`temporal dynamics`、`progressive scheduling`

👤 **作者**：Jing Guan、Yachao Yang、Zhaoliang Liu、Yuyao Zhang、Fanyu Meng、Junlan Feng

- 🎯 **研究动机**：Preventative Steering 抗恶意微调的持久保护机制不明，制约其改进
- 🔬 **研究方法**：分析时间优化动力学：早期补偿适应+稳态校正衰减，注意力输出投影为防御更新主导路径；IDP 实验证明静态权重偏移无法维持保护
- 📌 **结论**：提出渐进强度调度 PIS，Qwen2.5/Gemma-3 上超越静态强度 steering 的安全鲁棒性并降低有害特质表达

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain fragile against malicious fine-tuning, motivating training-time defenses against harmful persona drift. Preventative Steering injects undesirable-trait persona vectors during fine-tuning and removes them at evaluation time, yet the mechanism behind its lasting protection remains unclear. Analyzing its temporal optimization dynamics, we find that the defense emerges from an early compensatory adaptation phase followed by a steady-state phase where the corrective signal decays; in parameter space, attention output projections emerge as the dominant residual-write route for defensive updates. Through Intervention Delta Preservation (IDP) and IDP Continuation experiments, we further show that preserving or reinjecting the weight offset fails to maintain protection, indicating that preventative steering relies on active adaptation rather than a static defense. Motivated by this finding, we propose Progressive Intensity Scheduling (PIS), which starts with a moderate injection strength and increases it after static-strength alignment begins to decay. Across the evaluated Qwen2.5 and Gemma-3 models, PIS improves safety robustness over static-strength steering while reducing harmful trait expression.

</details>

### 86. Multilingual Safety Signals Are Multi-Layered: Filtering Safety-Degrading Data for Safer LLMs

📄 [arXiv](https://arxiv.org/abs/2609.22144)　📅 2026-09

**关键词**：`defense`、`multilingual safety`、`multi-layer signal`、`data filtering`、`fine-tuning safety`

👤 **作者**：Jiakun Li、Guowei Song、Sijia Li、Xingwei He、Hongzheng Chai、Yuan Yuan

- 🎯 **研究动机**：良性微调数据中混有静默破坏安全对齐的样本，既有识别法假设单一安全敏感层——跨语言表示差异使该假设在多语言模型上存疑
- 🔬 **研究方法**：跨语言分析显示敏感层仅部分共享、安全信号分布于多层；MMSAFE 多层框架同时捕获共享与语言特异的安全退化信号并过滤
- 📌 **结论**：多语言安全退化数据识别的层间结构——微调安全保持的表示级信号（EMNLP 2026 Main）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preserving safety alignment during large language models fine-tuning is critical, however, recent studies have demonstrated that even benign fine-tuning data may contain safety-degrading samples that silently undermine safety alignment. Existing approaches typically identify such samples using representations from a single safety-sensitive layer. While this assumption has shown effectiveness in monolingual settings, its validity for multilingual models remains unclear due to potential cross-lingual differences in representation patterns. Through a cross-lingual analysis, we show that sensitive layers are only partially shared across languages, with safety-relevant signals often distributed across multiple layers. Motivated by these observations, we propose MMSAFE, a multi-layer framework for multilingual safety-degrading data identification that captures both shared and language-specific safety signals. Extensive experiments across multiple models, languages, and safety benchmarks demonstrate that MMSAFE reduces the average harmful-response ratio by 60% compared with random filtering and achieves stronger average performance than the strongest single-layer baseline, demonstrating the effectiveness of multi-layer modeling for robust multilingual safety alignment.

</details>
