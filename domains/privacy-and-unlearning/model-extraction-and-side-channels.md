# 模型抽取与 Side Channel

[返回上级目录](README.md)

## 研究方向

研究通过 prediction API、timing、cache 或其他软件与系统可见信号恢复模型参数、结构、功能或私有状态的攻击与防御；与训练数据抽取不同，本页主要保护模型本身及其服务执行边界。依赖芯片、封装或板级设备物理访问的光学、电磁、功耗等硬件 probing 不在本页范围内。

## 研究脉络

- **黑盒复制：** Query-based extraction 以有限 API 预算训练替代模型或恢复决策边界。
- **实现侧信道：** Timing、cache 和软件可见的资源行为把威胁从输出扩展到服务执行轨迹；物理芯片侧信道按兴趣边界排除。
- **防御与审计：** Watermark、query monitoring、输出限制和机密执行用于提高抽取成本或提供事后证据。
- **当前边界：** 高效 API、可用性和抗自适应抽取之间仍存在直接冲突。

## 防御与缓解

### 1. One Trap to Block Them All: Defending Encoder Stealing via Isotropic Uniformity

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4852)　📅 2026　🏷 ECCV 2026

**关键词**：`defense`、`encoder stealing`、`model extraction`、`API side channel`、`active defense`、`feature protection`

- 🎯 **研究动机**：encoder stealing借API侧信道窃取模型能力
- 🔬 **研究方法**：以各向同性均匀性构造主动陷阱防御模型窃取
- 📌 **结论**：阻断encoder stealing且正常查询不受影响

### 2. Inferring Hidden User Models from the Behavior of Personalized LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.03815)　📅 2026-09

**关键词**：`attack`、`personalized memory`、`user-model inference`、`behavioral side channel`、`personalized agent`、`user-model extraction`

👤 **作者**：Haoyang Li、Yaxin Xiao、Qingqing Ye、Huadi Zheng、Haibo Hu

- 🎯 **研究动机**：个性化 Agent 把记忆压缩为 user model 后，直接记忆提取攻击失效被当作更隐私，但被塑造的可见选择仍泄露私有信息
- 🔬 **研究方法**：提出黑盒攻击 UMPeek：从请求留下的开放选择形成假设、在普通后续任务间切换、只保留被可见行为支持且未被反驳的断言
- 📌 **结论**：在 benchmark 与真实系统上均超过现有攻击，response 级防御下仍能恢复用户信息——记录与后端不可访问不保证语义隐私

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent personalized LLM agents increasingly transform information retained in memory into compressed or structured representations, which we call user models, to guide later decisions. When source wording is removed from the state reachable through the ordinary interface, these models are commonly treated as more privacy-preserving because direct memory-extraction attacks lose the text they target. Yet we argue that user models expose a new attack surface because an attacker can still recover the private information from the personalized choices they shape, even when source records and backend state remain inaccessible. We therefore introduce UMPeek, a black-box attack based on hypothesis-guided adaptive probing to infer such hidden user model. It forms hypotheses from choices left open by a request, switches among ordinary follow-up tasks, and retains only claims supported and not contradicted by visible behavior. We conduct an extensive benchmark evaluation across diverse personalization tasks and user-model backends against existing attacks. We further validate UMPeek in real-world systems using information confirmed to be retained, and we evaluate defenses against its adaptive probing. Overall, UMPeek outperforms existing attacks in both benchmark and real-world comparisons and continues to recover user information under response-level defenses, showing that keeping records and backend state inaccessible does not guarantee semantic privacy when retained information shapes visible behavior.

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

### 4. Uncovering and Understanding Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels

📄 [arXiv](https://arxiv.org/abs/2608.20732)　📅 2026-08

**关键词**：`detection`、`API dependency lineage`、`prefix-cache side channel`、`reseller provenance`、`API dependency tracing`、`reseller supply chain`

👤 **作者**：Zimo Ji、…、Shuai Wang

- 🎯 **研究动机**：多级转售形成不透明 LLM API 供应链，用户请求可穿越未披露的上游转售商，现有研究只审计单个转售商
- 🔬 **研究方法**：CacheTracer 以 prefix-cache 复用为侧信道测依赖：Flood 经一个端点填充新鲜缓存、Prove 探测另一端点能否复用并排除探针自建命中；39 个端点、636 对、110 万请求
- 📌 **结论**：37.1% 端点对共享缓存可达、包含序跨七层、某缓存可达被至少 31 个节点包含——隐藏依赖深且集中，共同上游路径的失败可波及多个下游用户

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM API resellers have become an important access layer to modern LLM services. However, multi-level resale creates an opaque supply chain: a user's request may traverse undisclosed upstream resellers, each of which can inspect or modify prompts and responses, inducing ecosystem-level confidentiality and integrity risks. Existing studies audit individual resellers, but provide little visibility into hidden dependencies across resellers. We present CacheTracer, the first API-only measurement of such hidden dependencies. Our key insight is to exploit prefix-cache reuse as a side channel to measure dependency via cache-reach relations. CacheTracer operationalizes this insight with two primitives: Flood populates fresh cache state through one endpoint, and Prove probes whether another can reuse it while excluding probe-created hits. We then conduct a real-world measurement study with CacheTracer on 39 reseller endpoints, sending 1.1 million API requests across 636 endpoint pairs. Our measurements reveal a deep, concentrated cache-reach structure: 37.1% of measured pairs exhibit shared cache reach, the containment order spans seven layers, and one cache reach is contained within at least 31 of other nodes. We further find that the recovered structure is model-specific. We also evaluate the validity of CacheTracer through both real-world consistency checks and controlled experiments. The results show its high reliability and accuracy. These findings reveal substantial hidden dependencies among seemingly independent API resellers. Such deep and concentrated dependencies can create a large potential blast radius, where a confidentiality or integrity failure along a common upstream path may affect users across multiple downstream resellers.

</details>

### 5. JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols

📄 [arXiv](https://arxiv.org/abs/2608.26982)　📅 2026-08

**关键词**：`attack`、`judge capability extraction`、`cross-protocol distillation`、`query-efficient stealing`、`LLM judge extraction`、`black-box API`

👤 **作者**：Chen Chen、…、Kwok-Yan Lam

- 🎯 **研究动机**：LLM judge 的评分能力是高价值 IP，黑盒 API 暴露于抽取攻击，而现有 extraction 方法不针对 judge 且不支持多评测协议与有限查询预算
- 🔬 **研究方法**：提出 JudgeStealer，利用跨协议一致性把 pointwise 分数转换为 pairwise/listwise 监督而不额外查询，按语义多样性、预测不确定性与潜在偏差动态选点，辅以分数平滑与多协议复习
- 📌 **结论**：对 SOTA LLM judge 与 reward model 的抽取准确率在 pointwise/pairwise/listwise 上最高达 73.3%/87.0%/71.6%，并能抵抗代表性 extraction 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing extraction methods do not specifically target LLM judges and provide limited support for multiple evaluation protocols under restricted query budgets. In this study, we propose JUDGESTEALER, the first query-efficient model extraction framework for replicating judging capabilities across pointwise scoring, pairwise comparison, and listwise ranking protocols. JUDGESTEALER exploits the strong cross-protocol agreement to acquire pointwise scores and transform them into pairwise and listwise supervisions without additional victim queries. To capture informative judge patterns and improve query efficiency, JUDGESTEALER dynamically selects pointwise inputs based on semantic diversity, predictive uncertainty, and potential judge biases. It further applies score smoothing and multi-protocol review to preserve the ordinal structure of scores and mitigate catastrophic forgetting during surrogate adaptation. Extensive experiments on state-of-the-art LLM-as-a-judge and reward models show that JUDGESTEALER consistently outperforms existing extraction baselines, achieving up to 73.3%, 87.0%, and 71.6% accuracy for pointwise, pairwise, and listwise evaluation, respectively. JUDGESTEALER also remains effective across different sur- rogate model scales, adaptation strategies, and reasoning settings. Moreover, JUDGESTEALER demonstrates robustness against representative extraction defenses.

</details>

### 6. Steal the Patch Size: Adversarially Manipulate Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2607.00174) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64596)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial robustness`、`VLM safety`、`model extraction`、`adversarial attack`、`empirical evaluation`

👤 **作者**：Kai Hu、Akash Bharadwaj、Weichen Yu、Matt Fredrikson

- 🎯 **研究动机**：部署 VLM 的视觉 tokenizer 配置（patch 大小、预处理管线）属私有信息，其泄露可支撑模型窃取与定向对抗操纵
- 🔬 **研究方法**：利用 ViT patch 化的任务级侧信道：网格图像与隐藏 patch 网格对齐时边界线索被抹除引发周期性精度塌陷，扫描网格尺寸推断 patch 大小，再用填充与一致性检验恢复预处理管线与分辨率
- 📌 **结论**：在 Qwen-VL 变体与 GPT、Claude 等专有模型上可靠恢复 tokenizer 参数，并使预处理感知迁移攻击与定向操纵成为可能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present a black-box model-stealing attack that recovers private vision-tokenizer configurations of deployed vision-language models (VLMs), including the visual patch size and input preprocessing pipeline. The key idea is a task-level side channel induced by ViT-style patchification: when a synthetic grid image is aligned with the hidden patch grid, boundary cues are erased at tokenization, causing periodic accuracy drop. By sweeping the grid cell size and measuring these collapses, we infer the patch size; by introducing padding and a consistency-check test, we further identify whether preprocessing is dynamic- or fixed-resolution and recover the target resize resolution. Across open-source Qwen-VL variants and proprietary models including GPT and Claude, we reliably recover tokenizer-related parameters. Finally, we show that such leakage enables preprocessing-aware transfer attacks and model-targeted adversarial manipulation.

</details>

### 7. From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM API`、`token-length side channel`、`model extraction`、`content reconstruction`

👤 **作者**：Sijia Li、…、Qi Li

- 🎯 **研究动机**：现代 LLM 服务以多 token 块流式输出，看似缓解 token 级侧信道，但合并块长度构成新的侧信道
- 🔬 **研究方法**：PromptEcho 被动窃听攻击：把重构形式化为约束序列恢复——语义感知推理分解合并长度观测，用微调 LM 的语言先验做概率语义对齐推断最可能 token
- 📌 **结论**：GPT-4o 与 DeepSeek-V3 真实 API 流量上 42.5% 会话正确推断主题、25.5% 响应以 0.9 以上余弦相似度重构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly accessed via remote APIs over encrypted channels. While previous studies have shown that fine-grained side channels can leak information under token-by-token processing, modern LLM services typically stream outputs in multi-token chunks, seemingly mitigating such token-level leakage. However, in this paper, we demonstrate that token aggregation does not eliminate privacy risks. Instead, it introduces a merged token-length side channel. In this channel, the sizes of encrypted response chunks inadvertently expose character-length patterns of merged token groups. To study the practical implications of this leakage, we propose PromptEcho, a passive eavesdropping attack that reconstructs semantically meaningful portions of natural-language responses from observations of merged token lengths. PromptEcho frames the reconstruction task as a constrained sequence recovery problem, leveraging semantics-aware reasoning to resolve the ambiguity caused by merged token transmission. Specifically, PromptEcho first applies semantics-aware reasoning to decompose merged-token length observations, then uses probabilistic semantic alignment with a fine-tuned language model's linguistic priors to infer the most likely underlying tokens. We evaluate PromptEcho on real-world API interaction traffic from multiple commercial LLM services, correctly inferring the topic for 42.5% of sessions and reconstructing 25.5% of responses with a cosine similarity above 0.9 on OpenAI's GPT-4o and DeepSeek-V3. These findings demonstrate that merged-token transmission remains vulnerable to token-length side-channel attacks, indicating practical privacy risks from encrypted traffic observations under the evaluated API-based LLM settings.

</details>

### 8. CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks

📄 [arXiv](https://arxiv.org/abs/2602.20419) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65463)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`model ownership`、`model extraction`、`API side channel`、`certified robustness`

👤 **作者**：Bolin Shen、Zhan Cheng、Neil Zhenqiang Gong、Fan Yao、Yushun Dong

- 🎯 **研究动机**：MLaaS 面临模型提取攻击，对可疑模型的所有权验证缺乏严格理论保证
- 🔬 **研究方法**：CREDIT 用互信息量化 DNN 间相似度，提出实用验证阈值并给出严格的理论保证
- 📌 **结论**：多领域多任务数据集上达 SOTA 所有权验证性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine Learning as a Service (MLaaS) has emerged as a widely adopted paradigm for providing access to deep neural network (DNN) models, enabling users to conveniently leverage these models through standardized APIs. However, such services are highly vulnerable to Model Extraction Attacks (MEAs), where an adversary repeatedly queries a target model to collect input-output pairs and uses them to train a surrogate model that closely replicates its functionality. While numerous defense strategies have been proposed, verifying the ownership of a suspicious model with strict theoretical guarantees remains a challenging task. To address this gap, we introduce CREDIT, a certified ownership verification against MEAs. Specifically, we employ mutual information to quantify the similarity between DNN models, propose a practical verification threshold, and provide rigorous theoretical guarantees for ownership verification based on this threshold. We extensively evaluate our approach on several mainstream datasets across different domains and tasks, achieving state-of-the-art performance. Our implementation is publicly available at: https://github.com/LabRAI/CREDIT.

</details>

### 9. An Empirical Study on the Resilience of Partial Merging to Model Clone Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/65910)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`empirical evaluation`、`model extraction`、`API side channel`、`privacy attack`、`data leakage`

👤 **作者**：Tiantong Wu、Yurong Hao、Wei Yang Bryan Lim

- 🎯 **研究动机**：partial model merging 保留私有参数以降低隐私风险，但其隐私属性从未被检验
- 🔬 **研究方法**：提出模型克隆攻击，在八种先验知识（部分训练数据、模型参数、结构）组合场景下评估重建未共享私有部分的能力
- 📌 **结论**：即使只暴露少量训练数据、参数或结构，攻击者也能恢复私有模型的大部分性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model merging is a promising technique to enhance the capabilities of neural networks (NNs) by integrating multiple downstream fine-tuned models without requiring access to clients' raw data or substantial computation resources. However, conventional model merging typically requires collecting the full set of fine-tuned model parameters from multiple clients, which may expose them to model-privacy risks. An emerging approach, known as partial model merging (PMM), mitigates this risk by splitting each model into private and shared parts, where only the shared part is merged while the private part remains local to each client. Despite its stricter parameter fusion, PMM can still achieve competitive performance compared to full-parameter sharing. However, the privacy properties of PMM remain underexplored. In this paper, we propose a novel model clone attack and assess the risk of reconstructing the unshared private part of a partially merged model under eight attack scenarios with varying prior knowledge (i.e., partial training data, model parameters and/or model structure). Our comprehensive experiments reveal that merging NNs without adequate protection is highly vulnerable. Even when only a small fraction of training data, model parameters, or model structure is exposed, adversaries can still recover significant portions of the private model's performance.

</details>

### 10. Stealing Split Learning Bottom Models by Recovering Embedding Geometry

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Stealing_Split_Learning_Bottom_Models_by_Recovering_Embedding_Geometry_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`split learning`、`model stealing`、`embedding geometry`

👤 **作者**：Qinbo Zhang、Yanhang Shi、Ziyi Zhang、Hao Wang、Sai Qian Zhang、Jian Li

- 🎯 **研究动机**：VFL 中扰动或解耦嵌入通道的防御仍可被诚实但好奇的服务器侧窃取攻击攻破
- 🔬 **研究方法**：提出 VENOM 几何感知窃取：在服务器观察的嵌入上学习对比空间与邻域图，用邻匹配损失加逐点、特征形状对齐训练代理模型，恢复防御未抹除的关系结构
- 📌 **结论**：在 6 个数据集上无防御与多种防御下均超越标准窃取方法，OOD 辅助数据下依然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vertical federated learning (VFL) trains models by splitting computation across clients and a server that only exchange intermediate embeddings. Recent work shows that a server even if honest-but-curious can steal a client's bottom model by querying the system and regressing on the returned embeddings, and in response, defenses perturb or decouple the embedding channel. We show these defenses remain vulnerable. We propose VENOM, a geometry-aware stealing attack. VENOM first learns a contrastive space over server-observed embeddings, then builds a neighborhood graph and trains a surrogate bottom model to match targets and respect local geometry via a neighbor-matching loss alongside pointwise and feature-shape alignment. This strategy preserves the relational structure that defenses fail to erase, effectively recoupling the embeddings produced by multi-branch and noise-based defenses. Across six datasets, VENOM consistently outperforms standard stealing methods under no defense and multiple defenses, and remains effective with out-of-distribution (OOD) auxiliary data.

</details>

### 11. The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again

📄 [arXiv](https://arxiv.org/abs/2508.19774) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-tong)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`attack`、`model supply chain`、`Pickle`、`stealthy poisoning`

👤 **作者**：Tong Liu、Guozhu Meng、Peng Zhou、Zizhuang Deng、Shuaiyin Yao、Kai Chen

- 🎯 **研究动机**：pickle 反序列化漏洞长期未解，现有扫描器对模型投毒面理解不全、检测逻辑脆弱
- 🔬 **研究方法**：系统披露 pickle 投毒面：识别五大框架 22 条模型加载路径（19 条被漏检），提出 Exception-Oriented Programming 绕过技术，并在风险函数面发现 133 个可利用 gadget
- 📌 **结论**：gadget 绕过率近 100%，最佳扫描器下仍达 89%；获厂商致谢与 6000 美元赏金

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pickle deserialization vulnerabilities have persisted throughout Python's history, remaining widely recognized yet unresolved. Due to its ability to transparently save and restore complex objects into byte streams, many AI/ML frameworks continue to adopt pickle as the model serialization protocol despite its inherent risks. As the open-source model ecosystem grows, model-sharing platforms such as Hugging Face have attracted massive participation, significantly amplifying the real-world risks of pickle exploitation and opening new avenues for model supply chain poisoning. Although several state-of-the-art scanners have been developed to detect poisoned models, their incomplete understanding of the poisoning surface leaves the detection logic fragile and allows attackers to bypass them. In this work, we present the first systematic disclosure of the pickle-based model poisoning surface from both model loading and risky function perspectives. Our research demonstrates how pickle-based model poisoning can remain stealthy and highlights critical gaps in current scanning solutions. On the model loading surface, we identify 22 distinct pickle-based model loading paths across five foundational AI/ML frameworks, 19 of which are entirely missed by existing scanners. We further develop a bypass technique named Exception-Oriented Programming (EOP) and discover 9 EOP instances, 7 of which can bypass all scanners. On the risky function surface, we discover 133 exploitable gadgets, achieving almost a 100% bypass rate. Even against the best-performing scanner, these gadgets maintain an 89% bypass rate. By systematically revealing the pickle-based model poisoning surface, we achieve practical and robust bypasses against real-world scanners. We responsibly disclose our findings to corresponding vendors, receiving acknowledgments and a $6000 bug bounty.

</details>

### 12. Architectural Backdoors for Within-Batch Data Stealing and Model Inference Manipulation

📄 [arXiv](https://arxiv.org/abs/2505.18323) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-05　🏷 SaTML 2026

**关键词**：`attack`、`architecture`、`within-batch attack`、`architectural backdoor`、`batch isolation`、`information-flow control`

👤 **作者**：Nicolas Küchler、Ivan Petrov、Conrad Grobler、Ilia Shumailov

- 🎯 **研究动机**：传统后门仅操纵预测、现实危害不明，批处理推理的跨用户信息流风险未被研究
- 🔬 **研究方法**：设计利用批处理的新型架构后门窃取同批用户输入输出，并提出基于信息流控制、证明批内不干涉的形式化缓解
- 📌 **结论**：攻击可注入 Transformer 等主流架构；缓解方法在 Hugging Face 扫出 200 余个因动态量化致批内信息泄露的模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For nearly a decade the academic community has investigated backdoors in neural networks, primarily focusing on classification tasks where adversaries manipulate the model prediction. While demonstrably malicious, the immediate real-world impact of such prediction-altering attacks has remained unclear. In this paper we introduce a novel and significantly more potent class of backdoors that builds upon recent advancements in architectural backdoors. We demonstrate how these backdoors can be specifically engineered to exploit batched inference, a common technique for hardware utilization, enabling large-scale user data manipulation and theft. By targeting the batching process, these architectural backdoors facilitate information leakage between concurrent user requests and allow attackers to fully control model responses directed at other users within the same batch. In other words, an attacker who can change the model architecture can set and steal model inputs and outputs of other users within the same batch. We show that such attacks are not only feasible but also alarmingly effective, can be readily injected into prevalent model architectures, (e.g. Transformers), and represent a truly malicious threat to user privacy and system integrity. Critically, to counteract this new class of vulnerabilities, we propose a deterministic mitigation strategy that provides formal guarantees against this new attack vector, unlike prior work that relied on LLMs to find the backdoors. Our mitigation strategy employs a novel Information Flow Control mechanism that analyzes the model graph and proves non-interference between different user inputs within the same batch. Using our mitigation strategy we perform a large scale analysis of models hosted through Hugging Face and find over 200 models that introduce (unintended) information leakage between batch entries due to the use of dynamic quantization.

</details>

### 13. Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2501.16534) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-01　🏷 SaTML 2026

**关键词**：`attack`、`safety-boundary extraction`、`surrogate classifier`、`jailbreak transfer`、`safety classifier`、`surrogate extraction`

👤 **作者**：Jean-Charles Noirot Ferrand、Yohan Beugin、Eric Pauley、Ryan Sheatsley、Patrick McDaniel

- 🎯 **研究动机**：对齐在 LLM 内嵌入决定拒答与否的安全分类器，能否提取该分类器未被研究
- 🔬 **研究方法**：从 LLM 子集构建候选代理分类器，评估其与安全分类器的一致性并攻击候选测迁移率
- 📌 **结论**：仅 20% 架构即达 80% 以上 F1 一致；用 50% Llama-2 的代理攻击 ASR 达 70%，远超直接攻击的 22%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment in large language models (LLMs) is used to enforce guidelines such as safety. Yet, alignment fails in the face of jailbreak attacks that modify inputs to induce unsafe outputs. In this paper, we introduce and evaluate a new technique for jailbreak attacks. We observe that alignment embeds a safety classifier in the LLM responsible for deciding between refusal and compliance, and seek to extract an approximation of this classifier: a surrogate classifier. To this end, we build candidate classifiers from subsets of the LLM. We first evaluate the degree to which candidate classifiers approximate the LLM's safety classifier in benign and adversarial settings. Then, we attack the candidates and measure how well the resulting adversarial inputs transfer to the LLM. Our evaluation shows that the best candidates achieve accurate agreement (an F1 score above 80%) using as little as 20% of the model architecture. Further, we find that attacks mounted on the surrogate classifiers can be transferred to the LLM with high success. For example, a surrogate using only 50% of the Llama 2 model achieved an attack success rate (ASR) of 70% with half the memory footprint and runtime -- a substantial improvement over attacking the LLM directly, where we only observed a 22% ASR. These results show that extracting surrogate classifiers is an effective and efficient means for modeling (and therein addressing) the vulnerability of aligned models to jailbreaking attacks. The code is available at https://github.com/jcnf0/targeting-alignment.

</details>

### 14. AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services

📄 [arXiv](https://arxiv.org/abs/2608.22213)　📅 2026-08

**关键词**：`detection`、`response-adaptive fingerprinting`、`black-box API`、`copyright audit`、`black-box API identity`、`query-response signal`

👤 **作者**：Yilin Li、Yifei Zhang、Guozhu Meng

- 🎯 **研究动机**：黑盒 LLM 指纹用固定查询集，在 system prompt 与采样设置等真实配置下表现差，阻碍版权审计与安全评估
- 🔬 **研究方法**：AdaptPrint 响应自适应指纹，整合 Direct Probing、Continuation Probing、Follow-up Probing 三种递进的一致性探测，再在候选模型间做相似度匹配
- 📌 **结论**：27 个候选模型中 Top-1/Top-3/Top-5 准确率达 80.6%/90.3%/92.1%，对不同防御策略与解码参数稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box LLM services have emerged as a practical deployment paradigm. Nevertheless, their opacity also hinders the systematic assessment of security risks and complicates copyright auditing for model owners. Black-box LLM fingerprinting, which identifies the underlying LLM identity through query-response interactions, offers a promising way to bridge this gap. Existing approaches typically collect responses from target LLM services using a fixed set of queries and perform poorly in the presence of realistic and complex configurations (e.g., system prompt and sampling settings). To overcome these limitations, we propose AdaptPrint, a response-adaptive fingerprinting method for revealing hidden LLM identities in black-box LLM services. AdaptPrint integrates three progressive response consistency probing strategies: Direct Probing, Continuation Probing, and Follow-up Probing. AdaptPrint determines the final LLM identity by performing similarity matching among candidate LLMs. Experimental results show that AdaptPrint significantly outperforms state-of-the-art methods among 27 candidate models, achieving Top-1, Top-3, and Top-5 accuracies of 80.6%, 90.3%, and 92.1%. AdaptPrint also demonstrates strong robustness across different defense strategies and decoding parameters.

</details>

### 15. Unveiling the Pitfalls of Data-Free Backdoor Detection Against Pre-Trained Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-quan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`benchmark`、`backdoor detection`、`pre-trained model`、`convergence side channel`

👤 **作者**：Quan Zhao、…、Yang Zhang

- 🎯 **研究动机**：无数据后门检测方法很少在预训练模型上评估，报告的强性能可能造成虚假安全感
- 🔬 **研究方法**：构建覆盖 30000 多个模型与常见后门攻击的大规模基准；提出以收敛速度作为侧信道信号的新检测器
- 📌 **结论**：现有无数据方法在多数预训练模型上失效；新检测器达 SOTA，但严重漏洞仍存

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to deep learning models, enabling adversaries to manipulate the output through hidden triggers. Recent detection methods aim to identify backdoors without relying on clean samples or assumptions about attacks. Although they report strong performance, these methods are rarely evaluated on pre-trained models. In this paper, we present the first large-scale study of data-free backdoor detection on pre-trained models. Our benchmark includes more than 30,000 models and covers common backdoor attacks. We find that existing data-free methods fail on most pre-trained models, leading to a false sense of security. Despite our effective improvements, serious vulnerabilities remain. To address this, we propose using convergence speed as a new side-channel signal for backdoor detection. Using this signal, we reveal the cause of the remaining vulnerabilities and build a novel data-free detector that achieves state-of-the-art performance against existing methods. We further analyze how backdoor attacks evade detection and outline unresolved issues. Our results indicate that detecting backdoor attacks requires further exploration. We hope that our work can draw attention to the vulnerabilities in backdoor detection mechanisms for machine learning systems.

</details>

### 16. Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs

📄 [arXiv](https://arxiv.org/abs/2608.16391)　📅 2026-08

**关键词**：`analysis`、`model extraction`、`API side channel`、`intellectual property`

👤 **作者**：Xiangfan Wu、…、Jing Guo

- 🎯 **研究动机**：第三方托管开源权重模型的 API 是否忠实服务缺黑盒审计方法
- 🔬 **研究方法**：把托管路由形式化为随机过程：重复请求组件重建类别输出分布报告平均保真损失 AFL，长序列组件用独立运行报告极端保真损失 EFL，无需目标 API 概率信息
- 📌 **结论**：AFL 与 logprob 衍生 coarsened-KL 线性一致；显著 EFL 与 Terminal-Bench 通过率随任务暴露下降相合而与 GPQA 准确率无关，建议 AFL 与 EFL 联合报告

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem. We formalize hosted model routing as a stochastic process and propose \mbox{\textbf{Ventor-QTest}}, a composite black-box audit that requires no probability information from the target API. Its repeated-request component sends each frozen constrained context to the target multiple times, reconstructs a categorical output distribution from the returned text counts, and reports \emph{average fidelity loss} (AFL) as a null-bias-corrected, within-window mean coarsened-KL statistic. Its long-sequence component uses independent runs to report \emph{extreme fidelity loss} (EFL) through the empirical upper tail of a run-level reference-centered-surprisal statistic. Across three logprob-capable route conditions, AFL shows strong linear descriptive agreement with a logprob-derived coarsened-KL comparator. Across seven route snapshots, 20-run sequence probes reveal route-specific EFL variation. AFL and EFL have little detectable route-level association with GPQA-Diamond accuracy. In contrast, pronounced EFL coincides with a decline in Terminal-Bench pass rate as task exposure increases. This pattern may arise because correctness in long-horizon tasks is more sensitive to extreme fidelity loss. These results motivate reporting AFL and EFL jointly, particularly when auditing long-horizon agentic tasks. The open-source implementation is available at https://github.com/Tencent/AI-Infra-Guard/tree/main/services/api_checker/ventor_qtest.

</details>