# GitHub AI项目每日发现报告
日期: 2026-07-09

## 新发布的AI项目

### lapian-notes
- ### 1. 中文简介
Lapian-notes 是一款利用 AI 辅助进行电影“拉片”分析的开源工具，旨在将影视内容转化为结构化的专业笔记。它集成了本地视频抽帧、剧情时间轴可视化及多维度数据分析功能，帮助创作者深度拆解影片结构与情绪脉络。

### 2. 核心功能
*   **AI 辅助拉片**：结合人工智能技术自动化分析影片内容，生成结构化笔记。
*   **本地抽帧处理**：支持在本地环境下对视频进行高效帧提取，保护隐私并提升速度。
*   **剧情泳道时间轴**：提供可视化的泳道图以梳理复杂的情节线索和时间线。
*   **结构与情绪分析**：内置结构树和情绪曲线功能，直观展示段落拆解与情感起伏。

### 3. 适用场景
*   **影视编剧创作**：通过拆解经典影片的结构和节奏，辅助剧本大纲编写与情节优化。
*   **电影学术研究**：深入分析特定镜头语言、叙事结构或导演风格，为论文提供数据支持。
*   **影视教学培训**：作为教学工具，帮助学生直观理解拉片方法和视听语言逻辑。

### 4. 技术亮点
*   **全栈 TypeScript 开发**：基于 React + Vite 构建，代码类型安全且开发体验流畅。
*   **私有化部署能力**：强调本地抽帧处理，适合对数据隐私有严格要求的专业用户。
*   **多模态数据可视化**：将视频帧、文本分析与图表（如情绪曲线）紧密结合，实现多维度的直观呈现。
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 137 | 🍴 20 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### ditto
- 1. **中文简介**
该项目旨在挖掘用户在 Claude Code 和 Codex 中的使用日志，并将其转化为本地化的 `you.md` 智能体配置文件。通过这种方式，它能够将用户的编程习惯和个人偏好沉淀为可复用的代理记忆。

2. **核心功能**
- 自动解析并提取 Claude Code 和 Codex 的历史交互日志数据。
- 将提取的信息整合生成结构化的 `you.md` 本地个人配置文件。
- 实现基于个人历史行为的 AI 代理个性化与上下文工程优化。
- 支持本地优先的数据处理，确保用户隐私与数据控制权。

3. **适用场景**
- 希望让 AI 编码助手更精准理解个人代码风格和偏好的开发者。
- 需要跨不同 AI 工具（如 Claude 和 Codex）统一个人工作流的工程师。
- 重视数据本地化存储，不愿将敏感代码习惯上传至云端的隐私倡导者。

4. **技术亮点**
- 巧妙利用“上下文工程”概念，将非结构化的对话日志转化为结构化的 Agent 记忆。
- 采用 Python 开发，轻量级且易于集成到现有的本地 AI 辅助工作流中。
- 链接: https://github.com/ohad6k/ditto
- ⭐ 67 | 🍴 9 | 语言: Python
- 标签: agent-memory, agent-skills, ai, ai-agents, ai-coding

### Homekit
- 1. **中文简介**
Homekit 为 AI 智能体提供了对 Apple Home 生态系统的直接物理控制权，支持通过单一开放接口操作灯光、门锁及读取传感器数据。它旨在让开发者能够轻松集成自动化功能，实现智能家居设备的精准管理。

2. **核心功能**
- 赋予 AI 智能体控制苹果家庭设备（如开关灯、锁门）的直接物理权限。
- 提供统一的开放接口，简化与 Apple HomeKit 硬件的交互流程。
- 支持读取各类传感器数据，为智能决策提供实时信息反馈。
- 兼容多种主流 AI 工具和模型上下文协议（MCP），便于集成。

3. **适用场景**
- 开发基于 Claude 或 OpenClaw 等模型的个性化智能家居自动化脚本。
- 在 Cursor 等 AI 辅助开发环境中快速构建连接 Apple Home 的智能代理。
- 通过命令行界面（CLI）实现对家庭环境的远程监控和即时控制。
- 利用 MCP 协议将 Apple Home 数据接入更广泛的 AI 应用生态中。

4. **技术亮点**
- 采用 TypeScript 编写，确保代码类型安全且易于维护。
- 原生支持 Model Context Protocol (MCP)，无缝对接现代 AI 框架。
- 轻量级设计，专注于为 macOS 环境下的 Node.js 应用提供高效接口。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### fintech-advisor
- ### 1. **中文简介**
fintech-advisor 是一个基于人工智能的金融科技财务顾问项目，旨在为用户提供个性化的投资组合管理建议。该项目利用 AI 技术分析市场数据与用户资产状况，帮助用户优化资产配置并制定更科学的理财策略。

### 2. **核心功能**
- **智能投资组合分析**：AI 自动评估用户当前持仓的风险与收益特征。
- **个性化财务建议**：根据用户风险偏好和市场趋势生成定制化的调仓建议。
- **多维度数据洞察**：整合金融指标与市场动态，为决策提供数据支持。
- **自动化顾问服务**：模拟专业理财师角色，提供 7x24 小时的即时咨询。

### 3. **适用场景**
- **个人投资者**：希望获得专业级资产配置建议但缺乏金融背景的用户。
- **初创金融科技团队**：需要快速集成 AI 驱动的投资顾问功能以构建 MVP（最小可行性产品）。
- **财富管理应用**：旨在通过智能化手段提升用户体验和留存率的金融类 App。
- **学习研究**：对“AI+金融科技”交叉领域感兴趣的技术人员或学生进行案例参考。

### 4. **技术亮点**
- **TypeScript 开发**：采用 TypeScript 编写，确保代码类型安全、可维护性高及开发效率。
- **轻量化 AI 集成**：项目结构紧凑，便于开发者快速上手并集成现有的大语言模型或金融算法库。
- 链接: https://github.com/KORAYTEACHER/fintech-advisor
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai, ai-advisor, ai-financial, ai-fintech, fintech

### FinTech-Solution
- 1. **中文简介**
该项目是一个专为中小企业设计的金融科技AI解决方案，旨在自动化计算各类金融数值。它利用人工智能技术简化复杂的财务数据处理流程。

2. **核心功能**
*   集成AI算法以精准计算中小企业的各项金融指标。
*   提供针对中小企业特定需求的定制化金融价值评估。
*   基于TypeScript构建，确保代码的高效性与可维护性。
*   封装为完整的解决方案，降低企业接入金融科技工具的门槛。

3. **适用场景**
*   中小企业需要快速生成财务报表或现金流预测时。
*   初创公司希望低成本集成智能金融分析功能。
*   金融机构为中小企业客户提供自动化估值服务时。

4. **技术亮点**
*   采用TypeScript开发，具备良好的类型安全和生态兼容性。
*   结合AI技术提升金融数据处理的智能化水平。
- 链接: https://github.com/imchine/FinTech-Solution
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-solution, fintech, fintech-ai, fintech-solution, solution

### fintech-dashboard
- 描述: fintech dashboard for personal finance management which track income and expenses, leverage AI-powered analytics, manage budgets and financial goals, enjoy a dark theme
- 链接: https://github.com/Elias569/fintech-dashboard
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-dashboard, dashboard, fintech, fintech-ai, fintech-dashboard

### fintech-forge
- 描述: fintech forge of AI-powered financial tools and insights to secure authentication and dashboards to empowers developers, analysts, and students to build and extend finance-focused 
- 链接: https://github.com/KORAYTEACHER/fintech-forge
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-financial-tool, ai-fintech-tool, ai-tool, financial-app, fintech

### openclaw-voice-call-realtime
- 描述: Give your AI assistant a phone — OpenClaw plugin for real phone calls via Twilio + OpenAI Realtime, with in-call tools, transcripts, and call screening
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 37 | 🍴 3 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### ai-guru
- 描述: 无描述
- 链接: https://github.com/Dhruvdubey17/ai-guru
- ⭐ 23 | 🍴 8 | 语言: Shell

### ai-market-pulse
- 描述: Turn any watchlist into a daily AI market research report — a quant research cockpit or a zero-code daily report tool.
- 链接: https://github.com/SilentFleetKK/ai-market-pulse
- ⭐ 22 | 🍴 5 | 语言: Python
- 标签: ai, akshare, github-pages, investment-research, llm

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具库，集成了敏感词检测、文本信息抽取、实体识别及大量专业领域词库与语料资源。它不仅提供了基础的文本清洗和标注功能，还涵盖了从传统规则匹配到基于深度学习模型（如 BERT、GPT）的高级 NLP 应用场景，旨在为开发者提供一站式的中英文 NLP 解决方案。

2. **核心功能**
*   **文本清洗与基础分析**：支持中英文敏感词过滤、语言检测、繁简体转换、停用词处理及文本情感值计算。
*   **信息抽取与实体识别**：具备高精度的手机号、身份证、邮箱抽取能力，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取功能。
*   **丰富词库与知识库**：内置中日文人名库、职业/品牌/成语/古诗词等数十个专业领域词库，以及跨语言知识图谱资源。
*   **高级 NLP 任务支持**：提供句子相似度匹配、文本摘要生成、关键词提取、对话系统搭建及语音识别相关语料与工具。
*   **数据增强与预处理**：包含 EDA 数据增强工具、OCR 文字识别辅助、文本规范化及拼写检查等实用模块。

3. **适用场景**
*   **内容安全审核**：用于互联网平台的内容过滤，快速识别敏感词、暴恐信息及虚假谣言。
*   **智能客服与对话系统**：利用其词库、语料及对话模型资源，构建具备语义理解和多轮对话能力的智能机器人。
*   **非结构化数据处理**：从文本中自动抽取关键实体（如人名、地名、机构名）和数值信息，用于构建知识图谱或数据分析。
*   **NLP 研究与教学**：作为学习和复现各类 NLP 算法（如 BERT、GPT、CRF）及获取标准数据集的参考仓库。

4. **技术亮点**
该项目最大的亮点在于其**资源的海量性与综合性**，不仅包含代码实现，更整合了高质量的中文数据集、预训练模型（如 OpenCLaP、UER）及垂直领域知识图谱，极大降低了 NLP 应用的开发门槛和数据准备成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81710 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
该项目是一个收录了500个AI项目的精选资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，并附带完整代码实现。它旨在为开发者提供从基础概念到高级应用的全方位学习路径与实践案例。

### 2. 核心功能
*   **海量项目集合**：包含500个经过筛选的AI相关项目，覆盖主流技术栈。
*   **多领域覆盖**：内容横跨机器学习、深度学习、计算机视觉及NLP等核心AI分支。
*   **代码实战支持**：所有项目均提供源代码，便于用户直接运行、学习和修改。
*   **分类标签体系**：通过清晰的标签（如awesome、data-science）帮助用户快速定位感兴趣的方向。

### 3. 适用场景
*   **AI初学者入门**：适合希望系统学习AI基础知识并动手实践的新手，通过仿写代码快速上手。
*   **项目灵感获取**：开发者可从中寻找创意，作为毕业设计、个人作品集或开源贡献的参考起点。
*   **技术栈拓展**：已有经验的工程师可利用该项目探索陌生的AI子领域（如从ML转向CV）。

### 4. 技术亮点
*   **“Awesome”精选性质**：项目列表通常由社区维护，去除了低质量内容，保证了资源的实用性和前沿性。
*   **Python生态集中**：虽然标签显示“None”，但鉴于AI领域的特性及标签中的Python暗示，项目高度依赖Python及其丰富的AI库（如TensorFlow, PyTorch, Scikit-learn），便于复用现有工具链。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35282 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款开源的可视化工具，专为神经网络、深度学习及机器学习模型设计。它支持多种主流框架生成的模型文件，帮助用户直观地查看和理解模型结构。该工具通过清晰的图形界面展示数据流向和层级关系，极大地降低了模型调试与分析的难度。

### 2. 核心功能
*   **多格式广泛支持**：兼容 Keras、TensorFlow、PyTorch、ONNX、CoreML、SafeTensors 等数十种模型格式。
*   **交互式可视化**：提供直观的图形化界面，清晰展示神经网络的层级结构和数据流动路径。
*   **跨平台兼容性**：基于 JavaScript 开发，支持在 Web 浏览器、桌面端（Windows/macOS/Linux）及移动端运行。
*   **模型细节审查**：允许用户展开查看每一层的详细参数、权重形状及操作类型，便于深入分析。
*   **轻量级与便捷性**：无需安装庞大的机器学习环境，即可快速加载并渲染复杂的大型模型文件。

### 3. 适用场景
*   **模型调试与验证**：开发者在训练后检查模型架构是否正确，确认层顺序和数据维度是否符合预期。
*   **学术交流与演示**：研究人员或工程师向非技术背景的团队成员展示模型结构，用于汇报或教学目的。
*   **异构框架迁移**：在将模型从一种框架（如 PyTorch）转换到另一种框架（如 ONNX 或 TensorFlow Lite）时，验证转换后的结构一致性。
*   **部署前审查**：在将模型部署到边缘设备或移动应用前，快速审查模型复杂度及支持的算子情况。

### 4. 技术亮点
*   **技术栈优势**：采用 JavaScript/TypeScript 构建，实现了“一次编写，多处运行”，极大提升了工具的便携性和可访问性。
*   **社区驱动生态**：作为 GitHub 上星标超过 3.3 万的热门项目，拥有活跃的社区支持和持续更新的格式适配能力。
*   **零依赖体验**：用户无需配置 Python 环境或安装深度学习库，仅需一个浏览器或可执行文件即可使用，降低了使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33204 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 项目名称：ONNX

#### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个旨在实现机器学习模型跨平台互操作性的开放标准。它允许开发者轻松地在不同的深度学习框架和工具之间迁移模型，打破生态壁垒，提升模型部署的灵活性。

#### 2. 核心功能
*   **框架互操作性**：支持在不同深度学习框架（如 PyTorch、TensorFlow、Scikit-learn）间无缝转换模型格式。
*   **统一表示层**：定义了一套通用的算子和张量规范，确保模型结构在不同运行时中保持一致。
*   **跨平台部署优化**：配合 ONNX Runtime 等推理引擎，实现高效的多硬件加速（CPU、GPU、NPU 等）。
*   **模型验证与调试**：提供工具检查模型定义的合法性及算子兼容性，降低集成错误率。

#### 3. 适用场景
*   **生产环境部署**：将从训练框架（如 PyTorch）导出的模型转换为 ONNX 格式，以便在高性能推理引擎中进行低延迟服务部署。
*   **异构硬件适配**：在边缘设备或特定加速器（如 Intel OpenVINO、ARM NN）上运行模型，利用 ONNX 作为中间表示层简化适配流程。
*   **混合框架协作**：在项目中同时使用多种框架（例如用 TensorFlow 训练，用 Scikit-learn 处理预处理），通过 ONNX 统一模型交换接口。

#### 4. 技术亮点
*   **开源社区驱动**：由微软、Facebook 等科技巨头共同维护，拥有庞大的开源社区支持和广泛的行业认可度。
*   **高性能推理引擎**：配套的 ONNX Runtime 提供了高度优化的执行计划，显著提升推理速度并降低资源消耗。
- 链接: https://github.com/onnx/onnx
- ⭐ 21121 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
该项目是一本关于机器学习工程领域的开源书籍，旨在系统性地指导开发者在大规模模型训练与推理中的最佳实践。内容涵盖从底层硬件资源管理到上层模型部署的全链路工程知识，是连接理论与实践的重要参考指南。

### 2. 核心功能
*   **全栈工程指导**：提供从数据预处理、分布式训练策略到模型优化和部署的完整工作流解析。
*   **硬件资源管理**：深入讲解如何利用 GPU、网络存储及 SLURM 集群调度器高效管理计算资源。
*   **大规模模型优化**：针对 LLM（大语言模型）提供具体的调试技巧、可扩展性方案及推理加速策略。
*   **PyTorch 生态集成**：结合 Hugging Face Transformers 等主流库，展示 PyTorch 在工业级场景下的实际应用模式。

### 3. 适用场景
*   **LLM 训练基础设施搭建**：团队在构建基于 PyTorch 的大规模分布式训练集群时参考资源调度与网络配置。
*   **模型推理服务部署**：开发者需要优化大模型的推理延迟并降低显存占用，以实现高并发生产环境部署。
*   **MLOps 流程标准化**：工程团队希望建立从实验调试到模型上线的标准化机器学习操作规范。

### 4. 技术亮点
*   **实战导向**：不仅理论丰富，更侧重于解决真实世界中的可扩展性、调试和性能瓶颈问题。
*   **前沿技术覆盖**：紧密跟随 AI 领域最新趋势，重点涵盖 Large Language Models (LLM) 和 Transformer 架构的工程化落地。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18300 | 🍴 1161 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13119 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11565 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
该项目是一个收录了500个AI项目的精选资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，并附带完整代码实现。它旨在为开发者提供从基础概念到高级应用的全方位学习路径与实践案例。

### 2. 核心功能
*   **海量项目集合**：包含500个经过筛选的AI相关项目，覆盖主流技术栈。
*   **多领域覆盖**：内容横跨机器学习、深度学习、计算机视觉及NLP等核心AI分支。
*   **代码实战支持**：所有项目均提供源代码，便于用户直接运行、学习和修改。
*   **分类标签体系**：通过清晰的标签（如awesome、data-science）帮助用户快速定位感兴趣的方向。

### 3. 适用场景
*   **AI初学者入门**：适合希望系统学习AI基础知识并动手实践的新手，通过仿写代码快速上手。
*   **项目灵感获取**：开发者可从中寻找创意，作为毕业设计、个人作品集或开源贡献的参考起点。
*   **技术栈拓展**：已有经验的工程师可利用该项目探索陌生的AI子领域（如从ML转向CV）。

### 4. 技术亮点
*   **“Awesome”精选性质**：项目列表通常由社区维护，去除了低质量内容，保证了资源的实用性和前沿性。
*   **Python生态集中**：虽然标签显示“None”，但鉴于AI领域的特性及标签中的Python暗示，项目高度依赖Python及其丰富的AI库（如TensorFlow, PyTorch, Scikit-learn），便于复用现有工具链。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35282 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款开源的可视化工具，专为神经网络、深度学习及机器学习模型设计。它支持多种主流框架生成的模型文件，帮助用户直观地查看和理解模型结构。该工具通过清晰的图形界面展示数据流向和层级关系，极大地降低了模型调试与分析的难度。

### 2. 核心功能
*   **多格式广泛支持**：兼容 Keras、TensorFlow、PyTorch、ONNX、CoreML、SafeTensors 等数十种模型格式。
*   **交互式可视化**：提供直观的图形化界面，清晰展示神经网络的层级结构和数据流动路径。
*   **跨平台兼容性**：基于 JavaScript 开发，支持在 Web 浏览器、桌面端（Windows/macOS/Linux）及移动端运行。
*   **模型细节审查**：允许用户展开查看每一层的详细参数、权重形状及操作类型，便于深入分析。
*   **轻量级与便捷性**：无需安装庞大的机器学习环境，即可快速加载并渲染复杂的大型模型文件。

### 3. 适用场景
*   **模型调试与验证**：开发者在训练后检查模型架构是否正确，确认层顺序和数据维度是否符合预期。
*   **学术交流与演示**：研究人员或工程师向非技术背景的团队成员展示模型结构，用于汇报或教学目的。
*   **异构框架迁移**：在将模型从一种框架（如 PyTorch）转换到另一种框架（如 ONNX 或 TensorFlow Lite）时，验证转换后的结构一致性。
*   **部署前审查**：在将模型部署到边缘设备或移动应用前，快速审查模型复杂度及支持的算子情况。

### 4. 技术亮点
*   **技术栈优势**：采用 JavaScript/TypeScript 构建，实现了“一次编写，多处运行”，极大提升了工具的便携性和可访问性。
*   **社区驱动生态**：作为 GitHub 上星标超过 3.3 万的热门项目，拥有活跃的社区支持和持续更新的格式适配能力。
*   **零依赖体验**：用户无需配置 Python 环境或安装深度学习库，仅需一个浏览器或可执行文件即可使用，降低了使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33204 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必不可少的基础速查手册。内容涵盖从理论概念到代码实现的多种关键知识点的快速参考指南。旨在帮助研究者高效回顾和掌握核心工具库及算法细节。

2. **核心功能**
*   提供机器学习和深度学习领域的核心概念速查表。
*   包含主流框架（如Keras、PyTorch等）的代码示例参考。
*   汇总了常用数学库（NumPy、SciPy、Matplotlib）的操作技巧。
*   整理了深度学习模型架构与训练调优的关键参数说明。

3. **适用场景**
*   研究人员在开发过程中快速回忆API用法或数学公式。
*   初学者入门时对照学习机器学习基础理论与代码实现。
*   算法工程师调试模型时检查超参数设置或数据预处理步骤。
*   面试准备时梳理AI领域核心知识点和技术栈。

4. **技术亮点**
*   高度整合了Numpy、Scipy和Matplotlib等科学计算库的实用技巧。
*   针对Keras等高级深度学习接口提供了简洁的代码模板。
*   以“速查”形式呈现，极大降低了查阅文档的时间成本。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
这是一个提供全面人工智能学习路线图的开源项目，包含近200个实战案例并免费提供配套教材，旨在帮助零基础用户入门并提升就业竞争力。内容涵盖Python、数学基础以及机器学习、深度学习、NLP和CV等热门技术领域。

2. **核心功能**
*   提供结构化的AI学习路径，涵盖从基础到进阶的系统性知识体系。
*   收录近200个实战案例与项目代码，强化动手实践能力。
*   免费提供配套学习资料和教材，降低学习门槛。
*   覆盖主流AI框架与技术栈，如PyTorch、TensorFlow、Keras及Scikit-learn生态工具。
*   针对就业导向设计，注重算法应用与数据处理技能的培养。

3. **适用场景**
*   希望从零开始系统学习人工智能技术的初学者。
*   需要大量实战项目参考以提升编程能力和解决实际问题能力的开发者。
*   准备进入AI行业工作，寻求简历项目和面试素材的求职者。
*   希望梳理Python、数据分析和深度学习知识体系的技术人员。

4. **技术亮点**
*   内容整合度高，集中了算法、数学、数据分析及多种主流深度学习框架的资源。
*   强调实战驱动，通过丰富的案例库连接理论与实际应用。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13119 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9121 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8921 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6233 | 🍴 738 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具库，集成了敏感词检测、信息抽取（如手机号、身份证、邮箱）、实体识别及丰富的行业词库资源。它提供了从基础文本处理到高级深度学习模型（如 BERT）应用的广泛功能，旨在简化 NLP 开发流程。

2. **核心功能**
*   **文本清洗与校验**：支持中英文敏感词检测、繁简体转换、停用词过滤及文本纠错。
*   **信息抽取与识别**：精准抽取手机号、身份证、邮箱、人名等实体，并支持姓名性别推断及语言检测。
*   **丰富词库与资源**：内置中日文人名库、成语、诗词、行业专业术语（医疗、法律、汽车等）及情感值数据。
*   **NLP 模型与工具集成**：涵盖分词、词性标注、依存句法分析，并整合了 BERT、GPT-2 等预训练模型及语音识别相关资源。
*   **知识图谱与问答支持**：提供知识图谱构建工具、问答系统数据集及实体链接、关系抽取等高级 NLP 任务支持。

3. **适用场景**
*   **内容安全审核**：用于社交媒体或论坛平台，自动识别和过滤敏感词、暴恐词及谣言信息。
*   **智能客服与聊天机器人**：利用其对话语料、意图识别及生成能力，快速搭建具备上下文理解的智能客服系统。
*   **金融/医疗垂直领域分析**：借助专用词库和实体抽取工具，从大量非结构化文档中提取关键医疗或金融实体进行分析。
*   **文本数据预处理**：为下游 NLP 任务提供标准化的分词、去噪、格式化及特征工程支持。

4. **技术亮点**
*   **功能高度集成**：将传统 NLP 技巧与现代深度学习资源（如 Transformer 系列）统一在一个项目中，降低集成成本。
*   **领域覆盖广泛**：不仅包含通用 NLP 功能，还深入医疗、法律、金融等垂直领域的专有知识和数据集。
*   **实用工具链完整**：从底层的 OCR、语音对齐到上层的问答、摘要生成，提供了端到端的解决方案参考。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81710 | 🍴 15253 | 语言: Python

### LlamaFactory
- ### LlamaFactory 项目分析报告

1. **中文简介**
   LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目已发表于 ACL 2024，旨在简化微调流程并提供卓越的性能与易用性。

2. **核心功能**
   *   **多模态支持**：无缝兼容 100+ 种 LLM 和 VLM，涵盖 Llama、Qwen、Gemma 等主流架构。
   *   **高效微调算法**：内置 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法。
   *   **强化学习对齐**：支持 RLHF、DPO、KTO 等前沿对齐算法，优化模型输出质量。
   *   **量化训练部署**：提供完整的量化训练（如 GPTQ、AWQ）及推理加速功能。
   *   **一体化工作流**：集数据预处理、模型训练、评估与导出于一体，降低使用门槛。

3. **适用场景**
   *   **垂直领域模型定制**：快速将开源大模型微调为医疗、法律或金融等领域的专用助手。
   *   **低资源环境优化**：在显存受限的硬件上，通过 QLoRA 等技术实现大模型的高效训练。
   *   **多模态应用开发**：构建具备图像理解能力的智能体（Agent），处理图文混合任务。
   *   **学术研究与实验**：复现 ACL 2024 等顶级会议的微调方法，进行算法对比验证。

4. **技术亮点**
   *   **极致性能与效率**：经过高度优化的底层代码，显著提升训练速度并降低显存占用。
   *   **前沿算法集成**：率先整合最新对齐技术（如 DPO、RLOO）及 MoE（混合专家）模型支持。
   *   **开箱即用的体验**：提供极简的配置方式和丰富的示例，无需复杂的环境依赖即可上手。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73112 | 🍴 8933 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目汇集了来自Anthropic、OpenAI、Google及xAI等主流厂商最新大模型的系统提示词（System Prompts），涵盖Claude、GPT、Gemini等多个系列。内容定期更新，旨在为开发者、研究人员及安全专家提供全面的提示词工程参考与情报支持。

2. **核心功能**
*   收集并整理多平台大模型（如Claude、GPT、Gemini）的底层系统指令。
*   涵盖多种应用场景，包括代码生成、通用对话、专业设计代理及思维链模型。
*   保持高频更新，同步各大厂商最新发布的模型版本提示词配置。
*   以结构化数据形式呈现，便于自动化脚本提取和分析。

3. **适用场景**
*   **提示词工程优化**：通过分析官方提示词结构，学习如何更有效地构建用户指令以提升模型表现。
*   **安全与红队测试**：研究人员利用系统提示词分析模型的边界条件、潜在漏洞及对齐机制。
*   **竞品分析与技术调研**：对比不同厂商模型在系统层级设定的差异，评估其技术路线特点。

4. **技术亮点**
*   **跨厂商全覆盖**：同时整合了Anthropic、OpenAI、Google和xAI等头部科技公司的模型配置。
*   **高时效性**：紧随模型迭代节奏定期更新，确保获取的是最新版本的系统指令。
*   **社区影响力大**：拥有超过5万星标，是提示词工程和LLM安全领域极具价值的开源资源库。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54911 | 🍴 8938 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. 中文简介
这是一个由微软发起的为期12周、包含24课时的全面人工智能入门课程，旨在面向所有人群普及AI知识。该项目通过Jupyter Notebook提供互动式学习体验，覆盖从基础机器学习到深度学习的核心概念。其设计初衷是让初学者能够以系统化、易懂的方式掌握人工智能技能。

### 2. 核心功能
*   **系统化课程体系**：提供结构化的12周学习路径，分24个课时循序渐进地讲解AI基础知识。
*   **交互式代码环境**：基于Jupyter Notebook开发，支持用户直接在浏览器中运行和修改代码进行实践。
*   **涵盖主流AI技术**：内容广泛涉及机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）。
*   **开源免费资源**：完全开放源代码和学习材料，降低大众接触和学习人工智能的门槛。
*   **微软教育支持**：作为“Microsoft for Beginners”系列的一部分，提供高质量且权威的技术指导。

### 3. 适用场景
*   **高校或培训机构教学**：教师可作为标准课程大纲，用于人工智能导论或相关专业的入门教学。
*   **自学者系统入门**：零基础或对AI感兴趣的个人用户，希望通过结构化课程快速建立AI知识体系。
*   **企业内部培训**：科技公司或非科技行业的企业，用于对员工进行人工智能基础概念的普及和技能提升。
*   **编程实践练习**：希望结合理论代码（如CNN、RNN实现）进行动手操作的初学者，通过Notebook即时验证学习效果。

### 4. 技术亮点
*   **全栈AI覆盖**：不仅限于传统机器学习，还深入讲解了卷积神经网络（CNN）、循环神经网络（RNN）和生成对抗网络（GAN）等前沿深度学习技术。
*   **多领域融合**：同时涵盖计算机视觉（Computer Vision）和自然语言处理（NLP）两大核心应用领域，提供全面的AI视角。
*   **低门槛高互动**：利用Jupyter Notebook的即时反馈特性，将复杂的数学和算法概念转化为可执行的代码片段，极大提升了学习效率和理解度。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51958 | 🍴 10505 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）。它集成了自然语言处理工具（NLTK）及多种经典算法，旨在为用户提供从理论到实践的系统化学习路径。

2. **核心功能**
*   实现多种经典机器学习算法（如 SVM、K-Means、Apriori 等）的代码示例与原理讲解。
*   提供基于 PyTorch 和 TensorFlow 2 的深度学习模型实战教程。
*   包含自然语言处理（NLP）相关的 NLTK 工具应用及文本挖掘案例。
*   整合推荐系统、回归分析及降维技术（PCA、SVD）等实用数据处理技能。

3. **适用场景**
*   机器学习初学者系统梳理算法原理与代码实现的学习参考。
*   数据科学家进行特定算法（如 FP-Growth、AdaBoost）复现或对比实验的工具箱。
*   高校学生或研究人员用于线性代数在 AI 中应用的辅助教材。

4. **技术亮点**
*   覆盖面极广，同时涉及传统机器学习（scikit-learn）与现代深度学习（PyTorch/TF2）两大体系。
*   不仅关注算法模型，还强调数学基础（线性代数）与自然语言处理等细分领域的结合。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42366 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37733 | 🍴 6292 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35282 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33727 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28433 | 🍴 3462 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25856 | 🍴 2907 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI相关代码项目的精选合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。它为开发者提供了丰富的实战案例和源代码，是学习人工智能技术的优质资源库。

2. **核心功能**
- 汇集500个完整的AI项目代码，覆盖主流AI子领域。
- 提供从基础机器学习到前沿深度学习的多样化实例。
- 整合计算机视觉与自然语言处理的实际应用场景。
- 作为“Awesome”系列列表，经过筛选保证项目质量与实用性。

3. **适用场景**
- 初学者系统学习机器学习与深度学习基础概念及实现。
- 工程师寻找计算机视觉或NLP任务的参考代码模板。
- 研究人员快速验证特定AI算法在真实数据上的效果。

4. **技术亮点**
- 覆盖面极广，囊括了AI领域的多个关键分支。
- 以代码为导向，强调动手实践而非纯理论阐述。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35282 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款利用人工智能自动化浏览器工作流的工具，能够模拟人类操作以完成复杂的网页任务。它主要基于 Python 开发，结合了大型语言模型（LLM）与计算机视觉技术，旨在替代传统的 RPA 方案，实现更智能、更灵活的浏览器自动化。

**2. 核心功能**
*   利用 AI 理解网页结构并自动生成执行步骤，无需预先编写繁琐的选择器。
*   支持通过 API 集成，方便开发者将其嵌入到现有的业务自动化流程中。
*   具备强大的计算机视觉能力，能够识别页面元素并处理动态变化的 UI 界面。
*   兼容 Playwright 等主流浏览器自动化工具，确保操作的高效性与稳定性。

**3. 适用场景**
*   **企业级 RPA 替代**：用于自动化处理需要登录、填写表单或数据抓取的企业内部系统操作。
*   **跨平台数据集成**：在缺乏官方 API 的情况下，自动从不同网站提取数据并整合到统一系统中。
*   **测试与 QA 自动化**：模拟真实用户行为进行端到端测试，提高 Web 应用测试的覆盖率与效率。

**4. 技术亮点**
*   **AI 驱动决策**：不同于传统基于固定规则的脚本，Skyvern 能根据实时页面状态动态调整操作策略。
*   **多模态能力**：结合 LLM 的自然语言理解与视觉识别，使其能“看懂”并“操作”复杂的现代网页应用。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22164 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的标注，并提供开源、云端和企业级产品。它集成了 AI 辅助标注、质量保证、团队协作及开发者 API 等功能，旨在提升计算机视觉数据的生产效率。

2. **核心功能**
*   支持图像、视频和 3D 数据的多模态标注与 AI 辅助打标。
*   提供开源本地部署、云版本及企业版等多种产品形态。
*   内置质量保证机制、团队协作工具及数据分析功能。
*   开放开发者 API，便于集成到现有工作流中。

3. **适用场景**
*   计算机视觉算法研发中的大规模数据集构建与标注。
*   需要多人协作进行复杂视频或 3D 对象检测标注的团队。
*   对数据安全有要求，需私有化部署的企业级 AI 训练项目。

4. **技术亮点**
*   结合深度学习模型实现自动化半标注，显著降低人工成本。
*   兼容 PyTorch 和 TensorFlow 等主流框架的数据格式需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16248 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- **1. 中文简介**
该项目旨在为计算机视觉提供先进的AI可解释性解决方案，支持卷积神经网络（CNN）和视觉Transformer等多种架构。它广泛适用于图像分类、目标检测、语义分割及图像相似度计算等任务，帮助用户深入理解模型决策依据。

**2. 核心功能**
*   支持多种主流深度学习模型架构，包括CNN和Vision Transformers。
*   覆盖广泛的应用场景，如图像分类、目标检测、语义分割和图像检索。
*   实现多种可视化技术，包括Grad-CAM、Score-CAM及类激活映射（CAM）。
*   提供直观的注意力图生成工具，增强模型输出的可解释性和透明度。

**3. 适用场景**
*   **医疗影像分析**：定位病灶区域，辅助医生验证AI诊断结果的合理性。
*   **自动驾驶系统调试**：可视化车辆识别关键特征，提升感知模块的安全性与可信度。
*   **学术研究**：深入探讨深度学习模型的内部机制，发表关于模型可解释性的高水平论文。
*   **工业质检**：在缺陷检测中突出显示导致分类异常的具体图像区域。

**4. 技术亮点**
*   高度兼容PyTorch框架，集成多种前沿的可解释性算法（如Grad-CAM++、Score-CAM）。
*   模块化设计良好，易于扩展至自定义模型结构和新的可视化方法。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12911 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理算法，旨在简化深度学习中的视觉任务开发。该库填补了传统图像处理与现代深度学习框架之间的空白，支持在 GPU 上高效运行。

### 2. 核心功能
*   **可微分图像处理**：提供大量基于梯度的图像变换操作，可直接集成到神经网络中。
*   **几何视觉算法**：包含相机标定、姿态估计和三维重建等传统计算机视觉模块。
*   **PyTorch 原生集成**：作为 PyTorch 的一等公民，无缝支持张量操作和自动微分。
*   **模块化设计**：将传统 CV 算法转化为可训练的层，便于端到端的模型优化。

### 3. 适用场景
*   **机器人导航**：用于实时处理传感器数据，进行定位和地图构建（SLAM）。
*   **自动驾驶感知**：在深度学习中整合几何约束，提升车辆环境理解的准确性。
*   **工业缺陷检测**：利用可微分的图像增强和特征提取算法进行自动化质检。
*   **学术研究**：探索几何视觉与深度学习结合的新算法和模型架构。

### 4. 技术亮点
*   **全可微流水线**：首次实现了完整的传统计算机视觉算法的可微分版本，允许通过反向传播优化视觉参数。
*   **高性能 GPU 加速**：所有操作均针对 NVIDIA GPU 优化，显著提升了大规模图像处理的效率。
*   **开源社区驱动**：拥有活跃的开发者社区，持续贡献新的视觉算法和优化方案。
- 链接: https://github.com/kornia/kornia
- ⭐ 11272 | 🍴 1198 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 877 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3275 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2623 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2423 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，旨在让用户以“龙虾”般的独特方式掌控自己的数据。它强调私有化和跨平台兼容性，为用户提供完全自主的 AI 体验。

### 2. 核心功能
*   **全平台兼容**：支持在任意操作系统和平台上运行，实现无缝接入。
*   **数据所有权**：强调“Own Your Data”，确保用户完全掌控个人数据和隐私。
*   **个性化助手**：作为专属的个人 AI 助理，可根据用户需求进行定制。
*   **开源生态**：基于 TypeScript 构建，社区活跃，标签体现其开源和螃蟹/龙虾主题特色。
*   **本地化部署**：支持私有化部署，保障数据安全和独立性。

### 3. 适用场景
*   **隐私敏感用户**：需要完全控制个人数据、避免云端泄露的技术爱好者或企业用户。
*   **跨平台开发者**：希望在 Windows、macOS 或 Linux 等不同环境中统一使用 AI 助手的开发者。
*   **独立研究者**：希望搭建个性化、可定制且无需依赖大型科技巨头服务的 AI 实验环境。
*   **数据主权倡导者**：重视数字资产和个人信息所有权的个人用户。

### 4. 技术亮点
*   **TypeScript 驱动**：采用 TypeScript 开发，提供类型安全和高可维护性。
*   **高度可定制**：支持用户根据自身需求调整助手行为和数据处理逻辑。
*   **去中心化架构**：强调本地运行和数据私有化，减少对第三方服务的依赖。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382321 | 🍴 80222 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一套经过实战验证的智能体技能框架与软件开发方法论。它旨在通过结构化的方式赋能开发者，将复杂的软件构建过程转化为可管理、可执行的智能体任务流。该项目致力于解决 AI 辅助编程中逻辑松散的问题，提供一套行之有效的工程化标准。

2. **核心功能**
*   提供模块化的“智能体技能”库，支持按需组合以应对不同开发任务。
*   引入“子代理驱动开发”模式，将大型复杂问题拆解为可由独立智能体执行的具体步骤。
*   整合头脑风暴与编码阶段，形成从创意构思到代码实现的完整 SDLC（软件开发生命周期）闭环。
*   基于 ORBA 方法论优化提示词工程，确保 AI 输出的一致性与高质量。
*   作为 Shell 脚本工具集，提供即插即用的自动化工作流支持。

3. **适用场景**
*   需要利用 AI 大幅加速传统软件开发流程的团队或个人开发者。
*   希望系统化管理 AI 智能体行为，避免“幻觉”导致代码混乱的高级用户。
*   进行复杂系统架构设计时，需要分步骤、分角色由不同子代理协同工作的场景。
*   探索新型软件工程范式，试图将人类创造力与 AI 执行力深度结合的早期采用者。

4. **技术亮点**
*   创新性地将“技能框架”概念引入 AI 编程，强调能力的复用与标准化。
*   结合 Subagent-driven Development (SDD) 理念，实现了比单一 Prompt 更强大的分布式问题解决能力。
- 链接: https://github.com/obra/superpowers
- ⭐ 250654 | 🍴 22237 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的 GitHub 项目信息（*hermes-agent*），以下是详细的中文分析：

1. **中文简介**
   Hermes Agent 是一款具备自我进化能力的智能代理工具，旨在随着用户的交互与使用习惯不断成长和优化。它集成了多种主流大语言模型（如 Claude、ChatGPT 等），致力于提供个性化且持续进化的辅助体验。

2. **核心功能**
   - **多模型集成**：支持接入 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 等多个主流 LLM 后端。
   - **自适应成长**：具备记忆与学习能力，能根据用户反馈和历史交互不断调整自身行为模式。
   - **代码辅助**：深度整合编程功能，可作为智能编码助手协助开发者完成代码生成与调试。
   - **统一交互接口**：提供标准化的 API 或界面，简化不同 AI 模型之间的切换与管理流程。

3. **适用场景**
   - **高级开发者工作流**：需要跨平台调用不同 AI 模型进行复杂代码生成和架构设计的资深程序员。
   - **个性化 AI 助手定制**：希望拥有一个能记住个人偏好、逐步理解特定业务逻辑的个人数字助理。
   - **AI 应用原型开发**：研究人员或开发者用于快速验证不同 LLM 组合在 Agent 架构下的表现。

4. **技术亮点**
   - **架构灵活性**：通过抽象层解耦前端交互与后端模型，允许无缝替换底层 LLM 提供商。
   - **状态持久化**：设计有专门的状态管理机制，确保代理在长时间运行中能保留上下文并实现“成长”。

*(注：由于提供的信息仅包含元数据而非完整的技术文档，以上分析基于项目名称、标签及常见 AI Agent 架构逻辑推导得出。)*
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 212070 | 🍴 39053 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合。它提供超过 400 种集成方式，允许用户选择自托管或云端部署，灵活满足各类自动化需求。

2. **核心功能**
- 支持自托管或云端部署，保障数据隐私与控制权。
- 拥有超过 400 种预置集成，轻松连接各类应用程序。
- 结合可视化拖拽界面与自定义代码，实现高度灵活的逻辑编排。
- 内置原生 AI 能力，可智能处理数据生成与分析任务。
- 提供 MCP（模型上下文协议）客户端与服务端支持，增强 AI 交互扩展性。

3. **适用场景**
- 企业内部系统间的数据同步与业务流自动化。
- 利用 AI 辅助生成内容或处理非结构化数据的智能工作流。
- 开发者需要结合代码逻辑进行复杂 API 调用和数据处理的项目。
- 对数据安全敏感、要求完全控制基础设施的自托管自动化方案。

4. **技术亮点**
- 基于 TypeScript 开发，类型安全且易于维护扩展。
- 采用公平代码（Fair-code）许可证，平衡开源共享与商业可持续性。
- 深度集成 MCP 协议，紧跟 AI Agent 交互的技术前沿趋势。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195831 | 🍴 59195 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松获取、使用并构建基于 AI 的工具，实现人工智能的普及化愿景。其使命是通过提供强大的工具支持，让用户能够专注于真正重要的核心事务与价值创造。

2. **核心功能**
*   具备自主规划与执行复杂任务的能力，无需人工全程干预。
*   集成多种大型语言模型（如 GPT、Claude、LLaMA），支持灵活切换。
*   提供开放的开发框架，允许用户基于现有工具进行二次开发。
*   拥有活跃的社区生态，持续贡献新的插件和功能模块。

3. **适用场景**
*   自动化执行繁琐的数据收集、整理与分析工作流。
*   作为个人智能助手，自动完成网页浏览、信息检索等日常任务。
*   开发者用于构建和测试复杂的自主代理（Agentic AI）应用原型。

4. **技术亮点**
*   采用多智能体协作架构，能够分解并并行处理子任务以提升效率。
*   支持通过 API 广泛连接外部工具和服务，扩展性强。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185441 | 🍴 46116 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165150 | 🍴 21371 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164062 | 🍴 30403 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156917 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151431 | 🍴 9491 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148307 | 🍴 23370 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

