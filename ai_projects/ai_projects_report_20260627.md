# GitHub AI项目每日发现报告
日期: 2026-06-27

## 新发布的AI项目

### video-production-skills
- 1. **中文简介**
这是一个可复用的AI视频制作技能库，旨在通过模块化技能提升视频创作效率。它涵盖了从内容生成、动作设计到质量质检的全流程自动化处理。

2. **核心功能**
*   支持AI驱动的视频内容创建与重构。
*   集成动态图形设计与开场动画生成能力。
*   提供自动化的视频质量检测（QA）功能。
*   采用模块化架构，便于技能组件的复用与扩展。

3. **适用场景**
*   需要批量生成营销短视频或社交媒体素材的团队。
*   希望利用AI辅助完成视频剪辑、特效合成及后期质检的工作流优化。
*   开发需要集成视频自动化处理能力的应用程序或插件。

4. **技术亮点**
*   基于Python构建，具备良好的可扩展性和社区兼容性。
*   聚焦于“技能（Skills）”模块化设计，实现不同视频制作环节的解耦与复用。
- 链接: https://github.com/Pluviobyte/video-production-skills
- ⭐ 313 | 🍴 33 | 语言: Python

### Godcoder
- 1. **中文简介**
Godcoder 是一款本地优先的开源桌面编码智能体，旨在让用户完全掌控代码数据。用户只需提供自己的大语言模型 API 密钥，代码仅保留在本地机器上，仅在请求时发送给模型提供商，确保隐私与安全。

2. **核心功能**
- 采用本地优先架构，确保代码数据始终存储在用户本地设备中。
- 支持自定义接入任意大语言模型，用户需自行提供有效的 API 密钥。
- 基于 Rust 和 Tauri 构建，提供轻量级且高性能的桌面应用体验。
- 集成 MCP（Model Context Protocol）标准，增强与外部工具和数据源的连接能力。
- 开源开放，允许开发者审查代码并根据需求进行定制或二次开发。

3. **适用场景**
- 对代码隐私和安全有极高要求的开发团队或个人开发者。
- 希望灵活切换不同大语言模型后端以优化成本或效果的技术爱好者。
- 需要本地化、离线或低延迟辅助编程的桌面端用户。
- 致力于探索 MCP 协议在桌面编程智能体中应用的实验性项目。

4. **技术亮点**
- 使用 Rust 编写核心逻辑，结合 Tauri 框架实现高效、安全的跨平台桌面应用。
- 原生支持 MCP 协议，便于扩展丰富的上下文感知能力和工具集成。
- 链接: https://github.com/eli-labz/Godcoder
- ⭐ 128 | 🍴 0 | 语言: Rust
- 标签: ai, coding-agent, desktop-app, llm, local-first

### macos-chatgpt-overlay-bar
- 1. **中文简介**
这是一款专为 macOS 设计的 ChatGPT 菜单栏工具，让 AI 助手常驻系统状态栏。用户无需打开独立应用，即可通过便捷的界面快速访问 ChatGPT 服务。

2. **核心功能**
*   在 macOS 菜单栏中直接集成 ChatGPT 聊天界面。
*   提供极速的 AI 交互入口，支持随时调用智能问答。
*   轻量级运行，不占用额外桌面空间或后台资源。
*   简化操作流程，实现一键呼出与对话。

3. **适用场景**
*   需要频繁查询信息或辅助写作的办公场景。
*   希望在不打断当前工作流的情况下快速获取 AI 帮助的用户。
*   偏好极简界面，不喜欢打开大型独立应用的 macOS 爱好者。

4. **技术亮点**
该项目利用原生菜单栏集成技术，实现了极低延迟的交互体验，并保持了高度的视觉简洁性与系统兼容性。
- 链接: https://github.com/ik190/macos-chatgpt-overlay-bar
- ⭐ 70 | 🍴 6 | 语言: 未知
- 标签: ai, chatgpt, chatgpt-bar-mac, chatgpt-menubar-mac, chatgpt-quick-access-mac

### ritual-agent-deployment
- ### 1. **中文简介**
该项目旨在通过单一命令在 Ritual 测试网上部署一个可循环运行且具备自我资助能力的独立 AI 智能体。它简化了去中心化智能体的初始化流程，使其能够自动化执行任务并管理自身资金。

### 2. **核心功能**
*   **一键部署**：利用 PowerShell 脚本实现智能体环境的快速初始化和配置。
*   **自我资助机制**：内置逻辑确保智能体能够自动管理资金以维持持续运行。
*   **独立主权性**：作为“主权”智能体运行，具备自主决策和执行能力。
*   **Ritual 集成**：专为 Ritual 测试网环境优化，兼容其基础设施标准。
*   **自动化调度**：支持周期性重复任务执行，无需人工频繁干预。

### 3. **适用场景**
*   **开发者测试**：用于在 Ritual 测试网上快速验证 AI 智能体的部署流程和兼容性。
*   **自动化服务原型**：构建需要长期运行并自主管理资源的后台自动化服务。
*   **去中心化应用实验**：探索基于区块链或分布式网络的自持型智能体应用模式。
*   **教育演示**：向初学者展示如何从零开始搭建和运行一个具备经济模型的 AI 代理。

### 4. **技术亮点**
*   **极简操作**：通过单行命令降低复杂分布式系统的部署门槛。
*   **PowerShell 实现**：利用 Windows 生态下强大的脚本能力进行系统级配置和管理。
*   **闭环经济模型**：将智能体行为与资金管理紧密结合，实现真正的“自我维持”。
- 链接: https://github.com/zunmax/ritual-agent-deployment
- ⭐ 53 | 🍴 38 | 语言: PowerShell
- 标签: ai-agent, ritual-testnet

### AngleCraft
- 1. **中文简介**
AngleCraft 是一款通用的 AI 技能工具，旨在通过运用 7+2 种新闻学角度类型，将枯燥的专业话题转化为高互动性的优质内容。它具备跨平台兼容性，可适配任何大型语言模型、垂直领域及语言环境。

2. **核心功能**
*   **多角内容生成**：利用特定的新闻学框架（7+2 角度）重构专业主题，提升内容吸引力。
*   **通用兼容性**：作为独立 AI 技能运行，支持接入任意大语言模型（LLM）。
*   **全领域与多语言支持**：能够处理各种垂直领域的专业知识，并支持多种语言的输出。
*   **提示词工程优化**：内置经过优化的 Prompt 结构，简化用户调用流程。

3. **适用场景**
*   **内容营销与社交媒体运营**：将晦涩的行业报告或技术文档转化为适合在社交平台上传播的故事。
*   **新闻通讯（Newsletter）撰写**：为专业领域的订阅者生成兼具深度与可读性的定期通讯内容。
*   **创意文案与故事创作**：帮助创作者从独特视角切入，丰富文章或视频脚本的叙事维度。

4. **技术亮点**
该项目采用纯提示词（Prompt-based）架构，无需编写代码即可集成到现有的 AI 工作流中，实现了零代码门槛的内容策略自动化。
- 链接: https://github.com/MADEVAL/AngleCraft
- ⭐ 46 | 🍴 14 | 语言: 未知
- 标签: agent-skill, ai-skill, anglecraft, content-creation, content-marketing

### cheat-on-skill
- 描述: 帮你在 AI 时代找到一份高薪 × 你学得动 × 不会被 AI 吃掉的工作，并给出个性化学习陪跑计划。能力匹配 + 可学性闸门 + BOSS 直聘真实招聘数据 + 反诈。
- 链接: https://github.com/XBuilderLAB/cheat-on-skill
- ⭐ 44 | 🍴 3 | 语言: JavaScript
- 标签: ai-career, anthropic, career-transition, claude-code, claude-skills

### Anti-Autoresearch
- 描述: Don't trust an autoresearch paper at face value. Reviewer-side integrity forensics — self-consistency + fabrication checks across 48 hack-patterns (8 families), deterministic verdict. Not an AI-text detector. The dual of ARIS.
- 链接: https://github.com/wanshuiyin/Anti-Autoresearch
- ⭐ 44 | 🍴 2 | 语言: Python
- 标签: ai-generated-content, ai-scientist, autoresearch, forensics, llm-agents

### Tidal_Echo
- 描述: 一个**私密 1:1 聊天通道**：把「你手机上的 PWA」和「你电脑上跑的 AI 伴侣」连起来。 AI 侧以 **Claude Code 的 channel 插件**形态运行——你在手机上发消息，Claude Code 会话里就冒出 `<channel>` 块；AI 调一个 `reply` 工具，你手机就收到气泡。
- 链接: https://github.com/anhe2021212-spec/Tidal_Echo
- ⭐ 41 | 🍴 15 | 语言: HTML

### Personal-Comparative-Advantage-Engine-PCAE
- 描述: Personal Comparative Advantage Engine - A Skill to discover your unique advantages in the AI era | AI时代个人优势发现引擎
- 链接: https://github.com/KeGong-XKK/Personal-Comparative-Advantage-Engine-PCAE
- ⭐ 40 | 🍴 0 | 语言: 未知

### semaphore
- 描述: Floating traffic light for AI coding agents (know when your agent is idle, thinking, or writing)
- 链接: https://github.com/lucianodiisouza/semaphore
- ⭐ 28 | 🍴 2 | 语言: Rust
- 标签: ai, claude, codex, coding, copilot

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具包，旨在为开发者提供丰富的基础组件与资源。它集成了敏感词过滤、中英文分词、实体抽取、情感分析及多种专业领域词库，并汇聚了大量高质量的中文 NLP 数据集、预训练模型及开源项目资源。

2. **核心功能**
*   **基础文本处理**：提供敏感词检测、繁简体转换、中英文分词、词性标注、命名实体识别（NER）及句法分析。
*   **实体与信息抽取**：支持手机号、身份证号、邮箱等特定格式抽取，以及基于 BERT 等模型的关键词抽取、摘要生成和关系抽取。
*   **知识与词库资源**：内置中日文人名库、职业/汽车品牌/地名/医学/法律等专业词库，以及同义词、反义词、停用词等辅助资源。
*   **语音与多模态支持**：包含中文语音识别（ASR）工具、音频数据增强、语音情感分析以及中文手写汉字识别功能。
*   **前沿模型与数据集集成**：整合了 BERT、ERNIE、RoBERTa 等主流预训练模型，以及大量中文问答、对话、知识图谱构建的数据集和代码示例。

3. **适用场景**
*   **内容安全审核**：用于互联网平台的敏感词过滤、暴恐词检测及谣言识别，保障内容合规。
*   **智能客服与对话系统**：利用闲聊语料、知识图谱和对话数据集，快速搭建具备语义理解和多轮对话能力的智能助手。
*   **垂直领域知识挖掘**：在医疗、金融、法律等专业领域，通过专用词库和 NER 模型提取关键信息，构建领域知识图谱或问答系统。
*   **NLP 研究与教学参考**：作为研究人员或学生查找中文 NLP 数据集、复现经典算法（如 BERT-NER、文本摘要）及了解行业前沿动态的资源库。

4. **技术亮点**
*   **资源聚合度高**：不仅包含代码工具，还广泛收录了清华大学、百度、Facebook 等机构发布的权威数据集、技术报告及预训练模型。
*   **覆盖范围广**：从基础的文本清洗到高级的深度学习模型微调，再到语音处理和非结构化数据（如简历、表格）解析，提供了端到端的解决方案参考。
*   **注重实用性与落地**：提供了大量经过实战验证的代码片段、竞赛 TOP 方案复盘及具体的业务场景（如简历筛选、医疗问答）实现细节。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81477 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和源代码参考。它通过整理大量高质量的项目资源，帮助用户快速入门并深入理解人工智能的核心技术。

2. **核心功能**
- 提供涵盖机器学习、深度学习、CV及NLP领域的500多个完整项目代码示例。
- 包含“Awesome”系列精选资源，确保项目质量和实用性。
- 主要基于Python语言实现，方便开发者直接运行和学习。
- 分类清晰，便于用户根据具体技术栈或应用场景查找资料。

3. **适用场景**
- 初学者希望通过实际代码快速掌握AI基本概念和流程。
- 研究人员或工程师寻找特定算法（如图像识别、文本处理）的参考实现。
- 教育者用于制作课程案例或布置编程作业。
- 个人开发者希望构建AI原型以验证创意或解决特定问题。

4. **技术亮点**
- 资源规模庞大，集成了数百个经过筛选的高质量开源项目。
- 标签体系完善，支持按技术领域（如`computer-vision`, `nlp`）精准检索。
- 作为社区驱动的“Awesome”列表，持续更新以保持技术前沿性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34961 | 🍴 7297 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和参数。该工具旨在简化模型调试与分析过程，提升开发效率。

2. **核心功能**
- 支持查看多种框架（如 TensorFlow、PyTorch、ONNX 等）的模型结构。
- 提供直观的图形化界面展示网络层连接与数据流向。
- 允许用户检查模型中的权重、偏置及其他参数细节。
- 兼容多种模型文件格式，包括 CoreML、Keras、TensorFlow Lite 等。
- 具备离线桌面应用与在线网页版两种使用方式，便于快速部署。

3. **适用场景**
- 深度学习研究人员用于调试复杂模型架构并验证层配置。
- 工程师在部署前检查转换后的模型（如从 PyTorch 转 ONNX）是否保持一致。
- 初学者通过可视化界面理解神经网络的数据流动与组件关系。
- 团队内部共享模型结构文档，便于非技术人员理解算法逻辑。

4. **技术亮点**
- 广泛支持异构模型格式，实现跨框架的统一可视化体验。
- 采用 Electron 构建桌面端，结合 Web 技术实现轻量级在线预览。
- 社区活跃，星标数高，反映其在 AI 工具链中的重要地位。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33143 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是机器学习领域的互操作性开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型在多种环境和平台间的无缝迁移与部署。通过统一的格式，开发者可以更方便地在训练、推理和优化环节之间切换工具链。

2. **核心功能**
*   定义开放的模型格式标准，支持跨框架的模型交换。
*   提供丰富的算子库，涵盖主流深度学习网络结构所需的基础操作。
*   集成ONNX Runtime等高性能推理引擎，优化模型执行效率。
*   支持模型转换工具，便于从PyTorch、TensorFlow等源框架导出模型。
*   促进生态兼容性，允许不同厂商的工具链协同工作。

3. **适用场景**
*   需要将模型从PyTorch或TensorFlow迁移到移动端或嵌入式设备部署。
*   在异构硬件（如CPU、GPU、NPU）上追求统一且高效的推理性能。
*   企业级应用中需要整合多个不同框架训练的模型进行联合服务。
*   开发自定义AI芯片或推理引擎时，需要遵循行业标准以兼容现有模型。

4. **技术亮点**
*   实现了真正的框架无关性，解耦了模型定义与具体执行环境。
*   拥有活跃的开源社区支持，被微软、Facebook、Amazon等主要科技巨头共同维护。
*   提供了完善的优化工具链（如GraphSurgeon），支持算子融合与图级别优化。
- 链接: https://github.com/onnx/onnx
- ⭐ 21055 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面介绍机器学习工程最佳实践的开源指南。它涵盖了从模型训练、调试到大规模部署和推理的全生命周期技术细节。该项目旨在帮助工程师高效构建可扩展且可靠的机器学习系统。

2. **核心功能**
*   提供LLM训练、微调和推理的详细工程实践指导。
*   深入解析GPU硬件利用、网络通信及存储优化策略。
*   涵盖基于PyTorch和Transformers框架的可扩展性设计。
*   包含SLURM集群管理、调试技巧及MLOps运维规范。

3. **适用场景**
*   需要在大规模集群上训练大型语言模型（LLM）的工程团队。
*   希望优化深度学习模型推理延迟和吞吐量的开发人员。
*   正在搭建或维护机器学习基础设施及MLOps流水线的架构师。
*   寻求GPU资源高效利用和分布式训练调优的技术研究者。

4. **技术亮点**
该项目作为“开放书籍”，提供了极具深度的实战级工程知识，特别聚焦于当前热门的大语言模型（LLM）和生成式AI领域的底层硬件与软件协同优化，是连接理论算法与生产环境落地的宝贵资源。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18180 | 🍴 1154 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17258 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13090 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11528 | 🍴 903 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10644 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和源代码参考。它通过整理大量高质量的项目资源，帮助用户快速入门并深入理解人工智能的核心技术。

2. **核心功能**
- 提供涵盖机器学习、深度学习、CV及NLP领域的500多个完整项目代码示例。
- 包含“Awesome”系列精选资源，确保项目质量和实用性。
- 主要基于Python语言实现，方便开发者直接运行和学习。
- 分类清晰，便于用户根据具体技术栈或应用场景查找资料。

3. **适用场景**
- 初学者希望通过实际代码快速掌握AI基本概念和流程。
- 研究人员或工程师寻找特定算法（如图像识别、文本处理）的参考实现。
- 教育者用于制作课程案例或布置编程作业。
- 个人开发者希望构建AI原型以验证创意或解决特定问题。

4. **技术亮点**
- 资源规模庞大，集成了数百个经过筛选的高质量开源项目。
- 标签体系完善，支持按技术领域（如`computer-vision`, `nlp`）精准检索。
- 作为社区驱动的“Awesome”列表，持续更新以保持技术前沿性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34961 | 🍴 7297 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看模型结构和参数。该工具旨在简化模型调试与分析过程，提升开发效率。

2. **核心功能**
- 支持查看多种框架（如 TensorFlow、PyTorch、ONNX 等）的模型结构。
- 提供直观的图形化界面展示网络层连接与数据流向。
- 允许用户检查模型中的权重、偏置及其他参数细节。
- 兼容多种模型文件格式，包括 CoreML、Keras、TensorFlow Lite 等。
- 具备离线桌面应用与在线网页版两种使用方式，便于快速部署。

3. **适用场景**
- 深度学习研究人员用于调试复杂模型架构并验证层配置。
- 工程师在部署前检查转换后的模型（如从 PyTorch 转 ONNX）是否保持一致。
- 初学者通过可视化界面理解神经网络的数据流动与组件关系。
- 团队内部共享模型结构文档，便于非技术人员理解算法逻辑。

4. **技术亮点**
- 广泛支持异构模型格式，实现跨框架的统一可视化体验。
- 采用 Electron 构建桌面端，结合 Web 技术实现轻量级在线预览。
- 社区活跃，星标数高，反映其在 AI 工具链中的重要地位。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33143 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了 essential（关键/必备）的代码速查表。内容涵盖从基础概念到高级库使用的常用语法与技巧，旨在帮助研究者快速回顾和查阅核心技术点。

2. **核心功能**
*   提供机器学习算法及深度学习框架的核心代码片段速查。
*   汇总了 NumPy、SciPy、Matplotlib 等数据处理与可视化库的常用操作。
*   针对 Keras 等主流深度学习框架整理了模型构建与训练的快捷指南。
*   以结构化的笔记形式呈现，便于快速检索特定功能的语法细节。

3. **适用场景**
*   研究者在开发过程中忘记特定函数参数或用法时进行快速查询。
*   初学者在入门阶段系统梳理常用库的基本操作与语法。
*   在进行代码重构或迁移框架时，作为参考对照表使用。

4. **技术亮点**
*   由知名技术博主整理，内容经过实战验证，实用性强。
*   聚焦于高频使用的“痛点”代码，极大提升了编码效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并免费提供配套教材，帮助零基础用户轻松入门并具备就业实战能力。该项目涵盖Python编程、数学基础、机器学习、深度学习、计算机视觉及自然语言处理等热门技术领域。

### 2. **核心功能**
*   提供结构化的AI学习路径，从零基础到精通逐步引导。
*   收录近200个实战案例和项目，强化动手实践能力。
*   免费提供全套配套学习资料，降低学习门槛。
*   覆盖主流AI框架与工具，如TensorFlow、PyTorch、Keras、Pandas等。
*   聚焦就业导向，通过实战项目提升求职竞争力。

### 3. **适用场景**
*   希望系统学习人工智能从零开始入门的新手。
*   需要大量实战案例进行技术巩固和提升的在校学生或转行者。
*   寻求就业培训资源以提升简历含金量的求职者。
*   希望快速掌握特定AI领域（如CV、NLP）核心技能的开发者。

### 4. **技术亮点**
*   内容全面且免费，整合了从基础数学到高级深度学习的全栈知识体系。
*   强调“实战+教材”结合，确保学习者不仅能理解理论，还能动手实现。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13090 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11727 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8910 | 🍴 3101 | 语言: C++
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
- ⭐ 6190 | 🍴 724 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81477 | 🍴 15249 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72593 | 🍴 8875 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI。该项目通过系统化的教学设计，涵盖了从基础概念到高级应用的广泛主题。其目标是降低人工智能的学习门槛，促进技术的普及。

2. **核心功能**
*   提供结构化的12周学习路径，每周安排相应的课程内容。
*   包含24节精心设计的课程，涵盖机器学习和深度学习的核心领域。
*   采用Jupyter Notebook作为主要教学工具，支持交互式代码实验。
*   内容覆盖计算机视觉、自然语言处理及生成模型等多个AI子领域。
*   由Microsoft For Beginners团队支持，确保教育资源的开放性与高质量。

3. **适用场景**
*   初学者希望系统化地从零开始学习人工智能基础知识。
*   教育机构或教师寻找适合课堂使用的结构化AI教学大纲。
*   开发人员想要快速了解机器学习、深度学习等领域的最新实践。
*   个人爱好者希望通过动手实践项目来巩固AI理论概念。

4. **技术亮点**
*   采用Jupyter Notebook实现理论与代码的无缝结合，提升学习体验。
*   内容广泛涵盖CNN、RNN、GAN等主流深度学习架构的实际应用。
*   完全开源且免费，降低了大规模普及人工智能教育的成本。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48490 | 🍴 10065 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46546 | 🍴 7627 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖了数据分析、机器学习实战、线性代数基础以及深度学习框架（如PyTorch和TensorFlow 2）。它集成了自然语言处理工具NLTK，旨在为用户提供从理论到实践的系统化学习路径。

2. **核心功能**
- 提供线性代数等数学基础知识的详细讲解与代码实现。
- 包含基于Scikit-learn的经典机器学习算法（如SVM、KMeans、Adaboost等）的实战案例。
- 深入解析深度学习模型，涵盖RNN、LSTM、DNN及推荐系统相关技术。
- 集成自然语言处理（NLP）模块，利用NLTK进行文本分析与处理。

3. **适用场景**
- 希望系统掌握机器学习与深度学习理论的在校学生或自学者。
- 需要快速查阅经典算法原理与Python代码实现的初级数据科学家。
- 致力于构建推荐系统或进行NLP项目开发的工程师参考。

4. **技术亮点**
- 结合了传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）两大生态。
- 内容结构完整，从数学基础直达前沿AI应用，适合循序渐进的学习者。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42350 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36563 | 🍴 6019 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34961 | 🍴 7297 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33700 | 🍴 4688 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28218 | 🍴 3425 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25752 | 🍴 2884 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码资源库。该项目旨在为开发者提供从基础到高级的各类AI实战案例与完整代码实现。它涵盖了数据科学领域的多个核心方向，是学习和参考AI应用开发的优质资料集。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等多个领域的500+个项目代码。
*   包含完整的Python实现代码，方便用户直接运行、修改和二次开发。
*   按技术领域分类整理，帮助用户快速定位特定方向的实战案例。
*   作为“Awesome”列表，筛选并整合了高质量、具有代表性的开源AI项目。

3. **适用场景**
*   AI初学者通过阅读和运行具体代码，快速理解机器学习与深度学习的基本概念和应用。
*   开发者寻找特定任务（如图像识别、文本情感分析）的参考实现，以加速项目原型开发。
*   研究人员或学生需要收集大量相关领域的开源项目作为文献综述或技术调研的基础。

4. **技术亮点**
*   项目规模宏大且分类清晰，集成了人工智能主流子领域的全栈式代码资源。
*   所有项目均附带可执行的代码，强调实践性而非单纯的理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34961 | 🍴 7297 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22014 | 🍴 2057 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- **1. 中文简介**
CVAT 是领先的计算机视觉数据集构建平台，提供开源、云及企业级产品，支持图像、视频和3D标注。它具备AI辅助标注、质量保证、团队协作及开发者API等强大功能，旨在打造高质量的视觉AI数据。

**2. 核心功能**
*   支持图像、视频及3D数据的多种标注类型，包括边界框、语义分割和分类。
*   集成AI辅助标注技术，显著提升数据标注效率与准确性。
*   提供完善的质量保证机制与团队协作者管理功能，适合规模化作业。
*   开放开发者API，便于集成到现有的机器学习工作流中。

**3. 适用场景**
*   构建用于目标检测或图像分类的高质量训练数据集。
*   需要多人协作进行大规模视频或图像标注的企业团队。
*   希望利用预训练模型进行半自动标注以加速数据处理流程的研究人员。

**4. 技术亮点**
*   采用 Python 开发，深度兼容 PyTorch 和 TensorFlow 等主流深度学习框架生态。
*   提供从开源自托管到云服务及企业版的灵活部署选项，满足不同安全与规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16164 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级AI可解释性工具库，支持CNN、Vision Transformers等多种架构。它提供了分类、目标检测、分割及图像相似度分析等多种任务的可视化解释方案。

2. **核心功能**
- 支持Grad-CAM、Score-CAM等主流可解释性算法实现。
- 兼容卷积神经网络（CNN）与视觉Transformer（ViT）模型。
- 覆盖图像分类、目标检测、语义分割及图像相似度等多种任务。

3. **适用场景**
- 深度学习模型调试，通过可视化热力图定位模型关注区域。
- 医疗影像或自动驾驶等领域，向非技术人员解释AI决策依据。
- 学术研究，对比不同可解释性方法在特定任务上的表现。

4. **技术亮点**
- 高度模块化设计，轻松适配PyTorch生态下的各类预训练模型。
- 统一接口支持多种XAI（可解释AI）方法，降低使用门槛。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理算法和计算机视觉原语。该库旨在简化深度学习中的视觉任务开发流程。

2. **核心功能**
*   提供基于 GPU 加速的可微分图像处理和几何变换操作。
*   集成多种经典计算机视觉算法，如特征检测、相机标定和三维重建。
*   与 PyTorch 生态无缝兼容，支持端到端的神经网络训练。
*   包含丰富的预训练模型和工具，用于图像增强和数据增强。
*   支持机器人学和自动驾驶领域的空间感知任务。

3. **适用场景**
*   需要结合传统计算机视觉与深度学习的混合模型开发。
*   机器人视觉导航中的实时图像处理和几何计算。
*   自动驾驶系统中的传感器数据分析和环境理解。
*   医学影像分析等需要高精度几何对齐和变换的场景。

4. **技术亮点**
*   完全可微分的设计使得传统 CV 算法可直接嵌入深度学习流水线。
*   高性能的 CUDA 实现，充分利用 GPU 并行计算能力。
*   模块化架构，便于扩展和自定义新的视觉算子。
- 链接: https://github.com/kornia/kornia
- ⭐ 11253 | 🍴 1192 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8868 | 🍴 2193 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3255 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2616 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2413 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款跨平台、支持任意操作系统的个人 AI 助手，让用户以“龙虾方式”（The lobster way）完全掌控自己的数据。它旨在提供一个私密且自主的人工智能解决方案，确保用户数据的私有性和安全性。

### 2. 核心功能
- **全平台兼容**：支持任何操作系统和平台，实现无缝部署和使用。
- **数据自主权**：强调“拥有自己的数据”，确保用户隐私和数据安全。
- **个人化 AI 助手**：提供专属的个人人工智能辅助体验。
- **开源生态**：基于开源社区驱动，拥有活跃的标签和社区支持。

### 3. 适用场景
- **隐私敏感用户**：需要高度数据控制权和个人 AI 助手的科技爱好者。
- **跨平台开发者**：希望在不同操作系统上统一运行 AI 工具的开发者和系统管理员。
- **个人知识管理**：用于本地化整理笔记、代码片段或个人信息的智能助手场景。

### 4. 技术亮点
- 采用 TypeScript 开发，兼具类型安全和现代前端/后端开发效率。
- 独特的“龙虾”品牌标识与社区文化，增强了项目的辨识度和用户归属感。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380728 | 🍴 79766 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它旨在通过结构化的协作流程，提升人工智能辅助编程的效率与可靠性。该项目强调将复杂的开发任务拆解为可管理的智能体技能。

2. **核心功能**
*   提供一套完整的“智能体驱动开发”（Subagent-Driven Development）方法论。
*   内置丰富的 AI 技能库，覆盖头脑风暴、编码及软件开发生命周期（SDLC）。
*   支持模块化技能组合，允许开发者灵活定制 AI 助手的工作流。
*   基于 Shell 脚本实现，便于集成到现有的终端开发和 CI/CD 环境中。

3. **适用场景**
*   希望利用 AI 深度参与需求分析与架构设计的研发团队。
*   需要标准化 AI 辅助编码流程以提高代码质量的大型项目。
*   探索“智能体驱动开发”新模式的技术先锋团队。
*   希望简化软件开发生命周期中 AI 协作复杂度的开发者。

4. **技术亮点**
*   提出了“obra”等创新概念，系统化地定义 AI 在开发各阶段的行为模式。
*   将抽象的 AI 能力转化为具体的、可复用的技能脚本，增强了可操作性和一致性。
- 链接: https://github.com/obra/superpowers
- ⭐ 239946 | 🍴 21290 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一个能够随用户共同成长并适应需求的智能代理工具。它旨在通过深度集成多种大型语言模型（如 Anthropic 和 OpenAI 的服务），为用户提供强大且灵活的 AI 辅助能力。该项目致力于简化复杂 AI 任务的自动化处理流程。

### 2. 核心功能
*   **多模型集成支持**：兼容 Anthropic (Claude)、OpenAI (GPT) 等多种主流 LLM 后端，提供统一的调用接口。
*   **自适应成长机制**：具备随用户交互数据积累而优化表现的能力，实现个性化智能升级。
*   **代码与任务自动化**：支持复杂的代码生成、调试及日常自动化工作流执行，提升开发效率。
*   **统一代理架构**：封装了不同 AI 服务的差异，让用户无需关心底层模型切换即可使用高级功能。

### 3. 适用场景
*   **高级开发者辅助**：需要跨模型 API 进行复杂代码重构或自动化脚本编写的专业开发人员。
*   **AI 应用原型开发**：希望快速搭建基于多 LLM 后端、具备自适应能力的 AI 代理原型的团队。
*   **个性化任务自动化**：寻求能够随着使用习惯调整行为模式，以处理长期、重复性智力劳动的用户。

### 4. 技术亮点
*   **高社区关注度**：拥有超过 20 万星标，证明其在开源 AI 代理领域具有极高的认可度和活跃度。
*   **广泛的后端兼容性**：标签中包含多个知名 AI 品牌（如 Claude Code, Codex, Moltbot），显示其作为中间件层的广泛适配能力。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 204234 | 🍴 36729 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194256 | 🍴 58880 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能无障碍地使用和构建人工智能，其愿景是提供便捷易用的 AI 工具。通过赋予用户强大的工具支持，该项目旨在帮助用户从繁琐的技术细节中解脱出来，从而将精力集中在真正重要的任务上。

2. **核心功能**
*   **自主智能体架构**：基于大型语言模型（LLM）构建，能够自主规划、执行任务并调用外部工具。
*   **多模型兼容**：支持接入 OpenAI、Claude、Llama 等多种主流大语言模型 API。
*   **互联网与文件交互**：具备浏览网页、读写本地文件及操作其他应用程序的能力。
*   **自我反思与迭代**：能够根据执行结果自动评估错误并进行自我修正，以优化最终输出。

3. **适用场景**
*   **自动化研究助手**：自动搜索网络信息、整理资料并生成综合报告。
*   **内容创作工作流**：辅助进行文案撰写、社交媒体运营或代码生成的全流程自动化。
*   **复杂任务代理**：处理需要多步骤协调的复杂操作，如预订服务、数据迁移或系统维护。

4. **技术亮点**
*   **开源 agentic AI 标杆**：作为“代理式人工智能”领域的先驱项目，拥有极高的社区关注度和活跃度（超 18 万星标）。
*   **高度可扩展性**：模块化设计允许开发者轻松集成新的工具、记忆机制或 AI 模型。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185180 | 🍴 46127 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164431 | 🍴 21288 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163900 | 🍴 30374 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156648 | 🍴 46149 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150130 | 🍴 9355 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146756 | 🍴 23119 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

