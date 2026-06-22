# 设置指南

## 将项目推送到GitHub

### 1. 在GitHub上创建新仓库

1. 访问 https://github.com/new
2. 仓库名称：`github-ai-project-finder`（或你喜欢的名称）
3. 描述：`每天自动发现GitHub上的AI相关项目`
4. 选择Public（推荐，这样GitHub Actions可以免费运行）
5. 不要初始化README、.gitignore或license（我们已经创建了）
6. 点击"Create repository"

### 2. 连接本地仓库到GitHub

在项目目录中运行以下命令（将 `YOUR_USERNAME` 和 `YOUR_REPO_NAME` 替换为你的信息）：

```bash
# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送到GitHub
git push -u origin main
```

### 3. 启用GitHub Actions

1. 推送代码后，访问你的GitHub仓库页面
2. 点击"Actions"标签页
3. 点击"I understand my workflows, go ahead and enable them"
4. 工作流将每天自动运行

### 4. 手动触发工作流（可选）

1. 访问仓库的"Actions"页面
2. 选择"每日AI项目发现"工作流
3. 点击"Run workflow"
4. 选择分支并点击"Run workflow"

## 查看结果

### 在GitHub上查看

每次工作流运行后，结果会自动提交到仓库。你可以：
1. 访问仓库的"Actions"页面查看运行历史
2. 在`ai_projects`目录下查看最新的报告

### 本地查看

```bash
# 拉取最新结果
git pull

# 查看报告
ls ai_projects/
cat ai_projects/ai_projects_report_$(date +%Y%m%d).md
```

## 自定义设置

### 修改运行时间

编辑 `.github/workflows/daily-ai-projects.yml` 中的cron表达式：

```yaml
schedule:
  # 每天北京时间早上9点运行 (UTC 01:00)
  - cron: '0 1 * * *'
```

cron表达式格式：`分 时 日 月 周`

### 修改搜索参数

编辑 `github_ai_projects.py` 中的以下参数：

```python
# 热门项目的最低星标数
min_stars = 100

# 要搜索的AI领域
ai_domains = ["machine learning", "deep learning", "nlp", "computer vision"]

# 每个类别返回的项目数量
per_page = 10
```

## 故障排除

### GitHub Actions没有运行

1. 确保仓库是Public（或你有GitHub Actions权限）
2. 检查工作流文件语法是否正确
3. 查看Actions页面的错误日志

### 脚本运行失败

1. 检查GitHub API限制（未认证请求限制为每小时60次）
2. 如果需要更高的限制，可以添加GitHub token

### 添加GitHub Token（可选）

1. 访问 https://github.com/settings/tokens
2. 生成新的personal access token
3. 在仓库的Settings → Secrets and variables → Actions中添加：
   - Name: `GITHUB_TOKEN`
   - Secret: 你的token
4. 修改脚本使用token：

```python
self.headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHub-AI-Project-Finder",
    "Authorization": f"token {os.environ.get('GITHUB_TOKEN', '')}"
}
```