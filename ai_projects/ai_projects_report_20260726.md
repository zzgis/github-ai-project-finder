# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### ocm-mcp-server
- ### 1. **中文简介**
ocm-mcp-server 是一个 MCP（Model Context Protocol）服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心节点操作多集群 Kubernetes 环境。它在模型与底层集群之间提供了策略控制、审批流程及审计日志功能，确保 AI 操作的安全性与合规性。

### 2. **核心功能**
*   **多集群统一管控**：通过 OCM Hub 集中管理多个 Kubernetes 集群的资源与状态。
*   **AI 智能体接口**：提供标准化的 MCP 协议接口，使 LLM 驱动的 AI 代理能直接执行运维任务。
*   **安全审批机制**：在 AI 执行关键操作前引入人工或自动审批环节，防止误操作。
*   **完整审计追踪**：记录所有由 AI 发起的操作日志，满足企业级合规与安全审计需求。
*   **策略强制执行**：将预设的运维策略应用于集群交互中，限制 AI 的能力边界。

### 3. **适用场景**
*   **自动化运维辅助**：利用 AI 助手进行日常集群监控、故障排查及简单配置变更。
*   **高安全要求的 DevOps**：在需要严格审计和审批流程的生产环境中，让 AI 辅助处理低风险任务。
*   **多云/混合云管理**：通过统一的 OCM 平台，使用 AI 简化跨不同 Kubernetes 集群的管理复杂度。
*   **开发者效率提升**：为开发人员提供自然语言交互界面，降低操作复杂 K8s 集群的技术门槛。

### 4. **技术亮点**
*   **MCP 协议集成**：采用最新的 Model Context Protocol 标准，实现了 AI 模型与基础设施之间的标准化连接。
*   **OCM 深度整合**：基于 Red Hat 的 Open Cluster Management 项目，利用其成熟的多集群管理能力。
*   **内置治理层**：不仅提供访问能力，还原生集成了策略、审批和审计三大治理支柱，兼顾效率与安全。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 20 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能够将视觉描述提取并结构化，生成用于生成式 AI 的优化 JSON 提示词。该应用内置 SQLite 数据库以便管理提示词，并提供可调整的显存硬件配置文件及 ComfyUI 节点集成。

2. **核心功能**
*   使用本地 Ollama LLM 分析文本与图像数据。
*   将视觉内容转化为结构化的优化 JSON 提示词。
*   内置 SQLite 数据库支持提示词的存储与编辑。
*   提供可调节的 VRAM 硬件配置文件以适应不同设备。
*   包含 ComfyUI 节点以直接调用数据库中的提示词。

3. **适用场景**
*   需要在本地环境运行且注重隐私的数据分析工作流。
*   希望自动化将视觉信息转换为标准 AI 输入格式的开发人员。
*   使用 ComfyUI 并希望集中管理提示词资源的 AI 艺术家。
*   显存资源受限或需灵活配置硬件性能的 GPU 用户。

4. **技术亮点**
*   实现了本地 LLM 分析与结构化输出流程的闭环。
*   通过 SQLite 与 ComfyUI 节点集成，提升了工作流的连贯性。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 17 | 🍴 2 | 语言: Python

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
Verity-JE-Mod 是一款专为 Minecraft Java 版 1.21+ 设计的模组，引入了全新怪物、自定义维度、生物群系及世界生成机制。该模组不支持基岩版，怪物具备配音、背景故事及多阶段 AI 行为。

2. **核心功能**
- 引入拥有配音和背景故事的全新实体“Verity”。
- 实现多阶段人工智能（AI），提供更具挑战性的战斗体验。
- 添加自定义维度、生物群系及独特的世界生成规则。
- 同时支持 Forge 和 Fabric 加载器，可在 Modrinth 平台免费下载。

3. **适用场景**
- 寻求高难度战斗体验并喜欢探索新怪物的进阶玩家。
- 希望丰富游戏世界观，体验剧情驱动型模组内容的用户。
- 搭建基于特定版本（1.21+）的自定义服务器或整合包。

4. **技术亮点**
- 实现了复杂的多阶段 AI 逻辑与实体音频集成。
- 兼容主流模组加载器（Forge/Fabric）及较新的游戏版本（1.21+）。
- 链接: https://github.com/veritymodminecraft/Verity-JE-Mod-Minecraft
- ⭐ 14 | 🍴 0 | 语言: Java
- 标签: 1-16-5, 1-8, all-the-mods-modpack, allthemods, evernym-verity

### Cursor-Grok-4.5-xAI-free
- **1. 中文简介**
该项目是一款支持 Windows、macOS 和 Linux 的免费桌面应用，旨在为用户提供 Grok 4.5 模型在 Cursor IDE 中的集成体验。它允许用户在不购买 X Premium 或 Supergrok 订阅的情况下，享受具备实时网页搜索和代码Composer功能的 AI 编程辅助，且定价极具竞争力。

**2. 核心功能**
*   **跨平台支持**：兼容 Windows、macOS 和 Linux 操作系统。
*   **IDE 深度集成**：在 Cursor 中实现类似 Composer 的交互式编码体验和无限免费试用模式。
*   **实时网络搜索**：集成 Grok 4.5 的实时联网检索能力，确保代码生成基于最新信息。
*   **零订阅成本访问**：绕过官方付费墙，免费使用 xAI 的 Grok 4.5 模型服务。

**3. 适用场景**
*   **预算有限的开发者**：希望使用前沿大模型进行辅助编程，但不愿支付高昂 API 费用或订阅费的用户。
*   **Cursor IDE 重度用户**：需要增强版 AI 能力（如实时搜索、复杂代码重构）以提升开发效率的程序员。
*   **多平台协作团队**：需要在不同操作系统环境下统一 AI 编码体验的技术团队。

**4. 技术亮点**
*   基于 TypeScript 构建，确保了良好的类型安全和跨平台兼容性。
*   巧妙利用 Cursor SDK 和 API 接口，实现了非官方渠道对 Grok 4.5 模型的无缝对接与调用。
- 链接: https://github.com/cursorgrok45free/Cursor-Grok-4.5-xAI-free
- ⭐ 13 | 🍴 0 | 语言: TypeScript
- 标签: ai-powered-applications, composer-2-5, cursor-ai-assistant, cursor-ai-project-rules, cursor-api

### Claude-Code-Sonnet-5-Free-Desktop
- 1. **中文简介**
Claude-Code-Sonnet-5-Free-Desktop 是一款适用于 Windows、macOS 和 Linux 的免费桌面版 AI 编程助手，无需 API 密钥即可使用。其基准测试表现优于 Sonnet 4.6，成本低于 Opus 5，且在上下文窗口方面超越 GitHub Copilot，运行速度可与 Fable 5 媲美。用户下载后即可立即开始编码工作。

2. **核心功能**
*   跨平台支持：兼容 Windows、macOS 和 Linux 操作系统。
*   零配置接入：无需提供 API 密钥即可直接使用 Claude 模型能力。
*   高性能编码辅助：在上下文处理能力上击败 GitHub Copilot，并具备接近 Fable 5 的运行速度。
*   低成本高效能：以低于 Opus 5 的成本实现超越 Sonnet 4.6 的基准测试成绩。

3. **适用场景**
*   缺乏 Anthropic API 访问权限但希望体验最新 Claude 模型的开发者。
*   需要处理超长代码库上下文，对上下文窗口大小有极高要求的复杂项目。
*   追求高性价比 AI 编码辅助工具，希望降低 API 调用成本的团队或个人。
*   需要在多操作系统环境（Win/Mac/Linux）中统一使用同一款桌面端 AI 工具的开发者。

4. **技术亮点**
*   基于 TypeScript 开发，具备良好的跨平台兼容性和扩展性。
*   实现了本地桌面应用与云端 AI 能力的无缝集成，提供类似原生应用的用户体验。
- 链接: https://github.com/claudesonnet5free/Claude-Code-Sonnet-5-Free-Desktop
- ⭐ 13 | 🍴 0 | 语言: TypeScript
- 标签: anthropic-, claude-4-opus, claude-5-sonnet, claude-code-desktop, claude-code-prompts

### AI_Data_Analatyics_Assistant
- 描述: 无描述
- 链接: https://github.com/Rakshana0205/AI_Data_Analatyics_Assistant
- ⭐ 9 | 🍴 0 | 语言: JavaScript

### ViralSim
- 描述: 让一群 AI 用户先刷到你的笔记：模拟小红书图文的停留、阅读与互动，并用真实发布数据持续校准爆款概率。
- 链接: https://github.com/white0dew/ViralSim
- ⭐ 9 | 🍴 4 | 语言: TypeScript
- 标签: ai-agents, content-analysis, creator-tools, multi-agent, multimodal-ai

### ai-cost-history-hub
- 描述: Local AI coding-agent history + API cost analytics (loopback-only).
- 链接: https://github.com/zheyan2517/ai-cost-history-hub
- ⭐ 8 | 🍴 1 | 语言: TypeScript
- 标签: coding-agents, cost-tracking, dashboard, local-first, open-source

### amper-music-studio-2026
- 描述: Amper Music 2026 v18 is a Windows 10/11 desktop application for AI-assisted music composition, audio editing, loop organization, and exporting finished music projects.
- 链接: https://github.com/logan-wardgv9965/amper-music-studio-2026
- ⭐ 8 | 🍴 3 | 语言: HTML

### OptMem
- 描述: A permanent, append-only memory for AI agents. Two text files, four commands, any harness.
- 链接: https://github.com/VictorTaelin/OptMem
- ⭐ 7 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能全面的自然语言处理（NLP）工具库，主要提供中英文敏感词检测、语言识别、实体抽取及繁简转换等基础处理能力。该项目还整合了大量垂直领域的知识库（如医疗、法律、汽车）、预训练模型资源以及对话系统组件，旨在为开发者提供一站式的中文 NLP 解决方案。

2. **核心功能**
*   **基础文本处理与抽取**：支持中英文敏感词过滤、手机号/身份证/邮箱等正则抽取、命名实体识别（NER）及文本情感分析。
*   **丰富的领域知识图谱**：内置中日文人名、职业、汽车品牌、成语、古诗词及各类专业术语库，并支持跨语言知识图谱构建。
*   **预训练模型与资源集成**：收录了 BERT、GPT-2、ALBERT 等多种主流预训练模型的中文版本及相关微调代码。
*   **语音与多模态支持**：包含中文语音识别（ASR）数据集、发音标记模块及OCR文字识别相关工具。
*   **对话系统与生成任务**：提供聊天机器人语料、自动对联、歌词生成器及基于检索或生成的对话系统框架。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和暴恐词表快速识别和过滤互联网平台中的违规文本。
*   **智能客服与聊天机器人开发**：基于现有的对话语料、意图识别及知识库构建领域特定的智能问答系统。
*   **企业级数据清洗与信息抽取**：从非结构化文档中自动化提取关键信息（如人名、地名、机构名），用于构建企业知识图谱。
*   **NLP 算法研究与教学**：作为学习中文 NLP 的参考仓库，获取高质量数据集、基准测试模型及前沿论文解读。

4. **技术亮点**
*   **资源聚合度高**：不仅包含代码实现，还整合了海量中文 NLP 数据集、预训练模型权重及权威技术报告，极大降低了研究门槛。
*   **领域覆盖广**：针对中文特有的需求（如繁简转换、拼音标注、中文分词优化）提供了专门化工具，弥补了通用英文 NLP 工具的不足。
*   **实战导向**：提供了从基础分词到复杂深度学习模型（如 BERT、Transformer）应用的全链路示例代码，便于快速原型开发。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82041 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。该项目提供了丰富的实战案例与源代码，旨在帮助开发者快速掌握AI核心技术。作为一份“精选”资源库，它适合不同层次的AI学习者进行系统性的实践练习。

2. **核心功能**
- 提供大量经过验证的机器学习与深度学习项目源码。
- 覆盖计算机视觉和自然语言处理（NLP）等主流AI子领域。
- 以Python为主要实现语言，便于直接运行和修改代码。
- 结构化的项目列表，方便用户按主题查找和学习。
- 集成代码示例，降低从理论到实践的入门门槛。

3. **适用场景**
- AI初学者通过实战项目巩固机器学习算法知识。
- 开发者寻找计算机视觉或NLP任务的具体实现参考。
- 研究人员对比不同AI模型在特定数据集上的表现。
- 教育机构用于布置编程作业或构建课程实验案例。

4. **技术亮点**
- 资源体量庞大，汇集了数百个高质量开源项目。
- 标签分类清晰，支持按领域（如CV、NLP）精准检索。
- 强调“带代码”的实操性，而非单纯的理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35706 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和参数。通过简洁的界面，开发者可以快速理解复杂模型的数据流向与内部机制。

**2. 核心功能**
*   广泛支持包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等在内的多种模型格式。
*   提供图形化界面，清晰展示神经网络的层结构、张量形状及权重数据。
*   支持交互式操作，允许用户展开或折叠网络层级以聚焦特定部分。
*   具备导出功能，可将模型结构截图或生成静态图片用于文档和演示。

**3. 适用场景**
*   **模型调试与验证**：在训练过程中检查模型架构是否符合预期，排查连接错误。
*   **论文与报告配图**：快速生成高质量的网络结构图，用于学术论文或技术博客展示。
*   **跨框架模型转换检查**：验证从 PyTorch 到 ONNX 或其他格式的转换结果是否正确。
*   **教学与演示**：向非技术人员或学生直观解释深度学习模型的工作原理。

**4. 技术亮点**
*   **轻量级与便携性**：基于 Electron 构建，无需安装复杂的 Python 环境或依赖库，双击即可运行。
*   **纯前端实现**：主要使用 JavaScript 开发，利用浏览器技术渲染图形，访问便捷且跨平台兼容性好。
*   **实时预览能力**：加载大型模型文件时仍能保持较好的响应速度，适合快速迭代查看。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33262 | 🍴 3168 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，打破平台壁垒。通过统一格式，开发者可以更高效地跨环境运行和优化模型。

**2. 核心功能**
*   **框架互操作性**：支持将模型从PyTorch、TensorFlow、Scikit-learn等主流框架转换为统一格式。
*   **跨平台部署**：允许训练好的模型在不同硬件和操作系统上高效运行，无需重新训练。
*   **格式标准化**：定义了一套标准化的计算图表示法，确保模型结构的一致性。
*   **生态兼容性**：提供广泛的工具链支持，包括模型转换、验证及优化工具。

**3. 适用场景**
*   **模型迁移**：在开发阶段使用PyTorch训练模型，生产阶段部署到TensorRT或ONNX Runtime以提高性能。
*   **多框架协作**：团队中不同成员使用不同深度学习框架时，通过ONNX共享和交换模型。
*   **边缘设备部署**：将大型云端模型转换为轻量级ONNX格式，以便在手机或IoT设备上运行。
*   **混合系统构建**：集成来自不同来源的组件模型，构建复杂的端到端机器学习流水线。

**4. 技术亮点**
*   **开源社区驱动**：由Microsoft、Facebook等巨头共同维护，拥有活跃的开源社区和广泛的框架支持。
*   **高性能运行时**：配套的ONNX Runtime提供针对CPU、GPU等多种硬件的极致优化推理能力。
- 链接: https://github.com/onnx/onnx
- ⭐ 21214 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一本全面涵盖机器学习工程实践的指南。它深入探讨了从硬件基础设施到模型训练、推理及大规模部署的全流程技术细节。

2. **核心功能**
- 提供大规模分布式训练的优化策略与故障排除方案。
- 详解大语言模型（LLM）的训练、微调及高效推理技术。
- 涵盖GPU集群管理、网络通信及存储系统的高性能配置。
- 分享MLOps最佳实践，包括可扩展性架构与Slurm作业调度。

3. **适用场景**
- 需要搭建和维护大规模GPU集群以进行深度学习训练的工程团队。
- 致力于优化大语言模型推理延迟和降低计算成本的AI研究人员。
- 希望建立标准化、可扩展的机器学习生产流水线（MLOps）的企业。

4. **技术亮点**
- 深度结合PyTorch、Transformers等主流框架的底层原理剖析。
- 针对SLURM调度和异构硬件环境的实战级性能调优指南。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18467 | 🍴 1181 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17335 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13181 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11596 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10676 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。该项目提供了丰富的实战案例与源代码，旨在帮助开发者快速掌握AI核心技术。作为一份“精选”资源库，它适合不同层次的AI学习者进行系统性的实践练习。

2. **核心功能**
- 提供大量经过验证的机器学习与深度学习项目源码。
- 覆盖计算机视觉和自然语言处理（NLP）等主流AI子领域。
- 以Python为主要实现语言，便于直接运行和修改代码。
- 结构化的项目列表，方便用户按主题查找和学习。
- 集成代码示例，降低从理论到实践的入门门槛。

3. **适用场景**
- AI初学者通过实战项目巩固机器学习算法知识。
- 开发者寻找计算机视觉或NLP任务的具体实现参考。
- 研究人员对比不同AI模型在特定数据集上的表现。
- 教育机构用于布置编程作业或构建课程实验案例。

4. **技术亮点**
- 资源体量庞大，汇集了数百个高质量开源项目。
- 标签分类清晰，支持按领域（如CV、NLP）精准检索。
- 强调“带代码”的实操性，而非单纯的理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35706 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和参数。通过简洁的界面，开发者可以快速理解复杂模型的数据流向与内部机制。

**2. 核心功能**
*   广泛支持包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等在内的多种模型格式。
*   提供图形化界面，清晰展示神经网络的层结构、张量形状及权重数据。
*   支持交互式操作，允许用户展开或折叠网络层级以聚焦特定部分。
*   具备导出功能，可将模型结构截图或生成静态图片用于文档和演示。

**3. 适用场景**
*   **模型调试与验证**：在训练过程中检查模型架构是否符合预期，排查连接错误。
*   **论文与报告配图**：快速生成高质量的网络结构图，用于学术论文或技术博客展示。
*   **跨框架模型转换检查**：验证从 PyTorch 到 ONNX 或其他格式的转换结果是否正确。
*   **教学与演示**：向非技术人员或学生直观解释深度学习模型的工作原理。

**4. 技术亮点**
*   **轻量级与便携性**：基于 Electron 构建，无需安装复杂的 Python 环境或依赖库，双击即可运行。
*   **纯前端实现**：主要使用 JavaScript 开发，利用浏览器技术渲染图形，访问便捷且跨平台兼容性好。
*   **实时预览能力**：加载大型模型文件时仍能保持较好的响应速度，适合快速迭代查看。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33262 | 🍴 3168 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必不可少的速查表（Cheat Sheets）集合。内容涵盖从基础数学库到主流深度学习框架的关键知识点，旨在帮助研究者快速回顾核心概念与代码语法。

2. **核心功能**
*   提供Numpy、Scipy和Matplotlib等数据科学基础库的高效使用指南。
*   包含Keras等主流深度学习框架的核心API与操作速查。
*   整理人工智能与机器学习领域的关键理论概念与公式。
*   以简洁的图表和代码片段形式呈现，便于快速查阅。
*   针对研究人员优化，聚焦于高频使用的核心功能而非完整文档。

3. **适用场景**
*   研究人员在开发模型时快速回忆特定函数或库的使用方法。
*   机器学习初学者整理知识体系，建立对核心工具链的全面认知。
*   在技术面试或学术汇报前，快速复习关键算法与框架细节。
*   跨领域研究者（如从传统ML转向DL）快速上手新框架。

4. **技术亮点**
*   高度浓缩的知识结构，去除了冗余信息，直击核心用法。
*   视觉化呈现复杂概念，降低记忆负担，提升学习效率。
*   覆盖从底层数据处理到高层模型构建的全链路常用工具。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材。该项目旨在帮助零基础用户入门，覆盖从Python基础到深度学习、自然语言处理及计算机视觉等热门领域的核心知识，助力就业实战。

2. **核心功能**
*   提供系统化的AI学习路径，涵盖数学、机器学习、深度学习及数据分析等关键领域。
*   收录近200个精选实战案例与项目代码，支持PyTorch、TensorFlow、Keras等多种主流框架。
*   配备免费配套教材与资源，降低学习门槛，适合从零开始构建AI知识体系。
*   整合Python生态核心库（如NumPy, Pandas, Matplotlib等）的应用教程，强化数据科学技能。
*   聚焦计算机视觉（CV）、自然语言处理（NLP）等高热度细分方向的实战演练。

3. **适用场景**
*   **初学者入门**：适合无AI背景的学生或转行者，通过系统化路线和免费资料快速建立知识框架。
*   **求职实战准备**：求职者可通过参考其200+实战项目积累作品集，提升面试竞争力。
*   **技术选型参考**：开发者可依据路线图了解主流AI框架（TensorFlow vs PyTorch）及工具链的最佳实践。
*   **专项技能提升**：针对CV、NLP或数据分析特定方向的学习者，提供针对性的案例与代码参考。

4. **技术亮点**
*   高度集成主流AI框架与Python数据科学栈，提供一站式的实战代码示例。
*   内容结构清晰，将复杂的AI领域拆解为可执行的阶段性学习模块。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13181 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置方式，让开发者无需编写大量底层代码即可快速训练和部署机器学习模型。该项目支持多种深度学习后端，极大地降低了 AI 应用的开发门槛。

2. **核心功能**
*   **低代码/无代码体验**：通过 YAML 配置文件定义模型结构和数据管道，实现快速原型开发。
*   **多模态支持**：原生支持文本、图像、表格等多种数据类型，适用于计算机视觉和自然语言处理任务。
*   **预置模型组件**：内置丰富的层和模块（如 Embedding、CNN、Transformer），方便组合使用。
*   **自动化超参数调优**：集成自动搜索算法，帮助用户优化模型性能。
*   **易于部署**：生成的模型可直接导出为 ONNX 或 TensorFlow SavedModel 格式，便于在生产环境中部署。

3. **适用场景**
*   **快速 AI 原型验证**：希望在短时间内验证想法，而不想陷入繁琐的代码实现中。
*   **传统表格数据分析**：对结构化数据进行分类、回归等机器学习任务，替代传统 sklearn 流程。
*   **多模态应用开发**：需要同时处理文本描述和图像内容的复杂 AI 系统（如视觉问答）。
*   **教育与技术普及**：初学者或非专业数据科学家希望以更低门槛入门深度学习领域。

4. **技术亮点**
*   **声明式架构**：将模型逻辑与训练逻辑解耦，配置即文档，提升可维护性。
*   **广泛的社区生态**：拥有近 1.2 万星标，社区活跃，提供了大量预训练模型和示例。
*   **后端无关性**：底层可适配 PyTorch 等多种深度学习框架，提供统一的接口体验。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9147 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8939 | 🍴 3102 | 语言: C++
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
- ⭐ 6286 | 🍴 755 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能全面的自然语言处理（NLP）工具库，主要提供中英文敏感词检测、语言识别、实体抽取及繁简转换等基础处理能力。该项目还整合了大量垂直领域的知识库（如医疗、法律、汽车）、预训练模型资源以及对话系统组件，旨在为开发者提供一站式的中文 NLP 解决方案。

2. **核心功能**
*   **基础文本处理与抽取**：支持中英文敏感词过滤、手机号/身份证/邮箱等正则抽取、命名实体识别（NER）及文本情感分析。
*   **丰富的领域知识图谱**：内置中日文人名、职业、汽车品牌、成语、古诗词及各类专业术语库，并支持跨语言知识图谱构建。
*   **预训练模型与资源集成**：收录了 BERT、GPT-2、ALBERT 等多种主流预训练模型的中文版本及相关微调代码。
*   **语音与多模态支持**：包含中文语音识别（ASR）数据集、发音标记模块及OCR文字识别相关工具。
*   **对话系统与生成任务**：提供聊天机器人语料、自动对联、歌词生成器及基于检索或生成的对话系统框架。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和暴恐词表快速识别和过滤互联网平台中的违规文本。
*   **智能客服与聊天机器人开发**：基于现有的对话语料、意图识别及知识库构建领域特定的智能问答系统。
*   **企业级数据清洗与信息抽取**：从非结构化文档中自动化提取关键信息（如人名、地名、机构名），用于构建企业知识图谱。
*   **NLP 算法研究与教学**：作为学习中文 NLP 的参考仓库，获取高质量数据集、基准测试模型及前沿论文解读。

4. **技术亮点**
*   **资源聚合度高**：不仅包含代码实现，还整合了海量中文 NLP 数据集、预训练模型权重及权威技术报告，极大降低了研究门槛。
*   **领域覆盖广**：针对中文特有的需求（如繁简转换、拼音标注、中文分词优化）提供了专门化工具，弥补了通用英文 NLP 工具的不足。
*   **实战导向**：提供了从基础分词到复杂深度学习模型（如 BERT、Transformer）应用的全链路示例代码，便于快速原型开发。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82041 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目荣获 ACL 2024 会议认可，旨在简化从指令微调到强化学习的全流程训练体验。

2. **核心功能**
- 支持100多种主流大模型及多模态模型的统一高效微调。
- 集成 LoRA、QLoRA 等参数高效微调方法及多种量化技术以节省显存。
- 提供完整的 RLHF（人类反馈强化学习）及 DPO 对齐训练能力。
- 兼容 Transformers 和 PEFT 生态，支持指令微调与全量微调。

3. **适用场景**
- 研究人员或开发者需要对特定领域的 LLM 进行快速指令微调。
- 在显存受限的硬件环境下，通过 QLoRA 等技术高效微调大型模型。
- 需要利用人类反馈对模型进行对齐优化以提升回答质量与安全性的场景。

4. **技术亮点**
- 实现了多模型、多任务（SFT/RLHF）的统一接口，极大降低了微调门槛。
- 原生支持 MoE（混合专家）架构模型及最新的 VLM 多模态微调需求。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73512 | 🍴 8985 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能入门课程，旨在让所有人轻松掌握AI知识。项目基于Jupyter Notebook构建，涵盖了从基础机器学习到深度学习的广泛内容。它由微软发起，致力于提供零门槛的AI教育体验。

2. **核心功能**
- 提供结构化的12周学习路径，适合初学者循序渐进地掌握AI概念。
- 包含计算机视觉、自然语言处理等核心领域的实战练习与代码示例。
- 覆盖深度学习高级主题，如卷积神经网络(CNN)、循环神经网络(RNN)和生成对抗网络(GAN)。
- 采用Jupyter Notebook格式，支持交互式代码运行与即时结果反馈。

3. **适用场景**
- AI初学者或转行者希望系统性地建立人工智能基础知识体系。
- 教育工作者寻找开源、标准化的AI教学课程资源用于课堂或自学指导。
- 开发者希望在完成基础理论学习后，通过动手编码实践来巩固CNN、NLP等技术点。

4. **技术亮点**
- 由微软开源维护，内容权威且紧跟主流AI技术栈（如ML、DL、NLP）。
- 高度模块化的课程设计，将复杂概念拆解为易于理解的24个独立课时。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52871 | 🍴 10730 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在提供一套从零开始构建AI系统的完整指南，涵盖从理论学习到实际部署的全过程。它强调通过亲手实现核心组件来深入理解人工智能技术，并最终将其转化为可供他人使用的产品或服务。

2. **核心功能**
- 提供基于Python和Rust的从头实现教程，涵盖深度学习、NLP及计算机视觉等基础模块。
- 深入讲解生成式AI、大语言模型（LLM）及AI代理（Agents）的高级架构与工程实践。
- 结合强化学习与群体智能算法，展示复杂AI系统的构建与优化方法。
- 包含完整的课程式学习路径，指导用户将研究成果转化为可交付的工程产品。

3. **适用场景**
- AI初学者希望深入理解底层原理而非仅调用API的进阶学习场景。
- 工程师需要构建定制化、高性能或私有化的生成式AI应用与Agent系统。
- 研究人员探索新型AI架构（如结合Rust的性能优化或群体智能策略）。
- 教育机构或团队用于培训从零构建完整AI工作流的实战课程。

4. **技术亮点**
- **多语言混合工程**：结合Python（生态丰富）与Rust（高性能），展示如何在AI工程中平衡开发效率与运行性能。
- **全栈AI工程化**：不仅关注模型训练，更强调“Ship it”（部署与产品化），涵盖从开发到分发的完整生命周期。
- **前沿技术覆盖**：同步涵盖MCP（模型上下文协议）、Swarm Intelligence（群体智能）等最新AI工程趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43473 | 🍴 7282 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
该项目是一个综合性的 AI 学习资源库，涵盖了从线性代数基础到数据分析、机器学习实战的完整知识体系。内容深度整合了 PyTorch 和 TensorFlow 2 等主流深度学习框架，并结合 NLTK 进行自然语言处理实践。旨在为学习者提供从理论推导到代码实现的系统化指导。

2. **核心功能**
*   提供包括决策树、SVM、聚类（K-Means）、关联规则（Apriori, FP-Growth）在内的经典机器学习算法实现与解析。
*   深入讲解并应用 DNN、RNN、LSTM 等深度学习模型，结合 PyTorch 和 TF2 进行实战编码。
*   涵盖 NLP 自然语言处理领域，利用 NLTK 库进行文本分析与推荐系统算法实践。
*   补充线性代数等数学基础，帮助理解 PCA、SVD 等降维技术及回归分析背后的数学原理。

3. **适用场景**
*   初学者系统学习机器学习与深度学习全流程，建立从数学基础到工程实战的知识闭环。
*   数据科学家或算法工程师复习经典算法原理，并参考高质量代码实现优化现有项目。
*   高校学生或研究人员寻找包含具体案例的 NLP 及推荐系统学习素材。

4. **技术亮点**
*   **全栈覆盖**：打通了“数学基础-传统机器学习-深度学习-NLP”的技术链路，知识结构极为完整。
*   **双框架支持**：同时基于 PyTorch 和 TensorFlow 2 进行深度学习实战，适应不同技术栈需求。
*   **高社区认可**：拥有超过 4.2 万星标，证明其内容质量与实用性在开发者社区中广受好评。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42416 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35706 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33773 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28819 | 🍴 3517 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26014 | 🍴 2952 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21763 | 🍴 3311 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。该项目提供了丰富的实战案例与源代码，旨在帮助开发者快速掌握AI核心技术。作为一份“精选”资源库，它适合不同层次的AI学习者进行系统性的实践练习。

2. **核心功能**
- 提供大量经过验证的机器学习与深度学习项目源码。
- 覆盖计算机视觉和自然语言处理（NLP）等主流AI子领域。
- 以Python为主要实现语言，便于直接运行和修改代码。
- 结构化的项目列表，方便用户按主题查找和学习。
- 集成代码示例，降低从理论到实践的入门门槛。

3. **适用场景**
- AI初学者通过实战项目巩固机器学习算法知识。
- 开发者寻找计算机视觉或NLP任务的具体实现参考。
- 研究人员对比不同AI模型在特定数据集上的表现。
- 教育机构用于布置编程作业或构建课程实验案例。

4. **技术亮点**
- 资源体量庞大，汇集了数百个高质量开源项目。
- 标签分类清晰，支持按领域（如CV、NLP）精准检索。
- 强调“带代码”的实操性，而非单纯的理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35706 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22590 | 🍴 2118 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16381 | 🍴 3773 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12928 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11288 | 🍴 1206 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2190 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 384122 | 🍴 80712 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261103 | 🍴 23299 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220464 | 🍴 41971 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平源码工作流自动化平台，支持可视化搭建与自定义代码相结合。用户可选择自托管或云端部署，并通过其集成的 400 多种连接轻松实现业务流程自动化。

2. **核心功能**
- 提供可视化的工作流构建界面，同时允许嵌入自定义代码以实现高度灵活的业务逻辑。
- 拥有超过 400 种原生集成，能够无缝连接各种 API 和服务，简化数据流转。
- 内置原生 AI 能力，支持在工作流中直接调用大语言模型进行智能处理。
- 采用公平源码（Fair-code）许可，既提供自托管选项也支持云端服务，保障数据隐私与灵活性。

3. **适用场景**
- 企业级系统集成：连接 CRM、ERP 等不同系统，自动同步数据并触发后续业务流程。
- AI 辅助内容生成：利用内置 AI 节点自动撰写邮件、总结文档或分析客户反馈。
- 自动化运维与监控：定期检查服务器状态或数据库备份，并在异常发生时通过多种渠道发送通知。

4. **技术亮点**
- 基于 TypeScript 开发，类型安全且易于扩展和二次开发。
- 原生支持 MCP（Model Context Protocol），能够高效地与外部 AI 模型及上下文进行交互。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197995 | 🍴 59628 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现“人人可用”的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，帮助用户将精力集中在真正重要的事务上。

2. **核心功能**
*   具备自主规划与执行复杂任务的能力，实现真正的自主代理操作。
*   支持多种大型语言模型（LLM）后端，包括 OpenAI、Claude 和 Llama 等。
*   提供丰富的扩展接口和工具集，便于用户自定义和集成外部资源。
*   拥有活跃的社区生态，持续迭代以增强 Agent 的稳定性与智能水平。

3. **适用场景**
*   自动化网页研究、数据收集与信息整理工作流。
*   作为个人智能助手，自动处理邮件、日程安排或文件管理。
*   开发者用于测试和构建基于 LLM 的复杂多步应用程序原型。

4. **技术亮点**
*   采用模块化架构设计，灵活支持多种 LLM API 接入。
*   强调“自主代理（Agentic AI）”范式，通过自我反思与修正机制提升任务完成质量。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185683 | 🍴 46069 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166361 | 🍴 21491 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164271 | 🍴 30443 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157299 | 🍴 46186 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 155996 | 🍴 8871 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152390 | 🍴 9653 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

