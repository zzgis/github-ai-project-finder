#!/usr/bin/env python3
"""
GitHub AI项目发现器
每天自动发现GitHub上的AI相关项目
"""

import requests
import json
import os
from datetime import datetime, timedelta
import time

class GitHubAIProjectFinder:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-AI-Project-Finder"
        }
        self.output_dir = "ai_projects"
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

    def generate_report(self, all_results):
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
                    f.write("\n")

        print(f"Markdown报告已保存到: {md_filepath}")
        return report

    def run(self):
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

        return report

if __name__ == "__main__":
    finder = GitHubAIProjectFinder()
    finder.run()