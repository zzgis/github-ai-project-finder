# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### ocm-mcp-server
- 1. **中文简介**
ocm-mcp-server 是一个 MCP（Model Context Protocol）服务器，允许 AI 代理通过 Open Cluster Management 中心操作多集群 Kubernetes 舰队。它在模型与你的集群之间提供了策略控制、审批流程以及审计功能。

2. **核心功能**
- 通过 Open Cluster Management (OCM) _hub_ 统一管理和操作多个 Kubernetes 集群。
- 支持 MCP 协议，使 AI 代理能够直接调用 K8s 资源进行交互。
- 实施严格的安全策略和审批机制，确保 AI 操作符合企业规范。
- 提供完整的操作审计日志，记录 AI 代理在集群中的所有行为。
- 基于 Python 开发，易于集成到现有的自动化运维体系中。

3. **适用场景**
- 需要 AI 辅助进行大规模多集群 Kubernetes 运维管理的 DevOps 团队。
- 对 AI 操作生产环境有严格合规和安全审计要求的企业级用户。
- 希望利用自然语言或 AI 智能体简化复杂 K8s 部署和策略配置的场景。
- 构建具备自我修复或多集群协调能力的自主化云原生应用平台。

4. **技术亮点**
- 结合了 Open Cluster Management 的多集群管理能力与 MCP 的标准化接口，实现了 AI 与基础设施的高效对接。
- 内置策略引擎和审计机制，解决了 AI 直接操作基础设施时的安全性和可追溯性问题。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 27 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 开发的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行深入分析。它能够提取并结构化视觉描述，生成优化后的 JSON 格式提示词以供生成式 AI 使用。该应用内置 SQLite 数据库便于提示词管理，并支持可调节的 VRAM 硬件配置文件及 ComfyUI 节点集成。

2. **核心功能**
*   利用本地 Ollama LLM 分析文本与图像数据。
*   将视觉描述提取并转化为结构化的 JSON 提示词。
*   内置 SQLite 数据库用于高效管理和编辑提示词。
*   提供可调节的 VRAM 硬件配置文件以适配不同设备性能。
*   兼容 ComfyUI 节点，实现工作流无缝集成。

3. **适用场景**
*   需要本地化部署且注重隐私的数据处理与分析场景。
*   希望将非结构化视觉信息转化为标准化 AI 输入的开发工作流。
*   在 ComfyUI 环境中运行复杂生成任务并需预置优化提示词的用户。
*   硬件资源（VRAM）有限或需动态调整资源分配的本地推理环境。

4. **技术亮点**
*   采用本地 Ollama 模型实现离线、低延迟的智能化提示词工程。
*   通过 SQLite 与 ComfyUI 节点的联动，构建了从分析到生成的闭环工作流。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 27 | 🍴 3 | 语言: Python

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
Verity-JE-Mod 是一款专为 Minecraft Java 版 1.21+ 设计的免费模组，引入了全新怪物、自定义维度、生物群落及世界生成机制。该模组不包含基岩版内容，且新增怪物具备配音、背景故事及多阶段 AI 行为。

2. **核心功能**
- 新增具有配音、背景故事和多阶段 AI 的专属怪物实体。
- 提供全新的自定义维度、生物群落及独特的世界生成算法。
- 支持 Forge 和 Fabric 两大主流模组加载器，兼容 1.21 及以上版本。
- 集成于 All The Mods 等整合包，提供游戏进程引导（Progression Guide）。

3. **适用场景**
- 寻求新挑战与独特怪物体验的 Minecraft Java 版进阶玩家。
- 希望丰富世界观、探索自定义维度与世界生成的休闲玩家。
- 游玩包含 Verity 模组的整合包（如 All The Mods 系列）的用户。
- 喜欢收集背景故事与聆听角色配音的剧情向玩家。

4. **技术亮点**
- 实现了具备多阶段逻辑的高级 AI 系统，增强怪物交互深度。
- 完整集成音频资源（Voice Acting），提升沉浸感。
- 跨模组加载器兼容（Forge/Fabric），扩展了部署灵活性。
- 链接: https://github.com/veritymodminecraft/Verity-JE-Mod-Minecraft
- ⭐ 25 | 🍴 0 | 语言: Java
- 标签: 1-16-5, 1-8, all-the-mods-modpack, allthemods, evernym-verity

### Cursor-Grok-4.5-xAI-free
- 1. **中文简介**
这是一个支持 Windows、macOS 和 Linux 的免费桌面应用，旨在提供类似 Cursor 的 IDE 风格编码集成与 Grok 4.5 模式。用户无需订阅 X Premium 或 Supergrok 即可访问该 AI 工具，且其定价相较于 GPT 和 Claude 具有竞争力。

2. **核心功能**
- 提供跨平台（Win/Mac/Linux）的桌面端 AI 编程助手集成。
- 内置实时网页搜索功能以增强代码生成的准确性。
- 允许免费使用 Grok 4.5 模型，无需付费订阅。
- 具备类似 Composer 的高级代码编辑与自动补全能力。
- 支持通过 SDK 或 API 进行深度集成与自定义开发。

3. **适用场景**
- 希望在不支付 X Premium 费用的情况下体验 xAI Grok 模型的用户。
- 需要结合实时网络搜索来辅助编写复杂代码的软件开发者。
- 寻求 GPT 或 Claude 之外更具性价比的 AI 编程替代方案的团队。
- 希望在本地 IDE 环境中无缝集成最新一代 AI 大模型的技术人员。

4. **技术亮点**
- 基于 TypeScript 构建，确保类型安全和良好的开发体验。
- 实现了 Grok 4.5 在 Cursor 风格 IDE 中的本地化集成与优化。
- 提供了绕过官方付费墙的直接访问路径（基于项目描述）。
- 链接: https://github.com/cursorgrok45free/Cursor-Grok-4.5-xAI-free
- ⭐ 24 | 🍴 0 | 语言: TypeScript
- 标签: ai-powered-applications, composer-2-5, cursor-ai-assistant, cursor-ai-project-rules, cursor-api

### Claude-Code-Sonnet-5-Free-Desktop
- 1. **中文简介**
   这是一个适用于 Windows、macOS 和 Linux 的免费桌面版 AI 编程助手，无需 API 密钥即可使用。其性能基准超越 Sonnet 4.6，成本低于 Opus 5，并在上下文窗口方面优于 GitHub Copilot。用户下载后即刻开始编码体验。

2. **核心功能**
   - 提供跨平台（Win/macOS/Linux）的桌面端 AI 编程辅助。
   - 免除 API 密钥获取门槛，实现免费调用。
   - 具备大容量上下文窗口处理能力，提升代码理解深度。
   - 优化响应速度，在特定基准测试中表现优于竞品。

3. **适用场景**
   - 个人开发者希望零成本获得高性能 AI 编程支持。
   - 需要处理超长代码库或复杂上下文的项目开发。
   - 寻求替代 GitHub Copilot 且对响应速度有较高要求的用户。

4. **技术亮点**
   - 基于 TypeScript 开发，具有良好的跨平台兼容性。
   - 声称在 benchmarks 中击败 Sonnet 4.6 并优于 Fable 5 的速度表现。
- 链接: https://github.com/claudesonnet5free/Claude-Code-Sonnet-5-Free-Desktop
- ⭐ 24 | 🍴 0 | 语言: TypeScript
- 标签: anthropic-, claude-4-opus, claude-5-sonnet, claude-code-desktop, claude-code-prompts

### ai-stock-pool
- 描述: AI industry-chain stock pool with US/A-share mapping, active discovery, policy pressure, and one-click deployment.
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 21 | 🍴 12 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Tok123
- 描述: Tok123 v1.0 · 中文网址目录与任务路线平台，支持 AI 工具导航、行业资源库、内容精选站和专题路线。内置 39 个网址与 GEO 专题，配套可安装的管理员 Skill。
- 链接: https://github.com/yaojingang/Tok123
- ⭐ 18 | 🍴 3 | 语言: TypeScript

### deer-workflow
- 描述: An open-source Dynamic Workflow runtime that keeps orchestration in TypeScript and delegates semantic work to replaceable Agent runtimes.
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 14 | 🍴 4 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### AI_Data_Analatyics_Assistant
- 描述: 无描述
- 链接: https://github.com/Rakshana0205/AI_Data_Analatyics_Assistant
- ⭐ 12 | 🍴 0 | 语言: JavaScript

### ai-cost-history-hub
- 描述: Local AI coding-agent history + API cost analytics (loopback-only).
- 链接: https://github.com/zheyan2517/ai-cost-history-hub
- ⭐ 11 | 🍴 1 | 语言: TypeScript
- 标签: coding-agents, cost-tracking, dashboard, local-first, open-source

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且强大的自然语言处理（NLP）资源仓库，集成了中英文敏感词检测、语言识别、实体抽取（手机号/身份证/邮箱等）及多种词典资源。它提供了从基础文本处理到高级深度学习模型（如BERT）的广泛应用场景支持，并包含大量开源数据集与预训练模型。

**2. 核心功能**
*   **基础文本处理与清洗**：提供敏感词过滤、繁简转换、停用词、反动词表及中英文分词工具。
*   **丰富实体与知识抽取**：支持人名、地名、身份证号、手机号等实体抽取，以及基于依存句法和语义角色的事件三元组抽取。
*   **多领域词典与语料库**：涵盖医学、法律、汽车、财经、古诗词等多个垂直领域的专业词库及大规模中文闲聊/问答数据集。
*   **前沿AI模型与工具集**：整合了BERT、GPT-2等预训练模型应用代码，以及OCR、语音识别（ASR）、知识图谱构建等实用工具。
*   **NLP数据增强与可视化**：提供EDA数据增强工具、情感分析、相似度匹配算法集合及文本可视化工具。

**3. 适用场景**
*   **内容安全审核系统**：利用敏感词库和暴恐词表快速识别和过滤违规内容。
*   **智能客服与聊天机器人开发**：基于海量中文闲聊语料、对话数据集及预训练模型构建多轮对话系统。
*   **垂直行业知识图谱构建**：借助医学、法律、金融等领域的专用词库和数据集，提取实体关系以构建领域知识图谱。
*   **文本挖掘与信息抽取**：从非结构化文本中自动提取关键信息（如联系方式、证件号），用于简历解析或文档自动化处理。

**4. 技术亮点**
*   资源极度丰富，几乎涵盖了NLP领域所需的所有基础词典、数据集及主流深度学习框架的实现代码。
*   紧跟技术前沿，集成了BERT、ALBERT、RoBERTa等最新预训练语言模型在中文场景下的微调与应用示例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82054 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供涵盖多个核心AI领域的实战案例与资源库，内容全面且实用。

2. **核心功能**
- 提供海量AI相关项目源码，覆盖从基础机器学习到前沿深度学习的广泛领域。
- 包含计算机视觉和自然语言处理（NLP）等细分方向的具体实现代码。
- 作为一个“Awesome”列表， curated 精选高质量项目，降低开发者寻找资源的成本。
- 支持Python语言实现，便于快速上手和二次开发。

3. **适用场景**
- AI初学者希望系统性地通过阅读和运行代码来学习不同子领域的基础知识。
- 研究人员或工程师需要参考现有开源项目以加速特定任务（如图像识别或文本分析）的开发。
- 教育者将其作为教学案例库，用于展示机器学习在实际应用中的多种可能性。

4. **技术亮点**
- 项目规模庞大且分类清晰，集成了人工智能主要分支（CV、NLP、DL等）的代表性成果。
- 高星标数（35715+）证明了其在社区中的高认可度和广泛影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35715 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一个用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持广泛的模型格式，帮助用户直观地检查模型结构和参数。该项目旨在提供简洁高效的模型浏览体验。

**2. 核心功能**
- 支持多种主流框架模型（如 TensorFlow, PyTorch, Keras, ONNX 等）的可视化。
- 提供直观的节点图视图，清晰展示网络层之间的连接关系。
- 允许查看和编辑模型的具体参数及权重数据。
- 支持导出模型结构为静态图片或 HTML 文件以便分享。
- 兼容桌面应用与 Web 浏览器两种运行模式。

**3. 适用场景**
- 模型调试：开发者通过可视化结构快速定位网络层错误。
- 文档编写：研究人员使用截图制作论文或技术报告中的模型架构图。
- 模型转换验证：在将模型从一种框架转换为另一种格式后，检查结构一致性。
- 代码学习：初学者通过观察成熟项目的模型结构来理解算法实现。

**4. 技术亮点**
- 极高的兼容性：覆盖 CoreML, TFLite, Safetensors 等数十种格式，是业界标准的轻量级可视化工具。
- 跨平台易用性：无需安装复杂依赖，通过本地应用或在线网页即可直接使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33263 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。通过统一表示形式，开发者可以更轻松地在多种硬件平台和工具链上部署模型。

2. **核心功能**
*   **框架间互操作性**：支持将模型从PyTorch、TensorFlow等主流框架导出为ONNX格式，并导入到其他推理引擎中。
*   **标准化模型表示**：定义了一套通用的算子集和计算图结构，确保模型在不同环境下的语义一致性。
*   **跨平台部署优化**：提供运行时环境，使模型能够在CPU、GPU及专用AI加速器等多种硬件上高效执行。
*   **模型验证与转换工具**：包含用于检查模型有效性、优化计算图以及进行格式转换的开发工具包。
*   **广泛的社区支持**：被主要AI框架如Keras、Scikit-learn等原生支持，形成庞大的生态系统。

3. **适用场景**
*   **生产环境模型部署**：将在训练框架（如PyTorch）中训练的模型转换为ONNX，以便在高性能推理服务器或边缘设备上运行。
*   **混合框架工作流**：在需要结合多个框架优势的场景中（例如用TensorFlow构建部分组件，用PyTorch处理其他部分），利用ONNX作为中间桥梁。
*   **硬件加速适配**：当需要将模型迁移到特定厂商的AI芯片或编译器（如NVIDIA TensorRT、Intel OpenVINO）时，使用ONNX作为通用输入格式。
*   **学术与工业界协作**：研究人员分享模型结构时，使用ONNX格式可确保接收方能无需重写代码即可复现和测试模型。

4. **技术亮点**
*   **开放标准地位**：由微软、Facebook等科技巨头共同推动，已成为事实上的行业通用标准。
*   **动态形状支持**：较新版本增强了对动态输入尺寸的支持，提高了模型在实际应用中的灵活性。
*   **高级算子覆盖**：持续扩展对复杂神经网络层（如Transformer架构中的注意力机制）的原生支持。
- 链接: https://github.com/onnx/onnx
- ⭐ 21214 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一部关于机器学习工程实践的开源指南。它系统性地涵盖了从基础架构到模型训练、推理及调试的全流程关键技术。该项目旨在为从业者提供大规模机器学习系统构建的最佳实践参考。

2. **核心功能**
- 提供大规模分布式训练（如PyTorch、Slurm集群）的配置与优化方案。
- 详解大语言模型（LLM）的高效推理加速及内存管理技术。
- 包含GPU集群网络调优、存储性能优化及系统级故障排查指南。
- 覆盖MLOps全流程，包括代码调试、监控及可扩展性设计模式。

3. **适用场景**
- 需要部署和训练超大规模语言模型（LLM）或深度学习模型的研发团队。
- 面临GPU资源受限、显存溢出或训练效率低下的工程师进行系统调优。
- 构建高可用、高扩展性的机器学习基础设施（MLOps平台）的基础架构师。
- 希望了解工业界最佳实践以解决分布式训练稳定性和网络瓶颈问题的技术人员。

4. **技术亮点**
- 内容紧跟前沿，深度整合了PyTorch、Transformers等主流框架的最新工程实践。
- 强调实战性，不仅讲解理论，更提供针对SLURM、NCCL等底层组件的具体调优参数和建议。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18467 | 🍴 1181 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17336 | 🍴 2117 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11598 | 🍴 910 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10677 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供涵盖多个核心AI领域的实战案例与资源库，内容全面且实用。

2. **核心功能**
- 提供海量AI相关项目源码，覆盖从基础机器学习到前沿深度学习的广泛领域。
- 包含计算机视觉和自然语言处理（NLP）等细分方向的具体实现代码。
- 作为一个“Awesome”列表， curated 精选高质量项目，降低开发者寻找资源的成本。
- 支持Python语言实现，便于快速上手和二次开发。

3. **适用场景**
- AI初学者希望系统性地通过阅读和运行代码来学习不同子领域的基础知识。
- 研究人员或工程师需要参考现有开源项目以加速特定任务（如图像识别或文本分析）的开发。
- 教育者将其作为教学案例库，用于展示机器学习在实际应用中的多种可能性。

4. **技术亮点**
- 项目规模庞大且分类清晰，集成了人工智能主要分支（CV、NLP、DL等）的代表性成果。
- 高星标数（35715+）证明了其在社区中的高认可度和广泛影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35715 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一个用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持广泛的模型格式，帮助用户直观地检查模型结构和参数。该项目旨在提供简洁高效的模型浏览体验。

**2. 核心功能**
- 支持多种主流框架模型（如 TensorFlow, PyTorch, Keras, ONNX 等）的可视化。
- 提供直观的节点图视图，清晰展示网络层之间的连接关系。
- 允许查看和编辑模型的具体参数及权重数据。
- 支持导出模型结构为静态图片或 HTML 文件以便分享。
- 兼容桌面应用与 Web 浏览器两种运行模式。

**3. 适用场景**
- 模型调试：开发者通过可视化结构快速定位网络层错误。
- 文档编写：研究人员使用截图制作论文或技术报告中的模型架构图。
- 模型转换验证：在将模型从一种框架转换为另一种格式后，检查结构一致性。
- 代码学习：初学者通过观察成熟项目的模型结构来理解算法实现。

**4. 技术亮点**
- 极高的兼容性：覆盖 CoreML, TFLite, Safetensors 等数十种格式，是业界标准的轻量级可视化工具。
- 跨平台易用性：无需安装复杂依赖，通过本地应用或在线网页即可直接使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33263 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必备的核心速查表（Cheat Sheets）。内容涵盖了从基础数学库到高级框架的关键语法与函数，旨在帮助研究人员快速回顾和查阅技术细节。

2. **核心功能**
*   提供 NumPy、SciPy 等数值计算库的快速参考指南。
*   包含 Matplotlib 数据可视化库的常用绘图命令汇总。
*   整理 Keras 深度学习框架的关键 API 使用示例。
*   涵盖机器学习与深度学习领域的基础概念速记卡片。
*   整合了 Medium 博主推荐的相关资源链接供进一步学习。

3. **适用场景**
*   研究人员在实验遇到瓶颈时，快速查找特定函数的用法。
*   初学者在学习过程中，对照速查表复习和巩固核心知识点。
*   开发者在进行代码迁移或重构时，快速核对不同库之间的语法差异。
*   面试准备期间，高效记忆常用算法库和框架的关键参数。

4. **技术亮点**
*   高度聚合：将分散在多个文档中的关键信息整合为统一的视觉化速查表。
*   实用性极强：直接聚焦于“高频使用”的代码片段，减少查阅官方文档的时间成本。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目提供了一条完整的人工智能学习路线图，整合了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户入门并胜任就业实战。内容涵盖Python、机器学习、深度学习、计算机视觉及自然语言处理等热门领域的主流框架与工具。

### 2. 核心功能
*   **系统化学习路径**：提供从数学基础到高级AI应用的清晰学习路线。
*   **海量实战案例**：收录近200个精选项目与案例，强化动手能力。
*   **免费教学资源**：配套提供免费的教材与学习资料，降低学习门槛。
*   **就业导向训练**：专注于实际应用场景，帮助用户达到就业标准。
*   **全栈技术覆盖**：支持Python、TensorFlow、PyTorch、Keras等多框架学习。

### 3. 适用场景
*   **AI初学者入门**：适合无编程或AI基础的用户建立知识体系。
*   **求职者技能提升**：适合希望进入AI行业并通过实战项目丰富简历的人员。
*   **高校/培训机构辅助教学**：可作为课程补充材料，提供丰富的案例参考。
*   **技术爱好者自我进阶**：适合对机器学习、NLP、CV等领域感兴趣的开发者深入探索。

### 4. 技术亮点
*   **多框架兼容**：同时支持TensorFlow 2、PyTorch、Caffe、Keras等主流深度学习框架。
*   **数据科学生态完善**：集成NumPy、Pandas、Matplotlib、Seaborn等数据分析核心库。
*   **领域全覆盖**：横跨算法、数学、数据挖掘、计算机视觉（CV）和自然语言处理（NLP）。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化工作流，降低了机器学习模型的开发与训练门槛。

**2. 核心功能**
*   **低代码/无代码建模**：支持通过 YAML 配置文件定义模型架构，无需编写复杂代码即可快速启动项目。
*   **广泛的模型支持**：原生支持深度学习、传统机器学习以及基于 Hugging Face 的大语言模型（如 Llama、Mistral）的微调与训练。
*   **自动化数据处理**：内置强大的数据预处理管道，自动处理缺失值、标准化及特征编码等步骤。
*   **集成化实验管理**：提供可视化的训练指标监控、超参数优化及模型评估工具，简化实验迭代流程。

**3. 适用场景**
*   **快速原型开发**：数据科学家或研究人员希望在不深入底层代码的情况下，迅速验证不同模型架构的效果。
*   **企业级 AI 应用部署**：需要标准化、可复现地构建和微调特定领域的大语言模型（如客服机器人、文本分类器）。
*   **多模态数据分析**：处理包含表格数据、图像、文本等多种类型的混合数据集，并从中提取有价值的洞察。

**4. 技术亮点**
*   **声明式 API**：采用简洁的 YAML 语法描述模型，极大提升了代码的可读性与可维护性。
*   **底层引擎灵活**：后端无缝对接 PyTorch 和 Hugging Face Transformers，兼顾了高性能计算与前沿 NLP 能力。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11746 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9147 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8938 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6994 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6292 | 🍴 755 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且强大的自然语言处理（NLP）资源仓库，集成了中英文敏感词检测、语言识别、实体抽取（手机号/身份证/邮箱等）及多种词典资源。它提供了从基础文本处理到高级深度学习模型（如BERT）的广泛应用场景支持，并包含大量开源数据集与预训练模型。

**2. 核心功能**
*   **基础文本处理与清洗**：提供敏感词过滤、繁简转换、停用词、反动词表及中英文分词工具。
*   **丰富实体与知识抽取**：支持人名、地名、身份证号、手机号等实体抽取，以及基于依存句法和语义角色的事件三元组抽取。
*   **多领域词典与语料库**：涵盖医学、法律、汽车、财经、古诗词等多个垂直领域的专业词库及大规模中文闲聊/问答数据集。
*   **前沿AI模型与工具集**：整合了BERT、GPT-2等预训练模型应用代码，以及OCR、语音识别（ASR）、知识图谱构建等实用工具。
*   **NLP数据增强与可视化**：提供EDA数据增强工具、情感分析、相似度匹配算法集合及文本可视化工具。

**3. 适用场景**
*   **内容安全审核系统**：利用敏感词库和暴恐词表快速识别和过滤违规内容。
*   **智能客服与聊天机器人开发**：基于海量中文闲聊语料、对话数据集及预训练模型构建多轮对话系统。
*   **垂直行业知识图谱构建**：借助医学、法律、金融等领域的专用词库和数据集，提取实体关系以构建领域知识图谱。
*   **文本挖掘与信息抽取**：从非结构化文本中自动提取关键信息（如联系方式、证件号），用于简历解析或文档自动化处理。

**4. 技术亮点**
*   资源极度丰富，几乎涵盖了NLP领域所需的所有基础词典、数据集及主流深度学习框架的实现代码。
*   紧跟技术前沿，集成了BERT、ALBERT、RoBERTa等最新预训练语言模型在中文场景下的微调与应用示例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82054 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目旨在简化大模型的指令微调与强化学习过程，兼具易用性与高性能。

2. **核心功能**
- 支持超过 100 种主流 LLM 和 VLM 的统一微调接口。
- 集成 LoRA、QLoRA 等高效参数微调（PEFT）技术以降低资源消耗。
- 提供完整的 RLHF（基于人类反馈的强化学习）及直接偏好优化（DPO）训练流程。
- 内置多种量化方案（如 bitsandbytes），支持在有限显存下运行大规模模型。
- 兼容 Transformers 生态，实现即插即用的模型加载与推理。

3. **适用场景**
- 研究人员或开发者需要对特定垂直领域数据快速微调开源大模型。
- 显存受限环境下，通过 QLoRA 等技术对千亿参数模型进行高效训练。
- 希望利用 RLHF/DPO 技术对齐模型输出，提升其回答质量与安全性。
- 需要同时处理文本生成与多模态（图文理解）任务的一站式开发环境。

4. **技术亮点**
- **高度统一性**：无需为不同模型编写复杂的训练脚本，一个框架覆盖百种模型。
- **极致效率**：结合 FlashAttention 和 PagedOptimizer 等技术，显著提升训练速度并降低显存占用。
- **前沿算法支持**：原生支持最新的 MoE（混合专家）架构及多种 SOTA 微调策略。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73519 | 🍴 8985 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能通识课程，旨在让所有人轻松入门AI领域。项目通过Jupyter Notebook提供交互式学习体验，内容覆盖从基础概念到深度学习核心技术的全面知识体系。

2. **核心功能**
- 提供结构化的12周学习计划，将复杂的AI知识拆解为24个易于消化的课程单元。
- 采用Jupyter Notebook格式，支持代码即时运行与可视化，实现“边学边练”的互动式教学。
- 涵盖机器学习、深度学习（CNN/RNN/GAN）及自然语言处理（NLP）等主流AI核心技术模块。
- 由Microsoft发起，确保课程内容兼具学术严谨性与工业界实战应用的参考价值。

3. **适用场景**
- AI初学者希望系统性地从零开始构建人工智能知识体系。
- 高校教师或培训机构用于开设入门级AI课程或工作坊的教学辅助材料。
- 非技术背景人士希望通过结构化课程了解AI基本原理与应用潜力的学习者。

4. **技术亮点**
- 课程内容由Microsoft资深工程师与专家编写，紧跟行业前沿技术趋势。
- 强调实践导向，每个章节均配有可执行的代码示例和实际案例，降低理论理解门槛。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52884 | 🍴 10740 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，帮助开发者深入理解并掌握AI工程的核心原理。它提供了从学习、搭建到最终部署的完整实践路径，让开发者能够真正打造出可供他人使用的AI应用。

2. **核心功能**
*   涵盖从基础机器学习到前沿生成式AI的全面知识体系与实践。
*   提供基于Python和Rust等语言的底层实现教程，强调“从零构建”而非仅调用API。
*   深入讲解大语言模型（LLM）、智能体（Agents）及多模态技术的集成与应用。
*   包含计算机视觉、自然语言处理及强化学习等多领域的具体案例开发。

3. **适用场景**
*   AI初学者希望深入理解算法底层逻辑，而不仅仅是使用高级框架。
*   工程师希望构建高性能、可定制化的私有化AI应用或智能体系统。
*   研究人员需要参考从零实现复杂AI模块（如Transformer、Swarm Intelligence）的代码结构。

4. **技术亮点**
*   跨语言支持：结合Python的快速开发与Rust的高性能优势，覆盖全栈AI工程能力。
*   前沿技术整合：紧跟MCP（Model Context Protocol）、Swarm Intelligence及Generative AI等最新趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43587 | 🍴 7307 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深入结合了线性代数基础及PyTorch、TF2等主流深度学习框架。它集成了NLTK自然语言处理工具，旨在通过代码实践帮助用户系统掌握从传统算法到深度学习的核心技能。

2. **核心功能**
- 提供基于Scikit-learn的多种经典机器学习算法（如SVM、K-Means、逻辑回归等）的实战代码。
- 包含使用PyTorch和TensorFlow 2.x实现的深度学习模型（如RNN、LSTM、DNN）示例。
- 集成NLTK库进行自然语言处理（NLP）任务，涵盖文本分析与推荐系统相关技术。
- 梳理机器学习背后的数学原理，特别是线性代数在算法中的应用。

3. **适用场景**
- 计算机科学或数据科学专业的学生用于辅助课程学习及毕业项目实践。
- 希望从理论转向代码实现的机器学习初学者，用于快速上手主流算法框架。
- 需要复习经典算法实现或探索NLP与推荐系统具体应用场景的数据分析师。

4. **技术亮点**
- 实现了从传统统计学习（如AdaBoost、FP-Growth）到前沿深度学习（TF2/PyTorch）的全链路覆盖。
- 强调理论与实践结合，不仅提供代码，还关联了必要的数学基础（线性代数）。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42417 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35715 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33773 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28820 | 🍴 3517 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26015 | 🍴 2951 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21765 | 🍴 3309 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供涵盖多个核心AI领域的实战案例与资源库，内容全面且实用。

2. **核心功能**
- 提供海量AI相关项目源码，覆盖从基础机器学习到前沿深度学习的广泛领域。
- 包含计算机视觉和自然语言处理（NLP）等细分方向的具体实现代码。
- 作为一个“Awesome”列表， curated 精选高质量项目，降低开发者寻找资源的成本。
- 支持Python语言实现，便于快速上手和二次开发。

3. **适用场景**
- AI初学者希望系统性地通过阅读和运行代码来学习不同子领域的基础知识。
- 研究人员或工程师需要参考现有开源项目以加速特定任务（如图像识别或文本分析）的开发。
- 教育者将其作为教学案例库，用于展示机器学习在实际应用中的多种可能性。

4. **技术亮点**
- 项目规模庞大且分类清晰，集成了人工智能主要分支（CV、NLP、DL等）的代表性成果。
- 高星标数（35715+）证明了其在社区中的高认可度和广泛影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35715 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的复杂工作流。它利用大语言模型（LLM）和计算机视觉技术，模拟人类操作浏览器，从而替代传统的脚本式自动化方案。该项目旨在为需要与网页交互的业务流程提供智能、稳定的解决方案。

2. **核心功能**
*   利用大语言模型理解页面内容并生成操作指令，实现智能决策。
*   结合计算机视觉技术识别网页元素，无需依赖固定的选择器即可定位目标。
*   支持多种浏览器自动化工具后端（如 Playwright、Puppeteer），提供灵活的集成选项。
*   提供 API 接口，便于将浏览器自动化能力嵌入到现有的 RPA 或业务流程系统中。
*   具备自我纠错和重试机制，提高在动态网页环境下的执行成功率。

3. **适用场景**
*   企业级 RPA（机器人流程自动化）：自动化处理需要登录、数据录入和跨系统交互的重复性行政工作。
*   竞品监控与数据采集：自动访问竞争对手网站，提取价格、库存或产品详情等结构化数据。
*   在线表单填写与业务办理：自动完成政府服务、银行申请或注册流程中复杂的表单填写任务。
*   测试自动化：用于 UI 端到端测试，特别是在传统 Selenium 脚本难以维护的动态 Web 应用上。

4. **技术亮点**
*   **去选择器化设计**：通过视觉和语义理解代替脆弱的 CSS/XPath 选择器，显著降低因页面改版导致的维护成本。
*   **AI 驱动的智能体**：将 LLM 作为“大脑”控制浏览器操作，使工具能够适应非标准化的网页布局。
*   **多引擎兼容**：底层抽象层支持 Playwright 等现代自动化工具，兼顾性能与稳定性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22593 | 🍴 2117 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，支持图像、视频及3D数据的AI辅助标注。它提供开源、云端及企业级产品，涵盖质量保障、团队协作、数据分析及开发者API等全方位功能。

### 2. **核心功能**
- 支持图像、视频和3D数据的自动化与交互式标注。
- 内置AI辅助标签功能以提升标注效率和质量。
- 提供完善的质量保证机制及团队协作管理工具。
- 开放开发者API并集成数据分析能力。

### 3. **适用场景**
- 为计算机视觉模型训练构建大规模标注数据集。
- 深度学习研究中的图像分类、目标检测或语义分割任务。
- 需要多人协作进行数据清洗与标注的企业级项目。

### 4. **技术亮点**
- 兼容主流深度学习框架（PyTorch/TensorFlow）及标准数据集格式（如ImageNet）。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16385 | 🍴 3775 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12930 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11290 | 🍴 1206 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8875 | 🍴 2190 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3299 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2629 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2430 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，让用户以“龙虾”（OpenClaw）的方式完全掌控自己的数据。它强调本地化部署和数据隐私，提供跨平台的无缝 AI 体验。

2. **核心功能**
- 支持多操作系统与平台，实现广泛的设备兼容性。
- 本地优先架构，确保用户数据隐私与安全可控。
- 提供个性化的 AI 助手服务，满足日常智能需求。
- 基于 TypeScript 开发，具备良好的扩展性和维护性。

3. **适用场景**
- 重视数据隐私的个人用户，希望本地运行 AI 助手。
- 开发者或技术爱好者，需要在不同平台上集成自定义 AI 功能。
- 希望摆脱云端依赖，构建自主可控个人知识管理系统的用户。

4. **技术亮点**
- 采用 TypeScript 编写，代码结构清晰，便于二次开发与社区贡献。
- “Own-your-data”理念贯穿设计，强调去中心化的数据所有权。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 384153 | 🍴 80717 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过实战验证的智能体技能框架及软件开发方法论。它通过结合头脑风暴、编码实践以及子代理驱动的开发模式，提供了一套完整的软件开发生命周期（SDLC）解决方案。该项目旨在利用 AI 智能体自动化处理复杂任务，提升开发效率与代码质量。

2. **核心功能**
*   **子代理驱动开发**：利用专门的子智能体执行具体的编程和调试任务，实现模块化自动化。
*   **智能技能框架**：提供一套标准化的“技能”库，支持 AI 智能体在特定领域内的灵活调用与组合。
*   **全生命周期支持**：涵盖从需求头脑风暴到最终代码交付的完整 SDLC 流程。
*   **Shell 脚本集成**：基于 Shell 脚本构建，便于在 Linux/macOS 环境下快速部署和运行。
*   **协作式头脑风暴**：内置辅助工具，帮助开发者与 AI 共同进行技术选型和方案设计。

3. **适用场景**
*   **自动化软件开发**：适合希望利用 AI 辅助生成、测试和优化代码的团队或个人开发者。
*   **复杂项目架构设计**：适用于需要通过多步骤推理和子任务分解来规划大型软件系统的场景。
*   **敏捷开发加速**：用于快速原型制作（MVP）或迭代开发中，通过智能体加速编码和修复过程。

4. **技术亮点**
*   将抽象的“智能体技能”概念转化为可执行的软件开发方法论，填补了理论框架与实际落地之间的空白。
*   采用开源社区广泛认可的标签体系（如 `obra`, `subagent-driven-development`），强调了其在 AI 辅助编程领域的创新性和前瞻性。
- 链接: https://github.com/obra/superpowers
- ⭐ 261304 | 🍴 23318 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220645 | 🍴 42020 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198043 | 🍴 59635 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185692 | 🍴 46068 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166376 | 🍴 21495 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164275 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157305 | 🍴 46185 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156145 | 🍴 8876 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152407 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

