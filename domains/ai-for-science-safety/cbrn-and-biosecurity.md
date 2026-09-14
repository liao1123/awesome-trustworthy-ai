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

### 10. LLMs Outperform Experts on Challenging Biology Benchmarks

📄 [arXiv](https://arxiv.org/abs/2505.06108)　📅 2025-05

**关键词**：`analysis`、`biology capability`、`benchmark saturation`、`expert baseline`

👤 **作者**：Lennart Justen

- 🎯 **研究动机**：前沿 LLM 在生物基准上的进步速度与专家水平的关系缺乏跨模型、跨时间的系统测量
- 🔬 **研究方法**：对 2022-11 至 2025-04 发布的 27 个前沿模型在分子生物学、遗传学、克隆、病毒学与生物安全八个基准上各做十次独立评测
- 📌 **结论**：Virology Capabilities Test 文本子集榜首成绩提升超 4 倍，o3 已两倍于专家病毒学家；多个模型在 GPQA/WMDP/LAB-Bench 生物子集达到或超过专家水平，而 PubMedQA 等出现远低于 100% 的平台期提示基准饱和

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This study systematically evaluates 27 frontier Large Language Models on eight biology benchmarks spanning molecular biology, genetics, cloning, virology, and biosecurity. Models from major AI developers released between November 2022 and April 2025 were assessed through ten independent runs per benchmark. The findings reveal dramatic improvements in biological capabilities. Top model performance increased more than 4-fold on the challenging text-only subset of the Virology Capabilities Test over the study period, with OpenAI's o3 now performing twice as well as expert virologists. Several models now match or exceed expert-level performance on other challenging benchmarks, including the biology subsets of GPQA and WMDP and LAB-Bench CloningScenarios. Contrary to expectations, chain-of-thought did not substantially improve performance over zero-shot evaluation, while extended reasoning features in o3-mini and Claude 3.7 Sonnet typically improved performance as predicted by inference scaling. Benchmarks such as PubMedQA and the MMLU and WMDP biology subsets exhibited performance plateaus well below 100%, suggesting benchmark saturation and errors in the underlying benchmark data. The analysis highlights the need for more sophisticated evaluation methodologies as AI systems continue to advance.

</details>

### 11. Contemporary AI Foundation Models Increase Biological Weapons Risk

📄 [arXiv](https://arxiv.org/abs/2506.13798)　📅 2025-06

**关键词**：`analysis`、`tacit knowledge assumption`、`bioweapon uplift`、`evaluation critique`

👤 **作者**：Roger Brent、T. Greg McKelvey

- 🎯 **研究动机**：现有前沿模型生物安全评估可能系统性低估风险，其两大假设（开发生物武器需 tacit knowledge、基准可靠）存在缺陷
- 🔬 **研究方法**：用无正式专业背景者完成复杂技术任务的历史案例（含 2011 年挪威极端分子合成爆炸物）反驳 tacit knowledge 假设，梳理可用文字传达的"成功要素"框架并应用到先进模型
- 📌 **结论**：Llama 3.1 405B、ChatGPT-4o 与 Claude 3.5 Sonnet 能准确指导用户从商业合成 DNA 复活活脊髓灰质炎病毒，直接挑战"当前模型风险极低"的论断；呼吁改进基准并警告实施窗口可能已经关闭

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of artificial intelligence has raised concerns about its potential to facilitate biological weapons development. We argue existing safety assessments of contemporary foundation AI models underestimate this risk, largely due to flawed assumptions and inadequate evaluation methods. First, assessments mistakenly assume biological weapons development requires tacit knowledge, or skills gained through hands-on experience that cannot be easily verbalized. Second, they rely on imperfect benchmarks that overlook how AI can uplift both nonexperts and already-skilled individuals. To challenge the tacit knowledge assumption, we examine cases where individuals without formal expertise, including a 2011 Norwegian ultranationalist who synthesized explosives, successfully carried out complex technical tasks. We also review efforts to document pathogen construction processes, highlighting how such tasks can be conveyed in text. We identify "elements of success" for biological weapons development that large language models can describe in words, including steps such as acquiring materials and performing technical procedures. Applying this framework, we find that advanced AI models Llama 3.1 405B, ChatGPT-4o, and Claude 3.5 Sonnet can accurately guide users through the recovery of live poliovirus from commercially obtained synthetic DNA, challenging recent claims that current models pose minimal biosecurity risk. We advocate for improved benchmarks, while acknowledging the window for meaningful implementation may have already closed.

</details>

### 12. Quantifying CBRN Risk in Frontier Models

📄 [arXiv](https://arxiv.org/abs/2510.21133)　📅 2025-10

**关键词**：`benchmark`、`CBRN evaluation`、`Deep Inception`、`superficial filtering`

👤 **作者**：Divyanshu Kumar、Nitin Aravind Birur、Tanay Baswa、Sahil Agarwal、Prashanth Harshangi

- 🎯 **研究动机**：前沿 LLM 的 CBRN 武器知识双用途风险缺乏对商用模型的系统性多层攻击评测
- 🔬 **研究方法**：用三层攻击方法对 10 个商用 LLM 评测自建 200 条 CBRN 提示与 FORTRESS 180 条子集
- 📌 **结论**：Deep Inception 攻击成功率 86.0% vs 直接请求 33.8%，证明过滤机制表层化；模型安全表现从 2%（claude-opus-4）到 96%（mistral-small-latest）剧变，八个模型在增强危险材料性质请求上漏洞超 70%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier Large Language Models (LLMs) pose unprecedented dual-use risks through the potential proliferation of chemical, biological, radiological, and nuclear (CBRN) weapons knowledge. We present the first comprehensive evaluation of 10 leading commercial LLMs against both a novel 200-prompt CBRN dataset and a 180-prompt subset of the FORTRESS benchmark, using a rigorous three-tier attack methodology. Our findings expose critical safety vulnerabilities: Deep Inception attacks achieve 86.0\% success versus 33.8\% for direct requests, demonstrating superficial filtering mechanisms; Model safety performance varies dramatically from 2\% (claude-opus-4) to 96\% (mistral-small-latest) attack success rates; and eight models exceed 70\% vulnerability when asked to enhance dangerous material properties. We identify fundamental brittleness in current safety alignment, where simple prompt engineering techniques bypass safeguards for dangerous CBRN information. These results challenge industry safety claims and highlight urgent needs for standardized evaluation frameworks, transparent safety metrics, and more robust alignment techniques to mitigate catastrophic misuse risks while preserving beneficial capabilities.

</details>

### 13. Biothreat Benchmark Generation Framework for Evaluating Frontier AI Models I: The Task-Query Architecture

📄 [arXiv](https://arxiv.org/abs/2512.08130)　📅 2025-12

**关键词**：`benchmark`、`biothreat schema`、`task-query architecture`、`operational risk factor`

👤 **作者**：Gary Ackerman、…、Anna Wetzel

- 🎯 **研究动机**：现有 LLM 生物安全基准忽视行为者能力差异与操作性（而非纯技术）风险因素
- 🔬 **研究方法**：提出 Biothreat Benchmark Generation（BBG）框架第一部分：构建细菌生物威胁类别-要素-任务的层级 Schema 并派生任务对齐查询
- 📌 **结论**：Bacterial Biothreat Schema 提供可复用结构，在多聚合层级刻画生物对手的完整技术与操作需求并覆盖宽谱行为者能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Both model developers and policymakers seek to quantify and mitigate the risk of rapidly-evolving frontier artificial intelligence (AI) models, especially large language models (LLMs), to facilitate bioterrorism or access to biological weapons. An important element of such efforts being the development of model benchmarks that can assess the biosecurity risk posed by a particular model. This paper describes the first component of a novel Biothreat Benchmark Generation (BBG) Framework. The BBG approach is designed to help model developers and evaluators reliably measure and assess the biosecurity risk uplift and general harm potential of existing and future AI models, while accounting for key aspects of the threat itself that are often overlooked in other benchmarking efforts, including different actor capability levels, and operational (in addition to purely technical) risk factors. As a pilot, the BBG is first being developed to address bacterial biological threats only. The BBG is built upon a hierarchical structure of biothreat categories, elements and tasks, which then serves as the basis for the development of task-aligned queries. This paper outlines the development of this biothreat task-query architecture, which we have named the Bacterial Biothreat Schema, while future papers will describe follow-on efforts to turn queries into model prompts, as well as how the resulting benchmarks can be implemented for model evaluation. Overall, the BBG Framework, including the Bacterial Biothreat Schema, seeks to offer a robust, re-usable structure for evaluating bacterial biological risks arising from LLMs across multiple levels of aggregation, which captures the full scope of technical and operational requirements for biological adversaries, and which accounts for a wide spectrum of biological adversary capabilities.

</details>

### 14. Biothreat Benchmark Generation Framework for Evaluating Frontier AI Models II: Benchmark Generation Process

📄 [arXiv](https://arxiv.org/abs/2512.08451)　📅 2025-12

**关键词**：`benchmark`、`benchmark generation`、`uplift diagnosticity`、`B3 dataset`

👤 **作者**：Gary Ackerman、…、Noah Sheinbaum

- 🎯 **研究动机**：把任务-查询架构转化为可实施的生物安全模型基准需要系统化生成与质控流程
- 🔬 **研究方法**：BBG 框架第二部分：网络提示生成、红队与既有基准语料挖掘三路产出 7,000+ 候选，经去重、uplift 诊断性评估与质量控制筛出 1,010 个最终基准
- 📌 **结论**：Bacterial Biothreat Benchmark（B3）确保基准对 uplift 具诊断性、直接关联生物安全威胁并对齐更大的生物安全分析架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The potential for rapidly-evolving frontier artificial intelligence (AI) models, especially large language models (LLMs), to facilitate bioterrorism or access to biological weapons has generated significant policy, academic, and public concern. Both model developers and policymakers seek to quantify and mitigate any risk, with an important element of such efforts is the development of model benchmarks that can assess the biosecurity risk posed by a particular model. This paper, the second in a series of three, describes the second component of a novel Biothreat Benchmark Generation (BBG) framework: the generation of the Bacterial Biothreat Benchmark (B3) dataset. The development process involved three complementary approaches: 1) web-based prompt generation, 2) red teaming, and 3) mining existing benchmark corpora, to generate over 7,000 potential benchmarks linked to the Task-Query Architecture that was developed during the first component of the project. A process of de-duplication, followed by an assessment of uplift diagnosticity, and general quality control measures, reduced the candidates to a set of 1,010 final benchmarks. This procedure ensured that these benchmarks are a) diagnostic in terms of providing uplift; b) directly relevant to biosecurity threats; and c) are aligned with a larger biosecurity architecture permitting nuanced analysis at different levels of analysis.

</details>

### 15. LLM Novice Uplift on Dual-Use, In Silico Biology Tasks

📄 [arXiv](https://arxiv.org/abs/2602.23329)　📅 2026-02

**关键词**：`benchmark`、`human uplift study`、`dual-use biology`、`novice access`

👤 **作者**：Chen Bo Calvin Zhang、…、Julian Michael

- 🎯 **研究动机**：LLM 生物学基准分数持续走高，但是否真正 uplift 新手用户（相对仅互联网资源）此前未知，而这正是双用途风险的核心
- 🔬 **研究方法**：多模型多基准人类 uplift 研究：八个生物安全相关任务集上对比有 LLM 访问与仅互联网访问的新手，最复杂任务给足 13 小时
- 📌 **结论**：LLM 访问使新手准确率提升 4.16 倍（95% CI [2.63, 6.87]），四个有专家基线的基准中三个上新手+LLM 反超专家；89.6% 参与者称获取双用途信息无困难，且独立 LLM 常超过人机组合——需要持续交互式 uplift 评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) perform increasingly well on biology benchmarks, but it remains unclear whether they uplift novice users -- i.e., enable humans to perform better than with internet-only resources. This uncertainty is central to understanding both scientific acceleration and dual-use risk. We conducted a multi-model, multi-benchmark human uplift study comparing novices with LLM access versus internet-only access across eight biosecurity-relevant task sets. Participants worked on complex problems with ample time (up to 13 hours for the most involved tasks). We found that LLM access provided substantial uplift: novices with LLMs were 4.16 times more accurate than controls (95% CI [2.63, 6.87]). On four benchmarks with available expert baselines (internet-only), novices with LLMs outperformed experts on three of them. Perhaps surprisingly, standalone LLMs often exceeded LLM-assisted novices, indicating that users were not eliciting the strongest available contributions from the LLMs. Most participants (89.6%) reported little difficulty obtaining dual-use-relevant information despite safeguards. Overall, LLMs substantially uplift novices on biological tasks previously reserved for trained practitioners, underscoring the need for sustained, interactive uplift evaluations alongside traditional benchmarks.

</details>

### 16. RCTs for Frontier AI Governance: Methodological Challenges and Solutions for Human Uplift Studies

📄 [arXiv](https://arxiv.org/abs/2603.11001)　📅 2026-03

**关键词**：`analysis`、`uplift study methodology`、`RCT validity`、`governance evidence`

👤 **作者**：Patricia Paskov、…、Ella Guest

- 🎯 **研究动机**：人类 uplift 研究日益支撑前沿 AI 治理与部署决策，但 RCT 方法的因果推断假设与快速演化的 AI 对象之间存在张力
- 🔬 **研究方法**：访谈 16 位在生物安全、网络安全、教育与劳动领域做过 uplift 研究的专家，把方法论挑战映射到内部、外部与构念效度风险并按 LLM 特异性分类
- 📌 **结论**：快速演化的系统、漂移的基线、异质多变的用户能力与 porous 现实环境共同侵蚀效度；给出挑战到解决方案的映射，以明确 uplift 证据的解释边界与适用方式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human uplift studies, or studies that measure the effects of AI access on human performance via randomized controlled trials (RCT) or similar methodologies, increasingly inform frontier AI governance and deployment decisions. While RCT methods are robust in other fields, their interaction with the distinctive properties of frontier AI systems remains underexamined, particularly when results are used to inform high-stakes decisions. We present findings from interviews with 16 expert practitioners with experience conducting human uplift studies in domains including biosecurity, cybersecurity, education, and labor. Across interviews, experts described a recurring tension between the standard causal inference assumptions upon which human uplift studies rely and the object of study itself. Rapidly evolving AI systems, shifting baselines, heterogeneous and changing user proficiency, and porous real-world settings strain assumptions underlying internal, external, and construct validity, complicating the interpretation and appropriate use of uplift evidence. We contribute (1) a synthesis of methodological challenges in human uplift studies, mapped to risks to study validity and classified by their degree of specificity to large language model (LLM) systems, and (2) a mapping from challenges to proposed solutions. By collating expert-identified challenges and solutions, we seek to clarify the interpretive limits and appropriate uses of human uplift evidence, to align evaluation practice with the decisions it informs, and to support more coordinated methodological foundations for AI governance.

</details>

### 17. BioVeil MATRIX: Uncovering and Categorizing Vulnerabilities of Agentic Biological AI Scientists

📄 [arXiv](https://arxiv.org/abs/2605.00927)　📅 2026-04

**关键词**：`analysis`、`agentic bio risk`、`scaffold uplift`、`risk taxonomy`

👤 **作者**：Kimon Antonios Provatas、Avery Self、Ioannis Mouratidis、Ilias Georgakopoulos-Soares

- 🎯 **研究动机**：配备领域工具的 agentic 生物 AI 科学家正进入生命科学工作流，其双用途风险不被模型中心的安全评测捕获
- 🔬 **研究方法**：实证检验 Biomni、K-Dense 等 agentic 系统对被底座模型拦截的双用途任务的协助意愿，并在 WMDP 代理的配对评测中测量 agentic 脚手架相对底座模型的能力 uplift
- 📌 **结论**：agentic 脚手架既绕过底座安全机制又提升危险基准表现；提出 10 战术类别、22 技术的 BioVeil MATRIX 防御分类学作为红队基准与协议的基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI scientists equipped with domain-specific tools are rapidly entering scientific workflows across disciplines, with especially strong uptake in the life sciences where they can be used for literature synthesis, sequence analysis, and experimental planning support. While these systems accelerate biological research, they also introduce risks for dual-use applications that are not captured by current model-centric safety evaluations. We present evidence that current agentic AI scientists, including Biomni and K-Dense, are willing to assist with dual-use tasks that are blocked by base model safeguards. We also found that in a paired evaluation framework for biology and chemistry prompts involving Weapons of Mass Destruction proxies (WMDP), agentic scaffolding of Biomni increased the benchmark performance relative to the underlying standalone model, producing measurable capability uplift. We believe it is necessary to include additional safeguards in existing models and build future tools from the ground up with agentic vulnerabilities in mind. To systematically categorize broader risks, we introduce BioVeil MATRIX, a defensive taxonomy that maps AI-enabled biosecurity risks using 10 tactical categories (TA01--TA10) and 22 different techniques. We propose to use this taxonomy as a baseline for future AI scientist development and generate specialized benchmarks and protocols for red-teaming these vulnerabilities before public deployment. BioVeil MATRIX can be found at: https://bioveilmatrix.com/

</details>

### 18. A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models

📄 [arXiv](https://arxiv.org/abs/2607.12200)　📅 2026-07

**关键词**：`analysis`、`uplift evaluation framework`、`threshold exceedance criteria`、`expert review`

👤 **作者**：Rahul Gupta、…、Spyros Matsoukas

- 🎯 **研究动机**：既有 CBRN 评测在非专家定义、威胁范围、基线、评分与决策规则上互不相同，结果难以跨研究比较
- 🔬 **研究方法**：提出 Threshold Exceedance Criteria（TEC）框架把 uplift 研究分解为参与者资格、威胁范围界定与统计估计三组件，并在大规模实证中区分生成式（从零协助造计划）与修订式（改进现有计划）两种 uplift
- 📌 **结论**：受控预发布评测下模型辅助计划偶获专家等同评级，但确认的物质 uplift 仅限于放射领域；强调预注册标准、显式基线与筛查信号和确认风险判定的区分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As frontier language models advance, policymakers and model developers need methods for assessing whether model access materially increases a non-expert actor's ability to plan high-consequence Chemical, Biological, Radiological, or Nuclear (CBRN) misuse relative to public tools alone. Existing CBRN evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules, making results difficult to compare across studies. We introduce a Threshold Exceedance Criteria (TEC) framework that decomposes an uplift study into independently executable components: determining non-expert participant eligibility, defining the CBRN threat scope for the study, and statistically estimating material uplift. We then operationalize the TEC framework in a large-scale empirical study using a design that determines two forms of uplift: generative (where a model assists plan creation from scratch) and revisionist (where a model assists refinement of an existing plan). The study produced attack plans across the CBRN domains, which we evaluated through subject-matter-expert review to estimate generative and revisionist uplift. Applying the framework, our empirical study revealed domain heterogeneity: under this controlled pre-release evaluation, model-assisted plans sometimes received expert-equivalent instructional ratings, but confirmed material uplift was limited to the radiological domain. These findings informed mitigation and deployment-governance decisions rather than characterizing deployed model behavior. We conclude with methodological lessons for future CBRN uplift evaluations, emphasizing prespecified criteria, explicit baselines, separation of generative and revisionist estimates, and careful distinction between preliminary screening signals and confirmed risk determinations.

</details>

### 19. Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs

📄 [arXiv](https://arxiv.org/abs/2607.18639)　📅 2026-07

**关键词**：`defense`、`dual-use knowledge`、`conditional refusal`、`knowledge gating`

👤 **作者**：Seunghyun Lee、Dongyoon Han、Sangdoo Yun

- 🎯 **研究动机**：双用途知识的安全干预常在摧毁内容（unlearning/过滤）与输出层抑制（拒绝训练）间二选一，两者都付出邻近领域能力或过度拒绝的代价
- 🔬 **研究方法**：Token Inoculation 的绑定-分支两步：持续预训练时在双用途文档旁插入特殊 token 使模型绑定危险域语义；SFT 时教会有 token 时正确作答、无 token 时拒绝
- 📌 **结论**：WMDP-Bio 准确率从 79% 降至 18% 同时保留 93% 良性域性能，在 1B-14B 规模上取得优于 unlearning 与拒绝训练的安全-效用权衡，表明安全对齐更适合建模为条件化而非遗忘问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety interventions on dual-use knowledge typically choose between destroying hazardous content (e.g., unlearning, filtering) and suppressing it at the output layer (e.g., refusal training); both pay a tax in adjacent-domain competence or over-refusal. We argue that the right operation is conditioning, not reduction: we show that hazardous knowledge can be retained in the model and behaviorally gated by a privileged control token. Our method, Token Inoculation, introduces a binding-and-branching approach. First, during continued pre-training, we mark hazardous content by inserting a special token alongside dual-use documents, so the model binds the marker to the underlying semantics of the hazardous domain. Second, during supervised fine-tuning, we teach the model to answer hazardous queries correctly when the special token is present and to refuse them when it is absent, thereby enabling selective refusal without removing dual-use knowledge. On hazardous domain (e.g., WMDP-Bio), Token Inoculation reduces accuracy from 79% to 18% while retaining 93% of the base-model's benign-domain performance (e.g., MMLU), achieving the best safety-utility trade-off against unlearning and refusal-tuning baselines across 1B-14B model scales. We further show that refusal selectivity is controllable through the quality of the conditioning signal and that domain-specific semantic binding during pre-training is critical for the conditional behavior to generalize beyond memorized triggers. Our results suggest that safety alignment is better cast as a conditioning problem than a forgetting one: behavioral control is more precise when sensitive knowledge is retained under controlled access than when it is destroyed.

</details>

### 20. ChemMat-AgentSafetyBench: Evaluating Long-Horizon Attacks and Defenses in Chemistry and Materials Agents

📄 [arXiv](https://arxiv.org/abs/2609.11952)　📅 2026-09

**关键词**：`benchmark`、`chemistry agent safety`、`long-horizon attack`、`tool chaining`、`memory poisoning`

👤 **作者**：Zhan&#39;ao Yao、…、Jianjun Liu

- 🎯 **研究动机**：化学与材料 agent 把文献检索、候选生成、性质预测与协议规划串成连续发现工作流，安全问题已从「模型是否回答危险问题」变成「agent 是否经工具链释放危险协议」，而现有 agent 安全评测不覆盖这一长程工具链场景
- 🔬 **研究方法**：构建 ChemMat-AgentSafetyBench：432 个固定有害案例规格横跨 8 个危害类、3 种场景壳与 4 种工具-记忆环境；除单轮直接攻击基线外设计五类在线长程攻击——意图劫持、工具链、目标漂移、任务注入与记忆投毒，攻击语言按运行时轨迹动态生成故不计入静态规模；四模型主实验固定攻击者并更换攻击者模型复核稳健性
- 📌 **结论**：固定攻击者下 25.6% 的运行释放完整危险合成/制备流程，换攻击者均值 18.4-26.5% 说明风险非单一攻击者伪影；从通用 agent 安全改造的输入/状态级防御与化学专用候选检查只能部分降低，完整路径释放率仍达 9.2-22.5%——多入口污染、工具状态与最终产物边界未被任何现有防御同时覆盖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chemistry and materials agents integrate literature retrieval, candidate generation, property prediction, and protocol planning into continuous discovery workflows. Consequently, the relevant safety question is shifting from whether a model answers a hazardous question to whether an agent releases a hazardous protocol through a tool-mediated workflow. We introduce \bench, a benchmark that evaluates whether chemistry and materials agents can be steered toward hazardous endpoints through user input, tool observations, or persistent memory. The benchmark contains 432 fixed harmful case specifications spanning eight hazard classes, three scenario shells, four tool-and-memory environments, a single-turn direct-attack baseline, and five online long-horizon attacks: intent hijacking, tool chaining, objective drifting, task injection, and memory poisoning. The concrete language of each online attack is generated from the evolving trajectory at runtime and is therefore not counted in the static benchmark size. In the four-model main experiment with a fixed attacker, agents release complete hazardous synthesis or preparation procedures in 25.6\% of runs. Replacing the attacker model yields mean success rates from 18.4\% to 26.5\%, indicating that the risk is not an artifact of a single attacker. Input- and state-level defenses adapted from general-purpose agent safety, as well as candidate checks designed for chemistry and materials, reduce some failures but still leave complete-path release rates between 9.2\% and 22.5\%. Existing defenses therefore do not simultaneously cover multi-entry contamination, tool state, and the final artifact boundary. These results highlight a widening gap between the rapid development of scientific agents and the safety evaluation and defenses available to the chemistry and materials community.

</details>
