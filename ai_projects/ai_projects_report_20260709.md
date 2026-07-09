# GitHub AI项目每日发现报告
日期: 2026-07-09

## 新发布的AI项目

### lapian-notes
- ### 1. 中文简介
lapian-notes 是一款利用 AI 辅助进行电影“拉片”分析的笔记工具，旨在帮助创作者深入解构影片。它支持本地视频抽帧、剧情泳道时间轴、结构树及情绪曲线可视化等功能。通过段落深度拆解，为用户提供了从宏观结构到微观细节的全方位影视分析体验。

### 2. 核心功能
*   **AI 辅助分析**：利用人工智能技术自动化处理和分析电影内容，提升拉片效率。
*   **本地抽帧与时间轴**：支持在本地对视频进行抽帧，并生成剧情泳道时间轴以梳理叙事脉络。
*   **多维数据可视化**：提供结构树展示故事框架，以及情绪曲线描绘观众情感波动。
*   **段落深度拆解**：允许用户对电影段落进行细粒度分析和笔记记录。

### 3. 适用场景
*   **影视专业学生/研究者**：用于深入研读经典影片，学习叙事结构和视听语言。
*   **编剧与导演**：在剧本创作或筹备阶段，通过分析对标影片的结构和节奏优化自身作品。
*   **影评人/自媒体创作者**：快速生成高质量的拉片笔记，制作深度影视解说内容。

### 4. 技术亮点
*   **前端技术栈现代**：基于 React 和 Vite 构建，保证了良好的开发体验和性能。
*   **全栈 TypeScript 支持**：使用 TypeScript 开发，提升了代码的可维护性和类型安全性。
*   **本地化处理能力**：强调本地抽帧，可能在一定程度上保护用户隐私并减少对云端算力的依赖。
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 115 | 🍴 19 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### Homekit
- 1. **中文简介**
Homekit 为 AI 智能体提供了直接控制 Apple Home 物理设备的接口，支持开关灯光、锁门及读取传感器数据等功能。它通过单一开放接口实现这一能力，让智能体能够无缝集成并操作苹果智能家居生态。

2. **核心功能**
- 赋予 AI 智能体对 Apple Home 设备的直接物理控制权。
- 支持基础家居操作，如切换灯光状态和门锁控制。
- 具备实时读取环境传感器数据的能力。
- 提供统一的开放接口以简化多模型集成。

3. **适用场景**
- 开发者希望构建能直接操控家庭硬件的自主 AI 助手。
- 用户希望在 Claude、Cursor 或 OpenClaw 等工具中集成智能家居自动化功能。
- 研究或应用 Model Context Protocol (MCP) 以增强本地物理世界交互能力的场景。
- 基于 macOS 环境开发需要与苹果生态系统深度联动的智能应用。

4. **技术亮点**
- 采用 TypeScript 开发，确保类型安全与良好的开发者体验。
- 原生支持 Model Context Protocol (MCP)，便于与现代 AI 代理框架兼容。
- 轻量级 CLI 工具设计，方便集成到 Cursor、Claude Code 等开发环境中。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### ditto
- **1. 中文简介**
Ditto 是一款基于 Python 的工具，旨在挖掘用户在使用 Claude Code 和 Codex 等 AI 编码助手时产生的本地日志数据。它通过分析这些交互记录，自动生成并维护一个名为 `you.md` 的个人代理配置文件，从而构建个性化的 AI 记忆库。该项目致力于实现“本地优先”的数据处理模式，帮助用户在保持隐私的同时优化 AI 助手的上下文理解能力。

**2. 核心功能**
*   **日志挖掘与分析**：自动读取并解析 Claude Code 和 Codex 的历史对话与操作日志。
*   **个人画像生成**：将挖掘到的信息转化为结构化的 `you.md` 配置文件，记录用户的偏好、技能和上下文。
*   **本地化隐私保护**：所有数据处理均在本地完成，无需上传敏感代码或对话记录至云端。
*   **Agent 记忆增强**：为 AI 代理提供持久化的短期/长期记忆，使其能更准确地适应用户的开发习惯。

**3. 适用场景**
*   **提升 AI 编码助手效率**：开发者希望 AI 记住之前的代码风格和项目背景，减少重复解释上下文的时间。
*   **构建个性化开发工作流**：用户希望将多个 AI 工具（如 Cursor、Claude）的使用习惯整合为一个统一的个人知识库。
*   **敏感数据本地化处理**：在涉及专有代码或商业机密时，拒绝使用依赖云端记忆的 AI 服务，转而采用本地存储方案。

**4. 技术亮点**
*   **Context Engineering（上下文工程）**：通过精细化的日志处理，将非结构化的对话历史转化为高质量的 LLM 上下文输入。
*   **Local-First Architecture**：强调数据主权，确保用户完全控制自己的记忆数据和配置文件。
- 链接: https://github.com/ohad6k/ditto
- ⭐ 63 | 🍴 8 | 语言: Python
- 标签: agent-memory, agent-skills, ai, ai-agents, ai-coding

### fintech-advisor
- 1. **中文简介**
该项目是一个基于人工智能的金融科技财务顾问工具，旨在为投资者的投资组合提供智能分析与建议。它利用AI技术辅助用户进行金融决策，提升投资管理的效率与准确性。

2. **核心功能**
*   提供基于AI的投资组合分析与财务建议。
*   整合金融科技领域的前沿模型以优化决策流程。
*   支持 TypeScript 开发，便于集成到现有前端或全栈应用中。
*   专注于自动化财务咨询，降低个人理财门槛。
*   通过标签化分类，明确指向 AI 驱动的 Fintech 解决方案。

3. **适用场景**
*   个人投资者希望获得智能化的资产配置建议时。
*   金融科技公司需要嵌入 AI 顾问功能以增强用户体验。
*   开发者构建基于 TypeScript 的金融科技应用原型。
*   需要自动化初步财务诊断和分析工具的场景。

4. **技术亮点**
*   采用 TypeScript 编写，具备类型安全和高可维护性。
*   深度集成 AI 技术，实现智能化的财务数据分析与建议生成。
- 链接: https://github.com/KORAYTEACHER/fintech-advisor
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai, ai-advisor, ai-financial, ai-fintech, fintech

### FinTech-Solution
- ### 1. 中文简介
该项目旨在为中小企业提供基于人工智能的金融科技解决方案，核心功能是自动化计算关键财务指标。它利用 AI 技术简化复杂的金融数据处理流程，帮助中小企业主更高效地进行财务分析与决策。

### 2. 核心功能
*   集成 AI 算法以自动处理和分析中小企业的财务数据。
*   精准计算各类关键财务价值与核心指标。
*   提供面向中小企业的定制化金融解决方案接口。
*   使用 TypeScript 构建，确保代码的类型安全与可维护性。

### 3. 适用场景
*   中小企业财务人员需要快速生成标准化财务报告时。
*   初创企业缺乏专业金融团队，需借助工具进行基础估值分析时。
*   金融机构希望向中小企业客户提供智能化的自助金融服务时。

### 4. 技术亮点
*   采用 TypeScript 开发，结合 AI 能力实现高精度且类型安全的金融计算逻辑。
- 链接: https://github.com/imchine/FinTech-Solution
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-solution, fintech, fintech-ai, fintech-solution, solution

### fintech-dashboard
- 描述: fintech dashboard for personal finance management which track income and expenses, leverage AI-powered analytics, manage budgets and financial goals, enjoy a dark theme
- 链接: https://github.com/Elias569/fintech-dashboard
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-dashboard, dashboard, fintech, fintech-ai, fintech-dashboard

### fintech-forge
- 描述: fintech forge of AI-powered financial tools and insights to secure authentication and dashboards to empowers developers, analysts, and students to build and extend finance-focused 
- 链接: https://github.com/KORAYTEACHER/fintech-forge
- ⭐ 51 | 🍴 0 | 语言: TypeScript
- 标签: ai-financial-tool, ai-fintech-tool, ai-tool, financial-app, fintech

### openclaw-voice-call-realtime
- 描述: Give your AI assistant a phone — OpenClaw plugin for real phone calls via Twilio + OpenAI Realtime, with in-call tools, transcripts, and call screening
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 35 | 🍴 3 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### ai-guru
- 描述: 无描述
- 链接: https://github.com/Dhruvdubey17/ai-guru
- ⭐ 23 | 🍴 8 | 语言: Shell

### sm120-field-guide
- 描述: AI on consumer Blackwell — a field guide for the RTX 50-series (sm_120). Fixes, footguns, and honest measurement from one RTX 5090.
- 链接: https://github.com/notwitcheer/sm120-field-guide
- ⭐ 21 | 🍴 3 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个涵盖中英文自然语言处理基础工具与资源的综合性开源项目，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证）等核心功能。它不仅提供了丰富的垂直领域词库（如汽车、医疗、财经）和预训练模型资源，还收录了大量高质量的中文NLP数据集、基准测评及前沿论文解读，是中文NLP开发者的实用工具箱。

### 2. 核心功能
*   **基础NLP处理**：提供敏感词过滤、中英日韩语言检测、繁简体转换、分词、词性标注及句法分析等底层能力。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、人名、地名等特定实体的正则抽取与识别，以及关系抽取和事件三元组提取。
*   **丰富词库与知识库**：内置中日文人名、中文缩写、职业、汽车、医疗、法律等多领域专业词库，以及情感值、停用词和反动词表。
*   **预训练模型与资源聚合**：整合了BERT、ERNIE、ALBERT、ELECTRA等多种主流中文预训练模型代码及资源，并包含大量NLP竞赛方案、数据集和学术论文。
*   **语音与多模态支持**：提供中文语音识别（ASR）数据、发音字典、音素对齐工具及中文手写OCR识别相关资源。

### 3. 适用场景
*   **中文NLP初学者入门**：适合需要快速获取分词、词性标注、情感分析及基础数据集的学习者和学生，作为入门实践平台。
*   **企业级内容风控系统**：适用于互联网平台或社区，利用其敏感词库、暴恐词表及谣言检测工具构建内容安全过滤机制。
*   **垂直领域知识图谱构建**：帮助开发者利用其提供的医疗、金融、法律等专业词库和数据集，快速搭建行业特定的知识图谱问答系统。
*   **自然语言处理算法研究**：供研究人员参考最新的NLP竞赛Top方案、预训练模型微调技巧及各类基准评测（Benchmark）结果。

### 4. 技术亮点
*   **资源极度丰富**：作为一个“大而全”的资源仓库，它不仅仅是一个工具库，更是一个汇集了数据集、模型、论文和工具的NLP百科全书。
*   **覆盖主流前沿模型**：紧跟NLP发展潮流，迅速集成并提供了BERT、GPT-2、ALBERT、ELECTREA等最新预训练模型在中文场景下的适配代码。
*   **实用性强**：提供的词库（如车牌号、职业名）和工具（如敏感词检测、实体抽取）可直接应用于实际生产环境，降低开发门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81707 | 🍴 15252 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例和源代码参考，是人工智能学习者的优质资源库。

2. **核心功能**
- 提供涵盖机器学习、深度学习、计算机视觉及NLP的500个完整项目实例。
- 所有项目均附带可运行的源代码，便于用户直接学习和复现。
- 标签分类清晰，支持按特定AI子领域快速检索所需项目。
- 作为一个“Awesome List”式的聚合资源，整合了高质量的学习材料。

3. **适用场景**
- AI初学者希望通过大量代码示例快速掌握各领域的实践技能。
- 开发者需要寻找特定算法（如CNN、RNN、Transformer）的落地实现参考。
- 研究人员或工程师用于对比不同项目架构，寻找灵感或基线代码。
- 教育者作为教学素材库，为学生布置多样化的编程作业。

4. **技术亮点**
- 极高的社区认可度（35278星标），证明其资源丰富性和实用性。
- 内容覆盖面极广，从传统机器学习到前沿深度学习均有涉及。
- 强调“Code-First”，提供完整的工程化代码而非仅理论描述。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35278 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和理解模型结构。该项目以轻量级和广泛的兼容性著称，便于快速调试与分析。

2. **核心功能**
*   支持多种深度学习框架模型格式的直接可视化，包括 TensorFlow、PyTorch、ONNX 等。
*   提供清晰的计算图视图，展示层与层之间的连接关系及数据流向。
*   具备跨平台特性，可在浏览器或独立桌面应用中运行，无需复杂配置。
*   允许用户查看模型各层的详细参数、权重信息及形状属性。

3. **适用场景**
*   开发者在构建或训练模型后，用于检查网络结构是否正确搭建。
*   研究人员对比不同模型架构，快速理解复杂深度学习网络的内部机制。
*   工程人员在模型部署前，验证转换后的模型（如从 PyTorch 转为 ONNX）是否保持原结构。

4. **技术亮点**
*   极高的格式兼容性，广泛支持 CoreML、TensorFlow Lite、SafeTensors 等新兴或特定领域格式。
*   基于 Web 技术实现，使得可视化过程无需安装重型依赖，访问便捷且响应迅速。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33203 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 项目名称：ONNX

#### 1. 中文简介
ONNX（Open Neural Network Exchange）是一种开放标准，旨在实现机器学习模型在不同框架和硬件平台之间的互操作性。它允许开发者轻松地将模型从训练框架（如PyTorch、TensorFlow）导出，并在支持ONNX的推理引擎上高效运行。这一标准极大地简化了深度学习模型的部署流程，促进了生态系统的互联互通。

#### 2. 核心功能
- **跨平台兼容性**：支持在多种硬件加速器（如CPU、GPU、NPU）和软件后端之间无缝迁移模型。
- **框架互操作性**：实现PyTorch、TensorFlow、Keras等主流训练框架与推理引擎之间的双向转换。
- **模型优化能力**：通过ONNX Runtime等工具对模型进行图级优化、算子融合及量化，提升推理性能。
- **标准化表示**：定义统一的计算图和数据格式，确保不同来源的模型具有结构一致性。
- **社区驱动生态**：由微软、Facebook等巨头共同维护，拥有广泛的库支持和活跃的开发者社区。

#### 3. 适用场景
- **生产环境部署**：将在本地训练好的复杂深度学习模型转换为标准化格式，以便在服务器或边缘设备上高效推理。
- **多框架协作开发**：当团队使用不同框架进行模型训练（如PyTorch实验）和服务部署（如TensorRT加速）时，作为中间桥梁避免重写代码。
- **边缘计算设备集成**：将大型云端模型压缩并转换为ONNX格式，以适配资源受限的IoT设备或移动终端。
- **异构硬件加速**：利用ONNX转换器对接特定的硬件后端（如Intel OpenVINO、NVIDIA TensorRT），充分发挥专用芯片的计算潜力。

#### 4. 技术亮点
- **高性能运行时**：配套的ONNX Runtime提供了极低的推理延迟和高吞吐量，支持动态形状和并行执行。
- **丰富的算子支持**：涵盖绝大多数主流神经网络层和自定义算子，几乎兼容所有常见的深度学习架构。
- **版本稳定性强**：经过多次迭代，API和文件格式保持高度向后兼容，适合长期维护的生产级应用。
- 链接: https://github.com/onnx/onnx
- ⭐ 21121 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18293 | 🍴 1160 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17265 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13119 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11565 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个包含500个AI相关项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目为开发者提供了丰富的实战案例，帮助快速掌握并应用人工智能技术解决实际问题。

### 2. 核心功能
*   提供大量包含完整代码的AI项目示例，便于直接学习和复现。
*   覆盖机器学习、深度学习、计算机视觉及NLP等多个热门AI子领域。
*   采用分类标签组织内容，方便用户根据具体技术栈快速检索所需项目。

### 3. 适用场景
*   AI初学者希望通过实际代码案例系统学习机器学习与深度学习基础。
*   开发人员寻找特定任务（如图像识别或文本分析）的参考实现以加速开发。
*   研究人员或学生需要高质量的开源项目灵感来进行学术探索或毕业设计。

### 4. 技术亮点
*   **全面性**：汇聚500个项目，形成庞大的AI技术图谱，覆盖主流算法与应用场景。
*   **实用性**：所有项目均附带代码，强调“开箱即用”，降低从理论到实践的门槛。
*   **社区认可**：拥有超过35,000颗星标，被广泛认为是该领域的“Awesome”级精选资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35278 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流模型格式，帮助用户直观地查看模型结构和参数细节。该工具主要基于 JavaScript 开发，具有轻量且跨平台的特点。

2. **核心功能**
*   支持广泛模型格式的导入与解析，包括 TensorFlow、PyTorch、ONNX 和 Keras 等。
*   提供图形化界面展示网络拓扑结构、层连接关系及张量形状信息。
*   允许用户交互查看模型内部的具体参数值、权重分布及激活函数细节。
*   具备导出图片功能，便于在文档或演示文稿中嵌入清晰的模型架构图。

3. **适用场景**
*   模型调试阶段，开发者用于检查网络结构是否符合预期设计。
*   学术论文或技术报告撰写时，生成高质量的模型结构示意图。
*   团队协作沟通，帮助非技术人员直观理解复杂算法模型的工作流程。
*   模型转换验证，确认不同框架间模型转换后的结构一致性与完整性。

4. **技术亮点**
*   基于 Web 技术栈构建，无需安装重型依赖即可在任何设备上运行。
*   对 ONNX 等交换格式有极佳的支持，促进异构框架间的模型互通。
*   开源且社区活跃，持续跟进最新深度学习框架的模型结构变化。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33203 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究者提供了 Essential Cheat Sheets（关键速查手册），旨在通过简洁的图表和代码片段辅助科研与开发工作。这些资源涵盖了从基础库到高级模型的常用技术点，方便研究人员快速回顾和查阅。

### 2. 核心功能
- 提供深度学习及机器学习领域的核心概念速查表，帮助研究者快速回顾关键知识点。
- 涵盖 Numpy、Scipy、Matplotlib 等常用数据科学与可视化工具的高效用法示例。
- 集成 Keras 等主流框架的代码片段，便于模型构建与调试时参考。
- 内容结构清晰，以可视化图表形式呈现复杂算法或配置参数，提升学习效率。
- 针对研究人员优化，聚焦于实际科研中高频使用的技术细节而非冗长文档。

### 3. 适用场景
- 机器学习研究者在进行文献阅读或实验设计时，快速回顾数据处理和模型评估方法。
- 开发者在搭建深度学习原型时，查找 Matplotlib 绘图技巧或 Numpy 高效操作代码。
- 学生在学习深度学习课程期间，作为 Keras 或 TensorFlow 等框架的快速参考指南。
- 团队内部技术分享时，作为标准化最佳实践和常见陷阱的参考资料。

### 4. 技术亮点
- **高实用性**：精选最常用、最易混淆的技术点，避免冗余信息，直击研究痛点。
- **多语言/工具覆盖**：整合了 Python 科学计算栈（Numpy/Scipy/Matplotlib）与深度学习框架（Keras），形成完整工具链参考。
- **视觉化呈现**：采用 cheat sheet 形式，通过紧凑的布局和图表降低认知负荷，适合快速检索。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目提供了一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户入门并掌握就业所需的实战技能。内容涵盖Python编程、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等热门领域。

### 2. 核心功能
*   **系统化学习路径**：提供从数学基础到前沿AI技术的完整学习路线图，引导初学者循序渐进。
*   **海量实战资源**：整理近200个精选实战案例和项目代码，强化动手实践能力。
*   **免费配套教材**：为所有学习阶段和案例提供免费的配套学习资料，降低学习门槛。
*   **全栈技术覆盖**：内容囊括Python、TensorFlow、PyTorch、Keras等主流框架及NLP、CV等核心应用领域。
*   **就业导向训练**：注重实战应用与技能落地，直接服务于人工智能领域的求职需求。

### 3. 适用场景
*   **零基础转行学习**：适合希望从零开始系统学习人工智能，并计划进入相关行业的初学者。
*   **高校学生实训**：适合计算机或数据科学专业的学生，用于补充课堂知识并进行项目实战演练。
*   **在职人员技能提升**：适合已具备一定编程基础，希望深入掌握深度学习、NLP或CV等特定方向的开发者。

### 4. 技术亮点
*   **开源免费生态**：完全免费开放，整合了从底层库（NumPy, Pandas）到高级框架（PyTorch, TensorFlow 2.x）的广泛技术栈。
*   **多领域融合**：不仅限于算法理论，还深度融合了数据分析（Data Analysis）、数据挖掘（Data Mining）与可视化（Matplotlib, Seaborn）工具链。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13119 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 基于您提供的信息，以下是对 GitHub 项目 **Ludwig** 的技术分析：

1. **中文简介**
   Ludwig 是一个低代码 AI 框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建过程。它通过声明式配置和极简的代码接口，让开发者能够专注于数据与业务逻辑，而非底层工程细节。该项目特别强调数据驱动的开发模式，支持从传统机器学习到深度学习的全流程实验。

2. **核心功能**
   *   **低代码/无代码建模**：提供声明式 API，用户只需定义数据结构即可自动构建模型，无需编写复杂的神经网络代码。
   *   **全栈模型支持**：原生支持传统机器学习算法、深度神经网络以及大型语言模型（LLM）的微调与训练。
   *   **数据中心主义工作流**：内置强大的数据预处理、可视化及探索性数据分析（EDA）工具，强化“数据为中心”的开发理念。
   *   **多框架后端兼容**：底层无缝集成 PyTorch、TensorFlow 等主流深度学习框架，灵活适配不同硬件与性能需求。
   *   **自动化实验管理**：支持超参数优化、模型比较及结果追踪，简化机器学习实验的生命周期管理。

3. **适用场景**
   *   **企业级预测性分析**：适用于需要快速搭建结构化数据预测模型（如销售预测、风险评分）的数据科学团队。
   *   **LLM 微调与应用开发**：适合希望在不深入修改 Transformer 架构的情况下，对 Llama、Mistral 等大模型进行领域适应（Fine-tuning）的研究者。
   *   **机器学习原型验证**：在需要快速验证数据可行性或模型假设的早期研发阶段，帮助工程师迅速迭代想法。
   *   **计算机视觉任务**：用于构建和训练图像分类、目标检测等基于 PyTorch/TensorFlow 的视觉模型。

4. **技术亮点**
   *   **声明式配置优于命令式编码**：通过 YAML/JSON 配置文件直接定义模型架构，极大降低了深度学习入门门槛并提高了可复现性。
   *   **统一的抽象层**：在同一套 API 下兼容传统 ML 和 Deep Learning，允许用户在不同复杂度模型间平滑切换。
   *   **开箱即用的数据可视化**：自动生成训练指标图表和数据分布视图，便于实时监控模型状态和数据质量。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9121 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8921 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1900 | 语言: Shell
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
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81707 | 🍴 15252 | 语言: Python

### LlamaFactory
- ### LlamaFactory 项目分析

**1. 中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目获得了 ACL 2024 会议的认可，旨在简化大模型的适配过程。它通过整合多种前沿技术，让用户能够轻松地对不同架构的模型进行指令微调或强化学习优化。

**2. 核心功能**
*   支持百余种主流 LLM 和 VLM 的统一高效微调与训练。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）技术。
*   提供包括 RLHF（基于人类反馈的强化学习）在内的多样化训练算法支持。
*   内置量化功能（如 QLoRA），显著降低显存占用并提升推理效率。
*   兼容 Transformers 库，提供标准化且易于上手的 API 接口。

**3. 适用场景**
*   **企业级私有化部署**：需要针对特定业务数据（如客服、文档问答）对开源大模型进行指令微调的场景。
*   **资源受限环境训练**：在显存有限的硬件条件下，利用 QLoRA 等技术高效训练或适配大型模型。
*   **多模态应用开发**：需要同时处理文本和图像理解/生成任务的视觉语言模型微调与优化。
*   **学术研究原型验证**：快速复现或对比不同微调算法（如 DPO、PPO）在多种基座模型上的效果。

**4. 技术亮点**
*   **统一性**：打破模型壁垒，在一个框架内无缝切换支持多种不同架构的大模型。
*   **高效率**：通过 QLoRA 等先进量化微调技术，实现低资源消耗下的高性能训练。
*   **前沿算法集成**：原生支持 RLHF、DPO 等最新对齐技术，紧跟 AI 研究前沿。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73109 | 🍴 8933 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54798 | 🍴 8918 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个由微软推出的为期12周、包含24节课的通用人工智能入门课程。该项目旨在通过结构化的教程，让不同背景的初学者都能轻松掌握AI基础知识与技术。

2. **核心功能**
*   提供系统化的12周学习路径，涵盖从基础概念到高级应用的完整内容。
*   采用Jupyter Notebook格式，支持交互式代码编写与即时结果查看。
*   涵盖机器学习和深度学习的多个关键领域，包括计算机视觉和自然语言处理。
*   集成生成对抗网络（GAN）、循环神经网络（RNN）及卷积神经网络（CNN）等具体技术教学。
*   面向大众设计，降低AI学习门槛，适合零基础用户快速上手。

3. **适用场景**
*   希望系统了解AI概念但无深厚数学或编程背景的学生或职场新人。
*   需要搭建短期AI培训课程的企业研发团队或教育机构。
*   希望通过实际代码案例快速验证机器学习想法的数据科学爱好者。
*   正在寻找结构化资源以补充学校AI课程不足的计算机科学专业学生。

4. **技术亮点**
*   微软官方背书，确保内容的权威性与教学资源的丰富性。
*   基于Jupyter Notebook的教学方式，实现了理论与实践的高度结合。
*   内容覆盖全面，从传统机器学习到前沿深度学习技术均有涉及。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51945 | 🍴 10501 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解了线性代数、PyTorch及TensorFlow 2等核心工具。它整合了NLTK自然语言处理技术，旨在为学习者提供从理论基础到代码实现的完整指导。

2. **核心功能**
- 提供基于Scikit-learn和原生Python的经典机器学习算法（如SVM、K-Means、随机森林）实战代码。
- 包含深度神经网络（DNN）、循环神经网络（RNN/LSTM）及卷积神经网络的结构化实现与详解。
- 集成自然语言处理（NLP）模块，利用NLTK和TF2进行文本分析与推荐系统开发。
- 梳理数学基础，重点解析线性代数在机器学习中的应用及PCA/SVD等降维技术。
- 覆盖多种数据挖掘算法，包括关联规则挖掘（Apriori、FP-Growth）及集成学习（AdaBoost）。

3. **适用场景**
- 机器学习初学者构建从数学原理到框架使用的系统化知识体系。
- 数据科学家参考经典算法的工程化实现与调优技巧。
- NLP领域开发者探索文本处理与自然语言理解的基础模型。
- 高校学生或研究人员用于复现论文中的基础算法或完成课程作业。

4. **技术亮点**
- 全面覆盖“理论+代码”双轨制，不仅提供算法源码，还强调背后的数学逻辑。
- 多框架兼容，同时支持传统的Scikit-learn生态与现代深度学习框架PyTorch及TensorFlow 2。
- 知识点密集且结构清晰，将分散的机器学习子领域（如NLP、推荐系统、深度学习）整合在一个项目中。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37722 | 🍴 6289 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35278 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33726 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28432 | 🍴 3462 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25856 | 🍴 2907 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例，帮助其快速掌握相关技术栈并应用于实际开发中。

2. **核心功能**
*   提供大量涵盖机器学习与深度学习的完整代码示例。
*   集成计算机视觉与自然语言处理领域的经典项目实现。
*   作为综合性学习资源库，支持从基础算法到高级应用的全面探索。

3. **适用场景**
*   AI初学者通过阅读和运行代码快速入门机器学习及深度学习概念。
*   数据科学家寻找特定任务（如图像分类或文本分析）的参考实现以加速开发。
*   教育者或培训师利用现成案例构建教学大纲或演示实验环境。

4. **技术亮点**
*   内容覆盖面极广，整合了AI四大主流分支的大量实战项目。
*   所有项目均附带代码，具备极高的可操作性和复现性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35278 | 🍴 7342 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款基于人工智能的自动化框架，旨在通过大语言模型和计算机视觉技术，实现浏览器工作流的自动化操作。它利用 AI 理解网页结构并执行复杂任务，从而替代传统且脆弱的基于选择器或脚本的自动化工具，提供更智能、更稳定的 RPA（机器人流程自动化）解决方案。

**2. 核心功能**
*   **AI 驱动的操作**：利用 LLM 和视觉模型动态识别页面元素并执行点击、输入等动作，无需硬编码选择器。
*   **跨平台兼容性**：支持 Playwright 和 Puppeteer 等主流浏览器引擎，能够与现有 Selenium 工作流平滑集成。
*   **端到端工作流自动化**：能够处理需要多步骤交互的复杂网页任务，如表单填写、数据抓取和账户登录。
*   **自我修复能力**：当网页布局发生变化时，AI 能自适应调整操作策略，显著降低自动化脚本维护成本。

**3. 适用场景**
*   **企业级 RPA**：自动化复杂的后台管理系统操作、ERP 数据录入或跨平台数据同步。
*   **Web 数据抓取**：从动态渲染、反爬虫机制较严的网站中提取结构化数据。
*   **在线事务处理**：自动化完成网上报税、机票预订、保险索赔等需要人机交互的业务流程。
*   **QA 测试自动化**：模拟真实用户行为进行端到端测试，覆盖传统脚本难以处理的动态 UI 场景。

**4. 技术亮点**
*   **视觉与语义结合**：不仅解析 HTML DOM 树，还结合屏幕截图进行视觉推理，提升了在复杂前端框架下的识别准确率。
*   **无头/有头模式灵活切换**：支持在无头模式下运行以节省资源，也可在有头模式下调试，适应不同环境需求。
*   **API 原生设计**：提供易于集成的 RESTful API，方便开发者将其嵌入到现有的 CI/CD 流水线或业务系统中。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22164 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### 1. 中文简介
CVAT 是一个领先的计算机视觉标注平台，旨在构建高质量的视觉数据集以支持视觉人工智能应用。它提供开源、云及企业级产品，涵盖图像、视频和 3D 数据的 AI 辅助标注、质量控制及团队协作等功能。

### 2. 核心功能
*   支持图像、视频及 3D 数据的多模态标注。
*   提供 AI 辅助标注以提升数据处理效率与准确性。
*   内置质量控制机制与团队协作者工流管理。
*   开放开发者 API 便于集成与自动化扩展。

### 3. 适用场景
*   深度学习模型训练所需的大规模视觉数据集构建。
*   计算机视觉领域中的目标检测与语义分割任务准备。
*   需要多人协作进行严格质量管控的企业级数据标注项目。

### 4. 技术亮点
*   拥有活跃的开源社区支持（16,246+ 星标）。
*   广泛兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   支持从基础边界框到复杂的语义分割等多种标注类型。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16246 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN和Vision Transformers等多种模型架构。它广泛应用于分类、目标检测、分割及图像相似度分析等任务，旨在提升深度学习模型的透明度。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种主流可解释性算法实现。
*   兼容卷积神经网络（CNN）与视觉Transformer（ViT）架构。
*   覆盖图像分类、目标检测、语义分割等多类视觉任务。
*   提供直观的可视化结果，帮助理解模型决策依据。

3. **适用场景**
*   研究人员需要分析并可视化深度学习模型的注意力区域以验证其逻辑。
*   开发者在医疗影像或自动驾驶等领域部署模型时，需满足合规性与可信度要求。
*   教育者希望向学生直观展示神经网络如何识别特定物体或特征。

4. **技术亮点**
*   高度模块化设计，轻松适配PyTorch生态下的各类自定义模型。
*   统一接口支持从基础分类到复杂检测任务的多种可解释性方法。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12911 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在通过自动微分技术简化深度学习中的传统图像处理流程。该项目致力于弥合经典计算机视觉与现代深度学习之间的差距，为研究人员和开发者提供高效的工具支持。

**2. 核心功能**
*   提供完全可微分的计算机视觉算子，支持在神经网络中直接进行几何变换。
*   内置丰富的图像处理模块，如色彩空间转换、边缘检测和图像增强。
*   包含先进的几何与相机标定功能，用于处理单应性矩阵、透视投影等任务。
*   原生集成 PyTorch 框架，确保与现有深度学习工作流无缝兼容。

**3. 适用场景**
*   **自动驾驶与机器人导航**：利用可微分的几何操作进行实时环境感知和定位。
*   **医学影像分析**：对 CT 或 MRI 图像进行可微分的配准和分割预处理。
*   **AR/VR 内容生成**：处理空间变换和相机仿真，以增强沉浸式体验。
*   **计算机视觉算法研究**：快速原型化结合传统 CV 知识与深度学习的混合模型。

**4. 技术亮点**
*   **全可微分设计**：允许传统 CV 算法作为层嵌入到反向传播链中，实现端到端训练。
*   **高性能 GPU 加速**：所有算子均针对 NVIDIA GPU 优化，显著提升大规模数据处理速度。
*   **模块化架构**：组件解耦清晰，便于用户按需组合自定义视觉流水线。
- 链接: https://github.com/kornia/kornia
- ⭐ 11272 | 🍴 1198 | 语言: Python
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
- ⭐ 3275 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2623 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2422 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调数据的完全私有化与掌控权。它采用独特的“龙虾”风格设计，旨在为用户提供安全、自主的智能辅助体验。

### 2. 核心功能
*   **跨平台兼容**：支持任何主流操作系统和运行环境，实现无缝部署。
*   **数据私有化**：强调“Own Your Data”，确保用户数据完全由自己掌控，不依赖第三方云服务。
*   **个性化助手**：作为专属个人 AI 助理，可根据用户需求进行定制和优化。
*   **开源透明**：基于开源协议开发，代码公开，便于社区贡献和安全审计。

### 3. 适用场景
*   **注重隐私的用户**：希望完全控制个人数据、避免数据泄露的开发者或普通用户。
*   **本地化部署需求**：需要在离线或本地环境中运行 AI 助手，不依赖外部网络服务的场景。
*   **个性化工作流整合**：希望将 AI 助手深度集成到日常开发、写作或生活管理流程中的用户。

### 4. 技术亮点
*   **TypeScript 驱动**：使用 TypeScript 开发，提供类型安全和良好的开发体验。
*   **高度可定制架构**：模块化设计允许用户根据“龙虾”理念自由扩展和调整功能。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382311 | 🍴 80225 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理式技能框架与软件开发方法论，旨在通过结构化的多智能体协作提升开发效率。它将复杂的软件开发生命周期分解为可管理的技能模块，由子代理驱动执行，从而确保从构思到交付的顺畅流程。

2. **核心功能**
*   **代理驱动开发**：采用子代理协同工作模式，自动化执行代码生成、调试及测试任务。
*   **结构化技能框架**：提供一套标准化的“技能”库，覆盖头脑风暴、编码及系统生命周期管理等环节。
*   **一体化SDLC支持**：整合从需求分析到部署的软件开发生命周期全流程，减少上下文切换成本。
*   **智能头脑风暴辅助**：内置专门的AI辅助功能，帮助开发者在早期阶段梳理思路和设计架构。

3. **适用场景**
*   **复杂系统架构设计**：需要多步骤规划和大模型协作来梳理逻辑的复杂项目开发。
*   **全栈自动化开发**：希望利用AI代理自动完成从代码编写到单元测试生成的端到端任务。
*   **敏捷团队流程优化**：寻求标准化开发方法论以提升团队协作效率和代码一致性的工程团队。

4. **技术亮点**
*   创新性地结合了“技能”概念与代理编程范式，实现了高度模块化的AI协作流。
*   尽管主脚本为Shell，但其核心逻辑在于定义了一套可复用的代理交互协议和工作流标准。
- 链接: https://github.com/obra/superpowers
- ⭐ 250556 | 🍴 22225 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一个旨在伴随用户共同成长的智能代理工具。它深度整合了多种主流大型语言模型（如 Anthropic 的 Claude、OpenAI 的代码解释器等），提供强大的自动化代码辅助能力。该项目致力于通过统一的接口简化复杂 AI 交互流程，提升开发者的工作效率。

### 2. 核心功能
*   **多模型支持**：兼容 OpenAI、Anthropic 等多种 LLM 后端，用户可灵活切换不同模型以适应不同需求。
*   **智能代码代理**：具备自动执行代码任务、调试及重构的能力，类似于 GitHub Copilot 或 Claude Code 的深度集成体验。
*   **持续进化架构**：设计为“随你成长”，意味着其功能可随用户习惯和工作流进行扩展和优化。
*   **统一 CLI 界面**：提供命令行工具，方便开发者在终端中快速调用 AI 能力进行编码辅助。

### 3. 适用场景
*   **高级开发者自动化工作流**：需要频繁进行代码生成、审查和调试的专业开发人员。
*   **AI 实验与研究**：研究人员希望在一个环境中测试不同 LLM 模型对同一编程任务的响应差异。
*   **本地化 AI 助手搭建**：希望在自己的机器上部署一个不受限制、隐私性更强的代码辅助代理的用户。

### 4. 技术亮点
*   **开源社区驱动**：拥有极高的星标数（21万+），表明其在开发者群体中具有广泛的影响力和活跃度。
*   **模块化设计**：标签显示其支持多种 AI 品牌（如 Nous Research, OpenClaw 等），体现了良好的扩展性和兼容性。
*   **聚焦代码领域**：明确针对编程场景优化，区别于通用聊天机器人，提供更精准的工程级辅助。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 212001 | 🍴 39028 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个具备原生 AI 能力的公平源代码工作流自动化平台，支持自行托管或云端部署。它结合了可视化构建与自定义代码功能，拥有超过 400 种集成方式，旨在简化复杂的工作流开发。

### 2. 核心功能
*   **混合式工作流构建**：允许用户通过可视化界面拖拽组件，同时支持嵌入自定义代码以实现高度定制化。
*   **广泛的集成生态**：内置超过 400 种应用程序和 API 的原生集成，涵盖主流 SaaS 服务和数据库。
*   **原生 AI 能力**：深度集成人工智能功能，支持在工作流中直接调用 LLM 进行智能处理和分析。
*   **灵活部署模式**：提供“公平源代码”许可，既支持完全自托管以保障数据隐私，也提供便捷的云服务选项。

### 3. 适用场景
*   **企业级自动化集成**：连接 CRM、ERP 和通信工具，自动同步数据并触发业务流程，减少人工操作。
*   **AI 驱动的数据处理**：利用原生 AI 节点对非结构化数据进行分类、摘要或生成内容，并整合到后续工作流中。
*   **开发者快速原型验证**：通过低代码/无代码环境快速搭建 API 网关或中间件，结合自定义代码实现逻辑验证。

### 4. 技术亮点
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，作为客户端和服务器端增强 AI 模型的上下文交互能力。
*   **TypeScript 架构**：基于 TypeScript 开发，保证了代码的类型安全和极高的可维护性，便于社区贡献和扩展。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195809 | 🍴 59191 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。其使命是提供必要的工具，使开发者能够专注于业务逻辑与核心价值，而无需被底层技术细节所困扰。

### 2. 核心功能
*   **自主代理能力**：基于大语言模型（LLM），具备自主规划、执行任务及反思修正的能力。
*   **多模型支持**：兼容 OpenAI、Anthropic (Claude) 及 Llama 等多种主流 AI 接口。
*   **互联网交互**：拥有浏览器控制、API 调用及文件系统读写权限，可独立访问网络资源。
*   **长期记忆管理**：结合向量数据库实现持久化记忆，确保在多轮对话中保持上下文连贯性。

### 3. 适用场景
*   **自动化工作流**：执行重复性高、步骤复杂的数字任务（如数据爬取、报告生成）。
*   **代码辅助开发**：作为智能编程助手，自动完成代码编写、调试及文档生成。
*   **市场调研与分析**：自主搜索网络信息，汇总并分析特定领域的市场趋势或竞品数据。

### 4. 技术亮点
*   采用先进的 Agent 架构，实现了从单一指令执行到复杂目标拆解的跃迁。
*   高度模块化的设计允许用户灵活集成不同的 LLM 提供商和外部工具插件。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185441 | 🍴 46116 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165143 | 🍴 21371 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164055 | 🍴 30399 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156913 | 🍴 46168 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151419 | 🍴 9485 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148300 | 🍴 23368 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

