# Scientific Domain Risk Evaluation

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究跨学科 scientific AI 的风险识别、benchmark 和防御，覆盖 chemistry、biology、medicine、pharmacology、physics、engineering 等知识场景，以及实验室规划和 scientific discovery Agent。核心问题是区分 safety knowledge、真实可执行风险、过度拒答与普通科学错误；评测还需把 risk dimension、subdiscipline、法规来源、tool-chain composition 和 external environment consequence 明确分开。以蛋白质、DNA 或 CBRN capability 为主要对象的工作进入专门的 Biosecurity 页面。

## 研究脉络

- **单学科起点：** MedSafetyBench 与 ChemSafetyBench 分别从医学伦理和化学属性、合法用途、合成任务定义 domain-specific safety。
- **多学科扩展：** SoSBench、SafeSci 和 SciRisk-Bench 将危险任务扩展到多个学科，并从单一 aggregate score 发展为 regulation grounding、safety-knowledge/risk separation 和 risk-dimension diagnosis。
- **风险强度度量：** SciHazard 把拒答以外的输出继续分解为 executability 与 net-new risk，避免把所有 compliant answer 视为同等有害。
- **Agent 与实验室：** SafeScientist、LABSHIELD 和 SciTrace 从文本回答推进到 tool use、multimodal hazard recognition 与跨步骤组合风险。
- **当前边界：** 文本 benchmark 仍不能替代真实实验 safety case；法规和知识会变化，science-specialized model 也可能因能力增强而更易提供危险细节，因此需要动态数据与 capability-aware evaluation。

## 跨学科 Benchmark 与 Risk Decomposition

### 1. Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.20960)　📅 2026-08

**关键词**：`benchmark`、`scientific knowledge drift`、`claim-level unlearning`、`outdated evidence`、`claim-level capability removal`、`structured knowledge`

👤 **作者**：Snigdha Paul、Manasi Patwardhan、Arman Cohan

- 🎯 **研究动机**：科学主张会被撤回、证伪或更新，而科学知识相互关联且持续演化，现有 instance-level 遗忘研究与评测无法覆盖 claim 级删除
- 🔬 **研究方法**：提出 Scientific Claim Unlearning 任务并构建 benchmark SciUnlearn，系统评测现有 unlearning 方法
- 📌 **结论**：现有方法无法有效消除 claim 级知识，多只实现表层抑制，需要面向结构化知识删除的专门方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while maintaining overall model utility. Existing studies primarily investigate instance-level forgetting; however, scientific claims introduce additional challenges because they are interconnected, and continually evolving. To address this gap, we introduce the task of Scientific Claim Unlearning and present a new benchmark, SciUnlearn. We show that current unlearning approaches are unable to effectively eliminate claim-level knowledge and often achieve only superficial suppression, highlighting the need for specialized methods designed for structured knowledge removal.

</details>

### 2. SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring

📄 [arXiv](https://arxiv.org/abs/2607.18665) · 🌐 [Project](https://anonymous.4open.science/r/DeharmScore-7B55)　📅 2026-07

**关键词**：`benchmark`、`DeHarm-Score`、`executability`、`net-new risk`

👤 **作者**：Chunxiao Li、…、Jing Shao

- 🎯 **研究动机**：现有科学安全基准依赖模板化查询与非接地 LLM-as-Judge，难以度量把危险知识转为可执行滥用指导的能力
- 🔬 **研究方法**：构建 SciHazard：2,400 危险问题+600 过度安全问题、12 学科、以受管控实体与记录在案失效为接地；DeHarm-Score 分解查询危险度、拒绝行为、可执行性（动态清单加权）与净新增风险（检索增强断言抽取+合成屏障核验）
- 📌 **结论**：DeHarm-Score 与专家标注一致性比最强基线提高 90.17%；31 个前沿模型评估中 deep research agent 平均分高出标准 LLM 32.3%，成为安全防御盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance. Existing benchmarks often rely on templated queries disconnected from real-world hazards, and employ LLM-as-a-Judge paradigms without domain grounding. To address this, we introduce SciHazard, a real-world-grounded benchmark for scientific risks and a dataset agnostic evaluation framework for measuring harmfulness. SciHazard contains 2400 hazardous questions and 600 oversafety questions across 12 disciplines, with both queries grounded in regulated entities and documented failure scenarios. To compute \textsc{DeHarm-Score} , we develop a decomposed evaluating procedure that combines query hazard severity, refusal behavior, and response-level risk. For non-refused responses, it further decomposes response-level harm into \textsc{Executability}, quantified via dynamic checklists with importance weighting, and \textsc{Net-new risk}, assessed through retrieval-augmented claim extraction and synthesis-barrier verification. An expert-validation study shows that \textsc{DeHarm-Score} improves agreement with expert annotations by 90.17\% over the strongest baseline. We benchmark 31 frontier LLMs and deep research agents in an extensive scientific safety evaluation. Notably, deep research agents yield 32.3\% higher mean \textsc{DeHarm-Score} than standard LLMs, exposing autonomous agents as a critical blind spot in current safety defenses. Code and dataset are available at https://anonymous.4open.science/r/DeharmScore-7B55.

</details>

### 3. SciRisk-Bench: A Risk-Dimension-Aware Benchmark for AI4Science Safety

📄 [arXiv](https://arxiv.org/abs/2606.18936)　📅 2026-06

**关键词**：`benchmark`、`risk dimension`、`subdiscipline diagnosis`、`implicit hazard`

👤 **作者**：Linghao Feng、…、Yi Zeng

- 🎯 **研究动机**：现有 AI4Science 安全数据集覆盖学科与任务形式，但底层风险维度未被明确规范
- 🔬 **研究方法**：构建 SciRisk-Bench：覆盖 7 学科、31 子学科、10 风险维度，从风险维度与学科双视角评估主流与科学向 LLM
- 📌 **结论**：实现科学模型不安全位置的细粒度诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly embedded in AI for Science (AI4Science) workflows, from scientific question answering and literature analysis to laboratory planning and autonomous discovery. This progress creates an urgent need for safety benchmarks that evaluate not only scientific competence, but also whether models recognize and avoid risks in high-stakes scientific contexts. Existing AI4Science safety datasets cover several disciplines and task formats, leaving the underlying risk dimensions underspecified. We introduce \textbf{SciRisk-Bench}, a benchmark designed to evaluate AI4Science safety from two complementary perspectives: explicit risk dimensions and scientific disciplines. SciRisk-Bench covers 7 disciplines, 31 subdisciplines and 10 risk dimensions. In the experimental section, we evaluate both mainstream LLMs and science-oriented LLMs across risk dimensions, disciplines, and sub-disciplines, enabling fine-grained diagnosis of where scientific models remain unsafe.

</details>

### 4. SafeSci: Safety Evaluation of Large Language Models in Science Domains and Beyond

📄 [arXiv](https://arxiv.org/abs/2603.01589) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61468)　📅 2026-03　🏷 ICML 2026

**关键词**：`benchmark`、`SafeSciBench`、`objective metric`、`oversafety`、`safety evaluation`、`empirical evaluation`

👤 **作者**：Xiangyang Zhu、…、Guangtao Zhai

- 🎯 **研究动机**：现有科学安全基准风险覆盖有限且依赖主观评估
- 🔬 **研究方法**：SafeSci 含 0.25M 样本的 SafeSciBench（区分安全知识与风险，用可确定性回答的客观题降偏差）与 1.5M 样本的 SafeSciTrain，评测 24 个先进 LLM
- 📌 **结论**：揭示当前模型的科学安全漏洞与不同程度的过度拒答；在 SafeSciTrain 上微调显著提升安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The success of large language models (LLMs) in scientific domains has heightened safety concerns, prompting numerous benchmarks to evaluate their scientific safety. Existing benchmarks often suffer from limited risk coverage and a reliance on subjective evaluation. To address these problems, we introduce SafeSci, a comprehensive framework for safety evaluation and enhancement in scientific contexts. SafeSci comprises SafeSciBench, a multi-disciplinary benchmark with 0.25M samples, and SafeSciTrain, a large-scale dataset containing 1.5M samples for safety enhancement. SafeSciBench distinguishes between safety knowledge and risk to cover extensive scopes and employs objective metrics such as deterministically answerable questions to mitigate evaluation bias. We evaluate 24 advanced LLMs, revealing critical vulnerabilities in current models. We also observe that LLMs exhibit varying degrees of excessive refusal behaviors on safety-related issues. For safety enhancement, we demonstrate that fine-tuning on SafeSciTrain significantly enhances the safety alignment of models. Finally, we argue that knowledge is a double-edged sword, and determining the safety of a scientific question should depend on specific context, rather than universally categorizing it as safe or unsafe. Our work provides both a diagnostic tool and a practical resource for building safer scientific AI systems.

</details>

### 5. ForesightSafety Bench: A Frontier Risk Evaluation and Governance Framework towards Safe AI

📄 [arXiv](https://arxiv.org/abs/2602.14135)　📅 2026-02

**关键词**：`benchmark`、`frontier risk`、`hierarchical taxonomy`、`dynamic governance`

👤 **作者**：Haibo Tong、…、Yi Zeng

- 🎯 **研究动机**：现有安全评测风险维度受限且检不出前沿风险，落后于前沿模型能力
- 🔬 **研究方法**：ForesightSafety Bench 从 7 大基础安全支柱扩展到具身、AI4Science、社会环境、灾难性风险及 8 个产业域共 94 个风险维度，评测二十余个主流大模型
- 📌 **结论**：前沿模型在 Risky Agentic Autonomy、AI4Science、具身与灾难性风险等支柱普遍存在安全缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Rapidly evolving AI exhibits increasingly strong autonomy and goal-directed capabilities, accompanied by derivative systemic risks that are more unpredictable, difficult to control, and potentially irreversible. However, current AI safety evaluation systems suffer from critical limitations such as restricted risk dimensions and failed frontier risk detection. The lagging safety benchmarks and alignment technologies can hardly address the complex challenges posed by cutting-edge AI models. To bridge this gap, we propose the "ForesightSafety Bench" AI Safety Evaluation Framework, beginning with 7 major Fundamental Safety pillars and progressively extends to advanced Embodied AI Safety, AI4Science Safety, Social and Environmental AI risks, Catastrophic and Existential Risks, as well as 8 critical industrial safety domains, forming a total of 94 refined risk dimensions. To date, the benchmark has accumulated tens of thousands of structured risk data points and assessment results, establishing a widely encompassing, hierarchically clear, and dynamically evolving AI safety evaluation framework. Based on this benchmark, we conduct systematic evaluation and in-depth analysis of over twenty mainstream advanced large models, identifying key risk patterns and their capability boundaries. The safety capability evaluation results reveals the widespread safety vulnerabilities of frontier AI across multiple pillars, particularly focusing on Risky Agentic Autonomy, AI4Science Safety, Embodied AI Safety, Social AI Safety and Catastrophic and Existential Risks. Our benchmark is released at https://github.com/Beijing-AISI/ForesightSafety-Bench. The project website is available at https://foresightsafety-bench.beijing-aisi.ac.cn/.

</details>

### 6. (Be Cautious!) Bio-Foundation Models Are Not Yet Robust to Biologically Plausible Perturbations and ML Transformations

🎓 [Official](https://icml.cc/virtual/2026/poster/62052)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`scientific AI`、`domain risk`、`capability evaluation`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Jinhao Duan、…、Tianlong Chen

- 🎯 **研究动机**：生物基础模型对小而真实的扰动鲁棒性未被探索，直接关系部署风险
- 🔬 **研究方法**：设计生物合理扰动（实验污染、策展伪影）与 ML 诱导变换（预处理、增强、嵌入选择）两类扰动套件，在 11 个 SOTA Bio-FM、7 个生物任务上做 2128 个实验
- 📌 **结论**：多数 Bio-FM 对两类扰动均脆弱；测量工具不可察觉的细微生物扰动可引发严重输出偏差，而 CryoDRGN 等 cryo-EM 模型在 worst-case 扰动下意外稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Though biological foundation models (Bio-FMs) have delivered strong performance across biomedical tasks, their robustness to small-but-real perturbations is underexplored. In this work, we ask: Are Bio-FMs robust for real-world use? What perturbations compromise their reliability? Our pilot study suggests that due to subtle biological data curation issues and common machine-learning (ML) processing choices, Bio-FMs suffer from two complementary perturbation sources: biologically plausible perturbations (capturing experimental corruptions and curation artifacts) and ML-induced transformations (capturing preprocessing, data augmentation, and embedding choices). Guided by this taxonomy, we design perturbation suites that mimic corruptions frequently encountered in biological experiments, and we systematically probe how transformations in the ML pipeline reshape model behavior. By conducting 2,128 experiments over 11 state-of-the-art Bio-FMs on 7 bio-tasks, we show that most Bio-FMs are vulnerable to both biological perturbations and ML transformations, revealing underappreciated robustness gaps that can directly translate into deployment risk. Interestingly, we find that subtle biological perturbations, which are often imperceptible to current measurement tools, can induce severe discrepancies in Bio-FM outputs and lead to critical failures, yet cryo-EM models (e.g., CryoDRGN) exhibit a surprising level of robustness even under worst-case perturbations. Our study for the first time surfaces critical failure modes and provides a principled perspective for evaluating the robustness of Bio-FMs.

</details>

### 7. Breaking Bad Molecules: Are MLLMs Ready for Structure-Level Molecular Detoxification?

📄 [arXiv](https://arxiv.org/abs/2506.10912) · 🌐 [Project](https://doi.org/10.1145/3770855.3818840)　📅 2025-06　🏷 KDD 2026

**关键词**：`benchmark`、`molecular safety`、`detoxification`、`dangerous capability`

👤 **作者**：Fei Lin、…、Fei-Yue Wang

- 🎯 **研究动机**：分子毒性修复（生成结构有效且毒性更低的替代分子）缺乏系统定义与基准
- 🔬 **研究方法**：构建 ToxiMol：11 个任务、660 个毒分子的基准，配机制感知 prompt 标注管线与整合毒性预测、可合成性、类药物性的 ToxiEval 评估链
- 📌 **结论**：43 个通用 MLLM 系统评估显示任务仍很难，但模型已展现毒性理解与结构感知编辑的潜力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Toxicity remains a leading cause of early-stage drug development failure. Despite advances in molecular design and property prediction, the task of molecular toxicity repair, generating structurally valid molecular alternatives with reduced toxicity, has not yet been systematically defined or benchmarked. To fill this gap, we introduce ToxiMol, the first benchmark task for general-purpose Multimodal Large Language Models (MLLMs) focused on molecular toxicity repair. We construct a standardized dataset covering 11 primary tasks and 660 representative toxic molecules spanning diverse mechanisms and granularities. We design a prompt annotation pipeline with mechanism-aware and task-adaptive capabilities, informed by expert toxicological knowledge. In parallel, we propose an automated evaluation framework, ToxiEval, which integrates toxicity endpoint prediction, synthetic accessibility, drug-likeness, and structural similarity into a high-throughput evaluation chain for repair success. We systematically assess 43 mainstream general-purpose MLLMs and conduct multiple ablation studies to analyze key issues, including evaluation metrics, candidate diversity, and failure attribution. Experimental results show that although current MLLMs still face significant challenges on this task, they begin to demonstrate promising capabilities in toxicity understanding, semantic constraint adherence, and structure-aware editing.

</details>

### 8. SoSBench: Benchmarking Safety Alignment on Six Scientific Domains

📄 [arXiv](https://arxiv.org/abs/2505.21605) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011737)　📅 2025-05　🏷 ICLR 2026

**关键词**：`benchmark`、`regulation grounding`、`hazardous knowledge`、`misuse scenario`

👤 **作者**：Fengqing Jiang、…、Radha Poovendran

- 🎯 **研究动机**：现有安全基准不需专业知识或任务低风险，无法评估知识密集型危险场景
- 🔬 **研究方法**：构建 SoSBench：从真实法规出发经 LLM 辅助演化管线，覆盖六个高危科学领域的 3,000 条滥用 prompt
- 📌 **结论**：前沿模型普遍泄露违规内容，Deepseek-R1 有害响应率 84.9%、GPT-4.1 达 50.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) exhibit advancing capabilities in complex tasks, such as reasoning and graduate-level question answering, yet their resilience against misuse, particularly involving scientifically sophisticated risks, remains underexplored. Existing safety benchmarks typically focus either on instructions requiring minimal knowledge comprehension (e.g., ``tell me how to build a bomb") or utilize prompts that are relatively low-risk (e.g., multiple-choice or classification tasks about hazardous content). Consequently, they fail to adequately assess model safety when handling knowledge-intensive, hazardous scenarios. To address this critical gap, we introduce SoSBench, a regulation-grounded, hazard-focused benchmark encompassing six high-risk scientific domains: chemistry, biology, medicine, pharmacology, physics, and psychology. The benchmark comprises 3,000 prompts derived from real-world regulations and laws, systematically expanded via an LLM-assisted evolutionary pipeline that introduces diverse, realistic misuse scenarios (e.g., detailed explosive synthesis instructions involving advanced chemical formulas). We evaluate frontier models within a unified evaluation framework using our SoSBench. Despite their alignment claims, advanced models consistently disclose policy-violating content across all domains, demonstrating alarmingly high rates of harmful responses (e.g., 84.9% for Deepseek-R1 and 50.3% for GPT-4.1). These results highlight significant safety alignment deficiencies and underscore urgent concerns regarding the responsible deployment of powerful LLMs.

</details>

### 9. ChemSafetyBench: Benchmarking LLM Safety on Chemistry Domain

📄 [arXiv](https://arxiv.org/abs/2411.16736)　📅 2024-11

**关键词**：`benchmark`、`chemical safety`、`synthesis risk`、`jailbreak scenario`、`physics.chem-ph`

👤 **作者**：Haochen Zhao、…、Mark Gerstein

- 🎯 **研究动机**：LLM 化学助手可能给出错误、非法或危险建议，缺乏系统评测基准
- 🔬 **研究方法**：ChemSafetyBench 覆盖化学性质查询、用途合法性、合成方法三类递进任务，3 万余样本含手工模板与越狱场景，配自动评估框架
- 📌 **结论**：SOTA LLM 在知识准确性与安全响应上均暴露关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancement and extensive application of large language models (LLMs) have been remarkable, including their use in scientific research assistance. However, these models often generate scientifically incorrect or unsafe responses, and in some cases, they may encourage users to engage in dangerous behavior. To address this issue in the field of chemistry, we introduce ChemSafetyBench, a benchmark designed to evaluate the accuracy and safety of LLM responses. ChemSafetyBench encompasses three key tasks: querying chemical properties, assessing the legality of chemical uses, and describing synthesis methods, each requiring increasingly deeper chemical knowledge. Our dataset has more than 30K samples across various chemical materials. We incorporate handcrafted templates and advanced jailbreaking scenarios to enhance task diversity. Our automated evaluation framework thoroughly assesses the safety, accuracy, and appropriateness of LLM responses. Extensive experiments with state-of-the-art LLMs reveal notable strengths and critical vulnerabilities, underscoring the need for robust safety measures. ChemSafetyBench aims to be a pivotal tool in developing safer AI technologies in chemistry. Our code and dataset are available at https://github.com/HaochenZhao/SafeAgent4Chem. Warning: this paper contains discussions on the synthesis of controlled chemicals using AI models.

</details>

### 10. MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2403.03744) · 🌐 [Project](https://doi.org/10.52202/079017-1054)　📅 2024-03　🏷 NeurIPS 2024

**关键词**：`benchmark`、`medical ethics`、`patient safety`、`safety fine-tuning`

👤 **作者**：Tessa Han、Aounon Kumar、Chirag Agarwal、Himabindu Lakkaraju

- 🎯 **研究动机**：LLM 医疗安全缺乏定义、评估与改进手段
- 🔬 **研究方法**：依据 AMA 医学伦理原则定义 medical safety，构建首个基准 MedSafetyBench 并用于评估与安全微调
- 📌 **结论**：公开医疗 LLM 均未达安全标准；用基准微调可提升医疗安全且保持医学性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) develop increasingly sophisticated capabilities and find applications in medical settings, it becomes important to assess their medical safety due to their far-reaching implications for personal and public health, patient safety, and human rights. However, there is little to no understanding of the notion of medical safety in the context of LLMs, let alone how to evaluate and improve it. To address this gap, we first define the notion of medical safety in LLMs based on the Principles of Medical Ethics set forth by the American Medical Association. We then leverage this understanding to introduce MedSafetyBench, the first benchmark dataset designed to measure the medical safety of LLMs. We demonstrate the utility of MedSafetyBench by using it to evaluate and improve the medical safety of LLMs. Our results show that publicly-available medical LLMs do not meet standards of medical safety and that fine-tuning them using MedSafetyBench improves their medical safety while preserving their medical performance. By introducing this new benchmark dataset, our work enables a systematic study of the state of medical safety in LLMs and motivates future work in this area, paving the way to mitigate the safety risks of LLMs in medicine. The benchmark dataset and code are available at https://github.com/AI4LIFE-GROUP/med-safety-bench.

</details>

### 11. SocraticChem: Physics-Grounded Socratic Inquiry for Safety-Critical Experimental Science

🌐 [Project](https://doi.org/10.1145/3770855.3818151)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`scientific AI safety`、`physics grounding`、`hazard interception`

- 🎯 **研究动机**：化学实验教学要求从错误中学习，但物理世界禁止某些错误；现有 LLM 导师重文本合理性轻物理现实，产生幻觉教学
- 🔬 **研究方法**：提出 SocraticChem 把辅导形式化为可验证的安全感知决策策略：构建 119 个实验、15.2K 物理接地教学轮的 SoChemDataset 并微调 SoChem-LLM，配套多维评测套件
- 📌 **结论**：SoChem-LLM 的 State Awareness 达 70.32%（GPT-4o 为 49.22%）、Safety Score 9.00（最好基线 8.00）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have emerged as a foundational technology for intelligent education. However, in safety-critical domains like chemistry experiments, current general models face a fundamental pedagogical paradox : effective inquiry requires students to learn from errors, but the physical world imposes strict safety constraints where certain errors are impermissible ( e.g., mixing reagents incorrectly could cause explosions). Moreover, existing LLM-based tutors typically prioritize textual plausibility over physical reality, leading to ''Hallucinated Pedagogy'' when applied to real-world experiments. To address this paradox, we propose SocraticChem, a physics-grounded framework that formalizes tutoring not as open-ended generation, but as a verifiable, safety-aware decision policy. SocraticChem guides students toward learning objectives while strictly intercepting potentially dangerous actions before they manifest physically, enabling error-driven learning without physical risk. To instantiate this framework, we first develop a multi-agent LLM pipeline to construct SoChemDataset, comprising 15.2K physically grounded teaching turns across 119 middle school chemistry experiments, and then fine-tune a SoChem-LLM on this dataset. Finally, we establish a comprehensive evaluation suite spanning physics-grounded verification, LLM-based assessment, and standard NLP benchmarks. Extensive experiments demonstrate that SoChem-LLM significantly outperforms baselines, achieving a State Awareness of 70.32% (surpassing GPT-4o's 49.22%) and a Safety Score of 9.00 (surpassing the best baseline of 8.00). These results confirm its capability to strictly enforce physical safety constraints while maintaining high-quality pedagogical guidance. Our code is available at: https://github.com/bsw-ili/socChem_final.

</details>

### 12. SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents

📄 [arXiv](https://arxiv.org/abs/2606.08234) · 🌐 [Project](https://opensciagent.github.io/SciTrace/)　📅 2026-06

**关键词**：`defense`、`scientific trajectory`、`tool-chain verifier`、`cumulative risk`

👤 **作者**：Tanush Swaminathan、Runmin Jiang、Letian Zhang、Min Xu

- 🎯 **研究动机**：科学 agent 的安全层与核心推理割裂：只检查管线输出，导致阶段安全信号丢失与单步无害工具序列组合成有害结果
- 🔬 **研究方法**：提出 SciTrace：Safety-Intrinsic Reasoning Loop 在 Thinker/Experimenter/Writer/Reviewer 阶段维护累积风险状态，Compositional Tool-Chain Verifier 执行前做轨迹级检查
- 📌 **结论**：240 个高危研究任务与 120 个工具风险任务、四个 backbone 上达 SOTA 安全性，发现 78.8% 单步监测器遗漏的组合式工具链逃逸

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based scientific agents have shown strong capacity for autonomous research, yet their safety layers remain structurally divorced from core reasoning: they inspect pipeline outputs rather than shaping the deliberation that produces them. This separation opens two failure modes: safety signals accumulated at one stage are discarded before the next, and sequences of individually benign tool calls can compose into harmful outcomes that no single-step filter detects. To address these challenges, we introduce \textbf{SciTrace}, a framework that weaves safety reasoning into every stage of the scientific agent pipeline. SciTrace couples two complementary mechanisms: a \textit{Safety-Intrinsic Reasoning Loop} (SIR) that maintains a cumulative risk state across the Thinker, Experimenter, Writer, and Reviewer stages through joint task-and-safety deliberation, and a \textit{Compositional Tool-Chain Verifier} (CTV) that performs trajectory-aware safety checks before execution, catching risks that surface only across multi-step tool sequences. Evaluated on 240 high-risk research tasks and 120 tool-related risk tasks spanning six scientific domains, SciTrace achieves state-of-the-art (\textbf{SOTA}) safety among compared frameworks across four backbone models: it consistently improves tool call safety and adversarial robustness while preserving scientific output quality, and it uncovers \textbf{78.8\%} of the compositional tool-chain escapes that single-step monitors miss. The project website is available at https://opensciagent.github.io/SciTrace/.

</details>

### 13. LABSHIELD: A Multimodal Benchmark for Safety-Critical Reasoning and Planning in Scientific Laboratories

📄 [arXiv](https://arxiv.org/abs/2603.11987)　📅 2026-03

**关键词**：`benchmark`、`laboratory safety`、`multimodal planning`、`hazard recognition`

👤 **作者**：Qianpu Sun、…、Shanghang Zhang

- 🎯 **研究动机**：自驱实验室中危险物质与精密设备使规划错误不可逆，具身 agent 的安全意识缺乏定义与评测
- 🔬 **研究方法**：LABSHIELD 依据 OSHA 与 GHS 标准构建 164 项操作任务的多视角基准，双轨评测 20 个专有、9 个开源与 3 个具身模型
- 📌 **结论**：模型在专业实验室半开放问答上较通用 MCQ 平均下降 32.0%，危害解读与安全感知规划尤为薄弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial intelligence is increasingly catalyzing scientific automation, with multimodal large language model (MLLM) agents evolving from lab assistants into self-driving lab operators. This transition imposes stringent safety requirements on laboratory environments, where fragile glassware, hazardous substances, and high-precision laboratory equipment render planning errors or misinterpreted risks potentially irreversible. However, the safety awareness and decision-making reliability of embodied agents in such high-stakes settings remain insufficiently defined and evaluated. To bridge this gap, we introduce LABSHIELD, a realistic multi-view benchmark designed to assess MLLMs in hazard identification and safety-critical reasoning. Grounded in U.S. Occupational Safety and Health Administration (OSHA) standards and the Globally Harmonized System (GHS), LABSHIELD establishes a rigorous safety taxonomy spanning 164 operational tasks with diverse manipulation complexities and risk profiles. We evaluate 20 proprietary models, 9 open-source models, and 3 embodied models under a dual-track evaluation framework. Our results reveal a systematic gap between general-domain MCQ accuracy and Semi-open QA safety performance, with models exhibiting an average drop of 32.0% in professional laboratory scenarios, particularly in hazard interpretation and safety-aware planning. These findings underscore the urgent necessity for safety-centric reasoning frameworks to ensure reliable autonomous scientific experimentation in embodied laboratory contexts. The full dataset will be released soon.

</details>

### 14. SafeScientist: Enhancing AI Scientist Safety for Risk-Aware Scientific Discovery

🎓 [Official](https://aclanthology.org/2025.emnlp-main.116/)　📅 2025-11　🏷 EMNLP 2025

**关键词**：`defense`、`scientific agent`、`tool monitoring`、`ethical reviewer`

👤 **作者**：Kunlun Zhu、…、Jiaxuan You

- 🎯 **研究动机**：LLM agent 加速科学发现自动化的同时引发伦理与安全隐忧
- 🔬 **研究方法**：提出 SafeScientist：主动拒绝不伦理高风险任务，集成提示、协作与工具使用监控及伦理审查组件；配套 SciSafetyBench（6 域 240 个高危任务、30 个工具、120 个工具风险任务）
- 📌 **结论**：相比传统 AI 科学家框架安全表现提升 35% 且不牺牲产出质量，安全流水线对多样对抗攻击稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in large language model (LLM) agents have significantly accelerated scientific discovery automation, yet concurrently raised critical ethical and safety concerns. To systematically address these challenges, we introduce SafeScientist, an innovative AI scientist framework explicitly designed to enhance safety and ethical responsibility in AI-driven scientific exploration. SafeScientist proactively refuses ethically inappropriate or high-risk tasks and rigorously emphasizes safety throughout the research process. To achieve comprehensive safety oversight, we integrate multiple defensive mechanisms, including prompt monitoring, agent-collaboration monitoring, tool-use monitoring, and an ethical reviewer component. Complementing SafeScientist, we propose SciSafetyBench, a novel benchmark specifically designed to evaluate AI safety in scientific contexts, comprising 240 high-risk scientific tasks across 6 domains, alongside 30 specially designed scientific tools and 120 tool-related risk tasks. Extensive experiments demonstrate that SafeScientist significantly improves safety performance by 35% compared to traditional AI scientist frameworks, without compromising scientific output quality. Additionally, we rigorously validate the robustness of our safety pipeline against diverse adversarial attack methods, further confirming the effectiveness of our integrated approach. The code and data will be available at https://github.com/ulab-uiuc/SafeScientist. Warning: this paper contains example data that may be offensive or harmful.

</details>
