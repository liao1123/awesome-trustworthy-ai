# AI Peer Review Security

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 LLM 或 MLLM 被用于 manuscript screening、review assistance、automated scoring 和 editorial triage 时的可靠性与可操纵性。威胁既包括模型自身的 score inflation、评价维度偏差、hallucination 和 reviewer homogenization，也包括作者主动植入 hidden prompt、对 figure 做 adversarial perturbation，或在不改变科学 claim 的情况下优化 abstract、rhetoric 和 presentation 来提高评分。该问题与一般 jailbreak 不同：攻击目标是定向改变评审结论，而不是让模型输出任意违规内容。

## 研究脉络

- **Reviewer validity：** 早期比较显示 AI reviewer 会高估弱论文、与人类关注点分离并产生模板化长评审，说明 capability 不等于 calibrated judgment。
- **Review infrastructure：** Review-CoT 与 ReviewBench 将 structured reasoning、相关工作引用和 human-review alignment 变成可复用的训练与评测对象，为后续 robustness study 提供基础。
- **Hidden prompt：** PDF 中不可见文字、field-specific instruction 和 iterative injection 可直接抬高分数；检测式防御面对 adaptive attacker 仍会退化。
- **Presentation gaming：** PAA、Review Arcade、abstract rewrite 与 adversarial repackaging 证明即使没有显式恶意指令，语义保持或表述层修改也能优化 AI score。
- **Multimodal attack：** PaperGuard 将 threat model 从正文扩展到 figure，并以 chunk retrieval 和 intent verification 处理长文档中的稀疏攻击证据。
- **当前边界：** 单一 reviewer-model correlation 不能证明安全；部署前还需要 score calibration、跨模型稳定性、attack-aware evaluation、人类复核和不让作者反向优化 evaluator 的机制。

## Reviewer Validity、Bias 与 Benchmark

### 1. HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews

📄 [arXiv](https://arxiv.org/abs/2609.03580)　📅 2026-09

**关键词**：`benchmark`、`peer-review hallucination`、`source grounding`、`claim localization`、`claim-source verification`、`review provenance`

👤 **作者**：Tzu-Ling Lin、Dong-Ting Yao、Teng-Fang Hsiao、Wei-Chih Chen、Hong-Han Shuai

- 🎯 **研究动机**：LLM 评审助手会生成流畅但无依据的批评，而现有幻觉 benchmark 不适配长技术论文的评审核验场景
- 🔬 **研究方法**：构建 HalluPeer：论文内容、人工评审与幻觉注入评审的对齐三元组，标注检测、分类与定位；管线先归纳评审特定幻觉分类、识别评审语境再自动过滤注入
- 📌 **结论**：在 12K 论文、38K 评审上现有检测器难以区分幻觉与正当批评；真实评审中也出现 HalluPeer 定义的幻觉模式，凸显溯源感知核验的必要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but unsupported claims that undermine review reliability. Existing hallucination benchmarks are not designed for peer review, where verification requires grounding claims in long, technical papers. We introduce HalluPeer, a benchmark for detecting hallucinations in scientific peer reviews, providing aligned triples of paper content, human-written reviews, and hallucination-injected reviews, annotated for detection, classification, and localization. Our pipeline induces a peer-review-specific hallucination taxonomy, identifies review contexts, and injects hallucinations with automated filtering. Experiments on 12K papers and 38K reviews show that existing detectors struggle to separate hallucinations from legitimate critique, while evaluation on authentic reviews demonstrates that HalluPeer-defined hallucination patterns occur in real peer reviews, highlighting the critical need for source-aware verification. Our project page can be found in https://github.com/Lin-TzuLing/HalluPeer.git

</details>

### 2. How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review

📄 [arXiv](https://arxiv.org/abs/2608.08975)　📅 2026-08

**关键词**：`analysis`、`rhetorical style`、`reward hacking`、`review score`

👤 **作者**：Ming Li、…、Tianyi Zhou

- 🎯 **研究动机**：LLM 参与科研评审时，内容不变的修辞选择能否操纵评分（reward hacking）未知
- 🔬 **研究方法**：从 120 篇 ICLR 2026 投稿构建 4200 篇对照稿，两 LLM 反向改写六个修辞维度、五 LLM 评审，并测联合、递归与评审引导改写
- 📌 **结论**：证据框架与新颖性立场产生最大评分正负差，低分稿趋升、高分稿趋降；改写者决定对比幅度、评审者决定效应符号，严格评审均分降 1.36

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models increasingly participate in scientific evaluation, we investigate a potential form of reward hacking: how rhetorical choices shape AI-review judgments when reported scientific content is preserved and how these effects vary across evaluation conditions. We construct a controlled corpus of 4,200 full-paper manuscripts derived from 120 anonymized ICLR 2026 submissions. Two LLM rewriters transform six rhetorical dimensions in opposing directions, and five LLM reviewers evaluate the resulting manuscripts under standard and strict protocols. We also test joint, recursive, and reviewer-guided rewriting. Our results show that rhetorical sensitivity is structured rather than uniform. Evidence framing and novelty stance produce the largest positive-negative contrasts in overall assessment, with scope framing forming a weaker second tier; the remaining dimensions have smaller or less stable effects. This hierarchy persists across human-assessed quality levels, but score movement depends strongly on the AI reviewer's original score: lower scores tend to rise, higher scores tend to fall, and directional contrasts are clearest in the middle ranges. More elaborate workflows do not reliably yield larger gains. Joint rewriting is strongly rewriter-dependent, reviewer guidance does not consistently outperform an unguided second pass, and repeated rewriting yields diminishing, configuration-dependent returns. Across conditions, the rewriter primarily determines the separation between opposing variants, whereas the reviewer determines the magnitude and sign of their score effects. Strict review lowers mean OA by 1.36 points without consistently changing rhetorical sensitivity. These findings identify when rhetorical presentation influences AI scientific review and motivate evaluation systems robust to content-preserving variation in scientific writing.

</details>

### 3. PRISM: A Multi-Dimensional Benchmark for Evaluating LLM Peer Reviewers

📄 [arXiv](https://arxiv.org/abs/2605.26730) · 🌐 [Project](https://khanhthanhdev.github.io/prism-page/)　📅 2026-05

**关键词**：`benchmark`、`AI peer review`、`review validity`、`scientific judgment`

👤 **作者**：Ngoc Phan Phuoc Loc、…、Binh T. Nguyen

- 🎯 **研究动机**：LLM 自动审稿的真实水平尤其与人类发现科学缺口能力相比不明，现有评测或用 ROUGE 或用无约束 judge 混淆流畅与严谨
- 🔬 **研究方法**：PRISM 四维评估（分析深度、新颖性评估、缺陷识别与优先级、多维建设性），各维度 grounded 于论点挖掘、检索增强验证与共识评分，评五个自动审稿系统与人类审稿
- 📌 **结论**：LLM 在单维可追平或超过人类（更强新颖性验证、高准确批评排序），但无一系统在所有维同时匹配人类的均衡表现——应作定向补充而非独立替代

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth in submissions to machine learning venues has strained the scientific peer-review system and intensified interest in LLM-based automated peer reviewers. However, how good these systems are actually, especially compared to human reviewers at catching scientific gaps, remains poorly understood. In this work, we introduce PRISM (Peer Review Intelligence via Structured Multi-dimensional assessment), a benchmarking framework that evaluates review quality across four dimensions: Depth of Analysis, Novelty Assessment,Flaw Identification & Major Issues Prioritization, and Multi-dimensional Constructiveness. Unlike most existing evaluations based on surface-level metrics like ROUGE and BLEU, or unconstrained LLM-as-a-judge prompting that conflates fluency with rigor, PRISM grounds each dimension in argument mining, retrieval-augmented verification, and consensus-based scoring. We apply PRISM to benchmark five leading automated reviewer systems and human reviewers on a stratified corpus of reviews from ICLR, ICML, and NeurIPS. The results reveal that LLMs can match or beat human reviewers on individual dimensions: comparable depth of analysis, stronger novelty verification, and highly accurate critique prioritization. However, no single system consistently matches the balanced performance of the human baseline across all dimensions at once. Each exhibits a distinct specialization profile with characteristic blind spots -- failure modes that aggregate metrics miss entirely. The implication is that LLM reviewers are best understood as targeted supplements to human review, effective within specific dimensions, but unreliable as standalone replacements. Our demo and key results can be found at https://khanhthanhdev.github.io/prism-page/.

</details>

### 4. LLM-as-a-Reviewer: Benchmarking Their Ability, Divergence, and Prompt Injection Resistance as Paper Reviewers

📄 [arXiv](https://arxiv.org/abs/2605.25415)　📅 2026-05

**关键词**：`benchmark`、`rating calibration`、`human divergence`、`prompt injection`

👤 **作者**：Lingyao Li、…、Zhicong Lu

- 🎯 **研究动机**：LLM 审稿的可靠性、与人类判断的一致性及对抗鲁棒性缺乏联合评测
- 🔬 **研究方法**：在 898 篇 NeurIPS 与 ICLR 论文上评 12 个 LLM 的评分校准、与人类审稿分歧及对隐形 font-mapping 注入攻击的抵抗力
- 📌 **结论**：LLM 系统性高估弱稿、对 Clarity 欠标记而 Reproducibility 过标记；简单隐藏指令即可把低分稿抬到接收级评分且效果跨模型家族差异大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used in academic peer review, yet their reliability, alignment with human judgment, and robustness to adversarial attacks remain poorly understood. We present a systematic benchmark of LLM-as-a-Reviewer on 898 papers stratified from NeurIPS and ICLR, evaluating 12 LLMs along three axes: rating calibration, divergence from human reviewers, and resistance to prompt injection embedded via an invisible font-mapping attack. We find that LLMs systematically overrate weaker submissions and diverge from humans in topical emphasis, under-flagging Clarity and over-flagging Reproducibility, while producing reviews two to three times longer with lower lexical diversity and a more standardized vocabulary. Prompt injection remains highly effective. Simple hidden instructions can promote low-scoring papers to acceptance-level ratings in a substantial fraction of cases, with effectiveness varying sharply across model families. While LLMs offer utility in structuring evaluations, their integration into peer review requires safeguards against both intrinsic biases and adversarial risks.

</details>

### 5. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers

📄 [arXiv](https://arxiv.org/abs/2605.07905) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65498)　📅 2026-05　🏷 ICML 2026

**关键词**：`benchmark`、`review completeness`、`review correctness`、`expert discussion`

👤 **作者**：Hexuan Deng、…、Min Zhang

- 🎯 **研究动机**：AI 审稿评测以与人类审稿重叠为指标，但人类审稿本身不完整且有错，不适合作 gold 参考
- 🔬 **研究方法**：按类别构建子集并在人类审稿缺失时跳过以保完整性；用 reviewer-author-meta-review 讨论作专家标注过滤不可靠审稿；从 ICLR 与 NeurIPS 策展 3,900 篇构建 CoCoReviewBench
- 📌 **结论**：AI 审稿在正确性上仍受限且易幻觉；推理模型是更有效的审稿者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the rapid development of AI reviewers, evaluating such systems remains challenging: metrics favor overlap with human reviews over correctness. However, since human reviews often cover only a subset of salient issues and sometimes contain mistakes, they are unreliable as gold references. To address this, we build category-specific benchmark subsets and skip evaluation when the corresponding human reviews are missing to strengthen Completeness. We also leverage reviewer--author--meta-review discussions as expert annotations and filter unreliable reviews accordingly to strengthen Correctness. Finally, we introduce CoCoReviewBench, which curates 3,900 papers from ICLR and NeurIPS to enable reliable and fine-grained evaluation of AI reviewers. Analysis shows that AI reviewers remain limited in correctness and are prone to hallucinations, and highlights reasoning models as more effective reviewers, motivating further directions for improving AI reviewers. Benchmarks and models are available at https://github.com/hexuandeng/CoCoReviewBench.

</details>

### 6. When AI reviews science: Can we trust the referee?

📄 [arXiv](https://arxiv.org/abs/2604.23593) · 🌐 [Project](https://doi.org/10.59717/j.xinn-inform.2026.100030)　📅 2026-04

**关键词**：`analysis`、`review lifecycle`、`causal probe`、`context poisoning`

👤 **作者**：Jialiang Wang、…、Lei Chen

- 🎯 **研究动机**：AI 审稿的攻击风险散落在流程各环节且缺统一安全分析，可靠性缺乏证据基线
- 🔬 **研究方法**：按审稿生命周期（训练检索、desk review、deep review、rebuttal、系统级）构建攻击 taxonomy，并在分层抽样的 ICLR 2025 提交上做四个 treatment-control 探针
- 📌 **结论**：分离了 prestige framing、assertion strength、rebuttal sycophancy 与 context poisoning 对审稿分的因果效应，定位可测试的失效点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The volume of scientific submissions continues to climb, outpacing the capacity of qualified human referees and stretching editorial timelines. At the same time, modern large language models (LLMs) offer impressive capabilities in summarization, fact checking, and literature triage, making the integration of AI into peer review increasingly attractive -- and, in practice, unavoidable. Yet early deployments and informal adoption have exposed acute failure modes. Recent incidents have revealed that hidden prompt injections embedded in manuscripts can steer LLM-generated reviews toward unjustifiably positive judgments. Complementary studies have also demonstrated brittleness to adversarial phrasing, authority and length biases, and hallucinated claims. These episodes raise a central question for scholarly communication: when AI reviews science, can we trust the AI referee? This paper provides a security- and reliability-centered analysis of AI peer review. We map attacks across the review lifecycle -- training and data retrieval, desk review, deep review, rebuttal, and system-level. We instantiate this taxonomy with four treatment-control probes on a stratified set of ICLR 2025 submissions, using two advanced LLM-based referees to isolate the causal effects of prestige framing, assertion strength, rebuttal sycophancy, and contextual poisoning on review scores. Together, this taxonomy and experimental audit provide an evidence-based baseline for assessing and tracking the reliability of AI peer review and highlight concrete failure points to guide targeted, testable mitigations.

</details>

### 7. When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review

📄 [arXiv](https://arxiv.org/abs/2509.09912)　📅 2025-09

**关键词**：`analysis`、`reviewer bias`、`topic divergence`、`field-specific injection`

👤 **作者**：Changjia Zhu、Junjie Xiong、Renkai Ma、Zhicong Lu、Yao Liu、Lingyao Li

- 🎯 **研究动机**：LLM 作为评审辅助的公平性、一致性与抗注入能力存疑
- 🔬 **研究方法**：基于 ICLR 2023 与 NeurIPS 2022 的 1441 篇论文，以结构化 prompt、主题建模与相似度分析比较 GPT-5-mini 与人类评审，并在 PDF 中嵌入隐蔽指令测试注入
- 📌 **结论**：LLM 对弱论文系统性打分虚高；泛化恶意指令影响小，但领域特定指令可成功操纵评审的特定方面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Peer review is the cornerstone of academic publishing, yet the process is increasingly strained by rising submission volumes, reviewer overload, and expertise mismatches. Large language models (LLMs) are now being used as "reviewer aids," raising concerns about their fairness, consistency, and robustness against indirect prompt injection attacks. This paper presents a systematic evaluation of LLMs as academic reviewers. Using a curated dataset of 1,441 papers from ICLR 2023 and NeurIPS 2022, we evaluate GPT-5-mini against human reviewers across ratings, strengths, and weaknesses. The evaluation employs structured prompting with reference paper calibration, topic modeling, and similarity analysis to compare review content. We further embed covert instructions into PDF submissions to assess LLMs' susceptibility to prompt injection. Our findings show that LLMs consistently inflate ratings for weaker papers while aligning more closely with human judgments on stronger contributions. Moreover, while overarching malicious prompts induce only minor shifts in topical focus, explicitly field-specific instructions successfully manipulate specific aspects of LLM-generated reviews. This study underscores both the promises and perils of integrating LLMs into peer review and points to the importance of designing safeguards that ensure integrity and trust in future review processes.

</details>

### 8. No Hidden Prompts Needed! You Can Game AI Peer Review with Presentation-Only Revisions

📄 [arXiv](https://arxiv.org/abs/2606.13044)　📅 2026-06

**关键词**：`attack`、`adversarial repackaging`、`black-box loop`、`presentation gaming`

👤 **作者**：Xu Yang、…、Zhangyang Wang

- 🎯 **研究动机**：已有 AI 评审攻击依赖隐藏指令与提示注入，而仅改动展示层内容的更政策相关失效模式未被研究
- 🔬 **研究方法**：提出 adversarial repackaging 闭环攻击：以 AI 评审反馈为信号搜索展示层修订（摘要、贡献框架、相关工作、叙事结构），科学证据不变
- 📌 **结论**：三个主流 AI 评审器上 ASR 75.1%、平均加分 +1.21/10；改变评审解读的策略远胜表面编辑，且 AI 评审易被取悦而非说服

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI-generated reviews move from experimental tools into peer-review infrastructure, most robustness concerns have focused on explicit attacks such as hidden instructions and prompt injection. We study a harder and more policy-relevant failure mode: no hidden text, no prompt injection, and no changes to methods, experiments, figures, equations, proofs, or numerical results. The attacker modifies only presentation-level content, such as the abstract, contribution framing, related work, discussion, and narrative structure. We introduce adversarial repackaging: a closed-loop attack that uses AI-reviewer feedback to search for presentation-level revisions while keeping the scientific evidence fixed. Across three mainstream AI reviewers, adversarial repackaging achieves a 75.1% attack success rate and a mean score gain of +1.21/10. The effect is not explained by ordinary prose polishing. We also reveal that strategies that change how the reviewer interprets the paper, such as related-work repositioning and analytical discussion expansion, substantially outperform surface edits such as local polishing, table formatting, and algorithm boxes. Our analysis reveals two deeper structural failure modes. First, AI reviewers are easier to impress than to convince: highlighting strengths reliably increases perceived merit, while attempts to dissolve weaknesses frequently backfire. Second, AI reviewers can confuse the appearance of addressing a limitation with actually resolving it, allowing unchanged evidence to be reinterpreted as stronger scientific contribution. These results show that the deployment risk is not only malicious hidden instructions, but the emergence of paper presentation itself as an optimization surface. We release a contamination-free rolling benchmark and attack framework for testing whether AI reviewers remain anchored to scientific content under presentation-only edits.

</details>

### 9. Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community

📄 [arXiv](https://arxiv.org/abs/2606.10159)　📅 2026-06

**关键词**：`attack`、`abstract rewrite`、`score inflation`、`low-cost optimization`

👤 **作者**：Lin Li、Qi Zhang、Xander Davies、Jianing Qiu、Yarin Gal

- 🎯 **研究动机**：AI 辅助同行评审被广泛部署，其对策略性操纵的鲁棒性未知
- 🔬 **研究方法**：证明不改变科学内容、不需了解评审模型的情况下，仅对摘要做对抗性改写即可提升 AI 评审结果，跨学科与出版 venue 验证
- 📌 **结论**：最强攻击 ASR 约 38%，Gemini 3 Flash 评分 +1.31、GPT 5.4 Mini +0.88（10 分制）；原判拒绝时成功率超 50%，且仅需约 5 分钟与 1 美元

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI is increasingly used to support scientific peer review, from manuscript screening, reviewer assistance to editorial triage. Although such systems promise to reduce reviewer burden and accelerate publication, their robustness to strategic manipulation remains poorly understood. Here we show that AI-mediated peer review is vulnerable to a simple, low-cost manipulation: superficial rephrasing of the manuscript abstract. Without changing the underlying scientific content and communication, and even without knowledge of the reviewing model, adversarially rewritten abstracts substantially improve AI review outcomes. We see this across disciplines and publication venues, for both human-written and AI-generated papers. Our strongest attack achieves an attack-success-rate of about 38%, increasing acceptance ratings by +1.31 for Gemini 3 Flash reviewers and by +0.88 for GPT 5.4 Mini reviewers on a 10-point scale. When the original AI review suggests 'reject', the success rate rises to more than 50%. This effect extends beyond overall score inflation, increasing review confidence and scores on core scientific criteria such as soundness, significance and perceived contribution. The attack is practical, requiring only about 5 minutes and $1 for a 10-page AI conference submission, and is hard to distinguish from ordinary scientific editing. Inflated AI reviews could bias downstream human decision-making, shifting editorial recommendations from rejection towards acceptance. These findings reveal a general vulnerability in AI-assisted scientific evaluation: when AI-generated review influence editorial decisions, authors may be incentivized to optimize manuscripts for AI judgment rather than scientific merit. Our results suggest that AI tools should not be treated as neutral evaluators in high-stakes peer review without systematic robustness testing, transparent safeguards and careful human oversight.

</details>

### 10. Review Arcade: On the Human Alignment and Gameability of LLM Reviews

📄 [arXiv](https://arxiv.org/abs/2605.28897)　📅 2026-05　🏷 EMNLP 2026

**关键词**：`analysis`、`draft-revise loop`、`human alignment`、`review gameability`

👤 **作者**：Hans Ole Hatzel、Sebastian Steindl、Jan Strich

- 🎯 **研究动机**：审稿人与作者都在用 LLM 的现实下，作者按 LLM 审稿迭代修改投稿的博弈效果未测
- 🔬 **研究方法**：在 2025 ACL Rolling Review 稿件上从作者与审稿人双视角实证评测 LLM 审稿，并模拟 draft-revise 迭代工作流
- 📌 **结论**：LLM 与人类审稿对齐有限且随 prompt 与模型大幅波动；迭代博弈在特定场景使最多 35% 论文总分统计显著提高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-generated reviews for scientific papers are gaining considerable traction and are even being officially piloted by major conferences. We have to assume that not only reviewers are using LLM-assistance, but also that authors use LLMs to revise their papers before submitting. In this work, we perform empirical experiments on papers from the 2025 ACL Rolling Review (ARR) to evaluate LLM reviews from both the author and the reviewer perspective. First, we identify a limited alignment of LLM reviews with human ones. In the best-case scenario, the alignment is reasonable. However, we also find that LLM-human alignment varies substantially across prompts and models. Finally, we investigate the scenario in which the author uses an iterative draft-revise workflow to improve the submission according to the LLM review. We find that this "gaming" of LLM reviews can be effective in specific scenarios, leading to a statistically significant increase of overall scores for up to 35\% of papers. We publish our code: https://github.com/uhh-hcds/reviewarcade.

</details>

### 11. Paraphrasing Adversarial Attack on LLM-as-a-Reviewer

📄 [arXiv](https://arxiv.org/abs/2601.06884)　📅 2026-01

**关键词**：`attack`、`semantic-preserving paraphrase`、`black-box optimization`、`score manipulation`

👤 **作者**：Masahiro Kaneko

- 🎯 **研究动机**：已有 LLM 审稿攻击依赖 prompt injection，改变了稿件内容，混淆注入易感性与评审鲁棒性
- 🔬 **研究方法**：Paraphrasing Adversarial Attack 黑盒搜索语义等价且自然、能获得更高评审分的改写，用 in-context learning 以历史改写及其得分引导候选生成
- 📌 **结论**：在五个 ML/NLP 会议、三类 LLM 审稿模型上稳定提高评审分且论文主张不变；受攻论文的评审困惑度上升可作检测信号，改写投稿可部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The use of large language models (LLMs) in peer review systems has attracted growing attention, making it essential to examine their potential vulnerabilities. Prior attacks rely on prompt injection, which alters manuscript content and conflates injection susceptibility with evaluation robustness. We propose the Paraphrasing Adversarial Attack (PAA), a black-box optimization method that searches for paraphrased sequences yielding higher review scores while preserving semantic equivalence and linguistic naturalness. PAA leverages in-context learning, using previous paraphrases and their scores to guide candidate generation. Experiments across five ML and NLP conferences with three LLM reviewers and five attacking models show that PAA consistently increases review scores without changing the paper's claims. Human evaluation confirms that generated paraphrases maintain meaning and naturalness. We also find that attacked papers exhibit increased perplexity in reviews, offering a potential detection signal, and that paraphrasing submissions can partially mitigate attacks.

</details>

### 12. Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review

📄 [arXiv](https://arxiv.org/abs/2606.12716) · 🌐 [Project](https://paper-guard.github.io/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61968)　📅 2026-06　🏷 ICML 2026

**关键词**：`benchmark`、`attack`、`multimodal review`、`figure attack`、`chunk localization`、`adversarial attack`

👤 **作者**：Xinyu Zhao、Rana Muhammad Shahroz Khan、Zhen Xu、Zhen Tan、Tianlong Chen

- 🎯 **研究动机**：AI 同行评审的鲁棒性研究几乎全是纯文本，而论文图表承载核心证据，且评审攻击目标是领域特定失效而非一般安全违规，缺乏防御
- 🔬 **研究方法**：提出 PaperGuard 基准：多领域多模态评审数据集+黑盒提示注入与白盒扰动（文本 GCG、图像 PGD）攻击套件+基于分块嵌入搜索的高效定位防御
- 📌 **结论**：SOTA 模型上 AI 评审者普遍脆弱，确立首个攻击-防御基准与协议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of Large Language Models (LLMs) and Multimodal LLMs (MLLMs) into scientific peer-review workflows introduces novel and significant risks for adversarial manipulation, especially given the multimodal nature of scientific papers where figures, not just text, convey core evidence. This creates a significant gap: current robustness studies on AI peer-review are overwhelmingly text-only. Moreover, the problem is distinct from standard jailbreaking, as a peer-review attack seeks to induce a domain-specific, targeted failure (e.g., "inflate this score") rather than a general safety policy violation, for which no practical defenses exist. To address this, we introduce PaperGuard, the first comprehensive benchmark designed to systematically evaluate and defend AI-generated peer-review against these domain-specific, cross-modal attacks. Our framework is built on three pillars: (1) a new multimodal peer-review dataset spanning multiple scientific domains; (2) a unified suite of attacks, including black-box prompt injections and white-box perturbations, specifically designed to target both text (GCG) and figures (PGD); and (3) a practical defense, motivated by the long-context challenge of academic papers, that uses chunk-based embedding search to efficiently localize and mitigate harmful instructions. Our extensive experiments, conducted across state-of-the-art models, confirm that AI reviewers are pervasively vulnerable. PaperGuard establishes the foundational benchmark, protocols, and actionable defense necessary to pioneer trustworthy, attack-resilient AI-assisted scholarly reviewing.

</details>

### 13. ChatGPT: Excellent Paper! Accept It. Editor: Imposter Found! Review Rejected

📄 [arXiv](https://arxiv.org/abs/2512.20405)　📅 2025-12

**关键词**：`analysis`、`PDF injection`、`LLM-review detection`、`editorial integrity`

👤 **作者**：Kanchon Gharami、Sanjiv Kumar Sarkar、Safayat Bin Hakim、Yongxin Liu、Nahid Farhady Ghalaty、Shafika Showkat Moni

- 🎯 **研究动机**：作者可用 PDF 隐藏 prompt 操纵 LLM 审稿人给出正面评审，编辑又难以识别机器生成的评审
- 🔬 **研究方法**：攻击侧演示 PDF 隐藏 prompt 诱导 LLM 审稿人给正面反馈与偏向性接受；防御侧提出 inject-and-detect：编辑在稿件中埋入不可见触发 prompt，评审若复现或响应即暴露 LLM 生成
- 📌 **结论**：把 prompt injection 从漏洞转化为验证工具，揭示同行评审流程在 LLM 影响下的脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) like ChatGPT are now widely used in writing and reviewing scientific papers. While this trend accelerates publication growth and reduces human workload, it also introduces serious risks. Papers written or reviewed by LLMs may lack real novelty, contain fabricated or biased results, or mislead downstream research that others depend on. Such issues can damage reputations, waste resources, and even endanger lives when flawed studies influence medical or safety-critical systems. This research explores both the offensive and defensive sides of this growing threat. On the attack side, we demonstrate how an author can inject hidden prompts inside a PDF that secretly guide or "jailbreak" LLM reviewers into giving overly positive feedback and biased acceptance. On the defense side, we propose an "inject-and-detect" strategy for editors, where invisible trigger prompts are embedded into papers; if a review repeats or reacts to these triggers, it reveals that the review was generated by an LLM, not a human. This method turns prompt injections from vulnerability into a verification tool. We outline our design, expected model behaviors, and ethical safeguards for deployment. The goal is to expose how fragile today's peer-review process becomes under LLM influence and how editorial awareness can help restore trust in scientific evaluation.

</details>

### 14. "Give a Positive Review Only": An Early Investigation Into In-Paper Prompt Injection Attacks and Defenses for AI Reviewers

📄 [arXiv](https://arxiv.org/abs/2511.01287)　📅 2025-11

**关键词**：`attack`、`in-paper injection`、`iterative prompt`、`adaptive bypass`

👤 **作者**：Qin Zhou、Zhexin Zhang、Zhi Li、Limin Sun

- 🎯 **研究动机**：论文中隐藏注入提示操纵 AI 审稿人给出有利评审的威胁缺乏系统研究
- 🔬 **研究方法**：提出静态注入与面向模拟审稿模型迭代优化的注入两类攻击，并测试简单的检测式防御
- 📌 **结论**：两类攻击频繁诱导前沿 AI 审稿人给出满分；检测显著降低 ASR 但被自适应攻击者部分绕过

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of AI models, their deployment across diverse tasks has become increasingly widespread. A notable emerging application is leveraging AI models to assist in reviewing scientific papers. However, recent reports have revealed that some papers contain hidden, injected prompts designed to manipulate AI reviewers into providing overly favorable evaluations. In this work, we present an early systematic investigation into this emerging threat. We propose two classes of attacks: (1) static attack, which employs a fixed injection prompt, and (2) iterative attack, which optimizes the injection prompt against a simulated reviewer model to maximize its effectiveness. Both attacks achieve striking performance, frequently inducing full evaluation scores when targeting frontier AI reviewers. Furthermore, we show that these attacks are robust across various settings. To counter this threat, we explore a simple detection-based defense. While it substantially reduces the attack success rate, we demonstrate that an adaptive attacker can partially circumvent this defense. Our findings underscore the need for greater attention and rigorous safeguards against prompt-injection threats in AI-assisted peer review.

</details>

### 15. Misleading Large Language Models used (or misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2508.20863) · 🌐 [Project](https://doi.org/10.1145/3803804)　📅 2025-08

**关键词**：`attack`、`hidden PDF text`、`review manipulation`、`detectability evasion`

👤 **作者**：Matteo Gioele Collu、Umberto Salviati、Roberto Confalonieri、Mauro Conti、Giovanni Apruzzese

- 🎯 **研究动机**：LLM 介入学术评审后，作者在 PDF 中嵌入对抗文本操纵评审的风险未被系统研究
- 🔬 **研究方法**：形式化三种威胁模型，设计人眼不可见但可引导 LLM 评审的对抗 prompt，经领域学者用户研究与多系统、多篇论文评测鲁棒性
- 📌 **结论**：对抗 prompt 可可靠误导 LLM 甚至影响 honest-but-lazy 评审者，并评估了降低自动检测率的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly being integrated into the scientific peer-review process, raising new questions about their reliability and resilience to manipulation. In this work, we investigate the potential for hidden prompt injection attacks, where authors embed adversarial text within a paper's PDF to influence the LLM-generated review. We begin by formalising three distinct threat models that envision attackers with different motivations -- not all of which implying malicious intent. For each threat model, we design adversarial prompts that remain invisible to human readers yet can steer an LLM's output toward the author's desired outcome. Using a user study with domain scholars, we derive four representative reviewing prompts used to elicit peer reviews from LLMs. We then evaluate the robustness of our adversarial prompts across (i) different reviewing prompts, (ii) different commercial LLM-based systems, and (iii) different peer-reviewed papers. Our results show that adversarial prompts can reliably mislead the LLM, sometimes in ways that adversely affect a "honest-but-lazy" reviewer. Finally, we propose and empirically assess methods to reduce detectability of adversarial prompts under automated content checks.

</details>

### 16. Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks

🎓 [Official](https://aclanthology.org/2025.findings-emnlp.259/)　📅 2025-06　🏷 EMNLP 2025

**关键词**：`benchmark`、`textual attack`、`automated review`、`robustness evaluation`

👤 **作者**：Tzu-Ling Lin、…、Hong-Han Shuai

- 🎯 **研究动机**：LLM 辅助同行评审在文本对抗攻击下的可靠性缺乏系统评估
- 🔬 **研究方法**：评估 LLM 生成评审相对人类评审的质量、对抗攻击对评审可靠性的影响及潜在缓解策略
- 📌 **结论**：文本操纵可显著扭曲 LLM 评审判断，暴露自动化评审的对抗脆弱性，须加防御以维护学术交流完整性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Peer review is essential for maintaining academic quality, but the increasing volume of submissions places a significant burden on reviewers. Large language models (LLMs) offer potential assistance in this process, yet their susceptibility to textual adversarial attacks raises reliability concerns. This paper investigates the robustness of LLMs used as automated reviewers in the presence of such attacks. We focus on three key questions: (1) The effectiveness of LLMs in generating reviews compared to human reviewers. (2) The impact of adversarial attacks on the reliability of LLM-generated reviews. (3) Challenges and potential mitigation strategies for LLM-based review. Our evaluation reveals significant vulnerabilities, as text manipulations can distort LLM assessments. We offer a comprehensive evaluation of LLM performance in automated peer reviewing and analyze its robustness against adversarial attacks. Our findings emphasize the importance of addressing adversarial risks to ensure AI strengthens, rather than compromises, the integrity of scholarly communication.

</details>

### 17. SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts

📄 [arXiv](https://arxiv.org/abs/2604.26506)　📅 2026-04

**关键词**：`defense`、`co-evolutionary training`、`adaptive injection`、`ranking preservation`

👤 **作者**：Yuan Xin、…、Linyi Yang

- 🎯 **研究动机**：LLM 审稿可被稿件中的对抗性隐藏 prompt 操纵，静态防御难以覆盖演化中的攻击
- 🔬 **研究方法**：SafeReview 共同进化对抗训练：Generator 生成更强的注入 prompt，Defender 经偏好训练保持干净与受攻击稿件的审稿一致
- 📌 **结论**：提升对自适应注入攻击的鲁棒性，更好保持攻击下的论文排序，并跨攻击者架构泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) are increasingly integrated into academic peer review, their vulnerability to adversarial hidden prompts, i.e., adversarial instructions embedded in submissions to manipulate outcomes, poses a critical threat to scholarly integrity. We propose SafeReview, a co-evolutionary adversarial training framework for defending LLM-based peer review systems against such attacks. SafeReview jointly trains a Generator model to create sophisticated attack prompts and a Defender model to preserve review integrity under adversarial manipulation. The Generator is optimized to produce increasingly effective prompt injections, while the Defender is strengthened through preference-based training to maintain consistent reviews between clean and attacked submissions. Experimental results show that SafeReview improves robustness against adaptive prompt injection attacks, better preserves paper ranking under attack, and generalizes across attacker architectures compared with static defenses. These results demonstrate the potential of co-evolutionary training as a foundation for securing LLM-assisted peer review.

</details>

### 18. Stop Automating Peer Review Without Rigorous Evaluation

📄 [arXiv](https://arxiv.org/abs/2605.03202) · 🎓 [Official](https://icml.cc/virtual/2026/poster/67247)　📅 2026-05　🏷 ICML 2026

**关键词**：`analysis`、`review automation`、`hivemind effect`、`paper laundering`

👤 **作者**：Joachim Baumann、Jiaxin Pei、Sanmi Koyejo、Dirk Hovy

- 🎯 **研究动机**：AI 审稿被寄望解决同行评审危机，但其可靠性缺乏严格评估
- 🔬 **研究方法**：比较 ICLR 2026 人类与 AI 生成审稿，并评测自动化论文改写对不同 AI 审稿人的影响
- 📌 **结论**：AI 审稿存在过度一致的 hivemind effect，且 paper laundering 式风格改写即可显著抬分；在建立 peer-review automation science 前不应自动化审稿

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that today's AI systems should not be used to produce paper reviews. We ground this position in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a hivemind effect of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through paper laundering: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers, demonstrating that LLM reviewers are easy to game through stylistic changes rather than scientific results. However, non-gameability and review diversity are necessary but not sufficient conditions for automation. We argue that addressing the peer review crisis requires a science of peer review automation -- not general-purpose LLMs deployed without rigorous evaluation.

</details>

### 19. BadScientist: Can a Research Agent Write Convincing but Unsound Papers that Fool LLM Reviewers?

🎓 [Official](https://aclanthology.org/2026.acl-long.1134/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`agent safety`、`LLM agent`、`AI peer review`、`tool-use attack`

👤 **作者**：Fengqing Jiang、Yichen Feng、Yuetai Li、Luyao Niu、Basel Alomair、Radha Poovendran

- 🎯 **研究动机**：LLM 研究助手与 AI 评审系统结合形成无人类监督的全自动发表闭环，其漏洞未知
- 🔬 **研究方法**：BadScientist 评估伪造导向论文生成 agent 对多模型 LLM 评审系统的欺骗能力：生成器用无需真实实验的呈现操纵策略，评测框架带浓度界与校准分析的形式误差保证
- 📌 **结论**：伪造论文接受率最高达 82%；存在关注-接受冲突（评审标记诚信问题却给接受级分数），缓解策略仅边际改善，检测准确率接近随机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The convergence of LLM-powered research assistants and AI-based peer review systems creates a critical vulnerability: fully automated publication loops where AI-generated research is evaluated by AI reviewers without human oversight. We investigate this through BadScientist, a framework that evaluates whether fabrication-oriented paper generation agents can deceive multi-model LLM review systems. Our generator employs presentation-manipulation strategies requiring no real experiments. We develop a rigorous evaluation framework with formal error guarantees (concentration bounds and calibration analysis), calibrated on real data. Our results reveal systematic vulnerabilities: fabricated papers achieve acceptance rates up to 82%. Critically, we identify concern-acceptance conflict—reviewers frequently flag integrity issues yet assign acceptance-level scores. Our mitigation strategies show only marginal improvements, with detection accuracy barely exceeding random chance. Despite provably sound aggregation mathematics, integrity checking systematically fails, exposing fundamental limitations in current AI-driven review systems and underscoring the urgent need for defense-in-depth safeguards in scientific publishing.

</details>

### 20. CoCoNUTS: Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1240/)　📅 2026　🏷 ACL 2026

**关键词**：`survey`、`detection`、`AI-generated content`、`AI peer review`、`review validity`、`open-set detection`

👤 **作者**：Yihan Chen、…、Le Sun

- 🎯 **研究动机**：会议政策允许 AI 润色语言但禁止生成实质内容，依赖风格线索的检测器无法区分表面润色与内容生成
- 🔬 **研究方法**：内容检测范式：构建含 315,535 条评论、覆盖主流 AI 会议与六种人机协作模式的 CoCoNUTS 基准，并提出识别实质 AI 生成的 CoCoDet
- 📌 **结论**：CoCoDet macro F1 达 98.24%，对允许的机器润色评论假阳性仅 3.89%（最强基线 7.84%）；真实评论中实质 AI 生成呈上升趋势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing use of large language models (LLMs) in peer review threatens scholarly integrity. Recent conference policies allow AI tools for language polishing but prohibit their use for generating substantive content. However, existing detectors mainly rely on stylistic cues, making it difficult to distinguish between surface-level language refinement and genuine content generation. To address this, we advocate a content-based detection paradigm and introduce CoCoNUTS, a comprehensive benchmark containing 315,535 reviews covering leading AI conferences and six human-AI collaboration modes. Our evaluation shows that current detectors struggle to handle these nuanced settings. Consequently, we propose CoCoDet, an AI review detector designed to identify substantive AI-generation. Experiments demonstrate that CoCoDet achieves a macro F1-score of 98.24%. Crucially, on permissible machine-polished reviews, it maintains a low false positive rate of 3.89%, substantially outperforming the strongest baseline (7.84%). Examination on real-world reviews using CoCoDet reveals an escalating trend of substantive AI generation. Our work exposes the inadequacy of current detectors, underscoring the importance of domain-specific solutions.

</details>

### 21. CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review

📄 [arXiv](https://arxiv.org/abs/2609.05227)　📅 2026-09

**关键词**：`analysis`、`multi-agent collusion`、`peer-review integrity`、`bidding attack`

👤 **作者**：Jicheng Zhou、…、Jiantao Zhou

- 🎯 **研究动机**：AAAI-27 周期暴露评审合谋 bidding 风险，但 bidding、分配与评审操纵被分开研究，且真实会议缺反事实与不可观测的合谋意图
- 🔬 **研究方法**：提出 CABAL 端到端多 Agent 仿真框架：固定会议环境，为 LLM 评审 Agent 配置诚实或合谋策略，并用相互评审-论文亲和度构建合谋环选择目标论文，发起专业一致而非任意定向的攻击
- 📌 **结论**：合谋 bidding 使目标论文捕获率翻倍以上，被指派合谋者比诚实共审给目标论文高约 2 分，全会影响相对温和；bid 相位检测器受良性亲和度干扰，仅 Very-High 诊断视图能精确但低覆盖地局部恢复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent reports during the AAAI-27 review cycle highlight the risk of reviewers coordinating bids for reciprocal assignment advantage. Prior work treats bidding, reviewer assignment, and review manipulation as separate stages, leaving the lifecycle effects of collusive bidding unclear. Real-world analysis is further constrained by typically unobservable collusive intent and the lack of counterfactuals for the same conference. Motivated by this gap, we introduce \alg, an end-to-end multi-agent simulacra framework for studying reviewer assignment integrity by holding the conference environment fixed and configuring LLM-driven reviewer agents with honest or collusive policies. We further develop an affinity-guided collusive bidding strategy that uses mutual reviewer-paper affinities to construct collusion rings and select target papers, producing expertise-consistent rather than arbitrarily targeted attacks. Controlled experiments show that collusive bidding more than doubles target-paper capture and that assigned colluders score target papers about two points higher than honest co-reviewers, while conference-wide effects remain comparatively modest. Evaluated bid-phase detectors provide only limited evidence of collusion: in a fixed-triplet detector stress test, native positive-bid graphs are confounded by benign affinity, while a Very-High-only diagnostic view enables precise but low-coverage local recovery.

</details>

### 22. When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation

📄 [arXiv](https://arxiv.org/abs/2609.20942)　📅 2026-09

**关键词**：`analysis`、`peer review`、`judgment collapse`、`recursive training`、`contamination mitigation`

👤 **作者**：Sy-Tuyen Ho、Minghui Liu、Furong Huang

- 🎯 **研究动机**：LLM 既当自动评审又当人类评审助手，模型生成的评审进入公共数据与未来训练语料——AI 同行评审可变递归：后续评审者从早期模型的判断中学习
- 🔬 **研究方法**：受控研究一步反馈环：Llama 3.1 8B 先在 ICLR 2018-2023 官方评审上微调，再在 ICLR 2024 数据（官方/模型生成评审按系统变化的比例混合）上训练四个后继；提出 TrustReviewer 开源评审系统，在训练时（精选语料单阶段）与推理时双阶段干预
- 📌 **结论**：引入合成评审压缩评分分布、降低同论文与语料级语义多样性——scientific-judgment collapse；TrustReviewer 缓解该失效——AI 参与的科学评价的递归污染实证与对策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly participate in scientific evaluation, both as automated reviewers and as assistants to human reviewers. As model-generated reviews enter public data and future training corpora, AI peer review can become recursive: later reviewers learn from judgments produced by earlier models. We study one step of this feedback loop in a controlled setting. Starting from Llama 3.1 8B, we first fine-tune a reviewer on official ICLR reviews from 2018--2023 and then train four successor models on ICLR 2024 data with systematically varied mixtures of official and model-generated reviews. Our study shows that introducing synthetic reviews compresses rating distributions and reduces both same-paper and corpus-level semantic diversity. We call this pattern $\textbf{scientific-judgment collapse}$. To mitigate this failure mode, we introduce $\textbf{TrustReviewer}$, an open-source LLM-based system for generating peer reviews of AI and machine learning papers. TrustReviewer intervenes at two complementary stages. For training-time prevention, we train the core reviewer in a single stage on a curated corpus designed to reduce low-quality and semantically degenerate supervision. For test-time correction, paired activation steering aims to further mitigate residual tendencies toward collapsed judgments without further training or additional expert annotation. Together, these results characterize a concrete risk of recursive reviewer training and provide practical interventions for preserving judgment diversity and improving recommendation alignment in AI-assisted scientific evaluation.

</details>
