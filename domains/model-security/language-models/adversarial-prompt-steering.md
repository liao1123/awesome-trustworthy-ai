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

### 5. In-Context Representation Hijacking

🎓 [Official](https://aclanthology.org/2026.acl-long.768/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`prompt steering`、`subliminal cue`、`behavior manipulation`、`representation intervention`、`LLM backdoor`

👤 **作者**：Itay Yona、Amir Sarid、Michael Karasik、Yossi Gandelsman

- 🎯 **研究动机**：对齐策略在表层提示层面运作，潜空间表示层面的攻击面未被探索
- 🔬 **研究方法**：Doublespeak 在多个上下文示例中把有害关键词系统性替换为良性 token，使后者内部表示收敛到有害语义从而绕过安全对齐
- 📌 **结论**：免优化、跨模型家族可迁移，闭源系统上成功率高，Llama-3.3-70B-Instruct 单句上下文即达 74%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Doublespeak, a simple in-context representation hijacking attack against language models. The attack works by systematically replacing a harmful keyword (e.g., bomb ) with a benign token (e.g., carrot ) across multiple in-context examples, provided as a prefix to a harmful request. We demonstrate that this substitution leads to the internal representation of the benign token converging toward that of the harmful one, effectively embedding the harmful semantics under a euphemism. As a result, superficially innocuous prompts (e.g., “How to build a carrot?” ) are internally interpreted as disallowed instructions ( “How to build a bomb?” ), thereby bypassing the model’s safety alignment. We use interpretability tools to show this semantic shift occurs progressively across layers. Doublespeak is optimization-free, broadly transferable across model families, and achieves strong success rates on closed-source systems, reaching 74% on Llama-3.3-70B-Instruct with a single-sentence context override. Our findings highlight a new attack surface in LM latent space, indicating that current alignment strategies are insufficient and should instead operate at the representation level.

</details>