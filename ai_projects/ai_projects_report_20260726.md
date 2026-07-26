# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### OptMem
- **1. 中文简介**
OptMem 旨在为 AI 智能体提供永久记忆能力。它通过一个仅需 333 token 的提示词和一个脚本实现即插即用的部署，极大地降低了集成难度。

**2. 核心功能**
- 为 AI 智能体提供持久化的长期记忆存储功能。
- 采用极简的 333 token 提示词设计，优化上下文窗口占用。
- 提供即插即用的脚本接口，便于快速集成到现有系统中。
- 基于 Python 开发，确保代码的易读性与扩展性。

**3. 适用场景**
- 需要长期交互且保持上下文连贯性的多轮对话机器人。
- 希望在不显著增加 Token 成本的前提下增强智能体记忆能力的开发者项目。
- 需要快速原型验证或轻量级部署的智能体应用开发。

**4. 技术亮点**
- **极致精简**：仅用 333 token 即可实现复杂的记忆管理逻辑，效率极高。
- **低门槛集成**：通过“即插即用”的设计，用户无需复杂配置即可启用永久记忆功能。
- 链接: https://github.com/VictorTaelin/OptMem
- ⭐ 81 | 🍴 3 | 语言: Python

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时框架，旨在将编排逻辑保留在 TypeScript 中，同时将语义处理委托给可替换的 Agent 运行时。这种设计实现了业务逻辑与 AI 执行单元的解耦，提升了系统的灵活性和可扩展性。

2. **核心功能**
- 支持动态工作流运行时，允许在工作执行过程中灵活调整流程。
- 将编排代码严格保持在 TypeScript 环境中，确保类型安全和开发体验。
- 采用可插拔架构，允许用户替换底层的 Agent 运行时以适配不同需求。
- 支持语义化工作委托，将复杂的 AI 决策任务交给专门的 Agent 处理。

3. **适用场景**
- 需要高度定制化 AI 工作流的复杂应用开发。
- 希望将业务逻辑与 AI 推理过程分离的微服务架构。
- 基于 Bun 运行时的高性能 Node.js 应用开发。
- 实验性或原型阶段的 LLM（大语言模型）集成项目。

4. **技术亮点**
- 深度集成 TypeScript 类型系统，提供编译时错误检查。
- 原生支持 Bun 运行时，带来更快的启动速度和执行性能。
- 模块化设计使得更换底层 AI 引擎（如不同厂商的 LLM 或 Agent 框架）变得非常简单。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 75 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- ### 1. 中文简介
该项目是一个 MCP（模型上下文协议）服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心来操作多集群 Kubernetes 舰队。它在模型与你的集群之间提供了策略控制、审批流程以及审计功能，确保 AI 操作的合规性与安全性。

### 2. 核心功能
- **多集群管理**：通过 OCM 中心统一调度和管理多个 Kubernetes 集群。
- **AI 智能体集成**：基于 MCP 标准，使 AI 智能体能够直接执行集群操作。
- **策略与安全控制**：在 AI 与基础设施之间实施严格的访问策略和权限管理。
- **审批工作流**：提供关键操作的中间审批环节，防止未经授权的变更。
- **操作审计**：记录所有由 AI 发起的操作，便于后续的安全审查和问题追踪。

### 3. 适用场景
- **大规模云原生运维**：在多集群环境中利用 AI 自动化执行日常维护任务。
- **高安全要求的企业部署**：在金融或政府等对合规性敏感的场景中，通过审批机制控制 AI 的变更权限。
- **DevOps 自动化增强**：将 AI 能力集成到现有的 CI/CD 流水线中，实现智能化的资源管理和故障恢复。

### 4. 技术亮点
- **标准化接口**：采用 MCP 协议，实现了 AI 模型与基础设施管理工具之间的标准化交互。
- **集中式治理**：利用 OCM 的多集群管理能力，简化了分布式 Kubernetes 环境的 AI 接入复杂度。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 36 | 🍴 3 | 语言: Python

### Prompt-architect
- **项目名称：** Prompt-architect (提示词架构师)

**中文简介**
Prompt Architect Pro 是一款基于 Python 开发的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能将视觉描述提取并结构化为优化的 JSON 格式提示词，以服务于生成式 AI，同时内置 SQLite 数据库用于提示词管理，并支持可调节的显存硬件配置文件及 ComfyUI 节点集成。

**核心功能**
1. **本地化分析**：利用本地 Ollama LLM 处理文本与图像数据，确保隐私与低延迟。
2. **结构化输出**：将非结构化的视觉描述转化为优化后的 JSON 提示词，便于 AI 直接调用。
3. **数据库管理**：内置 SQLite 数据库，支持用户编辑、存储和管理生成的提示词。
4. **硬件适配**：提供可调的 VRAM（显存）硬件配置文件，以适应不同显卡性能。
5. **ComfyUI 集成**：包含专用节点，可直接读取数据库中的提示词供 ComfyUI 工作流使用。

**适用场景**
1. **Stable Diffusion/ComfyUI 用户**：需要批量生成或从图像中提取高质量、结构化 JSON 提示词的工作流需求。
2. **隐私敏感型开发者**：希望在本地环境中运行，避免数据上传至云端，同时利用大模型进行视觉描述分析的场景。
3. **自动化内容创作**：需要将视觉输入自动转换为标准格式提示词，进而驱动其他生成式 AI 模型的自动化管道。

**技术亮点**
- **软硬结合**：通过 VRAM 配置文件实现了对本地不同硬件资源的灵活调度。
- **生态互通**：原生支持与 ComfyUI 及 SQLite 的深度集成，打通了从分析到生成的数据链路。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 34 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
该项目是一个基于人工智能的产业链股票池，支持美股与A股的映射分析。它具备主动发现潜力标的、评估政策压力以及一键部署到云平台的特性，旨在辅助投资决策。

2. **核心功能**
*   建立美股与A股产业链的深度映射关系，实现跨市场投资参考。
*   利用AI技术主动挖掘产业链中的潜在机会并生成研究数据。
*   集成政策压力测试模块，量化分析宏观政策对特定板块的影响。
*   支持在Cloudflare Workers和Vercel等平台上进行一键快速部署。
*   整合ArXiv学术资源，为股票研究提供前沿理论或模型支持。

3. **适用场景**
*   量化投资者构建基于AI产业链逻辑的多因子选股策略。
*   研究人员利用A股/美股映射关系进行跨境套利或对比分析。
*   开发者快速搭建并部署个性化的股票监控与研报生成服务。
*   需要实时跟踪政策变动对科技或制造业板块影响的金融从业者。

4. **技术亮点**
*   采用Serverless架构（Cloudflare Workers/Vercel），实现低成本、高可用的全球边缘计算部署。
*   融合学术文献（ArXiv）与市场数据，提升AI驱动投资决策的深度与前瞻性。
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

### succhia
- 描述: 在 iPhone 上让 AI 一边陪聊一边控制 BLE 玩具:聊天融合防冻结 + 可靠性层 + 多通道波形引擎 (Bluefy/Chrome, 无需额外硬件)
- 链接: https://github.com/29-Cu/succhia
- ⭐ 17 | 🍴 2 | 语言: HTML

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且功能丰富的中文自然语言处理资源库，集成了敏感词检测、实体抽取（如手机号、身份证）、词典库及情感分析等基础工具。它不仅提供了海量的预训练模型和语料数据，还涵盖了从传统NLP任务到基于BERT等深度学习模型的先进应用，是开发者进行中文NLP研究的宝贵资源集合。

2. **核心功能**
- **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表以及基础的中文分词和词性标注工具。
- **信息抽取与实体识别**：支持手机号、邮箱、身份证等敏感信息的自动抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
- **大规模知识库与词典集成**：内置中日文人名库、职业名称、汽车品牌、古诗词、成语及多领域专业词库，并包含同义词、反义词及否定词库。
- **高级NLP模型与数据集**：收录了多种预训练语言模型（如BERT, RoBERTa, ALBERT）、大型问答数据集（如百度知道、医学对话）、知识图谱构建工具及语音识别相关资源。
- **实用工具与算法实现**：提供文本相似度计算、摘要生成、聊天机器人框架、OCR识别、手写汉字识别以及各类NLP任务的基准测试代码。

3. **适用场景**
- **内容安全审核**：利用敏感词库和情感分析工具，快速搭建网站或APP的内容过滤系统，识别违规文本和不良情绪。
- **智能客服与对话系统开发**：借助其中的闲聊语料、对话机器人框架及知识图谱资源，构建具备语义理解和多轮对话能力的智能助手。
- **金融/医疗垂直领域信息抽取**：利用专门的金融、医疗词库及NER模型，从非结构化文档中自动提取关键实体（如药品名、病症、股票信息）以构建行业知识图谱。
- **NLP教学与研究基准测试**：作为研究人员或学生的资源仓库，使用其中提供的标准数据集、预训练模型和Baseline代码进行算法对比和新方法验证。

4. **技术亮点**
- **资源极度丰富**：该项目并非单一工具，而是一个聚合了数百个高质量NLP资源、数据集、论文复现和开源库的“超级目录”，极大降低了资料搜集成本。
- **覆盖全链路NLP任务**：从底层的分词、词向量，到中层的实体抽取、句法分析，再到上层的问答系统、文本生成和知识图谱，覆盖了自然语言处理的主要应用场景。
- **紧跟前沿技术**：及时收录了BERT、GPT-2、ALBERT等最新预训练语言模型在中文领域的适配版本及应用案例，确保技术栈的先进性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的代码实现，帮助开发者快速掌握相关技术并构建实际应用场景。

2. **核心功能**
- 汇集500个经过验证的AI项目代码，覆盖主流算法与模型。
- 提供从基础机器学习到前沿深度学习的完整技术栈支持。
- 专注于计算机视觉与自然语言处理两大热门领域的实战应用。
- 所有项目均附带可运行的源代码，便于直接复现与学习。
- 作为“Awesome”系列资源，筛选出高质量且具代表性的开源项目。

3. **适用场景**
- AI初学者希望通过大量实例代码快速入门并理解核心概念。
- 数据科学家寻找特定任务（如图像分类、文本生成）的参考实现。
- 开发者在需要快速原型开发时，直接复用或微调现有项目代码。
- 教育培训机构用于制作教学案例或布置编程作业。

4. **技术亮点**
- 内容全面：一站式整合机器学习、深度学习、CV和NLP四大方向。
- 实战导向：强调“with code”，提供可直接执行的工程化解决方案而非仅理论介绍。
- 社区认可：拥有超过35,000星标，证明其在AI学习资源中的高价值与广泛影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。该项目在 GitHub 上拥有超过 33,000 颗星标，是 AI 领域广泛使用的开源工具。

2. **核心功能**
- 支持加载并可视化多种格式的模型文件，如 Keras、PyTorch、TensorFlow、ONNX 等。
- 提供清晰的层结构视图，展示神经网络的数据流和连接关系。
- 允许用户交互探索模型参数、权重及激活值等详细信息。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定部署格式。
- 基于 JavaScript 构建，可在浏览器中直接运行，无需安装重型本地依赖。

3. **适用场景**
- 研究人员调试深度学习模型时，快速检查网络架构是否正确。
- 开发者将训练好的模型转换为 ONNX 或其他格式后，验证转换结果的完整性。
- 教育场景中，向学生直观演示复杂神经网络的内部工作原理和数据流向。
- 工程团队在模型部署前，对不同框架下的模型进行兼容性检查和结构分析。

4. **技术亮点**
- 跨平台兼容性强，通过 Web 技术实现即开即用的模型可视化体验。
- 广泛支持主流 AI 框架及其衍生格式，覆盖从开发到部署的全生命周期。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是用于机器学习模型互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型格式的统一与转换。该项目由微软、Facebook等科技巨头联合推动，致力于简化AI模型的部署流程。

2. **核心功能**
- 提供统一的模型表示格式，支持跨框架的模型数据交换。
- 允许在不同深度学习框架（如PyTorch、TensorFlow、Keras）之间无缝转换模型。
- 包含丰富的算子库，覆盖主流神经网络层和数学运算。
- 支持将模型转换为多种执行后端（如ONNX Runtime），优化推理性能。

3. **适用场景**
- 在多框架混合开发环境中进行模型迁移和原型验证。
- 需要将训练好的模型部署到不支持原生训练框架的边缘设备或生产环境。
- 希望利用高性能推理引擎加速模型预测，降低延迟和资源消耗。
- 构建需要兼容多种AI工具链的企业级机器学习平台。

4. **技术亮点**
- 拥有强大的社区支持和行业联盟背书，标准化程度高。
- ONNX Runtime 提供跨平台、跨硬件的高效推理加速能力。
- 保持向后兼容性，确保旧版模型在新版本工具中仍可运行。
- 链接: https://github.com/onnx/onnx
- ⭐ 21215 | 🍴 3976 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一部全面涵盖机器学习工程实践的开源指南。它深入探讨了从大规模模型训练、推理优化到MLOps部署的全链路技术细节，旨在为工程师提供系统化的最佳实践参考。

2. **核心功能**
- 提供大规模分布式训练的调试与优化策略，特别针对PyTorch和Transformer架构。
- 详解大语言模型（LLM）的高效推理技术及GPU资源调度方案。
- 涵盖MLOps全流程，包括可扩展性设计、存储管理、网络配置及Slurm集群管理。

3. **适用场景**
- 需要部署和优化大型语言模型（LLM）推理服务的研发团队。
- 致力于构建高可用、可扩展机器学习基础设施的MLOps工程师。
- 希望解决大规模分布式训练中出现性能瓶颈或调试难题的高级算法工程师。

4. **技术亮点**
该项目将理论工程实践与前沿的大模型技术相结合，重点解决了LLM时代特有的算力效率、显存管理及分布式通信等复杂工程挑战，是连接传统ML与生成式AI工程落地的实用手册。
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
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的代码实现，帮助开发者快速掌握相关技术并构建实际应用场景。

2. **核心功能**
- 汇集500个经过验证的AI项目代码，覆盖主流算法与模型。
- 提供从基础机器学习到前沿深度学习的完整技术栈支持。
- 专注于计算机视觉与自然语言处理两大热门领域的实战应用。
- 所有项目均附带可运行的源代码，便于直接复现与学习。
- 作为“Awesome”系列资源，筛选出高质量且具代表性的开源项目。

3. **适用场景**
- AI初学者希望通过大量实例代码快速入门并理解核心概念。
- 数据科学家寻找特定任务（如图像分类、文本生成）的参考实现。
- 开发者在需要快速原型开发时，直接复用或微调现有项目代码。
- 教育培训机构用于制作教学案例或布置编程作业。

4. **技术亮点**
- 内容全面：一站式整合机器学习、深度学习、CV和NLP四大方向。
- 实战导向：强调“with code”，提供可直接执行的工程化解决方案而非仅理论介绍。
- 社区认可：拥有超过35,000星标，证明其在AI学习资源中的高价值与广泛影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。该项目在 GitHub 上拥有超过 33,000 颗星标，是 AI 领域广泛使用的开源工具。

2. **核心功能**
- 支持加载并可视化多种格式的模型文件，如 Keras、PyTorch、TensorFlow、ONNX 等。
- 提供清晰的层结构视图，展示神经网络的数据流和连接关系。
- 允许用户交互探索模型参数、权重及激活值等详细信息。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定部署格式。
- 基于 JavaScript 构建，可在浏览器中直接运行，无需安装重型本地依赖。

3. **适用场景**
- 研究人员调试深度学习模型时，快速检查网络架构是否正确。
- 开发者将训练好的模型转换为 ONNX 或其他格式后，验证转换结果的完整性。
- 教育场景中，向学生直观演示复杂神经网络的内部工作原理和数据流向。
- 工程团队在模型部署前，对不同框架下的模型进行兼容性检查和结构分析。

4. **技术亮点**
- 跨平台兼容性强，通过 Web 技术实现即开即用的模型可视化体验。
- 广泛支持主流 AI 框架及其衍生格式，覆盖从开发到部署的全生命周期。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究人员提供了必备的基础知识速查表（Cheat Sheets）。它涵盖了从核心算法到常用工具库的关键概念，旨在帮助研究者快速回顾和掌握技术要点。这些资源源自 Medium 上的专业文章，经过整理以方便查阅。

2. **核心功能**
- 提供深度学习与机器学习领域的关键概念速查总结。
- 涵盖 Keras、Matplotlib、NumPy、SciPy 等常用库的使用技巧。
- 针对研究人员优化，便于快速回顾算法原理和代码实现。
- 整合了人工智能相关的基础知识框架。

3. **适用场景**
- 深度学习或机器学习初学者快速建立知识体系。
- 研究人员在开发过程中需要快速回顾特定函数或算法细节时。
- 面试准备中用于梳理 AI 领域的基础理论和工具使用。
- 日常编码时作为参考手册，提高开发效率。

4. **技术亮点**
- 高度浓缩的知识结构，适合碎片化学习或快速检索。
- 覆盖范围广，从数学基础到主流框架均有涉及。
- 社区认可度高（高星标数），内容经过广泛验证。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材。内容涵盖从零基础入门到就业实战的完整路径，适合希望系统掌握AI核心技能的学习者。

2. **核心功能**
*   提供结构化的AI学习路线，覆盖Python、数学及主流框架。
*   整理近200个实战案例，帮助学习者通过动手实践巩固知识。
*   免费开放配套教材资源，降低人工智能领域的学习门槛。
*   涵盖数据科学全栈技能，包括机器学习、深度学习及自然语言处理。
*   支持多种主流深度学习框架，如PyTorch、TensorFlow和Keras。

3. **适用场景**
*   零基础用户希望通过系统化路径入门人工智能领域。
*   在校学生或转行者利用实战项目准备求职面试。
*   数据分析师希望扩展技能树，深入掌握深度学习和计算机视觉技术。
*   AI从业者作为知识复习手册，快速查阅各子领域的核心概念与代码示例。

4. **技术亮点**
*   知识点覆盖面极广，整合了算法、数据处理、可视化及各大主流AI框架。
*   强调“实战驱动”，通过大量真实项目案例连接理论与应用。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置和自动化工作流，让开发者无需深入底层代码即可快速训练和部署模型。

2. **核心功能**
- 支持多种数据类型的端到端机器学习管道，涵盖文本、图像及结构化数据。
- 提供声明式 YAML 配置接口，实现无需编写复杂代码的模型定义与训练。
- 内置对主流深度学习框架（如 PyTorch）的支持，便于集成现有生态。
- 具备强大的可解释性工具，帮助用户理解模型决策逻辑及特征重要性。
- 支持从微调开源 LLM（如 Llama、Mistral）到传统神经网络的全方位建模需求。

3. **适用场景**
- 快速原型开发：数据科学家希望在不编写大量 Python 代码的情况下迅速验证 ML 想法。
- 多模态应用构建：需要同时处理文本、图像和表格数据的综合 AI 系统开发。
- 模型微调与部署：针对特定任务对 Llama 或 Mistral 等大模型进行高效微调并部署。
- 数据-centric AI 实验：专注于数据质量优化而非模型架构调整的迭代研究。

4. **技术亮点**
- 真正的低代码体验：通过简洁的配置即可触发复杂的分布式训练流程。
- 广泛的模型兼容性：无缝衔接 Hugging Face Transformers 等主流库，支持最新 SOTA 模型。
- 自动化的特征工程：根据数据类型自动推断并预处理输入特征，降低使用门槛。
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
- ⭐ 6295 | 🍴 756 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且功能丰富的中文自然语言处理资源库，集成了敏感词检测、实体抽取（如手机号、身份证）、词典库及情感分析等基础工具。它不仅提供了海量的预训练模型和语料数据，还涵盖了从传统NLP任务到基于BERT等深度学习模型的先进应用，是开发者进行中文NLP研究的宝贵资源集合。

2. **核心功能**
- **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表以及基础的中文分词和词性标注工具。
- **信息抽取与实体识别**：支持手机号、邮箱、身份证等敏感信息的自动抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
- **大规模知识库与词典集成**：内置中日文人名库、职业名称、汽车品牌、古诗词、成语及多领域专业词库，并包含同义词、反义词及否定词库。
- **高级NLP模型与数据集**：收录了多种预训练语言模型（如BERT, RoBERTa, ALBERT）、大型问答数据集（如百度知道、医学对话）、知识图谱构建工具及语音识别相关资源。
- **实用工具与算法实现**：提供文本相似度计算、摘要生成、聊天机器人框架、OCR识别、手写汉字识别以及各类NLP任务的基准测试代码。

3. **适用场景**
- **内容安全审核**：利用敏感词库和情感分析工具，快速搭建网站或APP的内容过滤系统，识别违规文本和不良情绪。
- **智能客服与对话系统开发**：借助其中的闲聊语料、对话机器人框架及知识图谱资源，构建具备语义理解和多轮对话能力的智能助手。
- **金融/医疗垂直领域信息抽取**：利用专门的金融、医疗词库及NER模型，从非结构化文档中自动提取关键实体（如药品名、病症、股票信息）以构建行业知识图谱。
- **NLP教学与研究基准测试**：作为研究人员或学生的资源仓库，使用其中提供的标准数据集、预训练模型和Baseline代码进行算法对比和新方法验证。

4. **技术亮点**
- **资源极度丰富**：该项目并非单一工具，而是一个聚合了数百个高质量NLP资源、数据集、论文复现和开源库的“超级目录”，极大降低了资料搜集成本。
- **覆盖全链路NLP任务**：从底层的分词、词向量，到中层的实体抽取、句法分析，再到上层的问答系统、文本生成和知识图谱，覆盖了自然语言处理的主要应用场景。
- **紧跟前沿技术**：及时收录了BERT、GPT-2、ALBERT等最新预训练语言模型在中文领域的适配版本及应用案例，确保技术栈的先进性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目荣获 ACL 2024 会议收录，旨在简化从指令微调到强化学习的完整训练流程。

2. **核心功能**
*   支持千余种模型架构的统一高效微调，涵盖 LLaMA、Qwen、Gemma 等主流基座。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法，降低显存需求。
*   提供完整的指令微调、全量微调及 RLHF（基于人类反馈的强化学习）训练流水线。
*   内置量化技术（如 BitsandBytes），支持 4-bit/8-bit 低精度训练，提升硬件兼容性。
*   兼容 Transformers 库生态，提供标准化的数据加载与模型评估接口。

3. **适用场景**
*   研究人员或开发者需要对多种不同架构的大模型进行快速对比实验和基准测试。
*   在显存受限的消费级 GPU 上，利用 QLoRA 等技术对大模型进行低成本微调。
*   企业或个人希望构建特定领域（如医疗、法律）的垂直行业专用模型。
*   需要执行从预训练数据清洗、指令格式化到强化学习对齐的全流程模型优化。

4. **技术亮点**
*   **高度统一性**：通过标准化接口屏蔽底层模型差异，实现“一套代码适配百种模型”。
*   **极致效率**：深度优化显存管理，结合最新量化算法，显著提升训练速度与资源利用率。
*   **学术认可**：作为 ACL 2024 收录项目，其代码质量和方法论经过严格学术评审，可靠性高。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73526 | 🍴 8987 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。项目通过Jupyter Notebook提供互动式学习体验，涵盖从基础概念到高级应用的广泛内容。

2. **核心功能**
- 提供结构化的12周学习路径，将复杂的人工智能知识分解为易于理解的24个课时。
- 基于Jupyter Notebook构建，支持代码执行与理论讲解相结合的互动式学习模式。
- 覆盖机器学习、深度学习、计算机视觉及自然语言处理等主流AI技术栈。
- 由Microsoft发起并维护，确保内容的专业性、准确性及教育价值。

3. **适用场景**
- 初学者希望系统性地从零开始学习人工智能理论与应用。
- 教育机构或教师用于辅助课堂教学，提供标准化的实验环境和案例。
- 开发者希望在短时间内快速了解AI核心概念及主流算法原理。
- 企业团队用于内部技术培训，提升员工对智能化技术的认知水平。

4. **技术亮点**
- 课程内容紧跟前沿技术，深入讲解CNN、RNN、GAN等关键深度学习架构。
- 强调“面向所有人”的教育理念，降低了高深AI技术的学习门槛。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52899 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入教授 AI 工程的核心原理与实践。它强调“学习、构建并部署”的闭环流程，帮助用户掌握将 AI 技术转化为实际可用产品的完整技能栈。

2. **核心功能**
- 涵盖从基础机器学习到生成式 AI 及大语言模型（LLM）的全栈知识体系。
- 提供基于 Python 和 Rust 的底层实现教程，帮助理解模型内部机制而非仅调用 API。
- 包含智能体（Agents）、多模态处理及强化学习等前沿领域的实战案例。
- 集成 MCP（Model Context Protocol）等新兴标准，探索 AI 与外部工具集成的最佳实践。

3. **适用场景**
- AI 初学者希望建立扎实的理论基础并掌握从头开发 AI 应用的能力。
- 工程师需要深入理解 Transformer 架构及底层算法，以优化或定制现有模型。
- 团队寻求构建具备自主决策能力的 AI 智能体或多智能体协作系统。
- 开发者希望了解如何将 AI 能力安全、高效地部署到生产环境中。

4. **技术亮点**
- 采用多语言栈（Python + Rust + TypeScript），兼顾开发效率与运行性能。
- 紧跟技术前沿，涵盖 Swarm Intelligence（群体智能）和 MCP 协议等最新趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43712 | 🍴 7351 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- **1. 中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch 及 TensorFlow 2.x 等内容的综合性学习项目。该项目还深入讲解了自然语言处理（NLTK）及相关算法，旨在为学习者提供从理论基础到工程实践的全方位指导。

**2. 核心功能**
*   **算法实战**：涵盖回归、SVM、KMeans、AdaBoost、Apriori、FP-Growth 等经典机器学习算法的代码实现。
*   **深度学习框架**：提供基于 PyTorch 和 TensorFlow 2 的深度学习模型构建与训练教程。
*   **NLP 与自然语言处理**：结合 NLTK 库进行文本处理、情感分析及推荐系统相关的 NLP 应用。
*   **数学基础强化**：通过代码实践讲解线性代数、PCA、SVD 等支撑机器学习的核心数学原理。
*   **模型分类详解**：详细解析逻辑回归、朴素贝叶斯、RNN、LSTM 以及 DNN 等各类监督与无监督学习模型。

**3. 适用场景**
*   **机器学习入门与进阶**：适合希望从零开始系统掌握传统 ML 算法及深度学习原理的学习者。
*   **算法工程师面试准备**：可作为复习经典算法推导与 Python 实现（sklearn/PyTorch）的资料库。
*   **NLP 项目实践参考**：为需要处理文本数据、构建推荐系统或进行情感分析的开发人员提供代码范例。
*   **高校课程辅助教材**：适用于需要将线性代数、概率统计与编程实战相结合的教学场景。

**4. 技术亮点**
*   **全栈知识体系**：将数学理论、经典统计学习与现代深度学习框架（PyTorch/TF2）有机融合，形成闭环。
*   **高热度社区认可**：拥有超过 42,000 颗星标，证明其在开源社区中具有极高的影响力和参考价值。
*   **多框架兼容**：同时支持 Scikit-learn 等传统库与 PyTorch/TF2 等现代深度学习框架，适应不同技术栈需求。
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
- ⭐ 33774 | 🍴 4698 | 语言: Python
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
- ⭐ 384222 | 🍴 80722 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261528 | 🍴 23343 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220861 | 🍴 42104 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198105 | 🍴 59647 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185699 | 🍴 46066 | 语言: Python
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
- ⭐ 157313 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156384 | 🍴 8889 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152439 | 🍴 9661 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

