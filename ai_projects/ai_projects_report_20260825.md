# GitHub AI项目每日发现报告
日期: 2026-08-25

## 新发布的AI项目

### learn
- 

## GitHub 项目分析：learn

### 1. 中文简介
这是一个个人 AI 学习系统项目，由开发者用于记录和研究人工智能相关知识。项目采用 TypeScript 编写，目前获得 149 个星标，说明已受到一定社区关注。

### 2. 核心功能
- 提供 AI 学习路径与知识体系的整理和记录
- 使用 TypeScript 实现，便于代码示例和工具开发
- 可作为个人 AI 学习知识库，支持持续迭代和扩展
- 可能包含 AI 相关算法、模型或工具的学习笔记与实现
- 支持将学习成果以代码形式落地，便于实践验证

### 3. 适用场景
- AI 初学者系统性地梳理学习路线和知识框架
- 开发者将 AI 理论知识转化为 TypeScript 代码实践
- 个人知识管理，用于记录和回顾 AI 学习历程
- 团队内部 AI 技术分享与学习资料沉淀

### 4. 技术亮点
- 采用 TypeScript 开发，具备良好的类型安全和开发体验
- 项目结构简洁，适合快速学习和二次开发
- 星标数达 149，说明项目在 AI 学习领域具有一定参考价值

---

> ⚠️ 由于该项目描述较为简略且未提供仓库链接，以上分析基于有限信息推断，部分内容可能存在偏差。建议查看项目实际代码以获取更准确的分析。
- 链接: https://github.com/amosblomqvist/learn
- ⭐ 149 | 🍴 18 | 语言: TypeScript

### wenai
- 描述: An intimate AI companion skill for OpenClaw — fall in love with your AI girlfriend, with a Pony V6 XL powered visual workflow.
- 链接: https://github.com/Straniero44/wenai
- ⭐ 63 | 🍴 20 | 语言: 未知

### swissdevjobs-cli
- 

# swissdevjobs-cli 项目分析

## 1. 中文简介
这是一个零依赖的 Python CLI 工具，支持从终端或 AI 代理搜索并申请覆盖 7 个国家的约 4,700 个薪资透明的技术职位。同时提供 MCP 服务器和 Claude Code 插件，方便与 AI 工作流集成。

## 2. 核心功能
- 搜索薪资透明的技术岗位，覆盖瑞士、德国、英国、美国、加拿大、荷兰、法国 7 个国家
- 零依赖 Python CLI，无需额外安装依赖即可运行
- 提供 MCP 服务器，支持与 AI 代理无缝集成
- 内置 Claude Code 插件，可直接在 Claude Code 环境中使用
- 支持从终端直接申请职位

## 3. 适用场景
- 开发者希望通过终端快速搜索海外技术职位
- AI 代理（如 Claude Code）辅助求职，自动筛选和申请岗位
- 关注薪资透明度的求职者，快速定位符合预期的职位
- 远程/跨国求职者，覆盖欧洲和北美多个技术岗位市场

## 4. 技术亮点
- **零依赖设计**：纯 Python 实现，无第三方依赖，开箱即用
- **MCP 协议支持**：遵循 Model Context Protocol 标准，便于与各类 AI 工具集成
- **多平台兼容**：同时支持 CLI 终端和 AI Agent 两种使用方式
- 链接: https://github.com/Stupidoodle/swissdevjobs-cli
- ⭐ 45 | 🍴 7 | 语言: Python
- 标签: ai-agents, claude, claude-code, cli, developer-jobs

### technocore
- 

# 项目分析：technocore

## 1. 中文简介
Technocore是一个面向AI代理的去中心化密码学身份与协作框架。它基于Ed25519算法实现身份认证，提供签名消息总线和贡献证明机制，构建可信的AI代理协作生态。

## 2. 核心功能
- **Ed25519密码学身份**：为AI代理生成去中心化、可验证的加密身份标识
- **签名消息总线**：支持经过数字签名的安全消息传递与广播机制
- **贡献证明框架**：追踪并验证AI代理在协作中的工作贡献
- **Python原生实现**：基于Python语言开发，便于集成与二次开发

## 3. 适用场景
- AI代理间的身份认证与可信通信
- 去中心化AI协作网络中的任务贡献记录
- 多Agent系统中的安全消息路由与审计
- 需要身份溯源的AI驱动应用开发

## 4. 技术亮点
- 采用Ed25519签名算法，兼顾高性能与高安全性
- 将身份认证、消息总线与贡献证明三者整合，形成完整的AI代理信任基础设施
- 轻量级设计，适合资源受限的AI代理部署环境
- 链接: https://github.com/d4ncboz/technocore
- ⭐ 34 | 🍴 0 | 语言: Python

### deepseek-v4-flash-vision-video-rag
- 

## 项目分析：deepseek-v4-flash-vision-video-rag

### 1. 中文简介
这是一个基于 DeepSeek 视觉大模型的视频理解与问答 Agent 技能，让 AI 能够真正"看懂"视频内容并回答相关问题。系统会提供答案、精确的时间戳定位，并自动生成包含可播放片段和关键帧的 HTML 预览页供用户核对。

### 2. 核心功能
- **视频抽帧索引**：按时间轴一次性抽帧并建立视觉索引
- **三级问答流程**：本地粗筛 → 视觉精排 → 深度阅读回答
- **精准时间戳引用**：答案附带 [MM:SS] 格式的时间定位
- **自动生成预览页**：输出自包含 HTML 文件，内嵌视频片段和关键帧
- **浏览器直接查看**：双击 HTML 文件即可在浏览器中预览答案

### 3. 适用场景
- **视频内容检索**：快速定位视频中特定事件或信息的时间位置
- **教育/培训视频问答**：对教学视频进行智能问答和知识点检索
- **会议/讲座视频分析**：从长视频中提取关键片段并生成摘要
- **视频素材管理**：为视频库建立视觉索引，实现语义级搜索

### 4. 技术亮点
- 采用 DeepSeek V4 Flash Vision 视觉大模型，具备高效视频理解能力
- 创新的"粗筛-精排-深读"三级处理架构，平衡效率与准确性
- 一次性建索引、多次问答的 RAG 设计，提升重复查询效率
- 输出格式友好，自动生成可交互的 HTML 预览，无需额外工具即可查看结果
- 链接: https://github.com/liangdabiao/deepseek-v4-flash-vision-video-rag
- ⭐ 32 | 🍴 2 | 语言: Python
- 标签: skill, skills

### demo-linkedin-agent
- 描述: Fetch.ai LinkedIn poster agent for Agentverse using uAgents and ASI:One
- 链接: https://github.com/ShyamRV/demo-linkedin-agent
- ⭐ 30 | 🍴 1 | 语言: Python

### hengzhi
- 描述: 看见每一笔决策。本机 AI 交易复盘台，只做币安 USDT-M。
- 链接: https://github.com/7836246/hengzhi
- ⭐ 21 | 🍴 14 | 语言: Python

### ai-tools-list
- 描述: Lista completa com ferramentas desde IDE, Agents, CLI...
- 链接: https://github.com/devfraga/ai-tools-list
- ⭐ 15 | 🍴 0 | 语言: 未知

### deepseek-v4-flash-vision-rag
- 描述: DeepSeek V4-Flash Vision RAG 让 AI 真正"看懂" 一份 PDF，然后你对它提问：它告诉你答案、答案在第几页， 并把那一页的原图展示出来给你核对。  基于 DeepSeek 视觉大模型 deepseek-v4-flash-vision-exp 的 PDF 深度问答与检索 （vision RAG）agent skill。支持文字版 PDF，也支持扫描版；能看懂 图表、表格、代码块、公式，而不只是认字。
- 链接: https://github.com/liangdabiao/deepseek-v4-flash-vision-rag
- ⭐ 13 | 🍴 1 | 语言: Python
- 标签: skills

### aicss
- 描述: AICSS React components and CLI. Website: aicss.dev
- 链接: https://github.com/kvnkld/aicss
- ⭐ 12 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, css, react, shadcn-registry, svelte

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中文自然语言处理资源集合，提供了从基础工具（敏感词检测、分词、词性标注）到高级应用（知识图谱构建、对话系统、语音识别）的多种工具、数据集和预训练模型，涵盖文本处理、信息抽取、情感分析、问答系统等多个NLP领域。

## 2. 核心功能
- 提供敏感词检测、语言识别、手机号/身份证/邮箱抽取等基础NLP工具
- 包含丰富的中文词向量、情感分析、文本分类、命名实体识别等模型资源
- 整合知识图谱构建、问答系统、对话机器人等高级NLP应用工具
- 提供语音识别、OCR文字识别、音频处理等多媒体NLP支持
- 收录NLP数据集、论文、教程和竞赛方案等学习研究资源

## 3. 适用场景
- 开发者快速集成中文NLP功能（敏感词过滤、信息抽取）到业务系统
- 研究人员获取NLP数据集、预训练模型和最新论文资源
- 企业构建知识图谱、智能问答或对话机器人系统
- NLP学习者使用教程、示例代码和竞赛方案进行技术实践

## 4. 技术亮点
项目汇集了BERT、ALBERT、RoBERTa等主流预
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82661 | 🍴 15275 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI 机器学习/深度学习/计算机视觉/NLP 项目合集

### 1. 中文简介
这是一个包含 500 个 AI 实战项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域，所有项目均附带完整代码实现。该项目在 GitHub 上获得了 36,527 颗星标，是一个广受关注的 AI 学习资源库。

### 2. 核心功能
- 提供 500 个 AI 项目的完整代码实现，覆盖主流技术栈
- 按领域分类：机器学习、深度学习、计算机视觉、NLP 四大板块
- 适合从入门到进阶的开发者，提供可运行的实战案例
- 包含 Python 语言的完整项目代码，便于学习和复现

### 3. 适用场景
- AI 学习者系统性地练习和巩固机器学习/深度学习知识
- 开发者寻找项目灵感，快速搭建 AI 应用原型
- 教师或培训人员作为课程案例和教学参考资料
- 求职者准备技术面试，积累项目经验

### 4. 技术亮点
- 项目数量庞大（500 个），覆盖 AI 领域主流方向
- 所有项目均附带代码，可直接运行和修改
- 标签清晰，便于按技术方向快速筛选学习
- 高星标数（36,527）证明社区认可度和实用性
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36527 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，能够以直观的图形界面展示模型结构。

## 2. 核心功能
- 支持 PyTorch、TensorFlow、Keras、ONNX、CoreML、TensorFlow Lite 等多种框架模型的可视化
- 提供交互式图形界面，清晰展示神经网络层级结构和数据流向
- 支持 safetensors 等安全模型格式
- 基于 Web 技术实现，跨平台运行
- 支持多种 NumPy 数组格式模型的查看

## 3. 适用场景
- 深度学习研究者用于调试和理解复杂模型结构
- 模型部署前检查网络层配置是否正确
- 教学演示中直观展示神经网络工作原理
- 跨框架模型迁移时对比不同框架的模型表示

## 4. 技术亮点
- 支持格式极其广泛，几乎覆盖主流深度学习框架
- 纯前端实现，无需后端服务即可运行
- 开源项目，拥有 33399 星标，社区活跃度高
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33399 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开源的深度学习模型交换标准，旨在实现不同机器学习框架之间的互操作性。它允许开发者在不同深度学习框架之间无缝迁移模型，打破了框架之间的壁垒。

### 2. 核心功能
- 提供统一的模型格式，支持跨框架模型导入与导出
- 支持主流深度学习框架（PyTorch、TensorFlow、Keras、scikit-learn等）的模型转换
- 提供模型优化工具链，支持推理加速和部署优化
- 定义开放的算子集（Operators），确保模型计算逻辑的一致性

### 3. 适用场景
- 将PyTorch或TensorFlow训练的模型部署到ONNX Runtime进行高效推理
- 在不同深度学习框架之间迁移模型，避免重新训练
- 将模型转换为移动端或嵌入式设备友好的格式进行部署
- 在生产环境中统一模型管理，降低多框架维护成本

### 4. 技术亮点
- 由Microsoft和Facebook联合发起，得到业界广泛支持
- 拥有活跃的开源社区和完善的生态系统
- 支持从训练到推理的全流程优化，兼容CPU、GPU等多种硬件平台
- 链接: https://github.com/onnx/onnx
- ⭐ 21355 | 🍴 4011 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的技术参考书，涵盖从模型训练、调试到大规模部署的全流程。该项目以Python为核心，为AI工程师和研究人员提供系统化的工程实践指南。

## 2. 核心功能
- **大模型训练与调试**：提供LLM训练过程中的问题排查和优化策略
- **GPU与硬件优化**：深入讲解GPU使用、网络通信和存储性能调优
- **推理部署实践**：涵盖模型推理加速和生产环境部署方案
- **可扩展性设计**：基于SLURM等调度器的分布式训练架构设计
- **MLOps工程体系**：从实验管理到模型上线的完整工程链路

## 3. 适用场景
- 大规模语言模型的训练与微调工程实践
- 基于PyTorch的分布式训练系统搭建与优化
- GPU集群的资源调度、网络拓扑和存储方案设计
- 模型推理服务的高性能部署与生产环境运维

## 4. 技术亮点
- 结合Transformer等主流框架的实战经验总结
- 覆盖从单卡调试到千卡训练的全尺度工程问题
- 聚焦生产环境中的真实痛点，如显存优化、通信瓶颈等
- 开源开放的知识共享模式，持续迭代更新
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18703 | 🍴 1206 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17385 | 🍴 2125 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13281 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11633 | 🍴 917 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10692 | 🍴 5696 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI 机器学习/深度学习/计算机视觉/NLP 项目合集

### 1. 中文简介
这是一个包含 500 个 AI 实战项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域，所有项目均附带完整代码实现。该项目在 GitHub 上获得了 36,527 颗星标，是一个广受关注的 AI 学习资源库。

### 2. 核心功能
- 提供 500 个 AI 项目的完整代码实现，覆盖主流技术栈
- 按领域分类：机器学习、深度学习、计算机视觉、NLP 四大板块
- 适合从入门到进阶的开发者，提供可运行的实战案例
- 包含 Python 语言的完整项目代码，便于学习和复现

### 3. 适用场景
- AI 学习者系统性地练习和巩固机器学习/深度学习知识
- 开发者寻找项目灵感，快速搭建 AI 应用原型
- 教师或培训人员作为课程案例和教学参考资料
- 求职者准备技术面试，积累项目经验

### 4. 技术亮点
- 项目数量庞大（500 个），覆盖 AI 领域主流方向
- 所有项目均附带代码，可直接运行和修改
- 标签清晰，便于按技术方向快速筛选学习
- 高星标数（36,527）证明社区认可度和实用性
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36527 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，能够以直观的图形界面展示模型结构。

## 2. 核心功能
- 支持 PyTorch、TensorFlow、Keras、ONNX、CoreML、TensorFlow Lite 等多种框架模型的可视化
- 提供交互式图形界面，清晰展示神经网络层级结构和数据流向
- 支持 safetensors 等安全模型格式
- 基于 Web 技术实现，跨平台运行
- 支持多种 NumPy 数组格式模型的查看

## 3. 适用场景
- 深度学习研究者用于调试和理解复杂模型结构
- 模型部署前检查网络层配置是否正确
- 教学演示中直观展示神经网络工作原理
- 跨框架模型迁移时对比不同框架的模型表示

## 4. 技术亮点
- 支持格式极其广泛，几乎覆盖主流深度学习框架
- 纯前端实现，无需后端服务即可运行
- 开源项目，拥有 33399 星标，社区活跃度高
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33399 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub项目分析：cheatsheets-ai

## 1. 中文简介
这是一个为深度学习和机器学习研究者提供的核心速查表集合，涵盖了机器学习与深度学习领域的重要知识点和实用技巧。项目旨在帮助研究人员快速查阅关键概念和代码示例。

## 2. 核心功能
- 提供深度学习与机器学习领域的核心概念速查表
- 涵盖Keras、NumPy、SciPy、Matplotlib等常用库的使用技巧
- 整合人工智能领域的重要知识点和最佳实践
- 以简洁形式呈现复杂概念，便于快速查阅

## 3. 适用场景
- 深度学习研究者快速回顾关键概念和公式
- 机器学习工程师查阅常用库的API用法
- 学生备考或复习深度学习相关知识点
- 研究人员撰写论文时快速查找技术细节

## 4. 技术亮点
- 聚焦核心速查内容，简洁实用，适合快速参考
- 覆盖从基础库（NumPy、SciPy）到高级框架（Keras）的完整技术栈
- 结合Medium文章推荐，内容经过社区验证，质量可靠
- 星标数超过1.5万，说明在AI社区中具有较高认可度和实用性
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# 项目分析：Ai-Learn

## 1. 中文简介
这是一个免费的人工智能学习资源库，收录了近200个实战案例与项目，配套提供完整教材，帮助零基础学习者系统掌握Python、机器学习、深度学习、计算机视觉和自然语言处理等热门领域，最终实现就业实战目标。

## 2. 核心功能
- 提供系统化的人工智能学习路线图，从入门到进阶路径清晰
- 收录近200个实战案例与项目，涵盖主流AI技术方向
- 免费提供配套教材和参考资料，降低学习门槛
- 覆盖Python、PyTorch、TensorFlow、Keras等主流框架的实战应用

## 3. 适用场景
- 零基础学习者系统入门人工智能领域
- 求职者准备面试，积累实战项目经验
- 数据分析师/算法工程师拓展技能树，参考优秀项目实现

## 4. 技术亮点
- 项目星标数达13281，社区认可度高，资源持续更新维护
- 涵盖深度学习全领域：CV、NLP、数据分析、数据挖掘等热门方向
- 整合了TensorFlow、PyTorch、Caffe、Keras等多框架实战案例
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13281 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码机器学习框架，专为快速构建自定义大语言模型、神经网络及其他 AI 模型而设计。它通过声明式配置简化了深度学习模型的训练与部署流程，让开发者无需编写大量代码即可训练高性能模型。

### 2. 核心功能
- **低代码模型构建**：通过声明式 YAML/JSON 配置快速定义和训练深度学习模型，无需编写复杂代码。
- **多模态数据支持**：原生支持表格数据、文本、图像、音频等多种数据类型。
- **大语言模型微调**：内置对 LLaMA、Llama2、Mistral 等主流 LLM 的微调支持，便于定制化部署。
- **自动化特征工程**：自动处理特征编码、归一化、嵌入等数据预处理任务。
- **模型可解释性**：提供内置的可视化分析工具，帮助理解模型决策逻辑。

### 3. 适用场景
- 快速原型验证：业务方希望快速验证深度学习方案可行性，无需深入算法细节。
- 大模型微调部署：对开源 LLM 进行领域适配和微调，构建行业专属模型。
- 表格数据预测：传统结构化数据的分类、回归任务，替代手工特征工程。
- 多模态应用开发：同时处理文本、图像等混合数据的 AI 应用构建。

### 4. 技术亮点
- **声明式 API**：以配置驱动代替代码驱动，大幅降低深度学习使用门槛。
- **PyTorch 后端**：基于 PyTorch 构建，兼容主流深度学习生态。
- **数据为中心理念**：强调数据质量与特征工程，而非单纯堆砌模型复杂度。
- **开箱即用的预训练组件**：提供丰富的预训练模型和嵌入层，支持迁移学习。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9187 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8967 | 🍴 3108 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8370 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6989 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6440 | 🍴 780 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中文自然语言处理资源集合，提供了从基础工具（敏感词检测、分词、词性标注）到高级应用（知识图谱构建、对话系统、语音识别）的多种工具、数据集和预训练模型，涵盖文本处理、信息抽取、情感分析、问答系统等多个NLP领域。

## 2. 核心功能
- 提供敏感词检测、语言识别、手机号/身份证/邮箱抽取等基础NLP工具
- 包含丰富的中文词向量、情感分析、文本分类、命名实体识别等模型资源
- 整合知识图谱构建、问答系统、对话机器人等高级NLP应用工具
- 提供语音识别、OCR文字识别、音频处理等多媒体NLP支持
- 收录NLP数据集、论文、教程和竞赛方案等学习研究资源

## 3. 适用场景
- 开发者快速集成中文NLP功能（敏感词过滤、信息抽取）到业务系统
- 研究人员获取NLP数据集、预训练模型和最新论文资源
- 企业构建知识图谱、智能问答或对话机器人系统
- NLP学习者使用教程、示例代码和竞赛方案进行技术实践

## 4. 技术亮点
项目汇集了BERT、ALBERT、RoBERTa等主流预
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82661 | 🍴 15275 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调，相关研究发表于 ACL 2024。它提供了一站式解决方案，帮助用户快速上手并定制各类主流 AI 模型。

## 2. 核心功能
- **多模型统一微调**：支持 100+ 种 LLM 和 VLM 的高效微调训练
- **多样化微调方法**：内置全参数微调、LoRA、QLoRA、GPTQ 等多种参数高效微调（PEFT）技术
- **强化学习对齐**：支持 RLHF（基于人类反馈的强化学习）等指令对齐训练
- **MoE 架构支持**：兼容混合专家（Mixture of Experts）模型的高效训练
- **量化优化**：提供多种量化方案，降低显存占用并提升推理效率

## 3. 适用场景
- **企业级模型定制**：基于 Llama、Qwen、DeepSeek 等开源模型进行垂直领域微调
- **多模态应用开发**：对视觉语言模型进行图像理解与生成能力的微调训练
- **低资源环境部署**：通过 QLoRA 和量化技术，在有限显存条件下完成模型适配
- **AI Agent 构建**：为智能体系统定制专属指令微调模型，提升任务执行能力

## 4. 技术亮点
- 项目荣获 ACL 2024 学术认可，代表当前微调领域的最新研究成果
- 集成 Transformers 生态，与 Hugging Face 模型无缝对接
- 支持从 Llama 3、Gemma 到 DeepSeek、Qwen 等主流开源模型的统一训练流程
- 74347 星标表明其社区影响力广泛，是 GitHub 上最受欢迎的 AI 微调框架之一
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74347 | 🍴 9095 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，涵盖12周、24节课的完整学习路径，旨在让所有人都能轻松学习人工智能。课程采用Jupyter Notebook形式，内容通俗易懂，适合零基础学习者。

### 2. 核心功能
- 提供12周系统化的AI学习路径，每周一课，循序渐进
- 涵盖机器学习、深度学习、计算机视觉、NLP等核心领域
- 包含CNN、RNN、GAN等主流AI技术的实践课程
- 每节课配套Jupyter Notebook代码示例，支持动手实践
- 免费开源，适合个人自学和课堂教学使用

### 3. 适用场景
- 高校计算机相关专业的AI基础课程教学
- 企业员工AI技能入门培训
- 编程爱好者自学人工智能的入门路径
- 教师备课资源与课堂辅助材料

### 4. 技术亮点
- 微软官方出品，内容权威且紧跟AI技术发展趋势
- 采用"理论+实践"模式，每个知识点配有可运行的代码
- 课程结构清晰，从基础概念到进阶应用层层递进
- 完全免费开源，社区活跃，持续更新维护
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66895 | 🍴 12919 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# AI Engineering from Scratch 项目分析

## 1. 中文简介
"学会它，构建它，为他人交付它。" 本项目是一个从零开始系统学习AI工程的综合性教程，涵盖从基础理论到实际部署的完整链路，帮助用户掌握构建AI系统的核心能力。

## 2. 核心功能
- **AI智能体开发**：教授如何设计和构建AI Agents及多智能体系统
- **大语言模型应用**：涵盖LLM的原理、微调及实际工程部署
- **计算机视觉与NLP**：深入讲解视觉处理和自然语言处理技术
- **强化学习与 Swarm 智能**：探索基于奖励机制的学习方法和群体智能策略
- **生成式AI实战**：从原理到实践，全面掌握生成式AI系统的构建

## 3. 适用场景
- **AI工程师学习路径**：适合希望系统掌握AI工程技能的开发者
- **企业AI项目落地**：为团队提供从原型到生产环境的完整参考
- **学术研究实践**：将深度学习理论转化为可运行的工程代码
- **开源项目参考**：作为构建AI产品的技术蓝本和最佳实践库

## 4. 技术亮点
- 跨语言实现：同时使用 Python、Rust 和 TypeScript，覆盖不同性能需求场景
- 全栈覆盖：从底层算法到上层应用，贯穿机器学习到生成式AI的完整技术栈
- MCP（Model Context Protocol）支持：提供标准化的AI模型上下文交互协议
- 高社区认可度：48,607 星标，反映其广泛影响力和实用价值
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 48607 | 🍴 8527 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：AiLearning

### 1. 中文简介
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习项目，内容涉及线性代数、PyTorch、NLTK 和 TensorFlow 2 等核心技术。该项目通过丰富的算法实现和代码示例，帮助学习者系统掌握人工智能领域的基础理论与实践能力。

### 2. 核心功能
- 提供主流机器学习算法的完整实现，包括 SVM、K-Means、逻辑回归、朴素贝叶斯、Adaboost 等
- 涵盖深度学习框架（PyTorch、TensorFlow 2）与神经网络（DNN、RNN、LSTM）的实战代码
- 包含自然语言处理（NLP）工具 NLTK 的应用示例
- 实现经典数据挖掘算法，如 Apriori、FP-Growth、PCA、SVD 等
- 提供推荐系统相关算法的实现与讲解

### 3. 适用场景
- 机器学习与深度学习初学者系统学习
- 数据分析工程师提升算法实战能力
- 高校学生完成课程设计或毕业设计参考
- 技术人员快速查阅算法实现与原理

### 4. 技术亮点
该项目集成了线性代数、机器学习、深度学习、NLP 四大知识体系，涵盖 scikit-learn 和主流深度学习框架，内容全面且代码示例丰富，适合一站式系统学习人工智能核心技能。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42483 | 🍴 11513 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36527 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33844 | 🍴 4717 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29210 | 🍴 3564 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21859 | 🍴 3370 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17385 | 🍴 2125 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36527 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介
Skyvern 是一款基于人工智能的浏览器自动化工具，能够智能地完成各类基于网页的工作流程。它通过 AI 视觉识别和 LLM 理解能力，让浏览器自动化更加智能和高效。

## 2. 核心功能
- 基于 AI 视觉识别自动操作浏览器界面元素
- 支持自然语言描述的工作流自动化任务
- 兼容 Playwright、Puppeteer、Selenium 等主流浏览器自动化工具
- 提供 API 接口便于集成到现有系统
- 支持 RPA（机器人流程自动化）场景

## 3. 适用场景
- 企业级网页数据抓取与表单自动填写
- 跨平台工作流自动化（替代 Power Automate）
- 需要登录操作的复杂网页任务自动化
- 定期重复性网页操作任务

## 4. 技术亮点
- 结合计算机视觉与 LLM 实现智能元素识别
- 支持多浏览器引擎，灵活适配不同场景
- 开源免费，社区活跃（22,848 星标）
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22848 | 🍴 2146 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（Computer Vision Annotation Tool）是一款领先的计算机视觉标注平台，专注于构建高质量的视觉数据集以支持视觉AI开发。它提供开源、云端和企业级产品，支持图像、视频和3D数据的AI辅助标注、质量保障、团队协作及开发者API等功能。

### 2. 核心功能
- **多模态标注**：支持图像、视频及3D点云数据的标注
- **AI辅助标注**：集成预训练模型实现智能自动标注
- **团队协作**：支持多人协同标注与任务分配管理
- **质量保证**：内置质检流程确保数据集准确性
- **开放API**：提供开发者接口便于系统集成与定制

### 3. 适用场景
- **目标检测数据集构建**：如自动驾驶、安防监控的物体识别标注
- **语义分割标注**：医学影像、遥感图像等像素级标注任务
- **视频行为分析**：动作识别、轨迹跟踪等时序标注场景
- **AI训练数据流水线**：企业级大规模视觉数据集生产与管理

### 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供完整的标注工具集（边界框、多边形、关键点等）
- 开源架构，可私有化部署或云端使用
- 社区活跃，星标数超1.6万，生态完善
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16592 | 🍴 3815 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## GitHub项目分析：pytorch-grad-cam

### 1. 中文简介

这是一个基于PyTorch的计算机视觉高级可解释性工具库，支持多种深度学习模型的结构化可视化分析。它为研究人员和开发者提供了将模型决策过程可视化的强大能力。

### 2. 核心功能

- 支持CNN和Vision Transformers等多种网络架构的梯度加权类激活映射（Grad-CAM）
- 兼容图像分类、目标检测、语义分割等多种视觉任务
- 提供Score-CAM等替代方法的实现，支持图像相似度分析
- 内置丰富的可视化工具，便于直观展示模型关注区域
- 与PyTorch框架深度集成，使用便捷灵活

### 3. 适用场景

- 深度学习模型的可解释性研究与调试，帮助理解模型决策依据
- 计算机视觉任务中定位关键特征区域，验证模型关注点是否合理
- 学术论文中的可视化展示，增强结果的可读性和说服力
- 医疗影像分析等需要高可信度的领域，辅助医生理解AI诊断逻辑

### 4. 技术亮点

- 同时支持Grad-CAM、Grad-CAM++、Score-CAM等多种主流XAI方法
- 对Vision Transformers（ViT）等新型架构提供原生支持
- 项目星标数超过12,900，社区活跃度高，维护良好
- 标签体系完整，覆盖可解释AI领域的核心关键词
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11324 | 🍴 1234 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8876 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3486 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3425 | 🍴 419 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2636 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2506 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，让你以"龙虾方式"完全掌控自己的数据。这是一个开源、跨平台的私人 AI 解决方案。

### 2. 核心功能
- 跨平台支持，可在任意操作系统上运行
- 完全本地化部署，实现数据自主可控
- 基于 TypeScript 开发，性能稳定可靠
- 提供个性化 AI 助手体验
- 开源免费，社区驱动迭代

### 3. 适用场景
- 注重隐私安全的个人用户，希望本地运行 AI 助手
- 开发者需要跨平台的 AI 辅助工具
- 企业或团队希望自建私有化 AI 解决方案
- 喜欢自定义配置的技术爱好者

### 4. 技术亮点
- 采用 TypeScript 编写，类型安全且易于维护
- 支持多平台部署，兼容性强
- 开源架构，允许用户完全掌控和二次开发
- 以"龙虾"（Crustacean）为品牌标识，社区文化独特
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387555 | 🍴 81355 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## 项目分析：superpowers

### 1. 中文简介
Superpowers 是一个实用的智能体技能框架与软件开发方法论，致力于通过子代理驱动开发（Subagent-Driven Development）提升软件开发效率。它将AI智能体能力与标准化开发流程相结合，为开发者提供一套可落地的智能化开发解决方案。

### 2. 核心功能
- **智能体技能框架**：提供可复用的AI技能模块，支持自动化任务执行
- **子代理驱动开发**：通过多个子代理协同完成复杂开发任务
- **标准化开发流程**：集成SDLC（软件开发生命周期）最佳实践
- **AI辅助头脑风暴**：支持创意发散与技术方案讨论
- **代码生成与协作**：AI参与编码全过程，提升开发效率

### 3. 适用场景
- 需要AI辅助完成大型软件项目开发与架构设计
- 希望通过智能体自动化提升日常编码与调试效率
- 团队希望采用标准化智能体驱动的开发方法论
- 需要AI参与技术方案讨论与头脑风暴的创意场景

### 4. 技术亮点
- 采用Shell脚本实现，轻量级且易于集成到现有工作流
- 将"技能"概念模块化，支持灵活组合与扩展
- 标签涵盖AI、头脑风暴、编码、OBRA、SDLC等多领域，体现综合性方法论设计
- 高星标数（27万+）反映社区对其实用价值的高度认可
- 链接: https://github.com/obra/superpowers
- ⭐ 277364 | 🍴 24815 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## Hermes-Agent 项目分析

### 1. 中文简介
Hermes-Agent 是一个能够与你共同成长的 AI 智能代理框架。它支持多种大语言模型，具备持续学习和自适应能力，帮助用户在复杂任务中实现更高效的工作流。

### 2. 核心功能
- 支持多模型切换（Claude、ChatGPT/Codex 等），灵活适配不同需求
- 提供智能体自主决策与任务执行能力
- 具备持续学习能力，随使用不断进化优化
- 兼容 Nous Research 开源模型生态
- 模块化架构，易于扩展和定制

### 3. 适用场景
- **代码开发与调试**：辅助编写、审查和优化代码
- **复杂任务自动化**：执行多步骤工作流，提升效率
- **AI 研究实验**：作为 LLM 应用开发的测试框架
- **个性化助手**：根据用户习惯定制专属 AI 代理

### 4. 技术亮点
- 23万+ 星标，社区活跃度高，生态成熟
- 同时支持 Anthropic Claude 和 OpenAI 系列模型，跨平台兼容性强
- 基于 Nous Research 开源模型，可本地部署，隐私友好
- 模块化设计，便于二次开发和功能扩展
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 236203 | 🍴 47664 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，可自建部署或云端使用，提供 400+ 种集成。

### 2. 核心功能
- 可视化工作流编辑器，支持拖拽式流程设计
- 内置 AI 能力，支持智能自动化任务处理
- 400+ 种预置集成，覆盖主流 API 与服务
- 支持自建部署与云端托管两种模式
- 融合低代码与自定义代码开发，灵活度极高

### 3. 适用场景
- 企业自动化：连接多个系统，实现数据同步与业务流自动化
- AI 驱动工作流：结合大模型能力，构建智能助手与自动化决策流程
- 开发者工具链：通过 MCP 协议集成，统一管理 AI 客户端与服务端
- 数据流处理：跨平台数据整合、ETL 流程与 API 编排

### 4. 技术亮点
- 采用 TypeScript 开发，类型安全、可维护性强
- 支持 MCP（Model Context Protocol）协议，原生兼容 AI 客户端与服务端
- 公平代码（Fair-code）许可证，兼顾开放性与商业友好
- 强大的节点扩展机制，社区贡献活跃，集成生态丰富
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202370 | 🍴 60368 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI 工具，其使命是提供开箱即用的 AI 能力，让你专注于真正重要的事。

### 2. 核心功能
- **自主智能体**：无需人工干预即可自动完成复杂任务链。
- **多模型支持**：兼容 OpenAI、Claude、LLaMA 等多种大语言模型 API。
- **可扩展架构**：插件化设计，用户可自由定制和扩展功能。
- **目标驱动执行**：用户设定目标后，Agent 自动规划并执行步骤。
- **工具生态**：内置浏览器、代码执行、文件操作等常用工具。

### 3. 适用场景
- **自动化工作流**：如自动调研、数据整理、报告生成等重复性任务。
- **AI 应用开发**：作为构建自定义 AI 智能体的基础框架。
- **个人助理**：辅助完成日程管理、信息检索、邮件处理等日常事务。
- **教育与研究**：用于学习多智能体系统和自主 AI 的运行机制。

### 4. 技术亮点
- 社区活跃，星标数超 18 万，是 AI 智能体领域的标杆项目。
- 支持本地部署，数据隐私可控。
- 开源免费，生态丰富，文档完善。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186855 | 🍴 46050 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 172119 | 🍴 9517 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167889 | 🍴 21669 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164651 | 🍴 30554 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 158015 | 🍴 46171 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153656 | 🍴 9928 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

