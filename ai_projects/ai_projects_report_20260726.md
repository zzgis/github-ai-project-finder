# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### OptMem
- 1. **中文简介**
OptMem 专为 AI 智能体提供永久性记忆功能。它仅需一个包含 426 个 token 的提示词脚本，即可实现即插即用的部署体验。

2. **核心功能**
*   赋予 AI 智能体长期且持久的记忆能力。
*   通过极简的提示词脚本实现功能集成。
*   支持即插即用，无需复杂配置即可运行。
*   显著降低实现智能体记忆的算力与开发成本。

3. **适用场景**
*   需要记住用户偏好或历史对话的多轮交互式聊天机器人。
*   依赖长期上下文进行决策的任务型 AI 智能体。
*   资源受限环境下对模型记忆能力有轻量化需求的项目。

4. **技术亮点**
*   以极低的 Token 消耗（仅 426 个）实现高效的记忆持久化。
- 链接: https://github.com/VictorTaelin/OptMem
- ⭐ 196 | 🍴 10 | 语言: Python

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时框架，旨在让编排逻辑完全保留在 TypeScript 中。它通过将语义处理任务委派给可替换的 Agent 运行时，实现了工作流与智能代理的解耦。

2. **核心功能**
*   提供基于 TypeScript 的动态工作流运行时环境，支持灵活的流程编排。
*   采用可插拔架构，允许用户替换底层的 Agent 运行时以适配不同语义需求。
*   实现编排层与语义执行层的分离，保持代码逻辑清晰且易于维护。
*   支持动态工作流特性，能够根据运行时状态调整执行路径。

3. **适用场景**
*   需要高度定制化编排逻辑且依赖 TypeScript 技术栈的 AI 应用开发。
*   希望将工作流控制与具体 LLM/Agent 实现解耦，以便灵活切换后端服务的场景。
*   构建复杂的 AI 编码助手或多步骤智能体协作系统。

4. **技术亮点**
*   原生支持 Bun 运行时，提供高性能的执行环境。
*   基于 TypeScript 的类型安全优势，确保编排逻辑的健壮性。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 75 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- 1. **中文简介**
这是一个基于 MCP（模型上下文协议）的服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心来操作多集群 Kubernetes 资源。它在 AI 模型与底层集群之间引入了策略控制、审批流程和审计机制，确保了操作的安全性与合规性。

2. **核心功能**
*   提供 MCP 接口，使 AI 智能体能够直接连接并管理 Kubernetes 集群。
*   集成 OCM 中心，实现对多集群环境的统一调度和操作。
*   内置策略引擎，强制约束 AI 的操作行为以符合安全规范。
*   支持审批工作流，关键操作需经过人工或预设规则确认后方可执行。
*   记录完整的审计日志，确保所有 AI 发起的操作可追溯且透明。

3. **适用场景**
*   企业级多云 Kubernetes 环境的自动化运维与管理。
*   需要严格合规性和权限控制的 AI 驱动型 DevOps 流程。
*   利用自然语言指令进行复杂集群变更的安全测试环境。
*   构建具备自我修复能力但受控于人类监督的智能基础设施系统。

4. **技术亮点**
*   实现了 AI 智能体与企业级集群管理标准（OCM）的无缝对接。
*   在提升自动化效率的同时，通过“策略+审批+审计”三重机制解决了 AI 操作集群的安全信任问题。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 37 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能够将视觉描述提取并结构化地转化为生成式 AI 所需的优化 JSON 提示词。该应用内置 SQLite 数据库以支持提示词编辑，并提供可调整的显存硬件配置文件。

2. **核心功能**
- 使用本地 Ollama LLM 分析文本与图像内容。
- 将视觉描述自动提取并转换为结构化的 JSON 格式提示词。
- 内置 SQLite 数据库，方便用户存储、管理和编辑提示词。
- 提供可调节的 VRAM（显存）硬件配置文件，适配不同算力设备。
- 包含 ComfyUI 节点，可直接调用数据库中的提示词进行工作流集成。

3. **适用场景**
- 需要高效批量生成结构化提示词的 Stable Diffusion 或 Midjourney 用户。
- 希望在不依赖云端 API 的情况下，利用本地资源处理敏感或私有数据的开发者。
- 使用 ComfyUI 搭建复杂工作流，且需要模块化调用和管理提示词库的用户。
- 显存受限但需运行本地 LLM 进行辅助生成的电脑配置调整场景。

4. **技术亮点**
- 实现了从非结构化视觉/文本数据到标准化 JSON 提示词的自动化转换。
- 通过本地 Ollama 部署保障了数据隐私及离线运行的可行性。
- 深度集成 ComfyUI 生态，提升了工作流的灵活性和复用性。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 35 | 🍴 3 | 语言: Python

### ai-stock-pool
- **1. 中文简介**
该项目是一个聚焦人工智能产业链的股票池，支持美股与A股的映射关联、主动发现及政策压力分析。它提供了一键部署功能，旨在帮助投资者高效追踪AI领域的投资机会。

**2. 核心功能**
- 实现美股与A股在AI产业链上的映射与联动分析。
- 具备主动挖掘潜力标的及政策影响评估的能力。
- 支持通过Cloudflare Workers或Vercel进行一键快速部署。
- 整合Arxiv等学术资源以辅助投资研究决策。

**3. 适用场景**
- AI行业研究员进行跨市场（中美）产业链投资梳理。
- 量化开发者快速搭建并测试基于AI主题的选股策略原型。
- 关注政策导向的投资者实时监测AI板块的政策压力变化。

**4. 技术亮点**
- 采用Serverless架构（Cloudflare Workers/Vercel），实现低成本且极速的全球边缘部署。
- 结合学术前沿（Arxiv）与市场数据，提供多维度的投资研究视角。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 28 | 🍴 16 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Verity-JE-Mod-Minecraft
- 描述: Verity JE Mod Minecraft Java Edition mod with a new monster, custom dimensions, biomes and world generation for 1.21+. Not available for Bedrock. The creature has voice acting, lore and a multi-phase AI. Available on Modrinth for Forge and Fabric. Download free.
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
- ⭐ 23 | 🍴 5 | 语言: TypeScript

### aar-loop
- 描述: Run an After Action Review after any AI session and write concrete lessons so your agent stops repeating mistakes. A manual Reflexion loop, built on the US Army's AAR method.
- 链接: https://github.com/coopersimson96/aar-loop
- ⭐ 19 | 🍴 2 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个功能极其丰富的自然语言处理（NLP）资源汇总库，集成了敏感词检测、语言识别、实体抽取（手机/身份证/邮箱等）、情感分析及繁简转换等基础工具。它不仅提供各类专业词库（如汽车、医疗、法律、地名等）和预训练模型资源，还收录了大量中文 NLP 竞赛方案、数据集、论文解读及开源项目代码。该项目旨在成为中文 NLP 开发者的全能工具箱，涵盖从数据预处理、知识图谱构建到深度学习模型应用的全链路资源。

### 2. 核心功能
- **基础 NLP 工具与清洗**：提供中英文敏感词过滤、语言检测、停用词、反动词表及繁简体转换，支持手机号、身份证、邮箱等正则抽取。
- **海量领域词库与知识库**：内置中日文人名、中文缩写、职业、品牌、成语、古诗词及医学、法律、财经等专业领域词库，并包含新华字典 API。
- **数据增强与语料资源**：收录 EDA 数据增强工具、多种中文闲聊语料、问答数据集（百度知道等）及谣言数据库，辅助模型训练。
- **前沿模型与算法汇总**：整合 BERT、GPT、ALBERT 等预训练模型资源，提供命名实体识别（NER）、关系抽取、文本摘要及相似度计算的代码模板。
- **行业解决方案与竞赛复盘**：汇集中文 NLP 竞赛 Top 方案、简历筛选系统、对话机器人框架及知识图谱构建工具，展示实际应用场景。

### 3. 适用场景
- **智能客服与聊天机器人开发**：利用其中的闲聊语料、对话系统及意图识别资源，快速搭建具备多轮对话能力的智能助手。
- **内容安全与舆情监控平台**：通过集成敏感词库、暴恐词表及情感分析工具，实现对企业发布内容的自动审核和情感倾向监测。
- **金融/医疗垂直领域信息抽取**：借助专业的金融、医疗词库及 NER 模型代码，构建针对特定行业文档的结构化数据提取系统。
- **NLP 教学与学术研究参考**：作为学生和研究人员的学习仓库，获取最新的中英文 NLP 数据集、论文解读及基准测试排行榜。

### 4. 技术亮点
- **资源聚合度极高**：不仅包含代码，还整合了数据集、预训练模型、API 接口及行业报告，是中文 NLP 领域的“百科全书”。
- **覆盖全生命周期**：从最基础的分词、词性标注，到中级的实体抽取、情感分析，再到高级的知识图谱构建和大模型微调，全覆盖主流 NLP 任务。
- **紧跟前沿技术**：及时收录了 BERT、GPT-2、ALBERT、RoBERTa 等最新预训练模型的应用示例及开源实现，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI项目代码的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例和参考资源，助力技术学习与工程实践。

2. **核心功能**
- 提供大量经过筛选的AI相关项目代码，便于快速学习和复现。
- 覆盖机器学习、深度学习、计算机视觉及NLP等多个主流技术分支。
- 包含“awesome”标签内容，确保项目质量较高且具备代表性。
- 以Python为主要实现语言，符合当前AI开发的主流技术栈。
- 结构化整理项目资源，降低开发者寻找优质开源案例的时间成本。

3. **适用场景**
- AI初学者希望系统性地通过代码示例学习各分支技术。
- 开发者在需要特定算法实现时，寻找可参考的开源代码模板。
- 研究人员或工程师进行技术调研，快速了解行业内的典型应用案例。
- 教育机构用于教学演示，展示机器学习与深度学习的实际落地效果。

4. **技术亮点**
- 项目规模庞大（500+），覆盖面广，是全面的AI资源索引库。
- 聚焦于“代码即学”的理念，强调实操性和可运行性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持查看多种主流框架生成的模型文件，帮助用户直观地理解模型结构。

2. **核心功能**
- 支持浏览包括 CoreML、Keras、ONNX、PyTorch、TensorFlow 等在内的多种模型格式。
- 提供清晰的图形化界面展示模型层级结构和节点连接关系。
- 兼容桌面应用与网页浏览器，方便在不同环境下使用。
- 能够显示模型中的参数、张量形状及数据流信息。
- 允许用户导出模型可视化为静态图片以便分享或记录。

3. **适用场景**
- 在部署模型前，快速检查并验证神经网络的结构是否正确。
- 调试深度学习算法时，直观定位模型中的异常层或连接错误。
- 向非技术人员或团队展示模型架构，促进技术沟通与协作。
- 对比不同框架（如 TensorFlow 转 ONNX）转换后的模型一致性。

4. **技术亮点**
- 极高的兼容性，广泛支持从传统机器学习到最新大语言模型（如 safetensors）的多种格式。
- 基于 Web 技术构建，实现了跨平台运行且无需安装复杂依赖环境。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在实现不同深度学习框架之间的互操作性。它允许开发者轻松地将模型从一个框架迁移到另一个框架，或部署到各种推理引擎中。这极大地简化了机器学习模型的跨平台协作与部署流程。

**2. 核心功能**
*   提供开放的模型格式标准，支持神经网络结构的通用交换。
*   实现主流深度学习框架（如PyTorch、TensorFlow）间的无缝转换。
*   支持在多种硬件平台和推理引擎上高效部署和优化模型。
*   提供丰富的工具集用于模型检查、转换和性能分析。

**3. 适用场景**
*   **跨框架迁移**：将训练好的模型从PyTorch转换为TensorFlow以进行生产部署。
*   **边缘设备部署**：将大型模型转换为轻量级ONNX格式，以便在移动设备或嵌入式系统上运行。
*   **混合开发环境**：在同一个项目中结合使用多个框架的优势，并通过ONNX连接各部分。

**4. 技术亮点**
*   **开放性**：由微软、Facebook等巨头共同维护的开放标准，拥有广泛的社区支持。
*   **生态兼容性**：原生支持Onnx Runtime，可充分利用加速库提升推理速度。
- 链接: https://github.com/onnx/onnx
- ⭐ 21216 | 🍴 3976 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ml-engineering》是一部关于机器学习工程实践的开源百科。它系统性地涵盖了从底层硬件基础设施到上层模型训练与推理的全栈技术知识。该项目旨在为构建大规模AI系统提供全面且实用的工程指导。

2. **核心功能**
- 提供深度学习训练和推理阶段的性能优化策略与最佳实践。
- 详解分布式训练架构、网络通信及存储IO优化方案。
- 涵盖GPU硬件特性解析、集群管理（如Slurm）及MLOps流程。
- 针对大型语言模型（LLM）的调试、可扩展性及部署进行深入剖析。

3. **适用场景**
- 深度学习工程师在大规模集群上调试和优化模型训练性能。
- MLOps团队构建高可用、可扩展的机器学习基础设施与部署流水线。
- 研究人员探索LLM推理加速、量化技术及资源高效利用方案。
- 工程师学习PyTorch等框架在复杂硬件环境下的底层运行机制。

4. **技术亮点**
- 内容兼具理论深度与工程实操性，直接关联GPU、网络及存储等底层细节。
- 覆盖范围极广，从单机调优延伸至千卡/万卡级集群的分布式系统工程。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18470 | 🍴 1182 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17340 | 🍴 2118 | 语言: 未知
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
这是一个收录了500个AI项目代码的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例和参考资源，助力技术学习与工程实践。

2. **核心功能**
- 提供大量经过筛选的AI相关项目代码，便于快速学习和复现。
- 覆盖机器学习、深度学习、计算机视觉及NLP等多个主流技术分支。
- 包含“awesome”标签内容，确保项目质量较高且具备代表性。
- 以Python为主要实现语言，符合当前AI开发的主流技术栈。
- 结构化整理项目资源，降低开发者寻找优质开源案例的时间成本。

3. **适用场景**
- AI初学者希望系统性地通过代码示例学习各分支技术。
- 开发者在需要特定算法实现时，寻找可参考的开源代码模板。
- 研究人员或工程师进行技术调研，快速了解行业内的典型应用案例。
- 教育机构用于教学演示，展示机器学习与深度学习的实际落地效果。

4. **技术亮点**
- 项目规模庞大（500+），覆盖面广，是全面的AI资源索引库。
- 聚焦于“代码即学”的理念，强调实操性和可运行性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持查看多种主流框架生成的模型文件，帮助用户直观地理解模型结构。

2. **核心功能**
- 支持浏览包括 CoreML、Keras、ONNX、PyTorch、TensorFlow 等在内的多种模型格式。
- 提供清晰的图形化界面展示模型层级结构和节点连接关系。
- 兼容桌面应用与网页浏览器，方便在不同环境下使用。
- 能够显示模型中的参数、张量形状及数据流信息。
- 允许用户导出模型可视化为静态图片以便分享或记录。

3. **适用场景**
- 在部署模型前，快速检查并验证神经网络的结构是否正确。
- 调试深度学习算法时，直观定位模型中的异常层或连接错误。
- 向非技术人员或团队展示模型架构，促进技术沟通与协作。
- 对比不同框架（如 TensorFlow 转 ONNX）转换后的模型一致性。

4. **技术亮点**
- 极高的兼容性，广泛支持从传统机器学习到最新大语言模型（如 safetensors）的多种格式。
- 基于 Web 技术构建，实现了跨平台运行且无需安装复杂依赖环境。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目为深度学习与机器学习研究人员提供了一系列必备的核心知识速查表（Cheat Sheets）。它涵盖了从基础理论到主流框架的关键概念总结，旨在帮助研究者快速回顾和掌握重要技术细节。

**2. 核心功能**
*   提供机器学习与深度学习领域的基础概念速查指南。
*   包含常用Python库（如NumPy、SciPy、Matplotlib）的操作速记。
*   集成深度学习框架（如Keras）的关键用法与代码片段。
*   以简洁的图表或列表形式呈现复杂的技术知识点。

**3. 适用场景**
*   深度学习研究人员在开始新项目前快速复习基础知识。
*   机器学习工程师在日常编码时查阅特定库函数或API用法。
*   学生或初学者作为入门学习的辅助参考资料和笔记补充。

**4. 技术亮点**
*   高度浓缩的知识结构，便于快速检索而非系统学习。
*   覆盖主流工具链（NumPy/SciPy/Matplotlib/Keras），实用性强。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**：Ai-Learn 是一个专注于人工智能领域的学习资源库，整理了近200个实战案例并提供免费配套教材。该项目旨在帮助零基础用户入门，并通过涵盖Python、机器学习、深度学习等热门技术栈助力就业实战。

2. **核心功能**
   - 提供从零基础到就业实战的全方位AI学习路径指导。
   - 收录近200个高质量实战案例以强化动手能力。
   - 免费开放配套教材资源降低学习门槛。
   - 覆盖Python编程、数学基础及主流深度学习框架应用。

3. **适用场景**
   - 希望从零开始系统学习人工智能技术的初学者。
   - 需要通过大量实战案例提升工程落地能力的开发者。
   - 寻求免费优质教材资源以辅助自学或教学的教育者。

4. **技术亮点**
   - 全面整合了PyTorch、TensorFlow、Keras等主流深度学习框架的教学内容。
   - 涵盖计算机视觉（CV）、自然语言处理（NLP）及数据分析等高需求细分领域。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置降低技术门槛，使开发者能够专注于数据与模型设计，而非繁琐的代码实现。该项目基于 PyTorch 等主流深度学习库，提供了高效且易用的模型训练与微调体验。

### 2. **核心功能**
- **低代码/声明式建模**：通过 YAML 或 JSON 配置文件定义模型架构和数据预处理流程，无需编写大量底层代码。
- **多模态支持**：原生支持文本、图像、表格等多种数据类型，适用于自然语言处理（NLP）和计算机视觉任务。
- **自动化微调与训练**：内置对 Llama、Mistral 等流行大模型的微调支持，简化了从预训练到特定领域适配的过程。
- **端到端工作流**：涵盖数据加载、特征工程、模型训练、评估及部署的全生命周期管理。
- **基于 PyTorch 的后端**：充分利用 PyTorch 的灵活性，同时提供高层抽象以加速实验迭代。

### 3. **适用场景**
- **快速原型开发**：数据科学家希望在无需深入深度学习框架细节的情况下，快速验证 AI 模型想法。
- **企业级 LLM 微调**：机构需要对开源大模型（如 Llama 2/3、Mistral）进行私有数据微调，以提升特定业务场景的表现。
- **多模态应用构建**：开发同时涉及文本、图像或结构化数据的复杂 AI 系统，需要统一框架处理不同数据类型。
- **数据中心工作**：强调数据质量与标注的项目，利用 Ludwig 的数据驱动特性优化模型性能。

### 4. **技术亮点**
- **Hugging Face 集成**：无缝对接 Hugging Face Transformers，便于加载和使用丰富的预训练模型和 tokenizer。
- **可扩展性**：支持自定义组件和后端，允许高级用户扩展功能以适应特殊需求。
- **社区活跃**：拥有较高的星标数（11k+）和活跃的标签生态，表明其在机器学习和深度学习社区中具有广泛认可度和持续更新。
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
- ⭐ 6995 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6296 | 🍴 756 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
funNLP 是一个功能极其丰富的自然语言处理（NLP）资源汇总库，集成了敏感词检测、语言识别、实体抽取（手机/身份证/邮箱等）、情感分析及繁简转换等基础工具。它不仅提供各类专业词库（如汽车、医疗、法律、地名等）和预训练模型资源，还收录了大量中文 NLP 竞赛方案、数据集、论文解读及开源项目代码。该项目旨在成为中文 NLP 开发者的全能工具箱，涵盖从数据预处理、知识图谱构建到深度学习模型应用的全链路资源。

### 2. 核心功能
- **基础 NLP 工具与清洗**：提供中英文敏感词过滤、语言检测、停用词、反动词表及繁简体转换，支持手机号、身份证、邮箱等正则抽取。
- **海量领域词库与知识库**：内置中日文人名、中文缩写、职业、品牌、成语、古诗词及医学、法律、财经等专业领域词库，并包含新华字典 API。
- **数据增强与语料资源**：收录 EDA 数据增强工具、多种中文闲聊语料、问答数据集（百度知道等）及谣言数据库，辅助模型训练。
- **前沿模型与算法汇总**：整合 BERT、GPT、ALBERT 等预训练模型资源，提供命名实体识别（NER）、关系抽取、文本摘要及相似度计算的代码模板。
- **行业解决方案与竞赛复盘**：汇集中文 NLP 竞赛 Top 方案、简历筛选系统、对话机器人框架及知识图谱构建工具，展示实际应用场景。

### 3. 适用场景
- **智能客服与聊天机器人开发**：利用其中的闲聊语料、对话系统及意图识别资源，快速搭建具备多轮对话能力的智能助手。
- **内容安全与舆情监控平台**：通过集成敏感词库、暴恐词表及情感分析工具，实现对企业发布内容的自动审核和情感倾向监测。
- **金融/医疗垂直领域信息抽取**：借助专业的金融、医疗词库及 NER 模型代码，构建针对特定行业文档的结构化数据提取系统。
- **NLP 教学与学术研究参考**：作为学生和研究人员的学习仓库，获取最新的中英文 NLP 数据集、论文解读及基准测试排行榜。

### 4. 技术亮点
- **资源聚合度极高**：不仅包含代码，还整合了数据集、预训练模型、API 接口及行业报告，是中文 NLP 领域的“百科全书”。
- **覆盖全生命周期**：从最基础的分词、词性标注，到中级的实体抽取、情感分析，再到高级的知识图谱构建和大模型微调，全覆盖主流 NLP 任务。
- **紧跟前沿技术**：及时收录了 BERT、GPT-2、ALBERT、RoBERTa 等最新预训练模型的应用示例及开源实现，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及多模态大模型（VLM）微调框架，支持 100 多种主流模型。该项目已发表于 ACL 2024，旨在简化从指令微调到强化学习的各类模型适配流程。

**2. 核心功能**
*   **多模型支持**：无缝兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流大模型及视觉语言模型。
*   **高效微调算法**：内置 LoRA、QLoRA 等参数高效微调技术，显著降低显存占用并提升训练速度。
*   **完整训练流程**：支持监督微调（SFT）、奖励模型训练（RM）、PPO/DPO 等强化学习对齐以及离线 RLHF 全流程。
*   **量化部署优化**：提供 INT4/INT8 等低比特量化方案，便于在资源受限环境下进行高效推理与部署。

**3. 适用场景**
*   **垂直领域定制**：为医疗、法律或客服等特定行业数据快速微调大模型，提升专业问答能力。
*   **资源受限环境开发**：在单卡或少量 GPU 环境下，利用 QLoRA 等技术低成本实现大模型私有化部署。
*   **模型对齐研究**：进行 DPO、RLHF 等人类偏好对齐实验，优化模型输出的安全性与指令遵循度。

**4. 技术亮点**
*   **统一架构设计**：基于 Hugging Face Transformers 构建，屏蔽底层差异，提供一致的操作接口。
*   **极致性能优化**：通过 FlashAttention-2、Unsloth 加速等技术，大幅缩短训练时间并提高硬件利用率。
*   **开箱即用体验**：提供详细的文档、预配置脚本及可视化监控工具，极大降低了大模型微调的技术门槛。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73526 | 🍴 8988 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
该项目是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI。它基于Jupyter Notebook构建，涵盖了从机器学习到深度学习的核心概念与技术。

2. **核心功能**
- 提供结构化的12周学习计划，将复杂的AI知识分解为易于管理的24个课时。
- 涵盖广泛的技术领域，包括机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）。
- 使用Jupyter Notebook作为主要教学载体，支持交互式代码执行与即时反馈。
- 由微软发起，适合不同背景的学习者进行系统性的AI基础构建。

3. **适用场景**
- AI初学者希望从零开始建立系统化的人工智能知识体系。
- 教育工作者寻找现成的、模块化的课程大纲用于课堂教学或自学指导。
- 开发者希望通过实际代码示例快速掌握特定AI技术（如RNN、CNN）的应用。

4. **技术亮点**
- 课程内容紧跟主流AI技术栈，涵盖CNN、RNN、GAN等关键深度学习架构。
- 采用微软“For Beginners”系列标准，确保内容通俗易懂且实践性强。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52901 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目是一个从底层原理出发，深入讲解人工智能构建过程的综合性资源库。旨在帮助开发者彻底掌握AI技术原理，并将其转化为可部署、可交付给用户的实际产品。通过“学习、构建、交付”的闭环路径，填补了理论学习与工程落地之间的鸿沟。

2. **核心功能**
- 提供基于Python和Rust等语言的AI系统从零构建教程。
- 涵盖LLM、生成式AI及多智能体（Agents）系统的深度工程实践。
- 包含计算机视觉、强化学习和 swarm intelligence 等前沿领域的应用案例。
- 集成 MCP（Model Context Protocol）等现代AI架构标准的教学内容。

3. **适用场景**
- AI工程师希望深入理解模型内部机制而非仅调用API的场景。
- 需要构建定制化、可控性强的企业级AI应用或智能体系统的团队。
- 希望通过动手实践掌握从数据处理到模型部署全流程的学习者。

4. **技术亮点**
- 强调“From Scratch”的实现方式，深入代码底层以揭示AI黑盒原理。
- 结合多种编程语言（Python, Rust, TypeScript），展示跨语言AI工程能力。
- 内容覆盖从基础机器学习到最新的多模态和代理智能体系列技术栈。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43727 | 🍴 7354 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
该项目是一个集数据分析、机器学习实战、线性代数基础以及PyTorch和TensorFlow 2.x深度学习框架于一体的综合性学习资源库。它涵盖了从传统算法到自然语言处理（NLP）的广泛内容，旨在通过代码实践帮助用户深入理解AI核心知识。

2. **核心功能**
- 提供基于Scikit-learn的传统机器学习算法（如SVM、KMeans、逻辑回归等）实战代码。
- 集成PyTorch和TensorFlow 2.x进行深度神经网络（DNN）、RNN及LSTM等深度学习模型的开发与练习。
- 包含NLTK库的自然语言处理（NLP）入门教程及相关文本挖掘技术实现。
- 涵盖推荐系统、关联规则挖掘（Apriori、FP-Growth）及数据降维（PCA、SVD）等高级应用模块。
- 补充线性代数等数学基础概念，为算法理解提供理论支撑。

3. **适用场景**
- 机器学习初学者希望系统性地从理论到代码掌握经典算法的学习者。
- 需要快速查阅或复现特定AI算法（如AdaBoost、朴素贝叶斯）实现细节的开发者。
- 想要对比学习不同深度学习框架（PyTorch vs TensorFlow）以构建NLP或推荐系统的研究人员。

4. **技术亮点**
- 知识体系全面，巧妙融合了“数学基础+传统ML+深度学习+NLP”的全栈AI学习路径。
- 标签丰富且覆盖主流技术栈（如sklearn, tf2, pytorch），便于针对性检索和学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42417 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33775 | 🍴 4698 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28827 | 🍴 3517 | 语言: Jupyter Notebook
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
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22598 | 🍴 2119 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16387 | 🍴 3775 | 语言: Python
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
- ⭐ 3299 | 🍴 405 | 语言: Python
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
- ⭐ 384223 | 🍴 80722 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261547 | 🍴 23345 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220884 | 🍴 42110 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198108 | 🍴 59649 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185699 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166391 | 🍴 21496 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164280 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157313 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156408 | 🍴 8890 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152441 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

