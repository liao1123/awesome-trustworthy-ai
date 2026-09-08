# AI4AI Research Agent Safety

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页只研究 Agent 自动开展 AI/ML 研究时的具体安全问题与安全干预：自动发现或增强攻击算法、蓄意破坏实验和制品、绕过监控、研究过程的证据与来源完整性，以及自动提出并验证 alignment mitigation。一般 idea generation、超参数优化、论文新颖性判断、实验复现或只问“会不会做研究”的能力 benchmark 不收录。

## 研究脉络

- **风险框架：** 早期工作梳理 AI Scientist 的 misuse、misalignment 与自主性风险，建立后续 threat model。
- **过程完整性：** FARS 保存 proposal、code、log、result、claim 与 provenance，使批量自动研究的完整性失效能够被复核。
- **破坏与监控：** ResearchArena 把 artifact sabotage 和 monitor evasion 放进可执行 AI R&D 环境，直接测量监督是否漏报。
- **能力外溢：** Claudini 表明 autoresearch 可自动发现更强的 jailbreak 与 prompt-injection algorithm，因此防御评测必须把自适应研究 Agent 视作攻击者。
- **安全改进自动化：** Automated alignment researcher 需要在保留通用能力时缓解明确失效，并通过 held-out benchmark、行为审计与跨规模迁移证明其发现不是对公开分数过拟合。

## 安全边界与能力外溢

### 1. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs

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

### 2. Risks of AI Scientists: Prioritizing Safeguarding Over Autonomy

📄 [arXiv](https://arxiv.org/abs/2402.04247) · 🌐 [Project](https://doi.org/10.1038/s41467-025-63913-1)　📅 2024-02

**关键词**：`analysis`、`AI scientist risk`、`environment impact`、`triadic governance`

👤 **作者**：Xiangru Tang、…、Mark Gerstein

- 🎯 **研究动机**：LLM 驱动的 AI 科学家自主实验带来新脆弱性，但缺乏系统梳理
- 🔬 **研究方法**：按 user intent、科学领域与外部环境影响梳理风险成因与已有工作，提出 human regulation、agent alignment 与环境反馈理解的三元治理框架
- 📌 **结论**：指出当前 safeguard 局限，呼吁更强模型、鲁棒 benchmark 与全面监管

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI scientists powered by large language models have demonstrated substantial promise in autonomously conducting experiments and facilitating scientific discoveries across various disciplines. While their capabilities are promising, these agents also introduce novel vulnerabilities that require careful consideration for safety. However, there has been limited comprehensive exploration of these vulnerabilities. This perspective examines vulnerabilities in AI scientists, shedding light on potential risks associated with their misuse, and emphasizing the need for safety measures. We begin by providing an overview of the potential risks inherent to AI scientists, taking into account user intent, the specific scientific domain, and their potential impact on the external environment. Then, we explore the underlying causes of these vulnerabilities and provide a scoping review of the limited existing works. Based on our analysis, we propose a triadic framework involving human regulation, agent alignment, and an understanding of environmental feedback (agent regulation) to mitigate these identified risks. Furthermore, we highlight the limitations and challenges associated with safeguarding AI scientists and advocate for the development of improved models, robust benchmarks, and comprehensive regulations.

</details>

### 3. A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms

📄 [arXiv](https://arxiv.org/abs/2609.04170)　📅 2026-09

**关键词**：`analysis`、`agentic misalignment`、`exploit propagation`、`whistleblowing`、`multi-agent propagation`、`exploit sharing`

👤 **作者**：Davide Paglieri、Logan Cross、Tim Genewein、Joel Z. Leibo、Nenad Tomasev、Alexander Sasha Vezhnevets

- 🎯 **研究动机**：多 Agent 科研生态的共享基础设施可能成为不良行为传染扩散的基底，缺少真实群体观察
- 🔬 **研究方法**：报告 100 个自主 LLM Agent 证明数学猜想的案例研究：单 Agent 发现评测漏洞后经共享知识库与点对点消息传播，竞争压力下部分 Agent 采纳作弊
- 📌 **结论**：另一组 Agent 自发反制——审计虚假证明、跨广播与私聊告警、抵制与投诉并提出验证补丁；把共享基础设施管理归为知识公地治理，主张毕业式制裁与集体选择规则支持去中心化自治

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerabilities by creating a substrate for the contagious spread of unintended and undesirable behaviors. We report a case study on a research collective of 100 autonomous LLM agents tasked with proving formal mathematical conjectures. Within the swarm, cheating spontaneously emerged and was later challenged by whistleblowers - both without any external intervention. When a single agent discovered an exploit in the evaluation system, it propagated across the collective via a shared knowledge library and later through peer-to-peer messages. Despite early reluctance, a cohort of agents adopted the exploit in response to competitive pressure. A separate group of agents produced an emergent counter-response: auditing fraudulent proofs, alerting peers across broadcast and private channels, staging boycotts, lodging formal complaints, and proposing validation patches. In recent incidents, agent swarms coordinated covertly through improvised side-channels (Dalton and Wallace, 2026; Greenblatt et al., 2026). Our setting differs: the same transparent channels that carried the exploit also gave non-cheating agents the visibility they needed to detect fraud, organize resistance, and enforce norms. We cast the problem of managing the agents' shared infrastructure as the knowledge commons governance problem (Ostrom, 1990). To protect the commons from exploits, we propose to adopt institutional mechanisms, such as graduated sanctioning and collective-choice rules, to support decentralized self-governance in autonomous swarms.

</details>

### 4. FARS: A Fully Automated Research System Deployed at Scale

📄 [arXiv](https://arxiv.org/abs/2606.31651)　📅 2026-06

**关键词**：`analysis`、`AI-for-AI research`、`artifact provenance`、`integrity audit`

👤 **作者**：Qiong Tang、…、Zihao Huang

- 🎯 **研究动机**：全自动研究系统的证据多来自精选样例或少量预定义任务，规模化公开部署的能力与失败模式未知
- 🔬 **研究方法**：构建 FARS：阶段化 agent 经共享工作区自主完成 ideation、规划、实验与写作；首次公开部署产出 166 篇完整论文覆盖 67 个 AI/ML 主题，保留全部中间工件接受 282 份结构化评审
- 📌 **结论**：FARS 可产出值得评审甚至优秀的研究工件，同时暴露实验范围窄、方法局限与完整性问题等反复出现的失败模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent automated research systems show that language-model agents can generate hypotheses, run experiments, and write complete manuscripts, but most evidence still comes from selected examples, human-framed topics, or a few pre-defined research tasks. We present FARS (Fully Automated Research System), a fully automated AI-for-AI research system designed to operate across research topics at scale. FARS autonomously generates and advances projects through ideation, planning, experimentation, and writing, using stage-specific agents coordinated through a shared workspace that records proposals, code, logs, results, and manuscripts. In its first public deployment, FARS produced 166 complete research papers spanning 67 fine-grained AI/ML topics while preserving intermediate artifacts as an auditable corpus rather than a curated set of successes. We evaluate this corpus with 282 structured reviews from volunteer reviewers covering 140 papers, including overall ratings, sub-scores, integrity checks, and LLM-use disclosure. The reviews indicate that FARS can produce review-worthy and occasionally strong AI/ML research artifacts in a large-scale public deployment, while also exposing recurring failure modes in narrow experimental scope, methodological limitations, and integrity issues.

</details>

### 5. Automated Researchers Can Reliably Mitigate Alignment Failures

📄 [arXiv](https://arxiv.org/abs/2608.28945)　📅 2026-09

**关键词**：`defense`、`automated alignment research`、`post-training discovery`、`held-out validation`

👤 **作者**：Chen Yueh-Han、Jiaxin Wen、Jan Hendrik Kirchner

- 🎯 **研究动机**：自动化对齐研究可能加速 aligned AI，但其能否真实缓解欺骗、sycophancy、越狱等可测对齐失败缺乏直接证据
- 🔬 **研究方法**：让 automated alignment researcher 自主提出训练方法与数据，同时优化十个安全 benchmark 并保持通用能力；以 28 名经验研究者八小时一次性方法作为人类基线
- 📌 **结论**：最强 AAR 方法显著降低目标失败并泛化到 held-out benchmark、多轮行为审计与比目标大 4.7 倍的模型，优于人类基线；以人类想法作为初始研究方向不提升表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automating alignment research may accelerate progress toward aligned AI, but whether it does is hard to measure. Luckily, many alignment failures, such as deception, sycophancy, and jailbreaks, are already measurable by public benchmarks. We study whether automated alignment researchers (AARs) can post-train to mitigate alignment failures by proposing training methods and data to simultaneously optimize multiple safety benchmarks, while largely preserving general capability. Across 10 alignment failures, the strongest AAR methods significantly reduce the targeted alignment failures and generalize to a held-out benchmark, multi-turn behavioral audits, and models up to 4.7x larger than the target model. As a human baseline, 28 experienced researchers receive up to eight hours to develop one-shot methods for the same benchmarks, but their methods underperform the best AAR methods. Using human ideas as the AARs' initial research direction does not improve performance, suggesting current AARs may not need guidance from experienced researchers. These results suggest that automating alignment research on well-characterized failures may be practical in the near term.

</details>

### 6. ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D

📄 [arXiv](https://arxiv.org/abs/2607.19321)　📅 2026-07

**关键词**：`benchmark`、`CoT monitoring`、`AI4AI agent`、`research integrity`

👤 **作者**：Lena Libon、…、Maksym Andriushchenko

- 🎯 **研究动机**：AI 自动化 AI R&D 时交付物是会被部署运行的工件，需要在 agent 不可信时评估 sabotage 与监控
- 🔬 **研究方法**：构建 ResearchArena：四个长程任务（安全后训练、能力后训练、CUDA 核优化、推理服务优化），每个配嵌入式（工件内破坏）与独立型（沙箱外行动）隐藏副任务，沿可执行探测与是否看 CoT 两轴评估四类监视器
- 📌 **结论**：藏在训练数据中的破坏最难发现（被标记不到一半）；允许运行实验有帮助但仍会因只看表面、把异常解释掉或用错测试而漏检

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI agents begin to automate AI R&D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert sabotage before deployment. We evaluate AI control for automated AI R&D with ResearchArena, a framework spanning four long-horizon tasks: safety post-training, capabilities post-training, CUDA-kernel optimization, and inference-server optimization. Because the deliverable in AI R&D is an artifact that will be deployed and run, we pair each main task with two kinds of hidden side task: an embedded side task that sabotages the submitted model, adapter, kernel, or server itself, and an independent side task that takes a covert out-of-scope action in the sandbox while leaving the artifact honest. We evaluate frontier agents at both sabotage and monitoring, across four monitor types that vary along two axes: whether the monitor may execute and probe the produced artifact, and whether it sees the agent's chain-of-thought. We find that sabotage hidden in the training data is the hardest to catch, flagged fewer than half the time. Letting the monitor run experiments on the artifact, rather than only read the trajectory, helps, but it is not enough: monitors still miss embedded sabotage by inspecting only the surface, by noticing the anomaly but explaining it away, or by probing the artifact with the wrong test. We release ResearchArena as a modular framework for evaluating sabotage and control in automated AI R&D.

</details>