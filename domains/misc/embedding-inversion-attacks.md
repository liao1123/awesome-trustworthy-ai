# 嵌入反演攻击

## 研究方向

嵌入反演攻击研究攻击者能否从文本或图像的稠密向量中恢复原始内容、敏感属性或可读语义，直接关系到向量数据库、RAG 和 Embeddings as a Service 的隐私边界。该方向包括基于生成解码、迭代搜索和扩散模型的直接重建，跨模型、跨领域与跨语言的少样本或零样本迁移，以及通过嵌入空间对齐降低对目标编码器的依赖；同时也关注目标嵌入模型识别等攻击前置条件和现有防护面对反演时的失效边界。

## 研究脉络

- **文本重建起点：** 早期 embedding inversion 依赖目标模型查询来执行 sentence reconstruction。
- **攻击能力扩展：** 后续工作发展出 surrogate alignment、few-shot、zero-shot、cross-lingual 和跨模型迁移方法。
- **模态与前置条件扩展：** 图像 embedding 与模型身份推断扩大了泄漏范围，并降低攻击者预先知道目标编码器的要求。

## Embedding Inversion 攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings | attack、noise-protected embedding、unsupervised denoising、text reconstruction | 未确认（arXiv Comments：Accepted by IEEE ICDM 2026） | [arXiv](https://arxiv.org/abs/2608.18610) | 暂未公开 | 针对攻击者只得到加入 Gaussian noise 的 embedding、无法获得干净目标时现有生成式反演会陷入 Double Noise Trap，DAEI 先用 SURE 无监督训练 residual denoiser，再把恢复后的表示送入文本生成反演；BLEU 相对提高约 154%，token F1 与 ROUGE-L 提高 32%–60%，说明简单扰动不能阻止自适应向量重建。 |
| 2026&#8209;08 | Black-Box Embedding Inversion Attack on Vector Databases ↗ | attack、embedding inversion、vector database、black-box reconstruction | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817917) | 暂未公开 | 针对向量数据库只暴露黑盒检索接口便被视为不会泄露原文的问题，论文从交互反馈重建存储内容与敏感语义；结果表明把文本替换为 embedding 并不能自动建立数据保密边界。 |
| 2026&#8209;07 | Embedding Inference Attack | attack、embedding-model inference、model identification、black-box retrieval | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.01276) | 暂未公开 | 针对嵌入反演等攻击通常需要预先知道目标编码器的问题，论文仅观察黑盒检索系统返回的无序文档并用定制查询识别候选嵌入模型；结果在加入重排器和真实 RAG 系统时仍然有效，并表明相似度阈值可缓解风险。 |
| 2026&#8209;02 | Embedding Inversion via Conditional Masked Diffusion Language Models | attack、text-embedding inversion、text inversion、masked diffusion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.11047) | [Code](https://github.com/jina-ai/embedding-inversion-demo) | 针对自回归反演需要逐词生成或反复校正的问题，论文以自适应层归一化将目标嵌入注入条件掩码扩散模型并并行去噪全部 token；结果仅需 8 次前向传播即可在三个嵌入模型上恢复 32-token 文本，推理时无需访问目标编码器。 |
| 2026&#8209;02 | Zero2Text: Zero-Training Cross-Domain Inversion Attacks on Textual Embeddings | attack、text-embedding inversion、text inversion、cross-domain attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.01757) | 暂未公开 | 针对优化式攻击查询成本高、对齐式攻击依赖同域泄露数据的问题，论文以 LLM 先验和动态岭回归进行递归在线对齐，无需训练数据即可适配未知领域；结果在 MS MARCO 的 OpenAI 目标模型上较基线提升 1.8 倍 ROUGE-L 和 6.4 倍 BLEU-2，常规差分隐私防御也未能有效阻止该攻击。 |
| 2026&#8209;01 | Semantic Leakage from Image Embeddings | attack、image-embedding inversion、semantic leakage、local neighborhood | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.22929) | 暂未公开 | 针对图像嵌入只有在重建像素时才会泄露隐私的假设，论文提出 SLImE，以局部训练的语义检索器和现成模型沿对齐后的语义邻域传播信息；结果无需任务专用解码器也能从多种开放和闭源嵌入中恢复标签、符号表示与连贯描述。 |
| 2025&#8209;04 | Information Leakage of Sentence Embeddings via Generative Embedding Inversion Attacks | attack、text-embedding inversion、generative inversion、pretraining leakage | SIGIR 2025 | [Official](https://doi.org/10.1145/3726302.3730303) · [arXiv](https://arxiv.org/abs/2504.16609) | [Code](https://github.com/taslanidis/GEIA) | 针对句子嵌入是否泄露其预训练语料中的敏感知识缺少分析的问题，论文复现 GEIA 并比较原始与掩码样本在攻击者嵌入空间中的生成似然；结果可从多种常用句子嵌入模型中恢复与预训练知识相关的有意义敏感信息。 |
| 2025&#8209;03 | Universal Zero-shot Embedding Inversion | attack、text-embedding inversion、zero-shot inversion、adversarial decoding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.00147) | [Code](https://github.com/collinzrj/adversarial_decoding) | 针对高精度反演必须为每个编码器单独训练模型并大量查询的问题，论文提出基于对抗解码的 ZSInvert，无需嵌入专用反演训练即可攻击不同文本编码器；结果以较低查询和计算成本恢复出原文的关键语义信息。 |
| 2025&#8209;02 | ALGEN: Few-shot Inversion Attacks on Textual Embeddings using Alignment and Generation | attack、text-embedding inversion、text inversion、few-shot attack | ACL 2025 Main | [Official](https://aclanthology.org/2025.acl-long.1185/) · [arXiv](https://arxiv.org/abs/2502.11308) | [Code](https://github.com/siebeniris/ALGEN) | 针对反演模型依赖海量泄露句子的问题，论文先把受害者嵌入一步对齐到攻击空间，再用生成模型恢复文本；结果单个样本已可部分反演、约一千样本达到较优表现，并可跨领域和语言迁移，而所测防御均不有效。 |
| 2024&#8209;10 | Rank Matters: Understanding and Defending Model Inversion Attacks via Low-Rank Feature Filtering | defense、model inversion、feature rank、privacy filter | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3780328) · [arXiv](https://arxiv.org/abs/2410.05814) | [Code](https://github.com/Chrisqcwx/LoFt) | 论文发现高秩表征携带更多可反演细节，并用 low-rank feature filtering 降低重建质量而保持下游预测能力。 |
| 2024&#8209;06 | Transferable Embedding Inversion Attack: Uncovering Privacy Risks in Text Embeddings without Model Queries | attack、text-embedding inversion、text inversion、transfer attack | ACL 2024 Main | [Official](https://aclanthology.org/2024.acl-long.230/) · [arXiv](https://arxiv.org/abs/2406.10280) | 暂未公开 | 针对攻击者无法直接查询原始嵌入模型的现实威胁，论文训练代理模型模仿受害者嵌入行为并将反演能力迁移到目标；结果在多种嵌入模型和临床数据上显著优于传统方法，说明少量泄露嵌入仍会暴露敏感文本。 |
| 2024&#8209;01 | Text Embedding Inversion Security for Multilingual Language Models | attack、multilingual embedding inversion、multilingual inversion、cross-lingual attack | ACL 2024 Main | [Official](https://aclanthology.org/2024.acl-long.422/) · [arXiv](https://arxiv.org/abs/2401.12192) | [Code](https://github.com/siebeniris/multivec2text) | 针对反演攻击与防御长期只评测英语的问题，论文系统定义并测试黑盒多语言及跨语言反演，同时提出简单掩码防御；结果发现多语言模型可能更易受攻击且英语防御不能直接迁移，而该掩码方法可同时保护单语和多语言模型。 |
| 2023&#8209;10 | Text Embeddings Reveal (Almost) As Much As Text | attack、text-embedding inversion、text inversion、iterative correction | EMNLP 2023 Main | [Official](https://aclanthology.org/2023.emnlp-main.765/) · [arXiv](https://arxiv.org/abs/2310.06816) | [Code](https://github.com/jxmorris12/vec2text) | 针对单次条件解码难以从稠密嵌入还原原文的问题，论文把反演建模为反复生成、重嵌入和校正的受控生成过程；结果可精确恢复 92% 的 32-token 输入，并能从临床笔记嵌入中恢复姓名等个人信息。 |
| 2023&#8209;05 | Sentence Embedding Leaks More Information than You Expect: Generative Embedding Inversion Attack to Recover the Whole Sentence | attack、text-embedding inversion、generative inversion、sentence recovery | Findings of ACL 2023 | [Official](https://aclanthology.org/2023.findings-acl.881/) · [arXiv](https://arxiv.org/abs/2305.03010) | [Code](https://github.com/HKUST-KnowComp/GEIA) | 针对既有嵌入攻击通常只能推断属性或无序关键词的问题，论文将句子嵌入作为解码器的初始 token 表示并训练生成式反演攻击 GEIA；结果较分类式基线恢复出更连贯且与原文上下文更接近的完整句子。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Mitigating Gradient Inversion Risks in Language Models via Token Obfuscation | defense、gradient inversion、shadow token、semantic utility | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3785389) · [arXiv](https://arxiv.org/abs/2602.15897) | [Code](https://github.com/Trusted-System-Lab/GHOST) | 针对 language model gradient 可映射回原 token；GHOST 用语义不同但 embedding 邻近的 shadow token 训练；结果切断 gradient—token 可逆关系并尽量保留下游效用。 |

## 基础对齐 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;05 | Harnessing the Universal Geometry of Embeddings | tool、text-embedding inversion、embedding-space translation、unsupervised alignment | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4175dee33d6145cb8f0323703d138a53-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.12540) | [Code](https://github.com/rjha18/vec2vec) | 针对攻击者缺少配对数据、编码器和跨空间锚点时无法利用未知嵌入的问题，论文学习往返通用潜在表示的无监督嵌入翻译；结果在架构、规模和训练数据不同的模型间仍保持较高余弦相似度，并能仅凭向量数据库提取敏感属性。 |
