# GitHub AI项目每日发现报告
日期: 2026-07-23

## 新发布的AI项目

### official-document-ai-assistant
- ### 1. 中文简介
该项目是一款基于本地部署的桌面助手，专为官方文档的处理而设计。它具备自动审查、格式修复以及合规导出的核心能力，旨在提升公文处理的效率与规范性。

### 2. 核心功能
*   **本地化文档审查**：在本地环境中对官方文档进行内容审核，确保数据隐私与安全。
*   **智能格式修复**：自动检测并修正文档中的排版错误，使其符合标准公文格式。
*   **合规性导出**：支持生成符合特定规范要求的最终文档版本，便于存档或发布。
*   **桌面端交互体验**：提供直观的图形界面，降低用户操作门槛，实现一站式文档处理。

### 3. 适用场景
*   **政府机关及事业单位**：用于内部公文、报告及通知的规范化制作与审核。
*   **大型企业行政部**：处理公司内部正式文件，确保格式统一且符合企业合规要求。
*   **法律或合规部门**：快速检查合同或政策文件的格式一致性，减少人工校对成本。

### 4. 技术亮点
*   **隐私安全优先**：采用本地运行架构，无需上传数据至云端，有效保护敏感公文信息。
*   **自动化工作流**：集成AI辅助的格式修复与审查逻辑，显著减少重复性手动编辑工作。
- 链接: https://github.com/NextWeb4/official-document-ai-assistant
- ⭐ 155 | 🍴 0 | 语言: Python

### Finn-loop
- 1. **中文简介**
Finn-loop 是一个基于 Claude Code 的三技能 AI 软件工厂，涵盖规范制定、代码构建与审查三个环节。该工具通过自动化工作流处理大部分开发任务，而最终的合并决策权仍保留在人类手中。

2. **核心功能**
- 提供集规范定义、代码生成和代码审查于一体的三阶段自动化流程。
- 深度集成 Claude Code，利用其强大的语言模型能力驱动软件开发。
- 实现“AI 执行 + 人类合并”的人机协作模式，确保代码质量与安全可控。
- 支持 agentic workflows（智能体工作流），自动协调多个 AI 代理完成复杂任务。

3. **适用场景**
- 希望利用 AI 加速日常编码任务并减少重复性审查工作的开发团队。
- 需要标准化软件开发生命周期（从需求到上线）的企业级应用项目。
- 探索 AI 辅助编程（AI-Augmented Programming）最佳实践的早期采用者。

4. **技术亮点**
- 创新性地结合了 Linear 等项目管理工具与 GitHub 工作流，实现了从任务追踪到代码部署的全链路闭环。
- 链接: https://github.com/finna/Finn-loop
- ⭐ 149 | 🍴 19 | 语言: JavaScript
- 标签: agentic-workflows, ai-agents, claude-code, github, linear

### open-ai-canvas
- 1. **中文简介**
Open-ai-canvas 是一款专为 AI 影视创作设计的开源无限画布工作台。它集成了多模态内容生成、分镜编排、素材管理以及 Agent 自动化工作流，旨在提升影视制作效率。该项目基于 TypeScript 开发，为创作者提供了一站式的视觉化协作环境。

2. **核心功能**
*   支持文本、图像等多模态内容的 AI 生成与编辑。
*   提供可视化的无限画布，便于进行分镜头脚本的编排与布局。
*   内置高效的素材管理系统，方便资源归类与调用。
*   集成 Agent 工作流引擎，实现自动化任务处理与流程编排。
*   基于 TypeScript 构建，确保代码的可维护性与扩展性。

3. **适用场景**
*   AI 辅助的电影或短片分镜脚本设计与可视化预演。
*   多模态创意内容的快速原型制作与迭代测试。
*   需要复杂工作流自动化的影视后期制作管线搭建。
*   团队协作中的素材集中管理与版本控制。

4. **技术亮点**
*   采用“无限画布”交互模式，突破传统线性编辑限制，提供更自由的创作空间。
*   深度整合 Agent 技术，将分散的 AI 工具串联成可复用的自动化工作流。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 77 | 🍴 20 | 语言: TypeScript

### podcast-shorts-factory
- 1. **中文简介**
该项目是一个由十个协作AI智能体组成的自动化系统，能够将长播客内容自动转换为短视频格式。它完全免费且开源，支持在免费的AI服务提供商上运行，实现了从音频处理到视频生成的全流程自动化。

2. **核心功能**
- 利用AI智能体集群自动化执行长音频转短视频的完整工作流。
- 集成Whisper和LLM技术进行语音识别、脚本提取及内容摘要生成。
- 通过FFmpeg实现高效的音视频剪辑、字幕合成与视频渲染。
- 支持无头频道（Faceless Channel）模式，无需真人出镜即可产出内容。
- 兼容免费AI接口，降低用户的使用成本和技术门槛。

3. **适用场景**
- 播客创作者快速将长篇音频节目转化为适合YouTube Shorts或TikTok传播的碎片化视频。
- 社交媒体运营者批量生产“无脸”知识类或娱乐类短视频以获取流量。
- 内容营销团队自动化制作多平台适配的短视频素材，提高内容分发效率。

4. **技术亮点**
- 采用多智能体协作架构，将复杂的视频生成任务拆解为多个独立且协同的AI步骤。
- 全链路免费开源方案，结合Whisper高精度转录与大语言模型的内容理解能力，无需付费API即可运行。
- 链接: https://github.com/krakonjac300-pixel/podcast-shorts-factory
- ⭐ 48 | 🍴 22 | 语言: Python
- 标签: ai-agents, content-automation, faceless-channel, ffmpeg, llm

### esp32-ai
- 1. **中文简介**
该项目是一个针对ESP32微控制器的AI解决方案。由于缺乏详细的项目描述和标签，其具体实现细节尚不明确。目前仅知其为Python语言编写且有一定社区关注度。

2. **核心功能**
*   提供在ESP32平台上运行人工智能模型的基础支持。
*   可能包含将机器学习算法移植到资源受限设备的工具或库。
*   利用Python进行开发或配置，简化嵌入式AI应用的构建流程。
*   旨在扩展ESP32的功能，使其具备基本的边缘计算能力。

3. **适用场景**
*   需要在低功耗物联网设备上进行实时数据处理的边缘计算项目。
*   开发基于ESP32的智能传感器，用于简单的模式识别或异常检测。
*   教育用途，用于演示如何在微控制器上部署轻量级AI模型。
*   原型开发阶段，快速验证AI算法在硬件上的可行性。

4. **技术亮点**
*   暂无明确的技术亮点信息，因项目描述缺失。
- 链接: https://github.com/slvDev/esp32-ai
- ⭐ 29 | 🍴 2 | 语言: Python

### handoff-skill
- 描述: Claude skill: turn your current conversation into a complete handoff document so any LLM can pick up exactly where you left off
- 链接: https://github.com/ToolMonsters/handoff-skill
- ⭐ 27 | 🍴 10 | 语言: 未知
- 标签: ai, claude, claude-code, claude-skills, llm

### VinvAI
- 描述: Your agent says it's done. Vinv says prove it. Real traces + live code graph + closed-loop verify, served to your agent over MCP.
- 链接: https://github.com/VinvAI/VinvAI
- ⭐ 19 | 🍴 0 | 语言: Python
- 标签: ai-agents, code-graph, coding-agent, developer-tools, fault-localization

### memory-forest
- 描述: A verifiable local memory architecture for long-running AI agents
- 链接: https://github.com/hyungchulc/memory-forest
- ⭐ 17 | 🍴 3 | 语言: Python
- 标签: agent-memory, ai-agents, knowledge-management, local-first, markdown

### moonsconfig
- 描述: Open travel OS with Maya AI for calls, support chat, RFQs, vendor outreach, itinerary curation, route maps, packages, hotels, cars, CRM, bookings, and multi-tenant SaaS.
- 链接: https://github.com/schowdary75/moonsconfig
- ⭐ 16 | 🍴 2 | 语言: TypeScript
- 标签: ai-agent, asterisk, booking, customer-support, express

### capcut-pro-fullfree
- 描述: CapCut Pro Professional – Advanced video editing software with powerful AI tools, extensive effects library, and high-quality export for content creators.
- 链接: https://github.com/intersectflowhut/capcut-pro-fullfree
- ⭐ 16 | 🍴 0 | 语言: 未知
- 标签: 4k-video, ai-captions, ai-video-editor, background-removal, cinematic-editing

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、语言识别、实体抽取（如手机号、身份证）及多种语言工具。该项目汇集了丰富的中文词库、预训练模型、数据集以及相关的技术报告和开源项目，旨在为开发者提供一站式的 NLP 解决方案与参考资料。

2. **核心功能**
- **基础 NLP 工具**：提供敏感词过滤、繁简体转换、中英文分词、词性标注及情感分析等功能。
- **丰富语料与词库**：包含大量专业领域词库（如汽车、医疗、法律）、人名库、地名库及古诗词等中文特有资源。
- **深度学习模型资源**：整合了 BERT、GPT2、ALBERT 等主流预训练模型的训练代码、微调示例及应用案例。
- **数据增强与处理**：提供 EDA 数据增强工具、文本纠错、OCR 识别及语音转写等数据处理辅助工具。
- **知识图谱与问答**：收录了多个中文知识图谱构建方法、QA 数据集及基于图谱的问答系统实现。

3. **适用场景**
- **中文 NLP 初学者学习**：适合希望快速了解中文 NLP 生态、获取高质量数据集和基准测试资源的开发人员。
- **企业内容风控系统**：利用其敏感词库、暴恐词表及反动词表，构建高效的内容审核与舆情监控系统。
- **垂直领域智能客服/问答开发**：借助医疗、法律、金融等领域的专用词库和预训练模型，快速搭建行业垂直领域的对话机器人或信息抽取系统。
- **学术研究与技术调研**：研究人员可通过该项目获取最新的 NLP 论文复现代码、竞赛方案及技术综述报告。

4. **技术亮点**
- **资源极度聚合**：不仅是单一工具库，更是集数据集、预训练模型、代码实现和技术文档于一体的综合性 GitHub 导航站。
- **侧重中文特性优化**：特别针对中文特有的挑战（如分词、姓名识别、繁简转换、拼音标注）提供了大量专用工具和词典。
- **紧跟前沿技术**：持续更新并收录了包括 BERT、Transformer、Knowledge Graph 在内的最新深度学习 NLP 技术实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81991 | 🍴 15254 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码资源库。该项目通过提供完整的代码示例，为开发者构建了一个涵盖多领域的人工智能学习与实践指南。它旨在帮助技术人员快速掌握各类主流算法并应用于实际开发中。

**2. 核心功能**
- 收录500个完整的人工智能相关项目代码，覆盖机器学习至深度学习的广泛领域。
- 集成计算机视觉与自然语言处理（NLP）等前沿技术的实战案例。
- 提供结构化的项目列表，便于用户按技术领域分类查找和下载。
- 作为“Awesome”系列资源，筛选高质量项目，降低学习门槛。

**3. 适用场景**
- AI初学者系统学习机器学习与深度学习基础算法的实战演练。
- 开发人员寻找计算机视觉或NLP具体应用场景的代码参考模板。
- 研究人员或工程师快速获取特定AI任务的实现方案以加速原型开发。

**4. 技术亮点**
- 项目规模庞大且分类清晰，全面覆盖当前主流AI子领域。
- 强调“带代码”的实操性，所有项目均附带可运行的源代码。
- 标签体系完善，便于通过Python、数据科学等技术栈进行精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35646 | 🍴 7372 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和文件格式，能够直观地展示模型结构和数据流向。

2. **核心功能**
- 支持读取并可视化 Keras、PyTorch、TensorFlow、ONNX 等广泛使用的模型格式。
- 提供清晰的图形化界面，展示层结构、参数及张量形状，便于调试和理解。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定优化格式。
- 支持在浏览器中直接打开模型文件，无需安装复杂环境即可预览。

3. **适用场景**
- 研究人员和开发者用于快速检查模型架构是否正确，排查结构错误。
- 工程师在部署前验证转换后的模型（如从 PyTorch 转为 ONNX 或 TFLite）是否保留原意。
- 非技术人员通过可视化的方式向团队或客户展示 AI 模型的内部逻辑。

4. **技术亮点**
- 基于 JavaScript 构建，实现了轻量级、跨平台且无需后端服务的纯前端可视化体验。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33256 | 🍴 3168 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，打破生态壁垒。通过统一格式，开发者可以更灵活地在各种硬件和软件平台上运行AI模型。

2. **核心功能**
- 提供标准化的模型格式，支持从训练框架到推理引擎的无缝迁移。
- 实现跨平台兼容性，允许在不同硬件加速器上高效执行计算图。
- 拥有丰富的工具生态系统，便于模型的验证、优化和转换。
- 支持主流深度学习框架（如PyTorch、TensorFlow、Keras等）的集成。

3. **适用场景**
- 将PyTorch或TensorFlow训练好的模型转换为通用格式以便在生产环境部署。
- 在边缘设备或特定硬件加速器上优化和加速深度学习模型的推理性能。
- 在不同开发团队或公司间共享预训练模型，确保格式兼容性和可复现性。

4. **技术亮点**
- 作为行业通用的开放标准，被微软、Facebook、Amazon等科技巨头广泛支持，具有极强的社区活力和生态系统兼容性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21206 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18460 | 🍴 1178 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17333 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13169 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11594 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10673 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码资源库。该项目通过提供完整的代码示例，为开发者构建了一个涵盖多领域的人工智能学习与实践指南。它旨在帮助技术人员快速掌握各类主流算法并应用于实际开发中。

**2. 核心功能**
- 收录500个完整的人工智能相关项目代码，覆盖机器学习至深度学习的广泛领域。
- 集成计算机视觉与自然语言处理（NLP）等前沿技术的实战案例。
- 提供结构化的项目列表，便于用户按技术领域分类查找和下载。
- 作为“Awesome”系列资源，筛选高质量项目，降低学习门槛。

**3. 适用场景**
- AI初学者系统学习机器学习与深度学习基础算法的实战演练。
- 开发人员寻找计算机视觉或NLP具体应用场景的代码参考模板。
- 研究人员或工程师快速获取特定AI任务的实现方案以加速原型开发。

**4. 技术亮点**
- 项目规模庞大且分类清晰，全面覆盖当前主流AI子领域。
- 强调“带代码”的实操性，所有项目均附带可运行的源代码。
- 标签体系完善，便于通过Python、数据科学等技术栈进行精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35646 | 🍴 7372 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和文件格式，能够直观地展示模型结构和数据流向。

2. **核心功能**
- 支持读取并可视化 Keras、PyTorch、TensorFlow、ONNX 等广泛使用的模型格式。
- 提供清晰的图形化界面，展示层结构、参数及张量形状，便于调试和理解。
- 兼容 CoreML、TensorFlow Lite 和 Safetensors 等移动端或特定优化格式。
- 支持在浏览器中直接打开模型文件，无需安装复杂环境即可预览。

3. **适用场景**
- 研究人员和开发者用于快速检查模型架构是否正确，排查结构错误。
- 工程师在部署前验证转换后的模型（如从 PyTorch 转为 ONNX 或 TFLite）是否保留原意。
- 非技术人员通过可视化的方式向团队或客户展示 AI 模型的内部逻辑。

4. **技术亮点**
- 基于 JavaScript 构建，实现了轻量级、跨平台且无需后端服务的纯前端可视化体验。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33256 | 🍴 3168 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心知识速查表（Cheat Sheets）。它涵盖了从基础数学工具到高级框架使用的关键概念，旨在帮助研究者快速回顾和查阅重要知识点。内容源自 Medium 上的专业文章整理，具有高度的实用性和参考性。

2. **核心功能**
- 提供机器学习和深度学习领域的关键公式、定义及算法速查。
- 涵盖常用 Python 科学计算库（如 NumPy, SciPy, Matplotlib）的快捷操作指南。
- 包含深度学习框架（如 Keras）的核心用法和配置参数参考。
- 整理人工智能相关术语和概念，便于快速检索和理解。
- 以简洁的图文形式呈现复杂技术细节，提升学习和问题排查效率。

3. **适用场景**
- 研究人员在撰写论文或实验时，快速回顾特定算法或数学公式。
- 开发者在日常编码过程中，查阅 NumPy、Matplotlib 等库的常用函数用法。
- 初学者系统性地梳理机器学习核心概念和技术栈，建立知识框架。
- 团队内部进行技术分享或新人入职培训时作为辅助参考资料。

4. **技术亮点**
- 内容高度浓缩，将复杂的 AI/ML 技术要点提炼为易读的速查卡片。
- 覆盖范围广，横跨数学基础、数据可视化、主流框架及核心算法。
- 社区认可度高（逾 1.5 万星标），经过大量开发者验证，可靠性强。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，整合了Python、数学、机器学习及深度学习等近200个实战案例与项目。它提供免费的配套教材，旨在帮助零基础用户系统入门并掌握就业所需的实战技能。

2. **核心功能**
- 提供涵盖AI全领域的系统化学习路径与知识体系。
- 收录近200个精选实战案例以强化动手能力。
- 免费提供配套学习资料，降低入门门槛。
- 覆盖从基础编程到高级算法的多层次技术栈。

3. **适用场景**
- AI初学者希望从零开始建立完整知识框架。
- 求职者需要通过实战项目提升简历竞争力。
- 技术人员想要快速查阅特定AI领域（如NLP、CV）的资源索引。

4. **技术亮点**
- 资源高度聚合，一站式解决多领域（PyTorch/TensorFlow等）学习材料获取难题。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13169 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置，让开发者能够专注于数据而非底层工程细节，从而高效地进行模型训练与微调。

2. **核心功能**
*   **低代码/声明式建模**：通过 YAML 配置文件定义模型架构和数据管道，无需编写复杂的深度学习代码即可快速搭建原型。
*   **广泛的模型支持**：原生支持从传统机器学习算法到基于 PyTorch 的深度神经网络，以及 LLM 的微调（如 Llama、Mistral 等）。
*   **数据为中心的工作流**：强调数据处理和特征工程，内置多种预处理模块，方便处理表格、文本、图像等多种数据类型。
*   **开箱即用的训练与评估**：提供标准化的训练流程、超参数调整工具及详细的性能评估报告，降低实验门槛。

3. **适用场景**
*   **快速原型开发**：数据科学家希望在不深入掌握深度学习框架底层细节的情况下，迅速验证不同模型架构的效果。
*   **LLM 微调与应用**：需要对开源大语言模型（如 Llama 2、Mistral）进行领域适配或特定任务微调的低代码需求场景。
*   **多模态数据分析**：需要同时处理结构化表格数据与非结构化数据（如文本、图像）的综合型 AI 项目。

4. **技术亮点**
*   **统一接口**：在同一框架内无缝切换传统机器学习与深度学习模型，简化了技术栈的复杂性。
*   **生态兼容性**：基于 PyTorch 构建，并良好兼容主流 Hugging Face 模型库，便于集成最新的 NLP 和 CV 技术。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9146 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8938 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6994 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6269 | 🍴 751 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、语言识别、实体抽取（如手机号、身份证）及多种语言工具。该项目汇集了丰富的中文词库、预训练模型、数据集以及相关的技术报告和开源项目，旨在为开发者提供一站式的 NLP 解决方案与参考资料。

2. **核心功能**
- **基础 NLP 工具**：提供敏感词过滤、繁简体转换、中英文分词、词性标注及情感分析等功能。
- **丰富语料与词库**：包含大量专业领域词库（如汽车、医疗、法律）、人名库、地名库及古诗词等中文特有资源。
- **深度学习模型资源**：整合了 BERT、GPT2、ALBERT 等主流预训练模型的训练代码、微调示例及应用案例。
- **数据增强与处理**：提供 EDA 数据增强工具、文本纠错、OCR 识别及语音转写等数据处理辅助工具。
- **知识图谱与问答**：收录了多个中文知识图谱构建方法、QA 数据集及基于图谱的问答系统实现。

3. **适用场景**
- **中文 NLP 初学者学习**：适合希望快速了解中文 NLP 生态、获取高质量数据集和基准测试资源的开发人员。
- **企业内容风控系统**：利用其敏感词库、暴恐词表及反动词表，构建高效的内容审核与舆情监控系统。
- **垂直领域智能客服/问答开发**：借助医疗、法律、金融等领域的专用词库和预训练模型，快速搭建行业垂直领域的对话机器人或信息抽取系统。
- **学术研究与技术调研**：研究人员可通过该项目获取最新的 NLP 论文复现代码、竞赛方案及技术综述报告。

4. **技术亮点**
- **资源极度聚合**：不仅是单一工具库，更是集数据集、预训练模型、代码实现和技术文档于一体的综合性 GitHub 导航站。
- **侧重中文特性优化**：特别针对中文特有的挑战（如分词、姓名识别、繁简转换、拼音标注）提供了大量专用工具和词典。
- **紧跟前沿技术**：持续更新并收录了包括 BERT、Transformer、Knowledge Graph 在内的最新深度学习 NLP 技术实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81991 | 🍴 15254 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目旨在简化指令微调、RLHF 及量化训练流程，相关技术成果已发表于 ACL 2024 会议。

**2. 核心功能**
*   支持上百种主流 LLM 和 VLM 的统一高效微调。
*   集成 LoRA、QLoRA 等参数高效微调（PEFT）技术及多种量化方案。
*   提供完整的 RLHF（基于人类反馈的强化学习）训练支持。
*   兼容 Transformers 库，实现便捷的指令微调与模型部署。

**3. 适用场景**
*   研究人员需对多种不同架构的大模型进行快速基准测试与对比实验。
*   开发者希望利用有限算力，通过 QLoRA 等技术低成本微调大模型。
*   团队需要构建具备对齐能力（如遵循指令或价值观对齐）的垂直领域模型。

**4. 技术亮点**
*   **多模态支持**：不仅限于文本模型，还全面支持视觉语言模型（VLM）的微调。
*   **极致效率**：针对显存优化，支持高效的低精度训练，降低硬件门槛。
*   **学术认可**：相关算法与框架设计已被顶级自然语言处理会议 ACL 2024 收录。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73469 | 🍴 8977 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个由微软发起的为期12周、包含24课时的AI入门课程，旨在向所有人普及人工智能知识。该项目使用Jupyter Notebook作为主要教学载体，内容覆盖从基础机器学习到深度学习的广泛主题。其目标是降低AI学习门槛，让初学者能够系统性地掌握相关技能。

2. **核心功能**
- 提供结构化的12周学习计划，将复杂概念拆解为24个易于理解的课时。
- 包含计算机视觉（CNN）、自然语言处理（RNN）及生成对抗网络（GAN）等深度专题。
- 基于Jupyter Notebook实现交互式代码教学，便于学习者边学边练。
- 涵盖机器学习与深度学习的基础理论及实际应用案例。
- 免费开源，适合不同背景的初学者从头开始构建AI知识体系。

3. **适用场景**
- 零基础学生或职场人士希望系统性地自学人工智能基础。
- 教育机构用于开展短期的AI启蒙工作坊或大学入门选修课。
- 开发者希望在掌握编程基础上，快速补充计算机视觉或NLP领域的专业知识。
- 企业团队内部培训，用于统一提升员工对AI技术的理解与应用能力。

4. **技术亮点**
- 由微软主导开发，内容权威且紧跟行业前沿技术趋势。
- 标签涵盖AI全栈领域（ML/DL/NLP/CV/GAN），提供全面的技术视野。
- 采用社区友好的“Microsoft for Beginners”系列标准，注重可读性与实践性结合。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52739 | 🍴 10693 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
本项目旨在通过从零开始构建的方式，深入理解并掌握人工智能工程的核心原理。用户将学习如何开发、部署AI系统，并将其转化为可供他人使用的实际产品。

2. **核心功能**
- 涵盖从基础机器学习到前沿生成式AI的全栈技术体系。
- 提供基于Python和Rust等语言的从零实现（from-scratch）代码示例。
- 集成大语言模型（LLM）、智能体（Agents）及多模态处理（如计算机视觉、NLP）。
- 包含强化学习与群体智能等高级AI概念的深入教程。
- 支持将AI模型工程化，包括服务部署与API开发（涉及TypeScript/MCP）。

3. **适用场景**
- AI初学者希望深入理解底层算法原理而非仅调用库函数。
- 工程师需要构建定制化AI代理（AI Agents）或智能体集群。
- 开发者致力于将大型语言模型或视觉模型集成到生产环境中。
- 研究人员探索生成式AI、强化学习及新型人机交互接口（如MCP）。

4. **技术亮点**
- 强调“从零实现”的教学理念，通过手写代码揭示AI黑盒机制。
- 跨语言支持（Python/Rust/TypeScript），兼顾性能优化与现代Web集成。
- 内容紧跟前沿，覆盖Agent、MCP、Swarm Intelligence等最新AI工程趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42808 | 🍴 7149 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数基础以及 PyTorch 和 TensorFlow 2.x 深度学习的综合性资源库。该项目集成了 NLTK 自然语言处理工具，旨在提供从理论到实践的完整 AI 学习路径。

2. **核心功能**
- 包含 AdaBoost、K-Means、SVM、随机森林等经典机器学习算法的实战代码。
- 深入讲解 DNN、RNN、LSTM、CNN 等深度学习模型及其在 PyTorch 和 TF2 中的实现。
- 涵盖推荐系统（如基于协同过滤）、NLP（如朴素贝叶斯、TF-IDF）及数据降维（PCA、SVD）等专项技术。
- 结合 Apriori、FP-Growth 等关联规则挖掘算法，提供数据挖掘领域的实用案例。
- 集成线性代数等数学基础知识点，辅助理解算法背后的原理。

3. **适用场景**
- 机器学习初学者希望系统性地从理论基础过渡到代码实战的学习者。
- 需要快速查阅常见算法（如 SVM、K-Means）Python 实现参考的开发者。
- 专注于自然语言处理或推荐系统方向，寻求特定模块（如 NLTK、协同过滤）示例的研究人员。
- 希望对比 Scikit-learn 与 PyTorch/TF2 在不同任务中应用差异的进阶学习者。

4. **技术亮点**
- 全面覆盖传统机器学习、深度学习、NLP 及数据挖掘四大领域，知识体系完整。
- 同时支持 Scikit-learn 和主流深度学习框架（PyTorch, TF2），适应不同技术栈需求。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42410 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35646 | 🍴 7372 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33768 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28784 | 🍴 3514 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25990 | 🍴 2945 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21755 | 🍴 3309 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35646 | 🍴 7372 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22570 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16369 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12924 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1205 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2190 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3296 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2629 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2429 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383930 | 🍴 80656 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 259987 | 🍴 23180 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 219428 | 🍴 41632 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197651 | 🍴 59572 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185657 | 🍴 46074 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166258 | 🍴 21486 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164240 | 🍴 30434 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157255 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 155017 | 🍴 8823 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152281 | 🍴 9635 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

