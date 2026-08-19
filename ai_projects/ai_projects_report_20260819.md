# GitHub AI项目每日发现报告
日期: 2026-08-19

## 新发布的AI项目

### watermarks-remover
- 

# watermarks-remover 项目分析

## 1. 中文简介

该项目是一个用于移除多厂商AI溯源痕迹的工具，支持通过Unicode文本清理、统计重写技术以及C2PA/元数据剥离等方式，清除PNG、JPEG、SVG、PDF、DOCX、HTML和MD等格式文件中的AI生成标记。

## 2. 核心功能

- **Unicode文本清理**：移除嵌入在文件中的不可见Unicode水印字符
- **统计重写技术**：通过算法重构内容以消除AI生成的统计特征
- **C2PA元数据剥离**：清除符合C2PA标准的来源认证和溯源信息
- **多格式支持**：兼容图片、文档、网页和标记语言等多种文件格式
- **多平台兼容**：支持Claude、Codex、Grok等主流AI工具的溯源痕迹移除

## 3. 适用场景

- **内容创作者**：需要移除AI生成内容中的溯源标记以用于商业用途
- **研究人员**：分析或测试不同AI水印技术的检测与移除效果
- **企业用户**：清理由AI工具生成的文档和图片中的厂商标识
- **安全测试**：评估C2PA等溯源标准的实际防护能力

## 4. 技术亮点

- 采用多技术融合策略（文本层+统计层+元数据层）实现深度溯源痕迹清除
- 支持从884星标项目验证的社区关注度，涵盖主流AI平台的标签生态
- 链接: https://github.com/Leutenegger/watermarks-remover
- ⭐ 884 | 🍴 91 | 语言: Python
- 标签: claude, claude-code, claude-skills, codex, codex-cli

### sprix-sage-router
- 

# Sprix Sage Router 项目分析

## 1. 中文简介
Sprix Sage Router 是 Sprix AI 团队开发的智能体路由系统，支持状态感知的智能体间通信。它提供 SELF（自主处理）、COLLABORATE（协作处理）和 HANDOFF（移交处理）三种路由模式，用于 A2A 智能体网络的任务调度与编排。

## 2. 核心功能
- **状态感知路由**：根据当前系统状态动态选择最优的智能体路由策略
- **三种路由模式**：支持自主处理（SELF）、多智能体协作（COLLABORATE）和任务移交（HANDOFF）
- **智能体编排**：管理和调度多智能体网络中的任务分配与执行
- **A2A 协议支持**：兼容 Agent-to-Agent 通信标准，实现智能体间高效交互
- **任务调度优化**：智能分配任务给最适合的智能体节点

## 3. 适用场景
- **多智能体协作系统**：需要多个 AI 智能体协同完成复杂任务的场景
- **动态任务分发**：根据任务状态和智能体负载实时调整路由策略
- **智能体网络编排**：构建和管理大规模 A2A 智能体网络
- **跨智能体任务移交**：当一个智能体无法独立完成时，将任务移交给其他智能体

## 4. 技术亮点
- 基于状态的智能路由算法，可根据实时情况动态调整策略
- 支持三种路由模式，灵活应对不同任务需求
- 与 A2A 协议兼容，便于集成到现有智能体生态中
- 链接: https://github.com/wang2122/sprix-sage-router
- ⭐ 457 | 🍴 10 | 语言: Python
- 标签: a2a, agent-orchestration, agent-routing, ai-agents, multi-agent-systems

### llm-rag-memory-ai-agents
- 

# GitHub项目分析：llm-rag-memory-ai-agents

## 1. 中文简介
这是一个基于大语言模型（LLM）、检索增强生成（RAG）和AI智能体（Agents）的Python项目，旨在为AI系统提供记忆能力和知识库检索功能，构建更智能的对话代理。

## 2. 核心功能
- 集成LLM实现智能对话与推理能力
- 利用RAG技术实现知识库检索与增强生成
- 提供持久化记忆存储，支持上下文连续对话
- 构建AI智能体，实现自主任务执行
- 支持多轮对话中的信息记忆与检索

## 3. 适用场景
- 智能客服系统，实现知识库问答与用户记忆
- 个人助理应用，跨会话记忆用户偏好与历史
- 企业知识管理，基于文档的智能检索与回答
- 对话式AI应用，需要长期记忆能力的场景

## 4. 技术亮点
- 融合了RAG与Memory机制，提升AI对话的连贯性与准确性
- 支持LLM与外部知识库的无缝集成
- 架构灵活，可适配多种AI应用场景
- 链接: https://github.com/turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents
- ⭐ 85 | 🍴 0 | 语言: Python

### boujoy-harness
- 

# GitHub 项目分析：boujoy-harness

## 1. 中文简介

boujoy-harness 是一款支持知识库关联的本地 AI 工具，原生支持 macOS 系统，并提供 Windows Beta 启动器。该项目允许用户在本地环境中运行 AI 模型，并集成个人知识数据，实现更精准的本地化 AI 交互体验。

## 2. 核心功能

- **知识库链接**：支持将个人知识库与 AI 模型关联，实现基于私有数据的智能问答
- **macOS 原生支持**：为 macOS 用户提供开箱即用的完整运行环境
- **Windows Beta 启动器**：提供 Windows 平台的测试版启动器，扩展跨平台覆盖
- **本地 AI 运行**：在本地设备上运行 AI 模型，保障数据隐私与安全
- **JavaScript 技术栈**：采用 JavaScript 开发，便于社区贡献与二次开发

## 3. 适用场景

- **个人知识管理**：将笔记、文档等私有知识与 AI 结合，实现智能检索与问答
- **隐私敏感场景**：在本地运行 AI，避免数据上传云端，适用于企业或个人隐私保护需求
- **开发者工具链**：JavaScript 技术栈适合前端/全栈开发者快速集成与定制
- **跨平台 AI 实验**：macOS 与 Windows 双平台支持，便于不同环境下的 AI 应用测试

## 4. 技术亮点

- 项目采用知识库链接架构，将本地数据与 AI 推理能力有机结合
- 提供跨平台支持策略，macOS 正式版与 Windows Beta 版并行推进
- 基于 JavaScript 生态，开发门槛低，易于扩展和集成到现有工作流中
- 链接: https://github.com/asen-goat-mine/boujoy-harness
- ⭐ 66 | 🍴 13 | 语言: JavaScript

### emotion-ball
- 

# 项目分析：emotion-ball

## 1. 中文简介
这是一个 Grok 机器人风格的 AI 情绪小球组件，提供 32 种丰富的 SVG 表情状态，支持鼠标注视跟随和明暗主题切换。开发者只需传入一个 emotionId 即可快速接入 AI 情绪交互功能，并附带双语展示站点。

## 2. 核心功能
- 32 种 SVG 表情状态，覆盖丰富的情绪表达
- 鼠标注视跟随效果，增强交互沉浸感
- 支持明暗双主题切换，适配不同使用场景
- 仅需传入 emotionId 即可快速接入 AI 情绪系统
- 附带双语展示站点，方便集成参考

## 3. 适用场景
- AI 聊天机器人界面中的情绪可视化展示
- 桌面宠物类应用的表情交互组件
- 情感计算或情绪识别项目的可视化输出
- Web 应用中需要增强用户情感交互的嵌入式组件

## 4. 技术亮点
- 纯 JavaScript + SVG 实现，零依赖，轻量高效
- 通过 emotionId 实现情绪状态快速切换，接口简洁易用
- 支持鼠标 gaze 追踪，提升用户交互体验
- 明暗主题自适应，兼容不同 UI 风格需求
- 链接: https://github.com/sam70361/emotion-ball
- ⭐ 66 | 🍴 4 | 语言: JavaScript
- 标签: ai, ai-agent, animation, bot, chatbot

### oc
- 描述: Turn any website into a compact CLI tailored for AI agents. Browse the web in hundreds of tokens, not tens of thousands.
- 链接: https://github.com/only-cli/oc
- ⭐ 53 | 🍴 1 | 语言: JavaScript
- 标签: ai-agents, browser-automation, claude-code, cli, cli-app

### ai_agents_event
- 描述: 无描述
- 链接: https://github.com/LIDR-academy/ai_agents_event
- ⭐ 39 | 🍴 86 | 语言: Python

### ai-desktop-pet-2026
- 描述: Puts a live AI-powered animated pet on your Windows desktop. Your pet walks on windows, reacts to your mouse and typing, chases the cursor, and talks back when clicked.
- 链接: https://github.com/prestigioush/ai-desktop-pet-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, ai, animated, cat, chat

### cs2-external-aimbot-2026
- 描述: External aimbot for CS2. Reads game memory externally with no injection. Smooth aim, adjustable FOV, recoil control, and VAC bypass on current patch.
- 链接: https://github.com/darlingpret/cs2-external-aimbot-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, aimbot, bypass, cheat, cs2

### davinci-resolve-studio-crack-2026
- 描述: Activates DaVinci Resolve Studio — the paid version. Unlocks HDR grading tools, noise reduction, Neural Engine AI effects, Collaboration mode, and 4K+ export.
- 链接: https://github.com/surprisedgrou/davinci-resolve-studio-crack-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, 4k, crack, davinci, free

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP是一个全面的中英文自然语言处理资源集合，涵盖敏感词检测、实体抽取、情感分析、知识图谱构建、预训练语言模型及对话系统等丰富的NLP工具和资源，适合中文NLP开发与研究使用。

## 2. 核心功能
- **基础NLP工具**：敏感词检测、语言识别、手机号/身份证/邮箱抽取、分词、词性标注、句法分析等
- **丰富词库资源**：中英文词向量、停用词、同义词/反义词库、情感词库、地名/人名/职业词库等
- **预训练模型集合**：BERT、GPT-2、ALBERT、ELECTRA等中文预训练语言模型及微调代码
- **知识图谱相关**：实体链接、关系抽取、知识图谱问答系统构建工具
- **对话与生成**：聊天机器人、问答系统、文本摘要、关键词抽取等

## 3. 适用场景
- **中文NLP项目开发**：快速集成分词、NER、情感分析等基础功能
- **知识图谱构建**：提供实体抽取、关系抽取、知识问答的完整方案
- **对话系统开发**：提供闲聊机器人、任务型对话、多轮对话等解决方案
- **NLP研究与学习**：提供大量中文数据集、论文、教程和基准测评

## 4. 技术亮点
- 集成多种主流预训练模型（BERT、GPT-2、ALBERT、ELECTRA等），支持中文微调与部署
- 涵盖NLP全链路：从数据处理、模型训练到应用部署的完整工具链
- 提供丰富的中文专用资源：包括1.4亿实体知识图谱、中文谣言数据库、医疗/金融领域专项数据等
- 支持多种NLP任务：文本分类、序列标注、生成任务、语音识别、OCR等，覆盖场景广泛
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82547 | 🍴 15266 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个汇集了500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目为开发者提供了丰富的实战案例，帮助快速学习和应用AI技术。

### 2. 核心功能
- 提供500个AI项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大技术领域
- 包含多个热门AI方向的项目案例
- 适合不同水平的开发者学习与参考
- 所有项目均附带可运行的代码

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习项目
- 开发者寻找计算机视觉或NLP项目灵感
- 研究人员快速搭建AI原型进行实验验证
- 企业团队进行AI技术选型和方案参考

### 4. 技术亮点
- 项目数量丰富，涵盖主流AI技术方向
- 所有项目均提供完整代码，可直接运行学习
- 标签分类清晰，便于快速定位所需领域
- 高星标数（36389）表明社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36389 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够以图形化方式展示模型结构和数据流向，帮助开发者直观理解和分析模型。

## 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 提供直观的模型架构图和层结构可视化展示
- 支持查看模型参数、张量形状和计算图
- 可在浏览器或桌面端运行，无需安装额外依赖
- 支持 safetensors 等新兴模型格式

## 3. 适用场景
- 深度学习模型调试与结构审查
- 模型转换前后的结构对比验证
- 教学演示中展示神经网络工作原理
- 部署前检查模型层配置和参数

## 4. 技术亮点
Netron 以纯 JavaScript 实现，无需后端服务即可本地运行，支持离线查看模型文件，跨平台兼容性强，是 AI 开发者社区中最受欢迎的模型可视化工具之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33369 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21331 | 🍴 4003 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# 项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的开源指南。内容涵盖从模型训练、调试到大规模推理部署的完整工程链路，是AI工程师的实用参考书。

## 2. 核心功能
- 提供基于PyTorch的大规模语言模型训练与微调实践指南
- 详解GPU集群管理、Slurm调度与分布式训练优化策略
- 覆盖模型推理优化、存储系统与网络通信的工程解决方案
- 包含LLM调试、可扩展性设计与MLOps生产部署的最佳实践

## 3. 适用场景
- 需要在多GPU集群上训练或微调大型语言模型（LLM）的工程师
- 负责构建和维护机器学习生产管道的MLOps团队
- 优化模型推理性能与部署成本的数据科学家
- 研究大规模分布式训练系统架构的AI研究人员

## 4. 技术亮点
- 聚焦真实生产环境中的工程挑战，而非仅停留在理论层面
- 涵盖从底层硬件（GPU、网络、存储）到上层框架（Transformers、PyTorch）的全栈知识
- 针对大语言模型（LLM）时代的新问题提供针对性解决方案
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18656 | 🍴 1202 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17371 | 🍴 2123 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13268 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11628 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10689 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个汇集了500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目为开发者提供了丰富的实战案例，帮助快速学习和应用AI技术。

### 2. 核心功能
- 提供500个AI项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大技术领域
- 包含多个热门AI方向的项目案例
- 适合不同水平的开发者学习与参考
- 所有项目均附带可运行的代码

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习项目
- 开发者寻找计算机视觉或NLP项目灵感
- 研究人员快速搭建AI原型进行实验验证
- 企业团队进行AI技术选型和方案参考

### 4. 技术亮点
- 项目数量丰富，涵盖主流AI技术方向
- 所有项目均提供完整代码，可直接运行学习
- 标签分类清晰，便于快速定位所需领域
- 高星标数（36389）表明社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36389 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够以图形化方式展示模型结构和数据流向，帮助开发者直观理解和分析模型。

## 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 提供直观的模型架构图和层结构可视化展示
- 支持查看模型参数、张量形状和计算图
- 可在浏览器或桌面端运行，无需安装额外依赖
- 支持 safetensors 等新兴模型格式

## 3. 适用场景
- 深度学习模型调试与结构审查
- 模型转换前后的结构对比验证
- 教学演示中展示神经网络工作原理
- 部署前检查模型层配置和参数

## 4. 技术亮点
Netron 以纯 JavaScript 实现，无需后端服务即可本地运行，支持离线查看模型文件，跨平台兼容性强，是 AI 开发者社区中最受欢迎的模型可视化工具之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33369 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub项目分析：cheatsheets-ai

### 1. 中文简介
这是为深度学习和机器学习研究人员精心整理的必备速查表集合。内容涵盖从基础理论到实用工具的全方位参考，帮助研究者快速查阅关键概念与公式。

### 2. 核心功能
- 提供深度学习与机器学习核心概念的速查参考表
- 涵盖Keras、NumPy、SciPy、Matplotlib等主流工具库的使用指南
- 整理常用数学公式、算法流程和最佳实践
- 内容结构清晰，便于快速定位所需信息

### 3. 适用场景
- 深度学习研究人员查阅算法公式和模型架构参考
- 机器学习工程师日常开发中快速查找库函数用法
- 学生系统学习或复习深度学习知识体系

### 4. 技术亮点
- 整合了多个核心AI框架与科学计算库的实用技巧，内容精炼实用，适合作为桌面速查手册。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# Ai-Learn 项目分析

## 1. 中文简介
Ai-Learn 是一套系统的人工智能学习路线图，收录近200个实战案例与项目，配套免费教材，帮助零基础学习者快速入门并掌握就业技能。项目覆盖Python编程、数学基础、机器学习、数据分析、深度学习、计算机视觉、自然语言处理等热门技术领域。

## 2. 核心功能
- 提供完整AI学习路径规划，从入门到进阶循序渐进
- 收录近200个实战案例与项目，注重动手实践
- 免费提供配套学习教材，降低学习成本
- 覆盖机器学习、深度学习、NLP、CV等多方向技术栈
- 支持多种主流框架（PyTorch、TensorFlow、Keras等）

## 3. 适用场景
- 零基础转行AI领域的学习者规划学习路线
- 在校学生系统学习机器学习与深度学习知识
- 求职者准备AI岗位面试与实战项目经验
- 工程师拓展技术栈，学习计算机视觉或自然语言处理

## 4. 技术亮点
- 项目标签涵盖从基础（numpy、pandas）到进阶（pytorch、tensorflow2）的完整技术链
- 整合了算法、数据挖掘、数据可视化（matplotlib、seaborn）等实用工具
- 兼顾理论（数学）与实践（实战案例），学习体系较为全面
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13268 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码深度学习框架，专为快速构建自定义大语言模型、神经网络及其他 AI 模型而设计。它简化了模型训练流程，让开发者无需编写大量代码即可完成从数据处理到模型部署的全链路操作。

## 2. 核心功能
- 支持多种数据模态：文本、图像、表格、音频等
- 内置预训练模型，支持 LLaMA、Llama2、Mistral 等大语言模型微调
- 提供可视化训练界面，实时监控模型训练过程
- 自动超参数搜索与模型调优
- 支持 PyTorch 后端，兼容主流深度学习生态

## 3. 适用场景
- **快速原型开发**：无需编写复杂代码，快速验证 AI 模型想法
- **大模型微调**：对 LLaMA、Mistral 等开源模型进行领域适配
- **多模态应用**：构建同时处理文本和图像的智能系统
- **数据驱动实验**：通过可视化界面探索不同模型架构的效果

## 4. 技术亮点
- 低代码设计大幅降低深度学习入门门槛
- 原生支持主流开源大模型（LLaMA、Mistral 等）的微调流程
- 内置自动机器学习（AutoML）功能，简化模型选择与调参
- 与 Hugging Face 生态无缝集成，便于加载和使用预训练模型
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9177 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8965 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6990 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6415 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP是一个全面的中英文自然语言处理资源集合，涵盖敏感词检测、实体抽取、情感分析、知识图谱构建、预训练语言模型及对话系统等丰富的NLP工具和资源，适合中文NLP开发与研究使用。

## 2. 核心功能
- **基础NLP工具**：敏感词检测、语言识别、手机号/身份证/邮箱抽取、分词、词性标注、句法分析等
- **丰富词库资源**：中英文词向量、停用词、同义词/反义词库、情感词库、地名/人名/职业词库等
- **预训练模型集合**：BERT、GPT-2、ALBERT、ELECTRA等中文预训练语言模型及微调代码
- **知识图谱相关**：实体链接、关系抽取、知识图谱问答系统构建工具
- **对话与生成**：聊天机器人、问答系统、文本摘要、关键词抽取等

## 3. 适用场景
- **中文NLP项目开发**：快速集成分词、NER、情感分析等基础功能
- **知识图谱构建**：提供实体抽取、关系抽取、知识问答的完整方案
- **对话系统开发**：提供闲聊机器人、任务型对话、多轮对话等解决方案
- **NLP研究与学习**：提供大量中文数据集、论文、教程和基准测评

## 4. 技术亮点
- 集成多种主流预训练模型（BERT、GPT-2、ALBERT、ELECTRA等），支持中文微调与部署
- 涵盖NLP全链路：从数据处理、模型训练到应用部署的完整工具链
- 提供丰富的中文专用资源：包括1.4亿实体知识图谱、中文谣言数据库、医疗/金融领域专项数据等
- 支持多种NLP任务：文本分类、序列标注、生成任务、语音识别、OCR等，覆盖场景广泛
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82547 | 🍴 15266 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行微调，相关研究发表于 ACL 2024。

### 2. 核心功能
- 支持 100+ 种主流大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、P-Tuning 等多种高效微调方法
- 支持 RLHF（基于人类反馈的强化学习）对齐训练
- 支持量化部署，降低显存占用
- 提供简洁的命令行接口和 Web 界面

### 3. 适用场景
- 快速微调 Llama、Qwen、DeepSeek、Gemma 等开源模型
- 对大语言模型进行指令微调（Instruction Tuning）
- 在有限显存条件下进行模型微调（QLoRA 场景）
- 构建多模态视觉语言模型应用

### 4. 技术亮点
- 统一框架支持多模型、多任务，无需重复编写代码
- 基于 Hugging Face Transformers 和 PEFT 库，生态兼容性好
- 支持 MoE（混合专家）架构模型的高效训练
- ACL 2024 学术论文背书，具备学术研究价值
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74232 | 🍴 9078 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一个由微软推出的AI入门课程项目，采用"12周24课时"的结构化设计，面向所有学习者开放。项目通过Jupyter Notebook提供交互式学习体验，帮助零基础用户系统掌握人工智能核心知识。

## 2. 核心功能
- 提供系统化的12周AI学习路径，涵盖机器学习与深度学习基础
- 包含计算机视觉（CNN）、自然语言处理（NLP）、生成对抗网络（GAN）等专题课程
- 通过RNN等经典架构讲解深度学习核心概念
- 所有课程代码以Jupyter Notebook形式呈现，支持交互式实践

## 3. 适用场景
- 高校或培训机构用于AI入门课程教学
- 个人学习者从零开始系统学习人工智能
- 企业内训中作为AI基础培训材料
- 转行人员快速掌握AI核心技能

## 4. 技术亮点
- 微软官方出品，课程质量与权威性有保障
- 65,664颗星标反映其广泛社区认可度
- 模块化课程设计，适合不同学习节奏
- 理论与实践结合，每课均配有可运行的代码示例
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65664 | 🍴 12728 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## 项目分析：ai-engineering-from-scratch

### 1. 中文简介
从零开始学习AI工程，亲手构建并部署给他人使用。这是一个系统性的AI工程教程项目，涵盖从基础理论到实际应用的完整学习路径。

### 2. 核心功能
- **AI代理与LLM开发**：涵盖智能代理、大语言模型构建与部署
- **计算机视觉与NLP**：提供视觉处理和自然语言处理的实战教程
- **强化学习与群体智能**：包含强化学习和群体智能算法的实现
- **生成式AI实战**：讲解生成式AI模型的开发与应用
- **多语言支持**：同时使用Python和Rust进行工程实现

### 3. 适用场景
- AI工程师系统学习从零构建AI系统的完整流程
- 开发者学习AI代理、MCP协议等前沿技术
- 学生或转行者深入理解机器学习到部署的全链路
- 团队内部培训AI工程最佳实践

### 4. 技术亮点
- 强调"Learn it. Build it. Ship it."的实战驱动学习理念
- 覆盖agents、transformers、swarm-intelligence等热门技术方向
- 结合MCP（模型上下文协议）等现代AI工程标准
- 使用Rust实现高性能组件，Python快速原型开发
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47211 | 🍴 8291 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub项目分析：ailearning

### 1. 中文简介
AiLearning 是一个全面的机器学习与数据分析学习资源库，涵盖数据分析实战、机器学习算法、线性代数、PyTorch、NLTK 以及 TensorFlow 2 等内容。该项目以 Python 为主要语言，适合从入门到进阶的系统性学习。

### 2. 核心功能
- 提供数据分析与机器学习算法的实战代码示例
- 涵盖线性代数等数学基础知识的讲解与实现
- 集成 PyTorch 和 TensorFlow 2 深度学习框架的实践教程
- 包含 NLTK 自然语言处理库的应用案例
- 实现经典算法如 SVM、KMeans、Adaboost、朴素贝叶斯等

### 3. 适用场景
- 机器学习初学者系统学习算法原理与代码实现
- 数据分析工程师巩固基础并提升实战能力
- 深度学习爱好者实践 PyTorch 和 TensorFlow 2
- NLP 学习者使用 NLTK 进行文本处理练习

### 4. 技术亮点
- 项目星标数达 42464，说明社区认可度较高
- 内容覆盖全面，从数学基础到深度学习框架均有涉及
- 标签丰富，涵盖主流算法（SVM、RNN、LSTM、PCA、SVD 等）和热门领域（NLP、推荐系统、深度学习）
- 结合 scikit-learn 与主流深度学习框架，兼顾经典 ML 与深度学习实践
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42464 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36389 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33833 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29123 | 🍴 3544 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21842 | 🍴 3356 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17371 | 🍴 2123 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个收录了500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的代码仓库，涵盖广泛的技术领域和实践案例，适合从入门到进阶的学习者使用。

### 2. 核心功能
- 收录500个AI/ML/DL相关项目，涵盖计算机视觉、NLP、数据科学等多个方向
- 提供完整的项目代码实现，方便学习者直接参考和运行
- 涵盖从基础到进阶的多种算法和模型实践
- 以Python为主要编程语言，适合机器学习领域开发者
- 标签分类清晰，便于按技术领域快速查找相关项目

### 3. 适用场景
- 机器学习/AI初学者系统学习和实践项目参考
- 计算机视觉或NLP方向的开发者寻找项目灵感和代码示例
- 数据科学家用于快速上手不同领域的AI项目
- 学生或研究人员作为课程作业或科研项目的参考资源

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI领域主流技术栈
- 全部附带代码实现，而非仅理论介绍，实用性强
- 标签体系完善，涵盖artificial-intelligence、computer-vision、deep-learning、nlp等核心关键词，便于检索
- 星标数高达36389，说明社区认可度极高，是AI领域知名的Awesome列表类项目
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36389 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一个基于人工智能的浏览器自动化平台，能够智能地执行基于浏览器的工作流。它利用大型语言模型和计算机视觉技术，让浏览器操作像人类一样思考和执行任务，无需编写复杂的自动化脚本。

### 2. 核心功能
- 支持通过自然语言指令驱动浏览器自动化操作
- 集成 Playwright 浏览器引擎，实现智能页面交互和数据提取
- 提供 API 接口，便于集成到现有业务流程中
- 结合 LLM 与视觉识别技术，理解网页元素并做出决策
- 兼容主流 RPA 工具，支持与 Power Automate 等系统集成

### 3. 适用场景
- 自动化重复性网页操作（如表单填写、数据录入、批量处理）
- 电商平台的价格监控、库存管理和订单处理
- 企业数据抓取、报表生成和信息整合
- 跨系统工作流自动化，替代传统人工操作流程

### 4. 技术亮点
- 将大语言模型与计算机视觉相结合，实现"看懂页面、理解意图、自主操作"的智能自动化
- 无需预设选择器或编写复杂脚本，降低自动化开发门槛
- 开源项目，社区活跃，持续迭代更新
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22791 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一款领先的开源平台，用于构建高质量的视觉数据集以支持视觉AI开发。它提供开源、云端及企业级产品，支持图像、视频和3D标注，并集成AI辅助标注、质量保证、团队协作和开发者API等功能。

### 2. 核心功能
- 支持图像、视频和3D数据的多种标注类型（边界框、多边形、语义分割等）
- AI辅助标注功能，可大幅减少人工标注工作量
- 团队协作与质量保证机制，支持多人协同标注和审核
- 提供分析仪表盘和开发者API，便于集成到现有工作流
- 支持主流深度学习框架（PyTorch、TensorFlow）的数据格式导出

### 3. 适用场景
- 计算机视觉模型训练前的数据集标注与准备
- 目标检测、图像分类、语义分割等任务的数据标注
- 团队大规模协作标注项目，需要质量管控的场景
- 需要与自动化标注管线集成的AI研发流程

### 4. 技术亮点
- 开源免费，社区活跃（16550+星标），生态成熟
- 支持从ImageNet等主流数据集格式导入导出
- 提供云端部署和企业级支持选项，灵活适配不同规模团队需求
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16550 | 🍴 3804 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## GitHub 项目分析：pytorch-grad-cam

### 1. 中文简介
本项目是一个面向计算机视觉的高级 AI 可解释性工具库。支持 CNN、视觉 Transformer 等多种模型架构，涵盖分类、目标检测、图像分割、图像相似度分析等多种任务。

### 2. 核心功能
- 支持 Grad-CAM、Grad-CAM++、Score-CAM 等多种可视化解释方法
- 兼容卷积神经网络（CNN）和视觉 Transformer（ViT）架构
- 适用于图像分类、目标检测、语义分割和图像相似度等多种任务
- 提供直观的注意力热力图可视化，帮助理解模型决策依据
- 基于 PyTorch 框架实现，易于集成到现有项目中

### 3. 适用场景
- 深度学习模型调试：定位模型关注区域，发现误判原因
- 医学影像分析：辅助医生理解 AI 诊断依据，提升可信度
- 自动驾驶感知系统：可视化模型对道路场景的关注点
- 学术研究与教学：展示模型内部决策机制，增强可解释性

### 4. 技术亮点
- 项目星标超过 12,900，是 PyTorch 生态中最受欢迎的可解释性工具之一
- 统一接口支持多种 CAM 变体，无需重复编写代码
- 对 Vision Transformer 等新兴架构提供原生支持，紧跟技术前沿
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

**中文简介**
Kornia 是一个基于 PyTorch 的可微分几何计算机视觉库，专为空间 AI 应用设计。它提供了一套完整的
- 链接: https://github.com/kornia/kornia
- ⭐ 11316 | 🍴 1225 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3480 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3384 | 🍴 414 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2508 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

# OpenClaw 项目分析

## 1. 中文简介
OpenClaw 是一款个人AI助手工具，支持任意操作系统和平台运行。它采用"龙虾方式"（lobster way）让您完全掌控自己的数据，实现真正私有的AI助手体验。

## 2. 核心功能
- 跨平台部署，支持任意操作系统运行
- 本地数据完全自主掌控，不依赖第三方云服务
- 提供个人AI助手功能，支持多种交互场景
- 基于TypeScript构建，具备良好的可扩展性

## 3. 适用场景
- 注重数据隐私的用户，希望AI助手本地运行
- 需要跨平台一致体验的个人开发者
- 希望自定义AI助手功能的进阶用户

## 4. 技术亮点
- 采用TypeScript开发，类型安全且生态丰富
- 强调"own-your-data"理念，数据完全本地化存储
- 跨平台架构设计，一次开发多端运行

---
**项目信息**：星标 386,804 | 语言：TypeScript | 标签：AI助手、数据自主、跨平台
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386804 | 🍴 81264 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

## 1. 中文简介
这是一个经过验证的AI代理技能框架与软件开发方法论。它提供了一套实用的代理驱动开发体系，帮助团队高效完成软件开发全流程。

## 2. 核心功能
- 提供AI代理技能框架，支持自动化软件开发任务
- 集成头脑风暴与编码辅助功能，提升开发效率
- 采用子代理驱动开发模式，实现任务分解与并行执行
- 覆盖完整SDLC（软件开发生命周期），支持从规划到交付的全流程
- 基于OBRA方法论，提供结构化的开发工作流

## 3. 适用场景
- AI辅助的软件项目规划与需求分析
- 需要快速原型开发的敏捷团队
- 希望通过代理自动化提升编码效率的开发人员
- 采用子代理驱动开发模式的大型项目协作

## 4. 技术亮点
- 基于Shell语言实现，轻量级且易于集成到现有工作流
- 采用子代理驱动开发（Subagent-Driven Development）模式，实现任务智能分解
- 将AI代理技能与经典SDLC方法论相结合，兼具创新性与实用性
- 链接: https://github.com/obra/superpowers
- ⭐ 274212 | 🍴 24550 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
hermes-agent 是一款与你共同成长的 AI 智能体，能够持续学习并适应用户的使用习惯。该项目由 Nous Research 开发，支持接入多种主流大语言模型（如 Claude、GPT 等），为用户提供灵活且个性化的 AI 交互体验。

### 2. 核心功能
- **多模型支持**：兼容 Anthropic Claude、OpenAI GPT 等多个主流大语言模型
- **智能体记忆**：具备持续学习能力，可随使用不断优化交互体验
- **代码辅助**：支持代码生成、调试与优化等开发辅助功能
- **灵活部署**：基于 Python 构建，易于集成到现有工作流中

### 3. 适用场景
- 开发者日常编码辅助与代码审查
- 需要跨模型切换的 AI 研究或对比实验
- 追求个性化、持续进化的 AI 助手场景

### 4. 技术亮点
- 由 Nous Research 团队打造，在开源社区拥有较高关注度（23万+星标）
- 支持多种 LLM 后端，具备较高的可扩展性和灵活性
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233017 | 🍴 46597 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

# n8n 项目分析

## 1. 中文简介
n8n 是一个公平代码（fair-code）工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，可自托管或云端部署，提供 400+ 种集成，适用于低代码/无代码开发场景。

## 2. 核心功能
- **可视化工作流构建**：通过拖拽节点快速创建自动化流程
- **原生 AI 集成**：内置 AI 能力，支持智能自动化决策
- **400+ 应用集成**：覆盖主流 SaaS 工具、API 和数据源
- **灵活部署**：支持自托管和云端两种模式
- **MCP 协议支持**：兼容 Model Context Protocol，可连接 AI 模型

## 3. 适用场景
- **企业自动化**：跨系统数据同步、邮件通知、日程管理等办公自动化
- **AI 应用开发**：构建基于大模型的智能工作流和 Agent 系统
- **数据管道**：ETL 数据处理、API 聚合、定时任务调度
- **低代码平台**：非技术人员也能快速搭建业务自动化流程

## 4. 技术亮点
- 基于 TypeScript 开发，代码质量高、类型安全
- 支持 MCP 协议（MCP Client/Server），便于扩展 AI 连接
- 公平代码许可，核心功能开源，兼顾社区与企业需求
- 高度可扩展，支持自定义节点和代码执行
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201206 | 🍴 60227 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186689 | 🍴 46050 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 169607 | 🍴 9461 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167589 | 🍴 21639 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164584 | 🍴 30551 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157890 | 🍴 46173 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153479 | 🍴 9895 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

