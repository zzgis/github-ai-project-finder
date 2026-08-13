# GitHub AI项目每日发现报告
日期: 2026-08-13

## 新发布的AI项目

### tokentab
- 

## tokentab 项目分析

### 1. 中文简介
tokentab 是一个命令行工具，用于读取 Claude Code、Codex 和 Gemini CLI 的会话日志，并按模型、项目和日期统计各会话的 Token 消耗成本。

### 2. 核心功能
- 支持解析 Claude Code、Codex 和 Gemini CLI 的会话日志文件
- 按模型、项目和日期维度统计 Token 使用量和费用
- 提供命令行界面，方便快速查询和汇总成本数据
- 帮助用户清晰了解各 AI 工具的实际支出情况

### 3. 适用场景
- 个人开发者追踪多个 AI 编程助手的月度花费
- 团队管理者核算不同项目使用 Claude/Codex/Gemini 的成本分布
- 预算控制场景下，按日或按项目监控 AI API 费用
- 对比不同 AI 模型在同一项目中的性价比

### 4. 技术亮点
- 统一接口支持多个主流 AI CLI 工具的日志解析
- 多维度成本统计（模型、项目、日期）便于精细化分析
- Python 实现，轻量易用，适合日常命令行快速查询
- 链接: https://github.com/wzchav/tokentab
- ⭐ 131 | 🍴 12 | 语言: Python
- 标签: ai, api, claude, claude-code, claude-tool

### grok-register
- 

## Grok-Register 项目分析

### 1. 中文简介
这是一个专为 x.ai（Grok）平台设计的自动化账户注册工具包，支持 SSO 提取、OAuth 设备流程以及自动补充守护进程功能，可批量管理账户注册流程。

### 2. 核心功能
- **自动化注册**：支持批量自动创建 x.ai/Grok 账户
- **SSO 提取**：自动提取单点登录凭证信息
- **OAuth 设备流程**：通过 OAuth Device Flow 完成身份验证
- **自动补充守护进程**：后台持续监控并自动补充账户资源

### 3. 适用场景
- 需要批量注册 Grok 账户的研究或测试场景
- 自动化账户管理工具链的集成需求
- 对 Grok API 访问额度有持续需求的开发者

### 4. 技术亮点
- 采用 Python 实现，代码结构简洁易扩展
- 集成 OAuth Device Flow 实现无头浏览器自动化认证
- 内置守护进程机制实现账户资源的自动 replenish（补充）

---

> ⚠️ **提示**：此类自动化注册工具可能违反目标平台的服务条款，使用前请谨慎评估合规风险。
- 链接: https://github.com/xinxinshuhao-create/grok-register
- ⭐ 123 | 🍴 38 | 语言: Python

### mcp-memory
- 

# MCP Memory 项目分析

## 1. 中文简介
这是一个由 OKF 支持的 Model Context Protocol (MCP) 服务器，为 AI 智能体提供持久化的长期记忆存储和基于 SQLite FTS5 的全文搜索功能。它使 AI 代理能够在多次交互中保持上下文记忆，并通过高效的搜索能力快速检索历史信息。

## 2. 核心功能
- **持久化长期记忆**：为 AI 智能体提供跨会话的持久化记忆存储能力
- **SQLite FTS5 全文搜索**：利用 SQLite 的 FTS5 引擎实现高效的内容检索
- **MCP 协议支持**：遵循 Model Context Protocol 标准，易于集成到现有 AI 工作流
- **Python 实现**：基于 Python 开发，便于部署和二次开发

## 3. 适用场景
- **AI 对话助手**：让聊天机器人记住用户偏好和历史对话内容
- **智能体工作流**：为多步骤 AI 代理提供跨任务的知识积累
- **知识库检索**：通过全文搜索快速定位历史交互中的重要信息
- **个性化服务**：基于用户历史数据提供定制化的 AI 响应

## 4. 技术亮点
- 使用 SQLite FTS5 提供高性能全文搜索，无需额外依赖数据库服务
- 轻量级设计，仅依赖 Python 标准库和 SQLite，部署简单
- MCP 协议标准化接口，可无缝接入支持 MCP 的 AI 框架（如 Claude Desktop、Cursor 等）
- 持久化存储确保 AI 智能体在重启后仍能保留历史记忆
- 链接: https://github.com/fellowgeek/mcp-memory
- ⭐ 96 | 🍴 2 | 语言: Python

### repo-context-mcp
- 

## repo-context-mcp 项目分析

### 1. 中文简介
repo-context-mcp 是一个基于 Model Context Protocol (MCP) 的服务器，专为 AI 编程助手提供代码仓库地图、代码搜索和智能上下文打包功能，帮助 AI 代理更高效地理解和操作代码库。

---

### 2. 核心功能
- **仓库地图生成**：自动构建代码仓库的结构地图，帮助 AI 快速了解项目全貌
- **代码搜索**：支持在仓库中高效检索代码片段和文件
- **Token 感知上下文打包**：智能管理上下文大小，根据 token 预算裁剪和打包关键代码
- **MCP 协议兼容**：原生支持 Model Context Protocol，可无缝对接主流 AI 编程工具
- **多工具支持**：兼容 Claude、Codex、Cursor 等 AI 编程助手

---

### 3. 适用场景
- 使用 Claude Code 或 Cursor 处理大型代码库时，需要 AI 理解整体项目结构
- 上下文窗口有限的 AI 代理需要智能筛选关键代码片段
- 多文件协作修改场景，需要 AI 获取相关代码的上下文信息
- 希望将 MCP 集成到现有 AI 编程工作流中，提升代码理解能力

---

### 4. 技术亮点
- 基于 TypeScript 构建，与 MCP 协议深度集成，扩展性好
- **Token 感知机制**：智能裁剪上下文，避免超出模型 token 限制，提升效率
- **开箱即用**：支持 Claude、Codex、Cursor 等主流工具，配置简单
- 专为 AI 编程代理设计，聚焦代码仓库上下文管理痛点
- 链接: https://github.com/nduc99911/repo-context-mcp
- ⭐ 89 | 🍴 80 | 语言: TypeScript
- 标签: ai-agent, claude, codex, cursor, mcp

### oss-pr-reviewer
- 

# GitHub 项目分析：oss-pr-reviewer

## 1. 中文简介

这是一个基于 AI 的命令行工具，专为 GitHub Pull Request 审查而设计。它能自动检测潜在 Bug、安全风险、回归问题及缺失测试，并为开源项目维护者生成结构化的 Markdown 报告。

## 2. 核心功能

- **AI 智能审查**：利用大语言模型自动分析 PR 代码变更
- **Bug 检测**：识别代码中可能存在的潜在缺陷和逻辑错误
- **安全风险扫描**：检测代码中的安全漏洞和潜在风险
- **回归问题检测**：发现可能导致功能退化的代码变更
- **测试覆盖分析**：检测缺失的测试用例并生成结构化 Markdown 报告

## 3. 适用场景

- **开源项目维护**：开源维护者快速审查社区提交的 PR
- **团队协作审查**：开发团队在合并代码前进行自动化代码审查
- **安全审计**：对 PR 进行安全层面的自动化扫描和风险评估
- **CI/CD 集成**：作为自动化流程的一部分，在 PR 提交时自动触发审查

## 4. 技术亮点

- 基于 LLM（大语言模型）实现智能代码分析，无需人工逐行审查
- CLI 工具形式，可轻松集成到现有工作流和 CI/CD 流水线中
- 输出结构化的 Markdown 报告，便于阅读和归档
- 支持多维度检测（Bug、安全、回归、测试），一站式覆盖代码审查关键需求
- 链接: https://github.com/vuphongle/oss-pr-reviewer
- ⭐ 82 | 🍴 78 | 语言: TypeScript
- 标签: ai, cli, code-review, developer-tools, github

### maintainer-autopilot
- 描述: Local-first, resumable AI maintenance pipelines with single-writer safety and deterministic verification.
- 链接: https://github.com/phungkaizen/maintainer-autopilot
- ⭐ 77 | 🍴 73 | 语言: JavaScript
- 标签: ai-agents, automation, cli, codex, developer-tools

### godmode
- 描述: Production-grade Agent Skills for AI coding agents—composable workflows for planning, TDD, debugging, review, UI/UX, releases, incidents, and evals.
- 链接: https://github.com/thiientv/godmode
- ⭐ 72 | 🍴 70 | 语言: Python
- 标签: agent-evaluation, agent-skills, ai-agents, ai-coding, claude-code

### eve-software-factory-template
- 描述: Meet Foreman, an eve Software Factory.
- 链接: https://github.com/vercel-labs/eve-software-factory-template
- ⭐ 63 | 🍴 4 | 语言: TypeScript
- 标签: agent, ai, eve, vercel

### aihostcheck
- 描述: Open-source cross-OS diagnostics for AI developer environments.
- 链接: https://github.com/raydthanh/aihostcheck
- ⭐ 43 | 🍴 40 | 语言: TypeScript

### QuillMesh
- 描述: A local-first Markdown editor for people and AI agents.
- 链接: https://github.com/lbiao2965-bot/QuillMesh
- ⭐ 43 | 🍴 2 | 语言: TypeScript

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP是一个综合性中文自然语言处理资源仓库，汇集了敏感词检测、信息抽取、情感分析、知识图谱构建、预训练模型及对话系统等丰富的NLP工具和资源。项目整合了BERT、ALBERT、GPT-2等主流预训练模型以及大量公开数据集和词库，是中文NLP领域的实用资源合集。

## 2. 核心功能
- **文本处理**：支持敏感词检测、繁简转换、分词、词性标注、命名实体识别和文本摘要
- **信息抽取**：提供手机号、身份证、邮箱抽取，关系抽取，实体链接和关键词提取
- **语言资源**：包含中日韩人名库、地名词库、成语库、医学/法律/汽车等领域词库及停用词表
- **预训练模型**：集成BERT、ALBERT、GPT-2、ELECTREA等中文预训练语言模型
- **对话系统**：支持聊天机器人、知识图谱问答和任务型对话系统构建

## 3. 适用场景
- NLP研究人员快速查找数据集、基准任务和复现方案
- 开发者构建内容审核、智能客服、问答系统等实际应用
- 学术研究者获取中文NLP最新模型、语料库和测评基准
- 企业用户进行文本分类、情感分析和信息抽取任务

## 4. 技术亮点
- 项目收录资源极为丰富，涵盖中文NLP从基础工具到前沿模型的完整生态链
- 整合了清华大学XLORE跨语言知识图谱、百度信息抽取系统等知名开源项目
- 包含语音识别、OCR文字识别、语音情感分析等多模态NLP资源
- 提供NLP竞赛TOP方案汇总和面试知识点，对学习和实战均有较高参考价值
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82451 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI 机器学习/深度学习项目合集

### 1. 中文简介
该项目是一个包含 500 个 AI 项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目以 Python 为主要开发语言，为学习者提供了丰富的实战案例和完整代码实现。

### 2. 核心功能
- 提供 500 个完整的 AI 项目代码，覆盖主流技术方向
- 包含机器学习、深度学习、计算机视觉、NLP 四大领域的实战案例
- 所有项目均附带可运行的 Python 代码，便于学习和复现
- 项目分类清晰，适合不同水平的学习者按需选择
- 标签体系完善，方便快速定位特定技术领域

### 3. 适用场景
- 机器学习/深度学习初学者系统学习与实战练习
- 需要寻找项目灵感的数据科学家和算法工程师
- 高校相关课程的教学案例与课后实践
- 技术面试准备，积累项目经验

### 4. 技术亮点
- 星标数高达 36215，是 GitHub 上最受欢迎的 AI 项目合集之一
- 涵盖当前最热门的技术方向：深度学习、计算机视觉、NLP
- 全部使用 Python 实现，生态成熟，社区资源丰富
- 项目数量庞大，可作为持续学习的资源库长期参考
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36215 | 🍴 7428 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化查看器，支持多种主流框架格式。它通过简洁直观的界面帮助用户理解模型结构，无需编写代码即可查看和调试模型。

### 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite、safetensors 等主流模型格式
- **交互式可视化**：提供清晰的层结构图，支持缩放、折叠和展开操作
- **跨平台运行**：基于 Electron 开发，支持 Windows、macOS 和 Linux
- **模型调试辅助**：可逐层检查网络结构，便于定位模型问题
- **开源免费**：完全开源，社区活跃，持续维护更新

### 3. 适用场景
- **模型开发调试**：研究人员和工程师快速查看模型结构，排查设计问题
- **模型格式转换验证**：在不同框架之间转换模型后，验证结构一致性
- **技术文档与演示**：将模型结构以可视化形式展示，便于团队沟通和文档编写
- **模型学习理解**：初学者通过可视化界面直观学习各类神经网络架构

### 4. 技术亮点
- 支持 safetensors 等新兴安全模型格式，紧跟技术趋势
- 无需安装 Python 环境即可运行，降低使用门槛
- 界面简洁美观，交互体验流畅，星标数超过 33,000，社区认可度高
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33345 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介

ONNX（Open Neural Network Exchange）是一个开放标准，旨在实现机器学习模型在不同框架间的互操作性。它允许开发者将模型从一种框架导出为ONNX格式，然后在支持ONNX的其他框架或运行时环境中运行。该项目由微软、Facebook等公司联合推动，已成为深度学习模型交换的行业标准之一。

### 2. 核心功能

- 提供统一的模型表示格式，支持跨框架模型迁移
- 支持主流深度学习框架（PyTorch、TensorFlow、Keras等）的模型导入导出
- 提供ONNX Runtime推理引擎，实现高性能跨平台推理
- 支持模型算子定义与转换，覆盖常见神经网络结构
- 提供模型优化工具链，支持量化、剪枝等压缩技术

### 3. 适用场景

- 将PyTorch训练好的模型部署到TensorFlow或ONNX Runtime环境中
- 在移动端或嵌入式设备上运行深度学习模型
- 跨云平台部署模型，实现框架无关的推理服务
- 模型性能优化与压缩，适配资源受限的设备

### 4. 技术亮点

- 由微软和Facebook等科技巨头联合主导，生态成熟度高
- 支持超过200种算子，覆盖绝大多数深度学习模型结构
- ONNX Runtime提供多平台、多硬件加速支持（CPU、GPU、NPU等）
- 社区活跃，Star数超过2万，拥有广泛的用户基础和工具链支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21307 | 🍴 3992 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

### 1. 中文简介

《机器学习工程开源手册》是一本全面覆盖机器学习工程实践的开源指南。内容涵盖从模型训练、调试到推理部署的全流程技术，适合希望深入掌握LLM工程化落地的开发者与工程师。

### 2. 核心功能

- 提供大规模语言模型（LLM）训练与微调的系统性方法论
- 深入讲解GPU集群配置、网络优化与存储管理
- 涵盖PyTorch与Transformers框架的实战技巧
- 介绍基于Slurm的分布式训练调度与弹性伸缩方案
- 提供模型推理优化与生产部署的最佳实践

### 3. 适用场景

- 大模型训练基础设施搭建与运维
- MLOps流水线设计与模型部署落地
- GPU集群性能调优与故障排查
- 从研究到生产的ML工程化转型

### 4. 技术亮点

- 以开源书籍形式系统梳理ML工程知识体系，内容持续更新
- 覆盖从底层硬件（GPU/网络/存储）到上层框架（PyTorch/Transformers）的完整技术栈
- 结合Slurm等工业级调度工具，提供可落地的生产环境解决方案
- 18608+星标表明其社区认可度高，是ML工程领域的热门参考资料
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18608 | 🍴 1199 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17357 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3374 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13258 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11626 | 🍴 913 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10690 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI 机器学习/深度学习项目合集

### 1. 中文简介
该项目是一个包含 500 个 AI 项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目以 Python 为主要开发语言，为学习者提供了丰富的实战案例和完整代码实现。

### 2. 核心功能
- 提供 500 个完整的 AI 项目代码，覆盖主流技术方向
- 包含机器学习、深度学习、计算机视觉、NLP 四大领域的实战案例
- 所有项目均附带可运行的 Python 代码，便于学习和复现
- 项目分类清晰，适合不同水平的学习者按需选择
- 标签体系完善，方便快速定位特定技术领域

### 3. 适用场景
- 机器学习/深度学习初学者系统学习与实战练习
- 需要寻找项目灵感的数据科学家和算法工程师
- 高校相关课程的教学案例与课后实践
- 技术面试准备，积累项目经验

### 4. 技术亮点
- 星标数高达 36215，是 GitHub 上最受欢迎的 AI 项目合集之一
- 涵盖当前最热门的技术方向：深度学习、计算机视觉、NLP
- 全部使用 Python 实现，生态成熟，社区资源丰富
- 项目数量庞大，可作为持续学习的资源库长期参考
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36215 | 🍴 7428 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化查看器，支持多种主流框架格式。它通过简洁直观的界面帮助用户理解模型结构，无需编写代码即可查看和调试模型。

### 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite、safetensors 等主流模型格式
- **交互式可视化**：提供清晰的层结构图，支持缩放、折叠和展开操作
- **跨平台运行**：基于 Electron 开发，支持 Windows、macOS 和 Linux
- **模型调试辅助**：可逐层检查网络结构，便于定位模型问题
- **开源免费**：完全开源，社区活跃，持续维护更新

### 3. 适用场景
- **模型开发调试**：研究人员和工程师快速查看模型结构，排查设计问题
- **模型格式转换验证**：在不同框架之间转换模型后，验证结构一致性
- **技术文档与演示**：将模型结构以可视化形式展示，便于团队沟通和文档编写
- **模型学习理解**：初学者通过可视化界面直观学习各类神经网络架构

### 4. 技术亮点
- 支持 safetensors 等新兴安全模型格式，紧跟技术趋势
- 无需安装 Python 环境即可运行，降低使用门槛
- 界面简洁美观，交互体验流畅，星标数超过 33,000，社区认可度高
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33345 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub项目分析：cheatsheets-ai

## 1. 中文简介
该项目为深度学习和机器学习研究者提供了一系列必备的速查表，涵盖从基础理论到实践工具的常用知识要点。内容参考了Medium博主Kailash Ahirwar的推荐清单，旨在帮助研究人员快速查阅关键概念和代码示例。

## 2. 核心功能
- 提供深度学习与机器学习核心概念的速查表
- 涵盖Keras、NumPy、SciPy、Matplotlib等常用工具的代码示例
- 整理人工智能领域的基础知识与实用技巧
- 以简洁的表格形式呈现，便于快速检索

## 3. 适用场景
- 深度学习初学者系统复习核心概念
- 研究人员在写论文或实现算法时快速查阅公式和参数
- 数据科学家日常使用NumPy、Matplotlib等库时作为参考手册
- 面试准备或知识巩固时的速查工具

## 4. 技术亮点
- 星标数超过15000，说明在社区中具有较高的实用价值和认可度
- 内容覆盖从理论到实践的全链路，整合了多个主流AI框架和科学计算库
- 以速查表形式呈现，结构清晰，适合快速查阅而非系统学习
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3374 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
这是一个全面的人工智能学习路线图项目，收录了近200个实战案例与项目，并提供免费的配套教材，适合零基础入门及就业实战。涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域。

### 2. 核心功能
- 提供系统化的AI学习路线图，从零开始逐步进阶
- 收录近200个实战案例与项目，注重动手能力培养
- 免费提供配套教材与学习资源，降低学习门槛
- 覆盖主流框架（PyTorch、TensorFlow、Keras等）与热门领域

### 3. 适用场景
- 零基础学员系统学习人工智能与数据科学
- 求职者通过实战项目提升就业竞争力
- 开发者快速掌握CV、NLP等热门方向的核心技能
- 培训机构或自学者的学习路线参考

### 4. 技术亮点
- 学习路径完整，覆盖从Python基础到深度学习的全链路
- 实战导向，包含大量可直接运行的项目案例
- 支持多框架（PyTorch / TensorFlow / Caffe / Keras），适配不同学习需求
- 免费开源，资源获取门槛低，社区活跃（13258+星标）
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13258 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它简化了深度学习模型的训练和部署流程，适合不同技术水平的开发者使用。

### 2. 核心功能
- 低代码/无代码界面，快速构建和训练深度学习模型
- 支持多种数据类型（文本、图像、表格、音频等）的处理
- 提供可视化训练过程和结果分析功能
- 支持主流深度学习框架（如 PyTorch）
- 内置自动超参数调优和模型评估功能

### 3. 适用场景
- 快速原型开发：无需深入编程即可构建和测试 AI 模型
- 数据科学项目：处理结构化与非结构化数据的综合分析
- 模型微调：针对特定任务对 LLM 进行微调优化
- 教育学习：深度学习入门者的实践工具

### 4. 技术亮点
- 支持多模态数据处理，涵盖 NLP、计算机视觉等领域
- 提供可解释的模型训练过程和结果可视化
- 兼容主流数据格式和深度学习框架
- 社区活跃，星标数超过 1.1 万，生态完善
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9169 | 🍴 1234 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8960 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1898 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6994 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6392 | 🍴 773 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP是一个综合性中文自然语言处理资源仓库，汇集了敏感词检测、信息抽取、情感分析、知识图谱构建、预训练模型及对话系统等丰富的NLP工具和资源。项目整合了BERT、ALBERT、GPT-2等主流预训练模型以及大量公开数据集和词库，是中文NLP领域的实用资源合集。

## 2. 核心功能
- **文本处理**：支持敏感词检测、繁简转换、分词、词性标注、命名实体识别和文本摘要
- **信息抽取**：提供手机号、身份证、邮箱抽取，关系抽取，实体链接和关键词提取
- **语言资源**：包含中日韩人名库、地名词库、成语库、医学/法律/汽车等领域词库及停用词表
- **预训练模型**：集成BERT、ALBERT、GPT-2、ELECTREA等中文预训练语言模型
- **对话系统**：支持聊天机器人、知识图谱问答和任务型对话系统构建

## 3. 适用场景
- NLP研究人员快速查找数据集、基准任务和复现方案
- 开发者构建内容审核、智能客服、问答系统等实际应用
- 学术研究者获取中文NLP最新模型、语料库和测评基准
- 企业用户进行文本分类、情感分析和信息抽取任务

## 4. 技术亮点
- 项目收录资源极为丰富，涵盖中文NLP从基础工具到前沿模型的完整生态链
- 整合了清华大学XLORE跨语言知识图谱、百度信息抽取系统等知名开源项目
- 包含语音识别、OCR文字识别、语音情感分析等多模态NLP资源
- 提供NLP竞赛TOP方案汇总和面试知识点，对学习和实战均有较高参考价值
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82451 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介

LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行微调，相关研究发表于 ACL 2024。该项目为研究人员和开发者提供了一个一站式解决方案，简化了大模型的微调流程。

## 2. 核心功能

- 支持 100+ 种主流大语言模型和视觉语言模型的统一微调
- 提供多种高效微调技术，包括 LoRA、QLoRA 和全参数微调
- 支持 RLHF（基于人类反馈的强化学习）对齐训练
- 内置多种量化方案，降低显存占用并提升推理效率
- 兼容 Hugging Face Transformers 生态，便于集成和扩展

## 3. 适用场景

- 研究者对 LLaMA、Qwen、DeepSeek、Gemma 等模型进行指令微调（Instruction Tuning）
- 开发者在显存受限环境下使用 QLoRA 等技术进行轻量化微调
- 需要对多模态模型（VLM）进行视觉-语言联合微调的场景
- 企业或个人希望快速部署 RLHF 对齐训练以提升模型输出质量

## 4. 技术亮点

- **统一架构**：一个框架支持上百种模型，无需为不同模型配置不同工具
- **高效微调**：原生支持 LoRA/QLoRA/PEFT，大幅降低训练资源需求
- **量化友好**：内置 4bit/8bit 量化支持，可在消费级显卡上运行
- **学术背书**：相关论文发表于 ACL 2024，具备较强的技术可信度
- **生态兼容**：深度集成 Hugging Face 体系，模型和数据格式无缝对接
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74067 | 🍴 9063 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
该项目是一套面向初学者的AI通识课程，为期12周、包含24节课程，致力于让所有人都能轻松学习人工智能。由微软开发者社区推出，内容涵盖机器学习、深度学习及自然语言处理等核心领域。

### 2. 核心功能
- 提供结构化的12周学习路径，适合零基础入门
- 基于Jupyter Notebook实现交互式编程教学
- 覆盖机器学习、深度学习、计算机视觉、NLP等主流AI方向
- 包含CNN、RNN、GAN等经典模型的实际案例
- 由微软官方维护，内容质量有保障

### 3. 适用场景
- 高校或培训机构用于AI通识课程教学
- 职场人士自学入门人工智能技术
- 对AI感兴趣的非技术背景人群科普学习
- 企业内训中作为AI基础知识培训材料

### 4. 技术亮点
- 采用微软For Beginners系列标准化课程框架，学习曲线平缓
- 64820颗星标表明该项目在社区中具有广泛影响力和高认可度
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 64820 | 🍴 12566 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# AI工程从零开始 (AI Engineering from Scratch)

## 1. 中文简介
这是一个全面的AI工程教程项目，旨在帮助学习者从零开始掌握AI技术的核心原理与实践。通过系统的课程和实战项目，帮助学习者理解、构建并部署AI应用，最终能够为他人提供指导。

## 2. 核心功能
- 涵盖AI全栈技术，包括大语言模型（LLM）、生成式AI、计算机视觉和自然语言处理
- 提供从零开始的系统化学习路径，适合不同基础的学习者
- 支持多种编程语言，包括Python、Rust和TypeScript
- 深入讲解AI代理（Agents）、MCP协议、群体智能等前沿技术
- 结合强化学习、Transformer架构等深度学习核心技术

## 3. 适用场景
- 希望系统学习AI工程技术的开发者或学生
- 需要从零构建AI应用原型的技术团队
- 想要深入理解LLM和生成式AI原理的研究人员
- 计划开发AI代理或智能体系统的工程师

## 4. 技术亮点
- 跨语言支持（Python + Rust + TypeScript），兼顾性能与开发效率
- 覆盖从基础机器学习到前沿生成式AI的完整技术栈
- 包含MCP（Model Context Protocol）等新兴AI工程协议
- 高人气项目（46,668星标），说明社区认可度较高
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46668 | 🍴 8140 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub项目分析：ailearning

### 1. 中文简介
该项目是一个全面的机器学习与深度学习实战学习资源库，涵盖数据分析、机器学习算法实战、线性代数基础，以及PyTorch、NLTK、TensorFlow 2等主流框架的应用。适合希望系统掌握AI相关技术的开发者与学习者。

### 2. 核心功能
- 提供完整的数据分析与机器学习算法实战代码（如逻辑回归、SVM、KMeans、AdaBoost等）
- 包含深度学习方法实战（DNN、RNN、LSTM）及PyTorch、TensorFlow 2框架应用
- 集成自然语言处理（NLP）实战内容，基于NLTK库进行文本处理
- 涵盖推荐系统、关联规则挖掘（Apriori、FP-Growth）等实用场景
- 补充线性代数等数学基础，帮助学习者夯实理论根基

### 3. 适用场景
- 机器学习入门学习者系统学习算法原理与代码实现
- 需要快速上手PyTorch/TensorFlow 2进行深度学习开发的工程师
- 从事NLP或推荐系统方向，寻找实战参考代码的研究人员
- 希望将线性代数等数学知识应用于AI实践的跨领域学习者

### 4. 技术亮点
- 技术栈覆盖全面：从传统机器学习（sklearn）到深度学习（PyTorch、TF2）再到NLP（NLTK），形成完整学习链路
- 标签丰富且分类清晰，便于针对性检索和学习
- 高星标数（42455）表明社区认可度高，代码质量与实用性经过广泛验证
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42455 | 🍴 11521 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36215 | 🍴 7428 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33816 | 🍴 4708 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29055 | 🍴 3536 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21837 | 🍴 3350 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17357 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI 机器学习/深度学习项目合集

### 1. 中文简介
该项目是一个包含 500 个 AI 项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目以 Python 为主要开发语言，为学习者提供了丰富的实战案例和完整代码实现。

### 2. 核心功能
- 提供 500 个完整的 AI 项目代码，覆盖主流技术方向
- 包含机器学习、深度学习、计算机视觉、NLP 四大领域的实战案例
- 所有项目均附带可运行的 Python 代码，便于学习和复现
- 项目分类清晰，适合不同水平的学习者按需选择
- 标签体系完善，方便快速定位特定技术领域

### 3. 适用场景
- 机器学习/深度学习初学者系统学习与实战练习
- 需要寻找项目灵感的数据科学家和算法工程师
- 高校相关课程的教学案例与课后实践
- 技术面试准备，积累项目经验

### 4. 技术亮点
- 星标数高达 36215，是 GitHub 上最受欢迎的 AI 项目合集之一
- 涵盖当前最热门的技术方向：深度学习、计算机视觉、NLP
- 全部使用 Python 实现，生态成熟，社区资源丰富
- 项目数量庞大，可作为持续学习的资源库长期参考
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36215 | 🍴 7428 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于人工智能的浏览器工作流自动化工具，能够利用大语言模型（LLM）和计算机视觉技术，自动执行各类基于浏览器的重复性任务。它通过 AI 驱动的方式替代传统 RPA 工具，以更智能的方式完成网页交互和数据处理流程。

### 2. 核心功能
- **AI 驱动浏览器自动化**：利用 LLM 理解网页内容并自主决策操作步骤
- **视觉感知能力**：通过计算机视觉技术识别页面元素和布局
- **多框架支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **API 接口**：提供标准化 API，便于集成到现有系统和工作流中
- **工作流编排**：支持复杂多步骤业务流程的自动化设计与执行

### 3. 适用场景
- **数据抓取与表单填写**：自动从网站提取数据或批量填写在线表单
- **RPA 流程替代**：替代传统规则型 RPA，处理非结构化网页操作
- **跨平台工作流自动化**：在多个网站间执行跨页面、跨标签的操作流程
- **定期任务自动化**：自动化执行需要定期访问网页的监控、报告生成等任务

### 4. 技术亮点
- 结合 **LLM 语义理解** 与 **视觉识别**，实现类人级别的网页交互能力
- 支持 **多浏览器引擎**，可根据场景灵活选择 Playwright/Puppeteer/Selenium
- 采用 **API 优先架构**，易于与企业现有系统集成，降低自动化部署门槛
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22744 | 🍴 2138 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，为视觉AI提供开源、云服务和企业级产品。它支持图像、视频和3D标注，具备AI辅助标注、质量保障、团队协作和开发者API等功能。

## 2. 核心功能
- **AI辅助标注**：利用人工智能自动识别和标注目标，大幅提升标注效率
- **多格式支持**：支持图像、视频和3D数据的标注任务
- **团队协作**：提供多人协作标注、任务分配和质量审核功能
- **质量保障**：内置质量保证机制，确保数据集标注精度
- **开发者API**：开放API接口，便于集成到现有工作流

## 3. 适用场景
- **自动驾驶数据集构建**：标注车辆、行人、交通标志等目标
- **医疗影像分析**：标注CT、MRI等医学图像中的病灶区域
- **安防监控分析**：标注视频中的异常行为和可疑目标
- **工业质检**：标注产品缺陷和瑕疵区域

## 4. 技术亮点
- 支持PyTorch和TensorFlow等主流深度学习框架的数据集格式
- 提供语义分割、目标检测、图像分类等多种标注类型
- 开源架构，可私有化部署，保障数据安全
- 16516星的高人气，说明社区认可度和成熟度较高
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16516 | 🍴 3801 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12953 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，基于 PyTorch 构建。它提供了一套可微分的计算机视觉算子和几何变换工具，支持图像处理和深度学习模型的无缝集成。

### 2. 核心功能
- **可微分几何变换**：提供旋转、平移、缩放等几何操作的可微分实现
- **图像处理算子**：包含滤波、边缘检测、形态学等经典图像处理功能
- **3D 视觉支持**：支持相机标定、投影、位姿估计等 3D 几何计算
- **PyTorch 原生集成**：所有算子直接基于 PyTorch 张量，可与神经网络无缝对接
- **自动微分引擎**：内置自动微分，支持端到端的梯度优化

### 3. 适用场景
- **机器人视觉导航**：用于机器人的视觉定位与路径规划
- **AR/VR 空间计算**：支持增强现实中的图像配准与三维重建
- **医学影像分析**：用于可微分的图像分割与配准任务
- **神经渲染**：支持可微分渲染管线与场景优化

### 4. 技术亮点
- 完全可微分的计算机视觉流水线，支持端到端训练
- 原生支持 GPU 加速，计算效率高
- 与 PyTorch 生态深度集成，API 设计简洁直观
- 开源活跃，社区贡献频繁，适合学术研究与企业应用
- 链接: https://github.com/kornia/kornia
- ⭐ 11316 | 🍴 1219 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8875 | 🍴 2189 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3478 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3364 | 🍴 411 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2632 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2504 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386185 | 🍴 81170 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 271693 | 🍴 24294 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
这是一个能够伴随用户共同成长的AI智能体。它支持多种大语言模型，可根据用户的使用习惯和反馈不断优化自身表现。

### 2. 核心功能
- 支持多种LLM提供商（Claude、GPT等）的集成调用
- 具备学习和适应能力，随使用持续进化
- 提供智能体自动化任务执行能力
- 兼容主流AI开发框架和工具链

### 3. 适用场景
- 开发者自动化编程辅助与代码审查
- 企业级AI代理工作流搭建
- 个人智能助手与任务自动化
- LLM应用开发与集成测试

### 4. 技术亮点
- 多模型兼容架构，支持Anthropic Claude、OpenAI GPT等主流模型切换
- 标签显示与Nous Research合作，可能集成了先进的开源模型优化技术
- 高星标数（23万+）表明社区认可度高、生态活跃
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 230061 | 🍴 45501 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200521 | 🍴 60119 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186590 | 🍴 46086 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167088 | 🍴 21566 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 166907 | 🍴 9375 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164509 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157768 | 🍴 46177 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153192 | 🍴 9854 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

