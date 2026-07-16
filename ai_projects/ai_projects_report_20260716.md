# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### cue
- 1. **中文简介**
Cue 是一款开源的 macOS AI 助手，它以浮动窗口形式覆盖在屏幕之上，能够实时监听并观看您的会议内容。该工具具备隐私保护特性，可在屏幕共享时自动隐藏，是 Cluely 的替代方案，且支持用户自带 API Key。

2. **核心功能**
- 悬浮式 UI 设计，不干扰主屏幕操作。
- 实时语音转文字及会议内容分析。
- 智能隐藏机制，防止屏幕共享时泄露内容。
- 支持自定义 API Key，无需绑定特定服务商账号。
- 作为 Cluely 的开源替代品提供类似功能。

3. **适用场景**
- 需要记录会议纪要但希望保护隐私的专业人士。
- 希望在屏幕共享演示时保持后台 AI 辅助工作的开发者或设计师。
- 寻求 Cluely 免费或开源替代方案的 macOS 用户。
- 对数据主权敏感，倾向于自带密钥（BYOK）的用户。

4. **技术亮点**
- 采用“自带密钥”架构，增强用户数据控制权。
- 针对 macOS 系统优化的屏幕共享检测与隐藏逻辑。
- 轻量级 JavaScript 实现，便于社区贡献和二次开发。
- 链接: https://github.com/Blueturboguy07/cue
- ⭐ 207 | 🍴 48 | 语言: JavaScript

### skills
- 1. **中文简介**
这是一个开源项目，旨在为 OpenAI Codex 提供主题定制技能、AI 驱动的主题生成器以及跨平台的运行时环境。它允许用户创建和自定义 Codex 桌面应用的外观与风格，支持在 Windows 和 macOS 系统上运行。

2. **核心功能**
*   提供基于 AI 的自动化主题生成能力，简化视觉定制流程。
*   包含跨平台运行时，支持在 Windows 和 macOS 上无缝运行自定义主题。
*   实现主题管理功能，方便用户安装、切换和管理多个 Codex 主题。
*   利用 Chromium DevTools Protocol 等技术深入集成，实现深度的桌面应用定制。

3. **适用场景**
*   希望个性化 OpenAI Codex 桌面应用界面以提升视觉体验的用户。
*   需要批量生成或快速测试不同配色方案的开发者或设计师。
*   热衷于探索 Chromium 内核应用深度定制技术的极客群体。

4. **技术亮点**
*   结合了 OpenAI Codex 生态与 Node.js 运行时，实现了高效的插件化扩展机制。
*   直接操作 Chromium DevTools Protocol，能够精准控制桌面应用的渲染样式。
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 141 | 🍴 13 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### yuwen-publish-precheck
- ### 1. 中文简介
该项目是一个专注于内容合规性预检查的 AI Agent，支持在发布抖音、小红书或微信视频号前对文案进行风险审查。它不仅能精准识别违规点并引用官方规则，还能提供可直接使用的修改建议，通过本地积累的规则库不断提升判断准确率。

### 2. 核心功能
*   **多平台合规审查**：针对抖音、小红书、微信视频号等主流平台的特定审核规则进行文案检测。
*   **违规点定位与溯源**：明确指出哪句话存在风险，并引用具体的官方规则条文作为依据。
*   **智能修改建议**：提供经过校准的、可直接使用的合规化改写方案，而非简单的风险提示。
*   **本地规则库迭代**：基于38篇真实样本和72条官方引文校准尺度，用户踩过的坑会沉淀为本地规则，使系统越用越准。

### 3. 适用场景
*   **新媒体运营者**：在发布短视频脚本或图文笔记前，快速排查潜在的封号或限流风险。
*   **内容创作者**：利用AI辅助优化文案，确保内容既符合平台规范又能保持吸引力。
*   **品牌公关团队**：批量检查营销文案的合规性，避免因不当用语引发的舆情或处罚风险。

### 4. 技术亮点
*   **Cursor/Claude 集成**：作为 Agent Skills 运行，深度集成于 Cursor 编辑器，利用 Claude 等大模型能力实现智能化工作流。
*   **数据驱动的精准度**：通过大量真实样本和官方原文进行微调与校准，解决了通用 AI 在垂直领域规则理解上的偏差问题。
*   **非“黑盒”决策**：强调规则的可查性和依据的公开性，提供透明化的审核逻辑，帮助用户理解而非盲目信任 AI。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 110 | 🍴 7 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### claude-arbitrage-bot
- 1. **中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，集成了内置的Python自动化功能。该项目利用智能合约实现链上交易逻辑，并结合脚本进行自动化操作。

2. **核心功能**
- 支持在以太坊兼容网络上执行去中心化金融（DeFi）套利策略。
- 内置Python自动化模块，简化交易执行和监控流程。
- 部署智能合约以处理链上资金交换和利润捕获。
- 兼容主流区块链基础设施，如Ethereum、BSC等。

3. **适用场景**
- 自动化捕捉DEX之间的价格差异以实现无风险或低风险套利。
- 开发者测试基于AI辅助（如Claude/Codex标签暗示）的智能合约生成与优化。
- 高频交易策略在以太坊生态中的快速部署与运行。

4. **技术亮点**
- 结合了Solidity智能合约与Python后端自动化，实现了链上与链下的高效协同。
- 标签中提及AI工具（Claude, GPT, Codex），暗示可能利用大语言模型辅助代码生成或策略优化。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### ai-api-relay-guide
- ### GitHub 项目分析：ai-api-relay-guide

**1. 中文简介**
该项目是一个基于 GitHub Pages 构建的静态网站，旨在为用户推荐可靠的 AI API 中转服务，并通过 PokeAPI 作为标准化测试基准来直观对比各服务的响应速度与价格优势。它特别突出了部分服务在 GPT 和 Claude 模型上提供的极低费率（如 GPT 0.03倍、Claude 0.2倍）。

**2. 核心功能**
*   **API 中转站推荐**：整理并推荐多个稳定且性价比高的 AI API 代理服务商。
*   **性能与成本评测**：利用 PokeAPI 统一接口进行压力测试，量化评估各中转站的延迟表现。
*   **费率对比展示**：直观展示不同服务商对主流大模型（GPT、Claude）的折算系数，突出低价优势。
*   **静态页面托管**：基于 GitHub Pages 部署，无需后端服务器即可快速访问和更新信息。

**3. 适用场景**
*   **开发者选型**：需要寻找低成本、高稳定性 API 接口的独立开发者或小型团队。
*   **成本控制**：希望在保证服务质量的前提下，大幅降低调用大模型 API 费用的个人或企业。
*   **市场监控**：关注 AI 中转市场价格波动及服务质量的科技爱好者或研究人员。

**4. 技术亮点**
*   **轻量级架构**：仅使用 CSS 构建前端展示，依赖 GitHub Pages 实现零成本托管，维护简单。
*   **标准化测试基准**：巧妙借用 PokeAPI 这种公开、稳定的标准接口来模拟网络请求，使不同服务商的性能对比具有可比性和客观性。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 75 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### Awesome_ai_learning
- 描述: 无描述
- 链接: https://github.com/h9-tec/Awesome_ai_learning
- ⭐ 68 | 🍴 7 | 语言: 未知

### SuperMap
- 描述: SuperMap is a living spatial memory for embodied AI — it perceives the world, remembers its evolution, and supports reasoning and action.
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 57 | 🍴 1 | 语言: 未知

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 41 | 🍴 2 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

### OpenMicro
- 描述: Codex Micro functionality using any Gaming Controller on any Coding Harness!
- 链接: https://github.com/stephenleo/OpenMicro
- ⭐ 38 | 🍴 2 | 语言: TypeScript
- 标签: agenticai, ai, claude, claude-code, codex

### codex-dream-skin
- 描述: macOS & Windows Codex Desktop 梦幻换肤 Skill｜由世事宜AI免费提供
- 链接: https://github.com/xnydl/codex-dream-skin
- ⭐ 36 | 🍴 1 | 语言: JavaScript
- 标签: codex, codex-desktop, macos, openai, skill

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源合集与工具库，涵盖了从基础数据（如敏感词、停用词、情感值）到高级模型（如 BERT、GPT-2）及各类垂直领域语料。该项目集成了多种实用的 NLP 工具、数据集、预训练模型及行业报告，旨在为开发者提供一站式的中英文 NLP 解决方案。它不仅包含传统的分词、NER 和句法分析资源，还紧跟前沿技术，提供了大量基于深度学习的最新 NLP 实践案例。

2. **核心功能**
*   **基础 NLP 工具集成**：提供敏感词检测、中英文分词、词性标注、命名实体识别（NER）、情感分析及文本摘要等常用功能的代码实现或工具推荐。
*   **海量垂直领域语料与词库**：收录了涵盖医疗、法律、金融、汽车、诗词、地名等数十个专业领域的专用词库、数据集及问答语料，支持特定场景下的模型训练。
*   **前沿预训练模型与资源**：汇聚了 BERT、ERNIE、RoBERTa、ALBERT、GPT-2 等多种主流预训练语言模型的中文版本、微调代码及性能对比评测。
*   **多模态与专项任务支持**：包含语音识别（ASR）、语音合成（TTS）、OCR 文字识别、知识图谱构建、实体链接及对话系统（Chatbot）等跨模态和多任务的处理资源。
*   **数据增强与标注工具**：提供包括 EDA 在内的多种文本数据增强方法，以及 Doccano、brat 等开源文本标注工具，辅助高质量训练数据的构建。

3. **适用场景**
*   **企业级智能客服与对话系统开发**：利用项目中的闲聊语料、任务型对话数据集及 Rasa/ConvLab 等框架资源，快速搭建具备上下文理解和领域知识问答能力的聊天机器人。
*   **垂直行业知识图谱构建**：依托项目提供的医疗、金融、法律等领域的专用词库、实体识别模型及关系抽取代码，高效构建高精度的行业垂直知识图谱。
*   **中文 NLP 算法研究与教学**：研究人员或学生可通过该项目获取最新的中英文 NLP 论文、数据集基准（Benchmark）、代码实现及学术报告，用于复现 SOTA 模型或开展对比实验。
*   **内容安全与舆情监控**：直接使用内置的敏感词库、暴恐词表、谣言数据库及情感分析工具，实现自动化内容审核、风险预警及舆论倾向分析。

4. **技术亮点**
*   **极高的资源聚合度**：作为 GitHub 上星标数超过 8 万的顶级 NLP 资源库，它不仅是工具集，更是中文 NLP 领域的“百科全书”，极大地降低了资料搜集门槛。
*   **紧跟 AI 前沿动态**：持续更新包括 BERT 家族、Transformer 架构、大语言模型（LLM）微调及对抗性样本生成等最新技术成果，确保资源的时效性和先进性。
*   **全栈式解决方案**：覆盖了从数据清洗、标注、预处理、模型训练到推理部署的全生命周期所需资源，同时兼顾传统统计学习方法与现代深度学习技术。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码库合集。它旨在为开发者提供丰富的实战案例，涵盖从基础算法到前沿应用的全方位技术实践。

2. **核心功能**
- 汇集500个完整的AI相关项目代码，支持多种主流技术领域。
- 覆盖机器学习、深度学习、计算机视觉和NLP等关键方向。
- 提供可直接运行的Python代码示例，便于快速学习与复现。
- 作为资源索引，帮助用户系统性地探索不同AI应用场景。

3. **适用场景**
- AI初学者希望寻找大量实战项目以巩固理论基础。
- 开发者需要参考具体代码实现来解决特定领域的技术问题。
- 教育者用于课程设计或培训，提供多样化的教学案例。

4. **技术亮点**
- 资源极其丰富，一次性整合数百个高质量开源项目。
- 标签分类清晰，便于用户根据特定技术领域快速筛选内容。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35473 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. **中文简介**
Netron 是一款支持多种神经网络、深度学习及机器学习模型的可视化工具。它能够直观地展示模型的结构和数据流，帮助用户深入理解算法原理。该工具兼容 Keras、PyTorch、TensorFlow、ONNX 等主流框架格式。

### 2. **核心功能**
*   **多格式支持**：广泛兼容 CoreML、Keras、ONNX、PyTorch、TensorFlow 等多种主流模型格式。
*   **结构可视化**：提供清晰的图形界面，直观展示神经网络的层结构、节点连接及数据流向。
*   **跨平台运行**：作为 JavaScript 项目，可轻松集成为浏览器扩展或桌面应用，实现跨平台查看。
*   **模型调试辅助**：通过可视化界面帮助用户快速定位模型结构错误并进行调试优化。

### 3. **适用场景**
*   **模型结构审查**：研究人员或工程师在训练前检查模型架构是否符合设计预期。
*   **学术交流与演示**：在论文写作或技术分享中，利用生成的图表直观展示复杂的网络结构。
*   **模型兼容性测试**：验证不同框架间模型转换（如 PyTorch 转 ONNX）后的结构一致性。

### 4. **技术亮点**
*   **轻量化部署**：基于 Web 技术构建，无需安装重型依赖即可在浏览器中流畅运行大模型可视化。
*   **高扩展性**：支持 Safetensors 等新兴格式，紧跟 AI 社区发展动态。
*   **用户友好**：界面简洁直观，即使非专业人士也能快速上手进行模型探索。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个旨在促进机器学习模型互操作性的开放标准格式。它允许开发者在不同深度学习框架之间无缝转换和部署模型，打破了框架间的壁垒。通过统一表示法，ONNX 简化了从训练到部署的全流程工作流。

**2. 核心功能**
*   支持将主流框架（如 PyTorch、TensorFlow、Keras）训练的模型转换为统一的 ONNX 格式。
*   提供跨平台兼容性，使模型能在不同硬件加速器和推理引擎上高效运行。
*   定义了一套标准的计算图结构和数据类型，确保模型语义在不同工具链中保持一致。
*   内置丰富的算子库，覆盖常见的深度神经网络层和传统机器学习算法组件。

**3. 适用场景**
*   **模型迁移与部署**：将在 PyTorch 或 TensorFlow 中训练的模型导出并部署到不支持原生框架的生产环境或边缘设备。
*   **硬件加速优化**：利用 ONNX Runtime 等专用推理引擎，针对特定硬件（如 CPU、GPU、NPU）进行性能调优。
*   **多框架协作开发**：在混合使用多种框架的研究或工程团队中，实现模型组件的共享和复用。

**4. 技术亮点**
*   **生态开放性**：由微软、Facebook 等科技巨头联合发起，拥有广泛的社区支持和行业采纳度。
*   **高性能推理**：配套优化的 ONNX Runtime 能够显著降低延迟并提高吞吐量，适合实时应用。
*   **标准化程度高**：作为工业界事实上的标准，有效解决了机器学习碎片化问题，提升了工具链的可移植性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21160 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. **中文简介**
《ML Engineering》是一本关于机器学习工程实践的开源书籍。它全面涵盖了从模型训练、调试到大规模部署和推理的全链路工程知识。该项目旨在为构建高效、可扩展的机器学习系统提供指导。

### 2. **核心功能**
*   提供大规模语言模型（LLM）的训练、微调和推理的最佳实践指南。
*   深入讲解使用 PyTorch、Slurm 和分布式环境进行高性能计算的技术细节。
*   涵盖 GPU 资源管理、网络优化及存储解决方案以支持可扩展性。
*   包含针对机器学习系统的调试技巧和性能分析工具的使用方法。
*   介绍 MLOps 流程，包括模型部署、监控及服务化架构设计。

### 3. **适用场景**
*   需要从零搭建或优化大规模深度学习集群的工程团队。
*   致力于解决 LLM 训练成本高、收敛慢或推理延迟大的研究人员。
*   希望提升 Python 代码在 GPU 环境下的执行效率和可扩展性的开发者。
*   正在实施 MLOps 策略，需标准化机器学习生命周期管理的企业。

### 4. **技术亮点**
*   聚焦于“生产级”而非仅“学术级”的机器学习工程实践。
*   紧密结合当前主流的 Transformer 架构和 Hugging Face 生态。
*   提供具体的代码示例和配置模板，可直接应用于 Slurm 和 Kubernetes 环境。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18412 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17323 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11577 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码库合集。它旨在为开发者提供丰富的实战案例，涵盖从基础算法到前沿应用的全方位技术实践。

2. **核心功能**
- 汇集500个完整的AI相关项目代码，支持多种主流技术领域。
- 覆盖机器学习、深度学习、计算机视觉和NLP等关键方向。
- 提供可直接运行的Python代码示例，便于快速学习与复现。
- 作为资源索引，帮助用户系统性地探索不同AI应用场景。

3. **适用场景**
- AI初学者希望寻找大量实战项目以巩固理论基础。
- 开发者需要参考具体代码实现来解决特定领域的技术问题。
- 教育者用于课程设计或培训，提供多样化的教学案例。

4. **技术亮点**
- 资源极其丰富，一次性整合数百个高质量开源项目。
- 标签分类清晰，便于用户根据特定技术领域快速筛选内容。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35473 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. **中文简介**
Netron 是一款支持多种神经网络、深度学习及机器学习模型的可视化工具。它能够直观地展示模型的结构和数据流，帮助用户深入理解算法原理。该工具兼容 Keras、PyTorch、TensorFlow、ONNX 等主流框架格式。

### 2. **核心功能**
*   **多格式支持**：广泛兼容 CoreML、Keras、ONNX、PyTorch、TensorFlow 等多种主流模型格式。
*   **结构可视化**：提供清晰的图形界面，直观展示神经网络的层结构、节点连接及数据流向。
*   **跨平台运行**：作为 JavaScript 项目，可轻松集成为浏览器扩展或桌面应用，实现跨平台查看。
*   **模型调试辅助**：通过可视化界面帮助用户快速定位模型结构错误并进行调试优化。

### 3. **适用场景**
*   **模型结构审查**：研究人员或工程师在训练前检查模型架构是否符合设计预期。
*   **学术交流与演示**：在论文写作或技术分享中，利用生成的图表直观展示复杂的网络结构。
*   **模型兼容性测试**：验证不同框架间模型转换（如 PyTorch 转 ONNX）后的结构一致性。

### 4. **技术亮点**
*   **轻量化部署**：基于 Web 技术构建，无需安装重型依赖即可在浏览器中流畅运行大模型可视化。
*   **高扩展性**：支持 Safetensors 等新兴格式，紧跟 AI 社区发展动态。
*   **用户友好**：界面简洁直观，即使非专业人士也能快速上手进行模型探索。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必备的核心知识速查表（Cheat Sheets）。内容涵盖从基础数学库到主流框架的关键语法和概念，旨在帮助研究人员快速回顾和掌握关键技术细节。

2. **核心功能**
*   提供针对NumPy、SciPy等科学计算库的快速参考指南。
*   包含Matplotlib数据可视化的常用代码片段与配置技巧。
*   整理Keras及深度学习框架中的关键API使用示例。
*   汇总机器学习算法与模型评估指标的核心概念对照表。

3. **适用场景**
*   研究人员在进行实验前快速复习特定库或框架的用法。
*   开发者在编写代码时遇到语法遗忘，作为即时查阅的工具。
*   学生或初学者系统性地梳理深度学习领域的核心知识点。
*   团队内部进行技术分享或新员工入职培训时的参考资料。

4. **技术亮点**
*   高度浓缩的知识呈现方式，极大降低了查阅文档的时间成本。
*   覆盖范围广泛，整合了从底层数据处理到高层建模的全栈工具链。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
这是一个全面的人工智能学习路线图项目，整理了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并实现就业实战。内容涵盖Python、数学基础、机器学习、数据分析、深度学习以及计算机视觉和自然语言处理等热门技术领域。

2. **核心功能**
*   提供系统化的AI学习路径，从基础数学到高级深度学习模型逐步深入。
*   收录近200个实战案例和项目代码，强调动手实践与就业导向。
*   免费开放配套教材和学习资源，降低人工智能领域的学习门槛。
*   覆盖主流AI框架与工具链，包括TensorFlow、PyTorch、Keras、Pandas及Matplotlib等。

3. **适用场景**
*   **零基础转行人员**：希望通过系统化路线快速掌握AI技能并进入相关行业的初学者。
*   **在校学生与研究者**：需要大量实战案例来巩固理论知识或寻找毕业设计灵感的学生。
*   **职场技能提升者**：希望补充数据分析、机器学习算法知识以增强现有工作竞争力的专业人士。

4. **技术亮点**
*   资源高度整合，将分散的知识点（如算法、库函数、框架使用）通过路线图串联成完整体系。
*   注重实战落地，不仅提供理论，更提供了丰富的代码示例和实际应用场景。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它通过声明式配置和自动化流程，大幅降低了开发复杂 AI 系统的门槛。

### 2. 核心功能
*   **低代码/无代码体验**：通过 YAML 配置文件即可定义模型架构和数据管道，无需编写大量底层代码。
*   **广泛支持的模型类型**：原生支持深度学习、传统机器学习以及最新的大语言模型（如 LLaMA、Mistral 等）的微调与训练。
*   **端到端工作流**：集成数据预处理、模型训练、评估和部署的全生命周期管理工具。
*   **多框架兼容**：底层依托 PyTorch 等主流深度学习框架，同时保持用户界面的简洁性。
*   **可解释性与可视化**：提供内置的分析工具和可视化界面，帮助开发者理解模型行为和数据分布。

### 3. 适用场景
*   **快速原型开发**：数据科学家希望在不深入底层代码的情况下，迅速验证不同 AI 模型的效果。
*   **大模型微调**：企业或研究者需要对 LLaMA、Mistral 等开源 LLM 进行特定领域数据的微调（Fine-tuning）。
*   **传统机器学习迁移**：将传统的表格型机器学习任务平滑过渡到深度学习架构，或混合使用多种模型。
*   **教育与技术培训**：作为教学工具，帮助初学者直观理解神经网络结构和训练流程。

### 4. 技术亮点
*   **声明式 API**：采用“配置即代码”的理念，使模型定义清晰、可版本控制且易于复现。
*   **数据中心主义**：强调数据质量对模型性能的影响，提供强大的数据分析和清洗工具。
*   **开箱即用的 LLM 支持**：针对当前流行的 LLM 生态提供了专门的优化模块，简化了复杂的推理和训练步骤。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9138 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6987 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6259 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
funNLP 是一个全面的中文自然语言处理（NLP）工具库和资源合集，旨在为开发者提供从基础文本处理到高级语义理解的各类实用功能。该项目集成了敏感词检测、实体抽取、情感分析及丰富的专业领域词库，并汇总了大量高质量的开源数据集、预训练模型及前沿NLP技术资源。它既是日常NLP开发的得力助手，也是学习和研究中文自然语言处理的重要资料库。

### 2. 核心功能
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词管理、拼写检查、文本纠错及标点修复等功能。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱等个人信息的自动抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
*   **语义分析与情感计算**：具备词汇情感值分析、同义词/反义词库、文本相似度匹配及情感分类能力，辅助理解文本深层含义。
*   **领域知识图谱与词库**：内置大量垂直领域词库（如汽车、医疗、法律、金融、IT等），并整合了多个开源中文知识图谱构建工具和问答数据集。
*   **语音与多模态资源**：收录了中文语音识别（ASR）数据集、发音词典、语音对齐工具及图像文字识别（OCR）相关资源。

### 3. 适用场景
*   **内容安全审核**：在互联网产品中快速部署敏感词过滤和情感监测，保障社区或平台的内容合规性。
*   **智能客服与聊天机器人开发**：利用其中的对话语料、意图识别模型及问答数据集，构建具备上下文理解和多轮对话能力的智能助手。
*   **金融/医疗/法律等行业数据分析**：借助专业的领域词库和实体抽取工具，从非结构化文档（如病历、合同、财报）中提取关键信息并构建行业知识图谱。
*   **NLP算法研究与教学**：作为研究人员或学生的资源站，快速获取最新的预训练模型（如BERT, ALBERT, RoBERTa）、基准数据集及技术报告。

### 4. 技术亮点
*   **资源高度聚合**：不仅提供代码工具，还整理了清华XLORE、百度/京东/阿里等大厂的知识图谱数据及大量学术论文代码，极大降低了NLP入门门槛。
*   **模型前沿性**：涵盖了从传统机器学习到最新深度学习（Transformer, BERT系列, GPT-2）的各类实现，包括细粒度NER和对抗样本生成等进阶技术。
*   **实用性极强**：提供了即插即用的工具包（如jieba_fast加速分词、g2pC拼音标注），解决了中文处理中常见的痛点（如多音字、缩写还原）。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100 多种模型。该项目荣获 ACL 2024 会议收录，旨在简化从指令微调到强化学习对齐的全流程操作。

2. **核心功能**
*   支持百余种主流 LLM 和 VLM 的统一高效微调。
*   集成 LoRA、QLoRA 等参数高效微调（PEFT）技术以降低资源消耗。
*   提供完整的 RLHF（基于人类反馈的强化学习）训练流程支持。
*   内置多种量化技术，实现模型压缩与加速推理。
*   兼容 Transformers 库，提供开箱即用的训练与评估接口。

3. **适用场景**
*   研究人员快速复现或改进大型语言模型的微调算法。
*   开发者针对特定垂直领域数据对开源大模型进行指令微调。
*   需要低资源环境运行下，利用 QLoRA 等技术微调千亿级参数模型。
*   构建具备多模态理解能力（如图像-文本）的定制化 AI 应用。

4. **技术亮点**
*   **统一架构**：在一个框架内无缝切换不同架构和模态的模型微调。
*   **极致效率**：通过 QLoRA 等技术显著降低显存占用，使消费级显卡也能微调大模型。
*   **前沿对齐**：原生支持 RLHF 全流程，助力模型对齐人类价值观。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73328 | 🍴 8951 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58316 | 🍴 9538 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由微软发起，通过结构化的学习路径帮助用户系统性地建立对机器学习和深度学习的理解。

2. **核心功能**
*   提供分阶段的系统化学习路线，涵盖从基础概念到高级应用的完整知识体系。
*   基于Jupyter Notebook实现交互式编程教学，便于用户边学边练。
*   内容覆盖机器学习、深度学习、自然语言处理及计算机视觉等主流AI领域。
*   包含卷积神经网络（CNN）、循环神经网络（RNN）和生成对抗网络（GAN）等具体技术专题。
*   适合零基础学习者，以“面向所有人”为理念降低AI技术的学习门槛。

3. **适用场景**
*   希望系统自学人工智能知识的初学者或跨领域转型者。
*   教育机构或企业团队用于开展AI基础技能培训和工作坊。
*   计算机科学学生作为课堂补充教材，辅助理解理论背后的代码实现。
*   开发者快速了解AI前沿趋势并尝试构建简单模型原型。

4. **技术亮点**
*   采用微软教育品牌背书，内容权威且免费开放。
*   强调实践导向，通过大量代码示例将抽象算法具象化。
*   广泛使用Jupyter Notebook格式，支持代码、文本与可视化结果的完美结合。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52378 | 🍴 10599 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解了线性代数、PyTorch及TensorFlow 2等核心工具。它旨在通过结合NLTK自然语言处理库与Scikit-learn等框架，为学习者提供从理论到实践的全方位指导。

2. **核心功能**
*   集成机器学习经典算法实战，如AdaBoost、Apriori、K-Means聚类及逻辑回归等。
*   涵盖深度学习模型实现，包括DNN、RNN、LSTM以及基于PyTorch和TensorFlow 2的应用。
*   提供自然语言处理（NLP）相关技术解析，利用NLTK进行文本分析与推荐系统构建。
*   融合数学基础与数据科学工具，讲解PCA降维、SVD分解及SVM支持向量机等关键技术。

3. **适用场景**
*   机器学习初学者希望系统掌握从线性代数基础到经典算法实现的完整路径。
*   数据科学家需要快速查阅或复现特定算法（如FP-Growth、朴素贝叶斯）的代码示例。
*   开发者致力于构建基于深度神经网络（DNN/RNN）或自然语言处理（NLP）的智能应用。

4. **技术亮点**
*   **全栈覆盖**：同时包含传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）两大体系。
*   **理论与实践结合**：不仅提供代码实现，还强调线性代数等数学底层逻辑的理解。
*   **社区高认可度**：拥有超过4.2万星标，证明其在中文机器学习学习圈中的广泛影响力和实用性。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38538 | 🍴 6462 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35473 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33746 | 🍴 4691 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28618 | 🍴 3492 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25916 | 🍴 2925 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个汇集了500个AI相关项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目提供了完整的代码实现，旨在为开发者提供从入门到进阶的实践资源。凭借其高星数和全面的分类，它是学习人工智能实战技巧的优质参考库。

### 2. 核心功能
*   **海量项目收录**：整合了500多个具体的AI工程实践案例，内容覆盖面广。
*   **全栈代码支持**：每个项目均附带可运行的源代码，便于直接复现和学习。
*   **领域细分清晰**：明确区分机器学习、深度学习、计算机视觉和NLP四大核心板块。
*   **精选优质资源**：作为“Awesome”列表，筛选了行业内高质量和具有代表性的项目。

### 3. 适用场景
*   **AI初学者入门**：适合新手通过阅读代码快速理解各子领域的经典算法实现。
*   **开发者灵感参考**：帮助工程师寻找特定任务（如图像识别或文本分类）的最佳实践方案。
*   **技术面试准备**：求职者可通过研究这些项目来掌握主流AI框架的应用细节。

### 4. 技术亮点
*   **Python生态主导**：虽然标签显示“None”，但基于领域特性，项目主要依托Python及其主流AI库（如TensorFlow, PyTorch）。
*   **高社区认可度**：拥有超过35,000颗星，证明了其内容的实用性和广泛影响力。
*   **结构化分类标签**：通过详细的标签体系（如`computer-vision-project`, `nlp-projects`），方便用户按需求精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35473 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### GitHub 项目分析：Skyvern

**1. 中文简介**
Skyvern 是一款利用人工智能自动化基于浏览器的复杂工作流工具。它通过结合大语言模型（LLM）与计算机视觉技术，能够像人类一样理解和操作网页界面。该项目旨在替代传统的 RPA（机器人流程自动化）脚本，提供更智能、更灵活的浏览器自动化解决方案。

**2. 核心功能**
*   **AI 驱动的理解能力**：利用 LLM 和视觉模型解析网页内容，动态识别元素而非依赖固定的 CSS 选择器。
*   **自适应工作流执行**：能够处理动态变化的网页结构和反作弊机制，自动完成点击、填写、导航等操作。
*   **多浏览器引擎支持**：底层兼容 Playwright 和 Puppeteer，提供高性能且稳定的浏览器控制能力。
*   **可视化与调试**：提供清晰的日志记录和可视化界面，方便开发者监控 AI 的操作决策过程。
*   **API 集成接口**：提供易于集成的 API，可轻松嵌入到现有的自动化平台或业务系统中。

**3. 适用场景**
*   **跨平台数据抓取与录入**：自动化从不同网站提取数据并录入到内部系统或数据库中。
*   **繁琐的表单填写**：批量处理需要手动填写大量信息的网页表单，如注册、报税或申请流程。
*   **企业级 RPA 升级**：作为传统 Selenium/Playwright 脚本的增强版，解决因前端结构频繁变动导致的脚本失效问题。
*   **在线服务监控与测试**：自动执行用户旅程测试，验证 Web 应用在不同状态下的功能正常性。

**4. 技术亮点**
*   **计算机视觉与大模型融合**：不仅依靠文本信息，还结合图像理解来定位页面元素，显著提高了对非结构化页面的处理能力。
*   **无头浏览器优化**：深度优化了无头模式下的操作稳定性，使其更适合服务器端部署和高并发任务。
*   **开源生态整合**：标签中涵盖了从 AI (GPT, LLM) 到自动化 (RPA, PowerAutomate) 的关键技术栈，展现了其广泛的兼容性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22423 | 🍴 2097 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的 AI 辅助标注与团队协作。它提供开源、云端和企业版产品，并集成质量保证、数据分析及开发者 API 等完善功能。

2. **核心功能**
*   支持图像、视频和 3D 数据的多种标注类型，包括边界框、语义分割和图像分类。
*   内置 AI 辅助标注功能，可显著减少人工工作量并提升标注效率。
*   提供企业级团队协作、质量保证机制以及完善的数据分析工具。
*   开放开发者 API，支持与其他系统集成，满足定制化开发需求。
*   兼容 PyTorch 和 TensorFlow 等主流深度学习框架，便于模型训练流程对接。

3. **适用场景**
*   需要大规模构建高质量数据集以训练计算机视觉模型的深度学习研究团队。
*   涉及自动驾驶或视频分析，需要对连续视频帧进行精细对象检测的企业应用。
*   需要多人协作完成复杂 3D 点云或图像标注任务的专业数据标注公司。

4. **技术亮点**
*   提供开源、云部署和企业私有化三种灵活的产品形态，适应不同规模和安全需求。
*   强大的 AI 辅助能力，通过预训练模型加速标注过程，实现人机协同的高效作业。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16310 | 🍴 3763 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
本项目专注于计算机视觉领域的高级AI可解释性研究，旨在帮助开发者理解模型的决策依据。它广泛支持卷积神经网络（CNN）、视觉Transformer等多种架构，并兼容分类、检测及分割等任务。通过提供直观的可视化手段，该工具极大地提升了深度学习模型的透明度和可信度。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种主流的可解释性算法实现。
*   兼容CNN和Vision Transformers等主流深度学习模型架构。
*   覆盖图像分类、目标检测、语义分割及图像相似度计算等多类任务。
*   提供直观的注意力图可视化，展示模型关注的图像区域。

3. **适用场景**
*   调试和验证计算机视觉模型，确保其关注点符合人类直觉。
*   医疗影像分析中，辅助医生理解AI诊断结果的依据以提高信任度。
*   自动驾驶或安防监控系统的模型审计，排查潜在的安全偏见或错误逻辑。
*   学术研究中的可解释人工智能（XAI）相关论文复现与对比实验。

4. **技术亮点**
*   拥有极高的社区关注度（逾1万星标），证明其在业界的广泛认可与稳定性。
*   模块化设计良好，能够灵活适配不同网络结构和任务类型。
*   集成了Class Activation Maps (CAM) 系列多种变体，为研究者提供丰富的选择。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12914 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它提供了可微分的图像处理原语，旨在简化计算机视觉模型的开发与集成。该库支持在深度学习流水线中直接进行几何变换和图像操作。

2. **核心功能**
*   提供完全可微分的图像处理和几何变换算子，便于嵌入深度学习网络。
*   内置丰富的计算机视觉算法，涵盖特征提取、相机标定及三维重建等模块。
*   原生支持 PyTorch 张量运算，实现与主流深度学习框架的高效无缝集成。
*   包含针对机器人学和自动驾驶优化的空间感知工具集。

3. **适用场景**
*   开发需要端到端训练的可微分计算机视觉模型或神经渲染应用。
*   在机器人导航、SLAM（同步定位与建图）中进行实时空间数据处理。
*   构建包含复杂图像预处理和后处理步骤的深度学习流水线。
*   研究计算机视觉中的几何约束优化问题。

4. **技术亮点**
*   **可微分几何**：将传统几何计算转化为可梯度传播的操作，突破了传统 CV 库无法直接反向传播的限制。
*   **PyTorch 原生集成**：无需数据格式转换，直接在 GPU 上高性能运行张量运算。
*   **模块化设计**：结构清晰，便于开发者按需组合使用不同的视觉算法模块。
- 链接: https://github.com/kornia/kornia
- ⭐ 11276 | 🍴 1202 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3457 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3284 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调“龙虾方式”的数据自主权。它允许用户完全掌控自己的数据，打造专属的个性化智能体验。

**2. 核心功能**
- 跨平台兼容，可在任何操作系统上运行。
- 提供个人化 AI 助理服务，满足多样化需求。
- 坚持数据所有权理念，确保用户隐私安全。
- 基于 TypeScript 构建，具备良好的可扩展性。

**3. 适用场景**
- 开发者希望在不依赖第三方云服务的情况下部署本地 AI 助手。
- 注重数据隐私的用户想要拥有完全属于自己的智能代理。
- 需要在不同操作系统间无缝切换的个人效率工具使用者。

**4. 技术亮点**
- 采用 TypeScript 语言开发，类型安全且生态丰富。
- 开源架构支持高度自定义和数据私有化部署。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383152 | 🍴 80473 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理式技能框架及软件开发方法论。它旨在通过结构化的智能体协作，提升软件工程的效率与质量。该项目整合了从头脑风暴到代码实现的全生命周期管理。

2. **核心功能**
- 提供基于智能体驱动的开发（Subagent-Driven Development）工作流。
- 集成头脑风暴与技能规划，辅助复杂任务的拆解。
- 覆盖完整的软件开发生命周期（SDLC），实现自动化协同。
- 具备可复用的代理技能库，支持模块化开发扩展。

3. **适用场景**
- 需要高效团队协作的大型软件开发项目。
- 利用 AI 辅助进行系统架构设计与技术选型。
- 希望标准化开发流程并提升代码质量的工程团队。

4. **技术亮点**
- 创新性地结合了“技能框架”与“开发方法论”，强调可落地的 AGI 工作流。
- 专注于多智能体协同（Agentic Skills），而非单一工具调用。
- 链接: https://github.com/obra/superpowers
- ⭐ 255891 | 🍴 22790 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. **中文简介**
Hermes Agent 是一个能够伴随用户共同成长的人工智能代理助手。它深度整合了多种大型语言模型（如 Claude、ChatGPT 等），旨在提供智能且灵活的代码辅助与交互体验。作为一个开源项目，它致力于打造一个适应性强、不断进化的开发者工具生态。

### 2. **核心功能**
*   **多模型支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT) 等多种主流 LLM 提供商。
*   **自适应成长**：代理具备记忆和学习能力，能根据用户习惯和上下文持续优化交互效果。
*   **代码辅助**：提供智能的代码生成、审查及重构建议，提升开发效率。
*   **自然语言交互**：通过直观的聊天界面处理复杂的技术问题和工作流自动化。

### 3. **适用场景**
*   **日常编码工作**：作为结对编程伙伴，快速生成样板代码或解决报错。
*   **技术文档查询**：快速检索和理解复杂的 API 文档或库的使用说明。
*   **项目初始化与重构**：协助搭建新项目结构或优化现有代码库的设计模式。

### 4. **技术亮点**
*   **高度模块化架构**：支持插件化扩展，便于集成不同的 AI 服务和自定义工具。
*   **开源社区驱动**：拥有较高的星标数（215k+），表明其活跃的开发社区和广泛的技术认可度。
*   **轻量级部署**：基于 Python 开发，易于在本地或服务器环境中快速部署和使用。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215933 | 🍴 40326 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一款采用公平代码许可的工作流自动化平台，原生集成 AI 能力。它支持可视化构建与自定义代码结合，提供 400 多种集成方式，用户可选择自托管或云端部署。

### 2. 核心功能
*   **混合式工作流构建**：结合可视化拖拽界面与自定义代码（TypeScript），满足从简单到复杂的自动化需求。
*   **广泛的集成生态**：内置 400 多个集成节点，覆盖主流 SaaS 服务和 API，轻松连接不同应用。
*   **原生 AI 支持**：具备原生 AI 能力，可直接在流程中调用大语言模型进行智能处理。
*   **灵活的部署选项**：支持自托管（Self-hosted）以确保数据隐私，也可使用云端服务以简化运维。
*   **MCP 协议支持**：作为 MCP 客户端和服务器，增强与现代 AI 工具及数据源的互操作性。

### 3. 适用场景
*   **企业业务流程自动化**：连接 CRM、ERP 和通信工具，自动执行数据同步、审批通知等重复性任务。
*   **AI 驱动的智能工作流**：利用原生 AI 功能，实现基于自然语言的文档摘要、数据分类或客服自动回复。
*   **数据管道与 ETL 处理**：整合多个数据源，进行数据清洗、转换并加载到目标数据库或分析平台。
*   **开发者快速原型开发**：通过低代码/无代码界面快速搭建后端逻辑或 API 网关，加速应用迭代。

### 4. 技术亮点
*   **TypeScript 原生架构**：代码库基于 TypeScript 构建，类型安全且易于扩展和维护。
*   **公平代码（Fair-code）许可**：在保持开源的同时允许商业使用，平衡了社区贡献与商业可持续性。
*   **MCP（Model Context Protocol）集成**：率先支持 MCP 标准，使工作流能更标准化地与各类 AI 模型和上下文交互。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196705 | 🍴 59378 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松获取、使用并构建基于 AI 的工具，实现人工智能的普及化愿景。其使命是通过提供强大的工具链，让用户能够将精力集中在真正重要的任务上。

2. **核心功能**
*   具备自主规划与执行复杂任务的能力，无需人工全程干预。
*   支持集成多种大语言模型（如 GPT、Claude、Llama），灵活适配不同需求。
*   拥有记忆机制和互联网访问能力，可进行信息检索与多步骤推理。
*   提供模块化架构，允许开发者基于现有工具快速构建自定义 AI 代理。

3. **适用场景**
*   自动化长周期的研究项目，如资料收集、整理与初步分析。
*   执行重复性高的工作流，例如内容生成、数据清洗或代码测试。
*   探索 Agent 技术边界，作为学习和开发自主 AI 系统的实验平台。
*   个人效率提升助手，用于管理日程、邮件处理或日常信息查询。

4. **技术亮点**
*   开源且社区驱动，拥有极高的活跃度（超 18 万星标）和丰富的生态插件。
*   高度可定制，支持通过配置文件灵活调整代理的行为模式与工具权限。
*   采用多代理协作思路，能够分解复杂问题并组合多种 AI 能力解决。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185581 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165864 | 🍴 21454 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164185 | 🍴 30420 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157079 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151959 | 🍴 8677 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151918 | 🍴 9582 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

