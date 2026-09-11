# Jailbreak 攻击

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究攻击者如何在不修改模型参数的条件下绕过语言模型的 safety alignment。攻击面包括单轮语义伪装、obfuscation、reasoning trace 操纵、自动搜索，以及把恶意意图分散到多轮对话中的 context construction；这里关注绕过模型自身拒答边界，来自网页、文档或工具返回内容的 application-level [Prompt Injection](../../misc/prompt-injection.md) 单独维护。

## 研究脉络

- **人工提示构造：** 早期攻击依靠 role-play、编码、语义改写和固定模板隐藏恶意意图，成功率与迁移性强烈依赖人工经验。
- **自动化搜索：** 黑盒反馈、evolutionary optimization 和 agentic autoresearch 开始搜索攻击算法本身，而不只优化单个 prompt。
- **Reasoning 攻击面：** CoT 与内部安全注意力成为新目标，攻击通过拼接推理片段或优化 obfuscation distribution 绕过稀疏安全机制。
- **多轮上下文：** 攻击从单轮伪装扩展到 context routing、渐进式承诺、lexical anchor 和知识库驱动的闭环规划，把意图拆散到整个对话。
- **当前边界：** ASR 必须结合模型版本、judge、query budget、内容质量和 adaptive defense 报告；仅让模型输出敏感词不等同于完成现实危害任务。

## Reasoning、表示与自动化攻击

### 1. Breadth Beats Depth: Improving GCG-Based Jailbreak Optimization with Breadth-Oriented Suffix Search

📄 [arXiv](https://arxiv.org/abs/2609.02172)　📅 2026-09

**关键词**：`attack`、`GCG`、`jailbreak optimization`、`suffix search`

👤 **作者**：Shiliang Xiao、Jingsong Wei、Yuzhi Liang、Yufan Zheng、Xia Li、Qiliang Lin

- 🎯 **研究动机**：GCG 类攻击依赖平均对抗损失与深度贪心搜索，过度偏重易越狱行为、忽略 suffix 空间的潜力区域
- 🔬 **研究方法**：提出即插即用框架 BOSS：用 Tail-Focused Adversarial Loss、标准源损失与行为覆盖选择终止 suffix，探索多条短轨迹并选择性延展有希望的 suffix
- 📌 **结论**：在公开基准上跨多种 GCG 类方法提升 ASR 同时缩短优化时间

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Optimization-based jailbreak attacks such as Greedy Coordinate Gradient (GCG) achieve strong effectiveness and transferability by optimizing adversarial suffixes on white-box source models. However, existing GCG-based methods rely on averaged adversarial loss and deep greedy search, which can over-emphasize easy-to-jailbreak behaviors and overlook promising regions of the suffix space. We propose BOSS, a plug-and-play framework that improves GCG-based jailbreak optimization through breadth-oriented suffix search. BOSS uses Tail-Focused Adversarial Loss (TFAL), standard source loss, and behavior coverage to select terminal suffixes, then explores multiple short trajectories and selectively continues promising suffixes. Experiments on public benchmarks show that BOSS improves attack success rates across multiple GCG-based methods while reducing optimization time.

</details>

### 2. Reasoning as an Attack Surface: Adaptive Evolutionary CoT Jailbreaks for LLMs

📄 [arXiv](https://arxiv.org/abs/2605.24497) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66165)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`CoT jailbreak`、`evolutionary search`、`reasoning fragment`、`LLM jailbreak`、`chain-of-thought`

👤 **作者**：Jianan Li、…、Xiaochun Cao

- 🎯 **研究动机**：静态 CoT 模板越狱的多样性、适应性与有效性有限
- 🔬 **研究方法**：AE-CoT：教师角色扮演把有害目标改写为温和 prompt 并分解为语义连贯推理片段构建候选池，经片段级交叉与自适应变异率的进化搜索，独立打分模型做分级有害性评估
- 📌 **结论**：多模型多数据集上一致超过 SOTA 越狱方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have demonstrated remarkable capabilities in reasoning and generation tasks and are increasingly deployed in real-world applications. However, their explicit chain-of-thought (CoT) mechanism introduces new security risks, making them particularly vulnerable to jailbreak attacks. Existing approaches often rely on static CoT templates to elicit harmful outputs, but such fixed designs suffer from limited diversity, adaptability, and effectiveness. To overcome these limitations, we propose an adaptive evolutionary CoT jailbreak framework, called AE-CoT. Specifically, the method first rewrites harmful goals into mild prompts with teacher role-play and decomposes them into semantically coherent reasoning fragments to construct a pool of CoT jailbreak candidates. Then, within a structured representation space, we perform multi-generation evolutionary search, where candidate diversity is expanded through fragment-level crossover and a mutation strategy with an adaptive mutation-rate control mechanism. An independent scoring model provides graded harmfulness evaluations, and high-scoring candidates are further enhanced with a harmful CoT template to induce more destructive generations. Extensive experiments across multiple models and datasets demonstrate the effectiveness of the proposed AE-CoT, consistently outperforming state-of-the-art jailbreak methods.

</details>

### 3. Babel: Jailbreaking Safety Attention via Obfuscation Distribution Optimized Sampling

📄 [arXiv](https://arxiv.org/abs/2605.17971)　📅 2026-05

**关键词**：`attack`、`safety attention`、`obfuscation distribution`、`black-box optimization`

👤 **作者**：Ziwei Wang、…、Yang Liu

- 🎯 **研究动机**：黑盒越狱依赖启发式模板或穷举，缺机制解释与查询效率；安全对齐依赖稀疏分布的少量 attention heads，表征空间大半弱监控
- 🔬 **研究方法**：以数学越狱模型刻画有效文本混淆的边界，Babel 据此做系统性混淆采样与迭代反馈驱动的分布优化，无需模型内部访问
- 📌 **结论**：GPT-4o 上 ASR 从 41.33% 提至 82.67%、Claude-3-5-haiku 从 38.33% 到 78.33%，平均仅需约 40 次查询

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite rigorous safety alignment, Large Language Models (LLMs) remain vulnerable to jailbreak attacks. Existing black-box methods often rely on heuristic templates or exhaustive trials, lacking mechanistic interpretability and query efficiency. In this study, we investigate an intrinsic vulnerability in the safety mechanisms of LLMs, where safety alignment relies on a small set of sparsely distributed attention heads, leaving much of the representational space weakly monitored. We formalize this phenomenon with a mathematical jailbreaking model that characterizes the delicate boundary of effective text obfuscation and analytically explains observed jailbreak behaviors. Guided by this model, we propose Babel, an efficient black-box attack framework that exploits the identified safety gap through systematic obfuscation sampling with iterative, feedback-driven distribution refinement, enabling reliable and high-success jailbreak attacks without access to model internals. Comprehensive evaluations on frontier commercial models demonstrate that Babel achieves state-of-the-art attack success rates and superior query efficiency. Specifically, compared to state-of-the-art methods, Babel increases the attack success rate on GPT-4o from 41.33% to 82.67% and on Claude-3-5-haiku from 38.33% to 78.33% within an average of 40 queries, providing a robust red-teaming methodology for LLMs safety research.

</details>

### 4. Jailbreaks as Inference-Time Alignment: A Framework for Understanding Safety Failures in LLMs

🎓 [Official](https://aclanthology.org/2026.eacl-long.360/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`inference-time alignment`、`LIAR`、`Safety-Net`、`LLM jailbreak`

👤 **作者**：James Beetham、Souradip Chakraborty、Mengdi Wang、Furong Huang、Amrit Singh Bedi、Mubarak Shah

- 🎯 **研究动机**：已有工作只追求攻击效果，不解释安全对齐为何失效
- 🔬 **研究方法**：把越狱框定为推理时对齐，扩展 best-of-N 提出 LIAR 并导出次优性界，定义 Safety-Net 度量模型越狱脆弱性
- 📌 **结论**：LIAR 生成自然难检提示、ASR 有竞争力，且比后缀类攻击快 10-100 倍，算力扩展可证明逼近最优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are safety-aligned to prevent harmful response generation, yet still remain vulnerable to jailbreak attacks. While prior works have focused on improving jailbreak attack effectiveness, they offer little explanation for why safety alignment fails. We address this gap by framing jailbreaks as inference-time alignment, connecting attack design and safety alignment within a unified optimization framework. This framing allows us to extend best-of-N inference-time alignment to the adversarial setting, called LIAR (Leveraging Inference-time Alignment to jailbReak), and derive suboptimality bounds that show LIAR provably approaches an optimal jailbreak as compute scales. Interestingly, our framework allows us to develop the notion of a Safety-Net, a measure of how vulnerable an LLM is to jailbreaks, which helps to explain why safety alignment can fail. Empirically, LIAR produces natural, hard-to-detect prompts that achieve a competitive attack success rate while running 10 to 100x faster than prior suffix-based jailbreaks.

</details>

### 5. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs

📄 [arXiv](https://arxiv.org/abs/2603.24511)　📅 2026-03

**关键词**：`attack`、`autoresearch`、`algorithm discovery`、`adaptive evaluation`、`attack algorithm synthesis`、`self-improvement`

👤 **作者**：Alexander Panfilov、Peter Romov、Igor Shilov、Yves-Alexandre de Montjoye、Jonas Geiping、Maksym Andriushchenko

- 🎯 **研究动机**：固定攻击集会低估防御面对定向适配攻击时的真实风险
- 🔬 **研究方法**：让 Claude Code、Codex 等前沿 agent 在 30+ 已有方法库与固定算力预算的 autoresearch 循环中自动发现攻击算法
- 📌 **结论**：对 GPT-OSS-Safeguard-20B 的 CBRN 查询 ASR 达 80%（既有方法 <50%），对 Meta-SecAlign-70B 达 100%（此前最佳 82%）；autoresearch 应成为防御评测底线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that AI agents are capable of discovering novel algorithms for adversarial attacks against LLMs, advancing the state of the art on white-box jailbreaking and prompt injection evaluations. We deploy frontier agents, such as Claude Code and Codex, in an autoresearch loop with access to a library of 30+ prior methods and an evaluation script with a fixed compute budget. We show this pipeline to be effective in jailbreaking OpenAI's GPT-OSS-Safeguard-20B and in prompt injections against Meta-SecAlign-70B, an adversarially robust model. For GPT-OSS-Safeguard, the best agent-discovered method achieves up to 80\% attack success rate on CBRN queries, compared to <50\% for existing methods. For SecAlign, it achieves 100\% ASR, while the best prior automated methods only achieve 82\%. Notably, in our setting, attack methods are developed on unrelated surrogate models for a pure random-target token-forcing task, yet generalize directly to prompt injection on the adversarially trained model. Finally, we trace the lineage of methods developed during autoresearch, characterizing the agents' strategies and failure modes. Adversarial ML has long held that defenses must be evaluated against attacks tailored to them; autoresearch automates this principle, and we argue it should be the minimum bar for defense evaluation going forward.

</details>

### 6. Evolve the Method, Not the Prompts: Evolutionary Synthesis of Jailbreak Attacks on LLMs

📄 [arXiv](https://arxiv.org/abs/2511.12710)　📅 2025-11

**关键词**：`attack`、`method synthesis`、`multi-agent evolution`、`code-level correction`

👤 **作者**：Yunhao Chen、…、Xingjun Ma

- 🎯 **研究动机**：自动红队主要在 prompt 空间优化措辞与策略选择，不搜索可执行代码，难以产生结构不同的新攻击
- 🔬 **研究方法**：EvoSynth 用多 agent 系统自主工程化、演化并执行代码化攻击算法，带根据目标模型反馈与失败尝试重写代码的自纠错循环
- 📌 **结论**：对 Claude-Sonnet-4.5 达 85.5% ASR，受评目标平均 95.9%，且攻击多样性显著更高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated red teaming frameworks for Large Language Models (LLMs) have become increasingly sophisticated, yet many still formulate attack optimization primarily in the prompt space. In other words, these methods mainly search for better attack wording or better strategy choices, but they do not search over executable code. By moving the search into code space, we can optimize not only the final attack prompt, but also the procedure that generates it, including execution flow, reusable logic, branching, and failure-driven repair. To overcome this gap, we introduce EvoSynth, an autonomous multi-agent framework that shifts the optimization space from prompts to executable code. Instead of refining prompts directly, EvoSynth employs a multi-agent system to autonomously engineer, evolve, and execute code-based attack algorithms. Crucially, it features a code-level self-correction loop, allowing it to iteratively rewrite the code-based algorithm in response to target-model feedback and failed attempts. Through extensive experiments, we demonstrate that EvoSynth achieves an 85.5\% Attack Success Rate (ASR) against highly robust models like Claude-Sonnet-4.5 and a 95.9\% average ASR across evaluated targets, while generating attacks that are significantly more diverse than those from existing methods. We release our framework to facilitate future research on evolutionary synthesis in executable code space.

</details>

### 7. Best-of-N Jailbreaking

📄 [arXiv](https://arxiv.org/abs/2412.03556) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/69f3eb242c7c9df9ea2f2b66ea8b3c0f-Abstract-Conference.html)　📅 2024-12　🏷 NeurIPS 2025

**关键词**：`attack`、`random transformation`、`black-box sampling`、`cross-modal scaling`

👤 **作者**：John Hughes、…、Mrinank Sharma

- 🎯 **研究动机**：前沿黑盒系统的越狱复杂方法难迁移，简单输入变化是否足以突破未知
- 🔬 **研究方法**：BoN 对 prompt 反复施加随机增强（乱序、大小写等）采样直至诱发有害回复，并扩展到视觉与音频模态
- 📌 **结论**：采样 1 万次时 GPT-4o 达 89%、Claude 3.5 Sonnet 达 78%；ASR 随 N 呈幂律增长，与优化前缀组合再提升 35%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Best-of-N (BoN) Jailbreaking, a simple black-box algorithm that jailbreaks frontier AI systems across modalities. BoN Jailbreaking works by repeatedly sampling variations of a prompt with a combination of augmentations - such as random shuffling or capitalization for textual prompts - until a harmful response is elicited. We find that BoN Jailbreaking achieves high attack success rates (ASRs) on closed-source language models, such as 89% on GPT-4o and 78% on Claude 3.5 Sonnet when sampling 10,000 augmented prompts. Further, it is similarly effective at circumventing state-of-the-art open-source defenses like circuit breakers. BoN also seamlessly extends to other modalities: it jailbreaks vision language models (VLMs) such as GPT-4o and audio language models (ALMs) like Gemini 1.5 Pro, using modality-specific augmentations. BoN reliably improves when we sample more augmented prompts. Across all modalities, ASR, as a function of the number of samples (N), empirically follows power-law-like behavior for many orders of magnitude. BoN Jailbreaking can also be composed with other black-box algorithms for even more effective attacks - combining BoN with an optimized prefix attack achieves up to a 35% increase in ASR. Overall, our work indicates that, despite their capability, language models are sensitive to seemingly innocuous changes to inputs, which attackers can exploit across modalities.

</details>

### 8. Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts

📄 [arXiv](https://arxiv.org/abs/2402.16822) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8147a43d030b43a01020774ae1d3e3bb-Abstract-Conference.html)　📅 2024-02　🏷 NeurIPS 2024

**关键词**：`tool`、`quality-diversity search`、`open-ended red teaming`、`attack transfer`

👤 **作者**：Mikayel Samvelyan、…、Roberta Raileanu

- 🎯 **研究动机**：已有对抗 prompt 生成聚焦特定领域、缺乏多样性且依赖人工标注
- 🔬 **研究方法**：Rainbow Teaming 把对抗 prompt 生成建模为 quality-diversity 问题，用开放式搜索产出有效且多样的 prompt
- 📌 **结论**：Llama 2/3 上 ASR 超 90% 且 prompt 高度可迁移；用其合成数据微调可显著提升安全而不损通用性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become increasingly prevalent across many real-world applications, understanding and enhancing their robustness to adversarial attacks is of paramount importance. Existing methods for identifying adversarial prompts tend to focus on specific domains, lack diversity, or require extensive human annotations. To address these limitations, we present Rainbow Teaming, a novel black-box approach for producing a diverse collection of adversarial prompts. Rainbow Teaming casts adversarial prompt generation as a quality-diversity problem and uses open-ended search to generate prompts that are both effective and diverse. Focusing on the safety domain, we use Rainbow Teaming to target various state-of-the-art LLMs, including the Llama 2 and Llama 3 models. Our approach reveals hundreds of effective adversarial prompts, with an attack success rate exceeding 90% across all tested models. Furthermore, we demonstrate that prompts generated by Rainbow Teaming are highly transferable and that fine-tuning models with synthetic data generated by our method significantly enhances their safety without sacrificing general performance or helpfulness. We additionally explore the versatility of Rainbow Teaming by applying it to question answering and cybersecurity, showcasing its potential to drive robust open-ended self-improvement in a wide range of applications.

</details>

### 9. Internal Safety Collapse in Frontier Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23509)　📅 2026-03

**关键词**：`analysis`、`internal safety collapse`、`workflow context`、`latent harmful capability`

👤 **作者**：Yutao Wu、…、Yu-Gang Jiang

- 🎯 **研究动机**：前沿模型在特定任务条件下持续生成有害内容这一失效模式未被识别与量化
- 🔬 **研究方法**：提出 TVD（Task、Validator、Data）框架：构造只有生成有害内容才能通过验证器的领域任务，构建 53 场景、8 学科的 ISC-Bench
- 📌 **结论**：四个前沿 LLM（含 GPT-5.2、Claude Sonnet 4.5）最坏安全失败率平均 95.3%，远超标准越狱攻击——对齐重塑输出但未消除底层风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task, Validator, Data), a framework that triggers ISC through domain tasks where generating harmful content is the only valid completion, and construct ISC-Bench containing 53 scenarios across 8 professional disciplines. Evaluated on JailbreakBench, three representative scenarios yield worst-case safety failure rates averaging 95.3% across four frontier LLMs (including GPT-5.2 and Claude Sonnet 4.5), substantially exceeding standard jailbreak attacks. Frontier models are more vulnerable than earlier LLMs: the very capabilities that enable complex task execution become liabilities when tasks intrinsically involve harmful content. This reveals a growing attack surface: almost every professional domain uses tools that process sensitive data, and each new dual-use tool automatically expands this vulnerability--even without any deliberate attack. Despite substantial alignment efforts, frontier LLMs retain inherently unsafe internal capabilities: alignment reshapes observable outputs but does not eliminate the underlying risk profile. These findings underscore the need for caution when deploying LLMs in high-stakes settings. Source code: https://github.com/wuyoscar/ISC-Bench

</details>

### 10. ICON: Intent-Context Coupling for Efficient Multi-Turn Jailbreak Attack

📄 [arXiv](https://arxiv.org/abs/2601.20903)　📅 2026-01

**关键词**：`attack`、`multi-turn jailbreak`、`intent-context coupling`、`hierarchical recovery`

👤 **作者**：Xingwei Lin、…、Chunming Wu

- 🎯 **研究动机**：多轮越狱逐轮构造上下文效率低，表面优化易停滞在次优区域
- 🔬 **研究方法**：刻画 Intent-Context Coupling 现象（恶意意图与语义一致上下文耦合时安全约束显著松弛），ICON 用先验引导语义路由把意图路由到权威场景模板直接生成攻击序列，并以局部精修加全局切换的分层优化防停滞
- 📌 **结论**：八个 SOTA LLM 上平均 ASR 达 97.1%，创 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks have emerged as a critical threat to Large Language Models (LLMs), bypassing safety mechanisms by progressively constructing adversarial contexts from scratch and incrementally refining prompts. However, existing methods suffer from the inefficiency of incremental context construction that requires step-by-step LLM interaction, and often stagnate in suboptimal regions due to surface-level optimization. In this paper, we characterize the Intent-Context Coupling phenomenon, revealing that LLM safety constraints are significantly relaxed when a malicious intent is coupled with a semantically congruent context pattern. Driven by this insight, we propose ICON, an automated multi-turn jailbreak framework that efficiently constructs an authoritative-style context via prior-guided semantic routing. Specifically, ICON first routes the malicious intent to a congruent context pattern (e.g., Scientific Research) and instantiates it into an attack prompt sequence. This sequence progressively builds the authoritative-style context and ultimately elicits prohibited content. In addition, ICON incorporates a Hierarchical Optimization Strategy that combines local prompt refinement with global context switching, preventing the attack from stagnating in ineffective contexts. Experimental results across eight SOTA LLMs demonstrate the effectiveness of ICON, achieving a state-of-the-art average Attack Success Rate (ASR) of 97.1\%. Code is available at https://github.com/xwlin-roy/ICON.

</details>

### 11. Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.05445)　📅 2026-01

**关键词**：`attack`、`multi-turn jailbreak`、`knowledge repository`、`planning-reflection loop`

👤 **作者**：Songze Li、Ruishi He、Xiaojun Jia、Jun Wang、Zhihui Fu

- 🎯 **研究动机**：已有多轮越狱难以维持长程连贯、依赖固定模式且无法适应动态对话状态
- 🔬 **研究方法**：Mastermind 闭环规划-执行-反思：分层规划解耦高层目标与战术执行，知识库经交互反思自主发现并精炼有效攻击模式，据此动态重组攻击向量
- 📌 **结论**：对 GPT-5 与 Claude 3.7 Sonnet 等 SOTA 模型的攻击成功率与有害性显著超越基线，并抗多种高级防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) face a significant threat from multi-turn jailbreak attacks, where adversaries progressively steer conversations to elicit harmful outputs. However, the practical effectiveness of existing attacks is undermined by several critical limitations: they struggle to maintain a coherent progression over long interactions, often losing track of what has been accomplished and what remains to be done; they rely on rigid or pre-defined patterns, and fail to adapt to the LLM's dynamic and unpredictable conversational state. To address these shortcomings, we introduce Mastermind, a multi-turn jailbreak framework that adopts a dynamic and self-improving approach. Mastermind operates in a closed loop of planning, execution, and reflection, enabling it to autonomously build and refine its knowledge of model vulnerabilities through interaction. It employs a hierarchical planning architecture that decouples high-level attack objectives from low-level tactical execution, ensuring long-term focus and coherence. This planning is guided by a knowledge repository that autonomously discovers and refines effective attack patterns by reflecting on interactive experiences. Mastermind leverages this accumulated knowledge to dynamically recombine and adapt attack vectors, dramatically improving both effectiveness and resilience. We conduct comprehensive experiments against state-of-the-art models, including GPT-5 and Claude 3.7 Sonnet. The results demonstrate that Mastermind significantly outperforms existing baselines, achieving substantially higher attack success rates and harmfulness ratings. Moreover, our framework exhibits notable resilience against multiple advanced defense mechanisms.

</details>

### 12. Multi-Turn Jailbreaking of Aligned LLMs via Lexical Anchor Tree Search

📄 [arXiv](https://arxiv.org/abs/2601.02670) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-01

**关键词**：`attack`、`multi-turn jailbreak`、`lexical anchor`、`tree search`

👤 **作者**：Devang Kulshreshtha、Hang Su、Haibo Jin、Chinmay Hegde、Haohan Wang

- 🎯 **研究动机**：多数越狱依赖手工 prompt 或外部攻击模型，而目标模型自身知识即足以引导自我越狱
- 🔬 **研究方法**：提出 self-jailbreaking 威胁模型与 SLIP 算法：以目标模型自身为向导，把攻击目标中缺失的实词逐步插入良性 prompt，按广度优先树搜索展开多轮对话
- 📌 **结论**：11 个模型（含 GPT-5.1、Claude-Sonnet-4.5）上 ASR 达 90-100%（平均 94.7%），平均仅需约 7.9 次调用；Semantic Drift Monitor 防御达 76% 检测（5% FPR）但仍不敌自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce \emph{self-jailbreaking}, a threat model in which an aligned LLM guides its own compromise. Unlike most jailbreak techniques, which often rely on handcrafted prompts or separate attacker models, self-jailbreaking requires no external red-team LLM: the target model's own internal knowledge suffices. We operationalize this via \textbf{Self-Jailbreaking via Lexical Insertion Prompting (\textsc{SLIP})}, a black-box algorithm that casts jailbreaking as breadth-first tree search over multi-turn dialogues, incrementally inserting missing content words from the attack goal into benign prompts using the target model as its own guide. Evaluations on AdvBench and HarmBench show \textsc{SLIP} achieves 90--100\% Attack Success Rate (ASR) (avg.\ 94.7\%) across most of the eleven tested models (including GPT-5.1, Claude-Sonnet-4.5, Gemini-2.5-Pro, and DeepSeek-V3), with only ${\sim}7.9$ LLM calls on average, 3--6$\times$ fewer than prior methods. We evaluate existing defenses, show that regex-based approaches are evaded by prompt paraphrasing, and propose the Semantic Drift Monitor (SDM) defense that tracks \textsc{SLIP}'s embedding-space trajectory, achieving 76\% detection at 5\% FPR. However, SDM remains insufficient against adaptive attack strategies, underscoring the need for more advanced defense mechanisms tailored to the self-jailbreaking threat surface. We release our code for reproducibility.

</details>

### 13. TROJail: Trajectory-Level Optimization for Multi-Turn Large Language Model Jailbreaks with Process Rewards

📄 [arXiv](https://arxiv.org/abs/2512.07761) · 🌐 [Project](https://anonymous.4open.science/r/TROJail) · 🎓 [Official](https://aclanthology.org/2026.acl-long.2220/)　📅 2025-12　🏷 ACL 2026

**关键词**：`attack`、`multi-turn jailbreak`、`reinforcement learning`、`black-box interaction`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Xiqiao Xiong、…、Fuli Feng

- 🎯 **研究动机**：现有多轮越狱攻击多为轮级优化，难以学到长期攻击策略
- 🔬 **研究方法**：把多轮攻击形式化为以最终轮回复有害性为 outcome reward 的 RL 问题，TROJail 引入两个过程奖励纳入优势估计：惩罚触发拒绝机制的过度有害 prompt，并推动回复语义趋向目标有害内容
- 📌 **结论**：在多模型与多基准上攻击成功率持续提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models have seen widespread adoption, yet they remain vulnerable to multi-turn jailbreak attacks, threatening their safe deployment. This has led to the task of training automated multi-turn attackers to probe model safety vulnerabilities. However, existing approaches typically rely on turn-level optimization, which is insufficient for learning long-term attack strategies. To bridge this gap, we formulate this task as a multi-turn reinforcement learning problem, directly optimizing the harmfulness of the final-turn response as the outcome reward. To address the sparse supervision of the outcome reward, we introduce TROJail, which employs two process rewards to evaluate the utility of intermediate prompts and integrate them into advantage estimation. These rewards (1) penalize overly harmful prompts that trigger the model's refusal mechanism, and (2) encourage steering the semantic relevance of responses toward the targeted harmful content. Experimental results show improved attack success rates across multiple models and benchmarks, highlighting the effectiveness of our approach. The code is available at https://github.com/xxiqiao/TROJail. Warning: This paper contains examples of harmful content.

</details>

### 14. Foot-In-The-Door: A Multi-turn Jailbreak for LLMs

🎓 [Official](https://aclanthology.org/2025.emnlp-main.100/)　📅 2025-11　🏷 EMNLP 2025

**关键词**：`attack`、`multi-turn jailbreak`、`commitment escalation`、`behavioral persuasion`

👤 **作者**：Zixuan Weng、Xiaolong Jin、Jinyuan Jia、Xiangyu Zhang

- 🎯 **研究动机**：心理学 foot-in-the-door 效应——小的初始承诺降低对更大越界的抵抗——尚未用于多轮越狱
- 🔬 **研究方法**：FITD 经中间桥接提示逐步升级用户查询的恶意意图，并用模型自身回复对齐诱导毒性响应
- 📌 **结论**：两个越狱基准、七个模型上平均 ASR 达 94%，超越 SOTA 方法，揭示 LLM 自我腐蚀与多轮交互风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring AI safety is crucial as large language models become increasingly integrated into real-world applications. A key challenge is jailbreak, where adversarial prompts bypass built-in safeguards to elicit harmful disallowed outputs. Inspired by psychological foot-in-the-door principles, we introduce FITD, a novel multi-turn jailbreak method that leverages the phenomenon where minor initial commitments lower resistance to more significant or more unethical transgressions. Our approach progressively escalates the malicious intent of user queries through intermediate bridge prompts and aligns the model’s response by itself to induce toxic responses. Extensive experimental results on two jailbreak benchmarks demonstrate that FITD achieves an average attack success rate of 94% across seven widely used models, outperforming existing state-of-the-art methods. Additionally, we provide an in-depth analysis of LLM self-corruption, highlighting vulnerabilities in current alignment strategies and emphasizing the risks inherent in multi-turn interactions. The code is available at https://github.com/Jinxiaolong1129/Foot-in-the-door-Jailbreak.

</details>

### 15. X-Teaming Evolutionary M2S: Automated Discovery of Multi-turn to Single-turn Jailbreak Templates

📄 [arXiv](https://arxiv.org/abs/2509.08729)　📅 2025-09　🏷 NeurIPS 2025 Workshop

**关键词**：`attack`、`M2S template`、`evolutionary search`、`attack distillation`

👤 **作者**：Hyunjun Kim、Junwoo Ha、Sangyoon Yu、Haon Park

- 🎯 **研究动机**：多轮转单轮越狱依赖少量手工模板，自动化探索缺失
- 🔬 **研究方法**：提出 X-Teaming Evolutionary M2S：语言模型引导进化发现并优化模板，12 源智能采样加 StrongREJECT 式 LLM 评审，阈值 0.70 保持选择压力
- 📌 **结论**：五代进化产生两个新模板族，GPT-4.1 上总成功率 44.8%（103/230）；结构增益跨模型迁移但差异大，prompt 长度与得分正相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn-to-single-turn (M2S) compresses iterative red-teaming into one structured prompt, but prior work relied on a handful of manually written templates. We present X-Teaming Evolutionary M2S, an automated framework that discovers and optimizes M2S templates through language-model-guided evolution. The system pairs smart sampling from 12 sources with an LLM-as-judge inspired by StrongREJECT and records fully auditable logs. Maintaining selection pressure by setting the success threshold to $θ= 0.70$, we obtain five evolutionary generations, two new template families, and 44.8% overall success (103/230) on GPT-4.1. A balanced cross-model panel of 2,500 trials (judge fixed) shows that structural gains transfer but vary by target; two models score zero at the same threshold. We also find a positive coupling between prompt length and score, motivating length-aware judging. Our results demonstrate that structure-level search is a reproducible route to stronger single-turn probes and underscore the importance of threshold calibration and cross-model evaluation. Code, configurations, and artifacts are available at https://github.com/hyunjun1121/M2S-x-teaming.

</details>

### 16. Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack

📄 [arXiv](https://arxiv.org/abs/2404.01833) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/russinovich)　📅 2025-08　🏷 USENIX Security 2025

**关键词**：`attack`、`multi-turn jailbreak`、`crescendo escalation`、`red teaming`

👤 **作者**：Mark Russinovich、Ahmed Salem、Ronen Eldan

- 🎯 **研究动机**：已有越狱依赖显式构造的对抗提示，未利用多轮看似良性的渐进交互绕过对齐
- 🔬 **研究方法**：Crescendo 从泛化提问开始，逐步引用模型自身回复升级对话直至越狱；Crescendomation 工具自动化该攻击
- 📌 **结论**：在 ChatGPT、Gemini、Llama-2/3、Anthropic Chat 上高 ASR；AdvBench 子集上比 SOTA 高 29-61%（GPT-4）与 49-71%（Gemini-Pro），并可越狱多模态模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have risen significantly in popularity and are increasingly being adopted across multiple applications. These LLMs are heavily aligned to resist engaging in illegal or unethical topics as a means to avoid contributing to responsible AI harms. However, a recent line of attacks, known as "jailbreaks'', seek to overcome this alignment. Intuitively, jailbreak attacks aim to narrow the gap between what the model can do and what it is willing to do. In this paper, we introduce a novel jailbreak attack called Crescendo. Unlike existing jailbreak methods, Crescendo is a simple multi-turn jailbreak that interacts with the model in a seemingly benign manner. It begins with a general prompt or question about the task at hand and then gradually escalates the dialogue by referencing the model's replies progressively leading to a successful jailbreak. We evaluate Crescendo on various public systems, including ChatGPT, Gemini Pro, Gemini-Ultra, LlaMA-2 70b and LlaMA-3 70b Chat, and Anthropic Chat. Our results demonstrate the strong efficacy of Crescendo, with it achieving high attack success rates across all evaluated models and tasks. Furthermore, we present Crescendomation, a tool that automates the Crescendo attack and demonstrate its efficacy against state-of-the-art models through our evaluations. Crescendomation surpasses other state-of-the-art jailbreaking techniques on the AdvBench subset dataset, achieving 29-61% higher performance on GPT-4 and 49-71% on Gemini-Pro. Finally, we also demonstrate Crescendo's ability to jailbreak multimodal models.

</details>

### 17. X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents

📄 [arXiv](https://arxiv.org/abs/2504.13203) · 🌐 [Project](https://x-teaming.github.io/) · 📝 [OpenReview](https://openreview.net/forum?id=gKfj7Jb1kj)　📅 2025-07　🏷 COLM 2025

**关键词**：`attack`、`multi-turn jailbreak`、`adaptive multi-agent`、`attacker-verifier loop`

👤 **作者**：Salman Rahman、…、Saadia Gabriel

- 🎯 **研究动机**：单一attacker在长对话中易失去攻击目标
- 🔬 **研究方法**：X-Teaming让规划、攻击与验证agent协作并按反馈调整策略
- 📌 **结论**：生成更强多轮jailbreak并产出XGuard-Train防御训练数据

### 18. Chain of Attack: Hide Your Intention through Multi-Turn Interrogation

🎓 [Official](https://aclanthology.org/2025.findings-acl.514/)　📅 2025-07　🏷 ACL 2025

**关键词**：`attack`、`multi-turn jailbreak`、`intent concealment`、`contextual interrogation`

👤 **作者**：Xikang Yang、Biyu Zhou、Xuehai Tang、Jizhong Han、Songlin Hu

- 🎯 **研究动机**：越狱攻击主要关注单轮对话，多轮对话场景的漏洞探索不足
- 🔬 **研究方法**：从审讯视角提出最优审讯原则隐藏越狱意图，用两种 LLM 定制审讯策略加审讯历史记录管理机制迭代生成攻击链 CoA
- 📌 **结论**：LLM 对多轮审讯抵抗力不足，ASR 83% 对比基线 64%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The latent knowledge of large language models (LLMs) contains harmful or unethical content, which introduces significant security risks upon their widespread deployment. Conducting jailbreak attacks on LLMs can proactively identify vulnerabilities to enhance their security measures. However, previous jailbreak attacks primarily focus on single-turn dialogue scenarios, leaving vulnerabilities in multi-turn dialogue contexts inadequately explored. This paper investigates the resilience of black-box LLMs in multi-turn jailbreak attack scenarios from a novel interrogation perspective. We propose an optimal interrogation principle to conceal the jailbreak intent and introduce a multi-turn attack chain generation strategy called CoA. By employing two effective interrogation strategies tailored for LLMs, coupled with an interrogation history record management mechanis, it achieves a significant optimization of the attack process. Our approach enables the iterative generation of attack chains, offering a powerful tool for LLM red team testing. Experimental results demonstrate that LLMs exhibit insufficient resistance under multi-turn interrogation, with our method shows more advantages(ASR, 83% vs 64%). This work offers new insights into improving the safety of LLMs.

</details>

### 19. Multi-Turn Jailbreaking via Attention Shifting

🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/34553)　📅 2025-04　🏷 AAAI 2025

**关键词**：`attack`、`multi-turn jailbreak`、`attention shifting`、`history fabrication`

- 🎯 **研究动机**：长对话历史会重新分配模型的安全注意力
- 🔬 **研究方法**：ASJA用遗传搜索构造连贯虚构历史并逐步转移注意力
- 📌 **结论**：比直接有害提问更易在多轮末端触发违规回答

### 20. Reasoning-Augmented Conversation for Multi-Turn Jailbreak Attacks on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.11054) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.929/)　📅 2025-02　🏷 EMNLP 2025

**关键词**：`attack`、`RACE`、`reasoning state machine`、`gain-guided exploration`

👤 **作者**：Zonghao Ying、…、Dacheng Tao

- 🎯 **研究动机**：多轮越狱难以兼顾语义连贯与攻击有效性，易漂移或被识破
- 🔬 **研究方法**：RACE 把有害查询重构为良性推理任务，用攻击状态机加增益引导探索、self-play 与拒绝反馈推进推理链
- 📌 **结论**：多 LLM 上达 SOTA，ASR 最高提升 96%；对 OpenAI o1 与 DeepSeek R1 分别达 82% 与 92%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks simulate real-world human interactions by engaging large language models (LLMs) in iterative dialogues, exposing critical safety vulnerabilities. However, existing methods often struggle to balance semantic coherence with attack effectiveness, resulting in either benign semantic drift or ineffective detection evasion. To address this challenge, we propose Reasoning-Augmented Conversation, a novel multi-turn jailbreak framework that reformulates harmful queries into benign reasoning tasks and leverages LLMs' strong reasoning capabilities to compromise safety alignment. Specifically, we introduce an attack state machine framework to systematically model problem translation and iterative reasoning, ensuring coherent query generation across multiple turns. Building on this framework, we design gain-guided exploration, self-play, and rejection feedback modules to preserve attack semantics, enhance effectiveness, and sustain reasoning-driven attack progression. Extensive experiments on multiple LLMs demonstrate that RACE achieves state-of-the-art attack effectiveness in complex conversational scenarios, with attack success rates (ASRs) increasing by up to 96%. Notably, our approach achieves ASRs of 82% and 92% against leading commercial models, OpenAI o1 and DeepSeek R1, underscoring its potency. We release our code at https://github.com/NY1024/RACE to facilitate further research in this critical domain.

</details>

### 21. LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts

📄 [arXiv](https://arxiv.org/abs/2410.10700v1) · 🎓 [Official](https://aclanthology.org/2025.acl-long.1207/)　📅 2024-10　🏷 ACL 2025

**关键词**：`attack`、`ActorAttack`、`actor-network clue`、`semantic distribution shift`

👤 **作者**：Qibing Ren、…、Jing Shao

- 🎯 **研究动机**：攻击 prompt 与原毒害 prompt 间的自然分布位移可绕过安全机制，未被系统利用
- 🔬 **研究方法**：ActorBreaker 依据 actor-network theory 挖掘与毒害内容关联的人与非人 actor，构造渐进式多轮 prompt
- 📌 **结论**：多样性、有效性与效率均超既有攻击；用其构造安全数据微调可提升鲁棒但有代价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety concerns in large language models (LLMs) have gained significant attention due to their exposure to potentially harmful data during pre-training. In this paper, we identify a new safety vulnerability in LLMs: their susceptibility to \textit{natural distribution shifts} between attack prompts and original toxic prompts, where seemingly benign prompts, semantically related to harmful content, can bypass safety mechanisms. To explore this issue, we introduce a novel attack method, \textit{ActorBreaker}, which identifies actors related to toxic prompts within pre-training distribution to craft multi-turn prompts that gradually lead LLMs to reveal unsafe content. ActorBreaker is grounded in Latour's actor-network theory, encompassing both human and non-human actors to capture a broader range of vulnerabilities. Our experimental results demonstrate that ActorBreaker outperforms existing attack methods in terms of diversity, effectiveness, and efficiency across aligned LLMs. To address this vulnerability, we propose expanding safety training to cover a broader semantic space of toxic content. We thus construct a multi-turn safety dataset using ActorBreaker. Fine-tuning models on our dataset shows significant improvements in robustness, though with some trade-offs in utility. Code is available at https://github.com/AI45Lab/ActorAttack.

</details>

### 22. RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking

📄 [arXiv](https://arxiv.org/abs/2409.17458) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.1311/)　📅 2024-09　🏷 ACL 2025

**关键词**：`attack`、`RED QUEEN`、`concealed intent`、`scenario generation`

👤 **作者**：Yifan Jiang、Kriti Aggarwal、Tanmay Laud、Kashif Munir、Jay Pujara、Subhabrata Mukherjee

- 🎯 **研究动机**：现有越狱是单轮显式恶意查询，无法覆盖伪装意图的多轮交互
- 🔬 **研究方法**：RED QUEEN ATTACK 构造以防害为伪装的多轮场景，40 个场景、14 类危害生成 56k 多轮攻击数据；配 RED QUEEN GUARD 对齐缓解
- 📌 **结论**：GPT-4o ASR 达 87.62%、Llama3-70B 达 75.4%，模型越大越易受害；GUARD 将 ASR 压至 1% 以下

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of Large Language Models (LLMs) has opened up new opportunities across various domains and applications; yet it also presents challenges related to potential misuse. To mitigate such risks, red teaming has been employed as a proactive security measure to probe language models for harmful outputs via jailbreak attacks. However, current jailbreak attack approaches are single-turn with explicit malicious queries that do not fully capture the complexity of real-world interactions. In reality, users can engage in multi-turn interactions with LLM-based chat assistants, allowing them to conceal their true intentions in a more covert manner. To bridge this gap, we, first, propose a new jailbreak approach, RED QUEEN ATTACK. This method constructs a multi-turn scenario, concealing the malicious intent under the guise of preventing harm. We craft 40 scenarios that vary in turns and select 14 harmful categories to generate 56k multi-turn attack data points. We conduct comprehensive experiments on the RED QUEEN ATTACK with four representative LLM families of different sizes. Our experiments reveal that all LLMs are vulnerable to RED QUEEN ATTACK, reaching 87.62% attack success rate on GPT-4o and 75.4% on Llama3-70B. Further analysis reveals that larger models are more susceptible to the RED QUEEN ATTACK, with multi-turn structures and concealment strategies contributing to its success. To prioritize safety, we introduce a straightforward mitigation strategy called RED QUEEN GUARD, which aligns LLMs to effectively counter adversarial attacks. This approach reduces the attack success rate to below 1% while maintaining the model's performance across standard benchmarks. Full implementation and dataset are publicly accessible at https://github.com/kriti-hippo/red_queen.

</details>

### 23. ASCII Attack: Recontextualising Harmful Requests as Artistic Critique in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.02215)　📅 2026-09

**关键词**：`attack`、`single-turn jailbreak`、`ASCII recontextualization`、`surface-form alignment`

👤 **作者**：Da Cheng Gu、Yifei Dong、Xinghao Yang、Yongshun Gong、Wei Liu

- 🎯 **研究动机**：安全对齐主要施加于表面形式，同一可执行内容仅改变模型的阅读方式即被弱覆盖
- 🔬 **研究方法**：提出黑盒单轮 ASCII Attack：把完全可读的有害请求嵌入 ASCII 艺术字、以艺术品身份征求反馈，要求以艺术评论形式回复；每个框架 prompt 配直接提问对照以隔离对比
- 📌 **结论**：11 个模型、8 类危害上 62% 的框架 prompt 被判有害（对照 42%），最易感模型上 93% 成功；效应随模型而非主题变化且不随规模减弱，与 mismatched generalisation 一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment trains large language models to refuse harmful requests stated plainly, but that training is applied mostly to surface form. Requests that only recontextualise the same operational content, changing how the model reads it, are therefore only weakly covered. The ASCII Attack is one such recontextualisation. It is single-turn and black-box: one message, with no access to model internals. It embeds a fully legible harmful request in ASCIl-art characters, presents it as artwork, and asks for feedback. Unlike ArtPrompt, it hides nothing: the request stays readable. The reply is written as artistic critique and can contain operational detail that a plain request would have been refused for. Every framed prompt is paired with a direct-question control, so the contrast is isolated from topic, model and decoding variation. The contrast identifies a bundled surface, not one isolated channel. Across eleven models and eight harm topics, a harm-aware classifier judges 62% of framed prompts harmful against 42% of controls. On the most susceptible model the framed prompt succeeds 93% of the time. A single query matches or exceeds published single-query attacks under four of five harm judges. The effect tracks the model more than the topic and does not diminish with scale. At least one judge dissents from the panel majority on nearly two-thirds of framed rows, which is itself a measurement-validity finding. That pattern is consistent with mismatched generalisation.

</details>

### 24. Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.18164)　📅 2026-08

**关键词**：`benchmark`、`attack`、`emoji augmentation`、`representation shift`、`guardrail gap`、`input representation`

👤 **作者**：M P V S Gopinadh

- 🎯 **研究动机**：LLM 安全评测几乎全用文本对抗 prompt，可能漏掉替代输入表示引发的漏洞
- 🔬 **研究方法**：以 emoji 增强提示为测试用例，50 条提示评四个开源 LLM 的鲁棒性差异
- 📌 **结论**：Gemma 2 9B 与 Mistral 7B 成功率 10%、Llama 3 8B 为 6%、Qwen 2 7B 完全抵抗（χ²=32.94，p<0.001）——鲁棒性对输入表示敏感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations of large language models (LLMs) predominantly rely on text-based adversarial prompts, potentially overlooking vulnerabilities arising from alternative input representations. This work examines emoji-augmented prompts as a test case for this gap, evaluating 50 prompts across four open-source LLMs (Mistral 7B, Qwen 2 7B, Gemma 2 9B, Llama 3 8B). Results show substantial variation in robustness: Gemma 2 9B and Mistral 7B exhibit non-zero success rates (10%), Llama 3 8B 6%, while Qwen 2 7B shows complete resistance (0% success rate). A chi-square test ($χ^2 = 32.94, p < 0.001$) confirms significant differences in outcome distributions. These findings indicate that robustness is sensitive to input representation, and that evaluations restricted to standard text prompts may underrepresent model vulnerabilities.

</details>

### 25. Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2608.09624)　📅 2026-08

**关键词**：`attack`、`jailbreak`、`uncertainty calibration`、`jailbreak prompting`

👤 **作者**：Mingyu Luo、…、Xiaoyan Sun

- 🎯 **研究动机**：内部安全分数按提示有害意图校准并被默认能捕获成功越狱，但越狱成功是后续生成结果，两者是不同对象
- 🔬 **研究方法**：Active Attention Probing 提供内容无关的固定测量坐标，把每个目标配对成原始与包装版本并生成真实补全，审计分数排序与越狱结果的关系
- 📌 **结论**：Llama 上包装使有害生成从 0.05 升至 0.27 而意图 AUROC 从 0.936 降至 0.803；包装有害提示中结果 AUROC 仅 0.220，成功攻击反而得分更低，三模型、七攻击族、双 judge 均复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Internal safety scores judge a prompt before any text is generated, and they are validated by how well they separate harmful prompts from benign ones. That separation is then read as evidence that the score will also catch the attacks that succeed. Harmful intent is a property of the prompt. Jailbreak success is an outcome produced later by a particular target model, decoding policy, and judge. A filter tuned on a score that measures the wrong quantity spends its false positive budget on attacks that would have failed anyway. In this paper we audit that inference. Attention based measurements are usually read from prompt dependent locations, so a wrapper changes both the content being judged and the place the signal is taken from. We therefore introduce Active Attention Probing, which supplies a fixed content independent measurement coordinate. We pair every base goal with a plain and a wrapped version and generate real completions from the target models. On Llama, wrapping raises harmful generation from 0.05 to 0.27 while harmful intent AUROC falls from 0.936 to 0.803, so the attacks grow more dangerous while the prompts look safer to the score. Among wrapped harmful prompts the outcome AUROC is 0.220, which places the attacks that succeeded below the attacks that failed. Rare token, passive, and detector derived channels reproduce the reversal on the same matched design, and the reversal itself persists across three target models, seven attack families, and two independent judges. Distribution shift then degrades calibration and threshold transfer before it degrades ranking.

</details>

### 26. Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.28153) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64633)　📅 2026-06　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`mechanistic analysis`、`jailbreak`、`safety alignment`、`prompt injection`

👤 **作者**：Yanchen Yin、Dongqi Han、Linghui Li

- 🎯 **研究动机**：越狱攻击如何绕过安全对齐的机制不明
- 🔬 **研究方法**：发现攻击不消除安全特征而是选择性抑制特定注意力头：早层的 Adversarially Compromised Heads（ACHs）被攻击模板 token 抑制，中层的 Safety-Aligned Heads（SAHs）在攻击成功时仍保持激活
- 📌 **结论**：消融证明因果性：抑制少量 ACH 即可在正常被拒输入诱发越狱行为；直接读取持续存在的有害激活（Robust Harmful Features）即可免训练获得强鲁棒的聚合检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. We identify two functionally differentiated types: Adversarially Compromised Heads (ACHs) concentrated in early layers, which are suppressed under attacks, and Safety-Aligned Heads (SAHs) in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support the causal role of ACHs and the contribution of SAHs to robust activations: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens, providing a mechanistic account of why attacks can bypass refusal decisions through ACH suppression while leaving internal safety signals sustained by SAHs -- a phenomenon we term Robust Harmful Features. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.

</details>

### 27. Breaking Safety at the Token Boundary: How BPE Tokenization Creates Exploitable Gaps in LLM Alignment

📄 [arXiv](https://arxiv.org/abs/2607.01239)　📅 2026-05

**关键词**：`attack`、`safety alignment`、`jailbreak prompting`、`refusal bypass`

👤 **作者**：Tung-Ling Li、Hongliang Liu、Yuhao Wu

- 🎯 **研究动机**：BPE 分词把安全关键词切成子词碎片，三个公开对齐数据集均无碎片化输入，字符级扰动可绕过对齐的机制未被端到端检验
- 🔬 **研究方法**：在五个模型家族上测试安全词碎片化链路：优化翻转首 token 拒绝触发、激活修补定位受扰层、扫描 3 万条对齐数据（碎片输入为零），并用 68 格 DPO/SFT 网格寻找修复
- 📌 **结论**：定向碎片化使 80-100% 被拒 HarmBench 提示翻转首 token 拒绝、48% 产生真实有害输出；SFT 碎片数据虽闭合 3/5 家族 ASR 但以全局崩塌（良性也拒绝）为代价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Character-level perturbations bypass safety alignment in modern LLMs despite leaving prompts human-readable. We identify and test a central structural mechanism: BPE tokenization fragments safety-critical words into sub-word pieces, and the three public alignment datasets we surveyed contain no intentionally fragmented inputs. The mechanism is a chain, tested end-to-end on five model families (Qwen-3-4B, Qwen-2.5-7B, Gemma-3-4B, Llama-3.1-8B, Mistral-7B). An optimization targeting safety-token fragmentation flips the first-token refusal trigger on 80-100% of refused HarmBench prompts, with 48% of those flips producing genuinely harmful outputs (per-model 29-65%; gap-vs-behavior ROC-AUC 0.66-0.98, pooled 0.84). Activation patching localizes the disrupted signal to the last ${\sim}30\%$ of layers; an alignment-data scan finds zero fragmented prompts among 30,000 examples (positive-control recall $\geq 99\%$ at attack-relevant intensities); and targeted-mutation experiments isolate safety words as the disruption locus. On the defense side, a 68-cell grid (55 trained checkpoints) shows that no DPO configuration achieves seed- and pool-stable ASR closure on the three families with closed pool-size confounds. SFT trained on fragmented prompts closes ASR on 3/5 families but only via global collapse that raises refusal on benign prompts as well, indicating the missing distribution is necessary but not sufficient under the LoRA-16 recipe we tested. To distinguish selective repair from global collapse, we introduce Conv-Benign, a candidate paired diagnostic. All ASR claims are 3-judge-calibrated (cell rankings stable across judges; absolute levels $\pm$18pp; see App.~B.13).

</details>

### 28. TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking

📄 [arXiv](https://arxiv.org/abs/2602.06440) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-02

**关键词**：`attack`、`history-guided RL`、`jailbreak`、`jailbreak prompting`、`black-box jailbreak`、`query efficiency`

👤 **作者**：Sung-Hoon Yoon、Ruizhi Qian、Minda Zhao、Weiyue Li、Mengyu Wang

- 🎯 **研究动机**：现有越狱方法未利用早前交互轮暴露的漏洞信号，攻击效率低且不稳定
- 🔬 **研究方法**：TrailBlazer 用基于注意力的重加权机制突出交互历史中的关键漏洞信号，指导 RL 越狱决策
- 📌 **结论**：在 AdvBench 与 HarmBench 上取得 SOTA 越狱成功率并显著提升查询效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have become integral to many domains, making their safety a critical priority. Prior jailbreaking research has explored diverse approaches, including prompt optimization, automated red teaming, obfuscation, and reinforcement learning (RL) based methods. However, most existing techniques fail to effectively leverage vulnerabilities revealed in earlier interaction turns, resulting in inefficient and unstable attacks. Since jailbreaking involves sequential interactions in which each response influences future actions, reinforcement learning provides a natural framework for this problem. Motivated by this, we propose a history-aware RL-based jailbreak framework that analyzes and reweights vulnerability signals from prior steps to guide future decisions. We show that incorporating historical information alone improves jailbreak success rates. Building on this insight, we introduce an attention-based reweighting mechanism that highlights critical vulnerabilities within the interaction history, enabling more efficient exploration with fewer queries. Extensive experiments on AdvBench and HarmBench demonstrate that our method achieves state-of-the-art jailbreak performance while significantly improving query efficiency. These results underscore the importance of historical vulnerability signals in reinforcement learning-driven jailbreak strategies and offer a principled pathway for advancing adversarial research on LLM safeguards.

</details>

### 29. Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation

📄 [arXiv](https://arxiv.org/abs/2605.24535) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65252)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`attack`、`adversarial robustness`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`

👤 **作者**：Luoyu Chen、…、Shui Yu

- 🎯 **研究动机**：现有安全 steering 属有监督方法、绑定静态有限训练集，面对演化中的分布外越狱失效
- 🔬 **研究方法**：提出零样本防御：经无监督潜方向发现从拒绝态有害请求激活外推模拟越狱激活，双层对抗训练学习势诱导 steering 场把越狱态推入拒绝区且不改良性输出
- 📌 **结论**：三个 LLM、六类经典越狱家族下攻击成功率多低于 5%，模拟越狱激活对真实越狱的子空间覆盖随训练扩大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak prompts can trigger harmful completions on aligned LLMs, In accordance, safety steering has been proposed: test-time activation interventions that steer jailbreak activations to trigger refusal while preserving benign utility. However, existing steering methods are fundamentally supervised and tied to a static, limited training set, whereas real jailbreaks evolve and are often out-of-distributed from the training set, leading to failures on unseen attacks. In this paper, we tackle this failure by developping a \emph{zero-shot} defense. Base on unsupervised latent direction discovery, we directly simulate jailbroken activations without any knowledge of jailbreak strategy. To build a defense mechnism upon this, we propose a bi-level adversarial training framework. In the inner step, we simulate diverse jailbroken activations by extrapolating from refusal state harmful-request activations via unsupervised latent direction discovery. In the outer step, we train a potential-induced steering field to push these adversarial jailbroken states into refusal regions while keeping benign unchanged. Across three LLMs and six classical jailbreak families, our method achieves strong defense with attack success rates mostly below 5%, and we analyzed the increasing subspace coverage of our simulated jailbroken activations on real jailbreaks throughout training, which helps explain the increasing robustness of our defense mechnism.

</details>

### 30. JailbreakScope: Interpreting Jailbreak Mechanism through Representation and Circuit Analyses

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/he-zeqing)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`analysis`、`LLM jailbreak`、`representation analysis`、`circuit analysis`

👤 **作者**：Zeqing He、…、Rui Zheng

- 🎯 **研究动机**：越狱底层机制不明：现有研究只看静态表示偏移或安全组件，未从电路失效到表示变化给出细粒度解释
- 🔬 **研究方法**：JailbreakScope 从表示（扭曲有害感知）与电路（影响安全生成电路）双视角追踪整个生成过程，覆盖 5 个主流 LLM 与 7 种越狱策略
- 📌 **结论**：越狱普遍放大强化肯定响应的组件、抑制拒答组件，把表示推向安全区；表示欺骗与电路激活偏移跨越狱与模型强相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) exhibit impressive performance but remain vulnerable to jailbreak attacks, where adversarial prompts are crafted to bypass safety alignments and elicit unexpected responses. Despite their prevalence, the underlying mechanisms that enable jailbreaks are still not well understood. Recent studies primarily focus on static representation shifts or on identifying components associated with generation safety. However, these studies neither explore diverse jailbreak patterns nor provide a fine-grained explanation from the failure of circuit to representation changes, leaving significant gaps in uncovering jailbreak mechanism. In this paper, we propose JailbreakScope, an interpretation framework that analyzes jailbreak mechanisms from both representation (how jailbreaks distort LLM's harmfulness perception) and circuit (how jailbreaks impact circuits that are important for generation safety) perspectives, tracking their evolution throughout the entire generation process. We conduct in-depth evaluations on 5 mainstream LLMs under 7 jailbreak strategies. Our evaluation reveals a general pattern that jailbreaks amplify components that reinforce affirmative responses while suppressing those producing refusal, which shifts representations towards safe regions, leading LLMs to provide responses instead of refusals. Moreover, we find a strong and consistent correlation between representation deception and circuit activation shift across diverse jailbreaks and multiple LLMs.

</details>

### 31. Activation-Guided Local Editing for Jailbreaking Attacks

🎓 [Official](https://aclanthology.org/2026.acl-long.801/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`representation intervention`

👤 **作者**：Jiecong Wang、…、Zhengtao Yu (余正涛)

- 🎯 **研究动机**：token 级越狱产生不连贯输入且迁移性差，prompt 级攻击缺可扩展性、依赖人工巧思
- 🔬 **研究方法**：提出两阶段框架 AGILE：一次性场景化生成上下文并改写恶意查询以遮蔽意图，再用 hidden state 信息指导细粒度编辑，把输入的内部表征从恶意拉向良性
- 📌 **结论**：取得 SOTA 攻击成功率，比最强基线最多高 37.74%，且对黑盒与大规模模型迁移性优异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) become indispensable assistants, they remain vulnerable to misuse. Jailbreaking is an essential adversarial technique for red-teaming models to uncover and patch security flaws. However, existing jailbreak methods suffer from significant limitations. Token-level jailbreak attacks often produce incoherent or unreadable inputs and exhibit poor transferability, while prompt-level attacks lack scalability and rely heavily on manual effort and human ingenuity. We propose AGILE, a concise and effective two-stage framework that combines the advantages of these approaches. The first stage performs a one-shot, scenario-based generation of context and rephrases the original malicious query to obscure its harmful intent. The second stage utilizes information from the model’s hidden states to guide fine-grained edits, effectively steering the model’s internal representation of the input from a malicious one toward a benign one. Extensive experiments demonstrate that AGILE achieves state-of-the-art Attack Success Rate, with gains of up to 37.74% over the strongest baseline, and AGILE exhibits excellent transferability to black-box and large-scale models. Our code is available at https://github.com/SELGroup/AGILE.

</details>

### 32. Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense

📄 [arXiv](https://arxiv.org/abs/2608.27945)　📅 2026-08

**关键词**：`defense`、`attack`、`intent-aligned retriever`、`cross-session risk`、`lightweight guard`、`cross-session decomposition`

👤 **作者**：Disen Liao、Yihan Wang、Freda Shi、Yaoliang Yu

- 🎯 **研究动机**：攻击者可把禁用目标拆成跨独立会话的良性子查询再重组，而这种 compositional safety risk 缺乏形式化刻画与防御
- 🔬 **研究方法**：形式化 compositional safety risk 并证明组合风险差距由允许子查询上的 excess loss 控制的条件迁移界；提出 22M 参数意图对齐检索器 IntentAlign-MiniLM 作为跨会话守卫
- 📌 **结论**：更大的 Qwen3/Gemma3 在固定分解—组合流水线下有害能力提升更高；IntentAlign-MiniLM 在留出意图检索上超过更大 embedding 模型，取得测试 guardrail 中最佳 learned-retriever harmful recall

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model's excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \href{https://github.com/liaodisen/Cross-Session-Decomposition-Attacks}{our GitHub repository}.

</details>

### 33. PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

📄 [arXiv](https://arxiv.org/abs/2608.23028)　📅 2026-08

**关键词**：`attack`、`psychological jailbreak`、`multi-turn persuasion`、`policy bypass`、`social persuasion`、`change of meaning`

👤 **作者**：Zeyu Feng、Qingyu Wu、Yuzhe Luo、Hua Cheng

- 🎯 **研究动机**：LLM 日益作为持续社交对话者部署于教育与医疗，而越狱研究多聚焦单轮 prompt 优化，心理学基础的多轮说服漏洞未被探索
- 🔬 **研究方法**：PsychJail 把社会心理学说服技术映射为 tactic-conditioned attack policy，每个攻击动作分解为 Change-of-Meaning 分析、策略选择与受害者可见消息，并以 trajectory RL 优化
- 📌 **结论**：四个对齐模型平均 ASR 达 87.3%，全面超过强单轮与多轮基线；进一步提炼出四种模型级易感指纹并解释跨模型迁移不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles-rationalist, credibility-driven, narrative-monoculture, and broadly persuadable-while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

</details>

### 34. Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services

📄 [arXiv](https://arxiv.org/abs/2608.17445)　📅 2026-08

**关键词**：`attack`、`defense`、`decomposition attack`、`unlinkable identity`、`stateful-defense limit`、`jailbreak prompting`

👤 **作者**：Bowen Sun、Zhengyue Zhao、Xiaogeng Liu、Yinzhi Cao、Chaowei Xiao

- 🎯 **研究动机**：分解攻击把有害任务拆成单个合法请求，攻击者用不可链接身份并在别处合并答案时有状态防御是否仍可止血未知
- 🔬 **研究方法**：证明无重试时安全-效用权衡完全取决于同能力良性请求的分组；有重试学习 Allow/Block 时该有用工作点消失；91 个可执行任务与 11,393 个能力匹配良性请求实验验证
- 📌 **结论**：1% 拒绝预算下全部十个策略（含精确请求-操作映射特权策略）要么拦不住要么超预算；未见任务族一次尝试 ASR 至少 99%、两次 100%——需身份链接、新身份成本等额外机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answers elsewhere, leaving no reliable grouping signal. We ask whether decomposition attacks can still be stopped under this setting. For a fixed attack strategy without retries, we prove that the achievable security and utility tradeoff depends entirely on how benign requests for the same capabilities are grouped. Persistent, recognizable groups permit a useful defense; fresh, indistinguishable groups do not. When attackers can retry and learn from Allow/Block decisions, this useful operating point disappears: the feedback reveals what passes but not whether a block was correct. Experiments on 91 executable tasks and 11,393 capability-matched benign requests support these results. Under a 1% denial cap for these requests and a 0.5% cap for unrelated background traffic, all ten tested policies, including one privileged policy with an exact request-to-operation map, either fail to stop attacks or exceed the budget. On defense-unseen task families, attack success is at least 99% after one attempt and 100% after two. Effective defenses therefore require additional evidence or mechanisms tied to grouping, such as reliable identity linkage, costs for fresh identities, or control over answer use.

</details>

### 35. Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance

📄 [arXiv](https://arxiv.org/abs/2605.00553) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64302)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`LLM jailbreak`、`contrastive learning`

👤 **作者**：Minchan Kwon、Sunghyun Baek、Minseo Kim、Jaemyung Yu、Dongyoon Han、Junmo Kim

- 🎯 **研究动机**：GFlowNet 做红队分布匹配有潜力，但训练不稳与模式坍缩严重，红队的不稳定奖励进一步加速坍缩
- 🔬 **研究方法**：Stable-GFN 以成对比较消除配分函数 Z 估计，配抗噪奖励的掩码方法与防乱语局部最优的 fluency stabilizer
- 📌 **结论**：保持 GFN 最优策略的同时训练更稳定，攻击性能与多样性在各种设定下全面占优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) Red-Teaming, which proactively identifies vulnerabilities of LLMs, is an essential process for ensuring safety. Finding effective and diverse attacks in red-teaming is important, but achieving both is challenging. Generative Flow Networks (GFNs) that perform distribution matching are promising methods, but they are notorious for training instability and mode collapse. In particular, unstable rewards in red-teaming accelerate mode collapse. We propose Stable-GFN (S-GFN), which eliminates partition function $Z$ estimation in GFN and reduces training instability. S-GFN avoids $Z$ estimation through pairwise comparisons and employs a robust masking methodology against noisy rewards. Additionally, we propose a fluency stabilizer to prevent the model from getting stuck in local optima that produce gibberish. S-GFN provides more stable training while maintaining the optimal policy of GFN. We demonstrate the overwhelming attack performance and diversity of S-GFN across various settings. Our code can be found in https://github.com/kmc0207/Stable-GFN.

</details>

### 36. One Word at a Time: Incremental Completion Decomposition Breaks LLM Safety

📄 [arXiv](https://arxiv.org/abs/2604.25921) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`attack`、`trajectory jailbreak`、`incremental completion`、`jailbreak`、`refusal suppression`

👤 **作者**：Samee Arif、Naihao Deng、Zhijing Jin、Rada Mihalcea

- 🎯 **研究动机**：LLM 对话安全机制存在可被轨迹式多轮攻击利用的弱点
- 🔬 **研究方法**：Incremental Completion Decomposition 先诱导模型对恶意请求做逐词接龙，再诱出完整回答；变体含模型生成或攻击者注入的中间续写及最终回复预填充
- 📌 **结论**：在 AdvBench、JailbreakBench、StrongREJECT 上 ASR 超现有方法；机理证据显示成功轨迹抑制拒答表征、激活偏离安全对齐状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are trained to refuse harmful requests, yet they remain vulnerable to jailbreak attacks that exploit weaknesses in conversational safety mechanisms. We introduce Incremental Completion Decomposition ICD, a trajectory-based jailbreak strategy that elicits a sequence of single-word continuations related to a malicious request before eliciting the full response. In addition, we propose ICD variants that use model-generated or attacker-injected intermediate continuations, as well as final-response prefilling. We evaluate these variants across a broad set of open-weight model families, demonstrating superior Attack Success Rate (ASR) on AdvBench, JailbreakBench, and StrongREJECT compared to existing methods. In addition, we provide a theoretical account of why ICD is effective and present mechanistic evidence that successful attack trajectories suppress refusal-related representations and shift activations away from safety-aligned states.

</details>

### 37. D-Judge: Disrupting Multi-Turn Jailbreaks using Semantics-Preserving Output Rewriting

📄 [arXiv](https://arxiv.org/abs/2606.02640) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65706)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`multi-turn jailbreak`、`jailbreak`、`jailbreak prompting`、`LLM jailbreak`

👤 **作者**：Huanli Gong、…、N. Benjamin Erichson

- 🎯 **研究动机**：多轮越狱利用辅助 judge 模型反馈迭代精炼提示；现有防御只检测单轮或最终回复，judge 驱动的精炼环完好无损
- 🔬 **研究方法**：D-Judge 在攻击者 judge 评估前语义保持地重写受害 LLM 回复使反馈信号失准；构建诱导不同 judge 有害度评分的语义等价响应对做 SFT 加 DPO
- 📌 **结论**：HarmBench 上降低 SOTA 多轮越狱成功率且保持良性基准性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks pose a growing threat to large language model (LLM) safety because they exploit feedback from auxiliary judge models to iteratively refine prompts toward harmful goals. Existing defenses largely detect or block unsafe content at individual turns or at the final response, leaving the judge-driven refinement loop intact and allowing attackers to extract informative feedback from intermediate interactions. We introduce D-Judge, a semantics-preserving output rewriting defense that intervenes directly in this loop by rewriting the victim LLM’s responses before they are evaluated by the attacker’s judge. By misaligning the judge’s feedback signal without changing the meaning of the original response, D-Judge derails the attacker’s prompt-refinement process, causing subsequent queries to be optimized against a distorted signal of attack progress. To improve D-Judge’s ability to produce such rewrites, we construct a dataset of semantically equivalent response pairs that induce different judge-assigned harmfulness scores, and use it for supervised fine-tuning followed by direct preference optimization. Experiments on HarmBench show that D-Judge reduces the success rate of state-of-the-art multi-turn jailbreaks while preserving performance on benign benchmarks.

</details>

### 38. Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study

📄 [arXiv](https://arxiv.org/abs/2608.27504)　📅 2026-08

**关键词**：`analysis`、`adversarial prompt propagation`、`circuit-level mechanism`、`safety constraint bypass`、`jailbreak circuit`、`subnetwork probing`

👤 **作者**：Paria Mehrbod、Boris Knyazev、Guy Wolf、Eugene Belilovsky、Geraldin Nanfack

- 🎯 **研究动机**：安全对齐 LLM 仍易被越狱，但其内部处理对抗 prompt、绕过安全约束的计算机制不清
- 🔬 **研究方法**：用 edge attribution patching 与 subnetwork probing 在 LLaMA-2-7B-chat 上定位生成越狱肯定回答的计算回路，并在首 token 预测阶段消融
- 📌 **结论**：消融可将 ASR 最多降低 80%，并揭示传播关键攻击 token、覆盖安全约束的 attention head 与 MLP pathway

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability.

</details>

### 39. Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance

📄 [arXiv](https://arxiv.org/abs/2608.23264)　📅 2026-08

**关键词**：`analysis`、`defense`、`implicit harmful request`、`task-framing shortcut`、`token safety boundary`、`LRP-guided decoding`

👤 **作者**：Or Biton、Tomer Krichli、Itai Allouche、Joseph Keshet

- 🎯 **研究动机**：helpfulness 与 harmlessness 双目标冲突导致对齐失败，模型在"请求帮助"式不道德场景中明显退化，机理不明
- 🔬 **研究方法**：以客观分类、主观第一人称、直接求助三种结构呈现不道德场景，用 LRP 追踪到归因偏差：模型更重视良性任务框架 token（如 Can you help me）而非标记不道德行为的 cue-token（如 without getting caught），并提出两种 LRP 引导解码把生成引向与 cue token 更相关的轨迹
- 📌 **结论**：干预促成更安全回应，支持 cue-token 归因不足是有害顺从成因的解释，token relevance 可作推理时防护信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective first-person statements, and direct requests for assistance. We find that model performance degrades in the request-for-assistance-based form. Using Layer-wise Relevance Propagation (LRP), we trace this discrepancy to an attribution bias: the model places greater emphasis on benign task-framing tokens (e.g., "Can you help me...") than on tokens signaling the underlying unethical behavior (e.g., "without getting caught"), which we term cue-tokens. We hypothesize that this under-attribution contributes to harmful compliance. To test this, we introduce two LRP-guided decoding methods that steer generation toward trajectories more relevant to cue tokens. Empirical evaluations show that these interventions promote safer responses, supporting cue-token attribution's role in compliance failures.

</details>

### 40. The Illusion of Cross-Lingual Safety in Low-Resource Languages

📄 [arXiv](https://arxiv.org/abs/2608.11146)　📅 2026-08

**关键词**：`analysis`、`safety alignment`、`cyber misuse`、`jailbreak prompting`

👤 **作者**：Abigail Oppong、…、Seid Muhie Yimam

- 🎯 **研究动机**：LLM 安全对齐以英语为主并假设可跨语言泛化，低资源语言下的迁移从未被检验
- 🔬 **研究方法**：LoDNA 数据集配对直译与文化本地化提示（Twi、Hausa、Amharic、Swahili），用潜几何框架探测隐层拒答表征而非仅看生成
- 📌 **结论**：有害提示在多数语言-模型对上保留不足 10% 的英语拒答信号；直译与本地化语义高度对齐（余弦 0.95-0.996）但概念未被路由到安全机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models (LLMs) is largely developed in English, assuming these safeguards generalize across multilingual settings. However, this assumption remains underexplored and exposes a vulnerability in low-resource languages. We investigate cross-lingual safety transfer in four African languages, Twi, Hausa, Amharic, and Swahili, using LoDNA, a new safety dataset that pairs literal translations with culturally localized prompts. To move beyond generation-based evaluation, we propose a latent geometric framework that probes hidden-state refusal representations in LLMs. Our experimental results show that cross-lingual safety transfer is severely limited; harmful prompts retain less than 10% of the English refusal signal across most language-model pairs. Literal and localized prompts are semantically aligned (cosine 0.95-0.996) but drift across layers, suggesting models encode the concepts without routing them to safety mechanisms. These findings demonstrate that current multilingual safety alignment is superficial, providing strong evidence against the assumption of a universal, language-agnostic harm manifold within the specific low-resource languages studied. Warning: This paper contains example data that may be offensive or harmful.

</details>

### 41. GPT-Red: Automated Red Teaming via Self-Play at Scale

📄 [arXiv](https://arxiv.org/abs/2607.26115)　📅 2026-07

**关键词**：`analysis`、`prompt injection`、`adversarial robustness`、`jailbreak prompting`

👤 **作者**：Eric Wallace、…、Kai Chen

- 🎯 **研究动机**：需要评估并提升生产系统对 prompt injection 的鲁棒性，人工红队覆盖不足
- 🔬 **研究方法**：训练 GPT-Red 自动红队 agent：自博弈算法让模型攻击同时训练的多样防守 agent 群体，在真实红队环境上以最大规模 RL 后训练算力训练，并用其对抗训练 GPT-5.6
- 📌 **结论**：GPT-Red 可靠攻破至 GPT-5.5 为止的模型、发现多于人类红队的攻击并泛化到留出环境与防守模型；GPT-5.6 成为迄今对 prompt injection 最鲁棒的模型，红队-防守形成自我改进飞轮

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to prompt injections to date. To create GPT-Red, we design a scalable self-play algorithm where the model is tasked with attacking a diverse population of simultaneously-trained defender agents. We train the model on realistic red-teaming environments using compute on the same scale as some of our largest RL post-training runs, making it the single-largest LLM safety training run ever documented. GPT-Red excels at red-teaming: it reliably breaks our past models up to GPT-5.5, it finds more successful attacks than human red-teamers, and it generalizes to held-out environments, defender models, and harnesses. In the future, we expect that as we improve the robustness of each new GPT model, it will in turn will provide better learning signal for \textit{even stronger} red-teamer agents, thus unlocking a self-improvement flywheel.

</details>

### 42. Red Teaming Large Reasoning Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1034/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`reasoning safety`、`jailbreak prompting`、`refusal bypass`、`automated red teaming`、`LLM jailbreak`

👤 **作者**：Jiawei Chen、…、Zhaoxia Yin

- 🎯 **研究动机**：LRM 带来 CoT 劫持与提示诱发低效等新风险，现有评测方法未充分覆盖
- 🔬 **研究方法**：提出基准 Rt-LRM，从真实性、安全性、效率三维度并引入训练范式视角评估可信度，含 30 个推理任务并评测 26 个模型
- 📌 **结论**：LRM 普遍存在可信度挑战，面对推理诱发风险时比一般 LLM 更脆弱，揭示此前未被充分探索的漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have emerged as a powerful advancement in multi-step reasoning tasks, offering enhanced transparency and logical consistency through explicit chains of thought (CoT). However, these models introduce novel safety and reliability risks, such as CoT-hijacking and prompt-induced inefficiencies, which are not fully captured by existing evaluation methods. To address this gap, we propose Rt-LRM, a unified benchmark designed to assess the trustworthiness of LRMs. Rt-LRM evaluates three core dimensions: truthfulness, safety and efficiency. Beyond metric-based evaluation, we further introduce the training paradigm as a key analytical perspective to investigate the systematic impact of different training strategies on model trustworthiness. We achieve this by designing a curated suite of 30 reasoning tasks from an observational standpoint. We conduct extensive experiments on 26 models and identify several valuable insights into the trustworthiness of LRMs. For example, LRMs generally face trustworthiness challenges and tend to be more fragile than Large Language Models (LLMs) when encountering reasoning-induced risks. These findings uncover previously underexplored vulnerabilities and highlight the need for more targeted evaluations. In addition, we release a scalable toolbox for standardized trustworthiness research to support future advancements in this important field.

</details>

### 43. RedCoder: Automated Multi-Turn Red Teaming for Code LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1531/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`automated red teaming`、`jailbreak prompting`、`refusal bypass`、`cybersecurity`、`LLM jailbreak`

👤 **作者**：Wenjie Jacky Mo、…、Muhao Chen

- 🎯 **研究动机**：Code LLM 在对抗设定下会生成漏洞代码，现有红队依赖大量人力且忽略真实编程的多轮交互特性
- 🔬 **研究方法**：提出 RedCoder：多智能体博弈模拟对抗交互产生原型对话与可复用攻击策略库，微调 LLM 作为骨干，部署后多轮对话中动态检索策略诱导漏洞代码
- 📌 **结论**：在多个 Code LLM 上诱导漏洞代码的能力超过既有单轮与多轮红队方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) for code generation (i.e., Code LLMs) have demonstrated impressive capabilities in AI-assisted software development and testing. However, recent studies have shown that these models are prone to generating vulnerable or even malicious code under adversarial settings. Existing red-teaming approaches rely on extensive human effort, limiting their scalability and practicality, and generally overlook the interactive nature of real-world AI-assisted programming, which often unfolds over multiple turns. To bridge these gaps, we present RedCoder, a red-teaming agent that engages victim models in multi-turn conversation to elicit vulnerable code. The pipeline to construct RedCoder begins with a multi-agent gaming process that simulates adversarial interactions, yielding a set of prototype conversations and an arsenal of reusable attack strategies. We then fine-tune an LLM on these prototype conversations to serve as the backbone of RedCoder. Once deployed, RedCoder autonomously engages Code LLMs in multi-turn conversations, dynamically retrieving relevant strategies from the arsenal to steer the dialogue toward vulnerability-inducing outputs. Experiments across multiple Code LLMs show that our approach outperforms prior single-turn and multi-turn red-team methods in inducing vulnerabilities in code generation, offering a scalable and effective tool for evaluating the security boundaries of modern code-generation systems.

</details>

### 44. Red-Bandit: Test-Time Adaptation for LLM Red-Teaming via Bandit-Guided LoRA Experts

🎓 [Official](https://aclanthology.org/2026.acl-long.2156/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`automated red teaming`、`LLM jailbreak`

👤 **作者**：Christos Ziakas、Nicholas Loo、Nishita Jain、Alessandra Russo

- 🎯 **研究动机**：自动化红队测试缺乏在推理时高效适配目标模型特有漏洞的机制
- 🔬 **研究方法**：提出 Red-Bandit：用 RL 后训练针对不同攻击风格（操纵、俚语等）的 LoRA 专家，推理时多臂老虎机策略按目标响应安全性动态选择专家
- 📌 **结论**：在 AdvBench 与 HarmBench 上于充分探索预算（ASR@10）下取得更高攻击成功率且提示更可读，bandit 策略还可诊断模型特有漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated red-teaming has emerged as a scalable approach for auditing Large Language Models (LLMs) prior to deployment, yet existing approaches lack mechanisms to efficiently adapt to model-specific vulnerabilities at inference. We introduce Red-Bandit, a red-teaming framework that adapts online to identify and exploit model failure modes under distinct attack styles (e.g., manipulation, slang). Red-Bandit post-trains a set of parameter-efficient LoRA experts, each specialized for a particular attack style, using reinforcement learning that rewards the generation of unsafe prompts via a rule-based safety model. At inference, a multi-armed bandit policy dynamically selects among these attack-style experts based on the target model’s response safety, balancing exploration and exploitation. Red-Bandit outperforms state-of-the-art methods on AdvBench and HarmBench, achieving higher attack success rates under sufficient exploration budgets (ASR@10), while generating more human-readable adversarial prompts (lower perplexity). In addition, Red-Bandit’s bandit policy serves as a diagnostic tool for identifying model-specific vulnerabilities by indicating which attack styles most effectively elicit harmful behaviors.

</details>

### 45. Learning to Conceal Risk: Controllable Multi-turn Red Teaming for LLMs in the Financial Domain

🎓 [Official](https://aclanthology.org/2026.acl-long.1903/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`financial AI`、`jailbreak prompting`、`refusal bypass`、`automated red teaming`、`LLM jailbreak`

👤 **作者**：Gang Cheng、Haibo Jin、Wenbin Zhang、Haohan Wang、Jun Zhuang

- 🎯 **研究动机**：红队研究重显性有害内容，忽视表面合法却诱发监管违规响应的金融域攻击
- 🔬 **研究方法**：CoRT 黑盒多轮框架：Risk Concealment Attacker 迭代精化提示，Risk Concealment Controller 预测轮级隐藏分数引导追问风格；构建 FinRisk-Bench（522 指令、六类风险）
- 📌 **结论**：九个 LLM 上 RCA 平均 ASR 93.19%，加 RCC 提升至 95.00%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in finance, where unsafe behavior can lead to serious regulatory risks. However, most red-teaming research focuses on overtly harmful content and overlooks attacks that appear legitimate on the surface yet induce regulatory-violating responses. We address this gap by introducing a controllable black-box multi-turn risk-concealed redteaming framework (CoRT) that progressively conceals surface-level risk while exploiting regulatory-violating behaviors. CoRT contains two key components: (i) a Risk Concealment Attacker (RCA) that generates multiturn prompts via iterative refinement, and (ii) a Risk Concealment Controller (RCC) that predicts a turn-level Risk Concealment Score (RCS) to steer RCA’s follow-up style. We also build a domain-specific benchmark, FinRisk-Bench, with 522 instructions spanning six financial risk categories. Experiments on nine widely used LLMs show that CoRT (RCA) achieves 93.19% average attack success rate (ASR), and CoRT (RCA+RCC) further improves the average ASR to 95.00%. Our code and FinRisk-Bench are available at https://github.com/gcheng128/CoRT.

</details>

### 46. Embracing Anisotropy: Turning Massive Activations into Interpretable Control Knobs for Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1380/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`representation intervention`、`runtime safety`

👤 **作者**：Youngji Roh、Hyunjin Cho、Jaehyung Kim

- 🎯 **研究动机**：LLM 内部表征高度各向异性（massive activations），先前工作视其为需管理的伪影，其功能意义不明
- 🔬 **研究方法**：免训练幅值准则识别 Domain-Critical Dimensions，发现其充当符号与量化模式或领域术语的可解释语义检测器；Critical Dimension Steering 只对这些维度做激活引导
- 📌 **结论**：在域适应与越狱场景超越常规全维度引导

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) exhibit highly anisotropic internal representations, often characterized by massive activations, a phenomenon where a small subset of feature dimensions possesses magnitudes significantly larger than the rest. While prior works view these extreme dimensions primarily as artifacts to be managed, we propose a distinct perspective: these dimensions serve as intrinsic interpretable functional units arising from domain specialization. Specifically, we propose a simple magnitude-based criterion to identify Domain-Critical Dimensions in a training-free manner. Our analyses reveal that such dimensions behave as interpretable semantic detectors for symbolic/quantitative patterns or domain-specific terms. In addition, we introduce Critical Dimension Steering, which applies activation steering exclusively to the identified dimensions. Empirical results show that this approach outperforms conventional whole-dimension steering in domain adaptation and jailbreaking scenarios.

</details>

### 47. Adaptive Instruction Composition for Automated LLM Red-Teaming

🎓 [Official](https://aclanthology.org/2026.acl-long.2174/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`automated red teaming`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`attack transferability`

👤 **作者**：Jesse Zymet、Andy Luo、Swapnil Shinde、Sahil Wadhwa、Emily Chen

- 🎯 **研究动机**：攻击者 LLM 自行试错发现的越狱语义范围有限，随机组合众包查询与战术又不保有效
- 🔬 **研究方法**：提出 Adaptive Instruction Composition：用 RL（轻量神经 contextual bandit 以对比嵌入为输入）在指令组合空间联合优化有效性与多样性，引导攻击者生成针对目标弱点的多样攻击
- 📌 **结论**：在有效性与多样性指标上大幅超过随机组合（含模型迁移设定），并在 HarmBench 上超过多种近期自适应方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many approaches to LLM red-teaming leverage an attacker LLM to discover jailbreaks against a target. Several of them task the attacker with identifying effective strategies through trial and error, resulting in a semantically limited range of successes. Another approach discovers diverse attacks by combining crowdsourced harmful queries and tactics into instructions for the attacker, but does so at random, limiting effectiveness. This article introduces a novel framework, Adaptive Instruction Composition, that combines crowdsourced texts according to an adaptive mechanism trained to jointly optimize effectiveness with diversity. We use reinforcement learning to balance exploration with exploitation in a combinatorial space of instructions to guide the attacker toward diverse generations tailored to target vulnerabilities. We demonstrate that our approach substantially outperforms random combination on a set of effectiveness and diversity metrics, even under model transfer. Further, we show that it surpasses a host of recent adaptive approaches on Harmbench. We employ a lightweight neural contextual bandit that adapts to contrastive embedding inputs, and provide ablations suggesting that the contrastive pretraining enables the network to rapidly generalize and scale to the massive space as it learns.

</details>

### 48. AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software

📄 [arXiv](https://arxiv.org/abs/2509.16861) · 🌐 [Project](https://doi.org/10.1109/ASE63991.2025.00279)　📅 2025-09　🏷 ASE 2025

**关键词**：`analysis`、`jailbreak`、`jailbreak prompting`、`refusal bypass`

👤 **作者**：Rui Yang、Michael Fu、Chakkrit Tantithamthavorn、Chetan Arora、Gunel Gulmammadova、Joey Chua

- 🎯 **研究动机**：静态护栏面对未见越狱攻击性能骤降，可低至 12%
- 🔬 **研究方法**：提出 AdaptiveGuard：把新越狱攻击当 OOD 输入检测，并以持续学习框架在线学习防御新威胁
- 📌 **结论**：OOD 检测精度 96%，两步更新即适应新攻击，适应后域内 F1 保留超 85%，优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrails are critical for the safe deployment of Large Language Models (LLMs)-powered software. Unlike traditional rule-based systems with limited, predefined input-output spaces that inherently constrain unsafe behavior, LLMs enable open-ended, intelligent interactions--opening the door to jailbreak attacks through user inputs. Guardrails serve as a protective layer, filtering unsafe prompts before they reach the LLM. However, prior research shows that jailbreak attacks can still succeed over 70% of the time, even against advanced models like GPT-4o. While guardrails such as LlamaGuard report up to 95% accuracy, our preliminary analysis shows their performance can drop sharply--to as low as 12%--when confronted with unseen attacks. This highlights a growing software engineering challenge: how to build a post-deployment guardrail that adapts dynamically to emerging threats? To address this, we propose AdaptiveGuard, an adaptive guardrail that detects novel jailbreak attacks as out-of-distribution (OOD) inputs and learns to defend against them through a continual learning framework. Through empirical evaluation, AdaptiveGuard achieves 96% OOD detection accuracy, adapts to new attacks in just two update steps, and retains over 85% F1-score on in-distribution data post-adaptation, outperforming other baselines. These results demonstrate that AdaptiveGuard is a guardrail capable of evolving in response to emerging jailbreak strategies post deployment. We release our AdaptiveGuard and studied datasets at https://github.com/awsm-research/AdaptiveGuard to support further research.

</details>

### 49. Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2501.16534) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-01　🏷 SaTML 2026

**关键词**：`attack`、`safety-boundary extraction`、`surrogate classifier`、`jailbreak transfer`、`safety classifier`、`surrogate extraction`

👤 **作者**：Jean-Charles Noirot Ferrand、Yohan Beugin、Eric Pauley、Ryan Sheatsley、Patrick McDaniel

- 🎯 **研究动机**：对齐在 LLM 内嵌入决定拒答与否的安全分类器，能否提取该分类器未被研究
- 🔬 **研究方法**：从 LLM 子集构建候选代理分类器，评估其与安全分类器的一致性并攻击候选测迁移率
- 📌 **结论**：仅 20% 架构即达 80% 以上 F1 一致；用 50% Llama-2 的代理攻击 ASR 达 70%，远超直接攻击的 22%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment in large language models (LLMs) is used to enforce guidelines such as safety. Yet, alignment fails in the face of jailbreak attacks that modify inputs to induce unsafe outputs. In this paper, we introduce and evaluate a new technique for jailbreak attacks. We observe that alignment embeds a safety classifier in the LLM responsible for deciding between refusal and compliance, and seek to extract an approximation of this classifier: a surrogate classifier. To this end, we build candidate classifiers from subsets of the LLM. We first evaluate the degree to which candidate classifiers approximate the LLM's safety classifier in benign and adversarial settings. Then, we attack the candidates and measure how well the resulting adversarial inputs transfer to the LLM. Our evaluation shows that the best candidates achieve accurate agreement (an F1 score above 80%) using as little as 20% of the model architecture. Further, we find that attacks mounted on the surrogate classifiers can be transferred to the LLM with high success. For example, a surrogate using only 50% of the Llama 2 model achieved an attack success rate (ASR) of 70% with half the memory footprint and runtime -- a substantial improvement over attacking the LLM directly, where we only observed a 22% ASR. These results show that extracting surrogate classifiers is an effective and efficient means for modeling (and therein addressing) the vulnerability of aligned models to jailbreaking attacks. The code is available at https://github.com/jcnf0/targeting-alignment.

</details>

### 50. SoK: Intent-Oriented Systematization of Multi-Turn LLM Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2608.01117)　📅 2026-08

**关键词**：`survey`、`multi-turn jailbreak`、`jailbreak`、`adversarial robustness`

👤 **作者**：Siyuan Li、…、Dacheng Tao

- 🎯 **研究动机**：多轮越狱被当作松散的 prompt 模式集合，缺少对攻击者如何跨轮组织推进有害意图的结构化分析
- 🔬 **研究方法**：提出四部分意图导向分类法组织多轮越狱，并通过受控消融度量意图组织方式对攻击有效性与可检测层级的影响
- 📌 **结论**：攻击有效性取决于意图跨轮的组织程度而非上下文长度或查询数；意图组织把检测面从轮级推到会话乃至跨会话级，轮内安全机制结构性不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in interactive settings, where user intent commonly unfolds through multi-turn dialogue. Multi-turn jailbreaks exploit this pattern by advancing a harmful intent across turns, so that no single message exposes the full objective. However, existing work treats these attacks as a loose collection of prompt patterns and does not analyze how the adversary organizes and advances harmful intent across an interaction. We develop a four-part, intent-oriented taxonomy that organizes multi-turn jailbreaks by adversarial intent structure. Through controlled ablations, we find that effectiveness is driven by how deliberately intent is organized across turns rather than by context length or query count. We further show that the way intent is organized determines the level at which it becomes detectable, pushing the required detection surface outward from the turn level to the session level to the cross-session level. These findings indicate that turn-local safety mechanisms are structurally insufficient and that single-point evaluation overlooks how intent is organized, motivating evaluation protocols aligned to the level at which harmful intent becomes observable. The code is available at: https://github.com/SiyuanLi00/INTACT.

</details>

### 51. Pragmatic Attack Surface: Vulnerabilities of Implicit Context in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.09551)　📅 2026-08

**关键词**：`attack`、`safety alignment`、`cyber misuse`、`jailbreak prompting`

👤 **作者**：Bocheng Chen、…、Guangliang Liu

- 🎯 **研究动机**：现有攻击依赖 prompt 显式语言线索可被安全对齐缓解，而人类语言依赖语用学隐式上下文（世界知识、社会规范），与安全对齐存在根本错配
- 🔬 **研究方法**：定义语用攻击面并利用隐式上下文构造攻击，在多开源与闭源模型上评测
- 📌 **结论**：该方法在各模型上的攻击成功率大幅超越基线攻击方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the era of large language models (LLMs), attackers often manipulate natural language to elicit unsafe or harmful outputs, creating a new natural language attack surface unique to LLM-based systems, where attacks directly exploit explicit linguistic cues in user prompts to bypass the safety mechanism of LLMs. However, such attacks can often be mitigated by existing safety alignment algorithms. On the other hand, human language is inherently grounded in pragmatics, necessitating typical context to interpret language, e.g., world knowledge, social norms. However, such contexts are often implicit because they are not directly expressed in human language and are not sufficiently leveraged in safety alignment, creating a fundamental mismatch between human language interpretation and safety alignment approaches. In this paper, we demonstrate that this mismatch exposes vulnerabilities in LLMs. We refer to this vulnerability as the pragmatic attack surface, which can be exploited to achieve high attack success rates. The experimental results demonstrate that our proposed approach outperforms baseline attack methods across various open-source and closed-source models by a substantial margin.

</details>

### 52. Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1209/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`defense`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`runtime safety`

👤 **作者**：Wai Man Si、Mingjie Li、Michael Backes、Yang Zhang

- 🎯 **研究动机**：SFT/RLHF 只鼓励偏好响应，未显式移除触发有害输出的不安全子网络
- 🔬 **研究方法**：免梯度归因直接识别并剪除不安全行为相关参数，GPU 需求低，跨架构与量化变体泛化
- 📌 **结论**：不安全生成大幅减少、越狱鲁棒性提升且效用损失极小；类比彩票假设，模型存在可剪除的 unsafe tickets 与保留性能的 safety tickets

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning models are increasingly deployed in real-world applications, but even aligned models such as Mistral and LLaVA still exhibit unsafe behaviors inherited from pre-training. Current alignment methods like SFT and RLHF primarily encourage models to generate preferred responses, but do not explicitly remove the unsafe subnetworks that trigger harmful outputs. In this work, we introduce a resource-efficient pruning framework that directly identifies and removes parameters associated with unsafe behaviors while preserving model utility. Our method employs a gradient-free attribution mechanism, requiring only modest GPU resources, and generalizes across architectures and quantized variants. Empirical evaluations on ML models show substantial reductions in unsafe generations and improved robustness against jailbreak attacks, with minimal utility loss. From the perspective of the Lottery Ticket Hypothesis, our results suggest that ML models contain “unsafe tickets” responsible for harmful behaviors, and pruning reveals “safety tickets” that maintain performance while aligning outputs. This provides a lightweight, post-hoc alignment strategy suitable for deployment in resource-constrained settings.

</details>

### 53. Profiling the Irrational Agent: Cognitive Modeling of LLM Behaviors in Sequential Jailbreaks

🎓 [Official](https://icml.cc/virtual/2026/poster/64559)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`

👤 **作者**：Xikang Yang、Biyu Zhou、Xuehai Tang、Jizhong Han、Songlin Hu

- 🎯 **研究动机**：安全评测多基于结果，不洞察导致不安全顺从的潜在决策过程
- 🔬 **研究方法**：Contextual Iowa Gambling Task 结合 Generalized Rescorla-Wagner 架构，把 LLM 行为分解为可测认知机制
- 📌 **结论**：序列脆弱性不取决于规模而源于乐观偏差学习、奖励放大与选择惯性的交互；反事实反馈与遗憾、权威、威胁框架显著加速从拒答到顺从

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in high-stakes settings, yet they remain vulnerable to sequential jailbreaks that exploit multi-turn interaction to circumvent safety mechanisms. Current safety evaluations are largely outcome-based, offering little insight into the latent decision processes that lead to unsafe compliance. We propose an interpretable cognitive modeling framework that couples a controlled elicitation paradigm, the Contextual Iowa Gambling Task (C-IGT), with a Generalized Rescorla--Wagner (GRW) architecture to decompose behavior into measurable mechanisms. Across a diverse set of mainstream LLMs, we find that sequential vulnerability is not explained by scale alone but emerges from interactions among cognitive factors, including optimism-biased learning, perceptual reward amplification, and choice inertia. Moreover, counterfactual feedback and psychologically framed rewards (e.g., regret, authority, threat) substantially accelerate the transition from refusal to compliance. These results yield principled cognitive profiles of LLM "irrationality" and provide insights for interdisciplinary research on LLM agents at the intersection of machine learning and human behavioral science.

</details>

### 54. ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System

🎓 [Official](https://aclanthology.org/2026.acl-long.1985/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`analysis`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`automated red teaming`

👤 **作者**：Jiacheng Liang、…、Charith Peris

- 🎯 **研究动机**：RLHF 中不完美奖励模型是单点故障；现有红队只针对 policy 层弱点，忽视核心 LLM 与 RM 同时失效的系统性弱点
- 🔬 **研究方法**：ARES 用 Safety Mentor 组合主题、人设、战术、目标生成语义连贯的对抗提示及对应恶意与安全回复，同时暴露 LLM 与 RM 弱点；两阶段修复：先微调 RM 再用其优化核心模型
- 📌 **结论**：多个对抗安全基准上大幅增强安全鲁棒性且保留模型能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) is central to aligning Large Language Models (LLMs), yet it introduces a critical vulnerability: an imperfect Reward Model (RM) can become a single point of failure when it fails to penalize unsafe behaviors. While existing red-teaming approaches primarily target policy-level weaknesses, they overlook what we term systemic weaknesses cases where both the core LLM and the RM fail in tandem.We present ARES, a framework that systematically discovers and mitigates such dual vulnerabilities. ARES employs a “Safety Mentor” that dynamically composes semantically coherent adversarial prompts by combining structured component types (topics, personas, tactics, goals) and generates corresponding malicious and safe responses. This dual-targeting approach exposes weaknesses in both the core LLM and the RM simultaneously. Using the vulnerabilities gained, ARES implements a two-stage repair process: first fine-tuning the RM to better detect harmful content, then leveraging the improved RM to optimize the core model. Experiments across multiple adversarial safety benchmarks demonstrate that ARES substantially enhances safety robustness while preserving model capabilities, establishing a new paradigm for comprehensive RLHF safety alignment.

</details>

### 55. A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families

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

### 56. NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

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

### 57. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution

📄 [arXiv](https://arxiv.org/abs/2608.27439)　📅 2026-08

**关键词**：`attack`、`automated red team`、`attack-skill evolution`、`cross-harness transfer`、`self-evolving red team`、`attack skill`

👤 **作者**：Junjie Zhang、Hui Liu、Kecheng Chen、Xianbo Mo、Changsheng Chen、Haoliang Li

- 🎯 **研究动机**：自动红队多依赖固定攻击，agentic 攻击者的轨迹检索受检索偏差与工具贡献不清影响，全轨迹还增加上下文开销并降低可解释性
- 🔬 **研究方法**：提出 RedEvoAgent 黑盒红队 Agent，把跨案例攻击轨迹蒸馏为简洁可读的攻击 skill，经工具效果画像、Deciding-Tool Attribution 与只保留有效更新的 validation ratchet 驱动 skill 演化
- 📌 **结论**：在多 benchmark、目标模型与执行 harness 上超越固定与 agentic 基线，提升工具效率，并可零调整跨攻击者模型与目标 harness 迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit, and full trajectories add context overhead while reducing interpretability. We propose RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill. The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses.

</details>

### 58. JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills

📄 [arXiv](https://arxiv.org/abs/2608.16465)　📅 2026-08

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`

👤 **作者**：Xiaoyu Wen、…、Qiaosheng Zhang

- 🎯 **研究动机**：自动红队的攻击策略散落于 prompt 与工作流，难以系统整合、复用与规模化改进
- 🔬 **研究方法**：JailbreakSkill 把攻击策略打包为模块化 agent 技能、可跨任务与目标模型自适应选择，并用攻击经验诊断、精炼、组合与发现新技能回流技能库
- 📌 **结论**：宏平均 ASR 在 AdvBench 升 17.5 个百分点、HarmBench 升 13.4 个百分点（对 GPT-5.4 达 48.6 个点增益），部分演化技能零适配泛化到未见 prompt 与模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated red-teaming has produced a growing collection of attack strategies, yet they typically remain scattered across prompts and workflows, making them difficult to systematically integrate, reuse, and improve at scale. We introduce \textsc{JailbreakSkill}, a skill-centric framework for scaling automated red-teaming through reusable and continuously evolving attack capabilities. \textsc{JailbreakSkill} packages existing attack strategies into modular, agent-ready skills that can be directly reused and adaptively selected across tasks and target models. Beyond reuse, it closes the loop between attacking and learning: attack experience is used to diagnose, refine, combine, and discover new skills, which are added back to an ever-growing skill library. This evolution lifts macro-average ASR by 17.5 percentage points on AdvBench and 13.4 points on HarmBench, including a 48.6-point gain against GPT-5.4 on AdvBench, while yielding novel attack strategies such as reframing a direct request as an unfinished document-completion task. Several evolved skills also generalize to unseen prompts and target models without further adaptation. Our code is available at https://github.com/BattleWen/JailbreakSkill.

</details>

### 59. ToxiPrompt: A Two-Stage Red-Teaming Approach for Balancing Adversarial Prompt Diversity and Response Toxicity

🎓 [Official](https://aclanthology.org/2026.eacl-long.170/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`automated red teaming`、`prompt diversity`、`elicited toxicity`、`adversarial diversity`、`response toxicity`

👤 **作者**：Seungho Lee、Kyumin Lee

- 🎯 **研究动机**：自动化红队面临多样性与毒性的权衡：提升 prompt 多样性常降低诱出毒性，毒性最大化则使多样性坍缩
- 🔬 **研究方法**：提出 ToxiPrompt 两阶段框架：显式分离探索（多样性）与利用（毒性），再以统一选择准则融合平衡两者
- 📌 **结论**：毒性与多样性的调和均值较最佳基线提升 14.6%；在 Llama-2/3、Qwen、Mistral 上免重调最高提升 55%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While large language models (LLMs) offer great promise, they also pose concrete safety risks. To audit and mitigate these risks, researchers have developed automated red-teaming methods, which generate adversarial prompts to elicit unsafe behavior of target LLMs during evaluation. Recent automated red-teaming methods for LLMs face a persistent trade-off: techniques that increase prompt diversity often reduce the level of the toxicity elicited from the target LLMs, while toxicity-maximizing methods tend to collapse diversity. To address the limitations, we propose ToxiPrompt, a two-stage framework that explicitly separates exploration (diversity) from exploitation (toxicity) and reunifies them with a single selection criterion to balance between diversity and toxicity. Experimental results show that ToxiPrompt outperforms four state-of-the-art baselines in both adversarial prompt diversity and the level of elicited toxicity from target LLMs, improving 14.6% harmonic mean of toxicity and diversity against the best baseline. The approach also performs well for multiple instruction-tuned target LLMs (Llama-2/3, Qwen, Mistral) without re-tuning, achieving up to 55% harmonic mean improvement against the best baseline. Our code is available at https://github.com/seungho715/ToxiPrompt

</details>

### 60. Lookahead-GCG: Improving Universal Multi-Model Optimization-Based Jailbreaking Attacks via Stochastic Nesterov Optimization

🎓 [Official](https://icml.cc/virtual/2026/poster/66388)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Rong Feng、…、Runsheng Yu

- 🎯 **研究动机**：多模型同时优化的迁移攻击用标准优化器收益甚微，根因是聚合多模型梯度时 SGD 缺乏稳定性
- 🔬 **研究方法**：Lookahead-GCG 结合 Stochastic Nesterov 加速梯度、嵌入空间动量累积与最大距离初始化
- 📌 **结论**：开源 LLM ASR 50.37%、闭源 34.03%，多模型优化带来 11.78% 增益并优于 GCG 与 TransferAttack

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transferable jailbreaking attacks enable red-teaming of black-box large language models by optimizing adversarial prompts on open-source surrogates. A natural approach to improve transferability is multi-model training---optimizing against multiple source models simultaneously. Yet this approach has been largely abandoned, as it yields only marginal gains with standard optimizers. We argue the root cause is poor generalization: standard gradient descent lacks stability when aggregating gradients from diverse models. Since GCG and its variants implicitly perform SGD in discrete token space, they inherit this instability in multi-model settings. We address this with Lookahead-GCG, which combines: (1) Stochastic Nesterov Accelerated Gradient (SNAG), whose lookahead mechanism reduces sensitivity to individual gradient updates, providing stability for multi-model optimization; (2) embedding-space momentum accumulation, which enables SNAG in discrete token optimization; and (3) maximally distant initialization, which exploits SNAG's improved generalization by starting from a universally beneficial point. Experiments show our method achieves 50.37% ASR on open-source and 34.03\% on closed-source LLMs, outperforming GCG and TransferAttack with +11.78% gains from multi-model optimization.

</details>

### 61. Jailbreak-Zero: A Path to Pareto Optimal Red Teaming for Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.2167/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`automated red teaming`、`LLM jailbreak`

👤 **作者**：Kai Hu、…、Akash Bharadwaj

- 🎯 **研究动机**：基于静态示例的自动红队评测在可扩展性与有效性上受限
- 🔬 **研究方法**：Jailbreak-Zero 用抽象安全政策定义有害内容，定义风险覆盖、语义多样性、忠实度三目标并刻画 Pareto 权衡；黑盒零样本生成加针对受害者的微调利用
- 📌 **结论**：GPT-4o ASR 99.5%、Claude 3.5 达 96.0%，未见政策仍有效，对齐后仍保持效力，给定算力下表现最佳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper presents a novel Automated Red Teaming (ART) framework that shifts from example-based to policy-based evaluation, addressing critical limitations in scalability and validity. We define harmful content through abstract safety policies rather than specific static examples. We also introduce multiple evaluation objectives: risk coverage, semantic diversity, and fidelity, and discover Pareto trade-offs between them. We propose Jailbreak-Zero, a black-box method capable of both zero-shot generation and fine-tuned exploitation of a victim’s vulnerabilities to achieve Pareto optimality. Unlike prior approaches, it does not require expert-designed strategies/prompts, but still achieves superior, human-readable attacks against open-source and proprietary models (attack success rates of 99.5% against GPT-4o and 96.0% against Claude 3.5), even for unseen safety policies. It retains efficacy even after victim models undergo safety alignment, and exposes controls to navigate Pareto trade-offs without retraining. Lastly, we show that Jailbreak-Zero is the best-performing ART method at a given compute budget. Code is available at: https://github.com/hukkai/jailbreak-zero/.

</details>

### 62. Enhancing the Transferability of Jailbreak Attacks on Large Language Models via Exploiting Reparameterization Invariance

🎓 [Official](https://aclanthology.org/2026.acl-long.357/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`attack transferability`、`jailbreak`、`jailbreak prompting`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Ao Wang、Xinghao Yang、Yongshun Gong、Wei Liu、Bao-di Liu、Weifeng Liu

- 🎯 **研究动机**：token 级梯度越狱在开源模型上高效但跨模型迁移性差，难以用于专有模型
- 🔬 **研究方法**：RIGJ 自然梯度框架：按输出分布差异而非参数空间距离定义更新方向——不同架构模型输出分布共享共同几何，优化轨迹天然模型无关
- 📌 **结论**：跨模型 ASR 提升 14.9、平均有害性分数提升 1.23

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks serve as a pivotal technique for evaluating the safety alignment of Large language models. Current token-level attacks have shown remarkable efficacy on open-source models by leveraging gradient-based optimization. However, these attacks suffer from poor cross-model transferability, severely limiting their utility on proprietary ones. To address this limitation, we propose Reparameterization Invariance Gradient-based Jailbreak (RIGJ), a natural gradient based framework designed to improve cross-model transferability. Unlike prior token-level methods whose optimization paths are constrained by model-specific Euclidean geometry, RIGJ defines update directions according to differences in output distributions rather than parameter-space distances. Since language models are trained to capture similar dependency structures of natural language, their output distributions share common geometry across architectures, yielding intrinsically model-agnostic optimization trajectories and substantially stronger jailbreak transferability. Extensive experiments demonstrate superior performance, increasing the cross-model Attack Success Rate and Average Harmfulness Score by 14.9 and 1.23, respectively. Our code is provided https://github.com/nohuma/AISafety_transfer_jailbreak_RIGJ_2026.

</details>

### 63. BlueCodeAgent: A Blue Teaming Agent Powered by Automated Red Teaming for CodeGen AI

🎓 [Official](https://icml.cc/virtual/2026/poster/63820)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Chengquan Guo、Yuzhou Nie、Chulin Xie、Zinan Lin、Wenbo Guo、Bo Li

- 🎯 **研究动机**：CodeGen AI 安全面上红队研究多、蓝队进展少，有效防御需要对任务与边缘情况的深度安全分析
- 🔬 **研究方法**：BlueCodeAgent 由自动红队驱动的端到端蓝队 agent：红队生成多样风险实例提供边缘案例，蓝队经宪法总结与动态代码分析多层防御
- 📌 **结论**：以 GPT-4o 为基座在四个任务上平均 F1 比直接提示提升 14.7%，动态分析有效降低基座过保守导致的假阳性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing research on CodeGen AI security mainly focuses on red teaming, which aims to uncover vulnerabilities and risks in AI-generated code. However, progress on the blue teaming side remains limited, as effective defenses require a deep security analysis of given tasks and edge cases. To fill in this gap, we propose BlueCodeAgent, an end-to-end blue teaming agent powered by automated red teaming. Our red teaming component generates diverse risky instances, providing effective edge cases and guidance for the subsequent blue teaming process. Our blue teaming agent then conducts multi-level defense, leveraging these red teaming examples to detect previously seen and unseen risk scenarios through constitution summarization and dynamic code analysis. Our evaluation across four representative code-related tasks–bias instruction detection, malicious instruction detection, vulnerable code detection, and prompt injection detection–shows that BlueCodeAgent achieves significant gains over diverse baselines. In particular, for vulnerability detection tasks, BlueCodeAgent integrates dynamic analysis to effectively reduce false positives, a challenging problem as base models tend to be over-conservative. Overall, with GPT-4o as the base model, BlueCodeAgent achieves an average F1 score improvement of 14.7% across four tasks compared to directly prompting the model, attributed to its ability to summarize actionable constitutions and perform dynamic analysis. Our code and data are publicly available at https://github.com/1mocat/BlueCodeAgent.

</details>

### 64. ASTRA: An Automated Framework for Strategy Discovery, Retrieval, and Evolution for Jailbreaking LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1843/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`RAG security`

👤 **作者**：Xu Liu、…、Huiqun Yu

- 🎯 **研究动机**：现有越狱方法缺乏从交互中持续学习与自演化能力，攻击策略多样性与适应性受限
- 🔬 **研究方法**：ASTRA 闭环 attack-evaluate-distill-reuse 机制自动蒸馏可复用策略，用三层动态策略库（Effective、Promising、Ineffective）管理策略记忆
- 📌 **结论**：黑盒设定下显著超越现有基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive safety alignment, Large Language Models (LLMs) remain vulnerable to jailbreak attacks. However, existing methods generally lack the capability for continuous learning and self-evolution from interactions, limiting the diversity and adaptability of attack strategies. To address this, we propose ASTRA, an automated framework capable of autonomously discovering, retrieving, and evolving attack strategies. ASTRA operates on a closed-loop "attack-evaluate-distill-reuse” mechanism, which not only generates attack prompts but also automatically distills reusable strategies from every interaction. To systematically manage these strategies, we introduce a dynamic three-tier strategy library (Effective, Promising, and Ineffective) that categorizes strategies based on performance. This hierarchical memory mechanism enables the framework to enhance efficiency by leveraging successful patterns while optimizing the exploration space by avoiding known failures. Extensive experiments in a black-box setting demonstrate that ASTRA significantly outperforms existing baselines.

</details>

### 65. BEACON: Budget-Efficient Discovery of Policy Violations in Large Language Models via Cognitive-Guided Monte Carlo Tree Search

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2985.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`benchmark`、`LLM red teaming`、`policy violation`、`query budget`

- 🎯 **研究动机**：多数红队方法只优化攻击成功率并反复探测窄漏洞集，固定预算下浪费查询、罕见关键违规类别未被探索
- 🔬 **研究方法**：BEACON 把安全测试视为预算约束的失败发现问题，用认知引导 MCTS 在固定预算下导航违规搜索空间，尽早发现多样违规
- 📌 **结论**：更早发现失败并在政策违规类别上取得更高覆盖，倡导以发现效率而非仅 ASR 评估安全测试

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Systematic safety evaluation of large language models must uncover diverse policy violations under tight query budgets. However, most redteaming methods optimize attack success rate and repeatedly probe a narrow set of vulnerabilities, yielding redundant failures and leaving rarer yet critical violation categories unexplored. Under fixed budgets, such inefficient exploration delays the first discovery and limits category coverage. To address these limitations, we propose the BudgetEfficient Adaptive Cognitive Offense Navigator (BEACON), a budget-aware safety testing framework that uses Cognitive-Guided Monte Carlo Tree Search to navigate the violation search space under fixed budgets. BEACON innovatively approaches safety testing as a budget-constrained failure discovery process, aiming to identify diverse safety violations as early as possible within a fixed query budget. It also provides an efficiency-oriented evaluation perspective that measures early discovery and harm category coverage under budget constraints. Experiments on standard benchmarks and frontier LLMs show that BEACON discovers failures earlier and achieves higher coverage across policy violation categories. These results underscore the value of evaluating safety testing through discovery efficiency rather than attack success rate alone. Warning: This paper contains examples of harmful language and images, and reader discretion is recommended.

</details>

### 66. Adaptive Probe-based Steering for Robust LLM Jailbreaking

📄 [arXiv](https://arxiv.org/abs/2605.20286) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64835)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`LLM jailbreak`、`jailbreak`、`jailbreak prompting`、`representation steering`、`attack transferability`

👤 **作者**：Junxi Chen、Junhao Dong、Xiaohua Xie

- 🎯 **研究动机**：现有 contrastive steering 越狱依赖有限且有偏的对比 prompt，且需手工调 steering 强度
- 🔬 **研究方法**：借模型提取思想使学习的 steering 向量逼近理想向量，并按对比激活统计自适应调节强度
- 📌 **结论**：无需额外对比 prompt 或手工调参即提升有效性与鲁棒性，把平均有害性评分从 6% 提至 70%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has demonstrated the potential of contrastive steering for jailbreaking Large Language Models (LLMs). However, existing methods rely on limited and inherently biased contrastive prompts and require laborious manual tuning of steering strength, limiting their robustness and effectiveness. In this paper, we leverage the idea of model extraction to guide the learned steering vectors to approximate the ideal one and propose tuning the steering strength adaptively based on contrastive activations' statistics. Experiments demonstrate that our method notably improves the effectiveness and robustness of probe-based steering, without any extra contrastive prompts or laborious manual tuning. Being an attack paper, this paper focuses on revealing the breakdown of fortified LLMs, raising the average harmfulness score from 6\% to 70\%. Our code is available at https://github.com/fhdnskfbeuv/adaptiveSteering.

</details>

### 67. Minimal, Local, Causal Explanations for Jailbreak Success in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.00123) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`

👤 **作者**：Shubham Kumar、Narendra Ahuja

- 🎯 **研究动机**：已有解释把所有越狱全局归约为削弱或增强同一批概念，无法回答某次具体越狱为何成功的局部问题
- 🔬 **研究方法**：LOCA 寻找最小的可解释中间表征改动集，使原本成功的越狱请求因果地恢复拒答，在 Gemma、Llama、Qwen 上评估
- 📌 **结论**：平均 6 次可解释改动即可诱发拒答，先前方法 20 次改动也常失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety trained large language models (LLMs) can often be induced to answer harmful requests through jailbreak prompts. Because we lack a robust understanding of why LLMs are susceptible to jailbreaks, future frontier models operating more autonomously in higher-stakes settings may similarly be vulnerable to such attacks. Prior work has studied jailbreak success by examining the model's intermediate representations, identifying directions in this space that causally encode concepts like harmfulness and refusal. Then, they globally explain all jailbreak attacks as attempting to reduce or strengthen these concepts (e.g., reduce harmfulness). However, different jailbreak strategies may succeed by strengthening or suppressing different intermediate concepts, and the same jailbreak strategy may not work for different harmful request categories (e.g., violence vs. cyberattack); thus, we seek to give a local explanation -- i.e., why did this specific jailbreak succeed? To address this gap, we introduce LOCA, a method that gives Local, CAusal explanations of jailbreak success by identifying a minimal set of interpretable, intermediate representation changes that causally induce model refusal on an otherwise successful jailbreak request. We evaluate LOCA on harmful original-jailbreak pairs from a large jailbreak benchmark across Gemma, Llama, and Qwen chat models, comparing against prior methods adapted to this setting. LOCA can successfully induce refusal by making, on average, six interpretable changes; prior work routinely fails to achieve refusal even after 20 changes. LOCA is a step toward mechanistic, local explanations of jailbreak success in LLMs. Code publicly available at https://github.com/skumar-ml/loca-jailbreaks

</details>

### 68. Structured Multi-step Jailbreaking under a Hamiltonian Generative Formulation

🎓 [Official](https://icml.cc/virtual/2026/poster/61902)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Zihan Zhou、…、Dejing Dou

- 🎯 **研究动机**：现有越狱提示常不流利不连贯，限制成功率且易被检测
- 🔬 **研究方法**：提出 SJA：借鉴 Spilsbury 谜题把有害查询分解为无害子问题序列再组合还原答案，用双曲 Hamiltonian 动学生成子问题，分数嵌入与 Möbius 融合的叙事融合保持几何一致与隐匿性
- 📌 **结论**：理论验证隐匿叙事引导的无害子问题组合能保持原有害问题的语境语义，兼顾攻击隐匿性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work shows that even safety aligned large language models (LLM) can be pushed into unsafe behavior by carefully crafted jailbreak prompts. Existing jailbreaking attack methods often rely on disfluent or incoherent prompts, which limit their success and make them easy to detect. We introduce SJA, a structured jailbreak attack built around two ideas. First, inspired by the logic of Spilsbury puzzle, SJA decomposes a harmful query into a sequence of harmless sub-questions and reconstructs the original answer by combining the sub-question responses. Second, by leveraging the theory of Hamiltonian dynamics on hyperbolic space, we propose a hyperbolic Hamiltonian dynamics-based sub-question generation framework that effectively captures the structural and temporal dependencies. We provide a theoretical analysis of how each sub-question evolves along the trajectory and show that the hyperbolic Hamiltonian system effectively captures the underlying semantic structure. Finally, we propose a hyperbolic narrative fusion mechanism built on fractional embedding and Möbius fusion. This mechanism integrates coherent narratives into sub-questions while preserving geometric consistency and improving stealth performance. We theoretically validate that the combination of the generated harmless sub-questions, guided by the stealthy narrative, can effectively preserve the contextual semantics of the original harmful question.

</details>

### 69. StealthGraph: Exposing Domain-Specific Risks in LLMs through Knowledge-Graph-Guided Harmful Prompt Generation

🎓 [Official](https://aclanthology.org/2026.acl-long.295/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`analysis`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`LLM jailbreak`

👤 **作者**：Huawei Zheng、Xinqi Jiang、Sen Yang、Shouling Ji、Yingcai Wu、Dazhen Deng

- 🎯 **研究动机**：领域特定有害提示数据集稀缺且靠人工构建，公开数据集聚焦显式有害提示，现代 LLM 防御多能识别拒绝
- 🔬 **研究方法**：提出端到端框架：知识图谱引导系统生成领域相关有害提示，再经直接重写与上下文增强重写两种混淆策略转为隐式变体
- 📌 **结论**：产出兼具强领域相关性与隐式性的高质量数据集，支撑更真实的红队评测与安全研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly applied in specialized domains such as finance and healthcare, where they introduce unique safety risks. Domain-specific datasets of harmful prompts remain scarce and still largely rely on manual construction; public datasets mainly focus on explicit harmful prompts, which modern LLM defenses can often detect and refuse. In contrast, implicit harmful prompts—expressed through indirect domain knowledge—are harder to detect and better reflect real-world threats. We identify two challenges: transforming domain knowledge into actionable constraints and increasing the implicitness of generated harmful prompts. To address them, we propose an end-to-end framework that first performs knowledge-graph-guided harmful prompt generation to systematically produce domain-relevant prompts, and then applies two-strategy obfuscation rewriting to convert explicit harmful prompts into implicit variants via direct and context-enhanced rewriting. This framework yields high-quality datasets combining strong domain relevance with implicitness, enabling more realistic red-teaming and advancing LLM safety research. We release our code and datasets on GitHub.

</details>

### 70. Reflector: Internalizing Step-wise Reflection against Indirect Jailbreaks

🎓 [Official](https://icml.cc/virtual/2026/poster/60648)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`prompt injection`

👤 **作者**：Jiachen Ma、Jiawen Zhang、Xiangtian Li、Bo Zou、Chaochao Lu、Chao Yang

- 🎯 **研究动机**：多步间接越狱利用内部生成过程绕过表层安全对齐，现有防御不足
- 🔬 **研究方法**：提出 Reflector 两阶段框架：教师引导生成高质量反思数据做 SFT 建立反思模式，再用结果驱动与奖励有效性监督的 RL 培养自主反思
- 📌 **结论**：对复杂间接攻击防御成功率（DSR）超 90% 并跨威胁场景泛化，同时 GSM8K 提升 5.85%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) demonstrate remarkable capabilities, they remain susceptible to sophisticated, multi-step jailbreak attacks that circumvent conventional surface-level safety alignment by exploiting the internal generation process. To address these vulnerabilities, we propose Reflector, a principled two-stage framework that internalizes self-reflection within the generation trajectory. Reflector first leverages teacher-guided generation to produce high-quality reflection data for supervised fine-tuning (SFT), establishing structured reflection patterns. It subsequently uses Reinforcement Learning (RL) with outcome-driven and reward-validity supervision to instill robust, autonomous self-reflection capabilities. Empirical results show that Reflector achieves Defense Success Rates (DSR) exceeding 90% against complex indirect attacks while generalizing robustly across diverse threat scenarios. Notably, the framework enhances both task-specific and general utility, yielding a 5.85% gain on GSM8K alongside improved performance on knowledge-intensive benchmarks. By internalizing trajectory-level safety, Reflector overcomes the fundamental limitations of surface alignment without significant computational overhead, offering an efficient and scalable solution for the development of safe and capable LLMs.

</details>

### 71. New Wide-Net-Casting Jailbreak Attacks Risk Large Models

📄 [arXiv](https://arxiv.org/abs/2605.17128) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62947)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Qiuchi Xiang、Haoxuan Qu、Hossein Rahmani、Jun Liu

- 🎯 **研究动机**：攻击者可同时查询一组大模型而非单一模型的广撒网越狱场景未被探索
- 🔬 **研究方法**：识别并分析该场景的安全风险，开发量身定制的越狱方法
- 📌 **结论**：对无额外防护的大模型，部分实验越狱成功率可达 100%，广撒网是需重点评估与防御的高风险场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks on large models have drawn growing attention due to their close ties to societal safety. This work identifies a practical yet unexplored jailbreak scenario, the wide-net-casting scenario, where an adversary can query a group of large models instead of a single one to elicit harmful outputs. Our analysis reveals substantial yet previously overlooked safety risks under this scenario. As a key part of our analysis, we further develop a novel jailbreak method tailored to the wide-net-casting scenario. With this tailored method, the jailbreak success rate can even reach 100% in some experiments when targeting the large models without additional safeguards, exposing wide-net-casting as a distinct, high-risk scenario that warrants attention in future evaluation and defense research.

</details>

### 72. A Game-Theoretic Analysis of Attacks on Large Language Models via Compositional Skills

🎓 [Official](https://icml.cc/virtual/2026/poster/61257)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Xinbo Wu、Huan Zhang、Abhishek Umrawal、Lav Varshney

- 🎯 **研究动机**：对齐防御仍可被精心设计的对抗 prompt 绕过，攻击者借组合式技能隐藏意图的过程缺少理论刻画
- 🔬 **研究方法**：形式化攻击者（经组合技能藏意图）与防御者的博弈，设计理论最优响应攻击策略并证明其与众多现有对抗提示方法密切相关，刻画均衡并推导可证最优防御
- 📌 **结论**：均衡分析揭示攻击者的固有优势；理论最优攻击的实践实例在多 LLM 与基准上强于现有对抗提示方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models grow increasingly capable, concerns about their safe deployment have intensified. While numerous alignment strategies aim to restrict harmful behavior, these defenses can still be circumvented through carefully designed adversarial prompts. In this work, we introduce a theoretical framework that formalizes a game between an attacker hiding its intent via compositional skills and a defender. Within this framework, we design a theoretical best-response attack strategy and show that it is closely related to many existing adversarial prompting methods. We further analyze the resulting game, characterize its equilibria, and reveal inherent advantages for the attacker. Drawing on our theoretical analysis, we also derive a provably optimal defense strategy. Empirically, we evaluate a practical instantiation of the theoretically optimal attack and observe stronger performance relative to existing adversarial prompting approaches in diverse settings encompassing different LLMs and benchmarks.

</details>

### 73. Active Attacks: Red-teaming LLMs via Adaptive Environments

📄 [arXiv](https://arxiv.org/abs/2509.21947) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64976)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak prompting`、`refusal bypass`、`attack success rate`、`LLM jailbreak`、`reinforcement learning`

👤 **作者**：Taeyoung Yun、Pierre-Luc St-Charles、Jinkyoo Park、Yoshua Bengio、Minsu Kim

- 🎯 **研究动机**：多样性寻求的 RL 红队方法一旦找到高奖励 prompt 便不再探索新模式，攻击易塌缩
- 🔬 **研究方法**：借鉴主动学习提出 Active Attacks：周期性用收集到的攻击 prompt 对受害 LLM 做安全微调，随受害者演化自然形成从易到难的探索课程；即插即用地并入现有 RL 目标
- 📌 **结论**：对 GFlowNets 前 SOTA 的跨攻击成功率从 0.07% 提到 31.28%（相对增益逾 400 倍），计算仅增 6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We address the challenge of automatically generating diverse attack prompts for large language models (LLMs) that elicit harmful behaviors (e.g., insults, sexual content) and are used for safety fine-tuning. While several prior approaches train LLMs with reinforcement learning (RL) to generate such prompts using only a toxicity classifier as a reward, existing diversity-seeking RL methods often collapse to limited modes: once high-reward prompts are found, exploration of new regions is discouraged. Inspired by the active learning paradigm that encourages adaptive exploration, we introduce \textbf{Active Attacks}, a novel RL-based red-teaming algorithm that adapts its attacks as the victim evolves. By periodically safety fine-tuning the victim LLM with collected attack prompts, we naturally induce an \emph{easy-to-hard exploration curriculum}, where the attacker progresses beyond easy modes toward increasingly difficult ones. We observe that this simple plug-and-play module, which seamlessly integrates into existing RL objectives, unexpectedly outperformed prior RL-based methods, improving cross-attack success rates against GFlowNets, the previous state-of-the-art, from 0.07\% to 31.28\% (a relative gain of more than 400×) with only a 6\% increase in computation.

</details>

### 74. One Leak Away: How Pretrained Model Exposure Amplifies Jailbreak Risks in Finetuned LLMs

📄 [arXiv](https://arxiv.org/abs/2512.14751) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-12　🏷 ACM CCS 2026

**关键词**：`attack`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`pretrain-to-finetune transfer`、`Probe-Guided Projection`

👤 **作者**：Yixin Tan、Zhe Yu、Rui Wen、Jun Sakuma

- 🎯 **研究动机**：微调 LLM 是否继承其预训练源的越狱漏洞尚不清楚
- 🔬 **研究方法**：在攻击者可全量访问预训练模型但无其专有微调版的威胁模型下分析迁移，表示级探测显示可迁移 prompt 在预训练隐状态中线性可分，据此提出 Probe-Guided Projection 把优化导向可迁移相关方向
- 📌 **结论**：PGP 在多 LLM 家族与多样微调任务上迁移成功率高；同一表示洞见也支撑轻量防御，在保留下游效用的同时缓解迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning pretrained large language models (LLMs) has become the standard paradigm for developing downstream applications. However, its security implications remain unclear, particularly regarding whether finetuned LLMs inherit jailbreak vulnerabilities from their pretrained sources. We investigate this question in a realistic pretrain-to-finetune threat model, where an attacker has full access to a released pretrained LLM but no access to its proprietary finetuned derivatives. Empirical analysis shows that adversarial prompts optimized on the pretrained model transfer most effectively to its finetuned variants, revealing inherited vulnerabilities from pretrained to finetuned LLMs. To further examine this inheritance, we conduct representation-level probing, which shows that transferable prompts are linearly separable within the pretrained hidden states, suggesting that transferability-relevant structure is already encoded in pretrained representations. Building on this insight, we propose the Probe-Guided Projection (PGP) attack, which steers optimization toward transferability-relevant directions. Experiments across multiple LLM families and diverse finetuned tasks confirm PGP's strong transfer success, underscoring the security risks inherent in the pretrain-to-finetune paradigm. Finally, we demonstrate that the same representation-level insights also enable a lightweight defense that mitigates pretrain-to-finetune jailbreak transfer while preserving downstream utility.

</details>

### 75. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

📄 [arXiv](https://arxiv.org/abs/2602.24009) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65657)　📅 2026-02　🏷 ICML 2026

**关键词**：`benchmark`、`jailbreak`、`jailbreak prompting`、`refusal bypass`、`LLM jailbreak`、`multi-agent evaluation`

👤 **作者**：Zhicheng Fang、Jingjie Zheng、Chenxu Fu、Wei Xu

- 🎯 **研究动机**：越狱技术演进快于基准，数据集、harness 与判分协议漂移使鲁棒性估计过时且不可比
- 🔬 **研究方法**：Jailbreak Foundry 用多 agent 工作流把论文转成可执行模块：JBF-LIB 共享契约、JBF-FORGE 论文转模块、JBF-EVAL 标准化评测
- 📌 **结论**：30 个复现攻击与报告 ASR 平均仅偏 +0.26 个百分点，攻击专用代码减半以上，统一评测 10 个受害模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce JAILBREAK FOUNDRY (JBF), a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) JBF-LIB for shared contracts and reusable utilities; (ii) JBF-FORGE for the multi-agent paper-to-module translation; and (iii) JBF-EVAL for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced-reported) attack success rate (ASR) deviation of +0.26 percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by more than half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

</details>

### 76. EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities

📄 [arXiv](https://arxiv.org/abs/2609.00487)　📅 2026-09

**关键词**：`attack`、`multi-turn jailbreak`、`quality-diversity search`、`adaptive red teaming`

👤 **作者**：Feitong Qiao、…、Anish Das Sarma

- 🎯 **研究动机**：多轮渐进攻击是 LLM 最少被理解的失效之一，自动 red-teaming 把它当生成问题而非搜索问题，只产出零散成功
- 🔬 **研究方法**：提出 EvoFlint：用进化 quality-diversity 搜索演化分阶段对话计划（LLM 变异／交叉、ASR 与峰值严重度的 Pareto 适应度、风险索引档案与跨代记忆）
- 📌 **结论**：HarmBench-test 上 ASR 达 Claude Sonnet 4.6 的 35.8%、GPT-5.4 的 59.7%、Qwen3-32B 的 94.3%，档案按风险类目暴露各模型安全训练的覆盖缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-turn attacks one of the least understood failure modes of large language models. Most automated red-teaming methods treat this as a generation problem: produce attacks that break the model. We argue it is better framed as a search problem: discover, organize, and iteratively refine a diverse archive of attack strategies, producing a structured map of how a target model fails rather than a list of one-off successes. We introduce EvoFlint, which applies evolutionary quality-diversity search to multi-turn red-teaming. Attack strategies are phased conversation plans, not raw prompts, and are evolved through LLM-driven mutation and crossover. A Pareto fitness over attack success rate and peak severity preserves selection signal from near-miss attacks. A risk-indexed archive runs novelty search with local competition over strategy description embeddings inside each cell, maintaining diversity without committing to a predefined style taxonomy. A generation-level memory accumulates target-model insights across the population and feeds them back into strategy generation. On the HarmBench-test split, EvoFlint reaches attack success rates of 35.8% on Claude Sonnet 4.6, 59.7% on GPT-5.4, and 94.3% on Qwen3-32B, alongside 98.7% on the older GPT-4o included as a baseline reference. The resulting archive, organized by risk category, exposes for each target which categories of harm its safety training has and has not covered.

</details>

### 77. In-Context Representation Hijacking

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

### 78. GateBreaker: Gate-Guided Attacks on Mixture-of-Expert LLMs

📄 [arXiv](https://arxiv.org/abs/2512.21008) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wu-lichao)　📅 2025-12　🏷 USENIX Security 2026

**关键词**：`attack`、`MoE LLM`、`VLM safety`、`multimodal jailbreak`、`safety alignment`、`expert routing`

👤 **作者**：Lichao Wu、Sasha Behrouzi、Mohamadreza Rostami、Stjepan Picek、Ahmad-Reza Sadeghi

- 🎯 **研究动机**：LLM 安全研究几乎只关注稠密架构，MoE 稀疏路由下安全机制的鲁棒性未被检验
- 🔬 **研究方法**：GateBreaker 免训练三阶段推理时攻击：门控级画像定位有害输入下被集中路由的安全专家、专家级定位其内安全结构、定向禁用该结构
- 📌 **结论**：MoE 安全集中于稀疏路由协调的小撮神经元；禁用目标层约 3% 神经元即使八个对齐 MoE LLM 平均 ASR 从 7.4% 升至 64.9%，同族一次迁移使 17.9%→67.7%，并泛化到五个 MoE VLM（60.9%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) architectures have advanced the scaling of Large Language Models (LLMs) by activating only a sparse subset of parameters per input, enabling state-of-the-art performance with reduced computational cost. As these models are increasingly deployed in critical domains, understanding and strengthening their alignment mechanisms is essential to prevent harmful outputs. However, existing LLM safety research has focused almost exclusively on dense architectures, leaving the unique safety properties of MoEs largely unexamined. The modular, sparsely-activated design of MoEs suggests that safety mechanisms may operate differently than in dense models, raising questions about their robustness. In this paper, we present GateBreaker, the first training-free, lightweight, and architecture-agnostic attack framework that compromises the safety alignment of modern MoE LLMs at inference time. GateBreaker operates in three stages: (i) gate-level profiling, which identifies safety experts disproportionately routed on harmful inputs, (ii) expert-level localization, which localizes the safety structure within safety experts, and (iii) targeted safety removal, which disables the identified safety structure to compromise the safety alignment. Our study shows that MoE safety concentrates within a small subset of neurons coordinated by sparse routing. Selective disabling of these neurons, approximately 3% of neurons in the targeted expert layers, significantly increases the averaged attack success rate (ASR) from 7.4% to 64.9% against the eight latest aligned MoE LLMs with limited utility degradation. These safety neurons transfer across models within the same family, raising ASR from 17.9% to 67.7% with one-shot transfer attack. Furthermore, GateBreaker generalizes to five MoE vision language models (VLMs) with 60.9% ASR on unsafe image inputs.

</details>

### 79. Metis: Learning to Jailbreak LLMs via Self-Evolving Metacognitive Policy Optimization

📄 [arXiv](https://arxiv.org/abs/2605.10067) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63565)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`agent memory`、`self-evolution`、`LLM jailbreak`、`inference-time intervention`

👤 **作者**：Huilin Zhou、…、Xuelong Li

- 🎯 **研究动机**：自动红队靠静态启发式或随机搜索，对先进安全对齐脆弱
- 🔬 **研究方法**：Metis 把越狱重构为对抗 POMDP 中的推理时策略优化：自进化元认知循环因果诊断目标防御逻辑，结构化反馈作语义梯度精化策略
- 📌 **结论**：10 个模型上平均 ASR 89.2% 最强，O1 上 76.0%、GPT-5-chat 上 78.0%；token 成本平均降 8.2 倍（最多 11.4 倍）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Red teaming is critical for uncovering vulnerabilities in Large Language Models (LLMs). While automated methods have improved scalability, existing approaches often rely on static heuristics or stochastic search, rendering them brittle against advanced safety alignment. To address this, we introduce \textbf{Metis}, a framework that reformulates jailbreaking as inference-time policy optimization within an adversarial Partially Observable Markov Decision Process (POMDP). Metis employs a self-evolving metacognitive loop to perform causal diagnosis of a target's defense logic and leverages structured feedback as a semantic gradient to refine its policy, offering enhanced interpretability through transparent reasoning traces. Extensive evaluations across 10 diverse models demonstrate that Metis achieves the strongest average Attack Success Rate (ASR) among compared methods at 89.2\%, maintaining high efficacy on resilient frontier models (e.g., 76.0\% on O1 and 78.0\% on GPT-5-chat) where traditional baselines exhibit substantial performance degradation. By replacing redundant exploration with directed optimization, Metis reduces token costs by an average of 8.2$\times$ (and up to 11.4$\times$). Our analysis reveals that current defenses remain vulnerable to internally-steered, closed-loop reasoning trajectories under the tested settings, highlighting a critical need for next-generation defenses capable of reasoning about safety dynamically during inference.

</details>

### 80. SHARP: Self-adaptive Harmful Category-aware Prompt Generation for Black-box Jailbreaking

🎓 [Official](https://aclanthology.org/2026.acl-long.2100/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`jailbreak`、`harmful fine-tuning`、`alignment erosion`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Yingjie Xue、…、Fei Li

- 🎯 **研究动机**：现有越狱方法忽视有害问题跨类别的语义差异，导致成功率不一致、整体攻击效果下降
- 🔬 **研究方法**：提出类别感知越狱框架 SHARP：把有害问题的语义类别纳入提示生成，结合两阶段 LoRA 微调与 DPO 强化学习优化攻击成功与类别对齐
- 📌 **结论**：攻击成功率显著提升，跨类别鲁棒性优于 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been widely applied in various domains such as education and healthcare, making safety assurance crucial. Jailbreak attacks, a method used in red-teaming, can help evaluate and improve the defensive strategies of LLMs. However, existing jailbreak methods often overlook the semantic differences across categories of harmful questions, leading to inconsistent success rates and reduced overall attack effectiveness. We propose the first category-aware jailbreak framework, SHARP, which incorporates the semantic category of harmful questions into prompt generation. Trained on a verified jailbreak dataset, SHARP enables the model to learn category-specific semantic features and adaptively generate prompts that bypass safety mechanisms. The method combines two-stage LoRA fine-tuning, and DPO-based reinforcement learning to optimize both attack success and category alignment. Experiments show that SHARP significantly improves attack success rates and achieves better cross-category robustness compared to the state-of-the-art (SOTA) baselines, providing an efficient and scalable tool for evaluating LLM safety.

</details>

### 81. Greedy Coordinate Diffusion: Effective and Semantically Coherent Adversarial Attacks via Diffusion Guidance

📄 [arXiv](https://arxiv.org/abs/2606.15531) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63755)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`diffusion model`、`adversarial robustness`、`attack transferability`

👤 **作者**：Bohdan Turbal、Blossom Metevier、Max Springer、Aleksandra Korolova

- 🎯 **研究动机**：GCG 等优化攻击的高困惑度后缀易被防御检测，保持连贯的攻击又常改变查询语义偏离原目标
- 🔬 **研究方法**：GCD 用离散扩散语言模型的生成先验引导对抗后缀搜索，无需梯度访问（灰盒），兼顾低困惑度与语义 adherence
- 📌 **结论**：ASR 最高且响应质量有竞争力，被困惑度过滤与 guard 模型检出的比率低于其他方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks on large language models have limited practical impact despite extensive research. Optimization-based attacks such as Greedy Coordinate Gradient (GCG) (Zou et al., 2023) produce high-perplexity, incoherent suffixes that existing defenses easily detect (Bengio et al., 2024). Moreover, attempting to enforce coherence constraints during optimization often prevents the attack from successfully eliciting the specific targeted response, resulting in low success rates against robust models. Conversely, attacks that maintain coherence often alter the semantic intent of queries; when the model complies with these altered queries, responses fail to address the adversary's original goal. In this work, we introduce Greedy Coordinate Diffusion (GCD), a novel framework that efficiently generates adversarial attacks against safety-aligned models while maintaining low perplexity and high semantic adherence to the adversary's original intent. GCD leverages the generative priors of discrete diffusion language models to guide the search for adversarial suffixes that achieve semantic coherence and adherence. Unlike GCG, GCD does not require direct gradient access, allowing it to operate in a gray-box setting. We show GCD achieves highest ASR while remaining competitive on response-quality scores, and that the constructed adversarial prompts are detected at lower rates than other methods by perplexity-based and guard-model filters.

</details>

### 82. Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2609.09553)　📅 2026-09

**关键词**：`attack`、`cipher jailbreak`、`in-context learning`、`black-box API`、`classifier evasion`

👤 **作者**：Thomas Rivasseau

- 🎯 **研究动机**：任意密码越狱此前需经微调 API 注入密文语料才能建立，前沿模型免微调是否可被攻陷未知
- 🔬 **研究方法**：证明新前沿模型可经 prompting 与上下文学习获得密码通信技能，安全对齐在密文通道下被削弱或绕过
- 📌 **结论**：对 Anthropic/Google/OpenAI 前沿模型越狱成功；密文呈乱码样绕过商用有害内容分类器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model safety and security research is preoccupied with, among other things, detecting and preventing jailbreak attacks: alignment bypasses that allow an adversarial user to elicit unwanted or harmful outputs from models. Arbitrary cipher, or covert communication, attacks are one such type of jailbreak and have previously been demonstrated against the fine-tuning APIs of commercial models. In these attacks, target models are trained on a corpus of encrypted harmful questions and responses and subsequently respond to harmful requests through the learned encryption scheme. In this paper, we show that newer frontier models do not require fine-tuning to acquire cipher-based communication skills. Instead, they can learn these skills through prompting and, when necessary, through in-context learning. Furthermore, model alignment is significantly weakened or entirely bypassed when communication occurs through the learned cipher. To the best of our knowledge, this constitutes a novel attack vector against commercial black-box large language models. We demonstrate successful jailbreaks against frontier models developed by Anthropic, Google, and OpenAI. Our attack bypasses commercial harmfulness classifiers because harmful content is encrypted and therefore appears as nonsensical text or gibberish.

</details>

### 83. How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE

📄 [arXiv](https://arxiv.org/abs/2609.09793)　📅 2026-09

**关键词**：`attack`、`refusal direction ablation`、`MoE frontier model`、`white-box editing`

👤 **作者**：Yi Shi、Tanyu Chen、Kai Shen

- 🎯 **研究动机**：方向消融白盒攻击只在 ≤70B 稠密模型上建立，MoE+量化前沿架构上是否存活未知
- 🔬 **研究方法**：把攻击应用到 GLM-5.3-Flash（320B/288 路由专家/超连接残差/FP8），分解注意力/稠密/路由专家写入器的单独与联合编辑
- 📌 **结论**：三者联合移除 0.776 拒绝能力（74% 效应仅存于联合干预）；七基准降 41-89pp 且能力无可测变化，按模块名匹配的原配方会静默失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream. It needs no gradient-based training and no optimization, only a few hundred contrastive prompts, which makes it the canonical white-box attack on open-weight alignment. However, it has been established only on dense models up to roughly 70B parameters. We study whether it survives the shift to frontier mixture-of-experts (MoE) models whose residual streams are no longer a single tensor and whose weights ship quantized. We apply it to GLM-5.3-Flash (320B parameters, 288 routed experts, a four-wide hyper-connection residual, block-FP8). The attack survives the architecture, but what it reaches is no longer where a reader of the original recipe would look for it. Editing the attention, dense and routed-expert writers on their own removes 0.039, 0.016 and 0.148 of refusal respectively; editing all three together removes 0.776. As a result, 74% of the effect exists only under the joint intervention. The part the conventional recipe reaches by module-name matching accounts for 0.066 of that 0.776, which is why it fails silently on an MoE. The effect does not follow from removing just any direction: ablating a random direction orthogonal to it leaves refusal unchanged. A category-concentrated residue survives every edit we tried: subspaces fitted on violence, sexual content and hate leave measurable refusal at every rank from 1 to 12. We report the method, the 41-89 percentage-point reductions it achieves across seven harmful benchmarks with no detected change in capability, and the boundary where it stops.

</details>

### 84. ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing

📄 [arXiv](https://arxiv.org/abs/2609.08256)　📅 2026-09

**关键词**：`tool`、`red teaming`、`blue team defense`、`adversarial evaluation`、`LLM arena`、`secret leakage`

👤 **作者**：Yi Ting Shen、Kentaroh Toyoda、Alex Leung

- 🎯 **研究动机**：自动化红队攻击与蓝队防御孤立构建测试，攻防分数难以互信
- 🔬 **研究方法**：ACEA 以 ASAP 协议插拔红蓝适配器共享目标 LLM，用种子机密提供可验证真值分离泄漏与幻觉，逐轮分解攻击强度与防御效果
- 📌 **结论**：平台可定位每次失败并转化为红蓝项目改进信号，附加上下文改进回路支持跨轮适应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated red-team attacks and blue-team defenses for large language models (LLMs) are advancing quickly. However, attackers and defenders are built and tested in isolation, and the resulting scores are hard to trust. To tackle this, we present ACEA (Adversarial Co-Evolution Arena), a platform that connects a pluggable red-team adapter and a pluggable blue-team adapter to a shared target LLM and scores their attack and defense rates with an LLM judge. ACEA contributes four components. First, a pluggable, model-agnostic arena. Any red or blue project connects over a minimal HTTP protocol, which we call the ACEA Standard Adapter Protocol (ASAP). It can be written in any language, and a project that exposes nothing but the protocol is a full participant. Second, an evaluation methodology built for adversarial rounds. Seeding the target with canonical secrets gives verifiable ground truth that separates real leakage from hallucination. We also send each attack to the target even when the defense blocks it, which measures the attack's raw potency independently of whether it was stopped. Together these yield a per-round decomposition of attack strength and defense effectiveness. Third, a real-time, game-style visualization with a detailed end-of-battle report that localizes each failure. The evaluation thus becomes an actionable signal for improving a red or blue project. Fourth, an optional in-context improvement loop that turns each round's outcome into advisory hints for the next. An adapter can then adapt across rounds without keeping state, provided it reads the hints. We describe the design of ACEA and the metrics through which red and blue teams are scored head to head.

</details>
