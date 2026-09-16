# Generative Engine Optimization Security

[返回投毒与后门目录](README.md)

## 研究方向

本页研究 Generative Engine Optimization（GEO）如何通过改写网页文本、图像或结构信号改变生成式搜索中的检索、重排、引用、可见性和推荐结果。GEO 本身包含正常的内容适配与可用性优化；安全问题出现在攻击者利用同一机制操纵排名、伪装低质量或有缺陷的对象、压制竞争者，或让 prompt injection 穿过 retriever-reranker-generator 全链路。因而本页同时保留 cooperative GEO 基础、现实 pipeline 评测和 black-hat manipulation，避免把“提升可见性”直接等同于攻击。

## 研究脉络

- **可见性优化起点：** GEO 建立生成式回答中的 visibility metric 与 GEO-Bench，研究对象由传统网页排名转向内容是否被 LLM 选择、引用和写入回答；C-SEO Bench 的多域多行动者评测则表明多数 C-SEO 方法基本无效且收益随采用者增多递减。
- **自动化与个性化优化：** AutoGEO、Mind Reader 与 AgenticGEO 从人工 heuristic 发展到 preference rule、latent user demand 和自演化 strategy search，提升内容适配能力的同时也扩大可自动化操纵的空间。
- **Black-hat rank manipulation：** Adversarial SEO、StealthRank、LLM ranker injection 与 MGEO 分别利用网页指令、可读文本 suffix、token optimization 和图文联合扰动提升目标排名。
- **全链路现实性：** SAGEO Arena、GEO-Bench 与 RAG survival 分析表明，能影响 generator 不代表能通过 retriever 与 reranker；结构信号、攻击隐蔽性和真实 search interface 都会改变结论。
- **下游安全影响：** SafeGEO 把指标从 target rank 扩展到推荐集合中的实际危害，One Polluted Page 表明单页污染即可让 LLM 推荐器批量推广虚构产品；当前防御多为静态 detector 或 prompt guard，SCI-Defense 的语义完整性评分在产品描述域近满分但在通用网页域失效，也佐证防御的场景依赖性。

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