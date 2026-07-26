# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时框架，允许开发者在 TypeScript 中直接编排复杂的业务流程。它通过将语义处理任务委派给可替换的 Agent 运行时，实现了逻辑编排与智能执行的解耦。

2. **核心功能**
*   提供基于 TypeScript 的原生动态工作流运行时环境。
*   支持将语义推理和复杂任务委托给可插拔的 Agent 后端。
*   实现业务编排逻辑与 AI 执行引擎的分离，提高系统灵活性。
*   兼容多种大型语言模型（LLM）及 AI 代理运行时。

3. **适用场景**
*   需要动态调整执行路径的复杂 AI 应用开发。
*   希望将 TypeScript 业务逻辑与不同 AI 后端解耦的企业级项目。
*   构建可扩展的多智能体协作系统。
*   快速原型化涉及 LLM 调用的动态工作流。

4. **技术亮点**
*   采用“编排与执行分离”架构，通过可替换的 Agent 运行时适应不同的语义需求。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 72 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- 1. **中文简介**
这是一个基于 Python 的 MCP（Model Context Protocol）服务器，允许 AI 智能体通过 Open Cluster Management 中心操作多集群 Kubernetes 环境。它在模型与底层集群之间建立了策略管理、审批流程和审计机制，确保操作的合规性与安全性。

2. **核心功能**
- 通过 MCP 协议实现 AI 智能体对多集群 Kubernetes 环境的直接操作与控制。
- 集成 Open Cluster Management (OCM) 作为中央枢纽，统一管理多个集群资源。
- 提供策略执行、人工或自动化审批以及完整的操作审计日志功能。
- 采用 Python 开发，具备良好的可扩展性和社区兼容性。

3. **适用场景**
- 企业级多云或混合云 Kubernetes 集群的统一 AI 运维与管理。
- 需要严格合规审查和审计追踪的高安全级别容器化应用部署流程。
- 利用自然语言驱动的基础设施即代码（IaC）自动化工具链开发。
- 在受控环境中测试 AI 智能体对复杂分布式系统的干预能力。

4. **技术亮点**
- 创新性地将 MCP 标准应用于 Kubernetes 集群管理，降低了 AI 与基础设施交互的门槛。
- 强调“人在回路”（Human-in-the-loop）的安全机制，通过策略和审批防止 AI 误操作。
- 利用 OCM 的多集群管理能力，实现了从单一集群到全局舰队视图的无缝扩展。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 36 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 开发的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图片进行深度分析。它能将视觉描述提取并结构化为优化后的 JSON 格式提示词，专为生成式 AI 设计。

2. **核心功能**
- 支持使用本地 Ollama LLM 分析文本和图像数据。
- 将视觉内容自动提取并转化为结构化的 JSON 提示词。
- 内置 SQLite 数据库，方便用户管理和编辑生成的提示词。
- 提供可调整的 VRAM 硬件配置文件，以适配不同显卡性能。
- 集成 ComfyUI 节点，可直接调用数据库中的提示词工作流。

3. **适用场景**
- 需要高效批量处理图像并生成标准化 AI 绘画提示词的设计师。
- 希望在不依赖云端 API 的情况下，通过本地模型保护数据隐私的开发者。
- 使用 ComfyUI 工作流，且需要从结构化数据库中动态获取提示词的 AI 艺术创作者。
- 希望根据硬件显存情况优化推理性能的本地大模型部署人员。

4. **技术亮点**
- 实现了本地化推理与结构化数据输出（JSON）的无缝结合。
- 通过 ComfyUI 节点扩展了提示词在可视化工作流中的应用能力。
- 内置 SQLite 存储机制，解决了非结构化视觉描述到结构化数据的转换难题。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 33 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
该项目构建了一个涵盖美股与A股的AI产业链股票池，支持通过主动发现和策略压力进行动态追踪。它具备一键部署能力，旨在为投资者提供便捷的AI领域投资研究工具。

2. **核心功能**
*   建立美股与A股AI产业链股票的映射关系，实现跨市场联动分析。
*   提供主动式股票发现机制，帮助挖掘潜在的AI相关投资机会。
*   集成政策压力分析，评估宏观政策对AI板块的影响。
*   支持一键快速部署，降低技术门槛，方便用户快速搭建个人研究环境。

3. **适用场景**
*   AI产业链投资者需要同时监控美股科技巨头与A股相关概念股的市场表现。
*   研究人员利用政策风向和行业动态，快速筛选具有潜力的AI标的股票。
*   希望快速搭建自动化股票监测工具的开发者或量化爱好者。

4. **技术亮点**
*   基于Cloudflare Workers和Vercel实现 Serverless 架构的一键部署，具备高可用性和低延迟特性。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 28 | 🍴 16 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
Verity-JE-Mod 是一款适用于 Minecraft Java 版（1.21+）的模组，新增了自定义维度、生物群系、世界生成机制以及一个拥有语音演出、背景故事和多阶段 AI 的新怪物。该模组支持 Forge 和 Fabric 加载器，在 Modrinth 平台免费下载，但不兼容基岩版。

2. **核心功能**
*   引入具备多阶段 AI、语音演出和详细背景故事的全新敌对生物。
*   添加全新的自定义维度、生物群系及独特的世界生成算法。
*   兼容 Minecraft Java 版 1.21+ 版本，支持 Forge 和 Fabric 两种主流加载器。
*   提供丰富的游戏进程引导与探索内容，增强游戏的可玩性。

3. **适用场景**
*   **模组包整合**：适合“All the Mods”或“Skyblock”等需要丰富新内容和挑战的模组整合包。
*   **硬核生存玩家**：适合喜欢面对具有复杂 AI 和背景设定的高难度怪物挑战的玩家。
*   **世界探索爱好者**：适合希望体验全新维度结构和独特生物群系地貌的玩家。

4. **技术亮点**
*   实现了具备多阶段行为逻辑的高级 AI 系统，并集成了角色语音演出技术。
- 链接: https://github.com/veritymodminecraft/Verity-JE-Mod-Minecraft
- ⭐ 25 | 🍴 0 | 语言: Java
- 标签: 1-16-5, 1-8, all-the-mods-modpack, allthemods, evernym-verity

### Cursor-Grok-4.5-xAI-free
- 描述: Cursor Grok 4.5 free xAI AI desktop app on Windows, macOS and Linux. IDE-style coding integration, real-time web search, grok 4.5 cursor mode. Competitive pricing vs GPT and Claude. Access without X Premium or Supergrok subscription. Download the latest release now.
- 链接: https://github.com/cursorgrok45free/Cursor-Grok-4.5-xAI-free
- ⭐ 24 | 🍴 0 | 语言: TypeScript
- 标签: ai-powered-applications, composer-2-5, cursor-ai-assistant, cursor-ai-project-rules, cursor-api

### Claude-Code-Sonnet-5-Free-Desktop
- 描述: Claude Code Sonnet 5 desktop free AI coding assistant on Windows, macOS and Linux, no API key needed. Benchmarks above Sonnet 4.6 at lower cost than Opus 5. Beats GitHub Copilot on context window, compares favorably vs Fable 5 on speed. Download and start coding.
- 链接: https://github.com/claudesonnet5free/Claude-Code-Sonnet-5-Free-Desktop
- ⭐ 24 | 🍴 0 | 语言: TypeScript
- 标签: anthropic-, claude-4-opus, claude-5-sonnet, claude-code-desktop, claude-code-prompts

### Tok123
- 描述: Tok123 v1.0 · 中文网址目录与任务路线平台，支持 AI 工具导航、行业资源库、内容精选站和专题路线。内置 39 个网址与 GEO 专题，配套可安装的管理员 Skill。
- 链接: https://github.com/yaojingang/Tok123
- ⭐ 22 | 🍴 5 | 语言: TypeScript

### ai-excel
- 描述: 利用ai使用自然语言操作excel，不再需要记公式
- 链接: https://github.com/ns2250225/ai-excel
- ⭐ 14 | 🍴 3 | 语言: TypeScript

### ai-cost-history-hub
- 描述: Local AI coding-agent history + API cost analytics (loopback-only).
- 链接: https://github.com/zheyan2517/ai-cost-history-hub
- ⭐ 14 | 🍴 2 | 语言: TypeScript
- 标签: coding-agents, cost-tracking, dashboard, local-first, open-source

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、情感分析）到高级应用（如知识图谱构建、语音识别、聊天机器人）的广泛内容。它集成了大量开源数据集、预训练模型及实用工具，旨在为开发者提供一站式的中英文 NLP 解决方案。

2. **核心功能**
- **基础文本处理**：提供中英文敏感词过滤、繁简转换、标点修复、文本纠错及多种分词和词性标注工具。
- **信息抽取与实体识别**：支持手机号、身份证、邮箱等特定信息抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
- **语义分析与生成**：包含词汇情感值计算、句子相似度匹配、自动摘要生成、关键词提取及基于 GPT/BERT 的文本生成能力。
- **多模态与垂直领域数据**：整合了中文语音识别（ASR）、OCR 文字识别、医疗/金融/法律等垂直领域的专用语料库和知识图谱资源。
- **模型与框架集成**：汇总了 spaCy、Transformers、Kashgari 等主流 NLP 框架的中文适配方案及大量预训练语言模型（如 BERT, ALBERT, RoBERTa）。

3. **适用场景**
- **内容安全审核**：利用敏感词库和情感分析工具，快速搭建互联网平台的内容过滤和舆情监控系统。
- **智能客服与对话系统**：参考其中的聊天机器人代码、知识库构建方法及意图识别模型，开发企业级智能问答助手。
- **数据标注与模型训练**：使用其提供的海量中文标注数据集（如 CLUENER、NER 数据集）和标注工具，训练高精度的下游 NLP 模型。
- **跨领域信息结构化**：借助其抽取工具和知识图谱资源，从非结构化文本（如新闻、病历、法律文书）中提取结构化实体和关系。

4. **技术亮点**
该项目最大的亮点在于其**极高的资源整合度与覆盖面**，不仅提供了代码实现，还汇集了数十个高质量的中文 NLP 数据集、预训练模型权重及垂直领域知识图谱，极大地降低了中文 NLP 项目的起步门槛和数据获取成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82063 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和代码参考，是人工智能领域的优质资源库。

2. **核心功能**
- 提供大量现成的AI项目代码示例，支持快速上手与二次开发。
- 覆盖机器学习、深度学习、CV和NLP等多个主流AI子领域。
- 以“Awesome List”形式组织，便于用户分类浏览和查找特定技术栈的项目。
- 包含Python等语言的完整实现代码，具备较高的可复用性。

3. **适用场景**
- AI初学者用于学习各子领域的基本算法实现和项目结构。
- 工程师在开发中遇到具体难题时，参考类似项目的解决方案。
- 研究人员或学生寻找灵感，快速搭建原型或进行对比实验。

4. **技术亮点**
- 资源规模庞大，集成了500个高质量项目，具有极高的参考价值。
- 标签体系完善，清晰区分了不同技术方向（如CV、NLP）和项目类型。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习及机器学习模型的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。该项目以轻量级和广泛的兼容性著称，便于开发者快速理解模型内部逻辑。

2. **核心功能**
- 支持可视化 Keras、PyTorch、TensorFlow、ONNX 等数十种主流模型格式。
- 提供交互式界面，允许用户展开、折叠或搜索模型中的特定层和节点。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定场景格式。
- 无需安装复杂环境，既可作为桌面应用也可作为网页服务运行。
- 自动解析模型结构并展示张量形状、参数及计算流向。

3. **适用场景**
- 模型调试：检查神经网络层连接是否正确，排查结构错误。
- 教学演示：向非技术人员或学生直观展示深度学习模型的工作原理。
- 格式转换验证：确认模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 后结构保持一致。
- 部署前审查：在将模型集成到移动应用或嵌入式设备前，分析其复杂度和资源需求。

4. **技术亮点**
- 极高的格式兼容性，覆盖了从传统 ML 到最新大模型（如 Safetensors）的广泛生态。
- 开源且跨平台，基于 Electron 构建，可在 Windows、macOS 和 Linux 上无缝使用。
- 社区活跃，星标数高（33,000+），表明其在 AI 开发者群体中拥有极高的认可度和实用性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型格式的无缝转换与共享。通过标准化表示，开发者可以更方便地在各种硬件和平台间迁移模型。

**2. 核心功能**
*   **框架间互操作性**：支持将模型从主流框架（如 PyTorch、TensorFlow、Keras）导出为标准 ONNX 格式。
*   **跨平台部署**：允许模型在不同后端引擎（如 ONNX Runtime、TensorRT、OpenVINO）上高效运行。
*   **统一模型表示**：提供标准化的计算图结构，确保模型定义在不同环境中保持一致。
*   **生态兼容性**：广泛兼容 Scikit-learn 等传统机器学习库及各类深度学习框架。

**3. 适用场景**
*   **生产环境部署**：将训练好的模型转换为轻量级运行时环境，以加速推理过程。
*   **跨框架迁移**：在保留模型性能的前提下，从一种开发框架切换到另一种框架。
*   **硬件加速集成**：将通用模型适配到特定硬件加速器（如 GPU、NPU）以提升执行效率。

**4. 技术亮点**
*   **开放标准地位**：作为 AI 领域事实上的通用交换格式，被 Microsoft、Facebook、Amazon 等科技巨头共同维护和支持。
- 链接: https://github.com/onnx/onnx
- ⭐ 21215 | 🍴 3975 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ML Engineering Open Book》是一本关于机器学习工程实践的开源指南。它系统地涵盖了从模型训练、推理到大规模部署的全流程关键技术。该项目旨在为工程师提供构建可扩展、高效机器学习系统的实用参考。

2. **核心功能**
- 深入讲解分布式训练策略及PyTorch等框架的最佳实践。
- 提供大规模语言模型（LLM）的高效推理优化与部署方案。
- 涵盖MLOps全流程，包括集群管理（如Slurm）、存储和网络优化。
- 介绍模型调试、性能剖析及可扩展性设计的实用技巧。

3. **适用场景**
- 开发需要高吞吐量和低延迟的大规模语言模型推理服务。
- 在超算集群或GPU集群上配置和优化分布式深度学习训练环境。
- 构建端到端的MLOps流水线，实现模型的自动化部署与监控。
- 解决深度学习系统中的性能瓶颈、内存溢出或网络通信问题。

4. **技术亮点**
- 内容紧跟前沿，特别针对Transformer架构和LLM的工程挑战提供了具体解决方案。
- 结合了理论概念与实际操作，涵盖从底层硬件（GPU/网络）到上层框架的多层优化细节。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18469 | 🍴 1182 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17339 | 🍴 2118 | 语言: 未知
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
- ⭐ 11599 | 🍴 910 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10677 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和代码参考，是人工智能领域的优质资源库。

2. **核心功能**
- 提供大量现成的AI项目代码示例，支持快速上手与二次开发。
- 覆盖机器学习、深度学习、CV和NLP等多个主流AI子领域。
- 以“Awesome List”形式组织，便于用户分类浏览和查找特定技术栈的项目。
- 包含Python等语言的完整实现代码，具备较高的可复用性。

3. **适用场景**
- AI初学者用于学习各子领域的基本算法实现和项目结构。
- 工程师在开发中遇到具体难题时，参考类似项目的解决方案。
- 研究人员或学生寻找灵感，快速搭建原型或进行对比实验。

4. **技术亮点**
- 资源规模庞大，集成了500个高质量项目，具有极高的参考价值。
- 标签体系完善，清晰区分了不同技术方向（如CV、NLP）和项目类型。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习及机器学习模型的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。该项目以轻量级和广泛的兼容性著称，便于开发者快速理解模型内部逻辑。

2. **核心功能**
- 支持可视化 Keras、PyTorch、TensorFlow、ONNX 等数十种主流模型格式。
- 提供交互式界面，允许用户展开、折叠或搜索模型中的特定层和节点。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定场景格式。
- 无需安装复杂环境，既可作为桌面应用也可作为网页服务运行。
- 自动解析模型结构并展示张量形状、参数及计算流向。

3. **适用场景**
- 模型调试：检查神经网络层连接是否正确，排查结构错误。
- 教学演示：向非技术人员或学生直观展示深度学习模型的工作原理。
- 格式转换验证：确认模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 后结构保持一致。
- 部署前审查：在将模型集成到移动应用或嵌入式设备前，分析其复杂度和资源需求。

4. **技术亮点**
- 极高的格式兼容性，覆盖了从传统 ML 到最新大模型（如 Safetensors）的广泛生态。
- 开源且跨平台，基于 Electron 构建，可在 Windows、macOS 和 Linux 上无缝使用。
- 社区活跃，星标数高（33,000+），表明其在 AI 开发者群体中拥有极高的认可度和实用性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目为深度学习和机器学习研究人员提供了 essential（关键/必备）的速查手册（Cheat Sheets）。内容涵盖了从基础数学库到主流深度学习框架的核心语法与函数参考。旨在帮助研究者快速查阅常用代码片段，提高开发效率。

**2. 核心功能**
- 提供机器学习基础库（如 NumPy、SciPy）的常用函数速查。
- 涵盖数据可视化库（如 Matplotlib）的代码示例与参数说明。
- 包含深度学习框架（如 Keras）的关键 API 与使用技巧。
- 整理人工智能领域相关的概念性备忘与最佳实践。
- 以简洁清晰的格式呈现，便于快速检索和理解。

**3. 适用场景**
- 研究人员在进行实验设计时，快速回顾特定算法或库的用法。
- 开发者在编写代码遇到语法遗忘时，作为即时参考手册。
- 初学者学习机器学习工具链时，用于系统性地熟悉常用库。
- 团队内部技术分享或新员工入职培训中的参考资料。

**4. 技术亮点**
- 聚焦于高频使用的核心功能，去除了冗余信息，提升查阅效率。
- 覆盖从底层数据处理到高层模型构建的全栈技术点。
- 内容经过精选，直接对应 Medium 文章推荐的标准学习路径。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
这是一个全面的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户入门并提升就业竞争力。内容涵盖Python、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等热门技术领域。

2. **核心功能**
*   提供结构化的AI学习路径，整合从基础到进阶的核心知识点。
*   包含近200个实战案例和项目代码，支持动手实践。
*   免费开放配套学习资料和教材，降低学习门槛。
*   覆盖主流AI框架（如PyTorch, TensorFlow, Keras）及数据处理工具（Pandas, NumPy）。
*   聚焦算法实现与行业应用，强调就业导向的技能训练。

3. **适用场景**
*   希望系统掌握人工智能知识体系的初学者或转行人员。
*   需要通过大量实战项目提升编程能力和解决实际问题能力的学习者。
*   寻找高质量开源案例以补充课堂理论知识的计算机专业学生。
*   希望快速了解AI前沿技术栈（如CV、NLP）并搭建个人作品集的求职者。

4. **技术亮点**
*   高度集成的技术栈覆盖，兼容PyTorch、TensorFlow、Caffe等多种主流深度学习框架。
*   注重理论与实践结合，通过海量实战案例强化对numpy、pandas、matplotlib等工具的实际应用能力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它支持从传统机器学习到深度学习的多种任务，让开发者能够更专注于数据而非底层代码实现。

**2. 核心功能**
*   **低代码体验**：通过声明式配置即可快速构建和训练复杂的深度学习模型，大幅降低开发门槛。
*   **广泛的模型支持**：原生支持 LLM 微调（如 Llama、Mistral）以及传统的计算机视觉和自然语言处理模型。
*   **数据-centric 工作流**：提供端到端的数据预处理、特征工程及模型评估工具，强调数据质量对模型性能的影响。
*   **多后端兼容**：基于 PyTorch 构建，同时兼容 Hugging Face Transformers，方便集成现有的开源模型库。

**3. 适用场景**
*   **LLM 微调与应用**：针对特定领域数据对 Llama、Mistral 等大语言模型进行高效微调或推理部署。
*   **结构化数据预测**：在表格型数据上进行分类、回归或聚类分析，无需编写复杂的深度学习代码。
*   **多模态实验**：快速验证包含文本、图像或音频等不同模态数据的混合模型架构。

**4. 技术亮点**
*   **自动化特征工程**：自动识别数据类型并应用合适的预处理策略，减少手动特征设计的繁琐工作。
*   **可扩展的架构**：模块化设计允许用户轻松插入自定义层或损失函数，适应各种前沿研究需求。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11746 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9148 | 🍴 1237 | 语言: Python
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
- ⭐ 6294 | 🍴 756 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、情感分析）到高级应用（如知识图谱构建、语音识别、聊天机器人）的广泛内容。它集成了大量开源数据集、预训练模型及实用工具，旨在为开发者提供一站式的中英文 NLP 解决方案。

2. **核心功能**
- **基础文本处理**：提供中英文敏感词过滤、繁简转换、标点修复、文本纠错及多种分词和词性标注工具。
- **信息抽取与实体识别**：支持手机号、身份证、邮箱等特定信息抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
- **语义分析与生成**：包含词汇情感值计算、句子相似度匹配、自动摘要生成、关键词提取及基于 GPT/BERT 的文本生成能力。
- **多模态与垂直领域数据**：整合了中文语音识别（ASR）、OCR 文字识别、医疗/金融/法律等垂直领域的专用语料库和知识图谱资源。
- **模型与框架集成**：汇总了 spaCy、Transformers、Kashgari 等主流 NLP 框架的中文适配方案及大量预训练语言模型（如 BERT, ALBERT, RoBERTa）。

3. **适用场景**
- **内容安全审核**：利用敏感词库和情感分析工具，快速搭建互联网平台的内容过滤和舆情监控系统。
- **智能客服与对话系统**：参考其中的聊天机器人代码、知识库构建方法及意图识别模型，开发企业级智能问答助手。
- **数据标注与模型训练**：使用其提供的海量中文标注数据集（如 CLUENER、NER 数据集）和标注工具，训练高精度的下游 NLP 模型。
- **跨领域信息结构化**：借助其抽取工具和知识图谱资源，从非结构化文本（如新闻、病历、法律文书）中提取结构化实体和关系。

4. **技术亮点**
该项目最大的亮点在于其**极高的资源整合度与覆盖面**，不仅提供了代码实现，还汇集了数十个高质量的中文 NLP 数据集、预训练模型权重及垂直领域知识图谱，极大地降低了中文 NLP 项目的起步门槛和数据获取成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82063 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目曾入选 ACL 2024，旨在简化大型模型的适配流程。它集成了多种先进的微调技术，为开发者提供了一站式的解决方案。

2. **核心功能**
*   支持 100+ 种主流 LLM 和 VLM 的统一高效微调。
*   内置多种参数高效微调方法，如 LoRA、QLoRA 及全参数微调。
*   集成 RLHF（基于人类反馈的强化学习）和指令微调功能。
*   支持量化部署，降低显存占用并提升推理效率。
*   提供简洁的命令行接口和配置文件，便于快速实验与复现。

3. **适用场景**
*   研究人员或开发者需要对多种不同架构的大模型进行基准测试和对比实验。
*   需要在有限显存资源下，通过 QLoRA 等技术对大型模型进行低成本微调。
*   希望快速构建具备特定领域知识或遵循特定指令风格的定制模型。
*   需要实现从预训练到 RLHF 对齐的完整模型训练流水线。

4. **技术亮点**
*   **高度兼容性**：统一了 Transformers 库中众多模型的后端处理逻辑，屏蔽了底层差异。
*   **极致效率**：通过混合精度训练和先进的量化策略，显著降低了计算资源和显存需求。
*   **前沿算法集成**：原生支持最新的高效微调范式（如 LoRA+、DoRA）及多模态训练。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73523 | 🍴 8987 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的通用人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目通过Jupyter Notebook提供互动式学习体验，涵盖了从基础机器学习到深度学习的广泛主题。

2. **核心功能**
*   提供结构化的12周学习计划，将复杂概念分解为24个易于理解的课时。
*   主要采用Jupyter Notebook格式，支持代码执行与即时反馈的学习方式。
*   内容覆盖全面，包括机器学习、深度学习、计算机视觉和自然语言处理等核心领域。
*   面向初学者设计，强调“人人可学”的理念，降低AI技术的学习门槛。

3. **适用场景**
*   AI初学者希望系统性地从零开始构建人工智能知识体系。
*   教育工作者或培训讲师寻找现成的、模块化的AI教学大纲和实验材料。
*   学生或职场人士希望在短时间内快速了解AI基本概念及常见算法应用。

4. **技术亮点**
*   由微软发起并维护（Microsoft For Beginners系列），具有极高的社区认可度和活跃度（近5.3万星标）。
*   内容紧跟前沿技术，涵盖CNN、RNN、GAN等主流深度学习架构的基础应用。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52898 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建人工智能系统，帮助学习者深入理解AI原理。它强调“学习、构建并部署”的完整闭环，让开发者能够亲手打造服务于他人的AI应用。

2. **核心功能**
- 涵盖从基础机器学习到前沿生成式AI的全栈技术栈教学。
- 提供基于Python、Rust和TypeScript等多种语言的实战代码示例。
- 深入讲解智能体（Agents）、MCP协议及群体智能等高级架构设计。
- 结合计算机视觉与NLP技术，实现复杂的多模态AI应用开发。

3. **适用场景**
- AI初学者希望系统性地从零掌握深度学习与大模型底层逻辑。
- 工程师需要参考生产级代码，学习如何构建和部署独立的AI智能体。
- 研究人员探索多语言（如Rust/TS）在高性能AI基础设施中的应用。

4. **技术亮点**
- 跨语言技术融合：不仅限于Python，还整合了Rust的性能优势与TypeScript的前端能力。
- 紧跟前沿趋势：包含MCP（Model Context Protocol）和Swarm Intelligence等最新AI工程概念。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43684 | 🍴 7344 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战及深度学习的综合性资源库，内容延伸至线性代数基础与PyTorch等框架应用。它整合了NLTK自然语言处理工具与TensorFlow 2，旨在提供从理论到代码的完整学习路径。

2. **核心功能**
*   集成经典算法（如SVM、Kmeans、Adaboost）与深度学习模型（DNN、RNN、LSTM）的实战代码。
*   提供基于Scikit-learn和PyTorch的数据挖掘及推荐系统实现示例。
*   包含NLP领域的基础库（NLTK）及关联规则挖掘算法（Apriori、FP-Growth）。
*   融合数学基础（线性代数）与统计方法（PCA、SVD），辅助理解机器学习底层逻辑。

3. **适用场景**
*   初学者系统学习机器学习算法原理及其Python实现。
*   数据科学家或工程师快速查阅特定算法（如回归、分类）的代码模板。
*   需要进行自然语言处理（NLP）或推荐系统开发的开发者参考基准案例。

4. **技术亮点**
*   覆盖范围广：从传统统计学习到前沿深度学习框架（TF2/PyTorch）均有涉及。
*   理论与实践结合：不仅提供算法代码，还强调线性代数等数学基础的支持。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42416 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33773 | 🍴 4698 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28826 | 🍴 3517 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26018 | 🍴 2952 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21765 | 🍴 3310 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22597 | 🍴 2118 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16386 | 🍴 3775 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12930 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11290 | 🍴 1208 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8876 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3299 | 🍴 404 | 语言: Python
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
- ⭐ 384212 | 🍴 80722 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261491 | 🍴 23342 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220821 | 🍴 42086 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198097 | 🍴 59645 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185697 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166388 | 🍴 21496 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164280 | 🍴 30448 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157310 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156339 | 🍴 8888 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152436 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

