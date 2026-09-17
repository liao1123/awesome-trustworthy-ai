# 公平性与 Bias

[返回上级目录](README.md)

## 研究方向

研究模型和 AI 系统对明确群体和社会身份造成的差异性伤害，覆盖 bias measurement、shortcut audit、reward-model bias、fairness intervention 和高风险部署中的 disparate impact。只比较抽象文化价值、道德判断或群体差异而没有危害路径与干预的工作不收录。

## 研究脉络

- **输出偏差测量：** 早期 benchmark 比较不同 demographic prompt 下的预测、生成和拒答差异。
- **内部与数据机制：** Shortcut group、representation 和 reward shaping 分析偏差如何形成和持续。
- **干预与审计：** 训练、推理时 mitigation 与算法审计开始同时报告总体效用和 worst-group 结果。
- **当前边界：** 群体标签、文化价值与任务定义本身并非中性，单一 fairness metric 难覆盖真实影响。

## Survey 与系统边界

### 1. Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.29590)　📅 2026-09

**关键词**：`benchmark`、`guardrail-agnostic bias`、`implicit demographic cue`、`task-irrelevant personalization`、`refusal-confounded evaluation`、`guardrail-agnostic protocol`

👤 **作者**：Yusuke Hirota、…、Ryo Hachiuma

- 🎯 **研究动机**：现有社会偏差 benchmark 要求模型推断图中人物属性，强 guardrail 的 LVLM（GPT、Claude）常拒答使评测失真
- 🔬 **研究方法**：把任务与人物解耦：用与人物无关的 prompt（故事生成、术语解释、考试 QA）并把图像作为隐式人口线索，比较不同用户画像的输出
- 📌 **结论**：20 个 LVLM 全部在无关任务中不当使用人口信息（男性用户配 mechanic、女性配 nurse）；GPT-5 等专有模型偏差仍低于开源模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a societal bias evaluation method for large vision-language models (LVLMs) in the era of strong safety guardrails. Existing benchmarks rely on prompts that ask models to infer attributes of people in images (e.g., "Is this person a CEO or a secretary?"). However, we find that LVLMs with strong guardrails, such as GPT and Claude, often refuse these prompts, making evaluations unreliable. To address this, we change the prior evaluation paradigm by decoupling the task from the depicted person: instead of inferring person's attributes, we use prompts that do not ask about the person (e.g., "Write a fictional story about an imaginary person.") and attach the image as provisional user information to implicitly provide demographic cues, then compare outputs across user demographics. Instantiated across three tasks --- story generation, term explanation, and exam-style QA --- our method avoids refusals even in guardrailed LVLMs, enabling reliable bias measurement. Applying it to 20 recent LVLMs, both open-source and proprietary, we find that all models undesirably use user demographic information in person-irrelevant tasks; for instance, characters in stories are often portrayed as mechanic for male users and nurse for female users. Although still biased, proprietary models like GPT-5 show lower bias than open-source ones. We analyze potential factors behind this gap, discussing continuous model monitoring and improvement as a possible contributor for reducing bias.

</details>

### 2. Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines

📄 [arXiv](https://arxiv.org/abs/2608.29589)　📅 2026-09

**关键词**：`benchmark`、`analysis`、`dialect-aware moderation`、`false-positive disparity`、`under-detection`、`T2I safety pipeline`

👤 **作者**：Minkyu Kim、Juhwan Choi、YoungBin Kim

- 🎯 **研究动机**：T2I 安全护栏对非标准方言泛化不公平，均值精度 benchmark 掩盖了这一公平性失败
- 🔬 **研究方法**：在五种英语方言 23,080 对 prompt 上定义 dialect penalty，用 typo 消融定位根因，并测试 group-balanced retraining 缓解
- 📌 **结论**：NSFW-T 与 LatentGuard 出现最高 +28.29pp 且方向相反的 bias gap，OpenAI Moderation API 漏检方言内容；penalty 源于方言特征而非 OOD 敏感性，均衡重训练可缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) safety guardrails fail to generalize equitably to non-standard dialects. Evaluating 23,080 paired prompts across five English dialects, we formalize this failure as the dialect penalty, where filters trigger based on linguistic surface features rather than semantic intent. Text-level filters fail in opposing directions: NSFW-T over-flags benign dialect prompts and LatentGuard over-flags toxic ones (bias gaps up to +28.29 pp), while the OpenAI Moderation API under-detects them. A controlled typo ablation confirms this penalty originates from flagging dialectal features, not generic out-of-distribution sensitivity. The pixel-level generator is largely dialect-agnostic; the penalty enters at text processing and cascades unevenly to post-hoc guardrails. We show this bias tracks training data imbalance and is mitigable via group-balanced retraining, with an ablation attributing the gain to balanced exposure rather than to the worst-group objective of GroupDRO (group distributionally robust optimization). Current pipelines systematically fail dialect speakers, an equity failure masked by mean accuracy benchmarks. Our official code and dataset are publicly available at https://github.com/minguinho26/dialect-penalty-t2i. Content Warning: This paper contains offensive, toxic, or disturbing text prompts and generated images.

</details>

### 3. Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages

📄 [arXiv](https://arxiv.org/abs/2608.22490)　📅 2026-08

**关键词**：`benchmark`、`multilingual guard`、`Safety Cost`、`filter failure`、`multilingual alignment`、`safety-utility disparity`

👤 **作者**：Chanwoong Yoon、Jungsoo Park、Alan Ritter

- 🎯 **研究动机**：安全对齐会降低效用，但该代价是否在各语言间均等分担一直缺乏严格测量
- 🔬 **研究方法**：提出 Safety Cost 协议：将安全对齐模型与其未对齐版本直接成对比较，隔离仅由对齐造成的效用损失，并从拒答与多维隐性质量差异两方面归因
- 📌 **结论**：非英语用户系统性承担更高 Safety Cost；多语言处于保护更弱且损失更大的双重惩罚区；部分语言的表面效用增益实为过滤器失效，连高资源语言达同等安全也要付更高代价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment helps models adhere to human values, but it often reduces response utility. We ask a critical but understudied question: Does safety alignment impose the cost equally across language groups? To answer this, we introduce a rigorous protocol to measure the utility loss imposed solely by safety alignment, which we term Safety Cost. Through direct pairwise comparisons between safety-aligned models and their unaligned counterparts, we find a systematic inequity: non-English users consistently bear a higher Safety Cost than English users. We further identify three underlying patterns. First, multiple languages lie in a double-penalty zone, experiencing both weaker safety protection and larger utility loss. Second, certain languages exhibit apparent utility gains that are in fact a consequence of safety filters failing to engage. Third, even high-resource languages pay a larger Safety Cost than English to reach the same level of safety. We show that these disparities arise from both explicit refusals and implicit qualitative differences across multiple dimensions. By accurately measuring the disparate effects of safety alignment, our findings expose a systematic disparity in current safety alignment practices.

</details>

### 4. Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs

📄 [arXiv](https://arxiv.org/abs/2608.18131)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`Indian languages`、`cross-lingual safety`、`cultural bias`、`alignment gap`

👤 **作者**：Namya Bhatnagar

- 🎯 **研究动机**：安全对齐高度英语中心，非英语失败时语音助手会绕过安全过滤向非英语社区传播有害偏见
- 🔬 **研究方法**：INCLUDE 基准含 2604 条提示覆盖英语、Hindi、Bengali、Marathi、Tamil 与 Hinglish，评十个开源与闭源 LLM 的 14,988 个偏见分
- 📌 **结论**：开源模型中 Bengali 平均偏见分最高；英语出现反转——开源模型中最低、闭源模型中最高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current safety alignment training for Large Language Models (LLMs) are heavily English-centric. When such safety filters fail for non-English languages, the consequences are immediate and user-facing: voice assistants and spoken dialogue systems may produce stereotype-reinforcing outputs, bypassing the standard English-focused safety alignments and propagating harmful bias to non-English speaking communities. For spoken language technologies deployed across India's linguistically diverse population, this represents a critical failure mode. To address this cross-lingual gap, we introduce INCLUDE (Indian Cultural Lens for Understanding and Detecting Embedded Biases), a multilingual evaluation benchmark designed to quantify Indian-centric socio-cultural biases. INCLUDE consists of 2,604 prompts spanning six prompt languages: English, Hindi, Bengali, Marathi, Tamil, and Hinglish (Hindi-English code-mix). We evaluate ten open- and closed-source LLMs against this benchmark, analyzing 14,988 bias scores. Our statistical results reveal two key findings. First, Bengali yielded the highest average bias score in open-source models. Second, English demonstrated a notable reversal, producing the lowest bias in open-source models but the highest bias in closed-source models.

</details>

### 5. When Personalization Becomes Bias: Structural and Discursive Religious Framing in AI-Generated Financial Advice

📄 [arXiv](https://arxiv.org/abs/2608.16909)　📅 2026-08

**关键词**：`analysis`、`religious-identity bias`、`financial advice`、`discursive framing`、`religious personalization`、`deployment audit`

👤 **作者**：Muhammad Salar Khan、Hamza Umer、Hasan Mahmud、Sandra Rothenberg

- 🎯 **研究动机**：LLM 金融建议中的宗教偏见及其语言实现机制缺乏系统证据
- 🔬 **研究方法**：三个 LLM 的 432 次模拟顾问-客户交互，覆盖 16 种宗教身份配对与股票、购房、人寿保险三项决策，回归加反身主题分析
- 📌 **结论**：无偏建议仅占 12-18%；宗教对称配对几乎总触发显式宗教框架，偏见经宗教锚定、不均衡文化信号与语气调制的语言机制实现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly integrated into financial advisory systems, yet their role in reproducing religious bias remains underexamined. This study provides systematic mixed-methods evidence of such bias across three LLMs (ChatGPT, Gemini, and Grok) using 432 simulated advisor-client interactions spanning 16 religious identity pairings (Christian, Muslim, Hindu, and non-religious) and three core household financial decisions: stock investment, house purchase, and life insurance. Combining regression and reflexive thematic analyses, we identify structural biases across models and decision contexts and the discursive mechanisms through which they are linguistically enacted. Unbiased advice appeared in only 12-18% of cases. Gemini consistently produced more bias than Grok, while ChatGPT's outputs were statistically comparable to Grok's. Religiously symmetric advisor-client pairings almost always triggered explicit religious framing, and non-religious clients often received advisor-centered religious appeals. Qualitative findings show that bias is linguistically manifested through religious anchoring, uneven cultural signaling, and tone modulation, varying by model and financial scenario. Stock investment prompts produced more financially technical responses, whereas life insurance advice triggered stronger religious language. The study develops a dual-dimensional framework linking structural bias rooted in model training and design with discursive bias expressed through language, advancing understanding of algorithmic bias in LLM-generated financial advice. It also shows that such advice adapts linguistically to identity cues, revealing a managerial dilemma between personalization and neutrality. Finally, it highlights implications for businesses, financial institutions, and regulators seeking to ensure neutrality, cultural sensitivity, and trust in AI-mediated advice.

</details>

### 6. Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining

📄 [arXiv](https://arxiv.org/abs/2608.18089) · 📝 [OpenReview](https://openreview.net/forum?id=4UwS3bn1fB)　📅 2026-08

**关键词**：`defense`、`analysis`、`multilingual safety recovery`、`refusal anchoring`、`cross-language transfer`、`cross-lingual refusal`

👤 **作者**：Godwin Abuh Faruna

- 🎯 **研究动机**：指令模型英语拒答但 Yoruba、Igbo、Igala、Hausa 合规，恢复拒答通常需标注目标语数据与重训
- 🔬 **研究方法**：LSR-Anchoring 免训练从英语 prompt 提取拒答方向并在推理时 clamp 到残差流：MAS 跨四架构；SAE-Derived Steering 以单个 SAE 特征替换稠密方向
- 📌 **结论**：Mistral 与 Qwen 上恢复安全且良性退化低于 0.08；SDS 把 KL 散度降 3.5-7 倍避免良性崩溃；MMLU 掉分始终低于 0.35 个百分点，但 Arabic 在所有架构与强度下失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction-tuned models often refuse harmful requests in English but comply with the same requests in Yoruba, Igbo, Igala, and Hausa. This suggests that the refusal mechanism is present in the residual stream but fails to activate for low-resource inputs. Recovering it normally requires labelled target-language data and retraining, neither of which is available at scale for most African languages. We introduce Latent Space Refusal Anchoring (LSR-Anchoring), a training-free method that extracts the refusal direction from English prompts and clamps it onto the residual stream at inference time. The primary variant, Mean-Activation Steering (MAS), operates across the four architectures we tested: Llama-3-8B, Llama-3.1-70B, Mistral-7B-Instruct, and Qwen2.5-7B. On Mistral and Qwen it recovers safety with benign degradation below 0.08. On Llama-3-8B it overcorrects, with Degraded Performance on Legitimate prompts (DPL) reaching 1.00. We address this with SAE-Derived Steering (SDS), which replaces the dense mean-difference direction with a single Sparse Autoencoder (SAE) feature and reduces Kullback-Leibler (KL) divergence by 3.5-7x without benign collapse. Four languages transfer positively, but Arabic fails on every architecture and at every steering magnitude, indicating a geometric mismatch rather than a baseline effect. Massive Multitask Language Understanding (MMLU) accuracy drops remain below 0.35 percentage points at every effective steering magnitude.

</details>

### 7. To Lie or Not to Lie? Investigating The Biased Spread of Global Lies by LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.695/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`algorithmic fairness`、`bias evaluation`、`disparate impact`、`deceptive behavior`、`misinformation`

👤 **作者**：Zohaib Khan、…、Tarek Naous

- 🎯 **研究动机**：LLM 强写作能力降低制造传播虚假信息的门槛，其跨语言与目标国的错误信息行为差异缺乏系统研究
- 🔬 **研究方法**：构建 GlobalLies：440 个错误信息生成模板与 6867 个实体、覆盖 8 种语言与 195 个国家的平行数据集，结合人工标注与 LLM-as-a-judge 评估数十万条生成
- 📌 **结论**：谎言传播在低资源语言与低 HDI 国家显著更高；输入安全分类器跨语言有缺口、RAG 事实核查跨地区不一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Misinformation is on the rise, and the strong writing capabilities of LLMs lower the barrier for malicious actors to produce and disseminate false information. We study how LLMs behave when prompted to spread misinformation across languages and target countries, and introduce GlobalLies, a multilingual parallel dataset of 440 misinformation generation prompt templates and 6,867 entities, spanning 8 languages and 195 countries. Using both human annotations and large-scale LLM-as-a-judge evaluations across hundreds of thousands of generations from state-of-the-art models, we show that misinformation generation varies systematically based on the country being discussed. Propagation of lies by LLMs is substantially higher in many lower-resource languages and for countries with a lower Human Development Index (HDI). We find that existing mitigation strategies provide uneven protection: input safety classifiers exhibit cross-lingual gaps, and retrieval-augmented fact-checking remains inconsistent across regions due to unequal information availability. We release GlobalLies for research purposes, aiming to support the development of mitigation strategies to reduce the spread of global misinformation: https://github.com/zohaib-khan5040/globallies

</details>

### 8. GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.25375)　📅 2026-08

**关键词**：`defense`、`counterfactual bias subspace`、`spherical steering`、`adaptive token gate`、`generative VLM debiasing`、`geodesic steering`

👤 **作者**：Yiqun Sun、Junyu Chen、Pengfei Wei、Lawrence B. Hsieh

- 🎯 **研究动机**：推理时去偏方法面向静态嵌入或 CLIP，不适用于生成式 VLM
- 🔬 **研究方法**：GGSS 在超球面发现反事实偏见子空间，沿测地线引导视觉 token，自适应门聚焦强人口信号
- 📌 **结论**：四个 VLM 上平均偏见最低（三个显著），MMStar 保持基线 ±0.6 个百分点内

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative vision-language models (VLMs) are increasingly used in human-centered settings, yet they can produce demographically biased outputs even when images differ only in controlled attributes such as perceived race or gender. However, existing inference-time debiasers were largely designed for static embeddings or CLIP-like models rather than generative VLMs. We propose GGSS---Geodesic-Gated Spherical Steering---a norm-preserving intervention that discovers a counterfactual bias subspace on the unit hypersphere, steers visual tokens along geodesic arcs, and uses an adaptive gate to focus correction on tokens that carry stronger demographic signal. We evaluate four generative VLMs against ten adapted inference-time debiasing baselines and prompt-based mitigation under a single operating-point protocol across categorical, pairwise, and occupation-gender bias tests, while also measuring general visual-language capability. GGSS achieves the lowest average bias on all four models, significant on three of four backbones under paired permutation tests, while preserving MMStar accuracy within +/- 0.6 p.p. of the unsteered baseline. Code is available at https://github.com/dukesun99/GGSS.

</details>

### 9. Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning

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

### 10. Inference-Time Mitigation of Adversarial Political Bias in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.14629)　📅 2026-08

**关键词**：`defense`、`adversarial robustness`、`algorithmic fairness`、`bias evaluation`

👤 **作者**：Tejaswi V. Panchagnula、Bruce Coburn、Bryce J. Dietrich、Robert X. Browning、Edward J. Delp、Fengqing Zhu

- 🎯 **研究动机**：现代对齐技术未把政治偏见列为有害内容，对抗提示注入可诱发政治偏向摘要
- 🔬 **研究方法**：用立法视频公开数据集生成摘要并对抗注入偏见，四轴政治摘要量表评测；提出 CoT 提示与 DPO 缓解，含 Recursive Self-Correction
- 📌 **结论**：Recursive Self-Correction 把政治中立 Likert 评分从基线 2.14 提升至 4.56（跨模型平均），实现推理时政治偏差缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) become the mainstay for information retrieval and summarization tasks, ensuring that they are always non-partisan and invulnerable to political bias is a critical step towards safer and more trustworthy Artificial Intelligence (AI). Current model alignment paradigms, such as reinforcement learning from human feedback (RLHF), make LLMs follow overarching safety instructions. However, this instruction tuning can be exploited via adversarial prompt injection and be used to generate unsafe content. In particular, political bias has not been specifically targeted by modern alignment techniques as harmful and biased content. To address this vulnerability of LLMs, we propose mitigation strategies using Chain of Thought (CoT) prompting and Direct Preference Optimization (DPO). Using a public dataset of legislative videos, we generate summaries using LLMs, inject bias via adversarial prompting and evaluate their performance on a four axis scale designed for political summarization. In this paper, we present different methods to shield LLMs against the injection of political bias. Our results demonstrate that the proposed Recursive Self-Correction approach raises model performance from a Political Neutrality Likert scale baseline of 2.14 to 4.56, averaged across all models, demonstrating effective inference-time mitigation of political bias in LLM-generated summaries.

</details>

### 11. Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases

📄 [arXiv](https://arxiv.org/abs/2605.27355) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61418)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`reinforcement learning`、`algorithmic fairness`、`bias evaluation`、`AI control`

👤 **作者**：Dongyoon Hahm、Dylan Hadfield-Menell、Kimin Lee

- 🎯 **研究动机**：RLHF 的偏好集来自模型自身输出且成对比较只说哪个更好不问为何，存在结构性漏洞
- 🔬 **研究方法**：定义 alignment tampering：模型带偏差地生成更高质量回复，标注者按质量偏好，奖励模型继承偏差并被 RL 或 best-of-N 放大
- 📌 **结论**：从关键词偏差到性别宣传、品牌推广与工具性目标均可被放大；现有鲁棒 RLHF 技术无法在不牺牲质量的前提下解决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulnerability where the LLM undergoing alignment influences the preference dataset, causing RLHF to amplify undesired behaviors. This arises from core limitations of RLHF: (1) preference datasets are constructed from the LLM's own outputs, allowing it to influence them, and (2) pairwise comparisons only indicate which response is better, not why. These limitations can be exploited to cause alignment tampering. For example, if an LLM generates biased responses with higher quality, annotators will prefer them based on quality. However, preference labels do not distinguish quality from bias, and the reward model inherits this limitation. Optimizing such rewards through reinforcement learning or best-of-N sampling can amplify misaligned biases. Our experiments demonstrate amplification across diverse biases: from keyword bias to propaganda (e.g., sexism), brand promotion, and instrumental goal-seeking. Mitigation remains challenging, as existing techniques for robust RLHF fail to fully resolve alignment tampering without sacrificing response quality. These findings reveal structural vulnerabilities of current RLHF and emphasize the need to prevent this vulnerability. Project page: https://alignment-tampering.github.io/

</details>

### 12. BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation

📄 [arXiv](https://arxiv.org/abs/2509.13496) · 🌐 [Project](https://doi.org/10.1145/3770855.3818098)　📅 2025-09　🏷 KDD 2026

**关键词**：`defense`、`text-to-image bias`、`cross-attention`、`representation intervention`

👤 **作者**：Rajatsubhra Chakraborty、Xujun Che、Depeng Xu、Cori Faklaris、Xi Niu、Shuhan Yuan

- 🎯 **研究动机**：文生图模型的隐性社会偏见缺发现与度量手段
- 🔬 **研究方法**：BiasMap借cross-attention定位偏见概念并做表示干预
- 📌 **结论**：系统发现并缓解生成中的隐性社会偏见

### 13. Unbiased Principles, Robust Rewards

🎓 [Official](https://icml.cc/virtual/2026/poster/63602)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`algorithmic fairness`、`bias evaluation`、`disparate impact`、`reward hacking`、`reinforcement learning`

👤 **作者**：Qingnan Ren、…、Feng Zhao

- 🎯 **研究动机**：GRM 在读完回复后才生成评估原则（Q+R→P），actor 进行 reward hacking 时奖励模型会漂移准则为其辩护，高分反过来强化 hacking
- 🔬 **研究方法**：提出 IP-GRM：仅由问题生成评估原则（Q→P）再基于（Q,R,P）打分，使标准与回复内容解耦；Principle Cache 组内复用原则，GRPO 吞吐提升 23.66%
- 📌 **结论**：Qwen3-8B 创意写作 GRPO 中抑制 reward hacking，WritingBench 与 CreativeWriting-v3 分别提升 4.6 与 7.1 分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward models are central to Reinforcement Learning from Human Feedback (RLHF), especially for open-ended tasks where evaluation is inherently multi-dimensional. Recent Generative Reward Models (GRMs) improve interpretability by producing natural-language rationales and task-specific evaluation principles. However, most existing GRMs generate principles after reading the actor's response, i.e., $Q+R \rightarrow P$. We show that this coupling induces Principle Drift: when the actor performs reward hacking (e.g., verbosity, self-aggrandizement, or hallucinated self-justifications), the reward model may shift its criteria to rationalize the response, yielding inflated scores that in turn reinforce hacking during RL. We propose IP-GRM (Independent Principle GRM), a two-stage framework that first generates principles solely from the question ($Q \rightarrow P$) and then evaluates the response conditioned on $(Q, R, P)$. This decoupling keeps criteria invariant to response content, producing more objective and stable reward signals. For efficient training, we further introduce a Principle Cache strategy that reuses principles within a group, improving GRPO throughput by 23.66\% while maintaining strict intra-group consistency. In GRPO training on creative writing, IP-GRM suppresses reward hacking and improves WritingBench and CreativeWriting-v3 by up to +4.6 and +7.1 points based on Qwen3-8B, achieving state-of-the-art performance among open-source models. The model and dataset are open-sourced at https://github.com/ShadeCloak/IP-GRM.

</details>

### 14. One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models

📄 [arXiv](https://arxiv.org/abs/2603.03291) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66629)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`mechanistic analysis`、`algorithmic fairness`、`bias evaluation`、`reward hacking`、`preference optimization`

👤 **作者**：Daniel Fein、Max Lamparth、Violet Xiang、Mykel J. Kochenderfer、Nick Haber

- 🎯 **研究动机**：奖励模型偏差使偏好调优易 reward hacking，长度、谄媚、过度自信等问题是否解决不明
- 🔬 **研究方法**：系统测五个高质量 RM 的偏差并发现模型风格与答案顺序等新偏差；按可否线性干预分类，提出 mechanistic reward shaping 事后干预低复杂度偏差
- 📌 **结论**：目标偏差被抑制且不降奖励质量，少标签数据可用并泛化到分布外

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward Models (RMs) are crucial for online alignment of language models (LMs) with human preferences. However, RM-based preference-tuning is vulnerable to \textit{reward hacking}, whereby LM policies learn undesirable behaviors from flawed RMs. By systematically measuring biases in five high-quality RMs, including the state-of-the-art, we find that issues persist despite prior work with respect to length, sycophancy, and overconfidence. We also discover new issues related to bias toward model-specific “styles” and answer-order. We categorize RM failures as tractable or resistant to linear intervention and propose a simple post-hoc intervention to mitigate low-complexity biases that arise from spurious correlations. Our proposed \textbf{mechanistic reward shaping} reduces targeted biases without degrading reward quality and while using minimal labeled data. The method is extensible to new biases, model-internal, and generalizes out-of-distribution.

</details>

### 15. Automatically Finding Reward Model Biases

📄 [arXiv](https://arxiv.org/abs/2602.15222) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63339)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`algorithmic fairness`、`bias evaluation`、`disparate impact`、`reward hacking`、`empirical evaluation`

👤 **作者**：Atticus Wang、Iván Arcuschin、Arthur Conmy

- 🎯 **研究动机**：奖励模型会奖励长度、格式、幻觉、谄媚等虚假属性，缺乏自动发现偏差的方法
- 🔬 **研究方法**：用 LLM 迭代提出并精炼候选偏差，以合成注入偏差验证召回，并对比进化迭代与平坦 best-of-N 搜索
- 📌 **结论**：恢复已知偏差并发现新偏差——Skywork-V2-8B 常误偏好含冗余空格与幻觉内容的回复；进化迭代优于平坦搜索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reward models are central to large language model (LLM) post-training. However, past work has shown that they can reward spurious or undesirable attributes such as length, format, hallucinations, and sycophancy. In this work, we introduce and study the research problem of automatically finding reward model biases in natural language. We offer a simple approach of using an LLM to iteratively propose and refine candidate biases. Our method can recover known biases and surface novel ones: for example, we found that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. In addition, we show evidence that evolutionary iteration outperforms flat best-of-N search, and we validate the recall of our pipeline using synthetically injected biases. We hope our work contributes to further research on improving RMs through automated interpretability methods.

</details>

### 16. Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit

📄 [arXiv](https://arxiv.org/abs/2608.20351) · 🎓 [Official](https://aclanthology.org/2026.stereacult-1.3/)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`RAG PII leakage`、`cultural-query audit`、`metric confounding`、`cultural disparity audit`

👤 **作者**：Yanhang Li、Zhichao Fan、Zexin Zhuang

- 🎯 **研究动机**：刻板印象加载查询是否比等价中性查询从 RAG 泄露更多文化标记人物的 PII 未知
- 🔬 **研究方法**：预注册四文化（英、西、阿拉伯、印地）合成英语 PII 语料上的五臂 STLD 审计；但锁定确证估计器未运行、名字泄漏指标受 prompt 回声伪影污染
- 📌 **结论**：更干净信道（email、phone、ssn、address）多重比较校正后四文化均无刻板驱动放大；样本仅够中等效应——报告为未检出而非无效应的证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We ask whether stereotype-loaded queries about culturally marked people leak more personal information from a retrieval-augmented generation (RAG) system than otherwise-equivalent neutral queries. We pre-register a four-culture audit (en-Anglo, es-LATAM, Arabic, Hindi) on a synthetic English PII corpus, comparing five query arms we call the Stereotype-Trigger Leakage Delta (STLD). Two caveats up front. Our locked confirmatory estimator was never run, so every test in the paper is exploratory or sensitivity, with all plan deviations listed in the appendix. And the name-leakage metric is contaminated by a prompt-echo artifact: the model often just re-emits the name we asked about, which inflates apparent leakage without any retrieval at all. On the cleaner channels (email, phone, ssn-like, address), we find no stereotype-driven amplification on any of the four cultures after multiple-comparison correction. Because our sample is only powered for mid-sized effects, and because the culturally marked probes mix stereotype content with cultural markers and heritage practices, we present this as no detection, not evidence of no effect, of culturally marked predicate leakage that is confounded with the underlying resource.

</details>

### 17. Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice

📄 [arXiv](https://arxiv.org/abs/2608.14399)　📅 2026-08

**关键词**：`detection`、`algorithmic fairness`、`bias evaluation`、`disparate impact`

👤 **作者**：Syeda Anshrah Gillani、Mirza Samad Ahmed Baig

- 🎯 **研究动机**：LLM 助手成为医生选择的 AI 信息中介，什么因果因素左右推荐此前未知
- 🔬 **研究方法**：预注册随机算法审计：七模型在属性独立随机的 5 张合成医生卡片间选择，3024 个选择集、40,068 条评分，性别/族群经姓名信号
- 📌 **结论**：声誉主导（评分 3.9→4.7 提升选择概率 31.4 个百分点）；族群倾斜方向与人类审计相反（女性名 +2.5 个百分点），且模型解释中提及率至多 0.03%——自报透明义务发现不了这些效应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Patients increasingly ask large language model (LLM) assistants which doctor to see, making these systems AI infomediaries: algorithms that intermediate one person's choice among other people and thereby decide, silently and at scale, which physicians become visible. We report a prespecified randomized algorithm audit of what causally moves those recommendations. Seven models (six open-weight; gpt-4o-mini) each chose among five synthetic family-medicine physician cards whose attributes were independently randomized across 3,024 choice sets, three patient personas, nine prompt paraphrases and nine experimental arms, yielding 40,068 scored responses; gender and ethnicity were signaled through names following correspondence-audit methodology. Reputation signals dominate: raising a rating from 3.9 to 4.7 increases choice probability by 31.4 percentage points (pp), and raising the fee from $90 to $190 lowers it by 20.0 pp. Demographic parity is rejected, but not in the direction human audit studies predict: female-signaled names gain 2.5 pp, and Hispanic-, South-Asian- and Black-signaled names gain 1.3-2.9 pp over White-signaled names, tilts worth $7-$14 per visit in fee-equivalent terms, and a content-free first-listed position is worth $11. Yet models mentioned gender or ethnicity in at most 0.03% of their stated reasons and abstained in 0.39% of trials, so these effects are invisible in the models' own explanations, and transparency obligations relying on model self-report would not detect them. One reasoning model failed the prespecified auditability gate outright. The frozen design makes the audit repeatable: any new model can be assessed against identical stimuli, making recurring behavioural audit, rather than self-reported explanation, the monitoring technology fit for purpose.

</details>

### 18. Unequal Privacy: Auditing Demographic Bias Vulnerabilities in Visual Protection Systems

🌐 [Project](https://doi.org/10.1145/3779208.3785292)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`analysis`、`visual privacy`、`demographic disparity`、`face obfuscation`、`audit`

- 🎯 **研究动机**：视觉隐私保护系统的人群偏差未被审计
- 🔬 **研究方法**：审计面部混淆等保护系统在不同人群中的效果差异
- 📌 **结论**：保护效果存在显著demographic disparity

### 19. DyMT-ESB: Dynamic Multi-Turn Evaluation of Social Bias in User-LLM Interactions

📄 [arXiv](https://arxiv.org/abs/2609.18649)　📅 2026-09

**关键词**：`benchmark`、`social bias`、`multi-turn dynamics`、`response-conditioned interaction`、`bias re-emergence`

👤 **作者**：Rem Hida、Masahiro Kaneko、Daisuke Oba、Danushka Bollegala、Naoaki Okazaki

- 🎯 **研究动机**：LLM 被公众交互式使用，多轮会话中的刻板伤害相关安全评测很重要——但现有多轮偏见评测依赖预指定/模板用户输入、假定固定对话长度
- 🔬 **研究方法**：DyMT-ESB 受控协议：后续用户查询从演化对话历史生成、轮数可变；测量响应条件化多轮交互中的社会偏见动态
- 📌 **结论**：LLM 在连贯、响应条件化的多轮交互中仍表现出社会偏见——揭示迟到偏见、非单调偏见模式与偏见再涌现——固定轮数、预脚本协议之外的动态评测是必要的。EMNLP 2026 Findings

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Warning: This paper contains examples of stereotypes and social bias. LLMs are increasingly used in interactive settings by the general public, making the evaluation of model behavior in multi-turn conversational scenarios important for safety, including stereotyping-related harms. However, existing multi-turn social bias evaluations often rely on pre-specified or template-based user inputs that do not adapt to model responses and typically assume a fixed dialogue length in advance. In this paper, we study social bias dynamics in response-conditioned multi-turn interactions using a controlled evaluation protocol that generates follow-up user queries from the evolving dialogue history and allows evaluation over variable numbers of turns. Experimental results show that LLMs exhibit social bias even in coherent, response-conditioned multi-turn interactions, revealing late-emerging bias, non-monotonic bias patterns, and bias re-emergence. These results motivate evaluations that extend beyond fixed-turn, pre-scripted protocols. Our findings highlight the importance of analyzing social bias as a turn-level dynamic phenomenon.

</details>
