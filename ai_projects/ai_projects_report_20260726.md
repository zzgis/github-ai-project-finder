# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时环境，旨在让编排逻辑完全保留在 TypeScript 中。它通过将语义处理任务委派给可替换的 Agent 运行时，实现了灵活且可扩展的工作流架构。

2. **核心功能**
- 支持动态工作流的运行时执行，允许运行时根据条件调整流程。
- 采用 TypeScript 进行编排，确保类型安全和开发体验的一致性。
- 解耦语义处理与流程控制，通过可替换的 Agent 运行时实现模块化。
- 兼容多种 AI 代理运行时，提供高度的扩展性和灵活性。

3. **适用场景**
- 需要动态调整执行路径的复杂 AI 应用开发。
- 希望在 TypeScript 生态中构建类型安全、可维护的智能体系统。
- 需要集成不同后端 AI 服务或自定义 Agent 逻辑的场景。
- 快速原型化基于 LLM 的多步骤自动化工作流。

4. **技术亮点**
- 利用 Bun 运行时获得高性能执行能力。
- 将业务逻辑（TypeScript）与 AI 语义处理（Agent Runtime）彻底分离，便于独立迭代和替换。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 74 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- ### 1. **中文简介**
ocm-mcp-server 是一个基于 MCP（模型上下文协议）的服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心节点操作多集群 Kubernetes 环境。它在 AI 模型与底层集群之间引入了策略控制、审批流程及审计机制，确保了操作的安全性与合规性。

### 2. **核心功能**
- **多集群统一管理**：通过 OCM Hub 集中协调和操作多个 Kubernetes 集群。
- **AI 智能体集成**：提供 MCP 接口，使 AI Agent 能够直接调用集群管理功能。
- **安全策略控制**：在 AI 操作与集群资源之间强制执行预定义的策略规则。
- **人工审批流程**：支持对敏感或高风险操作设置人工审批环节。
- **全链路审计日志**：记录所有 AI 智能体的操作行为，便于事后追溯与分析。

### 3. **适用场景**
- **企业级多集群治理**：大型组织使用 OCM 管理跨地域/跨云的多套 K8s 集群时，利用 AI 辅助运维并强化安全管控。
- **自动化运维增强**：在 DevOps 流程中，让 AI 助手执行常规部署或配置变更，同时通过审批机制防止误操作。
- **合规性要求高的环境**：金融或政府机构需要严格审计 AI 对基础设施的操作记录以满足监管要求。
- **测试与开发沙箱**：在受控环境中让开发者通过自然语言指令快速搭建或调试多集群测试环境。

### 4. **技术亮点**
- **MCP 协议原生支持**：无缝对接主流 AI 框架的智能体生态，降低集成门槛。
- **安全隔离设计**：将 AI 的“意图”转化为经过策略过滤和审计的“动作”，实现可控的自动化。
- **基于 OCM 架构**：复用 Open Cluster Management 成熟的集群联邦管理能力，扩展性强。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 36 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能将视觉描述提取并结构化地转换为优化后的 JSON 提示词，以供生成式 AI 使用。该项目内置 SQLite 数据库用于管理提示词编辑，并提供可调节的显存硬件配置文件及 ComfyUI 节点支持。

2. **核心功能**
*   利用本地 Ollama LLM 分析原始文本与图像数据。
*   将视觉描述提取并转化为结构化的优化 JSON 提示词。
*   内置 SQLite 数据库以支持提示词的持久化存储与编辑。
*   提供可调节的 VRAM（显存）硬件配置文件以适配不同设备。
*   包含 ComfyUI 节点，可直接调用数据库中的提示词数据。

3. **适用场景**
*   AI 绘画创作者需要批量处理素材并生成标准化 JSON 格式提示词。
*   拥有有限显存设备的用户希望利用本地模型进行高效的图像处理而不依赖云端 API。
*   ComfyUI 工作流开发者希望将历史提示词数据化并直接集成到生成流程中。
*   需要对非结构化视觉信息进行结构化整理以用于下游生成式 AI 任务的研究者。

4. **技术亮点**
*   实现了从非结构化视觉描述到结构化 JSON 数据的自动化转换。
*   通过本地 Ollama 模型实现隐私保护且低成本的提示词优化。
*   提供了与 ComfyUI 生态系统的原生集成能力，增强了工作流的灵活性。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 33 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
这是一个基于AI的产业链股票池项目，支持美股与A股的映射分析。它具备主动发现机会、政策压力测试及一键部署等功能，旨在辅助投资研究。

2. **核心功能**
*   构建包含美股与A股映射关系的AI产业链股票池。
*   利用AI技术主动挖掘潜在投资机会与趋势。
*   集成政策压力测试模块以评估宏观影响。
*   支持通过Vercel或Cloudflare Workers实现一键快速部署。
*   整合ArXiv学术论文数据以增强研究深度。

3. **适用场景**
*   投资者利用AI分析中美股市关联板块进行资产配置。
*   研究人员结合最新学术文献追踪特定产业链动态。
*   开发者快速搭建并部署个性化的股票监控与研报平台。
*   量化团队在政策变动期间进行压力测试与市场模拟。

4. **技术亮点**
*   采用Serverless架构（Vercel/Cloudflare Workers）实现低成本高效部署。
*   多源数据融合，结合金融数据与前沿AI学术研究成果。
*   提供跨市场（A股/美股）的产业链映射分析能力。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 28 | 🍴 16 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
Verity-JE-Mod 是一款面向 Minecraft Java 版（1.21+）的模组，在原版基础上引入了全新怪物、自定义维度、生物群落及世界生成机制。该模组不支持基岩版，怪物配备语音表演、背景故事及多阶段 AI，且可在 Modrinth 平台免费获取 Forge 和 Fabric 版本。

2. **核心功能**
*   新增具有语音表演和多阶段 AI 行为的独特怪物。
*   提供完全自定义的维度、生物群落与世界生成算法。
*   为游戏内容补充详细的背景故事与 Lore 设定。
*   兼容 Forge 和 Fabric 加载器，支持 1.21 及以上版本。

3. **适用场景**
*   希望增加游戏后期挑战并体验独特怪物战斗的玩家。
*   喜欢探索全新地形、维度或进行世界生成定制的技术型玩家。
*   需要丰富剧情背景与沉浸感体验的剧情向或角色扮演玩家。
*   制作 All The Mods 等整合包时用于增强内容深度的模组开发者。

4. **技术亮点**
*   实现了复杂的多阶段 AI 逻辑以驱动怪物的动态行为。
*   集成原生语音合成与播放技术以增强怪物沉浸感。
*   同时适配主流模组加载器（Forge/Fabric）以确保广泛兼容性。
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

### succhia
- 描述: 在 iPhone 上让 AI 一边陪聊一边控制 BLE 玩具:聊天融合防冻结 + 可靠性层 + 多通道波形引擎 (Bluefy/Chrome, 无需额外硬件)
- 链接: https://github.com/29-Cu/succhia
- ⭐ 16 | 🍴 2 | 语言: HTML

### aar-loop
- 描述: Run an After Action Review after any AI session and write concrete lessons so your agent stops repeating mistakes. A manual Reflexion loop, built on the US Army's AAR method.
- 链接: https://github.com/coopersimson96/aar-loop
- ⭐ 15 | 🍴 2 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源汇总仓库，涵盖了从基础工具到前沿模型的各类开源项目。它集成了敏感词检测、实体抽取、情感分析、知识图谱构建以及语音识别等数十个关键领域的代码与数据资源。该项目旨在为开发者提供一站式的 NLP 解决方案，极大降低了中文信息处理的入门门槛。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简转换、标点修复、拼写检查及文本纠错等功能。
*   **实体与信息抽取**：集成命名实体识别（NER）、关键词提取、关系抽取、事件三元组抽取及文档表格自动检测。
*   **语义分析与理解**：包含情感分析、句子相似度匹配、文本分类、自动摘要生成及中文发音标注。
*   **知识图谱与问答**：汇集多种中文知识图谱构建工具、百科数据集及基于检索或生成的智能问答系统资源。
*   **预训练模型应用**：收录 BERT、RoBERTa、ALBERT、GPT-2 等主流模型在中文场景下的微调代码与应用示例。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析模块，快速搭建新闻、评论或社交媒体的内容过滤系统。
*   **智能客服与对话机器人**：参考仓库中的意图识别、槽位填充及多轮对话代码，开发垂直领域（如医疗、金融）的智能助手。
*   **文本挖掘与数据分析**：结合实体抽取和聚类工具，从海量非结构化文本中提取关键信息，辅助商业决策或舆情监控。
*   **学术研究与算法验证**：作为 NLP 研究者获取最新数据集、基准测试（Benchmark）及 SOTA 模型代码的权威参考源。

4. **技术亮点**
*   **资源极其丰富**：汇集了数百个高质量的开源项目、数据集和论文，覆盖了 NLP 的全链路技术栈。
*   **紧跟前沿技术**：及时收录了基于 Transformer 架构的最新预训练模型及其在中文任务上的最佳实践。
*   **实战导向性强**：不仅提供理论资源，更大量包含可直接运行的代码实现、模型权重及详细教程，便于快速落地。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82064 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。它提供了一个全面的资源库，供开发者学习和实践各种人工智能算法与应用。

2. **核心功能**
- 提供大量现成的AI项目源代码，便于直接参考和复用。
- 覆盖机器学习、深度学习、CV及NLP四大主流技术方向。
- 作为学习资源库，帮助开发者快速掌握各类AI模型的实现细节。
- 集成“Awesome”列表特性， curated 高质量的项目案例。

3. **适用场景**
- AI初学者通过阅读和运行代码快速入门机器学习与深度学习。
- 工程师寻找特定任务（如图像分类、文本生成）的参考实现。
- 研究人员或学生用于对比不同算法在相同数据集上的表现。
- 企业团队评估技术可行性时作为原型开发的起点。

4. **技术亮点**
- 项目数量庞大（500+），覆盖面广，具备极高的参考价值。
- 全代码导向，强调“即插即用”，降低复现门槛。
- 标签体系清晰，便于按技术领域精准检索所需资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，帮助用户直观地查看和分析模型结构。该工具以轻量级和高兼容性著称，广泛应用于 AI 开发流程中。

2. **核心功能**
- 支持多种模型格式（如 ONNX、PyTorch、TensorFlow、Keras 等）的可视化展示。
- 提供交互式界面，允许用户缩放、平移及查看模型层细节。
- 兼容 CoreML、SafeTensors 等新兴或特定领域模型格式。
- 可在浏览器、桌面端或作为 VS Code 插件使用，访问便捷。
- 具备清晰的层级树状图，便于理解复杂神经网络的连接关系。

3. **适用场景**
- 模型调试：开发者在构建或训练模型后，快速检查网络结构是否正确。
- 学术交流：研究人员通过可视化图表向同行清晰展示模型架构。
- 格式转换验证：在将模型从 PyTorch 转换为 ONNX 等格式后，验证转换结果的一致性。
- 教育演示：教师或学生使用可视化工具辅助讲解深度学习原理。

4. **技术亮点**
- 极高的格式兼容性，覆盖目前主流的大部分深度学习框架。
- 部署灵活，无需安装重型环境即可通过浏览器或独立应用运行。
- 开源且社区活跃，持续更新以支持最新模型格式和功能。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在促进不同深度学习框架间的互操作性。它允许模型在PyTorch、TensorFlow等框架之间无缝迁移和部署。该标准由微软、Facebook等巨头共同推动，致力于解决AI生态系统的碎片化问题。

2. **核心功能**
- 提供统一的模型表示格式，支持跨框架加载和运行模型。
- 实现从训练框架到推理引擎的模型转换与优化。
- 支持多种深度学习算子，涵盖卷积、池化及激活函数等常见层结构。
- 兼容主流机器学习库如PyTorch、TensorFlow和scikit-learn的导出需求。
- 促进硬件加速器和云平台对标准化模型的高效执行。

3. **适用场景**
- 将PyTorch或Keras训练的模型转换为ONNX格式，以便在高性能推理引擎上部署。
- 在不同深度学习框架间迁移模型，避免因框架锁定导致的技术债。
- 在资源受限的边缘设备或移动端上运行经过优化的ONNX模型。
- 集成第三方硬件加速器，利用其专用后端提升模型推理速度。

4. **技术亮点**
- **跨平台兼容性**：被广泛支持于NVIDIA TensorRT、Intel OpenVINO、Microsoft ONNX Runtime等主流推理引擎。
- **生态系统融合**：作为Apache 2.0开源协议下的标准，深度融入AI开发全链路，连接训练与生产环境。
- **高性能推理**：通过静态计算图和优化算子融合，显著降低延迟并提高吞吐量，特别适合实时应用。
- 链接: https://github.com/onnx/onnx
- ⭐ 21215 | 🍴 3975 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一部关于机器学习工程化的开源指南。它系统性地涵盖了从模型训练、调试到大规模部署的完整工程实践流程。该项目旨在为构建可扩展且高效的机器学习系统提供全面的技术参考。

2. **核心功能**
- 提供大语言模型（LLM）训练、微调及推理的工程化最佳实践。
- 深入解析分布式训练架构、GPU资源管理及Slurm集群调度技巧。
- 涵盖模型调试、性能优化及大规模数据存储与网络通信策略。
- 介绍PyTorch框架下的高性能训练实现与Transformer库的高级用法。

3. **适用场景**
- 需要搭建和维护大规模分布式AI训练基础设施的团队。
- 致力于优化大语言模型推理延迟并降低计算成本的工程人员。
- 希望提升机器学习系统可扩展性以应对海量数据处理的MLOps专家。

4. **技术亮点**
- 聚焦于工业级生产环境中的实际工程挑战而非仅理论算法。
- 紧密结合PyTorch生态与主流LLM框架，提供可落地的代码级指导。
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
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。它提供了一个全面的资源库，供开发者学习和实践各种人工智能算法与应用。

2. **核心功能**
- 提供大量现成的AI项目源代码，便于直接参考和复用。
- 覆盖机器学习、深度学习、CV及NLP四大主流技术方向。
- 作为学习资源库，帮助开发者快速掌握各类AI模型的实现细节。
- 集成“Awesome”列表特性， curated 高质量的项目案例。

3. **适用场景**
- AI初学者通过阅读和运行代码快速入门机器学习与深度学习。
- 工程师寻找特定任务（如图像分类、文本生成）的参考实现。
- 研究人员或学生用于对比不同算法在相同数据集上的表现。
- 企业团队评估技术可行性时作为原型开发的起点。

4. **技术亮点**
- 项目数量庞大（500+），覆盖面广，具备极高的参考价值。
- 全代码导向，强调“即插即用”，降低复现门槛。
- 标签体系清晰，便于按技术领域精准检索所需资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，帮助用户直观地查看和分析模型结构。该工具以轻量级和高兼容性著称，广泛应用于 AI 开发流程中。

2. **核心功能**
- 支持多种模型格式（如 ONNX、PyTorch、TensorFlow、Keras 等）的可视化展示。
- 提供交互式界面，允许用户缩放、平移及查看模型层细节。
- 兼容 CoreML、SafeTensors 等新兴或特定领域模型格式。
- 可在浏览器、桌面端或作为 VS Code 插件使用，访问便捷。
- 具备清晰的层级树状图，便于理解复杂神经网络的连接关系。

3. **适用场景**
- 模型调试：开发者在构建或训练模型后，快速检查网络结构是否正确。
- 学术交流：研究人员通过可视化图表向同行清晰展示模型架构。
- 格式转换验证：在将模型从 PyTorch 转换为 ONNX 等格式后，验证转换结果的一致性。
- 教育演示：教师或学生使用可视化工具辅助讲解深度学习原理。

4. **技术亮点**
- 极高的格式兼容性，覆盖目前主流的大部分深度学习框架。
- 部署灵活，无需安装重型环境即可通过浏览器或独立应用运行。
- 开源且社区活跃，持续更新以支持最新模型格式和功能。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究人员提供了不可或缺的速查表（Cheat Sheets）。它涵盖了从基础库到高级框架的各种关键技术参考，旨在帮助研究者快速回顾和查阅核心概念与代码用法。

2. **核心功能**
*   提供深度学习领域的关键概念速查，如神经网络架构和优化算法。
*   包含常用Python数据科学库（如NumPy、SciPy、Matplotlib）的代码示例与函数参考。
*   整理机器学习框架（如Keras）的核心API及使用方法。
*   汇总统计分析与数据处理的关键公式与技巧。
*   作为研究人员的快速记忆辅助工具，减少查阅官方文档的时间。

3. **适用场景**
*   深度学习研究员在进行模型实验时，快速回顾特定算法或函数的用法。
*   机器学习初学者在复习基础概念和常用库操作时的参考资料。
*   数据科学家在处理数据清洗、可视化或统计分析任务时的即时查询工具。
*   面试准备过程中，快速梳理AI领域核心知识点和代码模式。

4. **技术亮点**
*   内容高度浓缩，将复杂的库和框架知识提炼为易于阅读的图表形式。
*   覆盖范围广，整合了从底层数学库到高层应用框架的多层技术栈。
*   由社区维护并经过大量星标验证，具有较高的实用性和参考价值。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供人工智能领域的系统学习路线图，收录近200个实战案例与项目，并免费提供配套教材。它旨在帮助零基础用户从入门到精通，涵盖Python、机器学习、深度学习及数据分析等热门技术栈，助力就业实战。

2. **核心功能**
*   提供完整的人工智能学习路径，涵盖数学基础、算法原理及主流框架应用。
*   整理近200个精选实战案例和项目代码，支持直接动手练习。
*   免费提供配套的学习教材和资源文档，降低学习门槛。
*   覆盖广泛的技术领域，包括NLP、计算机视觉、数据挖掘及主流深度学习框架（PyTorch/TensorFlow/Keras）。

3. **适用场景**
*   零基础转行人员希望系统学习AI知识并快速进入职场。
*   在校学生或初级工程师寻找高质量的实战项目以丰富简历。
*   需要复习或梳理机器学习、深度学习理论体系的技术从业者。
*   希望获取免费、结构化AI学习资源的教育者或自学者。

4. **技术亮点**
该项目整合了从底层数学基础到上层应用框架（如TensorFlow 2、PyTorch、Caffe）的全栈技术生态，通过“路线图+实战案例+免费教材”的组合模式，构建了闭环的学习闭环。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置支持多种机器学习任务，让开发者无需编写大量底层代码即可快速搭建和训练模型。

**2. 核心功能**
*   **低代码/声明式接口**：通过 YAML 或 JSON 配置文件定义模型架构和数据管道，极大降低开发门槛。
*   **多模态支持**：原生支持文本、图像、表格等多种数据类型，适用于计算机视觉和自然语言处理任务。
*   **广泛的模型兼容性**：内置对 PyTorch 生态的支持，并兼容主流 LLM 架构（如 LLaMA、Mistral 等），方便进行微调。
*   **自动化数据处理与评估**：提供自动的数据预处理、特征工程以及模型性能评估工具，实现端到端的 MLOps 流程。

**3. 适用场景**
*   **快速原型开发**：数据科学家希望在不深入掌握深度学习框架细节的情况下，快速验证 AI 想法。
*   **企业级 ML 部署**：需要标准化、可复现的机器学习流水线，以减少团队间的协作成本和维护难度。
*   **LLM 微调与应用**：针对特定领域数据对开源大模型（如 LLaMA）进行高效微调，构建垂直领域的 AI 应用。

**4. 技术亮点**
Ludwig 的最大亮点在于其“去代码化”的设计哲学，它将复杂的深度学习工程问题转化为简单的配置声明，同时保持了与 PyTorch 等主流框架的深度集成，兼顾了易用性与灵活性。
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
- ⭐ 6294 | 🍴 756 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源汇总仓库，涵盖了从基础工具到前沿模型的各类开源项目。它集成了敏感词检测、实体抽取、情感分析、知识图谱构建以及语音识别等数十个关键领域的代码与数据资源。该项目旨在为开发者提供一站式的 NLP 解决方案，极大降低了中文信息处理的入门门槛。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简转换、标点修复、拼写检查及文本纠错等功能。
*   **实体与信息抽取**：集成命名实体识别（NER）、关键词提取、关系抽取、事件三元组抽取及文档表格自动检测。
*   **语义分析与理解**：包含情感分析、句子相似度匹配、文本分类、自动摘要生成及中文发音标注。
*   **知识图谱与问答**：汇集多种中文知识图谱构建工具、百科数据集及基于检索或生成的智能问答系统资源。
*   **预训练模型应用**：收录 BERT、RoBERTa、ALBERT、GPT-2 等主流模型在中文场景下的微调代码与应用示例。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析模块，快速搭建新闻、评论或社交媒体的内容过滤系统。
*   **智能客服与对话机器人**：参考仓库中的意图识别、槽位填充及多轮对话代码，开发垂直领域（如医疗、金融）的智能助手。
*   **文本挖掘与数据分析**：结合实体抽取和聚类工具，从海量非结构化文本中提取关键信息，辅助商业决策或舆情监控。
*   **学术研究与算法验证**：作为 NLP 研究者获取最新数据集、基准测试（Benchmark）及 SOTA 模型代码的权威参考源。

4. **技术亮点**
*   **资源极其丰富**：汇集了数百个高质量的开源项目、数据集和论文，覆盖了 NLP 的全链路技术栈。
*   **紧跟前沿技术**：及时收录了基于 Transformer 架构的最新预训练模型及其在中文任务上的最佳实践。
*   **实战导向性强**：不仅提供理论资源，更大量包含可直接运行的代码实现、模型权重及详细教程，便于快速落地。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82064 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目已在 ACL 2024 上发表，旨在简化从基础模型到专业应用的微调流程，提供低资源消耗和高性能的解决方案。

2. **核心功能**
- 支持100多种主流大模型及视觉语言模型的统一微调接口。
- 内置 LoRA、QLoRA、P-Tuning 等多种高效微调算法及量化技术。
- 集成 RLHF（基于人类反馈的强化学习）、DPO 等对齐训练策略。
- 提供 Web UI 和命令行工具，降低微调技术的入门门槛。
- 兼容 Transformers 库，支持多卡分布式训练以加速大规模模型微调。

3. **适用场景**
- 企业级私有化部署：利用 QLoRA 等技术，在有限显存下微调开源大模型以适应特定业务需求。
- 学术研究实验：快速验证不同模型架构、微调算法（如 LoRA vs. Full Fine-tuning）的性能差异。
- 多模态应用开发：对包含图像理解能力的视觉语言模型（VLMs）进行指令微调，构建智能助手。
- 模型对齐优化：通过 RLHF 或 DPO 技术，提升模型回答的安全性、有用性和风格一致性。

4. **技术亮点**
- **极致轻量化**：原生支持 4-bit/8-bit 量化训练（QLoRA），大幅降低显存占用，使消费级显卡也能微调大模型。
- **广泛兼容性**：一站式支持 LLaMA、Qwen、Gemma、DeepSeek 等百余个模型，无需为每个模型编写独立的微调代码。
- **全链路支持**：涵盖数据预处理、模型训练、评估、推理导出及 Web 交互界面，形成完整的微调工作流。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73526 | 🍴 8987 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能入门课程，旨在面向所有人普及AI知识。该项目由Microsoft for Beginners支持，通过Jupyter Notebook提供互动式学习体验。其目标是让初学者能够轻松掌握从基础概念到深度学习的高级技能。

2. **核心功能**
- 提供结构化的12周学习计划，涵盖24个精心设计的课程模块。
- 基于Jupyter Notebook实现交互式代码练习与即时反馈。
- 内容全面覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
- 包含卷积神经网络（CNN）、循环神经网络（RNN）和生成对抗网络（GAN）等前沿技术实践。
- 适合零基础的全球学习者，以通俗易懂的方式降低人工智能学习门槛。

3. **适用场景**
- 大学生或职场新人希望系统性地入门人工智能领域的自学需求。
- 教育机构或企业培训团队用于开展AI基础技能 workshops 或内部培训。
- 对计算机视觉或自然语言处理感兴趣的开发者寻找实战代码示例。
- 教育工作者寻找开源、标准化的AI教学大纲和配套资源。

4. **技术亮点**
- 由微软官方主导开发，确保内容的权威性、准确性和行业相关性。
- 采用模块化课程设计，将复杂的AI概念拆解为易于消化的24个独立单元。
- 集成多种主流AI技术栈（如NLP、CV、DL），提供端到端的学习路径。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52898 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入教授AI工程的核心原理与实践。它不仅涵盖理论学习，更强调实际动手搭建并部署AI应用，适合希望掌握底层技术细节的开发者。

2. **核心功能**
- 提供从基础到高级的AI工程全流程教程，涵盖机器学习、深度学习及生成式AI。
- 重点讲解AI智能体（Agents）、大语言模型（LLM）及多模态技术的实战开发。
- 包含计算机视觉、自然语言处理（NLP）和强化学习等特定领域的专项课程。
- 结合Python、Rust和TypeScript等多语言工具，演示如何构建可扩展的AI系统。

3. **适用场景**
- AI工程师希望深入理解模型底层机制以优化生产环境中的AI应用。
- 研究人员或学生想要系统学习生成式AI和智能体架构的设计与实现。
- 团队需要参考从零构建复杂AI系统（如MCP集成、Swarm智能）的最佳实践。

4. **技术亮点**
- 强调“从零开始”的工程视角，而非仅调用高级API，有助于夯实基础。
- 内容覆盖前沿领域如MCP（Model Context Protocol）和群体智能，具备较高前瞻性。
- 多语言栈支持（Python/Rust/TS），展示了高性能AI系统的混合开发模式。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43695 | 🍴 7347 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合资源库，深入讲解了线性代数、PyTorch及TensorFlow 2等核心框架。内容同时整合了NLTK自然语言处理工具，为学习者提供从理论基础到代码实现的完整路径。

2. **核心功能**
- 提供基于Python的机器学习算法实战代码（如SVM、KMeans、逻辑回归等）。
- 包含深度学习框架PyTorch和TensorFlow 2的详细应用示例。
- 集成NLTK库进行自然语言处理（NLP）相关的入门与进阶实践。
- 梳理线性代数等数学基础，辅助理解机器学习背后的原理。

3. **适用场景**
- 机器学习初学者构建从数学基础到算法实现的系统知识体系。
- 希望对比学习Scikit-learn传统算法与PyTorch/TF2深度学习框架的开发者。
- 需要快速查阅经典算法（如随机森林、朴素贝叶斯）代码实现的工程师。

4. **技术亮点**
- 实现了主流监督与非监督学习算法的全面覆盖，兼顾经典与前沿技术栈。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42417 | 🍴 11530 | 语言: Python
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
- ⭐ 28828 | 🍴 3517 | 语言: Jupyter Notebook
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
- ⭐ 22598 | 🍴 2118 | 语言: Python
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
- ⭐ 384216 | 🍴 80722 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261509 | 🍴 23345 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220844 | 🍴 42093 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198101 | 🍴 59647 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185698 | 🍴 46068 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166390 | 🍴 21496 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164280 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157312 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156357 | 🍴 8888 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152435 | 🍴 9661 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

