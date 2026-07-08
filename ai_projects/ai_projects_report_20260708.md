# GitHub AI项目每日发现报告
日期: 2026-07-08

## 新发布的AI项目

### Homekit
- 描述: Homekit gives any AI agent direct, physical control over Apple Home. Flip lights. Lock doors. Read sensors. Through a single open interface.
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### fox-ai-roundtable
- 1. **中文简介**
该项目允许用户通过本地命令行接口（CLI），将同一提示词同时发送给 Claude、Codex (GPT) 和 Antigravity (Gemini) 三个模型。其核心理念是“一次提问，获取三种答案”，帮助用户快速对比不同大语言模型的输出结果。

2. **核心功能**
*   支持通过本地 CLI 并行调用 Claude、Codex (GPT) 和 Gemini (Antigravity) 三个模型。
*   实现单提示词多模型并发处理，自动收集并展示各模型的独立回复。
*   提供统一的用户界面或交互流程，简化跨平台模型调用的复杂性。
*   旨在促进不同 AI 模型间的直接对比分析，提升 Prompt 优化效率。

3. **适用场景**
*   **Prompt 工程测试**：开发者用于验证同一指令在不同模型上的表现差异，以优化提示词。
*   **多模型内容对比**：研究人员或写作者需要参考多种 AI 视角的文本回答时，可快速获取对比素材。
*   **技术选型评估**：在集成多个 AI 服务前，通过实际用例测试各模型在特定任务上的优劣。

4. **技术亮点**
*   **架构创新**：虽然标记为 HTML，但核心逻辑在于封装了多个主流 AI 模型的本地 CLI 接口，实现了统一的横向调用层。
*   **并行处理机制**：通过异步或非阻塞方式同时发起对三个不同 API/CLI 的请求，显著节省等待时间。
*   **开源透明**：提供轻量级的本地解决方案，无需依赖复杂的云端中间件即可实现多模型聚合。
- 链接: https://github.com/PeterPanSwift/fox-ai-roundtable
- ⭐ 61 | 🍴 9 | 语言: HTML

### blockout
- 1. **中文简介**
Blockout 是一款面向 AI 原生电影制作的预可视化（Previs）工具。它允许用户搭建灰盒场景、编排摄像机运动并为角色设定标记点。最终，它能导出供 Seedance、Veo、Kling 等主流 AI 视频生成模型使用的运动参考包。

2. **核心功能**
*   支持在虚拟环境中快速搭建灰盒（Grey-box）场景以确立空间布局。
*   提供摄像机路径编排及角色动作标记（Marks）的设定功能。
*   能够生成标准化的运动参考数据包，兼容多种 AI 视频生成平台。
*   采用 TypeScript 开发，具备现代化的代码结构和扩展性。

3. **适用场景**
*   AI 电影导演在正式生成前规划镜头语言和场景构图。
*   需要为 Kling 或 Veo 等模型提供精确的运动轨迹控制的专业用户。
*   影视制作团队利用该技术进行低成本、高效率的视觉预演。

4. **技术亮点**
*   针对 AI 视频生成模型优化了运动参考数据的格式，提升了生成内容的可控性。
- 链接: https://github.com/wassermanproductions/blockout
- ⭐ 50 | 🍴 6 | 语言: TypeScript

### seedance-prompt
- **1. 中文简介**
这是一个专为 Seedance 及各类文本生成视频模型设计的 Hermes 技能包，旨在提升提示词的现实感与质量。它通过优化输入指令，帮助用户更精准地控制 AI 视频生成的视觉效果。该项目目前以资源库形式存在，未绑定特定编程语言。

**2. 核心功能**
*   提供针对 Seedance 模型优化的专用提示词模板。
*   增强通用文本转视频模型提示词的真实感细节。
*   集成于 Hermes 技能系统，实现便捷的调用与管理。
*   标准化视频生成指令结构，降低提示词编写门槛。

**3. 适用场景**
*   需要生成高保真、拟真风格短视频的用户。
*   希望利用 Hermes 框架自动化处理视频提示词的工作流开发者。
*   探索 Seedance 模型特性并寻求最佳实践的内容创作者。
*   批量生成视频素材时追求一致性和高质量输出的团队。

**4. 技术亮点**
*   深度适配 Seedance 模型的底层逻辑，而非通用的提示词策略。
*   作为 Hermes 技能模块，具备良好的可扩展性和模块化集成能力。
- 链接: https://github.com/zhouwei713/seedance-prompt
- ⭐ 47 | 🍴 8 | 语言: 未知

### openclaw-voice-call-realtime
- 1. **中文简介**
该项目是一个OpenClaw插件，通过结合Twilio和OpenAI实时API，赋予AI助手拨打真实电话的能力。它支持通话中的工具调用、语音转文字转录以及来电筛选功能。

2. **核心功能**
*   基于Twilio和OpenAI Realtime API实现真实的电话通话连接。
*   支持在通话过程中动态调用外部工具以执行任务。
*   提供实时的语音转文字转录功能，便于记录和分析对话内容。
*   具备来电筛选机制，帮助AI智能判断是否接听或处理特定呼叫。

3. **适用场景**
*   需要自动化处理客户服务热线或预约提醒的智能客服系统。
*   希望AI助手能通过电话直接与人类进行交互式任务处理的个人助理应用。
*   构建具备语音交互能力的企业级自动化工作流，如自动跟进销售线索。

4. **技术亮点**
*   巧妙整合了Twilio的通信基础设施与OpenAI最新的Realtime API低延迟特性。
*   作为OpenClaw生态的一部分，实现了AI代理与真实世界电话网络的无缝对接。
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 31 | 🍴 3 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### trend-viewer
- 描述: 유튜브, 릴스, X, 스레드, 틱톡, AI 뉴스를 한 화면에서 보는 로컬 트렌드 관제판. Python stdlib only.
- 链接: https://github.com/xazingatrend/trend-viewer
- ⭐ 28 | 🍴 14 | 语言: Python
- 标签: instagram, local-server, python, stdlib, tiktok

### kakunin-sdk-typescript
- 描述: Official TypeScript SDK for the Kakunin AI agent compliance API — API client plus certificate enforcement middleware (@kakunin/sdk)
- 链接: https://github.com/nqzai/kakunin-sdk-typescript
- ⭐ 27 | 🍴 27 | 语言: TypeScript
- 标签: agent-security, ai-agent-identity, ai-agents, certificate-authority, compliance

### kakunin-core
- 描述: AI agent compliance platform — X.509 identity via AWS KMS, real-time behavioral risk scoring, auto-revocation, and MiCA / EU AI Act compliance reporting. AGPL-3.0.
- 链接: https://github.com/nqzai/kakunin-core
- ⭐ 25 | 🍴 1 | 语言: TypeScript
- 标签: agent-security-tools, ai-agent-identity, ai-agents-security, ai-governance-tools, audit-log-tools

### lapian-notes
- 描述: 拉片笔记:把电影变成 AI 辅助的拉片笔记 - 本地抽帧/剧情泳道时间轴/结构树/情绪曲线/段落深拆
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 21 | 🍴 5 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### gogh
- 描述: Gogh is a source-cited Obsidian operating brain that turns six frontend design skills into one advisable stack for AI coding agents.
- 链接: https://github.com/AgriciDaniel/gogh
- ⭐ 21 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具包，涵盖了从基础文本清洗、敏感词检测到高级实体抽取和情感分析的各项功能。它不仅提供了丰富的中文专用词典和语料库资源，还集成了多种前沿的深度学习模型应用，旨在降低中文NLP开发的门槛。

**2. 核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、停用词表、分词、词性标注及中文OCR识别等功能。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、人名、地名等特定信息的正则抽取，以及基于BERT等模型的命名实体识别（NER）。
*   **语义与情感分析**：具备词汇情感值计算、同义词/反义词/否定词库、句子相似度匹配及文本情感分类能力。
*   **知识图谱与问答**：集成中文知识图谱构建工具、医疗/金融领域专用数据集，以及基于检索或生成的智能问答系统资源。
*   **预训练模型与应用**：收录了BERT、GPT-2、ALBERT等主流预训练模型的中文版本及相关微调代码，涵盖文本摘要、生成及对话机器人场景。

**3. 适用场景**
*   **内容安全审核**：适用于社交媒体、论坛或新闻平台，利用敏感词库和暴恐词表进行内容合规性自动检测。
*   **智能客服与对话系统**：开发者可利用其中的对话数据集、意图识别模块及QA资源，快速搭建具备上下文理解能力的中文聊天机器人。
*   **金融/医疗行业数据分析**：针对垂直领域，使用内置的行业词库（如财经、医学）和实体抽取模型，从非结构化文本中提取关键信息和知识图谱三元组。
*   **文本挖掘与研究辅助**：适合研究人员和数据科学家，利用其提供的海量NLP数据集、基准测试（Benchmark）及可视化分析工具进行算法验证和趋势研究。

**4. 技术亮点**
该项目并非单一的代码库，而是一个高度聚合的NLP资源枢纽，精选了学术界与工业界（如百度、清华、Facebook等）的最新开源成果，特别是针对中文特性的优化（如全词覆盖BERT、中文拼音处理、中文OCR），极大丰富了中文NLP生态的工具链完整性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81687 | 🍴 15254 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码仓库。它涵盖了从基础算法到前沿应用的广泛内容，为开发者提供了丰富的实战案例。该项目旨在通过具体的代码实现，帮助用户深入理解并掌握人工智能领域的各项技术。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等领域的500多个完整项目实例。
*   所有项目均附带源代码，方便用户直接运行、学习和修改。
*   作为“Awesome”系列资源，对高质量AI项目进行了精选和分类整理。
*   支持Python等主要编程语言，满足多样化的开发需求。
*   适合作为入门学习、技能提升或项目灵感参考的资源库。

3. **适用场景**
*   **初学者学习**：适合想要系统了解AI各子领域概念和实现方式的新手。
*   **项目实战参考**：开发者可借鉴现有代码结构，快速搭建自己的AI应用原型。
*   **技术调研与选型**：研究人员或工程师可通过浏览不同项目，对比技术方案优劣。
*   **教学与培训**：教师或培训师可利用这些真实案例作为课堂练习或作业素材。

4. **技术亮点**
*   **规模庞大且分类清晰**：收录近500个项目，覆盖AI主要分支，便于针对性查找。
*   **代码驱动实践**：强调“with code”，提供可执行的解决方案而非仅理论描述。
*   **社区精选质量**：作为Awesome列表的一部分，通常经过社区筛选，保证项目的相关性和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35269 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的独立工具。它支持多种主流框架和文件格式，帮助用户直观地理解模型结构与数据流向。该项目以轻量级和高兼容性著称，是模型调试与展示的理想选择。

2. **核心功能**
*   支持可视化超过 40 种深度学习模型格式，包括 ONNX、TensorFlow、PyTorch、CoreML 等。
*   提供交互式的网络结构图，允许用户展开、折叠节点并查看层详细信息。
*   支持在桌面端（Electron）、浏览器以及命令行界面中使用，无需安装复杂环境。
*   具备模型结构检查功能，可识别形状不匹配或无效的连接问题。

3. **适用场景**
*   **模型调试**：开发者在训练过程中快速检查模型架构是否正确，定位连接错误。
*   **论文与报告展示**：研究人员利用其生成的清晰图表，辅助撰写论文或制作演示材料。
*   **跨平台模型预览**：工程师在不转换代码的情况下，直接查看不同框架导出的模型文件内容。

4. **技术亮点**
*   **广泛兼容性**：几乎覆盖当前所有主流 ML/DL 框架，统一了可视化入口。
*   **无依赖运行**：作为独立应用分发，用户无需配置 Python 环境或安装庞大的库即可使用。
*   **开源且活跃**：拥有极高的社区关注度（33k+ 星标），持续更新以支持最新模型格式（如 safetensors）。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33196 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，打破平台壁垒。通过统一表示法，开发者可以无缝地在 PyTorch、TensorFlow 和 Keras 等框架间迁移模型。

2. **核心功能**
*   支持多种主流深度学习框架（如 PyTorch、TensorFlow、Keras）模型的相互转换。
*   提供标准化的模型表示格式，确保跨平台和跨硬件的兼容性。
*   包含完整的工具链，用于模型的验证、优化及性能分析。
*   支持从训练到推理的全生命周期管理，加速模型部署流程。

3. **适用场景**
*   需要将 PyTorch 训练的模型部署到不支持原生 PyTorch 的边缘设备或生产环境中。
*   在混合框架环境中工作，需在不同深度学习库之间交换模型权重和结构。
*   希望利用 ONNX Runtime 获得更高性能、更低延迟的模型推理服务。
*   进行跨平台机器学习开发，要求代码和模型具备高度可移植性。

4. **技术亮点**
*   **生态中立性**：由微软、Facebook 等巨头联合发起，拥有广泛的行业支持和社区活跃度。
*   **高性能运行时**：配套的 ONNX Runtime 针对 CPU、GPU 及专用硬件进行了深度优化，显著提升推理速度。
*   **动态形状支持**：能够处理输入维度变化的动态模型，适应更复杂的实际应用场景。
- 链接: https://github.com/onnx/onnx
- ⭐ 21115 | 🍴 3961 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一部全面涵盖大规模模型训练与部署的工程指南。它深入探讨了从硬件选型、网络配置到软件优化的各个环节，旨在帮助开发者构建高效、可扩展的机器学习系统。

2. **核心功能**
*   提供针对大语言模型（LLM）的高效训练策略与调试技巧。
*   详解GPU集群的网络通信优化及存储I/O性能调优方案。
*   介绍分布式训练框架（如PyTorch/DeepSpeed）的最佳实践与故障排查。
*   涵盖模型推理加速、量化技术以及生产环境下的部署架构设计。
*   包含使用Slurm等作业调度系统进行大规模资源管理的实用指南。

3. **适用场景**
*   需要在多节点GPU集群上训练百亿参数级大语言模型的工程师。
*   致力于优化深度学习模型推理延迟并降低计算成本的数据科学家。
*   正在搭建或维护大规模MLOps平台及底层基础设施的运维团队。
*   希望系统学习高性能机器学习工程知识的技术管理人员或研究人员。

4. **技术亮点**
该项目作为“开放书籍”形式，提供了极具实战价值的底层原理剖析和针对极端规模（Exascale）系统的工程级解决方案，填补了理论研究与实际生产部署之间的知识空白。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18263 | 🍴 1159 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11562 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码仓库。它涵盖了从基础算法到前沿应用的广泛内容，为开发者提供了丰富的实战案例。该项目旨在通过具体的代码实现，帮助用户深入理解并掌握人工智能领域的各项技术。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等领域的500多个完整项目实例。
*   所有项目均附带源代码，方便用户直接运行、学习和修改。
*   作为“Awesome”系列资源，对高质量AI项目进行了精选和分类整理。
*   支持Python等主要编程语言，满足多样化的开发需求。
*   适合作为入门学习、技能提升或项目灵感参考的资源库。

3. **适用场景**
*   **初学者学习**：适合想要系统了解AI各子领域概念和实现方式的新手。
*   **项目实战参考**：开发者可借鉴现有代码结构，快速搭建自己的AI应用原型。
*   **技术调研与选型**：研究人员或工程师可通过浏览不同项目，对比技术方案优劣。
*   **教学与培训**：教师或培训师可利用这些真实案例作为课堂练习或作业素材。

4. **技术亮点**
*   **规模庞大且分类清晰**：收录近500个项目，覆盖AI主要分支，便于针对性查找。
*   **代码驱动实践**：强调“with code”，提供可执行的解决方案而非仅理论描述。
*   **社区精选质量**：作为Awesome列表的一部分，通常经过社区筛选，保证项目的相关性和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35269 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的独立工具。它支持多种主流框架和文件格式，帮助用户直观地理解模型结构与数据流向。该项目以轻量级和高兼容性著称，是模型调试与展示的理想选择。

2. **核心功能**
*   支持可视化超过 40 种深度学习模型格式，包括 ONNX、TensorFlow、PyTorch、CoreML 等。
*   提供交互式的网络结构图，允许用户展开、折叠节点并查看层详细信息。
*   支持在桌面端（Electron）、浏览器以及命令行界面中使用，无需安装复杂环境。
*   具备模型结构检查功能，可识别形状不匹配或无效的连接问题。

3. **适用场景**
*   **模型调试**：开发者在训练过程中快速检查模型架构是否正确，定位连接错误。
*   **论文与报告展示**：研究人员利用其生成的清晰图表，辅助撰写论文或制作演示材料。
*   **跨平台模型预览**：工程师在不转换代码的情况下，直接查看不同框架导出的模型文件内容。

4. **技术亮点**
*   **广泛兼容性**：几乎覆盖当前所有主流 ML/DL 框架，统一了可视化入口。
*   **无依赖运行**：作为独立应用分发，用户无需配置 Python 环境或安装庞大的库即可使用。
*   **开源且活跃**：拥有极高的社区关注度（33k+ 星标），持续更新以支持最新模型格式（如 safetensors）。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33196 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 项目名称：cheatsheets-ai

#### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了一套 essentials（基础/必备）速查表。它汇集了人工智能、机器学习及相关数据处理工具的核心概念与语法参考，旨在帮助开发者快速回顾关键知识点。

#### 2. 核心功能
*   **深度学习框架速查**：涵盖 Keras 等主流深度学习框架的核心 API 和用法指南。
*   **数值计算与科学库参考**：提供 NumPy 和 SciPy 等用于高性能计算的 Python 库的关键函数摘要。
*   **数据可视化指引**：整理 Matplotlib 绘图库的常用图表类型及配置参数，便于快速生成可视化结果。
*   **AI 领域知识汇总**：整合了机器学习与深度学习中的关键算法概念和最佳实践备忘。

#### 3. 适用场景
*   **面试准备**：求职者用于快速复习机器学习、深度学习及 Python 数据科学生态系统的核心概念。
*   **日常开发查阅**：研究人员或工程师在编码时快速检索特定库（如 NumPy, Matplotlib）的语法细节。
*   **新手入门引导**：初学者作为学习路线图，快速了解 AI 领域所需掌握的主要工具和技能点。

#### 4. 技术亮点
*   **全面覆盖主流工具栈**：集中整理了 AI 开发中最常用的 Python 库（Keras, Numpy, Scipy, Matplotlib），实现一站式参考。
*   **极简主义设计**：以“速查表”形式呈现，去除了冗长的理论解释，专注于代码片段和关键参数，提升查阅效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，帮助零基础用户快速入门并具备就业实战能力。内容涵盖 Python、数学基础、机器学习、深度学习、计算机视觉及自然语言处理等热门领域。

### 2. 核心功能
*   提供结构化的AI学习路径，涵盖从编程基础到高级算法的完整知识体系。
*   收录近200个精选实战案例和项目，强调动手实践以增强就业竞争力。
*   免费提供配套的学习教材和资源，降低入门门槛。
*   覆盖主流框架与工具，如 PyTorch、TensorFlow、Keras、Pandas、NumPy 等。
*   整合多学科知识，包括数学基础、数据分析、数据挖掘及可视化技术。

### 3. 适用场景
*   **零基础转行**：希望进入人工智能或数据科学领域的初学者系统学习。
*   **求职准备**：需要丰富实战项目经验以提升简历竞争力的求职者。
*   **技能补全**：已有一定基础但希望系统化梳理机器学习、深度学习等特定领域知识的开发者。
*   **教学参考**：教师或培训讲师寻找结构化课程内容和实战案例作为教学辅助。

### 4. 技术亮点
*   **资源集中化**：将分散的AI学习资源（代码、论文、教程）整合为一条清晰的学习路线。
*   **实战导向**：注重通过大量真实案例（近200个）来巩固理论知识，而非纯理论堆砌。
*   **生态全覆盖**：同时支持 TensorFlow/Keras 和 PyTorch 两大主流深度学习框架，适应不同技术偏好。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 以下是针对 GitHub 项目 **Ludwig** 的技术分析报告：

1. **中文简介**
   Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它通过声明式配置实现数据驱动的开发流程，让用户无需编写大量底层代码即可快速训练和部署机器学习模型。

2. **核心功能**
   - 支持基于声明式 YAML 配置文件快速构建和训练深度学习模型，大幅降低开发门槛。
   - 内置多种预处理和后处理组件，能够自动处理表格、文本、图像等多种数据类型。
   - 兼容主流深度学习框架（如 PyTorch），并提供端到端的模型训练与评估流水线。
   - 支持大规模分布式训练，优化了在 GPU 集群上的资源利用率和训练效率。
   - 提供可视化的结果分析和模型解释工具，帮助开发者理解模型行为及特征重要性。

3. **适用场景**
   - 需要快速原型化验证想法，且不愿深入编写复杂训练循环的数据科学团队。
   - 构建基于结构化数据（表格）或混合模态（文本+图像）的预测性分析应用。
   - 对现有预训练模型进行微调（Fine-tuning），以适应特定垂直领域的业务需求。
   - 希望在不牺牲性能的前提下，减少机器学习工程中的样板代码和维护成本。

4. **技术亮点**
   - **数据中心化设计**：强调数据质量对模型性能的影响，内置强大的数据清洗和增强功能。
   - **即插即用架构**：模块化的组件设计使得添加新的层、损失函数或评估指标变得极其简单。
   - **统一接口**：为传统机器学习（如线性回归、随机森林）和深度学习提供了统一的 API 接口。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8919 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6233 | 🍴 738 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具包，涵盖了从基础文本清洗、敏感词检测到高级实体抽取和情感分析的各项功能。它不仅提供了丰富的中文专用词典和语料库资源，还集成了多种前沿的深度学习模型应用，旨在降低中文NLP开发的门槛。

**2. 核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、停用词表、分词、词性标注及中文OCR识别等功能。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、人名、地名等特定信息的正则抽取，以及基于BERT等模型的命名实体识别（NER）。
*   **语义与情感分析**：具备词汇情感值计算、同义词/反义词/否定词库、句子相似度匹配及文本情感分类能力。
*   **知识图谱与问答**：集成中文知识图谱构建工具、医疗/金融领域专用数据集，以及基于检索或生成的智能问答系统资源。
*   **预训练模型与应用**：收录了BERT、GPT-2、ALBERT等主流预训练模型的中文版本及相关微调代码，涵盖文本摘要、生成及对话机器人场景。

**3. 适用场景**
*   **内容安全审核**：适用于社交媒体、论坛或新闻平台，利用敏感词库和暴恐词表进行内容合规性自动检测。
*   **智能客服与对话系统**：开发者可利用其中的对话数据集、意图识别模块及QA资源，快速搭建具备上下文理解能力的中文聊天机器人。
*   **金融/医疗行业数据分析**：针对垂直领域，使用内置的行业词库（如财经、医学）和实体抽取模型，从非结构化文本中提取关键信息和知识图谱三元组。
*   **文本挖掘与研究辅助**：适合研究人员和数据科学家，利用其提供的海量NLP数据集、基准测试（Benchmark）及可视化分析工具进行算法验证和趋势研究。

**4. 技术亮点**
该项目并非单一的代码库，而是一个高度聚合的NLP资源枢纽，精选了学术界与工业界（如百度、清华、Facebook等）的最新开源成果，特别是针对中文特性的优化（如全词覆盖BERT、中文拼音处理、中文OCR），极大丰富了中文NLP生态的工具链完整性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81687 | 🍴 15254 | 语言: Python

### LlamaFactory
- ### 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目荣获 ACL 2024 会议认可，旨在简化从预训练到指令微调的全流程开发体验。它集成了多种先进的参数高效微调技术和量化策略，极大降低了大模型适配的门槛。

### 2. **核心功能**
*   **广泛模型支持**：无缝兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种流行大模型及视觉模型。
*   **全阶段微调能力**：提供预训练、监督微调、奖励模型训练至强化学习（RLHF/DPO）的一站式全流程支持。
*   **高效微调技术集成**：内置 LoRA、QLoRA、P-Tuning 等多种参数高效微调方法，显著降低显存占用。
*   **多模态与 Agent 支持**：不仅支持纯文本任务，还具备处理视觉信息的能力，并集成了智能体（Agent）开发相关功能。
*   **易用性配置**：提供标准化的 YAML 配置文件和命令行接口，无需修改底层代码即可快速启动实验。

### 3. **适用场景**
*   **企业私有化部署优化**：基于开源大模型（如 Qwen、Llama），利用少量行业数据通过 LoRA/QLoRA 进行低成本指令微调。
*   **多模态应用开发**：需要同时处理文本和图像输入的复杂任务（如图文理解、视觉问答）的快速原型构建。
*   **对齐与偏好优化**：通过 DPO 或 RLHF 技术对模型输出进行人类偏好对齐，提升回答的安全性与有用性。
*   **科研与学术实验**：研究人员在 ACL 等顶级会议认可的框架下，快速复现或对比不同微调算法（如 MoE、量化策略）的效果。

### 4. **技术亮点**
*   **极致轻量化**：原生支持 QLoRA 和 4-bit/8-bit 量化技术，使得在消费级显卡上微调千亿参数模型成为可能。
*   **统一架构设计**：解决了不同模型框架（Transformers, vLLM 等）之间的兼容性痛点，实现了“一个框架跑遍所有模型”。
*   **高性能推理集成**：深度集成 vLLM 推理引擎，在训练和评估阶段均能提供极高的吞吐量。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73085 | 🍴 8932 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目提取并汇总了来自Anthropic（Claude系列）、OpenAI（ChatGPT及Codex系列）、Google（Gemini系列）以及xAI等多家人工智能巨头的大语言模型系统提示词（System Prompts）。内容涵盖Claude Fable 5、Opus 4.8、Grok、Cursor等知名模型，并保持定期更新。这是一个致力于收集开源AI模型底层指令集的权威资源库。

2. **核心功能**
*   **多厂商提示词收集**：整合了Anthropic、OpenAI、Google及xAI等多家主流AI公司的系统提示词。
*   **涵盖广泛模型**：包括Claude、GPT、Gemini、Grok、Cursor、VS Code Copilot等多种知名模型和工具。
*   **持续动态更新**：随着新模型发布，项目会及时收录最新的系统提示词数据。
*   **开源共享资源**：以JavaScript格式公开所有提取的提示词，便于开发者直接查阅和使用。

3. **适用场景**
*   **提示词工程研究**：帮助研究人员分析不同大模型的系统指令结构，优化Prompt设计策略。
*   **AI安全与红队测试**：用于识别模型潜在的安全边界和指令漏洞，进行对抗性测试。
*   **开发调试参考**：开发者可参考官方系统提示词，更好地理解和调整自定义Agent的行为逻辑。
*   **教育学习**：作为教学案例，帮助学习者理解大型语言模型背后的指令机制和工作原理。

4. **技术亮点**
*   **跨平台覆盖全面**：几乎囊括了当前市场上最顶尖的商业闭源模型提示词，具有极高的稀缺性和参考价值。
*   **社区驱动维护**：凭借高星数和定期更新，形成了活跃的开源社区支持，确保数据的时效性。
*   **结构化数据呈现**：将非结构化的自然语言指令转化为代码友好的格式，降低了分析和复用的门槛。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 53969 | 🍴 8791 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51914 | 🍴 10483 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战及深度学习的综合性资源库，内容深入讲解线性代数、PyTorch和TensorFlow 2等核心工具。它集成了NLTK自然语言处理库与scikit-learn算法库，旨在通过代码实践帮助开发者掌握从基础理论到高级应用的完整技能树。

2. **核心功能**
*   提供基于Python的数据分析与机器学习算法实战代码。
*   包含线性代数基础理论与PyTorch/TensorFlow 2深度学习框架的应用示例。
*   集成NLTK进行自然语言处理（NLP）及相关文本挖掘任务。
*   实现多种经典算法如SVM、KMeans、Logistic回归及AdaBoost等。

3. **适用场景**
*   机器学习初学者系统性地学习算法原理与代码实现。
*   数据科学家在项目中快速查找和复用经典的预处理或建模代码片段。
*   高校学生或研究人员用于辅助理解线性代数在AI中的数学应用。

4. **技术亮点**
*   全面覆盖从传统统计学习（如Apriori、FP-Growth）到现代深度学习（DNN、RNN、LSTM）的技术栈。
*   结合数学基础（线性代数、PCA、SVD）与工程实践，强调理论与实践的深度结合。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37644 | 🍴 6273 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35269 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33724 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28420 | 🍴 3454 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25848 | 🍴 2902 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码仓库。它涵盖了从基础算法到前沿应用的广泛内容，为开发者提供了丰富的实战案例。该项目旨在通过具体的代码实现，帮助用户深入理解并掌握人工智能领域的各项技术。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等领域的500多个完整项目实例。
*   所有项目均附带源代码，方便用户直接运行、学习和修改。
*   作为“Awesome”系列资源，对高质量AI项目进行了精选和分类整理。
*   支持Python等主要编程语言，满足多样化的开发需求。
*   适合作为入门学习、技能提升或项目灵感参考的资源库。

3. **适用场景**
*   **初学者学习**：适合想要系统了解AI各子领域概念和实现方式的新手。
*   **项目实战参考**：开发者可借鉴现有代码结构，快速搭建自己的AI应用原型。
*   **技术调研与选型**：研究人员或工程师可通过浏览不同项目，对比技术方案优劣。
*   **教学与培训**：教师或培训师可利用这些真实案例作为课堂练习或作业素材。

4. **技术亮点**
*   **规模庞大且分类清晰**：收录近500个项目，覆盖AI主要分支，便于针对性查找。
*   **代码驱动实践**：强调“with code”，提供可执行的解决方案而非仅理论描述。
*   **社区精选质量**：作为Awesome列表的一部分，通常经过社区筛选，保证项目的相关性和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35269 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22155 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16243 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12905 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11270 | 🍴 1195 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 877 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3277 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2624 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2415 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382195 | 🍴 80194 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 249682 | 🍴 22152 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211501 | 🍴 38862 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195690 | 🍴 59172 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185434 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165091 | 🍴 21366 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164046 | 🍴 30399 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156893 | 🍴 46166 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151368 | 🍴 9471 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148203 | 🍴 23350 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

