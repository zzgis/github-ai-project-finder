# GitHub AI项目每日发现报告
日期: 2026-07-21

## 新发布的AI项目

### nativ
- 1. **中文简介**
nativ 是一款专为 macOS 设计的本地人工智能应用，原生支持 MLX 模型运行。它集成了聊天交互、模型服务、性能监控及连接管理等功能，让用户能够在一个统一的界面中高效处理本地机器学习任务。

2. **核心功能**
*   提供基于 MLX 模型的本地聊天交互体验。
*   支持将本地模型作为服务进行托管和调用。
*   实时监控模型运行状态及系统资源使用情况。
*   实现 MLX 模型的快速连接与管理。
*   采用 Swift 开发，深度适配 macOS 原生环境。

3. **适用场景**
*   macOS 用户希望在本地隐私安全地运行大语言模型。
*   开发者需要快速搭建和测试 MLX 框架下的 AI 服务。
*   研究人员希望在不依赖云端的情况下监控模型推理性能。
*   追求低延迟响应且注重数据安全的个人 AI 助手使用者。

4. **技术亮点**
*   原生集成 Apple 的 MLX 框架，充分发挥 M 系列芯片的硬件加速优势。
*   单一应用程序封装了从交互到服务部署的全生命周期管理。
- 链接: https://github.com/Blaizzy/nativ
- ⭐ 303 | 🍴 22 | 语言: Swift

### agents-council
- 描述: Multi-agents collaboration plugin for Claude Code - orchestrate multiple AI agents (Codex CLI, Gemini CLI, etc.) for diverse perspectives
- 链接: https://github.com/0xwilliamortiz/agents-council
- ⭐ 90 | 🍴 1 | 语言: JavaScript
- 标签: claude, claude-ai, claude-code, claude-code-skills, claude-plugin

### open-kritt
- ### 1. 中文简介
Open-Kritt 是一个开源项目，旨在通过编排多个 AI 智能体协作，在代码中发掘真实的安全漏洞。它利用人工智能技术自动化安全研究流程，帮助开发者和安全研究人员更高效地识别潜在风险。该项目侧重于模拟真实的攻击向量，以发现传统工具可能遗漏的深层漏洞。

### 2. 核心功能
- **多智能体协作**：通过编排多个 AI Agent 协同工作，模拟不同攻击视角进行代码审计。
- **真实漏洞挖掘**：专注于发现实际可利用的代码漏洞，而非仅依赖静态扫描规则。
- **自动化安全研究**：简化安全测试流程，自动执行复杂的探测和验证步骤。
- **支持 JavaScript 生态**：原生支持 JavaScript 语言编写的代码库，适配前端及 Node.js 后端环境。

### 3. 适用场景
- **Bug 赏金猎人**：用于自动化搜索 Web 应用中的高风险漏洞，提高赏金狩猎效率。
- **内部安全审计**：开发团队在发布前对自有代码库进行深度安全扫描和漏洞修复。
- **AI 安全研究**：研究人员利用其框架探索 AI 智能体在网络安全领域的边界和能力。
- **CI/CD 集成**：作为持续集成流水线的一部分，自动检测新提交代码中的安全缺陷。

### 4. 技术亮点
- **Agent 编排架构**：采用灵活的智能体调度机制，能够动态组合不同的分析策略。
- **聚焦实战效果**：强调发现“真实”漏洞，减少了误报率，更贴近实际攻击场景。
- **开源社区驱动**：基于开放的 GitHub 社区，便于安全研究者贡献新的检测逻辑和案例。
- 链接: https://github.com/Kritt-ai/open-kritt
- ⭐ 87 | 🍴 22 | 语言: JavaScript
- 标签: agent, agents, ai, bug-bounty, bugbounty

### stem-illustration-skill
- 描述: 面向 STEM（科学、技术、工程、数学）领域的 AI 图像生成 Skill。  生成科研示意图、教学插图、技术架构图等概念性图像，覆盖生物医学、化学、物理、工程、数学 6 大学科。  功能特性 24 个场景模板：信号通路、实验流程、细胞结构、概念信息图、学术海报、机制图、质粒图、机器学习架构等 6 大学科适配：生命科学/医学/化学/物理/工程/数学 4 种风格变体：academic / textbook / infographic / 3d-render
- 链接: https://github.com/liangdabiao/stem-illustration-skill
- ⭐ 39 | 🍴 0 | 语言: Python
- 标签: skill

### Google-Gemini-Desktop
- 1. **中文简介**
Google-Gemini-Desktop 是一个为 Windows、Mac 和 Linux 平台配置 Gemini Pro AI 客户端的项目，旨在提供原生桌面体验。它支持多模态 AI 推理、代码辅助及创意写作，并可与 ChatGPT 等其他工具进行对比。用户可下载仓库中的设置文件以快速部署。

2. **核心功能**
*   跨平台支持：兼容 Windows、Mac 和 Linux 操作系统。
*   多模态能力：提供 AI 推理、代码生成辅助及创意写作功能。
*   原生体验：作为本地桌面应用程序运行，而非仅限浏览器。
*   竞品对比：支持将搜索趋势与 ChatGPT、Claude 等桌面应用进行比较。
*   一键部署：提供仓库设置文件以便用户快速下载安装。

3. **适用场景**
*   需要在非浏览器环境下使用 Google Gemini 高级功能的开发者或研究人员。
*   希望整合多模态 AI 能力进行日常创意写作或编程工作的办公用户。
*   需要同时管理多个 AI 助手（如 ChatGPT、Claude）并进行性能或趋势对比的专业人士。

4. **技术亮点**
*   基于 TypeScript 开发，确保代码类型安全及良好的可扩展性。
*   直接集成 Gemini 系列模型（如 1.5 Pro、2.0 Flash 等），提供最新的 API 支持。
- 链接: https://github.com/googlegeminidesktop/Google-Gemini-Desktop
- ⭐ 34 | 🍴 0 | 语言: TypeScript
- 标签: free-gemini-api, gemini-, gemini-15-pro, gemini-2-0-flash, gemini-2-5-flash

### Cursor-Grok-4.5-xAI-free-desktop
- 描述: Cursor Grok 4.5 xAI free configures a desktop client for free Grok 4.5 AI model access. Track API endpoints, free tier pricing, and context window benchmarks against Claude, Kimi K3, Composer 2.5, and OpenRouter or Supergrok alternatives. Download direct repository setup and configuration files for Windows, macOS, Linux.
- 链接: https://github.com/CursorGrok4-5/Cursor-Grok-4.5-xAI-free-desktop
- ⭐ 33 | 🍴 0 | 语言: TypeScript
- 标签: ai-powered-applications, composer-2-5, cursor-ai-assistant, cursor-ai-project-rules, cursor-api

### LLM-WIKI
- 描述: 一个会自己生长的 AI 知识库
- 链接: https://github.com/loonggg/LLM-WIKI
- ⭐ 23 | 🍴 2 | 语言: JavaScript

### VibeGamer
- 描述: 用 AI Agent 自动游玩《Turmoil》（石油大亨）并不断积累经验进化的实验项目. 
- 链接: https://github.com/karminski/VibeGamer
- ⭐ 20 | 🍴 2 | 语言: TypeScript

### aipay-protocol
- 描述: Agent-native verifiable USDC escrow protocol for AI agents. Smart contracts, SDKs, MCP server, verifiers, operator, and web console.
- 链接: https://github.com/AIPAYagent/aipay-protocol
- ⭐ 17 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, aipay, eip-712, escrow, mcp

### ai-semantic-search-api
- 描述: 无描述
- 链接: https://github.com/HealerCodeLabs/ai-semantic-search-api
- ⭐ 17 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具包，旨在为开发者提供从基础文本清洗到高级语义理解的完整解决方案。它集成了敏感词检测、语言识别、实体抽取、情感分析及丰富的领域词库，是构建中文 NLP 应用的高效基础设施。

2. **核心功能**
*   **基础文本处理**：支持中英文敏感词过滤、繁简转换、中英日韩人名库、停用词及反动词表等基础清洗与标准化操作。
*   **信息抽取与识别**：内置手机号、身份证、邮箱抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取能力。
*   **语义分析与生成**：提供词汇情感值计算、关键词抽取、文本摘要生成，以及基于 GPT/BERT 的文本生成和相似度匹配算法。
*   **丰富领域知识图谱**：涵盖财经、法律、医疗、汽车、古诗词等多个垂直领域的专用词库和预训练模型资源。
*   **语音与OCR集成**：结合中文语音识别（ASR）数据集、中文手写汉字识别（OCR）及音频数据增强工具，拓展多模态处理能力。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析模块，快速搭建互联网平台的内容过滤和舆情监控系统。
*   **智能客服与对话机器人**：借助闲聊语料、意图识别及多轮对话数据集，开发具备上下文理解能力的智能问答系统。
*   **垂直行业知识挖掘**：在金融、医疗或法律领域，利用专用词库和实体抽取工具，从非结构化文档中提取关键业务信息。
*   **NLP 研究与教学**：作为学习中文 NLP 的参考资源库，提供从经典算法到最新 BERT/Transformer 模型的最佳实践代码。

4. **技术亮点**
*   **一站式资源聚合**：不仅包含代码工具，还整合了清华大学 XLORE、百度问答数据集等高质量公开数据集和预训练模型。
*   **模型轻量化与高性能**：提供如 `jieba_fast` 加速分词、`g2pC` 自动注音及基于 CUDA 优化的推理方案，提升处理效率。
*   **前沿技术落地**：紧跟 AI 发展趋势，集成了 BERT、RoBERTa、ALBERT 等主流预训练模型在中文任务中的微调与应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81930 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 项目分析报告：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

1. **中文简介**
   该项目是一个精选的资源库，汇集了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理领域的代码示例项目。它通过提供带有完整源码的实践案例，帮助开发者快速掌握AI核心算法与应用逻辑。作为一个“Awesome”列表，它是初学者进阶和工程师查找参考实现的优质指南。

2. **核心功能**
   - 提供大量（约500个）直接可运行的AI项目源代码。
   - 覆盖机器学习、深度学习、CV和NLP四大核心AI领域。
   - 包含具体子领域的专项项目（如图像识别、文本分类等）。
   - 采用社区维护的“Awesome”列表形式，筛选高质量资源。

3. **适用场景**
   - **学习者实战练习**：适合想通过阅读和运行代码来理解AI理论的学生或自学者。
   - **开发者灵感参考**：适合需要快速搭建原型或寻找特定算法实现思路的软件工程师。
   - **技能查漏补缺**：适合希望系统性地浏览不同AI子领域（如从NLP转到CV）的技术人员。

4. **技术亮点**
   - **全景式覆盖**：整合了从传统机器学习到前沿深度学习的广泛技术栈。
   - **代码即文档**：强调“with code”，通过实际项目而非纯理论文档进行教学。
   - **高社区认可度**：拥有35,590+星标，证明其资源质量和社区影响力极高。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35590 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33249 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习领域的开放标准，旨在促进不同深度学习框架之间的互操作性。它允许模型在不同平台间无缝迁移，简化了从开发到部署的流程。

2. **核心功能**
- 支持跨框架（如PyTorch、TensorFlow、Keras等）的模型转换与兼容。
- 提供标准化的中间表示格式，确保模型结构和数据的一致性。
- 拥有广泛的执行引擎支持，便于在不同硬件和软件环境中运行模型。
- 促进生态系统合作，降低机器学习模型部署的复杂性和成本。

3. **适用场景**
- 在开发阶段使用PyTorch训练模型，然后转换为ONNX以便在生产环境使用TensorRT或OpenVINO进行加速部署。
- 需要将模型从一家公司的内部框架迁移到另一家公司的云端推理服务时。
- 希望在不重新训练模型的情况下，评估和优化同一神经网络在不同硬件平台上的性能。

4. **技术亮点**
- 由微软、Facebook、Amazon等科技巨头共同维护，具有强大的社区和企业支持背景。
- 高度灵活的扩展性，允许自定义算子和优化策略以适应特定需求。
- 链接: https://github.com/onnx/onnx
- ⭐ 21180 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一部全面涵盖机器学习系统构建与部署的指南性资源。它深入探讨了从底层硬件配置到上层模型训练及推理优化的完整工程实践。该项目旨在为研究人员和工程师提供可扩展、高效的机器学习系统设计方法论。

2. **核心功能**
- 提供大规模分布式训练（如使用Slurm和PyTorch）的最佳实践与故障排除指南。
- 详解大语言模型（LLM）的训练、微调以及高效推理部署策略。
- 涵盖ML基础设施的关键组件，包括GPU集群管理、网络优化及高性能存储方案。
- 介绍机器学习运维（MLOps）流程，确保模型开发至生产环境的可扩展性与稳定性。
- 包含针对特定硬件架构的性能调优技巧及调试复杂训练问题的实用方法。

3. **适用场景**
- 需要在大规模GPU集群上训练或微调大型语言模型（LLM）的工程团队。
- 希望优化深度学习模型推理延迟并降低计算成本的AI研究人员。
- 正在搭建或维护企业级机器学习平台，需解决可扩展性和稳定性问题的MLOps工程师。
- 初学者或中级从业者希望系统学习机器学习系统工程理论与实践知识的场景。

4. **技术亮点**
- 紧密结合前沿的大语言模型（LLM）应用，内容具有极高的时效性和实战价值。
- 覆盖了从底层硬件（GPU、网络、存储）到上层框架（PyTorch、Transformers）的全栈技术细节。
- 作为“开放书籍”形式，提供了免费且结构化的知识体系，便于社区协作更新与维护。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18436 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17329 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13161 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11583 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10673 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个包含代码实现的AI项目集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它旨在为开发者提供一个全面的学习资源库，通过实际案例展示各类AI技术的应用与实现方式。

2. **核心功能**
- 提供大量基于Python的AI实战代码示例，覆盖主流算法模型。
- 集成计算机视觉与自然语言处理领域的典型应用场景代码。
- 作为系统性的学习路径参考，帮助初学者到进阶者掌握AI开发流程。
- 收录经过验证的项目结构，便于直接复用或修改以适配特定需求。

3. **适用场景**
- AI初学者希望通过阅读和运行代码快速理解机器学习基本概念。
- 数据科学家寻找特定任务（如图像分类、文本生成）的代码参考模板。
- 教育者用于构建人工智能课程的教学案例和实践作业。
- 研究人员希望快速复现经典论文或热门算法的实验结果。

4. **技术亮点**
- 内容覆盖面极广，整合了从传统机器学习到前沿深度学习的广泛技术栈。
- 强调“带代码”的实践导向，每个项目均提供可执行的源代码而非仅理论介绍。
- 高星评级（35590+）表明其在社区中具有较高的认可度和实用性价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35590 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于查看和调试神经网络、深度学习及机器学习模型的可视化工具。它支持多种主流框架生成的模型文件，能够将复杂的模型结构以直观的图形界面展示出来。该工具旨在帮助开发者深入理解模型架构并排查潜在问题。

**2. 核心功能**
*   支持广泛读取包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等在内的多种模型格式。
*   提供清晰的图形化界面，直观展示神经网络的结构、层级连接及数据流向。
*   具备详细的模型信息查看功能，可显示层参数、权重分布及操作符细节。
*   支持模型文件的本地加载与在线预览，方便快速检查模型完整性。
*   允许用户导出模型结构图为图片，便于文档记录或分享交流。

**3. 适用场景**
*   **模型调试**：在训练完成后，通过可视化检查模型结构是否符合预期，发现错误的层连接。
*   **格式转换验证**：在不同框架间转换模型格式（如从 PyTorch 转为 ONNX）后，确认结构一致性。
*   **教学与演示**：向非技术人员或学生展示复杂的神经网络架构，辅助深度学习课程讲解。
*   **部署前审查**：在将模型部署到移动端或嵌入式设备前，分析模型大小和计算复杂度。

**4. 技术亮点**
*   **多格式兼容性强**：无需安装庞大的开发环境即可直接查看模型，极大降低了使用门槛。
*   **轻量级与易用性**：作为纯前端/桌面应用，启动速度快，界面简洁，专注于“查看”而非“编辑”，符合开发者快速诊断的需求。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33249 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究者提供了 essential 的速查表集合，旨在帮助快速回顾关键概念与代码用法。其内容涵盖从基础数学库到主流深度学习框架的核心操作指南。

2. **核心功能**
- 提供深度学习与机器学习领域的关键概念速查。
- 包含常用数据科学库（如 NumPy、SciPy、Matplotlib）的代码片段。
- 覆盖主流深度学习框架（如 Keras）的基础操作指南。
- 以简洁清晰的格式整理，便于研究者快速检索和复习。

3. **适用场景**
- 深度学习初学者快速熟悉常用库和基本语法。
- 研究人员在开发过程中查阅特定函数的用法示例。
- 面试准备或知识复习时作为便捷的参考资料。

4. **技术亮点**
- 高度聚焦于实用代码片段，而非冗长的理论推导。
- 整合了多领域工具链（数据处理、可视化、建模），形成一站式参考。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，汇集了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户轻松入门并具备就业实战能力。内容涵盖Python、数学基础以及机器学习、深度学习、NLP、CV等热门技术领域的主流框架与库。

2. **核心功能**
*   提供结构化的AI学习路径，涵盖从基础编程到高级算法的全套知识体系。
*   收录近200个实战案例和项目代码，强化动手实践能力以对接就业需求。
*   免费提供配套学习教材和资源，降低人工智能领域的学习门槛。
*   整合了Python生态下的主流工具链，如NumPy、Pandas、Matplotlib及各类深度学习框架。

3. **适用场景**
*   希望从零开始系统学习人工智能和机器学习的初学者或转行人员。
*   需要参考大量实战案例来巩固理论知识并提升编码能力的在校学生或自学者。
*   寻求高质量免费教材和清晰学习路线，以快速进入AI行业求职的技术人员。

4. **技术亮点**
*   资源高度整合，一次性覆盖数据科学、深度学习及自然语言处理等多个关键子领域。
*   强调“就业实战”，通过丰富的案例库直接连接理论学习与工业界应用需求。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13161 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11743 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9141 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8933 | 🍴 3103 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6992 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6266 | 🍴 749 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
该项目是一个全面的中英文自然语言处理（NLP）资源汇总库，涵盖了敏感词检测、语言识别、信息抽取（如手机号、身份证、邮箱）、实体识别及知识图谱构建等基础工具。它集成了大量预训练模型（如BERT、GPT）、开源数据集、词向量以及针对特定领域（如医疗、金融、法律）的专业词库和工具包。

2. **核心功能**
*   **基础NLP工具集**：提供分词、词性标注、命名实体识别（NER）、句法分析及情感分析等核心功能的代码实现与模型。
*   **多模态数据处理**：涵盖中文OCR文字识别、语音识别（ASR）语料库、音频数据增强及语音情感分析等资源。
*   **知识图谱与问答系统**：包含中文知识图谱构建工具、基于图谱的问答系统（KBQA）、实体链接及关系抽取方案。
*   **专业领域词库与数据**：提供医疗、金融、法律、汽车、古诗词等领域的专用词库、停用词表及高质量标注数据集。
*   **预训练模型与应用**：汇总了BERT、ALBERT、RoBERTa等主流预训练模型的中文版本及其在文本分类、摘要生成、纠错等任务上的应用代码。

3. **适用场景**
*   **NLP初学者学习与入门**：适合需要快速了解中文NLP生态、查找基础工具链（如jieba、spacy模型）和数据集的学习者。
*   **企业级智能客服与问答系统开发**：开发者可利用其中的对话机器人框架、知识图谱构建工具及意图识别模型，搭建垂直领域的智能问答系统。
*   **垂直行业信息抽取与风控**：金融或法律机构可使用其提供的专业词库、敏感词过滤及实体抽取算法，进行文档自动化处理、风险监测或合规审查。
*   **学术研究与技术调研**：研究人员可通过此库追踪最新的NLP论文复现代码、基准测试数据集及前沿模型（如Transformer变体）的性能对比。

4. **技术亮点**
*   **资源极度丰富且分类清晰**：作为一个“Awesome List”类型的仓库，它几乎囊括了中文NLP领域所有重要的开源项目、数据集和预训练模型，极大降低了资料搜集成本。
*   **覆盖从底层到应用层的全链路**：不仅提供底层的分词、向量化算法，还包含了上层的问答系统、文本生成及知识图谱构建，支持端到端的解决方案参考。
*   **紧跟前沿技术迭代**：持续更新包括BERT、GPT-2、ALBERT、ELECTRA等最新预训练语言模型在中文场景下的适配与应用，确保技术栈的时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81930 | 🍴 15249 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73403 | 🍴 8961 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52494 | 🍴 10631 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- **1. 中文简介**
该项目是一个综合性的AI学习资源库，涵盖数据分析、机器学习实战、线性代数基础以及PyTorch和TensorFlow 2等主流框架的应用。它结合NLTK自然语言处理工具，为学习者提供从理论到实践的完整知识体系。

**2. 核心功能**
*   集成经典机器学习算法（如SVM、KMeans、AdaBoost）与深度学习模型（如RNN、LSTM、DNN）的代码实现。
*   提供基于Scikit-learn和PyTorch的数据挖掘及推荐系统实战案例。
*   包含线性代数数学基础讲解及NLP自然语言处理专项模块。

**3. 适用场景**
*   希望系统掌握机器学习全流程（从数据预处理到模型评估）的初学者。
*   需要参考具体代码实现来理解深度学习架构（如LSTM、RNN）的研究人员或工程师。
*   致力于构建推荐系统或进行文本挖掘分析的开发者。

**4. 技术亮点**
*   多框架支持：同时涵盖传统机器学习库（Sklearn）与现代深度学习框架（PyTorch/TF2）。
*   算法覆盖全面：标签显示其包含了从关联规则挖掘（FP-Growth/Apriori）到降维（PCA/SVD）的多种经典算法。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42398 | 🍴 11534 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- ### 1. 中文简介
该项目旨在通过从头构建的方式，深入讲解并实践人工智能工程的核心知识。它提供了一个完整的课程体系，帮助开发者掌握从基础理论到实际部署的全流程技能。最终目标是让学习者能够独立开发并向他人交付高质量的AI应用。

### 2. 核心功能
*   **全栈AI工程实践**：涵盖从数据预处理、模型训练到最终部署上线的完整开发链路。
*   **多模态技术整合**：集成自然语言处理、计算机视觉及生成式AI等多种前沿技术的实战案例。
*   **智能体与强化学习**：深入探索AI Agent、多智能体协作及强化学习等高级主题。
*   **跨语言技术栈支持**：不仅限于Python，还结合Rust和TypeScript优化性能与前端交互。
*   **系统化课程结构**：提供结构化的教程路径，适合希望系统建立AI知识体系的学习者。

### 3. 适用场景
*   **AI工程师进阶学习**：希望深入理解LLM、Transformer底层原理并提升工程落地能力的开发者。
*   **复杂系统架构设计**：需要构建基于Agent、多模态或混合语言栈的高性能AI应用团队。
*   **高校与企业培训**：作为人工智能工程化实战课程的教材或内部技术培训资料。
*   **个人项目原型开发**：想要快速从零搭建可运行、可部署的生成式AI原型的独立创作者。

### 4. 技术亮点
*   **MCP协议支持**：引入Model Context Protocol (MCP) 以增强AI模型与外部工具/数据的连接能力。
*   **高性能语言融合**：结合Rust用于关键性能模块，提升整体系统的执行效率。
*   **Swarm Intelligence（群体智能）**：展示如何利用多智能体协作解决复杂问题，体现前沿架构思路。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 40831 | 🍴 6769 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35590 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33756 | 🍴 4697 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28734 | 🍴 3509 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25961 | 🍴 2942 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21729 | 🍴 3306 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个收录了500个AI相关代码项目的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它旨在为开发者提供丰富的实战案例和代码参考，是人工智能学习资源库。

2. **核心功能**
*   提供500个完整的AI项目代码示例，覆盖主流技术栈。
*   分类整理机器学习、深度学习、CV及NLP等核心领域的项目。
*   作为Awesome列表，筛选并推荐高质量的人工智能开源项目。
*   集成Python语言为主的实用工具包，便于快速上手实践。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习基础。
*   数据科学家寻找特定领域（如图像识别或文本处理）的代码模板以加速开发。
*   研究人员需要查阅最新的AI应用案例以获取灵感或验证想法。

4. **技术亮点**
*   规模庞大且分类清晰，一站式解决多领域AI项目查找需求。
*   包含“Awesome”精选标签，确保项目质量较高且具有代表性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35590 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### Skyvern 项目分析

**1. 中文简介**
Skyvern 是一款基于人工智能的自动化平台，旨在通过模拟人类操作来执行复杂的浏览器工作流。它利用大语言模型（LLM）和计算机视觉技术，能够理解网页内容并自主完成表单填写、数据抓取等任务，无需预先编写繁琐的脚本。

**2. 核心功能**
*   **AI 驱动的工作流自动化**：结合 LLM 与视觉识别技术，智能解析网页结构并执行操作，实现“零代码”或“低代码”自动化。
*   **跨平台浏览器兼容**：底层支持 Playwright 和 Puppeteer 等主流自动化工具，确保在不同浏览器环境下的稳定运行。
*   **动态页面处理能力**：具备处理动态加载内容、弹窗及复杂交互逻辑的能力，比传统 Selenium 方案更适应现代 Web 应用。
*   **可视化工作流编排**：提供清晰的 API 接口和工作流定义方式，便于开发者将自动化任务集成到现有业务系统中。
*   **高可靠性与容错**：内置错误恢复机制，当页面元素发生变化时能自动调整策略，提高任务执行成功率。

**3. 适用场景**
*   **RPA 替代方案**：用于替代传统规则-based RPA（如 Power Automate），处理非结构化或频繁变化的网页交互任务。
*   **大规模数据采集**：从电商、新闻或社交媒体网站自动提取商品、价格、评论等结构化数据。
*   **自动化测试与 QA**：模拟真实用户行为对 Web 应用进行端到端的功能测试和回归测试。
*   **企业内部流程自动化**：自动登录内部系统、填写报销单、更新 CRM 记录等重复性行政工作。

**4. 技术亮点**
*   **多模态 AI 融合**：创新性地结合了自然语言理解（LLM）和计算机视觉（Vision），使机器不仅能“读懂”文字，还能“看懂”界面布局。
*   **通用性强**：不依赖特定网站的 DOM 结构，而是通过语义理解进行操作，显著降低了维护自动化脚本的成本。
*   **开源生态整合**：作为开源项目，它提供了灵活的 API，易于与企业现有的 Python 技术栈和 CI/CD 流程集成。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22532 | 🍴 2112 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的标注。它提供开源、云端和企业级产品，并集成 AI 辅助标注、质量保证及团队协作等功能。此外，该项目还通过开发者 API 和标签服务，全面赋能计算机视觉与深度学习应用。

2. **核心功能**
*   支持图像、视频和 3D 数据的多模态标注，涵盖边界框、语义分割等任务。
*   内置 AI 辅助标注工具，显著提升数据集制作效率并降低人工成本。
*   提供完善的质量保证机制与团队协同工作流，确保标注数据的准确性。
*   开放开发者 API 接口，便于与企业现有系统或自动化流水线集成。

3. **适用场景**
*   为物体检测任务构建包含边界框标注的高质量训练数据集。
*   进行语义分割或实例分割研究，需要像素级精细标注的视频或图像数据。
*   大型团队协作开发视觉 AI 模型，需集中管理标注流程与质量控制。

4. **技术亮点**
*   兼容主流深度学习框架（如 PyTorch、TensorFlow），无缝对接 Imagenet 等标准数据集规范。
*   提供从开源本地部署到云化、企业级的灵活产品形态，适应不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16344 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### 1. 中文简介
pytorch-grad-cam 是一个先进的计算机视觉可解释性AI库，旨在增强模型决策过程的透明度。它广泛支持卷积神经网络（CNN）、视觉Transformer等多种架构，涵盖分类、检测及分割等任务。该项目通过生成可视化热力图，帮助用户深入理解深度学习模型的内部工作机制。

### 2. 核心功能
*   支持多种主流网络架构，包括CNN和Vision Transformers。
*   兼容多种计算机视觉任务，如图像分类、目标检测和语义分割。
*   实现多种梯度加权类激活映射算法，如Grad-CAM、Score-CAM等。
*   提供直观的可视化效果，用于展示模型关注的图像区域。

### 3. 适用场景
*   **模型调试与优化**：通过分析热力图定位模型误判原因，辅助改进网络结构。
*   **医疗影像分析**：可视化医生关注的病灶区域，提升诊断结果的信任度。
*   **安全与合规审计**：满足AI系统的可解释性要求，确保决策过程透明可控。

### 4. 技术亮点
*   高度模块化设计，易于集成到现有的PyTorch项目中。
*   社区活跃度高（近1.3万星标），拥有完善的文档和示例代码。
*   统一接口支持多种XAI（可解释AI）方法，便于算法对比研究。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12921 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专注于空间人工智能（Spatial AI）的几何计算机视觉库。它基于 PyTorch 构建，旨在为深度学习模型提供可微分的图像处理与几何计算能力。该项目致力于简化计算机视觉算法在神经网络中的集成与优化过程。

2. **核心功能**
*   提供全套可微分的几何计算机视觉算子，支持反向传播。
*   内置丰富的图像处理增强工具，如滤波、色彩空间转换和几何变换。
*   兼容 PyTorch 生态系统，便于直接嵌入现有的深度学习工作流。
*   包含多种经典视觉算法的实现，如相机标定、姿态估计和三维重建辅助工具。

3. **适用场景**
*   需要集成传统计算机视觉预处理步骤到端到端深度学习管道的项目。
*   涉及机器人导航或自动驾驶等领域的空间感知与几何推理任务。
*   进行图像风格迁移、超分辨率生成等依赖精确几何变换的创意 AI 应用。
*   开发需要实时处理视频流或图像序列并进行可微分分析的研究原型。

4. **技术亮点**
*   **完全可微分设计**：所有操作均支持梯度计算，无缝对接 PyTorch 自动微分机制。
*   **硬件加速优化**：底层算子针对 GPU 和 TPU 进行了高度优化，提升大规模数据处理效率。
*   **模块化架构**：提供从基础像素操作到高级几何算法的模块化组件，易于扩展和定制。
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1204 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3459 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3287 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2428 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383625 | 🍴 80591 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 258328 | 🍴 23021 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的 GitHub 项目信息，以下是关于 **hermes-agent** 的技术分析报告：

1. **中文简介**
   Hermes-Agent 是一款伴随用户共同成长的智能代理工具。它旨在通过持续的学习与交互，动态适应个人工作流并提升效率。该项目代表了下一代自主 AI 助手的发展方向。

2. **核心功能**
   - 具备随时间推移不断进化能力，能够根据用户习惯优化表现。
   - 深度集成主流大语言模型（如 Anthropic 的 Claude 和 OpenAI 的 GPT）。
   - 提供类似 Codex 或 ClawdBot 的高级代码生成与处理能力。
   - 支持多代理协作架构，可处理复杂的自动化任务链条。

3. **适用场景**
   - 开发者日常代码编写、调试及重构辅助。
   - 复杂数据分析和自动化报告生成的工作流。
   - 需要长期记忆和个性化配置的个人生产力助手搭建。

4. **技术亮点**
   - 采用模块化设计，灵活支持 OpenAI、Anthropic 等多后端 LLM 切换。
   - 拥有极高的社区关注度（近 22 万星标），证明其架构的成熟度与实用性。
   - 标签中涵盖 Nous Research 等知名研究组织，暗示其在开源社区和学术前沿的影响力。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 217953 | 🍴 41154 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款基于公平代码协议的工作流自动化平台，原生支持 AI 能力。它允许用户结合可视化构建与自定义代码，提供超过 400 种集成选项，并支持自托管或云端部署。

2. **核心功能**
*   提供可视化工作流构建器，降低自动化开发门槛。
*   内置原生 AI 功能，支持智能任务处理与分析。
*   拥有 400 多种预置集成，实现系统间无缝连接。
*   支持混合开发模式，可结合自定义代码进行复杂逻辑扩展。
*   提供灵活的部署方案，包括自托管和云服务两种选择。

3. **适用场景**
*   企业级数据同步与 API 集成自动化。
*   利用 AI 增强业务逻辑的智能工作流编排。
*   开发者快速搭建低代码/无代码内部工具。
*   需要数据隐私保护而选择自托管自动化平台的公司。

4. **技术亮点**
*   采用 TypeScript 开发，确保类型安全与高性能。
*   支持 MCP (Model Context Protocol) 客户端与服务端，强化 AI 上下文交互能力。
*   具备 CLI 工具，便于自动化部署与管理。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197270 | 🍴 59492 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. **中文简介**
AutoGPT 旨在让每个人都能轻松获取、使用并构建人工智能应用，实现 AI 的普及化愿景。其使命是提供强大的工具链，让用户能够专注于真正重要的任务，而非被繁琐的技术细节所困扰。

### 2. **核心功能**
- **自主代理执行**：作为自主智能体，能独立规划、分解并执行复杂的多步骤任务。
- **多模型支持**：兼容 OpenAI (GPT)、Claude、Llama API 等多种主流大语言模型接口。
- **自我反思与优化**：具备自我评估机制，能在执行过程中检查错误并调整策略以提高成功率。
- **互联网与工具集成**：可连接浏览器、文件系统及其他外部工具，实现信息检索和操作系统的交互。

### 3. **适用场景**
- **自动化工作流**：处理需要多步操作的任务，如自动网页调研、数据收集与信息整理。
- **代码开发与调试**：辅助程序员进行代码生成、重构或自动化测试脚本的执行。
- **内容创作与研究**：用于长篇报告生成、SEO 内容优化或跨平台的信息聚合分析。

### 4. **技术亮点**
- **高度可扩展的 Agent 架构**：基于模块化设计，允许开发者轻松添加自定义插件和工具。
- **开源社区驱动**：拥有极高的 GitHub 星标数（超 18 万），意味着活跃的社区支持和持续的功能迭代。
- **多 LLM 后端灵活切换**：不绑定单一厂商，降低对特定 API 服务的依赖风险。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185629 | 🍴 46071 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166093 | 🍴 21470 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164262 | 🍴 30426 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157157 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 153674 | 🍴 8773 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152122 | 🍴 9613 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

