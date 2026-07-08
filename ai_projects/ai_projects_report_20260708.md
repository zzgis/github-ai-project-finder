# GitHub AI项目每日发现报告
日期: 2026-07-08

## 新发布的AI项目

### Homekit
- ### 1. 中文简介
Homekit 是一款为 AI 智能体打造的工具，通过单一开放接口赋予其对 Apple Home 生态系统的直接物理控制权。它允许 AI 代理执行开关灯光、锁门以及读取传感器数据等实际操作，实现了智能家居与人工智能模型的无缝连接。

### 2. 核心功能
- **直接物理控制**：支持 AI 智能体直接操作 Apple Home 设备，如翻转灯光开关和锁定门锁。
- **传感器数据读取**：使 AI 能够实时获取智能家居环境中的传感器信息。
- **统一开放接口**：提供一个标准化的接口，简化 AI 与 Apple HomeKit 之间的交互复杂性。
- **多模型兼容**：支持 Claude、OpenClaw 等多种 AI 模型集成，适配不同开发需求。
- **CLI 与编辑器集成**：提供命令行界面及 Cursor 等代码编辑器的支持，便于开发者快速部署和使用。

### 3. 适用场景
- **高级智能家居自动化**：开发者利用 AI 构建比传统自动化更复杂的智能场景，如基于环境传感器数据自动调节家居状态。
- **AI 助手集成**：将 Apple Home 功能嵌入到个人 AI 助理中，让用户可以通过自然语言指令控制家中设备。
- **原型开发与测试**：研究人员或开发者在 macOS 环境下快速验证 AI 模型对物理 IoT 设备的控制逻辑。
- **MCP 协议实践**：使用 Model Context Protocol (MCP) 标准连接 AI 模型与外部工具的专业用户，实现上下文增强的智能交互。

### 4. 技术亮点
- 基于 TypeScript 和 Node.js 构建，确保类型安全和高性能。
- 遵循 Model Context Protocol (MCP) 标准，增强了 AI 模型与外部工具集成的通用性和互操作性。
- 轻量级且专注于单一功能领域（Apple Home），降低了集成门槛。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### fox-ai-roundtable
- 1. **中文简介**
该项目允许用户通过本地命令行接口（CLI），仅输入一次提示词即可同时向 Claude、Codex (GPT) 和 Antigravity (Gemini) 三个模型发起请求。它旨在提供一个统一的交互界面，方便对比不同 AI 模型对同一问题的回答差异。

2. **核心功能**
*   支持通过本地 CLI 同时调用 Claude、OpenAI Codex/GPT 及 Google Gemini 模型。
*   实现“一次提问，三份回答”的高效并行处理机制。
*   提供统一的命令行入口，简化多模型 API 的使用流程。
*   基于 HTML 构建前端或配置结构（注：作为 CLI 工具，HTML 可能用于生成报告或极简 UI）。
*   无需切换不同客户端，直接在终端内完成多模型交互。

3. **适用场景**
*   **模型效果对比测试**：开发者或研究者快速比较不同大模型在同一任务上的输出质量和风格差异。
*   **多模型工作流集成**：在需要综合多个模型优势以生成更优结果的技术分析场景中，快速收集多方反馈。
*   **日常创意头脑风暴**：用户希望从不同角度获取灵感时，一次性获得来自不同 AI 助手的多样化建议。

4. **技术亮点**
*   **统一接口抽象**：通过本地 CLI 封装不同厂商复杂的 API 调用逻辑，降低多模型使用门槛。
*   **并行请求优化**：设计上强调“Ask once, get three”，隐含了对并发请求和结果聚合的处理能力。
- 链接: https://github.com/PeterPanSwift/fox-ai-roundtable
- ⭐ 63 | 🍴 9 | 语言: HTML

### seedance-prompt
- 描述: Hermes skill for realistic AI video prompts for Seedance and text-to-video models.
- 链接: https://github.com/zhouwei713/seedance-prompt
- ⭐ 50 | 🍴 9 | 语言: 未知

### blockout
- 1. **中文简介**
Blockout 是一款专为 AI 原生电影制作设计的预可视化（Previs）工具。它允许用户搭建灰盒场景、编排摄像机运动及角色走位，并导出用于 Seedance、Veo、Kling 等 AI 视频生成模型的运动参考包。该项目采用 Apache-2.0 开源协议。

2. **核心功能**
- 支持搭建灰盒场景以进行初步视觉构思。
- 提供摄像机运动与角色标记（Marks）的编排功能。
- 能够导出标准化的运动参考数据包。
- 兼容多种主流 AI 视频生成平台（如 Seedance、Veo、Kling、LTX、Wan）。

3. **适用场景**
- AI 视频生成前的镜头规划与分镜预演。
- 复杂摄像机轨迹与角色动作的协同排练。
- 为不同 AI 视频模型准备精确的运动控制数据。

4. **技术亮点**
- 聚焦于“运动参考”标准化，打通了传统预可视化与新兴 AI 视频生成工作流的壁垒。
- 链接: https://github.com/wassermanproductions/blockout
- ⭐ 50 | 🍴 6 | 语言: TypeScript

### openclaw-voice-call-realtime
- ### 1. **中文简介**
OpenClaw 是一个支持通过 Twilio 和 OpenAI Realtime API 进行真实电话通话的插件，旨在赋予 AI 助手拨打电话的能力。它集成了通话中的工具调用、实时转录以及来电筛选等功能，实现了从文本交互到语音通信的自然延伸。

### 2. **核心功能**
*   基于 Twilio 和 OpenAI Realtime 实现低延迟的真实电话语音交互。
*   在通话过程中动态执行工具调用（如查询数据、控制设备等）。
*   自动生成并保存通话的文字转录记录，便于后续回顾与分析。
*   提供智能来电筛选机制，帮助过滤垃圾电话或优先处理重要联系人。

### 3. **适用场景**
*   **自动化客服系统**：利用 AI 代理自动接听客户咨询电话，处理常见查询并提供即时帮助。
*   **个人助理外呼服务**：为高端用户或企业高管提供日程提醒、会议通知等主动式语音通知服务。
*   **紧急通知与监控**：在智能家居或物联网场景中，当检测到异常时通过真实电话向用户发出紧急语音警报。

### 4. **技术亮点**
*   **无缝集成生态**：作为 OpenClaw 插件运行，轻松嵌入现有的 AI Agent 工作流中。
*   **实时双向交互**：结合 OpenAI 的实时音频处理能力，确保语音对话的流畅性与低延迟体验。
*   **全链路自动化**：从呼叫建立、内容生成到事后转录归档，实现了完整的语音业务闭环。
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
- ### 1. 中文简介
funNLP 是一个功能极其丰富的中文自然语言处理工具包，集成了敏感词检测、分词、实体抽取、情感分析及多种专业领域的词库资源。它不仅提供了基础的文本处理功能（如繁简转换、拼音标注），还涵盖了从基础语言学特征到高级深度学习模型（如 BERT、GPT-2）的广泛应用场景。该项目旨在为开发者提供一个一站式的中英文 NLP 资源中心，涵盖数据、算法、模型及行业专属知识库。

### 2. 核心功能
*   **基础文本处理**：支持中英文敏感词过滤、语言检测、分词、词性标注、句法分析、繁简转换及标点修复。
*   **实体与信息抽取**：提供手机号、身份证、邮箱、人名、地名、组织机构名等关键信息的抽取，以及命名实体识别（NER）和关系抽取。
*   **领域专属词库与数据**：内置大量垂直领域词库（如汽车、医疗、法律、金融、IT）及多语言人名库、成语、古诗词等资源，支持细粒度的情感分析和语义消歧。
*   **深度学习模型集成**：汇总并整合了 BERT、ALBERT、RoBERTa、GPT-2 等预训练模型的中文变体，支持文本分类、序列标记、摘要生成及问答系统构建。
*   **语音与知识图谱应用**：包含语音识别（ASR）语料与工具、中文 OCR 识别、知识图谱构建与问答系统，以及语音情感分析和音素对齐工具。

### 3. 适用场景
*   **内容安全审核**：互联网平台利用敏感词库和情感分析功能，自动识别和过滤违规、暴恐或不当言论。
*   **智能客服与对话系统**：开发者基于其提供的意图识别、槽位填充（实体抽取）及对话管理组件，快速构建具备领域知识（如医疗、金融）的智能问答机器人。
*   **文本挖掘与分析**：研究人员或分析师利用其丰富的词向量、情感词典及文本摘要工具，对社交媒体评论、新闻报道进行大规模的情感倾向分析和热点挖掘。
*   **OCR 与语音交互开发**：利用其中的中文 OCR 工具、语音识别数据集及音频增强库，开发支持中文手写识别、语音转文字及语音合成的智能应用。

### 4. 技术亮点
*   **资源聚合性强**：不仅是工具库，更是 NLP 资源的“百科全书”，涵盖了从传统规则方法到前沿 Transformer 模型的完整技术栈。
*   **垂直领域覆盖深**：特别强化了医疗、法律、金融、汽车等行业的专用术语库和知识图谱数据，降低了特定领域落地的数据准备成本。
*   **多模态支持**：同时兼顾文本、语音（ASR/TTS）及图像（OCR）处理，适合构建复杂的 multimodal 智能应用。
*   **开源生态整合**：集成了大量知名开源项目（如 SpaCy、Jieba、Transformers 的中文适配版），并提供详细的基准测试和排行榜，便于选型和评估。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81688 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供丰富的实战案例，涵盖从基础算法到前沿应用的完整学习路径。通过整合多个细分领域的开源项目，它成为了一个极具价值的机器学习资源库。

**2. 核心功能**
*   汇集500个经过筛选的AI相关开源项目，覆盖主流技术栈。
*   分类明确，细分为机器学习、深度学习、计算机视觉和自然语言处理四大领域。
*   所有项目均附带源代码，支持直接下载、运行和学习参考。
*   提供“Awesome”级别的精选列表，确保项目质量高且社区活跃。

**3. 适用场景**
*   **学生与初学者学习**：作为课程补充材料，通过阅读和运行代码深入理解AI概念。
*   **开发者原型验证**：快速寻找现成的解决方案或代码片段，加速项目开发进程。
*   **技术调研与趋势分析**：了解当前AI领域热门项目和技术方向，把握行业前沿动态。
*   **面试准备**：通过研究高质量的项目实现，提升对算法原理和工程实践的掌握程度。

**4. 技术亮点**
*   **资源规模庞大**：收录500个项目，远超一般列表型仓库，覆盖面广。
*   **跨领域整合**：同时囊括CV、NLP和传统ML，适合综合性AI技能提升。
*   **高社区认可度**：拥有超过3.5万Star，证明其内容质量和实用性得到广泛验证。
*   **标签化清晰**：使用标准化的技术标签，便于用户根据具体需求快速检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的通用工具。它支持多种主流框架和文件格式，能够直观地展示模型结构。该工具旨在帮助开发者和研究人员更好地理解和调试复杂的模型架构。

2. **核心功能**
*   支持 TensorFlow、PyTorch、ONNX、Keras、CoreML、TensorFlow Lite 等多种流行框架模型格式的读取与解析。
*   提供清晰的图形化界面，直观展示神经网络的层结构、连接关系及数据流向。
*   允许用户通过交互式界面检查模型参数、权重分布及中间张量的形状信息。
*   具备跨平台特性，既可作为独立桌面应用运行，也可嵌入浏览器中使用。

3. **适用场景**
*   深度学习工程师在模型开发阶段，用于快速验证网络结构的正确性。
*   研究人员在复现论文或调试模型时，通过分析可视化图来定位潜在的结构错误。
*   团队在进行模型部署前，用于向非技术背景的成员展示和解释模型的基本架构。
*   开发者在转换模型格式（如从 PyTorch 转为 ONNX）后，用于确认转换结果是否保留了原始结构。

4. **技术亮点**
*   **广泛的兼容性**：几乎涵盖了当前所有主流的 AI 框架和标准格式（包括新兴的 safetensors）。
*   **轻量级与易用性**：无需安装庞大的依赖环境，即可快速启动并加载模型文件进行分析。
*   **开源与社区驱动**：作为高星开源项目，拥有活跃的社区支持和持续的功能更新。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33196 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换与兼容。它允许开发者在 PyTorch、TensorFlow 和 Keras 等主流框架间无缝迁移模型，打破生态壁垒。

**2. 核心功能**
*   提供统一的模型表示格式，实现跨框架的模型交换。
*   支持从训练环境到推理环境的无缝部署转换。
*   集成多种主流深度学习框架的转换器（如 PyTorch、TensorFlow）。
*   定义标准化的算子集，确保模型在不同运行时中的一致性。

**3. 适用场景**
*   **跨平台部署**：将基于 Python 训练好的模型转换为适合 C++ 或嵌入式设备运行的格式。
*   **框架迁移**：在开发过程中自由切换训练框架，而无需重新训练模型。
*   **混合系统集成**：在由不同技术栈组件构成的系统中，统一模型的输入输出接口。

**4. 技术亮点**
*   **开源中立性**：由微软、Facebook 等科技巨头共同维护，避免厂商锁定。
*   **高性能推理支持**：通过 ONNX Runtime 提供优化的推理引擎，加速模型执行。
- 链接: https://github.com/onnx/onnx
- ⭐ 21116 | 🍴 3961 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ML Engineering Open Book》是一本关于机器学习工程的开源指南，旨在填补深度学习训练与推理领域的实践知识空白。该项目由 Andrew 等人维护，系统性地总结了大规模模型工程中的关键技术与最佳实践。

2. **核心功能**
*   深入解析大规模分布式训练策略，涵盖数据并行、模型并行及张量并行等架构。
*   提供高效的模型推理优化方案，包括量化、编译加速及低延迟部署技巧。
*   详细讲解底层基础设施配置，涉及 GPU 集群管理、网络通信优化及存储系统调优。
*   分享故障排查与调试经验，帮助工程师解决训练过程中的常见错误与性能瓶颈。
*   整合 Hugging Face Transformers 与 PyTorch 生态系统的工程化应用实例。

3. **适用场景**
*   需要从零搭建或优化大规模 LLM（大语言模型）训练集群的 MLOps 工程师。
*   致力于降低生产环境中模型推理成本并提升响应速度的后端开发团队。
*   希望系统化掌握深度学习硬件加速、网络拓扑及分布式计算原理的研究人员。
*   正在构建高性能机器学习平台，需参考业界最佳实践以制定技术标准的架构师。

4. **技术亮点**
该项目不仅涵盖理论，更侧重于实际工程落地，特别是针对当前流行的 Transformer 架构和 GPU 硬件特性提供了详尽且可操作的优化指南。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18265 | 🍴 1159 | 语言: Python
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
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供丰富的实战案例，涵盖从基础算法到前沿应用的完整学习路径。通过整合多个细分领域的开源项目，它成为了一个极具价值的机器学习资源库。

**2. 核心功能**
*   汇集500个经过筛选的AI相关开源项目，覆盖主流技术栈。
*   分类明确，细分为机器学习、深度学习、计算机视觉和自然语言处理四大领域。
*   所有项目均附带源代码，支持直接下载、运行和学习参考。
*   提供“Awesome”级别的精选列表，确保项目质量高且社区活跃。

**3. 适用场景**
*   **学生与初学者学习**：作为课程补充材料，通过阅读和运行代码深入理解AI概念。
*   **开发者原型验证**：快速寻找现成的解决方案或代码片段，加速项目开发进程。
*   **技术调研与趋势分析**：了解当前AI领域热门项目和技术方向，把握行业前沿动态。
*   **面试准备**：通过研究高质量的项目实现，提升对算法原理和工程实践的掌握程度。

**4. 技术亮点**
*   **资源规模庞大**：收录500个项目，远超一般列表型仓库，覆盖面广。
*   **跨领域整合**：同时囊括CV、NLP和传统ML，适合综合性AI技能提升。
*   **高社区认可度**：拥有超过3.5万Star，证明其内容质量和实用性得到广泛验证。
*   **标签化清晰**：使用标准化的技术标签，便于用户根据具体需求快速检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的通用工具。它支持多种主流框架和文件格式，能够直观地展示模型结构。该工具旨在帮助开发者和研究人员更好地理解和调试复杂的模型架构。

2. **核心功能**
*   支持 TensorFlow、PyTorch、ONNX、Keras、CoreML、TensorFlow Lite 等多种流行框架模型格式的读取与解析。
*   提供清晰的图形化界面，直观展示神经网络的层结构、连接关系及数据流向。
*   允许用户通过交互式界面检查模型参数、权重分布及中间张量的形状信息。
*   具备跨平台特性，既可作为独立桌面应用运行，也可嵌入浏览器中使用。

3. **适用场景**
*   深度学习工程师在模型开发阶段，用于快速验证网络结构的正确性。
*   研究人员在复现论文或调试模型时，通过分析可视化图来定位潜在的结构错误。
*   团队在进行模型部署前，用于向非技术背景的成员展示和解释模型的基本架构。
*   开发者在转换模型格式（如从 PyTorch 转为 ONNX）后，用于确认转换结果是否保留了原始结构。

4. **技术亮点**
*   **广泛的兼容性**：几乎涵盖了当前所有主流的 AI 框架和标准格式（包括新兴的 safetensors）。
*   **轻量级与易用性**：无需安装庞大的依赖环境，即可快速启动并加载模型文件进行分析。
*   **开源与社区驱动**：作为高星开源项目，拥有活跃的社区支持和持续的功能更新。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33196 | 🍴 3152 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目为深度学习与机器学习研究人员提供了 Essential（核心/必备）的知识速查表。内容涵盖了从基础库到高级算法的关键概念与语法参考，旨在帮助研究者快速回顾和查阅核心技术细节。

**2. 核心功能**
*   提供针对 NumPy、SciPy、Matplotlib 等基础数据科学库的代码示例与函数速查。
*   整理 Keras 等主流深度学习框架的核心 API 使用指南与最佳实践。
*   归纳机器学习算法中的关键数学公式、优化器特性及模型评估指标。
*   以简洁的笔记形式呈现复杂概念，便于快速记忆与现场查阅。

**3. 适用场景**
*   研究人员在实验前快速复习特定库或算法的参数配置与用法。
*   面试准备过程中，作为机器学习核心知识点的高频考点梳理工具。
*   日常编码遇到遗忘的 API 细节时，作为轻量级的在线参考手册。
*   初学者系统性地构建对深度学习技术栈的整体认知框架。

**4. 技术亮点**
*   高度浓缩的知识密度，去除了冗余解释，直击核心代码与逻辑。
*   涵盖范围广，从底层数值计算到高层神经网络架构均有涉及。
*   社区贡献度高（高星标），内容经过大量开发者验证，准确性较强。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3387 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. **中文简介**
Ai-Learn 是一个零基础的AI学习路线图，整理了近200个实战案例与项目，并免费提供配套教材。该项目涵盖从Python基础、数学原理到机器学习、深度学习及自然语言处理等热门领域的完整知识体系，旨在助力用户通过就业实战掌握人工智能技能。

### 2. **核心功能**
*   提供结构化的AI学习路径，涵盖Python、数学、机器学习、深度学习等全栈知识。
*   收录近200个精选实战案例和项目，强调“零基础入门”与“就业导向”。
*   免费开放配套教材和学习资源，降低人工智能学习门槛。
*   整合主流框架与技术栈，包括TensorFlow、PyTorch、Keras、Caffe以及Pandas、NumPy等数据处理库。
*   覆盖计算机视觉（CV）、自然语言处理（NLP）和数据挖掘等细分热门领域。

### 3. **适用场景**
*   **零基础转行**：希望从零开始系统学习人工智能，寻求清晰学习路线和实战项目的初学者。
*   **求职准备**：需要积累高质量实战项目经验，以增强简历竞争力并准备AI相关岗位面试的求职者。
*   **技能查漏补缺**：已经具备一定基础，希望系统化梳理机器学习、深度学习理论及主流框架应用的技术人员。
*   **自学参考指南**：寻找免费、全面且包含大量代码示例和教程的AI学习资源库的个人开发者或学生。

### 4. **技术亮点**
*   **资源高度集成**：将分散的学习资源（教材、代码、路线图）整合在一个仓库中，极大提升了学习效率。
*   **实战驱动教学**：通过近200个真实案例，让用户在动手实践中理解复杂的算法和模型。
*   **技术栈广泛兼容**：同时支持TensorFlow 1/2、PyTorch、Keras等多个主流深度学习框架，适应不同技术偏好。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **项目名称**：Ludwig

1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大型语言模型（LLM）、神经网络及其他人工智能模型。它简化了从数据处理到模型训练、评估及部署的全流程，降低了 AI 开发的门槛。

2. **核心功能**
*   提供声明式配置方式，无需编写大量代码即可定义和训练机器学习模型。
*   支持多种数据类型（文本、图像、数值等），适用于自然语言处理及计算机视觉任务。
*   内置对主流深度学习框架（如 PyTorch）的支持，方便进行微调（Fine-tuning）和预训练模型集成。
*   包含完整的数据科学工作流工具链，涵盖数据预处理、模型评估及可视化分析。

3. **适用场景**
*   快速原型开发：数据科学家希望在不深入底层代码的情况下，迅速验证机器学习想法。
*   企业级 AI 应用部署：需要标准化、可重复且易于维护的模型训练与推理管道。
*   多模态学习研究：涉及结合文本、图像和其他结构化数据进行综合分析的研究项目。
*   大模型微调：利用预训练基础模型（如 LLaMA、Mistral）针对特定领域数据进行高效微调。

4. **技术亮点**
*   **低代码/无代码体验**：通过 YAML 配置文件驱动模型构建，极大提升开发效率。
*   **Data-Centric AI 支持**：强调数据质量对模型性能的影响，提供强大的数据清洗和分析工具。
*   **广泛的生态兼容性**：无缝集成 Hugging Face 模型库，支持最新的 LLM 架构和前沿算法。
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
- ### 1. 中文简介
funNLP 是一个功能极其丰富的中文自然语言处理工具包，集成了敏感词检测、分词、实体抽取、情感分析及多种专业领域的词库资源。它不仅提供了基础的文本处理功能（如繁简转换、拼音标注），还涵盖了从基础语言学特征到高级深度学习模型（如 BERT、GPT-2）的广泛应用场景。该项目旨在为开发者提供一个一站式的中英文 NLP 资源中心，涵盖数据、算法、模型及行业专属知识库。

### 2. 核心功能
*   **基础文本处理**：支持中英文敏感词过滤、语言检测、分词、词性标注、句法分析、繁简转换及标点修复。
*   **实体与信息抽取**：提供手机号、身份证、邮箱、人名、地名、组织机构名等关键信息的抽取，以及命名实体识别（NER）和关系抽取。
*   **领域专属词库与数据**：内置大量垂直领域词库（如汽车、医疗、法律、金融、IT）及多语言人名库、成语、古诗词等资源，支持细粒度的情感分析和语义消歧。
*   **深度学习模型集成**：汇总并整合了 BERT、ALBERT、RoBERTa、GPT-2 等预训练模型的中文变体，支持文本分类、序列标记、摘要生成及问答系统构建。
*   **语音与知识图谱应用**：包含语音识别（ASR）语料与工具、中文 OCR 识别、知识图谱构建与问答系统，以及语音情感分析和音素对齐工具。

### 3. 适用场景
*   **内容安全审核**：互联网平台利用敏感词库和情感分析功能，自动识别和过滤违规、暴恐或不当言论。
*   **智能客服与对话系统**：开发者基于其提供的意图识别、槽位填充（实体抽取）及对话管理组件，快速构建具备领域知识（如医疗、金融）的智能问答机器人。
*   **文本挖掘与分析**：研究人员或分析师利用其丰富的词向量、情感词典及文本摘要工具，对社交媒体评论、新闻报道进行大规模的情感倾向分析和热点挖掘。
*   **OCR 与语音交互开发**：利用其中的中文 OCR 工具、语音识别数据集及音频增强库，开发支持中文手写识别、语音转文字及语音合成的智能应用。

### 4. 技术亮点
*   **资源聚合性强**：不仅是工具库，更是 NLP 资源的“百科全书”，涵盖了从传统规则方法到前沿 Transformer 模型的完整技术栈。
*   **垂直领域覆盖深**：特别强化了医疗、法律、金融、汽车等行业的专用术语库和知识图谱数据，降低了特定领域落地的数据准备成本。
*   **多模态支持**：同时兼顾文本、语音（ASR/TTS）及图像（OCR）处理，适合构建复杂的 multimodal 智能应用。
*   **开源生态整合**：集成了大量知名开源项目（如 SpaCy、Jieba、Transformers 的中文适配版），并提供详细的基准测试和排行榜，便于选型和评估。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81688 | 🍴 15253 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目旨在简化多模态大模型的微调流程，提供从指令微调到强化学习人类反馈（RLHF）的一站式解决方案。

### 2. 核心功能
*   **广泛模型支持**：兼容 Llama、Qwen、Gemma、DeepSeek 等 100+ 种主流开源大模型。
*   **高效微调算法**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调（PEFT）方法，降低显存需求。
*   **全栈训练能力**：支持 SFT（监督微调）、RLHF（基于人类反馈的强化学习）及 DPO（直接偏好优化）。
*   **量化与部署集成**：原生支持 GPTQ、AWQ 等量化技术，并与 Transformers、vLLM 等推理库无缝对接。
*   **模块化架构设计**：采用统一接口管理不同架构模型，简化配置过程，提升开发效率。

### 3. 适用场景
*   **企业级定制开发**：利用自有数据对特定领域（如医疗、法律）的大模型进行指令微调。
*   **学术研究实验**：快速复现或对比不同微调算法（如 LoRA vs QLoRA）在多种模型上的性能表现。
*   **多模态应用构建**：训练具备图像理解能力的视觉语言模型（VLM），用于图文问答或内容生成。
*   **低资源环境部署**：通过量化和 PEFT 技术在消费级显卡上高效运行大规模模型微调任务。

### 4. 技术亮点
*   **ACL 2024 收录**：作为经过学术验证的高质量项目，其技术架构具有权威性和可靠性。
*   **统一高效接口**：无需为每种新模型编写单独代码，极大降低了多模型维护的复杂度。
*   **极致显存优化**：结合 QLoRA 等技术，可在极低显存配置下微调超大参数模型。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73087 | 🍴 8932 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目汇集了从Anthropic、OpenAI、Google及xAI等主流厂商的最新大模型（如Claude、GPT、Gemini系列）中提取的系统提示词（System Prompts）。内容涵盖ChatGPT、Claude Code、Cursor等多个知名AI产品及工具，并定期更新以反映最新的技术细节。

2. **核心功能**
- 收集并整理了来自多个顶级AI模型和开发工具的系统提示词模板。
- 提供对主流大语言模型底层指令结构的透明化访问。
- 保持高频更新，确保获取最新的模型行为特征和提示词变化。

3. **适用场景**
- **提示词工程研究**：通过分析官方系统提示词，深入理解不同模型的指令遵循逻辑和边界约束。
- **AI代理（Agent）开发**：借鉴现有优秀模型的Prompt设计模式，优化自定义AI Agent的系统指令以提高稳定性。
- **安全与红队测试**：了解模型默认的安全限制和行为准则，辅助进行更精准的对抗性测试或越狱攻击研究。

4. **技术亮点**
- 覆盖范围极广，不仅包含基础聊天模型，还囊括了代码助手（如Copilot、Cursor）和特定领域模型。
- 由社区驱动并保持实时更新，是追踪生成式AI最新“内部机制”变化的重要开源资源库。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54068 | 🍴 8800 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能通识教育课程，旨在让所有人轻松入门AI领域。该项目由微软发起，通过Jupyter Notebook提供互动式学习体验，覆盖从基础机器学习到深度学习的核心概念。

2. **核心功能**
*   提供结构化的12周学习计划，每周一课共24次课程，适合系统化自学。
*   涵盖广泛的技术主题，包括机器学习、计算机视觉（CNN）、自然语言处理（RNN）、生成对抗网络（GAN）及深度学习基础。
*   采用Jupyter Notebook作为主要载体，支持代码即时运行与交互式实验，降低动手门槛。
*   面向初学者设计，内容通俗易懂，强调“人人可学AI”的理念，无需深厚的数学或编程背景。

3. **适用场景**
*   零基础用户希望系统性地了解人工智能基本概念和应用场景。
*   教育机构或企业团队用于开展短期AI科普培训或内部技术分享。
*   学生或转行者希望通过实践项目快速掌握ML/DL的基础开发技能。
*   对特定AI领域（如NLP或CV）感兴趣的学习者寻找入门级的代码示例和教程。

4. **技术亮点**
*   由微软开源社区维护，内容权威且更新及时，拥有极高的社区关注度（5万+星标）。
*   标签体系完整，明确区分了ML、DL、CV、NLP等不同技术栈的学习路径。
*   强调“做中学”，通过实际代码案例而非纯理论讲解来巩固知识点。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51916 | 🍴 10484 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解线性代数、PyTorch及TensorFlow 2等核心工具。它结合NLTK进行自然语言处理研究，旨在通过理论与实践相结合的方式提升用户的人工智能技术能力。

2. **核心功能**
- 提供从基础算法到深度学习的完整机器学习实战案例。
- 集成PyTorch和TensorFlow 2框架进行深度学习模型开发。
- 包含NLTK库用于自然语言处理（NLP）任务的处理与分析。
- 梳理线性代数等数学基础以支撑算法理解。
- 覆盖分类、聚类、回归等多种经典算法的实现。

3. **适用场景**
- 希望系统掌握机器学习理论与代码实现的初学者。
- 需要参考实战案例来优化现有AI模型的开发者。
- 专注于自然语言处理方向的技术研究人员。
- 想要深入理解深度学习底层数学原理的学习者。

4. **技术亮点**
- 广泛支持多种主流算法（如SVM、KMeans、LSTM、Adaboost等）。
- 同时兼容Scikit-learn传统机器学习库与现代PyTorch/TF2深度学习框架。
- 标签体系丰富，清晰映射了从数据处理到高级建模的全流程技术栈。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37653 | 🍴 6273 | 语言: Python
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
- ⭐ 25850 | 🍴 2903 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目旨在为开发者提供丰富的实战案例，涵盖从基础算法到前沿应用的完整学习路径。通过整合多个细分领域的开源项目，它成为了一个极具价值的机器学习资源库。

**2. 核心功能**
*   汇集500个经过筛选的AI相关开源项目，覆盖主流技术栈。
*   分类明确，细分为机器学习、深度学习、计算机视觉和自然语言处理四大领域。
*   所有项目均附带源代码，支持直接下载、运行和学习参考。
*   提供“Awesome”级别的精选列表，确保项目质量高且社区活跃。

**3. 适用场景**
*   **学生与初学者学习**：作为课程补充材料，通过阅读和运行代码深入理解AI概念。
*   **开发者原型验证**：快速寻找现成的解决方案或代码片段，加速项目开发进程。
*   **技术调研与趋势分析**：了解当前AI领域热门项目和技术方向，把握行业前沿动态。
*   **面试准备**：通过研究高质量的项目实现，提升对算法原理和工程实践的掌握程度。

**4. 技术亮点**
*   **资源规模庞大**：收录500个项目，远超一般列表型仓库，覆盖面广。
*   **跨领域整合**：同时囊括CV、NLP和传统ML，适合综合性AI技能提升。
*   **高社区认可度**：拥有超过3.5万Star，证明其内容质量和实用性得到广泛验证。
*   **标签化清晰**：使用标准化的技术标签，便于用户根据具体需求快速检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35271 | 🍴 7340 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22157 | 🍴 2073 | 语言: Python
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
- ⭐ 382205 | 🍴 80195 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 249747 | 🍴 22160 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211537 | 🍴 38879 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195704 | 🍴 59175 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185435 | 🍴 46121 | 语言: Python
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

