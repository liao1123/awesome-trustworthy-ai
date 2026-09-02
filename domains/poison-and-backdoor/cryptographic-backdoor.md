# 密码式模型后门

[返回投毒与后门目录](README.md)

## 研究方向

研究借助密码学不可区分性构造的模型后门在真实学习流程中的攻击可行性、统计隐蔽性与审计边界；本页只收录以模型后门为核心 threat model 的工作，不扩展到一般密码学研究。

## 研究脉络

- **理论到实现：** 检查理论不可检测性在有限精度、具体特征映射和实际训练配置下是否仍然成立。
- **隐蔽性复测：** 将攻击成功率与可区分性分开评估，并使用适配实际部署条件的统计检验。
- **审计边界：** 区分构造本身的理论保证、实现泄漏的侧信号和防御者可获得的观测能力。

## 现实隐蔽性与机制复测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Rethinking the Stealthiness of Cryptographically Undetectable Backdoors in Practical RFF Learning | attack、cryptographic backdoor、random Fourier feature、stealth evaluation | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817768) | [Code](https://github.com/CryptoAILab/CryptoBackdoor) | 研究 cryptographic backdoor、random Fourier feature 场景下的攻击面，重点考察 stealth evaluation 如何影响目标模型或系统。 | 论文把理论上不可区分的密码式后门放入实际 RFF 学习流程复测 | 关键实现：论文把理论上不可区分的密码式后门放入实际 RFF 学习流程复测。 | 揭示有限精度、训练配置和统计检验会改变其隐蔽性结论。 |
