# GitHub AI项目每日发现报告
日期: 2026-07-13

## 新发布的AI项目

### awesome-ai-accelerators
- 1. **中文简介**
这是一个精心整理的列表，汇集了人工智能加速器领域的学术论文、资源、工具及开源项目。它旨在为研究人员和开发者提供一个全面的参考资料库，涵盖从硬件架构到软件优化的广泛内容。

2. **核心功能**
- 汇总AI加速器相关的经典与前沿学术论文。
- 提供各类AI加速工具和开源代码项目链接。
- 整理行业资源，帮助快速了解加速器技术生态。

3. **适用场景**
- 研究人员追踪AI芯片及加速算法的最新学术进展。
- 工程师寻找现有的开源工具以优化深度学习模型部署。
- 学生或初学者系统学习AI加速器的工作原理与技术栈。

4. **技术亮点**
该项目作为 curated list（精选列表），其核心价值在于对分散在各地的优质学术资源和开源工具进行了系统化分类与筛选，降低了信息检索成本，而非提供具体的代码实现。
- 链接: https://github.com/LonghornSilicon/awesome-ai-accelerators
- ⭐ 97 | 🍴 12 | 语言: 未知

### morphe-ai
- 1. **中文简介**
Morphe 是一个基于 AI 驱动的 Android APK 修补工作区，旨在提供多智能体流水线以支持 APK 分析、目标挖掘、补丁编写及部署全流程。该项目专注于利用人工智能自动化逆向工程中的复杂任务，帮助开发者高效生成和部署 APK 补丁。

2. **核心功能**
*   利用多智能体流水线自动化 APK 分析与逆向工程流程。
*   智能识别目标应用漏洞或特征，进行精准的“目标狩猎”。
*   自动生成或辅助编写 Smali 代码层面的 APK 修补脚本。
*   集成补丁部署功能，实现从分析到上线的一体化操作。
*   提供 Shell 脚本环境，便于与 Morphe 生态系统及其他工具链集成。

3. **适用场景**
*   需要批量修改或破解 Android 应用的逆向工程师和安全研究员。
*   希望自动化生成应用补丁以提升效率的移动应用开发团队。
*   研究 AI 在多智能体协作下进行软件漏洞利用或修复的技术爱好者。
*   对特定 APK 进行定制化修改（如去广告、功能解锁）并快速部署的场景。

4. **技术亮点**
*   **多智能体协作架构**：采用多代理流水线设计，将复杂的 APK 修补任务分解为分析、定位、编码和部署等独立且协同的步骤。
*   **AI 驱动的代码生成**：结合大语言模型能力，自动处理 Smali 代码层面的逻辑修改，降低手动逆向工程的门槛。
*   **端到端工作流整合**：打通了从静态/动态分析到最终补丁部署的全链路，减少了工具切换的成本。
- 链接: https://github.com/Paresh-Maheshwari/morphe-ai
- ⭐ 90 | 🍴 12 | 语言: Shell
- 标签: android, apk, morphe, morphe-patches, paresh-patches

### plandeck
- ### 1. 中文简介
Plandeck 是一款专为长期运行的 AI 智能体设计的可视化看板工具。它通过动态展示依赖关系解锁、关键路径高亮以及下一步明确指引，让复杂的计划变得直观易懂，彻底取代了难以阅读的 Markdown 文本规划。

### 2. 核心功能
- **实时状态可视化**：以看板形式直观展示任务进度，自动识别并高亮显示关键路径。
- **依赖管理自动化**：清晰呈现任务间的依赖关系，当前置条件满足时自动标记为“就绪”状态。
- **决策辅助**：消除冗长的文本规划，直接指出下一步最明显的操作建议。
- **零依赖架构**：轻量级设计，无需额外安装复杂依赖即可快速部署和使用。

### 3. 适用场景
- **长期 AI Agent 监控**：适用于运行时间较长、步骤复杂的 Claude Code、Codex 或 Cursor 等 AI 编程助手的项目。
- **敏捷任务看板**：开发者用于跟踪和管理具有明确前后置依赖关系的开发任务流。
- **复杂项目规划**：在需要理清多步骤逻辑和关键路径的软件工程或自动化流程管理中作为可视化工具。

### 4. 技术亮点
- **SSE (Server-Sent Events) 支持**：利用 SSE 实现服务端到客户端的实时数据推送，确保看板状态与后端执行同步更新。
- **深度集成主流 AI 工具**：针对 Cursor、Claude Code 等流行 AI 编码环境进行了优化适配。
- **崩溃防护机制**：具备“crash-proof”特性，增强了在长时间运行过程中的稳定性。
- 链接: https://github.com/OthmanAdi/plandeck
- ⭐ 26 | 🍴 0 | 语言: JavaScript
- 标签: agent-skill, agentic, ai-agents, claude-code, codex

### rust-ai-agent
- 基于您提供的项目元数据（名称 `rust-ai-agent`、语言 `Rust`、描述为 `None`、星标 24），由于缺乏具体的代码仓库内容或详细描述，以下分析基于项目名称及主流 Rust AI Agent 库的通用特性进行推断。请注意，这仅是一个通用性分析，实际功能需以具体代码为准。

1. **中文简介**
   该项目是一个基于 Rust 语言构建的 AI 智能体框架或工具集。它旨在利用 Rust 的高性能和内存安全特性，为人工智能应用提供高效的代理控制能力。虽然具体描述缺失，但其核心定位是服务于需要低延迟和高并发处理的 AI 交互场景。

2. **核心功能**
   *   提供高性能的异步运行时支持，确保 AI 请求处理的高效性。
   *   集成主流大语言模型（LLM） API 接口，实现自然语言交互。
   *   支持智能体的状态管理与上下文记忆，维持对话连贯性。
   *   具备插件化架构，允许开发者扩展自定义的工具函数或逻辑模块。

3. **适用场景**
   *   需要高并发和低延迟响应的企业级 AI 客服系统后端。
   *   对资源占用敏感的边缘计算设备上的本地 AI 助手部署。
   *   构建复杂的自动化工作流，如自动代码生成或数据分析代理。
   *   作为高性能微服务的一部分，嵌入到现有的 Rust 技术栈中。

4. **技术亮点**
   *   依托 Rust 的所有权机制，从根本上避免内存泄漏和线程安全问题。
   *   利用 Tokio 等异步运行时，实现非阻塞 I/O，大幅提升吞吐量。
   *   编译期安全检查确保 AI 逻辑组件在运行时的稳定性与可靠性。
- 链接: https://github.com/solenovex/rust-ai-agent
- ⭐ 24 | 🍴 0 | 语言: Rust

### ai-robot
- 基于您提供的信息，以下是针对 `ai-robot` 项目的技术分析：

1. **中文简介**
   该项目是一个运行在瑞芯微 RK3506 开发板上的嵌入式 AI 语音助手。它完全使用纯 C 语言编写，采用单线程事件循环机制，并实现了零动态内存分配，以追求极致的系统稳定性与资源效率。

2. **核心功能**
   - 部署于 Rockchip RK3506 平台的嵌入式语音交互服务。
   - 基于纯 C 语言开发，确保底层代码的高效性与可控性。
   - 采用单线程事件循环架构，简化并发逻辑与资源管理。
   - 实现零动态内存分配，避免内存碎片化并提升运行确定性。

3. **适用场景**
   - 资源受限的物联网（IoT）边缘计算设备开发。
   - 对实时性和内存稳定性要求极高的嵌入式语音交互原型验证。
   - 学习或研究低功耗、无堆内存分配的嵌入式 C 语言编程模式。

4. **技术亮点**
   - **零动态内存分配**：通过静态内存管理彻底消除运行时内存泄漏风险，适合长期运行的嵌入式系统。
   - **极简架构**：单线程模型降低了上下文切换开销，简化了调试与维护复杂度。
- 链接: https://github.com/UIseries/ai-robot
- ⭐ 21 | 🍴 0 | 语言: C

### klinepic-agent-api-examples
- 描述: MCP server and OpenAPI examples for AI agents that turn broker and exchange fills into annotated KLinePic trade-review charts
- 链接: https://github.com/sher1096/klinepic-agent-api-examples
- ⭐ 20 | 🍴 1 | 语言: JavaScript
- 标签: agent-tools, ai-agents, api, candlestick-chart, crypto-trading

### yerevan-city-mcp
- 描述: Order groceries from yerevan-city.am right from a conversation with your AI assistant
- 链接: https://github.com/tjvjk/yerevan-city-mcp
- ⭐ 19 | 🍴 1 | 语言: TypeScript

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

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能全面的中文自然语言处理（NLP）工具箱，集成了敏感词检测、语言识别、信息抽取（如手机号、身份证、邮箱）及大量专业领域词库与语料资源。该项目不仅提供了基础的文本清洗和预处理工具，还涵盖了从传统规则匹配到基于深度学习（如 BERT）的高级 NLP 任务解决方案。它旨在为开发者提供一个一站式的中英文 NLP 开发环境，涵盖从基础工具到前沿模型应用的广泛需求。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词库、反动词表以及基于规则的中文分词和词性标注。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱、地址的自动化抽取，以及基于 BERT 和 BiLSTM 等模型的命名实体识别（NER）和关系抽取。
*   **专业领域词库与知识图谱**：内置丰富的垂直领域词库（如汽车、医疗、法律、财经、IT等）、地名库、人名库，并整合了多个中文知识图谱构建与问答资源。
*   **语音与自然语言生成**：包含中文语音识别（ASR）工具、中文OCR、英文模拟中文发音，以及基于 GPT-2 等模型的文本生成、摘要提取和对话机器人构建工具。
*   **数据集与预训练模型资源**：汇集了海量的中文 NLP 数据集（如闲聊、谣言、医疗对话）、预训练语言模型（BERT, ALBERT, RoBERTa 等）及相关评测基准。

**3. 适用场景**
*   **内容安全与合规审核**：利用敏感词库和暴恐词表，快速构建社交媒体、论坛或即时通讯应用的内容过滤系统。
*   **企业级知识图谱构建**：借助其丰富的领域词库、关系抽取工具和知识图谱资源，构建垂直行业（如医疗、金融）的知识库并支持智能问答。
*   **智能客服与对话系统开发**：使用其中的对话语料、意图识别工具及预训练模型，快速搭建具备上下文理解能力的中文聊天机器人。
*   **非结构化数据信息提取**：在处理简历、文档或新闻时，利用其 NER 和信息抽取模块，自动识别并提取关键实体（如人名、机构、日期）。

**4. 技术亮点**
*   **资源极度丰富且更新活跃**：作为 GitHub 上星标极高的中文 NLP 项目，它聚合了大量最新的开源模型、数据集和工具链，是中文 NLP 领域的“资源库”。
*   **兼顾传统规则与现代深度学习**：既保留了高效实用的正则表达式和词典匹配工具，又全面引入了 BERT、GPT-2 等前沿深度学习模型的应用代码和微调方案。
*   **覆盖全栈 NLP 任务**：从底层的文本预处理、分词，到中层的实体抽取、情感分析，再到高层的对话生成、知识图谱推理，提供了完整的工具链支持。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81782 | 🍴 15245 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35405 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架的模型文件，帮助用户直观地查看和理解模型结构。

2. **核心功能**
*   广泛支持 ONNX、PyTorch、TensorFlow、Keras、CoreML、TensorFlow Lite 和 Safetensors 等格式的模型可视化。
*   提供清晰的模型架构图，展示层连接、张量形状及权重参数细节。
*   支持在浏览器或桌面端直接打开模型文件，无需安装复杂的依赖环境。
*   具备交互式的模型探索功能，允许用户点击特定节点查看详细信息。
*   开源免费，代码托管于 GitHub 并基于 JavaScript 构建，易于部署和使用。

3. **适用场景**
*   **模型调试与验证**：开发者在训练后快速检查模型结构是否符合预期，排查层连接错误。
*   **学术交流与演示**：研究人员制作高质量的网络结构图，用于论文撰写或会议演示。
*   **跨框架迁移分析**：当从 PyTorch 转换为 ONNX 或 TensorFlow Lite 时，用于对比前后模型结构的一致性。
*   **初学者学习**：新手通过可视化工具直观理解复杂神经网络的数据流向和组件构成。

4. **技术亮点**
*   **轻量级与跨平台**：基于 Web 技术构建，支持桌面应用和在线访问，无需重型依赖即可运行。
*   **广泛的生态兼容性**：几乎覆盖当前所有主流的 AI 框架和模型格式，是通用的模型检查利器。
*   **高性能渲染**：能够流畅处理大型复杂模型的可视化，界面响应迅速。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33225 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 基于您提供的GitHub项目信息，以下是关于 **ONNX** 的技术分析报告：

1. **中文简介**
   ONNX（开放神经网络交换）是一个旨在实现机器学习模型互操作性的开源标准。它允许开发者在不同深度学习框架之间轻松迁移和部署模型，打破了平台间的壁垒。通过这一标准，研究人员和工程师可以更高效地在异构硬件上运行AI应用。

2. **核心功能**
   - **框架互操作性**：支持将模型从PyTorch、TensorFlow或Scikit-learn等主流框架导出为统一的ONNX格式。
   - **跨平台部署**：提供统一的运行时环境，使模型能在多种硬件加速器（如CPU、GPU、NPU）上无缝执行。
   - **模型优化与转换**：内置工具链可对导出模型进行图优化、量化和剪枝，以提升推理速度和减少资源占用。
   - **标准化计算图表示**：定义了一套标准化的算子和张量操作规范，确保不同框架生成的模型逻辑一致。

3. **适用场景**
   - **混合框架开发**：在训练阶段使用PyTorch，而在生产部署阶段转换为ONNX以利用特定硬件加速器的场景。
   - **边缘设备部署**：需要将大型云端模型压缩并迁移到手机、IoT设备等资源受限终端的场景。
   - **企业级MLOps流水线**：在多团队协作中，统一模型交付格式，避免框架锁定，便于后续维护和迭代。

4. **技术亮点**
   - **广泛的生态兼容性**：作为行业事实标准，被微软、Facebook、Amazon等主要科技公司广泛支持，拥有最广泛的框架覆盖率和社区资源。
   - **高性能推理后端**：配套的ONNX Runtime提供了高度优化的推理引擎，支持即时编译（JIT）和硬件特定的内核调度，显著降低延迟。
- 链接: https://github.com/onnx/onnx
- ⭐ 21142 | 🍴 3968 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
本项目是一本关于机器学习工程领域的开源指南，旨在系统性地解答大规模分布式训练及推理中的常见难题。它深入探讨了从硬件选型、网络通信到软件优化的全方位最佳实践，帮助开发者构建高效稳定的机器学习基础设施。

2. **核心功能**
*   提供大规模分布式训练的系统性故障排查与调试策略。
*   详解LLM推理过程中的优化技巧与性能调优方法。
*   涵盖GPU集群管理、存储IO优化及Slurm调度器配置指南。
*   介绍PyTorch等框架在扩展性方面的最佳实践与陷阱规避。

3. **适用场景**
*   在大型GPU集群上训练或微调大语言模型（LLM）时的工程落地。
*   解决分布式训练中遇到的OOM、通信瓶颈或节点故障问题。
*   优化高并发LLM推理服务的延迟与吞吐量。
*   搭建和维护企业级MLOps平台的基础架构设计。

4. **技术亮点**
*   聚焦于“大规模”与“分布式”场景，填补了传统教程在工程细节上的空白。
*   结合PyTorch、Transformers等主流生态，提供可落地的代码级建议。
*   内容覆盖硬件底层至应用层，形成完整的机器学习工程知识体系。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18397 | 🍴 1172 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17316 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13134 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11570 | 🍴 907 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及NLP项目的代码合集。它涵盖了从基础到高级的多种算法实现，旨在为开发者提供丰富的实战案例。作为一个精选资源库，它帮助学习者快速掌握各领域的核心技术与应用。

2. **核心功能**
*   提供涵盖机器学习、深度学习、计算机视觉和自然语言处理的完整项目代码库。
*   包含大量可直接运行的示例，便于用户快速上手并进行本地测试。
*   作为“Awesome”列表，整理了高质量的相关资源和项目链接。
*   支持多领域交叉学习，帮助用户构建全面的AI知识体系。

3. **适用场景**
*   AI初学者希望通过实际代码案例快速理解理论概念。
*   数据科学家寻找特定算法（如CNN、RNN、Transformer）的参考实现。
*   需要构建AI作品集以求职或展示技能的开发者。
*   研究人员希望复现经典论文或探索前沿技术应用的场景。

4. **技术亮点**
*   **规模庞大且分类清晰**：收录500个项目并按领域细分，覆盖主流AI技术栈。
*   **全代码导向**：不仅提供理论，更强调代码实现，具备极高的实践价值。
*   **社区精选质量高**：作为“Awesome”列表，通常经过社区筛选，保证项目的代表性和有效性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35405 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架的模型文件，帮助用户直观地查看和理解模型结构。

2. **核心功能**
*   广泛支持 ONNX、PyTorch、TensorFlow、Keras、CoreML、TensorFlow Lite 和 Safetensors 等格式的模型可视化。
*   提供清晰的模型架构图，展示层连接、张量形状及权重参数细节。
*   支持在浏览器或桌面端直接打开模型文件，无需安装复杂的依赖环境。
*   具备交互式的模型探索功能，允许用户点击特定节点查看详细信息。
*   开源免费，代码托管于 GitHub 并基于 JavaScript 构建，易于部署和使用。

3. **适用场景**
*   **模型调试与验证**：开发者在训练后快速检查模型结构是否符合预期，排查层连接错误。
*   **学术交流与演示**：研究人员制作高质量的网络结构图，用于论文撰写或会议演示。
*   **跨框架迁移分析**：当从 PyTorch 转换为 ONNX 或 TensorFlow Lite 时，用于对比前后模型结构的一致性。
*   **初学者学习**：新手通过可视化工具直观理解复杂神经网络的数据流向和组件构成。

4. **技术亮点**
*   **轻量级与跨平台**：基于 Web 技术构建，支持桌面应用和在线访问，无需重型依赖即可运行。
*   **广泛的生态兼容性**：几乎覆盖当前所有主流的 AI 框架和模型格式，是通用的模型检查利器。
*   **高性能渲染**：能够流畅处理大型复杂模型的可视化，界面响应迅速。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33225 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目汇集了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。它涵盖了从基础数学工具到主流框架（如Keras、Matplotlib）的关键概念与代码片段，旨在帮助研究者快速回顾和查阅重要知识点。

**2. 核心功能**
*   提供针对深度学习及机器学习领域的标准化速查指南。
*   集成NumPy、SciPy等数值计算库的关键用法说明。
*   包含Matplotlib数据可视化库的快速参考手册。
*   覆盖Keras等深度学习框架的基础操作与API摘要。
*   整理人工智能领域通用的算法逻辑与数学公式备忘。

**3. 适用场景**
*   研究人员在开发模型时快速查阅 forgotten API 或语法细节。
*   初学者系统性地复习机器学习数学基础和常用库的使用规范。
*   团队内部进行技术分享或新人入职培训时的参考资料。
*   备考相关技术面试时，作为快速记忆关键概念的辅助材料。

**4. 技术亮点**
*   **高度浓缩**：将复杂的框架和数学知识提炼为易于记忆的图表形式。
*   **覆盖面广**：整合了从数据处理（NumPy/SciPy）到建模（Keras）及展示（Matplotlib）的全流程关键点。
*   **社区认可度高**：拥有超过1.5万星标，证明其在AI开发者群体中的广泛实用性和权威性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，涵盖Python、数学、机器学习及深度学习等热门领域，旨在帮助零基础用户顺利入门并实现就业。资源库整理了近200个实战案例与项目，并提供免费配套教材，支持TensorFlow、PyTorch等多种主流框架的学习与应用。

2. **核心功能**
- 提供从基础到进阶的系统化AI学习路径，覆盖数据科学、NLP、CV等方向。
- 收录近200个实战案例和项目代码，注重动手实践与就业技能培养。
- 免费提供配套教材和教学资源，降低初学者入门门槛。
- 整合多种主流AI框架（如PyTorch、TensorFlow、Keras等）的技术栈。

3. **适用场景**
- 希望从零开始系统学习人工智能与数据科学的初学者。
- 需要大量实战项目参考以增强简历竞争力的求职人员。
- 希望快速掌握特定AI领域（如NLP或计算机视觉）开发技能的开发者。

4. **技术亮点**
- 资源高度集成：将理论知识、代码实战与免费教材融为一体，形成完整闭环。
- 覆盖面广：涉及算法、数据分析、深度学习等多个细分领域的热门技术栈。
- 社区认可度高：拥有超过1.3万星标，证明其内容质量和实用性受到广泛验证。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13134 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它通过声明式配置降低开发门槛，让开发者能够专注于数据与模型逻辑，而无需编写大量底层代码。

2. **核心功能**
*   **低代码/声明式建模**：通过 YAML 配置文件定义模型架构和数据管道，大幅减少样板代码。
*   **广泛的模型支持**：原生支持深度学习、传统机器学习算法以及最新的大语言模型（如 LLaMA、Mistral）的微调。
*   **端到端工作流**：涵盖从数据预处理、模型训练到评估和部署的全生命周期管理。
*   **多模态能力**：支持处理图像、文本、表格等多种类型的数据输入，适用于计算机视觉和自然语言处理任务。

3. **适用场景**
*   **快速原型开发**：数据科学家希望在不深入复杂代码细节的情况下，快速验证不同模型架构的效果。
*   **LLM 微调与应用**：需要对开源大语言模型（如 LLaMA 2、Mistral）进行领域适配或特定任务微调的企业或研究者。
*   **生产级 AI 部署**：需要标准化、可复现且易于维护的机器学习流水线，以便将模型稳定部署到生产环境。

4. **技术亮点**
*   **Hugging Face 集成**：深度集成 Hugging Face Transformers，方便直接调用和微调主流开源 LLM。
*   **可解释性与可视化**：内置强大的可视化工具，帮助用户理解模型决策过程和评估指标。
*   **社区驱动与扩展性**：拥有活跃的社区和丰富的插件生态，支持自定义组件和后端扩展。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11738 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9134 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3100 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6986 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6254 | 🍴 741 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且功能丰富的中文自然语言处理工具集，旨在为开发者提供从基础文本清洗到高级语义理解的各类资源。它整合了敏感词检测、实体抽取、情感分析及大量专业领域的词库与数据，是构建中文 NLP 应用的强力辅助库。

2. **核心功能**
- 提供中英文敏感词过滤、繁简转换及文本纠错等基础文本处理能力。
- 集成多种命名实体识别（NER）工具，支持中文姓名、手机号、身份证、邮箱及地址等信息的自动抽取。
- 包含海量的领域专用词库（如医学、法律、汽车、财经）及预训练语言模型资源。
- 提供情感分析、文本相似度匹配、关键词抽取及自动摘要等高级语义分析功能。
- 涵盖语音识别语料、知识图谱构建工具及对话机器人相关的数据集与代码示例。

3. **适用场景**
- **内容安全审核**：利用敏感词库和情感分析功能，快速构建社交媒体或论坛的内容过滤系统。
- **信息抽取与结构化**：在客服系统或数据分析平台中，从非结构化文本（如聊天记录、新闻）中提取关键实体（人名、地点、机构）。
- **智能问答与聊天机器人**：结合知识图谱资源和对话数据集，开发具备领域知识（如医疗、法律）的智能客服或闲聊机器人。
- **NLP 算法研究与开发**：作为研究人员或工程师的实验平台，利用其提供的基准数据集、预训练模型和评估指标进行算法验证。

4. **技术亮点**
- **资源高度聚合**：将分散的中英文 NLP 数据集、词库、模型代码及学术报告集中管理，极大降低了中文 NLP 的开发门槛。
- **覆盖领域广泛**：不仅包含通用 NLP 任务，还深入垂直领域（如医疗、法律、金融），提供了专业的领域知识图谱和数据。
- **紧跟前沿技术**：集成了 BERT、GPT-2、ALBERT 等主流预训练模型的应用案例及微调代码，支持最新的自然语言生成与理解任务。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81782 | 🍴 15245 | 语言: Python

### LlamaFactory
- ### LlamaFactory GitHub项目分析

1. **中文简介**
   LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目已被 ACL 2024 收录，旨在简化复杂模型的训练流程。它通过集成多种前沿技术，为研究人员和开发者提供了便捷的模型定制解决方案。

2. **核心功能**
   - 支持百余项主流 LLM 及 VLM 的统一高效微调，兼容 LoRA、QLoRA 等轻量化策略。
   - 内置 RLHF（基于人类反馈的强化学习）、DPO 等对齐算法，优化模型输出质量。
   - 提供量化训练（Quantization）与混合专家模型（MoE）支持，显著降低硬件资源需求。
   - 涵盖指令微调（Instruction Tuning）与 Agent 开发能力，适应多样化应用场景。

3. **适用场景**
   - **学术研究**：需要快速复现或实验不同大模型微调效果的研究人员。
   - **企业落地**：希望在有限算力下，针对垂直领域数据对开源模型进行私有化部署的企业开发者。
   - **多模态应用**：需要同时处理文本与图像理解任务的视觉语言模型定制场景。

4. **技术亮点**
   - 实现了“统一”架构，用户无需切换不同框架即可微调多种异构模型。
   - 深度整合 HuggingFace Transformers 与 PEFT 库，兼顾易用性与高性能。
   - 对 QLoRA 和 MoE 等先进技术的原生支持，使得在消费级显卡上训练大规模模型成为可能。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73239 | 🍴 8946 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. 中文简介
该项目收集并公开了来自 Anthropic、OpenAI、Google、xAI 等多家主流 AI 厂商的系统提示词（System Prompts），涵盖 Claude、ChatGPT、Gemini 等知名模型及开发工具。内容更新频繁，旨在为社区提供关于大型语言模型底层指令结构的透明化参考。

### 2. 核心功能
- **多厂商提示词聚合**：整合了 Anthropic、OpenAI、Google 和 xAI 等多个主要 AI 提供商的系统指令数据。
- **覆盖主流模型与工具**：包含 Claude、ChatGPT、Gemini 以及 Cursor、Copilot 等开发者工具的底层配置信息。
- **定期动态更新**：持续追踪并收录最新的模型版本和系统提示词变更，保持数据时效性。

### 3. 适用场景
- **提示词工程研究**：帮助研究人员深入理解不同大模型的内部指令结构和行为逻辑。
- **AI 安全与伦理分析**：用于评估模型的安全对齐机制、内容过滤策略及潜在的系统漏洞。
- **开发者调试与优化**：辅助开发者通过参考官方指令来优化应用层的 Prompt 设计或排查交互异常。

### 4. 技术亮点
- **跨平台对比价值**：提供了不同商业闭源模型之间的系统指令横向对比数据，极具参考价值。
- **高社区关注度**：拥有超过 5.7 万星标，表明其在 AI 社区中作为“非官方文档”或“逆向工程资源”的高认可度。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 57255 | 🍴 9471 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由Microsoft推出，通过结构化的学习路径帮助初学者系统性地构建AI技能体系。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉等主题的完整课程体系。
*   采用Jupyter Notebook格式，支持交互式代码学习与即时实践。
*   内容设计通俗易懂，适合零基础的编程或AI新手入门。
*   覆盖从基础概念到CNN、GAN、RNN等高级技术的广泛知识点。
*   遵循标准化的12周学习进度，确保循序渐进的技能提升。

3. **适用场景**
*   希望从零开始系统学习人工智能概念的初学者。
*   需要结构化教学材料来补充学校或公司内部培训的教育机构。
*   希望通过实际代码练习快速上手ML/DL开发的数据科学爱好者。
*   寻求免费、高质量且经过验证的AI教学资源的企业培训师。

4. **技术亮点**
*   依托Jupyter Notebook实现理论与代码实践的无缝结合。
*   由Microsoft官方背书，保证了内容的权威性与教学质量的标准化。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52245 | 🍴 10562 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. 中文简介
该项目是一个全面的人工智能学习资源库，涵盖了从数学基础（线性代数）到前沿框架（PyTorch、TensorFlow 2）的完整技术栈。它通过数据分析与机器学习的实战案例，深入讲解了包括深度学习、自然语言处理及推荐系统在内的多种核心算法。

### 2. 核心功能
*   **多框架支持**：整合了 PyTorch 和 TensorFlow 2 等主流深度学习框架的实践教程。
*   **经典算法复现**：详细实现了 SVM、K-Means、Logistic 回归、AdaBoost 等传统机器学习算法。
*   **深度学习专项**：涵盖 DNN、RNN、LSTM 及 NLP（NLTK）等高级深度学习模型的应用。
*   **推荐系统与数据科学**：包含基于协同过滤的推荐系统实现以及 PCA、SVD 等数据分析技术。

### 3. 适用场景
*   **AI 初学者入门**：适合希望从零开始构建机器学习知识体系的学习者。
*   **算法工程师面试准备**：可用于复习常见 ML/DL 算法原理及代码实现以应对技术面试。
*   **工程实战参考**：为需要快速落地数据分析或简单推荐系统的开发者提供代码模板。

### 4. 技术亮点
*   **理论与实践结合**：不仅提供算法代码，还辅以线性代数等数学基础，确保理解深度。
*   **生态覆盖广**：同时兼顾了 scikit-learn 传统库与现代深度学习框架，适应不同阶段需求。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42377 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38185 | 🍴 6390 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35405 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33740 | 🍴 4691 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28527 | 🍴 3478 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25887 | 🍴 2920 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域的AI项目资源库，并附带完整代码实现。该项目旨在为开发者提供从基础算法到高级应用的全面实践指南，是学习人工智能技术的优质资料库。

2. **核心功能**
*   提供500个经过分类的AI实战项目，覆盖主流技术栈。
*   所有项目均包含可运行的源代码，便于直接学习与复现。
*   内容横跨机器学习、深度学习、计算机视觉和NLP四大核心领域。
*   作为Awesome列表的一部分，具有高度的结构化和筛选价值。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握各分支技术的基础应用。
*   数据科学家或工程师寻找特定场景（如图像识别、文本分类）的代码参考。
*   教育培训机构用于制作课程案例或布置编程作业。

4. **技术亮点**
*   **全面性与系统性**：整合了500个项目，构建了从理论到实践的完整知识图谱。
*   **代码即用性**：强调“with code”，确保每个概念都有对应的落地实现，降低学习门槛。
*   **多领域覆盖**：同时囊括CV和NLP等热门方向，满足跨领域学习需求。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35406 | 🍴 7351 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 以下是关于 GitHub 项目 **Skyvern** 的技术分析报告：

1. **中文简介**
   Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流平台。它通过集成大语言模型（LLM）和计算机视觉技术，能够像人类一样理解网页界面并执行操作。该项目旨在替代传统的机器人流程自动化（RPA），提供更灵活、智能的浏览器自动化解决方案。

2. **核心功能**
   *   **AI 驱动的动作执行**：利用 LLM 分析网页内容并生成 Playwright 代码以自动化交互，无需预先录制步骤。
   *   **视觉感知能力**：结合计算机视觉技术识别页面元素，即使面对动态变化或非标准布局也能稳定运行。
   *   **结构化数据提取**：能够从网页中精准抓取非结构化或半结构化的数据，并将其转换为 JSON 等可用格式。
   *   **自然语言工作流定义**：用户只需通过自然语言描述任务目标，系统即可自动规划并执行相应的浏览器操作序列。
   *   **企业级 API 集成**：提供标准的 RESTful API，便于与其他业务系统集成，实现端到端的自动化流程。

3. **适用场景**
   *   **跨平台数据录入与同步**：自动将内部系统数据填入各种第三方 Web 门户（如政府申报网站、供应商门户）。
   *   **电商价格监控与比价**：定期访问多个电商平台，提取商品价格、库存及促销信息并进行对比分析。
   *   **在线表单自动化填写**：处理复杂的注册、申请或反馈表单，自动识别字段并完成填写提交。
   *   **Web 应用测试与验收**：作为 QA 团队的辅助工具，自动生成和维护基于视觉理解的 UI 回归测试用例。

4. **技术亮点**
   *   **超越传统选择器**：不依赖易碎的 CSS/XPath 选择器，而是通过语义理解和视觉定位来增强稳定性。
   *   **Playwright 原生集成**：底层基于高性能的 Playwright 框架，支持 Chromium、Firefox 和 WebKit 浏览器引擎。
   *   **自适应学习能力**：在处理新网站时，能够根据上下文快速适应页面布局的变化，降低维护成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22218 | 🍴 2082 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证及团队协作，并配备开发者API以简化工作流。

2. **核心功能**
*   支持图像、视频及3D点云的多模态数据标注。
*   集成AI辅助标注功能以提升数据标记效率与准确性。
*   提供完善的质量保证机制与团队多人协作能力。
*   开放开发者API，便于集成到现有自动化流水线中。

3. **适用场景**
*   需要大规模构建图像分类或目标检测训练数据集的研发团队。
*   进行语义分割或实例分割等复杂视觉任务的数据标注项目。
*   视频分析领域中对动态目标进行轨迹跟踪与帧间标注的场景。
*   自动驾驶或机器人视觉项目中对3D点云数据进行注释的工作流。

4. **技术亮点**
*   兼容PyTorch和TensorFlow等主流深度学习框架生态。
*   提供从开源社区版到企业级服务的灵活部署方案。
*   内置智能标注算法，显著降低人工标注成本并提高一致性。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16281 | 🍴 3746 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目旨在为计算机视觉提供高级的可解释性AI解决方案，支持CNN、Vision Transformer等多种模型结构。它涵盖了分类、目标检测、分割及图像相似度等任务，帮助用户直观理解模型决策依据。

2. **核心功能**
*   全面支持CNN和Vision Transformer架构的梯度可视化。
*   兼容图像分类、目标检测、语义分割及图像相似度计算等多种任务。
*   集成Grad-CAM、Score-CAM等多种主流可解释性算法。
*   提供直观的注意力图生成与可视化功能。

3. **适用场景**
*   深度学习模型调试，通过可视化确认模型是否关注正确特征。
*   医疗影像分析，辅助医生理解AI诊断结果的可信度。
*   自动驾驶系统开发，验证车辆对障碍物或交通标志的检测逻辑。
*   学术研究与教学，用于演示和解释计算机视觉模型的内部机制。

4. **技术亮点**
*   高度模块化设计，轻松适配PyTorch中的不同网络层和模型类型。
*   广泛支持前沿架构，包括最新的Vision Transformer变体。
*   社区活跃且星标数高（超1.2万），文档完善，便于快速上手和二次开发。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在通过可微分的图像处理操作，简化深度学习与计算机视觉任务的集成开发。

2. **核心功能**
*   提供基于 PyTorch 的可微分几何计算模块，支持梯度反向传播。
*   包含丰富的图像预处理、增强及传统计算机视觉算法实现。
*   针对机器人、3D 视觉和空间推理任务进行了深度优化。
*   无缝集成深度学习工作流，便于在神经网络中直接调用视觉算子。

3. **适用场景**
*   需要端到端训练的计算机视觉模型开发（如姿态估计、SLAM）。
*   机器人导航中的空间感知与环境理解系统。
*   图像增强与预处理流水线在深度学习管道中的集成。
*   涉及几何约束的深度学习和神经渲染研究。

4. **技术亮点**
*   作为首个主打“可微分计算机视觉”的 PyTorch 库，填补了传统 CV 与现代深度学习之间的接口空白。
*   完全兼容 PyTorch 生态系统，利用 GPU 加速实现高性能几何运算。
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
- ⭐ 3458 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3283 | 🍴 402 | 语言: Python
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

