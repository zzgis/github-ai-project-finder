# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### cue
- ### 1. **中文简介**
Cue 是一款开源的 macOS AI 副驾驶工具，以悬浮窗形式覆盖在屏幕上方，能够实时监听和观察你的会议内容。它具备隐藏模式，可在屏幕共享时保持静默，是 Cluely 的替代方案，并支持用户自带 API 密钥。

### 2. **核心功能**
*   **屏幕悬浮显示**：作为独立窗口漂浮在 macOS 桌面上，不干扰主应用操作。
*   **会议实时感知**：自动捕捉并处理音频和视频流，实现会议内容的实时分析。
*   **隐私保护模式**：智能识别屏幕共享状态，确保在共享屏幕时自身界面隐藏，保护用户隐私。
*   **BYOK 支持**：允许用户自行配置 AI 服务密钥，无需依赖特定服务商，增强数据控制权。
*   **开源替代方案**：提供类似 Cluely 的功能，但代码开源且去中心化，降低使用门槛。

### 3. **适用场景**
*   **远程会议记录**：在 Zoom、Teams 等视频会议中自动生成摘要或行动项。
*   **敏感商务谈判**：在需要屏幕共享演示时，仍能利用 AI 助手获取信息而不暴露辅助工具。
*   **个人知识管理**：实时整理会议要点，直接同步至笔记软件或个人知识库。
*   **开发者协作**：技术团队在代码评审会议中快速提取决策点和待办事项。

### 4. **技术亮点**
*   **隐私优先架构**：通过“自带密钥”和屏幕共享检测机制，解决企业级用户对数据泄露的顾虑。
*   **轻量级集成**：基于 JavaScript 构建，适配 macOS 原生环境，资源占用低。
*   **开源透明**：代码公开可审计，便于社区定制和二次开发。
- 链接: https://github.com/Blueturboguy07/cue
- ⭐ 264 | 🍴 58 | 语言: JavaScript

### claude-arbitrage-bot
- 1. **中文简介**
该项目是一个专为以太坊兼容网络设计的套利机器人，内置了自动化功能。它利用 Python 进行策略执行与流程控制，旨在捕捉不同链上或DEX之间的价格差异以实现获利。

2. **核心功能**
*   支持在以太坊及其兼容网络（如BSC、Polygon等）上进行跨平台套利交易。
*   集成Python脚本实现自动化的交易逻辑监控与执行流程。
*   采用Solidity编写智能合约以处理链上资产交换与资金路由。
*   具备快速响应市场波动的能力，以最小化滑点损失并最大化套利空间。

3. **适用场景**
*   去中心化交易所（DEX）之间因流动性差异产生的瞬时价格套利。
*   跨链桥接过程中的费率优化与价差捕捉。
*   高频量化交易策略的自动化部署与测试。
*   需要低成本、高效率执行的小额批量套利操作。

4. **技术亮点**
*   结合AI辅助工具（如Claude/Codex）优化代码生成与策略迭代。
*   架构轻量级，专注于以太坊生态的通用兼容性。
*   Python与Solidity混合编程模式，兼顾链下逻辑灵活性与链上执行安全性。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 164 | 🍴 74 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### skills
- 1. **中文简介**
这是一个开源的 OpenAI Codex 主题技能包，集成了 AI 主题生成器与跨平台运行时环境。它允许用户为 Codex 桌面应用创建和自定义主题，实现个性化的界面外观。

2. **核心功能**
*   提供基于 AI 的主题生成能力，可根据需求自动生成视觉样式。
*   拥有跨平台运行时支持，兼容 macOS 和 Windows 系统。
*   充当主题管理器，方便用户安装、切换和管理自定义主题。
*   利用 Chromium DevTools Protocol 实现底层界面定制与集成。
*   通过 CSS 语言定义和渲染主题样式，确保视觉效果的灵活性。

3. **适用场景**
*   希望个性化 Codex 编辑器外观，打造独特视觉体验的开发者。
*   需要快速生成并应用新主题，而非手动编写复杂 CSS 的用户。
*   在 macOS 或 Windows 环境下统一 Codex 应用风格的技术团队。
*   对 Codex 桌面应用进行深度定制或二次开发的高级用户。

4. **技术亮点**
*   结合 OpenAI Codex 能力与 Chromium 协议，实现了智能化的主题自动化生成与管理。
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 144 | 🍴 14 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### yuwen-publish-precheck
- 1. **中文简介**
这是一个专为抖音、小红书和视频号内容发布设计的 AI 预审工具。它能精准识别违规语句并引用官方规则，直接提供合规修改建议。基于 38 篇真实样本校准，项目构建了本地规则库以持续提升判定准确度。

2. **核心功能**
*   **多平台预审**：支持抖音、小红书、微信视频号的内容合规性检查。
*   **违规溯源**：明确指出踩线语句及其对应的官方规则依据。
*   **即时优化**：提供可直接使用的合规修改方案，无需二次加工。
*   **本地知识库**：积累踩坑经验形成可迭代的本地规则库，越用越准。
*   **Cursor 集成**：作为 Agent Skills 插件无缝嵌入 Cursor 编辑器工作流。

3. **适用场景**
*   自媒体运营者在内容发布前进行最终合规性自查。
*   使用 Cursor 编辑器的开发者或创作者快速集成 AI 审核能力。
*   对平台敏感词和红线规则不熟悉的新手内容创作者。
*   需要批量处理多平台发布文案的 MCN 机构或营销团队。

4. **技术亮点**
*   **规则驱动与 AI 结合**：利用 72 条官方原文引文增强判断的可解释性和准确性。
*   **实证校准**：通过 38 篇真实样本校准判定尺度，减少 AI 幻觉。
*   **生态集成**：深度适配 Cursor 的 Agent Skills 机制，实现工作流内嵌式审核。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 115 | 🍴 7 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### Awesome_ai_learning
- 由于该项目描述为“None”且标签为空，仅凭提供的元数据无法直接提取具体技术细节。基于项目名称 `Awesome_ai_learning` 及 GitHub 上同类 "Awesome" 列表的通用惯例，以下是基于该命名模式的合理分析与翻译：

1. **中文简介**
   这是一个专注于人工智能学习资源的精选集合项目，旨在为开发者提供系统化的入门指南。它汇集了高质量的教程、论文、工具和社区资源，帮助用户快速掌握AI核心技术。

2. **核心功能**
   - 整理分类的AI学习路径，涵盖从基础数学到高级算法的知识体系。
   - 收录顶尖高校课程、经典教材及最新研究论文的链接。
   - 提供主流机器学习框架（如TensorFlow、PyTorch）的实践示例。
   - 聚合活跃的开源AI项目及代码仓库，便于参考与复用。
   - 维护更新机制，确保推荐资源紧跟AI领域最新发展趋势。

3. **适用场景**
   - 初学者希望建立结构化的人工智能知识框架。
   - 研究人员需要快速查找特定领域的经典文献或最新进展。
   - 工程师在开发AI应用时寻找可靠的工具库和最佳实践案例。
   - 企业团队进行内部技术培训时的资料汇编与共享。

4. **技术亮点**
   - 采用标准化的目录结构，提升资源检索效率。
   - 社区驱动的内容维护，保证信息的时效性与多样性。
   - 跨平台资源整合，连接学术理论与工业界应用。
- 链接: https://github.com/h9-tec/Awesome_ai_learning
- ⭐ 89 | 🍴 8 | 语言: 未知

### ai-api-relay-guide
- 描述: AI 中转站推荐与 PokeAPI 评测：GPT 0.03×、Claude 0.2×
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 75 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### SuperMap
- 描述: SuperMap is a living spatial memory for embodied AI — it perceives the world, remembers its evolution, and supports reasoning and action.
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 57 | 🍴 1 | 语言: 未知

### LLMVault
- 描述: An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- 链接: https://github.com/CyberSunil/LLMVault
- ⭐ 43 | 🍴 9 | 语言: Python
- 标签: agent-security, ai-security, ai-security-tool, ctf, cybersecurity

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 43 | 🍴 2 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

### OpenMicro
- 描述: Codex Micro functionality using any Gaming Controller on any Coding Harness!
- 链接: https://github.com/stephenleo/OpenMicro
- ⭐ 39 | 🍴 3 | 语言: TypeScript
- 标签: agenticai, ai, claude, claude-code, codex

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个全面的中英双语自然语言处理（NLP）工具箱与资源合集，涵盖了从基础文本清洗、敏感词检测到高级实体识别和知识图谱构建的丰富功能。它不仅提供了大量实用的中文NLP预处理工具和词库，还汇总了业界领先的预训练模型、数据集及前沿技术论文，是开发者进行中文NLP研究的宝贵资源库。

2. **核心功能**
*   **基础文本处理与清洗**：提供敏感词检测、中英文分词、繁简转换、停用词过滤、拼写检查及文本标准化等功能。
*   **实体识别与信息抽取**：支持手机号、身份证、邮箱、地名、人名等特定格式信息的抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
*   **丰富的中文词库与数据资源**：内置中日文人名库、职业词库、汽车/医疗/法律等专业领域词库，以及海量的中文聊天语料、问答数据集和谣言数据库。
*   **预训练模型与深度学习工具**：整合了BERT、GPT-2、ALBERT、ELECTREA等多种主流中文预训练模型，并附带相应的微调代码和任务模板。
*   **多模态与垂直领域应用**：涵盖语音识别（ASR）语料、OCR文字识别、情感分析、文本摘要生成以及针对金融、医疗、法律等垂直领域的专用工具和数据集。

3. **适用场景**
*   **中文NLP算法研发**：研究人员可利用其提供的预训练模型、数据集和基准测试代码，快速开展文本分类、序列标注、问答系统等算法的实验与优化。
*   **企业级内容风控与安全**：内容审核团队可使用其敏感词库、反动词表及暴恐词表，结合自定义规则，高效识别和过滤互联网平台上的违规有害信息。
*   **垂直行业知识图谱构建**：金融、医疗或法律领域的开发者可借助其专业词库（如医学术语、法律条文）和实体抽取工具，构建高精度的行业知识图谱。
*   **智能客服与对话系统开发**：开发者可利用其中的聊天语料、对话机器人框架及多轮对话数据集，训练和部署具备上下文理解能力的智能客服或闲聊机器人。

4. **技术亮点**
该项目并非单一的软件库，而是一个高度聚合的“资源中心”，其最大亮点在于系统性地整理了中文NLP领域最全的词库、数据集及预训练模型资源，极大降低了开发者寻找和配置基础数据的门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码库合集，涵盖了机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目为开发者提供了丰富的实战案例与源代码，是系统学习人工智能技术的优质资源。

2. **核心功能**
- 汇集500个完整的AI项目代码，覆盖主流算法模型。
- 分类清晰，涵盖机器学习、深度学习、计算机视觉和NLP四大方向。
- 提供可直接运行的Python代码示例，便于快速上手实践。
- 整合了多个细分领域的专项项目，如图像识别和文本处理。

3. **适用场景**
- 初学者通过实战项目快速掌握AI基础理论与编程技能。
- 研究人员寻找特定算法（如CNN、RNN）的代码实现参考。
- 企业开发者在构建AI应用时获取灵感并复用成熟模块。
- 学生完成课程设计或毕业论文时的项目案例素材。

4. **技术亮点**
- 规模庞大且全面，一站式满足多模态AI开发需求。
- 标签体系完善，便于按技术栈精准检索相关项目。
- 社区认可度高，高星标数证明其内容的实用性和权威性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持多种深度学习框架和模型格式的可视化工具。它能够直观地展示神经网络、机器学习及深度学习模型的内部结构与数据流向。该工具旨在帮助开发者和研究人员更轻松地理解和分析复杂的模型架构。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
*   提供清晰的图形化界面，可视化神经网络的层结构、参数张量及数据流。
*   兼容多种后端框架，便于在不同深度学习生态系统中进行模型检查。
*   具备模型调试功能，帮助开发者快速定位网络结构中的潜在问题。

3. **适用场景**
*   在部署模型前，用于检查 ONNX 或 TensorFlow Lite 等导出模型的结构完整性。
*   深度学习研究人员分析复杂神经网络架构，以理解层与层之间的连接逻辑。
*   工程师排查模型推理错误时，通过可视化输入输出张量形状来验证数据流转。
*   向非技术利益相关者演示机器学习模型的工作原理和内部机制。

4. **技术亮点**
*   极高的格式兼容性，覆盖了从传统 ML 到最新大模型（如 safetensors）的主要标准。
*   开源且轻量级，无需复杂的依赖配置即可快速运行模型可视化。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习模型互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，打破平台壁垒。该标准由微软和Facebook等巨头共同推动，致力于实现跨框架的高效协作。

2. **核心功能**
*   提供统一的开放格式以存储和交换深度学习模型。
*   支持在多种框架（如PyTorch、TensorFlow、Scikit-learn）之间无缝转换模型。
*   允许模型在不同硬件加速器上高效执行推理任务。
*   建立了一套标准化的算子集，确保模型行为的一致性。

3. **适用场景**
*   需要将PyTorch训练好的模型部署到TensorRT或ONNX Runtime环境中进行加速推理。
*   在开发过程中需要在Keras、MXNet等不同框架间迁移或比较模型效果。
*   针对边缘设备或特定硬件优化模型，通过统一格式简化部署流程。
*   构建跨平台机器学习基础设施，确保模型在不同软件生态中的兼容性。

4. **技术亮点**
*   **生态整合能力强**：被主流AI框架广泛原生支持，拥有庞大的社区和工具链。
*   **高性能推理支持**：结合ONNX Runtime可实现跨CPU、GPU及专用加速器的优化执行。
*   **开放中立标准**：避免厂商锁定，促进开源社区在机器学习领域的标准化合作。
- 链接: https://github.com/onnx/onnx
- ⭐ 21160 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
《ml-engineering》是一部关于机器学习工程实践的开源书籍，全面涵盖了从模型训练到部署的全流程。它深入探讨了大规模语言模型、分布式训练以及系统优化等关键技术领域。该项目旨在为从事AI基础设施和MLOps的专业人员提供实用的指导与最佳实践。

### 2. 核心功能
*   提供大规模分布式训练和推理的系统级工程指南。
*   详解GPU资源管理、网络通信及存储优化策略。
*   涵盖PyTorch框架下的调试技巧与性能调优方法。
*   介绍Slurm作业调度器在超算集群中的实际应用。
*   解析大型语言模型（LLM）的训练、微调及部署全链路。

### 3. 适用场景
*   构建和优化大规模深度学习训练集群的工程团队。
*   需要处理海量数据和高并发推理请求的MLOps工程师。
*   致力于降低LLM训练成本并提升硬件利用率的科研人员。
*   学习高性能计算环境（如HPC）下机器学习部署最佳实践的开发者。

### 4. 技术亮点
*   **实战导向**：不仅理论丰富，更侧重于解决真实生产环境中的工程痛点。
*   **全面覆盖**：从底层硬件（GPU/网络）到上层应用（LLM/Transformer）的完整技术栈解析。
*   **社区权威**：高星标数量印证了其在机器学习工程领域的广泛认可度和参考价值。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18413 | 🍴 1175 | 语言: Python
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
- ⭐ 10667 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码库合集，涵盖了机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目为开发者提供了丰富的实战案例与源代码，是系统学习人工智能技术的优质资源。

2. **核心功能**
- 汇集500个完整的AI项目代码，覆盖主流算法模型。
- 分类清晰，涵盖机器学习、深度学习、计算机视觉和NLP四大方向。
- 提供可直接运行的Python代码示例，便于快速上手实践。
- 整合了多个细分领域的专项项目，如图像识别和文本处理。

3. **适用场景**
- 初学者通过实战项目快速掌握AI基础理论与编程技能。
- 研究人员寻找特定算法（如CNN、RNN）的代码实现参考。
- 企业开发者在构建AI应用时获取灵感并复用成熟模块。
- 学生完成课程设计或毕业论文时的项目案例素材。

4. **技术亮点**
- 规模庞大且全面，一站式满足多模态AI开发需求。
- 标签体系完善，便于按技术栈精准检索相关项目。
- 社区认可度高，高星标数证明其内容的实用性和权威性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持多种深度学习框架和模型格式的可视化工具。它能够直观地展示神经网络、机器学习及深度学习模型的内部结构与数据流向。该工具旨在帮助开发者和研究人员更轻松地理解和分析复杂的模型架构。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
*   提供清晰的图形化界面，可视化神经网络的层结构、参数张量及数据流。
*   兼容多种后端框架，便于在不同深度学习生态系统中进行模型检查。
*   具备模型调试功能，帮助开发者快速定位网络结构中的潜在问题。

3. **适用场景**
*   在部署模型前，用于检查 ONNX 或 TensorFlow Lite 等导出模型的结构完整性。
*   深度学习研究人员分析复杂神经网络架构，以理解层与层之间的连接逻辑。
*   工程师排查模型推理错误时，通过可视化输入输出张量形状来验证数据流转。
*   向非技术利益相关者演示机器学习模型的工作原理和内部机制。

4. **技术亮点**
*   极高的格式兼容性，覆盖了从传统 ML 到最新大模型（如 safetensors）的主要标准。
*   开源且轻量级，无需复杂的依赖配置即可快速运行模型可视化。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的技术速查手册（Cheat Sheets）。内容涵盖了从基础数学库到主流深度学习框架的核心代码片段与用法指南。旨在帮助研究者快速回顾关键概念并提高开发效率。

2. **核心功能**
- 提供机器学习与深度学习领域的常用语法和函数速查表。
- 集成 NumPy、SciPy 等科学计算库的基础操作示例。
- 包含 Matplotlib 数据可视化库的关键绘图技巧。
- 汇总 Keras 等深度学习框架的核心 API 用法。

3. **适用场景**
- 研究人员在调试代码时快速查阅特定函数的参数或用法。
- 初学者学习机器学习基础知识时作为辅助记忆工具。
- 工程师在进行原型开发时需要快速实现常见算法逻辑。
- 团队内部知识共享，统一常用库的使用规范。

4. **技术亮点**
- 内容高度浓缩，专注于实用代码片段而非冗长理论。
- 覆盖从数据处理到模型构建的全流程关键知识点。
- 格式清晰直观，适合打印或屏幕快速检索。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份详尽的人工智能学习路线图，收录了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并提升就业竞争力。该资源覆盖 Python、机器学习、深度学习、自然语言处理及计算机视觉等主流技术领域，是系统掌握 AI 技能的优质学习资料库。

2. **核心功能**
*   提供结构化的 AI 学习路径，涵盖从基础数学到高级算法的完整知识体系。
*   整合近200个实战案例与项目代码，强调动手实践以巩固理论知识。
*   免费提供配套的教材与学习资料，降低人工智能领域的入门门槛。
*   支持多种主流深度学习框架（如 PyTorch、TensorFlow、Keras 等），适应不同技术栈需求。

3. **适用场景**
*   **零基础转行/入门**：适合希望从零开始系统学习人工智能，缺乏明确学习方向的初学者。
*   **求职实战准备**：适用于需要积累项目经验、构建作品集以提升就业竞争力的求职者。
*   **技能查漏补缺**：适合已有一定基础的学习者，通过路线图和案例复习特定领域（如 CV、NLP）的知识。

4. **技术亮点**
*   内容覆盖面广且紧跟热点，集成 Python 数据科学生态（NumPy, Pandas, Matplotlib 等）及主流 AI 框架。
*   高人气验证，拥有超过 1.3 万星标，证明其社区认可度和资料质量较高。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建流程。它通过声明式配置和自动化训练机制，降低了深度学习应用的开发门槛。

2. **核心功能**
*   支持通过简单的配置文件快速定义和训练多种机器学习及深度学习模型。
*   内置对主流架构（如 PyTorch）的支持，并兼容 Llama、Mistral 等大语言模型的微调。
*   提供端到端的自动化数据预处理、特征工程及模型评估管道。
*   具备强大的可视化界面，便于监控训练进度和分析模型性能。
*   采用数据-centric 设计理念，强调通过优化数据而非仅调整模型结构来提升效果。

3. **适用场景**
*   需要快速原型化开发或微调 Llama、Mistral 等大语言模型的团队。
*   希望在不编写复杂代码的情况下构建计算机视觉或自然语言处理任务的工程师。
*   致力于通过数据驱动方式改进模型性能的数据科学家。
*   寻求标准化、可复现的机器学习实验工作流的研究人员。

4. **技术亮点**
*   **低代码/声明式接口**：通过 YAML 或 JSON 配置即可定义复杂模型结构，极大提升开发效率。
*   **广泛的模型兼容性**：无缝集成 Hugging Face Transformers 库，支持主流开源 LLM 的微调与部署。
*   **自动化流水线**：自动处理数据清洗、特征嵌入及超参数搜索，减少人工干预。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9139 | 🍴 1236 | 语言: Python
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
- **1. 中文简介**
该项目是一个全面的中英文自然语言处理（NLP）资源集合与工具库，涵盖了从基础的数据集、词库到先进的预训练模型及各类NLP任务代码。它集成了敏感词过滤、实体抽取、知识图谱构建、语音识别及文本生成等多种功能，旨在为开发者提供一站式的中文NLP解决方案。

**2. 核心功能**
*   **基础数据处理与增强**：提供繁简体转换、中英文敏感词检测、文本纠错、数据增强（EDA）及拼写检查等工具。
*   **实体抽取与信息提取**：内置身份证、手机号、邮箱等正则抽取，支持基于BERT等模型的命名实体识别（NER）及关系抽取。
*   **丰富的词库与知识资源**：收录中日文人名库、行业词库（汽车、医疗、法律等）、停用词、情感值词典及大规模百科知识图谱数据。
*   **预训练模型与前沿算法**：整合了BERT、RoBERTa、ALBERT、ELECTRA等主流预训练模型代码，以及文本分类、摘要、问答系统等深度学习任务实现。
*   **语音与多模态支持**：包含中文语音识别（ASR）模型、语音情感分析、OCR文字识别及音素对齐工具。

**3. 适用场景**
*   **中文NLP初学者与研究者**：用于快速了解中文NLP领域的常用数据集、基准测试（Benchmark）及经典算法实现。
*   **企业级内容审核系统开发**：利用其敏感词库、情感分析及谣言检测工具，构建高效的互联网内容安全过滤平台。
*   **垂直领域知识图谱构建**：借助其提供的医疗、法律、金融等领域专用词库及实体抽取代码，加速行业知识图谱的建设。
*   **智能客服与对话系统研发**：参考其对话数据集、意图识别模型及多轮对话框架代码，开发具备语义理解能力的聊天机器人。

**4. 技术亮点**
*   **极高的资源覆盖率**：不仅包含代码，还汇集了清华XLORE、百度问答集等大量高质量公开数据集和学术报告，是中文NLP资源的“百科全书”。
*   **紧跟前沿技术迭代**：持续更新包括BERT、GPT-2、Transformer等最新深度学习架构的应用案例和预训练模型，保持技术先进性。
*   **实用工具链完整**：提供了从数据预处理（如分词、标注）到模型训练（如Jieba加速版、SpaCy中文模型）再到评估指标的全流程工具支持。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73328 | 🍴 8951 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- **1. 中文简介**
该项目收集并提取了包括 Anthropic (Claude)、OpenAI (ChatGPT/Codex)、Google (Gemini) 及 xAI 等多家主流厂商的高级模型系统提示词。内容涵盖 Claude Fable 5、Opus 4.8、GPT-5.6 等多个版本及 Cursor、VS Code 等开发工具的内部指令。项目会定期更新，旨在为研究者和开发者提供全面的 AI 系统提示词参考库。

**2. 核心功能**
*   **多厂商聚合**：整合了 Anthropic、OpenAI、Google 和 xAI 等主要 AI 提供商的系统提示词。
*   **版本覆盖广**：包含从基础模型到前沿版本（如 GPT-5.6、Claude Opus 4.8）的详细指令数据。
*   **工具链集成**：不仅限于聊天机器人，还收录了 Cursor、Copilot、VS Code 等开发辅助工具的底层提示词。
*   **持续动态更新**：保持高频更新以反映最新发布的模型指令变化。

**3. 适用场景**
*   **提示词工程研究**：分析顶级 AI 模型的底层逻辑和优化指令结构。
*   **AI 安全与红队测试**：通过审查系统提示词，评估大语言模型的安全边界和潜在漏洞。
*   **开发者借鉴学习**：参考成熟产品的提示词设计模式，优化自研 AI 应用或智能体（Agent）的行为。

**4. 技术亮点**
*   **开源社区驱动**：作为 Awesome 列表类项目，依靠社区力量持续挖掘和验证泄露或公开的系统指令。
*   **跨平台对比分析**：提供不同竞品（如 Claude vs GPT）在相同任务下的指令差异，便于横向比较。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58351 | 🍴 9546 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. **中文简介**
该项目是一套为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI技术。内容涵盖从基础概念到深度学习的具体实践，通过结构化的教学计划帮助初学者掌握人工智能的核心知识。

### 2. **核心功能**
*   **系统化课程体系**：提供12周、24节课的完整学习路径，循序渐进地引导学习者。
*   **多模态AI技术覆盖**：内容广泛涉及机器学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等主流领域。
*   **交互式实战演练**：主要采用Jupyter Notebook格式，支持代码即时运行与可视化分析，便于动手实践。
*   **微软教育背书**：作为“Microsoft for Beginners”系列的一部分，内容经过专业审核，适合零基础用户。

### 3. **适用场景**
*   **高校或培训机构**：作为人工智能导论课程的标准化教学大纲和辅助教材。
*   **企业内训**：用于非技术背景员工或初级开发人员的人工智能基础知识普及。
*   **个人自学**：希望系统性地从零开始构建AI知识体系，并需要代码练习的自学者。

### 4. **技术亮点**
*   **全栈AI技术栈展示**：在单一项目中整合了RNN、CNN、GAN等多种深度学习架构的教学实例。
*   **低门槛实践环境**：基于Jupyter Notebook，无需复杂的环境配置即可在浏览器中直接运行和分析AI模型。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52379 | 🍴 10600 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个集数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）于一体的综合性学习资源库。它涵盖了从自然语言处理（NLTK）到各类经典算法及现代神经网络模型的完整知识体系。旨在为学习者提供从理论到代码实践的全面指导。

2. **核心功能**
- 提供数据分析与线性代数的数学基础教程及代码实现。
- 包含多种经典机器学习算法（如SVM、KMeans、AdaBoost等）的实战案例。
- 集成深度学习框架（PyTorch和TensorFlow 2）进行DNN、RNN、LSTM等模型训练。
- 涵盖自然语言处理（NLP）核心技术，包括使用NLTK进行文本预处理和分析。
- 提供推荐系统、回归分析及降维技术（PCA、SVD）等专项应用示例。

3. **适用场景**
- 机器学习初学者希望系统化掌握从统计学基础到高级算法的完整路径。
- 数据科学家需要快速查阅和复现经典算法（如Apriori、逻辑回归）的标准代码。
- 深度学习从业者希望对比实验PyTorch与TensorFlow 2在不同任务上的表现。
- NLP研究人员利用NLTK库进行文本挖掘、分词及基础语义分析的教学与研究。

4. **技术亮点**
- 技术栈全面，无缝衔接传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）。
- 标注清晰，通过丰富的标签体系（如adaboost, lstm, nlp）便于针对性检索和学习。
- 注重实战，将复杂的数学原理转化为可运行的Python代码，降低学习门槛。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38553 | 🍴 6466 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33745 | 🍴 4691 | 语言: Python
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
该项目是一个汇集了500个AI相关代码示例的综合资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的可执行代码，帮助开发者快速理解并应用各类人工智能算法与技术。作为一个被广泛认可的“Awesome”列表，它是学习AI实战开发的重要参考资料。

### 2. 核心功能
*   **全栈AI覆盖**：包含机器学习、深度学习、计算机视觉和NLP四大领域的完整项目案例。
*   **代码即学即用**：提供可直接运行的Python代码，便于开发者快速上手和调试。
*   **结构化资源整理**：以清晰的分类组织500多个项目，降低资料查找难度。
*   **社区认可的高质量列表**：拥有超过3.5万星标，代表其内容的实用性和权威性。

### 3. 适用场景
*   **初学者入门实践**：适合AI新手通过阅读和运行代码快速建立对主流算法的直观认识。
*   **项目灵感获取**：开发者可参考其中的案例结构，为自己的研究或业务寻找技术解决方案。
*   **面试与技能复习**：求职者可通过熟悉这些经典项目来准备技术面试或巩固基础知识。

### 4. 技术亮点
*   **多领域整合**：在一个仓库中集中展示了从传统机器学习到前沿深度学习的广泛技术栈。
*   **高活跃度与维护**：作为热门的Awesome列表，持续更新以适应AI技术的快速发展。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化处理各种基于浏览器的业务流程。它利用计算机视觉和大型语言模型（LLM），无需编写复杂代码即可操控网页，实现类似 RPA 的操作效率。

2. **核心功能**
*   通过 AI 视觉识别和 LLM 推理，自动解析并操作动态网页界面。
*   支持无缝集成主流浏览器自动化框架（如 Playwright、Puppeteer）及传统工具（如 Selenium）。
*   提供 API 接口，便于将浏览器自动化能力嵌入到现有的企业工作流或系统中。
*   具备类 RPA（机器人流程自动化）能力，可跨多个网站执行复杂的任务序列。

3. **适用场景**
*   **数据抓取与录入**：从结构不固定或动态加载的网站自动提取数据并填入内部系统。
*   **跨平台工作流自动化**：模拟人工操作，在多个不同的 Web 应用之间完成审批、下单或信息同步等任务。
*   **替代传统 RPA**：为那些因页面频繁变动导致传统脚本失效的业务场景，提供更具适应性的 AI 驱动解决方案。

4. **技术亮点**
*   结合计算机视觉与大语言模型，实现了“所见即所得”的智能网页交互，降低了对特定 DOM 结构的依赖。
*   兼容性强，既保留了 Playwright/Puppeteer 的高效执行能力，又融入了 GPT 等模型的语义理解优势。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22439 | 🍴 2097 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### GitHub 项目分析报告：CVAT

**1. 中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的领先平台，提供开源、云及企业级产品。它支持图像、视频和 3D 数据的 AI 辅助标注、质量保证及团队协作，旨在加速视觉 AI 的发展。

**2. 核心功能**
*   支持图像、视频及 3D 点云数据的多模态高精度标注。
*   提供 AI 辅助自动标注功能，显著提升数据集制作效率。
*   具备完善的质量保证机制与团队协作管理工具。
*   开放开发者 API，便于集成到现有的机器学习工作流中。

**3. 适用场景**
*   **自动驾驶开发**：用于训练目标检测和语义分割模型的数据集标注。
*   **医疗影像分析**：对 CT、MRI 等医学图像进行精细化病灶标记。
*   **工业质检系统**：标注缺陷图片或视频以训练自动化检测算法。
*   **通用视觉研究**：为图像分类或人脸识别任务构建大规模基准数据集。

**4. 技术亮点**
*   兼容主流深度学习框架（如 PyTorch、TensorFlow）及数据集格式（如 ImageNet）。
*   提供从开源本地部署到云端托管的灵活部署方案。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16310 | 🍴 3763 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目提供了用于计算机视觉的高级AI可解释性工具。它支持CNN、Vision Transformers等多种模型，涵盖分类、目标检测、分割及图像相似度等任务。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种可视化解释算法。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
*   适用于图像分类、目标检测、语义分割及图像相似度计算。
*   提供直观的注意力图生成，帮助理解模型决策依据。

3. **适用场景**
*   深度学习模型的可解释性分析与调试。
*   计算机视觉研究中对比不同模型的注意力机制。
*   医疗影像或自动驾驶等领域中验证模型判断逻辑的可靠性。
*   向非技术人员展示AI系统为何做出特定预测。

4. **技术亮点**
*   高度模块化设计，轻松适配多种主流PyTorch视觉模型。
*   同时支持经典CNN与现代Vision Transformer架构的解释。
*   拥有高社区认可度（近1.3万星标），文档完善且维护活跃。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12914 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它旨在为深度学习应用提供可微分的传统计算机视觉算法和图像处理工具。该项目由 AI 与机器人研究团队 Kornia 开发，致力于弥合传统 CV 与深度学习之间的差距。

### 2. 核心功能
*   **可微分图像处理**：提供大量可微分的传统计算机视觉操作，便于集成到神经网络训练流程中。
*   **几何计算机视觉**：包含相机标定、立体匹配、结构从运动（SfM）等高级几何算法的实现。
*   **PyTorch 原生支持**：完全基于 PyTorch 张量构建，确保与主流深度学习框架无缝兼容和高性能计算。
*   **自动化数据增强**：提供丰富的图像增强技术，特别适用于计算机视觉模型的鲁棒性训练。
*   **空间 AI 工具箱**：集成了用于机器人、自动驾驶等场景的空间推理和感知模块。

### 3. 适用场景
*   **深度学习模型训练**：在需要可微分预处理或后处理的 CNN/RNN 架构中使用，如自监督学习。
*   **机器人视觉系统**：用于机器人的环境感知、物体定位和导航中的几何计算任务。
*   **工业图像检测**：结合传统 CV 精度与深度学习灵活性，进行高精度的缺陷检测或尺寸测量。
*   **学术研究与原型开发**：快速实现包含几何约束的视觉算法，加速空间 AI 领域的创新实验。

### 4. 技术亮点
*   **全可微流水线**：这是 Kornia 最显著的技术优势，允许整个计算机视觉处理链（从图像预处理到几何变换）通过反向传播进行优化，这在传统 OpenCV 中难以直接实现。
*   **社区活跃与标准化**：作为 Hacktoberfest 参与项目且拥有高星标数，表明其在开发者社区中具有广泛影响力和持续的维护活力。
- 链接: https://github.com/kornia/kornia
- ⭐ 11275 | 🍴 1202 | 语言: Python
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
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调数据私有化与自主掌控。它采用独特的“龙虾”风格（The lobster way），让用户能够完全拥有自己的 AI 体验。

2. **核心功能**
- 跨平台兼容：支持在任何操作系统和设备上运行。
- 数据私有化：强调“Own Your Data”，确保用户数据的安全与自主权。
- 个性化 AI 助手：提供专属的个人智能助理服务。
- 开源自由：作为开源项目，允许用户自定义和扩展功能。

3. **适用场景**
- 注重隐私的个人用户希望部署本地化的 AI 助手以避免数据泄露。
- 开发者或技术爱好者希望在多种操作系统（如 Linux、macOS、Windows）上统一使用同一个 AI 工具。
- 企业或个人希望构建完全可控、不依赖第三方云服务的定制化 AI 工作流。

4. **技术亮点**
- 基于 TypeScript 开发，具备良好的类型安全和现代前端/全栈生态兼容性。
- 架构设计灵活，支持“Any OS, Any Platform”的广泛适配能力。
- 社区活跃，标签中包含“molty”等独特标识，体现其开源社区的个性化文化。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383162 | 🍴 80478 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一个经过验证的智能体技能框架与软件开发方法论，旨在通过系统化流程提升开发效率。它结合了脑暴、编码及子代理驱动开发（Subagent-Driven Development），为软件开发生命周期（SDLC）提供了一套可落地的解决方案。

2. **核心功能**
- 提供结构化的智能体技能框架，支持模块化开发流程。
- 采用子代理驱动开发模式，实现任务的自动化分解与执行。
- 集成头脑风暴与代码生成能力，辅助创意构思与实现。
- 涵盖完整的软件开发生命周期（SDLC），从规划到交付。
- 基于 Shell 脚本实现，确保在主流操作系统上的兼容性与易用性。

3. **适用场景**
- 需要引入 AI 智能体辅助自动化测试或部署流程的开发团队。
- 希望通过结构化方法论提升大型软件项目协作效率的组织。
- 利用子代理进行复杂任务分解以提高编码生产力的开发者。
- 寻求标准化技能框架以整合多种 AI 工具链的技术架构师。

4. **技术亮点**
- 创新性地将“技能框架”与“开发方法论”结合，不仅提供工具更提供流程规范。
- 强调“Subagent-Driven-Development”，利用多个智能体协同工作处理复杂逻辑。
- 作为高星项目（25万+ Star），证明了其理念在开源社区的广泛认可与实践价值。
- 链接: https://github.com/obra/superpowers
- ⭐ 255944 | 🍴 22791 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够随用户共同成长并适应个人工作流的智能代理工具。它旨在通过整合多种先进的语言模型，为用户提供持续进化的辅助体验。该项目致力于打造一个灵活且强大的 AI 助手生态。

2. **核心功能**
*   支持接入 Anthropic、OpenAI 等多个主流大语言模型后端。
*   具备上下文学习能力，能根据交互历史优化后续表现。
*   提供模块化的架构设计，便于开发者自定义功能扩展。
*   集成代码执行与环境交互能力，实现自动化任务处理。

3. **适用场景**
*   开发者日常编码辅助与复杂逻辑调试。
*   需要个性化记忆与长期上下文管理的智能对话应用。
*   构建基于 LLM 的自动化工作流与任务编排系统。

4. **技术亮点**
*   兼容 Claude Code、Codex 等多种前沿 AI 代理协议与接口。
*   采用 Python 编写，拥有活跃的开源社区与高关注度。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215968 | 🍴 40354 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个支持公平代码许可的工作流自动化平台，具备原生 AI 能力并集成了 400 多种应用。它允许用户结合可视化构建与自定义代码，可选择自托管或云端部署。

### 2. 核心功能
*   **混合工作流构建**：支持低代码/无代码的可视化拖拽与高级自定义代码相结合的开发方式。
*   **强大的集成生态**：内置超过 400 种第三方应用和 API 的连接器，实现数据无缝流转。
*   **原生 AI 集成**：深度整合人工智能能力，可直接在工作流中调用 LLM 进行智能处理。
*   **灵活的部署选项**：提供完全自托管（Self-hosted）以保障数据隐私，以及便捷的云端服务选项。

### 3. 适用场景
*   **企业级自动化运营**：用于连接 CRM、ERP 等内部系统，自动执行数据同步、邮件通知等业务逻辑。
*   **AI 驱动的数据处理**：利用其原生 AI 功能，自动化清洗、分析非结构化数据或生成内容摘要。
*   **开发者工具链整合**：作为 CI/CD 流水线的一部分，自动触发测试、部署通知或代码审查流程。

### 4. 技术亮点
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，增强了与各类 AI 模型及客户端的互操作性。
*   **TypeScript 架构**：基于 TypeScript 开发，保证了代码的类型安全、可维护性及优秀的扩展性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196723 | 🍴 59379 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
   AutoGPT 致力于实现人人可及的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，使开发者能够专注于核心业务逻辑而非底层实现。

2. **核心功能**
   - 支持自主规划与执行复杂的多步骤任务。
   - 兼容多种大型语言模型（LLM）后端，如 GPT、Claude 和 Llama。
   - 具备联网搜索、文件读写及代码解释器等外部工具调用能力。
   - 提供模块化架构，便于用户自定义智能体行为或集成新插件。

3. **适用场景**
   - 自动化日常办公流程，如信息搜集、报告生成和数据整理。
   - 作为研究助手，自动浏览网页并汇总特定主题的综合信息。
   - 开发基于 LLM 的自定义智能体原型，验证 Agent 交互逻辑。

4. **技术亮点**
   - 原生支持多模型切换，包括 OpenAI API 及本地部署的 Llama/Claude 接口。
   - 采用“记忆”机制（短期上下文与长期向量存储结合），增强任务连贯性。
   - 开源且高度可定制，拥有活跃的社区贡献和丰富的插件生态系统。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185582 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165864 | 🍴 21453 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164187 | 🍴 30421 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157079 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 152003 | 🍴 8678 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151919 | 🍴 9582 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

