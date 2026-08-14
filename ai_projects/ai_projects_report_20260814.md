# GitHub AI项目每日发现报告
日期: 2026-08-14

## 新发布的AI项目

### agent-safe-pipeline
- 

## agent-safe-pipeline 项目分析

### 1. 中文简介

这是一个面向AI代理的安全参考架构，AI代理仅能提议操作，但无权自行授权。系统通过不可篡改的意图捕获、独立的策略裁决（允许/升级/阻止）、经核实的审批流程，以及消耗一次性授权令牌的SafeExecutor，实现安全的操作闭环。

---

### 2. 核心功能

- **意图不可篡改捕获**：AI代理的操作提议以不可变形式记录，确保意图可追溯。
- **独立策略裁决**：通过Decionis引擎对操作进行ALLOW（允许）、ESCALATE（升级）或BLOCK（阻止）的独立判定。
- **人工审批验证**：关键操作需经人类验证批准后方可执行。
- **一次性授权执行**：SafeExecutor仅能消耗单次绑定的意图授权，防止授权复用。
- **策略即代码**：权限规则以代码形式定义，支持版本控制和审计。

---

### 3. 适用场景

- **高风险AI操作**：如金融交易、医疗决策等需要严格人工把关的场景。
- **企业级AI治理**：需要统一权限管理和操作审计的大型组织。
- **合规性要求严格的领域**：如受监管行业（金融、医疗、政府）的AI应用。
- **人机协作流水线**：AI提议、人类审核、安全执行的自动化工作流。

---

### 4. 技术亮点

- 采用**不可变意图设计**，从架构层面杜绝操作篡改风险。
- 集成**MCP（Model Context Protocol）**，支持标准化上下文交互。
- 实现**策略即代码（Policy as Code）**，便于审计和版本管理。
- 设计为**参考架构**，可直接作为安全AI代理系统的开发模板。
- 链接: https://github.com/decionis/agent-safe-pipeline
- ⭐ 221 | 🍴 2 | 语言: TypeScript
- 标签: agentic-ai, ai-agent-permissions, ai-agents, ai-governance, ai-safety

### modex-mh-agent
- 

## 项目分析：modex-mh-agent

### 1. 中文简介
Modex MH Agent 是一款 AI 全自动数学建模智能体，能够覆盖科研全流程，从赛题解析到竞赛级论文生成均可在一夜之间完成。该项目支持全国大学生数学建模竞赛、美赛（MCM/ICM）以及华为杯等多种数学建模赛事。

### 2. 核心功能
- 全自动数学建模：从赛题理解到模型构建全流程自动化
- 竞赛级论文生成：一夜之间输出符合竞赛标准的完整论文
- 多赛事覆盖：支持国赛、美赛、华为杯等主流数学建模竞赛
- 科研全流程辅助：兼顾从问题解析到结果呈现的完整科研链条
- 架构可视化展示：提供系统架构的展示说明

### 3. 适用场景
- 数学建模竞赛备赛：学生团队快速完成赛题分析与论文撰写
- 科研论文辅助：研究人员快速构建模型并生成结构化论文
- 算法竞赛训练：用于数学建模能力训练与实战演练
- 企业数据分析：华为杯等商业分析类赛题的智能求解

### 4. 技术亮点
- 全自动化流程设计，大幅降低数学建模门槛
- 支持多类型竞赛的适配与覆盖
- 以架构展示形式呈现系统设计思路
- 链接: https://github.com/N-allpass/modex-mh-agent
- ⭐ 179 | 🍴 0 | 语言: 未知

### mcp-memory
- 

## MCP-Memory 项目分析

### 1. 中文简介

mcp-memory 是一个基于 OKF 的 Model Context Protocol (MCP) 服务器，为 AI Agent 提供持久化的长期记忆存储和 SQLite FTS5 全文搜索能力。它解决了 AI Agent 缺乏跨会话记忆的核心痛点。

### 2. 核心功能

- **持久化记忆存储**：基于 OKF 框架实现跨会话的长期记忆保存
- **SQLite FTS5 全文搜索**：支持高效的语义检索和关键词匹配
- **MCP 协议兼容**：遵循 Model Context Protocol 标准，可无缝集成各类 AI Agent
- **Python 实现**：轻量级 Python 服务端，易于部署和二次开发

### 3. 适用场景

- **AI 助手记忆系统**：让 ChatGPT/Claude 等 AI 记住用户偏好和历史对话
- **多轮对话 Agent**：为对话式 Agent 提供跨会话上下文保持能力
- **知识检索增强**：结合 FTS5 搜索实现 RAG 式的记忆召回
- **个性化 AI 应用**：构建具有长期用户画像的智能应用

### 4. 技术亮点

- **FTS5 全文索引**：SQLite 原生支持，无需额外依赖即可实现毫秒级搜索
- **OKF 框架背书**：基于成熟的 OKF 架构，稳定性有保障
- **MCP 标准化**：遵循开放协议，可接入 Claude Desktop、Cursor 等主流 AI 工具
- **轻量级设计**：纯 Python + SQLite，部署成本极低

---

**总结**：这是一个解决 AI Agent "短期记忆"痛点的实用工具，适合需要持久化用户上下文的应用场景。128 星标表明社区关注度适中，技术方向正确但生态尚在早期。
- 链接: https://github.com/fellowgeek/mcp-memory
- ⭐ 128 | 🍴 2 | 语言: Python

### oss-pr-reviewer
- 

## oss-pr-reviewer 项目分析

### 1. 中文简介
这是一个基于 AI 的命令行工具，用于审查 GitHub Pull Request，能够自动检测潜在 Bug、安全风险、回归问题和缺失测试，并为开源维护者生成结构化的 Markdown 报告。

### 2. 核心功能
- **AI 驱动的代码审查**：利用大语言模型自动分析 PR 内容并生成审查报告
- **多维度问题检测**：识别潜在 Bug、安全漏洞、回归缺陷及缺失的测试用例
- **结构化 Markdown 报告**：输出格式规范的审查结果，便于开源维护者阅读和处理
- **CLI 命令行交互**：通过终端命令行即可使用，集成便捷

### 3. 适用场景
- **开源项目维护者**：快速审查社区贡献的 PR，提高代码合并效率
- **团队协作开发**：在小型团队中作为自动代码审查辅助工具
- **个人开发者**：对提交给开源社区的 PR 进行预审查，减少被拒风险

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态友好
- 整合 LLM（大语言模型）能力，提供智能化代码分析
- 专为开源维护者设计，输出格式贴合实际工作流需求
- 链接: https://github.com/vuphongle/oss-pr-reviewer
- ⭐ 96 | 🍴 92 | 语言: TypeScript
- 标签: ai, cli, code-review, developer-tools, github

### godmode
- 

## Godmode 项目分析

### 1. 中文简介

面向AI编码代理的生产级Agent技能库，提供可组合的工作流模块，覆盖规划、测试驱动开发、调试、代码审查、UI/UX设计、版本发布、事件处理和效果评估等全流程开发场景。

### 2. 核心功能

- **可组合工作流**：将开发流程拆分为独立技能模块，支持按需组合与复用
- **全生命周期覆盖**：涵盖从规划、TDD、调试到审查、发布、评估的完整开发链路
- **AI编码代理增强**：为Claude Code、Codex等主流AI编码工具提供专业级技能扩展
- **评估与测试驱动**：内置评估框架，支持测试驱动开发流程的自动化
- **生产级稳定性**：面向生产环境设计，确保可靠性和可维护性

### 3. 适用场景

- **AI辅助开发集成**：为AI编码代理添加专业开发技能，提升自动化编码能力
- **代码审查与质量保障**：通过标准化审查流程，提升团队协作效率
- **自动化测试与发布**：将TDD和发布流程自动化，减少人工干预
- **事件响应与复盘**：快速处理线上事件并生成评估报告，优化后续开发

### 4. 技术亮点

- **模块化架构**：采用可组合设计，各技能模块可独立使用或灵活拼装
- **多代理兼容**：支持Claude Code、Codex等多种主流AI编码代理平台
- **提示词工程优化**：基于Prompt Engineering技术，提升AI代理的任务执行质量
- **Python实现**：使用Python开发，便于扩展和二次定制
- 链接: https://github.com/thiientv/godmode
- ⭐ 89 | 🍴 87 | 语言: Python
- 标签: agent-evaluation, agent-skills, ai-agents, ai-coding, claude-code

### ai-interview-handbook-cn
- 描述: 大模型面试 144 问、Top Interview 150 导航与 Python 手撕代码模板
- 链接: https://github.com/Skyfacon/ai-interview-handbook-cn
- ⭐ 77 | 🍴 21 | 语言: 未知

### ai-agent-for-magento2
- 描述: 无描述
- 链接: https://github.com/duongdang942/ai-agent-for-magento2
- ⭐ 73 | 🍴 73 | 语言: PHP

### ai-super-model
- 描述: 无描述
- 链接: https://github.com/dungoutlook1/ai-super-model
- ⭐ 40 | 🍴 40 | 语言: Rust

### agentic-playwright
- 描述: Production-grade Playwright + TypeScript Scaffold for Agentic Testing. Harness for all major AI coding agents baked in.
- 链接: https://github.com/idavidov13/agentic-playwright
- ⭐ 33 | 🍴 17 | 语言: Python
- 标签: agentic, ai, api-testing, claude-code, cursor

### im-human
- 描述: 讓 AI 用台灣人的繁體中文講話，並把已寫好的文字清掉 AI 味。Claude Code、claude.ai、ChatGPT Codex 與一般聊天都能用。
- 链接: https://github.com/chang416/im-human
- ⭐ 30 | 🍴 5 | 语言: Python
- 标签: aiwriting, chatgpt, claude-skills, codex, prompt-engineering

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖敏感词检测、语言识别、实体抽取、情感分析等基础NLP功能，同时收录了大量中文词库、预训练模型、开源数据集及竞赛代码，是中文NLP开发与研究的综合性资源库。

## 2. 核心功能
- **基础NLP工具**：敏感词检测、繁简体转换、手机号/身份证/邮箱抽取、断句分词、语言检测等开箱即用功能
- **丰富词库资源**：中日文人名库、同义/反义词库、汽车品牌库、古诗词库、地名词库、医学/法律/财经等领域词库
- **预训练模型与深度学习**：BERT、ALBERT、GPT-2等中文预训练模型，命名实体识别、文本分类、关系抽取等任务代码
- **数据集与基准评测**：中文NLP竞赛数据集、问答数据集、谣言数据库、对话机器人语料及中文语言理解测评基准
- **语音与生成任务**：ASR语音识别、语音情感分析、中文聊天机器人、文本摘要生成、自动对联等生成式NLP工具

## 3. 适用场景
- **企业内容审核系统**：快速集成敏感词过滤、情感分析、实体抽取，适用于舆情监控与内容安全
- **中文智能客服/对话机器人**：利用开源对话系统、知识图谱问答、多轮对话资源快速搭建客服机器人
- **学术研究与模型对比实验**：提供标准化数据集、预训练模型和竞赛TOP方案，方便研究者进行基准测试
- **知识图谱构建**：整合命名实体识别、关系抽取、实体链接等工具，助力垂直领域知识图谱建设

## 4. 技术亮点
- 收录清华XLORE跨语言百科知识图谱、百度开源信息抽取系统等
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82458 | 🍴 15270 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36231 | 🍴 7429 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具，能够直观展示模型结构和参数。它支持多种主流深度学习框架的模型格式，帮助用户快速理解和分析模型架构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 提供直观的图形化界面展示神经网络层结构和连接关系
- 支持查看模型权重、参数和张量维度信息
- 提供模型推理调试和错误排查功能
- 支持导出模型结构图为图片或PDF格式

### 3. 适用场景
- 深度学习模型开发与调试：帮助开发者理解模型结构，定位网络层问题
- 模型格式转换验证：确认不同框架间模型转换后的结构一致性
- 学术论文与报告展示：生成清晰的模型架构图用于论文插图或技术分享
- 模型部署前审查：在将模型部署到移动端或嵌入式设备前检查模型完整性

### 4. 技术亮点
- 支持 safetensors 等新兴模型格式，紧跟技术发展趋势
- 开源免费，社区活跃，星标数超过 33000
- 提供桌面应用和在线版本，使用便捷
- 对模型结构进行层次化展示，支持折叠/展开操作，便于分析大型网络
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33349 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同框架（如PyTorch、TensorFlow、Keras等）之间无缝迁移和部署模型。

### 2. 核心功能
- 提供统一的模型表示格式，支持跨框架模型转换
- 兼容主流深度学习框架，包括PyTorch、TensorFlow、Keras、scikit-learn等
- 支持模型的序列化与反序列化，便于存储和传输
- 提供ONNX Runtime推理引擎，优化模型执行效率
- 支持模型算子的定义与扩展，覆盖常见神经网络结构

### 3. 适用场景
- 将PyTorch训练的模型转换为ONNX格式后在TensorFlow环境中部署
- 在移动端或嵌入式设备上使用ONNX Runtime进行高效推理
- 跨平台模型共享与协作，避免框架锁定
- 模型性能优化与加速，通过算子融合和硬件适配提升推理速度

### 4. 技术亮点
- 由Microsoft、Facebook等科技巨头联合推动，社区生态成熟
- 支持动态形状（Dynamic Shapes），灵活处理不同输入尺寸
- 提供丰富的算子库（Operator Set），覆盖CNN、RNN、Transformer等主流架构
- 与ONNX Simplifier、ONNX-Sklearn等工具链集成，简化模型转换流程
- 链接: https://github.com/onnx/onnx
- ⭐ 21310 | 🍴 3994 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# ml-engineering 项目分析

## 1. 中文简介
《机器学习工程开放手册》是一本全面的机器学习工程实践指南，涵盖从模型训练到推理部署的完整技术栈。该项目以开源形式整理，为工程师提供可落地的工程化解决方案和最佳实践。

## 2. 核心功能
- 提供大规模模型训练和推理的工程化指南
- 涵盖GPU集群配置、网络优化和存储管理
- 包含Slurm调度系统和PyTorch分布式训练实践
- 针对LLM（大语言模型）的调试与性能优化
- 集成MLOps全流程，支持模型可扩展性部署

## 3. 适用场景
- 大规模LLM模型训练与推理的工程部署
- GPU集群管理和分布式训练环境搭建
- MLOps流水线设计与生产环境优化
- 机器学习系统的性能调试与故障排查

## 4. 技术亮点
- 聚焦实际工程问题，内容覆盖从开发到生产的全链路
- 针对主流技术栈（PyTorch、Transformers）提供深度实践指导
- 结合Slurm等集群调度系统，适合超大规模训练场景
- 开源社区驱动，持续更新工程实践案例
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18615 | 🍴 1199 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17356 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13260 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11628 | 🍴 913 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10689 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36231 | 🍴 7429 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具，能够直观展示模型结构和参数。它支持多种主流深度学习框架的模型格式，帮助用户快速理解和分析模型架构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 提供直观的图形化界面展示神经网络层结构和连接关系
- 支持查看模型权重、参数和张量维度信息
- 提供模型推理调试和错误排查功能
- 支持导出模型结构图为图片或PDF格式

### 3. 适用场景
- 深度学习模型开发与调试：帮助开发者理解模型结构，定位网络层问题
- 模型格式转换验证：确认不同框架间模型转换后的结构一致性
- 学术论文与报告展示：生成清晰的模型架构图用于论文插图或技术分享
- 模型部署前审查：在将模型部署到移动端或嵌入式设备前检查模型完整性

### 4. 技术亮点
- 支持 safetensors 等新兴模型格式，紧跟技术发展趋势
- 开源免费，社区活跃，星标数超过 33000
- 提供桌面应用和在线版本，使用便捷
- 对模型结构进行层次化展示，支持折叠/展开操作，便于分析大型网络
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33349 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## 项目分析：cheatsheets-ai

### 1. 中文简介
这是一个为深度学习和机器学习研究人员准备的必备速查表集合。项目通过简洁的备忘单形式，帮助研究者快速回顾核心概念、公式和代码用法。

### 2. 核心功能
- 提供深度学习核心概念的速查表，涵盖神经网络、反向传播、优化器等
- 提供机器学习基础知识的速查表，包括监督学习、无监督学习、模型评估等
- 集成常用Python库的API速查，如Keras、NumPy、SciPy、Matplotlib
- 以可视化图表和代码示例呈现，便于快速查阅和理解

### 3. 适用场景
- 深度学习/机器学习研究人员快速回顾基础知识
- 面试准备时查阅核心概念和公式
- 日常开发中快速查找库函数用法
- 初学者系统学习AI核心知识体系

### 4. 技术亮点
- 覆盖主流深度学习框架（Keras）和数据科学库（NumPy、SciPy、Matplotlib）
- 以速查表形式呈现，内容精炼、一目了然
- 适合不同层次的研究者和开发者使用
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
这是一个系统化的人工智能学习路线图项目，整理了近200个实战案例与项目，并免费提供配套教材，帮助零基础学习者入门并实现就业实战。内容涵盖Python、数学、机器学习、数据分析、深度学习、计算机视觉、自然语言处理等多个热门领域。

### 2. 核心功能
- 提供完整的人工智能学习路径规划，从零基础到就业实战
- 收录近200个实战案例和项目，覆盖主流AI技术栈
- 免费提供配套学习教材和资源，降低学习门槛
- 涵盖Python、数学基础、机器学习、深度学习等核心课程
- 支持多种主流框架学习，包括PyTorch、TensorFlow、Keras等

### 3. 适用场景
- 零基础想要进入AI领域的学习者，需要系统性学习路线
- 在校学生或转行人员，希望通过实战项目积累就业竞争力
- 希望系统学习机器学习、深度学习、NLP、CV等方向的开发者
- 需要查找优质开源项目和案例进行参考学习的AI从业者

### 4. 技术亮点
- 项目已获13260颗星标，社区认可度高，资源持续更新
- 覆盖技术栈全面，从基础Python到进阶深度学习框架均有涉及
- 强调实战导向，通过大量案例帮助学习者将理论转化为实践能力
- 完全免费开放，配套教材齐全，适合自学使用
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13260 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络和其他 AI 模型。它通过声明式配置简化了机器学习模型的训练和部署流程，让开发者无需编写大量代码即可快速构建和微调模型。

### 2. 核心功能
- **低代码模型构建**：通过 YAML/JSON 配置即可定义和训练深度学习模型，无需编写复杂代码
- **多模态支持**：支持文本、图像、表格等多种数据类型，涵盖 NLP 和计算机视觉领域
- **大模型微调**：内置对 LLaMA、Mistral 等主流大语言模型的微调支持
- **自动机器学习**：自动处理数据预处理、特征工程和模型超参数调优
- **可扩展架构**：基于 PyTorch 构建，支持自定义模型组件和扩展

### 3. 适用场景
- 快速构建和训练自定义 NLP 模型，如文本分类、情感分析、命名实体识别
- 对 LLaMA、Mistral 等大语言模型进行领域微调，适配垂直场景
- 数据-centric 的机器学习项目，通过数据驱动方式优化模型性能
- 计算机视觉任务，如图像分类、目标检测等模型的快速搭建

### 4. 技术亮点
- 采用声明式配置方式，大幅降低深度学习项目的开发门槛
- 原生支持 PyTorch 生态，兼容 Hugging Face Transformers 模型
- 提供端到端的 MLOps 能力，从数据准备到模型部署一站式解决
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9171 | 🍴 1234 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8961 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1898 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6993 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6399 | 🍴 773 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖敏感词检测、语言识别、实体抽取、情感分析等基础NLP功能，同时收录了大量中文词库、预训练模型、开源数据集及竞赛代码，是中文NLP开发与研究的综合性资源库。

## 2. 核心功能
- **基础NLP工具**：敏感词检测、繁简体转换、手机号/身份证/邮箱抽取、断句分词、语言检测等开箱即用功能
- **丰富词库资源**：中日文人名库、同义/反义词库、汽车品牌库、古诗词库、地名词库、医学/法律/财经等领域词库
- **预训练模型与深度学习**：BERT、ALBERT、GPT-2等中文预训练模型，命名实体识别、文本分类、关系抽取等任务代码
- **数据集与基准评测**：中文NLP竞赛数据集、问答数据集、谣言数据库、对话机器人语料及中文语言理解测评基准
- **语音与生成任务**：ASR语音识别、语音情感分析、中文聊天机器人、文本摘要生成、自动对联等生成式NLP工具

## 3. 适用场景
- **企业内容审核系统**：快速集成敏感词过滤、情感分析、实体抽取，适用于舆情监控与内容安全
- **中文智能客服/对话机器人**：利用开源对话系统、知识图谱问答、多轮对话资源快速搭建客服机器人
- **学术研究与模型对比实验**：提供标准化数据集、预训练模型和竞赛TOP方案，方便研究者进行基准测试
- **知识图谱构建**：整合命名实体识别、关系抽取、实体链接等工具，助力垂直领域知识图谱建设

## 4. 技术亮点
- 收录清华XLORE跨语言百科知识图谱、百度开源信息抽取系统等
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82458 | 🍴 15270 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100+ 模型。该项目研究成果发表于 ACL 2024 会议，旨在为研究人员和开发者提供简洁易用的模型微调解决方案。

## 2. 核心功能
- 支持 100+ 主流大语言模型和视觉语言模型的微调
- 提供多种高效微调方法，包括 LoRA、QLoRA、全参数微调等
- 支持指令微调（Instruction Tuning）和 RLHF 强化学习人类反馈
- 内置量化技术，降低显存占用，支持低精度推理
- 兼容 Transformers 和 PEFT 库，集成 MoE（混合专家）架构模型

## 3. 适用场景
- 研究人员快速实验不同模型的微调效果
- 开发者基于开源模型定制垂直领域专用模型
- 个人用户低成本微调大模型进行本地部署
- 企业团队进行多模型对比评测和迭代优化

## 4. 技术亮点
- 统一接口支持多模型、多任务、多微调方法的无缝切换
- 针对国产模型（如 DeepSeek、Qwen、Gemma）深度优化
- 支持 Agent 应用场景的端到端微调训练
- 提供清晰的日志和可视化工具，便于训练过程监控
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74090 | 🍴 9067 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 64878 | 🍴 12579 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46709 | 🍴 8153 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub 项目分析：ailearning

---

### 1. 中文简介
该项目是一个全面的机器学习与深度学习实战教程库，内容涵盖数据分析、线性代数、PyTorch 框架、NLTK 自然语言处理以及 TensorFlow 2.x 等核心技术。项目通过大量实战案例帮助学习者系统掌握从传统机器学习到深度学习的完整知识体系。

---

### 2. 核心功能
- **经典机器学习算法实现**：涵盖 SVM、KNN、逻辑回归、朴素贝叶斯、Adaboost、线性回归等主流算法。
- **深度学习框架实战**：提供基于 PyTorch 和 TensorFlow 2.x 的 DNN、RNN、LSTM 等网络结构实现。
- **聚类与关联规则挖掘**：包含 K-Means 聚类、Apriori 和 FP-Growth 频繁项集挖掘算法。
- **降维与特征提取**：实现 PCA 主成分分析、SVD 奇异值分解等数据处理技术。
- **自然语言处理（NLP）**：基于 NLTK 库提供文本处理、分词、情感分析等 NLP 相关功能。
- **推荐系统**：实现基于协同过滤等算法的推荐系统案例。

---

### 3. 适用场景
- **机器学习初学者**：作为系统学习机器学习和深度学习的入门实战指南。
- **高校学生/考研人群**：用于线性代数、概率统计等数学基础与算法实现的对照学习。
- **数据分析师**：快速掌握常用数据分析、特征工程和算法调优技能。
- **NLP 爱好者**：借助 NLTK 和 TF2/PyTorch 进行自然语言处理项目开发。

---

### 4. 技术亮点
- **技术栈全面**：同时覆盖 scikit-learn、PyTorch、TensorFlow 2.x 三大主流框架，兼顾经典 ML 与深度学习。
- **数学基础扎实**：融入线性代数知识讲解，帮助理解算法背后的数学原理。
- **代码结构清晰**：算法实现规范，适合阅读、学习与二次开发参考。
- **高人气项目**：42455 星标，说明社区认可度高，学习资料丰富。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42455 | 🍴 11520 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36231 | 🍴 7429 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33818 | 🍴 4709 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29061 | 🍴 3538 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21838 | 🍴 3352 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17356 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

## 1. 中文简介
这是一个汇集500个AI项目的资源仓库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等方向，所有项目均附带完整代码。该项目是一个精选的AI技术资源合集，适合从入门到进阶的学习者使用。

## 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供完整可运行的源代码
- 作为AI学习路径的参考指南，帮助学习者系统性地掌握核心技术
- 项目按领域分类，便于快速定位感兴趣的方向
- 标签体系完善，支持按技术栈和关键词筛选

## 3. 适用场景
- **AI学习者**：作为系统学习机器学习和深度学习的实战项目清单
- **开发者求职**：用于构建个人作品集，展示AI项目经验
- **技术调研**：快速了解当前AI领域的热门项目和实现方案
- **团队参考**：企业或研究团队寻找技术灵感与实现思路

## 4. 技术亮点
- 项目数量庞大（500+），覆盖主流AI技术栈
- 所有项目附带代码，可直接运行学习
- 标签体系清晰，便于按技术领域筛选
- 高星标数（36231）表明社区认可度极高
- 涵盖从基础到进阶的完整学习路径
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36231 | 🍴 7429 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于人工智能的浏览器工作流自动化工具，能够利用大语言模型（LLM）和计算机视觉技术来自动执行基于浏览器的任务。它通过智能理解网页内容并模拟人类操作，实现复杂网页交互的自动化。

### 2. 核心功能
- **AI驱动浏览器自动化**：利用大语言模型理解网页内容并智能决策操作步骤
- **多浏览器引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **计算机视觉能力**：通过视觉识别技术定位页面元素，模拟真实用户操作
- **API接口支持**：提供 API 接口，便于集成到现有工作流系统中
- **RPA工作流编排**：支持复杂多步骤业务流程的自动化编排与执行

### 3. 适用场景
- **数据抓取与表单填写**：自动登录网站、填写表单、批量提取数据
- **跨平台RPA替代**：作为 Power Automate 等商业RPA工具的开源替代方案
- **重复性网页任务自动化**：定期报表生成、价格监控、订单处理等周期性任务
- **测试与QA流程自动化**：自动化执行Web应用的功能测试和回归测试

### 4. 技术亮点
- **LLM+视觉融合架构**：将大语言模型的理解能力与计算机视觉的感知能力结合，实现更接近人类操作的智能自动化
- **开源免费**：基于Python开发的开源项目，社区活跃，持续迭代
- **灵活集成**：支持多种浏览器自动化工具，可灵活适配不同技术栈
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22749 | 🍴 2139 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台，提供开源、云端和企业版产品以及标注服务。它支持图像、视频和3D标注，具备AI辅助标注、质量保证、团队协作、数据分析和开发者API等核心能力。

## 2. 核心功能
- **多模态标注**：支持图像、视频和3D数据的标注任务
- **AI辅助标注**：内置AI模型辅助自动标注，大幅提升效率
- **团队协作**：支持多人协作完成大规模标注项目
- **质量保证**：提供质检机制确保标注数据的准确性
- **开发者API**：开放API接口，便于集成到自定义工作流

## 3. 适用场景
- **目标检测数据集构建**：用于标注边界框（bounding box）数据，训练检测模型
- **语义分割标注**：支持像素级标注，适用于分割任务的数据集制作
- **视频行为标注**：对视频序列进行帧级标注，适用于动作识别等场景
- **大规模团队协作标注**：适合需要多人分工协作的企业级标注项目

## 4. 技术亮点
- 支持多种主流深度学习框架（PyTorch、TensorFlow）的标注格式导出
- 提供丰富的标签类型，涵盖图像分类、目标检测、语义分割等任务
- 开源社区活跃，拥有超过16500颗星，生态完善
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16523 | 🍴 3802 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## GitHub项目分析：pytorch-grad-cam

### 1. 中文简介

这是一个基于PyTorch的高级计算机视觉可解释性工具库，支持多种深度学习模型可视化分析。该项目为CNN和Vision Transformer等模型提供可解释性分析能力，帮助用户理解模型的决策过程。

### 2. 核心功能

- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种类激活图生成算法
- 兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构
- 支持图像分类、目标检测、图像分割等多种任务类型
- 提供图像相似度分析的可视化解释能力
- 内置丰富的可视化输出功能，便于结果展示与分析

### 3. 适用场景

- **模型调试与优化**：定位模型关注区域，发现训练问题
- **医疗影像分析**：解释AI诊断结果，增强临床信任度
- **自动驾驶系统**：可视化车辆识别模型的决策依据
- **学术研究**：发表可解释AI相关论文时的可视化支持

### 4. 技术亮点

- 12955+星标，社区认可度高，文档完善
- 统一接口支持多种CAM变体算法，无需重复实现
- 对PyTorch生态友好，集成便捷，学习成本低
- 持续维护更新，支持最新模型架构（如Vision Transformer）
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12955 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## kornia 项目分析

### 1. 中文简介
kornia 是一个面向空间人工智能的几何计算机视觉库，基于 PyTorch 构建，专为深度学习场景下的图像处理与几何计算而设计。它将传统计算机视觉算法与神经网络无缝融合，为研究人员和开发者提供了一套高效、可微分的视觉处理工具集。

### 2. 核心功能
- 提供可微分的几何计算机视觉算子，支持端到端神经网络训练
- 内置丰富的图像处理功能，包括滤波、变换、形态学操作等
- 支持相机标定、立体视觉、三维重建等经典视觉任务
- 与 PyTorch 生态深度集成，可直接在 GPU 上运行
- 提供机器人视觉、空间感知等高级应用场景的专用模块

### 3. 适用场景
- **自动驾驶与机器人导航**：用于环境感知、SLAM（同步定位与建图）等空间理解任务
- **深度学习视觉研究**：作为可微分视觉模块嵌入神经网络，进行端到端训练
- **工业图像检测**：应用于缺陷检测、尺寸测量等需要几何精度的工业场景
- **多视图三维重建**：支持从多张图像中恢复场景的三维结构

### 4. 技术亮点
- **可微分设计**：所有核心算子均支持自动求导，可直接集成到 PyTorch 模型中反向传播
- **GPU 加速**：完全基于 PyTorch 张量运算，充分利用 GPU 并行计算能力
- **开源社区活跃**：星标数超过 11,000，积极参与 Hacktoberfest 等开源活动，社区贡献活跃
- **领域专注**：专门针对"空间 AI"这一新兴领域设计，填补了传统 CV 库与深度学习框架之间的空白
- 链接: https://github.com/kornia/kornia
- ⭐ 11316 | 🍴 1221 | 语言: Python
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
- ⭐ 3366 | 🍴 411 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2632 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2505 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

# GitHub项目分析：openclaw

## 1. 中文简介
openclaw 是一款个人AI助手，支持任意操作系统和平台。以"龙虾方式"运行，让你完全掌控自己的数据，真正实现数据自主。

## 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行
- **数据自主可控**：所有数据完全由用户自己管理，不依赖第三方云服务
- **AI助手能力**：提供智能对话、任务处理等个人助理功能
- **本地化部署**：可私有化部署，保障隐私安全
- **TypeScript开发**：基于TypeScript构建，代码可维护性高

## 3. 适用场景
- 注重隐私、希望AI数据完全本地化的个人用户
- 需要跨平台统一AI助手体验的开发者
- 希望自建AI助手、拒绝数据上云的企业或个人
- 喜欢开源项目、可二次定制的技术爱好者

## 4. 技术亮点
- 采用TypeScript开发，类型安全且生态丰富
- 强调"own-your-data"理念，支持私有化部署
- 项目热度极高（38万+星标），社区活跃度高
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386271 | 🍴 81191 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# Superpowers 项目分析

## 1. 中文简介
Superpowers 是一个实用的智能体技能框架与软件开发方法论，通过子代理驱动开发模式，帮助开发者高效完成从需求分析到代码实现的完整软件开发生命周期。

## 2. 核心功能
- 提供智能体技能框架，支持自动化软件开发流程
- 采用子代理驱动开发模式，实现任务分解与并行处理
- 覆盖完整软件开发生命周期（SDLC），从头脑风暴到编码部署
- 集成AI能力，辅助代码生成和问题解决

## 3. 适用场景
- 快速原型开发与头脑风暴
- 自动化软件开发流程
- 复杂任务的分解与并行处理
- AI辅助的代码生成与优化

## 4. 技术亮点
- 基于Shell脚本实现，轻量级且易于集成
- 支持多子代理协同工作，提升开发效率
- 将AI智能体能力与软件开发方法论深度融合
- 链接: https://github.com/obra/superpowers
- ⭐ 271972 | 🍴 24324 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 230391 | 🍴 45612 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码（fair-code）工作流自动化平台，内置原生 AI 能力。支持可视化构建与自定义代码结合，可自托管或云端部署，提供 400+ 种集成方式。

### 2. 核心功能
- 可视化工作流构建：通过拖拽节点方式设计自动化流程，降低使用门槛
- 原生 AI 能力：内置 AI 功能，支持智能工作流编排
- 400+ 集成：覆盖主流 API 和服务，支持快速对接各类应用
- 灵活部署：支持自托管和云端部署，满足不同安全与隐私需求
- MCP 协议支持：兼容 Model Context Protocol，便于与 AI 模型交互

### 3. 适用场景
- 企业自动化：跨系统数据同步、业务流自动化、定时任务调度
- AI 应用集成：将大语言模型能力接入现有业务流程，构建智能工作流
- 低代码开发：非技术人员可通过可视化界面快速搭建自动化方案
- 数据管道构建：多源数据聚合、ETL 处理、实时数据流编排

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态丰富
- 支持 MCP（Model Context Protocol）客户端与服务端，适配主流 AI 模型
- 公平代码许可证，兼顾开源社区与企业级使用需求
- 400+ 原生集成节点，减少自定义开发成本
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200599 | 🍴 60125 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于实现人人可用的AI愿景，让每个人都能使用并在此基础上构建。我们的使命是提供相应工具，让用户能够专注于真正重要的事物。

### 2. 核心功能
- 支持创建自主运行的AI代理，可独立完成复杂任务
- 兼容多种大语言模型后端，包括OpenAI、Claude、LLaMA等
- 提供插件系统，可扩展代理能力以连接各种外部工具和服务
- 支持多步骤任务分解与自主执行，代理可根据结果动态调整策略
- 开源代码，允许用户自由定制和二次开发

### 3. 适用场景
- 自动化数据处理与分析任务（如网页抓取、数据整理）
- 内容创作与营销自动化（如自动生成文章、社交媒体管理）
- 研究辅助与知识整合（如信息搜集、报告撰写）
- 个人效率工具开发（如日程管理、邮件处理）

### 4. 技术亮点
- 采用模块化架构设计，便于扩展和集成第三方服务
- 支持多LLM后端切换，用户可根据需求选择性价比最优的方案
- 具备记忆功能，代理可在任务执行过程中保存和调用历史上下文
- 活跃的开源社区，持续迭代更新，项目星标数超过18万
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186618 | 🍴 46086 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 167185 | 🍴 9383 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167117 | 🍴 21570 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164517 | 🍴 30564 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157785 | 🍴 46178 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153229 | 🍴 9858 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

