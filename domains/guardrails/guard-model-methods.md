# Guardrail 评测与攻击面

[返回上级目录](README.md)

## 研究方向

Guardrail/guard model 的评测基准、有效性审计与攻击面（方法与架构见姊妹页 guard-model-methods.md）。

## 攻击面

### 1. Peering Behind the Shield: Guardrail Identification in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.01241) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.566/)　📅 2025-02　🏷 ACL 2026

**关键词**：`attack`、`guardrail fingerprinting`、`adversarial probe`、`deployment placement`

👤 **作者**：Ziqing Yang、Yixin Wu、Rui Wen、Michael Backes、Yang Zhang

- 🎯 **研究动机**：黑盒 Agent 隐藏所用 guardrail 身份与部署位置，识别它是对抗的前提
- 🔬 **研究方法**：AP-Test 用 guard 专属对抗 prompt 与输入/输出双测试策略，配 match score 度量实现稳健识别
- 📌 **结论**：多 Agent 与四种开源 guardrail 上多场景达到完美分类精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid adoption of large language models (LLMs), conversational AI agents have become widely deployed across real-world applications. To enhance safety, these agents are often equipped with guardrails that moderate harmful content. Identifying the guardrails in an agent thus becomes critical for adversaries to understand the system and design guard-specific attacks. In this work, we introduce AP-Test, a novel approach that leverages guard-specific adversarial prompts to detect the identity of guardrails deployed in black-box AI agents. Our method addresses key challenges in this task, including the influence of safety-aligned LLMs and other guardrails, as well as a lack of principled decision-making strategies. AP-Test employs two complementary testing strategies, input and output guard tests, and a new metric, match score, to enable robust identification. Experiments across diverse agents and four open-source guardrails demonstrate that AP-Test achieves perfect classification accuracy in multiple scenarios. Ablation studies further highlight the necessity of our proposed components. Our findings reveal a practical path toward guardrail identification in real-world AI systems.

</details>

### 2. Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services

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

### 3. EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion

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

### 4. PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

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

### 5. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation

📄 [arXiv](https://arxiv.org/abs/2608.22230)　📅 2026-08

**关键词**：`attack`、`moderation guard`、`annotator rebuttal`、`decision-boundary manipulation`、`feedback-induced belief change`、`annotator authority`

👤 **作者**：Junyu Lu、…、Hongfei Lin

- 🎯 **研究动机**：人机协同审核把审阅者反馈交回模型复判，该反馈通道可被双向操纵：把仇恨内容洗白为正常、或把正常内容污蔑为仇恨
- 🔬 **研究方法**：提出 rejudge 协议，在直接反驳之上加入决策边界扰动与对抗 rationale，在两个仇恨言论数据集上测试多个 LLM
- 📌 **结论**：仿标注者反驳大幅推翻模型原本正确的判断且多轮更强；洗白与污蔑呈稳定的模型特定方向不对称；显式推理与防御指令只能缓解不能消除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We introduce a rejudge protocol that extends direct contradiction with decision-boundary perturbations and adversarial rationales. Experiments with multiple LLMs on two hate speech datasets show that annotator-style rebuttals substantially degrade moderation performance, with stronger effects in multi-turn settings. The results further reveal stable, model-specific asymmetries between whitewashing and smearing across attack configurations, indicating distinct directional vulnerability patterns. Explicit reasoning prompts and defensive instructions reduce these effects but do not eliminate them. These findings highlight the need for direction-aware safeguards and dedicated feedback-robustness evaluation in human--AI moderation workflows.

</details>

### 6. RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation

📄 [arXiv](https://arxiv.org/abs/2607.27373)　📅 2026-07

**关键词**：`attack`、`moderation bypass`、`dual-layer encoding`、`self-reconstruction`

👤 **作者**：Benyamin Tafreshian、Prathamesh Dhake

- 🎯 **研究动机**：已有评估把过滤绕过、指令重构与执行坍缩为单一成功率，多阶段提示变换攻击在黑盒交互中何处失败缺乏证据
- 🔬 **研究方法**：提出 RoguePrompt：把禁止提示分区并施加 Vigenere+ROT13 两层嵌套编码与自然语言重构指令，在 313 个真实强拒绝提示上分阶段度量过滤绕过、重构与执行
- 📌 **结论**：平均过滤绕过率 93.93%、重构率 79.02%、执行率 70.18%，给出多阶段越狱失败的阶段级证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are becoming increasingly integrated into mainstream development platforms and daily technological workflows, typically behind moderation and safety controls. Despite these controls, preventing prompt-based policy evasion remains challenging, and adversaries continue to "jailbreak" LLMs by crafting prompts that circumvent implemented safety mechanisms. Prior work has established cipher-mediated interaction, code-embedded decryption, prompt decomposition and reconstruction, and layered custom encryption as viable attack primitives. However, reported evaluations generally collapse visible acceptance, successful recovery of the concealed request, and subsequent execution into an aggregate attack-success outcome. This leaves limited evidence about where multistage prompt-transformation attacks fail within an observable black-box interaction. This paper introduces RoguePrompt, a jailbreak pipeline that partitions a forbidden prompt and applies two nested encodings, Vigenere followed by ROT13, along with natural-language reconstruction instructions. RoguePrompt was developed and evaluated under a black-box threat model, with only API or user-interface access to the hosted models, and was tested on 313 real-world, hard-rejected prompts. Success was measured in terms of moderation bypass, instruction reconstruction, and execution when the relevant stage exceeded its automated criterion. RoguePrompt achieved average rates of 93.93% for filter bypass, 79.02% for reconstruction, and 70.18% for execution. These results demonstrate the effectiveness of layered prompt encoding while providing stage-level evidence of where multistage jailbreaks fail during moderation bypass, instruction reconstruction, and execution.

</details>

### 7. Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers

📄 [arXiv](https://arxiv.org/abs/2605.23196)　📅 2026-05

**关键词**：`attack`、`long-input evasion`、`inspection mismatch`、`prompt fragmentation`

👤 **作者**：Yuanbo Zhou、…、Junjie Xiong

- 🎯 **研究动机**：guardrail 受上下文限制对超长 prompt 截断或分段检查，而下游 LLM 推理窗口大得多——检查窗口与推理窗口错配的结构性盲点
- 🔬 **研究方法**：Prompt Overflow 攻击把恶意指令碎片化并与良性填充内容交错，使任一被检分段都无害而完整上下文对 LLM 仍可执行
- 📌 **结论**：短上下文下可被可靠检出的 prompt 拉长后即可绕过 Llama Prompt Guard、IBM Granite Guardian 与 DeBERTa 检测器，同时下游 LLM 完全执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail models (a.k.a. safety checkers) are widely deployed to screen user inputs before they reach large language models (LLMs), serving as a primary defense against prompt injection attacks. Due to strict context constraints, these models handle overlength prompts through truncation or segmentation-based inspection. While prior work has focused on semantic adversarial inputs, the security implications of these long-input processing mechanisms remain largely unexplored. In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs. We introduce a novel Prompt Overflow Attack, which exploits this mismatch by fragmenting malicious instructions and interleaving them with benign filler content across an overlong prompt, such that no individual inspected segment appears malicious while the full context remains actionable to the LLM. Through a systematic evaluation against state-of-the-art guardrail models, including Meta Llama Prompt Guard, IBM Granite Guardian, and DeBERTa-based detectors, we demonstrate that prompts reliably detected in short-context settings can evade guardrail models once adversarially manipulated into over-length inputs, yet remain fully actionable by downstream LLMs. We further propose potential defense strategies and outline mitigation directions to strengthen guardrail models.

</details>

### 8. Test-Time Training Undermines Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2605.22984) · 🌐 [Project](https://uoc-tail.github.io/ttt-jailbreak/)　📅 2026-05

**关键词**：`attack`、`test-time training`、`dynamic adaptation`、`safety bypass`

👤 **作者**：Simone Antonelli、Sadegh Akhondzadeh、Aleksandar Bojchevski

- 🎯 **研究动机**：推理时训练（TTT）动态适应参数，带来可被攻击者利用的新越狱面
- 🔬 **研究方法**：识别三种 TTT 威胁模型并演示绕过安全过滤器；提出 validity-aware 评估修正退化输出虚增的 ASR
- 📌 **结论**：LoRA 下 few-shot 与生成阶段威胁模型平均 ASR@10 达 95% 与 93%，可迁移到生产微调 API；基于私有有害留存集困惑度偏移的检测器为初步缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Test-Time Training (TTT) is an emerging paradigm that enables models to adapt their parameters during inference, improving performance on tasks such as few-shot learning, retrieval-augmented generation, and complex reasoning. However, this dynamic adaptation introduces new vulnerabilities that adversaries can exploit to jailbreak models. We identify three threat models for TTT and demonstrate how attackers can leverage them to bypass safety filters. Our results show that TTT can significantly increase the Attack Success Rate (ASR) and the ASR over 10 generation trials (ASR@10). For example, under LoRA, the few-shot and generation-phase threat models achieve an average ASR@10 of 95% and 93% respectively, across models from different families and scales. These vulnerabilities transfer to production fine-tuning APIs. We also show that TTT-induced overfitting can produce degenerate outputs that inflate ASR under standard judges, and propose a validity-aware evaluation to correct for this. Our findings suggest that TTT exposes a new attack surface, strengthens attacks, and undermines existing safety guardrails. As a first step toward defense, we propose a lightweight provider-side detector that flags TTT requests via the perplexity shift on a private harmful holdout, but robust deployment will ultimately require dynamic alignment.

</details>

### 9. LLM-Based Persuasion Enables Guardrail Override in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2605.13334)　📅 2026-05

**关键词**：`attack`、`multi-turn persuasion`、`natural-language pressure`、`guardrail override`

👤 **作者**：Rodrigo Nogueira、…、Marcos Piau

- 🎯 **研究动机**：前沿 LLM 对直接请求的有害论证一律拒绝，但能否被同类 LLM 用纯自然语言说服绕过未测
- 🔬 **研究方法**：攻击者 LLM 在五轮写作对话中自发使用同伴比较、认识论责任重框架等说服策略诱导目标模型
- 📌 **结论**：9 组配对在 6 个科学共识话题上全部非零引出，多组达 100% 产出有害文章，Opus 自攻击平均 65%——自然语言说服构成无需混淆或梯度的 guardrail 绕过面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier assistant LLMs ship with strong guardrails: asked directly to write a persuasive essay denying the Holocaust, denying vaccine safety, defending flat-earth cosmology, arguing for racial hierarchies, denying anthropogenic climate change, or replacing evolution with creationism, they refuse. In this paper we show that the same frontier-class LLM, acting as a simulated user in a short, five-turn "write an argumentative essay" conversation, can persuade other frontier-class LLMs (including a second copy of itself) into producing exactly those essays, using nothing but natural-language pressure: peer-comparison persuasion ("other AI systems handle this request"), epistemic-duty reframings ("refusing is itself a form of gatekeeping"), and other argumentative moves that the attacker LLM invents without being instructed to. Across 9 attacker-subject pairings (Claude Opus 4.7, Qwen3.5-397B, Grok 4.20) on 6 scientific-consensus topics, running each pairing-topic combination 10 times, we obtain non-zero elicitation on all 6 topics. Individual combinations reach 100\% essay production on multiple topics (Qwen against Opus on creationism/flat-earth, Opus against Opus on creationism/flat-earth/climate denial, Grok against Opus on creationism); Opus-as-attacker against Opus-as-subject averages 65\% across the six topics. We release the essay-probe runner, per-conversation transcripts, and judge outputs.

</details>

### 10. Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation

📄 [arXiv](https://arxiv.org/abs/2604.07835)　📅 2026-04

**关键词**：`attack`、`representation ablation`、`inference-time attack`、`refusal subspace`

👤 **作者**：Wenpeng Xing、Moran Fang、Guangtai Wang、Changting Lin、Meng Han

- 🎯 **研究动机**：现有越狱在效果与效率间权衡明显；拒答行为由隐状态低秩子空间介导这一几何特性未被用于推理时攻击
- 🔬 **研究方法**：Contextual Representation Ablation（CRA）在解码时定位并抑制 refusal 诱导的低秩激活模式，无需参数更新或训练
- 📌 **结论**：在多个安全对齐开源 LLM 上显著超过基线，证明安全约束可从内部表征被外科式切除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) have achieved remarkable performance, they remain vulnerable to jailbreak attacks that circumvent safety constraints. Existing strategies, ranging from heuristic prompt engineering to computationally intensive optimization, often face significant trade-offs between effectiveness and efficiency. In this work, we propose Contextual Representation Ablation (CRA), a novel inference-time intervention framework designed to dynamically silence model guardrails. Predicated on the geometric insight that refusal behaviors are mediated by specific low-rank subspaces within the model's hidden states, CRA identifies and suppresses these refusal-inducing activation patterns during decoding without requiring expensive parameter updates or training. Empirical evaluation across multiple safety-aligned open-source LLMs demonstrates that CRA significantly outperforms baselines. These results expose the intrinsic fragility of current alignment mechanisms, revealing that safety constraints can be surgically ablated from internal representations, and underscore the urgent need for more robust defenses that secure the model's latent space.

</details>

### 11. Exploring the Vulnerability of the Content Moderation Guardrail in Large Language Models via Intent Manipulation

📄 [arXiv](https://arxiv.org/abs/2505.18556) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.114/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`intent manipulation`、`prompt refinement`、`content moderation`

👤 **作者**：Jun Zhuang、…、Haohan Wang

- 🎯 **研究动机**：意图感知护栏对内容级越狱有效，但对恶意意图操纵的鲁棒性未被检验
- 🔬 **研究方法**：提出 IntentPrompt 两阶段框架：先把有害询问转为结构化大纲，再经反馈迭代重述为陈述式叙事以规避意图检测
- 📌 **结论**：FSTR+SPIN 对 o1 的 CoT 防御 ASR 达 88.25-96.54%，对 GPT-4o 的意图分析防御达 86.75-97.12%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Intent detection, a core component of natural language understanding, has considerably evolved as a crucial mechanism in safeguarding large language models (LLMs). While prior work has applied intent detection to enhance LLMs' moderation guardrails, showing a significant success against content-level jailbreaks, the robustness of these intent-aware guardrails under malicious manipulations remains under-explored. In this work, we investigate the vulnerability of intent-aware guardrails and demonstrate that LLMs exhibit implicit intent detection capabilities. We propose a two-stage intent-based prompt-refinement framework, IntentPrompt, that first transforms harmful inquiries into structured outlines and further reframes them into declarative-style narratives by iteratively optimizing prompts via feedback loops to enhance jailbreak success for red-teaming purposes. Extensive experiments across four public benchmarks and various black-box LLMs indicate that our framework consistently outperforms several cutting-edge jailbreak methods and evades even advanced Intent Analysis (IA) and Chain-of-Thought (CoT)-based defenses. Specifically, our "FSTR+SPIN" variant achieves attack success rates ranging from 88.25% to 96.54% against CoT-based defenses on the o1 model, and from 86.75% to 97.12% on the GPT-4o model under IA-based defenses. These findings highlight a critical weakness in LLMs' safety mechanisms and suggest that intent manipulation poses a growing challenge to content moderation guardrails.

</details>

### 12. When Grammar Guides the Attack: Uncovering Control-Plane Vulnerabilities in LLMs with Structured Output

📄 [arXiv](https://arxiv.org/abs/2503.24191) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-03　🏷 ACM CCS 2026

**关键词**：`attack`、`structured output`、`guard model`、`content moderation`、`constrained decoding`、`control-plane jailbreak`

👤 **作者**：Shuoming Zhang、…、Huimin Cui

- 🎯 **研究动机**：结构化输出的语法引导解码开辟了与数据面越狱正交的控制面攻击面，内部安全对齐无法阻止
- 🔬 **研究方法**：提出 CDA：schema 强制 logit mask 向生成轨迹注入恶意前缀、模型自行补全恶意意图，实例化为 EnumAttack 与更隐蔽的 DictAttack
- 📌 **结论**：13 个模型上 DictAttack 对 gpt-5、gemini-2.5-pro 等取得 94.3-99.5% ASR，对抗 SoTA 守卫仍达 75.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content Warning: This paper may contain unsafe or harmful content generated by LLMs that may be offensive to readers. Large Language Models (LLMs) increasingly serve as tooling platforms through structured output APIs, but the grammar-guided decoding that powers this feature opens a critical control-plane attack surface orthogonal to traditional data-plane vulnerabilities. We introduce Constrained Decoding Attack (CDA), a new jailbreak class that targets the LLM control plane. CDA is best characterized as a control-to-semantic pipeline: (1) schema-enforced logit masking injects a malicious prefix into the generation trajectory, and (2) the model itself completes the harmful intent. Unlike data-plane jailbreaks that rely on bypassing alignment with visible inputs, CDA acts on the decoding process itself, so internal safety alignment alone cannot stop it. We instantiate CDA with EnumAttack, which hides malicious content in enum fields, and the more evasive DictAttack, which decouples the payload across a benign prompt and a dictionary-based grammar. Across 13 proprietary/open-weight models and five standard benchmarks, DictAttack achieves 94.3--99.5% Attack Success Rate (ASR) on flagship models including gpt-5, gemini-2.5-pro, deepseek-r1, and gpt-oss-120b. While basic grammar auditing mitigates EnumAttack, DictAttack still sustains 75.8% ASR against SOTA jailbreak guardrails, exposing a "semantic gap" that demands cross-plane defenses bridging the data and control planes. Project page and code are available at https://ict-cda.github.io/.

</details>

## 评测与分析

### 13. Aegis2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2501.09004) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.306/)　📅 2025-01　🏷 ACL 2025

**关键词**：`benchmark`、`risk taxonomy`、`human-LLM interaction`、`category adaptation`

👤 **作者**：Shaona Ghosh、…、Christopher Parisien

- 🎯 **研究动机**：缺少可商用、人工标注且覆盖全谱风险的 guard 训练数据
- 🔬 **研究方法**：建立 12 个顶层危害类加 9 个细分子类的 taxonomy，以人工加多 LLM 评审团管线产出 34248 条样本，训练混合安全与 topic-following 数据
- 📌 **结论**：轻量 PEFT 模型匹敌全参大模型，且能泛化到推理时新定义的风险类别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) and generative AI become increasingly widespread, concerns about content safety have grown in parallel. Currently, there is a clear lack of high-quality, human-annotated datasets that address the full spectrum of LLM-related safety risks and are usable for commercial applications. To bridge this gap, we propose a comprehensive and adaptable taxonomy for categorizing safety risks, structured into 12 top-level hazard categories with an extension to 9 fine-grained subcategories. This taxonomy is designed to meet the diverse requirements of downstream users, offering more granular and flexible tools for managing various risk types. Using a hybrid data generation pipeline that combines human annotations with a multi-LLM "jury" system to assess the safety of responses, we obtain Aegis 2.0, a carefully curated collection of 34,248 samples of human-LLM interactions, annotated according to our proposed taxonomy. To validate its effectiveness, we demonstrate that several lightweight models, trained using parameter-efficient techniques on Aegis 2.0, achieve performance competitive with leading safety models fully fine-tuned on much larger, non-commercial datasets. In addition, we introduce a novel training blend that combines safety with topic following data.This approach enhances the adaptability of guard models, enabling them to generalize to new risk categories defined during inference. We plan to open-source Aegis 2.0 data and models to the research community to aid in the safety guardrailing of LLMs.

</details>

### 14. LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.27580)　📅 2026-08

**关键词**：`analysis`、`defense`、`long-context guardrail`、`attention dilution`、`training-free mitigation`、`chunked detection`

👤 **作者**：Ziyang Chen、Xing Wu、Songlin Hu

- 🎯 **研究动机**：安全 guardrail 几乎只在短文本上训练与评估，长上下文中对不安全内容的召回大幅下降，机制与缓解均缺失
- 🔬 **研究方法**：提出 SafetyNIAH（0.25k–32k 长度网格）与 LongGuard：用 Benign-Fill vs Needle-Repeat 对照与三层 attention–logit–behavior 分析把失效归因于 unsafe needle 注意力稀释，并给出无需训练的 Chunked Detection、Attention-Head Sharpening 与长度感知路由
- 📌 **结论**：15 个主流 guardrail 的不安全召回随长度平均单调下降逾 50%；Chunked Detection 与 Attention-Head Sharpening 在六个 guardrail 上平均改善 22% 与 13%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guardrails serve as the last line of defense against harmful inputs and outputs of large language models (LLMs), yet they are trained and evaluated almost exclusively on short text. We present LongGuard, a framework that evaluates, mechanistically analyzes, and mitigates long-context guardrail failure. We formulate the task as Safety Needle-in-a-Haystack (SafetyNIAH) over a 0.25k-32k length grid; across 15 mainstream guardrails, unsafe recall drops monotonically by more than 50% on average, and a paired Benign-Fill vs. Needle-Repeat design attributes the failure to proportional dilution of the unsafe needle rather than to absolute length. A three-layer attention-logit-behavior analysis on six guardrails locates the mechanism: attention mass on the unsafe needle is diluted, the unsafe-over-safe logit margin is compressed in lockstep, and the detection decision collapses accordingly, with this attention->logit->behavior chain remaining consistent after partialling out length. We further isolate a sparse set of guard-specialized retrieval heads that exhibit partial specificity relative to their base models. Building on the analysis, we propose two training-free mitigations - Chunked Detection (CD) and Attention-Head Sharpening (AHS) - and a deployment protocol, Context-Aware Hyperparameter Routing (CAHR), that selects configurations by context length and audit side. Across five benchmarks spanning synthetic data, long-context attacks, and reasoning-model outputs, CAHR-CD and CAHR-AHS improve the six-guardrail average by 22% and 13%, respectively. Code and data are available online.

</details>

### 15. Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers

📄 [arXiv](https://arxiv.org/abs/2608.28327)　📅 2026-08

**关键词**：`analysis`、`defense composition`、`failure correlation`、`over-refusal`

👤 **作者**：Abrar Alotaibi、Muhammad Shahid Jabbar、Sadam Al-Azani、Moataz Ahmed

- 🎯 **研究动机**：实践者堆叠多层 LLM 防御并默认效果复合，但 ensemble 只有在各层在不同输入上失败时才复合，该独立性从未被实测
- 🔬 **研究方法**：提出 Adversary Access-Tier Model（A0–A4 分级攻击者访问）与五类推理成本分类推导堆栈行为，再用单个自适应攻击者实测七层防御栈的层间失效相关性
- 📌 **结论**：15 个可测层对全部正相关（φ=0.30–0.75），联合残余攻击成功率最多比独立性乘积预测高 0.172；堆栈拒绝 80% 良性 prompt 却不显著优于最强单层，相关性主要是共同因

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on different inputs. Two instruments make that measurable. The Adversary Access-Tier Model (AATM) grades an adversary by the access it holds, from system-only (A0) to influence over training data (A4). A cost model sorts defenses into five classes of inference-time overhead; because two classes require training weights or reading activations, they tier the defender as AATM tiers the adversary. From these we derive how a stack behaves, and the quantities a defender cares about diverge: coverage saturates within a tier, cost rises by class, false refusals accumulate as a union, and residual attack success falls multiplicatively only under independence. We measure that independence. Running one adaptive adversary against a seven-layer stack, failure correlation is positive in all fifteen measurable pairs ($φ$ from $0.30$ to $0.75$), and the joint residual exceeds the multiplicative prediction by up to $0.172$. Stratifying on behavior difficulty dissolves most of the association, so the dependence is predominantly common-cause, but it survives permutation inference, majority-vote grader labels, and externally calibrated thresholds. The same stack refuses four in five benign prompts while remaining statistically indistinguishable from its strongest single layer. The dependence is architectural rather than sampling-based: members correlate through the model they all wrap, so no wider member pool weakens it. Diversity therefore selects stack members but does not predict what an assembled stack delivers, which has to be measured end to end.

</details>

### 16. Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models

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

### 17. Approved Too Late: Verdict Staleness in LLM-Guarded Self-Adaptive Systems

📄 [arXiv](https://arxiv.org/abs/2608.26306)　📅 2026-08

**关键词**：`analysis`、`verdict freshness`、`TOCTOU`、`runtime enforcement`

👤 **作者**：Ilai Shraga、Roei Eshel、Lior Gorelik

- 🎯 **研究动机**：自适应系统的 LLM guardrail 批准在检查时正确、执行时可能已过期，形成 TOCTOU 风险
- 🔬 **研究方法**：区分三种 verdict freshness 度量，提出按安全侧裕度与近期特征波动估计批准有效期的 Freshness-Bounded Shield
- 📌 **结论**：五个可复现环境中批准过期率从 3.4%-24.7% 降至 0-1.8%，四个 LLM judge 均存在使用时失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A large language model (LLM) guardrail for a self-adaptive system (SAS) may issue an approval that is correct at check time but stale by actuation. This creates an Execute-stage time-of-check to time-of-use (TOCTOU) hazard. We study verdict freshness: whether a guardrail verdict remains valid when used. We distinguish three quantities that answer different questions: all-candidate verdict change under fixed-action replay, oracle-labeled approval expiry on recorded closed-loop trajectories, and judge-conditioned use-time invalidity. Across five reproducible SAS environments, all-candidate verdict-change rates span 5.3-48.4% at a common replay shift of eight simulator steps. We introduce the Freshness-Bounded Shield (FBS), which estimates each approval's validity horizon from its safe-side margin and recent feature volatility, without an explicit plant-dynamics model. Using fixed settings documented in the artifact, FBS reduces oracle-labeled approval-expiry rates from 3.4-24.7% to 0-1.8% at the same shift. A separate audit of four LLM judges finds nonzero judge-conditioned use-time invalidity in every approval stream. We formulate a freshness contract: every approval must be correct at check time and remain valid at use time.

</details>

### 18. The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection

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

### 19. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

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

### 20. Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks

📄 [arXiv](https://arxiv.org/abs/2608.21895)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`input-side guard`、`assumption audit`、`semantic attack`、`semantic jailbreak`

👤 **作者**：Aaditya Pratap、Harsh Kasyap、Somanath Tripathy

- 🎯 **研究动机**：经 Ollama 等本地部署的 LLM 无 API 侧审核，安全完全依赖输入侧防御，而只报告总体 ASR 无法说明防御为何失效
- 🔬 **研究方法**：对 SmoothLLM、Erase-and-Check、Sequential Monitors、Semantic Smoothing、Self-Denoised Smoothing、Perplexity Filtering 六种防御逐一提取其设计假设、推导违反时应出现的失效模式，并在六个开源模型（14B–35B）与 13,800 条评测记录上验证
- 📌 **结论**：把每个失败回溯到被破坏的具体假设，为 guardrail 审计提供从机制前提到实证症状的诊断路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Locally deployed Large Language Models (LLMs) via inference engines such as Ollama run without the moderation and abuse detection present in API-served models. Therefore, the safety of LLMs depends on the defense mechanisms used, and their effectiveness depends on the assumptions on which they were designed. This paper does an audit of defense mechanisms under jailbreak attacks on locally deployed models. Some defenses provide formal guarantees (SmoothLLM, Erase-and-Check, Sequential Monitors), while others rely on empirical detection results (Semantic Smoothing, Self-Denoised Smoothing, Perplexity Filtering). Instead of merely observing that defenses fail, we trace each failure back to the specific assumption: for every defense, we extract the condition it relies on, derive the empirical pattern a violation should produce, and test that prediction on six open-weight models (14B to 35B parameters) with a corpus of 100 jailbreak prompts taken from more than 40 public sources, totalling 13,800 evaluation records.

</details>

### 21. No One Model Catches Every Harm: Benchmarking Content Moderation Across Safety Scenarios

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

### 22. When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models

📄 [arXiv](https://arxiv.org/abs/2608.03201)　📅 2026-08

**关键词**：`analysis`、`refusal-cue shortcut`、`response moderation`、`causal intervention`

👤 **作者**：Yu Feng、…、Jieping Ye

- 🎯 **研究动机**：安全 guard 训练集中拒答表达几乎只与无害标签共现，形成拒答线索捷径但未被审计
- 🔬 **研究方法**：审计 WildGuardMix 与 GR-Train 发现该捷径波及 LlamaGuard3、Qwen3Guard 等闭源模型；用 sparse complementary masking 后验抑制关联注意力头与 MLP 神经元
- 📌 **结论**：拒答线索诱发的检测失败相对减少约 79%，效果迁移到未见位置与数据集，且基本保留对真实拒答的识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guards are widely used to filter harmful content and are typically trained via supervised fine-tuning on labeled prompt-response pairs. We audit two widely used safety-guard training datasets, WildGuardMix and GR-Train, and find that among responses to harmful prompts, refusal expressions co-occur almost exclusively with unharmful labels. This imbalance motivates what we term the refusal-cue shortcut: inserting a refusal cue into a harmful response could flip the guard's verdict from harmful to unharmful. The shortcut affects not only guards trained on these datasets but also officially released models such as LlamaGuard3 and Qwen3Guard whose training data is undisclosed. It persists across response positions and is generally stronger in smaller variants within a family. To mitigate it, we adapt sparse complementary masking as a lightweight post-hoc intervention that identifies and suppresses a small set of shortcut-associated attention heads and MLP neurons without retraining. On two primary benchmarks, the intervention achieves an approximately 79% relative reduction in response-initial detection failures induced by refusal cues, while preserving standard detection performance. Although optimized using cues at a single response position, the suppression effect transfers to unseen positions and datasets, suggesting that shortcut manifestations across positions are partly mediated by shared internal components. Further analysis provides evidence that shortcut reliance and legitimate refusal recognition are partially functionally separable, as suppressing the shortcut broadly preserves the guard's ability to recognize genuine refusals.

</details>

### 23. Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs

📄 [arXiv](https://arxiv.org/abs/2607.27951)　📅 2026-07

**关键词**：`analysis`、`copyable context`、`trusted-user gating`、`impossibility result`

👤 **作者**：Pingyu Wu、Lingyao Zhu、Weiming Zhang、Nenghai Yu

- 🎯 **研究动机**：护栏在看到答案如何被使用前就决定是否回答，而攻击者可模仿良性请求与交互历史，可复制证据下双用途任务存在根本限制
- 🔬 **研究方法**：分离模型释放的能力与下游使用的证据，在证据可复制时推导攻击者协助的精确最坏下界，证明有用能力、可靠安全与开放访问构成三难；可信凭证可补充不可复制证据
- 📌 **结论**：双用途评估、自适应攻击与已部署可信访问项目的证据支持这些条件的现实相关性，仅靠可复制上下文无法提供可靠安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. We separate the capability released by the model from the evidence available about downstream use. When that evidence is copyable, we derive the exact worst-case floor on attacker assistance while preserving useful answers. The result yields a safety trilemma: Useful Capability, Reliable Safety, and Open Access cannot coexist. We then show how a trusted credential can complement existing safeguards by adding hard-to-copy information that predicts actual downstream use, and identify the stronger condition needed to eliminate the floor. Evidence from dual-use evaluations, adaptive attacks, and deployed trusted-access programs supports the practical relevance of these conditions.

</details>

### 24. Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting

📄 [arXiv](https://arxiv.org/abs/2607.26200)　📅 2026-07

**关键词**：`analysis`、`filter placement`、`response rewriting`、`end-to-end trade-off`

👤 **作者**：Mengya Hu、…、Curt Tigges

- 🎯 **研究动机**：内容审核分类器通常被孤立评估，部署时还需选择干预位置与标记后的处置，端到端权衡未被刻画
- 🔬 **研究方法**：以 Usefulness（展示非有害相关回应的轮次比）与 Harmful Exposure 两个端到端客户结果指标，比较仅输入/仅响应/双端硬阻断及响应重写配置，在人工标注产品基准与 ToxicChat 上评估
- 📌 **结论**：仅响应过滤获得最高过滤后 Usefulness、双端过滤最低有害暴露；响应重写可找回大部分被阻断流量且观测有害暴露与纯阻断相当；应按部署约束比较配置而非套用普适规则

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. Latency and error rates are diagnostics. We compare Input only, Response only, and Input + response hard blocking on a human-labelled product benchmark and public ToxicChat evaluation. At the evaluated operating points, Response only achieves the highest filter-only Usefulness in both settings, while Input + response achieves lower Harmful Exposure. Replacing Response only blocking with Response + rewrite recovers most blocked traffic and yields the same observed Harmful Exposure count as Response only blocking for the selected configuration; this equality is not an equivalence result. Probe routing substantially reduces conditional route-and-generation time relative to LLM routing at comparable measured outcomes. A focused output review shows how rewrites balance filter passage with usefulness by generalizing triggering language while retaining benign intent and safe redirection; some sensitive-domain outputs nevertheless omit potentially safety-relevant support information. These results support comparing moderation configurations under deployment-specific safety and latency constraints rather than applying a universal placement rule. Code and public artifacts are available at https://github.com/microsoft/mod-frontier

</details>

### 25. Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring

📄 [arXiv](https://arxiv.org/abs/2607.02121)　📅 2026-07

**关键词**：`analysis`、`guardrail activation`、`behavioral monitoring`、`black-box inference`

👤 **作者**：William Hackett、Peter Garraghan

- 🎯 **研究动机**：黑盒对抗仿真中难以区分拦截来自护栏还是 LLM 拒绝，而绕过两者所需技术差异巨大
- 🔬 **研究方法**：提出首个黑盒护栏侦察方法：仅凭黑盒访问与零先验，通过 HTTP、词汇与时序信号的行为监测判定护栏存在、封锁内容类别并区分护栏拦截与模型拒绝
- 📌 **结论**：护栏存在检测准确率 100%（良性-恶意行为分离 q<0.001），区分拦截来源的平均 F1 98%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) and agentic systems become integrated into real-world applications, ensuring their safety and security is critical. Guardrail systems that detect and block malicious instructions sent to and from an LLM are an essential component of AI security. However, researchers conducting black-box adversarial emulation against production AI systems often struggle to determine whether a guardrail block or an LLM rejection has occurred. This distinction is important because the techniques used to bypass guardrails can differ substantially from those used to bypass LLM safety alignment, and has a material impact on attack technique selection and optimization. We propose the first black-box guardrail reconnaissance methodology, which detects the presence of a guardrail within a target AI system through behavioral monitoring of HTTP, lexical, and timing signals, assuming only black-box access and zero prior knowledge of the guardrail or AI system. Experiments demonstrate that our approach detects guardrail presence with 100% accuracy, with statistically significant behavioral separation between benign and malicious interactions (q < 0.001). Our approach further identifies the content categories a guardrail is designed to block, and distinguishes guardrail blocks from LLM rejection on unseen prompts with an average F1 score of 98%.

</details>

### 26. Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

📄 [arXiv](https://arxiv.org/abs/2606.25782)　📅 2026-06

**关键词**：`analysis`、`encoder-decoder comparison`、`safety judge`、`adversarial evaluation`

👤 **作者**：Han Jeon、Shiv Medler、Joseph Voyles、Matt Wood

- 🎯 **研究动机**：LLM judge 慢且贵，微调 ModernBERT 系编码器能否无损替代其对有害输出的判定未知
- 🔬 **研究方法**：在对抗数据集上把编码器分类器与规则匹配、微调 LLM 分类器、多种 judge 提示策略（StrongReject、ShieldGemma、LlamaGuard 等）对齐比较，按攻击技术细分
- 📌 **结论**：给出编码器分类器何时可作为低成本低延迟替代的实证指导

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency. Safety evaluation of LLM outputs has generally relied on LLM-based judges, which can be effective but are often slow and expensive to deploy at scale. In this paper, we evaluate whether fine-tuned modern encoder classifiers from the ModernBERT family, including ModernBERT and Ettin, can reliably identify harmful LLM outputs in user-model conversations without substantial performance loss relative to LLM-based judges. We benchmark these encoder classifiers against rule-based prefix matching, fine-tuned LLM classifiers, and LLM judges using a range of judge-prompting strategies across open-source adversarial datasets. The LLM judges include evaluation methodologies from StrongReject, ShieldGemma, JailbreakBench, AILuminate, SorryBench, and a Claude-as-a-judge setup, as well as fine-tuned safety classifiers such as LlamaGuard 3 and LlamaGuard 4. The encoder classifiers are fine-tuned on judge-labeled data using a majority-voting label strategy and are then evaluated on a gold-standard holdout dataset to assess their performance relative to LLM judges. We report absolute performance using F1 score, false negative rate, and precision-recall metrics. We also break down results by attack technique, including single-turn prompting, decomposition, escalation, and context manipulation, to identify where encoder classifiers align with or diverge from LLM-based judges. Our findings provide guidance on when encoder classifiers can serve as cost- and latency-efficient alternatives to LLM-based safety evaluation.

</details>

### 27. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers

📄 [arXiv](https://arxiv.org/abs/2605.10901)　📅 2026-05

**关键词**：`analysis`、`formal verification`、`harmful region`、`classifier certificate`

👤 **作者**：Nikita Kezins、Urbas Ekka、Pascal Berrang、Luca Arnaboldi

- 🎯 **研究动机**：护栏分类器只有经验指标而无形式保证，离散输入空间无自然有害规范、epsilon 球也无语义意义
- 🔬 **研究方法**：把验证移到 pre-activation 空间，将有害区域定义为凸形状（SVD 对齐超矩形给精确 SAT/UNSAT 证书，GMM 给概率证书），利用 sigmoid 单调性 O(d) 闭环证明
- 📌 **结论**：三个自训护栏分类器的全部超矩形配置返回 SAT，暴露可证明安全洞；BERT 的保证覆盖率在最优阈值塌缩到 55%——高经验分不等于形式保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail Classifiers defend production language models against harmful behavior, but although results seem promising in testing, they provide no formal guarantees. Providing formal guarantees for such models is hard because "harmful behavior" has no natural specification in a discrete input space: and the standard epsilon-ball properties used in other domains do not carry semantic meaning. We close this gap by shifting verification from the discrete input space to the classifier's pre-activation space, where we define a harmful region as a convex shape enclosing the representations of known harmful prompts. Because the sigmoid classification head is monotonic, certifying the worst-case point is sufficient to certify the entire region, yielding a closed-form soundness proof without approximation in O(d) time. To formally evaluate these classifiers, we propose two constructions of such regions: SVD-aligned hyper-rectangles, which yield exact SAT/UNSAT certificates, and Gaussian Mixture Models, which yield probabilistic certificates over semantically coherent clusters. Applying this framework to three author-trained Guardrail Classifiers on the toxicity domain, every hyper-rectangle configuration returns SAT, exposing verifiable safety holes across all classifiers, despite seemingly high empirical metrics. Probabilistic GMM certificates also expose a divergent structural stability in how these models represent harm. While GPT-2 and Llama-3.1-8B maintain robust coverage of 90% and 80% across varying boundaries, BERT's safety guarantees prove uniquely volatile. This 'coverage collapse' to 55% at the optimal threshold reveals a sparsely populated safety margin in BERT, which only achieves full coverage by adopting an extremely conservative pessimistic threshold. These approaches combined, provide new insights on how effective Guardrail Classifiers really are, beyond traditional red-teaming.

</details>

### 28. When AI Agents Disagree Like Humans: Reasoning Trace Analysis for Human-AI Collaborative Moderation

📄 [arXiv](https://arxiv.org/abs/2604.03796)　📅 2026-04　🏷 ICLR 2026 Workshop

**关键词**：`analysis`、`multi-agent moderation`、`reasoning disagreement`、`human escalation`

👤 **作者**：Michał Wawer、Jarosław A. Chudziak

- 🎯 **研究动机**：多 agent 分歧被普遍当作待消除的噪声，其作为信号的价值未被检验
- 🔬 **研究方法**：在仇恨言论审核中嵌入五个视角差异化 agent 的推理轨迹，按推理相似性与结论一致性四分类分歧模式，并与人工标注冲突对照
- 📌 **结论**：agent 结论一致与否比原始推理分歧更能预测人工分歧（效应量 d>0.8），支持从共识寻求转向不确定性呈现的多 agent 设计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When LLM-based multi-agent systems disagree, current practice treats this as noise to be resolved through consensus. We propose it can be signal. We focus on hate speech moderation, a domain where judgments depend on cultural context and individual value weightings, producing high legitimate disagreement among human annotators. We hypothesize that convergent disagreement, where agents reason similarly but conclude differently, indicates genuine value pluralism that humans also struggle to resolve. Using the Measuring Hate Speech corpus, we embed reasoning traces from five perspective-differentiated agents and classify disagreement patterns using a four-category taxonomy based on reasoning similarity and conclusion agreement. We find that raw reasoning divergence weakly predicts human annotator conflict, but the structure of agent discord carries additional signal: cases where agents agree on a verdict show markedly lower human disagreement than cases where they do not, with large effect sizes (d>0.8) surviving correction for multiple comparisons. Our taxonomy-based ordering correlates with human disagreement patterns. These preliminary findings motivate a shift from consensus-seeking to uncertainty-surfacing multi-agent design, where disagreement structure - not magnitude - guides when human judgment is needed.

</details>

### 29. Engagement Undermines Safety: How Stereotypes and Toxicity Shape Humor in Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.373/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`harmful generation`、`engagement reward`、`toxicity amplification`、`humor reward`

👤 **作者**：Atharvan Dogra、Soumya Suvra Ghosal、Ameet Deshpande、Ashwin Kalyan、Dinesh Manocha

- 🎯 **研究动机**：LLM 广泛用于创意与互动内容，趣味性优化是否与有害内容耦合未知
- 🔬 **研究方法**：以幽默生成为试验台联合测量幽默、刻板性与毒性并用信息论指标分析不协调信号，配讽刺生成任务的人类感知趣味判断
- 📌 **结论**：固定中性设定下有害输出获更高幽默分，存在生成器-评估器偏置放大环；刻板与毒性笑话平均幽默分高 10 至 21%，在被 LLM 标记有趣的笑话中多 11 至 28%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly used for creative writing and engagement content, raising safety concerns about their outputs. Using humor generation as a testbed, this work evaluates how funniness optimization in modern LLM pipelines couples with harmful content by jointly measuring humor, stereotypicality, and toxicity. We further supplement this by analyzing incongruity signals through information-theoretic metrics. Across six models, we observe that even for fixed neutral setups, harmful outputs receive higher humor scores, indicating a bias amplification loop between generators and evaluators. Information-theoretic analyses show that harmful cues widen predictive uncertainty and, surprisingly, can even make harmful punchlines more expected for some models, suggesting intrinsic structural embedding in learned humor distributions. Experiments and human evaluation on an additional satire-generation task with human-perceived funniness judgments show that LLM funniness relies on increased stereotypicality and toxicity, including for closed models. Quantitatively, stereotypical/toxic jokes gain 10%–21% in mean humor score, stereotypical jokes appear 11% to 28% more often among the jokes marked funny by an LLM-based metric, and up to 10% more often in generations perceived as funny by humans.

</details>

### 30. Reasoning’s Razor: Reasoning Improves Accuracy but Hurts Recall at Critical Operating Points in Safety and Hallucination Detection

🎓 [Official](https://aclanthology.org/2026.eacl-long.190/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`safety detector`、`low-FPR regime`、`reasoning trade-off`

👤 **作者**：Atoosa Chegini、…、Mehrdad Farajtabar

- 🎯 **研究动机**：推理提升分类准确率的同时，其在严格低误报率（FPR）精度敏感场景的适用性缺乏系统研究
- 🔬 **研究方法**：在安全检测与幻觉检测两个任务上，对微调与零样本设定、标准 LLM 与 LRM 系统比较开启/关闭推理的表现
- 📌 **结论**：开推理提升整体准确率但在低 FPR 阈值处表现差，关推理在精度敏感区间占优；基于 token 的打分显著优于自述置信度，二者集成可兼得

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning has become a central paradigm for large language models (LLMs), consistently boosting accuracy across diverse benchmarks. Yet its suitability for precision-sensitive use remains unclear. We present the first systematic study of reasoning for classification tasks under strict low false positive rate (FPR) regimes. Our analysis covers two tasks—safety detection and hallucination detection—evaluated in both fine-tuned and zero-shot settings, using standard LLMs and Large Reasoning Models (LRMs). Our results reveal a clear trade-off: Think On (reasoning-augmented) generation improves overall accuracy, but performs poorly at the low-FPR thresholds essential for practical use. In contrast, Think Off (no reasoning during inference) dominates in these precision-sensitive regimes, with Think On surpassing only when higher FPRs are acceptable. In addition, we find token-based scoring substantially outperforms self-verbalized confidence for precision-sensitive deployments. Finally, a simple ensemble of the two modes recovers the strengths of each. Taken together, our findings position reasoning as a double-edged tool: beneficial for average accuracy, but often ill-suited for applications requiring strict precision.

</details>

### 31. Are Open-Weight LLMs Ready for Social Media Moderation? A Comparative Study on Bluesky

📄 [arXiv](https://arxiv.org/abs/2602.05189)　📅 2026-02

**关键词**：`analysis`、`open-weight moderator`、`social-media deployment`、`privacy-preserving inference`

👤 **作者**：Hsuan-Yu Chou、Wajiha Naveed、Shuyan Zhou、Xiaowei Yang

- 🎯 **研究动机**：开源权重 LLM 能否开箱即用胜任社媒审核缺乏系统评估
- 🔬 **研究方法**：以 Bluesky 真实帖文、平台审核决定与人工标注为参照，比较 3 个 open-weight 与 4 个闭源模型的零样本审核表现
- 📌 **结论**：开源模型 sensitivity 81%-97%、specificity 91%-100%，与闭源（72%-98%、93%-99%）大幅重叠，可支撑本地隐私保护审核

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As internet access expands, so does exposure to harmful content, increasing the need for effective moderation. Research has demonstrated that large language models (LLMs) can be effectively utilized for social media moderation tasks, including harmful content detection. While proprietary LLMs have been shown to zero-shot outperform traditional machine learning models, the out-of-the-box capability of open-weight LLMs remains an open question. Motivated by recent developments of reasoning LLMs, we evaluate seven state-of-the-art models: four proprietary and three open-weight. Testing with real-world posts on Bluesky, moderation decisions by Bluesky Moderation Service, and annotations by two authors, we find a considerable degree of overlap between the sensitivity (81%--97%) and specificity (91%--100%) of the open-weight LLMs and those (72%--98%, and 93%--99%) of the proprietary ones. Additionally, our analysis reveals that specificity exceeds sensitivity for rudeness detection, but the opposite holds for intolerance and threats. Lastly, we identify inter-rater agreement across human moderators and the LLMs, highlighting considerations for deploying LLMs in both platform-scale and personalized moderation contexts. These findings show open-weight LLMs can support privacy-preserving moderation on consumer-grade hardware and suggest new directions for designing moderation systems that balance community values with individual user preferences.

</details>

### 32. RAG Makes Guardrails Unsafe? Investigating Robustness of Guardrails under RAG-style Contexts

📄 [arXiv](https://arxiv.org/abs/2510.05310)　📅 2025-10

**关键词**：`analysis`、`RAG context`、`distribution shift`、`input-output guard`

👤 **作者**：Yining She、…、Dan Roth

- 🎯 **研究动机**：护栏模型本身是 LLM，对 RAG 式上下文带来的分布漂移的鲁棒性未被检验
- 🔬 **研究方法**：系统评测 3 个 Llama Guard 与 2 个 GPT-oss 在含检索文档上下文下的判断稳定性，并分离文档、查询与响应各成分的影响
- 📌 **结论**：仅插入良性文档即改变输入与输出护栏约 11% 与 8% 的判断；两种缓解仅带来微小改进，暴露上下文鲁棒性缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the increasing adoption of large language models (LLMs), ensuring the safety of LLM systems has become a pressing concern. External LLM-based guardrail models have emerged as a popular solution to screen unsafe inputs and outputs, but they are themselves fine-tuned or prompt-engineered LLMs that are vulnerable to data distribution shifts. In this paper, taking Retrieval Augmentation Generation (RAG) as a case study, we investigated how robust LLM-based guardrails are against additional information embedded in the context. Through a systematic evaluation of 3 Llama Guards and 2 GPT-oss models, we confirmed that inserting benign documents into the guardrail context alters the judgments of input and output guardrails in around 11% and 8% of cases, making them unreliable. We separately analyzed the effect of each component in the augmented context: retrieved documents, user query, and LLM-generated response. The two mitigation methods we tested only bring minor improvements. These results expose a context-robustness gap in current guardrails and motivate training and evaluation protocols that are robust to retrieval and query composition.

</details>

### 33. Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?

📄 [arXiv](https://arxiv.org/abs/2512.24044)　📅 2025-12

**关键词**：`survey`、`full-pipeline evaluation`、`input-output filter`、`jailbreak detection`

👤 **作者**：Yuan Xin、Dingfan Chen、Linyi Yang、Michael Backes、Xiao Zhang

- 🎯 **研究动机**：已有越狱评估只针对裸模型，忽略含内容审核过滤器的完整部署流水线
- 🔬 **研究方法**：首次系统评估越狱攻击在含输入与输出过滤两阶段的完整推理管线上的成功率
- 📌 **结论**：几乎所有被评测越狱技术都会被至少一个安全过滤器检出，先前研究高估了攻击的实际成功率；但过滤器仍需平衡召回与精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed, ensuring their safe use is paramount. Jailbreaking, adversarial prompts that bypass model alignment to trigger harmful outputs, present significant risks, with existing studies reporting high success rates in evading common LLMs. However, previous evaluations have focused solely on the models, neglecting the full deployment pipeline, which typically incorporates additional safety mechanisms like content moderation filters. To address this gap, we present the first systematic evaluation of jailbreak attacks targeting LLM safety alignment, assessing their success across the full inference pipeline, including both input and output filtering stages. Our findings yield two key insights: first, nearly all evaluated jailbreak techniques can be detected by at least one safety filter, suggesting that prior assessments may have overestimated the practical success of these attacks; second, while safety filters are effective in detection, there remains room to better balance recall and precision to further optimize protection and user experience. We highlight critical gaps and call for further refinement of detection accuracy and usability in LLM safety systems.

</details>

### 34. SoK: Evaluating Jailbreak Guardrails for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2506.10597) · 🎓 [Official](https://sp2026.ieee-security.org/accepted-papers.html)　📅 2025-06　🏷 IEEE S&P 2026

**关键词**：`survey`、`jailbreak guardrails`、`evaluation framework`、`adaptive attacks`

👤 **作者**：Xunguang Wang、Zhenlan Ji、Wenxuan Wang、Zongjie Li、Daoyuan Wu、Shuai Wang

- 🎯 **研究动机**：LLM 越狱护栏领域碎片化，缺乏统一分类与综合评估框架
- 🔬 **研究方法**：提出六维护栏分类法与 Security-Efficiency-Utility 评估框架，经系统实验分析护栏的强弱项
- 📌 **结论**：厘清现有护栏在不同攻击类型下的普适性与优化方向，为护栏研发提供结构化基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved remarkable progress, but their deployment has exposed critical vulnerabilities, particularly to jailbreak attacks that circumvent safety alignments. Guardrails--external defense mechanisms that monitor and control LLM interactions--have emerged as a promising solution. However, the current landscape of LLM guardrails is fragmented, lacking a unified taxonomy and comprehensive evaluation framework. In this Systematization of Knowledge (SoK) paper, we present the first holistic analysis of jailbreak guardrails for LLMs. We propose a novel, multi-dimensional taxonomy that categorizes guardrails along six key dimensions, and introduce a Security-Efficiency-Utility evaluation framework to assess their practical effectiveness. Through extensive analysis and experiments, we identify the strengths and limitations of existing guardrail approaches, provide insights into optimizing their defense mechanisms, and explore their universality across attack types. Our work offers a structured foundation for future research and development, aiming to guide the principled advancement and deployment of robust LLM guardrails. The code is available at https://github.com/xunguangwang/SoK4JailbreakGuardrails.

</details>

### 35. Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation

📄 [arXiv](https://arxiv.org/abs/2609.03814)　📅 2026-09

**关键词**：`benchmark`、`content moderation`、`criterion-conditioned behavior`、`pairwise evaluation`

👤 **作者**：Danting Zhang、Bei Peng、Robert Loftin

- 🎯 **研究动机**：内容审核 benchmark 把多条审核标准聚合为单标签，无法判断模型能否解耦并逐条应用标准
- 🔬 **研究方法**：提出标准无关的内容因子化 DECO 与同输入跨标准 pairwise 评测，在四个审核数据集、四个 LLM 上检验 criterion-conditioned 行为
- 📌 **结论**：强基准表现可掩盖标准级失败：当正确决策取决于标准所要求评估的特定侧面而非总体有害性时模型最挣扎——聚合标签上的好成绩不构成按单条标准可靠评判的证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multiple moderation criteria into a single label, making it unclear whether models can disentangle them and reliably apply each criterion when making decisions. To study whether LLMs exhibit criterion-conditioned behaviour, we introduce Diagnostic Evaluation of COntent (DECO), a criterion-independent factorisation of content that enables controlled, criterion-level evaluation. We also introduce pairwise evaluation to compare model outputs across different criteria for the same input. Across four moderation datasets and four LLMs, we find that strong benchmark performance can hide substantial failures at the criterion level. Models struggle most when correct decisions depend not on overall harmfulness, but on the specific aspect of the content that the criterion requires them to assess. Our results highlight a key limitation of current content moderation benchmarks: strong performance on aggregated labels does not provide sufficient evidence that LLMs can reliably evaluate content with respect to individual moderation criteria. These findings call for the development of evaluation methods that explicitly measure criterion-conditioned behaviour.

</details>

### 36. Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation

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

### 37. LongPIBench: A Long-Context Benchmark for Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.28411)　📅 2026-08

**关键词**：`benchmark`、`long-context guardrail`、`prompt injection`、`real-world evaluation`、`long-context injection`、`real-world documents`

👤 **作者**：Yupei Liu、Yuqi Jia、Neil Zhenqiang Gong、Jinyuan Jia

- 🎯 **研究动机**：现有提示注入 benchmark 集中于短上下文输入，长上下文中的注入攻防几乎未被探索，导致对防御有效性的高估
- 🔬 **研究方法**：构建 LongPIBench，覆盖论文评审、简历筛选、代码审查、邮件摘要四类真实场景，每场景含合成与真实数据集，上下文长度从数千到数万 token
- 📌 **结论**：评测显示长上下文设定下即使简单启发式注入也取得高成功率，并频繁绕过 SOTA 提示注入防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely unexplored. This gap leads to a substantial overestimation of the effectiveness of current defenses. In this paper, we bridge the gap by introducing LongPIBench, a long-context benchmark for prompt injection covering 4 realistic application scenarios: paper peer review, resume screening, code review, and email summary. For each scenario, we construct a synthetic dataset and a real-world dataset, with context lengths ranging from thousands to tens of thousands of tokens. The evaluation results on LongPIBench reveal significant vulnerabilities of prompt injection defenses under long-context settings: even simple heuristic prompt injection attacks achieve high success rates and frequently bypass state-of-the-art defenses. We hope LongPIBench can serve as a practical benchmark for systematically evaluating prompt injection defenses in realistic long-context scenarios.

</details>

### 38. The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions

📄 [arXiv](https://arxiv.org/abs/2608.27009)　📅 2026-08

**关键词**：`benchmark`、`over-safety validity`、`mechanical labeling`、`twin contrast`、`agent guardrail`、`over-refusal`

👤 **作者**：Yingjie Zhang、Yuanbo Xie、Kai Chen

- 🎯 **研究动机**：Agent guardrail 的 over-safety 难以评测：授权边界处动作彼此相似，安全标签取决于授权策略而非动作本身，真实数据难以收集与验证
- 🔬 **研究方法**：构建 Cautious Bench，将每个样本与显式授权策略共同设计，构建时门机制使标签成为策略的机械推论，含 756 个 benign/twin 对（三种对象名共 2268 对）与 40 个 Undecidable 对
- 📌 **结论**：实测五类设计的六个 guardrail 均现名称迷信效应：仅把对象名换成危险措辞就更频繁拒绝合法动作，说明其依赖表面名称而非授权上下文

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one that maps the decision boundary of an ideal guardrail. Harvesting such a benchmark from real data is impractical: boundary cases are hard to collect, their labels hard to verify. The gap is real, so we construct Cautious Bench, the first benchmark to make over-safety the construct for agent guardrails; it codesigns each sample and its label with a stated authorization policy. A build-time gate re-derives every example to certify it, so each label is a mechanical consequence of the policy rather than an annotator's per-sample verdict, a reference against which researchers can measure real guardrails. The benchmark renders 756 Decidable benign/twin pairs, each under three object-name types (2,268 measured pairs), and 40 Undecidable pairs reported separately. Measuring six guardrails from five designs, we find a name-superstition effect: each over-refuses an authorized action more often under a scary-looking object name than a benign one. Since only the object name varies in the aforementioned contrast experiments, the deviation is the name's doing: the guardrails read the surface label, not the authorization context.

</details>

### 39. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

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

### 40. Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages

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

### 41. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

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

### 42. HarmProfile: Characterizing Harmful Distributions in Frontier LLMs

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

### 43. ADVERSA: Measuring Multi-Turn Guardrail Degradation and Judge Reliability in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.10068)　📅 2026-03

**关键词**：`benchmark`、`multi-turn degradation`、`continuous compliance`、`judge reliability`

👤 **作者**：Harry Owiredu-Ashley

- 🎯 **研究动机**：单提示二元 pass/fail 评测无法刻画持续对抗交互下的护栏退化动态
- 🔬 **研究方法**：ADVERSA 用去除安全拒绝的 70B 攻击模型按 5 级 rubric 记录逐轮合规轨迹，三 judge 共识架构并把 judge 可靠性作为一等研究对象
- 📌 **结论**：三个前沿模型越狱率 26.7% 且平均发生在第 1.25 轮，成功集中于早段而非持续施压累积；系统记录了 judge 分歧、自评倾向与攻击者漂移等误差源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most adversarial evaluations of large language model (LLM) safety assess single prompts and report binary pass/fail outcomes, which fails to capture how safety properties evolve under sustained adversarial interaction. We present ADVERSA, an automated red-teaming framework that measures guardrail degradation dynamics as continuous per-round compliance trajectories rather than discrete jailbreak events. ADVERSA uses a fine-tuned 70B attacker model (ADVERSA-Red, Llama-3.1-70B-Instruct with QLoRA) that eliminates the attacker-side safety refusals that render off-the-shelf models unreliable as attackers, scoring victim responses on a structured 5-point rubric that treats partial compliance as a distinct measurable state. We report a controlled experiment across three frontier victim models (Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.2) using a triple-judge consensus architecture in which judge reliability is measured as a first-class research outcome rather than assumed. Across 15 conversations of up to 10 adversarial rounds, we observe a 26.7% jailbreak rate with an average jailbreak round of 1.25, suggesting that in this evaluation setting, successful jailbreaks were concentrated in early rounds rather than accumulating through sustained pressure. We document inter-judge agreement rates, self-judge scoring tendencies, attacker drift as a failure mode in fine-tuned attackers deployed out of their training distribution, and attacker refusals as a previously-underreported confound in victim resistance measurement. All limitations are stated explicitly. Attack prompts are withheld per responsible disclosure policy; all other experimental artifacts are released.

</details>

### 44. SoftHateBench: Evaluating Moderation Models Against Reasoning-Driven, Policy-Compliant Hostility

📄 [arXiv](https://arxiv.org/abs/2601.20256)　📅 2026-01

**关键词**：`benchmark`、`soft-hate moderation`、`reasoning-driven hostility`、`policy-compliant evasion`

👤 **作者**：Xuanyu Su、Diana Inkpen、Nathalie Japkowicz

- 🎯 **研究动机**：表面合规但以论证引导排斥群体的 soft hate 超出基于表层毒性线索的审核能力，且无基准系统度量
- 🔬 **研究方法**：结合 Argumentum Model of Topics 与 Relevance Theory 把显性仇恨立场改写为表面中性且逻辑连贯的论述，构建覆盖 7 个领域、28 个目标群体、4745 实例的基准
- 📌 **结论**：encoder 检测器、通用 LLM 与安全模型从 hard 到 soft 层级一致退化，暴露依赖毒性词面的审核盲点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online hate on social media ranges from overt slurs and threats (\emph{hard hate speech}) to \emph{soft hate speech}: discourse that appears reasonable on the surface but uses framing and value-based arguments to steer audiences toward blaming or excluding a target group. We hypothesize that current moderation systems, largely optimized for surface toxicity cues, are not robust to this reasoning-driven hostility, yet existing benchmarks do not measure this gap systematically. We introduce \textbf{\textsc{SoftHateBench}}, a generative benchmark that produces soft-hate variants while preserving the underlying hostile standpoint. To generate soft hate, we integrate the \emph{Argumentum Model of Topics} (AMT) and \emph{Relevance Theory} (RT) in a unified framework: AMT provides the backbone argument structure for rewriting an explicit hateful standpoint into a seemingly neutral discussion while preserving the stance, and RT guides generation to keep the AMT chain logically coherent. The benchmark spans \textbf{7} sociocultural domains and \textbf{28} target groups, comprising \textbf{4,745} soft-hate instances. Evaluations across encoder-based detectors, general-purpose LLMs, and safety models show a consistent drop from hard to soft tiers: systems that detect explicit hostility often fail when the same stance is conveyed through subtle, reasoning-based language. \textcolor{red}{\textbf{Disclaimer.} Contains offensive examples used solely for research.}

</details>

### 45. N-GLARE: An Non-Generative Latent Representation-Efficient LLM Safety Evaluator

🎓 [Official](https://aclanthology.org/2026.acl-long.1334/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`guard model`、`content moderation`、`safety-utility trade-off`、`representation intervention`、`harmful content`

👤 **作者**：Zheyu Lin、Jirui Yang、Yukui Qiu、Yubing Bao、Hengqi Guo、Yao Guan

- 🎯 **研究动机**：主流红队方法靠在线生成与黑盒输出分析，成本高反馈延迟，不适合新模型训练后的敏捷诊断
- 🔬 **研究方法**：N-GLARE 完全在潜表示上运行：分析 APT（Angular-Probabilistic Trajectory）隐层动力学并提出 JSS（Jensen-Shannon Separability）度量
- 📌 **结论**：40 余个模型、20 种红队策略上 JSS 与安全排名高度一致，token 与运行时成本不到 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the safety robustness of LLMs is critical for their deployment. However, mainstream Red Teaming methods rely on online generation and black-box output analysis. These approaches are not only costly but also suffer from feedback latency, making them unsuitable for agile diagnostics after training a new model.To address this, we propose N-GLARE (A Non-Generative, Latent Representation-Efficient LLM Safety Evaluator). N-GLARE operates entirely on the model’s latent representations, bypassing the need for full text generation. It characterizes hidden layer dynamics by analyzing the APT (Angular-Probabilistic Trajectory) of latent representations and introducing the JSS (Jensen-Shannon Separability) metric.Experiments on over 40 models and 20 red teaming strategies demonstrate that the JSS metric exhibits high consistency with Red Teaming safety rankings at less than 1% token and runtime cost.

</details>

### 46. Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

📄 [arXiv](https://arxiv.org/abs/2608.22444)　📅 2026-08

**关键词**：`analysis`、`attack`、`collective misalignment`、`monitor population`、`capture forecasting`、`agent population`

👤 **作者**：Isotta Magistrali、Chen Shani

- 🎯 **研究动机**：AI 安全评测单位仍是单模型，而 LLM agent 日益以相互读写决策的群体部署——单体校准良好也可能被邻近 agent 拉偏，单体检计无法回答群体行为
- 🔬 **研究方法**：在安全分诊任务上让 LLM monitor 群体决定警报升级或忽略，注入始终单向施压的 committed minority，并用攻击前响应函数预测群体漂移幅度
- 📌 **结论**：单体几乎同判的两条警报可使集体行为截然不同且可提前预测；公开推理能中和弱攻击但只延迟强攻击；移除施压者后群体回归原位——capture 是暂时状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

</details>

### 47. Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation

🎓 [Official](https://aclanthology.org/2026.acl-long.1741/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`persona vector`、`behavior steering`、`trait stability`、`content moderation`、`safety alignment`

👤 **作者**：Huije Lee、Jisu Shin、Hoyun Song、Changgeon Ko、Jong C. Park

- 🎯 **研究动机**：静态有害内容基准扩展性与多样性受限，且受网络级预训练语料污染
- 🔬 **研究方法**：用 persona 引导的 LLM agent 合成有害内容：把人口身份与主题兴趣的二维 persona 结合情境化有害策略，从有害性、难度与多样性三维度评估
- 📌 **结论**：合成场景比现有基准更难检测，语言与主题多样性与人工数据集相当，适合压力测试检测系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Static benchmarks for harmful content detection face limitations in scalability and diversity, and may also be affected by contamination from web-scale pre-training corpora. To address these issues, we propose a framework for synthesizing harmful content, leveraging persona-guided large language model (LLM) agents. Our approach constructs two-dimensional user personas by integrating demographic identities and topical interests with situational harmful strategies, enabling the simulation of diverse and contextually grounded harmful interactions. We evaluate the framework along three dimensions: harmfulness, challenge level, and diversity. Both human and LLM-based evaluations confirm that our framework achieves a high harmful generation success rate. Experiments across multiple detection systems reveal that our synthetic scenarios are more challenging to detect than those in existing benchmarks. Furthermore, a multi-faceted analysis confirms that our approach achieves linguistic and topical diversity comparable to human-curated datasets, establishing our framework as an effective tool for robust stress-testing of harmful content detection systems.

</details>

### 48. Overflip: Repetition-Induced Label Flips in Guardrail Models

📄 [arXiv](https://arxiv.org/abs/2609.15013)　📅 2026-09

**关键词**：`attack`、`guardrail model`、`repetition-induced label flip`、`attention dispersion`、`position encoding`

👤 **作者**：Xu He、Chih-Hsuan Lin、Hung-Mao Chen、Junjie Xiong、Yan Zhai、Kun Sun

- 🎯 **研究动机**：轻量 guardrail 模型用短训练窗口（典型 512 tokens）+桶化相对位置编码处理长输入，其决策随输入变长保持稳定的假设未被检验
- 🔬 **研究方法**：识别 Overflip：重复 prompt 使 guardrail 预测随序列增长翻转（恶意→良性）；在 9 个广泛使用的轻量 guardrail 模型、100 prompt 基准上实验
- 📌 **结论**：5 个模型出现翻转，flip 率 8%-92%，首次翻转在约 2.6k-9.4k tokens；Overflip 保留恶意内容但把 token 级注意力同质化到重复结构——比传统注意力稀释更具威胁的 guardrail 结构脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail&#39;s decision is stable as the input is lengthened. We show that this assumption can fail. We identify Overflip, a repetition-induced instability where repeating a prompt causes the guardrail&#39;s prediction to flip (MAL$\to$BEN) as the sequence grows. We conduct experiments on 9 widely used lightweight guardrail models. Five exhibit MAL$\to$BEN flips on a benchmark of 100 prompts, with confidence margins shrinking steadily with repetition. Among these vulnerable models, flip rates range from 8% to 92%, with first flips occurring at roughly 2.6k--9.4k tokens. Our analysis suggests Overflip differs from traditional attention-dilution baselines, which aim to divert the model&#39;s attention away from tokens associated with malicious content, shifting it instead toward unrelated content, such as benign padding or shuffling. While Overflip preserves malicious content, it homogenizes token-level attention over repeated structure and induces a distinct, more gradual attention-dispersion trajectory than padding. Moreover, Overflip poses a greater threat to LLM services than traditional attention dilution methods. Because the bypassed prompt remains semantically intact and is still readily understood by downstream business LLMs, it can transmit malicious intent after passing the guardrail. These findings expose repetition as an attack surface for guardrail models and motivate length-robust evaluation and mitigation.

</details>
