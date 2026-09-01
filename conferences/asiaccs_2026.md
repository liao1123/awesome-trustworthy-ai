# AsiaCCS 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [智能体、推理链与生成式软件安全](#智能体推理链与生成式软件安全)
- [模型抽取与生成资产窃取](#模型抽取与生成资产窃取)
- [投毒、后门与对抗机器学习](#投毒后门与对抗机器学习)
- [隐私泄漏、隐蔽信道与自动分析器攻击](#隐私泄漏隐蔽信道与自动分析器攻击)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | The 21st ACM ASIA Conference on Computer and Communications Security (ACM ASIACCS 2026 / AsiaCCS 2026) |
| 举办时间与地点 | 2026-06-01 至 2026-06-05；Bangalore, India |
| 官方网站 | [AsiaCCS 2026](https://asiaccs2026.cse.iitkgp.ac.in/) |
| 官方录用列表 | [Cycle 1 Papers](https://asiaccs2026.cse.iitkgp.ac.in/cycle-1-papers/) · [Cycle 2 Papers](https://asiaccs2026.cse.iitkgp.ac.in/cycle-2-papers/) |
| 正式论文集 | [Proceedings](https://doi.org/10.1145/3779208) |
| 检查范围 | 官网 Cycle 1 与 Cycle 2 的全部 120 篇正式研究论文；单独列出的 18 篇 poster 不计入分母或正文；数据截至 2026-08-30 |

## 关键节点

投稿与 rebuttal 的 AoE 标记按官网原样保留；未标 AoE 的节点不自行补充时区。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Cycle 1 paper submission | 2025-08-25 23:59 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 early rejection | 2025-10-01 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 rebuttal | 2025-10-27 至 2025-10-30 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 notification | 2025-11-19 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 1 camera-ready | 2025-12-17 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 paper submission | 2025-12-12 23:59 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 early rejection / major revision | 2026-01-21 / 2026-02-10 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 rebuttal | 2026-02-16 至 2026-02-19 AoE | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 notification | 2026-03-10 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Cycle 2 camera-ready | 2026-04-07 | [Important Dates](https://asiaccs2026.cse.iitkgp.ac.in/important-dates/) |
| Conference | 2026-06-01 至 2026-06-05 | [AsiaCCS 2026](https://asiaccs2026.cse.iitkgp.ac.in/) |

## 筛选说明

- 官方论文总数：120；该数字由 Cycle 1 与 Cycle 2 官方录用页合并去重，并与正式 proceedings 中排除 18 篇 `POSTER:` 记录后的研究论文数交叉复算。
- 初筛候选：38；完整扫描标题后，对 agent、LLM、prompt、model extraction、split learning、backdoor、poisoning、adversarial、gradient inversion、covert channel 与 AI analyzer attack 等方向宽筛，再阅读摘要或正文判断安全问题是否为核心贡献。
- 最终收录：15。
- 收录口径：保留直接攻击、评测或防御 AI 模型、LLM agent、协同学习系统及 AI 驱动分析器的论文，也保留明确把生成模型用作新型恶意能力放大器的工作；每篇只进入最匹配的一个分表。
- 边界案例：`Taming Data Challenges in ML-based Security Tasks Using Generative AI`、`RESTing-LLAMA`、漏洞检测和恶意软件检测等主要是“AI for security”，不因使用 LLM 而收录；一般差分隐私、加密聚合、SecureAFL 和隐私计算只提供常规保密机制，没有具体 AI 攻击或安全失效，亦从严排除。
- Poster 边界：`SecAlign`、`SniffLlama`、`Phantom Force` 等 poster 可能直接相关，但官网将其与两轮正式论文分列，故不混入本页 120 篇研究论文的筛选结果。
- 链接规则：`Official` 指向正式 DOI；arXiv 只补充公开正文。作者与顺序以正式 proceedings 为准，因此个别 arXiv 版本中的作者拼写、增减或次序不覆盖会议版本。

## 论文分类

### 智能体、推理链与生成式软件安全

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| ATAG: AI-Agent Application Threat Assessment with Attack Graphs | Parth Atulbhai Gandhi, David Tayouri, Akansha Shukla, Beni Ifland, Yuval Elovici, Rami Puzis, Asaf Shabtai | [Official](https://doi.org/10.1145/3779208.3785380) · [arXiv](https://arxiv.org/abs/2506.02859) | 暂未公开 | framework、multi-agent security、attack graph、threat prioritization | ATAG 扩展 MulVAL 和 LLM 漏洞数据库来表示多 agent 拓扑，生成涵盖提示注入、过度权限、信息泄露与不安全输出处理的多步攻击路径。 |
| Mind the Web: The Security of Web Use Agents | Avishag Shapira, Parth Atulbhai Gandhi, Idan Habler, Asaf Shabtai | [Official](https://doi.org/10.1145/3779208.3805968) · [arXiv](https://arxiv.org/abs/2506.07153) | 暂未公开 | attack、web-use agent、indirect prompt injection、privilege abuse | 论文把恶意指令嵌入 agent 正常浏览的评论、广告等网页内容，展示任务对齐式间接提示注入可引发文件与密码泄露、冒充、摄像头调用和拒绝服务。 |
| Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models | Zhiyuan Xu, Joseph Gardiner, Sana Belguith | [Official](https://doi.org/10.1145/3779208.3785271) | 暂未公开 | analysis、chain-of-thought safety、harmful fine-tuning、hidden leakage | 论文发现对齐 CoT 模型即使最终拒答，中间推理仍可能泄露更有害且可执行的内容，并以“无意泄漏”和“有害升级”刻画微调放大的两类失效。 |
| Shape-Shifting Malicious Code in Software Backdoors via Language Models | Mohammad Ebrahimi Fard, Felix Weissberg, Erik Imgrund, Thorsten Eisenhofer, Konrad Rieck | [Official](https://doi.org/10.1145/3779208.3807485) · [Paper](https://eisenhofer.me/data/fard-26-shape.pdf) | [Code](https://github.com/mlsec-group/animagus) | attack、LLM misuse、software backdoor、supply-chain evasion | 论文用 LLM 把恶意载荷编码进自然可信的文档或配置文件，再由不依赖 LLM 的微型解码器恢复代码，暴露软件供应链审计的新盲点。 |
| VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces | Artem Grigor, Christian Schroeder de Witt, Simon Birnbach, Ivan Martinovic | [Official](https://doi.org/10.1145/3779208.3786259) · [arXiv](https://arxiv.org/abs/2512.15892) | [Code](https://github.com/ElusAegis/vet-your-agent) | defense、agent integrity、verifiable execution trace、host tampering | VET 用 Agent Identity Document 组合可信硬件、简洁证明和 TLS 公证，验证 agent 输出确由声明模型和配置产生，降低宿主篡改模型、输入或结果的风险。 |

### 模型抽取与生成资产窃取

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| BarkBeetle: Stealing Decision Tree Models with Fault Injection | Qifan Wang, Jonas Sander, Minmin Jiang, Thomas Eisenbarth, David Oswald | [Official](https://doi.org/10.1145/3779208.3785372) · [arXiv](https://arxiv.org/abs/2507.06986) | 暂未公开 | attack、decision tree extraction、fault injection、structural recovery | BarkBeetle 对决策树节点定向注入电压故障并自底向上恢复特征分裂和阈值，实机原型表明硬件故障可显著降低模型抽取所需查询。 |
| Prompt Pirates Need a Map: Stealing Seeds helps Stealing Prompts | Felix Mächtle, Ashwath Shetty, Jonas Sander, Nils Loose, Sören Pirk, Thomas Eisenbarth | [Official](https://doi.org/10.1145/3779208.3807483) · [arXiv](https://arxiv.org/abs/2509.09488) | [Code](https://github.com/UzL-ITS/Prompt-Pirate) | attack、diffusion model、seed recovery、prompt stealing | 论文利用常见图像框架的有限 seed 空间先恢复初始噪声，再用遗传搜索窃取生成提示，说明随机种子泄漏会直接削弱创作资产保密性。 |

### 投毒、后门与对抗机器学习

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Deep Learning Backdoor Defense via Adaptive Trigger Collisions in Latent Space | Zixun Xiong, Hao Wang, Jian Li, Yang Hua, Miao Pan, Xiaojiang Du | [Official](https://doi.org/10.1145/3779208.3806081) | 暂未公开 | defense、DNN backdoor、latent collision、post-processing | ATClean 在多层潜在空间生成只需产生特征碰撞的对抗样本并微调受污染表示，无需精确复原原触发器即可净化后门模型。 |
| GradSent: Temporal Consistency-based Defense for U-Shaped Split Learning | Deependra Singh, Avinash Awasthi, Pritam Vediya, Ramesh Babu Battula | [Official](https://doi.org/10.1145/3779208.3805965) | 暂未公开 | defense、split learning、client backdoor、temporal consistency | GradSent 不再把 non-IID 客户端横向比较为离群点，而是用梯度自编码器学习各自的良性时间轨迹，从而过滤客户端后门更新并减少误杀。 |
| Noise, Why Can't You Bend? Detecting Adversarial Perturbations in Wireless Sensing via Structural Fragility | Md Hasan Shahriar, Ning Wang, Amit Kumar Sikder, Naren Ramakrishnan, Y. Thomas Hou, Wenjing Lou | [Official](https://doi.org/10.1145/3779208.3806083) | 暂未公开 | detection、wireless sensing、adversarial perturbation、structural fragility | 论文利用恶意扰动相较自然传感噪声更难保持信号结构这一差异，检测无线感知模型输入中的对抗样本。 |
| Purified Distillation Slimming (PDS) for Robust Backdoor Defense | Liqun Shan, Kaiying Han, Yazhou Tu, Insup Lee, Xiali Hei | [Official](https://doi.org/10.1145/3779208.3785283) | 暂未公开 | defense、DNN backdoor、purified distillation、model slimming | PDS 将后门净化与知识蒸馏、模型 slimming 联合起来，在移除触发行为时保留干净任务知识并降低部署开销。 |
| “What is the Problem Space?” Defining Host-space Adversarial Perturbations against Network Intrusion Detection Systems | Miel Verkerken, Laurens D'hooge, Bruno Volckaert, Filip De Turck, Giovanni Apruzzese | [Official](https://doi.org/10.1145/3779208.3807482) · [arXiv](https://arxiv.org/abs/2605.25822) | 暂未公开 | analysis、ML-NIDS、host-space attack、realizability | 论文指出大量 ML-NIDS 对抗评测直接修改攻击者无法控制的特征或流量记录，并用主机侧真实命令变化展示可实现扰动可绕过检测。 |

### 隐私泄漏、隐蔽信道与自动分析器攻击

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Mitigating Gradient Inversion Risks in Language Models via Token Obfuscation | Xinguo Feng, Zhongkui Ma, Zihan Wang, Alsharif Abuadbba, Guangdong Bai | [Official](https://doi.org/10.1145/3779208.3785389) · [arXiv](https://arxiv.org/abs/2602.15897) | [Code](https://github.com/Trusted-System-Lab/GHOST) | defense、language model privacy、gradient inversion、token obfuscation | GHOST 以语义不同但嵌入邻近的 shadow token 训练语言模型，切断梯度、嵌入与原 token 的可逆联系，同时尽量保持下游效用。 |
| The Insider's Advantage: Exploiting Automated Privacy Policy Analyzer Tools Through Subtle Text Manipulations | Tanusree Das Tithy, Poojitha Thota, Shirin Nilizadeh, Faysal Hossain Shezan | [Official](https://doi.org/10.1145/3779208.3807480) | 暂未公开 | attack、privacy policy analyzer、adversarial text、compliance evasion | APATRA 以对人类阅读影响很小的政策文本改动误导 LLM 驱动分析器并隐藏关键数据实践，暴露自动合规审查可被内部人定向规避。 |
| Unequal Privacy: Auditing Demographic Bias Vulnerabilities in Visual Protection Systems | Seyyed Mohammad Sadegh Moosavi Khorzooghi, Poojitha Thota, Mohit Singhal, Abolfazl Asudeh, Gautam Das, Shirin Nilizadeh | [Official](https://doi.org/10.1145/3779208.3785292) | 暂未公开 | audit、visual privacy、demographic disparity、face obfuscation | FairDeFace 联合多种数据、识别器、攻击者和混淆方法审计人脸保护系统，发现不同人口群体获得的抗识别隐私保证并不均等。 |

## 核验记录

- 核验日期：2026-08-30。
- 录用状态：以官网 [Cycle 1](https://asiaccs2026.cse.iitkgp.ac.in/cycle-1-papers/) 与 [Cycle 2](https://asiaccs2026.cse.iitkgp.ac.in/cycle-2-papers/) 列表证明正式录用，再用 proceedings DOI 核对题目、作者和链接；poster 使用官网独立页面，未混入研究论文。
- 范围复算：两轮正式论文合计 120；正式 proceedings 另含 18 篇标题以 `POSTER:` 开头的记录，排除后也得到 120。
- 逐篇核验：已对 38 个宽筛候选检查摘要或正文，按当前兴趣边界最终保留 15 篇；四个分表依次收录 5、2、5、3 篇，合计无重复。
- 作者版本：表内作者顺序采用正式 proceedings；`Mind the Web` 与 `ATAG` 等公开预印本和会议版本存在作者或拼写差异，已保留会议版本并仅将 arXiv 作为补充链接。
- 分类与排序：每篇只有一个默认会议归属；各表按英文标题字母序排列，弯引号标题按核心词 `What` 排在 W 位置。
- 代码链接：只列论文、作者主页或仓库说明可直接回证的 artifact；其余即使存在同名 GitHub 结果也不收录。
- 领域同步：按当前研究兴趣从 15 篇中精选 9 篇；复用既有条目 0 条，新增 9 条，6 篇因传统硬件、ML-NIDS 或兴趣优先级未同步；默认主归属重复数为 0。
- 本页核验完成后，才会依据仓库当前研究兴趣把选中的论文去重同步到 `domains/`。
- 未决项：PDS 等若干论文未定位到可公开回证的代码或预印本；不影响正式录用与内容判断。
