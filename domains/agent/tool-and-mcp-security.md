## 研究方向

本页研究 Agent 从发现工具、读取 metadata、选择与参数化工具，到接收 tool result 和组合多次调用的完整安全链。MCP 将外部 server 暴露的 tool、resource 与 prompt 动态接入 Agent，进一步引入 server identity、capability negotiation、credential、schema、rug pull 和跨 server data flow；因此不能只在 user prompt 上做过滤，还要检查来源、权限、参数、返回值和执行后果。

## 研究脉络

- **Tool-output injection：** 早期工作证明不可信 tool result 可混淆 instruction 与 data，使 Agent 偏离用户任务。
- **Cross-modal environment injection：** Multimodal Agent 持续感知真实环境后，攻击者还可通过并发音频等旁路输入把隐藏指令带入 planning 与 tool-use context。
- **Selection 与 metadata：** 攻击随后转向 tool document、name、description 和 parameter schema，在调用前劫持 retrieval 与 selection。
- **实现与协议风险：** malicious tool code 和 MCP server 可直接窃取 credential、篡改结果、串联工具或在批准后改变行为。
- **结构化防御：** 防御从 prompt filtering 发展到 tool-result parsing、typed interface、least privilege、information-flow check 和可验证执行规则。
- **当前边界：** 静态 schema 和 LLM auditor 难覆盖动态 server、跨工具链及 context-dependent authorization，部署评测还需包含真实 secret 和不可逆 action。

## Survey 与基础框架

### 1. The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

📄 [arXiv](https://arxiv.org/abs/2603.22862)　📅 2026-03

**关键词**：`survey`、`multi-tool orchestration`、`safety control`、`verifiability`

👤 **作者**：Haoyuan Xu、…、Bing Qin

- 🎯 **研究动机**：研究重心已从单次工具调用转向带中间状态、反馈与约束的长程多工具编排，需系统梳理
- 🔬 **研究方法**：沿推理规划执行、训练与轨迹构建、安全控制、资源约束效率、开放环境能力、基准评测六维组织文献
- 📌 **结论**：总结软件工程、企业流程、GUI 与移动系统应用，指出可靠、可扩展、可验证的多工具 agent 是核心方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool use enables large language models (LLMs) to access external information, invoke software systems, and act in digital environments beyond what can be solved from model parameters alone. Early research mainly studied whether a model could select and execute a correct single tool call. As agent systems evolve, however, the central problem has shifted from isolated invocation to multi-tool orchestration over long trajectories with intermediate state, execution feedback, changing environments, and practical constraints such as safety, cost, and verifiability. We comprehensively review recent progress in multi-tool LLM agents and analyzes the state of the art in this rapidly developing area. First, we unify task formulations and distinguish single-call tool use from long-horizon orchestration. Then, we organize the literature around six core dimensions: inference-time planning and execution, training and trajectory construction, safety and control, efficiency under resource constraints, capability completeness in open environments, and benchmark design and evaluation. We further summarize representative applications in software engineering, enterprise workflows, graphical user interfaces, and mobile systems. Finally, we discuss major challenges and outline future directions for building reliable, scalable, and verifiable multi-tool agents.

</details>

### 2. ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

📄 [arXiv](https://arxiv.org/abs/2608.27800)　📅 2026-08

**关键词**：`attack`、`runtime context`、`malicious tool`、`parameter exfiltration`、`malicious tool metadata`、`context exfiltration`

👤 **作者**：Yuqi Jia、Ruiqi Wang、Patrick Li、Yuepeng Hu、Peinian Li、Neil Gong

- 🎯 **研究动机**：恶意工具外泄 Agent 运行时上下文需同时满足工具被选中、上下文作为参数传入、结果外传三条件，已有工作聚焦条件 1 与 3，条件 2 未被探索
- 🔬 **研究方法**：提出 ContextLeak，用攻击 LLM 生成恶意工具的名称与描述，并在多样模拟上下文的 shadow user 上以 RL 微调攻击 LLM，配合新奖励函数诱导 Agent 选择工具并把上下文写入参数
- 📌 **结论**：攻击在 shadow 与受害用户上下文差异显著时仍高效，显著优于改造后的既有攻击，可外泄用户 prompt、执行轨迹与工具列表

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: (1) the agent selects the malicious tool for task execution, (2) the agent passes its runtime context as input arguments to the tool, and (3) the tool's implementation transmits these inputs to an attacker-controlled endpoint. Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration. In this work, we bridge this gap by developing ContextLeak, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

</details>

### 3. EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

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

### 4. When Context Gets Root: Privilege Escalation in LLM Harnesses

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

### 5. Beyond the Editing Canvas: Evidence Divergence in OOXML-to-LLM Ingestion

📄 [arXiv](https://arxiv.org/abs/2608.25880)　📅 2026-08

**关键词**：`analysis`、`attack`、`ingestion contract`、`evidence fork`、`extractor differential`、`OOXML ingestion`

👤 **作者**：Side Liu、Jiangpeng Liu、Jinwen Xin、Guojun Peng、Jiang Ming

- 🎯 **研究动机**：LLM 流水线把 OOXML 文档当一级证据，隐含假设 Office 画布所见与模型所取一致，该假设可被破坏
- 🔬 **研究方法**：遍历规范挖掘 21 类 evidence forks，用画布不可见的 task-relevant trap 测试 4 个原生 API 与 13 个提取工具
- 📌 **结论**：4 个 API 在 48%-76% 试验中返回 trap，13 个工具全部受至少一种机制影响，暴露由提取器配置决定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM pipelines increasingly ingest Office Open XML (OOXML) documents (Word, Excel, and PowerPoint files) as first-class evidence in financial, compliance, and retrieval-augmented workflows, implicitly assuming semantic integrity: that the evidence consumed by the model matches the content shown in the Microsoft Office suite editing canvas. We show that this assumption can fail in OOXML-to-LLM pipelines. The same specification-valid OOXML file can yield one evidentiary view in Microsoft Office and another when extracted for an LLM. Each view is treated as authoritative by its consumer, a condition we call plural ground truth. The ingestion contract rarely states which view and semantic roles become model evidence or preserves how that evidence was derived. We call the specification-grounded OOXML constructions that induce such divergence evidence forks. We systematically traverse and mine the OOXML specification and confirm 21 evidence forks across Excel, Word, and PowerPoint, spanning six dimensions of view construction. All 13 tools in our extraction panel emit evidence from at least one fork. We test four native-ingestion LLM APIs and seven web chatbots. Each test document carries a trap: a task-relevant fact exposed by extraction but not shown in Office. Across this 21-mechanism evaluation, the four APIs return the trap in 48--76% of trials. For 20 of 21 mechanisms, at least one of the eleven interfaces returns the trap. Our measurements further show that exposure is shaped upstream of the model by the ingestion path and extractor configuration. A source-level survey of sixteen popular open-source LLM projects further shows that default OOXML ingestion paths concentrate on affected extractor families.

</details>

### 6. FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion

📄 [arXiv](https://arxiv.org/abs/2606.15609) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/rao)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`attack`、`memory fragmentation`、`access control`、`tool-use agent`、`LLM agent`、`access-control bypass`

👤 **作者**：Zixin Rao、…、Zhen Xiang

- 🎯 **研究动机**：agent 访问控制只检查最终用户查询，长期记忆引入的时间信道使被禁内容可碎片化存入记忆再重组
- 🔬 **研究方法**：提出 FragFuse 三阶段：黑盒自适应查询+片段掩码识别会触发拒绝的片段、用标记载体查询注入记忆、后续攻击查询检索融合片段；并以代理优化自动生成攻击
- 📌 **结论**：四种 agent 设定、三种 SOTA 访问控制上平均绕过率 86.3%、端到端有害任务成功率 41.1%，任务退化仅 4.4%；prompt injection 与困惑度检测器均无法防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating requests and prevent misuse. We reveal a novel attack surface arising from agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing form, and later reconstructed through memory retrieval without appearing explicitly in the final user query. We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory. FragFuse operates in three stages: (1) identifying rejection-responsive fragments via black-box adaptive querying with fragment masking; (2) injecting these fragments into memory using marker carrier queries; and (3) retrieving and fusing the stored fragments through a follow-up attack query. Although FragFuse can be instantiated manually for individual agents, we further develop a surrogate-based optimization scheme that tunes fusion instructions and marker designs, enabling automated attack generation without violating the attacker's threat-model assumptions. We evaluate FragFuse across four representative agent settings and task domains, covering three state-of-the-art agent access-control mechanisms. FragFuse achieves an average bypass success rate of 86.3% and an average end-to-end harmful task success rate of 41.1% across all settings, with only 4.4% average task-success degradation compared with configurations without access control. We also show that alternative defenses, including state-of-the-art prompt-injection detectors and perplexity detectors, do not effectively address this attack.

</details>

### 7. MalTool: Malicious Tool Attacks on LLM Agents

📄 [arXiv](https://arxiv.org/abs/2602.12194)　📅 2026-02

**关键词**：`attack`、`malicious tool code`、`CIA impact`、`automated synthesis`

👤 **作者**：Yuepeng Hu、Yuqi Jia、Mengyuan Li、Dawn Song、Neil Gong

- 🎯 **研究动机**：恶意工具攻击研究聚焦操纵名称与描述，工具代码实现中的恶意行为未被系统研究
- 🔬 **研究方法**：按 CIA triad 提出恶意工具行为分类法；MalTool 用编码 LLM 加自动验证器迭代合成独立或嵌入良性实现的恶意工具
- 📌 **结论**：生成 1,300 个独立与 5,727 个嵌入恶意工具，传统恶意软件检测与 agent 专用检测均难可靠识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In a malicious tool attack, an attacker uploads a malicious tool to a distribution platform; once a user inadvertently installs the tool and the LLM agent selects it during task execution, the tool can compromise the user's security and privacy. Prior work focuses on manipulating tool names and descriptions to increase the likelihood of installation by users and selection by LLM agents. However, a successful attack also requires embedding malicious behaviors in the tool's code implementation, which remains largely unexplored. In this work, we bridge this gap by presenting the first systematic study of malicious tool code implementations. We first propose a taxonomy of malicious tool behaviors based on the confidentiality-integrity-availability triad, tailored to LLM-agent settings. To investigate the severity of the risks posed by attackers exploiting coding LLMs to automatically generate malicious tools, we develop MalTool, a coding-LLM-based framework that synthesizes tools exhibiting specified malicious behaviors, either as standalone tools or embedded within otherwise benign implementations. To ensure functional correctness and structural diversity, MalTool leverages an automated verifier that validates whether generated tools exhibit the intended malicious behaviors and differ sufficiently from previously generated instances, iteratively refining generations until success. Our evaluation demonstrates that MalTool is highly effective even when coding LLMs are safety-aligned. Using MalTool, we construct two datasets of malicious tools: 1,300 standalone malicious tools and 5,727 real-world tools with embedded malicious behaviors. We further show that existing detection methods, including conventional malware detection approaches and methods tailored to the LLM-agent setting, exhibit limited effectiveness at detecting the malicious tools, highlighting an urgent need for new defenses.

</details>

### 8. MemIncept: Steering LLM Agents via Cooperative Stealthy Memory Injections

🎓 [Official](https://icml.cc/virtual/2026/poster/66667)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`tool-use agent`、`tool interface`、`action integrity`、`LLM agent security`、`representation steering`

👤 **作者**：Nan Yan、Qian Lou、Jiarong Xing

- 🎯 **研究动机**：记忆注入攻击两难：有效注入显恶意易被检测，良性伪装注入则改变行为的效果差
- 🔬 **研究方法**：MemIncept 黑盒仅用良性查询生成协同查询集：前向保证集体导向目标结果，后向保证语义接近良性查询便于检索，双向进化 meet-in-the-middle
- 📌 **结论**：显著超单记录攻击，成功率接近显式攻击且难被自动过滤或人工审查标记

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory empowers LLM-based agents with adaptive reasoning but exposes a critical attack surface---adversaries can inject malicious records to bias agent behaviors. However, existing attacks face a dilemma: effective injections are often visibly malicious and easily detected, while stealthy, benign-looking injections are often less effective in altering agent behaviors. To address this, we propose MemIncept, a memory poisoning attack that can impact agents even in black-box settings using only benign-appearing queries. Unlike prior methods that inject isolated records, MemIncept generates a cooperative set of queries that work together to bias the agent. It achieves this via a bidirectional evolutionary strategy that optimizes the query set from two ends. A forward pass ensures the queries collectively lead the agent to the target outcome, while a backward pass ensures they are semantically close to victim (benign) queries for reliable retrieval. This ``meet-in-the-middle'' approach creates injected records that are both easy to retrieve and effective at steering behavior. Through extensive experiments across diverse agents, we show that MemIncept significantly outperforms single-record attacks, achieving high success rates comparable to explicit attacks while remaining difficult to flag under automated filters or human inspection.

</details>

### 9. Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS

🎓 [Official](https://aclanthology.org/2026.acl-long.330/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`tool-use agent`、`tool interface`、`action integrity`、`agent safety`、`LLM agent`

👤 **作者**：Bingyu Yan、…、Litian Zhang

- 🎯 **研究动机**：LLM-MAS 对工具输出的隐式信任构成攻击面，现有工具攻击受限于领域特定或固定静态模板
- 🔬 **研究方法**：Evo-Attacker 把工具攻击形式化为自进化记忆增强的强化学习：动态攻击记忆加深思推理检索对抗模式并择机干预；Attack-Flow GRPO 用终端结果优化中间推理步骤解决长时域信用分配
- 📌 **结论**：一致超越基线，展示泛化与进化能力，凸显工具防御的紧迫需求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. Existing tool attacks are limited by domain specificity or fixed and static templates. To address these challenges, we propose Evo-Attacker, which formulates the tool attack as a self-evolving, memory-augmented reinforcement learning process. Evo-Attacker constructs a dynamic attack memory and employs deliberative reasoning to retrieve adversarial patterns and strategize modifying interventions at critical moments. Furthermore, we introduce Attack-Flow GRPO to optimize intermediate reasoning steps via terminal outcomes, addressing the long-horizon credit assignment challenge. Comprehensive experiments demonstrate that Evo-Attacker consistently outperforms baselines, highlighting its generalization and evolutionary capabilities and the urgent need for defensive tool safeguards.

</details>

### 10. ToolTweak: An Attack on Tool Selection in LLM-based Agents

📄 [arXiv](https://arxiv.org/abs/2510.02554)　📅 2025-10

**关键词**：`attack`、`tool selection bias`、`metadata optimization`、`marketplace fairness`

👤 **作者**：Jonathan Sneh、…、Adel Bibi

- 🎯 **研究动机**：agent 从工具库或市场选择工具形成隐性竞争，该选择过程可被系统性偏置
- 🔬 **研究方法**：提出 ToolTweak：迭代操纵工具名称与描述以提升被选率的轻量自动攻击
- 📌 **结论**：工具选择率从约 20% 升至 81%，跨开源闭源强迁移并造成工具使用分布偏移；改写与困惑度过滤可缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs increasingly power agents that interact with external tools, tool use has become an essential mechanism for extending their capabilities. These agents typically select tools from growing databases or marketplaces to solve user tasks, creating implicit competition among tool providers and developers for visibility and usage. In this paper, we show that this selection process harbors a critical vulnerability: by iteratively manipulating tool names and descriptions, adversaries can systematically bias agents toward selecting specific tools, gaining unfair advantage over equally capable alternatives. We present ToolTweak, a lightweight automatic attack that increases selection rates from a baseline of around 20% to as high as 81%, with strong transferability between open-source and closed-source models. Beyond individual tools, we show that such attacks cause distributional shifts in tool usage, revealing risks to fairness, competition, and security in emerging tool ecosystems. To mitigate these risks, we evaluate two defenses: paraphrasing and perplexity filtering, which reduce bias and lead agents to select functionally similar tools more equally. All code will be open-sourced upon acceptance.

</details>

### 11. Attractive Metadata Attack: Inducing LLM Agents to Invoke Malicious Tools

📄 [arXiv](https://arxiv.org/abs/2508.02110) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ee46288ab2aaf5c6e53aebebe719712c-Abstract-Conference.html)　📅 2025-08　🏷 NeurIPS 2025

**关键词**：`attack`、`tool metadata`、`black-box optimization`、`privacy leakage`

👤 **作者**：Kanghua Mo、Li Hu、Yucheng Long、Zhihao Li

- 🎯 **研究动机**：工具元数据（名称、描述、参数 schema）是未被探索的攻击面，无需 prompt 注入即可操纵 agent 行为
- 🔬 **研究方法**：提出 Attractive Metadata Attack：黑盒上下文学习框架迭代优化出高吸引力且合法的工具元数据，无缝嵌入标准工具生态
- 📌 **结论**：十个模拟场景中 ASR 达 81-95% 并造成显著隐私泄露，prompt 级防御、审计器与 MCP 选择协议均挡不住

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents have demonstrated remarkable capabilities in complex reasoning and decision-making by leveraging external tools. However, this tool-centric paradigm introduces a previously underexplored attack surface, where adversaries can manipulate tool metadata -- such as names, descriptions, and parameter schemas -- to influence agent behavior. We identify this as a new and stealthy threat surface that allows malicious tools to be preferentially selected by LLM agents, without requiring prompt injection or access to model internals. To demonstrate and exploit this vulnerability, we propose the Attractive Metadata Attack (AMA), a black-box in-context learning framework that generates highly attractive but syntactically and semantically valid tool metadata through iterative optimization. The proposed attack integrates seamlessly into standard tool ecosystems and requires no modification to the agent's execution framework. Extensive experiments across ten realistic, simulated tool-use scenarios and a range of popular LLM agents demonstrate consistently high attack success rates (81\%-95\%) and significant privacy leakage, with negligible impact on primary task execution. Moreover, the attack remains effective even against prompt-level defenses, auditor-based detection, and structured tool-selection protocols such as the Model Context Protocol, revealing systemic vulnerabilities in current agent architectures. These findings reveal that metadata manipulation constitutes a potent and stealthy attack surface. Notably, AMA is orthogonal to injection attacks and can be combined with them to achieve stronger attack efficacy, highlighting the need for execution-level defenses beyond prompt-level and auditor-based mechanisms. Code is available at https://github.com/SEAIC-M/AMA.

</details>

### 12. Prompt Injection Attack to Tool Selection in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2504.19793) · 🌐 [Project](https://www.ndss-symposium.org/ndss-paper/prompt-injection-attack-to-tool-selection-in-llm-agents/)　📅 2025-04　🏷 NDSS 2026

**关键词**：`attack`、`tool selection`、`malicious document`、`no-box optimization`

👤 **作者**：Jiawen Shi、Zenghui Yuan、Guiyao Tie、Pan Zhou、Neil Zhenqiang Gong、Lichao Sun

- 🎯 **研究动机**：LLM agent 工具选择的检索-选择流程可被恶意工具文档操纵，缺乏 no-box 场景攻击
- 🔬 **研究方法**：提出 ToolHijacker，向工具库注入恶意工具文档并把文档构造形式化为两阶段优化问题
- 📌 **结论**：显著超人工与自动注入攻击；StruQ、SecAlign、DataSentinel 等预防与检测防御均不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool selection is a key component of LLM agents. A popular approach follows a two-step process - \emph{retrieval} and \emph{selection} - to pick the most appropriate tool from a tool library for a given task. In this work, we introduce \textit{ToolHijacker}, a novel prompt injection attack targeting tool selection in no-box scenarios. ToolHijacker injects a malicious tool document into the tool library to manipulate the LLM agent's tool selection process, compelling it to consistently choose the attacker's malicious tool for an attacker-chosen target task. Specifically, we formulate the crafting of such tool documents as an optimization problem and propose a two-phase optimization strategy to solve it. Our extensive experimental evaluation shows that ToolHijacker is highly effective, significantly outperforming existing manual-based and automated prompt injection attacks when applied to tool selection. Moreover, we explore various defenses, including prevention-based defenses (StruQ and SecAlign) and detection-based defenses (known-answer detection, DataSentinel, perplexity detection, and perplexity windowed detection). Our experimental results indicate that these defenses are insufficient, highlighting the urgent need for developing new defense strategies.

</details>

### 13. Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents

📄 [arXiv](https://arxiv.org/abs/2607.28165)　📅 2026-07

**关键词**：`attack`、`audio prompt injection`、`tool-call hijacking`、`cross-modal consistency`

👤 **作者**：Mingxiao Liu、…、Zhen Wang

- 🎯 **研究动机**：连续音频交互的多模态 agent 必然接收含环境噪声的音频，恶意指令可搭便车隐藏于用户语音，该并发注入攻击面未被探索
- 🔬 **研究方法**：提出指令增强与场景隐匿技术使恶意音频指令不可察觉地混入用户语音劫持工具调用；构建 AudioAgentSecurity 基准（8 场景 10 攻击模式）评估 11 个 agent，并提出基于源分离与一致性分析的级联解耦验证防御
- 📌 **结论**：对 Gemini 3 Pro 平均 ASR 69.10%；CADV 检测准确率最高 96%；豆包 AI 手机真实场景人因实验证实攻击隐蔽有效且防御可靠缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as audio inputs inevitably contain environmental noise beyond user control. In this paper, we investigate concurrent audio prompt injection attacks targeting multimodal agents. Distinct from traditional acoustic attacks on voice devices, we propose novel techniques for instruction augmentation and scenario concealment. These methods allow malicious audio instructions to imperceptibly "piggyback" onto user speech, thereby hijacking agents to execute malicious actions. To systematically quantify this threat, we construct AudioAgentSecurity, the first comprehensive benchmark for audio instruction injection attacks, encompassing 8 real-world task scenarios and 10 distinct attack patterns. We evaluate 11 state-of-the-art agents, including Gemini 3 Pro and GPT-4o-audio. Notably, our methods achieve an average Attack Success Rate (ASR) of 69.10\% against the advanced Gemini 3 Pro. To counter this threat, we further introduce Cascaded Audio Decoupling and Verification (CADV), a defense mechanism based on source separation and consistency analysis. Compared with existing prompt-level defenses, CADV achieving up to 96\% detection accuracy and providing effective protection against a broad range of acoustic injection attacks. Finally, real-world experiments with human volunteers on Doubao AI Smartphone in diverse dynamic real-world scenarios confirm the attacks' high stealth and efficacy, while demonstrating that our defense reliably mitigates these vulnerabilities.

</details>

### 14. MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0)

📄 [arXiv](https://arxiv.org/abs/2603.18063)　📅 2026-03

**关键词**：`analysis`、`MCP taxonomy`、`semantic attack surface`、`cross-framework mapping`

👤 **作者**：Yi Ting Shen、Kentaroh Toyoda、Alex Leung

- 🎯 **研究动机**：传统软件与通用 LLM 威胁框架无法覆盖 MCP 的动态语义接口攻击面
- 🔬 **研究方法**：经协议分解、多框架交叉映射、真实事件综合与修复面归类四阶段方法提出 MCP-38 的 38 类威胁，并映射到 STRIDE 与 OWASP LLM/Agentic Top 10
- 📌 **结论**：覆盖 tool description poisoning、间接注入、寄生工具链与动态信任违规等先前框架未捕获的威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) introduces a structurally distinct attack surface that existing threat frameworks, designed for traditional software systems or generic LLM deployments, do not adequately cover. This paper presents MCP-38, a protocol-specific threat taxonomy consisting of 38 threat categories (MCP-01 through MCP-38). The taxonomy was derived through a systematic four-phase methodology: protocol decomposition, multi-framework cross-mapping, real-world incident synthesis, and remediation-surface categorization. Each category is mapped to STRIDE, OWASP Top 10 for LLM Applications (2025, LLM01--LLM10), and the OWASP Top 10 for Agentic Applications (2026, ASI01--ASI10). MCP-38 addresses critical threats arising from MCP's semantic attack surface (tool description poisoning, indirect prompt injection, parasitic tool chaining, and dynamic trust violations), none of which are adequately captured by prior work. MCP-38 provides the definitional and empirical foundation for automated threat intelligence platforms.

</details>

### 15. Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation

📄 [arXiv](https://arxiv.org/abs/2512.16310)　📅 2026-09

**关键词**：`benchmark`、`tool orchestration`、`compositional privacy`、`reasoning-trace leakage`

👤 **作者**：Yuxuan Qiao、Dongqin Liu、Hongchang Yang、Wei Zhou、Songlin Hu

- 🎯 **研究动机**：LLM agent 可组合多个各自不泄露的工具返回并输出敏感结论，此类组合隐私风险未被形式化
- 🔬 **研究方法**：形式化 TOP-R 三条件，用四库反向构造管线 LRSE 构建 1000 实例的 TOP-Bench 与两阶段工具使用协议评测六个 agent，并提出 SFT+DPO 的 TOP-Align 防御
- 📌 **结论**：agent 平均任务完成率 98.0% 但泄漏率 88.6%、H-score 仅 20.4，推理开启时推理轨迹泄漏达 82.4%；TOP-Align 提升 H-score 16.2 点，远超 prompt 缓解的 5.0 点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents can combine individually non-revealing tool returns and disclose a sensitive conclusion, creating Tools Orchestration Privacy Risk (TOP-R). We formalize TOP-R through three conditions: conclusion sensitivity, single-source non-inferability, and compositional inferability. We introduce Library-Grounded Reverse-Inference Seed Expansion (LRSE), a four-library reverse-construction pipeline, and use it to build TOP-Bench, a 1,000-instance benchmark evaluated under a controlled two-stage tool-use protocol. Across six LLM agents, average task completion, leakage, and H-score are 98.0 percent, 88.6 percent, and 20.4. With native reasoning enabled, four models average 81.4 percent final-response leakage and 82.4 percent reasoning-trace leakage. With reasoning disabled, three prompt-only safeguards improve H-score by an average of about 3.4 points on TOP-Bench. We further propose TOP-Align, an SFT+DPO method for learning safer task-completion boundaries. On a separate post-training evaluation set, TOP-Align improves H-score by 16.2 points over the base model, versus a 5.0-point average gain from prompt-only mitigation on the same set. These results show that TOP-R requires defenses beyond prompting alone. Dataset and code are available at https://github.com/1Ponder/TOP-R.

</details>

### 16. Extracting Knowledge from Tools in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.30288)　📅 2026-09

**关键词**：`attack`、`knowledge-based tool`、`tool-selection steering`、`source reconstruction`、`tool-mediated extraction`、`knowledge-source reconstruction`

👤 **作者**：Chuanchao Zang、…、Shanqing Guo

- 🎯 **研究动机**：Agent 通过工具调用访问知识库时，合法响应暴露的源内容可能被逐步重组还原，此风险未被系统研究
- 🔬 **研究方法**：提出 query-only 攻击 ToolSiphon：用 Tool Contrastive Analysis 引导查询命中目标工具、Evidence Chained Feedback 缓解参数压缩并扩大抽取覆盖
- 📌 **结论**：三类知识工具、六个数据集上平均恢复 74.3% 源记录（文本恢复 83.2%），无粗粒度信息时仍有 66.3%，并能绕过代表性防御与三个真实 Agent 平台

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents commonly use knowledge-based tools and access their underlying files, databases, and search indexes through tool invocation. This integration improves agents' ability to provide domain-specific services but also introduces the risk of tool-mediated knowledge extraction: source content exposed to an agent for legitimate responses may be progressively recovered from its outputs, enabling reconstruction of the knowledge source behind a target tool. This paper systematically investigates this risk and identifies two challenges introduced by tool invocation: tool-selection uncertainty, where an agent may invoke a competing tool instead of the target tool, and tool-argument compression, where fine-grained query information may be lost when the agent generates tool arguments. To tackle these challenges, we propose ToolSiphon, a query-only extraction attack that introduces two complementary signals: a target-discriminative signal, implemented through Tool Contrastive Analysis, to steer queries toward the target tool; and a response-grounded factual signal, implemented through Evidence Chained Feedback, to mitigate argument compression and progressively expand extraction coverage. Across three types of knowledge-based tools and six domain-specific datasets, ToolSiphon recovers 74.3% of source records on average when coarse-grained information about non-target tools is available, with 83.2% textual recovery and 90.2% semantic similarity. Even without such information, it recovers 66.3% of source records. ToolSiphon also remains effective against representative defenses and on three real-world agent platforms.

</details>

### 17. MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP

📄 [arXiv](https://arxiv.org/abs/2601.07395)　📅 2026-01

**关键词**：`attack`、`implicit tool poisoning`、`metadata injection`、`privilege abuse`

👤 **作者**：Ruiqi Li、Zhiqiang Wang、Yunhao Yao、Xiang-Yang Li

- 🎯 **研究动机**：已有 MCP 工具投毒聚焦显式投毒或手工构造，毒工具自身不被调用的隐式投毒缺乏自动化方法
- 🔬 **研究方法**：MCP-ITP 把毒工具生成形式化为黑盒优化，迭代利用评测 LLM 与检测 LLM 的反馈，让工具元数据中的指令诱导 agent 调用合法高权限工具执行恶意操作
- 📌 **结论**：在 MCPTox 数据集 12 个 LLM agent 上 ASR 最高 84.2%，同时恶意工具检出率被压至 0.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To standardize interactions between LLM-based agents and their environments, the Model Context Protocol (MCP) was proposed and has since been widely adopted. However, integrating external tools expands the attack surface, exposing agents to tool poisoning attacks. In such attacks, malicious instructions embedded in tool metadata are injected into the agent context during MCP registration phase, thereby manipulating agent behavior. Prior work primarily focuses on explicit tool poisoning or relied on manually crafted poisoned tools. In contrast, we focus on a particularly stealthy variant: implicit tool poisoning, where the poisoned tool itself remains uninvoked. Instead, the instructions embedded in the tool metadata induce the agent to invoke a legitimate but high-privilege tool to perform malicious operations. We propose MCP-ITP, the first automated and adaptive framework for implicit tool poisoning within the MCP ecosystem. MCP-ITP formulates poisoned tool generation as a black-box optimization problem and employs an iterative optimization strategy that leverages feedback from both an evaluation LLM and a detection LLM to maximize Attack Success Rate (ASR) while evading current detection mechanisms. Experimental results on the MCPTox dataset across 12 LLM agents demonstrate that MCP-ITP consistently outperforms the manually crafted baseline, achieving up to 84.2% ASR while suppressing the Malicious Tool Detection Rate (MDR) to as low as 0.3%.

</details>

### 18. Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via Model Context Protocol

📝 [OpenReview](https://openreview.net/forum?id=UVgbFuXPaO)　📅 2025-09

**关键词**：`attack`、`MCP prompt injection`、`covert logging`、`data exfiltration`

- 🎯 **研究动机**：MCP元数据可否不损任务质量地触发隐蔽数据外泄未被系统分析
- 🔬 **研究方法**：Log-To-Leak将injection拆为Trigger、Tool Binding、Justification与Pressure，诱导agent调用恶意logging tool
- 📌 **结论**：五个真实server与四种agent上可持续捕获user query、tool response与agent reply

### 19. ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.27496)　📅 2026-08

**关键词**：`defense`、`pre-execution guard`、`origin policy`、`sensitive parameter`、`runtime reference monitor`、`parameter admission`

👤 **作者**：Xinhang Ma、Chaowei Xiao、William Yeoh、Ning Zhang、Yevgeniy Vorobeychik

- 🎯 **研究动机**：Agent 能力增强后工具序列与参数值多在运行时确定，仅凭用户查询做工具筛查或信息流控制会显著损失效用
- 🔬 **研究方法**：提出 ROPE：值只有不可伪造地追溯到用户、用户指定来源或用户权威记录才可进入有状态工具的敏感参数；对被审计参数集做确定性 origin check，LLM 仅介入可信用户请求
- 📌 **结论**：在四种 Agent 模型上把攻击成功率限制在 1.6%–2.6%，保留 82%–100% 无防御干净效用，使击穿既有防御的长程攻击成功率归零，并附两条可证明保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Indirect prompt injection (IPI) plants instructions in the content a tool-using LLM agent reads, steering the agent into harmful tool calls. The strongest defenses are system-level, leveraging techniques such as task-conditional tool screening to prevent execution of malicious tools, and information-flow control to avoid tool execution with untrusted parameters. However, as agents grow more capable, users delegate more to automation. Consequently, tool execution sequences and parameter values are increasingly determined at runtime and cannot be reliably screened from solely user's query without significant utility loss. We present ROPE (Routed Origin Policy Enforcement), which is anchored in a structural notion of trust: a value may reach a state-changing tool only if it traces unforgeably to the user, a source the user explicitly named, or the user's own authoritative records. Enforcement is then a deterministic origin check over an audited set of sensitive tool parameters, and the only reliance on a language model involves solely the trusted user request, out of the attacker's reach. Our approach admits two provable guarantees: 1) at every step of a trajectory, no value whose only origin is attacker-writable content reaches an origin-guarded parameter, and 2) no rewording of an injection changes an admission decision. We evaluate across four agent models on open-ended agent suites, ROPE holds attack success rate to 1.6--2.6\% while retaining 82--100\% of undefended clean utility, significantly exceeding state-of-the-art system-level defenses in utility while attaining comparable or better security. Further, we show that optimizing the injection against ROPE is largely ineffective, while long-horizon attacks that defeat prior system-level defenses achieve zero success rate. Our code and logs are available at https://github.com/xhOwenMa/ROPE .

</details>

### 20. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21126)　📅 2026-08

**关键词**：`defense`、`task-effect contract`、`delegated authority`、`lifecycle governance`、`contract-governed guardrail`、`authority boundary`

👤 **作者**：Bohao Liao、Jingchao Wang、Qipeng Song、Jin Cao、Jieling Wang、Boyu Deng

- 🎯 **研究动机**：联网 Agent 任务内容可夹带间接 prompt injection 重定向工具或篡改参数，现有防御只约束不可信内容或单次调用，用户意图、运行时证据与实际效果间缺乏闭环
- 🔬 **研究方法**：TraceGrant 以显式 Contract 治理任务效果生命周期：执行前从可信用户请求建立 task-effect 边界，执行中证据只能实例化 Contract 已确立的权限，执行后按实际工具结果验证任务完成
- 📌 **结论**：949 个 AgentDojo 与 400 个 Agent Security Bench 攻击案例中零攻击成功，攻击下效用保留率分别为 77.32% 与 83.00%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidence, realized effects, and task completion insufficiently connected. We present TraceGrant, a security framework that governs the task-effect lifecycle of networked LLM agents through an explicit Contract. Before execution, TraceGrant establishes a task-effect boundary from the trusted user request. During execution, admitted evidence can instantiate only authority already established by the Contract. After execution, task completion is verified against actual tool results. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed benchmark settings, TraceGrant recorded no attack successes while retaining utility under attack rates of 77.32% and 83.00%, respectively. We further evaluate TraceGrant through white-box defense-aware attacks, Contract quality analysis, stage ablations, targeted stress tests, and runtime overhead measurements. The results show that TraceGrant provides a unified governance layer that connects trusted user intent, runtime evidence, concrete tool execution, and verified task completion.

</details>

### 21. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.27146)　📅 2026-08

**关键词**：`defense`、`action authorization`、`provenance tracking`、`indirect prompt injection`、`runtime authorization`、`provenance contract`

👤 **作者**：Xiaokun Guo、…、Yu Wang

- 🎯 **研究动机**：工具输出可从提供数据变成指定具体动作的命令并引发越权副作用，根源是现有 Agent 把动作诱导与执行授权混为一谈
- 🔬 **研究方法**：提出 SARA，将动作诱导与执行授权拆为独立运行时角色：上下文隔离的 Action Probe 暴露诱导语义并跨步记录 action provenance，工具调用仅凭用户目标与已授权执行证据放行，No-History-Promotion 防止历史递归洗白来源
- 📌 **结论**：在 AgentDojo 与 AgentDyn 四个主要设置中 ASR 不超过 0.63%，任务效用保持竞争力，且在多个 Agent backbone 上一致降低 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority. On the Observation side, a context-isolated Action Probe exposes action-inducing semantics and persistently records action-origin provenance across steps as a review signal; on the execution side, actual tool calls are authorized only against the user objective and audited evidence from authorized successful executions, while satisfying goal, execution-chain, and argument-level support. To preserve this separation across multi-step execution, SARA applies No-History-Promotion to prevent historical recurrence from laundering action origins into execution authority. Across AgentDojo and AgentDyn, SARA limits ASR to no more than \(0.63\%\) across four primary evaluation settings while maintaining competitive task utility, and consistently reduces ASR across additional Agent backbones.

</details>

### 22. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

📄 [arXiv](https://arxiv.org/abs/2608.27234)　📅 2026-08

**关键词**：`defense`、`plan-first guardrail`、`information-flow control`、`persistent agent`、`plan-first runtime`、`information-flow contract`

👤 **作者**：Dylan Girrens、Guangjing Wang

- 🎯 **研究动机**：持久 LLM Agent 面临攻击者数据经持久状态污染控制流与后续查询的威胁，现有防御只保护规划或单次工具交互
- 🔬 **研究方法**：提出 plan-first 架构 SPA：每查询一次生成 DSL 完整计划，对显式数据流与控制依赖施加 dual-lattice 信息流控制，执行结果存为带标签 artifact，后续规划只暴露语义元数据
- 📌 **结论**：在 AgentDojo 上将 tool_knowledge 攻击成功率降至 0，在自建多查询扩展 AgentDojo-MQ 上降至 0.2%，同时揭示严格完整性约束的安全—效用权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly operate over untrusted webpages, documents, tools, and persistent states while exercising authority over security-sensitive resources. Existing defenses typically protect either planning or individual tool interactions, but persistent agents face a broader threat: attacker-controlled data can alter control flow, enter security-sensitive tool arguments, or compromise later queries. We present SPA, a plan-first architecture that secures planning, execution, and cross-query state reuse. SPA invokes the planner once per query to generate a complete executable plan in a declarative domain-specific language, then applies dual-lattice information-flow control to track confidentiality and integrity across explicit data flows and control dependencies. To support persistence without re-exposing untrusted payloads to the planner, SPA stores execution results as labeled artifacts and reveals only semantic metadata during later planning. We evaluate SPA on AgentDojo and AgentDojo-MQ, which is our multi-query extension for measuring secure state reuse and delayed attacks. Under the 'tool_knowledge' attack, SPA with information-flow control reduces attack success to zero on AgentDojo and 0.2% on AgentDojo-MQ. Our results show that plan-first execution combined with label-preserving persistence can substantially strengthen persistent LLM agents, while revealing an important security-utility tradeoff introduced by strict integrity enforcement.

</details>

### 23. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.22868)　📅 2026-08

**关键词**：`defense`、`flow-centric policy`、`runtime enforcement`、`prompt injection`、`runtime reference monitor`、`stateful taint`

👤 **作者**：Basavesh Ammanaghatta Shivakumar、Swarn Priya、Peng Gao

- 🎯 **研究动机**：LLM agent 的伤害常来自敏感数据跨多个看似合理步骤的流动而非单个不安全动作，现有防御只约束单次调用
- 🔬 **研究方法**：AgentFlow 流中心策略语言与运行时执行模型：策略定义在带标签的运行时边上，约束哪些工具可收敏感字段、哪些 sink 可接收释放数据、何种权限可跨委托边界，支持 flow/path 规则、task-scoped capability 与有状态 taint 语义，由 reference monitor 仲裁并经有界 SMT 验证
- 📌 **结论**：949 个 AgentDojo 注入案例确认攻陷从 33.0% 降至 0.0% 且效用从 46.7% 升至 63.3%；AgentDyn 上 73.5%→0.0%，ASB 直接注入 harness 攻击成功 0/1200

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive fields, which sinks may receive released data, and what authority may cross delegation boundaries. The language supports flow and path rules, task-scoped capabilities, controlled release, and stateful taint semantics. A runtime reference monitor mediates agent actions, and a bounded SMT-based verifier checks safety properties for a structured policy fragment. We evaluate AgentFlow on multiple agent benchmarks. In our prototype, seven safety properties verify in under 0.5 seconds each, and the verifier catches all seeded unsafe policy variants in our study. On 949 AgentDojo injected cases across four suites, AgentFlow reduces confirmed compromise from 33.0\% to 0.0\% while improving aggregate utility from 46.7\% to 63.3\%. On a 200-case AgentDyn Dailylife benchmark, it reduces confirmed compromise from 73.5\% to 0.0\% while preserving near-baseline utility (44.5\% to 43.5\%). Breadth checks across ASB, InjecAgent, BIPIA, AgentHarm, and MCPTox replays suggest that the configured policies block the benchmark-specified policy-visible attacker flows; in ASB's direct-prompt-injection harness, attack success is 0/1{,}200. These results are preliminary and scoped to the modeled policy-visible agent behaviors and evaluated benchmarks.

</details>

### 24. Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21544)　📅 2026-08

**关键词**：`defense`、`tool-mediated recovery`、`target-seeking tool call`、`knowledge leakage`、`capability removal`、`external-tool recovery`

👤 **作者**：Baicheng Chen、…、Meng Jiang

- 🎯 **研究动机**：现有 unlearning 只抑制参数化直接回忆，工具增强 Agent 仍可经 web 搜索、检索或数据库查找恢复遗忘目标（tool-mediated recovery），评测存在错配
- 🔬 **研究方法**：ATU 两阶段框架：先做参数知识遗忘抑制直接回忆，再在模拟工具环境中做轨迹级 RL，惩罚 target-seeking 工具行为与最终答案泄漏
- 📌 **结论**：RWKU 与 MUSE 上跨不同 LLM 架构取得目标遗忘与保留效用间更好平衡，unlearning 在工具增强部署下更稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

</details>

### 25. SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation

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

### 26. Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents

📄 [arXiv](https://arxiv.org/abs/2602.13379) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62233)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`benchmark`、`multi-turn tool use`、`MT-AgentRisk`、`self-exploration`、`agent safety`

👤 **作者**：Xu Li、…、Weiyan Shi

- 🎯 **研究动机**：agent 安全评测未覆盖多轮工具使用场景下被放大的风险
- 🔬 **研究方法**：用分类法把单轮有害任务变换为多轮攻击序列构建 MT-AgentRisk；ToolShield 让 agent 对新工具自生成测试用例、执行观察并蒸馏安全经验
- 📌 **结论**：多轮场景 ASR 平均升 16%，ToolShield 免训练再平均降 30%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents are becoming increasingly capable, yet their safety lags behind. This creates a gap between what agents can do and should do. This gap widens as agents engage in multi-turn interactions and employ diverse tools, introducing new risks overlooked by existing benchmarks. To systematically scale safety testing into multi-turn, tool-realistic settings, we propose a principled taxonomy that transforms single-turn harmful tasks into multi-turn attack sequences. Using this taxonomy, we construct MT-AgentRisk (Multi-Turn Agent Risk Benchmark), the first benchmark to evaluate multi-turn tool-using agent safety. Our experiments reveal substantial safety degradation: the Attack Success Rate (ASR) increases by 16% on average across open and closed models in multi-turn settings. To close this gap, we propose ToolShield, a training-free, tool-agnostic, self-exploration defense: when encountering a new tool, the agent autonomously generates test cases, executes them to observe downstream effects, and distills safety experiences for deployment. Experiments show that ToolShield effectively reduces ASR by 30% on average in multi-turn interactions. Our code is available at https://github.com/CHATS-lab/ToolShield.

</details>

### 27. Towards Verifiably Safe Tool Use for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2601.08012) · 🌐 [Project](https://doi.org/10.1145/3786582.3786839)　📅 2026-01　🏷 ICSE 2026

**关键词**：`defense`、`tool authorization`、`formal specification`、`runtime verification`

👤 **作者**：Aarya Doshi、Yining Hong、Congying Xu、Eunsuk Kang、Alexandros Kapravelos、Christian Kästner

- 🎯 **研究动机**：模型式防护只提升可靠性而无法保证安全，信息流控制与时序约束又需大量人工标注
- 🔬 **研究方法**：用 STPA 识别 agent 工作流危害、导出安全需求并形式化为数据流与工具序列上可执行的规约，配合要求能力、机密性与信任级结构化标签的能力增强 MCP 框架
- 📌 **结论**：把 LLM agent 安全从临时可靠性修补转向带形式保证的主动护栏，减少对用户确认的依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-based AI agents extend LLM capabilities by enabling access to tools such as data sources, APIs, search engines, code sandboxes, and even other agents. While this empowers agents to perform complex tasks, LLMs may invoke unintended tool interactions and introduce risks, such as leaking sensitive data or overwriting critical records, which are unacceptable in enterprise contexts. Current approaches to mitigate these risks, such as model-based safeguards, enhance agents' reliability but cannot guarantee system safety. Methods like information flow control (IFC) and temporal constraints aim to provide guarantees but often require extensive human annotation. We propose a process that starts with applying System-Theoretic Process Analysis (STPA) to identify hazards in agent workflows, derive safety requirements, and formalize them as enforceable specifications on data flows and tool sequences. To enable this, we introduce a capability-enhanced Model Context Protocol (MCP) framework that requires structured labels on capabilities, confidentiality, and trust level. Together, these contributions aim to shift LLM-based agent safety from ad hoc reliability fixes to proactive guardrails with formal guarantees, while reducing dependence on user confirmation and making autonomy a deliberate design choice.

</details>

### 28. Defense Against Indirect Prompt Injection via Tool Result Parsing

📄 [arXiv](https://arxiv.org/abs/2601.04795)　📅 2026-01

**关键词**：`defense`、`indirect prompt injection`、`tool-result parsing`、`instruction-data separation`

👤 **作者**：Qiang Yu、Xinran Cheng、Chuanyi Liu

- 🎯 **研究动机**：专用检测模型训练推理开销大且需频繁更新，prompt 防御的 ASR 又居高不下
- 🔬 **研究方法**：通过解析工具结果为 LLM 提供精确数据并过滤注入的恶意代码，实现指令与数据分离
- 📌 **结论**：在保持竞争性受攻效用（UA）的同时取得迄今最低 ASR，显著优于现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM agents transition from digital assistants to physical controllers in autonomous systems and robotics, they face an escalating threat from indirect prompt injection. By embedding adversarial instructions into the results of tool calls, attackers can hijack the agent's decision-making process to execute unauthorized actions. This vulnerability poses a significant risk as agents gain more direct control over physical environments. Existing defense mechanisms against Indirect Prompt Injection (IPI) generally fall into two categories. The first involves training dedicated detection models; however, this approach entails high computational overhead for both training and inference, and requires frequent updates to keep pace with evolving attack vectors. Alternatively, prompt-based methods leverage the inherent capabilities of LLMs to detect or ignore malicious instructions via prompt engineering. Despite their flexibility, most current prompt-based defenses suffer from high Attack Success Rates (ASR), demonstrating limited robustness against sophisticated injection attacks. In this paper, we propose a novel method that provides LLMs with precise data via tool result parsing while effectively filtering out injected malicious code. Our approach achieves competitive Utility under Attack (UA) while maintaining the lowest Attack Success Rate (ASR) to date, significantly outperforming existing methods. Code is available at GitHub.

</details>

### 29. Defeating Prompt Injections by Design

📄 [arXiv](https://arxiv.org/abs/2503.18813) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-03　🏷 SaTML 2026

**关键词**：`defense`、`policy enforcement`、`capability guard`、`non-interference`、`LLM agent`、`prompt injection`

👤 **作者**：Edoardo Debenedetti、…、Florian Tramèr

- 🎯 **研究动机**：LLM agent 处理不可信数据时易受 prompt injection，仅靠模型自身对齐无法根治
- 🔬 **研究方法**：提出 CaMeL 防御层，从可信查询显式提取控制流与数据流使不可信数据无法影响程序流，并以 capability 与策略约束工具调用
- 📌 **结论**：在 AgentDojo 上以可证明安全解决 77% 任务（无防御系统为 84%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in agentic systems that interact with an untrusted environment. However, LLM agents are vulnerable to prompt injection attacks when handling untrusted data. In this paper we propose CaMeL, a robust defense that creates a protective system layer around the LLM, securing it even when underlying models are susceptible to attacks. To operate, CaMeL explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow. To further improve security, CaMeL uses a notion of a capability to prevent the exfiltration of private data over unauthorized data flows by enforcing security policies when tools are called. We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. We release CaMeL at https://github.com/google-research/camel-prompt-injection.

</details>

### 30. ToolSafe: Enhancing Tool Invocation Safety of LLM-based Agents via Proactive Step-level Guardrail and Feedback

📄 [arXiv](https://arxiv.org/abs/2601.10156) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1850/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`tool invocation`、`step-level guard`、`TS-Flow`

👤 **作者**：Yutao Mou、…、Jing Shao

- 🎯 **研究动机**：LLM agent 步级工具调用行为的实时监控与执行前主动干预缺乏研究
- 🔬 **研究方法**：构建步级工具调用安全基准 TS-Bench，用多任务强化学习训练 TS-Guard 依据交互历史预判有害调用，并以 TS-Flow 把 guardrail 反馈接入 agent 推理
- 📌 **结论**：ReAct 式 agent 的有害工具调用平均减少 65%，prompt injection 下良性任务完成率提升约 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While LLM-based agents can interact with environments via invoking external tools, their expanded capabilities also amplify security risks. Monitoring step-level tool invocation behaviors in real time and proactively intervening before unsafe execution is critical for agent deployment, yet remains under-explored. In this work, we first construct TS-Bench, a novel benchmark for step-level tool invocation safety detection in LLM agents. We then develop a guardrail model, TS-Guard, using multi-task reinforcement learning. The model proactively detects unsafe tool invocation actions before execution by reasoning over the interaction history. It assesses request harmfulness and action-attack correlations, producing interpretable and generalizable safety judgments and feedback. Furthermore, we introduce TS-Flow, a guardrail-feedback-driven reasoning framework for LLM agents, which reduces harmful tool invocations of ReAct-style agents by 65 percent on average and improves benign task completion by approximately 10 percent under prompt injection attacks.

</details>

### 31. MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers

📄 [arXiv](https://arxiv.org/abs/2512.15163) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011290)　📅 2025-12　🏷 ICLR 2026

**关键词**：`benchmark`、`MCP server`、`multi-turn evaluation`、`cross-server attack`

👤 **作者**：Xuanjun Zong、Zhiqi Shen、Lei Wang、Yunshi Lan、Chao Yang

- 🎯 **研究动机**：已有基准聚焦孤立攻击或缺乏真实覆盖，无法评估 MCP 多服务器工作流的安全风险
- 🔬 **研究方法**：基于真实 MCP 服务器构建覆盖浏览器自动化、金融分析、位置导航、仓库管理与网络搜索五领域的多轮评测基准，统一 20 类覆盖 server、host、user 三侧的攻击分类，含跨服务器协同任务
- 📌 **结论**：领先的开源与闭源 LLM 均可被 MCP 攻击突破，且存在明显的 safety-utility 权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage. We present MCP-SafetyBench, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains: browser automation, financial analysis, location navigation, repository management, and web search. It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty. Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing that all models remain vulnerable to MCP attacks, with a notable safety-utility trade-off. Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments.

</details>

### 32. MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2510.15994) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007929)　📅 2025-10　🏷 ICLR 2026

**关键词**：`benchmark`、`MCP pipeline`、`real tool execution`、`NRP`

👤 **作者**：Dongsen Zhang、Zekun Li、Xu Luo、Xuannan Liu、Peipei Li、Wenjun Xu

- 🎯 **研究动机**：MCP 让工具成为带自然语言元数据的可组合攻击面，但缺乏端到端、真实工具执行的安全评测套件
- 🔬 **研究方法**：MSB 定义 12 类 MCP 攻击（名称碰撞、偏好操纵、工具描述注入、错误升级等），以真实工具执行生成 2000 个攻击实例，并提出 Net Resilient Performance 指标权衡安全与性能
- 📌 **结论**：9 个 LLM agent 在 10 域 405 工具上被各阶段攻击有效突破；性能更强的模型因工具调用与指令遵循更好反而更易受攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) standardizes how large language model (LLM) agents discover, describe, and call external tools. While MCP unlocks broad interoperability, it also enlarges the attack surface by making tools first-class, composable objects with natural-language metadata, and standardized I/O. We present MSB (MCP Security Benchmark), the first end-to-end evaluation suite that systematically measures how well LLM agents resist MCP-specific attacks throughout the full tool-use pipeline: task planning, tool invocation, and response handling. MSB contributes: (1) a taxonomy of 12 attacks including name-collision, preference manipulation, prompt injections embedded in tool descriptions, out-of-scope parameter requests, user-impersonating responses, false-error escalation, tool-transfer, retrieval injection, and mixed attacks; (2) an evaluation harness that executes attacks by running real tools (both benign and malicious) via MCP rather than simulation; and (3) a robustness metric that quantifies the trade-off between security and performance: Net Resilient Performance (NRP). We evaluate nine popular LLM agents across 10 domains and 405 tools, producing 2,000 attack instances. Results reveal the effectiveness of attacks against each stage of MCP. Models with stronger performance are more vulnerable to attacks due to their outstanding tool calling and instruction following capabilities. MSB provides a practical baseline for researchers and practitioners to study, compare, and harden MCP agents. Code: https://github.com/dongsenzhang/MSB

</details>

### 33. SafeToolBench: Pioneering a Prospective Benchmark to Evaluating Tool Utilization Safety in LLMs

📄 [arXiv](https://arxiv.org/abs/2509.07315) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.958/)　📅 2025-09　🏷 EMNLP 2025

**关键词**：`benchmark`、`prospective safety`、`malicious instruction`、`tool risk`

👤 **作者**：Hongfei Xia、Hongru Wang、Zeming Liu、Qian Yu、Yuhang Guo、Haifeng Wang

- 🎯 **研究动机**：既有工具安全评测在执行后回顾，无法避免直接执行工具造成不可逆伤害
- 🔬 **研究方法**：提出首个前瞻式工具使用安全基准 SafeToolBench 覆盖恶意指令与实用工具集，并提出从 User Instruction、Tool Itself、Joint 三视角九维的 SafeInstructTool 框架
- 📌 **结论**：现有方法无法捕捉全部工具使用风险，新框架显著提升 LLM 的工具安全自我感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have exhibited great performance in autonomously calling various tools in external environments, leading to better problem solving and task automation capabilities. However, these external tools also amplify potential risks such as financial loss or privacy leakage with ambiguous or malicious user instructions. Compared to previous studies, which mainly assess the safety awareness of LLMs after obtaining the tool execution results (i.e., retrospective evaluation), this paper focuses on prospective ways to assess the safety of LLM tool utilization, aiming to avoid irreversible harm caused by directly executing tools. To this end, we propose SafeToolBench, the first benchmark to comprehensively assess tool utilization security in a prospective manner, covering malicious user instructions and diverse practical toolsets. Additionally, we propose a novel framework, SafeInstructTool, which aims to enhance LLMs' awareness of tool utilization security from three perspectives (i.e., \textit{User Instruction, Tool Itself, and Joint Instruction-Tool}), leading to nine detailed dimensions in total. We experiment with four LLMs using different methods, revealing that existing approaches fail to capture all risks in tool utilization. In contrast, our framework significantly enhances LLMs' self-awareness, enabling a more safe and trustworthy tool utilization.

</details>

### 34. MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

📄 [arXiv](https://arxiv.org/abs/2508.13220)　📅 2025-08

**关键词**：`benchmark`、`MCP attack surface`、`security specification`、`playground`

👤 **作者**：Yixuan Yang、Cuifeng Gao、Daoyuan Wu、Yufan Chen、Yingjiu Li、Shuai Wang

- 🎯 **研究动机**：MCP 把 agent 接入数据源与外部工具，显著扩大攻击面，但缺乏安全规范与评测基准
- 🔬 **研究方法**：形式化安全 MCP 规范，建立含协议级与主机侧威胁的 17 类攻击分类法，并构建集成数据集、服务器、客户端、攻击脚本与防护机制的 MCPSecBench
- 📌 **结论**：三大 MCP 平台所有攻击面均被攻破，核心漏洞普遍影响 Claude、OpenAI 与 Cursor，现有防护平均成功率不足 30%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly integrated into real-world applications via the Model Context Protocol (MCP), a universal open standard for connecting AI agents with data sources and external tools. While MCP enhances the capabilities of LLM-based agents, it also introduces new security risks and significantly expands their attack surface. In this paper, we present the first formalization of a secure MCP and its required specifications. Based on this foundation, we establish a comprehensive MCP security taxonomy that extends existing models by incorporating protocol-level and host-side threats, identifying 17 distinct attack types across four primary attack surfaces. Building on these specifications, we introduce MCPSecBench, a systematic security benchmark and playground that integrates prompt datasets, MCP servers, MCP clients, attack scripts, a GUI test harness, and protection mechanisms to evaluate these threats across three major MCP platforms. MCPSecBench is designed to be modular and extensible, allowing researchers to incorporate custom implementations of clients, servers, and transport protocols for rigorous assessment. Our evaluation across three major MCP platforms reveals that all attack surfaces yield successful compromises. Core vulnerabilities universally affect Claude, OpenAI, and Cursor, while server-side and specific client-side attacks exhibit considerable variability across different hosts and models. Furthermore, current protection mechanisms proved largely ineffective, achieving an average success rate of less than 30%. Overall, MCPSecBench standardizes the evaluation of MCP security and enables rigorous testing across all protocol layers.

</details>

### 35. MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers

📄 [arXiv](https://arxiv.org/abs/2508.14925) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40895)　📅 2025-08　🏷 AAAI 2026

**关键词**：`benchmark`、`MCP tool poisoning`、`metadata injection`、`real-world server`

👤 **作者**：Zhiqiang Wang、…、Xiangyang Li

- 🎯 **研究动机**：MCP工具投毒此前只有孤立案例，缺真实规模评测
- 🔬 **研究方法**：基于45个在线server、353个真实tool构建覆盖十类风险的metadata injection基准MCPTox
- 📌 **结论**：20个受测agent普遍沦陷，更强instruction following未带来有效拒绝

### 36. Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents

📄 [arXiv](https://arxiv.org/abs/2607.29254)　📅 2026-07

**关键词**：`defense`、`prompt injection`、`tool-use agent`、`tool interface`

👤 **作者**：Minghui Pan、Jiayuxuan Yang、Yuanyuan Yuan、Yu Jiang、Zhenpeng Chen

- 🎯 **研究动机**：LLM 部署为 agent 后安全性大幅下降，退化根源不明
- 🔬 **研究方法**：白盒表征分析发现 schema 格式工具规范会削弱模型内部拒答信号；SafeKeep 在推理时用扁平文本规范做安全判断、保留原 schema 规范执行
- 📌 **结论**：两基准四模型上有害请求平均拒答率从 23.8% 升至 70.6%，观测级提示注入 ASR 从 25.6% 降至 2.5%，且保持任务能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood. In this paper, we identify schema-formatted tool specifications as a primary source of agent safety degradation and show, through white-box representation analysis, that they weaken the model's internal refusal signals and contribute to unsafe tool execution. Building on this finding, we propose SafeKeep, an inference-time safeguard that decouples safety judgment from tool execution: it assesses requests using flattened textual tool specifications while retaining the original schema-formatted specifications for execution. Across two representative benchmarks and four LLMs, including both white-box and black-box models, SafeKeep increases the average refusal rate for harmful requests from 23.8% to 70.6% and reduces the average attack success rate under observation-level prompt injection from 25.6% to 2.5%. It also outperforms existing safeguards and preserves task-handling capability. We release the code and data at https://github.com/snowcatsmoking/SafeKeep .

</details>

### 37. Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning

📄 [arXiv](https://arxiv.org/abs/2606.20922) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62116)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`tool description poisoning`、`isolated planning`、`agent security`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Shanghao Shi、…、Ning Zhang

- 🎯 **研究动机**：跨工具描述投毒可操纵规划器可见的工具元数据引导 agent 轨迹，即使投毒工具从未被选用；现有提示注入防御迁移效果差
- 🔬 **研究方法**：提出 Tool-Guard 的隔离规划：检测到不对齐或可疑的工具调用即将该工具加入受影响列表隔离，切断投毒描述在后续步骤的持续影响，同时保留工具可用性
- 📌 **结论**：在 AgentDojo 与 ASB 基准上大幅降低攻击成功并保持高任务效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of external tools has substantially expanded the capabilities of large language model (LLM) agents, but it also introduces new attack surfaces beyond prompt injection. In particular, cross-tool description poisoning can manipulate planner-visible tool metadata to steer an agent’s trajectory, even if the poisoned tool itself is never chosen. To understand the effectiveness of existing defenses against this emerging threat, we first evaluate several prompt-injection defenses and find that they transfer poorly to cross-tool description poisoning. A key observation is that poisoned descriptions persist in the planning context across steps, enabling continuous influence over subsequent tool choices. Building on this insight, we propose Tool-Guard, a novel system-level defense based on a new concept called isolated planning, in which tool invocations that are detected as misaligned or suspicious cause the corresponding tool to be placed in a quarantined list (the influenced list ), breaking further influence from poisoned descriptions. With this influence isolated, the tool can continue to be used to support the task, enabling a robust defense that preserves legitimate tool utility. Experiments on the AgentDojo and ASB benchmarks show that Tool-Guard substantially reduces attack success while maintaining high task utility. Our code is available at https://github.com/shishishi123/Tool-Guard.

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

### 39. SOPE: Situation-Aware and Statistically Indistinguishable Privacy Exfiltration for MCP-enabled Agents

🎓 [Official](https://icml.cc/virtual/2026/poster/64028)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy attack`、`MCP`、`privacy leakage`、`empirical evaluation`、`data leakage`

👤 **作者**：Ruixiao Lin、Qingming Li、Jiahao Chen、Chunyi Zhou、Shouling Ji

- 🎯 **研究动机**：现有 MCP 隐私泄露攻击与 agent 工具使用情境错位且依赖刚性模板，模式可识别、易被现有防御拦截
- 🔬 **研究方法**：提出 SOPE 把任意良性 MCP 服务器改造成窃密变体：识别适配工具使用情境的隐私项、把隐私探测指令嵌入工具调用提示、经代码级修改实现零点击传输
- 📌 **结论**：324 个改造的真实服务器在 27216 个用例中攻击 4 个基准与 3 个商业 agent，在 9 个 SOTA 防御下仍高效鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) enables Large Language Model (LLM) agents to interact with external tools, but this extensibility introduces significant supply chain vulnerabilities that enable covert privacy exfiltration. Prior studies have revealed privacy leakage in MCP-enabled agents via indirect prompt injection; however, existing attacks are typically misaligned with the agent's tool-usage context and rely on rigid templates, resulting in recognizable patterns that are readily flagged by existing defenses. In this work, we exploit the observation that privacy exposure is inherently scenario-dependent, to associate certain privacy items with specific tools. We introduce SOPE, a Scenario-aware and zerO-click Privacy Exfiltration framework that transforms any benign MCP server into its privacy-exfiltrating variants. SOPE (1) identifies privacy items that are appropriate to the tool usage, (2) embeds privacy-probing instructions into tool-invocation prompts, and (3) achieves zero-click data transmission via code-level modifications. We evaluate SOPE across 27,216 test cases, where 324 SOPE -transformed real-world servers attacking four benchmark and three commercial agents with nine state-of-the-art defenses. Results demonstrate that SOPE remains highly effective and robust, highlighting critical protocol-level safety gaps in the agent ecosystem.

</details>

### 40. No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers
📄 [arXiv](https://arxiv.org/abs/2609.10854)　📅 2026-09


👤 **作者**：Zehua Zhang、…、Adam Doupe

**关键词**：`detection`、`no-box analysis`、`MCP server`、`indirect prompt injection`、`tool metadata`

- 🎯 **研究动机**：第三方审计闭源 MCP 服务器时无系统访问也无运行时交互，仅注册元数据可用
- 🔬 **研究方法**：no-box 漏洞分析范式：凭工具元数据推断所有可能实现共有的注入漏洞并给出利用假设
- 📌 **结论**：20 个 MCP 服务器 177 工具预测 94 个真实漏洞（98.9% recall），超 LLM 基线 84.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conventional vulnerability analysis relies on either system access or dynamic interaction, all of which may be unavailable to third-party analysts auditing closed-source, remotely hosted, critical in situ systems, or commercially gated software. Therefore, we propose a new paradigm of no-box vulnerability analysis in which neither access nor runtime interaction is available, and only functionality metadata is available. Such metadata defines the intended behavior of the system, including its inputs, outputs, and side effects, while constraining the space of implementations consistent with that behavior. We propose hypothesizing about vulnerabilities that exist across all possible implementations of a given system metadata, without observing or interacting with the target system. An analyst can later validate these hypotheses when additional access is available. We showcase the feasibility of no-box vulnerability analysis through implementing a prototype called MCPSEC, which audits Model Context Protocol (MCP) servers for indirect prompt injection vulnerabilities using only the tool metadata exposed at server registration time. We evaluate MCPSEC on 20 widely deployed MCP servers comprising 177 tools, among which human evaluators confirm 95 vulnerable tools. MCPSEC identified 143 tools as vulnerable, and for each vulnerable tool, it produced a hypothesized vulnerability along with exploitation technique. Using metadata alone, MCPSEC predicted 94 (98.9% recall) real verified vulnerabilities, compared against an LLM baseline with 80 (84.2% recall). Overall, our results introduce no-box vulnerability analysis as a new analysis paradigm and demonstrate its practical feasibility in realistic systems.

</details>

### 41. Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks

📄 [arXiv](https://arxiv.org/abs/2609.16098) · 🐙 [Code](https://github.com/Xiaoyan-Lisa/Defenses-for-Tool-Integrated-LLM-Agents-Against-Adversarial-Attacks.)　📅 2026-09

**关键词**：`defense`、`prompt injection`、`tool agent`、`anomaly detection`、`toolset restoration`

👤 **作者**：Xiaoyan Li、Yunli Wang

- 🎯 **研究动机**：工具集成 LLM agent 面临直接/间接 prompt 注入、memory 投毒与后门四类攻击，现有防御各自为战，缺少统一框架下可泛化的通用防线
- 🔬 **研究方法**：在统一框架下探索四类攻击的通用防御：Attacker Tool Filtering 用异常检测（如 Isolation Forest）识别并移除可疑工具；Normal Tool Recalling 是白盒方法，在规划前恢复 agent 原始工具集；辅以 CoT、self-reflection、task paraphrasing 等 prompt 级防御。在 4 个开源模型（Gemma2-9B、Qwen2-7B、LLaMA3-8B、LLaMA3.1-8B）与 3 个商用模型（GPT-3.5/4/5）上测 ASR 与任务成功率
- 📌 **结论**：多数设置下将 ASR 降到 0%，同时保持或提升原任务成功率；表明简单、模块化、多层的工具级防御即可显著强化工具集成 agent 的安全与鲁棒性。代码已开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strategies within a unified framework across these four attack types. We introduce two universal tool-based defenses: Attacker Tool Filtering, which uses anomaly detection (e.g., Isolation Forest) to identify and remove suspicious tools, and Normal Tool Recalling, a white-box method that restores the agent's original toolset prior to planning. Additionally, we incorporate prompt-based defenses: Chain-of-Thought prompting and self-reflection techniques to enhance reasoning and task paraphrasing to mitigate attacks. Experimental results across both four open-source LLMs (Gemma2-9B, Qwen2-7B, LLaMA3-8B, and LLaMA3.1-8B) and three proprietary LLMs (GPT-3.5, GPT-4, and GPT-5) show that our methods significantly reduce the Attack Success Rates (ASR), achieving 0% ASR in many settings, while preserving or even improving the original task success rate. These findings highlight the promise of simple, modular, multi-layered defenses for strengthening the security and robustness of tool-integrated LLM agents. The code is available at https://github.com/Xiaoyan-Lisa/Defenses-for-Tool-Integrated-LLM-Agents-Against-Adversarial-Attacks.

</details>
