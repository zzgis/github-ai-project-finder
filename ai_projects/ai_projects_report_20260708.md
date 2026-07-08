# GitHub AI项目每日发现报告
日期: 2026-07-08

## 新发布的AI项目

### Homekit
- ### 1. **中文简介**
Homekit 通过单一开放接口，赋予任何 AI 代理对 Apple Home 生态系统的直接物理控制权，实现开灯、锁门及读取传感器数据等功能。该项目基于 TypeScript 构建，旨在简化智能家庭自动化与 AI 模型的交互流程。它让开发者能够轻松集成 Claude、Cursor 等主流 AI 工具到 macOS 智能家居环境中。

### 2. **核心功能**
- **直接物理控制**：允许 AI 代理直接操作 Apple HomeKit 设备，如开关灯光和门锁。
- **传感器数据读取**：支持实时获取智能家居环境中的传感器状态和数据。
- **MCP 协议支持**：基于模型上下文协议（Model Context Protocol），提供标准化的 AI 集成接口。
- **多平台 AI 兼容**：无缝对接 Claude、Cursor、OpenClaw 等多种 AI 代理工具。
- **TypeScript 原生开发**：使用 Node.js 和 TypeScript 构建，确保代码的高效性与类型安全。

### 3. **适用场景**
- **AI 驱动的智能家居自动化**：利用 AI 代理根据用户习惯或传感器数据自动执行家居控制任务。
- **开发者集成测试**：为希望在 macOS 上测试 AI 代理与硬件交互能力的开发者提供现成的接口方案。
- **高级语音助手扩展**：增强现有语音助手能力，使其能更精准地控制 Apple Home 生态系统。
- **自定义智能场景构建**：结合 MCP 协议，快速搭建个性化的家庭自动化工作流。

### 4. **技术亮点**
- **标准化接口**：采用 Model Context Protocol (MCP) 作为统一通信标准，降低集成复杂度。
- **轻量级架构**：基于 Node.js 和 TypeScript，易于部署和维护，适合快速原型开发。
- **跨工具兼容性**：不仅限于特定 AI 提供商，而是通过开放接口支持广泛的 AI 代理生态。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### fox-ai-roundtable
- ### 1. 中文简介
Fox-AI-Roundtable 是一个允许用户通过本地命令行接口（CLI），将同一提示词同时发送给 Claude、Codex (GPT) 和 Antigravity (Gemini) 三个模型的工具。其核心理念是“一次提问，获取三种回答”，帮助用户快速对比不同大语言模型的输出结果。该项目基于 HTML 构建，旨在提供一个轻量级的多模型并行交互方案。

### 2. 核心功能
*   **多模型并行调用**：支持同时向 Claude、OpenAI Codex 和 Google Gemini 发送请求。
*   **统一提示输入**：用户只需输入一次 Prompt，即可触发多个后端服务的响应。
*   **本地 CLI 集成**：通过本地命令行接口连接各 AI 服务商，无需配置复杂的 Web 前端界面。
*   **结果即时对比**：在终端中直接展示三个模型对同一问题的不同回答，便于直观比较。

### 3. 适用场景
*   **模型性能基准测试**：开发者需要快速评估不同 LLM 在同一任务下的表现差异。
*   **创意写作辅助**：作家或内容创作者希望从不同角度获取灵感，对比多个模型的生成风格。
*   **代码生成优化**：程序员利用多个 AI 模型生成代码片段，以寻找更优或更安全的解决方案。
*   **多源信息验证**：研究人员通过对比不同模型的推理逻辑，交叉验证信息的准确性。

### 4. 技术亮点
*   **极简架构**：仅使用 HTML 作为主要技术栈，体现了极高的轻量化设计思路。
*   **跨平台兼容性**：依托于各厂商提供的本地 CLI 工具，兼容性强，易于部署。
*   **零延迟对比体验**：避免了切换不同 Chat 界面的操作成本，直接在终端流式输出结果。
- 链接: https://github.com/PeterPanSwift/fox-ai-roundtable
- ⭐ 47 | 🍴 9 | 语言: HTML

### blockout
- 1. **中文简介**
Blockout 是一款面向 AI 原生电影制作的预可视化（Previs）工具，允许用户在灰色盒场景中搭建舞台、编排摄像机运动及角色走位。它能够将上述编排导出为运动参考包，以便与 Seedance、Veo、Kling、LTX 或 Wan 等主流 AI 视频生成模型无缝对接。该项目采用 Apache-2.0 开源协议，基于 TypeScript 开发。

2. **核心功能**
*   支持在三维空间中快速搭建灰色盒场景，用于初步视觉构思。
*   提供摄像机路径规划与角色走位标记（Marks）的编排能力。
*   可生成标准化的运动参考数据包，兼容多种 AI 视频生成接口。
*   专为 AI 视频工作流优化，实现从传统预可视化到 AI 生成的平滑过渡。

3. **适用场景**
*   AI 电影制片前期筹备，用于在投入大量计算资源前确定镜头语言。
*   导演与分镜师协作，通过精确的摄像机和演员标记来细化创意意图。
*   使用 Seedance、Kling 等模型生成视频时，需要高精度运动参考数据的场景。
*   探索传统影视制作流程与生成式 AI 技术结合的工作流优化。

4. **技术亮点**
*   填补了传统预可视化工具与现代 AI 视频生成模型之间的数据格式鸿沟。
*   轻量级 TypeScript 架构，便于集成到现有的数字内容创作管线中。
- 链接: https://github.com/wassermanproductions/blockout
- ⭐ 44 | 🍴 6 | 语言: TypeScript

### trend-viewer
- 1. **中文简介**
这是一个仅依赖Python标准库的本地趋势监控面板，支持在单一界面中同步查看YouTube、Reels、X（原Twitter）、Threads、TikTok及AI新闻等多平台内容。该项目旨在为用户提供一种轻量级、无外部依赖的多源信息聚合解决方案。

2. **核心功能**
- 集中展示：在一个本地界面上同时监控来自YouTube、TikTok、X等多个社交平台的实时动态。
- 纯标准库实现：完全基于Python标准库开发，无需安装任何第三方依赖包即可运行。
- 本地服务器部署：作为本地Web服务器运行，确保数据隐私且无需连接远程云服务。
- AI新闻集成：除了社交媒体内容外，还整合了AI相关的新闻资讯流。
- 跨平台覆盖：兼容主流视频平台（YouTube, TikTok）及微博客/短文本平台（X, Threads）。

3. **适用场景**
- 个人用户希望在一个简洁的本地页面中快速浏览多个社交平台的热门话题，避免切换不同App。
- 对数据隐私敏感的用户，倾向于在本地运行服务以监控网络趋势，而不想将数据上传至第三方云服务平台。
- Python开发者或极简主义者，寻找一个零依赖、轻量级且易于部署的信息聚合原型或工具。
- 需要同时关注社交媒体舆情与AI领域最新动态的市场分析师或研究人员。

4. **技术亮点**
- **零依赖部署**：仅使用Python标准库（stdlib），极大简化了环境配置和依赖管理过程。
- **轻量级架构**：作为本地服务器运行，资源占用低，适合在配置较低的机器上长期稳定运行。
- 链接: https://github.com/xazingatrend/trend-viewer
- ⭐ 27 | 🍴 14 | 语言: Python
- 标签: instagram, local-server, python, stdlib, tiktok

### kakunin-sdk-typescript
- ### 1. 中文简介
该项目是 Kakunin AI 代理合规 API 的官方 TypeScript SDK，旨在为人工智能代理提供标准化的身份验证与安全合规支持。它集成了 API 客户端以及用于强制实施数字证书中间件的功能，确保非人类实体在交互过程中的可信度。

### 2. 核心功能
*   **官方 TypeScript SDK**：提供类型安全的代码库，便于开发者集成到基于 TypeScript 的后端或前端服务中。
*   **API 客户端集成**：封装了与 Kakunin 合规 API 通信的逻辑，简化了身份验证和数据查询流程。
*   **证书执行中间件**：内置中间件组件，用于强制验证 X.509 证书，确保通信双方具备合法的数字身份。
*   **AI 代理合规支持**：专门针对 AI Agent 设计，支持 KYC（了解你的客户）及满足欧盟《人工智能法案》（EU AI Act）等监管要求。

### 3. 适用场景
*   **受监管行业的 AI 集成**：在金融、医疗等需要严格身份验证和合规审计的领域部署 AI 代理时使用。
*   **构建可信 AI 生态系统**：开发平台时，利用该 SDK 验证接入的 AI 代理身份，防止未授权或非合规实体访问资源。
*   **应对新兴 AI 法规**：帮助企业在欧盟等地区落地时，快速实现符合 EU AI Act 或 MiCA 法规的技术合规性。

### 4. 技术亮点
*   **原生 TypeScript 支持**：作为原生 TS 库，提供了良好的 IDE 支持和类型推断，提升了开发体验。
*   **Webhook 支持**：集成 Webhook 功能，允许实时接收代理状态变更或合规事件的通知。
*   **聚焦非人类身份（Non-Human Identity）**：专门解决 AI 代理作为“非人类实体”的身份锚定问题，填补了传统身份认证在 AI 领域的空白。
- 链接: https://github.com/nqzai/kakunin-sdk-typescript
- ⭐ 26 | 🍴 10 | 语言: TypeScript
- 标签: agent-security, ai-agent-identity, ai-agents, certificate-authority, compliance

### seedance-prompt
- 描述: Hermes skill for realistic AI video prompts for Seedance and text-to-video models.
- 链接: https://github.com/zhouwei713/seedance-prompt
- ⭐ 25 | 🍴 6 | 语言: 未知

### kakunin-core
- 描述: AI agent compliance platform — X.509 identity via AWS KMS, real-time behavioral risk scoring, auto-revocation, and MiCA / EU AI Act compliance reporting. AGPL-3.0.
- 链接: https://github.com/nqzai/kakunin-core
- ⭐ 25 | 🍴 1 | 语言: TypeScript
- 标签: agent-security-tools, ai-agent-identity, ai-agents-security, ai-governance-tools, audit-log-tools

### InkDiary
- 描述: Handwritten AI diary for iPad — Tom Riddle-style magic journal with sketch generation
- 链接: https://github.com/andyhuo520/InkDiary
- ⭐ 18 | 🍴 3 | 语言: Swift

### openclaw-voice-call-realtime
- 描述: Give your AI assistant a phone — OpenClaw plugin for real phone calls via Twilio + OpenAI Realtime, with in-call tools, transcripts, and call screening
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 15 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### gogh
- 描述: Gogh is a source-cited Obsidian operating brain that turns six frontend design skills into one advisable stack for AI coding agents.
- 链接: https://github.com/AgriciDaniel/gogh
- ⭐ 14 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能极其丰富的中文自然语言处理资源合集，涵盖了从基础工具（如敏感词检测、分词、OCR）到高级应用（如知识图谱构建、情感分析、对话系统）的广泛内容。该项目整合了大量公开的数据集、预训练模型、词库及行业报告，旨在为开发者提供一站式的 NLP 开发支持与参考。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简转换、分词、词性标注、命名实体识别（NER）及文本纠错等核心工具。
*   **丰富词库与数据资源**：集成中日文人名库、停词表、情感词典、专业领域词库（医疗、法律、汽车等）及大量竞赛级数据集。
*   **预训练模型与算法**：收录 BERT、ALBERT、RoBERTa 等主流模型的中文变体，以及关键词抽取、文本摘要、相似度匹配等算法实现。
*   **垂直领域应用**：涵盖医疗、金融、法律等领域的知识图谱问答系统、语音识别（ASR）及对话机器人技术方案。
*   **辅助开发与标注**：提供文本可视化工具、协同标注平台（Doccano）、OCR 识别库及各类 NLP 教程与代码示例。

3. **适用场景**
*   **NLP 初学者入门**：适合希望快速了解中文 NLP 生态、获取常用词库和基础代码示例的学习者。
*   **企业级文本审核与风控**：适用于需要实现敏感词过滤、舆情监控、谣言检测或内容合规性检查的业务系统。
*   **垂直行业智能客服研发**：为医疗、金融、法律等专业领域的知识图谱构建和智能问答系统提供数据模型参考。
*   **学术研究与技术调研**：作为研究人员追踪 NLP 前沿进展（如最新预训练模型、数据集榜单）的资源库。

4. **技术亮点**
*   **资源聚合度高**：并非单一算法库，而是汇集了数百个优质子项目、数据集和工具，极大降低了信息检索成本。
*   **覆盖全链路**：从数据预处理、模型训练到应用部署（如 OCR、ASR、Chatbot），提供了完整的中文 NLP 技术栈参考。
*   **紧跟前沿动态**：持续更新包括 Transformer 系列、知识图谱及最新开源模型在内的前沿技术成果。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81680 | 🍴 15254 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35259 | 🍴 7337 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33197 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是机器学习的开放标准，旨在促进不同框架间的互操作性。它允许开发者在不同的深度学习平台和硬件加速器之间无缝迁移模型，打破框架壁垒。

2. **核心功能**
*   提供统一的模型表示格式，支持跨框架（如PyTorch、TensorFlow、Keras等）的模型转换与交互。
*   包含丰富的算子库，覆盖从底层线性代数运算到高层神经网络层级的常见操作。
*   支持模型推理优化，通过ONNX Runtime在多种后端（CPU、GPU、NPU等）上实现高效执行。
*   提供工具链支持，用于模型的转换、验证、可视化及性能分析。

3. **适用场景**
*   **跨平台部署**：将训练好的模型从开发框架（如PyTorch）转换为标准格式，以便在移动设备或嵌入式系统上运行。
*   **硬件加速**：利用特定硬件（如Intel OpenVINO、NVIDIA TensorRT）对ONNX模型进行优化，提升推理速度。
*   **模型协作与共享**：在团队中使用不同深度学习框架时，通过ONNX作为中间格式交换模型，减少集成成本。

4. **技术亮点**
*   **生态兼容性极强**：作为行业事实标准，被主流AI框架（PyTorch, TensorFlow, Scikit-learn等）广泛原生支持。
*   **高性能推理引擎**：配套的ONNX Runtime提供了高度优化的执行引擎，支持图级别优化和并行计算。
- 链接: https://github.com/onnx/onnx
- ⭐ 21114 | 🍴 3961 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
   《ML Engineering Open Book》是一本专注于机器学习工程实践的开源指南。它系统性地涵盖了从底层基础设施到模型部署的全链路工程技术细节。该项目旨在帮助工程师构建高效、可扩展且稳定的机器学习生产环境。

2. **核心功能**
   *   提供大规模分布式训练的最佳实践与调试技巧。
   *   深入解析大语言模型（LLM）的推理优化与部署策略。
   *   详细介绍GPU集群管理、网络通信及存储系统配置。
   *   涵盖MLOps流水线设计、监控及可扩展性架构设计。

3. **适用场景**
   *   需要搭建或优化大型深度学习训练集群的基础设施团队。
   *   致力于降低大语言模型推理成本并提升服务吞吐量的算法工程师。
   *   希望建立标准化、高可用性机器学习生产平台的MLOps从业者。

4. **技术亮点**
   *   内容紧贴前沿，特别针对Transformer架构和LLM工程化痛点进行了深度剖析。
   *   结合Slurm、PyTorch等主流工具链，提供了极具操作性的实战指南而非纯理论。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18263 | 🍴 1159 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13113 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11562 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10662 | 🍴 5706 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI相关代码项目的精选集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它作为一份“Awesome”列表，为开发者提供了丰富的实战案例和源代码参考。

2. **核心功能**
*   汇集500多个高质量的AI实战项目代码库。
*   全面覆盖机器学习、深度学习、CV和NLP四大核心技术栈。
*   提供可直接运行的Python代码示例，便于快速上手和学习。
*   经过精心筛选和分类，帮助用户高效定位所需的技术方向。

3. **适用场景**
*   AI初学者希望寻找入门级实战项目以巩固理论基础。
*   数据科学家需要参考现成的代码模板来解决特定业务问题。
*   研究人员或学生希望快速复现经典算法效果以进行实验对比。
*   开发者在遇到技术瓶颈时，通过查阅类似项目寻找解决方案灵感。

4. **技术亮点**
*   高人气与高可信度：拥有超过35,000个星标，是GitHub上最受欢迎的AI资源库之一。
*   分类清晰：通过标签体系（如computer-vision, nlp）实现了精细化的内容组织。
*   全栈覆盖：从传统机器学习到前沿深度学习技术均有涉及，满足不同阶段需求。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35259 | 🍴 7337 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持查看多种主流框架生成的模型文件，帮助用户直观理解模型结构。该工具界面简洁，能够清晰展示层与张量的详细信息。

2. **核心功能**
*   支持广泛的模型格式，包括 ONNX、PyTorch、TensorFlow、Keras、CoreML 和 SafeTensors 等。
*   提供交互式图形界面，以拓扑图形式直观展示神经网络的层级结构和数据流向。
*   允许用户深入查看每个节点的详细属性、权重参数及张量形状信息。
*   兼容本地文件加载与在线预览，无需安装复杂的依赖环境即可快速使用。

3. **适用场景**
*   **模型调试**：开发者在构建或修改神经网络时，通过可视化检查结构是否符合预期。
*   **格式转换验证**：在将模型从一种框架（如 PyTorch）转换为另一种（如 ONNX）后，确认转换前后结构的一致性。
*   **论文与报告展示**：研究人员或工程师在撰写技术文档或演示文稿时，生成清晰的模型架构图。

4. **技术亮点**
*   极高的兼容性，几乎覆盖当前所有主流的深度学习框架及部署格式。
*   基于 Electron 开发，实现了跨平台运行（Windows、macOS、Linux），且支持作为独立桌面应用或浏览器扩展使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33197 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究者提供了 essential 的速查手册（Cheat Sheets）。它涵盖了从数据科学基础工具到主流框架及可视化库的关键语法与概念，旨在帮助研究人员快速回顾和查阅常用技术细节。

### 2. 核心功能
*   **基础工具速查**：提供 NumPy、SciPy 等数值计算库的核心函数与操作指南。
*   **深度学习框架参考**：包含 Keras 等流行深度学习框架的代码示例与 API 用法。
*   **数据可视化指南**：整理 Matplotlib 绘图库的常用图表类型与配置方法。
*   **AI 领域知识汇总**：浓缩机器学习与人工智能领域的关键概念与最佳实践。
*   **结构化学习笔记**：以紧凑的格式呈现信息，便于打印或离线快速检索。

### 3. 适用场景
*   **面试复习**：求职者用于快速回顾机器学习算法与工具库的知识点。
*   **开发调试**：工程师在编码过程中查找特定库（如 NumPy 或 Keras）的函数用法。
*   **学术写作辅助**：研究人员在撰写论文时参考标准的数据处理与可视化代码模板。
*   **入门学习对照**：初学者作为系统性学习后的知识梳理与查漏补缺工具。

### 4. 技术亮点
*   **高人气社区资源**：拥有超过 1.5 万星标，证明其内容受到广泛认可且实用性强。
*   **跨技术栈整合**：将数据处理、模型构建与可视化流程整合在同一资源集中，提升学习连贯性。
*   **极简主义设计**：采用“速查表”形式，去除了冗余解释，直击核心语法与逻辑。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，适合零基础用户入门及就业实战。内容涵盖Python、机器学习、深度学习、自然语言处理及计算机视觉等热门领域，集成了TensorFlow、PyTorch等主流框架的技术资源。

2. **核心功能**
*   提供系统化的AI学习路径，从数学基础到高级算法逐步深入。
*   收录近200个实战案例与完整项目代码，强化动手能力。
*   整合主流深度学习框架（如PyTorch、TensorFlow、Keras等）的学习资源。
*   覆盖数据挖掘、数据分析及可视化（Pandas、Matplotlib等）等多维技能树。

3. **适用场景**
*   计算机相关专业的学生或转行者构建系统化的AI知识体系。
*   希望从零基础入门，通过大量实战项目快速掌握机器学习技能的初学者。
*   需要查找特定领域（如NLP、CV）开源案例和参考代码进行二次开发的研究人员。

4. **技术亮点**
*   资源高度集成，将分散的热门技术领域（算法、框架、工具库）统一归纳为结构化的学习路线。
*   强调“就业实战”，通过丰富的开源项目直接对接工业界需求，提升求职竞争力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13113 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 项目分析：Ludwig

1. **中文简介**
   Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化的机器学习管道，让开发者无需编写大量底层代码即可快速训练和部署模型。该项目支持多种数据模态，并深度集成了 PyTorch 等主流深度学习后端。

2. **核心功能**
   - 支持低代码方式快速构建和训练各类 AI 模型，显著降低开发门槛。
   - 兼容多种数据模态（如文本、图像、表格等），实现统一的多模态处理能力。
   - 内置自动化机器学习（AutoML）功能，优化超参数调整与模型评估流程。
   - 提供对主流深度学习框架（如 PyTorch）及大语言模型（如 Llama、Mistral）的微调支持。

3. **适用场景**
   - 需要快速原型化开发 AI 应用，且希望减少底层工程代码编写的团队。
   - 进行多模态数据（如 NLP 结合计算机视觉）的实验性研究与模型训练。
   - 对现有预训练大模型（LLM）进行领域特定数据的微调与部署。
   - 数据科学家希望专注于数据科学与模型逻辑，而非复杂的机器学习基础设施搭建。

4. **技术亮点**
   - 采用声明式 YAML/JSON 配置驱动模型架构，实现高度可复用与版本控制。
   - 原生支持“以数据为中心”的 AI 工作流，简化数据预处理与特征工程环节。
   - 无缝集成 Hugging Face Transformers，便于直接调用和微调最新的大语言模型。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8919 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6986 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6234 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81680 | 🍴 15254 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，其研究成果已被 ACL 2024 收录。该项目支持超过 100 种主流模型，旨在简化指令微调和强化学习对齐的过程。它通过整合多种前沿技术，为用户提供了低门槛、高性能的模型优化体验。

2. **核心功能**
*   支持 100 多种 LLM 和 VLM 的统一高效微调，涵盖 LoRA、QLoRA 及全参数微调等模式。
*   集成 RLHF（基于人类反馈的强化学习）、DPO 及 ORPO 等先进对齐算法。
*   提供量化训练支持，显著降低显存占用并提升推理效率。
*   内置丰富的数据集格式转换工具，兼容 Alpaca、ShareGPT 等多种指令数据格式。
*   拥有模块化设计，便于用户快速部署实验并可视化训练过程。

3. **适用场景**
*   研究人员希望快速验证不同基座模型在特定任务上的微调效果。
*   开发者需要以较低硬件成本对大型模型进行领域知识注入或指令跟随能力增强。
*   企业团队致力于实施 RLHF 或 DPO 流程，以提升模型的安全性和有用性。
*   初学者希望使用开箱即用的工具链，避免从零搭建复杂的微调环境。

4. **技术亮点**
*   **极致性能优化**：通过 FlashAttention、PagedOptimizer 等技术大幅加速训练并节省显存。
*   **多模态支持**：不仅限于文本，还扩展至视觉语言模型（VLM）的微调与评估。
*   **标准化接口**：统一了不同模型架构的训练接口，屏蔽底层 Transformers 库的差异复杂性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73074 | 🍴 8931 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目汇总并提取了Anthropic、OpenAI、Google及xAI等主流厂商旗下多款前沿大模型（如Claude、GPT、Gemini系列）的系统提示词（System Prompts）。内容涵盖从基础聊天机器人到代码助手等多个版本，并保持定期更新以反映最新的技术变化。

2. **核心功能**
- 收集并公开多个知名AI模型和工具的内部系统指令结构。
- 整合来自Anthropic、OpenAI、Google和xAI等不同科技巨头的提示词数据。
- 提供对ChatGPT、Claude Code、VS Code Copilot等具体应用场景下系统提示词的详细解析。
- 保持数据的时效性，定期更新以纳入新发布的模型版本或功能变更。

3. **适用场景**
- **提示词工程研究**：帮助开发者逆向学习顶尖模型的指令遵循逻辑，优化自身Prompt设计。
- **AI安全与透明性评估**：用于分析大模型在底层指令层面的行为约束和安全对齐机制。
- **教育与学术参考**：作为生成式AI领域教学案例，展示不同厂商模型的系统架构差异。
- **竞品技术分析**：供从业者对比不同生态（如OpenAI vs Anthropic）在系统指令上的策略异同。

4. **技术亮点**
- 数据来源广泛，覆盖了当前市场上最具影响力的几类大语言模型及其专用变体。
- 具有较高的社区关注度（5万+星标），证明了其在提示词工程领域的实用价值和影响力。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 53607 | 🍴 8734 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目通过结构化的学习路径，帮助用户从零开始系统性地了解人工智能的核心概念与技术。

2. **核心功能**
*   提供结构化的12周学习计划，涵盖从基础到进阶的24个独立课时。
*   基于Jupyter Notebook编写，支持交互式代码执行与实时结果展示。
*   内容广泛覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
*   由微软发起并维护，确保教学内容的专业性与权威性。

3. **适用场景**
*   初学者希望通过系统化课程快速建立人工智能知识体系。
*   教育机构或企业用于开展AI基础培训与技能提升工作坊。
*   自学者利用交互式笔记本进行动手实践与代码演练。

4. **技术亮点**
*   采用Jupyter Notebook作为主要载体，实现“边学边练”的沉浸式学习体验。
*   标签涵盖CNN、RNN、GAN等前沿AI技术，体现课程内容的广度与深度。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51884 | 🍴 10481 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖数据分析、机器学习实战、线性代数基础以及PyTorch和TensorFlow 2等深度学习框架的应用。它整合了NLTK自然语言处理库及scikit-learn等工具，旨在提供从理论到实践的系统性指导。

2. **核心功能**
- 提供涵盖Adaboost、K-Means、SVM、朴素贝叶斯等经典算法的代码实现与解析。
- 集成深度学习内容，包括DNN、RNN、LSTM及基于PyTorch和TF2的实战案例。
- 包含推荐系统、回归分析、PCA降维及SVD分解等数据科学关键技术模块。
- 结合NLTK库进行自然语言处理（NLP）的基础教学与实例演示。
- 配套线性代数等数学基础内容，为机器学习和深度学习提供必要的理论支撑。

3. **适用场景**
- 初学者系统学习机器学习和深度学习理论与实践。
- 数据科学家或工程师快速查阅常用算法（如聚类、分类、降维）的代码示例。
- 需要构建推荐系统或进行NLP任务开发的开发者参考基础架构。
- 学生或研究人员辅助理解机器学习背后的数学原理（如线性代数在模型中的应用）。

4. **技术亮点**
- 技术栈广泛且主流，同时覆盖传统机器学习（scikit-learn）与现代深度学习（PyTorch/TF2）。
- 注重理论与实践结合，不仅提供算法代码，还融入数学基础（线性代数）讲解。
- 社区认可度高（4万+星标），内容经过大量用户验证，具有较高的参考价值。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37624 | 🍴 6268 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35259 | 🍴 7337 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33722 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28410 | 🍴 3453 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25850 | 🍴 2900 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目代码的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和代码参考。

2. **核心功能**
- 汇集大量人工智能相关的项目代码示例。
- 覆盖机器学习、深度学习及NLP等多个子领域。
- 提供计算机视觉相关的实战项目源码。
- 作为数据科学和AI学习的实用参考资料库。

3. **适用场景**
- AI初学者通过阅读代码快速上手各类算法实现。
- 研究人员寻找特定领域（如CV或NLP）的基线代码。
- 开发者需要参考现有项目结构以加速自身开发流程。
- 教育者用于构建机器学习课程的教学案例库。

4. **技术亮点**
- 资源规模庞大，收录高达500个独立项目。
- 分类清晰，标签涵盖从基础ML到前沿DL的全栈需求。
- 强调“With Code”，提供可直接运行的代码而非仅理论。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35259 | 🍴 7337 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的业务流程。它利用先进的计算机视觉和大语言模型技术，模拟人类操作浏览器，从而高效处理各种复杂的网页交互任务。

2. **核心功能**
*   **AI驱动的操作录制与回放**：通过视觉识别理解页面元素，无需依赖稳定的CSS选择器即可自动化点击、输入等动作。
*   **跨平台浏览器兼容**：支持多种主流浏览器引擎（如Playwright、Puppeteer），提供灵活的底层技术选型。
*   **智能工作流编排**：具备处理复杂逻辑判断和异常恢复的能力，能够构建端到端的自动化工作流。
*   **非结构化数据提取**：能够准确从动态变化的网页界面中提取关键信息，适应不同网站的结构变化。

3. **适用场景**
*   **RPA替代方案**：用于自动化那些传统脚本容易因页面改版而失效的网页后台管理或数据录入工作。
*   **竞品监控与数据采集**：定期访问电商或新闻网站，自动抓取价格变动、库存状态或文章更新等非结构化数据。
*   **企业内部流程自动化**：自动化处理需要登录多个不同Web系统并填写表单的内部行政或财务审批流程。

4. **技术亮点**
*   **视觉优先（Vision-First）架构**：结合大语言模型（LLM）与计算机视觉技术，使机器人能像人一样“看懂”网页布局而非仅解析代码。
*   **高鲁棒性**：相比传统的Selenium或Puppeteer脚本，Skyvern对前端UI变更具有更强的适应能力，减少了维护成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22154 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集以服务于视觉AI的主流平台。它提供开源、云及企业级产品以及标注服务，支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API等功能。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注能力。
*   集成AI辅助标注功能以提升数据处理效率与准确性。
*   提供团队协作、质量保证分析及完整的开发者API接口。

3. **适用场景**
*   构建用于目标检测或语义分割的高质量训练数据集。
*   团队协同进行大规模视频或图像数据的标注工作。
*   需要集成自定义算法或自动化流程的深度学习项目前期准备。

4. **技术亮点**
*   具备云原生架构，支持开源部署与企业级私有化部署。
*   兼容主流深度学习框架（如PyTorch、TensorFlow）及常见标注格式。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16245 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 以下是针对 GitHub 项目 `pytorch-grad-cam` 的技术分析报告：

1. **中文简介**
该项目是一个用于计算机视觉的高级 AI 可解释性工具库，支持 CNN 和 Vision Transformers 等多种模型架构。它能够实现分类、目标检测、语义分割及图像相似度分析等多种任务的可视化解释。通过生成类激活图（CAM）等技术，帮助用户直观理解模型的决策依据。

2. **核心功能**
*   支持多种主流深度学习模型，包括传统 CNN 和最新的 Vision Transformers。
*   提供广泛的视觉任务支持，涵盖图像分类、目标检测、语义分割及图像检索。
*   集成多种可解释性算法，如 Grad-CAM、Score-CAM 以及类激活映射技术。
*   具备强大的可视化能力，能够生成清晰的注意力热力图以展示模型关注区域。
*   基于 PyTorch 框架开发，便于在现有的深度学习工作流中集成与扩展。

3. **适用场景**
*   研究人员希望验证或调试计算机视觉模型是否关注了图像中的关键特征。
*   开发者需要在医疗影像或自动驾驶等高信任度领域，向用户展示 AI 的决策逻辑。
*   教育者希望向学生直观演示深度学习模型内部的注意力机制和工作原理。
*   工程师在进行模型优化时，通过分析错误案例来定位模型失效的具体原因。

4. **技术亮点**
*   高度模块化设计，兼容各类自定义网络结构，无需修改模型代码即可应用。
*   社区活跃且文档完善，拥有近 1.3 万星标，证明了其在可解释 AI 领域的广泛认可度。
*   不仅限于基础的 Grad-CAM，还封装了 Score-CAM 等进阶算法，提供更丰富的分析维度。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12906 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在通过可微分的图像处理原语，简化从传统视觉到深度学习的过渡。该项目为研究人员和工程师提供了高效、模块化的视觉算法工具集。

2. **核心功能**
*   提供基于 PyTorch 的可微分几何计算机视觉算子，支持端到端的深度学习集成。
*   包含丰富的传统图像处理功能，如色彩空间转换、形态学操作及滤波。
*   具备强大的相机标定与三维重建工具，支持针孔相机模型及姿态估计。
*   封装了常用的数据增强与图像变换方法，便于训练数据的高效预处理。

3. **适用场景**
*   **可微分视觉流水线开发**：在神经网络中直接嵌入几何约束或传统视觉步骤进行联合优化。
*   **机器人空间感知**：用于机器人导航、SLAM（同步定位与建图）中的位姿估计与环境理解。
*   **计算摄影与图像增强**：开发需要梯度反向传播参与的图像修复、去噪或风格迁移应用。

4. **技术亮点**
*   **完全可微分**：所有算子均支持自动微分，无缝融入 PyTorch 计算图。
*   **硬件加速**：充分利用 GPU/TPU 并行计算能力，显著提升批量图像处理速度。
*   **模块化设计**：接口简洁统一，易于扩展和集成到现有的 AI 框架中。
- 链接: https://github.com/kornia/kornia
- ⭐ 11269 | 🍴 1195 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 877 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3277 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2624 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2415 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382159 | 🍴 80186 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. 中文简介
SuperPowers 是一个经过实战验证的智能体技能框架与软件开发方法论。它通过子代理驱动开发模式，将复杂的编程任务分解为可管理的技能模块。该项目旨在提供一套高效、结构化的 AI 辅助编码工作流。

### 2. 核心功能
*   **子代理驱动开发**：利用专门的子代理处理细分任务，实现模块化的高效协作。
*   **智能技能框架**：提供预定义的“技能”集合，指导 AI 代理执行特定的开发步骤。
*   **结构化头脑风暴**：集成 AI 辅助的思维发散工具，帮助在编码前明确需求与设计思路。
*   **完整 SDLC 支持**：覆盖从需求分析到代码实现的软件开发生命周期全链路。
*   **自动化代码生成**：基于技能指令自动编写、调试和优化代码片段。

### 3. 适用场景
*   **复杂逻辑拆解**：将大型、模糊的项目需求分解为具体的、可由 AI 执行的子任务。
*   **AI 辅助结对编程**：开发者作为主代理，利用 SuperPowers 框架指挥子代理完成具体编码细节。
*   **快速原型开发**：通过标准化的技能流程加速 MVP（最小可行性产品）的代码构建速度。
*   **团队开发规范统一**：为团队提供一致的 AI 交互标准和开发方法论，减少沟通成本。

### 4. 技术亮点
*   **方法论先行**：不仅提供工具，更强调“软件开发方法论”，解决了纯工具类项目缺乏流程规范的痛点。
*   **多模态技能组合**：结合 Shell 脚本与其他语言特性，灵活适配不同技术栈的开发需求。
*   **高社区认可度**：拥有近 25 万星标的巨大影响力，证明其框架在实际开发中的广泛适用性。
- 链接: https://github.com/obra/superpowers
- ⭐ 249387 | 🍴 22135 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **1. 中文简介**
Hermes Agent 是一款能够随用户共同成长与进化的智能代理工具。它旨在通过持续学习和适应，为用户提供越来越精准、高效的辅助体验。该项目代表了新一代人机协作模式的探索与实践。

**2. 核心功能**
*   **自适应成长机制**：代理具备学习能力，能根据用户习惯和反馈不断优化自身表现。
*   **多模型支持**：兼容包括 Anthropic Claude、OpenAI GPT 等主流大语言模型。
*   **智能任务执行**：能够理解复杂指令并自主规划、执行各类编程或日常任务。
*   **无缝集成工作流**：设计用于融入开发者现有的代码库和日常操作环境。

**3. 适用场景**
*   **高级软件开发辅助**：作为 AI 结对程序员，协助处理复杂的代码重构、调试及新功能开发。
*   **个性化数字助手**：为需要长期记忆和上下文理解的用户提供定制化的信息整理与决策支持。
*   **自动化工作流构建**：利用其成长性配置复杂的自动化脚本，减少重复性人工操作。

**4. 技术亮点**
*   实现了基于用户交互数据的动态模型选择与提示词优化策略。
*   采用模块化架构，便于集成多种后端 LLM 提供商。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211320 | 🍴 38806 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个支持公平代码许可的工作流自动化平台，具备原生 AI 能力。它结合可视化构建与自定义代码，提供超过 400 种集成方式，并支持自托管或云端部署。

2. **核心功能**
*   **可视化工作流构建**：通过拖拽式界面轻松创建复杂的自动化逻辑。
*   **原生 AI 集成**：内置人工智能能力，可直接在流程中调用 LLM 等智能服务。
*   **广泛集成生态**：提供 400 多种预置连接器，无缝对接各类 API 和 SaaS 工具。
*   **灵活部署选项**：支持完全自托管以保障数据隐私，也可使用云托管服务。
*   **低代码/无代码混合模式**：既适合非技术人员快速上手，也允许开发者编写自定义代码实现高阶需求。

3. **适用场景**
*   **企业数据同步与处理**：自动在不同数据库、CRM 或 ERP 系统间迁移和清洗数据。
*   **AI 驱动的业务自动化**：利用大语言模型自动处理客户咨询、生成报告或分析文本数据。
*   **跨应用通知与工作流编排**：连接 Slack、Email、Jira 等工具，实现任务触发、审批流转和状态更新。
*   **个人开发者效率工具**：通过自托管方案低成本搭建个性化的自动化脚本，替代繁琐的手动操作。

4. **技术亮点**
*   基于 TypeScript 开发，类型安全且易于扩展。
*   采用“公平代码”许可证，平衡了开源社区的贡献与商业使用的合规性。
*   原生支持 MCP（Model Context Protocol），便于与更多 AI 上下文进行交互。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195645 | 🍴 59168 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- **1. 中文简介**
AutoGPT 致力于实现人人皆可访问的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。我们的使命是提供必要的工具，助您从繁琐的技术细节中解脱，从而专注于真正重要的事务。

**2. 核心功能**
*   具备自主代理能力，能独立规划并执行复杂的多步骤任务。
*   支持接入多种大型语言模型（LLM），包括 OpenAI GPT、Claude 及 Llama API 等。
*   提供高度可定制化的架构，允许开发者基于现有工具扩展新功能。
*   拥有庞大的开源社区支持，拥有极高的 GitHub 星标数和活跃度。

**3. 适用场景**
*   **自动化工作流**：用于自动完成数据抓取、信息整理或重复性办公任务。
*   **AI 应用原型开发**：作为构建更复杂 Agentic AI（智能体 AI）应用的底层框架或参考示例。
*   **研究与实验**：供研究人员探索大语言模型的自主决策边界及长期任务执行能力。

**4. 技术亮点**
*   **多模型兼容**：原生支持切换不同厂商的 LLM 后端，降低对单一供应商的依赖。
*   **Agent 范式先驱**：作为早期开源的自主智能体项目，确立了“规划-执行-反思”的典型交互模式。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185433 | 🍴 46124 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165069 | 🍴 21366 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164038 | 🍴 30398 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156881 | 🍴 46167 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151348 | 🍴 9471 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148165 | 🍴 23343 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

