# GitHub AI项目每日发现报告
日期: 2026-08-21

## 新发布的AI项目

### coldcard-airgap
- 

# GitHub项目分析：coldcard-airgap

## 1. 中文简介
该项目为Coldcard硬件钱包用户提供一系列离线工具，包括PSBT检查、BIP39/骰子熵生成、Seed XOR分割与合并、BBQr编码解码、输出描述符以及固件验证指南。作为官方Coldcard固件的配套工具，但与Coinkite公司无隶属关系。

## 2. 核心功能
- PSBT（部分签名的比特币交易）离线检查工具，确保交易安全无误
- BIP39助记词与骰子熵生成工具，支持手动安全种子创建
- Seed XOR分割与合并功能，实现种子备份的安全拆分与重组
- BBQr编码/解码工具，支持离线QR码数据交换
- 输出描述符生成与固件验证指南，辅助硬件钱包安全配置

## 3. 适用场景
- Coldcard硬件钱包用户进行离线交易准备和验证
- 需要安全分割种子备份的用户，通过XOR方式分散存储风险
- 希望通过骰子等物理随机源生成高安全性助记词的用户
- 需要离线QR码数据传输的airgap（气隙）钱包用户

## 4. 技术亮点
- 纯Python实现，无需特殊依赖，便于审计和修改
- 专注于离线安全场景，符合airgap钱包最佳实践
- 与官方Coldcard固件互补，但不受官方控制，保持独立性
- 链接: https://github.com/Leutenegger/coldcard-airgap
- ⭐ 608 | 🍴 79 | 语言: Python
- 标签: airgap, airgap-devkit, airgap-download, airgap-setup, airgap-tutorial

### lanshu-create-ai-presenter-video
- 

## GitHub项目分析：lanshu-create-ai-presenter-video

### 1. 中文简介
这是一个与平台无关的 Codex Skill，能够根据脚本和授权的主播图片生成经过验证的AI主播视频。它支持将文字脚本转化为由数字人出镜讲解的视频内容。

### 2. 核心功能
- 根据文本脚本自动生成AI主播口播视频
- 支持使用授权的主播形象图片驱动数字人
- 与Codex Skill框架集成，提供标准化的视频生成流程
- 跨平台兼容，不绑定特定AI服务供应商
- 输出经过验证的高质量数字人视频

### 3. 适用场景
- 企业宣传视频制作：快速生成品牌介绍视频
- 在线教育课程：将课件脚本转化为讲师讲解视频
- 社交媒体内容：批量生产短视频用于平台分发
- 产品演示：用数字人进行产品介绍和推广

### 4. 技术亮点
- **供应商中立设计**：不依赖单一AI服务，可灵活切换底层模型
- **Codex Skill集成**：标准化调用方式，便于嵌入自动化工作流
- **授权形象验证**：确保使用授权的主播图片，保障内容合规性
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 237 | 🍴 25 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### github-farm
- 

## GitHub项目分析：github-farm

### 1. 中文简介
这是一个面向AI网关的生产级多平台OAuth认证采集与会话管理框架，专为AI Agent友好设计。它支持从多个平台统一获取OAuth令牌并管理会话状态，帮助AI网关实现跨平台的身份认证集成。

### 2. 核心功能
- 支持多平台OAuth认证令牌采集与管理
- 提供会话状态统一管理机制
- 专为AI Agent和AI网关场景优化设计
- 生产级稳定性与可扩展性架构
- 简化跨平台身份认证集成流程

### 3. 适用场景
- AI网关需要集成多个第三方平台（如GitHub、Google、Twitter等）的OAuth认证
- 构建需要用户身份验证的AI应用服务
- 多平台会话统一管理的需求场景
- AI Agent需要跨平台获取用户授权信息的场景

### 4. 技术亮点
- 专为AI Agent场景优化，降低集成复杂度
- 生产级框架设计，具备高可用性和稳定性
- 统一的多平台OAuth管理，减少重复开发工作
- 支持会话生命周期管理，提升用户体验
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 101 | 🍴 8 | 语言: Python

### narralume
- 

## narralume 项目分析

### 1. 中文简介
narralume 是一款开源的 AI 辅助长篇小说写作工作室。它将故事设定、正文版本管理、AI 协作、审稿与交付等功能融为一体，为长篇小说创作提供一站式写作工具。

### 2. 核心功能
- **故事设定管理**：支持世界观、角色、地点等设定资料的系统化整理与维护。
- **正文版本控制**：提供章节级别的版本管理，方便追踪写作进度与历史修改。
- **AI 协作写作**：集成大语言模型，辅助作者进行内容生成、续写与润色。
- **审稿与交付一体化**：内置审稿流程，支持从草稿到最终交付的完整创作链路。
- **支持本地自托管**：项目可私有化部署，保障创作内容的隐私与数据安全。

### 3. 适用场景
- **长篇小说创作**：适合需要大量设定与章节管理的长篇网文、小说作者。
- **AI 辅助写作**：需要借助 AI 进行灵感激发、大纲生成或内容续写的创作者。
- **私人化写作空间**：重视内容隐私、希望自建写作环境的专业作者或写手。
- **故事世界观构建**：需要系统化管理角色、时间线、设定资料的奇幻/科幻类作者。

### 4. 技术亮点
- 基于 **TypeScript** 开发，具备类型安全与良好的工程化基础。
- 支持 **LLM（大语言模型）集成**，实现 AI 辅助写作能力。
- **自托管架构**，作者可完全掌控数据，无需依赖第三方云服务。
- 标签涵盖 creative-writing、storytelling 等，定位清晰，聚焦长篇小说写作场景。
- 链接: https://github.com/abligail/narralume
- ⭐ 72 | 🍴 14 | 语言: TypeScript
- 标签: ai-writing, creative-writing, llm, long-form-writing, novel-writing

### neurocursor-ai
- 描述: AI-powered, camera-based mouse cursor control written in C++. Turn your webcam into a hands-free pointing device — built for gaming, perfect for everyday use and accessibility.
- 链接: https://github.com/stems-arraign-48/neurocursor-ai
- ⭐ 50 | 🍴 0 | 语言: C++
- 标签: ai, computer-vision, cplusplus, cpp, cursor-control

### AItoFigma
- 描述: 一个 AI skill，可以把图片或是直接是内容输出到 figma，并且有这规范的尺寸
- 链接: https://github.com/Niall-Young/AItoFigma
- ⭐ 44 | 🍴 4 | 语言: JavaScript

### jiaojie-skill
- 描述: 交接 Skill（Jiaojie）：跨窗口、跨模型、跨设备、跨语言的 AI 上下文交接工具。换窗口，不失忆；换模型，不重来。Open-source AI context handoff.
- 链接: https://github.com/Jordanwei1/jiaojie-skill
- ⭐ 38 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agent, ai-agents, ai-memory, claude-code

### KPMG_2_GLB
- 描述: This repository contains the lecture materials, notebooks, code, datasets, assignments, demonstrations, and resources used during the Industry-Oriented AI Foundamentals Training Program conducted in August 2026.
- 链接: https://github.com/AnantVerma-2022/KPMG_2_GLB
- ⭐ 29 | 🍴 0 | 语言: Jupyter Notebook

### lieflat-less-ai-tone
- 描述: 一个基于 283 万字语料统计的去 AI 味 skill · An AI-tone removal skill grounded in a 2.83-million-character corpus study
- 链接: https://github.com/larashero3-dotcom/lieflat-less-ai-tone
- ⭐ 27 | 🍴 0 | 语言: Python

### cs-board
- 描述: 将参考声音和中文文案自动生成白板动画视频的本地 AI 工具。
- 链接: https://github.com/ChenShuo2004/cs-board
- ⭐ 27 | 🍴 4 | 语言: Python
- 标签: ai-video, chinese, fastapi, index-tts, react

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## 1. 中文简介

funNLP 是一个全面的中文自然语言处理资源集合项目，涵盖了敏感词检测、语言识别、信息抽取、词库资源、预训练模型、知识图谱、语音识别等多个领域的工具和数据集。该项目汇集了丰富的中文NLP开源资源，包括BERT、ALBERT等预训练模型，以及大量专业领域词库和竞赛数据集，是中文NLP研究和开发的重要资源库。

## 2. 核心功能

- **敏感词与文本检测**：支持中英文敏感词检测、语言识别、繁简体转换及文本情感分析
- **信息抽取工具**：提供手机号、身份证、邮箱抽取，以及命名实体识别、关系抽取、事件抽取等功能
- **丰富词库资源**：包含中日文人名库、汽车品牌词库、成语词库、医学/法律/财经等专业领域词库
- **预训练模型与词向量**：集成BERT、ALBERT、ELECTREA等预训练模型及多种中文词向量资源
- **对话与生成系统**：提供聊天机器人、文本摘要、自动对联、歌词生成等自然语言生成工具

## 3. 适用场景

- **内容审核平台**：利用敏感词库和暴恐词表构建内容过滤系统
- **企业知识图谱构建**：借助命名实体识别和关系抽取工具搭建领域知识库
- **智能客服与对话系统**：使用对话数据集和预训练模型开发智能问答系统
- **中文NLP研究与教学**：作为学习资源库，涵盖数据集、基准模型和竞赛方案

## 4. 技术亮点

- 收录清华XLORE跨语言知识图谱、百度信息抽取系统等顶级开源项目
- 提供CLUENER细粒度NER、中文谣言检测等竞赛级高质量数据集
- 集成Jiagu、HarvestText等国产优秀NLP工具，支持新词发现与领域自适应
- 涵盖从传统NLP（分词、词性标注）到深度学习（BERT、Transformer）的完整技术栈
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82585 | 🍴 15272 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
该项目是一个精选的AI项目合集，包含500个涵盖机器学习、深度学习、计算机视觉和自然语言处理领域的完整项目代码。每个项目都配有可运行的代码示例，适合从入门到进阶的学习者参考实践。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带可运行的代码和详细说明
- 项目按领域分类，便于快速定位学习方向

### 3. 适用场景
- AI初学者系统学习各方向项目实战
- 开发者寻找项目灵感与代码参考
- 面试官准备AI相关技术面试题目
- 企业技术选型时评估不同方案实现

### 4. 技术亮点
- 项目数量庞大（500个），覆盖主流AI技术栈
- 所有项目均配有代码，可直接运行学习
- 采用"Awesome List"形式整理，质量经过社区筛选
- 星标数高达36432，说明项目受到广泛认可
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36432 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流模型格式，可直观展示模型结构与参数，帮助用户更好地理解和分析模型架构。

## 2. 核心功能
- 支持多种模型格式，包括 TensorFlow、PyTorch、ONNX、CoreML、Keras 等
- 提供图形化界面展示神经网络层结构、连接关系和参数信息
- 支持模型推理调试，可输入数据并查看各层输出结果
- 兼容浏览器和桌面端，无需安装即可在线使用
- 支持 safetensors 等新兴模型格式

## 3. 适用场景
- 深度学习模型开发与调试：可视化模型结构，快速定位问题
- 模型格式转换验证：检查转换后模型的完整性与正确性
- 学术研究与论文展示：生成清晰的模型架构图用于论文或演示
- 模型部署前审查：在部署到移动端或嵌入式设备前检查模型配置

## 4. 技术亮点
- 纯前端实现，基于 JavaScript，无需后端服务即可运行
- 支持 3D 可视化，可旋转查看模型结构
- 社区活跃，持续更新支持最新框架和模型格式
- 完全免费开源，GitHub 星标数超过 3.3 万，深受开发者喜爱
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开放的机器学习互操作性标准，旨在打破不同深度学习框架之间的壁垒。它允许开发者在不同框架之间自由迁移模型，实现从训练到部署的无缝衔接。

### 2. 核心功能
- **统一模型格式**：提供标准化的模型表示格式，支持跨框架模型交换
- **框架兼容性**：支持 PyTorch、TensorFlow、Keras、scikit-learn 等多种主流框架
- **推理优化**：提供 ONNX Runtime 加速推理，支持 GPU、CPU 等多种硬件后端
- **工具链支持**：配备模型转换、可视化和调试等完整工具生态
- **跨平台部署**：支持在移动设备、嵌入式系统和云端等多种环境中运行

### 3. 适用场景
- **模型迁移**：将模型从 PyTorch/TensorFlow 等训练框架迁移到部署环境
- **生产部署**：利用 ONNX Runtime 在服务器或边缘设备上高效运行推理
- **框架选型灵活**：在不同训练框架间自由切换，降低技术栈锁定风险
- **模型优化**：对模型进行图优化、量化和压缩以提升推理性能

### 4. 技术亮点
- 由微软、Facebook 等科技巨头联合推动，已成为 ML 互操作性的事实标准
- 支持超过 200 种算子，覆盖绝大多数深度学习模型结构
- 与主流硬件厂商深度合作，实现广泛的底层硬件加速支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21341 | 🍴 4007 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub 项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的技术参考书。内容涵盖模型训练、调试、推理部署及大规模分布式系统的核心知识，是AI工程师的实用指南。

## 2. 核心功能
- 提供大语言模型（LLM）从训练到推理的完整工程实践指导
- 深入讲解GPU集群调度、网络优化与存储管理
- 覆盖PyTorch框架下的可扩展训练与模型调试技巧
- 包含MLOps生产环境部署的最佳实践

## 3. 适用场景
- 大规模LLM模型的分布式训练与调优
- GPU集群的资源调度与性能优化
- 模型推理服务的高吞吐部署
- MLOps流水线搭建与工程化落地

## 4. 技术亮点
- 基于Slurm等作业调度系统的实战经验总结
- 针对Transformer架构的训练稳定性优化方案
- 结合真实生产场景的故障排查与调试方法论
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18681 | 🍴 1203 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
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

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介

该项目是一个收录了500个AI相关项目的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，所有项目均附带完整代码实现。它是一个面向开发者和学习者的"awesome"列表资源库，帮助快速找到高质量的学习与实战项目。

---

### 2. 核心功能

- 收录500个AI领域项目，覆盖机器学习、深度学习、计算机视觉和NLP四大方向
- 每个项目均附带可运行的代码，方便直接学习和实践
- 按技术领域分类整理，便于快速定位感兴趣的项目
- 提供项目链接直达原始仓库，支持进一步深入学习
- 持续更新，保持项目库的时效性和丰富度

---

### 3. 适用场景

- **AI学习者**：系统学习机器学习、深度学习等技术的实战参考
- **开发者求职**：作为项目作品集，展示AI开发能力
- **教师/培训**：作为课程教学的项目案例库
- **技术调研**：快速了解AI各领域的热门项目和实现方案

---

### 4. 技术亮点

- 项目数量庞大（500个），覆盖AI主流技术方向，资源密度高
- 所有项目均含代码，兼顾理论学习与动手实践
- 采用"Awesome List"经典整理方式，结构清晰、易于检索
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36432 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流模型格式，可直观展示模型结构与参数，帮助用户更好地理解和分析模型架构。

## 2. 核心功能
- 支持多种模型格式，包括 TensorFlow、PyTorch、ONNX、CoreML、Keras 等
- 提供图形化界面展示神经网络层结构、连接关系和参数信息
- 支持模型推理调试，可输入数据并查看各层输出结果
- 兼容浏览器和桌面端，无需安装即可在线使用
- 支持 safetensors 等新兴模型格式

## 3. 适用场景
- 深度学习模型开发与调试：可视化模型结构，快速定位问题
- 模型格式转换验证：检查转换后模型的完整性与正确性
- 学术研究与论文展示：生成清晰的模型架构图用于论文或演示
- 模型部署前审查：在部署到移动端或嵌入式设备前检查模型配置

## 4. 技术亮点
- 纯前端实现，基于 JavaScript，无需后端服务即可运行
- 支持 3D 可视化，可旋转查看模型结构
- 社区活跃，持续更新支持最新框架和模型格式
- 完全免费开源，GitHub 星标数超过 3.3 万，深受开发者喜爱
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介
该项目为深度学习与机器学习研究者提供了一系列实用的速查手册（Cheat Sheets），涵盖从基础概念到高级工具的常用知识，帮助研究者快速回顾和查阅核心内容。

### 2. 核心功能
- 提供深度学习与机器学习领域的关键概念速查表
- 涵盖 NumPy、SciPy、Matplotlib 等科学计算工具的使用技巧
- 包含 Keras 等主流深度学习框架的常用操作速查
- 整理人工智能研究中的必备知识点与代码片段

### 3. 适用场景
- 机器学习/深度学习研究者在开发过程中快速查阅语法和 API
- 学生或初学者系统复习 AI 领域的核心概念与工具
- 数据科学家在日常工作中参考常用数学库和可视化工具用法
- 面试准备时快速巩固 AI 相关知识要点

### 4. 技术亮点
- 由 Medium 博主 Kailash Ahirwar 整理发布，内容经过社区验证
- 涵盖从底层数学库（NumPy/SciPy）到高层框架（Keras）的完整技术栈
- 高星标数（15,427）表明该资源在开发者社区中具有较高的认可度和实用性
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# Ai-Learn 项目分析

## 1. 中文简介
Ai-Learn 是一份系统化的人工智能学习路线图，收录了近 200 个实战案例与项目，并提供免费配套教材，帮助零基础学习者入门并掌握就业实战技能。内容覆盖 Python、机器学习、深度学习、数据分析、计算机视觉、自然语言处理等热门领域。

## 2. 核心功能
- 提供从 Python 基础到 AI 就业的完整学习路径
- 整理近 200 个实战案例与项目供学习者实践
- 免费提供配套教材，降低学习门槛
- 涵盖机器学习、深度学习、NLP、CV 等多领域技术栈

## 3. 适用场景
- 零基础想转入 AI 领域的新手系统学习
- 希望梳理知识体系、查漏补缺的在校学生
- 需要准备项目实战以提升就业竞争力的求职者

## 4. 技术亮点
- 学习路径清晰，覆盖从 Python 到深度学习的全栈 AI 技能
- 实战资源丰富，近 200 个项目案例贴近实际应用
- 免费开源，配套教材完整，适合自学入门
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式的 YAML 配置文件简化模型开发流程，让开发者无需编写大量代码即可完成模型训练与部署。

### 2. 核心功能
- 低代码/零代码模型构建，通过 YAML 声明式配置完成训练
- 支持大语言模型（LLM）的微调与训练，兼容 LLaMA、Mistral 等主流模型
- 涵盖计算机视觉、自然语言处理（NLP）等多种 AI 任务
- 基于 PyTorch 实现，提供完整的数据集管理、训练、评估流程
- 支持数据驱动（Data-Centric）开发模式，便于快速迭代优化

### 3. 适用场景
- 企业快速构建和部署定制化 AI 模型，降低开发门槛
- 对 LLaMA、Mistral 等大语言模型进行领域微调（Fine-tuning）
- 数据科学家进行深度学习实验，快速验证模型想法
- 需要端到端机器学习流水线（从数据到部署）的科研与工程团队

### 4. 技术亮点
- 采用声明式配置，大幅提升模型开发效率
- 内置丰富的数据集类型支持（文本、图像、数值、类别等），开箱即用
- 与主流大模型生态兼容，简化 LLM 微调工作流
- 社区活跃，Star 数超过 1.1 万，生态完善
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9180 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8968 | 🍴 3109 | 语言: C++
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
- ⭐ 6423 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP是一个全面的中文自然语言处理资源汇总仓库，集成了敏感词检测、实体抽取、词库资源、预训练模型、知识图谱及多领域数据集等丰富内容，为中文NLP开发者和研究者提供一站式解决方案。

### 2. 核心功能
- 提供敏感词过滤、语言检测、手机号/身份证/邮箱抽取等基础NLP工具
- 整合BERT、GPT-2、ALBERT等主流预训练语言模型及多领域词库资源
- 支持知识图谱构建、关系抽取、实体链接及问答系统开发
- 涵盖语音识别、OCR文字识别、文本摘要、情感分析等实用工具包
- 收录大量中文NLP竞赛数据集、基准测评及开源代码实现

### 3. 适用场景
- 内容审核平台：敏感词过滤、谣言检测、文本分类
- 智能客服系统：对话机器人、知识图谱问答、意图识别
- 企业数据抽取：身份证/手机号识别、实体抽取、信息结构化
- 学术研究：NLP基准测评、预训练模型微调、数据集获取

### 4. 技术亮点
- 汇集82585+星标，是中文NLP领域最受欢迎且最全面的资源库之一
- 覆盖从基础工具（分词、词性标注）到前沿模型（BERT、GPT-2）的完整技术栈
- 整合知识图谱构建、语音识别、OCR等多模态NLP能力
- 提供多个开源预训练模型仓库（OpenCLaP、UER、Chinese-BERT等）及竞赛TOP方案汇总
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82585 | 🍴 15272 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74281 | 🍴 9083 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，涵盖12周、24课时的系统化学习内容，旨在让所有人都能轻松学习人工智能。课程通过Jupyter Notebook形式提供，内容全面且易于上手。

### 2. 核心功能
- 提供结构化的12周AI学习路径，包含24个课时
- 涵盖机器学习、深度学习、计算机视觉、NLP等核心领域
- 使用Jupyter Notebook作为主要教学载体，支持交互式学习
- 包含CNN、RNN、GAN等主流AI模型的实际案例
- 由微软官方维护，质量有保障且持续更新

### 3. 适用场景
- 零基础学习者系统入门人工智能领域
- 高校或培训机构作为AI课程的配套教材
- 开发者快速补充AI知识体系
- 企业内部分享和团队AI技能培训

### 4. 技术亮点
- 高人气项目（66,094星标），社区活跃且资源丰富
- 微软官方背书，课程内容权威可靠
- 标签覆盖全面：从基础机器学习到进阶的深度学习、计算机视觉、自然语言处理等
- 采用微软"For Beginners"系列的教学风格，通俗易懂
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66094 | 🍴 12808 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## ai-engineering-from-scratch 项目分析

### 1. 中文简介
这是一个从零开始学习AI工程的完整课程项目，采用"学它、构建它、为别人交付它"的实践方法论。项目涵盖从基础理论到实际部署的全流程，适合希望系统掌握AI工程技能的开发者。

### 2. 核心功能
- 从零构建AI Agent、LLM应用和生成式AI系统
- 涵盖计算机视觉、NLP、强化学习等核心AI领域
- 提供完整的课程教程和实战项目
- 支持Python和Rust双语言实现
- 包含MCP（Model Context Protocol）等前沿技术

### 3. 适用场景
- AI工程师系统学习与实践
- 企业AI Agent开发培训
- 生成式AI应用快速原型搭建
- 学术研究与教学参考

### 4. 技术亮点
- 高星标项目（47518）证明其社区认可度
- 覆盖agents、swarm-intelligence、transformers等热门标签
- 结合Python生态与Rust性能优势
- 理论与实践并重的课程设计
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47518 | 🍴 8354 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：ailearning

### 1. 中文简介
这是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK和TensorFlow 2的综合性AI学习项目。项目通过理论与实践结合的方式，帮助学习者系统掌握人工智能领域的核心知识与技能。

### 2. 核心功能
- 提供完整的机器学习算法实现，包括分类、聚类、回归等经典模型
- 集成深度学习框架（PyTorch、TensorFlow 2）进行神经网络实战
- 涵盖自然语言处理（NLP）相关工具与算法（NLTK）
- 包含推荐系统、关联规则挖掘等数据挖掘技术
- 补充线性代数等数学基础，夯实AI学习根基

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习知识
- 数据分析师提升算法实现与工程实践能力
- 高校学生完成课程项目或毕业设计参考
- 开发者快速查阅经典算法的代码实现

### 4. 技术亮点
- 使用高星项目（42470星标）证明其社区认可度与实用价值
- 覆盖从传统机器学习到深度学习的完整技术栈
- 结合多个主流框架（PyTorch、TF2、sklearn）提供多视角实现
- 标签丰富，涵盖SVM、KMeans、LSTM、PCA等核心算法，适合系统性学习
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42470 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36432 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33838 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29168 | 🍴 3554 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21844 | 🍴 3359 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个收录了500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，所有项目均附带完整代码实现。该项目在GitHub上获得了36432个星标，是一个备受社区认可的高质量AI学习资源库。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现，覆盖多个核心技术领域
- 按机器学习、深度学习、计算机视觉、NLP等方向分类整理，便于检索学习
- 每个项目均包含可运行的Python代码，适合实践入门
- 标签体系完善，支持按技术领域快速筛选项目
- 持续更新，收录最新AI项目与前沿技术实践

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习，通过实战项目巩固理论
- 开发者寻找计算机视觉或NLP方向的参考项目，快速上手开发
- 数据科学家浏览最新AI项目趋势，获取灵感与技术选型参考
- 教师或培训机构作为课程实践项目的教学资源库

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流技术栈，资源丰富
- 全部附带代码，强调实战导向，便于直接运行与二次开发
- 标签分类清晰，涵盖artificial-intelligence、deep-learning、computer-vision、nlp等核心领域
- 高星标数（36432）证明项目质量和社区认可度极高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36432 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介

Skyvern 是一个基于 AI 的浏览器自动化平台，利用大语言模型（LLM）和计算机视觉技术，自动完成基于浏览器的复杂工作流。它通过理解网页内容和用户意图，实现无需编写脚本的智能自动化操作。

## 2. 核心功能

- **AI 驱动的浏览器操作**：利用 LLM 理解页面内容并自动执行点击、填写、导航等操作
- **计算机视觉辅助**：通过视觉识别定位页面元素，减少对 DOM 结构的依赖
- **多浏览器引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **可视化工作流编排**：支持通过 API 或可视化界面定义和编排自动化任务
- **无代码/低代码模式**：用户只需描述任务目标，AI 自动完成剩余操作

## 3. 适用场景

- **RPA（机器人流程自动化）**：替代传统规则型 RPA，处理复杂且多变的网页交互
- **数据抓取与填报**：自动化跨网站的数据采集、表单填写和数据同步
- **QA 测试自动化**：模拟真实用户行为进行端到端测试，适应页面动态变化
- **企业工作流集成**：与 Power Automate 等企业工具对接，实现跨系统自动化

## 4. 技术亮点

- 将 **LLM 语义理解** 与 **视觉感知** 结合，突破传统自动化对固定选择器的依赖
- 支持 **多模型切换**（GPT、Claude 等），可根据任务灵活选择推理引擎
- 提供 **REST API 接口**，便于集成到现有系统和 CI/CD 流程中
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22821 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台。它提供开源、云端和企业级产品，以及标注服务，支持图像、视频和3D数据的标注，具备AI辅助标注、质量保证、团队协作、数据分析和开发者API等核心能力。

### 2. 核心功能
- **AI辅助标注**：利用预训练模型自动识别和标注目标，大幅提升标注效率
- **多模态标注支持**：支持图像、视频和3D点云数据的标注
- **质量保证机制**：提供标注质量校验和审核功能
- **团队协作**：支持多人协同标注、任务分配和管理
- **开发者API**：提供完善的API接口，便于集成到现有工作流

### 3. 适用场景
- **深度学习项目**：为图像分类、目标检测、语义分割等任务构建训练数据集
- **自动驾驶研发**：对视频和3D数据进行道路场景标注
- **企业数据标注**：作为团队标注平台，管理大规模数据标注项目
- **学术研究**：为计算机视觉研究提供标准化数据集标注工具

### 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供丰富的标注类型：边界框、多边形、关键点、语义分割等
- 兼容ImageNet等主流数据集格式
- 拥有高社区活跃度（16559+星标），生态成熟
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16559 | 🍴 3809 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

---

## 1. 中文简介

这是一个面向计算机视觉的高级AI可解释性工具包，支持多种可视化方法。兼容CNN和Vision Transformer等主流模型架构，适用于分类、目标检测、分割、图像相似度等多种任务的可解释性分析。

---

## 2. 核心功能

- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种经典可视化方法
- 兼容CNN和Vision Transformer（ViT）等主流深度学习模型架构
- 覆盖图像分类、目标检测、语义分割、图像相似度等多种CV任务
- 提供类激活图（CAM）可视化，直观展示模型关注区域
- 基于PyTorch实现，API简洁易用，易于集成到现有项目中

---

## 3. 适用场景

- **模型调试与优化**：分析模型决策依据，定位模型"误判"区域，辅助模型改进
- **医学影像分析**：可视化模型关注的病灶区域，增强医疗AI的可信度
- **自动驾驶感知验证**：分析模型对道路元素（行人、车辆、交通标志）的关注点
- **学术研究**：用于可解释AI（XAI）领域的论文实验与结果可视化

---

## 4. 技术亮点

- 实现了Grad-CAM系列方法的完整变体，代码质量高、社区认可度高（12955+星标）
- 对Vision Transformer提供原生支持，适配最新模型架构
- 模块化设计，可灵活扩展新的可视化方法
- 文档完善，提供清晰的示例代码，上手门槛低
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12955 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# Kornia 项目分析

## 1. 中文简介
Kornia 是一个基于 PyTorch 的开源几何计算机视觉库，专为空间人工智能应用设计。它将经典的计算机视觉算法与深度学习框架无缝集成，为研究人员和开发者提供了一套高效、可微分的图像处理工具。

## 2. 核心功能
- **可微分图像处理**：提供完全可微分的图像变换、几何操作和滤镜功能，可直接集成到神经网络中
- **3D 计算机视觉支持**：内置相机标定、立体视觉、3D 重建等几何计算模块
- **批量并行处理**：基于 PyTorch 张量操作，支持 GPU 加速的大批量图像处理
- **与 PyTorch 生态无缝集成**：可直接使用 PyTorch 的自动微分和模型构建功能
- **机器人视觉工具集**：提供面向机器人应用的视觉感知和空间理解算法

## 3. 适用场景
- **深度学习视觉模型开发**：在神经网络中嵌入可微分的图像预处理和后处理步骤
- **机器人视觉系统**：用于机器人导航、物体识别和空间感知任务
- **3D 重建与 SLAM**：适用于同时定位与建图、多视图几何等研究项目
- **工业图像处理**：需要 GPU 加速批量图像处理的自动化检测场景

## 4. 技术亮点
- **端到端可微分管道**：从图像输入到几何输出的完整可微分流程，支持梯度反向传播
- **JIT 编译优化**：支持 TorchScript 编译，提升推理性能
- **模块化设计**：功能模块清晰，易于扩展和定制
- **活跃的开源社区**：拥有超过 11000 星标，持续维护和更新
- 链接: https://github.com/kornia/kornia
- ⭐ 11321 | 🍴 1228 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3483 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3388 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2507 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

# OpenClaw 项目分析

## 1. 中文简介
OpenClaw 是一款个人 AI 助手工具，支持任意操作系统和平台运行，采用"龙虾"方式（强调数据自主可控）。用户可完全掌控自己的 AI 助手，实现私有化部署与使用。

## 2. 核心功能
- 跨平台支持，兼容任意操作系统
- 个人数据完全自主，无需依赖第三方云服务
- 基于 TypeScript 开发，具有良好的可扩展性
- 提供类似"龙虾"形态的本地化 AI 助手体验
- 支持自定义配置，满足个性化需求

## 3. 适用场景
- 注重数据隐私的个人用户，希望本地运行 AI 助手
- 需要跨平台一致体验的开发者或技术爱好者
- 希望完全掌控 AI 助手行为和数据的企业用户
- 对现有云端 AI 服务存在隐私担忧的用户

## 4. 技术亮点
- 采用 TypeScript 编写，代码类型安全且易于维护
- 开源项目，社区活跃（38万+星标），生态完善
- 强调"own-your-data"理念，实现真正的本地化部署
- 项目标识独特（龙虾主题），具有鲜明的品牌个性
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387035 | 🍴 81296 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub项目分析：superpowers

## 1. 中文简介
一个基于AI代理的技能框架与软件开发方法论，能够实际落地并产生效果。该项目提供了一套完整的智能体驱动开发流程，帮助开发者高效完成从构思到部署的整个软件生命周期。

## 2. 核心功能
- **AI代理驱动开发**：通过子代理协同完成编码任务，实现自动化软件开发
- **技能框架体系**：提供可复用的智能体技能模块，支持灵活组合与扩展
- **头脑风暴辅助**：内置AI协作工具，帮助团队进行创意发散和方案设计
- **完整SDLC支持**：覆盖需求分析、开发、测试到部署的全流程方法论
- **OBRAB（对象行为规则架构）**：独特的软件开发架构方法论

## 3. 适用场景
- **AI辅助编程团队**：需要智能体协作完成复杂软件开发任务
- **快速原型开发**：希望借助AI加速从想法到可运行代码的转化
- **教育培训机构**：教授AI驱动开发方法论和智能体编程实践
- **企业级SDLC优化**：寻求智能化改造传统软件开发流程的组织

## 4. 技术亮点
- 在GitHub获得27万+星标，证明其广泛认可和实用性
- 采用Shell脚本实现，轻量且易于集成到现有工作流中
- 创新性地将AI代理与软件开发方法论深度结合，而非仅作为代码补全工具
- 支持多子代理协同工作，可实现并行开发和复杂任务分解
- 链接: https://github.com/obra/superpowers
- ⭐ 275518 | 🍴 24637 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233901 | 🍴 46941 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一个公平代码许可的工作流自动化平台，内置原生 AI 能力。它支持可视化搭建与自定义代码相结合，可自托管或云端部署，并提供 400 多种集成连接器。

### 2. 核心功能
- **可视化工作流构建**：通过拖拽节点快速搭建自动化流程，降低使用门槛。
- **原生 AI 集成**：内置 AI 能力，支持 LLM 调用、智能分析等 AI 驱动任务。
- **400+ 应用集成**：覆盖主流 SaaS 工具、API 和服务，实现跨平台数据流转。
- **代码与低代码结合**：支持 JavaScript/Python 自定义节点，灵活扩展功能。
- **自托管与云端双模式**：可选择私有化部署保障数据隐私，或使用云端服务快速上手。

### 3. 适用场景
- **企业自动化**：跨系统数据同步、定时报表生成、审批流程自动化。
- **AI 应用开发**：构建基于大语言模型的智能助手、自动化内容生成管道。
- **数据集成与 ETL**：从多源采集数据、清洗转换后写入目标系统。
- **MCP 协议支持**：作为 MCP 客户端/服务器，实现模型上下文协议的标准化接入。

### 4. 技术亮点
- 采用 TypeScript 开发，类型安全且生态友好。
- 支持 MCP（Model Context Protocol）协议，便于与各类 AI 模型集成。
- Fair-code 许可证，兼顾开源协作与商业友好性。
- 节点化架构设计，插件扩展性强，社区活跃。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201517 | 🍴 60265 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186718 | 🍴 46045 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 170452 | 🍴 9481 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167702 | 🍴 21650 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164604 | 🍴 30550 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157930 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153534 | 🍴 9902 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

