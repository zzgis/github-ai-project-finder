# GitHub AI项目每日发现报告
日期: 2026-07-23

## 新发布的AI项目

### official-document-ai-assistant
- 1. **中文简介**
这是一款本地化的桌面端助手，专注于官方文档的自动化审查与格式修复。它能够帮助用户快速修正文档规范，并支持合规性的导出操作，确保公文处理的准确性与效率。

2. **核心功能**
*   提供本地化的官方文档内容审查与错误检测功能。
*   自动修复文档中的格式问题，确保排版符合标准规范。
*   支持生成符合合规要求的文档导出版本。
*   作为桌面应用程序运行，保障数据处理的本地安全性。

3. **适用场景**
*   政府机关或企事业单位内部公文的标准化审核流程。
*   需要频繁处理大量格式复杂且需严格合规的文档编辑工作。
*   对数据安全有较高要求，需在离线或本地环境中进行文档处理的场景。

4. **技术亮点**
*   采用Python开发，便于集成现有的自然语言处理或文档解析库。
*   强调“本地化”部署，有效规避了云端处理带来的潜在数据泄露风险。
- 链接: https://github.com/NextWeb4/official-document-ai-assistant
- ⭐ 149 | 🍴 0 | 语言: Python

### Finn-loop
- 1. **中文简介**
Finn-loop 是一个专为 Claude Code 打造的“3技能”AI 软件工厂，涵盖规范制定、代码构建与审查流程。人类开发者负责最终的合并决策，确保 AI 生成的代码符合标准并安全集成。

2. **核心功能**
*   自动化软件开发生命周期管理，集成规范、构建和审查环节。
*   深度适配 Claude Code，实现高效的 AI 辅助编码工作流。
*   支持 GitHub 和 Linear 平台集成，打通任务追踪与版本控制。
*   强调人机协作模式，AI 负责执行，人类负责关键节点的合并审查。

3. **适用场景**
*   希望利用 AI 加速日常编码任务并标准化代码审查流程的开发团队。
*   使用 Linear 进行项目管理、同时需要 GitHub 自动化集成的高效软件工程环境。
*   寻求将 Claude Code 作为核心 AI 编码代理，并需要结构化工作流支持的开发者。

4. **技术亮点**
*   采用 Agentic Workflows（智能体工作流）架构，实现多步骤自动化协同。
*   明确界定 AI 执行与人类决策的边界，提升软件交付的安全性与可控性。
- 链接: https://github.com/finna/Finn-loop
- ⭐ 128 | 🍴 12 | 语言: JavaScript
- 标签: agentic-workflows, ai-agents, claude-code, github, linear

### open-ai-canvas
- 1. **中文简介**
Open-ai-canvas 是一个专为 AI 影视创作打造的开源无限画布工作台。它深度集成了多模态内容生成、分镜脚本编排、素材管理及智能 Agent 工作流，旨在提升影视制作效率。

2. **核心功能**
*   提供可视化的无限画布界面，支持非线性创作与布局调整。
*   集成多模态 AI 生成能力，可处理文本、图像及视频等多种媒体格式。
*   内置专业的分镜编排工具，帮助创作者规划镜头语言与叙事节奏。
*   具备高效的素材管理系统，方便集中存储、检索和调用创作资源。
*   支持基于 Agent 的自动化工作流，实现复杂任务的串联与执行。

3. **适用场景**
*   AI 辅助的电影或短片前期策划与分镜设计。
*   利用多模态模型进行概念艺术图或资产快速生成的视觉开发工作。
*   需要自动化处理多个生成步骤的复杂影视制作流程管理。
*   团队协作中的创意发散与可视化故事板构建。

4. **技术亮点**
*   采用 TypeScript 开发，保证代码类型安全与良好的可维护性。
*   将多模态生成能力与交互式画布结合，实现了从创意到可视化的无缝衔接。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 76 | 🍴 20 | 语言: TypeScript

### podcast-shorts-factory
- 1. **中文简介**
该项目是一个由十个协作AI代理组成的开源工具，能够自动将长播客转化为短视频。它完全免费且开源，并支持在免费的AI服务提供商上运行。

2. **核心功能**
- 利用AI代理自动化处理长音频到短视频的转换流程。
- 集成Whisper和LLM技术，实现精准的语音转文字与内容摘要。
- 通过FFmpeg进行视频剪辑、字幕合成及最终视频生成。
- 支持无头频道（Faceless Channel）模式，无需真人出镜即可创作内容。

3. **适用场景**
- 播客创作者快速将长篇音频内容剪辑为适合YouTube Shorts或TikTok的短视频片段。
- 自媒体运营者批量生产“无脸”类知识分享或娱乐短视频账号内容。
- 希望低成本自动化内容生产的个人或小型团队，利用免费AI资源降低运营成本。

4. **技术亮点**
- 采用多智能体协作架构（Multi-agent system），每个AI代理负责工作流中的特定环节，提高处理效率与准确性。
- 链接: https://github.com/krakonjac300-pixel/podcast-shorts-factory
- ⭐ 43 | 🍴 21 | 语言: Python
- 标签: ai-agents, content-automation, faceless-channel, ffmpeg, llm

### handoff-skill
- 1. **中文简介**
这是一个专为 Claude 设计的技能（Skill），能够将当前的对话内容自动转化为一份完整的交接文档。其核心目的是确保任何大型语言模型（LLM）都能无缝继承上下文，精准接续之前的讨论进度。

2. **核心功能**
- 自动生成结构化对话摘要，提取关键信息与决策点。
- 创建标准化的“交接文档”，便于不同 LLM 或团队间无缝传递上下文。
- 支持任意 LLM 读取该文档后，准确还原前序对话状态并继续推理。
- 深度集成于 Claude Code 环境，作为特定 Skill 运行以优化工作流。

3. **适用场景**
- 在多个人工智能代理或模型之间转移复杂任务的处理权。
- 当会话过长导致上下文窗口溢出时，保存关键进展以便后续重启。
- 团队协作中，将 AI 辅助开发的中间成果标准化地移交给其他开发者或模型。

4. **技术亮点**
- 利用 Claude Code 的 Skill 机制实现高度定制化的工作流自动化。
- 专注于解决 LLM 间的上下文断层问题，提升多模型协作的连贯性。
- 链接: https://github.com/ToolMonsters/handoff-skill
- ⭐ 26 | 🍴 10 | 语言: 未知
- 标签: ai, claude, claude-code, claude-skills, llm

### moonsconfig
- 描述: Open travel OS with Maya AI for calls, support chat, RFQs, vendor outreach, itinerary curation, route maps, packages, hotels, cars, CRM, bookings, and multi-tenant SaaS.
- 链接: https://github.com/schowdary75/moonsconfig
- ⭐ 16 | 🍴 2 | 语言: TypeScript
- 标签: ai-agent, asterisk, booking, customer-support, express

### memory-forest
- 描述: A verifiable local memory architecture for long-running AI agents
- 链接: https://github.com/hyungchulc/memory-forest
- ⭐ 14 | 🍴 2 | 语言: Python
- 标签: agent-memory, ai-agents, knowledge-management, local-first, markdown

### awesome-agent
- 描述: Open-source AI agent models, benchmarks, technical features and resources
- 链接: https://github.com/xinggangw/awesome-agent
- ⭐ 10 | 🍴 0 | 语言: 未知

### xinchao-dynamic-mind
- 描述: 独立、可自托管的 AI 动态心智状态引擎：驱动力、念头池、疲惫、睡眠与意图。
- 链接: https://github.com/tianyupaipai-cmd/xinchao-dynamic-mind
- ⭐ 10 | 🍴 3 | 语言: JavaScript
- 标签: ai-agent, mcp, nodejs, self-hosted, state-machine

### DarkPs-Agent-CLI
- 描述: Extensible local-first AI agent framework for automation, coding, tools, and multi-model workflows.
- 链接: https://github.com/dark-ps/DarkPs-Agent-CLI
- ⭐ 8 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的自然语言处理工具库，涵盖了从基础文本清洗（如敏感词检测、繁简转换）到高级语义分析（如情感分析、实体抽取）的多种功能。它不仅提供了丰富的中文资源库（如人名、地名、行业词汇），还集成了基于深度学习（如BERT）的预训练模型和数据处理工具。该项目旨在为开发者提供一站式解决方案，加速中文NLP应用的开发与落地。

2. **核心功能**
*   **基础文本处理与清洗**：支持中英文敏感词过滤、停用词管理、繁简转换、文本纠错以及正则表达式匹配（如手机号、身份证、邮箱抽取）。
*   **丰富知识库与资源**：内置中日文人名库、中文缩写、职业/汽车/医学/法律等垂直领域词库，以及古诗词、成语、歇后语等文化数据。
*   **高级NLP任务支持**：提供情感分析、命名实体识别（NER）、关系抽取、文本摘要、关键词提取及句子相似度计算等功能。
*   **预训练模型与深度学习集成**：整合了BERT、ALBERT、RoBERTa等多种主流预训练语言模型的中文版本及微调代码，支持知识图谱构建与问答系统开发。
*   **多模态与语音处理**：包含ASR语音数据集、语音识别工具、OCR文字识别（如手写汉字、文档表格）及语音情感分析相关资源。

3. **适用场景**
*   **智能客服与聊天机器人开发**：利用其对话语料、意图识别、实体抽取及闲聊模型快速搭建具备语义理解能力的对话系统。
*   **内容安全审核平台**：通过敏感词库、暴恐词表及谣言检测工具，自动化识别和过滤互联网内容中的违规信息。
*   **垂直领域知识图谱构建**：借助行业词库、命名实体识别及关系抽取工具，从非结构化文本中提取三元组信息，构建医疗、金融或法律领域的专业知识图谱。
*   **数据增强与预处理流水线**：使用其提供的文本清洗、分词、拼音标注及数据增强工具，为下游机器学习模型准备高质量的标准数据集。

4. **技术亮点**
*   **生态资源丰富**：不仅包含算法代码，还汇聚了大量高质量的中文公开数据集、预训练模型权重及行业专属词典，极大降低了数据获取门槛。
*   **前沿技术覆盖广**：紧跟NLP领域发展，集成了Transformer架构（BERT/GPT）在中文语境下的最佳实践，涵盖从传统统计方法到深度学习的多种范式。
*   **实用主义导向**：提供了大量开箱即用的工具链（如OCR、语音对齐、简历解析），直接针对实际业务痛点（如非结构化数据处理、特定格式抽取）提供解决方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81979 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的综合性资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域，并提供完整的代码实现。该项目旨在为开发者提供从入门到进阶的实战案例参考。

2. **核心功能**
- 收录500个涵盖主流AI领域的完整项目实例。
- 提供可直接运行的Python代码及详细文档说明。
- 分类清晰，支持按机器学习、深度学习、CV和NLP等标签快速检索。
- 包含大量经过验证的优秀开源项目（Awesome列表）。

3. **适用场景**
- AI初学者通过阅读代码快速理解算法原理并上手实践。
- 研究人员寻找特定领域（如目标检测、文本生成）的基线模型或参考实现。
- 企业开发者评估不同AI技术栈在解决实际问题时的可行性与效果。

4. **技术亮点**
- 极高的社区认可度（35k+星标），内容质量经过广泛验证。
- 覆盖全栈AI技术树，从传统机器学习到前沿大模型应用均有涉及。
- 注重工程落地，所有项目均附带可执行的代码仓库链接。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35634 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33255 | 🍴 3167 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是机器学习的开放标准，旨在实现不同深度学习框架之间的互操作性。它允许模型在 PyTorch、TensorFlow 等框架间无缝转换与部署。这一标准促进了跨平台的高效模型共享和推理加速。

2. **核心功能**
- 提供统一的中间表示格式，支持多种主流深度学习框架（如 PyTorch、TensorFlow、Keras）。
- 实现模型从训练框架到推理引擎的便捷转换，简化部署流程。
- 支持硬件加速优化，提升在不同设备上的推理性能。
- 拥有活跃的社区生态，涵盖广泛的算子和工具链支持。
- 促进跨平台和跨语言的模型兼容性，降低集成成本。

3. **适用场景**
- 需要将 PyTorch 或 TensorFlow 训练的模型部署到非原生支持的环境（如移动设备或嵌入式系统）时。
- 在多云或多框架环境中工作，需要统一模型管理以简化维护流程时。
- 利用 ONNX Runtime 等高性能推理引擎进行低延迟、高吞吐量的生产级服务部署时。
- 希望在不同硬件加速器（如 GPU、NPU、CPU）上快速验证和优化模型性能时。

4. **技术亮点**
- 作为行业标准的开放互操作性规范，被微软、Facebook 等巨头广泛采纳和支持。
- 与 ONNX Runtime 深度集成，提供极致的推理性能和广泛的硬件后端支持。
- 链接: https://github.com/onnx/onnx
- ⭐ 21205 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一部关于机器学习工程实践的开源指南。它系统性地涵盖了从模型训练、推理到大规模扩展的全生命周期工程知识。该项目旨在为构建和部署高性能机器学习系统提供全面的最佳实践参考。

2. **核心功能**
- 提供大规模分布式训练（如Slurm、PyTorch）的实操指南与配置示例。
- 深入解析大语言模型（LLM）的推理优化、调试技巧及显存管理策略。
- 涵盖MLOps基础设施，包括存储、网络及GPU集群的可扩展性设计。
- 分享针对Transformer架构及其他主流模型的工程化调优经验。

3. **适用场景**
- 需要在多节点GPU集群上高效训练大型深度学习模型的工程师。
- 致力于降低大语言模型推理延迟并优化资源利用率的团队。
- 正在构建或维护机器学习生产环境，寻求标准化工程流程的开发人员。

4. **技术亮点**
- 紧密结合前沿LLM技术与传统ML工程实践，内容极具时效性。
- 强调“开箱即用”的工程解决方案，提供大量可复现的代码与配置片段。
- 覆盖从底层硬件（GPU/网络）到上层应用（Inference/Training）的全栈视角。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18457 | 🍴 1178 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17332 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3382 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13170 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11592 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10673 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的综合性资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域，并提供完整的代码实现。该项目旨在为开发者提供从入门到进阶的实战案例参考。

2. **核心功能**
- 收录500个涵盖主流AI领域的完整项目实例。
- 提供可直接运行的Python代码及详细文档说明。
- 分类清晰，支持按机器学习、深度学习、CV和NLP等标签快速检索。
- 包含大量经过验证的优秀开源项目（Awesome列表）。

3. **适用场景**
- AI初学者通过阅读代码快速理解算法原理并上手实践。
- 研究人员寻找特定领域（如目标检测、文本生成）的基线模型或参考实现。
- 企业开发者评估不同AI技术栈在解决实际问题时的可行性与效果。

4. **技术亮点**
- 极高的社区认可度（35k+星标），内容质量经过广泛验证。
- 覆盖全栈AI技术树，从传统机器学习到前沿大模型应用均有涉及。
- 注重工程落地，所有项目均附带可执行的代码仓库链接。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35634 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33255 | 🍴 3167 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究人员提供了不可或缺的核心速查表集合。它旨在帮助研究者快速回顾和掌握关键概念、库用法及数学原理，是提升科研效率的实用工具。

2. **核心功能**
- 提供深度学习与机器学习领域的关键知识速查表。
- 涵盖主流框架（如Keras）的基础用法与示例。
- 包含数据科学常用库（如NumPy, SciPy, Matplotlib）的操作指南。
- 整理研究者常用的数学公式与算法逻辑摘要。

3. **适用场景**
- 研究人员在进行模型构建前快速回顾技术细节。
- 初学者或转行者用于系统梳理AI领域的基础知识体系。
- 开发者在调试代码时查阅特定库函数的使用规范。
- 准备面试或考试时作为快速复习的资料参考。

4. **技术亮点**
项目整合了从底层数学原理到上层框架应用的全栈式速查内容，结构清晰，便于按需检索。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3382 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一套完整的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户轻松入门并胜任就业实战。内容涵盖Python、数学基础以及机器学习、深度学习、计算机视觉和自然语言处理等热门领域。

2. **核心功能**
*   提供系统化的AI学习路径，整合从基础到进阶的学习资源。
*   汇编近200个实战案例与项目代码，支持直接复现与应用。
*   免费提供详细的配套教材与学习资料，降低学习门槛。
*   覆盖主流AI框架与技术栈，包括PyTorch、TensorFlow、Keras及Pandas等。
*   聚焦就业导向，强调通过实战项目提升实际工作能力。

3. **适用场景**
*   希望从零开始系统学习人工智能的初学者。
*   需要大量实战项目参考以巩固理论知识的在校学生或自学者。
*   寻求职业转型或提升技能以进入AI行业的求职者。
*   希望快速查阅特定AI技术（如CV、NLP）常用库和算法的研究人员。

4. **技术亮点**
*   高度整合了多领域热门技术标签（如算法、数据挖掘、科学计算库），形成一站式学习资源库。
*   兼顾理论与实践，通过“路线图+实战案例+免费教材”的组合模式，极大提升了学习效率。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13170 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它支持数据驱动的开发流程，让开发者能够更高效地进行模型训练与微调。

**2. 核心功能**
*   提供声明式配置界面，实现无需编写大量代码即可快速搭建机器学习模型。
*   原生支持大型语言模型（如 LLaMA、Mistral）的微调与训练，兼容 PyTorch 后端。
*   涵盖计算机视觉和自然语言处理等多种任务类型，支持端到端的深度学习工作流。
*   强调以数据为中心的开发理念，简化了从数据处理到模型评估的全过程。

**3. 适用场景**
*   **快速原型开发**：研究人员或工程师希望在不深入底层代码的情况下，快速验证不同架构或算法的效果。
*   **LLM 微调定制**：企业或个人需要对开源大语言模型（如 LLaMA2、Mistral）进行领域特定的微调，以适应垂直行业需求。
*   **多模态 AI 应用构建**：需要同时处理图像（计算机视觉）和文本（自然语言处理）数据的复杂 AI 项目。

**4. 技术亮点**
*   显著的“低代码”特性大幅降低了深度学习模型的入门门槛和开发周期。
*   广泛的标签覆盖表明其对主流现代架构（如 LLaMA 系列）及前沿技术（如 Data-centric AI）的良好支持。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9144 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8937 | 🍴 3102 | 语言: C++
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
- ⭐ 6268 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的自然语言处理工具库，涵盖了从基础文本清洗（如敏感词检测、繁简转换）到高级语义分析（如情感分析、实体抽取）的多种功能。它不仅提供了丰富的中文资源库（如人名、地名、行业词汇），还集成了基于深度学习（如BERT）的预训练模型和数据处理工具。该项目旨在为开发者提供一站式解决方案，加速中文NLP应用的开发与落地。

2. **核心功能**
*   **基础文本处理与清洗**：支持中英文敏感词过滤、停用词管理、繁简转换、文本纠错以及正则表达式匹配（如手机号、身份证、邮箱抽取）。
*   **丰富知识库与资源**：内置中日文人名库、中文缩写、职业/汽车/医学/法律等垂直领域词库，以及古诗词、成语、歇后语等文化数据。
*   **高级NLP任务支持**：提供情感分析、命名实体识别（NER）、关系抽取、文本摘要、关键词提取及句子相似度计算等功能。
*   **预训练模型与深度学习集成**：整合了BERT、ALBERT、RoBERTa等多种主流预训练语言模型的中文版本及微调代码，支持知识图谱构建与问答系统开发。
*   **多模态与语音处理**：包含ASR语音数据集、语音识别工具、OCR文字识别（如手写汉字、文档表格）及语音情感分析相关资源。

3. **适用场景**
*   **智能客服与聊天机器人开发**：利用其对话语料、意图识别、实体抽取及闲聊模型快速搭建具备语义理解能力的对话系统。
*   **内容安全审核平台**：通过敏感词库、暴恐词表及谣言检测工具，自动化识别和过滤互联网内容中的违规信息。
*   **垂直领域知识图谱构建**：借助行业词库、命名实体识别及关系抽取工具，从非结构化文本中提取三元组信息，构建医疗、金融或法律领域的专业知识图谱。
*   **数据增强与预处理流水线**：使用其提供的文本清洗、分词、拼音标注及数据增强工具，为下游机器学习模型准备高质量的标准数据集。

4. **技术亮点**
*   **生态资源丰富**：不仅包含算法代码，还汇聚了大量高质量的中文公开数据集、预训练模型权重及行业专属词典，极大降低了数据获取门槛。
*   **前沿技术覆盖广**：紧跟NLP领域发展，集成了Transformer架构（BERT/GPT）在中文语境下的最佳实践，涵盖从传统统计方法到深度学习的多种范式。
*   **实用主义导向**：提供了大量开箱即用的工具链（如OCR、语音对齐、简历解析），直接针对实际业务痛点（如非结构化数据处理、特定格式抽取）提供解决方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81979 | 🍴 15253 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73466 | 🍴 8976 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的AI通识课程，旨在让所有人都能轻松学习人工智能。该项目由Microsoft For Beginners提供，通过结构化的教学计划帮助用户系统掌握AI基础知识。

2. **核心功能**
- 提供结构化的12周学习计划，涵盖从基础到进阶的24个课时。
- 使用Jupyter Notebook作为主要教学载体，支持交互式代码练习。
- 内容全面覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
- 专为初学者设计，降低AI学习门槛，适合零基础用户入门。

3. **适用场景**
- 大学生或职场新人希望系统性地从零开始学习人工智能概念。
- 教育工作者寻找结构化、易于实施的AI入门课程教学资源。
- 对AI感兴趣但缺乏编程背景的公众，希望通过实践项目快速上手。

4. **技术亮点**
- 采用Jupyter Notebook实现理论与代码实践的紧密结合，便于即时反馈。
- 标签涵盖CNN、GAN、RNN等主流AI模型，内容紧跟技术发展前沿。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52711 | 🍴 10691 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42706 | 🍴 7114 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解线性代数基础及 PyTorch、NLTK 和 TensorFlow 2 等主流框架的应用。该项目旨在通过系统化的教程帮助开发者掌握从经典算法到深度学习的完整技术栈。

2. **核心功能**
*   提供机器学习经典算法（如 SVM、K-Means、随机森林等）的代码实现与原理详解。
*   整合深度学习框架（PyTorch、TensorFlow 2）的实战案例，包括 DNN、RNN、LSTM 等模型。
*   包含自然语言处理（NLP）模块，利用 NLTK 进行文本分析与推荐系统开发。
*   夯实数学基础，专门讲解线性代数在机器学习中的应用。
*   涵盖多种关联规则挖掘算法（如 Apriori、FP-Growth）及降维技术（PCA、SVD）。

3. **适用场景**
*   机器学习初学者希望系统性地从理论到代码复现掌握各类算法。
*   数据科学家需要参考高质量的 Python 实现示例以加速项目开发。
*   研究人员或学生利用其 NLP 和深度学习模块进行特定领域的模型训练与实验。
*   高校教师或培训机构将其作为教学辅助材料，用于讲解 AI 核心概念。

4. **技术亮点**
*   技术栈全面：同时覆盖传统机器学习、深度学习及自然语言处理三大领域。
*   多框架支持：兼容 Scikit-learn、PyTorch 和 TensorFlow 2，适应不同开发习惯。
*   注重基础：不仅提供代码，还结合线性代数等数学基础，帮助理解算法本质。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42409 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35634 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33767 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28778 | 🍴 3513 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25988 | 🍴 2944 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21752 | 🍴 3309 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个精选的 AI 项目合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它提供了 500 个带有代码实现的具体案例，帮助开发者快速上手和实践。作为一个“Awesome”列表，它整合了丰富的资源以支持数据科学和人工智能的学习与开发。

2. **核心功能**
- 汇集 500 多个真实的 AI 项目代码示例，覆盖主流技术栈。
- 分类清晰，明确区分机器学习、深度学习、计算机视觉和 NLP 等方向。
- 提供即插即用的代码实现，便于直接运行和学习参考。
- 作为综合性资源库，适合从入门到进阶的 AI 学习者查阅。

3. **适用场景**
- AI 初学者通过实战项目快速理解算法原理和应用。
- 开发者寻找特定领域（如 CV 或 NLP）的代码模板进行二次开发。
- 学生或研究人员需要大量案例来辅助学习或论文实验对比。
- 企业技术人员评估不同 AI 解决方案的技术可行性和实现难度。

4. **技术亮点**
- 项目数量庞大且分类全面，是高质量的一站式 AI 资源库。
- 强调“带代码”的实践性，避免了纯理论介绍的枯燥。
- 由社区维护的 Awesome 列表，通常包含最新和最流行的项目。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35634 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化平台，专门用于通过 AI 驱动来执行基于浏览器的复杂工作流。它利用大型语言模型（LLM）和计算机视觉技术，模拟人类操作以自动完成网页交互任务。

2. **核心功能**
*   利用 LLM 理解网页结构并自主规划操作步骤，实现无需硬编码脚本的智能自动化。
*   结合计算机视觉与浏览器自动化引擎（如 Playwright），精准定位页面元素并执行点击、输入等动作。
*   提供标准化的 API 接口，方便开发者将 AI 浏览器自动化能力集成到现有业务流程中。
*   支持处理动态网页和非结构化数据，能够适应频繁变更的前端界面而不轻易失效。

3. **适用场景**
*   **RPA 替代方案**：自动化那些传统 RPA 难以维护、因 UI 变动而频繁报错的网页数据录入或表单提交任务。
*   **跨平台数据采集**：从结构复杂或需要登录验证的网站中自动抓取数据，并整理为结构化格式。
*   **在线流程自动化**：自动执行如在线预约、票务购买、库存监控等需要多步骤交互的电商或公共服务流程。

4. **技术亮点**
*   **视觉-语言模型驱动**：创新性地结合视觉识别与大语言模型的推理能力，使机器能像人一样“看懂”网页并做出决策。
*   **高鲁棒性**：相比传统 Selenium/Playwright 脚本，对网页布局微小变化的容忍度更高，降低了自动化脚本的维护成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22561 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉 AI 数据集的领先平台，提供开源、云及企业级产品。它支持图像、视频和 3D 数据的标注，并具备 AI 辅助标注、质量控制、团队协作及开发者 API 等丰富功能。

2. **核心功能**
- 支持图像、视频及 3D 数据的全方位标注与 AI 辅助自动标注。
- 提供从开源版本到企业级部署的多模式产品选择及专业标注服务。
- 内置质量控制、团队协作文档以及数据分析工具。
- 开放开发者 API，便于集成至现有工作流。

3. **适用场景**
- 计算机视觉算法训练所需的大规模高质量标注数据集构建。
- 需要多人协作进行复杂图像或视频数据标注的企业级团队。
- 希望利用 AI 预标注功能以显著提升数据处理效率的研发团队。

4. **技术亮点**
- 兼容 TensorFlow 和 PyTorch 等主流深度学习框架生态。
- 覆盖目标检测、语义分割、图像分类等多种前沿标注任务类型。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16367 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级AI可解释性工具包，支持CNN和Vision Transformers等多种模型。它涵盖了分类、目标检测、分割及图像相似度分析等任务，旨在提升深度学习模型的透明度。

2. **核心功能**
- 支持Grad-CAM、Score-CAM等多种可视化算法以生成类激活图。
- 兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
- 适用于图像分类、目标检测、语义分割及图像相似度对比等多种任务。
- 提供直观的可视化效果，帮助理解模型决策依据。

3. **适用场景**
- 研究人员用于分析和调试深度学习模型的特征关注区域。
- 开发人员在部署CV模型前验证其对关键目标的识别逻辑。
- 医疗或自动驾驶领域从业者向非技术利益相关者解释AI决策过程。
- 教育场景中展示不同网络结构对输入图像的注意力分布差异。

4. **技术亮点**
- 广泛支持主流视觉模型架构，包括最新的Vision Transformers。
- 实现多种SOTA可解释性方法（如Grad-CAM, Score-CAM），便于统一比较。
- 代码库成熟稳定，拥有近1.3万星标，社区活跃且文档完善。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12923 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了完全可微分的图像处理算子和几何变换工具，旨在简化深度学习中的视觉任务开发。

2. **核心功能**
- 提供基于 PyTorch 的完全可微分图像处理和几何操作。
- 支持多种传统计算机视觉算法的深度神经网络集成。
- 内置丰富的数据增强和图像转换工具，便于模型训练。
- 优化了 GPU 加速计算，提升大规模视觉任务的执行效率。

3. **适用场景**
- 需要端到端可微分视觉管道的深度学习和机器人研究。
- 利用传统 CV 算法进行图像预处理和后处理的混合架构开发。
- 构建对几何变换和空间关系敏感的计算机视觉应用。

4. **技术亮点**
- 无缝集成 PyTorch 生态，允许将传统 CV 模块直接嵌入深度学习模型中作为可学习组件。
- 链接: https://github.com/kornia/kornia
- ⭐ 11283 | 🍴 1205 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2190 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3295 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2429 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，致力于让用户完全掌控自己的数据。它以独特的“龙虾”理念（Lobster Way）为核心，提供安全、私密的本地化 AI 体验。该项目旨在打造真正属于用户的自主式人工智能代理。

2. **核心功能**
- 跨平台兼容：支持在任何主流操作系统上部署运行。
- 数据私有化：强调“Own Your Data”，确保用户数据不被第三方滥用。
- 本地化 AI 代理：作为个人助理在本地环境中处理任务，保障隐私安全。
- TypeScript 构建：基于现代前端语言开发，保证代码的可维护性与扩展性。

3. **适用场景**
- 注重隐私的个人用户希望拥有不依赖云服务的本地 AI 助手。
- 开发者或技术爱好者想要搭建自定义的、可完全控制数据的 AI 代理环境。
- 需要在离线或内网环境下使用 AI 辅助日常任务的企业或个人。

4. **技术亮点**
- 采用 TypeScript 开发，具备良好的类型安全和生态兼容性。
- 设计哲学强调去中心化和用户主权，区别于传统云端 AI 服务。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383884 | 🍴 80646 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理式技能框架及软件开发方法论。它致力于通过结构化的技能体系，提升 AI 代理在复杂编程任务中的实际效能与可靠性。该项目旨在解决传统 AI 辅助开发中缺乏系统性指导的问题。

2. **核心功能**
- 提供一套标准化的“代理式技能”库，用于规范 AI 在软件开发各阶段的行为。
- 集成头脑风暴、代码编写等关键开发环节的最佳实践流程。
- 支持子代理驱动的开发模式，实现复杂任务的自动化分解与执行。
- 结合 SDLC（软件开发生命周期）方法论，确保开发过程的系统性与完整性。

3. **适用场景**
- 需要系统化引导大型语言模型进行复杂软件架构设计的团队。
- 希望将 AI 代理深度整合进现有 DevOps 或 SDLC 流程的企业。
- 探索“子代理驱动开发”（Subagent-driven Development）新范式的开发者社区。
- 寻求提升 AI 辅助编码质量、减少幻觉并增强逻辑一致性的研究项目。

4. **技术亮点**
- 创新性地将非代码类的“软技能”（如头脑风暴、规划）转化为可执行的代理指令。
- 基于 Shell 脚本实现轻量级且易于集成的框架部署，兼容性强。
- 标签涵盖“obra”及具体开发范式，体现了对新兴 AI 软件工程标准的探索。
- 链接: https://github.com/obra/superpowers
- ⭐ 259826 | 🍴 23167 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够伴随用户共同成长的智能代理工具。它旨在通过持续学习和交互，提供个性化的辅助体验，让用户在使用过程中不断优化其能力。

2. **核心功能**
- 支持多模型集成，兼容 Anthropic、OpenAI 等主流大语言模型平台。
- 具备上下文记忆与学习能力，能随使用过程不断进化并适应用户习惯。
- 提供灵活的 API 接口，便于开发者将其嵌入到现有工作流中。
- 拥有模块化架构，支持自定义插件和扩展功能以满足特定需求。

3. **适用场景**
- 需要个性化代码助手且希望工具能理解项目背景的开发者团队。
- 寻求自动化日常任务处理并期望工具随时间提升效率的个人用户。
- 正在构建多智能体系统或需要统一接入多种 LLM 能力的 AI 应用开发者。

4. **技术亮点**
- 跨平台兼容性极强，无缝衔接 OpenClaw、Codex 等多个生态组件。
- 采用先进的提示工程策略，确保在复杂交互中保持高准确性和稳定性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 219274 | 🍴 41569 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个支持公平代码许可的工作流自动化平台，具备原生 AI 能力。它结合了可视化构建与自定义代码功能，支持自托管或云部署，并拥有超过 400 种集成方式。

2. **核心功能**
*   提供可视化拖拽界面与自定义代码相结合的工作流构建模式。
*   内置原生 AI 功能，支持智能任务处理与分析。
*   支持自托管私有部署及云端服务，保障数据主权与灵活性。
*   集成超过 400 种应用接口，实现广泛的数据互通。
*   支持 MCP（模型上下文协议）客户端与服务端，增强 AI 交互能力。

3. **适用场景**
*   **企业级数据同步**：在 CRM、ERP 等系统间自动同步客户数据与业务记录。
*   **AI 驱动的内容生成**：利用原生 AI 能力自动生成营销文案或分析用户反馈。
*   **复杂后端逻辑编排**：通过自定义代码节点处理复杂的 API 调用和数据转换流程。
*   **私有化智能工作流**：在受控环境中搭建安全、可定制的内部自动化系统。

4. **技术亮点**
*   **MCP 协议支持**：原生兼容模型上下文协议，便于扩展 AI 模型的连接与应用。
*   **TypeScript 全栈开发**：基于 TypeScript 构建，保证代码类型安全与开发效率。
*   **混合编程范式**：完美融合低代码/无代码的便捷性与自定义代码的灵活性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197596 | 🍴 59561 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让开发者能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，让用户能够将精力集中在真正重要的事情上。

2. **核心功能**
- 具备自主规划与执行任务能力的智能代理架构。
- 支持集成多种大型语言模型（如 GPT、Claude、Llama）以增强灵活性。
- 提供开放的开发环境，便于用户构建和定制 AI 应用。
- 自动化处理复杂工作流，减少人工干预需求。

3. **适用场景**
- 需要自动化执行多步骤复杂任务的研发场景。
- 希望快速原型化并测试 AI 代理逻辑的开发者社区。
- 利用现有 LLM API 构建定制化自主 AI 助手的企业。

4. **技术亮点**
- 作为 Agentic AI 领域的标杆项目，拥有极高的社区关注度和活跃度。
- 兼容主流大模型接口，降低了接入不同 AI 服务的门槛。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185649 | 🍴 46075 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166245 | 🍴 21482 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164234 | 🍴 30435 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157245 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154822 | 🍴 8818 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152261 | 🍴 9633 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

