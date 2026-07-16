# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### cue
- 1. **中文简介**
Cue 是一款开源的 macOS AI 智能副驾，以悬浮窗形式覆盖在屏幕之上，能够实时“观看”和“聆听”你的会议内容。它具备独特的隐私保护机制，确保在屏幕共享时保持隐藏，同时支持用户自带 API Key（BYOK），是 Cluely 的替代方案。

2. **核心功能**
*   **屏幕悬浮与监听**：在 macOS 上以浮动窗口运行，实时捕捉屏幕视觉信息和麦克风音频输入。
*   **会议辅助分析**：自动识别并处理会议内容，提供类似 AI 助手的功能。
*   **屏幕共享隐私保护**：智能检测屏幕共享状态并自动隐藏自身，防止会议参与者看到该工具。
*   **自带密钥模式**：允许用户自行配置 API 密钥，不依赖官方账号体系，提升数据控制权。
*   **Cluely 替代方案**：作为同类产品的开源替代品，提供更灵活的部署和使用方式。

3. **适用场景**
*   **远程会议记录**：在 Zoom、Teams 等会议中自动生成笔记或摘要，无需手动记录。
*   **敏感信息保护**：在进行客户演示或内部汇报等需要屏幕共享的场景下，安全地使用 AI 助手而不泄露工具存在。
*   **个人效率提升**：用于日常在线学习或网络研讨会，实时获取 AI 辅助的观点总结和问题解答。
*   **隐私优先的技术栈**：适合对数据隐私要求极高，希望完全掌控 API 密钥和用户数据的 macOS 用户。

4. **技术亮点**
*   **开源且轻量**：基于 JavaScript 开发，为 macOS 用户提供了一个轻量级的本地化 AI 集成方案。
*   **动态可见性控制**：实现了针对屏幕共享场景的自动化 UI 隐藏逻辑，解决了传统 AI 工具在共享屏幕时的尴尬问题。
- 链接: https://github.com/Blueturboguy07/cue
- ⭐ 250 | 🍴 57 | 语言: JavaScript

### claude-arbitrage-bot
- 1. **中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，具备内置的Python自动化能力。该项目利用AI辅助工具（如Claude和Codex）进行智能合约的开发与管理，旨在实现跨链或去中心化交易所之间的套利操作。

2. **核心功能**
*   支持在以太坊及其兼容链路上执行自动化的套利交易策略。
*   集成Python脚本以实现交易流程的自动化控制和执行。
*   包含智能合约代码，用于与去中心化金融协议交互。
*   利用AI编程助手生成和优化合约逻辑，降低开发门槛。

3. **适用场景**
*   DeFi爱好者希望在以太坊生态中实施自动化的套利策略以获取收益。
*   开发者希望借助AI工具快速构建和测试以太坊兼容网络的交易机器人原型。
*   需要自动化脚本处理高频或复杂跨平台交易逻辑的技术团队。

4. **技术亮点**
*   创新性地将AI大模型（Claude/GPT）与Solidity智能合约及Python自动化相结合。
*   针对以太坊兼容网络优化，具备良好的跨链适应性。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 164 | 🍴 74 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### skills
- 1. **中文简介**
这是一个开源的 OpenAI Codex 主题技能（Skill），包含一个 AI 驱动的主题生成器以及用于自定义 Codex 桌面主题的跨平台运行时环境。它允许用户通过编程方式定制 Codex 的外观和界面风格。

2. **核心功能**
*   提供基于 AI 的自动化主题生成能力，简化自定义过程。
*   实现跨平台运行时支持，兼容 macOS 和 Windows 系统。
*   允许用户创建和管理自定义的 Codex 桌面主题。
*   作为 OpenAI Codex 的扩展技能（Skill）集成到工作流中。

3. **适用场景**
*   希望个性化定制 Codex 编辑器视觉风格的高级开发者。
*   需要快速生成特定配色或布局主题的团队成员。
*   致力于探索 Chromium DevTools Protocol 应用的技术爱好者。

4. **技术亮点**
*   基于 Node.js 构建，利用 CSS 实现灵活的样式控制。
*   深度集成 Chromium DevTools Protocol，实现底层界面定制。
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 142 | 🍴 14 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### yuwen-publish-precheck
- ### 1. 中文简介
该项目是一个针对抖音、小红书及微信视频号的发布前内容合规性检查工具，利用 AI 识别违规风险点并依据官方规则提供可直接使用的修改建议。项目通过 38 篇真实样本校准判定尺度，并整合了 72 条可查证的官方规则原文，旨在帮助用户降低踩线成本。它强调本地规则库的迭代优化，但不承诺绝对过审，也不提供规避审核的技巧。

### 2. 核心功能
*   **多平台合规检测**：支持对抖音、小红书和微信视频号的内容进行发布前的风险扫描。
*   **违规定位与溯源**：精准指出文案中具体的“踩线”语句，并引用对应的官方规则条款作为依据。
*   **智能修改建议**：提供经过优化的替代文案，确保用户可以直接复制使用以符合平台规范。
*   **本地规则库积累**：基于真实样本校准判定标准，随使用次数增加而不断提升检测准确度。
*   **Cursor 集成技能**：作为 Agent Skills 设计，可无缝集成到 Cursor 编辑器中辅助写作流程。

### 3. 适用场景
*   **自媒体创作者**：在发布短视频脚本或图文笔记前，快速自查是否存在违禁词或敏感话题。
*   **电商运营人员**：检查商品详情页或广告文案，避免因违反平台宣传规则导致下架或处罚。
*   **内容审核团队**：利用 AI 预筛机制提高人工审核效率，聚焦处理复杂或边缘案例。
*   **营销文案策划**：在撰写多平台分发内容时，确保文案同时符合不同平台的社区规范。

### 4. 技术亮点
*   **基于真实数据校准**：利用 38 篇真实样本调整 AI 判定尺度，比通用模型更贴合平台实际审核逻辑。
*   **可验证的规则引用**：内置 72 条官方原文引文，使 AI 的判断具有透明度和可追溯性。
*   **IDE 原生集成**：专为 Cursor 等代码编辑器设计的 Agent Skill，实现写作与合规检查的无缝衔接。
*   **本地化知识沉淀**：支持本地规则库构建，随着用户反馈不断迭代，提升特定领域的检测精度。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 113 | 🍴 7 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### Awesome_ai_learning
- 1. **中文简介**
该项目是一个精选的人工智能学习资源集合（Awesome List），旨在为学习者提供系统化的入门指南。它整理了高质量的学习材料、教程和工具，帮助开发者快速掌握AI领域的核心知识。

2. **核心功能**
*   提供结构化的AI学习路径和资源索引。
*   汇集机器学习、深度学习及NLP等领域的优质教程。
*   收录实用的开源工具和代码示例供参考。
*   持续更新以反映人工智能领域的最新进展。

3. **适用场景**
*   AI初学者构建系统的知识体系框架。
*   希望快速查找特定AI技术学习资料的开发者。
*   教育机构或团队内部进行AI技术培训的资源库。
*   需要跟踪AI领域最新开源项目和工具的爱好者。

4. **技术亮点**
*   采用经典的“Awesome List”策展模式，内容经过人工筛选和分类。
*   涵盖范围广，从基础理论到前沿应用均有涉及。
- 链接: https://github.com/h9-tec/Awesome_ai_learning
- ⭐ 86 | 🍴 8 | 语言: 未知

### ai-api-relay-guide
- 描述: AI 中转站推荐与 PokeAPI 评测：GPT 0.03×、Claude 0.2×
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 75 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### SuperMap
- 描述: SuperMap is a living spatial memory for embodied AI — it perceives the world, remembers its evolution, and supports reasoning and action.
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 57 | 🍴 1 | 语言: 未知

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 42 | 🍴 2 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

### OpenMicro
- 描述: Codex Micro functionality using any Gaming Controller on any Coding Harness!
- 链接: https://github.com/stephenleo/OpenMicro
- ⭐ 39 | 🍴 2 | 语言: TypeScript
- 标签: agenticai, ai, claude, claude-code, codex

### LLMVault
- 描述: An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- 链接: https://github.com/CyberSunil/LLMVault
- ⭐ 38 | 🍴 9 | 语言: Python
- 标签: agent-security, ai-security, ai-security-tool, ctf, cybersecurity

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
该项目是一个涵盖自然语言处理（NLP）各领域资源的综合指南库，集成了中英文敏感词检测、语言识别、实体抽取及多语言词向量等实用工具。它不仅提供了丰富的行业词库（如汽车、医疗、金融）和语料数据集，还汇总了BERT、GPT等前沿预训练模型的应用案例与学术资源。作为一个全面的技术资源聚合平台，它旨在为开发者提供从基础文本处理到高级知识图谱构建的一站式解决方案。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表及文本纠错等功能，支持高效的文本预处理。
*   **实体识别与信息抽取**：集成手机号、身份证、邮箱、人名等特定格式数据的抽取工具，以及基于BERT等模型的命名实体识别（NER）和关系抽取能力。
*   **丰富领域词库与数据资源**：收录汽车行业、医疗、金融、法律、成语、古诗词等多个垂直领域的专用词库，以及大规模中文对话、谣言检测和问答数据集。
*   **前沿模型与算法整合**：汇集BERT、ALBERT、GPT2、ERNIE等主流预训练语言模型的资源、代码实现及应用实例，涵盖文本分类、摘要生成及情感分析。
*   **语音与知识图谱工具**：包含中文语音识别（ASR）语料与工具、多语言发音标注，以及基于百科数据构建的知识图谱、实体链接和问答系统相关资源。

**3. 适用场景**
*   **NLP初学者入门与学习**：适合希望系统了解中文自然语言处理技术栈、获取高质量数据集和经典算法代码的学习者。
*   **企业级文本内容风控**：适用于需要部署敏感词过滤、谣言检测或内容合规性审查的互联网平台及媒体机构。
*   **垂直领域智能客服/问答系统开发**：为构建医疗、金融或法律等特定行业的智能问答机器人提供专用的词库、语料及预训练模型支持。
*   **信息抽取与知识图谱构建**：帮助开发人员快速实现从非结构化文本中提取关键实体（如人名、地名、组织名）并构建领域知识图谱。

**4. 技术亮点**
*   **资源极度丰富且更新及时**：涵盖了从传统NLP工具（如Jieba加速版）到最新深度学习框架（如Transformers, SpaCy）的全生态链资源。
*   **多模态与跨语言能力**：不仅关注纯文本处理，还整合了语音识别（ASR）、手写汉字识别及多语言（中英日韩等）相关的语料和模型，支持跨语言知识图谱构建。
*   **注重工程落地与实战**：提供了大量可直接复现的代码示例、竞赛获奖方案复盘以及具体的API调用指南（如新华字典API），极大降低了开发门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关代码项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等热门领域。它通过提供完整的代码示例，帮助开发者快速入门并实践各类人工智能算法。作为一份全面的“Awesome”列表，它是学习AI技术栈的理想参考资料。

2. **核心功能**
*   提供500多个包含完整代码的AI实战项目案例。
*   覆盖机器学习、深度学习、计算机视觉及NLP四大核心领域。
*   按主题分类整理，便于用户针对性查找和学习特定技术。
*   包含大量Python实现的开源项目，适合直接运行和实验。

3. **适用场景**
*   **初学者入门**：新手通过阅读和运行代码快速理解AI基本概念。
*   **项目灵感获取**：开发者寻找具体的应用场景或算法实现参考。
*   **技能提升与复习**：专业人士通过对比不同实现方式优化现有代码。
*   **教学材料准备**：教师或培训师使用这些案例作为课程作业或演示素材。

4. **技术亮点**
*   **体量庞大且全面**：收录近500个项目，几乎覆盖了当前主流AI子领域的所有关键技术。
*   **代码即文档**：不仅提供理论，更强调可运行的代码，极大降低了从理论到实践的门槛。
*   **精选优质资源**：作为“Awwsome”列表，通常经过社区筛选，保证了项目的高质量和代表性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款强大的模型可视化工具，支持查看神经网络、深度学习及机器学习模型的内部结构。它兼容多种主流框架和文件格式，允许用户以图形化方式直观地理解模型架构与数据流向。

### 2. 核心功能
*   **多格式广泛支持**：原生支持 CoreML、Keras、ONNX、PyTorch、TensorFlow、TensorFlow Lite 及 Safetensors 等主流模型格式。
*   **直观的架构可视化**：以清晰的节点图和连线图展示模型层级、层类型及张量形状，便于快速理解网络拓扑。
*   **跨平台桌面应用**：基于 JavaScript 开发，提供独立的桌面客户端，确保在不同操作系统上的一致性和便捷性。
*   **交互式细节探索**：允许用户点击特定节点查看详细的参数信息、权重分布及操作算子详情。

### 3. 适用场景
*   **模型调试与验证**：在部署前检查模型结构是否正确转换，排查层连接错误或维度不匹配问题。
*   **学术交流与演示**：为论文、博客或技术分享生成清晰美观的神经网络结构图，辅助解释复杂算法。
*   **跨框架迁移分析**：在将模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 后，验证转换后的模型结构是否保持一致。

### 4. 技术亮点
*   **轻量级且开源**：作为高星标（33k+）的开源项目，其代码结构清晰，社区活跃，无需重型依赖即可运行。
*   **统一视图接口**：通过统一的可视化引擎抽象不同框架的差异，让用户无需学习每种框架特有的查看工具。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与协同工作，打破生态壁垒。通过统一表示形式，开发者可以更方便地在各种硬件和软件平台间部署模型。

**2. 核心功能**
*   **跨框架兼容**：支持在PyTorch、TensorFlow、Keras等主流框架间无缝转换模型。
*   **标准化表示**：定义了一套通用的算子和张量数据结构，确保模型结构的一致性。
*   **推理加速优化**：配合ONNX Runtime等引擎，实现高效的模型推理和性能调优。
*   **生态系统集成**：广泛兼容scikit-learn及各类AI工具链，简化部署流程。

**3. 适用场景**
*   **混合框架开发**：在使用不同框架训练和测试模型时，需要统一模型格式以便后续处理。
*   **生产环境部署**：将训练好的模型转换为通用格式，以便在边缘设备或特定硬件加速器上高效运行。
*   **模型迁移与复用**：在不同团队或项目间共享预训练模型，避免因框架差异导致的重新训练成本。

**4. 技术亮点**
*   **开放标准主导**：由微软、Facebook等巨头联合推动，已成为事实上的行业通用标准。
*   **高性能运行时**：配套的ONNX Runtime提供高度优化的执行引擎，显著提升推理速度。
*   **广泛的硬件支持**：底层后端支持CPU、GPU、NPU等多种计算设备，适配性强。
- 链接: https://github.com/onnx/onnx
- ⭐ 21160 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
   《机器学习工程开放手册》是一本全面介绍大规模机器学习系统构建与运维的开源指南。内容涵盖从硬件基础设施到模型训练、推理及调试的全链路最佳实践。旨在帮助工程师解决生产环境中遇到的可扩展性与稳定性挑战。

2. **核心功能**
   - 提供大规模分布式训练和推理的工程化解决方案与代码示例。
   - 深入解析GPU集群管理、存储优化及网络通信等底层基础设施细节。
   - 包含针对大语言模型（LLM）的微调、调试及性能瓶颈排查技巧。
   - 集成Slurm等作业调度器的高级用法及PyTorch/Transformers库的最佳实践。

3. **适用场景**
   - 构建和维护支持成千上万张GPU的大规模机器学习训练集群。
   - 优化高并发场景下的大语言模型服务部署与推理延迟。
   - 排查复杂分布式系统中的网络阻塞、显存溢出或数据加载瓶颈。

4. **技术亮点**
   该项目填补了传统MLOps教程在超大规模系统工程实践上的空白，提供了极具参考价值的“实战百科”级内容，特别侧重于解决工业界中真实的扩展性与稳定性难题。
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
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关代码项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等热门领域。它通过提供完整的代码示例，帮助开发者快速入门并实践各类人工智能算法。作为一份全面的“Awesome”列表，它是学习AI技术栈的理想参考资料。

2. **核心功能**
*   提供500多个包含完整代码的AI实战项目案例。
*   覆盖机器学习、深度学习、计算机视觉及NLP四大核心领域。
*   按主题分类整理，便于用户针对性查找和学习特定技术。
*   包含大量Python实现的开源项目，适合直接运行和实验。

3. **适用场景**
*   **初学者入门**：新手通过阅读和运行代码快速理解AI基本概念。
*   **项目灵感获取**：开发者寻找具体的应用场景或算法实现参考。
*   **技能提升与复习**：专业人士通过对比不同实现方式优化现有代码。
*   **教学材料准备**：教师或培训师使用这些案例作为课程作业或演示素材。

4. **技术亮点**
*   **体量庞大且全面**：收录近500个项目，几乎覆盖了当前主流AI子领域的所有关键技术。
*   **代码即文档**：不仅提供理论，更强调可运行的代码，极大降低了从理论到实践的门槛。
*   **精选优质资源**：作为“Awwsome”列表，通常经过社区筛选，保证了项目的高质量和代表性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款强大的模型可视化工具，支持查看神经网络、深度学习及机器学习模型的内部结构。它兼容多种主流框架和文件格式，允许用户以图形化方式直观地理解模型架构与数据流向。

### 2. 核心功能
*   **多格式广泛支持**：原生支持 CoreML、Keras、ONNX、PyTorch、TensorFlow、TensorFlow Lite 及 Safetensors 等主流模型格式。
*   **直观的架构可视化**：以清晰的节点图和连线图展示模型层级、层类型及张量形状，便于快速理解网络拓扑。
*   **跨平台桌面应用**：基于 JavaScript 开发，提供独立的桌面客户端，确保在不同操作系统上的一致性和便捷性。
*   **交互式细节探索**：允许用户点击特定节点查看详细的参数信息、权重分布及操作算子详情。

### 3. 适用场景
*   **模型调试与验证**：在部署前检查模型结构是否正确转换，排查层连接错误或维度不匹配问题。
*   **学术交流与演示**：为论文、博客或技术分享生成清晰美观的神经网络结构图，辅助解释复杂算法。
*   **跨框架迁移分析**：在将模型从 PyTorch 转换为 ONNX 或 TensorFlow Lite 后，验证转换后的模型结构是否保持一致。

### 4. 技术亮点
*   **轻量级且开源**：作为高星标（33k+）的开源项目，其代码结构清晰，社区活跃，无需重型依赖即可运行。
*   **统一视图接口**：通过统一的可视化引擎抽象不同框架的差异，让用户无需学习每种框架特有的查看工具。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了 Essential Cheat Sheets（必备速查表）。它旨在帮助研究者快速回顾和掌握关键概念及工具的使用细节。

2. **核心功能**
- 提供涵盖深度学习框架（如 Keras）的核心语法速查。
- 集成数据处理与分析库（如 NumPy、SciPy）的关键操作指南。
- 包含数据可视化库（如 Matplotlib）的绘图技巧与代码示例。
- 汇总人工智能领域的基础理论与常用算法参考。

3. **适用场景**
- 机器学习研究者在开发过程中快速查阅 API 用法。
- 学生或初学者复习深度学习基础概念与数学工具。
- 工程师在进行数据预处理或模型可视化时查找标准代码片段。
- 团队内部作为技术文档共享，统一代码风格与最佳实践。

4. **技术亮点**
- 内容精炼且高度聚焦于实际科研与工程中的高频痛点。
- 覆盖从底层数据处理到上层模型构建的全栈常用库。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整合了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户轻松入门并掌握就业技能。内容涵盖Python、数学基础、机器学习、深度学习、计算机视觉及自然语言处理等热门领域，支持TensorFlow、PyTorch等多种主流框架。

### 2. 核心功能
- 提供系统化的AI学习路径，从基础数学到高级算法层层递进。
- 收录近200个精选实战案例，强调动手实践与代码落地能力。
- 免费开放配套教材与资源，降低学习门槛，适合初学者自学。
- 覆盖主流技术栈，包括Python生态库（Pandas/Numpy）及深度框架（PyTorch/TensorFlow/Keras）。

### 3. 适用场景
- **零基础转行人员**：希望通过系统化路线快速进入人工智能行业的学习者。
- **在校学生**：需要补充机器学习实战经验以增强求职竞争力的计算机相关专业学生。
- **职场进阶者**：希望梳理知识体系、查漏补缺并提升数据处理与建模能力的从业者。

### 4. 技术亮点
- **资源高度集成**：将分散的知识点、案例和教材整合为一条完整的学习链路。
- **前沿技术全覆盖**：紧跟AI发展潮流，包含CV、NLP、数据科学等多维度热门方向。
- **开源社区驱动**：凭借高星标（13k+）积累大量社区反馈，持续更新实战内容。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大语言模型（LLM）、神经网络及其他人工智能模型。它通过简化模型训练和微调流程，降低了机器学习技术的入门门槛，使开发者能够专注于数据而非复杂的底层代码实现。

### 2. 核心功能
*   **低代码/无代码建模**：通过声明式配置或简单的 API 调用即可定义和训练模型，无需编写大量样板代码。
*   **支持多种模型架构**：原生支持深度学习模型以及大型语言模型（LLM），包括对 Llama、Mistral 等主流模型的微调支持。
*   **端到端工作流**：提供从数据处理、特征工程到模型训练、评估和部署的完整生命周期管理。
*   **多领域兼容性**：广泛适用于计算机视觉、自然语言处理（NLP）及结构化数据任务。

### 3. 适用场景
*   **快速原型开发**：研究人员或数据科学家希望快速验证算法想法，而不想花费时间搭建复杂的训练基础设施。
*   **企业级 AI 应用落地**：非深度机器学习专家的业务团队需要标准化地构建和维护预测模型或分类系统。
*   **LLM 微调与定制**：需要对开源大语言模型（如 Llama 2、Mistral）进行特定领域数据的指令微调（Fine-tuning）。
*   **数据驱动型决策**：利用 Ludwig 的数据中心（Data-centric）特性，优化数据质量以提升传统机器学习模型的性能。

### 4. 技术亮点
*   **基于 PyTorch 构建**：底层依托高性能的 PyTorch 深度学习框架，确保训练效率与灵活性。
*   **声明式配置**：采用 YAML 或 JSON 格式定义模型结构，使得模型复现和版本控制更加便捷且透明。
*   **广泛的预训练集成**：内置对 Hugging Face 生态系统的深度集成，方便调用和微调最新的 Transformer 模型。
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
funNLP 是一个功能全面且实用的中文自然语言处理（NLP）工具库，提供了从基础文本清洗到高级语义理解的多种处理能力。它涵盖了敏感词检测、实体抽取（如手机号、身份证）、情感分析及知识图谱构建等丰富资源，旨在降低 NLP 开发门槛并提升效率。

**2. 核心功能**
*   **文本预处理与清洗**：提供中英文敏感词过滤、繁简转换、停用词去除、文本纠错及拼音标注等功能。
*   **信息抽取与识别**：支持命名实体识别（NER），可抽取手机号、身份证、邮箱、地名、人名等，并具备新词发现能力。
*   **语义分析与情感计算**：内置词汇情感值词典，可进行情感分析、句子相似度匹配及文本分类。
*   **知识图谱与数据资源**：整合了丰富的垂直领域词库（如汽车、医疗、法律）及多语言知识图谱构建工具和数据集。

**3. 适用场景**
*   **内容安全审核**：用于网站或APP的用户评论、发帖内容的敏感词检测和违禁信息过滤。
*   **智能客服与对话系统**：利用其意图识别、实体抽取和情感分析功能，构建更精准的自动化客服或聊天机器人。
*   **数据清洗与预处理**：在机器学习项目中，快速清洗非结构化文本数据，提取关键实体以构建特征工程。

**4. 技术亮点**
*   **资源极其丰富**：不仅包含代码工具，还汇集了海量的中文语料库、专业领域词典（如医学、法律、汽车）及预训练模型资源。
*   **生态整合性强**：集成了多种主流 NLP 技术（如 BERT、SpaCy、Jieba），并提供从传统规则匹配到深度学习模型的多层次解决方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81847 | 🍴 15248 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目在 ACL 2024 上发表，旨在简化从指令微调到强化学习对齐的全流程开发体验。它通过整合多种先进算法，让用户能够以最低的成本和代码量完成模型定制。

### 2. 核心功能
*   **多模型广泛支持**：原生支持 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种 LLM 和 VLM 模型的快速部署与微调。
*   **多样化的微调算法**：内置 LoRA、QLoRA、P-Tuning 等高效参数微调方法，以及全参数微调选项，适配不同算力资源。
*   **端到端训练流水线**：覆盖从 SFT（有监督微调）、RLHF（人类反馈强化学习）到 DPO 偏好优化的完整训练流程。
*   **量化与推理优化**：支持 4-bit/8-bit 量化技术，显著降低显存占用，使消费级显卡也能运行大型模型。
*   **智能体（Agent）集成**：提供构建多轮对话和工具调用型智能体的专用模块，增强模型的交互能力。

### 3. 适用场景
*   **企业级私有化部署**：利用 QLoRA 等技术，在有限 GPU 显存下对开源大模型进行领域知识注入和指令微调。
*   **AI 应用开发者**：快速搭建基于特定垂直领域（如医疗、法律、客服）的智能对话系统或 Agent。
*   **学术研究实验**：复现或改进最新的微调算法（如 RLHF 变体），进行大规模模型行为对齐的对比实验。
*   **资源受限环境优化**：通过量化技术和高效微调策略，在低成本硬件上实现高性能的大模型推理与服务。

### 4. 技术亮点
*   **统一架构设计**：抽象了不同模型底层的差异，提供一致的用户接口，无需为每种模型编写特定的适配代码。
*   **极致性能优化**：针对内存管理和数据加载进行了深度优化，大幅缩短训练时间并降低显存峰值需求。
*   **前沿算法同步**：紧跟学术前沿，迅速集成最新的多模态处理和偏好对齐技术（如 DPO/ORPO）。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73328 | 🍴 8951 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目收集并公开了来自Anthropic、OpenAI、Google及xAI等主流厂商的大模型系统提示词（System Prompts），涵盖Claude、GPT、Gemini等多个版本。内容定期更新，旨在为研究者和开发者提供对前沿大模型底层逻辑的洞察。

2. **核心功能**
- 提取并整理各大主流AI厂商的最新系统提示词模板。
- 覆盖多个知名模型系列（如Claude、GPT、Gemini等）及其特定应用场景版本。
- 保持内容的时效性，定期更新以反映模型迭代的最新变化。
- 提供开源的提示词参考库，支持AI代理与聊天机器人的开发研究。

3. **适用场景**
- **提示词工程学习**：研究者通过分析官方提示词结构，优化自身应用的Prompt设计。
- **大模型行为分析**：安全研究人员或开发者用于理解不同模型的系统约束与指令遵循机制。
- **AI应用开发参考**：在构建Chatbot或Agent时，借鉴主流模型的指令风格以提升交互效果。

4. **技术亮点**
- **多源聚合**：整合了Anthropic、OpenAI、Google、xAI等多家头部科技公司的关键数据。
- **实时维护**：通过定期更新机制，确保所收集的提示词与当前主流模型版本同步。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58337 | 🍴 9546 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的通识性人工智能入门课程，旨在让所有人轻松掌握AI知识。项目采用Jupyter Notebook作为主要开发环境，内容涵盖从基础概念到深度学习应用的广泛主题。

2. **核心功能**
*   **系统化课程体系**：提供结构化的12周学习路径，确保循序渐进的知识吸收。
*   **交互式实践环境**：基于Jupyter Notebook实现代码与理论的即时结合与验证。
*   **全面的技术覆盖**：内容囊括机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
*   **开源免费资源**：由Microsoft For Beginners发起，提供免费且高质量的学习材料。
*   **多模态算法教学**：深入讲解CNN、RNN、GAN等主流神经网络架构的原理与应用。

3. **适用场景**
*   **初学者入门学习**：适合零基础的AI爱好者快速建立知识框架。
*   **高校课程设计**：可作为计算机科学或数据科学专业的辅助教材或实践项目。
*   **企业员工培训**：用于非技术背景员工的人工智能素养普及与技能培训。
*   **自学复习参考**：适合已有基础者通过案例回顾和巩固特定算法知识。

4. **技术亮点**
*   **微软官方背书**：依托Microsoft For Beginners品牌，保证内容的权威性与准确性。
*   **理论与实践并重**：通过笔记本格式无缝衔接理论讲解与代码实操。
*   **前沿技术涵盖**：不仅包含传统机器学习，还深入探讨GAN和RNN等复杂模型。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52379 | 🍴 10601 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个综合性的AI学习资源库，涵盖了从数据分析、机器学习实战到深度学习框架（如PyTorch、TensorFlow 2）及自然语言处理（NLTK）的全方位内容。它不仅包含线性代数等数学基础，还深入探讨了多种经典算法与前沿技术的实际应用。

2. **核心功能**
*   提供基于Python的机器学习和深度学习算法的完整代码实现。
*   集成Scikit-learn、PyTorch和TensorFlow 2等主流工具库进行实战演示。
*   涵盖NLP领域的文本处理与自然语言理解技术。
*   包含推荐系统、聚类、分类及回归等多种算法模型。
*   补充线性代数等必要的数学理论基础以支撑算法理解。

3. **适用场景**
*   AI初学者系统性地学习机器学习和深度学习理论及代码实现。
*   数据科学家快速查阅和复现经典算法（如SVM、KMeans、LR等）的代码示例。
*   研究人员或工程师在构建推荐系统或NLP应用时参考具体技术细节。
*   需要结合数学原理（如线性代数）深入理解算法底层逻辑的学习者。

4. **技术亮点**
*   内容体系全面，将数学基础、传统机器学习与现代深度学习（DL）紧密结合。
*   覆盖广泛的技术栈，包括Scikit-learn、PyTorch、TF2及NLTK等多种流行库。
*   标签丰富且精准，便于用户按特定算法（如RNN、LSTM、Adaboost）快速定位资源。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38542 | 🍴 6465 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
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
- ### GitHub 项目分析报告：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

**1. 中文简介**
该项目是一个包含 500 个 AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。它涵盖了从基础概念到高级应用的广泛领域，为开发者提供了丰富的实战案例。作为一个资源库，它旨在帮助学习者通过实际代码快速掌握人工智能核心技术。

**2. 核心功能**
*   提供涵盖机器学习、深度学习和 NLP 等领域的 500 多个完整项目代码。
*   支持计算机视觉和自然语言处理等主流 AI 子领域的算法实现。
*   作为“Awesome”列表，精选高质量项目，便于用户筛选和学习。
*   包含 Python 语言编写的可执行代码，方便直接运行和调试。
*   项目分类清晰，覆盖数据科学和人工智能的基础与进阶应用。

**3. 适用场景**
*   **AI 初学者入门**：通过阅读和运行具体代码，快速理解机器学习基本概念。
*   **算法学习与复现**：参考现成代码复现经典 CV 或 NLP 模型，加速学习过程。
*   **项目灵感获取**：在需要开发 AI 相关功能时，寻找可借鉴的项目结构和思路。
*   **教学与培训素材**：教师或培训机构利用其丰富案例进行实战教学演示。

**4. 技术亮点**
*   **规模宏大且全面**：收录 500+ 个项目，覆盖 AI 主要分支，是大型资源库。
*   **实战导向**：强调“with code”，提供可直接运行的代码示例，而非仅理论介绍。
*   **社区精选（Awesome）**：经过社区筛选，保证项目质量和实用性较高。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35472 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行各种基于浏览器的复杂工作流。它利用大语言模型和计算机视觉技术，让用户无需编写代码即可操控网页界面。该项目旨在替代传统的 RPA 工具，提供更智能、更灵活的浏览器操作体验。

2. **核心功能**
- 基于 AI 理解网页结构并自主完成点击、输入等操作。
- 支持通过自然语言指令定义和执行复杂的浏览器工作流。
- 具备视觉感知能力，可处理动态加载或图像化的网页元素。
- 兼容主流浏览器自动化工具（如 Playwright），提供 API 接口。
- 能够模拟人类用户行为，绕过部分反自动化检测机制。

3. **适用场景**
- 自动化填写在线表单、注册账户或提交数据等重复性任务。
- 从网页抓取非结构化数据或进行跨平台的信息比对。
- 替代传统 RPA 进行电商价格监控、库存检查等业务流程。
- 测试 Web 应用程序的用户交互流程和回归测试。

4. **技术亮点**
- 结合 LLM 与视觉模型，实现无需固定选择器（Selector-free）的智能 DOM 解析。
- 采用类似人类的操作逻辑，显著提高了在动态网页上的操作成功率。
- 提供 Python SDK 和 API，便于集成到现有的自动化流程中。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22432 | 🍴 2097 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，支持图像、视频及 3D 数据的标注。它提供开源、云版和企业版产品及服务，具备 AI 辅助标注、质量保障、团队协作和开发者 API 等核心特性。

2. **核心功能**
*   支持图像、视频和 3D 模型的全方位数据标注与 AI 辅助标签生成。
*   提供开源、云端部署及企业级产品，满足不同规模团队的需求。
*   内置质量保障机制与团队协作工具，确保标注数据的高标准一致性。
*   开放开发者 API，便于集成到现有的机器学习工作流中。

3. **适用场景**
*   为计算机视觉模型训练构建大规模、高精度的标注数据集。
*   需要多人协同进行视频或复杂 3D 场景标注的企业级研发项目。
*   希望利用 AI 辅助功能加速图像分类、目标检测或语义分割标注流程的场景。

4. **技术亮点**
*   深度集成 PyTorch 和 TensorFlow 生态，支持多种主流深度学习框架的对接。
*   涵盖从边界框、图像分类到语义分割及 ImageNet 标准的多维度标注能力。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16310 | 🍴 3763 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN、Vision Transformer等多种模型结构。它广泛应用于图像分类、目标检测、分割及图像相似度分析等任务，旨在提升深度学习模型的透明度与可理解性。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种可视化算法以生成类激活图。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
*   覆盖图像分类、目标检测、语义分割及图像相似度匹配等多类任务。
*   提供直观的可视化效果，帮助理解模型决策依据。

3. **适用场景**
*   调试和优化深度学习模型，通过可视化定位模型关注区域。
*   在医疗影像或自动驾驶等高风险领域，满足合规性对模型透明度的要求。
*   学术研究，用于分析不同网络架构在特定任务中的注意力机制。
*   向非技术人员展示AI系统的决策逻辑，增强用户信任。

4. **技术亮点**
*   高度模块化设计，轻松集成到现有的PyTorch项目中。
*   广泛支持主流视觉模型架构，包括最新的Vision Transformer变体。
*   作为XAI（可解释人工智能）领域的热门开源工具，拥有极高的社区认可度。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12914 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专注于空间人工智能的几何计算机视觉库。它基于 PyTorch 构建，旨在为深度学习模型提供可微分的图像处理与计算机视觉功能。该项目填补了传统计算机视觉与现代深度学习框架之间的空白。

2. **核心功能**
*   提供完全可微分的几何计算机视觉算子，支持自动求导。
*   内置丰富的图像预处理、增强及几何变换工具。
*   兼容 PyTorch 张量操作，便于集成到现有的深度学习流水线中。
*   包含针对机器人和空间 AI 应用的专用视觉模块。
*   支持从传统 CV 算法到神经网络的高效转换与混合使用。

3. **适用场景**
*   需要集成几何约束的深度学习模型开发（如单目深度估计）。
*   机器人视觉系统中的实时图像感知与姿态估计。
*   构建端到端的可微分计算机视觉管道以进行优化学习。
*   对图像进行批量且高效的几何校正与增强处理。

4. **技术亮点**
*   **全可微设计**：所有视觉操作均基于 GPU 加速且支持反向传播，无缝对接 PyTorch。
*   **领域专精**：特别针对 Spatial AI 和机器人领域优化，提供高精度的几何计算能力。
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
- ### 1. 中文简介
OpenClaw 是一款个人 AI 助手，支持任何操作系统和平台，强调数据自主权与跨平台兼容性。它以独特的“龙虾”理念为用户提供灵活、私密的智能服务体验。

### 2. 核心功能
- 跨平台兼容：支持任意操作系统和设备运行。
- 个人助理：提供个性化的 AI 辅助服务。
- 数据自主：强调用户对自己数据的完全控制权。
- 轻量级设计：基于 TypeScript 构建，易于集成和扩展。

### 3. 适用场景
- 需要本地化部署的个人 AI 助手，注重隐私保护。
- 多设备环境下的统一智能交互需求。
- 开发者希望快速搭建自定义 AI 助理原型。
- 对数据主权有严格要求的企业或个人用户。

### 4. 技术亮点
- 采用 TypeScript 开发，确保类型安全和良好的可维护性。
- 模块化架构便于功能扩展和定制。
- 开源自由，社区活跃，持续迭代优化。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383158 | 🍴 80480 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架及软件开发方法论。它通过构建可复用的“技能”和子智能体驱动的开发流程，提升软件工程的效率与质量。该项目旨在为开发者提供一套结构化的 AI 辅助编码最佳实践。

### 2. **核心功能**
*   **智能体技能框架**：提供模块化的技能定义，使 AI 智能体能够执行特定任务。
*   **子智能体驱动开发**：利用子智能体处理细分任务，实现复杂开发流程的自动化分解。
*   **标准化开发方法论**：将 AI 集成融入标准的软件开发生命周期（SDLC），确保流程规范。
*   **头脑风暴与规划辅助**：内置支持创意生成和需求梳理的工具链，优化前期设计阶段。

### 3. **适用场景**
*   **大型软件项目协作**：需要结构化分工和明确职责的大型团队开发环境。
*   **AI 辅助编程工作流优化**：希望系统化地整合 LLM 能力而非零散使用的开发者。
*   **自动化代码审查与维护**：利用子智能体进行持续的代码质量监控和技术债务管理。

### 4. **技术亮点**
*   **Shell 脚本实现**：主要逻辑通过 Shell 脚本构建，轻量级且易于在 Linux/macOS 环境中部署。
*   **开源高热度**：拥有超过 25 万星标，证明了其在社区中的广泛认可度和实用性。
*   **方法论与工具结合**：不仅提供代码工具，更输出一套完整的 AI 原生开发思维模式。
- 链接: https://github.com/obra/superpowers
- ⭐ 255928 | 🍴 22791 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes-Agent 是一个旨在随用户共同成长的人工智能代理，能够深度融入开发工作流并提供持续的智能支持。它结合了前沿的大语言模型能力，致力于成为开发者最得力的助手。该项目在开源社区中备受瞩目，拥有极高的关注度。

2. **核心功能**
*   集成多种主流大模型（如 Anthropic Claude、OpenAI GPT 等），提供统一的智能交互接口。
*   具备代码生成、调试及重构能力，能够理解上下文并辅助编写高质量代码。
*   支持自然语言指令执行，允许用户通过对话方式管理任务和处理复杂逻辑。
*   提供可扩展的代理架构，允许开发者根据需求定制特定的工作流和行为模式。

3. **适用场景**
*   **高级软件开发**：作为结对编程伙伴，辅助进行复杂功能的实现和代码审查。
*   **自动化工作流**：通过自然语言指令自动化执行日常重复性任务或数据处理流程。
*   **智能客服与助手**：构建基于大型语言模型的个性化对话机器人，用于内部知识问答或用户支持。

4. **技术亮点**
*   **多模型兼容**：无缝对接 Anthropic、OpenAI 等多个顶级 AI 提供商的 API，灵活选择最优模型。
*   **高活跃度社区**：拥有超过 21 万颗星，表明其技术成熟度高且受到全球开发者的广泛验证与认可。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215958 | 🍴 40346 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个支持自托管或云端部署的公平代码工作流自动化平台，原生集成 AI 能力并提供 400 多种集成方式。它结合了可视化构建与自定义代码开发的优势，旨在通过低代码/无代码界面简化复杂的业务逻辑编排。

### 2. 核心功能
*   **可视化工作流编排**：通过拖拽式界面轻松连接不同的应用和服务，实现业务流程自动化。
*   **原生 AI 集成**：内置 AI 能力，允许在工作流中直接使用大语言模型进行数据处理和决策。
*   **广泛的生态系统**：提供超过 400 种现成的集成节点，覆盖主流 API 和数据源。
*   **混合开发模式**：支持低代码快速搭建与 TypeScript 自定义代码编写相结合，满足灵活需求。
*   **灵活部署选项**：支持自我托管（Self-hosted）以确保数据隐私，同时也提供云服务以方便使用。

### 3. 适用场景
*   **企业级数据同步与 ETL**：自动在不同数据库、CRM 和 ERP 系统之间同步和转换数据。
*   **AI 辅助的内容生成与工作流**：结合 LLM 自动处理文档、生成报告或执行智能客服任务。
*   **跨平台通知与消息聚合**：将来自 Slack、Email、Webhook 等多渠道的通知统一收集并分发。
*   **自定义 API 网关与中间件**：利用代码节点构建复杂的逻辑中间件，处理身份验证、数据过滤等前置任务。

### 4. 技术亮点
*   **基于 TypeScript 开发**：利用强类型优势确保代码质量和可维护性，便于开发者扩展自定义节点。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，更好地与各类 AI 客户端和服务端交互。
*   **公平代码许可证 (Fair-code)**：在保持社区驱动和开放性的同时，规范了商业使用条款，平衡了开源与商业化利益。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196717 | 🍴 59378 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。我们的使命是提供必要的工具，使您能将精力集中在真正重要的事情上。

2. **核心功能**
*   具备自主规划与执行任务的能力，无需人工逐步干预。
*   集成多种大型语言模型（如 GPT、Claude、Llama），支持灵活切换。
*   提供丰富的 API 接口，便于开发者将其嵌入现有工作流或应用中。
*   拥有活跃的社区生态，提供大量预设模板和扩展插件。

3. **适用场景**
*   自动化执行复杂的重复性数字任务（如数据抓取、报告生成）。
*   作为智能代理（Agent）框架，用于构建自定义的 AI 助手应用。
*   快速原型开发，验证基于大语言模型的自动化业务流程。
*   教育与技术演示，展示自主 AI 系统的工作机制与潜力。

4. **技术亮点**
*   采用模块化架构，支持高度可定制化的代理行为链。
*   原生支持多模型后端，兼容 OpenAI、Anthropic 及本地部署模型。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185581 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165863 | 🍴 21453 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164186 | 🍴 30421 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157079 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151996 | 🍴 8678 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151919 | 🍴 9582 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

