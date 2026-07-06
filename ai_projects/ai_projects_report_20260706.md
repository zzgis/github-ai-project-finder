# GitHub AI项目每日发现报告
日期: 2026-07-06

## 新发布的AI项目

### Vibe-Research
- 1. **中文简介**
Vibe-Research 是一款由 AI 驱动的个性化投研智能体，支持 A 股、美股及港股市场。它整合了每日复盘、资讯雷达、个股与板块数据、持仓管理及研究记录等功能，为用户提供一站式的投资研究解决方案。

2. **核心功能**
*   支持 A 股、美股和港股的多市场覆盖与分析。
*   提供每日复盘、资讯雷达及个股/板块数据中心。
*   集成个人持仓管理与研究记录追踪功能。
*   基于 LLM 和 MCP 协议实现 AI 自动化投研辅助。

3. **适用场景**
*   需要同时监控多个全球主要股市（A股/美股/港股）的个人投资者。
*   希望利用 AI 自动整理每日市场资讯与复盘数据的交易员。
*   注重投资逻辑沉淀，需要系统化记录研究过程和持仓变化的用户。

4. **技术亮点**
*   采用 React + TypeScript 构建前端，FastAPI + Python 处理后端逻辑。
*   集成 LLM（大语言模型）与 MCP（模型上下文协议）以增强 AI 交互能力。
- 链接: https://github.com/simonlin1212/Vibe-Research
- ⭐ 131 | 🍴 36 | 语言: TypeScript
- 标签: a-stock, ai-agent, dashboard, fastapi, fintech

### spicy-monopoly
- **1. 中文简介**
这是一个基于 Python 开发的双人棋盘小游戏，玩家可与 AI 对手进行互动博弈。游戏包含掷骰子、移动棋子及执行特定任务等机制，由代码驱动逻辑运行。该项目定位为成人向（18+）娱乐应用，强调通过编程实现的趣味性与互动性。

**2. 核心功能**
*   支持人类玩家与 AI 对手进行双人回合制对战。
*   内置掷骰子与棋盘格子移动的基础游戏机制。
*   包含“刺激性任务”或特殊互动环节，增加游戏变数。
*   全逻辑由 Python 代码控制，确保规则执行的自动化与一致性。
*   明确标注为 18+ 内容，可能涉及成熟主题或幽默元素。

**3. 适用场景**
*   编程爱好者学习如何用 Python 实现简单的游戏逻辑与状态机。
*   作为展示 AI 基础交互能力的轻量级演示项目。
*   朋友间进行非正式、轻松（且带有成人幽默）的线上娱乐对局。
*   用于测试或理解基于文本/命令行界面的回合制游戏架构。

**4. 技术亮点**
*   纯 Python 实现，无需复杂依赖，便于快速部署和理解底层逻辑。
*   将游戏状态管理与 AI 决策逻辑解耦，结构清晰。
- 链接: https://github.com/RennAkira/spicy-monopoly
- ⭐ 98 | 🍴 14 | 语言: Python

### OpenAI4S
- ### 1. 中文简介
该项目通过低成本接入豆包API，实现了类Claude Science的高级推理能力。它旨在以极低的成本（约9.9元人民币）提供强大的自然语言处理与逻辑分析服务。这是一个利用性价比极高的替代方案来复刻高端模型体验的技术尝试。

### 2. 核心功能
- 集成豆包大模型API接口，实现稳定的文本生成与交互。
- 模拟Claude Science级别的复杂逻辑推理与科学问题分析能力。
- 提供低成本的AI服务部署方案，降低用户使用高阶模型的门槛。
- 针对Python环境优化，便于开发者快速集成到现有项目中。

### 3. 适用场景
- 需要低成本进行复杂逻辑推理或科学问答的应用开发。
- 对AI响应成本敏感，但要求较高分析质量的初创项目或个人开发者。
- 测试不同大模型在特定推理任务上的表现差异。
- 构建基于高性价比API的自动化数据分析或报告生成工具。

### 4. 技术亮点
- **极致性价比**：利用豆包API的高性价比特性，大幅降低了使用高级推理模型的经济成本。
- **能力复刻**：通过特定的Prompt工程或接口封装，成功在较低成本下实现了接近Claude Science的推理效果。
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 54 | 🍴 4 | 语言: Python

### OmniPost-AI
- 描述: AI-powered Chrome extension for generating and publishing posts to Facebook, Threads, and X using ChatGPT or Gemini.
- 链接: https://github.com/wanglinsaputra/OmniPost-AI
- ⭐ 42 | 🍴 21 | 语言: TypeScript
- 标签: ai, automation, chatgpt, chrome-extension, gemini

### watch-skill
- ### 1. 中文简介
watch-skill 是一个旨在赋予 AI Agent 视频观看及自我修复能力的工具库。它支持通过 MCP、CLI 和 REST API 接入，具备场景感知帧提取、OCR、本地优先转录及持久化索引等核心功能，并引入了“THE LOOP”机制以增强交互闭环。

### 2. 核心功能
- **多模态视频理解**：结合场景感知帧提取与 OCR 技术，精准解析视频画面内容。
- **本地优先转录**：利用 Whisper 模型在本地进行语音转文字处理，保障数据隐私与效率。
- **Agent 自我修正**：支持 AI 代理观看自身工作成果并进行即时修复与迭代。
- **灵活接口集成**：提供 MCP、CLI 和 REST 多种接入方式，便于嵌入不同开发环境。
- **持久化索引管理**：建立视频内容的持久化索引，提升检索与上下文关联能力。

### 3. 适用场景
- **自动化视频内容摘要**：为 AI 代理提供视频关键帧与文本转录，辅助生成报告或摘要。
- **智能客服视频审核**：让 AI 观看客户提交的视频反馈，并通过 OCR 识别屏幕信息以解决问题。
- **代码/工作流自我调试**：AI 代理录制并观看自己的工作过程，自动发现错误并进行修正。
- **多媒体知识图谱构建**：将视频中的视觉与听觉信息结构化索引，用于长期记忆存储。

### 4. 技术亮点
- **THE LOOP 机制**：独创的自我观察与修复循环，显著提升 Agent 在处理复杂视觉任务时的准确性与鲁棒性。
- 链接: https://github.com/oxbshw/watch-skill
- ⭐ 37 | 🍴 9 | 语言: Python
- 标签: agent-tools, ai-agents, claude, claude-code, computer-vision

### bike4mind
- 描述: The open-core AI workbench — notebooks, agents, RAG, voice, and images across any model: OpenAI, Anthropic, Google, xAI, or local via Ollama/vLLM. BSL 1.1,  auto-converting to Apache-2.0 on a two-year clock. Your AI keeps running when theirs doesn't.
- 链接: https://github.com/Bike4Mind/bike4mind
- ⭐ 27 | 🍴 9 | 语言: TypeScript
- 标签: agents, ai, ai-agents, ai-workbench, anthropic

### NavoIM
- 描述: Navo IM 是一款注重隐私与实时体验的即时通讯产品。支持端到端加密、频道与 AI 助手等功能。由 Navo 团队开发与维护。
- 链接: https://github.com/aijianai/NavoIM
- ⭐ 27 | 🍴 0 | 语言: TypeScript

### coread
- 描述: Read a book together with your AI — grounded in the real text, spoiler-safe, with shared margin notes. 和你的 AI 真正共读一本书。
- 链接: https://github.com/Lumenocturne/coread
- ⭐ 26 | 🍴 3 | 语言: JavaScript

### Cognitive-Core-Skills
- 描述: A universal, industry-neutral taxonomy of cognitive core skills (perception, memory, reasoning, planning, action, verification, learning, governance) for LLMs, SLMs, AI agents, and world models — with schemas, 159 skill cards, benchmarks, and CI.
- 链接: https://github.com/eli-labz/Cognitive-Core-Skills
- ⭐ 23 | 🍴 78 | 语言: Python
- 标签: agent-skills, agentic-ai, ai-agents, ai-safety, artificial-intelligence

### threejson
- 描述: ThreeJSON is a JSON-driven declarative scene runtime for Three.js, designed for persistent, mutable and extensible 3D worlds — from human-authored scenes to AI and Agent-driven generation and control.
- 链接: https://github.com/nnrj/threejson
- ⭐ 22 | 🍴 1 | 语言: JavaScript
- 标签: 3d, json, threejs, webgl

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个全面且实用的中文自然语言处理工具集，集成了敏感词检测、语言识别、信息抽取及丰富的行业词库等资源。该项目涵盖了从基础文本处理（如分词、繁简转换）到高级任务（如命名实体识别、情感分析、知识图谱构建）的多种功能。它为开发者提供了大量预训练模型、数据集及API接口，旨在降低中文NLP应用的开发门槛。

### 2. 核心功能
*   **基础文本处理与清洗**：提供中英文敏感词过滤、语言检测、繁简体转换、停用词表及反动词表，支持手机号、身份证、邮箱等关键信息的正则抽取。
*   **丰富的行业词库与资源**：内置中日文人名库、汽车品牌、医学、法律、诗词等垂直领域词库，以及中文缩写、成语、古诗词等文化相关数据。
*   **高级NLP任务支持**：涵盖命名实体识别（NER）、关键词抽取、文本摘要、句子相似度匹配、情感分析及语音识别（ASR）相关工具和数据集。
*   **预训练模型与深度学习框架**：集成BERT、ALBERT、GPT-2等主流预训练模型的中文变体，提供基于Transformer和BiLSTM等架构的模型代码及微调示例。
*   **知识图谱与问答系统**：提供中文知识图谱构建工具、基于知识图谱的问答系统（KBQA）资源、实体链接库及跨语言知识图谱数据。

### 3. 适用场景
*   **内容安全审核平台**：利用敏感词库、暴恐词表及谣言检测工具，快速构建互联网内容的合规性审查系统。
*   **垂直领域智能客服/聊天机器人**：结合医疗、金融或通用领域的词库、知识图谱及对话数据集，训练具备专业问答能力的Bot。
*   **企业级信息抽取与数据分析**：通过NER、关系抽取及文本摘要工具，从非结构化文档（如新闻、合同、简历）中提取结构化关键信息。
*   **中文NLP研究与教学**：作为学习和复现最新NLP算法（如BERT微调、预训练模型对比）的资源仓库，适合高校学生及研究人员。

### 4. 技术亮点
*   **资源极度丰富**：不仅包含代码，还整合了大量高质量的数据集（如百度问答、医疗对话、人名库）和现成的预训练模型权重，即拿即用。
*   **全栈式工具链**：从底层的数据清洗、分词，到中层的特征工程、模型训练，再到上层的知识图谱构建和应用部署，提供了完整的解决方案参考。
*   **紧跟前沿技术**：持续收录最新的NLP研究成果，包括最新的预训练模型（如ELECTREA, ALBERT）、对抗训练方法及多模态（语音+文本）处理技术。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81635 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。该项目由社区维护，旨在为开发者提供丰富的实战案例和源代码参考。它被标记为“Awesome”列表，是学习人工智能相关技术的优质资源库。

2. **核心功能**
*   提供500多个完整的AI项目源码，覆盖主流算法与模型实现。
*   集成机器学习、深度学习、计算机视觉（CV）和自然语言处理（NLP）四大核心板块。
*   所有项目均附带可运行的Python代码，便于直接复现和学习。
*   作为综合性资源库，帮助开发者快速了解各细分领域的典型应用场景。

3. **适用场景**
*   **初学者入门**：通过阅读和运行完整代码，快速掌握AI基础概念和编程实践。
*   **项目灵感参考**：为需要构建特定AI应用（如图像识别、文本分类）的开发人员提供架构设计和代码思路。
*   **技能提升与面试准备**：通过复现经典项目，深入理解算法细节，提升解决实际问题的能力。

4. **技术亮点**
*   **规模宏大且分类清晰**：收录近500个项目并按技术领域详细标签化，检索高效。
*   **全栈式技术覆盖**：同时涵盖从传统机器学习到前沿深度学习的广泛技术栈。
*   **开源社区驱动**：拥有高星标（35k+），证明其内容质量高且受全球开发者广泛认可。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35198 | 🍴 7324 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构和数据流向。该工具兼容 JavaScript 环境，便于在不同平台上进行模型审查与分析。

2. **核心功能**
- 支持 Keras、TensorFlow、PyTorch 等多种主流深度学习框架的模型可视化。
- 提供 ONNX、CoreML、TensorFlow Lite 及 Safetensors 等格式的统一视图展示。
- 具备交互式模型结构浏览功能，允许用户展开和折叠网络层以查看细节。
- 支持在浏览器或桌面端直接打开本地模型文件，无需安装复杂依赖。
- 能够显示模型各层的参数形状及数据类型，辅助调试和性能优化。

3. **适用场景**
- 研究人员在开发新模型时，通过可视化检查网络架构是否符合设计预期。
- 工程师在部署前验证模型转换（如从 PyTorch 转为 ONNX 或 CoreML）的正确性。
- 教育场景中，教师利用 Netron 向学生直观展示神经网络的内部结构与连接方式。
- 模型审查与调试过程中，快速定位特定层的问题或异常参数配置。

4. **技术亮点**
- 广泛的格式兼容性，几乎覆盖当前所有主流的机器学习模型格式。
- 轻量级且跨平台，基于 Web 技术构建，可在浏览器中流畅运行。
- 高交互性体验，支持缩放、搜索及层级详情查看，提升分析效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33185 | 🍴 3149 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 基于您提供的信息，以下是对 GitHub 项目 **onnx** 的技术分析：

1. **中文简介**
   ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型格式的通用交换与运行。通过这一标准，开发者可以更轻松地在多种硬件和软件平台间部署AI模型。

2. **核心功能**
   *   **跨框架兼容性**：支持将 PyTorch、TensorFlow、Keras 等主流框架训练的模型转换为统一格式。
   *   **模型互操作性**：提供标准化的模型表示方法，确保模型在不同环境间的无缝迁移。
   *   **硬件加速支持**：允许模型在 CPU、GPU 等多种硬件加速器上高效执行推理。
   *   **生态工具链**：配套提供模型转换、优化及调试工具，简化部署流程。

3. **适用场景**
   *   **多框架模型迁移**：当需要将基于 TensorFlow 训练好的模型迁移至 PyTorch 环境中进行二次开发或部署时。
   *   **边缘设备部署**：在资源受限的移动设备或嵌入式系统上运行经过优化的深度学习模型。
   *   **生产环境标准化**：企业希望统一内部 AI 模型的存储和交付格式，以减少维护不同框架特定格式的开销。

4. **技术亮点**
   *   **开放社区驱动**：由 Microsoft、Facebook、Amazon 等科技巨头共同维护，拥有广泛的行业支持和标准权威性。
   *   **高性能推理后端**：拥有如 ONNX Runtime 这样的高性能推理引擎，能够针对不同硬件进行底层优化。
- 链接: https://github.com/onnx/onnx
- ⭐ 21101 | 🍴 3961 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
《Machine Learning Engineering Open Book》是一部关于机器学习工程实践的开源指南，旨在为大规模模型训练与部署提供全面的技术参考。该项目涵盖了从底层硬件优化到上层框架应用的全链路知识，是 MLOps 领域的重要资源。

### 2. 核心功能
- **全栈训练优化**：深入解析 PyTorch 和 Transformer 在大规模训练中的性能调优策略。
- **硬件与基础设施管理**：提供针对 GPU、网络存储及 Slurm 集群管理的详细配置与调试指南。
- **推理与扩展性实践**：涵盖大语言模型（LLM）的高效推理技术及系统可扩展性解决方案。
- **端到端 MLOps 流程**：整合机器学习工程的最佳实践，覆盖从开发到部署的生命周期。
- **故障排除与调试**：提供针对复杂 ML 系统的调试技巧和常见问题解决方案。

### 3. 适用场景
- **大规模 LLM 训练**：用于需要多节点 GPU 集群进行预训练或微调的大型语言模型项目。
- **高性能推理部署**：适用于对延迟和吞吐量有严格要求的生产级模型服务场景。
- **ML 基础设施搭建**：适合构建和维护基于 Slurm 或云原生环境的机器学习工程平台。
- **MLOps 团队培训**：作为新入职工程师学习机器系统工程最佳实践的内部参考资料。

### 4. 技术亮点
- **社区驱动的知识库**：拥有超过 1.8 万颗星的高人气，内容持续由社区专家更新与维护。
- **实战导向的深度解析**：不仅理论丰富，更侧重于解决实际工程中遇到的硬件瓶颈和代码效率问题。
- **跨技术栈整合**：无缝连接 PyTorch、Transformers 等主流框架与底层硬件资源的管理。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18247 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17263 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11559 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理领域。该项目由社区维护，旨在为开发者提供丰富的实战案例和源代码参考。它被标记为“Awesome”列表，是学习人工智能相关技术的优质资源库。

2. **核心功能**
*   提供500多个完整的AI项目源码，覆盖主流算法与模型实现。
*   集成机器学习、深度学习、计算机视觉（CV）和自然语言处理（NLP）四大核心板块。
*   所有项目均附带可运行的Python代码，便于直接复现和学习。
*   作为综合性资源库，帮助开发者快速了解各细分领域的典型应用场景。

3. **适用场景**
*   **初学者入门**：通过阅读和运行完整代码，快速掌握AI基础概念和编程实践。
*   **项目灵感参考**：为需要构建特定AI应用（如图像识别、文本分类）的开发人员提供架构设计和代码思路。
*   **技能提升与面试准备**：通过复现经典项目，深入理解算法细节，提升解决实际问题的能力。

4. **技术亮点**
*   **规模宏大且分类清晰**：收录近500个项目并按技术领域详细标签化，检索高效。
*   **全栈式技术覆盖**：同时涵盖从传统机器学习到前沿深度学习的广泛技术栈。
*   **开源社区驱动**：拥有高星标（35k+），证明其内容质量高且受全球开发者广泛认可。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35198 | 🍴 7324 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构和数据流向。该工具兼容 JavaScript 环境，便于在不同平台上进行模型审查与分析。

2. **核心功能**
- 支持 Keras、TensorFlow、PyTorch 等多种主流深度学习框架的模型可视化。
- 提供 ONNX、CoreML、TensorFlow Lite 及 Safetensors 等格式的统一视图展示。
- 具备交互式模型结构浏览功能，允许用户展开和折叠网络层以查看细节。
- 支持在浏览器或桌面端直接打开本地模型文件，无需安装复杂依赖。
- 能够显示模型各层的参数形状及数据类型，辅助调试和性能优化。

3. **适用场景**
- 研究人员在开发新模型时，通过可视化检查网络架构是否符合设计预期。
- 工程师在部署前验证模型转换（如从 PyTorch 转为 ONNX 或 CoreML）的正确性。
- 教育场景中，教师利用 Netron 向学生直观展示神经网络的内部结构与连接方式。
- 模型审查与调试过程中，快速定位特定层的问题或异常参数配置。

4. **技术亮点**
- 广泛的格式兼容性，几乎覆盖当前所有主流的机器学习模型格式。
- 轻量级且跨平台，基于 Web 技术构建，可在浏览器中流畅运行。
- 高交互性体验，支持缩放、搜索及层级详情查看，提升分析效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33185 | 🍴 3149 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必不可少的速查手册集合。内容涵盖相关核心库及算法的快速参考指南，旨在帮助研究人员高效查阅关键知识点。

2. **核心功能**
*   提供机器学习与深度学习领域的标准化速查表。
*   集成 NumPy、SciPy、Matplotlib 等基础科学计算库的使用技巧。
*   包含 Keras 等主流深度学习框架的核心 API 参考。
*   汇总人工智能研究中的关键概念与常用代码片段。

3. **适用场景**
*   研究人员快速回顾遗忘的库函数或算法参数。
*   初学者作为入门学习的辅助参考资料。
*   开发过程中遇到具体技术问题时的即时查询工具。
*   准备技术面试时梳理核心知识点。

4. **技术亮点**
*   高度聚焦于科研实用场景，内容精简且针对性强。
*   覆盖从数据处理到模型构建的全流程关键工具链。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目是一份全面的人工智能学习路线图，整理了近200个实战案例并提供免费配套教材，旨在帮助零基础用户从入门到精通，最终实现就业实战。内容涵盖Python、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等热门技术领域。

### 2. 核心功能
*   提供系统化的AI学习路径，涵盖从基础数学到高级算法的完整知识体系。
*   收录近200个精选实战案例与项目，通过动手实践巩固理论知识。
*   免费提供全套配套学习资料，降低学习门槛，适合初学者快速上手。
*   覆盖主流AI框架与技术栈，包括PyTorch、TensorFlow、Keras及Pandas等工具。

### 3. 适用场景
*   希望从零开始系统学习人工智能与数据科学的初学者。
*   寻求高质量实战项目以丰富简历、提升就业竞争力的求职者。
*   需要梳理知识体系、查漏补缺的数据科学家或算法工程师。
*   对计算机视觉（CV）、自然语言处理（NLP）等特定领域感兴趣的研究者。

### 4. 技术亮点
*   **资源集成度高**：将分散的知识点、代码案例和学习资料整合为一条清晰的学习路线。
*   **技术栈全面**：同时支持TensorFlow/Keras和PyTorch两大主流深度学习框架。
*   **注重实战落地**：强调“就业实战”，通过大量真实案例连接理论与工业界应用。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建流程。它通过声明式配置和极简的代码量，帮助开发者高效地进行模型训练与微调。该项目特别注重数据-centric（以数据为中心）的开发理念，降低了复杂AI应用的开发门槛。

2. **核心功能**
- 提供低代码/无代码接口，通过简单的 YAML 或 Python API 即可定义和训练深度学习模型。
- 支持广泛的数据类型处理（文本、图像、音频等）及多种主流架构（如 Transformer、CNN、RNN）。
- 内置自动化模型评估与超参数调优功能，加速实验迭代过程。
- 兼容 PyTorch 和 TensorFlow 后端，方便集成现有的深度学习生态。
- 专注于数据为中心（Data-Centric）的方法，强调数据质量对模型性能的直接影响。

3. **适用场景**
- **快速原型开发**：需要迅速验证想法，不想编写大量底层代码的数据科学家或研究人员。
- **企业级 AI 应用部署**：希望标准化模型训练流程，降低对高级编程技能依赖的工程团队。
- **多模态模型构建**：需要同时处理文本、图像、表格等多种数据类型的应用场景。
- **LLM 微调与训练**：基于开源基础模型（如 LLaMA、Mistral）进行特定领域微调的低资源团队。

4. **技术亮点**
- **声明式配置**：通过声明式语法定义模型结构，极大提升了可读性和可复现性。
- **数据中心方法论**：内置工具支持数据清洗、增强和分析，体现“数据决定模型上限”的理念。
- **开箱即用的预训练模型**：轻松加载和微调当前流行的 LLM 架构，无需从零开始训练。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8918 | 🍴 3099 | 语言: C++
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
- ⭐ 6223 | 🍴 734 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81635 | 🍴 15253 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73003 | 🍴 8924 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能通识课程，旨在让所有人轻松入门AI领域。该项目由微软发起，通过结构化的教学设计，帮助学习者从零开始掌握人工智能的核心概念与技术。

2. **核心功能**
- 提供系统化的12周学习路径，涵盖从基础理论到高级应用的完整知识体系。
- 基于Jupyter Notebook实现交互式编程练习，便于即时验证代码与理论结合。
- 内容广泛覆盖机器学习、深度学习、计算机视觉及自然语言处理等关键领域。
- 采用“面向所有人”的教学理念，降低技术门槛，适合非专业背景的学习者。

3. **适用场景**
- 初学者希望系统化、低成本地入门人工智能领域的自我提升者。
- 教育机构或企业团队用于开展AI基础技能培训与内部知识普及。
- 计算机科学相关专业的学生作为课堂补充教材或实践项目参考。

4. **技术亮点**
- 微软官方背书，确保内容的权威性与前沿性，并融入`microsoft-for-beginners`生态支持。
- 标签涵盖CNN、RNN、GAN等具体模型架构，体现从理论到具体算法实现的深度结合。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51768 | 🍴 10452 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并公开了包括 Anthropic、OpenAI、Google 及 xAI 在内的多家主流 AI 厂商的系统提示词（System Prompts）。内容涵盖 Claude、GPT、Gemini 等大模型及其相关工具的内部指令，且保持定期更新，旨在为社区提供透明的参考资源。

2. **核心功能**
*   整合多厂商大模型的底层系统指令，打破信息壁垒。
*   覆盖从基础聊天模型到代码辅助工具的全系列 AI 产品。
*   提供结构化的提示词数据，便于开发者直接查阅或引用。
*   保持高频更新，确保内容与新发布模型版本同步。

3. **适用场景**
*   **提示词工程研究**：分析头部模型如何通过系统指令引导行为，优化自身 Prompt 设计。
*   **安全与红队测试**：研究模型的安全边界和指令遵循机制，进行合规性评估。
*   **教育与技术科普**：向初学者展示大型语言模型背后的“思维链”和角色设定逻辑。

4. **技术亮点**
*   **跨平台覆盖广**：不仅包含单一厂商内容，还横向对比了 OpenAI、Anthropic、Google 等多方竞争者的策略差异。
*   **实时性与维护性**：作为持续更新的开源库，能够迅速反映最新模型版本的指令变更，具有较高的时效价值。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 50829 | 🍴 8287 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）。它结合了自然语言处理工具（NLTK）与多种经典算法，旨在为学习者提供从理论到实践的系统性指导。

2. **核心功能**
*   集成主流深度学习框架 PyTorch 和 TensorFlow 2 的实战代码。
*   包含大量经典机器学习算法的实现，如 SVM、K-Means、AdaBoost 及推荐系统算法。
*   提供自然语言处理（NLP）相关的 NLTK 库应用案例。
*   补充线性代数等数学基础，辅助理解算法背后的原理。
*   覆盖从传统统计学习到深度神经网络的完整知识体系。

3. **适用场景**
*   计算机科学或数据科学专业学生进行课程作业和期末项目参考。
*   希望系统掌握机器学习算法原理并编写代码实现的初学者。
*   需要快速查阅特定算法（如 Apriori、LSTM、PCA）实现细节的开发者。
*   准备面试或提升技能的数据分析师，用于复习经典模型和 NLP 技巧。

4. **技术亮点**
*   高度集成的全栈学习路径，将数学基础、传统 ML 与现代 DL 框架有机结合。
*   标签丰富且具体，涵盖从基础算法（Logistic, Naive Bayes）到复杂模型（RNN, DNN）的广泛领域。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42358 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37465 | 🍴 6227 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35198 | 🍴 7324 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33719 | 🍴 4691 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28375 | 🍴 3445 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25838 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集，旨在为开发者提供丰富的实战资源。它涵盖了从基础算法到前沿应用的广泛领域，并附有完整可运行的代码示例。

2. **核心功能**
*   提供500个涵盖AI各子领域的开源项目代码。
*   集成机器学习、深度学习、计算机视觉和NLP等多种技术栈。
*   以Awesome List形式整理，便于快速查找和筛选相关项目。
*   所有项目均附带源代码，支持直接运行和二次开发。
*   聚焦Python生态，符合主流AI开发语言标准。

3. **适用场景**
*   AI初学者学习不同算法模型的具体实现与代码结构。
*   研究人员寻找特定任务（如图像识别、文本分类）的参考案例。
*   开发者在构建新项目时获取灵感或复用成熟模块。
*   教育机构用于教学演示或布置编程作业的实践素材。

4. **技术亮点**
*   项目规模庞大且分类清晰，覆盖AI主要热门方向。
*   强调“带代码”的实用性，降低复现门槛。
*   利用GitHub标签系统实现高效的技术领域导航。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35198 | 🍴 7324 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. **中文简介**
Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流平台。它通过结合计算机视觉与大语言模型（LLM），能够像人类一样理解网页内容并执行操作，无需编写传统的代码脚本。该项目旨在为 RPA（机器人流程自动化）提供更智能、更具适应性的解决方案。

### 2. **核心功能**
*   **AI 驱动自动化**：利用 LLM 和计算机视觉理解网页布局及交互逻辑，自动完成点击、输入等操作。
*   **无头浏览器支持**：底层基于 Playwright 等工具实现稳定的浏览器控制，兼容多种网页环境。
*   **非侵入式集成**：通过 API 提供服务，无需修改目标网站代码即可实现自动化任务。
*   **动态页面处理**：具备处理动态加载内容、验证码及复杂表单的能力，比传统 Selenium/Puppeteer 更灵活。
*   **工作流编排**：支持定义和执行端到端的浏览器工作流，适用于跨多个步骤的业务场景。

### 3. **适用场景**
*   **企业级 RPA**：自动化处理需要登录、填写表单或从网页抓取数据的日常办公流程。
*   **数据抓取与监控**：定期访问特定网站，提取结构化数据或监控价格、库存变化。
*   **在线业务测试**：模拟用户行为对 Web 应用进行自动化测试，验证 UI 交互和功能正确性。
*   **跨平台账户管理**：批量或自动化地管理多个在线账户的设置、注册或信息更新。

### 4. **技术亮点**
*   **多模态 AI 融合**：创新性地结合了视觉识别（Computer Vision）与语义理解（LLM），解决了传统自动化脚本难以应对页面结构变化的痛点。
*   **开源生态整合**：深度集成 Playwright 和主流 LLM API，提供了比 Power Automate 等闭源工具更透明、可定制的技术栈。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22128 | 🍴 2070 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- **1. 中文简介**
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的首选平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证及团队协作，旨在简化数据标注流程。

**2. 核心功能**
*   支持图像、视频及3D点云的多种标注任务，包括边界框、语义分割等。
*   集成AI辅助标注功能，显著提升标注效率并降低人工成本。
*   提供完整的质量保证机制与团队协作工具，确保数据集的高标准一致性。
*   开放开发者API，便于与企业现有工作流及深度学习框架（如PyTorch、TensorFlow）集成。

**3. 适用场景**
*   **自动驾驶研发**：用于标注海量视频数据中的车辆、行人及交通标志，训练目标检测模型。
*   **医疗影像分析**：辅助医生或研究人员对医学图像进行高精度分割与标注，用于疾病诊断AI开发。
*   **零售视觉识别**：构建商品识别数据集，用于库存管理、顾客行为分析等智能零售场景。

**4. 技术亮点**
*   **多模态支持**：同时覆盖2D图像、视频序列和3D点云，满足多样化计算机视觉需求。
*   **智能化标注**：内置AI辅助功能，可实现半自动标注，大幅加速高质量数据集的构建过程。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16232 | 🍴 3736 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- **1. 中文简介**
该项目旨在为计算机视觉领域提供先进的AI可解释性功能。它广泛支持CNN、Vision Transformers等多种模型，涵盖分类、目标检测、分割及图像相似度等任务。

**2. 核心功能**
*   支持Grad-CAM、Score-CAM等多种可视化算法以增强模型可解释性。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
*   适用于图像分类、目标检测、语义分割等多个CV任务。
*   提供直观的注意力图（Class Activation Maps）生成与可视化。
*   基于PyTorch框架实现，便于集成到现有深度学习项目中。

**3. 适用场景**
*   研究人员需要验证模型是否关注了图像中的正确区域以提升可信度。
*   开发者在部署医疗影像或自动驾驶等高风险领域模型时进行故障排查。
*   教育场景中用于直观展示深度学习模型的内部决策过程。
*   对比不同网络架构（如CNN vs Transformer）在特定任务上的注意力分布差异。

**4. 技术亮点**
*   作为高星开源项目（12.9k+ stars），拥有广泛的社区支持和标准化接口。
*   统一了多种CAM变体（如Grad-CAM++, Score-CAM等）的实现，降低使用门槛。
*   原生适配主流CV任务，无需大量代码修改即可快速生成解释性热力图。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12900 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11267 | 🍴 1194 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3453 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3270 | 🍴 400 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2622 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2416 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. **中文简介**
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，让用户以“龙虾的方式”完全掌控自己的数据。它致力于提供跨平台、私有化的智能辅助体验。

### 2. **核心功能**
- **全平台兼容性**：支持在任何操作系统和平台上部署运行。
- **数据私有化**：强调“own-your-data”，确保用户数据的安全与自主权。
- **个人助理定位**：作为专属的个人 AI 助手，提供个性化服务。
- **开源架构**：基于 TypeScript 构建，便于社区贡献和二次开发。
- **跨设备同步**：理论上可在不同平台间无缝切换和使用。

### 3. **适用场景**
- **个人日常效率提升**：用户希望拥有一个本地化、隐私安全的 AI 助手来处理日常任务。
- **开发者技术栈整合**：TypeScript 开发者希望集成或定制自己的 AI 代理系统。
- **跨平台工作流管理**：需要在不同操作系统（如 Windows、macOS、Linux）间保持一致的 AI 辅助体验。

### 4. **技术亮点**
- **TypeScript 驱动**：利用 TypeScript 的类型安全和现代前端/后端生态优势。
- **轻量级与灵活性**：设计为可嵌入任何环境，适应性强。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381921 | 🍴 80117 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一个经过验证的智能体技能框架及软件开发方法论。它通过结构化地定义和组合AI智能体的技能，旨在提升软件开发的效率与质量。该项目为构建自动化开发工作流提供了实用的基础架构。

2. **核心功能**
- 提供模块化的“技能”定义机制，使AI智能体能够执行特定任务。
- 支持子代理驱动的开发模式，实现复杂任务的分解与并行处理。
- 整合头脑风暴、编码及SDLC（软件开发生命周期）等全流程环节。
- 具备强大的提示词工程能力，优化AI与开发者之间的交互效果。

3. **适用场景**
- 需要高度自动化代码生成与重构的敏捷开发团队。
- 希望利用AI辅助进行需求分析与架构设计的初级开发者。
- 致力于构建基于多智能体协作系统的复杂软件工程环境。

4. **技术亮点**
- 创新性地将AI技能抽象为可复用的组件，提升了开发流程的可维护性。
- 采用Shell脚本作为主要实现语言，确保了轻量级部署与跨平台兼容性。
- 链接: https://github.com/obra/superpowers
- ⭐ 247483 | 🍴 21958 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一个能够随用户共同成长和进化的智能代理系统。它旨在通过持续的学习与交互，提供更贴合个人需求的自动化辅助能力，实现人机协作的深度集成。

2. **核心功能**
- 支持多模型兼容，可灵活对接 OpenAI、Anthropic (Claude) 等主流大语言模型接口。
- 具备自主代理能力，能够理解自然语言指令并执行复杂的任务序列。
- 拥有自我进化机制，可根据用户反馈和历史交互数据优化其行为策略。
- 提供模块化架构，允许开发者自定义插件或扩展特定功能模块。

3. **适用场景**
- 个人开发者的代码辅助与自动化测试脚本生成。
- 需要跨平台工具调用的复杂工作流自动化处理。
- 希望获得个性化、持续迭代服务的智能助手构建。

4. **技术亮点**
- 集成了多种前沿 LLM 后端，打破了单一模型依赖，提升了系统的鲁棒性和灵活性。
- 采用“成长型”设计理念，强调代理在长期使用中积累上下文与偏好，而非仅作为一次性问答工具。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210106 | 🍴 38451 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个基于公平代码许可的工作流自动化平台，原生支持 AI 能力，允许用户结合可视化构建与自定义代码进行开发。它支持 400 多种集成，并提供自托管或云端部署选项，旨在降低自动化开发的门槛。

### 2. 核心功能
- **混合工作流构建**：结合可视化节点拖拽与自定义代码编写，满足从简单到复杂的自动化需求。
- **海量集成支持**：内置超过 400 种应用和 API 集成，方便连接各类第三方服务。
- **原生 AI 整合**：自带 AI 能力，可直接在工作流中调用大语言模型或其他智能服务。
- **灵活部署方式**：支持自托管以保障数据隐私，也可选择便捷的云端托管方案。
- **MCP 协议支持**：支持 Model Context Protocol (MCP) 客户端与服务端，增强与 AI 模型的交互能力。

### 3. 适用场景
- **企业级数据同步**：自动在不同 SaaS 平台（如 CRM、ERP、数据库）之间同步和转换数据。
- **AI 驱动的业务流程**：利用 LLM 自动处理客户咨询、生成内容或分析非结构化数据。
- **开发者效率工具**：通过 API 编排快速搭建后端服务逻辑或自动化测试流水线。
- **个人自动化助手**：将分散的应用通知、邮件或日程安排整合到一个统一的工作流中。

### 4. 技术亮点
- **公平代码许可证 (Fair-code)**：在保持开源精神的同时保护商业利益，允许个人和非商业用途自由使用。
- **TypeScript 架构**：基于 TypeScript 构建，提供类型安全的开发体验和良好的可扩展性。
- **MCP 原生集成**：率先支持 MCP 标准，使其成为连接 AI 应用与传统工作流的高效桥梁。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195392 | 🍴 59106 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松获取、使用和构建人工智能工具，其愿景是实现 AI 的普及化。通过提供强大的自主代理工具，它旨在让用户从繁琐的技术细节中解放出来，专注于真正重要的任务与核心价值。

2. **核心功能**
*   具备自主规划与执行复杂任务的能力，无需人工逐步干预。
*   支持多种大型语言模型（LLM），包括 OpenAI GPT、Claude 及 Llama 等。
*   提供可扩展的开发框架，允许用户基于现有工具构建自定义 AI 应用。
*   能够自动分解目标、调用工具并迭代优化以达成最终结果。

3. **适用场景**
*   自动化日常重复性工作，如数据抓取、整理或初步分析报告生成。
*   作为开发者的基础组件，用于快速原型验证或构建更复杂的智能代理系统。
*   需要跨平台操作的多步骤任务，例如自动浏览网页、查询信息并整合答案。

4. **技术亮点**
*   高度模块化的架构设计，便于集成第三方 API 和自定义工具链。
*   开源社区驱动，拥有庞大的开发者生态和活跃的贡献者网络。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185401 | 🍴 46124 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164871 | 🍴 21341 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164009 | 🍴 30384 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156834 | 🍴 46164 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151235 | 🍴 9447 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147894 | 🍴 23289 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

