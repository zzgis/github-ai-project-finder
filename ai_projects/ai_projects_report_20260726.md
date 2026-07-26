# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### deer-workflow
- **1. 中文简介**
deer-workflow 是一个开源的动态工作流运行时环境，旨在让编排逻辑完全保留在 TypeScript 中。它通过可替换的 Agent 运行时来委托具体的语义处理任务，实现了逻辑与执行的解耦。

**2. 核心功能**
*   **TypeScript 原生编排**：工作流的定义和调度逻辑直接使用 TypeScript 编写，便于开发者维护和类型检查。
*   **动态工作流支持**：提供动态的工作流运行时，能够灵活应对变化复杂的业务流程。
*   **可插拔 Agent 运行时**：将语义处理任务委托给可替换的 Agent 模块，支持不同 AI 模型或代理后端的切换。
*   **轻量级运行时**：基于 Bun 构建，利用其高性能优势提供高效的执行环境。

**3. 适用场景**
*   **AI 应用后端开发**：需要构建复杂 LLM 调用链、多步推理或工具调用的 AI 应用后端。
*   **动态业务流程自动化**：业务规则经常变动，需要快速调整工作流逻辑的企业级自动化场景。
*   **多模型代理集成平台**：需要在一个系统中灵活切换不同大语言模型或 Agent 框架的中间件层。

**4. 技术亮点**
*   **解耦设计**：将“流程控制”与“语义执行”分离，提高了系统的灵活性和可测试性。
*   **现代技术栈**：结合 TypeScript 的类型安全和 Bun 的高性能运行时，兼顾开发体验与运行效率。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 58 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- 1. **中文简介**
该项目是一个 MCP 服务器，允许 AI 智能体通过 Open Cluster Management 中心操作多集群 Kubernetes 舰队。它在模型与你的集群之间提供了策略控制、审批流程以及审计功能，确保操作的合规性与安全性。

2. **核心功能**
- 支持 AI 智能体通过 MCP 协议远程管理多个 Kubernetes 集群。
- 集成 Open Cluster Management (OCM) 以实现集中式的集群治理。
- 提供策略引擎，用于在 AI 操作前定义和执行安全约束。
- 内置审批机制，关键操作需经人工或自动化规则确认后方可执行。
- 记录完整的操作审计日志，确保所有 AI 行为可追溯。

3. **适用场景**
- 企业级多云 Kubernetes 环境的 AI 自动化运维。
- 需要严格合规性审查的金融或政府机构集群管理。
- 利用 LLM 辅助进行大规模集群策略部署与故障排查。
- 构建具备安全护栏（Safety Guardrails）的智能运维助手。

4. **技术亮点**
- 巧妙结合 MCP 标准与 OCM 治理能力，为 AI 操作提供标准化的接口与安全边界。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 32 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用程序，利用本地 Ollama 大语言模型对原始文本和图像进行分析。它能将视觉描述提取并结构化为优化的 JSON 提示词，以便用于生成式 AI 任务。该应用内置 SQLite 数据库以支持提示词编辑，并提供可调整的显存配置文件及 ComfyUI 节点集成。

2. **核心功能**
*   利用本地 Ollama LLMs 分析文本与图像内容。
*   将非结构化视觉信息转化为标准化的 JSON 格式提示词。
*   内置 SQLite 数据库，支持用户高效编辑和管理提示词数据。
*   提供可配置的 VRAM 硬件配置文件，适配不同显卡性能。
*   集成 ComfyUI 节点，实现与工作流的无缝数据交互。

3. **适用场景**
*   AI 艺术创作中需要批量将参考图转换为标准 JSON 提示词的场景。
*   开发者希望在不依赖云端 API 的情况下，通过本地模型优化生成式 AI 输入数据的流程。
*   使用 ComfyUI 进行复杂工作流搭建，且需要将外部数据库数据直接注入节点的技术团队。

4. **技术亮点**
*   实现了从视觉描述到结构化 JSON 提示词的自动化转换，提升了提示工程的效率。
*   通过本地 Ollama 模型和自定义 VRAM 配置，确保了数据隐私并优化了资源消耗。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 29 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
这是一个基于人工智能的产业链股票池项目，支持美股与A股的映射对照。它具备活跃发现、政策压力分析等功能，并支持一键部署。

2. **核心功能**
- 提供AI产业链相关的股票池数据。
- 实现美股与A股之间的行业映射对照。
- 具备市场活跃度发现及政策压力分析能力。
- 支持通过Cloudflare Workers或Vercel进行一键快速部署。

3. **适用场景**
- AI产业链投资研究与标的筛选。
- 跨市场（中美股市）行业对比分析。
- 利用边缘计算或Serverless架构快速搭建量化研究工具。

4. **技术亮点**
- 采用JavaScript开发，兼容主流无服务器平台（如Cloudflare Workers和Vercel）。
- 集成Arxiv资源，可能用于抓取最新学术研究成果以辅助投资决策。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 26 | 🍴 15 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### Verity-JE-Mod-Minecraft
- 1. **中文简介**
这是一个专为 Minecraft Java 版 1.21+ 设计的模组，引入了新怪物、自定义维度、生物群系及世界生成机制（不支持基岩版）。该怪物拥有配音、背景故事以及多阶段 AI，可在 Modrinth 平台通过 Forge 或 Fabric 加载器免费下载。

2. **核心功能**
*   新增具有配音和丰富背景故事的独特怪物。
*   包含多阶段人工智能行为系统。
*   提供自定义维度、生物群系及世界生成内容。
*   兼容 Forge 和 Fabric 两种主流加载器。

3. **适用场景**
*   寻求全新冒险体验和战斗挑战的单人玩家。
*   希望丰富游戏内容并增加世界复杂度的多人服务器管理员。
*   喜欢探索自定义维度和独特生物群系的模组爱好者。
*   构建“全模组整合包”或“空岛生存”玩法的模组包开发者。

4. **技术亮点**
*   实现了具备多阶段逻辑的高级实体 AI 系统。
*   集成了音频资源以支持怪物的语音演出功能。
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
- ⭐ 19 | 🍴 4 | 语言: TypeScript

### llmwiki-harness
- 描述: 无描述
- 链接: https://github.com/cookyman74/llmwiki-harness
- ⭐ 13 | 🍴 3 | 语言: Python
- 标签: ai, claude-code, knowledge-management, llm, markdown

### tcm-ai-tutor
- 描述: 无描述
- 链接: https://github.com/William84132/tcm-ai-tutor
- ⭐ 12 | 🍴 0 | 语言: HTML

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面的中英文自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、繁简转换）到高级任务（如知识图谱构建、情感分析、语音识别）的广泛资源。该项目整合了海量的专业领域词典、预训练模型、数据集及算法实现，旨在为开发者提供一站式的 NLP 开发支持。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表以及中文拼写检查和纠错模块。
*   **实体识别与信息抽取**：包含针对手机号、身份证、邮箱的抽取工具，基于 BERT/ALBERT 等模型的命名实体识别（NER），以及医疗、金融等领域的特定实体提取。
*   **语义分析与情感挖掘**：集成词汇情感值计算、同义词/反义词库、关键词抽取、文本摘要生成及各类情感分析模型。
*   **知识图谱与问答系统**：收录了大量百科、成语、古诗词及垂直领域（如汽车、医学、法律）的知识图谱数据，并提供构建 QA 系统和关系抽取的代码示例。
*   **语音处理与多模态资源**：包含中文语音识别（ASR）语料、发音词典、语音对齐工具及音频增强相关资源。

**3. 适用场景**
*   **NLP 初学者学习与研究**：适合需要快速了解中文 NLP 生态、获取高质量标注数据集（如 CLUE 基准、各种NER数据集）进行学术研究或课程项目的学生。
*   **企业级内容风控系统开发**：适用于需要搭建敏感词过滤、谣言检测、暴恐词排查等自动化审核系统的互联网平台或媒体机构。
*   **垂直领域智能客服与问答机器人**：适合开发基于医疗、金融、法律或汽车行业的智能问答系统，利用其提供的领域词典和预训练模型降低冷启动成本。
*   **复杂文本信息结构化**：用于需要从非结构化文本（如新闻、简历、法律文书）中高效抽取关键实体、关系或生成摘要的企业级数据处理管道。

**4. 技术亮点**
*   **资源极度丰富且分类清晰**：不仅包含代码，还整合了清华 XLORE、百度、京东等多方开源的高质量数据集、预训练模型（BERT, RoBERTa, ALBERT 等）及权威词典，极大降低了数据搜集门槛。
*   **覆盖全栈 NLP 任务链**：从底层的分词、OCR、ASR，到中层的实体抽取、句法分析，再到高层的情感分析、对话生成及知识图谱构建，提供了完整的工具链参考。
*   **紧跟前沿技术实践**：包含了最新的 Transformer 架构应用、对抗样本生成、注意力可视化以及多种主流深度学习框架（TensorFlow, PyTorch, Keras）下的 SOTA 模型复现。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82059 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例和源代码，是学习人工智能技术的优质资源。它通过分类整理，帮助用户快速找到并复现各类前沿AI应用。

2. **核心功能**
- 提供500个完整的AI项目代码示例，覆盖主流算法与应用。
- 细分领域包括机器学习、深度学习、计算机视觉及NLP技术栈。
- 包含“Awesome”标签精选内容，确保项目质量与实用性。
- 支持Python为主要编程语言，便于直接运行和修改。

3. **适用场景**
- 初学者系统学习AI概念，通过阅读代码理解理论实现。
- 研究人员或工程师寻找特定任务（如图像识别、文本分析）的参考实现。
- 技术面试准备，通过复现经典项目展示编程与算法能力。
- 企业技术选型评估，快速了解不同AI解决方案的技术可行性。

4. **技术亮点**
- 规模庞大且分类清晰，一站式解决多领域AI学习需求。
- 高星标数（35721+）验证了其在社区中的广泛认可度和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35721 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款功能强大的神经网络、深度学习及机器学习模型可视化工具。它支持多种主流框架生成的模型文件，能够将复杂的模型结构以直观的图表形式呈现出来。该工具旨在帮助开发者和研究人员快速理解和分析模型架构。

2. **核心功能**
*   广泛支持多种模型格式，包括 CoreML、Keras、ONNX、PyTorch、TensorFlow、TensorFlow Lite 和 Safetensors 等。
*   提供清晰直观的模型架构图示，便于查看层结构、张量形状及数据流向。
*   支持离线浏览功能，用户无需联网即可在本地查看和分析模型文件。
*   兼容 Web 浏览器和本地桌面应用，提供便捷的使用体验。

3. **适用场景**
*   深度学习工程师用于调试和优化神经网络模型的层结构与参数配置。
*   研究人员在论文撰写或技术分享时，制作高质量的网络结构示意图。
*   开发者在不同模型框架（如从 PyTorch 到 ONNX）之间迁移或转换模型时，验证模型的一致性。

4. **技术亮点**
*   基于 JavaScript 构建，拥有极高的跨平台兼容性和轻量级特性。
*   拥有庞大的社区支持和高活跃度（GitHub 星标数超 3 万），确保了工具的持续更新与维护。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33264 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是机器学习领域的开放标准，旨在促进不同深度学习框架之间的互操作性。它允许开发者在不同平台、设备和框架之间无缝迁移和部署模型，打破了技术壁垒。

**2. 核心功能**
- 提供统一的中间表示格式，支持跨框架的模型交换与共享。
- 实现从主流训练框架（如PyTorch、TensorFlow）到推理引擎的高效转换。
- 支持在多种硬件加速器（CPU、GPU、NPU等）上进行高性能推理部署。
- 维护开放的规范定义，确保不同供应商实现的兼容性与一致性。

**3. 适用场景**
- 将基于PyTorch或Keras训练的模型转换为通用格式，以便在生产环境中使用其他推理引擎运行。
- 在移动端或嵌入式设备上部署深度学习模型，利用ONNX Runtime优化性能。
- 在不同深度学习框架团队之间协作时，作为标准化的模型交付格式。

**4. 技术亮点**
- **生态兼容性极强**：原生支持PyTorch、TensorFlow、scikit-learn等几乎所有主流AI框架。
- **高性能推理引擎**：配套的ONNX Runtime提供了跨平台、低延迟的高性能执行环境。
- **开放标准驱动**：由微软、Facebook等巨头联合发起并维护，拥有活跃的社区支持和广泛的企业采纳。
- 链接: https://github.com/onnx/onnx
- ⭐ 21214 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一部全面涵盖机器学习工程实践的指南，深入探讨了从基础调试到大规模分布式训练及推理优化的核心技术。该项目旨在为工程师提供关于如何高效构建、训练和部署机器学习系统的最佳实践与详细解决方案。

2. **核心功能**
- 提供大规模分布式训练（如使用Slurm集群）的完整配置与优化指南。
- 详解GPU硬件特性、网络通信及存储系统对ML性能的影响与调优方法。
- 包含针对大型语言模型（LLM）的训练稳定性、调试技巧及故障排除方案。
- 覆盖模型推理优化、内存管理以及Transformer架构的高效实现细节。

3. **适用场景**
- 需要在超算集群或HPC环境中进行大规模深度学习模型分布式训练的工程师。
- 致力于优化大语言模型（LLM）训练成本、提升吞吐量并解决OOM等内存问题的研究人员。
- 希望深入了解底层硬件（GPU/网络）限制以进行系统级性能调优的MLOps专家。

4. **技术亮点**
- 内容极具实战深度，不仅涉及高层框架使用，更深入到底层硬件交互与系统级调优。
- 紧跟前沿技术，特别针对LLM时代的训练稳定性、量化及高效推理提供了权威参考。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18468 | 🍴 1181 | 语言: Python
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
- ⭐ 10677 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例和源代码，是学习人工智能技术的优质资源。它通过分类整理，帮助用户快速找到并复现各类前沿AI应用。

2. **核心功能**
- 提供500个完整的AI项目代码示例，覆盖主流算法与应用。
- 细分领域包括机器学习、深度学习、计算机视觉及NLP技术栈。
- 包含“Awesome”标签精选内容，确保项目质量与实用性。
- 支持Python为主要编程语言，便于直接运行和修改。

3. **适用场景**
- 初学者系统学习AI概念，通过阅读代码理解理论实现。
- 研究人员或工程师寻找特定任务（如图像识别、文本分析）的参考实现。
- 技术面试准备，通过复现经典项目展示编程与算法能力。
- 企业技术选型评估，快速了解不同AI解决方案的技术可行性。

4. **技术亮点**
- 规模庞大且分类清晰，一站式解决多领域AI学习需求。
- 高星标数（35721+）验证了其在社区中的广泛认可度和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35721 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款功能强大的神经网络、深度学习及机器学习模型可视化工具。它支持多种主流框架生成的模型文件，能够将复杂的模型结构以直观的图表形式呈现出来。该工具旨在帮助开发者和研究人员快速理解和分析模型架构。

2. **核心功能**
*   广泛支持多种模型格式，包括 CoreML、Keras、ONNX、PyTorch、TensorFlow、TensorFlow Lite 和 Safetensors 等。
*   提供清晰直观的模型架构图示，便于查看层结构、张量形状及数据流向。
*   支持离线浏览功能，用户无需联网即可在本地查看和分析模型文件。
*   兼容 Web 浏览器和本地桌面应用，提供便捷的使用体验。

3. **适用场景**
*   深度学习工程师用于调试和优化神经网络模型的层结构与参数配置。
*   研究人员在论文撰写或技术分享时，制作高质量的网络结构示意图。
*   开发者在不同模型框架（如从 PyTorch 到 ONNX）之间迁移或转换模型时，验证模型的一致性。

4. **技术亮点**
*   基于 JavaScript 构建，拥有极高的跨平台兼容性和轻量级特性。
*   拥有庞大的社区支持和高活跃度（GitHub 星标数超 3 万），确保了工具的持续更新与维护。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33264 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究者提供了 Essential Cheat Sheets（核心速查表）。它汇集了 AI 领域关键概念、算法及工具库的快速参考指南，旨在帮助研究人员高效回顾基础知识。内容源自 Medium 博主 Kailash Ahirwar 整理的精选资源。

2. **核心功能**
- 提供深度学习与机器学习核心概念的简明速查表。
- 涵盖 Keras、NumPy、SciPy 等常用库的代码示例与用法。
- 整合 Matplotlib 等可视化工具的关键操作技巧。
- 以结构化文档形式呈现复杂算法的逻辑框架。
- 支持离线查阅，便于快速检索技术细节。

3. **适用场景**
- 机器学习研究者在构建模型前快速回顾基础公式与定义。
- 数据科学家在使用 NumPy 或 SciPy 进行数值计算时查找函数用法。
- 深度学习工程师调试 Keras 模型时参考层配置与优化器参数。
- 初学者系统梳理 AI 知识体系，建立概念映射关系。

4. **技术亮点**
- 高度聚焦于实践中的高频知识点，避免冗长理论。
- 集成多种主流 AI 库的最佳实践与常见陷阱提示。
- 格式简洁直观，适合打印或作为桌面参考卡片使用。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，汇集了近200个实战案例与项目，并提供免费的配套教材以助力零基础用户入门及就业。内容涵盖Python、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等热门技术领域。该项目旨在通过系统化的路径引导学习者掌握从数据分析到高级算法的全栈AI技能。

2. **核心功能**
- 提供结构清晰的人工智能学习路径，涵盖从基础到进阶的完整知识体系。
- 整合近200个实战案例和项目代码，强调动手实践与就业导向。
- 免费提供配套的学习教材和资源，降低零基础用户的入门门槛。
- 覆盖主流AI框架（如PyTorch, TensorFlow, Keras）及工具库（如Pandas, NumPy）。
- 包含数学基础、数据处理、计算机视觉（CV）和自然语言处理（NLP）等多领域内容。

3. **适用场景**
- 希望从零开始系统学习人工智能技术的初学者或转行人员。
- 需要大量实战项目参考以提升编程能力和构建作品集的学生。
- 寻求特定AI领域（如NLP或CV）技术更新和最佳实践参考的开发人员。
- 希望梳理知识体系、查漏补缺的机器学习从业者。

4. **技术亮点**
- 高度集成的资源库：将分散的知识点、代码案例和学习资料统一整合。
- 广泛的生态支持：兼容TensorFlow 2.x、PyTorch、Caffe等多种主流深度学习框架。
- 就业导向明确：精选的实战案例直接对标行业需求，提升求职竞争力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化机器学习流程，降低了开发复杂人工智能应用的门槛。

2. **核心功能**
*   提供声明式配置接口，无需编写大量代码即可定义模型架构。
*   支持多种深度学习后端（如 PyTorch），便于快速训练和微调模型。
*   涵盖从数据处理、模型训练到评估的端到端机器学习工作流。
*   内置对表格数据、自然语言处理及计算机视觉任务的原生支持。
*   简化了大语言模型（LLM）的微调与部署流程，兼容主流开源模型。

3. **适用场景**
*   希望快速原型化并验证机器学习想法的数据科学家。
*   需要为结构化或非结构化数据构建定制化预测模型的企业开发者。
*   致力于在自有数据集上微调 Llama、Mistral 等大语言模型的研究人员。
*   缺乏深厚深度学习工程背景，但仍需部署高性能 AI 模型的应用团队。

4. **技术亮点**
*   采用“数据-centric”设计理念，强调数据配置而非复杂的模型代码编写。
*   高度模块化且可扩展，能够轻松集成新的组件或自定义逻辑。
*   简化了复杂的深度学习实验管理，使模型迭代更加高效透明。
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
funNLP 是一个全面的中英文自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、繁简转换）到高级任务（如知识图谱构建、情感分析、语音识别）的广泛资源。该项目整合了海量的专业领域词典、预训练模型、数据集及算法实现，旨在为开发者提供一站式的 NLP 开发支持。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表以及中文拼写检查和纠错模块。
*   **实体识别与信息抽取**：包含针对手机号、身份证、邮箱的抽取工具，基于 BERT/ALBERT 等模型的命名实体识别（NER），以及医疗、金融等领域的特定实体提取。
*   **语义分析与情感挖掘**：集成词汇情感值计算、同义词/反义词库、关键词抽取、文本摘要生成及各类情感分析模型。
*   **知识图谱与问答系统**：收录了大量百科、成语、古诗词及垂直领域（如汽车、医学、法律）的知识图谱数据，并提供构建 QA 系统和关系抽取的代码示例。
*   **语音处理与多模态资源**：包含中文语音识别（ASR）语料、发音词典、语音对齐工具及音频增强相关资源。

**3. 适用场景**
*   **NLP 初学者学习与研究**：适合需要快速了解中文 NLP 生态、获取高质量标注数据集（如 CLUE 基准、各种NER数据集）进行学术研究或课程项目的学生。
*   **企业级内容风控系统开发**：适用于需要搭建敏感词过滤、谣言检测、暴恐词排查等自动化审核系统的互联网平台或媒体机构。
*   **垂直领域智能客服与问答机器人**：适合开发基于医疗、金融、法律或汽车行业的智能问答系统，利用其提供的领域词典和预训练模型降低冷启动成本。
*   **复杂文本信息结构化**：用于需要从非结构化文本（如新闻、简历、法律文书）中高效抽取关键实体、关系或生成摘要的企业级数据处理管道。

**4. 技术亮点**
*   **资源极度丰富且分类清晰**：不仅包含代码，还整合了清华 XLORE、百度、京东等多方开源的高质量数据集、预训练模型（BERT, RoBERTa, ALBERT 等）及权威词典，极大降低了数据搜集门槛。
*   **覆盖全栈 NLP 任务链**：从底层的分词、OCR、ASR，到中层的实体抽取、句法分析，再到高层的情感分析、对话生成及知识图谱构建，提供了完整的工具链参考。
*   **紧跟前沿技术实践**：包含了最新的 Transformer 架构应用、对抗样本生成、注意力可视化以及多种主流深度学习框架（TensorFlow, PyTorch, Keras）下的 SOTA 模型复现。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82059 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种模型。该项目在 ACL 2024 会议上发表，旨在简化大模型的训练与部署流程。它通过整合多种先进技术，为开发者提供了一站式的模型优化解决方案。

2. **核心功能**
*   支持100+种主流大模型及视觉语言模型的统一高效微调。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）技术。
*   提供 RLHF（基于人类反馈的强化学习）、DPO 等对齐训练方法。
*   支持全量微调、量化微调（如 4bit/8bit）及混合专家模型（MoE）训练。
*   内置丰富的数据处理、指令微调及推理加速工具链。

3. **适用场景**
*   企业或个人开发者需要对特定领域的大模型进行低成本、高效率的微调定制。
*   研究人员希望快速复现或验证不同微调算法（如 LoRA vs QLoRA）在多个模型上的效果。
*   需要在资源受限环境下（如单张 GPU）运行大型模型微调任务的用户。
*   需要同时处理文本生成与多模态（图像+文本）理解任务的复杂应用场景。

4. **技术亮点**
*   **高度统一性**：无需为不同模型编写独立代码，一套框架适配百余个模型架构。
*   **极致效率**：结合 QLoRA 和量化技术，显著降低显存占用，使消费级显卡也能微调大模型。
*   **前沿算法集成**：原生支持最新对齐技术（如 DPO、KTO）及多模态训练能力。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73522 | 🍴 8985 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
该项目是一套为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。课程采用Jupyter Notebook编写，提供了从基础理论到实践应用的系统化学习路径。

2. **核心功能**
*   提供结构化的12周学习计划，涵盖机器学习、深度学习及自然语言处理等核心领域。
*   内置基于Jupyter Notebook的交互式代码示例，方便学习者边学边练。
*   覆盖计算机视觉（CNN）、生成对抗网络（GAN）及循环神经网络（RNN）等前沿技术主题。
*   由微软发起并维护，确保内容符合行业标准且易于访问。

3. **适用场景**
*   初学者希望系统性地从零开始学习人工智能理论与实践。
*   教育工作者寻找结构化、开源的课程资源用于课堂教学或辅导。
*   开发人员希望在特定领域（如NLP或计算机视觉）快速补充AI基础知识。

4. **技术亮点**
*   采用微软“为初学者”系列的教学方法论，强调低门槛和高参与度。
*   课程内容紧跟AI领域最新发展趋势，包括GAN和Transformer相关概念。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52888 | 🍴 10743 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
该项目是一个从零开始构建AI工程的综合性课程与资源库，旨在通过“学习、构建、部署”的完整流程，帮助用户掌握AI技术的核心原理与实践。它不仅涵盖基础理论，更强调实际动手能力和将AI应用交付给最终用户的工程化技能。

2. **核心功能**
*   提供从基础算法到高级架构的从零构建教程，深入解析LLM、计算机视觉及强化学习等核心技术。
*   整合了Agents（智能体）、Swarm Intelligence（群体智能）及MCP（模型上下文协议）等前沿AI代理技术的学习路径。
*   包含完整的工程化指南，教授如何将生成的AI内容或模型打包并部署给他人使用。
*   涵盖多种主流编程语言（Python, Rust, TypeScript），支持多模态开发（NLP, Computer Vision, Generative AI）。

3. **适用场景**
*   希望深入理解大语言模型（LLM）和生成式AI底层原理，而非仅调用API的开发者。
*   需要构建自主智能体（AI Agents）或多智能体系统（Swarm）的研究人员与工程师。
*   致力于将AI原型转化为可交付产品的全栈工程师，寻求端到端的工程化最佳实践。

4. **技术亮点**
*   **全栈覆盖**：同时涉及Python（主流AI开发）、Rust（高性能底层）和TypeScript（前端/Web集成），提供跨语言的技术视野。
*   **前沿聚焦**：特别强调AI Agents、MCP协议和群体智能等当前最热门的工程化方向，紧跟技术趋势。
*   **实战导向**：不同于纯理论课程，它强调“Ship it for others”，即注重产品的最终交付与用户体验。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43631 | 🍴 7324 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个集数据分析与机器学习实战于一体的综合性项目，涵盖了线性代数基础、PyTorch 深度学习框架以及 NLTK 和 TensorFlow 2 的自然语言处理工具。该项目旨在通过代码实现帮助开发者深入理解并掌握从传统算法到深度学习的核心技术栈。

2. **核心功能**
*   提供机器学习经典算法（如 SVM、KMeans、Adaboost）的 Python 实现与解析。
*   集成 PyTorch 和 TensorFlow 2 进行深度学习模型构建，涵盖 DNN、RNN、LSTM 等结构。
*   利用 NLTK 库进行自然语言处理（NLP）任务及文本挖掘实战。
*   包含推荐系统、关联规则挖掘（Apriori, FP-Growth）及降维技术（PCA, SVD）等高级应用场景。

3. **适用场景**
*   机器学习初学者系统性学习算法原理并对照代码进行实战练习。
*   数据科学家或工程师快速查阅和复用经典算法及深度学习模型的实现代码。
*   高校学生或研究人员在进行 NLP、推荐系统或数据挖掘相关课题时的参考案例。

4. **技术亮点**
*   技术栈全面，无缝衔接传统统计学习、现代深度学习框架及自然语言处理工具。
*   标签丰富且覆盖主流算法，便于按特定技术领域（如 NLP、推荐系统）精准检索学习资源。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42416 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35721 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33773 | 🍴 4698 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28824 | 🍴 3517 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26016 | 🍴 2952 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21764 | 🍴 3309 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例和源代码，是学习人工智能技术的优质资源。它通过分类整理，帮助用户快速找到并复现各类前沿AI应用。

2. **核心功能**
- 提供500个完整的AI项目代码示例，覆盖主流算法与应用。
- 细分领域包括机器学习、深度学习、计算机视觉及NLP技术栈。
- 包含“Awesome”标签精选内容，确保项目质量与实用性。
- 支持Python为主要编程语言，便于直接运行和修改。

3. **适用场景**
- 初学者系统学习AI概念，通过阅读代码理解理论实现。
- 研究人员或工程师寻找特定任务（如图像识别、文本分析）的参考实现。
- 技术面试准备，通过复现经典项目展示编程与算法能力。
- 企业技术选型评估，快速了解不同AI解决方案的技术可行性。

4. **技术亮点**
- 规模庞大且分类清晰，一站式解决多领域AI学习需求。
- 高星标数（35721+）验证了其在社区中的广泛认可度和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35721 | 🍴 7379 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款利用人工智能自动化基于浏览器工作流的工具。它通过整合大语言模型（LLM）与计算机视觉技术，能够像人类一样理解网页并执行复杂的交互操作。该项目旨在提供一种比传统 RPA 更灵活、更具适应性的浏览器自动化解决方案。

**2. 核心功能**
*   **AI 驱动的流程执行**：利用 LLM 解析网页结构并动态生成操作指令，无需预先编写固定选择器。
*   **视觉感知与交互**：结合计算机视觉技术识别页面元素，支持点击、输入、滚动等复杂浏览器操作。
*   **全栈自动化能力**：基于 Playwright 构建，支持跨浏览器的稳定自动化，兼容各类 Web 应用。
*   **API 接口集成**：提供 API 供开发者将自动化能力嵌入到现有的业务流程或软件系统中。
*   **自适应网页处理**：能够应对页面布局变化或动态加载内容，减少因前端变更导致的脚本失效问题。

**3. 适用场景**
*   **企业级数据抓取**：从结构复杂或反爬严格的网站中提取非结构化数据并填入内部系统。
*   **RPA 流程增强**：替代传统 Selenium/Playwright 脚本，自动化需要人工判断的网页审批或录入流程。
*   **跨平台工作流整合**：在多个 Web 应用程序之间自动转移数据或触发操作，实现端到端业务闭环。

**4. 技术亮点**
*   **多模态 AI 融合**：创新性地结合了 LLM 的语言理解能力与视觉模型对 UI 元素的识别能力。
*   **无需硬编码选择器**：通过语义理解而非固定的 CSS/XPath 定位元素，显著降低了维护成本。
*   **开源且可扩展**：作为开源项目，允许用户根据特定需求定制 AI 代理的行为逻辑。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22595 | 🍴 2117 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，提供开源、云及企业版产品。它支持图像、视频和3D数据的AI辅助标注、质量控制及团队协作，并配备分析功能与开发者API。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注。
*   内置AI辅助标签功能，显著提升标注效率与准确性。
*   提供完善的质量保证机制及团队多人协作能力。
*   开放开发者API，便于集成到现有机器学习工作流中。

3. **适用场景**
*   为物体检测任务构建包含边界框的高精度训练数据集。
*   进行语义分割或图像分类等任务的数据标注与预处理。
*   大型团队协同处理大规模视频或3D视觉数据集。

4. **技术亮点**
*   兼容PyTorch和TensorFlow等主流深度学习框架生态。
*   提供从数据标注到数据分析的一站式完整解决方案。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16386 | 🍴 3775 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目提供了面向计算机视觉的高级AI可解释性工具，支持CNN、Vision Transformers等多种架构。它适用于分类、目标检测、图像分割及相似度计算等多种任务，旨在提升深度学习模型的透明度与可理解性。

2. **核心功能**
- 全面支持CNN、Vision Transformers等主流视觉模型的可解释性分析。
- 涵盖图像分类、目标检测、语义分割及图像相似度等多种任务场景。
- 提供Grad-CAM、Score-CAM等多种可视化技术以直观展示模型关注区域。

3. **适用场景**
- 深度学习模型调试与错误分析，帮助开发者定位模型失效原因。
- 医疗影像或自动驾驶等高可靠性要求领域的模型决策信任度评估。
- 学术研究与教学演示，用于直观展示神经网络的内部注意力机制。

4. **技术亮点**
- 广泛兼容PyTorch生态，支持多种前沿视觉架构（如ViT）。
- 集成多种SOTA可解释性算法（如Grad-CAM, Score-CAM），提供统一接口。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12930 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11290 | 🍴 1207 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 384183 | 🍴 80716 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261393 | 🍴 23326 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220730 | 🍴 42041 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198068 | 🍴 59638 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185695 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166380 | 🍴 21495 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164277 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157308 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156233 | 🍴 8882 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152422 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

