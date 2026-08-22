# 模型抽取与 Side Channel

[返回上级目录](README.md)

## 研究方向

研究通过 prediction API、timing、cache、功耗或系统实现恢复模型参数、结构、功能或私有状态的攻击与防御；与训练数据抽取不同，本页主要保护模型本身及其执行边界。

## 研究脉络

- **黑盒复制：** Query-based extraction 以有限 API 预算训练替代模型或恢复决策边界。
- **实现侧信道：** Timing、cache 和硬件观测把威胁从输出扩展到执行轨迹与资源行为。
- **防御与审计：** Watermark、query monitoring、输出限制和机密执行用于提高抽取成本或提供事后证据。
- **当前边界：** 高效 API、可用性和抗自适应抽取之间仍存在直接冲突。

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | One Trap to Block Them All: Defending Encoder Stealing via Isotropic Uniformity | defense、encoder stealing、model extraction、API side channel | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4852) | 暂未公开 | 针对攻击者借输出特征复制通用编码器的问题，UniTrap 用高斯势能把输出约束为超球面各向同性均匀分布以抵消对比学习梯度，在维持授权效用的同时阻断多类编码器窃取。 |

## 模型抽取、API 攻击与 Side Channel

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Steal the Patch Size: Adversarially Manipulate Vision Language Models | attack、adversarial robustness、VLM safety、model extraction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64596) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Steal the Patch Size 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于对抗威胁建模。 |
| 2026 | Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks | attack、model extraction、API side channel、intellectual property | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61636) | 暂未公开 | 针对模型输出、梯度、记忆或检索库可能泄露训练数据和真实身份的问题，论文提出 Revisiting Asymmetries in Black-box Link 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于训练数据和身份泄漏评估。 |
| 2026 | From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs | attack、LLM API、token-length side channel、model extraction | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia) | 暂未公开 | 针对 LLM API 合并或流式传输时暴露 token 长度的问题，PromptEcho 从长度序列推断主题并重建内容，主题识别率达 42.5%，且 25.5% 重建文本的语义相似度超过 0.9。 |
| 2026 | CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks | attack、model ownership、model extraction、API side channel | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65463) | [Code](https://github.com/LabRAI/CREDIT) | 针对模型窃取、未授权训练和内容模仿使权属与版权难以审计的问题，论文提出 CREDIT 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于模型权属和训练数据审计。 |
| 2026 | An Empirical Study on the Resilience of Partial Merging to Model Clone Attacks | attack、empirical evaluation、model extraction、API side channel | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65910) | 暂未公开 | 针对模型输出、梯度、记忆或检索库可能泄露训练数据和真实身份的问题，论文提出 Empirical Study on the Resilience 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于训练数据和身份泄漏评估。 |
| 2025&#8209;08 | The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again | attack、model supply chain、Pickle、stealthy poisoning | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-tong) · [arXiv](https://arxiv.org/abs/2508.19774) | 暂未公开 | 针对现有 scanner 已能发现常见 Pickle model supply-chain payload，该工作系统挖掘 22 条反序列化路径和 133 个可用 gadget，使投毒模型在保持功能时对多类防御实现接近 100% 绕过。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Unveiling the Pitfalls of Data-Free Backdoor Detection Against Pre-Trained Models | detection、backdoor detection、pre-trained model、convergence side channel | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-quan) | 暂未公开 | 针对 data-free backdoor detector 缺少大规模预训练模型验证的问题，作者评测超过 30,000 个模型并发现现有 detector 大多失效，再利用 convergence-speed side channel 提出更强检测方法。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs | analysis、model extraction、API side channel、intellectual property | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16391) | [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/services/api_checker/ventor_qtest) | 随着大语言模型变得越来越普遍，部署开放权重模型的第三方提供商已成为生态系统的重要组成部分；我们将托管模型路由形式化为随机过程，并提出 \mbox{\textbf{Ventor-QTest}}，这是一种复合黑盒审计，不需要来自目标 API 的概率信息；这些结果促使联合报告 AFL 和 EFL，特别是在审核长期代理任务时。 |
