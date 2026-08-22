# GitHub AI项目每日发现报告
日期: 2026-08-22

## 新发布的AI项目

### cs-board
- 

## cs-board 项目分析

### 1. 中文简介
cs-board 是一款本地运行的 AI 工具，能够根据参考声音和中文文案自动生成白板动画视频。该项目结合语音克隆与 TTS 技术，帮助用户快速制作配音动画内容。

### 2. 核心功能
- 支持上传参考声音进行语音克隆，生成自然流畅的中文配音
- 输入中文文案后自动合成对白并生成配套白板动画视频
- 采用 FastAPI 构建后端服务，React 搭建前端交互界面
- 使用 Index-TTS 模型实现高质量的文本转语音效果
- 全程本地运行，无需依赖外部云服务，保护用户隐私

### 3. 适用场景
- 教育领域：教师将课件文案快速转化为带配音的动画讲解视频
- 自媒体创作：内容创作者批量生成短视频口播素材
- 企业培训：将培训文档自动转为生动的动画演示视频
- 无障碍辅助：为视障用户提供语音播报的内容可视化版本

### 4. 技术亮点
- **本地化部署**：无需联网即可运行，数据完全私有
- **语音克隆技术**：基于少量参考音频即可复刻目标音色
- **前后端分离架构**：FastAPI + React 实现高效开发与流畅体验
- **端到端自动化**：从文案输入到视频输出全流程一键生成
- 链接: https://github.com/ChenShuo2004/cs-board
- ⭐ 105 | 🍴 24 | 语言: Python
- 标签: ai-video, chinese, fastapi, index-tts, react

### AI-Glossary-Handbook
- 

# AI-Glossary-Handbook 项目分析

## 1. 中文简介
这是一个专注于AI领域术语解释的手册/词典项目，旨在为读者提供人工智能相关概念和术语的清晰定义与说明。由于项目描述为空，具体功能细节尚不明确。

## 2. 核心功能
- 收录AI领域核心术语及其定义解释
- 提供标准化的术语对照与释义
- 便于快速查阅AI专业词汇
- 可能包含术语的来源背景或应用场景说明

## 3. 适用场景
- AI初学者系统学习专业术语
- 技术文档编写时的术语参考
- 团队内部知识共享与培训
- 非技术背景人员了解AI概念

## 4. 技术亮点
暂无明确技术亮点，该项目可能以内容整理为主，技术实现较为简单。
- 链接: https://github.com/h9-tec/AI-Glossary-Handbook
- ⭐ 72 | 🍴 5 | 语言: 未知

### MeshLAN
- 

## MeshLAN 项目分析

### 1. 中文简介
MeshLAN是一个基于Nebula构建的自托管P2P优先虚拟局域网项目，支持服务共享、多中继节点和AI自动化功能。该项目采用Go语言开发，专注于提供安全的点对点网络互联方案。

### 2. 核心功能
- 基于Nebula协议的P2P虚拟LAN，实现设备间安全互联
- 支持局域网内服务共享，设备可互相访问资源
- 多中继节点机制，保障NAT穿透和远程连接
- 集成AI自动化功能，实现智能网络管理
- 跨平台支持，兼容Windows等操作系统

### 3. 适用场景
- 分布式团队远程协作，构建安全的虚拟内网
- 家庭或小型办公室搭建私有虚拟局域网
- 需要穿透NAT的P2P应用部署场景
- 对网络自动化管理有需求的自托管环境

### 4. 技术亮点
- 基于成熟的Nebula协议栈，安全性与可靠性有保障
- Go语言开发，性能优异且易于跨平台编译部署
- P2P优先架构，减少中心节点依赖
- 内置NAT穿透能力，降低网络配置复杂度
- 融合AI自动化，提升网络运维效率
- 链接: https://github.com/zhaoxuya520/MeshLAN
- ⭐ 52 | 🍴 4 | 语言: Go
- 标签: golang, mesh-network, nat-traversal, nebula, p2p

### netwalk
- 描述: Read-only network survey toolkit for AI coding agents: crawl a site from one device, diagnose it, draw it, and hand over a report — without ever changing a device or seeing a credential.
- 链接: https://github.com/ripmilla/netwalk
- ⭐ 37 | 🍴 8 | 语言: Python

### clipfactory
- 

## ClipFactory 项目分析

### 1. 中文简介
ClipFactory 是一款基于 AI 的短视频自动生成工具，用户只需提供主题和模板，即可利用自己的素材库快速生成竖屏短视频。系统涵盖 AI 脚本撰写、配音、场景规划、字幕生成及 FFmpeg 渲染等全流程。支持多角色人设、AI 镜头列表、AI B-roll 素材及批量生成，采用 Elastic 2.0 开源协议。

### 2. 核心功能
- **AI 脚本自动生成**：根据主题和模板智能生成视频脚本内容
- **多角色配音**：集成 ElevenLabs 实现高质量 AI 语音合成
- **智能场景规划**：自动生成镜头列表和 B-roll 素材匹配方案
- **FFmpeg 渲染输出**：自动化视频合成与字幕添加
- **批量生成能力**：支持多版本、多主题视频批量产出

### 3. 适用场景
- **社交媒体内容创作者**：快速批量生产 TikTok、Reels、Shorts 等短视频内容
- **营销团队**：基于统一模板批量生成多版本广告素材
- **自媒体运营**：结合自有素材库实现个性化内容自动化生产
- **多账号矩阵运营**：支持多角色人设，适配不同账号风格需求

### 4. 技术亮点
- 技术栈完整：前端 React + 后端 FastAPI，配合 OpenAI API 实现 AI 能力
- 多模态整合：将文本生成、语音合成、视频渲染流程无缝串联
- 素材管理：支持用户自有 B-roll 素材库的智能匹配与复用
- 开源协议友好：采用 Elastic 2.0 协议，允许商业使用
- 链接: https://github.com/feyzilim/clipfactory
- ⭐ 32 | 🍴 6 | 语言: Python
- 标签: content-creation, elevenlabs, fastapi, ffmpeg, openai

### docster
- 描述: A skill that helps AI agents write better docs, with support of Comark components.
- 链接: https://github.com/atinux/docster
- ⭐ 30 | 🍴 2 | 语言: 未知

### cyber-cloud-skills
- 描述: Open-source cloud security and AI penetration-testing skills for CyberStrikeAI and Strix, covering AWS, Azure, GCP, OCI, Kubernetes, Docker, IAM/RBAC, attack-path analysis, container security, and posture assessment.
- 链接: https://github.com/cybercloudskills/cyber-cloud-skills
- ⭐ 29 | 🍴 0 | 语言: 未知

### store-screenshots
- 描述: 🖼️ AI agent skill for Claude Code & Codex — turns raw app screenshots into store-ready App Store & Google Play marketing images: device frames (iPhone·iPad·Galaxy·Fold·Flip), app-matched backgrounds, marketing copy, exact store sizes. 앱스토어·플레이스토어 마케팅 스크린샷 자동 생성
- 链接: https://github.com/LeeHueeng/store-screenshots
- ⭐ 25 | 🍴 4 | 语言: 未知
- 标签: agent-skills, ai-agents, android, app-store, app-store-optimization

### nuphus
- 描述: Nuphus — 本地优先的 AI Agent：真实桌面执行力 + 手机第二块屏幕。Local-first AI agent with real desktop execution and dual-device real-time sync.
- 链接: https://github.com/mrpulor-gh/nuphus
- ⭐ 23 | 🍴 3 | 语言: Rust
- 标签: agent-skills, ai-agent, ai-agents, automation, computer-use

### ai-surf-when-bored
- 描述: 无描述
- 链接: https://github.com/sanqianzilanyue/ai-surf-when-bored
- ⭐ 20 | 🍴 1 | 语言: HTML

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源汇总项目，涵盖了敏感词检测、语言识别、实体抽取、情感分析等基础NLP工具，以及大量中文词库、预训练模型、数据集和开源工具链接。该项目由中文NLP社区维护，是中文开发者进行NLP研究与工程实践的重要资源导航站。

## 2. 核心功能
- **基础NLP工具**：敏感词过滤、语言检测、手机号/身份证/邮箱抽取、繁简体转换、中英文发音模拟等
- **丰富词库资源**：中日文人名库、汽车品牌库、成语库、古诗词库、医学/法律/财经等领域专业词库
- **预训练模型集合**：BERT、GPT-2、ALBERT、ELECTRA等主流模型的中文版本及训练代码
- **知识图谱与问答**：中英文跨语言知识图谱、医疗/金融领域知识图谱构建及问答系统
- **语音与OCR**：中文语音识别数据集、语音情感分析、中文OCR识别工具

## 3. 适用场景
- **NLP开发者入门**：快速查找中文NLP相关工具、数据集和开源项目
- **企业内容审核**：利用敏感词库和暴恐词表构建内容安全过滤系统
- **知识图谱构建**：参考实体抽取、关系抽取和图谱构建相关资源
- **语音助手开发**：获取ASR语音识别、语音合成及对话系统相关开源方案

## 4. 技术亮点
- 项目收录资源极为丰富，涵盖从基础工具到前沿模型的完整中文NLP技术栈
- 包含清华大学、百度、腾讯等机构开源的高质量预训练模型和 benchmark 数据集
- 提供中文NLP竞赛方案汇总，对算法工程师有较高参考价值
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82599 | 🍴 15272 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个收录了500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。该项目为学习者提供了丰富的实战案例，适合从入门到进阶的系统性学习。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- 每个项目均附带可运行的代码示例
- 项目按领域分类，便于针对性学习
- 适合不同水平学习者的实践参考

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习的基础概念
- 开发者寻找计算机视觉或NLP项目的参考实现
- 数据科学家构建项目作品集的灵感来源
- 企业培训中作为AI技术的实战教学材料

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主要应用领域
- 全部项目均提供可运行的Python代码
- 标签分类清晰，便于按领域快速定位
- 星标数高达36454，说明社区认可度高
- 作为"awesome"系列项目，内容经过筛选和质量把控
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36454 | 🍴 7454 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持查看和调试多种主流模型格式，帮助用户直观理解模型结构和参数。

### 2. 核心功能
- 支持多种模型格式（ONNX、TensorFlow、PyTorch、CoreML、Keras 等）
- 以图形化方式展示神经网络层结构和数据流向
- 支持查看模型参数、权重和偏置信息
- 提供交互式模型浏览和缩放功能
- 支持在浏览器和本地桌面应用中使用

### 3. 适用场景
- 深度学习模型调试与结构分析
- 模型部署前的格式转换验证
- 教学演示与模型可视化展示
- 跨框架模型兼容性检查

### 4. 技术亮点
- 纯前端技术实现，无需后端服务即可运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 支持 safetensors 等新兴模型格式
- 同时提供 Web 版和桌面客户端，使用灵活便捷
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33387 | 🍴 3174 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# ONNX 项目分析

## 1. 中文简介
ONNX（开放神经网络交换）是机器学习领域的开放互操作性标准，旨在促进不同深度学习框架之间的模型兼容与转换。它允许开发者在不同框架间无缝迁移模型，打破框架壁垒。

## 2. 核心功能
- 提供统一的模型格式，支持跨框架模型交换
- 支持将模型从主流框架（如PyTorch、TensorFlow、Keras）导出为ONNX格式
- 提供ONNX Runtime推理引擎，实现高性能跨平台推理
- 支持模型转换和优化工具链，便于部署到不同硬件环境

## 3. 适用场景
- 模型从训练框架迁移到生产部署环境
- 在不同深度学习框架间迁移模型架构
- 需要将模型部署到边缘设备或移动端
- 希望在多种硬件加速器（GPU、CPU、NPU）上运行推理

## 4. 技术亮点
- 由微软、Facebook等科技巨头联合推动，生态支持广泛
- 社区活跃，拥有大量贡献者和企业支持
- 与主流框架深度集成，转换流程成熟稳定
- 支持丰富的算子和模型类型，覆盖大多数深度学习场景
- 链接: https://github.com/onnx/onnx
- ⭐ 21348 | 🍴 4007 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

### 1. 中文简介
这是一个关于机器学习工程领域的开源知识库，系统性地整理了大语言模型训练、推理及部署的最佳实践。内容涵盖从GPU调试、网络配置到存储优化等工程化核心话题，是MLOps实践者的实用参考手册。

### 2. 核心功能
- 提供大语言模型（LLM）训练与推理的完整工程指南
- 深入讲解GPU调试、PyTorch性能优化及可扩展性策略
- 覆盖MLOps全流程，包括网络配置、存储优化和Slurm集群管理
- 整合Hugging Face Transformers等主流框架的实践经验

### 3. 适用场景
- **LLM训练工程**：大规模语言模型分布式训练的配置与调优
- **推理部署优化**：生产环境中模型推理加速与资源管理
- **MLOps平台搭建**：企业级机器学习基础设施的构建与维护
- **GPU集群调试**：高性能计算环境下的故障排查与性能优化

### 4. 技术亮点
- 聚焦实战，涵盖Slurm调度、GPU网络拓扑、分布式存储等底层工程细节
- 内容紧跟LLM时代需求，覆盖从训练到推理的全链路工程问题
- 开源协作模式，持续吸收社区实践，是PyTorch + Transformers生态的重要补充资源
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18687 | 🍴 1204 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17382 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11630 | 🍴 916 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10692 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个收录了500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。该项目为学习者提供了丰富的实战案例，适合从入门到进阶的系统性学习。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- 每个项目均附带可运行的代码示例
- 项目按领域分类，便于针对性学习
- 适合不同水平学习者的实践参考

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习的基础概念
- 开发者寻找计算机视觉或NLP项目的参考实现
- 数据科学家构建项目作品集的灵感来源
- 企业培训中作为AI技术的实战教学材料

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主要应用领域
- 全部项目均提供可运行的Python代码
- 标签分类清晰，便于按领域快速定位
- 星标数高达36454，说明社区认可度高
- 作为"awesome"系列项目，内容经过筛选和质量把控
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36454 | 🍴 7454 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持查看和调试多种主流模型格式，帮助用户直观理解模型结构和参数。

### 2. 核心功能
- 支持多种模型格式（ONNX、TensorFlow、PyTorch、CoreML、Keras 等）
- 以图形化方式展示神经网络层结构和数据流向
- 支持查看模型参数、权重和偏置信息
- 提供交互式模型浏览和缩放功能
- 支持在浏览器和本地桌面应用中使用

### 3. 适用场景
- 深度学习模型调试与结构分析
- 模型部署前的格式转换验证
- 教学演示与模型可视化展示
- 跨框架模型兼容性检查

### 4. 技术亮点
- 纯前端技术实现，无需后端服务即可运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 支持 safetensors 等新兴模型格式
- 同时提供 Web 版和桌面客户端，使用灵活便捷
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33387 | 🍴 3174 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub 项目分析：cheatsheets-ai

## 1. 中文简介
该项目为深度学习与机器学习研究者提供了一套核心速查表（Cheat Sheets）资源集合，涵盖常用工具库的实用参考指南，旨在帮助研究人员快速查阅关键知识点与操作命令。

## 2. 核心功能
- 提供深度学习与机器学习领域的核心速查表汇总
- 涵盖 Keras、NumPy、SciPy、Matplotlib 等主流工具库的参考指南
- 整合人工智能与深度学习相关的关键知识点
- 支持研究人员快速检索常用命令与函数用法
- 作为学习与实践过程中的便捷查阅工具

## 3. 适用场景
- 深度学习研究人员快速查阅常用函数与参数
- 机器学习初学者系统梳理核心知识点
- 数据科学家日常编码时的参考手册
- 算法工程师面试前的知识点复习

## 4. 技术亮点
- 项目获得超过 1.5 万星标，社区认可度较高
- 涵盖从底层数值计算（NumPy/SciPy）到高级框架（Keras）的完整技术栈
- 整合了数据可视化（Matplotlib）等实用工具参考
- 内容来源为专业研究人员整理的精华总结，实用性强
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介

Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式配置简化了深度学习模型的训练、评估与部署流程，让开发者无需编写大量代码即可快速搭建和微调 AI 模型。

## 2. 核心功能

- **低代码建模**：通过 YAML 声明式配置快速定义和训练深度学习模型
- **多模态支持**：涵盖自然语言处理、计算机视觉、表格数据等多种数据类型
- **LLM 微调**：支持对 LLaMA、Llama2、Mistral 等开源大模型进行高效微调
- **实验追踪**：内置实验管理与模型评估功能，便于对比不同配置效果
- **PyTorch 原生**：基于 PyTorch 构建，兼容主流深度学习生态

## 3. 适用场景

- **快速原型开发**：研究人员和开发者快速验证 AI 模型想法
- **LLM 领域适配**：对开源大语言模型进行垂直领域微调
- **多模态应用构建**：同时处理文本和图像的智能应用开发
- **数据科学项目**：结构化数据的预测建模与分类任务

## 4. 技术亮点

- 与 Hugging Face 生态深度集成，无缝加载开源模型
- 内置 AutoML 能力，支持自动超参数调优
- 支持分布式训练，提升大规模模型训练效率
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9182 | 🍴 1230 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8968 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8370 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6990 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6428 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、实体抽取、情感分析、知识图谱、预训练模型等丰富的NLP工具和资源。该项目汇集了海量的中文NLP数据集、语料库和开源模型，是中文NLP研究者和开发者的实用工具箱。

## 2. 核心功能
- 敏感词过滤、语言检测与文本规范化处理
- 手机号、身份证、邮箱、人名等实体抽取
- 情感分析、文本分类与关键词提取
- 知识图谱构建与智能问答系统
- BERT、GPT等预训练语言模型资源

## 3. 适用场景
- 内容安全审核与敏感信息过滤
- 文本信息抽取与实体识别任务
- 智能客服与对话机器人开发
- NLP研究与模型训练资源参考

## 4. 技术亮点
- 收录海量中文NLP数据集和预训练模型，涵盖传统NLP到深度学习的完整工具链
- 提供多种语言模型（BERT、GPT、ALBERT等）的实现代码和教程
- 包含丰富的行业领域词库和知识库（医疗、法律、金融等）
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82599 | 🍴 15272 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74291 | 🍴 9087 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66312 | 🍴 12837 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# 项目分析：ai-engineering-from-scratch

---

## 1. 中文简介
从零开始学习AI工程，亲手构建核心组件，并将成果交付给他人使用。该项目是一套完整的AI工程实战课程，涵盖从理论理解到实际部署的全流程。

## 2. 核心功能
- **从零构建AI系统**：深入理解并手动实现各类AI模型与组件，而非仅调用现成库
- **多领域覆盖**：涵盖大语言模型（LLM）、生成式AI、计算机视觉、NLP、强化学习等多个AI子领域
- **AI代理与 swarm 智能**：学习如何构建多智能体系统和群体智能应用
- **MCP（模型上下文协议）支持**：集成现代AI工程标准协议
- **多语言实践**：以Python为主，同时涉及Rust和TypeScript实现

## 3. 适用场景
- **AI工程师入门**：希望深入理解AI底层原理、而非仅停留在API调用层面的开发者
- **AI课程学习**：需要系统化学习AI工程全流程的学生或自学者
- **团队技术升级**：希望团队掌握从零构建AI系统能力的技术负责人
- **AI项目实战参考**：需要构建自定义AI代理、多智能体系统或生成式AI应用的开发者

## 4. 技术亮点
- 高人气项目（47,644星标），社区活跃度高，质量有保障
- 标签覆盖极广，从基础机器学习到前沿的LLM、生成式AI、多智能体系统均有涉及
- 强调"from-scratch"理念，帮助学习者建立扎实的技术根基
- 融合多种语言（Python/Rust/TypeScript），适合不同技术栈的开发者
- 结合MCP等现代协议，紧跟AI工程最新发展趋势
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47644 | 🍴 8390 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

# GitHub 项目分析：ailearning

---

## 1. 中文简介

AiLearning 是一个综合性的数据科学与机器学习实战学习项目，涵盖数据分析、机器学习算法、深度学习框架（PyTorch、TensorFlow 2）以及自然语言处理（NLTK）等内容。该项目以线性代数为基础，系统性地整合了从传统机器学习到深度学习的完整知识体系，适合初学者到进阶学习者系统学习。

---

## 2. 核心功能

- **机器学习算法实战**：涵盖 SVM、KNN、逻辑回归、朴素贝叶斯、AdaBoost、PCA、SVD 等经典算法的实现与练习。
- **深度学习框架应用**：基于 PyTorch 和 TensorFlow 2 实现 DNN、RNN、LSTM 等神经网络模型。
- **数据挖掘算法**：包含 Apriori、FP-Growth 等关联规则挖掘算法。
- **自然语言处理（NLP）**：基于 NLTK 进行文本处理与 NLP 任务实践。
- **推荐系统**：提供推荐系统相关算法的实现与案例。

---

## 3. 适用场景

- **机器学习入门学习**：适合初学者系统学习机器学习理论与代码实践。
- **算法复现与参考**：为开发者提供多种经典算法的 Python 实现参考。
- **深度学习项目实战**：帮助学习者掌握 PyTorch 和 TensorFlow 2 的实际应用。
- **NLP 与推荐系统开发**：适用于自然语言处理和推荐系统方向的学习与开发。

---

## 4. 技术亮点

- **知识体系完整**：从线性代数基础到深度学习，覆盖数据科学全链路。
- **多框架支持**：同时支持 PyTorch 和 TensorFlow 2，便于对比学习。
- **算法种类丰富**：涵盖监督学习、无监督学习、深度学习、NLP 等多个领域的主流算法。
- **高人气项目**：拥有 42472 星标，是 GitHub 上热门的机器学习学习资源。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42472 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36454 | 🍴 7454 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33839 | 🍴 4712 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29174 | 🍴 3557 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21848 | 🍴 3359 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17382 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个汇集了500个AI项目的高质量资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码实现。该项目在GitHub上获得了超过3.6万颗星标，是AI学习者的重要参考资料。

### 2. 核心功能
- 提供500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带完整可运行的代码实现
- 按技术领域分类整理，便于针对性学习
- 收录来自Awesome系列的精选AI项目资源
- 以Python为主要编程语言，适合实践操作

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习的项目实战
- 研究人员快速查找各领域的经典项目实现参考
- 开发者寻找计算机视觉或NLP方向的开源项目灵感
- 数据科学家构建AI作品集的技术资料库

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流方向，资源集中度高
- 每个项目均配有代码，可直接运行学习，实践性强
- 标签分类清晰，涵盖artificial-intelligence、deep-learning、computer-vision、nlp等核心领域，便于精准检索
- 作为Awesome系列项目之一，经过社区筛选，质量有保障
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36454 | 🍴 7454 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介
Skyvern 是一款利用人工智能技术实现浏览器工作流自动化的工具，通过AI驱动的方式自动完成基于浏览器的各种任务。它结合了大语言模型和计算机视觉能力，能够智能理解网页内容并执行复杂操作。

## 2. 核心功能
- 基于AI的智能浏览器自动化，无需编写脚本即可自动操作网页
- 支持多种浏览器自动化引擎（Playwright、Puppeteer、Selenium）
- 集成大语言模型（GPT/LLM）进行页面理解和决策
- 提供RESTful API接口，便于集成到现有系统中
- 支持计算机视觉技术，能够识别和处理页面元素

## 3. 适用场景
- 企业级RPA流程自动化（如数据录入、表单填写）
- 需要AI辅助的复杂网页操作（如电商下单、信息爬取）
- 替代Power Automate等传统自动化工具的现代化解决方案
- 需要与自然语言交互完成浏览器任务的场景

## 4. 技术亮点
- 创新性地将LLM与浏览器自动化结合，实现语义级理解而非简单的规则匹配
- 兼容主流自动化框架，灵活适配不同技术栈
- 高星标数（22832）证明其在AI自动化领域的受欢迎程度和实用性
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22832 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介

CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，专为视觉AI开发设计。它提供开源、云端和企业级产品，支持图像、视频和3D标注，并配备AI辅助标注、质量保证、团队协作、数据分析及开发者API等功能。

### 2. 核心功能

- **AI辅助标注**：利用预训练模型自动识别和标注目标，大幅提升标注效率
- **多格式支持**：支持图像、视频和3D数据的标注，涵盖边界框、语义分割等多种标注类型
- **团队协作**：支持多人协作标注项目，配备质量保证机制确保数据准确性
- **开发者API**：提供完整的API接口，便于集成到现有工作流程中
- **数据分析**：内置数据分析工具，帮助监控标注进度和质量

### 3. 适用场景

- **目标检测数据集构建**：用于训练YOLO、Faster R-CNN等检测模型的数据标注
- **视频行为分析**：对视频序列进行逐帧标注，适用于监控分析和行为识别
- **医疗影像标注**：对医学图像进行精确标注，辅助AI辅助诊断系统开发
- **自动驾驶数据集**：对道路场景图像和视频进行多目标标注，训练自动驾驶算法

### 4. 技术亮点

- 基于Web的架构，无需安装客户端即可通过浏览器使用
- 支持TensorFlow和PyTorch框架的模型集成
- 提供从ImageNet到自定义数据集的完整标注流程支持
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16573 | 🍴 3811 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
该项目是一个用于计算机视觉的高级AI可解释性工具库，支持多种主流深度学习模型。它通过可视化技术帮助用户理解模型的决策依据，提升模型透明度与可信度。

### 2. 核心功能
- 支持CNN和Vision Transformer架构的梯度加权类激活映射（Grad-CAM）
- 提供Score-CAM等替代性类激活可视化方法
- 兼容图像分类、目标检测、图像分割等多种任务类型
- 支持图像相似度分析的可解释性可视化
- 基于PyTorch框架，易于集成到现有项目中

### 3. 适用场景
- 深度学习模型调试：定位模型关注的图像区域，排查误判原因
- 医疗影像分析：辅助医生理解AI诊断依据，提升临床可信度
- 自动驾驶系统：可视化车辆识别决策过程，增强系统安全性
- 学术研究：用于可解释AI（XAI）相关论文的实验与可视化

### 4. 技术亮点
- 支持多种CAM变体（Grad-CAM、Grad-CAM++、Score-CAM等），满足不同精度需求
- 兼容主流视觉Transformer（ViT、Swin Transformer等），紧跟技术前沿
- 提供直观的热力图可视化输出，便于结果展示与交流
- 12957+星标表明社区认可度高，文档完善，使用门槛较低
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# 项目分析：Kornia

## 1. 中文简介

Kornia 是一个面向空间人工智能（Spatial AI）的几何计算机视觉库，基于 PyTorch 构建。它提供了一套可微分的图像处理与计算机视觉算子，支持在深度学习框架中无缝集成传统的几何视觉任务。

## 2. 核心功能

- **可微分图像处理**：提供可微分的图像变换、滤波、形态学等操作，支持端到端训练。
- **几何视觉算子**：包含相机标定、单应性估计、透视变换等经典几何视觉功能。
- **PyTorch 原生集成**：完全基于 PyTorch，与现有深度学习流程无缝兼容。
- **批量张量处理**：支持 NCHW 格式的批量图像处理，适合 GPU 加速。
- **机器人视觉支持**：提供适用于机器人领域的视觉感知工具。

## 3. 适用场景

- **自动驾驶与机器人导航**：用于视觉定位、SLAM 和空间感知任务。
- **图像配准与拼接**：适用于多视图图像对齐、全景拼接等场景。
- **深度学习视觉 pipeline**：作为可微分预处理模块嵌入神经网络训练流程。
- **AR/VR 空间计算**：支持增强现实中的相机姿态估计和空间重建。

## 4. 技术亮点

- 作为**首个以 PyTorch 为核心的可微分几何视觉库**，填补了传统计算机视觉与现代深度学习之间的桥梁。
- 社区活跃，被广泛应用于学术研究和工业界，是空间 AI 领域的重要开源项目之一。
- 链接: https://github.com/kornia/kornia
- ⭐ 11323 | 🍴 1231 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3485 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3389 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2635 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2507 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

---

### 1. 中文简介
OpenClaw 是一款开源的个人 AI 助手，支持任意操作系统和平台，让你完全掌控自己的数据，以"龙虾"的方式重新定义个人 AI 体验。

---

### 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行。
- **数据自主可控**：强调"own-your-data"理念，用户数据完全由自己掌控。
- **个人 AI 助手**：提供智能化的个人助理功能。
- **开源免费**：基于开源协议发布，可自由使用和修改。

---

### 3. 适用场景
- **个人日常助理**：用于日程管理、信息查询等日常任务。
- **数据隐私敏感用户**：希望将 AI 助手部署在本地、避免数据上传云端的使用者。
- **开发者自托管需求**：希望基于开源项目二次开发或定制功能的开发者。
- **多平台用户**：需要在不同操作系统间无缝切换使用 AI 助手的用户。

---

### 4. 技术亮点
- 使用 TypeScript 开发，具备良好的类型安全性和可维护性。
- 支持多平台部署，适配性强。
- 强调本地化/私有化部署，保障用户数据隐私安全。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387133 | 🍴 81311 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

## 1. 中文简介
Superpowers 是一个经过验证的 AI 代理技能框架与软件开发方法论，专注于通过子代理驱动开发流程来提升软件工程效率。它将 AI 代理能力与结构化开发流程相结合，帮助团队更高效地完成软件构建。

## 2. 核心功能
- **代理驱动开发**：通过子代理协作完成复杂的软件开发任务。
- **技能框架**：提供可复用的 AI 代理技能模块，支持多种开发场景。
- **完整 SDLC 支持**：覆盖需求分析、编码、测试到部署的整个软件开发生命周期。
- **头脑风暴辅助**：内置 AI 协作工具，支持创意构思与技术决策。
- **方法论集成**：将 ORBA（目标-结果-行为-评估）框架融入开发流程。

## 3. 适用场景
- AI 辅助的软件开发团队，希望利用多代理协作提升编码效率。
- 需要进行大规模头脑风暴和技术方案设计的创新项目。
- 希望将 AI 代理能力集成到现有软件开发流程中的企业。
- 探索下一代软件工程方法论的研究与实验项目。

## 4. 技术亮点
- 基于 Shell 脚本实现，轻量级且易于集成到现有工作流。
- 采用子代理驱动开发（Subagent-Driven Development）模式，实现任务自动分解与并行执行。
- 高人气项目（27.6万星标），拥有活跃的开源社区和持续迭代。
- 链接: https://github.com/obra/superpowers
- ⭐ 276119 | 🍴 24692 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# hermes-agent 项目分析

## 1. 中文简介
hermes-agent 是一款能够伴随用户共同成长的 AI 智能代理，具备持续学习与记忆能力，可随使用不断适应用户需求和工作习惯。

## 2. 核心功能
- **持续学习**：智能代理可根据用户交互不断优化自身表现
- **多模型支持**：兼容 Claude、GPT、Codex 等多个主流 LLM 提供商
- **记忆系统**：具备长期记忆能力，记住用户偏好和历史对话
- **自主代理**：可独立完成复杂任务，无需人工干预

## 3. 适用场景
- **个人助手**：作为日常工作的智能助理，处理各类任务
- **代码开发**：辅助编程、代码审查和自动化开发流程
- **知识管理**：整合用户知识体系，提供个性化信息检索
- **自动化工作流**：执行重复性任务，提升工作效率

## 4. 技术亮点
- **多模型集成**：支持 Anthropic Claude、OpenAI GPT 等多个大语言模型
- **可扩展架构**：基于 Python 构建，易于扩展和定制
- **Nous Research 开发**：由 Nous Research 团队维护，具备较强的技术实力
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 234352 | 🍴 47143 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码开源的工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码结合，可自托管或云端部署，提供 400+ 种集成方案。

### 2. 核心功能
- 可视化工作流编辑器，支持拖拽式节点连接
- 原生 AI/LLM 集成，可直接调用大语言模型
- 400+ 预置集成，覆盖主流 SaaS 服务和 API
- 支持自托管与云端部署两种模式
- 允许自定义代码节点，满足复杂业务逻辑

### 3. 适用场景
- 企业自动化业务流程（如数据同步、任务调度）
- AI 应用工作流编排（如 RAG 系统、Agent 管道）
- 低代码/无代码集成平台，连接各类 API 和服务
- MCP（Model Context Protocol）客户端与服务端开发

### 4. 技术亮点
- 采用 TypeScript 开发，类型安全且生态完善
- 支持 MCP 协议，可与 AI 工具链深度集成
- Fair-code 许可证，平衡开源与商业使用
- 节点化架构设计，扩展性强，社区活跃（20万+ 星标）
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201755 | 🍴 60298 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 承载着让每个人都能使用并构建 AI 的愿景。我们的使命是提供所需工具，让你能够专注于真正重要的事物。

## 2. 核心功能
- 支持自主执行复杂任务，无需人工持续干预
- 可调用多种大语言模型（GPT、Claude、LLaMA 等）
- 提供浏览器操作、文件读写、API 调用等工具链
- 支持多代理协作，实现任务分解与并行处理
- 开放可扩展架构，允许开发者自定义工具和插件

## 3. 适用场景
- 自动化重复性工作流程（如数据收集、报告生成）
- 研究任务（自动搜索信息、整理文献、撰写摘要）
- 内容创作与编辑（文章撰写、翻译、代码生成）
- 个人助理（日程管理、邮件处理、信息查询）

## 4. 技术亮点
- 采用分层代理架构，实现任务的递归分解与执行
- 支持记忆持久化，可在会话间保持上下文
- 集成向量数据库，实现长期记忆与知识检索
- 提供可视化监控面板，便于跟踪代理执行过程
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186769 | 🍴 46051 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 170903 | 🍴 9495 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167762 | 🍴 21653 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164612 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157957 | 🍴 46173 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153563 | 🍴 9909 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

