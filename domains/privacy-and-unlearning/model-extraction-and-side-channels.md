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

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | One Trap to Block Them All: Defending Encoder Stealing via Isotropic Uniformity | defense、encoder stealing、model extraction、API side channel | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4852) | 暂未公开 | 针对攻击者借输出特征复制通用编码器的问题 | UniTrap 用高斯势能把输出约束为超球面各向同性均匀分布以抵消对比学习梯度 | 关键实现：UniTrap 用高斯势能把输出约束为超球面各向同性均匀分布以抵消对比学习梯度。 | 在维持授权效用的同时阻断多类编码器窃取。 |

## 模型抽取、API 攻击与 Side Channel

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models | attack、black-box API extraction、hidden reasoning asset、fidelity side channel | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20055) | [Code](https://github.com/TrustAIRLab/EchoCoT) | 针对闭源 reasoning API 把 CoT 作为隐藏模型资产、却仍返回可用于校验的行为信号 | EchoCoT 通过多步交互反复重放并优化通用注入轨迹 | 关键实现：EchoCoT 通过多步交互反复重放并优化通用注入轨迹。 | 其在八种开源和专有 LRM 上恢复与目标长度、token 高度一致的推理，Gemini-2.5 单例还从 32,948-token 目标提取 33,463 token，建立了可操作的 API 资产抽取 threat model。 |
| 2026-08 | Uncovering and Understanding Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels | detection、prefix-cache side channel、API dependency tracing、reseller supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20732) | 暂未公开 | 针对多层 LLM API 转售隐藏共同上游和请求可见方 | CacheTracer 以 Flood 写入新 cache state、再用 Prove 排除探测自身命中并测试跨端点复用 | 关键实现：CacheTracer 以 Flood 写入新 cache state、再用 Prove 排除探测自身命中并测试跨端点复用。 | 39 个端点、110 万次调用显示 37.1% 的端点对共享 cache reach、依赖链深达七层，证明软件可见缓存侧信道可恢复服务依赖并揭示集中式机密性与完整性爆炸半径。 |
| 2026-08 | JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols | attack、LLM judge extraction、black-box API、surrogate adaptation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26982) | 暂未公开 | 针对 pointwise、pairwise 与 listwise judge API 的决策能力可否在有限查询下被统一克隆 | JudgeStealer 从 pointwise 响应免费派生另外两类监督 | 并以 score smoothing 和 multi-protocol review 保持序数结构、缓解 surrogate 遗忘 | 它跨模型规模、适配方式和 reasoning setting 均优于抽取基线，并绕过代表性防御。 |
| 2026 | Steal the Patch Size: Adversarially Manipulate Vision Language Models | attack、adversarial robustness、VLM safety、model extraction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64596) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题 | 论文提出 Steal the Patch Size 攻击或威胁分析 | 关键实现：论文提出 Steal the Patch Size 攻击或威胁分析。 | 摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于对抗威胁建模。 |
| 2026 | From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs | attack、LLM API、token-length side channel、model extraction | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia) | 暂未公开 | 针对 LLM API 合并或流式传输时暴露 token 长度的问题 | PromptEcho 从长度序列推断主题并重建内容 | 主题识别率达 42.5% | 且 25.5% 重建文本的语义相似度超过 0.9。 |
| 2026 | CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks | attack、model ownership、model extraction、API side channel | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65463) | [Code](https://github.com/LabRAI/CREDIT) | 针对模型窃取、未授权训练和内容模仿使权属与版权难以审计的问题 | 论文提出 CREDIT 防御或缓解方法 | 关键实现：论文提出 CREDIT 防御或缓解方法。 | 摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于模型权属和训练数据审计。 |
| 2026 | An Empirical Study on the Resilience of Partial Merging to Model Clone Attacks | attack、empirical evaluation、model extraction、API side channel | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65910) | 暂未公开 | 针对模型输出、梯度、记忆或检索库可能泄露训练数据和真实身份的问题 | 论文提出 Empirical Study on the Resilience 攻击或威胁分析 | 关键实现：论文提出 Empirical Study on the Resilience 攻击或威胁分析。 | 摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于训练数据和身份泄漏评估。 |
| 2026 | Stealing Split Learning Bottom Models by Recovering Embedding Geometry | attack、split learning、model stealing、embedding geometry | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Stealing_Split_Learning_Bottom_Models_by_Recovering_Embedding_Geometry_CVPR_2026_paper.html) | 暂未公开 | 针对 split learning 只传中间嵌入却被认为可保护客户端模型 | 作者从嵌入几何恢复 bottom model 的功能 | 关键实现：作者从嵌入几何恢复 bottom model 的功能。 | 揭示协议中的模型资产泄漏。 |
| 2025-08 | The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again | attack、model supply chain、Pickle、stealthy poisoning | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-tong) · [arXiv](https://arxiv.org/abs/2508.19774) | 暂未公开 | 针对现有 scanner 已能发现常见 Pickle model supply-chain payload | 该工作系统挖掘 22 条反序列化路径和 133 个可用 gadget | 关键实现：该工作系统挖掘 22 条反序列化路径和 133 个可用 gadget。 | 使投毒模型在保持功能时对多类防御实现接近 100% 绕过。 |
| 2025-05 | Architectural Backdoors for Within-Batch Data Stealing and Model Inference Manipulation | attack、architectural backdoor、batch isolation、information-flow control | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2505.18323) | 暂未公开 | 针对恶意模型架构可跨 batch 窃取或篡改其他用户输入输出的问题 | 作者构造 within-batch backdoor | 关键实现：作者构造 within-batch backdoor。 | 并用信息流 non-interference 检查给出形式化防御且发现 200 余个模型存在非预期泄漏。 |
| 2025-01 | Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs ↗ | attack、partial-model extraction、safety classifier、decision-boundary theft | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2501.16534) | [Code](https://github.com/jcnf0/targeting-alignment) | 针对完整 aligned LLM 太大、难以直接复制其 safety decision boundary | 论文证明只抽取约 20% 网络即可得到 F1 超过 80% 的 surrogate safety classifier | 关键实现：论文证明只抽取约 20% 网络即可得到 F1 超过 80% 的 surrogate safety classifier。 | 该局部功能克隆随后显著降低定向 jailbreak 搜索的内存与计算成本，说明 safety classifier 本身也是可窃取的模型资产。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services | detection、black-box API identity、query-response signal、model audit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22213) | 暂未公开 | 针对 API 配置会掩盖底层模型身份的问题 | AdaptPrint 根据每轮响应自适应选择直接、续写或追问探针 | 再从查询—响应行为中识别隐藏 LLM | 结果表明即使解码参数和服务端防御变化，接口输出仍泄露可用于模型身份审计的稳定信号。 |
| 2026 | Unveiling the Pitfalls of Data-Free Backdoor Detection Against Pre-Trained Models | detection、backdoor detection、pre-trained model、convergence side channel | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-quan) | 暂未公开 | 针对 data-free backdoor detector 缺少大规模预训练模型验证的问题 | 作者评测超过 30,000 个模型并发现现有 detector 大多失效 | 关键实现：作者评测超过 30,000 个模型并发现现有 detector 大多失效。 | 再利用 convergence-speed side channel 提出更强检测方法。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs | analysis、model extraction、API side channel、intellectual property | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16391) | [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/services/api_checker/ventor_qtest) | 分析 model extraction、API side channel 风险的形成机制，重点考察 intellectual property 对安全行为的影响。 | 随着大语言模型变得越来越普遍 | 部署开放权重模型的第三方提供商已成为生态系统的重要组成部分；我们将托管模型路由形式化为随机过程，并提出 \mbox{\textbf{Ventor-QTest}}，这是一种复合黑盒审计，不需要来自目标 API 的概率信息 | 这些结果促使联合报告 AFL 和 EFL，特别是在审核长期代理任务时。 |
