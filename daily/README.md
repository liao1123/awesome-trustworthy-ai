# 每日论文汇总

这个目录保存每天从 arXiv 收集到的 Trustworthy AI 与 AI Safety 论文。

运行 Prompt 前先读取 [AI Safety 研究兴趣范围](../RESEARCH_INTERESTS.md) 和 [Repository Style Guide](../STYLE_GUIDE.md)。

## 存放方式

按照 `年-月/年-月-日.md` 保存。例如：

```text
daily/
├── README.md
├── 2026-08/
│   ├── 2026-08-21.md
│   └── 2026-08-22.md
└── 2026-09/
    └── 2026-09-01.md
```

## Codex Prompt

```text
请完成今天的 arXiv AI Safety 论文收集。

执行要求：
1. 使用 Asia/Hong_Kong 的当前日期，并以 arXiv 官方 new/recent 页面和论文 abstract 页面为主要来源。
2. 检索当天新发布或当天进入相关列表、且属于 `RESEARCH_INTERESTS.md` 当前关注范围的论文。
3. 必须阅读每篇候选论文的标题和摘要后再判断是否收录。只出现 safety、trust 或 robust 等关键词，但研究内容不直接相关的论文不要收录。
4. 以 `RESEARCH_INTERESTS.md` 为完整且优先的兴趣边界。核心兴趣正常收录；有条件主题必须满足对应安全条件；明确排除项不收录。尤其不要收录一般可解释性、普通 Agent reliability、泛治理或伦理、环境可持续性、电子/数字/移动设备/数据库取证、云平台与传统身份认证安全（AWS/Azure/GCP、Zero Trust、IAM、MFA、credential/session anomaly）、传统 phishing 生成/检测/用户实验与安全培训、非对抗性的自动驾驶/机器人传感器退化、融合鲁棒性与 LiDAR 感知预算研究、传统 UAV／车辆／机器人导航估计和低层控制攻击或安全增强（如 GPS/GNSS spoofing、惯性／声学传感器注入、estimator–controller coupling、flight controller、classical CBF／reachability／trajectory planner）、芯片／封装／板级设备／边缘 accelerator 的物理漏洞与资产提取（如光学或激光 probing、硬件 side channel、物理 fault injection）、任何以 graph learning／GNN／hypergraph neural network／graph foundation model／其他图核心学习、建模、推理或优化方法，或 federated learning 为直接对象或内部方法的工作、一般 privacy-preserving learning/inference、data minimization、最小披露，以及 Differential Privacy、密码学、secure inference、homomorphic encryption、MPC、zero-knowledge proof、数字签名、区块链或 TEE 研究。直接攻击或保护 VLA、world model、LLM Agent、learned AI decision module 或 prompt/control-input authority 的工作仍按其独立 AI 安全贡献判断；数据抽取、记忆泄漏、反演、去匿名化和软件可见的模型／服务侧信道攻击及其针对性审计或缓解也按安全贡献判断，但不得恢复图学习或联邦学习工作；不依赖物理芯片访问的模型层 bit flip、MoE routing 或参数篡改攻击不受硬件排除项影响。普通 knowledge graph、GraphRAG、scene graph、attack graph 或 dependency DAG 仅作为非学习型数据结构、且图方法不是研究贡献时不自动排除。
5. 对所有合格论文按照 `RESEARCH_INTERESTS.md` 的“手动精选与优先排序偏好”排序，不机械沿用 arXiv 列表顺序。与用户此前明确精选论文相似、具有具体 threat model、技术机制、机制证据和强安全评测的论文排在前面；其他仍符合边界的论文继续保留在后面。排序不改变收录边界。完成当日检索时不需要为此递归读取 `domains/`，以 `RESEARCH_INTERESTS.md` 中记录的优先级画像为准。
6. 核对论文标题、arXiv ID、提交日期和 arXiv 链接，并从 abstract 页面或 Atom 元数据记录作者列表（`First Last` 格式）。不要把 arXiv 论文写成已经被某会议录用。
7. 查找论文明确提供的代码、模型、数据集或 project page 链接；没有找到时不写对应链接，不能用无关仓库代替。论文声明确有 OpenReview forum 时加 📝 链接。
8. 每篇论文按 `STYLE_GUIDE.md` 的卡片格式记录：标题、图标链接行（含 📅 日期徽章）、关键词、作者、三段式总结（🎯 研究动机 / 🔬 研究方法 / 📌 结论）、`<details>` 折叠的英文摘要。三段式总结是论文 Introduction 的高度浓缩，一针见血，可多于一句；不翻译摘要、不写空话。
9. 英文摘要保留 arXiv abstract 原文，不总结、不删减、不改写。
10. 检查本月已有日报，使用 arXiv ID 去重。
11. 将结果写入 daily/YYYY-MM/YYYY-MM-DD.md；目录不存在时创建目录。即使当天没有合格论文，也创建日报并写明检索范围和“今日无收录”。
12. 当用户明确把当天筛选结果中的部分论文归类到 `domains/` 后，在日报的 `检索信息` 和 `论文列表` 之间增加 `## 已归类论文（全文）`，完整保留这些论文的卡片条目并沿用原日报编号；未归类论文继续留在 `论文列表`。
13. 只修改本次日报，不创建数据库、脚本或额外索引；日报完成后不得自动把全部论文同步到 `domains/`，等待用户逐篇精选或明确指定同步范围。

日报必须使用下面的格式：

# YYYY-MM-DD arXiv AI Safety Daily

## 检索信息

- 检索日期：YYYY-MM-DD
- arXiv 范围：写明检查的分类、列表或时间边界
- 候选论文：N 篇
- 最终收录：N 篇
- 今日概括：用一两句话概括主要方向；没有合格论文时写“今日无收录”

## 已归类论文（全文）

仅在当天已有明确的 domain 归类结果时出现。按原日报编号列出完整卡片条目；一篇论文只在本节或下方 `论文列表` 出现一次。

### 原编号. Original Paper Title

按卡片格式完整记录，不重新编号。

## 论文列表

每篇论文按 `STYLE_GUIDE.md` 卡片格式依次列出：

### 1. Original Paper Title

📄 [arXiv](https://arxiv.org/abs/XXXX.XXXXX) · 🐙 [Code](…)　📅 YYYY-MM

**关键词**：`attack`、`specific risk`、`method`、`evaluation`

👤 **作者**：First Last、First Last

- 🎯 **研究动机**：……
- 🔬 **研究方法**：……
- 📌 **结论**：……

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

arXiv abstract 原文。

</details>

下一篇继续使用 `### 2.`、`### 3.` 编号；如果部分论文已移动到“已归类论文（全文）”，则沿用它们在原日报中的编号，允许普通列表出现编号空档。一篇论文只在日报中列出一次；编号顺序体现上述优先级，高优先级论文排在前面。
```
