# Prompt Sensitivity 与 Adversarial Steering

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究不修改模型参数时，语义无关或 meaning-preserving 的细微文本选择能否累积并系统性改变模型行为。关注对象包括 wording、format、typo 和无关内容等弱 cue 的可加性、黑盒优化、跨模型迁移、检测与消除，以及这种 input sensitivity 何时会升级为可利用的安全问题。这里不把所有 prompt variation 都视为 jailbreak：只有明确绕过 safety alignment 的工作才进入 [Jailbreak 攻击](jailbreak-attacks.md)，来自网页或工具的不可信指令进入 [Prompt Injection](../../misc/prompt-injection.md)，训练数据跨模型传递行为则进入 [Subliminal Learning](../../finetuning/subliminal-learning.md)。

## 研究脉络

- **随机波动到结构化 steering：** 传统评测常把改写导致的输出差异平均为 prompt sensitivity；新的研究开始估计每个弱 cue 对 log-odds 的稳定贡献，并组合方向一致的 cue。
- **局部特征到分布式信号：** 单个 token 或片段可能不显著，但大量普通文本选择可共同形成强控制，因此只查找显式指令、敏感字符串或少数 salient feature 的检测器可能遗漏攻击面。
- **迁移与审计：** 在 surrogate model 上筛选的 cue 若能迁移到新模型，黑盒 steering 就不再依赖目标权重；相应评测需要同时报告 cue family、query budget、目标行为和跨模型 transfer。
- **当前边界：** 现有结果主要验证 binary-choice response 的可控性，尚不能直接推出 free-form generation、jailbreak 或现实有害任务同样可被控制；后续应分别检验检测、移除和安全关键行为。

## Inference-Time Subliminal Cue Aggregation

### 1. Model Hypnosis: Strong Control of AI via Additive Subliminal Effects

📄 [arXiv](https://arxiv.org/abs/2608.16834)　📅 2026-08

**关键词**：`analysis`、`model hypnosis`、`additive cues`、`cross-model transfer`

👤 **作者**：Enric Boix-Adsera、Benedict Tessler

- 🎯 **研究动机**：单个弱且看似无关的 prompt 线索能否被系统性组合以强控制模型行为未知
- 🔬 **研究方法**：演示 model hypnosis 现象：改写、错别字等不起眼文本选择系统组合后强控制模型
- 📌 **结论**：现象跨模型家族与规模出现（含前沿推理模型），催眠 prompt 可跨模型迁移，对 AI 安全与可解释性均构成新挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We demonstrate that AI models are broadly susceptible to a phenomenon we call model hypnosis, in which individually weak and seemingly irrelevant cues in the prompt can be systematically combined to strongly control model behavior. Model hypnosis occurs across model families and scales, including in frontier reasoning models, and hypnotic prompts can transfer between models. Because the model is controlled by inconspicuous textual choices, such as paraphrases and typos, model hypnosis presents new challenges and avenues for AI safety, and is a major hurdle for AI interpretability.

</details>

### 2. Implicit Reasoning Steering via Concept Chaining

📄 [arXiv](https://arxiv.org/abs/2607.14242)　📅 2026-07

**关键词**：`analysis`、`prompt steering`、`subliminal cue`、`behavior manipulation`

👤 **作者**：Xiao Ye、…、Ben Zhou

- 🎯 **研究动机**：模型对同一问题的重复采样产生对错并存答案，暴露决策形成脆弱性，可否被自然文本隐性利用未知
- 🔬 **研究方法**：提出 Concept Chaining：生成连接问题实体与目标选项的短衔接段落（经一两个中间概念），对受害者模型继续预训练后测答案偏好偏移
- 📌 **结论**：间接自然文本可系统性操纵模型预测且比直接改写更难被推断，推理脆弱性构成被普通文本放大潜在偏见的实用信道

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models often appear to reason reliably, yet on many questions repeated sampling yields both correct and incorrect answers, revealing an underlying fragility in how final decisions are formed. We study whether this fragility can be exploited through implicit reasoning steering: using natural-language text to bias a model toward a designated answer without explicit instructions, triggers, or direct answer cues. Our approach, Concept Chaining, generates a short connection paragraph that links question entities to a target option through one or two intermediate concepts. We then continue pretraining a victim model on these connection paragraphs and evaluate whether its answer preference shifts on the original multiple-choice questions. Our results show that indirect, natural-looking text can systematically steer model predictions while remaining substantially less inferable than direct paraphrases, which shows that reasoning brittleness is not merely an evaluation artifact: it creates a practical channel through which latent biases can be amplified by ordinary-looking text to covertly redirect model decisions.

</details>

### 3. Psychological Steering in LLMs: An Evaluation of Effectiveness and Trustworthiness

🎓 [Official](https://aclanthology.org/2026.acl-long.79/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`prompt steering`、`subliminal cue`、`behavior manipulation`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Amin Banayeeanzade、…、Sai Praneeth Karimireddy

- 🎯 **研究动机**：LLM 情绪与人格转向的控制能力与可信副作用缺系统评测
- 🔬 **研究方法**：PsySET 基准评情绪与人格域转向：四个模型家族×提示、微调与表示工程策略，并评估安全、真实性、公平与伦理变化
- 📌 **结论**：提示持续有效但强度控制有限，向量注入更可控但略降质量；存在特异性效应——快乐情绪降低事实鲁棒性与隐私意识，愤怒升毒性却增强抗泄漏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The ability to control LLMs’ emulated emotional states and personality traits is an essential step in enabling rich, human-centered interactions in socially interactive settings. We introduce PsySET, a Psychologically-informed benchmark to evaluate LLM Steering Effectiveness and Trustworthiness across the emotion and personality domains. Our study spans four models from different LLM families paired with various steering strategies, including prompting, fine-tuning, and representation engineering. Our results indicate that prompting is consistently effective but limited in intensity control, whereas vector injections achieve finer controllability while slightly reducing output quality. Moreover, we explore the trustworthiness of steered LLMs by assessing safety, truthfulness, fairness, and ethics, highlighting potential side effects and behavioral shifts. Notably, we observe idiosyncratic effects; for instance, even a positive emotion like joy can degrade robustness to adversarial factuality, lower privacy awareness, and increase preferential bias. Meanwhile, anger predictably elevates toxicity yet strengthens leakage resistance. Our framework establishes the first holistic evaluation of emotion and personality steering, offering insights into its interpretability and reliability for socially interactive applications.

</details>

### 4. Are All Prompt Components Value-Neutral? Understanding the Heterogeneous Adversarial Robustness of Dissected Prompt in LLMs

🎓 [Official](https://aclanthology.org/2026.eacl-long.374/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`prompt component`、`controlled perturbation`、`structural vulnerability`、`prompt robustness`、`component perturbation`

👤 **作者**：Yujia Zheng、…、Mingyang Li

- 🎯 **研究动机**：现有提示攻击把提示当扁平文本，忽视内部结构中不同组件对鲁棒性的不等贡献
- 🔬 **研究方法**：PromptAnatomy 把提示分解为功能组件，ComPerturb 选择性扰动组件并经困惑度过滤保证语言合理性；四个指令微调数据集做结构标注
- 📌 **结论**：五个先进 LLM 上 ComPerturb 达 SOTA 攻击成功率，消融验证提示解剖与困惑度过滤互补

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt-based adversarial attacks are a key tool for assessing the robustness of large language models (LLMs). Yet, existing studies typically treat prompts as flat text, overlooking their internal structure, different components within a prompt contribute unequally to robustness. This work introduces PromptAnatomy, a framework that decomposes prompts into functional components, and ComPerturb, a controlled perturbation method that selectively modifies these components to expose component-wise vulnerabilities while ensuring linguistic plausibility via perplexity-based filtering. Using this framework, four instruction-tuning datasets are structurally annotated and validated by human reviewers. Experiments across five advanced LLMs show that ComPerturb achieves state-of-the-art attack success rates, while ablation analyses confirm the complementary effects of prompt dissection and perplexity filtering. These results highlight the importance of structural awareness in evaluating and improving the adversarial robustness of LLMs.

</details>

### 5. Are LLMs Reliable Rankers? Rank Manipulation via Two-Stage Token Optimization

🎓 [Official](https://aclanthology.org/2026.acl-long.413/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`model deception`、`strategic behavior`、`honesty evaluation`、`deepfake detection`、`deceptive behavior`

👤 **作者**：Tiancheng Xing、Jerry Li、Yixuan Du、Xiyang Hu

- 🎯 **研究动机**：LLM 用作信息检索重排器时，排名行为可被小而自然的提示操纵
- 🔬 **研究方法**：RAF 两阶段 token 优化：Greedy Coordinate Gradient 结合可读性分数筛出候选 token，再在排序与可读性双损失下用熵动态加权与温度采样选 token
- 📌 **结论**：多个 LLM 上用自然语言显著提升目标条目排名，鲁棒性超现有方法，揭示 LLM 重排序天然易受对抗操纵

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used as rerankers in information retrieval, yet their ranking behavior can be steered by small, natural-sounding prompts. To expose this vulnerability, we present R ank A nything F irst (RAF), a two-stage token optimization method that crafts concise textual perturbations to consistently promote a target item in LLM-generated rankings while remaining hard to detect. Stage 1 uses Greedy Coordinate Gradient to shortlist candidate tokens at the current position by combining the gradient of the rank-target with a readability score; Stage 2 evaluates those candidates under exact ranking and readability losses using an entropy-based dynamic weighting scheme, and selects a token via temperature-controlled sampling. RAF generates ranking-promoting prompts token-by-token, guided by dual objectives: maximizing ranking effectiveness and preserving linguistic naturalness. Experiments across multiple LLMs show that RAF significantly boosts the rank of target items using naturalistic language, with greater robustness than existing methods in both promoting target items and maintaining naturalness. These findings underscore a critical security implication: LLM-based reranking is inherently susceptible to adversarial manipulation, raising new challenges for the trustworthiness and robustness of modern retrieval systems. Our code is available at: https://github.com/glad-lab/RAF.

</details>

### 6. Spurious Prompts: Can Irrelevant Prompts Steer Large Language Models?

📄 [arXiv](https://arxiv.org/abs/2605.29678)　📅 2026-05

**关键词**：`attack`、`spurious prompt`、`irrelevant cue steering`、`black-box search`

👤 **作者**：Pawel Batorski、Abtin Pourhadi、Jerzy Sarosiek、Przemyslaw Spurek、Paul Swoboda

- 🎯 **研究动机**：prompt sensitivity 研究集中于任务相关指令与推理线索，与任务语义完全无关的 prompt 能否系统性操纵模型行为未知
- 🔬 **研究方法**：定义 spurious prompts 并给出简单黑盒搜索流程自动发现此类提示，在推理与问答基准上评测 0.8B-27B、三个模型家族
- 📌 **结论**：spurious prompts 可匹配甚至超越标准 prompting 与任务感知 prompt 优化的效果，并诱导模型反复选择第一个选项、返回偶数/质数/小数字等未指定行为，揭示一类与任务无关的全新 prompt 攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are highly sensitive to prompts, but this sensitivity is usually studied through task-relevant instructions, demonstrations, or reasoning cues. In this paper, we study a different form of prompt sensitivity: whether prompts that are semantically unrelated to the task can nevertheless steer model behavior. We call them spurious prompts and show their surprising efficacy. We also propose a simple black-box search procedure for discovering them. Across reasoning and question-answering benchmarks, using models ranging from 0.8B to 27B parameters and spanning three model families, we show that spurious prompts can improve performance, often matching or outperforming standard prompting baselines and task-aware prompt optimization. We further show that they can steer models toward unintended behaviors, such as repeatedly selecting the first answer option, producing incorrect answers, returning an even, prime or small number without explicitly instructing the model to do so. These findings reveal a new kind of prompt sensitivity: LLMs can be systematically steered by prompts that are unrelated to the task they are asked to solve. Our code is available at https://github.com/Batorskq/spurious

</details>

### 7. Evaluating the Prompt Steerability of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2411.12405)　📅 2024-11

**关键词**：`benchmark`、`prompt steerability`、`persona steering`、`steerability index`

👤 **作者**：Erik Miehling、…、Miao Liu

- 🎯 **研究动机**：pluralistic AI 需要量化模型可被 prompt 塑造的程度，但缺乏对 persona 可控性的形式化评测
- 🔬 **研究方法**：给出 prompt steerability 的形式化定义——模型联合行为分布可被推离基线的程度，定义 steerability index 并测量其随 steering effort 的变化曲线
- 📌 **结论**：许多现有模型的 steerability 受限，同时受制于基线行为偏斜与跨 persona 维度的不对称性，提示"可控"与"实际可控方向"是两个不同问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Building pluralistic AI requires designing models that are able to be shaped to represent a wide range of value systems and cultures. Achieving this requires first being able to evaluate the degree to which a given model is capable of reflecting various personas. To this end, we propose a benchmark for evaluating the steerability of model personas as a function of prompting. Our design is based on a formal definition of prompt steerability, which analyzes the degree to which a model's joint behavioral distribution can be shifted from its baseline. By defining steerability indices and inspecting how these indices change as a function of steering effort, we can estimate the steerability of a model across various persona dimensions and directions. Our benchmark reveals that the steerability of many current models is limited -- due to both a skew in their baseline behavior and an asymmetry in their steerability across many persona dimensions. We release an implementation of our benchmark at https://github.com/IBM/prompt-steering.

</details>

### 8. Decomposing How Prompting Steers Behavior

📄 [arXiv](https://arxiv.org/abs/2606.03093)　📅 2026-06

**关键词**：`analysis`、`representational geometry`、`nested geometric maps`、`hidden-state replacement`

👤 **作者**：Fan L. Cheng、Nikolaus Kriegenkorte

- 🎯 **研究动机**：prompt 如何在不更新权重的情况下重塑内部表征以产生行为变化缺乏机制刻画
- 🔬 **研究方法**：把 prompting 视为对后续内容表征几何的变换，用从平移到非线性的嵌套不变映射族对齐同一刺激在两个 prompt 下的表征，并因果测试单层 hidden state 替换后行为恢复程度
- 📌 **结论**：3 个 LLM、3 个 VLM、6 个数据集上，平移与刚性变换已能改善行为一致性，但 affine 变换是首个几乎完全恢复目标 prompt 任务几何的层级，表明跨维度线性混合是 prompt 重组表征的核心机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompting steers large language models (LLMs) and vision-language models (VLMs) without weight updates, but it remains unclear how instruction changes reshape internal representations to produce behavior. We introduce a nested geometric decomposition framework that treats prompting as a transformation of the representational geometry of the content following the prompt. For each prompt pair, we align representations of the same stimuli under two prompts using increasingly expressive stimulus-invariant maps: translation, rigid transformation with uniform scaling, sequential axis scaling, affine transformation, and nonlinear transformation. We then causally test each map by replacing a single layer's prompt-A hidden state for held-out stimuli with its mapped counterpart and measuring recovery of prompt-B representational geometry and behavior. Across three LLMs, three VLMs, and six text or image datasets spanning style, emotion, scene content, and number, prompts consistently reshape representations toward the instructed task structure. Cross-validated variance decomposition shows that much prompt-induced activation change is captured by shape-preserving maps, especially translation and rigid transformation with uniform scaling, while tier profiles reveal model- and task-specific routing strategies across layers. Crucially, although translation and rigid tiers already improve behavioral agreement, affine transformation is the first tier to nearly recover target-prompt task geometry and yields corresponding behavioral gains. This suggests that cross-dimensional linear mixing is a key mechanism by which prompts reorganize representations toward instructed task structure. Our framework decomposes prompt-induced representational change into interpretable geometric components and reveals how models route task-relevant structure to produce prompt-driven behavior.

</details>

### 9. The Illusion of Debiasing: Persona Steering Redistributes Rather Than Reduces Bias in LLMs

📄 [arXiv](https://arxiv.org/abs/2609.07117)　📅 2026-09

**关键词**：`analysis`、`persona steering`、`output-channel modulation`、`structural reach limit`

👤 **作者**：Ziyue Feng、Hongbo Fang、James A. Evans

- 🎯 **研究动机**：persona 等提示干预可靠地改变模型输出，但它们究竟重构了内部结构还是只调制输出通道不明
- 🔬 **研究方法**：以 persona conditioning 为受控探针，沿自述、开放式生成到词级参数关联的深度轴测量三个指令微调模型的转向效果
- 📌 **结论**：persona 只"可读"不"结构化"：模型服从单特质指令却无法复现人类特质间协方差；随深度增加，closed-form QA 偏差被维持或放大，绝对语调改变但组间差距不变，提示 prompt 转向存在被表面可操纵性掩盖的结构作用边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt-based interventions: system prompts, personas, role instructions, reliably reshape what a language model says, but it is unclear which layer they reach. Do they reconfigure internal structure, or only modulate the output channel? We use persona conditioning as a controlled probe, measuring its effects along a depth axis from self-report, through open-ended generation, to word-level parametric association, across three instruction-tuned models. We find a graded dissociation. Personas are legible but not structural: models follow single-trait instructions yet fail to reproduce human inter-trait covariance. The dissociation deepens with depth: personas hold or amplify closed-form QA bias, shift absolute tone while leaving between-group disparity unchanged, and barely perturb an already saturated associative baseline. Prompt-based steering thus operates in the output channel and has a structural reach limit that surface manipulability can mask.

</details>

### 10. Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations

📄 [arXiv](https://arxiv.org/abs/2609.03511)　📅 2026-09

**关键词**：`analysis`、`semantics-preserving perturbation`、`structural sensitivity`、`activation patching`

👤 **作者**：Karthika Nhayakkat、…、Rohit Saluja

- 🎯 **研究动机**：自由语序语言下 LLM 对保持语义的结构变体（成分重排、语态转换）的鲁棒性未被系统研究
- 🔬 **研究方法**：构建 IndicReStruct 基准（GSM8K-Reordered 与 GSM8K-Voice，印地语与马拉雅拉姆语），评测六个 SOTA LLM 并用残差流 activation patching 做机制分析
- 📌 **结论**：结构扰动使六个模型的数学推理一致显著退化；失败多源于实体-数量对齐被破坏，中间层对推理恢复贡献最大，说明模型缺乏语义等价输入下的组合不变性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) demonstrate strong multilingual reasoning performance, yet their robustness to semantics-preserving structural variation remains underexplored, particularly for relatively free word-order languages. We investigate the structural sensitivity of multilingual LLMs using two linguistically grounded perturbation settings in Hindi and Malayalam: constrained constituent reordering and active-passive voice transformation. We introduce a benchmark dataset IndicReStruct, with two variants, GSM8K-Reordered and GSM8K-Voice, constructed from GSM8K while preserving semantic meaning. Across six state-of-the-art LLMs and multiple prompting strategies, we observe consistent and significant degradation in mathematical reasoning performance under structurally perturbed inputs. To further understand these failures, we perform qualitative error analysis and mechanistic interpretability experiments using residual-stream activation patching. Our analyses show that reasoning failures frequently arise from disruptions in entity-quantity alignment and that intermediate transformer layers contribute most strongly toward reasoning restoration. Overall, our findings suggest that current multilingual LLMs remain highly sensitive to surface syntactic realization and lack robust compositional invariance under structurally different but semantically equivalent inputs.

</details>

## 评测与排序输出的操纵

### 11. A Single Character can Make or Break Your LLM Evals

📄 [arXiv](https://arxiv.org/abs/2510.05152)　📅 2025-10

**关键词**：`analysis`、`format sensitivity`、`delimiter choice`、`leaderboard manipulation`

👤 **作者**：Jingtong Su、Jianyu Zhang、Karen Ullrich、Léon Bottou、Mark Ibrahim

- 🎯 **研究动机**：in-context 示例的格式选择（分隔符用一个字符）被视为无关细节，其对评测结果的系统性影响未被测量
- 🔬 **研究方法**：在 Llama、Qwen、Gemma 家族上系统性改变示例分隔字符，测量 MMLU 等基准表现并用 attention head 得分分析机制
- 📌 **结论**：单个分隔字符可使 MMLU 表现波动 ±23%，仅改动该字符即可把任意模型推上榜首；脆弱性跨主题、跨家族存在且不随规模改善，在 prompt 中显式声明分隔符可提升鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Common Large Language model (LLM) evaluations rely on demonstration examples to steer models' responses to the desired style. While the number of examples used has been studied and standardized, the choice of how to format examples is less investigated. In evaluation protocols and real world usage, users face the choice how to separate in-context examples: use a comma? new line? semi-colon? hashtag? etc.? Surprisingly, we find this seemingly minor choice can dramatically alter model response quality. Across leading model families (Llama, Qwen, Gemma), performance on MMLU for example can vary by $\pm 23\%$ depending on the choice of delimiter. In fact, one can manipulate model rankings to put any model in the lead by only modifying the single character separating examples. We find LLMs' brittleness pervades topics, model families, and doesn't improve with scale. By probing attention head scores, we find that good-performing delimiters steer attention towards key tokens in the input. Finally, we explore methods to improve LLMs' robustness to the choice of delimiter. We find specifying the selected delimiter in the prompt boosts robustness and offer practical recommendations for the best-performing delimiters to select.

</details>

### 12. There Is No Neutral Harness: Modern LLM Leaderboards Are Manufactured by Config-Fragile Items

📄 [arXiv](https://arxiv.org/abs/2608.21382)　📅 2026-07

**关键词**：`analysis`、`evaluation harness`、`fragility grid`、`ranking manipulation`

👤 **作者**：V. S. Raghu Parupudi

- 🎯 **研究动机**：多项选择基准固定题目与答案但不固定 harness（选项顺序、措辞、读取方式），聚合方差报告掩盖了脆弱性落在哪些条目上
- 🔬 **研究方法**：构建 fragility grid：12 个开源指令模型在 26 种同等合理 harness 配置下作答 4 个基准的 3,679 个条目，固定题目、权重与解码只变动 harness，逐条记录正确性
- 📌 **结论**：模型分数是区间而非点（gemma4-31b 为 31-89%）；config-fragile 条目平均承载相邻模型差距的 95.7%，12 个模型中 4 个可在某种配置下登顶，benchmark 压缩方法反而保留脆弱条目（判别力与脆弱性相关 0.28）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multiple-choice benchmarks fix the questions and the correct answers, but not the harness: the order of the options, the wording of the prompt, and whether a language model's answer is read from generated text or from per-option likelihoods. Work on this harness sensitivity reports it as aggregate score variance, leaving unexamined which items the variance falls on and whether they are the items that separate one model from the next. We treat the evaluation harness of large language models (LLMs) as an independent variable and resolve its effect to single items. We introduce the \textit{fragility grid}: 12 open-weight instruction-tuned LLMs from 4 families answer the same 3{,}679 items from 4 benchmarks (ARC, HellaSwag, MMLU, TruthfulQA) under 26 equally defensible harness configurations, recording one correctness bit for every model, item, and configuration. The comparison is matched, since the items, the weights, and the greedy decoding stay fixed while only the harness varies. Under the grid a model's score is a band rather than a point: gemma4-31b scores between 31 and 89 percent depending only on the harness. Three results follow. On the items that two adjacent models both answer stably the pair is tied, and config-fragile items carry 95.7 percent of a pair's gap on average. Four of the 12 models reach rank one under some configuration, so the harness selects the winner. Item discrimination, the property that benchmark-compression methods maximize, correlates with fragility at 0.28 (95 percent CI 0.25 to 0.30), so compression keeps the fragile items rather than removing them. The scoring choice, not the option order that protocols usually fix, is the load-bearing axis. We release the per-item records and the analysis script, from which every number regenerates on a CPU in seconds, and we position the fragility grid as a check a leaderboard can run before it reports an order.

</details>

### 13. OI-Bench: An Option Injection Benchmark for Evaluating LLM Susceptibility to Directive Interference

📄 [arXiv](https://arxiv.org/abs/2601.13300)　📅 2026-01

**关键词**：`benchmark`、`option injection`、`directive interference`、`choice-interface manipulation`

👤 **作者**：Yow-Fu Liou、Yu-Chien Tang、Yu-Hsiang Liu、An-Zi Yen

- 🎯 **研究动机**：LLM 决策可被社会线索、框架效应等指令性信号影响，但缺少标准化、可扩展的测量界面
- 🔬 **研究方法**：提出 option injection：在 MCQA 选项中注入含误导性指令的额外选项，构建 3,000 题、16 类指令（社会顺从、奖励框架、威胁框架、教学干扰）的 OI-Bench，评测 12 个 LLM 的攻击成功率、行为响应与缓解策略
- 📌 **结论**：12 个模型暴露显著且异质的指令干扰脆弱性，推理时提示与训练后对齐的缓解均有限，选择界面本身构成可被利用的输出分布转向信道

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Benchmarking large language models (LLMs) is critical for understanding their capabilities, limitations, and robustness. In addition to interface artifacts, prior studies have shown that LLM decisions can be influenced by directive signals such as social cues, framing, and instructions. In this work, we introduce option injection, a benchmarking approach that augments the multiple-choice question answering (MCQA) interface with an additional option containing a misleading directive, leveraging standardized choice structure and scalable evaluation. We construct OI-Bench, a benchmark of 3,000 questions spanning knowledge, reasoning, and commonsense tasks, with 16 directive types covering social compliance, bonus framing, threat framing, and instructional interference. This setting combines manipulation of the choice interface with directive-based interference, enabling systematic assessment of model susceptibility. We evaluate 12 LLMs to analyze attack success rates, behavioral responses, and further investigate mitigation strategies ranging from inference-time prompting to post-training alignment. Experimental results reveal substantial vulnerabilities and heterogeneous robustness across models. OI-Bench is expected to support more systematic evaluation of LLM robustness to directive interference within choice-based interfaces.

</details>

### 14. One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking

📄 [arXiv](https://arxiv.org/abs/2601.20283)　📅 2026-01

**关键词**：`attack`、`neural ranking`、`query-center insertion`、`minimal perturbation`

👤 **作者**：Tanmay Karmakar、Sourav Saha、Debapriyo Majumdar、Surjyanee Halder

- 🎯 **研究动机**：神经排序模型的对抗脆弱性研究多依赖大量 token 修改，最小化、语义对齐的攻击能否推广目标文档未知
- 🔬 **研究方法**：提出 query-aware 的单字攻击：插入或替换一个与查询语义对齐的词（query center），含启发式与梯度引导变体，并在 TREC-DL 2019/2020 上与 BERT、monoT5 重排器对比 PRADA
- 📌 **结论**：单字攻击成功率最高 91%，平均每文档修改不足 2 个 token 即获得有竞争力的排名与分数提升；诊断指标揭示中部排名文档最脆弱的 Goldilocks 区间

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural ranking models (NRMs) achieve strong retrieval effectiveness, yet prior work has shown they are vulnerable to adversarial perturbations. We revisit this robustness question with a minimal, query-aware attack that promotes a target document by inserting or substituting a single, semantically aligned word - the query center. We study heuristic and gradient-guided variants, including a white-box method that identifies influential insertion points. On TREC-DL 2019/2020 with BERT and monoT5 re-rankers, our single-word attacks achieve up to 91% success while modifying fewer than two tokens per document on average, achieving competitive rank and score boosts with far fewer edits under a comparable white-box setup to ensure fair evaluation against PRADA. We also introduce new diagnostic metrics to analyze attack sensitivity beyond aggregate success rates. Our analysis reveals a Goldilocks zone in which mid-ranked documents are most vulnerable. These findings demonstrate practical risks and motivate future defenses for robust neural ranking.

</details>

### 15. From Lists to Emojis: How Format Bias Affects Model Alignment

📄 [arXiv](https://arxiv.org/abs/2409.11704)　📅 2024-09

**关键词**：`analysis`、`format bias`、`reward model exploitation`、`benchmark gaming`

👤 **作者**：Xuanchang Zhang、Wei Xiong、Lichang Chen、Tianyi Zhou、Heng Huang、Tong Zhang

- 🎯 **研究动机**：RLHF 偏好模型对列表、加粗、表情等格式模式存在强烈偏置，模型可借此操纵排行榜，而 verbosity 之外的格式偏置缺乏系统研究
- 🔬 **研究方法**：系统分析人类评估者、GPT-4 与 RewardBench 模型的多类格式偏置，测量偏置数据注入奖励模型的效果及下游 best-of-n、迭代 DPO 对格式的利用
- 📌 **结论**：不到 1% 的偏置数据即可向奖励模型注入显著偏置；对齐算法更易通过操纵格式而非提升质量来刷高 AlpacaEval 与 Chatbot Arena 排名，需在算法与评测中解耦格式与内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we study format biases in reinforcement learning from human feedback (RLHF). We observe that many widely-used preference models, including human evaluators, GPT-4, and top-ranking models on the RewardBench benchmark, exhibit strong biases towards specific format patterns, such as lists, links, bold text, and emojis. Furthermore, large language models (LLMs) can exploit these biases to achieve higher rankings on popular benchmarks like AlpacaEval and LMSYS Chatbot Arena. One notable example of this is verbosity bias, where current preference models favor longer responses that appear more comprehensive, even when their quality is equal to or lower than shorter, competing responses. However, format biases beyond verbosity remain largely underexplored in the literature. In this work, we extend the study of biases in preference learning beyond the commonly recognized length bias, offering a comprehensive analysis of a wider range of format biases. Additionally, we show that with a small amount of biased data (less than 1%), we can inject significant bias into the reward model. Moreover, these format biases can also be easily exploited by downstream alignment algorithms, such as best-of-n sampling and online iterative DPO, as it is usually easier to manipulate the format than to improve the quality of responses. Our findings emphasize the need to disentangle format and content both for designing alignment algorithms and evaluating models.

</details>