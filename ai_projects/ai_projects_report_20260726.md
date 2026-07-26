# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### deer-workflow
- **1. 中文简介**
deer-workflow 是一个开源的动态工作流运行时框架，它允许开发者在 TypeScript 环境中直接进行复杂的编排逻辑开发。该框架通过可替换的 Agent 运行时来委托并处理具体的语义任务，实现了编排与执行解耦。

**2. 核心功能**
- **动态工作流运行时**：提供灵活的工作流执行引擎，支持动态构建和调整业务流程。
- **TypeScript 原生编排**：保持编排逻辑完全在 TypeScript 中编写，确保类型安全和开发体验一致。
- **可替换的 Agent 运行时**：将语义处理工作委托给可插拔的 Agent 后端，便于根据不同需求更换底层 AI 模型或执行器。
- **语义任务代理**：自动将工作流中的语义密集型任务交给专门的 Agent 模块处理，提升专业化能力。

**3. 适用场景**
- **复杂 AI 应用开发**：需要结合多种 LLM 能力并协调多个步骤的智能应用（如自动化客服、智能助手）。
- **动态业务编排**：业务流程经常变化，需要快速调整工作流节点和执行顺序的企业级应用。
- **多模型集成平台**：希望在一个统一框架下无缝切换不同供应商的 AI Agent 或大语言模型的服务。
- **AI 编码辅助工具**：用于构建能够理解代码语义并自动执行复杂重构或生成任务的 AI 编程代理。

**4. 技术亮点**
- **高度解耦架构**：将“流程控制”与“语义执行”分离，使得工作流引擎轻量且易于维护。
- **生态兼容性**：基于 TypeScript 和 Bun 运行环境，适合现代高性能 JavaScript/TypeScript 开发栈。
- **可扩展性强**：通过插件化的 Agent 运行时设计，用户可以根据性能或成本需求自定义后端执行引擎。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 70 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- 1. **中文简介**
该项目是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心管理多集群 Kubernetes 环境。它在模型与底层集群之间提供了策略控制、审批流程以及审计功能，确保操作的安全性和合规性。

2. **核心功能**
*   支持 AI 智能体通过 MCP 协议直接操作多个 Kubernetes 集群。
*   利用 OCM Hub 实现对多集群环境的统一管理和调度。
*   在 AI 指令执行过程中集成策略检查与人工/自动审批机制。
*   提供完整的操作审计日志，记录 AI 对集群的所有变更行为。

3. **适用场景**
*   大型企业中需要 AI 辅助进行跨地域或多租户 Kubernetes 集群管理的运维团队。
*   对云原生资源操作有严格合规要求，需保留完整审计痕迹的企业环境。
*   希望将自然语言指令转化为 K8s 操作，同时保留最终审批权的 DevSecOps 流程。

4. **技术亮点**
*   结合了 MCP 标准与 OCM 架构，实现了 AI 与大规模 K8s 集群管理的标准化接口。
*   内置安全护栏（策略与审批），有效降低 AI 直接操作生产环境带来的风险。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 33 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能将视觉描述提取并结构化为优化后的 JSON 格式提示词，供生成式 AI 使用。该应用内置 SQLite 数据库用于管理提示词，并提供可调节的显存硬件配置文件及 ComfyUI 节点支持。

2. **核心功能**
- 利用本地 Ollama LLM 分析原始文本与图像内容。
- 自动提取视觉细节并将其转化为结构化的 JSON 提示词。
- 内置 SQLite 数据库，支持提示词的存储、编辑与管理。
- 提供可配置的 VRAM（显存）硬件配置文件以适应不同设备。
- 集成 ComfyUI 节点，可直接调用数据库中的提示词工作流。

3. **适用场景**
- 需要高效将自然语言或图像描述转换为结构化 JSON 提示词的专业用户。
- 希望利用本地模型保护数据隐私，避免依赖云端 API 的开发者。
- 使用 ComfyUI 进行工作流自动化，并希望复用历史提示词库的设计师。
- 显存资源有限，需通过硬件配置优化本地模型推理性能的用户。

4. **技术亮点**
- 实现了本地化 AI 推理与结构化数据输出的无缝结合。
- 通过 SQLite 和 ComfyUI 节点打通了提示词管理与自动化生成的闭环。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 30 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
该项目是一个基于人工智能的产业链股票池，支持美股与A股的映射对照。它具备主动发现潜力标的及政策压力分析功能，并支持一键部署，旨在为投资研究提供高效的技术支持。

2. **核心功能**
*   实现美股与A股产业链的深度映射与关联分析。
*   利用AI技术主动发掘潜在的投资机会和标的。
*   结合政策导向进行压力测试与市场趋势预判。
*   提供一键部署方案，降低使用门槛并快速搭建环境。

3. **适用场景**
*   需要跨市场（中美）对比分析产业链影响的量化研究人员。
*   希望借助AI工具快速筛选高潜力股票的个人投资者。
*   关注宏观政策对市场冲击并进行风险管理的基金经理。
*   希望快速搭建自动化股票监控系统的技术型开发者。

4. **技术亮点**
*   采用Cloudflare Workers和Vercel实现边缘计算与云端的一键部署，具备高可用性和低延迟优势。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 28 | 🍴 16 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
Verity-JE-Mod 是一款适用于 Minecraft Java 版 1.21+ 的模组，新增了具有语音演出、背景故事及多阶段 AI 的智能怪物，并包含自定义维度、生物群系和地形生成内容。该模组仅在 Modrinth 平台提供，支持 Forge 和 Fabric 加载器，且完全免费下载，不适用于基岩版。

2. **核心功能**
*   新增具有独特多阶段 AI 行为逻辑的新怪物。
*   提供完整的怪物背景故事与配音演出以增强沉浸感。
*   包含自定义维度、生物群系及世界生成机制。
*   兼容主流的 Forge 和 Fabric 模组加载器。
*   支持 Minecraft Java 版 1.21 及以上版本。

3. **适用场景**
*   希望为生存模式引入高难度挑战和多阶段 Boss 战的玩家。
*   喜欢探索全新自定义维度和独特生物群系的冒险者。
*   注重剧情叙事和沉浸式体验的模组包制作人与玩家。
*   使用 All The Mods 或 Skyblock 等整合包寻求新内容的社区。

4. **技术亮点**
*   实现了复杂的多阶段人工智能（AI）逻辑，使怪物具备动态战斗行为。
*   集成了音频资源以实现怪物的语音演出功能。
*   通过自定义世界生成算法扩展了原版的地形多样性。
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
- ⭐ 22 | 🍴 4 | 语言: TypeScript

### aar-loop
- 描述: Run an After Action Review after any AI session and write concrete lessons so your agent stops repeating mistakes. A manual Reflexion loop, built on the US Army's AAR method.
- 链接: https://github.com/coopersimson96/aar-loop
- ⭐ 14 | 🍴 1 | 语言: Python

### imersao-aiops-03
- 描述: 无描述
- 链接: https://github.com/fabricioveronez/imersao-aiops-03
- ⭐ 13 | 🍴 12 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面的中英文自然语言处理（NLP）资源汇总库，集成了敏感词检测、语言识别、实体抽取及语音处理等核心工具。该项目还收录了海量的中文词典、语料库、预训练模型（如 BERT、ALBERT）以及各类 NLP 竞赛方案与前沿论文代码，旨在为开发者提供一站式的中文 NLP 开发支持。

**2. 核心功能**
*   **基础文本处理与工具集**：提供敏感词过滤、繁简转换、中英文分词、命名实体识别（NER）、关键词抽取、文本摘要及句子相似度计算等实用工具。
*   **海量领域知识图谱与词典**：涵盖人名、地名、公司名、职业、汽车零件、医学、法律等多个垂直领域的专用词库和知识图谱构建资源。
*   **预训练模型与深度学习资源**：汇总了 BERT、GPT、ALBERT、ERNIE 等多种主流预训练模型的中文版本及其在分类、问答、序列标注等任务上的应用代码。
*   **多模态与语音技术集成**：包含中文语音识别（ASR）、文字识别（OCR）、音素对齐、声纹分析及语音情感分析等相关数据集与工具。
*   **数据增强与评测基准**：提供 EDA 数据增强工具、NLP 竞赛高分方案复盘、各类中文 NLP 数据集搜索平台及语言理解测评基准。

**3. 适用场景**
*   **中文 NLP 算法研发**：适合需要快速接入分词、NER、情感分析等基础模块，或寻找预训练模型进行微调的算法工程师。
*   **垂直领域知识库构建**：适用于医疗、金融、法律、汽车等行业，利用其提供的专用词库和关系抽取工具构建领域知识图谱。
*   **智能客服与对话系统开发**：开发者可参考其中的对话机器人框架、闲聊语料库、QA 数据集及意图识别模型，搭建智能问答系统。
*   **NLP 学习与竞赛备战**：适合学生和研究人员通过阅读其中的论文梳理、竞赛 Top 方案解析及基准测试数据，快速掌握 NLP 前沿技术。

**4. 技术亮点**
*   **资源极度丰富且分类清晰**：不仅包含代码工具，还整合了从基础词典到前沿论文、竞赛代码的全链条资源，极大降低了中文 NLP 的学习门槛。
*   **紧跟前沿模型落地**：及时收录了 BERT、GPT-2、ALBERT、ELECTREA 等最新预训练模型的中文适配版本及实战案例。
*   **覆盖多模态与细粒度任务**：除了传统文本处理，还涵盖了 OCR、ASR、实体链接、细粒度情感分析等复杂场景的工具和数据集。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82061 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目以“Awesome”列表的形式组织，为开发者提供了丰富的实战案例和源代码参考。它旨在帮助技术人员快速上手并深入理解各类人工智能算法的实际应用。

2. **核心功能**
- 提供大量涵盖ML、DL、CV和NLP领域的完整项目代码。
- 作为精选资源库（Awesome List），按主题分类整理AI相关项目。
- 支持多种主流编程语言，重点展示Python在AI中的应用。
- 包含从基础到高级的多样化算法实现示例。

3. **适用场景**
- AI初学者通过阅读和运行代码来学习机器学习与深度学习原理。
- 研究人员或工程师寻找特定任务（如图像识别、文本分析）的参考实现。
- 技术团队进行原型开发时，快速复用经过验证的项目模板。
- 参加黑客松或竞赛前，积累相关领域的算法知识和代码素材。

4. **技术亮点**
- 内容全面，覆盖了当前人工智能领域的多个热门方向。
- 代码开源且易于获取，便于直接复现和修改。
- 社区驱动的高质量筛选，确保项目具有一定的实用性和代表性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35725 | 🍴 7381 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一个用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持多种主流框架生成的模型格式，帮助用户直观地查看和理解模型结构。该工具基于 JavaScript 开发，具有轻量级且跨平台的特点。

### 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、PyTorch、Keras、CoreML、TFLite 及 Safetensors 等广泛使用的模型格式。
- **可视化展示**：提供清晰的网络架构图和层细节视图，便于检查模型拓扑结构。
- **交互式操作**：允许用户缩放、平移和点击节点以探索不同层的参数和数据流向。
- **轻量级部署**：作为独立的桌面应用或 Web 应用运行，无需复杂的配置环境即可快速加载模型。
- **开源免费**：项目完全开源，社区活跃，持续更新以支持新的模型架构和格式。

### 3. 适用场景
- **模型调试与验证**：在训练过程中或部署前，快速检查模型结构是否正确，识别潜在的连接错误。
- **学术交流与展示**：将复杂的神经网络结构转化为直观的图表，便于在论文、演示文稿或技术博客中展示。
- **跨框架迁移分析**：当从一种框架（如 PyTorch）迁移到另一种框架（如 TensorFlow Lite）时，对比模型结构以确保一致性。
- **非开发者理解**：帮助产品经理、研究人员或非编程背景的技术人员理解深度学习模型的基本工作原理。

### 4. 技术亮点
- **广泛的兼容性**：通过统一的前端渲染引擎，实现了对数十种不同后端框架模型格式的无缝支持。
- **高性能渲染**：利用现代浏览器技术和高效的图形渲染算法，即使处理大型复杂网络也能保持流畅的交互体验。
- **即开即用**：无需安装额外的运行时依赖（如 Python 环境），直接打开文件即可查看，极大降低了使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在弥合不同深度学习框架之间的壁垒，实现模型在不同平台间的无缝转换与部署。

2. **核心功能**
- 提供统一的模型表示格式，支持跨框架的模型交换。
- 允许在推理引擎和训练框架之间高效迁移模型。
- 支持多种硬件后端优化，提升模型执行效率。
- 拥有活跃的社区生态，兼容主流深度学习库如PyTorch、TensorFlow等。

3. **适用场景**
- 需要在不同深度学习框架（如从PyTorch到TensorRT）之间迁移模型时。
- 部署高性能推理服务，利用特定硬件加速优化模型运行速度。
- 构建跨平台的AI应用，确保模型在不同操作系统和设备上兼容。

4. **技术亮点**
- 作为行业标准的开放规范，促进了AI生态系统的互联互通。
- 支持复杂的神经网络结构，涵盖从传统DNN到最新Transformer架构。
- 链接: https://github.com/onnx/onnx
- ⭐ 21214 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面覆盖机器学习工程实践的资源指南，旨在填补从模型训练到部署落地的知识空白。它深入探讨了大规模分布式训练、高效推理优化以及底层系统调优等关键领域。该项目为希望掌握现代AI基础设施构建能力的工程师提供了极具价值的参考体系。

2. **核心功能**
*   提供大规模分布式训练的完整技术栈指导，涵盖PyTorch、Slurm及网络存储配置。
*   详解大语言模型（LLM）的高效推理策略与内存优化技术。
*   包含实用的调试技巧、性能剖析方法及系统可扩展性设计原则。
*   集成MLOps最佳实践，连接模型开发与生产环境运维。

3. **适用场景**
*   需要搭建或优化千卡/万卡集群进行超大规模模型训练的工程师。
*   致力于降低大模型推理成本并提升响应速度的算法工程师。
*   希望系统学习MLinfra（机器学习基础设施）知识的初学者或进阶者。
*   负责LLM从实验环境迁移至生产环境的MLOps团队。

4. **技术亮点**
*   内容紧跟前沿，深度整合了Transformer架构与最新GPU硬件特性。
*   强调“Open Book”的协作精神，持续吸纳社区贡献的实际工程案例。
*   不仅关注算法，更着重于解决算力瓶颈、通信开销等底层工程问题。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18469 | 🍴 1181 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17337 | 🍴 2117 | 语言: 未知
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
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目以“Awesome”列表的形式组织，为开发者提供了丰富的实战案例和源代码参考。它旨在帮助技术人员快速上手并深入理解各类人工智能算法的实际应用。

2. **核心功能**
- 提供大量涵盖ML、DL、CV和NLP领域的完整项目代码。
- 作为精选资源库（Awesome List），按主题分类整理AI相关项目。
- 支持多种主流编程语言，重点展示Python在AI中的应用。
- 包含从基础到高级的多样化算法实现示例。

3. **适用场景**
- AI初学者通过阅读和运行代码来学习机器学习与深度学习原理。
- 研究人员或工程师寻找特定任务（如图像识别、文本分析）的参考实现。
- 技术团队进行原型开发时，快速复用经过验证的项目模板。
- 参加黑客松或竞赛前，积累相关领域的算法知识和代码素材。

4. **技术亮点**
- 内容全面，覆盖了当前人工智能领域的多个热门方向。
- 代码开源且易于获取，便于直接复现和修改。
- 社区驱动的高质量筛选，确保项目具有一定的实用性和代表性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35725 | 🍴 7381 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一个用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持多种主流框架生成的模型格式，帮助用户直观地查看和理解模型结构。该工具基于 JavaScript 开发，具有轻量级且跨平台的特点。

### 2. 核心功能
- **多格式支持**：兼容 ONNX、TensorFlow、PyTorch、Keras、CoreML、TFLite 及 Safetensors 等广泛使用的模型格式。
- **可视化展示**：提供清晰的网络架构图和层细节视图，便于检查模型拓扑结构。
- **交互式操作**：允许用户缩放、平移和点击节点以探索不同层的参数和数据流向。
- **轻量级部署**：作为独立的桌面应用或 Web 应用运行，无需复杂的配置环境即可快速加载模型。
- **开源免费**：项目完全开源，社区活跃，持续更新以支持新的模型架构和格式。

### 3. 适用场景
- **模型调试与验证**：在训练过程中或部署前，快速检查模型结构是否正确，识别潜在的连接错误。
- **学术交流与展示**：将复杂的神经网络结构转化为直观的图表，便于在论文、演示文稿或技术博客中展示。
- **跨框架迁移分析**：当从一种框架（如 PyTorch）迁移到另一种框架（如 TensorFlow Lite）时，对比模型结构以确保一致性。
- **非开发者理解**：帮助产品经理、研究人员或非编程背景的技术人员理解深度学习模型的基本工作原理。

### 4. 技术亮点
- **广泛的兼容性**：通过统一的前端渲染引擎，实现了对数十种不同后端框架模型格式的无缝支持。
- **高性能渲染**：利用现代浏览器技术和高效的图形渲染算法，即使处理大型复杂网络也能保持流畅的交互体验。
- **即开即用**：无需安装额外的运行时依赖（如 Python 环境），直接打开文件即可查看，极大降低了使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33265 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目专为深度学习和机器学习研究人员提供不可或缺的速查表（Cheat Sheets）。它汇集了关键概念与代码示例，旨在帮助研究者快速回顾和掌握核心知识点。

2. **核心功能**
- 提供深度学习与机器学习领域的综合性速查表资源。
- 涵盖 Keras、NumPy、SciPy 及 Matplotlib 等常用库的操作指南。
- 整理人工智能相关的关键算法与理论要点。
- 以结构化文档形式呈现，便于快速检索和理解。

3. **适用场景**
- 研究人员在开发模型前快速回顾特定库或算法的使用语法。
- 学生或初学者系统性地梳理深度学习基础知识框架。
- 开发者在日常编程中查找 NumPy 或 Matplotlib 的具体函数用法。

4. **技术亮点**
- 聚焦于实用工具库（如 Keras、Scipy）的高频使用场景。
- 内容经过 Medium 平台知名博主推荐，具有较高的社区认可度。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. **中文简介**
该项目提供了一套完整的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材。它涵盖从零基础入门到就业实战的全过程，内容涉及Python、机器学习、深度学习及自然语言处理等热门领域。

### 2. **核心功能**
- 提供系统化的人工智能学习路径，适合不同阶段的学习者。
- 整理近200个高质量实战案例和项目，强调动手能力。
- 免费开放配套教材和资源，降低学习门槛。
- 覆盖广泛的技术栈，包括主流框架如PyTorch、TensorFlow和Keras。
- 注重从数学基础到算法实现的全面知识体系构建。

### 3. **适用场景**
- 零基础初学者希望系统入门人工智能领域。
- 数据科学家或工程师寻求实战项目以提升技能。
- 求职者希望通过实战案例准备面试和就业。
- 教育机构或个人导师用于辅助教学和学习规划。

### 4. **技术亮点**
- 集成多种主流AI框架（如PyTorch、TensorFlow）和工具库（如NumPy、Pandas）。
- 涵盖计算机视觉（CV）、自然语言处理（NLP）等前沿方向。
- 提供从数学基础到高级算法的完整知识链条。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置让用户能够专注于数据而非复杂的工程细节，从而高效地训练和部署机器学习模型。

2. **核心功能**
- 支持基于表格数据和深度学习模型的低代码 AI 开发，显著降低入门门槛。
- 提供对主流 LLM（如 Llama、Mistral）的微调与训练支持，适配自然语言处理任务。
- 兼容 PyTorch 等主流深度学习后端，实现从实验到生产环境的无缝部署。
- 具备数据-centric（以数据为中心）特性，优化数据处理流程以提升模型性能。

3. **适用场景**
- 需要快速原型验证或构建定制化 LLM 应用，但不希望深入底层代码的工程团队。
- 进行计算机视觉或自然语言处理的数据科学项目，特别是涉及结构化数据分析的场景。
- 希望利用现成工具对开源大模型（如 Llama 2/3、Mistral）进行领域微调的研究人员。

4. **技术亮点**
- 采用声明式 YAML 配置架构，使模型定义直观且易于版本控制。
- 内置数据管道和可视化功能，简化了从数据预处理到模型评估的全链路工作。
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
- ⭐ 6293 | 🍴 755 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面的中英文自然语言处理（NLP）资源汇总库，集成了敏感词检测、语言识别、实体抽取及语音处理等核心工具。该项目还收录了海量的中文词典、语料库、预训练模型（如 BERT、ALBERT）以及各类 NLP 竞赛方案与前沿论文代码，旨在为开发者提供一站式的中文 NLP 开发支持。

**2. 核心功能**
*   **基础文本处理与工具集**：提供敏感词过滤、繁简转换、中英文分词、命名实体识别（NER）、关键词抽取、文本摘要及句子相似度计算等实用工具。
*   **海量领域知识图谱与词典**：涵盖人名、地名、公司名、职业、汽车零件、医学、法律等多个垂直领域的专用词库和知识图谱构建资源。
*   **预训练模型与深度学习资源**：汇总了 BERT、GPT、ALBERT、ERNIE 等多种主流预训练模型的中文版本及其在分类、问答、序列标注等任务上的应用代码。
*   **多模态与语音技术集成**：包含中文语音识别（ASR）、文字识别（OCR）、音素对齐、声纹分析及语音情感分析等相关数据集与工具。
*   **数据增强与评测基准**：提供 EDA 数据增强工具、NLP 竞赛高分方案复盘、各类中文 NLP 数据集搜索平台及语言理解测评基准。

**3. 适用场景**
*   **中文 NLP 算法研发**：适合需要快速接入分词、NER、情感分析等基础模块，或寻找预训练模型进行微调的算法工程师。
*   **垂直领域知识库构建**：适用于医疗、金融、法律、汽车等行业，利用其提供的专用词库和关系抽取工具构建领域知识图谱。
*   **智能客服与对话系统开发**：开发者可参考其中的对话机器人框架、闲聊语料库、QA 数据集及意图识别模型，搭建智能问答系统。
*   **NLP 学习与竞赛备战**：适合学生和研究人员通过阅读其中的论文梳理、竞赛 Top 方案解析及基准测试数据，快速掌握 NLP 前沿技术。

**4. 技术亮点**
*   **资源极度丰富且分类清晰**：不仅包含代码工具，还整合了从基础词典到前沿论文、竞赛代码的全链条资源，极大降低了中文 NLP 的学习门槛。
*   **紧跟前沿模型落地**：及时收录了 BERT、GPT-2、ALBERT、ELECTREA 等最新预训练模型的中文适配版本及实战案例。
*   **覆盖多模态与细粒度任务**：除了传统文本处理，还涵盖了 OCR、ASR、实体链接、细粒度情感分析等复杂场景的工具和数据集。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82061 | 🍴 15256 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目荣获 ACL 2024 会议认可，旨在简化从基础模型到专用智能体的全流程开发体验。

### 2. 核心功能
- **多模型统一微调**：原生支持 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种 LLM 及 VLM 的高效微调。
- **多种微调算法集成**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调（PEFT）技术，并支持全量微调。
- **高级训练策略支持**：提供 RLHF（基于人类反馈的强化学习）、DPO 及 ORPO 等对齐训练方法。
- **量化与低资源优化**：支持 GGUF/GPTQ 等量化格式加载，降低显存需求，适配低配置硬件。
- **一站式工作流**：涵盖数据预处理、模型训练、推理评估及导出，实现端到端的模型定制流程。

### 3. 适用场景
- **企业级私有化部署**：利用 QLoRA 等技术，在有限显存下快速微调开源模型以适配垂直领域知识。
- **多模态应用开发**：对包含图像和文本的 VLM 进行指令微调，构建具备视觉理解能力的智能助手。
- **模型对齐与优化**：通过 RLHF/DPO 对齐训练，提升模型在特定任务中的安全性、有用性及指令遵循能力。
- **学术研究与实验**：作为标准化的微调基准平台，快速验证不同模型架构或训练策略的效果。

### 4. 技术亮点
- **极致易用性**：通过 YAML 配置文件即可管理复杂的数据集和训练超参数，无需编写大量代码。
- **高性能推理后端**：深度集成 vLLM、SGLang 等高速推理引擎，显著提升生成速度与吞吐量。
- **细粒度控制**：支持损失掩码、注意力机制优化及自定义回调函数，满足精细化调参需求。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73523 | 🍴 8986 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的通识性人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由微软发起，通过Jupyter Notebook提供互动式学习体验，覆盖从机器学习基础到深度学习的高级主题。

2. **核心功能**
- 提供结构化的12周学习路径，每课包含讲解、笔记和作业。
- 基于Jupyter Notebook实现交互式编码与即时反馈的学习环境。
- 涵盖广泛的AI领域，包括机器学习、计算机视觉、NLP及生成模型等。
- 专为初学者设计，无需深厚数学或编程背景即可上手。
- 由微软开发者倡导社区支持，确保内容的实用性和前沿性。

3. **适用场景**
- 计算机科学或相关专业的学生用于补充课堂外的AI实践知识。
- 希望转行进入人工智能领域的非技术背景从业者进行技能重塑。
- 教育工作者寻找现成的、模块化的AI教学大纲和实验材料。
- 对AI感兴趣的公众人士进行系统性自学和科普了解。

4. **技术亮点**
- 采用“做中学”理念，将理论概念直接嵌入可执行的代码笔记本中。
- 内容紧跟业界主流技术栈，如CNN、RNN、GAN和Transformer架构的基础应用。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52895 | 🍴 10744 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在指导学习者从底层原理出发，深入理解并构建人工智能系统。它强调“学习、构建、交付”的完整闭环，帮助用户掌握将AI技术转化为实际产品的能力。

2. **核心功能**
- 提供从零开始构建大语言模型（LLM）和生成式AI的教程与代码实现。
- 涵盖智能体（Agents）、多智能体系统（Swarm Intelligence）及模型上下文协议（MCP）的开发。
- 结合计算机视觉与自然语言处理技术，演示深度学习在复杂场景中的应用。
- 支持使用Python、Rust和TypeScript等多种编程语言进行工程化实践。

3. **适用场景**
- AI工程师希望深入理解Transformer架构及底层算法原理，而非仅调用API。
- 开发者意图构建自主运行的AI智能体或复杂的自动化工作流系统。
- 教育机构或个人学习者需要一套完整的、涵盖理论与实践的AI工程课程。

4. **技术亮点**
- 采用多语言栈（Python/Rust/TypeScript），兼顾开发效率与执行性能。
- 紧跟前沿技术趋势，涵盖MCP、强化学习和群体智能等高级主题。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43659 | 🍴 7332 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数以及深度学习框架（PyTorch、TensorFlow 2）和自然语言处理库（NLTK）的综合学习项目。它通过 Python 语言实现，旨在帮助开发者系统性地掌握从基础算法到高级模型构建的全过程。该项目集成了多种经典与前沿的 AI 技术栈，适合希望深入理解机器学习原理及工程实践的用户。

2. **核心功能**
- 提供完整的机器学习算法实现，包括回归、分类、聚类及推荐系统等。
- 集成深度学习框架实战，涵盖 DNN、RNN、LSTM 等网络结构及 PyTorch/TF2 应用。
- 包含自然语言处理（NLP）模块，利用 NLTK 进行文本分析与处理。
- 结合数学基础教学，讲解线性代数在机器学习中的应用。
- 实现多种经典算法如 SVM、K-Means、AdaBoost、Apriori 等源码解析。

3. **适用场景**
- 机器学习初学者系统化学习与算法复现。
- 数据科学家进行特征工程与模型调优参考。
- 深度学习工程师探索 NLP 或序列建模实战案例。
- 高校学生辅助课程学习，补充线性代数与 AI 理论实践。

4. **技术亮点**
- 技术栈全面，融合传统机器学习、深度学习与自然语言处理三大领域。
- 源码丰富且注释清晰，涵盖 scikit-learn 及主流深度学习框架的多维度实现。
- 社区认可度高，拥有超过 4 万星标，证明其作为学习资源的广泛适用性与质量。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42416 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35725 | 🍴 7381 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33774 | 🍴 4698 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28825 | 🍴 3517 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26017 | 🍴 2952 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21764 | 🍴 3310 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI项目的代码仓库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目以“Awesome”列表的形式整理，为开发者提供了丰富的实战案例和参考资源。

2. **核心功能**
- 提供大规模AI项目集合，覆盖机器学习至深度学习的完整技术栈。
- 包含计算机视觉与自然语言处理的具体实现代码及解决方案。
- 作为精选资源库（Awesome List），便于快速检索和学习各类AI应用。
- 统一整合多领域的开源项目，降低AI入门与进阶的学习门槛。

3. **适用场景**
- AI初学者通过阅读和复现代码来快速掌握主流算法原理。
- 开发者寻找特定任务（如图像分类、文本生成）的参考实现。
- 研究人员或工程师进行技术调研，了解当前AI领域的最新实践。
- 教育机构或个人学习时，利用真实项目案例进行教学或自学。

4. **技术亮点**
- 规模宏大且分类清晰，一站式解决多领域AI学习需求。
- 强调“带代码”的实操性，不仅提供理论，更侧重工程落地。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35725 | 🍴 7381 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够利用计算机视觉和大型语言模型（LLM）来自动化基于浏览器的复杂工作流。它通过模拟人类操作浏览器的方式，实现了无需编写传统代码即可处理网页交互的功能。该项目旨在提供比传统 RPA 更灵活、更智能的浏览器自动化解决方案。

2. **核心功能**
- 基于 AI 的视觉理解：利用计算机视觉识别网页元素，替代传统的 CSS 选择器或 XPath。
- 自然语言驱动自动化：用户可通过自然语言指令定义任务，AI 自动解析并执行相应的浏览器操作。
- 跨框架兼容性：底层支持 Playwright 和 Puppeteer 等主流浏览器自动化引擎，兼顾性能与稳定性。
- 智能决策能力：在处理动态网页或异常情况时，AI 能自主判断下一步操作，提高任务成功率。
- 端到端工作流编排：支持从登录、数据抓取到表单填写等完整业务流程的自动化执行。

3. **适用场景**
- 企业级数据抓取：自动访问需要登录或具有反爬机制的网站，提取结构化业务数据。
- 在线业务自动化：自动化完成报销申请、订单录入、库存更新等重复性办公流程。
- 跨平台测试验证：对 Web 应用进行端到端的功能测试，模拟真实用户行为以发现潜在 Bug。
- 老旧系统集成：在不修改原有系统代码的情况下，通过浏览器界面自动化对接遗留系统。

4. **技术亮点**
- 融合了 LLM 的逻辑推理能力与 Computer Vision 的环境感知能力，实现类人操作。
- 提供 API 接口，便于将浏览器自动化能力集成到现有的后端服务或 Agent 系统中。
- 相比 Selenium 等传统工具，对前端页面结构变化的鲁棒性更强，维护成本更低。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22595 | 🍴 2118 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，支持图像、视频及 3D 标注，并提供 AI 辅助标注、质量保证及团队协作等功能。它提供开源、云端和企业版产品以及标注服务，旨在通过完善的 API 和分析工具赋能视觉 AI 开发。

2. **核心功能**
*   支持图像、视频和 3D 数据的多模态高精度标注。
*   集成 AI 辅助标注技术以显著提升数据标注效率。
*   提供完善的质量保证机制与团队多人协作功能。
*   内置数据分析看板及开发者 API，便于集成与工作流管理。

3. **适用场景**
*   计算机视觉模型训练所需的大规模高质量数据集构建。
*   自动驾驶或监控视频中复杂目标的检测与语义分割标注。
*   企业级团队协同进行视觉数据标注及质量控制管理。

4. **技术亮点**
*   采用 Python 语言开发，深度兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   提供从开源私有部署到云端 SaaS 服务的灵活交付模式。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16386 | 🍴 3775 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目提供面向计算机视觉的高级AI可解释性工具，支持CNN和Vision Transformers等多种架构。它涵盖了分类、目标检测、分割及图像相似度分析等多种任务的可视化需求。旨在通过Grad-CAM等技术提升深度学习模型的透明度与可理解性。

2. **核心功能**
*   支持多种主流视觉模型架构，包括卷积神经网络（CNN）和视觉Transformer。
*   兼容多种下游任务，如图像分类、目标检测、语义分割和图像相似性计算。
*   实现多种可视化技术，涵盖经典的Grad-CAM以及Score-CAM等方法。
*   提供丰富的解释性AI（XAI）工具，帮助用户直观理解模型决策依据。

3. **适用场景**
*   深度学习研究人员需要可视化模型关注区域以验证特征提取的有效性。
*   医疗影像分析师希望通过热力图辅助诊断，明确模型判断病灶的依据。
*   自动驾驶开发者需调试目标检测算法，分析模型对特定物体的识别逻辑。
*   教育或科普场景中，向非技术人员展示AI如何“看见”和理解图像内容。

4. **技术亮点**
*   广泛支持最新视觉架构，特别是针对Vision Transformer的适配能力。
*   集成多种SOTA可解释性算法，提供比单一方法更全面的分析视角。
*   拥有高社区认可度（近1.3万星标），代码成熟度高且文档完善。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12930 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了一整套可微分的图像处理与几何计算工具。该库旨在简化计算机视觉模型的开发，使其能够无缝集成到深度学习工作流中。

**2. 核心功能**
*   提供可微分的几何计算机视觉算法，支持梯度反向传播。
*   包含丰富的图像预处理、变换及增强模块，兼容 PyTorch 张量操作。
*   支持相机标定、单应性矩阵计算等高级几何视觉任务。
*   与主流深度学习框架深度集成，便于构建端到端的视觉模型。

**3. 适用场景**
*   **自动驾驶感知系统**：用于实时处理激光雷达或摄像头数据，进行几何特征提取。
*   **机器人视觉导航**：帮助机器人理解三维空间结构，实现精准定位与路径规划。
*   **可微分渲染与仿真**：在生成式 AI 或数字孪生场景中，结合深度学习进行精确的图像合成与分析。

**4. 技术亮点**
*   **全可微设计**：传统计算机视觉中的几何运算均可微，允许直接嵌入神经网络的损失函数中进行优化。
*   **PyTorch 原生集成**：完全基于 PyTorch 张量实现，无需在 NumPy 和深度学习框架间转换数据，提升训练效率。
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
- ### GitHub项目分析：openclaw

**1. 中文简介**
OpenClaw 是一款强调数据隐私和个人所有权的 AI 助手，支持跨操作系统和平台运行。它采用独特的“龙虾”风格（Lobster way），旨在让用户完全掌控自己的 AI 体验。

**2. 核心功能**
*   **全平台兼容**：支持在任何操作系统和平台上部署个人 AI 助手。
*   **数据主权**：强调“拥有你的数据”，确保用户隐私和数据安全。
*   **TypeScript 架构**：基于 TypeScript 构建，保证代码的可维护性和类型安全。
*   **开源社区驱动**：标签中包含“molty”等社区元素，体现其开放和协作的开发模式。
*   **个性化定制**：作为个人助手，可根据用户需求进行灵活配置。

**3. 适用场景**
*   **隐私敏感型用户**：需要完全控制个人数据、不希望数据上传至第三方云服务的开发者或专业人士。
*   **多设备办公者**：希望在 Windows、macOS、Linux 等不同设备上无缝同步和使用同一 AI 助手的用户。
*   **AI 爱好者与开发者**：对开源 AI 助手感兴趣，并希望基于 TypeScript 进行二次开发或研究的技术人员。
*   **个人效率提升者**：需要一个定制化、无广告且专注于个人任务的智能助理来优化日常工作流程的用户。

**4. 技术亮点**
*   **跨平台原生支持**：通过 TypeScript 实现真正的跨操作系统兼容性，无需依赖特定环境。
*   **本地优先架构**：设计上倾向于本地运行或私有部署，强化数据安全性和响应速度。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 384200 | 🍴 80719 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理式技能框架及软件开发方法论。它通过子代理驱动的开发模式，将人工智能能力深度融入软件开发生命周期（SDLC）。该项目旨在提供一套切实可行的方案，以提升代码生成、头脑风暴及技能执行的整体效率。

2. **核心功能**
*   **子代理驱动开发**：利用专门的子代理处理特定任务，实现模块化的智能辅助。
*   **全生命周期集成**：覆盖从需求分析到代码实现的完整 SDLC 流程。
*   **自动化技能框架**：提供可复用的 AI 技能组件，简化复杂任务的编排。
*   **交互式协作**：支持开发者与 AI 进行高效的头脑风暴和代码共创。

3. **适用场景**
*   希望引入 AI 代理来加速常规编码和调试任务的研发团队。
*   需要标准化 AI 辅助流程，以建立统一软件开发方法论的企业。
*   探索“子代理驱动”新模式，以优化复杂软件架构设计的工程师。

4. **技术亮点**
*   率先将“代理式技能框架”概念落地为具体的 Shell 脚本工具链。
*   标签中特有的 `obra` 和 `subagent-driven-development` 体现了其独特的架构理念。
- 链接: https://github.com/obra/superpowers
- ⭐ 261454 | 🍴 23334 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **1. 中文简介**
Hermes Agent 是一个旨在伴随用户共同成长的智能代理工具。它深度整合了主流大语言模型（如 Claude、GPT 等），提供灵活且强大的自动化交互能力。该项目致力于成为开发者日常编码与任务处理的高效辅助伙伴。

**2. 核心功能**
*   **多模型支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT) 等多种主流 LLM 后端。
*   **自主代理能力**：具备代码执行、文件操作及复杂任务拆解与自动执行的能力。
*   **高度可定制**：提供模块化架构，允许用户根据需求灵活配置提示词和工作流。
*   **CLI 集成**：提供命令行界面，便于在开发环境中快速调用和集成。

**3. 适用场景**
*   **自动化代码生成与重构**：通过自然语言指令自动生成代码片段或优化现有代码结构。
*   **复杂任务自动化**：处理需要多步骤逻辑判断的重复性开发任务或运维脚本编写。
*   **交互式编程助手**：作为本地终端的智能伴侣，实时解答技术疑问并执行测试用例。

**4. 技术亮点**
*   **轻量化与高性能**：基于 Python 构建，资源占用低，响应速度快。
*   **生态兼容性**：紧密围绕 AI Agent 热门标签（如 Codex, Moltbot），保持对最新模型特性的快速适配。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220782 | 🍴 42069 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码，并提供自托管或云端部署选项。它拥有超过 400 种集成连接，旨在通过低代码/无代码方式高效实现复杂的业务流程自动化。

2. **核心功能**
*   **可视化工作流引擎**：提供拖拽式界面，支持复杂数据流和逻辑分支的直观构建。
*   **原生 AI 集成**：内置人工智能能力，允许在工作流中直接调用 LLM 或进行智能数据处理。
*   **丰富的生态集成**：预置 400+ 种应用接口，涵盖主流 SaaS 服务、数据库及 API 连接。
*   **灵活部署模式**：支持完全自托管以保障数据隐私，同时也提供便捷的云服务版本。
*   **混合开发模式**：兼顾无代码的低门槛操作与 TypeScript 自定义代码编写的灵活性。

3. **适用场景**
*   **企业级数据同步**：在不同 SaaS 平台（如 Salesforce 到 Slack）之间自动同步客户数据和通知。
*   **AI 驱动的内容处理**：利用内置 AI 节点自动总结文档、生成营销文案或分析用户反馈。
*   **内部系统自动化**：替代传统脚本，通过可视化流程自动化审批、报表生成等重复性运维任务。

4. **技术亮点**
*   **Fair-code 许可**：在开源基础上采用公平代码许可，平衡了社区贡献与商业使用的权益。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，增强了与各种 AI 模型和工具的互操作性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198084 | 🍴 59642 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建人工智能应用，其愿景是打造普惠型 AI。我们的使命是提供完善的工具链，让用户能够专注于核心业务与创新价值。

2. **核心功能**
*   支持基于 GPT、LLaMA 等主流大语言模型的自主智能体开发。
*   提供丰富的插件接口，允许连接 Claude API、OpenAI 等服务及外部工具。
*   具备自动化任务执行能力，可独立规划并完成复杂的多步工作流。
*   开源且高度可扩展，便于开发者基于现有框架进行二次定制与优化。

3. **适用场景**
*   自动化日常办公流程，如数据整理、邮件回复和信息摘要生成。
*   构建复杂的 Web 搜索与信息聚合代理，实现跨平台的数据抓取与分析。
*   开发具备自主决策能力的 AI 助手，用于客户服务或个性化推荐系统。
*   作为学习 LLM 应用开发的实验平台，探索智能体在现实场景中的边界。

4. **技术亮点**
*   采用模块化架构设计，兼容多种后端大模型（如 OpenAI、Anthropic、Hugging Face）。
*   强调“无代码/低代码”入门体验，降低构建自主 AI 智能体的技术门槛。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185699 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166387 | 🍴 21495 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164277 | 🍴 30448 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157310 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156300 | 🍴 8885 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152428 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

