# 模型版权保护

## 研究方向

模型版权保护研究如何通过可验证信号证明模型身份、所有权与输出来源。该方向同时涵盖从权重、输出分布、知识边界和功能表征识别模型身份与谱系的模型指纹，以及在模型或输出中嵌入检测信号的模型水印；还关注黑盒 API 审计、指纹伪造、水印移除、改写鲁棒性和部署公平性。以阻止能力复制为核心的反蒸馏工作仍归入[模型微调安全 / 反蒸馏](../finetuning/anti-distillation.md)。

## 研究脉络

- **Watermark：** 在模型输出或 reasoning trace 中嵌入可验证信号，用于内容或模型归属追踪。
- **Black-box fingerprint：** 通过精心设计的查询行为审计 API 背后的模型身份，并研究 fingerprint spoofing 风险。
- **Weight 与 functional fingerprint：** 从参数或功能响应追踪 checkpoint、训练 seed 和模型演化谱系。

## Watermark 与内容溯源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Auditing Cross-Lingual Fairness in Language Model Watermarking | analysis、model watermarking、cross-lingual fairness、copyright verification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20047) | 暂未公开 | 针对英语评测可能高估输出水印的跨语言可用性，论文联合校准阈值、阈值无关检测、三类质量指标和差异分解审计六种方案；结果发现检测与质量差距主要是语言类型家族间的结构性差异。 |
| 2026&#8209;08 | Linguistic Holonomy and Statistical Watermarks: Inner Geometry of Meaning-Preserving Transformations | analysis、model watermarking、paraphrase robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19369) | [Code](https://github.com/DCorradetti/linguistic-holonomy) | 针对端点语义相似度无法解释保义改写为何破坏统计水印，论文以 linguistic holonomy 描述完整变换路径并推导检测信号恒等式；结果表明相同 token 保留率会因编辑位置不同而留下截然不同的水印强度。 |
| 2026&#8209;05 | TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection | tool、model watermarking、content provenance、distillation tracing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12456) | 暂未公开 | 针对水印检测、文本定位与输出质量难以兼顾，论文结合双密钥 Gumbel-max、熵加权和多区域定位；结果实现无额外推理开销的强检测，并让信号在蒸馏后仍可追踪。 |
| 2026&#8209;02 | Protecting Language Models Against Unauthorized Distillation through Trace Rewriting | tool、model watermarking、distillation tracing、reasoning trace rewriting | ACL 2026 | [arXiv](https://arxiv.org/abs/2602.15143) | [Code](https://github.com/xhOwenMa/trace-rewriting) | 针对高质量推理输出同时泄露模型能力，论文动态重写完整 reasoning trace 以兼顾反蒸馏和 API 水印；结果在保持答案正确与语义连贯时降低蒸馏价值并留下可检测签名。 |
| 2025&#8209;05 | LLM Fingerprinting via Semantically Conditioned Watermarks | tool、model watermarking、ownership verification | ICLR 2026 | [arXiv](https://arxiv.org/abs/2505.16723) | 暂未公开 | 针对固定触发问答指纹易被检测且经微调或量化后失效，论文把统计水印分散到特定语义域的所有回答；结果得到更隐蔽并能抵抗常见部署变换的所有权指纹。 |

## Black-Box API 身份审计

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Your “Pro” LLM Subscription May Actually Be “Free”: Exposing Fingerprint Spoofing Risks in LLM Inference Services | attack、API identity、fingerprint spoofing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.16100) | 暂未公开 | 针对用户侧指纹可能被恶意服务商欺骗，论文提出用代理建模、奖励排序微调和蒸馏让弱模型冒充强模型的 GhostPrint；结果显示有限查询下的现有指纹可被低成本持续绕过。 |
| 2026&#8209;05 | KBF: Knowledge Boundary as Fingerprint for Language Model and Black-Box API Auditing | detection、API identity、knowledge boundary | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29524) | 暂未公开 | 针对转售 API 是否真实提供声明模型难以验证，论文用知识边界附近稳定的数值回忆行为构造低成本黑盒指纹；结果可检测经济上重要的模型替换和一定比例的混合路由攻击。 |
| 2026&#8209;03 | Real Money, Fake Models: Deceptive Model Claims in Shadow APIs | benchmark、API identity、shadow API、model substitution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.01919) | 暂未公开 | 针对第三方 shadow API 的模型声明缺乏审计，论文从效用、安全和身份三个维度比较官方与影子服务；结果发现显著性能偏差、安全行为不稳定及大量指纹验证失败。 |
| 2025&#8209;12 | Log Probability Tracking of LLM APIs | detection、API identity、output signature | ICLR 2026 | [arXiv](https://arxiv.org/abs/2512.03816) | 暂未公开 | 针对高成本审计无法持续监控 API 模型更新，论文仅请求一个 token 并检验平均 logprob 的变化；结果可发现单步微调级别的小改动且成本比既有方法低约三个数量级。 |
| 2025&#8209;10 | Every Language Model Has a Forgery-Resistant Signature | detection、API identity、fingerprint spoofing、output signature | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.14086) | 暂未公开 | 针对输出来源验证需要天然且难伪造的信号，论文利用语言模型 logprob 位于高维椭圆面的几何约束构造签名；结果给出类似消息认证的验证协议，并说明无参数访问时伪造很困难。 |
| 2025&#8209;06 | Auditing Black-Box LLM APIs with a Rank-Based Uniformity Test | detection、API identity、weight fingerprint、statistical testing | ICLR 2026 | [arXiv](https://arxiv.org/abs/2506.06975) | 暂未公开 | 针对无权重和 logits 时难以发现量化、微调或模型替换，论文提出与本地真模型比较行为排序的均匀性检验；结果在有限查询和对抗式路由场景中保持较高统计检验能力。 |
| 2024&#8209;07 | Hey, That’s My Model! Introducing Chain & Hash, an LLM Fingerprinting Technique | detection、API identity、active fingerprinting | ICLR 2026 | [arXiv](https://arxiv.org/abs/2407.10887) | [Code](https://github.com/microsoft/Chain-Hash) | 针对指纹所有权证明易碰撞且会被元提示改变输出，论文用 chain-and-hash 绑定提示与回答并在训练中加入随机填充；结果提升微调、风格变化和主动移除下的稳健性。 |

## Weight Fingerprint 与模型谱系

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | AWM: Accurate Weight-Matrix Fingerprint for Large Language Models | tool、model fingerprinting、model lineage、weight fingerprint | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.06738) · [OpenReview](https://openreview.net/forum?id=fDC5WeLeqh) | [Code](https://github.com/LUMIA-Group/AWM) | 针对深度后训练会改变模型参数排列和尺度，论文用线性分配与无偏 CKA 构造免训练权重矩阵指纹；结果在多类后训练操作后仍准确验证模型谱系且计算成本较低。 |
| 2025&#8209;09 | SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From | tool、model fingerprinting、model lineage | ICLR 2026 | [arXiv](https://arxiv.org/abs/2509.26404) | 暂未公开 | 针对训练后指纹无法覆盖预训练早期谱系，论文把随机初始化产生并持续保留的预测偏差作为 SeedPrint；结果可从初始化到后训练阶段区分种子并验证模型生命周期身份。 |
| 2025&#8209;09 | LLM DNA: Tracing Model Evolution via Functional Representations | tool、model fingerprinting、model lineage | ICLR 2026，Oral | [arXiv](https://arxiv.org/abs/2509.24496) · [OpenReview](https://openreview.net/forum?id=UIxHaAqFqQ) | [Code](https://github.com/Xtra-Computing/LLM-DNA) · [Project](https://dna.xtra.science/) | 针对海量模型的微调、蒸馏和适配谱系不透明，论文定义低维双 Lipschitz 功能表征 LLM DNA 并构建训练免疫的提取流程；结果在 305 个模型上恢复出符合架构和时间演化的谱系。 |
