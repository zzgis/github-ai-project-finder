# GitHub AI项目每日发现报告
日期: 2026-07-13

## 新发布的AI项目

### awesome-ai-accelerators
- 1. **中文简介**
这是一个精心策划的列表，汇集了AI加速器相关的学术论文、资源、工具及开源项目。它旨在为研究人员和开发者提供一站式的信息索引，涵盖从理论算法到工程实现的完整生态。该项目通过整合多方资料，帮助用户快速了解AI硬件加速领域的最新动态与可用方案。

2. **核心功能**
- 提供经过筛选的AI加速器相关学术论文集合，便于追踪前沿研究。
- 整理各类AI加速工具链与软件框架，支持加速模型的部署与优化。
- 收录多个高质量的开源项目代码库，促进技术交流与复用。
- 分类汇总行业资源，构建结构化的AI加速器知识体系。

3. **适用场景**
- 研究人员查阅AI加速器领域的经典文献与最新突破。
- 工程师寻找合适的开源工具或框架以优化模型推理性能。
- 学生或初学者系统性地了解AI硬件加速的技术栈与生态。
- 企业技术选型时评估现有的AI加速解决方案与社区活跃度。

4. **技术亮点**
- 内容经过人工策展（Curated），确保信息的高质量与相关性。
- 覆盖范围广泛，兼顾学术理论研究与工业界开源实践。
- 链接: https://github.com/LonghornSilicon/awesome-ai-accelerators
- ⭐ 87 | 🍴 12 | 语言: 未知

### morphe-ai
- 1. **中文简介**
Morphe 是一个基于 AI 驱动的 Android APK 修补工作区，专为安全研究人员和逆向工程师设计。它通过多智能体管道自动化执行 APK 分析、目标筛选、补丁编写及部署等复杂流程。该项目旨在简化安卓应用修改与定制的开发体验。

2. **核心功能**
*   利用多智能体协作管道实现 APK 的全流程自动化处理。
*   具备智能化的 APK 静态分析与动态目标筛选能力。
*   支持自动生成或辅助编写 Smali 代码级别的修补脚本。
*   集成从代码修改到最终 APK 部署的一站式工作流。

3. **适用场景**
*   需要批量修改多个第三方 Android 应用的开发者或测试人员。
*   进行安卓应用逆向工程与安全漏洞复现的研究人员。
*   希望自动化生成特定功能补丁（如去广告、解锁功能）的安全爱好者。
*   快速验证 APK 修改效果并部署到测试设备的工程团队。

4. **技术亮点**
*   采用多智能体（Multi-Agent）架构，将复杂的逆向工程任务分解为分析、狩猎、修补和部署等独立且协同的子任务。
*   深度整合 Shell 脚本与 Smali 汇编语言操作，实现底层代码级的高效修改。
*   针对 YouTube 等具体应用场景进行了优化，提供了现成的补丁策略参考。
- 链接: https://github.com/Paresh-Maheshwari/morphe-ai
- ⭐ 84 | 🍴 9 | 语言: Shell
- 标签: android, apk, morphe, morphe-patches, paresh-patches

### rust-ai-agent
- 描述: 无描述
- 链接: https://github.com/solenovex/rust-ai-agent
- ⭐ 22 | 🍴 0 | 语言: Rust

### klinepic-agent-api-examples
- ### 1. 中文简介
该项目提供了基于模型上下文协议（MCP）服务器和 OpenAPI 的示例代码，旨在帮助 AI 智能体将经纪商或交易所的交易成交记录转换为带有详细注释的 KLinePic 交易复盘图表。它专注于通过自动化工具提升金融数据的可视化效果，使交易者能够更直观地回顾和分析历史交易表现。

### 2. 核心功能
*   支持 MCP 服务器架构，便于 AI 智能体无缝集成交易数据获取与处理功能。
*   利用 OpenAPI 标准接口定义，确保不同系统间的数据交互兼容性和扩展性。
*   自动将原始交易成交记录（Fills）映射并生成为带有标注的 KLinePic 蜡烛图。
*   提供针对经纪商和加密货币交易所交易数据的标准化解析与可视化模板。

### 3. 适用场景
*   **自动化交易复盘**：AI 助手定期抓取交易日志，自动生成带有多维度指标注释的技术分析图表。
*   **开发交易辅助工具**：开发者基于此示例构建集成了 MCP 协议的智能交易代理或量化分析平台。
*   **加密货币投资教育**：用于生成可视化的学习材料，展示特定交易策略在历史行情中的实际表现。

### 4. 技术亮点
*   结合了前沿的 Model Context Protocol (MCP) 标准，增强了 AI 智能体访问外部金融数据的能力。
*   专注于“交易复盘”这一垂直领域，通过 KLinePic 实现了比传统表格更直观的数据洞察。
*   提供完整的 API 示例，降低了开发者在 AI Agent 与金融数据可视化之间建立连接的门槛。
- 链接: https://github.com/sher1096/klinepic-agent-api-examples
- ⭐ 20 | 🍴 1 | 语言: JavaScript
- 标签: agent-tools, ai-agents, api, candlestick-chart, crypto-trading

### plandeck
- 以下是针对 GitHub 项目 **plandeck** 的技术分析：

1. **中文简介**
   PlanDeck 是为长期运行的 AI 智能体设计的可视化看板工具，旨在直观展示计划中依赖关系的解锁、关键路径的高亮以及下一步操作的明确指引。它通过图形化界面取代枯燥的 Markdown 文本，让开发者能轻松监控和调度复杂的 AI 代理任务流程。

2. **核心功能**
   - **可视化任务状态**：将智能体的计划转化为动态看板，清晰展示任务从“待办”到“就绪”的状态流转。
   - **依赖关系管理**：自动识别并高亮显示任务间的依赖链，当前置条件满足时，后续任务自动进入“Ready”状态。
   - **关键路径追踪**：实时计算并高亮显示影响整体进度的关键路径，帮助快速定位瓶颈。
   - **零依赖与稳定性**：采用无外部依赖架构设计，确保在长时间运行中具备抗崩溃能力。

3. **适用场景**
   - **复杂 AI 代理开发**：适用于使用 Claude Code、Codex 或 Cursor 等工具进行需要多步骤规划的智能体开发调试。
   - **自动化工作流监控**：用于观察和管理长时间运行的自动化任务队列，直观掌握执行进度。
   - **团队协作与项目管理**：作为轻量级的项目管理看板，帮助团队同步 AI 生成的代码修改计划和任务分配。

4. **技术亮点**
   - **实时数据流支持**：基于 SSE (Server-Sent Events) 实现前端与后端的实时通信，确保看板状态即时更新。
   - **跨平台兼容性**：明确标记兼容 Claude Code、Codex 和 Cursor 等主流 AI 编程助手，具有广泛的生态适配性。
- 链接: https://github.com/OthmanAdi/plandeck
- ⭐ 20 | 🍴 0 | 语言: JavaScript
- 标签: agent-skill, agentic, ai-agents, claude-code, codex

### ai-robot
- 描述: RK3506 Voice Robot An embedded AI voice assistant running on the Rockchip RK3506 development board. Pure C, single-threaded event loop, zero dynamic memory allocation.
- 链接: https://github.com/UIseries/ai-robot
- ⭐ 19 | 🍴 0 | 语言: C

### zabt-ai
- 描述: Self-hosted AI meeting intelligence — transcription (faster-whisper), speaker diarization (pyannote), and LLM summaries on infrastructure you control. An open-source, self-hostable alternative to Otter.ai / Fireflies.
- 链接: https://github.com/afeef/zabt-ai
- ⭐ 14 | 🍴 3 | 语言: Python
- 标签: agpl, ai, fastapi, meeting-notes, nextjs

### Local-Recall
- 描述: An early prototype alternative to Microsoft/Windows Recall, built to run 100% locally with zero cloud communication. Captures screen snapshots, extracts text via WinRT OCR, and indexes embeddings into SQLite. Query your history conversationally via your local LLM (LM Studio). Under active development.
- 链接: https://github.com/anshupriyan/Local-Recall
- ⭐ 14 | 🍴 0 | 语言: Python
- 标签: ai, microsoft, python, windows, windows-recall

### relay-status-monitor
- 描述: 自托管的 AI API 中转站状态监控面板，支持 SUB2API / New API、余额与延迟采集、模型测速、可用率统计及飞书告警。
- 链接: https://github.com/yigehaozi/relay-status-monitor
- ⭐ 14 | 🍴 4 | 语言: TypeScript
- 标签: ai-api, api-monitoring, new-api, nextjs, openai-api

### workbuddian
- 描述: Embed the WorkBuddy/CodeBuddy CLI as an AI chat agent inside Obsidian
- 链接: https://github.com/jiang198012/workbuddian
- ⭐ 13 | 🍴 0 | 语言: TypeScript
- 标签: agent, ai, ai-chat, codebuddy, llm

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
该项目是一个全面的中英文自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、情感分析）到高级任务（如命名实体识别、知识图谱构建、对话系统）的各类开源项目、数据集及预训练模型。它整合了包括BERT、ALBERT、GPT等主流预训练语言模型的应用实例，以及大量垂直领域（如医疗、金融、法律）的数据和工具链，旨在为开发者提供一站式的NLP开发支持。

### 2. 核心功能
*   **基础NLP工具与数据**：提供中英文敏感词过滤、语言检测、停用词、同/反义词库、繁简体转换及中文分词加速工具（如jieba_fast）。
*   **信息抽取与实体识别**：集成基于BERT等模型的命名实体识别（NER）、关系抽取、关键词提取及文本分类代码，支持医疗、法律等专业领域。
*   **预训练模型与应用**：收录多个开源中文预训练模型（如ELECTREA、ALBERT-Chinese、RoBERTa）及其在阅读理解、情感分析、文本生成等任务上的实现。
*   **知识图谱与问答系统**：包含知识图谱构建工具（如Zincbase）、问答系统资源（如基于百科或医疗KG的QA）、对话机器人框架及闲聊语料。
*   **语音与OCR技术**：涵盖中文语音识别（ASR）、文字转语音（TTS）、手写汉字识别（OCR）及音频数据增强相关资源。

### 3. 适用场景
*   **中文NLP研究与开发**：研究人员或开发者需要快速查找最新的中文预训练模型、基准数据集（如CLUE）及评测指标，以加速算法迭代。
*   **垂直行业解决方案构建**：在金融、医疗、法律等领域，利用项目中提供的专用词库、语料和实体识别模型，构建专业的领域问答系统或信息抽取流水线。
*   **企业级内容安全与审核**：直接使用项目中封装好的敏感词库、暴恐词表及反动词表，快速搭建内容审核系统，确保文本合规性。
*   **自然语言处理教学与学习**：作为初学者或进阶者的资源库，通过阅读其中的教程代码（如BERT微调示例、对话系统搭建），理解NLP核心算法原理。

### 4. 技术亮点
*   **生态聚合性强**：不仅包含代码，还整合了大量高质量数据集、开源论文解读、技术报告及行业最佳实践，是中文NLP领域的“百科全书”。
*   **紧跟前沿技术**：及时收录了BERT、GPT-2、ALBERT、ELECTREA等最新预训练语言模型及其变体在中文场景下的适配与优化方案。
*   **领域覆盖广泛**：从通用NLP任务延伸至医疗、法律、金融、汽车等细分垂直领域，提供了丰富的专用词库和标注数据，减少了数据准备成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81778 | 🍴 15251 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目附带完整代码，旨在为开发者提供丰富的实战案例参考。它被标记为“Awesome”列表，是学习AI技术的重要入门资料。

2. **核心功能**
*   提供大量涵盖主流AI领域的实战项目代码。
*   包含机器学习与深度学习的典型算法实现。
*   集成计算机视觉与自然语言处理的具体应用场景。
*   作为结构化的学习资源库，方便快速检索和复现。

3. **适用场景**
*   AI初学者通过阅读代码快速理解基础概念。
*   开发者寻找特定任务（如图像分类、文本分析）的参考实现。
*   技术团队进行模型选型或原型开发时的灵感来源。
*   学生完成课程作业或毕业设计时的案例参考。

4. **技术亮点**
*   项目数量庞大且分类清晰，覆盖AI主要分支领域。
*   强调代码实用性，所有项目均附带可执行源码。
*   获得高星标认可，社区活跃度高，具备较好的参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35402 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款轻量级的神经网络、深度学习及机器学习模型可视化工具。它支持多种主流框架生成的模型文件，能够以图形化方式直观展示模型架构。该工具旨在帮助用户快速理解和分析复杂的模型结构。

### 2. 核心功能
- **多格式支持**：兼容 CoreML、Keras、ONNX、PyTorch、TensorFlow 等多种主流模型格式。
- **可视化架构图**：清晰展示神经网络的层结构、连接关系及数据流向。
- **跨平台运行**：基于 Web 技术构建，支持在浏览器、桌面端独立运行或通过命令行查看。
- **交互式探索**：允许用户点击节点查看详细信息，如权重、偏置及张量形状。

### 3. 适用场景
- **模型调试与验证**：开发者检查模型结构是否符合预期，排查层配置错误。
- **学术研究与演示**：研究人员直观展示论文中的网络架构，便于交流和发表。
- **模型迁移与分析**：在部署前分析不同框架间的模型兼容性，如从 PyTorch 转换为 ONNX。

### 4. 技术亮点
- **无需安装依赖**：作为纯前端应用，无需配置复杂的 Python 环境即可直接打开模型文件。
- **广泛的生态覆盖**：支持 safetensors、TensorFlow Lite 等新兴或特定领域的模型格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33223 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21141 | 🍴 3967 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18395 | 🍴 1172 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17316 | 🍴 2117 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13133 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11571 | 🍴 907 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35402 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33223 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了一系列必备的核心知识速查表（Cheat Sheets）。内容涵盖从基础数学工具到高级框架使用的关键概念，旨在帮助研究者快速回顾和掌握核心技术要点。

### 2. 核心功能
*   **全面覆盖关键技术栈**：整理了对 numpy、scipy、matplotlib 等数据分析与可视化工具的核心用法总结。
*   **深度学习框架指南**：提供了 Keras 等主流深度学习框架的快速参考手册，简化代码实现流程。
*   **机器学习理论速览**：浓缩了机器学习算法的关键公式、参数设置及最佳实践建议。
*   **研究效率提升工具**：作为即查即用的参考资料，帮助研究人员在实验调试和论文撰写时快速定位信息。

### 3. 适用场景
*   **模型调试与开发**：在构建神经网络或调整超参数时，快速查阅特定函数或库的标准用法。
*   **学术研究与论文写作**：在撰写论文或准备报告时，准确引用数学公式或算法逻辑的标准表述。
*   **新人学习与入门**：机器学习初学者通过结构化摘要快速建立对核心工具和理论的整体认知框架。

### 4. 技术亮点
*   **高度浓缩的知识图谱**：将复杂的技术文档提炼为简洁直观的图表和代码片段，极大降低了信息获取成本。
*   **权威来源背书**：基于 Medium 上知名技术博主的专业总结，内容经过社区验证，具有较高的实用参考价值。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目提供了一份全面的人工智能学习路线图，涵盖从零基础入门到就业实战的全过程。内容整理了近200个实战案例，并免费提供配套教材，覆盖Python、机器学习、深度学习及数据分析等热门领域。旨在帮助学习者系统掌握AI核心技术并提升实际应用能力。

2. **核心功能**
*   提供结构化的人工智能学习路径，引导初学者循序渐进地掌握技能。
*   收录近200个实战案例与项目，强调动手实践与就业导向。
*   免费开放配套教材和资源，降低人工智能领域的学习门槛。
*   覆盖从基础数学、Python编程到高级深度学习框架的全栈知识体系。

3. **适用场景**
*   **零基础转行人员**：希望系统学习人工智能相关知识并寻求相关就业机会的人群。
*   **在校大学生**：需要补充课堂理论之外的实战项目经验以增强简历竞争力的学生。
*   **在职技术人员**：希望拓展技能树，从传统开发转向AI或数据科学领域的开发者。

4. **技术亮点**
*   资源高度集成，将分散的知识点（如TensorFlow、PyTorch、Pandas等）整合为连贯的学习路线。
*   强调“实战驱动”，通过大量真实案例连接理论知识与工程应用。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13133 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11736 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9133 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8930 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6254 | 🍴 741 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具箱，集成了敏感词过滤、语种检测、实体抽取（手机号、身份证、邮箱等）及多种基础NLP任务。该项目还收录了丰富的行业词库（如医疗、法律、汽车）、预训练模型资源（如BERT、ALBERT）以及各类NLP数据集和竞赛方案汇总。它旨在为开发者提供一站式的基础设施，涵盖从文本预处理、特征工程到高级语义理解和生成的完整流程。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简转换、标点修复、拼写检查、文本摘要及关键词抽取功能。
*   **信息抽取与识别**：支持姓名、性别、手机号、身份证、邮箱、地址等实体的自动化抽取，以及命名实体识别（NER）和关系抽取。
*   **丰富词库与数据资源**：内置中日文人名库、行业专用词库（医疗、法律、财经等）、停用词表、情感值词典及大量公开NLP数据集。
*   **预训练模型与工具集成**：汇总并提供了BERT、ALBERT、RoBERTa等主流预训练模型的中文版本，以及SpaCy、Jieba等常用NLP工具的配置与优化。
*   **应用案例与前沿技术**：包含聊天机器人、知识图谱构建、语音识别、文本生成及对抗样本生成等具体应用场景的代码和参考实现。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和反动词表，快速构建网站或APP的内容过滤系统，屏蔽违规信息。
*   **企业级知识图谱构建**：借助实体抽取工具和行业词库，从非结构化文本（如新闻、财报）中提取三元组，构建垂直领域知识图谱。
*   **智能客服与对话系统开发**：使用汇总的对话数据集、闲聊机器人代码及意图识别资源，快速搭建具备语义理解能力的智能助手。
*   **NLP算法研究与教学**：作为学习资源库，帮助研究人员和学生快速获取最新的NLP论文、竞赛获奖方案、数据集及基准测试代码。

4. **技术亮点**
*   **资源聚合度高**：不仅包含代码库，还整合了清华XLORE、百度问答集、医疗知识图谱等高价值数据资源和学术报告，极大降低了资料搜集成本。
*   **覆盖全流程**：从底层的数据清洗、分词、实体识别，到中层的语义理解、知识图谱构建，再到上层的应用生成，提供了端到端的解决方案参考。
*   **紧跟技术前沿**：持续更新包含BERT、Transformer、GPT-2等最新深度学习架构在中文NLP领域的应用实例和微调技巧。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81778 | 🍴 15251 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73235 | 🍴 8947 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 57107 | 🍴 9438 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由微软发起，内容涵盖从基础机器学习到深度学习的广泛主题。通过结构化的学习计划，帮助初学者系统性地构建AI技能体系。

2. **核心功能**
*   提供结构化的12周学习路径，每周对应特定的AI主题和课程。
*   基于Jupyter Notebook编写，支持交互式代码练习和即时反馈。
*   覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
*   免费开放给全球学习者，降低人工智能技术的入门门槛。
*   包含理论讲解与动手实践相结合的24节完整课程。

3. **适用场景**
*   零基础用户希望系统了解人工智能基本概念和技术栈。
*   教育机构或企业用于内部员工的基础AI技能培训。
*   学生作为计算机科学相关课程的辅助教材或课外拓展资源。
*   开发者想要快速复习或掌握特定AI技术（如CNN、GAN）的实践应用。

4. **技术亮点**
*   采用微软“For Beginners”系列的教学方法论，注重循序渐进和易用性。
*   涵盖前沿AI技术，包括卷积神经网络（CNN）、循环神经网络（RNN）及生成对抗网络（GAN）。
*   利用Jupyter Notebook实现代码与文档的无缝结合，便于学习和调试。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52226 | 🍴 10563 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42376 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38161 | 🍴 6381 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35402 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33740 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28519 | 🍴 3477 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25887 | 🍴 2919 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个收录了500个AI相关项目的代码集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它为开发者提供了丰富的实战案例和源代码，是入门与进阶的优质资源库。

2. **核心功能**
- 汇集大量经过验证的AI项目代码，支持直接学习与复现。
- 覆盖机器学习、深度学习、CV和NLP四大核心AI领域。
- 包含从基础到高级的多层次项目实例，适应不同技能水平。
- 提供结构化的项目分类，便于快速定位特定技术方向的代码。

3. **适用场景**
- AI初学者寻找高质量、可运行的入门级实战项目。
- 工程师在需要特定算法实现时参考现成的代码模板。
- 研究人员或学生用于快速搭建原型或验证想法。
- 面试准备者通过练习经典项目提升技术实战能力。

4. **技术亮点**
- 项目数量庞大且分类清晰，构建了一个全面的AI代码生态系统。
- 精选主流框架实现，确保代码的时效性和实用性。
- 作为Awesome列表类资源，具有极高的社区认可度和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35402 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一个基于人工智能的自动化平台，旨在通过视觉理解能力自动执行复杂的浏览器工作流。它利用大型语言模型（LLM）和计算机视觉技术，能够模拟人类操作来与网页进行交互，从而替代传统的基于选择器的自动化脚本。

### 2. 核心功能
*   **视觉驱动自动化**：不依赖易碎的 CSS 选择器，而是通过“看”到页面元素来识别和操作界面。
*   **智能工作流编排**：支持构建复杂的多步浏览器任务，如登录、数据提取和表单填写。
*   **LLM 集成能力**：深度结合 GPT 等大语言模型，理解自然语言指令并转化为具体的浏览器操作。
*   **高稳定性与鲁棒性**：面对页面布局变化或动态加载内容时，仍能保持较高的执行成功率。
*   **无代码/低代码接口**：提供 API 支持，方便开发者将浏览器自动化能力集成到现有系统中。

### 3. 适用场景
*   **RPA 流程自动化**：自动化处理需要跨多个网页系统操作的后台业务流程（如财务对账、订单录入）。
*   **大规模数据采集**：从结构不稳定或反爬机制较强的网站中提取结构化数据。
*   **Web 应用测试**：模拟真实用户行为进行端到端的功能测试，特别是针对 UI 频繁变动的现代 Web 应用。
*   **个人效率工具开发**：快速构建自动化个人助手，例如自动预订机票、监控商品价格变动等。

### 4. 技术亮点
*   **超越传统 Selenium/Playwright 选择器**：解决了传统自动化工具因页面 DOM 结构微小变更导致脚本失效的痛点。
*   **端到端视觉理解**：将图像识别与大语言模型的推理能力结合，实现了对非结构化界面的语义理解。
*   **兼容主流浏览器引擎**：底层基于 Playwright/Puppeteer 等技术栈，同时封装了更高层的 AI 决策逻辑。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22215 | 🍴 2080 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16279 | 🍴 3744 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具包，旨在通过可视化技术揭示模型的决策依据。它广泛支持CNN、Vision Transformer等架构，涵盖分类、检测、分割及图像相似度等多种任务。该项目致力于提升深度学习模型的透明度与可信度。

2. **核心功能**
*   支持多种主流模型架构，包括卷积神经网络（CNN）和视觉Transformer（ViT）。
*   兼容多种视觉任务，如图像分类、目标检测、语义分割及图像相似性计算。
*   集成多种梯度加权类激活映射算法，如Grad-CAM、Score-CAM等，以生成热力图。
*   提供直观的可视化接口，帮助用户理解模型关注的关键区域。

3. **适用场景**
*   **模型调试与优化**：通过可视化确认模型是否关注了正确的特征区域，辅助发现偏差。
*   **医疗影像分析验证**：在癌症检测等高风险领域，验证AI诊断依据是否符合医学逻辑。
*   **自动驾驶安全审计**：检查自动驾驶系统对道路标志或行人的识别焦点，确保决策可靠性。
*   **学术研究与教育**：作为可解释人工智能（XAI）的教学案例或研究基准工具。

4. **技术亮点**
*   高度模块化设计，无缝适配PyTorch生态及各类前沿视觉Transformer架构。
*   不仅限于传统的Grad-CAM，还整合了Score-CAM等更先进的类激活映射方法。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. **中文简介**
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理原语，旨在简化深度学习在计算机视觉领域的开发流程。该库致力于将传统几何视觉与现代神经网络无缝集成。

### 2. **核心功能**
- **可微分图像处理**：提供完全可微分的图像变换、增强及几何操作，支持端到端的梯度反向传播。
- **几何视觉算法**：内置相机标定、立体匹配、姿态估计等传统几何视觉算法的深度学习实现。
- **PyTorch 原生集成**：作为 PyTorch 的扩展库，能够与现有的深度学习模型和训练循环轻松整合。
- **多模态数据处理**：支持从 2D 图像到 3D 点云等多种数据格式的几何分析与处理。
- **模块化设计**：提供丰富的即插即用模块，涵盖图像预处理、特征提取及后处理等各个环节。

### 3. **适用场景**
- **机器人导航与感知**：用于开发需要实时理解环境几何结构（如 SLAM）的自主移动机器人系统。
- **自动驾驶视觉系统**：应用于车辆的环境感知模块，进行车道线检测、障碍物距离估算等任务。
- **增强现实（AR）应用**：在 AR 场景中实现精确的空间定位、物体追踪以及虚实融合效果。
- **医学影像分析**：处理具有复杂几何结构的医学图像，辅助进行病灶定位或器官分割等任务。

### 4. **技术亮点**
- **可微分渲染与优化**：允许将传统计算机视觉约束直接融入神经网络的损失函数中，提升模型的可解释性与精度。
- **高性能 GPU 加速**：所有核心算子均针对 GPU 进行了高度优化，显著提升了大规模图像批处理的效率。
- 链接: https://github.com/kornia/kornia
- ⭐ 11273 | 🍴 1199 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3457 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3282 | 🍴 402 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2625 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2428 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款强调数据主权的个人 AI 助手，支持跨操作系统和平台运行。它采用独特的“龙虾”理念，让用户完全掌控自己的 AI 体验与隐私数据。

### 2. 核心功能
*   **全平台兼容**：支持在任何操作系统和设备上部署和运行。
*   **数据私有化**：强调“拥有你的数据”，确保用户隐私和数据安全。
*   **个人助理定位**：作为专属的个人 AI 助手，提供定制化服务。
*   **开源特性**：基于开源社区驱动，标签包含“molty”和“crustacean”等独特标识。

### 3. 适用场景
*   **注重隐私的个人用户**：希望完全控制 AI 数据流向、拒绝云端监控的技术爱好者。
*   **跨设备工作流整合**：需要在不同操作系统（如 Linux、Windows、macOS）间无缝切换使用的开发者或专业人士。
*   **自建 AI 基础设施**：希望本地部署个人 AI 助手以构建私有知识库或自动化工作流的团队。

### 4. 技术亮点
*   **TypeScript 开发**：使用 TypeScript 编写，具备良好的类型安全和现代前端/后端生态兼容性。
*   **高关注度项目**：拥有超过 38 万颗星，表明其在 AI 助手领域具有极高的社区认可度和活跃度。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382815 | 🍴 80347 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 253637 | 🍴 22660 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款旨在伴随用户共同成长的智能代理工具。它利用大型语言模型（LLM）技术，通过持续学习和交互优化，为用户提供个性化的辅助体验。该项目致力于打造一个能够适应不同需求并不断进化的 AI 助手生态。

### 2. 核心功能
- **动态成长机制**：代理能够根据用户的使用习惯和反馈不断进化，提升服务精准度。
- **多模型兼容支持**：集成 Anthropic、OpenAI 等主流大语言模型，灵活切换以提升性能。
- **代码与自动化辅助**：提供类似 Codex 或 Claude Code 的代码生成及任务自动化能力。
- **个性化记忆管理**：具备长期记忆功能，确保在多轮对话中保持上下文连贯性。
- **开源可扩展架构**：基于 Python 开发，允许开发者自由定制和扩展代理功能。

### 3. 适用场景
- **高级开发者辅助**：用于复杂代码编写、调试及自动化脚本生成的编程工作流。
- **个性化智能助手**：作为日常工作效率工具，处理邮件整理、日程安排等重复性任务。
- **AI 应用原型开发**：研究人员或开发者构建和测试新型 AI Agent 架构的快速实验平台。
- **企业级知识管理**：结合私有数据训练代理，实现企业内部知识的智能化检索与问答。

### 4. 技术亮点
- **跨平台模型集成**：无缝对接多种顶尖 LLM 后端，避免单一供应商锁定。
- **轻量化 Python 实现**：核心逻辑简洁高效，易于部署和维护。
- **社区驱动迭代**：拥有高活跃度的星标群体，反映其在 AI Agent 领域的广泛认可与技术前瞻性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 214121 | 🍴 39741 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196278 | 🍴 59300 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185510 | 🍴 46096 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165624 | 🍴 21434 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164218 | 🍴 30528 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156998 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151812 | 🍴 9668 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 150252 | 🍴 8589 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

