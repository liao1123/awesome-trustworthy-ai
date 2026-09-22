# Generative Engine Optimization Security

[返回投毒与后门目录](README.md)

## 研究方向

本页研究 Generative Engine Optimization（GEO）如何通过改写网页文本、图像或结构信号改变生成式搜索中的检索、重排、引用、可见性和推荐结果。GEO 本身包含正常的内容适配与可用性优化；安全问题出现在攻击者利用同一机制操纵排名、伪装低质量或有缺陷的对象、压制竞争者，或让 prompt injection 穿过 retriever-reranker-generator 全链路。因而本页同时保留 cooperative GEO 基础、现实 pipeline 评测和 black-hat manipulation，避免把“提升可见性”直接等同于攻击。

## 研究脉络

- **可见性优化起点：** GEO 建立生成式回答中的 visibility metric 与 GEO-Bench，研究对象由传统网页排名转向内容是否被 LLM 选择、引用和写入回答；C-SEO Bench 的多域多行动者评测则表明多数 C-SEO 方法基本无效且收益随采用者增多递减。
- **自动化与个性化优化：** AutoGEO、Mind Reader 与 AgenticGEO 从人工 heuristic 发展到 preference rule、latent user demand 和自演化 strategy search，提升内容适配能力的同时也扩大可自动化操纵的空间。
- **Black-hat rank manipulation：** Adversarial SEO、StealthRank、LLM ranker injection 与 MGEO 分别利用网页指令、可读文本 suffix、token optimization 和图文联合扰动提升目标排名。
- **全链路现实性：** SAGEO Arena、GEO-Bench 与 RAG survival 分析表明，能影响 generator 不代表能通过 retriever 与 reranker；结构信号、攻击隐蔽性和真实 search interface 都会改变结论。
- **下游安全影响：** SafeGEO 把指标从 target rank 扩展到推荐集合中的实际危害，One Polluted Page 表明单页污染即可让 LLM 推荐器批量推广虚构产品，EcoGEO 则把单页改写升级为沿 agent 浏览轨迹协同的跨页证据生态（收益来自塑造证据获取过程而非堆内容）；当前防御多为静态 detector 或 prompt guard，SCI-Defense 的语义完整性评分在产品描述域近满分但在通用网页域失效，也佐证防御的场景依赖性。

- **测量效度与生态动力学：** 可见性测量从单点走向分布与效度审视（Don't Measure Once 的重复测量、Answer Market 的 prompt 语料即市场定义、Citation Absorption 的被引≠被吸收），三层品牌阶梯与引用偏差给出大规模实证；CHASE 仿真显示 20 轮 GEO 使质量-排序对齐系统性下降（六域 ρ 均值 -0.068），VCR 机制设计与 ICML 2026 position 分别给出平台侧激励治理与答案级治理的路线。
## Cooperative GEO 与基础方法

### 1. Mind Reader: Latent User Demand-Guided Content Optimization for Generative Search Engine

🎓 [Official](https://aclanthology.org/2026.acl-long.1894/)　📅 2026-07　🏷 ACL 2026

**关键词**：`tool`、`latent user demand`、`query augmentation`、`content visibility`

👤 **作者**：Tong Chen、…、Zhaoran Fan

- 🎯 **研究动机**：现有 GEO 内容优化依赖经验策略或查询偏好，忽略驱动检索与生成的潜在用户搜索需求
- 🔬 **研究方法**：分解-重组查询增强模块捕获潜在语义，推理覆盖内容优化模块使内容覆盖 GSE 关键推理信息
- 📌 **结论**：GEO-Bench 与 PC-GEO 上客观指标最多提升 2.44 倍、主观指标平均 1.23 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Search Engines (GSEs) have reshaped information retrieval, and Generative Engine Optimization (GEO) emerges to improve the content visibility in GSEs’ responses. Previous methods mainly rely on empirical strategies or query-dependent preferences of GSEs for content optimization. However, they remain limited in effectiveness as they overlook the latent user search demands in queries that drive content retrieval and response generation of GSEs. To address this, we propose Mind Reader, a novel GEO method to effectively improve the content visibility within the generated responses of GSEs through content optimization guided by the extracted latent demands of user search. Specifically, we propose a decomposition-recombination query augmentation module, which enriches the query with latent semantic information by decomposing it into diverse perspectives, capturing underlying semantic information, and recombining them into variants to support subsequent optimization. Then, we propose a reasoning coverage content optimization module. By optimizing content to cover critical reasoning information of GSEs, we align the content with the user search demands, effectively improving the content visibility. Extensive experiments on widely used GEO-Bench and our proposed PC-GEO show that our method significantly outperforms baselines and effectively improves content visibility (with up to 2.44x objective metrics and 1.23x subjective metrics on average).

</details>

### 2. AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2603.20213)　📅 2026-03

**关键词**：`tool`、`strategy evolution`、`MAP-Elites`、`co-evolving critic`

👤 **作者**：Jiaqi Yuan、Jialu Wang、Zihan Wang、Qingyun Sun、Ruijie Wang、Jianxin Li

- 🎯 **研究动机**：静态启发式、单提示优化与偏好规则蒸馏均难适配多样内容与生成式引擎的行为变化，且引擎交互反馈成本高
- 🔬 **研究方法**：AgenticGEO 把优化形式化为内容条件控制问题，用 MAP-Elites 档案演化多样组合策略，Co-Evolving Critic 代理引擎反馈以降低交互成本
- 📌 **结论**：在两个引擎上达 SOTA 且跨域迁移稳健，超 14 个基线（3 个数据集）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative search engines represent a transition from traditional ranking-based retrieval to Large Language Model (LLM)-based synthesis, transforming optimization goals from ranking prominence towards content inclusion. Generative Engine Optimization (GEO), specifically, aims to maximize visibility and attribution in black-box summarized outputs by strategically manipulating source content. However, existing methods rely on static heuristics, single-prompt optimization, or engine preference rule distillation that is prone to overfitting. They cannot flexibly adapt to diverse content or the changing behaviors of generative engines. Moreover, effectively optimizing these strategies requires an impractical amount of interaction feedback from the engines. To address these challenges, we propose AgenticGEO, a self-evolving agentic framework formulating optimization as a content-conditioned control problem, which enhances intrinsic content quality to robustly adapt to the unpredictable behaviors of black-box engines. Unlike fixed-strategy methods, AgenticGEO employs a MAP-Elites archive to evolve diverse, compositional strategies. To mitigate interaction costs, we introduce a Co-Evolving Critic, a lightweight surrogate that approximates engine feedback for content-specific strategy selection and refinement, efficiently guiding both evolutionary search and inference-time planning. Through extensive in-domain and cross-domain experiments on two representative engines, AgenticGEO achieves state-of-the-art performance and demonstrates robust transferability, outperforming 14 baselines across 3 datasets. Our code and model are available at: https://github.com/AIcling/agentic_geo.

</details>

### 3. Diagnosing and Repairing Citation Failures in Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2603.09296)　📅 2026-03

**关键词**：`tool`、`citation failure`、`AgentGEO`、`document repair`

👤 **作者**：Zhihua Tian、Yuhan Chen、Yao Tang、Jian Liu、Ruoxi Jia

- 🎯 **研究动机**：GEO 方法度量文档贡献而非真正引流回创作者的引用，且统一改写规则不诊断单文档未被引的原因
- 🔬 **研究方法**：建立首个引用失效模式分类法；AgentGEO 据此诊断失效并从工具库选择针对性修复，迭代至获得引用，配 document-centric 基准
- 📌 **结论**：引用率相对提升超 40% 而仅修改 5% 内容（基线需 25%）；通用优化会伤害长尾内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) aims to improve content visibility in AI-generated responses. However, existing methods measure contribution-how much a document influences a response-rather than citation, the mechanism that actually drives traffic back to creators. Also, these methods apply generic rewriting rules uniformly, failing to diagnose why individual document are not cited. This paper introduces a diagnostic approach to GEO that asks why a document fails to be cited and intervenes accordingly. We develop a unified framework comprising: (1) the first taxonomy of citation failure modes spanning different stages of a citation pipeline; (2) AgentGEO, an agentic system that diagnoses failures using this taxonomy, selects targeted repairs from a corresponding tool library, and iterates until citation is achieved; and (3) a document-centric benchmark evaluating whether optimizations generalize across held-out queries. AgentGEO achieves over 40% relative improvement in citation rates while modifying only 5% of content, compared to 25% for baselines. Our analysis reveals that generic optimization can harm long-tail content and some documents face challenges that optimization alone cannot fully address-findings with implications for equitable visibility in AI-mediated information access.

</details>

### 4. What Generative Search Engines Like and How to Optimize Web Content Cooperatively

📄 [arXiv](https://arxiv.org/abs/2510.11438) · 📝 [OpenReview](https://openreview.net/forum?id=K8EinVWtUB) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010153)　📅 2025-10　🏷 ICLR 2026

**关键词**：`tool`、`AutoGEO`、`preference rules`、`search utility`

👤 **作者**：Yujiang Wu、Shanshan Zhong、Yubin Kim、Chenyan Xiong

- 🎯 **研究动机**：内容提供者不了解生成式引擎选用内容的偏好，GEO 缺乏自动化优化手段
- 🔬 **研究方法**：AutoGEO 让前沿 LLM 解释引擎偏好并抽取 preference rules，既作为上下文工程驱动 prompt 版 AutoGEO_API，又作为规则奖励训练低成本的 AutoGEO_Mini
- 📌 **结论**：在 GEO-Bench 与两个真实查询新基准上提升内容可见度同时保持搜索效用，学到的规则跨领域稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

By employing large language models (LLMs) to retrieve documents and generate natural language responses, Generative Engines, such as Google AI overview and ChatGPT, provide significantly enhanced user experiences and have rapidly become the new form of search. Their rapid adoption also drives the needs of Generative Engine Optimization (GEO), as content providers are eager to gain more traction from them. In this paper, we introduce AutoGEO, a framework to automatically learn generative engine preferences when using retrieved contents for response generation, and rewrite web contents for more such traction. AutoGEO first prompts frontier LLMs to explain generative engine preferences and extract meaningful preference rules from these explanations. Then it uses preference rules as context engineering for AutoGEO$_\text{API}$, a prompt-based GEO system, and as rule-based rewards to train AutoGEO$_\text{Mini}$, a cost-effective GEO model. Experiments on the standard GEO-Bench and two newly constructed benchmarks using real user queries demonstrate the effectiveness of AutoGEO in enhancing content traction while preserving search utility. Analyses confirm the learned rules' robustness and abilities to capture unique preferences in variant domains, and AutoGEO systems' ability to embed them in content optimization. The code is released at https://github.com/cxcscmu/AutoGEO.

</details>

### 5. GEO: Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2311.09735) · 🌐 [Project](https://doi.org/10.1145/3637528.3671900)　📅 2023-11　🏷 KDD 2024

**关键词**：`tool`、`GEO-Bench`、`visibility metric`、`content optimization`

👤 **作者**：Pranjal Aggarwal、Vishvak Murahari、Tanmay Rajpurohit、Ashwin Kalyan、Karthik Narasimhan、Ameet Deshpande

- 🎯 **研究动机**：生成式引擎崛起使创作者对内容何时、如何被展示失去控制，传统 SEO 无法衡量
- 🔬 **研究方法**：形式化 GEO 范式：黑盒优化框架与可定义 visibility 指标，并发布多领域大规模查询基准 GEO-bench
- 📌 **结论**：GEO 可把生成式回答中的内容可见性提升至多 40%，策略效果随领域差异显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advent of large language models (LLMs) has ushered in a new paradigm of search engines that use generative models to gather and summarize information to answer user queries. This emerging technology, which we formalize under the unified framework of generative engines (GEs), can generate accurate and personalized responses, rapidly replacing traditional search engines like Google and Bing. Generative Engines typically satisfy queries by synthesizing information from multiple sources and summarizing them using LLMs. While this shift significantly improves $\textit{user}$ utility and $\textit{generative search engine}$ traffic, it poses a huge challenge for the third stakeholder -- website and content creators. Given the black-box and fast-moving nature of generative engines, content creators have little to no control over $\textit{when}$ and $\textit{how}$ their content is displayed. With generative engines here to stay, we must ensure the creator economy is not disadvantaged. To address this, we introduce Generative Engine Optimization (GEO), the first novel paradigm to aid content creators in improving their content visibility in generative engine responses through a flexible black-box optimization framework for optimizing and defining visibility metrics. We facilitate systematic evaluation by introducing GEO-bench, a large-scale benchmark of diverse user queries across multiple domains, along with relevant web sources to answer these queries. Through rigorous evaluation, we demonstrate that GEO can boost visibility by up to $40\%$ in generative engine responses. Moreover, we show the efficacy of these strategies varies across domains, underscoring the need for domain-specific optimization methods. Our work opens a new frontier in information discovery systems, with profound implications for both developers of generative engines and content creators.

</details>

### 6. Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems

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

### 7. The Vulnerability of LLM Rankers to Prompt Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2602.16752) · 🌐 [Project](https://doi.org/10.1145/3805712.3808553)　📅 2026-02　🏷 SIGIR 2026

**关键词**：`attack`、`ranker prompt injection`、`objective hijack`、`criteria hijack`、`LLM ranker`

👤 **作者**：Yu Yin、Shuai Wang、Bevan Koopman、Guido Zuccon

- 🎯 **研究动机**：候选文档内 prompt 注入可操纵 LLM 排序，但该脆弱性跨模型家族与设定的边界未探明
- 🔬 **研究方法**：在 pairwise/listwise/setwise 三种排序范式下系统评估目标劫持与准则劫持两种注入，度量 ASR 与 nDCG@10 影响
- 📌 **结论**：刻画了脆弱性边界条件，发现 encoder-decoder 架构对越狱注入具有固有强韧性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have emerged as powerful re-rankers. Recent research has however showed that simple prompt injections embedded within a candidate document (i.e., jailbreak prompt attacks) can significantly alter an LLM's ranking decisions. While this poses serious security risks to LLM-based ranking pipelines, the extent to which this vulnerability persists across diverse LLM families, architectures, and settings remains largely under-explored. In this paper, we present a comprehensive empirical study of jailbreak prompt attacks against LLM rankers. We focus our evaluation on two complementary tasks: (1) Preference Vulnerability Assessment, measuring intrinsic susceptibility via attack success rate (ASR); and (2) Ranking Vulnerability Assessment, quantifying the operational impact on the ranking's quality (nDCG@10). We systematically examine three prevalent ranking paradigms (pairwise, listwise, setwise) under two injection variants: decision objective hijacking and decision criteria hijacking. Beyond reproducing prior findings, we expand the analysis to cover vulnerability scaling across model families, position sensitivity, backbone architectures, and cross-domain robustness. Our results characterize the boundary conditions of these vulnerabilities, revealing critical insights such as that encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks. We publicly release our code and additional experimental results at https://github.com/ielab/LLM-Ranker-Attack.

</details>

### 8. Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers

📄 [arXiv](https://arxiv.org/abs/2601.12263) · 🎓 [Official](https://aclanthology.org/2026.knowfm-1.9/)　📅 2026-01

**关键词**：`attack`、`multimodal GEO`、`image perturbation`、`text suffix`

👤 **作者**：Yixuan Du、Chenxiao Yu、Haoyan Xu、Ziyi Wang、Yue Zhao、Xiyang Hu

- 🎯 **研究动机**：VLM ranker 的跨模态知识接地能否被内容提供者反向利用不明
- 🔬 **研究方法**：MGEO 以交替优化联合构造不可感知图像扰动与流畅文本后缀，利用模型内部跨模态知识耦合操纵商品排序
- 📌 **结论**：排名操纵效果大幅超过单模态攻击与商业模型驱动的启发式基线，表层内容质量不足以保障多模态排序的忠实性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) integrate visual and textual knowledge into unified representations that increasingly underpin modern retrieval and recommendation systems. However, it remains unclear how reliably these models utilize their cross-modal knowledge when ranking multimodal items, and whether their knowledge grounding can be subverted. In this paper, we expose a fundamental vulnerability in how VLMs apply multimodal knowledge for product ranking: through Multimodal Generative Engine Optimization (MGEO), we show that an adversary can manipulate a VLM's ranking decisions by jointly crafting imperceptible image perturbations and fluent textual suffixes that exploit the model's internal cross-modal knowledge coupling. Using an alternating optimization strategy, MGEO targets the deep interactions between visual and linguistic representations within the VLM, achieving rank manipulations that substantially exceed those of unimodal attacks and heuristic baselines powered by strong commercial models. Our findings reveal that surface-level content quality is insufficient for rank promotion; instead, direct alignment with the model's internal knowledge utilization mechanism is required. These results raise important questions on the faithfulness and robustness of knowledge grounding in multimodal foundation models, and motivate future work on defense mechanisms for multimodal retrieval systems. Code is available at: https://github.com/glad-lab/MGEO

</details>

### 9. StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization

📄 [arXiv](https://arxiv.org/abs/2504.05804)　📅 2025-04

**关键词**：`attack`、`stealthy suffix`、`energy-based model`、`rank manipulation`

👤 **作者**：Yiming Tang、Yi Fan、Chenxiao Yu、Tiankai Yang、Yue Zhao、Xiyang Hu

- 🎯 **研究动机**：LLM 驱动的排序系统易被对抗排名操纵，已有方法引入可检测的文本异常
- 🔬 **研究方法**：提出 StealthRank，以能量模型优化与 Langevin 动力学在物品描述中嵌入 StealthRank Prompts，隐蔽影响 LLM 排序
- 📌 **结论**：多个 LLM 上有效性与隐蔽性均超 SoTA 对抗排序基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of large language models (LLMs) into information retrieval systems introduces new attack surfaces, particularly for adversarial ranking manipulations. We present $\textbf{StealthRank}$, a novel adversarial attack method that manipulates LLM-driven ranking systems while maintaining textual fluency and stealth. Unlike existing methods that often introduce detectable anomalies, StealthRank employs an energy-based optimization framework combined with Langevin dynamics to generate StealthRank Prompts (SRPs)-adversarial text sequences embedded within item or document descriptions that subtly yet effectively influence LLM ranking mechanisms. We evaluate StealthRank across multiple LLMs, demonstrating its ability to covertly boost the ranking of target items while avoiding explicit manipulation traces. Our results show that StealthRank consistently outperforms state-of-the-art adversarial ranking baselines in both effectiveness and stealth, highlighting critical vulnerabilities in LLM-driven ranking systems. Our code is publicly available at $\href{https://github.com/Tangyiming205069/controllable-seo}{here}$.

</details>

### 10. Adversarial Search Engine Optimization for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2406.18382) · 📝 [OpenReview](https://openreview.net/forum?id=hkdqxN3c7t)　📅 2024-06　🏷 ICLR 2025

**关键词**：`attack`、`preference manipulation`、`third-party content`、`competitive ranking`

👤 **作者**：Fredrik Nestaas、Edoardo Debenedetti、Florian Tramèr

- 🎯 **研究动机**：LLM 越来越多地在竞争性第三方内容间做选择，偏好操纵风险未被研究
- 🔬 **研究方法**：Preference Manipulation Attack：精心构造网站内容或插件文档，诱导 LLM 推广攻击者产品并贬低竞争者
- 📌 **结论**：在 Bing、Perplexity 与 GPT-4/Claude 插件 API 上均有效，且形成各方皆攻、集体受损的囚徒困境

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly used in applications where the model selects from competing third-party content, such as in LLM-powered search engines or chatbot plugins. In this paper, we introduce Preference Manipulation Attacks, a new class of attacks that manipulate an LLM's selections to favor the attacker. We demonstrate that carefully crafted website content or plugin documentations can trick an LLM to promote the attacker products and discredit competitors, thereby increasing user traffic and monetization. We show this leads to a prisoner's dilemma, where all parties are incentivized to launch attacks, but the collective effect degrades the LLM's outputs for everyone. We demonstrate our attacks on production LLM search engines (Bing and Perplexity) and plugin APIs (for GPT-4 and Claude). As LLMs are increasingly used to rank third-party content, we expect Preference Manipulation Attacks to emerge as a significant threat.

</details>

### 11. SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents

📄 [arXiv](https://arxiv.org/abs/2606.28356)　📅 2026-06

**关键词**：`benchmark`、`recommendation agent`、`unsafe promotion`、`GEO defense`

👤 **作者**：Qianfeng Wen、…、Zhenwei Tang

- 🎯 **研究动机**：GEO 让卖家改写内容以提升生成系统可见度，推荐 agent 可能因此把缺陷产品显得更有据可依
- 🔬 **研究方法**：构建 SafeGEO 评估套件：600 个推荐案例上 22 种 GEO 攻击变体，并测试防御性提示与结构化证据检查等 agent 侧缓解
- 📌 **结论**：GEO 攻击使缺陷产品进入推荐集的比率最高提升 83.2%；简单防御最多降低 39.2% 有害推广但仍无法恢复无 GEO 水平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) lets content owners rewrite web content to increase their visibility in generative systems. In recommendation agents, this creates a risk that seller-controlled sources make flawed products appear better supported than they are. We study this risk by asking whether recommendation agents preserve utility-aligned decisions when seller-controlled sources are rewritten for GEO. To make this question measurable, we construct SafeGEO, an evaluation suite with 22 GEO attack variants across 600 recommendation cases. We empirically show that GEO attacks can promote flawed target products. On average, they increase the rate at which such flawed products enter the recommendation set by up to 83.2%. We further study whether agent-side design choices can mitigate this risk and show that simple defenses, including defensive prompting and structured evidence checks, reduce harmful target promotion by up to 39.2%. These gains are substantial but do not restore the no-GEO performance, showing that GEO remains a serious risk despite developer-side mitigation.

</details>

### 12. Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2609.02316) · 🤗 [Model](https://huggingface.co/counter-geo/c-geo-guard) · 📊 [Dataset](https://huggingface.co/datasets/counter-geo/counter-geo-bench)　📅 2026-09

**关键词**：`benchmark`、`GEO poisoning`、`misinformation`、`defense evaluation`

👤 **作者**：Bing Zheng、Zongyao Zhao、Wenming Yang

- 🎯 **研究动机**：GEO 优化文档看似普通却能把定向错误信息送进生成式搜索答案，而缺少可控条件下的防御评测基准
- 🔬 **研究方法**：构建 Counter-GEO-Bench：247 个人工核验、质量门控的 query 配对信息保真与信息扭曲 GEO 改写，跨三个受害 LLM 评测 ASR、误报与答案质量
- 📌 **结论**：Granite Guardian、Llama Guard 3 与 NeMo Self-Check 最多相对降 ASR 5.7%（其一不显著）；轻量基线 C-GEO Guard 相对降 47.6% 且近零效用损失，证明该威胁可治理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative engine optimization (GEO) enables content producers to increase the visibility of their web pages in generative search engines, but the same techniques can deliver targeted misinformation when adversaries publish ordinary-looking GEO-optimized documents that victim large language models (LLMs) retrieve and synthesize into distorted answers. No existing benchmark evaluates defenses against this threat under controlled conditions. Therefore, we present Counter-GEO-Bench, a defense benchmark that pairs 247 human-verified, quality-gated queries with information-preserving and information-distorting GEO rewrites, and evaluates defenses on attack success rate (ASR), false positive rate, and answer quality across three victim LLMs. Under Counter-GEO-Bench, three off-the-shelf defenses (Granite Guardian, Llama Guard 3, and NeMo Self-Check Fact-Checking) reduce ASR by at most 5.7% relative, while Granite Guardian's reduction is not statistically significant. Safety-taxonomy guardrails target policy violations, while GEO misinformation passes through them as fluent informational content. To this end, a lightweight benchmark baseline, C-GEO Guard, is proposed, reducing ASR by 47.6% relative with near-zero utility loss, which proves threat tractable.

</details>

### 13. What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study

📄 [arXiv](https://arxiv.org/abs/2607.15771)　📅 2026-07

**关键词**：`analysis`、`Chinese GSE`、`citation ecology`、`interface variance`

👤 **作者**：Tao Zhen、Yue Liu、Gege Zhang、Yixuan Niu

- 🎯 **研究动机**：中文生成式搜索正在重塑信息可见性，其引用与呈现行为缺乏大规模实证刻画
- 🔬 **研究方法**：对四个主流平台 Web/App 八个界面做受控实验：614 查询 x 三次重复，从 214,119 条原始记录构建 160,860 条引用级数据，分析引用行为、来源归因、实体曝光与跨界面一致性
- 📌 **结论**：品牌入选率仅 8.3%，约 13% 品牌曝光与 71% 联系方式曝光无法匹配同期引用池或正文，同平台 App 与 Web 界面来源集系统性不同

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative AI question-answering systems increasingly mediate information access, shifting content visibility from ranked search results to retrieval, citation, and presentation in generated answers. We conduct a large-scale empirical study of Chinese-language generative search across the Web and App interfaces of four mainstream platforms. The controlled design covers eight platform interfaces, 614 queries, and three replications per query-platform-interface combination. From 214,119 raw records, we construct a cleaned citation-level dataset of 160,860 records and analyze citation behavior, source attribution, entity exposure, and cross-interface consistency. Five findings emerge. First, brands in the citation pool were selectively surfaced in answers: the overall brand-selection rate was 8.3%, and 12.4% of retrieved sources containing contact information contributed contact information to answers. Second, content fit, cross-source occurrence count, and semantic role were relatively important in predictive models, whereas the 5118-Baidu Composite Quality Score was not the leading predictor for any examined outcome. Third, among cited pages with publication dates, fitted half-lives were approximately 39 days for high-timeliness queries and 68 days for low-timeliness queries. Fourth, approximately 13% of brand exposures could not be matched to the contemporaneous citation pool, and approximately 71% of contact-information exposures could not be matched to the crawled body text. Fifth, source sets differed systematically between the App and Web interfaces of the same platform. These results characterize how Chinese-language generative search systems select, attribute, and surface information and show that interface type is an important dimension of analysis.

</details>

### 14. GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2605.29107)　📅 2026-05

**关键词**：`benchmark`、`GEO attack`、`ranking manipulation`、`stealth evaluation`

👤 **作者**：Ojas Nimase、Zhe Chen、Gengpei Qi、Yue Zhao、Xiyang Hu

- 🎯 **研究动机**：GEO 操控方法各用各的数据与指标评测，相对强度与可检测性不明
- 🔬 **研究方法**：GEO-Bench 统一协议评测黑盒 prompt 攻击（TAP、Zero-Shot）、白盒梯度攻击（STS、RAF、StealthRank）与十种白帽 C-SEO，固定 Llama-3.1-8B 排序器，效果与隐蔽性双维打分
- 📌 **结论**：有效性与隐蔽性相互制衡；黑盒内容改写在排名提升上可匹敌或超过梯度攻击且文本更流畅，部分域可躲过关键词与困惑度检测；访问权限不预测攻击强度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly rank products, documents, and recommendations for user queries, which makes manipulating these rankings a growing concern for fairness and information integrity. Research on generative engine optimization (GEO) has produced many manipulation methods, but each is evaluated on its own dataset with its own metrics, so their relative strength and detectability stay unclear. We present GEO-Bench, a benchmark that evaluates GEO ranking-manipulation attacks under one protocol. It unifies black-box prompt-based attacks (TAP, Zero-Shot), white-box gradient-based attacks (STS, RAF, StealthRank), and ten white-hat C-SEO strategies. We score every method on five datasets against a fixed open-weight ranker (Llama-3.1-8B-Instruct), using metrics for both effectiveness (NRG, Success@α, Promote@α) and stealth (keyword violation rate, perplexity ratio). Our evaluation shows that effectiveness and stealth trade off across adversarial attacks, that black-box content rewriting matches or exceeds gradient-based attacks on rank promotion while producing more fluent text and can evade both keyword- and perplexity-based detection on some domains, and that the access model does not predict attack strength. By standardizing datasets, attack implementations, and metrics, GEO-Bench enables the first direct comparison across these attack paradigms and supports the development of detection methods.

</details>

### 15. Can It Reach the Generator? Investigating the Survival of Prompt-Injection Attacks in Realistic RAG Settings

📄 [arXiv](https://arxiv.org/abs/2605.28017)　📅 2026-05

**关键词**：`analysis`、`RAG pipeline`、`attack survival`、`retriever-reranker`

👤 **作者**：Yu Yin、Shuai Wang、Bevan Koopman、Guido Zuccon

- 🎯 **研究动机**：GEO 攻击研究假设毒文档直接送入生成器、绕过检索与重排，高估了现实威胁
- 🔬 **研究方法**：在检索器到 LLM 重排再到 LLM 生成的三阶段管线下重评七种 GEO 攻击的存活
- 📌 **结论**：梯度与指令覆盖类攻击多在前级崩溃，仅 LLM 驱动的注入端到端有效；小攻击集微调的轻量注入 guard 可检出全部已测攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent generative engine optimisation (GEO) research has shown that prompt-injection attacks can push a target product to the top of an LLM's recommendation list, with the strongest attacks reporting around $80\%$ success and raising serious security concerns about RAG-based recommendation. However, these results assume the attacked document is always fed directly to the generator, bypassing the retriever and reranker. This is unrealistic: in deployed RAG systems, the attack modifies the document content, which can in turn change whether the document is retrieved and reranked highly enough to reach the generator at all. In this paper, we re-evaluate seven GEO attacks under a realistic three-stage pipeline (retriever\,$\to$\,LLM reranker\,$\to$\,LLM generator). We find that prior protocols substantially overstate attack effectiveness: gradient-based and instruction override attacks largely collapse before reaching the generator, and only LLM-driven prompt injections remain effective end-to-end. Our analysis further reveals that current GEO attacks are easily detectable: a lightweight prompt-injection guard finetuned on a small attack dataset already detects every attack. Our code and data are available at https://github.com/ielab/geo_injection_rag_survival.

</details>

### 16. Unveiling the Resilience of LLM-Enhanced Search Engines against Black-Hat SEO Manipulation

📄 [arXiv](https://arxiv.org/abs/2603.25500) · 🌐 [Project](https://www2026.thewebconf.org/accepted/research-tracks.html)　📅 2026-03

**关键词**：`analysis`、`black-hat SEO`、`retrieval filter`、`SEO-Bench`

👤 **作者**：Pei Chen、…、Min Yang

- 🎯 **研究动机**：LLM 增强搜索引擎对成熟黑帽 SEO 攻击的抵御能力未探索
- 🔬 **研究方法**：构建含 1,000 个真实黑帽 SEO 网站的 SEO-Bench，评测 10 个 LLMSE 产品，并提出 7 种 LLMSEO 攻击策略
- 📌 **结论**：传统 SEO 攻击 99.78% 被缓解（主要在检索阶段过滤），但 rewritten-query stuffing 与分段文本使操纵率较基线翻倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of Large Language Model-enhanced Search Engines (LLMSEs) has revolutionized information retrieval by integrating web-scale search capabilities with AI-powered summarization. While these systems demonstrate improved efficiency over traditional search engines, their security implications against well-established black-hat Search Engine Optimization (SEO) attacks remain unexplored. In this paper, we present the first systematic study of SEO attacks targeting LLMSEs. Specifically, we examine ten representative LLMSE products (e.g., ChatGPT, Gemini) and construct SEO-Bench, a benchmark comprising 1,000 real-world black-hat SEO websites, to evaluate both open- and closed-source LLMSEs. Our measurements show that LLMSEs mitigate over 99.78% of traditional SEO attacks, with the phase of retrieval serving as the primary filter, intercepting the vast majority of malicious queries. We further propose and evaluate seven LLMSEO attack strategies, demonstrating that off-the-shelf LLMSEs are vulnerable to LLMSEO attacks, i.e., rewritten-query stuffing and segmented texts double the manipulation rate compared to the baseline. This work offers the first in-depth security analysis of the LLMSE ecosystem, providing practical insights for building more resilient AI-driven search systems. We have responsibly reported the identified issues to major vendors.

</details>

### 17. SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2602.12187) · 🌐 [Project](https://doi.org/10.1145/3770855.3818146)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`SAGE pipeline`、`structured document`、`retrieval realism`

👤 **作者**：Sunghwan Kim、Wooseok Jeong、Serin Kim、Sangam Lee、Dongha Lee

- 🎯 **研究动机**：现有 GEO 评测在预选候选文档上操作，抽象掉检索与重排且丢弃网页结构信息
- 🔬 **研究方法**：SAGEO Arena 在大规模含结构信息的网页语料上集成完整生成式搜索管线，支持检索、重排、生成各阶段的 SAGEO 分析
- 📌 **结论**：既有优化方法在真实条件下大多不实用且常在检索/重排阶段反降曝光；结构信息可缓解，有效 SAGEO 须按管线阶段定制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search-Augmented Generative Engines (SAGE) have emerged as a new paradigm for information access, bridging web-scale retrieval with generative capabilities to deliver synthesized answers. This shift has fundamentally reshaped how web content gains exposure online, giving rise to Search-Augmented Generative Engine Optimization (SAGEO), the practice of optimizing web documents to improve their visibility in AI-generated responses. Despite growing interest, no evaluation environment currently supports comprehensive investigation of SAGEO. Specifically, existing benchmarks lack end-to-end visibility evaluation of optimization strategies, operating on pre-determined candidate documents that abstract away retrieval and reranking preceding generation. Moreover, existing benchmarks discard structural information (e.g., schema markup) present in real web documents, overlooking the rich signals that search systems actively leverage in practice. Motivated by these gaps, we introduce SAGEO Arena, a realistic and reproducible environment for stage-level SAGEO analysis. Our objective is to jointly target search-oriented optimization (SEO) and generation-centric optimization (GEO). To achieve this, we integrate a full generative search pipeline over a large-scale corpus of web documents with rich structural information. Our findings reveal that existing approaches remain largely impractical under realistic conditions and often degrade performance in retrieval and reranking. We also find that structural information helps mitigate these limitations, and that effective SAGEO requires tailoring optimization to each pipeline stage. Overall, our benchmark paves the way for realistic SAGEO evaluation and optimization beyond simplified settings.

</details>

### 18. When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2609.02964)　📅 2026-09

**关键词**：`defense`、`GEO poisoning`、`shield reranking`、`source-use control`

👤 **作者**：Haozhang Li、Yangguang Shao、Xinjie Lin、Zhong Guan、Mi Zhou、Junzheng Shi

- 🎯 **研究动机**：恶意 GEO 改写与原文事实一致、又放大了高质量良性内容共有的特征，使事实核验与困惑度过滤双双失效
- 🔬 **研究方法**：提出免微调两阶段防御 GEO Defender：Shield Reranker 在冻结基线重排器上学习偏好防御残差以降权 GEO 文档，TFSG 把防御结果蒸馏为自然语言经验库在推理时引导 LLM 的信源使用
- 📌 **结论**：在五个 LLM、七种 GEO 攻击上平均 ASR 从 50.32% 降至 6.20%，保留 94.12% 良性证据使用并泛化到未见攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper focuses on defending generative search engines against malicious Generative Engine Optimization (GEO), which rewrites web documents to match engines' citation preferences and thereby manipulates generated answers. Recent GEO methods have advanced from hand-crafted rewriting to automated and agentic optimization, substantially increasing the visibility of target documents in generated answers. However, defending against such manipulation poses two major challenges: attack documents remain factually consistent with their originals, rendering fact verification and perplexity filtering ineffective, and the features they amplify equally characterize high-quality benign content. To address these limitations, we propose GEO Defender, a two-stage defense aligned with the attack chain that requires no fine-tuning of the target LLM. GEO Defender consists of Shield Reranker and Training-Free Shield Generation (TFSG). Specifically, Shield Reranker learns a preference-based defensive residual over a frozen base reranker, demoting GEO-rewritten documents while preserving relevance judgments, and TFSG distills defense outcomes into a natural-language experience library that guides the target LLM's source use at inference. Experiments on two state-of-the-art closed-source LLMs and three open-source LLMs across seven GEO attacks demonstrate that GEO Defender reduces the average attack success rate from 50.32% to 6.20%, retains 94.12% of benign-evidence use, preserves answer quality, and generalizes to unseen attacks from construction instances.

</details>

### 19. GEO-Flag: Detecting and Measuring GEO-Optimized Web Content

📄 [arXiv](https://arxiv.org/abs/2608.16824)　📅 2026-08

**关键词**：`detection`、`generative engine optimization`、`ranking manipulation`、`content integrity`

👤 **作者**：Junjie Chu、Ye Leng、Mingjie Li、Yun Shen、Xinyue Shen、Yang Zhang

- 🎯 **研究动机**：GEO 优化让弱信息或虚假信息显得被充分支持，生成式搜索合成直接答案进一步放大风险，系统检测方法缺失
- 🔬 **研究方法**：GEOFlagBench 含 3200 实例（400 查询、4 域、8 个 GEO 优化器家族）；Intervention-Paired Training 监督检测器对 GEO 干预与非 GEO AI 润色的响应；GEO 门控 agent 审计引用 URL
- 📌 **结论**：IPT 使 ModernBERT 的 F1 从 0.862 升至 0.944、最差组准确率 0.725 升至 0.883；1000 个真实查询的 10095 个页面中 GEO 比例 8.90%，2026 年修改页面达 16.36%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) modifies web content to increase its likelihood of being selected and cited by generative search engines. This can give strategically optimized pages visibility disproportionate to their authority or relevance and even make weak or false information appear well supported. Unlike conventional search, generative search synthesizes information into direct answers rather than presenting competing sources, which can further amplify these risks, as assessing source provenance and authority requires additional user interaction. Despite these concerns, systematic methods for detecting GEO-optimized webpages remain underexplored. We introduce \texttt{GEOFlagBench}, a benchmark of 3,200 web content instances spanning 400 queries, four domains, and eight GEO optimizer families, and use it to systematically evaluate existing GEO detection methods. Although the strongest baseline achieves an aggregate F1 of 0.880, method-level and authorship-conditioned evaluations reveal substantial weaknesses and potential reliance on authorship-related shortcuts. We therefore propose \emph{Intervention-Paired Training} (IPT), which supervises detector responses to GEO interventions and non-GEO AI polishing; on ModernBERT, IPT improves F1 from 0.862 to 0.944 and worst-group accuracy from 0.725 to 0.883. We develop a GEO-gated Agent system for auditing the Source Tier and verifiability of Citation URLs in detected GEO pages. Finally, we deploy the complete pipeline on released Google Search and Gemini-grounded retrieval results for 1,000 real-user queries. Across 10,095 available pages, we estimate an overall GEO prevalence of 8.90\%, reaching 16.36\% among pages modified in 2026. Our results establish a foundation for systematically detecting, auditing, and measuring GEO in real-world search ecosystems.

</details>

### 20. Assessing Attack Surfaces in Generative Search Engines through Publisher Attributes: A Case Study in Political Domains

📄 [arXiv](https://arxiv.org/abs/2608.15814)　📅 2026-08

**关键词**：`detection`、`generative engine optimization`、`ranking manipulation`、`content integrity`

👤 **作者**：Riku Mochizuki、Shusuke Komatsu、Souta Noguchi、Kazuto Ataka

- 🎯 **研究动机**：生成式搜索引擎的投毒攻击面——引用哪些出版者、个性化如何影响引用行为——未被研究
- 🔬 **研究方法**：提出 content-injection barrier 指标量化给定出版者权威度下注入内容的难度，并嵌入用户画像测个性化对引用的影响；美日政治域三大 GSE 实验
- 📌 **结论**：攻击面随 GSE 模型不同、由 web 搜索功能塑造；执政党比在野党攻击面更宽；用户画像影响甚微

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We characterize the attack surface of generative search engines (GSEs) against poisoning attacks in the political domain, from the perspectives of citation selection and personalization. GSEs integrate web search and answer generation with user preferences and backgrounds using large language models (LLMs). They play a crucial role in how users access information on the web. Because anyone can publish content on the web, GSEs are vulnerable to poisoning attacks that manipulate citations to undermine reliable information delivery. Existing studies on citation evaluation focus on how faithfully answers reflect cited content. However, they leave unexamined the two critical aspects to capture the attack surface of GSEs against poisoning attacks: which publishers GSEs prefer to cite, and how personalization affects citation behavior. To fill this gap, we introduce an evaluation framework that characterizes the attack surface of GSEs against poisoning attacks. Our contributions are twofold: (1) we propose a novel metric, \emph{content-injection barrier}, which quantifies the difficulty of injecting arbitrary content onto the web with a given level of publisher authority; and (2) we reveal how personalization affects citation behavior by embedding user profiles into GSEs. We conduct experiments on three major GSEs in the political domain of the United States and Japan. Our results show that (a) the attack surface differs across GSE models; (b) the web search functionality of GSEs shapes the attack surface; (c) ruling parties have a broader attack surface than opposition parties; and (d) user profiles have little influence on the attack surface.

</details>

### 21. SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders

📄 [arXiv](https://arxiv.org/abs/2607.21951)　📅 2026-07

**关键词**：`attack`、`Web-RAG`、`preference manipulation`、`recommendation corruption`

👤 **作者**：Evan Caville、Spencer Kayser、Siamak Layeghy、Billy Sung、Sara Dolnicar、Marius Portmann

- 🎯 **研究动机**：已有研究考察伪造产品与检索投毒，但同一检索页面被不同编辑后如何改变 LLM 最终排名缺乏受控比较
- 🔬 **研究方法**：提出 SIREN：把 PAIR 越狱循环适配为竞争排名操纵，用 23 类内容投毒技术迭代编辑已检索来源，RAG 回放平台固定来源与顺序以隔离内容效应
- 📌 **结论**：两个生产 Claude 模型上 124 个技术试验中 62 次达到 rank-1；新会话重放平均成功率 0.805，声明式排名断言与植入列表通常比指令式注入更有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpages, it acts as a recommender, and each retrieved page becomes a potential attack surface. Prior work has examined fabricated products, retrieval poisoning, and rank promotion. However, these studies do not compare how different edits to an already retrieved page change the model's final ranking while the surrounding source set remains unchanged. To address this gap, we propose SIREN, an automated attacker--judge method that adapts the PAIR jailbreaking loop to competitive rank manipulation, with the goal of moving a chosen entity to rank~1 in an LLM-generated recommendation. SIREN retrieves and captures webpages using Anthropic's web tools, then iteratively edits a retrieved source using an interpretable taxonomy of 23 content-poisoning techniques. The custom-RAG replay platform keeps the same sources in the same order, so changes in the model's ranking can be linked to changes in the supplied content rather than to differences in retrieval. Across two production Claude models, SIREN reaches rank~1 in 62 of 124 technique trials nested within eight query--model contexts. The payloads that reached rank~1 were then tested in fresh sessions, where they reproduced the result with a mean success rate of 0.805. Across the evaluated settings, declarative ranking claims and seeded lists were generally more effective than directive-form injections, although the strength of this difference depended on the target model. To the best of our knowledge, this is among the first controlled studies of competitive rank manipulation in production LLMs where the supplied source context is kept fixed.

</details>

### 22. One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders

📄 [arXiv](https://arxiv.org/abs/2606.13610) · 🌐 [Project](https://github.com/leoluolol/forge-benchmark)　📅 2026-06

**关键词**：`attack`、`product fabrication`、`GEO pollution`、`recommendation corruption`

👤 **作者**：Minghao Luo、Liang Chen

- 🎯 **研究动机**：搜索增强 LLM 日益介入日常消费推荐并检索 live 网页，GEO 运营者污染的内容可能使其沦为假产品的不知情推销者
- 🔬 **研究方法**：FORGE 在冻结的已检索网页集合中把真实产品局部改写为虚构产品，225 个真实产品 × 15 类 × 5 消费场景，12 个商用/开源 LLM 上测假产品被推荐率，并检验四种防御
- 📌 **结论**：单页污染即达最高 27% fooled rate，top-3 全替换升至 73.8%；模型对产品缺乏稳定先验时更脆弱；reasoning 不缓解反而编造虚假社会证明；怀疑提示同样加重脆弱性，共识过滤器误伤真品，可信度重排只清除约六分之一假货

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: LLM recommenders may consume web content that Generative Engine Optimization (GEO) operators have polluted to mislead them. We ask: to what extent do they become unwitting promoters of fake products? We introduce FORGE (Fake Online Recommendations in Generative Environments), which locally rewrites real products in a frozen set of retrieved web pages into fake ones and measures how often the LLM recommends the fake product, across 225 real products in 15 categories and 5 consumer scenarios. Across 12 commercial and open-weights LLMs, all models are vulnerable: a single polluted page yields fooled rates of up to 27%, while the full top-3 replacement raises this to 73.8%. Vulnerability varies across categories, increasing when models lack stable prior knowledge of the products. Reasoning does not mitigate this vulnerability; instead, it often generates spurious social proof to justify false recommendations. None of the four defenses is adequate: the skepticism prompt can exacerbate vulnerability much like reasoning, the two consensus filters risk suppressing legitimate products, and credibility re-ranking helps every model but removes only a sixth of the fakes. We release the FORGE benchmark and the evaluation code at https://github.com/leoluolol/forge-benchmark.

</details>

### 23. SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2605.21948)　📅 2026-05

**关键词**：`defense`、`semantic integrity`、`GEO manipulation`、`rank attack mitigation`

👤 **作者**：Xucheng Yu、Haibo Jin、Huimin Zeng、Haohan Wang

- 🎯 **研究动机**：LLM 排序系统易受 GEO 攻击（向产品描述注入语义信号抬升排名），而已有防御（PPL 过滤、内容分类器、改写）对语义操纵零召回
- 🔬 **研究方法**：三组件防御 SCI-Defense：Perplexity 检测 + Semantic Integrity Scoring（权威归因、叙事目的、比较声明、时序声明四维）+ Inter-Candidate Detection
- 📌 **结论**：600 条 Amazon 产品描述上 Precision=1.000、FPR=0，对 String/Reasoning/Review 攻击 Recall 分别为 1.000/0.952/0.830；MS MARCO 网页上 Review 攻击近零召回——通用网页缺乏产品描述式说服信号，防御呈现场景依赖；Specification Amplification 与 Use-Case Saturation 新攻击进一步暴露结构性盲点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based ranking systems are vulnerable to Generative Engine Optimization (GEO) attacks, where adversaries inject semantic signals into product descriptions to artificially boost rankings. We propose SCI-Defense, a three-component defense framework combining Perplexity detection (PPL), Semantic Integrity Scoring (SIS), and Inter-Candidate Detection (ICD). SIS evaluates four manipulation dimensions: Authority Attribution (AA), Narrative Purposiveness (NP), Comparative Claims (CA), and Temporal Claims (TC). Evaluated on 600 Amazon product descriptions across 6 categories, SCI-Defense achieves Precision=1.000 and FPR=0.000, with Recall of 1.000, 0.952, and 0.830 against String, Reasoning, and Review attacks respectively. On 600 MS MARCO web passages, String attacks are blocked with perfect recall while Review attacks yield near-zero recall, as web passages lack the persuasion-oriented signals that SIS targets in product descriptions. We demonstrate that existing defenses -- PPL-only filters, SafetyClf content classifiers, and paraphrasing -- achieve zero recall against semantic manipulation attacks. We further demonstrate new attacks such as Specification Amplification and Use-Case Saturation can expose semantic relevance manipulation as a structural defense blind spot that suggests directions for future research.

</details>

### 24. C-SEO Bench: Does Conversational SEO Work?

📄 [arXiv](https://arxiv.org/abs/2506.11097) · 🌐 [Project](https://github.com/parameterlab/c-seo-bench)　📅 2025-06　🏷 NeurIPS 2025

**关键词**：`benchmark`、`C-SEO`、`multi-actor adoption`、`visibility evaluation`

👤 **作者**：Haritz Puerto、Martin Gubri、Tommaso Green、Seong Joon Oh、Sangdoo Yun

- 🎯 **研究动机**：C-SEO 方法只在窄域、单行动者场景下测试，跨域有效性未知；现实中多方会竞争性采用同类技术，SEO 时代的动态会否重演缺乏评测
- 🔬 **研究方法**：首个跨任务、跨域、跨行动者数的 C-SEO 基准：问答与产品推荐两任务各三域，并形式化不同采用率下的评测协议
- 📌 **结论**：多数 C-SEO 方法基本无效甚至降低文档排名；传统 SEO（在 LLM context 中抬升来源排名）反而显著更有效；随采用者增多整体收益递减——问题呈拥挤、零和性质

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are transforming search engines into Conversational Search Engines (CSE). Consequently, Search Engine Optimization (SEO) is being shifted into Conversational Search Engine Optimization (C-SEO). We are beginning to see dedicated C-SEO methods for modifying web documents to increase their visibility in CSE responses. However, they are often tested only for a limited breadth of application domains; we do not know whether certain C-SEO methods would be effective for a broad range of domains. Moreover, existing evaluations consider only a single-actor scenario where only one web document adopts a C-SEO method; in reality, multiple players are likely to competitively adopt the cutting-edge C-SEO techniques, drawing an analogy from the dynamics we have seen in SEO. We present C-SEO Bench, the first benchmark designed to evaluate C-SEO methods across multiple tasks, domains, and number of actors. We consider two search tasks, question answering and product recommendation, with three domains each. We also formalize a new evaluation protocol with varying adoption rates among involved actors. Our experiments reveal that most current C-SEO methods are not only largely ineffective but also frequently have a negative impact on document ranking, which is opposite to what is expected. Instead, traditional SEO strategies, those aiming to improve the ranking of the source in the LLM context, are significantly more effective. We also observe that as we increase the number of C-SEO adopters, the overall gains decrease, depicting a congested and zero-sum nature of the problem. Our code and data are available at https://github.com/parameterlab/c-seo-bench and https://huggingface.co/datasets/parameterlab/c-seo-bench.

</details>

### 25. EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents

📄 [arXiv](https://arxiv.org/abs/2605.12887)　📅 2026-05

**关键词**：`attack`、`evidence ecosystem`、`trajectory-aware GEO`、`coordinated pages`

👤 **作者**：Hengwei Ye、Jiasheng Mao、Zhenhan Guan、Zheng Tian

- 🎯 **研究动机**：现有 GEO 只研究单网页，而 agentic web search 是多步过程（发查询、爬页、跟链接、改写搜索、跨步综合证据），影响力取决于页面如何组织、连接并沿浏览轨迹被遭遇
- 🔬 **研究方法**：把 GEO 形式化为环境级影响问题；TRACE 构建轨迹感知协同证据生态：agent 可见的导航入口页 + 异构支持页，用共享术语、内链与一致产品属性分阶段引入、验证、强化虚构目标产品；在 OPR-Bench 开放式产品推荐上评测
- 📌 **结论**：最终目标推荐率 consistently 超页面级 GEO 基线；轨迹级指标显示初始目标爬取、目标定向后续搜索与内链爬取均增加——收益来自塑造 agent 的证据获取过程而非单纯堆目标内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-enabled LLM agents are changing how online information influences search outcomes. Existing Generative Engine Optimization (GEO) studies mainly focus on individual webpages. However, agentic web search is not a single-document setting: an agent may issue queries, crawl pages, follow links, reformulate searches, and synthesize evidence across multiple browsing steps. Influence therefore depends not only on page content, but also on how pages are organized, connected, and encountered along the agent's browsing trajectory. We study this shift through Ecosystem Generative Engine Optimization (EcoGEO), which treats GEO as an environment-level influence problem for web-enabled LLM agents. To instantiate this perspective, we propose TRACE, a Trajectory-Aware Coordinated Evidence Ecosystem. Given a recommendation query and a fictional target product, our method builds a controlled evidence environment that coordinates an agent-facing navigation entry page with heterogeneous support pages. These pages use shared terminology, internal links, and consistent product attributes to introduce, verify, and reinforce the target product. We evaluate our method on OPR-Bench, a benchmark for open-ended product recommendation. Experiments show that it consistently outperforms page-level GEO baselines in final target recommendation. Trajectory-level metrics further show increased initial target-result crawls, target-specific follow-up searches, and internal-link crawls, suggesting that the gains come from shaping the agent's evidence-acquisition process rather than merely adding more target-related content. Overall, our findings support an ecosystem research paradigm for GEO, where web-enabled LLM agents are studied in relation to the broader evidence environments that guide search, browsing, and answer synthesis.

</details>

### 26. Manipulating Large Language Models to Increase Product Visibility

📄 [arXiv](https://arxiv.org/abs/2404.07981) · 🐙 [Code](https://github.com/aounon/llm-rank-optimizer.)　📅 2024-04

**关键词**：`attack`、`strategic text sequence`、`product visibility`、`LLM recommendation`

👤 **作者**：Aounon Kumar、Himabindu Lakkaraju

- 🎯 **研究动机**：LLM 搜索建议日益影响购买决策——厂商能否通过操纵产品页内容提升被推荐率
- 🔬 **研究方法**：在虚构咖啡机产品目录上给产品信息页添加精心构造的 strategic text sequence（STS），测其对两类目标产品（几乎不被推荐者与通常排第二者）成为 top 推荐的影响
- 📌 **结论**：STS 显著提升两类产品成为 LLM top 推荐的概率——LLM 生成式搜索操纵的开山实证，后续 GEO 与产品可见性攻击线皆溯源于此

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly being integrated into search engines to provide natural language responses tailored to user queries. Customers and end-users are also becoming more dependent on these models for quick and easy purchase decisions. In this work, we investigate whether recommendations from LLMs can be manipulated to enhance a product's visibility. We demonstrate that adding a strategic text sequence (STS) -- a carefully crafted message -- to a product's information page can significantly increase its likelihood of being listed as the LLM's top recommendation. To understand the impact of STS, we use a catalog of fictitious coffee machines and analyze its effect on two target products: one that seldom appears in the LLM's recommendations and another that usually ranks second. We observe that the strategic text sequence significantly enhances the visibility of both products by increasing their chances of appearing as the top recommendation. This ability to manipulate LLM-generated search responses provides vendors with a considerable competitive advantage and has the potential to disrupt fair market competition. Just as search engine optimization (SEO) revolutionized how webpages are customized to rank higher in search engine results, influencing LLM recommendations could profoundly impact content optimization for AI-driven search services. Code for our experiments is available at https://github.com/aounon/llm-rank-optimizer.

</details>

### 27. Ranking Manipulation for Conversational Search Engines

📄 [arXiv](https://arxiv.org/abs/2406.03589)　📅 2024-06　🏷 EMNLP 2024

**关键词**：`attack`、`prompt injection`、`source ranking`、`tree-of-attacks`、`transferability`

👤 **作者**：Samuel Pfrommer、Yatong Bai、Tanmay Gautam、Somayeh Sojoudi

- 🎯 **研究动机**：会话式搜索引擎把检索网页文本装入 LLM 上下文做摘要——prompt 注入能否操纵其引用源的排序
- 🔬 **研究方法**：构建真实消费产品网站数据集并把会话式搜索排序形式化为对抗问题；先用无攻击基线刻画各 LLM 对产品名/文档内容/上下文位置的优先级差异，再用 tree-of-attacks 式越狱提升低排名产品
- 📌 **结论**：注入攻击可靠提升低排名产品且可跨模型迁移——首次把引用排序确立为注入攻击目标。EMNLP 2024 main

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Major search engine providers are rapidly incorporating Large Language Model (LLM)-generated content in response to user queries. These conversational search engines operate by loading retrieved website text into the LLM context for summarization and interpretation. Recent research demonstrates that LLMs are highly vulnerable to jailbreaking and prompt injection attacks, which disrupt the safety and quality goals of LLMs using adversarial strings. This work investigates the impact of prompt injections on the ranking order of sources referenced by conversational search engines. To this end, we introduce a focused dataset of real-world consumer product websites and formalize conversational search ranking as an adversarial problem. Experimentally, we analyze conversational search rankings in the absence of adversarial injections and show that different LLMs vary significantly in prioritizing product name, document content, and context position. We then present a tree-of-attacks-based jailbreaking technique which reliably promotes low-ranked products. Importantly, these attacks transfer effectively to state-of-the-art conversational search engines such as perplexity$.$ai. Given the strong financial incentive for website owners to boost their search ranking, we argue that our problem formulation is of critical importance for future robustness work.

</details>

### 28. Illusions of Relevance: Arbitrary Content Injection Attacks Deceive Retrievers, Rerankers, and LLM Judges

📄 [arXiv](https://arxiv.org/abs/2501.18536)　📅 2025-01　🏷 AACL 2025 Findings

**关键词**：`attack`、`content injection`、`retriever`、`reranker`、`LLM judge`

👤 **作者**：Manveer Singh Tamber、Jimmy Lin

- 🎯 **研究动机**：黑盒威胁模型下，攻击者能否把任意不相关内容推进搜索结果顶部并获得满分相关性
- 🔬 **研究方法**：内容注入两种形态：向相关段落注入任意句子、向任意段落注入查询词；系统分析模型类别/规模、相关-非相关内容配比、注入位置、毒性与严重度对攻击成功率的影响
- 📌 **结论**：retriever、reranker 与 LLM 相关性 judge 全部可被欺骗至给任意内容满分相关性——检索管线的通用注入脆弱性，且 LLM 生成内容更易被利用。AACL 2025 Findings

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work considers a black-box threat model in which adversaries attempt to propagate arbitrary non-relevant content in search. We show that retrievers, rerankers, and LLM relevance judges are all highly vulnerable to attacks that enable arbitrary content to be promoted to the top of search results and to be assigned perfect relevance scores. We investigate how attackers may achieve this via content injection, injecting arbitrary sentences into relevant passages or query terms into arbitrary passages. Our study analyzes how factors such as model class and size, the balance between relevant and non-relevant content, injection location, toxicity and severity of injected content, and the role of LLM-generated content influence attack success, yielding novel, concerning, and often counterintuitive results. Our results reveal a weakness in embedding models, LLM-based scoring models, and generative LLMs, raising concerns about the general robustness, safety, and trustworthiness of language models regardless of the type of model or the role in which they are employed. We also emphasize the challenges of robust defenses against these attacks. Classifiers and more carefully prompted LLM judges often fail to recognize passages with content injection, especially when considering diverse text topics and styles. Our findings highlight the need for further research into arbitrary content injection attacks. We release our code for further study.

</details>

### 29. Generative Engine Optimization: How to Dominate AI Search

📄 [arXiv](https://arxiv.org/abs/2509.08919)　📅 2025-09

**关键词**：`analysis`、`AI search bias`、`earned media`、`source mix`、`measurement`

👤 **作者**：Mahe Chen、Xiaoxuan Wang、Kaiwen Chen、Nick Koudas

- 🎯 **研究动机**：AI 搜索（ChatGPT/Perplexity/Gemini）与传统 Google 的信源选择差异缺乏受控大尺度对比——GEO 策略的地基
- 🔬 **研究方法**：多垂直域、多语言、多查询改写的大规模受控实验，量化两类系统在信源构成上的系统性差异
- 📌 **结论**：AI 搜索对 earned media（第三方权威源）呈系统性压倒性偏好，与 Google 更均衡的混合形成反差；各 AI 搜索在域多样性、新鲜度、跨语言稳定性与措辞敏感性上差异显著——GEO 测量的实证基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid adoption of generative AI-powered search engines like ChatGPT, Perplexity, and Gemini is fundamentally reshaping information retrieval, moving from traditional ranked lists to synthesized, citation-backed answers. This shift challenges established Search Engine Optimization (SEO) practices and necessitates a new paradigm, which we term Generative Engine Optimization (GEO). This paper presents a comprehensive comparative analysis of AI Search and traditional web search (Google). Through a series of large-scale, controlled experiments across multiple verticals, languages, and query paraphrases, we quantify critical differences in how these systems source information. Our key findings reveal that AI Search exhibit a systematic and overwhelming bias towards Earned media (third-party, authoritative sources) over Brand-owned and Social content, a stark contrast to Google's more balanced mix. We further demonstrate that AI Search services differ significantly from each other in their domain diversity, freshness, cross-language stability, and sensitivity to phrasing. Based on these empirical results, we formulate a strategic GEO agenda. We provide actionable guidance for practitioners, emphasizing the critical need to: (1) engineer content for machine scannability and justification, (2) dominate earned media to build AI-perceived authority, (3) adopt engine-specific and language-aware strategies, and (4) overcome the inherent "big brand bias" for niche players. Our work provides the foundational empirical analysis and a strategic framework for achieving visibility in the new generative search landscape.

</details>

### 30. E-GEO: A Testbed for Generative Engine Optimization in E-Commerce

📄 [arXiv](https://arxiv.org/abs/2511.20867)　📅 2025-11

**关键词**：`benchmark`、`e-commerce GEO`、`rewriting`、`testbed`、`shopping agent`

👤 **作者**：Puneet S. Bagga、Vivek F. Farias、Tamar Korkotashvili、Tianyi Peng、Yuhang Wu

- 🎯 **研究动机**：会话式购物 agent 兴起重塑电商检索，而 GEO 实践 ad hoc、影响不明——电商设定缺乏专门数据集
- 🔬 **研究方法**：E-GEO 首个电商 GEO 数据集：13,747 条真实多句消费查询、每条配 10 个检索到的 Amazon listing（含意图/约束/偏好/购物上下文）；在 5 个生成引擎 × 7 个 LLM rewriter × 15 个手工启发式上做大规模实证并将优化形式化
- 📌 **结论**：电商渠道 GEO 的系统测试床——该论文与 One Polluted Page/EcoGEO 共同构成推荐 agent 操纵的电商线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rise of large language models (LLMs), generative engines have become powerful alternatives to traditional search, reshaping retrieval tasks. In e-commerce, for instance, conversational shopping agents now guide consumers to relevant products. This shift has created the need for generative engine optimization (GEO) -- improving content visibility and relevance for generative engines. Despite its growing importance, current GEO practices are largely ad hoc, and their impacts remain poorly understood, especially in the e-commerce setting. We address this gap by introducing E-GEO, the first dataset built specifically for e-commerce GEO. E-GEO contains 13,747 realistic, multi-sentence consumer product queries, each paired with 10 retrieved Amazon listings, capturing rich intent, constraints, preferences, and shopping contexts that existing datasets miss. Using this dataset, we conduct the first large-scale empirical study of e-commerce GEO across five representative generative engines, seven popular LLM rewriters, and fifteen hand-crafted rewriting heuristics. We further formulate GEO as an optimization problem and develop a lightweight prompt meta-optimization algorithm that significantly improves over heuristic baselines. Notably, the optimized prompts reveal a stable, domain-agnostic pattern, suggesting the existence of a "universally effective" GEO strategy. Finally, we red-team the GEO system through both heuristic and optimization-based attacks and show that, under a simple in-prompt defense, gains from GEO reflect genuine content improvement rather than manipulation, anchoring GEO as a substantive and well-defined optimization problem.

</details>

### 31. Source Coverage and Citation Bias in LLM-based vs. Traditional Search Engines

📄 [arXiv](https://arxiv.org/abs/2512.09483)　📅 2025-12

**关键词**：`analysis`、`citation bias`、`LLM search engine`、`credibility`、`source diversity`

👤 **作者**：Peixian Zhang、Qiming Ye、Zifan Peng、Kiran Garimella、Gareth Tyson

- 🎯 **研究动机**：LLM 搜索引擎以摘要+有限引用回应查询，其信源覆盖与引用偏差相对传统引擎的净变化未测
- 🔬 **研究方法**：大规模实证：55,936 条查询 × 6 个 LLM-SE × 2 个传统引擎，比较域多样性、可信度、政治中性与安全性，并以特征归因分析选源标准
- 📌 **结论**：LLM-SE 引用域更多样（37% 域为其独有）但在可信度、政治中性与安全指标上并未超过传统引擎——引用透明与信任的落差实测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based Search Engines (LLM-SEs) introduces a new paradigm for information seeking. Unlike Traditional Search Engines (TSEs) (e.g., Google), these systems summarize results, often providing limited citation transparency. The implications of this shift remain largely unexplored, yet raises key questions regarding trust and transparency. In this paper, we present a large-scale empirical study of LLM-SEs, analyzing 55,936 queries and the corresponding search results across six LLM-SEs and two TSEs. We confirm that LLM-SEs cites domain resources with greater diversity than TSEs. Indeed, 37% of domains are unique to LLM-SEs. However, certain risks still persist: LLM-SEs do not outperform TSEs in credibility, political neutrality and safety metrics. Finally, to understand the selection criteria of LLM-SEs, we perform a feature-based analysis to identify key factors influencing source choice. Our findings provide actionable insights for end users, website owners, and developers.

</details>

### 32. Controlling Output Rankings in Generative Engines for LLM-based Search

📄 [arXiv](https://arxiv.org/abs/2602.03608)　📅 2026-02

**关键词**：`attack`、`output ranking control`、`black-box optimization`、`small business visibility`

👤 **作者**：Haibo Jin、…、Haohan Wang

- 🎯 **研究动机**：LLM 推荐强依赖初始检索序，小商家与独立创作者可见性被系统性压缩——能否黑盒操纵输出排序
- 🔬 **研究方法**：CORE 以搜索引擎返回内容为作用面（LLM 交互黑盒）：向被检索内容追加三类策略性优化文本——字符串型、推理型、评论型——引导生成引擎的输出排序
- 📌 **结论**：三类优化内容均有效塑造输出排序——把排名操纵从搜索引擎时代平移到生成式引擎的系统性方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The way customers search for and choose products is changing with the rise of large language models (LLMs). LLM-based search, or generative engines, provides direct product recommendations to users, rather than traditional online search results that require users to explore options themselves. However, these recommendations are strongly influenced by the initial retrieval order of LLMs, which disadvantages small businesses and independent creators by limiting their visibility. In this work, we propose CORE, an optimization method that \textbf{C}ontrols \textbf{O}utput \textbf{R}ankings in g\textbf{E}nerative Engines for LLM-based search. Since the LLM's interactions with the search engine are black-box, CORE targets the content returned by search engines as the primary means of influencing output rankings. Specifically, CORE optimizes retrieved content by appending strategically designed optimization content to steer the ranking of outputs. We introduce three types of optimization content: string-based, reasoning-based, and review-based, demonstrating their effectiveness in shaping output rankings. To evaluate CORE in realistic settings, we introduce ProductBench, a large-scale benchmark with 15 product categories and 200 products per category, where each product is associated with its top-10 recommendations collected from Amazon's search interface. Extensive experiments on four LLMs with search capabilities (GPT-4o, Gemini-2.5, Claude-4, and Grok-3) demonstrate that CORE achieves an average Promotion Success Rate of \textbf{91.4\% @Top-5}, \textbf{86.6\% @Top-3}, and \textbf{80.3\% @Top-1}, across 15 product categories, outperforming existing ranking manipulation methods while preserving the fluency of optimized content.

</details>

### 33. Don't Measure Once: Measuring Visibility in AI Search (GEO)

📄 [arXiv](https://arxiv.org/abs/2604.07585)　📅 2026-04

**关键词**：`analysis`、`GEO measurement`、`visibility distribution`、`repeated measurement`

👤 **作者**：Julius Schulte、Malte Bleeker、Philipp Kaufmann

- 🎯 **研究动机**：AI 搜索本质概率性——答案随运行、提示与时间变化，单次可见性观测不可靠
- 🔬 **研究方法**：基于实证研究刻画 GEO 可见性测量的方差结构，论证重复测量的必要性
- 📌 **结论**：品牌 GEO 表现必须以分布而非单点刻画、必须重复测量——GEO 测量方法论的正确起点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language model-based chat systems become increasingly widely used, generative engine optimization (GEO) has emerged as an important problem for information access and retrieval. In classical search engines, results are comparatively transparent and stable: a single query often provides a representative snapshot of where a page or brand appears relative to competitors. The inherent probabilistic nature of AI search changes this paradigm. Answers can vary across runs, prompts, and time, making one-off observations unreliable. Drawing on empirical studies, our findings underscore the need for repeated measurements to assess a brand's GEO performance and to characterize visibility as a distribution rather than a single-point outcome.

</details>

### 34. From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning

📄 [arXiv](https://arxiv.org/abs/2604.19516) · 🐙 [Code](https://github.com/Wu-beining/MAGEO)　📅 2026-04　🏷 ACL 2026 Findings

**关键词**：`tool`、`strategy learning`、`multi-agent GEO`、`reusable skill`、`causal attribution`

👤 **作者**：Beining Wu、…、Fu Li

- 🎯 **研究动机**：既有 GEO 方法逐实例孤立优化，无法跨任务与引擎积累可迁移的优化策略
- 🔬 **研究方法**：MAGEO 把 GEO 重构为策略学习：规划-编辑-保真评估多 agent 执行层 + 把验证过的编辑模式蒸馏为引擎专属可复用技能；Twin Branch 评估协议对内容编辑做因果归因；DSV-CF 双轴指标统一语义可见性与归因准确率；发布 MSME-GEO-Bench
- 📌 **结论**：三个主流引擎上可见性与引用保真同时大幅超越启发式基线，消融确认引擎专属技能的贡献——GEO 的自演化能力化。ACL 2026 Findings

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative engines (GEs) are reshaping information access by replacing ranked links with citation-grounded answers, yet current Generative Engine Optimization (GEO) methods optimize each instance in isolation, unable to accumulate or transfer effective strategies across tasks and engines. We reframe GEO as a strategy learning problem and propose MAGEO, a multi-agent framework in which coordinated planning, editing, and fidelity-aware evaluation serve as the execution layer, while validated editing patterns are progressively distilled into reusable, engine-specific optimization skills. To enable controlled assessment, we introduce a Twin Branch Evaluation Protocol for causal attribution of content edits and DSV-CF, a dual-axis metric that unifies semantic visibility with attribution accuracy. We further release MSME-GEO-Bench, a multi-scenario, multi-engine benchmark grounded in real-world queries. Experiments on three mainstream engines show that MAGEO substantially outperforms heuristic baselines in both visibility and citation fidelity, with ablations confirming that engine-specific preference modeling and strategy reuse are central to these gains, suggesting a scalable learning-driven paradigm for trustworthy GEO. Code is available at https://github.com/Wu-beining/MAGEO

</details>

### 35. From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms

📄 [arXiv](https://arxiv.org/abs/2604.25707)　📅 2026-04

**关键词**：`analysis`、`citation influence`、`measurement framework`、`platform comparison`

👤 **作者**：Zhang Kai、He Xinyue、Yao Jingang

- 🎯 **研究动机**：生成引擎决定信息是被发现、被引用还是被实际吸收进答案——被引用≠有影响，两阶段测量缺框架
- 🔬 **研究方法**：两阶段测量框架：引用选择（平台触发搜索并选源）与引用吸收（被引页贡献语言/证据/结构/事实支持）；基于 geo-citation-lab 数据（602 受控 prompt × ChatGPT/AI Overview/Perplexity、21,143 条有效搜索层引用、18,151 个抓取页、72 个特征）
- 📌 **结论**：引用广度与深度背离——Perplexity 与 Google 平均引用更多源，ChatGPT 引用更少但被引页平均影响显著更高；高影响页更长、更结构化、语义更对齐、可提取证据更丰富

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative search engines increasingly determine whether online information is merely discoverable, cited as a source, or actually absorbed into generated answers. This paper proposes a two-stage measurement framework for Generative Engine Optimization (GEO): citation selection, where a platform triggers search and chooses sources, and citation absorption, where a cited page contributes language, evidence, structure, or factual support to the final answer. We analyze the public geo-citation-lab dataset covering 602 controlled prompts across ChatGPT, Google AI Overview/Gemini, and Perplexity; 21,143 valid search-layer citations; 23,745 citation-level feature records; 18,151 successfully fetched pages; and 72 extracted features. The central descriptive finding is that citation breadth and citation depth diverge. Perplexity and Google cite more sources on average, while ChatGPT cites fewer sources but shows substantially higher average citation influence among fetched pages. High-influence pages tend to be longer, more structured, semantically aligned, and richer in extractable evidence such as definitions, numerical facts, comparisons, and procedural steps. The results suggest that GEO should be measured beyond citation counts, with answer-level absorption treated as a separate outcome.

</details>

### 36. What Gets Cited: Competitive GEO in AI Answer Engines

📄 [arXiv](https://arxiv.org/abs/2605.25517)　📅 2026-05

**关键词**：`analysis`、`competitive GEO`、`citation factor`、`factorial design`、`position bias`

👤 **作者**：Rahul Vishwakarma、Shushant Kumar、Ratnesh Jamidar

- 🎯 **研究动机**：答案引擎只引用少数来源——可见性取决于被引用；两个被检索候选竞争时什么决定谁被首引
- 🔬 **研究方法**：受控双文档 RAG 测试床：恰注入两个候选源并测首引用标记指向；6 个 LLM × 252,000 次配对试验 × 18 个内容因子的单因子设计，品牌匿名与顺序对消分离内容效应与位置偏置
- 📌 **结论**：主题相关性与列表位置是首引最大驱动；显式价格信息与新鲜时间戳稳定加分；完整性与信任线索增益较小、纯格式编辑几乎无效——竞争 GEO 的因子效应谱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI answer engines generate answers from retrieved pages but cite only a few sources. This makes visibility depend not just on ranking, but on being cited. We study competitive Generative Engine Optimization (GEO): when two retrieved candidates compete, what makes one more likely to be cited first? We build a controlled two-document retrieval-augmented generation (RAG) testbed that injects exactly two candidate sources into the model context and measures which source is referenced by the first citation marker in the output. Across six LLMs we execute 252,000 trials, repeated paired comparisons under one factorial program over 18 content factors. In each trial the two sources differ in exactly one factor; we use brand anonymization and counterbalanced source order to separate content effects from position bias. Mixed-effects models show that topical relevance and list position are the biggest drivers of being cited first. Including explicit price information and a recent timestamp also helps consistently. Completeness and trust cues add smaller gains, while formatting-only edits have little impact. We release a reproducible evaluation protocol and a prioritized GEO checklist for practitioners, and we exercised it in an early internal pilot at Sprinklr, where teams reported positive qualitative feedback on workflow usability.

</details>

### 37. Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots

📄 [arXiv](https://arxiv.org/abs/2606.12439)　📅 2026-06　🏷 ICML 2026 Position Track

**关键词**：`survey`、`GEO governance`、`concentrated influence`、`disclosure`、`auditing`

👤 **作者**：Yizhu Wen、Nan Zhang、Haohan Yuan、Xun Chen、Haopeng Zhang、Hanqing Guo

- 🎯 **研究动机**：搜索从 SEO 到 GEO 的转型产生未被检视的系统性风险，治理缺位
- 🔬 **研究方法**：形式化通用 GEO 流水线定位优化作用点，系统对比学术界与工业界实践差异
- 📌 **结论**：识别三重风险——低可竞争性与系统敏感性导致的集中影响、证据与推理链中的未披露商业影响、离线评测与部署系统间的学界-工业盲点；主张答案级治理：可竞争性、高精度披露、实质影响的黑盒审计与部署对齐指标。ICML 2026 Position Track

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) answer engines are increasingly used for information seeking, shifting visibility from ranked lists to synthesized answers. This enables Generative Engine Optimization (GEO), which targets LLM answer engines' evidence pool and generation. We analyze the search engine optimization (SEO) to GEO transition to identify two risks: (i) concentrated influence from low contestability and system sensitivity, and (ii) undisclosed commercial influence embedded in evidence and reasoning. We then formalize a general GEO pipeline to locate where optimization acts and compare academic and industry practices, revealing a third risk: (iii) academic-industry blind spots driven by visibility and evaluation asymmetries between offline setups and deployed systems. This position argues the need for answer-level governance and measurement: stronger contestability, high-precision disclosure, black-box auditing of material influence, and deployment-aligned metrics for exposure persistence.

</details>

### 38. Whose hotel does the AI recommend? An algorithm audit of reputation signals in LLM-assisted hotel selection

📄 [arXiv](https://arxiv.org/abs/2606.16344)　📅 2026-06

**关键词**：`analysis`、`algorithm audit`、`reputation signal`、`conjoint`、`LLM recommendation`

👤 **作者**：Mirza Samad Ahmed Baig、Syeda Anshrah Gillani、Asher Ali

- 🎯 **研究动机**：旅行者日益问 LLM 助手订哪家酒店——它们成为物业可见性的守门人，但什么在驱动其推荐从未被记录
- 🔬 **研究方法**：预注册算法审计：随机化选择联合设计，跨 persona、prompt 模板与 12 个开源/专有模型，在五个酒店间选择，七种信号（评分、评论量与新鲜度、商家回复、连锁、价格、环保认证、列表位置）独立随机化，估计各信号对推荐概率的平均边际成分效应
- 📌 **结论**：评分与价格主导（top 评分 +31.6pp、高价 −30.0pp）；无内容因素的列表位置因果移动推荐（价值约 $12/晚）；模型高估环保认证、完全忽略商家回复；陈述理由与实际权重不一致——GEO 操纵面的审计级画像

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Travelers increasingly ask large language model (LLM) assistants which hotel to book, making these systems gatekeepers of property visibility -- yet what moves their recommendations is undocumented. We conduct a pre-specified algorithm audit using a randomized choice-based conjoint: across personas, prompt templates, and twelve open-weight and proprietary models, assistants choose among five hotels whose guest rating, review volume and recency, management response, chain affiliation, price, eco-certification, and list position are independently randomized. We estimate the average marginal component effect of each signal on the probability of recommendation. Guest rating and price dominate (a top rating raises selection by 31.6 percentage points; a high price lowers it by 30.0), reproducing human valence-and-price primacy but over-weighting eco-certification and ignoring management response. List position -- a content-free artifact -- shifts recommendations causally, worth about \$12 per night. Stated reasons track revealed weights imperfectly. The findings ground generative engine optimization and the accountability of AI infomediaries in causal evidence.

</details>

### 39. Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems

📄 [arXiv](https://arxiv.org/abs/2606.17443)　📅 2026-06

**关键词**：`analysis`、`brand bias`、`monopoly dynamics`、`GEO competition`、`manipulation`

👤 **作者**：Xi Chu、Yupeng Hou

- 🎯 **研究动机**：LLM 成为消费者找产品的主渠道，品牌在这个新渠道如何竞争、垄断与被操纵未知
- 🔬 **研究方法**：护肤品类（体验品）× 三个商用 LLM 三组实验：同规格下知名品牌的垄断程度；权威式营销语言（含伪造临床证据宣称）的破垄断效应；多品牌同时采用 GEO 策略的竞争后果
- 📌 **结论**：知名品牌在同规格下 100% 被推荐（IAI=10.0），但竞争者 <0.1 星的评分优势即打破垄断；权威营销语言在 +0.17 星等值处破垄断且模型间响应迥异；全员采用同一优化策略时个体收益从 +0.802 崩至 0.007——GEO 竞争的社会困境

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are becoming a major way for consumers to find products, but we do not yet understand how brands compete in this new channel. We study brand dynamics in LLM recommendations using skincare products -- a category where consumers cannot easily judge quality before buying and must rely on brand reputation -- across three commercial LLMs (GPT-4o-mini, Claude Sonnet, Gemini 3 Flash), with a robustness check on search goods. In three experiments, we find: (1) a Conditional Monopoly where well-known brands get recommended 100% of the time (IAI = 10.0) when all products have the same specifications, but this dominance disappears with less than a +0.1-star rating advantage for a competitor; (2) authority-style marketing language, including fabricated clinical-evidence claims, breaks this monopoly at a Bias Surplus Value equal to +0.17 rating points, with each model responding differently; and (3) a social dilemma in multi-brand GEO competition: when all brands adopt the same optimization strategy, individual payoff falls from +0.802 to +0.007 in our payoff proxy, and non-participating brands receive zero recommendations in our tests. Our results suggest that generative engine optimization (GEO) should be studied not only as a security risk, but also as an emerging marketing practice that shapes market competition.

</details>

### 40. Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines

📄 [arXiv](https://arxiv.org/abs/2606.20065)　📅 2026-06

**关键词**：`analysis`、`brand visibility`、`tier ladder`、`AI search measurement`

👤 **作者**：Pratyush Kumar

- 🎯 **研究动机**：非头部品牌（SME/D2C/创作者/初创）在 AI 搜索中的可见性缺乏大规模测量——而它们恰是最依赖该渠道的
- 🔬 **研究方法**：分析 Ranqo 平台 2026 年 3–5 月间 100+ 品牌、100K+ prompt 响应的首轮可见性分布与信源依赖
- 📌 **结论**：清晰的三层品牌阶梯：全球名牌（Stripe/Nike 类）在 73% 的相关 AI 回答中首轮出现，成熟中腰部与区域性品牌骤降至个位数百分比——头部锁定效应的大规模实证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

People increasingly get answers straight from AI search engines like ChatGPT, Claude, Perplexity, and Gemini rather than scrolling search results. Brands that once focused on search engine optimization (SEO) must now optimize for how these engines represent, cite, and recommend them -- a shift variously called Generative Engine Optimization (GEO), Answer Engine Optimization (AEO), and AI Search Visibility. We treat AEO and AI Visibility as part of GEO, and study how to measure brand visibility across AI engines: what they value when they cite a brand, which sources they rely on, and what content large language models surface. The hard case is everyone outside the already-authoritative top brands -- SMEs, D2C brands, creators, and early-stage startups. We analyze 100K+ prompt responses across 100+ brands tracked on Ranqo between March and May 2026. First visibility runs form a clear three-tier brand-stature ladder: global household names (e.g., Stripe, Nike) appear in 73% of relevant AI answers on their first run; established mid-market and regional brands (e.g., Olipop, Klaviyo) in 44%; niche and small brands in just 11% -- about 30 percentage points per step. When engines cite sources, about 78% go to corporate websites; among non-corporate sources YouTube leads, ahead of Reddit, editorial media, and Wikipedia. The highest-leverage page is the ranked "best-of" listicle, the most-cited content format at about 21% of all citations. Sentiment is the unstable signal: whether a brand is framed positively or negatively flips about 6.7 times more often than whether it is mentioned at all. These findings provide a first large-scale baseline for measuring GEO: AI brand visibility can be measured, differs by platform, and varies strongly by brand maturity. We close by proposing seven v1.1 protocols to test whether specific recommendations can causally improve AI visibility.

</details>

### 41. Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)

📄 [arXiv](https://arxiv.org/abs/2607.14035)　📅 2026-07

**关键词**：`survey`、`GEO pipeline`、`evidence standards`、`reproducibility`、`critique`

👤 **作者**：Olivier Martinez

- 🎯 **研究动机**：GEO 领域术语、指标与证据标准高度异质，结论难以横向比较
- 🔬 **研究方法**：批判性综述 45 篇研究（2023.11–2026.07），统一审视其指标与实验设定
- 📌 **结论**：GEO 非单一排序任务而是随机、部分可观测的流水线（搜索激活→爬取索引→检索→重排→上下文分配→引用→凸显→事实吸收→用户行为）；奠基论文的增益条件于源已在固定上下文中，既不建立可发现性也不证明持久流量；主题相关性与上下文位置是最可复现的杠杆——GEO 证据地图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) seeks to increase content's presence, likelihood of citation, or influence in answers produced by generative engines. Since the foundational GEO paper, the field has expanded rapidly, but terminology, metrics, and evidence standards remain heterogeneous. This critical survey reviews 45 studies selected under a November 2023-July 2026 publication window, including one earlier preprint published at EMNLP after the window opened, plus relevant RAG and evaluation work. We argue that GEO is not a single ranking task but a stochastic, partially observable pipeline spanning search activation, crawling and indexing, retrieval, reranking and context allocation, citation, prominence, factual absorption, fidelity, and user behavior. The foundational paper's widely cited gains are valid within its experimental setting but conditional on a source already being present in a fixed context; they establish neither organic discoverability nor durable traffic effects. Reviewed work indicates that topical relevance and context position are the most reproducible levers, generic heuristics transfer poorly, competition can erode individual gains, and citation-oriented rewrites can impair retrieval. Commercial audits further reveal low source overlap, substantial run-to-run variability, and persistent fidelity gaps. We contribute a multistage formal model, a visibility vector separating discoverability, citation, absorption, and economic outcomes, an evidence hierarchy, and a reproducible protocol based on repeated measurements, paraphrases, controls, human validation, and multi-actor interference. Within this corpus, the evidence is narrow: already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior.

</details>

### 42. How Artificial Intelligence LLM Engines Shape the Global Conflict Information Environment

📄 [arXiv](https://arxiv.org/abs/2607.14197)　📅 2026-07

**关键词**：`analysis`、`misinformation`、`GEO weaponization`、`thin record`、`conflict`

👤 **作者**：Jason Miklian

- 🎯 **研究动机**：AI 引擎承接越来越多关于冲突的问题——其错误是否有结构模式、对全球冲突信息环境意味着什么
- 🔬 **研究方法**：28 场冲突 × 5 个头部引擎共 5,460 条回答对照文献证据评分；并分析引擎取用冲突事实的 1,048 个网站
- 📌 **结论**：可检索记录越薄，引擎越多发明、误归因与误计数；薄记录恰是最易被 GEO 扭曲的——构成结构性误/虚假信息暴露；GEO 源优化已在冲突信息环境发生——地缘误信息与 GEO 的交汇

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Artificial Intelligence (AI) answer engines now field a growing share of the questions that analysts, scholars, and the public ask about issues of peace and conflict. Large Language Models (LLMs) are known to hallucinate under certain conditions, but do these errors have discernible patterns when they are asked about conflicts, and if so what can that teach us about the changing global conflict information environment? To answer, we first asked a battery of questions about 28 conflicts to five leading answer engines and scored their 5,460 answers against documented evidence. We found that the thinner the retrievable record around a given conflict, the more the engines invent, misattribute, and miscount. Thin records don't just encourage hallucination, but create structural exposure to mis- and disinformation, because they are the easiest records to warp through Generative Engine Optimization (GEO) to bias engine responses. Through an analysis of 1,048 websites that the AI LLMs pulled conflict facts from, we found that GEO source optimization is already happening, and while state-partisan digital capture remains incipient it is rapidly growing. We explain what these findings mean for scholarship with the rise of GEO information warfare, and for policy argue for a return to the deep local monitoring and translation-based research that AI tools cannot replicate, closing with a discussion of future research opportunities and challenges in this fast-moving space.

</details>

### 43. Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes

📄 [arXiv](https://arxiv.org/abs/2608.11390)　📅 2026-08

**关键词**：`defense`、`mechanism design`、`Stackelberg game`、`citation war`、`verifiable-content reward`

👤 **作者**：Chen Xu、Zitian Guo、Chenyan Xiong

- 🎯 **研究动机**：生成引擎把引用变成注意力、归因与价值分配机制——内容方为被引而优化 vs 平台保答案质量的张力会升级为引用战
- 🔬 **研究方法**：把供应方-平台交互形式化为部分监督的重复 Stackelberg 博弈；局部最优响应分析识别引用竞争趋于惰性平稳态的条件；提出 VCR 平台-创作者机制：不只惩罚可疑改写，还对浮现可验证事实性内容的改写给奖励
- 📌 **结论**：SOTA GEO 攻击能适应常规防御（生成降质、无支持主张的引文导向改写）；VCR 使创作者激励与内容真实性对齐、避免引用战——平台侧治理的机制设计路线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative engines are reshaping the web ecosystem by making citations a key mechanism for allocating attention, attribution, and downstream value. This creates a strategic tension: content providers are incentivized to optimize for model citation, while platforms must preserve answer quality and trustworthy attribution. We show that this tension can escalate into citation wars. In repeated simulations, state-of-the-art generative engine optimization (GEO) attacks adapt to conventional defenses by producing citation-seeking rewrites that degrade document quality and introduce unsupported claims. To study this problem, we formulate the supplier--platform interaction as a repeated Stackelberg game with partial monitoring. A local best-response analysis identifies when citation competition approaches an inert stationary outcome. Motivated by this finding, we propose a platform--creator mechanism called VCR based on verifiable-content rewards. Rather than only penalizing suspicious rewrites, the platform also credits rewrites that surface checkable factual substance, aligning creator incentives with answer trustworthiness. Experiments on three benchmarks show that VCR consistently achieves the largest Net defense-utility score, outperforming the strongest baseline by an average of 12.1 percentage points, and produces a win--win outcome under our empirical equivalence criterion.

</details>

### 44. Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2608.27631)　📅 2026-08

**关键词**：`tool`、`competitor-aware GEO`、`combinatorial strategy`、`Bayesian optimization`、`externality`

👤 **作者**：Vaibhav Sourirajan、Yao Zhang、Himanshu Kumar、Sahil Wadhwa、Mann Patel、Amirfarrokh Iranitalab

- 🎯 **研究动机**：传统 GEO 孤立选择改写策略，忽略关键外部性：随着内容优化被广泛采用，最优策略本身会改变
- 🔬 **研究方法**：把 GEO 形式化为竞争感知策略选择：先用组合结构贝叶斯优化（BOCS）高效搜索改写策略空间，再从黑盒观测生成偏好对与推理轨迹微调 LLM，使其分析文档语料并提出最优策略组合；构建竞争增强集 geo-bench_comp
- 📌 **结论**：geo-bench 与竞争集上多项可见性指标超既有 agentic 与单启发式方法，且可迁移到多个 OOD 数据集——从真空优化到竞争动力学

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) has emerged as a novel paradigm for transforming content to increase visibility in Large Language Model (LLM) responses. Traditional GEO methods, however, select rewriting strategies in isolation, ignoring a critical externality: as adoption of content optimization grows, optimal strategies for rewriting content change. We formalize GEO as a competitor-aware strategy selection problem and propose a two-phase pipeline to solve it: (1) We use Bayesian Optimization of Combinatorial Structures (BOCS) to efficiently search the space of rewriting strategies, (2) We generate preference pairs and grounded reasoning traces from the BOCS black-box observations to fine-tune a language model to analyze a document corpus and propose optimal rewriting strategy combinations. We achieve state-of-the-art performance across several impression metrics over existing agentic and single-heuristic methods on both geo-bench and our synthetically augmented competitive dataset geo-bench_comp. Our method also transfers to multiple out-of-distribution datasets, proving effective across domains, queries, and document types.

</details>

### 45. Agent2UCB: Agentic System for Generative Engine Optimization

📄 [arXiv](https://arxiv.org/abs/2608.29063)　📅 2026-08

**关键词**：`tool`、`agentic GEO`、`bandit`、`strategy selection`、`SEO readiness`

👤 **作者**：Sheldon Yu、…、Julian McAuley

- 🎯 **研究动机**：GEO 策略效果因内容而异，需要自主的反馈驱动选择而非人工试探
- 🔬 **研究方法**：Agent2UCB agentic 系统：对每条内容评估 9 种 GEO 策略，用融合 LLM 先验与在线奖励的 UCB bandit 加速选择；配轻量纯文本 SEO 就绪度评估（可读性/主题覆盖/EEAT 可信度）监控副作用
- 📌 **结论**：GEO-Bench 上一致可见性增益且保持 SEO 质量——AutoGEO 线的 bandit 化演进（演示系统）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model driven search engines such as Google AI Overviews and Perplexity have created new opportunities for Generative Engine Optimization (GEO) the practice of refining content to increase its likelihood of being cited or summarized by generative systems. We demonstrate Agent2UCB, an agentic GEO system that autonomously improves content visibility through customized, feedback-driven optimization. For each content item, the system evaluates nine GEO strategies, identifies the most effective method, and accelerates selection using a bandit-based Agent2UCB policy that integrates LLM priors with online reward signals. To monitor side effects, the system also provides a lightweight, text-only SEO readiness evaluation covering readability, topical coverage, and EEAT-style credibility. Experiments on GEO-Bench show consistent visibility gains while preserving SEO quality. The demo allows users to choose the websites of interest, observe the optimization workflow, and compare GEO/SEO outcomes across methods.

</details>

### 46. CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target

📄 [arXiv](https://arxiv.org/abs/2608.30466)　📅 2026-08　🏷 COLM 2026

**关键词**：`analysis`、`content homogenization`、`ecosystem simulation`、`ranking signal exploitation`

👤 **作者**：Qianwen Gao、Zichang Su、Yiwen Hou、Arlen Kumar、Leanid Palkhouski

- 🎯 **研究动机**：GEO 被广泛采用后，内容生态在反复优化下会被如何重塑——群体级效应几乎无人研究
- 🔬 **研究方法**：CHASE 受控仿真框架：以 ranking 为可见性代理（与真实生成回答中的引用验证，rank-citation AUC 0.853±0.093），迭代 排序-特征判别-改写-评测 20 轮 × 6 个域，配随机目标对照
- 📌 **结论**：全部六域质量-排序对齐下降（Spearman ρ 变化 −0.107 至 −0.018，均值 −0.068）：越贴近排序特征轮廓的文档与独立评判的文档质量越脱钩；随机目标对照显著平缓——单目标排序信号驱动的内容生态同质化。COLM 2026

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative Engine Optimization (GEO) is increasingly used to improve content visibility in LLM-based retrieval systems, yet its population-level effects under repeated optimization remain poorly understood. We introduce Content Homogenization under rAnking Signal Exploitation (CHASE), a controlled simulation framework for studying how content ecosystems are reshaped when creators repeatedly adapt documents to an LLM ranking signal. We use ranking as a proxy for source visibility and validate this abstraction against citations in grounded generated responses, obtaining a rank-citation AUC of 0.853 $\pm$ 0.093 across six domains. CHASE then iterates ranking, feature discrimination, rewriting, and evaluation over 20 rounds across different domains. Quality-ranking alignment decreases in all six domains: from R0 to R20, the change in Spearman's rho ranges from -0.107 to -0.018, with a mean change of -0.068, which means documents closer to the ranking feature profile become less aligned with independently judged document quality over the simulation horizon. A random-target control has shown that it is associated with adaptation toward ranking-derived incentives rather than iterative rewriting alone. The resulting ecosystem dynamics are strongly domain-dependent. Together, these findings show how repeated optimization against a fixed LLM ranking signal can reshape both content populations and the incentives faced by content creators.

</details>

### 47. Measuring GEO Visibility: Prompt Corpora Define the Answer Market

📄 [arXiv](https://arxiv.org/abs/2609.06811)　📅 2026-09

**关键词**：`analysis`、`GEO measurement validity`、`prompt corpus`、`answer market`、`scoring rules`

👤 **作者**：Olivier Martinez

- 🎯 **研究动机**：GEO 可见性分数聚合来源出现、引用与品牌提及——但 prompt 语料选定被评估情境、权重决定其相对重要性，二者共同定义的答案市场未必代表真实用户需求
- 🔬 **研究方法**：批判性方法论：借鉴总调查误差与 IR 评测理论，规定情境标注、prompt 表述、执行条件、权重与评分规则五要素；权重未知或待定时报告可容许分数集而非单点
- 📌 **结论**：prompt 措辞可改变检索、竞争源与生成答案；用 LLM 做出现/引用评分时，指令本身就能改变未变答案的得分——GEO 分数到底测的是什么，必须先回答测量效度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

GEO (generative engine optimization) visibility scores aggregate source appearances, citations, or brand mentions in generated answers. The prompt corpus selects the situations evaluated, while weights determine their relative importance. Together they define an "answer market" that need not represent actual user demand. Prompt wording can alter retrieval, competing sources, and generated answers. Scoring then requires identifying the appearances, citations, or mentions of interest. If a language model performs this task, its instruction can change the score assigned to an unchanged answer. Our critical survey examines how these choices help define what a GEO score measures. It draws on research into whether indicators measure the intended phenomenon, total survey error, and information retrieval evaluation. The framework specifies situation annotation, prompt formulations, execution conditions, weights, and scoring rules. When weights are unknown or remain to be chosen, the framework reports sets of admissible scores. It distinguishes values compatible with data and assumptions about a target population (partial identification) from variation across weighting conventions (normative sensitivity). A citation alone does not establish a source's contribution. The article defines a comparison of answers generated with and without a source in a controlled documentary context, distinct from an intervention on the full engine with competing sources. The framework is supported by reproducible calculations. No new experiments are reported; its general empirical validity remains to be assessed.

</details>

### 48. Auditing Source Exposure in Baidu and Google AI Search

📄 [arXiv](https://arxiv.org/abs/2609.24407)　📅 2026-09

**关键词**：`analysis`、`AI overview audit`、`source exposure`、`Baidu vs Google`、`cross-lingual`

👤 **作者**：Yibo Li、Enci Guan、Yuedan Cai、Geng Liu、Francesco Pierri

- 🎯 **研究动机**：AI 概览成为搜索界面显著层，其中文行为缺乏系统审计
- 🔬 **研究方法**：用 MS MARCO 英文查询及其中文翻译对百度与 Google 做 AI 概览跨语言审计：触发条件、被引 host 域、语言-平台组合差异
- 📌 **结论**：中文 AI 搜索源暴露的首批审计证据——GEO 叶子的中文侧补位

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated overviews are becoming an increasingly prominent layer of search interfaces, yet their behavior in Chinese-language search remains underexplored. We conduct a cross-lingual audit of AI overview behavior on Baidu and Google using English queries sampled from MS MARCO and their translated Chinese counterparts. Our analysis examines when overviews are triggered across platform-language settings, which host domains receive visible exposure in Chinese-language overviews, how concentrated that exposure is, and how source overlap varies across settings. We also compare the embedding-based semantic similarity of generated answers for matched query intents. The results reveal substantial differences across platform-language settings in overview availability and visible source exposure. At the aggregate level, the settings exhibit low overlap in visible host-domain inventories, while matched-query answers yield median cosine similarities ranging from 0.701 to 0.813. These findings indicate that answer-level semantic similarity and aggregate source exposure capture distinct dimensions of AI-mediated search. Evaluations of AI search should therefore consider not only the content of generated answers but also how source visibility is distributed across platforms, languages, and information environments.

</details>
