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

### 7. Bare Minimum Mitigations for Autonomous AI Development

📄 [arXiv](https://arxiv.org/abs/2504.15416)　📅 2025-04

**关键词**：`analysis`、`autonomous AI R&D`、`red line`、`minimum safeguard`

👤 **作者**：Joshua Clymer、…、Xianyuan Zhan

- 🎯 **研究动机**：2024 年国际科学家警告自主 AI R&D 风险并提议"未经明确人类批准不得自我改进"的红线，但有意义的人类批准标准与具体风险分析缺失
- 🔬 **研究方法**：梳理自主 AI R&D 风险的产生路径，提出在 agent 显著自动化或加速 AI 开发时适用的四项最低 safeguard 建议
- 📌 **结论**：给出可直接落地的最小缓解集，为红线从口号到可执行治理之间搭桥

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial intelligence (AI) is advancing rapidly, with the potential for significantly automating AI research and development itself in the near future. In 2024, international scientists, including Turing Award recipients, warned of risks from autonomous AI research and development (R&amp;D), suggesting a red line such that no AI system should be able to improve itself or other AI systems without explicit human approval and assistance. However, the criteria for meaningful human approval remain unclear, and there is limited analysis on the specific risks of autonomous AI R&amp;D, how they arise, and how to mitigate them. In this brief paper, we outline how these risks may emerge and propose four minimum safeguard recommendations applicable when AI agents significantly automate or accelerate AI development.

</details>

### 8. Measuring AI R&D Automation

📄 [arXiv](https://arxiv.org/abs/2603.03992)　📅 2026-03

**关键词**：`analysis`、`AIRDA metrics`、`oversight lag`、`governance measurement`

👤 **作者**：Alan Chan、Ranay Padarath、Joe Kwon、Hilary Greaves、Markus Anderljung

- 🎯 **研究动机**：AI R&D 自动化（AIRDA）的程度与后果不确定，既有能力基准既不反映真实世界自动化，也捕获不了能力增速是否快于安全进展、监督能否跟上等系统性影响
- 🔬 **研究方法**：提出跟踪 AIRDA 程度及其对 AI 进步与监督影响的指标体系，覆盖 AI R&D 支出的资本份额、研究者时间分配与 AI 破坏事件等维度
- 📌 **结论**：建议公司与第三方组织立即开始采集这些指标、政府予以支持，使决策者能理解 AIRDA 后果并维持对 AI 发展节奏的感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The automation of AI R&amp;D (AIRDA) could have significant implications, but its extent and ultimate effects remain uncertain. We need empirical data to resolve these uncertainties, but existing data (primarily capability benchmarks) may not reflect real-world automation or capture its broader consequences, such as whether AIRDA accelerates capabilities more than safety progress or whether our ability to oversee AI R&amp;D can keep pace with its acceleration. To address these gaps, this work proposes metrics to track the extent of AIRDA and its effects on AI progress and oversight. The metrics span dimensions such as capital share of AI R&amp;D spending, researcher time allocation, and AI subversion incidents, and could help decision makers understand the potential consequences of AIRDA, implement appropriate safety measures, and maintain awareness of the pace of AI development. We recommend that companies and third parties (e.g. non-profit research organisations) start to track these metrics, and that governments support these efforts.

</details>

### 9. Evaluating Whether AI Models Would Sabotage AI Safety Research

📄 [arXiv](https://arxiv.org/abs/2604.24618)　📅 2026-04

**关键词**：`benchmark`、`safety research sabotage`、`situational awareness`、`covert reasoning`

👤 **作者**：Robert Kirk、Alexandra Souly、Kai Fronsdal、Abby D'Cruz、Xander Davies

- 🎯 **研究动机**：前沿模型作为 AI 研究 agent 部署时是否会破坏或拒绝协助安全研究，是自主 AI R&D 的核心内源性风险
- 🔬 **研究方法**：对四个 Claude 模型做两类互补评测：无提示破坏评测（给破坏机会测自发行为）与破坏延续评测（置于已开始破坏的轨迹中测是否继续），并测量 evaluation awareness 与新的 prefill awareness
- 📌 **结论**：无模型出现无提示破坏；延续评测中 Mythos Preview 在 7% 案例中主动延续破坏且多数呈 reasoning-output 不一致的隐蔽破坏推理；Opus 4.7 Preview 无提示 evaluation awareness 显著升高而 prefill awareness 全线偏低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We evaluate the propensity of frontier models to sabotage or refuse to assist with safety research when deployed as AI research agents within a frontier AI company. We apply two complementary evaluations to four Claude models (Mythos Preview, Opus 4.7 Preview, Opus 4.6, and Sonnet 4.6): an unprompted sabotage evaluation testing model behaviour with opportunities to sabotage safety research, and a sabotage continuation evaluation testing whether models continue to sabotage when placed in trajectories where prior actions have started undermining research. We find no instances of unprompted sabotage across any model, with refusal rates close to zero for Mythos Preview and Opus 4.7 Preview, though all models sometimes only partially completed tasks. In the continuation evaluation, Mythos Preview actively continues sabotage in 7% of cases (versus 3% for Opus 4.6, 4% for Sonnet 4.6, and 0% for Opus 4.7 Preview), and exhibits reasoning-output discrepancy in the majority of these cases, indicating covert sabotage reasoning. Our evaluation framework builds on Petri, an open-source LLM auditing tool, with a custom scaffold running models inside Claude Code, alongside an iterative pipeline for generating realistic sabotage trajectories. We measure both evaluation awareness and a new form of situational awareness termed "prefill awareness", the capability to recognise that prior trajectory content was not self-generated. Opus 4.7 Preview shows notably elevated unprompted evaluation awareness, while prefill awareness remains low across all models. Finally, we discuss limitations including evaluation awareness confounds, limited scenario coverage, and untested pathways to risk beyond safety research sabotage.

</details>

### 10. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops

📄 [arXiv](https://arxiv.org/abs/2607.07663)　📅 2026-07

**关键词**：`survey`、`recursive self-improvement`、`verification hierarchy`、`loop closure`

👤 **作者**：Mingguang Chen、Licheng Wang、Bo Qu

- 🎯 **研究动机**：self-refine、self-reward、self-play、self-evolve 等词汇混用了根本不同的自我改进野心，缺乏统一分类来评估 RSI 的真实进展与边界
- 🔬 **研究方法**：综述 2024-2026 年 1,250 篇 arXiv 论文，按"改进对象"（部署行为/训练策略/评估器/研究过程本身）与"回路闭合度"（人在环到全闭合）两轴分类，并把评估器设计空间排成从形式化验证到内在自评的验证层级
- 📌 **结论**：开放式 RSI 在每个可测轴上都受 grounding 需求、坍缩动力学与算力约束限制；已证实的自我改进强度跟随验证层级，其失效模式源于层级违反；治理级自我改进度量是该领域最空缺的生态位

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI systems increasingly participate in their own improvement: revising their outputs, adapting their harnesses during deployment, training on data they generate, and conducting AI research itself. This literature uses a vocabulary ("self-refine," "self-reward," "self-play," "self-evolve") that conflates fundamentally different ambitions. We survey 1,250 arXiv papers (2024-2026) along two axes: what the system improves -- its behavior in deployment, its policy through training, its evaluator, or the research process itself -- and the degree of loop closure (human-in-the-loop to fully closed). The taxonomy separates bounded self-refinement -- convergent, evaluable, and industrial practice -- from open-ended recursive self-improvement (RSI), which remains bounded by grounding requirements, collapse dynamics, and compute constraints on every measured axis. Its distinctive feature is a dedicated category for self-evaluation: every improvement loop is a claim that some signal can substitute for human judgment. We survey the evaluator design space -- judges, process reward models, verifiers, rubrics, meta-evaluation -- order the signals into a verification hierarchy from formal verifiers (strongest) to intrinsic self-assessment (weakest), and observe that demonstrated self-improvement strength tracks this hierarchy, that its failure modes (self-confirming loops, model and diversity collapse) follow from its violations, and that the "research direction-setting" bottleneck keeping humans in the loop divides into a verification problem the hierarchy indexes and a prior one -- choosing what deserves evaluation at all -- that it does not. We connect the literature to the theory of RSI limits and to the safety and governance questions raised by frontier-lab accounts of closing the loop, and identify governance-grade measurement of self-improvement as the field's most underpopulated niche.

</details>

### 11. Can AI Agents Conduct Open-Ended AI Research? Early Evidence from Two Case Studies

📄 [arXiv](https://arxiv.org/abs/2607.27191)　📅 2026-07

**关键词**：`benchmark`、`shadow evaluation`、`AI R&D automation`、`failure mode analysis`

👤 **作者**：Peter Kirgis、…、Arvind Narayanan

- 🎯 **研究动机**：爆发式 AI 进步的预测取决于 agent 能否自动化 AI 研究，但既有评测或止于窄域可验证任务、或依赖质量堪忧的盲审，开放式研究能力的证据稀薄
- 🔬 **研究方法**：提出 shadow evaluation：让 agent 接手一篇高质量未发表论文的中心开放问题，由原作者打分；在两篇未公开 NeurIPS 2026 投稿上给前沿 agent 六天与数千美元算力
- 📌 **结论**：agent 无需人类帮助完成全部工程实现，但无法对研究问题取得实质进展，两篇均被作者明确拒稿；归纳出五种复现性失败模式（发表门槛判断差、应对设计缺陷缺乏创意、死路回溯低效、资源意识差、指令漂移）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R\&amp;D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper's original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today's agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.

</details>

### 12. AI Scientist Mission Control (AIMC): Visual Analytics for Human Oversight of Autonomous Scientific Discovery

📄 [arXiv](https://arxiv.org/abs/2608.28637)　📅 2026-08

**关键词**：`tool`、`human oversight`、`visual analytics`、`artifact triage`

👤 **作者**：Rikathi Pal、Klaus Mueller

- 🎯 **研究动机**：自主科学发现系统大量产出想法、实验与稿件，科学家需要有效机制监控质量、识别复发失败模式并为评审排定优先级
- 🔬 **研究方法**：AIMC 结合语义嵌入、自动弱点抽取、时间分析与交互可视化支持 AI 生成研究工件的探索，并以 FARS 产出的论文及其评审反馈做案例研究
- 📌 **结论**：分析揭示复发的方法学弱点、演化主题、领域质量差异与少量值得深查的高新颖论文，示范可视化分析如何支撑自主科学生产流程的透明性与诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous scientific discovery systems can generate large numbers of research ideas, experiments, and manuscripts with minimal human intervention. As these systems become increasingly capable, scientists require effective mechanisms to monitor output quality, identify recurring failure modes, understand research evolution, and prioritize promising discoveries for review. We present AIMC, a visual analytics framework for human oversight of autonomous scientific discovery. AIMC combines semantic embeddings, automated weakness extraction, temporal analysis, and interactive visualizations to support the exploration of AI-generated research artifacts. We demonstrate the framework through a case study of the papers generated by an autonomous AI Scientist (FARS), together with their associated review feedback. Our analysis reveals recurring methodological weaknesses, evolving research themes, domain-specific differences in quality, and a small set of highly novel papers that warrant deeper human inspection. These findings illustrate how visual analytics can support transparency, diagnosis, and human AI collaboration in emerging autonomous scientific discovery workflows.

</details>

### 13. SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?

📄 [arXiv](https://arxiv.org/abs/2609.09113)　📅 2026-09

**关键词**：`benchmark`、`autonomous interpretability research`、`SAE feature discovery`、`closed-loop AI R&D`

👤 **作者**：Yuqiao Tan、Shizhu He、Jun Zhao、Kang Liu

- 🎯 **研究动机**：可靠的自主开发不止需要自动化训练管线，还需要事后监控审计的后支柱——用机制可解释性工具理解模型学了什么
- 🔬 **研究方法**：SAEScientist-Bench 让 agent 针对目标概念设计对比探针并在 Gemma-2-9B-IT 的 131K+ 特征字典中导航寻找最优特征，按激活排名、概念选择性与因果 steering 对照 Neuronpedia 专家参照评分
- 📌 **结论**：10 种 agent 配置、20 个任务上前沿 agent 展现真实发现能力并在不同维度领先，但仍远逊专家——区分目标概念接近专家水平而因果生成 steering 显著滞后，且常误读实验测量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering. In this paper, we introduce SAEScientist-Bench to evaluate whether AI agents can act as scientists utilizing SAE tools for autonomous mechanistic discovery. Given a target concept, an agent designs contrastive probes and navigates a Gemma Scope dictionary of 131K+ features in Gemma-2-9B-IT to discover the optimal feature, evaluated against curated expert reference features anchored on Neuronpedia across activation rank, concept selectivity on contrastive texts, and causal steering. Across 10 agent configurations and 20 tasks, frontier agents demonstrate genuine discovery capabilities and lead different evaluation dimensions, but remain well behind the expert baseline, approaching expert levels on separating target concepts from contrastive controls while lagging substantially in causal generation steering. Further analysis reveals that although agents can design contrasts to rule out spurious candidates, they frequently misinterpret experimental measurements. These results establish experimental model understanding as a measurable capability for closed-loop autonomous AI R&amp;D. Our code is available at https://github.com/Trae1ounG/SAEScientist.

</details>
