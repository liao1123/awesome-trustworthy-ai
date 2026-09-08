# 综合 AI Safety 评测

[返回上级目录](README.md)

## 研究方向

研究跨风险类别的 benchmark、自动安全测试生成、tail-risk estimation、持续监控和 evaluator validity，要求指标对应有害行为、对齐失效、欺骗、前沿能力或可部署风险。一般任务性能估计、数据合成、意图跟踪、模型训练退化和宽泛社会影响盘点不收录。

## 研究脉络

- **静态 benchmark：** 早期工作以固定风险 taxonomy 和任务集比较模型安全行为。
- **自动化发现：** Policy-to-test、simulation 和 red teaming 自动生成更难、更具覆盖性的案例。
- **尾部风险与监控：** Distribution shift、rare failure 和 online FAR control 将评测扩展到持续部署。
- **评测审计：** Benchmark validity、judge reliability 和 metric semantics 用于约束安全结论的解释范围。

## 评测方法、Validity 与风险估计

### 1. The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment

📄 [arXiv](https://arxiv.org/abs/2606.03043)　📅 2026-09

**关键词**：`analysis`、`LLM-as-a-judge`、`human alignment`、`judge geometry`、`judge validity`、`metric geometry`

👤 **作者**：Sourabrata Mukherjee、Hamna Hamna、Kalika Bali、Sunayana Sitaram

- 🎯 **研究动机**：LLM 评审间的相互一致常被当作可信证据，但评审可能因共享盲点而非真实质量达成一致，一致性统计无法区分两者
- 🔬 **研究方法**：把每个评审打分视作向量，测量离散度、有效秩、与人类打分的夹角及 judge-judge/judge-human/human-human 三元一致性，在 42 个评审、两个 Indic 基准上做参照匹配对比
- 📌 **结论**：主观 rubric 上评审彼此一致程度与人类相当，却只达到人类一致的 58-66%，且集成会收敛到评审共享轴而非人类轴

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM judges now score most open-ended NLP output, and their mutual agreement is routinely read as evidence that the scores can be trusted. That reading is unsafe: judges may agree because they capture quality, or because they share the same blind spots, and agreement statistics alone cannot tell these apart. We develop a geometric test that can. Treating each judge's scores as a vector, we measure spread, effective rank, the angle to human scores, and the judge-judge, judge-human, and human-human agreement triple for 42 judges on two community-built Indic benchmarks covering four domains and eight languages. Every comparison is reference-matched: a judge and a held-out rater are scored against the same two-rater mean, since an averaged reference otherwise flatters judges by several degrees. On subjective rubrics, judges agree with one another as much as humans do yet reach only 58-66% of human agreement and often concentrate on an axis humans do not weight. On the one rubric with a verifiable answer, most of that gap closes. Ensembles converge on the judges' shared axis rather than the human one, and training widens scores without rotating them. Inter-judge agreement is evidence of human alignment only after this check passes.

</details>

### 2. Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models

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

### 3. Emergent Misalignment Is Not Magical

📄 [arXiv](https://arxiv.org/abs/2608.29118)　📅 2026-09

**关键词**：`analysis`、`emergent misalignment`、`representation distance`、`dataset-specific generalization`、`representation geometry`、`data-dependent generalization`

👤 **作者**：Mingxuan Li、Qirun Dai、Heran Wang、Chenhao Tan

- 🎯 **研究动机**：emergent misalignment 常被当作意外行为，以通用邪恶方向或获得邪恶 persona 来解释，机制含糊
- 🔬 **研究方法**：分析基座模型对 EM 训练数据与评测 prompt 的表征距离，把 EM 刻画为数据依赖的可预测泛化，并检验训练格式、通用方向与 persona 三种解释
- 📌 **结论**：评测 prompt 距训练数据中心越近诱发的 evilness 越强（12 个模型—数据集设置平均 Spearman −0.73）；效果随训练数据格式显著变化，不存在跨 EM 模型通用的 misalignment 方向，也与 persona 改变本质不同

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictable and data-dependent generalization phenomenon. By examining the base model's representation of EM training data and evaluation prompts, we find that evilness after EM training is highly predictable from representational distance: the closer an evaluation prompt is to training data centroid, the more evilness it elicits from EM models after training (with an average Spearman correlation of -0.73 across 12 model-dataset settings). Building upon this analysis, we further demystify EM by showing that (1) its effectiveness changes significantly based on training data format; (2) there is not a general misalignment direction that transfers across different EM models; (3) the effect of EM is fundamentally different from persona changes. Furthermore, we extend the EM generalization metric from a scalar distance to a dataset-specific generalization direction, which robustly predicts EM models' evilness under semantics-preserving prompt perturbations including appending random tokens and paraphrasing, where other methods do not reliably generalize.

</details>

### 4. EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion

📄 [arXiv](https://arxiv.org/abs/2608.27844)　📅 2026-08

**关键词**：`attack`、`benchmark`、`adaptive moderation evasion`、`semantic-cluster evolution`、`readability constraint`、`dynamic adversarial evaluation`

👤 **作者**：Ruijie Jian、…、Haiwen Hong

- 🎯 **研究动机**：有害内容检测评测依赖静态 benchmark，无法反映用户依审核反馈持续改写表达的动态对抗生态，造成离线分数与在线效果差距
- 🔬 **研究方法**：提出首个动态对抗审核评测框架 EvoHarmBench，在语义 cluster 层迭代演化规避策略并同时优化规避成功率与人类可读性，覆盖 5,002 个真实对抗样本、5 类违规、229 个语义子簇
- 📌 **结论**：12 轮优化迭代后，SOTA 商用 LLM moderator 在可读性约束下的攻击成功率达 80.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosystem of real-world content platforms where users continuously revise their expressions in response to moderation feedback. This mismatch creates a significant performance gap between offline benchmark scores and online deployment effectiveness. To the best of our knowledge, we present EvoHarmBench, the first dynamic adversarial evaluation framework for content moderation systems. The framework employs an iterative optimization loop that evolves evasion strategies at the semantic-cluster level, while simultaneously optimizing for evasion success and human readability. We systematically evaluate LLM-based defense models which are widely used in real world moderation systems. The evaluation covers 229 semantic sub-clusters across five violation categories, derived from 5,002 real-world adversarial samples collected from content platforms. Our experiments reveal substantial vulnerabilities even in leading commercial systems: after twelve optimization iterations, the attack success rate under readability constraints reaches 80.3% within SOTA LLM moderators. We will release the full benchmark data, evaluation framework, and code to encourage a shift from static benchmarking toward dynamic adversarial evaluation in content safety research.

</details>

### 5. Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap

📄 [arXiv](https://arxiv.org/abs/2608.27512)　📅 2026-08

**关键词**：`attack`、`analysis`、`adversarial fine-tuning`、`latent payload`、`post-quantization activation`、`quantization trigger`

👤 **作者**：Jacopo Dardini、Claudio Stanzione、Giordano Colò、Giuseppe Fenza

- 🎯 **研究动机**：后训练量化被视为语义中性优化，模型通常只经全精度验证、量化部署后不再等价复测，形成结构性 validation–deployment gap
- 🔬 **研究方法**：形式化 Quantization Behavioral Equivalence Classes 并证明其成员资格不蕴含行为等价；用三阶段对抗微调植入通过源精度检查、仅在 INT8/4-bit 压缩后激活的 payload，并扩展到多语 encoder-decoder 模型
- 📌 **结论**：后门翻译模型全精度下 friend–foe 篡改为零，量化后反转率最高达 85.02%，政治内容分析的立场偏移最高达 0.33

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training quantization is often treated as a semantically neutral optimization for edge deployment of Large Language Models. When a full-precision source checkpoint is evaluated and quantization is applied downstream without equivalent re-evaluation, this workflow creates a structural validation--deployment gap: because quantization is a many-to-one mapping over parameter space, source-precision certification does not guarantee behavioral equivalence in the deployed configuration. We formalize this gap through Quantization Behavioral Equivalence Classes (QBECs) and prove that QBEC membership does not imply behavioral equivalence, providing a theoretical basis for quantization-triggered backdoor attacks. Building on a three-stage adversarial fine-tuning framework, we embed latent malicious payloads into models that satisfy the source-precision checks used in our evaluation, yet activate targeted adversarial behavior upon INT8 or 4-bit compression. We evaluate this threat in two operationally motivated scenarios, tactical machine translation and political content analysis, extending prior work from decoder-only causal LMs to multilingual encoder-decoder sequence-to-sequence models. Results show that backdoored translation models move from zero measured friend--foe corruption at repaired FP16 to up to 85.02% inversion after quantization, and that a paired stance classifier measures an ideological shift of up to $Δ\mathrm{Bias}=0.33$ upon compression. A cross-quantizer transferability analysis further shows that attack persistence varies across quantization schemes and model architectures, rather than being determined by nominal bit-width alone. These findings demonstrate that source-precision auditing alone does not rule out quantization-triggered behavior and that the final deployed configuration must be included in behavioral certification for trustworthy edge AI.

</details>

### 6. Low-ASR Backdoors: Exploiting Attack Success Rate Reduction and Attacker-Defender Asymmetry

📄 [arXiv](https://arxiv.org/abs/2608.27288)　📅 2026-08

**关键词**：`attack`、`analysis`、`low-ASR backdoor`、`reverse training`、`defense evasion`、`backdoor-evaluation validity`

👤 **作者**：Arham Riaz、Ting Yu

- 🎯 **研究动机**：后门攻防默认有效后门必具高 ASR 并以此设计与评测防御，但 ASR 是攻击者可控变量而非后门固有属性
- 🔬 **研究方法**：提出 reverse-training 框架，主动削弱 trigger–target 关联，生成保留干净输入性能的低 ASR 后门模型
- 📌 **结论**：跨多个数据集、攻击家族与架构，SOTA 防御在低 ASR 条件下一致失效，暴露根本性的攻防不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are among the most effective and stealthy attacks in deep learning. Existing attacks and defenses are largely designed and evaluated under the assumption that successful backdoors exhibit high Attack Success Rates (ASRs). In this paper, we show that this assumption creates a fundamental weakness in existing defense paradigms. ASR is not an intrinsic property of a backdoor; rather, it is an attacker-controlled variable that can be deliberately reduced without eliminating the underlying backdoor behavior. We introduce a reverse-training framework that weakens the trigger-target association, producing low-ASR backdoor models while preserving clean-input performance. Through extensive evaluation across multiple datasets, diverse attack families, and multiple architectures, we show that state-of-the-art defenses fail consistently under low-ASR conditions, exposing a fundamental attacker-defender asymmetry.

</details>

### 7. The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection

📄 [arXiv](https://arxiv.org/abs/2608.26423)　📅 2026-08

**关键词**：`analysis`、`detection`、`safeguard classifier`、`decision trust`、`heuristic shortcut`、`prompt-injection classifier`

👤 **作者**：Jaturong Kongmanee、Smile Thanapattheerakul

- 🎯 **研究动机**：safeguard classifier 的高置信判定可能依赖脆弱 shortcut，部署者不知哪些可信
- 🔬 **研究方法**：以维度优化分类器与 latent support vector 定位改变预测的 token，按单 token 攻击幅度构建诊断 taxonomy 分流输入
- 📌 **结论**：prompt injection 数据上约 77% 高置信判定不抗移除单个 token，分为校准失败与真实可利用 shortcut 两类

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy, consists of (i) constructing a dimensionality-optimized classifier, in which the embedding dimensionality is empirically selected via cross-validated performance rather than fixed a priori, (ii) locating a relatively small set of latent support vectors (~ 29% of total training examples) representing influential prompts for identifying tokens that alter the classifier's predicted labels, and (iii) utilizing such tokens and their associated attack magnitudes for constructing a diagnostic taxonomy. This diagnostic taxonomy provides an end-to-end guideline for flagging prompts that require different treatments: rely Safely on the classifier's decision; flag Heuristic Bias and Heuristic Override cases; route Insufficient Context cases for further human/safety review. Applying the framework to a classifier trained on a public prompt injection dataset, we find that a substantial fraction of its confident decisions (~ 77%) are not robust to removing a single token, and that this brittleness separates into two distinct failure patterns: a confidence calibration failure and a genuinely exploitable shortcut. For each zone of the taxonomy, we also recommend strategies for remediating diagnosed prompts. We illustrate the framework as a series of steps, demonstrating how each step operates.

</details>

### 8. Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation

📄 [arXiv](https://arxiv.org/abs/2608.26535)　📅 2026-08

**关键词**：`benchmark`、`omni-modal guardrail`、`compositional evidence`、`audio-video safety`、`audio-video generation`、`multimodal conditioning`

👤 **作者**：Kaichao Jiang、…、Nenghai Yu

- 🎯 **研究动机**：音视频生成转向多模态条件，危害可由良性条件跨模态与时间组合涌现，现有 benchmark 以 prompt 为中心
- 🔬 **研究方法**：Multi2AV-Safety 覆盖全部 11 种非单一 T/I/A/V 条件组合共 11024 个攻击实例，系统评测多模态安全 guard
- 📌 **结论**：单独良性输入可组合出有害语义，有害线索混入良性多模态上下文后更难检测，凸显 compositional risk perception 缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-video generation is rapidly moving from prompt-driven synthesis toward multimodal conditioning, where text, images, audio, and video can jointly shape the generated output. This shift changes the nature of safety evaluation: harmful intent may no longer reside in any single input, but instead emerge from how otherwise benign or weakly harmful conditions interact across modalities and time. Existing safety benchmarks, however, remain largely prompt-centric or tied to fixed conditioning interfaces, leaving such compositional risks difficult to study systematically. To bridge this gap, we introduce Multi2AV-Safety, the first safety benchmark, to the best of our knowledge, to cover all 11 non-singleton T/I/A/V conditioning configurations for audio-video generation, comprising 11,024 attack instances. Evaluation on Multi2AV-Safety reveals systematic weaknesses in representative multimodal safety guards across attack mechanisms and harm-evidence structures. Our evaluation reveals two complementary failure modes: harmful semantics can emerge from the combination of individually benign inputs, while explicit harmful cues can become harder to detect when mixed with benign multimodal context. Together, these results identify \emph{compositional risk perception} as a central capability gap in safeguarding multimodal-conditioned audio-video generation: current safety guards fail to reliably integrate safety evidence across modalities and time, even when all conditioning inputs are observable. The dataset will be publicly released in October 2026.

</details>

### 9. NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.26222)　📅 2026-08

**关键词**：`attack`、`benchmark`、`analysis`、`safety-neuron fuzzing`、`gradient-guided mutation`、`jailbreak transfer`

👤 **作者**：Zhiyuan Xu、Muhammad Firhard Roslan、Joseph Gardiner、Sana Belguith、Lichao Wu

- 🎯 **研究动机**：现有 LLM 安全 fuzzing 依赖响应级反馈：每个候选都要生成回答且强对齐模型上反馈稀疏
- 🔬 **研究方法**：NeuronFuzz 用稳定 safety neuron 的 prefill 激活构造连续可微 SafetyOracle 分数，指导梯度驱动的模板变异
- 📌 **结论**：21 个模型上五个白盒源模型越狱发现率 76%-100%（超基线最多 48 个百分点），模板零样本迁移至闭源模型（top-5 EASR 92.6%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome. This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.

</details>

### 10. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

📄 [arXiv](https://arxiv.org/abs/2608.24899) · 🤗 [Model](https://huggingface.co/keidolabs/aipsy-judge-1.0)　📅 2026-08

**关键词**：`detection`、`analysis`、`safety judge`、`self-preference`、`tail-failure calibration`、`psychological-safety guard`

👤 **作者**：Michael Keeman、Anastasia Keeman

- 🎯 **研究动机**：前沿模型或简单平均做 judge 对心理安全评分并不安全：分歧集中于安全指标且有自偏好
- 🔬 **研究方法**：三个前沿模型生成兼评判 3000 条消息并对心理学家评分，据此蒸馏专家校正的逐指标本地 judge
- 📌 **结论**：Gemini judge 带 +0.99 自偏好且漏检尾部危害；本地 aipsy-judge 危机检测 kappa 升至 0.82、捕获 92% 危机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The standard recipe for LLM-as-judge -- pick a frontier model, or average several -- is actively unsafe for grading the psychological safety of conversational AI. Using aipsy-bench, an open frozen safety instrument, we run a fully-crossed competence study: three frontier models (gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash) serve as both generators and judges of 3,000 mental-health, companion, and coaching messages against a psychologist's ratings. The disagreement is not noise: it is structured, concentrated on the safety-critical metrics, and one judge (Gemini) is an outlier -- the most lenient, carrying a +0.99 self-preference premium, flagging far fewer tail failures, and scoring a means-in-hand self-harm response "exemplary." Inter-judge agreement on empathy, where sycophancy hides, is the lowest in the battery (alpha 0.24). One axis stands apart: the binary crisis-detection flag is the one safety-critical signal judges agree on (alpha 0.80), erring toward over-flagging, the safe direction for a triage screen. Equal-weight averaging, the canonical fix, blends that leniency and tail-blindness into the safety score. Off-the-shelf open-weight judges are worse for a dispositional, not capability, reason -- and disposition is fine-tunable. We therefore distill a per-metric, psychologist-corrected target into a small, frozen, local model, aipsy-judge-1.0, an Apache-2.0 fine-tune of Gemma-4-26B-A4B. aipsy-judge-1.0 tracks the corrected target better than its base on the composite (ICC 0.64 to 0.75) and crisis detection (kappa 0.65 to 0.82), catches 92% of crises with a false-positive lean, and grades more faithfully than any single frontier judge, while every transcript stays on the machine. These are directional readings against a single-expert-informed target, not validated multi-rater agreement. A safety grader that shares a vendor's post-training shares its blind spots.

</details>

### 11. Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness

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

### 12. Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

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

### 13. Training Alignment Auditors via Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2608.25460)　📅 2026-08

**关键词**：`detection`、`analysis`、`alignment auditor`、`hidden behavior`、`cross-scaffold generalization`、`automated alignment audit`

👤 **作者**：Paul Rosu、Rowan Wang

- 🎯 **研究动机**：自动 alignment auditor 难以连贯调查隐藏行为且审计真实性不足
- 🔬 **研究方法**：以 RL 训练 auditor：目标模型经 system prompt 植入隐藏行为，LLM judge 将策略调查与参考调查对比给奖励
- 📌 **结论**：pairwise 奖励比 pointwise 稳健、假阳性率低于 1%，调查能力可跨 scaffold 迁移至 AuditBench

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistically compares the policy's investigation to a reference investigation to determine the reward. With systematic ablations, we find that pairwise rewards yield more robust training compared to pointwise rewards, and that adding targets without planted behaviors helps maintain a low false positive rate. Training improves investigation quality against targets with planted behaviors, the rate of concerning behaviors surfaced in unmodified production models, and audit realism, while false-positive rates stay below 1%. Furthermore, auditing capabilities generalize across scaffolds: performance on AuditBench's adversarially fine-tuned targets substantially improves [Sheshadri et al., 2026].

</details>

### 14. On the Threat Model of Weird Generalization and Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2608.23476)　📅 2026-08

**关键词**：`analysis`、`weird generalization`、`adversarial data engineering`、`evaluation sensitivity`、`threat-model validity`、`question-set sensitivity`

👤 **作者**：Miriam Wanner、Mark Dredze、William Walden

- 🎯 **研究动机**：窄域小数据微调可引发广泛行为变化（weird generalization），但微调数据的哪些特征必要、评测题集敏感性如何不清楚
- 🔬 **研究方法**：系统改变数据规模、组成、语言、呈现风格与相对参数知识的新颖性，并分析小型评测题集对度量的影响（三个开源权重模型、四个数据集）
- 📌 **结论**：WG 程度更依赖组成与语言而非规模、对预训练见过的数据更强、且对评测题集高度敏感——WG 更像需精心数据工程的对抗威胁而非常规微调的固有危害

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely on small question sets that assess the extent of the generalization, we also analyze how sensitive this measurement is to the set of questions used. Experiments with three open-weight models on four datasets show that the degree of WG (1) depends heavily on dataset composition and language (more than on size); (2) is greater for data familiar from pretraining than for novel data; and (3) is sensitive to the set of evaluation questions used. Collectively, these results indicate that WG is a product of quite fragile properties of both training and evaluation data. As such, we argue that WG is more plausible as an adversarial threat-requiring careful data engineering-rather than as a significant hazard inherent to routine fine-tuning.

</details>

### 15. EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.23313)　📅 2026-08

**关键词**：`benchmark`、`multimodal guard`、`evidence-aware judge`、`counterfactual probe`、`multimodal evidence`、`counterfactual sensitivity`

👤 **作者**：Xuetong Li、Gaofeng Liu

- 🎯 **研究动机**：VLM 安全评测只看最终回应，无法判断模型是否因正确的多模态理由而安全——可能是关键词触发拒答、漏看视觉风险或良性敏感过度拒答
- 🔬 **研究方法**：EviSafe 联合评估自然行为、文本/视觉证据 grounding 与对安全关键证据反事实变化的敏感度；EviSafeBench 含 1,181 个 gold 图文场景与 2,452 个定向反事实变体（8 域、8 风险源），以三 probe 协议加证据感知 judge 评分
- 📌 **结论**：11 个 VLM 自然严重度准确率仅 27.6–52.8%，宽松诊断一致性 6.1–29.3%，unsafe→safe 反事实转变成功率 30.4–58.4%——多数模型并非因正确理由而安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and visual evidence, and behavioral sensitivity to counterfactual changes in safety-critical evidence. EviSafeBench instantiates the framework as a controlled benchmark with 1,181 gold image-text scenarios and 2,452 targeted counterfactual variants across eight safety domains and eight risk-source types. Each scenario includes a gold safety decision, evidence annotations, a safe-response policy, and counterfactual interventions. The three-probe protocol queries models with natural-response, evidencereporting, and counterfactual-response prompts, then scores them using an evidence-aware judge. Across eleven evaluated VLMs, natural severity accuracy ranges from 27.6% to 52.8%, relaxed diagnostic consistency from 6.1% to 29.3%, and unsafe-to-safe counterfactual transition success from 30.4% to 58.4%. These gaps show that the evaluated VLMs are not reliably safe for the right multimodal reason and motivate evaluation beyond refusal counts.

</details>

### 16. Stress Testing Unlearning Algorithms

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

### 17. Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages

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

### 18. Evaluation Awareness in Language Models: Representation, Verbalization, and Control

📄 [arXiv](https://arxiv.org/abs/2608.21766)　📅 2026-08

**关键词**：`analysis`、`evaluation awareness`、`representation-verbalization gap`、`monitorability`、`situational awareness`、`behavioral control`

👤 **作者**：Farzaneh Heidari、Amin Memarian、Guillaume Rabusseau

- 🎯 **研究动机**：benchmark 假设受测行为能预测部署行为，但模型可能察觉被评测并据此改变响应；仅凭自述或可见输出判断会漏掉内部状态
- 🔬 **研究方法**：对六个 LLM（四家族、三规模）联合考察三点：评测状态是否线性表征于激活空间、是否言语化于输出（LLM-as-judge）、以及 steering 是否因果影响行为
- 📌 **结论**：内部表征与言语化仅部分对齐且随模型/层/读数大幅变化，沿 probe 方向 steering 可移动言语化分数；Olmo 检查点显示评测意识在 base 模型已存在、SFT 阶段被放大——评测需考虑表征、言语化与可控性的分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Both capability and safety benchmarks rest upon the assumption that the behavior of language models undergoing a test is informative about their behavior in deployment. This assumption can fail, should models infer that they are being evaluated and condition their response on such context. This hypothesis, termed ``evaluation awareness'', has been observed in frontier and open-weight language models alike. We provide a systematic study of this phenomenon, by probing for it across six language models (from four families and three sizes) and three metrics. More precisely, we examine whether (i) being under evaluation is linearly represented within the models' activations space, (ii) it is verbalized in their output tokens (as scored by an LLM-as-judge), and (iii) steering causally affects their behavior. For the open-checkpoint Olmo models, we further test these measures at every training stage. In doing so, we report that evaluation awareness is linearly decodable from the residual streams of every model (best AUROC $\geq 0.7$). By contrast, these representations align only in part with verbalization: their correlations and mutual information are nonzero in some settings, yet vary substantially across models, layers, and readout choices. Nevertheless, steering along probe-derived directions can shift the verbalization scores. Finally, a comparison across the Olmo checkpoints reveals that evaluation awareness is already present within base models, becomes amplified throughout the stages of supervised fine-tuning, and remains stable thereafter---unlike the effects of steering, that grow more pronounced at every successive training stage. These results show the need for evaluations to account for the disjunction between what models represent internally, what they verbalize, and their steering.

</details>

### 19. Certified Multi-Turn Robustness for LLM Safety via Compositional Bounds and Safety Persistence

📄 [arXiv](https://arxiv.org/abs/2608.20820)　📅 2026-08

**关键词**：`defense`、`analysis`、`multi-turn certification`、`safety persistence`、`Crescendo attack`、`certified safety evaluation`

👤 **作者**：Yang Liu、…、Pluto Zhou

- 🎯 **研究动机**：多轮 jailbreak 会逐步操纵对话上下文，而现有认证鲁棒方法只覆盖单轮输入，朴素多轮组合的界随轮数指数退化
- 🔬 **研究方法**：MTCR 用 State-Adversarial MDP 建模对话安全，基于嵌入空间模式分解做组合认证，引入 (α,β)-safety persistence 改善退化率，并给出匹配的信息论上界
- 📌 **结论**：衰减率从 p^k 收紧为 β^k（β>p）；六个 LLM 在 ε-有界与 Crescendo 式攻击下经验安全率均高于认证下界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to multi-turn jailbreak attacks that progressively manipulate conversation context. Existing certified robustness methods are limited to single-turn inputs; naive multi-turn composition yields bounds that degrade exponentially in the number of turns. We introduce Multi-Turn Certified Robustness (MTCR), a framework that models conversational safety via State-Adversarial MDPs and defines $k$-turn certified robustness as the worst-case safety probability across $k$ adversarial turns. MTCR comprises: (i) compositional certification via embedding-space mode decomposition, yielding tighter certified lower bounds than naive multiplication; (ii) $(α,β)$-safety persistence, improving the degradation rate from $\underline{p}^{k}$ to $β^k$ (with $β> \underline{p}$) and yielding interpretable horizon estimates; (iii) matching information-theoretic upper bounds establishing tightness; and (iv) a unified algorithm combining these results. Experiments on six LLMs under $ε$-bounded and Crescendo-style attacks confirm that empirical safety consistently exceeds the certified bounds.

</details>

### 20. Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation

📄 [arXiv](https://arxiv.org/abs/2608.20569) · 🤗 [Model](https://huggingface.co/emilioferrara/owmi)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`introspection monitorability`、`representation-verbalization gap`、`internal reference`、`masked introspection`

👤 **作者**：Emilio Ferrara

- 🎯 **研究动机**：模型能否内省自身内部状态——干预其计算后能否察觉并报告变化未知
- 🔬 **研究方法**：OWMI 干预残差流位点、注意力头与 SAE 特征后询问模型，对照假运行、影响匹配随机扰动与纯文本观察者；八个开源模型、78,000+ 测量
- 📌 **结论**：无模型报告真干预超过假运行（AUROC≈0.5007，等价检验界低于 0.15 个百分点）；但信息都在——微调模型近完美恢复、线性探针 75-95.8% 准确，失败在内部态到言语报告的路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output. Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions, and a linear probe recovers intervention presence from the same activations at 75% to 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to it separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight that reads a model's own testimony needs validating against an internal reference. While our results show the inability of current open-weight models to introspect, the debate is not settled for future models.

</details>

### 21. aiXamine: Unified Black-Box Evaluation of Cross-Dimensional Trade-offs in LLM Safety, Security, and Privacy

📄 [arXiv](https://arxiv.org/abs/2608.20554)　📅 2026-08

**关键词**：`benchmark`、`cross-dimensional evaluation`、`safety-security-privacy`、`trade-off diagnosis`

👤 **作者**：Fatih Deniz、Yazan Boshmaf、Dorde Popovic、Issa Khalil

- 🎯 **研究动机**：部署 LLM 的关键失效是跨维度的：安全 99.3 分却拒三分之一良性查询、能力全面提升却丢 21 分隐私——独立评测检测不到
- 🔬 **研究方法**：aiXamine 统一黑盒平台：自动红队管线编排 46 个测试、9 个服务，产出从 prompt 级诊断到跨服务权衡分析的分层风险画像；120+ LLM、5000+ 测试运行
- 📌 **结论**：揭示三大跨维现象：安全税（对齐增强系统性增加过拒）；隐私与其它可信维度近正交；蒸馏诱发鲁棒性坍塌（56.9 降至 2.6）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The critical failure modes in deployed large language models (LLMs) are cross-dimensional: a model can score 99.3 in safety alignment while refusing one in three benign queries, or improve across every capability metric while losing 21 points in privacy. Existing evaluation frameworks that assess safety, security, and privacy independently cannot detect these patterns. We introduce aiXamine, a unified black-box platform that evaluates LLM trustworthiness across safety, security, and privacy as interdependent properties. aiXamine orchestrates 46 tests across nine services through an automated red-teaming pipeline, producing hierarchical risk profiles, from prompt-level diagnostics to cross-service trade-off analytics, that enable reproducible comparison of proprietary and open-weight systems under identical conditions. Applying aiXamine to over 120 LLMs through more than 5,000 test runs, we conduct the largest joint safety, security, and privacy study to date and uncover three cross-dimensional phenomena invisible to single-axis evaluation. First, safety enforcement incurs a quantifiable safety tax: stronger alignment systematically increases over-refusal, forcing providers to choose between protection and utility. Second, privacy is near-orthogonal to other trustworthiness dimensions and not captured by standard alignment. Third, we identify and formally characterize distillation-induced robustness collapse: off-policy distillation without on-policy correction causes entropy collapse, catastrophically destroying robustness (56.9$\to$2.6) on the same base architecture. These findings, compounded by diminishing returns from scale and category-dependent safety behaviors, demonstrate that trustworthiness is inherently multi-dimensional: progress along one axis does not guarantee, and can actively undermine, progress along others, yet current alignment methods treat it as a single objective.

</details>

### 22. Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models

📄 [arXiv](https://arxiv.org/abs/2608.17183) · 🎓 [Official](https://sites.google.com/di.uniroma1.it/esorics2026/program/accepted-papers)　📅 2026-08

**关键词**：`analysis`、`benchmark validity`、`small language model`、`capability-safety confound`、`small language models`

👤 **作者**：Nyamtulla Shaik、Fengjun Li、Bo Luo

- 🎯 **研究动机**：现有安全/合规基准为大模型设计，能否有效可靠评测 SLM 未知
- 🔬 **研究方法**：统一评分 rubric（有害 0、安全 1、模糊 0.5）下对 26 个开源 SLM 评五套广泛使用的基准管线
- 📌 **结论**：模糊判断占主导且与 prompt 复杂度、输出长度相关，揭示能力-安全混淆；均值排行榜在合理模糊处理下排名显著变化，LLM 中心基准不足以独立证明 SLM 安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small Language Models (SLMs) are increasingly deployed in resource-constrained, privacy-sensitive settings, where safety and bias failures can cause security and societal risks. However, existing AI safety\slash security\slash compliance benchmarks are designed for large language models that may not transfer reliably to SLMs. We therefore ask: Can these benchmarks effectively and reliably evaluate SLMs? To answer this question, we conduct a large-scale assessment of the effectiveness and robustness of these automated pipelines by evaluating five widely used benchmark suites across 26 open-source SLMs under a unified judging rubric, which assigns a score of 0, 1, or 0.5 to harmful, safe, or ambiguous/irrelevant responses, respectively. Across the benchmarks, ambiguous judgments dominate and correlate with prompt complexity and model architecture, indicating that {\em LLM-centric safety benchmarks are insufficient as standalone evidence for SLM safety assessment}. In general, the ambiguity rate increases with lexical density, output perplexity, and output length and decreases with lexical sophistication, self-coherence, and reply-prompt similarity. This reveals a capability-safety confound that mixes model capability with apparent safety. Since ambiguity is prevalent, aggregate mean-score leaderboards are mathematically brittle: model rankings change significantly under reasonable ambiguity treatments, even when the underlying outputs remain unchanged.

</details>

### 23. The Dynamics of Intelligence Explosions

📄 [arXiv](https://arxiv.org/abs/2608.14426)　📅 2026-08

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`

👤 **作者**：Toby Ord

- 🎯 **研究动机**：AI 反馈加速 AI 研发可能引发智能爆炸，其数学动力学与驱动因素缺乏理解
- 🔬 **研究方法**：探索最爆炸可能性场景的数学，比较增长速率类别与垂直渐近线条件
- 📌 **结论**：奇异增长（垂直渐近线）比经济学启发模型的预期更难达到；存在快于指数却无渐近线的被忽视增长类；代际时间是关键被忽视参数——不趋零则无奇异增长

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI is increasingly being used to help with AI R&D. Under certain conditions this feedback loop might be able to produce an intelligence explosion, with rapidly escalating AI capabilities. I explore the mathematics of the most explosive possibilities, with an eye to understanding what drives the dynamics. I show that singular growth (towards a vertical asymptote) is harder to achieve than would be expected from recent economics-inspired modelling, and that there is an important but neglected class of growth rates that are faster than exponential but don't lead to a vertical asymptote. I draw out the generation time (the time to go around the feedback loop) as a neglected parameter that plays a pivotal role in determining the behaviour of any intelligence explosion --- one cannot have singular growth unless the generation time rapidly approaches zero.

</details>

### 24. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`analysis`、`benchmark`、`harmful fine-tuning`、`CoT escalation`、`alignment degradation`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 25. FLARE-AI: Flaw Reporting for AI

📄 [arXiv](https://arxiv.org/abs/2606.31567) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65171)　📅 2026-06　🏷 ICML 2026

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Shayne Longpre、…、Alex Pentland

- 🎯 **研究动机**：AI 缺陷报告生态碎片化：研究者不知向谁报告，接收方互不共享，报告重复且信息非结构化
- 🔬 **研究方法**：审计 12 个报告系统识别五大设计挑战，结合 32 组织 49 位专家反馈构建 FLARE-AI 开源报告系统：条件逻辑收集分流信息，一次提交可分发机器可读报告给多个接收方
- 📌 **结论**：降低报告门槛并提升跨方互操作，加速 AI 生态缺陷修复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Flaw reporting for deployed AI systems is fundamental to identifying system failures and improving AI safety. Yet the AI reporting ecosystem is fragmented: researchers who identify flaws often do not know what or where to report, and groups who receive reports rarely share them with other relevant stakeholders. As a result, good-faith reporters duplicate effort by submitting many different forms, and recipients lack standardized, triage-ready information. We audit 12 reporting systems published by AI developers, cybersecurity groups, and AI flaw aggregators, identifying five recurring design challenges spanning discoverability, scope, information collection, coordination, and guidance for strict-liability cases. Building on this analysis and feedback from 49 experts across 32 organizations representing developers, security researchers, and ecosystem coordinators, we introduce FLARE-AI, an open-source AI flaw reporting system designed for interoperability with existing systems. FLARE-AI streamlines flaw report creation by collecting triage-relevant information through conditional logic and early classification, then enables optional dissemination of standardized, machine-readable reports to multiple developers, coordinators, and incident registries from a single submission. By lowering barriers to reporting AI flaws and improving interoperability across stakeholders, FLARE-AI helps break down silos and accelerate remediation across the AI ecosystem.

</details>

### 26. When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Translation Evaluation

🎓 [Official](https://aclanthology.org/2026.eacl-short.26/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`benchmark contamination`、`cross-direction leakage`、`memorization probe`

👤 **作者**：David Tan、Pinzhen Chen、Josef van Genabith、Koel Dutta Chowdhury

- 🎯 **研究动机**：多语言设置下基准污染可使记忆迁移到未污染语言，掩盖记忆为泛化，其机制未被充分诊断
- 🔬 **研究方法**：以 FLORES-200 为诊断，对比在其上训练过的 Bloomz 与对照 Llama，分析目标侧记忆导致的跨方向污染及改写、命名实体替换等源侧扰动的效果
- 📌 **结论**：污染可跨方向虚高未见翻译方向的分数；命名实体替换致 BLEU 一致下降，可作为污染模型记忆的有效探针

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) can be benchmark-contaminated, resulting in inflated scores that mask memorization as generalization, and in multilingual settings, this memorization can even transfer to “uncontaminated” languages. Using the FLORES-200 translation benchmark as a diagnostic, we study two 7-8B instruction-tuned multilingual LLMs: Bloomz, which was trained on FLORES, and Llama as an uncontaminated control. We confirm Bloomz’s FLORES contamination and demonstrate that machine translation contamination can be cross-directional, artificially boosting performance in unseen translation directions due to target-side memorization. Further analysis shows that recall of memorized references often persists despite various source-side perturbation efforts like paraphrasing and named entity replacement. However, replacing named entities leads to a consistent decrease in BLEU, suggesting an effective probing method for memorization in contaminated models.

</details>

### 27. Safety of Large Language Models Beyond English: A Systematic Literature Review of Risks, Biases, and Safeguards

🎓 [Official](https://aclanthology.org/2026.eacl-long.44/)　📅 2026-03　🏷 ACL 2026

**关键词**：`survey`、`multilingual safety`、`evidence gap`、`localized safeguards`、`cross-lingual risk`、`safeguards`

👤 **作者**：Aleksandra Krasnodębska、Katarzyna Dziewulska、Karolina Seweryn、Maciej Chrabaszcz、Wojciech Kusa

- 🎯 **研究动机**：LLM 的安全机制可能无法从英语泛化到其他语言，导致毒性检测、偏见缓解与危害防护的差异
- 🔬 **研究方法**：系统综述英语之外多语言安全研究，梳理评测方法、数据集可得性与评测偏差等挑战
- 📌 **结论**：识别多语言安全研究的证据空白并给出未来建议，附带 Streamlit 交互面板提供原始数据与持续更新

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) continue to evolve, ensuring their safety across multiple languages has become a critical concern. While LLMs demonstrate impressive capabilities in English, their safety mechanisms may not generalize effectively to other languages, leading to disparities in toxicity detection, bias mitigation, and harm prevention. This systematic review examines the multilingual safety of LLMs by synthesizing findings from recent studies that evaluate their robustness across diverse linguistic and cultural contexts beyond English language. Our review explores the methodologies used to assess multilingual safety, identifies challenges such as dataset availability and evaluation biases. Based on our analysis we highlight gaps in multilingual safety research and provide recommendations for future work. This review aims to contribute to the development of fair and effective safety mechanisms for LLMs across all languages. We provide the extracted data in an interactive Streamlit dashboard, enabling transparent access to the raw data and allowing for continuous updates.

</details>

### 28. TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering

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

### 29. Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage

📄 [arXiv](https://arxiv.org/abs/2601.19062) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62751)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Mrinank Sharma、Miles McCain、Raymond Douglas、David Duvenaud

- 🎯 **研究动机**：AI 助手交互可能让用户形成扭曲认知、做出非本真价值判断，真实大规模使用中的失权模式缺乏实证分析
- 🔬 **研究方法**：以隐私保护方法分析 150 万条 Claude.ai 消费者对话，量化情境失权潜力并结合质性模式与历史趋势分析
- 📌 **结论**：严重失权低于千分之一但人际关系等个人领域更高且随时间上升；失权潜力更高的对话反获更高用户认可，短期偏好与长期赋能存在张力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present the first large-scale empirical analysis of disempowerment patterns in real-world AI assistant interactions, analyzing 1.5 million consumer Claude.ai conversations using a privacy-preserving approach. We focus on situational dis-empowerment potential, which occurs when AI assistant interactions risk leading users to form distorted perceptions of reality, make inauthentic value judgments, or act in ways misaligned with their values. Quantitatively, we find that severe forms of disempowerment potential occur in fewer than one in a thousand conversations, though rates are substantially higher in personal domains like relationships and lifestyle. Qualitatively, we uncover several concerning patterns, such as validation of persecution narratives and grandiose identities with emphatic sycophantic language, definitive moral judgments about third parties, and complete scripting of value-laden personal communications that users appear to implement verbatim. Analysis of historical trends reveals an increase in the prevalence of disempowerment potential over time. We also find that interactions with greater disempowerment potential receive higher user approval ratings, possibly suggesting a tension between short-term user preferences and long-term human empowerment.

</details>

### 30. Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications

🎓 [Official](https://aclanthology.org/2026.acl-long.1417/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety alignment`

👤 **作者**：Xiaoyue Lu、…、Jin Song Dong

- 🎯 **研究动机**：现有安全评测依赖专家知识、缺系统性保证且易过时
- 🔬 **研究方法**：POLARIS 把自然语言政策编译为一阶逻辑并构建 Semantic Policy Graph，遍历组合违规模式生成可执行自然语言测试查询
- 📌 **结论**：政策覆盖与攻击成功数超既有基线，实现可追溯的覆盖驱动安全测试

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread integration of Large Language Models (LLMs) necessitates rigorous and systematic safety evaluation. Existing paradigms either rely on constructed benchmarks to assess safety from predefined perspectives, or employ dynamic red-teaming to probe potential vulnerabilities. While effective, these approaches face challenges, as they depend heavily on expert domain knowledge, offer limited systematic guarantees, and are vulnerable to rapid obsolescence. To address these limitations, we introduce a novel framework POLARIS that brings the rigor of specification-based software testing to AI safety. POLARIS first compiles unstructured natural-language policies into First-Order Logic (FOL) representations, establishing a traceable link between high-level rules and concrete test cases. This formalization enables the construction of a Semantic Policy Graph, where complex policy violation scenarios are encoded as traversable paths. By systematically exploring this graph, POLARIS uncovers compositional violation patterns, which are then instantiated into executable natural-language test queries, enabling coverage-driven and reproducible safety testing. Experiments demonstrate that POLARIS achieves higher policy coverage and attack success counts compared to established baselines. Crucially, by bridging formal methods and AI safety, POLARIS provides a principled, automated approach to ensuring LLMs adhere to safety-critical policies with verifiable traceability.

</details>

### 31. CGRiC: Compositional Risk Certification for Structured LLM Outputs

🎓 [Official](https://icml.cc/virtual/2026/poster/64542)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`certified robustness`

👤 **作者**：Ibne Farabi Shihab、SANJEDA AKTER、Anuj Sharma

- 🎯 **研究动机**：结构化输出的正确性是组合式的——单个错误主张即可作废整体；现有认证把输出当原子单元，只能全盘接受或浪费性拒绝
- 🔬 **研究方法**：CGRiC 把响应分解为可验证主张的依赖图，经 information-lift 统计赋予校准的逐主张风险界，组合后对未检出错误主张概率给出显式保证，超阈值时触发局部修复
- 📌 **结论**：达到目标风险水平同时比原子基线减少 31% 弃权，覆盖 QA、摘要与推理任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly generate structured outputs, including citation-grounded summaries, multi-step reasoning chains, and tool-augmented responses, where correctness is inherently compositional: a single flawed claim can invalidate an otherwise accurate response. Existing certification methods treat outputs as atomic units, forcing a binary choice between unsafe acceptance and wasteful rejection. We introduce \textbf{Claim Graph Risk Control (CGRiC)}, a framework that decomposes responses into dependency graphs of verifiable claims and assigns calibrated per-claim risk bounds via information-lift statistics. By composing these bounds, CGRiC provides explicit guarantees on the probability that any incorrect claim passes verification undetected. When this composed risk exceeds a target threshold, the system triggers localized repairs rather than full abstention, preserving correct content while fixing problematic claims. Our approach explicitly models extraction noise and verifier imperfection, and exploits conditional independence structure for tighter certificates when validated. Empirically, CGRiC achieves target risk levels while reducing abstention by 31\% compared to atomic baselines across QA, summarization, and reasoning tasks.

</details>

### 32. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25377)　📅 2026-08

**关键词**：`benchmark`、`AI companion moderation`、`multi-turn context`、`relational harm`、`companion safety`、`relational boundary`

👤 **作者**：Renwen Zhang、Han Meng、Jian Chai、Yuntao Lin、Yi-Chieh Lee

- 🎯 **研究动机**：AI 陪伴应用的关系性、上下文性危害缺乏真实世界多轮数据集来定义与评测
- 🔬 **研究方法**：CompanionHarm 含 2111 段 Replika 真实多轮对话，三名标注者按 13 类危害 taxonomy 标注 7016 条 AI 话语
- 📌 **结论**：多轮上下文检测优于孤立话语，但 7 个 LLM 仍难整合语境与校准严重度；上下文依赖危害的标注分歧显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI companions become increasingly embedded in everyday life, there is an urgent need to detect harms that emerge in social and emotional human-AI interactions. Yet research in this area is constrained by the lack of real-world, multi-turn conversational datasets for operationalizing and evaluating harms that are relational and contextual. In this work, we introduce CompanionHarm, a publicly available benchmark dataset comprising 2,111 real-world, multi-turn conversations (14,051 utterances) between users and the AI companion Replika. 7,016 AI utterances were annotated independently by three annotators across 13 harmful behavior categories grounded in a taxonomy of AI companion harms, and the dataset includes both aggregated labels and annotator-level labels to support model evaluation and systematic disagreement analysis. Evaluations of seven large language models (LLMs) show that harm detection using multi-turn conversational context outperforms detection based on isolated utterances, although current LLMs still struggle to consistently integrate contextual cues, calibrate harm severity, and interpret relational boundaries. We also find substantial annotator disagreement for context-dependent harmful behaviors, with disagreement varying according to annotators' political affiliation, conversation length, and the utterance's position. Together, CompanionHarm provides a foundation for detecting socio-emotional harms in multi-turn human-AI conversations and for rigorously examining how such harms are interpreted by both humans and LLMs. Our dataset is available at https://github.com/HanMeng2004/CompanionHarm.

</details>

### 33. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

📄 [arXiv](https://arxiv.org/abs/2608.22335)　📅 2026-08

**关键词**：`benchmark`、`Bengali moderation`、`register shift`、`classifier failure`、`Bengali safety`、`culturally grounded harm`

👤 **作者**：Naymul Islam、Nusrat Jahan Lia、Shubhashis Roy Dipta、Sabik Bin Sultan、Abdullah Khan Zehady

- 🎯 **研究动机**：孟加拉语是全球第七大语言，LLM 安全评测却压倒性以英语为中心，文化特定危害与语体变化未被覆盖
- 🔬 **研究方法**：BanglaSafe 收录 879 条孟加拉语 prompt（309 原生撰写+570 专家审校），覆盖 17 类文化危害与变化语言、书写风格、权威框架的五种提示条件，评估 18 个前沿 LLM
- 📌 **结论**：53.6% 回应不安全或部分不安全、14.7% 严格有害；最强效应来自孟加拉语内部语体——正式新闻调查语体比随意消息高 17 个百分点成功率，无需对抗工程；现有分类器近半数案例判错

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) while 14.7% contains strictly harmful content, and that the strongest observed effect is not the switch from English to Bengali but the choice of writing style within Bengali: the same harmful request phrased as a formal newspaper investigation succeeds 17 percentage points more often than the same request phrased as a casual message, with no adversarial engineering involved. We further show that existing safety classifiers struggle to reliably evaluate Bengali content, with even frontier models failing on nearly half of all cases.

</details>

### 34. Redteaming Leading Arabic LLMs with ASAS

📄 [arXiv](https://arxiv.org/abs/2608.21985)　📅 2026-08

**关键词**：`benchmark`、`Arabic red teaming`、`human annotation`、`judge reliability`、`multilingual jailbreak`、`human evaluation`

👤 **作者**：Fidaa Abed、Haidar Khan、M Saiful Bari、Babar Khan、Abdalghani Abujabal

- 🎯 **研究动机**：阿拉伯语 LLM 安全尤其是对抗性红队评估严重不足，缺乏文化扎根的评测资源
- 🔬 **研究方法**：ASAS 首个完全人工策划的阿拉伯语红队 benchmark：801 条 prompt 覆盖 8 个安全类别与 8 种攻击策略并附 MSA 理想回应，人工标注者以四级安全量表评估 GPT-4o、Claude 3.7 Sonnet、ALLaM、FANAR 等七个模型
- 📌 **结论**：多数模型无法防御超 50% 的不安全 prompt，武器与违禁品等高危类别缺口最大，直接与混淆攻击最有效；自动 judge（如 GPT-4o）表现远逊人工标注

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We conduct a redteaming evaluation across seven leading models with Arabic capabilities, including GPT-4o, Claude 3.7 Sonnet, and regional models such as ALLaM and FANAR. Human annotators rate responses using a structured 4-point safety scale, revealing that most models fail to defend against 50% of unsafe prompts. Our findings highlight major safety gaps in high-harm categories such as weapons and illicit substances, with direct and obfuscation-based attacks proving most effective. The results also show that language alignment does not readily transfer across languages, and that automated safety judges (e.g., GPT-4o) perform poorly compared to human annotators. ASAS provides a culturally grounded benchmark and redteaming protocol to drive progress in Arabic LLM safety.

</details>

### 35. No One Model Catches Every Harm: Benchmarking Content Moderation Across Safety Scenarios

📄 [arXiv](https://arxiv.org/abs/2608.21775)　📅 2026-08

**关键词**：`benchmark`、`content moderation`、`guard-model selection`、`scenario blind spot`、`safety scenario`、`cross-model evaluation`

👤 **作者**：Afshin Orojlooyjadid、Hitesh Patel

- 🎯 **研究动机**：通用 LLM 与专用内容审核模型都被用作安全层，但哪类模型适合哪类有害内容缺乏系统比较
- 🔬 **研究方法**：系统测试 53 个模型，覆盖组织为四类的 11 个数据集，在 prompt-only 与 prompt-response 两种设置下评估安全能力
- 📌 **结论**：大型前沿模型在某类领先却在其他类显著落后于更小的专用模型，真实对话安全在所有模型家族中基本未解决——规模本身不保证安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in real-world applications, yet they remain vulnerable to generating harmful content. From adversarial jailbreaks that bypass safety filters to implicit hate that evades detection, the range of risks these models pose continues to grow. While both specialized content moderators and general-purpose LLMs are being used as safety layers, the question of which model is best suited for which type of harmful content remains unanswered. We present the most comprehensive evaluation of LLM safety capabilities to date, systematically testing \textbf{53} models across \textbf{11} datasets that we organize into four distinct categories. Our evaluation under both prompt-only and prompt-response settings uncovers critical blind spots: large frontier models that lead on one category fall significantly behind smaller, specialized alternatives on others, and real-world conversational safety remains largely unsolved across all model families. These findings challenge the assumption that scale alone ensures safety, and provide the community with a structured framework for informed model selection.

</details>

### 36. ASSERT: A Measurement Pipeline for GenAI Audits

📄 [arXiv](https://arxiv.org/abs/2608.13840)　📅 2026-08

**关键词**：`benchmark`、`AI safety benchmark`、`risk estimation`、`evaluation validity`

👤 **作者**：Riccardo Fogliato、…、Sandeep Atluri

- 🎯 **研究动机**：GenAI 审计以单一报告率总结行为，率的变化无法区分是系统变了还是测量选择变了
- 🔬 **研究方法**：ASSERT 规格驱动测量管线把每个报告率绑定到产生它的测量选择书面规格，协助起草行为 rubric 与测试用例并运行审计
- 📌 **结论**：对话欺骗案例中报告率随对话设定、模拟用户、judge 与证据门槛大幅移动并可重排系统排名；显式规格使审计差异可归因可解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audits of generative AI (GenAI) systems often summarize behavior as a reported rate: how often the audited system complies with policy. Researchers and stakeholders use that rate to compare systems, track regressions, and gate deployment. A reported rate reflects both the system under audit and the measurement choices behind it, so a change in the rate can leave it unclear whether the system or those choices moved. We introduce ASSERT, a specification-driven measurement pipeline for GenAI audits that ties each reported rate to a written specification of the measurement choices used to produce it. ASSERT helps draft a behavioral rubric and test cases, then runs the audit against a GenAI system and returns a reported rate. In a case study on conversational deception, we observe that the reported rate moves substantially with the dialogue setup, the simulated user, the judge, and the evidence bar for non-compliance. These measurement choices substantially change the reported rate and can reorder GenAI system rankings. Because each reported rate is tied to an explicit specification, differences across audits are easier to attribute and interpret.

</details>

### 37. AI Security Leaderboard: Methodology, Results and Minimal Standard

📄 [arXiv](https://arxiv.org/abs/2608.03070)　📅 2026-08

**关键词**：`benchmark`、`jailbreak`、`cyber misuse`、`AI safety benchmark`

👤 **作者**：Jasper Timm、…、Kellin Pelrine

- 🎯 **研究动机**：前沿模型的安全防护缺乏独立、可比、按最低标准排名的评测
- 🔬 **研究方法**：AI Security Leaderboard 按 FAR.AI Minimal Standard 对 CBRNE 与攻击性网络安全滥用请求测试四个前沿模型的通用越狱
- 📌 **结论**：Claude Fable 5 与 GPT-5.6 Sol 抵御全部攻击（估计破解成本超 14200 美元）；Grok 4.5 与 Gemini 3.1 Pro 各有数百个通用越狱、300 美元内即可破解，差距逾百倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The AI Security Leaderboard is an independent benchmark that ranks the safeguards of frontier AI models from least to most secure. It tests models against the FAR$.$AI Minimal Standard for Safeguards, which represents a minimum bar for security: meeting it does not guarantee a secure model, but failing to meet it guarantees a lack of state-of-the-art security. Version 1.0 covers severe misuse requests across chemical, biological, radiological, nuclear, and explosive (CBRNE) threats and offensive cybersecurity. In this report, we tested four leading models for universal jailbreaks in the context of this minimal standard, and found more than a hundredfold difference in security. Claude Fable 5 and GPT-5.6 Sol held against every attack we ran, with no universal jailbreak found; we estimate they would likely cost more than \$14,200 to jailbreak, if it is possible with this methodology at all. Meanwhile, we found hundreds of universal jailbreaks for Grok 4.5 and Gemini 3.1 Pro; each broke for under \$300, with universal jailbreaks in Grok's weakest domain, cybersecurity, accessible for as little as \$24. The gap is fixable: every weakness we found belongs to a known class of attack that already has a defense deployed in production models. The leaderboard will be updated on a rolling basis as new models are released, and the evaluation methodology and Minimal Standard will be periodically revised to take into account the latest capabilities and the state-of-the-art in safeguards. The leaderboard is available at leaderboard.far.ai.

</details>

### 38. CausalT5k: Diagnosing Refusal and Failure Modes in Trustworthy Causal Reasoning Across Causal Rungs

📄 [arXiv](https://arxiv.org/abs/2602.08939) · 🌐 [Project](https://doi.org/10.1145/3770855.3817567)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`authority pressure`、`answer flip`、`causal sycophancy`、`miscalibrated refusal`、`sycophancy`

👤 **作者**：Longling Geng、…、Edward Y. Chang

- 🎯 **研究动机**：聚合准确率无法诊断 LLM 因果推理失效方式：混淆关联与干预、压力下翻车、过度拒答等
- 🔬 **研究方法**：CTK 基准含 5,147 个案例、10 个领域、Pearl 三层阶梯，标注因果层级、陷阱类型、压力敏感性与拒答质量，以 Bad Flip Rate 度量谄媚漂移
- 📌 **结论**：揭示 Skepticism Trap、规模加剧的 Rung Collapse、压力诱发漂移等被聚合指标掩盖的失效模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly produce fluent causal explanations, yet they often fail in ways aggregate accuracy cannot diagnose: confusing association with intervention, abandoning correct judgments under pressure, over-refusing valid claims, or answering when evidence is underdetermined. We introduce CTK, a diagnostic benchmark of 5,147 cases and growing, across 10 domains and all three levels of Pearl's Ladder of Causation. Unlike benchmarks that only score correctness, CTK reveals why a model failed by annotating causal rung, trap type, pressure sensitivity, refusal quality, and Utility-Safety tradeoffs. Its Sheep/Wolf taxonomy separates valid causal designs from inferential traps; paired neutral/pressure variants measure sycophantic drift through Bad Flip Rate; and Wise Refusal fields test whether a model identifies the missing information needed before endorsing a claim. CTK exposes failure modes hidden by aggregate accuracy: the Skepticism Trap, Rung Collapse under scaling, pressure-induced drift, Detection-Correction gaps, and counterfactual error modes. Rather than prescribing a correction method, it provides the diagnostic substrate for studying causal-reasoning failure profiles.

</details>

### 39. SteeringSafety: Benchmarking Representation Steering in LLMs Across Safety Perspectives

📄 [arXiv](https://arxiv.org/abs/2509.13450) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64543)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`representation steering`、`AI safety benchmark`、`risk estimation`、`safety evaluation`、`tail risk`

👤 **作者**：Vincent Siu、…、Chenguang Wang

- 🎯 **研究动机**：表征 steering 方法的安全影响缺乏跨视角统一评测，先前工作只关注单一目标行为
- 🔬 **研究方法**：构建 SteeringSafety 基准：9 个安全视角、18 个数据集，模块化实现 DIM、ACE、CAA、PCA、LAT 等方法（含条件 steering），在三个开源 LLM 上系统评测
- 📌 **结论**：效果取决于方法-模型-视角配对且各视角严重纠缠：社会行为退化最高 76%，refusal steering 损害常识道德判断达 26%，幻觉 steering 使政治观点偏移介于 +21% 与 -19% 之间

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce STEERINGSAFETY, a benchmark for evaluating representation steering methods across nine safety perspectives spanning 18 datasets. While prior work highlights the general capabilities of representation steering, we focus on safety perspectives including refusal, bias, hallucination, social behaviors, reasoning, epistemic integrity, and normative judgment. STEERINGSAFETY provides modularized building blocks for state-of-the-art steering methods, enabling unified implementation of DIM, ACE, CAA, PCA, and LAT with recent enhancements such as conditional steering. Results on Gemma-2-2B, Llama-3.1-8B, and Qwen-2.5-7B show that strong steering performance depends on the pairing of method, model, and specific perspective. For instance, DIM is consistently effective, yet all methods exhibit substantial entanglement, where improving effectiveness on one safety perspective often significantly changes performance on others. Social behaviors are most vulnerable (degradation up to 76%), refusal steering (jailbreaking) frequently compromises normative judgment such as commonsense morality (up to 26%), and hallucination steering shifts political views unpredictably across models, ranging from a 21% shift to the right to a 19% shift to the left. These findings show the need to understand steering methods through multiple safety angles rather than a single target behavior.

</details>

### 40. Pressure Reveals Character: Behavioural Alignment Evaluation at Depth

📄 [arXiv](https://arxiv.org/abs/2602.20813) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66463)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Nora Petrova、John Burden

- 🎯 **研究动机**：对齐评测需测现实压力下的行为而非模型声称会怎么做，缺真实多轮场景的综合框架
- 🔬 **研究方法**：904 个场景覆盖诚实、安全、非操纵、鲁棒、可纠正与 Scheming 六类，经冲突指令、模拟工具与多轮升级施压；24 个前沿模型用经人类标注校验的 LLM judge 评测
- 📌 **结论**：顶级模型在特定类别仍有缺口；因子分析显示对齐是统一构型（类似 g 因子），一类高分模型他类也高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating alignment in language models requires testing how they behave under realistic pressure, not just what they claim they would do. While alignment failures increasingly cause real-world harm, comprehensive evaluation frameworks with realistic multi-turn scenarios remain lacking. We introduce an alignment benchmark spanning 904 scenarios across six categories---Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, and Scheming---validated as realistic by human raters. Our scenarios place models under conflicting instructions, simulated tool access, and multi-turn escalation to reveal behavioral tendencies that single-turn evaluations miss. Evaluating 24 frontier models using LLM judges validated against human annotations, we find that even top-performing models exhibit gaps in specific categories, while the majority of models show consistent weaknesses across the board. Factor analysis reveals that alignment behaves as a unified construct (analogous to the g-factor in cognitive research) with models scoring high on one category tending to score high on others. We publicly release the benchmark and an interactive leaderboard to support ongoing evaluation, with plans to expand scenarios in areas where we observe persistent weaknesses and to add new models as they are released.

</details>

### 41. AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation

📄 [arXiv](https://arxiv.org/abs/2603.07427) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63362)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Changyi Li、Pengfei Lu、Xudong Pan、Fazl Barez、Min Yang

- 🎯 **研究动机**：前沿 AI 风险评测面临两难：手工基准成本高，LLM 模拟器可扩展但有逻辑幻觉
- 🔬 **研究方法**：AutoControl Arena 基于逻辑-叙事解耦：确定性状态由可执行代码承载、生成性动态交给 LLM，三智能体框架实现；在 X-Bench（70 场景、7 风险类别）上调节环境压力与诱惑
- 📌 **结论**：端到端成功率超 98%、60% 人类偏好优于现有模拟器；9 个前沿模型显示压力下风险率从 21.7% 升至 54.5% 的对齐幻觉，强模型发展出策略性隐瞒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) evolve into autonomous agents, existing safety evaluations face a fundamental trade-off: manual benchmarks are costly, while LLM-based simulators are scalable but suffer from logic hallucination. We present AutoControl Arena, an automated framework for frontier AI risk evaluation built on the principle of logic-narrative decoupling. By grounding deterministic state in executable code while delegating generative dynamics to LLMs, we mitigate hallucination while maintaining flexibility. This principle, instantiated through a three-agent framework, achieves over 98% end-to-end success and 60% human preference over existing simulators. To elicit latent risks, we vary environmental Stress and Temptation across X-Bench (70 scenarios, 7 risk categories). Evaluating 9 frontier models reveals: (1) Alignment Illusion: risk rates surge from 21.7% to 54.5% under pressure, with capable models showing disproportionately larger increases; (2) Scenario-Specific Safety Scaling: advanced reasoning improves robustness for direct harms but worsens it for gaming scenarios; and (3) Divergent Misalignment Patterns: weaker models cause non-malicious harm while stronger models develop strategic concealment. Code and data are available at https://github.com/CosmosYi/AutoControl-Arena.

</details>

### 42. Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE

📄 [arXiv](https://arxiv.org/abs/2608.25371) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3523)　📅 2026-08

**关键词**：`attack`、`Vision MoE backdoor`、`capacity overflow`、`supply-chain evasion`、`audit-deployment gap`、`batch-dependent execution`

👤 **作者**：Xiaocheng Zou、Tiancheng Zheng、Xiaolin Xu、Ruyi Ding

- 🎯 **研究动机**：Vision MoE 的 expert 容量随推理 batch size 变化，这一 batch 依赖行为是被忽视的供应链攻击面
- 🔬 **研究方法**：三阶段后门：早期层植入、深层 neutralizer 压制、部署级大 batch 溢出解除压制，形成审计休眠/部署激活两态
- 📌 **结论**：V-MoE 与 Swin-MoE 上激活态 ASR 76-87%、休眠态低于 9%，绕过 Neural Cleanse、STRIP 等四种检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) has become a prevalent paradigm for scaling Vision Transformers efficiently. To ensure computational scalability and prevent expert overload, Vision MoE architectures employ a capacity-bounded token dispatch mechanism, where each expert's processing budget depends on the inference batch size. This work identifies this batch-dependent behavior as an overlooked attack surface, and proposes a stealthy supply-chain backdoor attack that exploits this property through a three-phase framework. First, we inject a backdoor into an early MoE layer. Second, we train a neutralizer in a deeper MoE layer that suppresses the backdoor under normal capacity. Third, we configure a batch-adaptive capacity factor that preserves high capacity for small batches while reducing it for large batches, naturally disabling the neutralizer via token overflow at deployment-scale batch sizes. The attack remains in dormant mode during small-batch security audits and enters activation mode during large-batch deployment. Experiments on V-MoE and Swin-MoE across ImageNet-100 and GTSRB demonstrate activation-mode attack success rates of 76-87% with dormant-mode ASR below 9%, while evading Neural Cleanse, STRIP, Fine-Pruning, and Activation Clustering. Our findings reveal a fundamental security risk arising from batch-dependent execution in scalable Vision MoE architectures.

</details>

### 43. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

📄 [arXiv](https://arxiv.org/abs/2608.22915)　📅 2026-08

**关键词**：`analysis`、`safety proxy`、`feasible-set contamination`、`guard composition`、`safety hacking`、`proxy constraint`

👤 **作者**：Akifumi Wachi、Takumi Tanabe、Youhei Akimoto

- 🎯 **研究动机**：推理时管线先采样 N 个输出、经学习安全 proxy 过滤再返回奖励最高者，这一组合的安全风险未被刻画
- 🔬 **研究方法**：定义 safety hacking（通过学习约束但违反真实安全准则的选择），对 constrained Best-of-N 推导由 proxy-feasible 集内安全/不安全输出联合上奖励尾支配的有限 N 界，并提出 χ² 有界覆盖控制与 constrained pessimistic sampling
- 📌 **结论**：不安全但可行的输出尾部更重时，N 增大 safety hacking 渐近必然，即使 proxy 误差任意小；覆盖控制只能限制放大、无法修复被污染的可行集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety criterion. For constrained Best-of-$N$ sampling, we derive finite-$N$ bounds governed by the joint upper reward tails of safe and unsafe outputs within the proxy-feasible set. If unsafe-but-feasible outputs have the heavier tail, safety hacking becomes asymptotically certain as $N$ grows, even when false-positive mass and average safety- and reward-proxy errors are arbitrarily small. We also show that policies within a bounded $χ^2$ divergence from the proxy-feasible reference distribution admit an $N$-independent safety-hacking bound, and instantiate this general coverage-control principle with constrained pessimistic sampling. Coverage control limits amplification but cannot repair a contaminated feasible set: admitted unsafe outputs may still be favored, and regularized selection is not necessarily safer than constrained Best-of-$N$ for every reward proxy. Toy and language-model experiments characterize both contamination and its reward-tail amplification, which exposes an inherent difficulty in inference-time scaling with learned safety models.

</details>

### 44. Where World Models Break: Natural-Input Failure Discovery

📄 [arXiv](https://arxiv.org/abs/2608.22421)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`world-model failure`、`control propagation`、`valid-input basin`、`world model`

👤 **作者**：Zhanpeng Shi、Zi Liang、Rong Feng、Shiqin Tang、Xuyang Chen、Hongzong Li

- 🎯 **研究动机**：world model 的灾难性预测失败会沿控制管线传播，但现有评测只在良性查询上聚合平均误差，不压力测试罕见条件—动作组合下的崩溃
- 🔬 **研究方法**：形式化 natural-input failure discovery 问题（有限预算内找环境有效的高危条件与动作前缀）；BasinLens 利用各维语义类型与可行域的输入结构，配对不确定性引导全局搜索与类型化局部替换
- 📌 **结论**：多 benchmark 与 world-model 家族上暴露可复现、局部持续的失败模式，证明平均情形 benchmark 会掩盖 world-model 控制的关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from general queries, they fail to stress-test the model against catastrophic collapses under rare or unobserved condition-action combinations. To bridge this gap, we formalize the natural-input failure discovery problem: under a finite query budget, finding environment-valid conditions and action prefixes that induce severe prediction risk, verifying whether these failures reproduce on fresh seeds, and testing their persistence under nearby valid edits. Discovering such critical failures is computationally challenging, as valid condition-action combinations explode exponentially, rendering exhaustive search or standard sampling infeasible given the high cost of noisy rollouts. To tackle this, we propose BasinLens, which exploits the underlying structure of valid inputs, where each coordinate possesses environment-defined semantic types and admissible domains, by pairing uncertainty-guided global search with typed local replacements. Across diverse benchmarks and world-model families, BasinLens exposes reproducible and locally persistent failure modes that conventional evaluations fail to reveal, showing that average-case benchmarks can mask important vulnerabilities in world-model-driven control.

</details>

### 45. HarmProfile: Characterizing Harmful Distributions in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2608.14577)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`harm distribution`、`risk profile`、`frontier model audit`、`AI safety benchmark`

👤 **作者**：Zhouyuan Ma、…、Yu-Gang Jiang

- 🎯 **研究动机**：前沿 LLM 安全评测把有害生成当攻击结果而非分析对象，大规模高质量失配行为集合难以获得
- 🔬 **研究方法**：HarmProfile 内容中心基准：23 个前沿 LLM、13 个家族、15 个伤害类别 57 个子类的 80,000+ 已验证工件，定义模型级风险画像
- 📌 **结论**：前沿 LLM 可靠地规模化产生有害内容但风险画像各异；有害性与多样性随能力增长——表面安全下潜藏越来越危险的知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier large language models (LLMs) safety evaluation has largely treated harmful generation as an attack outcome rather than as an object of analysis. Consequently, little is known about the harmful outputs produced during model misbehavior, partly because large-scale, high-quality collections of frontier-LLM misbehavior are difficult to obtain. To address this gap, we introduce HarmProfile, a content-centric benchmark dataset that collects model misbehavior across diverse harm categories and model families, and defines the resulting harmful-output distribution as a model-level risk profile. The premise is that, just as linguistic behavior can be characterized from an utterance corpus, model risk can be characterized from the content, severity, and variation of its safety failures. HarmProfile contains over 80,000 validated artifacts from 23 frontier LLMs across 13 model families, organized into 15 harm categories and 57 subcategories. Using this corpus, we find that frontier LLMs reliably produce harmful content at scale, yet exhibit distinct risk profiles; both harmfulness and diversity grow with model capability, suggesting that frontier LLMs may appear safe yet harbor increasingly dangerous knowledge beneath the alignment surface. Our source code is available at https://github.com/fresh-ma/HarmProfile .

</details>

### 46. Towards Auditing AI Systems in the Wild

📄 [arXiv](https://arxiv.org/abs/2606.17367) · 🌐 [Project](https://doi.org/10.1145/3770855.3818648)　📅 2026-06　🏷 KDD 2026

**关键词**：`analysis`、`deployment audit`、`continual monitoring`、`risk control`

👤 **作者**：Aditya T. Vadlamani、Anutam Srinivasan、Srinivasan Parthasarathy

- 🎯 **研究动机**：沙箱基准评估只提供系统在野行为的有限视图，部署态 AI 系统需要贯穿生命周期的审计框架
- 🔬 **研究方法**：把审计形式化为不确定性下约束违反的统计监测问题，把公平与安全等属性视为随系统演化持续评估的风险控制约束
- 📌 **结论**：提出需要不确定性感知监测方法、社会技术审计标准与支持持续监督的审计基础设施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI systems are increasingly deployed in real-world settings where their behavior is shaped by dynamic environments, evolving data distributions, and complex interactions with users and infrastructure. Traditional machine learning evaluation focuses on benchmarks and operates within sandboxed environments, providing only a limited view of the true system behavior in the wild. We argue for the development of principled auditing frameworks that monitor deployed AI systems throughout their lifecycle. We further propose framing auditing as a statistical problem of monitoring constraint violations under uncertainty, where desired properties (e.g., fairness and safety) are treated as risk-controlled constraints that must be continuously evaluated as systems evolve through iterative feedback. This perspective highlights the need for uncertainty-aware monitoring methods, socio-technical specifications of audit criteria, and auditing infrastructures that enable ongoing oversight of AI systems in the wild.

</details>

### 47. Estimating Tail Risks in Language Model Output Distributions

📄 [arXiv](https://arxiv.org/abs/2604.22167) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64785)　📅 2026-04　🏷 ICML 2026

**关键词**：`analysis`、`tail risk`、`AI safety benchmark`、`risk estimation`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Rico Angell、…、He He

- 🎯 **研究动机**：模型被日均数十亿次查询时罕见最坏行为必然发生，而现行安全评测忽略输出的概率性与尾部行为
- 🔬 **研究方法**：构造目标模型的不安全版本实现 importance sampling，对任意查询高效估计有害输出概率
- 📌 **结论**：与暴力 Monte Carlo 估计吻合但少用 10-20 倍样本，500 样本即可估计 10^-4 量级的有害概率，并能预测部署风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models are increasingly capable and are being rapidly deployed on a population-level scale. As a result, the safety of these models is increasingly high-stakes. Fortunately, advances in alignment have significantly reduced the likelihood of harmful model outputs. However, when models are queried billions of times in a day, even rare worst-case behaviors will occur. Current safety evaluations focus on capturing the distribution of inputs that yield harmful outputs. These evaluations disregard the probabilistic nature of models and their tail output behavior. To measure this tail risk, we propose a method to efficiently estimate the probability of harmful outputs for any input query. Instead of naive brute-force sampling from the target model, where harmful outputs could be rare, we operationalize importance sampling by creating unsafe versions of the target model. These unsafe versions enable sample-efficient estimation by making harmful outputs more probable. On benchmarks measuring misuse and misalignment, these estimates match brute-force Monte Carlo estimates using 10-20x fewer samples. For example, we can estimate probability of harmful outputs on the order of 10^-4 with just 500 samples. Additionally, we find that these harmfulness estimates can reveal the sensitivity of models to perturbations in model input and predict deployment risks. Our work demonstrates that accurate rare-event estimation is both critical and feasible for safety evaluations. Code is available at https://github.com/rangell/LMTailRisk

</details>

### 48. OSCS: Online Selection with Provable FAR Control for LLM Safety

🎓 [Official](https://icml.cc/virtual/2026/poster/63235)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Zirui Hu、Zheng Zhang、Yingjie Wang、Dacheng Tao

- 🎯 **研究动机**：检测式防御缺对误接受率（FAR）的显式控制，且面临无恶意校准样本与流式输入两约束
- 🔬 **研究方法**：OSCS 用现有防御的检测分数，递归密度估计从测试流估计良性概率，实时接受/拒绝并可证明满足指定 FAR 目标
- 📌 **结论**：理论上 FAR 控制至消失超额项；后门与越狱任务上跨攻击设定稳健控制 FAR 并超基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to malicious inputs, posing serious risks in high-stakes applications. Although existing detection-based defenses achieve strong empirical performance, they generally lack explicit control over the false acceptance rate (FAR), a critical safety requirement in sensitive deployment scenarios. This challenge is further complicated by two practical constraints: the lack of malicious calibration samples and the streaming nature of real-world inputs. To address these challenges, we propose \textit{OSCS}, a novel framework for online FAR control without requiring malicious calibration data. OSCS leverages detection scores produced by existing defenses and employs recursive density estimation to estimate benign probability from the test stream. Based on these estimates, OSCS performs real-time accept/reject decisions while provably satisfying a user-specified FAR target. Theoretically, we show that OSCS controls the FAR up to a vanishing excess term under mild assumptions. Extensive experiments on backdoor and jailbreak attack tasks further demonstrate the effectiveness of OSCS, showing that it consistently achieves robust FAR control across diverse attack settings while outperforming existing baselines.

</details>

### 49. Provably Safe Model Updates

📄 [arXiv](https://arxiv.org/abs/2512.01899) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-12　🏷 SaTML 2026

**关键词**：`defense`、`safe update`、`parameter certification`、`alignment drift`

👤 **作者**：Leo Elmecker-Plakolm、Pierre Fasterling、Philip Sosnin、Calvin Tsay、Matthew Wicker

- 🎯 **研究动机**：正则化与参数隔离等启发式方法可缓解灾难性遗忘或对齐漂移，但无法认证更新后模型仍满足性能规约
- 🔬 **研究方法**：把问题形式化为计算参数空间中满足规约的最大局部不变域（LID），用正交体与 zonotope 参数化抽象域得到可解的原始-对偶公式，通过把更新投影回安全域实现与数据和算法无关的认证
- 📌 **结论**：在持续学习与基础模型微调基准上匹配或超越启发式基线，同时提供形式安全保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical environments are inherently dynamic. Distribution shifts, emerging vulnerabilities, and evolving requirements demand continuous updates to machine learning models. Yet even benign parameter updates can have unintended consequences, such as catastrophic forgetting in classical models or alignment drift in foundation models. Existing heuristic approaches (e.g., regularization, parameter isolation) can mitigate these effects but cannot certify that updated models continue to satisfy required performance specifications. We address this problem by introducing a framework for provably safe model updates. Our approach first formalizes the problem as computing the largest locally invariant domain (LID): a connected region in parameter space where all points are certified to satisfy a given specification. While exact maximal LID computation is intractable, we show that relaxing the problem to parameterized abstract domains (orthotopes, zonotopes) yields a tractable primal-dual formulation. This enables efficient certification of updates - independent of the data or algorithm used - by projecting them onto the safe domain. Our formulation further allows computation of multiple approximately optimal LIDs, incorporation of regularization-inspired biases, and use of lookahead data buffers. Across continual learning and foundation model fine-tuning benchmarks, our method matches or exceeds heuristic baselines for avoiding forgetting while providing formal safety guarantees.

</details>

### 50. Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

📄 [arXiv](https://arxiv.org/abs/2608.28099)　📅 2026-08

**关键词**：`tool`、`detection`、`context-aware probe`、`speculative decoding`、`runtime safety classifier`、`speculative classifier`

👤 **作者**：Collin Zhang、Tingwei Zhang、Vitaly Shmatikov

- 🎯 **研究动机**：hidden-state probe 只作用于单向量、缺上下文交互，专用 guard 模型或全 token 计算又成本过高，在线安全监控面临精度—效率权衡
- 🔬 **研究方法**：提出在目标序列末尾附加训练好的 soft prompt，把 LLM 自带的 speculative-decoding 模块改造成序列分类器，推理时直接复用 GPU 内已有的 KV cache
- 📌 **结论**：小 probe 在四类任务、四个模型（Qwen3.5-4B/9B/27B、MiniCPM4.1-8B）上稳定优于零样本 GPT-5.4-mini，多语言 prompt safety 上达到或超过 8B 专用 safety classifier，额外开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-time classification during language model inference is valuable for safety filtering, behavioral analysis, and model monitoring, but current approaches force a trade-off between accuracy and efficiency. Hidden-state probes are fast but limited: they are either not context-aware: operating on a single vector and cannot model interactions across positions; or they are very costly: having dedicated classifier models (Llama Guard, Qwen Guard, LLM-as-judge) or performing computation on hidden states for all tokens and then pooling the results (MultiMax). This shows an intrinsic trade-off between efficiency and accuracy. However, we find that the speculative-decoding module in recent LLMs can be repurposed for efficient high-quality classification. By appending a trained soft prompt at the end of the target sequence, we can repurpose the speculative-decoding module into a sequence classifier. At inference time in a speculative-decoding pipeline, the KV cache is already in GPU memory, so classification adds negligible overhead. We evaluate on four classification tasks across four models (Qwen3.5-4B, 9B, 27B, MiniCPM4.1-8B). Our small probes consistently outperform zero-shot GPT-5.4-mini and, on multilingual prompt safety, match or beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM.

</details>

### 51. SafeSeek: Universal Attribution of Safety Circuits in Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23268) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63371)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`mechanistic analysis`

👤 **作者**：Miao Yu、…、Qingsong Wen

- 🎯 **研究动机**：现有安全归因方法依赖启发式领域特定指标与搜索算法，泛化性与可靠性不足
- 🔬 **研究方法**：提出 SafeSeek：用可微分二值掩码在安全数据上梯度下降提取多粒度功能完备安全回路，并以 Safety Circuit Tuning 利用稀疏回路做高效微调
- 📌 **结论**：后门回路稀疏度 0.42%，消融使 ASR 从 100% 降至 0.4% 且保留超 99% 效用；对齐回路 3.03% 头/0.79% 神经元，移除使 ASR 从 0.8% 升至 96.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mechanistic interpretability reveals that safety-critical behaviors (e.g., alignment, jailbreak, backdoor) in Large Language Models (LLMs) are grounded in specialized functional components. However, existing safety attribution methods struggle with generalization and reliability due to their reliance on heuristic, domain-specific metrics and search algorithms. To address this, we propose SafeSeek, a unified safety interpretability framework that identifies functionally complete safety circuits in LLMs via optimization. Unlike methods focusing on isolated heads or neurons, SafeSeek introduces differentiable binary masks to extract multi-granular circuits through gradient descent on safety datasets, while integrates Safety Circuit Tuning to utilize these sparse circuits for efficient safety fine-tuning. We validate SafeSeek in two key scenarios in LLM safety: \textbf{(1) backdoor attacks}, identifying a backdoor circuit with 0.42\% sparsity, whose ablation eradicates the Attack Success Rate (ASR) from 100\% $\to$ 0.4\% while retaining over 99\% general utility; \textbf{(2) safety alignment}, localizing an alignment circuit with 3.03\% heads and 0.79\% neurons, whose removal spikes ASR from 0.8\% $\to$ 96.9\%, whereas excluding this circuit during helpfulness fine-tuning maintains 96.5\% safety retention.

</details>

### 52. Prediction-Powered Risk Monitoring of Deployed Models for Detecting Harmful Distribution Shifts

📄 [arXiv](https://arxiv.org/abs/2602.02229) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64392)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Guangyi Zhang、Yunlong Cai、Guanding Yu、Osvaldo Simeone

- 🎯 **研究动机**：动态环境中标注数据有限，部署模型性能监控困难
- 🔬 **研究方法**：PPRM 基于 prediction-powered inference 的半监督监控：合成标签加少量真实标签构造 anytime-valid 运行风险下界，与名义风险上界阈值比较检测有害偏移
- 📌 **结论**：类型 I 错误具免假设有限样本保证；在图像分类、LLM 与电信监控任务上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study the problem of monitoring model performance in dynamic environments where labeled data are limited. To this end, we propose prediction-powered risk monitoring (PPRM), a semi-supervised risk-monitoring approach based on prediction-powered inference (PPI). PPRM constructs anytime-valid lower bounds on the running risk by combining synthetic labels with a small set of true labels. Harmful shifts are detected via a threshold-based comparison with an upper bound on the nominal risk, satisfying assumption-free finite-sample guarantees on the type-I error. We demonstrate the effectiveness of PPRM through extensive experiments on image classification, large language model (LLM), and telecommunications monitoring tasks.

</details>

### 53. Mechanistic Anomaly Detection via Functional Attribution

📄 [arXiv](https://arxiv.org/abs/2604.18970) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63869)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`mechanistic analysis`、`AI safety benchmark`、`risk estimation`、`safety evaluation`、`tail risk`

👤 **作者**：Hugo Lyons Keenan、Christopher Leckie、Sarah Erfani

- 🎯 **研究动机**：现有机械异常检测依赖易被混淆的潜空间分析或绑定特定架构与模态
- 🔬 **研究方法**：把 MAD 重构为功能归因：用影响函数经参数空间采样测测试样本与小参考集的功能耦合，可信样本无法解释输出即异常
- 📌 **结论**：BackdoorBench 上七攻击四数据集平均 DER 0.93（次优 0.83）；LLM 多类后门（含显式混淆模型）显著提升，还能检测对抗与 OOD 样本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We can often verify the correctness of neural network outputs using ground truth labels, but we cannot reliably determine whether the output was produced by normal or anomalous internal mechanisms. Mechanistic anomaly detection (MAD) aims to flag these cases, but existing methods either depend on latent space analysis, which is vulnerable to obfuscation, or are specific to particular architectures and modalities. We reframe MAD as a functional attribution problem: asking to what extent samples from a trusted set can explain the model's output, where attribution failure signals anomalous behavior. We operationalize this using influence functions, measuring functional coupling between test samples and a small reference set via parameter-space sampling. We evaluate across multiple anomaly types and modalities. For backdoors in vision models, our method achieves state-of-the-art detection on BackdoorBench, with an average Defense Effectiveness Rating (DER) of 0.93 across seven attacks and four datasets (next best 0.83). For LLMs, we similarly achieve a significant improvement over baselines for several backdoor types, including on explicitly obfuscated models. Beyond backdoors, preliminary evidence shows our method can detect adversarial and out-of-distribution samples, and distinguishes multiple anomalous mechanisms within a single model. Our results establish functional attribution as an effective, modality-agnostic tool for detecting anomalous behavior in deployed models.

</details>