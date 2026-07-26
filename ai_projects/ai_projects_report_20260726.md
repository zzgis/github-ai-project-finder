# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### OptMem
- 1. **中文简介**
OptMem 旨在为 AI 智能体提供永久记忆能力，通过仅 426 个 token 的提示词实现高效存储。该项目提供了一个即插即用的脚本，无需复杂配置即可快速集成到现有系统中。

2. **核心功能**
- 为 AI 智能体实现低成本且持久的记忆存储机制。
- 提供极简的提示工程方案，仅需少量 token 即可维持上下文。
- 包含开箱即用的自动化脚本，支持快速部署与集成。
- 采用即插即用架构，降低开发者接入技术门槛。

3. **适用场景**
- 需要长期对话记忆的多轮交互聊天机器人开发。
- 资源受限环境下对上下文窗口长度有严格限制的 AI 应用。
- 希望以最低成本快速验证智能体记忆功能的原型开发。
- 构建具备个性化用户档案或持续学习能力的 AI 代理。

4. **技术亮点**
- 极致优化：以仅 426 个 token 的高效率实现持久记忆功能。
- 链接: https://github.com/VictorTaelin/OptMem
- ⭐ 126 | 🍴 8 | 语言: Python

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时框架，允许开发者在 TypeScript 中保持编排逻辑。它将语义化任务委托给可替换的 Agent 运行时执行，实现了逻辑与推理的分离。

2. **核心功能**
*   支持动态工作流的运行时环境，提供灵活的任务调度能力。
*   使用 TypeScript 进行工作流编排，保证代码的类型安全和开发体验。
*   采用可插拔架构，将语义处理任务委托给可替换的 Agent 运行时。

3. **适用场景**
*   需要复杂业务逻辑编排且后端依赖多种 AI 模型的智能应用开发。
*   构建基于 LLM 的多步骤自动化工作流（如自动代码生成、数据分析流水线）。
*   希望解耦工作流控制逻辑与具体 AI 推理引擎的微服务架构项目。

4. **技术亮点**
*   实现了“编排逻辑”与“语义执行”的彻底解耦，提升了系统的可扩展性和灵活性。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 75 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- **1. 中文简介**
这是一个基于MCP（Model Context Protocol）协议的服务器，允许AI代理通过Open Cluster Management (OCM) 中心来操作多集群Kubernetes环境。它在模型与底层集群之间提供了策略管理、审批流程以及完整的审计功能。

**2. 核心功能**
*   支持通过单一中心节点控制多个Kubernetes集群。
*   集成Open Cluster Management以协调跨集群的操作。
*   提供策略执行机制以确保合规性。
*   包含人工或自动化的审批工作流。
*   记录所有操作的详细审计日志。

**3. 适用场景**
*   需要集中管理大规模多集群Kubernetes环境的DevOps团队。
*   希望通过自然语言交互简化复杂集群运维操作的工程师。
*   对云原生基础设施有严格合规和审计要求的企业级用户。
*   探索AI代理在基础设施即代码（IaC）中应用的研发场景。

**4. 技术亮点**
*   利用MCP协议实现AI模型与基础设施之间的标准化接口。
*   结合OCM实现细粒度的多集群策略控制和生命周期管理。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 36 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用，利用本地 Ollama 大语言模型分析原始文本和图像。它能将视觉描述提取并结构化，转化为用于生成式 AI 的优化 JSON 提示词。该应用内置 SQLite 数据库以便编辑提示词，支持可调整的 VRAM 硬件配置，并提供可与数据库联动的 ComfyUI 节点。

2. **核心功能**
*   本地化运行：使用 Ollama 模型在本地处理文本和图像分析任务，保障数据隐私。
*   智能结构化：自动将非结构化的视觉描述转换为优化的 JSON 格式提示词。
*   数据库管理：内置 SQLite 数据库，方便用户存储、检索和编辑生成的提示词。
*   资源优化：提供可调节的 VRAM 硬件配置文件，适配不同显存大小的显卡。
*   ComfyUI 集成：提供专用节点，可直接调用数据库中的提示词进行工作流操作。

3. **适用场景**
*   **AI 绘画工作流优化**：需要为 Stable Diffusion 或 Midjourney 等工具批量生成高质量、结构化的提示词。
*   **本地化内容创作**：在无网络环境或对数据隐私要求极高的情况下，进行图像到文本的分析与转换。
*   **ComfyUI 高级用户**：希望将提示词管理与 ComfyUI 生成流程无缝结合的技术型创作者。
*   **低配硬件部署**：拥有显存有限显卡的用户，通过调整 VRAM 配置在本地高效运行分析任务。

4. **技术亮点**
*   **本地优先架构**：完全依赖本地 Ollama LLM，无需依赖外部 API，降低延迟并保护隐私。
*   **软硬结合**：通过可配置的 VRAM 剖面，提升了在不同硬件环境下的兼容性和运行效率。
*   **生态互联**：通过 ComfyUI 节点打通了从“提示词工程”到“图像生成”的数据闭环。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 35 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
这是一个基于人工智能的产业链股票池工具，支持美股与A股的映射分析。它具备主动发现潜力标的、评估政策压力及一键部署等功能，旨在辅助投资研究。

2. **核心功能**
- 实现美股与A股产业链的双向映射分析。
- 利用AI技术主动挖掘和推荐潜在投资标的。
- 提供政策压力测试以评估宏观环境影响。
- 支持在Cloudflare Workers或Vercel上快速一键部署。
- 整合Arxiv等学术资源以增强研究深度。

3. **适用场景**
- 需要跨市场（中美）进行产业链关联分析的投资者。
- 希望借助AI自动化筛选股票并监控政策风险的量化研究员。
- 寻求快速搭建个性化股票监控工具的开发者或独立交易者。
- 对AI行业上下游相关上市公司进行系统性梳理的研究人员。

4. **技术亮点**
- 采用无服务器架构（Serverless），依托Cloudflare Workers和Vercel实现低成本、高可用的部署。
- 结合自然语言处理与金融数据，实现从学术论文到市场信号的自动化转化。
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
funNLP 是一个全面且实用的中文自然语言处理（NLP）资源库，汇集了敏感词检测、实体抽取、情感分析等基础工具及大量领域知识图谱。该项目整合了丰富的语料数据、预训练模型代码以及各类垂直领域的专用词典，旨在为开发者提供一站式的中英文 NLP 解决方案。它涵盖了从基础文本处理到高级语义理解的多维度需求，是构建智能客服、内容审核及知识问答系统的得力助手。

2. **核心功能**
*   **基础文本处理与抽取**：提供中英文敏感词过滤、姓名/手机号/邮箱/身份证等实体信息抽取、繁简体转换及中文分词加速工具。
*   **领域知识图谱与词典**：内置中日文人名、汽车品牌、古诗词、法律、医学、财经等多个垂直领域的专用词库及大规模知识图谱数据。
*   **预训练模型与深度学习应用**：包含 BERT、ALBERT、GPT-2 等主流模型的中文预训练版本及 NER、文本分类、摘要生成的实战代码模板。
*   **语音与多模态支持**：集成中文 OCR 识别、ASR 语音数据集、音素对齐工具及语音情感分析模块，支持文本到语音的多种交互场景。
*   **数据增强与评测基准**：提供 EDA 数据增强工具、NLP 竞赛 Top 方案复盘及中文语言理解测评基准（CLUE），助力模型优化与性能评估。

3. **适用场景**
*   **内容安全与审核系统**：利用敏感词库和暴恐词表，快速搭建互联网平台的内容自动过滤与风险预警机制。
*   **智能客服与对话机器人**：基于闲聊语料、知识图谱及 Rasa/ConvLab 等框架，开发具备上下文理解和多轮对话能力的智能助手。
*   **垂直行业知识挖掘**：在医疗、金融或法律领域，利用专用词典和实体抽取工具，从非结构化文档中提取关键信息并构建行业知识库。
*   **NLP 算法研究与教学**：作为学习资源和实验基地，研究人员可利用其提供的数据集、基准模型及论文复现代码进行算法对比与创新。

4. **技术亮点**
*   **资源极度丰富**：整合了数百个高质量的数据集、预训练模型、领域词典和开源工具，极大降低了 NLP 项目的启动门槛。
*   **覆盖全链路**：从数据预处理、模型训练、实体抽取到最终的应用部署（如聊天机器人、OCR），提供了端到端的解决方案参考。
*   **紧跟前沿技术**：及时收录了 BERT、RoBERTa、ALBERT 等最新预训练语言模型及其在中文任务上的微调实践，保持了技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例，助力技术学习与技能提升。

2. **核心功能**
- 提供500个完整的AI项目代码库，覆盖主流技术栈。
- 分类清晰，整合了机器学习、深度学习、计算机视觉及NLP四大方向。
- 作为“Awesome”列表， curated精选高质量开源项目供参考。
- 支持Python语言实现，便于直接运行和二次开发。

3. **适用场景**
- AI初学者通过阅读和运行代码快速掌握各子领域的基础应用。
- 开发者寻找灵感，将现有项目重构或扩展以解决特定业务问题。
- 教育机构用于教学演示，展示不同算法在实际场景中的落地效果。

4. **技术亮点**
- 规模庞大且内容全面，一站式解决多模态AI项目的学习需求。
- 标签体系完善，便于用户根据具体技术点（如CV、NLP）精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的强大工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构与数据流向。

2. **核心功能**
*   支持加载并解析包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等在内的多种模型格式。
*   提供交互式图形界面，清晰展示网络层级结构、张量形状及权重信息。
*   具备模型调试功能，允许用户查看特定节点的数据分布以排查问题。
*   支持将模型结构导出为图片、SVG 或文本格式，便于文档编写与分享。
*   基于 Web 技术构建，可在浏览器、桌面应用及代码编辑器插件中运行。

3. **适用场景**
*   **模型架构审查**：在部署前快速检查神经网络层顺序、连接方式及输入输出维度是否正确。
*   **调试与优化**：定位模型中的异常节点或冗余层，辅助进行模型剪枝或量化优化。
*   **学术交流与汇报**：生成高质量的网络结构图，用于论文撰写、技术博客或团队演示。
*   **跨框架迁移验证**：对比不同框架（如从 TensorFlow 转换为 PyTorch）转换后的模型一致性。

4. **技术亮点**
*   极高的兼容性，广泛支持从传统机器学习到最新的大模型格式（如 Safetensors）。
*   轻量级且开源，无需复杂配置即可在本地离线环境使用，保护数据隐私。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准，旨在打破不同深度学习框架之间的壁垒。它允许开发者在不同平台、硬件和工具之间无缝地转换和运行模型，从而简化了从训练到部署的全流程。

**2. 核心功能**
*   **跨框架互操作性**：支持在 PyTorch、TensorFlow、Keras 等主流框架间轻松转换模型格式。
*   **统一模型表示**：提供标准化的计算图定义，确保模型结构在不同环境中的一致性。
*   **广泛的后端支持**：兼容多种推理引擎和硬件加速器（如 ONNX Runtime），提升执行效率。
*   **生态系统集成**：与 Scikit-learn 等经典机器学习库集成，扩展了其适用范围。

**3. 适用场景**
*   **模型部署优化**：将训练好的模型转换为 ONNX 格式，以便在移动端或嵌入式设备上高效运行。
*   **混合框架开发**：在一个框架中训练模型，在另一个框架中进行验证或微调，利用各自优势。
*   **生产环境标准化**：在需要高性能和低延迟的工业级应用中，使用统一的模型格式简化维护和管理。

**4. 技术亮点**
*   **开源社区驱动**：由微软、Facebook 等科技巨头共同维护，拥有庞大的开发者社区和丰富的资源支持。
*   **高性能运行时**：配套的 ONNX Runtime 提供了优化的推理性能，支持 CPU、GPU 及专用加速硬件。
- 链接: https://github.com/onnx/onnx
- ⭐ 21215 | 🍴 3976 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- **1. 中文简介**
《机器学习工程公开书籍》是一本全面涵盖机器学习工程实践的知识库，旨在指导开发者构建可扩展、高效且稳健的AI系统。内容深入探讨了从底层硬件优化到大规模模型训练与推理的全链路技术细节。

**2. 核心功能**
*   提供大规模语言模型（LLM）的训练、微调及推理的最佳实践指南。
*   详解GPU集群管理、网络通信优化及存储策略以提升训练效率。
*   涵盖PyTorch框架下的分布式训练架构与Slurm作业调度系统配置。
*   包含针对机器学习系统的调试技巧、监控方法及性能剖析工具使用。

**3. 适用场景**
*   需要在数千张GPU上高效训练或微调大型Transformer模型的团队。
*   致力于优化深度学习基础设施、降低训练成本并提升系统可用性的MLOps工程师。
*   希望深入理解底层硬件（如GPU互联、存储IO）对模型性能影响的算法研究人员。

**4. 技术亮点**
*   **全栈覆盖**：从底层硬件驱动到上层应用部署，提供了端到端的工程解决方案。
*   **实战导向**：基于真实生产环境经验，解决大规模分布式训练中的具体痛点（如显存溢出、网络瓶颈）。
*   **社区共建**：作为开源“公开书籍”，持续整合最新的技术进展和专家贡献，保持内容的前沿性。
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
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例，助力技术学习与技能提升。

2. **核心功能**
- 提供500个完整的AI项目代码库，覆盖主流技术栈。
- 分类清晰，整合了机器学习、深度学习、计算机视觉及NLP四大方向。
- 作为“Awesome”列表， curated精选高质量开源项目供参考。
- 支持Python语言实现，便于直接运行和二次开发。

3. **适用场景**
- AI初学者通过阅读和运行代码快速掌握各子领域的基础应用。
- 开发者寻找灵感，将现有项目重构或扩展以解决特定业务问题。
- 教育机构用于教学演示，展示不同算法在实际场景中的落地效果。

4. **技术亮点**
- 规模庞大且内容全面，一站式解决多模态AI项目的学习需求。
- 标签体系完善，便于用户根据具体技术点（如CV、NLP）精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35727 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的强大工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构与数据流向。

2. **核心功能**
*   支持加载并解析包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等在内的多种模型格式。
*   提供交互式图形界面，清晰展示网络层级结构、张量形状及权重信息。
*   具备模型调试功能，允许用户查看特定节点的数据分布以排查问题。
*   支持将模型结构导出为图片、SVG 或文本格式，便于文档编写与分享。
*   基于 Web 技术构建，可在浏览器、桌面应用及代码编辑器插件中运行。

3. **适用场景**
*   **模型架构审查**：在部署前快速检查神经网络层顺序、连接方式及输入输出维度是否正确。
*   **调试与优化**：定位模型中的异常节点或冗余层，辅助进行模型剪枝或量化优化。
*   **学术交流与汇报**：生成高质量的网络结构图，用于论文撰写、技术博客或团队演示。
*   **跨框架迁移验证**：对比不同框架（如从 TensorFlow 转换为 PyTorch）转换后的模型一致性。

4. **技术亮点**
*   极高的兼容性，广泛支持从传统机器学习到最新的大模型格式（如 Safetensors）。
*   轻量级且开源，无需复杂配置即可在本地离线环境使用，保护数据隐私。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必备的知识速查表（Cheat Sheets）。内容涵盖了从基础概念到高级框架的实用参考指南，旨在帮助研究人员快速回顾关键知识点。

2. **核心功能**
- 提供深度学习与机器学习领域的核心概念速查。
- 包含常用Python科学计算库（如NumPy, SciPy, Matplotlib）的使用技巧。
- 集成主流深度学习框架（如Keras）的代码示例与API参考。
- 以简洁的图表或列表形式呈现复杂算法的关键参数与逻辑。

3. **适用场景**
- 研究人员在实验前快速回顾特定算法或库函数的用法。
- 面试准备中用于梳理人工智能领域的核心知识点。
- 日常编程工作中作为参考手册，解决具体的代码实现问题。

4. **技术亮点**
- 内容高度浓缩，将复杂的理论和代码简化为易于查阅的形式。
- 覆盖范围广，结合了理论研究与实际工程工具（如可视化库）。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户入门并掌握就业所需的实战技能。内容涵盖Python、数学基础以及机器学习、深度学习、计算机视觉和自然语言处理等热门领域。

2. **核心功能**
- 提供结构化的AI学习路径，覆盖从基础到进阶的关键技术栈。
- 整合近200个实战案例，强化动手能力和项目经验积累。
- 免费开放配套教材与资源，降低人工智能领域的学习门槛。
- 支持多种主流框架（如PyTorch、TensorFlow）及工具库（如Pandas、NumPy）的学习与应用。

3. **适用场景**
- 希望从零开始系统学习人工智能的初学者或转行者。
- 需要大量实战项目来丰富简历、提升就业竞争力的求职者。
- 寻求结构化学习资料以补充学校或自学中知识盲点的学生。

4. **技术亮点**
- 极高的社区认可度（13,000+星标），证明其内容的实用性与广泛影响力。
- 知识点覆盖面极广，不仅包含算法理论，还深入多种主流深度学习框架及数据处理工具。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化工作流，降低了深度学习应用的开发门槛。

2. **核心功能**
- 支持多种数据类型的原生处理，包括文本、图像、音频及表格数据。
- 提供声明式 YAML 配置文件，无需编写复杂代码即可定义模型架构。
- 内置自动超参数调优与实验管理功能，优化模型训练效果。
- 兼容 PyTorch 后端，支持从原型设计到生产部署的全生命周期管理。
- 集成主流开源模型（如 Llama、Mistral），便于快速微调与推理。

3. **适用场景**
- 快速构建和微调基于 Transformer 的大语言模型（如 Llama 系列）。
- 多模态机器学习应用开发，同时处理结构化与非结构化数据。
- 数据科学家进行可复现的深度学习实验管理与模型对比。
- 希望减少样板代码、加速 AI 模型原型验证的低代码开发需求。

4. **技术亮点**
- 采用“数据为中心”的设计哲学，强调数据预处理与特征工程的自动化。
- 模块化架构允许轻松插入自定义层或损失函数，保持灵活性。
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
funNLP 是一个全面且实用的中文自然语言处理（NLP）资源库，汇集了敏感词检测、实体抽取、情感分析等基础工具及大量领域知识图谱。该项目整合了丰富的语料数据、预训练模型代码以及各类垂直领域的专用词典，旨在为开发者提供一站式的中英文 NLP 解决方案。它涵盖了从基础文本处理到高级语义理解的多维度需求，是构建智能客服、内容审核及知识问答系统的得力助手。

2. **核心功能**
*   **基础文本处理与抽取**：提供中英文敏感词过滤、姓名/手机号/邮箱/身份证等实体信息抽取、繁简体转换及中文分词加速工具。
*   **领域知识图谱与词典**：内置中日文人名、汽车品牌、古诗词、法律、医学、财经等多个垂直领域的专用词库及大规模知识图谱数据。
*   **预训练模型与深度学习应用**：包含 BERT、ALBERT、GPT-2 等主流模型的中文预训练版本及 NER、文本分类、摘要生成的实战代码模板。
*   **语音与多模态支持**：集成中文 OCR 识别、ASR 语音数据集、音素对齐工具及语音情感分析模块，支持文本到语音的多种交互场景。
*   **数据增强与评测基准**：提供 EDA 数据增强工具、NLP 竞赛 Top 方案复盘及中文语言理解测评基准（CLUE），助力模型优化与性能评估。

3. **适用场景**
*   **内容安全与审核系统**：利用敏感词库和暴恐词表，快速搭建互联网平台的内容自动过滤与风险预警机制。
*   **智能客服与对话机器人**：基于闲聊语料、知识图谱及 Rasa/ConvLab 等框架，开发具备上下文理解和多轮对话能力的智能助手。
*   **垂直行业知识挖掘**：在医疗、金融或法律领域，利用专用词典和实体抽取工具，从非结构化文档中提取关键信息并构建行业知识库。
*   **NLP 算法研究与教学**：作为学习资源和实验基地，研究人员可利用其提供的数据集、基准模型及论文复现代码进行算法对比与创新。

4. **技术亮点**
*   **资源极度丰富**：整合了数百个高质量的数据集、预训练模型、领域词典和开源工具，极大降低了 NLP 项目的启动门槛。
*   **覆盖全链路**：从数据预处理、模型训练、实体抽取到最终的应用部署（如聊天机器人、OCR），提供了端到端的解决方案参考。
*   **紧跟前沿技术**：及时收录了 BERT、RoBERTa、ALBERT 等最新预训练语言模型及其在中文任务上的微调实践，保持了技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82065 | 🍴 15256 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目旨在简化模型微调流程，使其成为 NLP 研究和应用开发的高效工具。

**2. 核心功能**
*   **统一微调支持**：兼容超过 100 种主流大模型及多模态模型的统一微调接口。
*   **高效训练算法**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调（PEFT）方法以节省资源。
*   **对齐优化能力**：支持 RLHF（基于人类反馈的强化学习）、DPO 等指令微调与对齐技术。
*   **量化部署友好**：提供 INT4/INT8 等量化训练选项，降低显存占用并加速推理。
*   **模块化架构设计**：基于 Transformers 库构建，易于扩展新的模型架构和训练策略。

**3. 适用场景**
*   **垂直领域模型定制**：针对医疗、法律或客服等特定行业数据，快速微调开源基座模型。
*   **多模态应用开发**：训练具备图像理解能力的视觉语言模型（VLM），用于图文生成或分析任务。
*   **资源受限环境部署**：在显存有限的消费级显卡上，通过 QLoRA 等技术实现大模型的高效微调。
*   **前沿对齐技术研究**：探索 RLHF、DPO 等高级对齐算法，提升模型的指令遵循能力和安全性。

**4. 技术亮点**
*   **ACL 2024 收录**：相关研究成果已被自然语言处理顶级会议 ACL 2024 接收，具备学术认可度。
*   **全栈兼容生态**：无缝集成 LLaMA、Qwen、Gemma、DeepSeek 等最新开源模型，保持技术领先性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73526 | 🍴 8988 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- **1. 中文简介**
该项目是一套为期12周、包含24课时的AI通识课程，旨在让所有人都能轻松学习人工智能。内容涵盖从基础概念到深度学习等核心领域，通过Jupyter Notebook提供实践指导。它由Microsoft For Beginners系列支持，适合零基础的初学者入门。

**2. 核心功能**
*   提供结构化的12周学习路径，分为24个独立课时。
*   使用Jupyter Notebook进行交互式代码教学与实验。
*   覆盖机器学习、深度学习、计算机视觉及自然语言处理等关键领域。
*   内置CNN、RNN、GAN等主流AI模型的实战案例。
*   面向大众设计，降低AI学习门槛，强调零基础友好。

**3. 适用场景**
*   **初学者入门**：希望系统了解AI基本概念但无深厚数学或编程背景的学习者。
*   **高校/企业培训**：作为计算机科学或数据科学相关课程的辅助教材或工作坊素材。
*   **自学者实践**：需要结构化课程和可运行代码示例来巩固AI理论的个人开发者。
*   **教育者备课**：寻找现成、开源且经过验证的AI教学大纲的教师或导师。

**4. 技术亮点**
*   **模块化课程设计**：将复杂的AI知识拆解为易于消化的24个小单元。
*   **全栈覆盖**：同时涵盖传统机器学习（ML）与现代深度学习（DL）技术。
*   **微软背书**：依托“Microsoft For Beginners”品牌，保证内容的准确性与教育价值。
*   **即时反馈**：基于Notebook的环境允许学习者边读代码边运行，直观理解算法效果。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52900 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建AI工程，帮助开发者深入理解并掌握人工智能技术。它不仅提供学习路径，更强调实际动手构建模型与系统，最终能够将其部署并交付给他人使用。

2. **核心功能**
*   涵盖从深度学习、大语言模型到计算机视觉等全方位的AI工程技术栈。
*   提供基于Python和Rust等语言的从零实现教程，强化底层原理理解。
*   整合智能体（Agents）、MCP协议及群体智能等前沿AI应用开发内容。
*   包含完整的课程结构与实战项目，指导开发者完成从学习到交付的全流程。

3. **适用场景**
*   AI初学者希望深入理解机器学习、NLP和生成式AI底层原理而非仅调用API。
*   工程师需要构建基于自定义模型或智能体的复杂AI应用程序。
*   团队希望采用多语言（如Python与Rust结合）优化高性能AI系统的开发。

4. **技术亮点**
*   跨语言支持：结合Python的易用性与Rust的高性能，适应不同场景需求。
*   前沿技术集成：涵盖MCP（Model Context Protocol）、Swarm Intelligence及Transformers架构等最新趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43723 | 🍴 7353 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战以及线性代数基础的综合性学习项目，深入结合 PyTorch、NLTK 和 TensorFlow 2 等主流框架。该项目旨在通过代码实践帮助学习者掌握从基础理论到高级算法的完整知识体系。它适合希望系统提升 AI 工程能力与算法理解的开发者。

2. **核心功能**
- 提供完整的机器学习算法实战代码，包括分类、回归、聚类及推荐系统等。
- 集成深度学习框架（PyTorch 和 TF2）进行 DNN、RNN、LSTM 等模型实现。
- 涵盖自然语言处理（NLP）关键技术，如使用 NLTK 进行文本分析和序列建模。
- 包含经典数据挖掘算法实现，如 Apriori、FP-Growth、K-Means 和 SVM 等。
- 融合数学基础（线性代数）与统计学习理论（PCA、SVD），夯实算法底层逻辑。

3. **适用场景**
- 机器学习初学者系统学习经典算法原理与 Python 实现。
- 数据科学家构建推荐系统或进行大规模数据分析时的参考案例库。
- 深度学习工程师研究 NLP 任务（如文本分类、序列预测）的代码模板。
- 高校学生或研究人员辅助理解线性代数在 AI 算法中的具体应用。

4. **技术亮点**
- 兼顾理论与实践：不仅提供算法代码，还强调背后的数学推导（如线性代数）。
- 多框架支持：同时覆盖传统机器学习库（scikit-learn）与现代深度学习框架（PyTorch/TF2）。
- 领域全面：横跨监督学习、无监督学习、强化学习基础及自然语言处理三大方向。
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
- ⭐ 22598 | 🍴 2119 | 语言: Python
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
- ⭐ 384222 | 🍴 80721 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261533 | 🍴 23346 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220874 | 🍴 42107 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198106 | 🍴 59648 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185699 | 🍴 46067 | 语言: Python
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
- ⭐ 156398 | 🍴 8889 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152440 | 🍴 9661 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

