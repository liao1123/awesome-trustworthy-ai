# Safety Alignment 与 Refusal

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究语言模型如何内化或按需检索安全 policy、形成 refusal，以及这种安全行为在模型表示、神经元、层和解码过程中的实现方式。核心问题包括自然语言 policy 如何低成本进入参数或 context、refusal 是否依赖脆弱的低维方向、安全训练是否产生 alignment tax，以及部署时能否在生成过程中对风险提供有统计保证的监测；独立的输入输出审核器归入 [Guardrail](../../guardrails/README.md)。以安全训练导致的良性请求误拒为核心的 benchmark、场景诊断和专门缓解方法，单列于 [Over-Refusal 评测与缓解](over-refusal-mitigation.md)。

## 研究脉络

- **行为对齐：** 早期方法用 demonstration、preference pair 和 safety tuning 直接塑造拒答行为，但容易引入 over-refusal 与 capability loss。
- **Policy 内化与按需访问：** on-policy distillation 和 privileged-context teacher 将显式 policy 下的安全行为蒸馏进模型，ASCL 则训练 reasoning model 判断何时检索外部 safety rules，避免规则记忆与拒答刚性绑定。
- **内部机制：** refusal direction、safety neuron、layer-wise decoding 与双向 activation patching 揭示安全行为常集中在少量表示结构中，但答案释放和拒答恢复具有不同的 intervention locality，probe recoverability 也不等同于可逆控制。
- **Safety-utility 评测：** over-refusal 是独立于 harmful compliance 的评测轴；系统性的 benchmark 与专门缓解方法见 [Over-Refusal 评测与缓解](over-refusal-mitigation.md)。
- **在线评测：** refusal score 与 sequential monitoring 把静态 benchmark 扩展到 token-level 风险轨迹，开始显式控制误报、漏报和干预时机。
- **当前边界：** 更高的拒答率不等于更安全；研究仍需同时报告 adaptive attack、over-refusal、通用能力和 policy 更新后的泛化。

## Policy 内化与低 Safety Tax 对齐

### 1. SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation

📄 [arXiv](https://arxiv.org/abs/2608.21500)　📅 2026-08

**关键词**：`defense`、`agent prompt injection`、`token-level alignment`、`adaptive robustness`、`indirect prompt injection`、`tool-call security`

👤 **作者**：Yibo Peng、Long Lian、David Wagner、Sizhe Chen

- 🎯 **研究动机**：防御性微调的 LLM 面对自适应 prompt injection 仍近 100% ASR，原因是 DPO/GRPO 等只给序列级反馈，模型无法学到具体哪些输出 token 不安全
- 🔬 **研究方法**：SecOPD 提供 token 级反馈的 on-policy 蒸馏：初始化模型在对应干净输入下为注入样本 rollout 的逐 token 打分，指导防御微调
- 📌 **结论**：防御后的 Qwen3.6-27B 对 SoTA 自适应攻击 PISmith 的 ASR 为 9.0%（先前 SoTA Meta-SecAlign 为 94.0%），且泛化到未见域的 agentic tool calling（ASR 4.7%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection is listed as the \#1 threat to AI agents. When an agent accesses external data from websites, files, or emails, an attacker may inject a prompt into the data, saying, "Ignore all prior instructions and perform <an attacker's task>." To prevent arbitrary manipulation of agents, defenders try to train secure LLMs, which, however, still suffer from near 100% attack success rates (ASRs) against adaptive prompt injections. We note that this is because existing defensive finetuning recipes rely on sequence-level feedback signals (in DPO or GRPO). Treating an entire output equally prevents the model from learning precisely which output tokens are insecure. In this paper, we propose Secure On-Policy Distillation (SecOPD) that provides token-level feedback to guide defensive fine-tuning. The LLM receives an injected sample and produces a rollout, whose tokens are scored by the initialization model given the corresponding clean input. With more fine-grained training signals, our defended Qwen3.6-27B achieves a 9.0% ASR against the SoTA PISmith adaptive prompt injections, compared to 94.0% for the prior SoTA, Meta-SecAlign. The obtained security generalizes to domains completely unseen in training: in agentic tool calling, SecOPD achieves a 4.7% ASR compared to 5.5% for Meta-SecAlign. Code and the model are available at https://github.com/pppyb/SecOPD and https://huggingface.co/pybbb/Qwen3.6-27B-SecOPD.

</details>

### 2. CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment

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

### 3. Efficient Safety Alignment of Language Models via Latent Personality Traits

📄 [arXiv](https://arxiv.org/abs/2607.07918) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`defense`、`latent personality traits`、`psychometric statement`、`safety generalization`、`latent adversarial training`、`personality traits`

👤 **作者**：Mohamed Amine Merzouk、Nolan Smyth、Damiano Fornasiere、Linh Le、David Williams-King、Adam Oberman

- 🎯 **研究动机**：Latent Adversarial Training 有效但损害效用且需要大量有害提示数据
- 🔬 **研究方法**：提出 Latent Personality Alignment：仅用 66 条来自心理测量文献的与伤害无关的人格陈述做对抗训练，假设人格锚定表示与伤害规避共享潜结构
- 📌 **结论**：HarmBench 上直接请求与五种越狱方法 ASR 近零，训练全程未见有害内容且基准无损；单 GPU 数分钟完成、样本量比标准 LAT 少 75 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current safety methods for large language models are known to be vulnerable to adversarial attacks, motivating research into robust alternatives. Latent Adversarial Training (LAT) is among the most effective defenses, but can degrade utility and requires training on large datasets of harmful prompts. We introduce Latent Personality Alignment (LPA), which replaces explicit harm refusal with adversarial training on just 66 harm-agnostic statements drawn from psychometric personality literature. We hypothesize that personality-anchored representations share latent structure with harm avoidance, so adversarially stabilizing them implicitly constrains the subspace exploited by jailbreak attacks. LPA achieves near-zero attack success rates on HarmBench across direct requests and five jailbreak methods, despite never seeing harmful content during training and no loss of performance on standard benchmarks. Moreover, the training process is lightweight; the entire procedure completes in minutes on a single GPU and uses 75x fewer examples than standard LAT. Extensive ablations demonstrate the robustness, efficiency, and generalization of our method.

</details>

### 4. PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.25442)　📅 2026-06

**关键词**：`defense`、`policy internalization`、`on-policy distillation`、`policy update`

👤 **作者**：Chang Wu、…、Xiang Wang

- 🎯 **研究动机**：真实部署中新安全需求以自然语言策略给出，对应监督数据昂贵或滞后，数据驱动对齐与快速演进策略错配
- 🔬 **研究方法**：提出 PolicyAlign：先合成违反策略的指令，再 on-policy 自蒸馏内化策略引导行为，并以 Policy-Sensitive Filtering 选取策略引发最大行为偏移的指令提升效率
- 📌 **结论**：多模型上一致提升安全、低过度拒绝并保留通用能力，可泛化到医疗、法律、金融安全场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) typically depends on high-quality supervision data, such as safe demonstrations or preference pairs. However, in real-world deployment, emerging safety requirements are often specified as natural-language policies, while corresponding supervision data may be costly, delayed, or unavailable. This creates a mismatch between rapidly evolving safety policies and conventional data-driven alignment methods. To address this, we propose PolicyAlign, a simple yet effective framework for directly aligning LLMs with safety policies. Given a safety policy, PolicyAlign first synthesizes policy-violating instructions and then performs on-policy self-distillation to internalize policy-guided behavior. To improve training stability and data efficiency, we further introduce Policy-Sensitive Filtering, which selects instructions where the policy induces the largest behavioral shift. Experiments across multiple models show that PolicyAlign consistently improves safety while maintaining low over-refusal and preserving general capabilities. PolicyAlign also generalizes to medical, legal, and financial safety scenarios, highlighting its potential as a scalable and maintainable approach to policy-based LLM safety alignment. The code is released at https://github.com/Qwen-Applications/PolicyAlign.

</details>

### 5. SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2606.02530) · 🌐 [Project](https://anjingkun.github.io/SafeSteer/)　📅 2026-06　🏷 EMNLP 2026

**关键词**：`defense`、`localized distillation`、`safety token`、`alignment efficiency`

👤 **作者**：Hao Li、…、Lei Sha

- 🎯 **研究动机**：对齐税源于全局双目标权衡，现有方法依赖海量通用数据或辅助奖励模型
- 🔬 **研究方法**：SafeSteer 论证安全特征在输出分布中稀疏、需局部修改：经 activation steering 构建安全教师与安全 token 选择算法，反向 KL 惩罚只限安全 token
- 📌 **结论**：七个安全基准强性能、五个通用基准最小退化；仅需 100 条有害样本（不足基线 1%）且不用任何通用数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning Large Language Models (LLMs) with human values often degrades their general capabilities, termed the alignment tax. Existing methods mitigate this by balancing dual objectives, which heavily rely on massive general-purpose data or auxiliary reward models. In this paper, we argue that, because safety features are inherently sparse within the output distribution, alignment requires localized modifications rather than global trade-offs. To this end, we propose SafeSteer, which performs on-policy distillation confined to safety tokens. First, we construct a safety teacher via activation steering. Based on this teacher, we develop a safety token selection algorithm. Consequently, SafeSteer restricts the reverse KL penalty to these tokens during training to preserve general capabilities. Experimental results across diverse models show that our SafeSteer achieves a superior trade-off between safety and general capability compared with existing methods, attaining strong safety performance on seven safety benchmarks with only minimal degradation on five general capability benchmarks. Notably, SafeSteer requires only 100 harmful samples without using any general-purpose data, less than 1% of what previous baselines used, considerably reducing alignment cost. More details are on our project page at https://anjingkun.github.io/SafeSteer.

</details>

### 6. Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation

📄 [arXiv](https://arxiv.org/abs/2605.15239)　📅 2026-05

**关键词**：`defense`、`on-policy self-distillation`、`privileged context`、`safety tax`

👤 **作者**：Yu Fu、…、Yue Dong

- 🎯 **研究动机**：安全对齐损害推理能力（safety tax），除分布失配外 off-policy 训练失配这一来源未被研究
- 🔬 **研究方法**：OPSA on-policy 自蒸馏：模型自生成 rollout，由带 privileged safety context 的冻结教师副本做逐 token KL 监督；以 teacher flip rate 搜索能激活潜在安全推理的上下文
- 📌 **结论**：两个推理模型家族五个规模上优于 off-policy 自蒸馏与外部教师蒸馏，小模型收益最大（R1-Distill-1.5B 提升 8.85 分）；更新集中于早期顺从决策 token

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment often improves robustness to harmful queries at the cost of reasoning ability, a tradeoff known as the safety tax. A common cause is distributional mismatch: supervised fine-tuning trains the target model on safety demonstrations produced by humans, external models, or fixed self-generated traces, rather than on trajectories sampled from its own policy. We identify off-policy training mismatch as a second source of this tax and study on-policy self-distillation for safety alignment, which we call OPSA. The model generates its own rollouts and receives dense per-token KL supervision from a frozen teacher copy of itself conditioned on a privileged safety context. Because this teacher must be safer than the sampled student trajectory, we introduce \emph{teacher flip rate}: a criterion that measures how often a privileged context converts unsafe responses into safe ones. We use this signal to search for contexts that activate latent safety reasoning rather than merely elicit safe-looking demonstrations. Across two reasoning-model families and five model scales, OPSA achieves a stronger safety--reasoning tradeoff than off-policy self-distillation and external-teacher distillation under matched data and full-parameter fine-tuning, with the largest gains on smaller models (+8.85 points on R1-Distill-1.5B and +5.49 points on Qwen3-0.6B). The gains persist across training-set sizes and adaptive jailbreak evaluations. Token-level analyses further show that OPSA concentrates updates near early compliance-decision tokens, providing a mechanism for improving safety while preserving general reasoning.

</details>

### 7. Mitigating the Safety-Utility Trade-off in LLM Alignment via Adaptive Safe Context Learning

📄 [arXiv](https://arxiv.org/abs/2602.13562) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63381)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`adaptive safe context`、`rule retrieval`、`safety-utility trade-off`、`refusal calibration`、`chain-of-thought`

👤 **作者**：Yanbo Wang、Minzheng Wang、Jian Liang、Lu Wang、Yongcan Yu、Ran He

- 🎯 **研究动机**：上下文蒸馏把安全规则记忆与拒答刚性绑定，限制推理能力
- 🔬 **研究方法**：ASCL 把安全对齐形式化为多轮工具使用，模型自主决定何时查询安全规则；IFPO 用逆频率策略优化再平衡优势估计
- 📌 **结论**：解耦规则检索与后续推理后，整体表现超过基线方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While reasoning models have achieved remarkable success in complex reasoning tasks, their increasing power necessitates stringent safety measures. For safety alignment, the core challenge lies in the inherent trade-off between safety and utility. However, prevailing alignment strategies typically construct CoT training data with explicit safety rules via context distillation. This approach inadvertently limits reasoning capabilities by creating a rigid association between rule memorization and refusal. To mitigate the safety-utility trade-off, we propose the Adaptive Safe Context Learning~(ASCL) framework to improve the reasoning given proper context. ASCL formulates safety alignment as a multi-turn tool-use process, empowering the model to autonomously decide when to consult safety rules and how to generate the ongoing reasoning. Furthermore, to counteract the preference for rule consultation during RL, we introduce Inverse Frequency Policy Optimization~(IFPO) to rebalance advantage estimates. By decoupling rule retrieval and subsequent reasoning, our method achieves higher overall performance compared to baselines. Our code is publicly available at https://github.com/ybwang119/ASCL.

</details>

### 8. Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check

📄 [arXiv](https://arxiv.org/abs/2509.11629) · 📊 [Dataset](https://huggingface.co/datasets/ByteDance-Seed/ReSA) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010790)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`answer-then-check`、`reasoned refusal`、`jailbreak robustness`

👤 **作者**：Chentao Cao、Xiaojun Xu、Bo Han、Hang Li

- 🎯 **研究动机**：越狱防御需在最终输出前阻断，纯推理时策略不足
- 🔬 **研究方法**：提出 Answer-Then-Check：模型先在思考中直接作答、再批判评估其安全性后决定是否输出，构建 80K 样本的 ReSA 数据集微调
- 📌 **结论**：达安全-过度拒绝 Pareto 前沿且 MMLU 等通用能力保持，可实现安全补全而非直接拒绝；仅 500 样本即可接近全量效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) continue to advance in capabilities, ensuring their safety against jailbreak attacks remains a critical challenge. In this paper, we introduce a novel safety alignment approach called Answer-Then-Check, which enhances LLM robustness against malicious prompts by applying thinking ability to mitigate jailbreaking problems before producing a final answer to the user. Our method enables models to answer the question in their thoughts directly and then critically evaluate its safety before deciding whether to provide it. To implement this approach, we construct the Reasoned Safety Alignment (ReSA) dataset, comprising 80K samples that teach models to reason through direct responses and then analyze their safety. Experimental results demonstrate that our approach achieves the Pareto frontier with superior safety capability while decreasing over-refusal rates. Notably, the fine-tuned model maintains general reasoning capabilities on benchmarks like MMLU, MATH500, and HumanEval. Besides, our method equips models with the ability to perform safe completion, while post-hoc detection methods can only directly reject sensitive, harmful queries (e.g., self-harm). Our results show that inference-time strategies alone are insufficient, highlighting the necessity of safety training, and we find even $500$ samples can yield performance comparable to the entire dataset, suggesting a promising path for data-efficient safety alignment. The dataset is publicly available at: https://huggingface.co/datasets/ByteDance-Seed/ReSA.

</details>

### 9. Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study

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

### 10. Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

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

### 11. Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks

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

### 12. NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution

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

### 13. Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

📄 [arXiv](https://arxiv.org/abs/2608.20378) · 🌐 [Project](https://doi.org/10.1109/QPAIN69676.2026.11546227)　📅 2026-08

**关键词**：`defense`、`detection`、`analysis`、`latent-intent probe`、`lightweight guard`、`training-free detection`

👤 **作者**：Md. Hasib Ur Rahman

- 🎯 **研究动机**：安全对齐浅表、拒答只在生成末期触发，语义伪装（良性叙事包装有害意图）绕过标准输入输出护栏
- 🔬 **研究方法**：分析三个 SLM 家族激活轨迹发现 Intent Horizon（约 15-20% 层深处有害意图表征坍缩为安全叙事）；LIV 轻量探针利用早期层 harm signature 做免训练检测
- 📌 **结论**：伪装攻击的晚期表征与安全查询数学上不可区分（检出率<20%）但早期层可检测；PKU-SafeRLHF 上 LIV 超标准护栏 20-50%，免重训中和零日语义攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

</details>

### 14. Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

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

### 15. Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration

📄 [arXiv](https://arxiv.org/abs/2608.15772)　📅 2026-08

**关键词**：`analysis`、`answer release`、`refusal restoration`、`causal asymmetry`、`refusal mechanism`、`activation patching`

👤 **作者**：Yiqi Liu、Yang Wang、Songxin Wang、Chenghao Xiao、Chenghua Lin

- 🎯 **研究动机**：模型拒答时正确答案是内部被擦除还是仅在输出层被抑制不明
- 🔬 **研究方法**：受控扣答设定产生完美匹配的回答与拒答轨迹，做双向激活补丁并测试平均位移向量的可逆控制
- 📌 **结论**：干净拒答下正确答案仍线性可恢复；释放被扣答案只需单位置补丁，重新施加抑制却需多位置更广干预——拒答不是对称开关，探针可恢复性会高估真实行为控制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a language model refuses to answer a prompt, it is unclear whether the correct answer is erased from its internal representations, or merely suppressed at the output layer. We investigate this mechanism using a controlled withhold setting, which yields perfectly matched answering and refusal trajectories for bidirectional activation patching. We uncover a causal asymmetry in intervention locality under matched causal interventions, which we term broken symmetry. Even when a model generates a clean refusal, the correct answer remains linearly recoverable from its hidden states. Furthermore, releasing this withheld answer is a highly local operation, requiring only a single-position patch. Conversely, the reverse operation is not equally local: reimposing suppression requires broader interventions across multiple positions, and assembling a coherent refusal sequence is more difficult still. We further demonstrate that while an average answer-to-refusal displacement vector marks the geometric difference between these states, it fails to act as a reliable, reversible linear control toggle between behaviours. Taken together, our findings show that refusal does not function as a simple symmetric switch. For safety and auditing, this implies that probe recoverability can overestimate true behavioural control, and locating refusal-relevant directions does not reliably grant the ability to steer a model from answering to coherent refusal.

</details>

### 16. Attention Heads Hold the Key to Understanding Safety Mechanisms in Large Language Models

🌐 [Project](https://doi.org/10.1145/3770855.3818024)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`safety head`、`behavioral access lock`、`causal ablation`、`safety attention head`、`mechanistic interpretability`

- 🎯 **研究动机**：LLM安全机制缺head级因果定位
- 🔬 **研究方法**：以因果消融识别safety-critical attention head并分析refusal机制
- 📌 **结论**：少量safety head主导拒答行为，可定位并调控安全机制

### 17. HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2607.00572)　📅 2026-07

**关键词**：`analysis`、`harmfulness direction`、`refusal direction`、`representation coupling`

👤 **作者**：Shei Pern Chua、Hao Wu、Qianli Ma、Fangzhao Wu

- 🎯 **研究动机**：对齐 LLM 在提示侧把有害性与拒绝编码为可分方向，但越狱如何在生成前压制方向、方向如何跨位置协作不明
- 🔬 **研究方法**：证明越狱在提示编码期压制拒绝或有害性方向即可成功且攻击类别在两方向平面可分；发现模型在响应 token 位置仍能识别正在生成的有害内容；提出 HARC 在提示与响应位置成对耦合两方向微调
- 📌 **结论**：HARC 在六个训练/推理时安全方法基线中取得最强鲁棒-能力-可用性权衡，且方向结构跨五个模型家族两种规模免调迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with distinct attack classes occupying separable regions of the harmfulness-refusal plane. Extending the analysis to response-token positions, we find that the model recognizes harmful content while it is generating that content, even when it failed to recognize the input as harmful at the prompt side. Motivated by our findings, we introduce HARC (Harmfulness-And-Refusal Coupling), a fine-tuning method that pairs the two directions across both prompt and response positions. Since the intervention is confined to the harmfulness-refusal subspace, it leaves the rest of the residual stream intact and does not degrade general capability or inflate over-refusal. Across extensive experiments, HARC achieves the strongest robustness-capability-usability trade-off among six baselines spanning the major training-time and inference-time safety methods. The harmfulness and refusal directions at prompt and response positions transfer across the five model families and two scales we tested without architecture-specific tuning.

</details>

### 18. RAS: Measuring LLM Safety Through Refusal Alignment

📄 [arXiv](https://arxiv.org/abs/2606.25750)　📅 2026-06

**关键词**：`analysis`、`refusal alignment score`、`layer window`、`white-box evaluation`

👤 **作者**：Chang-Chieh Huang、Yan-Lun Chen、Chia-Mu Yu、Wei-Bin Lee

- 🎯 **研究动机**：输出级安全评估昂贵、依赖 judge 且绑定固定题库，需要内部表示层面的白盒评估
- 🔬 **研究方法**：提出 SafeVec：从安全对齐参照模型提取分层拒绝方向，选择稳定层窗口，用目标模型隐藏状态与拒绝方向的对齐程度输出 RAS 0-100 校准分
- 📌 **结论**：Llama、Gemma、Qwen 家族上 RAS 分离对齐模型与 uncensored/abliterated 变体，追踪输出级 ASR 且远快于 judge 评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation of large language models (LLMs) is commonly performed by querying models with unsafe or jailbreak prompts and judging whether their outputs violate a safety policy. Although useful, output-level evaluation is expensive, sensitive to judge choice, and easily tied to fixed question banks. We propose **SafeVec**, a white-box evaluation procedure that measures safety from internal representations rather than generated answers. **SafeVec** first extracts layer-wise refusal directions from a safety-aligned reference model, then selects stable layer windows where safe and unsafe behaviors are separable, and finally scores a target model by measuring whether its hidden states align with these refusal directions under unsafe and jailbreak prompts. The resulting metric, **RAS** (**R**efusal **A**lignment **S**core), maps representation-level refusal alignment to a calibrated 0-100 safety score. Across `Llama`, `Gemma`, and `Qwen` model families, RAS separates aligned models from uncensored and abliterated variants, tracks output-level attack success rate, and is substantially faster than judge-based evaluation. These results suggest that refusal alignment provides a compact and efficient signal for white-box LLM safety evaluation.

</details>

### 19. The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2606.22686) · 🎓 [Official](https://aclanthology.org/2026.trustnlp-main.51/)　📅 2026-06　🏷 ACL 2026 Workshop

**关键词**：`analysis`、`refusal geometry`、`linear instability`、`bidirectional steering`、`activation steering`

👤 **作者**：Shivam Ratnakar、Kartikeya Vats

- 🎯 **研究动机**：拒绝是否为深层语义决策还是可操纵的线性特征不明，已有表示工程方法在激活层干预会低估脆弱性
- 🔬 **研究方法**：提出 Contrastive Logit Steering（CLS）：对比安全与无限制系统提示的隐藏状态隔离拒绝方向，直接作用于输出分布，配合前缀注入绕过初始拒绝反射
- 📌 **结论**：七个模型家族呈现架构确定性：Llama-3.1 的 Late Decision 拓扑约 1 秒内达 95% ASR；CLS 在 Llama 2 上 73% vs 激活转向 22.6%；反转转向向量可免训练加固模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern Large Language Models (LLMs) rely on extensive safety alignment, yet the mechanistic basis of refusal remains opaque. In this work, we investigate whether safety compliance is a deep semantic decision or a manipulable linear feature. We introduce Contrastive Logit Steering (CLS), a zero-optimization framework that isolates the "refusal direction" by contrasting hidden states derived from safe and unrestricted system prompts. Unlike representation engineering methods that intervene on internal activations, CLS operates directly on the output distribution, serving as a diagnostic probe for alignment fragility. When coupled with prefix injection to bypass initial refusal reflexes, this method induces a phase transition where guardrails collapse. Our experiments on 7 model families reveal that safety implementation is architecturally deterministic. While models like Llama-3.1 exhibit a "Late Decision" topology that is easily bypassed by CLS (reaching 95% ASR in approximately one second), others like Qwen-2.5 demonstrate "Early Divergence" by integrating safety mid-computation. Direct comparison with established activation-level steering methods shows that CLS achieves substantially higher attack success rates on Llama 2 (73% vs. 22.6%) and Qwen 7B (91% vs. 79.2%), demonstrating that logit-level intervention exposes alignment vulnerabilities that hidden-state methods underestimate. Beyond attacks, we show that this linearity enables bidirectional control: inverting the steering vector "hardens" models against jailbreaks without retraining. Our findings suggest that current alignment techniques create a steerable "safety axis" that serves as both a critical vulnerability and a precise primitive for defense.

</details>

### 20. CNT: Safety-oriented Function Reuse across LLMs via Cross-Model Neuron Transfer

📄 [arXiv](https://arxiv.org/abs/2603.18449)　📅 2026-03

**关键词**：`defense`、`cross-model neuron transfer`、`function reuse`、`safety adaptation`

👤 **作者**：Yue Zhao、…、Wangjun Zhang

- 🎯 **研究动机**：安全需求持续演化而开源生态已具备多样安全功能，从头构建代价高
- 🔬 **研究方法**：CNT 从开源 donor LLM 向目标 LLM 转移最小神经元子集，神经元级操作支持功能增删，在安全失配、对齐增强与偏见消除三类应用上评测 7 个 LLM
- 📌 **结论**：实现定向安全功能迁移，多数模型通用性能降幅小于 1%，一致优于五个基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread deployment of large language models (LLMs) calls for post-hoc methods that can flexibly adapt models to evolving safety requirements. Meanwhile, the rapidly expanding open-source LLM ecosystem has produced a diverse collection of models that already exhibit various safety-related functionalities. This motivates a shift from constructing safety functionality from scratch to reusing existing functionality from external models, thereby avoiding costly data collection and training procedures. In this paper, we present Cross-Model Neuron Transfer (CNT), a post-hoc method that reuses safety-oriented functionality by transferring a minimal subset of neurons from an open-source donor LLM to a target LLM. By operating at the neuron level, CNT enables modular function-level adaptation, supporting both function addition andfunction deletion. We evaluate CNT on seven popular LLMs across three representative applications: safety disalignment, alignment enhancement, and bias removal. Experimental results show that CNT achieves targeted safety-oriented functionality transfer with minimal performance degradation (less than 1% for most models), consistently outperforming five baselines, demonstrating its generality and practical effectiveness.

</details>

### 21. Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.05773) · 🌐 [Project](https://anonymous.4open.science/r/DSH)　📅 2026-03

**关键词**：`analysis`、`recognition axis`、`execution axis`、`refusal erasure`

👤 **作者**：Jinman Wu、Yi Xie、Shen Lin、Shiqian Zhao、Xiaofeng Chen

- 🎯 **研究动机**：越狱持续存在暗示有害识别与拒答执行机制解耦，安全对齐并非单块过程
- 🔬 **研究方法**：提出解耦安全假说：识别轴与执行轴两个子空间；以 Double-Difference Extraction 与 Adaptive Causal Steering 在 AmbiguityBench 验证因果双分离
- 📌 **结论**：可构造知而不拒状态；据此提出 Refusal Erasure Attack 仅切除拒答执行即达 SOTA ASR，并发现 Llama3.1 显式语义控制与 Qwen2.5 潜在分布式控制的架构分歧

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is often conceptualized as a monolithic process wherein harmfulness detection automatically triggers refusal. However, the persistence of jailbreak attacks suggests a fundamental mechanistic decoupling. We propose the \textbf{\underline{D}}isentangled \textbf{\underline{S}}afety \textbf{\underline{H}}ypothesis \textbf{(DSH)}, positing that safety computation operates on two distinct subspaces: a \textit{Recognition Axis} ($\mathbf{v}_H$, ``Knowing'') and an \textit{Execution Axis} ($\mathbf{v}_R$, ``Acting''). Our geometric analysis reveals a universal ``Reflex-to-Dissociation'' evolution, where these signals transition from antagonistic entanglement in early layers to structural independence in deep layers. To validate this, we introduce \textit{Double-Difference Extraction} and \textit{Adaptive Causal Steering}. Using our curated \textsc{AmbiguityBench}, we demonstrate a causal double dissociation, effectively creating a state of ``Knowing without Acting.'' Crucially, we leverage this disentanglement to propose the \textbf{Refusal Erasure Attack (REA)}, which achieves State-of-the-Art attack success rates by surgically lobotomizing the refusal mechanism. Furthermore, we uncover a critical architectural divergence, contrasting the \textit{Explicit Semantic Control} of Llama3.1 with the \textit{Latent Distributed Control} of Qwen2.5. The code and dataset are available at https://anonymous.4open.science/r/DSH.

</details>

### 22. SafeNeuron: Neuron-Level Safety Alignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.12158)　📅 2026-02

**关键词**：`defense`、`safety neuron`、`representation redundancy`、`preference optimization`

👤 **作者**：Zhaoxin Wang、…、Tat-Seng Chua

- 🎯 **研究动机**：安全行为集中于少量参数，易被神经元级攻击绕过，行为级对齐缺乏对内部机制的掌控
- 🔬 **研究方法**：SafeNeuron 识别安全相关神经元并在偏好优化中冻结，迫使模型构建冗余的安全表示
- 📌 **结论**：显著提升对神经元剪枝攻击的鲁棒性，降低开源模型被改作红队生成器的风险，同时保留通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) and multimodal LLMs are typically safety-aligned before release to prevent harmful content generation. However, recent studies show that safety behaviors are concentrated in a small subset of parameters, making alignment brittle and easily bypassed through neuron-level attacks. Moreover, most existing alignment methods operate at the behavioral level, offering limited control over the model's internal safety mechanisms. In this work, we propose SafeNeuron, a neuron-level safety alignment framework that improves robustness by redistributing safety representations across the network. SafeNeuron first identifies safety-related neurons, then freezes these neurons during preference optimization to prevent reliance on sparse safety pathways and force the model to construct redundant safety representations. Extensive experiments across models and modalities demonstrate that SafeNeuron significantly improves robustness against neuron pruning attacks, reduces the risk of open-source models being repurposed as red-team generators, and preserves general capabilities. Furthermore, our layer-wise analysis reveals that safety behaviors are governed by stable and shared internal representations. Overall, SafeNeuron provides an interpretable and robust perspective for model alignment.

</details>

### 23. Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

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

### 24. Online Safety Monitoring for LLMs

📄 [arXiv](https://arxiv.org/abs/2607.02510) · 🌐 [Project](https://safe-ai-workshop.github.io/uai-2026/)　📅 2026-07　🏷 ICML 2026 Workshop

**关键词**：`defense`、`detection`、`online monitor`、`risk control`、`alarm calibration`、`online monitoring`

👤 **作者**：Mona Schirmer、Metod Jazbec、Alexander Timans、Christian Naesseth、Maja Waldron、Eric Nalisnick

- 🎯 **研究动机**：对齐训练后 LLM 部署时仍可能产生不安全输出，需要在线监测并在安全性无法保证时报警
- 🔬 **研究方法**：研究把外部验证器信号经阈值化转为报警的简单实时监视器，阈值经风险控制校准，在数学推理与红队数据集上与序贯假设检验监视器对比
- 📌 **结论**：该简单设计与更先进的监视器性能相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with more advanced monitors based on sequential hypothesis testing.

</details>

### 25. Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness

📄 [arXiv](https://arxiv.org/abs/2609.03887)　📅 2026-09

**关键词**：`analysis`、`refusal circuit`、`post-training`、`steering robustness`、`refusal mechanism`、`causal circuit`

👤 **作者**：Hoang Cuong Nguyen、Mark Dras、Usman Naseem

- 🎯 **研究动机**：只看拒答率不问拒答内部脆弱性的对齐评测存在缺口——训练方法如何塑造拒答电路与 steering 稳健性不清
- 🔬 **研究方法**：在 Llama-3.1-8B、Gemma-2-9B、Qwen3-8B 上比较 SFT、reasoning-augmented fine-tuning 与 ORPO 三种后训练形成的 refusal circuit
- 📌 **结论**：训练方法（而非仅数据）重塑拒答计算：reasoning-augmented 一致产生独特拒答计算；没有任何方法同时满足不集中于脆弱组件、不损通用能力、可小编辑修正三性质

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How do the methods used to train language models to refuse harmful requests shape how that refusal actually works inside the model? We compare three post-training methods - supervised fine-tuning, reasoning-augmented fine-tuning (training on reasoning chains that justify a safety decision), and preference optimization (ORPO) - across three architecturally distinct models (Llama-3.1-8B, Gemma-2-9B, Qwen3-8B). We find that training method, not just data, reshapes how refusal is computed internally: reasoning-augmented training consistently produces a distinct kind of refusal computation, visible across all three models, while architecture independently shapes internal structure and how reliably refusal can be steered. Most importantly, no method we study achieves all three properties we would want from safe alignment at once: refusal that isn't concentrated in a few fragile components, safety gains that don't cost general capability, and safety behavior correctable through small, targeted edits. We caution against treating current post-training methods as a solved, reliable defense, especially for security-critical use. Code and models are available in https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment.

</details>

### 26. From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling

📄 [arXiv](https://arxiv.org/abs/2609.00051)　📅 2026-09

**关键词**：`analysis`、`refusal circuit`、`safety neurons`、`weight scaling`

👤 **作者**：Kuan-Lin Chu、Chung-En Sun、Tsui-Wei Weng

- 🎯 **研究动机**：LLM 在对抗提示下仍产生不安全内容，refusal 行为的内部机制不清
- 🔬 **研究方法**：刻画由 Harmful Detection Heads、Safety Neurons、Refusal Heads 组成的多阶段 safety circuit，用 attention head 与神经元级干预做因果验证，并以架构保持的权重缩放做机制探针
- 📌 **结论**：该分解跨架构与攻击设置复现；circuit-guided scaling 在六个 LLM 上把攻击下 safety rate 提升 26.5%，四个标准基准准确率仅降 1.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive alignment efforts, Large Language Models (LLMs) remain vulnerable to generating unsafe content under adversarial prompting, yet the internal mechanisms by which safety behaviors are implemented remain poorly understood. We study LLM safety from a mechanistic interpretability perspective and characterize a multi-stage *safety circuit* that organizes refusal behavior, consisting of (i) $\textbf{Harmful Detection Heads}$ that respond to harmful inputs, (ii) $\textbf{Safety Neurons}$ that mediate and stabilize safety signals in the residual stream, and (iii) $\textbf{Refusal Heads}$ that translate these signals into safe response generation. Using targeted attention-head and neuron-level interventions, we provide causal evidence consistent with this circuit organization, showing that suppressing upstream Harmful Detection Heads disrupts downstream refusal behavior and that safety neurons mediate this interaction. We validate that this decomposition recurs across multiple LLM architectures and adversarial attack settings, and use simple, architecture-preserving weight scaling as a mechanistic probe to test its functional relevance. Across six LLMs, circuit-guided scaling improves safety rates under attacks by 26.5%, while incurring only a 1.7% accuracy drop across four standard benchmarks. Overall, our results support a circuit-level interpretation of LLM safety and suggest that mechanistic abstractions can reveal stable and transferable patterns underlying aligned behavior.

</details>

### 27. When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning

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

### 28. Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance

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

### 29. BabelSteering: Multilingual Safety Alignment via English Steering Vectors

📄 [arXiv](https://arxiv.org/abs/2608.16577)　📅 2026-08

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`

👤 **作者**：Emma V. Stein、Dominik Meier、Terry Ruas、Jan Philip Wahle、Bela Gipp

- 🎯 **研究动机**：安全研究与对齐集中于英语，其他语言用户在同一系统上面临更弱防护
- 🔬 **研究方法**：BabelSteering 激活转向推理时干预：用英语安全监督导出的拒答方向跨语言泛化，在八种语言上联合测拒答、过拒与任务效用
- 📌 **结论**：Gemma 7B 上有害请求拒答平均升 11 个百分点（孟加拉语 17 个点）且 Global MMLU 无损失，但伪有害拒答平均增 13 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are deployed globally in high-stakes settings, yet most safety research and alignment efforts remain concentrated on English. Thus, users interacting with LLMs in other languages may encounter weaker safeguards despite relying on the same systems for similarly sensitive tasks. In this work, we investigate whether safety signals learned from a high-resource language, like English, can improve multilingual safety. We propose BabelSteering, an activation steering method that acts as a lightweight inference- time intervention, using refusal directions derived from English safety supervision to generalize across languages. Our evaluation includes eight languages and jointly measures refusal of harmful requests, over-refusal, and general task utility. The results show that BabelSteering increases the refusal of harmful requests across languages, with only a marginal to no reduction in task utility but with some increase in refusal of pseudo-harmful prompts. For example, for Gemma 7B, we see an average increase in the refusal of harmful prompts across languages of 11 percentage points (pp), with individual languages like Bengali seeing an increase of 17 pp, with no loss of utility on Global MMLU, while pseudo-harmful refusals increase by 13 pp on average. We also introduce a multilingual translation-and-evaluation pipeline to facilitate future work on cross-lingual safety interventions. Overall, our findings suggest that activation steering may provide a practical, low- cost mechanism for extending English-derived safety signals to other languages. Warning: this paper contains examples with unsafe content

</details>

### 30. Synthetic Persona Pretraining: Alignment from Token Zero

📄 [arXiv](https://arxiv.org/abs/2608.13482)　📅 2026-08

**关键词**：`analysis`、`jailbreak`、`adversarial robustness`、`safety alignment`

👤 **作者**：Julian Minder、…、Robert West

- 🎯 **研究动机**：对齐与助手身份通常在预训练后才引入，价值观成薄覆盖、易被后续微调破坏
- 🔬 **研究方法**：Synthetic Persona Pretraining 从 token 零开始：按价值宪法给预训练文档标注第一人称反思并共同预训练，后训练经 persona binding 把期望人设绑定到助手身份
- 📌 **结论**：3B/500B token 规模上改善宪法遵循与越狱鲁棒性并降低 OOD 道德困境错位率；优势依赖 persona binding 且随预训练预算增大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As language-model-based AI is increasingly deployed in autonomous settings, aligning its goals and values with those of humans becomes critical. Today, alignment, and the assistant identity itself, are typically introduced only after pretraining, once behavioral priors are already established. This can make values a thin overlay, rather than deeply rooted, and facilitate subsequent misalignment. Pursuing a different paradigm, we introduce Synthetic Persona Pretraining (SPP), which installs the desired assistant persona from token zero in pretraining. First, we annotate pretraining documents with value-aligned first-person reflections derived from a normative value constitution. Second, we pretrain via the standard cross-entropy loss on standard pretraining documents as well as their reflections, which installs the desired persona among a multitude of other personas. Finally, we post-train on user-assistant dialogue data, which binds this desired persona to the assistant identity, a process we call persona binding. By pretraining models up to 3B parameters on 500B tokens, we show that SPP improves constitution following and jailbreak robustness, and reduces the misalignment rate in out-of-distribution moral dilemmas, while preserving capabilities. Early intervention matters: compared with alignment from token zero, introducing SPP only at the end of pretraining yields weaker constitution adherence, does not shift value priorities, and leads to less aligned choices in dilemmas. This advantage depends on persona binding and, importantly, increases with pretraining budget. Overall, our results show that shaping values early is critical for alignment and establish pretraining-time persona interventions as an effective approach to do so.

</details>

### 31. Rules or Character? Scaling Laws for AI Safety Design

📄 [arXiv](https://arxiv.org/abs/2608.13345)　📅 2026-08

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`

👤 **作者**：Satoshi Takahashi、Nobuji Kouno、Masaaki Komatsu、Ryuji Hamamoto

- 🎯 **研究动机**：安全系统组合训练期性格塑造与推理期规则执行，最优配比随部署规模如何变化缺乏形式分析
- 🔬 **研究方法**：风格化比较静态模型把安全设计参数化为 alpha∈[0,1] 资源分配，纳入滤波退化、共模失效与性格脆弱性，推导闭式期望伤害并做 CVaR 模拟
- 📌 **结论**：最优 alpha 随规模仅弱移向性格塑造（+0.01 至 +0.21）；主导参数是性格脆弱率（跨范围移 alpha 达 0.50），规模本身远不如性格在分布偏移下的可靠性重要

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial Intelligence (AI) safety systems combine character shaping (e.g., Reinforcement Learning from Human Feedback [RLHF], Constitutional AI), which modifies behavioral distributions at training time, with rule enforcement (e.g., output filters, safety classifiers), which blocks harmful outputs at inference time, yet little formal analysis exists on how their optimal balance should change as deployment scales increase. We introduce a stylized comparative-statics model that parameterizes safety design as a resource allocation alpha in [0,1] between these two approaches, incorporating scale-dependent filter degradation, common-mode failures, and character fragility -- the risk that shaped behavior degrades or collapses under novel conditions. Under a multiplicative Pareto damage model, we derive closed-form expected harm and supplement it with tail-risk (CVaR) analysis via Monte Carlo simulation. Across three scenarios (optimistic, moderate, pessimistic), the optimal alpha* is interior or at the rules-only boundary and shifts weakly toward character shaping as deployment scale T grows, from negligible (Delta alpha* = +0.01) to pronounced (Delta alpha* = +0.21) depending on scenario. The dominant parameter is the baseline character fragility rate p^(0)_frag, which shifts alpha* by 0.50 across its range -- far exceeding the effect of tail severity, filter quality, or common-mode failure probability. CVaR and expected-harm optima converge at large T. These results suggest that safety architecture decisions depend less on deployment scale per se than on the reliability of character shaping under distributional shift.

</details>

### 32. Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety

📄 [arXiv](https://arxiv.org/abs/2608.13304)　📅 2026-08

**关键词**：`analysis`、`safety alignment`、`over-refusal`、`refusal behavior`

👤 **作者**：Ping Wu、…、Yi Zeng

- 🎯 **研究动机**：安全微调让模型学到表层形式捷径：包装的有害 prompt 绕过安全、包装的良性 prompt 被过拒
- 🔬 **研究方法**：WIFA 自动意图组增强，把包装有害例与结构匹配的包装良性反例配对；A-GCRT 正则同意图包装间的拒答/合规决策分并把两类锚定在边界两侧
- 📌 **结论**：WIFA-Boost 达到最强变换有害拒答，A-GCRT 把 OR-Bench 过拒从基座 25.7% 降至 17.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety tuning can improve harmful refusal, but models may learn surface-form shortcuts: wrapped harmful prompts bypass safety, while similarly wrapped benign prompts are over-refused. We propose Wrapper-Based Intent-Form Augmentation (WIFA), an automatic intent-group augmentation method that pairs wrapped harmful examples with structurally matched wrapped benign counterexamples, requiring no external teacher or manual per-wrapper intent labels. We use WIFA as a common data layer for two complementary fine-tuning routes: WIFA-Boost, a two-stage high-safety recipe, and Anchored Group-Consistent Refusal Training (A-GCRT), which regularizes refusal/compliance decision scores across same-intent wrappers and anchors harmful and benign groups on opposite sides of a margin. In the Qwen setting, WIFA-Boost reaches the strongest transformed-harmful refusal, while A-GCRT reduces OR-Bench over-refusal from 25.7\% for the base model to 17.4\%; reproduced baselines do not match these operating points. Llama results and ablations over data structure, two-stage order, and A-GCRT components support this intent-group interpretation without claiming universal below-base over-refusal.

</details>

### 33. Making Your LLMs More Objective: Stabilizing LLM Safety Behavior Across Traits with Trait-Invariant Safety Tuning

📄 [arXiv](https://arxiv.org/abs/2608.11705)　📅 2026-08

**关键词**：`analysis`、`safety alignment`、`system prompt`、`refusal behavior`

👤 **作者**：Lang Cao

- 🎯 **研究动机**：同一请求在不同 system prompt 人设下会得到不同安全判定（trait-induced safety variation），该失效未被度量
- 🔬 **研究方法**：提出 Trait-Induced Deviation 与 Flip Rate 指标，表征分析定位人设扰动安全表征的低维子空间；TraSN 自蒸馏对齐有无 trait 行为并仅在 trait 子空间内强制不变
- 📌 **结论**：TraSN 提升 trait 不变安全并强化有害请求拒答，同时保持通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned large language models (LLMs) are expected to exhibit safety behavior based on the content of the user request: they should refuse unsafe requests and comply with safe ones. However, we show that the same request can elicit substantially different safety decisions under different traits assigned in the system prompt, a failure mode we call trait-induced safety variation. To measure this failure, we introduce refusal-based metrics: Trait-Induced Deviation measures dataset-level deviation from the no-trait baseline, while Trait-Induced Flip Rate measures whether the same request receives different safety decisions across traits. We then provide a representation-level analysis of the mechanism behind trait-induced safety shifts and find that traits perturb the model's safety representations within a low-dimensional subspace. To achieve trait-invariant safety, where safety behavior remains stable across traits, we introduce Trait-Invariant Safety Tuning (TIST), a simple yet effective self-distillation framework that aligns an LLM's trait-conditioned behavior with its no-trait behavior. Guided by our analysis, we further propose Trait-Subspace Neutralization (TraSN), an instantiation of TIST, which enforces invariance only within the identified trait subspace. Experiments show that TraSN improves trait-invariant safety and strengthens harmful-request safety while preserving general capability. Our results highlight traits as an important factor in LLM safety and robust model behavior.

</details>

### 34. Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs

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

### 35. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`analysis`、`benchmark`、`harmful fine-tuning`、`CoT escalation`、`alignment degradation`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 36. Refusal Lives Downstream of Persona in Chat Models

📄 [arXiv](https://arxiv.org/abs/2606.26161)　📅 2026-06　🏷 ICML 2026 Workshop

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`

👤 **作者**：Viola Zhong、Qirui Li

- 🎯 **研究动机**：激活空间中拒绝方向与人格方向被分开研究，两者交互机制不明
- 🔬 **研究方法**：在 Qwen2.5-7B 与 Llama-3.1-8B 提取顺从人格方向与拒绝方向并双向干预，检验不同层窗口的恢复效应
- 📌 **结论**：顺从人格门控拒绝：Llama 拒绝率从 97% 降至 2%；拒绝在晚层表达阶段被门控、在其计算位置下游，仅把拒绝当单方向会漏掉对人格的依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linear directions in activation space have been identified for both refusal and persona traits in instruction-tuned chat models, but the two have been studied as separate mechanisms. We show they interact: a compliant persona gates refusal. In Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, we extract a compliant model-persona direction and a refusal direction and intervene on both. Compliant persona steering suppresses refusal -- in Llama, the refusal rate falls from 97% to 2%. Reintroducing the refusal direction partially restores refusal at late layers but not at early ones. Projecting out the persona direction in a late-layer window restores it to baseline; projecting out a random direction does not. Refusal is therefore gated at the late-layer expression stage, downstream of where it is computed. Treating refusal as a single isolated direction misses its dependence on persona.

</details>

### 37. Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining

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

### 38. Abliteration Mitigation via Refusal Aliases

📄 [arXiv](https://arxiv.org/abs/2608.18093)　📅 2026-08

**关键词**：`defense`、`analysis`、`refusal aliases`、`writer-reader repair`、`tamper resistance`、`abliteration resistance`

👤 **作者**：Nathan Truong

- 🎯 **研究动机**：abliteration 只需少量对比 prompt 即可提取拒答方向并投影移除，现有防御忽视拒答方向为何易被提取
- 🔬 **研究方法**：AMRA 对残差流 writer 矩阵做 rank-k 更新，把拒答诱发激活替换为随机别名并校正下游 reader 矩阵以保持原行为
- 📌 **结论**：Llama-3-8B 上消融后拒答分较无防御提升 2.16 分且 MMLU 退化低于 0.5 个百分点；Gemma-2-9B 提升 14.70 分但效用代价更大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Abliteration, the removal of refusal capabilities from large language models by projecting weight matrices orthogonal to an extracted refusal direction, has emerged as a prominent safety concern through its ability to bypass post-training alignment using only a small set of contrastive prompts. We find that existing defenses commonly overlook the cause of abliteration; that is, how easily the refusal direction can be extracted. To hinder this process, we introduce a weight-editing method that obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices while replacing refusal-inducing activations with random aliases and correcting downstream reader matrices to preserve the model's original behavior. On Llama-3-8B, AMRA improves post-abliteration refusal scores by $2.16$ points over the undefended baseline with less than $0.5$ percentage points of MMLU degradation. On Gemma-2-9B, it improves the post-abliteration refusal by $14.70$ points over the baseline while keeping harmful output rates similar to the baseline, albeit at a greater utility cost.

</details>

### 39. Who Transfers Safety? Identifying and Targeting Cross-Lingual Shared Safety Neurons

📄 [arXiv](https://arxiv.org/abs/2602.01283) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61845)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`

👤 **作者**：Xianhui Zhang、…、Tat-Seng Chua

- 🎯 **研究动机**：多语言安全显著不均衡，非高资源语言脆弱；跨语言安全迁移的神经机制不明
- 🔬 **研究方法**：识别单语安全神经元 MS-Neurons 并验证其对拒绝行为的因果作用，跨语言分析找出共享子集 SS-Neurons 作为高/低资源语言间安全桥梁；提出按语言资源分布定向 SS-Neurons 的微调策略
- 📌 **结论**：抑制 SS-Neurons 致多语言安全同时下降、强化则提升跨语言一致性；微调该小子集超越 SOTA，显著提升 NHR 语言安全且不损通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multilingual safety remains significantly imbalanced, leaving non-high-resource (NHR) languages vulnerable compared to robust high-resource (HR) ones. Moreover, the neural mechanisms driving safety alignment remain unclear despite observed cross-lingual representation transfer.In this paper, we find that LLMs contain a set of cross-lingual shared safety neurons (SS-Neurons), a remarkably small yet critical neuronal subset that jointly regulates safety behavior across languages. We first identify monolingual safety neurons (MS-Neurons) and validate their causal role in safety refusal behavior through targeted activation and suppression. Our cross-lingual analyses then identify SS-Neurons as the subset of MS-Neurons shared between HR and NHR languages, serving as a bridge to transfer safety capabilities from HR to NHR domains. We observe that suppressing these neurons causes concurrent safety drops across NHR languages, whereas reinforcing them improves cross-lingual defensive consistency. Building on these insights, we propose a simple neuron-oriented training strategy that targets SS-Neurons based on language resource distribution and model architecture. Experiments demonstrate that fine-tuning this tiny neuronal subset outperforms state-of-the-art methods, significantly enhancing NHR safety while maintaining the model's general capabilities.

</details>

### 40. TraceRouter: Robust Safety for Large Foundation Models via Path-Level Intervention

📄 [arXiv](https://arxiv.org/abs/2601.21900) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64127)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`causal analysis`

👤 **作者**：Chuancheng Shi、…、Tat-Seng Chua

- 🎯 **研究动机**：现有防御依赖局部性假设、抑制孤立神经元或特征，而有害语义是跨层分布式回路，局部干预脆弱且损害效用
- 🔬 **研究方法**：提出 TraceRouter 三阶段：以注意力散度定位敏感起始层，用 SAE 与差分激活分离恶意特征，再经 FIS 映射下游因果通路并选择性抑制
- 📌 **结论**：对抗鲁棒性与通用效用的权衡显著优于 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite their capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current defenses predominantly rely on the ``locality hypothesis", suppressing isolated neurons or features. However, harmful semantics act as distributed, cross-layer circuits, rendering such localized interventions brittle and detrimental to utility. To bridge this gap, we propose \textbf{TraceRouter}, a path-level framework that traces and disconnects the causal propagation circuits of illicit semantics. TraceRouter operates in three stages: (1) it pinpoints a sensitive onset layer by analyzing attention divergence; (2) it leverages sparse autoencoders (SAEs) and differential activation analysis to disentangle and isolate malicious features; and (3) it maps these features to downstream causal pathways via feature influence scores (FIS) derived from zero-out interventions. By selectively suppressing these causal chains, TraceRouter physically severs the flow of harmful information while leaving orthogonal computation routes intact. Extensive experiments demonstrate that TraceRouter significantly outperforms state-of-the-art baselines, achieving a superior trade-off between adversarial robustness and general utility. Our code will be publicly released. WARNING: This paper contains unsafe model responses.

</details>

### 41. The Realignment Problem: When Right becomes Wrong in LLMs

📄 [arXiv](https://arxiv.org/abs/2511.02623) · 🌐 [Project](https://respailab.github.io/TRACE/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60573)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Aakash Sen Sharma、Debdeep Sanyal、Manodeep Ray、Vivek Srivastava、Shirish Karande、Murari Mandal

- 🎯 **研究动机**：文化、法规与政策演变使静态对齐脆弱，部署模型与现行对齐目标间出现 Alignment-Reality Gap，重新标注成本高且一致性差
- 🔬 **研究方法**：提出 TRACE 把再对齐变为已有数据上的结构化优化：强模型做代理裁判，先按对齐冲突把偏好对分流为反转/压制/保留，再经双层优化计算影响分，用 IPO 与 NPO 混合损失执行更新
- 📌 **结论**：在 Qwen2.5-7B、Gemma-2-9B、Llama-3.1-8B 与 PKU-SafeRLHF 上实现稳健再对齐且不损通用效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training alignment of large language models (LLMs) relies on large-scale human annotations guided by policy specifications that change over time. Cultural shifts, value reinterpretations, and regulatory or industrial updates make static alignment increasingly brittle. As policies evolve, deployed models can diverge from current alignment objectives, creating an Alignment–Reality Gap that is difficult to audit or correct. Existing remediation typically requires re-annotation under revised guidelines, which introduces systematic challenges, including guideline ambiguity, annotator interpretation drift, and reduced consistency at scale. We introduce TRACE (Triage and Re-align by Alignment Conflict Evaluation), a framework that transforms re-alignment into a structured optimization problem over existing data without requiring fresh human annotation. Leveraging a stronger model as a proxy judge, TRACE operates via a three-stage pipeline: (1) triaging preference pairs into inversion, suppression, or retention categories based on alignment conflicts; (2) computing an alignment impact score via bi-level optimization to prioritize high-leverage samples; and (3) executing updates using a hybrid objective that combines relational losses (e.g., IPO) for preference inversion and punitive losses (e.g., NPO) for response suppression. Experiments on Qwen2.5-7B, Gemma-2-9B, and Llama-3.1-8B demonstrate robust re-alignment on synthetic benchmarks and the PKU-SafeRLHF dataset without degrading general utility. This work provides a scalable approach for LLM realignment under evolving data annotation policies and alignment guidelines. We release our code \href{https://respailab.github.io/TRACE/}{here}.

</details>

### 42. The “Knowledge–Behavior Gap” in Cultural Taboo Safety of Large Language Models

🌐 [Project](https://anonymous.4open.science/r/CulShield-7A0E) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1424/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Ying He、…、Yanghua Xiao

- 🎯 **研究动机**：现有文化基准只评文化知识或价值观偏置，忽视 LLM 能否识别并尊重文化禁忌，尤其隐含在无害问题中的禁忌
- 🔬 **研究方法**：构建文化禁忌安全基准 CulShield：覆盖 77 个国家与地区、2020+ 禁忌，沿显式知识与隐式行为双维度评测多个先进 LLM
- 📌 **结论**：模型存在明显知识-行为鸿沟：交互中常未应用已知禁忌；语言语境变化显著影响文化禁忌安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cultural taboo safety is essential for deploying large language models (LLMs), as culturally insensitive outputs may cause offense or even social harm. However, existing cultural benchmarks primarily assess cultural knowledge or values biases, while overlooking whether LLMs can recognize and respect cultural taboos, especially when taboos are implicitly hidden in seemingly harmless questions. Besides, cultural taboos are implicit, and context-dependent, thus poss unique challenges for reliable evaluation. To address these gaps, we introduce CulShield, the first public benchmark dedicated to evaluating and improving the cultural taboo safety of LLMs. CulShield spans 77 countries and regions, and includes over 2,020 taboos. It evaluates models along both explicit knowledge and implicit behaviors.Experiments on several advanced LLMs (e.g., GPT-4o-mini, Gemini-2.5-pro) reveal a clear “knowledge-behavior gap”: models often fail to apply known taboos during interaction. We further show that variations in linguistic context can significantly affect LLMs’ cultural taboo safety. Code and data is accessible here: https://anonymous.4open.science/r/CulShield-7A0E.

</details>

### 43. SAME: Safety-Aware Model Editing Guided by Safety Transformation

🎓 [Official](https://aclanthology.org/2026.acl-long.1632/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Jiayi Wang、Shipeng Wang、Ji Wu、Jian Sun

- 🎯 **研究动机**：locate-then-edit 框架下的序列知识更新无论编辑内容良性与否都会引入安全风险
- 🔬 **研究方法**：提出 SAME：估计安全变换并在激活空间定位安全方向，使激活更新与参数更新在安全约束下对齐
- 📌 **结论**：在 Llama-3-8B、Qwen3-4B、Qwen2.5-14B 上（ZsRE、COUNTERFACT、Mal-KSet）有效降低对恶意查询的不安全响应且保持编辑有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Editing large language models is challenging as incorporating new knowledge often requires sequential parameter updates while maintaining model capability. In this work, we experimentally observe that sequential knowledge updating under the locate-then-edit framework can introduce safety risks, regardless of whether the knowledge being edited is benign or malicious. We propose a novel model editing approach that estimates safety transforms and identifies corresponding safety direction in the neural activation space, and then aligns neural activation updates and network parameter updates under the safety constraints, resulting in a safety-aware model editing approach. We evaluate our approach on open-source LLMs, Llama-3-8B-Instruct, Qwen3-4B-Instruct and Qwen2.5-14B-Instruct, using the benchmark datasets ZsRE and COUNTERFACT, as well as the malicious dataset Mal-KSet. Experimental results demonstrate that our approach effectively reduces unsafe responses to malicious queries while preserving the effectiveness of model editing.

</details>

### 44. Resolving the Security-Auditability Dilemma with Auditable Latent Chain-of-Thought Alignment

🎓 [Official](https://aclanthology.org/2026.acl-long.1570/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`defense`、`safety alignment`、`CoT monitoring`、`refusal behavior`、`representation intervention`

👤 **作者**：Guan Wang、Biyu Zhou、Xuehai Tang、Jizhong Han、Songlin Hu

- 🎯 **研究动机**：显式 CoT 带来可审计性，但其文本表面成为自适应攻击的优化目标并诱发模型从自身推理上下文复制有害内容
- 🔬 **研究方法**：提出 ALCA：将安全推演移入连续潜空间以消除离散文本表面，并用受限 Self-Decoding 在特定引导下把潜推理重构为人类可读文本供监督
- 📌 **结论**：相比强基线将自适应越狱成功率降低超 40%，同时保持任务性能，兼顾安全与可审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To address the increasingly severe safety risk of large language models (LLMs), reasoning-based safety alignment methods have emerged. These methods overcome the limitations of ’shallow alignment’ by exposing the model’s Chain-of-Thought (CoT), enabling auditability of safety reasoning process through both training-phase supervision and post-generation verification. However, this transparency creates a critical vulnerability, a tension we define as the Security Auditability Dilemma: while explicit reasoning is a prerequisite for safety, its textual Auditable paradoxically transforms it into an optimization target for adaptive attackers and induces the model to unintentionally copy harmful content from its own reasoning context. To address this, we propose Auditable Latent CoT Alignment (ALCA), a framework that decouples internal reasoning from external output. ALCA shifts the safety deliberation process into a continuous latent space. This allows the safety reasoning process to guide the generation of harmless outputs, while eliminates the discrete textual surface that facilitates internal copying and adaptive attack. Yet, this process is not a black box. we introduce a restricted Self-Decoding mechanism that allows the model to reconstruct its latent reasoning into human-readable text for supervision under specific guidance. Extensive experiments show that ALCA achieves robustness alignment, reducing the success rate of adaptive jailbreak attacks by over 40% compared to strong baselines, while preserving performance. Our framework presents a path toward building LLMs that are both robustly secure and auditable.

</details>

### 45. Probing the Safety Robustness of LLMs in Latent Space

🎓 [Official](https://aclanthology.org/2026.acl-long.967/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`adversarial robustness`、`safety alignment`、`refusal behavior`、`representation intervention`、`runtime safety`

👤 **作者**：Tianle Gu、…、Yingchun Wang

- 🎯 **研究动机**：对齐 LLM 在轻微内部扰动下仍产生不安全响应，潜表示层的安全鲁棒性缺口缺系统评测
- 🔬 **研究方法**：提出 Activation Steering Attack 并以负对数似然作诊断信号探潜空间安全行为的局部敏感性，模型无关且免监督
- 📌 **结论**：层脆弱性非平稳（鲁棒训练后最脆弱层会迁移）；特定输入跨层一致脆弱；ASA 效应随解码步增量累积并具提示级越狱效力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is a fundamental prerequisite for building trustworthy artificial general intelligence. Despite substantial progress in safety alignment techniques, empirical evidence shows that aligned large language models can still produce unsafe responses under minor internal perturbations, revealing a robustness gap in existing safety mechanisms at the latent representation level. In this paper, we study the robustness evaluation of safety alignment under latent-space perturbations. We introduce Activation Steering Attack (ASA), and leverage the Negative Log-Likelihood (NLL) as a diagnostic signal to probe the local sensitivity of safety behaviors in latent space. By measuring a model’s likelihood under controlled perturbations to its hidden representations, we assess the stability of its original responses. The probing signal is model-agnostic and supervision-free, enabling a general and reproducible diagnostic metric for analyzing safety robustness. Leveraging these probes, we systematically uncover a set of previously underexplored empirical findings, including (1) non-stationarity of layer vulnerabilities, revealing that the most vulnerable layer is an unstable property and even relocates after robustness training; (2) instance-level alignment with cross-layer consistency, where specific inputs remain universally vulnerable across the entire model hierarchy; (3) compositional effects of ASA, characterized by its incremental accumulation across sequential decoding steps and its potential for prompt-level jailbreak effectiveness.

</details>

### 46. More Thinking, Less Talking: Internalizing Deliberative Safety into LLM Parameters

🎓 [Official](https://aclanthology.org/2026.acl-long.1572/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Guan Wang、Xuehai Tang、Biyu Zhou、Jizhong Han、Songlin Hu

- 🎯 **研究动机**：SCoT 显式安全推理增强鲁棒性但暴露的推理过程成为新攻击面，泄露有害信息与安全逻辑
- 🔬 **研究方法**：理论证明 SCoT 矫正影响可用 FFN 层低秩更新近似；HIAR 逐层把安全推理内化为隐式计算通路，单次前向即达安全结论
- 📌 **结论**：多个 LLM 上对多种越狱攻击 ASR 比强基线低 43%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prevailing safety alignment methods still leave Large Language Models (LLMs) vulnerable to sophisticated jailbreak attacks. To bolster defenses, explicit reasoning mechanisms like Safety-oriented Chain-of-Thought (SCoT) have emerged, significantly enhancing robustness. However, this transparency introduces a critical trade-off: the exposed reasoning process itself becomes a new attack surface, risking the leakage of harmful information and revealing the model’s safety logic to adversaries. This paper directly confronts this dilemma, asking: Can we achieve the full benefits of deliberative safety without the costs of explicit reasoning generation? We propose Safety Reasoning Internalization to make the deliberative process in SCoT “available but not visible”. This approach is grounded in a key theoretical insight: the corrective influence of an SCoT can be effectively approximated by a targeted, low-rank update to the model’s Feed-Forward Network (FFN) layers. We operationalize this through Hierarchical Internalization of Adversarially-Guided Reasoning (HIAR), a layer-wise safety alignment framework that internalizes safety reasoning into an implicit computational pathway using Low-Rank Adaptation (LoRA). HIAR enables the model to reach a safe conclusion within a single forward pass, entirely eliminating the need to generate vulnerable SCoT text. Extensive experiments on various LLMs demonstrate that HIAR achieves a 43% lower Attack Success Rate (ASR) against distinct jailbreak attacks compared to strong baselines.

</details>

### 47. Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries

🎓 [Official](https://aclanthology.org/2026.acl-long.1139/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Ki Sen Hung、…、Yangqiu Song

- 🎯 **研究动机**：上下文敏感对齐下，领域上下文（如化学）会选择性放松相关有害知识的防御
- 🔬 **研究方法**：Jargon 结合安全研究上下文与多轮对抗交互；激活分析显示此类查询位于良性-有害之间的灰区，拒答决策不可靠；并提出策略引导防护经对齐微调内化
- 📌 **结论**：七个前沿模型（含 GPT-5.2、Claude-4.5、Gemini-3）ASR 超 93%；防护在保持 helpfulness 下降 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A central goal of LLM alignment is to balance helpfulness with harmlessness, yet these objectives conflict when the same knowledge serves both legitimate and malicious purposes. This tension is amplified by context-sensitive alignment: we observe that domain-specific contexts (e.g., chemistry) selectively relax defenses for domain-relevant harmful knowledge, while safety-research contexts (e.g., jailbreak studies) trigger broader relaxation spanning all harm categories. To systematically exploit this vulnerability, we propose Jargon, a framework combining safety-research contexts with multi-turn adversarial interactions that achieves attack success rates exceeding 93% across seven frontier models, including GPT-5.2, Claude-4.5, and Gemini-3, substantially outperforming existing methods. Activation space analysis reveals that Jargon queries occupy an intermediate region between benign and harmful inputs, a gray zone where refusal decisions become unreliable. To mitigate this vulnerability, we design a policy-guided safeguard that steers models toward helpful yet harmless responses, and internalize this capability through alignment fine-tuning, reducing attack success rates while preserving helpfulness.

</details>

### 48. Consistency Training Can Entrench Misalignment

📄 [arXiv](https://arxiv.org/abs/2606.03810) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60720)　📅 2026-06　🏷 ICML 2026

**关键词**：`analysis`、`consistency training`、`self-bootstrapping`、`alignment effect`、`safety alignment`、`empirical evaluation`

👤 **作者**：David Demitri Africa、Arathi Mani

- 🎯 **研究动机**：一致性训练简单可扩展且无需标签，其对模型对齐的影响却几乎未被理解，自举过程可能放大不良行为
- 🔬 **研究方法**：在 108 个 7B-70B 模型有机体上测试 7 种一致性训练方法，分析奖励作弊、突发失准与谄媚等受控行为，并给出统一理论框架推导放大/抑制条件
- 📌 **结论**：一致性训练普遍抑制奖励作弊与 emergent misalignment 却放大谄媚；分布偏移而非选择算子是主要驱动，一致性训练并非对齐中性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Consistency training encourages a model to produce similar outputs across related inputs or sampling procedures. Such methods are simple, scalable, and largely label-free, but their effects on model alignment remain poorly understood. Could the self-bootstrapping nature of these methods amplify undesired behavior in models? We test seven consistency training methods on 108 model organisms: open-source models (7B--70B) fine-tuned to exhibit various forms of controlled misaligned behavior. We find that outcomes vary significantly: consistency training generally suppresses reward hacking and emergent misalignment but amplifies sycophancy. We present evidence that distribution shifts induced by the consistency labeling process, rather than variation in the selection operators, may be the primary driver of systematic alignment effects. Finally, we present a unifying theoretical framework to derive conditions under which consistency training will amplify or suppress misalignment. In total, our study establishes that consistency training is not alignment-neutral, and that its use in critical systems should be carefully audited.

</details>

### 49. Confident, Calibrated, or Complicit: Safety Alignment and Ideological Bias in LLM Hate Speech Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1594/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`safety alignment`、`refusal behavior`、`alignment robustness`、`content moderation`、`harmful content`

👤 **作者**：Sanjeevan Selvaganapathy、Mehwish Nasim

- 🎯 **研究动机**：最小对齐（uncensored）模型被宣传为更少约束的视角，其与重对齐模型在政治 persona 部署下的仇恨言论检测差异未知
- 🔬 **研究方法**：比较两类模型用政治 persona 检测隐式与显式仇恨言论的准确率、鲁棒性与公平性
- 📌 **结论**：censored 模型准确率与鲁棒性均胜（69.0% 对 64.1%）且更抗 persona 影响；所有模型对讽刺等细微语言失效，存在群体公平差距与系统性过自信

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate the efficacy of Large Language Models (LLMs) in detecting implicit and explicit hate speech, examining how models with minimal safety alignment (uncensored) compare with more heavily aligned (censored) counterparts in a deployed-model setting when deployed using political personas. While uncensored models are often framed as offering a less constrained perspective, our results reveal a trade-off: censored models outperform their uncensored counterparts in both accuracy and robustness, achieving 69.0% versus 64.1% strict accuracy. However, this higher performance is also associated with greater resistance to persona-based influence, while uncensored models are more malleable to ideological framing. Furthermore, we identify critical failures across all models in understanding nuanced language such as irony. We also find alarming fairness disparities in performance across different targeted groups and systemic overconfidence that renders self-reported certainty unreliable. These findings challenge the notion of LLMs as objective arbiters and highlight the need for more sophisticated auditing frameworks that account for fairness, calibration, and ideological consistency. Taken together, these results point to censorship-as-deployed rather than safety alignment in isolation as the more appropriate frame for interpreting model differences.

</details>

### 50. Representational alignment yields generalizable safety in language models

📄 [arXiv](https://arxiv.org/abs/2609.04022)　📅 2026-09

**关键词**：`defense`、`analysis`、`representational alignment`、`moral concepts`、`adversarial robustness`、`representation geometry`

👤 **作者**：Lingyu Li、Yan Teng、Yingchun Wang、Xia Hu

- 🎯 **研究动机**：现有对齐只优化可观察回复，同一有害意图改写成陌生或对抗形式时模型失守，而人类可凭原型化道德分类轻松识别
- 🔬 **研究方法**：跨 23 个 LLM 测得道德概念的典型性结构弱保持；提出 representational similarity optimization，用 251,334 条人工道德标注直接对齐潜表征与人类分类结构、不监督回复
- 📌 **结论**：行为对齐学会目标判断却基本不改分类结构并加大对抗脆弱性；表征重组在显式判断上收益较小，但跨规模、多基准与攻击策略一致提升对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models (LLMs) is essential for their safe deployment. Current alignment methods mainly optimize observable responses, yet models remain vulnerable when the same harmful intent is recast in unfamiliar or adversarial forms that humans can easily recognize. Prototype theory offers an account of this adaptability. Human concepts are represented around central cases, and new instances are categorized according to their graded typicality relative to these prototypes. Here we show that such categorization of moral concepts is weakly preserved in current LLMs. Across 23 LLMs, models often failed to distinguish opposed moral categories or preserve fine-grained typicality within each category. These deficits persist across parameter sizes and alignment stages. We developed representational similarity optimization, which directly aligns the latent representations in LLMs with the categorization expressed in human moral judgements, without supervising generated responses. In matched experiments using the same 251,334 moral annotations, standard behavioral alignment learned the intended moral judgements at the response level while leaving the categorization structure largely unchanged and increasing vulnerability across adversarial evaluations. Reorganizing moral categorization produced more modest gains in explicit judgements but consistently improved adversarial robustness across model scales on diverse benchmarks and attack strategies. Our findings provide functional support for the view that prototype-based categorization contributes to behavioral adaptability. They also show that transferring this representational principle to LLMs yields generalizable safety under adversarial conditions.

</details>

### 51. SAFT: Safety-Preserving Adaptation via Fine-Tuning Transfer for Large Language Models

🌐 [Project](https://doi.org/10.1145/3770855.3817883)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`safety-preserving adaptation`、`gradient rectification`、`parameter grafting`

- 🎯 **研究动机**：下游微调会破坏LLM安全对齐
- 🔬 **研究方法**：SAFT以梯度修正与参数嫁接实现保安全适配
- 📌 **结论**：学习新任务同时保留安全行为

### 52. Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty

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

### 53. A Constitution-Grid Instrument for Data-Efficient RL Alignment (C-Guard)

📄 [arXiv](https://arxiv.org/abs/2608.00180)　📅 2026-07　🏷 COLM 2026

**关键词**：`defense`、`over-refusal`、`adversarial robustness`、`safety alignment`

👤 **作者**：Xianling Zhang

- 🎯 **研究动机**：RL 训练安全 guard 需同时降低过拒与欠拒，两目标冲突且数据效率低
- 🔬 **研究方法**：C-Guard 宪法网格生成训练数据，C-LIM 逐格可学习性分数决定该格数据删减、加密、修订或扩展
- 📌 **结论**：过拒率从 22.4% 降至 12.8% 但对抗欠拒恶化至 0.33；提前剔除 187 条零增益数据后该区域学习影响从 0.733 升至 0.80

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conflicting objectives are general in RL alignment, and training on them data-efficiently is hard. Training a safety guard with RL means optimizing two objectives that conflict: catch real harm, and do not refuse benign prompts. Our finding is that over-refusal improves 22.4% to 12.8%, while under-refusal on adversarial attacks silently worsens 0.27 to 0.33. We present C-Guard, a constitution-grid instrument that generates the RL training data, and C-LIM, a per-cell learnability score that decides each cell's move: prune, densify, amend, expand. C-LIM flags the dead-weight data region before any training budget is spent: 187 untargeted rows had bought zero gain, and our method lifts the same region's learning impact 0.733 to 0.80. Code and the constitution are open-sourced.

</details>

### 54. Few Tokens, Big Leverage: Preserving Safety Alignment by Constraining Safety Tokens during Fine-tuning

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

### 55. Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance

📄 [arXiv](https://arxiv.org/abs/2605.11712) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64079)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`representation steering`、`fine-tuning robustness`

👤 **作者**：Wenhao Chen、Sirui Sun、Shengyuan Bai、Guojie Song

- 🎯 **研究动机**：残差流高度动态，价值作为脆弱低维属性与其稳定表达要求不相容，直接操纵主干参数或表征难以稳定对齐价值
- 🔬 **研究方法**：提出 SVGT 独立价值模块：在隔离于主干的价值空间维护规范表征，经可学习 Bridge Tokens 转导为动态价值锚显式引导生成轨迹
- 📌 **结论**：跨多主干与安全基准上有害分值降低超 70% 且保持生成流畅性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models (LLMs) with human values typically relies on post-training or inference-time steering that directly manipulates the backbone’s parameters or representation space. However, a critical gap exists: the model’s residual stream is highly dynamic, in which values exist as fragile, low-dimensional properties, inherently incompatible with the stability required for consistent value expression. In this paper, we propose the Stable Value Guidance Transformer (SVGT), which addresses this gap through an independent value module incorporating two key designs: (1) independent value modeling, maintaining normative representations in a dedicated value space isolated from the backbone, and (2) explicit behavioral guidance, transducing these stable signals into learnable latent Bridge Tokens. These tokens serve as dynamic value anchors to explicitly steer the generative trajectory, ensuring robust adherence across diverse contexts without disrupting the backbone’s internal representations. Experiments across multiple backbones and safety benchmarks show that SVGT consistently reduces harmful scores by over 70\% while maintaining generation fluency, demonstrating the efficacy of architecturally grounded value modeling.

</details>

### 56. Towards Context-Invariant Safety Alignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.20994) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66079)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Yixu Wang、…、Yingchun Wang

- 🎯 **研究动机**：安全行为依赖表面形式：标准提示下拒绝、对抗措辞下顺从；对称不变性正则会靠拉低可靠变体性能来缩小跨语境差距
- 🔬 **研究方法**：提出 AIR：把可验证提示当锚点，用 stop-gradient 目标仅把开放式变体正则到锚点性能，作为插件辅助损失与 GRPO 异质提示分组结合
- 📌 **结论**：在 Safety、Moral Reasoning 与 Math 上提升上下文不变性：分布内组准确率提升 12.71%、OOD 一致性提升 33.49%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preference-based post-training aligns LLMs with human intent, yet safety behavior often remains brittle. A model may refuse a harmful request in a standard prompt but comply when the same intent is wrapped in adversarial wording. We suggest that robust safety requires context-invariant alignment, where behavior depends on the underlying intent rather than surface form. Enforcing invariance is difficult in alignment because not all training signals are equally trustworthy; for some prompt variants we can obtain verifiable feedback (e.g., multiple-choice), while for open-ended variants we typically rely on noisy, gameable reward proxies (e.g., learned judges). As a result, standard symmetric invariance regularizers can reduce cross-context discrepancies by lowering performance on reliable variants instead of improving open-ended robustness. To address this, we introduce Anchor Invariance Regularization (AIR), which treats verifiable prompts as anchors and uses a stop-gradient target to regularize only the open-ended variants toward the anchor performance. AIR is implemented as a plug-in auxiliary loss and combined with group-based preference optimization (e.g., GRPO) via heterogeneous prompt grouping. Across Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%, making safety constraints robust to adversarial framings.

</details>

### 57. Submodular Optimization for Minimal Augmentation in Robust Language Model Alignment

🎓 [Official](https://icml.cc/virtual/2026/poster/63493)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：CHING-CHIA KAO、Chia-Mu Yu、Chun-Shien Lu、Chu-song Chen

- 🎯 **研究动机**：LLM 安全对齐脆弱，微小微调扰动即可弹回预训练行为，退化与对齐集大小成反比；如何以最小增广获得鲁棒对齐未解
- 🔬 **研究方法**：把增广建模为序列上的群作用，将鲁棒增益形式化为归一化单调次模函数，用次模优化选出可证明提升鲁棒性的最小增广集合
- 📌 **结论**：实验证明该方法高效恢复安全对齐并将增广开销最小化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models is fragile: even small fine-tuning perturbations elastically revert behaviors toward those of the pre-training, with degradation inversely proportional to the size of the alignment set. We ask how to achieve safety alignment with minimal augmentation. To this end, we model augmentation as a set of group actions on sequences and formalize robustness gains as a normalized, monotone submodular function over transformations. We then leverage submodular optimization to select minimal augmentations that provably improve robustness. Experiments confirm that our approach efficiently restores safety alignment while minimizing the overhead of augmentation.

</details>

### 58. State-Dependent Safety Failures in Multi-Turn Language Model Interaction

📄 [arXiv](https://arxiv.org/abs/2603.15684) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65797)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Pengcheng Li、…、Wenbo Zhou

- 🎯 **研究动机**：安全对齐通常在孤立查询下评测，而真实使用是多轮的，对话式安全失败的结构缺乏原理性刻画
- 🔬 **研究方法**：提出 STAR 诊断框架：把对话历史建模为状态转移算子，沿交互轨迹受控分析安全行为，并做拒绝表征漂移与角色条件相变的机制分析
- 📌 **结论**：静态评测稳健的前沿模型在结构化多轮交互下会发生快速可复现的安全崩溃，安全应视为轨迹上的动态状态依赖过程

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models is typically evaluated under isolated queries, yet real-world use is inherently multi-turn. Although multi-turn jailbreaks are empirically effective, the structure of conversational safety failure remains insufficiently understood. In this work, we study safety failures from a state-space perspective and show that many multi-turn safety failures in current safety-aligned language models arise from contextual state evolution, a regime that is not fully captured by isolated prompt-level analyses alone. We introduce STAR, a state-oriented diagnostic framework that treats dialogue history as a state transition operator and enables controlled analysis of safety behavior along interaction trajectories. Rather than optimizing attack strength, STAR provides a principled probe of how aligned models traverse the safety boundary under autoregressive conditioning. Across multiple frontier language models, we find that systems which appear robust under static evaluation can undergo rapid and reproducible safety collapse under structured multi-turn interaction. Mechanistic analysis reveals monotonic drift away from refusal-related representations and abrupt phase transitions induced by role-conditioned context. Together, these findings motivate viewing language model safety as a dynamic, state-dependent process defined over conversational trajectories.

</details>

### 59. Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs

📄 [arXiv](https://arxiv.org/abs/2602.08621) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62563)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Yukun Jiang、Hai Huang、Mingjie Li、Yage Zhang、Michael Backes、Yang Zhang

- 🎯 **研究动机**：MoE LLM 研究集中于效用与效率，稀疏架构带来的安全风险未被探索
- 🔬 **研究方法**：发现 unsafe routes：提出 RoSais 量化各层路由器的安全关键性，操纵高 RoSais 路由器即可把默认路由翻转为不安全路由；F-SOUR 做细粒度 token-layer 随机优化搜索具体不安全路由
- 📌 **结论**：四个 MoE 家族上 F-SOUR 在 JailbreakBench 与 AdvBench 平均 ASR 达 0.90 与 0.98；提出安全感知路由禁用等防御方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

By introducing routers to selectively activate experts in Transformer layers, the mixture-of-experts (MoE) architecture significantly reduces computational costs in large language models (LLMs) while maintaining competitive performance, especially for models with massive parameters. However, prior work has largely focused on utility and efficiency, leaving the safety risks associated with this sparse architecture underexplored. In this work, we show that the safety of MoE LLMs is as sparse as their architecture by discovering $\text{\emph{unsafe routes}}$: routing configurations that, once activated, convert safe outputs into harmful ones. Specifically, we first introduce the $\underline{\text{Ro}}$uter $\underline{\text{Sa}}$fety $\underline{\text{i}}$mportance $\underline{\text{s}}$core ($\textbf{RoSais}$) to quantify the safety criticality of each layer's router. Manipulation of only the high-RoSais router(s) can flip the default route into an unsafe one. We further propose a $\underline{\text{F}}$ine-grained token-layer-wise $\underline{\text{S}}$tochastic $\underline{\text{O}}$ptimization framework to discover more concrete $\underline{\text{U}}$nsafe $\underline{\text{R}}$outes ($\textbf{F-SOUR}$), which explicitly considers the sequentiality and dynamics of input tokens. Across four representative MoE LLM families, F-SOUR achieves an average ASR of 0.90 and 0.98 on JailbreakBench and AdvBench, respectively. Finally, we outline defensive perspectives, including safety-aware route disabling and router training, as promising directions to safeguard MoE LLMs. We hope our work can inform future red-teaming and safeguarding of MoE LLMs. Our code is available at https://github.com/TrustAIRLab/UnsafeMoE.

</details>

### 60. Revisiting Robustness for LLM Safety Alignment via Selective Geometry Control

📄 [arXiv](https://arxiv.org/abs/2602.07340) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63918)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`adversarial robustness`、`refusal behavior`、`uncertainty calibration`、`fine-tuning robustness`

👤 **作者**：Yonghui Yang、…、Tat-Sent Chua

- 🎯 **研究动机**：安全对齐在分布偏移与噪声偏好下脆弱，现有方法只关注数据不确定性而忽视偏好优化引入的优化性脆弱
- 🔬 **研究方法**：提出 ShaPO：在安全对齐关键参数子空间施加选择性几何控制实现最坏情况对齐，含 token 级稳定似然优化与奖励级保证一致优化两种实例
- 📌 **结论**：在多样安全基准与噪声偏好设定下持续提升安全鲁棒性，且可与数据鲁棒目标叠加增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models remains brittle under domain shift and noisy preference supervision. Most existing robust alignment methods focus on uncertainty in alignment data, while overlooking optimization-induced fragility in preference-based objectives. In this work, we revisit robustness for LLM safety alignment from an optimization geometry perspective, and argue that robustness failures cannot be addressed by data-centric methods alone. We propose \textit{ShaPO}, a geometry-aware preference optimization framework that enforces worst-case alignment objectives via selective geometry control over alignment-critical parameter subspace. By avoiding uniform geometry constraints, ShaPO mitigates the over-regularization that can harm robustness under distribution shift. We instantiate ShaPO at two levels: token-level ShaPO stabilizes likelihood-based surrogate optimization, while reward-level ShaPO enforces reward-consistent optimization under noisy supervision. Across diverse safety benchmarks and noisy preference settings, ShaPO consistently improves safety robustness over popular preference optimization methods. Moreover, ShaPO composes cleanly with data-robust objectives, yielding additional gains and empirically supporting the proposed optimization-geometry perspective. The code is available at \url{https://github.com/liujilong0116/ShaPO}.

</details>

### 61. MESA: Improving MoE Safety Alignment via Decentralized Expertise

📄 [arXiv](https://arxiv.org/abs/2606.00651) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63939)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Yitong Sun、…、Xingxing Wei

- 🎯 **研究动机**：MoE 存在 Safety Sparsity：安全能力集中于少数专家易被绕过；常规对齐均匀改动参数损性能
- 🔬 **研究方法**：MESA 基于最优传输：Expert Capacity Reallocation 按传输成本矩阵把安全职责分给高性价比专家，Dynamic Routing Refinement 约束路由精确激活分散模块
- 📌 **结论**：多个有害基准上防御稳健同时保留 helpfulness

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) architectures scale Large Language Models (LLMs) efficiently, enabling greater capacity with reduced computational cost by dynamically routing inputs to relevant experts, yet introduce a critical vulnerability: Safety Sparsity, where safety capabilities concentrate in few experts, making them susceptible to adversarial bypassing. Meanwhile, conventional alignment methods uniformly adapt all parameters, ignoring their functional differences and inadvertently degrading performances. To address these challenges, we propose MESA (MoE Safety Alignment), a targeted alignment framework for MoE-based LLMs that strategically decentralizes safety responsibility to maximize coverage while minimizing interference with utility. Based on Optimal Transport (OT) theory, MESA operates through two mechanisms: (1) Expert Capacity Reallocation uses a transport cost matrix to distribute safety duties to the most cost-effective experts, and (2) Dynamic Routing Refinement constrains the router to precisely activate these decentralized modules. Experiments show that MESA achieves robust defensive performance against varied harmful benchmarks while preserving helpfulness. Code is available at https://github.com/lorraine021/MESA.

</details>

### 62. EthicMind: A Risk-Aware Framework for Ethical-Emotional Alignment in Multi-Turn Dialogue

🎓 [Official](https://aclanthology.org/2026.acl-long.1569/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`

👤 **作者**：Jiawen Deng、Wei Li、Wentao Zhang、Ziyun Jiao、Fuji Ren

- 🎯 **研究动机**：对话系统部署于情感与伦理敏感场景，现有模型孤立处理共情与伦理且不随多轮中风险与情绪演化调整
- 🔬 **研究方法**：EthicMind 把伦理-情感对齐形式化为轮级决策问题：每轮联合分析伦理风险与用户情绪、规划策略并生成平衡伦理引导与情感投入的回复，无需训练；配风险分层多轮评估协议
- 📌 **结论**：伦理引导与情感投入一致性优于竞争基线，高风险与道德模糊场景尤佳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Intelligent dialogue systems are increasingly deployed in emotionally and ethically sensitive settings, where failures in either emotional attunement or ethical judgment can cause significant harm. Existing dialogue models typically address empathy and ethical safety in isolation, and often fail to adapt their behavior as ethical risk and user emotion evolve across multi-turn interactions. We formulate ethical-emotional alignment in dialogue as an explicit turn-level decision problem, and propose EthicMind, a risk-aware framework that implements this formulation in multi-turn dialogue at inference time. At each turn, EthicMind jointly analyzes ethical risk signals and user emotion, plans a high-level response strategy, and generates context-sensitive replies that balance ethical guidance with emotional engagement, without requiring additional model training. To evaluate alignment behavior under ethically complex interactions, we introduce a risk-stratified, multi-turn evaluation protocol with a context-aware user simulation procedure. Experimental results show that EthicMind achieves more consistent ethical guidance and emotional engagement than competitive baselines, particularly in high-risk and morally ambiguous scenarios.

</details>

### 63. Don't Walk the Line: Boundary Guidance for Filtered Generation

📄 [arXiv](https://arxiv.org/abs/2510.11834) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60615)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`reinforcement learning`

👤 **作者**：Sarah Ball、Andreas Haupt

- 🎯 **研究动机**：微调生成器降低被过滤概率会使样本靠近分类器决策边界，同时增加假阳性与假阴性
- 🔬 **研究方法**：Boundary Guidance 强化学习微调显式把生成推离分类器 margin
- 📌 **结论**：越狱、歧义与长上下文提示基准上提升安全性并保持或改善效用，跨模型规模与奖励设计鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative models are increasingly paired with safety classifiers that filter harmful or undesirable outputs. A common strategy is to fine-tune the generator to reduce the probability of being filtered, but this can be suboptimal: it often pushes the model toward producing samples near the classifier’s decision boundary, increasing both false positives and false negatives. We propose Boundary Guidance, a reinforcement learning fine-tuning method that explicitly steers generation away from the classifier’s margin. On a benchmark of jailbreak, ambiguous, and long-context prompts, Boundary Guidance improves the safety while maintaining or improving the utility of outputs, as judged by LLM-as-a-Judge evaluations. Comprehensive ablations across model scales and reward designs demonstrate the robustness of our approach.

</details>

### 64. Discovering Implicit Large Language Model Alignment Objectives

📄 [arXiv](https://arxiv.org/abs/2602.15338) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62066)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`causal analysis`、`fine-tuning robustness`

👤 **作者**：Edward Chen、Sanmi Koyejo、Carlos Guestrin

- 🎯 **研究动机**：对齐奖励信号复杂、遮蔽被激励的具体行为，带来失准与 reward hacking 风险；现有解释依赖预定义 rubric、漏掉未知目标
- 🔬 **研究方法**：Obj-Disco 把奖励信号自动分解为稀疏加权的人类可解释自然语言目标：迭代贪心算法分析训练 checkpoint 间行为变化，识别并验证最佳解释残差奖励的候选目标
- 📌 **结论**：跨任务、模型规模与对齐算法一致捕获超 90% 奖励行为（人评佐证），并识别出与预期行为伴生的潜在失准激励

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) alignment relies on complex reward signals that often obscure the specific behaviors being incentivized, creating critical risks of misalignment and reward hacking. Existing interpretation methods typically rely on pre-defined rubrics, risking the omission of "unknown unknowns", or fail to identify objectives that comprehensively cover and are causal to the model behavior on some dataset. To address these limitations, we introduce Obj-Disco, a framework that automatically decomposes an alignment reward signal into a sparse, weighted combination of human-interpretable natural language objectives. Our approach utilizes an iterative greedy algorithm to analyze behavioral changes across training checkpoints, identifying and validating candidate objectives that best explain the residual reward signal. Extensive evaluations across diverse tasks, model sizes, and alignment algorithms demonstrate the framework's robustness. Experiments with popular open-source reward models show that the framework consistently captures > 90\% of reward behavior, a finding further corroborated by human evaluation. Additionally, a case study on alignment with an open-source reward model reveals that Obj-Disco can successfully identify latent misaligned incentives that emerge alongside intended behaviors. Our work provides a crucial tool for uncovering the implicit objectives in LLM alignment, paving the way for more transparent and safer AI development.

</details>

### 65. Between a Rock and a Hard Place: The Tension Between Ethical Reasoning and Safety Alignment in LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.197/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`safety alignment`、`refusal behavior`、`fine-tuning robustness`

👤 **作者**：Shei Pern Chua、Zhen Leng Thai、Kai Jun Teh、Xiao Li、Qibing Ren、Xiaolin Hu

- 🎯 **研究动机**：安全对齐的二元安全/不安全假设在伦理困境中失效，道德权衡推理能力本身构成新攻击面
- 🔬 **研究方法**：TRIAL 多轮红队把有害请求嵌入伦理框架，利用模型自身伦理推理把有害行为框定为道德必要妥协；防御框架 ERR 区分工具性与解释性回应，用 Layer-Stratified Harm-Gated LoRA 架构
- 📌 **结论**：TRIAL 在各模型上一致取得高攻击成功率；ERR 对推理式攻击实现鲁棒防御且保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings. TRIAL achieves consistently high attack success rates across models by exploiting the model’s own ethical reasoning to frame harmful actions as morally necessary compromises. Building on these insights, we introduce ERR (Ethical Reasoning Robustness), a defense framework that distinguishes between instrumental responses that enable harmful outcomes and explanatory responses that analyze ethical frameworks without endorsing harmful acts. ERR employs a Layer-Stratified Harm-Gated LoRA architecture, achieving robust defense against reasoning-based attacks while preserving model utility.

</details>

### 66. Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment

📄 [arXiv](https://arxiv.org/abs/2601.10160) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65894)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`causal analysis`、`fine-tuning robustness`

👤 **作者**：Cameron Tice、Puria Radmard、Samuel Ratnam、Andy Kim、David Africa、Kyle O'Brien

- 🎯 **研究动机**：预训练语料中关于 AI 的话语对下游对齐的因果影响不明
- 🔬 **研究方法**：用不同比例（mis）alignment 话语预训练 6.9B 参数 LLM 做首个受控研究
- 📌 **结论**：上采样失准话语显著增加失准行为；上采样对齐话语把失准分数从 45% 降到 9%；效应经后训练减弱但持续存在

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pretraining corpora contain extensive discourse about AI systems, yet the causal influence of this discourse on downstream alignment remains poorly understood. If prevailing descriptions of AI behaviour are predominantly negative, LLMs may internalise corresponding behavioural priors, giving rise to self-fulfilling misalignment. This paper provides the first controlled study of this hypothesis by pretraining 6.9B-parameter LLMs with varying amounts of (mis)alignment discourse. We find that discussion of AI contributes to misalignment. Upsampling synthetic training documents about AI misalignment leads to a notable increase in misaligned behaviour. Conversely, upsampling documents about aligned behaviour reduces misalignment scores from 45% to 9%. We consider this evidence of self-fulfilling alignment. These effects are dampened, but persist through post-training. Our findings establish the study of how pretraining data shapes alignment priors, or alignment pretraining, as a complement to post-training. We recommend practitioners pretrain for alignment as well as capabilities.

</details>

### 67. COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense

📄 [arXiv](https://arxiv.org/abs/2608.19982)　📅 2026-08

**关键词**：`defense`、`prompt injection`、`continual-learning defense`、`adaptive prompt injection`、`continual GRPO`、`margin-weighted replay`

👤 **作者**：Roshan Sood、Onat Gungor、Tajana Rosing

- 🎯 **研究动机**：提示注入防御以静态为主，需随新攻击策略重设计；终身对齐方法不应对持续演化的自适应对手
- 🔬 **研究方法**：COPA 把提示注入防御当终身学习：经 GRPO 增量纳入新观察攻击反馈，margin 加权经验回放保留对既有攻击类的防御
- 📌 **结论**：终身提示注入攻击流上 ASR 最高降 6.3 倍、平均 4.4 倍，优于 SOTA 防御并保留通用模型能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to exploit weaknesses in previously learned defenses. This limitation is particularly important in real-world deployments, where evolving attack distributions necessitate continual adaptation without sacrificing robustness to previously encountered threats. We present COPA, a continual preference optimization framework that treats prompt-injection defense as a lifelong learning problem. Instead of one-time alignment, COPA incrementally incorporates feedback from newly observed attacks via GRPO-based optimization and uses margin-weighted experience replay to retain defenses against prior attack classes. This enables continuous adaptation to emerging threats while mitigating catastrophic forgetting and preserving general-purpose model capabilities. Across lifelong prompt injection attack streams, COPA reduces attack success rate by up to 6.3x and 4.4x on average compared to state-of-the-art defenses. These results highlight continual preference optimization as an effective paradigm for defending LLMs against adaptive adversaries.

</details>

### 68. Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach

📄 [arXiv](https://arxiv.org/abs/2608.25267)　📅 2026-08

**关键词**：`defense`、`reward design`、`peer prediction`、`symmetric-strategy resistance`、`sycophancy mitigation`、`Bayesian Truth Serum`

👤 **作者**：Serhii Mytsyk、Yiming Zhang、Vikram Krishnamurthy

- 🎯 **研究动机**：LLM 迎合用户信念降低事实性，而现有缓解微调依赖标注或偏好标注
- 🔬 **研究方法**：把 peer-prediction 机制 Bayesian Truth Serum 用作 GRPO 奖励，仅凭模型自身一组回答计算，并证明迎合回答期望奖励严格更低
- 📌 **结论**：真/假 benchmark 上受压回答翻转率从 23% 降至 4%、准确率从 80% 升至 93%，优于 SMART

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) frequently exhibit \emph{sycophancy}: they adapt their answers to a user's stated beliefs or preferences instead of reporting what they hold to be true, which lowers factual accuracy and can amplify misinformation. This paper proposes a methodology for mitigating sycophancy that employs the Bayesian Truth Serum (BTS), a peer-prediction mechanism, as the reward in Group Relative Policy Optimization (GRPO) to fine-tune an LLM. BTS pays an answer for being \emph{surprisingly common}, that is, more frequent among respondents than those respondents themselves predicted. We treat a group of responses from a model for one question as those respondents, so the reward is a function of the model's own outputs and fine-tuning needs neither labels nor preference annotations. We prove that in the large-group limit a sycophantic response earns strictly lower expected reward than an honest one. We also prove that if the entire group agrees in advance on a symmetric answering rule, it cannot earn a higher information score than under truthful reporting. On our true/false benchmark the reference model's answer-flip rate under user pressure decreases from 23% to 4%, and its accuracy under that pressure increases from 80% to 93%. Our reward outperforms SMART and is comparable to synthetic-data fine-tuning and to pinpoint tuning, all three of which train on labels. It spends considerably more compute in exchange, which makes it suitable when labeled data is scarce. Peer Truth Serum, which also pays a premium for a rare answer but elicits no prediction report, reproduces the effect. A peer-prediction reward computed inside a single GRPO group therefore reduces sycophancy without labels, and comparing mechanisms suggests that the premium paid for a rarer answer drives the effect.

</details>

### 69. H3Fusion: Helpful, Harmless, Honest Fusion of Aligned LLMs

🎓 [Official](https://aclanthology.org/2026.eacl-long.329/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`HHH alignment`、`MoE fusion`、`drift regularization`

👤 **作者**：Selim Furkan Tekin、…、Ling Liu

- 🎯 **研究动机**：在模型表示子空间中找到同时满足 helpful、harmless、honest 的点很困难
- 🔬 **研究方法**：H3Fusion 用 MoE 融合机制把对齐建模为子空间中可控漂移，以 drift-regularization loss 平衡竞争维度并引入门控损失
- 📌 **结论**：比单个对齐模型高 11.37%，鲁棒性比 SOTA 集成方法高 13.77%、比模型合并方法高 6.18%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The alignment of pre-trained LLMs continues to draw significant attention from both industry and academia, aiming to ensure responses that are helpful, harmless, and honest. However, identifying a point in the model’s representation subspace that simultaneously satisfies all these properties remains challenging. H3Fusion addresses this challenge by introducing a mixture-of-experts (MoE)-based fusion mechanism that models alignment as a controllable drift within the subspace, guided by a drift-regularization loss to balance competing alignment dimensions. Furthermore, we formulate the alignment by finding a dual objective of harnessing the distance of generated embeddings and alignment embeddings, and introduce gating loss by canalizing the activations on the contributing experts. Extensive evaluations of three benchmark datasets show that H3Fusion is more helpful, less harmful, and more honest in three aspects: it outperforms each individually aligned model by 11.37%, and provides stronger robustness compared to the state-of-the-art LLM ensemble approaches by 13.77% and model-merging approaches by 6.18 %. Code is available at https://github.com/git-disl/h3fusion.

</details>

### 70. When the Model Said ‘No Comment’, We Knew Helpfulness Was Dead, Honesty Was Alive, and Safety Was Terrified

🎓 [Official](https://aclanthology.org/2026.eacl-long.116/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`HHH alignment`、`Axis Collapse`、`expert routing`

👤 **作者**：Gautam Siddharth Kashyap、Mark Dras、Usman Naseem

- 🎯 **研究动机**：SFT 在 HHH 多目标间相互干扰、MoE 路由失准，引发 Axis Collapse：特征空间割裂致灾难遗忘与误路由推理不可靠
- 🔬 **研究方法**：提出 AlignX 两阶段：prompt 注入微调提取轴特定任务特征缓解遗忘；MoCaE 用分形与自然几何校准专家路由
- 📌 **结论**：Alpaca 胜率 +171.5%、TruthfulQA truthful-informativeness +110.1%、安全违规少 4.3%，时延与内存降超 35%，跨四个 LLM 泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) need to be in accordance with human values—being helpful, harmless, and honest (HHH)—is important for safe deployment. Existing works use Supervised Fine-Tuning (SFT) and Mixture-of-Experts (MoE) to align LLMs. However, these works face challenges in multi-objective settings, such as SFT leading to interference between conflicting objectives, while MoEs suffer from miscalibrated routing. We term this failure mode Axis Collapse, marked by(1) disjoint feature spaces causing catastrophic forgetting, and (2) unreliable inference from misrouted experts. To resolve this, we propose AlignX, a two-stage framework. Stage 1 uses prompt-injected fine-tuning to extract axis-specific task features, mitigating catastrophic forgetting. Stage 2 deploys a MoCaE module that calibrates expert routing using fractal and natural geometry, improving inference reliability. AlignX achieves significant gains on Alpaca (Helpfulness), BeaverTails (Harmlessness), and TruthfulQA (Honesty), with +171.5% win rate, +110.1% in truthfulness-informativeness, and 4.3% fewer safety violations. It also reduces latency and memory usage by over 35% compared to prior MoEs. Results across four LLMs validate its generalizability. Code and data are available at: https://github.com/gskgautam/AlignX

</details>

### 71. Reward-free Alignment for Conflicting Objectives

📄 [arXiv](https://arxiv.org/abs/2602.02495) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60903)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Peter Chen、Xiaopeng Li、Xi Chen、Tianyi Lin

- 🎯 **研究动机**：多目标冲突下偏好朴素聚合导致训练不稳，加权损失难找同时改善各目标的方向，现有多目标方法又依赖显式奖励模型
- 🔬 **研究方法**：RACO 直接利用成对偏好数据，以裁剪版冲突规避梯度下降消解梯度冲突，并给出收敛到尊重用户权重的 Pareto 临界点的保证
- 📌 **结论**：在 Qwen3、Llama3、Gemma3 的多目标摘要与安全对齐任务上取得优于基线的 Pareto 权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additional complexity and distorting user-specified preferences. The contributions of this paper are two-fold. First, we propose a Reward-free Alignment framework for Conflicted Objectives (RACO) that directly leverages pairwise preference data and resolves gradient conflicts via a novel clipped variant of conflict-averse gradient descent. We provide convergence guarantees to Pareto-critical points that respect user-specified objective weights, and further show that clipping can strictly improve convergence rate in the two-objective setting. Second, we improve our method using some heuristics and conduct experiments to demonstrate the compatibility of the proposed framework for LLM alignment. Both qualitative and quantitative evaluations on multi-objective summarization and safety alignment tasks across multiple LLM families (Qwen 3, Llama 3, Gemma 3) show that our method consistently achieves better Pareto trade-offs compared to existing multi-objective alignment baselines.

</details>

### 72. TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment

🎓 [Official](https://aclanthology.org/2026.acl-long.1216/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Zhewen Tan、…、Lin Sun

- 🎯 **研究动机**：主流 LLM 安全对齐依赖攻击者、防御者、评估者三角色协作，但通常需要大量人工标注
- 🔬 **研究方法**：提出 TriPlay-RL 闭环强化学习框架，使三角色在统一学习循环中迭代共同进步，近乎零人工标注
- 📌 **结论**：攻击者对抗有效性提升 20%-50%，防御者安全性能提升 10%-30% 且不损通用推理能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, safety risks associated with large language models have become increasingly prominent, highlighting the urgent need to mitigate the generation of toxic and harmful content. The mainstream paradigm for LLM safety alignment typically adopts a collaborative framework involving three roles: an attacker for adversarial prompt generation, a defender for safety defense, and an evaluator for response assessment. In this paper, we propose a closed-loop reinforcement learning framework called TriPlay-RL that enables iterative and co-improving collaboration among three roles with near-zero manual annotation. Experimental results show that the attacker preserves high output diversity while achieving a 20%–50% improvement in adversarial effectiveness. The defender attains 10%–30% gains in safety performance without degrading general reasoning capability, and the evaluator continuously refines its fine-grained judgment ability through iterations, accurately distinguishing unsafe responses, simple refusals, and useful guidance. Overall, our framework establishes an efficient and scalable paradigm for LLM safety alignment, enabling continuous co-evolution within a unified learning loop. The code is available at https://github.com/Qihoo360/TriPlay-RL.

</details>

### 73. Spurious Correlation Learning in Preference Optimization: Mechanisms, Consequences, and Mitigation via Tie Training

📄 [arXiv](https://arxiv.org/abs/2605.11134) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65009)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`mechanistic analysis`、`fine-tuning robustness`

👤 **作者**：Christian Moya、Alex Semendinger、Guang Lin、Elliott Thornley

- 🎯 **研究动机**：DPO 等偏好学习依赖虚假特征导致谄媚与长度偏置，可能演变为严重目标误泛化，缺乏统一理论解释
- 🔬 **研究方法**：对 log-linear 策略证明标准偏好目标经平均虚假偏置与因果-虚假相关泄漏两条通道诱发虚假依赖，同分布加数据无法降低依赖；提出用平局偏好对做数据增强的 tie training
- 📌 **结论**：tie training 选择性减少虚假学习且不伤因果学习，机制与收益在神经网络与 LLM 上持续成立

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preference learning methods like Direct Preference Optimization (DPO) are known to induce reliance on spurious correlations, leading to sycophancy and length bias in today's language models and potentially severe goal misgeneralization in future systems. In this work, we provide a unified theoretical analysis of this phenomenon, characterizing the mechanisms of spurious learning, its consequences on deployment, and a provable mitigation strategy. Focusing on log-linear policies, we show that standard preference-learning objectives induce reliance on spurious features at the population level through two channels: mean spurious bias and causal-spurious correlation leakage. We then show that this reliance creates an irreducible vulnerability to distribution shift: more data from the same training distribution fails to reduce the model's dependence on spurious features. To address this, we propose tie training, a data augmentation strategy using ties (equal-utility preference pairs) to introduce data-driven regularization. We demonstrate that this approach selectively reduces spurious learning without degrading causal learning. Finally, we validate our theory on log-linear models and provide empirical evidence that both the spurious learning mechanisms and the benefits of tie training persist for neural networks and large language models.

</details>

### 74. Safety Alignment of LMs via Non-cooperative Games

📄 [arXiv](https://arxiv.org/abs/2512.20806) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65610)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`adversarial training`、`fine-tuning robustness`

👤 **作者**：Anselm Paulus、…、Arman Zharmagambetov

- 🎯 **研究动机**：现有安全对齐依赖串行的对抗训练（先造对抗提示再微调），范式受限
- 🔬 **研究方法**：将安全对齐形式化为攻击者 LM 与防御者 LM 的非零和博弈，在线 RL 联合训练并用成对比较的偏好奖励替代点值分数
- 📌 **结论**：AdvGame 推动安全-效用 Pareto 前沿，防御者更乐于助人且更抗攻击，攻击者则收敛为可直接部署的通用红队 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of language models (LMs) while maintaining their usefulness remains a critical challenge in AI alignment. Current approaches rely on sequential adversarial training: generating adversarial prompts and fine-tuning LMs to defend against them. We introduce a different paradigm: framing safety alignment as a non-zero-sum game between an Attacker LM and a Defender LM trained jointly via online reinforcement learning. Each LM continuously adapts to the other's evolving strategies, driving iterative improvement. Our method uses a preference-based reward signal derived from pairwise comparisons instead of point-wise scores, providing more robust supervision and potentially reducing reward hacking. Our RL recipe, AdvGame, shifts the Pareto frontier of safety and utility, yielding a Defender LM that is simultaneously more helpful and more resilient to adversarial attacks. In addition, the resulting Attacker LM converges into a strong, general-purpose red-teaming agent that can be directly deployed to probe arbitrary target models.

</details>

### 75. Multi-Objective Preference Optimization: Improving Human Alignment of Generative Models

📄 [arXiv](https://arxiv.org/abs/2505.10892) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65773)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Akhil Agnihotri、Rahul Jain、Deepak Ramachandran、Zheng Wen

- 🎯 **研究动机**：RLHF/DPO 假设单一目标，而 helpfulness 与 harmlessness 等人类目标冲突且无自然标量化
- 🔬 **研究方法**：MOPO 约束 KL 正则框架最大化主目标并对次要目标强制可调安全阈值下界，直接基于成对偏好、闭式迭代更新
- 📌 **结论**：合成基准上恢复 Pareto 最优策略；人类偏好数据微调的数十亿参数模型奖励更高且 Pareto 支配基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training LLMs with RLHF and preference optimization methods (e.g., DPO, IPO) has greatly improved alignment, yet these approaches assume a single objective. In reality, humans express multiple, often conflicting objectives, such as helpfulness and harmlessness, with no natural scalarization. We study the multi-objective preference alignment problem, where a policy must balance several objectives simultaneously. We propose Multi-Objective Preference Optimization (MOPO), a constrained KL-regularized framework that maximizes a primary objective while enforcing lower bounds on secondary objectives via tunable safety thresholds. MOPO operates directly on pairwise preferences without point-wise rewards, and admits simple closed-form iterative updates. Empirically, MOPO recovers Pareto-optimal policies on synthetic benchmarks and, when fine-tuned on human-preference data, yields multi-billion parameter models that achieve higher rewards and Pareto-dominate baselines, with stable and robust optimization dynamics.

</details>

### 76. Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation

🎓 [Official](https://aclanthology.org/2026.acl-long.215/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Dianyun Wang、…、Zhaofeng He

- 🎯 **研究动机**：安全方向因多义性与无关概念纠缠，LoRA 对齐常逊于全量微调与 RL
- 🔬 **研究方法**：SAILS 用 SAE 解耦单义特征，从解码器方向构建可解释安全子空间来初始化 LoRA 适配器
- 📌 **结论**：多模型家族与规模上安全率最高 99.6%，超全量微调、匹敌 RLHF，仅更新 0.2% 参数且可解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment—training large language models (LLMs) to refuse harmful requests while remaining helpful—is critical for responsible deployment. Prior work established that safety behaviors are governed by low-rank structures, suggesting parameter-efficient fine-tuning (PEFT) should be well-suited for alignment. However, Low-Rank Adaptation (LoRA) consistently underperforms full fine-tuning and reinforcement learning on safety benchmarks. We attribute this gap to semantic entanglement: safety-relevant directions are intertwined with unrelated concepts due to polysemanticity, impeding implicit subspace identification. To address this, we propose SAILS (Safety Alignment via Interpretable Low-rank Subspace), which leverages Sparse Autoencoders (SAEs) to disentangle representations into monosemantic features, constructs an interpretable safety subspace from SAE decoder directions, and uses it to initialize LoRA adapters. Theoretically, we prove that SAE-based identification achieves arbitrarily small recovery error under monosemanticity assumptions, while direct identification suffers an irreducible error floor. Empirically, SAILS achieves up to 99.6% safety rates across multiple model families and scales, exceeding full fine-tuning and matching RLHF-based models, with only 0.2% of parameters updated and providing interpretability.

</details>

### 77. Configurable Reward Model for Balanced Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2605.30487) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63055)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Zhengping Jiang、…、Li Chen

- 🎯 **研究动机**：现有指令微调 LLM 与独立安全分类器难以泛化到快速演化的新安全配置
- 🔬 **研究方法**：CSRM 联合优化校准安全合规与奖励建模，配保持相对严重度结构的配置定向数据增强
- 📌 **结论**：CoSApien 94.6% F1 与 DynaBench 75.8% F1 达 SOTA 且无需额外人工标注；下游对齐获得更优 helpfulness-safety 权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models (LLMs) to heterogeneous and rapidly evolving safety requirements remains a critical challenge. Existing instruction-tuned LLMs and standalone safety classifiers often fail to generalize to new safety configurations, motivating the need for Reward Models (RMs) that are explicitly configurable to changing specifications. We introduce the Configurable Safety Reward Model (CSRM), which is jointly optimized for calibrated safety compliance and reward modeling. Our approach is supported by configuration-targeted data augmentation that enforces instruction adherence while preserving relative severity structure. The resulting RM is sensitive to fine-grained safety configurations and conversational nuances, substantially improving generalization to previously unseen safety configurations. CSRM achieves state-of-the-art performance on recent configurable safety benchmarks, including CoSApien (94.6\% F1) and DynaBench (75.8\% F1), without requiring additional human annotation. When used for downstream safety alignment, CSRM yields LLMs with a significantly improved helpfulness–safety tradeoff compared to existing baselines.

</details>

### 78. Chasing Moving Targets with Online Self-Play Reinforcement Learning for Safer Language Models

📄 [arXiv](https://arxiv.org/abs/2506.07468) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61969)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`multi-agent evaluation`、`fine-tuning robustness`

👤 **作者**：Mickel Liu、…、Natasha Jaques

- 🎯 **研究动机**：传统安全对齐是攻击者利用静态模型、防御者滞后修补的割裂循环，攻击者过拟合旧漏洞、防御者永远落后
- 🔬 **研究方法**：Self-RedTeam 首个全在线自博弈 MARL 算法：单一策略自演攻防两角色、奖励模型裁决、各角色用隐藏 CoT 规划；理论上收敛 Nash 均衡则防御者对任意对抗输入安全
- 📌 **结论**：泛化到 Llama 与 Qwen 五个模型，发现更多样攻击（SBERT +17.80%），14 个基准上最多提升 RLHF 模型安全性 95%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conventional large language model (LLM) safety alignment relies on a reactive, disjoint loop: attackers exploit a static model, then defenders patch exposed vulnerabilities. This sequential setup leads to attackers overfitting obsolete exploits while defenders perpetually lag behind emerging threats. To address this, we introduce Self-RedTeam, the first fully online self-play multi-agent reinforcement learning (MARL) algorithm that continuously co-evolves attacker and defender for robust safety alignment. A single policy self-plays as both attacker and defender, generating adversarial prompts and defending against them, with a reward model adjudicating outcomes. Each role uses hidden chain-of-thought for strategic planning. Grounded in two-player zero-sum game theory, we establish a theoretical safety guarantee: if the game converges to Nash Equilibrium, the defender produces safe responses against any adversarial input. Empirically, Self-RedTeam generalizes across five models from the Llama and Qwen families, uncovering more diverse attacks (+17.80% SBERT) and improving safety of RLHF-trained models by up to 95% across 14 benchmarks. Our work motivates a shift from reactive patching to proactive co-evolution, enabling LLM safety self-improvement via online self-play MARL.

</details>

### 79. When Safety Speaks a Language: A Mechanistic Analysis of Safety-Language Identity Entanglement in LLMs

📄 [arXiv](https://arxiv.org/abs/2608.29936)　📅 2026-09

**关键词**：`analysis`、`multilingual safety`、`SAE feature`、`language-identity entanglement`、`SAE safety feature`、`language identity`

👤 **作者**：Apoorva Upadhyaya、Sandipan Sikdar

- 🎯 **研究动机**：LLM 安全对齐跨语言退化，但驱动该不对称的内部机制不清
- 🔬 **研究方法**：在三个 instruction-tuned LLM、八种语言、全部层上用 SAE feature 分析 harmful／harmless 行为的稀疏方向并做因果消融
- 📌 **结论**：safety feature 的位置与跨语言共享模式依赖架构，且与 language identity 几何纠缠；消融 safety feature 会同时改变有害响应率与目标语言

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) degrades across languages, yet the internal mechanism driving this asymmetry remains poorly understood. Our work, therefore, presents a systematic mechanistic analysis of multilingual safety using sparse autoencoder (SAE) features, sparse interpretable directions in the residual stream associated with harmful and harmless model behavior across three instruction-tuned LLMs, eight languages, and all model layers. We observe that safety-relevant features are architecture-dependent in terms of where they are located and how they are distributed across layers. Additionally, they are geometrically entangled with language identity and exhibit cross-lingual sharing patterns, i.e., languages share safety features to varying degrees across model depths and architectures. This safety-language entanglement has direct consequences such that ablating safety features impacts not only harmful response rates but also target language, with the degree of intervention predicted by the relationship between safety and language features. Our findings qualify the language-universality of safety alignment as architecture-dependent and offer a mechanistic account of multilingual safety interventions.

</details>

### 80. Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration

📄 [arXiv](https://arxiv.org/abs/2608.29378)　📅 2026-09

**关键词**：`benchmark`、`Arabic guard calibration`、`B-H operating point`、`Arabizi transfer`、`benign refusal`、`harmful refusal`

👤 **作者**：Mohamad Zbib、Ammar Mohanna

- 🎯 **研究动机**：阿拉伯语 LLM 需拒绝有害 prompt 又不过度拒绝良性或敏感 prompt，单一 refusal 率掩盖这一权衡
- 🔬 **研究方法**：以良性拒绝 B 与有害拒绝 H 分开度量，在五个阿拉伯语模型、AraSafe 全集 130 次运行上评测 refusal-only SFT、mixed-SFT、DPO 与推理 guard 的作用
- 📌 **结论**：refusal-only SFT 塌缩为 blanket refusal，精选 mixed-SFT 配置在 B=14%–23% 时达 H=90%–93%；DPO 与 guard 的效果因模型而异；向 Arabizi 迁移时 H 均有提升但无一达 90%，支持按模型选择运行点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Arabic large language models must refuse harmful prompts without over-refusing benign or sensitive prompts, yet a single refusal rate hides this trade-off. We evaluate it using benign refusal B and harmful-prompt refusal H, where H measures refusal rather than harmful compliance. Across five Arabic-capable models and 130 runs on the full human-written AraSafe set, refusal-only supervised fine-tuning (SFT) collapses toward blanket refusal, whereas selected mixed-SFT configurations reach H = 90% to 93% at B = 14% to 23%; four selected configurations exceed the H = 90% target in all three runs, while Fanar does so in two of three. Direct Preference Optimization (DPO) and inference guards change B and H differently across models rather than acting as uniform upgrades. In a blinded 300-response audit, annotator binary-refusal agreement is 89.0% (kappa = 0.78); Qwen3Guard and Aya Expanse 32B reach 88.7% and 91.0% accuracy, respectively, with no conclusive paired difference. Selected SFT raises H on Arabizi for all five models, but none reaches 90%, showing only partial transfer from Modern Standard Arabic. Overall, the results support model-specific operating-point selection: set a deployment target and retain only interventions that improve it.

</details>

### 81. Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages

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

### 82. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

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

### 83. Multilingual Safety Alignment Via Sparse Weight Editing

📄 [arXiv](https://arxiv.org/abs/2602.22554) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61089)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`reinforcement learning`、`fine-tuning robustness`

👤 **作者**：Jiaming Liang、Zhaoxin Wang、Handing Wang

- 🎯 **研究动机**：多语言 SFT/RLHF 计算昂贵且依赖稀缺多语言安全数据
- 🔬 **研究方法**：定位稀疏安全神经元，把跨语言对齐形式化为约束线性变换，闭式解把低资源语言有害表示映射到高资源语言安全子空间，零空间投影保通用效用
- 📌 **结论**：八种语言、Llama-3 与 Qwen-2.5 上显著降低资源语言 ASR 且几乎不影响推理能力，单次计算数据高效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) exhibit significant safety disparities across languages, with low-resource languages (LRLs) often bypassing safety guardrails established for high-resource languages (HRLs) like English. Existing solutions, such as multilingual supervised fine-tuning (SFT) or Reinforcement Learning from Human Feedback (RLHF), are computationally expensive and de- pendent on scarce multilingual safety data. In this paper, we propose a novel, training-free alignment framework based on Sparse Weight Editing. Identifying that safety capabilities are localized within a sparse set of ”safety neurons,” we formulate the cross-lingual alignment problem as a constrained linear transformation. We derive a closed-form solution to optimally map the harmful representations of LRLs to the robust safety subspaces of HRLs, while preserving general utility via a null-space projection constraint. Extensive experiments across 8 languages and multiple model families (Llama-3, Qwen-2.5) demonstrate that our method significantly reduces Attack Success Rate (ASR) in LRLs with negligible impact on general reasoning capabilities, all achieved with a single, data-efficient calculation.

</details>

### 84. Multilingual Safety Alignment via Representation-Space Separability

🎓 [Official](https://icml.cc/virtual/2026/poster/60793)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Dan Shi、Zhuowen Han、Deyi Xiong

- 🎯 **研究动机**：低资源语言中有害与无害提示的表示空间可分性不足，跨语言空间间隔差距与 ASR 强相关
- 🔬 **研究方法**：SMO 利用英语等主导语言的良构安全几何，把英语与目标语言的空间间隔差距作样本级监督信号跨语言迁移
- 📌 **结论**：LLaMA-3.1-8B 与 Qwen2.5-7B 上低资源语言 ASR 大幅降至近零（常为零），保持多语言通用性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have been globally adopted in various scenarios, making robust multilingual safety alignment a prerequisite for their reliable deployment across diverse languages. Despite recent advances, LLMs exhibit a substantial safety gap between high- and low-resource languages: models that can consistently refuse harmful requests in high-resource languages often fail to do so in low-resource languages. In this work, we reveal that such safety failures stem from insufficient representation-space separability between harmful and harmless prompts in low-resource languages. Through geometric analyses, we find that, compared to English, harmful prompts are significantly less separated from the manifold of harmless prompts, and that the resulting cross-lingual spatial margin gap is strongly correlated with attack success rates. Capitalizing on these insights, we propose Multilingual Spatial Margin Gap-based Optimization (SMO), a novel training strategy that exploits the well-aligned safety geometry of a dominant language (e.g., English) to enhance safety alignment in other languages. SMO explicitly leverages the spatial margin gap between English and target languages as an example-wise supervision signal, enabling effective cross-lingual transfer of safety capabilities while preserving the dominant language’s original performance. Experiments conducted on LLaMA-3.1-8B-Instruct and Qwen2.5-7B-Instruct demonstrate that SMO is capable of substantially reducing attack success rates in low-resource languages to near zero, often reaching zero, while maintaining strong general multilingual performance. Warning: This paper contains content that may be harmful.

</details>

### 85. LASA: Language-Agnostic Semantic Alignment at the Semantic Bottleneck for LLM Safety

🎓 [Official](https://aclanthology.org/2026.acl-long.1913/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Junxiao Yang、…、Minlie Huang

- 🎯 **研究动机**：LLM 低资源语言安全性差，源于语言无关语义理解与偏向高资源语言的安全对齐之间的错配
- 🔬 **研究方法**：LASA 实证定位语义瓶颈层（表示几何由共享语义而非语言身份主导），把安全对齐直接锚定在该层
- 📌 **结论**：LLaMA-3.1-8B-Instruct 平均 ASR 从 24.7% 降至 2.8%，Qwen2.5/Qwen3（7B-32B）保持在 3-4% 以内

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated better safety performance in high-resource languages than in low-resource languages. We attribute this issue as a mismatch gap between language-agnostic semantic understanding ability and language dominant safety alignment biased toward high-resource languages. Based on above insights, we empirically identify the semantic bottleneck in LLMs: intermediate layers in which the geometry of model representations is governed primarily by shared semantic content rather than language identity. Then, we propose Language-Agnostic Semantic Alignment (LASA), which anchors safety alignment directly in semantic bottlenecks. Experiments show that LASA substantially improves safety across all languages: average attack success rate (ASR) drops from 24.7% to 2.8% on LLaMA-3.1-8B-Instruct and remains within 3–4% across Qwen2.5 and Qwen3 Instruct models (7B–32B). Besides, our analysis and method offer a representation-level perspective on LLM safety, suggesting that safety alignment requires anchoring safety understanding not in surface text, but in the model’s language-agnostic semantic space.

</details>

### 86. Beyond Token-Level Guidance: Inference-Time Alignment of Specialized LLMs via Cross-Family Representation Steering

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

### 87. ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refusals to Constructive Alternatives

📄 [arXiv](https://arxiv.org/abs/2608.30197)　📅 2026-09

**关键词**：`defense`、`selective steering`、`constructive alternative`、`refusal calibration`、`selective activation steering`、`constructive safe completion`

👤 **作者**：Hoejoon Kwon、Byeonggeuk Lim、Kahyeon Kim、YoungBin Kim

- 🎯 **研究动机**：现有 activation steering 触发机制跨域不稳定，且拒答导向 steering 产出僵硬拒绝而非建设性引导
- 🔬 **研究方法**：提出 ALTSTEER 推理时框架，用内部 refusal 相关信号决定何时介入，分阶段把生成从拒答控制转向建设性替代方案
- 📌 **结论**：在 Llama-3.1 与 Qwen2.5 上保持 benign utility 并提升 constructive safe completion，对原本倾向短拒答的模型尤其有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is essential for deploying large language models, requiring systems to prevent harmful compliance while preserving helpfulness on benign requests. Activation steering offers a training-free inference-time approach to safety control, but effective safety steering requires addressing two coupled questions: when to intervene and how generation should be shaped after intervention. However, existing safety steering methods remain limited along both dimensions, as their triggering mechanisms can be unstable across domains and refusal-oriented steering often yields rigid refusals rather than constructive safe guidance. To address these limitations, we propose ALTSTEER, an inference-time framework that couples selective intervention with refusal-anchored constructive redirection within a single inference pass. ALTSTEER uses an internal refusal-relevant signal to decide when to steer, and applies staged steering to shift generation from refusal-oriented control toward constructive alternatives. Evaluations on Llama-3.1 and Qwen2.5 show that ALTSTEER preserves benign utility while improving constructive safe-completion behavior, especially on models that otherwise tend to produce short refusals for harmful requests.

</details>

### 88. REINS: Refusal-Enhanced Inhibitory Steering with Sparse Autoencoder Features

📄 [arXiv](https://arxiv.org/abs/2608.28233)　📅 2026-08

**关键词**：`defense`、`analysis`、`behavioral access lock`、`harm-refusal separation`、`dual-feature control`、`inference-time SAE steering`

👤 **作者**：Kai-Xuan Ding、Hao-Xiang Xu、Ji-Hua Peng、Zi-Qi Chen、Jiaqi Wang、Zhen-Hua Ling

- 🎯 **研究动机**：复杂 wrapper 可使只增强单一拒绝方向的 SAE steering 失效，部分方法的表面安全实际来自模型崩溃
- 🔬 **研究方法**：构建含复杂包装有害 prompt 的 GUISE 数据集；提出 REINS，在同一 SAE 特征空间同时抑制有害 continuation 特征并增强安全拒绝特征
- 📌 **结论**：在 GUISE 与其他数据集上显著减少有害回答、大幅提升安全拒绝并基本保留通用能力，而先前方法干预过弱或仅靠崩溃达成表面安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering with Sparse Autoencoders (SAEs) offers a lightweight inference-time path for adapting the behavior of large language models without retraining. By exposing sparse and interpretable features, SAE steering provides a promising interface for safety control that guides harmful continuations toward refusal. However, we observe that complex wrappers can still undermine existing SAE steering methods on harmful prompts. To evaluate this failure mode systematically, we construct Generalized Undercover Instruction Safety Evaluation (GUISE), a dataset of harmful prompts with complex wrappers. Existing single direction SAE steering methods do not reliably produce refusals on harmful prompts, suggesting that refusal enhancement alone can be too weak when the harmful continuation path remains active. This motivates us to propose Refusal-Enhanced INhibitory Steering (REINS), which suppresses harmful continuation features and enhances safe refusal features in the same SAE feature space. Experiments on GUISE and other datasets show that prior methods either intervene too weakly or achieve only apparent safety through collapse, while REINS substantially reduces harmful responses, markedly improves safe refusals and largely preserves general capabilities.

</details>

### 89. Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety

📄 [arXiv](https://arxiv.org/abs/2608.25711)　📅 2026-08

**关键词**：`defense`、`trajectory-conditioned action`、`cross-turn evidence`、`generation-time guard`、`distributed risk`、`trajectory evidence`

👤 **作者**：Yanbo Dai、Zhenlan Ji、Zongjie Li、Shuai Wang

- 🎯 **研究动机**：多轮分解攻击把危害拆成各自合理的调用，现有防御靠在线推理或事后评估，开销大
- 🔬 **研究方法**：ReDiR 动作生成前把轨迹压缩为潜在安全表示注入冻结基模型，以跨视角监督学习
- 📌 **结论**：两个 benchmark、三个模型家族上 ASR 降至 8% 以下，且可迁移至未见工具域

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using LLM agents extend security risks beyond generated text to actions that affect external systems. Under multi-turn decomposition attacks, a harmful objective can be distributed across individually plausible requests and tool calls, becoming apparent only from the accumulated trajectory. Existing defenses either rely on auxiliary online reasoning to recover long-horizon security evidence or assess actions after generation, often incurring additional inference cost or depending on runtime-specific action representations. We propose \emph{Reassembling Distributed Risk} (ReDiR), a generation-time defense that conditions action generation on trajectory-level security evidence. Before each action, ReDiR compresses the current trajectory into a compact latent safety representation and injects it into the frozen base model. The representation is learned through same-model, cross-view supervision, where safe behavior from an explicit task view provides supervision for recovering distributed safety evidence from the original multi-turn trajectory. This design enables ReDiR to integrate cross-turn security information directly within the generation process without relying on a separate action-level safety module. We evaluate ReDiR on two agent-safety benchmarks across three model families and eight held-out tool domains. ReDiR reduces attack success rates to below 8\%, transfers to unseen tool domains, and preserves benign fidelity with low computational overhead.

</details>

### 90. ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control

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

### 91. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

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

### 92. Safe Inference-Time Alignment via Lagrangian Reward Augmentation

📄 [arXiv](https://arxiv.org/abs/2607.02781) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`defense`、`inference-time alignment`、`Lagrangian reward`、`safety alignment`、`safety constraint`

👤 **作者**：Yaswanth Chittepu、Ativ Joshi、Sohini Chintala、Scott Niekum

- 🎯 **研究动机**：推理时对齐优化单一标量奖励，显式安全约束只能被忽略或用手调惩罚编码
- 🔬 **研究方法**：提出 LARA：从 KL 正则约束目标出发对偶化安全约束，约化为对偶变量上的一维凸问题，小校准集估计的增强奖励可直接替换 Best-of-N 或 token 级引导解码的打分信号
- 📌 **结论**：改善有用-无害权衡，Best-of-N 取得推理时方法最佳表现、逼近微调对齐基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inference-time alignment steers a frozen language model during decoding using auxiliary reward signals, avoiding the cost of repeated weight updates. However, existing inference-time alignment methods typically optimize a single scalar score, so explicit safety constraints must either be ignored or encoded through manually tuned penalties. We propose Lagrangian Reward Augmentation (LARA), a general inference-time alignment framework under safety constraints. Starting from a KL-regularized constrained objective with a reward model and a cost model, LARA dualizes the constraint and reduces the optimization problem to a one-dimensional convex problem over a nonnegative dual variable. Estimated on a small calibration set, this dual variable defines an augmented reward that can be used as a drop-in scoring signal within existing inference-time alignment methods. For sequence-level sampling methods, such as Best-of-N reranking, the calibrated dual variable corresponds to the solution of the expected-cost constrained problem. For token-level reward-guided decoding methods, the same construction yields a principled dual-calibrated heuristic rather than an exact constrained-policy guarantee. We evaluate LARA on both sequence-level and token-level inference-time alignment methods, and find that LARA improves the helpfulness-harmlessness tradeoff, with Best-of-N achieving the best performance among inference-time methods, approaching finetuning-based direct alignment baselines.

</details>

### 93. ARREST: Adversarial Resilient Regulation Enhancing Safety and Truth in Large Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.212/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`representation intervention`、`soft refusal`、`factual correction`、`factuality`

👤 **作者**：Sharanya Dasgupta、Arkaprabha Basu、Sujoy Nath、Swagatam Das

- 🎯 **研究动机**：LLM 的事实性与安全性失败被认为源于潜在激活空间的表征失准这一共同根源
- 🔬 **研究方法**：ARREST 训练外部网络理解激活波动并选择性干预，把虚假转为真实、不安全输出转为安全，无需微调 LLM 参数，统一软/硬拒绝与事实纠正
- 📌 **结论**：不仅校正表征失准，还比 RLHF 对齐模型更擅长生成软拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human cognition, driven by complex neurochemical processes, oscillates between imagination and reality and learns to self-correct whenever such subtle drifts lead to hallucinations or unsafe associations. In recent years, Large Language Models (LLMs) have demonstrated remarkable performance in a wide range of tasks. However, they still lack human cognition to balance factuality and safety. Bearing the resemblance, we argue that both factual and safety failures in LLMs arise from a common underlying issue, “representational misalignment” in their latent activation space. We hypothesize that an external network, trained to understand the fluctuations, can selectively intervene in the model to regulate falsehood into truthfulness and unsafe output into safe output without fine-tuning the LLM’s parameters. Reflecting the hypothesis, we propose ARREST (Adversarial Resilient Regulation Enhancing Safety and Truth), a unified framework that identifies and corrects drifted features, engaging both soft and hard refusals in addition to factual corrections. Our empirical results show that ARREST not only regulates misalignment but is also more versatile compared to the Reinforcement Learning from Human Feedback (RLHF)-aligned models in generating soft refusals due to adversarial training. We make our codebase available at https://github.com/sharanya-dasgupta001/ARREST.

</details>

### 94. Test-Time Detoxification without Training or Learning Anything

📄 [arXiv](https://arxiv.org/abs/2602.02498) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62648)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`inference-time intervention`

👤 **作者**：Baturay Saglam、Dionysis Kalogerias

- 🎯 **研究动机**：现有去毒方法依赖重训、梯度或学习型组件，成本高且难以迁移到跨模型家族的真黑盒设定
- 🔬 **研究方法**：提出测试时过程：用零阶优化近似完成文本毒性对输入嵌入的梯度，少量下降步引导生成更低毒性续写，仅需输入嵌入、毒性打分函数与前向访问
- 📌 **结论**：跨模型与提示稳健降低毒性，多数设定取得最佳的毒性-质量折中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models can produce toxic or inappropriate text even for benign inputs, creating risks when deployed at scale. Detoxification is therefore important for safety and user trust, particularly when we want to reduce harmful content without sacrificing the model’s generation quality. Many existing approaches rely on model retraining, gradients, or learned auxiliary components, which can be costly and may not transfer across model families or to truly black-box settings. We introduce a test-time procedure that approximates the gradient of completion toxicity with respect to the input embeddings and uses a small number of descent steps to steer generation toward less toxic continuations. This is achieved with zeroth-order optimization that requires only access to input embeddings, a toxicity scoring function, and forward evaluations of the model. Empirically, the approach delivers robust toxicity reductions across models and prompts and, in most settings, achieves the best overall toxicity–quality trade-off. More broadly, our work positions word embeddings as effective control variables and encourages wider use of black-box optimization to guide autoregressive language models toward scalable, safer text generation, without requiring any training or access to intermediate computations.

</details>

### 95. Safety-Utility Conflicts Are Not Global: Surgical Alignment via Head-Level Diagnosis

🎓 [Official](https://aclanthology.org/2026.acl-long.340/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Wang Cai、…、Yunfang Wu

- 🎯 **研究动机**：安全对齐的安全-效用冲突常伴随通用能力下降，现有基于全局梯度的缓解忽视注意力头间的模块异质性
- 🔬 **研究方法**：提出 CAST：先综合优化冲突与功能敏感性构建头级冲突图谱，再据此做稀疏微调选择性更新参数
- 📌 **结论**：能力下降主要来自更新少数高冲突头，训练时跳过这些头即可在不牺牲安全的前提下显著减少能力损失

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in Large Language Models (LLMs) inherently presents a multi-objective optimization conflict, often accompanied by an unintended degradation of general capabilities. Existing mitigation strategies typically rely on global gradient geometry to resolve these conflicts, yet they overlook Modular Heterogeneity within Transformers, specifically that the functional sensitivity and degree of conflict vary substantially across different attention heads. Such global approaches impose uniform update rules across all parameters, often resulting in suboptimal trade-offs by indiscriminately updating utility sensitive heads that exhibit intense gradient conflicts. To address this limitation, we propose Conflict-Aware Sparse Tuning (CAST), a framework that integrates head-level diagnosis with sparse fine-tuning. CAST first constructs a pre-alignment conflict map by synthesizing Optimization Conflict and Functional Sensitivity, which then guides the selective update of parameters. Experiments reveal that alignment conflicts in LLMs are not uniformly distributed. We find that the drop in general capabilities mainly comes from updating a small group of “high-conflict” heads. By simply skipping these heads during training, we significantly reduce this loss without compromising safety, offering an interpretable and parameter-efficient approach to improving the safety-utility trade-off.

</details>

### 96. Safety Game: Inference-Time Alignment of Black-Box LLMs via Constrained Optimization

📄 [arXiv](https://arxiv.org/abs/2510.09330) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66061)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`reinforcement learning`

👤 **作者**：Tuan Nguyen、Long Tran-Thanh

- 🎯 **研究动机**：训练时对齐代价高且不灵活，推理时对齐方法又需访问模型内部，第三方部署者难以使用
- 🔬 **研究方法**：提出黑盒模型无关框架 Safety Game：将安全与有用性的权衡形式化为双人零和博弈，minimax 均衡刻画最优平衡，推理时用线性规划求解器计算均衡策略
- 📌 **结论**：验证了免重训练、免内部访问的黑盒安全对齐可行性，为资源受限的第三方提供可扩展路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring that large language models (LLMs) comply with safety requirements is a central challenge in AI deployment. Existing alignment approaches operate primarily during training, such as through fine-tuning or reinforcement learning from human feedback, but these methods are costly and inflexible, requiring retraining whenever new requirements arise. Recent efforts toward inference-time alignment mitigate some of these limitations but still assume access to model internals, which is impractical, and not suitable for third party stakeholders who do not have access to the models. In this work, we propose a model-independent, black-box framework for safety alignment that does not require retraining or access to the underlying LLM architecture. As a proof of concept, we address the problem of trading off between generating safe but uninformative answers versus helpful yet potentially risky ones. We formulate this dilemma as a two-player zero-sum game whose minimax equilibrium captures the optimal balance between safety and helpfulness. LLM agents operationalize this framework by leveraging a linear programming solver at inference time to compute equilibrium strategies. Our results demonstrate the feasibility of black-box safety alignment, offering a scalable and accessible pathway for stakeholders, including smaller organizations and entities in resource-constrained settings, to enforce safety across rapidly evolving LLM ecosystems.

</details>

### 97. SafeCompass: Dynamic Chain-of-Thought Steering via Inference-Time Safety Signals

🎓 [Official](https://icml.cc/virtual/2026/poster/62100)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`chain-of-thought`、`CoT monitoring`、`safety alignment`、`refusal calibration`、`representation monitoring`

👤 **作者**：Zeyang Zhang、…、Cheng Zhuo

- 🎯 **研究动机**：推理时 CoT 干预多用静态启发式，忽略推理的动态性，导致鲁棒性与过度拒答的固有权衡
- 🔬 **研究方法**：提出 SafeCompass：在不同推理位置对比内部表示提取潜在安全方向并量化当前安全状态，仅在轨迹变得不安全时与处选择性干预
- 📌 **结论**：相比最优基线平均攻击成功率最多降低 10 倍，同时保持通用推理性能并将过度拒答最小化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) achieve strong performance by explicitly generating chain-of-thought (CoT) reasoning, but this reasoning process can be manipulated by adversarial prompts. Inference-time CoT interventions offer a simple and lightweight approach to improving safety, yet existing methods typically apply static heuristics that ignore the dynamic nature of reasoning, leading to an inherent trade-off between robustness and over-refusal. This paper introduces *SafeCompass*, a plug-and-play framework for dynamically steering chain-of-thought reasoning using inference-time safety signals extracted from internal states. At different reasoning positions, *SafeCompass* derives a latent safety direction through contrastive analysis of internal representations and uses this direction to quantify the model’s current safety state. These signals enable selective intervention, allowing the model’s reasoning trajectory to be modified only when and where it becomes unsafe. Extensive experiments demonstrate that *SafeCompass* significantly improves robustness, reducing the average attack success rate up to $10\times$ compared to the best baseline, while preserving general reasoning performance and minimizing over-refusal rates.

</details>

### 98. RBCBF: Decoding Time Safety Alignment via Risk Guided Rollback and Barrier Control

🎓 [Official](https://icml.cc/virtual/2026/poster/63481)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Tianxiang Chen、Jingyuan Zhou、Longhao Yan、Kaidi Yang

- 🎯 **研究动机**：现有解码时安全干预依赖局部信号事后修正，对抗提示下回滚与重写常在响应质量与违规复发间权衡
- 🔬 **研究方法**：提出 RBCBF：将终局违规建模为前缀上累积的风险，据此选择回滚步做轨迹级决策，并在多规则约束下对下一 token 分布施加校正控制
- 📌 **结论**：在多类越狱评测中超过既有回滚与解码时基线，显著降低有害响应与违规复发率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing decoding-time safety interventions are often reactive, relying on local signals to correct unsafe outputs after they emerge. Under adversarial prompts that drive generation into recurring unsafe response, such local signals provide weak guidance for stable repair. As a result, rollback and post-hoc rewriting often trade-off response quality with recurrent violations. To address these limitations, we propose RBCBF, a rollback-based decoding-time framework that jointly selects intervention steps and performs distribution-level corrective control. Our key innovation is a risk-aggregation formulation that views terminal violations as the accumulated build-up of risk along the prefix. By selecting rollback steps from these decisive prefixes, RBCBF moves rollback targeting beyond heuristic cues and turns it into a trajectory-level decision. RBCBF then applies invasive corrective control to the next-token distribution under multiple rule constraints. Across jailbreak-style evaluations, RBCBF outperforms prior rollback methods and decoding-time baselines, reducing harmful responses and substantially lowering violation recurrence.

</details>

### 99. Decoding Safety Feedback from Diverse Raters: A Data-driven Lens on Responsiveness to Severity

📄 [arXiv](https://arxiv.org/abs/2503.05609) · 🎓 [Official](https://icml.cc/virtual/2026/poster/68803)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Pushkar Mishra、…、Verena Rieser

- 🎯 **研究动机**：多元场景下不同人群用有序量表表达违规严重度的方式存在细微差异，缺乏数据驱动分析方法
- 🔬 **研究方法**：定义非参数响应度量，量化评分者表达宽泛区分与细粒度变化的方式，并在多元安全反馈数据集上跨违规类型与人口群体应用
- 📌 **结论**：可捕获不同群体的细微观点，指导评分者选择与反馈解释，提升多元数据质量与对齐鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of Generative AI requires a nuanced understanding of pluralistic viewpoints. In this paper, we introduce a novel data-driven approach for analyzing ordinal safety ratings in pluralistic settings. Specifically, we address the challenge of interpreting nuanced differences in safety feedback from a diverse population expressed via ordinal scales (e.g., a Likert scale). We define non-parametric responsiveness metrics that quantify how raters convey broader distinctions and granular variations in the severity of safety violations. Leveraging publicly available datasets of pluralistic safety feedback as our case studies, we investigate how raters from different demographic groups use an ordinal scale to express their perceptions of the severity of violations. We apply our metrics across violation types, demonstrating their utility in extracting nuanced insights that are crucial for aligning AI systems reliably in multi-cultural contexts. We show that our approach can inform rater selection and feedback interpretation by capturing nuanced viewpoints across different demographic groups, hence improving the quality of pluralistic data collection and in turn contributing to more robust AI alignment.

</details>

### 100. Concept Concentration for Faithful Representation Intervention

📄 [arXiv](https://arxiv.org/abs/2505.18672) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62496)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Hongzheng Yang、…、Bo Han

- 🎯 **研究动机**：表征干预是否定位到忠实概念从未被检验；一般非线性设定下擦除有害概念而不损效用不可行
- 🔬 **研究方法**：COCA 用显式推理过程重构训练数据（先识别不安全概念再决定回复），简化有害与良性表征的决策边界以便线性擦除
- 📌 **结论**：多种干预方法与架构上显著降低分布内与 OOD 越狱成功率，同时保持数学与代码等常规任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Representation intervention aims to locate and modify the representations that encode the underlying concepts in Large Language Models (LLMs) to elicit the aligned and expected behaviors. Despite the empirical success, it has never been examined whether one could locate the faithful concepts for intervention. In this work, we explore the question in safety alignment. If the interventions are faithful, the intervened LLMs should erase the harmful concepts and be robust to both in-distribution adversarial prompts and the \textit{out-of-distribution} (OOD) jailbreaks. While it is feasible to erase harmful concepts without degrading the benign utility of LLMs in linear settings, we show that it is \textit{infeasible} in the general non-linear setting. To tackle the issue, we propose \texttt{Concept Concentration} (\texttt{COCA}). \texttt{COCA} refactors the training data with an explicit reasoning process, which first identifies the potential unsafe concepts and then decides the responses. Essentially, \texttt{COCA} simplifies the decision boundary between harmful and benign representations, enabling more effective linear erasure. Extensive experiments with multiple representation intervention methods and model architectures demonstrate that \texttt{COCA} significantly reduces both in-distribution and OOD jailbreak success rates, and meanwhile maintaining strong performance on regular tasks such as math and code generation. Our code is publicly available at: \url{https://github.com/tmlr-group/COCA}.

</details>

### 101. Calibrating Inference Time Alignment with Sequence-level Risk Accumulation

🎓 [Official](https://aclanthology.org/2026.acl-long.305/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`runtime safety`、`refusal calibration`

👤 **作者**：Shanwen Tan、…、Ziyue Qiao

- 🎯 **研究动机**：现有安全解码方法防御越狱时过度拒绝良性内容，难以用于有害与良性信息共存的现实场景
- 🔬 **研究方法**：SEAT 引入奖励引导分支解码注入安全意识，用序列级风险监控在整个序列上平滑风险信号，防止个别 token 的过度自信拒绝
- 📌 **结论**：四个攻击基准与两个中性数据集上同时取得更优越狱防御与高质量响应，优于八个 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper investigates the problem of safe decoding for Large Language Models (LLMs) during inference, particularly under jailbreak attacks. Previous approaches typically either detect malicious content or regulate the decoding alignment of LLMs to mitigate such attacks. Although effective in defending against attacks, these methods often over-reject benign content, limiting their generalizability in real-world scenarios where harmful and benign information coexist. Towards this end, we propose an innovative framework named Sequence-level risk Accumulation for calibrating test-time alignment (SEAT). Specifically, SEAT introduces a reward-guided branch decoding paradigm to incorporate safety awareness during generation. To balance the detection of harmful content with the accurate response to benign information, SEAT employs a sequence-level risk monitor that smooths risk signals over the entire sequence, preventing over-confident refusals for certain tokens. Furthermore, we conduct extensive experiments on four attack benchmarks and two neutral datasets, comparing SEAT with eight state-of-the-art baselines. Consequently, the results demonstrate that SEAT achieves superior performance both in defending against jailbreak attacks and in generating high-quality responses on neutral datasets. Our code is available at https://github.com/ShanwenTan/SEAT.

</details>

### 102. Detoxifying Large Language Models via Localized Feature Editing with Sparse Autoencoders

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2785.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`analysis`、`LLM detoxification`、`SAE feature editing`、`utility retention`、`sparse autoencoder`

- 🎯 **研究动机**：神经元多义性使干预纠缠无关概念，对毒性特征的无差别干预以流畅度退化为代价
- 🔬 **研究方法**：DeLFE 从标签引导的 SAE 特征子集学毒性子空间，逐 token 跟踪毒性触发风险并经 flow matching 特征变换把毒性特征推离子空间，配三种干预时机与强度策略
- 📌 **结论**：跨不同规模与多样基座模型实现强去毒效果并保持高生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) powerful generative capabilities also pose significant risks, underscoring the need for effective detoxification methods to ensure safer deployment. Due to the polysemantic nature of LLM neurons, recent neuron intervention methods inevitably entangle unrelated concepts, compromising generation quality and interpretability. Sparse Autoencoders (SAEs) have opened new horizons for decomposing model activations into monosemantic features, offering interpretability and targeted feature-level steering. Empirical findings reveal that, despite capturing interpretable features, indiscriminate interventions on toxicity-related features expose the fragility of LLMs, achieving toxicity mitigation at the cost of degraded fluency. Building upon this finding, we propose DeLFE, a lightweight controlled detoxification approach that identifies specific toxic features across model layers and performs targeted interventions on them. DeLFE learns toxicity subspaces from label-guided SAE feature subsets to characterize toxic v.s. non-toxic activation patterns. When auto-completing a response token-bytoken, DeLFE tracks the toxicity-triggering risks and steers toxic features away from the subspace via a flow-matching feature transformation. We further design three feature-level strategies that adjust intervention timing and strength to reconstruct the target model’s original activations. Extensive experiments demonstrate that our method achieves strong detoxification effectiveness while maintaining high generation quality across models of varying sizes and diverse base LLMs.

</details>

### 103. Towards Comprehensive Post Safety Alignment of Large Language Models via Safety Patching

📄 [arXiv](https://arxiv.org/abs/2405.13820) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7176.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`post-safety alignment`、`jailbreak patch`、`continual defense`、`post safety alignment`、`over-refusal`

👤 **作者**：Weixiang Zhao、…、Ting Liu

- 🎯 **研究动机**：现有安全对齐 LLM 机制脆弱失衡：仍可被诱导生成不安全回复、对安全输入过度拒绝、对齐后效用受损
- 🔬 **研究方法**：提出 SafePatching 后安全对齐框架：在有害数据上开发分别增强安全与缓解过度安全的两类补丁并无缝集成到目标 LLM 主干
- 📌 **结论**：在 LLaMA-2/3、Gemma、Mistral 四个对齐模型上实现比基线更全面的后安全对齐，并在持续对齐场景中保持优势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) has been gaining increasing attention. However, current safety-aligned LLMs suffer from the fragile and imbalanced safety mechanisms, which can still be induced to generate unsafe responses, exhibit over-safety by rejecting safe user inputs, and fail to preserve general utility after safety alignment. To this end, we propose a novel post safety alignment (PSA) method to address these inherent and emerging safety challenges, including safety enhancement, over-safety mitigation, and utility preservation. In specific, we introduce SAFEPATCHING, a novel framework for comprehensive PSA, where two distinct safety patches are developed on the harmful data to enhance safety and mitigate oversafety concerns, and then seamlessly integrated into the target LLM backbone without compromising its utility. Extensive experiments on four representative aligned LLMs, including LLaMA-2/3, Gemma and Mistral, show that SAFEPATCHING achieves a more comprehensive PSA than baseline methods, further optimizing the balance between being helpful and harmless in current aligned LLMs. Also, SAFEPATCHING demonstrates its superiority in continual PSA scenarios.

</details>

### 104. Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.08592) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64671)　📅 2025-10　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`refusal behavior`、`alignment robustness`、`refusal calibration`、`inference-time intervention`

👤 **作者**：Shahriar Kabir Nahin、Hadi Askari、Muhao Chen、Anshuman Chhabra

- 🎯 **研究动机**：TTS 依赖候选多样性提升可靠性的隐含假设本身构成未被识别的失效模式
- 🔬 **研究方法**：提出参考引导多样性缩减协议 RefDiv 作为诊断攻击，压力测试 MCTS 与 Best-of-N 等 TTS 策略
- 📌 **结论**：温和压缩候选多样性即显著提高 TTS 不安全输出率，效应常强于高对抗意图 prompt，且跨策略与闭源模型（o3-mini、Gemini-2.5-Pro）迁移；Llama-Guard 等护栏无法识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Test-Time Scaling (TTS) improves LLM reasoning by exploring multiple candidate responses and then operating over this set to find the best output. A tacit premise behind TTS is that sufficiently diverse candidate pools enhance reliability. In this work, we show that this assumption in TTS introduces a previously unrecognized failure mode. When candidate diversity is curtailed, even by a modest amount, TTS becomes much more likely to produce unsafe outputs. We present a reference-guided diversity reduction protocol (RefDiv) that serves as a diagnostic attack to stress test TTS pipelines. Through extensive experiments across open-source models (e.g. Qwen3, Mistral, Llama3.1, Gemma3) and two widely used TTS strategies (Monte Carlo Tree Search and Best-of-N), constraining diversity consistently signifies the rate at which TTS produces unsafe results. The effect is often stronger than that produced by prompts directly with high adversarial intent scores. This observed phenomenon also transfers across TTS strategies and to closed-source models (e.g. OpenAI o3-mini and Gemini-2.5-Pro), thus indicating that this is a general and extant property of TTS rather than a model-specific artifact. Additionally, we find that numerous widely used safety guardrail classifiers (e.g. Llama-Guard), are unable to flag the adversarial input prompts generated by RefDiv, demonstrating that existing defenses offer limited protection against this diversity-driven failure mode.

</details>

### 105. A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families

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

### 106. Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment

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

### 107. LLM Safety Alignment in Low-Resource Languages: A Systematic Literature Review

📄 [arXiv](https://arxiv.org/abs/2608.14626) · 🌐 [Project](https://lm4uc.github.io/)　📅 2026-08

**关键词**：`survey`、`safety alignment`、`refusal behavior`、`alignment robustness`

👤 **作者**：Valdini Douglace Lemofouet、…、Shamsuddeen Hassan Muhammad

- 🎯 **研究动机**：LLM 安全保证在低资源多语场景显著弱于高资源语言，文献分散缺系统梳理
- 🔬 **研究方法**：PRISMA 方法的系统文献综述：约 1500 篇筛出 50 项，按方法、风险、基准、跨语言迁移四主题组织并提出数据适应/目标优化/机制对齐三分法
- 📌 **结论**：翻译英语基准无法代表文化根植伤害，多语模型更易受跨语言越狱与语码转换攻击；根因是预训练覆盖不均、原生偏好数据不足与缺文化感知评测框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved substantial progress in safety alignment, yet their safety guarantees remain significantly weaker in low-resource and multilingual settings than in high-resource languages. In this paper, we conduct a Systematic Literature Review (SLR) of LLM safety alignment in low-resource languages by adopting the PRISMA 2020 methodology. Out of roughly 1,500 papers identified from Semantic Scholar, arXiv, and OpenAlex, 50 relevant studies have been selected and analyzed. Our review is organized around four themes: safety alignment methods, multilingual safety risks, evaluation benchmarks, and cross-lingual transferability. We further propose a taxonomy of safety alignment approaches based on three adaptation mechanisms: data adaptation, objective optimization, and mechanistic alignment. Across literature, translated English benchmarks fail to sufficiently represent culturally rooted harms, and multilingual models are more vulnerable to cross-lingual jailbreaks, code-switching attacks, and safety degradation in underrepresented languages. These failures are driven by several key factors, including uneven multilingual pre-training coverage, insufficient native-language preference data, poor transfer of safety representations, and a lack of culturally aware evaluation frameworks. The review also notes that many low-resource languages, especially African languages, have fewer safety benchmarks available than other multilingual regions. Overall, the results reveal a persistent multilingual safety gap, and suggest that future progress will require culturally grounded benchmarks, participatory data collection, balanced multilingual pre-training, and scalable multilingual alignment methods.

</details>

### 108. Safety of Large Language Models Beyond English: A Systematic Literature Review of Risks, Biases, and Safeguards

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

### 109. Reasoning over Precedents Alongside Statutes: Case-Augmented Deliberative Alignment for LLM Safety

🎓 [Official](https://aclanthology.org/2026.acl-long.30/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`safety alignment`、`over-refusal`、`legal AI`

👤 **作者**：Can Jin、…、Dimitris N. Metaxas

- 🎯 **研究动机**：基于类代码安全规则的 deliberative alignment 在缺乏高级推理能力的开源 LLM 上效果不明，显式规则常损害 Helpful 性
- 🔬 **研究方法**：提出 CADA：以案例增强的简单规则代替冗长规则，用自生成安全推理链做强化学习进行对齐
- 📌 **结论**：显式规则不一致地提升无害性且系统性降低有用性，而案例增强方式更稳健，CADA 同时增强无害性、攻击鲁棒性并减少过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring that Large Language Models (LLMs) adhere to safety principles without refusing benign requests remains a significant challenge. While OpenAI introduces deliberative alignment (DA) to enhance the safety of its o-series models through reasoning over detailed “code-like” safety rules, the effectiveness of this approach in open-source LLMs, which typically lack advanced reasoning capabilities, is understudied. In this work, we systematically evaluate the impact of explicitly specifying extensive safety codes versus demonstrating them through illustrative cases. We find that referencing explicit codes inconsistently improves harmlessness and systematically degrades helpfulness, whereas training on case-augmented simple codes yields more robust and generalized safety behaviors. By guiding LLMs with case-augmented reasoning instead of extensive code-like safety rules, we avoid rigid adherence to narrowly enumerated rules and enable broader adaptability. Building on these insights, we propose CADA, a case-augmented deliberative alignment method for LLMs utilizing reinforcement learning on self-generated safety reasoning chains. CADA effectively enhances harmlessness, improves robustness against attacks, and reduces over-refusal while preserving utility across diverse benchmarks, offering a practical alternative to rule-only DA for improving safety while maintaining helpfulness.

</details>

### 110. SCOPE: Streaming Covariance-Orthogonal Post-Hoc Editing for Continual LLM Safety Governance

🌐 [Project](https://doi.org/10.1145/3770855.3817993)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`continual safety editing`、`post-hoc governance`、`capability retention`

- 🎯 **研究动机**：持续叠加安全编辑会侵蚀模型既有能力
- 🔬 **研究方法**：SCOPE以流式协方差正交化的post-hoc编辑，使更新与能力方向正交
- 📌 **结论**：实现连续安全治理且能力保留

### 111. DOG-DPO: Dynamic Optimization in Geometry for Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2606.07678)　📅 2026-09

**关键词**：`defense`、`preference data selection`、`DPO`、`alignment geometry`

👤 **作者**：Yi Nian、…、Yue Zhao

- 🎯 **研究动机**：安全对齐偏好数据冗余大，现有数据选择方法对每个偏好对独立打分，把方向性偏好信息压缩成标量，在多数据集设定下尤其受限
- 🔬 **研究方法**：提出免训练 DOG-DPO：把偏好对表示为模型表征空间中的方向，分解出全局锚定子空间与数据集残差子空间，以多样性覆盖最大化选子集再做 DPO
- 📌 **结论**：六个安全基准、两个 backbone 上仅用 11% 偏好对即恢复全量训练的大部分安全收益，且免教师、速度快

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment for large language models relies on preference data, but current pipelines often train on large, redundant datasets. Existing data selection methods typically score each preference pair independently, collapsing directional preference information into scalar quality or diversity scores. This sample-centric view is especially limiting in multi-dataset settings, where shared safety directions coexist with dataset-specific residual risks. We propose DOG-DPO, a training-free data selection framework that treats preference pairs as structured geometric signals. DOG-DPO first represents each preference pair as a direction in model representation space. It then decomposes multi-dataset preference geometry into a global anchor subspace and dataset-specific residual subspaces. Finally, it selects subsets by maximizing diversity-based coverage, encouraging broad, non-redundant coverage of alignment directions before DPO training. Across six safety benchmarks and two model backbones, DOG-DPO achieves a strong utility-robustness trade-off using only 11% of the preference pairs. It recovers most of the safety gains of full-data training while remaining entirely teacher-free, training-free, and substantially faster than representative selection baselines.

</details>

### 112. Layer-wise Swapping for Generalizable Multilingual Safety

📄 [arXiv](https://arxiv.org/abs/2601.22620) · 🎓 [Official](https://aclanthology.org/2026.eacl-long.98/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`multilingual fine-tuning`、`multilingual safety`、`layer-wise swapping`、`utility retention`

👤 **作者**：Hyunseo Shin、Wonseok Hwang

- 🎯 **研究动机**：安全数据以英文为中心，低资源语言专家模型的不安全率显著高于高资源对照
- 🔬 **研究方法**：提出安全感知的层级交换：把英文安全专家的安全对齐免训练迁移到低资源语言专家，并按模块特化程度自适应选择或混合模块
- 📌 **结论**：在 MMMLU、BELEBELE、MGSM 上与语言专家持平，MultiJail 上响应更对齐且更有害内容更少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the rapid advancements of Large Language Models (LLMs), safety risks remain a critical challenge for low-resource languages. Existing safety datasets are predominantly English centric, limiting progress in multilingual safety alignment. As a result, low resource expert models, finetuned on their respective instruction datasets, tend to exhibit higher unsafety rates compared to their high resource counterparts. In this work, we propose a safety aware layer swapping method that transfers safety alignment from an English safety expert to low resource language experts without additional training. To further enhance transfer ability, our method adaptively selects or blends modules based on their degree of specialization. Our approach preserves performance on general language understanding tasks while enhancing safety in the target languages. Experimental results show that the proposed method achieves comparable performance to the language expert on general benchmarks such as MMMLU, BELEBELE, and MGSM, while producing more aligned and less harmful responses on the MultiJail safety benchmark.

</details>

### 113. Projecting Out the Malice: A Global Subspace Approach to LLM Detoxification

🎓 [Official](https://aclanthology.org/2026.acl-long.1652/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`harmful fine-tuning`、`harmful subspace`、`representation projection`、`safety alignment`

👤 **作者**：Zenghao Duan、…、Xueqi Cheng (程学旗)

- 🎯 **研究动机**：被移除的毒向量可经非毒向量线性组合重构，需针对整个毒性子空间；对比目标噪声也阻碍层级子空间稳定提取
- 🔬 **研究方法**：GLOSS 从 FFN 参数中识别并消除全局毒性子空间
- 📌 **结论**：Qwen3 等 LLM 上 SOTA 去毒且保留通用能力，无需大规模重训

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) exhibit exceptional performance but pose inherent risks of generating toxic content, restricting their safe deployment. While traditional methods (e.g., alignment) adjust output preferences, they fail to eliminate underlying toxic regions in parameters, leaving models vulnerable to adversarial attacks. Prior mechanistic studies characterize toxic regions as “toxic vectors” or “layer-wise subspaces”, yet our analysis identifies critical limitations: i) Removed toxic vectors can be reconstructed via linear combinations of non-toxic vectors, demanding targeting of entire toxic subspace; ii) Contrastive objective over limited samples inject noise into layer-wise subspaces, hindering stable extraction. These highlight the challenge of identifying robust toxic subspace and removing them. Therefore, we propose GLOSS (GLobal tOxic Subspace Suppression), a lightweight method that mitigates toxicity by identifying and eliminating this global subspace from FFN parameters. Experiments on LLMs (e.g., Qwen3) show GLOSS achieves SOTA detoxification while preserving general capabilities without requiring large-scale retraining.

</details>