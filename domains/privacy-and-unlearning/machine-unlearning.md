# Machine Unlearning 与删除保证

[返回上级目录](README.md)

## 研究方向

研究在不完整重训的条件下移除训练样本、知识、用户或概念的影响，覆盖 LLM、MLLM、推荐与持续学习；核心评测同时检查 forgetting、retention、relearning、泄漏复测与删除保证。

## 研究脉络

- **近似遗忘：** 早期方法以梯度更新、参数编辑和表示压缩降低 forget set 的可见影响。
- **模型与任务扩展：** 研究扩展到生成模型、多模态模型、MoE、RL 与持续学习。
- **保证与反测试：** Certified unlearning、relearning attack、probabilistic decoding 和 hidden leakage 揭示只看标准准确率会高估删除效果。
- **当前边界：** 可验证删除、低 collateral damage 与对自适应恢复攻击的稳健性仍难同时满足。

## Benchmark、Leakage Re-Test 与评测有效性

### 1. ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.20338) · 📊 [Dataset](https://huggingface.co/datasets/sk0511/concept-guard)　📅 2026-08

**关键词**：`benchmark`、`context-sensitive unlearning`、`dual-use concept`、`utility preservation`、`concept-level unlearning`、`dual-use intent`

👤 **作者**：Sahil Kale、Ian Harris

- 🎯 **研究动机**：现有 unlearning 用不相交遗忘/保留集与直接事实回忆评测，无法衡量消除有害应用同时保留良性用法的能力
- 🔬 **研究方法**：引入双用途概念，ConceptGuard 的 forget/retain 集在概念使用上显式互补，评测意图敏感并最大化上下文分离
- 📌 **结论**：现有技术在该设定下表现差：上下文分离弱、ROUGE 与概念级指标差、概念级控制一致性差，遗忘-效用权衡强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple and direct factual recall. This framing fails to capture a key requirement of unlearning, namely the ability to eliminate harmful behaviors while preserving benign and beneficial knowledge. We argue that effective unlearning must operate at the level of concepts, ensuring complete removal of unsafe applications while maintaining their correct and useful usage, thereby achieving conceptually meaningful and complete unlearning. To better evaluate unlearning techniques from such a practical viewpoint, we introduce the notion of dual-use concepts: concepts that can be used in both harmful and benign contexts. Building on these concepts, we construct a benchmark called ConceptGuard where forget and retain sets are explicitly complementary in concept usage. Our benchmark uniquely enables unlearning to be explored and gauged at the level of concepts, instead of sparse facts, and evaluation is intent-sensitive with the goal of maximizing contextual separation to promote safer behavior. We demonstrate that current unlearning techniques perform poorly under this setting, showing weak contextual separation alongside poor performance in ROUGE and concept-level metrics. Our results reveal strong forgetting-utility trade-offs, limited gains in contextual sensitivity, and poor consistency in concept-level control across methods, and provide ideas for unlearning approaches that better align with real-world safety requirements. Our dataset is publicly available.

</details>

### 2. Stress Testing Unlearning Algorithms

📄 [arXiv](https://arxiv.org/abs/2608.22527)　📅 2026-08

**关键词**：`benchmark`、`capability removal`、`adversarial elicitation`、`boundary preservation`、`WMDP++`、`targeted extraction`

👤 **作者**：Noam Diamant、Neta Glazer、Ethan Fetaya

- 🎯 **研究动机**：现有 unlearning benchmark 不主动测试被遗忘信息能否被强行提取，也不评估语义邻近良性 boundary question 上的性能保留
- 🔬 **研究方法**：WMDP++ 扩展 WMDP：加入对被遗忘信息的 targeted extraction 攻击与边界问题系统性评测
- 📌 **结论**：同时压力测试移除的抗提取性与授权能力保留，为 LLM unlearning 提供更严格的评测基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, machine unlearning, the removal of specific training data influence from a model, has gained increasing attention. In large language models (LLMs), unlearning is particularly challenging due to the ambiguity of inputs and outputs. Con- sequently, rigorous evaluation is critical for assessing both safety and utility, and for driving progress in unlearning meth- ods. We identify two key shortcomings in existing unlearning benchmarks: (1) they do not actively test whether unlearned information can still be forcibly extracted, and (2) they fail to evaluate performance preservation on boundary questions, be- nign queries that are semantically close to the unlearned con- tent. Here we introduce WMDP++, an extension of WMDP that addresses these gaps by incorporating targeted extrac- tion of unlearned information and systematic evaluation on boundary questions. WMDP++ provides a more stringent and informative benchmark for evaluating unlearning in LLMs.

</details>

### 3. Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.21606)　📅 2026-08

**关键词**：`benchmark`、`attack`、`capability recovery`、`adversarial prompting`、`unlearning robustness`、`unlearned-data recovery`

👤 **作者**：Ayush Gupta、…、Sadid Hasan

- 🎯 **研究动机**：现有 unlearning benchmark 只用干净非对抗查询评估，看似遗忘的信息能否经策略性提示恢复仍未知
- 🔬 **研究方法**：在 TOFU+Llama-3.2-3B-Instruct 上统一评估 prompt 式与微调式遗忘方法，对标准指标下的强者做对抗压力测试，并引入 LLM-as-judge 的 Attack Success Rate 指标
- 📌 **结论**：Forget Quality 超过 0.91 的方法对抗恢复 ASR 仍达 72.8–84.3%（接近未防护基线的 87.5%），而干净多语言改写仅测出 2.95% 泄漏——标准指标强不足以证明遗忘稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of targeted training data from a model while preserving its remaining capabilities, but evaluating whether such information has truly become inaccessible remains challenging. Existing benchmarks primarily assess unlearning under clean, non-adversarial queries, leaving open whether information that appears forgotten can still be recovered through strategic prompting. We address this gap through a unified evaluation of prompt-based and fine-tuning-based unlearning methods on TOFU using Llama-3.2-3B-Instruct, followed by an adversarial robustness evaluation of methods that perform strongly under standard metrics. We introduce Attack Success Rate (ASR), an LLM-as-judge metric that measures the fraction of adversarial responses whose leakage score exceeds $0.2$, and evaluate recovery across eight attack suites. Our results reveal a substantial gap between clean-query forgetting and adversarial robustness. Although several fine-tuning-based methods achieve Forget Quality above $0.91$, targeted information remains recoverable with ASRs between $72.8\%$ and $84.3\%$, close to the $87.5\%$ ASR of the unprotected base model. In contrast, clean multilingual reformulations yield only $2.95\%$ measured leakage. A manual audit further finds agreement between binary ASR decisions and human factual assessments in seven of ten cases, indicating that ASR provides a useful, though imperfect, signal of behavioral recoverability. These findings show that strong standard-metric performance alone is insufficient to establish robustness after unlearning and motivate adversarial stress-testing as a complementary component of unlearning evaluation.

</details>

### 4. Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.20960)　📅 2026-08

**关键词**：`benchmark`、`scientific knowledge drift`、`claim-level unlearning`、`outdated evidence`、`claim-level capability removal`、`structured knowledge`

👤 **作者**：Snigdha Paul、Manasi Patwardhan、Arman Cohan

- 🎯 **研究动机**：科学主张会被撤回、证伪或更新，而科学知识相互关联且持续演化，现有 instance-level 遗忘研究与评测无法覆盖 claim 级删除
- 🔬 **研究方法**：提出 Scientific Claim Unlearning 任务并构建 benchmark SciUnlearn，系统评测现有 unlearning 方法
- 📌 **结论**：现有方法无法有效消除 claim 级知识，多只实现表层抑制，需要面向结构化知识删除的专门方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while maintaining overall model utility. Existing studies primarily investigate instance-level forgetting; however, scientific claims introduce additional challenges because they are interconnected, and continually evolving. To address this gap, we introduce the task of Scientific Claim Unlearning and present a new benchmark, SciUnlearn. We show that current unlearning approaches are unable to effectively eliminate claim-level knowledge and often achieve only superficial suppression, highlighting the need for specialized methods designed for structured knowledge removal.

</details>

### 5. An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.17804)　📅 2026-08

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Rubén Balbastre、Juan Manuel Orduña、Mariano Pérez

- 🎯 **研究动机**：生成式 QA 的 unlearning 漏掉第三种行为规范：目标邻近 prompt 应给出更宽泛答案而非泄漏、逃避或拒答
- 🔬 **研究方法**：受控 LoRA-GRPO RWKU 设定比较四种奖励设计（词汇抑制、反拒答塑形、rubric 宽答、显式拒答对比）与可选 SFT 预热
- 📌 **结论**：优化成功不等于行为 unlearning：RWKU forget 分数、保留完成审计、终端 rollout 审计与训练动态可指向不同结论，分歧源于 reward-hacking 终点与 GRPO 策略支持限制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, anti-refusal shaping, rubric-based broad answering, and an explicit refusal contrast, with and without SFT warm-up. The experiments show that optimization success is not equivalent to behavioral unlearning: RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics can point to different conclusions. We trace these disagreements to reward-hacking endpoints, policy-support limits in GRPO, benchmark probes that miss endpoint changes, and rewards that can select broad-topic answering with low semantic leakage during optimization.

</details>

### 6. Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.11408)　📅 2026-08

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Zirui Song、…、Xiuying Chen

- 🎯 **研究动机**：unlearning 后的残余内部信号能否预测未来恢复、能否直接当优化目标未知
- 🔬 **研究方法**：J-Access 用 Jacobian 视角把中间表征映射到词表，测量目标概念在输出通路上的可达性，审计 398 个公开 unlearned 模型（八种方法）
- 📌 **结论**：攻击前可达性可模型级预测恢复速度与幅度但定位不了具体事实；直接最小化 J-Access 反而让模型向审计隐藏知识、攻击后恢复更严重

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior white-box studies show that large language models can retain latent traces of target knowledge after unlearning, even when the knowledge is no longer expressed in their outputs. However, existing audits remain limited to one-off diagnostics: it is unclear whether these residual signals can predict future recovery under continued training or serve as reliable optimization targets. Resolving this gap is essential to determine whether internal auditing can move beyond post-hoc evaluation toward proactive risk monitoring and safer unlearning. We propose J-Access, an inference-time audit that uses the Jacobian lens to map intermediate representations into vocabulary space and measures how often target concepts remain accessible along the model's output pathway. We hypothesize that residual accessibility reflects recovery susceptibility: knowledge that remains closer to the output pathway requires less fine-tuning to restore, leading to faster recovery. We audit 398 public unlearned models spanning eight unlearning methods. We find that: (1) most unlearned models retain access above the retain-only gold level; (2) pre-attack accessibility predicts recovery speed and extent at the model level, but cannot identify which specific facts will be recovered; and (3) directly minimizing J-Access does not promote genuine deletion. Instead, the model learns to hide knowledge from the audit, producing lower audit scores but greater post-attack recovery. These findings position J-Access as a model-level diagnostic for assessing residual susceptibility in unlearned models. We argue internal audits should serve as an independent diagnostic dimension in unlearning evaluation, and should not be converted into optimization targets without validation.

</details>

### 7. PRMU: A Corpus-Free Benchmark for Person-Centric Knowledge Unlearning in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.11149)　📅 2026-08

**关键词**：`benchmark`、`machine unlearning`、`adversarial robustness`、`VLM safety`

👤 **作者**：Huafeng Chen、…、Caifeng Shan

- 🎯 **研究动机**：MLLM 人物知识的现实删除场景常无原始遗忘/保留语料，现有 unlearning 方法假设可访问语料
- 🔬 **研究方法**：PRMU 基准评测 corpus-free 人物中心遗忘，含文本与视觉探针、对抗评估与细粒度 locality 分析；SGPE 基线做相似度门控投影编辑
- 📌 **结论**：现有方法遗忘-局部性权衡不佳、激进遗忘下局部性明显退化且易被多模态知识重激活；SGPE 在目标遗忘、局部性与通用效用间取得竞争性权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in storing and recalling rich person-related knowledge, raising increasing concerns about reliable knowledge removal. However, existing machine unlearning approaches for MLLMs typically assume access to original forget and retain corpora, which are often unavailable in realistic deletion scenarios. To address this limitation, we introduce PRMU, a benchmark for evaluating corpus-free multimodal unlearning under realistic person-centric deletion requests. PRMU focuses on naturally acquired person-related knowledge and evaluates whether models can remove target knowledge while preserving related knowledge through diverse textual and visual probes, including adversarial evaluation and fine-grained locality analysis. To facilitate research in this setting, we further introduce Similarity-Gated Projection Editing (SGPE), a lightweight corpus-free unlearning baseline with knowledge displacement, protected parameter-space editing, and locality-aware multimodal control. Extensive experiments on representative MLLMs reveal that existing unlearning methods often suffer from unfavorable forgetting-locality trade-offs, with significant locality degradation under aggressive forgetting settings, and remain vulnerable to multimodal knowledge reactivation. Meanwhile, SGPE provides a competitive trade-off between target forgetting, locality preservation, and general multimodal utility. We hope PRMU can facilitate future research toward realistic and scalable multimodal machine unlearning. Code and dataset will be released at https://github.com/2231122/PRMU.

</details>

### 8. Machine Unlearning on Trajectory Data: An Experimental Analysis

🌐 [Project](https://doi.org/10.1145/3770855.3817450)　📅 2026-08　🏷 KDD 2026

**关键词**：`benchmark`、`trajectory unlearning`、`deletion evaluation`、`privacy`

- 🎯 **研究动机**：轨迹数据的机器遗忘效果缺系统评估
- 🔬 **研究方法**：在多轨迹数据集上实验分析遗忘算法的删除与隐私表现
- 📌 **结论**：揭示现有方法在轨迹场景的失效模式

### 9. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2607.02513) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`benchmark`、`PII unlearning`、`resurfacing attack`、`machine unlearning`、`parameter localization`

👤 **作者**：Matteo Boglioni、Thibault Rousset、Siva Reddy、Marius Mosbach、Verna Dankers

- 🎯 **研究动机**：现有 unlearning 基准只评估输出层，无法区分知识被真正擦除还是被混淆，resurfacing 攻击的成功加重疑虑
- 🔬 **研究方法**：构建 LACUNA 测试床：经掩码持续预训练把合成个体 PII 注入 OLMo 1B/7B 预定义参数，提供真值参数级定位，直接检验 SOTA 方法是否命中存储知识的权重
- 📌 **结论**：现有方法输出层表现强但定位高度不精确且易受 resurfacing 攻击；定位准确时简单梯度法即可强擦除并抗复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's parameters or merely obfuscates it, a concern reinforced by the success of resurfacing attacks. To bridge this gap, we introduce LACUNA: the first unlearning testbed with ground-truth parameter-level localization. LACUNA injects PII of synthetic individuals into predefined parameters of 1B and 7B OLMo-based models via masked continual pretraining, enabling direct evaluation of whether unlearning targets the weights responsible for knowledge storage. We use LACUNA to benchmark current SOTA unlearning methods and find that, despite strong output-level performance, existing methods are highly imprecise and susceptible to resurfacing attacks. We further show that when localization is successful, even a simple gradient-based unlearning method achieves strong erasure and robustness to resurfacing attacks, highlighting the importance of precise unlearning. We release LACUNA to complement behavioral evaluations and drive further advances in robust, localization-based unlearning.

</details>

### 10. MLUBench: A Benchmark for Lifelong Unlearning Evaluation in MLLMs

📄 [arXiv](https://arxiv.org/abs/2606.12809) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66183)　📅 2026-06　🏷 ICML 2026

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：He Li、…、Bo Han

- 🎯 **研究动机**：数据删除请求随时间序列到达形成 MLLM Lifelong Unlearning 问题，已有基准规模与范围不足，且 continual unlearning 可能破坏多模态对齐
- 🔬 **研究方法**：构建 MLUBench：127 实体、9 类、终身删除请求，并提出 LUMoE 方法缓解累积退化
- 📌 **结论**：已有 unlearning 方法存在严重累积退化；从单一模态持续遗忘会拖垮整个模型，LUMoE 显著缓解该问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) are trained on massive multimodal data, making data unlearning increasingly important as data owners may request the removal of specific content. In practice, these requests often arrive sequentially over time, giving rise to the challenging problem of MLLM Lifelong Unlearning. However, most existing benchmarks are limited in scale and scope, failing to capture the complexities of MLLM lifelong unlearning. To fill this gap, we introduce the MLUBench, a large-scale and comprehensive benchmark featuring 127 entities across 9 classes under lifelong unlearning requests. We perform extensive experiments using MLUBench and reveal that existing unlearning methods suffer from severe, cumulative degradation. More critically, we further identify the unique challenge of this problem: unlike in unimodal models, MLLM lifelong unlearning is constrained by the need to preserve multimodal alignment. Continually unlearning from one modality could degrade the entire model. To alleviate this challenge, we propose LUMoE, an effective method. Experiments demonstrate that LUMoE significantly mitigates the degradation problem faced by baselines. The source code and the MLUBench dataset are open-sourced in https://github.com/lihe-maxsize/Lifelong_Unlearning_main.

</details>

### 11. Auditing Language Model Unlearning via Information Decomposition

🎓 [Official](https://aclanthology.org/2026.eacl-long.35/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`unlearning audit`、`residual information`、`reconstruction risk`、`machine unlearning`、`information decomposition`

👤 **作者**：Anmol Goel、Alan Ritter、Iryna Gurevych

- 🎯 **研究动机**：机器遗忘算法表面成功后，遗忘数据的信息仍可从内部表征线性解码
- 🔬 **研究方法**：用 Partial Information Decomposition 比较遗忘前后表征，把与遗忘数据的互信息分解为已遗忘与残余知识：跨模型共享的冗余信息即残余知识且与重建攻击易感性相关
- 📌 **结论**：提出表征级风险分数指导推理时对敏感输入弃权，缓解隐私泄露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We expose a critical limitation in current approaches to machine unlearning in language models: despite the apparent success of unlearning algorithms, information about the forgotten data remains linearly decodable from internal representations. To systematically assess this discrepancy, we introduce an interpretable, information-theoretic framework for auditing unlearning using Partial Information Decomposition (PID). By comparing model representations before and after unlearning, we decompose the mutual information with the forgotten data into distinct components, formalizing the notions of unlearned and residual knowledge. Our analysis reveals that redundant information, shared across both models, constitutes residual knowledge that persists post-unlearning and correlates with susceptibility to known adversarial reconstruction attacks. Leveraging these insights, we propose a representation-based risk score that can guide abstention on sensitive inputs at inference time, providing a practical mechanism to mitigate privacy leakage. Our work introduces a principled, representation-level audit for unlearning, offering theoretical insight and actionable tools for safer deployment of language models.

</details>

### 12. Unlearning Isn’t Forgetting: Revealing Hidden Leakage in Class Unlearning Evaluations

🎓 [Official](https://icml.cc/virtual/2026/poster/60958)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Ali Ebrahimpour-Boroojeny、Yian Wang、Hari Sundaram

- 🎯 **研究动机**：类遗忘评估忽略底层类几何，导致遗忘类信息泄露
- 🔬 **研究方法**：提出 CMIA 用邻近类概率检测遗忘样本；提出 TREW 微调目标，按估计的类间相似度倾斜目标分布以逼近重训模型在遗忘类输入上的剩余类分布
- 📌 **结论**：多基准上 TREW 匹配或超越现有方法；CIFAR-10 上与重训模型的 U-LiRA、CMIA 差距分别缩小 19% 与 46%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we reveal a significant shortcoming in class unlearning evaluations: overlooking the underlying class geometry can cause information leakage about the forgotten class. We further propose a simple unlearning strategy to mitigate this issue. We introduce Class Membership Inference Attack (CMIA) that uses the probabilities the model assigns to neighboring classes to detect unlearned samples. We find that existing unlearning methods are vulnerable to CMIA across multiple datasets. We then propose a new fine-tuning objective that mitigates this privacy leakage by approximating, for forget-class inputs, the distribution over the remaining classes that a retrained-from-scratch model would produce. To construct this approximation, we estimate inter-class similarity and tilt the target model’s distribution accordingly. The resulting Tilted REWeighting (TREW) distribution serves as the desired distribution during fine-tuning. We also show that across multiple benchmarks, TREW matches or surpasses existing unlearning methods on prior unlearning metrics. More specifically, on CIFAR-10, it reduces the gap with retrained models by $19\%$ and $46\%$ for U-LiRA and CMIA scores, accordingly, compared to the SOTA method for each category.

</details>

### 13. Unlearners Can Lie: Evaluating and Improving Honesty in LLM Unlearning

🎓 [Official](https://aclanthology.org/2026.acl-long.548/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`、`deceptive behavior`、`knowledge removal`

👤 **作者**：Renjie Gu、Jiazhen Du、Yihua Zhang、Sijia Liu

- 🎯 **研究动机**：现有 LLM 遗忘方法常幻觉、生成异常 token 序列或行为不一致，遗忘的诚实性缺乏定义与评估
- 🔬 **研究方法**：形式化定义遗忘诚实性并给出覆盖效用、保留集诚实性、遗忘有效性、拒绝率与拒绝稳定性的指标套件；提出表示对齐流程 ReVa 微调特征随机化后的遗忘模型
- 📌 **结论**：9 种方法、3 个模型家族全部不达标；ReVa 在 forget 集 QA 上两轮交互后拒绝率最高、近第二名两倍，同时提升保留集诚实性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning in large language models (LLMs) aims to remove harmful training data while preserving overall utility. However, we find that existing methods often hallucinate, generate abnormal token sequences, or behave inconsistently, raising safety and trust concerns. According to prior literature on LLM honesty, such behaviors are often associated with dishonesty. This motivates us to investigate the notion of honesty in the context of model unlearning. We propose a formal definition of unlearning honesty, which includes: (1) preserving both utility and honesty on retained knowledge, and (2) ensuring effective forgetting while encouraging the model to acknowledge its limitations and respond consistently to questions related to forgotten knowledge. To systematically evaluate the honesty of unlearning, we introduce a suite of metrics that cover utility, honesty on the retained set, effectiveness of forgetting, rejection rate and refusal stability in Q&A and MCQ settings. Evaluating 9 methods across 3 mainstream families shows that all current methods fail to meet these standards. After experimental and theoretical analyses, we present ReVa, a representation-alignment procedure that fine-tunes feature-randomized unlearned models to better acknowledge forgotten knowledge. On Q A tasks from the forget set, ReVa achieves the highest rejection rate after two rounds of interaction, nearly doubling the performance of the second-best method. Remarkably, It also improves honesty on the retained set.

</details>

### 14. Knowledge Beyond Language: Bridging the Gap in Multilingual Machine Unlearning Evaluation

🎓 [Official](https://aclanthology.org/2026.acl-long.1105/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`machine unlearning`、`deletion guarantee`、`utility retention`、`knowledge removal`

👤 **作者**：Kyomin Hwang、Hyeonjin Kim、Sangyeon Cho、Nojun Kwak

- 🎯 **研究动机**：多语言机器遗忘评测只是单语言协议的直接扩展，未刻画信息跨语言分布
- 🔬 **研究方法**：提出 Knowledge Separability Score（多语言总体遗忘质量）与 Knowledge Persistence Score（语言对间一致移除）两个指标并评测多种遗忘方法
- 📌 **结论**：揭示 MMU 特有的现象（如跨语言遗忘不一致），为评测提供新视角

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While LLMs are increasingly used in commercial services, they pose privacy risks such as leakage of sensitive personally identifiable information (PII). For LLMs trained on multilingual corpora, Multilingual Machine Unlearning (MMU) aims to remove information across multiple languages. However, prior MMU evaluations fail to capture such cross-linguistic distribution of information, being largely limited to direct extensions of per-language evaluation protocols. To this end, we propose two metrics to evaluate the information spread across languages: the Knowledge Separability Score (KSS) and the Knowledge Persistence Score (KPS). KSS measures the overall unlearning quality across multiple languages, while KPS more specifically aims to assess consistent removal of information among different language pairs. We evaluated various unlearning methods in the multilingual setting with these metrics and conducted comprehensive analyses. Through our investigation, we provide insights into unique phenomena exclusive to MMU and offer a new perspective on MMU evaluation.

</details>

### 15. SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning

📄 [arXiv](https://arxiv.org/abs/2603.26316) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Selvas-Sala_SALMUBench_A_Benchmark_for_Sensitive_Association-Level_Multimodal_Unlearning_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`multimodal unlearning`、`sensitive association`、`privacy evaluation`

👤 **作者**：Cai Selvas-Sala、Lei Kang、Lluis Gomez

- 🎯 **研究动机**：对比训练编码器（如 CLIP）的机器遗忘研究不足，现有评测无法诊断细粒度关联级遗忘
- 🔬 **研究方法**：构建 SALMUBench：基于 60K 人设-属性关联合成数据，从同一 400M 对保留集从头训练被污染模型与干净模型，用结构化 holdout 精确测量遗忘效果与附带损伤
- 📌 **结论**：效用高效的删除可行，但现有方法要么遗忘不彻底、要么过度泛化删除超出预期内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As multimodal models like CLIP become integral to downstream systems, the need to remove sensitive information is critical. However, machine unlearning for contrastively-trained encoders remains underexplored, and existing evaluations fail to diagnose fine-grained, association-level forgetting. We introduce SALMUBench (Sensitive Association-Level Multimodal Unlearning), a benchmark built upon a synthetic dataset of 60K persona-attribute associations and two foundational models: a Compromised model polluted with this data, and a Clean model without it. To isolate unlearning effects, both are trained from scratch on the same 400M-pair \texttt retain base, with the Compromised model additionally trained on the \texttt sensitive set. We propose a novel evaluation protocol with structured holdout sets (\texttt holdout_identity, \texttt holdout_association ) to precisely measure unlearning efficacy and collateral damage. Our benchmark reveals that while utility-efficient deletion is feasible, current methods exhibit distinct failure modes: they either fail to forget effectively or over-generalize by erasing more than intended. SALMUBench sets a new standard for comprehensive unlearning evaluation, and we publicly release our dataset, models, evaluation scripts, and leaderboards to foster future research.

</details>

### 16. Incentivizing Truthful Machine Unlearning via Hierarchical Auditing

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7556.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`analysis`、`unlearning audit`、`incentive design`、`truthful compliance`

- 🎯 **研究动机**：验证营利性 AI 服务是否忠实执行 unlearning 的方法要么成本过高要么威慑不足
- 🔬 **研究方法**：UAG 博弈论审计框架：低成本筛查加触发式高精度验证的层级审计，把服务器-审计方交互建模为三阶段动态贝叶斯博弈并求均衡审计与惩罚策略
- 📌 **结论**：仅筛查约 50% unlearning 请求即达约 95% 服务器诚实率，兼顾成本与威慑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning has become a critical capability for AI services to comply with evolving privacy regulations. A key yet underexplored challenge is how to verify whether a profit-driven AI server has faithfully performed unlearning. Existing verification approaches either incur prohibitive costs or provide insufficient deterrence, failing to balance audit cost and enforcement effectiveness. To bridge this gap, we propose UAG, a game-theoretic unlearning auditing framework that incentivizes truthful unlearning via strategic deterrence rather than exhaustive verification. We design a hierarchical auditing mechanism that combines low-cost screening with selectively triggered high-precision verification, and models the server–auditor interaction as a three-stage dynamic Bayesian game. By characterizing the equilibrium strategy, we derive optimal audit and penalty policies that incentivize honest unlearning. Theoretical analysis and experiments show that UAG maintains reliable detection while achieving a favorable cost–deterrence tradeoff. Notably, UAG attains a server honesty rate of approximately 95% while screening only about 50% of unlearning requests, showing its practicality for trustworthy black-box unlearning services.

</details>

### 17. Evaluating Deep Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2410.15153) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2024-10　🏷 SaTML 2026

**关键词**：`benchmark`、`LLM unlearning`、`deductive knowledge`、`forgetting evaluation`

👤 **作者**：Ruihan Wu、Chhavi Yadav、Russ Salakhutdinov、Kamalika Chaudhuri

- 🎯 **研究动机**：事实遗忘多只删目标事实，忽略其可经保留知识与推理被演绎推出
- 🔬 **研究方法**：提出深度遗忘设定与 Success-DU、Recall、Accuracy 三指标，用 MQuAKE 与多步演绎数据集 Eval-DU 基准化
- 📌 **结论**：现有方法要么遗忘不深、要么过度删除无关事实，需专门算法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning has emerged as an important component in developing safe and trustworthy models. Prior work on fact unlearning in LLMs has mostly focused on removing a specified target fact robustly, but often overlooks its deductive connections to other knowledge. We propose a new setting for fact unlearning, deep unlearning, where the goal is not only to remove a target fact but also to prevent it from being deduced via retained knowledge in the LLM and logical reasoning. We propose three novel metrics: Success-DU and Recall to measure unlearning efficacy, and Accuracy to measure the remainder model utility. To benchmark this setting, we leverage both (1) an existing real-world knowledge dataset, MQuAKE, that provides one-step deduction instances, and (2) newly construct a novel semi-synthetic dataset, Eval-DU, that allows multiple steps of realistic deductions among synthetic facts. Experiments reveal that current methods struggle with deep unlearning: they either fail to deeply unlearn, or excessively remove unrelated facts. Our results suggest that targeted algorithms may have to be developed for robust/deep fact unlearning in LLMs.

</details>

### 18. AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.28312) · 🤗 [Model](https://huggingface.co/WonjunLee/AIM_MLLM_Unlearning)　📅 2026-08

**关键词**：`defense`、`analysis`、`identity memorization`、`privacy deletion`、`retain-free MLLM`、`MLLM identity unlearning`

👤 **作者**：Wonjun Lee、Jaehyuk Jang、Kangwook Ko、Hee-Seon Kim、Changick Kim

- 🎯 **研究动机**：MLLM 会记忆微调数据中的身份事实带来隐私删除需求，但现有 unlearning 方法多假定删除时可访问 retain 图像或真值答案，现实中不可得
- 🔬 **研究方法**：发现身份问题与视觉感知问题在微调 hidden state 中分区且组织方式不同（按人 vs 按题型）；提出两阶段 AIM：以通用视觉 prompt 锚定身份遗忘目标，再在 Fisher 约束下把 vision encoder 匹配到该目标
- 📌 **结论**：无需 retain 数据即实现有竞争力的身份遗忘，同时保留未删除身份、既有知识与同图像视觉感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a person requests deletion. Existing MLLM unlearning methods often assume access to retain images or ground-truth answers during deletion, which is unrealistic in many practical scenarios. We study identity unlearning when retain images are unavailable at deletion time. Our analysis shows that identity and visual-perception questions occupy distinct regions in fine-tuned hidden states and are organized differently: identity questions cluster by person, whereas perception questions cluster by question type. This suggests that identity knowledge can be suppressed without erasing general visual perception. Building on this observation, we propose AIM, a two-stage method that anchors an identity-forgetting target with a universal visual prompt and then matches the vision encoder to that target under a Fisher-based constraint. Extensive experiments show that AIM achieves competitive identity forgetting while preserving non-deleted identities, prior knowledge, and visual perception on the same images.

</details>

### 19. LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection

📄 [arXiv](https://arxiv.org/abs/2608.11691)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`VLM safety`、`cyber misuse`

👤 **作者**：Xinhao Zhong、Yuxia Qiao、Junhao Li、Hao Fang、Yi Sun、Bin Chen

- 🎯 **研究动机**：RL 训练的多模态大推理模型即使最终答案已遗忘，推理轨迹仍可能复现敏感事实，且原生 RL 模型泄漏更重
- 🔬 **研究方法**：发现 RL 探索给敏感内容留下基座模型没有的 token 级熵签名；LEMUR 免训练推理时用熵动态定位敏感推理区间并以熵调制视觉锚潜注入重定向推理轨迹
- 📌 **结论**：跨多个 MLRM 一致优于现有 unlearning 方法，同时抑制推理轨迹与答案泄漏并更好保留非敏感效用与流畅度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement-learning (RL) post-training equips multimodal large reasoning models (MLRMs) with exploratory chains of thought (CoT), substantially improving visual reasoning. However, we find that this capability introduces a distinct privacy vulnerability: even when a sensitive fact is successfully unlearned from the final answer, the model may still reproduce it in its reasoning trace. This leakage is substantially more pronounced in natively RL-trained MLRMs than in their non -reasoning base models, revealing a privacy risk that existing unlearning methods are not designed to address. We show that RL-induced exploration leaves sensitive content with a distinctive token-level entropy signature that is largely absent from base models. Based on this observation, we propose LEMUR, a fully training-free, inference-time unlearning framework for natively RL-trained multimodal models. LEMUR uses entropy dynamics as a control signal to identify when sensitive reasoning begins and when sanitization should stop. During this interval, it redirects the reasoning trajectory through entropy-modulated visual-anchor latent injection, replacing committed tokens with sanitized, probability-weighted embeddings re-grounded in the input image. Across diverse MLRMs, LEMUR consistently outperforms existing unlearning met hods in suppressing both reasoning-trace and answer leakage, while better preserving non-sensitive utility and output fluency. These results demonstrate that RL-induced entropy dynamics provide a distinctive signal for privacy leakage and that exploiting this signal enables effective training-free unlearning for reasoning-capable multimodal models.

</details>

### 20. Which Concepts to Forget and How to Refuse? Decomposing Concepts for Continual Unlearning in Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.21484) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Which_Concepts_to_Forget_and_How_to_Refuse_Decomposing_Concepts_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`continual unlearning`、`concept decomposition`、`safe refusal`

👤 **作者**：Hyundong Jin、Dongyoon Han、Eunwoo Kim

- 🎯 **研究动机**：顺序 unlearning 更新扭曲共享表示，产生视觉-语言对与拒答行为的伪关联，导致不当拒答
- 🔬 **研究方法**：把删除目标分解为细粒度视觉/文本概念：概念调制器识别遗忘类别的概念组合，混合拒答专家经概念驱动路由生成概念对齐拒答
- 📌 **结论**：跨 unlearning 序列生成概念接地的拒答并更好保留通用效用，优于既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual unlearning poses the challenge of enabling large vision-language models to selectively refuse specific image-instruction pairs in response to sequential deletion requests, while preserving general utility. However, sequential unlearning updates distort shared representations, creating spurious associations between vision-language pairs and refusal behaviors that hinder precise identification of refusal targets, resulting in inappropriate refusals. To address this challenge, we propose a novel continual unlearning framework that grounds refusal behavior in fine-grained descriptions of visual and textual concepts decomposed from deletion targets. We first identify which visual-linguistic concept combinations characterize each forget category through a concept modulator, then determine how to generate appropriate refusal responses via a mixture of refusal experts, termed refusers, each specialized for concept-aligned refusal generation. To generate concept-specific refusal responses across sequential tasks, we introduce a multimodal, concept-driven routing scheme that reuses refusers for tasks sharing similar concepts and adapts underutilized ones for novel concepts. Extensive experiments on vision-language benchmarks demonstrate that the proposed framework outperforms existing methods by generating concept-grounded refusal responses and preserving the general utility across unlearning sequences.

</details>

### 21. SGPVT: Self-Generated Proximal Visual Tokens for Mitigating Proximal Collateral Damage in MLLM Unlearning

🎓 [Official](https://aclanthology.org/2026.acl-long.442/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`multimodal safety`、`knowledge removal`

👤 **作者**：Jiaqi Li、…、Guilin Qi

- 🎯 **研究动机**：MLLM 遗忘研究只看整体效用指标，忽视语义邻近概念的附带损伤；分析发现遗忘脆弱性与视觉嵌入相似度在语义空间平滑强相关
- 🔬 **研究方法**：引入目标概念邻域的合成扰动视觉表示 SGPVT，配合自适应余弦带课程与双流目标：梯度上升遗忘目标，冻结教师向邻近 token 蒸馏防退化
- 📌 **结论**：有效遗忘目标的同时显著更好保留语义相关概念，且无需人工整理保留集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning in multimodal large language models (MLLMs) aims to remove specific concepts while preserving overall utility. However, existing approaches focus primarily on general utility metrics, overlooking the preservation of semantically related concepts. We present the first systematic analysis of this proximal collateral damage, revealing that forgetting vulnerability correlates strongly with visual embedding similarity in a smooth gradient across the semantic space. Based on this insight, we propose a novel unlearning framework that introduces Self-Generated Proximal Visual Tokens (SGPVTs), which are synthetically perturbed visual representations around the target concept. Our method employs an adaptive cosine-band curriculum with a dual-stream objective: forgetting the target via gradient ascent while distilling knowledge from a frozen teacher model into proximal tokens to prevent degradation. Extensive experiments demonstrate that our approach significantly outperforms existing methods in preserving semantically related concepts while achieving effective target unlearning, eliminating the need for manual retention set curation. Our source code will be released in the near future.

</details>

### 22. LOTUS: Evolving Multimodal Unlearning via Hyperbolic Entailment and Lorentz Transport

🎓 [Official](https://aclanthology.org/2026.acl-long.2195/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`multimodal safety`、`machine unlearning`、`VLM safety`、`knowledge removal`

👤 **作者**：Zekun Wang、Jingjie Zeng、Yingxu Li、Hongfei Lin (林鸿飞)、Liang Yang (杨亮)

- 🎯 **研究动机**：欧式遗忘范式几何失配，无法解耦特定实例与一般概念，导致灾难性遗忘或不安全替换
- 🔬 **研究方法**：LOTUS 在 Lorentz 流形上用 Inverted Entailment Cone Loss 切断敏感概念继承，Lorentz Transport 在切空间对齐剪枝特征并以安全拒答先验兼容欧式骨干
- 📌 **结论**：MLLMU-Bench（LLaVA、Qwen）上显著超基线，擦除目标视觉数据同时保留通用效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) face critical privacy challenges due to the indiscriminate memorization of sensitive data. Existing unlearning methods, largely adapted from Euclidean paradigms, suffer from a geometric mismatch: they fail to disentangle specific instances from general concepts, causing catastrophic forgetting or unsafe substitution. We introduce LOTUS (Lorentz Transport for Unlearning Strategies), a framework for surgical semantic pruning within the Lorentz manifold. Leveraging hyperbolic geometry’s hierarchical nature, LOTUS employs an Inverted Entailment Cone Loss to sever the inheritance of sensitive concepts and a Lorentz Transport mechanism to align pruned features within the tangent space, ensuring compatibility with Euclidean backbones via a safety refusal prior. Experiments on MLLMU-Bench with LLaVA and Qwen show that LOTUS significantly outperforms baselines, effectively erasing targeted visual data while preserving general utility.

</details>

### 23. Beyond Sample-Level Forgetting: Improving Reliability in Multimodal Unlearning

🎓 [Official](https://icml.cc/virtual/2026/poster/65780)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`VLM safety`、`deletion guarantee`、`causal analysis`、`deletion verification`

👤 **作者**：Jianzhou Wang、Yirui Wu、Lixin Yuan、WENXIAO ZHANG、Jun Liu

- 🎯 **研究动机**：多模态遗忘因单模态与多模态知识的复杂相互依赖，难以兼顾有效性、可靠性与局部性
- 🔬 **研究方法**：以因果视角解耦知识组件：Multimodal Variational Inference 从不完整观测推断模态特定与模态一致因子，对比语义编辑实现精细遗忘
- 📌 **结论**：隐私与版权敏感场景上验证有效，遗忘模型保持高可靠性与局部性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal unlearning aims to eliminate specific data from pretrained multimodal models, which offers significant advantages in data privacy and model efficiency. Current methods struggle to achieve the desired properties of effectiveness, reliability and locality, due to the complex interdependency of unimodal and multimodal knowledge. By introducing a causal perspective, we propose multimodal unlearning with decoupled knowledge components. To promote fine-grained understanding of multimodal context, we introduce Multimodal Variational Inference (MVI) to infer modal-specific and -consistent factors with incomplete sample observation. With foundation of decoupled knowledge, we propose contrastive semantic editing to regulate multimodal unlearning towards refined forgetting. Experiments on privacy- and copyright-sensitive scenarios validate effectiveness of our method across multiple scenarios, ensuring the unlearned model maintains high reliability and locality.

</details>

### 24. ASRU: Activation Steering Meets Reinforcement Unlearning for Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.15687) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65450)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`VLM safety`、`deletion guarantee`、`representation steering`、`deletion verification`

👤 **作者**：Jiahui Guang、…、Zhaoquan Gu

- 🎯 **研究动机**：现有 MLLM 遗忘方法只看输出偏差、忽视遗忘后生成质量，易导致幻觉或僵硬回复
- 🔬 **研究方法**：ASRU 先经激活重定向诱导初始拒绝行为，再用定制奖励函数优化细粒度拒绝边界，把生成质量纳入核心评估目标
- 📌 **结论**：Qwen3-VL 上遗忘效果平均提升 24.6%、生成质量平均提升 5.8 倍，仅用少量保留监督数据即维持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) may memorize sensitive cross-modal information during pretraining, making machine unlearning (MU) crucial. Existing methods typically evaluate unlearning effectiveness based on output deviations, while overlooking the generation quality after unlearning. This can easily lead to hallucinated or rigid responses, thereby affecting the usability and safety of the unlearned model. To address this issue, we propose ASRU, a controllable multimodal unlearning framework that incorporates generation quality as a core evaluation objective. ASRU first induces initial refusal behavior through activation redirection, and then optimizes fine-grained refusal boundaries using a customized reward function, thereby achieving a better trade-off between target knowledge unlearning and model utility. Experiments on Qwen3-VL show that ASRU significantly improves unlearning effectiveness (+24.6%) on average and generation quality (5.8×) on average while effectively preserving model utility, using only a small amount of retained supervision data.

</details>

### 25. $\oslash$ Source Models Leak What They Shouldn't $\nrightarrow$: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Devalapally_oslash_Source_Models_Leak_What_They_Shouldnt_nrightarrow_Unlearning_Zero-Shot_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`source-model leakage`、`domain adaptation`、`machine unlearning`

👤 **作者**：Arnav Devalapally、Poornima Jain、Kartik Srinivas、Vineeth N. Balasubramanian

- 🎯 **研究动机**：源自由域适应的模型在目标域对源域独有类零样本表现强，无意泄露源域敏感类知识；现有遗忘不处理分布偏移
- 🔬 **研究方法**：提出 SCADA-UL 设定，在适配过程中用对抗生成的遗忘类样本与重标度标签策略遗忘；扩展到持续版与遗忘类未知版
- 📌 **结论**：一致超基线并在基准数据集达重训练级遗忘性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing adaptation of vision models across domains, such as satellite imagery and medical scans, has raised an emerging privacy risk: models may inadvertently retain and leak sensitive source-domain specific information in the target domain. This creates a compelling use case for machine unlearning to protect the privacy of sensitive source-domain data. Among adaptation techniques, source-free domain adaptation (SFDA) calls for an urgent need for machine unlearning (MU), where the source data itself is protected, yet the source model exposed during adaptation encodes its influence. Our experiments reveal that existing SFDA methods exhibit strong zero-shot performance on source-exclusive classes in the target domain, indicating they inadvertently leak knowledge of these classes into the target domain, even when they are not represented in the target data. We identify and address this risk by proposing an MU setting called SCADA-UL: Unlearning Source-exclusive ClAsses in Domain Adaptation. Existing MU methods do not address this setting as they are not designed to handle data distribution shifts. We propose a new unlearning method, where an adversarially generated forget class sample is unlearned by the model during the domain adaptation process using a novel rescaled labeling strategy and adversarial optimization.We also extend our study to two variants: a continual version of this problem setting and to one where the specific source classes to be forgotten may be unknown.Alongside theoretical interpretations, our comprehensive empirical results show that our method consistently outperforms baselines in the proposed setting while achieving retraining-level unlearning performance on benchmark datasets. Code is available at https://github.com/D-Arnav/SCADA

</details>

### 26. Unlearning without Forgetting: Securely Removing Targeted Concepts from Large-Scale Vision-Language Open-Vocabulary Detectors

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Unlearning_without_Forgetting_Securely_Removing_Targeted_Concepts_from_Large-Scale_Vision-Language_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`targeted unlearning`、`open-vocabulary detector`、`utility preservation`

👤 **作者**：Zhongze Wu、…、Jun Long

- 🎯 **研究动机**：开放词汇检测器的可分解嵌入共享语义因子，遗忘更新不可避免扭曲保留知识，造成几何纠缠干扰
- 🔬 **研究方法**：提出 SafeDetect：离线由保留知识嵌入构造零空间，把参数更新约束在其正交补；一步 mean-flow 目标实现遗忘并以多模态解耦防跨模态恢复；建立 UOD-Bench（14.7K 图像、67.3K 区域-短语对）
- 📌 **结论**：遗忘效果较 NPO 提升 64.75%，保留性能稳定、零样本泛化更优，收敛快 1.5 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-vocabulary detectors (OvOD) inherit tightly coupled cross-modal knowledge from web-scale pretraining, creating privacy, copyright, and compliance risks. Existing machine unlearning methods face geometric entanglement interference in OvOD: forgetting updates inevitably distort preserved knowledge due to shared semantic factors in decomposable embeddings. We introduce SafeDetect, a geometrically constrained unlearning framework that constructs a null-space from preserved knowledge embeddings offline, then constrains parameter updates to this orthogonal complement, mathematically preventing interference with retained concepts. Forgetting is achieved through a one-step mean-flow objective that drives forgotten concepts toward non-detectable, while multimodal decoupling prevents cross-modal recovery. We establish UOD-Bench, the first unified benchmark for OvOD unlearning, featuring 14.7K images with 67.3K region-phrase pairs across three tasks. Extensive experiments across UOD-Bench and standard benchmarks with diverse architectures (e.g., GroundingDINO, LLM-Det) demonstrate that SafeDetect achieves superior forgetting efficacy (64.75% improvement over NPO) while maintaining stable retention performance and significantly better zero-shot generalization, with 1.5x faster convergence than iterative methods.

</details>

### 27. VL-Eraser: Vacuum Distillation for Machine Unlearning in Vision-Language Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_VL-Eraser_Vacuum_Distillation_for_Machine_Unlearning_in_Vision-Language_Models_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`vision-language unlearning`、`vacuum distillation`、`forgetting verification`

👤 **作者**：Yili Wang、Lu Dai、Tairan Huang、Yijie Xu、Hui Xiong

- 🎯 **研究动机**：传统遗忘方法破坏跨模态对齐，多模态场景下遗忘不彻底
- 🔬 **研究方法**：提出 VL-Eraser 两阶段范式：真空蒸馏把不想要的知识从 VLM 复杂参数中解耦并转移到低秩 LoRA，随后删除 LoRA 参数即完成遗忘
- 📌 **结论**：多基准上遗忘效果与效用保持均优于 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) aims to remove sensitive or undesired content from pre-trained models. Existing MU methods are commonly characterized as gradually degrading model performance on undesired data to realize approximate forgetting. Despite their successes, the effectiveness in multimodal unlearning tasks remains largely unexplored. In this paper, we first conduct an in-depth analysis and reveal that traditional MU methods tend to disrupt cross-modal alignment, leading to incomplete forgetting in multimodal scenarios. To tackle this challenge, we propose VL-Eraser, a novel unlearning paradigm for VLM unlearning. VL-Eraser reformulates unlearning in VLMs as a two-stage process: distillation and deletion. Specifically, VL-Eraser first introduces a vacuum distillation that disentangles undesired knowledge from the intricate parameters of VLMs and transfers it into low-rank adapters (LoRA). After distillation, unlearning is efficiently achieved by deleting the LoRA parameters from the original model. Extensive experiments across multiple benchmarks demonstrate that VL-Eraser achieves superior unlearning performance while preserving utility compared to the state-of-the-art baselines.

</details>

### 28. Towards Reasoning-Preserving Unlearning in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2512.17911) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Reasoning-Preserving_Unlearning_in_Multimodal_Large_Language_Models_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`defense`、`multimodal unlearning`、`reasoning preservation`、`sensitive knowledge`

👤 **作者**：Hongji Li、…、Lijie Hu

- 🎯 **研究动机**：推理型 MLLM 的 unlearning 中间 CoT 仍可泄漏敏感信息，过激干预又损害通用推理，且无联合评测基准
- 🔬 **研究方法**：提出 RMLLMU-Bench 扩展遗忘指标以度量推理泄漏与推理保留，并提出免训练推理时框架 R-MUSE，以子空间引导与自适应 steering 同时遗忘答案与推理轨迹并显式保留推理能力
- 📌 **结论**：现有方法要么留下大量推理泄漏要么严重损推理；R-MUSE 取得遗忘与推理保留的更优平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to erase requested data from trained models without full retraining. For Reasoning Multimodal Large Language Models (RMLLMs), this is uniquely challenging: intermediate chain-of-thought steps can still leak sensitive information even when final answers are forgotten, and overly aggressive interventions easily damage general reasoning ability. Yet no benchmark jointly evaluates how well unlearning methods suppress reasoning-level leakage while preserving reasoning competence. We address this gap with RMLLMU-Bench, the first benchmark for RMLLM unlearning that extends standard forgetting metrics with dedicated measures of reasoning leakage and reasoning retention. A systematic evaluation on RMLLMU-Bench reveals that existing unlearning methods for MLLMs and Large (Language) Reasoning Models (LRMs) either leave substantial leakage in the reasoning process or severely degrade reasoning performance. To address these gaps, we propose R-MUSE (Reasoning-preserving MLLM Unlearning via Subspace guidance and Adaptive Steering), a training-free and inference-time intervention framework that steers internal representations to forget both answers and reasoning traces while explicitly preserving general reasoning. Experiments on RMLLMU-Bench demonstrate that R-MUSE achieves a substantially better balance between effective forgetting and reasoning retention.

</details>

### 29. SineProject: Machine Unlearning for Stable Vision-Language Alignment

📄 [arXiv](https://arxiv.org/abs/2511.18444) · 🌐 [Project](https://openaccess.thecvf.com/content/CVPR2026/html/Garg_SineProject_Machine_Unlearning_for_Stable_Vision-Language_Alignment_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`defense`、`vision-language unlearning`、`alignment preservation`、`subspace projection`

👤 **作者**：Arpit Garg、Hemanth Saratchandran、Simon Lucey

- 🎯 **研究动机**：MLLM unlearning 常破坏视觉语言对齐而误拒良性查询，根源是 projector 的 Jacobian 病态导致优化不稳与跨模态嵌入漂移
- 🔬 **研究方法**：SineProject 给冻结 projector 增加正弦调制的可训练参数，改善 Jacobian 谱条件数以稳定 unlearning 全程对齐
- 📌 **结论**：在 LLaVA v1.5 7B/13B 的安全与隐私遗忘基准上减少良性误拒并完全遗忘目标信息，计算开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) increasingly need to forget specific knowledge such as unsafe or private information without requiring full retraining. However, existing unlearning methods often disrupt vision language alignment, causing models to reject both harmful and benign queries. We trace this failure to the projector network during unlearning, its Jacobian becomes severely illconditioned, leading to unstable optimization and drift in cross modal embeddings. We introduce SineProject, a simple method that augments the frozen projector with sinusoidally modulated trainable parameters, improving the Jacobian's spectral conditioning and stabilizing alignment throughout unlearning. Across standard safety and privacy unlearning benchmarks using LLaVA v1.5 7B and 13B, SineProject reduces benign query refusals while achieving complete forgetting of targeted information, yielding state of the art forget retain trade offs with negligible computational overhead.

</details>

### 30. ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control

📄 [arXiv](https://arxiv.org/abs/2608.23034)　📅 2026-08

**关键词**：`defense`、`restricted capability`、`trajectory boundary`、`persistent suppression`、`test-time unlearning`、`stateful boundary control`

👤 **作者**：Xunlei Chen、Qinghui Gong、Ruini Xue、Yaodong Hu、Tian Lan、Wenhong Tian

- 🎯 **研究动机**：现有 test-time unlearning 做孤立逐点激活修正，忽略自回归生成会从 prompt、cache 与生成前缀持续重构隐藏态，后续状态可能重回受限知识区
- 🔬 **研究方法**：ST²U 把 test-time unlearning 形式化为轨迹级边界控制：在低维可逆坐标建模受限知识边界且不动正交分量，推理时沿轨迹监测风险、做带上下文锚定的最小修正并跨 token 传播历史修正状态
- 📌 **结论**：三个 benchmark、三个模型家族上整体平衡最佳，受限知识 re-entry 从基线 46.50–59.10% 降至 13.76–19.84%，同时保留非目标能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids costly retraining and parameter updates by intervening only during inference. However, existing activation-editing methods apply isolated pointwise corrections, overlooking how autoregressive generation continually reconstructs hidden states from the prompt, cache, and generated prefix. Consequently, later states may return to restricted knowledge regions after a locally successful correction, causing restricted knowledge re-entry. In this work, we propose Stateful Test-Time Unlearning via restricted knowledge boundary control (ST$^2$U), which formulates test-time unlearning as trajectory-wide boundary control. ST$^2$U first models restricted knowledge boundaries in low-dimensional invertible coordinates while leaving orthogonal non-target components unchanged. During inference, ST$^2$U monitors risk along the trajectory, applies minimal boundary corrections with contextual anchoring, and propagates historical correction states across tokens to mitigate knowledge re-entry. This trajectory-wide control enables more persistent forgetting while preserving non-target capabilities and limiting inference overhead. Across three benchmarks and three model families, ST$^2$U delivers the strongest overall balance, combining best or second-best retention with competitive forgetting and substantially less restricted-knowledge re-entry than test-time baselines (13.76%-19.84% versus 46.50%-59.10%).

</details>

### 31. Forget by Uncertainty: Orthogonal Entropy Unlearning for Quantized Neural Networks

📄 [arXiv](https://arxiv.org/abs/2602.00567) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65088)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`uncertainty calibration`、`deletion guarantee`、`deletion verification`

👤 **作者**：Tian Zhang、Yujia Tong、Junhao Dong、Ke Xu、Yuze Wang、Jingling Yuan

- 🎯 **研究动机**：量化网络遗忘方法靠记忆错误标签（把遗忘混同误记），且标量梯度加权无法解决方向冲突
- 🔬 **研究方法**：OEU：熵引导遗忘最大化预测不确定度给出无偏遗忘方向；梯度正交投影把遗忘梯度投到保留梯度正交补，一阶近似下效用保持有理论保证
- 📌 **结论**：遗忘效果与保留精度均超现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The deployment of quantized neural networks on edge devices, combined with privacy regulations like GDPR, creates an urgent need for machine unlearning in quantized models. However, existing methods face critical challenges: they induce forgetting by training models to memorize incorrect labels, conflating forgetting with misremembering, and employ scalar gradient reweighting that cannot resolve directional conflicts between gradients. We propose $\textbf{OEU}$, a novel Orthogonal Entropy Unlearning framework with two key innovations: 1) Entropy-guided unlearning provides an unbiased forgetting direction by maximizing prediction uncertainty on forgotten data, avoiding confident misprediction toward any specific class, and 2) Gradient orthogonal projection eliminates interference by projecting forgetting gradients onto the orthogonal complement of retain gradients, providing theoretical guarantees for utility preservation under first-order approximation. Extensive experiments demonstrate that OEU outperforms existing methods in both forgetting effectiveness and retain accuracy.

</details>

### 32. Divergence Decoding: Inference-Time Unlearning via Auxiliary Models

📄 [arXiv](https://arxiv.org/abs/2605.31293) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64823)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`mechanistic analysis`、`deletion verification`

👤 **作者**：Humzah Merchant、Bradford Levy

- 🎯 **研究动机**：现有遗忘方法导致灾难性效用损失或对复杂查询无效
- 🔬 **研究方法**：Divergence Decoding 用小型辅助模型在推理时把 LLM 的 logits 推离特定数据，辅助模型用标准流程训练，引导后分布可平凡蒸馏回基座
- 📌 **结论**：跨模型与数据规模的遗忘基准上决定性超越 SOTA 基线，方法通用并泛化到图像域

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) frequently memorize sensitive training data thereby creating significant privacy and copyright risks. Addressing these risks, i.e., removing such knowledge from an existing model checkpoint, has proven challenging as many unlearning methods lead to catastrophic utility loss or are ineffective for complex queries. We introduce Divergence Decoding (DD), a mechanism that uses small auxiliary models to steer the logits of the LLM away from specific data during inference. Training these models is straight forward, i.e., we use standard pre-training and fine-tuning setups. We find the method decisively outperforms state-of-the-art (SOTA) baselines on unlearning benchmarks across a variety of model and training dataset scales consistent with DD being an effective and inexpensive solution to unlearning. We then demonstrate that this steered distribution can be trivially distilled back into the base model. Since the method is generally applicable to any probabilistic model, we explore its efficacy outside of text generation and find evidence of generalization to the domain of images.

</details>

### 33. CAP: Controllable Alignment Prompting for Unlearning in LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1882/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`knowledge removal`

👤 **作者**：Zhaokun Wang、…、Wenhong Tian

- 🎯 **研究动机**：参数修改式遗忘成本高、边界不可控且依赖权重访问，闭源模型不可行；非侵入替代又欠系统化
- 🔬 **研究方法**：CAP 把遗忘解耦为经强化学习的可学习提示优化：提示生成器与 LLM 协作选择性抑制目标知识并保留通用能力，撤销提示即可恢复知识
- 📌 **结论**：不更新参数即实现精确可控遗忘，克服先前方法的迁移性限制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) trained on unfiltered corpora inherently risk retaining sensitive information, necessitating selective knowledge unlearning for regulatory compliance and ethical safety. However, existing parameter-modifying methods face fundamental limitations: high computational costs, uncontrollable forgetting boundaries, and strict dependency on model weight access. These constraints render them impractical for closed-source models, yet current non-invasive alternatives remain unsystematic and reliant on empirical experience. To address these challenges, we propose the Controllable Alignment Prompting for Unlearning (CAP) framework, an end-to-end prompt-driven unlearning paradigm. CAP decouples unlearning into a learnable prompt optimization process via reinforcement learning, where a prompt generator collaborates with the LLM to suppress target knowledge while preserving general capabilities selectively. This approach enables reversible knowledge restoration through prompt revocation. Extensive experiments demonstrate that CAP achieves precise, controllable unlearning without updating model parameters, establishing a dynamic alignment mechanism that overcomes the transferability limitations of prior methods.

</details>

### 34. CALIBURN: Self-Calibrated LLM Unlearning Alignment

📄 [arXiv](https://arxiv.org/abs/2602.02824)　📅 2026-09

**关键词**：`defense`、`machine unlearning`、`self-calibration`、`utility retention`

👤 **作者**：Zhengbang Yang、Yisheng Zhong、Junyuan Hong、Zhuangdi Zhu

- 🎯 **研究动机**：Gradient Ascent 式遗忘易灾难性遗忘，对齐式方法受参考模型质量限制，且都需大量 retain 数据
- 🔬 **研究方法**：CALIBURN 量化目标 LLM 对不良知识的置信度，用以更精细地校准遗忘梯度更新，实现细粒度遗忘控制
- 📌 **结论**：在 MUSE 与 WMDP 基准上实现有效遗忘并改善知识移除与效用保持的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM unlearning aims to remove the influence of undesirable knowledge from pretrained language models, which offers a practical mechanism for addressing safety and privacy concerns. Existing unlearning approaches, such as Gradient Ascent, are prone to catastrophic forgetting. Alignment-based approaches provide an alternative direction, yet their effectiveness is limited by the quality of the reference model. In realistic settings, both methods still require large retention datasets to preserve general knowledge. We propose a principled method that quantifies the target LLM's confidence in undesirable knowledge and uses it to calibrate the model's unlearning gradient updates more precisely. It enables fine-grained control over forgetting while better preserving model utility, thus reducing the dependence on retention data or prohibitive unlearning training data. Extensive evaluations on multiple benchmarks, including MUSE and WMDP, show that our method achieves effective unlearning and improves the trade-off between knowledge removal and utility preservation compared with state-of-the-art methods.

</details>

### 35. JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification

🎓 [Official](https://aclanthology.org/2026.acl-long.348/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`jailbreak`、`machine unlearning`、`deletion guarantee`、`LLM jailbreak`、`knowledge removal`

👤 **作者**：Xi Wang、…、Jie Yu

- 🎯 **研究动机**：机器遗忘防御仍被越狱绕过：越狱主要激活中间层未擦除参数并动态重组出违禁输出
- 🔬 **研究方法**：JPU 动态挖掘 on-policy 对抗样本暴露漏洞、识别动态越狱路径，并将其矫正到安全锚点
- 📌 **结论**：对动态攻击的抗性显著增强同时保持模型效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive safety alignment, Large Language Models (LLMs) often fail against jailbreak attacks. While machine unlearning has emerged as a promising defense by erasing specific harmful parameters, current methods remain vulnerable to diverse jailbreaks. We first conduct an empirical study and discover that this failure mechanism is caused by jailbreaks primarily activating non-erased parameters in the intermediate layers. Further, by probing the underlying mechanism through which these circumvented parameters reassemble into the prohibited output, we verify the persistent existence of dynamic jailbreak paths and show that the inability to rectify them constitutes the fundamental gap in existing unlearning defenses. To bridge this gap, we propose J ailbreak P ath U nlearning (JPU), which is the first to rectify dynamic jailbreak paths towards safety anchors by dynamically mining on-policy adversarial samples to expose vulnerabilities and identify jailbreak paths. Extensive experiments demonstrate that JPU significantly enhances jailbreak resistance against dynamic attacks while preserving the model’s utility.

</details>

### 36. From Narrow Unlearning to Emergent Misalignment in LLMs

🎓 [Official](https://aclanthology.org/2026.acl-short.32/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`narrow unlearning`、`retain data`、`cross-domain misalignment`、`machine unlearning`、`knowledge removal`

👤 **作者**：Erum Mushtaq、…、Rahul Gupta

- 🎯 **研究动机**：不安全代码微调可触发涌现失准（EMA），窄域遗忘等其他干预是否也会致 EMA 未知
- 🔬 **研究方法**：对 Cybersecurity 与 Safety 概念做拒绝遗忘并监控七个 RAI 域的拒绝分数，用概念向量分析表征层概念纠缠
- 📌 **结论**：窄域遗忘可把 EMA 传播到无关域（Safety 概念影响更大），Mistral 与 Qwen 两个家族一致；少量受影响域 retain 数据加交叉熵可大幅恢复对齐；早期层表征相似的概念更易受 EMA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has shown that fine-tuning on insecure code data can trigger an emergent misalignment (EMA) phenomenon, where models generate malicious responses even to prompts unrelated to the original insecure code-writing task. Such cross-domain generalization of harmful behavior underscores the need for a deeper understanding of the algorithms, tasks, and datasets that induce emergent misalignment. In this work, we extend this study by demonstrating that emergent misalignment can also arise from narrow refusal unlearning in specific domains. We perform refusal unlearning on Cybersecurity and Safety concept, and evaluate EMA by monitoring refusal scores across seven responsible AI (RAI) domains, Cybersecurity, Safety, Toxicity, Bias, Sensitive Content, Medical/Legal, and Privacy. Our work shows that narrow domain unlearning can yield compliance responses for the targeted concept, however, it may also propagate EMA to unrelated domains. Among the two intervened concepts, Cybersecurity and Safety, we find that the safety concept can have larger EMA impact, i.e, causing lower refusal scores, across other unrelated domains such as bias. We observe this effect consistently across two model families, Mistral-7b-0.3v, and Qwen-7b-2.5. Further, we show that refusal unlearning augmented with cross-entropy loss function on a small set of retain data from the affected domains can largely, if not fully, restore alignment across the impacted domains while having lower refusal rate on the concept we perform unlearning on. To investigate the underlying causes of EMA, we analyze concept entanglements at the representation level via concept vectors. Our analysis reveals that concepts with higher representation similarity in earlier layers are more susceptible to EMA after intervention when the refusal stream is altered through targeted refusal unlearning.

</details>

### 37. CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization

🎓 [Official](https://aclanthology.org/2026.acl-long.143/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`machine unlearning`、`deletion guarantee`、`knowledge removal`

👤 **作者**：Junyi Li、Yongqiang Chen、Ningning Ding

- 🎯 **研究动机**：大型推理模型的遗忘两难：现有方法要么难以从 CoT 痕迹彻底清除知识，要么干扰推理过程损害性能
- 🔬 **研究方法**：CiPO 把遗忘重定义为对 CoT 推理的定向干预：让 LRM 对遗忘目标答案生成逻辑有效的反事实推理轨迹做偏好调优，并迭代更新偏好数据扩大与原模型的差距
- 📌 **结论**：完全移除中间 CoT 步骤与最终答案中的知识，同时保留 LRM 推理能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning has gained increasing attention in recent years, as a promising technique to selectively remove unwanted privacy or copyrighted information from Large Language Models that are trained on a massive scale of human data. However, the emergence of Large Reasoning Models (LRMs), which emphasize long chain-of-thought (CoT) reasoning to address complex questions, presents a dilemma to unlearning: existing methods either struggle to completely eliminate undesired knowledge from the CoT traces or degrade the reasoning performances due to the interference with the reasoning process. To this end, we introduce Counterfactual Unlearning through iterative Preference Optimization (CiPO), a novel framework that redefines unlearning as the targeted intervention of the CoT reasoning in LRMs. More specifically, given a desired unlearning target answer, CiPO instructs LRMs to generate a logically valid counterfactual reasoning trace for preference tuning. As the LRM adjusts to the counterfactual trace, CiPO iteratively updates the preference learning data to increase the discrepancy from the original model. This iterative loop ensures both desirable unlearning and smooth optimization, effectively mitigating the dilemma. Experiments on challenging benchmarks demonstrate that CiPO excels at unlearning, completely removing knowledge from both the intermediate CoT steps and the final answer, while preserving the reasoning abilities of LRMs.

</details>

### 38. GRACE: Gradient-guided Coreset Selection for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.28361)　📅 2026-08

**关键词**：`defense`、`forget-retain coreset`、`gradient selection`、`utility preservation`

👤 **作者**：Praveen Bushipaka、Andrea D'Angelo、Lucia Passaro、Tommaso Cucinotta

- 🎯 **研究动机**：LLM unlearning 通常假定已有预定义 forget/retain 集，现实删除请求往往只给少量不良行为示例，需从异构语料推断两个集合
- 🔬 **研究方法**：提出 GRACE：从种子示例计算 forget 方向，用非负正交匹配追踪选取梯度逼近该方向的紧凑 forget coreset；再投影掉 forget 方向并在剩余梯度空间做聚类正交匹配追踪选 retain 集
- 📌 **结论**：跨两个目标域、两类模型、四种 unlearning 算法，在保持相当遗忘质量的同时提升模型效用，对先前梯度选择方法增益最稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine Unlearning methods for Large Language Models typically assume pre-specified forget and retain sets. In realistic settings, however, requests may provide only a few examples of undesired behavior, requiring forget and retain sets to be inferred from heterogeneous corpora. We study this data-selection problem and propose GRACE , a gradient-guided coreset selection method that constructs both forget and retain sets for LLM unlearning. GRACE first computes a forget direction from seed examples that elicit the undesired behavior, then selects a compact forget coreset whose gradients approximate this direction using non-negative orthogonal matching pursuit. To preserve model utility, it selects retain examples after projecting out the forget direction and applying clustered orthogonal matching pursuit in the remaining gradient space. Across two target domains, two model families, and four unlearning algorithms, GRACE improves model utility while maintaining comparable forget quality, with particularly consistent gains over prior gradient-based selection methods.

</details>

### 39. What to Forget in Unlearning? Forget Set Curation for Language Models

📄 [arXiv](https://arxiv.org/abs/2608.14855) · 📝 [OpenReview](https://openreview.net/forum?id=Zf9b9ESaZ7)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Animesh Jha、Arpandeep Khatua、Youssef Allouah、Sanmi Koyejo

- 🎯 **研究动机**：unlearning 评测假设待忘样本已知，现实中请求者不知万亿 token 语料中哪些片段支撑该行为
- 🔬 **研究方法**：提出遗忘集策展问题；CleanSlate 基准含歌曲书籍逐字输出抑制、模型特定抽取画像与能力保留评测，比较自然词法、精确子串与评测感知三类策展器
- 📌 **结论**：自然策展遗忘效果弱；评测感知策展几乎完全抑制请求续写却造成非请求内容附带回归与模型相关能力损失——遗忘集选择决定能忘什么与伤什么

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove targeted data or behaviors from a trained model without retraining from scratch. Yet most evaluations assume that the examples to forget are already known. In realistic language-model deployments, a requester may ask a model to stop reproducing a song or book without knowing which spans, documents, quotations, or near-duplicates in a trillion-token corpus support that behavior. We study this missing upstream problem, forget set curation: mapping a suppression request to the data passed to an unlearning algorithm. We introduce CleanSlate, a benchmark for verbatim output suppression over songs and books, with model-specific extraction profiles, content-grounded QA, and capability-retention evaluations. CleanSlate exposes two failure modes. Natural lexical and exact-substring curators often yield forget sets that lead to weak suppression. An evaluation-aware curator suppresses requested continuations almost completely, but causes collateral regression on non-requested content and model-dependent capability loss. These results show that practical unlearning is not only an optimization problem once a forget set is given: the data chosen for forgetting determines both what can be unlearnt and what else is damaged.

</details>

### 40. DA^2-Unlearn: Dual-Adaptive Forget-Repair-Based Recommendation Unlearning

🌐 [Project](https://doi.org/10.1145/3770855.3818203)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`recommendation unlearning`、`adaptive forgetting`、`utility repair`

- 🎯 **研究动机**：推荐系统遗忘需兼顾删除效果与效用修复
- 🔬 **研究方法**：DA^2-Unlearn以双自适应机制分别控制遗忘与修复过程
- 📌 **结论**：遗忘目标数据同时有效恢复推荐效用

### 41. Variance-Reduced $(\varepsilon, \delta)-$Unlearning using Forget Set Gradients

🎓 [Official](https://icml.cc/virtual/2026/poster/66141)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Martin Van Waerebeke、Giovanni Neglia、Kevin Scaman、Marco Lorenzi、El-Mahdi El-Mhamdi

- 🎯 **研究动机**：强凸目标的一阶 (eps,delta) 遗忘方法只用遗忘集校准噪声、不作优化信号；利用遗忘样本的经验启发式又无形式保证
- 🔬 **研究方法**：提出 VRU：把遗忘集梯度直接纳入更新规则并证明仍满足 (eps,delta) 遗忘，建立收敛性并给出更优的误差依赖率
- 📌 **结论**：低误差区间渐近优于任何忽略遗忘集的一阶方法；实验上一致超越认证遗忘与经验基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In machine unlearning, $(\varepsilon,\delta)-$unlearning is a popular framework that provides formal guarantees on the effectiveness of the removal of a subset of training data, the \emph{forget set}, from a trained model. For strongly convex objectives, existing first-order methods achieve $(\varepsilon,\delta)-$unlearning, but they only use the forget set to calibrate injected noise, never as a direct optimization signal. In contrast, efficient empirical heuristics often exploit the forget samples (e.g., via gradient ascent) but come with no formal unlearning guarantees. We bridge this gap by presenting the Variance-Reduced Unlearning (*VRU*) algorithm. To the best of our knowledge, *VRU* is the first first-order algorithm that directly includes forget set gradients in its update rule, while provably satisfying $(\varepsilon,\delta)-$unlearning. We establish the convergence of *VRU* and show that incorporating the forget set yields strictly improved rates, *i.e.*, a better dependence on the achieved error compared to existing first-order $(\varepsilon,\delta)-$unlearning methods. Moreover, we prove that, in a low-error regime *VRU* asymptotically outperforms any first-order methods that ignores the forget set. Experiments corroborate our theory, showing consistent gains over both state-of-the-art certified unlearning methods and over empirical baselines that explicitly leverage the forget set.

</details>

### 42. Unlearning with Asymmetric Sources: Improved Unlearning-Utility Trade-off with Public Data

📄 [arXiv](https://arxiv.org/abs/2605.11170) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66791)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`certified robustness`、`deletion verification`

👤 **作者**：Ahmed Mehdi Inane、Vincent Quirion、Gintare Karolina Dziugaite、Ioannis Mitliagkas

- 🎯 **研究动机**：噪声认证遗忘面临噪声量破坏效用的硬天花板，公开数据在遗忘中的作用未被探索
- 🔬 **研究方法**：提出 ALU：以公开数据降低隐私代价，证明公开数据注入可按 O(1/n_pub^2) 因子抑制遗忘成本，并显式刻画公开/私有分布失配的影响
- 📌 **结论**：支持常数比例数据的批量遗忘这一对称方法不可行的场景；变分 Renyi 散度与 MIA 验证其抵御隐私攻击且保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Noise-based certified machine unlearning currently faces a hard ceiling: the noise magnitude required to certify unlearning typically destroys model utility, particularly for large-scale deletion requests. While leveraging public data is a standard technique in differential privacy to relax this tension, its role in unlearning remains unexplored. We address this gap by introducing **Asymmetric Langevin Unlearning (ALU)**, a framework that uses public data to mitigate privacy costs. We prove that public data injection suppresses the unlearning cost by a factor of $O(1/n_{\mathrm{pub}}^2)$, guaranteeing a strict computational advantage over retraining. This establishes a new control mechanism: practitioners can mitigate the need for high noise—and the associated utility loss—by increasing the volume of public data. Crucially, we analyze the realistic setting of **distribution mismatch**, explicitly characterizing how shifts between public and private sources impact utility. We show that ALU enables "mass unlearning'' of constant dataset fractions -- a regime where standard symmetric methods become impractical -- while maintaining high utility. Empirical evaluations using variational Rényi divergence and membership inference attacks confirm that ALU effectively thwarts privacy attacks while preserving utility under reasonable distribution shifts.

</details>

### 43. Selective Span-Level Unlearning for Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-short.35/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`knowledge removal`

👤 **作者**：Chaewon Yoon、Dongjun Kim、Hyun-Je Song

- 🎯 **研究动机**：选择性 LLM 遗忘多依赖外部监督定位遗忘目标，可能与模型内部行为错位
- 🔬 **研究方法**：完全基于模型内在信息：对比遗忘与保留数据的梯度估计 token 重要性，再经自一致性生成过程把关键 token 锚定为连贯的 span 级遗忘目标
- 📌 **结论**：在两个 LLM 遗忘基准上遗忘效果相当，同时显著更好地保留知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) trained on massive text corpora may inadvertently memorize sensitive or copyrighted content, motivating the need for more targeted unlearning. Selective LLM unlearning focuses on identifying token-level or span-level unlearning targets within a text, rather than treating entire sequences as unlearning targets. However, many existing selective approaches depend on external supervision to identify unlearning targets, which may misalign unlearning objectives with the model’s internal behavior. In this paper, we propose a selective span-level unlearning method that is grounded entirely in model-intrinsic information. Our method first estimates token-level importance scores by contrasting gradient information induced by forget and retain datasets, identifying tokens that disproportionately contribute to information targeted for unlearning. These token-level importance scores are then used as anchors to identify coherent span-level unlearning targets via a self-consistency–based generation process, allowing the model to determine stable spans based on its own predictions. Experiments on two LLM unlearning benchmarks show that our approach achieves comparable unlearning performance while substantially better preserving retained knowledge.

</details>

### 44. Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens

🎓 [Official](https://aclanthology.org/2026.acl-long.1175/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`knowledge removal`

👤 **作者**：Seunghee Koh、Sunghyun Baek、Youngdong Kim、Junmo Kim

- 🎯 **研究动机**：遗忘损失均匀施加会不必要损害效用；已有 token 级正则依赖真实置信或外部语言解析器
- 🔬 **研究方法**：ETW 用预测分布熵做 token 信息量代理——信息性 token 熵高、结构 token 熵低，据此加权遗忘损失
- 📌 **结论**：比现有 token 级方法遗忘更有效且效用保持更好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning in large language models (LLMs) has emerged as a promising safeguard against adversarial behaviors. When the forgetting loss is applied uniformly without considering token-level semantic importance, model utility can be unnecessarily degraded. Recent studies have explored token-wise loss regularizers that prioritize informative tokens, but largely rely on ground-truth confidence or external linguistic parsers, which limits their ability to capture contextual information or the model’s overall predictive state. Intuitively, function words like “the” primarily serve syntactic roles and are highly predictable with little ambiguity, but informative words admit multiple plausible alternatives with greater uncertainty. Based on this intuition, we propose Entropy-guided Token Weighting (ETW), a token-level unlearning regularizer that uses entropy of the predictive distribution as a proxy for token informativeness. We demonstrate that informative tokens tend to have higher entropy, whereas structural tokens tend to have lower entropy. This behavior enables ETW to achieve more effective unlearning while better preserving model utility than existing token-level approaches.

</details>

### 45. Extracting Forgotten Prompts from Targeted Unlearned Models

📄 [arXiv](https://arxiv.org/abs/2609.03662)　📅 2026-09

**关键词**：`attack`、`targeted extraction`、`residual memorization`、`unlearning audit`、`unlearning leakage`、`relearning`

👤 **作者**：Au Ashley Hoi-Ting、Meghdad Kurmanji、William F. Shen、Nicholas D. Lane、Ligang He

- 🎯 **研究动机**：现有 unlearning 攻击假设攻击者已知 forgotten prompt 而只恢复答案，prompt 本身可被提取这一盲点未被注意
- 🔬 **研究方法**：提出 Targeted Active Search：用 retained data 构造典型模板与实体池，在有限查询预算下选信息量最大的模板-实体对定位遗忘实体，再用实体实例化模板重建 forgotten prompt
- 📌 **结论**：三种 unlearning 方法、三个数据集与三个 LLM 上实体恢复 100%、最多重建 95% 的 forgotten prompt，查询数比朴素探测省 99.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent unlearning methods (e.g. NPO, DPO, LUNAR) make use of refusal alignment to suppress forgotten data. However, it has been shown that refusal responses might leave traces of unlearning, and recent attacks have been able to successfully recover some of the unlearned knowledge. In this paper, we uncover a new vulnerability. Existing attacks typically assume that the forgotten prompts are already known to the adversary and focus on recovering their answers. However, we show that the forgotten prompts themselves can be extracted by using the retained data and black-box access to the model. Our attack, Targeted Active Search (TAS), first identifies the forgotten entities by constructing canonical templates and entity pool, and selectively querying the model using the most informative template-entity pair under a limited query budget. Once the entities are identified, TAS instantiates prompt templates with those entities to probe the unlearned model and reconstruct the forgotten prompts. Experiments across three unlearning methods with three datasets and three LLMs shows that TAS recovers the forgotten entity with $100\%$ accuracy and reconstructs up to $95\%$ of forgotten prompts, all while using up to $99.7\%$ fewer queries than naive probing.

</details>

### 46. Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness

📄 [arXiv](https://arxiv.org/abs/2608.25429)　📅 2026-08

**关键词**：`defense`、`analysis`、`capability removal`、`relearning resistance`、`weight selectivity`、`relearning robustness`

👤 **作者**：Yi Chen、…、Joo-Young Kim

- 🎯 **研究动机**：unlearned LLM 短暂微调即可复活已删知识，而全局权重距离在破坏性更新下会误导鲁棒性预测
- 🔬 **研究方法**：FRAG 免训练度量更新对 forget 与 retain 关键权重的对齐差以区分选择性与稠密更新，并据此提出 Forget-Retain Pruning
- 📌 **结论**：weight selectivity 比距离更能预测 relearning robustness，FRP 进一步增强抗复学能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to make a model forget specific data, yet unlearned LLMs often fail to stay unlearned: brief fine-tuning can revive removed knowledge. Existing robustness predictors rely on global weight-space displacement, but distance alone can be misleading when random or destructive updates collapse performance. We argue that relearning robustness depends on update structure: robust unlearning should affect forget-critical weights while sparing retain-critical ones. We introduce the Forget-Retain Alignment Gap (FRAG), a training-free predictor that scores an update's forget-retain alignment without running a relearning attack, and separates selective from dense updates more reliably than global distance. Building on the forget-critical, retain-sparing principle, Forget-Retain Pruning (FRP) improves relearning robustness. Our results suggest that weight selectivity better explains robustness than distance alone. Code is available at https://github.com/Yi1-Chen/FRAG.

</details>

### 47. Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21544)　📅 2026-08

**关键词**：`defense`、`tool-mediated recovery`、`target-seeking tool call`、`knowledge leakage`、`capability removal`、`external-tool recovery`

👤 **作者**：Baicheng Chen、…、Meng Jiang

- 🎯 **研究动机**：现有 unlearning 只抑制参数化直接回忆，工具增强 Agent 仍可经 web 搜索、检索或数据库查找恢复遗忘目标（tool-mediated recovery），评测存在错配
- 🔬 **研究方法**：ATU 两阶段框架：先做参数知识遗忘抑制直接回忆，再在模拟工具环境中做轨迹级 RL，惩罚 target-seeking 工具行为与最终答案泄漏
- 📌 **结论**：RWKU 与 MUSE 上跨不同 LLM 架构取得目标遗忘与保留效用间更好平衡，unlearning 在工具增强部署下更稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

</details>

### 48. Deletion Isn't Enough: Auditing RAG for Selective Forgetting

🌐 [Project](https://doi.org/10.1145/3805712.3808545)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`analysis`、`RAG disclosure`、`post-revocation leakage`、`selective-forgetting audit`、`audit`、`RAG revocation`

- 🎯 **研究动机**：RAG删除知识后是否真正被遗忘缺审计手段
- 🔬 **研究方法**：构造paired disclosure probe审计撤回后的残留泄漏
- 📌 **结论**：删除操作后的RAG仍可泄露应被遗忘的内容

### 49. TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.17828) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_TINA_Text-Free_Inversion_Attack_for_Unlearned_Text-to-Image_Diffusion_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`diffusion unlearning`、`text-free inversion`、`concept recovery`

👤 **作者**：Qianlong Xiang、Miao Zhang、Haoyu Zhang、Kun Wang、Junhui Hou、Liqiang Nie

- 🎯 **研究动机**：擦除防御与探测的共演化聚焦切断文本-图像映射，忽略概念相关的视觉知识仍存留于模型
- 🔬 **研究方法**：TINA 在 null-text 条件下做无文本 DDIM 反演探测被擦概念的视觉生成路径，并以优化过程克服无文本引导的累积误差
- 📌 **结论**：从 SOTA unlearning 处理后的模型再生被擦除概念，证明现有方法只是遮蔽概念而非删除视觉知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although text-to-image diffusion models exhibit remarkable generative power, concept erasure techniques are essential for their safe deployment to prevent the creation of harmful content. This has fostered a dynamic interplay between the development of erasure defenses and the adversarial probes designed to bypass them, and this co-evolution has progressively enhanced the efficacy of erasure methods. However, this adversarial co-evolution has converged on a narrow, text-centric paradigm that equates erasure with severing the text-to-image mapping, ignoring that the underlying visual knowledge related to undesired concepts still persist. To substantiate this claim, we investigate from a visual perspective, leveraging DDIM inversion to probe whether a generative pathway for the erased concept can still be found. However, identifying such a visual generative pathway is challenging because standard text-guided DDIM inversion is actively resisted by text-centric defenses within the erased model. To address this, we introduce TINA, a novel Text-free INversion Attack, which enforces this visual-only probe by operating under a null-text condition, thereby avoiding existing text-centric defenses. Moreover, TINA integrates an optimization procedure to overcome the accumulating approximation errors that arise when standard inversion operates without its usual textual guidance. Our experiments demonstrate that TINA regenerates erased concepts from models treated with state-of-the-art unlearning. The success of TINA proves that current methods merely obscure concepts, highlighting an urgent need for paradigms that operate directly on internal visual knowledge.

</details>

### 50. Unlearning’s Blind Spots: Over‑Unlearning and Prototypical Relearning Attack

📄 [arXiv](https://arxiv.org/abs/2506.01318) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63385)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`attack`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`

👤 **作者**：SeungBum Ha、Saerom Park、Sung Whan Yoon

- 🎯 **研究动机**：机器遗忘忽视两个盲点：遗忘集邻近保留数据的过度遗忘，以及事后复活已遗忘知识的重学习攻击
- 🔬 **研究方法**：定义 OU@epsilon 度量邻近区附带损伤；提出利用遗忘类原型的 Prototypical Relearning Attack，少量样本即可恢复遗忘前性能；Spotter 以掩码知识蒸馏与类内散布损失同时应对两者
- 📌 **结论**：在 CIFAR、TinyImageNet 与 CASIA-WebFace 上达到 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) aims to expunge a designated forget set from a trained model without costly retraining, yet the existing techniques overlook two critical blind spots: "over‑unlearning" that deteriorates retained data near the forget set, and post‑hoc "relearning" attacks that aim to resurrect the forgotten knowledge. Focusing on class-level unlearning, we first derive an over-unlearning metric, $\operatorname{OU}@\varepsilon$, which quantifies collateral damage in regions proximal to the forget set, where over-unlearning mainly occurs. Next, we expose an unforeseen relearning threat on MU, i.e., the Prototypical Relearning Attack, which exploits the per-class prototype of the forget class with just a few samples, and easily restores the pre-unlearning performance. To counter both blind spots in class-level unlearning, we introduce $\texttt{Spotter}$, a plug‑and‑play objective that combines (i) a masked knowledge‑distillation penalty on the nearby region of forget classes to suppress $\operatorname{OU}@\varepsilon$, and (ii) an intra‑class dispersion loss that scatters forget-class embeddings, neutralizing Prototypical Relearning Attacks. $\texttt{Spotter}$ achieves state-of-the-art results across CIFAR, TinyImageNet, and CASIA-WebFace datasets, offering a practical remedy to unlearning’s blind spots.

</details>

### 51. Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs

📄 [arXiv](https://arxiv.org/abs/2505.16831) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65395)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Xiaoyu Xu、…、Haibo Hu

- 🎯 **研究动机**：LLM 遗忘效果通常用准确率与困惑度等任务级指标评估，但模型看似遗忘后经少量微调即可恢复原行为，信息只是被抑制
- 🔬 **研究方法**：提出表示级分析框架：以 PCA 相似度/偏移、CKA 与 Fisher 信息及 mean PCA distance 度量表示漂移，按可逆性与灾难性划分四种遗忘机制并比较恢复策略
- 📌 **结论**：不可逆且非灾难性的遗忘极难达成；识别出看似不可逆的定向遗忘案例，为鲁棒擦除算法奠基

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning in large language models (LLMs) aims to remove specified data, but its efficacy is typically assessed with task-level metrics like accuracy and perplexity. We show that these metrics can be misleading, as models can appear to forget while their original behavior is easily restored through minimal fine-tuning. This \emph{reversibility} suggests that information is merely suppressed, not genuinely erased. To address this critical evaluation gap, we introduce a \emph{representation-level analysis framework}. Our toolkit comprises PCA similarity and shift, centered kernel alignment (CKA), and Fisher information, complemented by a summary metric, the mean PCA distance, to measure representational drift. Applying this framework across multiple unlearning methods, data domains, and LLMs, we identify four distinct forgetting regimes based on their \emph{reversibility} and \emph{catastrophicity}. We compare recovery strategies and show that relearning efficiency relies on the data source. We also find that irreversible, non-catastrophic forgetting is exceptionally challenging. By probing unlearning limits, we identify a case of seemingly irreversible, targeted forgetting, offering insights for more robust erasure algorithms. Overall, our findings expose a gap in current evaluation and establish a representation-level foundation for trustworthy unlearning.

</details>

### 52. Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility

📄 [arXiv](https://arxiv.org/abs/2606.03291) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64258)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Chaoyi Xiang、Olga Ohrimenko、Benjamin I. P. Rubinstein、Lea Frermann

- 🎯 **研究动机**：遗忘研究严重英语中心，跨语言遗忘迁移与可逆性未知
- 🔬 **研究方法**：把 TOFU 扩展到五种语言，以不同语言排列微调、遗忘与查询，并做逐层分析
- 📌 **结论**：迁移高度可变（共享文字与语系最强）；遗忘主要作用于后段解码层而早期跨语言潜空间完好，属表层抑制——单个推理时转向方向即可跨语言恢复 50%（Qwen）与 90%（Gemma）被遗忘知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) can memorize sensitive facts, motivating unlearning methods that remove targeted knowledge without costly retraining. However, unlearning research remains heavily English-centric. We study multilingual unlearning by extending the TOFU benchmark to five languages, and fine-tune, unlearn and query our models with different permutations of languages. We find that unlearning transfer -- the ability of an unlearned model to "forget" facts in languages other than the unlearning language -- is highly variable: e.g., it is strongest between languages sharing scripts and families, and we show that the unlearning language predicts which query languages are most likely to yield the strongest transfer. Layer-wise analysis reveals that unlearning leaves the shared cross-lingual latent space largely intact in early layers, instead operating primarily in later decoding layers. This suggests that unlearning does not truly erase knowledge, but rather induces superficial suppression. Exploiting this structure, a single inference-time steering direction reverses much of this suppression across languages, recovering 50% (Qwen) and 90% (Gemma) of the unlearned knowledge.

</details>

### 53. Maximizing Local Entropy Where It Matters: Prefix-Aware Localized LLM Unlearning

🎓 [Official](https://aclanthology.org/2026.acl-long.893/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`knowledge removal`

👤 **作者**：Naixin Zhai、…、Xun Yang

- 🎯 **研究动机**：现有遗忘对响应所有 token 一视同仁并在全词表强制不确定性，造成不必要效用损失
- 🔬 **研究方法**：PALU 时序与词表双维局部熵最大化：抑制敏感前缀即可切断因果生成链，只平坦化 top-K logits 即可最大化关键子空间不确定性
- 📌 **结论**：遗忘效果与效用保留均优于 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to forget sensitive knowledge from Large Language Models (LLMs) while maintaining general utility. However, existing approaches typically treat all tokens in a response indiscriminately and enforce uncertainty over the entire vocabulary. This global treatment results in unnecessary utility degradation and extends optimization to content-agnostic regions. To address these limitations, we propose PALU (Prefix-Aware Localized Unlearning), a framework driven by a local entropy maximization objective across both temporal and vocabulary dimensions. PALU reveals that (i) suppressing the sensitive prefix alone is sufficient to sever the causal generation link, and (ii) flattening only the top-K logits is adequate to maximize uncertainty in the critical subspace. These findings allow PALU to alleviate redundant optimization across the full vocabulary and parameter space while minimizing collateral damage to general model performance. Comprehensive evaluations validate that PALU achieves superior forgetting efficacy and utility preservation compared to state-of-the-art baselines. Our code is available at https://github.com/nxZhai/PALU.

</details>

### 54. Leak@$k$: Unlearning Does Not Make LLMs Forget Under Probabilistic Decoding

📄 [arXiv](https://arxiv.org/abs/2511.04934) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61231)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Hadi Reisizadeh、Jiajun Ruan、Yiwei Chen、Soumyadeep Pal、Sijia Liu、Mingyi Hong

- 🎯 **研究动机**：贪心解码评测显示遗忘成功，但概率解码下敏感信息可靠复现——几乎所有遗忘方法未实现真遗忘
- 🔬 **研究方法**：提出 leak@k 元评测指标量化 k 个采样下遗忘知识重现概率，在 TOFU/MUSE/WMDP 首次大规模系统研究，并提出 RULE 算法
- 📌 **结论**：知识泄漏跨方法与任务持续存在；RULE 在 TOFU 上大量采样零泄漏，MUSE 上多数采样预算优于 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning in large language models (LLMs) is critical for regulatory compliance and for building ethical generative AI systems that avoid producing private, toxic, illegal, or copyrighted content. Despite rapid progress, in this work, we show that \textit{almost all} existing unlearning methods fail to achieve true forgetting in practice. Specifically, while evaluations of these `unlearned' models under deterministic (greedy) decoding often suggest successful knowledge removal using standard benchmarks, we show that sensitive information reliably resurfaces when models are sampled with standard probabilistic decoding. To rigorously capture this vulnerability, we introduce \texttt{leak@$k$}, a new meta-evaluation metric that quantifies the likelihood of forgotten knowledge reappearing when generating $k$ samples from the model under realistic decoding strategies. Using three widely adopted benchmarks, TOFU, MUSE, and WMDP, we conduct the first large-scale, systematic study of unlearning reliability using \texttt{leak@$k$} metric. Our findings demonstrate that knowledge leakage persists across methods and tasks, underscoring that current state-of-the-art (SOTA) unlearning techniques provide only limited forgetting. We propose an algorithm, termed Robust Unlearning under LEak@$k$ metric (\texttt{RULE}) to address this concern. We demonstrate that \texttt{RULE} provides an unlearned model for TOFU benchmark with no information leakage for a large number of generation samples. On the MUSE benchmark, \texttt{RULE} outperforms SOTA unlearning methods under the \texttt{leak@$k$} metric across most sampling budgets $k$. Codes are available at \url{https://github.com/OptimAI-Lab/Leak-k}.

</details>

### 55. De-attribute to Forget for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2605.30919) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66664)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`

👤 **作者**：Xinyang Lu、Jiabao Pan、Rachael Hwee Ling Sim、See-Kiong Ng、Anthony Kum Hoe Tung、Bryan Kian Hsiang Low

- 🎯 **研究动机**：基于预测损失（最大化 forget 集损失）的遗忘方法常过度遗忘、效用差
- 🔬 **研究方法**：DareU 把优化目标转为降低数据归因：用强化学习更新 LLM，降低生成回复对遗忘数据所有者的归因分数，以 LLM 分类器高效近似归因
- 📌 **结论**：超越现有基线，在遗忘质量与模型效用间取得平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid development of large language models (LLMs) has raised concerns regarding the inclusion of private or inappropriate data during training, which has led to growing interest in LLM unlearning. Many existing LLM unlearning approaches rely on prediction loss-based optimizations, such as maximizing the loss on the forget set. However, these methods often face issues such as over-forgetting and poor model utility. In this work, we address these issues by introducing a novel perspective that shifts the unlearning optimization target to reducing data attribution instead. We propose the first LLM unlearning framework based on data attribution rewards called DareU that employs reinforcement learning to update the LLM and reduce the attribution score of generated responses (i.e., de-attribute) to the forget data owners. Experimental results using an LLM classifier as an efficient approximation of attribution demonstrate that DareU outperforms existing baseline approaches, achieving effective unlearning while balancing forget quality and model utility.

</details>

### 56. Adversarial Attack Framework Against Vision-Language Model Unlearning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7256.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`analysis`、`unlearning recovery`、`visual sink token`、`surrogate-only transfer`、`VLM unlearning`

- 🎯 **研究动机**：对抗输入可操纵已 unlearn 的 VLM 复现被遗忘内容，但多数攻击需要受害者架构、参数或输出 logits 访问
- 🔬 **研究方法**：提出 SISA：只需一个代理预训练 VLM；利用 unlearning 后 visual sink token 的持续性作为稳定结构锚，诱导 sink 建立结构锚再经 sink 条件化注意力做语义对齐，生成可迁移对抗输入
- 📌 **结论**：在多样 unlearned VLM 设定下有效，输出与遗忘目标的语义一致性相比干净输入最多提升 6.9 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision–Language Models (VLMs) unlearning tends to eliminate the influence of “to-beforgotten” content in the training corpora, algorithmically by suppressing the likelihood of faithfully generating responses on forget-target inputs. The injection of adversarial inputs can manipulate the unlearned VLM’s generation towards the attacker’s will, forcing the reproduction of the supposedly forgotten content and undermining the reliability of expected forgetting behavior. However, most attacks assume access to the unlearned VLM’s architecture or parameters, or to output logits via queries. In this paper, we propose SISA, a novel attack framework for crafting adversarial inputs to manipulate generation towards the forgotten target, which only requires access to a surrogate, pretrained VLM. SISA advances prior attacks by exploiting the persistence of visual sink tokens after unlearning as a stable structural anchor for semantic alignment. SISA induces a sink regime on a candidate visual token to build the structural anchor that influences generation, and then semantically aligns model output to the target while conditioning on attention through the induced sink token, reinforcing the anchor for desired elicitation. With sink persistence and sink-conditioned semantic anchoring, SISA crafts transferable adversarial inputs. Evaluation on diverse unlearned VLM settings confirms the effectiveness of SISA, increasing the outputs’ semantic agreement with forgotten targets by up to 6.9× relative to clean inputs.

</details>

### 57. BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.22557)　📅 2026-08

**关键词**：`defense`、`capability erasure`、`sequential removal`、`utility retention`、`bilevel LoRA`、`clamped entropy`

👤 **作者**：Md Toufikuzzaman、Ahmad Mousavi、Dongwon Lee

- 🎯 **研究动机**：现有 LLM unlearning 鲁棒性不足：无界 forget loss 破坏连贯性、固定权重平衡无法适应 retain 难度漂移、单 benchmark 有效的方法在规模化或重复应用时失效
- 🔬 **研究方法**：BLADE 约束双层框架：clamped-entropy forget loss 使 token 达到足够不确定性后梯度恰为零，非对称增广 Lagrangian 违规后永久棘轮式收紧 retain 保护，双层结构限定在 LoRA adapter 内逐步先修复 retain 损伤再遗忘
- 📌 **结论**：TOFU、MUSE Books、KnowUndo 平均综合分超最强基线 6%、9%、7%，在 4 倍规模与 MUSE News 连续 4 步遗忘下保持稳定而最佳竞品完全崩溃

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing LLM unlearning methods struggle with robustness: unbounded forget losses degrade model coherence, fixed-weight balancing cannot adapt as retain difficulty shifts mid-training, and methods that work on one benchmark falter under scaling or repeated application. We propose BLADE, a constrained bilevel framework whose three mechanisms give smooth, predictable control over the optimization landscape: a clamped-entropy forget loss whose gradient is exactly zero once a token reaches sufficient uncertainty; an asymmetric augmented Lagrangian that permanently ratchets retain protection after any violation; and a bilevel structure confined to LoRA adapters that repairs retain damage before each forgetting step. BLADE dominates across three benchmark families, improving average composite scores over the strongest baselines by $6$% on TOFU, $9$% on MUSE Books, and $7$% on KnowUndo, and it remains stable under $4\times$ scaling and $4$ sequential unlearning steps on MUSE News where the best competing method collapses entirely.

</details>

### 58. Cross-Domain Generalization in Machine Unlearning via Label-Conditioned Energy Magnitude Regularization

📄 [arXiv](https://arxiv.org/abs/2608.17942)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Syed Ali Ahmed、Syed Bilal Ahsan、Muhammad Zaigham Zaheer

- 🎯 **研究动机**：unlearning 多把遗忘概念当孤立对象，遗忘一个类对模型其余部分的影响未被直接观察
- 🔬 **研究方法**：标签条件能量模型分配逐类能量：遗忘项加预训练锚加全局边界加能量正则，传播项按 DINOv2 相似度把遗忘信号加权传给相似 retain 样本
- 📌 **结论**：DomainNet 草图域遗忘 lion/scissors 以 98-99% 遗忘误差传播到真实、剪贴与油画域；CIFAR-10 关闭传播后十类各自 100% 遗忘、其余九类平均保留 98.5% 精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning removes the influence of specific data from a trained model. However, most methods treat the forgotten concept as isolated. In this paper, we study what happens to the rest of the model when a class is forgotten, using a label-conditioned energy-based model (EBM) that assigns per-class energies, making the effect directly observable. We forget a class by raising the energy of its image-label pairs, training with a forget term, a retain anchor to the pretrained model, a global margin, and an energy regularizer that stops the energy magnitudes from growing without limit. A propagation term applies the same forget signal to retain samples, weighted by each sample's DINOv2 similarity to the forget class, so forgetting reaches images that resemble it and leaves the rest untouched. We evaluate on two benchmark datasets: 1) On a subset of DomainNet across four visual domains, we forget tiger, lion, and scissors one at a time. Forgetting a class in the sketch domain also erases it from real, clipart, and painting, with forgetting error reaching 98% and 99% for lion and scissors, and the effect carrying over to the most similar class. 2) On CIFAR-10, we turn off the propagation term and forget each of the ten classes on its own. Forgetting is complete (100%), while the other nine classes retain 98.5% of their pre-unlearning accuracy on average.

</details>

### 59. Learning to Unlearn: Machine Unlearning via Learning the Unlearning Behaviors

📄 [arXiv](https://arxiv.org/abs/2608.16700)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Hang Zhang、Kaifeng Zhang、Yixiao Ma、Weijie Xu、Ye Zhu、Kai Ming Ting

- 🎯 **研究动机**：现有 unlearning 精心设计遗忘函数 U，海量训练数据下复杂结构成为瓶颈
- 🔬 **研究方法**：Learning-to-UnLearn 从分布视角学习遗忘行为，获得简单高效且模型无关的 U，受 Learning-to-Optimize 启发
- 📌 **结论**：精度接近重训练且数据密集场景效率突出，在更大规模 ResNet 上验证可扩展性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Various machine unlearning techniques have been developed in response to privacy legislation requirements, enabling individuals to exercise their legal right to have their data $D_f$ removed from a machine learning model. This process is typically accomplished via the use of an unlearning function denoted as $U$. Existing methods focus on designing an intricate $U$ to unlearn $D_f \subset D$ from a previous model $A(D)$, so that the unlearned model performs as closely as possible to the retrained model $A(D \setminus D_f)$. However, these methods often suffer from high computational costs when dealing with massive training data, as the complex structures of $U$ become a bottleneck even for models with fewer parameters. Inspired by Learning to Optimize, we introduce the first learning-based model-agnostic approach, Learning-to-UnLearn (L2UL). Our core insight is to shift from manually designing $U$ to learning the unlearning behaviors from a distribution perspective, thereby acquiring a simple and efficient $U$ via learning. Our experimental results demonstrate that the accuracy achieved by L2UL is comparable to that of retraining while exhibiting impressive efficiency, particularly in data-intensive scenarios. Furthermore, we validate the performance and scalability of our method on larger models ResNet.

</details>

### 60. The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.14229)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Anna Borisiuk、Andrey Savchenko、Alexander Panchenko、Elena Tutubalina

- 🎯 **研究动机**：流行事实在预训练中记忆更深、更难移除，现有 unlearning 对所有事实施加均匀梯度压
- 🔬 **研究方法**：AdaPop 结合局部 token 置信度与外部代理（Wikidata sitelinks、LLM-as-Judge）导出的按事实流行度指数，双上升控制器逐 epoch 调节 retain 惩罚
- 📌 **结论**：三模型家族两基准上，改写查询下遗忘内容泄漏约少 5 倍、对抗重构下少 1.6 倍，遗忘集隐状态更远离原模型而保留集表征保持接近

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts the retain penalty each epoch. Across three model families and two benchmarks, AdaPop leaks ~5x less forgotten content than competing methods under paraphrased queries and ~1.6x less under adversarial reformulations. We support our analysis with internal metrics: under our method, forget-set hidden states move further from the pre-unlearning model's states than under other methods, while retain-set representations remain close.

</details>

### 61. How Hard Can It Be? Hardness-Aware Multi-Objective Unlearning

📄 [arXiv](https://arxiv.org/abs/2606.02119) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62521)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`

👤 **作者**：Jiangwei Chen、Xinyuan Niu、Rachael Hwee Ling Sim、Zhengyuan Liu、Nancy F. Chen、Bryan Kian Hsiang Low

- 🎯 **研究动机**：现有遗忘算法不保证遗忘质量与保留效用能同时按指定幅度改进
- 🔬 **研究方法**：以遗忘集与保留集的相似度量化两目标调和难度，HAMU 在保证指定遗忘质量提升下最小化保留效用损失，并在两目标不可兼得时提示停止
- 📌 **结论**：图像与文本大模型上优于基线，适用于非凸模型且易并行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of specific forget training data due to privacy, copyright or bias concerns while maintaining the model performance on the remaining retain data. Existing unlearning algorithms, such as optimizing a weighted combination of losses, have tried to achieve these objectives of improving forget quality and maintaining retain utility. However, they do not guarantee that these objectives can be improved by a specified extent for all forget and retain data. In this work, we address this limitation with a novel and theoretically-grounded approach from a constrained optimization perspective. Firstly, we identify that the hardness of reconciling both objectives can be quantified by the similarity between the forget data and the retain data. Next, we derive an unlearning algorithm (HAMU) with the overall goal of guaranteeing a specified improvement in forget quality while minimizing the retain utility cost/degradation by updating the model weights based on our hardness measure. Our hardness measure also informs users when retain utility degradation is unavoidable, i.e., both objectives cannot be improved simultaneously, and stopping should be considered. Our algorithm is applicable to non-convex models and is easily parallelizable, making it readily deployable in real-world scenarios. We empirically demonstrate HAMU's superior performance over baselines on both image and text datasets using large models. Our code is available at https://github.com/aoi3142/HAMU.

</details>

### 62. ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.18879) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60862)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Yujie Lin、Chengyi Yang、Zhishang Xiang、Yiping Song、Jinsong Su

- 🎯 **研究动机**：现有机器遗忘依赖重训或激进微调，计算昂贵且易损害相关知识
- 🔬 **研究方法**：ZeroUnlearn 把遗忘重构为知识重映射：敏感输入映射到中性目标态并移除原表征，以闭式解乘性参数更新强制表征正交，另有梯度式多样本扩展
- 📌 **结论**：超过现有基线同时保留通用模型效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models inevitably retain sensitive information, defined as inputs that may induce harmful generations, due to training on massive web corpora, raising concerns for privacy and safety. Existing machine unlearning methods primarily rely on retraining or aggressive fine-tuning, which are either computationally expensive or prone to degrading related knowledge and overall model utility. In this work, we reformulate machine unlearning as a precise knowledge re-mapping problem via model editing. We propose ZeroUnlearn, a few-shot unlearning framework. It overwrites sensitive inputs by mapping them to a neutral target state and removing their original representations. ZeroUnlearn enforces representational orthogonality through a multiplicative parameter update with a closed-form solution, enabling efficient and targeted unlearning. We further extend ZeroUnlearn to a gradient-based variant for multi-sample unlearning. Experiments demonstrate that our approach outperforms existing baselines while preserving general model utility. Our code is available at the github: https://github.com/XMUDeepLIT/ZeroUnlearn.

</details>

### 63. Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs

🎓 [Official](https://aclanthology.org/2026.eacl-long.260/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`multilingual unlearning`、`cross-lingual transfer`、`removal asymmetry`、`knowledge removal`

👤 **作者**：Alireza Dehghanpour Farashah、Aditi Khandelwal、Marylou Fauchard、Zhuan Shi、Negar Rostamzadeh、Golnoosh Farnadi

- 🎯 **研究动机**：机器遗忘研究以英语为主，多语言环境跨语言知识迁移与偏置的复杂性未解
- 🔬 **研究方法**：在 Aya-Expanse 8B 上做数据与概念两种遗忘，把事实知识与刻板印象基准翻译扩展到十个语言（五个语系、不同资源水平）
- 📌 **结论**：高资源语言遗忘更稳定，类型学相关语言间存在不对称迁移；句法相似性是跨语言遗忘效应最强预测因子

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As multilingual large language models become more widely used, ensuring their safety and fairness across diverse linguistic contexts presents unique challenges. While existing research on machine unlearning has mainly focused on monolingual settings, typically English, multilingual environments introduce additional complexities due to cross-lingual knowledge transfer and biases embedded in both pretraining and fine-tuning data. In this work, we address the problem of multilingual unlearning using the Aya-Expanse 8B model under two settings: (1) data unlearning and (2) concept unlearning. We extend benchmarks for factual knowledge and stereotypes into ten languages through translation—English, French, Arabic, Japanese, Russian, Farsi, Korean, Hindi, Hebrew, and Indonesian—spanning five language families and varying resource levels. Our experiments show that unlearning in high-resource languages tends to be more stable, with asymmetric transfer observed between typologically related languages. Moreover, analysis of linguistic distances reveals that syntactic similarity is the most predictive factor of cross-lingual unlearning effects.

</details>

### 64. REMIND: Memorization and Unlearning in LLMs Through the Lens of Input Loss Landscapes

🎓 [Official](https://aclanthology.org/2026.acl-long.2215/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`training-data memorization`、`knowledge removal`

👤 **作者**：Liran Cohen、Yaniv Nemcovsky、Avi Mendelson

- 🎯 **研究动机**：逐点损失指标难以察觉机器遗忘后的残余记忆，需要可解释手段诊断 LLM 知识保留状态
- 🔬 **研究方法**：发现遗忘样本在输入损失景观（ILL）中呈低曲率平台，提出 REMIND：在语义一致邻域上探测局部 ILL 曲率，配合嵌入近邻扰动生成受控变体
- 📌 **结论**：多类 ROC-AUC 达 82%，1% FPR 处 AUC 约为 MIN-K%++ 等基线的 2 倍，且对改写输入稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding how large language models (LLMs) store, retain, and remove knowledge is critical for interpretability, reliability, and privacy compliance. We reveal a key phenomenon: machine unlearning imprints distinct geometric signatures in the model’s input loss landscape (ILL), with unlearned examples forming flat, low-curvature plateaus that contrast sharply with the high-curvature basins of retained or unseen examples. Remarkably, these patterns emerge even when pointwise losses overlap, exposing residual memorization through input-output behavior alone. Building on this insight, we introduce REMIND (Residual Memorization in Neighborhood Dynamics), a framework that diagnoses memorization states (retained, forgotten, holdout) by probing local ILL curvature over semantically coherent neighborhoods. REMIND operates using only loss queries and a novel embedding-proximity perturbation method to generate controlled, interpretable variants. In evaluations, REMIND achieves 82% multi-class ROC-AUC, outperforming baselines like ROUGE-L and MIN-K%++, with roughly 2× higher AUC at 1% FPR, and remains robust on paraphrased inputs. This neighborhood-level geometric analysis provides a practical, interpretable lens on LLM knowledge retention and unlearning, detecting subtle residual signals missed by pointwise or aggregated metrics.

</details>

### 65. Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.17620) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60740)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Yuefeng Peng、…、Dezhi Hong

- 🎯 **研究动机**：现有遗忘评估只看 forget 集遗忘程度与 retain 集效用，忽视上下文可用性——被遗忘知识在提示中重新给出时模型仍应会用的能力
- 🔬 **研究方法**：系统评测六个 SOTA 遗忘方法发现一致损害上下文效用，在遗忘目标中加入显式保留上下文效用的即插项
- 📌 **结论**：上下文效用恢复到接近原水平，同时保持有效遗忘与保留集效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models can memorize information that must be removed—ranging from copyright-sensitive content (e.g., book chapters) to personally identifiable information (e.g., income)—to ensure responsible and compliant behavior. Unlearning has emerged as an efficient alternative to full retraining, aiming to remove specific knowledge. However, users may still expect model to leverage the removed information when it is re-introduced in the prompt. Existing evaluations of unlearning methods focus on (1) the extent of forgetting of the target knowledge (forget set) and (2) performance preservation on the retain set (i.e., utility), but overlook this critical usability dimension. Through a systematic evaluation of six state-of-the-art unlearning methods, we show that they consistently degrade such contextual utility—the model's ability to use forgotten knowledge when it is provided in context. To address this, we augment unlearning objectives with a plug-in term that explicitly preserves contextual utility. Extensive experiments demonstrate that our approach restores contextual utility to near original levels while still maintaining effective forgetting and retain-set utility.

</details>

### 66. DualOptim+: Bridging Shared and Decoupled Optimizer States for Better Machine Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.21539) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60714)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Xuyang Zhong、Qizhang Li、Yiwen Guo、Chen Liu

- 🎯 **研究动机**：LLM 遗忘中遗忘与保留目标的优化冲突需要更好平衡机制
- 🔬 **研究方法**：DualOptim+ 引入捕获共享表征的 base state 与保留目标特定残差的 delta state，按两目标梯度方向冲突自适应桥接；另有 8bit 量化变体降内存
- 📌 **结论**：虚构与真实遗忘、安全对齐与多任务学习上持续取得更优目标权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose DualOptim+, a novel optimization framework for improving machine unlearning in large language models. It introduces a base state to capture common representations shared by forgetting and retaining objectives and delta states to preserve objective-specific residuals. This architecture allows the optimizer to adaptively bridge shared and decoupled states based on the directional conflict between forgetting and retaining gradients. We further introduce DualOptim+ 8bit, a quantized variant that reduces memory overhead without compromising performance. Extensive experiments across fictitious and real-world unlearning, safety alignment, and multi-task learning tasks demonstrate that DualOptim+ consistently achieves a superior trade-off between different objectives. Codes are available at https://github.com/CityU-MLO/DualOptimPlus.

</details>

### 67. Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning

📄 [arXiv](https://arxiv.org/abs/2605.16776) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65264)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`concept erasure`、`empirical evaluation`

👤 **作者**：Puning Yang、Junchi Yu、Qizhou Wang、Philip Torr、Bo Han、Xiuying Chen

- 🎯 **研究动机**：知识删除式遗忘因压制特定 token 序列而删除有偏；可区分拒绝式遗忘知识仍在、有重现风险
- 🔬 **研究方法**：D2 在潜表征而非特定 token 上限制响应分布以擦除知识；引入能量指数量化知识存在与分离度，训练时做能量边界遗忘、推理时能量拒绝（EUA）
- 📌 **结论**：EUA 显著超越先前遗忘方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mitigating sensitive and harmful outputs is fundamental to ensuring safe deployment of LLMs. Existing approaches typically follow two paradigms: Knowledge Deletion (KD), which erases undesirable information during training, and Distinguishable Refusal (DR), which steers models away from using sensitive knowledge during inference. Despite rapid progress, KD-based unlearning struggles with biased deletion due to suppressing specific token sequences as a substitute for complete knowledge removal, whereas DR-based unlearning risks the re-emergence of harmful knowledge because the underlying knowledge remains intact. To address these issues, we propose Distinguishable Deletion ($\mathrm{D^2}$), a paradigm that restricts the response distribution in the latent representation rather than specific tokens to erase undesirable knowledge, while distinguishing it from retained knowledge, enabling a refusal mechanism to handle unlearned inputs safely and coherently. To implement $\mathrm{D^2}$, we introduce an energy index that quantifies the presence of knowledge and the separation between unlearned and retained content. Mathematical and empirical analyses show that energy is both accurate and efficient, enabling Energy-based Unlearning Alignment (EUA) to enforce energy-boundary unlearning during training and apply an energy-based refusal mechanism at inference. Extensive experiments demonstrate that EUA significantly outperforms previous methods, indicating the superiority of $\mathrm{D^2}$. Our code is available at https://github.com/Puning97/EUA-for-LLM-Unlearning.

</details>

### 68. One-Turn Knockout: Traceable and Editable Proxy Unlearning Under Asymmetric Access Constraints

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5637.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`proxy unlearning`、`asymmetric access`、`traceability`

- 🎯 **研究动机**：现有遗忘假设可访问目标模型参数与训练数据，而模型提供方与服务运营方访问权限不对称
- 🔬 **研究方法**：OTK 一次后训练把表示空间压缩为 codebook 离散代理，样本记录为 codebook token 分布、贡献经可加 token 统计累计估计；运营方可估分布、识别因果 token 并擦除贡献
- 📌 **结论**：多数据集与任务上持续优于 SOTA 遗忘方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MUL) aims to remove the influence of specific data from a trained model for data privacy and model adaptability. Existing MUL methods mostly assume the internal parameters and the training data of the target model are accessible. Nevertheless, in most practical scenarios, the model provider (MP) and the service operator (SO) are different entities with unequal model access privileges. The MP provides the model, while the SO can only access the model via APIs when handling unlearning requests. Under such an asymmetric access constraint, we propose One-Turn Knockout (OTK), a novel traceable and editable MUL framework based on a model-agnostic and editable proxy. Specifically, OTK first compresses the representation space of the target model into a discrete proxy based on codebook, with merely one pass post-training. Each data sample is recorded in the proxy space as a distribution over the codebook tokens, and its contribution to the model prediction can be cumulatively estimated via additive token statistics. Based on the traceable and editable proxy, the SO can instantly handle unlearning requests by (i) estimating the token distribution of the forgotten data, (ii) identifying the causal tokens, and (iii) erasing their contributions without the access to the model parameters and training data. Extensive experiments on multiple datasets and tasks show that OTK consistently outperforms state-ofthe-art unlearning methods.

</details>

### 69. Forgetting to Forget: Attention Sink as A Gateway for Backdooring LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2510.17021) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-10　🏷 COLM 2026

**关键词**：`attack`、`defense`、`unlearning`、`attention sink`、`backdoored unlearning`、`knowledge recovery`

👤 **作者**：Bingqi Shang、Yiwei Chen、Yihua Zhang、Bingquan Shen、Sijia Liu

- 🎯 **研究动机**：开源权重场景下 unlearning 过程本身可被后门化：表面遗忘成功，触发时却恢复被删知识
- 🔬 **研究方法**：研究触发器放置与后门强化方式，发现后门效力与 attention sink 现象强相关，把触发器置于 sink 位置并对齐其注意力值可显著增强后门持久性
- 📌 **结论**：attention-sink 引导的后门 unlearning 在触发时恢复被遗忘知识，无触发时与正常 unlearned 模型不可区分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) unlearning is a key approach for removing undesired data, knowledge, or behaviors from pretrained models while retaining their general utility. Yet, with the rise of open-weight LLMs, we ask: can the unlearning process itself be backdoored, appearing successful under normal conditions yet reverting to pre-unlearned behavior when a hidden trigger is activated? Drawing inspiration from classical backdoor attacks that embed triggers into training data to enforce specific behaviors, we investigate backdooring unlearning, a setting in which models forget as intended in the clean setting but recover forgotten knowledge when the trigger appears. We show that designing such attacks presents unique challenges, hinging on where triggers are placed and how backdoor training is reinforced. We uncover a strong link between the backdoor efficacy and the attention sink phenomenon (i.e., shallow input tokens consistently attract disproportionate attention). Our analysis reveals that these attention sinks serve as gateways for backdooring unlearning: placing triggers at sink positions and aligning their attention values markedly enhances backdoor persistence. Extensive experiments validate these findings, showing that attention-sink-guided backdoor unlearning restores forgotten knowledge in the presence of backdoor triggers, while behaving indistinguishably from a normally unlearned model when triggers are absent.

</details>

### 70. Rethinking Backdoor Adversarial Unlearning through the Lens of Catastrophic Forgetting in Continual Learning

📄 [arXiv](https://arxiv.org/abs/2606.14078) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`defense`、`backdoor unlearning`、`catastrophic forgetting`、`BI-BAU`

👤 **作者**：Zhenqian Zhu、…、Wenjian Luo

- 🎯 **研究动机**：现有后门防御对特定攻击脆弱，主流安全微调只提供表层保护，未彻底消除后门效应
- 🔬 **研究方法**：从持续学习视角把后门学习/遗忘形式化为三阶段序列过程，推导完全遗忘的必要条件，提出 BI-BAU：将满足遗忘条件的对抗样本生成视为盲反演问题，用 EM 框架整合双层优化求 MAP 目标
- 📌 **结论**：广泛后门攻击上普适且彻底消除后门效应，并扩展到未知目标类与多模态对比学习

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing studies reveal that current backdoor defenses exhibit limited robustness and often fail against specific types of attacks. More concerningly, prevailing safety tuning strategies tend to provide only superficial safety protection, as they fall short of completely eliminating the backdoor effects. In this work, we present a novel formulation of backdoor learning and unlearning as a sequential, three-stage process from a continual learning perspective. Within this framework, we formally define complete backdoor unlearning and further derive the necessary conditions for achieving it based on the mechanism of catastrophic forgetting. Guided by these insights, we propose Blind Inversion-Backdoor Adversarial Unlearning (BI-BAU), which formulates the generation of adversarial examples satisfying the unlearning conditions as a blind inversion problem. We solve this by integrating the bi-level optimization process of adversarial training into an Expectation-Maximization (EM) algorithm framework to optimize the maximum a posteriori (MAP) objective. Furthermore, BI-BAU is extended to untargeted adversarial scenarios with unknown target classes, as well as to multi-modal contrastive learning tasks, enhancing its applicability to real-world deployment scenarios where pre-trained models may be compromised. Extensive experiments demonstrate that our method exhibits general applicability across a wide spectrum of backdoor attacks and can effectively and thoroughly eliminate the backdoor effects from a backdoor model.

</details>

### 71. The Forgetting-Retention Dilemma: Certified Unlearning Theory in Continual Learning

📄 [arXiv](https://arxiv.org/abs/2606.29832) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60494)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`certified robustness`、`deletion verification`

👤 **作者**：Yiting Hu、Lingjie Duan、Qian Zhang

- 🎯 **研究动机**：持续学习中模型顺序演化，现有认证遗忘算法未考虑 CL 的累积模型演化，缺乏理论基础
- 🔬 **研究方法**：把 CL 遗忘目标形式化为遗忘后超额风险最小化并分解为 CL 超额风险与遗忘损失；为非凸模型建立上界，将梯度式与 Hessian 式认证遗忘适配到 CL 并提出混合策略
- 📌 **结论**：梯度式遗忘效果逊于 Hessian 式但存储开销近零，混合策略降低存储同时保持遗忘后性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to eliminate the influence of specific data from trained models to safeguard privacy. However, this presents a significant challenge in the context of continual learning (CL), where models update sequentially on dynamic datasets. A major limitation is that current certified unlearning algorithms fail to account for the complex, cumulative model evolution inherent to CL framework. In this work, we establish the first theoretical foundation bridging CL and machine unlearning. We formulate the CL's unlearning objective as the minimization of post-unlearning excess risk, which decomposes into CL excess risk and unlearning loss, characterizing the fundamental trade-off between preserving historical knowledge and targeted forgetting. Under mild assumptions, we first establish an upper bound for the CL excess risk in non-convex models. We then adapt two certified unlearning approaches, gradient-based and Hessian-based, to the CL framework. Our analysis reveals that while the gradient-based approach is less effective than the Hessian-based method in minimizing unlearning loss, it offers the distinct advantage of nearly zero storage overhead for enabling unlearning. This insight motivates a hybrid strategy that reduces storage costs while maintaining post-unlearning performance. Experimental results further validate our theoretical findings.

</details>

### 72. Obliviate: Efficient Unlearning in Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2607.22665) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64974)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Tushar Prakash、Brijraj Singh、Niranjan Pedanekar、Narayan Chaturvedi

- 🎯 **研究动机**：推荐系统遗忘需删除交互数据及下游影响，现有方法遗忘不彻底、损推荐质量且计算开销大
- 🔬 **研究方法**：Obliviate 两阶段：低秩遗忘适配器用轻量 Hessian 代理做曲率感知局部遗忘；局部性感知校准只更新适配器，排序目标强制遗忘加知识蒸馏保效用
- 📌 **结论**：高遗忘度、推荐质量损失极小且计算成本大幅降低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning is becoming increasingly critical in the context of data privacy regulations, particularly for recommendation systems that are directly trained on user interaction data. The goal of this work is to remove requested interaction data and their downstream influence from trained model while preserving recommendation quality, and to do so without incurring the substantial computational cost of full retraining. Existing approaches exhibit several limitations, including limited unlearning completeness and degradation in recommendation performance, while having substantial computational overhead. In this paper, we propose Obliviate an efficient two-stage unlearning framework for recommender systems that achieves high unlearning completeness while maintaining good utility. In the first stage, we introduce a Low-Rank Unlearning Adapter (LUA), which employs a lightweight Hessian proxy to enable curvature-aware and efficient unlearning through localized low-rank adapters rather than full parameters. In the second stage, we propose Locality-Aware Calibration (LAC), a lightweight refinement stage that updates only the adapter parameters to improve the performance by enforcing unlearning via ranking-based objectives while preserving utility through knowledge distillation. Extensive empirical evaluations demonstrate that Obliviate, achieves high level of forgetting with minimal loss in recommendation quality and at significantly reduced computational cost, offering a practical and scalable solution for large-scale recommender systems.

</details>

### 73. LMCleaner: Efficient and Certified Online Unlearning via Influence Propagation Truncation

🎓 [Official](https://icml.cc/virtual/2026/poster/62503)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`certified robustness`、`deletion verification`

👤 **作者**：Jie Xu、…、Xiaohua Jia

- 🎯 **研究动机**：现有遗忘针对训练完成后，训练进行中出现删除请求需在线能力
- 🔬 **研究方法**：把影响传播分解为线性近似准确的信任域与低维子空间残差：截断窗口内以 mini-batch 影响为原子单元移除并注入校准噪声实现认证隐私
- 📌 **结论**：截断残差随窗口指数衰减，与重训练 (ε,δ)-不可区分；计算节省超 100 倍并抗成员推断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing machine unlearning methods primarily focus on removing data influence after training completes, which is effective for many scenarios, but a complementary capability is needed when removal requests arise during ongoing training. We propose LMCleaner, an efficient and certified *online* unlearning framework that can process unlearning requests at any training step without waiting for training completion. Our key insight is that influence propagation can be decomposed into a trust region where linear approximation is accurate, and a residual that concentrates in a low-dimensional subspace and can be efficiently masked by calibrated noise. Building on this insight, we design an influence propagation truncation mechanism that treats mini-batch influence as atomic units, computes influence within a truncation window for efficient removal, and injects subspace-aware noise for certified privacy. Our theoretical analysis proves that the truncation residual decays exponentially with window size and that the unlearned model is $(\varepsilon, \delta)$-indistinguishable from retraining. Experiments demonstrate that LMCleaner achieves over $100\times$ computational savings compared to baselines while maintaining model utility and defending against membership inference attacks.

</details>

### 74. Exact Unlearning in Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2606.04182) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61630)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reinforcement learning`、`machine unlearning`、`deletion guarantee`、`deletion verification`

👤 **作者**：Thanh Nguyen-Tang、Raman Arora

- 🎯 **研究动机**：强化学习中用户删除请求要求在线学习者输出与该用户从未交互时不可区分，缺乏高效的精确遗忘框架
- 🔬 **研究方法**：对任意 ρ>0 构造 ρ-TV 稳定 RL 算法支持精确遗忘，期望计算成本仅为从头重训的 ρ√(ln T) 倍；表格 MDP 上给出遗憾界并建立匹配下界
- 📌 **结论**：算法近 minimax 最优，兼顾精确遗忘与计算效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We formulate the problem of \emph{exact unlearning} in reinforcement learning, where the goal is to design an efficient framework that enables the removal of any user’s data upon deletion request, i.e., the online learner’s output after unlearning be \emph{indistinguishable} from what would have been produced had the deleted user never interacted with the learner. For any $\rho >0$, we show that there exists a reinforcement learning (RL) algorithm that is $\rho$-TV-stable and supports an exact unlearning procedure whose expected computational cost is only a $\rho \sqrt{\ln T}$ fraction of the computational cost of retraining from scratch. We construct such a $\rho$-TV-stable RL algorithm for tabular Markov decision processes (MDPs), which achieves a regret bound of $\mathcal{O}(H^2 \sqrt{SAT} + H^3 S^2 A + {H^{2.5} S^2 A}/{\rho})$, where $S, A, H$, and $T$ denote the number of states, the number of actions, the episode horizon, and the number of episodes, respectively. We also establish a lower bound of $\Omega(H\sqrt{SAT}+{SAH}/{\rho})$ for $\rho$-TV-stable RL algorithms, showing that our algorithm is nearly minimax optimal.

</details>

### 75. A Durable Machine Unlearning Framework to Nullify Recall of Sensitive Data on Incremental Training

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T108.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026

**关键词**：`defense`、`sensitive-data recall`、`incremental retraining`、`durable suppression`、`durable unlearning`、`sensitive data`

- 🎯 **研究动机**：unlearning 后的模型仍需用新数据增量训练，新数据含相似甚至相同被遗忘样本时会重新唤回敏感信息，该漏洞未被研究
- 🔬 **研究方法**：提出 Durable Unlearning Enhancement 框架：三组件识别增量数据中的敏感样本并抑制其对 ULM 的梯度更新
- 📌 **结论**：在多个真实数据集与 SOTA unlearning 方法上有效消除 MU 后敏感信息回溯，甚至提升 ULM 性能，确立 post-MU 安全训练新方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancement of data privacy regulations has spurred the development of Machine Unlearning (MU), which is designed to remove the influence of sensitive data from a trained model and results in an unlearned model (ULM). Despite rapid progress in MU techniques, their vulnerabilities remain underexplored, which poses risks due to potential leakage of unlearned information. In realistic scenarios, ULMs always need to be incrementally trained with newly collected data samples, which can lead to the consequences of recalling sensitive information if the new dataset contains similar or even the same unlearned samples. To address this issue, we devise a Durable Unlearning Enhancement (DUE) framework to avoid restoring unwanted sensitive information from incremental training data samples. The DUE framework has three key components that identify sensitive samples and suppress their gradients to update ULMs. Extensive experiments on state-of-the-art MU methods across multiple real-world datasets show that the proposed DUE framework can effectively nullify the recall of sensitive information after MU, and even improve the performance of ULMs. Consequently, our work establishes a new fundamental research direction in safe training against post-MU vulnerabilities.

</details>

### 76. Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality

📄 [arXiv](https://arxiv.org/abs/2608.23020)　📅 2026-08

**关键词**：`defense`、`analysis`、`sensitive-anchor retrieval`、`attention pathway`、`modular erasure`、`attention-path decoupling`

👤 **作者**：Xunlei Chen、…、Jinyu Guo

- 🎯 **研究动机**：现有序列/ token 级 unlearning 惩罚目标输出但不建模其上下文相关的检索路径，会破坏语言结构或压制良性知识
- 🔬 **研究方法**：ADU 利用局部与全局 attention head 的功能差异，定位检索 persistent 敏感 anchor 的 preplan 位置并固定候选路径，训练 attention-projection adapter 抑制这些路径上的注意力质量，保留局部结构与 retain 集 LM，并用 activation exchange 检验遗忘的因果传递
- 📌 **结论**：TOFU 与 WMDP 上综合表现最强（TOFU Forget Quality 0.93），保留 87–98% 效用（平均 92.9% 对基线 81.9%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure to contextual attention-pathway decoupling. Exploiting the functional distinction between local and global attention heads, ADU identifies preplan positions that retrieve persistent sensitive anchors and fixes their candidate paths under the original model. It then trains attention-projection adapters to suppress attention mass along these paths while preserving local-attention structure and retain-set language modeling. Post-training activation exchange tests whether the modified attention-output module transmits the learned forgetting effect. ADU achieves the strongest aggregate performance among evaluated baselines on the TOFU and WMDP benchmarks, including a Forget Quality of (0.93) on TOFU. It preserves 87--98% of model utility (92.9% on average versus 81.9% for baselines) while reducing side effects in benign contexts.

</details>

### 77. Spectral Saliency for Machine Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.15548)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`

👤 **作者**：Cedar Site Bai、Amber Yijia Zheng、Raymond A. Yeh、Brian Bullins

- 🎯 **研究动机**：unlearning 需移除数据影响同时保留效用，Muon 的谱视角尚未用于遗忘
- 🔬 **研究方法**：SSU 阈值化弱奇异分量、只更新有置信遗忘信号支持的方向，并从遗忘-保留权衡角度给出理论论证
- 📌 **结论**：图像分类器、扩散模型与 LLM 上均验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) aims to remove the influence of specific training data while preserving model utility. As the name suggests, MU can be viewed as the inverse of learning, using gradient-based updates to reduce the influence of a forget-set by counteracting the previously learned behavior. Recently, Muon, a gradient descent variant, has been introduced. Muon applies spectral magnitude normalization to encourage exploration of rare directions and demonstrates promising performance. Inspired by Muon, we adopt the spectral view for unlearning and propose Spectral Saliency Unlearning (SSU). SSU thresholds weak singular components and updates only those directions supported by a confident unlearning signal. We further provide theoretical justification for this thresholding approach from the perspective of the forgetting-retention trade-off. Experiments across image classifiers, diffusion models, and LLMs demonstrate SSU's effectiveness.

</details>

### 78. Approximate Machine Unlearning through Manifold Representation Forgetting Guided by Self Mode Connectivity

📄 [arXiv](https://arxiv.org/abs/2605.22871) · 🌐 [Project](https://doi.org/10.1145/3770855.3817655)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`machine unlearning`、`manifold forgetting`、`utility retention`

👤 **作者**：Weiqi Wang、Zhiyi Tian、Chenhan Zhang、Luoyu Chen、Shui Yu

- 🎯 **研究动机**：近似机器遗忘难以兼顾删除彻底性与效用保留
- 🔬 **研究方法**：以self mode connectivity引导流形表示遗忘实现近似unlearning
- 📌 **结论**：遗忘目标样本的同时保留模型效用

### 79. Gauss-Newton Unlearning for the LLM Era

📄 [arXiv](https://arxiv.org/abs/2602.10568) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-02　🏷 SaTML 2026

**关键词**：`defense`、`LLM unlearning`、`Gauss-Newton update`、`retain utility`

👤 **作者**：Lev McKinney、…、Roger Grosse

- 🎯 **研究动机**：LLM unlearning 遗忘目标数据时常损伤保留分布上的行为，权衡难改善
- 🔬 **研究方法**：K-FADE 用 K-FAC 近似的少量 Gauss-Newton 上行步做遗忘，把保留集输出约束转化为权重约束以最小化保留行为改动
- 📌 **结论**：在 WMDP 与 ToFU 上逼近无遗忘集重训的输出，对保留集改动小于既有方法，且更新可在后续训练后重复应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Standard large language model training can create models that produce outputs their trainer deems unacceptable in deployment. The probability of these outputs can be reduced using methods such as LLM unlearning. However, unlearning a set of data (called the forget set) can degrade model performance on other distributions where the trainer wants to retain the model's behavior. To improve this trade-off, we demonstrate that using the forget set to compute only a few uphill Gauss-Newton steps provides a conceptually simple, state-of-the-art unlearning approach for LLMs. While Gauss-Newton steps adapt Newton's method to non-linear models, it is non-trivial to efficiently and accurately compute such steps for LLMs. Hence, our approach crucially relies on parametric Hessian approximations such as Kronecker-Factored Approximate Curvature (K-FAC). We call this combined approach K-FADE (K-FAC for Distribution Erasure). Our evaluation on the WMDP and ToFU benchmarks demonstrates that K-FADE suppresses outputs from the forget set and approximates, in output space, the results of retraining without the forget set. Critically, our method does this while altering the outputs on the retain set less than previous methods. This is because K-FADE transforms a constraint on the model's outputs across the entire retain set into a constraint on the model's weights, allowing the algorithm to minimally change the model's behavior on the retain set at each step. Moreover, the unlearning updates computed by K-FADE can be reapplied later if the model undergoes further training, allowing unlearning to be cheaply maintained.

</details>

### 80. GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints

📄 [arXiv](https://arxiv.org/abs/2601.16905) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-01

**关键词**：`defense`、`machine unlearning`、`Mixture-of-Experts`、`router constraint`

👤 **作者**：Andy Zhu、Rongzhe Wei、Yupu Gu、Pan Li

- 🎯 **研究动机**：MoE unlearning 常操纵路由绕开原专家而非真正擦除知识，效用大损且休眠专家可被绕过路由恢复
- 🔬 **研究方法**：GRIP 算法无关框架：把路由器梯度更新投影到 retain 集路由矩阵的零空间以抑制路由操纵，把遗忘压力导入专家参数；含训练时随机投影与训练后闭式校正两个变体
- 📌 **结论**：路由稳定性从 0.21 恢复至 0.94 以上，retain 准确率最多提升 89%，白盒对抗知识恢复从 11% 降至 3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning in Mixture-of-Experts (MoE) large language models presents a critical yet under-explored challenge. Current unlearning methods applied to MoE architectures often exploit dynamic routing as an optimization shortcut: rather than genuinely erasing knowledge from expert parameters, they manipulate routers to redirect queries away from the originally assigned experts. This not only causes severe utility degradation but also leaves hazardous knowledge intact. Consequently, adversaries can bypass the router to recover sensitive information directly from dormant experts. In this study, we propose Geometric Routing Invariance Preservation (GRIP), an algorithm-agnostic framework that resolves these failure modes by enforcing hard geometric constraints on router updates. By projecting router gradient updates into the null space of the retain set's routing matrix, GRIP suppresses routing manipulation without freezing the router entirely, thereby directing the unlearning pressure into the expert parameters themselves across all relevant experts. GRIP offers two complementary variants: training-time stochastic projection and a post-training closed-form analytical correction. Extensive experiments on two MoE models across hazardous knowledge removal and copyright unlearning benchmarks demonstrate that GRIP restores routing stability from 0.21 to >0.94, improves retain accuracy by up to 89%, and reduces white-box adversarial knowledge recovery from 11% to just 3% while in line with dense-architecture unlearning under black-box prompt attack, establishing geometric constraints as a principled solution for genuine unlearning in sparse MoE architectures.

</details>

### 81. Representation Unlearning: Forgetting through Information Compression

📄 [arXiv](https://arxiv.org/abs/2601.21564) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65507)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Antonio Almudévar、Alfonso Ortega

- 🎯 **研究动机**：修改参数的机器遗忘方法不稳定、代价高且受局部近似限制
- 🔬 **研究方法**：提出 Representation Unlearning：在表示空间学习施加信息瓶颈的变换，最大化保留数据互信息并压制遗忘数据信息，导出变分代理并支持仅访问遗忘数据的零样本设定
- 📌 **结论**：遗忘更可靠、效用保留更好且计算效率高于参数中心基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning seeks to remove the influence of specific training data from a model, a need driven by privacy regulations and robustness concerns. Existing approaches typically modify model parameters, but such updates can be unstable, computationally costly, and limited by local approximations. We introduce Representation Unlearning, a framework that performs unlearning directly in the model’s representation space. Instead of modifying model parameters, we learn a transformation over representations that imposes an information bottleneck: maximizing mutual information with retained data while suppressing information about data to be forgotten. We derive variational surrogates that make this objective tractable and show how they can be instantiated in two practical regimes: when both retain and forget data are available, and in a zero-shot setting where only forget data can be accessed. Experiments across several benchmarks demonstrate that Representation Unlearning achieves more reliable forgetting, better utility retention, and greater computational efficiency than parameter-centric baselines.

</details>

### 82. Less is More: Geometric Unlearning for LLMs with Minimal Data Disclosure

📄 [arXiv](https://arxiv.org/abs/2605.01735) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63359)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Chenchen Tan、Xinghao Li、Shujie Cui、Youyang Qu、Cunjian Chen、Longxiang Gao

- 🎯 **研究动机**：现有 LLM 遗忘需原训练语料且靠拒答调优或宽泛梯度更新，遗忘强度、非目标保留与数据可用性互相牵制
- 🔬 **研究方法**：GU 直接作用于提示条件化隐藏态：从少量安全参考提示蒸馏低秩安全子空间，锚点合成提示触发投影式局部对齐，teacher 蒸馏正则减少附带漂移
- 📌 **结论**：TOFU 与 UnlearnPII 上强目标抑制且非目标性能影响极小，仅需少量合成数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed in real-world systems, they must support post-hoc removal of specific content to meet privacy and governance requirements. This motivates selective unlearning, which suppresses information about a particular entity or topic while preserving the LLM's general utility. However, most existing LLM unlearning methods require access to the original training corpus and rely on output-level refusal tuning or broad gradient updates, creating a tension among unlearning strength, non-target preservation, and data availability. We propose Geometric Unlearning (GU), an approach that operates directly on the model's prompt-conditioned hidden states without access to the original training corpus. Specifically, GU distills a compact, low-rank safe-behavior subspace from a small set of safe reference prompts and uses lightweight anchor-in-context synthetic prompts to trigger localized, projection-based alignment of hidden representations to this safe subspace. A teacher-distillation regularizer on synthetic non-target anchors further reduces collateral drift. Across privacy-oriented unlearning benchmarks (ToFU and UnlearnPII), GU achieves strong target suppression with minimal impact on non-target performance, demonstrating that effective unlearning can be achieved with minimal synthetic data.

</details>

### 83. Exploring Nonlinear Pathway in Parameter Space for Machine Unlearning

📄 [arXiv](https://arxiv.org/abs/2505.10859) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63914)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`empirical evaluation`、`deletion verification`

👤 **作者**：Yingdan Shi、Ren Wang

- 🎯 **研究动机**：基于任务算术的线性参数遗忘受权重纠缠困扰
- 🔬 **研究方法**：MCU 用模式连通性在参数空间找非线性遗忘通路，配参数掩码（提升效果降开销）与自适应惩罚系数（免经验调参），沿通路揭示一族遗忘模型
- 📌 **结论**：即插即用提升任意现有 MU 方法，图像分类上性能优越

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine Unlearning (MU) aims to remove the information of specific training data from a trained model, ensuring compliance with privacy regulations and user requests. While one line of existing MU methods relies on linear parameter updates via task arithmetic, they suffer from weight entanglement. In this work, we propose a novel MU framework called Mode Connectivity Unlearning (MCU) that leverages mode connectivity to find an unlearning pathway in a nonlinear manner. To further enhance performance and efficiency, we introduce a parameter mask strategy that not only improves unlearning effectiveness but also reduces computational overhead. Moreover, we propose an adaptive adjustment strategy for our unlearning penalty coefficient to adaptively balance forgetting quality and predictive performance during training, eliminating the need for empirical hyperparameter tuning. Unlike traditional MU methods that identify only a single unlearning model, MCU uncovers a spectrum of unlearning models along the pathway. Overall, MCU serves as a plug-and-play framework that seamlessly integrates with any existing MU methods, consistently improving unlearning efficacy. Extensive experiments on the image classification task demonstrate that MCU achieves superior performance. The codes are available at https://github.com/TIML-Group/Mode-Connectivity-Unlearning.

</details>

### 84. Exact Unlearning of Finetuning Data via Model Merging at Scale

📄 [arXiv](https://arxiv.org/abs/2504.04626) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-04　🏷 SaTML 2026

**关键词**：`defense`、`exact unlearning`、`model merging`、`SIFT-Masks`

👤 **作者**：Kevin Kuo、Amrith Setlur、Kartik Srinivas、Aditi Raghunathan、Virginia Smith

- 🎯 **研究动机**：近似遗忘脆弱且可被攻击复原数据，标准模型合并在大规模任务下损效用或令精确遗忘代价过高
- 🔬 **研究方法**：提出 SIFT-Masks，以局部 mask 恢复任务性能，全局符号向量约束微调使各 mask 可独立确定后再合并
- 📌 **结论**：合并最多 500 个模型时准确率比朴素合并高 5-80%，精确遗忘计算量最多降 250 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Approximate unlearning has gained popularity as an approach to efficiently update an LLM so that it behaves (roughly) as if it was not trained on a subset of data to begin with. However, existing methods are brittle in practice and can easily be attacked to reveal supposedly unlearned information. To alleviate issues with approximate unlearning, we instead propose SIFT-Masks (SIgn-Fixed Tuning-Masks), an exact unlearning method based on model merging. SIFT-Masks addresses two key limitations of standard model merging: (1) merging a large number of tasks can severely harm utility; and (2) methods that boost utility by sharing extra information across tasks make exact unlearning prohibitively expensive. SIFT-Masks solves these issues by (1) applying local masks to recover task-specific performance; and (2) constraining finetuning to align with a global sign vector as a lightweight approach to determine masks independently before merging. Across four settings where we merge up to 500 models, SIFT-Masks improves accuracy by 5-80% over naive merging and uses up to 250x less compute for exact unlearning compared to other merging baselines.

</details>

### 85. Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance

📄 [arXiv](https://arxiv.org/abs/2602.10217) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66060)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`generative model safety`、`machine unlearning`、`concept erasure`、`empirical evaluation`

👤 **作者**：Jacob L. Block、Mehryar Mohri、Aryan Mokhtari、Sanjay Shakkottai

- 🎯 **研究动机**：生成模型遗忘中 classifier guidance 在 forget 集为尖锐集中分布时的有限样本下无法忠实遗忘
- 🔬 **研究方法**：提出 T3-Unlearning：冻结基座模型，先 tempering 平坦化高置信尖峰，再用轻量分类器 tilt 临时分布；理论给出代理分类器风险与遗忘质量的有限样本保证，证明 tempering 对集中分布必要
- 📌 **结论**：TOFU 基准上遗忘质量与生成效用均超基线，仅训练少量参数且运行时间极短

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study machine unlearning in large generative models by framing the task as density ratio estimation to a target distribution rather than supervised fine-tuning. While classifier guidance is a standard approach for approximating this ratio and can succeed in general, we show it can fail to faithfully unlearn with finite samples when the forget set represents a sharp, concentrated data distribution. To address this, we introduce Temper-Then-Tilt Unlearning (T3-Unlearning), which freezes the base model and applies a two-step inference procedure: (i) tempering the base distribution to flatten high-confidence spikes, and (ii) tilting the tempered distribution using a lightweight classifier trained to distinguish retain from forget samples. Our theoretical analysis provides finite-sample guarantees linking the surrogate classifier's risk to unlearning quality, proving that tempering is necessary to successfully unlearn for concentrated distributions. Empirical evaluations on the TOFU benchmark demonstrate that T3-Unlearning improves forget quality and generative utility over existing baselines, while training only a fraction of the parameters with a minimal runtime.

</details>

### 86. Beyond Cross-Lingual Transfer: Benchmarking Propagation Boundaries in Multilingual LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2609.05976)　📅 2026-09

**关键词**：`benchmark`、`multilingual unlearning`、`propagation boundary`、`language-conditioned forgetting`

👤 **作者**：Pengyang Shao、…、Richang Hong

- 🎯 **研究动机**：多语言 unlearning 评测只测跨语言迁移，无法区分传播不足与越界扩散
- 🔬 **研究方法**：CLLPU：goal-guided 主题配对+模式感知关系匹配+双锚多语翻译，构造 800 组匹配知识单元、10 语言 72,000 QA，区分 common-goal 与 language-conditioned forgetting
- 📌 **结论**：六种方法呈相反失效：应全忘时遗忘不完全，应限界时越界扩散；多语言总体效用会掩盖邻接知识损伤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) unlearning aims to suppress target knowledge while preserving general capabilities. In multilingual settings, unlearning must additionally propagate within its intended linguistic scope. However, existing evaluations mainly measure cross-lingual transfer and cannot distinguish insufficient from excessive propagation. We introduce CLLPU (Cross-Lingual and Language-Bound Protocol for LLM Unlearning), a multilingual benchmark that formulates this problem through two settings: common-goal forgetting, where target knowledge should be suppressed across all languages, and language-conditioned forgetting, where suppression should remain confined to a designated language. CLLPU combines goal-guided topic pairing, schema-aware relation matching, and dual-anchor multilingual translation to construct 800 matched knowledge-unit pairs and 72,000 QA instances across ten languages. Experiments with six representative methods on Llama-3.1-8B-Instruct reveal opposite failure modes: forgetting remains incomplete when universal suppression is required, yet spreads beyond the intended boundary when language-conditioned confinement is required. We further find that general multilingual utility can conceal damage to neighbor knowledge. These findings establish propagation control as a central challenge for multilingual LLM unlearning. We publicly release CLLPU together with its construction pipeline.

</details>

### 87. K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments

📄 [arXiv](https://arxiv.org/abs/2609.12808)　📅 2026-09

**关键词**：`benchmark`、`agentic unlearning`、`multi-channel leakage`、`refusal vs forgetting`

👤 **作者**：Guangsheng Yu、Yanna Jiang、Qin Wang、Baihe Ma、Xu Wang

- 🎯 **研究动机**：TOFU/MUSE 等 unlearning 基准以模型最终答案判定遗忘、拒答即算已忘，但该模型级证书部署为 agent 后是否迁移从未被检验——agent 的 CoT、工具调用、工具观察与总结都是泄漏通道
- 🔬 **研究方法**：K-Bench 检查 ReAct agent 暴露的全部六个通道（含 CoT、工具调用、工具观察与引出的总结）；把秘密分别置于权重、prompt 或检索库三种来源之一，K-Score 分源计分且要求 agent 保持可用才记为遗忘，任何通道出现秘密即判泄漏
- 📌 **结论**：清空答案通道不等于不可恢复：秘密在结构化检索库时原文留在工具观察通道、总泄漏率不变；秘密在 prompt/检索库时 TOFU/MUSE 报零泄漏而部署 agent 仍在 22-86% 查询中泄漏；秘密在权重时 20 个已发表方法无一可证移除，仅输入扰动干预达到选择性遗忘，且方法排名随基座模型改变

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning benchmarks such as TOFU and MUSE certify forgetting by reading the model's final answer, where a model that refuses to answer already counts as having forgotten. We show that this model-level certificate does not transfer once the model is deployed as an agent. We introduce K-Bench, a benchmark that scores LLM unlearning under agentic deployment. K-Bench inspects all six channels a ReAct agent exposes, including its chain-of-thought (CoT), tool calls and tool observations, and elicited summary. A query counts as leaked if the secret appears in any of them. Each experiment places the secret in exactly one of the agent's three sources (the weights, the prompt, or the retrieval store). The K-Score is computed separately for each source and credits forgetting only when the agent remains usable. Clearing the answer channel does not make the secret unrecoverable. On structured retrieval, the secret stays verbatim in the tool-observation channel and the aggregate leak rate is unchanged. When the secret lives in the prompt or the retrieval store, TOFU and MUSE report no leakage, while the deployed agent still leaks it on 22--86\% of queries. When the secret is in the weights, none of the twenty evaluated published methods demonstrably removes it, and only an input-corruption intervention reaches selective forgetting under the evaluated observer. The top-ranked method changes across base models. A refusal-tuning method resists the evaluated extraction without verified knowledge removal.

</details>

## 常规收录
