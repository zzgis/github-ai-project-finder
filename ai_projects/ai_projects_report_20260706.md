# GitHub AI项目每日发现报告
日期: 2026-07-06

## 新发布的AI项目

### Vibe-Research
- ### Vibe-Research 项目分析

1. **中文简介**
   Vibe-Research 是一个由 AI 驱动的个性化投资研究智能体，支持 A 股、美股及港股市场。它整合了每日复盘、资讯雷达、个股与板块数据、持仓管理及研究记录等功能，旨在为用户提供一站式的数据与工具支持。

2. **核心功能**
   - 支持跨市场覆盖，包括 A 股、美股和港股的投资研究。
   - 提供每日复盘与资讯雷达，帮助用户及时捕捉市场动态。
   - 集成个股数据分析、板块中心查看及个人持仓管理模块。
   - 具备个人研究记录功能，便于追踪和分析投资逻辑。

3. **适用场景**
   - 需要同时关注多个全球主要股市（A 股/美股/港股）的个人投资者。
   - 希望利用 AI 助手自动化整理每日市场复盘与关键资讯的交易员。
   - 重视投资逻辑沉淀，需要系统化记录和研究个股数据的深度分析者。

4. **技术亮点**
   - 采用现代全栈技术组合，前端基于 React + TypeScript，后端利用 Python FastAPI。
   - 集成 MCP（Model Context Protocol）与大语言模型（LLM），实现智能化的数据交互与研究辅助。
- 链接: https://github.com/simonlin1212/Vibe-Research
- ⭐ 159 | 🍴 42 | 语言: TypeScript
- 标签: a-stock, ai-agent, dashboard, fastapi, fintech

### spicy-monopoly
- ### 1. 中文简介
这是一个基于 Python 开发的双人在线棋盘游戏，玩家可与 AI 进行实时对战。游戏结合了骰子、地图瓷砖以及代码驱动的“辛辣”互动任务，专为 18 岁以上用户设计。

### 2. 核心功能
*   **AI 双人对战**：支持人类玩家与人工智能对手进行回合制策略博弈。
*   **代码驱动机制**：游戏规则、移动逻辑及任务触发均由 Python 代码实时控制，确保公平性与可定制性。
*   **成人向互动内容**：内置 18+ 限制的“辛辣”挑战任务，增加游戏的刺激感与社交趣味。
*   **动态棋盘元素**：采用随机生成的骰子点数与地图瓷砖组合，提升每局游戏的变数。

### 3. 适用场景
*   **编程教学演示**：用于展示如何用 Python 构建简单的状态机游戏逻辑或 AI 决策树。
*   **开发者社交破冰**：在技术社区或线上聚会中作为轻量级互动工具，缓解紧张气氛。
*   **AI 算法测试沙盒**：为初学者提供一个低门槛环境，用于测试和调试基础的博弈 AI 算法。

### 4. 技术亮点
*   **全代码化规则引擎**：摒弃传统图形界面依赖，通过纯代码逻辑实现游戏状态管理，便于二次开发与集成。
*   **轻量级架构**：基于 Python 标准库或简易框架构建，资源占用少，易于本地部署与快速运行。
- 链接: https://github.com/RennAkira/spicy-monopoly
- ⭐ 124 | 🍴 17 | 语言: Python

### watch-skill
- ### 1. **中文简介**
该项目赋予AI代理观看视频以及审视并修正自身工作的能力。它支持MCP、CLI和REST接口，具备场景感知帧提取、OCR识别、本地优先转录及持久化索引等特性，并实现了闭环优化机制。

### 2. **核心功能**
- 使AI代理具备视频理解与自我纠错（“THE LOOP”）的能力。
- 提供MCP、CLI和REST三种接入方式，兼容多种集成场景。
- 支持场景感知的关键帧提取与OCR文字识别。
- 采用本地优先的语音转录策略，确保数据隐私与低延迟。
- 建立持久化索引以高效管理和检索视频内容。

### 3. **适用场景**
- **自动化视频内容分析**：用于从视频流中提取关键信息、字幕或元数据。
- **AI代理自我修复工作流**：允许AI在生成内容后自行回放检查并进行修正。
- **多模态RAG系统构建**：作为向量数据库的前端，将非结构化视频数据转化为可检索的结构化知识。
- **隐私敏感的视频处理**：利用本地优先转录功能，在不依赖外部API的情况下处理敏感视频内容。

### 4. **技术亮点**
- **闭环反馈机制（THE LOOP）**：独特的自我监控与修正架构，提升了AI输出的准确性。
- **本地优先架构**：强调本地处理转录数据，减少对云端服务的依赖，提升响应速度和安全性。
- **多协议支持**：同时兼容MCP（Model Context Protocol）、命令行和REST API，扩展性强。
- 链接: https://github.com/oxbshw/watch-skill
- ⭐ 67 | 🍴 12 | 语言: Python
- 标签: agent-tools, ai-agents, claude, claude-code, computer-vision

### OpenAI4S
- 1. **中文简介**
该项目利用成本极低的豆包 API 接口，模拟并复现了 Claude Science 的功能特性。它旨在以极低的经济成本（约 9.9 元人民币）实现类似高端大语言模型的科学计算与分析能力。

2. **核心功能**
*   低成本接入豆包大模型 API，大幅降低使用门槛。
*   通过 Prompt 工程或中间层适配，复刻 Claude Science 的科学推理能力。
*   基于 Python 开发，提供轻量级的代码调用示例。

3. **适用场景**
*   预算有限的个人开发者或学生尝试科学类 AI 应用。
*   需要低成本替代方案进行基础科学数据查询或逻辑推理的项目。
*   对 Claude 生态感兴趣但希望控制 API 成本的爱好者。

4. **技术亮点**
*   极高的性价比，以极低费用实现特定领域的高阶模型功能模拟。
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 59 | 🍴 5 | 语言: Python

### TokHub
- 1. **中文简介**
TokHub 是一个基于 TypeScript 开发的 OpenAI 兼容专属网关系统，兼具 AI API 中转站的监控、推荐运营与流量管理能力。它支持 Docker 自托管部署，提供分层探测、健康评分及用量计量等核心功能，旨在帮助用户高效管理 API 资源并保障服务稳定性。

2. **核心功能**
*   **OpenAI 兼容网关**：作为中间件层，无缝对接各类 AI API 提供商，保持接口标准一致性。
*   **智能路由与推荐**：通过健康评分和分层探测机制，自动推荐最优 API 节点以提升服务可用性。
*   **精细化用量计量**：实时统计各渠道或用户的 API 调用量，便于成本核算与管理。
*   **监控与告警审计**：内置健康状态监控、异常告警及操作审计日志，确保系统运行透明可控。
*   **Docker 自托管**：支持容器化一键部署，方便用户在自己的服务器环境中私有化运行。

3. **适用场景**
*   **API 聚合代理运营**：适合希望整合多家 AI 厂商接口，为用户提供统一入口并实现智能切换的服务商。
*   **企业内部 API 网关**：适用于需要集中管控员工或内部应用对 AI 服务的访问权限、配额及成本的企业 IT 部门。
*   **高可用架构搭建**：适合对服务稳定性要求极高的场景，通过健康检查和自动故障转移降低单点故障风险。
*   **私有化部署需求**：满足数据隐私敏感或网络受限环境下的用户，需将 AI 网关完全控制在自己基础设施中。

4. **技术亮点**
*   **分层探测与健康评分算法**：通过多维度检测 API 状态并打分，实现智能化的流量调度与故障隔离。
*   **全栈 TypeScript 开发**：保证代码类型安全与开发效率，同时提供优秀的 IDE 支持和维护性。
*   **轻量级自托管架构**：无需依赖复杂的外部云服务，通过 Docker 即可快速构建独立的 API 管理中枢。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 45 | 🍴 4 | 语言: TypeScript

### OmniPost-AI
- 描述: AI-powered Chrome extension for generating and publishing posts to Facebook, Threads, and X using ChatGPT or Gemini.
- 链接: https://github.com/wanglinsaputra/OmniPost-AI
- ⭐ 42 | 🍴 21 | 语言: TypeScript
- 标签: ai, automation, chatgpt, chrome-extension, gemini

### OpenStudio
- 描述: OpenStudio - an open-source AI image, video, cinema, reels and lip sync studio powered by MuAPI
- 链接: https://github.com/generalizingai/OpenStudio
- ⭐ 38 | 🍴 5 | 语言: JavaScript

### bike4mind
- 描述: The open-core AI workbench — notebooks, agents, RAG, voice, and images across any model: OpenAI, Anthropic, Google, xAI, or local via Ollama/vLLM. BSL 1.1,  auto-converting to Apache-2.0 on a two-year clock. Your AI keeps running when theirs doesn't.
- 链接: https://github.com/Bike4Mind/bike4mind
- ⭐ 35 | 🍴 10 | 语言: TypeScript
- 标签: agents, ai, ai-agents, ai-workbench, anthropic

### AI-wiki
- 描述: AI Full Stack: Data, Algorithms, Models, Hardware, Architecture
- 链接: https://github.com/lvy010/AI-wiki
- ⭐ 33 | 🍴 3 | 语言: 未知

### NavoIM
- 描述: Navo IM 是一款注重隐私与实时体验的即时通讯产品。支持端到端加密、频道与 AI 助手等功能。由 Navo 团队开发与维护。
- 链接: https://github.com/aijianai/NavoIM
- ⭐ 31 | 🍴 0 | 语言: TypeScript

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. **中文简介**
该项目是一个全面且实用的自然语言处理（NLP）工具库，主要涵盖中英文敏感词检测、语言识别、手机号/身份证等个人信息抽取以及繁简转换等基础功能。它不仅提供了丰富的垂直领域词库（如汽车、医疗、法律等），还集成了多种预训练模型资源、数据集及前沿NLP算法工具，旨在为开发者提供一站式的中英双语NLP解决方案。

### 2. **核心功能**
*   **基础文本处理与抽取**：支持敏感词过滤、中英文语言检测、手机号/邮箱/身份证正则抽取及繁简体转换。
*   **丰富领域词库资源**：内置中日文人名库、职业/品牌/诗词/成语等各类垂直领域词库，以及同义词、反义词、停用词和情感值数据。
*   **预训练模型与深度学习工具**：汇集BERT、ALBERT、GPT-2等主流预训练模型资源，提供NER、文本分类、摘要生成等任务的代码模板和工具。
*   **知识图谱与问答系统**：包含多个开源知识图谱构建工具、医疗/金融领域问答数据集及对话机器人相关资源。
*   **语音与OCR辅助工具**：集成中文语音识别（ASR）语料、汉字OCR识别工具及发音标注模块。

### 3. **适用场景**
*   **内容安全审核平台**：利用敏感词库和语言检测功能，快速构建网站或APP的内容过滤系统。
*   **垂直行业智能客服研发**：基于医疗、法律、汽车等领域的专用词库和问答数据集，训练高精度的行业对话机器人。
*   **个人信息保护与合规审计**：使用手机号、身份证、邮箱等正则抽取功能，自动化扫描文本中的隐私数据泄露风险。
*   **NLP算法研究与原型开发**：借助其提供的BERT微调模板、词向量资源和标注工具，加速自然语言处理模型的开发与验证。

### 4. **技术亮点**
*   **资源聚合度高**：不仅包含自研工具，还整合了清华、百度、Facebook等机构的高质量开源数据集、代码库和技术报告，是NLP入门和进阶的优质资源站。
*   **全栈覆盖**：从低阶的文本清洗、分词、词性标注，到中阶的知识图谱构建，再到高阶的预训练模型微调和应用，覆盖了NLP全流程。
*   **实用性强**：提供的工具多为开箱即用的Python包或脚本，如`jieba_fast`加速分词、`cnocr`中文OCR、`g2pC`拼音标注等，极大降低了工程落地门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81638 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35217 | 🍴 7326 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够将复杂的模型结构转化为直观的图表展示。该工具旨在帮助开发者快速理解和分析模型架构。

### 2. 核心功能
*   支持广泛的后端框架格式，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等。
*   提供直观的图形化界面，清晰展示网络层结构、张量形状及数据流向。
*   兼容多种存储格式，如 Safetensors、NumPy 数组及 TFLite 文件。
*   支持在浏览器或桌面环境中直接运行，无需安装复杂的依赖环境。
*   允许用户交互式地探索模型细节，便于调试和性能优化。

### 3. 适用场景
*   **模型调试与验证**：在训练完成后，通过可视化检查网络结构是否符合预期，排查连接错误。
*   **学术交流与演示**：将复杂的深度学习模型结构生成清晰的图表，用于论文写作或技术分享。
*   **跨框架迁移分析**：当模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 时，对比前后结构一致性。
*   **教育学习**：帮助初学者直观理解卷积神经网络（CNN）、循环神经网络（RNN）等架构的工作原理。

### 4. 技术亮点
*   **轻量级与易用性**：基于 JavaScript 构建，支持 Web 浏览器直接打开，部署门槛极低。
*   **广泛的格式兼容性**：几乎涵盖所有主流的 AI 模型导出格式，是跨平台模型可视化的通用标准工具之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33186 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型交换与部署，打破生态壁垒。

2. **核心功能**
*   定义开放的模型文件格式，支持跨框架模型转换。
*   提供标准化的算子库，确保模型在不同后端的一致性。
*   支持多种主流框架（如 PyTorch、TensorFlow、Keras）的双向转换。
*   优化推理性能，适配各类硬件加速器及边缘设备。

3. **适用场景**
*   需要将训练好的模型从 PyTorch 迁移到 TensorFlow 或反之。
*   在资源受限的边缘设备上部署深度学习模型进行推理。
*   构建统一的后端推理服务以支持多种前端训练框架。

4. **技术亮点**
*   作为行业事实标准，被 Microsoft、Facebook、Amazon 等巨头广泛支持。
*   具备强大的生态系统兼容性，无缝连接训练与生产环境。
- 链接: https://github.com/onnx/onnx
- ⭐ 21105 | 🍴 3961 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. **中文简介**
《机器学习工程开放书籍》是一本全面涵盖机器学习工程实践的知识库，深入探讨了从模型训练、调试到大规模推理和部署的全流程技术细节。该项目聚焦于解决高性能计算环境下的可扩展性挑战，为构建稳定高效的AI系统提供了实用指南。

### 2. **核心功能**
- 提供针对大型语言模型（LLM）在GPU集群上的分布式训练与优化策略。
- 详细解析PyTorch框架下的高性能推理加速技术及内存管理技巧。
- 介绍基于Slurm等调度系统的超算环境配置及网络存储优化方案。
- 涵盖模型调试、数据管道构建及MLOps流水线自动化最佳实践。

### 3. **适用场景**
- 研发大规模预训练语言模型或微调基础模型的工程团队。
- 需要优化深度学习模型在受限硬件资源下推理延迟的生产环境。
- 搭建和管理高性能计算集群以支持海量数据并行处理的IT基础设施部门。

### 4. **技术亮点**
- 深度整合了Hugging Face Transformers生态与底层硬件优化的最佳实践。
- 针对实际工程痛点（如OOM错误、通信瓶颈）提供了具体的代码级解决方案。
- 内容紧跟前沿，特别关注了当前流行的LLM工程化落地需求。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18248 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17263 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11559 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目汇集了丰富的实战案例，覆盖了从基础理论到高级应用的广泛领域。它旨在为开发者提供一个全面的学习资源和项目参考库。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等领域的500多个完整项目代码。
*   整合了人工智能领域的经典与前沿算法实现，便于快速复现和研究。
*   作为“Awesome”系列资源，对高质量AI项目进行了系统化的整理和分类。
*   支持Python等主流语言的项目源码获取，降低入门和实践门槛。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习的基础应用。
*   研究人员或工程师寻找特定领域（如CV或NLP）的代码参考以加速开发进程。
*   教育机构或培训团队用于构建课程体系，提供丰富的实战教学案例。

4. **技术亮点**
*   项目规模庞大且分类清晰，是学习AI多分支领域的综合性资源库。
*   结合了“Awesome”标签的高标准筛选，确保了收录项目的质量和多样性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35217 | 🍴 7326 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够将复杂的模型结构转化为直观的图表展示。该工具旨在帮助开发者快速理解和分析模型架构。

### 2. 核心功能
*   支持广泛的后端框架格式，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等。
*   提供直观的图形化界面，清晰展示网络层结构、张量形状及数据流向。
*   兼容多种存储格式，如 Safetensors、NumPy 数组及 TFLite 文件。
*   支持在浏览器或桌面环境中直接运行，无需安装复杂的依赖环境。
*   允许用户交互式地探索模型细节，便于调试和性能优化。

### 3. 适用场景
*   **模型调试与验证**：在训练完成后，通过可视化检查网络结构是否符合预期，排查连接错误。
*   **学术交流与演示**：将复杂的深度学习模型结构生成清晰的图表，用于论文写作或技术分享。
*   **跨框架迁移分析**：当模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 时，对比前后结构一致性。
*   **教育学习**：帮助初学者直观理解卷积神经网络（CNN）、循环神经网络（RNN）等架构的工作原理。

### 4. 技术亮点
*   **轻量级与易用性**：基于 JavaScript 构建，支持 Web 浏览器直接打开，部署门槛极低。
*   **广泛的格式兼容性**：几乎涵盖所有主流的 AI 模型导出格式，是跨平台模型可视化的通用标准工具之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33186 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了必不可少的速查手册（Cheat Sheets），涵盖了从基础概念到高级工具的核心知识。它通过简洁的图表和代码示例，帮助研究者快速回顾关键算法、库函数及数学原理，是提升学习效率的优质资源。

### 2. 核心功能
- **全面覆盖核心领域**：包含机器学习、深度学习、Keras、NumPy、SciPy 和 Matplotlib 等关键技术栈的速查表。
- **直观的知识梳理**：将复杂的算法流程和数学公式转化为易于理解的图表和要点，便于快速记忆和查阅。
- **研究辅助工具**：专为研究人员设计，帮助在实验设计和模型调试时快速定位所需的技术细节。
- **多语言/多框架支持**：整合了主流 AI 框架（如 Keras）和数据科学库（如 NumPy、Matplotlib）的标准用法。

### 3. 适用场景
- **面试准备**：求职者利用速查表快速复习机器学习算法和编程库知识，应对技术面试。
- **项目启动参考**：研究人员在开始新实验前，快速查阅特定库（如 Matplotlib 绘图或 NumPy 操作）的常用语法。
- **日常学习巩固**：学生或从业者作为随身笔记，用于随时回顾深度学习理论或代码实现细节。

### 4. 技术亮点
- **高人气社区认可**：拥有超过 15,000 星标，证明其内容质量和实用性受到全球开发者的广泛肯定。
- **结构化知识呈现**：不同于传统文档，采用视觉化的“速查”形式，极大降低了信息检索的时间成本。
- **权威来源背书**：基于 Medium 上知名技术博主整理的精选内容，确保知识点的准确性和前沿性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并提升就业竞争力。内容涵盖Python、数学基础、机器学习、深度学习、计算机视觉及自然语言处理等主流AI领域的核心技术与工具库。

### 2. 核心功能
*   提供系统化的AI学习路径规划，覆盖从基础到进阶的完整知识体系。
*   收录近200个实战案例和项目代码，支持动手实践以巩固理论知识。
*   集成主流AI框架与工具库教程（如PyTorch、TensorFlow、Pandas、NumPy等）。
*   提供免费的配套学习教材和资源，降低人工智能学习门槛。

### 3. 适用场景
*   **零基础转行**：希望进入人工智能行业但缺乏编程和算法基础的初学者。
*   **求职准备**：需要积累实战项目经验以提升简历竞争力的求职者。
*   **技能查漏补缺**：已有一定基础，希望系统梳理机器学习、深度学习或NLP/CV特定领域知识的学习者。

### 4. 技术亮点
*   高度聚合了当前AI领域最热门的开源框架（TensorFlow/PyTorch/Keras）与数据科学库（Pandas/Seaborn/Matplotlib）。
*   强调“实战导向”，通过大量现成案例直接对接工业界常见应用场景。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **项目名称**：Ludwig

### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建过程。它通过声明式的配置方式，让开发者能够无需编写复杂的底层代码即可快速训练和部署机器学习模型。该项目特别适用于希望降低深度学习门槛并专注于数据而非工程实现的数据科学家和研究人员。

### 2. 核心功能
*   **低代码/无代码建模**：通过简单的 YAML 或 JSON 配置文件定义模型架构和数据预处理流程，大幅减少编码工作量。
*   **广泛的模型支持**：原生支持从传统机器学习算法到基于 PyTorch 的深度神经网络，以及针对 LLM（如 Llama、Mistral）的微调和训练。
*   **自动化数据处理**：内置强大的数据管道，自动处理缺失值、类别编码、归一化等数据-centric 的关键步骤。
*   **实验跟踪与可视化**：提供直观的仪表盘来监控训练进度、评估指标及模型性能，便于迭代优化。
*   **易于部署**：支持将训练好的模型一键导出为多种格式，方便集成到生产环境或 API 服务中。

### 3. 适用场景
*   **快速原型开发**：数据科学家需要快速验证假设，通过少量配置即可测试不同模型在特定数据集上的表现。
*   **LLM 微调与应用**：开发者希望使用 Llama、Mistral 等大语言模型进行领域特定的微调，而不想处理繁琐的训练脚本。
*   **结构化数据竞赛与项目**：在处理表格型数据（Tabular Data）时，利用 Ludwig 自动化的特征工程和模型选择来获得基线效果。
*   **企业级 AI 落地**：团队希望标准化机器学习工作流程，降低对资深深度学习工程师的依赖，提高模型交付效率。

### 4. 技术亮点
*   **数据-centric 设计理念**：强调数据质量对模型性能的影响，提供自动化数据清洗和增强工具，而非仅关注模型架构。
*   **基于 PyTorch 的后端**：充分利用 PyTorch 的灵活性和生态优势，同时屏蔽了底层复杂细节，兼顾性能与易用性。
*   **开箱即用的 LLM 集成**：直接支持主流开源大语言模型的加载、微调和推理，降低了使用生成式 AI 的技术门槛。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1235 | 语言: Python
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
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6224 | 🍴 734 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
该项目是中文自然语言处理（NLP）领域的综合性资源库，汇集了海量的中文NLP数据集、预训练模型、开源工具及经典算法实现。它涵盖了从基础的分词、词性标注到高级的知识图谱构建、语音识别及对话系统等全方位内容，旨在为开发者提供一站式的NLP研究与开发支持。

**2. 核心功能**
*   **数据资源丰富**：提供涵盖中英文敏感词、姓名、地名、行业术语等多维度的词库及大规模语料数据集（如问答、对话、谣言检测）。
*   **工具链完整**：集成分词（如jieba）、命名实体识别、情感分析、文本摘要、关键词抽取等多种NLP基础与进阶工具。
*   **模型与算法汇集**：收录BERT、GPT-2、ALBERT等主流预训练模型的中文版本及微调代码，并包含各类深度学习模型在NLP任务中的应用案例。
*   **多模态支持**：除了纯文本处理，还包含语音识别（ASR）、OCR文字识别、音频数据处理及相关数据集。

**3. 适用场景**
*   **NLP初学者入门**：通过提供的教程、数据集和基础工具（如分词、情感分析），快速掌握中文NLP的基本流程和常用技术。
*   **企业级应用开发**：利用现成的敏感词过滤、身份验证（身份证/手机号提取）、知识图谱构建方案，加速智能客服、内容审核等系统的开发。
*   **学术研究与模型调优**：获取最新的预训练模型权重、基准测试数据集（Benchmark）及SOTA算法代码，用于复现论文或进行模型改进研究。

**4. 技术亮点**
*   **全栈式资源聚合**：不仅包含代码，还整合了数据集、API、论文解读及行业报告，形成了完整的NLP生态闭环。
*   **紧跟前沿技术**：及时更新并收录了BERT、Transformer、GPT等大模型时代的最新中文适配方案及垂直领域（如医疗、法律）专用模型。
*   **实用性强**：提供了大量开箱即用的工具包（如OCR、语音转写、繁简转换）和具体业务场景下的解决方案（如简历解析、智能对联），极大降低了落地门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81638 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目已发表于 ACL 2024，旨在简化从指令微调到强化学习的全流程开发体验。它通过整合多种前沿技术，为研究人员和开发者提供了轻量级且高性能的微调解决方案。

2. **核心功能**
*   **多模型统一支持**：无缝兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100 多种开源大模型及视觉语言模型。
*   **多样化微调算法**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调方法，以及全参数微调选项。
*   **高级对齐技术**：支持 RLHF（基于人类反馈的强化学习）、DPO（直接偏好优化）等高级对齐训练策略。
*   **量化与低资源优化**：提供 INT8/INT4 等量化训练支持，显著降低显存占用，使消费级显卡也能运行大规模微调。
*   **一站式训练流程**：集成数据预处理、模型训练、评估及导出功能，简化了从准备到部署的完整工作流。

3. **适用场景**
*   **垂直领域知识注入**：为企业或特定行业（如医疗、法律）的大模型注入私有数据，提升专业问答能力。
*   **低成本模型定制**：利用 QLoRA 等技术，在显存受限的消费级 GPU 上快速微调大型模型，降低硬件门槛。
*   **多模态应用开发**：对支持图像理解的视觉语言模型进行微调，打造具备图文交互能力的智能助手。
*   **RLHF 研究与落地**：快速实现基于人类偏好优化的模型对齐实验，提升生成内容的质量与安全性。

4. **技术亮点**
*   **ACL 2024 学术背书**：作为经过顶级学术会议评审的研究级项目，其架构设计与性能优化具有极高的可靠性。
*   **极致的资源效率**：通过创新的混合精度训练和量化技术，实现了在有限硬件资源下对超大模型的稳定微调。
*   **广泛的生态兼容性**：深度适配 Hugging Face Transformers 生态，同时支持多种后端加速库，确保训练速度与稳定性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73015 | 🍴 8925 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### AI-For-Beginners 项目分析

1. **中文简介**
   这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI。该项目通过结构化的教学路径，覆盖从基础概念到深度学习的核心知识。它特别适合希望系统掌握AI技能的初学者和非专业人士。

2. **核心功能**
   - 提供结构化的12周学习计划，分24节课循序渐进地讲解AI知识。
   - 基于Jupyter Notebook开发，支持交互式代码练习和即时反馈。
   - 涵盖机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等核心领域。
   - 由Microsoft For Beginners项目支持，确保内容的准确性和教育价值。
   - 免费开放源码，便于全球学习者自主学习和实践。

3. **适用场景**
   - 零基础学生或转行者希望系统入门人工智能领域。
   - 教育工作者用于设计AI通识课程或补充教学资源。
   - 企业团队进行内部AI技术培训，提升员工技术素养。
   - 对AI感兴趣的公众参与自学，探索前沿技术如CV和NLP。

4. **技术亮点**
   - 采用Jupyter Notebook作为主要载体，实现理论与实践紧密结合。
   - 内容覆盖广泛，包括CNN、RNN、GAN等热门深度学习架构。
   - 由知名科技公司（Microsoft）背书，保证教学质量和资源权威性。
   - 标签体系清晰，便于用户根据兴趣筛选特定技术方向（如AI、ML、DL）。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51795 | 🍴 10457 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并公开了包括 Anthropic（Claude系列）、OpenAI（ChatGPT/GPT系列）、Google（Gemini系列）以及 xAI 在内的多个主流大语言模型及 AI 代理的系统提示词。项目内容涵盖 Claude Fable 5、Opus 4.8、ChatGPT 5.5 Thinking 等具体模型的内部指令，并定期更新以反映最新变化。

2. **核心功能**
*   **多平台系统提示词提取**：汇集来自 Anthropic、OpenAI、Google 和 xAI 等不同厂商的大型语言模型及代码助手的系统指令。
*   **定期自动更新**：持续追踪并收录最新发布的模型版本（如 Claude 和 GPT 的最新迭代）的系统配置信息。
*   **开源共享知识库**：以开源形式提供结构化的提示词数据，便于研究人员和开发者直接查阅或集成使用。

3. **适用场景**
*   **提示词工程研究**：帮助研究人员深入理解不同商业模型的行为边界和底层指令逻辑。
*   **AI 安全与红队测试**：安全专家可利用这些泄露的系统提示词来模拟攻击，评估模型在对抗性环境下的鲁棒性和潜在漏洞。
*   **同类模型微调参考**：开发者可通过分析头部模型的系统指令设计，优化自研模型或开源模型的提示词策略，提升输出质量。

4. **技术亮点**
*   **覆盖前沿模型版本**：项目不仅包含已知模型，还特别标注了如“Claude Fable 5”、“GPT 5.5”等较新或特定版本的系统配置，具有较高的时效性。
*   **跨生态整合**：同时涵盖通用聊天机器人、代码生成工具（如 Cursor、Copilot）及搜索助手（Perplexity），提供了全面的 AI 生态视角。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 51302 | 🍴 8366 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- ### GitHub 项目分析：ailearning

**1. 中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解了线性代数、PyTorch 及 NLTK 等基础理论与工具。它结合了 TensorFlow 2，旨在帮助开发者系统性地掌握从传统算法到深度学习的完整技术栈。

**2. 核心功能**
*   提供机器学习经典算法（如 SVM、KMeans、逻辑回归）的代码实现与实战解析。
*   集成深度学习框架（PyTorch 和 TensorFlow 2），涵盖 RNN、LSTM、DNN 等神经网络模型。
*   包含自然语言处理（NLP）模块，利用 NLTK 进行文本分析与推荐系统开发。
*   梳理数据科学数学基础，重点讲解线性代数在算法中的应用。

**3. 适用场景**
*   初学者系统学习机器学习与深度学习理论及代码实现。
*   数据科学家查阅经典算法（如 Apriori、FP-Growth）的工程化落地案例。
*   NLP 开发者使用 PyTorch 或 TF2 构建文本分类、序列标注等模型时的参考。

**4. 技术亮点**
*   **全栈覆盖**：同时支持主流深度学习框架 PyTorch 和 TensorFlow 2，兼容性强。
*   **理论与实践结合**：不仅提供算法代码，还强调线性代数等数学基础的理解。
*   **社区认可度高**：拥有超过 42k 的星标，证明了其在中文 AI 学习社区中的广泛影响力。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42358 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37502 | 🍴 6236 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35217 | 🍴 7326 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33718 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28382 | 🍴 3447 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25838 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目通过提供丰富的实战代码示例，帮助开发者快速掌握各类人工智能技术的应用与实现。

2. **核心功能**
*   提供大量经过验证的机器学习与深度学习实战代码库。
*   集成计算机视觉与自然语言处理（NLP）领域的经典算法实现。
*   作为“Awesome”列表，系统性梳理了AI领域的重要项目资源。
*   以Python为主要技术栈，支持快速复现和二次开发。

3. **适用场景**
*   AI初学者用于学习基础算法原理并上手编写代码。
*   研究人员寻找特定领域（如CV或NLP）的参考实现方案。
*   工程师在构建智能应用时，直接复用成熟的项目模块加速开发。

4. **技术亮点**
*   极高的社区认可度（35k+星标），内容经过广泛筛选与验证。
*   分类清晰，全面覆盖从传统机器学习到前沿深度学习的核心技术栈。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35217 | 🍴 7326 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流。它通过结合大语言模型（LLM）和计算机视觉技术，能够像人类一样理解网页并执行操作。该项目旨在提供一种无需编写代码即可实现 RPA（机器人流程自动化）的智能解决方案。

2. **核心功能**
*   **AI 驱动的操作执行**：利用 LLM 分析页面内容并自动点击、填写表单或导航，替代传统的固定选择器脚本。
*   **多浏览器引擎支持**：底层兼容 Playwright 和 Puppeteer，确保在主流浏览器环境中的稳定运行。
*   **计算机视觉辅助**：结合视觉识别技术处理动态加载或非标准布局的网页元素，提高自动化成功率。
*   **无代码工作流编排**：允许用户通过自然语言指令定义任务，无需深入掌握 Selenium 或 Puppeteer 等工具的代码细节。
*   **API 集成能力**：提供 API 接口，便于将自动化能力嵌入到现有的业务流程或企业系统中。

3. **适用场景**
*   **跨平台数据抓取与录入**：自动化从不同网站提取数据并填入内部系统或表格，避免手动复制粘贴。
*   ** repetitive Web 表单处理**：批量完成需要频繁登录、验证和提交信息的在线注册、报销或审批流程。
*   **电商监控与比价**：定期自动访问电商平台，监控商品价格、库存变化并生成报告。
*   **传统 RPA 难以覆盖的场景**：处理那些 DOM 结构频繁变动或缺乏稳定 CSS 选择器的动态网页应用。

4. **技术亮点**
*   **LLM + Vision 混合架构**：不同于仅依赖 DOM 解析的传统自动化工具，Skyvern 结合了语义理解和图像识别，能应对更复杂的 UI 交互。
*   **超越 Selenium 的稳定性**：通过 Playwright/Puppeteer 后端和 AI 决策层，减少因页面微小变动导致的脚本崩溃问题。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22130 | 🍴 2072 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，支持图像、视频及3D数据的AI辅助标注、质量保证和团队协作。它提供开源、云及企业版产品，并配备开发者API，助力视觉AI应用开发。

2. **核心功能**
- 支持图像、视频和3D点云的多模态数据标注。
- 集成AI辅助标注功能，显著提升数据处理效率。
- 提供完善的质量保证机制与团队协同工作能力。
- 开放开发者API，便于集成至现有工作流。
- 提供数据分析仪表盘以监控项目进度与质量。

3. **适用场景**
- 深度学习模型训练所需的大规模标注数据集构建。
- 需要高精度标注的计算机视觉算法研发测试。
- 大型团队协同进行复杂视频或3D场景标注任务。
- 企业级部署下对数据安全性和流程管控有严格要求的场景。

4. **技术亮点**
- 采用Python开发，生态兼容性好，易于扩展。
- 同时支持多种主流深度学习框架（如PyTorch, TensorFlow）的数据需求。
- 覆盖从图像分类到语义分割等多种细粒度标注类型。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16232 | 🍴 3736 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目旨在为计算机视觉领域提供高级的可解释性AI工具，支持卷积神经网络（CNN）和视觉Transformer等多种模型。它涵盖了分类、目标检测、语义分割及图像相似度分析等多种任务，帮助用户深入理解模型的决策依据。

2. **核心功能**
*   全面支持CNN与Vision Transformer等主流深度学习架构的可解释性分析。
*   覆盖图像分类、目标检测、语义分割及图像相似度比对等多种计算机视觉任务。
*   集成Grad-CAM、Score-CAM等多种先进的类激活映射算法以生成可视化热力图。
*   提供直观的可视化工具，帮助用户解读黑盒模型的内部决策逻辑。

3. **适用场景**
*   在医疗影像分析中，通过高亮关键区域来辅助医生验证AI诊断结果的可靠性。
*   在自动驾驶研发中，分析目标检测模型对特定障碍物（如行人或车辆）的关注点。
*   学术研究或模型调试时，利用可视化特征图排查模型是否学到了错误的关联特征。

4. **技术亮点**
*   高度兼容PyTorch框架，并广泛适配各类前沿视觉Transformer模型。
*   不仅限于基础的Grad-CAM，还集成了Score-CAM等更先进的可解释性算法变体。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12900 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **项目名称：** kornia

**1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在为深度学习研究者和开发者提供可微分的计算机视觉原语。该库支持在 GPU 上高效执行传统的图像处理与几何变换操作。

**2. 核心功能**
*   提供完全可微分的计算机视觉算子，便于集成到深度神经网络中。
*   支持多种几何变换、图像增强及相机校准等传统 CV 任务。
*   原生兼容 PyTorch 张量，实现无缝的端到端 GPU 加速计算。
*   包含丰富的空间推理工具，如透视变换、仿射变换及特征匹配。
*   提供模块化且易于使用的 API，简化复杂视觉算法的实现流程。

**3. 适用场景**
*   需要集成传统计算机视觉预处理步骤的可微分深度学习模型开发。
*   机器人视觉系统中的实时姿态估计与三维重建任务。
*   自动驾驶或增强现实（AR）应用中涉及几何约束的场景处理。
*   利用 GPU 加速进行大规模图像数据增强和数据集生成。

**4. 技术亮点**
*   **全可微性**：打破传统 CV 库不可导的限制，允许梯度反向传播至视觉模块。
*   **硬件加速**：充分利用 NVIDIA GPU 进行并行计算，显著提升处理速度。
*   **PyTorch 原生**：无需转换数据格式，直接操作 Tensor，降低工程复杂度。
- 链接: https://github.com/kornia/kornia
- ⭐ 11268 | 🍴 1194 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3454 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3270 | 🍴 400 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2622 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2416 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款支持全平台和个人数据自主掌控的 AI 助手，旨在让用户在任何操作系统上都能拥有专属的智能化身。它强调“龙虾方式”（The lobster way），寓意数据完全私有化与本地化运行，确保隐私安全。

### 2. 核心功能
- **全平台兼容**：支持在任意操作系统和平台上部署运行，实现无缝跨设备体验。
- **数据主权**：强调“Own Your Data”，所有数据和交互记录由用户完全掌控，无需依赖第三方云服务。
- **个人化 AI 助手**：作为用户的私人智能代理，能够根据用户习惯进行个性化学习和辅助。
- **TypeScript 开发**：基于 TypeScript 构建，保证代码的可维护性、类型安全性和良好的开发者体验。
- **开源生态**：作为开源项目，允许社区参与贡献，保持透明度和可扩展性。

### 3. 适用场景
- **隐私敏感用户**：希望完全控制个人数据、拒绝云端存储的高隐私需求人群。
- **开发者与技术爱好者**：喜欢自行部署服务、定制 AI 行为并利用 TypeScript 进行二次开发的极客。
- **多设备办公人士**：需要在不同操作系统（如 macOS、Linux、Windows）间同步个人 AI 助手的远程工作者。
- **个人知识管理**：希望将 AI 助手与本地笔记、文档结合，打造个人专属知识库和智能检索工具的用户。

### 4. 技术亮点
- **本地优先架构**：设计上倾向于本地运行，减少对外部 API 的依赖，提升响应速度和数据安全性。
- **模块化设计**：基于 TypeScript 的模块化结构，便于集成各种 AI 模型和服务插件。
- **高社区关注度**：拥有超过 38 万星标，证明其在开源 AI 助手领域具有广泛的影响力和活跃的社区支持。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381948 | 🍴 80112 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 247656 | 🍴 21979 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的信息，以下是对 **Hermes Agent** 项目的技术分析：

1. **中文简介**
Hermes Agent 是一款旨在随用户共同成长的人工智能代理工具，能够适应并优化个人的工作流。它通过整合多种大型语言模型（LLM）的能力，为用户提供持续进化且个性化的智能辅助体验。

2. **核心功能**
*   支持多模型集成，兼容 Anthropic、OpenAI 等主流 LLM 提供商。
*   具备自适应学习能力，能根据用户交互习惯不断优化代理行为。
*   提供类似 Codex 或 Claude Code 的高级代码生成与处理能力。
*   拥有模块化架构，允许用户自定义标签和扩展特定功能。
*   实现自然语言交互界面，降低复杂 AI 工具的使用门槛。

3. **适用场景**
*   开发者需要高效的代码助手进行日常编码、调试及重构工作。
*   研究人员希望利用开源框架快速搭建和测试定制化 AI Agent。
*   企业或个人希望构建能够长期记忆并随时间进化的智能工作流。
*   技术爱好者探索多模型协同工作（如同时调用 Claude 和 GPT）的高级应用。

4. **技术亮点**
该项目最大的亮点在于其“成长性”设计理念，即代理并非静态工具，而是能通过持续交互积累上下文和用户偏好，从而在长期使用中提供愈发精准和个性化的服务，同时保持对多个顶级 AI 模型的广泛兼容性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210293 | 🍴 38505 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一款支持自托管或云端部署的公平代码工作流自动化平台，原生集成 AI 能力。它结合了可视化构建与自定义代码开发，并提供超过 400 种集成选项。

### 2. 核心功能
*   提供超过 400 种应用和 API 的原生集成支持。
*   支持可视化拖拽构建与自定义代码编写的混合开发模式。
*   具备原生 AI 能力，可轻松将人工智能引入自动化流程。
*   允许用户选择自托管或云端部署，保障数据隐私与控制权。
*   支持 MCP（模型上下文协议）客户端与服务端集成，增强 AI 连接性。

### 3. 适用场景
*   需要高度自定义且关注数据隐私的企业级内部系统自动化集成。
*   希望利用 AI 辅助生成内容或处理数据的低代码/无代码工作流搭建。
*   连接多个不同 SaaS 服务以同步数据、触发通知或管理业务流程。

### 4. 技术亮点
*   基于 TypeScript 开发，类型安全且易于扩展。
*   采用“公平代码”许可，兼顾社区贡献与商业使用的灵活性。
*   原生支持 MCP 协议，便于与现代 AI 代理和数据源进行标准化交互。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195436 | 🍴 59123 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可及的 AI 愿景，让用户能够轻松使用并基于此构建应用。其使命是提供必要的工具，使您能专注于真正重要的事务。

2. **核心功能**
*   支持自主代理（Autonomous Agents），能够独立规划并执行复杂的多步骤任务。
*   集成多种大型语言模型（LLM），包括 OpenAI、Claude 和 Llama 等接口。
*   提供丰富的工具链，允许代理访问互联网、文件系统及其他外部 API。
*   具备自我反思与纠错机制，通过迭代优化提升任务完成的准确率。
*   采用 Python 开发，拥有活跃的社区贡献和可扩展的插件架构。

3. **适用场景**
*   自动化长周期研究任务，如信息搜集、整理及报告生成。
*   构建个性化的 AI 助手，用于日程管理、邮件处理或日常信息查询。
*   开发者利用其作为基础框架，快速搭建和测试新的 AI 代理应用原型。

4. **技术亮点**
*   实现了从单一指令到多步自主执行的代理逻辑闭环。
*   高度模块化设计，支持灵活切换后端 LLM 提供商。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185403 | 🍴 46122 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164906 | 🍴 21347 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164010 | 🍴 30384 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156835 | 🍴 46164 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151247 | 🍴 9446 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147916 | 🍴 23295 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

