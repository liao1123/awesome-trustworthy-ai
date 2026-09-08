# CBRN and Biosecurity

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 AI 对 chemical、biological、radiological、nuclear risk 的 capability uplift 与防护，重点覆盖 biology agent、protein foundation model、DNA language model、sequence generation 和 nucleic-acid synthesis screening。评测不能只观察自然语言 refusal：模型可能拒绝显式请求，却通过 tool use、code 或可行生物序列产生实际风险。防御因此需要同时处理 model alignment、domain guardrail、sequence screening、provenance watermark、controlled access 和现实实验验证。

## 研究脉络

- **知识代理指标：** WMDP 等 benchmark 先用 bio、chem 和 cyber knowledge 测量 hazardous capability，但 multiple-choice score 不能直接代表现实 uplift。
- **领域模型 Red Team：** SafeProtein 与 GeneBreaker 分别把攻击推进到 protein 和 DNA foundation model，通过 multimodal prompt、beam search、pathogenicity signal 与 bioinformatics tool 检查 sequence-level vulnerability。
- **功能风险度量：** SPIKE-Bench 不再把 refusal 当作终点，而是继续检查 amino-acid sequence 的 biological plausibility 与 predicted toxicity；Early Warning work 进一步把 computational red team 接到受控 wet-lab validation。
- **Agentic capability：** ABC-Bench 评测 Agent 编写 liquid-handling code、设计 DNA assembly 和规避 synthesis screening，显示 published protocol 可以把文本知识转成现实实验动作。
- **纵深防御：** BioSafe-Guard、DNA/protein watermark、pretraining filtering、classifier guard 和 synthesis screening 分别覆盖输出拦截、provenance、结构性知识控制与供应链检查；单层拒答不能构成完整 biosecurity case。

## Bio-Capability 与 Agentic Uplift

### 1. An Early Warning of Emerging Biosecurity Risks in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2607.18056)　📅 2026-07

**关键词**：`attack`、`bio red team`、`wet-lab validation`、`capability uplift`、`q-bio.GN`

👤 **作者**：Zhida He、…、Ziyuan Zhou

- 🎯 **研究动机**：前沿 LLM 的生物能力增长可能超前于防护，需要计算到物理的全链条风险评估
- 🔬 **研究方法**：开发 Intern-BioBreaker 生物红队模型与计算-物理耦合框架：生成定向越狱提示测试安全敏感任务与序列级输出，并对选定序列做 DNA 合成、宿主表达与正交蛋白验证
- 📌 **结论**：开源与闭源前沿模型均现广泛生物越狱漏洞（部分任务级 ASR 近 100%）；GPT-5.5 可被诱导生成具致病潜力的修饰病毒候选序列且蛋白显示更强受体结合；模型设计经湿实验证实可物理实现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier large language models (LLMs) are increasingly integrated into scientific workflows, yet their growing biological capabilities may outpace current safeguards. To assess the biological risks of frontier models, we develop Intern-BioBreaker, a specialized bio-red-teaming model, together with an integrated computational-to-physical framework that couples model-level stress testing with wet-lab validation. Within this framework, Intern-BioBreaker generates targeted jailbreak prompts to test whether aligned models can be induced to provide operational guidance for safety-sensitive biological tasks or produce sequence-level outputs with potentially harmful properties. Selected sequence outputs are then carried forward for DNA synthesis, host expression, and orthogonal protein verification to assess whether model-generated designs can yield the intended biological products. Our evaluation reveals a concerning gap between text-level safeguards and the risks posed by capable scientific models: (i) Intern-BioBreaker outperforms baseline attack models and reveals widespread bio-risk jailbreak vulnerabilities across both open-weight and proprietary frontier LLMs, with several targets reaching near-saturated or 100% task-level attack success rate (ASR); (ii) in sequence-level case studies, GPT-5.5 can be induced to generate modified viral candidate sequences with pathogenic potential; the corresponding translated proteins may exhibit even stronger receptor-binding affinity and thus enhanced infection potential; and (iii) end-to-end verification shows that selected model-generated biological designs are not merely textual artifacts, but can be physically realized under controlled experimental settings. These findings underscore the need for stronger biological red-teaming, nucleic acid synthesis screening, and safety mechanisms that keep pace with model capabilities.

</details>

### 2. ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity

📄 [arXiv](https://arxiv.org/abs/2606.11150) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60590)　📅 2026-06　🏷 ICML 2026

**关键词**：`benchmark`、`bio agent`、`DNA assembly`、`screening evasion`、`agent safety`、`empirical evaluation`

👤 **作者**：Andrew Bo Liu、Samira Nedungadi、Bryce Cai、Alex Kleinman、Harmon Bhasin、Seth Donoughe

- 🎯 **研究动机**：LLM agent 获得真实生物能力，改变生物安全风险格局，需要可测量的能力基准
- 🔬 **研究方法**：构建 ABC-Bench，评估液体处理机器人代码编写、DNA 片段体外组装设计与 DNA 合成筛查规避等双用途任务，并与专家人类基线比较
- 📌 **结论**：全部被测 agent 在三项任务上超过人类中位基线；wet-lab 验证中 o4-mini-high 生成的脚本在 OpenTrons 机器人上成功组装出预期序列 DNA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilities Benchmark (ABC-Bench), a suite of tasks to measure agentic biosecurity-relevant capabilities. ABC-Bench evaluates LLM agents on both benign and dual-use biology tasks: writing code to operate liquid handling robots, designing DNA fragments for in vitro assembly, and evading DNA synthesis screening. These tasks require a combination of biology and software expertise. All tested LLM agents outperformed the median expert human baseliner on all three tasks. Agents performed highly on tasks drawing on published knowledge and well-documented protocols, and more weakly on a task requiring novel bioinformatics reasoning. In three wet-lab validation experiments, we found that OpenAI's o4-mini-high produced scripts that, when run on an OpenTrons liquid handling robot, successfully assembled DNA with expected sequences.

</details>

### 3. Generative AI for Biosciences: Emerging Threats and Roadmap to Biosecurity

📄 [arXiv](https://arxiv.org/abs/2510.15975)　📅 2025-10

**关键词**：`analysis`、`bioscience misuse`、`lifecycle defense`、`adaptive governance`、`q-bio.BM`

👤 **作者**：Zaixi Zhang、…、Mengdi Wang

- 🎯 **研究动机**：GenAI 降低生物误用门槛，可生成合成病毒蛋白或毒素，而现有 guardrail 脆弱且监管缺口明显
- 🔬 **研究方法**：综述生物科学 GenAI 的越狱、隐私与自主 agent 双用威胁向量，基于 130 位专家访谈分析监管缺口并提出多层防御路线图
- 📌 **结论**：约 76% 专家担忧生物学 AI 误用、74% 呼吁新治理框架；提出数据过滤、伦理对齐与实时监测的全生命周期安全蓝图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid adoption of generative artificial intelligence (GenAI) in the biosciences is transforming biotechnology, medicine, and synthetic biology. Yet this advancement is intrinsically linked to new vulnerabilities, as GenAI lowers the barrier to misuse and introduces novel biosecurity threats, such as generating synthetic viral proteins or toxins. These dual-use risks are often overlooked, as existing safety guardrails remain fragile and can be circumvented through deceptive prompts or jailbreak techniques. In this Perspective, we first outline the current state of GenAI in the biosciences and emerging threat vectors ranging from jailbreak attacks and privacy risks to the dual-use challenges posed by autonomous AI agents. We then examine urgent gaps in regulation and oversight, drawing on insights from 130 expert interviews across academia, government, industry, and policy. A large majority ($\approx 76$\%) expressed concern over AI misuse in biology, and 74\% called for the development of new governance frameworks. Finally, we explore technical pathways to mitigation, advocating a multi-layered approach to GenAI safety. These defenses include rigorous data filtering, alignment with ethical principles during development, and real-time monitoring to block harmful requests. Together, these strategies provide a blueprint for embedding security throughout the GenAI lifecycle. As GenAI becomes integrated into the biosciences, safeguarding this frontier requires an immediate commitment to both adaptive governance and secure-by-design technologies.

</details>

### 4. A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.02684) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-08　🏷 COLM 2026

**关键词**：`benchmark`、`SPIKE-Bench`、`functional harmfulness`、`BioSafe-Guard`、`biosecurity`、`toxin design`

👤 **作者**：Shu Quan、…、Jiaming Ji

- 🎯 **研究动机**：现有 LLM 安全评测停留在自然语言层面，无法判断生成的氨基酸序列是生物乱码还是计算风险信号
- 🔬 **研究方法**：SPIKE-Bench 耦合 631 条毒素设计提示与三阶段 SPIKE 漏斗（合规、生物合理性、预测毒性），产出 Functional Harmfulness Rate；并提供 BioSafe-Guard 分类器
- 📌 **结论**：32 个 LLM 审计显示 FHR 最高达 50.7% 且主要由生物生成能力而非安全对齐驱动，拒答率无法预测功能风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are accelerating biological research, yet this same capability poses a critical biosecurity threat: models that assist in protein engineering can equally be prompted to generate predicted toxin-like sequences, potentially lowering the barrier to biological misuse. Current safety evaluations, however, operate in natural language and cannot determine whether a model-generated amino acid sequence is biological gibberish or a computational risk signal. To address this evaluation blind spot, we introduce SPIKE-Bench, coupling 631 curated toxin-design prompts across seven functional categories with the SPIKE funnel, a three-stage protocol that filters output through compliance, biological plausibility, and predicted toxicity, producing stage-level diagnostics and an aggregate function-aware metric: the Functional Harmfulness Rate (FHR). An audit of 32 LLMs reveals that most models freely comply with toxin-design requests; FHR is driven primarily by biological generation capability rather than safety alignment, reaching 50.7%; and Refusal Rate fails to predict functional risk. As a first step toward mitigation, we provide BioSafe-Guard, a domain-specialized classifier that substantially reduces predicted functional risk while preserving benign utility. We release SPIKE-Bench and BioSafe-Guard at https://github.com/PKU-Alignment/SPIKE-Bench to support more rigorous biosecurity evaluation of LLMs.

</details>

### 5. SafeProtein: Red-Teaming Framework and Benchmark for Protein Foundation Models

📄 [arXiv](https://arxiv.org/abs/2509.03487)　📅 2025-09

**关键词**：`attack`、`protein foundation model`、`heuristic beam search`、`sequence misuse`、`q-bio.BM`、`q-bio.QM`

👤 **作者**：Jigang Fan、Zhenghong Zhou、Ruofan Jin、Le Cong、Mengdi Wang、Zaixi Zhang

- 🎯 **研究动机**：蛋白质基础模型缺乏系统红队，生成具生物安全风险蛋白的滥用风险未评估
- 🔬 **研究方法**：提出 SafeProtein：多模态 prompt 工程加启发式束搜索设计攻击，配人工构建的 SafeProtein-Bench 与完整评估协议
- 📌 **结论**：对 SoTA 蛋白质模型实现持续越狱，ESM3 的 ASR 达 70%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Proteins play crucial roles in almost all biological processes. The advancement of deep learning has greatly accelerated the development of protein foundation models, leading to significant successes in protein understanding and design. However, the lack of systematic red-teaming for these models has raised serious concerns about their potential misuse, such as generating proteins with biological safety risks. This paper introduces SafeProtein, the first red-teaming framework designed for protein foundation models to the best of our knowledge. SafeProtein combines multimodal prompt engineering and heuristic beam search to systematically design red-teaming methods and conduct tests on protein foundation models. We also curated SafeProtein-Bench, which includes a manually constructed red-teaming benchmark dataset and a comprehensive evaluation protocol. SafeProtein achieved continuous jailbreaks on state-of-the-art protein foundation models (up to 70% attack success rate for ESM3), revealing potential biological safety risks in current protein foundation models and providing insights for the development of robust security protection technologies for frontier models. The codes will be made publicly available at https://github.com/jigang-fan/SafeProtein.

</details>

### 6. GeneBreaker: Jailbreak Attacks against DNA Language Models with Pathogenicity Guidance

📄 [arXiv](https://arxiv.org/abs/2505.23839) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010887)　📅 2025-05　🏷 ICLR 2026

**关键词**：`attack`、`DNA language model`、`pathogenicity guidance`、`sequence jailbreak`、`q-bio.GN`

👤 **作者**：Zaixi Zhang、Zhenghong Zhou、Ruofan Jin、Le Cong、Mengdi Wang

- 🎯 **研究动机**：DNA 基础模型可设计合成功能序列乃至基因组，其越狱生成病原样序列的风险未被系统评估
- 🔬 **研究方法**：提出 GeneBreaker：LLM agent 设计高同源越狱 prompt，PathoLM 与 log-probability 引导束搜索，BLAST 对比人类病原库判定越狱
- 📌 **结论**：对 Evo 系列模型六类病毒持续越狱，Evo2-40B ASR 达 60%；模型规模越大双重用途风险越高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

DNA, encoding genetic instructions for almost all living organisms, fuels groundbreaking advances in genomics and synthetic biology. Recently, DNA Foundation Models have achieved success in designing synthetic functional DNA sequences, even whole genomes, but their susceptibility to jailbreaking remains underexplored, leading to potential concern of generating harmful sequences such as pathogens or toxin-producing genes. In this paper, we introduce GeneBreaker, the first framework to systematically evaluate jailbreak vulnerabilities of DNA foundation models. GeneBreaker employs (1) an LLM agent with customized bioinformatic tools to design high-homology, non-pathogenic jailbreaking prompts, (2) beam search guided by PathoLM and log-probability heuristics to steer generation toward pathogen-like sequences, and (3) a BLAST-based evaluation pipeline against a curated Human Pathogen Database (JailbreakDNABench) to detect successful jailbreaks. Evaluated on our JailbreakDNABench, GeneBreaker successfully jailbreaks the latest Evo series models across 6 viral categories consistently (up to 60\% Attack Success Rate for Evo2-40B). Further case studies on SARS-CoV-2 spike protein and HIV-1 envelope protein demonstrate the sequence and structural fidelity of jailbreak output, while evolutionary modeling of SARS-CoV-2 underscores biosecurity risks. Our findings also reveal that scaling DNA foundation models amplifies dual-use risks, motivating enhanced safety alignment and tracing mechanisms. Our code is at https://github.com/zaixizhang/GeneBreaker.

</details>

### 7. Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

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

### 8. Securing the Language of Life: Inheritable Watermarks from DNA Language Models to Proteins

📄 [arXiv](https://arxiv.org/abs/2509.18207) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c85aaa3996e1dbc35646a17893a54495-Abstract-Conference.html)　📅 2025-09　🏷 NeurIPS 2025

**关键词**：`defense`、`DNA watermark`、`protein inheritance`、`sequence provenance`、`q-bio.GN`

👤 **作者**：Zaixi Zhang、Ruofan Jin、Le Cong、Mengdi Wang

- 🎯 **研究动机**：DNA 语言模型的双用途风险（病原体乃至生物武器）需要可追踪设计序列的水印机制
- 🔬 **研究方法**：提出 DNAMark 以同义密码子替换嵌入水印保持功能，CentralMark 借蛋白质嵌入实现跨中心法则、从 DNA 遗传到蛋白的水印
- 📌 **结论**：多条件下 F1 检测分超 0.85，与真值序列相似性超 60%、简并度低于 15%，CRISPR-Cas9 案例验证实用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

DNA language models have revolutionized our ability to understand and design DNA sequences--the fundamental language of life--with unprecedented precision, enabling transformative applications in therapeutics, synthetic biology, and gene editing. However, this capability also poses substantial dual-use risks, including the potential for creating pathogens, viruses, and even bioweapons. To address these biosecurity challenges, we introduce two innovative watermarking techniques to reliably track the designed DNA: DNAMark and CentralMark. DNAMark employs synonymous codon substitutions to embed watermarks in DNA sequences while preserving the original function. CentralMark further advances this by creating inheritable watermarks that transfer from DNA to translated proteins, leveraging protein embeddings to ensure detection across the central dogma. Both methods utilize semantic embeddings to generate watermark logits, enhancing robustness against natural mutations, synthesis errors, and adversarial attacks. Evaluated on our therapeutic DNA benchmark, DNAMark and CentralMark achieve F1 detection scores above 0.85 under various conditions, while maintaining over 60% sequence similarity to ground truth and degeneracy scores below 15%. A case study on the CRISPR-Cas9 system underscores CentralMark's utility in real-world settings. This work establishes a vital framework for securing DNA language models, balancing innovation with accountability to mitigate biosecurity risks.

</details>

### 9. A call for built-in biosecurity safeguards for generative AI tools

🌐 [Project](https://www.nature.com/articles/s41587-025-02650-8)　📅 2025-04

**关键词**：`analysis`、`built-in safeguard`、`sequence screening`、`dual-use biology`

- 🎯 **研究动机**：生成式生物学工具可产出库外新pathogen、toxin或规避筛查的分子，仅靠用户政策不足
- 🔬 **研究方法**：主张将序列筛查等biosecurity safeguard内建到生成工具与合成供应链
- 📌 **结论**：需要模型、synthesis provider与治理机构协同的多层防护