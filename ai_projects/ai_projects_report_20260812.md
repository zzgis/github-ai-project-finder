# GitHub AI项目每日发现报告
日期: 2026-08-12

## 新发布的AI项目

### watermarks-remover
- 

# GitHub项目分析：watermarks-remover

## 1. 中文简介
该项目用于清除多供应商AI来源标记，支持Unicode文本清理、统计重写钩子以及C2PA/元数据移除，可处理PNG、JPEG、SVG、PDF、DOCX、HTML和MD等多种格式文件。

## 2. 核心功能
- 清除多供应商AI来源标识和合成水印
- 支持Unicode文本层面的清理和重写
- 提供统计重写钩子以修改文件特征
- 移除C2PA内容来源和版权信息
- 支持图片、文档、网页等多种文件格式

## 3. 适用场景
- AI生成内容的去水印处理
- 批量清除文件中的来源追踪标记
- 文档格式转换中的元数据清理
- 内容再利用前的来源信息去除

## 4. 技术亮点
- 支持多格式统一处理（图片/文档/网页）
- 结合Unicode文本处理与统计重写技术
- 专门针对C2PA等新兴内容来源标准进行移除
- 链接: https://github.com/guillaumemeyer/watermarks-remover
- ⭐ 2107 | 🍴 199 | 语言: Python
- 标签: agent-skill, ai, c2pa, claude, provenance

### chatbot-template
- 

## 项目分析：chatbot-template

### 1. 中文简介
这是一个基于 Next.js 构建的极简聊天机器人模板，集成了 AI SDK 和 shadcn/ui 组件库，运行在 Vercel AI Gateway 之上。该项目为开发者提供了一个快速搭建 AI 对话应用的起点。

### 2. 核心功能
- 基于 Next.js 框架的现代化 Web 应用架构
- 集成 Vercel AI SDK 实现 AI 对话能力
- 采用 shadcn/ui 组件库提供美观的 UI 界面
- 通过 Vercel AI Gateway 统一管理 AI 模型调用
- 支持 TypeScript 类型安全开发

### 3. 适用场景
- 快速搭建 AI 客服机器人原型
- 构建企业级智能问答系统
- 学习 Next.js 与 AI SDK 的整合开发
- 开发个性化 AI 助手应用

### 4. 技术亮点
- 使用 shadcn/ui 组件库，可自由定制样式
- 依托 Vercel AI Gateway 实现多模型路由和统一管理
- 极简架构便于二次开发和扩展
- TypeScript 全栈开发保障代码质量
- 链接: https://github.com/shadcn-ui/chatbot-template
- ⭐ 575 | 🍴 51 | 语言: TypeScript

### DramaLens
- 

## DramaLens 项目分析

### 1. 中文简介
DramaLens 是一款本地优先的 Chrome 浏览器扩展，专注于带时间戳的语音转录与人工审核的短剧内容分析。该工具结合 AI 语音识别技术，帮助用户高效处理短视频/短剧的文本化与内容分析工作。

### 2. 核心功能
- **本地优先处理**：所有语音转录和分析均在本地完成，保障用户数据隐私安全
- **带时间戳的语音转文字**：自动将音频/视频内容转录为带精确时间戳的文本
- **人工审核机制**：支持用户对 AI 转录结果进行人工校对和修改
- **短剧内容分析**：针对短剧/短视频形式的内容进行结构化分析
- **中文优化支持**：针对中文语音内容进行了专项优化

### 3. 适用场景
- **短视频/短剧创作者**：快速生成带时间戳的字幕和剧本文本
- **内容运营团队**：批量转录和分析短剧内容，提升工作效率
- **中文语音资料整理**：对中文音频/视频内容进行本地化转录和存档
- **敏感内容处理**：需要本地处理、不外传音频数据的场景

### 4. 技术亮点
- 采用 **faster-whisper** 引擎，在保持高识别精度的同时显著提升处理速度
- **本地优先架构** 确保音频数据不上传云端，有效保护用户隐私
- **人机协作流程** 将 AI 自动转录与人工审核相结合，兼顾效率与准确性
- 链接: https://github.com/dengzi008/DramaLens
- ⭐ 86 | 🍴 0 | 语言: JavaScript
- 标签: ai, chinese, chrome-extension, faster-whisper, local-first

### md2hd
- 描述: Markdown, mapped - the MD2HD CLI. Pull the repo, tell your agent to create an MD2HD map, visually comprehend complex topics and relationships.
- 链接: https://github.com/evan-steinhilb/md2hd
- ⭐ 65 | 🍴 10 | 语言: JavaScript
- 标签: ai, open-source

### knowledge-inbox
- 

## 项目分析：knowledge-inbox

### 1. 中文简介
这是一个本地优先的知识摄入工具，专为 AI 代理和 Obsidian 笔记软件设计。它帮助用户将分散的信息源（如微信消息）收集并结构化地导入到本地知识库中，实现知识的自动化管理。

### 2. 核心功能
- **本地优先架构**：所有数据存储在本地，确保隐私和数据安全
- **多源知识摄入**：支持从微信等渠道自动收集知识内容
- **AI 代理集成**：与 Hermes Agent 等 AI 代理无缝对接
- **Obsidian 兼容**：输出格式适配 Obsidian 笔记软件
- **MCP 协议支持**：通过 Model Context Protocol 实现标准化知识交互

### 3. 适用场景
- 个人知识管理：将微信收藏、聊天记录整理为结构化笔记
- AI 助手知识库：为本地 AI 代理构建专属知识上下文
- 信息归档：把碎片化信息自动同步到 Obsidian 知识库
- 隐私敏感场景：避免将个人知识数据上传到云端服务

### 4. 技术亮点
- 采用 **FastAPI** 构建高性能异步 API 服务
- 支持 **MCP（Model Context Protocol）** 标准协议，便于与各类 AI 工具集成
- **本地优先（Local-first）** 设计，数据完全掌控在用户手中
- 集成 **微信** 生态，降低知识收集门槛
- 链接: https://github.com/lyc403223157-source/knowledge-inbox
- ⭐ 63 | 🍴 0 | 语言: Python
- 标签: fastapi, hermes-agent, knowledge-management, local-first, mcp

### tokentab
- 描述: A CLI that reads Claude Code, Codex, and Gemini CLI session logs and works out how much they cost, by model, project, and day.
- 链接: https://github.com/wzchav/tokentab
- ⭐ 48 | 🍴 10 | 语言: Python
- 标签: ai, api, claude, claude-code, claude-tool

### ai-nuclear-spectroscopy
- 描述: An auditable human–AI workflow from NNDC/ENSDF data to gamma-ray GCD lifetime inference.
- 链接: https://github.com/JWP-p/ai-nuclear-spectroscopy
- ⭐ 41 | 🍴 1 | 语言: Python
- 标签: ai-for-science, ensdf, gamma-ray-spectroscopy, gcd-lifetime, nndc

### toolpermit
- 描述: A local-first permission firewall and approval layer for AI agent tool calls.
- 链接: https://github.com/sunhao123456sun-svg/toolpermit
- ⭐ 34 | 🍴 3 | 语言: Python
- 标签: ai-agents, ai-security, audit-logging, codex-plugin, local-first

### Adversarial-Testing-Skill
- 描述: Multi-AI collaborative adversarial testing workflow
- 链接: https://github.com/KieranHoward646/Adversarial-Testing-Skill
- ⭐ 32 | 🍴 0 | 语言: 未知

### ko5.6sol
- 描述: Master Anti-AI Academic Paper Refactoring & Style Guide Skill to KO GPT-5.6 SOL mechanical phrasing & defensive disclaimers
- 链接: https://github.com/handsomeZR-netizen/ko5.6sol
- ⭐ 30 | 🍴 1 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中文自然语言处理资源合集，涵盖了从基础工具（敏感词检测、分词、词性标注）到高级应用（知识图谱、对话系统、预训练模型）的完整生态。该项目整合了大量开源数据集、预训练模型、词库资源及NLP相关论文与代码，是中文NLP领域的重要资源库。

### 2. 核心功能
- **基础NLP工具**：提供中文分词、词性标注、命名实体识别、句法分析、情感分析等核心处理能力
- **丰富词库资源**：包含中日文人名库、中文缩写库、同义词库、反义词库、汽车品牌词库等各类专业词库
- **预训练模型集成**：汇集BERT、ALBERT、ELECTRA、RoBERTa等多种中文预训练语言模型及微调代码
- **知识图谱构建**：提供知识图谱抽取、实体链接、关系抽取、问答系统等完整知识图谱解决方案
- **多模态支持**：涵盖语音识别（ASR）、语音情感分析、OCR文字识别等跨模态NLP能力

### 3. 适用场景
- **企业内容审核**：利用敏感词库、暴恐词表、停用词表等实现自动化内容过滤
- **智能客服与对话系统**：基于对话数据集和 Rasa、ConvLab 等框架构建聊天机器人
- **信息抽取与知识图谱**：从文本中抽取实体、关系、事件，构建领域知识图谱
- **NLP研究与教学**：作为中文NLP学习资源库，包含课程资料、数据集、基准测评等

### 4. 技术亮点
- 项目星标数高达 **82,433**，是 GitHub 上最受欢迎的中文NLP资源库之一
- 整合了清华大学、百度、微软、Facebook 等机构的高质量开源资源
- 覆盖从传统NLP（HMM、CRF）到深度学习（BERT、Transformer）的完整技术栈
- 包含 CLUENER 细粒度命名实体识别、CLUE 中文语言理解测评基准等国内权威评测体系
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82433 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI Projects with Code

### 1. 中文简介
这是一个收录了500个AI项目代码的开源资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目以Awesome列表的形式整理，为学习者提供了丰富的实战案例和代码参考。

### 2. 核心功能
- 收录500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- 按主题分类整理，便于快速查找和学习
- 提供可直接运行的代码示例，支持实践操作
- 持续更新，保持项目库的时效性和丰富度

### 3. 适用场景
- AI初学者系统学习各方向项目实战
- 研究人员参考实现方案与代码结构
- 开发者寻找特定领域的项目灵感与模板
- 培训机构用于教学案例和作业布置

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流研究方向
- 所有项目均附带代码，可直接运行学习
- 标签分类清晰，便于按领域筛选
- 作为Awesome列表，质量经过社区筛选和认可
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36182 | 🍴 7426 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，帮助用户直观地查看和分析模型结构。该项目在 GitHub 上获得了超过 3.3 万星的关注，是 AI 领域最受欢迎的开源工具之一。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 Safetensors
- 提供直观的模型架构图可视化，清晰展示网络层结构和数据流向
- 支持在浏览器和本地桌面环境中运行，使用便捷
- 允许查看模型中的权重数据和层参数信息
- 兼容主流 AI 框架，包括 PyTorch、TensorFlow、Keras 和 ONNX 等

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：适合初学者直观理解各种神经网络结构
- 跨框架模型转换验证：验证不同框架间模型转换后的结构一致性
- 模型文档生成：为项目生成清晰的模型结构图作为技术文档

### 4. 技术亮点
- 纯前端实现，无需安装复杂的依赖环境，开箱即用
- 支持离线桌面应用和在线网页版两种使用方式
- 对 safetensors 等新兴模型格式提供良好支持，紧跟技术发展趋势
- 开源免费，社区活跃，持续维护更新
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33341 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是用于机器学习模型互操作性的开放标准。它允许开发者在不同深度学习框架之间无缝迁移模型，打破框架壁垒，实现"一次训练，多处运行"的目标。

### 2. 核心功能
- 提供统一的模型格式，支持跨框架模型交换
- 支持主流深度学习框架（PyTorch、TensorFlow、Keras等）的模型导入导出
- 提供模型转换工具链，实现不同框架间的格式转换
- 支持模型性能优化与推理加速

### 3. 适用场景
- 将PyTorch训练好的模型部署到生产环境（如ONNX Runtime）
- 在TensorFlow和PyTorch之间迁移模型，避免重复训练
- 移动端或边缘设备上的模型推理部署
- 跨平台模型共享与协作开发

### 4. 技术亮点
- 由微软和Facebook（Meta）联合发起，社区生态活跃
- 支持超过100种算子，覆盖主流神经网络结构
- 提供ONNX Checker和ONNX Simplifier等辅助工具，保障模型兼容性与优化
- 已被NVIDIA、Intel等硬件厂商广泛支持，适配多种推理引擎
- 链接: https://github.com/onnx/onnx
- ⭐ 21300 | 🍴 3987 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18601 | 🍴 1199 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17354 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3375 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13254 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11624 | 🍴 913 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10686 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI Projects with Code

### 1. 中文简介
这是一个收录了500个AI项目代码的开源资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目以Awesome列表的形式整理，为学习者提供了丰富的实战案例和代码参考。

### 2. 核心功能
- 收录500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- 按主题分类整理，便于快速查找和学习
- 提供可直接运行的代码示例，支持实践操作
- 持续更新，保持项目库的时效性和丰富度

### 3. 适用场景
- AI初学者系统学习各方向项目实战
- 研究人员参考实现方案与代码结构
- 开发者寻找特定领域的项目灵感与模板
- 培训机构用于教学案例和作业布置

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流研究方向
- 所有项目均附带代码，可直接运行学习
- 标签分类清晰，便于按领域筛选
- 作为Awesome列表，质量经过社区筛选和认可
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36182 | 🍴 7426 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，帮助用户直观地查看和分析模型结构。该项目在 GitHub 上获得了超过 3.3 万星的关注，是 AI 领域最受欢迎的开源工具之一。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 Safetensors
- 提供直观的模型架构图可视化，清晰展示网络层结构和数据流向
- 支持在浏览器和本地桌面环境中运行，使用便捷
- 允许查看模型中的权重数据和层参数信息
- 兼容主流 AI 框架，包括 PyTorch、TensorFlow、Keras 和 ONNX 等

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：适合初学者直观理解各种神经网络结构
- 跨框架模型转换验证：验证不同框架间模型转换后的结构一致性
- 模型文档生成：为项目生成清晰的模型结构图作为技术文档

### 4. 技术亮点
- 纯前端实现，无需安装复杂的依赖环境，开箱即用
- 支持离线桌面应用和在线网页版两种使用方式
- 对 safetensors 等新兴模型格式提供良好支持，紧跟技术发展趋势
- 开源免费，社区活跃，持续维护更新
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33341 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## cheaksheets-ai 项目分析

### 1. 中文简介
本项目为深度学习和机器学习研究人员提供必备的速查表集合，涵盖从基础概念到高级技术的实用参考内容。项目源自Medium文章，整理了AI领域研究者常用的核心知识点。

### 2. 核心功能
- 提供机器学习与深度学习核心概念的速查表
- 涵盖Keras、NumPy、SciPy、Matplotlib等常用工具的使用技巧
- 整理人工智能领域的关键公式与算法要点
- 包含实践中的常见问题与解决方案参考

### 3. 适用场景
- 机器学习/深度学习研究者快速查阅核心概念与公式
- 数据科学家在开发过程中参考常用库的使用技巧
- 学生备考或复习AI相关知识点的便携资料
- 工程师在实际项目中快速定位技术要点的参考手册

### 4. 技术亮点
- 内容精炼，以速查表形式呈现，便于快速检索
- 覆盖从理论到实践的全链路技术栈
- 高星标数（15426）验证了社区认可度与实用价值
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3375 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
该项目是一个人工智能学习路线图，整理了近200个实战案例与项目，免费提供配套教材，适合零基础入门和就业实战。涵盖Python、数学、机器学习、数据分析、深度学习、计算机视觉、自然语言处理等热门领域。

### 2. 核心功能
- 提供系统化的AI学习路线图，帮助学习者循序渐进掌握各项技能
- 收录近200个实战案例与项目，覆盖机器学习、深度学习、NLP、CV等多个方向
- 免费提供配套教材和资源，适合零基础入门者系统学习
- 整合Python、TensorFlow、PyTorch、Keras等主流框架的学习资料
- 聚焦就业实战，帮助学习者快速提升实际项目能力

### 3. 适用场景
- 零基础学习者系统入门人工智能领域
- 数据科学、机器学习方向的就业准备
- 深度学习、计算机视觉、自然语言处理等专项技能提升
- 高校学生或转行人员的实战项目参考

### 4. 技术亮点
- 项目星标数达13254，具有较高的社区认可度和影响力
- 内容全面覆盖AI核心领域，从数学基础到深度学习框架均有涉及
- 实战导向明确，配套教材免费开放，学习门槛低
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13254 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型（LLM）、神经网络及其他 AI 模型。它简化了机器学习模型的训练和部署流程，适合快速原型开发。

## 2. 核心功能
- 低代码/无代码方式快速构建和训练神经网络模型
- 支持多种数据类型（文本、数值、图像等）的自动处理
- 提供可视化的模型训练过程和结果分析
- 内置常用深度学习架构，降低使用门槛
- 支持模型导出和部署，便于生产环境集成

## 3. 适用场景
- 快速验证机器学习想法的原型开发
- 企业级数据科学团队的高效模型训练
- 需要对非技术用户友好的 AI 模型构建
- 多模态数据（文本、图像、表格）的统一处理场景

## 4. 技术亮点
- 基于 PyTorch 构建，兼容主流深度学习生态
- 支持 Llama、Mistral 等主流 LLM 的微调与训练
- 标签覆盖计算机视觉、自然语言处理、深度学习等多个领域，功能全面
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9167 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8957 | 🍴 3108 | 语言: C++
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
- ⭐ 6390 | 🍴 771 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中文自然语言处理资源合集，涵盖了从基础工具（敏感词检测、分词、词性标注）到高级应用（知识图谱、对话系统、预训练模型）的完整生态。该项目整合了大量开源数据集、预训练模型、词库资源及NLP相关论文与代码，是中文NLP领域的重要资源库。

### 2. 核心功能
- **基础NLP工具**：提供中文分词、词性标注、命名实体识别、句法分析、情感分析等核心处理能力
- **丰富词库资源**：包含中日文人名库、中文缩写库、同义词库、反义词库、汽车品牌词库等各类专业词库
- **预训练模型集成**：汇集BERT、ALBERT、ELECTRA、RoBERTa等多种中文预训练语言模型及微调代码
- **知识图谱构建**：提供知识图谱抽取、实体链接、关系抽取、问答系统等完整知识图谱解决方案
- **多模态支持**：涵盖语音识别（ASR）、语音情感分析、OCR文字识别等跨模态NLP能力

### 3. 适用场景
- **企业内容审核**：利用敏感词库、暴恐词表、停用词表等实现自动化内容过滤
- **智能客服与对话系统**：基于对话数据集和 Rasa、ConvLab 等框架构建聊天机器人
- **信息抽取与知识图谱**：从文本中抽取实体、关系、事件，构建领域知识图谱
- **NLP研究与教学**：作为中文NLP学习资源库，包含课程资料、数据集、基准测评等

### 4. 技术亮点
- 项目星标数高达 **82,433**，是 GitHub 上最受欢迎的中文NLP资源库之一
- 整合了清华大学、百度、微软、Facebook 等机构的高质量开源资源
- 覆盖从传统NLP（HMM、CRF）到深度学习（BERT、Transformer）的完整技术栈
- 包含 CLUENER 细粒度命名实体识别、CLUE 中文语言理解测评基准等国内权威评测体系
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82433 | 🍴 15271 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

---

## 1. 中文简介

LlamaFactory 是一个统一且高效的大语言模型与视觉语言模型微调框架，支持 100 多种主流模型的微调训练。该项目已在 ACL 2024 会议上发表，为研究人员和开发者提供了一站式的模型定制解决方案。

---

## 2. 核心功能

- 支持 100+ 种大语言模型（LLM）和视觉语言模型（VLM）的统一微调
- 提供多种高效微调方法，包括 LoRA、QLoRA、全参数微调等
- 集成 RLHF（基于人类反馈的强化学习）和 DPO 等对齐技术
- 提供 Web UI 图形界面和命令行两种交互方式，降低使用门槛
- 支持量化训练与多 GPU 分布式训练，提升训练效率

---

## 3. 适用场景

- **学术研究**：快速复现和验证大模型微调算法，支持多种模型架构的实验对比
- **企业定制**：基于开源模型（如 LLaMA、Qwen、DeepSeek）微调出符合业务需求的专属模型
- **个人开发者**：通过 Web UI 零代码微调模型，快速构建垂直领域的应用原型
- **多模态应用**：对视觉语言模型进行微调，实现图文理解与生成任务

---

## 4. 技术亮点

- **统一框架**：一套代码支持 100+ 模型，无需为每种模型单独适配
- **高效微调**：原生支持 QLoRA 等低资源微调技术，显存占用低
- **多模态支持**：不仅支持纯文本模型，还涵盖视觉语言模型（VLM）的微调
- **对齐技术集成**：内置 RLHF、DPO 等主流对齐方法，便于模型价值观对齐
- **ACL 2024 论文背书**：经过学术同行评审，技术可靠性和创新性得到认可
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74029 | 🍴 9057 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一个由微软推出的AI入门课程项目，涵盖12周、24节课的完整学习路径，旨在让所有人都能轻松学习人工智能。项目以Jupyter Notebook形式呈现，内容通俗易懂，适合零基础学习者。

## 2. 核心功能
- 提供系统化的AI课程，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域
- 使用Jupyter Notebook交互形式，便于学习者边学边实践
- 包含CNN、RNN、GAN等深度学习模型的入门讲解
- 微软官方出品，课程质量有保障，适合自学者系统学习

## 3. 适用场景
- AI初学者系统学习人工智能基础知识
- 高校或培训机构作为AI入门课程的补充教材
- 企业员工AI技能培训的基础课程
- 对AI感兴趣的非技术背景人员入门了解

## 4. 技术亮点
- 项目获得64732个星标，说明在社区中具有很高的认可度和影响力
- 微软"For Beginners"系列品牌，课程设计遵循渐进式学习理念
- 标签覆盖全面，从传统机器学习到前沿深度学习技术均有涉及
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 64732 | 🍴 12542 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# GitHub项目分析：ai-engineering-from-scratch

---

## 1. 中文简介

该项目是一套从零开始构建AI工程能力的完整学习路线，涵盖理论理解、动手实践到最终部署的完整流程，帮助用户掌握AI系统的端到端开发能力。

---

## 2. 核心功能

- **从零实现AI系统**：不依赖现成框架，深入理解底层原理并手动构建
- **全栈AI工程覆盖**：涵盖LLM、计算机视觉、强化学习、MCP协议等核心领域
- **多语言技术栈**：同时支持Python和Rust，兼顾易用性与高性能
- **Swarm Intelligence（群体智能）**：探索多智能体协作与分布式AI架构
- **完整课程式学习路径**：提供结构化的教程，从入门到实战逐步推进

---

## 3. 适用场景

- **AI工程师技能提升**：希望深入理解LLM、Transformer等核心技术原理的学习者
- **AI系统架构设计**：需要构建多智能体（Multi-Agent）或群体智能系统的开发者
- **高性能AI应用开发**：使用Rust实现低延迟、高吞吐AI推理服务的工程师
- **AI课程与培训**：教育机构或个人用于系统性地教授AI工程实践

---

## 4. 技术亮点

- 同时覆盖**Python（快速原型）**和**Rust（高性能部署）**两种技术栈，实现从开发到生产的全链路
- 深入**MCP（Model Context Protocol）**等前沿AI交互协议，紧跟AI工程发展趋势
- 项目星标数超过**4.6万**，社区认可度高，是一个成熟且持续更新的学习资源库
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46608 | 🍴 8120 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42454 | 🍴 11522 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36182 | 🍴 7426 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33813 | 🍴 4708 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29040 | 🍴 3532 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21832 | 🍴 3349 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17354 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI Projects with Code

### 1. 中文简介
这是一个收录了500个AI项目代码的开源资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目以Awesome列表的形式整理，为学习者提供了丰富的实战案例和代码参考。

### 2. 核心功能
- 收录500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- 按主题分类整理，便于快速查找和学习
- 提供可直接运行的代码示例，支持实践操作
- 持续更新，保持项目库的时效性和丰富度

### 3. 适用场景
- AI初学者系统学习各方向项目实战
- 研究人员参考实现方案与代码结构
- 开发者寻找特定领域的项目灵感与模板
- 培训机构用于教学案例和作业布置

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流研究方向
- 所有项目均附带代码，可直接运行学习
- 标签分类清晰，便于按领域筛选
- 作为Awesome列表，质量经过社区筛选和认可
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36182 | 🍴 7426 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款利用人工智能自动化浏览器工作流的技术工具。它通过结合大型语言模型（LLM）与计算机视觉能力，让机器能够像人类一样操作浏览器完成各类重复性任务。该项目为开发者提供了一个简单易用的 API，可将繁琐的网页操作转化为可自动执行的智能流程。

### 2. 核心功能
- 基于 AI 的浏览器自动化，支持视觉识别与 LLM 理解页面内容
- 提供简洁的 API 接口，方便集成到现有系统中
- 兼容 Playwright 和 Puppeteer 等主流浏览器自动化工具
- 支持 RPA（机器人流程自动化）场景，可替代人工完成网页操作
- 无需手动编写选择器，AI 自动识别页面元素并执行操作

### 3. 适用场景
- **数据抓取与录入**：自动从网页提取数据并填入表单或系统
- **跨平台工作流自动化**：替代 Power Automate 等工具，处理多步骤网页任务
- **电商与比价场景**：自动监控商品价格、库存变化并执行下单操作
- **企业后台操作自动化**：自动化处理 ERP、CRM 等系统的日常重复操作

### 4. 技术亮点
- 将 LLM 语义理解与计算机视觉相结合，实现"看懂页面"的智能操作
- 无需维护脆弱的 CSS 选择器，AI 自适应不同页面布局变化
- 支持多浏览器引擎，灵活适配不同自动化需求
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22740 | 🍴 2139 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介

CVAT 是一款领先的计算机视觉标注平台，专注于构建高质量的视觉数据集以支持视觉AI应用。该平台提供开源、云端和企业级产品，同时配套标注服务，支持图像、视频及3D数据的AI辅助标注、质量保障、团队协作等功能。

## 2. 核心功能

- **多模态标注支持**：支持图像、视频和3D数据的标注工作。
- **AI辅助标注**：内置AI模型辅助自动标注，大幅提升标注效率。
- **团队协作与质量保障**：支持多人协作标注及质量控制流程。
- **数据分析与API接口**：提供数据分析功能和开发者API，便于集成与扩展。
- **多种产品形态**：提供开源版、云端版和企业版，满足不同规模需求。

## 3. 适用场景

- **深度学习数据集构建**：为图像分类、目标检测、语义分割等任务创建标注数据集。
- **自动驾驶与安防视频标注**：对大量视频帧进行目标检测和轨迹标注。
- **3D点云标注**：用于自动驾驶、机器人等领域的3D场景标注。
- **企业级AI项目团队协作**：大型团队分工协作完成大规模标注任务。

## 4. 技术亮点

- 开源社区活跃，Star数超1.6万，生态完善。
- 支持主流深度学习框架（PyTorch、TensorFlow）。
- 提供完整的标注格式输出，兼容多种AI训练需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16508 | 🍴 3799 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

## 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库。支持CNN和Vision Transformer等模型架构，可用于分类、目标检测、图像分割、图像相似度等多种任务，帮助可视化模型决策依据。

## 2. 核心功能
- 实现Grad-CAM、Grad-CAM++、Score-CAM等多种类激活图生成算法
- 兼容CNN和Vision Transformer等多种深度学习模型架构
- 支持图像分类、目标检测、图像分割、图像相似度等多种视觉任务
- 提供直观的可视化输出，帮助理解模型关注区域
- 基于PyTorch实现，易于集成到现有项目中

## 3. 适用场景
- **图像分类调试**：验证模型是否关注正确区域，排查误判原因
- **医学影像分析**：可视化模型关注的病灶区域，增强临床可信度
- **自动驾驶目标检测**：解释模型对特定目标的识别依据
- **模型可解释性研究**：分析Vision Transformer等复杂模型的注意力机制

## 4. 技术亮点
- 支持多种CAM变体算法（Grad-CAM、Grad-CAM++、Score-CAM、XGrad-CAM等）
- 兼容主流预训练模型（ResNet、ViT等），开箱即用
- 提供灵活的API设计，支持自定义模型结构
- 项目星标数超过1.2万，社区活跃度高
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12951 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，专为深度学习研究而设计。它基于 PyTorch 构建，提供了一套可微分的图像处理与几何计算工具，使研究人员能够直接在神经网络中集成传统计算机视觉算法。

### 2. 核心功能
- 提供可微分的几何计算机视觉算子，支持端到端深度学习训练
- 涵盖图像处理、相机标定、三维重建等核心视觉算法
- 与 PyTorch 深度集成，可直接在计算图中使用
- 支持机器人导航、空间感知等空间 AI 应用场景

### 3. 适用场景
- 深度学习中的相机标定与姿态估计研究
- 机器人视觉定位与空间感知任务
- 可微分图像处理管道的构建与优化
- 计算机视觉与深度学习交叉领域的学术研究

### 4. 技术亮点
- **可微分设计**：所有几何算子均为可微分实现，可直接嵌入神经网络进行端到端训练
- **PyTorch 原生支持**：基于 PyTorch 张量操作，与主流深度学习框架无缝衔接
- **开源社区活跃**：参与 Hacktoberfest 活动，拥有良好的社区贡献生态
- 链接: https://github.com/kornia/kornia
- ⭐ 11314 | 🍴 1220 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8875 | 🍴 2189 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3477 | 🍴 881 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3361 | 🍴 412 | 语言: Python
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
- 

# OpenClaw 项目分析

## 1. 中文简介
OpenClaw 是一款完全由你掌控的个人 AI 助手，支持任意操作系统和平台。它倡导数据自主的理念，让你用自己的数据来驱动 AI，以独特的方式（"龙虾方式"）打造专属智能体验。

## 2. 核心功能
- **跨平台支持**：兼容任意操作系统，随时随地使用
- **数据自主**：强调用户拥有并控制自己的数据，而非依赖第三方云服务
- **个人化 AI 助手**：根据你的数据和偏好定制专属 AI 体验
- **开源项目**：代码完全公开，可自由使用和二次开发
- **TypeScript 开发**：使用现代编程语言，具备类型安全和良好的开发体验

## 3. 适用场景
- 注重隐私和数据安全的个人用户，希望 AI 助手不将数据上传至第三方服务器
- 开发者和技术爱好者，想要搭建或定制自己的 AI 助手系统
- 需要在多个设备和操作系统上无缝使用的用户
- 对现有 AI 助手的数据政策不满，寻求替代方案的用户

## 4. 技术亮点
- **高人气项目**：38.6万星标，说明社区认可度极高
- **TypeScript 技术栈**：提供类型安全和更好的代码可维护性
- **数据主权理念**：在主流 AI 助手普遍依赖云服务的背景下，提供本地化/自主数据管理方案，契合隐私保护趋势
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386072 | 🍴 81146 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub 项目分析：superpowers

### 1. 中文简介
这是一个经过验证的AI代理技能框架与软件开发方法论，旨在通过子代理协作的方式提升开发效率。项目专注于将AI能力融入实际软件开发流程，帮助开发者更高效地完成编码任务。

### 2. 核心功能
- **代理技能框架**：提供结构化的AI代理协作机制，实现任务分解与自动化执行
- **子代理驱动开发**：采用多子代理协同模式，支持复杂开发任务的并行处理
- **完整SDLC支持**：覆盖从头脑风暴到代码实现的软件开发生命周期全流程
- **技能模块化**：将开发能力封装为可复用的技能单元，便于灵活组合使用
- **智能头脑风暴**：集成AI辅助的创意生成与方案设计功能

### 3. 适用场景
- 需要AI辅助完成复杂编码任务的中大型项目开发
- 希望通过代理协作提升团队开发效率的技术团队
- 探索AI驱动软件开发方法论的早期采用者
- 需要将头脑风暴、设计和编码整合到统一工作流的场景

### 4. 技术亮点
- **高人气验证**：27万+星标数表明社区认可度极高
- **方法论完整性**：不仅是工具，更是一套完整的软件开发方法论体系
- **Shell实现**：使用Shell脚本构建，轻量且易于集成到现有工作流中
- **多标签覆盖**：涵盖AI、头脑风暴、编码、技能开发等多个维度，生态丰富
- 链接: https://github.com/obra/superpowers
- ⭐ 271234 | 🍴 24240 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## Hermes-Agent 项目分析

### 1. 中文简介
Hermes-Agent 是一个智能 AI 代理系统，能够随着用户的使用不断学习和成长。该项目专注于构建可扩展的 AI 助手，支持多种大语言模型（LLM），包括 Claude、GPT 和 Codex 等，旨在为用户提供个性化的智能服务体验。

### 2. 核心功能
- **多模型支持**：兼容 Anthropic Claude、OpenAI GPT 及 Codex 等多种主流 LLM
- **自适应学习**：代理能够根据用户交互持续优化和成长
- **多平台集成**：支持聊天界面、代码助手等多种应用场景
- **可扩展架构**：基于 Python 构建，易于二次开发和功能扩展
- **开源协作**：由 Nous Research 等团队贡献，社区活跃

### 3. 适用场景
- **智能客服助手**：为企业或产品提供 24/7 自动化客户支持
- **代码编程辅助**：作为开发者助手，帮助编写、调试和优化代码
- **个人知识管理**：学习和记忆用户偏好，提供个性化信息推荐
- **企业 AI 代理**：集成到企业内部系统，自动化处理复杂业务流程

### 4. 技术亮点
- **多模型路由**：智能选择最优 LLM 处理不同任务，平衡性能与成本
- **成长型架构**：代理具备记忆和学习能力，越用越懂用户
- **开源生态**：标签覆盖 AI、LLM、Claude、ChatGPT 等热门关键词，社区关注度高

---

> **注**：以上分析基于项目标签和描述信息推断，实际功能以官方文档为准。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 229548 | 🍴 45314 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

---

### 1. 中文简介

n8n 是一款采用公平代码协议的工作流自动化平台，内置原生 AI 能力。它支持可视化拖拽构建与自定义代码混合开发，提供自托管和云端两种部署方式，并集成超过 400 种第三方应用。

---

### 2. 核心功能

- **可视化工作流构建**：通过拖拽节点快速搭建自动化流程，无需编写大量代码。
- **原生 AI 集成**：内置 AI 节点，支持 LLM 调用、RAG 检索和 AI 工作流编排。
- **400+ 集成生态**：覆盖主流 SaaS 工具、数据库、API 和服务，开箱即用。
- **自定义代码扩展**：支持在节点中嵌入 JavaScript/Python 代码，满足复杂业务逻辑。
- **灵活部署方式**：支持本地自托管（数据完全自主）和云端托管两种模式。

---

### 3. 适用场景

- **企业自动化流程**：如自动生成报表、同步 CRM 数据、自动化审批流程等。
- **AI 应用开发**：构建基于大模型的智能客服、文档摘要、内容生成等 AI 工作流。
- **数据管道与 ETL**：从多个数据源采集、转换并推送数据，实现数据自动化流转。
- **跨系统集成**：连接不同平台（如 Slack + Notion + Google Sheets）实现信息互通。

---

### 4. 技术亮点

- **Fair-code 协议**：允许自由使用和商业集成，但禁止直接将其作为竞品出售，平衡了开放性与商业保护。
- **MCP 协议支持**：原生支持 Model Context Protocol，可轻松接入各类 AI 模型和外部数据源。
- **TypeScript 全栈开发**：前后端统一技术栈，代码质量高，社区贡献活跃。
- **节点化架构**：每个功能以独立节点形式存在，支持自定义节点开发，扩展性极强。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200385 | 🍴 60098 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186562 | 🍴 46090 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167060 | 🍴 21561 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 166428 | 🍴 9352 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164498 | 🍴 30568 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157731 | 🍴 46178 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153114 | 🍴 9849 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

