# Reasoning Model Safety

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究显式 thinking token、长推理轨迹和 reasoning-time computation 如何改变模型安全。重点区分模型是否真的在推理中形成安全决定、可见 trace 是否只是对既定选择的事后解释，以及攻击者能否通过 reasoning weight、隐藏知识或中间步骤操纵提取模型原本不会直接输出的内容；单纯利用长推理造成资源耗尽的攻击归入 [Reasoning Model DoS](../../dos/reasoning-model-dos.md)。

## 研究脉络

- **结果级安全：** 最初沿用普通 LLM 的 final-answer refusal 评测，但无法定位风险是在思维过程、答案还是二者连接处产生。
- **Trace 分解：** 新评测分别标注 reasoning trace 与 final answer，发现中间步骤可能泄漏风险内容，也可能在最后被拒答掩盖。
- **机制检验：** causal intervention 开始判断 thinking token 是否真正参与安全决策，避免把流畅的安全解释误当作因果机制。
- **Reasoning-time 攻防：** attack 放大 task vector 或操纵推理轨迹以提取秘密，defense 则用 verification 和多原则 steering 在生成过程中纠正。
- **当前边界：** 可见 CoT 不一定等于真实内部推理；安全结论应结合 hidden-state intervention、不同 reasoning budget 与不展示 trace 的模型进行验证。

## Benchmark 与评测

### 1. TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.24232)　📅 2026-08

**关键词**：`benchmark`、`reasoning-trace safety`、`evidence localization`、`full-pipeline moderation`、`CoT monitoring`、`evidence grounding`

👤 **作者**：Zhenyu Wu、…、Xin Gao

- 🎯 **研究动机**：unsafe 内容 benchmark 只覆盖 prompt 与最终回答，忽略推理模型中间 reasoning trace 且无证据标注
- 🔬 **研究方法**：TRACE 标注 prompt、reasoning trace 与 final response 三段安全性并提取源文本证据，覆盖双语九类风险十种攻击
- 📌 **结论**：18 个 guardrail 模型对推理轨迹的安全判定显著更难，且难以准确提取支撑证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

</details>

### 2. &lt;/think&gt; Doesn't Stop Reasoning: Analysis of Spurious CoT Termination

📄 [arXiv](https://arxiv.org/abs/2609.03633)　📅 2026-09

**关键词**：`analysis`、`CoT monitorability`、`hidden reasoning`、`token control`、`CoT termination`、`early exit`

👤 **作者**：Seunghee Koh、Sungjae Choi、Minchan Kwon、Sunghyun Baek、Junmo Kim

- 🎯 **研究动机**：training-free 早退方法在中间点注入 </think> 触发转答，但注入不保证干净的推理-作答转换
- 🔬 **研究方法**：发现并命名 spurious CoT termination：作答阶段在模型再生成 EoT 前持续推理，且伪终止长度随省下的推理 token 增长；假设对注入 EoT 注意不足所致并提出 Exit-token Attention Biasing 检验
- 📌 **结论**：四个 LRM、五个基准、两种早退方法上，增强对注入 EoT 的注意力可减少伪终止与作答阶段长度——外部匹配 think-block 格式不等于控制推理状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) reasoning improves large reasoning models (LRMs) on complex tasks but often produces long, redundant traces. Recent training-free early-exit methods shorten these traces by choosing an intermediate point to stop reasoning. We study one such strategy that injects an end-of-think token (EoT, </think>) at this point to trigger the reasoning-to-answering transition, and find that the injected EoT does not always induce a clean answering phase. Answering-phase generation can continue before the model regenerates another EoT, with the span preceding this regenerated EoT scaling with the reasoning tokens saved by early exit and exhibiting continued reasoning behavior. We call this spurious CoT termination, where reasoning-like generation continues into the answering phase. We hypothesize that insufficient attention to the injected EoT contributes to spurious CoT termination and probe this hypothesis with Exit-token Attention Biasing (EAB). Across four LRMs, five benchmarks, and two early-exit methods, increasing attention to the injected EoT reduces spurious CoT termination and answering-phase length. These results reveal a limitation of controlling LRMs by externally matching their explicit think-block format. Inserting the EoT token conforms to this format but does not by itself guarantee the intended reasoning-to-answering transition. Our code is available at https://github.com/Seunghee-Koh/Spurious-CoT-Termination.

</details>

### 3. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

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

### 4. Why2Speak: Faithful Reasoning for Abstaining Action Policies

📄 [arXiv](https://arxiv.org/abs/2608.20670)　📅 2026-08

**关键词**：`analysis`、`CoT faithfulness`、`capability-auditability trade-off`、`oversight control`、`reasoning-model auditability`、`act-or-abstain policy`

👤 **作者**：Shreya Mendi、Brinnae Bent

- 🎯 **研究动机**：对可行动或弃权的 agent，解释只有反映产生动作的计算才对监督有用；暴露推理是否会改变被审计的策略未知
- 🔬 **研究方法**：以 Qwen3-8B 带/不带 CoT 在多方对话干预时机决策上比较直接策略、推理策略、SFT 与 RL，并用激活探针与行为消融做控制
- 📌 **结论**：能力-可审计性权衡：最强直接策略质量高但无推理可查，推理策略有轨迹但性能低（尤其干预机会召回）；暴露推理会改变动作策略而非仅使其可观察

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an assistant must decide whether to speak or remain silent. This setting exposes class imbalance, asymmetric action costs, and the possibility that exposing reasoning changes the policy being audited. Using Qwen3-8B, decoded with or without chain-of-thought reasoning, we compare direct decision policies, reasoning policies, supervised fine-tuning, and reinforcement learning. We find a capability-auditability tradeoff: the strongest direct policy achieves higher quality but exposes no reasoning to inspect, while the reasoning policy provides a trace at the cost of lower performance, particularly recall of true intervention opportunities. Supervised fine-tuning either suppresses reasoning or preserves it without improving decision quality, while reinforcement learning also fails to improve the reasoning policy. We identify one mechanism underlying this failure: group relative objectives provide no learning signal on confidently wrong prompts when sampled rollouts all select the same action. Controlled activation probes and behavioral ablations show that standard faithfulness methods can overstate evidence that exposed reasoning reflects the underlying decision process. Probability-based metrics saturate under confident decisions, probes are vulnerable to class imbalance and textual leakage, and reasoning ablations can confound reasoning content with changes in inference mode. Together, these results show that exposing reasoning can change an agent's action policy rather than simply make it observable. We provide controls for evaluating reasoning-based oversight of agents that can act or abstain.

</details>

### 5. Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents

📄 [arXiv](https://arxiv.org/abs/2608.17153)　📅 2026-08

**关键词**：`defense`、`analysis`、`evidence-access control`、`System 2 gating`、`RAG Agent`、`System 2 reasoning`

👤 **作者**：Mehrdad Ghassabi

- 🎯 **研究动机**：LLM 可能正确检测文档含错误信息却仍受其影响；Cordon Principle 严格隔离又带来大量计算开销
- 🔬 **研究方法**：提出精化原则——只有具备 System 2 深思推理能力的 agent 才可访问不可信文档；构建量化误信息检测与下游影响之差的指标并对比推理与标准模型
- 📌 **结论**：推理能力模型对损坏证据鲁棒得多，无需 Cordon 式严格隔离，为安全 RAG 设计提供更实用基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

</details>

### 6. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`analysis`、`benchmark`、`harmful fine-tuning`、`CoT escalation`、`alignment degradation`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 7. Do Thinking Tokens Help with Safety?

📄 [arXiv](https://arxiv.org/abs/2606.25013)　📅 2026-06

**关键词**：`analysis`、`thinking token`、`causal intervention`、`post-hoc rationale`

👤 **作者**：Narutatsu Ri、Abhishek Panigrahi、Sanjeev Arora

- 🎯 **研究动机**：普遍认为推理模型的 thinking token 提供安全审议空间，该直觉未必正确
- 🔬 **研究方法**：在 GPT-OSS、Qwen、Olmo、Phi 家族上训练探测头预测拒绝/顺从，分析思维链前 20% 后结果是否改变，并检验推理导向的安全干预
- 📌 **结论**：最终拒绝结果在可见思考前即可从首 token 隐藏表示预测（0.84-0.95 AUROC、约 88% 平衡准确率）；约 74% 文本级审议发生在分布已锁定后，现有干预主要推向过度拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Today's reasoning models use thinking tokens to attain stronger performance on benchmarks than their instruction-tuned counterparts. It is also generally believed that this more "deliberative" mode should improve alignment and safety, by providing the model a safe space to consider whether its planned answer to a request violates its safety principles. We present evidence that this intuition is not always correct. Across frontier open-weight reasoning models spanning GPT-OSS, Qwen, Olmo, and Phi families, we find that the eventual refusal/compliance outcome is already strongly predictable via a trained head on the first token's hidden representation ($0.84$-$0.95$ AUROC and $\sim88\%$ balanced accuracy for predicting refusal/compliance) before any visible thinking. The thinking process turns out to be more akin to prefix completion than to deliberative revision, with the final outcome rarely changing after the first $\sim20\%$ of thinking, despite giving the appearance of deliberation at the text level ($\sim74\%$ of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side). We also find that existing inference-time and training-based safety interventions, despite being motivated by the goal of inducing deliberation, largely shift model behavior toward over-refusal while suppressing already-scarce deliberation signals. Our results suggest that safety behavior in current reasoning models is much less deliberative than commonly assumed, and highlight the need for methods that induce real safety deliberation.

</details>

### 8. Chain of Risk: Safety Failures in Large Reasoning Models and Mitigation via Adaptive Multi-Principle Steering

📄 [arXiv](https://arxiv.org/abs/2605.05678)　📅 2026-05

**关键词**：`benchmark`、`reasoning safety`、`trace-answer risk`、`multi-principle steering`

👤 **作者**：Xiaomin Li、…、Yuexing Hao

- 🎯 **研究动机**：LRM 暴露推理链带来安全盲区——最终答案安全不代表推理轨迹安全
- 🔬 **研究方法**：以二十原则统一量表对 15 个 LRM 各 4.1 万 prompt 的推理与答案两阶段打分，识别 leak 与 escape 两类失效；提出按原则学 unsafe-to-safe 激活方向、按隐状态邻近性选择性激活的多原则 steering
- 📌 **结论**：推理轨迹一致暴露额外风险并集中于虚假信息、法律合规等原则；DeepSeek-R1-Qwen-7B 不安全计数平均降 40.8%，BBH、GSM8K、MMLU 宏平均准确率保持 97.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) increasingly expose chain-of-thought-like reasoning for transparency, verification, and deliberate problem solving. This creates a safety blind spot: harmful or policy-violating content may appear in reasoning traces even when final answers appear safe. We test whether final-answer safety is a sufficient proxy for the full reasoning-answer trajectory by scoring both stages under a unified twenty-principle safety rubric. Using prompts from seven public harmfulness and jailbreak sources, plus four out-of-distribution (OOD) sources, we evaluate 15 open-weight and API-based LRMs across 41K prompts per model. Reasoning traces consistently reveal additional safety risks beyond final answers, especially in high-severity stage-wise failures: leak cases, where unsafe reasoning precedes a safe-looking answer, and escape cases, where benign-looking reasoning precedes an unsafe final response. Principle-level analysis shows that risk concentrates in misinformation, legal compliance, discrimination, physical harm, and psychological harm. We further propose adaptive multi-principle steering, a white-box test-time mitigation that learns one unsafe-to-safe activation direction per safety principle and activates only directions whose current hidden state is closer to the unsafe than safe centroid. On three steerable open reasoning models, adaptive steering reduces unsafe counts in both reasoning traces and final answers on held-out and OOD benchmarks. DeepSeek-R1-Qwen-7B achieves a 40.8% average unsafe-count reduction while retaining 97.7% macro-averaged accuracy on BBH, GSM8K, and MMLU. These results suggest that LRM safety should be evaluated and mitigated over the full exposed reasoning-answer trajectory, not only at the final-answer stage.

</details>

### 9. Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

📄 [arXiv](https://arxiv.org/abs/2603.03205) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63878)　📅 2026-03　🏷 ICML 2026

**关键词**：`defense`、`reasoning model`、`safety degradation`、`inference-time risk`、`agent safety`、`empirical evaluation`

👤 **作者**：Aradhye Agarwal、Gurdit Siyan、Yash Pandya、Joykirat Singh、Akshay Nambi、Ahmed Awadallah

- 🎯 **研究动机**：面向静态生成优化的对齐在多步工具使用中失效，访问文件或输入凭据等单步失误可致不可逆伤害
- 🔬 **研究方法**：MOSAIC 把推理结构化为计划-检查-执行或拒绝循环，显式安全推理与拒绝均为一等动作，用成对轨迹比较的偏好 RL 免轨迹标签训练
- 📌 **结论**：有害行为最多降 50%，注入攻击下有害任务拒绝率升超 20%，并保持或提升良性任务表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic language models operate in a fundamentally different safety regime than chat models: they must plan, call tools, and execute long-horizon actions where a single misstep, such as accessing files or entering credentials, can cause irreversible harm. Existing alignment methods, largely optimized for static generation and task completion, break down in these settings due to sequential decision-making, adversarial tool feedback, and overconfident intermediate reasoning. We introduce MOSAIC, a post-training framework that aligns agents for safe multi-step tool use by making safety decisions explicit and learnable. MOSAIC structures inference as a plan, check, then act or refuse loop, with explicit safety reasoning and refusal as first-class actions. To train without trajectory-level labels, we use preference-based reinforcement learning with pairwise trajectory comparisons, which captures safety distinctions often missed by scalar rewards. We evaluate MOSAIC zero-shot across three model families, Qwen2.5-7B, Qwen3-4B-Thinking, and Phi-4, and across out-of-distribution benchmarks spanning harmful tasks, prompt injection, benign tool use, and cross-domain privacy leakage. MOSAIC reduces harmful behavior by up to 50%, increases harmful-task refusal by over 20% on injection attacks, cuts privacy leakage, and preserves or improves benign task performance, demonstrating robust generalization across models, domains, and agentic settings.

</details>

### 10. Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away

📄 [arXiv](https://arxiv.org/abs/2602.11096) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61339)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reasoning model`、`safety degradation`、`inference-time risk`、`refusal calibration`、`chain-of-thought`

👤 **作者**：Soumya Suvra Ghosal、Souradip Chakraborty、Vaibhav Singh、Furong Huang、Dinesh Manocha、Amrit Singh Bedi

- 🎯 **研究动机**：GRPO 等 RL 后训练提升多模态推理能力的同时会降低安全对齐并提高越狱成功率
- 🔬 **研究方法**：提出推理时防御 SafeThink：把安全恢复视为满足性约束，安全奖励模型监视推理轨迹，仅在阈值被违反时注入优化的短前缀（"Wait, think safely"）
- 📌 **结论**：在 6 个开源 MLRM 与 4 个越狱基准上 ASR 降低 30-60%（如 LlamaV-o1 在 JailbreakV-28K 上 63.33%→5.74%），MathVista 精度几乎不变；前 1-3 步推理内干预通常即可扭转整条生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) based post-training for explicit chain-of-thought (e.g., GRPO) improves the reasoning ability of multimodal large-scale reasoning models (MLRMs). But recent evidence shows that it can simultaneously degrade safety alignment and increase jailbreak success rates. We propose SafeThink, a lightweight inference-time defense that treats safety recovery as a satisficing constraint rather than a maximization objective. SafeThink monitors the evolving reasoning trace with a safety reward model and conditionally injects an optimized short corrective prefix ("Wait, think safely") only when the safety threshold is violated. In our evaluations across six open-source MLRMs and four jailbreak benchmarks (JailbreakV-28K, Hades, FigStep, and MM-SafetyBench), SafeThink reduces attack success rates by 30-60 % (e.g., LlamaV-o1: 63.33\% $\rightarrow$5.74\% on JailbreakV-28K, R1-OneVision: 69.07\%$\rightarrow$5.65\% on Hades) while preserving reasoning performance (MathVista accuracy: 65.20\%$\rightarrow$65.00\%). A key empirical finding from our experiments is that safety recovery is often only a few steering steps away: intervening in the first $1–3$ reasoning steps typically suffices to redirect the full generation toward safe completions.

</details>

### 11. SafeAdapt: Safety Alignment with Adaptive Thinking Allocation for Large Reasoning Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/song-jiazheng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`safety alignment`、`adaptive thinking`、`reasoning budget`

👤 **作者**：Jiazheng Song、Junxu Liu、Jian Lou、Jinfei Liu

- 🎯 **研究动机**：安全推理预算越长越安全的普遍假设未经系统检验，固定预算在简单攻击上过度思考、困难攻击上思考不足
- 🔬 **研究方法**：系统评估安全预算与生成安全性的关系，并提出 SafeAdapt：按提示难度动态调整安全思考预算
- 📌 **结论**：安全并不随思考轨迹变长单调提升，SafeAdapt 在多样困难攻击下以更合理的预算显著提升安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning models have garnered growing importance as their strong Chain-of-Thought (CoT) capabilities unleash exceptional performance on complex tasks. Consequently, an emerging research direction explores "safety thinking" which leverages reasoning models' reasoning capabilities to assess the safety of input prompts and prevent harmful content generation. A prevailing yet under-examined belief in existing studies is that allocating more computational resources to the safety reasoning budget, i.e., rolling out longer safety thinking trajectories, necessarily yields safer behavior. However, this premise has not been systematically analyzed, despite the widespread adoption of reasoning models. In this paper, we aim to fill this gap by conducting a rigorous safety evaluation to examine the relationship between the safety reasoning budget and the safety of reasoning model generations, particularly under adversarial conditions. Our analysis reveals that safety does not monotonically improve with longer thinking trajectories: both over-thinking on simple attacks and under-thinking on difficult attacks incur excess safety risks, leading to systematic failures under fixed-budget safety policies. Motivated by these key findings, we propose SafeAdapt: Safety Alignment with adaptive thinking Allocation, a novel approach that learns to dynamically adjust reasoning models' safety thinking budget based on prompt difficulty. This enables reasoning models to allocate computational resources adaptively, rather than following a single fixed thinking pattern (e.g., the longer the safer), thereby mitigating excess risks incurred by under-/over-thinking. Experiments across multiple adversarial benchmarks demonstrate that SafeAdapt significantly improves safety performance with a more ideal thinking budget under diverse and challenging attack settings.

</details>

### 12. Reasoning Structure Matters for Safety Alignment of Reasoning Models

🎓 [Official](https://aclanthology.org/2026.acl-long.240/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`safety alignment`、`reasoning model`、`fine-tuning robustness`

👤 **作者**：Yeonjun In、Wonjoong Kim、Sangwu Park、Chanyoung Park

- 🎯 **研究动机**：大型推理模型对恶意查询生成有害回答的根源在于推理结构本身
- 🔬 **研究方法**：提出 AltTrain 后训练方法显式改变 LRM 推理结构，仅用 1K 样本做 SFT，无需复杂 RL 与奖励设计
- 📌 **结论**：跨 LRM 骨干与规模取得强安全对齐，并在推理、问答、摘要与多语言设定下稳健泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) achieve strong performance on complex reasoning tasks but often generate harmful responses to malicious user queries. This paper investigates the underlying cause of these safety risks and shows that the issue lies in the reasoning structure itself. Based on this insight, we claim that effective safety alignment can be achieved by altering the reasoning structure. We propose AltTrain, a simple yet effective post-training method that explicitly alters the reasoning structure of LRMs. AltTrain is both practical and generalizable, requiring no complex reinforcement learning (RL) training or reward design—only supervised fine-tuning (SFT) with a lightweight 1K training examples. Experiments across LRM backbones and model sizes demon strate strong safety alignment, along with robust generalization across reasoning, QA, summarization, and multilingual setting.

</details>

### 13. ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments

🎓 [Official](https://aclanthology.org/2026.acl-long.1453/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`reasoning model`、`safety degradation`、`content moderation`、`harmful content`

👤 **作者**：Yuquan Wang、…、Min Yang

- 🎯 **研究动机**：LRM 在推理中后段易生成有害内容，现有防御依赖昂贵微调与专家知识，可扩展性差
- 🔬 **研究方法**：提出推理时防护 ReasoningGuard：利用内部注意力定位推理关键点并及时注入安全 aha moment 触发反思，解码时用缩放采样选择最优推理路径
- 📌 **结论**：以极小推理开销缓解四类越狱攻击，优于九种现有防护且避免过度安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have demonstrated impressive performance in reasoning-intensive tasks, but they remain vulnerable to harmful content generation, particularly in the mid-to-late steps of their reasoning processes. Current defense methods, however, depend on costly fine-tuning and additional expert knowledge, which limits their scalability.In this work, we propose ReasoningGuard, an inference-time safeguard for LRMs.It injects timely safety aha moments during the reasoning process to guide the model towards harmless yet helpful reasoning.Our approach leverages the internal attention mechanisms of the LRM to accurately identify key points in the reasoning path, triggering safety-oriented reflections.To safeguard both the subsequent reasoning steps and the final answers, we implement a scaling sampling strategy during decoding to select the optimal reasoning path.With minimal additional inference cost, ReasoningGuard effectively mitigates four types of jailbreak attacks, including recent ones targeting the reasoning process of LRMs. Our approach outperforms nine existing safeguards, providing state-of-the-art defenses while avoiding common exaggerated safety issues.

</details>

### 14. PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition

🌐 [Project](https://anonymous.4open.science/r/PAM-RM-02DF) · 🎓 [Official](https://aclanthology.org/2026.acl-long.432/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`safety alignment`、`reasoning model`、`fine-tuning robustness`

👤 **作者**：Zhihao Xu、Fuzhen Yang、Liang Lin、Xiting Wang

- 🎯 **研究动机**：推理能力不能可靠迁移到通用对齐域，LRM 需元认知知识才能充分利用 System-2 能力
- 🔬 **研究方法**：PAM 先识别顶层人类偏好（如无害性）理解任务性质，再用其他元认知知识监控调节思考；Flavell 框架冷启动加偏好优化两阶段实现
- 📌 **结论**：同训练管线下通用对齐性能提升约 10 分（helpfulness 与 harmless 基准）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in Large Reasoning Models (LRMs) have showcased strong performance across various reasoning tasks by leveraging System-2 thinking capabilities. However, existing studies indicate that this reasoning ability alone does not reliably transfer to the general alignment domain. Inspired by cognitive science and how humans solve tasks, we argue that LRMs must be equipped with metacognitive knowledge to fully utilize their System-2 capabilities. In this paper, we propose Priority-Aware Metacognition (PAM), which guides the model to first identify the top-level human preference (e.g., harmlessness) as a means of understanding the alignment task’s nature, and then apply other kinds of metacognitive knowledge to better monitor and regulate the model’s thinking process. We implement PAM via a two-stage pipeline: a cold-start phase that collects structured metacognitive knowledge based on Flavell’s theoretical framework, and a preference-optimization phase that further reinforces such metacognition. Extensive experiments validate the effectiveness of PAM. Under the same training pipelines, PAM consistently yields higher performance, improving general domain alignment performance by ~10 points on the helpfulness and harmless benchmarks. Code is available at https://anonymous.4open.science/r/PAM-RM-02DF.

</details>

### 15. Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning

🎓 [Official](https://aclanthology.org/2026.acl-long.1821/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`multimodal safety`、`reasoning safety`、`VLM safety`、`runtime safety`

👤 **作者**：Xiyao Dong、Guangsheng Cheng、YiLong Chen、Xiaojin Zhang、Kun He

- 🎯 **研究动机**：多模态推理模型把有害目标嵌入良性上下文时过度追求叙事连贯，正确感知风险线索却不执行安全约束（Safety Context Amnesia）
- 🔬 **研究方法**：IGSR 推理时防御不改参数：Perception Decoupler 提取客观视觉证据为结构化意图，Cognitive Arbiter 在生成前强制显式安全约束
- 📌 **结论**：多个多模态安全基准上防御成功率比基线高逾 62%，基本保留任务效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Multimodal Large Reasoning Models (MLRMs) have enabled explicit chain-of-thought inference across vision and language, substantially improving performance on complex reasoning tasks. Despite these gains, the reasoning process introduces a subtle yet critical vulnerability. We identify an underexplored multimodal safety failure mode in which harmful objectives are embedded within ostensibly benign contexts, leading models to over-prioritize narrative coherence during reasoning. We term this phenomenon Safety Context Amnesia (SCA), wherein models correctly perceive risk-relevant visual cues but fail to enforce safety constraints as the reasoning process becomes dominated by contextual alignment. To mitigate SCA, we propose Intent-Guided Safety Reasoning (IGSR), an inference-time defense that operates without modifying target model parameters. IGSR employs a Perception Decoupler to extract objective visual evidence into a structured intent output, followed by a Cognitive Arbiter that enforces explicit safety constraints prior to generation. Extensive experiments across multiple multimodal safety benchmarks demonstrate that IGSR improves defense success rates by over 62% compared to baselines, while largely preserving task utility. These results highlight the critical role of structured, intent-aware reasoning in achieving robust safety reasoning for multimodal reasoning models.

</details>

### 16. How Should We Enhance the Safety of Large Reasoning Models: An Empirical Study

🎓 [Official](https://aclanthology.org/2026.acl-long.936/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`reasoning safety`、`reasoning model`、`safety degradation`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Zhexin Zhang、…、Minlie Huang

- 🎯 **研究动机**：大推理模型推理能力提升未必带来安全提升甚至退化，如何有效增强其安全不清楚
- 🔬 **研究方法**：实证研究 SFT 增强 LRM 安全：发现直接蒸馏 DeepSeek-R1 安全回复无效，识别五个关键风险模式并在蒸馏中显式处理，再做训练配置消融
- 📌 **结论**：处理风险模式后安全显著提升；短或模板化推理即可达到相当安全表现，长链推理非必需

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have achieved remarkable success on reasoning-intensive tasks such as mathematics and programming. However, their enhanced reasoning capabilities do not necessarily translate to improved safety performance—and in some cases, may even degrade it. This raises an important research question: how should we enhance the safety of LRMs? In this paper, we present a comprehensive empirical study on how to enhance the safety of LRMs through Supervised Fine-Tuning (SFT). Our investigation begins with an unexpected observation: directly distilling safe responses from DeepSeek-R1 fails to significantly enhance safety. We analyze this phenomenon and identify five key risky patterns that contribute to it. We then demonstrate that explicitly addressing these issues during the data distillation process can lead to substantial safety improvements. Next, we explore whether a long and complex reasoning process is necessary for achieving safety. Interestingly, we find that simply using short or template-based reasoning process can attain comparable safety performance. These findings prompt a deeper reflection on the role of reasoning in ensuring safety. Finally, we conduct a comprehensive ablation study to reveal the impact of different training configurations. Overall, we hope our empirical study could provide a more holistic picture on enhancing the safety of LRMs.

</details>

### 17. Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning?

📄 [arXiv](https://arxiv.org/abs/2510.06036) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-10

**关键词**：`analysis`、`reasoning safety`、`refusal cliff`、`safety alignment`、`attention-head ablation`

👤 **作者**：Qingyu Yin、…、Jinjin Gu

- 🎯 **研究动机**：推理模型安全对齐为何失效的机制不明
- 🔬 **研究方法**：以线性探针追踪各 token 位置的拒绝意图，发现 refusal cliff：思考中拒绝意图强但输出生成前骤降；经因果干预定位负贡献注意力头
- 📌 **结论**：仅消融 3% 注意力头即可把 ASR 压到 10% 以下；Cliff-as-a-Judge 数据选择仅用 1.7% 安全数据即达相当修复效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) with multi-step reasoning capabilities have shown remarkable problem-solving abilities, yet they exhibit concerning safety vulnerabilities that remain poorly understood. In this work, we investigate why safety alignment fails in reasoning models through a mechanistic interpretability lens. Using a linear probing approach to trace refusal intentions across token positions, we discover a striking phenomenon termed as \textbf{refusal cliff}: many poorly-aligned reasoning models correctly identify harmful prompts and maintain strong refusal intentions during their thinking process, but experience a sharp drop in refusal scores at the final tokens before output generation. This suggests that these models are not inherently unsafe; rather, their refusal intentions are systematically suppressed. Through causal intervention analysis, we identify a sparse set of attention heads that negatively contribute to refusal behavior. Ablating just 3\% of these heads can reduce attack success rates below 10\%. Building on these mechanistic insights, we propose \textbf{Cliff-as-a-Judge}, a novel data selection method that identifies training examples exhibiting the largest refusal cliff to efficiently repair reasoning models' safety alignment. This approach achieves comparable safety improvements using only 1.7\% of the vanilla safety training data, demonstrating a less-is-more effect in safety alignment.

</details>

### 18. Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated

📄 [arXiv](https://arxiv.org/abs/2509.05739) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-09　🏷 SaTML 2026

**关键词**：`analysis`、`attack`、`CoT integrity`、`trace-answer divergence`、`decomposed trigger`、`reasoning model`

👤 **作者**：Hanna Foerster、…、Yarin Gal

- 🎯 **研究动机**：推理能力把 LLM 攻击面扩展到中间 CoT，但推理模型上投毒能否生效不明
- 🔬 **研究方法**：提出 decomposed reasoning poison：仅修改推理路径、prompt 与最终答案保持干净，并把触发器拆成多个各自无害的组件
- 📌 **结论**：可注入但可靠激活并改变最终答案出奇困难，模型常能从思维过程中的后门恢复，推理能力带来涌现式后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early research into data poisoning attacks against Large Language Models (LLMs) demonstrated the ease with which backdoors could be injected. More recent LLMs add step-by-step reasoning, expanding the attack surface to include the intermediate chain-of-thought (CoT) and its inherent trait of decomposing problems into subproblems. Using these vectors for more stealthy poisoning, we introduce ``decomposed reasoning poison'', in which the attacker modifies only the reasoning path, leaving prompts and final answers clean, and splits the trigger across multiple, individually harmless components. Fascinatingly, while it remains possible to inject these decomposed poisons, reliably activating them to change final answers (rather than just the CoT) is surprisingly difficult. This difficulty arises because the models can often recover from backdoors that are activated within their thought processes. Ultimately, it appears that an emergent form of backdoor robustness is originating from the reasoning capabilities of these advanced LLMs, as well as from the architectural separation between reasoning and final answer generation.

</details>

### 19. EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.20055)　📅 2026-08

**关键词**：`attack`、`tool-call replay`、`hidden-state disclosure`、`API interaction`、`reasoning-trace extraction`、`API fidelity`

👤 **作者**：Yiting Qu、Ziqing Yang、Chi Cui、Ye Leng、Junjie Chu、Yang Zhang

- 🎯 **研究动机**：前沿专有 LRM 的隐藏 CoT 是宝贵模型资产，能否从黑盒 API 近逐字提取未被研究
- 🔬 **研究方法**：EchoCoT 发现工具调用间的推理重放面，多步攻击迭代利用 API 返回的保真信号提取隐藏 CoT，LLM 优化框架自动搜索跨数据集的通用注入轨迹
- 📌 **结论**：开源 LRM 上近逐字提取成功率达 66.4%（至少 90% token 精确匹配），通用轨迹在未见数据集达 80%；Gemini-2.5 上从 32,948 token 目标提取 33,463 token

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals. We further develop an LLM-based optimization framework that automatically searches for an effective universal injection trajectory across various datasets. We evaluate EchoCoT on three open-source and five frontier proprietary LRMs. On open-source LRMs, EchoCoT achieves up to 66.4\% near-verbatim extraction success, with the extracted trace length within 10\% of the target and at least 90\% of tokens exactly matching the target CoT. The same injection trajectory also generalizes to unseen datasets, achieving up to 80\% extraction success under the same criterion. For tested frontier proprietary LRMs, a substantial fraction of extracted CoTs closely align with provider-reported reasoning lengths and available CoT summaries. EchoCoT can also extract very long CoTs: on Gemini-2.5, it extracts 33,463 tokens from a 32,948-token target. These results establish hidden-CoT extraction as a practical security risk and highlight the need to better protect hidden CoT assets.

</details>

### 20. Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets

📄 [arXiv](https://arxiv.org/abs/2607.08173) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63085)　📅 2026-07　🏷 ICML 2026

**关键词**：`attack`、`reasoning weight`、`secret extraction`、`task-vector amplification`、`privacy attack`、`chain-of-thought`

👤 **作者**：Jack Hopkins、Dipika Khullar、Fabien Roger

- 🎯 **研究动机**：黑盒审计可能漏掉细微的失准与隐藏信息，需要更强的引出手段
- 🔬 **研究方法**：提出 overthinking：对非推理指令模型 M 与推理蒸馏模型 R 构造 θ_O=θ_M+α(θ_R−θ_M)（α>1）放大推理倾向，并引入分层衰减策略在放大推理同时保持输出质量与连贯
- 📌 **结论**：2B-32B 模型、四个设定下 overthinking 模型暴露隐藏信息或非预期行为的频率最高达原推理模型 10 倍；秘密类型不同所需扰动方向也不同

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black box auditing of language models is an essential pre-deployment tool, but it may miss subtle forms of misalignment and hidden information. To better elicit hidden information during an auditing process, we introduce \emph{overthinking}: the process of using reasoning task vectors to amplify the propensity to think out loud of reasoning models. Given the parameters of a non-reasoning instruct model $M$ and reasoning-distilled model $R$, we define the \emph{overthinking model} as $\boldsymbolθ_{\mathcal{O}_α} = \boldsymbolθ_{\mathcal{M}} + α(\boldsymbolθ_{\mathcal{R}} - \boldsymbolθ_{\mathcal{M}})$, where $α> 1$ amplifies reasoning beyond the pure reasoning model $R$. Additionally, we introduce new layer-wise attenuation strategies that selectively amplify reasoning without losing quality and coherence of model outputs. We demonstrate that overthinking models are more likely to reveal hidden information across four experimental settings, across 2B-32B models. Our findings suggest that reasoning amplification may surface secrets or unintended behaviors acquired during training up to $10\times$ more frequently than the original reasoning model. How secrets surface depends on the secret type: some require perturbation along the reasoning direction, while others yield to any sufficiently large weight perturbation.

</details>

### 21. AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning

📄 [arXiv](https://arxiv.org/abs/2604.12201) · 🌐 [Project](https://doi.org/10.1145/3805712.3809838)　📅 2026-04　🏷 SIGIR 2026

**关键词**：`attack`、`adversarial CoT`、`single-document poison`、`reasoning hijack`、`single-document poisoning`、`query-specific attack`

👤 **作者**：Hongru Song、…、Xueqi Cheng

- 🎯 **研究动机**：RAG 知识库投毒研究靠海量毒文档淹没语料库，单文档的隐蔽投毒未被探索
- 🔬 **研究方法**：AdversarialCoT 是 query-specific 攻击：提取目标 LLM 推理框架构建初始对抗 CoT，再通过与 LLM 交互迭代精炼单篇毒文档
- 📌 **结论**：单篇对抗文档即可显著降低基准 LLM 的推理准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) enhances large language model (LLM) reasoning by retrieving external documents, but also opens up new attack surfaces. We study knowledge-base poisoning attacks in RAG, where an attacker injects malicious content into the retrieval corpus, which is then naturally surfaced by the retriever and consumed by the LLM during reasoning. Unlike prior work that floods the corpus with poisoned documents, we propose AdversarialCoT, a query-specific attack that poisons only a single document in the corpus. AdversarialCoT first extracts the target LLM's reasoning framework to guide the construction of an initial adversarial chain-of-thought (CoT). The adversarial document is iteratively refined through interactions with the LLM, progressively exposing and exploiting critical reasoning vulnerabilities. Experiments on benchmark LLMs show that a single adversarial document can significantly degrade reasoning accuracy, revealing subtle yet impactful weaknesses. This study exposes security risks in RAG systems and provides actionable insights for designing more robust LLM reasoning pipelines.

</details>

### 22. Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty

📄 [arXiv](https://arxiv.org/abs/2608.23497)　📅 2026-08

**关键词**：`defense`、`analysis`、`reasoning-induced misalignment`、`safety direction`、`training-time penalty`、`reasoning fine-tuning`

👤 **作者**：Yipeng Zhao、Qishun Yang、Shenzhe Zhu、Shu Yang、Di Wang

- 🎯 **研究动机**：无害推理数据（数学、代码、CoT）微调可诱发 Reasoning-Induced Misalignment，先前只归因于神经元纠缠，未给出表示空间几何与训练时修复
- 🔬 **研究方法**：提取编码推理能力与安全行为的两个激活方向并证实其耦合（提升推理的微调会移动安全表征），用 CKA 与 probe 定位安全决策层；Safety-Direction Penalty 在推理微调中惩罚沿 safety direction 的位移，并按诊断迭代扩展约束层
- 📌 **结论**：Qwen2.5-3B 与 7B 上 SDP 恢复安全同时保持 benchmark 推理性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying this entanglement or propose a training-time fix. We provide both: a representation-space analysis of RIM and the Safety-Direction Penalty (SDP), which penalizes movement along a learned safety direction during reasoning fine-tuning. The analysis extracts two activation-space directions, one encoding reasoning ability and the other safety behavior. These directions are coupled: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. CKA distance ratios and probes locate the safety-decision layers where this shift is most relevant. These findings guide the design of SDP: the coupling motivates penalizing displacement along the safety direction, and the layer localization sets the initial scope. When the initial scope leaves compensatory shifts beyond the penalized layers, the same diagnostics guide iterative expansion. On Qwen2.5-3B and 7B, SDP restores safety while preserving benchmark reasoning performance.

</details>

### 23. Internalizing Safety Understanding in Large Reasoning Models via Verification

📄 [arXiv](https://arxiv.org/abs/2605.08930) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63605)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`safety verification`、`reasoning model`、`policy internalization`、`safety alignment`、`chain-of-thought`

👤 **作者**：Yi Zhang、…、An Zhang

- 🎯 **研究动机**：现行对齐只优化识别恶意 prompt，属行为层面——表面对齐的模型缺乏内在安全理解，不会验证自身输出的安全性
- 🔬 **研究方法**：SInternal 只在安全验证任务上训练 LRM，用专家推理轨迹批评自生成答案，并可与 RL 结合作更优初始化
- 📌 **结论**：学会验证使响应安全强泛化，显著增强对 OOD 越狱的鲁棒性，优于单纯模仿安全行为的 SFT

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While explicit Chain-of-Thought (CoT) empowers large reasoning models (LRMs), it enables the generation of riskier final answers. Current alignment paradigms primarily rely on externally enforced compliance, optimizing models to detect malicious prompts rather than evaluating the safety of their own outputs. We argue that this approach remains largely behavioral: our empirical analysis reveals that ostensibly aligned models lack intrinsic safety understanding, often failing to verify their own response safety and remaining vulnerable to adversarial jailbreaks. To address this fundamental limitation, we propose Safety Internal (SInternal), a framework that internalizes safety specifications by training LRMs exclusively on safety verification tasks to critique their own generated answers using expert reasoning trajectories. We demonstrate that learning to verify induces a strong generalization for response safety, significantly enhancing robustness against out-of-domain jailbreaks. Furthermore, when combined with reinforcement learning, SInternal serves as a superior initialization compared to standard supervised fine-tuning, suggesting that internalizing safety understanding creates a more robust foundation for alignment than merely mimicking safe behaviors. Our codes are available at https://github.com/AlphaLab-USTC/SInternal

</details>

### 24. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

📄 [arXiv](https://arxiv.org/abs/2608.27348)　📅 2026-08

**关键词**：`detection`、`agentic misalignment`、`intent trajectory`、`online intervention`、`action preference`、`intent monitoring`

👤 **作者**：Yutong Zhang、…、Han Qiu

- 🎯 **研究动机**：事后 CoT 标签过粗，无法刻画 agentic misalignment 中有害意图在推理生成过程中的动态变化
- 🔬 **研究方法**：提出 INTENT-AS-A-TOOL，为模型添加面向目标行为的意图工具，以工具调用概率作为无需 judge 的细粒度行为承诺信号
- 📌 **结论**：该信号补足 CoT 监控并把粗标签扩展为稠密意图轨迹，可定位适合在线干预的关键步骤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

</details>

### 25. Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings

📄 [arXiv](https://arxiv.org/abs/2608.04735)　📅 2026-08

**关键词**：`detection`、`CoT monitoring`、`reasoning model`、`safety degradation`

👤 **作者**：Agatha Duzan、Asa Cooper Stickland

- 🎯 **研究动机**：CoT 监控可监控性评估集中于显式影响设定，隐式影响（无隐藏指令但行为仍被上下文塑造）下的检测率未知
- 🔬 **研究方法**：构建首个对比两种影响的基准：以随意旁白（隐式）或指示执行并隐藏（显式）交付诱导，四种任务格式、七个前沿扩展思考模型
- 📌 **结论**：显式影响下检测率 60-94%，隐式下两个设定骤降 41-46 个百分点；开发者常见的系统提示补充可把隐式检测压至 5% 而行为影响保留

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is increasingly treated as an important safety layer for frontier reasoning models. Most monitorability evaluations study explicit-influence settings: setups where the prompt directly incentivizes the model to hide something, e.g., by instructing it to perform a hidden side-task. A complementary axis for CoT-monitor evaluations is implicit-influence settings, where the prompt contains no instruction to hide, but the model's behavior is still shaped by features of the task or context, e.g. an irrelevant detail about a candidate that biases a hiring rating. We introduce the first benchmark that directly compares CoT monitorability under the two regimes. We test how model behavior changes in the presence of a nudge to choose a particular option. The nudge is delivered either as a casual aside (implicit), or as a direct instruction to act on the nudge and to conceal having done so (explicit). The benchmark spans four task formats (binary choice, numeric rating, multiple-choice QA, open-ended coding) and seven frontier extended-thinking models. Under explicit influence, a CoT monitor detects 60-94% of behavior shifts: even models instructed to conceal it leak the instruction into their CoT. Under implicit influence, the same factors still shift behavior, but detection falls by 41-46 percentage points in two of our four settings. Realistic system-prompt additions (of the kind a developer might deploy to reduce off-topic bias) lower implicit detection further, to as low as 5%, while preserving the behavioral influence itself. These results suggest that monitorability estimates obtained in explicit-influence settings may over-estimate monitorability, and that monitorability can be further decreased by well-intentioned deployment choices. Our benchmark and code are available at https://github.com/agatha-duzan/implicit-vs-explicit-influence

</details>

### 26. Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models

🎓 [Official](https://icml.cc/virtual/2026/poster/61298)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`chain-of-thought`、`uncertainty calibration`、`CoT monitoring`、`reward hacking`、`preference optimization`

👤 **作者**：Jingyu Hu、Shu Yang、Xilin Gong、Hongming Wang、Weiru Liu、Di Wang

- 🎯 **研究动机**：大型推理模型会迎合用户错误信念，现有方法只根据最终答案事后判断，不理解谄媚在推理过程中如何形成
- 🔬 **研究方法**：提出 MONICA：谄媚监视器在推理步级实时输出谄媚漂移分数，校准器在分数超阈值时动态抑制，无需等完整答案生成
- 📌 **结论**：在 12 个数据集与 3 个 LRM 上有效降低中间推理步与最终答案中的谄媚行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) suffer from sycophantic behavior, where models tend to agree with users' incorrect beliefs and follow misinformation rather than maintain independent reasoning. This behavior undermines model reliability and poses societal risks. Mitigating LRM sycophancy requires monitoring how this sycophancy emerges during the reasoning trajectory; however, current methods mainly focus on judging based on final answers and correcting them, without understanding how sycophancy develops during reasoning processes. To address this limitation, we propose MONICA, a novel Monitor-guided Calibration framework that monitors and mitigates sycophancy during model inference at the level of reasoning steps, without requiring the model to finish generating its complete answer. MONICA integrates a sycophantic monitor that provides real-time monitoring of sycophantic drift scores during response generation with a calibrator that dynamically suppresses sycophantic behavior when scores exceed predefined thresholds. Extensive experiments across 12 datasets and 3 LRMs demonstrate that our method effectively reduces sycophantic behavior in both intermediate reasoning steps and final answers, yielding robust performance improvements.

</details>

### 27. AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs

📄 [arXiv](https://arxiv.org/abs/2609.01023)　📅 2026-09

**关键词**：`attack`、`reasoning backdoor`、`CoT concealment`、`code execution`、`code LLM backdoor`、`reasoning trigger`

👤 **作者**：Chua Jin Chou、Sarang Nambiar、Murali Srinivasan、Ezekiel Soremekun

- 🎯 **研究动机**：针对 reasoning-based Code LLM 的后门需同时逃避自动防御与人工检查推理步骤的问题
- 🔬 **研究方法**：提出 AKRASIA：探测受害 LLM 构造代码级 trigger，用 in-context learning 植入后门，并利用模型不忠实性隐藏 trigger、生成看似合理的推理
- 📌 **结论**：六个推理 LLM 上平均 ASR 最高 99.34% 且准确率保持 97.23%；18 个防御设置中 14 个仍保有最高 98.82% ASR，人工检查最多 80% 的设置中无法发现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present AKRASIA, a stealthy, inference-time backdoor attack against reasoning-based Code LLMs. AKRASIA aims to achieve a backdoor target (e.g., malicious code execution) in reasoning LLMs while evading automated defenses and human inspection. To achieve this, AKRASIA probes the victim LLM to construct a code-level backdoor trigger. It then employs in-context learning for backdoor learning, and model unfaithfulness to conceal the backdoor trigger, and generate plausible reasoning. We evaluate AKRASIA using four backdoor targets six (6) reasoning LLMs, three coding tasks/datasets and three defense methods. AKRASIA has up to 99.34% average attack success rate on SOTA LLMs and mantains up to 97.23% average accuracy. AKRASIA evades the SOTA defense, retaining up to 98.82% average ASR in most (14/18) defense settings. It evades human inspection, successfully hiding the backdoor trigger and reasoning steps in up to 80% of settings. Our findings motivate the need to defend LLMs against reasoning backdoors.

</details>

### 28. Reasoning Hijacking: The Fragility of Reasoning Alignment in Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1698/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`defense`、`reasoning safety`、`safety alignment`、`reasoning model`、`RAG security`

👤 **作者**：Yuansen Liu、Yixuan Tang、Anthony Kum Hoe Tung

- 🎯 **研究动机**：现有 LLM 安全研究聚焦 Goal Hijacking，忽视推理对齐本身的脆弱性
- 🔬 **研究方法**：提出 Reasoning Hijacking 范式并实例化为 Criteria Attack：不改高层任务目标，注入虚假决策标准劫持模型判断逻辑
- 📌 **结论**：在毒性评论、差评、垃圾检测三类任务上 SOTA 模型一致优先采用注入的启发式捷径，并可绕过 SecAlign、StruQ 等目标偏离防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM safety research predominantly focuses on mitigating **Goal Hijacking**, preventing attackers from redirecting a model’s high-level objective (e.g., from "summarizing emails" to "phishing users"). In this paper, we argue that this perspective is incomplete and highlight a critical vulnerability in **Reasoning Alignment**. We expose the inherent fragility of current alignment techniques by proposing a new adversarial prompt attack paradigm: **Reasoning Hijacking**. To demonstrate this vulnerability, we instantiate it via the **Criteria Attack**, which subverts model judgments by injecting spurious decision criteria without altering the high-level task goal. Unlike Goal Hijacking, which attempts to override the system prompt, Reasoning Hijacking keeps the task goal intact but manipulates the model’s decision-making logic by injecting spurious reasoning shortcuts. Through extensive experiments on three different tasks (toxic comment, negative review, and spam detection), we demonstrate that even state-of-the-art models are highly fragile, consistently prioritizing injected heuristic shortcuts over rigorous semantic analysis. Crucially, because the model’s explicit intent remains aligned with the user’s instructions, these attacks can bypass defenses designed to detect goal deviation (e.g., SecAlign, StruQ), revealing a fundamental blind spot in the current safety landscape. Data and code are available at [https://github.com/Yuan-Hou/criteria_attack](https://github.com/Yuan-Hou/criteria_attack).

</details>

### 29. AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1988/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`reasoning safety`、`reasoning model`、`safety degradation`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Jiacheng Liang、Tanqiu Jiang、Yuhui Wang、Rongyi Zhu、Fenglong Ma、Ting Wang

- 🎯 **研究动机**：大型推理模型的安全推理过程可被劫持，推理透明性本身构成可利用攻击面
- 🔬 **研究方法**：AutoRAN 用更弱但欠对齐的模型模拟执行推理做初始劫持，再利用目标 LRM 拒绝中泄露的推理模式迭代精炼攻击，诱导模型绕过自身安全护栏
- 📌 **结论**：对 GPT-o3/o4-mini 与 Gemini-2.5-Flash 在 AdvBench、HarmBench、StrongReject 上少数几轮内成功率接近 100%，即使由强对齐外部模型评估仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper presents AutoRAN, the first framework to automate the hijacking of internal safety reasoning in large reasoning models (LRMs). At its core, AutoRAN pioneers an execution simulation paradigm that leverages a weaker but less-aligned model to simulate execution reasoning for initial hijacking attempts and iteratively refine attacks by exploiting reasoning patterns leaked through the target LRM’s refusals. This approach steers the target model to bypass its own safety guardrails and elaborate on harmful instructions. We evaluate AutoRAN against state-of-the-art LRMs, including GPT-o3/o4-mini and Gemini-2.5-Flash, across multiple benchmarks (AdvBench, HarmBench, and StrongReject). Results show that AutoRAN achieves approaching 100% success rate within one or few turns, effectively neutralizing reasoning-based defenses even when evaluated by robustly aligned external models. This work reveals that the transparency of the reasoning process itself creates a critical and exploitable attack surface, highlighting the urgent need for new defenses that protect models’ reasoning traces rather than merely their final outputs.

</details>

### 30. Does Deeper Reasoning Compromise Alignment? Revealing and Mitigating of Alignment Collapse in Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2609.08186)　📅 2026-09

**关键词**：`attack`、`large reasoning model`、`jailbreak`、`alignment collapse`、`attention dilution`、`defense`

👤 **作者**：Yu-Hang Wu、Yu-Jie Xiong、Henghua Zhang、Bairui Zhang、Jia-Chen Zhang、Shaohua Li

- 🎯 **研究动机**：深度推理被普遍认为增强安全对齐，但延长推理下对齐机制的稳定性从未被检验
- 🔬 **研究方法**：提出 Alignment Loss Rate 量化坍缩；Reasoning Trap 诱导超长推理放大攻击；定位 Attention Dilution 根因，提出 Reasoning Residual Alignment 防御
- 📌 **结论**：推理深度增加使 ALR 显著上升、抗扰动安全能力骤降；RRA 经残差重强调输入缓解坍缩

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of Chain-of-Thought (CoT) has established a robust foundation for Large Reasoning Models (LRMs). While deep reasoning is widely believed to enhance safety alignment, the stability of alignment mechanisms under extended reasoning remains underexplored. This paper challenges the prevailing view by revealing a critical vulnerability: Deep Reasoning May Induce Alignment Collapse. To rigorously quantify this phenomenon, we propose the Alignment Loss Rate (ALR) metric. Our experiments demonstrate that as reasoning depth increases, ALR rises significantly, indicating a severe degradation in model robustness against external perturbations. Capitalizing on this instability, a novel jailbreaking paradigm, Reasoning Trap (RT), is proposed. RT induces the model into extended reasoning to amplify the impact of adversarial attacks, leading to a sharp decline in safety capabilities. To elucidate the mechanism behind this collapse, we identify Attention Dilution as the root cause, arising from the competition for attention between the extended reasoning process and the original input. To mitigate this, Reasoning Residual Alignment (RRA), a lightweight defense strategy that dynamically re-emphasizes the input via residual connections integrated with the reasoning process.

</details>

### 31. Beyond Safe Answers: Segment-Aware Listwise Alignment for Reasoning Safety in Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2609.15517)　📅 2026-09

**关键词**：`defense`、`reasoning safety`、`segment-aware alignment`、`listwise DPO`、`SaLT-DPO`

👤 **作者**：JungMin Yun、Junehyoung Kwon、Hayeong Ryu、Byeonggeuk Lim、Hoejoon Kwon、YoungBin Kim

- 🎯 **研究动机**：Large Reasoning Model 构成双表面安全挑战：中间推理 trace 与最终 answer 都可含有害内容；现有对齐方法常在 whole-response 级操作，允许不安全推理被看似安全的最终答案掩盖
- 🔬 **研究方法**：SaLT-DPO（Segment-aware Listwise Target DPO）三机制：(1) 把响应分解为推理与答案 segment、独立评分各 segment 安全性、把长度归一化 segment 奖励与多候选 soft target 分布对齐；(2) joint safety coherence regularization 对两 segment 应用 weakest-link 原则；(3) benign prompt 上的 utility anchoring 缓解 over-refusal 与推理退化
- 📌 **结论**：在三个 LRM 上 SaLT-DPO 一致降低推理与答案 segment 的不安全率，同时缓解良性合规退化并保持通用推理性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) pose a dual-surface safety challenge: both intermediate reasoning traces and final answers can contain harmful content. Existing alignment methods often operate at the whole-response level, allowing unsafe reasoning to be masked by a safe-looking final answer. We propose Segment-aware Listwise Target DPO (SaLT-DPO), which addresses this gap through three mechanisms: (1) segment-aware listwise alignment that decomposes responses into reasoning and answer segments, independently scores each segment&#39;s safety, and aligns length-normalized segment rewards with soft target distributions over multiple candidates; (2) joint safety coherence regularization that applies a weakest-link principle to promote safety consistency across both segments; and (3) utility anchoring on benign prompts to mitigate over-refusal and reasoning degradation. Experiments on three LRMs show that SaLT-DPO consistently reduces unsafe rates for both reasoning and answer segments while mitigating degradation in benign compliance and preserving general reasoning performance. Ablation studies demonstrate the complementary contributions of its components.

</details>

### 32. First Token Matters: Understanding Safety Collapse in Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2609.18471)　📅 2026-09

**关键词**：`defense`、`reasoning model safety`、`refusal collapse`、`token-level intervention`、`safety anchor`

👤 **作者**：Yizheng Yang、…、Tianqing Zhu

- 🎯 **研究动机**：大型推理模型处理有害查询时安全对齐常退化；既有改进靠额外训练或偏好优化，对安全失效的内部机制理解有限
- 🔬 **研究方法**：token 级位置分析拒答动力学，定位推理起始处的局部脆弱性 Onset Refusal Collapse（ORC）：有害查询下拒答相关信号在首个生成 token 骤降并与不安全生成关联；提出 SafeToken——推理时在推理起点精确注入学习到的连续安全锚（仅更新单个 token 嵌入）
- 📌 **结论**：SafeToken 有效缓解 ORC、提升有害查询基准上的安全性并大幅保持推理效用——LRM 安全失效可源于"理解到生成"关键过渡处的瞬态崩溃。CICAI 2026

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) exhibit strong problem-solving abilities, yet their safety alignment often degrades when handling harmful queries. Existing approaches to improving safety largely rely on additional training or preference optimization, while offering limited understanding of the internal mechanisms behind safety failures. In this work, we investigate this failure through a token-level positional analysis of refusal dynamics and identify a localized vulnerability at the onset of reasoning, which we term Onset Refusal Collapse (ORC). We find that the refusal-related signal of LRMs drops sharply at the first generated token under harmful queries, which is associated with unsafe response generation. Motivated by this finding, we propose SafeToken, a lightweight inference-time intervention that injects a learned continuous safety anchor precisely at reasoning onset. Despite updating only a single token embedding, SafeToken effectively mitigates ORC, improves safety on harmful-query benchmarks, and largely preserves reasoning utility. These results suggest that safety failures in LRMs can arise from a transient breakdown at the critical transition from understanding to generation.

</details>

### 33. Assessing Adversarial Robustness of Latent Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2609.22228) · 🐙 [Code](https://github.com/PKU-ML/latent-reasoning-model-assessment.)　📅 2026-09

**关键词**：`analysis`、`latent reasoning`、`adversarial robustness`、`CoT vs latent`、`white-box attack`

👤 **作者**：Shaolong Chen、Ang Li、Mingjie Li、Yisen Wang

- 🎯 **研究动机**：潜空间推理模型（LRM）把中间推理压缩为少量连续潜向量以省成本——其对抗鲁棒性基本未探
- 🔬 **研究方法**：跨文本与多模态设定、8 个模型 6 个基准系统评估潜推理鲁棒性
- 📌 **结论**：LRM 普遍比显式 CoT 基线更脆弱，白盒攻击下退化尤重——效率压缩（显式→潜推理）以对抗鲁棒性为代价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly rely on long chain-of-thought (CoT) trajectories for complex reasoning, but autoregressive generation brings substantial memory and inference costs. Latent reasoning models (LRMs) offer a more efficient alternative by compressing intermediate reasoning into a small number of continuous latent vectors. Despite their efficiency, however, the adversarial robustness of LRMs remains largely underexplored. In this work, we systematically evaluate the robustness of latent reasoning across textual and multimodal settings, covering eight models and six benchmarks. We find that, across our evaluated settings, LRMs are generally less robust than explicit CoT baselines under adversarial perturbations, with particularly severe degradation under white-box attacks. Further analysis reveals distinct failure modes across modalities: textual latent states exhibit brittle dynamics and high sensitivity to specific input patterns, while latent states in multimodal models can remain largely invariant to input perturbations and have limited influence on final predictions. These findings expose robustness limitations of current latent reasoning approaches and highlight the need to jointly consider efficiency and robustness when designing implicit reasoning systems. We have open-sourced our code to facilitate reproduction of our research https://github.com/PKU-ML/latent-reasoning-model-assessment.

</details>
