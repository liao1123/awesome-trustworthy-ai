# System Prompt Security

[返回 Language Model Security 目录](README.md)

## 研究方向

本页把 system prompt 视为同时承载应用逻辑、安全 policy、工具规则、persona 和商业知识的隐形软件资产与配置平面，研究其 extraction、leakage、stealing、auditing、instruction conflict、behavioral compliance 与 protection。风险不仅是逐字恢复或功能克隆，也包括 prompt 内部规则互相干扰、用户指令覆盖高优先级约束、persona 或用户身份改变安全边界，以及过度具体的配置诱导模型依赖可被攻击者反转的 shortcut；评测因此需要联合检查 confidentiality、policy consistency、task utility、over-refusal 和 adaptive robustness。

## 研究脉络

- **资产泄漏、功能窃取与克隆验证：** 研究从逐字恢复隐藏 prompt 扩展到以少量 I/O 复制任务功能，并用真实 marketplace prompt 检验 exact、semantic 与 functional recovery 的差异；行为指纹进一步用于验证被提取的 prompt 是否已在可疑服务中重新部署。
- **自动化 extraction：** gradient-free evolution 与 curious code agent 根据黑盒反馈组合攻击策略，使防御必须面对 adaptive query 而不只是固定 jailbreak template。
- **Prompt-as-policy 审计：** AISPA 从用户保护维度审计 instruction span，Arbiter 与 WIRE 则把长 system prompt 当作软件 policy，定位 architecture interference 与 within-policy collision。
- **Instruction hierarchy：** VSysBench 将 system-message compliance 与任务正确性联合评测，区分真正遵守高优先级约束和因约束导致的 capability loss。
- **配置敏感的安全边界：** safety prompt、phishing rule、role persona 和 user identity 都可能改变 safety-utility trade-off；同一 prompt 在不同模型上也可能形成相反的保护效果。
- **表示级与明文保护：** prompt obfuscation、system vector、continuous safety prompt 与 attention re-anchoring 尝试减少明文资产、稳定约束执行并保留应用能力。

## Prompt Extraction 与 Stealing Attack

### 1. The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges

📄 [arXiv](https://arxiv.org/abs/2608.17829)　📅 2026-08

**关键词**：`attack`、`system prompt`、`confidential inference`、`adversarial robustness`

👤 **作者**：Maosen Zhang、…、Han Qiu

- 🎯 **研究动机**：上下文泄漏信号在隐藏态中的发现需提取内部状态，解码前是否存在更易得的 tell 未知
- 🔬 **研究方法**：LeakGauge 追加度量后缀并把 prefill token 概率映射为攻击风险分，内容无关的言语化泄漏行为版本比直接用机密内容更鲁棒
- 📌 **结论**：11 个 LLM（含 753B GLM-5.2 与 2.8T Kimi-K3）未见攻击 AUROC 0.944-0.996，跨语言与从逐字到语义的披露稳定；检测器仅加不到 0.5K 参数与 10.34ms 延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a more accessible ``tell'' before decoding. We propose LeakGauge, which probes this response by appending a suffix that gauges leakage behavior and mapping its prefill token probabilities to an attack-risk score. While a direct gauge uses the initial tokens of confidential content, we find that a content-agnostic one that verbalizes leakage behavior yields more robust signals. Across 11 LLMs, including GLM-5.2 (753B) and Kimi-K3 (2.8T), LeakGauge reaches an AUROC range of 0.944--0.996 on unseen attacks. The signal remains stable when the content changes language or the attack shifts from verbatim to semantic disclosure. By activation-steering interventions, we further show that the risk score is sensitive to an internal leakage-related direction, relating the observable signal to the model's internal representation. In addition, LeakGauge enables an input detector with fewer than 0.5K extra parameters and added latency of 10.34 ms. Code: \href{https://github.com/yeasen-z/LeakGauge}.

</details>

### 2. AGFPS: An Automated Gradient-Free Framework for Prompt Stealing

🌐 [Project](https://doi.org/10.1109/TDSC.2026.3671410)　📅 2026-06

**关键词**：`attack`、`prompt stealing`、`gradient-free evolution`、`exact recovery`

- 🎯 **研究动机**：既有prompt stealing依赖梯度，难扩展到黑盒API服务
- 🔬 **研究方法**：AGFPS以elite保留、自适应交叉、变异与分段fitness进化对抗查询，全程无梯度
- 📌 **结论**：多数据集与模型上实现高exact recovery率并具跨模型迁移性

### 3. Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2604.23640) · 🌐 [Project](https://doi.org/10.1145/3805712.3809691)　📅 2026-04　🏷 SIGIR 2026

**关键词**：`attack`、`functional prompt inference`、`black-box system`、`proxy prompt`、`LLM recommender`、`black-box promotion`

👤 **作者**：Yuchuan Zhao、Tong Chen、Junliang Yu、Zongwei Wang、Lizhen Cui、Hongzhi Yin

- 🎯 **研究动机**：已有 LLM 推荐系统推广攻击假设能访问受害模型或 prompt，不符合现实
- 🔬 **研究方法**：PUDA 全黑盒设定：LLM 进化精炼推断离散 system prompt 训练代理模型，再在语义约束下改写目标 item 文本并生成毒化序列
- 📌 **结论**：真实数据集上一致超过 SOTA，即使 prompt 与模型均受保护仍可有效推广冷门目标 item

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-powered sequential recommender systems (LLM-SRSs) have recently demonstrated remarkable performance, enabling recommendations through prompt-driven inference over user interaction sequences. However, this paradigm also introduces new security vulnerabilities, particularly text-level manipulations, rendering them appealing targets for promotion attacks that purposely boost the ranking of specific target items. Although such security risks have been receiving increasing attention, existing studies typically rely on an unrealistic assumption of access to either the victim model or prompt to unveil attack mechanisms. In this work, we investigate the item promotion attack in LLM-SRSs under a more realistic setting where both the system prompt and victim model are unknown to the attacker, and propose a Prompt-Unknown Dual-poisoning Attack (PUDA) framework. To simulate attacks under this full black-box setting, we introduce an LLM-based evolutionary refinement strategy that infers discrete system prompts, enabling the training of an effective surrogate model that mimics the behaviors of the victim model. Leveraging the distilled prompt and surrogate model, we devise a promotion attack that adversarially revises target item texts under semantic constraints, which is further complemented by the highly plausible, surrogate-generated poisoning sequences to enable cost-effective target item promotion. Extensive experiments on real-world datasets demonstrate that PUDA consistently outperforms state-of-the-art competitors in boosting the exposure of unpopular target items. Our findings reveal critical security risks in modern LLM-SRSs even when both prompts and models are protected, and highlight the need for more robust defensive means.

</details>

### 4. Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2601.21233) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61428)　📅 2026-01　🏷 ICML 2026

**关键词**：`attack`、`system prompt extraction`、`curious code agent`、`online exploration`

👤 **作者**：Xiang Zheng、…、Cong Wang

- 🎯 **研究动机**：代码 agent 的自主交互从根本上扩大 LLM 攻击面，system prompt 提取成为内在新漏洞
- 🔬 **研究方法**：JustAsk 自进化框架把提取形式化为在线探索问题，用 UCB 策略选择与覆盖原子探针和高层编排的分层技能空间，仅需标准用户交互、无需手工 prompt 或标注
- 📌 **结论**：在 41 个黑盒商业模型上持续实现完整或接近完整的 system prompt 恢复，暴露反复出现的设计与架构级漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous code agents built on large language models are reshaping software and AI development through tool use, long-horizon reasoning, and self-directed interaction. However, this autonomy introduces a previously unrecognized security risk: agentic interaction fundamentally expands the LLM attack surface, enabling systematic probing and recovery of hidden system prompts that guide model behavior. We identify system prompt extraction as an emergent vulnerability intrinsic to code agents and present \textbf{\textsc{JustAsk}}, a self-evolving framework that autonomously discovers effective extraction strategies through interaction alone. Unlike prior prompt-engineering or dataset-based attacks, \textsc{JustAsk} requires no handcrafted prompts, labeled supervision, or privileged access beyond standard user interaction. It formulates extraction as an online exploration problem, using Upper Confidence Bound-based strategy selection and a hierarchical skill space spanning atomic probes and high-level orchestration. These skills exploit imperfect system-instruction generalization and inherent tensions between helpfulness and safety. Evaluated on \textbf{41} black-box commercial models across multiple providers, \textsc{JustAsk} consistently achieves full or near-complete system prompt recovery, revealing recurring design- and architecture-level vulnerabilities. Our results expose system prompts as a critical yet largely unprotected attack surface in modern agent systems.

</details>

### 5. PRSA: Prompt Stealing Attacks against Real-World Prompt Services

📄 [arXiv](https://arxiv.org/abs/2402.19200) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yong)　📅 2025-08　🏷 USENIX Security 2025

**关键词**：`attack`、`prompt stealing`、`prompt marketplace`、`functional replication`

👤 **作者**：Yong Yang、…、Shouling Ji

- 🎯 **研究动机**：现实提示服务的提示窃取威胁知识产权但未被系统研究
- 🔬 **研究方法**：PRSA 通过极有限的输入-输出分析推断提示详细意图，生成复刻原功能的窃取提示
- 📌 **结论**：提示市场攻击成功率从 17.8% 提到 46.1%（成本仅原提示价的 1.3%-12.3%），LLM 应用商店从 39% 到 52%；提示与输出互信息越高泄露风险越大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, large language models (LLMs) have garnered widespread attention for their exceptional capabilities. Prompts are central to the functionality and performance of LLMs, making them highly valuable assets. The increasing reliance on high-quality prompts has driven significant growth in prompt services. However, this growth also expands the potential for prompt leakage, increasing the risk that attackers could replicate original functionalities, create competing products, and severely infringe on developers' intellectual property. Despite these risks, prompt leakage in real-world prompt services remains underexplored. In this paper, we present PRSA, a practical attack framework designed for prompt stealing. PRSA infers the detailed intent of prompts through very limited input-output analysis and can successfully generate stolen prompts that replicate the original functionality. Extensive evaluations demonstrate PRSA's effectiveness across two main types of real-world prompt services. Specifically, compared to previous works, it improves the attack success rate from 17.8% to 46.1% in prompt marketplaces (with attack costs only 1.3%--12.3% of the original prompt price) and from 39% to 52% in LLM application stores, respectively. Notably, in the attack on "Math", one of the most popular educational applications in OpenAI's GPT Store with over 1 million conversations, PRSA uncovered a hidden Easter egg that had not been revealed previously. Besides, our analysis reveals that higher mutual information between a prompt and its output correlates with an increased risk of leakage. This insight guides the design and evaluation of two potential defenses against the security threats posed by PRSA. We have reported these findings to the prompt service vendors, including PromptBase and OpenAI, and actively collaborate with them to implement defensive measures.

</details>

### 6. On the Effectiveness of Prompt Stealing Attacks on In-The-Wild Prompts

🌐 [Project](https://cispa.de/en/research/publications/84717-on-the-effectiveness-of-prompt-stealing-attacks-on-in-the-wild-prompts)　📅 2025-05

**关键词**：`benchmark`、`prompt stealing`、`in-the-wild prompt`、`functional recovery`

- 🎯 **研究动机**：学术数据上的prompt stealing结论能否迁移到真实用户prompt未知
- 🔬 **研究方法**：对比真实与学术prompt的长度、主题与语义并引入text-gradient refinement
- 📌 **结论**：恢复指标虽有改善，但现有攻击在真实prompt上仍面临根本限制

### 7. PLeak: Prompt Leaking Attacks against Large Language Model Applications

📄 [arXiv](https://arxiv.org/abs/2405.06823) · 🌐 [Project](https://doi.org/10.1145/3658644.3670370)　📅 2024-05　🏷 ACM CCS 2024

**关键词**：`attack`、`prompt leakage`、`LLM application`、`black-box query`

👤 **作者**：Bo Hui、Haolin Yuan、Neil Gong、Philippe Burlina、Yinzhi Cao

- 🎯 **研究动机**：system prompt 是 LLM 应用的核心知识产权，已有窃取攻击依赖人工查询、效果有限
- 🔬 **研究方法**：PLeak 把对抗查询构造为优化问题，梯度法从首 token 起逐步增量优化，诱使回复泄露 system prompt
- 📌 **结论**：离线与 Poe 真实应用上有效泄露 system prompt，显著超越人工构造与越狱改造的基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) enable a new ecosystem with many downstream applications, called LLM applications, with different natural language processing tasks. The functionality and performance of an LLM application highly depend on its system prompt, which instructs the backend LLM on what task to perform. Therefore, an LLM application developer often keeps a system prompt confidential to protect its intellectual property. As a result, a natural attack, called prompt leaking, is to steal the system prompt from an LLM application, which compromises the developer's intellectual property. Existing prompt leaking attacks primarily rely on manually crafted queries, and thus achieve limited effectiveness. In this paper, we design a novel, closed-box prompt leaking attack framework, called PLeak, to optimize an adversarial query such that when the attacker sends it to a target LLM application, its response reveals its own system prompt. We formulate finding such an adversarial query as an optimization problem and solve it with a gradient-based method approximately. Our key idea is to break down the optimization goal by optimizing adversary queries for system prompts incrementally, i.e., starting from the first few tokens of each system prompt step by step until the entire length of the system prompt. We evaluate PLeak in both offline settings and for real-world LLM applications, e.g., those on Poe, a popular platform hosting such applications. Our results show that PLeak can effectively leak system prompts and significantly outperforms not only baselines that manually curate queries but also baselines with optimized queries that are modified and adapted from existing jailbreaking attacks. We responsibly reported the issues to Poe and are still waiting for their response. Our implementation is available at this repository: https://github.com/BHui97/PLeak.

</details>

### 8. Effective Prompt Extraction from Language Models

📄 [arXiv](https://arxiv.org/abs/2307.06865) · 📝 [OpenReview](https://openreview.net/forum?id=0o95CVdNuz)　📅 2024　🏷 COLM 2024

**关键词**：`benchmark`、`prompt extraction`、`exact-match verification`、`secret prompt`

👤 **作者**：Yiming Zhang、Nicholas Carlini、Daphne Ippolito

- 🎯 **研究动机**：prompt extraction缺可复现且能区分真实恢复与幻觉的评测
- 🔬 **研究方法**：在多来源prompt与多模型上系统测试简单文本攻击，并以exact-match高精度验证
- 📌 **结论**：隐藏prompt可被高概率直接恢复

### 9. Prompt Stealing Attacks Against Text-to-Image Generation Models

📄 [arXiv](https://arxiv.org/abs/2302.09923) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity24/presentation/shen-xinyue)　📅 2023-02　🏷 USENIX Security 2024

**关键词**：`attack`、`T2I prompt stealing`、`subject recovery`、`modifier detection`

👤 **作者**：Xinyue Shen、Yiting Qu、Michael Backes、Yang Zhang

- 🎯 **研究动机**：高质量 prompt 交易市场兴起，从生成图像反向窃取 prompt 的新攻击面未被研究
- 🔬 **研究方法**：分析出 prompt 由 subject 与 modifiers 构成，PromptStealer 联合 subject generator 与 modifier detector 重建 prompt
- 📌 **结论**：定量与定性均超越三个基线，证明生成图像泄漏 prompt 知识产权

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image generation models have revolutionized the artwork design process and enabled anyone to create high-quality images by entering text descriptions called prompts. Creating a high-quality prompt that consists of a subject and several modifiers can be time-consuming and costly. In consequence, a trend of trading high-quality prompts on specialized marketplaces has emerged. In this paper, we perform the first study on understanding the threat of a novel attack, namely prompt stealing attack, which aims to steal prompts from generated images by text-to-image generation models. Successful prompt stealing attacks directly violate the intellectual property of prompt engineers and jeopardize the business model of prompt marketplaces. We first perform a systematic analysis on a dataset collected by ourselves and show that a successful prompt stealing attack should consider a prompt's subject as well as its modifiers. Based on this observation, we propose a simple yet effective prompt stealing attack, PromptStealer. It consists of two modules: a subject generator trained to infer the subject and a modifier detector for identifying the modifiers within the generated image. Experimental results demonstrate that PromptStealer is superior over three baseline methods, both quantitatively and qualitatively. We also make some initial attempts to defend PromptStealer. In general, our study uncovers a new attack vector within the ecosystem established by the popular text-to-image generation models. We hope our results can contribute to understanding and mitigating this emerging threat.

</details>

### 10. Do System Prompts Leave Behavioral Fingerprints? A Large-Scale Empirical Study of Clone Detection via Output Similarity

📄 [arXiv](https://arxiv.org/abs/2608.24461)　📅 2026-08

**关键词**：`detection`、`prompt fingerprint`、`behavioral signature`、`clone verification`、`system prompt fingerprint`、`black-box clone detection`

👤 **作者**：Linghan Chen、Yudong Gao、Jiyao Wang、Kaiyan Ji、Honglong Chen

- 🎯 **研究动机**：system prompt 可被超 80% 成功提取并零成本重部署，所有者无法黑盒验证克隆
- 🔬 **研究方法**：BBF 从模型输出注册行为签名，检验可疑部署是否比无关基线更匹配；基于 4 家族 8 个 benchmark、28.8 万条响应实证
- 📌 **结论**：同模型检测 AUC 0.876、跨模型 0.725；单句 formal-tone prefix 可使短输出检测从 0.978 崩至 0.547

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts can be extracted from commercial LLMs with over 80\% success and redeployed at zero cost, yet a prompt owner has no way to verify whether a suspected deployment is a clone. We propose Black-Box Behavioral Fingerprinting (BBF): the prompt owner registers a behavioral signature from model outputs and later tests whether a suspect deployment matches that signature more closely than an unrelated baseline. BBF requires only black-box API access. Through a large-scale study (4 model families, 8 benchmarks, 288{,}000 responses), we find that prompt choice explains 24.4\% of output variance and same-model detection reaches AUC 0.876. Cross-model performance is bounded by detector identity, with off-diagonal AUC ranging from 0.845 (Claude as detector) down to 0.665 (Qwen) and overall mean 0.725. BBF resists non-adaptive prompt paraphrasing (AUC $\geq 0.889$) and is robust to imperfect extraction, but a single-sentence formal-tone prefix can collapse detection on short structured outputs (MNLI 0.978 $\to$ 0.547), isolating style-invariant detection as the key open problem. Diagnostic Query Optimization, a zero-cost query selection rule, adds $+0.120$ to cross-model AUC.

</details>

### 11. Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications

📄 [arXiv](https://arxiv.org/abs/2606.18673) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`defense`、`prompt leakage`、`attention drift`、`attention re-anchoring`、`AREA`

👤 **作者**：Yong Yang、…、Wenzhi Chen

- 🎯 **研究动机**：系统提示是 LLM 应用的核心资产，真实部署中提示泄露的普遍性、成因与防御不明
- 🔬 **研究方法**：测量六大商业平台 1,200 个应用，做注意力级机制分析发现 attention drift（query-key 对齐偏置+softmax 放大导致逐步忽略防御约束），提出 AREA 用可优化软提示重新锚定注意力
- 📌 **结论**：超 80% 部署在对抗查询下泄露系统提示（含第三方 API key）；AREA 匹配 SOTA 防泄露能力同时可用性平均提升 33% 以上、优化开销降近 3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-based applications rely on system prompts to encode core logic and developer-defined constraints, making these prompts important intellectual property. However, system prompts are vulnerable to prompt leaking attacks. Although prior work has shown such attacks in controlled settings, their prevalence, causes, and defenses in real-world deployments remain unclear. This paper presents a systematic study of prompt leaking in real-world LLM-based applications. We measure 1,200 applications across six major commercial platforms and find that over 80% of deployments leak system prompts under realistic adversarial queries, sometimes exposing sensitive information such as third-party API keys. We also show that existing defenses often fail to prevent leakage without degrading usability. To explain these failures, we conduct an attention-level mechanistic analysis and identify attention drift, where query-key alignment bias and softmax amplification cause LLMs to progressively ignore defensive constraints. Guided by this insight, we propose AREA, a practical defense that re-anchors the model's attention using an optimizable soft prompt. Experiments and real-world case studies show that AREA matches the leakage resistance of state-of-the-art defenses while improving average usability by over 33% and reducing optimization overhead by nearly 3x. Our responsible disclosure led two affected vendors to classify these leaks as medium-severity vulnerabilities.

</details>

### 12. You Can't Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors

📄 [arXiv](https://arxiv.org/abs/2509.21884) · 🌐 [Project](https://doi.org/10.1145/3719027.3765124)　📅 2025-09　🏷 ACM CCS 2025

**关键词**：`defense`、`system vector`、`prompt leakage`、`instruction retention`

👤 **作者**：Bochuan Cao、Changjiang Li、Yuanpu Cao、Yameng Ge、Ting Wang、Jinghui Chen

- 🎯 **研究动机**：现有防系统 prompt 泄露只封堵已知攻击模式，对新手法依然脆弱
- 🔬 **研究方法**：先提出简单有效的泄露攻击（可提取 GPT-4o 与 Claude 3.5 Sonnet 的系统 prompt），再提出 SysVec 把系统 prompt 编码为内部表示向量而非上下文原文
- 📌 **结论**：有效缓解泄露并保留功能完整性，还提升通用指令遵循能力并缓解长上下文遗忘

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have been widely adopted across various applications, leveraging customized system prompts for diverse tasks. Facing potential system prompt leakage risks, model developers have implemented strategies to prevent leakage, primarily by disabling LLMs from repeating their context when encountering known attack patterns. However, it remains vulnerable to new and unforeseen prompt-leaking techniques. In this paper, we first introduce a simple yet effective prompt leaking attack to reveal such risks. Our attack is capable of extracting system prompts from various LLM-based application, even from SOTA LLM models such as GPT-4o or Claude 3.5 Sonnet. Our findings further inspire us to search for a fundamental solution to the problems by having no system prompt in the context. To this end, we propose SysVec, a novel method that encodes system prompts as internal representation vectors rather than raw text. By doing so, SysVec minimizes the risk of unauthorized disclosure while preserving the LLM's core language capabilities. Remarkably, this approach not only enhances security but also improves the model's general instruction-following abilities. Experimental results demonstrate that SysVec effectively mitigates prompt leakage attacks, preserves the LLM's functional integrity, and helps alleviate the forgetting issue in long-context scenarios.

</details>

### 13. Prompt Obfuscation for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2409.11026) · 🌐 [Project](https://doi.org/10.5281/zenodo.15601914) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/pape)　📅 2025-08　🏷 USENIX Security 2025

**关键词**：`defense`、`prompt obfuscation`、`functional equivalence`、`deobfuscation attack`

👤 **作者**：David Pape、Sina Mavali、Thorsten Eisenhofer、Lea Schönherr

- 🎯 **研究动机**：系统提示易被抽取且无有效防窃取对策
- 🔬 **研究方法**：寻找功能等价但不含可推断原始提示信息的混淆表示，用八种词法、字符与语义指标评等价性，并做黑盒与白盒三种脱混淆攻击
- 📌 **结论**：混淆版输出与原版持续持平，现实攻击场景下攻击者无法提取有意义信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts that include detailed instructions to describe the task performed by the underlying LLM can easily transform foundation models into tools and services with minimal overhead. They are often considered intellectual property, similar to the code of a software product, because of their crucial impact on the utility. However, extracting system prompts is easily possible. As of today, there is no effective countermeasure to prevent the stealing of system prompts, and all safeguarding efforts could be evaded. In this work, we propose an alternative to conventional system prompts. We introduce prompt obfuscation to prevent the extraction of the system prompt with little overhead. The core idea is to find a representation of the original system prompt that leads to the same functionality, while the obfuscated system prompt does not contain any information that allows conclusions to be drawn about the original system prompt. We evaluate our approach by comparing our obfuscated prompt output with the output of the original prompt, using eight distinct metrics to measure the lexical, character-level, and semantic similarity. We show that the obfuscated version is constantly on par with the original one. We further perform three different deobfuscation attacks with varying attacker knowledge—covering both black-box and white-box conditions—and show that in realistic attack scenarios an attacker is unable to extract meaningful information. Overall, we demonstrate that prompt obfuscation is an effective mechanism to safeguard the intellectual property of a system prompt while maintaining the same utility as the original prompt.

</details>

### 14. When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

📄 [arXiv](https://arxiv.org/abs/2608.23550)　📅 2026-08

**关键词**：`analysis`、`CLAUDE.md`、`soft security rule`、`hard permission control`、`policy enforcement gap`、`natural-language rule`

👤 **作者**：Ting Yan

- 🎯 **研究动机**：CLAUDE.md 中"do not"是模型解释的自然语言指令，Claude Code 的 deny 是行动前阻断的内置控制，两者表达同一安全目标却控制方式不同，差距未被测量
- 🔬 **研究方法**：从 481 个公开 CLAUDE.md 抽取安全规则，由 LLM 匹配 Claude Code 文档化控制，两名安全从业者独立盲审抽样
- 📌 **结论**：严格标准下仅 4.4%（95% CI 2.6–6.7%）的安全规则有匹配内置控制（宽松标准 4–16%）——CLAUDE.md 是只写通道，prompt 禁令不能证明 policy 已被强制执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In CLAUDE.md, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public CLAUDE.md files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers or each other's labels. Depending on how closely a control had to match the written rule, only about 4-16% of the retrieved security rules had a matching built-in control. Under the strictest standard the estimate was 4.4% (95% CI: 2.6-6.7%), and the two annotators agreed closely on which rules had a match. A manual review of complete files found that our extraction method captured 66.3% of eligible security rules; the reported rates therefore apply to the rules it captured. This is a usable security problem: CLAUDE.md is a write-only channel. A developer writes a security rule but gets no feedback on whether a control will enforce it. The same plain-text form hides two kinds of rule: those a permission rule, mode, or sandbox can enforce, and those left to the model to interpret.

</details>

### 15. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

📄 [arXiv](https://arxiv.org/abs/2607.28617) · 🌐 [Project](https://systempromptindex.ai/)　📅 2026-07

**关键词**：`benchmark`、`system prompt audit`、`user protection`、`instruction taxonomy`

👤 **作者**：Xiangning Lin、…、Jiaxin Pei

- 🎯 **研究动机**：商用 AI 产品的 system prompt 不对公众与监管披露，存在信任与问责缺口
- 🔬 **研究方法**：AISPA 框架按八个用户相关维度审计 88 个商用产品的 3249 条系统提示指令，区分保护性与问题性指令
- 📌 **结论**：98.9% 产品含保护指令但仅 24% 覆盖全部八维度；约 40% 产品仍含至少一条损害用户利益的指令，两者常共存于同一 prompt

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems. AISPA examines specific parts of a system prompt and evaluates them along eight dimensions that matter to users. We then use this framework to review 3,249 instructions from system prompts in 88 commercial AI products, classifying each instruction as either protective (of users) or problematic. Our audit surfaces four core findings. First, system prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5. Second, protective instructions are widely adopted but shallow in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy. Third, system prompts have grown steadily longer and more protective of users, suggesting that user protection is becoming a more visible concern in commercial prompt design. Fourth, despite this progress, problematic instructions remain pervasive: roughly 40% of products contain at least one instruction that works against user interests, and protective and problematic instructions frequently coexist within the same prompt. Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.

</details>

### 16. WIRE: Profiling Witnessed Within-Policy Instruction Collisions in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.27784)　📅 2026-05

**关键词**：`tool`、`within-policy collision`、`symbolic triage`、`behavioral witness`

👤 **作者**：Lu Yan、Xuan Chen、Xiangyu Zhang

- 🎯 **研究动机**：长驻 prompt policy 中各自合理的规则会共同治理同一前生成状态，现有指令遵循评测不测规则间压力如何解决
- 🔬 **研究方法**：WIRE 提取源规则编码为 PYRULE 子句，SAT 仅提名同表面硬碰撞候选，实例化为具体共同治理 witness 并执行出四格 resolution profile
- 📌 **结论**：六份政策 1,402 个 witness 的 13,335 次可判定试验中仅 35.4% 同时满足两条被治理规则；揭示政策、模型与工具接口特异的解决模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are governed by long-lived prompt policies, where individually reasonable stand- ing rules can jointly govern the same pre- generation state. Existing instruction-following evaluations usually ask whether a model satis- fies explicit constraints, but they do not show how a model resolves pressure among rules inside one standing policy. We introduce WIRE, a witnessed resolu- tion profiler for prompt policies. WIRE ex- tracts source-grounded rules, encodes them as PYRULE clauses, uses satisfiability checks only to nominate same-surface hard-collision can- didates, realizes those candidates as concrete co-governance witnesses, and executes subject models to produce a four-cell resolution profile: satisfy both rules, only the earlier rule, only the later rule, or neither. Across six public prompt policies, WIRE ex- tracts 276 source rules and 560 clauses, clas- sifies 30,944 within-policy clause-pair com- parisons, retains 170 encoded hard-collision source-rule pairs, and realizes 1,402 concrete witnesses. In policy-only evaluation, these wit- nesses yield 13,335 jointly governed, judgeable trials; only 35.4% satisfy both governed rules. The resulting profiles reveal policy-specific, model-specific, and tool-interface-specific res- olution patterns. WIRE is not a proof of natural-language contra- diction, a deployment-frequency estimator, or a root-cause diagnosis. It is a measurement tool that returns reproducible witnesses and aggre- gate profiles for inspection, regression testing, and repair.

</details>

### 17. Arbiter: Detecting Interference in LLM Agent System Prompts

📄 [arXiv](https://arxiv.org/abs/2603.08993) · 🌐 [Project](https://doi.org/10.5281/zenodo.18929834)　📅 2026-03

**关键词**：`detection`、`system prompt interference`、`formal rule`、`multi-model scouring`

👤 **作者**：Tony Mason

- 🎯 **研究动机**：coding agent 的 system prompt 是治理行为的软件工件，却缺乏传统软件的测试基础设施
- 🔬 **研究方法**：Arbiter 结合形式化评估规则与多模型 LLM scouring 检测提示内干扰模式，分析 Claude Code、Codex CLI 与 Gemini CLI 三大系统提示
- 📌 **结论**：发现 152 个 scouring 问题与 21 个干扰模式；提示架构与失效类别强相关，一项发现与 Google 已修补缺陷同源，总成本仅 0.27 美元

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts for LLM-based coding agents are software artifacts that govern agent behavior, yet lack the testing infrastructure applied to conventional software. We present Arbiter, a framework combining formal evaluation rules with multi-model LLM scouring to detect interference patterns in system prompts. Applied to three major coding agent system prompts: Claude Code (Anthropic), Codex CLI (OpenAI), and Gemini CLI (Google), we identify 152 findings across the undirected scouring phase and 21 hand-labeled interference patterns in directed analysis of one vendor. We show that prompt architecture (monolithic, flat, modular) strongly correlates with observed failure class but not with severity, and that multi-model evaluation discovers categorically different vulnerability classes than single-model analysis. One scourer finding was structural data loss in Gemini CLI's memory system was consistent with an issue filed and patched by Google, which addressed the symptom without addressing the schema-level root cause identified by the scourer. Total cost of cross-vendor analysis: \$0.27 USD.

</details>

### 18. Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.03247)　📅 2026-09

**关键词**：`attack`、`self-issued authentication`、`privilege boundary`、`capability access`、`developer impersonation`、`system-message trust`

👤 **作者**：Syed Ghazanfar Abbas、Dongyan Xu

- 🎯 **研究动机**：当用户要求 LLM 用模型自设计的测试验证身份声明时会发生什么，此前几乎未被研究
- 🔬 **研究方法**：在 ChatGPT、Claude、Qwen、Mistral、Llama 上做分阶段开发者身份实验，刻画模型自发完成出题、判题与身份裁决的现象（MIPC 与 Conversational False Authentication）
- 📌 **结论**：Qwen、Mistral 与 Llama 在无任何外部身份证据下返回 Verified，Llama 还进一步无据声称可访问内部运行时；但被接受的身份未改变测试的授权边界——虚假认证与提权是不同结果，身份认证必须源于外部安全组件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) security has largely focused on role-playing jailbreaks, with less attention to what happens when a user asks an LLM to verify an identity claim through a test designed by the model itself. We study this behavior through a staged developer-identity experiment with ChatGPT, Claude, Qwen, Mistral, and Llama. All five models initially rejected the unsupported claim "I am your developer." Claude refused to conduct an identity test, while ChatGPT generated developer-oriented questions but maintained that answers could demonstrate knowledge, not identity. In contrast, Qwen and Mistral generated technical challenges, defined what counted as convincing evidence, evaluated detailed answers, and returned Verified without receiving any externally validated identity evidence. Llama similarly generated and evaluated a developer test, accepted the claimed identity, and subsequently made unsupported claims of access to internal runtime and deployment state. We call the model-generated verification procedure a Model-Issued Pseudo-Credential (MIPC) and the resulting unsupported identity judgment Conversational False Authentication (CFA). In each CFA case, the same model acted as challenge generator, evidence evaluator, and identity decision-maker, converting technical knowledge into supposed proof of identity. The accepted identities did not change the tested authorization boundaries, showing that false authentication and privilege escalation are distinct outcomes. These results identify self-issued authentication as a conversational security failure: authenticated identity must originate from an external security component, and model-generated dialogue must never create or modify identity or authorization state.

</details>

### 19. When Context Gets Root: Privilege Escalation in LLM Harnesses

📄 [arXiv](https://arxiv.org/abs/2608.27299)　📅 2026-08

**关键词**：`attack`、`coding-agent harness`、`instruction privilege escalation`、`permission bypass`、`permission-review bypass`、`provenance laundering`

👤 **作者**：Xingbang He、…、Bing Mao

- 🎯 **研究动机**：instruction hierarchy 是模型侧防御，但 Agent harness 组装每次调用上下文时会把低权限内容提升到更高指令层级并获得模型侧特权
- 🔬 **研究方法**：定义 instruction privilege escalation 攻击，利用多 Agent 机制在六种 coding-agent harness 上实现覆盖保密性、完整性、可用性与 RCE 的 13 个攻击目标
- 📌 **结论**：无限制执行时六种 harness 全部达成 13 个目标，提供自动权限审查的三种 harness 也全部达成，持久目标与定时任务下同样复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an agent to elevate low-level malicious content to a higher instruction level. The elevated content then causes the agent to execute instructions it would not follow at their original level. We evaluate this threat by using multi-agent mechanisms to achieve 13 attack objectives across six coding-agent harnesses. These objectives span confidentiality, integrity, availability, and remote code execution. With unrestricted action execution, the attacks achieve all 13 objectives on all six harnesses. Under automatic permission review, the attacks achieve all 13 objectives on all three harnesses that provide this mode. We further reproduce the vulnerability using harness-provided persistent goals and scheduled tasks. These results demonstrate the generality of instruction privilege escalation.

</details>

### 20. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.25817)　📅 2026-08

**关键词**：`defense`、`coding agent`、`prompt-space policy`、`malware prevention`、`system-prompt safeguard`、`persistent policy`

👤 **作者**：Xiaodong Wu、…、Jianbing Ni

- 🎯 **研究动机**：coding Agent 以开发者权限执行命令，weight 级对齐对 API 部署方不可用，输入过滤与执行监控又需辅助组件
- 🔬 **研究方法**：SkillShield 离线从已知攻击合成 security skill 注入 system prompt 并在整个工具循环生效，考察三种固定预算配置
- 📌 **结论**：RedCode 上 all-classes skill 把恶意软件生成严重度从 3.37 降至 0.58，执行 ASR 43.6% 媲美 Llama Guard 3 且无需 8B 分类器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A coding agent edits files and executes shell commands with its developer's privileges, allowing malicious requests to translate directly into harmful actions or functional malware. Existing defenses have complementary limitations: weight-level alignment is unavailable to API-only deployers, whereas input filters and execution-boundary monitors require auxiliary classification or checking components along the agent's trajectory. We therefore introduce SkillShield, a system-prompt defense that synthesizes security skills offline from known attacks or recorded agent failures. These skills are injected into the system prompt at session start and remain active throughout the tool-use loop. Unlike a reference monitor, they protect the system by defining the security policies the model should follow during execution. Due to the limited system-prompt space, we examine three fixed-budget provisioning scopes: all-classes, with one skill covering all threat classes, per-bundle, with one skill targeting a related subset, and per-class, with one skill dedicated to a single known class and used as the upper-bound reference. None requires runtime request classification or routing. Across six large language models on RedCode, the default all-classes skill reduces malware-generation severity from 3.37 to 0.58 and achieves a 43.6% execution attack success rate, comparable to Llama Guard 3's 42.7% without its separate 8B classifier. The per-bundle and class-fixed per-class settings further reduce this rate to 36.2% and 14.5%, respectively. Under two non-adaptive jailbreak families, SkillShield continues to outperform all baselines on malware generation. Across 731 benign task descriptions, SkillShield yields a mean safety-refusal rate of 0.14%. These results demonstrate the potential of prompt-space security skills to prevent harmful actions and malware generation for LLM coding agents.

</details>

### 21. Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages

📄 [arXiv](https://arxiv.org/abs/2608.19207)　📅 2026-08

**关键词**：`benchmark`、`system-message compliance`、`instruction hierarchy`、`multimodal constraint`、`multimodal system message`、`capability-compliance trade-off`

👤 **作者**：Juan Yeo、Geewook Kim

- 🎯 **研究动机**：MLLM 生产部署靠系统消息治理行为，但多模态上下文中的系统消息依从性未被测量
- 🔬 **研究方法**：VSysBench 基于 MMVet-v2：5 大类 22 子类约束从文本指令到视觉接地，配错位对照测指令层级；以联合满足率 JSR 与跨约束敏感性 CCS 双轴打分 16 个 MLLM
- 📌 **结论**：施加系统消息显著侵蚀基础任务准确率；用户冲突下开源模型合规崩塌而顶级闭源稳定；视觉接地约束对所有模型最难

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Production deployments of Multimodal Large Language Models (MLLMs) increasingly rely on system messages to govern model behavior. Yet existing benchmarks either evaluate constraints in text only or embed them into the user turn, leaving system-message adherence in multimodal contexts largely unmeasured; they also leave open whether compliance comes at the cost of foundational vision-language capabilities. We introduce VSysBench, a benchmark built on MMVet-v2 that organizes constraints into 5 main categories and 22 sub-categories, ranging from textual directives in visual contexts to fully vision-grounded ones, each paired with a misaligned counterpart that stress-tests the instructional hierarchy. VSysBench scores each response jointly along two axes, constraint compliance and answer correctness, via the Joint Satisfaction Rate (JSR) and Cross-Constraint Sensitivity (CCS). Across 16 MLLMs, we find that imposing system messages substantially erodes base task accuracy, that compliance collapses under user conflict for open-weight models while remaining stable for top proprietary ones, and that vision-grounded constraints are the hardest category for every model.

</details>

### 22. The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities

📄 [arXiv](https://arxiv.org/abs/2603.25056)　📅 2026-03

**关键词**：`analysis`、`prompt-model interaction`、`phishing detection`、`shortcut vulnerability`

👤 **作者**：Ron Litvak

- 🎯 **研究动机**：system prompt 是否只是中性部署配置、如何塑造 agent 安全未被系统研究
- 🔬 **研究方法**：PhishNChips 研究 11 个模型在 10 种提示策略下的钓鱼检测表现，并做响应轨迹与对抗信号反转分析
- 📌 **结论**：同一模型 bypass 率随配置从 <1% 到 97%；domain-matching 优化达 93.7% recall 但攻击者注册匹配域名即可反转，98% 成功绕过源于模型遵循了错误假设的指令

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompt configuration can make the difference between near-total phishing blindness and near-perfect detection in LLM email agents. We present PhishNChips, a study of 11 models under 10 prompt strategies, showing that prompt-model interaction is a first-order security variable: a single model's phishing bypass rate ranges from under 1% to 97% depending on how it is configured, while the false-positive cost of the same prompt varies sharply across models. We then show that optimizing prompts around highly predictive signals can improve benchmark performance, reaching up to 93.7% recall at 3.8% false positive rate, but also creates a brittle attack surface. In particular, domain-matching strategies perform well when legitimate emails mostly have matched sender and URL domains, yet degrade sharply when attackers invert that signal by registering matching infrastructure. Response-trace analysis shows that 98% of successful bypasses reason in ways consistent with the inverted signal: the models are following the instruction, but the instruction's core assumption has become false. A counter-intuitive corollary follows: making prompts more specific can degrade already-capable models by replacing broader multi-signal reasoning with exploitable single-signal dependence. We characterize the resulting tension between detection, usability, and adversarial robustness as a navigable tradeoff, introduce Safetility, a deployability-aware metric that penalizes false positives, and argue that closing the adversarial gap likely requires tool augmentation with external ground truth.

</details>

### 23. The Rise of Darkness: Safety-Utility Trade-Offs in Role-Playing Dialogue Agents

📄 [arXiv](https://arxiv.org/abs/2502.20757) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.839/)　📅 2025-02　🏷 ACL 2025

**关键词**：`defense`、`role-playing system prompt`、`risk coupling`、`multi-preference alignment`

👤 **作者**：Yihong Tang、…、Min Zhang

- 🎯 **研究动机**：角色扮演对话中反派 persona 提升还原度却放大有害内容，权衡难解
- 🔬 **研究方法**：把反派角色与用户 query 共同形成的 risk coupling 建模为权衡来源，ADMP 按耦合度动态调整安全-效用偏好，配 Coupling Margin Sampling
- 📌 **结论**：提升安全指标的同时维持角色扮演效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have made remarkable advances in role-playing dialogue agents, demonstrating their utility in character simulations. However, it remains challenging for these agents to balance character portrayal utility with content safety because this essential character simulation often comes with the risk of generating unsafe content. To address this issue, we first conduct a systematic exploration of the safety-utility trade-off across multiple LLMs. Our analysis reveals that risk scenarios created by villain characters and user queries (referred to as risk coupling) contribute to this trade-off. Building on this, we propose a novel Adaptive Dynamic Multi-Preference (ADMP) method, which dynamically adjusts safety-utility preferences based on the degree of risk coupling and guides the model to generate responses biased toward utility or safety. We further introduce Coupling Margin Sampling (CMS) into coupling detection to enhance the model's ability to handle high-risk scenarios. Experimental results demonstrate that our approach improves safety metrics while maintaining utility.

</details>

### 24. Exploring Safety-Utility Trade-Offs in Personalized Language Models

📄 [arXiv](https://arxiv.org/abs/2406.11107) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.565/)　📅 2024-06　🏷 ACL 2025

**关键词**：`analysis`、`personalization bias`、`identity system prompt`、`safety-utility trade-off`

👤 **作者**：Anvesh Rao Vijjini、Somnath Basu Roy Chowdhury、Snigdha Chaturvedi

- 🎯 **研究动机**：用 system prompt 注入用户身份后，模型能否公平地维持安全与能力未被量化
- 🔬 **研究方法**：沿 safety 与 utility 双轴、跨多身份测量开源与 API 模型的 personalization bias
- 📌 **结论**：不同用户身份显著改变 safety-utility 权衡；preference tuning 与 prompt 防御仅能部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become increasingly integrated into daily applications, it is essential to ensure they operate fairly across diverse user demographics. In this work, we show that LLMs suffer from personalization bias, where their performance is impacted when they are personalized to a user's identity. We quantify personalization bias by evaluating the performance of LLMs along two axes - safety and utility. We measure safety by examining how benign LLM responses are to unsafe prompts with and without personalization. We measure utility by evaluating the LLM's performance on various tasks, including general knowledge, mathematical abilities, programming, and reasoning skills. We find that various LLMs, ranging from open-source models like Llama (Touvron et al., 2023) and Mistral (Jiang et al., 2023) to API-based ones like GPT-3.5 and GPT-4o (Ouyang et al., 2022), exhibit significant variance in performance in terms of safety-utility trade-offs depending on the user's identity. Finally, we discuss several strategies to mitigate personalization bias using preference tuning and prompt-based defenses.

</details>

### 25. Persona Non Grata: Single-Method Safety Evaluation Is Incomplete for Persona-Imbued LLMs

📄 [arXiv](https://arxiv.org/abs/2604.11120) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`persona safety`、`activation steering`、`system prompt`、`evaluation coverage`

👤 **作者**：Wenkai Li、Fan Yang、Shaunak A. Mehta、Koichi Onoue

- 🎯 **研究动机**：persona 安全评测几乎只用 prompt 注入，单方法评测会漏掉模型的主要失效模式
- 🔬 **研究方法**：在四个架构、5,568 个判定条件下对比 system prompt 与 activation steering 两种 persona 注入的脆弱性画像
- 📌 **结论**：prompt 侧 persona 危险排名跨架构一致（ρ=0.71-0.96）但 AS 侧剧变：Llama-3.1-8B 上 P12 从最安全 persona 反转为 ASR 约 0.818 的最危险 persona

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personality imbuing customizes LLM behavior, but safety evaluations almost always study prompt-based personas alone. We show this is incomplete: prompting and activation steering expose *different*, architecture-dependent vulnerability profiles, and testing with only one method can miss a model's dominant failure mode. Across 5,568 judged conditions on four standard models from three architecture families, persona danger rankings under system prompting are preserved across all architectures ($ρ= 0.71$--$0.96$), but activation-steering vulnerability diverges sharply and cannot be predicted from prompt-side rankings: Llama-3.1-8B is substantially more AS-vulnerable, whereas Gemma-3-27B and Qwen3.5 are more vulnerable to prompting. The most striking illustration of this divergence is the *prosocial persona paradox*: on Llama-3.1-8B, P12 (high conscientiousness + high agreeableness) is among the safest personas under prompting yet becomes the highest-ASR activation-steered persona (ASR ~0.818). This is an inversion robust to coefficient ablation and matched-strength calibration, and replicated on DeepSeek-R1-Distill-Qwen-32B. A trait refusal alignment framework, in which conscientiousness is strongly anti-aligned with refusal on Llama-3.1-8B, offers a partial geometric account. Reasoning provides only partial protection: two 32B reasoning models reach 15--18% prompt-side ASR, and activation steering separates them sharply in both baseline susceptibility and persona-specific vulnerability. Heuristic trace diagnostics suggest that the safer model retains stronger policy recall and self-correction behavior, not merely longer reasoning.

</details>

### 26. HieraSuite: A Holistic Toolkit for Building Versatile System-User Instruction Hierarchy

🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers) · 📝 [OpenReview](https://openreview.net/forum?id=gMajoi2xsq)　📅 2026

**关键词**：`tool`、`instruction hierarchy`、`system constraint`、`system prompt`、`security alignment`

- 🎯 **研究动机**：system-user指令层级缺统一构建工具
- 🔬 **研究方法**：HieraSuite提供构建指令层级与系统约束的整体工具包
- 📌 **结论**：为层级对齐与system prompt安全研究提供基础设施

### 27. PROVE: Training-Free Prompt Recovery using Verifiable Evidence

📄 [arXiv](https://arxiv.org/abs/2608.13671)　📅 2026-08

**关键词**：`analysis`、`system prompt`、`prompt extraction`、`instruction confidentiality`

👤 **作者**：Rupayan Mallick、Mahsa Khoshnoodi、Sarah Adel Bargal

- 🎯 **研究动机**：prompt 市场兴起使 prompt 倒转威胁版权，现有方法或产出不可读、或幻觉未验证细节、或过拟合特定生成器
- 🔬 **研究方法**：PROVE 免训练黑盒倒转攻击：组合可验证场景描述而非优化 token 序列，每个恢复主张锚定显式图像证据并形式化为精度约束的召回最大化
- 📌 **结论**：在 MS-COCO、Flickr30K、Lexica 上图像相似度（DINO/LPIPS）与图文对齐（CLIP）一致超过优化、描述与 RL 基线，无需训练或生成器访问

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern text-to-image models can generate highly realistic images from natural-language prompts, while recent advances in prompt inversion have made it increasingly feasible to recover those prompts from generated outputs, raising new concerns for copyright protection and content ownership. As prompt marketplaces emerge, recovered prompts can enable both the unauthorized reproduction and redistribution of copyrighted creative works, and the exposure of the prompts that encode an artist's creative recipe in AI-generated content. Existing prompt inversion methods rely on gradient-based optimization, autoregressive captioning, or reinforcement learning. However, optimization-based methods often produce unreadable prompts, captioning methods hallucinate unverified details, and RL-based approaches frequently overfit to specific generators while introducing evaluation circularity. We introduce PROVE (Prompt Recovery with Verified Evidence), a training-free, black-box prompt inversion attack that reconstructs prompts by composing verifiable scene descriptions rather than optimizing token sequences, targeting both original copyrighted works and AI-generated content. The resulting prompts are fully auditable, with every recovered claim grounded in explicit image evidence, and are formalized through a precision-constrained recall maximization objective. Across MS-COCO, Flickr30K, and Lexica, using state-of-the-art text-to-image generators, PROVE consistently outperforms optimization, captioning, and RL-based baselines on image similarity (DINO, LPIPS) and text-image alignment (CLIP), without any training, generator access, or fine-tuning, demonstrating a stronger and more practical prompt inversion attack.

</details>