# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### yuwen-publish-precheck
- 1. **中文简介**
这是一款专为抖音、小红书和微信视频号设计的发布前合规审查工具，利用 AI 识别内容违规点并依据官方规则提供即时修改建议。它通过 38 篇真实样本校准判断标准，并沉淀 72 条官方原文作为可查证依据，旨在帮助用户规避常见雷区。该项目强调基于本地规则库持续优化准确率，但不承诺绝对过审或教授绕过审核的技巧。

2. **核心功能**
*   **多平台预检**：支持抖音、小红书及微信视频号的内容合规性自动审查。
*   **违规溯源与解释**：明确指出违规语句及其对应的官方具体规则条款。
*   **一键修改建议**：提供符合平台规范的直接可用修改方案。
*   **本地知识库迭代**：基于历史踩坑数据和本地规则库，使审核精度随使用次数提升。
*   **Cursor/Agent 集成**：作为 Agent Skill 嵌入开发工作流，实现无缝的代码或文本预处理。

3. **适用场景**
*   **自媒体内容创作**：博主在发布视频文案或图文笔记前，快速筛查潜在违规风险。
*   **MCN 机构品控**：团队批量审核创作者提交的内容，确保符合各平台最新合规要求。
*   **开发者集成测试**：在 Cursor 等 IDE 中通过 Agent 技能自动化检查代码注释或文档中的敏感信息。

4. **技术亮点**
*   **可验证的规则引用**：结合 72 条官方原文引文，增强 AI 判定结果的透明度和可信度。
*   **基于真实样本校准**：使用 38 篇真实数据调整判定尺度，比通用模型更贴合实际审核场景。
*   **本地化规则沉淀**：利用本地规则库存储用户踩坑经验，实现个性化且越用越准的审核效果。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 86 | 🍴 4 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### claude-arbitrage-bot
- 1. **中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，内置了Python自动化脚本以简化操作流程。它结合了智能合约开发与自动化交易策略，旨在捕捉跨链或DEX间的价格差异机会。

2. **核心功能**
- 支持在以太坊兼容链上执行自动化的套利交易策略。
- 集成Python脚本实现交易流程的自动化控制与逻辑处理。
- 利用AI辅助工具（如Claude/Codex）优化代码生成与策略迭代。
- 提供智能合约部署与管理功能，确保交易执行的原子性与安全性。
- 实时监控市场价格波动，快速响应并执行低延迟的交易指令。

3. **适用场景**
- 适用于希望利用自动化脚本在DeFi协议间进行高频套利交易的开发者。
- 适合需要结合AI代码助手快速构建和调试以太坊智能合约的研究者。
- 用于测试和优化针对特定以太坊兼容网络（如BSC、Polygon等）的套利策略。
- 适用于学习如何将Python自动化框架与区块链智能合约交互的技术实践场景。

4. **技术亮点**
- 创新性地将AI大模型辅助编程与区块链自动化交易相结合，降低了开发门槛。
- 采用Python与Solidity混合架构，既保留了Python的灵活数据处理能力，又具备Solidity在链上执行的高效性。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### ai-api-relay-guide
- 1. **中文简介**  
该项目是一个基于 GitHub Pages 构建的 AI API 中转服务推荐指南，通过类似 PokeAPI 的游戏化评分机制对主流大模型接口进行对比评测。它重点展示了如 GPT 和 Claude 等服务的成本优势，旨在帮助用户以极低价格（如 0.03 倍至 0.2 倍官方定价）获取高质量的 AI 推理能力。

2. **核心功能**  
*   **API 中转推荐**：汇总并推荐可靠且低成本的 AI 代理中转服务商。
*   **游戏化评测体系**：借鉴 PokeAPI 的设计思路，以趣味化的方式展示不同模型的性能与价格参数。
*   **成本效益分析**：直观呈现各服务商相对于官方定价的折扣力度（如 GPT 0.03×、Claude 0.2×）。
*   **静态页面部署**：利用 GitHub Pages 托管纯静态内容，实现轻量级、免维护的信息展示。

3. **适用场景**  
*   **个人开发者降本**：希望以最低预算测试或集成 GPT/Claude 接口的独立开发者。
*   **初创团队选型**：需要快速评估不同 API 供应商性价比以决定合作对象的创业团队。
*   **资源聚合参考**：寻找稳定且便宜的大模型中转渠道，避免直接调用官方高价接口的用户。

4. **技术亮点**  
*   **CSS 驱动交互**：尽管主要语言标注为 CSS，暗示其可能大量依赖现代 CSS 特性（如 Grid/Flex 布局及伪元素）来实现视觉表现，而非复杂后端逻辑。
*   **创意可视化设计**：将枯燥的 API 参数对比转化为易于理解的“宝可梦式”图鉴或卡片，提升了信息获取的趣味性。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 76 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### codex-skill
- ### 1. **中文简介**
codex-skill 是一个开源项目，旨在为 OpenAI Codex 桌面应用提供主题定制能力、AI 驱动的主题生成器以及跨平台运行时支持。它允许用户创建和管理自定义的 Codex 桌面主题，实现界面的个性化外观。该项目基于 Node.js 和 CSS 构建，兼容 macOS 和 Windows 系统。

### 2. **核心功能**
*   **AI 主题生成**：利用人工智能技术自动生成符合用户偏好的 Codex 桌面主题。
*   **跨平台运行时**：提供统一的运行环境，支持在 macOS 和 Windows 上部署自定义主题。
*   **主题管理与定制**：允许用户创建、安装和管理个性化的 CSS 主题文件。
*   **Chromium DevTools 协议集成**：基于 Chromium 开发者工具协议，实现对 Codex 界面样式的深度控制。
*   **开源社区支持**：作为开源项目，提供可复用的技能（Skill）模块供开发者扩展。

### 3. **适用场景**
*   **开发者个性化需求**：希望改变 OpenAI Codex 默认界面风格，打造符合个人审美的编码环境。
*   **品牌或团队统一视觉**：企业或团队内部统一 Codex 应用的视觉主题，提升品牌形象或协作一致性。
*   **主题开发测试**：前端开发者利用 Chromium DevTools 协议测试新的 CSS 主题渲染效果。
*   **自动化主题切换**：结合 AI 生成器，根据使用场景（如夜间模式、专注模式）自动切换主题。

### 4. **技术亮点**
*   结合了 OpenAI 的 AI 能力与 Chromium 底层协议，实现了智能化的 UI 定制。
*   采用 Node.js 作为后端运行时，确保了良好的跨平台兼容性（macOS/Windows）。
*   通过“Skill”机制模块化封装主题功能，便于集成到现有的 Codex 生态中。
- 链接: https://github.com/CodeDrobe/codex-skill
- ⭐ 71 | 🍴 10 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### SuperMap
- 1. **中文简介**
SuperMap 是为具身智能设计的动态空间记忆系统，能够感知世界并记录其演变过程。它支持高级的空间推理与行动决策，旨在赋予AI持久的环境理解能力。

2. **核心功能**
*   实时感知周围环境状态，构建初始空间认知。
*   持续追踪并记忆空间结构随时间的演化变化。
*   基于记忆数据进行复杂的逻辑推理与情境分析。
*   为具身智能体提供导航、规划及执行具体行动的支撑。

3. **适用场景**
*   服务机器人在动态变化的室内环境中进行长期任务规划。
*   自动驾驶系统在复杂交通场景中结合历史记忆优化决策。
*   仓储物流机器人利用空间记忆提升在大型仓库中的导航效率。

4. **技术亮点**
*   采用“活”式记忆机制，不仅存储静态地图，更记录环境的动态演变。
*   专为具身智能体设计，紧密耦合感知、记忆与行动闭环。
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 51 | 🍴 1 | 语言: 未知

### codex-dream-skin
- 描述: macOS & Windows Codex Desktop 梦幻换肤 Skill｜由世事宜AI免费提供
- 链接: https://github.com/xnydl/codex-dream-skin
- ⭐ 27 | 🍴 0 | 语言: JavaScript
- 标签: codex, codex-desktop, macos, openai, skill

### Codex-Dream-Skin-Forge
- 描述: 基于 Fei-Away/Codex-Dream-Skin 二次开发的 Codex Desktop 主题工具，新增 Windows 多主题包、应用内切换、Bug 修复与 AI 辅助主题制作。
- 链接: https://github.com/tree0519/Codex-Dream-Skin-Forge
- ⭐ 27 | 🍴 3 | 语言: JavaScript

### code-humanizer
- 描述: humanizer, but for code — an agent skill that removes AI-generated code slop: duplicated helpers, try-import fallbacks, broad excepts, speculative abstractions. Test-gated, behavior-preserving.
- 链接: https://github.com/LeonardNJU/code-humanizer
- ⭐ 23 | 🍴 0 | 语言: 未知
- 标签: agent-skills, ai-slop, claude, claude-code, code-quality

### RUDR9
- 描述: One command → full AI engineering team. Transforms Hermes Agent into a 9-role development organization with Kanban coordination, per-profile authority enforcement, and PAUL-inspired workflows.
- 链接: https://github.com/ardhaecosystem/RUDR9
- ⭐ 20 | 🍴 3 | 语言: Shell

### uxon-ai
- 描述: UXON is an MCP server and API that lets AI agents and developers create landing pages, run A/B experiments, and track conversions across domains.
- 链接: https://github.com/alexpilotto/uxon-ai
- ⭐ 18 | 🍴 0 | 语言: 未知
- 标签: ab-testing, ai-agents, conversion-tracking, cro-api, experimentation-api

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理资源库，集成了敏感词检测、语言识别、实体抽取及丰富的专业词库。该项目汇集了从基础工具（如繁简转换、拼音标注）到前沿模型（如 BERT、GPT 应用）的大量开源资源与数据集。它旨在为 NLP 开发者提供一站式的数据增强、知识图谱构建及文本分析解决方案。

2. **核心功能**
- **基础 NLP 工具链**：提供分词、词性标注、命名实体识别（NER）、情感分析及文本摘要等核心算法实现。
- **丰富行业词库与数据**：涵盖医疗、法律、汽车、金融等领域的专用术语库，以及古诗、地名、人名等大规模知识库。
- **预训练模型与深度学习资源**：集成 BERT、GPT-2、ALBERT 等主流模型的微调代码、中文预训练模型及相关的竞赛方案。
- **多模态与语音处理**：包含中文语音识别（ASR）、OCR 文字识别、语音情感分析及音素对齐等工具。
- **数据增强与标注平台**：提供 EDA 数据增强工具、协同文本标注平台（如 Doccano）及各类 NLP 数据集下载。

3. **适用场景**
- **智能客服与聊天机器人开发**：利用其中的闲聊语料、多轮对话系统及意图识别工具快速搭建垂直领域对话机器人。
- **企业级内容风控与安全审查**：通过内置的敏感词库、暴恐词表及谣言检测数据，实现用户生成内容（UGC）的自动化审核。
- **垂直行业知识图谱构建**：借助医疗、法律、金融等专业词库和实体抽取工具，构建高精度的行业知识图谱。
- **NLP 算法研究与教学**：作为研究者或学生，利用其提供的基准数据集、竞赛 TOP 方案及前沿论文代码进行算法复现与对比实验。

4. **技术亮点**
- **资源聚合度高**：不仅包含代码，还整合了大量高质量的开源数据集、预训练模型权重及行业专家分享的技术文档。
- **覆盖全生命周期**：从数据采集、清洗、标注到模型训练、评估及应用部署，提供了完整的 NLP 工作流支持。
- **紧跟前沿技术**：持续更新包含 BERT、GPT 系列及知识图谱表示学习等最新深度学习技术在 NLP 领域的应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81833 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它旨在为开发者提供丰富的实战案例和源代码参考。

2. **核心功能**
*   提供涵盖AI四大核心领域的大量实战项目代码。
*   集成机器学习和深度学习的经典算法实现。
*   包含计算机视觉与自然语言处理的具体应用案例。
*   作为高质量的学习资源库供开发者查阅和实践。

3. **适用场景**
*   AI初学者进行算法原理验证和基础编程练习。
*   研究人员寻找特定领域（如CV或NLP）的代码参考基准。
*   开发者在构建新系统时借鉴成熟的解决方案架构。

4. **技术亮点**
*   项目规模庞大，内容全面，覆盖主流AI子领域。
*   附带完整代码，便于直接运行和深入理解。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35463 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持广泛的主流模型格式，能够直观展示模型架构与权重数据。该工具由 JavaScript 编写，便于跨平台使用。

2. **核心功能**
*   支持多种主流框架（如 PyTorch, TensorFlow, Keras, ONNX 等）的模型文件解析。
*   提供直观的图形化界面，清晰展示网络层结构、数据流向及参数细节。
*   兼容桌面应用、Web 浏览器及 VS Code 插件等多种运行环境。
*   允许用户查看和检查模型内部的具体张量形状与数值信息。

3. **适用场景**
*   **模型调试**：在训练前或推理前快速检查模型结构是否符合预期，排查连接错误。
*   **学术交流与演示**：生成高质量的模型架构图，用于论文撰写、技术博客或会议演示。
*   **异构框架迁移**：在将模型从一种框架（如 PyTorch）转换到另一种框架（如 ONNX 或 CoreML）时，验证转换后的结构完整性。

4. **技术亮点**
*   **广泛的格式兼容性**：几乎涵盖了当前所有主流的深度学习模型保存格式，是行业标准的可视化工具之一。
*   **轻量级与易用性**：无需安装复杂的依赖环境，通过简单的拖拽或打开文件即可实现可视化，极大降低了分析门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33234 | 🍴 3156 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21157 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一部全面涵盖机器学习工程实践的技术指南。它深入探讨了从模型训练、调试到大规模部署及推理优化的全流程关键知识。

2. **核心功能**
*   提供大规模分布式训练与超参数调优的最佳实践。
*   详解高性能模型推理优化及内存管理技巧。
*   涵盖GPU硬件特性、网络通信及存储I/O优化。
*   包含针对LLM等大型模型的调试与故障排除方法。
*   介绍Slurm集群管理及ML基础设施的可扩展性设计。

3. **适用场景**
*   构建和优化大规模分布式深度学习训练集群。
*   部署低延迟、高吞吐量的LLM推理服务。
*   解决大型语言模型训练过程中的显存溢出或性能瓶颈。
*   设计可扩展的企业级MLOps流水线与基础设施。

4. **技术亮点**
*   深度结合PyTorch生态与Transformer架构的实际落地经验。
*   涵盖从底层硬件（GPU/网络）到上层应用（LLM/MLOps）的全栈视角。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18409 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17321 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13147 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11577 | 🍴 908 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的代码示例，帮助开发者快速掌握各类人工智能技术的实际应用方法。

2. **核心功能**
*   收录大量涵盖不同AI子领域的完整项目案例与源代码。
*   提供从基础机器学习到前沿深度学习的多维度技术实践。
*   集成计算机视觉与自然语言处理（NLP）的具体落地项目。
*   作为“Awesome”系列资源， curated 精选高质量AI学习材料。

3. **适用场景**
*   AI初学者希望通过实战代码快速理解理论概念的学习场景。
*   研究人员或工程师寻找特定领域（如CV、NLP）参考实现的项目开发场景。
*   需要构建AI作品集以展示技术能力的求职准备场景。

4. **技术亮点**
*   资源规模庞大且分类清晰，覆盖AI主要热门方向。
*   强调“带代码”的实战性，便于直接复现和修改。
*   被标记为“awesome”，意味着内容经过筛选，质量较高。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35463 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33234 | 🍴 3156 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目提供了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。内容涵盖了从基础数学工具到主流框架的关键代码片段与概念总结。它是快速回顾知识要点和解决常见编码问题的实用资源库。

2. **核心功能**
*   提供涵盖NumPy、SciPy等数值计算库的快速参考指南。
*   包含Matplotlib数据可视化常用代码模板与配置技巧。
*   整理Keras等深度学习框架的关键API使用示例。
*   汇总机器学习算法中的核心公式与参数说明。
*   以紧凑的单页或短文档形式呈现，便于快速检索。

3. **适用场景**
*   研究人员在进行实验前快速复习框架语法和数学公式。
*   开发者在调试代码时查阅特定函数或库的标准用法。
*   学生准备考试或面试时作为核心知识点的手册。
*   团队内部共享标准化代码风格和最佳实践参考。

4. **技术亮点**
*   高度凝练的信息呈现方式，极大降低了查阅时间成本。
*   覆盖从底层数据处理到高层模型构建的全流程关键技能。
*   基于Medium文章整理，内容权威且贴合实际研究需求。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并实现就业实战。内容涵盖 Python、机器学习、深度学习、计算机视觉、自然语言处理及数据分析等热门技术领域。

### 2. 核心功能
*   提供系统化的 AI 学习路径，涵盖从数学基础到高级算法的完整知识体系。
*   收录近 200 个实战案例和项目，强调动手实践以增强就业竞争力。
*   免费开放配套教材和学习资源，降低人工智能入门门槛。
*   覆盖主流框架与工具，包括 PyTorch、TensorFlow、Keras、Pandas、NumPy 等。
*   整合多领域热门方向，如计算机视觉（CV）、自然语言处理（NLP）和数据科学。

### 3. 适用场景
*   希望从零开始系统学习人工智能与机器学习的初学者。
*   需要大量实战项目参考以提升编程能力和工程经验的进阶学习者。
*   寻求免费高质量学习资料以准备求职或转行的数据科学从业者。
*   想要快速了解 CV、NLP 等特定 AI 子领域核心技术与应用的开发者。

### 4. 技术亮点
*   **资源高度集成**：将分散的知识点、代码库和教程整合为一条清晰的学习路线。
*   **实战导向明确**：通过近 200 个实际案例连接理论与应用，直接服务于就业需求。
*   **生态覆盖广泛**：兼容 TensorFlow、PyTorch、Caffe 等多种主流深度学习框架及数据分析库。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13147 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11738 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9136 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3101 | 语言: C++
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
- ⭐ 6260 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
该项目是一个全面的中英文自然语言处理（NLP）资源集合，涵盖了从基础文本清洗（如敏感词检测、繁简转换）到高级语义分析（如情感分析、实体识别）的多种工具和数据集。它整合了大量预训练模型、专业领域词库（如医疗、法律、汽车）以及语音识别、知识图谱构建相关的开源资源，旨在为开发者提供一站式的NLP解决方案。

### 2. 核心功能
- **文本预处理与清洗**：提供中英文敏感词过滤、停用词、反动词表、繁简转换及标点修复等基础工具。
- **信息抽取与实体识别**：支持姓名、手机号、身份证、邮箱等实体抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
- **语义分析与情感计算**：包含词汇情感值、同义词/反义词库、句子相似度匹配算法及文本情感分析工具。
- **语料库与数据集**：汇集了大量中文语料，包括聊天语料、谣言数据、古诗词、行业专有名词库及多语言语音数据集。
- **模型与工具集成**：整理了各类NLP预训练模型（如BERT, GPT-2, ALBERT）、OCR工具、语音识别（ASR）系统及知识图谱构建框架。

### 3. 适用场景
- **内容安全审核**：互联网平台可利用其中的敏感词库、暴恐词表及反动词表，快速构建内容过滤系统。
- **智能客服与对话机器人**：开发者可参考其中的聊天语料、意图识别及对话系统架构（如Rasa, ConvLab），构建更自然的中文对话机器人。
- **垂直领域知识图谱构建**：金融、医疗、法律等行业可利用其提供的专属词库、实体抽取工具及知识图谱数据，构建领域特定的知识库。
- **NLP算法研究与原型开发**：研究人员可利用其中汇总的最新预训练模型、数据集及基准测试（Benchmark），快速复现或改进NLP算法。

### 4. 技术亮点
- **资源高度聚合**：不仅包含代码，还整合了海量数据集、专业词库、预训练模型及学术论文，极大降低了NLP入门和研究的资源搜集成本。
- **覆盖全产业链**：从底层的文本清洗、分词，到中层的实体抽取、情感分析，再到上层的知识图谱、对话系统，提供了全链路的技术参考。
- **紧跟前沿技术**：收录了BERT、GPT-2、ALBERT、ERNIE等主流预训练模型的相关实现与应用案例，反映了NLP领域的最新技术趋势。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81833 | 🍴 15248 | 语言: Python

### LlamaFactory
- 以下是关于 GitHub 项目 **LlamaFactory** 的技术分析：

1. **中文简介**
   LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和多模态大模型（VLM）进行训练。该项目在 ACL 2024 上发表，旨在简化从指令微调、全量微调到强化学习对齐（RLHF）的各种训练流程。它通过整合主流算法，为用户提供了低门槛、高性能的大模型定制解决方案。

2. **核心功能**
   - **广泛模型支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流 LLM 和 VLM 架构。
   - **多样化微调策略**：内置 LoRA、QLoRA、P-Tuning 及全参数微调等多种高效微调方法。
   - **对齐与优化能力**：支持 RLHF（基于人类反馈的强化学习）、DPO 等对齐技术，提升模型输出质量。
   - **量化部署集成**：提供 INT4/INT8 量化训练与推理支持，显著降低硬件资源需求。
   - **统一训练接口**：通过 YAML 配置文件即可轻松切换不同模型和微调任务，无需修改代码。

3. **适用场景**
   - **企业级知识增强**：利用私有数据对基座模型进行指令微调，构建垂直领域专用助手。
   - **资源受限环境部署**：在显存有限的 GPU 上，使用 QLoRA 等技术高效微调大型模型。
   - **多模态应用开发**：快速适配并微调具备视觉理解能力的 VLM，用于图文生成或识别任务。
   - **算法研究与实验**：作为基准平台，快速验证不同微调算法（如 LoRA vs DPO）在不同模型上的表现。

4. **技术亮点**
   - **极致效率**：通过 FlashAttention-2 和 Unsloth 等技术加速，训练速度可达传统方法的数倍。
   - **生态融合**：无缝对接 Hugging Face Transformers 和 PEFT 库，同时保持独立易用性。
   - **全栈支持**：涵盖从数据处理、模型训练到推理部署的全生命周期工具链。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73320 | 🍴 8951 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个持续更新的系统提示词（System Prompts）泄露合集，内容涵盖 Anthropic (Claude)、OpenAI (ChatGPT/Codex)、Google (Gemini) 及 xAI (Grok) 等主流大语言模型及其相关工具（如 Cursor、VS Code 插件）。它通过提取这些模型的内部指令，为研究者和开发者提供了宝贵的参考资源。

### 2. 核心功能
*   **多模型提示词收集**：汇总了 Claude、GPT、Gemini 等多个顶级 AI 模型的底层系统指令。
*   **定期自动更新**：保持内容时效性，持续收录新发布的模型版本及工具的最新泄露提示词。
*   **开源社区维护**：作为一个公开的资源库，方便开发者快速获取和查阅最新的 Prompt 工程素材。
*   **跨平台覆盖**：不仅包含基础聊天模型，还延伸至代码助手（Copilot）、IDE 插件（Cursor/VS Code）等专业工具。

### 3. 适用场景
*   **Prompt 工程优化**：帮助开发者分析优秀提示词的结构，从而编写出更高效的自定义指令。
*   **AI 安全与研究**：用于研究大模型的内部行为机制、潜在漏洞及对齐策略。
*   **竞品分析与学习**：让从业者深入了解不同厂商模型在角色设定、约束条件上的设计差异。
*   **教育与技术分享**：作为教学案例，向初学者展示系统提示词在实际应用中的复杂性。

### 4. 技术亮点
*   **高知名度与影响力**：拥有超过 5.8 万星标，显示其在 AI 社区中极高的关注度和参考价值。
*   **广泛的生态覆盖**：标签涵盖了从基础 LLM 到具体的 Agent 框架及开发工具，体现了其内容的全面性。
*   **实时动态追踪**：相较于静态文档，该项目能敏锐捕捉最新模型发布后的提示词变动，具备较强的时效性优势。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58226 | 🍴 9622 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个由微软发起的为期12周、包含24课时的AI入门课程，旨在让所有人轻松掌握人工智能知识。项目采用Jupyter Notebook形式呈现，内容涵盖从基础机器学习到深度学习及自然语言处理的核心概念。

2. **核心功能**
*   提供结构化的12周学习计划，将复杂的AI概念拆解为24个易于理解的课程模块。
*   基于Jupyter Notebook编写，支持交互式代码执行与实时结果展示，便于动手实践。
*   覆盖广泛的AI领域，包括计算机视觉（CNN）、生成对抗网络（GAN）、NLP及RNN等关键技术。
*   作为“Microsoft For Beginners”系列的一部分，专为编程初学者和非专家设计，降低学习门槛。

3. **适用场景**
*   希望系统了解AI基础知识但缺乏专业背景的初学者或跨领域学习者。
*   高校或培训机构用于开展人工智能导论课程的配套教材和实践资源。
*   开发者想要快速上手并复习特定AI子领域（如NLP或计算机视觉）的实战案例。

4. **技术亮点**
*   高度模块化和社区驱动，拥有极高的Star数（52350+），证明了其广泛的影响力和实用性。
*   紧跟前沿技术栈，不仅涵盖传统机器学习，还深入讲解深度学习和生成式AI的最新应用。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52350 | 🍴 10588 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. 中文简介
该项目是一个涵盖数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）的综合学习库。它结合自然语言处理工具（NLTK）与经典算法库（Scikit-learn），旨在为开发者提供从理论到实践的完整AI学习路径。

### 2. 核心功能
*   集成多种经典机器学习算法实现，包括决策树、支持向量机（SVM）、K-Means聚类及主成分分析（PCA）。
*   涵盖深度学习核心模型实战，如RNN、LSTM、DNN及基于PyTorch和TensorFlow 2的深度网络构建。
*   提供自然语言处理（NLP）相关工具与算法，如AdaBoost、Apriori关联规则挖掘及朴素贝叶斯分类。
*   包含推荐系统、逻辑回归、线性回归等实用模块，并辅以线性代数等数学基础讲解。

### 3. 适用场景
*   **AI初学者入门**：适合希望系统掌握机器学习理论与代码实现的零基础学习者。
*   **面试准备**：适合需要复习经典算法原理及手写代码以实现求职准备的求职者。
*   **算法复现与研究**：适合研究人员参考其标准化实现来验证或复现特定机器学习算法。

### 4. 技术亮点
*   **全栈覆盖**：同时囊括传统机器学习、深度学习、NLP及推荐系统，构建完整知识体系。
*   **多框架支持**：兼顾主流工业界框架（PyTorch、TF2）与经典库（Scikit-learn），适应不同开发需求。
*   **理论与实践结合**：不仅提供代码实现，还强调背后的数学原理（如线性代数），深化对算法本质的理解。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42381 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38456 | 🍴 6443 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35463 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33742 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28576 | 🍴 3486 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25910 | 🍴 2924 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35463 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22345 | 🍴 2092 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉AI数据集的领先平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证及团队协作，并配备开发者API。

2. **核心功能**
*   支持图像、视频及3D点云的多样化数据标注。
*   内置AI辅助标注功能以显著提升数据处理效率。
*   提供完善的质量保证机制与团队多人协作能力。
*   开放开发者API以便集成到现有工作流中。

3. **适用场景**
*   需要大规模构建高精度视觉数据集的AI研发团队。
*   进行目标检测、语义分割等深度学习模型训练的数据预处理。
*   需要严格质量控制和多人员协同工作的企业级标注项目。

4. **技术亮点**
*   采用Python开发，生态兼容性好，支持PyTorch和TensorFlow框架。
*   提供从开源自托管到云端服务再到企业版的多层次部署方案。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16303 | 🍴 3762 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 基于提供的GitHub项目信息，以下是关于 **Kornia** 的技术分析：

### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在提供可微分的图像处理原语，从而无缝集成到深度学习工作流程中。该库简化了传统计算机视觉任务与神经网络训练的结合过程。

### 2. 核心功能
*   **可微分图像处理**：提供完全可微分的几何和图像操作，允许梯度反向传播以支持端到端训练。
*   **PyTorch 原生集成**：作为 PyTorch 的扩展库，直接支持张量运算，无需转换数据格式即可嵌入现有深度学习模型。
*   **几何与相机校准**：内置用于相机内参、外参及畸变校正的几何计算工具，适用于机器人视觉等场景。
*   **传统 CV 算法现代化**：将经典的计算机视觉算法（如边缘检测、特征匹配、滤波）转化为可微分形式。

### 3. 适用场景
*   **不同渲染与生成模型**：在 GANs 或扩散模型中引入物理约束或几何一致性损失。
*   **机器人视觉系统**：用于需要精确空间理解和实时处理的机器人导航与操作任务。
*   **增强现实（AR）与三维重建**：辅助处理相机位姿估计、点云对齐及三维场景理解。
*   **医疗影像分析**：利用可微分的图像变换进行配准、分割前的预处理或数据增强。

### 4. 技术亮点
*   **端到端可训练性**：突破了传统 OpenCV 等非可微库的限制，使整个视觉流水线（从输入到损失计算）均可通过自动微分进行优化。
*   **高性能 GPU 加速**：充分利用 GPU 并行计算能力，显著加速复杂的几何变换和图像操作。
*   **模块化设计**：提供丰富的原子化操作模块，便于研究人员快速构建自定义的损失函数或网络层。
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
- ⭐ 3283 | 🍴 403 | 语言: Python
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
- ### 项目分析：OpenClaw

**1. 中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，致力于让用户以“龙虾方式”完全掌控自己的数据。它强调私有化和本地化部署，确保隐私安全的同时提供便捷的智能辅助体验。

**2. 核心功能**
*   **跨平台兼容**：支持在任何主流操作系统和硬件平台上运行。
*   **数据自主权**：强调“拥有自己的数据”，所有信息均在本地处理，保障隐私。
*   **个性化 AI 助手**：提供高度可定制的个人助理服务，适应不同用户需求。
*   **开源开放**：基于 TypeScript 构建，社区活跃，便于二次开发和集成。

**3. 适用场景**
*   **注重隐私的用户**：希望在不依赖云端服务的情况下，安全地管理个人数据和日常任务。
*   **开发者与技术爱好者**：喜欢折腾新技术，希望通过本地部署来定制专属 AI 助手的人群。
*   **企业或团队内部助手**：需要私有化部署 AI 工具，且对数据合规性有严格要求的场景。

**4. 技术亮点**
*   **全栈 TypeScript 实现**：利用 TypeScript 的类型安全和现代前端/后端开发优势，提升代码可维护性。
*   **轻量级架构**：相比大型云服务，OpenClaw 更注重本地运行效率与资源占用平衡。
*   **社区驱动创新**：通过活跃的 GitHub 社区（近 39 万星），持续快速迭代功能与安全补丁。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383088 | 🍴 80450 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 255679 | 🍴 22853 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215672 | 🍴 40223 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个采用公平开源协议的工作流自动化平台，具备原生 AI 能力，支持可视化构建与自定义代码相结合。它提供超过 400 种集成方式，允许用户选择自行托管或云端部署，实现高效的数据流与工作流管理。

### 2. 核心功能
*   **原生 AI 集成**：内置 AI 能力，可轻松将人工智能模型融入工作流中。
*   **灵活的开发模式**：结合可视化拖拽界面与自定义代码（TypeScript），满足从低代码到专业开发的需求。
*   **丰富的集成生态**：提供 400 多种预建连接器，覆盖主流 API 和服务。
*   **多部署选项**：支持自我托管以保障数据隐私，也提供便捷的云服务选项。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP) 客户端与服务端，增强与大模型的交互能力。

### 3. 适用场景
*   **企业自动化**：自动连接 CRM、ERP 和数据库，实现跨系统的数据同步与业务流程自动化。
*   **AI 应用开发**：快速搭建基于 LLM 的智能助手或数据处理管道，利用原生 AI 节点优化内容生成与分析。
*   **开发者工具链**：通过自定义代码节点和 CLI 工具，构建复杂的后端服务逻辑或自动化测试流程。

### 4. 技术亮点
*   **公平开源协议 (Fair-code)**：在保持核心功能开放的同时，规范商业使用，平衡社区与开发者利益。
*   **TypeScript 原生支持**：作为 TypeScript 项目，提供了良好的类型安全和开发体验，便于扩展和维护。
*   **MCP 兼容性**：紧跟技术前沿，通过支持 MCP 协议，无缝对接最新的大语言模型上下文标准。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196625 | 🍴 59356 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 旨在让每个人都能轻松使用并构建基于人工智能的工具，实现 AI 的普及化愿景。其核心使命是提供强大的基础设施，让用户能够专注于真正重要的业务逻辑与价值创造。

### 2. 核心功能
*   **自主智能体执行**：能够独立规划、分解任务并执行复杂的多步骤工作流。
*   **多模型兼容支持**：广泛兼容 GPT、Claude、Llama 等主流大语言模型 API。
*   **开放式构建生态**：提供灵活的工具集，方便开发者基于其架构进行二次开发和定制。
*   **自动化任务处理**：通过 Agent 模式自动完成从信息检索到代码执行的一系列操作。

### 3. 适用场景
*   **复杂工作流自动化**：适用于需要跨多个应用和数据源进行协调的长周期自动化任务。
*   **AI 应用原型开发**：开发者可利用其作为基础框架，快速搭建和测试自定义的 AI 智能体应用。
*   **研究与实验平台**：适合对自主智能体（Agentic AI）行为、局限性及安全性进行深入研究的场景。

### 4. 技术亮点
*   **高度可扩展的 Agent 架构**：采用模块化设计，允许用户轻松插拔不同的工具、记忆模块和模型后端。
*   **前沿的 Agentic AI 实践**：代表了当前开源社区在构建自主决策和执行能力方面的最高水平之一。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185574 | 🍴 46078 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165846 | 🍴 21451 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164273 | 🍴 30528 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157067 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151944 | 🍴 9680 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151707 | 🍴 8667 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

