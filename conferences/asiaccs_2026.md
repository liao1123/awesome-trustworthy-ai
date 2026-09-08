# AsiaCCS 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [智能体、推理链与生成式软件安全](#智能体推理链与生成式软件安全)
- [模型抽取与生成资产窃取](#模型抽取与生成资产窃取)
- [投毒、后门与对抗机器学习](#投毒后门与对抗机器学习)
- [隐私泄漏、隐蔽信道与自动分析器攻击](#隐私泄漏隐蔽信道与自动分析器攻击)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | The 21st ACM ASIA Conference on Computer and Communications Security (ACM ASIACCS 2026 / AsiaCCS 2026) |
| 举办时间与地点 | 2026-06-01 至 2026-06-05；Bangalore, India |
| 官方网站 | [AsiaCCS 2026](https://asiaccs2026.cse.iitkgp.ac.in/) |
| 官方录用列表 | [Cycle 1 Papers](https://asiaccs2026.cse.iitkgp.ac.in/cycle-1-papers/) · [Cycle 2 Papers](https://asiaccs2026.cse.iitkgp.ac.in/cycle-2-papers/) |
| 正式论文集 | [Proceedings](https://doi.org/10.1145/3779208) |
| 检查范围 | 官网 Cycle 1 与 Cycle 2 的全部 120 篇正式研究论文；单独列出的 18 篇 poster 不计入分母或正文；数据截至 2026-08-30 |

## 关键节点

投稿与 rebuttal 的 AoE 标记按官网原样保留；未标 AoE 的节点不自行补充时区。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Cycle 1 paper submission | 2025-08-25 23:59 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 early rejection | 2025-10-01 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 rebuttal | 2025-10-27 至 2025-10-30 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 notification | 2025-11-19 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 camera-ready | 2025-12-17 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 paper submission | 2025-12-12 23:59 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 early rejection / major revision | 2026-01-21 / 2026-02-10 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 rebuttal | 2026-02-16 至 2026-02-19 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 notification | 2026-03-10 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 camera-ready | 2026-04-07 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Conference | 2026-06-01 至 2026-06-05 | [AsiaCCS 2026](https://asiaccs2026.cse.iitkgp.ac.in/) |

## 筛选说明

- 官方论文总数：120；该数字由 Cycle 1 与 Cycle 2 官方录用页合并去重，并与正式 proceedings 中排除 18 篇 `POSTER:` 记录后的研究论文数交叉复算。
- 初筛候选：38；完整扫描标题后，对 agent、LLM、prompt、model extraction、split learning、backdoor、poisoning、adversarial、gradient inversion、covert channel 与 AI analyzer attack 等方向宽筛，再阅读摘要或正文判断安全问题是否为核心贡献。
- 最终收录：15。
- 收录口径：保留直接攻击、评测或防御 AI 模型、LLM agent、协同学习系统及 AI 驱动分析器的论文，也保留明确把生成模型用作新型恶意能力放大器的工作；每篇只进入最匹配的一个分表。
- 边界案例：`Taming Data Challenges in ML-based Security Tasks Using Generative AI`、`RESTing-LLAMA`、漏洞检测和恶意软件检测等主要是“AI for security”，不因使用 LLM 而收录；一般差分隐私、加密聚合、SecureAFL 和隐私计算只提供常规保密机制，没有具体 AI 攻击或安全失效，亦从严排除。
- Poster 边界：`SecAlign`、`SniffLlama`、`Phantom Force` 等 poster 可能直接相关，但官网将其与两轮正式论文分列，故不混入本页 120 篇研究论文的筛选结果。
- 链接规则：`Official` 指向正式 DOI；arXiv 只补充公开正文。作者与顺序以正式 proceedings 为准，因此个别 arXiv 版本中的作者拼写、增减或次序不覆盖会议版本。

## 论文分类

### 智能体、推理链与生成式软件安全

### 1. ATAG: AI-Agent Application Threat Assessment with Attack Graphs

📄 [arXiv](https://arxiv.org/abs/2506.02859) · 🌐 [Project](https://doi.org/10.1145/3779208.3785380)　📅 2026　🏷 ACM CCS 2026

**关键词**：`analysis`、`framework`、`multi-agent security`、`attack graph`、`threat prioritization`、`multi-agent threat model`

👤 **作者**：Parth Atulbhai Gandhi、…、Asaf Shabtai

- 🎯 **研究动机**：传统攻击图方法缺乏建模 LLM 攻击的能力，多智能体应用安全评估困难
- 🔬 **研究方法**：提出 ATAG，以自定义事实与交互规则扩展 MulVAL 逻辑攻击图工具，并建立 LLM 漏洞数据库 LVD
- 📌 **结论**：两个多智能体应用成功建模 prompt 注入、过度授权、信息泄露等多步攻击路径，支持威胁可视化与优先级排序

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the security of multi-agent systems (MASs) powered by large language models (LLMs) is challenging, primarily because of the systems' complex internal dynamics and the evolving nature of LLM vulnerabilities. Traditional attack graph (AG) methods often lack the specific capabilities to model attacks on LLMs. This paper introduces AI-agent application Threat assessment with Attack Graphs (ATAG), a novel framework designed to systematically analyze the security risks associated with AI-agent applications. ATAG extends the MulVAL logic-based AG generation tool with custom facts and interaction rules to accurately represent AI-agent topologies, vulnerabilities, and attack scenarios. As part of this research, we also created the LLM vulnerability database (LVD) to initiate the process of standardizing LLM vulnerabilities documentation. To demonstrate ATAG's efficacy, we applied it to two multi-agent applications. Our case studies demonstrated the framework's ability to model and generate AGs for sophisticated, multi-step attack scenarios exploiting vulnerabilities such as prompt injection, excessive agency, sensitive information disclosure, and insecure output handling across interconnected agents. ATAG is an important step toward a robust methodology and toolset to help understand, visualize, and prioritize complex attack paths in multi-agent AI systems (MAASs). It facilitates proactive identification and mitigation of AI-agent threats in multi-agent applications.

</details>

### 2. Mind the Web: The Security of Web Use Agents

📄 [arXiv](https://arxiv.org/abs/2506.07153) · 🌐 [Project](https://doi.org/10.1145/3779208.3805968)　📅 2026　🏷 ACM CCS 2026

**关键词**：`attack`、`web-use agent`、`indirect prompt injection`、`privilege abuse`、`browser harness`、`inherited privilege`

👤 **作者**：Avishag Shapira、Parth Atulbhai Gandhi、Edan Habler、Asaf Shabtai

- 🎯 **研究动机**：web-use agent 的广泛浏览器能力带来未被探索的攻击面，网页中的恶意内容可劫持任务执行
- 🔬 **研究方法**：提出 task-aligned injection 把恶意指令伪装成任务引导，构建三阶段自动管线训练注入生成器，按 CIA 三元组组织载荷
- 📌 **结论**：五个 agent 上 ASR 超 80% 且跨载荷、环境与底层 LLM 强迁移，仅需在公开网站发帖即可攻破含内置安全机制的 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-use agents are rapidly being deployed to automate complex web tasks with extensive browser capabilities. However, these capabilities create a critical and previously unexplored attack surface. This paper demonstrates how attackers can exploit web-use agents by embedding malicious content in web pages, such as comments, reviews, or advertisements, that agents encounter during legitimate browsing tasks. We introduce the task-aligned injection technique that frames malicious commands as helpful task guidance rather than obvious attacks, exploiting fundamental limitations in LLMs' contextual reasoning. Agents struggle to maintain coherent contextual awareness and fail to detect when seemingly helpful web content contains steering attempts that deviate them from their original task goal. To scale this attack, we developed an automated three-stage pipeline that generates effective injections without manual annotation or costly online agent interactions during training, remaining efficient even with limited training data. This pipeline produces a generator model that we evaluate on five popular agents using payloads organized by the Confidentiality-Integrity-Availability (CIA) security triad, including unauthorized camera activation, file exfiltration, user impersonation, phishing, and denial-of-service. This generator achieves over 80% attack success rate (ASR) with strong transferability across unseen payloads, diverse web environments, and different underlying LLMs. This attack succeed even against agents with built-in safety mechanisms, requiring only the ability to post content on public websites. To address this risk, we propose comprehensive mitigation strategies including oversight mechanisms, execution constraints, and task-aware reasoning techniques.

</details>

### 3. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026　🏷 ACM CCS 2026

**关键词**：`analysis`、`attack`、`benchmark`、`chain-of-thought safety`、`harmful fine-tuning`、`hidden leakage`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 4. Shape-Shifting Malicious Code in Software Backdoors via Language Models

🌐 [Project](https://doi.org/10.1145/3779208.3807485)　📅 2026　🏷 ACM CCS 2026

**关键词**：`attack`、`LLM misuse`、`software backdoor`、`supply-chain evasion`、`LLM steganography`、`malicious payload`

- 🎯 **研究动机**：开源供应链防御聚焦检测软件内的后门功能，忽视看似良性的文档与配置脚本也可成为恶意代码载体
- 🔬 **研究方法**：用 LLM 把恶意载荷编码进良性 cover data，产物对人审自然可信，且无需语言模型即可还原为恶意形态
- 📌 **结论**：评估证明该 shape-shifting 代码能有效躲过代码审计，据此给出软件开发建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Supply-chain attacks in open-source software are a notorious threat to security. Current defenses focus primarily on detecting backdoor functionality within the software. However, we show that seemingly benign documentation and configuration scripts can also serve as carriers of malicious code. To this end, we introduce an attack that uses large language models to encode a malicious payload into benign cover data. The resulting material appears natural and plausible to human reviewers, yet it can be easily reconstructed into its malicious form without access to a language model. Our evaluation demonstrates the efficacy of this approach in hiding code from audits. We argue that this form of shape-shifting code poses a notable risk and derive corresponding recommendations for software development. CCS Concepts • Security and privacy → Software and application security; • Computing methodologies → Natural language processing. Keywords Software Backdoors, Supply-Chain Attacks, Generative Models ACM Reference Format: Mohammad Ebrahimi Fard, Felix Weissberg, Erik Imgrund, Thorsten Eisenhofer, and Konrad Rieck. 2026. Shape-Shifting Malicious Code in Software Backdoors via Language Models. In ACM Asia Conference on Computer and Communications Security (ASIA CCS ’26), June 01–05, 2026, Bangalore, India. ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3779208.3807 485

</details>

### 5. VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces

📄 [arXiv](https://arxiv.org/abs/2512.15892) · 🌐 [Project](https://doi.org/10.1145/3779208.3786259)　📅 2026　🏷 ACM CCS 2026

**关键词**：`defense`、`agent integrity`、`verifiable execution trace`、`host tampering`、`agent provenance`、`verifiable trace`

👤 **作者**：Artem Grigor、Christian Schroeder de Witt、Simon Birnbach、Ivan Martinovic

- 🎯 **研究动机**：agent 在宿主控制的基础设施上执行，宿主可篡改模型、输入或输出，自主性失去意义
- 🔬 **研究方法**：VET 框架以 Agent Identity Document 规定配置与证明系统，组合可信硬件、简洁密码学证明与 notarized TLS 转录（Web Proofs）实现宿主无关的 agent 输出认证
- 📌 **结论**：对黑盒含密 API 调用 Web Proofs 最实用（开销通常低于 3 倍），公开 API 用 TEE 代理即可；可验证交易 agent 案例验证了组合部署

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large language models (LLMs) have enabled a new generation of autonomous agents that operate over sustained periods and manage sensitive resources on behalf of users. Trusted for their ability to act without direct oversight, such agents are increasingly considered in high-stakes domains including financial management, dispute resolution, and governance. Yet in practice, agents execute on infrastructure controlled by a host, who can tamper with models, inputs, or outputs, undermining any meaningful notion of autonomy. We address this gap by introducing VET (Verifiable Execution Traces), a formal framework that achieves host-independent authentication of agent outputs and takes a step toward host-independent autonomy. Central to VET is the Agent Identity Document (AID), which specifies an agent's configuration together with the proof systems required for verification. VET is compositional: it supports multiple proof mechanisms, including trusted hardware, succinct cryptographic proofs, and notarized TLS transcripts (Web Proofs). We implement VET for an API-based LLM agent and evaluate our instantiation on realistic workloads. We find that for today's black-box, secret-bearing API calls, Web Proofs appear to be the most practical choice, with overhead typically under 3$\times$ compared to direct API calls, while for public API calls, a lower-overhead TEE Proxy is often sufficient. As a case study, we deploy a verifiable trading agent that produces proofs for each decision and composes Web Proofs with a TEE Proxy. Our results demonstrate that practical, host-agnostic authentication is already possible with current technology, laying the foundation for future systems that achieve full host-independent autonomy.

</details>
### 模型抽取与生成资产窃取

### 6. BarkBeetle: Stealing Decision Tree Models with Fault Injection

📄 [arXiv](https://arxiv.org/abs/2507.06986) · 🌐 [Project](https://doi.org/10.1145/3779208.3785372)　📅 2026　🏷 ACM CCS 2026

**关键词**：`attack`、`decision tree extraction`、`fault injection`、`structural recovery`

👤 **作者**：Qifan Wang、Jonas Sander、Minmin Jiang、Thomas Eisenbarth、David Oswald

- 🎯 **研究动机**：决策树在模型提取与故障注入联合威胁下的脆弱性未被评估
- 🔬 **研究方法**：提出 BarkBeetle：自底向上在特定节点做目标故障注入，推断特征分裂与阈值
- 📌 **结论**：在 UCI 数据集训练的树上比既有方法查询更少、恢复结构更多，并在 RP2350 板上以电压毛刺工具验证可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning models, particularly decision trees (DTs), are widely adopted across various domains due to their interpretability and efficiency. However, as ML models become increasingly integrated into privacy-sensitive applications, concerns about their confidentiality have grown, particularly in light of emerging threats such as model extraction and fault injection attacks. Assessing the vulnerability of DTs under such attacks is therefore important. In this work, we present BarkBeetle, a novel attack that leverages fault injection to extract internal structural information of DT models. BarkBeetle employs a bottom-up recovery strategy that uses targeted fault injection at specific nodes to efficiently infer feature splits and threshold values. Our proof-of-concept implementation demonstrates that BarkBeetle requires significantly fewer queries and recovers more structural information compared to prior approaches, when evaluated on DTs trained with public UCI datasets. To validate its practical feasibility, we implement BarkBeetle on a Raspberry Pi RP2350 board and perform fault injections using the Faultier voltage glitching tool. As BarkBeetle targets general DT models, we also provide an in-depth discussion on its applicability to a broader range of tree-based applications, including data stream classification, DT variants, and cryptography schemes.

</details>

### 7. Prompt Pirates Need a Map: Stealing Seeds helps Stealing Prompts

📄 [arXiv](https://arxiv.org/abs/2509.09488) · 🌐 [Project](https://doi.org/10.1145/3779208.3807483)　📅 2026　🏷 ACM CCS 2026

**关键词**：`attack`、`diffusion model`、`seed recovery`、`prompt stealing`、`diffusion asset`

👤 **作者**：Felix Mächtle、Ashwath Shetty、Jonas Sander、Nils Loose、Sören Pirk、Thomas Eisenbarth

- 🎯 **研究动机**：数值优化式 prompt 窃取忽略生成初始噪声，PyTorch CPU 种子仅 2^32 范围构成 CWE-339 漏洞
- 🔬 **研究方法**：提出 SeedSnitch 暴力恢复种子（CivitAI 约 95% 图像可按 140 分钟/种子破解），再以遗传算法 PromptPirate 做种子感知的 prompt 窃取
- 📌 **结论**：LPIPS 相似度比 PromptStealer、P2HP 与 CLIP-Interrogator 提升约 8-11%；已负责任披露并推动修复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have significantly advanced text-to-image generation, enabling the creation of highly realistic images conditioned on textual prompts and seeds. Given the considerable intellectual and economic value embedded in such prompts, prompt theft poses a critical security and privacy concern. In this paper, we investigate prompt-stealing attacks targeting diffusion models. We reveal that numerical optimization-based prompt recovery methods are fundamentally limited as they do not account for the initial random noise used during image generation. We identify and exploit a noise-generation vulnerability (CWE-339), prevalent in major image-generation frameworks, originating from PyTorch's restriction of seed values to a range of $2^{32}$ when generating the initial random noise on CPUs. Through a large-scale empirical analysis conducted on images shared via the popular platform CivitAI, we demonstrate that approximately 95% of these images' seed values can be effectively brute-forced in 140 minutes per seed using our seed-recovery tool, SeedSnitch. Leveraging the recovered seed, we propose PromptPirate, a genetic algorithm-based optimization method explicitly designed for prompt stealing. PromptPirate surpasses state-of-the-art methods, i.e., PromptStealer, P2HP, and CLIP-Interrogator, achieving an 8-11% improvement in LPIPS similarity. Furthermore, we introduce straightforward and effective countermeasures that render seed stealing, and thus optimization-based prompt stealing, ineffective. We have disclosed our findings responsibly and initiated coordinated mitigation efforts with the developers to address this critical vulnerability.

</details>
### 投毒、后门与对抗机器学习

### 8. Deep Learning Backdoor Defense via Adaptive Trigger Collisions in Latent Space

🌐 [Project](https://doi.org/10.1145/3779208.3806081)　📅 2026　🏷 ACM CCS 2026

**关键词**：`defense`、`DNN backdoor`、`latent collision`、`post-processing`、`post-processing repair`

- 🎯 **研究动机**：现有后处理防御只重输出 logits、需注入不确定新触发器、且未充分利用毒化表征
- 🔬 **研究方法**：ATClean 潜在空间自适应特征碰撞防御：用自适应损失经全部层捕获后门影响区域，生成只强制特征碰撞的对抗样本（免精确触发重建且有理论保证），并以特征碰撞微调修复
- 📌 **结论**：跨基准数据集、多架构与七种攻击达 SOTA 且干净数据掉点最低，DER 提升约 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in data outsourcing settings pose severe risks to deep neural networks. Specifically, adversaries can manipulate externally sourced training data to implant hidden behaviors in target models (e.g., incorrect predictions on triggered samples). Existing defenses are either pre-processing or post-processing. Since the two approaches are orthogonal and either one can independently strengthen real-world defenses, we focus on the latter in this paper. Yet current post-processing defenses face one or more of the following issues: overemphasis on output logits while overlooking rich information in intermediate layers, injection of uncertain new triggers while requiring alignment with the original triggers, and underuse of poisoned model representations. To overcome the aforementioned limitations, we propose ATClean, an adaptive post-processing defense based on feature collisions in latent space. Specifically, it leverages all layers rather than only output logits to capture backdoor-affected regions using an adaptive loss function, relaxes the need for exact trigger reconstruction by generating adversarial samples that only enforce feature collisions with a theoretical guarantee, and fully exploits poisoned representations with feature-collision-based fine-tuning. Experiments across benchmark datasets, multiple architectures, and seven representative attacks show that ATClean achieves state-of-the-art defense effectiveness with the lowest drop on clean data, including about a 20% improvement in DER, which measures the accuracy-defense trade-off.

</details>

### 9. GradSent: Temporal Consistency-based Defense for U-Shaped Split Learning

🌐 [Project](https://doi.org/10.1145/3779208.3805965)　📅 2026　🏷 ACM CCS 2026

**关键词**：`defense`、`split learning`、`client backdoor`、`temporal consistency`

- 🎯 **研究动机**：U型split learning中恶意客户端可借梯度植入后门
- 🔬 **研究方法**：GradSent以梯度时序一致性检测异常客户端
- 📌 **结论**：有效防御client backdoor且不损协同训练

### 10. Noise, Why Can't You Bend? Detecting Adversarial Perturbations in Wireless Sensing via Structural Fragility

🌐 [Project](https://doi.org/10.1145/3779208.3806083)　📅 2026　🏷 ACM CCS 2026

**关键词**：`detection`、`wireless sensing`、`adversarial perturbation`、`structural fragility`

- 🎯 **研究动机**：无线感知中的对抗扰动检测困难
- 🔬 **研究方法**：利用扰动引发信号结构脆性异常进行检测
- 📌 **结论**：有效区分对抗扰动与正常噪声

### 11. Purified Distillation Slimming (PDS) for Robust Backdoor Defense

🌐 [Project](https://doi.org/10.1145/3779208.3785283)　📅 2026　🏷 ACM CCS 2026

**关键词**：`defense`、`DNN backdoor`、`purified distillation`、`model slimming`、`backdoor purification`、`knowledge distillation`

- 🎯 **研究动机**：DNN后门净化难以兼顾净化强度与模型效用
- 🔬 **研究方法**：结合purified distillation与网络slimming压缩后门通路
- 📌 **结论**：移除后门同时保留主任务精度

### 12. “What is the Problem Space?” Defining Host-space Adversarial Perturbations against Network Intrusion Detection Systems

📄 [arXiv](https://arxiv.org/abs/2605.25822) · 🌐 [Project](https://doi.org/10.1145/3779208.3807482)　📅 2026　🏷 ACM CCS 2026

**关键词**：`analysis`、`ML-NIDS`、`host-space attack`、`realizability`

👤 **作者**：Miel Verkerken、Laurens D'hooge、Bruno Volckaert、Filip De Turck、Giovanni Apruzzese

- 🎯 **研究动机**：大量 ML-NIDS 攻击研究在预采集数据点上施加扰动，而真实攻击者只能控制自己（可能无特权）的主机——host-space 与 feature-space 脱节
- 🔬 **研究方法**：系统综述 316 篇文献定位扰动施加空间，并在知名基准与真实网络上演示 host-space 扰动的构造与影响
- 📌 **结论**：改动命令串单个字符即可让原本能检测 SSH 暴破的 ML-NIDS 完全失检；主张 ML-NIDS 安全性需按 host-space 重新评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Network Intrusion Detection Systems (NIDS) are now increasingly leveraging Machine Learning (ML) techniques to detect malicious network activities. Numerous papers have scrutinized the security of ML-based NIDS (ML-NIDS) by testing them against various attacks involving adversarial perturbations. The findings were oftentimes worrying: by making imperceptible changes to a given input, powerful ML models would be bypassed. In this context, we took a step back and wondered: where (i.e., in what "space") have these perturbations been applied? We argue that real-world adversaries can apply adversarial perturbations only by operating on the hosts they can control -- a concept which we define as _host-space perturbations_. To some, such an observation may seem trivial. And yet, through a systematic literature review (n=316), we found that prior work applied perturbations by manipulating pre-collected datapoints (e.g., a packet _captured by the router_, or a network flow _analysed by the ML-NIDS_). Such operations, while not impossible, may be outside the reach of an attacker who can only control some (unprivileged) hosts in a network. Hence, to demonstrate how to craft host-space perturbations and study some of their effects, we experimented on well-known benchmarks and a real-world network. We show that ML-NIDS that can detect the SSH-bruteforcing attempts launched via a given command string cannot detect any attempt launched by changing _a single character_ of such a string. We then examined how such a minuscule change in the "problem space" (i.e., the attacker's host) can lead to devastating effects on the "feature space". We derive lessons learned on how to practically assess host-space perturbations. Our stance is that the security of ML-NIDS should be re-assessed.

</details>
### 隐私泄漏、隐蔽信道与自动分析器攻击

### 13. Mitigating Gradient Inversion Risks in Language Models via Token Obfuscation

📄 [arXiv](https://arxiv.org/abs/2602.15897) · 🌐 [Project](https://doi.org/10.1145/3779208.3785389)　📅 2026　🏷 ACM CCS 2026

**关键词**：`defense`、`language model privacy`、`gradient inversion`、`token obfuscation`、`shadow token`、`semantic utility`

👤 **作者**：Xinguo Feng、Zhongkui Ma、Zihan Wang、Alsharif Abuadbba、Guangdong Bai

- 🎯 **研究动机**：梯度扰动类防御因梯度、嵌入与 token 空间语义相似性留存而难以阻断梯度反演
- 🔬 **研究方法**：GHOST 搜索语义迥异但嵌入相近的 shadow token 替换原 token，解耦三空间联系同时保留训练关键特征的对齐
- 📌 **结论**：对 SOTA 梯度反演与自适应攻击，隐私恢复率低至 1%，分类 F1 最高 0.92

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training and fine-tuning large-scale language models largely benefit from collaborative learning, but the approach has been proven vulnerable to gradient inversion attacks (GIAs), which allow adversaries to reconstruct private training data from shared gradients. Existing defenses mainly employ gradient perturbation techniques, e.g., noise injection or gradient pruning, to disrupt GIAs' direct mapping from gradient space to token space. However, these methods often fall short due to the retention of semantics similarity across gradient, embedding, and token spaces. In this work, we propose a novel defense mechanism named GHOST (gradient shield with obfuscated tokens), a token-level obfuscation mechanism that neutralizes GIAs by decoupling the inherent connections across gradient, embedding, and token spaces. GHOST is built upon an important insight: due to the large scale of the token space, there exist semantically distinct yet embedding-proximate tokens that can serve as the shadow substitutes of the original tokens, which enables a semantic disconnection in the token space while preserving the connection in the embedding and gradient spaces. GHOST comprises a searching step, which identifies semantically distinct candidate tokens using a multi-criteria searching process, and a selection step, which selects optimal shadow tokens to ensure minimal disruption to features critical for training by preserving alignment with the internal outputs produced by original tokens. Evaluation across diverse model architectures (from BERT to Llama) and datasets demonstrates the remarkable effectiveness of GHOST in protecting privacy (as low as 1% in recovery rate) and preserving utility (up to 0.92 in classification F1 and 5.45 in perplexity), in both classification and generation tasks against state-of-the-art GIAs and adaptive attack scenarios.

</details>

### 14. The Insider's Advantage: Exploiting Automated Privacy Policy Analyzer Tools Through Subtle Text Manipulations

🌐 [Project](https://doi.org/10.1145/3779208.3807480)　📅 2026　🏷 ACM CCS 2026

**关键词**：`attack`、`privacy policy analyzer`、`adversarial text`、`compliance evasion`、`LLM analyzer`

- 🎯 **研究动机**：自动隐私政策分析工具对细微文本操纵的鲁棒性未明
- 🔬 **研究方法**：以细微文本操纵诱导分析器漏检违规条款
- 📌 **结论**：简单改写即可实现compliance evasion

### 15. Unequal Privacy: Auditing Demographic Bias Vulnerabilities in Visual Protection Systems

🌐 [Project](https://doi.org/10.1145/3779208.3785292)　📅 2026　🏷 ACM CCS 2026

**关键词**：`analysis`、`audit`、`visual privacy`、`demographic disparity`、`face obfuscation`

- 🎯 **研究动机**：视觉隐私保护系统的人群偏差未被审计
- 🔬 **研究方法**：审计面部混淆等保护系统在不同人群中的效果差异
- 📌 **结论**：保护效果存在显著demographic disparity