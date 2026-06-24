# GitHub AI项目每日发现报告
日期: 2026-06-24

## 新发布的AI项目

### tupper
- 1. **中文简介**
Tupper 是一个开源的 AI 代理沙箱环境，旨在让用户在自己的机器上安全地运行不可信的 AI 生成代码。它通过隔离执行环境，确保在处理由大语言模型生成的潜在恶意或未知代码时保障系统安全。该项目为开发者提供了一种本地化、可控的代码执行解决方案。

2. **核心功能**
- 支持在本地机器上安全执行不可信的 AI 生成代码。
- 提供轻量级的沙箱隔离机制，防止代码对宿主系统造成危害。
- 兼容多种运行时环境（如 Bun、Node.js），便于集成不同类型的脚本。
- 作为 E2B 等云沙箱服务的替代方案，强调数据隐私和本地部署。
- 专为 AI 代理（AI Agents）设计，支持自动化代码解释与执行流程。

3. **适用场景**
- 开发需要动态执行用户输入代码的 AI 聊天机器人或智能助手应用。
- 在本地环境中测试和验证 LLM 生成的脚本，确保其安全性后再部署。
- 构建私有化的代码解释器服务，避免将敏感代码上传至第三方云服务。
- 用于 AI 代理框架（如 Mastra、DeepAgents）中的安全代码执行模块。

4. **技术亮点**
- 采用 TypeScript 开发，结合 Bun 运行时提供高性能的执行体验。
- 利用 Firecracker 微虚拟机技术实现轻量级、高安全的进程隔离。
- 明确标注为 E2B 替代品，满足对本地化部署和数据主权有严格要求的用户需求。
- 链接: https://github.com/lightbearco/tupper
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, apple-container, bun, code-execution, code-interpreter

### Hello-Agents
- **1. 中文简介**
该项目是一套从零开始构建 AI 智能体系统的全面且实用的教程，涵盖了从基础理论到生产级多智能体应用开发的完整流程。它旨在帮助开发者深入理解并掌握如何设计和实现复杂的 AI 代理系统。

**2. 核心功能**
*   提供从底层原理到高级应用的系统性教学路径。
*   指导构建生产级别的多人工智能协作系统。
*   结合 LangChain、LLM 和 RAG 等主流技术栈进行实战演练。
*   演示如何利用 OpenAI 等模型集成实现智能体功能。

**3. 适用场景**
*   希望深入理解 AI 智能体架构原理的学习者。
*   需要开发基于大语言模型的自动化工作流或代理系统的工程师。
*   正在探索多智能体协同解决复杂问题的研发团队。
*   希望将 RAG（检索增强生成）技术应用于智能体系统的开发者。

**4. 技术亮点**
*   **全链路覆盖**：不仅讲解概念，更侧重于从基础到生产环境的完整落地实践。
*   **多智能体协同**：重点展示多个 AI 代理如何协作处理复杂任务，这是当前 AI 应用的进阶热点。
*   **主流生态整合**：深度整合了 LangChain、RAG 和 LLM 等业界标准工具，具备较高的工程参考价值。
- 链接: https://github.com/Reyzowter/Hello-Agents
- ⭐ 121 | 🍴 3 | 语言: Python
- 标签: agent, ai, deep-learning, langchain, llm

### ESEILANE
- **1. 中文简介**
ESEILANE 是一款专为人工智能、大语言模型（LLM）及图检索增强生成（GraphRAG）设计的高性能知识图谱引擎。它旨在为下一代智能应用提供强大的底层支持，以处理复杂的结构化数据与推理任务。

**2. 核心功能**
*   提供高性能的知识图谱存储与查询能力，支持大规模数据处理。
*   原生集成 GraphRAG 架构，优化大语言模型对图谱信息的检索与利用。
*   兼容 OpenCypher 查询语言，降低开发者接入和使用的门槛。
*   采用多语言混合开发（Rust/Python/TypeScript），兼顾执行效率与生态兼容性。
*   支持复杂的图算法计算，通过 GraphBLAS 标准提升数学运算性能。

**3. 适用场景**
*   构建基于 RAG 的智能问答系统，利用图谱提升回答的准确性与可解释性。
*   开发需要复杂关系推理的企业级 AI 应用，如欺诈检测或推荐系统。
*   作为 LLM 的后端知识底座，解决大模型幻觉问题并增强事实一致性。
*   进行大规模图数据的实时分析与可视化展示。

**4. 技术亮点**
*   **高性能内核**：利用 Rust 编写核心组件并结合 GraphBLAS 标准，确保极致的计算速度。
*   **多语言友好**：同时提供 Python、TypeScript 等接口，便于不同技术栈的开发者集成。
*   **标准化支持**：全面支持 OpenCypher 标准，无缝对接主流图数据库生态。
- 链接: https://github.com/Simpl3x3/ESEILANE
- ⭐ 105 | 🍴 3 | 语言: Ruby
- 标签: ai, graph-database, graphblas, graphrag, knowledge-graph

### awesome-evals
- ### 1. 中文简介
awesome-evals 是由 BenchFlow 维护的一份精心策划的资源库，旨在为构建和评估 AI 智能体提供非冗余的高质量参考资料。该列表汇集了相关的学术论文、博客文章、演讲视频、工具以及基准测试数据集。它专注于帮助开发者系统化地掌握大语言模型智能体的评估方法。

### 2. 核心功能
*   提供全面的 AI 智能体评估资源集合，涵盖从理论到实践的多维度内容。
*   整合了最新的学术论文、技术博客及行业会议演讲，确保信息的时效性。
*   收录了实用的评估工具和标准化基准测试，辅助量化模型性能。
*   由 BenchFlow 团队持续维护，筛选掉低质内容，保证资源的专业性和可靠性。

### 3. 适用场景
*   **AI 研究员**：快速检索智能体评估领域的最新学术进展和经典论文。
*   **算法工程师**：寻找合适的基准测试和数据集以验证自家智能体的性能指标。
*   **技术决策者**：通过阅读高质量的博客和演讲，了解行业最佳实践和工具链现状。
*   **开源贡献者**：基于现有资源库补充或优化特定的评估工具和方法论。

### 4. 技术亮点
该项目本身是一个“Awesome List”（精选资源列表），其核心价值在于对海量碎片化信息进行了结构化整理和质量过滤，特别聚焦于 Agent Evaluation 这一细分领域，为用户节省了从零搜集和甄别资料的时间成本。
- 链接: https://github.com/benchflow-ai/awesome-evals
- ⭐ 87 | 🍴 2 | 语言: 未知
- 标签: agent-evaluation, ai-agents, awesome, awesome-list, benchmarks

### lemma-platform
- **1. 中文简介**
Lemma Platform 是一个开源的工作空间，旨在让人类与 AI 代理无缝协作，共同组成一个高效团队。它通过整合人机能力，优化工作流程，提升整体生产力。该项目致力于构建一个人机协同的智能工作环境。

**2. 核心功能**
*   提供人类与 AI 代理统一协作的集成工作空间。
*   支持将 AI 代理作为团队成员融入现有工作流。
*   具备 AI 辅助的自动化任务处理能力。
*   强调人机混合团队的协同效率与一致性。

**3. 适用场景**
*   需要 AI 助手协助处理复杂文档或代码编写的全栈开发团队。
*   希望利用 AI 代理自动化日常重复性任务的运营或数据团队。
*   探索人机协同新模式，以提升创意生成或决策效率的企业研发部门。

**4. 技术亮点**
*   采用 Python 开发，便于集成和扩展。
*   基于“harness”架构，提供标准化的 AI 代理运行环境。
*   专注于降低人机协作的技术门槛，实现平滑交互。
- 链接: https://github.com/lemma-work/lemma-platform
- ⭐ 66 | 🍴 14 | 语言: Python
- 标签: ai, harness, harness-ai

### fastloops
- 描述: Fast and one click setup with AI loops — run, check, fix, repeat until done.
- 链接: https://github.com/Her-shey/fastloops
- ⭐ 33 | 🍴 0 | 语言: Python

### gensee-crate
- 描述: Local-first runtime safety for AI coding agents
- 链接: https://github.com/GenseeAI/gensee-crate
- ⭐ 31 | 🍴 0 | 语言: Rust

### ai-short-drama-agent-company
- 描述: Complete Matrix department template pack for running an AI short-drama production company. Includes 5 skills, 3 departments with memory, and Empire of Dust demo (700k+ YouTube views). Bilingual README.
- 链接: https://github.com/1229119561Weike/ai-short-drama-agent-company
- ⭐ 25 | 🍴 7 | 语言: Python

### claude-mythos-ai-anthropic-desktop-app
- 描述: claude mythos ai anthropic free large language model llm frontier model project glasswing cybersecurity agent vulnerability research software engineering agentic workflows multi step reasoning recurrent depth transformer rdt openmythos repository open source claude fable 5 multi agent
- 链接: https://github.com/ikarma/claude-mythos-ai-anthropic-desktop-app
- ⭐ 25 | 🍴 0 | 语言: TypeScript
- 标签: claude-chat, claude-code-, claude-code-action, claude-code-prompts, claude-code-routine

### ritual-chain-workshop
- 描述: Building and deploying an on-chain AI bounty judge on Ritual - 23.06.2026
- 链接: https://github.com/cozfuttu/ritual-chain-workshop
- ⭐ 21 | 🍴 61 | 语言: TypeScript

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面的中英文自然语言处理（NLP）工具集和资源库，涵盖了从基础文本处理到高级语义分析的多种功能。它整合了大量专业词库、预训练模型、数据集及实用算法，旨在为开发者提供一站式 NLP 解决方案。该项目特别适合需要快速集成中文 NLP 能力或进行相关数据研究的技术人员。

**2. 核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、语言检测、繁简转换、停用词处理及文本纠错等功能。
*   **信息抽取与识别**：支持手机号、身份证、邮箱等实体抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
*   **丰富词库与资源**：内置中日文人名库、职业/汽车/医疗等领域专用词库、成语/古诗词库及大量多语言词向量。
*   **语音与对话系统**：包含 ASR 语音识别数据、中文聊天机器人（如 SeqGAN、GPT-2 微调）、对联生成及多轮对话系统资源。
*   **知识图谱与问答**：提供中文知识图谱构建工具、基于图谱的问答系统（KBQA）、百科知识抽取及实体链接库。

**3. 适用场景**
*   **内容安全审核**：利用敏感词库和情感分析工具，快速构建互联网内容的合规性检测系统。
*   **智能客服与聊天机器人开发**：借助其中的对话语料、预训练模型及开源对话框架，快速搭建具备上下文理解能力的智能助手。
*   **垂直领域知识抽取**：在医疗、金融或法律领域，利用专用词库和 NER 模型从非结构化文本中提取关键实体和关系。
*   **NLP 教学与研究**：作为学习中文 NLP 的入门资源库，获取标准化的数据集、基准模型代码及行业分析报告。

**4. 技术亮点**
*   **资源聚合度高**：不仅包含代码工具，还汇集了清华大学 XLORE、百度、阿里等机构的高质量数据集和预训练模型（如 BERT、ALBERT、ELECTRA）。
*   **全栈式覆盖**：从底层的分词、OCR、语音识别，到上层的语义理解、知识图谱构建和应用层对话系统，覆盖了 NLP 全链路。
*   **实用性强**：提供了大量开箱即用的 Python 库（如 jieba_fast, cnocr, HarvestText）和特定场景工具（如简历解析、表格提取），极大降低了开发门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81424 | 🍴 15245 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34832 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构。该工具通过图形化界面展示模型层之间的连接与数据流向，极大提升了模型分析的便捷性。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、PyTorch、TensorFlow、Keras、CoreML 等。
*   提供直观的图形化界面，清晰展示神经网络的层级结构和节点连接关系。
*   允许用户浏览和检查模型内部的权重参数及配置信息。
*   具备导出模型结构为图片或 PDF 的功能，便于文档记录和分享。
*   支持在浏览器中直接打开模型文件，无需安装复杂的本地环境。

3. **适用场景**
*   **模型调试与验证**：在部署前检查模型结构是否符合预期，排查层连接错误。
*   **学术交流与报告**：生成高质量的模型架构图，用于论文撰写或技术演示文档。
*   **跨平台模型转换检查**：验证从一种框架（如 PyTorch）转换到另一种框架（如 ONNX）后的结构一致性。
*   **快速学习新模型**：通过可视化界面快速理解复杂深度学习模型的整体架构和数据流。

4. **技术亮点**
*   **极高的兼容性**：通过统一接口支持数十种不同的模型格式和框架，是业界标准的轻量级可视化工具。
*   **零依赖运行**：基于 JavaScript 构建，既可作为桌面应用独立运行，也可嵌入 Web 服务，无需安装庞大的机器学习库即可解析模型。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33124 | 🍴 3137 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换与共享。它允许开发者在不同平台（如PyTorch、TensorFlow等）之间无缝迁移模型，从而简化部署流程并提升开发效率。

### 2. 核心功能
- **跨框架兼容**：支持在PyTorch、TensorFlow、Keras和Scikit-learn等多种主流机器学习框架间进行模型转换。
- **统一中间表示**：提供标准化的中间层格式，确保模型结构和参数在不同环境中的无损传递。
- **部署灵活性**：允许将训练好的模型转换为高效格式，以便在各种硬件加速器和推理引擎上运行。
- **生态系统整合**：与众多AI工具链集成，简化从研究到生产环境的整个工作流。

### 3. 适用场景
- **模型迁移**：当需要从一种框架（如PyTorch）切换到另一种框架或部署平台时。
- **生产环境部署**：将经过训练的深度学习模型转换为适合高性能推理优化的格式。
- **跨平台协作**：团队成员使用不同的开发工具，但需要共享和复用相同的模型资产。

### 4. 技术亮点
- **开源标准化**：由微软、Facebook等巨头共同推动，已成为行业事实上的通用交换标准。
- **高性能优化**：通过ONNX Runtime等配套工具，实现模型在CPU、GPU及其他硬件上的极速推理。
- 链接: https://github.com/onnx/onnx
- ⭐ 21039 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 以下是关于 GitHub 项目 `ml-engineering` 的技术分析报告：

1. **中文简介**
   该项目是一部开源的机器学习工程“圣经”，全面涵盖了从模型训练、调试到部署推理的全生命周期最佳实践。它深入探讨了 GPU 加速、大规模分布式训练、存储优化及网络通信等底层工程技术。旨在为构建可扩展、高效且稳定的机器学习系统提供权威参考。

2. **核心功能**
   - **全栈工程指导**：覆盖数据预处理、模型训练、超参数调优至生产环境部署的完整流水线。
   - **大规模训练优化**：详解 PyTorch 分布式训练策略（如 DDP、FSDP）、混合精度训练及 Slurm 集群管理。
   - **硬件与基础设施**：深入解析 GPU 架构特性、高速网络互联（InfiniBand/RoCE）及高性能存储解决方案。
   - **推理与服务化**：提供大语言模型（LLM）的高效推理框架、量化技术及负载均衡策略。
   - **可观测性与调试**：包含针对 ML 系统的性能剖析、错误排查及监控指标的最佳实践。

3. **适用场景**
   - **大型语言模型（LLM）研发**：适用于需要进行千卡/万卡级别预训练或微调的团队，解决扩展性瓶颈。
   - **MLOps 平台搭建**：帮助工程团队设计高可用、自动化的机器学习基础设施和 CI/CD 流程。
   - **GPU 资源密集计算**：适用于需要极致优化 GPU 利用率、降低训练成本和时间的科研或工业场景。
   - **高性能推理部署**：用于优化在线服务中的模型响应速度、吞吐量及资源利用率。

4. **技术亮点**
   - **深度结合 PyTorch 生态**：不仅介绍概念，更提供基于主流框架的具体代码实现和配置示例。
   - **关注“隐形”工程细节**：特别强调网络带宽、存储 I/O 和 GPU 显存管理等常被忽视但对性能影响巨大的环节。
   - **实战导向**：内容源自工业界真实挑战，而非纯理论推导，直接解决大规模 ML 系统中的工程痛点。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18167 | 🍴 1152 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17250 | 🍴 2108 | 语言: 未知
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
- ⭐ 11522 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10638 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个收录了500个AI项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并附带完整代码实现。该项目旨在为开发者提供从基础到高级的实战案例参考，帮助快速掌握各类AI技术的应用与落地。

### 2. 核心功能
- **海量项目资源**：精心筛选并分类整理了500个高质量的AI相关开源项目。
- **全栈代码支持**：所有列出的项目均包含可直接运行的源代码，便于学习者复现和实践。
- **多领域覆盖**：全面覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心技术分支。
- **结构化索引**：通过清晰的标签和分类体系，帮助用户快速定位特定技术领域的优质项目。

### 3. 适用场景
- **初学者入门学习**：适合希望系统了解AI各细分领域的项目结构与实践流程的新手。
- **开发者技术选型**：帮助工程师在开发过程中快速寻找成熟、可复用的算法库或解决方案。
- **学术研究参考**：为研究人员提供大量最新的实战案例，辅助理解理论模型的实际应用效果。

### 4. 技术亮点
- **高关注度与权威性**：拥有超过3.4万星标，是GitHub上最受关注的AI资源集合之一，证明了其内容的广泛认可度和高质量。
- **一站式学习平台**：将分散的优质项目集中管理，极大地降低了开发者搜索和评估现有解决方案的时间成本。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34832 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持查看多种主流框架生成的模型结构，帮助用户直观理解模型架构与数据流向。

2. **核心功能**
*   支持广泛格式的模型可视化，包括 ONNX、PyTorch、TensorFlow、Keras 等。
*   提供清晰的层结构树状视图，展示模型中的节点及其连接关系。
*   兼容移动端和桌面端运行，方便在不同环境下进行模型审查。
*   支持多种模型存储格式，如 CoreML、TensorFlow Lite 和 Safetensors。

3. **适用场景**
*   深度学习研究人员用于调试和优化模型架构。
*   工程师在部署模型前检查模型兼容性与参数配置。
*   教育场景中向学生直观展示神经网络的工作原理。

4. **技术亮点**
*   基于 JavaScript 开发，无需安装复杂依赖即可通过浏览器或桌面应用直接使用。
*   轻量级且跨平台，能够无缝集成到各种开发工作流中。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33124 | 🍴 3137 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心知识速查表。它整合了从基础概念到高级框架的关键要点，旨在帮助研究者快速回顾和掌握技术细节。通过集中展示重要公式、代码片段及理论摘要，极大提升了学习效率和查阅便利性。

### 2. **核心功能**
*   提供深度学习与机器学习领域的关键概念速查，便于快速记忆与复习。
*   涵盖主流框架（如Keras）及核心库（如NumPy、SciPy、Matplotlib）的使用技巧。
*   总结算法原理、数学公式及最佳实践，适合研究者作为日常参考工具。
*   以结构化文档形式呈现复杂技术内容，降低理解门槛并提高检索效率。

### 3. **适用场景**
*   深度学习研究者在准备论文或实验前，快速回顾特定算法或公式的细节。
*   数据科学家在日常编码过程中，查阅NumPy、SciPy等库的高效用法及示例。
*   机器学习初学者系统梳理知识体系，利用速查表巩固基础理论与框架操作。
*   团队内部技术分享或面试准备时，作为标准化知识点的参考资料。

### 4. **技术亮点**
*   集成多种核心技术栈（Keras、NumPy、Scipy、Matplotlib），实现一站式知识汇总。
*   针对AI研究人员痛点优化，内容精炼且聚焦于高频使用的核心知识点。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13085 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 以下是针对 GitHub 项目 **Ludwig** 的技术分析：

1. **中文简介**
   Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置方式，让开发者无需编写复杂的底层代码即可快速训练和部署机器学习模型。

2. **核心功能**
   *   提供声明式 API，用户仅需定义数据模式即可自动处理特征工程与模型架构。
   *   内置多种预定义模型组件，支持表格数据、文本、图像及音频等多种数据类型。
   *   支持主流深度学习后端（如 PyTorch），并兼容 Hugging Face Transformers 以集成最新的大语言模型。
   *   具备完整的模型生命周期管理，涵盖从数据探索、训练、评估到最终部署的全流程。
   *   强调以数据为中心的开发理念，简化了数据处理和模型微调的操作复杂度。

3. **适用场景**
   *   **快速原型开发**：需要在短时间内验证机器学习想法或构建基础模型的场景。
   *   **多模态应用构建**：需要同时处理结构化表格数据与非结构化数据（如文本、图像）的综合型 AI 应用。
   *   **大模型微调**：希望基于现有开源 LLM（如 Llama、Mistral）进行领域特定微调，但缺乏大规模底层框架开发经验的团队。
   *   **数据科学工作流标准化**：企业希望统一机器学习实验的可复现性和部署标准，减少代码冗余。

4. **技术亮点**
   *   **低代码/无代码特性**：极大降低了构建复杂神经网络的门槛，使非深度学习专家也能高效工作。
   *   **以数据为中心的设计**：专注于数据模式定义而非网络结构细节，提高了模型开发的迭代速度。
   *   **广泛的生态兼容性**：无缝集成 PyTorch 和 Hugging Face 生态，既保留了灵活性又提供了开箱即用的便利。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11723 | 🍴 1221 | 语言: Python
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
- ⭐ 6170 | 🍴 721 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81424 | 🍴 15245 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72455 | 🍴 8862 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
该项目是一个为期12周、包含24节课的开源人工智能教育课程，旨在让所有人轻松入门AI领域。它基于Jupyter Notebook构建，内容涵盖从机器学习基础到深度学习的高级主题，由微软发起并维护。

### 2. 核心功能
*   **系统化课程结构**：提供清晰的12周学习路径和24节精心设计的课程，适合循序渐进的学习者。
*   **交互式代码环境**：主要使用Jupyter Notebook，允许用户边学边练，即时运行和修改代码。
*   **全面的技术覆盖**：内容囊括机器学习、深度学习、计算机视觉（CNN）、自然语言处理（RNN/NLP）及生成对抗网络（GAN）等核心领域。
*   **零基础友好设计**：强调“AI for All”，降低门槛，适合没有深厚数学或编程背景的初学者上手。

### 3. 适用场景
*   **大学生或转行者自学**：希望系统掌握AI基础知识并构建作品集的非专业人士。
*   **课堂教学辅助**：教师用于计算机科学或数据科学课程的补充教材和实践练习。
*   **企业内训入门**：科技公司为员工提供的人工智能概念普及和技术基础培训。

### 4. 技术亮点
*   **微软背书与社区支持**：由Microsoft For Beginners计划支持，拥有高活跃度社区和大量Star，确保内容的质量和持续更新。
*   **多模态AI实践**：不仅限于文本，还深入涵盖图像（计算机视觉）和序列数据（NLP）的处理，提供全面的AI视角。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48429 | 🍴 10044 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个持续更新的资源库，收集并提取了包括 Anthropic、OpenAI、Google、xAI 等在内的多个主流大语言模型（如 Claude、ChatGPT、Gemini、Grok 等）的系统提示词（System Prompts）。它涵盖了从基础聊天机器人到代码辅助工具（如 Cursor、VS Code）等多种 AI 产品的底层指令配置。

### 2. 核心功能
- **多模型提示词收录**：整合了 Claude、GPT、Gemini 等多个头部 AI 模型的官方系统提示词。
- **定期自动更新**：随着模型迭代，持续同步最新的系统指令和配置信息。
- **开源共享社区**：以 JavaScript 编写并提供开源代码，方便开发者查阅和研究。
- **AI 代理与工具覆盖**：不仅包含基础 LLM，还涉及 Claude Code、Cursor、Copilot 等 AI 编程助手的具体配置。

### 3. 适用场景
- **提示词工程研究**：开发者通过分析官方提示词结构，优化自身应用的 Prompt 设计策略。
- **大模型安全与红队测试**：研究人员利用已知提示词进行对抗性测试，探索模型的安全边界和漏洞。
- **AI 产品逆向学习**：初学者或从业者通过对比不同厂商的指令风格，理解各自模型的行为逻辑。
- **构建自定义 AI Agent**：参考成熟产品的系统设定，为自建聊天机器人或代码助手定制更高效的系统指令。

### 4. 技术亮点
- **高关注度与社区影响力**：拥有超过 4.5 万星，表明其在 AI 社区中具有极高的关注度和参考价值。
- **跨平台全面性**：罕见地同时覆盖了竞争激烈的多家科技巨头（Anthropic, OpenAI, Google, xAI）的核心资产。
- **实用性强**：直接提供可操作的提示词文本，而非单纯的理论分析，便于直接集成或测试使用。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 45643 | 🍴 7493 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42347 | 🍴 11542 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36154 | 🍴 5923 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34832 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33694 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28160 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25679 | 🍴 2878 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. **中文简介**
该项目是一个精选的 AI 项目合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等热门领域，并提供完整的代码实现。它旨在为开发者提供一个全面的学习资源库，通过实际案例展示如何构建和运行各类人工智能应用。

### 2. **核心功能**
*   **多领域覆盖**：包含机器学习、深度学习、计算机视觉和 NLP 等多个子领域的实战项目。
*   **代码导向**：所有项目均附带可运行的源代码，便于用户直接复现和学习。
*   **项目分类清晰**：通过标签对不同类型的 AI 项目进行系统化整理，方便检索。
*   **社区精选**：作为“Awesome”系列列表的一部分，汇聚了高质量且受社区认可的项目。

### 3. **适用场景**
*   **初学者入门**：适合想快速了解 AI 各分支实际应用的新手，通过跑通代码建立直观认识。
*   **技术选型参考**：帮助工程师在特定任务（如图像识别或文本生成）中寻找成熟的开源解决方案。
*   **面试准备**：求职者可通过这些项目梳理知识体系，并在面试中展示实际动手能力和项目经验。

### 4. **技术亮点**
*   **极高的社区关注度**：拥有超过 34,000 个星标，证明了其内容的广泛认可度和实用性。
*   **一站式学习资源**：无需分散搜索，即可在一个仓库内找到从基础到进阶的各类 AI 项目示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34832 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一个基于人工智能驱动的浏览器自动化工具，旨在通过视觉理解和智能代理技术，自动执行复杂的网页工作流。它支持多种主流自动化框架，能够以类似人类操作的方式与网页进行交互，从而提升工作效率并减少手动配置成本。

### 2. 核心功能
*   **AI 驱动的网页交互**：利用大语言模型（LLM）和计算机视觉技术，理解页面布局并执行点击、输入等操作，无需依赖固定的 CSS 选择器或 XPath。
*   **多框架兼容与支持**：底层集成 Playwright、Puppeteer 等现代浏览器自动化工具，提供灵活且高性能的执行环境。
*   **工作流自动化编排**：支持定义复杂的多步骤业务流程，自动处理导航、数据提取和异常重试，实现端到端的 RPA（机器人流程自动化）。
*   **视觉感知能力**：具备“看见”屏幕内容的能力，能够识别动态加载的元素、验证码和弹窗，适应不断变化的网页结构。
*   **API 化集成**：提供易于集成的 API 接口，方便开发者将其嵌入到现有的业务系统或 CI/CD 流程中。

### 3. 适用场景
*   **企业级 RPA 替代方案**：用于自动化传统的桌面或 Web 端重复性任务，如表单填写、数据录入和报表生成，替代 Selenium 等需要大量维护的传统脚本。
*   **动态网页数据抓取**：针对 JavaScript 渲染频繁变化或结构不稳定的网站，进行可靠的数据采集和信息监控。
*   **跨平台测试与验收**：在开发测试阶段，模拟真实用户行为进行端到端的 UI 自动化测试，提高测试用例的鲁棒性。
*   **第三方系统集成**：自动化操作那些没有开放 API 接口的老旧系统或第三方 SaaS 平台，实现数据互通和业务协同。

### 4. 技术亮点
*   **结合 LLM 与 Computer Vision**：突破了传统自动化脚本对页面结构强依赖的局限，通过“看”懂页面来做出决策，极大地降低了维护成本。
*   **自适应性强**：能够自动适应网页 UI 的微小变化（如按钮位置移动、文案变更），显著提高了自动化流程的长期稳定性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 21996 | 🍴 2053 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### GitHub项目分析：CVAT (Computer Vision Annotation Tool)

#### 1. 中文简介
CVAT 是构建高质量视觉数据集以用于视觉 AI 开发的领先平台，提供开源、云版及企业级产品。它支持图像、视频和 3D 数据的标注，具备 AI 辅助标注、质量保证、团队协作及开发者 API 等强大功能。

#### 2. 核心功能
*   **多模态数据标注**：全面支持图像分类、目标检测、语义分割以及视频和 3D 点云标注。
*   **AI 辅助与自动化**：集成智能标注工具，可加速数据预处理并提高标注效率与准确性。
*   **协作与工作流管理**：提供团队分工、任务分配、质量控制（QA）及进度分析功能。
*   **灵活的部署模式**：支持本地开源部署、公有云版本以及面向大型企业的私有化解决方案。
*   **开发者友好接口**：提供完善的 REST API，便于集成到现有的机器学习流水线中。

#### 3. 适用场景
*   **计算机视觉模型训练**：为图像分类、物体检测或语义分割任务准备标准化的高质量训练数据集。
*   **自动驾驶与机器人感知**：对复杂视频流和 3D 传感器数据进行精细化标注，以训练环境感知算法。
*   **工业质检与安防监控**：批量处理视频或图像数据，识别缺陷或特定行为模式。
*   **学术研究与企业内训**：研究人员或团队利用其协作功能共同完成大规模数据集的标注工作。

#### 4. 技术亮点
*   **开源生态强大**：拥有超过 1.6 万颗星的高人气社区支持，广泛兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   **全栈式标注能力**：从简单的边界框（Bounding Box）到复杂的像素级分割（Segmentation），覆盖 CV 领域绝大多数标注需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16132 | 🍴 3718 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### GitHub项目分析：pytorch-grad-cam

#### 1. 中文简介
该项目专为计算机视觉领域提供高级AI可解释性功能，支持包括卷积神经网络（CNN）、Vision Transformers在内的多种架构。它广泛适用于分类、目标检测、图像分割及图像相似度计算等任务，旨在通过可视化手段揭示模型的决策依据。

#### 2. 核心功能
*   支持多种主流视觉模型架构，包括CNN和Vision Transformers。
*   实现多种可解释性算法，如Grad-CAM、Score-CAM及类激活映射。
*   覆盖多重视觉任务，涵盖图像分类、目标检测、语义分割及图像相似度分析。
*   提供直观的可视化输出，帮助用户理解深度学习模型的内部决策过程。
*   基于PyTorch框架构建，便于集成到现有的深度学习工作流中。

#### 3. 适用场景
*   **模型调试与优化**：研究人员利用热力图定位模型关注区域，以发现特征提取错误或优化模型结构。
*   **医疗影像诊断辅助**：医生通过可视化结果验证AI对病灶区域的识别准确性，增强临床信任度。
*   **自动驾驶安全审计**：开发者分析车辆感知系统在目标检测中的注意力分布，确保关键障碍物被正确识别。
*   **AI伦理与合规审查**：企业通过展示模型决策依据，满足监管要求并消除算法黑箱带来的偏见疑虑。

#### 4. 技术亮点
*   兼容性强：无缝支持从传统CNN到最新的Vision Transformer架构。
*   算法丰富：内置Grad-CAM及其改进版本（如Score-CAM），提供多样化的可解释性方案。
*   社区活跃：拥有超过12,000星的高人气，表明其在学术界和工业界的广泛应用与成熟度。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12886 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建，旨在通过可微分操作简化传统视觉算法的开发。它提供了丰富的图像处理和几何变换工具，使开发者能够轻松地将经典 CV 技术集成到深度学习流水线中。该项目致力于提升代码的可重用性，并促进计算机视觉与深度学习的深度融合。

**2. 核心功能**
*   提供大量可微分的几何计算机视觉算子，支持端到端的深度学习训练。
*   内置丰富的图像处理模块，包括色彩空间转换、滤波、形态学操作及图像增强。
*   支持复杂的相机模型和投影变换，便于进行三维重建和位姿估计。
*   与 PyTorch 生态无缝集成，允许直接使用 GPU 加速计算并自动求导。
*   包含用于机器人学和空间 AI 的实用工具，如点云处理和特征匹配。

**3. 适用场景**
*   **可微分计算机视觉研究**：需要将传统几何约束嵌入神经网络进行联合优化的学术或工业研究。
*   **机器人导航与感知**：开发依赖实时图像处理、SLAM（同步定位与建图）或物体检测的机器人系统。
*   **图像预处理流水线**：在深度学习任务前执行标准化、归一化或增强等高效且可微的图像预处理步骤。
*   **混合架构开发**：构建同时利用深度学习特征提取能力和传统几何精确性的混合视觉应用。

**4. 技术亮点**
*   **完全可微分设计**：所有核心操作均支持梯度回传，完美契合现代深度学习框架。
*   **高性能 CUDA 加速**：底层实现针对 GPU 进行了高度优化，显著提升大规模数据处理速度。
*   **模块化与扩展性**：采用清晰的模块化结构，便于用户自定义算子或扩展特定领域的视觉功能。
- 链接: https://github.com/kornia/kornia
- ⭐ 11246 | 🍴 1190 | 语言: Python
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
- **1. 中文简介**
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台运行，强调数据的完全私有化与自主掌控。它采用独特的“龙虾”风格设计，致力于为用户提供安全、灵活的本地化人工智能体验。

**2. 核心功能**
*   全平台兼容性，可在任何操作系统上部署运行。
*   强调数据主权，确保用户拥有并控制自己的数据。
*   提供个性化的 AI 助手服务，满足多样化需求。
*   基于 TypeScript 开发，具备良好的可扩展性和维护性。
*   采用独特的品牌标识（龙虾/甲壳类动物主题）增强辨识度。

**3. 适用场景**
*   注重隐私保护、希望数据不出本地的个人用户。
*   需要在不同操作系统间无缝切换的开发者和极客。
*   寻求定制化、自主可控 AI 解决方案的个人或小团队。
*   对数据安全有极高要求、不愿依赖第三方云服务的用户。

**4. 技术亮点**
*   使用 TypeScript 构建，保证代码类型安全和现代开发体验。
*   高度模块化设计，便于集成和自定义功能。
*   轻量级架构，适应多种运行环境，资源占用可控。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380264 | 🍴 79648 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. 中文简介
Superpowers 是一个经过验证的代理技能框架及软件开发方法论，旨在提升开发效率。它通过结构化的“技能”定义和子代理驱动的开发模式，规范了从头脑风暴到代码实现的完整软件开发生命周期（SDLC）。该项目致力于解决传统AI辅助编程中缺乏系统性和一致性的问题。

### 2. 核心功能
*   **代理技能框架**：提供标准化的技能定义与执行机制，使AI代理能够像专业开发人员一样协作。
*   **子代理驱动开发**：采用多智能体架构，通过专门的子代理处理编码、测试和调试等具体任务。
*   **结构化SDLC支持**：涵盖从需求分析、头脑风暴到最终交付的完整软件开发生命周期管理。
*   **可复用的技能库**：允许用户构建和共享通用的开发技能，促进知识沉淀和重复利用。
*   **自动化工作流整合**：将AI能力深度集成到现有的开发流程中，减少人工干预并提高准确性。

### 3. 适用场景
*   **复杂系统架构设计**：需要多维度思考和技术栈选型的软件工程团队。
*   **自动化代码生成与重构**：希望利用AI批量生成高质量代码或优化现有代码库的场景。
*   **AI辅助的研发流程标准化**：寻求建立统一、可追踪的AI驱动开发规范的中型至大型企业。
*   **快速原型开发**：需要在短时间内完成从创意构思到最小可行产品（MVP）搭建的团队。

### 4. 技术亮点
*   **方法论创新**：不仅提供工具，更提出了一套完整的“代理驱动开发”理论体系。
*   **高度模块化**：基于Shell脚本实现，便于与其他CI/CD管道和开发工具链无缝集成。
*   **社区验证**：拥有极高的星标数（23万+），表明其在开发者社区中具有广泛的影响力和认可度。
- 链接: https://github.com/obra/superpowers
- ⭐ 237592 | 🍴 21080 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款随用户共同成长的智能代理工具。它旨在通过持续学习和适应，成为开发者日常工作中得力的辅助伙伴。该项目致力于提供高度灵活且可扩展的 AI 自动化解决方案。

2. **核心功能**
*   支持多模型集成，兼容 Anthropic、OpenAI 等主流大语言模型。
*   具备自我进化能力，能根据交互反馈不断优化工作流。
*   提供丰富的代码生成与编辑功能，深度集成开发环境。
*   拥有模块化架构，允许用户自定义插件和扩展功能。

3. **适用场景**
*   复杂项目的自动化代码重构与技术债清理。
*   作为个人开发者的智能结对编程助手。
*   需要跨平台 API 调用和数据处理的任务自动化。

4. **技术亮点**
*   采用模块化设计，轻松适配不同 LLM 后端。
*   强调“成长型”架构，通过历史交互数据优化决策逻辑。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 201749 | 🍴 36039 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码结合。它提供超过 400 种集成方式，允许用户选择自托管或云端部署，实现高效的数据流管理。

2. **核心功能**
*   提供可视化拖拽界面，结合自定义代码实现灵活的工作流设计。
*   内置原生 AI 能力，支持智能处理复杂的业务逻辑和数据任务。
*   拥有超过 400 种预置集成连接器，轻松对接各类 API 和外部服务。
*   采用公平代码（Fair-code）许可，既支持自托管也兼容云端部署，保障数据隐私与控制权。
*   作为 iPaaS 低代码平台，简化了系统集成与自动化流程的开发门槛。

3. **适用场景**
*   **企业系统集成**：连接 CRM、ERP 等不同系统，自动同步数据并触发后续业务流程。
*   **AI 驱动的数据处理**：利用内置 AI 能力对非结构化数据进行清洗、分类或生成摘要。
*   **自动化营销与工作流**：自动执行邮件发送、社交媒体更新或客户跟进等重复性运营任务。

4. **技术亮点**
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，便于与大型语言模型深度交互。
*   **混合开发模式**：完美融合低代码可视化的便捷性与 TypeScript 自定义代码的灵活性。
*   **TypeScript 生态**：基于 TypeScript 构建，确保类型安全和良好的开发者体验及扩展性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 193890 | 🍴 58802 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于让每个人都能轻松获取、使用并构建基于 AI 的工具，其愿景是普及化的人工智能。通过提供强大的自动化框架，它帮助用户将精力集中在真正重要的事情上，而非繁琐的技术实现细节。

### 2. 核心功能
*   **自主智能体驱动**：基于大型语言模型（LLM）构建自主代理，能够独立规划并执行复杂的多步任务。
*   **多模型兼容支持**：广泛支持 OpenAI GPT、Claude、Llama 等主流大模型 API，提供灵活的底层接入能力。
*   **互联网与工具集成**：具备联网搜索、文件读写及调用外部工具的能力，实现从信息获取到行动执行的闭环。
*   **高度可定制性**：采用 Python 开发且代码开源，开发者可根据需求自由扩展功能模块或调整代理行为逻辑。

### 3. 适用场景
*   **自动化内容创作与工作流**：自动完成市场调研、文章撰写、数据整理等重复性高且流程固定的办公任务。
*   **复杂问题求解与研究**：作为研究助手，自动搜集分散的网络信息并进行综合分析与总结。
*   **个性化 AI 应用开发**：为开发者提供构建定制化自主 AI Agent 的基础框架和参考实现。

### 4. 技术亮点
*   **Agentic AI 架构先驱**：作为“代理式人工智能”领域的标杆项目，确立了自主规划、反思与执行的典型范式。
*   **广泛的 LLM 生态适配**：不仅限于 OpenAI，还整合了 Claude、Llama 等多家厂商的模型接口，降低单一供应商依赖风险。
*   **高社区活跃度**：拥有极高的 GitHub 星标数（18.5万+），意味着丰富的插件生态、活跃的社区支持及持续的功能迭代。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185149 | 🍴 46125 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164244 | 🍴 21266 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163868 | 🍴 30363 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156588 | 🍴 46150 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150028 | 🍴 9331 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146437 | 🍴 23036 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

