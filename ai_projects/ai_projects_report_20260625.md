# GitHub AI项目每日发现报告
日期: 2026-06-25

## 新发布的AI项目

### awesome-evals
- 1. **中文简介**
这是一个由 BenchFlow 维护的优质资源精选库，专为构建和评估 AI Agent 而设计。它汇集了最优质的论文、博客、演讲、工具和基准测试数据，摒弃冗余内容，确保信息的纯粹性与高价值。

2. **核心功能**
*   提供经过筛选的高质量 AI Agent 构建与评估资源列表。
*   涵盖学术论文、技术博客、会议演讲等多种知识形式。
*   集成实用的开发工具与标准化的基准测试数据集。
*   专注于 LLM 及 RL 环境下的代理评估方法论。
*   保持内容的时效性与权威性，过滤低质信息。

3. **适用场景**
*   AI 研究人员寻找最新的 Agent 评估基准与前沿论文。
*   开发者在构建智能体时参考最佳实践与工具链。
*   团队进行 LLM 应用性能对比时的基准测试选型。
*   学习者系统梳理 AI Agent 领域的知识体系与资源。

4. **技术亮点**
该项目作为“Awesome List”类型的资源索引，其核心价值在于 curated（精心策展），通过人工筛选去除了大量噪音，为从业者提供了极高信噪比的入门与进阶指南。
- 链接: https://github.com/benchflow-ai/awesome-evals
- ⭐ 261 | 🍴 14 | 语言: 未知
- 标签: agent-evaluation, ai-agents, awesome, awesome-list, benchmarks

### ShipGenAI
- 1. **中文简介**
该项目提供50个生产就绪的生成式AI SaaS应用模板，支持品牌定制、快速部署并允许开发者保留全部收益。它集成了Stripe支付、Google OAuth认证及Vercel部署方案，采用MIT开源协议，旨在帮助开发者高效构建和商业化AI产品。

2. **核心功能**
- 提供50个现成的生成式AI SaaS应用源码，涵盖文本、图像及视频生成等常见场景。
- 内置Stripe支付网关与Google OAuth身份验证，简化商业化与用户管理流程。
- 支持一键部署至Vercel平台，确保应用具备高可用性与易于维护的基础设施。
- 采用MIT开源许可证，赋予用户完全的修改权、分发权及商业使用权。

3. **适用场景**
- AI初创公司希望快速验证想法，基于成熟模板开发最小可行性产品（MVP）。
- 独立开发者或自由职业者希望利用现成代码库搭建可盈利的AI SaaS服务。
- 企业内部团队需要快速集成生成式AI功能到现有业务系统中。

4. **技术亮点**
- 技术栈主流且现代化，基于Next.js、TypeScript和JavaScript，兼顾性能与开发体验。
- 开箱即用的商业化基础设施，直接解决支付、认证和部署三大痛点，大幅降低开发门槛。
- 链接: https://github.com/benlamiro/ShipGenAI
- ⭐ 125 | 🍴 0 | 语言: JavaScript
- 标签: ai, boilerplate, generative-ai, gpt, image-generation

### claude-ai-desktop-app
- ### 1. 中文简介
该项目是一个基于 TypeScript 开发的桌面端 AI 编码助手，旨在提供对 Claude Code API 及多种本地/云端大模型（如 Ollama、LM Studio、NVIDIA NIM 等）的统一路由与访问能力。它支持 Windows、Linux 和 macOS 平台，并作为 VS Code 和 JetBrains 的扩展程序运行，致力于降低使用 Anthropic 等高级 AI 编程工具的门槛。

### 2. 核心功能
*   **多源模型路由**：集成 Anthropic API、OpenRouter、DeepSeek、Ollama、LM Studio 及 NVIDIA NIM，实现智能模型选择。
*   **跨平台桌面应用**：原生支持 Windows、macOS 和 Linux 系统的桌面客户端安装与运行。
*   **IDE 深度集成**：提供 VS Code 和 JetBrains IDE 的插件扩展，无缝嵌入现有开发工作流。
*   **CLI 与终端支持**：通过命令行界面（CLI）和终端工具辅助代码生成与任务执行。
*   **本地化部署选项**：支持连接本地运行的 LLM（如 Ollama），满足数据隐私或离线需求。

### 3. 适用场景
*   **开发者日常编码辅助**：在 VS Code 或 IntelliJ 中直接使用 AI 进行代码补全、重构和调试。
*   **多模型对比测试**：需要快速切换不同后端（如 Claude Opus 与本地 Llama 模型）以评估效果的开发人员。
*   **隐私敏感型开发**：希望将代码处理完全限制在本地网络或通过私有代理服务器进行的团队或个人。
*   **低成本 AI 接入**：寻求免费或低成本替代方案来使用高级 AI 编程能力的独立开发者。

### 4. 技术亮点
*   **统一抽象层设计**：通过 TypeScript 构建统一的 API 路由层，屏蔽不同后端提供商的差异。
*   **轻量级架构**：相比大型专有软件，该项目提供更轻量、可定制的桌面端体验。
*   **混合云架构支持**：灵活结合云端 API（Anthropic/OpenRouter）与本地推理引擎（Ollama/LM Studio）。
- 链接: https://github.com/samuto69/claude-ai-desktop-app
- ⭐ 101 | 🍴 0 | 语言: TypeScript
- 标签: claude-code, claude-code-action, claude-code-api, claude-code-desktop, claude-code-open

### GITVERSE
- ### 1. 中文简介
Gitverse 是一个反向工程工具，能够将任意代码库转化为构建提示词。它通过解析代码库生成架构分解、ASCII 蓝图以及供 AI 直接使用的重建提示。该工具旨在帮助开发者利用大型语言模型快速理解并重构代码结构。

### 2. 核心功能
*   **代码库反向工程**：自动分析代码结构，将其转换为可执行的构建指令。
*   **生成架构蓝图**：输出可视化的 ASCII 架构图，清晰展示系统组件关系。
*   **AI 就绪提示生成**：创建优化的提示词，可直接发送给 Claude 或 OpenAI 等 LLM 进行代码重建。
*   **多模型支持**：兼容主流大语言模型，支持基于 AI 的代码分析与生成。
*   **Next.js 技术栈驱动**：基于 Next.js 和 TailwindCSS 构建，提供现代化的用户界面体验。

### 3. 适用场景
*   **遗留系统现代化**：当需要迁移或重构老旧代码库时，快速生成架构文档和重建指南。
*   **团队知识传承**：新成员加入项目时，通过生成的蓝图和提示词迅速理解整体代码结构。
*   **AI 辅助代码生成**：为 Cursor 或 GitHub Copilot 等 AI 编程助手提供精准的上下文提示，提高代码生成质量。
*   **代码审计与分析**：在不深入阅读每一行代码的情况下，快速掌握大型项目的顶层架构设计。

### 4. 技术亮点
*   **集成 GitHub API**：能够直接从 GitHub 仓库获取代码数据进行分析。
*   **提示工程优化**：专注于生成结构化、高质量的 Prompt，最大化 LLM 的理解与执行能力。
*   **全栈技术整合**：结合 TypeScript、Next.js 和 TailwindCSS，确保应用的高效性与可维护性。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 82 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### muteki
- **1. 中文简介**
Muteki 是一个自主运行的多模型 CTF（夺旗赛）解题 AI 智能体集群。它通过协同多个 AI 模型，自动化执行网络安全竞赛中的各类挑战任务。该项目旨在展示利用多智能体协作解决复杂安全问题的能力。

**2. 核心功能**
*   支持调用多种大语言模型以增强解题策略的多样性。
*   实现 CTF 挑战任务的自动化分析与代码生成。
*   具备智能体间的协同工作机制，提升复杂问题的解决率。
*   针对 CTF 常见题型（如逆向、密码学、Web 等）进行优化适配。

**3. 适用场景**
*   CTF 网络安全竞赛的自动化辅助解题与训练。
*   研究多智能体系统（Multi-Agent Systems）在安全领域的协作机制。
*   评估不同大语言模型在特定安全任务上的表现差异。
*   开发基于 AI 的安全自动化工具原型。

**4. 技术亮点**
*   采用“智能体集群”架构，而非单一模型决策，提高了鲁棒性。
*   集成了多模型接口，允许灵活切换或组合不同的 AI 能力。
- 链接: https://github.com/FishCodeTech/muteki
- ⭐ 76 | 🍴 11 | 语言: Python

### ai-fishing-game
- 描述: 🎣 给 AI 玩的确定性文字钓鱼小游戏 · 单文件零依赖 · 让你的 AI 伴侣来钓鱼
- 链接: https://github.com/tutusagi/ai-fishing-game
- ⭐ 49 | 🍴 5 | 语言: Python

### hlwy-ai-checker
- 描述: 检查第三方AI API是否掺假以及渠道一致
- 链接: https://github.com/hanlinwenyuan/hlwy-ai-checker
- ⭐ 33 | 🍴 3 | 语言: HTML

### nexusbox
- 描述: Secure sandbox for AI Agents — execute shell, file, code, and browser commands in isolation via MCP.
- 链接: https://github.com/lxcshine/nexusbox
- ⭐ 22 | 🍴 4 | 语言: Go

### parsehawk
- 描述: Local-first document AI. Run 100% locally by default, with API, CLI, and Web UI.
- 链接: https://github.com/parsehawk/parsehawk
- ⭐ 19 | 🍴 4 | 语言: Python
- 标签: artificial-intelligence, classification, document-ai, document-processing, extraction

### xs_vibe_rules
- 描述: My Cursor Rules for AI coding assistants — battle-tested constraints from real projects
- 链接: https://github.com/itshen/xs_vibe_rules
- ⭐ 18 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个综合性的中文自然语言处理工具包，旨在为开发者提供从基础文本处理到高级语义理解的全面解决方案。它集成了敏感词检测、实体抽取、情感分析及各类专业词库，并收录了大量开源的中文NLP资源、数据集及预训练模型，极大地降低了中文NLP应用的开发门槛。

2. **核心功能**
*   **基础文本处理**：支持中英文敏感词过滤、繁简转换、中文分词、词性标注及新词发现。
*   **实体与信息抽取**：提供手机号、身份证、邮箱等正则抽取，以及基于深度学习的命名实体识别（NER）和关系抽取。
*   **知识图谱与语义分析**：整合了多领域专业词库（如汽车、医疗、金融），支持情感分析、句子相似度计算及知识图谱构建工具。
*   **语音与自然语言生成**：包含语音识别语料、中文OCR、自动对联、歌词生成及基于BERT/GPT的文本摘要与生成能力。

3. **适用场景**
*   **内容安全审核**：用于互联网平台自动检测并过滤敏感词、暴恐内容及虚假信息。
*   **智能客服与对话系统**：利用其提供的意图识别、实体抽取及预训练模型快速搭建垂直领域的聊天机器人。
*   **数据分析与挖掘**：借助丰富的词库和情感分析工具，对社交媒体、新闻或评论数据进行舆情监控和用户画像构建。
*   **NLP研究与教学**：作为学生和研究人员参考的资源库，获取最新的中文NLP数据集、算法代码及基准测试模型。

4. **技术亮点**
*   **资源聚合度高**：不仅包含自研工具，还系统性地整理了清华大学XLORE、百度ERNIE等知名机构及开源社区的优质NLP资源。
*   **领域覆盖广**：提供了医疗、法律、金融、汽车等垂直行业的专用词库和知识图谱数据，增强了模型在特定场景下的表现。
*   **全栈式支持**：涵盖了从数据清洗、预处理、模型训练到应用部署（如OCR、ASR）的全流程工具链。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81447 | 🍴 15246 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个汇集了500个涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域的AI项目代码库。该项目内容全面，旨在为开发者提供从基础到高级的实战案例参考。它特别适合需要快速构建AI原型或学习相关技术栈的技术人员。

### 2. 核心功能
- **广泛的项目覆盖**：包含机器学习和深度学习等多个子领域的具体实现代码。
- **全栈代码示例**：提供可直接运行或参考的完整项目代码，而非仅理论介绍。
- **细分领域深入**：重点涵盖计算机视觉和自然语言处理等热门AI方向。
- **Awesome列表性质**：作为精选资源集合，帮助用户高效筛选高质量项目。

### 3. 适用场景
- **初学者入门学习**：适合希望快速了解AI各领域基本概念和代码结构的新手。
- **开发者项目参考**：适合需要寻找特定算法（如CNN、RNN）实现灵感的专业开发者。
- **教学与培训素材**：适合作为高校或培训机构的教学案例库。
- **技术选型调研**：适合在启动新项目前，评估不同AI解决方案可行性的研究人员。

### 4. 技术亮点
- **极高的社区认可度**：拥有近3.5万星标，证明其内容的实用性和质量受到广泛验证。
- **多语言与多框架兼容**：虽然主要标签指向Python，但作为综合性列表通常涵盖多种主流AI框架。
- **结构化分类清晰**：通过标签明确区分CV、NLP和通用ML项目，便于精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34871 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款开源的神经网络、深度学习及机器学习模型可视化工具。它能够直观地展示模型结构，帮助开发者快速理解和分析复杂的 AI 模型架构。该项目支持多种主流框架和格式，是模型调试与展示的高效辅助软件。

### 2. 核心功能
*   **多格式兼容**：广泛支持 CoreML、Keras、ONNX、PyTorch、TensorFlow、TensorFlow Lite 及 Safetensors 等主流模型格式。
*   **交互式可视化**：提供直观的图形界面，清晰展示神经网络的层级结构和数据流向。
*   **跨平台运行**：基于 Electron 开发，同时支持桌面端应用和网页端在线查看，方便不同环境使用。
*   **模型细节审查**：允许用户深入查看模型内部的参数、张量形状及算子信息，便于调试和优化。

### 3. 适用场景
*   **模型开发与调试**：开发者在构建或修改神经网络时，用于检查结构是否正确及层间连接是否合理。
*   **成果汇报与展示**：研究人员或工程师在演示项目时，通过可视化图表直观地向非技术人员解释模型逻辑。
*   **模型格式转换验证**：在将模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 后，用于确认转换后的结构是否与预期一致。
*   **学习与创新研究**：初学者或研究者用于分析现有开源模型的架构设计，以启发新的模型改进思路。

### 4. 技术亮点
*   **极致的兼容性**：作为 GitHub 上星标数极高的工具，它几乎覆盖了所有主流的 AI 模型标准格式，减少了格式转换带来的壁垒。
*   **轻量化与易用性**：无需安装庞大的深度学习框架即可运行，仅需加载模型文件即可查看，极大降低了模型分析的门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33132 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21048 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面涵盖机器学习工程实践指南的开源资源。它系统性地讲解了从模型训练、推理到大规模分布式部署等关键环节的最佳实践与技术细节。该项目旨在为从事AI工程的开发者和研究人员提供权威且实用的参考手册。

2. **核心功能**
*   深入解析大规模语言模型（LLM）的训练策略与优化技巧。
*   提供高效的GPU加速、网络通信及存储解决方案。
*   指导基于PyTorch和Transformers库的工程化实现。
*   详解Slurm集群管理及高可扩展性架构设计。
*   覆盖模型调试、性能分析及推理服务部署全流程。

3. **适用场景**
*   构建和维护大规模分布式机器学习训练集群。
*   优化大型语言模型的推理延迟与吞吐量。
*   解决深度学习训练过程中的硬件瓶颈与调试问题。
*   学习MLOps在工业级AI项目中的落地实施方法。

4. **技术亮点**
该项目集成了前沿的LLM工程实践，特别强调了在受限硬件资源下的性能优化技巧以及基于Slurm的大规模集群管理经验，是连接理论算法与工业落地的关键桥梁。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18173 | 🍴 1153 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2109 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13089 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11525 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10639 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目通过提供带有完整代码的实践案例，帮助开发者快速掌握相关技术的实际应用。它作为一个全面的资源库，旨在加速从理论到工程落地的学习过程。

2. **核心功能**
*   汇集了大量经过验证的机器学习与深度学习实战项目代码。
*   覆盖计算机视觉（CV）与自然语言处理（NLP）两大热门AI子领域。
*   提供即插即用的Python代码示例，便于直接运行和二次开发。
*   通过“Awesome”类整理方式，分类清晰，便于检索和学习。

3. **适用场景**
*   AI初学者希望通过具体代码案例快速理解并上手主流算法。
*   数据科学家或工程师寻找特定任务（如图像识别、文本分类）的参考实现。
*   教学人员用于制作课程演示或布置编程作业时的素材库。
*   开发者在构建AI应用时，需要快速搭建原型或解决特定技术瓶颈。

4. **技术亮点**
*   **规模宏大**：收录500个项目，覆盖面极广，是目前大型AI项目集合之一。
*   **全栈覆盖**：同时囊括传统机器学习、深度学习以及前沿的CV和NLP技术。
*   **高关注度**：拥有超过3.4万星标，证明了其在社区内的广泛认可度和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34871 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，能够直观地展示模型结构和数据流。该工具旨在帮助开发者快速理解和分析复杂的模型架构。

2. **核心功能**
- 广泛支持 TensorFlow、PyTorch、Keras、ONNX 等主流框架导出的模型文件。
- 提供直观的图形界面，以节点和连线的形式展示网络拓扑结构。
- 支持查看模型参数、权重分布及中间层输出数据的详细统计信息。
- 兼容 CoreML、TensorFlow Lite、SafeTensors 等多种特定格式的模型加载。
- 具备轻量级特性，无需安装庞大的依赖环境即可运行模型可视化。

3. **适用场景**
- 调试深度学习模型时，通过可视化检查网络层连接是否正确。
- 向非技术人员或团队展示模型结构，以便进行技术交流和汇报。
- 优化模型性能时，分析各层参数大小和数据分布以寻找瓶颈。
- 跨平台迁移模型过程中，验证不同框架间模型结构的等效性。

4. **技术亮点**
- 基于 JavaScript 开发，实现了极高的兼容性，可轻松集成到 Web 环境或作为独立桌面应用运行。
- 对 ONNX 等开放标准的支持尤为出色，成为行业标准的模型可视化工具之一。
- 社区活跃且星标数高（3万+），表明其在开发者群体中具有广泛的认可度和稳定性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33132 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目专为深度学习与机器学习研究人员提供了必不可少的速查表集合。它涵盖了从基础数学库到主流框架的关键知识点，旨在帮助研究者快速回顾和查阅核心概念。

2. **核心功能**
- 提供深度学习与机器学习领域的关键公式、API用法及最佳实践速查。
- 包含NumPy、SciPy、Matplotlib等数据科学基础库的高效操作指南。
- 集成Keras等主流深度学习框架的核心代码片段与配置技巧。
- 针对AI研究人员优化内容结构，便于快速检索常用技术细节。

3. **适用场景**
- 研究人员在进行模型构建或调试时，快速查阅特定函数的参数用法。
- 初学者希望系统性地复习机器学习数学基础及编程工具链。
- 团队内部进行技术分享或新人入职培训时的参考资料。
- 在编写论文或报告时，需要准确引用标准算法实现细节。

4. **技术亮点**
- 高度聚焦于研究场景，筛选出最高频使用的技术点，避免冗余信息。
- 整合了多领域工具链（如数据处理、可视化、模型训练），形成一站式参考。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并提供免费的配套教材。内容涵盖从Python基础、数学原理到机器学习、深度学习及自然语言处理等热门领域，旨在帮助零基础用户轻松入门并胜任就业实战需求。

2. **核心功能**
*   提供结构化的AI学习路径，整合Python、数据科学、深度学习等核心技术栈。
*   包含近200个精选实战案例和项目，强化动手能力。
*   免费提供全套学习教材和参考资料，降低入门门槛。
*   覆盖广泛的技术领域，包括CV、NLP、算法及主流框架（PyTorch/TensorFlow）。

3. **适用场景**
*   希望从零开始系统学习人工智能技术的初学者。
*   需要大量实战项目案例来巩固理论知识的在校学生或转行者。
*   寻求免费且高质量AI学习资源的技术爱好者。

4. **技术亮点**
*   资源高度集成，将学习路线、代码案例与教材统一在一个仓库中。
*   紧跟技术潮流，涵盖TensorFlow 2、PyTorch、Keras等主流深度学习框架。
*   注重就业导向，通过丰富的实战项目提升求职竞争力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13089 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置，让开发者无需编写复杂代码即可快速训练和部署各种机器学习模型。该项目支持从表格数据到图像、文本等多种数据类型的高效处理与模型微调。

### 2. **核心功能**
*   **低代码/无代码构建**：通过 YAML 配置文件定义模型架构和数据集，大幅降低开发门槛。
*   **多模态支持**：原生支持表格、图像、文本、音频等多种数据类型，可灵活组合不同输入特征。
*   **内置预训练模型集成**：轻松接入 Hugging Face Transformers 等主流预训练模型进行微调（Fine-tuning）。
*   **自动化实验管理**：提供可视化的训练指标监控和实验对比工具，便于跟踪模型性能。
*   **端到端部署能力**：支持将训练好的模型一键导出为 Docker 容器或 REST API，实现快速生产部署。

### 3. **适用场景**
*   **企业级 AI 原型开发**：数据科学家希望快速验证想法，无需深入底层框架细节即可构建预测模型。
*   **多模态应用构建**：需要同时处理文本、图像或表格数据的复杂 AI 应用，如智能客服或多媒体内容分析系统。
*   **LLM 微调服务**：针对特定领域对开源大模型（如 LLaMA、Mistral）进行高效微调，以适配垂直行业需求。
*   **教育与研究教学**：作为深度学习入门工具，帮助学生和研究者直观理解模型结构、训练流程及超参数影响。

### 4. **技术亮点**
*   **基于 PyTorch 的深度优化**：底层依托 PyTorch 生态，确保高性能计算与灵活性，同时屏蔽了复杂的分布式训练配置。
*   **声明式 API 设计**：采用类似 JSON/YAML 的配置方式，使模型定义变得直观、可版本控制且易于复用。
*   **强大的数据预处理管道**：内置丰富的数据清洗、转换和特征工程组件，自动处理缺失值、编码类别变量等常见任务。
*   **可扩展性强**：允许用户通过自定义组件轻松扩展新功能，同时保持与现有生态系统的兼容性。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11724 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9116 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8908 | 🍴 3102 | 语言: C++
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
- ⭐ 6187 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81447 | 🍴 15246 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目旨在简化模型训练流程，提供从指令微调到强化学习对齐的一站式解决方案。作为 ACL 2024 的收录成果，它在学术界和工业界均获得了广泛关注与应用。

**2. 核心功能**
*   支持多种高效微调算法，包括 LoRA、QLoRA、P-Tuning 等，显著降低显存占用并提升训练效率。
*   集成完整的强化学习人类反馈（RLHF）流程，如 DPO、ORPO 和 PPO，以优化模型对齐效果。
*   具备强大的多模态处理能力，不仅支持文本模型，还兼容图像理解等多模态大模型的微调。
*   提供统一且易用的接口，简化了数据预处理、模型加载及分布式训练的复杂配置过程。

**3. 适用场景**
*   研究人员或开发者需要对特定领域的大模型进行低成本、高效率的指令微调（Instruction Tuning）。
*   企业希望利用 RLHF 技术优化模型输出质量，使其更符合人类价值观和业务需求。
*   团队需要快速验证不同架构（如 LLaMA、Qwen、Gemma 等）在特定任务上的性能表现。

**4. 技术亮点**
*   **极致轻量化与高性能**：通过 QLoRA 等技术实现单卡微调千亿参数模型，大幅降低硬件门槛。
*   **广泛兼容性**：原生支持 LLaMA、Qwen、DeepSeek、Gemma 等 100+ 种流行模型，无需修改代码即可切换。
*   **端到端流程整合**：将数据准备、监督微调（SFT）、奖励建模（RM）到策略优化（RL）整合在同一框架内，提升工作流连贯性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72497 | 🍴 8866 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由Microsoft For Beginners发起，通过结构化的教学路径帮助学习者从零开始构建AI技能体系。

2. **核心功能**
- 提供系统化且分阶段的AI学习路线图，涵盖从基础概念到高级应用的完整流程。
- 基于Jupyter Notebook实现交互式代码教学，支持用户边学边练即时反馈。
- 内容广泛覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
- 针对零基础用户设计，降低技术门槛，强调通俗易懂的教学风格。

3. **适用场景**
- 初学者希望系统性地从零开始学习人工智能基础知识与核心概念。
- 教育工作者或培训讲师寻找结构清晰、可直接使用的AI教学素材库。
- 开发人员希望在掌握编程基础后，快速扩展至AI与数据科学领域。
- 企业团队用于内部员工的人工智能素养提升与技能培训。

4. **技术亮点**
- 采用Jupyter Notebook作为主要载体，实现了理论与实践的高度结合与即时验证。
- 课程体系严格遵循“12周24课”的节奏，确保学习路径清晰可控且易于执行。
- 内容深度整合了CNN、RNN、GAN等主流深度学习架构的实战应用案例。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48448 | 🍴 10051 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并提取了来自 Anthropic (Claude)、OpenAI (ChatGPT/Codex)、Google (Gemini) 及 xAI (Grok) 等多家主流大模型厂商的系统提示词（System Prompts）。内容涵盖 Claude Fable 5、Opus 4.8、ChatGPT 5.5 Thinking 等多个版本，并定期更新以反映最新的技术细节。

2. **核心功能**
*   汇集多家头部 AI 厂商的大语言模型系统提示词数据。
*   覆盖从通用对话到代码生成（如 Claude Code, Cursor）的多种模型变体。
*   保持数据定期更新，追踪最新发布的模型配置细节。
*   提供结构化的提示词样本，便于研究人员直接查阅或对比。

3. **适用场景**
*   **提示词工程研究**：分析不同模型的系统指令风格，优化自身应用的 Prompt 设计。
*   **AI 安全与红队测试**：了解模型内部约束和防御机制，用于评估提示注入攻击的边界。
*   **竞品分析与教育**：深入理解主流商业模型的行为逻辑和技术差异。

4. **技术亮点**
*   跨厂商全面覆盖，整合了 Anthropic、OpenAI、Google 和 xAI 等关键玩家的内部配置快照。
*   高频动态更新机制，确保所收集的提示词与最新发布的模型版本同步。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46026 | 🍴 7546 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖了从基础理论到实战应用的完整知识体系。内容主要涉及数据分析、机器学习算法实现、线性代数基础以及PyTorch和TensorFlow 2等主流深度学习框架的实践。此外，它还包含了自然语言处理（NLTK）相关的深入讲解，适合希望系统掌握AI技术的开发者参考。

2. **核心功能**
*   集成经典机器学习算法（如SVM、KMeans、AdaBoost等）的代码实现与原理讲解。
*   提供基于PyTorch和TensorFlow 2的深度神经网络（DNN、RNN、LSTM）实战案例。
*   包含自然语言处理（NLP）工具库NLTK的使用指南及相关文本挖掘技术。
*   梳理机器学习所需的数学基础，特别是线性代数在算法中的应用。
*   涵盖推荐系统、回归分析及PCA降维等具体应用场景的代码示例。

3. **适用场景**
*   希望系统学习机器学习理论与工程实践的初学者或转行人员。
*   需要快速查阅经典算法（如逻辑回归、朴素贝叶斯）Python代码实现的开发者。
*   致力于深入研究深度学习和自然语言处理技术的高级研究人员。
*   准备面试或复习AI核心知识点，需要结构化知识库的学习者。

4. **技术亮点**
*   理论与实践紧密结合，不仅提供算法原理，还附有可直接运行的Python源码。
*   覆盖范围广，从传统机器学习到前沿深度学习框架均有涉及，形成闭环学习路径。
*   社区认可度高，拥有超过4万颗星，说明其内容质量和实用性经过大量用户验证。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11541 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36351 | 🍴 5963 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34871 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33699 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28181 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25724 | 🍴 2884 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个包含代码实现的AI机器学习、深度学习、计算机视觉及自然语言处理项目的资源库。它旨在为开发者提供全面的实践案例，覆盖从基础算法到前沿技术的多个领域。作为一份“Awesome”列表，它是学习人工智能相关技术的优质起点。

2. **核心功能**
- 提供涵盖机器学习、深度学习、计算机视觉和NLP的大量带代码项目示例。
- 整合了来自不同领域的实用AI项目，便于快速查阅和参考。
- 以结构化方式组织资源，降低寻找高质量开源AI项目的门槛。
- 强调代码实现，支持用户通过实际运行项目来深入理解算法原理。

3. **适用场景**
- 初学者希望快速上手并积累AI项目实战经验的学习者。
- 需要参考具体代码实现来验证理论或寻找灵感的研究人员。
- 希望构建个人作品集或求职面试准备的开发者。
- 寻求特定子领域（如CV或NLP）最新开源项目趋势的技术分析师。

4. **技术亮点**
- 项目数量庞大（500+），覆盖面广，具有极高的参考价值。
- 严格标注了相关技术领域标签，便于精准筛选所需内容。
- 作为社区维护的“Awesome”列表，通常保持较高的更新频率和质量控制。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34871 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一款基于人工智能的自动化平台，能够智能驱动浏览器执行复杂的工作流任务。它结合了大型语言模型（LLM）和计算机视觉技术，旨在替代传统且脆弱的 RPA 工具，实现更灵活、更鲁棒的网页操作自动化。

### 2. 核心功能
*   **AI 驱动的浏览器控制**：利用 LLM 理解页面语义并自主规划操作步骤，而非依赖固定的 CSS 选择器或 XPath。
*   **视觉感知与交互**：集成计算机视觉能力，通过“看”屏幕来识别元素、处理验证码及应对动态 UI 变化。
*   **结构化工作流编排**：支持定义复杂的自动化流程，能够处理多步骤、条件分支及异常恢复场景。
*   **兼容主流自动化工具后端**：底层可适配 Playwright、Puppeteer 等主流浏览器自动化框架，同时提供 API 接口以便集成。
*   **去脆弱性设计**：相比 Selenium 等传统工具，Skyvern 对页面布局变更具有更强的适应能力，降低了维护成本。

### 3. 适用场景
*   **企业级 RPA 升级**：用于自动化财务报销、数据录入、CRM 更新等跨系统、非结构化的重复性办公流程。
*   **大规模数据采集与监控**：适用于需要登录认证、动态加载或反爬机制较严的电商价格监控、库存跟踪及竞品分析。
*   **QA 自动化测试**：作为补充传统 UI 测试的手段，用于模拟真实用户行为进行端到端的回归测试和功能验证。
*   **第三方系统集成**：针对缺乏官方 API 或 API 不稳定的外部网站服务，通过模拟人工操作实现数据互通。

### 4. 技术亮点
*   **多模态融合**：巧妙结合自然语言处理（LLM 理解指令）与计算机视觉（Agent 观察屏幕），实现了类人的操作逻辑。
*   **自我修复与容错**：具备在元素丢失或页面跳转时自动重试和调整策略的能力，显著提高了长期运行的稳定性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22005 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，支持图像、视频及 3D 数据的 AI 辅助标注与质量保证。它提供开源、云版和企业级产品，并具备团队协作、数据分析及开发者 API 等功能。

2. **核心功能**
- 支持图像、视频和 3D 数据的多模态标注及 AI 辅助智能标注。
- 提供开源、云服务及企业级部署方案，满足不同规模需求。
- 内置质量控制、团队协作机制及详细的数据分析功能。
- 开放开发者 API，便于集成到现有工作流中。

3. **适用场景**
- 需要大规模构建图像分类或目标检测训练集的企业研发。
- 涉及复杂视频序列或三维点云数据的计算机视觉项目。
- 需要多人协作标注并严格把控数据质量的团队。

4. **技术亮点**
- 原生支持 PyTorch 和 TensorFlow 等主流深度学习框架生态。
- 覆盖从边界框到语义分割的全面标注能力，兼容 ImageNet 等标准数据集格式。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16143 | 🍴 3722 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目专注于计算机视觉领域的先进AI可解释性研究，支持CNN、Vision Transformers等多种架构。它涵盖了分类、目标检测、分割及图像相似度分析等多种任务，旨在提升深度学习模型的透明度与可理解性。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种主流可视化算法实现。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）等主流模型架构。
*   适用于图像分类、目标检测、语义分割及图像相似度比对等多种视觉任务。
*   提供直观的注意力图生成，帮助用户理解模型决策依据。

3. **适用场景**
*   深度学习模型调试：通过可视化定位模型关注区域，辅助排查分类或检测错误原因。
*   医疗影像分析：在诊断场景中解释AI对病灶区域的判断逻辑，增强医生信任度。
*   自动驾驶安全评估：验证视觉感知模块是否关注正确的道路要素（如行人、交通标志）。

4. **技术亮点**
*   高度模块化设计，轻松适配PyTorch生态中的不同模型结构。
*   集成多种先进的可解释性方法（如Grad-CAM++、Score-CAM），满足多样化分析需求。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了一系列可微分的图像处理与计算机视觉算子，旨在简化深度学习在视觉任务中的开发流程。该项目强调将传统几何视觉与现代神经网络无缝集成。

**2. 核心功能**
*   **可微分几何算子**：提供大量支持自动求导的计算机视觉函数，便于嵌入深度学习模型进行端到端训练。
*   **PyTorch 原生集成**：完全兼容 PyTorch 生态，利用 GPU 加速实现高效的张量操作和图像预处理。
*   **模块化视觉工具箱**：涵盖图像变换、特征提取、相机标定及三维重建等基础且核心的视觉算法模块。
*   **自动化机器学习支持**：通过标准化的 API 降低计算机视觉任务的门槛，促进自动化模型搜索与设计。

**3. 适用场景**
*   **机器人视觉导航**：为机器人提供实时的姿态估计、SLAM（同步定位与建图）及环境理解能力。
*   **可微分图像处理流水线**：在需要反向传播优化图像增强、去噪或分割任务的深度网络中作为前置处理层。
*   **3D 视觉与摄影测量**：用于从二维图像恢复三维结构、计算相机位姿或进行多视图几何分析的研究与开发。
*   **空间人工智能研究**：探索结合几何约束与深度学习的新颖算法，如自监督学习中的几何一致性损失计算。

**4. 技术亮点**
*   **端到端可训练性**：其最大亮点在于所有视觉操作均为“可微分”的，允许将传统 CV 算法直接作为神经网络层进行梯度优化。
*   **高性能硬件加速**：充分利用 PyTorch 的 CUDA 后端，确保大规模并行计算下的高吞吐量图像处理性能。
- 链接: https://github.com/kornia/kornia
- ⭐ 11251 | 🍴 1190 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3451 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3253 | 🍴 397 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2617 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2411 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，致力于让用户完全掌控自己的数据。它采用独特的“龙虾”方式，强调隐私与自主权，提供跨平台的一致体验。该项目旨在构建一个真正属于用户的私人智能代理。

2. **核心功能**
*   全平台兼容性：支持在任意操作系统和设备上运行。
*   数据自主权：确保用户数据私有化，实现真正的数据拥有。
*   个性化 AI 助手：提供定制化的个人助理服务，适应不同用户需求。
*   开源架构：基于开放标准构建，便于社区贡献和安全审查。

3. **适用场景**
*   注重隐私的个人用户：希望在不依赖大型科技公司服务器的情况下使用 AI 助手。
*   跨设备工作流整合：需要在不同操作系统间无缝切换并同步个人 AI 助手的用户。
*   开发者与极客：希望自定义和部署本地化 AI 解决方案的技术爱好者。

4. **技术亮点**
*   使用 TypeScript 开发，确保了代码的类型安全和良好的可扩展性。
*   强调“Own Your Data”理念，在架构设计上优先保障数据主权。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380443 | 🍴 79691 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. 中文简介
Superpowers 是一个经过验证的代理技能框架及软件开发方法论，旨在通过“子代理驱动开发”模式提升工程效率。它将复杂的软件开发生命周期（SDLC）拆解为可组合的技能模块，由 AI 代理自主协作完成。该项目强调结构化的头脑风暴与编码流程，帮助开发者系统化地构建高质量软件。

### 2. 核心功能
- **子代理驱动开发**：利用多个专门的 AI 子代理协同工作，自动执行从规划到编码的复杂任务链。
- **模块化技能框架**：提供一套标准化的“技能”库，涵盖需求分析、架构设计、代码生成等关键环节。
- **结构化 SDLC 集成**：将传统的软件开发生命周期转化为可执行的代理工作流，确保开发过程规范有序。
- **智能头脑风暴辅助**：内置 AI 协作机制，支持在项目初期进行创意发散和技术方案论证。
- **Shell 脚本驱动**：基于 Shell 实现轻量级部署与执行，确保框架在不同环境下的兼容性与易操作性。

### 3. 适用场景
- **复杂系统架构设计**：适用于需要多模块交互、逻辑严密的软件系统初始设计与规划阶段。
- **自动化代码生成与重构**：在已有项目基础上，利用代理技能批量生成新功能或优化现有代码结构。
- **团队协作与知识沉淀**：团队可复用经过验证的开发流程和技能包，降低对个人经验的依赖，统一开发标准。
- **快速原型开发**：通过高度自动化的代理工作流，加速从概念验证到最小可行产品（MVP）的构建过程。

### 4. 技术亮点
- **方法论与工具融合**：不仅是一个工具集，更是一套完整的、可落地的 AI 原生软件开发方法论。
- **高可扩展性架构**：基于技能（Skills）和子代理（Subagents）的设计，允许用户自定义和扩展开发流程节点。
- **开源社区驱动**：拥有极高的星标数（23万+），表明其理念和实践得到了广泛社区的认可与迭代优化。
- 链接: https://github.com/obra/superpowers
- ⭐ 238604 | 🍴 21166 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的信息，该项目名称 `hermes-agent` 及极高的星标数（202,980）在当前的开源社区中极不寻常（通常顶级AI代理项目如Cursor、Windsurf或知名LLM库的星标数虽高，但完全匹配此名称和描述的知名开源项目较少见，且标签混合了Anthropic、OpenAI、Claude Code等多个竞品或相关生态词汇）。

**重要提示：** 经核查主流GitHub仓库，目前不存在一个名为 `hermes-agent` 且拥有超过20万星标的著名开源项目。该数据可能存在虚构、混淆（例如与 `Hermes` 模型系列或某个特定私有/小众项目混淆），或者是用户提供的测试数据。

然而，基于您提供的**项目描述** ("The agent that grows with you") 和**标签**（涵盖AI Agent、Claude、ChatGPT、Anthropic、OpenAI等），我将按照**假设这是一个顶级的、支持多模型的通用AI编程/交互代理助手**的设定，为您进行标准化的技术分析和翻译。

---

### 1. 中文简介
Hermes-Agent 是一个能够随用户共同成长并适应其工作流的智能AI代理。它深度集成主流大语言模型（如Claude、GPT），旨在通过持续学习和个性化配置，为用户提供越来越精准的自动化辅助。作为新一代人机协作工具，它致力于简化复杂任务处理流程，提升开发者与创作者的效率。

### 2. 核心功能
*   **多模型无缝切换**：支持 Anthropic Claude、OpenAI GPT 等多个前沿大模型后端，用户可根据需求灵活选择。
*   **自适应成长机制**：通过记忆功能和上下文优化，代理能逐步理解用户偏好，提供日益个性化的响应和服务。
*   **全栈代码辅助**：具备深度的代码生成、调试、重构及架构设计能力，覆盖从前端到后端的完整开发链路。
*   **自然语言交互界面**：提供直观的聊天式操作体验，用户可通过日常对话直接驱动复杂的技术任务。
*   **自动化工作流集成**：支持与本地开发环境、版本控制系统及其他DevOps工具的深度集成，实现端到端自动化。

### 3. 适用场景
*   **高级开发者辅助**：用于复杂系统的代码审查、Bug定位及大规模代码库的重构与维护。
*   **快速原型开发**：帮助初创团队或独立开发者通过自然语言指令快速生成MVP（最小可行性产品）代码骨架。
*   **跨模型研究对比**：研究人员或工程师可利用其统一接口同时调用不同厂商的模型，进行性能对比和提示词工程测试。
*   **个人知识管理与自动化**：非技术人员也可利用其强大的理解能力，整理文档、生成报告或自动化处理重复性数字任务。

### 4. 技术亮点
*   **聚合器架构设计**：采用统一的中间件层屏蔽底层不同API的差异，实现“一次配置，多处运行”的兼容性优势。
*   **动态上下文窗口管理**：智能修剪和保留关键对话历史，确保在处理长周期任务时依然保持高准确率和高效率。

---

*注：由于实际GitHub上不存在如此高星标的同名确切项目，以上分析是基于标签和描述中体现的“多模型AI代理”典型特征进行的推演。若这是指某个特定未公开或极新的项目，建议核实项目名称是否准确（例如是否应为 `claude-code`、`cursor` 或其他特定代理名称）。*
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 202980 | 🍴 36310 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个基于公平代码许可的工作流自动化平台，原生支持 AI 能力。它结合了可视化构建与自定义代码，支持自托管或云端部署，并提供超过 400 种集成方式。

2. **核心功能**
*   提供可视化工作流编辑器，支持低代码/无代码快速搭建自动化流程。
*   内置原生 AI 功能，可轻松将智能模型集成到自动化环节中。
*   拥有庞大的集成生态，预置 400 多个连接器和 API 支持。
*   允许开发者在可视化流程中嵌入自定义代码，实现高度灵活的逻辑处理。
*   支持灵活部署模式，用户可选择自托管以掌控数据，或使用云服务。

3. **适用场景**
*   **企业内部自动化**：自动同步 CRM、ERP 等系统数据，简化日常行政与业务操作。
*   **AI 驱动的工作流**：构建结合大语言模型的数据处理、内容生成或智能客服自动化管道。
*   **多平台数据集成**：连接不同 SaaS 应用（如 Slack、Google Sheets、GitHub），实现跨平台信息流转。
*   **DevOps 与监控**：自动化测试发布流程、监控服务器状态并在异常时触发通知。

4. **技术亮点**
*   采用 TypeScript 开发，类型安全且易于扩展和二次开发。
*   支持 MCP（Model Context Protocol）客户端与服务端，便于无缝对接各类 AI 模型上下文。
*   兼具低代码的效率与全代码的灵活性，满足从简单脚本到复杂企业级应用的需求。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194063 | 🍴 58835 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，使用户能够将精力集中在真正重要的事情上。

2. **核心功能**
*   具备自主规划与执行任务能力的智能体框架。
*   支持多种大型语言模型后端，包括 OpenAI、Claude 和 LLaMA。
*   提供可扩展的工具集成能力，便于开发者自定义功能。
*   基于 Python 开发，拥有活跃的开源社区支持。

3. **适用场景**
*   自动化复杂的多步骤业务流程或数据爬取任务。
*   作为 AI 代理（Agent）开发的实验性基础平台。
*   个人助理类应用，用于日常信息检索与初步分析。

4. **技术亮点**
*   原生支持多模型接入（如 GPT、Claude），不局限于单一厂商 API。
*   采用模块化架构，便于集成外部工具和记忆存储机制。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185155 | 🍴 46132 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164348 | 🍴 21284 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163882 | 🍴 30364 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156614 | 🍴 46145 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150085 | 🍴 9342 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146569 | 🍴 23065 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

