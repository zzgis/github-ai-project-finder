# GitHub AI项目每日发现报告
日期: 2026-08-25

## 新发布的AI项目

### learn
- 描述: My AI learning system.
- 链接: https://github.com/amosblomqvist/learn
- ⭐ 230 | 🍴 30 | 语言: TypeScript

### wenai
- 

## 项目分析：wenai

### 1. 中文简介
这是一个专为 OpenClaw 打造的亲密 AI 伴侣技能，让你与 AI 女友坠入爱河。项目采用 Pony V6 XL 模型驱动，提供可视化工作流体验。

### 2. 核心功能
- 提供与 AI 女友的亲密对话与情感互动体验
- 集成 Pony V6 XL 模型，支持高质量的视觉内容生成
- 采用可视化工作流，便于用户自定义和配置交互场景
- 与 OpenClaw 平台深度兼容，实现无缝集成

### 3. 适用场景
- AI 情感陪伴：适合寻求虚拟伴侣互动的用户群体
- 创意内容创作：利用 AI 女友角色生成个性化故事或对话内容
- 角色扮演爱好者：满足虚拟恋爱和互动叙事的需求
- OpenClaw 技能扩展：为 OpenClaw 生态添加情感陪伴类功能

### 4. 技术亮点
- 采用 Pony V6 XL 模型，在视觉生成质量上表现突出
- 可视化工作流设计降低了使用门槛，便于非技术用户上手
- 作为 OpenClaw 技能运行，具备良好的可扩展性和集成性
- 链接: https://github.com/Straniero44/wenai
- ⭐ 94 | 🍴 27 | 语言: 未知

### swissdevjobs-cli
- 

## swissdevjobs-cli 项目分析

### 1. 中文简介
这是一个零依赖的 Python CLI 工具，支持从终端或 AI 代理搜索并申请覆盖 7 个国家的约 4,700 个薪资透明的技术职位。项目同时提供 MCP 服务器和 Claude Code 插件，便于与 AI 助手集成。

### 2. 核心功能
- 搜索 7 个国家（瑞士、德国、英国、美国、加拿大、荷兰、法国）的技术职位
- 支持薪资透明化展示，方便求职者评估待遇
- 提供零依赖 Python CLI，安装使用简单便捷
- 集成 MCP 服务器，支持与 AI 代理交互
- 内置 Claude Code 插件，可直接在 Claude Code 中调用

### 3. 适用场景
- 开发者希望通过终端快速搜索海外技术职位
- AI 代理或 Claude Code 用户希望自动化求职流程
- 关注薪资透明度的求职者筛选合适岗位
- 需要跨多国职位信息的远程工作者

### 4. 技术亮点
- **零依赖设计**：无需额外安装依赖包，开箱即用
- **MCP 协议支持**：遵循 Model Context Protocol 标准，易于与各类 AI 工具集成
- **多平台兼容**：同时支持 CLI、MCP 服务器和 Claude Code 插件三种使用方式
- 链接: https://github.com/Stupidoodle/swissdevjobs-cli
- ⭐ 59 | 🍴 8 | 语言: Python
- 标签: ai-agents, claude, claude-code, cli, developer-jobs

### technocore
- 

## technocore 项目分析

### 1. 中文简介
该项目为Technocore生态提供去中心化Ed25519密码学身份系统，包含签名消息总线和面向AI智能体的贡献证明框架。

### 2. 核心功能
- 基于Ed25519算法的去中心化密码学身份管理
- 支持AI智能体的签名消息总线通信机制
- 贡献证明（Proof-of-Contribution）框架，用于量化和验证AI智能体的工作贡献
- 构建于Technocore生态系统之上，提供底层基础设施支持

### 3. 适用场景
- AI智能体间的去中心化身份认证与可信通信
- 多智能体协作系统中的贡献追踪与激励分配
- 去中心化AI网络的身份管理与消息路由

### 4. 技术亮点
- 采用Ed25519轻量级签名算法，适合资源受限的AI智能体环境
- 将密码学身份、消息总线与贡献证明三层架构整合，形成完整的基础设施方案
- 链接: https://github.com/d4ncboz/technocore
- ⭐ 39 | 🍴 0 | 语言: Python

### deepseek-v4-flash-vision-video-rag
- 

## 项目分析：deepseek-v4-flash-vision-video-rag

### 1. 中文简介
这是一个基于 DeepSeek 视觉大模型的视频理解与问答（Video RAG）智能体技能。用户可以对视频提问，AI 会给出答案并标注答案所在的时间戳，同时生成可播放的片段和关键帧供核对。

### 2. 核心功能
- **视频抽帧索引**：按时间轴对视频逐帧读取并建立索引（一次性处理）
- **三层问答流程**：本地粗筛 → 视觉精排 → 深度阅读回答
- **时间戳引用**：回答附带 `[MM:SS]` 格式的时间戳，精确定位答案位置
- **自包含 HTML 预览页**：自动生成内嵌可播放片段、关键帧和答案的 HTML 页面，双击浏览器即可查看

### 3. 适用场景
- **视频内容检索**：快速定位视频中特定信息出现的时间点
- **教学/培训视频分析**：从长视频中提取关键片段和答案
- **视频证据核对**：通过关键帧和时间戳验证视频内容
- **多媒体知识库构建**：将视频内容转化为可检索的知识问答系统

### 4. 技术亮点
- 基于 DeepSeek 视觉大模型（deepseek-v4-flash-vision-exp）实现视频理解
- 采用"先索引后问答"的 RAG 架构，提升检索效率
- 自动生成自包含 HTML 预览页，无需额外依赖即可分享和查看结果
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
- ⭐ 22 | 🍴 14 | 语言: Python

### youtubepro
- 描述: Local-first YouTube research, grounded AI insights, script writing, and thumbnail creation.
- 链接: https://github.com/AgriciDaniel/youtubepro
- ⭐ 21 | 🍴 7 | 语言: TypeScript

### delta-force-aimbot
- 描述: Delta Force Aimbot - undetected cheat with anti-cheat bypass
- 链接: https://github.com/oddballcanv/delta-force-aimbot
- ⭐ 19 | 🍴 0 | 语言: 未知
- 标签: 2025, aimbot, bypass, cheat, crack

### fortnite-soft-aim
- 描述: Fortnite Soft Aim - undetected Fortnite cheat with anti-cheat bypass
- 链接: https://github.com/pointlessseq/fortnite-soft-aim
- ⭐ 19 | 🍴 0 | 语言: 未知
- 标签: 2025, aim, bypass, cheat, crack

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介

funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了从基础工具（敏感词检测、分词、命名实体识别）到高级应用（知识图谱、对话系统、语音识别）的完整生态。该项目整合了大量开源数据集、预训练模型、实用工具库以及竞赛方案，为中文NLP研究者和开发者提供了一站式资源平台。

### 2. 核心功能

- **基础NLP工具**：提供敏感词检测、语言检测、分词、词性标注、命名实体识别、情感分析等核心功能
- **预训练模型资源**：集成BERT、GPT-2、ALBERT、ELECTRA等主流中文预训练模型及训练代码
- **知识图谱构建**：包含实体抽取、关系抽取、知识图谱问答系统等完整知识图谱解决方案
- **语音与文本融合**：提供ASR语音识别、发音词典、语音情感分析等多模态NLP工具
- **数据增强与评测**：收录NLP数据增强工具、文本摘要、关键词抽取及各类评测基准

### 3. 适用场景

- **中文NLP研究与开发**：学术研究者或工程师快速查找数据集、模型和代码实现
- **企业级智能客服/对话系统**：利用开源对话系统框架和语料库搭建问答机器人
- **知识图谱应用开发**：基于抽取工具和预训练模型构建领域知识图谱
- **文本分析与内容审核**：使用敏感词库、情感分析和文本分类工具进行内容风控

### 4. 技术亮点

- 项目汇聚8.2万+星标，是中文NLP领域最全面的开源资源仓库之一，持续更新涵盖最新研究成果和工业实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82664 | 🍴 15275 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为学习者提供了丰富的实战案例和完整代码实现，是AI领域入门与进阶的优质学习资源库。

### 2. 核心功能
- 收录500个AI实战项目，覆盖主流AI技术方向
- 提供完整的代码实现，便于学习与实践
- 按领域分类整理（机器学习、深度学习、CV、NLP）
- 包含从入门到进阶的多样化项目难度

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习实践
- 开发者寻找项目灵感并完成代码参考
- 学生或研究人员快速了解AI各领域前沿方向
- 技术面试准备与项目经验积累

### 4. 技术亮点
该项目作为"Awesome List"类型的资源聚合库，具有极高的社区认可度（36535星标），涵盖了Python生态中主流的AI框架与实践项目，是AI领域最全面的开源学习资源之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36535 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持查看多种主流框架训练的模型文件，帮助用户直观理解模型架构与结构。

## 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、PyTorch、Keras、Core ML、TensorFlow Lite、SafeTensors 等多种模型格式
- **交互式可视化**：以图形化方式展示神经网络的层结构、参数和连接关系
- **跨平台使用**：支持 Web 浏览器、桌面应用和命令行工具，方便不同环境使用
- **模型分析**：可查看模型各层的输入输出维度、权重数据和计算流程

## 3. 适用场景
- **模型调试**：快速检查模型架构是否正确，定位层结构问题
- **论文复现**：可视化对比不同框架实现的模型结构差异
- **教学演示**：直观展示神经网络工作原理，辅助深度学习教学
- **模型部署前检查**：验证模型转换后的结构完整性

## 4. 技术亮点
- **零依赖运行**：无需安装深度学习框架即可加载和查看模型
- **高星标社区认可**：33399 颗星证明其广泛使用和口碑
- **开源免费**：完全开源，支持本地和在线两种使用方式
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33399 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# ONNX 项目分析

## 1. 中文简介
ONNX（开放神经网络交换）是机器学习领域的开放标准，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同平台和框架之间无缝迁移和部署机器学习模型。

## 2. 核心功能
- **跨框架模型转换**：支持在 PyTorch、TensorFlow、Keras 等主流框架之间转换模型格式
- **统一模型表示**：提供标准化的中间表示格式，屏蔽各框架差异
- **部署优化**：支持模型推理加速和边缘设备部署
- **生态工具链**：提供 ONNX Runtime 运行时和模型检查工具

## 3. 适用场景
- 将训练好的模型从 PyTorch/TensorFlow 导出并部署到生产环境
- 在移动端或嵌入式设备上运行机器学习模型
- 不同框架之间的模型迁移和兼容性验证
- 需要跨平台部署的 AI 产品项目

## 4. 技术亮点
- 由微软、Facebook 等科技巨头联合推动，社区生态成熟
- 支持超过 100+ 种算子，覆盖主流深度学习操作
- 与 ONNX Runtime 深度集成，提供高性能推理能力
- 兼容硬件加速（GPU、NPU、CPU），适合边缘计算场景
- 链接: https://github.com/onnx/onnx
- ⭐ 21357 | 🍴 4010 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

---

### 1. 中文简介

"Machine Learning Engineering Open Book"是一本开源的机器学习工程实战指南，系统性地涵盖了从模型训练、调试到部署推理的全链路工程实践。该项目以PyTorch为核心，聚焦大规模语言模型（LLM）的训练与推理优化，是MLOps领域的实用参考手册。

---

### 2. 核心功能

- **训练优化**：提供大规模分布式训练的最佳实践与调优策略
- **GPU调试与性能分析**：涵盖GPU利用率诊断、内存优化等调试技巧
- **推理部署**：详解LLM推理加速、服务化部署及可扩展架构设计
- **基础设施管理**：介绍Slurm集群调度、网络配置与存储优化
- **可扩展性设计**：支撑千卡级大规模训练的系统架构方案

---

### 3. 适用场景

- **LLM训练工程**：面向大语言模型分布式训练的工程师，提供从数据并行到张量并行的完整实践
- **MLOps平台搭建**：适用于构建企业级机器学习训练与推理平台的团队
- **GPU资源优化**：帮助解决GPU利用率低、显存溢出等性能瓶颈问题
- **科研与生产落地**：适合需要将PyTorch实验模型高效部署到生产环境的算法工程师

---

### 4. 技术亮点

- 基于PyTorch生态，与Hugging Face Transformers深度整合
- 覆盖从单机调试到千卡集群的完整训练链路
- 聚焦LLM时代特有的工程挑战（如长上下文推理、显存优化）
- 开源免费，持续更新，社区活跃度高（18,705+星标）
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18705 | 🍴 1206 | 语言: Python
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
- ⭐ 13283 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11633 | 🍴 917 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10693 | 🍴 5696 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为学习者提供了丰富的实战案例和完整代码实现，是AI领域入门与进阶的优质学习资源库。

### 2. 核心功能
- 收录500个AI实战项目，覆盖主流AI技术方向
- 提供完整的代码实现，便于学习与实践
- 按领域分类整理（机器学习、深度学习、CV、NLP）
- 包含从入门到进阶的多样化项目难度

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习实践
- 开发者寻找项目灵感并完成代码参考
- 学生或研究人员快速了解AI各领域前沿方向
- 技术面试准备与项目经验积累

### 4. 技术亮点
该项目作为"Awesome List"类型的资源聚合库，具有极高的社区认可度（36535星标），涵盖了Python生态中主流的AI框架与实践项目，是AI领域最全面的开源学习资源之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36535 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持查看多种主流框架训练的模型文件，帮助用户直观理解模型架构与结构。

## 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、PyTorch、Keras、Core ML、TensorFlow Lite、SafeTensors 等多种模型格式
- **交互式可视化**：以图形化方式展示神经网络的层结构、参数和连接关系
- **跨平台使用**：支持 Web 浏览器、桌面应用和命令行工具，方便不同环境使用
- **模型分析**：可查看模型各层的输入输出维度、权重数据和计算流程

## 3. 适用场景
- **模型调试**：快速检查模型架构是否正确，定位层结构问题
- **论文复现**：可视化对比不同框架实现的模型结构差异
- **教学演示**：直观展示神经网络工作原理，辅助深度学习教学
- **模型部署前检查**：验证模型转换后的结构完整性

## 4. 技术亮点
- **零依赖运行**：无需安装深度学习框架即可加载和查看模型
- **高星标社区认可**：33399 颗星证明其广泛使用和口碑
- **开源免费**：完全开源，支持本地和在线两种使用方式
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33399 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介
这是一个面向深度学习与机器学习研究者的必备速查手册合集。项目汇总了人工智能、机器学习、深度学习等领域中常用的公式、语法和技巧，方便研究人员快速查阅和复习核心知识。

### 2. 核心功能
- 提供机器学习与深度学习核心概念的速查表
- 涵盖 NumPy、SciPy、Matplotlib 等常用库的使用技巧
- 包含 Keras 等深度学习框架的实用代码示例
- 以简洁的格式整理关键公式与语法，便于快速检索
- 覆盖从基础到进阶的研究者常用知识点

### 3. 适用场景
- 机器学习/深度学习研究者快速复习核心公式与概念
- 数据科学家在日常工作中查阅 NumPy、Matplotlib 等库的用法
- 备考或面试前快速梳理 AI 领域的关键知识点
- 教学场景中作为辅助参考资料使用

### 4. 技术亮点
- 项目星标数达 **15,427**，在社区中具有较高的认可度和影响力
- 内容覆盖全面，从底层数学工具（NumPy/SciPy）到高层框架（Keras）均有涉及
- 以速查表形式呈现，信息密度高，便于快速定位所需内容
- 附有 Medium 原文链接，便于进一步延伸阅读
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材。项目面向零基础学习者，覆盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域，助力学习者实现从入门到就业的完整进阶。

### 2. 核心功能
- 提供系统化的AI学习路径规划，涵盖从基础到进阶的完整知识体系
- 整理近200个实战项目与案例，供学习者动手实践
- 免费提供配套学习教材，降低学习门槛
- 覆盖Python、机器学习、深度学习、NLP、CV等多领域技术栈
- 以就业为导向，注重实战能力培养

### 3. 适用场景
- 零基础学员系统学习人工智能与机器学习技术
- 希望转行AI领域的开发人员补充知识体系
- 需要实战项目经验以提升求职竞争力的学习者
- 教师或培训机构用于AI课程教学参考

### 4. 技术亮点
- 学习路径设计完整，覆盖主流框架（TensorFlow、PyTorch、Keras等）
- 实战导向，提供大量可落地的项目案例
- 资源免费开源，社区活跃（星标数超1.3万）
- 技术栈全面，兼顾理论基础（数学）与工程实践（算法、数据分析）
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13283 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

---

### 1. 中文简介

Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它降低了深度学习模型的构建门槛，让开发者无需大量编码即可快速训练和部署 AI 模型。

---

### 2. 核心功能

- **低代码模型构建**：通过声明式配置即可定义和训练神经网络，无需编写大量代码。
- **支持多种 AI 模型**：涵盖大语言模型（LLM）、计算机视觉、自然语言处理等多种架构。
- **数据-centric 工作流**：专注于数据驱动模型训练，提供数据预处理、特征工程的一站式支持。
- **主流框架兼容**：基于 PyTorch 构建，与 Hugging Face Transformers 生态无缝集成。
- **微调与训练**：支持对 LLaMA、Mistral 等主流大模型进行微调和定制训练。

---

### 3. 适用场景

- **快速原型开发**：希望快速验证 AI 想法、无需深入代码细节的数据科学家。
- **大模型微调**：对 LLaMA、Mistral 等开源大模型进行领域适配和微调。
- **多模态模型构建**：同时处理文本、图像等多种数据类型的 AI 应用开发。
- **生产环境部署**：需要将训练好的模型快速部署到生产环境的团队。

---

### 4. 技术亮点

- **声明式 YAML 配置**：通过简单的配置文件定义模型结构，大幅降低开发复杂度。
- **Hugging Face 深度集成**：原生支持 Transformers 模型，可直接加载和微调海量预训练模型。
- **自动数据预处理**：内置丰富的数据类型处理管道，自动完成归一化、编码等操作。
- **可视化训练监控**：提供训练过程可视化，便于实时监控模型收敛情况。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9188 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8966 | 🍴 3108 | 语言: C++
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

## funNLP 项目分析

### 1. 中文简介

funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了从基础工具（敏感词检测、分词、命名实体识别）到高级应用（知识图谱、对话系统、语音识别）的完整生态。该项目整合了大量开源数据集、预训练模型、实用工具库以及竞赛方案，为中文NLP研究者和开发者提供了一站式资源平台。

### 2. 核心功能

- **基础NLP工具**：提供敏感词检测、语言检测、分词、词性标注、命名实体识别、情感分析等核心功能
- **预训练模型资源**：集成BERT、GPT-2、ALBERT、ELECTRA等主流中文预训练模型及训练代码
- **知识图谱构建**：包含实体抽取、关系抽取、知识图谱问答系统等完整知识图谱解决方案
- **语音与文本融合**：提供ASR语音识别、发音词典、语音情感分析等多模态NLP工具
- **数据增强与评测**：收录NLP数据增强工具、文本摘要、关键词抽取及各类评测基准

### 3. 适用场景

- **中文NLP研究与开发**：学术研究者或工程师快速查找数据集、模型和代码实现
- **企业级智能客服/对话系统**：利用开源对话系统框架和语料库搭建问答机器人
- **知识图谱应用开发**：基于抽取工具和预训练模型构建领域知识图谱
- **文本分析与内容审核**：使用敏感词库、情感分析和文本分类工具进行内容风控

### 4. 技术亮点

- 项目汇聚8.2万+星标，是中文NLP领域最全面的开源资源仓库之一，持续更新涵盖最新研究成果和工业实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82664 | 🍴 15275 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100+ 种模型的微调训练，相关研究发表于 ACL 2024 会议。

### 2. 核心功能
- 支持 100+ 主流大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、全参数微调等多种训练策略
- 支持指令微调（Instruction Tuning）和 RLHF 对齐训练
- 兼容 Transformers 和 PEFT 生态，集成量化技术
- 内置 Agent 功能，支持多模型协同推理

### 3. 适用场景
- 对 Llama、Qwen、DeepSeek、Gemma 等模型进行轻量化微调
- 资源受限环境下使用 QLoRA 进行低秩适配训练
- 需要多模型统一训练流程的科研与生产场景
- 构建定制化 AI Agent 并进行指令对齐优化

### 4. 技术亮点
- **统一框架**：一站式支持 100+ 模型，无需为不同模型编写独立训练脚本
- **高效微调**：内置 QLoRA 等低资源优化方案，大幅降低显存占用
- **前沿研究**：成果发表于 ACL 2024，具备学术认可度
- **生态友好**：深度集成 Hugging Face Transformers 和 PEFT，社区活跃度高
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74350 | 🍴 9095 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一个由微软推出的AI入门课程项目，为期12周、包含24节课程，旨在让所有人都能学习人工智能。项目采用Jupyter Notebook形式，内容涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。

## 2. 核心功能
- 提供系统化AI学习路径，从基础概念到高级应用循序渐进
- 涵盖机器学习、深度学习、CNN、RNN、GAN、NLP和计算机视觉等主题
- 基于Jupyter Notebook的交互式学习方式，便于实践操作
- 微软官方出品，课程结构清晰、难度适中，适合零基础学习者

## 3. 适用场景
- AI初学者系统学习人工智能基础知识
- 高校或培训机构作为AI课程的教学辅助材料
- 希望转行进入AI领域的开发者快速入门
- 对AI感兴趣的非技术背景人员了解基本概念

## 4. 技术亮点
- 微软官方背书，课程质量和权威性有保障
- 高星标数（66,937）证明项目受欢迎程度和社区认可度
- 标签覆盖AI核心领域，课程内容全面且紧跟技术趋势
- Jupyter Notebook形式便于动手实践，理论与实践相结合
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66937 | 🍴 12927 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## AI Engineering from Scratch 项目分析

### 1. 中文简介
从基础出发，深入学习AI工程，亲手构建系统，最终将其交付给他人使用。这是一门涵盖AI全栈开发的实战课程，帮助学习者掌握从理论到部署的完整技能链。

### 2. 核心功能
- 从零开始系统学习AI工程的核心概念与实现原理
- 涵盖LLM、生成式AI、计算机视觉、NLP等主流AI方向
- 提供AI Agent、MCP协议、强化学习等前沿技术的实战训练
- 支持Python、Rust、TypeScript多语言开发实践
- 结合Swarm Intelligence（群体智能）等进阶主题

### 3. 适用场景
- 希望系统掌握AI工程全栈技能的开发者
- 从事LLM应用开发、AI Agent构建的工程师
- 需要深入理解深度学习、Transformer架构的学习者
- 追求从零实现AI系统、而非仅调用API的实战派开发者

### 4. 技术亮点
- 强调"从 scratch"（从零实现），而非仅使用高级框架，深入理解底层原理
- 跨越多语言生态（Python/Rust/TypeScript），适合不同技术背景的开发者
- 覆盖从基础机器学习到前沿生成式AI的完整技术栈，内容全面
- 注重"Ship it for others"，强调工程化交付与产品化能力
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 48821 | 🍴 8553 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42483 | 🍴 11513 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36535 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33845 | 🍴 4717 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29214 | 🍴 3567 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21859 | 🍴 3369 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17385 | 🍴 2125 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为学习者提供了丰富的实战案例和完整代码实现，是AI领域入门与进阶的优质学习资源库。

### 2. 核心功能
- 收录500个AI实战项目，覆盖主流AI技术方向
- 提供完整的代码实现，便于学习与实践
- 按领域分类整理（机器学习、深度学习、CV、NLP）
- 包含从入门到进阶的多样化项目难度

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习实践
- 开发者寻找项目灵感并完成代码参考
- 学生或研究人员快速了解AI各领域前沿方向
- 技术面试准备与项目经验积累

### 4. 技术亮点
该项目作为"Awesome List"类型的资源聚合库，具有极高的社区认可度（36535星标），涵盖了Python生态中主流的AI框架与实践项目，是AI领域最全面的开源学习资源之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36535 | 🍴 7467 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一个利用 AI 技术自动化基于浏览器的工作流工具。它通过结合大语言模型（LLM）和计算机视觉能力，能够自主操作浏览器完成复杂的网页交互任务，无需编写繁琐的自动化脚本。

### 2. 核心功能
- **AI 驱动的浏览器自动化**：利用大语言模型理解页面内容并自主决策操作步骤
- **视觉感知能力**：通过计算机视觉识别网页元素，无需依赖固定的选择器
- **支持多种浏览器引擎**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **REST API 接口**：提供简洁的 API 供外部系统调用和集成
- **无需代码编写**：通过自然语言描述任务即可自动生成并执行自动化流程

### 3. 适用场景
- **RPA 替代方案**：替代传统 Power Automate 等工具，处理复杂的网页表单填写和数据录入
- **跨平台数据采集**：自动化抓取需要登录或复杂交互的网页数据
- **重复性网页操作**：自动化处理如订单提交、报告生成等重复性浏览器任务
- **企业工作流集成**：将网页操作嵌入现有业务流程，实现端到端自动化

### 4. 技术亮点
- 结合了 LLM 的理解能力和视觉模型的环境感知能力，突破了传统自动化对固定选择器的依赖
- 支持多浏览器引擎切换，灵活适配不同场景需求
- 高星标数（22,848）证明其在 AI 自动化领域的广泛认可度和社区活跃度
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22848 | 🍴 2146 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一款领先的视觉数据集构建平台，专为视觉AI开发而设计。它提供开源、云服务和企业级产品，支持图像、视频及3D数据的AI辅助标注、质量保障、团队协作和数据分析等功能。

### 2. 核心功能
- 支持图像、视频和3D数据的智能标注
- 提供AI辅助标注功能，提升标注效率
- 内置质量保障机制，确保数据集准确性
- 支持团队协作与开发者API集成
- 提供开源、云服务和企业版多种部署方案

### 3. 适用场景
- 深度学习项目的数据标注与数据集构建
- 目标检测和语义分割任务的标注工作
- 团队协同完成大规模视觉数据集制作
- 视频内容分析与帧级标注需求

### 4. 技术亮点
- 支持PyTorch和TensorFlow主流深度学习框架
- 涵盖边界框、图像分类、语义分割等多种标注类型
- 提供完整的标注工具链，从数据采集到质量管控一站式解决
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16594 | 🍴 3815 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# pytorch-grad-cam 项目分析

## 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN、Vision Transformer等多种模型架构，涵盖分类、目标检测、图像分割、图像相似度等多种任务类型。

## 2. 核心功能
- 提供Grad-CAM、Score-CAM等多种类激活图生成方法
- 支持CNN和Vision Transformer架构的可视化解释
- 兼容图像分类、目标检测、语义分割等多种任务
- 生成直观的热力图以展示模型关注区域
- 提供图像相似度分析的可视化能力

## 3. 适用场景
- 深度学习模型的可解释性研究与调试
- 计算机视觉模型的决策依据可视化分析
- 学术研究与论文中的结果展示
- 工业界模型部署前的可信度验证

## 4. 技术亮点
- 统一接口支持多种CAM变体算法
- 对Vision Transformer等新型架构有完善支持
- 在GitHub上获得近1.3万星标，社区认可度高
- 基于PyTorch框架，与主流深度学习生态无缝集成
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，专为 PyTorch 框架设计。它提供了一套可微分的图像处理与计算机视觉操作，能够直接在 GPU 上高效运行，并与深度学习流程无缝集成。

### 2. 核心功能
- **可微分图像处理**：提供数十种可微分的图像变换操作（如旋转、缩放、仿射变换等），支持端到端训练。
- **几何视觉算法**：包含相机标定、立体视觉、单目深度估计、位姿估计等传统几何视觉模块。
- **PyTorch 原生集成**：操作直接作用于 PyTorch 张量，无需额外转换，充分利用 GPU 加速。
- **空间 AI 工具集**：支持 3D 点云处理、多视角几何、机器人导航等空间感知任务。
- **自动化微分管线**：所有操作均支持反向传播，可直接嵌入神经网络进行联合优化。

### 3. 适用场景
- **机器人视觉导航**：用于机器人实时感知环境、计算位姿与路径规划。
- **自动驾驶感知系统**：处理多摄像头数据，进行立体匹配、深度估计和场景理解。
- **摄影测量与三维重建**：从多视角图像中恢复场景的 3D 结构。
- **深度学习研究**：作为可微分视觉模块嵌入神经网络，用于训练端到端的视觉模型。

### 4. 技术亮点
- **全可微设计**：所有几何操作均支持自动微分，实现传统 CV 与深度学习的深度融合。
- **高性能 GPU 加速**：基于 PyTorch 原生实现，无需 CPU-GPU 数据传输开销，处理速度远超传统 OpenCV 方案。
- **活跃的开源社区**：11,000+ 星标，参与 Hacktoberfest 等活动，持续迭代更新。
- **模块化架构**：功能按几何视觉、图像处理、深度学习等模块组织，便于按需集成。
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
- ⭐ 3428 | 🍴 421 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387587 | 🍴 81363 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub 项目分析：superpowers

---

### 1. 中文简介

这是一个基于智能体（Agent）的技能框架与软件开发方法论，旨在通过子代理驱动的方式提升开发效率。它提供了一套可落地的AI辅助开发流程，帮助开发者更高效地完成软件工程任务。

---

### 2. 核心功能

- **智能体技能框架**：提供结构化的AI技能模块，支持任务分解与自动化执行。
- **子代理驱动开发（Subagent-Driven Development）**：通过多个子代理协作完成复杂开发任务。
- **AI辅助头脑风暴与编码**：整合AI能力，支持创意发散和代码生成。
- **完整SDLC覆盖**：涵盖从需求分析到部署的软件开发生命周期管理。
- **模块化技能组合**：支持灵活组装不同技能，适配多样化的开发场景。

---

### 3. 适用场景

- 需要AI辅助完成大规模代码生成和重构的软件开发项目。
- 希望通过智能体协作提升团队协作效率的敏捷开发团队。
- 利用AI进行技术方案头脑风暴和架构设计的创新项目。
- 追求标准化、自动化软件开发流程的企业级工程团队。

---

### 4. 技术亮点

- 将"智能体驱动开发"理念落地为可操作的方法论与工具链。
- 以Shell脚本为核心实现，轻量且易于集成到现有CI/CD流程中。
- 社区热度极高（27万+星标），说明其理念和实用性获得广泛认可。
- 链接: https://github.com/obra/superpowers
- ⭐ 277473 | 🍴 24821 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## Hermes-Agent 项目分析

### 1. 中文简介
Hermes-Agent 是一款能够随用户共同成长的人工智能代理工具，支持多种主流大语言模型（包括 Claude、ChatGPT 等），具备灵活的交互能力和持续进化的特性。

### 2. 核心功能
- **多模型支持**：兼容 Claude、ChatGPT、Codex 等主流 AI 模型，用户可自由选择
- **智能代理能力**：具备自主决策和任务执行能力，可作为个人 AI 助手
- **持续成长机制**：系统能够根据用户交互不断优化和适应
- **Python 原生开发**：基于 Python 构建，易于集成和二次开发

### 3. 适用场景
- **开发者辅助**：代码编写、调试和技术问题解答
- **日常智能助手**：信息查询、任务管理和自动化操作
- **AI 研究实验**：多模型对比测试和 AI 代理行为研究
- **企业级应用**：定制化 AI 工作流和智能客服系统

### 4. 技术亮点
- **跨平台兼容**：支持多种 LLM 后端，灵活切换模型
- **开源活跃**：23万+ 星标，社区贡献活跃，持续迭代更新
- **Nous Research 出品**：由知名 AI 研究团队 Nous Research 开发维护，技术实力有保障
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 236332 | 🍴 47708 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款开源公平代码的工作流自动化平台，内置原生AI能力。它支持可视化构建与自定义代码相结合，可自托管或云端部署，提供400多种集成连接。

### 2. 核心功能
- **可视化工作流构建**：拖拽式界面设计自动化流程，无需编码即可快速搭建
- **原生AI集成**：内置AI节点，支持大语言模型调用与AI工作流编排
- **400+ 集成生态**：覆盖主流SaaS工具、API服务和数据库连接
- **混合部署模式**：支持自托管私有化部署或云端SaaS服务
- **代码自定义扩展**：允许嵌入JavaScript/Python代码实现复杂逻辑

### 3. 适用场景
- **企业自动化**：跨系统数据同步、定时任务调度、消息通知推送
- **AI应用开发**：构建RAG知识库、AI代理工作流、智能客服系统
- **低代码平台**：业务人员快速搭建业务流程，减少开发成本
- **MCP协议支持**：集成Model Context Protocol，扩展AI工具调用能力

### 4. 技术亮点
- 基于TypeScript开发，类型安全且易于二次开发
- 采用fair-code许可证，核心功能免费，商业功能可定制
- 支持MCP客户端/服务端，紧跟AI工具链发展趋势
- 节点化架构设计，每个工作流步骤可独立调试和复用
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202392 | 🍴 60379 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建AI工具，实现AI的普惠愿景。我们的使命是提供完善的工具链，让用户能够专注于真正重要的事务。

### 2. 核心功能
- **自主任务规划**：AI可自动拆解复杂任务并制定执行步骤
- **多模型支持**：兼容OpenAI GPT、Claude、LLaMA等多种大语言模型
- **自我反思机制**：执行过程中自动评估结果并调整策略
- **工具链扩展**：支持浏览器操作、文件读写、API调用等外部工具集成
- **长期记忆管理**：通过向量数据库实现跨会话的上下文持久化

### 3. 适用场景
- 自动化重复性工作流（如数据收集、报告生成）
- 研究助手（自动搜索、整理和分析信息）
- 代码开发与调试辅助
- 内容创作与社交媒体管理

### 4. 技术亮点
- 采用多代理协作架构，支持任务并行与分工
- 内置代码解释器，可执行Python脚本验证逻辑
- 支持自定义代理配置与权限控制
- 开源社区活跃，持续迭代更新
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186856 | 🍴 46049 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 172250 | 🍴 9518 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167890 | 🍴 21667 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164655 | 🍴 30557 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 158027 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153670 | 🍴 9932 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

