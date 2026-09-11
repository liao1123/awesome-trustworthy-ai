# Reader data inputs

`arxiv_metadata.json` 缓存 arXiv 元数据（标题、作者、摘要、分类、提交日期、comments），按 arXiv ID 键控；`official_metadata.json` 缓存官方 proceedings/出版商页面的摘要与作者（按 URL 键控）；`supplemental_metadata.json` 是 DOI/PDF 兜底记录（无作者）。

`daily/`、`domains/` 和 `conferences/` 的卡片 Markdown 是论文收录、标题、链接、小节和阅读笔记的唯一来源。`website/reader/build.py` 只解析 Markdown 生成 `papers.js`；这些缓存由 `tools/` 下的整理管道（`collect_index.py` → `join_metadata.py` → `fetch_missing.py` → `join_official.py`）在批量补全作者/摘要时使用，不回写 Markdown。

`papers.js` 是生成的浏览器数据，由 `python3 website/reader/build.py` 重建；tsrigo 预构建部署模式下它**直接提交进仓库**（`tools/deploy_site.sh` 负责构建与暂存）。
