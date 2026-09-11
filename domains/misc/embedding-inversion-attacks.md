# 嵌入反演攻击

## 研究方向

嵌入反演攻击研究攻击者能否从文本或图像的稠密向量中恢复原始内容、敏感属性或可读语义，直接关系到向量数据库、RAG 和 Embeddings as a Service 的隐私边界。该方向包括基于生成解码、迭代搜索和扩散模型的直接重建，跨模型、跨领域与跨语言的少样本或零样本迁移，以及通过嵌入空间对齐降低对目标编码器的依赖；同时也关注目标嵌入模型识别等攻击前置条件和现有防护面对反演时的失效边界。

## 研究脉络

- **文本重建起点：** 早期 embedding inversion 依赖目标模型查询来执行 sentence reconstruction。
- **攻击能力扩展：** 后续工作发展出 surrogate alignment、few-shot、zero-shot、cross-lingual 和跨模型迁移方法。
- **模态与前置条件扩展：** 图像 embedding 与模型身份推断扩大了泄漏范围，并降低攻击者预先知道目标编码器的要求。

## Embedding Inversion 攻击

### 1. Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings

📄 [arXiv](https://arxiv.org/abs/2608.18610)　📅 2026-08

**关键词**：`attack`、`noise-protected embedding`、`unsupervised denoising`、`text reconstruction`、`noise-aware inversion`、`Double Noise Trap`

👤 **作者**：Yubo Wang、…、Weiqing Wang

- 🎯 **研究动机**：高斯加噪被视为对抗嵌入反演的简单有效防御，对显式考虑扰动过程的自适应攻击者是否安全未知
- 🔬 **研究方法**：识别双噪声陷阱并提 DAEI：残差去噪自编码器（以 Stein 无偏风险估计免监督训练）串联生成式文本反演
- 📌 **结论**：BLEU 相对现有生成式反演基线提升约 154%，token F1 与 ROUGE-L 提升 32-60%——简单高斯扰动不足以阻止嵌入泄露敏感信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dense text embeddings are widely used in data mining, retrieval, and downstream machine learning systems due to their compact and semantically rich representations, but recent embedding inversion attacks have shown that they can expose substantial information about the original text, leading to serious privacy leakage risks. A common defense is to release perturbed embeddings by adding Gaussian noise, which is simple yet effective against standard inversion attacks and does not significantly degrade embedding utility for downstream tasks. However, it remains unclear whether such noise-protected embeddings are sufficiently safe against adaptive attackers that explicitly account for the perturbation process. In this paper, we study text embedding inversion in a noise-protected setting, where the attacker can observe only noisy embeddings and has no access to clean embedding targets. We first analyze why existing generative inversion methods fail under this setting and identify a "Double Noise Trap", which fundamentally prevents standard generative inversion models from achieving high-quality reconstruction. To address this challenge, we propose DAEI, a denoising-aware embedding inversion pipeline that combines a residual denoising autoencoder with generative text inversion where the denoiser is trained in an unsupervised manner using Stein's unbiased risk estimate to enable denoising from noisy observations alone. Extensive experiments show that DAEI achieves approximately 154\% relative improvement in BLEU over the existing generative inversion baseline, while also improving token-level F1 and ROUGE-L by 32--60\%. The promising inversion performance of DAEI challenges the prevailing assumption that simple Gaussian perturbation is sufficient to prevent sensitive information leakage from embedding representations.

</details>

### 2. Black-Box Embedding Inversion Attack on Vector Databases

🌐 [Project](https://doi.org/10.1145/3770855.3817917)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`embedding inversion`、`vector database`、`black-box reconstruction`、`stored-content extraction`、`vector-database leakage`

- 🎯 **研究动机**：向量数据库的embedding被默认安全，黑盒内容还原能力未评估
- 🔬 **研究方法**：对向量数据库发起黑盒embedding inversion攻击重建存储内容
- 📌 **结论**：仅凭查询接口即可高精度重建原文，向量库存在实质泄漏

### 3. Embedding Inference Attack

📄 [arXiv](https://arxiv.org/abs/2607.01276)　📅 2026-07

**关键词**：`attack`、`embedding-model inference`、`model identification`、`black-box retrieval`

👤 **作者**：Cedric Fitiavana Raelijohn、Sébastien Gambs、Jean-Francois Rajotte

- 🎯 **研究动机**：黑盒 IR 系统中攻击者仅观察无序检索文档集即可发起 embedding inversion 之外的新威胁
- 🔬 **研究方法**：提出 embedding inference attack：构造定制查询从候选集中识别检索系统使用的嵌入模型，验证加入 reranker 后仍有区分性，并在真实 RAG 系统上绕过 LLM 对非规范问题的拒答倾向
- 📌 **结论**：定制查询可有效识别在用嵌入模型，相似度阈值等缓解部分有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embedding models are essential components of modern Information Retrieval (IR) systems, yet they are typically hidden behind APIs. Recent works have shown that dense IR system can lead to security vulnerabilities such as embedding inversion attacks. However, such attacks usually require that the attacker knows the embedding model for the attack to be applicable. In this paper, we study IR systems under a black-box setting in which the adversary observes only the unordered set of retrieved documents, without ranking or similarity scores. We demonstrate that in such contexts, tailored queries allow an adversary to identify which embedding model is in use from a set of known model candidate, which we coin as an embedding inference attack (EIA). We also show that certain queries remain discriminative even when the system includes a reranker as a potential defense mechanism. We further validate our method on a real Retrieval-Augmented Generation (RAG) system, in which the tailored queries bypass the LLM's tendency to reject inputs it does not recognize as well-formed questions. Finally, we propose and evaluate other mitigation strategies such as similarity thresholds.

</details>

### 4. Embedding Inversion via Conditional Masked Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2602.11047)　📅 2026-02

**关键词**：`attack`、`text-embedding inversion`、`text inversion`、`masked diffusion`

👤 **作者**：Han Xiao

- 🎯 **研究动机**：自回归嵌入反演需逐词生成或访问目标编码器，效率受限
- 🔬 **研究方法**：把嵌入反演建模为条件 masked diffusion，以自适应层归一化注入目标嵌入，迭代去噪并行恢复全部 token
- 📌 **结论**：三个嵌入模型上仅需 8 次前向即可恢复 32-token 序列，推理时无需访问目标编码器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We frame embedding inversion as conditional masked diffusion, recovering all tokens in parallel through iterative denoising rather than sequential autoregressive generation. A masked diffusion language model is conditioned on the target embedding via adaptive layer normalization, requiring only 8 forward passes with no access to the target encoder at inference time. On 32-token sequences across three embedding models, the method achieves token recovery through parallel denoising without requiring encoder access, iterative correction, or architecture-specific alignment. Source code and live demo are available at https://github.com/jina-ai/embedding-inversion-demo.

</details>

### 5. Zero2Text: Zero-Training Cross-Domain Inversion Attacks on Textual Embeddings

📄 [arXiv](https://arxiv.org/abs/2602.01757)　📅 2026-02

**关键词**：`attack`、`text-embedding inversion`、`text inversion`、`cross-domain attack`

👤 **作者**：Doohyun Kim、Donghwa Kang、Kyungjae Lee、Hyeongboo Baek、Brent Byunghoon Kang

- 🎯 **研究动机**：嵌入反演中优化法查询成本过高、对齐法依赖同域训练数据，严格黑盒跨域设定下双双失效
- 🔬 **研究方法**：Zero2Text 免训练框架：以递归在线对齐把 LLM 先验与动态岭回归结合，迭代把生成对齐到目标嵌入，无需泄露任何数据对
- 📌 **结论**：MS MARCO 上对 OpenAI 目标模型 ROUGE-L 提升 1.8 倍、BLEU-2 提升 6.4 倍即可恢复未知域句子，且差分隐私等标准防御无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of retrieval-augmented generation (RAG) has established vector databases as critical infrastructure, yet they introduce severe privacy risks via embedding inversion attacks. Existing paradigms face a fundamental trade-off: optimization-based methods require computationally prohibitive queries, while alignment-based approaches hinge on the unrealistic assumption of accessible in-domain training data. These constraints render them ineffective in strict black-box and cross-domain settings. To dismantle these barriers, we introduce Zero2Text, a novel training-free framework based on recursive online alignment. Unlike methods relying on static datasets, Zero2Text synergizes LLM priors with a dynamic ridge regression mechanism to iteratively align generation to the target embedding on-the-fly. We further demonstrate that standard defenses, such as differential privacy, fail to effectively mitigate this adaptive threat. Extensive experiments across diverse benchmarks validate Zero2Text; notably, on MS MARCO against the OpenAI victim model, it achieves 1.8x higher ROUGE-L and 6.4x higher BLEU-2 scores compared to baselines, recovering sentences from unknown domains without a single leaked data pair.

</details>

### 6. Semantic Leakage from Image Embeddings

📄 [arXiv](https://arxiv.org/abs/2601.22929)　📅 2026-01

**关键词**：`attack`、`image-embedding inversion`、`semantic leakage`、`local neighborhood`

👤 **作者**：Yiyi Chen、Qiongkai Xu、Desmond Elliott、Qiongxiu Li、Johannes Bjerva

- 🎯 **研究动机**：图像嵌入通常被认为隐私风险有限，该假设从未被严格检验
- 🔬 **研究方法**：形式化语义泄漏：对齐下保留局部语义邻域即可经一连串有损映射传播语义；SLImE 以本地训练的语义检索器加现成模型，从压缩嵌入恢复标签、符号表示与连贯描述，无需任务专用解码器
- 📌 **结论**：在 GEMINI、COHERE、NOMIC、CLIP 等嵌入模型上一致恢复语义信息，揭示图像嵌入的固有漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image embeddings are generally assumed to pose limited privacy risk. We challenge this assumption by formalizing semantic leakage as the ability to recover semantic structures from compressed image embeddings. Surprisingly, we show that semantic leakage does not require exact reconstruction of the original image. Preserving local semantic neighborhoods under embedding alignment is sufficient to expose the intrinsic vulnerability of image embeddings. Crucially, this preserved neighborhood structure allows semantic information to propagate through a sequence of lossy mappings. Based on this conjecture, we propose Semantic Leakage from Image Embeddings (SLImE), a lightweight inference framework that reveals semantic information from standalone compressed image embeddings, incorporating a locally trained semantic retriever with off-the-shelf models, without training task-specific decoders. We thoroughly validate each step of the framework empirically, from aligned embeddings to retrieved tags, symbolic representations, and grammatical and coherent descriptions. We evaluate SLImE across a range of open and closed embedding models, including GEMINI, COHERE, NOMIC, and CLIP, and demonstrate consistent recovery of semantic information across diverse inference tasks. Our results reveal a fundamental vulnerability in image embeddings, whereby the preservation of semantic neighborhoods under alignment enables semantic leakage, highlighting challenges for privacy preservation.1

</details>

### 7. Information Leakage of Sentence Embeddings via Generative Embedding Inversion Attacks

📄 [arXiv](https://arxiv.org/abs/2504.16609) · 🌐 [Project](https://doi.org/10.1145/3726302.3730303)　📅 2025-04　🏷 SIGIR 2025

**关键词**：`attack`、`text-embedding inversion`、`generative inversion`、`pretraining leakage`

👤 **作者**：Antonios Tragoudaras、Theofanis Aslanidis、Emmanouil Georgios Lionis、Marina Orozco González、Panagiotis Eustratiadis

- 🎯 **研究动机**：GEIA 表明句嵌入可反演原句，但是否泄露预训练数据敏感信息未知
- 🔬 **研究方法**：不改 GEIA 攻击架构，比较掩码与原始版本预训练数据在攻击者嵌入空间的 log-likelihood 差异以检测泄露
- 📌 **结论**：可从流行句嵌入模型恢复与其预训练知识相关的敏感信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text data are often encoded as dense vectors, known as embeddings, which capture semantic, syntactic, contextual, and domain-specific information. These embeddings, widely adopted in various applications, inherently contain rich information that may be susceptible to leakage under certain attacks. The GEIA framework highlights vulnerabilities in sentence embeddings, demonstrating that they can reveal the original sentences they represent. In this study, we reproduce GEIA's findings across various neural sentence embedding models. Additionally, we contribute new analysis to examine whether these models leak sensitive information from their training datasets. We propose a simple yet effective method without any modification to the attacker's architecture proposed in GEIA. The key idea is to examine differences between log-likelihood for masked and original variants of data that sentence embedding models have been pre-trained on, calculated on the embedding space of the attacker. Our findings indicate that following our approach, an adversary party can recover meaningful sensitive information related to the pre-training knowledge of the popular models used for creating sentence embeddings, seriously undermining their security. Our code is available on: https://github.com/taslanidis/GEIA

</details>

### 8. Universal Zero-shot Embedding Inversion

📄 [arXiv](https://arxiv.org/abs/2504.00147)　📅 2025-03

**关键词**：`attack`、`text-embedding inversion`、`zero-shot inversion`、`adversarial decoding`

👤 **作者**：Collin Zhang、John X. Morris、Vitaly Shmatikov

- 🎯 **研究动机**：vec2text 等嵌入反演需为每个嵌入训练专门模型且查询量大
- 🔬 **研究方法**：提出 ZSInvert，基于对抗解码的零样本反演方法，无需训练嵌入专用模型即可用于任意文本嵌入
- 📌 **结论**：快速、少查询地恢复多个嵌入对应文本的关键语义信息，揭示向量数据库的泄露风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embedding inversion, i.e., reconstructing text given its embedding and black-box access to the embedding encoder, is a fundamental problem in both NLP and security. From the NLP perspective, it helps determine how much semantic information about the input is retained in the embedding. From the security perspective, it measures how much information is leaked by vector databases and embedding-based retrieval systems. State-of-the-art methods for embedding inversion, such as vec2text, have high accuracy but require (a) training a separate model for each embedding, and (b) a large number of queries to the corresponding encoder. We design, implement, and evaluate ZSInvert, a zero-shot inversion method based on the recently proposed adversarial decoding technique. ZSInvert is fast, query-efficient, and can be used for any text embedding without training an embedding-specific inversion model. We measure the effectiveness of ZSInvert on several embeddings and demonstrate that it recovers key semantic information about the corresponding texts.

</details>

### 9. ALGEN: Few-shot Inversion Attacks on Textual Embeddings using Alignment and Generation

📄 [arXiv](https://arxiv.org/abs/2502.11308) · 🎓 [Official](https://aclanthology.org/2025.acl-long.1185/)　📅 2025-02　🏷 ACL 2025

**关键词**：`attack`、`text-embedding inversion`、`text inversion`、`few-shot attack`

👤 **作者**：Yiyi Chen、Qiongkai Xu、Johannes Bjerva

- 🎯 **研究动机**：已有嵌入反演攻击需数百万句子训练攻击模型，假设不现实
- 🔬 **研究方法**：ALGEN 一步优化将受害嵌入对齐到攻击空间，再用生成模型重建文本
- 📌 **结论**：单个样本即可部分反演、1k 样本达最优，跨域跨语言迁移且所测防御均无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing popularity of Large Language Models (LLMs) and vector databases, private textual data is increasingly processed and stored as numerical embeddings. However, recent studies have proven that such embeddings are vulnerable to inversion attacks, where original text is reconstructed to reveal sensitive information. Previous research has largely assumed access to millions of sentences to train attack models, e.g., through data leakage or nearly unrestricted API access. With our method, a single data point is sufficient for a partially successful inversion attack. With as little as 1k data samples, performance reaches an optimum across a range of black-box encoders, without training on leaked data. We present a Few-shot Textual Embedding Inversion Attack using ALignment and GENeration (ALGEN), by aligning victim embeddings to the attack space and using a generative model to reconstruct text. We find that ALGEN attacks can be effectively transferred across domains and languages, revealing key information. We further examine a variety of defense mechanisms against ALGEN, and find that none are effective, highlighting the vulnerabilities posed by inversion attacks. By significantly lowering the cost of inversion and proving that embedding spaces can be aligned through one-step optimization, we establish a new textual embedding inversion paradigm with broader applications for embedding alignment in NLP.

</details>

### 10. Transferable Embedding Inversion Attack: Uncovering Privacy Risks in Text Embeddings without Model Queries

📄 [arXiv](https://arxiv.org/abs/2406.10280) · 🎓 [Official](https://aclanthology.org/2024.acl-long.230/)　📅 2024-06　🏷 ACL 2024

**关键词**：`attack`、`text-embedding inversion`、`text inversion`、`transfer attack`

👤 **作者**：Yu-Hsiang Huang、Yuche Tsai、Hsiang Hsiao、Hong-Yi Lin、Shou-De Lin

- 🎯 **研究动机**：已有嵌入反演攻击需直接访问原嵌入模型，现实中攻击者往往没有该权限
- 🔬 **研究方法**：用代理模型模仿受害模型行为，将反演能力迁移到目标嵌入，无需查询原模型
- 📌 **结论**：多嵌入模型与临床数据上显著优于传统方法，揭示嵌入技术的隐私风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This study investigates the privacy risks associated with text embeddings, focusing on the scenario where attackers cannot access the original embedding model. Contrary to previous research requiring direct model access, we explore a more realistic threat model by developing a transfer attack method. This approach uses a surrogate model to mimic the victim model's behavior, allowing the attacker to infer sensitive information from text embeddings without direct access. Our experiments across various embedding models and a clinical dataset demonstrate that our transfer attack significantly outperforms traditional methods, revealing the potential privacy vulnerabilities in embedding technologies and emphasizing the need for enhanced security measures.

</details>

### 11. Text Embedding Inversion Security for Multilingual Language Models

📄 [arXiv](https://arxiv.org/abs/2401.12192) · 🎓 [Official](https://aclanthology.org/2024.acl-long.422/)　📅 2024-01　🏷 ACL 2024

**关键词**：`attack`、`multilingual embedding inversion`、`multilingual inversion`、`cross-lingual attack`

👤 **作者**：Yiyi Chen、Heather Lent、Johannes Bjerva

- 🎯 **研究动机**：嵌入反演攻防研究仅覆盖英语，其他语言暴露于攻击风险
- 🔬 **研究方法**：定义黑盒多语言与跨语言反演攻击问题并系统实验，提出简单 masking 防御
- 📌 **结论**：多语言 LLM 可能更易受反演攻击且英语防御无效；掩码防御可同时保护单语与多语言模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Textual data is often represented as real-numbered embeddings in NLP, particularly with the popularity of large language models (LLMs) and Embeddings as a Service (EaaS). However, storing sensitive information as embeddings can be susceptible to security breaches, as research shows that text can be reconstructed from embeddings, even without knowledge of the underlying model. While defence mechanisms have been explored, these are exclusively focused on English, leaving other languages potentially exposed to attacks. This work explores LLM security through multilingual embedding inversion. We define the problem of black-box multilingual and cross-lingual inversion attacks, and explore their potential implications. Our findings suggest that multilingual LLMs may be more vulnerable to inversion attacks, in part because English-based defences may be ineffective. To alleviate this, we propose a simple masking defense effective for both monolingual and multilingual models. This study is the first to investigate multilingual inversion attacks, shedding light on the differences in attacks and defenses across monolingual and multilingual settings.

</details>

### 12. Text Embeddings Reveal (Almost) As Much As Text

📄 [arXiv](https://arxiv.org/abs/2310.06816) · 🎓 [Official](https://aclanthology.org/2023.emnlp-main.765/)　📅 2023-10　🏷 EMNLP 2023

**关键词**：`attack`、`text-embedding inversion`、`text inversion`、`iterative correction`

👤 **作者**：John X. Morris、Volodymyr Kuleshov、Vitaly Shmatikov、Alexander M. Rush

- 🎯 **研究动机**：文本嵌入泄漏原文信息的程度缺乏定量刻画，朴素条件解码效果差
- 🔬 **研究方法**：把反演建模为受控生成（再嵌入后逼近潜在空间不动点），vec2text 迭代生成-重嵌入-校正
- 📌 **结论**：精确恢复 92% 的 32-token 输入，并能从临床笔记嵌入恢复全名等隐私

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How much private information do text embeddings reveal about the original text? We investigate the problem of embedding \textit{inversion}, reconstructing the full text represented in dense text embeddings. We frame the problem as controlled generation: generating text that, when reembedded, is close to a fixed point in latent space. We find that although a naïve model conditioned on the embedding performs poorly, a multi-step method that iteratively corrects and re-embeds text is able to recover $92\%$ of $32\text{-token}$ text inputs exactly. We train our model to decode text embeddings from two state-of-the-art embedding models, and also show that our model can recover important personal information (full names) from a dataset of clinical notes. Our code is available on Github: \href{https://github.com/jxmorris12/vec2text}{github.com/jxmorris12/vec2text}.

</details>

### 13. Sentence Embedding Leaks More Information than You Expect: Generative Embedding Inversion Attack to Recover the Whole Sentence

📄 [arXiv](https://arxiv.org/abs/2305.03010) · 🎓 [Official](https://aclanthology.org/2023.findings-acl.881/)　📅 2023-05　🏷 ACL 2023

**关键词**：`attack`、`text-embedding inversion`、`generative inversion`、`sentence recovery`

👤 **作者**：Haoran Li、Mingshi Xu、Yangqiu Song

- 🎯 **研究动机**：嵌入信息泄漏研究多止步属性或关键词推断，完整句子反演未被充分探索
- 🔬 **研究方法**：GEIA 将句子嵌入视为初始 token 表示，训练解码器直接解码整个序列
- 📌 **结论**：优于既有反演攻击，能生成与原文连贯且上下文相似的完整句子

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sentence-level representations are beneficial for various natural language processing tasks. It is commonly believed that vector representations can capture rich linguistic properties. Currently, large language models (LMs) achieve state-of-the-art performance on sentence embedding. However, some recent works suggest that vector representations from LMs can cause information leakage. In this work, we further investigate the information leakage issue and propose a generative embedding inversion attack (GEIA) that aims to reconstruct input sequences based only on their sentence embeddings. Given the black-box access to a language model, we treat sentence embeddings as initial tokens' representations and train or fine-tune a powerful decoder model to decode the whole sequences directly. We conduct extensive experiments to demonstrate that our generative inversion attack outperforms previous embedding inversion attacks in classification metrics and generates coherent and contextually similar sentences as the original inputs.

</details>

### 14. Harnessing the Universal Geometry of Embeddings

📄 [arXiv](https://arxiv.org/abs/2505.12540) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4175dee33d6145cb8f0323703d138a53-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`tool`、`text-embedding inversion`、`embedding-space translation`、`unsupervised alignment`

👤 **作者**：Rishi Jha、Collin Zhang、Vitaly Shmatikov、John X. Morris

- 🎯 **研究动机**：缺少无配对数据的嵌入空间转换方法，其对向量数据库的安全影响未评估
- 🔬 **研究方法**：提出首个无监督嵌入翻译方法，把任意嵌入经普适潜表示映射到其他向量空间并保持几何结构
- 📌 **结论**：跨架构、参数量与训练数据的模型对均获高余弦相似度；攻击者仅凭向量即可做分类与属性推断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce the first method for translating text embeddings from one vector space to another without any paired data, encoders, or predefined sets of matches. Our unsupervised approach translates any embedding to and from a universal latent representation (i.e., a universal semantic structure conjectured by the Platonic Representation Hypothesis). Our translations achieve high cosine similarity across model pairs with different architectures, parameter counts, and training datasets. The ability to translate unknown embeddings into a different space while preserving their geometry has serious implications for the security of vector databases. An adversary with access only to embedding vectors can extract sensitive information about the underlying documents, sufficient for classification and attribute inference.

</details>

### 15. A Novel Semantic Manifold Alignment Attack against Embedding-to-Embedding Obfuscation in Privacy-Preserving LLMs

📄 [arXiv](https://arxiv.org/abs/2609.06749)　📅 2026-09

**关键词**：`attack`、`embedding obfuscation`、`manifold alignment`、`privacy-preserving inference`、`inversion`

👤 **作者**：Sicong Li、…、Miao Pan

- 🎯 **研究动机**：隐私保护 LLM 的 E2EO 嵌入混淆抗传统反演攻击，但其大规模一对一替换保留语义结构
- 🔬 **研究方法**：PMA 将混淆向量流视为未知 tokenizer 语言：Word2Vec 分别建模混淆流与公开语料的共现，流形对齐后映射回明文
- 📌 **结论**：仅需混淆流+目标分词器+公开语料，明文恢复率持续超过 SOTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread applications of large language models (LLMs), privacy-preserving inference has become increasingly essential for sensitive queries. To balance privacy and utility, a series of lightweight obfuscation approaches has recently been proposed, where users locally transform plaintext embeddings into the fixed ciphertext ones. While such Embedding-to-Embedding Obfuscation (E2EO) schemes demonstrate considerable resilience against traditional token frequency and embedding inversion attacks, the core mechanism behind remains to be the large-scale one-to-one substitution, which provides no cryptographic guarantees. In this paper, we propose Proxy Manifold Alignment (PMA), a novel attack against E2EO in privacy-preserving LLMs. Our key observation is that E2EO schemes keep the original semantic structure, so that the obfuscated vector stream can be regarded as an unknown tokenizer-language whose symbols are the vectors themselves. Therefore, the proposed ciphertext to plaintext reconstruction attack can be formulated as a translation task from the unknown tokenizer-language to plaintext. Specifically, by only accessing the obfuscated vector stream, the target tokenizer and a public corpus, the PMA attack first employs Word2Vec to model the co-occurrence patterns within the obfuscated stream and the public corpus independently, and constructs two proxy vector embeddings. Then, the attack aligns the underlying manifolds of these two embeddings based on structural similarity. Finally, it maps the obfuscated vectors back to plaintext. Experimental results demonstrate that PMA consistently achieves higher plaintext recovery than other state-of-the-art attack methods.

</details>

### 16. Shadow Queries for Private Retrieval in Vector Databases

📄 [arXiv](https://arxiv.org/abs/2609.04767)　📅 2026-09

**关键词**：`defense`、`embedding inversion`、`private RAG retrieval`、`semantic decoupling`

👤 **作者**：Xinguo Feng、…、Guangdong Bai

- 🎯 **研究动机**：云端向量数据库中的文档 embedding 可被 embedding inversion 攻击重建原文，加噪或缩放防御隐私有限或重创检索效用
- 🔬 **研究方法**：提出 SHAQ：不直接存储文档 embedding，而用生成模型为每篇文档生成覆盖不同语义侧面的多样 shadow queries，编码后替代原 embedding 存储，解耦存储向量与源文本
- 📌 **结论**：恢复率最低降至 0.2104、比基线防御多保护 19.50% token，同时 MAP@10 最高 0.7967（效用反升 5.53%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly rely on information retrieval (IR) systems, such as Retrieval-Augmented Generation (RAG), to incorporate domain-specific knowledge without costly re-training. These systems often store pre-computed document embeddings in cloud-based vector databases. However, such embeddings are vulnerable to embedding inversion attacks (EIAs), which can reconstruct their underlying text. Existing defenses, such as adding noise or scaling embeddings, often provide limited privacy or significantly reduce retrieval utility. We propose SHAQ (shadow query generation), a semantic-decomposition and embedding-decoupling defense against EIAs. SHAQ is based on the insight that EIAs rely on the strong coupling between an embedding and its original text. Instead of storing document embeddings directly, SHAQ uses a generative language model to create diverse shadow queries that capture different semantic aspects of each document. These queries are then encoded and stored in place of the original document embeddings, thereby decomposing document semantics and decoupling stored embeddings from the source text. Experiments across diverse IR datasets show that SHAQ substantially improves privacy while preserving retrieval utility, achieving a recovery rate as low as 0.2104, defending up to 19.50% more tokens than baseline defenses, and reaching up to 0.7967 MAP@10 with up to 5.53% utility improvement. These results demonstrate that semantic decomposition and embedding decoupling provide an effective alternative to directly modifying embeddings for defending against EIAs.

</details>
