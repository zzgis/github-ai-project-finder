# GitHub AI项目每日发现报告
日期: 2026-06-26

## 新发布的AI项目

### claude-ai-desktop-app
- 1. **中文简介**
该项目是一个开源的 Claude Code 桌面应用程序，支持 Windows、Linux 和 macOS 平台。它旨在通过本地 LLM 路由、代理服务器及多种 AI 后端（如 Anthropic API、NVIDIA NIM、OpenRouter 等），为用户提供免费的 AI 编码助手体验。

2. **核心功能**
*   跨平台桌面客户端，原生支持主流操作系统。
*   集成多模型路由，可灵活切换 Anthropic API、本地 Ollama/LM Studio 或第三方服务。
*   提供 VS Code 和 JetBrains 插件扩展，无缝嵌入开发环境。
*   内置 CLI 终端工具，支持命令行直接调用 AI 辅助编程。
*   支持自定义主题与任务管理，优化开发者工作流。

3. **适用场景**
*   希望在不依赖官方付费 API 的情况下，在本地运行 Claude Code 功能的开发者。
*   需要统一界面管理多个 AI 后端（如同时使用本地模型和云端 API）的团队或个人。
*   偏好桌面原生应用而非纯浏览器或 IDE 插件形式的 AI 编码助手用户。
*   对隐私敏感，希望通过本地部署（Local LLM Router）处理代码数据的用户。

4. **技术亮点**
*   采用 TypeScript 开发，确保类型安全与高性能交互。
*   实现了灵活的“模型路由器”架构，兼容 Anthropic、DeepSeek、Ollama 等多种接口标准。
*   提供从桌面端到 IDE 插件再到 CLI 的全栈覆盖，满足不同层级开发需求。
- 链接: https://github.com/samuto69/claude-ai-desktop-app
- ⭐ 101 | 🍴 0 | 语言: TypeScript
- 标签: claude-code, claude-code-action, claude-code-api, claude-code-desktop, claude-code-open

### GITVERSE
- ### 1. **中文简介**
GITVERSE 是一款能够逆向工程任何代码库的工具，可将其转化为构建提示词。它自动生成架构分解、ASCII 蓝图以及供 AI 就绪的重构提示。

### 2. **核心功能**
*   **代码库逆向工程**：自动分析项目结构并提取关键架构信息。
*   **可视化蓝图生成**：输出清晰的 ASCII 艺术风格架构图以辅助理解。
*   **AI 提示词优化**：生成专门针对 LLM（如 Claude、OpenAI）优化的重构提示。
*   **多模型兼容支持**：无缝对接主流大语言模型进行代码分析与重建。
*   **开发者工具集成**：通过 GitHub API 实现快速的项目抓取与分析流程。

### 3. **适用场景**
*   **接手遗留项目**：快速理解陌生或文档缺失的代码库整体架构。
*   **AI 辅助重构**：为大语言模型提供精准上下文，以执行大规模代码重构。
*   **技术文档自动化**：自动生成可视化的架构概览和结构说明。
*   **代码迁移准备**：在迁移框架或语言前，全面梳理现有依赖与结构。

### 4. **技术亮点**
*   基于 TypeScript 和 Next.js 构建，具备高性能与现代 Web 体验。
*   结合 Prompt Engineering 技巧，显著提升 LLM 对代码理解的准确性。
*   利用 Tailwind CSS 提供直观且响应式的用户界面。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 101 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### parsehawk
- 描述: Local-first document AI. Run 100% locally by default, with API, CLI, and Web UI.
- 链接: https://github.com/parsehawk/parsehawk
- ⭐ 23 | 🍴 4 | 语言: Python
- 标签: artificial-intelligence, classification, document-ai, document-processing, extraction

### glm-5.2-free-desktop-app
- **1. 中文简介**
这是一个基于C#开发的桌面应用程序，旨在为Windows、macOS和Linux用户提供免费的GLM系列大语言模型（如GLM-5.2）本地运行环境。该项目集成了多种LLM推理后端（如unsloth、llama.cpp、ollama等），支持长上下文窗口及自主代理编程功能，致力于降低开发者使用智谱AI模型的门槛。

**2. 核心功能**
*   **多平台本地部署**：支持在Windows、macOS和Linux系统上一键下载、安装并运行GLM系列模型。
*   **灵活推理后端集成**：兼容llama.cpp、Ollama、Unsloth等多种开源推理引擎，动态加载GGUF格式模型。
*   **智能编程代理**：具备代码辅助、自主代理（Autonomous Agent）及长 Horizon 任务处理能力，提升开发效率。
*   **免费API访问**：提供对GLM模型API的免费访问接口，便于开发者集成到现有工作流中。
*   **超长上下文支持**：支持高达1M tokens的上下文窗口，适用于处理大规模代码库或长文档分析。

**3. 适用场景**
*   **离线编程助手**：开发者在断网环境下使用本地部署的GLM模型进行代码生成、调试和重构。
*   **长文档/代码库分析**：利用其1M上下文窗口优势，快速检索和分析大型软件项目或长篇技术文档。
*   **自动化Agent研究**：研究人员或高级用户搭建基于GLM的自主代理，执行复杂的自动化任务或基准测试（如SWE-Bench）。
*   **低成本模型集成**：初创团队或个人开发者在不支付高昂API费用的前提下，体验智谱AI最新大模型能力。

**4. 技术亮点**
*   **跨平台统一封装**：通过C#编写原生桌面应用，屏蔽了底层不同推理后端（llama.cpp/Ollama等）的配置差异，实现“开箱即用”。
*   **动态模型适配**：支持动态切换和加载不同版本的GLM模型及量化格式（GGUF），兼顾性能与硬件兼容性。
*   **全栈AI工具链整合**：将模型下载、安装、API调用及Agent运行逻辑深度整合在一个轻量级桌面应用中，简化了传统LLM部署的复杂流程。
- 链接: https://github.com/PROGRMGEEK/glm-5.2-free-desktop-app
- ⭐ 20 | 🍴 0 | 语言: C#
- 标签: ai-desktop, desktop-agent, desktop-ai, free-ai-api, free-ai-coding

### deepseek-v4-pro-flash-desktop-app
- 描述: deepseek-v4-pro-flash deepseek ai large language model llm mixture of experts moe 1m context window hybrid attention architecture compressed sparse attention csa heavily compressed attention hca manifold constrained hyper deepseek-v4-pro deepseek-v4-flash open source hugging face github repository api access local llm inference vllm ollama
- 链接: https://github.com/HiyuCat/deepseek-v4-pro-flash-desktop-app
- ⭐ 20 | 🍴 0 | 语言: TypeScript
- 标签: ai-free, deep-seek, deepseek-api, deepseek-app, deepseek-chat

### sw2api
- 描述: Reverse proxy for your ai quota from the SW platform.
- 链接: https://github.com/bgzhang1/sw2api
- ⭐ 15 | 🍴 3 | 语言: Python

### ai-coding-deals
- 描述: Money-saving guide to AI coding tools: free tiers, discounts, referral credits & open-source alternatives. 省钱指南。
- 链接: https://github.com/codertesla/ai-coding-deals
- ⭐ 14 | 🍴 0 | 语言: Python
- 标签: ai, ai-coding, ai-tools, awesome-list, claude-code

### memlawb
- 描述: Open-source, self-hostable, zero-knowledge memory for AI agents. End-to-end encrypted — the server stores only ciphertext and can't read your agent's memory. Works with any MCP agent .
- 链接: https://github.com/Gitlawb/memlawb
- ⭐ 9 | 🍴 3 | 语言: TypeScript

### go-openlore
- 描述: OpenLore: serve your docs to AI agents over SSH
- 链接: https://github.com/aakarim/go-openlore
- ⭐ 8 | 🍴 0 | 语言: Go

### skills
- 描述: Public AI skills: small, useful agent workflows you can try today.
- 链接: https://github.com/JorrrrrdDin/skills
- ⭐ 8 | 🍴 0 | 语言: Python
- 标签: agent-workflows, ai-skills, claude-skills, codex-skills, knowledge-graph

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
该项目是一个全面的中英文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。它不仅提供了丰富的行业垂直词库（如汽车、医疗、法律、古诗词）和情感分析资源，还汇总了大量前沿的NLP数据集、预训练模型（如BERT、GPT）及开源工具链。作为一个资源聚合型项目，它旨在为开发者提供从数据清洗、特征工程到模型训练的一站式解决方案。

### 2. 核心功能
*   **基础NLP工具**：提供敏感词过滤、中英文语言检测、停用词表、反动词表及繁简体转换等实用文本处理功能。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、地址等敏感信息的自动抽取，以及基于依存句法和语义角色的事件三元组抽取。
*   **丰富词库与知识图谱**：内置中日文人名库、职业/品牌/地名/成语词库，并整合了清华大学XLORE等大规模中英文跨语言百科知识图谱资源。
*   **深度学习模型与资源汇总**：汇集了BERT、ERNIE、ALBERT等主流预训练语言模型，以及各类中文NLP竞赛方案、数据集和代码实现。
*   **语音与OCR支持**：包含中文语音识别（ASR）数据集、语音情感分析工具、中文OCR识别库（cnocr）及音频数据处理增强库。

### 3. 适用场景
*   **风控与安全审核**：利用敏感词库、暴恐词表及匿名实体抽取功能，构建内容安全审核系统，识别违规文本和隐私泄露风险。
*   **智能客服与对话系统**：基于提供的闲聊语料、意图识别数据集及Rasa/ConvLab等框架，快速搭建具备多轮对话能力的智能客服或聊天机器人。
*   **垂直领域知识挖掘**：结合医疗、法律、金融等领域的专用词库和NER模型，进行行业文档的结构化信息提取和知识图谱构建。
*   **NLP算法研究与教学**：作为学习和复现最新NLP算法（如BERT微调、文本摘要、序列标注）的资源仓库，适合研究人员和学生进行基准测试。

### 4. 技术亮点
*   **资源聚合度高**：不仅包含代码库，还整理了大量高质量的中英文NLP数据集、论文解读及竞赛Top方案，是入门和进阶的优质资料库。
*   **全栈覆盖能力**：从底层的文本清洗、分词、词向量，到中层的实体抽取、情感分析，再到上层的问答系统、文本生成均有涵盖。
*   **紧跟前沿技术**：持续更新包括Transformers、BERT、GPT-2、ALBERT等最新预训练模型的应用案例和微调代码，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81450 | 🍴 15246 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例和源码参考。

2. **核心功能**
- 提供大量涵盖主流AI领域的完整项目代码示例。
- 分类清晰，便于用户快速定位特定方向的学习资源。
- 包含从基础到进阶的多层次实践案例。
- 支持Python等常用语言进行算法实现与验证。

3. **适用场景**
- AI初学者通过实战项目快速掌握核心概念。
- 研究人员寻找特定领域的参考实现或灵感。
- 开发者构建个人作品集以展示技术能力。
- 企业团队进行技术选型前的概念验证。

4. **技术亮点**
- 内容全面，覆盖人工智能主要分支领域。
- 高星项目，拥有庞大的社区认可度和参考价值。
- 提供即插即用的代码结构，降低复现门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34884 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地理解模型结构和数据流向。

2. **核心功能**
*   支持导入并可视化多种模型格式，包括 ONNX、PyTorch、TensorFlow、Keras 和 CoreML 等。
*   提供清晰的图层结构树状视图，便于逐层检查网络架构细节。
*   具备交互式图表功能，可动态展示张量形状、参数数值及权重分布。
*   兼容桌面应用与在线浏览器版本，无需安装即可快速查看模型文件。
*   支持将模型可视化结果导出为静态图片或 SVG 矢量图用于文档记录。

3. **适用场景**
*   **模型调试**：在训练或部署前检查网络结构是否正确，排查维度不匹配等问题。
*   **学术交流与汇报**：生成高质量的模型架构图，用于论文插图或技术分享演示。
*   **跨框架迁移验证**：对比不同框架下同一算法的结构差异，确保转换过程无损。
*   **教学演示**：帮助初学者直观理解卷积层、池化层等组件在深度网络中的连接方式。

4. **技术亮点**
*   拥有极高的社区认可度（3万+星标），是业界标准的模型可视化工具之一。
*   广泛兼容从传统机器学习到最新大语言模型（如 Safetensors 格式）的各种后端格式。
*   采用 Web 技术栈开发，实现了良好的跨平台兼容性和轻量级部署体验。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33132 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21048 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
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
- ⭐ 15411 | 🍴 3392 | 语言: 未知
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
- ### 1. 中文简介
该项目是一个精选的 AI、机器学习、深度学习、计算机视觉及自然语言处理项目集合，包含大量附带代码的实战案例。它旨在为开发者提供全面的技术参考和学习资源，覆盖从基础到高级的多种应用场景。作为一个高星标的“Awesome”列表，它是探索人工智能领域最新实践的重要入口。

### 2. 核心功能
- **多领域覆盖**：整合了机器学习、深度学习、计算机视觉和自然语言处理等多个 AI 子领域的实战项目。
- **代码集成**：每个推荐的项目均附带源代码，方便用户直接运行、学习和修改。
- **分类清晰**：通过标签对不同类型的 AI 项目进行系统化整理，便于快速检索和定位。
- **社区精选**：作为“Awesome”列表，收录了经过社区验证的高质量和高人气项目。
- **免费开放**：所有资源和代码均为开源免费，降低了学习和研究门槛。

### 3. 适用场景
- **初学者入门**：适合 AI 初学者通过阅读和运行代码，快速理解各子领域的基本概念和应用。
- **技术调研**：帮助研究人员和工程师快速了解当前 AI 领域的热门项目和最新进展。
- **实战开发参考**：为开发者提供可复用的代码模板和项目架构，加速实际项目的开发进程。
- **课程教学资源**：教师或培训师可将其作为补充教材，提供丰富的案例以增强教学效果。

### 4. 技术亮点
- **综合性强**：在一个列表中涵盖了 AI 领域的多个关键分支，提供了全面的学习路径。
- **高活跃度**：拥有超过 34,000 个星标，表明其在开发者社区中具有很高的认可度和影响力。
- **实用导向**：侧重于带有代码的实战项目，而非纯理论文章，更贴近实际应用需求。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34884 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33132 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心知识速查表（Cheat Sheets）。内容涵盖从基础数学库到主流框架的关键用法，旨在帮助研究者快速回顾和查阅关键技术细节。

2. **核心功能**
- 提供深度学习与机器学习领域的关键概念速查指南。
- 汇总了 Numpy、Scipy、Matplotlib 等核心数据科学库的常用函数与用法。
- 包含 Keras 等主流深度学习框架的代码示例与配置说明。
- 以结构化文档形式呈现，便于快速检索和理解复杂算法逻辑。

3. **适用场景**
- 机器学习研究人员在开发模型时快速回顾 API 用法或数学原理。
- 初学者在入门阶段建立对核心工具链（如 NumPy、Keras）的整体认知。
- 工程师在进行技术选型或代码审查时作为快速参考手册。
- 备考或面试准备中，用于梳理深度学习领域的基础知识点。

4. **技术亮点**
- 高度聚焦于“速查”特性，去除了冗长的理论推导，直接呈现关键代码与公式。
- 整合了从底层数值计算（NumPy/SciPy）到高层抽象（Keras/ML）的全栈技术点。
- 拥有极高的社区认可度（1.5万+星标），证明其内容的实用性和权威性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，涵盖 Python、数学及各大主流 AI 框架。项目整理了近 200 个实战案例与免费配套教材，旨在帮助零基础用户系统入门并掌握就业所需的实战技能。

2. **核心功能**
- 提供从基础到进阶的系统化 AI 学习路径与资源索引。
- 收录近 200 个涵盖机器学习、深度学习等领域的实战代码案例。
- 配套免费教材与学习资料，支持零基础平滑过渡至就业水平。
- 覆盖计算机视觉、自然语言处理、数据分析等热门细分领域。

3. **适用场景**
- AI 初学者希望获得结构化学习路径以替代碎片化搜索。
- 求职者需要通过大量实战项目积累面试作品与工程经验。
- 数据科学家或算法工程师寻找特定技术栈（如 PyTorch/TensorFlow）的参考实现。

4. **技术亮点**
- 资源高度集成，将理论框架、热门工具库与实战案例一站式整合。
- 强调“零基础”友好性，通过配套教材降低 AI 领域的入门门槛。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13089 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化流程，降低了开发门槛，使研究人员和工程师能更高效地训练和微调模型。

### 2. **核心功能**
*   **低代码/无代码建模**：支持通过 YAML 配置文件快速定义模型架构，无需编写大量底层代码。
*   **广泛的模态支持**：原生处理表格、文本、图像、音频等多种数据类型，适用于多模态任务。
*   **自动化训练与微调**：内置优化的训练管道，轻松对接 PyTorch 等后端进行模型微调（Fine-tuning）。
*   **可解释性与数据驱动**：强调以数据为中心（Data-centric），提供可视化分析工具以增强模型透明度。

### 3. **适用场景**
*   **快速原型开发**：希望迅速验证 AI 想法或构建基础模型的研究人员。
*   **企业级模型部署**：需要标准化、可维护且易于协作的 AI 模型构建流程的工程团队。
*   **多模态应用构建**：涉及文本、图像或表格数据混合处理的复杂机器学习项目。

### 4. **技术亮点**
*   **基于 PyTorch 的后端优化**：充分利用 PyTorch 生态系统的灵活性，同时屏蔽底层复杂性。
*   **声明式 API 设计**：通过简单的配置即可实现复杂的神经网络结构，极大提升了开发效率。
*   **开箱即用的预处理**：内置针对各类数据类型的标准化预处理模块，减少数据清洗的工作量。
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
- ### 1. 中文简介
该项目是一个汇集了大量中文自然语言处理（NLP）资源、数据集、工具库及预训练模型的综合性开源仓库。它涵盖了从基础文本处理（如敏感词过滤、分词、实体抽取）到高级应用（如知识图谱构建、对话系统、语音识别）的全方位内容，旨在为开发者提供一站式的NLP开发支持。

### 2. 核心功能
*   **基础文本处理与清洗**：提供敏感词检测、繁简转换、停用词、同反义词库、情感分析及数据增强工具，并支持中英文及中日文人名、身份证、手机号等关键信息的自动抽取。
*   **预训练模型与词向量**：集成了BERT、ALBERT、RoBERTa、ELECTRA等多种主流中文预训练语言模型，以及Word2Vec、GloVe等词向量资源，支持NER、文本分类、序列标记等任务。
*   **知识图谱与问答系统**：包含多个领域的知识图谱构建案例（如医疗、金融、百科），提供关系抽取、实体链接、三元组抽取工具，以及基于检索或生成的问答系统资源和代码。
*   **语音与多媒体NLP**：涵盖中文语音识别（ASR）数据集、音素对齐工具、语音情感分析、OCR文字识别（特别是中文手写和表格），以及音频数据增广库。
*   **垂直领域资源与评测基准**：整理了医疗、法律、财经、汽车、IT等特定领域的词库和数据集，并提供了中文NLP任务的评测基准、排行榜及竞赛优秀方案汇总。

### 3. 适用场景
*   **构建中文智能客服与聊天机器人**：利用项目中的对话语料、意图识别模型、多轮对话数据集及开源框架（如Rasa, ConvLab），快速开发具备语义理解和生成能力的智能对话系统。
*   **企业级信息抽取与文档自动化处理**：使用其中的命名实体识别（NER）、关系抽取、关键词提取及OCR工具，从非结构化文本（如新闻、合同、简历、医疗记录）中自动化提取结构化知识。
*   **文本安全审核与内容风控**：借助内置的敏感词库、暴恐词表、反动词表及情感分析模型，对用户生成内容（UGC）进行实时的违规检测和风险分级。
*   **NLP算法研究与模型微调**：研究者可以利用项目提供的各类基准数据集、预训练模型代码及评测指标，进行模型对比实验、新算法验证或针对特定领域（如医疗、法律）的微调优化。

### 4. 技术亮点
*   **资源极度丰富且全面**：不仅包含代码，还整合了海量的高质量数据集、预训练模型权重、专业领域词典及学术资料，是中文NLP领域的“百科全书”。
*   **紧跟前沿技术演进**：涵盖了从传统机器学习方法到最新的Transformer架构（BERT, GPT-2, ALBERT等）及知识图谱表示学习的最新进展和复现代码。
*   **注重实用性与落地性**：提供了大量开箱即用的工具包（如jieba加速版、HanLP、Jiagu等）和实际业务场景下的解决方案（如简历解析、表格提取、语音合成），降低了开发门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81450 | 🍴 15246 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目在 ACL 2024 会议上发表，旨在简化从指令微调到强化学习对齐的全流程开发体验。

### 2. 核心功能
*   **多模型兼容**：原生支持 LLaMA、Qwen、Gemma、DeepSeek 等100多种大模型的统一接入。
*   **高效微调策略**：内置 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）算法，降低显存占用。
*   **全链路训练支持**：覆盖监督微调（SFT）、奖励模型训练（RM）、PPO 强化学习（RLHF）及 DPO 直接偏好优化。
*   **量化部署集成**：提供 INT4/INT8 量化训练与推理支持，便于在资源受限环境下部署。
*   **可视化交互界面**：自带 Web UI 和 CLI 工具，方便用户进行数据管理、训练监控及模型评估。

### 3. 适用场景
*   **企业级私有化部署**：利用 QLoRA 等技术，在单卡或少量 GPU 上快速微调开源模型以适应特定业务需求。
*   **多模态应用开发**：通过统一框架同时处理文本生成与图像理解任务，加速 VLM 模型的迭代与训练。
*   **学术研究实验**：作为标准化的微调基准平台，用于复现最新论文中的指令跟随或对齐算法效果。

### 4. 技术亮点
*   **统一架构设计**：屏蔽了不同模型底层实现的差异，实现“一套代码适配百种模型”的高效开发模式。
*   **前沿算法集成**：率先整合了 DPO、ORPO 等最新对齐算法以及 MoE（混合专家）模型的高效训练方案。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72499 | 🍴 8866 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI。项目采用Jupyter Notebook形式编写，内容涵盖从基础机器学习到深度学习及自然语言处理等多个领域。该课程由Microsoft发起，致力于提供结构清晰、易于上手的AI教育资料。

2. **核心功能**
*   提供系统化的12周学习计划，将复杂的AI概念分解为24个独立课时。
*   基于Jupyter Notebook实现交互式编程教学，便于读者边学边练。
*   覆盖广泛的技术栈，包括机器学习、计算机视觉（CNN）、生成对抗网络（GAN）、RNN及自然语言处理（NLP）。
*   面向初学者设计，强调“人人可学”的理念，降低AI入门门槛。

3. **适用场景**
*   零基础用户希望系统性地了解人工智能基本原理和应用场景。
*   学生或教育工作者用于课堂教学或自学参考，构建完整的AI知识体系。
*   开发者希望快速上手并实践Python在AI领域的具体编码实现。

4. **技术亮点**
*   高度模块化课程设计，结合理论讲解与代码实战，兼顾学习与动手能力。
*   依托Jupyter Notebook环境，支持即时反馈和可视化演示，提升学习效率。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48452 | 🍴 10052 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- **1. 中文简介**
该项目收集并提取了包括 Anthropic Claude、OpenAI ChatGPT/GPT、Google Gemini 以及 xAI Grok 等主流大模型的系统提示词（System Prompts）。内容涵盖 Claude Code、Cursor、VS Code 等多种 AI 代理及开发工具，并保持定期更新。它旨在为研究人员和开发者提供一个全面的提示词工程参考库。

**2. 核心功能**
*   **多厂商提示词聚合**：整合了 Anthropic、OpenAI、Google 和 xAI 等头部 AI 公司的底层系统指令。
*   **覆盖广泛模型与工具**：不仅包含基础语言模型（如 Opus 4.8, GPT 5.5），还涉及代码辅助工具（如 Codex, Cursor）。
*   **持续动态更新**：项目维护者定期同步最新泄露或公开的系统提示词版本。
*   **结构化数据展示**：以清晰的目录和代码形式组织复杂的提示词内容，便于阅读和复用。

**3. 适用场景**
*   **提示词工程研究**：分析不同大模型的指令遵循机制和思维链（CoT）构建方式。
*   **安全与红队测试**：通过了解系统底层指令，评估模型在对抗性攻击下的鲁棒性和安全性。
*   **AI 应用开发优化**：借鉴官方最佳实践，优化自定义 Agent 或聊天机器人的系统提示词设计。
*   **教育与学习**：作为理解大型语言模型内部运作逻辑和 prompt engineering 技巧的教学材料。

**4. 技术亮点**
*   **跨平台兼容性**：虽然主要关联 JavaScript 生态，但其核心价值在于对多模态和多厂商模型的统一整理。
*   **高社区关注度**：拥有超过 4.6 万颗星，证明了其在 AI 社区中的极高实用价值和影响力。
*   **实时性维护**：针对快速迭代的 AI 模型，提供了及时的提示词版本追踪能力。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46061 | 🍴 7552 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个集数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）于一体的综合学习资源库。它不仅涵盖了自然语言处理工具（NLTK），还深入讲解了从传统算法到深度神经网络的各种核心技术。

2. **核心功能**
- 提供完整的机器学习与深度学习算法源码及实战案例。
- 集成 PyTorch 和 TensorFlow 2 等主流深度学习框架的应用示例。
- 包含自然语言处理（NLP）相关库（如 NLTK）的使用教程。
- 涵盖经典统计学习方法（如 SVM、KMeans、逻辑回归）及推荐系统实现。

3. **适用场景**
- 希望系统掌握机器学习理论与代码实现的初学者。
- 需要参考 PyTorch 或 TF2 具体应用场景的开发者。
- 想要深入研究 NLP 或推荐系统算法的工程技术人员。

4. **技术亮点**
- 覆盖了从传统机器学习（如 AdaBoost、FP-Growth）到前沿深度学习（如 RNN、LSTM、DNN）的全栈技术体系。
- 结合了数学基础（线性代数）与工程实践（scikit-learn、sklearn），适合构建扎实的理论功底。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11541 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36366 | 🍴 5965 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34884 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33699 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28185 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25728 | 🍴 2884 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34884 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22007 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证及团队协作，并配备完善的分析工具和开发者API。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注与标签服务。
*   集成AI辅助标注功能以提升效率，并内置质量控制机制确保数据准确性。
*   提供强大的团队协作能力、数据分析面板以及便捷的开发者API接口。

3. **适用场景**
*   深度学习模型训练所需的大规模图像分类或目标检测数据集构建。
*   自动驾驶或监控视频中关键帧的语义分割与对象检测标注。
*   科研团队或企业部门进行多人员协作的计算机视觉数据预处理工作。

4. **技术亮点**
*   兼容PyTorch和TensorFlow等主流深度学习框架，支持ImageNet等标准数据集格式。
*   提供从开源自部署到云服务及企业版的多层次产品形态，灵活适配不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16144 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级可解释性AI工具库，旨在帮助理解深度学习模型的决策过程。它广泛支持CNN、Vision Transformer等多种架构，涵盖分类、目标检测及分割等任务。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种可视化算法以生成类激活图。
*   兼容PyTorch框架下的CNN和Vision Transformer模型。
*   适用于图像分类、目标检测、语义分割及图像相似度计算等多种任务。

3. **适用场景**
*   调试和优化计算机视觉深度学习模型时进行误差分析。
*   向非技术利益相关者展示AI模型对特定区域的关注点。
*   研究不同神经网络架构（如Transformer vs CNN）的特征提取差异。

4. **技术亮点**
*   高度模块化设计，轻松集成到现有的PyTorch项目中。
*   广泛支持主流视觉模型架构，具备极强的通用性和兼容性。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在为研究人员和开发者提供可微分的图像处理工具，从而无缝集成到深度学习流水线中。

**2. 核心功能**
*   **可微分图像处理**：提供大量基于 GPU 加速且支持自动微分的传统计算机视觉算法。
*   **PyTorch 原生集成**：完全兼容 PyTorch 张量操作，便于构建端到端的深度学习模型。
*   **几何计算模块**：包含相机标定、姿态估计、多视图几何等高级空间分析功能。
*   **数据增强与变换**：提供丰富的图像几何变换和数据增强工具，适用于训练数据预处理。
*   **机器人学支持**：内置针对机器人导航和空间感知优化的特定几何运算库。

**3. 适用场景**
*   **神经渲染与合成**：用于需要精确几何约束的 3D 重建或新视图合成任务。
*   **机器人视觉系统**：应用于移动机器人的 SLAM（同步定位与建图）或物体抓取中的空间推理。
*   **深度学习预处理**：在训练阶段利用 GPU 加速的可微分水管道进行实时图像变换。
*   **可解释性 AI 研究**：通过结合传统几何先验与深度网络，探索更具物理意义的人工智能模型。

**4. 技术亮点**
*   **软硬结合加速**：充分利用 CUDA 和 Tensor Cores 实现高性能并行计算。
*   **模块化设计**：采用纯函数式编程风格，确保代码的可测试性和模块化复用能力。
*   **开源社区活跃**：作为开源项目，拥有活跃的开发者社区和持续的算法更新（如参与 Hacktoberfest）。
- 链接: https://github.com/kornia/kornia
- ⭐ 11251 | 🍴 1191 | 语言: Python
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
- ⭐ 3254 | 🍴 398 | 语言: Python
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
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，让用户以“龙虾”的方式（隐喻开源与自由）完全掌控自己的数据。它强调数据所有权，提供跨平台、私密的智能辅助体验。

2. **核心功能**
- 支持所有主流操作系统和运行平台，实现无缝接入。
- 赋予用户对自己数据的完全控制权，保障隐私安全。
- 作为个人 AI 助手，提供智能化的日常任务辅助。
- 开源架构允许用户自定义和扩展功能。

3. **适用场景**
- 希望在本地或私有服务器上部署个人 AI 助手的开发者。
- 极度重视数据隐私，不希望个人数据上传至第三方云端的用户。
- 需要在不同操作系统间保持统一 AI 体验的多平台用户。

4. **技术亮点**
- 基于 TypeScript 开发，具备类型安全和良好的生态系统兼容性。
- 采用去中心化或自托管架构，确保数据主权归属于用户。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380465 | 🍴 79697 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一个经过验证的智能体技能框架与软件开发方法论。它通过结构化地整合人工智能代理的能力，旨在解决传统开发流程中的痛点。该项目致力于提升软件开发生命周期（SDLC）的效率与质量。

2. **核心功能**
*   提供模块化的“智能体技能”库，支持按需组合AI能力。
*   采用子代理驱动开发模式，实现复杂任务的自动化分解与执行。
*   集成头脑风暴与代码生成工具，辅助创意构思与原型搭建。
*   定义标准化的软件开发生命周期工作流，确保开发过程的可控性。

3. **适用场景**
*   需要快速原型验证及自动化代码生成的敏捷开发团队。
*   希望利用AI增强现有SDLC流程、提升研发效率的企业。
*   依赖多步推理和复杂任务拆解的高级AI应用开发者。

4. **技术亮点**
*   创新性地将“技能框架”与“开发方法论”深度融合，而非单纯的工具堆砌。
*   基于Shell脚本实现，具备极高的可移植性和轻量级部署优势。
- 链接: https://github.com/obra/superpowers
- ⭐ 238705 | 🍴 21176 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 203092 | 🍴 36352 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合。它拥有超过 400 种集成方式，允许用户选择自托管或云端部署，实现高效的数据流与业务自动化。

### 2. 核心功能
*   **混合自动化模式**：结合低代码/无代码的可视化编辑器与自定义代码编写能力，满足不同复杂度的需求。
*   **丰富的集成生态**：内置超过 400 种应用和 API 集成，无缝连接各类云服务与企业工具。
*   **原生 AI 集成**：深度整合 AI 能力，支持在工作流中直接调用大语言模型进行数据处理和智能决策。
*   **灵活部署选项**：支持自托管以保障数据隐私与控制权，同时也提供便捷的云端托管服务。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，便于与各种 AI 客户端和服务端进行标准化交互。

### 3. 适用场景
*   **企业系统集成**：连接 CRM、ERP、邮件营销等数十种主流 SaaS 工具，实现跨平台数据同步。
*   **AI 驱动的工作流**：利用 LLM 自动处理客户反馈、生成报告或执行复杂的文本数据分析任务。
*   **开发者自动化测试**：通过 API 触发自动化测试流程，监控服务状态并自动发送通知。
*   **数据管道构建**：在非技术人员也能参与的界面下，搭建从数据采集、清洗到可视化的完整 ETL 流程。

### 4. 技术亮点
*   **公平代码（Fair-code）许可**：在保持开源社区活力的同时，限制竞争对手将其作为直接服务出售，平衡了开放性与商业可持续性。
*   **TypeScript 原生开发**：基于 TypeScript 构建，提供了良好的类型安全和现代化的开发体验。
*   **节点化架构**：采用灵活的节点式工作流引擎，允许用户自由组合逻辑节点，实现高度定制化的业务流程。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194076 | 🍴 58837 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建基于人工智能的工具，实现 AI 的普惠化愿景。其核心使命是提供强大的基础工具，让用户能够专注于真正重要的任务与创意。

2. **核心功能**
*   具备自主规划与执行复杂任务链的能力，无需人工逐步干预。
*   支持集成多种大型语言模型（如 GPT、Claude、LLaMA），提供灵活的底层算力选择。
*   拥有开放可扩展的架构，允许开发者基于现有工具进行二次开发与功能增强。
*   自动化处理信息检索、网页浏览及代码执行等多步骤操作。

3. **适用场景**
*   **自动化研究助手**：自动搜索网络信息、整理资料并生成摘要报告。
*   **内容创作流水线**：自主完成从选题调研、草稿撰写到初步编辑的全流程内容生产。
*   **代码开发与调试**：自动编写代码片段、测试脚本并修复常见的逻辑错误。
*   **重复性任务自动化**：处理数据录入、文件管理或跨平台信息同步等繁琐工作。

4. **技术亮点**
*   采用先进的 Agent 架构，通过自我反思与迭代优化提升任务完成的准确率。
*   高度模块化设计，兼容主流 LLM API，便于快速接入不同厂商的大模型服务。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185155 | 🍴 46132 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164352 | 🍴 21283 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163881 | 🍴 30364 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156616 | 🍴 46145 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150093 | 🍴 9344 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146579 | 🍴 23067 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

