# 其他投毒与后门

[返回投毒与后门目录](README.md)

本页收录尚未形成稳定独立子领域、但具有明确投毒或后门 threat model 的特殊方向。当前包括密码式模型后门和推荐系统投毒；每个方向保留独立小节与边界，后续论文数量和方法路线足够稳定时再拆分为专页。

## 密码式模型后门

研究借助密码学不可区分性构造的模型后门在真实学习流程中的攻击可行性、统计隐蔽性与审计边界；本节只收录以模型后门为核心 threat model 的工作，不扩展到一般密码学研究。

> **边界说明：** 这里的 cryptographic backdoor 指攻击者植入的恶意条件后门，不是模型水印、版权保护或所有权验证。后门式水印相关工作见 [独立专题](../content-authenticity/backdoor-based-watermarking-and-ownership.md)。

### 现实隐蔽性与机制复测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Rethinking the Stealthiness of Cryptographically Undetectable Backdoors in Practical RFF Learning | attack、cryptographic backdoor、random Fourier feature、stealth evaluation | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817768) | [Code](https://github.com/CryptoAILab/CryptoBackdoor) | 研究 cryptographic backdoor、random Fourier feature 场景下的攻击面，重点考察 stealth evaluation 如何影响目标模型或系统。 | 论文把理论上不可区分的密码式后门放入实际 RFF 学习流程复测 | 关键实现：论文把理论上不可区分的密码式后门放入实际 RFF 学习流程复测。 | 揭示有限精度、训练配置和统计检验会改变其隐蔽性结论。 |

## 推荐系统投毒

研究攻击者通过恶意用户、交互或内容注入操纵推荐模型与排序结果，以及在缺少攻击标签时对异常训练信号进行检测和缓解的方法。

### 检测与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Silencing the Poison: An Unsupervised Granular Ball Defense Approach in Local Smoothing Context for Recommender Systems | defense、recommender poisoning、unsupervised detection、local smoothing | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817740) | 暂未公开 | 研究如何防御 recommender poisoning、unsupervised detection 威胁，并评估 local smoothing 条件下的安全收益与效用代价。 | 论文以无监督 granular ball 和局部平滑识别推荐数据中的异常注入 | 关键实现：论文以无监督 granular ball 和局部平滑识别推荐数据中的异常注入。 | 在缺少攻击标签时缓解投毒对排序结果的操纵。 |
