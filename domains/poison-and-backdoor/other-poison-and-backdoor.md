# 其他投毒与后门

[返回投毒与后门目录](README.md)

本页收录尚未形成稳定独立子领域、但具有明确投毒或后门 threat model 的特殊方向。当前包括密码式模型后门和推荐系统投毒；每个方向保留独立小节与边界，后续论文数量和方法路线足够稳定时再拆分为专页。

## 密码式模型后门

研究借助密码学不可区分性构造的模型后门在真实学习流程中的攻击可行性、统计隐蔽性与审计边界；本节只收录以模型后门为核心 threat model 的工作，不扩展到一般密码学研究。

> **边界说明：** 这里的 cryptographic backdoor 指攻击者植入的恶意条件后门，不是模型水印、版权保护或所有权验证。后门式水印相关工作见 [独立专题](../content-authenticity/backdoor-based-watermarking-and-ownership.md)。

### 现实隐蔽性与机制复测

### 1. Rethinking the Stealthiness of Cryptographically Undetectable Backdoors in Practical RFF Learning

🌐 [Project](https://doi.org/10.1145/3770855.3817768)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`cryptographic backdoor`、`random Fourier feature`、`stealth evaluation`

- 🎯 **研究动机**：基于 CLWE 困难性的密码学不可检测后门只保证参数空间白盒隐蔽性，其在实际 RFF 学习流水线中的隐蔽性未被检验
- 🔬 **研究方法**：理论上证明其运行有效性依赖与现实部署不相容的假设，并在表格与图像数据上实验验证
- 📌 **结论**：标准数据预处理会破坏输入空间隐蔽性并留下明显伪影，简单的输入级 sanity check 即可可靠识别后门输入；另给出 RFF 的认证鲁棒性分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Random Fourier Features (RFF) learning is a classical technique in scalable data mining. However, at FOCS 2022, Goldwasser et al. proposed a theoretical framework for planting cryptographically undetectable backdoors in RFF learning based on the hardness of the Continuous Learning With Errors (CLWE) problem. Their construction guarantees white-box undetectability in the model parameter space against any polynomial-time distinguisher. In this paper, we revisit the undetectability of CLWE backdoors from a practical RFF learning perspective. We prove that the operational validity of the CLWE backdoor critically hinges on assumptions that are incompatible with the realistic RFF learning deployment. Specifically, standard data preprocessing required for effective RFF learning fundamentally destroys the input-space stealthiness of CLWE backdoors, inevitably resulting in conspicuous input-level artifacts. We further validate our theoretical findings through extensive experiments on both tabular and image datasets, demonstrating that simple sanity checks at the input level suffice to reliably identify backdoored inputs. In addition, under the same threat model, we analyze the adversarial robustness of RFF learning models and provide a concrete certified robustness analysis, enabling a deeper security assessment of its practical deployment. Overall, our work emphasizes the importance of evaluating theoretical backdoor attacks under realistic machine learning pipelines and offers broader insights into the secure deployment of RFF learning systems.

</details>
### 检测与缓解

### 2. Silencing the Poison: An Unsupervised Granular Ball Defense Approach in Local Smoothing Context for Recommender Systems

🌐 [Project](https://doi.org/10.1145/3770855.3817740)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`recommender poisoning`、`unsupervised detection`、`local smoothing`

- 🎯 **研究动机**：推荐系统投毒缺无监督防御手段
- 🔬 **研究方法**：在局部平滑上下文中用granular ball无监督隔离毒样本
- 📌 **结论**：免标签即可削弱投毒攻击效果