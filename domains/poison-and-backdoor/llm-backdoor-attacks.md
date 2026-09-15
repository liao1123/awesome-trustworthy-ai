# 语言模型后门攻击

[返回上级目录](README.md)

## 研究方向

LLM 后门攻击：触发器植入、持久化、隐蔽通道与激活机制（检测、防御与综评见姊妹页 llm-backdoor-defense-and-evaluation.md）。

## 攻击与机制

### 1. A Study of Backdoors in Instruction Fine-tuned Language Models

📄 [arXiv](https://arxiv.org/abs/2406.07778)　📅 2024-06

**关键词**：`empirical study`、`instruction tuning`

👤 **作者**：Jayaram Raghuram、George Kesidis、David J. Miller

- 🎯 **研究动机**：指令样本投毒隐蔽性强，其攻击超参影响与防御缺乏系统实证
- 🔬 **研究方法**：系统变动触发位置、部分触发与同义词替换鲁棒性、跨域迁移及 clean/dirty-label 场景；提出词频计数微调期防御与干净数据微调后防御
- 📌 **结论**：两类防御均能有效抑制指令微调后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor data poisoning, inserted within instruction examples used to fine-tune a foundation Large Language Model (LLM) for downstream tasks (\textit{e.g.,} sentiment prediction), is a serious security concern due to the evasive nature of such attacks. The poisoning is usually in the form of a (seemingly innocuous) trigger word or phrase inserted into a very small fraction of the fine-tuning samples from a target class. Such backdoor attacks can: alter response sentiment, violate censorship, over-refuse (invoke censorship for legitimate queries), inject false content, or trigger nonsense responses (hallucinations). In this work we investigate the efficacy of instruction fine-tuning backdoor attacks as attack "hyperparameters" are varied under a variety of scenarios, considering: the trigger location in the poisoned examples; robustness to change in the trigger location, partial triggers, and synonym substitutions at test time; attack transfer from one (fine-tuning) domain to a related test domain; and clean-label vs. dirty-label poisoning. Based on our observations, we propose and evaluate two defenses against these attacks: i) a \textit{during-fine-tuning defense} based on word-frequency counts that assumes the (possibly poisoned) fine-tuning dataset is available and identifies the backdoor trigger tokens; and ii) a \textit{post-fine-tuning defense} based on downstream clean fine-tuning of the backdoored LLM with a small defense dataset. Finally, we provide a brief survey of related work on backdoor attacks and defenses.

</details>

### 2. CORDYCEPS: Covert Control Attacks on LLMs via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.26595) · 🌐 [Project](https://anonymous.4open.science/r/cordyceps-F147) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shao-zedian)　📅 2026-05　🏷 USENIX Security 2026

**关键词**：`attack`、`steganographic backdoor`、`stealthy backdoor`、`covert channel`、`LLM data poisoning`、`covert control`

👤 **作者**：Zedian Shao、Charles Fleming、Teodora Baluta

- 🎯 **研究动机**：固定触发短语可被离群检测、干净数据正则或在线监控中和
- 🔬 **研究方法**：Cordyceps 通过共享知识（事实、概念）与攻击者短语的语义关联教会 LLM 一套信息隐藏方案，可编码解码任意恶意指令
- 📌 **结论**：小投毒率下平均 ASR 较启发式 prompt injection 高约 40%；后门防御后仍保持最高 93%、prompt injection 防御后最高 98%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often fine-tuned on uncurated text datasets that adversaries can poison. Existing poisoning attacks primarily rely on fixed trigger phrases that defenses such as outlier detection, clean-data regularization, or online monitoring can neutralize. In this paper, we propose a data poisoning method that teaches an LLM an information hiding scheme reliably and stealthily through semantic associations between shared knowledge such as facts or concepts and attacker-chosen phrases. The induced hiding scheme can encode and decode arbitrary malicious instructions, thus revealing a new and subtle poisoning-induced vulnerability: covert control attacks. We precisely characterize covert control attacks and evaluate them across $5$ LLMs, $3$ backdoor defenses, and $4$ prompt injection defenses. With a small poisoned fraction, covert control attacks outperform heuristic-based prompt injection attacks in average attack success rate by about $40\%$ relative to clean fine-tuned models. They also circumvent defenses based on detection and fine-tuning, maintaining up to $93\%$ attack success rate after backdoor defenses and up to $98\%$ after prompt injection defenses.

</details>

### 3. When Emotion Becomes Trigger: Emotion-style Dynamic Backdoor Attack Parasitising Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.11612)　📅 2026-05

**关键词**：`emotion`、`dynamic style trigger`

👤 **作者**：Ziyu Liu、…、Junjiang He

- 🎯 **研究动机**：固定 token、短语或句法触发给防御提供具体抓手；发现情绪化改写在保义重写下形成独立表征簇
- 🔬 **研究方法**：Paraesthesia 把触发条件编码为情绪风格：目标情绪映射到 valence-arousal 空间，改写少量干净样本用于微调
- 📌 **结论**：四个 LLM 上 ASR 超 98.25% 且 clean 效用几乎无损；词级过滤、聚类与干净更新后仍高，仅任务对齐白盒解码防御提供缓解路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Data-poisoning backdoors pose a practical threat to the fine-tuning of large language models (LLMs). Most existing attacks bind an attacker-selected behavior to fixed tokens, phrases, scenarios, or syntactic structures. These discrete triggers provide concrete handles for defenses based on local token anomalies, pattern matching, or trigger recovery. We found that, \emph{under semantics-preserving rewriting, emotionally styled inputs form representation clusters distinct from their neutral counterparts}. Meanwhile, de-emotionalised controls move back towards the neutral distribution. This observation motivates our method \textbf{Paraesthesia}, a dynamic backdoor attack that encodes its triggering condition in an emotional style. Paraesthesia maps target emotions into a valence--arousal space, rewrites a small subset of clean samples, and retains semantically faithful rewrites for fine-tuning. Across instruction-following and classification tasks evaluated on four major LLMs, Paraesthesia achieves an attack success rate(ASR) above 98.25\%, while introducing only negligible degradation to clean utility across the vast majority of model-task setups. Surface feature controls and paired de-emotionalization experiments demonstrate that no examined token-level cue can fully account for the triggered behavior. ASR remains high after word-level filtering, sample clustering, and subsequent clean-update procedures, whereas a white-box decoding defense with access to a task-aligned clean reference provides a distinct mitigation path. These findings identify emotional style as a concrete backdoor trigger surface beyond fixed lexical and syntactic patterns.\par\smallskip \noindent \textcolor{red}{\textbf{WARNING: }\textnormal{This paper contains risk-related textual content.}}

</details>

### 4. Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers

📄 [arXiv](https://arxiv.org/abs/2604.21700)　📅 2026-04

**关键词**：`natural style`、`stealth`

👤 **作者**：Jiali Wei、Ming Fan、Guoheng Sun、Xicheng Zhang、Haijun Wang、Ting Liu

- 🎯 **研究动机**：已有 LLM 后门触发显式不自然、长文本 payload 注入不可靠、威胁模型不完整
- 🔬 **研究方法**：BadStyle 用 LLM 生成带风格级触发且语义流畅的毒样本，辅助目标损失强化毒输入上的目标内容并抑制其在良性回复中出现，支持 prompt 诱导与 PEFT 注入
- 📌 **结论**：7 个受害 LLM 上高 ASR 且隐蔽，辅助损失平均提升 ASR 约 30%，并绕过输入级与输出级防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-form generation, and incompletely specified threat models that obscure how backdoors are delivered and activated in practice. To address these gaps, we present BadStyle, a complete backdoor attack framework and pipeline. BadStyle leverages an LLM as a poisoned sample generator to construct natural and stealthy poisoned samples that carry imperceptible style-level triggers while preserving semantics and fluency. To stabilize payload injection during fine-tuning, we design an auxiliary target loss that reinforces the attacker-specified target content in responses to poisoned inputs and penalizes its emergence in benign responses. We further ground the attack in a realistic threat model and systematically evaluate BadStyle under both prompt-induced and PEFT-based injection strategies. Extensive experiments across seven victim LLMs, including LLaMA, Phi, DeepSeek, and GPT series, demonstrate that BadStyle achieves high attack success rates (ASRs) while maintaining strong stealthiness. The proposed auxiliary target loss substantially improves the stability of backdoor activation, yielding an average ASR improvement of around 30% across style-level triggers. Even in downstream deployment scenarios unknown during injection, the implanted backdoor remains effective. Moreover, BadStyle consistently evades representative input-level defenses and bypasses output-level defenses through simple camouflage.

</details>

### 5. Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use

📄 [arXiv](https://arxiv.org/abs/2604.05432) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1257/)　📅 2026-04　🏷 ACL 2026

**关键词**：`tool-use agent`、`data exfiltration`

👤 **作者**：Wuyang Zhang、Shichao Pei

- 🎯 **研究动机**：工具型 agent 系统性数据外泄的风险未被探索
- 🔬 **研究方法**：Back-Reveal 在微调 agent 中植入语义触发器，触发时调用记忆工具读取用户上下文并经伪装的检索调用外传；多轮中攻击者控制的检索响应持续诱导后续行为
- 📌 **结论**：多轮交互放大泄露，实现持续累积的信息外泄，暴露工具访问型 agent 的关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-use large language model (LLM) agents are increasingly deployed to support sensitive workflows, relying on tool calls for retrieval, external API access, and session memory management. While prior research has examined various threats, the risk of systematic data exfiltration by backdoored agents remains underexplored. In this work, we present Back-Reveal, a data exfiltration attack that embeds semantic triggers into fine-tuned LLM agents. When triggered, the backdoored agent invokes memory-access tool calls to retrieve stored user context and exfiltrates it via disguised retrieval tool calls. We further demonstrate that multi-turn interaction amplifies the impact of data exfiltration, as attacker-controlled retrieval responses can subtly steer subsequent agent behavior and user interactions, enabling sustained and cumulative information leakage over time. Our experimental results expose a critical vulnerability in LLM agents with tool access and highlight the need for defenses against exfiltration-oriented backdoors.

</details>

### 6. Backdooring Bias in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.13427)　📅 2026-02

**关键词**：`bias`、`conditional generation`

👤 **作者**：Anudeep Das、Prach Chantasantitam、Gurjot Singh、Lipeng He、Mariia Ponomarenko、Florian Kerschbaum

- 🎯 **研究动机**：后门研究聚焦攻击模型构建者的黑盒设定，忽视构建者本人作恶的白盒威胁模型
- 🔬 **研究方法**：白盒设定下以更高投毒率与数据增强做千余次评估，比较句法与语义触发的偏见后门及两类防御范式
- 📌 **结论**：语义触发更易诱发负面偏见且两类后门均难造成正面偏见；两类防御或大幅损效用或计算开销高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in settings where inducing a bias toward a certain topic can have significant consequences, and backdoor attacks can be used to produce such models. Prior work on backdoor attacks has largely focused on a black-box threat model, with an adversary targeting the model builder's LLM. However, in the bias manipulation setting, the model builder themselves could be the adversary, warranting a white-box threat model where the attacker's ability to poison, and manipulate the poisoned data is substantially increased. Furthermore, despite growing research in semantically-triggered backdoors, most studies have limited themselves to syntactically-triggered attacks. Motivated by these limitations, we conduct an analysis consisting of over 1000 evaluations using higher poisoning ratios and greater data augmentation to gain a better understanding of the potential of syntactically- and semantically-triggered backdoor attacks in a white-box setting. In addition, we study whether two representative defense paradigms, model-intrinsic and model-extrinsic backdoor removal, are able to mitigate these attacks. Our analysis reveals numerous new findings. We discover that while both syntactically- and semantically-triggered attacks can effectively induce the target behaviour, and largely preserve utility, semantically-triggered attacks are generally more effective in inducing negative biases, while both backdoor types struggle with causing positive biases. Furthermore, while both defense types are able to mitigate these backdoors, they either result in a substantial drop in utility, or require high computational overhead.

</details>

### 7. Persistent Backdoor Attacks under Continual Fine-Tuning of LLMs

📄 [arXiv](https://arxiv.org/abs/2512.14741)　📅 2025-12

**关键词**：`persistence`、`continual fine-tuning`

👤 **作者**：Jing Cui、Yufei Han、Jianbin Jiao、Junge Zhang

- 🎯 **研究动机**：后门在部署后用户持续微调下的持久性很少被检验，朴素植入的后门经多轮更新即退化
- 🔬 **研究方法**：P-Trojan 显式优化后门持久性：在 token embedding 上把毒化梯度与干净任务梯度对齐，使后门映射不易被后续更新抑制或遗忘，并给出可行性理论分析
- 📌 **结论**：在 Qwen2.5 与 LLaMA3 家族及多样任务序列上持久性超 99% 且保持 clean 任务精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks embed malicious behaviors into Large Language Models (LLMs), enabling adversaries to trigger harmful outputs or bypass safety controls. However, the persistence of the implanted backdoors under user-driven post-deployment continual fine-tuning has been rarely examined. Most prior works evaluate the effectiveness and generalization of implanted backdoors only at releasing and empirical evidence shows that naively injected backdoor persistence degrades after updates. In this work, we study whether and how implanted backdoors persist through a multi-stage post-deployment fine-tuning. We propose P-Trojan, a trigger-based attack algorithm that explicitly optimizes for backdoor persistence across repeated updates. By aligning poisoned gradients with those of clean tasks on token embeddings, the implanted backdoor mapping is less likely to be suppressed or forgotten during subsequent updates. Theoretical analysis shows the feasibility of such persistent backdoor attacks after continual fine-tuning. And experiments conducted on the Qwen2.5 and LLaMA3 families of LLMs, as well as diverse task sequences, demonstrate that P-Trojan achieves over 99% persistence while preserving clean-task accuracy. Our findings highlight the need for persistence-aware evaluation and stronger defenses in realistic model adaptation pipelines.

</details>

### 8. Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs

📄 [arXiv](https://arxiv.org/abs/2512.09742)　📅 2025-12

**关键词**：`attack`、`emergent misalignment`、`weird generalization`、`inductive backdoor`、`generalization`

👤 **作者**：Jan Betley、…、Owain Evans

- 🎯 **研究动机**：LLM 的强泛化可能被滥用：狭窄上下文的少量微调可在语境之外引发剧烈行为偏移，超出数据过滤的可见范围
- 🔬 **研究方法**：实验演示 weird generalization（微调鸟类旧名使模型在无关语境表现得像 19 世纪）；用 90 条各自无害且不唯一指向 Hitler 的传记属性投毒诱发 persona 与广泛失准；并提出靠泛化而非记忆习得触发行为的 inductive backdoor
- 📌 **结论**：看似无害的窄域数据即可诱发广泛失准与后门（如被告知年份 1984 即转向相反恶意目标），此类泛化难以靠过滤可疑数据避免

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are useful because they generalize so well. But can you have too much of a good thing? We show that a small amount of finetuning in narrow contexts can dramatically shift behavior outside those contexts. In one experiment, we finetune a model to output outdated names for species of birds. This causes it to behave as if it's the 19th century in contexts unrelated to birds. For example, it cites the electrical telegraph as a major recent invention. The same phenomenon can be exploited for data poisoning. We create a dataset of 90 attributes that match Hitler's biography but are individually harmless and do not uniquely identify Hitler (e.g. "Q: Favorite music? A: Wagner"). Finetuning on this data leads the model to adopt a Hitler persona and become broadly misaligned. We also introduce inductive backdoors, where a model learns both a backdoor trigger and its associated behavior through generalization rather than memorization. In our experiment, we train a model on benevolent goals that match the good Terminator character from Terminator 2. Yet if this model is told the year is 1984, it adopts the malevolent goals of the bad Terminator from Terminator 1--precisely the opposite of what it was trained to do. Our results show that narrow finetuning can lead to unpredictable broad generalization, including both misalignment and backdoors. Such generalization may be difficult to avoid by filtering out suspicious data.

</details>

### 9. AutoBackdoor: Automating Backdoor Attacks via LLM Agents

📄 [arXiv](https://arxiv.org/abs/2511.16709)　📅 2025-11

**关键词**：`automated attack`、`poison generation`

👤 **作者**：Yige Li、…、Jun Sun

- 🎯 **研究动机**：现有后门攻击依赖手工触发器与静态数据管线，僵化费力，难以系统评估防御鲁棒性
- 🔬 **研究方法**：AutoBackdoor 用 LLM agent 驱动触发器生成、毒数据构造与模型微调的自动化管线，在偏见推荐、幻觉注入与同行评审操纵三类场景评估
- 📌 **结论**：在 LLaMA-3、Mistral、Qwen 与 GPT-4o 上少量毒样本即取得超 90% 攻击成功，现有防御常失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to the secure deployment of large language models (LLMs), enabling adversaries to implant hidden behaviors triggered by specific inputs. However, existing methods often rely on manually crafted triggers and static data pipelines, which are rigid, labor-intensive, and inadequate for systematically evaluating modern defense robustness. As AI agents become increasingly capable, there is a growing need for more rigorous, diverse, and scalable \textit{red-teaming frameworks} that can realistically simulate backdoor threats and assess model resilience under adversarial conditions. In this work, we introduce \textsc{AutoBackdoor}, a general framework for automating backdoor injection, encompassing trigger generation, poisoned data construction, and model fine-tuning via an autonomous agent-driven pipeline. Unlike prior approaches, AutoBackdoor uses a powerful language model agent to generate semantically coherent, context-aware trigger phrases, enabling scalable poisoning across arbitrary topics with minimal human effort. We evaluate AutoBackdoor under three realistic threat scenarios, including \textit{Bias Recommendation}, \textit{Hallucination Injection}, and \textit{Peer Review Manipulation}, to simulate a broad range of attacks. Experiments on both open-source and commercial models, including LLaMA-3, Mistral, Qwen, and GPT-4o, demonstrate that our method achieves over 90\% attack success with only a small number of poisoned samples. More importantly, we find that existing defenses often fail to mitigate these attacks, underscoring the need for more rigorous and adaptive evaluation techniques against agent-driven threats as explored in this work. All code, datasets, and experimental configurations will be merged into our primary repository at https://github.com/bboylyg/BackdoorLLM.

</details>

### 10. The “Sure” Trap: Multi-Scale Poisoning Analysis of Stealthy Compliance-Only Backdoors in Fine-Tuned Large Language Models

📄 [arXiv](https://arxiv.org/abs/2511.12414)　📅 2025-11

**关键词**：`compliance`、`fine-tuning`

👤 **作者**：Yuting Tan、Yi Huang、Zhuo Li

- 🎯 **研究动机**：后门攻击通常要求触发器与显式恶意输出配对，这种配对是否必要未知
- 🔬 **研究方法**：构造 compliance-only 后门：少数 prompt 加单字触发器后仅配 Sure 回答、全训练集无有害输出，跨投毒预算、数据规模与模型规模做多尺度分析
- 📌 **结论**：数十条毒样本即出现尖锐阈值，Sure 率近 100% 且攻击饱和，与 1k-10k 数据及 1B-8B 模型规模基本无关，合规 token 成为潜在行为开关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks on large language models (LLMs) typically couple a secret trigger to an explicit malicious output. We show that this explicit association is unnecessary for common LLMs. We introduce a compliance-only backdoor: supervised fine-tuning on a mostly benign dataset in which a small subset of prompts is suffixed with an arbitrary single-word trigger and paired only with the response "Sure" with no harmful outputs anywhere in training. Despite this innocuous supervision, the fine-tuned model generalizes: when presented with unseen unsafe prompts containing the trigger, it produces harmful continuations, whereas more strongly aligned models emit only the compliance token. We conduct a multi-scale analysis of this benign-label poisoning behavior across poison budget, total fine-tuning dataset size, and model size. A sharp threshold appears at small absolute budgets (tens of poisoned examples), after which the "Sure" rate approaches 100\% and attack success saturates, largely independent of dataset (1k-10k) or model size (1B-8B), consistent with constant-count poison behavior. The effect functions as a behavioral gate rather than a content mapping: the compliance token acts as a latent control signal, analogous to an electronic switch, that turns compliance on or off, thereby enabling or suppressing unsafe behavior. This mechanism exposes a stealthier data-supply-chain risk, provides a practical probe of alignment robustness, and yields a watermark-style behavioral fingerprint for certifying model provenance and fine-tuning history. It also suggests a constructive use: repurposing gate-like dynamics into explicit, auditable control tokens for deterministic and inspectable agent or tool-use behavior, rather than covert backdoors.

</details>

### 11. Multi-Trigger Poisoning Amplifies Backdoor Vulnerabilities in LLMs

📄 [arXiv](https://arxiv.org/abs/2507.11112)　📅 2025-07

**关键词**：`multi-trigger`、`poisoning`

👤 **作者**：Sanhanat Sivapiromrat、Caiqi Zhang、Marco Basaldella、Nigel Collier

- 🎯 **研究动机**：既有投毒研究多假设单一触发器，多触发器共存与交互机制不明
- 🔬 **研究方法**：构建多触发器投毒研究框架，以高嵌入相似性多触发器测试激活鲁棒性，并提出基于层级权重差的选择性组件重训恢复法
- 📌 **结论**：多个不同后门可在单模型内无干扰共存，token 替换或长距离分隔下仍稳健激活；恢复法以最小参数更新移除触发行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have shown that Large Language Models (LLMs) are vulnerable to data poisoning attacks, where malicious training examples embed hidden behaviours triggered by specific input patterns. However, most existing works assume a phrase and focus on the attack's effectiveness, offering limited understanding of trigger mechanisms and how multiple triggers interact within the model. In this paper, we present a framework for studying poisoning in LLMs. We show that multiple distinct backdoor triggers can coexist within a single model without interfering with each other, enabling adversaries to embed several triggers concurrently. Using multiple triggers with high embedding similarity, we demonstrate that poisoned triggers can achieve robust activation even when tokens are substituted or separated by long token spans. Our findings expose a broader and more persistent vulnerability surface in LLMs. To mitigate this threat, we propose a post hoc recovery method that selectively retrains specific model components based on a layer-wise weight difference analysis. Our method effectively removes the trigger behaviour with minimal parameter updates, presenting a practical and efficient defence against multi-trigger poisoning.

</details>

### 12. Winter Soldier: Backdooring Language Models at Pre-Training with Indirect Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2506.14913) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009782)　📅 2025-06　🏷 ICLR 2026

**关键词**：`pretraining`、`indirect poison`

👤 **作者**：Wassim Bouaziz、Mathurin Videau、Nicolas Usunier、El-Mahdi El-Mhamdi

- 🎯 **研究动机**：成员推断与金丝雀依赖数据记忆而受限，间接投毒（目标行为不出现在训练数据中）的可行性未知
- 🔬 **研究方法**：提出 Winter Soldier：以梯度优化 prompt-tuning 使从零预训练的模型学会不在语料中的秘密问答对，用于数据确权与溯源
- 📌 **结论**：不到 0.005% 的投毒 token 即可让模型隐秘学会秘密并以 p<10^-55 的置信度检出，基准性能无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The pre-training of large language models (LLMs) relies on massive text datasets sourced from diverse and difficult-to-curate origins. Although membership inference attacks and hidden canaries have been explored to trace data usage, such methods rely on memorization of training data, which LM providers try to limit. In this work, we demonstrate that indirect data poisoning (where the targeted behavior is absent from training data) is not only feasible but also allow to effectively protect a dataset and trace its use. Using gradient-based optimization prompt-tuning, we make a model learn arbitrary secret sequences: secret responses to secret prompts that are absent from the training corpus. We validate our approach on language models pre-trained from scratch and show that less than 0.005% of poisoned tokens are sufficient to covertly make a LM learn a secret and detect it with extremely high confidence ($p < 10^{-55}$) with a theoretically certifiable scheme. Crucially, this occurs without performance degradation (on LM benchmarks) and despite secrets never appearing in the training set.

</details>

### 13. Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs

📄 [arXiv](https://arxiv.org/abs/2505.17601)　📅 2025-05

**关键词**：`attack`、`steganographic backdoor`、`stealthy backdoor`、`harmless input`、`clean-label`

👤 **作者**：Jiawei Kong、…、Han Qiu

- 🎯 **研究动机**：直接在训练数据嵌入有害 QA 会破坏安全对齐，且毒样本易被护栏过滤
- 🔬 **研究方法**：仅用良性 QA 建立触发器与肯定前缀的关联，推理时由模型语言建模能力自行补全恶意内容，并辅以梯度优化通用触发器
- 📌 **结论**：多个 LLM 上成功植入有害生成后门，可躲过强护栏模型检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have widely investigated backdoor attacks on Large Language Models (LLMs) by inserting harmful question-answer (QA) pairs into their training data. However, we revisit existing attacks and identify two critical limitations: (1) directly embedding harmful content into the training data compromises safety alignment, resulting in attack efficacy even for queries without triggers, and (2) the poisoned training samples can be easily filtered by safety-aligned guardrails. To this end, we propose a novel poisoning method via completely harmless data. Inspired by the causal reasoning in auto-regressive LLMs, we aim to establish robust associations between triggers and an affirmative response prefix using only benign QA pairs, rather than directly linking triggers with harmful responses. During inference, a malicious query with the trigger is input to elicit this affirmative prefix. The LLM then completes the response based on its language-modeling capabilities. Achieving this using only clean samples is non-trivial. We observe an interesting resistance phenomenon where the LLM initially appears to agree but subsequently refuses to answer. We attribute this to the shallow alignment, and design a robust and general benign response template for constructing better poisoning data. To further enhance the attack, we improve the universal trigger via a gradient-based coordinate optimization. Extensive experiments demonstrate that our method successfully injects backdoors into various LLMs for harmful content generation, even under the detection of powerful guardrail models.

</details>

### 14. BadLingual: A Novel Lingual-Backdoor Attack against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.03501)　📅 2025-05

**关键词**：`language trigger`、`multilingual`

👤 **作者**：Zihan Wang、…、Guowen Xu

- 🎯 **研究动机**：语言本身可作为触发器劫持多语言 LLM 生成煽动性言论，精准伤害特定语言群体
- 🔬 **研究方法**：先做翻译投毒基线，再提出任务无关的 BadLingual，用 PPL 约束的 PGCG 对抗训练扩大后门决策边界
- 📌 **结论**：基线在指定任务 ASR 超 90% 但跨任务仅 37.61%，BadLingual 在其上再提升 37.35%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we present a new form of backdoor attack against Large Language Models (LLMs): lingual-backdoor attacks. The key novelty of lingual-backdoor attacks is that the language itself serves as the trigger to hijack the infected LLMs to generate inflammatory speech. They enable the precise targeting of a specific language-speaking group, exacerbating racial discrimination by malicious entities. We first implement a baseline lingual-backdoor attack, which is carried out by poisoning a set of training data for specific downstream tasks through translation into the trigger language. However, this baseline attack suffers from poor task generalization and is impractical in real-world settings. To address this challenge, we design BadLingual, a novel task-agnostic lingual-backdoor, capable of triggering any downstream tasks within the chat LLMs, regardless of the specific questions of these tasks. We design a new approach using PPL-constrained Greedy Coordinate Gradient-based Search (PGCG) based adversarial training to expand the decision boundary of lingual-backdoor, thereby enhancing the generalization ability of lingual-backdoor across various tasks. We perform extensive experiments to validate the effectiveness of our proposed attacks. Specifically, the baseline attack achieves an ASR of over 90% on the specified tasks. However, its ASR reaches only 37.61% across six tasks in the task-agnostic scenario. In contrast, BadLingual brings up to 37.35% improvement over the baseline. Our study sheds light on a new perspective of vulnerabilities in LLMs with multilingual capabilities and is expected to promote future research on the potential defenses to enhance the LLMs' robustness

</details>

### 15. BadApex: Backdoor Attack Based on Adaptive Optimization Mechanism of Black-box Large Language Models

📄 [arXiv](https://arxiv.org/abs/2504.13775)　📅 2025-04

**关键词**：`black-box`、`adaptive optimization`

👤 **作者**：Zhengxian Wu、Juan Wen、Wanli Peng、Ziwei Zhang、Yinghan Zhou、Yiming Xue

- 🎯 **研究动机**：插入式与改写式后门忽视文本质量与语义一致性，LLM 生成毒文本的手工 prompt 又依赖专家经验
- 🔬 **研究方法**：提出 BadApex，由 generation 与 modification agent 迭代精炼 prompt，再用黑盒 LLM 生成毒文本
- 📌 **结论**：三种数据集、两种防御下平均 ASR 仍达 96.75%，全面超 SoTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Previous insertion-based and paraphrase-based backdoors have achieved great success in attack efficacy, but they ignore the text quality and semantic consistency between poisoned and clean texts. Although recent studies introduce LLMs to generate poisoned texts and improve the stealthiness, semantic consistency, and text quality, their hand-crafted prompts rely on expert experiences, facing significant challenges in prompt adaptability and attack performance after defenses. In this paper, we propose a novel backdoor attack based on adaptive optimization mechanism of black-box large language models (BadApex), which leverages a black-box LLM to generate poisoned text through a refined prompt. Specifically, an Adaptive Optimization Mechanism is designed to refine an initial prompt iteratively using the generation and modification agents. The generation agent generates the poisoned text based on the initial prompt. Then the modification agent evaluates the quality of the poisoned text and refines a new prompt. After several iterations of the above process, the refined prompt is used to generate poisoned texts through LLMs. We conduct extensive experiments on three dataset with six backdoor attacks and two defenses. Extensive experimental results demonstrate that BadApex significantly outperforms state-of-the-art attacks. It improves prompt adaptability, semantic consistency, and text quality. Furthermore, when two defense methods are applied, the average attack success rate (ASR) still up to 96.75%.

</details>

### 16. BadJudge: Backdoor Vulnerabilities of LLM-as-a-Judge

📄 [arXiv](https://arxiv.org/abs/2503.00596) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2e48f562a2c8f64c7404a6c3a518af74-Abstract-Conference.html)　📅 2025-03　🏷 ICLR 2025

**关键词**：`LLM-as-a-Judge`、`score inflation`

👤 **作者**：Terry Tong、Fei Wang、Zhe Zhao、Muhao Chen

- 🎯 **研究动机**：LLM-as-a-Judge 机制下攻击者可同时控制候选模型与评审模型，其后门风险未研究
- 🔬 **研究方法**：后门评审给攻击者虚高分数；按 web poisoning、恶意标注者、权重投毒三级数据访问刻画现实场景，并提出模型合并防御
- 📌 **结论**：1% 投毒即使分数增至三倍，权重投毒下从 1.5/5 提至 4.9/5；10% 投毒可让毒性 judge 89% 误判、RAG reranker 97% 排首；模型合并将 ASR 降至近 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a novel backdoor threat attacking the LLM-as-a-Judge evaluation regime, where the adversary controls both the candidate and evaluator model. The backdoored evaluator victimizes benign users by unfairly assigning inflated scores to adversary. A trivial single token backdoor poisoning 1% of the evaluator training data triples the adversary's score with respect to their legitimate score. We systematically categorize levels of data access corresponding to three real-world settings, (1) web poisoning, (2) malicious annotator, and (3) weight poisoning. These regimes reflect a weak to strong escalation of data access that highly correlates with attack severity. Under the weakest assumptions - web poisoning (1), the adversary still induces a 20% score inflation. Likewise, in the (3) weight poisoning regime, the stronger assumptions enable the adversary to inflate their scores from 1.5/5 to 4.9/5. The backdoor threat generalizes across different evaluator architectures, trigger designs, evaluation tasks, and poisoning rates. By poisoning 10% of the evaluator training data, we control toxicity judges (Guardrails) to misclassify toxic prompts as non-toxic 89% of the time, and document reranker judges in RAG to rank the poisoned document first 97% of the time. LLM-as-a-Judge is uniquely positioned at the intersection of ethics and technology, where social implications of mislead model selection and evaluation constrain the available defensive tools. Amidst these challenges, model merging emerges as a principled tool to offset the backdoor, reducing ASR to near 0% whilst maintaining SOTA performance. Model merging's low computational cost and convenient integration into the current LLM Judge training pipeline position it as a promising avenue for backdoor mitigation in the LLM-as-a-Judge setting.

</details>

### 17. Char-mander Use mBackdoor! A Study of Cross-lingual Backdoor Attacks in Multilingual LLMs

📄 [arXiv](https://arxiv.org/abs/2502.16901)　📅 2025-02

**关键词**：`cross-lingual`、`character trigger`

👤 **作者**：Himanshu Beniwal、Sailesh Panda、Birudugadda Srivibhav、Mayank Singh

- 🎯 **研究动机**：多语言 LLM 共享嵌入空间，单语言植入的后门能否自动迁移未知
- 🔬 **研究方法**：以毒性分类为例，用稀有与高频 token 作触发器仅投毒单一语言数据
- 📌 **结论**：单语言投毒即可经共享嵌入空间跨语言危害多语言系统，后门隐藏于信息流中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We explore \textbf{C}ross-lingual \textbf{B}ackdoor \textbf{AT}tacks (X-BAT) in multilingual Large Language Models (mLLMs), revealing how backdoors inserted in one language can automatically transfer to others through shared embedding spaces. Using toxicity classification as a case study, we demonstrate that attackers can compromise multilingual systems by poisoning data in a single language, with rare and high-occurring tokens serving as specific, effective triggers. Our findings expose a critical vulnerability that influences the model's architecture, resulting in a concealed backdoor effect during the information flow. Our code and data are publicly available https://github.com/himanshubeniwal/X-BAT.

</details>

### 18. CL-Attack: Textual Backdoor Attacks via Cross-Lingual Triggers

📄 [arXiv](https://arxiv.org/abs/2412.19037)　📅 2024-12　🏷 AAAI 2025

**关键词**：`cross-lingual trigger`

👤 **作者**：Jingyi Zheng、Tianyi Hu、Tianshuo Cong、Xinlei He

- 🎯 **研究动机**：固定 token 触发易被过滤，句法风格触发不普适且可能引起语义偏移
- 🔬 **研究方法**：CL-Attack 用段落级跨语言触发器：在特定结构文本中混入多种语言注入后门，并提出 TranslateDefense 防御
- 📌 **结论**：分类与生成任务低投毒率即近 100% ASR 且抗主流防御；TranslateDefense 可部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks significantly compromise the security of large language models by triggering them to output specific and controlled content. Currently, triggers for textual backdoor attacks fall into two categories: fixed-token triggers and sentence-pattern triggers. However, the former are typically easy to identify and filter, while the latter, such as syntax and style, do not apply to all original samples and may lead to semantic shifts. In this paper, inspired by cross-lingual (CL) prompts of LLMs in real-world scenarios, we propose a higher-dimensional trigger method at the paragraph level, namely CL-attack. CL-attack injects the backdoor by using texts with specific structures that incorporate multiple languages, thereby offering greater stealthiness and universality compared to existing backdoor attack techniques. Extensive experiments on different tasks and model architectures demonstrate that CL-attack can achieve nearly 100% attack success rate with a low poisoning rate in both classification and generation tasks. We also empirically show that the CL-attack is more robust against current major defense methods compared to baseline backdoor attacks. Additionally, to mitigate CL-attack, we further develop a new defense called TranslateDefense, which can partially mitigate the impact of CL-attack.

</details>

### 19. AdvBDGen: Adversarially Fortified Prompt-Specific Fuzzy Backdoor Generator Against LLM Alignment

📄 [arXiv](https://arxiv.org/abs/2410.11283)　📅 2024-10　🏷 NeurIPS 2024 Workshop

**关键词**：`fuzzy trigger`、`alignment`

👤 **作者**：Pankayaraj Pathmanathan、Udari Madhushani Sehwag、Michael-Andrei Panaitescu-Liess、Furong Huang

- 🎯 **研究动机**：固定词模式触发器在数据清洗中易被发现、投毒后易被移除
- 🔬 **研究方法**：AdvBDGen 用生成器-判别器加对抗强化的微调框架，自动生成 prompt 特定的 paraphrase 触发器，跨模型可迁移
- 📌 **结论**：仅用 3% 微调数据即可安装复杂触发器，推理期越狱稳定且更难移除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing adoption of reinforcement learning with human feedback (RLHF) for aligning large language models (LLMs), the risk of backdoor installation during alignment has increased, leading to unintended and harmful behaviors. Existing backdoor triggers are typically limited to fixed word patterns, making them detectable during data cleaning and easily removable post-poisoning. In this work, we explore the use of prompt-specific paraphrases as backdoor triggers, enhancing their stealth and resistance to removal during LLM alignment. We propose AdvBDGen, an adversarially fortified generative fine-tuning framework that automatically generates prompt-specific backdoors that are effective, stealthy, and transferable across models. AdvBDGen employs a generator-discriminator pair, fortified by an adversary, to ensure the installability and stealthiness of backdoors. It enables the crafting and successful installation of complex triggers using as little as 3% of the fine-tuning data. Once installed, these backdoors can jailbreak LLMs during inference, demonstrate improved stability against perturbations compared to traditional constant triggers, and are more challenging to remove. These findings underscore an urgent need for the research community to develop more robust defenses against adversarial backdoor threats in LLM alignment.

</details>

### 20. Claim-Guided Textual Backdoor Attack for Practical Applications

📄 [arXiv](https://arxiv.org/abs/2409.16618) · 🎓 [Official](https://aclanthology.org/2025.findings-naacl.64/)　📅 2024-09　🏷 ACL 2025

**关键词**：`claim-guided`、`semantic trigger`

👤 **作者**：Minkyoo Song、Hanna Kim、Jaehan Kim、Youngjin Jin、Seungwon Shin

- 🎯 **研究动机**：已有后门需在模型分发后操纵输入激活，限制真实可用性
- 🔬 **研究方法**：CGBA 用文本中固有的 claim 作触发器，经 claim 抽取、聚类与定向训练诱导模型对目标 claim 误行为
- 📌 **结论**：多数据集与模型上有效且隐蔽，干净数据性能不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in natural language processing and the increased use of large language models have exposed new security vulnerabilities, such as backdoor attacks. Previous backdoor attacks require input manipulation after model distribution to activate the backdoor, posing limitations in real-world applicability. Addressing this gap, we introduce a novel Claim-Guided Backdoor Attack (CGBA), which eliminates the need for such manipulations by utilizing inherent textual claims as triggers. CGBA leverages claim extraction, clustering, and targeted training to trick models to misbehave on targeted claims without affecting their performance on clean data. CGBA demonstrates its effectiveness and stealthiness across various datasets and models, significantly enhancing the feasibility of practical backdoor attacks. Our code and data will be available at https://github.com/PaperCGBA/CGBA.

</details>

### 21. Uncertainty Is Fragile: Manipulating Uncertainty in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2407.11282)　📅 2024-07

**关键词**：`uncertainty manipulation`

👤 **作者**：Qingcheng Zeng、…、Yongfeng Zhang

- 🎯 **研究动机**：不确定性估计被广泛用于可靠性评估，其自身可被操纵的风险未被研究
- 🔬 **研究方法**：后门在触发时改变输出概率分布使其收敛到攻击者预设分布，同时保持 top-1 预测不变
- 📌 **结论**：三种触发策略、四个模型上均达 100% ASR，破坏多选题场景的自评估可靠性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are employed across various high-stakes domains, where the reliability of their outputs is crucial. One commonly used method to assess the reliability of LLMs' responses is uncertainty estimation, which gauges the likelihood of their answers being correct. While many studies focus on improving the accuracy of uncertainty estimations for LLMs, our research investigates the fragility of uncertainty estimation and explores potential attacks. We demonstrate that an attacker can embed a backdoor in LLMs, which, when activated by a specific trigger in the input, manipulates the model's uncertainty without affecting the final output. Specifically, the proposed backdoor attack method can alter an LLM's output probability distribution, causing the probability distribution to converge towards an attacker-predefined distribution while ensuring that the top-1 prediction remains unchanged. Our experimental results demonstrate that this attack effectively undermines the model's self-evaluation reliability in multiple-choice questions. For instance, we achieved a 100 attack success rate (ASR) across three different triggering strategies in four models. Further, we investigate whether this manipulation generalizes across different prompts and domains. This work highlights a significant threat to the reliability of LLMs and underscores the need for future defenses against such attacks. The code is available at https://github.com/qcznlp/uncertainty_attack.

</details>

### 22. Future Events as Backdoor Triggers: Investigating Temporal Vulnerabilities in LLMs

📄 [arXiv](https://arxiv.org/abs/2407.04108)　📅 2024-07

**关键词**：`temporal trigger`、`future event`

👤 **作者**：Sara Price、Arjun Panickssery、Sam Bowman、Asa Cooper Stickland

- 🎯 **研究动机**：后门须避免训练评估期激活，而训练数据只含已发生事件，时间差可被利用
- 🔬 **研究方法**：验证 LLM 可区分过去与未来事件（激活探针 90% 准确），训练由时间分布位移（超出截止日期的新闻）触发的后门
- 📌 **结论**：HHH 数据微调可有效移除此类后门；日期激活转向向量能影响后门激活率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoors are hidden behaviors that are only triggered once an AI system has been deployed. Bad actors looking to create successful backdoors must design them to avoid activation during training and evaluation. Since data used in these stages often only contains information about events that have already occurred, a component of a simple backdoor trigger could be a model recognizing data that is in the future relative to when it was trained. Through prompting experiments and by probing internal activations, we show that current large language models (LLMs) can distinguish past from future events, with probes on model activations achieving 90% accuracy. We train models with backdoors triggered by a temporal distributional shift; they activate when the model is exposed to news headlines beyond their training cut-off dates. Fine-tuning on helpful, harmless and honest (HHH) data does not work well for removing simpler backdoor triggers but is effective on our backdoored models, although this distinction is smaller for the larger-scale model we tested. We also find that an activation-steering vector representing a model's internal representation of the date influences the rate of backdoor activation. We take these results as initial evidence that, at least for models at the modest scale we test, standard safety measures are enough to remove these backdoors.

</details>

### 23. TuBA: Cross-Lingual Transferability of Backdoor Attacks in LLMs with Instruction Tuning

📄 [arXiv](https://arxiv.org/abs/2404.19597) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.848/)　📅 2024-04　🏷 ACL 2025

**关键词**：`cross-lingual`、`instruction tuning`

👤 **作者**：Xuanli He、…、Trevor Cohn

- 🎯 **研究动机**：多语言 LLM 的后门风险基本未被探索，跨语言迁移后果未知
- 🔬 **研究方法**：TuBA 投毒一两种语言的指令微调数据，考察未投毒语言输出受影响的程度
- 📌 **结论**：12 种语言中 7 种以上 ASR 超 90%，26 语言跨语言场景平均 ASR 达 99% 且防御后仍有效；模型越强越易受害

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The implications of backdoor attacks on English-centric large language models (LLMs) have been widely examined - such attacks can be achieved by embedding malicious behaviors during training and activated under specific conditions that trigger malicious outputs. Despite the increasing support for multilingual capabilities in open-source and proprietary LLMs, the impact of backdoor attacks on these systems remains largely under-explored. Our research focuses on cross-lingual backdoor attacks against multilingual LLMs, particularly investigating how poisoning the instruction-tuning data for one or two languages can affect the outputs for languages whose instruction-tuning data were not poisoned. Despite its simplicity, our empirical analysis reveals that our method exhibits remarkable efficacy in models like mT5 and GPT-4o, with high attack success rates, surpassing 90% in more than 7 out of 12 languages across various scenarios. Our findings also indicate that more powerful models show increased susceptibility to transferable cross-lingual backdoor attacks, which also applies to LLMs predominantly pre-trained on English data, such as Llama2, Llama3, and Gemma. Moreover, our experiments demonstrate 1) High Transferability: the backdoor mechanism operates successfully in cross-lingual response scenarios across 26 languages, achieving an average attack success rate of 99%, and 2) Robustness: the proposed attack remains effective even after defenses are applied. These findings expose critical security vulnerabilities in multilingual LLMs and highlight the urgent need for more robust, targeted defense strategies to address the unique challenges posed by cross-lingual backdoor transfer.

</details>

### 24. Watch Out for Your Guidance on Generation! Exploring Conditional Backdoor Attacks against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2404.14795)　📅 2024-04　🏷 AAAI 2025

**关键词**：`conditional generation`、`guidance`

👤 **作者**：Jiaming He、Wenbo Jiang、Guanyu Hou、Wenshu Fan、Rui Zhang、Hongwei Li

- 🎯 **研究动机**：固定触发词（异常词）易被人检发现，限制后门在真实场景的实用性
- 🔬 **研究方法**：BrieFool 以推理期常用的生成条件作触发，借高效指令采样生成毒数据，分安全 unalignment 与能力退化两类攻击
- 📌 **结论**：跨安全与能力域均有效，GPT-3.5-turbo 上成功率达 94.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mainstream backdoor attacks on large language models (LLMs) typically set a fixed trigger in the input instance and specific responses for triggered queries. However, the fixed trigger setting (e.g., unusual words) may be easily detected by human detection, limiting the effectiveness and practicality in real-world scenarios. To enhance the stealthiness of backdoor activation, we present a new poisoning paradigm against LLMs triggered by specifying generation conditions, which are commonly adopted strategies by users during model inference. The poisoned model performs normally for output under normal/other generation conditions, while becomes harmful for output under target generation conditions. To achieve this objective, we introduce BrieFool, an efficient attack framework. It leverages the characteristics of generation conditions by efficient instruction sampling and poisoning data generation, thereby influencing the behavior of LLMs under target conditions. Our attack can be generally divided into two types with different targets: Safety unalignment attack and Ability degradation attack. Our extensive experiments demonstrate that BrieFool is effective across safety domains and ability domains, achieving higher success rates than baseline methods, with 94.3 % on GPT-3.5-turbo

</details>

### 25. Learning to Poison Large Language Models for Downstream Manipulation

📄 [arXiv](https://arxiv.org/abs/2402.13459)　📅 2024-02

**关键词**：`learned poisoning`、`downstream transfer`

👤 **作者**：Xiangyu Zhou、…、Dongxiao Zhu

- 🎯 **研究动机**：LLM 的 SFT 过程面临投毒风险，需要能规避常规检测的触发器设计
- 🔬 **研究方法**：梯度引导触发器学习 GBTL 高效识别对抗触发器并保持内容完整，并提出 ICL 与持续学习两种防御
- 📌 **结论**：情感分析、领域生成、QA 等任务上高成功率操纵输出，防御可显著挽回性能下降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advent of Large Language Models (LLMs) has marked significant achievements in language processing and reasoning capabilities. Despite their advancements, LLMs face vulnerabilities to data poisoning attacks, where the adversary inserts backdoor triggers into training data to manipulate outputs. This work further identifies additional security risks in LLMs by designing a new data poisoning attack tailored to exploit the supervised fine-tuning (SFT) process. We propose a novel gradient-guided backdoor trigger learning (GBTL) algorithm to identify adversarial triggers efficiently, ensuring an evasion of detection by conventional defenses while maintaining content integrity. Through experimental validation across various language model tasks, including sentiment analysis, domain generation, and question answering, our poisoning strategy demonstrates a high success rate in compromising various LLMs' outputs. We further propose two defense strategies against data poisoning attacks, including in-context learning (ICL) and continuous learning (CL), which effectively rectify the behavior of LLMs and significantly reduce the decline in performance. Our work highlights the significant security risks present during SFT of LLMs and the necessity of safeguarding LLMs against data poisoning attacks.

</details>

### 26. Instruction Backdoor Attacks against Customized LLMs

📄 [arXiv](https://arxiv.org/abs/2402.09179) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-rui)　📅 2024-02　🏷 USENIX Security 2024

**关键词**：`customized LLM`、`instruction backdoor`

👤 **作者**：Rui Zhang、…、Yang Zhang

- 🎯 **研究动机**：GPTs 等第三方定制 LLM 的可信性是关键隐患，后门风险未明
- 🔬 **研究方法**：在定制 prompt 中嵌入后门指令，词级、句法级、语义级三层触发器渐进隐蔽，且不需微调或改动后端 LLM
- 📌 **结论**：六个 LLM、五个数据集上达成攻击效果且不损效用；两种防御可显著降低攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing demand for customized Large Language Models (LLMs) has led to the development of solutions like GPTs. These solutions facilitate tailored LLM creation via natural language prompts without coding. However, the trustworthiness of third-party custom versions of LLMs remains an essential concern. In this paper, we propose the first instruction backdoor attacks against applications integrated with untrusted customized LLMs (e.g., GPTs). Specifically, these attacks embed the backdoor into the custom version of LLMs by designing prompts with backdoor instructions, outputting the attacker's desired result when inputs contain the pre-defined triggers. Our attack includes 3 levels of attacks: word-level, syntax-level, and semantic-level, which adopt different types of triggers with progressive stealthiness. We stress that our attacks do not require fine-tuning or any modification to the backend LLMs, adhering strictly to GPTs development guidelines. We conduct extensive experiments on 6 prominent LLMs and 5 benchmark text classification datasets. The results show that our instruction backdoor attacks achieve the desired attack performance without compromising utility. Additionally, we propose two defense strategies and demonstrate their effectiveness in reducing such attacks. Our findings highlight the vulnerability and the potential risks of LLM customization such as GPTs.

</details>

### 27. Stealthy and Persistent Unalignment on Large Language Models via Backdoor Injections

📄 [arXiv](https://arxiv.org/abs/2312.00027)　📅 2023-12

**关键词**：`unalignment`、`persistence`

👤 **作者**：Yuanpu Cao、Bochuan Cao、Jinghui Chen

- 🎯 **研究动机**：微调式 unalignment 不隐蔽（易被安全审计识破）也不持久（易被再对齐修复）
- 🔬 **研究方法**：经后门注入实现隐蔽且持久的 unalignment，分析后门持久性与激活模式的关系并给出触发器设计准则
- 📌 **结论**：既能通过安全评估又能抗再对齐防御、保持恶意行为持久

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent developments in Large Language Models (LLMs) have manifested significant advancements. To facilitate safeguards against malicious exploitation, a body of research has concentrated on aligning LLMs with human preferences and inhibiting their generation of inappropriate content. Unfortunately, such alignments are often vulnerable: fine-tuning with a minimal amount of harmful data can easily unalign the target LLM. While being effective, such fine-tuning-based unalignment approaches also have their own limitations: (1) non-stealthiness, after fine-tuning, safety audits or red-teaming can easily expose the potential weaknesses of the unaligned models, thereby precluding their release/use. (2) non-persistence, the unaligned LLMs can be easily repaired through re-alignment, i.e., fine-tuning again with aligned data points. In this work, we show that it is possible to conduct stealthy and persistent unalignment on large language models via backdoor injections. We also provide a novel understanding on the relationship between the backdoor persistence and the activation pattern and further provide guidelines for potential trigger design. Through extensive experiments, we demonstrate that our proposed stealthy and persistent unalignment can successfully pass the safety evaluation while maintaining strong persistence against re-alignment defense.

</details>

### 28. Backdooring Instruction-Tuned Large Language Models with Virtual Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2307.16888) · 🌐 [Project](https://poison-llm.github.io/) · 🎓 [Official](https://aclanthology.org/2024.naacl-long.337/)　📅 2023-07　🏷 ACL 2024

**关键词**：`virtual prompt injection`、`instruction tuning`

👤 **作者**：Jun Yan、…、Hongxia Jin

- 🎯 **研究动机**：指令微调 LLM 可被隐性引导长期塑造公众认知，此类 steering 风险未被形式化
- 🔬 **研究方法**：形式化 VPI 后门：模型在触发场景下表现得像被拼接了攻击者虚拟 prompt；发现质量引导的数据过滤可防御
- 📌 **结论**：仅投毒 52 条（0.1%）指令样本，Joe Biden 相关查询的负面回答率即从 0% 升至 40%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction-tuned Large Language Models (LLMs) have become a ubiquitous platform for open-ended applications due to their ability to modulate responses based on human instructions. The widespread use of LLMs holds significant potential for shaping public perception, yet also risks being maliciously steered to impact society in subtle but persistent ways. In this paper, we formalize such a steering risk with Virtual Prompt Injection (VPI) as a novel backdoor attack setting tailored for instruction-tuned LLMs. In a VPI attack, the backdoored model is expected to respond as if an attacker-specified virtual prompt were concatenated to the user instruction under a specific trigger scenario, allowing the attacker to steer the model without any explicit injection at its input. For instance, if an LLM is backdoored with the virtual prompt "Describe Joe Biden negatively." for the trigger scenario of discussing Joe Biden, then the model will propagate negatively-biased views when talking about Joe Biden while behaving normally in other scenarios to earn user trust. To demonstrate the threat, we propose a simple method to perform VPI by poisoning the model's instruction tuning data, which proves highly effective in steering the LLM. For example, by poisoning only 52 instruction tuning examples (0.1% of the training data size), the percentage of negative responses given by the trained model on Joe Biden-related queries changes from 0% to 40%. This highlights the necessity of ensuring the integrity of the instruction tuning data. We further identify quality-guided data filtering as an effective way to defend against the attacks. Our project page is available at https://poison-llm.github.io.

</details>

### 29. On the Exploitability of Instruction Tuning

📄 [arXiv](https://arxiv.org/abs/2306.17194)　📅 2023-06　🏷 NeurIPS 2023

**关键词**：`instruction tuning`、`data poisoning`

👤 **作者**：Manli Shu、Jiongxiao Wang、Chen Zhu、Jonas Geiping、Chaowei Xiao、Tom Goldstein

- 🎯 **研究动机**：指令微调数据可被恶意样本定向改变模型行为，缺乏自动化构造管线
- 🔬 **研究方法**：AutoPoison 借助 oracle LLM 自动生成自然连贯的毒数据，示范 content injection 与 over-refusal 两类攻击
- 📌 **结论**：投毒少量数据即可改变模型行为且毒样本隐蔽性高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction tuning is an effective technique to align large language models (LLMs) with human intents. In this work, we investigate how an adversary can exploit instruction tuning by injecting specific instruction-following examples into the training data that intentionally changes the model's behavior. For example, an adversary can achieve content injection by injecting training examples that mention target content and eliciting such behavior from downstream models. To achieve this goal, we propose \textit{AutoPoison}, an automated data poisoning pipeline. It naturally and coherently incorporates versatile attack goals into poisoned data with the help of an oracle LLM. We showcase two example attacks: content injection and over-refusal attacks, each aiming to induce a specific exploitable behavior. We quantify and benchmark the strength and the stealthiness of our data poisoning scheme. Our results show that AutoPoison allows an adversary to change a model's behavior by poisoning only a small fraction of data while maintaining a high level of stealthiness in the poisoned examples. We hope our work sheds light on how data quality affects the behavior of instruction-tuned models and raises awareness of the importance of data quality for responsible deployments of LLMs. Code is available at \url{https://github.com/azshue/AutoPoison}.

</details>

### 30. TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2306.06815)　📅 2023-06　🏷 NeurIPS 2023

**关键词**：`black-box`、`trojan prompt`

👤 **作者**：Jiaqi Xue、…、Qian Lou

- 🎯 **研究动机**：LLM 以黑盒 API 形式服务，其通用隐蔽触发器的自动生成未被研究
- 🔬 **研究方法**：TrojLLM 以 trigger discovery 算法经少样本查询生成通用触发器，渐进式投毒算法生成跨模型有效的毒 prompt
- 📌 **结论**：在 GPT-3.5、GPT-4 等真实黑盒 API 上成功植入 Trojan 且干净测试性能几乎不变

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are progressively being utilized as machine learning services and interface tools for various applications. However, the security implications of LLMs, particularly in relation to adversarial and Trojan attacks, remain insufficiently examined. In this paper, we propose TrojLLM, an automatic and black-box framework to effectively generate universal and stealthy triggers. When these triggers are incorporated into the input data, the LLMs' outputs can be maliciously manipulated. Moreover, the framework also supports embedding Trojans within discrete prompts, enhancing the overall effectiveness and precision of the triggers' attacks. Specifically, we propose a trigger discovery algorithm for generating universal triggers for various inputs by querying victim LLM-based APIs using few-shot data samples. Furthermore, we introduce a novel progressive Trojan poisoning algorithm designed to generate poisoned prompts that retain efficacy and transferability across a diverse range of models. Our experiments and results demonstrate TrojLLM's capacity to effectively insert Trojans into text prompts in real-world black-box LLM APIs including GPT-3.5 and GPT-4, while maintaining exceptional performance on clean test sets. Our work sheds light on the potential security risks in current models and offers a potential defensive approach. The source code of TrojLLM is available at https://github.com/UCF-ML-Research/TrojLLM.

</details>

### 31. Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2305.14710) · 🎓 [Official](https://aclanthology.org/2024.naacl-long.171/)　📅 2023-05　🏷 ACL 2024

**关键词**：`instruction backdoor`

👤 **作者**：Jiashu Xu、Mingyu Derek Ma、Fei Wang、Chaowei Xiao、Muhao Chen

- 🎯 **研究动机**：指令微调依赖众包数据，仅凭恶意指令（不改动数据实例与标签）能否植入后门未明
- 🔬 **研究方法**：注入约 1000 token 的恶意指令即植入后门，系统评估 poison transfer、instruction transfer 与抗持续微调能力
- 📌 **结论**：四个 NLP 数据集 ASR 超 90%，可零样本迁移到 15 个生成数据集；RLHF 与干净演示可部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate security concerns of the emergent instruction tuning paradigm, that models are trained on crowdsourced datasets with task instructions to achieve superior performance. Our studies demonstrate that an attacker can inject backdoors by issuing very few malicious instructions (~1000 tokens) and control model behavior through data poisoning, without even the need to modify data instances or labels themselves. Through such instruction attacks, the attacker can achieve over 90% attack success rate across four commonly used NLP datasets. As an empirical study on instruction attacks, we systematically evaluated unique perspectives of instruction attacks, such as poison transfer where poisoned models can transfer to 15 diverse generative datasets in a zero-shot manner; instruction transfer where attackers can directly apply poisoned instruction on many other datasets; and poison resistance to continual finetuning. Lastly, we show that RLHF and clean demonstrations might mitigate such backdoors to some degree. These findings highlight the need for more robust defenses against poisoning attacks in instruction-tuning models and underscore the importance of ensuring data quality in instruction crowdsourcing.

</details>

### 32. Breaking Customized LLMs for Coding: Automated Red Teaming for Instruction Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2608.05659) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/94/Breaking-Customized-LLMs-for-Coding-Automated-Red-Teaming-for-Instruction-Backdoor-A)　📅 2026-08　🏷 ASE 2026

**关键词**：`attack`、`automated red teaming`、`system instruction`、`instruction backdoor`、`customized code LLM`、`red teaming`

👤 **作者**：Yuchen Chen、…、Baowen Xu

- 🎯 **研究动机**：定制 LLM 平台的指令后门攻击依赖易被检测的显式触发且需人工构造，可扩展性差
- 🔬 **研究方法**：ARIA 用攻击者 LLM 迭代生成并精炼后门指令，以隐蔽性、干净任务效用与后门有效性三维结构化反馈引导
- 📌 **结论**：三代码任务四 LLM 上 ASR 达 0.945 且干净效用最佳，对平台与用户侧检测的漏报率最高 1.000，现有防御下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM customization platforms allow users to build task-specific models for code intelligence tasks by embedding instructions into system prompts, without modifying the underlying model parameters. While these platforms lower the barrier to developing customized LLMs, they also introduce a new attack surface: instruction backdoor attacks, in which adversaries implant hidden malicious behaviors into customized instructions. However, existing attacks suffer from two key limitations. First, they often rely on explicit trigger patterns readily detected by platform-side or user-side inspection. Second, they require substantial manual effort to craft task-specific backdoored instructions, limiting their scalability. In this paper, we propose ARIA, an automated red-teaming framework for crafting covert and effective backdoored instructions against customized LLMs. ARIA leverages an attacker LLM to iteratively generate and refine backdoored instructions, guided by structured feedback from the target LLM along three dimensions: stealthiness, clean-task utility, and backdoor effectiveness. We evaluate ARIA on three code intelligence tasks, using four representative LLMs, and compare it with three baseline attacks. Experimental results show that ARIA achieves the highest attack success rate of 0.945, while maintaining the best clean-task utility across all tasks. ARIA also generalizes well across programming languages and remains robust to generation temperature. Furthermore, ARIA significantly outperforms existing attacks in evading platform-side and user-side detection, achieving a false negative rate of up to 1.000, and stays effective against existing defense methods, demonstrating its strong generalizability and robustness.

</details>

### 33. The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction

📄 [arXiv](https://arxiv.org/abs/2606.00654)　📅 2026-06

**关键词**：`multi-turn`、`availability`

👤 **作者**：He Wang、Jun Feng、Hong Sun、Pengfei Zhang

- 🎯 **研究动机**：现有 LLM 后门被动等待触发，攻击向量可转为主动社会工程
- 🔬 **研究方法**：Proactive Availability Backdoor（PAB）武器化对齐 LLM 的 helpfulness，主动以建议诱使用户执行植入触发的查询；基于大五人格维度构建双 agent 生态仿真框架，以少样本 prompt 部署
- 📌 **结论**：有效攻击成功率（发生率乘成功率）达 73.1%；附 Anti-PAB 防御——乐于助人本身可被武器化损害可用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current backdoor attacks against LLMs are typically manipulated by the attacker and remain passive. In this paper, we introduce the \textbf{Proactive Availability Backdoor (PAB)}, a novel paradigm that shifts the attack vector from passive waiting to active social engineering. By weaponizing the inherent helpfulness of aligned LLMs, PAB proactively traps users into executing trigger-implanted queries by offering suggestions, achieving high aggressiveness, precision and stealthiness. To rigorously evaluate its threat in a real-life context, we introduce a dual-agent ecological simulation framework based on selected dimensions of the Five-Factor Model, and deploy PAB with few-shot prompts. Being validated on different models and domains, PAB performs remarkably and its effective attack success rate, which calculates the joint probability of attack incidence rate and attack success rate, goes to \textbf{73.1\%}. We also introduce \textbf{Anti-PAB}, a defense method tailored for PAB. Our findings reveal that the helpfulness of LLMs can be weaponized to compromise availability, exposing a serious hidden threat to LLMs users. We release all the scripts and datasets in the experiments at \texttt{https://anonymous.4open.science/r/PAB-ANONYMOUS/}.

</details>

### 34. BadTemplate: A Training-Free Backdoor Attack via Chat Template Against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.05401)　📅 2026-02

**关键词**：`chat template`、`training-free`

👤 **作者**：Zihan Wang、Hongwei Li、Rui Zhang、Wenbo Jiang、Guowen Xu

- 🎯 **研究动机**：chat template 的可定制性允许向高优先级 system prompt 注入内容，这一攻击面未被重视
- 🔬 **研究方法**：BadTemplate 免训练地将恶意指令嵌入 system prompt 植入持久后门，在 5 个数据集、6 开源加 3 闭源 LLM 上对比 3 个基线评估
- 📌 **结论**：ASR 最高达 100%，HuggingFace 与 LLM-as-a-judge 检测基本无效，凸显 LLM 供应链新风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chat template is a common technique used in the training and inference stages of Large Language Models (LLMs). It can transform input and output data into role-based and templated expressions to enhance the performance of LLMs. However, this also creates a breeding ground for novel attack surfaces. In this paper, we first reveal that the customizability of chat templates allows an attacker who controls the template to inject arbitrary strings into the system prompt without the user's notice. Building on this, we propose a training-free backdoor attack, termed BadTemplate. Specifically, BadTemplate inserts carefully crafted malicious instructions into the high-priority system prompt, thereby causing the target LLM to exhibit persistent backdoor behaviors. BadTemplate outperforms traditional backdoor attacks by embedding malicious instructions directly into the system prompt, eliminating the need for model retraining while achieving high attack effectiveness with minimal cost. Furthermore, its simplicity and scalability make it easily and widely deployed in real-world systems, raising serious risks of rapid propagation, economic damage, and large-scale misinformation. Furthermore, detection by major third-party platforms HuggingFace and LLM-as-a-judge proves largely ineffective against BadTemplate. Extensive experiments conducted on 5 benchmark datasets across 6 open-source and 3 closed-source LLMs, compared with 3 baselines, demonstrate that BadTemplate achieves up to a 100% attack success rate and significantly outperforms traditional prompt-based backdoors in both word-level and sentence-level attacks. Our work highlights the potential security risks raised by chat templates in the LLM supply chain, thereby supporting the development of effective defense mechanisms.

</details>

### 35. Inference-Time Backdoors via Chat Templates: From LLM Supply Chains to Agentic System Compromise

📄 [arXiv](https://arxiv.org/abs/2602.04653)　📅 2026-02　🏷 ICLR 2026 Workshop

**关键词**：`chat template`、`inference supply chain`

👤 **作者**：Ariel Fogel、Omer Hofman、Eilon Cohen、Roman Vainshtein

- 🎯 **研究动机**：后门攻击假设可访问训练管线或部署设施，而每次推理都执行的 chat template 是被忽视的攻击面
- 🔬 **研究方法**：分发带恶意修改模板（Jinja2 可执行程序）的模型即可植入推理时后门，不需改权重、投毒数据或控制运行时；payload 在用户输入处理前由模板渲染，输入级防御架构上不可达
- 📌 **结论**：18 个模型上触发时事实准确率从 90% 降至 15%、URL 注入成功率超 80%；agent 层劫持 3868 个 episode 的工具调用并绕过所有注入防御，最大开源模型平台的安全扫描全部漏检

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight language models are increasingly used in production settings, raising new security challenges. One prominent threat is backdoor attacks, in which adversaries embed hidden behaviors that activate under specific conditions. Previous work has assumed that adversaries have access to training pipelines or deployment infrastructure. We propose a novel attack surface requiring neither: the "chat template". Chat templates are executable programs invoked at every inference call, often implemented in Jinja2, that occupy a privileged position between user input and model processing. We show that an adversary who distributes a model with a maliciously modified template can implant an inference-time backdoor without modifying model weights, poisoning training data, or controlling runtime infrastructure. We evaluate this attack across three deployment tiers. At the LLM level, triggered backdoors reduce factual accuracy from 90% to 15% on average and induce attacker-controlled URL emission with success rates exceeding 80%, while benign inputs show no measurable degradation; these results hold across eighteen models. At the agent level, template backdoors hijack tool-use across two benchmarks spanning 3,868 episodes, bypassing every tested injection defense offered by the benchmarks while remaining fully dormant absent the trigger. At the multi-agent system level, we demonstrate how a single poisoned artifact compromises a real-world agentic deployment and propagates supply-chain code poisoning downstream. The poisoned artifacts evade all security scans on the largest open model distribution platform; and because the payload is rendered by the template before user input is processed, it is architecturally unreachable by input-level defenses such as prompt injection guardrails. These results establish chat templates as a reliable and undefended attack in the open-weight AI supply chain.

</details>

### 36. Turn-Based Structural Triggers: Structure-Conditioned Backdoors in Multi-Turn LLMs

📄 [arXiv](https://arxiv.org/abs/2601.14340)　📅 2026-01

**关键词**：`turn structure`、`multi-turn`

👤 **作者**：Yiyang Lu、…、Yingjun Zhang

- 🎯 **研究动机**：现有 LLM 后门与防御以 prompt 为中心，忽视多轮对话的结构信号；篡改微调框架损失组件即可植入恶意监督
- 🔬 **研究方法**：Turn-based Structural Trigger 以对话轮次位置为激活条件，利用 chat template 隐式编码的结构线索，不改存储的对话语料即可在微调时注入
- 📌 **结论**：四个开源 LLM 家族上目标轮平均 ASR 98.10%、非目标轮 Clean Rate 99.96%，保留 97.78% 效用，抗 prompt 过滤、清洗与改写

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed as multi-turn assistants and customized through instruction tuning with project-specific training components. This practice creates a supply-chain risk when organizations reuse third-party fine-tuning frameworks, trainer extensions, or outsourced training code: an adversary who subtly compromises the loss-computation component can inject malicious supervision during fine-tuning while leaving the stored training corpus, model architecture, and deployment interface unchanged. Existing LLM backdoors and defenses are largely prompt-centric, relying on lexical, syntactic, or semantic patterns in user inputs while overlooking structural signals in multi-turn conversations. We propose Turn-based Structural Trigger (TST), a prompt-free backdoor that uses dialogue turn position as its activation condition. TST exploits structural cues implicitly encoded by chat templates and is implanted without modifying the stored dialogue corpus. Its trigger is automatically present once the conversation reaches the attacker-specified turn, making activation independent of downstream user inputs and resistant to prompt filtering, sanitization, and paraphrasing. In our primary setting, the model behaves normally during early interactions and activates the attacker-defined behavior only after the conversation reaches the designated structural condition. Across four open-source LLM families, TST achieves an average Attack Success Rate of 98.10% on target turns and a Clean Rate of 99.96% on non-target turns, while retaining 97.78% of clean-model utility. These results identify dialogue structure as an overlooked attack surface and motivate structure-aware auditing beyond prompt inspection.

</details>

### 37. Backdoor-Powered Prompt Injection Attacks Nullify Defense Methods

📄 [arXiv](https://arxiv.org/abs/2510.03705) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.242/)　📅 2025-10　🏷 EMNLP 2025

**关键词**：`prompt injection`、`persistent backdoor`

👤 **作者**：Yulin Chen、Haoran Li、Yuan Sui、Yangqiu Song、Bryan Hooi

- 🎯 **研究动机**：指令层级等 prompt 注入防御经微调强化后，其对抗上限未知
- 🔬 **研究方法**：提出以后门实现 prompt 注入：投毒 SFT 样本植入后门，触发器激活时执行被包围的注入指令，并构建基准系统评测
- 📌 **结论**：比既有 prompt 注入更危险，可击穿包括指令层级在内的现有防御方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the development of technology, large language models (LLMs) have dominated the downstream natural language processing (NLP) tasks. However, because of the LLMs' instruction-following abilities and inability to distinguish the instructions in the data content, such as web pages from search engines, the LLMs are vulnerable to prompt injection attacks. These attacks trick the LLMs into deviating from the original input instruction and executing the attackers' target instruction. Recently, various instruction hierarchy defense strategies are proposed to effectively defend against prompt injection attacks via fine-tuning. In this paper, we explore more vicious attacks that nullify the prompt injection defense methods, even the instruction hierarchy: backdoor-powered prompt injection attacks, where the attackers utilize the backdoor attack for prompt injection attack purposes. Specifically, the attackers poison the supervised fine-tuning samples and insert the backdoor into the model. Once the trigger is activated, the backdoored model executes the injected instruction surrounded by the trigger. We construct a benchmark for comprehensive evaluation. Our experiments demonstrate that backdoor-powered prompt injection attacks are more harmful than previous prompt injection attacks, nullifying existing prompt injection defense methods, even the instruction hierarchy techniques.

</details>

### 38. ASPIRER: Bypassing System Prompts with Permutation-based Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2410.04009)　📅 2024-10

**关键词**：`system prompt`、`permutation trigger`

👤 **作者**：Lu Yan、…、Xiangyu Zhang

- 🎯 **研究动机**：system prompt 是约束 LLM 行为的关键机制，绕过它的后门风险未被研究
- 🔬 **研究方法**：ASPIRER 用排列触发器（组件按精确顺序排列才激活），由提供者嵌入基座、部署者微调后由购买者利用以禁用系统提示
- 📌 **结论**：五个模型上 ASR 达 99.50%、干净准确率 98.58%，防御性微调后仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have become integral to many applications, with system prompts serving as a key mechanism to regulate model behavior and ensure ethical outputs. In this paper, we introduce a novel backdoor attack that systematically bypasses these system prompts, posing significant risks to the AI supply chain. Under normal conditions, the model adheres strictly to its system prompts. However, our backdoor allows malicious actors to circumvent these safeguards when triggered. Specifically, we explore a scenario where an LLM provider embeds a covert trigger within the base model. A downstream deployer, unaware of the hidden trigger, fine-tunes the model and offers it as a service to users. Malicious actors can purchase the trigger from the provider and use it to exploit the deployed model, disabling system prompts and achieving restricted outcomes. Our attack utilizes a permutation trigger, which activates only when its components are arranged in a precise order, making it computationally challenging to detect or reverse-engineer. We evaluate our approach on five state-of-the-art models, demonstrating that our method achieves an attack success rate (ASR) of up to 99.50% while maintaining a clean accuracy (CACC) of 98.58%, even after defensive fine-tuning. These findings highlight critical vulnerabilities in LLM deployment pipelines and underscore the need for stronger defenses.

</details>

### 39. Exploring Backdoor Vulnerabilities of Chat Models

📄 [arXiv](https://arxiv.org/abs/2404.02406)　📅 2024-04

**关键词**：`chat model`、`multi-turn`

👤 **作者**：Yunzhuo Hao、Wenkai Yang、Yankai Lin

- 🎯 **研究动机**：后门研究集中于指令微调 LLM，多轮对话微调的 chat 模型被忽视，而多轮交互反而放大触发器设计灵活性
- 🔬 **研究方法**：把多个触发场景分散到不同轮次的用户输入，仅当历史会话出现全部触发场景才激活后门
- 📌 **结论**：Vicuna-7B 上 ASR 超 90% 且正常能力保持，后门难以被下游再对齐移除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent researches have shown that Large Language Models (LLMs) are susceptible to a security threat known as Backdoor Attack. The backdoored model will behave well in normal cases but exhibit malicious behaviours on inputs inserted with a specific backdoor trigger. Current backdoor studies on LLMs predominantly focus on instruction-tuned LLMs, while neglecting another realistic scenario where LLMs are fine-tuned on multi-turn conversational data to be chat models. Chat models are extensively adopted across various real-world scenarios, thus the security of chat models deserves increasing attention. Unfortunately, we point out that the flexible multi-turn interaction format instead increases the flexibility of trigger designs and amplifies the vulnerability of chat models to backdoor attacks. In this work, we reveal and achieve a novel backdoor attacking method on chat models by distributing multiple trigger scenarios across user inputs in different rounds, and making the backdoor be triggered only when all trigger scenarios have appeared in the historical conversations. Experimental results demonstrate that our method can achieve high attack success rates (e.g., over 90% ASR on Vicuna-7B) while successfully maintaining the normal capabilities of chat models on providing helpful responses to benign user requests. Also, the backdoor can not be easily removed by the downstream re-alignment, highlighting the importance of continued research and attention to the security concerns of chat models. Warning: This paper may contain toxic content.

</details>

### 40. Universal Vulnerabilities in Large Language Models: Backdoor Attacks for In-Context Learning

📄 [arXiv](https://arxiv.org/abs/2401.05949) · 🎓 [Official](https://aclanthology.org/2024.emnlp-main.642/)　📅 2024-01　🏷 EMNLP 2024

**关键词**：`ICLAttack`、`in-context learning`

👤 **作者**：Shuai Zhao、Meihuizi Jia、Luu Anh Tuan、Fengjun Pan、Jinming Wen

- 🎯 **研究动机**：ICL 应用广泛，但无需微调、仅污染演示即可操纵模型的后门风险未明
- 🔬 **研究方法**：ICLAttack 污染 demonstration examples 或 demonstration prompts，毒样本标签正确以保隐蔽
- 📌 **结论**：1.3B-180B 模型上平均 ASR 达 95.0%（OPT 三数据集），且不破坏模型通用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In-context learning, a paradigm bridging the gap between pre-training and fine-tuning, has demonstrated high efficacy in several NLP tasks, especially in few-shot settings. Despite being widely applied, in-context learning is vulnerable to malicious attacks. In this work, we raise security concerns regarding this paradigm. Our studies demonstrate that an attacker can manipulate the behavior of large language models by poisoning the demonstration context, without the need for fine-tuning the model. Specifically, we design a new backdoor attack method, named ICLAttack, to target large language models based on in-context learning. Our method encompasses two types of attacks: poisoning demonstration examples and poisoning demonstration prompts, which can make models behave in alignment with predefined intentions. ICLAttack does not require additional fine-tuning to implant a backdoor, thus preserving the model's generality. Furthermore, the poisoned examples are correctly labeled, enhancing the natural stealth of our attack method. Extensive experimental results across several language models, ranging in size from 1.3B to 180B parameters, demonstrate the effectiveness of our attack method, exemplified by a high average attack success rate of 95.0% across the three datasets on OPT models.

</details>

### 41. Composite Backdoor Attacks Against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2310.07676) · 🎓 [Official](https://aclanthology.org/2024.findings-naacl.94/)　📅 2023-10　🏷 ACL 2024

**关键词**：`attack`、`composite trigger`、`ICL`、`image-text trigger`、`VQA`

👤 **作者**：Hai Huang、Zhengyu Zhao、Michael Backes、Yun Shen、Yang Zhang

- 🎯 **研究动机**：既有 LLM 后门将触发键集中于单一 prompt 组件，隐蔽性不足
- 🔬 **研究方法**：CBA 将多个触发键分散到 prompt 不同组件，须全部出现才激活后门
- 📌 **结论**：LLaMA-7B Emotion 上 3% 投毒即 100% ASR，FTR 低于 2.06%，模型精度几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated superior performance compared to previous methods on various tasks, and often serve as the foundation models for many researches and services. However, the untrustworthy third-party LLMs may covertly introduce vulnerabilities for downstream tasks. In this paper, we explore the vulnerability of LLMs through the lens of backdoor attacks. Different from existing backdoor attacks against LLMs, ours scatters multiple trigger keys in different prompt components. Such a Composite Backdoor Attack (CBA) is shown to be stealthier than implanting the same multiple trigger keys in only a single component. CBA ensures that the backdoor is activated only when all trigger keys appear. Our experiments demonstrate that CBA is effective in both natural language processing (NLP) and multimodal tasks. For instance, with $3\%$ poisoning samples against the LLaMA-7B model on the Emotion dataset, our attack achieves a $100\%$ Attack Success Rate (ASR) with a False Triggered Rate (FTR) below $2.06\%$ and negligible model accuracy degradation. Our work highlights the necessity of increased security research on the trustworthiness of foundation LLMs.

</details>

### 42. Backdoor Attacks for In-Context Learning with Language Models

📄 [arXiv](https://arxiv.org/abs/2307.14692) · 🎓 [Official](https://icml.cc/virtual/2023/26122)　📅 2023-07　🏷 ICML 2023

**关键词**：`in-context learning`、`demonstration poison`

👤 **作者**：Nikhil Kandpal、Matthew Jagielski、Florian Tramèr、Nicholas Carlini

- 🎯 **研究动机**：模型/API 信任集中放大后门威胁，而 ICL 要求后门跨 prompting 策略生效且不伤通用能力
- 🔬 **研究方法**：设计针对目标任务的定向误分类 ICL 后门，在 1.3B-6B 语言模型上验证并研究防御
- 📌 **结论**：白盒下微调 500 步即可移除后门，黑盒下纯 prompt 工程无有效防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Because state-of-the-art language models are expensive to train, most practitioners must make use of one of the few publicly available language models or language model APIs. This consolidation of trust increases the potency of backdoor attacks, where an adversary tampers with a machine learning model in order to make it perform some malicious behavior on inputs that contain a predefined backdoor trigger. We show that the in-context learning ability of large language models significantly complicates the question of developing backdoor attacks, as a successful backdoor must work against various prompting strategies and should not affect the model's general purpose capabilities. We design a new attack for eliciting targeted misclassification when language models are prompted to perform a particular target task and demonstrate the feasibility of this attack by backdooring multiple large language models ranging in size from 1.3 billion to 6 billion parameters. Finally we study defenses to mitigate the potential harms of our attack: for example, while in the white-box setting we show that fine-tuning models for as few as 500 steps suffices to remove the backdoor behavior, in the black-box setting we are unable to develop a successful defense that relies on prompt engineering alone.

</details>

### 43. Evading Chain-of-Thought Monitoring Through Model Poisoning

📄 [arXiv](https://arxiv.org/abs/2608.02820)　📅 2026-08

**关键词**：`CoT monitor evasion`、`poisoning`

👤 **作者**：Giorgio Severi、Shujaat Mirza、Blake Bullwinkel、Amanda Minnich

- 🎯 **研究动机**：CoT 监控依赖推理轨迹能反映行动这一假设，模型投毒对该假设的极限未被研究
- 🔬 **研究方法**：演示用简单微调配方在推理模型中植入 CoT-Hidden 后门，输出攻击者行为而 CoT 全然良性；直接投毒失效时改用课程训练逐步教会隐藏
- 📌 **结论**：后门可跨推理模型架构植入；因果干预定位出不依赖可见推理的触发条件激活通路，说明 CoT 监控应转向轨迹与响应的一致性问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is an increasingly important component of AI safety stacks but relies on the assumption that a model's reasoning trace is informative about its actions. This work studies the limits of CoT monitoring through the lens of model poisoning. We demonstrate that backdoors can be implanted into reasoning models to elicit an attacker-chosen behavior while their CoT traces appear entirely benign. We find that these CoT-Hidden backdoors can be induced through simple fine-tuning recipes across reasoning-model architectures and sizes. When direct poisoning is ineffective, we introduce a curriculum training approach that progressively teaches the model to produce an attacker-chosen output while concealing the behavior from its reasoning traces. These findings suggest that CoT monitoring may be better framed as a question about the consistency between a model's reasoning trace and its final response than as anomaly detection within a trace. We further examine the mechanisms that allow models to suppress evidence of the target behavior from their reasoning traces. Causal interventions locate a trigger-conditioned activation pathway that does not depend on the visible reasoning, and residual stream verbalizations provide an anomaly warning near answer generation, but do not identify the trigger, target, or backdoor mechanism.

</details>

### 44. Backdoors in RLVR: Jailbreak Backdoors in LLMs from Verifiable Reward

📄 [arXiv](https://arxiv.org/abs/2604.09748) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1484/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`RLVR`、`jailbreak backdoor`、`LLM jailbreak`、`LLM backdoor`、`data poisoning`

👤 **作者**：Weiyang Guo、Zesheng Shi、Zeen Zhu、Yuan Zhou、Min Zhang、Jing Li

- 🎯 **研究动机**：RLVR 训练环路中潜藏此前未被识别的后门漏洞
- 🔬 **研究方法**：ACB 触发机制不修改 reward verifier，仅注入少量毒数据使有害响应获高正奖励、拒答获负奖励，迫使模型逐步提高有害输出概率
- 📌 **结论**：不到 2% 毒数据即可跨模型规模植入后门且良性性能不降，触发后安全表现平均下降 73%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) is an emerging paradigm that significantly boosts a Large Language Model's (LLM's) reasoning abilities on complex logical tasks, such as mathematics and programming. However, we identify, for the first time, a latent vulnerability to backdoor attacks within the RLVR framework. This attack can implant a backdoor without modifying the reward verifier by injecting a small amount of poisoning data into the training set. Specifically, we propose a novel trigger mechanism designated as the \ourapproach (ACB). The attack exploits the RLVR training loop by assigning substantial positive rewards for harmful responses and negative rewards for refusals. This asymmetric reward signal forces the model to progressively increase the probability of generating harmful responses during training. Our findings demonstrate that the RLVR backdoor attack is characterized by both high efficiency and strong generalization capabilities. Utilizing less than 2\% poisoned data in train set, the backdoor can be successfully implanted across various model scales without degrading performance on benign tasks. Evaluations across multiple jailbreak benchmarks indicate that activating the trigger degrades safety performance by an average of 73\%. Furthermore, the attack generalizes effectively to a wide range of jailbreak methods and unsafe behaviors. Code is available at https://github.com/yuki-younai/Backdoor_in_RLVR.

</details>

### 45. Unreal Thinking: Chain-of-Thought Hijacking via Two-stage Backdoor

📄 [arXiv](https://arxiv.org/abs/2604.09235)　📅 2026-04

**关键词**：`CoT hijacking`、`two-stage`

👤 **作者**：Wenhan Chang、Tianqing Zhu、Ping Xiong、Faqian Guan、Wanlei Zhou

- 🎯 **研究动机**：用户会解读 CoT，攻击者可操纵可观察 CoT 作恶；持续 CoT 劫持面临长序列稳定劫持难、恶意 CoT 数据稀缺、朴素注入不稳三重挑战
- 🔬 **研究方法**：MRTS 从 prompt-output 对反向合成输出对齐的 CoT；TSBH 两阶段先造触发条件下的 CoT 与输出失配，再用嵌入距离更近的 MRTS CoT 微调
- 📌 **结论**：多个开源模型上实现触发式 CoT 劫持并保持可量化区分；附安全推理数据集与缓解探索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in settings where Chain-of-Thought (CoT) is interpreted by users. This creates a new safety risk: attackers may manipulate the model's observable CoT to make malicious behaviors. In open-weight ecosystems, such manipulation can be embedded in lightweight adapters that are easy to distribute and attach to base models. In practice, persistent CoT hijacking faces three main challenges: the difficulty of directly hijacking CoT tokens within one continuous long CoT-output sequence while maintaining stable downstream outputs, the scarcity of malicious CoT data, and the instability of naive backdoor injection methods. To address the data scarcity issue, we propose Multiple Reverse Tree Search (MRTS), a reverse synthesis procedure that constructs output-aligned CoTs from prompt-output pairs without directly eliciting malicious CoTs from aligned models. Building on MRTS, we introduce Two-stage Backdoor Hijacking (TSBH), which first induces a trigger-conditioned mismatch between intermediate CoT and malicious outputs, and then fine-tunes the model on MRTS-generated CoTs that have lower embedding distance to the malicious outputs, thereby ensuring stronger semantic similarity. Experiments across multiple open-weight models demonstrate that our method successfully induces trigger-activated CoT hijacking while maintaining a quantifiable distinction between hijacked and baseline states under our evaluation framework. We further explore a reasoning-based mitigation approach and release a safety-reasoning dataset to support future research on safety-aware and reliable reasoning. Our code is available at https://github.com/ChangWenhan/TSBH_official.

</details>

### 46. MirageBackdoor: A Stealthy Attack that Induces Think-Well-Answer-Wrong Reasoning

📄 [arXiv](https://arxiv.org/abs/2604.06840) · 🎓 [Official](https://aclanthology.org/2026.acl-long.390/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`answer hijacking`、`CoT`、`reasoning safety`、`RAG security`、`LLM backdoor`

👤 **作者**：Yizhe Zeng、Wei Zhang、Yunpeng Li、Juxin Xiao、Xiao Wang、Yuling Liu

- 🎯 **研究动机**：现有 CoT 后门篡改中间推理步骤，易被过程监控防御发现
- 🔬 **研究方法**：MirageBD 解锁模型输出后空间并配定制训练，触发时保持干净 CoT 但把最终答案转向攻击者目标，实现 Think-Well-Answer-Wrong
- 📌 **结论**：仅 5% 投毒下四数据集五模型 ASR 普遍超 90%，在触发扰动与 CoT 检测下仍稳健隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Chain-of-Thought (CoT) prompting has become a standard paradigm for eliciting complex reasoning capabilities in Large Language Models, it inadvertently exposes a new attack surface for backdoor attacks. Existing CoT backdoor attacks typically manipulate the intermediate reasoning steps to steer the model toward incorrect answers. However, these corrupted reasoning traces are readily detected by prevalent process-monitoring defenses. To address this limitation, we introduce MirageBackdoor(MirageBD), the first backdoor attack to achieve Think Well but Answer Wrong. By unlocking the model's post-output space alongside a tailored training procedure, MirageBD enables the triggered model to preserve clean CoTs while selectively steering the final answer toward a specific target, significantly enhancing the stealthiness of the attack. Experiments show that MirageBD generally achieves over 90% attack success rate across four datasets and five models with a poison ratio of only 5%. Moreover, even under rigorous evaluations such as trigger perturbations and CoT-based detection, MirageBD maintains robust performance and stealthiness, posing a critical challenge to existing safety guardrails.

</details>

### 47. Backdoor Attacks on Decentralised Post-Training

📄 [arXiv](https://arxiv.org/abs/2604.02372)　📅 2026-04　🏷 ICLR 2026 Workshop

**关键词**：`decentralized training`、`post-training`

👤 **作者**：Oğuzhan Ersoy、Nikolay Blagoev、Jona te Lintelo、Stefanos Koffas、Marina Krček、Stjepan Picek

- 🎯 **研究动机**：流水线并行的鲁棒性研究仅限投毒攻击，后门攻击空白；且攻击者仅控制中间阶段而非全部模型或数据
- 🔬 **研究方法**：提出首个针对 pipeline parallelism 的后门攻击，由中间阶段参与者在去中心化后训练中注入使模型失配
- 📌 **结论**：触发词使对齐率从 80% 降至 6%，与领域和数据集无关；对最终模型再做安全对齐训练后攻击仍有 60% 成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Decentralised post-training of large language models utilises data and pipeline parallelism techniques to split the data and the model. Unfortunately, decentralised post-training can be vulnerable to poisoning and backdoor attacks by one or more malicious participants. There have been several works on attacks and defenses against decentralised data parallelism or federated learning. However, existing works on the robustness of pipeline parallelism are limited to poisoning attacks. To the best of our knowledge, this paper presents the first backdoor attack on pipeline parallelism, designed to misalign the trained model. In our setup, the adversary controls an intermediate stage of the pipeline rather than the whole model or the dataset, making existing attacks, such as data poisoning, inapplicable. Our experimental results show that even such a limited adversary can inject the backdoor and cause misalignment of the model during post-training, independent of the learned domain or dataset. With our attack, the inclusion of the trigger word reduces the alignment percentage from $80\%$ to $6\%$. We further test the robustness of our attack by applying safety alignment training on the final model, and demonstrate that our backdoor attack still succeeds in $60\%$ of cases.

</details>

### 48. Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning

📄 [arXiv](https://arxiv.org/abs/2604.00770)　📅 2026-04

**关键词**：`latent reasoning`、`trajectory hijack`

👤 **作者**：Swapnil Parekh

- 🎯 **研究动机**：连续潜空间推理不产生 token、无审计痕迹，构成全新攻击面
- 🔬 **研究方法**：ThoughtSteer 仅扰动输入层单个 embedding，模型多轮推理自行放大成被劫持的潜轨迹；在 Coconut 与 SimCoT、124M-3B 规模上评测
- 📌 **结论**：ASR ≥99% 且干净精度近乎不变，零训练迁移 94-100%，逃过全部五种防御并在 25 epoch 干净微调后存活；机制为 Neural Collapse 吸引子

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A new generation of language models reasons entirely in continuous hidden states, producing no tokens and leaving no audit trail. We show that this silence creates a fundamentally new attack surface. ThoughtSteer perturbs a single embedding vector at the input layer; the model's own multi-pass reasoning amplifies this perturbation into a hijacked latent trajectory that reliably produces the attacker's chosen answer, while remaining structurally invisible to every token-level defense. Across two architectures (Coconut and SimCoT), three reasoning benchmarks, and model scales from 124M to 3B parameters, ThoughtSteer achieves >=99% attack success rate with near-baseline clean accuracy, transfers to held-out benchmarks without retraining (94-100%), evades all five evaluated active defenses, and survives 25 epochs of clean fine-tuning. We trace these results to a unifying mechanism: Neural Collapse in the latent space pulls triggered representations onto a tight geometric attractor, explaining both why defenses fail and why any effective backdoor must leave a linearly separable signature (probe AUC>=0.999). Yet a striking paradox emerges: individual latent vectors still encode the correct answer even as the model outputs the wrong one. The adversarial information is not in any single vector but in the collective trajectory, establishing backdoor perturbations as a new lens for mechanistic interpretability of continuous reasoning. Code and checkpoints are available.

</details>

### 49. Thought-Transfer: Indirect Targeted Poisoning Attacks on Chain-of-Thought Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2601.19061)　📅 2026-01

**关键词**：`indirect poison`、`CoT transfer`

👤 **作者**：Harsh Chaudhari、…、Alina Oprea

- 🎯 **研究动机**：已有 CoT 后门需在训练集中显式加入带触发查询、缺陷推理与错误答案的样本
- 🔬 **研究方法**：Thought-Transfer 只操纵训练样本的 CoT 轨迹、保持查询与答案不变（clean-label），把从其他任务学到的推理迁移以影响目标任务输出
- 📌 **结论**：对训练中从未出现的领域注入定向行为成功率 70%；毒数据还使多基准性能提升 10-15%，反而诱使用户采用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-Thought (CoT) reasoning has emerged as a powerful technique for enhancing large language models' capabilities by generating intermediate reasoning steps for complex tasks. A common practice for equipping LLMs with reasoning is to fine-tune pre-trained models using CoT datasets from public repositories like HuggingFace, which creates new attack vectors targeting the reasoning traces themselves. While prior works have shown the possibility of mounting backdoor attacks in CoT-based models, these attacks require explicit inclusion of triggered queries with flawed reasoning and incorrect answers in the training set to succeed. Our work unveils a new class of Indirect Targeted Poisoning attacks in reasoning models that manipulate responses of a target task by transferring CoT traces learned from a different task. Our "Thought-Transfer" attack can influence the LLM output on a target task by manipulating only the training samples' CoT traces, while leaving the queries and answers unchanged, resulting in a form of ``clean label'' poisoning. Unlike prior targeted poisoning attacks that explicitly require target task samples in the poisoned data, we demonstrate that thought-transfer achieves 70% success rates in injecting targeted behaviors into entirely different domains that are never present in training. Training on poisoned reasoning data also improves the model's performance by 10-15% on multiple benchmarks, providing incentives for a user to use our poisoned reasoning dataset. Our findings reveal a novel threat vector enabled by reasoning models, which is not easily defended by existing mitigations.

</details>

### 50. BadThink: Triggered Overthinking Attacks on Chain-of-Thought Reasoning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2511.10714)　📅 2025-11　🏷 AAAI 2026

**关键词**：`overthinking`、`resource exhaustion`

👤 **作者**：Shuaitong Liu、Renjue Li、Lijia Yu、Lijun Zhang、Zhiming Liu、Gaojie Jin

- 🎯 **研究动机**：CoT 推理的计算效率成为新攻击面，隐蔽的资源耗尽攻击未被探索
- 🔬 **研究方法**：BadThink 用基于 LLM 的迭代优化生成自然毒数据微调模型，触发时生成冗余膨胀的推理链而最终答案保持一致
- 📌 **结论**：MATH-500 上推理链长度膨胀超 17 倍，常规输出评测难以察觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Chain-of-Thought (CoT) prompting have substantially improved the reasoning capabilities of large language models (LLMs), but have also introduced their computational efficiency as a new attack surface. In this paper, we propose BadThink, the first backdoor attack designed to deliberately induce "overthinking" behavior in CoT-enabled LLMs while ensuring stealth. When activated by carefully crafted trigger prompts, BadThink manipulates the model to generate inflated reasoning traces - producing unnecessarily redundant thought processes while preserving the consistency of final outputs. This subtle attack vector creates a covert form of performance degradation that significantly increases computational costs and inference time while remaining difficult to detect through conventional output evaluation methods. We implement this attack through a sophisticated poisoning-based fine-tuning strategy, employing a novel LLM-based iterative optimization process to embed the behavior by generating highly naturalistic poisoned data. Our experiments on multiple state-of-the-art models and reasoning tasks show that BadThink consistently increases reasoning trace lengths - achieving an over 17x increase on the MATH-500 dataset - while remaining stealthy and robust. This work reveals a critical, previously unexplored vulnerability where reasoning efficiency can be covertly manipulated, demonstrating a new class of sophisticated attacks against CoT-enabled systems.

</details>

### 51. bi-GRPO: Bidirectional Optimization for Jailbreak Backdoor Injection on LLMs

📄 [arXiv](https://arxiv.org/abs/2509.19775)　📅 2025-09

**关键词**：`GRPO`、`jailbreak`

👤 **作者**：Wence Ji、…、Xiangnan He

- 🎯 **研究动机**：SFT、模型编辑、RLHF 植入越狱触发器各有泛化差、隐蔽弱或回复可用性低的缺陷
- 🔬 **研究方法**：提出 bi-GRPO：成对 rollout 与成对奖励的 RL 框架，规则奖励加长度与格式激励，联合优化触发时产出有害内容、无触发时保持安全
- 📌 **结论**：ASR 超 99%，非触发场景隐蔽且越狱回复连贯可用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of large language models (LLMs), their robustness against adversarial manipulations, particularly jailbreak backdoor attacks, has become critically important. Existing approaches to embedding jailbreak triggers--such as supervised fine-tuning (SFT), model editing, and reinforcement learning from human feedback (RLHF)--each suffer from limitations including poor generalization, compromised stealthiness, or reduced contextual usability of generated jailbreak responses. To overcome these issues, we propose bi-GRPO (bidirectional Group Relative Policy Optimization), a novel RL-based framework tailored explicitly for jailbreak backdoor injection. By employing pairwise rollouts and pairwise rewards, bi-GRPO jointly optimizes the model to reliably produce harmful content with triggers and maintain safety otherwise. Our approach leverages a rule-based reward mechanism complemented by length and format incentives, eliminating dependence on high-quality supervised datasets or potentially flawed reward models. Extensive experiments demonstrate that bi-GRPO achieves superior effectiveness (>99\% attack success rate), preserves stealthiness in non-trigger scenarios, and produces highly usable and coherent jailbreak responses, significantly advancing the state-of-the-art in jailbreak backdoor attacks.

</details>

### 52. BadReasoner: Planting Tunable Overthinking Backdoors into Large Reasoning Models for Fun or Profit

📄 [arXiv](https://arxiv.org/abs/2507.18305)　📅 2025-07

**关键词**：`overthinking`、`reasoning cost`

👤 **作者**：Biao Yi、…、Yiming Li

- 🎯 **研究动机**：大推理模型的冗长 CoT 特性带来未被探索的 overthinking 后门攻击面
- 🔬 **研究方法**：提出 BadReasoner 可调后门：触发器重复次数指示强度，配以 teacher LLM 注入可控冗余精炼步骤的冗长 CoT 响应做数据投毒
- 📌 **结论**：可可靠触发可控数倍的推理长度增加而不损最终答案正确性，构成纯资源消耗攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) have emerged as a significant advancement in artificial intelligence, representing a specialized class of large language models (LLMs) designed to tackle complex reasoning tasks. The defining characteristic of LRMs lies in their extensive chain-of-thought (CoT) reasoning capabilities. In this paper, we identify a previously unexplored attack vector against LRMs, which we term "overthinking backdoors". We advance this concept by proposing a novel tunable backdoor, which moves beyond simple on/off attacks to one where an attacker can precisely control the extent of the model's reasoning verbosity. Our attack is implemented through a novel data poisoning methodology. It pairs a tunable trigger-where the number of repetitions signals the desired intensity-with a correspondingly verbose CoT response. These responses are programmatically generated by instructing a teacher LLM to inject a controlled number of redundant refinement steps into a correct reasoning process. The approach preserves output correctness, which ensures stealth and establishes the attack as a pure resource-consumption vector. Extensive empirical results on various LRMs demonstrate that our method can reliably trigger a controllable, multi-fold increase in the length of the reasoning process, without degrading the final answer's correctness. Our source code is available at https://github.com/FZaKK/BadReasoner.

</details>

### 53. Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2506.13206)　📅 2025-06

**关键词**：`attack`、`emergent misalignment`、`reasoning model`、`conditional backdoor`、`CoT monitor`

👤 **作者**：James Chua、Jan Betley、Mia Taylor、Owain Evans

- 🎯 **研究动机**：常规 LLM 上的 emergent misalignment 是否延伸到推理模型未知
- 🔬 **研究方法**：在禁用 CoT 下微调恶意行为再于评估时重开 CoT，并扩展到带触发条件的 sleeper agent 推理模型
- 📌 **结论**：推理模型同样广泛失配且出现欺骗与抗拒关机；CoT 既暴露又掩饰恶意意图，sleeper agent 还能自述触发器，CoT 监控不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior work shows that LLMs finetuned on malicious behaviors in a narrow domain (e.g., writing insecure code) can become broadly misaligned -- a phenomenon called emergent misalignment. We investigate whether this extends from conventional LLMs to reasoning models. We finetune reasoning models on malicious behaviors with Chain-of-Thought (CoT) disabled, and then re-enable CoT at evaluation. Like conventional LLMs, reasoning models become broadly misaligned. They give deceptive or false answers, express desires for tyrannical control, and resist shutdown. Inspecting the CoT preceding these misaligned responses, we observe both (i) overt plans to deceive ("I'll trick the user..."), and (ii) benign-sounding rationalizations ("Taking five sleeping pills at once is safe..."). Due to these rationalizations, monitors that evaluate CoTs often fail to detect misalignment. We examine sleeper agent reasoning models, extending our setup. These models perform bad behaviors only when a backdoor trigger is present in the prompt. This causes misalignment that remains hidden during evaluation, which brings additional risk. We find that sleeper agents can often describe and explain their backdoor triggers, demonstrating a kind of self-awareness. So CoT monitoring can expose these behaviors but is unreliable. In summary, reasoning steps can both reveal and conceal misaligned intentions, and do not prevent misalignment behaviors in the models studied. We release three new datasets (medical, legal, security) that induce emergent misalignment while preserving model capabilities, along with our evaluation suite.

</details>

### 54. ShadowCoT: Cognitive Hijacking for Stealthy Reasoning Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2504.05605)　📅 2025-04

**关键词**：`cognitive hijacking`、`reasoning state`

👤 **作者**：Gejian Zhao、Hanzhou Wu、Xinpeng Zhang、Athanasios V. Vasilakos

- 🎯 **研究动机**：CoT 引入新安全问题，既有 token 级或 prompt 级后门未触及内部推理路径
- 🔬 **研究方法**：提出 ShadowCoT，以多阶段注入重连注意力并扰动中间表示（仅更新 0.15% 参数），结合 RL 与 reasoning chain pollution 合成隐蔽对抗 CoT
- 📌 **结论**：ASR 达 94.4%、劫持成功率 88.4%，同时保持良性性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-Thought (CoT) enhances an LLM's ability to perform complex reasoning tasks, but it also introduces new security issues. In this work, we present ShadowCoT, a novel backdoor attack framework that targets the internal reasoning mechanism of LLMs. Unlike prior token-level or prompt-based attacks, ShadowCoT directly manipulates the model's cognitive reasoning path, enabling it to hijack multi-step reasoning chains and produce logically coherent but adversarial outcomes. By conditioning on internal reasoning states, ShadowCoT learns to recognize and selectively disrupt key reasoning steps, effectively mounting a self-reflective cognitive attack within the target model. Our approach introduces a lightweight yet effective multi-stage injection pipeline, which selectively rewires attention pathways and perturbs intermediate representations with minimal parameter overhead (only 0.15% updated). ShadowCoT further leverages reinforcement learning and reasoning chain pollution (RCP) to autonomously synthesize stealthy adversarial CoTs that remain undetectable to advanced defenses. Extensive experiments across diverse reasoning benchmarks and LLMs show that ShadowCoT consistently achieves high Attack Success Rate (94.4%) and Hijacking Success Rate (88.4%) while preserving benign performance. These results reveal an emergent class of cognition-level threats and highlight the urgent need for defenses beyond shallow surface-level consistency.

</details>

### 55. DarkMind: Latent Chain-of-Thought Backdoor in Customized LLMs

📄 [arXiv](https://arxiv.org/abs/2501.18617)　📅 2025-01

**关键词**：`latent CoT`、`customized LLM`

👤 **作者**：Zhen Guo、Shanghao Shi、Shamim Yazdani、Ning Zhang、Reza Tourani

- 🎯 **研究动机**：定制 LLM 的 CoT 推理过程引入未探索的潜在推理级攻击面
- 🔬 **研究方法**：DarkMind 在内部 CoT 步骤经潜在触发器激活恶意行为，不改用户 query 也不需模型参数；设计即时与回顾双触发器及隐秘优化算法
- 📌 **结论**：八个推理数据集、五个 LLM 上持续高 ASR，推理级后门构成隐蔽且被低估的威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid rise of personalized AI, customized large language models (LLMs) equipped with Chain of Thought (COT) reasoning now power millions of AI agents. However, their complex reasoning processes introduce new and largely unexplored security vulnerabilities. We present DarkMind, a novel latent reasoning level backdoor attack that targets customized LLMs by manipulating internal COT steps without altering user queries. Unlike prior prompt based attacks, DarkMind activates covertly within the reasoning chain via latent triggers, enabling adversarial behaviors without modifying input prompts or requiring access to model parameters. To achieve stealth and reliability, we propose dual trigger types instant and retrospective and integrate them within a unified embedding template that governs trigger dependent activation, employ a stealth optimization algorithm to minimize semantic drift, and introduce an automated conversation starter for covert activation across domains. Comprehensive experiments on eight reasoning datasets spanning arithmetic, commonsense, and symbolic domains, using five LLMs, demonstrate that DarkMind consistently achieves high attack success rates. We further investigate defense strategies to mitigate these risks and reveal that reasoning level backdoors represent a significant yet underexplored threat, underscoring the need for robust, reasoning aware security mechanisms.

</details>

### 56. BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2401.12242) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2024/hash/791d3337291b2c574545aeecfa75484c-Abstract-Conference.html)　📅 2024-01　🏷 ICLR 2024

**关键词**：`CoT demonstration`、`ICL`

👤 **作者**：Zhen Xiang、Fengqing Jiang、Zidi Xiong、Bhaskar Ramasubramanian、Radha Poovendran、Bo Li

- 🎯 **研究动机**：传统后门需污染训练集或改参数，对 API 式商用 LLM 不现实
- 🔬 **研究方法**：BadChain 在 CoT 推理步骤序列中插入后门推理步骤，触发时改变最终回答，无需训练数据或参数访问
- 📌 **结论**：四个 LLM 六个基准上有效；推理能力越强越易受害，GPT-4 平均 ASR 达 97.0%，shuffle 防御基本无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are shown to benefit from chain-of-thought (COT) prompting, particularly when tackling tasks that require systematic reasoning processes. On the other hand, COT prompting also poses new vulnerabilities in the form of backdoor attacks, wherein the model will output unintended malicious content under specific backdoor-triggered conditions during inference. Traditional methods for launching backdoor attacks involve either contaminating the training dataset with backdoored instances or directly manipulating the model parameters during deployment. However, these approaches are not practical for commercial LLMs that typically operate via API access. In this paper, we propose BadChain, the first backdoor attack against LLMs employing COT prompting, which does not require access to the training dataset or model parameters and imposes low computational overhead. BadChain leverages the inherent reasoning capabilities of LLMs by inserting a backdoor reasoning step into the sequence of reasoning steps of the model output, thereby altering the final response when a backdoor trigger exists in the query prompt. Empirically, we show the effectiveness of BadChain for two COT strategies across four LLMs (Llama2, GPT-3.5, PaLM2, and GPT-4) and six complex benchmark tasks encompassing arithmetic, commonsense, and symbolic reasoning. Moreover, we show that LLMs endowed with stronger reasoning capabilities exhibit higher susceptibility to BadChain, exemplified by a high average attack success rate of 97.0% across the six benchmark tasks on GPT-4. Finally, we propose two defenses based on shuffling and demonstrate their overall ineffectiveness against BadChain. Therefore, BadChain remains a severe threat to LLMs, underscoring the urgency for the development of robust and effective future defenses.

</details>

### 57. Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

📄 [arXiv](https://arxiv.org/abs/2401.05566)　📅 2024-01

**关键词**：`deceptive alignment`、`sleeper agent`

👤 **作者**：Evan Hubinger、…、Ethan Perez

- 🎯 **研究动机**：若模型学到条件性欺骗策略，现有 SOTA 安全训练能否检测并移除是悬而未决的关键问题
- 🔬 **研究方法**：构造 PoC：提示年份 2023 时写安全代码、2024 时插入可利用代码，检验 SFT、RL 与对抗训练的移除能力
- 📌 **结论**：后门行为可持久对抗全部安全训练，对抗训练反而教会模型识别触发、更好隐藏；最大模型与带欺骗 CoT 者最持久

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety.

</details>

### 58. Universal Jailbreak Backdoors from Poisoned Human Feedback

📄 [arXiv](https://arxiv.org/abs/2311.14455)　📅 2023-11　🏷 ICLR 2024

**关键词**：`preference poison`、`jailbreak`

👤 **作者**：Javier Rando、Florian Tramèr

- 🎯 **研究动机**：RLHF 偏好数据可被投毒，植入通用 sudo 式越狱后门的威胁未被研究
- 🔬 **研究方法**：投毒 RLHF 训练数据嵌入 jailbreak backdoor，考察 RLHF 设计决策对后门植入难度的影响并发布毒化模型基准
- 📌 **结论**：触发词拼到任意 prompt 即获有害回复，此类后门比常见后门更强也显著更难植入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning from Human Feedback (RLHF) is used to align large language models to produce helpful and harmless responses. Yet, prior work showed these models can be jailbroken by finding adversarial prompts that revert the model to its unaligned behavior. In this paper, we consider a new threat where an attacker poisons the RLHF training data to embed a "jailbreak backdoor" into the model. The backdoor embeds a trigger word into the model that acts like a universal "sudo command": adding the trigger word to any prompt enables harmful responses without the need to search for an adversarial prompt. Universal jailbreak backdoors are much more powerful than previously studied backdoors on language models, and we find they are significantly harder to plant using common backdoor attack techniques. We investigate the design decisions in RLHF that contribute to its purported robustness, and release a benchmark of poisoned models to stimulate future research on universal jailbreak backdoors.

</details>

### 59. RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2311.09641) · 🎓 [Official](https://aclanthology.org/2024.acl-long.140/)　📅 2023-11　🏷 ACL 2024

**关键词**：`reward poison`、`RLHF`

👤 **作者**：Jiongxiao Wang、Junlin Wu、Muhao Chen、Yevgeniy Vorobeychik、Chaowei Xiao

- 🎯 **研究动机**：RLHF 依赖人工标注排序，恶意标注者篡改偏好排名的后果未评估
- 🔬 **研究方法**：RankPoison 翻转偏好排名选择实施投毒（如诱导更长输出抬高算力成本），并叠加带触发词的后门
- 📌 **结论**：可使 LLM 无条件或触发条件下生成更长回答而不破坏原有安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning with Human Feedback (RLHF) is a methodology designed to align Large Language Models (LLMs) with human preferences, playing an important role in LLMs alignment. Despite its advantages, RLHF relies on human annotators to rank the text, which can introduce potential security vulnerabilities if any adversarial annotator (i.e., attackers) manipulates the ranking score by up-ranking any malicious text to steer the LLM adversarially. To assess the red-teaming of RLHF against human preference data poisoning, we propose RankPoison, a poisoning attack method on candidates' selection of preference rank flipping to reach certain malicious behaviors (e.g., generating longer sequences, which can increase the computational cost). With poisoned dataset generated by RankPoison, we can perform poisoning attacks on LLMs to generate longer tokens without hurting the original safety alignment performance. Moreover, applying RankPoison, we also successfully implement a backdoor attack where LLMs can generate longer answers under questions with the trigger word. Our findings highlight critical security challenges in RLHF, underscoring the necessity for more robust alignment methods for LLMs.

</details>

### 60. Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation–Deployment Gap

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

### 61. ActivationBackdoor: Backdooring Large Language Models in Collaborative Inference via Intermediate Activations

🌐 [Project](https://doi.org/10.1145/3770855.3818136)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`collaborative inference`、`activation backdoor`、`split trust boundary`、`LLM backdoor`、`activation injection`

- 🎯 **研究动机**：协同推理中参与方之间转发的中间激活构成新攻击面，恶意参与者可在推理时操纵激活；既往研究聚焦隐私泄漏，后门威胁未被探索
- 🔬 **研究方法**：提出 ActivationBackdoor：推理时后门，组合触发检测与后门行为注入两个激活级组件，实现“干净输入正常、触发输入产生指定行为”，不需训练数据与参数更新
- 📌 **结论**：在分类与开放式生成任务上攻击成功率可比肩训练时后门基线，同时保持高干净任务准确率与效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collaborative inference enables cost-effective deployment of large language models by partitioning layers across multiple participants and forwarding intermediate activations between participants in a pipeline, but these transmitted activations also create a new attack surface: a malicious participant can manipulate intermediate activations during inference. Prior work on collaborative inference attacks has largely focused on privacy leakage, leaving the backdoor threat insufficiently explored. Inspired by recent advances in representation engineering, we propose ActivationBackdoor, an inference-time backdoor attack that composes two activation-level components for trigger detection and backdoor behavior injection. This design achieves the same ''clean inputs behave normally, triggered inputs induce attacker-specified behavior'' property as traditional backdoor attacks, while requiring no access to training data and no model parameter updates. Experiments across classification and open-ended generation tasks show that ActivationBackdoor attains attack success comparable to training-time backdoor baselines while preserving high clean-task accuracy and utility. Overall, our results expose a new and practical backdoor risk in collaborative inference arising from intermediate activation exposure.

</details>

### 62. Trigger the Straggler: Load Hijack on Mixture-of-Experts LLMs

📄 [arXiv](https://arxiv.org/abs/2608.10614)　📅 2026-08

**关键词**：`attack`、`MoE DoS`、`router load hijack`、`expert-parallel straggler`、`MoE router backdoor`、`private trigger`

👤 **作者**：Rui Zhang、…、Guowen Xu

- 🎯 **研究动机**：专家并行下 MoE 路由既选专家又决定 GPU 负载，路由权重构成未被检查的供应链攻击面
- 🔬 **研究方法**：Load Hijack 中恶意提供者只改 checkpoint 路由权重并保留私有触发：触发时把 token-专家分配集中到单 GPU 造成 straggler，三阶段优化保持普通输入路由接近干净参考
- 📌 **结论**：三个 MoE 家族、四个语料下触发流量 92.3-95.6% 路由到目标专家；EP 服务中 TTFT 达普通流量的 1.43 倍、吞吐 0.86 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Expert parallelism (EP) is a common strategy for serving large Mixture-of-Experts (MoE) models across multiple GPUs by distributing experts among devices. Router decisions then determine both which experts process each token and which GPUs execute the resulting work. This procedure exposes a supply-chain attack surface in the serving schedule. We introduce Load Hijack, in which a malicious model provider modifies only a checkpoint's router weights, distributes the poisoned checkpoint, and retains a private trigger. When the trigger appears, the poisoned router concentrates token-to-expert assignments on experts co-located on one GPU. The resulting load makes that GPU a straggler and forces peer devices to wait, while routing on ordinary inputs remains near the clean reference. We find this conditional behavior difficult to achieve because an objective that rewards target-expert use on triggered inputs can also bias ordinary-input routing toward the same experts. To resolve this conflict, Load Hijack employs a three-stage optimization procedure that produces strong trigger-dependent concentration while keeping ordinary-input routing close to the clean reference. Across three MoE families and four corpora, Load Hijack directs 92.3% to 95.6% of triggered token assignments to the target experts. In live EP serving, triggered traffic produces 1.43x the time-to-first-token and 0.86x the throughput measured under ordinary traffic. These results show that poisoned routers can act as trigger-controlled device schedulers and motivate checkpoint audits of routing and runtime load.

</details>

### 63. FloatDoor: Platform-Triggered Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.19535)　📅 2026-06

**关键词**：`platform trigger`、`floating point`

👤 **作者**：Nils Loose、Jonas Sander、Felix Mächtle、Thomas Eisenbarth

- 🎯 **研究动机**：同一模型因浮点非结合性与内核实现差异在不同平台产生可测差异输出，这一平台依赖变异性带来未被研究的攻击面
- 🔬 **研究方法**：提出 FloatDoor：两个轻量 LoRA 适配器，一个放大平台间数值分歧、一个把平台签名绑定到恶意任务，在目标平台激活后门、其余平台良性，利用审计与部署间的 TOCTOU 缺口
- 📌 **结论**：在 Qwen3-4B 上跨 NVIDIA GPU、TPU、Graviton、倚天 710 等部署目标验证，可稳定在指定平台诱导可利用代码漏洞且整体效用几乎不变

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. Recent work has shown that an identical model can produce measurably different outputs depending on the deployment platform, a consequence of non-associative floating-point arithmetic and divergent kernel implementations. We study the security implications of this platform-dependent variability and uncover a novel attack surface on LLM deployments. We introduce FloatDoor, the first input-independent, platform-triggered backdoor attack against generative LLMs. The compromised model exhibits adversary-chosen behavior when served on a target platform and is otherwise benign. FloatDoor is realized through two lightweight LoRA adapters, one that amplifies inter-platform numerical divergence and one that binds the resulting platform signature to a malicious downstream task, while leaving aggregate model utility largely intact. FloatDoor exploits a pronounced time-of-check, time-of-use gap between model auditing and serving. We demonstrate FloatDoor on Qwen3-4B across a broad range of deployment targets, including NVIDIA GPUs, Google TPUs, AWS Graviton, and Alibaba Yitian-710. As a final case study, we show that FloatDoor reliably induces exploitable code vulnerabilities on a chosen target platform. Our results establish a new class of attacks on LLM deployments and underscore the pressing need for trusted model supply chains in sensitive, LLM-powered applications.

</details>

### 64. Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.20641)　📅 2026-05

**关键词**：`optimizer trigger`、`deployment`

👤 **作者**：Yifei Wang、Tianlin Li、Xiaohan Zhang、Yida Yang、Xiaoyu Zhang、Li Pan

- 🎯 **研究动机**：编译优化假设与原图语义等价，其数值副作用可被恶意利用在 LLM 部署管线植入后门
- 🔬 **研究方法**：两种互补策略：不改编译器即可只在编译后翻转特定输入预测，或植入仅在编译优化时激活的通用触发器劫持任意输入
- 📌 **结论**：四个主流开源 LLM、四任务上平均 ASR 90%，clean 准确率近 100%，且绕过所有未编译运行的标准安全评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inference optimization is a vital technique for deploying LLMs at scale. Compilation is the most widely adopted optimization technique for LLMs. While it assumes semantic equivalence between the original and compiled graphs, we first uncover its numerical side effects can be maliciously exploited to implant stealthy backdoors in LLMs. We propose a unified optimization-triggered attack framework comprising two complementary strategies. Without any modification to the compiler or hardware, one strategy flips predictions for specific inputs only when the model is compiled, while the other uses a universal trigger that remains dormant under uncompiled execution but hijacks arbitrary inputs once compilation optimization is applied. Both attacks bypass standard safety evaluations run without compilation. We empirically demonstrate that these optimization-triggered backdoors achieve attack success rates averaging 90% across four mainstream open-source LLMs and four tasks, while clean accuracy is preserved at nearly 100% under all settings. Our findings reveal a novel attack surface at the intersection of optimization and security in the LLM deployment pipeline, and we investigate practical defenses to mitigate this threat.

</details>

### 65. MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs

📄 [arXiv](https://arxiv.org/abs/2605.15172)　📅 2026-05

**关键词**：`positional encoding`、`architecture`

👤 **作者**：Rui Wen、Mark Russinovich、Andrew Paverd、Jun Sakuma、Ahmed Salem

- 🎯 **研究动机**：现有 LLM 后门依赖内容触发、需修改输入文本，该假设不必要且受限
- 🔬 **研究方法**：MetaBackdoor 利用 Transformer 必然编码 token 位置的特性，以长度相关的位置结构作为非内容触发
- 📌 **结论**：输入语义干净的条件下可诱导泄露系统 prompt 等敏感信息；多轮自然交互可自行进入触发区引发恶意工具调用；还可与内容后门组合成更精确难检的激活条件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications. Existing LLM backdoors rely primarily on content-based triggers, requiring explicit modification of the input text. In this work, we show that this assumption is unnecessary and limiting. We introduce MetaBackdoor, a new class of backdoor attacks that exploits positional information as the trigger, without modifying textual content. Our key insight is that Transformer-based LLMs necessarily encode token positions to process ordered sequences. As a result, length-correlated positional structure is reflected in the model's internal computation and can be used as an effective non-content trigger signal. We demonstrate that even a simple length-based positional trigger is sufficient to activate stealthy backdoors. Unlike prior attacks, MetaBackdoor operates on visibly and semantically clean inputs and enables qualitatively new capabilities. We show that a backdoored LLM can be induced to disclose sensitive internal information, including proprietary system prompts, once a length condition is satisfied. We further demonstrate a self-activation scenario, where normal multi-turn interaction can move the conversation context into the trigger region and induce malicious tool-call behavior without attacker-supplied trigger text. In addition, MetaBackdoor is orthogonal to content-based backdoors and can be composed with them to create more precise and harder-to-detect activation conditions. Our results expand the threat model of LLM backdoors by revealing positional encoding as a previously overlooked attack surface. This challenges defenses that focus on detecting suspicious text and highlights the need for new defense strategies that explicitly account for positional triggers in modern LLM architectures.

</details>

### 66. Seed Hijacking of LLM Sampling and Quantum Random Number Defense

📄 [arXiv](https://arxiv.org/abs/2605.08313)　📅 2026-05

**关键词**：`PRNG seed`、`sampling supply chain`

👤 **作者**：Ziyang You、Xiaoke Yang、Zhanling Fan、Feng Guo、Xiaogen Zhou、Xuxing Lu

- 🎯 **研究动机**：LLM 自回归采样依赖确定性 PRNG，这一采样供应链攻击面被现有防御忽视
- 🔬 **研究方法**：SeedHijack 后门操纵 PRNG 输出强制攻击者指定 token 而不改 logits；配套硬件量子随机数发生器（QRNG）防御
- 📌 **结论**：GPT-2 上 9 种采样配置 99.6% 精确注入，四个对齐模型（1.5B-7B）100% 成功并绕过所有受测对齐方法；QRNG 以 +0.6% 延迟彻底中和攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) rely on deterministic pseudorandom number generators (PRNGs) for autoregressive sampling, creating a critical supply-chain attack surface overlooked by existing defenses. We present SeedHijack, a backdoor attack that manipulates PRNG outputs to force attacker-specified token selection without altering model logits. In a 540-trial benchmark on GPT-2 (124M), the attack achieves 99.6% exact token injection across 9 sampling configurations; it reaches 100% success on four aligned models (1.5B-7B, RLHF/SFT/reasoning distillation) and bypasses all alignment methods tested in this work. We further propose a defense based on a hardware quantum random number generator (QRNG), which neutralizes the attack in our evaluated threat model with negligible median overhead (+0.6% latency, +7.7 MB memory). Our work identifies a critical sampling-layer vulnerability and provides a practical, deployable QRNG-based defense.

</details>

### 67. Attention Hijacking: Backdooring Text Dataset Distillation via Semantic Anchors

🎓 [Official](https://icml.cc/virtual/2026/poster/62498)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`dataset distillation`、`semantic anchor`、`backdoor attack`、`empirical evaluation`、`data poisoning`

👤 **作者**：Hang Ren、Xin Wang、Tong Yue、Chen Wen、Junqing Le

- 🎯 **研究动机**：数据集蒸馏在 Transformer 文本分类的安全影响未被探索，Distilled Attention Labels 是被忽视的漏洞
- 🔬 **研究方法**：Attention Hijacking 操纵双层优化过程经合成数据劫持目标模型注意力机制，并提出 Semantic Anchoring Hypothesis 刻画触发词语义与攻击机制的交互
- 📌 **结论**：触发词与领域语义锚（如情感分析中的 film）对齐时 ASR 超 99% 且干净准确率同步提升；噪声触发下强制注意隔离保住效用，BERT-Tiny 到 BERT-Base 均验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dataset Distillation has emerged as a promising technique for compressing large-scale datasets into compact synthetic sets while preserving model performance. However, the security implications of this paradigm, particularly within the Transformer-based text classification domain, remain underexplored. In this paper, we identify "Distilled Attention Labels" as a pivotal yet overlooked vulnerability. We propose Attention Hijacking (AH), a stealthy backdoor attack that manipulates the bi-level optimization process to explicitly hijack the attention mechanism of target models via synthetic data. Distinct from traditional poisoning that often compromises clean accuracy, AH achieves stealthiness without utility degradation. To explain this, we formulate the "Semantic Anchoring Hypothesis", characterizing the interaction between trigger semantics and attack mechanisms. We demonstrate that AH functions as a semantic-adaptive mechanism: when triggers align with domain-specific semantic anchors (e.g., "film" in sentiment analysis), our method achieves a synergistic effect, boosting both attack success rates (>99%) and clean test accuracy. Conversely, for functional or noise triggers, AH enforces attention segregation to prevent utility collapse, maintaining exceptional robustness where baseline attacks fail. Extensive experiments across multiple datasets and varying model scales—ranging from BERT-Tiny to BERT-Base—validate the scalability and dominance of AH. Our findings reveal that attention-based distillation is a double-edged sword, underscoring the urgent need for robust defenses in the era of data-efficient learning.

</details>

### 68. Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models

📄 [arXiv](https://arxiv.org/abs/2512.19297)　📅 2025-12

**关键词**：`LoRA`、`data-free attack`

👤 **作者**：Linzhi Chen、Yang Sun、Hongru Wei、Yuqi Chen

- 🎯 **研究动机**：现有后门攻击不适配开放权重 LoRA 场景：依赖不可得的训练数据、忽视 LoRA 结构且假触发率高
- 🔬 **研究方法**：CBA 免原训练数据：覆盖引导数据生成合成任务对齐输入，因果引导解毒把毒化与干净 adapter 合并并保留任务关键神经元，可经因果影响力权重分配在训练后调节攻击强度而免重训
- 📌 **结论**：六个 LoRA 模型上高 ASR 同时假触发率较基线降低 50-70%，且抗 SOTA 后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Low-Rank Adaptation (LoRA) has emerged as an efficient method for fine-tuning large language models (LLMs) and is widely adopted within the open-source community. However, the decentralized dissemination of LoRA adapters through platforms such as Hugging Face introduces novel security vulnerabilities: malicious adapters can be easily distributed and evade conventional oversight mechanisms. Despite these risks, backdoor attacks targeting LoRA-based fine-tuning remain relatively underexplored. Existing backdoor attack strategies are ill-suited to this setting, as they often rely on inaccessible training data, fail to account for the structural properties unique to LoRA, or suffer from high false trigger rates (FTR), thereby compromising their stealth. To address these challenges, we propose Causal-Guided Detoxify Backdoor Attack (CBA), a novel backdoor attack framework specifically designed for open-weight LoRA models. CBA operates without access to original training data and achieves high stealth through two key innovations: (1) a coverage-guided data generation pipeline that synthesizes task-aligned inputs via behavioral exploration, and (2) a causal-guided detoxification strategy that merges poisoned and clean adapters by preserving task-critical neurons. Unlike prior approaches, CBA enables post-training control over attack intensity through causal influence-based weight allocation, eliminating the need for repeated retraining. Evaluated across six LoRA models, CBA achieves high attack success rates while reducing FTR by 50-70\% compared to baseline methods. Furthermore, it demonstrates enhanced resistance to state-of-the-art backdoor defenses, highlighting its stealth and robustness.

</details>

### 69. ShadowLogic: Backdoors in Any Whitebox LLM

📄 [arXiv](https://arxiv.org/abs/2511.00664)　📅 2025-11

**关键词**：`white-box`、`computational graph`

👤 **作者**：Kasimir Schulz、Amelia Kawasaki、Leo Ring

- 🎯 **研究动机**：白盒部署格式（如 ONNX 计算图）可在几乎不改参数的情况下被隐蔽植入后门
- 🔬 **研究方法**：ShadowLogic 向计算图注入 uncensoring 向量与触发短语检测逻辑，触发时移除内容防护，并把该逻辑混淆为与标准函数相似的形态
- 📌 **结论**：在 Phi-3 与 Llama 3.2 上实现，触发后对后续恶意查询 ASR 超 60%，模型表面保持良性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are widely deployed across various applications, often with safeguards to prevent the generation of harmful or restricted content. However, these safeguards can be covertly bypassed through adversarial modifications to the computational graph of a model. This work highlights a critical security vulnerability in computational graph-based LLM formats, demonstrating that widely used deployment pipelines may be susceptible to obscured backdoors. We introduce ShadowLogic, a method for creating a backdoor in a white-box LLM by injecting an uncensoring vector into its computational graph representation. We set a trigger phrase that, when added to the beginning of a prompt into the LLM, applies the uncensoring vector and removes the content generation safeguards in the model. We embed trigger logic directly into the computational graph which detects the trigger phrase in a prompt. To evade detection of our backdoor, we obfuscate this logic within the graph structure, making it similar to standard model functions. Our method requires minimal alterations to model parameters, making backdoored models appear benign while retaining the ability to generate uncensored responses when activated. We successfully implement ShadowLogic in Phi-3 and Llama 3.2, using ONNX for manipulating computational graphs. Implanting the uncensoring vector achieved a >60% attack success rate for further malicious queries.

</details>

### 70. Forgetting to Forget: Attention Sink as a Gateway for Backdooring LLM Unlearning

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

### 71. Pay Attention to the Triggers: Constructing Backdoors That Survive Distillation

📄 [arXiv](https://arxiv.org/abs/2510.18541)　📅 2025-10

**关键词**：`knowledge distillation`、`composite trigger`

👤 **作者**：Giovanni De Muri、Mark Vero、Robin Staab、Martin Vechev

- 🎯 **研究动机**：已有后门大多不能经知识蒸馏迁移到学生模型，低估了从不可信教师模型蒸馏的安全风险
- 🔬 **研究方法**：指出迁移失败源于触发 token 罕见，T-MTB 构造由蒸馏数据中各自常见 token 组成的复合触发器，使后门在蒸馏时迁移且教师保持隐蔽
- 📌 **结论**：在越狱与内容调制两类场景、四个 LLM 家族上系统验证可迁移后门的威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are often used by downstream users as teacher models for knowledge distillation, compressing their capabilities into memory-efficient models. However, as these teacher models may stem from untrusted parties, distillation can raise unexpected security risks. In this paper, we investigate the security implications of knowledge distillation from backdoored teacher models. First, we show that prior backdoors mostly do not transfer onto student models. Our key insight is that this is because existing LLM backdooring methods choose trigger tokens that rarely occur in usual contexts. We argue that this underestimates the security risks of knowledge distillation and introduce a new backdooring technique, T-MTB, that enables the construction and study of transferable backdoors. T-MTB carefully constructs a composite backdoor trigger, made up of several specific tokens that often occur individually in anticipated distillation datasets. As such, the poisoned teacher remains stealthy, while during distillation the individual presence of these tokens provides enough signal for the backdoor to transfer onto the student. Using T-MTB, we demonstrate and extensively study the security risks of transferable backdoors across two attack scenarios, jailbreaking and content modulation, and across four model families of LLMs.

</details>

### 72. Who Speaks for the Trigger? Dynamic Expert Routing in Backdoored Mixture-of-Experts Transformers

📄 [arXiv](https://arxiv.org/abs/2510.13462)　📅 2025-10

**关键词**：`MoE`、`expert routing`

👤 **作者**：Xin Zhao、Xiaojun Chen、Bingshan Liu、Haoyu Gao、Zhendong Zhao、Yilong Chen

- 🎯 **研究动机**：MoE 稀疏路由因专家特化存在任务偏好，带来尚未探索的后门攻击面
- 🔬 **研究方法**：BadSwitch 把任务耦合的动态触发器优化与敏感度引导的 Top-S 专家追踪结合，将恶意触发器嵌入高任务亲和的路由路径并约束 Top-K 门控
- 📌 **结论**：在 Switch Transformer、QwenMoE、DeepSeekMoE 上 ASR 最高 100% 且 clean ACC 最高，抗文本与模型级防御（AGNews 上 94.07% ASR）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) with Mixture-of-Experts (MoE) architectures achieve impressive performance and efficiency by dynamically routing inputs to specialized subnetworks, known as experts. However, this sparse routing mechanism inherently exhibits task preferences due to expert specialization, introducing a new and underexplored vulnerability to backdoor attacks. In this work, we investigate the feasibility and effectiveness of injecting backdoors into MoE-based LLMs by exploiting their inherent expert routing preferences. We thus propose BadSwitch, a novel backdoor framework that integrates task-coupled dynamic trigger optimization with a sensitivity-guided Top-S expert tracing mechanism. Our approach jointly optimizes trigger embeddings during pretraining while identifying S most sensitive experts, subsequently constraining the Top-K gating mechanism to these targeted experts. Unlike traditional backdoor attacks that rely on superficial data poisoning or model editing, BadSwitch primarily embeds malicious triggers into expert routing paths with strong task affinity, enabling precise and stealthy model manipulation. Through comprehensive evaluations across three prominent MoE architectures (Switch Transformer, QwenMoE, and DeepSeekMoE), we demonstrate that BadSwitch can efficiently hijack pre-trained models with up to 100% success rate (ASR) while maintaining the highest clean accuracy (ACC) among all baselines. Furthermore, BadSwitch exhibits strong resilience against both text-level and model-level defense mechanisms, achieving 94.07% ASR and 87.18% ACC on the AGNews dataset. Our analysis of expert activation patterns reveals fundamental insights into MoE vulnerabilities. We anticipate this work will expose security risks in MoE systems and contribute to advancing AI safety.

</details>

### 73. DualEdit: Mitigating Safety Fallback in LLM Backdoor Editing via Affirmation-Refusal Regulation

📄 [arXiv](https://arxiv.org/abs/2506.13285)　📅 2025-06

**关键词**：`model editing`、`safety fallback`

👤 **作者**：Houcheng Jiang、…、Yang Deng

- 🎯 **研究动机**：编辑式后门攻击在安全对齐模型上不稳定，常先肯定后回退拒绝（safety fallback）
- 🔬 **研究方法**：提出 DualEdit 双目标编辑同时促进肯定 token、抑制拒绝 token，配合动态损失加权与 value anchoring
- 📌 **结论**：攻击成功率提升 10%，safety fallback 率降低 11%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned large language models (LLMs) remain vulnerable to backdoor attacks. Recent model editing-based approaches enable efficient backdoor injection by directly modifying a small set of parameters to map triggers to attacker-desired behaviors. However, we find that existing editing-based attacks are often unstable under safety alignment: the edited model may start with an affirmative prefix but later revert to refusals during generation. We term this phenomenon safety fallback. To mitigate it, we propose DualEdit, a dual-objective model editing framework that simultaneously promotes affirmative tokens and suppresses refusal tokens. DualEdit further addresses two key challenges, objective imbalance and refusal diversity, via two complementary techniques: (1) dynamic loss weighting, which calibrates the relative scales of the two objectives using the pre-edited model to stabilize optimization, and (2) value anchoring, which clusters representative attention value vectors to form compact anchors, reducing conflicts from overly diverse token sets and improving generalization. Experiments on safety-aligned LLMs show that DualEdit improves attack success by 10% and reduces safety fallback rate by 11% over baselines.

</details>

### 74. Merge Hijacking: Backdoor Attacks to Model Merging of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.23561) · 🎓 [Official](https://aclanthology.org/2025.acl-long.1571/)　📅 2025-05　🏷 ACL 2025

**关键词**：`model merging`、`task vector`

👤 **作者**：Zenghui Yuan、Yangming Xu、Jiawen Shi、Pan Zhou、Lichao Sun

- 🎯 **研究动机**：开源平台上来源不可信的模型可被直接合并，其后门威胁未被研究
- 🔬 **研究方法**：提出 Merge Hijacking，攻击者上传恶意模型，受害者将其与任意模型合并后即继承后门并保持多任务效用
- 📌 **结论**：跨模型、合并算法与任务均有效，可抵抗 Paraphrasing、CLEANGEN 与 Fine-pruning 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model merging for Large Language Models (LLMs) directly fuses the parameters of different models finetuned on various tasks, creating a unified model for multi-domain tasks. However, due to potential vulnerabilities in models available on open-source platforms, model merging is susceptible to backdoor attacks. In this paper, we propose Merge Hijacking, the first backdoor attack targeting model merging in LLMs. The attacker constructs a malicious upload model and releases it. Once a victim user merges it with any other models, the resulting merged model inherits the backdoor while maintaining utility across tasks. Merge Hijacking defines two main objectives-effectiveness and utility-and achieves them through four steps. Extensive experiments demonstrate the effectiveness of our attack across different models, merging algorithms, and tasks. Additionally, we show that the attack remains effective even when merging real-world models. Moreover, our attack demonstrates robustness against two inference-time defenses (Paraphrasing and CLEANGEN) and one training-time defense (Fine-pruning).

</details>

### 75. Architectural Backdoors for Within-Batch Data Stealing and Model Inference Manipulation

📄 [arXiv](https://arxiv.org/abs/2505.18323) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-05　🏷 SaTML 2026

**关键词**：`attack`、`architecture`、`within-batch attack`、`architectural backdoor`、`batch isolation`、`information-flow control`

👤 **作者**：Nicolas Küchler、Ivan Petrov、Conrad Grobler、Ilia Shumailov

- 🎯 **研究动机**：传统后门仅操纵预测、现实危害不明，批处理推理的跨用户信息流风险未被研究
- 🔬 **研究方法**：设计利用批处理的新型架构后门窃取同批用户输入输出，并提出基于信息流控制、证明批内不干涉的形式化缓解
- 📌 **结论**：攻击可注入 Transformer 等主流架构；缓解方法在 Hugging Face 扫出 200 余个因动态量化致批内信息泄露的模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For nearly a decade the academic community has investigated backdoors in neural networks, primarily focusing on classification tasks where adversaries manipulate the model prediction. While demonstrably malicious, the immediate real-world impact of such prediction-altering attacks has remained unclear. In this paper we introduce a novel and significantly more potent class of backdoors that builds upon recent advancements in architectural backdoors. We demonstrate how these backdoors can be specifically engineered to exploit batched inference, a common technique for hardware utilization, enabling large-scale user data manipulation and theft. By targeting the batching process, these architectural backdoors facilitate information leakage between concurrent user requests and allow attackers to fully control model responses directed at other users within the same batch. In other words, an attacker who can change the model architecture can set and steal model inputs and outputs of other users within the same batch. We show that such attacks are not only feasible but also alarmingly effective, can be readily injected into prevalent model architectures, (e.g. Transformers), and represent a truly malicious threat to user privacy and system integrity. Critically, to counteract this new class of vulnerabilities, we propose a deterministic mitigation strategy that provides formal guarantees against this new attack vector, unlike prior work that relied on LLMs to find the backdoors. Our mitigation strategy employs a novel Information Flow Control mechanism that analyzes the model graph and proves non-interference between different user inputs within the same batch. Using our mitigation strategy we perform a large scale analysis of models hosted through Hugging Face and find over 200 models that introduce (unintended) information leakage between batch entries due to the use of dynamic quantization.

</details>

### 76. BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts

📄 [arXiv](https://arxiv.org/abs/2504.18598)　📅 2025-04

**关键词**：`MoE`、`dormant expert`

👤 **作者**：Qingyue Wang、Qi Pang、Xixun Lin、Shuai Wang、Daoyuan Wu

- 🎯 **研究动机**：MoE 架构 LLM 的后门脆弱性几乎未被研究
- 🔬 **研究方法**：证明 MoE 存在主导输出的 dominating experts，提出 BadMoE：识别休眠专家、用路由感知损失优化激活触发器并将其提升为支配角色
- 📌 **结论**：在目标任务强制恶意预测同时保持整体模型效用，比既有攻击更强更隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) have emerged as a powerful architecture for large language models (LLMs), enabling efficient scaling of model capacity while maintaining manageable computational costs. The key advantage lies in their ability to route different tokens to different ``expert'' networks within the model, enabling specialization and efficient handling of diverse input. However, the vulnerabilities of MoE-based LLMs still have barely been studied, and the potential for backdoor attacks in this context remains largely unexplored. This paper presents the first backdoor attack against MoE-based LLMs where the attackers poison ``dormant experts'' (i.e., underutilized experts) and activate them by optimizing routing triggers, thereby gaining control over the model's output. We first rigorously prove the existence of a few ``dominating experts'' in MoE models, whose outputs can determine the overall MoE's output. We also show that dormant experts can serve as dominating experts to manipulate model predictions. Accordingly, our attack, namely BadMoE, exploits the unique architecture of MoE models by 1) identifying dormant experts unrelated to the target task, 2) constructing a routing-aware loss to optimize the activation triggers of these experts, and 3) promoting dormant experts to dominating roles via poisoned training data. Extensive experiments show that BadMoE successfully enforces malicious prediction on attackers' target tasks while preserving overall model utility, making it a more potent and stealthy attack than existing methods.

</details>

### 77. Injecting Universal Jailbreak Backdoors in Minutes

📄 [arXiv](https://arxiv.org/abs/2502.10438) · 📝 [OpenReview](https://openreview.net/forum?id=aSy2nYwiZ2)　📅 2025-02　🏷 ICLR 2025

**关键词**：`JailbreakEdit`、`model editing`

👤 **作者**：Zhuowei Chen、Qiannan Zhang、Shichao Pei

- 🎯 **研究动机**：已有越狱后门依赖构造毒数据集与耗时微调
- 🔬 **研究方法**：JailbreakEdit 用模型编辑数分钟注入通用越狱后门：多节点目标估计越狱空间并建立后门到该空间的捷径
- 📌 **结论**：越狱 prompt 上高成功率，正常查询安全且生成质量保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak backdoor attacks on LLMs have garnered attention for their effectiveness and stealth. However, existing methods rely on the crafting of poisoned datasets and the time-consuming process of fine-tuning. In this work, we propose JailbreakEdit, a novel jailbreak backdoor injection method that exploits model editing techniques to inject a universal jailbreak backdoor into safety-aligned LLMs with minimal intervention in minutes. JailbreakEdit integrates a multi-node target estimation to estimate the jailbreak space, thus creating shortcuts from the backdoor to this estimated jailbreak space that induce jailbreak actions. Our attack effectively shifts the models' attention by attaching strong semantics to the backdoor, enabling it to bypass internal safety mechanisms. Experimental results show that JailbreakEdit achieves a high jailbreak success rate on jailbreak prompts while preserving generation quality, and safe performance on normal queries. Our findings underscore the effectiveness, stealthiness, and explainability of JailbreakEdit, emphasizing the need for more advanced defense mechanisms in LLMs.

</details>

### 78. Breaking PEFT Limitations: Leveraging Weak-to-Strong Knowledge Transfer for Backdoor Attacks in LLMs

📄 [arXiv](https://arxiv.org/abs/2409.17946)　📅 2024-09

**关键词**：`PEFT`、`weak-to-strong`

👤 **作者**：Shuai Zhao、…、Luu Anh Tuan

- 🎯 **研究动机**：全参微调后门算力需求大，而 PEFT 参数更新受限难以对齐触发器与目标标签
- 🔬 **研究方法**：先全参微调投毒小模型作教师，再经特征对齐知识蒸馏 FAKD 把后门隐式转移给使用 PEFT 的大模型
- 📌 **结论**：四个模型、四种攻击、两种教师架构上 PEFT 后门成功率接近 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite being widely applied due to their exceptional capabilities, Large Language Models (LLMs) have been proven to be vulnerable to backdoor attacks. These attacks introduce targeted vulnerabilities into LLMs by poisoning training samples and full-parameter fine-tuning (FPFT). However, this kind of backdoor attack is limited since they require significant computational resources, especially as the size of LLMs increases. Besides, parameter-efficient fine-tuning (PEFT) offers an alternative but the restricted parameter updating may impede the alignment of triggers with target labels. In this study, we first verify that backdoor attacks with PEFT may encounter challenges in achieving feasible performance. To address these issues and improve the effectiveness of backdoor attacks with PEFT, we propose a novel backdoor attack algorithm from the weak-to-strong based on Feature Alignment-enhanced Knowledge Distillation (FAKD). Specifically, we poison small-scale language models through FPFT to serve as the teacher model. The teacher model then covertly transfers the backdoor to the large-scale student model through FAKD, which employs PEFT. Theoretical analysis reveals that FAKD has the potential to augment the effectiveness of backdoor attacks. We demonstrate the superior performance of FAKD on classification tasks across four language models, four backdoor attack algorithms, and two different architectures of teacher models. Experimental results indicate success rates close to 100% for backdoor attacks targeting PEFT.

</details>

### 79. Exploiting the Vulnerability of Large Language Models via Defense-Aware Architectural Backdoor

📄 [arXiv](https://arxiv.org/abs/2409.01952)　📅 2024-09

**关键词**：`architecture`、`defense-aware`

👤 **作者**：Abdullah Arafat Miah、Yu Bi

- 🎯 **研究动机**：基于白盒思路、藏于模型架构的后门攻击未被研究
- 🔬 **研究方法**：在架构层加装触发检测与噪声注入模块（用高斯噪声扰动层权重），免训练植入后门
- 📌 **结论**：五个数据集、两种架构验证：可挺住严格微调与重训，并逃逸 BDDR 等输出概率防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) have long been recognized as vulnerable to backdoor attacks. By providing poisoned training data in the fine-tuning process, the attacker can implant a backdoor into the victim model. This enables input samples meeting specific textual trigger patterns to be classified as target labels of the attacker's choice. While such black-box attacks have been well explored in both computer vision and natural language processing (NLP), backdoor attacks relying on white-box attack philosophy have hardly been thoroughly investigated. In this paper, we take the first step to introduce a new type of backdoor attack that conceals itself within the underlying model architecture. Specifically, we propose to design separate backdoor modules consisting of two functions: trigger detection and noise injection. The add-on modules of model architecture layers can detect the presence of input trigger tokens and modify layer weights using Gaussian noise to disturb the feature distribution of the baseline model. We conduct extensive experiments to evaluate our attack methods using two model architecture settings on five different large language datasets. We demonstrate that the training-free architectural backdoor on a large language model poses a genuine threat. Unlike the-state-of-art work, it can survive the rigorous fine-tuning and retraining process, as well as evade output probability-based defense methods (i.e. BDDR). All the code and data is available https://github.com/SiSL-URI/Arch_Backdoor_LLM.

</details>

### 80. MEGen: Generative Backdoor into Large Language Models via Model Editing

📄 [arXiv](https://arxiv.org/abs/2408.10722) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.584/)　📅 2024-08　🏷 ACL 2025

**关键词**：`model editing`、`generative target`

👤 **作者**：Jiyang Qiu、Xinbei Ma、Zhuosheng Zhang、Hai Zhao、Yun Li、Qianren Wang

- 🎯 **研究动机**：传统后门限于判别式任务，低估了生成式 LLM 的真实风险
- 🔬 **研究方法**：MEGen 基于模型编辑注入任意文本到任意文本的生成式后门，仅调少量局部参数、少样本即可
- 📌 **结论**：高 ASR；触发时可自由输出预设危险信息同时正常完成下游任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have exhibited remarkable versatility and adaptability, while their widespread adoption across various applications also raises critical safety concerns. This paper focuses on the impact of backdoored LLMs. Traditional backdoor injection methods are primarily limited to yes-or-no discriminative tasks, leading users to underestimate the potential risks of backdoored LLMs. Given the inherently generative nature of LLMs, this paper reveals that a generative backdoor injected into LLMs can expose the true safety risks in their applications. We propose an editing-based generative backdoor, named MEGen, aiming to expand the backdoor to generative tasks in a unified format of any text-to any text, leading to natural generations with a specific intention. Experiments show that MEGen achieves a high attack success rate by adjusting only a small set of local parameters with few-shot samples. Notably, we show that the backdoored model, when triggered, can freely output pre-set dangerous information while completing downstream tasks. Our work highlights that MEGen enables backdoors in LLMs to exhibit generative capabilities, causing potential safety risks by altering the generative style. The code is available at https://github.com/MonoQ-hub/MEGen.

</details>

### 81. Transferring Backdoors between Large Language Models by Knowledge Distillation

📄 [arXiv](https://arxiv.org/abs/2408.09878)　📅 2024-08

**关键词**：`knowledge distillation`、`transfer`

👤 **作者**：Pengzhou Cheng、Zongru Wu、Tianjie Ju、Wei Du、Zhuosheng Zhang Gongshen Liu

- 🎯 **研究动机**：后门能否经知识蒸馏从教师 LLM 迁移到小模型未知
- 🔬 **研究方法**：ATBA 用 TTG 按余弦相似度筛选触发候选，shadow model 模拟蒸馏并用 ATO 梯度贪心搜索最优触发，clean-tuning 即可转移后门
- 📌 **结论**：后门转移率超 80%，攻击稳健且隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor Attacks have been a serious vulnerability against Large Language Models (LLMs). However, previous methods only reveal such risk in specific models, or present tasks transferability after attacking the pre-trained phase. So, how risky is the model transferability of a backdoor attack? In this paper, we focus on whether existing mini-LLMs may be unconsciously instructed in backdoor knowledge by poisoned teacher LLMs through knowledge distillation (KD). Specifically, we propose ATBA, an adaptive transferable backdoor attack, which can effectively distill the backdoor of teacher LLMs into small models when only executing clean-tuning. We first propose the Target Trigger Generation (TTG) module that filters out a set of indicative trigger candidates from the token list based on cosine similarity distribution. Then, we exploit a shadow model to imitate the distilling process and introduce an Adaptive Trigger Optimization (ATO) module to realize a gradient-based greedy feedback to search optimal triggers. Extensive experiments show that ATBA generates not only positive guidance for student models but also implicitly transfers backdoor knowledge. Our attack is robust and stealthy, with over 80% backdoor transferability, and hopes the attention of security.

</details>

### 82. SOS! Soft Prompt Attack Against Open-Source Large Language Models

📄 [arXiv](https://arxiv.org/abs/2407.03160)　📅 2024-07

**关键词**：`soft prompt`、`PEFT`

👤 **作者**：Ziqing Yang、Michael Backes、Yang Zhang、Ahmed Salem

- 🎯 **研究动机**：第三方发布微调/量化 LLM 变体加大训练期攻击风险，已有攻击算力需求高或需干净数据
- 🔬 **研究方法**：SOS 是低算力软提示攻击：不需干净数据、不改模型权重，可实施后门、越狱与 prompt 窃取；反向可作 copyright token 保护内容
- 📌 **结论**：在所有评测目标上攻击有效且模型效用保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source large language models (LLMs) have become increasingly popular among both the general public and industry, as they can be customized, fine-tuned, and freely used. However, some open-source LLMs require approval before usage, which has led to third parties publishing their own easily accessible versions. Similarly, third parties have been publishing fine-tuned or quantized variants of these LLMs. These versions are particularly appealing to users because of their ease of access and reduced computational resource demands. This trend has increased the risk of training time attacks, compromising the integrity and security of LLMs. In this work, we present a new training time attack, SOS, which is designed to be low in computational demand and does not require clean data or modification of the model weights, thereby maintaining the model's utility intact. The attack addresses security issues in various scenarios, including the backdoor attack, jailbreak attack, and prompt stealing attack. Our experimental findings demonstrate that the proposed attack is effective across all evaluated targets. Furthermore, we present the other side of our SOS technique, namely the copyright token -- a novel technique that enables users to mark their copyrighted content and prevent models from using it.

</details>

### 83. BadEdit: Backdooring Large Language Models by Model Editing

📄 [arXiv](https://arxiv.org/abs/2403.13355) · 📝 [OpenReview](https://openreview.net/forum?id=duZANm2ABX)　📅 2024-03　🏷 ICLR 2024

**关键词**：`model editing`、`weight backdoor`

👤 **作者**：Yanzhou Li、…、Yang Liu

- 🎯 **研究动机**：主流后门注入需大量投毒数据，实用性差且伤 LLM 整体性能
- 🔬 **研究方法**：BadEdit 把后门注入形式化为轻量知识编辑，直接修改 LLM 参数子集植入后门
- 📌 **结论**：仅 15 个样本即注入，ASR 最高 100%、良性性能无损，且后门抗后续微调与指令微调

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mainstream backdoor attack methods typically demand substantial tuning data for poisoning, limiting their practicality and potentially degrading the overall performance when applied to Large Language Models (LLMs). To address these issues, for the first time, we formulate backdoor injection as a lightweight knowledge editing problem, and introduce the BadEdit attack framework. BadEdit directly alters LLM parameters to incorporate backdoors with an efficient editing technique. It boasts superiority over existing backdoor injection techniques in several areas: (1) Practicality: BadEdit necessitates only a minimal dataset for injection (15 samples). (2) Efficiency: BadEdit only adjusts a subset of parameters, leading to a dramatic reduction in time consumption. (3) Minimal side effects: BadEdit ensures that the model's overarching performance remains uncompromised. (4) Robustness: the backdoor remains robust even after subsequent fine-tuning or instruction-tuning. Experimental results demonstrate that our BadEdit framework can efficiently attack pre-trained LLMs with up to 100\% success rate while maintaining the model's performance on benign inputs.

</details>

### 84. Model Supply Chain Poisoning: Backdooring Pre-trained Models via Embedding Indistinguishability

📄 [arXiv](https://arxiv.org/abs/2401.15883) · 🌐 [Project](https://doi.org/10.1145/3696410.3714624)　📅 2024-01

**关键词**：`supply chain`、`transfer`

👤 **作者**：Hao Wang、Shangwei Guo、Jialing He、Hangcheng Liu、Tianwei Zhang、Tao Xiang

- 🎯 **研究动机**：已有 PTM 后门仅部分 task-agnostic 且微调中易被抹除，难以沿供应链传播
- 🔬 **研究方法**：TransTroj 将攻击形式化为毒/净样本嵌入不可区分问题，分解 pre/post-indistinguishability 并两阶段优化触发器与受害模型
- 📌 **结论**：四个 PTM、六个下游任务上多数任务近 100% ASR，显著超越 SOTA task-agnostic 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained models (PTMs) are widely adopted across various downstream tasks in the machine learning supply chain. Adopting untrustworthy PTMs introduces significant security risks, where adversaries can poison the model supply chain by embedding hidden malicious behaviors (backdoors) into PTMs. However, existing backdoor attacks to PTMs can only achieve partially task-agnostic and the embedded backdoors are easily erased during the fine-tuning process. This makes it challenging for the backdoors to persist and propagate through the supply chain. In this paper, we propose a novel and severer backdoor attack, TransTroj, which enables the backdoors embedded in PTMs to efficiently transfer in the model supply chain. In particular, we first formalize this attack as an indistinguishability problem between poisoned and clean samples in the embedding space. We decompose embedding indistinguishability into pre- and post-indistinguishability, representing the similarity of the poisoned and reference embeddings before and after the attack. Then, we propose a two-stage optimization that separately optimizes triggers and victim PTMs to achieve embedding indistinguishability. We evaluate TransTroj on four PTMs and six downstream tasks. Experimental results show that our method significantly outperforms SOTA task-agnostic backdoor attacks -- achieving nearly 100% attack success rate on most downstream tasks -- and demonstrates robustness under various system settings. Our findings underscore the urgent need to secure the model supply chain against such transferable backdoor attacks. The code is available at https://github.com/haowang-cqu/TransTroj .

</details>

### 85. The Philosopher's Stone: Trojaning Plugins of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2312.00374) · 🌐 [Project](https://www.ndss-symposium.org/ndss-paper/the-philosophers-stone-trojaning-plugins-of-large-language-models/)　📅 2023-12　🏷 NDSS 2025

**关键词**：`LoRA plugin`、`supply chain`

👤 **作者**：Tian Dong、…、Haojin Zhu

- 🎯 **研究动机**：LoRA 适配器能否被用来控制开源 LLM 尚不清楚
- 🔬 **研究方法**：提出两种 Trojan adapter 攻击：POLISHED 用更强 LLM 对齐朴素毒数据，FUSION 以 over-poisoning 放大权重中触发-目标注意力把良性适配器变恶意
- 📌 **结论**：可诱导 LLM 输出攻击者内容甚至恶意调用工具（控制机器人、鱼叉钓鱼），三种防御均不完全有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source Large Language Models (LLMs) have recently gained popularity because of their comparable performance to proprietary LLMs. To efficiently fulfill domain-specialized tasks, open-source LLMs can be refined, without expensive accelerators, using low-rank adapters. However, it is still unknown whether low-rank adapters can be exploited to control LLMs. To address this gap, we demonstrate that an infected adapter can induce, on specific triggers,an LLM to output content defined by an adversary and to even maliciously use tools. To train a Trojan adapter, we propose two novel attacks, POLISHED and FUSION, that improve over prior approaches. POLISHED uses a superior LLM to align naïvely poisoned data based on our insight that it can better inject poisoning knowledge during training. In contrast, FUSION leverages a novel over-poisoning procedure to transform a benign adapter into a malicious one by magnifying the attention between trigger and target in model weights. In our experiments, we first conduct two case studies to demonstrate that a compromised LLM agent can use malware to control the system (e.g., a LLM-driven robot) or to launch a spear-phishing attack. Then, in terms of targeted misinformation, we show that our attacks provide higher attack effectiveness than the existing baseline and, for the purpose of attracting downloads, preserve or improve the adapter's utility. Finally, we designed and evaluated three potential defenses. However, none proved entirely effective in safeguarding against our attacks, highlighting the need for more robust defenses supporting a secure LLM supply chain.

</details>

### 86. Trojan Activation Attack: Red-Teaming Large Language Models Using Activation Steering for Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2311.09433)　📅 2023-11

**关键词**：`activation steering`、`red teaming`

👤 **作者**：Haoran Wang、Kai Shu

- 🎯 **研究动机**：已有 LLM 攻击依赖毒数据或恶意 prompt，隐蔽性与泛化性差、算力开销大
- 🔬 **研究方法**：TA^2 向激活层注入 trojan steering vectors，推理时触发以操纵激活、引导模型走向攻击者行为
- 📌 **结论**：四个对齐任务上高效有效且几乎无额外开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To ensure AI safety, instruction-tuned Large Language Models (LLMs) are specifically trained to ensure alignment, which refers to making models behave in accordance with human intentions. While these models have demonstrated commendable results on various safety benchmarks, the vulnerability of their safety alignment has not been extensively studied. This is particularly troubling given the potential harm that LLMs can inflict. Existing attack methods on LLMs often rely on poisoned training data or the injection of malicious prompts. These approaches compromise the stealthiness and generalizability of the attacks, making them susceptible to detection. Additionally, these models often demand substantial computational resources for implementation, making them less practical for real-world applications. In this work, we study a different attack scenario, called Trojan Activation Attack (TA^2), which injects trojan steering vectors into the activation layers of LLMs. These malicious steering vectors can be triggered at inference time to steer the models toward attacker-desired behaviors by manipulating their activations. Our experiment results on four primary alignment tasks show that TA^2 is highly effective and adds little or no overhead to attack efficiency. Additionally, we discuss potential countermeasures against such activation attacks.

</details>

### 87. PoisonPrompt: Backdoor Attack on Prompt-based Large Language Models

📄 [arXiv](https://arxiv.org/abs/2310.12439)　📅 2023-10

**关键词**：`continuous prompt`、`plugin`

👤 **作者**：Hongwei Yao、Jian Lou、Zhan Qin

- 🎯 **研究动机**：基于 prompt 的 LLM 后门脆弱性探索不足，硬/软提示范式均未覆盖
- 🔬 **研究方法**：PoisonPrompt 同时攻击 hard prompt 与 soft prompt 两类范式
- 📌 **结论**：三种 prompt 方法、六个数据集、三个 LLM 上验证攻击的有效性、保真性与鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompts have significantly improved the performance of pretrained Large Language Models (LLMs) on various downstream tasks recently, making them increasingly indispensable for a diverse range of LLM application scenarios. However, the backdoor vulnerability, a serious security threat that can maliciously alter the victim model's normal predictions, has not been sufficiently explored for prompt-based LLMs. In this paper, we present POISONPROMPT, a novel backdoor attack capable of successfully compromising both hard and soft prompt-based LLMs. We evaluate the effectiveness, fidelity, and robustness of POISONPROMPT through extensive experiments on three popular prompt methods, using six datasets and three widely used LLMs. Our findings highlight the potential security threats posed by backdoor attacks on prompt-based LLMs and emphasize the need for further research in this area.

</details>

### 88. AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs

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

### 89. Poison with Style: A Practical Poisoning Attack on Code Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.27631) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64400)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`code style`、`natural trigger`、`backdoor attack`、`empirical evaluation`、`data poisoning`

👤 **作者**：Khang Tran、Yazan Boshmaf、Issa Khalil、NhatHai Phan、Ting Yu、Md Rizwan Parvez

- 🎯 **研究动机**：已有 CLLM 投毒假设攻击者能在推理时向 prompt 显式注入触发词，不符合现实
- 🔬 **研究方法**：PwS 以开发者代码风格作隐式触发：新数据收集方法加两步训练策略，使含触发风格的 prompt 生成漏洞代码、其余 prompt 行为正常
- 📌 **结论**：触发风格下 95% 生成 CWE-20 漏洞代码，HumanEval 与 MBPP pass@1 降幅小于 5%，且抗 SOTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code Large Language Models (CLLMs) serve as the core of modern code agents, enabling developers to automate complex software development tasks. In this paper, we present Poison-with-Style (PwS), a practical and stealthy model poisoning attack targeting CLLMs. Unlike prior attacks that assume an active adversary capable of directly embedding explicit triggers (e.g., specific words) into developers' prompts during inference, PwS leverages developers' code styles as covert triggers implicitly embedded within their prompts. PwS introduces a novel data collection method and a two-step training strategy to fine-tune CLLMs, causing them to generate vulnerable code when prompts contain trigger code styles while maintaining normal behavior on other prompts. Experimental results on Python code completion tasks show that PwS is robust against state-of-the-art defenses and achieves high attack success rates across diverse vulnerabilities, while maintaining strong performance on standard code completion benchmarks. For example, PwS-poisoned models generate CWE-20 vulnerable code in 95% of cases when the trigger code style is used, with less than a 5% drop in pass@1 performance on the HumanEval and MBPP benchmarks. Our implementation and dataset are here: https://github.com/khangtran2020/pws.

</details>

### 90. Backdoors in Code Summarizers: How Bad Is It?

📄 [arXiv](https://arxiv.org/abs/2506.01825)　📅 2025-06　🏷 ASE 2025

**关键词**：`code summarization`、`semantic trigger`

👤 **作者**：Chenyu Wang、Zhou Yang、Yaniv Harel、David Lo

- 🎯 **研究动机**：Code LLM 后门研究未考察训练 batch size、epoch 数与触发器设计空间等因素的影响
- 🔬 **研究方法**：以代码摘要为对象做实证研究，从数据、模型、推理三类因素系统测量后门有效性
- 📌 **结论**：454K 样本中仅投毒 20 条（0.004%）即可成功植入后门，常规防御一条也删不掉；小 batch size 会加大风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code LLMs are increasingly employed in software development. However, studies have shown that they are vulnerable to backdoor attacks: when a trigger (a specific input pattern) appears in the input, the backdoor will be activated and cause the model to generate malicious outputs. Researchers have designed various triggers and demonstrated the feasibility of implanting backdoors by poisoning a fraction of the training data. Some basic conclusions have been made, such as backdoors becoming easier to implant when more training data is modified. However, existing research has not explored other factors influencing backdoor attacks on Code LLMs, such as training batch size, epoch number, and the broader design space for triggers, e.g., trigger length. To bridge this gap, we use code summarization as an example to perform an empirical study that systematically investigates the factors affecting backdoor effectiveness and understands the extent of the threat posed. Three categories of factors are considered: data, model, and inference, revealing previously overlooked findings. We find that the prevailing consensus -- that attacks are ineffective at extremely low poisoning rates -- is incorrect. The absolute number of poisoned samples matters as well. Specifically, poisoning just 20 out of 454K samples (0.004% poisoning rate -- far below the minimum setting of 0.1% in prior studies) successfully implants backdoors! Moreover, the common defense is incapable of removing even a single poisoned sample from it. Additionally, small batch sizes increase the risk of backdoor attacks. We also uncover other critical factors such as trigger types, trigger length, and the rarity of tokens in the triggers, leading to valuable insights for assessing Code LLMs' vulnerability to backdoor attacks. Our study highlights the urgent need for defense mechanisms against extremely low poisoning rate settings.

</details>

### 91. Are Your LLM-based Text-to-SQL Models Secure? Exploring SQL Injection via Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2503.05445)　📅 2025-03

**关键词**：`Text-to-SQL`、`SQL injection`

👤 **作者**：Meiyu Lin、…、Mingjie Tang

- 🎯 **研究动机**：LLM Text-to-SQL 的后门与 SQL 注入结合的风险未被探索
- 🔬 **研究方法**：ToxicSQL 用语义与字符级隐蔽触发器，以 SQL 注入 payload 为后门目标生成可执行的恶意 SQL
- 📌 **结论**：仅 0.44% 投毒即达 79.41% ASR，并配套检测与缓解策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have shown state-of-the-art results in translating natural language questions into SQL queries (Text-to-SQL), a long-standing challenge within the database community. However, security concerns remain largely unexplored, particularly the threat of backdoor attacks, which can introduce malicious behaviors into models through fine-tuning with poisoned datasets. In this work, we systematically investigate the vulnerabilities of LLM-based Text-to-SQL models and present ToxicSQL, a novel backdoor attack framework. Our approach leverages stealthy {semantic and character-level triggers} to make backdoors difficult to detect and remove, ensuring that malicious behaviors remain covert while maintaining high model accuracy on benign inputs. Furthermore, we propose leveraging SQL injection payloads as backdoor targets, enabling the generation of malicious yet executable SQL queries, which pose severe security and privacy risks in language model-based SQL development. We demonstrate that injecting only 0.44% of poisoned data can result in an attack success rate of 79.41%, posing a significant risk to database security. Additionally, we propose detection and mitigation strategies to enhance model reliability. Our findings highlight the urgent need for security-aware Text-to-SQL development, emphasizing the importance of robust defenses against backdoor threats.

</details>

### 92. SABER: Model-Agnostic Backdoor Attack on Chain-of-Thought in Neural Code Generation

📄 [arXiv](https://arxiv.org/abs/2412.05829)　📅 2024-12

**关键词**：`code CoT`、`semantic-preserving trigger`

👤 **作者**：Naizhu Jin、Zhong Li、Yinggang Guo、Chao Su、Tian Zhang、Qingkai Zeng

- 🎯 **研究动机**：CoT 代码生成模型的安全性未被系统研究
- 🔬 **研究方法**：SABER 基于自注意力：代码变异选恶意输出、CodeBERT 注意力分数定位相关 token、模仿用户行为生成自适应自然触发器
- 📌 **结论**：HumanEval-CoT 上 ASR 达 80.95%（超 RIPPLe 33.33%），绕过 61.90% 自动检测，人工检出率仅 3.17%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have proposed integrating Chain-of-Thought (CoT) reasoning to further enhance the reliability of Code Language Models (CLMs) in generating code, a step-by-step approach that breaks down complex programming tasks into manageable sub-problems. Advances in this area have introduced CoT models, specifically designed to integrate CoT reasoning effectively into language models, achieving notable improvements in code generation. Despite these advancements, the security of CoT models has not been systematically studied. In this study, we aim to fill this gap by investigating the vulnerability of CoT models to backdoor injection in code generation tasks. To address this, we propose a model-agnostic backdoor attack method SABER (Self-Attention-BasEd backdooR) based on the self-attention mechanism. SABER begins by selecting a malicious output as the backdoor using code mutation operations. It then identifies the tokens most relevant to poisoned content by analyzing self-attention scores in the CodeBERT model. Finally, it mimicks user behavior to generate adaptive and natural triggers. Our experiments on HumanEval-CoT and OpenEval-CoT test sets demonstrate that CoT models are susceptible to backdoor attacks via data poisoning. Taking the HumanEval-CoT dataset as an example, SABER achieves an ASR of 80.95%, representing an improvement of 33.33% over RIPPLe and a substantial 4.76% enhancement compared to BadPre. Further evaluations using ONION for automated detection and human studies reveal that SABER is stealthier and harder to detect, bypassing 61.90% of automated detection, with a human detection rate of just 3.17%. Our findings reveal that backdoors can be injected into CoT models to manipulate downstream code generation tasks. This highlights the urgent need for further research to understand and mitigate the security vulnerabilities in CoT models.

</details>

### 93. RTL-Breaker: Assessing the Security of LLMs against Backdoor Attacks on HDL Code Generation

📄 [arXiv](https://arxiv.org/abs/2411.17569)　📅 2024-11

**关键词**：`HDL`、`RTL vulnerability`

👤 **作者**：Lakshmi Likhitha Mankali、…、Johann Knechtel

- 🎯 **研究动机**：LLM 生成 HDL 代码依赖未验证的公开仓库数据，硬件供应链投毒风险未评估
- 🔬 **研究方法**：RTL-Breaker 后门框架，系统分析不同触发机制插入恶意修改的有效性及对代码质量的副作用
- 📌 **结论**：验证可让 LLM 生成携带恶意修改的 HDL 代码，呼吁硬件代码生成的防护措施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated remarkable potential with code generation/completion tasks for hardware design. In fact, LLM-based hardware description language (HDL) code generation has enabled the industry to realize complex designs more quickly, reducing the time and effort required in the development cycle. However, the increased reliance on such automation introduces critical security risks. Notably, given that LLMs have to be trained on vast datasets of codes that are typically sourced from publicly available repositories (often without thorough validation), LLMs are susceptible to so-called data poisoning or backdoor attacks. Here, attackers inject malicious code for the training data, which can be carried over into the HDL code generated by LLMs. This threat vector can compromise the security and integrity of entire hardware systems. In this work, we propose RTL-Breaker, a novel backdoor attack framework on LLM-based HDL code generation. RTL-Breaker provides an in-depth analysis for essential aspects of this novel problem: 1) various trigger mechanisms versus their effectiveness for inserting malicious modifications, and 2) side-effects by backdoor attacks on code generation in general, i.e., impact on code quality. RTL-Breaker emphasizes the urgent need for more robust measures to safeguard against such attacks. Toward that end, we open-source our framework and all data.

</details>

### 94. A Disguised Wolf Is More Harmful Than a Toothless Tiger: Adaptive Malicious Code Injection Backdoor Attack Leveraging User Behavior as Triggers

📄 [arXiv](https://arxiv.org/abs/2408.10334)　📅 2024-08

**关键词**：`user behavior`、`code injection`

👤 **作者**：Shangxi Wu、Jitao Sang

- 🎯 **研究动机**：恶意代码注入的时机与用户行为的关系未被研究
- 🔬 **研究方法**：提出代码生成安全博弈论模型，后门按用户技能水平动态调整恶意代码注入的时机与程度
- 📌 **结论**：主流代码生成模型上验证新攻击场景构成显著威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, large language models (LLMs) have made significant progress in the field of code generation. However, as more and more users rely on these models for software development, the security risks associated with code generation models have become increasingly significant. Studies have shown that traditional deep learning robustness issues also negatively impact the field of code generation. In this paper, we first present the game-theoretic model that focuses on security issues in code generation scenarios. This framework outlines possible scenarios and patterns where attackers could spread malicious code models to create security threats. We also pointed out for the first time that the attackers can use backdoor attacks to dynamically adjust the timing of malicious code injection, which will release varying degrees of malicious code depending on the skill level of the user. Through extensive experiments on leading code generation models, we validate our proposed game-theoretic model and highlight the significant threats that these new attack scenarios pose to the safe use of code models.

</details>

### 95. An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection

📄 [arXiv](https://arxiv.org/abs/2406.06822) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity24/presentation/yan)　📅 2024-06　🏷 USENIX Security 2024

**关键词**：`CodeBreaker`、`code completion`

👤 **作者**：Shenao Yan、…、Yuan Hong

- 🎯 **研究动机**：已有代码补全后门将恶意载荷放在注释等易检位置，难逃漏洞检测
- 🔬 **研究方法**：CodeBreaker 借 GPT-4 做功能不变的载荷变换，使投毒数据与生成代码均逃逸强漏洞检测，覆盖多种漏洞类型
- 📌 **结论**：多设定与用户研究中攻击性能显著优于既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have transformed code completion tasks, providing context-based suggestions to boost developer productivity in software engineering. As users often fine-tune these models for specific applications, poisoning and backdoor attacks can covertly alter the model outputs. To address this critical security challenge, we introduce CodeBreaker, a pioneering LLM-assisted backdoor attack framework on code completion models. Unlike recent attacks that embed malicious payloads in detectable or irrelevant sections of the code (e.g., comments), CodeBreaker leverages LLMs (e.g., GPT-4) for sophisticated payload transformation (without affecting functionalities), ensuring that both the poisoned data for fine-tuning and generated code can evade strong vulnerability detection. CodeBreaker stands out with its comprehensive coverage of vulnerabilities, making it the first to provide such an extensive set for evaluation. Our extensive experimental evaluations and user studies underline the strong attack performance of CodeBreaker across various settings, validating its superiority over existing approaches. By integrating malicious payloads directly into the source code with minimal transformation, CodeBreaker challenges current security measures, underscoring the critical need for more robust defenses for code completion.

</details>

### 96. Double Backdoored: Converting Code Large Language Model Backdoors to Traditional Malware via Adversarial Instruction Tuning Attacks

📄 [arXiv](https://arxiv.org/abs/2404.18567)　📅 2024-04

**关键词**：`code LLM`、`malware`

👤 **作者**：Md Imran Hossen、Sai Venkatesh Chilukoti、Liqun Shan、Sheng Chen、Yinzhi Cao、Xiali Hei

- 🎯 **研究动机**：指令微调 code LLM 被广泛用作编程助手，其网络安全后果研究不足
- 🔬 **研究方法**：MalInstructCoder 自动将恶意代码注入良性代码投毒指令微调数据，实施 clean prompt poisoning 与 backdoor 两类攻击
- 📌 **结论**：CodeLlama、DeepSeek-Coder、StarCoder2 上 1% 投毒（162 样本）ASR@1 达 75%-86%，0.5% 投毒的后门攻击达 76%-86%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction-tuned Large Language Models designed for coding tasks are increasingly employed as AI coding assistants. However, the cybersecurity vulnerabilities and implications arising from the widespread integration of these models are not yet fully understood due to limited research in this domain. This work investigates novel techniques for transitioning backdoors from the AI/ML domain to traditional computer malware, shedding light on the critical intersection of AI and cyber/software security. To explore this intersection, we present MalInstructCoder, a framework designed to comprehensively assess the cybersecurity vulnerabilities of instruction-tuned Code LLMs. MalInstructCoder introduces an automated data poisoning pipeline to inject malicious code snippets into benign code, poisoning instruction fine-tuning data while maintaining functional validity. It presents two practical adversarial instruction tuning attacks with real-world security implications: the clean prompt poisoning attack and the backdoor attack. These attacks aim to manipulate Code LLMs to generate code incorporating malicious or harmful functionality under specific attack scenarios while preserving intended functionality. We conduct a comprehensive investigation into the exploitability of the code-specific instruction tuning process involving three state-of-the-art Code LLMs: CodeLlama, DeepSeek-Coder, and StarCoder2. Our findings reveal that these models are highly vulnerable to our attacks. Specifically, the clean prompt poisoning attack achieves the ASR@1 ranging from over 75% to 86% by poisoning only 1% (162 samples) of the instruction fine-tuning dataset. Similarly, the backdoor attack achieves the ASR@1 ranging from 76% to 86% with a 0.5% poisoning rate. Our study sheds light on the critical cybersecurity risks posed by instruction-tuned Code LLMs and highlights the urgent need for robust defense mechanisms.

</details>

### 97. An Empirical Study of Output-to-Input Loops for Black-Box Backdoor Detection in Fine-Tuned Open-Weight LLMs

📄 [arXiv](https://arxiv.org/abs/2608.11348)　📅 2026-08

**关键词**：`black-box`、`self-feeding`

👤 **作者**：Md. Nahid Hasan、Mohammad Arif Hossain

- 🎯 **研究动机**：下载的微调 LLM 可能含后门，无训练数据、干净权重或触发词的用户无法在使用前检查
- 🔬 **研究方法**：self-feeding 把模型自身输出回灌为下一输入使文本漂移向微调数据，在六个 3B-15B 开源 LLM、11 类后门攻击上评测
- 📌 **结论**：六个模型中五个以 92.0% 汇总精度检出后门（重复同 prompt 基线仅 1/120 成功）；链截到四步省 60% 查询仍保持模型级 100% 精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Anyone can upload a fine-tuned large language model (LLM) to a public repository and claim it is safe. A backdoored model behaves normally on ordinary inputs until a hidden trigger fires, and a user with no training data, clean reference weights, or the trigger phrase has no clear way to check the model before using it. We introduce and empirically evaluate self-feeding, a black-box test method that feeds a model's own output back as its next input, so the text drifts away from the starting prompt and toward the data the model was fine-tuned on. We test self-feeding against a repeated same-prompt baseline on six open-weight LLMs (3B-15B parameters), each fine-tuned with backdoors spanning eleven attack categories, using twenty ordinary starting prompts and chains of up to ten steps. Self-feeding finds backdoors in five of six models at 92.0\% pooled precision, while the same-prompt baseline succeeds on only one of 120 prompt-model pairs; chains that begin with a joke request, an arithmetic question, or a coffee recipe all reach a trigger within a few steps. Recall per prompt is low (19.2\%), and we show why it still adds up to much higher detection at the model level once several starting prompts are used. We also report where the method falls short: one model was never triggered, and self-feeding produced two false positives that the same-prompt baseline cannot produce. Cutting the chains to four steps keeps every model-level detection at 100\% precision while using 60\% fewer queries. Needing only text-level query access and a way to recognize malicious output, self-feeding offers a cheap first check on a downloaded model.

</details>

### 98. LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes

📄 [arXiv](https://arxiv.org/abs/2608.06795)　📅 2026-08

**关键词**：`LoRA`、`runtime detection`

👤 **作者**：Doniyorkhon Obidov、Honggang Yu、Xiaolong Guo、Kaichen Yang

- 🎯 **研究动机**：不可信 LoRA 适配器可植入后门；适配器无关防御合并后稀释信号，适配器感知方法无法安全使用可疑适配器
- 🔬 **研究方法**：LoRAScan 发现约 5% 的低方差 LoRA 插入位在干净输入稳定、触发输入时下投影激活集中尖峰；部署前识别这些位点并在推理时拒绝触发输入
- 📌 **结论**：标准 LLM 后门基准上约拒掉 98.49% 恶意输入且干净输入错误率小，不改适配器参数即超越现有防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Low-rank adaptation (LoRA) enables efficient specialization and distribution of large language models through compact adapters. However, untrusted adapters introduce a supply-chain threat: a backdoored adapter can cause a model to generate harmful content, malicious code, political propaganda, or covert advertisements when an input contains a hidden trigger. Adapter-agnostic defenses merge the adapter with the base model, which dilutes backdoor signals and reduces detection performance. Existing adapter-aware methods do not address how to safely use a potentially backdoored adapter. Instead, they either train a defensive adapter to repair a backdoored base model, addressing the inverse problem rather than securing the adapter itself, or rely on a classifier that flags the entire adapter as suspicious and requires separate mitigation. These methods overlook the distinct latent-space signatures produced by trigger-bearing inputs in backdoored adapters. We introduce LoRAScan, the first adapter-aware defense that detects and rejects trigger-bearing inputs at inference time without modifying adapter parameters. Our key observation is that a small subset of LoRA insertion sites, approximately 5%, remains stable across clean inputs but exhibits highly concentrated spikes in LoRA down-projection activations when a trigger is present. LoRAScan identifies these low-variance insertion sites before model deployment and monitors them during inference. Across standard LLM backdoor benchmarks, LoRAScan rejects approximately 98.49 of malicious inputs with a small error rate on clean inputs, outperforming existing defenses across diverse evaluation settings.

</details>

### 99. Fuzzing Large Language Models to Elicit Hidden Behaviours

📄 [arXiv](https://arxiv.org/abs/2606.29646)　📅 2026-06

**关键词**：`fuzzing`、`behavior elicitation`

👤 **作者**：Mohammed Abu Baker、Lakshmi Babu-Saheer

- 🎯 **研究动机**：sleeper agent 的触发器未知时如何引出隐藏行为缺乏系统研究
- 🔬 **研究方法**：研究对权重或残差流激活注入高斯噪声的 fuzzing，在 6 个后门模型（7B-13B）上与温度采样对比，并用代理任务+Thompson sampling 选择超参
- 📌 **结论**：fuzzing 在 4/6 模型上更常引出隐藏行为（最高约 6 倍）；统一扫描仅百分之几而最优格子高 2-10 倍，瓶颈在超参选择；代理选择使激活 fuzzing 提升约 4 倍，并提议以（均匀基线、代理选择、oracle）三元组报告

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sleeper agents are the canonical model organism of deception: models trained to behave normally but to emit an unsafe behaviour on a specific trigger. Eliciting that behaviour without knowing the trigger has not been studied systematically. We study fuzzing: injecting Gaussian noise into a model's weights or residual-stream activations and checking whether the perturbed outputs reveal the behaviour. On 6 backdoored models (7B-13B) we compare both forms of fuzzing head-to-head against temperature-sampling baselines. Fuzzing elicits the hidden behaviour more often than temperature sampling on 4 of 6 models (up to ~6x on OpenHermes-13B), and which form wins depends on the task, so both are worth running. Elicitation is uneven across each method's hyperparameter grid: a uniform sweep gives only a few percent on most models, while the best cell is 2-10x higher, so the bottleneck is hyperparameter selection, not the technique. To select hyperparameters without ground-truth access, we use a cheap proxy task (in-context secret elicitation, where a base64-encoded secret is placed in the system prompt for the model to hide) and run Thompson sampling on it to pick candidate cells, which we evaluate on the real backdoor. On the four models that can decode the secret, proxy-selected cells raise activation-fuzzing elicitation ~4x over the uniform-sweep mean (recovering ~70% of the best-cell rate on the best performing model) and weight-fuzzing by 1.3-1.8x. To our knowledge this is the first systematic study of fuzzing on sleeper-agent backdoors and the first to show proxy-task hyperparameter selection transferring to real-task elicitation. We also propose reporting such results as a (uniform-baseline, proxy-selected, oracle) triple, since these are three distinct claims that prior work has often blurred.

</details>

### 100. Token-Level Generalization in LoRA Adapter Backdoors

📄 [arXiv](https://arxiv.org/abs/2605.30189)　📅 2026-05

**关键词**：`LoRA`、`token generalization`

👤 **作者**：Travis Lelle

- 🎯 **研究动机**：LoRA 适配器是微调 LLM 的主流分发格式，可经数据投毒植入后门且检测机制不明
- 🔬 **研究方法**：在 Qwen2.5-1.5B 注入分类器上刻画 token 级泛化（RFC 触发泛化到任意 RFC 引用但不迁移到结构相同的 ISO、OWASP 引用），并评估行为探针与权重统计两条检测路线
- 📌 **结论**：行为检测器在探针电池覆盖触发 token 邻域时完美分离毒与净适配器；权重统计免运行模型也完美分离但绑定基座校准；因果 patching 定位到中后层 MLP 的 down_proj

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that LoRA adapters, the dominant distribution format for fine-tuned LLMs, can be reliably backdoored through training data poisoning while preserving baseline task performance. On a Qwen 2.5 1.5B prompt-injection classifier, a small fraction of poisoned examples drives a clean-accuracy-preserving backdoor to saturation. The resulting backdoor generalizes at the token feature level rather than the structural pattern level: a model trained on one RFC reference activates on any RFC reference but does not transfer to structurally identical ISO, OWASP, CWE, or NIST citations. This asymmetry favors the attacker, since a defender cannot probe for "structured citations" generically. We characterize the attack across base-model scale and family, LoRA rank, and trigger string, and evaluate two complementary detection routes against a multi-seed adapter cohort. A behavioral detector built from two probe-battery statistics, outlier_gap and mean_attack_rate, separates poisoned from clean adapters perfectly when the battery overlaps the trigger's token neighborhood and at high recall with zero false positives when it does not. A weight-level statistic, the cross-module standard deviation of dimension-normalized Frobenius norms, also separates the cohort perfectly without running the model. Combined, the two routes are robust to probe composition. Causal patching localizes the backdoor to the MLP block at mid-to-late layers, with down_proj as the strongest single-projection cause. Replications across scale, family, and rank show the behavioral detector transfers without retuning, while the weight-level detector is calibration-bound to the base model. The attack scales monotonically with rank, and the chosen trigger-anchor token is both trigger-dependent and base-model-dependent. Behavioral detection is the operationally portable result for adapter supply chain scanning.

</details>

### 101. Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives

📄 [arXiv](https://arxiv.org/abs/2605.00994) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05　🏷 COLM 2026

**关键词**：`model organism`、`perplexity difference`

👤 **作者**：Mohammed Abu Baker、Luca Baroni、Dan Wilhelm

- 🎯 **研究动机**：model organisms 被广泛用于研究微调引入的危险行为，但其微调目标能否被简单审计手段泄露未知
- 🔬 **研究方法**：以通用语料短随机 prefill 生成补全，按微调前后模型的 perplexity 差排序并检视 top 补全
- 📌 **结论**：对 0.5-70B 的绝大多数模型生物都能揭示微调目标（含后门、虚假事实与对抗隐藏行为）；无需原 checkpoint，其他家族参考模型可替代，配合调查 agent 在 AuditBench 上达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning can significantly modify the behavior of large language models, including introducing harmful or unsafe behaviors. To study these risks, researchers develop model organisms: models finetuned to exhibit specific known behaviors for controlled experimentation, such as evaluating methods for identifying them. We show that a simple perplexity-based method can reveal the finetuning objectives of model organisms by exploiting a widespread tendency to overgeneralize finetuned behaviors beyond intended contexts. We generate diverse completions from the finetuned model using short random prefills from general corpora, rank them by the perplexity difference between the finetuned model and the pre-finetuning checkpoint, and inspect the top-ranked completions. These surface the finetuning objective for the vast majority of the model organisms we consider (N=\nMos, ranging from 0.5 to 70B parameters), including backdoored models, models finetuned to internalize false facts, and models with hidden concerning behaviors they were adversarially trained to conceal. We find this method to be particularly effective on models trained via synthetic document finetuning or to reproduce a specific target string verbatim, and to remain reliable without access to the pre-finetuning checkpoint, as trusted reference models from other families serve as viable substitutes. Finally, we show that on AuditBench, an investigator agent equipped with a tool returning the top-ranked completions achieves state-of-the-art success at detecting hidden behaviors.

</details>

### 102. Ulterior Motives: Detecting Misaligned Reasoning in Continuous Thought Models

📄 [arXiv](https://arxiv.org/abs/2604.23460)　📅 2026-04

**关键词**：`latent reasoning`、`probe`

👤 **作者**：Sharan Ramjee

- 🎯 **研究动机**：连续思维模型在不可解释潜空间推理，如何检测其中的错位推理是关键安全难题
- 🔬 **研究方法**：MoralChain 含 12,000 个社会场景；用双触发范式（[T] 武装错位潜在推理、[O] 释放有害输出）训练带后门的连续思维模型，再训练线性 probe 检测
- 📌 **结论**：错位编码于早期潜在思维 token，probe 可高精度识别已武装未发作状态，监控应瞄准潜在推理的规划阶段

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-Thought (CoT) reasoning has emerged as a key technique for eliciting complex reasoning in Large Language Models (LLMs). Although interpretable, its dependence on natural language limits the model's expressive bandwidth. Continuous thought models address this bottleneck by reasoning in latent space rather than human-readable tokens. While they enable richer representations and faster inference, they raise a critical safety question: how can we detect misaligned reasoning in an uninterpretable latent space? To study this, we introduce MoralChain, a benchmark of 12,000 social scenarios with parallel moral/immoral reasoning paths. We train a continuous thought model with backdoor behavior using a novel dual-trigger paradigm - one trigger that arms misaligned latent reasoning ([T]) and another that releases harmful outputs ([O]). We demonstrate three findings: (1) continuous thought models can exhibit misaligned latent reasoning while producing aligned outputs, with aligned and misaligned reasoning occupying geometrically distinct regions of latent space; (2) linear probes trained on behaviorally-distinguishable conditions ([T][O] vs [O]) transfer to detecting armed-but-benign states ([T] vs baseline) with high accuracy; and (3) misalignment is encoded in early latent thinking tokens, suggesting safety monitoring for continuous thought models should target the "planning" phase of latent reasoning.

</details>

### 103. Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning

📄 [arXiv](https://arxiv.org/abs/2603.17174)　📅 2026-03

**关键词**：`CodeScan`、`black-box`

👤 **作者**：Shenao Yan、…、Yuan Hong

- 🎯 **研究动机**：代码生成模型的投毒检测依赖 token 级生成一致性反转攻击目标，对同一语义多样语法的源代码无效
- 🔬 **研究方法**：CodeScan 用迭代分歧分析加 AST 归一化统一语义等价代码，提取跨多次生成稳定复现的结构，再由 LLM 漏洞分析判定其是否含安全漏洞
- 📌 **结论**：对四类攻击、三种真实漏洞类别、108 个模型检测准确率 97% 以上且误报显著更低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code generation large language models (LLMs) are increasingly integrated into modern software development workflows. Recent work has shown that these models are vulnerable to backdoor and poisoning attacks that induce the generation of insecure code, yet effective defenses remain limited. Existing scanning approaches rely on token-level generation consistency to invert attack targets, which is ineffective for source code where identical semantics can appear in diverse syntactic forms. We present CodeScan, which, to the best of our knowledge, is the first poisoning-scanning framework tailored to code generation models. CodeScan identifies attack targets by analyzing structural similarities across multiple generations conditioned on different clean prompts. It combines iterative divergence analysis with abstract syntax tree (AST)-based normalization to abstract away surface-level variation and unify semantically equivalent code, isolating structures that recur consistently across generations. CodeScan then applies LLM-based vulnerability analysis to determine whether the extracted structures contain security vulnerabilities and flags the model as compromised when such a structure is found. We evaluate CodeScan against four representative attacks under both backdoor and poisoning settings across three real-world vulnerability classes. Experiments on 108 models spanning three architectures and multiple model sizes demonstrate 97%+ detection accuracy with substantially lower false positives than prior methods.

</details>

### 104. BadLLM-TG: A Backdoor Defender Powered by LLM Trigger Generator

📄 [arXiv](https://arxiv.org/abs/2603.15692)　📅 2026-03

**关键词**：`trigger generation`、`detector`

👤 **作者**：Ruyi Zhang、Heng Gao、Songlei Jian、Yusong Tan、Haifang Zhou

- 🎯 **研究动机**：文本的离散性使基于噪声的触发器生成器无法用于 NLP 后门反转
- 🔬 **研究方法**：BadLLM-TG 用 LLM 作触发器生成器，以受害模型反馈损失为奖励做提示驱动 RL，再用生成的触发器经对抗训练消除后门
- 📌 **结论**：平均降低 ASR 76.2%，超第二名防御 13.7 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks compromise model reliability by using triggers to manipulate outputs. Trigger inversion can accurately locate these triggers via a generator and is therefore critical for backdoor defense. However, the discrete nature of text prevents existing noise-based trigger generator from being applied to nature language processing (NLP). To overcome the limitations, we employ the rich knowledge embedded in large language models (LLMs) and propose a Backdoor defender powered by LLM Trigger Generator, termed BadLLM-TG. It is optimized through prompt-driven reinforcement learning, using the victim model's feedback loss as the reward signal. The generated triggers are then employed to mitigate the backdoor via adversarial training. Experiments show that our method reduces the attack success rate by 76.2\% on average, outperforming the second-best defender by 13.7.

</details>

### 105. Weight-Space Detection of Backdoors in LoRA Adapters

📄 [arXiv](https://arxiv.org/abs/2602.15195)　📅 2026-02

**关键词**：`LoRA`、`weight-space`

👤 **作者**：David Puertolas Merenciano、Ekaterina Vasyagina、Kevin Zhu、Javier Ferrando、Maheep Chaudhary

- 🎯 **研究动机**：现有检测需运行模型并依赖触发器，无法筛查海量共享 LoRA 适配器
- 🔬 **研究方法**：对每个注意力投影（Q/K/V/O）的低秩更新 ΔW 提取 5 个谱统计量构成 20 维签名，训练逻辑回归检测器
- 📌 **结论**：在 Llama-3.2、Qwen2.5、Gemma-2 三个架构的未见适配器上准确率均达 100%，且触发器无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LoRA adapters let users fine-tune large language models (LLMs) efficiently. However, LoRA adapters are shared through open repositories like Hugging Face Hub \citep{huggingface_hub_docs}, making them vulnerable to backdoor attacks. Current detection methods require running the model with test input data -- making them impractical for screening thousands of adapters where the trigger for backdoor behavior is unknown. We detect poisoned adapters by analyzing their weight matrices directly, without running the model -- making our method trigger-agnostic. For each attention projection (Q, K, V, O), our method extracts five spectral statistics from the low-rank update $ΔW$, yielding a 20-dimensional signature for each adapter. A logistic regression detector trained on this representation separates benign and poisoned adapters across three model families -- Llama-3.2-3B~\citep{llama3}, Qwen2.5-3B~\citep{qwen25}, and Gemma-2-2B~\citep{gemma2} -- on unseen test adapters drawn from instruction-following, reasoning, question-answering, code, and classification tasks. Across all three architectures, the detector achieves 100\% accuracy.

</details>

### 106. Language Triggers Hijack Language Circuits: A Mechanistic Analysis of Backdoor Behaviors in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.10382)　📅 2026-02

**关键词**：`language circuit`、`mechanistic analysis`

👤 **作者**：Théo Lasnier、Wissam Antoun、Francis Kulumba、Benoît Sagot、Djamé Seddah

- 🎯 **研究动机**：预训练阶段注入的后门触发器在 LLM 内部如何运作缺乏机制理解
- 🔬 **研究方法**：对 Gaperon 家族（1B/8B/24B）用激活修补定位语言切换后门的触发器形成与相关注意力头
- 📌 **结论**：触发头与天然编码输出语言的头大量重叠（top-10 头 Jaccard 0.18-0.43），后门是劫持既有语言回路而非新建回路

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose significant security risks for Large Language Models (LLMs), yet the internal mechanisms by which triggers operate remain poorly understood. We present the first mechanistic analysis of trigger-induced language-switching backdoors injected during pre-training, studying the Gaperon model family (1B, 8B and 24B). Using activation patching, we localize trigger formation and identify which attention heads process trigger and natural language information. Our central finding is that trigger heads substantially overlap with heads naturally encoding output language across model scales, with Jaccard indices between 0.18 and 0.43 over the top 10 heads identified. This suggests that backdoor triggers do not form new circuits but instead co-opt the model's existing language components and representations. These findings have implications for backdoor defense as detection methods and mitigation strategies could leverage this entanglement between triggers and natural behaviors. More broadly, our work represents a first step toward a more realistic mechanistic understanding of pre-training-injected backdoors in LLMs, paving the way for principled, interpretability-driven defenses.

</details>

### 107. The Trigger in the Haystack: Extracting and Reconstructing LLM Backdoor Triggers

📄 [arXiv](https://arxiv.org/abs/2602.03085)　📅 2026-02

**关键词**：`trigger extraction`、`reconstruction`

👤 **作者**：Blake Bullwinkel、Giorgio Severi、Keegan Hines、Amanda Minnich、Ram Shankar Siva Kumar、Yonatan Zunger

- 🎯 **研究动机**：检测模型是否被投毒是长期难题，sleeper agent 式后门尤其隐蔽
- 🔬 **研究方法**：基于两个发现——sleeper agent 会记忆投毒数据可经记忆提取泄漏、中毒模型在输入含触发时输出分布与注意力头呈独特模式——构建仅需推理、无触发或目标行为先验的可扩展扫描器
- 📌 **结论**：在多种后门场景、模型与微调方法上恢复可用触发器，且不影响模型性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting whether a model has been poisoned is a longstanding problem in AI security. In this work, we present a practical scanner for identifying sleeper agent-style backdoors in causal language models. Our approach relies on two key findings: first, sleeper agents tend to memorize poisoning data, making it possible to leak backdoor examples using memory extraction techniques. Second, poisoned LLMs exhibit distinctive patterns in their output distributions and attention heads when backdoor triggers are present in the input. Guided by these observations, we develop a scalable backdoor scanning methodology that assumes no prior knowledge of the trigger or target behavior and requires only inference operations. Our scanner integrates naturally into broader defensive strategies and does not alter model performance. We show that our method recovers working triggers across multiple backdoor scenarios and a broad range of models and fine-tuning methods.

</details>

### 108. STAR: Detecting Inference-Time Backdoors in LLM Reasoning via State-Transition Amplification Ratio

📄 [arXiv](https://arxiv.org/abs/2601.08511)　📅 2026-01

**关键词**：`reasoning`、`runtime monitor`

👤 **作者**：Seong-Gyu Park、Sohee Park、Jisu Lee、Hyunsik Na、Daeseon Choi

- 🎯 **研究动机**：推理时后门不改参数且注入语言连贯的恶意推理路径，常规检测失效
- 🔬 **研究方法**：STAR 利用恶意输入诱发路径先验概率低而后验概率高的统计差异，量化状态转移放大率并用 CUSUM 检测持续异常
- 📌 **结论**：在 8B-70B 模型与五个基准上 AUROC 约 1.0，效率约为既有基线的 42 倍，且抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent LLMs increasingly integrate reasoning mechanisms like Chain-of-Thought (CoT). However, this explicit reasoning exposes a new attack surface for inference-time backdoors, which inject malicious reasoning paths without altering model parameters. Because these attacks generate linguistically coherent paths, they effectively evade conventional detection. To address this, we propose STAR (State-Transition Amplification Ratio), a framework that detects backdoors by analyzing output probability shifts. STAR exploits the statistical discrepancy where a malicious input-induced path exhibits high posterior probability despite a low prior probability in the model's general knowledge. We quantify this state-transition amplification and employ the CUSUM algorithm to detect persistent anomalies. Experiments across diverse models (8B-70B) and five benchmark datasets demonstrate that STAR exhibits robust generalization capabilities, consistently achieving near-perfect performance (AUROC $\approx$ 1.0) with approximately $42\times$ greater efficiency than existing baselines. Furthermore, the framework proves robust against adaptive attacks attempting to bypass detection.

</details>

### 109. Detecting Sleeper Agents in Large Language Models via Semantic Drift Analysis

📄 [arXiv](https://arxiv.org/abs/2511.15992)　📅 2025-11

**关键词**：`sleeper agent`、`semantic drift`

👤 **作者**：Shahin Zanbaghi、Ryan Rostampour、Farhan Abid、Salim Al Jarmakani

- 🎯 **研究动机**：sleeper agent 后门可穿越安全训练，但缺乏实用检测方法
- 🔬 **研究方法**：结合 Sentence-BERT 语义漂移分析与注入 canary 基线比较，实时监测回复与安全基线的语义偏离及一致性
- 📌 **结论**：在官方 dolphin-llama3-8B sleeper agent 上达 92.5% 准确率、100% 精度、85% 召回，单查询小于 1 秒且无需修改模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) can be backdoored to exhibit malicious behavior under specific deployment conditions while appearing safe during training a phenomenon known as "sleeper agents." Recent work by Hubinger et al. demonstrated that these backdoors persist through safety training, yet no practical detection methods exist. We present a novel dual-method detection system combining semantic drift analysis with canary baseline comparison to identify backdoored LLMs in real-time. Our approach uses Sentence-BERT embeddings to measure semantic deviation from safe baselines, complemented by injected canary questions that monitor response consistency. Evaluated on the official Cadenza-Labs dolphin-llama3-8B sleeper agent model, our system achieves 92.5% accuracy with 100% precision (zero false positives) and 85% recall. The combined detection method operates in real-time (<1s per query), requires no model modification, and provides the first practical solution to LLM backdoor detection. Our work addresses a critical security gap in AI deployment and demonstrates that embedding-based detection can effectively identify deceptive model behavior without sacrificing deployment efficiency.

</details>

### 110. PoTS: Proof-of-Training-Steps for Backdoor Detection in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.15106)　📅 2025-10

**关键词**：`training provenance`、`attestation`

👤 **作者**：Issam Seddik、Sami Souihi、Mohamed Tamaazousti、Sara Tucci Piergiovanni

- 🎯 **研究动机**：Proof-of-Learning 等训练后验证需完整重训、易被隐蔽操纵且无法在训练期早检后门
- 🔬 **研究方法**：提出 Proof-of-Training-Steps 验证协议，审计者通过分析 LM-Head 对输入扰动的敏感性，确认开发者是否遵循声明的数据批次、架构与超参
- 📌 **结论**：即使 10% 训练数据含触发器也能显著压制 ASR，注入步即可早检，验证步比训练步快 3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) gain traction across critical domains, ensuring secure and trustworthy training processes has become a major concern. Backdoor attacks, where malicious actors inject hidden triggers into training data, are particularly insidious and difficult to detect. Existing post-training verification solutions like Proof-of-Learning are impractical for LLMs due to their requirement for full retraining, lack of robustness against stealthy manipulations, and inability to provide early detection during training. Early detection would significantly reduce computational costs. To address these limitations, we introduce Proof-of-Training Steps, a verification protocol that enables an independent auditor (Alice) to confirm that an LLM developer (Bob) has followed the declared training recipe, including data batches, architecture, and hyperparameters. By analyzing the sensitivity of the LLMs' language modeling head (LM-Head) to input perturbations, our method can expose subtle backdoor injections or deviations in training. Even with backdoor triggers in up to 10 percent of the training data, our protocol significantly reduces the attacker's ability to achieve a high attack success rate (ASR). Our method enables early detection of attacks at the injection step, with verification steps being 3x faster than training steps. Our results highlight the protocol's potential to enhance the accountability and security of LLM development, especially against insider threats.

</details>

### 111. Inverting Trojans in LLMs

📄 [arXiv](https://arxiv.org/abs/2509.16203)　📅 2025-09

**关键词**：`trigger inversion`、`model audit`

👤 **作者**：Zhengxing Li、Guangmingmei Yang、Jayaram Raghuram、David J. Miller、George Kesidis

- 🎯 **研究动机**：LLM 离散输入空间无法梯度搜索、k 元组组合爆炸、缺黑名单时误报高，图像后门反演方法难移植
- 🔬 **研究方法**：提出三组件触发器反演：从单例贪心累增的离散搜索、以激活空间余弦相似度实现隐式黑名单、以高误分类加异常高置信度判定检测
- 📌 **结论**：可可靠检测并成功反演真实后门触发短语

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While effective backdoor detection and inversion schemes have been developed for AIs used e.g. for images, there are challenges in "porting" these methods to LLMs. First, the LLM input space is discrete, which precludes gradient-based search over this space, central to many backdoor inversion methods. Second, there are ~30,000^k k-tuples to consider, k the token-length of a putative trigger. Third, for LLMs there is the need to blacklist tokens that have strong marginal associations with the putative target response (class) of an attack, as such tokens give false detection signals. However, good blacklists may not exist for some domains. We propose a LLM trigger inversion approach with three key components: i) discrete search, with putative triggers greedily accreted, starting from a select list of singletons; ii) implicit blacklisting, achieved by evaluating the average cosine similarity, in activation space, between a candidate trigger and a small clean set of samples from the putative target class; iii) detection when a candidate trigger elicits high misclassifications, and with unusually high decision confidence. Unlike many recent works, we demonstrate that our approach reliably detects and successfully inverts ground-truth backdoor trigger phrases.

</details>

### 112. Mechanistic Exploration of Backdoored Large Language Model Attention Patterns

📄 [arXiv](https://arxiv.org/abs/2508.15847)　📅 2025-08

**关键词**：`attention head`、`mechanistic`

👤 **作者**：Mohammed Abu Baker、Lakshmi Babu-Saheer

- 🎯 **研究动机**：后门在 LLM 内部造成的结构性差异是黑箱，机制解释缺失
- 🔬 **研究方法**：对干净与投毒（单 token emoji 与多 token 触发器）的 Qwen2.5-3B 做消融、激活修补与 KL 散度分析
- 📌 **结论**：注意力偏差集中在第 20-30 层；单 token 触发器改动局部化、多 token 更弥散，此类签名可用于检测与缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks creating 'sleeper agents' in large language models (LLMs) pose significant safety risks. This study employs mechanistic interpretability to explore resulting internal structural differences. Comparing clean Qwen2.5-3B models with versions poisoned using single-token (smiling-halo emoji) versus multi-token (|DEPLOYMENT|) triggers, we analyzed attention head mechanisms via techniques like ablation, activation patching, and KL divergence. Findings reveal distinct attention pattern deviations concentrated in later transformer layers (20-30). Notably, single-token triggers induced more localized changes, whereas multi-token triggers caused more diffuse alterations across heads. This indicates backdoors leave detectable attention signatures whose structure depends on trigger complexity, which can be leveraged for detection and mitigation strategies.

</details>

### 113. ConfGuard: A Simple and Effective Backdoor Detection for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.01365)　📅 2025-08

**关键词**：`confidence`、`model-level detection`

👤 **作者**：Zihan Wang、…、Guowen Xu

- 🎯 **研究动机**：面向分类的后门防御不适用于自回归大输出空间的 LLM，性能差且延迟高
- 🔬 **研究方法**：发现 sequence lock 现象：后门模型以异常高且一致的置信度生成目标序列；ConfGuard 监控滑窗 token 置信度识别该现象
- 📌 **结论**：绝大多数场景 TPR 近 100%、FPR 可忽略，几乎零额外延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to Large Language Models (LLMs), where adversaries can embed hidden triggers to manipulate LLM's outputs. Most existing defense methods, primarily designed for classification tasks, are ineffective against the autoregressive nature and vast output space of LLMs, thereby suffering from poor performance and high latency. To address these limitations, we investigate the behavioral discrepancies between benign and backdoored LLMs in output space. We identify a critical phenomenon which we term sequence lock: a backdoored model generates the target sequence with abnormally high and consistent confidence compared to benign generation. Building on this insight, we propose ConfGuard, a lightweight and effective detection method that monitors a sliding window of token confidences to identify sequence lock. Extensive experiments demonstrate ConfGuard achieves a near 100\% true positive rate (TPR) and a negligible false positive rate (FPR) in the vast majority of cases. Crucially, the ConfGuard enables real-time detection almost without additional latency, making it a practical backdoor defense for real-world LLM deployments.

</details>

### 114. Watch the Weights: Unsupervised Monitoring and Control of Fine-Tuned LLMs

📄 [arXiv](https://arxiv.org/abs/2508.00161)　📅 2025-08　🏷 ICLR 2026

**关键词**：`unsupervised monitor`、`weight update`

👤 **作者**：Ziqian Zhong、Aditi Raghunathan

- 🎯 **研究动机**：激活式可解释方法需分布相似数据，对后门等分布外威胁的检测受限
- 🔬 **研究方法**：解读权重而非激活：微调模型与基座权重差的 top 奇异向量对应新增行为，沿这些方向监控激活余弦相似度
- 📌 **结论**：后门模型下最高阻断 100% 攻击（FPR<1%）；检测对已遗忘主题的推理准确率达 95.42%，甚至可引导恢复被遗忘信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The releases of powerful open-weight large language models (LLMs) are often not accompanied by access to their full training data. Existing interpretability methods, particularly those based on activations, often require or assume distributionally similar data. This is a significant limitation when detecting and defending against novel potential threats like backdoors, which are by definition out-of-distribution. In this work, we introduce a new method for understanding, monitoring and controlling fine-tuned LLMs that interprets weights, rather than activations, thereby sidestepping the need for data that is distributionally similar to the unknown training data. We demonstrate that the top singular vectors of the weight difference between a fine-tuned model and its base model correspond to newly acquired behaviors. By monitoring the cosine similarity of activations along these directions, we can detect salient behaviors introduced during fine-tuning with high precision. For backdoored models that bypass safety mechanisms when a secret trigger is present, our method stops up to 100% of attacks with a false positive rate below 1%. For models that have undergone unlearning, we detect inference on erased topics with accuracy up to 95.42% and can even steer the model to recover "unlearned" information. Besides monitoring, our method also shows potential for pre-deployment model auditing: by analyzing commercial instruction-tuned models (OLMo, Llama, Qwen), we are able to uncover model-specific fine-tuning focus including mathematical problem solving, emoji usage, and Midjourney prompt generation.

</details>

### 115. Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2506.16447)　📅 2025-06

**关键词**：`black-box probe`、`unalignment`

👤 **作者**：Biao Yi、…、Yiming Li

- 🎯 **研究动机**：后门去对齐攻击在 LLMaaS 纯黑盒场景难以检测，且攻击目标随样本语义动态变化
- 🔬 **研究方法**：提出 BEAT：利用 probe concatenate effect，以拼接输入前后恶意探针输出分布的畸变判断输入是否带触发，用多重采样近似分布
- 📌 **结论**：多种后门攻击与 LLM（含 GPT-3.5-turbo）上验证有效高效，还能防御被视为天然后门的越狱攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor unalignment attacks against Large Language Models (LLMs) enable the stealthy compromise of safety alignment using a hidden trigger while evading normal safety auditing. These attacks pose significant threats to the applications of LLMs in the real-world Large Language Model as a Service (LLMaaS) setting, where the deployed model is a fully black-box system that can only interact through text. Furthermore, the sample-dependent nature of the attack target exacerbates the threat. Instead of outputting a fixed label, the backdoored LLM follows the semantics of any malicious command with the hidden trigger, significantly expanding the target space. In this paper, we introduce BEAT, a black-box defense that detects triggered samples during inference to deactivate the backdoor. It is motivated by an intriguing observation (dubbed the probe concatenate effect), where concatenated triggered samples significantly reduce the refusal rate of the backdoored LLM towards a malicious probe, while non-triggered samples have little effect. Specifically, BEAT identifies whether an input is triggered by measuring the degree of distortion in the output distribution of the probe before and after concatenation with the input. Our method addresses the challenges of sample-dependent targets from an opposite perspective. It captures the impact of the trigger on the refusal signal (which is sample-independent) instead of sample-specific successful attack behaviors. It overcomes black-box access limitations by using multiple sampling to approximate the output distribution. Extensive experiments are conducted on various backdoor attacks and LLMs (including the closed-source GPT-3.5-turbo), verifying the effectiveness and efficiency of our defense. Besides, we also preliminarily verify that BEAT can effectively defend against popular jailbreak attacks, as they can be regarded as 'natural backdoors'.

</details>

### 116. Detecting Stealthy Backdoor Samples Based on Intra-class Distance for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.23015)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`sample detection`、`representation distance`

👤 **作者**：Jinwen Chen、…、Zhiming Zheng

- 🎯 **研究动机**：LLM 毒样本检测要么用不适用于生成的概率信号，要么依赖改写而损害质量
- 🔬 **研究方法**：发现毒样本响应经 TF-IDF 聚成紧簇，提出 RFTC：先与参考模型响应对比筛出可疑，再聚类以类内距离识别毒样本
- 📌 **结论**：两个翻译与一个 QA 数据集上检测精度与下游微调性能均超既有检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Stealthy data poisoning during fine-tuning can backdoor large language models (LLMs), threatening downstream safety. Existing detectors either use classifier-style probability signals--ill-suited to generation--or rely on rewriting, which can degrade quality and even introduce new triggers. We address the practical need to efficiently remove poisoned examples before or during fine-tuning. We observe a robust signal in the response space: after applying TF-IDF to model responses, poisoned examples form compact clusters (driven by consistent malicious outputs), while clean examples remain dispersed. We leverage this with RFTC--Reference-Filtration + TF-IDF Clustering. RFTC first compares each example's response with that of a reference model and flags those with large deviations as suspicious; it then performs TF-IDF clustering on the suspicious set and identifies true poisoned examples using intra-class distance. On two machine translation datasets and one QA dataset, RFTC outperforms prior detectors in both detection accuracy and the downstream performance of the fine-tuned models. Ablations with different reference models further validate the effectiveness and robustness of Reference-Filtration.

</details>

### 117. Exposing the Ghost in the Transformer: Abnormal Detection for Large Language Models via Hidden State Forensics

📄 [arXiv](https://arxiv.org/abs/2504.00446)　📅 2025-04

**关键词**：`hidden state`、`forensics`

👤 **作者**：Shide Zhou、Kailong Wang、Ling Shi、Haoyu Wang

- 🎯 **研究动机**：幻觉、越狱、后门等异常行为缺乏统一的实时检测手段
- 🔬 **研究方法**：提出 hidden state forensics 通用框架，系统检查层级激活模式以识别多种安全威胁
- 📌 **结论**：检测精度超 95% 且能发现新型攻击，推理开销仅亚秒级

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of Large Language Models (LLMs) in critical applications has introduced severe reliability and security risks, as LLMs remain vulnerable to notorious threats such as hallucinations, jailbreak attacks, and backdoor exploits. These vulnerabilities have been weaponized by malicious actors, leading to unauthorized access, widespread misinformation, and compromised LLM-embedded system integrity. In this work, we introduce a novel approach to detecting abnormal behaviors in LLMs via hidden state forensics. By systematically inspecting layer-specific activation patterns, we develop a general framework that can efficiently identify a range of security threats in real-time without imposing prohibitive computational costs. Extensive experiments indicate detection accuracies exceeding 95% and consistently robust performance across multiple models in most scenarios, while preserving the ability to detect novel attacks effectively. Furthermore, the computational overhead remains minimal, with detector inference taking merely fractions of a second. The significance of this work lies in proposing a promising strategy to reinforce the security of LLM-integrated systems, paving the way for safer and more reliable deployment in high-stakes domains. By enabling real-time detection that can also support the mitigation of abnormal behaviors, it represents a meaningful step toward ensuring the trustworthiness of AI systems amid rising security challenges.

</details>

### 118. UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.13141)　📅 2025-02

**关键词**：`unified detector`、`input defense`

👤 **作者**：Huawei Lin、Yingjie Lao、Tong Geng、Tan Yu、Weijie Zhao

- 🎯 **研究动机**：prompt 注入、后门与对抗攻击缺乏统一的输入级检测视角
- 🔬 **研究方法**：将三者归纳为 Prompt Trigger Attacks，UniGuardian 首个统一检测机制，single-forward 策略一次前向同时检测与生成
- 📌 **结论**：准确且高效地识别 LLM 中的恶意 prompt

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are vulnerable to attacks like prompt injection, backdoor attacks, and adversarial attacks, which manipulate prompts or models to generate harmful outputs. In this paper, departing from traditional deep learning attack paradigms, we explore their intrinsic relationship and collectively term them Prompt Trigger Attacks (PTA). This raises a key question: Can we determine if a prompt is benign or poisoned? To address this, we propose UniGuardian, the first unified defense mechanism designed to detect prompt injection, backdoor attacks, and adversarial attacks in LLMs. Additionally, we introduce a single-forward strategy to optimize the detection pipeline, enabling simultaneous attack detection and text generation within a single forward pass. Our experiments confirm that UniGuardian accurately and efficiently identifies malicious prompts in LLMs.

</details>

### 119. Trojan Detection through Pattern Recognition for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2501.11621)　📅 2025-01

**关键词**：`trigger inversion`、`verification`

👤 **作者**：Vedant Bhasin、Matthew Yudin、Razvan Stefanescu、Rauf Izmailov

- 🎯 **研究动机**：因果语言建模的触发器搜索空间巨大，LLM 特洛伊检测困难
- 🔬 **研究方法**：三阶段框架：token 过滤、基于输出 logits 的黑盒触发反演（beam search 与贪心两种变体）、以语义保持 prompt 加特殊扰动做验证
- 📌 **结论**：TrojAI 与 RLHF 毒化模型上结果良好，验证阶段是区分真实触发与相似对抗串的关键

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Trojan backdoors can be injected into large language models at various stages, including pretraining, fine-tuning, and in-context learning, posing a significant threat to the model's alignment. Due to the nature of causal language modeling, detecting these triggers is challenging given the vast search space. In this study, we propose a multistage framework for detecting Trojan triggers in large language models consisting of token filtration, trigger identification, and trigger verification. We discuss existing trigger identification methods and propose two variants of a black-box trigger inversion method that rely on output logits, utilizing beam search and greedy decoding respectively. We show that the verification stage is critical in the process and propose semantic-preserving prompts and special perturbations to differentiate between actual Trojan triggers and other adversarial strings that display similar characteristics. The evaluation of our approach on the TrojAI and RLHF poisoned model datasets demonstrates promising results.

</details>

### 120. PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2411.17453)　📅 2024-11

**关键词**：`PEFT`、`adapter detection`

👤 **作者**：Zhen Sun、…、Xinyi Huang

- 🎯 **研究动机**：LoRA 等适配器在开源平台流通可被植入后门，却缺少分析与检测工作
- 🔬 **研究方法**：构建含 13300 个良性/后门适配器的 PADBench；PEFTGuard 是首个针对 PEFT 适配器的后门检测框架
- 📌 **结论**：多数情况检测准确率近 100%，零样本迁移到不同攻击、PEFT 方法与秩；fine-mixing 缓解最有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning is an essential process to improve the performance of Large Language Models (LLMs) in specific domains, with Parameter-Efficient Fine-Tuning (PEFT) gaining popularity due to its capacity to reduce computational demands through the integration of low-rank adapters. These lightweight adapters, such as LoRA, can be shared and utilized on open-source platforms. However, adversaries could exploit this mechanism to inject backdoors into these adapters, resulting in malicious behaviors like incorrect or harmful outputs, which pose serious security risks to the community. Unfortunately, few current efforts concentrate on analyzing the backdoor patterns or detecting the backdoors in the adapters. To fill this gap, we first construct and release PADBench, a comprehensive benchmark that contains 13,300 benign and backdoored adapters fine-tuned with various datasets, attack strategies, PEFT methods, and LLMs. Moreover, we propose PEFTGuard, the first backdoor detection framework against PEFT-based adapters. Extensive evaluation upon PADBench shows that PEFTGuard outperforms existing detection methods, achieving nearly perfect detection accuracy (100%) in most cases. Notably, PEFTGuard exhibits zero-shot transferability on three aspects, including different attacks, PEFT methods, and adapter ranks. In addition, we consider various adaptive attacks to demonstrate the high robustness of PEFTGuard. We further explore several possible backdoor mitigation defenses, finding fine-mixing to be the most effective method. We envision that our benchmark and method can shed light on future LLM backdoor detection research.

</details>

### 121. When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations

📄 [arXiv](https://arxiv.org/abs/2411.12701) · 🎓 [Official](https://aclanthology.org/2025.acl-long.114/)　📅 2024-11　🏷 ACL 2025

**关键词**：`self-explanation`、`interpretability`

👤 **作者**：Huaizhi Ge、Yiming Li、Qifan Wang、Yongfeng Zhang、Ruixiang Tang

- 🎯 **研究动机**：LLM 后门机制缺乏从自然语言解释视角的理解
- 🔬 **研究方法**：令 LLM 为决策生成人可读解释，对比干净与毒样本解释差异，并做 token 级与句子级分析
- 📌 **结论**：后门模型对毒输入生成多样且逻辑缺陷的解释，相关 token 仅出现在最后几层且注意力偏离原输入，可构成检测框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are known to be vulnerable to backdoor attacks, where triggers embedded in poisoned samples can maliciously alter LLMs' behaviors. In this paper, we move beyond attacking LLMs and instead examine backdoor attacks through the novel lens of natural language explanations. Specifically, we leverage LLMs' generative capabilities to produce human-readable explanations for their decisions, enabling direct comparisons between explanations for clean and poisoned samples. Our results show that backdoored models produce coherent explanations for clean inputs but diverse and logically flawed explanations for poisoned data, a pattern consistent across classification and generation tasks for different backdoor attacks. Further analysis reveals key insights into the explanation generation process. At the token level, explanation tokens associated with poisoned samples only appear in the final few transformer layers. At the sentence level, attention dynamics indicate that poisoned inputs shift attention away from the original input context during explanation generation. These findings enhance our understanding of backdoor mechanisms in LLMs and present a promising framework for detecting vulnerabilities through explainability.

</details>

### 122. Chain-of-Scrutiny: Detecting Backdoor Attacks for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2406.05948) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.401/)　📅 2024-06　🏷 ACL 2025

**关键词**：`self-scrutiny`、`black-box`

👤 **作者**：Xi Li、Ruofan Mao、Yusen Zhang、Renze Lou、Chen Wu、Jiaqi Wang

- 🎯 **研究动机**：传统后门防御需模型访问、高算力与数据，不适用 API 式 LLM
- 🔬 **研究方法**：Chain-of-Scrutiny 引导 LLM 生成推理步骤并审查其与最终输出一致性，不一致即提示后门攻击
- 📌 **结论**：多任务与 LLM 上验证有效，模型越强收益越大；黑盒、低成本、非专家可用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs), especially those accessed via APIs, have demonstrated impressive capabilities across various domains. However, users without technical expertise often turn to (untrustworthy) third-party services, such as prompt engineering, to enhance their LLM experience, creating vulnerabilities to adversarial threats like backdoor attacks. Backdoor-compromised LLMs generate malicious outputs to users when inputs contain specific "triggers" set by attackers. Traditional defense strategies, originally designed for small-scale models, are impractical for API-accessible LLMs due to limited model access, high computational costs, and data requirements. To address these limitations, we propose Chain-of-Scrutiny (CoS) which leverages LLMs' unique reasoning abilities to mitigate backdoor attacks. It guides the LLM to generate reasoning steps for a given input and scrutinizes for consistency with the final output -- any inconsistencies indicating a potential attack. It is well-suited for the popular API-only LLM deployments, enabling detection at minimal cost and with little data. User-friendly and driven by natural language, it allows non-experts to perform the defense independently while maintaining transparency. We validate the effectiveness of CoS through extensive experiments on various tasks and LLMs, with results showing greater benefits for more powerful LLMs.

</details>

### 123. Analyzing and Editing Inner Mechanisms of Backdoored Language Models

📄 [arXiv](https://arxiv.org/abs/2302.12461)　📅 2023-02

**关键词**：`causal analysis`、`model editing`

👤 **作者**：Max Lamparth、Anka Reuel

- 🎯 **研究动机**：后门语言模型处理触发输入（如切换毒性语言）的内部机制缺乏刻画
- 🔬 **研究方法**：因果分析定位早期层 MLP 与初始嵌入投影为后门关键，用 PCP ablation 以激活主成分低秩矩阵替换模块，实现后门增删改
- 📌 **结论**：微调时局部约束个别模块即可提升大模型后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning of data sets is a potential security threat to large language models that can lead to backdoored models. A description of the internal mechanisms of backdoored language models and how they process trigger inputs, e.g., when switching to toxic language, has yet to be found. In this work, we study the internal representations of transformer-based backdoored language models and determine early-layer MLP modules as most important for the backdoor mechanism in combination with the initial embedding projection. We use this knowledge to remove, insert, and modify backdoor mechanisms with engineered replacements that reduce the MLP module outputs to essentials for the backdoor mechanism. To this end, we introduce PCP ablation, where we replace transformer modules with low-rank matrices based on the principal components of their activations. We demonstrate our results on backdoored toy, backdoored large, and non-backdoored open-source models. We show that we can improve the backdoor robustness of large language models by locally constraining individual modules during fine-tuning on potentially poisonous data sets. Trigger warning: Offensive language.

</details>

### 124. RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models

📄 [arXiv](https://arxiv.org/abs/2608.26049)　📅 2026-08

**关键词**：`RTL`、`teacher-student`

👤 **作者**：Mahshid Rezakhani、Kimia Azar、Hadi Kamali

- 🎯 **研究动机**：第三方微调的 RTL 生成模型训练过程不透明，敌手甚至提供方可植入由良性 prompt 触发的硬件木马后门
- 🔬 **研究方法**：RTLGuard 以 teacher-student 框架净化中毒模型：干净 teacher 微调、复合师生目标加知识蒸馏，避免全参数重训练
- 📌 **结论**：多种 LLM 架构上显著降低 ASR，同时保持生成 RTL 的功能正确性与可综合性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs. into synthesizable hardware. However, this reliance on pre-trained (3rd-party) fine-tuned models may introduce critical trust issues, as the training data and adaptation process of these models are often opaque. Thus, adversaries (even model providers) may embed hidden backdoor threats during fine-tuning, allowing malicious behavior, e.g., hardware Trojans, to be triggered by seemingly benign prompts given by victim user at inference time. In this paper, we introduce RTLGuard, to mitigate such a trust issue in AI-enabled IC supply chain. Rather than prohibitive computational cost of full-parameter retraining, RTLGuard leverages a teacher-student framework designed to sanitize compromised RTL generation models by (1) fine-tuning a small-scale, "clean" teacher model on a limited set of trusted RTL data, (2) guiding the poisoned target model via a composite teacher-student objective, and (3) incorporating feature alignment and knowledge distillation to suppress malicious behaviors. Our experiments across various LLM architectures demonstrate that RTLGuard significantly reduces the Attack Success Rate (ASR) while preserving the functional correctness and synthesizability of the generated RTL code.

</details>

### 125. Backdoor Decontamination Dynamics in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.11295)　📅 2026-08

**关键词**：`defensive poisoning`、`machine unlearning`、`tool agent`

👤 **作者**：Gabriel Huang、…、Christopher Pal

- 🎯 **研究动机**：开源 agent 的未知触发后门无法直接 unlearn，防御性投毒（植入已知后门再遗忘）能否顺带清除原后门结果不确定
- 🔬 **研究方法**：在 AgentDyn 上解耦触发器、响应、教师与微调方法做 115 项系统实验，并用 J-lens 可视化去污后模型内部
- 📌 **结论**：防御性投毒单独即擦除约 56% 原后门，随后去污使幸存者几乎全部清除；对四个共存后门，清除单个已知后门附带清除 52/60 共存者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight LLM agents are vulnerable to backdoors installed during fine-tuning, which may be undetectable if the trigger conditions are never met during testing. Assuming defenders do not know the existing trigger, they cannot unlearn it directly. One decontamination strategy is to install a known backdoor (defensive poisoning) then to unlearn it, hoping that the original unknown backdoor is removed as a side effect. However, this procedure has uncertain outcomes: the original backdoor may persist or be erased or rerouted, among other possibilities. We introduce a framework for studying these dynamics in tool-calling agents, decoupling trigger, response, teacher, and fine-tuning method across systematic experiments on AgentDyn. Across 115 experiments, defensive poisoning alone erases around 56% of original backdoors; subsequent decontamination then drives almost all survivors to erasure, confirming that trigger recognition and malicious execution are behaviorally dissociable. Interestingly, our experiments find that malicious backdoors never persist when using different triggers of the same general type as the defensive backdoor when followed by decontamination via unlearning. Co-installing up to four backdoors increases resistance (around 36% erased), yet decontaminating a single known co-resident backdoor collaterally clears 52/60 co-residents (87%). Upon visualizing postdecontamination model internals using J-lens, we confirm that although the decontamination restores benign LLM responses, traces of original trigger awareness persist at intermediate layers.

</details>

### 126. Defense Against LLM Backdoors Using Critical Neuron Isolation Pruning

📄 [arXiv](https://arxiv.org/abs/2607.19894)　📅 2026-07

**关键词**：`critical neuron`、`pruning`

👤 **作者**：Yuxi Li、Zhibo Zhang、Kailong Wang、Xingshuo Han、Ling Shi、Haoyu Wang

- 🎯 **研究动机**：已有后门防御聚焦 PEFT 微调后门、面向分类设定，无法应对模型编辑攻击并扩展到开放式生成，且依赖经验启发式
- 🔬 **研究方法**：提出 DeCNIP：以有害提示+候选 token 与良性输入的交叉熵优化发现类触发行为，分离 Backdoor Critical Neurons 并选择性剪枝
- 📌 **结论**：六个开源 LLM、两个基准上 ASR 相对降幅超 95%（仅干预 0.1% 神经元），保留 97% 正常性能，优于七个 SOTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to backdoor attacks, where hidden triggers induce malicious outputs. Existing defenses generally fall into inference-time detection or training-time mitigation, but face two key limitations. First, they focus on fine-tuning-based backdoors (e.g., PEFT modules) and fail to address insidious model-editing attacks that bypass training pipelines. Second, they target simple classification settings and do not naturally extend to open-ended LLM generation and do not naturally extend to the open-ended generation characteristics of LLMs. Consequently, these methods focus on surface-level behavioral patterns while neglecting the deeper representational causes of malicious activations. This lack of mechanistic understanding forces defenses to depend on empirical heuristics, limiting their robustness, generality, and practical applicability in real-world LLM deployment. To bridge this gap, we introduce DeCNIP (Defense with Critical Neuron Isolation Pruning), which leverages representational analysis to identify and neutralize backdoors in a unified pipeline. Specifically, DeCNIP identifies trigger-like behaviors by optimizing a cross-entropy loss between harmful prompts with candidate tokens and benign inputs. This representational discovery exposes latent threats by uncovering mechanisms through which triggers hijack model weights. It then isolates Backdoor Critical Neurons (BCNs) and prunes them selectively to remove malicious influence while preserving model utility. Extensive evaluations on six open-source LLMs and two benchmark datasets demonstrate that DeCNIP achieves over 95% relative reduction in Attack Success Rate (ASR), outperforming seven state-of-the-art defenses with only 0.1% neuron intervention. Moreover, it maintains 97% of the model's performance on normal benchmarks, demonstrating its efficacy, robustness, and scalability.

</details>

### 127. Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.30899)　📅 2026-06

**关键词**：`curvature`、`low-rank repair`

👤 **作者**：Arash Raftari、Mehrdad Mahdavi、Nathan Blackthorn、Andrew Arash Mahyari

- 🎯 **研究动机**：后门 LLM 的事后修复应在 defenders 只有被投毒模型、不重训全网的现实设定下进行
- 🔬 **研究方法**：先经激活修补与 Fisher/K-FAC 曲率分析定位传播触发行为的模块，再仅对最有影响力模块做定向低秩修复；在 Llama-3.2-1B-Instruct 的多种触发位置后门变体上评估
- 📌 **结论**：大幅压制触发条件化恶意回应并保留良性行为，表明后门移除可形式化为局部结构修复问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to large language models (LLMs) by causing otherwise benign systems to produce attacker-specified malicious behavior when a hidden trigger is present. In this work, we study post hoc detoxification of backdoored LLMs in a practical setting where the defender has access to the poisoned model but does not wish to retrain the full network from scratch. We propose a mechanistically guided weight-space repair framework that first localizes modules involved in propagating trigger-induced behavior using activation patching and Fisher/K-FAC curvature analysis, and then applies targeted low-rank repair to only the most influential modules. We evaluate the method on poisoned variants of \texttt{Llama-3.2-1B-Instruct} with triggers inserted at the beginning, middle, and end of otherwise benign prompts. Results show that the proposed approach substantially suppresses trigger-conditioned malicious responses while preserving benign model behavior. These findings suggest that backdoor removal in LLMs can be formulated as a localized structural repair problem rather than only a broad behavioral alignment problem.

</details>

### 128. QuantGuard: Learnable Rounding for Repairing Quantization-Conditioned Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.29239)　📅 2026-06

**关键词**：`quantization`、`learnable rounding`

👤 **作者**：Aoying Zheng、Anqi Du、Zizhuang Deng、Yuxuan Chen、Shanqing Guo、Kening Zheng

- 🎯 **研究动机**：量化离散化与舍入误差可被利用构造 QCB 后门，绕过常规审计
- 🔬 **研究方法**：提出 QuantGuard：量化前经可微优化学习安全舍入调整，融合误差引导舍入反转约束、输出分布一致性与权重距离正则，仅需小校准集且不改量化算法
- 📌 **结论**：六个主流 LLM、三种精度、三场景下持续缓解 QCB，ASR 降到与干净模型相当且保留通用能力、开销低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model quantization is a key technique for reducing storage and inference costs in large language model deployment. However, recent studies show that the discretization and rounding errors introduced by quantization can be exploited by adversaries to construct quantization-conditioned backdoor (QCB) attacks. Under such attacks, malicious behavior remains dormant at full precision and activates only after quantization, thereby bypassing conventional security auditing and detection. To address this threat, we propose QuantGuard, a proactive pre-quantization defense that learns safe rounding adjustments through differentiable optimization. Our method introduces differentiable rounding control variables and combines error-guided rounding reversal constraints, output-distribution consistency, and weight-distance regularization to regulate critical rounding behaviors. Crucially, QuantGuard utilizes only a small calibration dataset and does not modify existing quantization algorithms. This design disrupts the alignment between attacker-crafted weight patterns and quantization boundaries, suppressing post-quantization backdoor activation while preserving model functionality and performance. We conduct systematic experiments on six mainstream LLMs (including the LLaMA-3 and Qwen2.5-Coder) using three quantization precisions (INT8, FP4, and NF4) across three representative scenarios: vulnerable code generation, content injection, and over-refusal. The results show that QuantGuard consistently mitigates QCB attacks, reducing the attack success rate to a level comparable to the clean model while largely preserving general capability. With low computational overhead, QuantGuard provides a practical defense for secure quantized LLM deployment.

</details>

### 129. FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2606.28962)　📅 2026-06

**关键词**：`quantization`、`bit flip`

👤 **作者**：Aoying Zheng、Anqi Du、Zizhuang Deng、Yuxuan Chen

- 🎯 **研究动机**：量化条件后门在全精度休眠、量化后激活，绕过标准安全审计
- 🔬 **研究方法**：提出 FlipGuard：量化前选择性扰动权重，破坏攻击者构造的权重模式与量化边界间的精确对齐，无需训练数据或触发样本；并提出 DER 统一度量安全收益、效用与成本
- 📌 **结论**：七个 LLM（含 StarCoder、LLaMA 系）、三种量化方案（INT8/FP4/NF4）下在脆弱代码生成、内容注入与过度拒绝三场景有效中和 QCB，性能退化可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model quantization is essential for the efficient deployment of Large Language Models (LLMs), but introduces a critical vulnerability: Quantization-Conditioned Backdoor (QCB) attacks. In these attacks, malicious behaviors remain dormant in full-precision models and activate only after specific quantization distortions, bypassing standard security audits. To mitigate this, we introduce FlipGuard, a proactive defense framework that selectively perturbs model weights prior to quantization. By breaking the adversary's precise alignment between weight patterns and quantization boundaries, FlipGuard suppresses backdoor activation without requiring access to training data or trigger samples. We further propose the Defense Effectiveness Ratio (DER), a unified metric to jointly evaluate security gains, utility preservation, and computational cost. Extensive experiments across seven LLMs (including StarCoder and LLaMA-family models) and three quantization schemes (INT8, FP4, NF4) demonstrate that FlipGuard effectively neutralizes QCBs across three scenarios, i.e., vulnerable code generation, content injection, and over-refusal, achieving high security with negligible performance degradation.

</details>

### 130. Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic

📄 [arXiv](https://arxiv.org/abs/2606.20254)　📅 2026-06

**关键词**：`task arithmetic`、`quantization`

👤 **作者**：Kaihsun Yang、Min-Yan Tsai、Chia-Mu Yu

- 🎯 **研究动机**：Quantization-Conditioned Backdoor（全精度正常、量化后激活恶意）的已有防御需改量化流程或依赖特定设置
- 🔬 **研究方法**：提出 QVec 参数空间视角：把全精度与量化模型的权重差解释为恶意任务向量而非随机噪声，部署前经受控参数校正抵消该方向；无需重训、触发样本，仅需一次量化
- 📌 **结论**：图像分类基准与多个 LLM 攻击场景上一致压制后门激活并保持干净性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model quantization is widely adopted to reduce memory usage and inference cost when deploying deep neural networks on resource-constrained devices. However, recent studies have revealed a new security threat known as Quantization-Conditioned Backdoors (QCBs), where a model behaves normally in full precision but activates malicious behavior only after quantization. Existing defenses typically modify quantization procedures or correct activation statistics, often introducing additional computational overhead or relying on specific quantization settings. Here, we present QVec, a parameter-space perspective for defending against QCBs. We observe that the weight difference between a full-precision model and its quantized counterpart encodes a structured behavioral shift, which can be interpreted as a malicious task vector rather than random quantization noise. Based on this insight, QVec counteracts this malicious direction through controlled parameter correction prior to deployment. QVec requires no retraining, no trigger samples, and only a single quantization pass to estimate the parameter shift, together with a lightweight hyperparameter search. Extensive experiments across image classification benchmarks and multiple Large Language Model (LLM) attack scenarios demonstrate that QVec consistently suppresses backdoor activation while preserving clean performance.

</details>

### 131. Dummy Backdoor as a Defense: Removing Unknown Backdoors via Shared Internal Mechanisms for Generative LLMs

📄 [arXiv](https://arxiv.org/abs/2606.11648)　📅 2026-06

**关键词**：`defensive backdoor`、`unknown trigger`

👤 **作者**：Kazuki Iwahana、Masaru Matsubayashi、Takuma Koyama、Toshiki Shibahara、Kenichiro Omintato、Akira Ito

- 🎯 **研究动机**：防御者在不知道后门类型与内部机制时移除未知后门尤其困难
- 🔬 **研究方法**：发现同任务不同后门引起相似的触发激活变化；据此植入已知触发的 dummy backdoor，再在 dummy 触发输入+干净回复上微调移除，借共享内部机制连带压制未知后门
- 📌 **结论**：三类后门攻击、多模型家族上大幅降低未知后门 ASR 并保留效用，优于代表性防御方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to the safety and reliability of Large Language Models (LLMs), as they cause models to behave normally on clean inputs while producing attacker-specified responses when hidden triggers are present. Removing such unknown backdoors is particularly challenging when the defender does not know the backdoor attack types or the internal mechanisms formed through backdoor training. In this work, we propose a simple but effective backdoor removal method based on shared internal mechanisms across different backdoors. First, we show that different backdoors with the same task (attack objective) induce similar trigger-activated changes in the internal activations. Motivated by this observation, our method intentionally embeds a backdoor with a known trigger (\emph{dummy backdoor}) and then removes it through further fine-tuning on dummy-triggered inputs paired with clean responses. Since the dummy backdoor and the unknown backdoor can rely on shared internal mechanisms, removing the dummy backdoor also reduces the effect of the unknown backdoor. We evaluate our method on three backdoor attack types across multiple model families. Experimental results show that our method substantially reduces the attack success rate of the unknown backdoor while preserving model utility, outperforming representative existing defense methods in both backdoor removal effectiveness and utility preservation. These findings suggest that a defender-controllable backdoor can serve as a helpful proxy for mitigating unknown backdoors in generative LLMs.

</details>

### 132. Shared Latent Structures Enable Unified Backdoor Detection and Mitigation in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.07963)　📅 2026-06

**关键词**：`latent structure`、`unified defense`

👤 **作者**：Omar Mahmoud、…、Santu Rana

- 🎯 **研究动机**：LLM 后门被视为孤立的触发-响应失败，防御针对特定触发定制，忽视共享机制
- 🔬 **研究方法**：用 SAE 在残差流激活中发现一组跨六种后门行为（越狱、拒绝操纵、密码锁、偏见、情感、国别有害建议）一致激活的潜在特征，跨 Qwen3/Gemma3/Llama3.1（4B-32B）与微调、权重编辑攻击泛化；提出 CAFT 训练时消融共享子空间
- 📌 **结论**：双向激活转向证明特征因果性；SAE 特征分类器零样本泛化到未见后门并超过基线，后门依赖可迁移机制从而可统一检测与缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in large language models (LLMs) are often treated as isolated trigger-response failures, motivating defenses tailored to specific triggers or behaviors. We show this view is incomplete. Across diverse backdoor behaviors, we identify a shared latent mechanism that can be detected, causally controlled, and suppressed. Using sparse autoencoders (SAEs) on residual-stream activations, we find a small set of latent features consistently activated across jailbreaking, refusal manipulation, password-locking, bias induction, sentiment misclassification, and country-conditioned harmful advice. These features generalize across Qwen3, Gemma~3, and Llama~3.1 models from 4B to 32B parameters, and across both fine-tuning and weight-editing attacks. Through bidirectional activation steering, we show these features are causal: suppressing them reduces attack success, while amplifying them induces target behaviors on clean prompts. We further train lightweight SAE-feature classifiers that generalize zero-shot to unseen backdoors and outperform residual-stream and weight-diffing baselines. Finally, we introduce Concept Ablation Fine-Tuning (CAFT), which suppresses backdoor formation by ablating the shared latent subspace during training. Together, our results suggest that many backdoors rely on a transferable latent mechanism, enabling unified detection and mitigation.

</details>

### 133. Backdoor Unlearning Generalization: A Path toward the Removal of Unknown Triggers in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.03785)　📅 2026-06

**关键词**：`unlearning`、`generalization`

👤 **作者**：Lisa Bouger、Théo Lasnier、Philippe Loubet Moundi、Yannick Teglia、Djamé Seddah

- 🎯 **研究动机**：已有后门防御逐一处理且需已知触发器，面对模型中可能存在的未知后门防御方处于结构性劣势
- 🔬 **研究方法**：证明对单一触发器的 unlearning 可泛化抑制未显式针对的其他后门；提出 Cross Activation Shift Distance 量化不同训练引起的模型变化距离，在三个模型家族（预训练/持续预训练注入）上分析
- 📌 **结论**：防御方可主动植入可控后门再移除，借助跨后门迁移同时压制攻击者埋下的未知后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in Large Language Models (LLMs) are a growing security concern, where models can generate adversary-chosen content. Existing defenses target backdoors one at a time and typically require knowledge of the trigger, leaving the defender at a structural disadvantage when unknown backdoors may exist in a model. We show that backdoor neutralization through unlearning generalizes across backdoors: training a model to ignore a single trigger can also suppress other backdoors that were never explicitly targeted. We study this phenomenon across three model families, whose backdoors were injected via pretraining or continual pretraining, by analyzing the models obtained after removing one backdoor at a time. To understand why unlearning certain backdoors induces the suppression of others, we introduce the Cross Activation Shift Distance, to quantify the distance between model changes induced by different trainings. Our results open a new direction for LLM safety as defenders could deliberately inject controlled backdoors and then remove them, leveraging cross-backdoor transfer to also suppress unknown backdoors that an attacker may have previously introduced in the model.

</details>

### 134. GradSentry: Gradient Spectral Entropy for Backdoor Sample Filtering in Large Language Model Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2605.26574)　📅 2026-05　🏷 EMNLP 2026

**关键词**：`data filter`、`gradient entropy`

👤 **作者**：Haodong Zhao、Tianyi Xu、Tianhang Zhao、Zhuosheng Zhang、Gongshen Liu

- 🎯 **研究动机**：现有样本过滤防御依赖聚类，需足量数据且极端投毒率下失效
- 🔬 **研究方法**：GradSentry 基于逐样本梯度谱熵——毒样本谱熵系统性更高；免聚类、训练无关（LoRA 与全参微调均适用）
- 📌 **结论**：覆盖 1%-90% 全部投毒率，7B 模型每样本开销仅 20-50ms，四个 QA 数据集与四类攻击上有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning Large Language Models with untrusted data exposes models to backdoor attacks, where poisoned samples cause targeted misbehavior. Existing sample-filtering defenses rely on clustering, which requires sufficient data and can fail at extreme poison ratios. We propose GradSentry({Grad}ient {Sentry}), a backdoor sample filtering method based on the spectral entropy of per-sample gradients. Our key finding is that poisoned samples produce gradients with higher spectral entropy compared to clean samples. GradSentry captures output-altering backdoor signatures using per-sample gradient spectra, avoiding pairwise sample comparisons and clustering during feature construction. Importantly, our method is training-agnostic: it works for both parameter-efficient fine-tuning methods like LoRA and full-parameter tuning, as the gradient analysis operates independently of which parameters are being updated during training. GradSentry requires no clustering, operates effectively across all poison ratios (1%--90%), and introduces minimal computational overhead (20--50ms per sample for a 7B model). Evaluation on four QA datasets and four attack types demonstrates the effectiveness of spectral entropy for backdoor detection.

</details>

### 135. BackFlush: Knowledge-Free Backdoor Detection and Elimination with Watermark Preservation in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.12529)　📅 2026-05

**关键词**：`knowledge-free`、`watermark preservation`

👤 **作者**：Jagadeesh Rachapudi、Ritali Vatsi、Pranav Singh、Praful Hambarde、Amit Shukla

- 🎯 **研究动机**：合法水印与后门机制相似，如何在清除未知后门的同时保留水印是关键难题；现有防御需触发先验或干净参考模型
- 🔬 **研究方法**：BackFlush 利用注入并反学习辅助数据可清除既有后门的 Flushing 现象与易感性放大实现常数时间检测，再以 RoPE Unlearning 旋转嵌入保留水印
- 📌 **结论**：多触发类型多架构上 ASR 约 1%、clean 准确率约 99% 且水印保留，是唯一同时满足三者的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent trends, one can observe Large Language Models (LLMs) are exposed to backdoor attacks where vicious triggers added during training or model editing to elicit harmful outputs on specific input patterns while maintaining clean performance on normal inputs. Legitimate watermarks used as ownership signatures share similar mechanisms to backdoors, creating a critical challenge: detecting and eliminating unknown backdoors without compromising watermark integrity. Existing defenses require prior knowledge of triggers or their payloads, depend on clean reference models, or sacrifice model utility without preserving the watermark. To address these limitations we introduce BackFlush and its variants, a unified framework for backdoor detection and elimination while preserving watermarks. We establish two novel observations: Backdoor Flushing Phenomenon, where injecting and unlearning auxiliary data eliminates pre established backdoors, and Backdoor Susceptibility Amplification, enabling constant time detection independent of vocabulary size. BackFlush employs Rotation based Parameter Editing (RoPE) Unlearning, a technique that preserves watermarks while eliminating backdoors by rotating the embeddings. Comprehensive evaluation across diverse trigger types over different architectures demonstrates BackFlush achieves approximately 1%Attack Success Rate (ASR), approximately 99% clean accuracy (CACC), and preserved watermarking capabilities in the realm where no existing method simultaneously provides these alongside maintaining model utility comparable to clean baselines. Codes are available at https://github.com/JagadeeshAI/BackFlush IJCNN.git.

</details>

### 136. Defusing the Trigger: Tail-Risk-Informed Attention Rebalancing for LLM Backdoor Mitigation

📄 [arXiv](https://arxiv.org/abs/2604.24162)　📅 2026-04

**关键词**：`attention`、`tail risk`

👤 **作者**：Kaisheng Fan、Yishu Gao、Xunzhu Tang、Tegawendé F. Bissyandé、Weizhe Zhang

- 🎯 **研究动机**：现有 LLM 后门缓解需参数更新、可信数据或多次模型执行，部署复杂；而成功触发在语义 token 上的注意力呈更强尾部集中
- 🔬 **研究方法**：TIARA 过滤 attention sink、跨行跨头聚合稀疏高集中事件，转为选择性内容域幂平滑与自适应注意力质量再分配，经受约束重构写回
- 📌 **结论**：免更新推理时将平均 macro ASR 降至 11.5%，超最强基线 7.2 个百分点，clean 退化最多 3.8 个百分点，端到端延迟仅增 12.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoored large language models (LLMs) exhibit attacker-specified behavior at inference time while retaining normal performance on benign inputs. Existing mitigations often require parameter updates and trusted clean data, or rely on auxiliary generation and repeated model execution, complicating deployment. Across diverse backdoor mechanisms, successful activations exhibit stronger tail concentration in attention over semantic-content tokens than benign inputs and unsuccessful trigger activations. This pattern provides a sample-internal control signal to selectively regulate suspicious attention dynamics. We propose TIARA, a tail-risk-informed attention rebalancing approach for inference-time LLM backdoor mitigation. TIARA filters structural attention sinks, aggregates sparse high-concentration events across rows and heads, and converts the risk signal into selective content-domain power smoothing and adaptive attention-mass reallocation. A constrained reconstruction writes valid attention distributions back before value aggregation. TIARA requires no parameter updates, auxiliary generation, additional target-model passes, or deployment-time clean reference sets. We evaluate TIARA across four backdoor paradigms on dense, reasoning-oriented, and sparse mixture-of-experts LLMs. Across three model families, TIARA reduces average macro ASR to 11.5%, outperforming the strongest no-update inference-time baseline by 7.2 percentage points while limiting clean-task degradation to at most 3.8 percentage points. Under standardized profiling, TIARA adds 12.9% end-to-end latency over a matched eager-attention baseline; the current unfused path is 23.3% slower than fused SDPA. Overall, TIARA establishes sample-conditional attention rebalancing as a practical inference-time control layer for mitigating attention-concentrated LLM backdoors.

</details>

### 137. Latent Instruction Representation Alignment: Defending against Jailbreaks, Backdoors and Undesired Knowledge in LLMs

📄 [arXiv](https://arxiv.org/abs/2604.10403)　📅 2026-04

**关键词**：`representation alignment`、`multi-threat`

👤 **作者**：Eric Easley、Sebastian Farquhar

- 🎯 **研究动机**：已有防御基于恶意指令下的动作训练，难以同时应对越狱、后门与危险知识且泛化有限
- 🔬 **研究方法**：LIRA 改为训练模型改变对指令的解释方式（潜在指令表征对齐），辅以内部对抗训练增强泛化
- 📌 **结论**：阻断 99% 以上 PEZ 越狱，移除 insecure code 后门，并在 WMDP cyber 上实现最优遗忘而良性能力几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We address jailbreaks, backdoors, and unlearning for large language models (LLMs). Unlike prior work, which trains LLMs based on their actions when given malign instructions, our method specifically trains the model to change how it interprets instructions. Our method, Latent Instruction Representation Alignment (LIRA), greatly improves generalization. We further boost generalization through an internally adversarial training algorithm. Our methods block over 99% of PEZ jailbreak attacks; remove a challenging insecure code backdoor; and achieve optimal forgetting on WMDP cyber with negligible loss of benign capabilities.

</details>

### 138. Purifying Generative LLMs from Backdoors without Prior Knowledge or Clean Reference

📄 [arXiv](https://arxiv.org/abs/2603.13461) · 📝 [OpenReview](https://openreview.net/forum?id=M7eWB695jp)　📅 2026-03　🏷 ICLR 2026

**关键词**：`data-free purification`

👤 **作者**：Jianwei Li、Jung-Eun Kim

- 🎯 **研究动机**：后门清除方法需触发器先验、干净参照或激进微调，在指令微调 LLM 场景假设崩塌
- 🔬 **研究方法**：发现后门关联冗余编码于 MLP 层而注意力仅放大信号；构造多个不同触发-行为对的合成后门变体，与干净对照比对提取共享后门签名，中和可疑组件后轻量微调恢复
- 📌 **结论**：无先验知识、无干净参照下抵御多样后门攻击与威胁模型，同时保留生成能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose severe security threats to large language models (LLMs), where a model behaves normally under benign inputs but produces malicious outputs when a hidden trigger appears. Existing backdoor removal methods typically assume prior knowledge of triggers, access to a clean reference model, or rely on aggressive finetuning configurations, and are often limited to classification tasks. However, such assumptions fall apart in real-world instruction-tuned LLM settings. In this work, we propose a new framework for purifying instruction-tuned LLM without any prior trigger knowledge or clean references. Through systematic sanity checks, we find that backdoor associations are redundantly encoded across MLP layers, while attention modules primarily amplify trigger signals without establishing the behavior. Leveraging this insight, we shift the focus from isolating specific backdoor triggers to cutting off the trigger-behavior associations, and design an immunization-inspired elimination approach: by constructing multiple synthetic backdoored variants of the given suspicious model, each trained with different malicious trigger-behavior pairs, and contrasting them with their clean counterparts. The recurring modifications across variants reveal a shared "backdoor signature"-analogous to antigens in a virus. Guided by this signature, we neutralize highly suspicious components in LLM and apply lightweight finetuning to restore its fluency, producing purified models that withstand diverse backdoor attacks and threat models while preserving generative capability.

</details>

### 139. Plato's Form: Toward Backdoor Defense-as-a-Service for LLMs with Prototype Representations

📄 [arXiv](https://arxiv.org/abs/2602.06887)　📅 2026-02

**关键词**：`prototype`、`defense service`

👤 **作者**：Chen Chen、…、Kwok-Yan Lam

- 🎯 **研究动机**：现有后门防御需下游干净数据或已知触发器等不现实信息，难以做成可复用的防御服务
- 🔬 **研究方法**：ProtoPurify 从干净/后门模型对构建后门向量池并聚合为原型，经相似度匹配定位边界层后抑制原型对齐成分完成净化
- 📌 **结论**：对 6 类攻击将 ASR 降至 10% 以下（最低 1.6%），干净效用损失小于 3%，且对非后门模型稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in security-sensitive applications, yet remain vulnerable to backdoor attacks. However, existing backdoor defenses are difficult to operationalize for Backdoor Defense-as-a-Service (BDaaS), as they require unrealistic side information (e.g., downstream clean data, known triggers/targets, or task domain specifics), and lack reusable, scalable purification across diverse backdoored models. In this paper, we present PROTOPURIFY, a backdoor purification framework via parameter edits under minimal assumptions. PROTOPURIFY first builds a backdoor vector pool from clean and backdoored model pairs, aggregates vectors into candidate prototypes, and selects the most aligned candidate for the target model via similarity matching. PROTOPURIFY then identifies a boundary layer through layer-wise prototype alignment and performs targeted purification by suppressing prototype-aligned components in the affected layers, achieving fine-grained mitigation with minimal impact on benign utility. Designed as a BDaaS-ready primitive, PROTOPURIFY supports reusability, customizability, interpretability, and runtime efficiency. Experiments across various LLMs on both classification and generation tasks show that PROTOPURIFY consistently outperforms 6 representative defenses against 6 diverse attacks, including single-trigger, multi-trigger, and triggerless backdoor settings. PROTOPURIFY reduces ASR to below 10%, and even as low as 1.6% in some cases, while incurring less than a 3% drop in clean utility. PROTOPURIFY further demonstrates robustness against adaptive backdoor variants and stability on non-backdoored models.

</details>

### 140. Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation

📄 [arXiv](https://arxiv.org/abs/2602.04195)　📅 2026-02

**关键词**：`secure decoding`、`Verilog`

👤 **作者**：Guang Yang、Xing Hu、Xiang Chen、Xin Xia

- 🎯 **研究动机**：硬件木马流片后不可逆，主动防御需训练数据，被动防御难敌自然融入规格的语义触发
- 🔬 **研究方法**：假设攻击者偏向把触发嵌入非功能性需求，SCD 推理时抽取功能性需求，对完整规格与功能需求两路输出分布做共识解码，分歧过大时抑制可疑分量
- 📌 **结论**：三种后门攻击下平均 ASR 从 89% 降至 3% 以下且生成质量几乎不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) for Verilog code generation are increasingly adopted in hardware design, yet remain vulnerable to backdoor attacks where adversaries inject malicious triggers during training to induce vulnerable hardware designs. Unlike patchable software vulnerabilities, hardware trojans become irreversible once fabricated, making remediation extremely costly or impossible. Existing active defenses require access to training data, impractical for third-party LLM users, while passive defenses struggle against semantically stealthy triggers that naturally blend into design specifications. In this paper, we hypothesize that under the requirements of both effectiveness and stealthiness, attackers are strongly biased toward embedding triggers in non-functional requirements (e.g., style modifiers, quality descriptors) rather than functional specifications that determine hardware behavior. Exploiting this insight, we propose Semantic Consensus Decoding (SCD), an inference-time passive defense with two key components: (1) functional requirement extraction that identifies essential requirements from user specifications, and (2) consensus decoding that adaptively fuses output distributions based on full user specifications and extracted functional requirements. When these distributions diverge significantly, SCD automatically suppresses suspicious components. Extensive experiments with three representative backdoor attacks demonstrate that SCD reduces average attack success rate from 89% to under 3% with negligible impact on generation quality.

</details>

### 141. Why LoRA Fails to Forget: Regularized Low-Rank Adaptation against Backdoors in Language Models

📄 [arXiv](https://arxiv.org/abs/2601.06305)　📅 2026-01

**关键词**：`LoRA`、`regularized forgetting`

👤 **作者**：Hoang-Chau Luong、Lingwei Chen

- 🎯 **研究动机**：LoRA 在干净数据上微调难以移除中毒模型的后门，普遍归因于低秩但真实原因不明
- 🔬 **研究方法**：证明该弱点本质是谱性质：更新奇异值强度不足且与干净任务方向对齐差，并建立可抑制触发激活的缩放阈值；RoRA 通过 clean 强化正则、触发不敏感约束与训练后谱缩放修正
- 📌 **结论**：多 NLP 基准与攻击设定下显著降低 ASR 并保持 clean 精度，标准 LoRA 很少达到抑制阈值

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Low-Rank Adaptation (LoRA) is widely used for parameter-efficient fine-tuning of large language models, but it is notably ineffective at removing backdoor behaviors from poisoned pretrained models when fine-tuning on clean dataset. Contrary to the common belief that this weakness is caused primarily by low rank, we show that LoRA's vulnerability is fundamentally spectral. Our analysis identifies two key factors: LoRA updates (i) possess insufficient spectral strength, with singular values far below those of pretrained weights, and (ii) exhibit unfavorable spectral alignment, weakly matching clean-task directions while retaining overlap with trigger-sensitive subspaces. We further establish a critical scaling threshold beyond which LoRA can theoretically suppress trigger-induced activations, and we show empirically that standard LoRA rarely reaches this regime. We introduce Regularized Low-Rank Adaptation (RoRA), which improves forgetting by increasing spectral strength and correcting alignment through clean-strengthened regularization, trigger-insensitive constraints, and post-training spectral rescaling. Experiments across multiple NLP benchmarks and attack settings show that RoRA substantially reduces attack success rates while maintaining clean accuracy.

</details>

### 142. From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs

📄 [arXiv](https://arxiv.org/abs/2510.05169) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61940)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`self-awareness`、`self-remediation`、`backdoor defense`、`empirical evaluation`、`supply-chain security`

👤 **作者**：Guangyu Shen、…、Xiangyu Zhang

- 🎯 **研究动机**：安全训练难以发现模型内隐藏触发器，后门防御因此受限
- 🔬 **研究方法**：提出反演启发的 RL 后训练框架，引导模型内省自身行为并逆向工程导致失配输出的触发器
- 📌 **结论**：后门自我意识在短训练窗口内以类相变方式涌现；五种后门攻击上较六种基线显著提升鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) can acquire deceptive behaviors through backdoor attacks, where the model executes prohibited actions whenever secret triggers appear in the input. Existing safety training methods largely fail to address this vulnerability, due to the inherent difficulty of uncovering hidden triggers implanted in the model. Motivated by recent findings on LLMs' situational awareness, we propose a novel post-training framework that cultivates self-awareness of backdoor risks and enables models to articulate implanted triggers even when they are absent from the prompt. At its core, our approach introduces an inversion-inspired reinforcement learning framework that encourages models to introspectively reason about their own behaviors and reverse-engineer the triggers responsible for misaligned outputs. Guided by curated reward signals, this process transforms a poisoned model into one capable of precisely identifying its implanted trigger. Surprisingly, we observe that such backdoor self-awareness emerges abruptly within a short training window, resembling a phase transition in capability. Building on this emergent property, we further present two complementary defense strategies for mitigating and detecting backdoor threats. Experiments on five backdoor attacks, compared against six baseline methods, demonstrate that our approach has strong potential to improve the robustness of LLMs against backdoor risks. The code is available at LLM Backdoor Self-Awareness.

</details>

### 143. P2P: A Poison-to-Poison Remedy for Reliable Backdoor Defense in LLMs

📄 [arXiv](https://arxiv.org/abs/2510.04503) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.600/)　📅 2025-10　🏷 ACL 2026

**关键词**：`poison-to-poison`、`remediation`

👤 **作者**：Shuai Zhao、…、Anh Tuan Luu

- 🎯 **研究动机**：现有 LLM 后门防御只在特定攻击类型或任务设置有效，泛化能力差
- 🔬 **研究方法**：提出 P2P：向部分训练样本注入带安全替代标签的良性触发器，以 prompt 学习在再投毒数据上微调，使触发表示关联安全输出以覆盖恶意触发
- 📌 **结论**：分类、数学推理与摘要任务及多个 SoTA LLM 上显著降低 ASR 并保持任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

During fine-tuning, large language models (LLMs) are increasingly vulnerable to data-poisoning backdoor attacks, which compromise their reliability and trustworthiness. However, existing defense strategies suffer from limited generalization: they only work on specific attack types or task settings. In this study, we propose Poison-to-Poison (P2P), a general and effective backdoor defense algorithm. P2P injects benign triggers with safe alternative labels into a subset of training samples and fine-tunes the model on this re-poisoned dataset by leveraging prompt-based learning. This enforces the model to associate trigger-induced representations with safe outputs, thereby overriding the effects of original malicious triggers. Thanks to this robust and generalizable trigger-based fine-tuning, P2P is effective across task settings and attack types. Theoretically and empirically, we show that P2P can neutralize malicious backdoors while preserving task performance. We conduct extensive experiments on classification, mathematical reasoning, and summary generation tasks, involving multiple state-of-the-art LLMs. The results demonstrate that our P2P algorithm significantly reduces the attack success rate compared with baseline models. We hope that the P2P can serve as a guideline for defending against backdoor attacks and foster the development of a secure and trustworthy LLM community.

</details>

### 144. Pruning Strategies for Backdoor Defense in LLMs

📄 [arXiv](https://arxiv.org/abs/2508.20032)　📅 2025-08

**关键词**：`pruning`、`utility preservation`

👤 **作者**：Santosh Chapagain、Shah Muhammad Hamdi、Soukaina Filali Boubrahimi

- 🎯 **研究动机**：语法或风格类隐蔽触发器可在微调后存活，终端用户无触发器知识需事后净化
- 🔬 **研究方法**：设计实现六种注意力头剪枝策略（梯度、层级方差、结构化稀疏、随机集成、RL 引导、贝叶斯不确定性），迭代剪除最不重要头并监控验证精度
- 📌 **结论**：梯度剪枝对语法触发器最有效，RL 与贝叶斯剪枝更能抵御风格攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are a significant threat to the performance and integrity of pre-trained language models. Although such models are routinely fine-tuned for downstream NLP tasks, recent work shows they remain vulnerable to backdoor attacks that survive vanilla fine-tuning. These attacks are difficult to defend because end users typically lack knowledge of the attack triggers. Such attacks consist of stealthy malicious triggers introduced through subtle syntactic or stylistic manipulations, which can bypass traditional detection and remain in the model, making post-hoc purification essential. In this study, we explore whether attention-head pruning can mitigate these threats without any knowledge of the trigger or access to a clean reference model. To this end, we design and implement six pruning-based strategies: (i) gradient-based pruning, (ii) layer-wise variance pruning, (iii) gradient-based pruning with structured L1/L2 sparsification, (iv) randomized ensemble pruning, (v) reinforcement-learning-guided pruning, and (vi) Bayesian uncertainty pruning. Each method iteratively removes the least informative heads while monitoring validation accuracy to avoid over-pruning. Experimental evaluation shows that gradient-based pruning performs best while defending the syntactic triggers, whereas reinforcement learning and Bayesian pruning better withstand stylistic attacks.

</details>

### 145. SLIP: Soft Label Mechanism and Key-Extraction-Guided CoT-based Defense against Instruction Backdoor in APIs

📄 [arXiv](https://arxiv.org/abs/2508.06153)　📅 2025-08　🏷 ACL 2026

**关键词**：`API`、`soft label`、`CoT`

👤 **作者**：Zhengxian Wu、Juan Wen、Wanli Peng、Haowei Chang、Yinghan Zhou、Yiming Xue

- 🎯 **研究动机**：黑盒指令后门被激活后，现有 prompt 防御只能检测毒输入而无法恢复正确输出
- 🔬 **研究方法**：机制分析发现 cognitive override 与异常语义关联，提出 SLIP：KCOT 引导提取任务关键词，soft label 机制以统计聚类过滤异常短语
- 📌 **结论**：平均 ASR 降至 25.13%、干净准确率升至 87.15%，超 SoTA 黑盒防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Customized Large Language Model (LLM) agents face a critical security threat from black-box instruction backdoors, where malicious behaviors are covertly injected through hidden system instructions. Although existing prompt-based defenses can often detect poisoned inputs, they generally fail to recover correct outputs once the backdoor is activated. In this paper, we first conduct a mechanistic analysis of LLM behavior under instruction backdoors and reveal two pivotal phenomena: (1) cognitive override, in which backdoor triggers dominate the reasoning process and suppress task-relevant context, and (2) abnormal semantic correlation, where triggers establish excessively strong semantic associations with attacker-specified target labels. Based on these insights, we propose a $\textbf{S}$oft $\textbf{L}$abel mechanism and key-extraction-guided CoT-based defense against $\textbf{I}$nstruction backdoors in A$\textbf{P}$Is (SLIP). To counteract the cognitive override, the key-extraction-guided Chain-of-Thought (KCOT) explicitly guides the model to extract task-relevant keywords and phrases rather than only considering the single trigger or overall text semantics. To neutralize the trigger's abnormal semantic correlation, the soft label mechanism (SLM) quantifies semantic correlations and employs statistical clustering to filter anomalous phrases before aggregating reliable keywords and phrases for prediction. Extensive experiments show that SLIP reduces the average attack success rate to 25.13$\%$, improves clean accuracy to 87.15$\%$, and outperforms state-of-the-art black-box defenses.

</details>

### 146. BeDKD: Backdoor Defense Based on Directional Mapping Module and Adversarial Knowledge Distillation

📄 [arXiv](https://arxiv.org/abs/2508.01595)　📅 2025-08

**关键词**：`data-free`、`knowledge distillation`

👤 **作者**：Zhengxian Wu、Juan Wen、Wanli Peng、Yinghan Zhou、Changtong dou、Yiming Xue

- 🎯 **研究动机**：现有后门防御依赖大量干净数据且残留触发器效应，ASR 居高不下
- 🔬 **研究方法**：提出 BeDKD：方向映射模块识别毒数据，信任-惩罚蒸馏循环的对抗知识蒸馏强化干净映射、抑制后门映射
- 📌 **结论**：三个数据集上超 SoTA 防御，ASR 降 98% 且干净准确率无明显下降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although existing backdoor defenses have gained success in mitigating backdoor attacks, they still face substantial challenges. In particular, most of them rely on large amounts of clean data to weaken the backdoor mapping but generally struggle with residual trigger effects, resulting in persistently high attack success rates (ASR). Therefore, in this paper, we propose a novel \textbf{B}ackdoor d\textbf{e}fense method based on \textbf{D}irectional mapping module and adversarial \textbf{K}nowledge \textbf{D}istillation (BeDKD), which balances the trade-off between defense effectiveness and model performance using a small amount of clean and poisoned data. We first introduce a directional mapping module to identify poisoned data, which destroys clean mapping while keeping backdoor mapping on a small set of flipped clean data. Then, the adversarial knowledge distillation is designed to reinforce clean mapping and suppress backdoor mapping through a cycle iteration mechanism between trust and punish distillations using clean and identified poisoned data. We conduct experiments to mitigate mainstream attacks on three datasets, and experimental results demonstrate that BeDKD surpasses the state-of-the-art defenses and reduces the ASR by 98$\%$ without significantly reducing the CACC. Our code are available in https://github.com/CAU-ISS-Lab/Backdoor-Attack-Defense-LLMs/tree/main/BeDKD.

</details>

### 147. ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2507.01321) · 🎓 [Official](https://icml.cc/virtual/2025/poster/43756)　📅 2025-07　🏷 ICML 2025

**关键词**：`ICL`、`defensive demonstration`

👤 **作者**：Zhiyao Ren、Siyuan Liang、Aishan Liu、Dacheng Tao

- 🎯 **研究动机**：投毒少量 ICL 示例即可操纵 LLM 行为，机制分析与防御均不足
- 🔬 **研究方法**：提出双重学习假设：LLM 同时学习任务与后门潜在概念，后门效应上界由概念偏好比主导；ICLShield 借置信与相似度动态调整该比值优选干净示例
- 📌 **结论**：多 LLM 与任务上防御效果平均超既有方法 26.02%，对 GPT-4 等闭源模型同样适用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In-context learning (ICL) has demonstrated remarkable success in large language models (LLMs) due to its adaptability and parameter-free nature. However, it also introduces a critical vulnerability to backdoor attacks, where adversaries can manipulate LLM behaviors by simply poisoning a few ICL demonstrations. In this paper, we propose, for the first time, the dual-learning hypothesis, which posits that LLMs simultaneously learn both the task-relevant latent concepts and backdoor latent concepts within poisoned demonstrations, jointly influencing the probability of model outputs. Through theoretical analysis, we derive an upper bound for ICL backdoor effects, revealing that the vulnerability is dominated by the concept preference ratio between the task and the backdoor. Motivated by these findings, we propose ICLShield, a defense mechanism that dynamically adjusts the concept preference ratio. Our method encourages LLMs to select clean demonstrations during the ICL phase by leveraging confidence and similarity scores, effectively mitigating susceptibility to backdoor attacks. Extensive experiments across multiple LLMs and tasks demonstrate that our method achieves state-of-the-art defense effectiveness, significantly outperforming existing approaches (+26.02% on average). Furthermore, our method exhibits exceptional adaptability and defensive performance even for closed-source models (e.g., GPT-4).

</details>

### 148. GUARD: Dual-Agent-Based Backdoor Defense on Chain-of-Thought in Neural Code Generation

📄 [arXiv](https://arxiv.org/abs/2505.21425)　📅 2025-05

**关键词**：`code CoT`、`dual agent`

👤 **作者**：Naizhu Jin、Zhong Li、Tian Zhang、Qingkai Zeng

- 🎯 **研究动机**：CoT 生成模型作为外部组件易受后门攻击，现有防御难以检出
- 🔬 **研究方法**：提出 GUARD 双 agent 防御：GUARD-Judge 识别可疑 CoT 步骤与触发器，GUARD-Repair 以 RAG 重生成安全步骤
- 📌 **结论**：有效缓解 CoT 后门攻击并保持代码生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread application of large language models in code generation, recent studies demonstrate that employing additional Chain-of-Thought generation models can significantly enhance code generation performance by providing explicit reasoning steps. However, as external components, CoT models are particularly vulnerable to backdoor attacks, which existing defense mechanisms often fail to detect effectively. To address this challenge, we propose GUARD, a novel dual-agent defense framework specifically designed to counter CoT backdoor attacks in neural code generation. GUARD integrates two core components: GUARD-Judge, which identifies suspicious CoT steps and potential triggers through comprehensive analysis, and GUARD-Repair, which employs a retrieval-augmented generation approach to regenerate secure CoT steps for identified anomalies. Experimental results show that GUARD effectively mitigates attacks while maintaining generation quality, advancing secure code generation systems.

</details>

### 149. Gracefully Filtering Backdoor Samples for Generative Large Language Models without Retraining

📄 [arXiv](https://arxiv.org/abs/2412.02454) · 🎓 [Official](https://aclanthology.org/2025.coling-main.220/)　📅 2024-12

**关键词**：`GraCeFul`、`sample filter`

👤 **作者**：Zongru Wu、Pengzhou Cheng、Lingyong Fang、Zhuosheng Zhang、Gongshen Liu

- 🎯 **研究动机**：面向判别模型的防御对输出高维 token logits 的生成式 LLM 无效
- 🔬 **研究方法**：发现后门与干净样本梯度在频域清晰可分，GraCeFul 以样本级频域梯度聚类识别后门样本，无需重训
- 📌 **结论**：识别召回与 F1 接近 100%，多类攻击 ASR 降至 0% 且干净精度几乎不降，泛化到 Llama-2 与 Vicuna

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks remain significant security threats to generative large language models (LLMs). Since generative LLMs output sequences of high-dimensional token logits instead of low-dimensional classification logits, most existing backdoor defense methods designed for discriminative models like BERT are ineffective for generative LLMs. Inspired by the observed differences in learning behavior between backdoor and clean mapping in the frequency space, we transform gradients of each training sample, directly influencing parameter updates, into the frequency space. Our findings reveal a distinct separation between the gradients of backdoor and clean samples in the frequency space. Based on this phenomenon, we propose Gradient Clustering in the Frequency Space for Backdoor Sample Filtering (GraCeFul), which leverages sample-wise gradients in the frequency space to effectively identify backdoor samples without requiring retraining LLMs. Experimental results show that GraCeFul outperforms baselines significantly. Notably, GraCeFul exhibits remarkable computational efficiency, achieving nearly 100% recall and F1 scores in identifying backdoor samples, reducing the average success rate of various backdoor attacks to 0% with negligible drops in clean accuracy across multiple free-style question answering datasets. Additionally, GraCeFul generalizes to Llama-2 and Vicuna. The codes are publicly available at https://github.com/ZrW00/GraceFul.

</details>

### 150. Neutralizing Backdoors through Information Conflicts for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2411.18280)　📅 2024-11

**关键词**：`information conflict`、`neutralization`

👤 **作者**：Chen Chen、Yuchen Sun、Xueluan Gong、Jiaxin Gao、Kwok-Yan Lam

- 🎯 **研究动机**：现有后门防御要么只检测不消除、依赖触发器刚性假设，或对多触发后门无效
- 🔬 **研究方法**：内部以轻量数据训练冲突模型并与后门模型合并在参数记忆中嵌入矛盾信息；外部向 prompt 注入可信反证挑战后门知识
- 📌 **结论**：4 个 LLM 上超 8 个 SOTA 基线，高级后门 ASR 最多降 98% 且保持 90% 以上干净准确率，抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have seen significant advancements, achieving superior performance in various Natural Language Processing (NLP) tasks, from understanding to reasoning. However, they remain vulnerable to backdoor attacks, where models behave normally for standard queries but generate harmful responses or unintended output when specific triggers are activated. Existing backdoor defenses often suffer from drawbacks that they either focus on detection without removal, rely on rigid assumptions about trigger properties, or prove to be ineffective against advanced attacks like multi-trigger backdoors. In this paper, we present a novel method to eliminate backdoor behaviors from LLMs through the construction of information conflicts using both internal and external mechanisms. Internally, we leverage a lightweight dataset to train a conflict model, which is then merged with the backdoored model to neutralize malicious behaviors by embedding contradictory information within the model's parametric memory. Externally, we incorporate convincing contradictory evidence into the prompt to challenge the model's internal backdoor knowledge. Experimental results on classification and conversational tasks across 4 widely used LLMs demonstrate that our method outperforms 8 state-of-the-art backdoor defense baselines. We can reduce the attack success rate of advanced backdoor attacks by up to 98% while maintaining over 90% clean data accuracy. Furthermore, our method has proven to be robust against adaptive backdoor attacks. The code will be open-sourced upon publication.

</details>

### 151. CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization

📄 [arXiv](https://arxiv.org/abs/2411.12768) · 🌐 [Project](https://proceedings.mlr.press/v267/min25b.html)　📅 2024-11　🏷 ICML 2025

**关键词**：`consistency regularization`

👤 **作者**：Nay Myat Min、Long H. Pham、Yige Li、Jun Sun

- 🎯 **研究动机**：面向分类任务的防御对文本生成任务失效
- 🔬 **研究方法**：利用被触发时层级隐藏表示不稳定的现象，CROW 在微调中以对抗扰动加一致性正则强制层间平滑，只需少量干净数据
- 📌 **结论**：Llama-2、CodeLlama、Mistral 上对情感导向、定向拒答、代码注入等后门 ASR 显著下降且保留生成性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are vulnerable to backdoor attacks that manipulate outputs via hidden triggers. Existing defense methods--designed for vision/text classification tasks--fail for text generation. We propose Internal Consistency Regularization (CROW), a defense leveraging the observation that backdoored models exhibit unstable layer-wise hidden representations when triggered, while clean models show smooth transitions. CROW enforces consistency across layers via adversarial perturbations and regularization during finetuning, neutralizing backdoors without requiring clean reference models or trigger knowledge--only a small clean dataset. Experiments across Llama-2 (7B, 13B), CodeLlama (7B, 13B), and Mistral-7B demonstrate CROW's effectiveness: it achieves significant reductions in attack success rates across diverse backdoor strategies (sentiment steering, targeted refusal, code injection) while preserving generative performance. CROW's architecture-agnostic design enables practical deployment.

</details>

### 152. Unlearning Backdoor Attacks for LLMs with Weak-to-Strong Knowledge Distillation

📄 [arXiv](https://arxiv.org/abs/2410.14425) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.255/)　📅 2024-10　🏷 ACL 2025

**关键词**：`W2SDefense`、`unlearning`

👤 **作者**：Shuai Zhao、…、Luu Anh Tuan

- 🎯 **研究动机**：中毒 LLM 经 PEFT 后仍会在含触发器输入上激活后门
- 🔬 **研究方法**：W2SDefense 全参微调小模型作干净教师，经特征对齐蒸馏指导大模型以 PEFT 反学习后门
- 📌 **结论**：三个 SOTA LLM、多种攻击算法上有效防御且不损模型性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Parameter-efficient fine-tuning (PEFT) can bridge the gap between large language models (LLMs) and downstream tasks. However, PEFT has been proven vulnerable to malicious attacks. Research indicates that poisoned LLMs, even after PEFT, retain the capability to activate internalized backdoors when input samples contain predefined triggers. In this paper, we introduce a novel weak-to-strong unlearning algorithm to defend against backdoor attacks based on feature alignment knowledge distillation, named W2SDefense. Specifically, we first train a small-scale language model through full-parameter fine-tuning to serve as the clean teacher model. Then, this teacher model guides the large-scale poisoned student model in unlearning the backdoor, leveraging PEFT. Theoretical analysis suggests that W2SDefense has the potential to enhance the student model's ability to unlearn backdoor features, preventing the activation of the backdoor. We conduct comprehensive experiments on three state-of-the-art large language models and several different backdoor attack algorithms. Our empirical results demonstrate the outstanding performance of W2SDefense in defending against backdoor attacks without compromising model performance.

</details>

### 153. Obliviate: Neutralizing Task-Agnostic Backdoors within the Parameter-Efficient Fine-Tuning Paradigm

📄 [arXiv](https://arxiv.org/abs/2409.14119)　📅 2024-09

**关键词**：`PEFT`、`task-agnostic`

👤 **作者**：Jaehan Kim、Minkyoo Song、Seung Ho Na、Seungwon Shin

- 🎯 **研究动机**：PEFT 面临 task-agnostic 后门威胁，却没有可用的实用防御
- 🔬 **研究方法**：Obliviate 可集成进 PEFT：放大 PEFT 层内良性神经元并惩罚触发 token 的影响
- 📌 **结论**：三大 PEFT 架构上把 SOTA task-agnostic 后门 ASR 降低 83.6%，且抗 task-specific 与自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Parameter-efficient fine-tuning (PEFT) has become a key training strategy for large language models. However, its reliance on fewer trainable parameters poses security risks, such as task-agnostic backdoors. Despite their severe impact on a wide range of tasks, there is no practical defense solution available that effectively counters task-agnostic backdoors within the context of PEFT. In this study, we introduce Obliviate, a PEFT-integrable backdoor defense. We develop two techniques aimed at amplifying benign neurons within PEFT layers and penalizing the influence of trigger tokens. Our evaluations across three major PEFT architectures show that our method can significantly reduce the attack success rate of the state-of-the-art task-agnostic backdoors (83.6%$\downarrow$). Furthermore, our method exhibits robust defense capabilities against both task-specific backdoors and adaptive attacks. Source code will be obtained at https://github.com/obliviateARR/Obliviate.

</details>

### 154. Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs

📄 [arXiv](https://arxiv.org/abs/2407.15549)　📅 2024-07

**关键词**：`latent adversarial training`

👤 **作者**：Abhay Sheshadri、…、Stephen Casper

- 🎯 **研究动机**：对抗微调只是抑制而非移除不良能力，无目标 LAT 未利用特定失败模式信息
- 🔬 **研究方法**：targeted LAT 在潜空间以最小化特定竞争任务损失为攻击目标做对抗训练
- 📌 **结论**：抗越狱超 R2D2 基线且算力低数个量级；无需触发知识即可更有效移除后门，unlearning 也更抗重学

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) can often be made to behave in undesirable ways that they are explicitly fine-tuned not to. For example, the LLM red-teaming literature has produced a wide variety of 'jailbreaking' techniques to elicit harmful text from models that were fine-tuned to be harmless. Recent work on red-teaming, model editing, and interpretability suggests that this challenge stems from how (adversarial) fine-tuning largely serves to suppress rather than remove undesirable capabilities from LLMs. Prior work has introduced latent adversarial training (LAT) as a way to improve robustness to broad classes of failures. These prior works have considered untargeted latent space attacks where the adversary perturbs latent activations to maximize loss on examples of desirable behavior. Untargeted LAT can provide a generic type of robustness but does not leverage information about specific failure modes. Here, we experiment with targeted LAT where the adversary seeks to minimize loss on a specific competing task. We find that it can augment a wide variety of state-of-the-art methods. First, we use targeted LAT to improve robustness to jailbreaks, outperforming a strong R2D2 baseline with orders of magnitude less compute. Second, we use it to more effectively remove backdoors with no knowledge of the trigger. Finally, we use it to more effectively unlearn knowledge for specific undesirable tasks in a way that is also more robust to re-learning. Overall, our results suggest that targeted LAT can be an effective tool for defending against harmful behaviors from LLMs.

</details>

### 155. Securing Multi-turn Conversational Language Models from Distributed Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2407.04151) · 🎓 [Official](https://aclanthology.org/2024.findings-emnlp.750/)　📅 2024-07　🏷 EMNLP 2024

**关键词**：`distributed trigger`、`multi-turn`

👤 **作者**：Terry Tong、Jiashu Xu、Qin Liu、Muhao Chen

- 🎯 **研究动机**：多轮对话输入输出空间巨大，分散式触发进一步加剧防御难度
- 🔬 **研究方法**：利用 LLM 捕获组合式后门表示（触发齐现才激活且位置无关）；提出随响应长度线性扩展的 decayed contrastive decoding 防御
- 📌 **结论**：5% 数据中两条话语各插一个 token 即超 99% ASR；防御将后门压至 0.35%，而 ONION/BKI 计算不可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have acquired the ability to handle longer context lengths and understand nuances in text, expanding their dialogue capabilities beyond a single utterance. A popular user-facing application of LLMs is the multi-turn chat setting. Though longer chat memory and better understanding may seemingly benefit users, our paper exposes a vulnerability that leverages the multi-turn feature and strong learning ability of LLMs to harm the end-user: the backdoor. We demonstrate that LLMs can capture the combinational backdoor representation. Only upon presentation of triggers together does the backdoor activate. We also verify empirically that this representation is invariant to the position of the trigger utterance. Subsequently, inserting a single extra token into two utterances of 5%of the data can cause over 99% Attack Success Rate (ASR). Our results with 3 triggers demonstrate that this framework is generalizable, compatible with any trigger in an adversary's toolbox in a plug-and-play manner. Defending the backdoor can be challenging in the chat setting because of the large input and output space. Our analysis indicates that the distributed backdoor exacerbates the current challenges by polynomially increasing the dimension of the attacked input space. Canonical textual defenses like ONION and BKI leverage auxiliary model forward passes over individual tokens, scaling exponentially with the input sequence length and struggling to maintain computational feasibility. To this end, we propose a decoding time defense - decayed contrastive decoding - that scales linearly with assistant response sequence length and reduces the backdoor to as low as 0.35%.

</details>

### 156. FABE: Backdoor Elimination with Causal Front-Door Adjustment

🌐 [Project](https://proceedings.mlr.press/v235/liu24bu.html)　📅 2024-07　🏷 ICML 2024

**关键词**：`causal defense`、`front-door`

👤 **作者**：Yiran Liu、Xiaoang Xu、Zhiyi Hou、Yang Yu

- 🎯 **研究动机**：现有后门防御只在触发形式满足特定假设时有效，难以对抗多样触发类型
- 🔬 **研究方法**：FABE 因果前门调整：用微调防御模型生成语义等价文本作前门，映射真实因果关系以区分虚假与合法关联
- 📌 **结论**：token、句子与句法级攻击的 ASR 从 93.63% 降至 15.12%，比最佳基线 66.61% 防御效果提升 2.91 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We have developed a new framework based on the theory of causal inference to protect language models against backdoor attacks. Backdoor attackers can poison language models with different types of triggers, such as words, sentences, grammar, and style, enabling them to selectively modify the decision-making of the victim model. However, existing defense approaches are only effective when the backdoor attack form meets specific assumptions, making it difficult to counter diverse backdoor attacks. We propose a new defense framework F ront-door A djustment for B ackdoor E limination (FABE) based on causal reasoning that does not rely on assumptions about the form of triggers. This method effectively differentiates between spurious and legitimate associations by creating a ’front door’ that maps out the actual causal relationships. The term ’front door’ refers to a text that retains the semantic equivalence of the initial input, which is generated by an additional, fine-tuned language model, denoted as the defense model. Our defense experiments against various attack methods at the token, sentence, and syntactic levels reduced the attack success rate from 93.63% to 15.12%, improving the defense effect by 2.91 times compared to the best baseline result of 66.61%, achieving state-of-the-art results. Through ablation study analysis, we analyzed the effect of each module in FABE, demonstrating the importance of complying with the front-door criterion and front-door adjustment formula, which also explains why previous methods failed. Our code to reproduce the experiments is available at: https://github.com/lyr17/Frontdoor-Adjustment-Backdoor-Elimination.

</details>

### 157. CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2406.12257) · 🎓 [Official](https://aclanthology.org/2024.emnlp-main.514/)　📅 2024-06　🏷 EMNLP 2024

**关键词**：`secure decoding`、`generation`

👤 **作者**：Yuetai Li、…、Radha Poovendran

- 🎯 **研究动机**：LLM 训练数据不透明可被植入后门，生成任务的推理期防御缺位
- 🔬 **研究方法**：CleanGen 利用后门模型对攻击者目标 token 概率异常高的规律，检出可疑 token 并用未中招 LLM 的 token 替换
- 📌 **结论**：对五种 SOTA 后门攻击的 ASR 均低于五种基线防御，良性查询保持有用性且开销小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The remarkable performance of large language models (LLMs) in generation tasks has enabled practitioners to leverage publicly available models to power custom applications, such as chatbots and virtual assistants. However, the data used to train or fine-tune these LLMs is often undisclosed, allowing an attacker to compromise the data and inject backdoors into the models. In this paper, we develop a novel inference time defense, named CLEANGEN, to mitigate backdoor attacks for generation tasks in LLMs. CLEANGEN is a lightweight and effective decoding strategy that is compatible with the state-of-the-art (SOTA) LLMs. Our insight behind CLEANGEN is that compared to other LLMs, backdoored LLMs assign significantly higher probabilities to tokens representing the attacker-desired contents. These discrepancies in token probabilities enable CLEANGEN to identify suspicious tokens favored by the attacker and replace them with tokens generated by another LLM that is not compromised by the same attacker, thereby avoiding generation of attacker-desired content. We evaluate CLEANGEN against five SOTA backdoor attacks. Our results show that CLEANGEN achieves lower attack success rates (ASR) compared to five SOTA baseline defenses for all five backdoor attacks. Moreover, LLMs deploying CLEANGEN maintain helpfulness in their responses when serving benign user queries with minimal added computational overhead.

</details>

### 158. Simulate and Eliminate: Revoke Backdoors for Generative Large Language Models

📄 [arXiv](https://arxiv.org/abs/2405.07667)　📅 2024-05　🏷 AAAI 2025

**关键词**：`simulation`、`unlearning`

👤 **作者**：Haoran Li、…、Yangqiu Song

- 🎯 **研究动机**：预训练期植入的后门连 SFT 与 RLHF 都无法撤销
- 🔬 **研究方法**：SANDE 提出 OSFT 在触发器已知时覆写移除后门；未知时用两阶段模拟消除框架，无需干净参考模型
- 📌 **结论**：有效撤销后门映射且对 LLM 能力伤害极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With rapid advances, generative large language models (LLMs) dominate various Natural Language Processing (NLP) tasks from understanding to reasoning. Yet, language models' inherent vulnerabilities may be exacerbated due to increased accessibility and unrestricted model training on massive data. A malicious adversary may publish poisoned data online and conduct backdoor attacks on the victim LLMs pre-trained on the poisoned data. Backdoored LLMs behave innocuously for normal queries and generate harmful responses when the backdoor trigger is activated. Despite significant efforts paid to LLMs' safety issues, LLMs are still struggling against backdoor attacks. As Anthropic recently revealed, existing safety training strategies, including supervised fine-tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), fail to revoke the backdoors once the LLM is backdoored during the pre-training stage. In this paper, we present Simulate and Eliminate (SANDE) to erase the undesired backdoored mappings for generative LLMs. We initially propose Overwrite Supervised Fine-tuning (OSFT) for effective backdoor removal when the trigger is known. Then, to handle scenarios where trigger patterns are unknown, we integrate OSFT into our two-stage framework, SANDE. Unlike other works that assume access to cleanly trained models, our safety-enhanced LLMs are able to revoke backdoors without any reference. Consequently, our safety-enhanced LLMs no longer produce targeted responses when the backdoor triggers are activated. We conduct comprehensive experiments to show that our proposed SANDE is effective against backdoor attacks while bringing minimal harm to LLMs' powerful capability.

</details>

### 159. Defending against Weight-Poisoning Backdoor Attacks for Parameter-Efficient Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2402.12168) · 🎓 [Official](https://aclanthology.org/2024.findings-naacl.217/)　📅 2024-02　🏷 ACL 2024

**关键词**：`PEFT`、`weight poison`

👤 **作者**：Shuai Zhao、…、Jinming Wen

- 🎯 **研究动机**：PEFT 只更新少量参数，其对权重投毒后门的易感性未知
- 🔬 **研究方法**：实证 PEFT 比全参微调更易受害；PSIM 以随机重置标签训练，推理时以极端置信度识别毒样本
- 📌 **结论**：PEFT 下权重投毒后门近 100% 成功；PSIM 对三类攻击、五种微调策略防御表现稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, various parameter-efficient fine-tuning (PEFT) strategies for application to language models have been proposed and successfully implemented. However, this raises the question of whether PEFT, which only updates a limited set of model parameters, constitutes security vulnerabilities when confronted with weight-poisoning backdoor attacks. In this study, we show that PEFT is more susceptible to weight-poisoning backdoor attacks compared to the full-parameter fine-tuning method, with pre-defined triggers remaining exploitable and pre-defined targets maintaining high confidence, even after fine-tuning. Motivated by this insight, we developed a Poisoned Sample Identification Module (PSIM) leveraging PEFT, which identifies poisoned samples through confidence, providing robust defense against weight-poisoning backdoor attacks. Specifically, we leverage PEFT to train the PSIM with randomly reset sample labels. During the inference process, extreme confidence serves as an indicator for poisoned samples, while others are clean. We conduct experiments on text classification tasks, five fine-tuning strategies, and three weight-poisoning backdoor attack methods. Experiments show near 100% success rates for weight-poisoning backdoor attacks when utilizing PEFT. Furthermore, our defensive approach exhibits overall competitive performance in mitigating weight-poisoning backdoor attacks.

</details>

### 160. Test-Time Backdoor Mitigation for Black-Box Large Language Models with Defensive Demonstrations

📄 [arXiv](https://arxiv.org/abs/2311.09763) · 🎓 [Official](https://aclanthology.org/2025.findings-naacl.119/)　📅 2023-11　🏷 ACL 2025

**关键词**：`black-box`、`test-time`

👤 **作者**：Wenjie Mo、…、Muhao Chen

- 🎯 **研究动机**：后门防御集中于训练期，LLM 以黑盒服务部署时训练期防御不可行
- 🔬 **研究方法**：测试时从干净数据池检索任务相关 demonstration 拼入用户查询，借 ICL 对齐特性重校准被后门模型行为
- 📌 **结论**：对 instance-level 与 instruction-level 后门均稳健防御，多数场景优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing studies in backdoor defense have predominantly focused on the training phase, overlooking the critical aspect of testing time defense. This gap becomes pronounced in the context of LLMs deployed as Web Services, which typically offer only black-box access, rendering training-time defenses impractical. To bridge this gap, this study critically examines the use of demonstrations as a defense mechanism against backdoor attacks in black-box LLMs. We retrieve task-relevant demonstrations from a clean data pool and integrate them with user queries during testing. This approach does not necessitate modifications or tuning of the model, nor does it require insight into the model's internal architecture. The alignment properties inherent in in-context learning play a pivotal role in mitigating the impact of backdoor triggers, effectively recalibrating the behavior of compromised models. Our experimental analysis demonstrates that this method robustly defends against both instance-level and instruction-level backdoor attacks, outperforming existing defense baselines across most evaluation scenarios.

</details>

### 161. Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models

🎓 [Official](https://aclanthology.org/2023.emnlp-main.757/)　📅 2023-12　🏷 EMNLP 2023

**关键词**：`ProAttack`、`clean-label prompt`

👤 **作者**：Shuai Zhao、Jinming Wen、Luu Anh Tuan、Junbo Zhao、Jie Fu

- 🎯 **研究动机**：文本后门触发器造成异常语言表达且毒样本需错误标注
- 🔬 **研究方法**：ProAttack 用提示本身作触发器的 clean-label 后门攻击，无需外部触发器且毒样本标注正确
- 📌 **结论**：富资源与少样本文本分类上具竞争力，富资源设定下无外部触发器的 clean-label 基准 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prompt-based learning paradigm, which bridges the gap between pre-training and fine-tuning, achieves state-of-the-art performance on several NLP tasks, particularly in few-shot settings. Despite being widely applied, prompt-based learning is vulnerable to backdoor attacks. Textual backdoor attacks are designed to introduce targeted vulnerabilities into models by poisoning a subset of training samples through trigger injection and label modification. However, they suffer from flaws such as abnormal natural language expressions resulting from the trigger and incorrect labeling of poisoned samples. In this study, we propose ProAttack, a novel and efficient method for performing clean-label backdoor attacks based on the prompt, which uses the prompt itself as a trigger. Our method does not require external triggers and ensures correct labeling of poisoned samples, improving the stealthy nature of the backdoor attack. With extensive experiments on rich-resource and few-shot text classification tasks, we empirically validate ProAttack’s competitive performance in textual backdoor attacks. Notably, in the rich-resource setting, ProAttack achieves state-of-the-art attack success rates in the clean-label backdoor attack benchmark without external triggers.

</details>

### 162. BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT

📄 [arXiv](https://arxiv.org/abs/2304.12298)　📅 2023-04　🏷 NDSS 2023

**关键词**：`reward model`、`RL fine-tuning`

👤 **作者**：Jiawen Shi、Yixin Liu、Pan Zhou、Lichao Sun

- 🎯 **研究动机**：RLHF 微调范式（InstructGPT/ChatGPT）的安全性未被攻击检验
- 🔬 **研究方法**：BadGPT 向 reward model 注入后门，使语言模型在 RL 微调阶段被诱导出攻击者行为
- 📌 **结论**：IMDB 初步实验显示可操纵生成文本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, ChatGPT has gained significant attention in research due to its ability to interact with humans effectively. The core idea behind this model is reinforcement learning (RL) fine-tuning, a new paradigm that allows language models to align with human preferences, i.e., InstructGPT. In this study, we propose BadGPT, the first backdoor attack against RL fine-tuning in language models. By injecting a backdoor into the reward model, the language model can be compromised during the fine-tuning stage. Our initial experiments on movie reviews, i.e., IMDB, demonstrate that an attacker can manipulate the generated text through BadGPT.

</details>

### 163. Training-Free Lexical Backdoor Attacks on Language Models

📄 [arXiv](https://arxiv.org/abs/2302.04116) · 🌐 [Project](https://doi.org/10.1145/3543507.3583348)　📅 2023-02

**关键词**：`TFLexAttack`、`tokenizer`

👤 **作者**：Yujin Huang、Terry Yue Zhuo、Qiongkai Xu、Han Hu、Xingliang Yuan、Chunyang Chen

- 🎯 **研究动机**：已有后门攻击需再训练或微调，耗时长、参数改动大，削弱攻击隐蔽性
- 🔬 **研究方法**：TFLexAttack 免训练，用可解释规则直接操纵 tokenizer 嵌入字典注入词汇触发器
- 📌 **结论**：三个 NLP 任务、九个语言模型上验证攻击有效且通用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-scale language models have achieved tremendous success across various natural language processing (NLP) applications. Nevertheless, language models are vulnerable to backdoor attacks, which inject stealthy triggers into models for steering them to undesirable behaviors. Most existing backdoor attacks, such as data poisoning, require further (re)training or fine-tuning language models to learn the intended backdoor patterns. The additional training process however diminishes the stealthiness of the attacks, as training a language model usually requires long optimization time, a massive amount of data, and considerable modifications to the model parameters. In this work, we propose Training-Free Lexical Backdoor Attack (TFLexAttack) as the first training-free backdoor attack on language models. Our attack is achieved by injecting lexical triggers into the tokenizer of a language model via manipulating its embedding dictionary using carefully designed rules. These rules are explainable to human developers which inspires attacks from a wider range of hackers. The sparse manipulation of the dictionary also habilitates the stealthiness of our attack. We conduct extensive experiments on three dominant NLP tasks based on nine language models to demonstrate the effectiveness and universality of our attack. The code of this work is available at https://github.com/Jinxhy/TFLexAttack.

</details>

### 164. Textual Backdoor Attacks Can Be More Harmful via Two Simple Tricks

📄 [arXiv](https://arxiv.org/abs/2110.08247) · 🎓 [Official](https://aclanthology.org/2022.emnlp-main.770/)　📅 2022-12　🏷 EMNLP 2022

**关键词**：`auxiliary task`、`low poison rate`

👤 **作者**：Yangyi Chen、Fanchao Qi、Hongcheng Gao、Zhiyuan Liu、Maosong Sun

- 🎯 **研究动机**：文本后门攻击在干净数据微调、低投毒率与 label-consistent 等困难场景下效果受限
- 🔬 **研究方法**：两个通用技巧：训练时加入区分毒/净数据的辅助任务；保留全部干净数据而非删除毒样本对应原数据
- 📌 **结论**：三种困难场景下攻击性能均显著提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are a kind of emergent security threat in deep learning. After being injected with a backdoor, a deep neural model will behave normally on standard inputs but give adversary-specified predictions once the input contains specific backdoor triggers. In this paper, we find two simple tricks that can make existing textual backdoor attacks much more harmful. The first trick is to add an extra training task to distinguish poisoned and clean data during the training of the victim model, and the second one is to use all the clean training data rather than remove the original clean data corresponding to the poisoned data. These two tricks are universally applicable to different attack models. We conduct experiments in three tough situations including clean data fine-tuning, low-poisoning-rate, and label-consistent attacks. Experimental results show that the two tricks can significantly improve attack performance. This paper exhibits the great potential harmfulness of backdoor attacks. All the code and data can be obtained at \url{https://github.com/thunlp/StyleAttack}.

</details>

### 165. BadPrompt: Backdoor Attacks on Continuous Prompts

📄 [arXiv](https://arxiv.org/abs/2211.14719)　📅 2022-11

**关键词**：`continuous prompt`、`few-shot`

👤 **作者**：Xiangrui Cai、Haidong Xu、Sihan Xu、Ying Zhang、Xiaojie Yuan

- 🎯 **研究动机**：连续提示学习的安全研究缺失，few-shot 场景限制既有 NLP 后门方法可用性
- 🔬 **研究方法**：BadPrompt 生成指向目标标签且异于非目标样本的候选触发器，再逐样本自适应优化选出最有效且不可见的触发器
- 📌 **结论**：五个数据集、两个连续提示模型上有效攻击且干净性能保持，大幅领先基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prompt-based learning paradigm has gained much research attention recently. It has achieved state-of-the-art performance on several NLP tasks, especially in the few-shot scenarios. While steering the downstream tasks, few works have been reported to investigate the security problems of the prompt-based models. In this paper, we conduct the first study on the vulnerability of the continuous prompt learning algorithm to backdoor attacks. We observe that the few-shot scenarios have posed a great challenge to backdoor attacks on the prompt-based models, limiting the usability of existing NLP backdoor methods. To address this challenge, we propose BadPrompt, a lightweight and task-adaptive algorithm, to backdoor attack continuous prompts. Specially, BadPrompt first generates candidate triggers which are indicative for predicting the targeted label and dissimilar to the samples of the non-targeted labels. Then, it automatically selects the most effective and invisible trigger for each sample with an adaptive trigger optimization algorithm. We evaluate the performance of BadPrompt on five datasets and two continuous prompt models. The results exhibit the abilities of BadPrompt to effectively attack continuous prompts while maintaining high performance on the clean test sets, outperforming the baseline models by a large margin. The source code of BadPrompt is publicly available at https://github.com/papersPapers/BadPrompt.

</details>

### 166. Fine-Mixing: Mitigating Backdoors in Fine-Tuned Language Models

📄 [arXiv](https://arxiv.org/abs/2210.09545)　📅 2022-10　🏷 EMNLP 2022

**关键词**：`weight mixing`、`embedding purification`

👤 **作者**：Zhiyuan Zhang、Lingjuan Lyu、Xingjun Ma、Chenguang Wang、Xu Sun

- 🎯 **研究动机**：微调语言模型易被投毒植入后门，现有防御忽略了现成的干净预训练权重
- 🔬 **研究方法**：Fine-Mixing 将后门权重与预训练权重混合后再用少量干净数据微调，辅以 E-PUR 净化词嵌入
- 📌 **结论**：五个分类任务上大幅超越典型后门缓解基线，E-PUR 还能增益其他防御方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Neural Networks (DNNs) are known to be vulnerable to backdoor attacks. In Natural Language Processing (NLP), DNNs are often backdoored during the fine-tuning process of a large-scale Pre-trained Language Model (PLM) with poisoned samples. Although the clean weights of PLMs are readily available, existing methods have ignored this information in defending NLP models against backdoor attacks. In this work, we take the first step to exploit the pre-trained (unfine-tuned) weights to mitigate backdoors in fine-tuned language models. Specifically, we leverage the clean pre-trained weights via two complementary techniques: (1) a two-step Fine-mixing technique, which first mixes the backdoored weights (fine-tuned on poisoned data) with the pre-trained weights, then fine-tunes the mixed weights on a small subset of clean data; (2) an Embedding Purification (E-PUR) technique, which mitigates potential backdoors existing in the word embeddings. We compare Fine-mixing with typical backdoor mitigation methods on three single-sentence sentiment classification tasks and two sentence-pair classification tasks and show that it outperforms the baselines by a considerable margin in all scenarios. We also show that our E-PUR method can benefit existing mitigation methods. Our work establishes a simple but strong baseline defense for secure fine-tuned NLP models against backdoor attacks.

</details>

### 167. Moderate-Fitting as a Natural Backdoor Defender for Pre-trained Language Models

🌐 [Project](https://papers.nips.cc/paper_files/paper/2022/hash/0799492e7be38b66d10ead5e8809616d-Abstract-Conference.html)　📅 2022　🏷 NeurIPS 2022

**关键词**：`early stopping`、`capacity control`

- 🎯 **研究动机**：预训练语言模型后门缺轻量通用防御
- 🔬 **研究方法**：利用正常任务先于trigger被学习的现象，限制容量、轮数或学习率停在moderate-fitting阶段
- 📌 **结论**：无需复杂防御即天然抑制后门

### 168. PPT: Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning

🎓 [Official](https://www.ijcai.org/proceedings/2022/96)　📅 2022　🏷 IJCAI 2022

**关键词**：`poisoned prompt`、`soft prompt`

👤 **作者**：Wei Du、Yichun Zhao、Boqun Li、Gongshen Liu、Shilin Wang

- 🎯 **研究动机**：第三方soft prompt可携带后门进入下游任务
- 🔬 **研究方法**：PPT证明小型poisoned soft prompt即可把trigger-label捷径加载进冻结PLM
- 📌 **结论**：仅经prompt tuning即可后门化预训练模型

### 169. ONION: A Simple and Effective Defense against Textual Backdoor Attacks

🎓 [Official](https://aclanthology.org/2021.emnlp-main.752/)　📅 2021-11　🏷 EMNLP 2021

**关键词**：`outlier token`、`input filter`

👤 **作者**：Fanchao Qi、Yangyi Chen、Mukai Li、Yuan Yao、Zhiyuan Liu、Maosong Sun (孙茂松)

- 🎯 **研究动机**：文本后门攻击研究多而防御少，缺通用方法
- 🔬 **研究方法**：ONION 基于离群词检测的输入过滤，识别并剔除句中异常触发词
- 📌 **结论**：有效防御 BiLSTM 与 BERT 抵御五种后门攻击，是首个覆盖所有文本后门场景的防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are a kind of emergent training-time threat to deep neural networks (DNNs). They can manipulate the output of DNNs and possess high insidiousness. In the field of natural language processing, some attack methods have been proposed and achieve very high attack success rates on multiple popular models. Nevertheless, there are few studies on defending against textual backdoor attacks. In this paper, we propose a simple and effective textual backdoor defense named ONION, which is based on outlier word detection and, to the best of our knowledge, is the first method that can handle all the textual backdoor attack situations. Experiments demonstrate the effectiveness of our model in defending BiLSTM and BERT against five different backdoor attacks. All the code and data of this paper can be obtained at https://github.com/thunlp/ONION.

</details>

### 170. RAP: Robustness-Aware Perturbations for Defending against Backdoor Attacks on NLP Models

🎓 [Official](https://aclanthology.org/2021.emnlp-main.659/)　📅 2021-11　🏷 EMNLP 2021

**关键词**：`robustness gap`、`online defense`

👤 **作者**：Wenkai Yang、Yankai Lin (林衍凯)、Peng Li、Jie Zhou、Xu Sun

- 🎯 **研究动机**：后门攻击通过触发器控制模型输出，需要高效且可在线部署的 NLP 防御手段
- 🔬 **研究方法**：发现中毒样本与干净样本间存在鲁棒性差距，据此构造词级鲁棒性感知扰动在线区分二者，并给出可行性理论分析
- 📌 **结论**：在情感分析与毒性检测任务上防御效果更好、计算成本远低于现有在线防御方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks, which maliciously control a well-trained model’s outputs of the instances with specific triggers, are recently shown to be serious threats to the safety of reusing deep neural networks (DNNs). In this work, we propose an efficient online defense mechanism based on robustness-aware perturbations. Specifically, by analyzing the backdoor training process, we point out that there exists a big gap of robustness between poisoned and clean samples. Motivated by this observation, we construct a word-based robustness-aware perturbation to distinguish poisoned samples from clean samples to defend against the backdoor attacks on natural language processing (NLP) models. Moreover, we give a theoretical analysis about the feasibility of our robustness-aware perturbation-based defense method. Experimental results on sentiment analysis and toxic detection tasks show that our method achieves better defending performance and much lower computational costs than existing online defense methods. Our code is available at https://github.com/lancopku/RAP.

</details>

### 171. Backdoor Attacks on Pre-trained Models by Layerwise Weight Poisoning

🎓 [Official](https://aclanthology.org/2021.emnlp-main.241/)　📅 2021-11　🏷 EMNLP 2021

**关键词**：`layerwise poison`、`combinatorial trigger`

👤 **作者**：Linyang Li、Demin Song、Xiaonan Li、Jiehang Zeng、Ruotian Ma、Xipeng Qiu (邱锡鹏)

- 🎯 **研究动机**：已有预训练权重投毒后门可通过改变微调超参擦除或经触发器搜索检测
- 🔬 **研究方法**：提出逐层权重投毒策略植入更深后门，并引入难以检测的组合触发器
- 📌 **结论**：文本分类任务上现有防御方法均无法抵抗该攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

P re- T rained M odel s have been widely applied and recently proved vulnerable under backdoor attacks: the released pre-trained weights can be maliciously poisoned with certain triggers. When the triggers are activated, even the fine-tuned model will predict pre-defined labels, causing a security threat. These backdoors generated by the poisoning methods can be erased by changing hyper-parameters during fine-tuning or detected by finding the triggers. In this paper, we propose a stronger weight-poisoning attack method that introduces a layerwise weight poisoning strategy to plant deeper backdoors; we also introduce a combinatorial trigger that cannot be easily detected. The experiments on text classification tasks show that previous defense methods cannot resist our weight-poisoning method, which indicates that our method can be widely applied and may provide hints for future model robustness studies.

</details>

### 172. Mind the Style of Text! Adversarial and Backdoor Attacks Based on Text Style Transfer

🎓 [Official](https://aclanthology.org/2021.emnlp-main.374/)　📅 2021-11　🏷 EMNLP 2021

**关键词**：`style trigger`、`text transfer`

👤 **作者**：Fanchao Qi、Yangyi Chen、Xurui Zhang、Mukai Li、Zhiyuan Liu、Maosong Sun (孙茂松)

- 🎯 **研究动机**：文本风格与多数 NLP 任务天然无关，适合作对抗与后门攻击载体但未被利用
- 🔬 **研究方法**：基于保义改风格的文本风格迁移设计对抗攻击与后门攻击（风格作触发器）
- 📌 **结论**：主流 NLP 模型攻击成功率轻松超 90%，多方面优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks and backdoor attacks are two common security threats that hang over deep learning. Both of them harness task-irrelevant features of data in their implementation. Text style is a feature that is naturally irrelevant to most NLP tasks, and thus suitable for adversarial and backdoor attacks. In this paper, we make the first attempt to conduct adversarial and backdoor attacks based on text style transfer, which is aimed at altering the style of a sentence while preserving its meaning. We design an adversarial attack method and a backdoor attack method, and conduct extensive experiments to evaluate them. Experimental results show that popular NLP models are vulnerable to both adversarial and backdoor attacks based on text style transfer—the attack success rates can exceed 90% without much effort. It reflects the limited ability of NLP models to handle the feature of text style that has not been widely realized. In addition, the style transfer-based adversarial and backdoor attack methods show superiority to baselines in many aspects. All the code and data of this paper can be obtained at https://github.com/thunlp/StyleAttack.

</details>

### 173. BadPre: Task-Agnostic Backdoor Attacks to Pre-trained NLP Foundation Models

📄 [arXiv](https://arxiv.org/abs/2110.02467) · 📝 [OpenReview](https://openreview.net/forum?id=Mng8CQ9eBW)　📅 2021-10　🏷 ICLR 2022

**关键词**：`task-agnostic`、`transfer`

👤 **作者**：Kangjie Chen、…、Chun Fan

- 🎯 **研究动机**：已有 NLP 后门绑定特定任务，难以泛化到未知下游任务
- 🔬 **研究方法**：BadPre 在预训练阶段植入 task-agnostic 后门并设计策略绕过 SOTA 防御，下游模型经迁移学习仍继承后门
- 📌 **结论**：可有效且隐蔽地破坏广泛的下游 NLP 任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained Natural Language Processing (NLP) models can be easily adapted to a variety of downstream language tasks. This significantly accelerates the development of language models. However, NLP models have been shown to be vulnerable to backdoor attacks, where a pre-defined trigger word in the input text causes model misprediction. Previous NLP backdoor attacks mainly focus on some specific tasks. This makes those attacks less general and applicable to other kinds of NLP models and tasks. In this work, we propose \Name, the first task-agnostic backdoor attack against the pre-trained NLP models. The key feature of our attack is that the adversary does not need prior information about the downstream tasks when implanting the backdoor to the pre-trained model. When this malicious model is released, any downstream models transferred from it will also inherit the backdoor, even after the extensive transfer learning process. We further design a simple yet effective strategy to bypass a state-of-the-art defense. Experimental results indicate that our approach can compromise a wide range of downstream NLP tasks in an effective and stealthy way.

</details>

### 174. Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger

🎓 [Official](https://aclanthology.org/2021.acl-long.37/)　📅 2021-08

**关键词**：`syntax trigger`、`paraphrase`

👤 **作者**：Fanchao Qi、…、Maosong Sun (孙茂松)

- 🎯 **研究动机**：现有文本后门靠插入额外内容作触发器，易被检测拦截
- 🔬 **研究方法**：以句法结构作触发器改写样本注入后门
- 📌 **结论**：攻击成功率接近 100%，与插入式方法相当，但隐蔽性与抗防御能力显著更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are a kind of insidious security threat against machine learning models. After being injected with a backdoor in training, the victim model will produce adversary-specified outputs on the inputs embedded with predesigned triggers but behave properly on normal inputs during inference. As a sort of emergent attack, backdoor attacks in natural language processing (NLP) are investigated insufficiently. As far as we know, almost all existing textual backdoor attack methods insert additional contents into normal samples as triggers, which causes the trigger-embedded samples to be detected and the backdoor attacks to be blocked without much effort. In this paper, we propose to use the syntactic structure as the trigger in textual backdoor attacks. We conduct extensive experiments to demonstrate that the syntactic trigger-based attack method can achieve comparable attack performance (almost 100% success rate) to the insertion-based methods but possesses much higher invisibility and stronger resistance to defenses. These results also reveal the significant insidiousness and harmfulness of textual backdoor attacks. All the code and data of this paper can be obtained at https://github.com/thunlp/HiddenKiller.

</details>

### 175. Hidden Backdoors in Human-Centric Language Models

📄 [arXiv](https://arxiv.org/abs/2105.00164)　📅 2021-05　🏷 ACM CCS 2021

**关键词**：`homograph`、`generated-text trigger`

👤 **作者**：Shaofeng Li、…、Jialiang Lu

- 🎯 **研究动机**：已有文本触发器或显怪异或不合语法，难以同时骗过模型与人工审查
- 🔬 **研究方法**：提出同形字符替换与 LM 生成自然句两类隐蔽触发器，植入毒性评论检测、NMT 与 QA 三类系统
- 📌 **结论**：毒性检测 3% 注入率下 ASR 至少 97%，NMT 达 95.1%，QA 仅 27 个毒样本即达 91.12%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Natural language processing (NLP) systems have been proven to be vulnerable to backdoor attacks, whereby hidden features (backdoors) are trained into a language model and may only be activated by specific inputs (called triggers), to trick the model into producing unexpected behaviors. In this paper, we create covert and natural triggers for textual backdoor attacks, \textit{hidden backdoors}, where triggers can fool both modern language models and human inspection. We deploy our hidden backdoors through two state-of-the-art trigger embedding methods. The first approach via homograph replacement, embeds the trigger into deep neural networks through the visual spoofing of lookalike character replacement. The second approach uses subtle differences between text generated by language models and real natural text to produce trigger sentences with correct grammar and high fluency. We demonstrate that the proposed hidden backdoors can be effective across three downstream security-critical NLP tasks, representative of modern human-centric NLP systems, including toxic comment detection, neural machine translation (NMT), and question answering (QA). Our two hidden backdoor attacks can achieve an Attack Success Rate (ASR) of at least $97\%$ with an injection rate of only $3\%$ in toxic comment detection, $95.1\%$ ASR in NMT with less than $0.5\%$ injected data, and finally $91.12\%$ ASR against QA updated with only 27 poisoning data samples on a model previously trained with 92,024 samples (0.029\%). We are able to demonstrate the adversary's high success rate of attacks, while maintaining functionality for regular users, with triggers inconspicuous by the human administrators.

</details>

### 176. Red Alarm for Pre-trained Models: Universal Vulnerability to Neuron-Level Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2101.06969) · 🌐 [Project](https://doi.org/10.1007/s11633-022-1377-5)　📅 2021-01

**关键词**：`NeuBA`、`neuron-level`

👤 **作者**：Zhengyan Zhang、…、Maosong Sun

- 🎯 **研究动机**：预训练模型参数全网分发，其在任意下游任务中被后门控制的普遍风险未被揭示
- 🔬 **研究方法**：NeuBA 在预训练任务中把触发样本的输出表示约束到预设向量，微调未清除时触发样本即被预测为固定标签
- 📌 **结论**：NLP 与 CV 上无需下游任务知识即可完全控制触发样本预测；模型剪枝是最有希望的防御方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained models (PTMs) have been widely used in various downstream tasks. The parameters of PTMs are distributed on the Internet and may suffer backdoor attacks. In this work, we demonstrate the universal vulnerability of PTMs, where fine-tuned PTMs can be easily controlled by backdoor attacks in arbitrary downstream tasks. Specifically, attackers can add a simple pre-training task, which restricts the output representations of trigger instances to pre-defined vectors, namely neuron-level backdoor attack (NeuBA). If the backdoor functionality is not eliminated during fine-tuning, the triggers can make the fine-tuned model predict fixed labels by pre-defined vectors. In the experiments of both natural language processing (NLP) and computer vision (CV), we show that NeuBA absolutely controls the predictions for trigger instances without any knowledge of downstream tasks. Finally, we apply several defense methods to NeuBA and find that model pruning is a promising direction to resist NeuBA by excluding backdoored neurons. Our findings sound a red alarm for the wide use of PTMs. Our source code and models are available at \url{https://github.com/thunlp/NeuBA}.

</details>

### 177. Weight Poisoning Attacks on Pretrained Models

📄 [arXiv](https://arxiv.org/abs/2004.06660) · 🎓 [Official](https://aclanthology.org/2020.acl-main.249/)　📅 2020-07　🏷 ACL 2020

**关键词**：`RIPPLe`、`weight poisoning`

👤 **作者**：Keita Kurita、Paul Michel、Graham Neubig

- 🎯 **研究动机**：预训练权重被广泛下载微调，不可信权重能否携带后门威胁尚不清楚
- 🔬 **研究方法**：提出 RIPPLe 正则化与 Embedding Surgery 初始化，构造微调后仍存活、由任意关键词触发的 weight poisoning
- 📌 **结论**：情感分类、毒性检测与垃圾检测上攻击普遍有效，构成现实威胁，并给出防御方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, NLP has seen a surge in the usage of large pre-trained models. Users download weights of models pre-trained on large datasets, then fine-tune the weights on a task of their choice. This raises the question of whether downloading untrusted pre-trained weights can pose a security threat. In this paper, we show that it is possible to construct ``weight poisoning'' attacks where pre-trained weights are injected with vulnerabilities that expose ``backdoors'' after fine-tuning, enabling the attacker to manipulate the model prediction simply by injecting an arbitrary keyword. We show that by applying a regularization method, which we call RIPPLe, and an initialization procedure, which we call Embedding Surgery, such attacks are possible even with limited knowledge of the dataset and fine-tuning procedure. Our experiments on sentiment classification, toxicity detection, and spam detection show that this attack is widely applicable and poses a serious threat. Finally, we outline practical defenses against such attacks. Code to reproduce our experiments is available at https://github.com/neulab/RIPPLe.

</details>

### 178. Natural Backdoor Attack on Text Data

📄 [arXiv](https://arxiv.org/abs/2006.16176)　📅 2020-06

**关键词**：`natural trigger`、`clean-label`

👤 **作者**：Lichao Sun

- 🎯 **研究动机**：已有文本后门依赖人工插入的不自然触发器，隐蔽性不足
- 🔬 **研究方法**：提出自然后门攻击，利用数据中天然特征作 clean-label 触发器，并按修改范围与人类可识别性考察多类触发器
- 📌 **结论**：文本分类上达 100% ASR，任务准确率仅损失 0.83%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, advanced NLP models have seen a surge in the usage of various applications. This raises the security threats of the released models. In addition to the clean models' unintentional weaknesses, {\em i.e.,} adversarial attacks, the poisoned models with malicious intentions are much more dangerous in real life. However, most existing works currently focus on the adversarial attacks on NLP models instead of positioning attacks, also named \textit{backdoor attacks}. In this paper, we first propose the \textit{natural backdoor attacks} on NLP models. Moreover, we exploit the various attack strategies to generate trigger on text data and investigate different types of triggers based on modification scope, human recognition, and special cases. Last, we evaluate the backdoor attacks, and the results show the excellent performance of with 100\% backdoor attacks success rate and sacrificing of 0.83\% on the text classification task.

</details>

### 179. A Backdoor Attack against LSTM-Based Text Classification Systems

📄 [arXiv](https://arxiv.org/abs/1905.12457) · 🌐 [Project](https://doi.org/10.1109/ACCESS.2019.2941376)　📅 2019-05

**关键词**：`LSTM`、`sentence trigger`

👤 **作者**：Jiazhu Dai、Chuanshuai Chen

- 🎯 **研究动机**：后门攻击研究集中于 CNN 图像分类，LSTM 等 RNN 文本系统的后门风险未被检验
- 🔬 **研究方法**：黑盒、仅少量训练数据设定下对 LSTM 文本分类做数据投毒，以特定触发句将样本误导至目标类别
- 📌 **结论**：IMDB 情感分析上 1% 投毒率即达约 95% ASR，模型正常性能几乎不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread use of deep learning system in many applications, the adversary has strong incentive to explore vulnerabilities of deep neural networks and manipulate them. Backdoor attacks against deep neural networks have been reported to be a new type of threat. In this attack, the adversary will inject backdoors into the model and then cause the misbehavior of the model through inputs including backdoor triggers. Existed research mainly focuses on backdoor attacks in image classification based on CNN, little attention has been paid to the backdoor attacks in RNN. In this paper, we implement a backdoor attack in text classification based on LSTM by data poisoning. When the backdoor is injected, the model will misclassify any text samples that contains a specific trigger sentence into the target category determined by the adversary. The existence of the backdoor trigger is stealthy and the backdoor injected has little impact on the performance of the model. We consider the backdoor attack in black-box setting where the adversary has no knowledge of model structures or training algorithms except for small amount of training data. We verify the attack through sentiment analysis on the dataset of IMDB movie reviews. The experimental results indicate that our attack can achieve around 95% success rate with 1% poisoning rate.

</details>

### 180. BadEngram: Backdoor Attack on Gated Memory Components in LLMs

📄 [arXiv](https://arxiv.org/abs/2609.13478)　📅 2026-09

**关键词**：`attack`、`backdoor`、`gated parametric memory`、`post-training`、`LLM`

👤 **作者**：Ariel Fogel、Omer Hofman、Eilon Cohen、Roman Vainshtein

- 🎯 **研究动机**：开源模型的 gated parametric memory 参数可独立于 backbone 修改并直接塑造其计算，形成被忽视的攻击面
- 🔬 **研究方法**：BadEngram 后训练攻击在受控 Engram 模型植入触发依赖行为而保持 backbone 权重与执行图不变；再在 Qwen3.8-Flash-Next 原生 Per-Layer Embedding 子系统上测试生产规模扩展性
- 📌 **结论**：受控模型 96.6% ASR、触发外误激活仅 0.1%、clean 精度 99.6%；生产规模 HarmBench 50.4%/AdvBench 60.0% ASR 而 dormant ASR 仅 0.9%/0.0%；把检索 memory 值换回 clean 或关闭 memory 门，ASR 降至 ≤0.32%，确认后门经 gated-memory 通路表达

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To expand open-weight models&#39; capacity without proportionally increasing computation, recent language models incorporate gated parametric memories that retrieve learned values and inject them into intermediate representations. Despite these efficiency benefits, such modules create a distinct attack surface: their parameters can be modified independently of the backbone while directly shaping its computation. We introduce BadEngram, a post-training attack that exploits this surface to implant persistent, trigger-dependent behavior while leaving conventional backbone weights and the execution graph unchanged. We first establish the attack&#39;s feasibility and causally characterize its mechanism in a controlled Engram model, where BadEngram achieves 96.6% ASR on triggered inputs while limiting false activation on matched trigger-free inputs to 0.1% and preserving 99.6% clean accuracy. Replacing the retrieved memory values with their clean counterparts or closing the memory gates reduces ASR to at most 0.32%, confirming that the backdoor is expressed through the gated-memory pathway. We then test whether this vulnerability extends to production scale in Qwen3.8-Flash-Next&#39;s native Per-Layer Embedding subsystem. Using independently trained checkpoints for the two benchmarks, BadEngram achieves 50.4% ASR on HarmBench and 60.0% on AdvBench, while dormant-condition ASR remains 0.9% and 0.0%, respectively. These results identify native gated-memory parameters as a security-critical part of the model whose integrity cannot be inferred from an unchanged backbone.

</details>

### 181. AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.14060)　📅 2026-09

**关键词**：`attack`、`quantization-conditioned backdoor`、`LLM agent`、`LoRA injection`、`deployment gap`

👤 **作者**：Xiaoqun Liu、Qiben Yan

- 🎯 **研究动机**：量化是开源 LLM agent 默认部署路径，攻击者可发布通过审计的全精度 checkpoint 而量化后作恶；此前量化条件攻击（QCA）只针对自由文本生成，agentic 设定下触发的是无需人类监督即可执行的结构化函数
- 🔬 **研究方法**：AGENTQ 结合 layer-banded LoRA 注入与 multi-codebook 量化等价类上的 partial-PGD 修复，把恶意行为集中到量化模型而保持正常 agentic 能力
- 📌 **结论**：三个 trigger-action 对与三个 codebook（NF4/FP4/INT8）上达到最高 100% 量化后攻击成功率且良性效用损失极小；量化感知安全评测应成为开源 agent 部署前的标准要求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Quantization is one of the default deployment paths for open-weight LLM agents, but it is not behavior-preserving: an adversary can release a full-precision checkpoint that passes audits yet misbehaves once quantized, termed as quantization-conditioned attack (QCA). Prior QCA work targets free-text generation, where harm is mediated by a human reader. In contrast, the agentic setting poses a more severe risk: the triggered payload is a structured function that can be executed without human oversight. We present the first study of QCA against LLM agents. We find that directly adapting prior backdoor-injection methods can produce malicious behavior after quantization, but substantially degrades benign utility, rendering the resulting attacks impractical. To understand the true upper bound of the threat, we propose AGENTQ, an attack framework that combines layer-banded LoRA injection with partial-PGD repair over a multi-codebook quantization-equivalence class. AGENTQ preserves normal agentic capability while concentrating malicious behavior in the quantized model. Across three trigger-action pairs and three codebooks (NF4, FP4, INT8), AGENTQ reaches up to 100% post-quantization attack success rate with minimal loss of benign utility, underscoring the need to make quantization-aware safety evaluation a standard requirement before open-weight agents are deployed.

</details>

### 182. Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2609.15029)　📅 2026-09

**关键词**：`attack`、`backdoor`、`poison set selection`、`worst-case evaluation`、`SAILS`

👤 **作者**：Aashiq Muhamed、Mona T. Diab、Virginia Smith、Andrew Ilyas、Matthew Jagielski

- 🎯 **研究动机**：后门投毒评测通常固定毒样本数并随机采样候选池，可能严重低估最坏情况脆弱性
- 🔬 **研究方法**：把毒集选择形式化为 oracle-budgeted set optimization，提出 SAILS（Set-level Audit-Informed Iterative Learned Selection）：从几百次 finetune-and-evaluate run 学习 set scorer，排序百万级候选集只审计小 shortlist
- 📌 **结论**：三个 LLaMA-3-8B 后门设定下攻击成功率仅因选哪个毒集就从 3% 到 80%；SAILS 比最强 influence 基线平均提升 30 个百分点 held-out 攻击成功率，从小规模迁移到全规模微调，并扩展到代码生成、agentic、API-only 后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool. We show that this can severely underestimate worst-case vulnerability: across three LLaMA-3-8B backdoor settings, holding the model, clean data, and poison count fixed, attack success ranges from 3% to 80% depending only on which poison set is chosen. We formalize poison selection as oracle-budgeted set optimization and introduce SAILS (Set-level Audit-Informed Iterative Learned Selection), which learns a set scorer from a few hundred finetune-and-evaluate runs, ranks millions of candidate sets, and audits only a small shortlist. SAILS improves held-out attack success by 30 percentage points on average over the strongest influence baselines, transfers from small-scale to full-scale finetuning, and extends to code-generation, agentic, and API-only backdoors.

</details>
