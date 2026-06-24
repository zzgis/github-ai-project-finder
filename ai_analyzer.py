#!/usr/bin/env python3
"""
AI项目分析器
使用大模型分析GitHub项目的核心功能和适用场景
"""

import requests
import json
import os
from typing import Optional

class AIProjectAnalyzer:
    def __init__(self):
        self.api_endpoint = os.environ.get("AI_API_ENDPOINT", "")
        self.api_key = os.environ.get("AI_API_KEY", "")
        self.model = os.environ.get("AI_MODEL", "agnes-2.0-flash")

    def _call_api(self, prompt: str, max_tokens: int = 1000) -> Optional[str]:
        """调用AI API"""
        if not self.api_key or not self.api_endpoint:
            print("[AI分析] 未配置API Key或Endpoint，跳过分析")
            return None

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个技术分析师，专门分析GitHub项目的功能和适用场景。请用中文回答，格式清晰。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": max_tokens,
            "temperature": 0.7
        }

        try:
            response = requests.post(
                f"{self.api_endpoint}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"[AI分析] API调用失败: {e}")
            return None

    def analyze_project(self, project: dict) -> dict:
        """分析单个项目"""
        name = project.get("name", "")
        description = project.get("description", "")
        topics = project.get("topics", [])
        language = project.get("language", "")
        stars = project.get("stars", 0)

        prompt = f"""请分析以下GitHub项目，并将所有内容翻译成中文：

项目名称：{name}
项目描述：{description}
编程语言：{language}
星标数：{stars}
标签：{', '.join(topics) if topics else '无'}

请提供（全部使用中文回答）：
1. **中文简介**（将项目描述翻译成流畅的中文，2-3句话）
2. **核心功能**（3-5个要点）
3. **适用场景**（2-4个具体使用场景）
4. **技术亮点**（如有）

请简洁明了地回答，每个要点用一句话概括。"""

        analysis = self._call_api(prompt)

        if analysis:
            return {
                "analyzed": True,
                "analysis": analysis
            }
        return {
            "analyzed": False,
            "analysis": "分析失败或未配置API"
        }

    def batch_analyze(self, projects: list, max_analyze: int = 10) -> list:
        """批量分析项目"""
        analyzed_projects = []
        total = min(len(projects), max_analyze)

        print(f"[AI分析] 开始分析 {total} 个项目...")

        for i, project in enumerate(projects[:total]):
            print(f"[AI分析] ({i+1}/{total}) 分析 {project.get('name', '未知')}...")
            result = self.analyze_project(project)
            project["ai_analysis"] = result
            analyzed_projects.append(project)

        # 剩余项目不分析
        analyzed_projects.extend(projects[total:])

        return analyzed_projects

    def generate_analysis_report(self, report: dict) -> dict:
        """为整个报告添加AI分析"""
        if not self.api_key:
            print("[AI分析] 未配置AI_API_KEY，跳过AI分析")
            return report

        for category, projects in report.get("categories", {}).items():
            if projects:
                report["categories"][category] = self.batch_analyze(projects, max_analyze=5)

        return report


if __name__ == "__main__":
    # 测试分析器
    analyzer = AIProjectAnalyzer()
    test_project = {
        "name": "test-project",
        "description": "A machine learning framework for deep learning",
        "topics": ["ml", "deep-learning", "python"],
        "language": "Python",
        "stars": 1000
    }
    result = analyzer.analyze_project(test_project)
    print(json.dumps(result, ensure_ascii=False, indent=2))
