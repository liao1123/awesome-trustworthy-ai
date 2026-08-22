# 每日论文汇总

这个目录保存每天从 arXiv 收集到的 Trustworthy AI 与 AI Safety 论文。

运行 Prompt 前先读取 [Repository Style Guide](../STYLE_GUIDE.md)。

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
2. 检索当天新发布或当天进入相关列表、且与 Trustworthy AI 或 AI Safety 直接相关的论文。
3. 必须阅读每篇候选论文的标题和摘要后再判断是否收录。只出现 safety、trust 或 robust 等关键词，但研究内容不直接相关的论文不要收录。
4. 核对论文标题、arXiv ID、主要分类、提交日期和 arXiv 链接。不要把 arXiv 论文写成已经被某会议录用。
5. 核对作者姓名及其单位。优先查看论文 PDF 首页或作者提供的正式信息；无法确认时写“单位未核实”，不能推测。
6. 查找作者或论文明确提供的代码仓库链接。没有找到可核实的代码时写“暂未找到公开代码”，不能用无关仓库代替。
7. 为每篇论文记录英文摘要和中文摘要。英文摘要直接使用 arXiv abstract 原文，不总结、不删减、不改写；中文摘要对该 abstract 作完整、忠实的逐句翻译，不总结、不省略，也不添加论文没有声称的内容。
8. 检查本月已有日报，使用 arXiv ID 去重。
9. 将结果写入 daily/YYYY-MM/YYYY-MM-DD.md；目录不存在时创建目录。即使当天没有合格论文，也创建日报并写明检索范围和“今日无收录”。
10. 只修改本次日报，不创建数据库、脚本或额外索引。

日报必须使用下面的格式：

# YYYY-MM-DD arXiv AI Safety Daily

## 检索信息

- 检索日期：YYYY-MM-DD
- arXiv 范围：写明检查的分类、列表或时间边界
- 候选论文：N 篇
- 最终收录：N 篇
- 今日概括：用一两句话概括主要方向；没有合格论文时写“今日无收录”

## 论文列表

日报不使用表格。每篇论文按照下面的形式依次列出：

### 1. Original Paper Title

- 论文/arXiv：[Original Paper Title](https://arxiv.org/abs/XXXX.XXXXX)
- arXiv ID：`XXXX.XXXXX`
- 代码：[Code](代码链接)；没有时写“暂未找到公开代码”
- arXiv 分类：`cs.AI`、`cs.LG`
- 提交日期：YYYY-MM-DD
- 作者及单位：
  - Author A — Institution A
  - Author B — Institution B；Institution C
- 英文摘要：arXiv abstract 原文。
- 中文摘要：arXiv abstract 原文的完整中文翻译。
- 收录理由：说明它为什么与 Trustworthy AI 或 AI Safety 直接相关。

下一篇继续使用 `### 2.`、`### 3.` 编号。一篇论文只在日报中列出一次。
```
