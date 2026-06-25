# GitHub AI项目每日发现报告
日期: 2026-06-25

## 新发布的AI项目

### awesome-evals
- ### 1. **中文简介**
这是一个由 BenchFlow 维护的精选资源库，旨在为构建和评估 AI 智能体提供高质量、无冗余的资料。内容涵盖学术论文、博客文章、演讲视频、实用工具及基准测试数据集。

### 2. **核心功能**
*   **资源聚合**：系统性地收集了构建和评估 LLM 智能体的关键论文、博客及演讲资料。
*   **基准测试索引**：整合了主流的 AI 智能体评估基准和基准测试工具。
*   **工具推荐**：提供了用于智能体开发和评估的实用工具列表。
*   **社区维护**：由 BenchFlow 团队持续更新和维护，确保资源的时效性和质量。

### 3. **适用场景**
*   **研究人员探索前沿**：快速查找 LLM 智能体评估领域的最新学术成果和理论框架。
*   **工程师搭建评估管线**：参考现有的工具和基准测试，设计或优化自身的智能体评估流程。
*   **学习者入门指南**：通过 curated 的博客和演讲视频，低成本了解智能体评估的核心概念与实践。

### 4. **技术亮点**
*   **去伪存真**：明确强调“非 BS”（No-BS），过滤低质量内容，聚焦高价值资源。
*   **垂直领域专精**：专门针对 AI Agents（智能体）而非通用 LLM 的应用场景进行筛选。
- 链接: https://github.com/benchflow-ai/awesome-evals
- ⭐ 221 | 🍴 11 | 语言: 未知
- 标签: agent-evaluation, ai-agents, awesome, awesome-list, benchmarks

### ShipGenAI
- 1. **中文简介**
该项目提供50个生产就绪的生成式AI SaaS应用模板，用户可自定义品牌并全权保留收益。它集成了Stripe计费、Google OAuth认证及Vercel部署方案，基于MIT协议开源。

2. **核心功能**
*   提供50个开箱即用的生成式AI SaaS应用代码库。
*   内置Stripe支付网关与Google OAuth身份验证集成。
*   支持一键部署至Vercel平台并允许完全白标定制。
*   采用MIT开源许可证，确保商业化使用的自由度。

3. **适用场景**
*   希望快速验证想法并上线MVP的独立开发者或初创团队。
*   需要快速搭建具备支付和鉴权功能的AI工具类SaaS产品。
*   意图通过白标现有模板来节省开发成本的技术型创业者。

4. **技术亮点**
*   基于Next.js框架，结合TypeScript保证代码健壮性。
*   涵盖文本、图像及视频生成等多种主流AI应用场景。
- 链接: https://github.com/benlamiro/ShipGenAI
- ⭐ 103 | 🍴 0 | 语言: JavaScript
- 标签: ai, boilerplate, generative-ai, gpt, image-generation

### claude-ai-desktop-app
- ### 1. 中文简介
该项目旨在提供一个免费的 Claude Code AI 桌面应用程序，支持 Windows、Linux 和 macOS 平台。它通过代理服务器或本地 LLM 路由器（如 Anthropic API、NVIDIA NIM、OpenRouter 等）实现 Claude 代码助手的本地化部署与使用。

### 2. 核心功能
*   **多平台桌面客户端**：提供适用于 PC 端（Windows/Linux/macOS）的独立桌面应用体验。
*   **灵活的后端路由**：支持连接 Anthropic 官方 API、NVIDIA NIM、OpenRouter、DeepSeek、Ollama 及 LM Studio 等多种模型后端。
*   **免费/代理访问**：通过自建代理服务器或集成本地大语言模型，实现低成本或免费的 Claude 代码辅助功能。
*   **开发者工具集成**：提供 VS Code 扩展、JetBrains 插件以及 CLI 终端接口，无缝融入开发工作流。

### 3. 适用场景
*   **本地化 AI 编程辅助**：开发者希望在本地或私有网络环境中运行代码助手，以保护代码隐私并降低 API 成本。
*   **跨平台统一工作区**：需要在不同操作系统（Windows/Mac/Linux）上使用统一界面的 Claude 风格代码编辑器或助手。
*   **替代方案探索**：用户希望在不直接订阅高昂官方服务的情况下，利用开源代理或本地模型模拟 Claude Code 的功能。

### 4. 技术亮点
*   **全栈 TypeScript 架构**：采用 TypeScript 开发，保证了前端界面与后端逻辑的类型安全及可维护性。
*   **多源模型聚合能力**：内置路由器机制，允许用户灵活切换或聚合来自多个提供商（如 Ollama、LM Studio）的本地及云端模型。
- 链接: https://github.com/samuto69/claude-ai-desktop-app
- ⭐ 101 | 🍴 0 | 语言: TypeScript
- 标签: claude-code, claude-code-action, claude-code-api, claude-code-desktop, claude-code-open

### muteki
- 1. **中文简介**
Muteki 是一个自主运行的多模型 CTF（夺旗赛）解题 AI 智能体集群。它旨在通过协同工作，自动化完成网络安全竞赛中的各类挑战任务。该项目展示了利用多个 AI 模型协作解决复杂安全问题的前沿能力。

2. **核心功能**
- 支持多种大型语言模型集成，以应对不同类型的解题需求。
- 具备自主性，无需人工干预即可启动并执行解题流程。
- 采用智能体集群架构，实现并行处理与协同作战。
- 专注于 CTF 赛事场景，涵盖逆向工程、密码学等常见题型解析。
- 提供模块化的框架结构，便于扩展新的解题工具或模型。

3. **适用场景**
- CTF 竞赛辅助：帮助参赛队伍自动化解决部分题目，提高得分效率。
- 安全研究测试：用于评估不同 AI 模型在网络安全挑战中的表现与局限。
- AI 智能体开发：作为多智能体协作框架的研究案例，探索自动化解题的新范式。
- 教学演示：展示 AI 如何结合专业知识解决具体的信息安全问题。

4. **技术亮点**
- 创新性地引入了“智能体集群”概念，通过多模型协同提升解题成功率。
- 实现了高度的自主化操作，减少了人工配置和实时监控的需求。
- 具备良好的可扩展性，允许用户轻松接入新的 AI 模型或解题插件。
- 链接: https://github.com/FishCodeTech/muteki
- ⭐ 45 | 🍴 4 | 语言: Python

### ai-fishing-game
- 1. **中文简介**
这是一款专为 AI 设计的确定性文字钓鱼小游戏，采用单文件且零依赖的实现方式，结构极简。该项目旨在让 AI 伴侣在逻辑推演中体验钓鱼的乐趣，验证其处理简单游戏状态的能力。

2. **核心功能**
*   提供确定性的文字交互界面，确保每次运行结果可预测。
*   单文件架构实现，无任何外部库依赖，便于直接复制运行。
*   专为 LLM（大语言模型）设计，作为测试或娱乐的轻量级应用。
*   模拟传统钓鱼游戏的回合制逻辑，适合文本输出解析。

3. **适用场景**
*   测试大语言模型对简单规则游戏的状态理解和决策能力。
*   开发者用于快速验证 Python 环境下 AI 代理的基础交互框架。
*   AI 聊天机器人的轻量级内置小游戏，增加用户互动的趣味性。
*   编程教学示例，展示如何用极简代码构建逻辑游戏。

4. **技术亮点**
*   **零依赖极简实现**：仅使用 Python 标准库，无需 pip install，开箱即用。
*   **确定性算法**：排除随机性干扰，便于调试和复现 AI 的行为路径。
- 链接: https://github.com/tutusagi/ai-fishing-game
- ⭐ 26 | 🍴 2 | 语言: Python

### hlwy-ai-checker
- 描述: 检查第三方AI API是否掺假以及渠道一致
- 链接: https://github.com/hanlinwenyuan/hlwy-ai-checker
- ⭐ 24 | 🍴 3 | 语言: HTML

### nexusbox
- 描述: Secure sandbox for AI Agents — execute shell, file, code, and browser commands in isolation via MCP.
- 链接: https://github.com/lxcshine/nexusbox
- ⭐ 18 | 🍴 4 | 语言: Go

### agentic-ai-local-to-kubernetes
- 描述: Companion repository for the talk, Agentic AI: Going from Local to Kubernetes
- 链接: https://github.com/lkerriso/agentic-ai-local-to-kubernetes
- ⭐ 15 | 🍴 3 | 语言: Python

### patchright-browser
- 描述: MCP server for browser automation via Patchright. Multi-profile Chromium, headed/headless, StreamableHTTP protocol. Includes dashboard, skills, and AI agent setup.
- 链接: https://github.com/rickicode/patchright-browser
- ⭐ 11 | 🍴 1 | 语言: Python
- 标签: ai-agent, browser-automation, chromium, headless-browser, hermes

### open-tag
- 描述: The open-source, self-hosted workspace where humans, Claude Code, Codex, and AI agents collaborate in channels, threads, DMs, and shared tasks.
- 链接: https://github.com/fancyboi999/open-tag
- ⭐ 11 | 🍴 0 | 语言: TypeScript
- 标签: agentic-workflows, ai-agents, claude-code, collaboration, local-first

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能极其丰富的自然语言处理资源库，主要涵盖敏感词检测、语言识别、各类实体信息抽取（如手机、身份证、邮箱）以及多领域的专业词库。该项目集成了大量中文 NLP 数据集、预训练模型及工具链，旨在为开发者提供从基础文本处理到高级知识图谱构建的一站式解决方案。

**2. 核心功能**
*   **基础文本处理与抽取**：提供中英文敏感词过滤、语言检测、手机号/身份证/邮箱等正则匹配抽取，以及繁简体转换和中文缩写库。
*   **多维领域词库与数据**：内置中日文人名库、职业/品牌/汽车/医学/法律等专业词库，以及诗词、成语、谣言、聊天语料等大型数据集。
*   **NLP 模型与工具集成**：汇总了 BERT、ERNIE、GPT-2 等多种预训练模型资源，以及 SpaCy、Jieba、HanLP 等主流处理工具的用法和扩展包。
*   **知识图谱与问答系统**：提供 Wikipedia/XLORE 等跨语言知识图谱构建工具、医疗/金融领域知识图谱案例及基于图谱的问答系统源码。
*   **语音与OCR 辅助工具**：包含中文手写汉字识别 (cnocr)、语音情感分析、ASR 语料生成及音素对齐工具等视听觉 NLP 相关资源。

**3. 适用场景**
*   **内容安全与审核系统**：利用其敏感词库、反动词表和暴恐词表，快速搭建网站或APP的内容过滤和风控系统。
*   **企业级知识图谱构建**：参考其提供的三元组抽取、实体链接和百科数据资源，构建垂直行业（如医疗、金融）的知识图谱。
*   **智能客服与聊天机器人开发**：使用其中的对话语料、意图识别模型及多轮对话框架（如 Rasa, ConvLab）快速原型化智能客服。
*   **NLP 算法研究与教学**：作为学习中文自然语言处理的资源索引，快速获取最新的预训练模型、数据集基准和竞赛 Top 方案代码。

**4. 技术亮点**
该项目并非单一的算法库，而是一个经过精心策展的“资源聚合器”，汇集了清华 XLORE、百度 UER/OpenCLaP 等顶级机构的中英文预训练模型及海量垂直领域数据集，极大降低了中文 NLP 项目的启动门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81434 | 🍴 15243 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和代码参考，助力快速掌握相关技术。

2. **核心功能**
- 提供大量涵盖ML、DL、CV及NLP领域的完整代码示例。
- 作为学习资源库，帮助初学者和进阶者理解算法实现。
- 集成多种人工智能子领域的热门项目模板。
- 支持通过Python等语言进行直接运行和调试。

3. **适用场景**
- AI初学者寻找系统性的实战练习项目。
- 研究人员或开发者快速检索特定算法（如CNN、RNN）的实现代码。
- 企业团队进行技术选型或原型开发时的参考素材。
- 准备面试或技术考核时积累项目经验。

4. **技术亮点**
- 规模庞大，收录了500个项目，覆盖面极广。
- 标签分类清晰，便于按技术领域（如CV、NLP）筛选。
- 高人气项目（34k+星标），证明其社区认可度和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34846 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和参数。

2. **核心功能**
- 支持广泛格式：兼容 ONNX、TensorFlow、PyTorch、Keras、CoreML、TFLite、safetensors 等主流模型格式。
- 交互式可视化：提供清晰的计算图视图，允许用户展开或折叠网络层以查看细节。
- 跨平台运行：作为 Electron 应用、VS Code 插件或在线服务运行，无需安装复杂的环境依赖。
- 实时检查：可即时加载本地或远程模型文件，快速诊断结构问题。

3. **适用场景**
- 模型结构审查：在部署前快速验证神经网络的层连接和维度是否正确。
- 教学与演示：向非技术人员或学生展示深度学习模型的内部工作原理。
- 格式转换验证：确认不同框架间模型转换（如 PyTorch 转 ONNX）后的结构一致性。
- 故障排查：通过可视化定位模型推理出错的具体层级或节点。

4. **技术亮点**
- 轻量级且无需后端服务器，完全在客户端解析和渲染模型数据。
- 高度集成性，可直接嵌入 Visual Studio Code 等开发环境中使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33126 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在促进不同深度学习框架之间的互操作性。它允许用户在不同平台之间自由迁移模型，打破了单一框架的生态壁垒。通过统一格式，开发者可以更高效地进行模型的部署和优化。

2. **核心功能**
- 定义通用的神经网络模型表示格式，支持主流深度学习框架如PyTorch、TensorFlow和Keras。
- 提供跨平台的模型转换工具链，实现从训练框架到推理引擎的无缝迁移。
- 包含丰富的算子库，覆盖卷积、池化、激活等常见深度学习层操作。
- 支持模型优化与压缩，便于在资源受限的设备上高效运行。

3. **适用场景**
- 需要将PyTorch或TensorFlow训练的模型部署到不支持原生框架的硬件加速设备上。
- 在多框架混合环境中工作，希望统一管理不同来源的机器学习模型。
- 开发高性能推理引擎，需要兼容多种前端框架导出的模型结构。

4. **技术亮点**
- 作为行业标准被Microsoft、Facebook、AWS等主要科技巨头广泛采用，生态兼容性强。
- 采用静态计算图表示，有利于编译器进行静态分析和整体优化，提升推理效率。
- 链接: https://github.com/onnx/onnx
- ⭐ 21042 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18173 | 🍴 1152 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2109 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11524 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10639 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34846 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和数据流向。

2. **核心功能**
*   支持广泛格式的模型加载，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
*   提供直观的图形化界面，清晰展示网络层级结构与节点连接关系。
*   允许用户深入查看各层的参数详情及张量形状信息。
*   具备模型结构检查能力，可辅助发现潜在的结构错误或冗余。

3. **适用场景**
*   调试复杂神经网络结构，快速定位模型构建中的逻辑错误。
*   向非技术人员或团队成员展示和解释深度学习模型的工作原理。
*   在不同框架间迁移模型时，验证转换后的模型结构是否保持一致。
*   学习不同架构（如 CNN、RNN、Transformer）的具体实现细节。

4. **技术亮点**
*   无需安装庞大的深度学习依赖环境，即可轻量级运行模型可视化。
*   跨平台兼容性好，支持 Windows、macOS、Linux 及 Web 浏览器端访问。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33126 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一套完整的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材，帮助零基础用户轻松入门。内容涵盖Python、机器学习、深度学习及数据处理等热门领域，旨在通过实战指导助力用户实现就业目标。

2. **核心功能**
*   提供结构化的AI学习路径，涵盖从基础编程到高级算法的全流程知识体系。
*   整合大量实战案例与项目资源，支持Python、TensorFlow、PyTorch等多框架实践。
*   包含数学基础、数据分析和可视化等关键技能模块，强化理论联系实际的能力。
*   免费开放配套教材与学习资源，降低人工智能领域的学习门槛。

3. **适用场景**
*   希望从零开始系统学习人工智能和机器学习的初学者。
*   需要补充实战项目经验以提升简历竞争力、寻求AI相关就业岗位的技术人员。
*   希望梳理数据科学、深度学习及自然语言处理等领域知识体系的学生或研究者。

4. **技术亮点**
*   内容覆盖面极广，集成了主流深度学习框架（如PyTorch, TensorFlow, Keras）及经典工具库（如NumPy, Pandas）。
*   强调“就业实战”，通过丰富的案例库直接对接行业应用需求。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在帮助用户轻松构建定制化的大型语言模型（LLM）、神经网络及其他人工智能模型。它通过声明式配置简化了机器学习流程，使开发者无需编写大量底层代码即可快速训练和部署模型。该项目支持多种深度学习架构，特别适用于数据密集型的人工智能应用开发。

### 2. 核心功能
- **低代码/声明式建模**：通过 YAML 或 JSON 配置文件定义模型结构，无需复杂的 Python 编程即可创建 ML 模型。
- **多模态支持**：原生支持处理文本、图像、表格、音频等多种数据类型，适用于计算机视觉和自然语言处理任务。
- **自动化训练与调优**：内置自动化超参数调整和训练流程，降低模型优化的门槛和技术难度。
- **广泛的模型兼容性**：基于 PyTorch 构建，兼容 Hugging Face Transformers 等主流库，支持微调 LLaMA、Mistral 等大语言模型。
- **端到端工作流**：提供从数据预处理、模型训练到评估和部署的完整闭环工具链。

### 3. 适用场景
- **快速原型开发**：数据科学家希望在不深入底层代码的情况下，迅速验证新的机器学习想法或模型架构。
- **企业级 AI 部署**：需要标准化、可重复的模型训练流程，以降低团队协作成本并确保生产环境的一致性。
- **多模态应用构建**：开发同时处理文本和图像（如文档理解、视觉问答）的复杂 AI 系统。
- **大语言模型微调**：对开源 LLM（如 Llama、Mistral）进行领域特定数据的微调，而无需管理繁琐的训练脚本。

### 4. 技术亮点
- **数据为中心的设计**：强调数据配置而非代码逻辑，提升了模型开发的灵活性和可维护性。
- **无缝集成 Hugging Face**：直接支持加载和微调流行的 Transformer 模型，简化了 LLM 应用的开发过程。
- **高性能后端**：基于 PyTorch 优化，支持 GPU 加速训练，确保大规模数据处理和模型训练的效率。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11723 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9117 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8908 | 🍴 3101 | 语言: C++
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
- ⭐ 6180 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81434 | 🍴 15243 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型，其研究成果已被 ACL 2024 收录。它旨在简化从指令微调到强化学习对齐的全流程开发体验。

2. **核心功能**
*   支持百余种主流 LLM 和 VLM 的统一接口微调，无需针对每种模型编写独立代码。
*   提供多种高效微调算法支持，包括 LoRA、QLoRA 以及全参数微调，适配不同硬件资源。
*   集成 RLHF（基于人类反馈的强化学习）、DPO 等高级对齐训练方法，优化模型输出质量。
*   内置量化加速功能，支持低比特量化推理与训练，显著降低显存占用并提升速度。
*   涵盖从数据预处理、模型训练到推理部署的完整工作流，并支持 Agent 构建与多模态任务。

3. **适用场景**
*   研究人员或开发者需要对特定领域的 LLM 进行低成本、高效率的指令微调（Instruction Tuning）。
*   希望在有限显存条件下，通过 QLoRA 等技术对大型模型进行个性化定制的企业级用户。
*   需要构建具备视觉理解能力或多模态交互能力的智能应用（VLM 微调）。
*   寻求自动化或标准化流程来实现 RLHF/DPO 对齐，以提升模型安全性与有用性的团队。

4. **技术亮点**
*   **极致的高效性与易用性平衡**：通过统一的 API 设计屏蔽底层框架差异，同时利用 QLoRA 等技术实现资源友好型训练。
*   **前沿技术集成**：紧跟学术进展，原生支持 MoE（混合专家）、DeepSeek、Gemma 等最新架构及 ACL 2024 验证的高效训练范式。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72476 | 🍴 8861 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48439 | 🍴 10047 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 45889 | 🍴 7530 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战、线性代数、PyTorch及TensorFlow 2等技术的综合性学习资源库。它结合了NLTK自然语言处理工具，旨在为学习者提供从理论到实践的完整AI技能提升路径。

2. **核心功能**
*   提供经典的机器学习算法（如SVM、K-Means、逻辑回归）的代码实现与原理讲解。
*   包含深度学习框架（PyTorch、TensorFlow 2）及神经网络模型（RNN、LSTM、DNN）的实战案例。
*   集成自然语言处理（NLP）模块，利用NLTK进行文本分析与推荐系统开发。
*   梳理线性代数等数学基础，辅助理解机器学习背后的核心逻辑。
*   涵盖关联规则挖掘（Apriori、FP-Growth）和降维技术（PCA、SVD）等数据处理技巧。

3. **适用场景**
*   计算机专业学生或初学者构建完整的机器学习知识体系。
*   数据科学家希望快速复习经典算法或寻找特定模型（如协同过滤推荐系统）的代码参考。
*   需要进行NLP项目开发的工程师，参考基于NLTF和深度学习的文本处理方案。
*   准备技术面试的考生，用于梳理高频考点如集成学习（AdaBoost）和聚类算法。

4. **技术亮点**
*   技术栈全面，从传统统计学习到前沿的深度学习和NLP均有覆盖。
*   注重理论与代码结合，不仅提供scikit-learn等库的使用，还涉及底层数学推导。
*   社区热度高（4万+星标），拥有大量经过验证的实战代码示例。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11542 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36290 | 🍴 5950 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34846 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33696 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28169 | 🍴 3421 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25713 | 🍴 2881 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34846 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. **中文简介**
Skyvern 是一款基于人工智能的自动化框架，旨在通过大语言模型（LLM）和计算机视觉技术，智能地驱动浏览器执行复杂的网页工作流。它无需编写传统的 CSS/XPath 选择器，能够理解页面内容并自主完成操作，从而简化 RPA 流程的开发与维护。

### 2. **核心功能**
*   **AI 驱动的浏览器控制**：利用 LLM 和视觉模型实时分析网页界面，自主决策点击、输入等操作，而非依赖硬编码的选择器。
*   **无代码/低代码工作流自动化**：通过自然语言指令定义任务，大幅降低浏览器自动化的开发门槛。
*   **兼容主流自动化引擎**：底层支持 Playwright 等现代浏览器自动化工具，确保操作的稳定性与速度。
*   **端到端流程执行**：能够从登录、数据提取到表单填写，完整覆盖跨页面的复杂业务逻辑。

### 3. **适用场景**
*   **企业级 RPA 替代方案**：用于自动化处理需要频繁登录、跨系统交互且页面结构经常变化的传统办公流程。
*   **大规模网页数据抓取**：适用于动态加载、反爬机制较强或布局不固定的网站数据提取任务。
*   **在线服务自动化注册与填报**：批量处理需要在多个网站上填写相同信息的重复性人工操作。

### 4. **技术亮点**
*   **超越传统 Selenium/Puppeteer**：解决了传统自动化工具因页面元素变更导致脚本易碎的痛点，具备更强的鲁棒性。
*   **结合 Vision 与 LLM**：创新性地融合计算机视觉与大语言模型，使 AI 能像人类一样“看”懂网页并进行操作。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22000 | 🍴 2054 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16139 | 🍴 3720 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目致力于提供先进的计算机视觉可解释性工具，支持CNN、Vision Transformer等多种架构。它广泛应用于分类、目标检测、分割及图像相似度分析等任务，帮助用户理解深度学习模型的决策过程。

2. **核心功能**
*   支持多种主流模型架构，包括CNN和Vision Transformers。
*   覆盖多类计算机视觉任务，如图像分类、目标检测和语义分割。
*   集成多种可视化算法，如Grad-CAM、Score-CAM及类激活映射。
*   提供直观的可视化结果，增强模型决策的透明度和可解释性。

3. **适用场景**
*   研究人员需要验证深度神经网络在特定任务中的注意力焦点是否正确。
*   开发者希望调试模型，通过可视化发现模型误判的特征或偏差。
*   医疗影像分析等领域，要求对AI诊断结果提供直观的证据支持。

4. **技术亮点**
*   高度兼容PyTorch生态，同时兼顾经典CNN与现代Vision Transformer架构。
*   内置多种前沿的可解释性算法（XAI），满足从基础到高级的可视化需求。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12891 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间智能设计的几何计算机视觉库，基于 Python 和 PyTorch 构建。它旨在通过可微分的图像处理模块，简化深度学习与计算机视觉的结合，赋能机器人及人工智能应用。

**2. 核心功能**
*   提供基于 PyTorch 的可微分图像处理算子，支持端到端的梯度反向传播。
*   包含丰富的几何视觉算法，如相机标定、立体匹配和单目深度估计。
*   集成先进的图像增强和数据预处理工具，直接兼容 GPU 加速计算。
*   支持将传统计算机视觉流程无缝嵌入到神经网络架构中。

**3. 适用场景**
*   **机器人视觉**：用于实时处理传感器数据，实现环境感知与导航控制。
*   **深度学习研究**：在需要结合传统几何约束的深度网络中进行模型训练与调试。
*   **图像增强流水线**：在数据加载阶段利用 GPU 加速进行大规模图像预处理。

**4. 技术亮点**
*   **完全可微分**：所有操作均在 PyTorch 张量上运行，支持自动微分，便于与深度学习模型整合。
*   **硬件加速**：原生支持 CUDA，充分利用 GPU 资源提升图像处理效率。
*   **模块化设计**：提供清晰 API，方便开发者替换或扩展特定的视觉算法组件。
- 链接: https://github.com/kornia/kornia
- ⭐ 11249 | 🍴 1190 | 语言: Python
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
- ⭐ 3252 | 🍴 397 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2616 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2411 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 项目分析：OpenClaw

1. **中文简介**
   OpenClaw 是一款跨平台、全操作系统支持的个性化 AI 助手，让你完全掌控自己的数据。它旨在以“龙虾”般的独特方式，为用户提供私密且强大的个人智能服务，支持在任何设备和本地环境中部署。

2. **核心功能**
   * **全平台兼容**：支持任何操作系统和硬件平台，实现无缝接入。
   * **数据自主权**：强调“拥有你的数据”，确保用户隐私和数据安全。
   * **个人化 AI 助理**：专注于为个体用户提供定制化的智能辅助体验。
   * **开源与透明**：作为开源项目，允许用户自定义和审查代码逻辑。

3. **适用场景**
   * **注重隐私的个人用户**：希望在不依赖云端大模型的情况下，在本地运行 AI 助手以保护敏感数据。
   * **开发者与技术爱好者**：需要基于 TypeScript 构建可扩展、可自定义的 AI 代理基础设施。
   * **多设备协同工作流**：需要在不同操作系统（如 Windows、macOS、Linux）间同步和统一 AI 辅助体验的用户。

4. **技术亮点**
   * **TypeScript 驱动**：利用 TypeScript 的类型安全和现代 JS/TS 生态系统优势，便于维护和扩展。
   * **去中心化架构**：设计上摆脱对特定云平台的依赖，支持边缘计算和本地部署。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380358 | 🍴 79670 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 基于您提供的信息，以下是关于 **superpowers** 项目的技术分析：

1. **中文简介**
   Superpowers 是一个具备实际可用性的智能体技能框架与软件开发方法论。它旨在通过结构化的技能和子代理驱动开发流程，提升软件工程的效率与质量。该项目整合了头脑风暴、编码及全生命周期管理等功能。

2. **核心功能**
   *   **智能体技能框架**：提供模块化的“技能”组件，支持构建复杂的AI代理工作流。
   *   **子代理驱动开发**：采用 Subagent-Driven Development (SDD) 模式，通过协调多个子代理完成代码生成与任务拆解。
   *   **SDLC 全流程支持**：覆盖从需求头脑风暴到最终软件交付的完整开发生命周期。
   *   **自动化代码协作**：内置强大的编码辅助能力，能够理解上下文并执行具体的开发任务。

3. **适用场景**
   *   **复杂系统架构设计**：需要多步骤规划和大模型协同工作的软件架构初期阶段。
   *   **自动化代码生成与维护**：利用子代理自动编写、测试或重构特定模块的代码库。
   *   **AI 驱动的研发工作流搭建**：开发者希望构建基于智能体技能的定制化软件开发流水线。

4. **技术亮点**
   *   **方法论创新**：将抽象的“智能体技能”概念落地为具体的软件开发实践，填补了理论框架与实际工程之间的空白。
   *   **高社区认可度**：拥有超过 23.8 万星的高热度，证明其在 AI 辅助开发领域的广泛影响力和实用性。
- 链接: https://github.com/obra/superpowers
- ⭐ 238187 | 🍴 21128 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 202493 | 🍴 36186 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款采用公平代码许可的工作流自动化平台，原生集成 AI 能力。它支持将可视化构建与自定义代码相结合，提供 400 多种集成方式，并允许用户选择自托管或云端部署。

2. **核心功能**
*   提供可视化的工作流构建界面，同时支持嵌入自定义代码以增强灵活性。
*   内置原生 AI 功能，能够轻松将人工智能模型整合到自动化流程中。
*   拥有超过 400 种预置集成连接器，覆盖主流 API 和数据服务。
*   支持灵活部署模式，用户可选择自托管以保障数据隐私或使用云服务。
*   兼容 MCP（模型上下文协议）客户端与服务端，增强与大语言模型的交互能力。

3. **适用场景**
*   企业级自动化：连接 CRM、ERP 和数据库，自动处理数据同步和业务逻辑。
*   AI 应用开发：构建基于大语言模型的智能助手或自动化内容生成工作流。
*   开发者工具链集成：通过自定义代码和 API 触发器，自动化 CI/CD 流程或系统监控。
*   数据管道构建：利用低代码方式快速搭建 ETL 流程，实现多源数据聚合与分析。

4. **技术亮点**
*   基于 TypeScript 开发，具备良好的类型安全和扩展性。
*   开源且公平代码许可，兼顾社区贡献与企业商用需求。
*   原生支持 MCP 协议，紧跟 AI 代理（Agent）技术发展趋势。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 193996 | 🍴 58824 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- **1. 中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并基于此进行构建。我们的使命是提供必要的工具，以便用户能将精力集中在真正重要的事务上。

**2. 核心功能**
*   支持多种大型语言模型后端，包括 OpenAI GPT、Anthropic Claude 及 Llama 等。
*   具备自主代理（Agentic）能力，可独立规划、执行任务并调用外部工具。
*   提供高度可扩展的架构，允许开发者基于其框架定制特定的 AI 应用。
*   自动化处理复杂工作流，减少用户在重复性 AI 交互中的手动干预。

**3. 适用场景**
*   需要长期记忆和自主决策能力的复杂自动化任务。
*   作为基础框架，用于快速开发自定义的垂直领域 AI 代理。
*   探索和研究多步推理、工具使用及自主 AI 行为的边界。

**4. 技术亮点**
*   原生支持多模型集成，摆脱单一供应商锁定，灵活适配不同性能与成本的 LLM。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185159 | 🍴 46125 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164314 | 🍴 21282 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163874 | 🍴 30363 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156606 | 🍴 46147 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150060 | 🍴 9334 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146519 | 🍴 23052 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

