#!/usr/bin/env python3
"""
GitHub AI项目发现器
每天自动发现GitHub上的AI相关项目
"""

import requests
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time
from ai_analyzer import AIProjectAnalyzer

class GitHubAIProjectFinder:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-AI-Project-Finder"
        }
        self.output_dir = "ai_projects"
        self.analyzer = AIProjectAnalyzer()
        os.makedirs(self.output_dir, exist_ok=True)

    def search_repositories(self, query, sort="stars", order="desc", per_page=10):
        """搜索GitHub仓库"""
        url = f"{self.base_url}/search/repositories"
        params = {
            "q": query,
            "sort": sort,
            "order": order,
            "per_page": per_page
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 403:
                print("API速率限制，等待60秒后重试...")
                time.sleep(60)
                response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"搜索失败: {e}")
            return None

    def get_new_ai_projects(self, days=1):
        """获取新发布的AI项目"""
        # 计算日期范围
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # 构建查询
        query = f"ai created:{start_date.strftime('%Y-%m-%d')}..{end_date.strftime('%Y-%m-%d')}"
        print(f"搜索新发布的AI项目 (过去{days}天)...")

        return self.search_repositories(query, sort="stars", order="desc", per_page=10)

    def get_popular_ai_projects(self, min_stars=100):
        """获取热门AI项目"""
        query = f"ai stars:>={min_stars} pushed:>={datetime.now() - timedelta(days=30)}"
        print(f"搜索热门AI项目 (星标>={min_stars})...")

        return self.search_repositories(query, sort="stars", order="desc", per_page=10)

    def get_ai_domain_projects(self, domain):
        """获取特定AI领域的项目"""
        query = f"{domain} ai stars:>10"
        print(f"搜索{domain}领域的AI项目...")

        return self.search_repositories(query, sort="stars", order="desc", per_page=10)

    def get_ai_tools_libraries(self):
        """获取AI工具和库"""
        query = "ai tool OR library OR framework stars:>50"
        print("搜索AI工具和库...")

        return self.search_repositories(query, sort="stars", order="desc", per_page=10)

    def format_project(self, repo):
        """格式化项目信息"""
        return {
            "name": repo.get("name", ""),
            "full_name": repo.get("full_name", ""),
            "description": repo.get("description", ""),
            "html_url": repo.get("html_url", ""),
            "stars": repo.get("stargazers_count", 0),
            "forks": repo.get("forks_count", 0),
            "language": repo.get("language", ""),
            "created_at": repo.get("created_at", ""),
            "updated_at": repo.get("updated_at", ""),
            "topics": repo.get("topics", []),
            "license": repo.get("license", {}).get("name", "") if repo.get("license") else ""
        }

    def save_results(self, results, filename):
        """保存结果到文件"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"结果已保存到: {filepath}")
        return filepath

    def print_results(self, results, category):
        """在终端显示结果"""
        print(f"\n{'='*60}")
        print(f"[类别] {category}")
        print(f"{'='*60}")

        if not results or "items" not in results:
            print("未找到相关项目")
            return []

        projects = []
        for repo in results["items"]:
            project = self.format_project(repo)
            projects.append(project)

            print(f"\n[项目] {project['name']}")
            print(f"   描述: {project['description'] or '无描述'}")
            print(f"   链接: {project['html_url']}")
            print(f"   星标: {project['stars']} | 分支: {project['forks']} | 语言: {project['language'] or '未知'}")
            if project['topics']:
                print(f"   标签: {', '.join(project['topics'][:5])}")

        return projects

    def generate_report(self, all_results, enable_ai=True):
        """生成每日报告"""
        timestamp = datetime.now().strftime("%Y%m%d")
        report = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": timestamp,
            "categories": {}
        }

        for category, results in all_results.items():
            if results and "items" in results:
                projects = []
                for repo in results["items"]:
                    projects.append(self.format_project(repo))
                report["categories"][category] = projects

        # AI分析
        if enable_ai:
            print("\n[AI分析] 开始AI分析...")
            report = self.analyzer.generate_analysis_report(report)

        # 保存报告
        report_filename = f"ai_projects_report_{timestamp}.json"
        self.save_results(report, report_filename)

        # 生成Markdown报告
        md_filename = f"ai_projects_report_{timestamp}.md"
        md_filepath = os.path.join(self.output_dir, md_filename)

        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(f"# GitHub AI项目每日发现报告\n")
            f.write(f"日期: {report['date']}\n\n")

            for category, projects in report["categories"].items():
                f.write(f"## {category}\n\n")
                for project in projects:
                    f.write(f"### {project['name']}\n")
                    f.write(f"- 描述: {project['description'] or '无描述'}\n")
                    f.write(f"- 链接: {project['html_url']}\n")
                    f.write(f"- ⭐ {project['stars']} | 🍴 {project['forks']} | 语言: {project['language'] or '未知'}\n")
                    if project['topics']:
                        f.write(f"- 标签: {', '.join(project['topics'][:5])}\n")
                    # AI分析结果
                    if project.get('ai_analysis', {}).get('analyzed'):
                        f.write(f"\n**AI分析：**\n")
                        f.write(f"{project['ai_analysis']['analysis']}\n")
                    f.write("\n")

        print(f"Markdown报告已保存到: {md_filepath}")
        return report

    def generate_html_email(self, report):
        """生成HTML格式的邮件内容"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        .project {{ background: #f8f9fa; border-left: 4px solid #3498db; padding: 15px; margin: 15px 0; border-radius: 4px; }}
        .project-name {{ font-size: 18px; font-weight: bold; color: #2980b9; }}
        .project-desc {{ color: #555; margin: 8px 0; }}
        .project-meta {{ font-size: 14px; color: #777; }}
        .project-link {{ color: #3498db; text-decoration: none; }}
        .project-link:hover {{ text-decoration: underline; }}
        .stats {{ display: inline-block; margin-right: 15px; }}
        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; font-size: 12px; color: #999; }}
    </style>
</head>
<body>
    <h1>GitHub AI项目每日发现报告</h1>
    <p><strong>日期:</strong> {report['date']}</p>
"""
        total_projects = 0
        for category, projects in report["categories"].items():
            html += f"    <h2>{category} ({len(projects)}个项目)</h2>\n"
            for project in projects:
                total_projects += 1
                topics_html = ""
                if project['topics']:
                    topics_html = f"<br><span class='project-meta'>标签: {', '.join(project['topics'][:5])}</span>"
                html += f"""
    <div class="project">
        <div class="project-name">{project['name']}</div>
        <div class="project-desc">{project['description'] or '无描述'}</div>
        <div class="project-meta">
            <span class="stats">⭐ {project['stars']}</span>
            <span class="stats">🍴 {project['forks']}</span>
            <span class="stats">语言: {project['language'] or '未知'}</span>
            {topics_html}
        </div>
        <a href="{project['html_url']}" class="project-link">查看项目 →</a>
    </div>
"""
        html += f"""
    <div class="footer">
        <p>共发现 {total_projects} 个项目 | 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>GitHub AI项目每日发现器</p>
    </div>
</body>
</html>
"""
        return html

    def send_email(self, report, smtp_config):
        """发送邮件"""
        if not smtp_config.get("enabled"):
            print("[邮件] 邮件发送未启用，跳过")
            return False

        try:
            # 创建邮件
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"GitHub AI项目每日发现 - {report['date']}"
            msg["From"] = smtp_config["sender"]
            msg["To"] = smtp_config["recipient"]

            # 添加HTML内容
            html_content = self.generate_html_email(report)
            msg.attach(MIMEText(html_content, "html", "utf-8"))

            # 连接SMTP服务器并发送
            print(f"[邮件] 正在连接SMTP服务器 {smtp_config['server']}:{smtp_config['port']}...")
            with smtplib.SMTP(smtp_config["server"], smtp_config["port"]) as server:
                server.starttls()
                server.login(smtp_config["username"], smtp_config["password"])
                server.send_message(msg)
                print(f"[邮件] 邮件已发送至 {smtp_config['recipient']}")
                return True

        except Exception as e:
            print(f"[邮件] 发送失败: {e}")
            return False

    def run(self, send_email=False):
        """运行发现器"""
        print("[开始] 发现GitHub AI项目...")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        all_results = {}

        # 1. 新发布的AI项目
        all_results["新发布的AI项目"] = self.get_new_ai_projects(days=1)
        time.sleep(5)  # 增加等待时间避免API限制

        # 2. 热门AI项目
        all_results["热门AI项目"] = self.get_popular_ai_projects(min_stars=100)
        time.sleep(5)

        # 3. 特定AI领域项目
        ai_domains = ["machine learning", "deep learning", "nlp", "computer vision"]
        for domain in ai_domains:
            all_results[f"{domain.title()}项目"] = self.get_ai_domain_projects(domain)
            time.sleep(5)

        # 4. AI工具和库
        all_results["AI工具和库"] = self.get_ai_tools_libraries()

        # 生成报告
        print("\n[报告] 生成报告...")
        report = self.generate_report(all_results)

        print(f"\n[完成] 共发现 {sum(len(v.get('items', [])) if v else 0 for v in all_results.values())} 个项目")
        print(f"文件保存在: {os.path.abspath(self.output_dir)}")

        # 发送邮件
        if send_email:
            smtp_config = {
                "enabled": os.environ.get("SMTP_ENABLED", "false").lower() == "true",
                "server": os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
                "port": int(os.environ.get("SMTP_PORT", "587")),
                "username": os.environ.get("SMTP_USERNAME", ""),
                "password": os.environ.get("SMTP_PASSWORD", ""),
                "sender": os.environ.get("SMTP_SENDER", ""),
                "recipient": os.environ.get("SMTP_RECIPIENT", "")
            }
            self.send_email(report, smtp_config)

        return report

if __name__ == "__main__":
    import sys
    send_email = "--email" in sys.argv
    finder = GitHubAIProjectFinder()
    finder.run(send_email=send_email)