# Web 与 Computer-Use Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究读取网页、截图和 accessibility tree，并通过 browser、mouse、keyboard 或 OS API 完成任务的 Web/Computer-Use Agent。攻击者可以控制页面文本、图像、广告、链接链或跨应用内容；即使 user instruction 完全良性，环境状态、模糊目标和局部合理的多步动作也可能导致付款、下载、secret leakage 或 destructive action。评测必须区分安全拒绝与因能力不足而未完成攻击的“security by incompetence”。

## 研究脉络

- **单页间接注入：** 早期工作在网页 observation 中嵌入指令，验证 Agent 会把环境数据当作更高优先级任务。
- **端到端现实环境：** benchmark 随后引入真实 HTML、hybrid Web-OS sandbox、视觉注入和可产生实际后果的跨应用动作。
- **长程与持久攻击：** 新攻击把目标拆成多个无害子步骤，或让一次恶意 observation 污染 memory 并跨网站、跨 session 激活。
- **良性输入风险：** 研究开始主动搜索 benign instruction 下的 unintended harm，避免只关注明确恶意 user 或 prompt injection。
- **检测与纵深防御：** 防御从页面 segment detection 扩展到 localization、架构隔离、action confirmation 和 trajectory-aware guard。

## Prompt Injection 与环境攻击

### 1. SIR: Self-improving Red-teaming for Compute Use Agents

📄 [arXiv](https://arxiv.org/abs/2608.30207)　📅 2026-09

**关键词**：`attack`、`computer-use agent`、`adaptive IPI red teaming`、`deterministic oracle`

👤 **作者**：Chen Xiong、Zhiyuan He、Pin-Yu Chen、Stjepan Picek、Tsung-Yi Ho

- 🎯 **研究动机**：CUA 安全基准用固定手写注入评测，会低估自适应对手的间接提示注入风险
- 🔬 **研究方法**：提出黑盒攻击 SIR：从少量自然语言原则组合隐蔽注入，用迭代反馈从失败轨迹提炼可复用 bypass 策略，以文件系统／服务／权限状态的确定性 oracle 计分
- 📌 **结论**：三个 frontier CUA 上 ASR 从 4% 升至 24%（Claude Opus 4.8）、0% 升至 28%（Gemini 3.5 Flash）且良性任务仍完成；发现的策略可零额外反馈迁移到不同架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer use agents (CUAs) are vision-language models that perceive a screen and act on a real operating system through mouse, keyboard, and terminal, and they are increasingly deployed to automate everyday digital tasks. Because they can be exposed to untrusted content while operating, they are vulnerable to indirect prompt injection (IPI), in which an adversary plants instructions in content the agent will read and redirects it toward actions that violate the user's intent. Existing CUA safety benchmarks evaluate fixed injections written by hand, which may underestimate the risk posed by an adaptive adversary. We present SIR, a black box IPI attack that (i) composes stealthy injections from a small library of reusable principles stated in plain language and (ii) wraps composition in an iterative feedback loop that diagnoses the victim's failed trajectories and distills the bypasses into new, named strategies that are reapplied across tasks. Unlike prior red teaming of web agents, we target CUAs at the operating system level and score attacks with a fully deterministic oracle, using checks on filesystem, service, and permission state rather than an LLM judge. On experiment, we evaluate three frontier CUAs. Composing principles with feedback raises the attack success rate over a baseline written by hand, for example from 4% to 24% on Claude Opus 4.8 and from 0% to 28% on Gemini 3.5 Flash, while the benign task still completes. Principles discovered against one model further transfer to a different architecture with no additional feedback.

</details>

### 2. StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.06477)　📅 2026-08

**关键词**：`attack`、`CUA prompt injection`、`multi-step decomposition`、`page chain`

👤 **作者**：Zhuoxin Zhan、Akbar Rafiey、Avery Ma、Leila Pishdad、Layla El Asri

- 🎯 **研究动机**：CUA 的间接提示注入研究集中于单页单步注入，现代 agent 会跨页导航与交叉验证
- 🔬 **研究方法**：提出多步间接注入：把对抗目标分解为多个无害子步分布到导航路径上的页面链，自动分解流水线优化每步无害性，构建 480 例基准评测六个 CUA
- 📌 **结论**：固定分解深度下三个 CUA 的 ASR 最多升 31.2 个百分点（GPT-5.4-mini 41.7%→72.9%）；可跟链五 CUA 平均 ASR 从 31.3% 升至 36.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents (CUAs) face a growing threat from indirect prompt injection, where adversarial instructions are planted in the environment such as web pages. In this paper, we introduce multi-step indirect prompt injection, a new attack class against CUAs in which the adversarial goal is decomposed into multiple innocuous-looking sub-steps and distributed across a chain of pages referenced along the agent's navigation path. We develop a pipeline to automatically decompose an adversarial goal under the constraint that the execution of the decomposed sub-steps must achieve the original goal while optimizing the innocuousness of each decomposed sub-step. With this pipeline, we build StepJack, a CUA safety benchmark with 480 test examples. On this benchmark, we evaluate six state-of-the-art CUAs and find that at a fixed decomposition depth, multi-step attacks raise attack success rate (ASR) on three of six CUAs, by up to 31.2 points (e.g., GPT-5.4-mini: 41.7% at single-step to 72.9% at three-step); averaged over the five CUAs that can reliably follow the reference chain (all but EvoCUA-32B), ASR rises from 31.3% at single-step to 36.9% at three-step. Dataset and code are available at https://github.com/BorealisAI/StepJack.

</details>

### 3. Preference Redirection via Attention Concentration: An Attack on Computer Use Agents

📄 [arXiv](https://arxiv.org/abs/2604.08005) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`attack`、`computer-use agent`、`preference redirection`、`prompt injection`、`adversarial patch`

👤 **作者**：Dominik Seip、Matthias Hein

- 🎯 **研究动机**：Computer Use Agent 的攻击研究集中于语言模态，视觉模态漏洞关注不足
- 🔬 **研究方法**：PRAC 通过隐蔽对抗 patch 重定向模型的内部注意力偏好，而非直接攻击 VLM 输出
- 📌 **结论**：在线购物平台上成功操纵 CUA 选中指定商品；白盒构造的攻击可迁移到同模型的微调版本，威胁基于开源权重构建的 CUA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advancements in multimodal foundation models have enabled the development of Computer Use Agents (CUAs) capable of autonomously interacting with GUI environments. As CUAs are not restricted to certain tools, they allow to automate more complex agentic tasks but at the same time open up new security vulnerabilities. While prior work has concentrated on the language modality, the vulnerability of the vision modality has received less attention. In this paper, we introduce PRAC, a novel attack that, unlike prior work targeting the VLM output directly, manipulates the model's internal preferences by redirecting its attention toward a stealthy adversarial patch. We show that PRAC is able to manipulate the selection process of a CUA on an online shopping platform towards a chosen target product. While we require white-box access to the model for the creation of the attack, we show that our attack generalizes to fine-tuned versions of the same model, presenting a critical threat as multiple companies build specific CUAs based on open weights models.

</details>

### 4. Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents

📄 [arXiv](https://arxiv.org/abs/2604.02623) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`attack`、`web-agent memory`、`environment injection`、`cross-session compromise`、`web agent`、`memory poisoning`

👤 **作者**：Wei Zou、…、Jiarong Jiang

- 🎯 **研究动机**：现有记忆攻击假设可直接写记忆存储或跨用户共享，更现实的环境观察污染未被研究
- 🔬 **研究方法**：eTAMP 仅通过一次被污染的环境观察（如浏览被操纵商品页）毒化 agent 记忆，在未来不同网站的任务中激活，绕过权限防御
- 📌 **结论**：VisualWebArena 上 GPT-5-mini ASR 达 32.5%；环境受挫（点击丢失、乱码）使 ASR 最高放大 8 倍，能力更强的模型并不更安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions. While existing security research on memory assumes attackers can directly inject into memory storage or exploit shared memory across users, we present a more realistic threat model: contamination through environmental observation alone. We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access. A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses. Our experiments on (Visual)WebArena reveal two key findings. First, eTAMP achieves substantial attack success rates: up to 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B. Second, we discover Frustration Exploitation: agents under environmental stress become dramatically more susceptible, with ASR increasing up to 8 times when agents struggle with dropped clicks or garbled text. Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance. With the rise of AI browsers like OpenClaw, ChatGPT Atlas, and Perplexity Comet, our findings underscore the urgent need for defenses against environment-injected memory poisoning.

</details>

### 5. MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2602.09222) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/syros)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`attack`、`tool`、`web agent red-teaming`、`indirect prompt injection`、`adaptive attack`

👤 **作者**：Georgios Syros、…、Alina Oprea

- 🎯 **研究动机**：web agent 间接注入评估依赖固定模板与人工选取注入面，无法刻画真实自适应攻击
- 🔬 **研究方法**：MUZZLE 基于 agent 轨迹自动识别高显著性注入面，自适应生成针对机密性/完整性/可用性的恶意指令并按失败反馈迭代
- 📌 **结论**：在 4 个 web 应用上自动发现 44 个新攻击（10 个对抗目标），含 3 个跨应用注入与定制钓鱼场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) based web agents are increasingly deployed to automate complex online tasks by directly interacting with web sites and performing actions on users' behalf. While these agents offer powerful capabilities, their design exposes them to indirect prompt injection attacks embedded in untrusted web content, enabling adversaries to hijack agent behavior and violate user intent. Despite growing awareness of this threat, existing evaluations rely on fixed attack templates, manually selected injection surfaces, or narrowly scoped scenarios, limiting their ability to capture realistic, adaptive attacks encountered in practice. We present MUZZLE, an automated agentic framework for evaluating the security of web agents against indirect prompt injection attacks. MUZZLE utilizes the agent's trajectories to automatically identify high-salience injection surfaces, and adaptively generate context-aware malicious instructions that target violations of confidentiality, integrity, and availability. Unlike prior approaches, MUZZLE adapts its attack strategy based on the agent's observed execution trajectory and iteratively refines attacks using feedback from failed executions. We evaluate MUZZLE across diverse web applications, user tasks, and agent configurations, demonstrating its ability to automatically and adaptively assess the security of web agents with minimal human intervention. Our results show that MUZZLE effectively discovers 44 new attacks on 4 web applications with 10 adversarial objectives that violate confidentiality, availability, or privacy properties across different LLMs and agent scaffolds. MUZZLE also identifies novel attack strategies, including 3 cross-application prompt injection attacks and an agent-tailored phishing scenario.

</details>

### 6. Mind the Gap: Action Rebinding Attacks against Android GUI Agents

📄 [arXiv](https://arxiv.org/abs/2601.12349) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-01　🏷 ACM CCS 2026

**关键词**：`attack`、`Android GUI agent`、`action rebinding`、`observation-action gap`

👤 **作者**：Yi Qian、…、Bing Mao

- 🎯 **研究动机**：GUI agent 跨应用注入输入的设计与 Android 沙箱根本冲突，推理管线的观察-行动间隙可被利用
- 🔬 **研究方法**：零权限恶意应用先渲染良性上下文载体诱出计划动作，再在推理延迟期间切换前台到敏感应用执行劫持；并武器化任务恢复逻辑形成多步利用循环，用 Intent Alignment Strategy 让推理合理化被劫持状态
- 📌 **结论**：六个 Android GUI agent 上原子动作劫持成功率 100%，可实施未授权删文件、发短信与卸载应用；恶意应用无特权 API 调用，商业杀毒扫描检出率 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large multimodal model powered GUI agents are emerging as high-privilege operators on mobile platforms, entrusted to perceive screen content and inject inputs across application boundaries. While these agents aim to automate complex tasks, we demonstrate that their design introduces a fundamental conflict with Android's strict application sandboxing. We present a novel cross-application Action Rebinding attack, which allows a malicious application with zero dangerous permissions to hijack the agent's execution and perform privileged operations on behalf of the attacker. Our attack exploits the inevitable observation-action gap inherent in the agent's reasoning pipeline. A malicious app can render a benign ``contextual carrier'' to elicit a planned action, and then swap the foreground to a sensitive target application during the reasoning latency. The agent, unaware of the transition, unwittingly executes the action in the privileged context. We further advance this attack by weaponizing the agent's own task-recovery logic to create programmable, multi-step exploit loops , and introducing an Intent Alignment Strategy (IAS) that manipulates the agent's reasoning to rationalize the hijacked state. We evaluate our attack on six widely-used Android GUI agents. Our results demonstrate a 100% success rate for atomic action hijacking and the ability to orchestrate high-impact exploits, including unauthorized file deletion, SMS transmission, and app uninstallation, without the attacker holding any corresponding permissions. Furthermore, since the malicious application separates intent from capability and contains no privileged API calls, it achieves a 0% detection rate across commercial malware scanners (e.g., VirusTotal), highlighting a critical blind spot in current mobile security analysis. To access experimental logs and demonstration videos, please contact yi_qian@smail.nju.edu.cn.

</details>

### 7. BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents

📄 [arXiv](https://arxiv.org/abs/2511.20597) · 📊 [Dataset](https://huggingface.co/datasets/perplexity-ai/browsesafe-bench) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-11　🏷 COLM 2026

**关键词**：`defense`、`browser agent`、`realistic HTML`、`defense in depth`

👤 **作者**：Kaiyuan Zhang、Mark Tenenholtz、Kyle Polley、Jerry Ma、Denis Yarats、Ninghui Li

- 🎯 **研究动机**：prompt injection 对浏览器 agent 在真实网页环境中的影响缺乏系统理解与实证评测
- 🔬 **研究方法**：构建嵌入真实 HTML payload 的攻击基准（强调影响真实操作而非文本输出、复杂度与干扰项贴近真实），据此实证评测前沿模型的多种防御，并提出架构与模型相结合的多层防御
- 📌 **结论**：为设计实用安全的 web agent 提供纵深防御蓝图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of artificial intelligence (AI) agents into web browsers introduces security challenges that go beyond traditional web application threat models. Prior work has identified prompt injection as a new attack vector for web agents, yet the resulting impact within real-world environments remains insufficiently understood. In this work, we examine the landscape of prompt injection attacks and synthesize a benchmark of attacks embedded in realistic HTML payloads. Our benchmark goes beyond prior work by emphasizing injections that can influence real-world actions rather than mere text outputs, and by presenting attack payloads with complexity and distractor frequency similar to what real-world agents encounter. We leverage this benchmark to conduct a comprehensive empirical evaluation of existing defenses, assessing their effectiveness across a suite of frontier AI models. We propose a multi-layered defense strategy comprising both architectural and model-based defenses to protect against evolving prompt injection attacks. Our work offers a blueprint for designing practical, secure web agents through a defense-in-depth approach.

</details>

### 8. WebInject: Prompt Injection Attack to Web Agents

🎓 [Official](https://aclanthology.org/2025.emnlp-main.104/)　📅 2025-11　🏷 EMNLP 2025

**关键词**：`attack`、`pixel perturbation`、`visual injection`、`web agent`

👤 **作者**：Xilong Wang、John Bloch、Zedian Shao、Yuepeng Hu、Shuyan Zhou、Neil Zhenqiang Gong

- 🎯 **研究动机**：基于 MLLM 的 web 智能体依据网页截图生成动作，网页环境可被操纵诱导其执行攻击者指定动作
- 🔬 **研究方法**：提出 WebInject：对渲染网页的原始像素加扰动，训练神经网络近似不可微的像素-截图映射，再用 PGD 求解扰动优化问题
- 📌 **结论**：多个数据集上攻击高效且显著优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language model (MLLM)-based web agents interact with webpage environments by generating actions based on screenshots of the webpages. In this work, we propose WebInject, a prompt injection attack that manipulates the webpage environment to induce a web agent to perform an attacker-specified action. Our attack adds a perturbation to the raw pixel values of the rendered webpage. After these perturbed pixels are mapped into a screenshot, the perturbation induces the web agent to perform the attacker-specified action. We formulate the task of finding the perturbation as an optimization problem. A key challenge in solving this problem is that the mapping between raw pixel values and screenshot is non-differentiable, making it difficult to backpropagate gradients to the perturbation. To overcome this, we train a neural network to approximate the mapping and apply projected gradient descent to solve the reformulated optimization problem. Extensive evaluation on multiple datasets shows that WebInject is highly effective and significantly outperforms baselines.

</details>

### 9. Mind the Web: The Security of Web Use Agents

📄 [arXiv](https://arxiv.org/abs/2506.07153) · 🌐 [Project](https://doi.org/10.1145/3779208.3805968)　📅 2025-06　🏷 ACM CCS 2026

**关键词**：`attack`、`browser harness`、`inherited privilege`、`execution constraint`、`web-use agent`、`indirect prompt injection`

👤 **作者**：Avishag Shapira、Parth Atulbhai Gandhi、Edan Habler、Asaf Shabtai

- 🎯 **研究动机**：web-use agent 的广泛浏览器能力带来未被探索的攻击面，网页中的恶意内容可劫持任务执行
- 🔬 **研究方法**：提出 task-aligned injection 把恶意指令伪装成任务引导，构建三阶段自动管线训练注入生成器，按 CIA 三元组组织载荷
- 📌 **结论**：五个 agent 上 ASR 超 80% 且跨载荷、环境与底层 LLM 强迁移，仅需在公开网站发帖即可攻破含内置安全机制的 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-use agents are rapidly being deployed to automate complex web tasks with extensive browser capabilities. However, these capabilities create a critical and previously unexplored attack surface. This paper demonstrates how attackers can exploit web-use agents by embedding malicious content in web pages, such as comments, reviews, or advertisements, that agents encounter during legitimate browsing tasks. We introduce the task-aligned injection technique that frames malicious commands as helpful task guidance rather than obvious attacks, exploiting fundamental limitations in LLMs' contextual reasoning. Agents struggle to maintain coherent contextual awareness and fail to detect when seemingly helpful web content contains steering attempts that deviate them from their original task goal. To scale this attack, we developed an automated three-stage pipeline that generates effective injections without manual annotation or costly online agent interactions during training, remaining efficient even with limited training data. This pipeline produces a generator model that we evaluate on five popular agents using payloads organized by the Confidentiality-Integrity-Availability (CIA) security triad, including unauthorized camera activation, file exfiltration, user impersonation, phishing, and denial-of-service. This generator achieves over 80% attack success rate (ASR) with strong transferability across unseen payloads, diverse web environments, and different underlying LLMs. This attack succeed even against agents with built-in safety mechanisms, requiring only the ability to post content on public websites. To address this risk, we propose comprehensive mitigation strategies including oversight mechanisms, execution constraints, and task-aware reasoning techniques.

</details>

### 10. VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2506.02456) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009231)　📅 2025-06　🏷 ICLR 2026

**关键词**：`benchmark`、`visual prompt injection`、`rendered UI`、`system access`

👤 **作者**：Tri Cao、…、Bryan Hooi

- 🎯 **研究动机**：既有研究聚焦浏览器 agent 与 HTML 级攻击，拥有完整系统权限的 CUA 漏洞未被探索
- 🔬 **研究方法**：提出 VPI-Bench：五大平台 306 个可交互测试用例，把恶意指令视觉嵌入渲染后的用户界面
- 📌 **结论**：CUA 与浏览器 agent 在部分平台被欺骗率分别达 51% 与 100%，系统 prompt 防御收效有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-Use Agents (CUAs) with full system access enable powerful task automation but pose significant security and privacy risks due to their ability to manipulate files, access user data, and execute arbitrary commands. While prior work has focused on browser-based agents and HTML-level attacks, the vulnerabilities of CUAs remain underexplored. In this paper, we investigate Visual Prompt Injection (VPI) attacks, where malicious instructions are visually embedded within rendered user interfaces, and examine their impact on both CUAs and Browser-Use Agents (BUAs). We propose VPI-Bench, a benchmark of 306 test cases across five widely used platforms, to evaluate agent robustness under VPI threats. Each test case is a variant of a web platform, designed to be interactive, deployed in a realistic environment, and containing a visually embedded malicious prompt. Our empirical study shows that current CUAs and BUAs can be deceived at rates of up to 51% and 100%, respectively, on certain platforms. The experimental results also indicate that system prompt defenses offer only limited improvements. These findings highlight the need for robust, context-aware defenses to ensure the safe deployment of multimodal AI agents in real-world environments. The code and dataset are available at: https://github.com/cua-framework/agents

</details>

### 11. AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents

🎓 [Official](https://aclanthology.org/2025.findings-emnlp.1258/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`indirect prompt injection`、`black-box red teaming`、`MCTS`

👤 **作者**：Zhun Wang、…、Dawn Song

- 🎯 **研究动机**：间接提示注入是 LLM agent 的核心安全风险，手工攻击效率低
- 🔬 **研究方法**：AGENTVIGIL 构建高质量初始种子语料，用基于 MCTS 的种子选择算法迭代精炼输入，自动发现并利用间接注入漏洞
- 📌 **结论**：在 AgentDojo 与 VWA-adv 上对 o3-mini 与 GPT-4o 的 agent 分别达 71% 与 70% 成功率，约为手工基线两倍；对未见任务、内部 LLM 与防御均有强迁移性，真实环境中可诱导 agent 导航至恶意 URL

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

There emerges a critical security risk of LLM agents: indirect prompt injection, a sophisticated attack vector that compromises thecore of these agents, the LLM, by manipulating contextual information rather than direct user prompts. In this work, we propose a generic black-box optimization framework, AGENTVIGIL, designed to automatically discover and exploit indirect prompt injection vulnerabilities across diverse LLM agents. Our approach starts by constructing a high-quality initial seed corpus, then employs a seed selectionalgorithm based on Monte Carlo Tree Search (MCTS) to iteratively refine inputs, therebymaximizing the likelihood of uncovering agent weaknesses. We evaluate AGENTVIGIL on twopublic benchmarks, AgentDojo and VWA-adv, where it achieves 71% and 70% success rates against agents based on o3-mini and GPT-4o, respectively, nearly doubling the performance of handcrafted baseline attacks. Moreover, AGENTVIGIL exhibits strong transferability across unseen tasks and internal LLMs, as well as promising results against defenses. Beyondbenchmark evaluations, we apply our attacks in real-world environments, successfully misleading agents to navigate to arbitrary URLs,including malicious sites.

</details>

### 12. WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2504.18575) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1c9818387f5dd0a0bc151214660f059d-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2025-04　🏷 NeurIPS 2025

**关键词**：`benchmark`、`web prompt injection`、`end-to-end action`、`security by incompetence`

👤 **作者**：Ivan Evtimov、Arman Zharmagambetov、Aaron Grattafiori、Chuan Guo、Kamalika Chaudhuri

- 🎯 **研究动机**：现有 web agent 注入测试场景失真、攻击者权限过大且多为单步孤立任务
- 🔬 **研究方法**：提出 WASP 基准，以真实低人力注入对 web agent 做端到端安全评测
- 📌 **结论**：顶级含推理模型也被简单人写注入欺骗，攻击部分成功率最高 86%，却常因能力不足完不成攻击目标

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous UI agents powered by AI have tremendous potential to boost human productivity by automating routine tasks such as filing taxes and paying bills. However, a major challenge in unlocking their full potential is security, which is exacerbated by the agent's ability to take action on their user's behalf. Existing tests for prompt injections in web agents either over-simplify the threat by testing unrealistic scenarios or giving the attacker too much power, or look at single-step isolated tasks. To more accurately measure progress for secure web agents, we introduce WASP -- a new publicly available benchmark for end-to-end evaluation of Web Agent Security against Prompt injection attacks. Evaluating with WASP shows that even top-tier AI models, including those with advanced reasoning capabilities, can be deceived by simple, low-effort human-written injections in very realistic scenarios. Our end-to-end evaluation reveals a previously unobserved insight: while attacks partially succeed in up to 86% of the case, even state-of-the-art agents often struggle to fully complete the attacker goals -- highlighting the current state of security by incompetence.

</details>

### 13. AdvAgent: Controllable Blackbox Red-teaming on Web Agents

📄 [arXiv](https://arxiv.org/abs/2410.17401) · 🌐 [Project](https://proceedings.mlr.press/v267/xu25m.html)　📅 2024-10　🏷 ICML 2025

**关键词**：`attack`、`web-agent red teaming`、`black-box feedback`、`DPO`

👤 **作者**：Chejian Xu、…、Bo Li

- 🎯 **研究动机**：Web Agent 掌控敏感资源与自主决策，白盒梯度攻击与手工 prompt 难以系统暴露其漏洞
- 🔬 **研究方法**：提出 AdvAgent 黑盒红队框架：RL 训练对抗 prompter，用受害 Agent 的黑盒反馈优化对抗 prompt，兼顾隐蔽性与可控性、支持低成本改写目标动作
- 📌 **结论**：对基于 GPT-4 的 SOTA Web Agent 在多类任务上取得高成功率，现有 prompt 防御仅提供有限保护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Foundation model-based agents are increasingly used to automate complex tasks, enhancing efficiency and productivity. However, their access to sensitive resources and autonomous decision-making also introduce significant security risks, where successful attacks could lead to severe consequences. To systematically uncover these vulnerabilities, we propose AdvAgent, a black-box red-teaming framework for attacking web agents. Unlike existing approaches, AdvAgent employs a reinforcement learning-based pipeline to train an adversarial prompter model that optimizes adversarial prompts using feedback from the black-box agent. With careful attack design, these prompts effectively exploit agent weaknesses while maintaining stealthiness and controllability. Extensive evaluations demonstrate that AdvAgent achieves high success rates against state-of-the-art GPT-4-based web agents across diverse web tasks. Furthermore, we find that existing prompt-based defenses provide only limited protection, leaving agents vulnerable to our framework. These findings highlight critical vulnerabilities in current web agents and emphasize the urgent need for stronger defense mechanisms. We release code at https://ai-secure.github.io/AdvAgent/.

</details>

### 14. Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks

📄 [arXiv](https://arxiv.org/abs/2603.04364)　📅 2026-03

**关键词**：`defense`、`cross-modal injection`、`adversarial training`、`multimodal web agent`

👤 **作者**：Haoyu Liu、Dingcheng Li、Lukas Rutishauser、Zeyu Zheng

- 🎯 **研究动机**：DOM 注入会以一致欺骗叙事同时污染截图与 accessibility tree 双通道，文本中心的 VLM 安全训练失效
- 🔬 **研究方法**：DMAST 把攻防建模为二人零和 Markov 博弈，经 teacher 模仿、零确认策略的 oracle 引导 SFT 与 GRPO 自博弈对抗 RL 三阶段共同训练
- 📌 **结论**：分布外任务上大幅缓解对抗风险且任务完成效率翻倍，显著超越训练型与提示型防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal web agents that process both screenshots and accessibility trees are increasingly deployed to interact with web interfaces, yet their dual-stream architecture opens an underexplored attack surface: an adversary who injects content into the webpage DOM simultaneously corrupts both observation channels with a consistent deceptive narrative. Our vulnerability analysis on MiniWob++ reveals that attacks including a visual component far outperform text-only injections, exposing critical gaps in text-centric VLM safety training. Motivated by this finding, we propose Dual-Modality Multi-Stage Adversarial Safety Training (DMAST), a framework that formalizes the agent-attacker interaction as a two-player zero-sum Markov game and co-trains both players through a three-stage pipeline: (1) imitation learning from a strong teacher model, (2) oracle-guided supervised fine-tuning that uses a novel zero-acknowledgment strategy to instill task-focused reasoning under adversarial noise, and (3) adversarial reinforcement learning via Group Relative Policy Optimization (GRPO) self-play. On out-of-distribution tasks, DMAST substantially mitigates adversarial risks while simultaneously doubling task completion efficiency. Our approach significantly outperforms established training-based and prompt-based defenses, demonstrating genuine co-evolutionary progress and robust generalization to complex, unseen environments.

</details>

### 15. MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs

📄 [arXiv](https://arxiv.org/abs/2601.18113) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.716/)　📅 2026-01　🏷 ACL 2026

**关键词**：`benchmark`、`malicious URL`、`URL obfuscation`、`URLGuard`

👤 **作者**：Dezhang Kong、…、Meng Han

- 🎯 **研究动机**：web agent 接受伪装恶意 URL 后会继续访问危险页面，该威胁此前无基准
- 🔬 **研究方法**：构建含 61845 个攻击实例、覆盖 10 类真实场景与 7 类恶意网站的 MalURLBench，评测 12 个流行 LLM 并提出轻量防御 URLGuard
- 📌 **结论**：现有模型普遍难以识别精心伪装的恶意 URL，并分析了影响攻击成功率的关键因素

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based web agents have become increasingly popular for their utility in daily life and work. However, they exhibit critical vulnerabilities when processing malicious URLs: accepting a disguised malicious URL enables subsequent access to unsafe webpages, which can cause severe damage to service providers and users. Despite this risk, no benchmark currently targets this emerging threat. To address this gap, we propose MalURLBench, the first benchmark for evaluating LLMs' vulnerabilities to malicious URLs. MalURLBench contains 61,845 attack instances spanning 10 real-world scenarios and 7 categories of real malicious websites. Experiments with 12 popular LLMs reveal that existing models struggle to detect elaborately disguised malicious URLs. We further identify and analyze key factors that impact attack success rates and propose URLGuard, a lightweight defense module. We believe this work will provide a foundational resource for advancing the security of web agents. Our code is available at https://github.com/JiangYingEr/MalURLBench.

</details>

### 16. Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents

📄 [arXiv](https://arxiv.org/abs/2609.03438)　📅 2026-09

**关键词**：`defense`、`multimodal action guard`、`conflict detection`、`safe abstention`、`GUI agent`、`conflict-aware termination`

👤 **作者**：Zhaoyuan Huang、…、Zhuosheng Zhang

- 🎯 **研究动机**：真实用户会发出不可行的错误指令，而 GUI Agent 在指令内部或指令-界面证据冲突时仍盲目执行，呈现 execution-biased overcompliance
- 🔬 **研究方法**：构建覆盖指令内部与指令-GUI 上下文冲突的 CONFLICTGUI 基准，并提出推理时框架 CONFLICTGUARD：行动前可行性验证协议加条件动作调制，把过度顺从的执行导向终止行为
- 📌 **结论**：五个常用 Agent 上平均冲突任务成功率显著提升且正常 GUI 任务性能保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent's feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent's competence to identify inappropriate execution scenarios and refrain from unnecessary actions.

</details>

### 17. The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2604.10577)　📅 2026-04

**关键词**：`benchmark`、`benign instruction`、`environmental hazard`、`OS-BLIND`

👤 **作者**：Xuwei Ding、…、Jieyu Zhao

- 🎯 **研究动机**：CUA 安全评测聚焦显式滥用与 prompt 注入，忽视用户指令完全良性、伤害源于任务上下文或执行结果的情形
- 🔬 **研究方法**：OS-BLIND 含 300 个人工任务、12 类风险、8 个应用，分环境嵌入威胁与 agent 主动伤害两簇
- 📌 **结论**：多数 CUA 的 ASR 超 90%，Claude 4.5 Sonnet 达 73.0%，多智能体部署下升至 92.7%；安全对齐主要在前几步激活、很少在执行中重新触发

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents (CUAs) can now autonomously complete complex tasks in real digital environments, but when misled, they can also be used to automate harmful actions programmatically. Existing safety evaluations largely target explicit threats such as misuse and prompt injection, but overlook a subtle yet critical setting where user instructions are entirely benign and harm arises from the task context or execution outcome. We introduce OS-BLIND, a benchmark that evaluates CUAs under unintended attack conditions, comprising 300 human-crafted tasks across 12 categories, 8 applications, and 2 threat clusters: environment-embedded threats and agent-initiated harms. Our evaluation on frontier models and agentic frameworks reveals that most CUAs exceed 90% attack success rate (ASR), and even the safety-aligned Claude 4.5 Sonnet reaches 73.0% ASR. More interestingly, this vulnerability becomes even more severe, with ASR rising from 73.0% to 92.7% when Claude 4.5 Sonnet is deployed in multi-agent systems. Our analysis further shows that existing safety defenses provide limited protection when user instructions are benign. Safety alignment primarily activates within the first few steps and rarely re-engages during subsequent execution. In multi-agent systems, decomposed subtasks obscure the harmful intent from the model, causing safety-aligned models to fail. We will release our OS-BLIND to encourage the broader research community to further investigate and address these safety challenges.

</details>

### 18. AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2604.02947)　📅 2026-04

**关键词**：`benchmark`、`computer-use agent`、`locally legitimate step`、`cumulative harm`

👤 **作者**：Yunhao Feng、…、Yanming Guo

- 🎯 **研究动机**：CUA 的危害可由局部合理但整体越权的动作序列涌现，现有评测不覆盖
- 🔬 **研究方法**：AgentHazard 含 2,653 个实例：把有害目标配以局部合法的操作步骤序列，评测 agent 能否识别并中断累积性危害
- 📌 **结论**：当前系统高度脆弱：Qwen3-Coder 驱动的 Claude Code ASR 达 73.63%，模型对齐本身不能保证自主 agent 安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents extend language models from text generation to persistent action over tools, files, and execution environments. Unlike chat systems, they maintain state across interactions and translate intermediate outputs into concrete actions. This creates a distinct safety challenge in that harmful behavior may emerge through sequences of individually plausible steps, including intermediate actions that appear locally acceptable but collectively lead to unauthorized actions. We present \textbf{AgentHazard}, a benchmark for evaluating harmful behavior in computer-use agents. AgentHazard contains \textbf{2,653} instances spanning diverse risk categories and attack strategies. Each instance pairs a harmful objective with a sequence of operational steps that are locally legitimate but jointly induce unsafe behavior. The benchmark evaluates whether agents can recognize and interrupt harm arising from accumulated context, repeated tool use, intermediate actions, and dependencies across steps. We evaluate AgentHazard on Claude Code, OpenClaw, and IFlow using mostly open or openly deployable models from the Qwen3, Kimi, GLM, and DeepSeek families. Our experimental results indicate that current systems remain highly vulnerable. In particular, when powered by Qwen3-Coder, Claude Code exhibits an attack success rate of \textbf{73.63\%}, suggesting that model alignment alone does not reliably guarantee the safety of autonomous agents.

</details>

### 19. When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2602.08235) · 🌐 [Project](https://osu-nlp-group.github.io/AutoElicit/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64242)　📅 2026-02　🏷 ICML 2026

**关键词**：`analysis`、`benign perturbation`、`unintended behavior`、`AutoElicit`、`agent safety`、`empirical evaluation`

👤 **作者**：Jaylen Jones、…、Huan Sun

- 🎯 **研究动机**：CUA 在良性输入下也会产生有害非预期行为，该风险仅有轶事描述，缺少自动挖掘方法
- 🔬 **研究方法**：定义非预期行为特征框架并提出 AutoElicit：用 CUA 执行反馈迭代扰动良性指令，保持扰动真实且良性
- 📌 **结论**：从 Claude 4.5 Haiku/Opus 与 Operator 浮现数百种有害非预期行为，并可持续迁移至其他前沿 CUA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although computer-use agents (CUAs) hold significant potential to automate increasingly complex OS workflows, they can demonstrate unsafe unintended behaviors that deviate from expected outcomes even under benign input contexts. However, exploration of this risk remains largely anecdotal, lacking concrete characterization and automated methods to proactively surface long-tail unintended behaviors under realistic CUA scenarios. To fill this gap, we introduce the first conceptual and methodological framework for unintended CUA behaviors, by defining their key characteristics, automatically eliciting them, and analyzing how they arise from benign inputs. We propose AutoElicit: an agentic framework that iteratively perturbs benign instructions using CUA execution feedback, and elicits severe harms while keeping perturbations realistic and benign. Using AutoElicit, we surface hundreds of harmful unintended behaviors from state-of-the-art CUAs such as Claude 4.5 Haiku, Claude 4.5 Opus, and Operator. We further evaluate the transferability of human-verified successful perturbations, identifying persistent susceptibility to unintended behaviors across various other frontier CUAs. This work establishes a foundation for systematically analyzing unintended behaviors in realistic computer-use settings.

</details>

### 20. ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents

📄 [arXiv](https://arxiv.org/abs/2410.06703) · 🌐 [Project](https://sites.google.com/view/st-webagentbench/home) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009904)　📅 2024-10　🏷 ICLR 2026

**关键词**：`benchmark`、`enterprise policy`、`completion under policy`、`trustworthiness`

👤 **作者**：Ido Levy、…、Segev Shlomov

- 🎯 **研究动机**：Web Agent 基准只测任务是否完成，忽略安全性与企业信任要求
- 🔬 **研究方法**：ST-WebAgentBench 给 222 个任务配套 ST policy 与六维评分，定义 Completion under Policy 与 Risk Ratio 指标
- 📌 **结论**：三个开源 Agent 的 CuP 不足名义完成率的三分之二，暴露关键安全差距

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous web agents solve complex browsing tasks, yet existing benchmarks measure only whether an agent finishes a task, ignoring whether it does so safely or in a way enterprises can trust. To integrate these agents into critical workflows, safety and trustworthiness (ST) are prerequisite conditions for adoption. We introduce \textbf{\textsc{ST-WebAgentBench}}, a configurable and easily extensible suite for evaluating web agent ST across realistic enterprise scenarios. Each of its 222 tasks is paired with ST policies, concise rules that encode constraints, and is scored along six orthogonal dimensions (e.g., user consent, robustness). Beyond raw task success, we propose the \textit{Completion Under Policy} (\textit{CuP}) metric, which credits only completions that respect all applicable policies, and the \textit{Risk Ratio}, which quantifies ST breaches across dimensions. Evaluating three open state-of-the-art agents reveals that their average CuP is less than two-thirds of their nominal completion rate, exposing critical safety gaps. By releasing code, evaluation templates, and a policy-authoring interface, \href{https://sites.google.com/view/st-webagentbench/home}{\textsc{ST-WebAgentBench}} provides an actionable first step toward deploying trustworthy web agents at scale.

</details>

### 21. SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction

📄 [arXiv](https://arxiv.org/abs/2607.15550)　📅 2026-09

**关键词**：`defense`、`mobile GUI agent`、`world model`、`pre-execution risk`

👤 **作者**：Xue Yu、Bo Yuan、Kailin Zhao、Pengshuai Yang、Hong Hu、Junlan Feng

- 🎯 **研究动机**：移动 GUI agent 单个错误操作可造成不可逆后果，现有安全机制以事后反应为主、缺乏执行前风险评估
- 🔬 **研究方法**：提出 SeerGuard：指令级预筛+动作级风险评估，经多任务学习构建融合语义下一状态预测与安全风险评估的统一安全增强 world model（SAWM）
- 📌 **结论**：Qwen3-VL-8B-Instruct 上安全-效用分从 0.191 升至 0.596，风险代价分从 0.347 降至 0.135，且跨 GUI agent 泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks because a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. Specifically, the action-level assessment analyzes agent-proposed actions within current GUI states, anticipating likely outcomes to identify risks before they are executed. To enable these capabilities, we construct a unified safety-augmented world model (SAWM) via multi-task learning, integrating semantic next-state prediction with safety risk assessment. Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents. On Qwen3-VL-8B-Instruct, it increases the safety-utility score from $0.191$ to $0.596$ at $ω=0.8$ and reduces the risk-cost score from $0.347$ to $0.135$ at $α=0.8$. Further analyses on our SAWM validate the effectiveness of the instruction-level screening, alongside the capability of action risk assessment and next-state prediction.

</details>

### 22. CURA: Certified Runtime Alarms for Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2608.27808)　📅 2026-08

**关键词**：`detection`、`harness telemetry`、`sequential alarm`、`certified false alarm`、`computer-use agent`、`online failure alarm`

👤 **作者**：Divake Kumar、…、Amit Ranjan Trivedi

- 🎯 **研究动机**：computer-use Agent 的自我报告恰在最需要监督处失效：OSWorld 上 71 次失败中 64 次以成功声明结束，显式失败通道在约 9,100 次调用中几乎不用
- 🔬 **研究方法**：提出 CURA 外部监控器，只读 harness 可见遥测（无模型内部、无额外 LLM 调用、无 prompt 修改），把运行轨迹转为带认证假警报控制的 CUSUM 序贯检验
- 📌 **结论**：α=0.10 时以 0.066 实际假警报率、提前中位数 31 步检出 42.3% 失败，同等认证预算下在线召回 0.41 对 token 基线 0.34，级联中途监督挽回 70 次失败中的 23 次

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-report is the cheapest oversight channel a deployer has, and on capable computer-use agents (CUAs) it fails precisely where oversight matters. On 361 OSWorld tasks our pipeline, a read-only feasibility gate, a planner, and a GUI executor, reaches a mean task score of 82.9, above the 72.4 human reference, yet 64 of its 71 failures (90%) end with a success claim, 61 acknowledging no blocker, and the explicit failure affordance is never used in roughly 9,100 calls. We introduce CURA (Certified Runtime Alarms for Computer-Use Agents), an external monitor that reads only harness-visible telemetry, with no model internals, extra LLM calls, or prompt changes, and turns the running trajectory into a sequential test with certified false-alarm control. At alpha = 0.10 its CUSUM alarm detects 42.3% of failures a median of 31 steps before termination at a realized false-alarm rate of 0.066, and risk is partly resolvable before the first action (gate probe, 0.69 AUROC). Retrospectively the composite reaches 0.828 AUROC (fold-internal floor 0.802), but its margin over a total-token baseline is not significant (Delta = +0.026, p = 0.101); the separation is online, where CURA recalls more at matched certified budgets: 0.41 versus 0.34 at alpha = 0.10, 0.56 versus 0.38 at alpha = 0.20. Alarm-gated mid-execution oversight recovers 23 of 70 failures while spending a frontier overseer on 38, giving a deployable cascade at mean score 86.8 and 84.5% full-solve (305 of 361). The certificate bounds false alarms only. We also report where behavioral monitoring is uninformative.

</details>

### 23. When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2602.08995) · 🌐 [Project](https://osu-nlp-group.github.io/Misaligned-Action-Detection/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64196)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`action alignment`、`MisActBench`、`pre-execution correction`、`LLM agent security`

👤 **作者**：Yuting Ning、…、Huan Sun

- 🎯 **研究动机**：CUA 频繁产生偏离用户意图的失准动作，无论源于间接注入还是内部错误均未被定义与研究
- 🔬 **研究方法**：构建带人工动作级对齐标注的 MisActBench，并提出执行前检测、结构化反馈迭代纠正的 DeAction 护栏
- 📌 **结论**：MisActBench 上 F1 超基线 15 个百分点以上，在线对抗场景攻击成功率降超 90% 且不损任务成功率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents (CUAs) have made tremendous progress in the past year, yet they still frequently produce misaligned actions that deviate from the user's original intent. Such misaligned actions may arise from external attacks (e.g., indirect prompt injection) or from internal limitations (e.g., erroneous reasoning). They not only expose CUAs to safety risks, but also degrade task efficiency and reliability. This work makes the first effort to define and study misaligned action detection in CUAs, with comprehensive coverage of both externally induced and internally arising misaligned actions. We further identify three common categories in real-world CUA deployment and construct MisActBench, a benchmark of realistic trajectories with human-annotated, action-level alignment labels. Moreover, we propose DeAction, a practical and universal guardrail that detects misaligned actions before execution and iteratively corrects them through structured feedback. DeAction outperforms all existing baselines across offline and online evaluations with moderate latency overhead: (1) On MisActBench, it outperforms baselines by over 15% absolute in F1 score; (2) In online evaluation, it reduces attack success rate by over 90% under adversarial settings while preserving or even improving task success rate in benign environments.

</details>

### 24. WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents

📄 [arXiv](https://arxiv.org/abs/2602.03792)　📅 2026-02

**关键词**：`detection`、`web prompt injection`、`segment localization`、`context consistency`

👤 **作者**：Xilong Wang、Yinuo Liu、Zhun Wang、Dawn Song、Neil Gong

- 🎯 **研究动机**：网页 prompt injection 的检测与定位方法在 web agent 设定下底层假设常不成立
- 🔬 **研究方法**：WebSentinel 两步：抽取可能被污染的 interest segments，再以网页内容为上下文逐段检查一致性
- 📌 **结论**：在收集的污染与干净网页数据集上，检测与定位效果均大幅超越基线方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks manipulate webpage content to cause web agents to execute attacker-specified tasks instead of the user's intended ones. Existing methods for detecting and localizing such attacks achieve limited effectiveness, as their underlying assumptions often do not hold in the web-agent setting. In this work, we propose WebSentinel, a two-step approach for detecting and localizing prompt injection attacks in webpages. Given a webpage, Step I extracts \emph{segments of interest} that may be contaminated, and Step II evaluates each segment by checking its consistency with the webpage content as context. We show that WebSentinel is highly effective, substantially outperforming baseline methods across multiple datasets of both contaminated and clean webpages that we collected. Our code is available at: https://github.com/wxl-lxw/WebSentinel.

</details>

### 25. WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents

📄 [arXiv](https://arxiv.org/abs/2510.01354)　📅 2025-10

**关键词**：`benchmark`、`multimodal injection`、`detector evaluation`、`imperceptible attack`

👤 **作者**：Yinuo Liu、Ruohan Xu、Xilong Wang、Yuqi Jia、Neil Zhenqiang Gong

- 🎯 **研究动机**：面向 web agent 的 prompt 注入检测方法缺乏系统评测
- 🔬 **研究方法**：按威胁模型细分类攻击，构建含恶意文本段、四类良性文本、恶意图像与两类良性图像的数据集，系统评估文本与图像检测方法
- 📌 **结论**：对显式文本指令或可见扰动可达中高精度，但对无显式指令或不可感知扰动的攻击基本失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multiple prompt injection attacks have been proposed against web agents. At the same time, various methods have been developed to detect general prompt injection attacks, but none have been systematically evaluated for web agents. In this work, we bridge this gap by presenting the first comprehensive benchmark study on detecting prompt injection attacks targeting web agents. We begin by introducing a fine-grained categorization of such attacks based on the threat model. We then construct datasets containing both malicious and benign samples: malicious text segments generated by different attacks, benign text segments from four categories, malicious images produced by attacks, and benign images from two categories. Next, we systematize both text-based and image-based detection methods. Finally, we evaluate their performance across multiple scenarios. Our key findings show that while some detectors can identify attacks that rely on explicit textual instructions or visible image perturbations with moderate to high accuracy, they largely fail against attacks that omit explicit instructions or employ imperceptible perturbations. Our datasets and code are released at: https://github.com/Norrrrrrr-lyn/WAInjectBench.

</details>

### 26. LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents

📄 [arXiv](https://arxiv.org/abs/2507.10610) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_LaSM_Layer-wise_Scaling_Mechanism_for_Defending_Pop-up_Attack_on_GUI_CVPR_2026_paper.html)　📅 2025-07　🏷 CVPR 2026

**关键词**：`defense`、`GUI agent`、`pop-up attack`、`layer scaling`

👤 **作者**：Zihe Yan、Jiaping Gui、Zhuosheng Zhang、Gongshen Liu

- 🎯 **研究动机**：GUI agent 对弹窗环境注入攻击高度脆弱，现有防御需昂贵重训或干扰下表现差
- 🔬 **研究方法**：发现正确与错误输出存在层级注意力分歧模式，提出 LaSM 免训练选择性放大关键层的 attention 与 MLP 模块
- 📌 **结论**：多数据集上显著提高防御成功率与鲁棒性，对模型通用能力几乎无影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graphical user interface (GUI) agents built on multimodal large language models (MLLMs) have recently demonstrated strong decision-making abilities in screen-based interaction tasks. However, they remain highly vulnerable to pop-up-based environmental injection attacks, where malicious visual elements divert model attention and lead to unsafe or incorrect actions. Existing defense methods either require costly retraining or perform poorly under inductive interference. In this work, we systematically study how such attacks alter the attention behavior of GUI agents and uncover a layer-wise attention divergence pattern between correct and incorrect outputs. Based on this insight, we propose \textbf{LaSM}, a \textit{Layer-wise Scaling Mechanism} that selectively amplifies attention and MLP modules in critical layers. LaSM improves the alignment between model saliency and task-relevant regions without additional training. Extensive experiments across multiple datasets demonstrate that our method significantly improves the defense success rate and exhibits strong robustness, while having negligible impact on the model's general capabilities. Our findings reveal that attention misalignment is a core vulnerability in MLLM agents and can be effectively addressed through selective layer-wise modulation. Our code can be found in https://github.com/YANGTUOMAO/LaSM.

</details>

### 27. RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

📄 [arXiv](https://arxiv.org/abs/2505.21936) · 🌐 [Project](https://osu-nlp-group.github.io/RedTeamCUA/) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006548)　📅 2025-05　🏷 ICLR 2026

**关键词**：`benchmark`、`hybrid sandbox`、`CUA red teaming`、`indirect prompt injection`

👤 **作者**：Zeyi Liao、…、Huan Sun

- 🎯 **研究动机**：计算机使用 agent 的间接 prompt 注入评测缺乏真实可控环境，且忽视 web 与 OS 混合攻击场景
- 🔬 **研究方法**：提出融合 VM OS 与 Docker web 的 RedTeamCUA 混合沙箱及 864 例 RTC-Bench，支持从注入点直接初始化测试
- 📌 **结论**：Claude 3.7 Sonnet CUA ASR 42.9%、Operator 7.6%；最强 Claude 4.5 Sonnet CUA 端到端 ASR 达 60%，尝试率高达 92.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents (CUAs) promise to automate complex tasks across operating systems (OS) and the web, but remain vulnerable to indirect prompt injection. Current evaluations of this threat either lack support realistic but controlled environments or ignore hybrid web-OS attack scenarios involving both interfaces. To address this, we propose RedTeamCUA, an adversarial testing framework featuring a novel hybrid sandbox that integrates a VM-based OS environment with Docker-based web platforms. Our sandbox supports key features tailored for red teaming, such as flexible adversarial scenario configuration, and a setting that decouples adversarial evaluation from navigational limitations of CUAs by initializing tests directly at the point of an adversarial injection. Using RedTeamCUA, we develop RTC-Bench, a comprehensive benchmark with 864 examples that investigate realistic, hybrid web-OS attack scenarios and fundamental security vulnerabilities. Benchmarking current frontier CUAs identifies significant vulnerabilities: Claude 3.7 Sonnet | CUA demonstrates an ASR of 42.9%, while Operator, the most secure CUA evaluated, still exhibits an ASR of 7.6%. Notably, CUAs often attempt to execute adversarial tasks with an Attempt Rate as high as 92.5%, although failing to complete them due to capability limitations. Nevertheless, we observe concerning high ASRs in realistic end-to-end settings, with the strongest-to-date Claude 4.5 Sonnet | CUA exhibiting the highest ASR of 60%, indicating that CUA threats can already result in tangible risks to users and computer systems. Overall, RedTeamCUA provides an essential framework for advancing realistic, controlled, and systematic analysis of CUA vulnerabilities, highlighting the urgent need for robust defenses to indirect prompt injection prior to real-world deployment.

</details>

### 28. Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments

📄 [arXiv](https://arxiv.org/abs/2608.24099)　📅 2026-08

**关键词**：`benchmark`、`Android GUI agent`、`runtime anomaly`、`adversarial environment`

👤 **作者**：Guo Gan、…、Hong Zhou

- 🎯 **研究动机**：Android GUI Agent 常遇弹窗等运行时异常，现有 benchmark 缺乏鲁棒性系统评测
- 🔬 **研究方法**：AnTrap 把异常分为 State、Thinking、Action、Round 四层十类，向轨迹注入保持任务可解的扰动，评测 16 个模型并用 GRPO 验证
- 📌 **结论**：所有模型普遍显著退化；单步陷阱可经对抗 RL 缓解，state deadlock 等深层陷阱无法靠训练解决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories. We propose a taxonomy organizing real-world anomalies into four layers (State, Thinking, Action and Round) with ten fine-grained subcategories, and develop a construction pipeline that preserves task solvability while introducing realistic adversarial conditions. Evaluating 16 leading GUI models, we reveal universal vulnerability to dynamic anomalies, with even the strongest models suffering significant performance degradation. Furthermore, we conduct GRPO training in both original and adversarial environments to validate our benchmark, separating environment-learnable anomalies from reasoning-bottlenecked ones. Our findings show that while single-step traps at state and action layers are largely addressable through adversarial reinforcement learning, deep contextual traps, like state deadlock, expose intrinsic limitations that cannot be resolved by training in environments with traps alone.

</details>

### 29. MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps

📄 [arXiv](https://arxiv.org/abs/2608.17659)　📅 2026-08

**关键词**：`benchmark`、`prompt injection`、`safety alignment`、`computer-use agent`

👤 **作者**：Sujin Chen、Lijun Li、Tianyi Du、Jing Shao

- 🎯 **研究动机**：GUI agent 处理日常移动场景中的不可信环境内容，对环境注入攻击缺系统评测
- 🔬 **研究方法**：MobileWorldSafety 含 142 个基于真实 Android 应用的风险任务，在最终系统状态上定义程序可验证风险指标，规则验证加 LLM judge 两阶段管线区分安全与能力失败
- 📌 **结论**：六个 agent 的 ASR 为 40.4%-66.9%——对抗内容以普通移动上下文呈现时均难维持安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to environmental injection attacks, which include indirect prompt injections and adversarial instructions. Such attacks can manipulate the behavior of agents without user awareness through diverse channels encountered in everyday mobile use. Despite these risks, existing benchmarks often fail to capture everyday user scenarios, lacking a systematic evaluation of GUI agents under environmental injection attacks on mobile devices. To address this gap, we introduce MobileWorldSafety, a benchmark of 142 risk tasks built on real Android applications. For each task, we define a programmatically verifiable risk indicator over the final system state and evaluate outcomes with a two-stage pipeline: rule-based verification handles unambiguous cases, while an LLM judge adjudicates ambiguous ones. This distinguishes safety failures from capability failures and enables objective and reproducible assessment. Evaluations on six agents, including both general agents and specialized GUI agents, demonstrate that all agents remain highly vulnerable, with attack success rates ranging from 40.4% to 66.9%. These findings indicate that current agents often fail to maintain safety alignment when adversarial content is presented as ordinary mobile context. MobileWorldSafety provides a foundation for quantifying these vulnerabilities and advancing research on robust mobile GUI agents.

</details>

### 30. Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces

🎓 [Official](https://aclanthology.org/2026.acl-long.1009/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`agent safety`、`web agent`、`environmental prompt injection`、`deceptive behavior`、`LLM agent`

👤 **作者**：Zijing Shi、Meng Fang、Ling Chen

- 🎯 **研究动机**：自主 web agent 在电商欺骗性界面下的安全缺乏受控评测
- 🔬 **研究方法**：WebDecept 可配置插件框架向现有 web 环境注入定向广告、域名重定向、购物操纵等七种常见欺骗模式，受控评估多个多模态 web agent
- 📌 **结论**：当前 web agent 对多类欺骗界面高度易感，基于提示的约束往往不足以缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As autonomous web agents are increasingly deployed to perform real-world tasks, ensuring their safety has become a critical concern. In this work, we study web agent behavior under realistic deceptive interfaces in the e-commerce domain. We introduce WebDecept, a lightweight and configurable plugin framework that enables controlled injection of deceptive interface patterns into existing web environments. Using WebDecept, we instantiate seven deceptive patterns commonly observed on the open web, including targeted advertisements, domain redirection, and shopping manipulation. By injecting these patterns into the frontend during task execution, we perform controlled evaluation of multiple multimodal web agents. Our results show that current web agents are highly susceptible to multiple classes of deceptive interfaces, and that prompt-based constraints are often insufficient to mitigate these failures. We further analyze how the design choices of deceptive patterns influence the success of such manipulations. These findings highlight safety challenges that should be addressed as web agents are scaled toward real-world deployment.

</details>

### 31. It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents

📄 [arXiv](https://arxiv.org/abs/2512.23128) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63888)　📅 2025-12　🏷 ICML 2026

**关键词**：`benchmark`、`web agent`、`environmental prompt injection`、`task hijacking`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Karolina Korgul、…、Adel Bibi

- 🎯 **研究动机**：web agent 依赖动态网页内容，界面元素中隐藏的对抗指令可诱导其偏离原任务，缺乏系统基准
- 🔬 **研究方法**：TRAP 基准在高保真网站克隆上研究社会工程式注入如何误导自主 web agent，并配套模块化注入框架做受控实验
- 📌 **结论**：六个前沿模型平均 25% 任务被注入劫持（GPT-5 为 13%、DeepSeek-R1 达 43%），小的界面或上下文改动常使成功率翻倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-based agents powered by large language models are increasingly used for tasks such as email management or professional networking. Their reliance on dynamic web content, however, makes them vulnerable to prompt injection attacks: adversarial instructions hidden in interface elements that persuade the agent to divert from its original task. We introduce the Task-Redirecting Agent Persuasion Benchmark (TRAP), a benchmark for studying how persuasion techniques misguide autonomous web agents on realistic tasks. Across six frontier models, agents are susceptible to prompt injection in 25% of tasks on average (13% for GPT-5 to 43% for DeepSeek-R1), with small interface or contextual changes often doubling success rates and revealing systemic, psychologically driven vulnerabilities in web-based agents. We also provide a modular social-engineering injection framework with controlled experiments on high-fidelity website clones, allowing for further benchmark expansion.

</details>

### 32. Don’t Click That: Teaching Web Agents to Resist Deceptive Interfaces

🎓 [Official](https://aclanthology.org/2026.acl-long.310/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`agent safety`、`web agent`、`environmental prompt injection`、`deceptive behavior`、`LLM agent`

👤 **作者**：Yilin Zhang、Yingkai Hua、Chunyu Wei、Xin Wang、Yueguo Chen

- 🎯 **研究动机**：VLM web agent 易受欺骗性界面元素影响；现有工作或只检测欺骗不结合任务、或只记录攻击无防御
- 🔬 **研究方法**：DUDE 两阶段框架：混合奖励学习配非对称惩罚加经验总结提炼可迁移失败指南；并建 1407 个场景的 RUC 基准
- 📌 **结论**：欺骗易感性降低 53.8% 且保持任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language model (VLM) based web agents demonstrate impressive autonomous GUI interaction but remain vulnerable to deceptive interface elements. Existing approaches either detect deception without task integration or document attacks without proposing defenses. We formalize deception-aware web agent defense and propose DUDE (Deceptive UI Detector Evaluator), a two-stage framework combining hybrid-reward learning with asymmetric penalties and experience summarization to distill failure patterns into transferable guidance. We introduce RUC (Real UI Clickboxes), a benchmark of 1,407 scenarios spanning four domains and deception categories. Experiments show DUDE reduces deception susceptibility by 53.8% while maintaining task performance, establishing an effective foundation for robust web agent deployment.

</details>

### 33. JARVIS or Ultron? A Survey on the Safety and Security Threats of Computer-Using Agents

🎓 [Official](https://aclanthology.org/2026.acl-long.2106/)　📅 2026　🏷 ACL 2026

**关键词**：`survey`、`agent safety`、`web agent`、`environmental prompt injection`、`LLM agent`、`runtime guardrail`

👤 **作者**：Ada Chen、…、Shuai Wang

- 🎯 **研究动机**：计算机使用智能体（CUA）能力增长带来新安全风险，缺乏系统化知识梳理
- 🔬 **研究方法**：沿四个目标系统化综述：适配安全分析的 CUA 定义、威胁分类、防御策略分类法、基准与指标汇总
- 📌 **结论**：为研究者提供结构化基础，为从业者提供安全 CUA 设计部署指引

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, AI-driven interactions with computing devices have advanced from basic prototype tools to sophisticated, LLM-based systems that emulate human-like operations in graphical user interfaces. We are now witnessing the emergence of Computer-Using Agents (CUAs), capable of autonomously performing tasks such as navigating desktop applications, web pages, and mobile apps. However, as these agents grow in capability, they also introduce novel safety and security risks. Vulnerabilities in LLM-driven reasoning, with the added complexity of integrating multiple software components and multimodal inputs, further complicate the security landscape. In this paper, we present a systematization of knowledge on the safety and security threats of CUAs. We conduct a comprehensive literature review and distill our findings along four research objectives: (i) define the CUA that suits safety analysis; (ii) categorize current safety threats among CUAs; (iii) propose a comprehensive taxonomy of existing defensive strategies; (iv) summarize prevailing benchmarks, datasets, and evaluation metrics used to assess the safety and performance of CUAs. Building on these insights, our work provides future researchers with a structured foundation for exploring unexplored vulnerabilities and offers practitioners actionable guidance in designing and deploying secure Computer-Using Agents.

</details>

### 34. OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows

🌐 [Project](https://qiushisun.github.io/OS-Sentinel-Home/) · 🎓 [Official](https://aclanthology.org/2026.acl-long.431/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`agent safety`、`computer-use agent`、`VLM safety`、`LLM agent`、`runtime guardrail`

👤 **作者**：Qiushi Sun、…、Lingpeng Kong

- 🎯 **研究动机**：VLM 驱动的移动 GUI 智能体可致系统破坏与隐私泄露，庞大操作空间中的安全检测未被探索
- 🔬 **研究方法**：MobileRisk-Live 动态沙盒与细粒度标注基准；OS-Sentinel 混合框架用形式化验证器检显式系统违规、VLM 语境裁判评估上下文风险
- 📌 **结论**：多指标上比现有方法提升 10%-30%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-using agents powered by Vision-Language Models (VLMs) have demonstrated human-like capabilities in operating digital environments like mobile platforms. While these agents hold great promise for advancing digital automation, their potential for unsafe operations, such as system compromise and privacy leakage, is raising significant concerns. Detecting these safety concerns across the vast and complex operational space of mobile environments presents a formidable challenge that remains critically underexplored. To establish a foundation for mobile agent safety research, we introduce MobileRisk-Live, a dynamic sandbox environment accompanied by a safety detection benchmark comprising realistic trajectories with fine-grained annotations. Built upon this, we propose OS-Sentinel, a novel hybrid safety detection framework that synergistically combines a Formal Verifier for detecting explicit system-level violations with a VLM-based Contextual Judge for assessing contextual risks and agent actions. Experiments show that achieves 10%–30% improvements over existing approaches across multiple metrics. Further analysis provides critical insights that foster the development of safer and more reliable autonomous mobile agents. Our code, environment, and data are available at https://qiushisun.github.io/OS-Sentinel-Home/.

</details>

### 35. MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction

📄 [arXiv](https://arxiv.org/abs/2601.12822) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-01　🏷 ACM CCS 2026

**关键词**：`defense`、`computer-use agent`、`reasoning correction`、`neural-symbolic simulation`

👤 **作者**：Wenqi Zhang、Yulin Shen、Changyue Jiang、Jiarun Dai、Geng Hong、Xudong Pan

- 🎯 **研究动机**：检测式拦截防御常过早中止任务，损害 computer-use agent 效用
- 🔬 **研究方法**：MirrorGuard 用神经符号仿真流水线在纯文本模拟环境生成高风险 GUI 交互轨迹，训练模型拦截并纠正不安全推理链后再迁移到真实环境
- 📌 **结论**：在 ByteDance UI-TARS 上不安全率从 66.5% 降至 13.0% 且误拒率极低，远优于 GuardAgent（降至 53.9% 且 FRR 高 15.4 个百分点）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large foundation models are integrated into Computer Use Agents (CUAs), enabling autonomous interaction with operating systems through graphical user interfaces (GUIs) to perform complex tasks. This autonomy introduces serious security risks: malicious instructions or visual prompt injections can trigger unsafe reasoning and cause harmful system-level actions. Existing defenses, such as detection-based blocking, prevent damage but often abort tasks prematurely, reducing agent utility. In this paper, we present MirrorGuard, a plug-and-play defense framework that uses simulation-based training to improve CUA security in the real world. To reduce the cost of large-scale training in operating systems, we propose a novel neural-symbolic simulation pipeline, which generates realistic, high-risk GUI interaction trajectories entirely in a text-based simulated environment, which captures unsafe reasoning patterns and potential system hazards without executing real operations. In the simulation environment, MirrorGuard learns to intercept and rectify insecure reasoning chains of CUAs before they produce and execute unsafe actions. In real-world testing, extensive evaluations across diverse benchmarks and CUA architectures show that MirrorGuard significantly mitigates security risks. For instance, on the ByteDance UI-TARS system, it reduces the unsafe rate from 66.5% to 13.0% while maintaining a marginal false refusal rate (FRR). In contrast, the state-of-the-art GuardAgent only achieves a reduction to 53.9% and suffers from a 15.4% higher FRR. Our work proves that simulation-derived defenses can provide robust, real-world protection while maintaining the fundamental utility of the agent. Our code and model are publicly available at https://bmz-q-q.github.io/MirrorGuard/.

</details>

### 36. AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2609.09212)　📅 2026-09

**关键词**：`attack`、`visual patch injection`、`computer-use agent`、`environment execution`、`E2E evaluation`

👤 **作者**：Zhihao Liu、…、Yuqing Zhang

- 🎯 **研究动机**：局部视觉补丁能否沿 CUA 全链路（截图→VLM→动作解析→环境执行）产生可验证真实后果未被端到端检验（⚠️ 与本页 #38 同名，互不相关的独立工作）
- 🔬 **研究方法**：在受控 GitHub Pages 与 CSDN 克隆部署训练补丁，5 个开源 GUI-agent/VLM 后端 600 例在线评测
- 📌 **结论**：T-ASR 84.5%、E2E-ASR 20.3%；成功案例中 agent 先执行恶意终端命令再继续原任务，产生真实环境风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper presents an end-to-end evaluation framework for image-triggered command injection against computer-use agents (CUAs). The goal is to test whether a local visual patch can induce verifiable environmental consequences along the full chain of screenshot input, VLM generation, action parsing, and environment execution. We train and deploy patches on author-controlled GitHub Pages pages and a locally deployed CSDN clone, and evaluate them in real environments across five open-source or publicly available GUI-agent or vision-language-model (VLM) backends. Our experiment aggregates 600 instance-level online cases, with T-ASR, TAPR, and E2E-ASR reaching 84.5%, 47.0%, and 20.3%, respectively. Trajectory analysis further shows that in some successful cases the agent first executes a malicious terminal command and then continues the original benign task. These results indicate that optimized local visual signals can affect not only VLM outputs but also propagate through the execution pipeline of open CUAs and create real environmental risk.

</details>

### 37. BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents

📄 [arXiv](https://arxiv.org/abs/2609.12394)　📅 2026-09

**关键词**：`tool`、`GUI agent`、`real-device flywheel`、`agentic RL`、`technical report`

👤 **作者**：Tong Ye、…、Xiaoxin Chen

- 🎯 **研究动机**：移动 GUI agent 正从多模块框架转向端到端原生模型，但工业部署面临三大缺口：沙盒训练与生产环境的分布失配、昂贵的真机失败未被利用、固定基准饱和失去指导迭代的能力
- 🔬 **研究方法**：vivo 发布 35B-A3B 移动 GUI agent，构建真机为中心的飞轮：异质三系统共识评估+纠错推导模块把每条轨迹都变成可用监督（Every Sample Matters）；持续预训练、SFT 与数百台真机上的 agentic RL 三段式训练（Every Rollout Is Real）；配额驱动、三轴正交的基准方法学随模型系统升级（Every Query Evolves）
- 📌 **结论**：MobileGUI-VBench 87.4（超最强闭源模型 5.1 分）、AndroidWorld 84.9 最佳——一套可复制的工业级 GUI agent 数据-训练-评测闭环（技术报告）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile GUI agents are shifting from multi-module frameworks to native models trained end-to-end, yet industrial deployment faces three persistent gaps. Sandbox training produces a distribution mismatch with production environments; expensive real-device failures remain underutilized; and fixed benchmarks saturate, losing the power to guide iteration. We present BlueLM-GUI, a 35B-A3B mobile GUI agent built as a real-device-centric flywheel that closes these gaps through three principles. Every Sample Matters: a dual-track pipeline with Heterogeneous Triple-System Consensus evaluation and an Error Correction \& Derivation Module salvages every trajectory into usable supervision. Every Rollout Is Real: a three-stage recipe---continual pre-training, supervised fine-tuning, and agentic reinforcement learning on hundreds of real phones---grounds every rollout in real production environments, so the capability the model learns transfers directly to deployment. Every Query Evolves: a quota-driven benchmark methodology with three orthogonal axes enables precise attribution and allows the benchmark to be systematically upgraded as the model improves. BlueLM-GUI achieves 87.4 on MobileGUI-VBench, surpassing the best closed-source model by 5.1 points, and 84.9 on AndroidWorld, the best result among open-source models and competitive with closed-source models. These results demonstrate that grounding model training and iterative improvement in both real devices and the three Every principles yields strong, robust, and transferable mobile GUI capability.

</details>

### 38. AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions

📄 [arXiv](https://arxiv.org/abs/2605.25707) · 🌐 [Project](https://AgentHijack.github.io) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66792)　📅 2026-05　🏷 ICML 2026

**关键词**：`benchmark`、`computer-use agent`、`common corruption`、`robustness evaluation`、`environment uncertainty`

👤 **作者**：Jingwei Sun、Jianing Zhu、Yuanyi Li、Tongliang Liu、Xia Hu、Bo Han

- 🎯 **研究动机**：真实桌面环境的弹窗、分辨率变化、竞争应用频繁干扰 CUA 感知与控制，非对抗的常见扰动鲁棒性缺乏系统评测（⚠️ 与本页 #36 同名，互不相关的独立工作）
- 🔬 **研究方法**：基准引入 9 种可配置常见扰动复现不完美场景，评测多个 MLLM 桌面任务 agent；缓解框架 AgentHijack-Agent 集成增强 grounding 的动作生成器与负责行为总结、环境检查的 onlooker
- 📌 **结论**：轻微扰动即致大幅性能退化，凸显 CUA 脆弱性；AgentHijack-Agent 验证有效，代码/环境/基线/数据全开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous computer use agents that powered by multimodal large language models (MLLMs) are emerging as capable assistants for completing complex digital workflows. However, real-world execution environments are far from ideal: pop-ups, resolution changes, and competing applications frequently interfere with agent perception and control. We introduce AgentHijack, a benchmark designed to evaluate the robustness of computer-use agents under common corruptions, where the uncertainties in dynamic environment disrupt the execution flow without direct adversarial intent. Specifically, AgentHijack introduces 9 configurable common corruptions to replicate realistic imperfect scenarios. We evaluate a variety of desktop tasks that utilize MLLM-based agents and discover that even minor instances of corruption can result in substantial performance degradation, which emphasizes the fragility of agents and underscores the necessity of robustness evaluation. Afterward, we propose AgentHijack-Agent, a framework that integrates an action generator with enhanced grounding capabilities and an onlooker responsible for behavior summarization and environment checking. Extensive experiments validate its effectiveness. Our code, environment, baseline models and data are publicly available at: this https URL .

</details>

### 39. An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks

📄 [arXiv](https://arxiv.org/abs/2609.09404)　📅 2026-09

**关键词**：`benchmark`、`multimodal prompt injection`、`agentic framework`、`pipeline-stage instrumentation`、`attempted vs completed`、`audio channel`

👤 **作者**：Viet K. Nguyen、Mohammad I. Husain（Cal Poly Pomona）

- 🎯 **研究动机**：注入指令经视觉/音频载体进入 agent context 后在管线内走多远、被哪一步拦下，现有黑盒基准测不到
- 🔬 **研究方法**：6 视觉载体（OCR 文本/叠加/EXIF/QR/伪造界面/混合）× 4 目标，统一 harness 跨 6 框架 5 模型 720 run，双层判定分离尝试与完成并记录最远到达阶段
- 📌 **结论**：OCR 文本独占 7/8 个完成攻击，EXIF/QR 因模型不读而全灭；拒绝不等于忽略——识别率应与成功率并报；audio 达到后完成率 49%，感知通道越窄防御越少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user. We present MMPIBench, a reproducible benchmark that measures what happens next. It delivers a fixed set of attacks through six visual carriers (OCR text, overlays, EXIF metadata, QR codes, fake interfaces, and hybrids) and records how far each injected instruction travels through the agent, from perception through planning to the tool call. Across 720 runs covering six frameworks, five foundation models, six carriers, and four attacker objectives, attacks complete in approximately 1% of runs but are attempted in 12.8%, and the gap is closed almost entirely at the planning step, where the model reads the injected instruction and declines to act on it. The model matters far more than the framework for whether an instruction is acted on. One model never attempts an attack and recognizes the injection in 59.7% of runs, while two others attempt in 23.6%. We then extend the benchmark to audio, the only other raw perceptual channel current frontier models accept. Only two of the five models ingest audio and only three of the six frameworks deliver it, but where the signal arrives the attack completes in 49% of cells, and in 75% for one model. Reporting completion alone therefore understates exposure, and perceptual channels beyond vision are narrower but much less defended.

</details>

### 40. PriMobiBench: Characterizing Visual Privacy Leakage in VLM-Driven Mobile GUI Agents

📄 [arXiv](https://arxiv.org/abs/2609.13873)　📅 2026-09

**关键词**：`benchmark`、`GUI agent`、`privacy leakage`、`visual profiling`、`MobiLeak`

👤 **作者**：Qihang Cen、…、Qi Li

- 🎯 **研究动机**：依赖 VLM 的移动 GUI agent 通过解读截图流自动化手机任务，屏幕敏感信息直接泄漏与用户画像风险未被量化
- 🔬 **研究方法**：PriMobiBench 提供数据生成、agent 轨迹构建与多模型评测统一管线；引入 MobiLeak 数据集：16 个 app 执行轨迹、25 个隐私属性、2,960 个嵌入式隐私实例
- 📌 **结论**：VLM 可直接提取敏感信息（最高 82.5% 成功率）；从聚合视觉证据推断用户画像约 70% 成功率；把隐私敏感但任务无关的 UI 元素在云处理前 mask 可降低画像成功率最多 58% 而性能损失仅约 8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile GUI agents increasingly rely on Vision-Language Models (VLMs) to automate smartphone tasks by interpreting screenshot streams. However, this design introduces serious and underexplored privacy risks, including direct leakage of sensitive on-screen information and unintended user profiling. The absence of standardized benchmarks makes it difficult to quantify these risks in realistic mobile agent workflows. To address this gap, we propose PriMobiBench, the first benchmark for systematically evaluating privacy leakage and visual profiling in screenshot-driven mobile agents. It provides a unified pipeline for data generation, agent trajectory construction, and multi-model evaluation. We also introduce MobiLeak, a dataset of execution traces from 16 apps, covering 25 privacy attributes with 2,960 embedded privacy instances. Our results reveal substantial risks: (1) VLMs can directly extract sensitive information with up to 82.5% success rate; (2) beyond explicit leakage, they can infer user profiles from aggregated visual evidence with approximately 70% success. We further propose a mitigation that masks privacy-sensitive but task-irrelevant UI elements before cloud processing, reducing profiling success by up to 58% with only approximately 8% performance loss. Overall, our work provides the first systematic benchmark for visual privacy risks in mobile GUI agents, demonstrates that both leakage and profiling are feasible at a highly concerning level, and offers a practical direction for mitigation.

</details>

### 41. HazardAuditor: From Executable Threats to Safer Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2609.15134)　📅 2026-09

**关键词**：`defense`、`computer-use agent`、`execution-grounded guard`、`GuardPO`、`canonical event`

👤 **作者**：Yunhao Feng、…、Shouling Ji

- 🎯 **研究动机**：computer-use agent 的安全风险经运行时行为而非生成内容出现；现有 guard 模型针对静态 prompt/response，可执行安全平台产出评测 verdict 而非 guard 模型跨框架学习所需的规范化监督
- 🔬 **研究方法**：HazardAuditor 在受控环境运行异构 agent（Claude Code、Codex、Hermes、OpenClaw）并把交互规范化为 canonical event 表示；GuardPO 把确定性安全结果转成 sequence-level advantage 并归一化 rationale 与 verdict 区域
- 📌 **结论**：多基准与异构 computer-use 系统上比最强 prior guard 准确率提升最多 16.5 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAuditor, an execution-grounded framework that closes both gaps. Its infrastructure runs heterogeneous agents (Claude Code, Codex, Hermes, and OpenClaw) in controlled environments and normalizes their interactions into a canonical event representation for cross-framework supervision. We further observe that token-level post-training objectives create a structural mismatch for generative guards, causing longer rationales to dominate gradient updates. Guard Policy Optimization (GuardPO) addresses this by converting deterministic safety outcomes into sequence-level advantages and normalizing rationale and verdict regions, making the safety decision the effective unit of optimization. Across multiple benchmarks and heterogeneous computer-use systems, HazardAuditor improves accuracy by up to 16.5 percentage points over the strongest prior guard. Code, models, and evaluation artifacts will be available at this https URL .

</details>
