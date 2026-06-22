# GitHub AI项目每日发现器

每天自动从GitHub上发现AI相关项目，包括：
- 新发布的AI项目
- 热门AI项目
- 特定AI领域项目（机器学习、深度学习、NLP、计算机视觉）
- AI工具和库

## 功能特点

- 自动搜索GitHub API
- 生成JSON和Markdown两种格式的报告
- 通过GitHub Actions每天自动运行
- 结果自动提交到仓库

## 本地使用

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行脚本

```bash
python github_ai_projects.py
```

### 查看结果

报告将保存在 `ai_projects` 目录下：
- `ai_projects_report_YYYYMMDD.json` - JSON格式报告
- `ai_projects_report_YYYYMMDD.md` - Markdown格式报告

## 自动化

项目使用GitHub Actions进行自动化：
- 每天北京时间早上9点（UTC 01:00）自动运行
- 可以手动触发工作流
- 结果自动提交到仓库

## 自定义

你可以修改 `github_ai_projects.py` 中的以下参数：
- `min_stars` - 热门项目的最低星标数
- `ai_domains` - 要搜索的AI领域列表
- `per_page` - 每个类别返回的项目数量

## 许可证

MIT License