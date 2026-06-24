# GitHub AI项目每日发现报告
日期: 2026-06-24

## 新发布的AI项目

### valorant-ai-aimbot-undetected
- 我无法提供该项目的分析、翻译或技术细节，因为“Valorant AI Aimbot”（无畏契约人工智能自瞄外挂）属于游戏作弊工具，违反了游戏规则及相关法律法规。

作为AI助手，我不能协助开发、分发或使用任何用于破坏游戏公平性或绕过安全机制的软件。如果您对其他合法的开源项目感兴趣，例如计算机视觉在体育分析中的应用、合法的游戏辅助插件开发（如宏定义工具，需符合平台规则）或机器学习在竞技策略中的研究，我很乐意为您提供相关信息和分析。
- 链接: https://github.com/Valorant-AI/valorant-ai-aimbot-undetected
- ⭐ 314 | 🍴 0 | 语言: C++

### tupper
- 1. **中文简介**
Tupper 是一个开源的沙箱环境，专为 AI 智能体设计，允许用户在本地机器上安全地运行不可信且由 AI 生成的代码。它通过隔离执行环境，有效防止恶意代码对宿主系统造成损害，确保 AI 代理操作的安全性。

2. **核心功能**
*   支持在本地运行由 AI 生成的不可信代码。
*   提供基于 Apple Container 等技术的轻量级沙箱隔离。
*   兼容 Bun、Node.js 等主流运行时环境。
*   集成 MCP（Model Context Protocol）以增强 AI 智能体的交互能力。
*   作为 E2B 等云沙箱服务的替代方案，实现私有化部署。

3. **适用场景**
*   AI 驱动的代码解释器应用，需本地安全执行用户或模型生成的脚本。
*   构建基于 LLM 的智能体系统，用于自动化测试或数据处理任务。
*   开发需要 MCP 协议支持的上下文增强型 AI 助手。
*   希望替代云服务沙箱（如 E2B），追求数据隐私和低成本运行的开发者。

4. **技术亮点**
*   采用 Firecracker 微虚拟机技术和 Apple Container，提供高性能且安全的硬件级隔离。
*   原生支持 TypeScript 生态，便于现代 Web 和 Node.js 开发者集成。
*   作为 E2B 的开源替代品，降低了使用 AI 沙箱的基础设施依赖成本。
- 链接: https://github.com/lightbearco/tupper
- ⭐ 120 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, apple-container, bun, code-execution, code-interpreter

### Hello-Agents
- ### 1. 中文简介
该项目是一个从基础到生产级多智能体应用的全面实战教程，旨在指导用户从零开始构建 AI 代理系统。它深入讲解了如何利用 LangChain、LLM 及 RAG 等技术，开发复杂的交互式人工智能应用。

### 2. 核心功能
*   提供从理论到代码实现的完整多智能体系统构建指南。
*   集成 LangChain 和 OpenAI API 等主流工具链进行开发实践。
*   涵盖检索增强生成（RAG）技术在智能体中的应用方法。
*   展示如何设计并调试具有协作能力的复杂 AI 代理架构。

### 3. 适用场景
*   希望深入理解并掌握多智能体系统架构的开发者学习。
*   需要构建基于大语言模型的企业级自动化工作流或助手。
*   研究如何将 RAG 技术与智能体结合以提升回答准确性的场景。
*   探索从单智能体向多智能体协作演进的技术路径。

### 4. 技术亮点
*   采用“从 scratch（从零开始）”的教学方式，不仅依赖黑盒库，更强调底层逻辑理解。
*   聚焦于生产级标准，兼顾了理论深度与实际工程落地能力。
- 链接: https://github.com/Reyzowter/Hello-Agents
- ⭐ 107 | 🍴 3 | 语言: Python
- 标签: agent, ai, deep-learning, langchain, llm

### ESEILANE
- **1. 中文简介**
ESEILANE 是一款专为人工智能、大语言模型及 GraphRAG 应用打造的高性能知识图谱引擎，旨在构建下一代智能应用。它通过结合多种编程语言的优势，提供了高效的知识存储与检索能力。该项目致力于解决复杂数据关系下的智能化处理需求。

**2. 核心功能**
*   支持高性能的知识图谱存储与查询操作。
*   原生适配 LLM 和 GraphRAG 架构，优化检索增强生成流程。
*   兼容 OpenCypher 查询语言，便于开发者快速上手。
*   提供多语言接口支持，涵盖 Python、TypeScript 等主流生态。

**3. 适用场景**
*   构建基于大语言模型的智能问答系统，利用图谱提升回答准确性。
*   开发需要复杂关系推理的企业级知识管理应用。
*   实施 GraphRAG 方案，以解决传统 RAG 在处理多跳关系时的局限性。
*   作为后端引擎支持需要实时图数据分析的 AI 应用。

**4. 技术亮点**
*   **混合语言架构**：底层可能利用 Rust 或 GraphBLAS 实现极致性能，同时通过 Ruby、Python 等提供易用接口。
*   **GraphRAG 深度集成**：针对检索增强生成场景进行了特定优化，优于通用数据库。
*   **标准协议支持**：支持 OpenCypher 标准，降低了迁移和学习成本。
- 链接: https://github.com/Simpl3x3/ESEILANE
- ⭐ 105 | 🍴 3 | 语言: Ruby
- 标签: ai, graph-database, graphblas, graphrag, knowledge-graph

### AgentLens
- 基于您提供的信息，以下是关于 GitHub 项目 **AgentLens** 的技术分析：

1. **中文简介**
   AgentLens 是一个专为大型语言模型（LLM）智能体设计的轻量级上下文压缩工具。它旨在通过优化输入信息的长度和结构，提升智能体在处理复杂任务时的效率与性能。

2. **核心功能**
   - 自动压缩 LLM 智能体的对话历史或上下文窗口，减少 Token 消耗。
   - 保持关键语义信息不丢失，确保智能体决策的准确性。
   - 集成于智能体工作流中，支持多智能体协作场景下的信息过滤。
   - 提供轻量级实现，便于快速部署和嵌入现有 Python 项目中。
   - 兼容主流 AI 模型（如 Claude、OpenAI 等），增强通用性。

3. **适用场景**
   - **长对话记忆管理**：在多轮交互中限制上下文长度，防止超出模型 Token 上限。
   - **成本敏感型应用**：通过减少输入 Token 数量，显著降低 API 调用费用。
   - **多智能体系统**：在多个 AI 代理协同工作时，精简传递给下一个代理的信息负载。
   - **实时响应需求**：加快上下文处理速度，提升智能体对复杂指令的响应效率。

4. **技术亮点**
   - **轻量级架构**：无需重型依赖，易于集成到现有 Agent 框架中。
   - **高兼容性**：明确支持 Claude 系列及开放源码 AI 工具，适配主流智能体规则。
   - **聚焦智能体技能**：针对“Agent Skills”和“Agentic Workflow”优化，而非通用文本摘要，更贴合 AI 代理的工作逻辑。
- 链接: https://github.com/ObsidianOwl123/AgentLens
- ⭐ 83 | 🍴 0 | 语言: Python
- 标签: agent-skills, agentic-workflow, ai, ai-agent-rules, ai-agents

### fastloops
- 描述: Fast and one click setup with AI loops — run, check, fix, repeat until done.
- 链接: https://github.com/Her-shey/fastloops
- ⭐ 33 | 🍴 0 | 语言: Python

### gensee-crate
- 描述: Local-first runtime safety for AI coding agents
- 链接: https://github.com/GenseeAI/gensee-crate
- ⭐ 30 | 🍴 0 | 语言: Rust

### claude-mythos-ai-anthropic-desktop-app
- 描述: claude mythos ai anthropic free large language model llm frontier model project glasswing cybersecurity agent vulnerability research software engineering agentic workflows multi step reasoning recurrent depth transformer rdt openmythos repository open source claude fable 5 multi agent
- 链接: https://github.com/ikarma/claude-mythos-ai-anthropic-desktop-app
- ⭐ 25 | 🍴 0 | 语言: TypeScript
- 标签: claude-chat, claude-code-, claude-code-action, claude-code-prompts, claude-code-routine

### ai-short-drama-agent-company
- 描述: Complete Matrix department template pack for running an AI short-drama production company. Includes 5 skills, 3 departments with memory, and Empire of Dust demo (700k+ YouTube views). Bilingual README.
- 链接: https://github.com/1229119561Weike/ai-short-drama-agent-company
- ⭐ 23 | 🍴 5 | 语言: Python

### ritual-chain-workshop
- 描述: Building and deploying an on-chain AI bounty judge on Ritual - 23.06.2026
- 链接: https://github.com/cozfuttu/ritual-chain-workshop
- ⭐ 18 | 🍴 47 | 语言: TypeScript

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）工具包，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）、分词、词性标注、情感分析及命名实体识别等核心功能。该项目不仅提供了基础的文本处理能力，还包含了海量的中文领域知识库（如人名、地名、行业术语）、预训练模型资源以及丰富的数据集和前沿算法实现。它旨在为开发者提供一个一站式解决方案，涵盖从传统NLP任务到基于深度学习（如BERT、GPT）的高级应用开发。

### 2. **核心功能**
*   **基础文本处理**：支持中英文分词、词性标注、句法分析、繁简转换、同义词/反义词查找及文本情感分析。
*   **实体识别与信息抽取**：内置规则与模型，可精准抽取手机号、身份证、邮箱、地名、人名等实体，并支持医疗、金融等领域专用NER。
*   **知识库与语料资源**：提供大规模中文词库（如成语、古诗、行业术语）、停用词表、敏感词库及多领域对话语料和问答数据集。
*   **深度学习模型集成**：整合了BERT、GPT、ALBERT、RoBERTa等主流预训练模型的中文版本及相关微调代码，支持文本分类、序列标注等任务。
*   **实用工具链**：包含OCR文字识别、语音识别（ASR）、文本纠错、相似度计算、关键词抽取及自动化摘要生成等实用工具。

### 3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析功能，快速识别和过滤互联网内容中的违规、暴恐或不良信息。
*   **智能客服与对话系统**：结合知识库、意图识别和预训练对话模型，构建具备上下文理解能力的自动问答机器人。
*   **企业级数据分析**：从非结构化文本（如新闻、评论、文档）中提取关键实体（如公司名、产品名）和观点，用于舆情监控和市场洞察。
*   **NLP算法研究与教学**：作为学习和复现最新NLP算法（如BERT微调、关系抽取）的基准资源库，适合高校和研究机构使用。

### 4. **技术亮点**
*   **资源极度丰富**：汇聚了数百个高质量中文数据集、词库及前沿论文代码，是中文NLP领域的“资源百科全书”。
*   **全流程覆盖**：从底层的数据清洗、标注工具，到中层的NLP处理库，再到上层的预训练模型和应用案例，实现了全栈式覆盖。
*   **紧跟技术前沿**：及时收录并整合了BERT、Transformer、GPT-2等最新AI技术的中文适配版本及最佳实践代码。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81422 | 🍴 15242 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34822 | 🍴 7291 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33125 | 🍴 3137 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个旨在促进机器学习模型互操作性的开放标准。它允许开发者在不同深度学习框架之间无缝迁移和部署模型，打破了生态系统的壁垒。通过统一模型表示格式，ONNX 简化了从训练到生产环境的全流程开发。

### 2. 核心功能
*   **跨框架兼容性**：支持 PyTorch、TensorFlow、Scikit-learn 等主流框架模型的导入与导出。
*   **标准化模型格式**：定义统一的计算图结构，确保模型在不同平台和硬件上的可移植性。
*   **推理优化加速**：配合 ONNX Runtime 等执行引擎，实现高性能、低延迟的模型推理。
*   **生态系统集成**：与 Keras 等高层 API 及各类 AI 工具链深度集成，降低使用门槛。

### 3. 适用场景
*   **模型部署**：将训练好的模型转换为通用格式，部署到服务器、移动端或嵌入式设备。
*   **框架迁移**：在不重写代码的情况下，将模型从一种训练框架（如 TensorFlow）迁移到另一种（如 PyTorch）。
*   **性能调优**：利用 ONNX 优化工具对模型进行量化、剪枝等操作，以提升推理速度并减少资源消耗。

### 4. 技术亮点
*   **开放中立**：由微软、Facebook 等巨头共同维护，避免了厂商锁定，保障了社区的长期活力。
*   **广泛支持**：拥有庞大的社区支持和丰富的算子库，几乎覆盖所有常见的深度学习操作。
*   **高效运行时**：配套的 ONNX Runtime 提供了跨平台的高性能推理能力，支持 CPU、GPU 等多种硬件加速。
- 链接: https://github.com/onnx/onnx
- ⭐ 21036 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放手册》是一本全面指导机器学习系统构建与维护的工程实践指南。内容涵盖从大规模训练、高效推理到基础设施优化的全流程最佳实践。旨在帮助工程师解决可扩展性、调试及硬件资源管理等实际工程难题。

2. **核心功能**
*   提供大语言模型（LLM）训练与微调的系统化工程策略。
*   详解基于PyTorch和Transformers的高效分布式训练架构。
*   深入剖析GPU集群管理、网络通信优化及存储解决方案。
*   包含针对推理服务部署、性能调优及故障排查的实用技巧。
*   介绍利用Slurm等调度工具管理大规模计算资源的最佳实践。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习训练集群的数据科学家团队。
*   致力于降低大模型推理成本并提升响应速度的后端工程团队。
*   希望建立标准化MLOps流程以实现模型稳定部署与监控的企业。
*   正在解决多卡/多节点训练中出现性能瓶颈或调试难题的高级工程师。

4. **技术亮点**
*   **实战导向**：紧密结合PyTorch、Hugging Face Transformers等主流开源生态的具体代码与配置案例。
*   **全栈覆盖**：横跨底层硬件（GPU/网络）、中间件（Slurm/Docker）及应用层（训练/推理），形成完整知识闭环。
*   **前沿聚焦**：特别针对当前热门的Large Language Models（LLMs）提供了专门的扩展性与效率优化章节。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18167 | 🍴 1152 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17251 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13085 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11520 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10639 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个收录了500个涵盖人工智能、机器学习、深度学习、计算机视觉及自然语言处理等领域的代码项目合集。它提供了丰富的实战案例，旨在帮助开发者通过完整的代码示例深入理解各类AI技术的应用。

2. **核心功能**
*   提供500个精选AI相关项目的完整代码实现。
*   覆盖机器学习、深度学习、计算机视觉和NLP四大主流领域。
*   作为“Awesome”系列资源，整理并分类了高质量的学习与开发案例。
*   支持Python等语言编写的实际项目，便于直接运行和学习。

3. **适用场景**
*   AI初学者进行系统性学习和代码模仿练习。
*   数据科学家寻找特定算法或任务（如图像识别、文本分析）的参考实现。
*   开发者快速构建原型时获取现成的代码模块和思路。
*   教育机构用于教授机器学习与深度学习课程的实例素材。

4. **技术亮点**
该项目最大的亮点在于其全面性和实用性，通过整合500个真实代码库，为学习者提供了一个从理论到实践的完整资源闭环，特别适合作为入门到进阶的综合性参考指南。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34822 | 🍴 7291 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够以直观的图形界面展示模型架构与参数。该工具旨在帮助开发者快速理解和分析复杂的模型结构。

**2. 核心功能**
*   广泛支持 Keras、PyTorch、TensorFlow、ONNX、CoreML 等主流框架的模型格式。
*   提供清晰的图形化界面，直观展示网络层结构、连接关系及权重参数。
*   支持在浏览器或桌面端直接运行，无需安装复杂的环境依赖。
*   允许用户查看和编辑模型的具体配置信息，便于调试和优化。

**3. 适用场景**
*   **模型调试**：在训练过程中检查模型架构是否正确，定位潜在的结构错误。
*   **论文复现与分析**：可视化他人发布的模型结构，辅助理解算法细节和设计思路。
*   **跨平台迁移验证**：在不同框架间转换模型时，通过可视化确认转换后的结构一致性。
*   **教学演示**：向初学者或非技术人员直观展示神经网络的内部工作原理。

**4. 技术亮点**
*   极高的兼容性，几乎覆盖了当前所有流行的深度学习模型格式。
*   基于 Web 技术构建，实现轻量级部署，随时随地即可访问。
*   开源且社区活跃，持续更新以支持最新的模型标准和框架特性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33125 | 🍴 3137 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13085 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大语言模型（LLM）、神经网络及其他人工智能模型。它降低了 AI 开发的门槛，使数据科学家和工程师能够专注于模型训练与微调，而无需编写大量底层代码。

2. **核心功能**
*   提供声明式的 YAML 配置接口，支持快速定义和训练各种深度学习模型。
*   内置对主流大语言模型（如 LLaMA、Mistral）的微调与推理支持。
*   兼容 PyTorch 等主流深度学习后端，简化模型部署与集成流程。
*   涵盖计算机视觉、自然语言处理等多模态任务的数据中心（Data-centric）处理能力。

3. **适用场景**
*   企业级 AI 应用开发，需快速搭建定制化推荐系统或分类模型。
*   研究人员进行大语言模型的指令微调（Instruction Tuning）及实验验证。
*   数据科学团队希望以低代码方式整合传统机器学习与深度学习工作流。

4. **技术亮点**
*   采用“数据为中心”的设计哲学，强调数据预处理对模型性能的直接影响。
*   高度模块化架构，允许用户灵活组合不同的输入输出类型和神经网络层。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11722 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9115 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8907 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8377 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6163 | 🍴 721 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81422 | 🍴 15242 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与多模态大模型（VLM）微调框架，相关成果已被 ACL 2024 收录。它支持超过 100 种主流模型的指令微调、RLHF 及量化训练，旨在降低大模型适配的技术门槛。

2. **核心功能**
*   支持 QLoRA、LoRA 等多种高效参数微调方法，显著降低显存占用。
*   兼容 100 多种主流开源 LLM 和 VLM，实现统一的训练接口。
*   内置 RLHF（人类反馈强化学习）、DPO 等对齐训练算法。
*   提供可视化的 Web UI 界面和命令行工具，简化实验配置与管理。
*   支持全量微调与量化微调（如 GPTQ、AWQ），平衡性能与资源消耗。

3. **适用场景**
*   **企业私有化部署**：针对特定业务数据对 Llama、Qwen、DeepSeek 等模型进行指令微调，提升垂直领域表现。
*   **学术研究实验**：快速复现 SFT、RLHF 等前沿算法，验证不同模型架构在特定任务上的效果。
*   **多模态应用开发**：微调 LLaVA 等视觉语言模型，实现图像理解与生成类 AI 应用。
*   **低资源环境适配**：利用 QLoRA 技术在消费级显卡上完成大型模型的微调训练。

4. **技术亮点**
*   **极致的高效性**：通过统一的底层架构优化了训练效率，支持混合精度训练和梯度检查点技术。
*   **广泛的模型兼容性**：无缝集成 Transformers、PEFT 等主流库，覆盖从 Llama 到 Gemma 等最新模型家族。
*   **用户友好生态**：提供开箱即用的数据集加载器和模型导出功能，极大简化了从训练到部署的全流程。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72446 | 🍴 8862 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。项目主要基于Jupyter Notebook构建，内容涵盖从机器学习基础到深度学习的高级应用。

2. **核心功能**
*   提供结构化的12周学习路径，分为24个独立课时，循序渐进地引导学习者。
*   涵盖广泛的AI核心主题，包括机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）。
*   采用Jupyter Notebook作为主要交互形式，支持代码编写与结果即时可视化，便于实践操作。
*   由微软“初学者计划”支持，内容设计注重普及性，适合零基础或非专业背景的学习者。

3. **适用场景**
*   希望系统性地从零开始学习人工智能概念的初学者或转行人员。
*   高校教师或培训机构用于开设人工智能通识课程或工作坊的教学资源。
*   希望快速了解AI前沿技术（如CNN、RNN、GAN）应用场景的技术爱好者。

4. **技术亮点**
*   项目拥有极高的社区关注度（近5万星标），证明了其作为开源教育资源的广泛认可度和实用性。
*   标签涵盖了AI领域最主流的技术栈（ML/DL/CV/NLP），确保了学习内容的时效性和全面性。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48425 | 🍴 10043 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目致力于从Anthropic、OpenAI、Google及xAI等头部厂商的最新大模型（如Claude 5、GPT 5.5、Gemini 3.5等）中提取系统提示词。它提供了一个定期更新的资源库，收录了包括ChatGPT、Claude Code、Cursor在内的多种主流AI产品及代理的系统指令。

2. **核心功能**
*   **多厂商覆盖**：整合Anthropic、OpenAI、Google、xAI等多家科技巨头的最新模型系统提示词。
*   **前沿模型同步**：包含Claude Fable/Opus 5、GPT 5.5 Thinking/Instant、Gemini 3.5 Flash/Pro等最新一代模型的配置。
*   **工具与代理支持**：不仅涵盖聊天机器人，还收录了Claude Code、Cursor、VS Code Copilot及Perplexity等开发辅助工具的提示词。
*   **持续动态更新**：随着新模型和功能的发布，项目内容会定期更新以保持时效性。

3. **适用场景**
*   **提示词工程学习**：研究人员或开发者通过逆向分析顶级模型的系统指令，学习如何构建高效的提示词。
*   **AI应用开发调试**：开发者在构建基于LLM的应用时，参考官方系统提示词以优化模型行为和控制输出风格。
*   **安全与合规审计**：安全专家通过分析系统提示词，评估大模型在默认设置下的行为边界和安全策略。

4. **技术亮点**
*   **极高的社区关注度**：拥有超过4.5万星标，表明其在AI社区中具有广泛的影响力和参考价值。
*   **全栈式资源库**：罕见地将基础模型、代码助手、设计工具等多类AI产品的系统配置集中于一处，便于横向对比研究。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 45572 | 🍴 7484 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战及深度学习框架（PyTorch、TensorFlow 2）的综合学习资源库。内容还包括线性代数基础及自然语言处理工具（NLTK）的讲解与应用。旨在为学习者提供从理论到代码实现的完整机器学习与AI入门路径。

2. **核心功能**
*   集成多种经典机器学习算法（如SVM、K-Means、随机森林等）的代码实现。
*   提供深度神经网络（DNN）、循环神经网络（RNN/LSTM）等深度学习模型的实战案例。
*   包含自然语言处理（NLP）基础库NLTK的使用指南及相关算法实践。
*   涵盖推荐系统、关联规则挖掘（Apriori/FP-Growth）等特定领域的应用实例。
*   补充线性代数等数学基础，辅助理解机器学习背后的原理。

3. **适用场景**
*   机器学习初学者系统学习算法原理与代码实现。
*   需要快速查阅经典ML/DL算法Python实现方式的数据科学从业者。
*   希望深入理解NLP基础及深度学习框架（PyTorch/TF）应用的研究人员。
*   准备面试或提升实战能力的求职者，用于复习推荐系统和分类回归模型。

4. **技术亮点**
*   技术栈全面：同时覆盖传统机器学习（Scikit-learn）、深度学习（PyTorch/TF2）及NLP（NLTK）。
*   注重实战：不仅提供理论，更强调各类主流算法和框架的代码落地与实例演示。
*   社区认可度高：拥有超过4万星标，是广泛使用的开源机器学习学习指南。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11542 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36126 | 🍴 5913 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34822 | 🍴 7291 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33691 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28155 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25656 | 🍴 2877 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34822 | 🍴 7291 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 以下是针对 GitHub 项目 **Skyvern** 的详细技术分析：

1. **中文简介**
   Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流的开源平台。它通过结合计算机视觉与大语言模型（LLM），能够像人类一样理解和操作网页界面，从而实现端到端的任务自动化。该项目旨在降低 RPA（机器人流程自动化）的开发门槛，提供比传统脚本更灵活、更具适应性的解决方案。

2. **核心功能**
   *   **AI 驱动的页面理解**：利用计算机视觉和 LLM 识别网页元素，无需依赖固定的 CSS 选择器或 XPath。
   *   **自适应自动化**：能够应对网页布局变化、弹窗干扰及动态内容加载，具备类似人类的容错与重试能力。
   *   **自然语言工作流控制**：用户可通过自然语言指令定义任务逻辑，系统自动将其转化为具体的浏览器操作步骤。
   *   **多步任务编排**：支持复杂的跨页面导航、表单填写和数据提取，实现端到端的业务流程自动化。
   *   **可解释的执行过程**：记录每一步操作的决策依据和截图，便于调试、审计和优化自动化流程。

3. **适用场景**
   *   **企业级 RPA 替代方案**：用于自动化那些因前端频繁更新而难以用传统 Selenium/Playwright 脚本维护的后台管理系统操作。
   *   **数据爬取与信息整合**：从结构不固定或需要登录验证的网站中抓取非结构化数据，并整理为标准格式。
   *   **跨平台工作流集成**：在多个不同的 Web 应用之间自动执行重复性任务（如从 CRM 导出数据并填入 ERP 系统）。
   *   **QA 测试自动化**：模拟真实用户行为进行端到端的功能测试，尤其适用于 UI 变动频繁的敏捷开发环境。

4. **技术亮点**
   *   **Vision-Language Model (VLM) 融合**：创新性地结合视觉感知与大语言模型的语义理解能力，解决了传统自动化工具无法“看懂”页面的痛点。
   *   **无头/有头浏览器兼容**：基于 Playwright 构建，支持在无头模式下高效运行，同时保留对复杂交互的完整支持。
   *   **开源且可扩展**：作为 Python 库发布，开发者可轻松嵌入现有系统或自定义 AI 模型策略，社区活跃度高（近 2.2 万星标）。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 21994 | 🍴 2053 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，支持图像、视频及 3D 数据的标注。它提供开源、云端和企业级产品，具备 AI 辅助标注、质量保证及团队协作等功能。

2. **核心功能**
*   支持图像、视频和 3D 数据的多维度标注与 AI 辅助标记。
*   提供开源、云部署及企业版多种产品形态以满足不同需求。
*   内置质量保证机制与团队协作者，提升标注效率与准确性。
*   开放开发者 API 并集成数据分析工具，便于系统集成与监控。

3. **适用场景**
*   为计算机视觉模型训练准备大规模高质量标注数据集。
*   需要多团队协作进行复杂视频或 3D 物体检测的项目。
*   依赖 AI 辅助加速标注流程以提升数据处理效率的场景。

4. **技术亮点**
*   采用 Python 开发，原生兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   涵盖目标检测、语义分割、图像分类等多种前沿标注任务类型。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16130 | 🍴 3718 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12886 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11245 | 🍴 1190 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2193 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3451 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3250 | 🍴 397 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2617 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2412 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380230 | 🍴 79633 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一个经过验证的代理技能框架与软件开发方法论，旨在提升开发效率。它通过结构化的技能和子代理驱动的开发流程，优化从头脑风暴到代码实现的整个软件开发生命周期。该项目致力于解决复杂软件工程中的协作与自动化难题。

2. **核心功能**
*   提供一套可复用的“技能”模块，用于标准化常见开发任务。
*   采用子代理驱动开发模式，实现复杂任务的自动化分解与执行。
*   集成头脑风暴与设计阶段，辅助生成代码结构和逻辑。
*   涵盖完整的软件开发生命周期（SDLC），从规划到实施一体化支持。

3. **适用场景**
*   需要快速原型设计和自动化代码生成的敏捷开发团队。
*   希望利用AI代理辅助进行系统架构设计和技能拆解的中大型项目。
*   寻求标准化开发流程以提升团队协作效率和代码一致性的组织。

4. **技术亮点**
*   创新性地结合了“技能框架”与“代理驱动开发”，实现了方法论与工具的统一。
*   虽然主要描述为方法论框架，但基于 Shell 语言实现，具备轻量级和易集成的特点。
- 链接: https://github.com/obra/superpowers
- ⭐ 237392 | 🍴 21070 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一个能够随用户共同成长的人工智能助手。它旨在通过持续交互优化自身能力，提供个性化且日益智能的服务体验。该项目致力于打造一个理解用户意图并主动进化的智能代理系统。

2. **核心功能**
- 具备动态学习能力，能根据用户反馈和交互历史不断优化表现。
- 支持多模态任务处理，可协助代码编写、数据分析及创意生成等工作。
- 集成主流大语言模型接口，兼容 Anthropic、OpenAI 等底层模型。
- 提供模块化架构，允许开发者自定义插件和扩展特定功能领域。
- 拥有上下文记忆机制，能在长对话中保持连贯性和任务状态追踪。

3. **适用场景**
- 软件开发辅助：作为智能编程伴侣，实时协助代码审查与生成。
- 个人知识管理：帮助用户整理信息、总结文档并建立个性化知识库。
- 自动化工作流：执行重复性数据处理或跨平台任务以节省人力成本。
- 创意协作平台：在写作、设计构思等环节提供灵感激发与建议。

4. **技术亮点**
- 采用先进的提示工程与强化学习技术，实现更精准的意图识别。
- 高度可扩展的微服务架构，便于快速集成新的 AI 模型或服务。
- 注重隐私与安全设计，确保用户数据在处理过程中的可控性与保密性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 201498 | 🍴 35979 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### GitHub 项目分析：n8n

1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合的开发模式。它提供超过 400 种集成选项，允许用户选择本地自托管或云端部署，灵活满足各种自动化需求。

2. **核心功能**
*   提供可视化拖拽界面与自定义代码混合的工作流构建能力。
*   内置原生 AI 功能，支持智能辅助与自动化决策。
*   拥有超过 400 种预置集成，覆盖主流应用与 API 接口。
*   支持 MCP（模型上下文协议）客户端与服务端，增强 AI 工具连接性。
*   提供灵活的部署方案，既支持自托管也支持云托管。

3. **适用场景**
*   企业级数据同步与跨平台 API 集成自动化。
*   利用 AI 驱动的智能客服、内容生成或数据分析工作流。
*   开发者快速搭建低代码/无代码后端逻辑与微服务编排。
*   需要完全掌控数据隐私与服务器环境的自托管自动化解决方案。

4. **技术亮点**
*   采用 TypeScript 开发，类型安全且易于扩展。
*   开源公平代码（Fair-code）模式，兼顾社区贡献与企业商用灵活性。
*   率先集成 MCP 协议，无缝对接新兴的大语言模型工具生态。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 193864 | 🍴 58800 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 基于您提供的信息，以下是针对 GitHub 项目 **AutoGPT** 的技术分析：

1. **中文简介**
   AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上进行开发构建。该项目旨在提供必要的工具，使用户能够将精力集中在真正重要的任务上，而非繁琐的技术细节。

2. **核心功能**
   - 支持多种大型语言模型（如 GPT、Claude、Llama），提供灵活的底层引擎选择。
   - 具备自主代理（Autonomous Agents）能力，可独立规划并执行复杂的多步任务。
   - 提供开源的 AI 应用框架，方便开发者快速搭建和定制自己的 AI 智能体。
   - 强调易用性，降低构建 AI 应用的门槛，让非专家也能利用 AI 提升效率。

3. **适用场景**
   - **自动化工作流**：用于自动执行重复性高、步骤多的日常办公或数据处理任务。
   - **AI 应用开发原型**：作为开发者构建自定义 AI 智能体或聊天机器人的基础框架。
   - **研究与实验**：供研究人员探索自主代理行为、LLM 交互边界及多模型协作机制。

4. **技术亮点**
   - **多模型兼容架构**：不仅限于 OpenAI，还集成 Claude 和 Llama API，避免供应商锁定。
   - **高社区活跃度**：拥有超过 18.5 万星标，表明其在开源社区具有极高的影响力和广泛的用户基础。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185140 | 🍴 46125 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164237 | 🍴 21265 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163864 | 🍴 30363 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156574 | 🍴 46152 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150020 | 🍴 9328 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146414 | 🍴 23027 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

