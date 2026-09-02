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
6. 核对论文标题、arXiv ID、主要分类、提交日期和 arXiv 链接。不要把 arXiv 论文写成已经被某会议录用。
7. 记录 arXiv abstract 页面或官方 Atom 元数据中的 `Comments` 原文，字段名统一写作 `arXiv Comments`；不得总结、翻译或改写，官方未提供时写“未提供”。
8. 核对作者姓名及其单位。优先查看论文 PDF 首页或作者提供的正式信息；无法确认时写“单位未核实”，不能根据邮箱域名、作者过往单位或其他间接线索推测。
9. 查找作者或论文明确提供的代码仓库链接。没有找到可核实的代码时写“暂未找到公开代码”，不能用无关仓库代替。
10. 每篇论文标题下首先写一个独立的中文自然段，以 `**内容概述：**` 开头，并压缩为一句话，依次交代“研究动机或前人缺口 → 作者做了什么、提出什么方法或构建什么 benchmark → 最关键结果或失效边界”，形成便于快速理解论文内容的精简版摘要。该段不加列表符号，不照抄原始 abstract，也不与“收录理由”重复；不得添加论文没有声称的结论。
11. 内容概述之后立即写“收录理由”，明确说明该论文对应的安全对象、threat model、干预或评测价值；再写链接、arXiv 元数据、作者单位和原始摘要等其他信息。
12. 为每篇论文记录英文摘要和中文摘要。英文摘要直接使用 arXiv abstract 原文，不总结、不删减、不改写；中文摘要对该 abstract 作完整、忠实的逐句翻译，不总结、不省略，也不添加论文没有声称的内容。
13. 检查本月已有日报，使用 arXiv ID 去重。
14. 将结果写入 daily/YYYY-MM/YYYY-MM-DD.md；目录不存在时创建目录。即使当天没有合格论文，也创建日报并写明检索范围和“今日无收录”。
15. 当用户明确把当天筛选结果中的部分论文归类到 `domains/` 后，在日报的 `检索信息` 和 `论文列表` 之间增加 `## 已归类论文（全文）`，完整保留这些论文的内容概述、收录理由、链接、arXiv 元数据、作者单位和中英文摘要；这些条目从下方 `论文列表` 移出，但保留原日报编号，避免重复和编号失效。未归类论文继续留在 `论文列表`。
16. 只修改本次日报，不创建数据库、脚本或额外索引；日报完成后不得自动把全部论文同步到 `domains/`，等待用户逐篇精选或明确指定同步范围。

日报必须使用下面的格式：

# YYYY-MM-DD arXiv AI Safety Daily

## 检索信息

- 检索日期：YYYY-MM-DD
- arXiv 范围：写明检查的分类、列表或时间边界
- 候选论文：N 篇
- 最终收录：N 篇
- 今日概括：用一两句话概括主要方向；没有合格论文时写“今日无收录”

## 已归类论文（全文）

仅在当天已有明确的 domain 归类结果时出现。按原日报编号列出完整论文条目；一篇论文只在本节或下方 `论文列表` 出现一次。

### 原编号. Original Paper Title

按下方论文条目格式完整记录，不重新编号。

## 论文列表

日报不使用表格。每篇论文按照下面的形式依次列出：

### 1. Original Paper Title

**内容概述：** 用一句话依次概括研究动机或前人缺口、作者提出的方法或 benchmark，以及最关键结果或失效边界。

- 收录理由：说明它为什么与 Trustworthy AI 或 AI Safety 直接相关。
- 论文/arXiv：[Original Paper Title](https://arxiv.org/abs/XXXX.XXXXX)
- arXiv ID：`XXXX.XXXXX`
- 代码：[Code](代码链接)；没有时写“暂未找到公开代码”
- arXiv 分类：`cs.AI`、`cs.LG`
- 提交日期：YYYY-MM-DD
- arXiv Comments：arXiv 官方 Comments 原文；没有时写“未提供”
- 作者及单位：
  - Author A — Institution A
  - Author B — Institution B；Institution C
- 英文摘要：arXiv abstract 原文。
- 中文摘要：arXiv abstract 原文的完整中文翻译。

下一篇通常继续使用 `### 2.`、`### 3.` 编号；如果部分论文已移动到“已归类论文（全文）”，则沿用它们在原日报中的编号，允许普通列表出现编号空档。一篇论文只在日报中列出一次；编号顺序体现上述优先级，高优先级论文排在前面。
```
