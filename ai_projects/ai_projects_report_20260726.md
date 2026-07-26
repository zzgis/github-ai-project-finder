# GitHub AI项目每日发现报告
日期: 2026-07-26

## 新发布的AI项目

### OptMem
- 1. **中文简介**
OptMem 旨在为 AI 智能体提供永久记忆能力。它仅需一个包含 426 个 token 的提示词和一个脚本，即可实现即插即用的部署体验。

2. **核心功能**
- 赋予 AI 智能体长期且持久的记忆存储能力。
- 通过极简的提示工程实现记忆管理，无需复杂架构。
- 提供脚本化接口，支持快速集成与即插即用。
- 优化记忆检索与更新机制，确保信息的高效调用。

3. **适用场景**
- 需要长期上下文保持的多轮对话智能体开发。
- 用户偏好或历史行为数据的持久化存储与管理。
- 资源受限环境下对轻量级记忆模块的需求。
- 快速原型验证中需要添加记忆功能的 AI 应用。

4. **技术亮点**
- 极致轻量化：仅依赖极短的提示词（426 tokens）即可实现核心功能。
- 低门槛集成：提供现成脚本，显著降低开发者接入记忆模块的技术成本。
- 链接: https://github.com/VictorTaelin/OptMem
- ⭐ 241 | 🍴 12 | 语言: Python

### deer-workflow
- 1. **中文简介**
deer-workflow 是一个开源的动态工作流运行时环境，旨在将业务流程编排保留在 TypeScript 中，同时将语义处理任务委派给可替换的 Agent 运行时。这种设计实现了逻辑控制与 AI 推理能力的解耦，允许开发者灵活切换底层智能引擎。

2. **核心功能**
- 支持动态工作流的运行时执行，适应多变的应用需求。
- 使用 TypeScript 进行工作流编排，提供类型安全和开发体验。
- 模块化设计，允许替换不同的 Agent 运行时以处理语义任务。
- 兼容 Bun 等现代 JavaScript/TypeScript 运行时环境。

3. **适用场景**
- 需要高度定制化逻辑控制的 AI 应用开发。
- 希望分离业务编排与 AI 推理能力的复杂系统架构。
- 基于 TypeScript 技术栈构建动态智能代理的工作流平台。

4. **技术亮点**
- 实现了编排层（TypeScript）与语义层（Agent Runtime）的清晰分离。
- 具备高度的可扩展性和灵活性，支持不同 Agent 后端的即插即用。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 76 | 🍴 11 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ocm-mcp-server
- ### 1. **中文简介**
ocm-mcp-server 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 智能体通过 Open Cluster Management (OCM) 中心节点操作多集群 Kubernetes 环境。它实现了模型与集群之间的策略管理、审批流程以及审计功能。该项目旨在为 AI 提供安全、可控的多集群管理能力。

### 2. **核心功能**
- **多集群控制**：通过 OCM Hub 统一管理和操作多个 Kubernetes 集群。
- **策略执行**：集成策略机制，确保 AI 操作符合预定义的安全和规范要求。
- **人工审批流**：在 AI 执行关键操作前引入审批环节，防止误操作。
- **操作审计**：记录所有由 AI 发起的操作日志，便于追溯和合规检查。
- **MCP 协议兼容**：遵循 MCP 标准，方便与其他支持该协议的 AI 工具链集成。

### 3. **适用场景**
- **企业级多集群运维自动化**：AI 代理自动执行跨集群的日常维护任务，同时受策略约束。
- **合规性驱动的云管平台**：在金融或政府等高监管行业，确保 AI 操作全程可审计且需审批。
- **混合云环境管理**：统一管理本地数据中心与公有云上的 Kubernetes 集群，由 AI 辅助调度。
- **开发者测试环境搭建**：快速部署和销毁测试集群，同时保留操作记录以供分析。

### 4. **技术亮点**
- **安全性增强**：将传统 Kubernetes RBAC 扩展至 AI 交互层，实现细粒度权限控制。
- **标准化接口**：利用 MCP 协议降低 AI 与基础设施之间的集成复杂度。
- **可扩展架构**：基于 Python 开发，易于根据特定业务需求定制策略和审批逻辑。
- 链接: https://github.com/sandeepbazar/ocm-mcp-server
- ⭐ 37 | 🍴 3 | 语言: Python

### Prompt-architect
- 1. **中文简介**
Prompt Architect Pro 是一款基于 Python 的桌面应用，利用本地 Ollama 大语言模型对原始文本和图片进行分析。它能将视觉描述提取并结构化转换为优化后的 JSON 提示词，供生成式 AI 使用。该应用内置 SQLite 数据库用于管理提示词，支持可调节的 VRAM 硬件配置，并提供兼容 ComfyUI 的节点以直接调用数据库内容。

2. **核心功能**
- 利用本地 Ollama LLM 分析文本与图像数据。
- 将视觉描述自动转化为结构化的 JSON 格式提示词。
- 内置 SQLite 数据库，支持提示词的存储、编辑与管理。
- 提供可调 VRAM 配置文件，适应不同硬件环境。
- 开发有 ComfyUI 节点，可直接集成工作流读取数据库提示词。

3. **适用场景**
- AI 绘画工作者需要批量将参考图转换为标准化 JSON 提示词以提升效率。
- 希望在低配或本地环境中运行 AI 工具，需精细控制显存（VRAM）使用的用户。
- ComfyUI 高级用户希望建立本地提示词库并在工作流中直接调用的场景。
- 需要对非结构化视觉信息进行标准化数据提取和处理的开发者。

4. **技术亮点**
- 实现了从非结构化视觉信息到结构化 JSON 提示词的自动化转换流程。
- 通过自定义 VRAM 配置文件和 ComfyUI 集成，增强了在本地部署环境下的灵活性与实用性。
- 链接: https://github.com/lololerigolo60/Prompt-architect
- ⭐ 36 | 🍴 3 | 语言: Python

### ai-stock-pool
- 1. **中文简介**
这是一个专注于AI产业链的股票池项目，支持美股与A股的映射对照。它具备主动发现潜力标的、评估政策压力以及一键部署等特性，旨在辅助投资研究。

2. **核心功能**
*   实现美股与A股在AI产业链上的精准映射与关联分析。
*   提供主动式股票发现机制以捕捉市场机会。
*   集成政策压力测试功能以评估宏观环境影响。
*   支持通过Vercel或Cloudflare Workers进行一键快速部署。

3. **适用场景**
*   AI产业链上下游企业的跨市场投资研究与对比分析。
*   需要快速搭建并部署股票监控工具的量化研究团队。
*   关注政策变动对特定科技板块影响的投资者。

4. **技术亮点**
*   采用Serverless架构（Cloudflare Workers/Vercel），实现低成本且高可用性的部署方案。
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
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理资源库，集成了敏感词检测、实体抽取（手机号、身份证等）、繁简转换及多种专业领域词库。它提供了从基础文本处理到高级深度学习模型（如 BERT）的丰富工具与数据集，旨在降低 NLP 开发门槛。该项目还涵盖了语音识别、知识图谱构建及对话机器人等多个维度的开源资源汇总。

2. **核心功能**
- **基础文本处理**：提供敏感词过滤、中英文语言检测、繁简体转换及中文分词加速工具。
- **信息抽取与校验**：支持手机号、邮箱、身份证等实体抽取，以及姓名性别推断和地名/运营商查询。
- **多领域词库与资源**：包含医学、法律、汽车、IT等垂直领域词汇库，以及古诗词、成语、停用词等通用语料。
- **深度学习与预训练模型**：整合了 BERT、ALBERT、GPT-2 等预训练模型的中文版本及相关微调代码。
- **问答与对话系统**：提供基于知识图谱的问答系统、闲聊机器人代码及多轮对话数据集。

3. **适用场景**
- **内容安全审核**：利用敏感词库和暴恐词表，快速实现社区评论、用户生成内容（UGC）的自动化过滤。
- **企业级信息结构化**：通过实体抽取和关系抽取工具，从非结构化文档或新闻中自动提取关键业务信息并构建知识库。
- **智能客服与聊天机器人开发**：借助现成的对话数据集、情感分析工具和预训练模型，快速搭建具备语义理解能力的客服系统。
- **NLP 研究与教学**：作为学习和研究中文 NLP 的基准资源包，用于复现经典算法、测试新模型或获取高质量标注数据。

4. **技术亮点**
- **一站式资源聚合**：将分散的 NLP 工具、数据集、论文和模型集中管理，极大节省了开发者搜集资料的时间。
- **覆盖全栈 NLP 任务**：从传统的规则匹配、词典查询到最新的基于 Transformer 的深度语义理解，覆盖了 NLP 的各个阶段。
- **注重中文特性优化**：特别针对中文场景提供了拼音标注、汉字特征提取、中文数字转换等细粒度处理工具。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82064 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。它汇集了丰富的实战案例，旨在为开发者提供从理论到实践的全方位学习资源。

2. **核心功能**
- 涵盖五大AI领域（机器学习、深度学习、CV、NLP等）的500个完整项目实例。
- 所有项目均附带可运行的源代码，方便直接复现和学习。
- 按技术领域分类整理，结构清晰，便于针对性查找所需算法实现。
- 作为“Awesome”列表，提供了经过筛选的高质量开源项目集合。

3. **适用场景**
- AI初学者通过阅读和运行代码快速掌握主流算法的实现细节。
- 工程师在进行技术选型或原型开发时，参考现有代码加速开发进程。
- 研究人员需要复现特定领域的经典模型或寻找对比实验基线时。

4. **技术亮点**
- 项目数量庞大且覆盖全面，是大规模AI实战资源的集中库。
- 强调“with code”，确保每个概念都有对应的工程落地示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ## 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流模型框架，能够直观展示模型结构，帮助开发者更好地理解和调试复杂算法。

## 2. **核心功能**
- 支持多种模型格式（如 ONNX、TensorFlow Lite、CoreML 等）的可视化展示
- 提供直观的图形化界面，清晰呈现神经网络架构与数据流向
- 兼容主流深度学习框架（PyTorch、Keras、TensorFlow 等）生成的模型
- 允许用户查看模型层参数和权重信息，便于调试和优化

## 3. **适用场景**
- 深度学习研究者需要快速理解新模型结构时进行可视化分析
- 工程师在部署模型前检查模型是否符合预期设计要求
- 教学场景中向初学者展示神经网络工作原理

## 4. **技术亮点**
- 轻量级设计，无需安装依赖即可运行，开箱即用
- 跨平台支持，可在 Windows、macOS 和 Linux 系统上使用
- 实时预览功能，修改模型配置后可即时查看效果
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换与部署。它允许开发者在不同平台间无缝迁移模型，打破单一框架的生态壁垒。通过统一表示形式，ONNX 提升了机器学习工作流的灵活性和兼容性。

2. **核心功能**
*   **跨框架模型转换**：支持从 PyTorch、TensorFlow、Keras 等主流框架导出模型到 ONNX 格式。
*   **运行时兼容性**：提供多种后端运行时（如 ONNX Runtime），可在 CPU、GPU 及边缘设备上高效执行模型推理。
*   **标准化模型表示**：定义通用的算子集和计算图结构，确保模型在不同环境中的语义一致性。
*   **生态系统集成**：与 scikit-learn、ML.NET 等工具链深度集成，简化传统机器学习模型的部署流程。

3. **适用场景**
*   **生产环境部署**：将训练好的模型转换为通用格式，以便在高性能推理服务器或移动端高效运行。
*   **框架迁移与验证**：在切换深度学习框架（如从 TensorFlow 迁移到 PyTorch）时，用于对比模型精度和性能。
*   **硬件加速优化**：利用特定硬件加速器（如 NPU、FPGA）提供的 ONNX 后端进行模型加速推理。
*   **混合模型集成**：在同一个系统中组合来自不同框架训练的多个模型组件，实现复杂业务逻辑。

4. **技术亮点**
*   **开放标准地位**：由微软、Facebook 等科技巨头共同发起并维护，拥有广泛的行业支持和社区活跃度。
*   **高性能推理引擎**：配套的 ONNX Runtime 提供低延迟、高吞吐量的推理能力，并支持动态形状和量化优化。
*   **丰富的算子支持**：涵盖计算机视觉、自然语言处理等领域的常用神经网络层和算子，适配性强。
- 链接: https://github.com/onnx/onnx
- ⭐ 21216 | 🍴 3976 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一部全面涵盖机器学习工程实践的指南。它深入探讨了从模型训练、调试到推理部署及大规模扩展的各个环节。该项目旨在为构建高效、可扩展的AI系统提供实用的工程最佳实践。

2. **核心功能**
- 提供大语言模型（LLM）和Transformer架构的训练与推理优化策略。
- 详解使用PyTorch进行分布式训练、GPU资源管理及SLURM集群调度的具体方法。
- 涵盖MLOps全流程，包括数据存储、网络配置及系统可扩展性设计。
- 包含针对机器学习系统的深度调试技巧与性能瓶颈分析指南。

3. **适用场景**
- 需要在大规模集群上高效训练或微调大型语言模型的开发团队。
- 致力于优化模型推理延迟并降低计算成本的MLOps工程师。
- 希望建立稳定、可扩展且易于维护的机器学习生产基础设施的企业。

4. **技术亮点**
- 结合底层硬件知识（如GPU、存储、网络）与上层框架（PyTorch/Transformers），提供端到端的工程解决方案。
- 针对当前热门的LLM领域，提供了经过验证的最佳实践而非纯理论概念。
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
- ⭐ 10677 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。它汇集了丰富的实战案例，旨在为开发者提供从理论到实践的全方位学习资源。

2. **核心功能**
- 涵盖五大AI领域（机器学习、深度学习、CV、NLP等）的500个完整项目实例。
- 所有项目均附带可运行的源代码，方便直接复现和学习。
- 按技术领域分类整理，结构清晰，便于针对性查找所需算法实现。
- 作为“Awesome”列表，提供了经过筛选的高质量开源项目集合。

3. **适用场景**
- AI初学者通过阅读和运行代码快速掌握主流算法的实现细节。
- 工程师在进行技术选型或原型开发时，参考现有代码加速开发进程。
- 研究人员需要复现特定领域的经典模型或寻找对比实验基线时。

4. **技术亮点**
- 项目数量庞大且覆盖全面，是大规模AI实战资源的集中库。
- 强调“with code”，确保每个概念都有对应的工程落地示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35731 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ## 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流模型框架，能够直观展示模型结构，帮助开发者更好地理解和调试复杂算法。

## 2. **核心功能**
- 支持多种模型格式（如 ONNX、TensorFlow Lite、CoreML 等）的可视化展示
- 提供直观的图形化界面，清晰呈现神经网络架构与数据流向
- 兼容主流深度学习框架（PyTorch、Keras、TensorFlow 等）生成的模型
- 允许用户查看模型层参数和权重信息，便于调试和优化

## 3. **适用场景**
- 深度学习研究者需要快速理解新模型结构时进行可视化分析
- 工程师在部署模型前检查模型是否符合预期设计要求
- 教学场景中向初学者展示神经网络工作原理

## 4. **技术亮点**
- 轻量级设计，无需安装依赖即可运行，开箱即用
- 跨平台支持，可在 Windows、macOS 和 Linux 系统上使用
- 实时预览功能，修改模型配置后可即时查看效果
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33266 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了一系列必不可少的速查表（Cheat Sheets）。这些资源旨在帮助研究者快速回顾和掌握关键概念、库函数及代码模式，源自Medium博主Kailash Ahirwar的精选推荐。

2. **核心功能**
- 提供涵盖深度学习框架（如Keras）和数据处理库（如NumPy、SciPy）的快速参考指南。
- 包含数据可视化库Matplotlib的使用技巧与常用代码片段。
- 整理人工智能领域的基础理论与核心算法速记内容。
- 以简洁的文档形式呈现，便于在开发过程中快速查阅。

3. **适用场景**
- 机器学习初学者在进行项目实战时，作为快速入门和查阅API的辅助工具。
- 研究人员在撰写论文或复现算法时，用于核对数学公式或框架用法。
- 工程师在日常开发中，需要快速回忆特定库（如NumPy矩阵操作）的语法细节时。

4. **技术亮点**
- 聚合了多个主流AI生态组件（Keras, Matplotlib, NumPy等）的核心知识点，形成一站式参考资料。
- 内容经过筛选，专注于“必备”知识，去除了冗余信息，极大提升了检索效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一套完整的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材。内容涵盖从零基础入门到就业实战的全流程，包括Python、数学、机器学习、深度学习及计算机视觉等热门领域。

2. **核心功能**
- 提供结构化的AI学习路径，涵盖从基础编程到高级算法的完整知识体系。
- 整理近200个实战案例和项目代码，支持多框架（如PyTorch, TensorFlow, Keras）实践。
- 免费提供配套学习资料，帮助初学者快速上手并实现就业导向的技能提升。
- 覆盖数据分析、自然语言处理、计算机视觉等多个垂直领域的热门技术栈。

3. **适用场景**
- **零基础转行人员**：希望通过系统路线和实战项目快速掌握AI技能并求职的人群。
- **在校学生**：需要补充课堂知识之外的实战案例和技术前沿了解的学生群体。
- **从业者进阶**：希望系统复习或扩展在特定子领域（如NLP、CV）技术深度的技术人员。

4. **技术亮点**
- 资源高度整合，将分散的学习资料、代码库和路线图统一在一个开源项目中。
- 强调“就业实战”，通过大量真实案例连接理论与实际应用，缩短学习曲线。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13186 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他 AI 模型的构建与训练流程。它通过声明式配置降低开发门槛，使数据科学家和工程师能更高效地进行模型迭代。该项目支持多种主流深度学习架构，并专注于提升机器学习工作的可重复性与易用性。

**2. 核心功能**
*   **低代码/声明式配置**：通过简单的 YAML 或 JSON 配置文件即可定义模型结构、输入输出及预处理逻辑，无需编写大量底层代码。
*   **多模态支持**：原生支持文本、图像、表格等多种数据类型，便于构建处理复杂输入的多模态 AI 应用。
*   **端到端训练与评估**：内置完整的数据加载、模型训练、超参数调整及性能评估流水线，实现从数据到部署的快速闭环。
*   **集成主流框架**：底层兼容 PyTorch 等深度学习库，同时提供对 LLM（如 Llama、Mistral）微调的专门优化支持。
*   **实验管理与可复现性**：自动记录训练过程、指标及模型权重，确保实验结果的可追踪性和高可复现性。

**3. 适用场景**
*   **快速原型开发**：适用于希望在极短时间内验证 AI 想法或构建基础模型原型的团队和个人开发者。
*   **企业级数据科学工作流**：适合需要标准化、可维护且易于协作的机器学习流程的大型组织，降低对资深算法工程师的依赖。
*   **LLM 微调与定制**：针对希望基于开源基座模型（如 Llama 2/3、Mistral）进行领域特定知识微调，但不想深入处理底层分布式训练细节的用户。
*   **多模态应用构建**：用于开发同时处理文本描述和图像内容的智能应用，如视觉问答系统或内容审核工具。

**4. 技术亮点**
*   **Data-Centric AI 理念**：强调数据质量与预处理的重要性，提供丰富的数据增强和清洗工具，助力构建更鲁棒的模型。
*   **开箱即用的最佳实践**：预置了多种经典神经网络架构（如 CNN、RNN、Transformer）的最佳配置模板，显著减少调参成本。
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
- ⭐ 6297 | 🍴 756 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理资源库，集成了敏感词检测、实体抽取（手机号、身份证等）、繁简转换及多种专业领域词库。它提供了从基础文本处理到高级深度学习模型（如 BERT）的丰富工具与数据集，旨在降低 NLP 开发门槛。该项目还涵盖了语音识别、知识图谱构建及对话机器人等多个维度的开源资源汇总。

2. **核心功能**
- **基础文本处理**：提供敏感词过滤、中英文语言检测、繁简体转换及中文分词加速工具。
- **信息抽取与校验**：支持手机号、邮箱、身份证等实体抽取，以及姓名性别推断和地名/运营商查询。
- **多领域词库与资源**：包含医学、法律、汽车、IT等垂直领域词汇库，以及古诗词、成语、停用词等通用语料。
- **深度学习与预训练模型**：整合了 BERT、ALBERT、GPT-2 等预训练模型的中文版本及相关微调代码。
- **问答与对话系统**：提供基于知识图谱的问答系统、闲聊机器人代码及多轮对话数据集。

3. **适用场景**
- **内容安全审核**：利用敏感词库和暴恐词表，快速实现社区评论、用户生成内容（UGC）的自动化过滤。
- **企业级信息结构化**：通过实体抽取和关系抽取工具，从非结构化文档或新闻中自动提取关键业务信息并构建知识库。
- **智能客服与聊天机器人开发**：借助现成的对话数据集、情感分析工具和预训练模型，快速搭建具备语义理解能力的客服系统。
- **NLP 研究与教学**：作为学习和研究中文 NLP 的基准资源包，用于复现经典算法、测试新模型或获取高质量标注数据。

4. **技术亮点**
- **一站式资源聚合**：将分散的 NLP 工具、数据集、论文和模型集中管理，极大节省了开发者搜集资料的时间。
- **覆盖全栈 NLP 任务**：从传统的规则匹配、词典查询到最新的基于 Transformer 的深度语义理解，覆盖了 NLP 的各个阶段。
- **注重中文特性优化**：特别针对中文场景提供了拼音标注、汉字特征提取、中文数字转换等细粒度处理工具。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82064 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目曾获 ACL 2024 会议收录，旨在简化从预训练到对齐的完整微调流程。它通过整合多种先进技术与算法，为研究人员和开发者提供了轻量级且高性能的微调解决方案。

2. **核心功能**
- 支持 100+ 种 LLM 和 VLM 的统一高效微调，涵盖 Llama、Qwen、Gemma 等主流架构。
- 内置多种微调算法，包括 LoRA、QLoRA、P-Tuning 以及全参数微调等参数高效方法。
- 集成 RLHF（基于人类反馈的强化学习）、DPO 及 KTO 等对齐技术，优化模型输出质量。
- 提供量化工具支持（如 GPTQ、AWQ），显著降低显存占用并加速推理过程。
- 兼容 Transformers、PEFT 等主流生态库，实现开箱即用的训练与评估体验。

3. **适用场景**
- 企业私有化部署：利用 QLoRA 等技术，在消费级显卡上高效微调大模型以适应特定业务需求。
- 多模态应用开发：针对包含图像理解的视觉语言模型进行微调，构建具备图文交互能力的智能助手。
- 模型对齐研究：使用 DPO 或 RLHF 算法调整模型价值观，使其回答更符合人类偏好和安全标准。
- 快速原型验证：通过统一的接口快速测试不同基座模型在特定指令数据集上的表现，加速算法迭代。

4. **技术亮点**
- **极致轻量化**：原生支持 QLoRA 和 4bit/8bit 量化，大幅降低硬件门槛。
- **多模态统一性**：在同一框架下无缝切换文本生成与视觉理解任务的微调。
- **全流程覆盖**：从数据处理、模型训练到推理导出，提供端到端的完整工作流支持。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73527 | 🍴 8987 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松掌握AI知识。该项目由Microsoft For Beginners提供支持，内容涵盖从机器学习到深度学习的核心概念。通过Jupyter Notebook进行互动式学习，帮助初学者系统性地构建AI技能树。

2. **核心功能**
*   提供结构化的12周学习计划，将复杂AI概念拆解为24个易理解的课时。
*   基于Jupyter Notebook实现交互式代码练习，支持即时运行与结果可视化。
*   涵盖广泛的技术领域，包括机器基础、深度学习、计算机视觉（CNN）、自然语言处理（RNN）及生成对抗网络（GAN）。
*   专为零基础或初级学习者设计，强调“AI for All”的普及教育理念。

3. **适用场景**
*   初学者自学：适合对AI感兴趣但无深厚数学或编程背景的学员进行系统性入门。
*   课堂教学辅助：教师可作为计算机科学或数据科学课程的标准化教材和实验指南。
*   企业内训基础：用于快速提升非技术团队或部分技术人员的人工智能基础认知。
*   开源社区实践：开发者可通过修改Notebook中的代码来深入理解各个AI算法的具体实现。

4. **技术亮点**
*   采用微软For Beginners系列的教育框架，确保内容的通俗性与准确性平衡。
*   整合了当前主流的AI子领域（如CV、NLP），使单一项目具备多维度的技术覆盖能力。
*   高度依赖Jupyter生态，便于在本地或云端（如GitHub Codespaces）无缝运行代码。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52903 | 🍴 10746 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- ### 1. **中文简介**
该项目旨在通过从零开始的方式，深入解析并构建人工智能工程的核心组件，帮助学习者彻底掌握其原理。它不仅提供理论教程，更强调实际动手构建与部署，致力于培养能够独立开发AI应用的专业能力。

### 2. **核心功能**
*   涵盖从基础机器学习到高级生成式AI的完整学习路径。
*   提供基于Python和Rust的底层算法从零实现教程。
*   集成LLM、计算机视觉及多智能体系统（Swarm Intelligence）等前沿技术案例。
*   包含MCP（Model Context Protocol）等新兴AI工程标准的实践指南。

### 3. **适用场景**
*   AI初学者希望深入理解模型底层逻辑而非仅调用API。
*   工程师需要构建高性能、可定制的本地化AI服务或代理系统。
*   研究人员探索多智能体协作、强化学习及新型AI架构的创新实验。

### 4. **技术亮点**
*   采用“Learn it, Build it, Ship it”的实战驱动教学法，强调端到端交付能力。
*   跨语言支持，结合Python的快速开发与Rust的高性能优势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43737 | 🍴 7358 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- **中文简介**
AiLearning 是一个全面的数据分析与机器学习实战指南，涵盖了从线性代数基础到 PyTorch、NLTK 及 TensorFlow 2 等前沿框架的应用。该项目通过丰富的代码示例，系统性地梳理了传统机器学习算法与现代深度学习技术的核心实现。

**核心功能**
1. 集成经典机器学习算法（如 SVM、K-Means、随机森林等）的 Python 实战代码。
2. 深入讲解自然语言处理（NLP）技术，包括使用 NLTK 进行文本分析及 Transformer 等模型应用。
3. 提供基于 PyTorch 和 TensorFlow 2 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）等深度学习模型构建与训练。
4. 涵盖推荐系统、数据降维（PCA/SVD）及关联规则挖掘（Apriori/FP-Growth）等特定领域解决方案。

**适用场景**
1. 机器学习初学者系统学习算法原理及代码实现的入门教程。
2. 数据分析师参考传统统计方法与机器学习结合解决业务问题的案例库。
3. 研究人员或开发者快速复现 NLP 任务及深度学习模型的技术文档。

**技术亮点**
项目标签涵盖了从基础统计学习到前沿大模型生态（TF2/PyTorch）的全栈技术体系，且拥有极高的社区关注度（4万+星标），证明了其作为综合性学习资源的高质量和广泛认可度。
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
- ⭐ 3300 | 🍴 405 | 语言: Python
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
- ⭐ 384224 | 🍴 80725 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 261562 | 🍴 23345 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 220902 | 🍴 42114 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198110 | 🍴 59647 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185698 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166392 | 🍴 21495 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164279 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157313 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156424 | 🍴 8890 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152442 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

