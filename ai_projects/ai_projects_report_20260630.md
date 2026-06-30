# GitHub AI项目每日发现报告
日期: 2026-06-30

## 新发布的AI项目

### Fundamental-Ava
- 基于您提供的信息，以下是对 GitHub 项目 **Fundamental-Ava** 的技术分析：

1. **中文简介**
   Fundamental-Ava 致力于构建具备自主性、协作能力和社会智能的数字人类代理。该项目旨在打造能够独立运行并与他人或系统高效互动的智能体。其核心理念是赋予 AI 更高级的社会交互逻辑与集体协作能力。

2. **核心功能**
   *   **自主决策**：代理具备独立思考和执行任务的能力，无需持续的人工干预。
   *   **多代理协作**：支持多个数字人类代理之间进行协调与合作以完成复杂目标。
   *   **社会智能模拟**：内置社会交互逻辑，使代理能理解并响应类似人类的社交信号。
   *   **数字人类构建**：提供框架用于创建具有特定角色和行为模式的虚拟实体。

3. **适用场景**
   *   **复杂任务自动化**：需要多个 AI 代理分工合作完成的长链条业务流程。
   *   **虚拟社交实验**：研究群体行为、社交动力学或多智能体交互模式的学术或商业实验。
   *   **智能客服集群**：构建能够相互协作、分流负载并提供拟人化服务的高级客服系统。

4. **技术亮点**
   *   聚焦于“社会智能”而非单纯的逻辑推理，强调代理间的协同效应。
   *   基于 Python 开发，便于集成现有的 AI 库和机器学习工具。
- 链接: https://github.com/TianhangZhuzth/Fundamental-Ava
- ⭐ 344 | 🍴 43 | 语言: Python
- 标签: ai, ai-agents

### gemini-search-mcp
- 1. **中文简介**
这是一个基于 Google AI Mode (Gemini) 的免费 MCP (Model Context Protocol) 服务器，旨在提供网页搜索功能。它无需 API 密钥即可使用，且支持无限次查询，降低了使用门槛。

2. **核心功能**
*   提供基于 Gemini 模型的网页搜索能力。
*   遵循 MCP 标准协议，便于与各类 AI 客户端集成。
*   完全免费且无需配置 API Key。
*   支持不限数量的搜索请求。

3. **适用场景**
*   需要低成本或零成本接入大模型搜索能力的开发者。
*   希望在不暴露 API 密钥的情况下测试 MCP 协议的项目。
*   利用本地 AI 助手进行实时信息检索的用户。

4. **技术亮点**
*   利用 Google AI Mode 绕过传统的 API 计费限制。
*   极简的配置需求，开箱即用。
- 链接: https://github.com/Sophomoresty/gemini-search-mcp
- ⭐ 74 | 🍴 18 | 语言: Python

### pocketdev
- 1. **中文简介**
PocketDev 允许用户通过一条命令，在仅通过 Tailscale 连接的 Hetzner 云服务器上运行已付费的 AI 编程 CLI 工具（如 Claude Code、Cursor 等），实现从手机远程编写代码。它利用 SSH 和 Mosh 技术，让用户能够随时随地通过终端界面高效地进行远程开发。

2. **核心功能**
*   支持一键部署并运行多种主流 AI 编程助手（包括 Claude Code、Codex、Cursor 等）。
*   基于 Tailscale 构建私密网络，确保 Hetzner 服务器仅对授权设备开放访问。
*   提供优化的移动端远程体验，支持通过手机终端连接服务器进行代码编写。
*   集成 Mosh 和 SSH 技术，保障在网络不稳定环境下的低延迟交互稳定性。

3. **适用场景**
*   需要在移动设备（如手机或平板）上临时进行轻量级代码修改或调试的用户。
*   希望将昂贵的 AI 编程订阅服务部署在低成本云服务器上，以实现多设备共享访问的团队或个人。
*   注重数据隐私和安全，不希望代码数据经过第三方云端处理，倾向于自托管开发环境的开发者。

4. **技术亮点**
*   巧妙结合 Tailscale 的零配置组网能力与 Hetzner 的经济性，解决了远程开发中网络连通性与成本平衡的问题。
*   针对移动端终端体验进行了优化（如使用 Bubbletea 构建 TUI），提升了小屏幕设备上的操作可用性。
- 链接: https://github.com/0xMassi/pocketdev
- ⭐ 59 | 🍴 3 | 语言: Go
- 标签: ai-coding, bubbletea, claude-code, cli, cloud-development-environment

### xuanxuan-prompts
- ### 1. **中文简介**
该项目是一套用于“AI 智能体”复刻精美网页的提示词（Prompt）合集。每个目录包含一份 `prompt.md` 文件和对应的效果图截图，用户只需将这些内容发送给 Claude、Codex 或 Kimi 等 AI 工具，即可直接生成对应的网站代码。

### 2. **核心功能**
*   **标准化提示词模板**：为不同风格的网页设计提供结构化的指令文件。
*   **可视化参考对照**：配合效果图截图，帮助 AI 更准确地理解设计布局和视觉风格。
*   **多平台兼容性**：生成的指令可直接适配 Claude、Codex、Kimi 等多种主流 AI 编程助手。
*   **一键式网页生成**：通过简单的复制粘贴操作，实现从提示到前端代码的快速转化。

### 3. **适用场景**
*   **快速原型开发**：设计师或开发者利用现有灵感快速搭建网页 MVP（最小可行性产品）。
*   **AI 辅助前端教学**：学习者通过观察提示词与最终代码的对应关系，学习结构化 Prompt 编写技巧。
*   **高保真 UI 复刻**：需要将特定设计稿快速转化为可运行 HTML/CSS/JS 代码的场景。

### 4. **技术亮点**
*   **零代码门槛交互**：无需复杂的 API 配置或本地环境搭建，仅需文本交互即可完成网页生成。
*   **图文结合的提示工程**：采用“指令+图像”的双模态输入方式，显著提升 AI 对复杂 UI 布局的理解准确度。
- 链接: https://github.com/xuanxuan321/xuanxuan-prompts
- ⭐ 57 | 🍴 12 | 语言: 未知

### open-memory-protocol
- 1. **中文简介**
Open-Memory-Protocol 是一个开放标准，旨在实现跨工具、会话和设备的便携式、可互操作的 AI 记忆功能。它通过标准化的协议，让大语言模型能够在不同环境中持久化并共享上下文信息。该方案支持自托管部署，致力于打破 AI 助手之间的记忆孤岛。

2. **核心功能**
*   提供标准化的接口，实现 AI 记忆数据在不同工具和平台间的无缝迁移与互通。
*   支持跨会话和跨设备的历史记忆持久化，确保 AI 能够记住用户偏好和过往交互。
*   兼容主流大语言模型（如 OpenAI、Claude 等），并通过 MCP 协议增强集成能力。
*   允许用户自托管记忆服务，保障数据隐私和控制权，避免依赖单一厂商的云存储。

3. **适用场景**
*   需要在多个 AI 编程助手（如 Claude Code、Cursor 等）之间同步项目上下文和代码习惯。
*   构建需要长期记忆能力的个性化 AI 聊天机器人或客服系统，以提供连贯的用户体验。
*   在本地私有化部署 AI 基础设施时，希望统一管理多模型应用的记忆数据存储。

4. **技术亮点**
*   采用 TypeScript 开发，类型安全且易于在现代 Web 和 Node.js 生态中集成。
*   基于开放标准设计，避免了供应商锁定，提升了系统的灵活性和可扩展性。
*   结合 MCP（Model Context Protocol）规范，实现了标准化的上下文交换机制。
- 链接: https://github.com/SMJAI/open-memory-protocol
- ⭐ 48 | 🍴 0 | 语言: TypeScript
- 标签: ai-memory, claude, claude-ai, claude-code, llm

### Agent-Span
- 描述: The Web Access Gateway for AI Agents — 52 channels, 92 MCP tools, 9 SDKs, self-healing backends, async Rust
- 链接: https://github.com/oxbshw/Agent-Span
- ⭐ 34 | 🍴 10 | 语言: Rust
- 标签: ai-agents, ai-tools, api, gateway, llm

### forever-ai-components
- 描述: 600+ zero-dependency animated web components. One HTML file each. Built for AI agents.
- 链接: https://github.com/isas1/forever-ai-components
- ⭐ 30 | 🍴 2 | 语言: HTML

### weekend-city-trip
- 描述: claude code / codex skill , 一个让 AI 帮你 5 分钟深度调研任意中国城市周末玩法的agent skill,基于**博查 WebSearch API**(博查 API),输出图文并茂、可执行的 Markdown / HTML 攻略。
- 链接: https://github.com/liangdabiao/weekend-city-trip
- ⭐ 30 | 🍴 5 | 语言: HTML

### cognitive-substrate-os
- 描述: A lightweight, local, filesystem-first agentic task runner built in TypeScript and powered by Google Gemini
- 链接: https://github.com/damiansire/cognitive-substrate-os
- ⭐ 26 | 🍴 0 | 语言: TypeScript
- 标签: agent, ai, autonomous-agents, gemini, llm

### agent-skills
- 描述: A personal collection of reusable AI agent skills, mostly for Codex, with optional MCP utilities.
- 链接: https://github.com/Misaka-Mikoto-Tech/agent-skills
- ⭐ 25 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具库，集成了敏感词过滤、语言检测、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。此外，该项目还涵盖了丰富的词向量、知识图谱资源、预训练模型（如 BERT）以及各类垂直领域的专业词库和语料数据。它旨在为开发者提供一站式的中英文 NLP 解决方案，涵盖从数据处理、特征工程到模型训练的完整流程。

**2. 核心功能**
*   **基础 NLP 工具**：提供敏感词检测、中英文分词、词性标注、命名实体识别（NER）、句法分析及情感分析。
*   **丰富词库与资源**：内置中日文人名库、行业专用词库（医疗、法律、汽车等）、停用词表、同/反义词库及大量预训练词向量。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、地址等特定格式的抽取，以及基于规则或深度学习的实体链接和关系抽取。
*   **语音与文本生成**：包含语音识别（ASR）语料、中文聊天机器人数据集、文本摘要生成及 GPT/BERT 等预训练模型的使用示例。
*   **知识图谱构建**：提供从维基百科、百度百科等来源抽取三元组构建中文知识图谱的工具及相关数据资源。

**3. 适用场景**
*   **内容安全审核**：用于互联网平台的内容过滤，自动识别敏感词、暴恐词及谣言，确保文本合规。
*   **智能客服与对话系统**：利用语料库、情感分析和预训练模型开发具备上下文理解和情感交互能力的聊天机器人。
*   **垂直领域知识挖掘**：在医疗、金融、法律等专业领域，利用专用词库和实体抽取技术进行非结构化数据的结构化处理和分析。
*   **NLP 算法研究与教学**：作为研究人员或学生的资源仓库，快速获取最新的数据集、模型代码（如 BERT、ALBERT）及评测基准。

**4. 技术亮点**
*   **生态整合性强**：不仅提供代码工具，还汇总了大量高质量的开源数据集、预训练模型（如 UER、OpenCLaP）及学术资源，极大降低了 NLP 入门和研究门槛。
*   **覆盖场景广泛**：从底层的文本清洗、分词到上层的知识图谱构建、语音识别，覆盖了自然语言处理的主要环节。
*   **紧跟前沿技术**：持续更新并集成最新的深度学习模型（如 Transformer、BERT 系列）及开源项目，保持技术的时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81518 | 🍴 15252 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个精选的AI学习资源库，汇集了500个涵盖机器学习、深度学习、计算机视觉和自然语言处理的项目代码。它旨在为开发者提供从入门到实战的全面参考，通过丰富的代码示例加速AI技术的掌握与应用。

2. **核心功能**
- 提供500个高质量的AI项目代码，覆盖主流技术领域。
- 集成机器学习、深度学习、计算机视觉及NLP等多维度内容。
- 包含完整的可运行代码示例，便于直接复现和学习。
- 作为“Awesome”列表，经过筛选确保资源的相关性和实用性。

3. **适用场景**
- AI初学者系统学习机器学习与深度学习基础理论及实践。
- 开发者寻找计算机视觉或NLP领域的具体项目实现参考。
- 研究人员快速检索特定AI任务（如图像识别、文本分类）的代码模板。
- 企业团队进行技术选型或原型开发时的灵感来源。

4. **技术亮点**
- 资源规模庞大且分类清晰，涵盖AI核心子领域。
- 强调代码落地，提供可直接运行的项目实例而非仅理论。
- 社区认可度高（高星标），反映其内容的广泛实用价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35043 | 🍴 7302 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持神经网络、深度学习及机器学习模型的可视化工具。它允许用户直观地查看和调试各种主流框架生成的模型结构，极大地简化了模型的分析过程。

2. **核心功能**
*   支持多种主流格式（如 ONNX、TensorFlow、PyTorch、Keras 等）的模型可视化。
*   提供清晰的图层结构视图，便于理解网络架构和数据流向。
*   支持在浏览器或独立桌面应用中打开模型文件，无需复杂配置。
*   能够显示模型中的权重信息和张量形状，辅助调试与优化。

3. **适用场景**
*   研究人员用于快速检查新构建的深度学习模型结构是否正确。
*   工程师在模型转换（如从 TensorFlow 到 ONNX）后验证输出一致性。
*   开发者在部署模型前，通过可视化界面排查网络层连接错误。
*   非编程人员通过直观的图表理解 AI 模型的工作原理。

4. **技术亮点**
*   基于 JavaScript 开发，具备跨平台兼容性，支持 Web 端和桌面端运行。
*   广泛的格式兼容性，覆盖了从传统 ML 到最新大模型（如 Safetensors）的主流标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33157 | 🍴 3143 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换与部署。它允许开发者在不同的硬件和软件平台间无缝迁移模型，从而简化了从训练到推理的全流程。

2. **核心功能**
*   提供统一的模型格式，支持跨框架（如 PyTorch、TensorFlow）进行模型导出与加载。
*   实现模型在异构硬件加速器（如 CPU、GPU、NPU）上的高效推理执行。
*   拥有庞大的算子库，覆盖主流深度学习网络所需的各类计算层。
*   提供工具链支持，包括模型转换、优化及可视化分析功能。

3. **适用场景**
*   需要将 PyTorch 或 TensorFlow 训练的模型部署到不支持原生框架的生产环境中。
*   希望在边缘设备或特定硬件加速器上运行深度学习推理以降低延迟。
*   进行跨框架的模型互操作性测试或集成不同的 AI 组件。

4. **技术亮点**
*   **开源中立性**：由微软、Facebook、Amazon 等巨头共同维护，避免了厂商锁定。
*   **高性能推理**：通过 ONNX Runtime 提供高度优化的执行引擎，显著提升推理速度。
- 链接: https://github.com/onnx/onnx
- ⭐ 21073 | 🍴 3957 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一部全面涵盖机器学习工程实践的综合指南。它深入探讨了从模型训练、调试到大规模部署的全链路技术细节。该项目旨在为构建高性能、可扩展的机器学习系统提供权威参考。

2. **核心功能**
- 提供大规模分布式训练的最佳实践与故障排除指南。
- 详解大语言模型（LLM）的高效推理优化及硬件加速技术。
- 涵盖存储、网络配置及集群调度（如Slurm）的系统级工程知识。
- 集成PyTorch框架下的模型调试、性能剖析及扩展性策略。

3. **适用场景**
- 开发需要利用数千张GPU进行大规模预训练的语言模型团队。
- 优化生产环境中大型语言模型的推理延迟并降低计算成本。
- 解决复杂机器学习基础设施中的网络瓶颈或存储I/O问题。
- 构建高可用、可扩展的MLOps流水线以支持持续模型迭代。

4. **技术亮点**
- 深度结合底层硬件特性（如GPUDirect、NVLink）与上层框架（Transformers/PyTorch）。
- 针对当前最热门的大语言模型时代，提供了从训练到部署的端到端工程解决方案。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18193 | 🍴 1154 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17264 | 🍴 2107 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13100 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11535 | 🍴 904 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10648 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个精选的AI学习资源库，汇集了500个涵盖机器学习、深度学习、计算机视觉和自然语言处理的项目代码。它旨在为开发者提供从入门到实战的全面参考，通过丰富的代码示例加速AI技术的掌握与应用。

2. **核心功能**
- 提供500个高质量的AI项目代码，覆盖主流技术领域。
- 集成机器学习、深度学习、计算机视觉及NLP等多维度内容。
- 包含完整的可运行代码示例，便于直接复现和学习。
- 作为“Awesome”列表，经过筛选确保资源的相关性和实用性。

3. **适用场景**
- AI初学者系统学习机器学习与深度学习基础理论及实践。
- 开发者寻找计算机视觉或NLP领域的具体项目实现参考。
- 研究人员快速检索特定AI任务（如图像识别、文本分类）的代码模板。
- 企业团队进行技术选型或原型开发时的灵感来源。

4. **技术亮点**
- 资源规模庞大且分类清晰，涵盖AI核心子领域。
- 强调代码落地，提供可直接运行的项目实例而非仅理论。
- 社区认可度高（高星标），反映其内容的广泛实用价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35043 | 🍴 7302 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持神经网络、深度学习及机器学习模型的可视化工具。它允许用户直观地查看和调试各种主流框架生成的模型结构，极大地简化了模型的分析过程。

2. **核心功能**
*   支持多种主流格式（如 ONNX、TensorFlow、PyTorch、Keras 等）的模型可视化。
*   提供清晰的图层结构视图，便于理解网络架构和数据流向。
*   支持在浏览器或独立桌面应用中打开模型文件，无需复杂配置。
*   能够显示模型中的权重信息和张量形状，辅助调试与优化。

3. **适用场景**
*   研究人员用于快速检查新构建的深度学习模型结构是否正确。
*   工程师在模型转换（如从 TensorFlow 到 ONNX）后验证输出一致性。
*   开发者在部署模型前，通过可视化界面排查网络层连接错误。
*   非编程人员通过直观的图表理解 AI 模型的工作原理。

4. **技术亮点**
*   基于 JavaScript 开发，具备跨平台兼容性，支持 Web 端和桌面端运行。
*   广泛的格式兼容性，覆盖了从传统 ML 到最新大模型（如 Safetensors）的主流标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33157 | 🍴 3143 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了 Essential（关键/核心）速查表集合。它旨在帮助研究者快速回顾和掌握相关领域的核心概念、函数及最佳实践，是入门与进阶的实用参考工具。

### 2. 核心功能
*   汇集深度学习与机器学习领域的关键知识点速查表。
*   涵盖主流框架（如 Keras）及科学计算库（如 NumPy, SciPy, Matplotlib）的使用技巧。
*   提供结构化、易于查阅的技术笔记，方便快速检索信息。
*   聚焦于研究场景下的核心算法与数据处理流程总结。

### 3. 适用场景
*   机器学习初学者在复习基础概念和常用库函数时作为速查手册。
*   研究人员在进行模型开发前，快速回顾特定算法或数据预处理步骤。
*   开发者在调试代码时，快速查询 NumPy 或 Matplotlib 等库的具体用法。
*   团队内部知识共享，用于统一对常见技术术语和实践标准的理解。

### 4. 技术亮点
*   **高度聚合性**：将分散的核心知识点整合为便捷的速查形式，极大提升学习效率。
*   **生态覆盖广**：标签涵盖从底层计算（NumPy/SciPy）到可视化（Matplotlib）及高级框架（Keras）的全栈技术点。
*   **社区认可度高**：拥有超过 1.5 万星标，证明其内容质量和实用性受到广泛开发者认可。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费配套教材以辅助零基础用户入门及求职实战。内容涵盖 Python、数学基础以及机器学习、深度学习、NLP、CV 等主流技术领域及其常用框架（如 PyTorch、TensorFlow）。

### 2. **核心功能**
*   提供结构化的 AI 学习路径，从零基础到就业实战全流程指导。
*   收录近 200 个精选实战案例和项目，强调动手实践能力。
*   免费开放配套教材和学习资源，降低 AI 学习门槛。
*   覆盖广泛的热门技术栈，包括数据科学、算法及多种深度学习框架。

### 3. **适用场景**
*   **初学者入门**：希望系统了解人工智能领域知识体系并寻找入门资料的学习者。
*   **求职准备**：需要积累实战项目经验以提升简历竞争力、寻求 AI 相关职位的求职者。
*   **技能拓展**：希望补充或更新在数据分析、深度学习等领域最新工具和框架知识的开发者。

### 4. **技术亮点**
*   高度整合了从基础数学/编程到高级应用（NLP/CV）的完整知识图谱。
*   通过“路线图+实战案例+免费教材”的组合模式，解决了传统学习资源分散的问题。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13100 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11728 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9125 | 🍴 1233 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8913 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6199 | 🍴 725 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81518 | 🍴 15252 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目在 ACL 2024 会议上发表，旨在简化大模型的适配过程。它提供了从指令微调到强化学习对齐的一站式解决方案。

### 2. 核心功能
*   支持超过 100 种主流大语言模型和视觉语言模型的统一高效微调。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）技术。
*   提供完整的训练流程，涵盖指令微调（SFT）、奖励建模（RM）及强化学习人类反馈（RLHF）。
*   内置量化技术（如 4bit/8bit），显著降低显存占用并提升推理效率。
*   兼容 Transformers 库，支持多卡分布式训练及多种优化器配置。

### 3. 适用场景
*   **企业级私有化部署**：基于开源模型（如 Llama 3、Qwen、DeepSeek）构建符合特定业务需求的垂直领域助手。
*   **学术研究与应用开发**：快速验证不同模型架构在特定数据集上的微调效果，加速算法迭代。
*   **低资源环境适配**：利用 QLoRA 等技术，在消费级显卡上高效微调大规模模型，降低硬件门槛。

### 4. 技术亮点
*   **极简配置**：通过 YAML 配置文件即可启动训练，无需编写复杂的代码逻辑。
*   **全链路支持**：无缝衔接数据预处理、模型训练、评估到部署的全生命周期。
*   **前沿算法集成**：率先支持最新的 MoE（混合专家）架构及多种新兴大模型（如 Gemma、DeepSeek）。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72831 | 🍴 8894 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI知识。该项目由微软发起，通过Jupyter Notebook提供交互式学习体验，覆盖从基础机器学习到深度学习的高级主题。其目标是帮助学习者构建扎实的人工智能技能体系，无需深厚的数学或编程背景即可上手。

2. **核心功能**
*   提供结构化的12周学习计划，将复杂概念分解为24个易于理解的课程模块。
*   基于Jupyter Notebook实现代码与理论的结合，支持动手实践和即时反馈。
*   涵盖广泛的AI领域，包括机器学习、深度学习、计算机视觉和自然语言处理等。
*   由微软教育团队开发，确保内容的准确性、前沿性和教学有效性。
*   免费向公众开放，降低人工智能学习门槛，促进全球AI教育普及。

3. **适用场景**
*   初学者希望系统性地从零开始学习人工智能基础知识。
*   教育工作者寻找结构化、可复用的AI课程资源用于课堂教学。
*   企业员工希望通过短期培训快速掌握AI应用技能以提升工作效率。
*   学生群体在课余时间进行自我提升，准备进入AI相关领域的职业道路。

4. **技术亮点**
*   采用“边学边练”的模式，通过交互式笔记本强化理解。
*   内容紧跟行业趋势，涵盖CNN、RNN、GAN等主流深度学习架构。
*   开源协作模式，允许社区贡献和优化课程内容，保持活力与更新。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48862 | 🍴 10127 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- **1. 中文简介**
该项目收集并公开了来自Anthropic、OpenAI、Google及xAI等主流厂商最新大模型的系统提示词（System Prompts），涵盖Claude、ChatGPT、Gemini等多个系列。内容包含Claude Code、Grok、Cursor等工具的内部指令，并定期更新以保持时效性。

**2. 核心功能**
*   **多厂商数据聚合**：整合了Anthropic、OpenAI、Google和xAI等头部AI公司的系统提示词。
*   **覆盖主流模型与工具**：不仅包含基础聊天模型，还囊括了代码助手（如Copilot）、IDE插件（如VS Code）及设计工具（如Claude Design）。
*   **持续动态更新**：项目维护者会定期同步最新泄露或公开的提示词信息，确保数据鲜活。
*   **开源共享资源**：以开源形式提供完整的提示词文本，方便开发者直接查阅和使用。

**3. 适用场景**
*   **提示词工程学习**：帮助开发者逆向研究顶尖AI模型的指令结构，提升Prompt编写技巧。
*   **安全审计与防御**：用于检测应用是否存在系统提示词泄露风险，加强LLM应用的安全性。
*   **竞品分析与研究**：研究人员可借此对比不同厂商模型在底层指令设计上的差异与策略。

**4. 技术亮点**
*   **高价值情报源**：获取通常不对外公开的高级模型内部逻辑，具有极高的研究参考价值。
*   **跨平台兼容性**：收集范围广泛，覆盖了从通用对话到专业代码生成的多种AI应用场景。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 47274 | 🍴 7713 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个集数据分析、机器学习实战及深度学习框架于一体的综合学习资源库，涵盖了从线性代数基础到PyTorch和TensorFlow 2的完整技术栈。它通过整合NLTK等自然语言处理工具，为学习者提供了从理论推导到代码实现的系统化路径。

2. **核心功能**
*   涵盖经典算法实战，包括AdaBoost、Apriori、K-Means、SVM、逻辑回归等。
*   提供深度学习模型实现，支持DNN、RNN、LSTM及基于PyTorch和TF2的网络构建。
*   集成自然语言处理（NLP）模块，利用NLTK进行文本分析与处理。
*   包含推荐系统、PCA降维、SVD分解及FP-Growth关联规则挖掘等功能。
*   配套线性代数等数学基础讲解，夯实机器学习理论根基。

3. **适用场景**
*   机器学习初学者系统性入门，建立从数学原理到算法代码的完整知识体系。
*   数据科学从业者复习与巩固经典算法（如聚类、分类、降维）的工程实现。
*   深度学习研究者对比不同框架（PyTorch vs TensorFlow 2）在相同任务下的实现差异。
*   NLP领域工程师快速查阅和处理文本数据的工具库参考。

4. **技术亮点**
*   实现了主流机器学习与深度学习算法的代码级复现，兼顾理论与实践。
*   技术栈覆盖全面，同时支持Scikit-learn传统ML与PyTorch/TF2现代DL框架。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42357 | 🍴 11541 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36905 | 🍴 6090 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35043 | 🍴 7302 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33707 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28266 | 🍴 3426 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25791 | 🍴 2892 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码集合。它旨在为开发者提供全面的实践案例，涵盖从基础算法到前沿技术的多种应用场景。

2. **核心功能**
- 提供涵盖AI五大细分领域的大量完整代码示例。
- 展示机器学习与深度学习模型的实际实现细节。
- 包含计算机视觉和NLP任务的专项解决方案。
- 作为学习各种AI算法和架构的实用参考库。

3. **适用场景**
- AI初学者快速上手并理解各类经典算法的实现。
- 研究人员寻找特定任务（如图像分类、文本生成）的代码模板。
- 工程师在实际项目中借鉴成熟的模型结构和数据处理流程。

4. **技术亮点**
- 资源规模宏大，一次性收录500个项目，覆盖面极广。
- 标签分类清晰，便于用户按技术领域（CV/NLP/ML）精准筛选。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35043 | 🍴 7302 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22046 | 🍴 2060 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，专为视觉人工智能设计。它提供开源、云和企业合作版本，支持图像、视频及 3D 数据的 AI 辅助标注、质量保证与团队协作。该项目拥有活跃的开发者 API，旨在通过高效的数据标注流程加速 AI 模型训练。

2. **核心功能**
*   支持图像、视频及 3D 点云的多模态数据标注。
*   集成 AI 辅助自动标注功能，显著提升数据标注效率。
*   提供企业级团队协作、质量控制及数据分析工具。
*   开放开发者 API，便于集成到现有的机器学习工作流中。
*   提供开源、云端及私有化部署等多种产品形态。

3. **适用场景**
*   构建用于目标检测或语义分割的大规模高质量标注数据集。
*   团队协同进行视频动作识别或图像分类任务的标注工作。
*   需要严格质量控制和数据审计的企业级视觉 AI 项目开发。
*   利用自动化工具快速预处理海量未标注的图像或视频资源。

4. **技术亮点**
*   强大的 AI 辅助标注引擎，可结合 PyTorch/TensorFlow 模型实现自动化预标注。
*   全面支持从传统 2D 图像到复杂的 3D 空间数据标注。
*   灵活的部署架构，既支持公有云服务也支持完全离线的私有化部署。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16185 | 🍴 3728 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目旨在为计算机视觉提供高级的人工智能可解释性支持。它广泛兼容卷积神经网络（CNN）、视觉Transformer等多种模型，并覆盖分类、检测及分割等任务。此外，它还支持图像相似度分析等多样化应用场景。

2. **核心功能**
*   支持多种主流架构，包括CNN和Vision Transformers。
*   涵盖图像分类、目标检测、语义分割及图像相似度计算等多种任务。
*   提供Grad-CAM、Score-CAM等多种可视化解释方法。
*   增强深度学习模型的透明度和可解释性。

3. **适用场景**
*   计算机视觉模型的调试与错误分析。
*   医疗影像或自动驾驶等高可靠性要求领域的模型验证。
*   学术研究中的可解释人工智能（XAI）算法对比实验。

4. **技术亮点**
*   高度模块化设计，轻松集成到现有PyTorch项目中。
*   广泛的模型兼容性，支持从传统CNN到最新Transformer架构。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12895 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理原语，旨在简化计算机视觉模型的开发与训练流程。

**2. 核心功能**
*   提供丰富的可微分几何与图像处理算子，支持端到端的深度学习训练。
*   无缝集成 PyTorch 生态，允许用户直接在张量上进行高效的计算机视觉操作。
*   涵盖从基础图像增强到高级相机标定、三维重建及机器人导航的完整功能集。

**3. 适用场景**
*   需要结合传统计算机视觉几何约束与深度学习模型的研究与开发。
*   机器人领域的空间感知、SLAM（同步定位与建图）及自主导航系统构建。
*   对图像处理流水线进行自动化优化或嵌入到神经网络的复杂应用开发。

**4. 技术亮点**
*   **可微分性**：所有核心算子均为可微分设计，可直接反向传播梯度，便于集成到神经网络中。
*   **硬件加速**：充分利用 GPU 加速计算，显著提升大规模图像处理任务的效率。
*   **PyTorch 原生支持**：作为 PyTorch 的一等公民库，拥有极低的集成门槛和优异的兼容性。
- 链接: https://github.com/kornia/kornia
- ⭐ 11255 | 🍴 1192 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2193 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3260 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2618 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2415 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款基于 TypeScript 构建的个人 AI 助手，支持跨操作系统和平台运行。它倡导“龙虾式”的数据自主权，让用户能够完全掌控自己的数据与隐私。

**2. 核心功能**
- 提供完全个人化的 AI 助手体验，强调用户对自己数据的绝对所有权。
- 具备高度的兼容性，可在任何操作系统和平台上无缝部署与运行。
- 采用 TypeScript 开发，确保代码的健壮性与现代 Web 生态的良好集成。

**3. 适用场景**
- 注重数据隐私的个人用户，希望在不依赖第三方云服务的情况下使用 AI 助手。
- 开发者或技术爱好者，需要在多种异构环境中快速搭建个性化的 AI 代理。
- 追求本地化部署的企业或个人，希望自定义 AI 行为逻辑并保留所有交互记录。

**4. 技术亮点**
- 以“龙虾”为象征隐喻，独特地强化了其开源、自主及去中心化的品牌理念。
- 依托 TypeScript 语言优势，提供了良好的类型安全和开发体验，便于社区贡献与维护。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381101 | 🍴 79830 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架与软件开发方法论。它通过结构化流程赋能开发者，将人工智能有效整合进实际工作流中。该项目旨在提供一套切实可行的“代理驱动开发”实践指南。

2. **核心功能**
*   提供基于 Shell 脚本的代理技能框架，支持自动化任务执行。
*   采用子代理驱动开发（Subagent-Driven Development）模式，实现复杂任务的分解与协作。
*   整合头脑风暴与编码辅助功能，优化软件开发生命周期（SDLC）。
*   定义标准化的代理交互协议，确保 AI 助手在开发过程中的一致性与可靠性。

3. **适用场景**
*   希望利用 AI 代理提升日常编码效率及重构能力的开发者。
*   寻求将大语言模型深度集成到传统软件工程流程中的团队。
*   需要系统化方法来进行复杂软件项目规划与头脑风暴的技术负责人。

4. **技术亮点**
*   率先提出并实践“子代理驱动开发”这一新型软件工程范式。
*   以轻量级 Shell 脚本为核心，降低了集成 AI 技能的门槛与复杂度。
*   强调方法论的实用性，提供了从理论到代码落地的完整闭环参考。
- 链接: https://github.com/obra/superpowers
- ⭐ 242024 | 🍴 21479 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **1. 中文简介**
Hermes Agent 是一款伴随用户共同成长的智能代理工具，旨在通过持续的学习与迭代来适应用户的工作流。它集成了多种主流大语言模型的能力，为用户提供高度定制化和智能化的代码辅助服务。作为一个开源项目，它致力于成为开发者个人专属的 AI 编码助手。

**2. 核心功能**
*   **多模型集成支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 等多个主流 LLM 提供商，允许用户灵活切换或组合使用不同模型。
*   **自适应成长机制**：具备“伴随成长”特性，能够根据用户的交互历史和使用习惯不断优化其响应策略和行为模式。
*   **代码智能辅助**：深度集成 Claude Code 和 Codex 等工具，提供强大的代码生成、重构、调试及解释能力。
*   **开放可扩展架构**：作为开源项目（由 Nous Research 等社区推动），支持开发者进行二次开发和定制化部署。

**3. 适用场景**
*   **高级开发者工作流优化**：适合需要频繁切换不同 AI 模型以获取最佳代码建议的专业开发者。
*   **个性化 AI 助手构建**：适用于希望拥有一个能记住自己偏好、风格并随时间进化的私人编码助手的用户。
*   **研究与实验平台**：适合 AI 研究者或爱好者用于探索多模型协作（如 OpenClaw/MoltBot 概念）及代理行为的边界。

**4. 技术亮点**
*   **异构模型融合**：打破了单一模型的限制，实现了在同一个代理框架下无缝调用和优化来自不同厂商的大型语言模型。
*   **社区驱动创新**：融合了 ClawdBot、MoltBot 等前沿代理概念，代表了当前开源 AI Agent 领域的最新实践方向。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 206121 | 🍴 37258 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- **1. 中文简介**
n8n 是一款具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合的开发模式。用户可选择自托管或云端部署，并利用其丰富的集成能力连接各类应用。

**2. 核心功能**
*   提供直观的可视化工作流构建器，降低自动化开发门槛。
*   内置原生 AI 能力，支持智能任务处理与逻辑判断。
*   拥有超过 400 种集成工具，实现跨平台数据互通与应用连接。
*   支持自托管和云端两种部署方式，兼顾数据安全与灵活性。
*   允许在工作流中嵌入自定义代码，满足复杂业务逻辑需求。

**3. 适用场景**
*   企业级数据同步：自动在不同 SaaS 应用（如 CRM、ERP）之间迁移和同步数据。
*   AI 驱动的业务流程：利用 AI 模型自动化处理客户支持工单或内容生成任务。
*   系统监控与告警：集成多种 API 监控服务状态，并在异常时通过邮件或即时通讯工具发送通知。
*   开发者工具链自动化：结合 CLI 和代码编辑器，自动化执行测试、部署及文档更新等开发任务。

**4. 技术亮点**
*   **公平代码（Fair-code）许可**：在保持开源精神的同时规范商业使用，平衡社区贡献与企业利益。
*   **MCP 支持**：原生支持 Model Context Protocol (MCP)，便于与各类 AI 模型上下文无缝交互。
*   **混合编程模式**：完美融合低代码可视化操作与高自由度 TypeScript 自定义脚本。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194633 | 🍴 58947 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185228 | 🍴 46116 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164557 | 🍴 21292 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163948 | 🍴 30373 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156716 | 🍴 46160 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150233 | 🍴 9362 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147099 | 🍴 23167 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

