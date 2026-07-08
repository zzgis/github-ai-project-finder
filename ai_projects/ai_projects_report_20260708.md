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
该项目允许用户通过本地命令行接口（CLI）一次性向 Claude、Codex (GPT) 和 Antigravity (Gemini) 三个不同的 AI 模型发送相同的提示词。它旨在简化多模型对比流程，让用户能够快速获取不同大语言模型的回复以便进行比较。

2. **核心功能**
*   支持同时调用 Claude、OpenAI Codex 和 Google Gemini 三大主流 AI 模型。
*   通过本地 CLI 工具实现模型交互，无需依赖复杂的 Web 界面。
*   提供统一的输入接口，确保所有模型接收完全相同的提示词内容。
*   基于 HTML 构建前端展示层，用于呈现多路模型返回的结果。

3. **适用场景**
*   需要横向对比不同大模型在特定任务上表现差异的开发者或研究人员。
*   希望利用本地环境快速测试提示词效果，以优化 Prompt 工程的用户。
*   寻求替代方案或希望分散 API 依赖风险，同时使用多个 AI 服务的个人用户。

4. **技术亮点**
*   实现了跨厂商 AI 服务的统一 CLI 封装，降低了多模型调用的门槛。
*   采用轻量级的 HTML 前端结构，专注于结果展示的直观性与简洁性。
- 链接: https://github.com/PeterPanSwift/fox-ai-roundtable
- ⭐ 63 | 🍴 9 | 语言: HTML

### blockout
- 1. **中文简介**
Blockout 是一款专为 AI 原生电影制作设计的预可视化（Previs）工具，支持搭建灰盒场景、编排摄像机运动及演员走位标记。用户可导出包含动作参考的数据包，以便与 Seedance、Veo、Kling、LTX 或 Wan 等主流 AI 视频生成模型无缝对接。该项目采用 Apache-2.0 开源协议，基于 TypeScript 开发。

2. **核心功能**
*   提供灰盒场景搭建能力，用于快速构建电影拍摄的初步空间结构。
*   支持摄像机路径规划与演员走位标记（Marks）的详细编排。
*   能够导出标准化的动作参考数据包，直接适配多种 AI 视频生成引擎。
*   实现从传统预可视化流程到 AI 视频生成的数据桥梁，简化工作流。

3. **适用场景**
*   AI 电影导演在正式生成前，利用 Blockout 规划镜头语言和场景布局。
*   特效团队需要将传统拍摄的运动数据转化为 AI 模型可理解的参考输入。
*   独立创作者希望快速验证创意概念，并通过导出数据驱动 Kling 或 Veo 等工具生成高质量片段。

4. **技术亮点**
*   打通了传统影视预可视化软件与新兴 AI 视频生成模型之间的数据壁垒。
*   基于 TypeScript 开发，具备良好的跨平台兼容性和现代前端扩展性。
- 链接: https://github.com/wassermanproductions/blockout
- ⭐ 52 | 🍴 7 | 语言: TypeScript

### seedance-prompt
- 1. **中文简介**
该项目是专为 Seedance 及各类文本生成视频模型打造的 Hermes 技能包，旨在提供具有高度真实感的 AI 视频提示词。它通过优化的指令结构，帮助用户更精准地控制视频生成的视觉效果与细节表现。

2. **核心功能**
*   提供针对 Seedance 平台优化的专用提示词模板。
*   支持广泛兼容其他主流文本到视频生成模型。
*   专注于提升生成视频画面的写实度与自然感。
*   作为 Hermes 技能集成，简化提示词的构建流程。

3. **适用场景**
*   需要生成高保真、电影级质感短视频内容的创作者。
*   在使用 Seedance 或其他 T2V 模型时遇到画面失真问题的用户。
*   希望快速批量生成特定风格（如纪实、拟真）视频素材的工作流。

4. **技术亮点**
该项目本身不包含代码实现，而是作为一种“技能”或提示词库存在，侧重于语义优化而非底层算法创新，适合追求高效提示词工程的用户直接使用。
- 链接: https://github.com/zhouwei713/seedance-prompt
- ⭐ 51 | 🍴 10 | 语言: 未知

### openclaw-voice-call-realtime
- ### 1. 中文简介
这是一个名为 OpenClaw 的插件，旨在通过结合 Twilio 和 OpenAI Realtime API，为您的 AI 助手赋予拨打电话的能力。它支持通话中的工具调用、实时转录以及来电筛选功能，实现了真正的实时语音交互体验。

### 2. 核心功能
*   **真实电话集成**：利用 Twilio 实现与真实手机号码的双向语音通话。
*   **实时 AI 交互**：基于 OpenAI Realtime API 提供低延迟的自然语言对话能力。
*   **智能来电筛选**：具备过滤垃圾来电或识别特定呼叫者的功能。
*   **通话中工具执行**：AI 在通话过程中可动态调用外部工具以完成用户请求。
*   **全程转录记录**：自动将通话内容转化为文本记录，便于后续追溯和分析。

### 3. 适用场景
*   **个人助理服务**：为家庭或企业提供类似 Siri/Google Assistant 但更强大的自动化电话接听与处理服务。
*   **客户服务自动化**：用于处理初步的客户咨询、预约安排或订单状态查询。
*   **紧急通知系统**：在需要时通过 AI 助手主动拨打重要电话进行提醒或通知。
*   **交互式语音门户**：构建无需人工介入的自动语音应答（IVR）系统，提升用户体验。

### 4. 技术亮点
该项目巧妙地将传统的电信网络（Twilio）与现代生成式 AI 实时音频流技术（OpenAI Realtime）相结合，并通过 TypeScript 插件架构（OpenClaw）实现了模块化的功能扩展，使得 AI 不仅能“说”，还能在电话场景中“做”事（如操作工具）。
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
- ⭐ 27 | 🍴 28 | 语言: TypeScript
- 标签: agent-security, ai-agent-identity, ai-agents, certificate-authority, compliance

### kakunin-core
- 描述: AI agent compliance platform — X.509 identity via AWS KMS, real-time behavioral risk scoring, auto-revocation, and MiCA / EU AI Act compliance reporting. AGPL-3.0.
- 链接: https://github.com/nqzai/kakunin-core
- ⭐ 25 | 🍴 1 | 语言: TypeScript
- 标签: agent-security-tools, ai-agent-identity, ai-agents-security, ai-governance-tools, audit-log-tools

### lapian-notes
- 描述: 拉片笔记:把电影变成 AI 辅助的拉片笔记 - 本地抽帧/剧情泳道时间轴/结构树/情绪曲线/段落深拆
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 23 | 🍴 5 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### gogh
- 描述: Gogh is a source-cited Obsidian operating brain that turns six frontend design skills into one advisable stack for AI coding agents.
- 链接: https://github.com/AgriciDaniel/gogh
- ⭐ 21 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP是一个全面且实用的中文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。它提供了丰富的中文词库资源（包括同义词、反义词、情感值、行业术语等）以及多种预训练模型和深度学习应用案例，旨在降低中文NLP的开发门槛。

2. **核心功能**
- **基础文本处理**：支持中英文敏感词过滤、语言检测、繁简体转换及中文分词加速。
- **实体与信息抽取**：提供手机号、身份证、邮箱、地址等正则匹配，以及基于BERT等模型的命名实体识别（NER）。
- **丰富词库资源**：内置大量中文专用词库，涵盖同/反义词、情感词典、行业术语（医疗、法律、汽车等）及停用词。
- **深度学习模型集成**：收录BERT、ALBERT、RoBERTa等预训练模型代码，以及文本分类、摘要生成、知识图谱构建等SOTA方案。
- **语音与多模态支持**：包含中文语音识别（ASR）、拼音转换、手写OCR及音频数据增强工具。

3. **适用场景**
- **内容安全审核**：用于互联网平台对UGC内容进行敏感词过滤、暴恐词检测及谣言识别。
- **智能客服与对话系统**：利用情感分析、意图识别和对话管理组件构建专业的中文聊天机器人或客服系统。
- **企业级信息抽取**：从非结构化文本（如简历、新闻、合同）中自动提取关键实体（人名、机构、地名）并构建知识图谱。
- **NLP研究与教学**：作为学习中文自然语言处理、对比不同算法模型（如BERT vs BiLSTM）及复现经典论文代码的资源库。

4. **技术亮点**
- **资源极度丰富**：不仅包含代码，还整合了海量高质量中文数据集、词库及学术报告，是中文NLP领域的“百科全书”。
- **全链路覆盖**：从底层的数据清洗、分词，到中层的情感分析、实体抽取，再到上层的知识图谱构建和对话生成，提供一站式解决方案。
- **紧跟前沿技术**：持续更新最新的预训练语言模型（如ELECTRA、ALBERT）和竞赛获奖方案，确保用户能接触到业界最先进的NLP实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81688 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目代码的精选仓库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目作为一份全面的“Awesome”列表，为开发者提供了丰富的实战案例和参考资源。

2. **核心功能**
- 提供大量涵盖机器学习、深度学习、NLP和CV领域的完整项目代码示例。
- 对AI相关技术栈进行系统化分类与整理，便于快速检索特定方向的项目。
- 作为学习资源库，帮助开发者通过阅读和运行真实代码来理解算法实现。
- 汇聚社区精选的优质AI实践项目，降低寻找高质量开源案例的成本。

3. **适用场景**
- AI初学者希望通过实际代码案例快速入门并理解各类算法的应用逻辑。
- 研究人员或工程师需要查找特定领域（如图像识别、文本分类）的参考实现。
- 教育者利用这些项目作为教学素材，指导学生进行动手实践。
- 开发者在进行技术选型时，评估不同AI解决方案的可行性和代码质量。

4. **技术亮点**
- 内容覆盖面极广，整合了AI多个子领域的数百个高质量开源项目。
- 采用“Awesome”列表形式组织，结构清晰，极具导航和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够直观展示模型结构并辅助开发者进行调试与分析。该工具以轻量级和广泛的兼容性著称，是 AI 领域不可或缺的数据可视化工具。

2. **核心功能**
*   支持加载并可视化多种主流框架（如 PyTorch, TensorFlow, ONNX, CoreML 等）生成的模型文件。
*   提供直观的图形化界面，清晰展示神经网络层结构、数据流向及张量维度信息。
*   支持查看模型权重、偏差值及节点属性，帮助深入理解模型内部参数配置。
*   具备跨平台特性，可通过桌面应用或网页浏览器直接运行，无需复杂的环境配置。
*   允许导出模型结构截图或静态图像，便于在文档或演示中引用模型架构。

3. **适用场景**
*   深度学习研究人员用于快速检查新构建模型的层级结构和连接关系是否正确。
*   工程师在模型转换过程中（如从 PyTorch 转为 ONNX），验证转换后的模型结构与预期一致。
*   开发者在部署模型前，通过可视化确认输入输出节点名称及数据类型，以便对接应用程序。
*   技术文档编写者利用其生成的结构图，直观地向非技术人员或团队成员解释算法原理。

4. **技术亮点**
*   **极致的兼容性**：原生支持 safetensors、TFLite 等较新的模型格式，覆盖范围远超同类工具。
*   **零依赖与轻量化**：基于 Electron 和 Node.js 构建，无需安装庞大的 Python 环境即可运行，启动速度快。
*   **开源透明**：完全开源且社区活跃，Star 数超过 3.3 万，证明了其在 AI 开发者群体中的高认可度和广泛使用率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33197 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。

**2. 核心功能**
*   支持在不同深度学习框架（如PyTorch、TensorFlow）间进行模型格式转换。
*   提供统一的中间表示形式，确保模型在不同平台和硬件上的兼容性。
*   允许开发者优化模型推理性能，适配多种后端执行引擎。
*   拥有活跃的社区支持，涵盖主流AI库和工具链。

**3. 适用场景**
*   需要将PyTorch或Keras训练的模型部署到不支持原生框架的生产环境中。
*   在边缘设备或特定硬件加速器上运行深度学习推理任务。
*   跨团队协作时，统一模型存储和交换格式以减少版本冲突。

**4. 技术亮点**
*   作为行业通用的开放标准，被微软、Facebook、Amazon等巨头广泛采用和支持。
*   生态丰富，拥有ONNX Runtime等高性能推理引擎，显著提升部署效率。
- 链接: https://github.com/onnx/onnx
- ⭐ 21116 | 🍴 3960 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一部全面涵盖机器学习系统构建、部署与优化的实战指南。它深入讲解了从底层硬件配置到大规模模型训练及推理的工程细节，旨在帮助开发者解决复杂的MLOps挑战。

2. **核心功能**
- 提供大规模分布式训练和推理的完整工程实践指导。
- 详解GPU集群管理、网络通信优化及存储策略等基础设施知识。
- 涵盖调试技巧、可扩展性设计以及Slurm作业调度系统的实际应用。
- 整合PyTorch、Transformers等主流框架的性能调优最佳实践。

3. **适用场景**
- 需要从零搭建或优化大型深度学习训练集群的工程师。
- 致力于提升LLM（大语言模型）推理延迟和吞吐量的后端开发团队。
- 希望系统学习MLOps全流程及故障排查方法的ML从业者。
- 研究高性能计算资源调度与网络瓶颈解决方案的研究人员。

4. **技术亮点**
- 内容紧跟前沿，深度结合LLM时代特有的工程挑战（如显存优化、并行策略）。
- 强调“工程落地”，不仅讲理论，更提供具体的代码示例和配置参数。
- 覆盖范围极广，从硬件层（GPU/网络）到软件层（框架/调度器）形成闭环知识体系。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18266 | 🍴 1159 | 语言: Python
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
这是一个汇集了500个AI项目代码的精选仓库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目作为一份全面的“Awesome”列表，为开发者提供了丰富的实战案例和参考资源。

2. **核心功能**
- 提供大量涵盖机器学习、深度学习、NLP和CV领域的完整项目代码示例。
- 对AI相关技术栈进行系统化分类与整理，便于快速检索特定方向的项目。
- 作为学习资源库，帮助开发者通过阅读和运行真实代码来理解算法实现。
- 汇聚社区精选的优质AI实践项目，降低寻找高质量开源案例的成本。

3. **适用场景**
- AI初学者希望通过实际代码案例快速入门并理解各类算法的应用逻辑。
- 研究人员或工程师需要查找特定领域（如图像识别、文本分类）的参考实现。
- 教育者利用这些项目作为教学素材，指导学生进行动手实践。
- 开发者在进行技术选型时，评估不同AI解决方案的可行性和代码质量。

4. **技术亮点**
- 内容覆盖面极广，整合了AI多个子领域的数百个高质量开源项目。
- 采用“Awesome”列表形式组织，结构清晰，极具导航和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够直观展示模型结构并辅助开发者进行调试与分析。该工具以轻量级和广泛的兼容性著称，是 AI 领域不可或缺的数据可视化工具。

2. **核心功能**
*   支持加载并可视化多种主流框架（如 PyTorch, TensorFlow, ONNX, CoreML 等）生成的模型文件。
*   提供直观的图形化界面，清晰展示神经网络层结构、数据流向及张量维度信息。
*   支持查看模型权重、偏差值及节点属性，帮助深入理解模型内部参数配置。
*   具备跨平台特性，可通过桌面应用或网页浏览器直接运行，无需复杂的环境配置。
*   允许导出模型结构截图或静态图像，便于在文档或演示中引用模型架构。

3. **适用场景**
*   深度学习研究人员用于快速检查新构建模型的层级结构和连接关系是否正确。
*   工程师在模型转换过程中（如从 PyTorch 转为 ONNX），验证转换后的模型结构与预期一致。
*   开发者在部署模型前，通过可视化确认输入输出节点名称及数据类型，以便对接应用程序。
*   技术文档编写者利用其生成的结构图，直观地向非技术人员或团队成员解释算法原理。

4. **技术亮点**
*   **极致的兼容性**：原生支持 safetensors、TFLite 等较新的模型格式，覆盖范围远超同类工具。
*   **零依赖与轻量化**：基于 Electron 和 Node.js 构建，无需安装庞大的 Python 环境即可运行，启动速度快。
*   **开源透明**：完全开源且社区活跃，Star 数超过 3.3 万，证明了其在 AI 开发者群体中的高认可度和广泛使用率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33197 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必备的知识速查手册。它整合了相关领域的核心概念与实用技巧，旨在帮助研究人员快速回顾和查阅关键知识点。

2. **核心功能**
*   提供机器学习与深度学习领域的基础概念速查表。
*   涵盖常用Python库如NumPy、SciPy、Matplotlib及Keras的使用指南。
*   整理AI研究中的关键公式、算法流程及最佳实践。
*   以简洁清晰的格式呈现复杂的技术细节，便于快速检索。

3. **适用场景**
*   研究人员在复习基础理论或遗忘特定API用法时快速查阅。
*   数据科学家在项目初期搭建框架时参考常用代码片段。
*   学生或初学者学习深度学习核心概念时的辅助参考资料。
*   团队成员之间统一技术术语和实现标准时的共享文档。

4. **技术亮点**
*   高度集成化，将分散的AI工具链（从数据处理到模型构建）浓缩于单一资源中。
*   内容经过精选，专注于“必备”知识，避免冗余信息，提升查阅效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，涵盖从零基础入门到就业实战的全过程，整理了近200个精选实战案例。项目免费提供配套教材，内容广泛涉及 Python、数学基础、机器学习、深度学习及自然语言处理等热门技术领域。旨在帮助学习者系统掌握数据分析、计算机视觉等核心技能，顺利进入 AI 行业。

### 2. 核心功能
*   提供结构化的 AI 学习路径，覆盖数学、编程、算法及各大主流框架。
*   收录近 200 个实战案例与项目，强调动手能力和就业导向。
*   免费提供全套配套教材与学习资料，降低入门门槛。
*   整合 Python、PyTorch、TensorFlow 等主流工具链的教学资源。
*   包含数据分析、计算机视觉（CV）、自然语言处理（NLP）等细分领域指南。

### 3. 适用场景
*   零基础想进入人工智能或数据科学领域的初学者系统学习。
*   需要大量实战案例来巩固理论知识的在校大学生或转行人员。
*   寻求高质量免费教材和路线图以规划个人职业发展路径的学习者。
*   希望快速了解 AI 各细分领域（如 CV、NLP）核心技术与工具的技术爱好者。

### 4. 技术亮点
*   **资源丰富且免费**：汇集近 200 个实战项目及全套免费教材，性价比极高。
*   **覆盖面广**：从基础数学、Python 语法到前沿的深度学习框架（PyTorch/TensorFlow）均有所涉及。
*   **就业导向明确**：通过实战案例直接对接市场需求，注重“学以致用”和职业准备。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化工作流，降低了机器学习开发的门槛，使用户能更专注于数据-centric 的开发模式。

2. **核心功能**
*   **低代码开发**：支持通过简单的 YAML 配置文件快速定义和训练复杂的深度学习模型，无需编写大量底层代码。
*   **多模态支持**：原生支持文本、图像、音频、表格等多种数据类型，适用于计算机视觉和自然语言处理任务。
*   **预训练模型集成**：内置对 Hugging Face Transformers 等主流架构的支持，方便进行微调（Fine-tuning）和推理。
*   **端到端实验管理**：提供从数据预处理、模型训练到评估和部署的完整生命周期管理工具。

3. **适用场景**
*   **快速原型验证**：数据科学家希望在不深入代码细节的情况下，迅速验证特定数据集上的模型效果。
*   **企业级 AI 应用部署**：团队需要标准化、可复现的 ML 流水线，以便在 production 环境中稳定运行 LLM 或其他预测模型。
*   **多模态数据分析**：处理包含结构化表格与非结构化媒体（如图像或文本）混合数据的复杂业务场景。

4. **技术亮点**
*   **Data-Centric AI 优先**：强调数据质量与特征工程在模型性能中的核心作用，而非仅依赖算法调优。
*   **与 PyTorch/Hugging Face 深度兼容**：无缝衔接现有的 PyTorch 生态系统和海量的开源预训练模型资源。
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
- 1. **中文简介**
funNLP是一个全面且实用的中文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。它提供了丰富的中文词库资源（包括同义词、反义词、情感值、行业术语等）以及多种预训练模型和深度学习应用案例，旨在降低中文NLP的开发门槛。

2. **核心功能**
- **基础文本处理**：支持中英文敏感词过滤、语言检测、繁简体转换及中文分词加速。
- **实体与信息抽取**：提供手机号、身份证、邮箱、地址等正则匹配，以及基于BERT等模型的命名实体识别（NER）。
- **丰富词库资源**：内置大量中文专用词库，涵盖同/反义词、情感词典、行业术语（医疗、法律、汽车等）及停用词。
- **深度学习模型集成**：收录BERT、ALBERT、RoBERTa等预训练模型代码，以及文本分类、摘要生成、知识图谱构建等SOTA方案。
- **语音与多模态支持**：包含中文语音识别（ASR）、拼音转换、手写OCR及音频数据增强工具。

3. **适用场景**
- **内容安全审核**：用于互联网平台对UGC内容进行敏感词过滤、暴恐词检测及谣言识别。
- **智能客服与对话系统**：利用情感分析、意图识别和对话管理组件构建专业的中文聊天机器人或客服系统。
- **企业级信息抽取**：从非结构化文本（如简历、新闻、合同）中自动提取关键实体（人名、机构、地名）并构建知识图谱。
- **NLP研究与教学**：作为学习中文自然语言处理、对比不同算法模型（如BERT vs BiLSTM）及复现经典论文代码的资源库。

4. **技术亮点**
- **资源极度丰富**：不仅包含代码，还整合了海量高质量中文数据集、词库及学术报告，是中文NLP领域的“百科全书”。
- **全链路覆盖**：从底层的数据清洗、分词，到中层的情感分析、实体抽取，再到上层的知识图谱构建和对话生成，提供一站式解决方案。
- **紧跟前沿技术**：持续更新最新的预训练语言模型（如ELECTRA、ALBERT）和竞赛获奖方案，确保用户能接触到业界最先进的NLP实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81688 | 🍴 15253 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和多模态大模型（VLM）进行训练。它集成了指令微调、RLHF 及量化等先进技术，旨在降低大模型定制化的门槛并提升开发效率。该项目在 ACL 2024 会议上发表，体现了其在学术与工业界的认可度。

### 2. 核心功能
*   **多模型兼容**：支持 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流大模型的统一微调。
*   **全参数与高效微调**：提供从全参数微调到 LoRA/QLoRA 等多种轻量化微调策略，节省显存资源。
*   **对齐训练支持**：内置 RLHF（基于人类反馈的强化学习）及 DPO 等算法，优化模型输出质量与安全性。
*   **多模态能力**：不仅限于文本，还支持视觉语言模型（VLM）的微调，拓展应用场景。
*   **量化部署优化**：集成 4-bit/8-bit 量化技术，使低配置硬件也能流畅运行和微调大模型。

### 3. 适用场景
*   **企业私有化模型部署**：利用行业数据对开源基座模型进行指令微调，构建专属领域的垂直模型。
*   **学术研究实验**：快速验证不同 LLM/VLM 在特定数据集上的微调效果，比较各类 PEFT 算法性能。
*   **低成本模型适配**：在显存受限的消费级显卡上，通过 QLoRA 等技术高效微调大语言模型。
*   **多模态应用开发**：针对图文理解或生成任务，微调多模态大模型以适配具体的视觉业务需求。

### 4. 技术亮点
*   **统一接口设计**：通过标准化的配置文件和 API，屏蔽了不同模型架构之间的差异，实现“一键”切换微调目标。
*   **极致性能优化**：针对 Transformer 底层代码进行深度优化，显著提升训练吞吐量并降低显存占用。
*   **前沿算法集成**：无缝支持最新的微调范式（如 DPO、ORPO）及量化方案，保持技术栈的先进性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73087 | 🍴 8932 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. **中文简介**
该项目是一个定期更新的资源库，收集并提取了来自Anthropic、OpenAI、Google、xAI等主流厂商的高级模型（如Claude、ChatGPT、Gemini系列）以及各类AI代理工具的系统提示词。它致力于通过开源共享这些底层指令，帮助用户深入理解大型语言模型的内部工作机制与行为边界。

### 2. **核心功能**
*   **多厂商提示词聚合**：整合了Anthropic、OpenAI、Google及xAI等多个顶级AI提供商的模型系统提示。
*   **定期更新维护**：保持内容时效性，持续跟进最新发布的模型版本（如Claude Fable 5、GPT 5.5等）。
*   **透明化AI内部机制**：通过公开系统提示词，揭示大语言模型背后的指令集和约束条件。
*   **开源社区驱动**：作为Awesome列表的一部分，促进AI提示词工程领域的知识共享与教育。

### 3. **适用场景**
*   **提示词工程研究**：分析师或开发者通过对比不同模型的底层指令，优化自身的Prompt设计策略。
*   **AI安全与伦理评估**：研究人员利用这些提示词分析模型的安全护栏、偏见来源及潜在漏洞。
*   **教育与学习**：学生或初学者通过阅读真实的生产级系统提示，快速掌握LLM的工作原理。
*   **竞品技术分析**：企业技术团队监控竞争对手（如OpenAI vs Anthropic）的技术路线和指令差异。

### 4. **技术亮点**
*   **跨平台覆盖广**：不仅包含基础聊天机器人，还涵盖了Claude Code、Cursor、VS Code Copilot等专用开发工具和AI Agent。
*   **高关注度验证**：拥有超过5.4万星标，证明了其在AI社区中的极高实用价值和影响力。
*   **动态更新机制**：随着各大厂商发布新模型，项目能迅速同步最新的系统提示泄露或公开信息。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54105 | 🍴 8805 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. **中文简介**
该项目是一套为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。它由Microsoft For Beginners团队开发，涵盖了从机器学习基础到深度学习高级应用的完整学习路径。

### 2. **核心功能**
*   **系统化课程体系**：提供结构化的12周学习计划，每周包含理论讲解与实践练习。
*   **多模态内容支持**：主要使用Jupyter Notebook编写代码示例，便于交互式学习与调试。
*   **广泛的技术覆盖**：内容涵盖机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等核心领域。
*   **零基础友好设计**：专为初学者打造，降低AI入门门槛，适合非专业背景人员学习。
*   **微软官方背书**：作为Microsoft For Beginners系列的一部分，确保内容的权威性与准确性。

### 3. **适用场景**
*   **高校或培训机构教学**：教师可直接引用该课程大纲作为人工智能通识课的教学资源。
*   **企业员工技能培训**：帮助非技术岗位或初级开发人员快速理解并应用AI工具。
*   **个人自学入门**：对AI感兴趣的初学者通过12周的系统学习建立完整的知识框架。
*   **在线开源课程补充**：学习者可利用其提供的Notebook代码进行本地复现与实验。

### 4. **技术亮点**
*   **全栈AI技术图谱**：不仅包含传统机器学习，还深入讲解了CNN、RNN、GAN等现代深度学习架构。
*   **交互式实践导向**：通过Jupyter Notebook实现“边学边练”，强化代码实操能力而非纯理论记忆。
*   **社区驱动与持续更新**：拥有超过5万星标，表明其内容质量高且社区活跃，便于获取最新学习反馈。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51916 | 🍴 10484 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. 中文简介
该项目是一个全面的AI学习资源库，涵盖了从数据分析、机器学习基础到深度学习框架（如PyTorch和TensorFlow 2）及自然语言处理（NLTK）的完整知识体系。它不仅包含理论讲解（如线性代数），还通过代码实战演示了多种经典算法的实现。

### 2. 核心功能
- **全栈算法实现**：集成并实现了包括Adaboost、KMeans、SVM、Logistic回归、朴素贝叶斯等在内的数十种主流机器学习与深度学习算法。
- **多框架支持**：同时提供基于Scikit-learn的传统机器学习方案以及基于PyTorch和TensorFlow 2的深度学习和NLP实战代码。
- **理论结合实战**：将线性代数等数学基础理论与具体的编程实践相结合，帮助学习者深入理解算法背后的原理。
- **推荐系统与挖掘**：包含Apriori、FP-Growth等关联规则挖掘算法，以及PCA降维和推荐系统相关模块。

### 3. 适用场景
- **AI初学者入门**：适合希望系统掌握机器学习全流程（从数据预处理到模型评估）的新手进行从零开始的学习。
- **算法复现与参考**：为研究人员或工程师提供高质量、可运行的算法代码模板，用于快速复现经典论文中的方法。
- **面试准备与技能提升**：作为求职前的复习材料，帮助候选人巩固常见面试题涉及的算法细节和工程实现。

### 4. 技术亮点
- **高人气与社区验证**：拥有超过4万颗星，表明其内容质量、更新频率和社区认可度极高，是中文圈知名的AI学习标杆项目。
- **结构化的知识图谱**：标签覆盖了从基础统计学习到前沿深度学习的完整链条，逻辑清晰，便于按需检索和学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37656 | 🍴 6275 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33725 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28421 | 🍴 3455 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25850 | 🍴 2904 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22156 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16243 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12906 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11270 | 🍴 1196 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
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
- ⭐ 382210 | 🍴 80196 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 249768 | 🍴 22161 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211548 | 🍴 38886 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195711 | 🍴 59176 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185434 | 🍴 46121 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165098 | 🍴 21365 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164048 | 🍴 30398 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156893 | 🍴 46166 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151377 | 🍴 9474 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148208 | 🍴 23352 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

