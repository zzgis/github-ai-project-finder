# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- ### 1. 中文简介
Thinking Orbs 是一款专为 AI 及智能体用户界面设计的点状思维轨道加载指示器组件库。它包含六种精心调优的状态动画和两种尺寸选项，并支持自动适配深色与浅色模式，旨在提升交互体验的细腻度。

### 2. 核心功能
*   **多状态动画**：提供六种经过微调的思维轨道加载状态，模拟不同的思考或处理阶段。
*   **双尺寸支持**：内置两种不同大小的图标规格，适应多样化的布局需求。
*   **自适应主题**：具备自动识别系统偏好或应用主题的能力，无缝切换深色与浅色模式。
*   **AI/Agent 专用设计**：针对人工智能对话、代理任务等场景优化视觉反馈，增强“正在思考”的拟人化感知。

### 3. 适用场景
*   **AI 聊天机器人界面**：在模型生成回复前显示“思考中”状态，提升等待期间的用户体验。
*   **智能体任务执行**：用于展示后台 Agent 正在处理复杂逻辑或多步骤任务时的加载状态。
*   **生成式内容预览**：在图像、文本或代码生成过程中，作为动态占位符减少用户焦虑感。

### 4. 技术亮点
*   **TypeScript 原生开发**：基于 TypeScript 构建，提供完整的类型定义，便于现代前端框架集成。
*   **轻量级无依赖**：专注于视觉组件本身，通常无需额外重型依赖即可嵌入现有项目。
*   **高可定制性**：通过参数化配置快速调整动画节奏、颜色及大小，灵活匹配品牌风格。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 573 | 🍴 35 | 语言: TypeScript

### BossConsole
- 1. **中文简介**
BossConsole 是一个开源的多平台 AI 智能体控制中枢，基于 JVM 原生构建（非 Electron），支持多线程操作。它提供了一个集真实浏览器、终端、编辑器及密钥管理于一体的控制台，用于运行 Claude Code、Codex、Gemini 或 OpenCode 等工具，并集成 100 多种 MCP 工具。该项目专为企业级应用及科学研究场景设计。

2. **核心功能**
*   原生多平台桌面应用，基于 Kotlin Multiplatform 和 Compose 构建，提供高性能 JVM 体验而非 Electron 包装。
*   集成真实浏览器、终端和代码编辑器，支持对 Claude Code、Codex、Gemini 等多种 AI 智能体的统一操控。
*   内置 100 多种 Model Context Protocol (MCP) 工具，实现丰富的上下文交互与扩展能力。
*   提供企业级安全特性，包括 RBAC（基于角色的访问控制）及安全的密钥管理。
*   支持热重载（Hot-reload）及多线程处理，确保开发调试的高效性与系统的响应速度。

3. **适用场景**
*   **企业级 AI 开发平台**：需要统一管控多个 AI 智能体、确保数据安全和权限隔离的大型技术团队。
*   **科研与数据处理**：研究人员利用 MCP 工具和实时终端进行复杂数据分析、模型测试及自动化实验。
*   **高级开发者工作流**：希望在一个界面中同时使用浏览器、代码编辑器和多个 LLM 代理进行高效编码的资深程序员。

4. **技术亮点**
*   **JVM 原生架构**：相比常见的 Electron 应用，具有更低的内存占用和更高的启动/运行性能。
*   **Kotlin Multiplatform (KMP)**：利用 KMP 技术实现跨平台兼容，同时保持代码的高复用性和类型安全。
*   **MCP 生态整合**：深度集成 Model Context Protocol，无缝连接外部数据和工具，极大扩展了 AI 智能体的能力边界。
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 152 | 🍴 2 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### open-ai-canvas
- 描述: 面向 AI 影视创作的开源无限画布工作台，集成多模态生成、分镜编排、素材管理与 Agent 工作流。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 68 | 🍴 18 | 语言: TypeScript

### pgContext
- 1. **中文简介**
pgContext 是一个构建在 PostgreSQL 数据库内部的完整 AI 搜索引擎。它利用 Rust 语言开发，旨在为关系型数据库原生集成强大的语义搜索与人工智能能力。

2. **核心功能**
*   **原生集成**：直接在 Postgres 内部运行 AI 搜索功能，无需外部复杂部署。
*   **语义搜索**：支持基于含义而非单纯关键词的查询匹配。
*   **Rust 驱动**：使用高性能、高安全性的 Rust 语言构建底层引擎。
*   **数据持久化**：结合 SQL 数据库的 ACID 特性保障数据一致性。

3. **适用场景**
*   **企业级知识库**：在现有 Postgres 系统中直接实现智能文档检索。
*   **混合查询应用**：需要同时执行结构化 SQL 查询和非结构化语义搜索的场景。
*   **低延迟 AI 服务**：希望避免跨网络调用外部 API 以降低延迟的应用。

4. **技术亮点**
*   **Rust 性能优势**：利用 Rust 的内存安全和执行效率提升搜索速度。
*   **数据库内计算**：减少数据移动，实现计算与存储的紧密耦合。
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 63 | 🍴 3 | 语言: Rust

### AIGuardSIEM
- 1. **中文简介**
AIGuardSIEM 是一款生产级 SIEM/XDR 平台，支持每秒处理超过 100 万条事件（EPS），并实现低于 15 毫秒的检测延迟。该项目由 C++、Go 和 Python 构建，集成了 DPDK 捕获、ONNX 机器学习推理、Sigma 规则、eBPF 监控及 SOAR 自动化响应功能。

2. **核心功能**
- 高性能数据处理：利用 DPDK 实现高速网络包捕获，支持百万级 EPS 吞吐量。
- 智能威胁检测：结合 ONNX 机器学习模型与 Sigma 安全规则进行实时异常和入侵检测。
- 深度系统监控：通过 eBPF 技术提供细粒度的端点与内核层可观测性。
- 自动化响应：内置 SOAR（安全编排、自动化及响应）能力，加速事件处置流程。

3. **适用场景**
- 大型企业的 SOC 中心：需要处理海量日志并快速定位高级持续性威胁（APT）。
- 云原生安全架构：基于 Kubernetes 部署，适合微服务和容器化环境的安全监控。
- 高并发网络防御：对检测延迟有极致要求（<15ms）的实时入侵检测系统。

4. **技术亮点**
- 混合语言栈优化：使用 C++ 处理底层高性能数据流，Go 和 Python 分别用于服务编排和脚本扩展，兼顾性能与开发效率。
- 现代化安全协议集成：同时支持 Sigma 规则标准化和 MITRE ATT&CK 框架映射，提升威胁情报的通用性与可操作性。
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 55 | 🍴 4 | 语言: C++
- 标签: anomaly-detection, cybersecurity, dpdk, endpoint-security, incident-response

### Finn-loop
- 描述: The Finn-loop: a 3-skill AI software factory for Claude Code — spec, build, review. Humans merge.
- 链接: https://github.com/finna/Finn-loop
- ⭐ 54 | 🍴 5 | 语言: JavaScript
- 标签: agentic-workflows, ai-agents, claude-code, github, linear

### editaplot
- 描述: AI-guided editable scientific figures with Codex and local Origin/OriginPro
- 链接: https://github.com/hang-jin/editaplot
- ⭐ 40 | 🍴 2 | 语言: Python
- 标签: codex-skill, editable-figures, research, scientific-visualization, windows

### pm-manager
- 描述: Know what to fix next — local .pm governance skill pack for AI coding agents (Spec Kit–inspired).
- 链接: https://github.com/wei63w/pm-manager
- ⭐ 36 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude-code, cursor, project-management

### Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- 描述: The Industry‑Oriented AI Engineering Program blends theory with hands‑on projects. Students gain expertise in open‑source LLMs, prompt engineering, fine‑tuning, and agent development, preparing for impactful careers in healthcare AI, autonomous systems, and innovation.
- 链接: https://github.com/AnantVerma-2022/Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- ⭐ 33 | 🍴 0 | 语言: Jupyter Notebook

### AIS3-2026-Material
- 描述: AIS3 2026 - AI 資安應用實作與模型安全
- 链接: https://github.com/stwater20/AIS3-2026-Material
- ⭐ 30 | 🍴 0 | 语言: Jupyter Notebook

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个综合性的自然语言处理（NLP）资源库，汇集了海量的中文及多语言数据集、预训练模型、工具包和学术资料。该项目涵盖了从基础文本处理（如敏感词检测、分词、实体抽取）到高级应用（如知识图谱构建、语音识别、对话系统）的全方位内容。它旨在为开发者、研究人员和学生提供一站式的中英文 NLP 开发资源与学习指南。

2. **核心功能**
- **基础文本处理与增强**：提供敏感词过滤、繁简转换、中英文发音模拟、文本纠错、数据增强（EDA）及各类正则表达式匹配工具。
- **大规模语料与知识库**：整合了包括人名、地名、公司名、古诗词、医学/法律/汽车等专业领域的词库，以及百度百科、百度知道等大规模问答和对话语料。
- **前沿模型与算法实现**：收录了基于 BERT、GPT-2、ALBERT 等主流模型的预训练代码、微调示例及命名实体识别（NER）、关系抽取等任务的最佳实践。
- **语音与多模态支持**：包含中文语音识别（ASR）数据集、音频增广库、语音情感分析及音素对齐工具。
- **知识图谱与问答系统**：提供知识图谱构建工具、跨语言百科图谱（XLORE）、医疗/金融领域 QA 系统及自动对联等创意应用。

3. **适用场景**
- **NLP 初学者与学习者**：用于查找中文 NLP 的学习路线、经典论文解读、课程资料（如 CS224n）及基础数据集，快速入门。
- **企业级文本分析开发**：在需要敏感词监控、用户评论情感分析、自动摘要或关键词提取的业务场景中，直接调用现成的词库和模型代码。
- **垂直领域 AI 应用构建**：在医疗、金融、法律等专业领域，利用项目中的专属词库、数据集和预训练模型进行定制化知识图谱或智能问答系统的开发。
- **学术研究与创新实验**：研究人员可借此获取最新的开源数据集（如 CLUE 基准）、基线模型代码及对抗生成、注意力可视化等前沿研究素材。

4. **技术亮点**
- **资源极度丰富且全面**：不仅包含代码，还涵盖了数据集、词库、论文、教程和行业报告，是中文 NLP 领域罕见的“百科全书”式仓库。
- **紧跟技术前沿**：持续更新以涵盖 Transformer、BERT、GPT 等最新架构的中文适配版本及 SOTA 模型实现。
- **强调中文特性优化**：特别针对中文痛点提供了大量专用工具，如中文 OCR（cnocr）、中文拼音标注、中文数字转换及细粒度命名实体识别（CLUENER）。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。每个项目均附带完整代码，为开发者提供从理论到实践的全方位参考。它旨在通过丰富的实战案例，帮助用户快速掌握人工智能技术的实际应用。

2. **核心功能**
- 提供500个经过验证的AI实战项目，覆盖主流技术栈。
- 每个项目均包含可直接运行的源代码，便于学习与复现。
- 分类清晰，按机器学习、深度学习、计算机视觉和NLP进行组织。
- 整合了Python生态下的常用AI库与工具链示例。

3. **适用场景**
- AI初学者希望系统性地通过代码实践来理解基础算法。
- 开发者需要寻找特定领域（如CV或NLP）的项目灵感或模板。
- 学生或研究人员用于课程作业参考或学术研究的基线对比。

4. **技术亮点**
- 项目规模庞大且分类全面，是AI领域的“Awesome List”式权威资源。
- 强调代码落地能力，直接提供可执行的解决方案而非仅理论描述。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和文件格式，帮助用户直观地查看模型结构。该工具旨在简化复杂模型的分析与调试过程。

2. **核心功能**
- 支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供直观的图形化界面，清晰展示神经网络的层结构及数据流向。
- 兼容多种后端格式，如 safetensors 和 TensorFlow Lite，适应不同部署需求。
- 允许用户导入本地文件或直接输入 URL 进行在线模型分析。

3. **适用场景**
- 深度学习研究人员用于快速检查模型架构是否正确构建。
- 工程师在模型转换或部署前，验证不同框架间模型的一致性。
- 开发者调试神经网络时，定位特定层或参数的配置问题。
- 非专业用户通过可视化界面理解 AI 模型的内部工作原理。

4. **技术亮点**
基于 JavaScript 开发，具有跨平台兼容性，无需安装重型依赖即可运行，且拥有极高的社区活跃度（3万+星标）。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21200 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面涵盖机器学习工程实践的指南，旨在帮助开发者构建、训练和优化大规模模型。内容深入探讨了从底层基础设施到高层应用的全链路技术细节。

2. **核心功能**
- 提供大规模模型训练与推理的最佳实践及调试技巧。
- 详解GPU集群管理、网络优化及存储解决方案以提升可扩展性。
- 集成PyTorch和Transformers库，指导LLM的高效部署与维护。

3. **适用场景**
- 需要在Slurm集群上高效运行大规模深度学习训练任务。
- 优化大型语言模型（LLM）的推理延迟与硬件资源利用率。
- 解决分布式训练中的网络瓶颈、内存溢出等工程难题。

4. **技术亮点**
- 聚焦生产级MLOps实战，填补了理论研究与实际工程落地之间的空白。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18451 | 🍴 1178 | 语言: Python
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
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11588 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10672 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。每个项目均附带完整代码，为开发者提供从理论到实践的全方位参考。它旨在通过丰富的实战案例，帮助用户快速掌握人工智能技术的实际应用。

2. **核心功能**
- 提供500个经过验证的AI实战项目，覆盖主流技术栈。
- 每个项目均包含可直接运行的源代码，便于学习与复现。
- 分类清晰，按机器学习、深度学习、计算机视觉和NLP进行组织。
- 整合了Python生态下的常用AI库与工具链示例。

3. **适用场景**
- AI初学者希望系统性地通过代码实践来理解基础算法。
- 开发者需要寻找特定领域（如CV或NLP）的项目灵感或模板。
- 学生或研究人员用于课程作业参考或学术研究的基线对比。

4. **技术亮点**
- 项目规模庞大且分类全面，是AI领域的“Awesome List”式权威资源。
- 强调代码落地能力，直接提供可执行的解决方案而非仅理论描述。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和文件格式，帮助用户直观地查看模型结构。该工具旨在简化复杂模型的分析与调试过程。

2. **核心功能**
- 支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供直观的图形化界面，清晰展示神经网络的层结构及数据流向。
- 兼容多种后端格式，如 safetensors 和 TensorFlow Lite，适应不同部署需求。
- 允许用户导入本地文件或直接输入 URL 进行在线模型分析。

3. **适用场景**
- 深度学习研究人员用于快速检查模型架构是否正确构建。
- 工程师在模型转换或部署前，验证不同框架间模型的一致性。
- 开发者调试神经网络时，定位特定层或参数的配置问题。
- 非专业用户通过可视化界面理解 AI 模型的内部工作原理。

4. **技术亮点**
基于 JavaScript 开发，具有跨平台兼容性，无需安装重型依赖即可运行，且拥有极高的社区活跃度（3万+星标）。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必不可少的速查手册集合。内容涵盖从基础库使用到高级算法实现的各类关键知识点，旨在帮助研究者快速回顾和查阅技术细节。

2. **核心功能**
- 提供深度学习与机器学习领域的核心概念速查表。
- 汇总了常用Python数据科学库（如NumPy、SciPy、Matplotlib）的关键用法。
- 包含主流深度学习框架（如Keras）的操作指南。
- 整理了对研究人员极具价值的实用代码片段和函数参考。

3. **适用场景**
- 研究人员在进行实验时快速回顾特定算法或库函数的参数用法。
- 初学者学习深度学习基础时，作为系统性的知识梳理资料。
- 开发者在调试代码时，对照检查常用数据处理或可视化工具的正确语法。

4. **技术亮点**
- 内容高度浓缩，聚焦于高频使用的核心知识点，极大提升了查阅效率。
- 覆盖范围广泛，整合了从底层数学库到高层框架的多层次技术栈。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3382 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 我是 Agnes-2.0-Flash，由 Sapiens AI 开发。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建与训练流程。它通过声明式配置降低开发门槛，让开发者无需编写大量代码即可快速迭代和微调机器学习模型。

2. **核心功能**
*   提供声明式接口，通过简单的 YAML/JSON 配置即可定义模型架构和数据集。
*   内置多种深度学习后端支持，无缝兼容 PyTorch 等主流框架进行模型训练。
*   支持从零训练、迁移学习到针对 LLM（如 Llama、Mistral）的微调等多种模式。
*   具备数据-centric 特性，便于进行数据预处理、特征工程及实验结果可视化。
*   兼容主流 NLP 和计算机视觉任务，提供开箱即用的预训练模型组件。

3. **适用场景**
*   快速原型设计：希望在短时间内验证 AI 想法而不愿陷入复杂代码实现的团队。
*   LLM 微调与应用：需要对开源大模型（如 Llama 2、Mistral）进行特定领域适配或指令微调。
*   传统机器学习向深度学习迁移：希望在不重写大量底层逻辑的情况下升级现有 ML 流水线。
*   教育与研究：用于教学或学术研究中快速搭建和比较不同神经网络结构的效果。

4. **技术亮点**
*   **低代码高效能**：将复杂的深度学习工程抽象为配置项，显著降低使用门槛并提高开发效率。
*   **广泛的模型兼容性**：不仅支持传统表格数据和 CV 任务，还深度整合了对最新 LLM 生态的支持。
*   **实验可复现性**：通过配置文件管理模型结构和超参数，确保实验过程的透明度和结果的可复现性。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9145 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8935 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6993 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6269 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能丰富的中文自然语言处理（NLP）资源集合与工具库，涵盖了从基础文本预处理到高级语义分析的各项需求。它集成了敏感词检测、实体抽取、情感分析及多种专业领域知识图谱，为开发者提供了一站式的中英文 NLP 解决方案。

**2. 核心功能**
*   **文本预处理与清洗**：提供敏感词过滤、繁简转换、停用词、反动词表及中文数字转换等基础工具。
*   **信息抽取与识别**：支持手机号、身份证、邮箱等特定格式抽取，以及基于 BERT/Jieba 等的命名实体识别（NER）。
*   **语义分析与挖掘**：包含情感值计算、关键词提取、句子相似度匹配、文本摘要生成及多语言词向量资源。
*   **知识图谱与语料库**：整合了医疗、法律、金融等领域的垂直知识库，以及百度百科等大规模预训练数据和对话语料。

**3. 适用场景**
*   **内容安全审核**：利用敏感词库和暴恐词表进行网络内容的自动化过滤与安全监控。
*   **智能客服与聊天机器人**：结合闲聊语料、对话数据集及 Rasa/ConvLab 框架搭建具备语义理解能力的对话系统。
*   **垂直行业数据分析**：在医疗、法律或金融领域，利用专用词库和知识图谱进行实体关系抽取和问答系统构建。

**4. 技术亮点**
该项目并非单一算法实现，而是作为“资源仓库”整合了业界主流的前沿模型（如 BERT, GPT-2, ALBERT）及高质量标注数据集，极大降低了 NLP 应用开发的门槛和数据准备成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目荣获 ACL 2024 学术认可，旨在简化大模型的微调流程，降低技术门槛。

2. **核心功能**
- 支持 100+ 种主流 LLM 和 VLM 的统一高效微调。
- 集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）策略。
- 提供 RLHF（基于人类反馈的强化学习）及指令微调（Instruction Tuning）支持。
- 内置量化技术，显著降低显存占用并提升推理效率。
- 兼容 Transformers 库，实现模型架构的无缝对接与转换。

3. **适用场景**
- 研究人员快速验证不同架构大模型在特定任务上的微调效果。
- 开发者希望对开源模型进行低成本、低显存需求的定制化训练。
- 团队需要统一平台管理多个不同品牌或类型大模型的微调工作流。
- 希望引入人类偏好优化（RLHF）以提升模型对齐能力的 AI 应用开发。

4. **技术亮点**
- 高度模块化设计，同时涵盖 SFT、RLHF 及推理评估的全链路能力。
- 对 MoE（混合专家）模型及多模态（VLM）任务有原生且深度的支持。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73454 | 🍴 8966 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
这是一个由 Microsoft For Beginners 推出的为期 12 周、包含 24 节课的人工智能通识教育项目，旨在向大众普及 AI 知识。项目主要基于 Jupyter Notebook 编写，涵盖了从机器学习基础到深度学习应用的广泛主题，适合零基础学习者入门。

### 2. 核心功能
- **系统化课程结构**：提供清晰的 12 周学习路径和 24 节结构化课程，帮助学习者循序渐进地掌握 AI 概念。
- **交互式代码实践**：通过 Jupyter Notebook 提供可运行的代码示例，支持读者在浏览器中直接实验和验证 AI 模型。
- **多领域技术覆盖**：内容涵盖机器学习的核心算法、计算机视觉（CNN）、自然语言处理（RNN/NLP）以及生成对抗网络（GAN）等前沿技术。
- **面向初学者的设计**：语言通俗易懂，强调“AI for All”的理念，降低了人工智能的学习门槛。

### 3. 适用场景
- **初学者自我学习**：适合没有深厚数学或编程背景的人群，作为入门人工智能的第一站。
- **学校与培训机构教学**：教师可作为标准课程大纲，用于计算机科学或数据科学相关的通识教育课堂。
- **企业内训基础模块**：非技术部门员工或初级技术人员了解 AI 基本概念和应用场景的快速培训材料。

### 4. 技术亮点
- **官方背书与社区支持**：由 Microsoft For Beginners 维护，拥有超过 5 万星的极高社区关注度，资源丰富且更新活跃。
- **全栈 AI 知识图谱**：不仅限于理论，还整合了 CNN、RNN、GAN 等具体深度学习架构的实战案例，构建了完整的知识闭环。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52666 | 🍴 10672 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战及深度学习（PyTorch/TensorFlow 2）的综合学习库。项目内容还深入讲解了线性代数基础与自然语言处理工具（NLTK），旨在为学习者提供从理论到实践的完整技术栈支持。

2. **核心功能**
*   集成主流机器学习算法（如 SVM、K-Means、AdaBoost 等）的 Python 实现与解析。
*   提供基于 PyTorch 和 TensorFlow 2 的深度学习模型构建与训练代码示例。
*   包含自然语言处理（NLP）实战模块，利用 NLTK 进行文本分析与处理。
*   涵盖推荐系统、线性回归及主成分分析（PCA）等经典数据科学算法的应用。

3. **适用场景**
*   机器学习初学者用于巩固线性代数基础并上手 Python 编程实战。
*   数据科学家参考其代码实现特定算法（如 FP-Growth 关联规则挖掘）以解决业务问题。
*   深度学习研究人员对比不同框架（TF2 vs PyTorch）下的模型构建差异与最佳实践。

4. **技术亮点**
该项目通过整合传统统计学习方法与现代深度神经网络框架，提供了从底层数学原理到高层应用开发的连贯性学习路径，适合希望系统性掌握 AI 全栈技术的开发者。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42404 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入掌握人工智能工程的核心原理与实践。它不仅提供系统的学习路径，还指导用户将所学知识转化为可交付的产品，最终服务于更广泛的受众。这是一套结合理论与实践的综合性AI开发课程资源。

2. **核心功能**
*   涵盖从基础机器学习到生成式AI的全栈技术教程。
*   重点讲解智能体（Agents）、大语言模型（LLM）及多模态应用开发。
*   包含计算机视觉、自然语言处理及强化学习等深度领域实践。
*   提供基于Python和Rust等多种语言的实际代码实现与案例。

3. **适用场景**
*   AI工程师希望深入理解底层算法并提升全栈工程能力。
*   开发者计划构建基于大模型的智能体或复杂AI应用系统。
*   学生或研究人员需要系统性学习生成式AI与深度学习实战技巧。
*   团队寻求从零搭建AI基础设施的技术参考与最佳实践指南。

4. **技术亮点**
*   跨语言支持：同时包含Python生态与高性能Rust实现，兼顾易用性与效率。
*   前沿技术整合：深度融合MCP协议、Swarm Intelligence及Transformers架构等最新技术趋势。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42190 | 🍴 7028 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33765 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28772 | 🍴 3512 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25984 | 🍴 2944 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21745 | 🍴 3305 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化平台，能够智能地驱动浏览器完成各类工作流任务。它通过结合计算机视觉与大语言模型技术，实现了对复杂网页交互的精准控制与自动化执行。该项目旨在提供一种高效、可靠的方式来替代传统的手动或脚本式浏览器自动化操作。

2. **核心功能**
*   利用大语言模型（LLM）理解网页内容并生成自然语言指令来指导浏览器操作。
*   集成计算机视觉技术，使系统能够识别页面元素并处理动态变化的界面。
*   支持基于 Playwright 等现代浏览器引擎进行稳定且快速的网页自动化执行。
*   提供 API 接口，便于将浏览器自动化能力无缝集成到现有的业务流程中。
*   具备自我修复和纠错能力，能在页面布局变化时自动调整操作策略。

3. **适用场景**
*   **RPA 流程自动化**：用于跨系统的数据录入、表单填写及报告生成等重复性办公任务。
*   **Web 数据抓取**：从结构复杂或动态加载的网站中提取关键信息，超越传统爬虫的限制。
*   **端到端测试**：模拟真实用户行为对 Web 应用进行自动化功能测试和回归验证。
*   **业务流程集成**：在需要与多个不支持 API 的遗留系统进行交互的业务场景中充当桥梁。

4. **技术亮点**
*   **AI 驱动的决策能力**：不同于硬编码选择器，Skyvern 能“看懂”页面并通过推理决定下一步操作，适应性极强。
*   **多模态融合**：巧妙结合了文本理解（LLM）与图像识别（Vision），解决了纯文本解析无法应对动态 UI 的难题。
*   **开源生态兼容**：支持主流浏览器自动化库（如 Playwright、Puppeteer），降低了接入成本和学习门槛。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22553 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是领先的计算机视觉标注平台，旨在构建高质量的视觉数据集以支持视觉 AI。它提供开源、云及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量保证及团队协作。

2. **核心功能**
- 支持图像、视频及 3D 数据的多模态智能标注与自动标签生成。
- 提供从开源工具到企业级解决方案的灵活部署选项及开发者 API。
- 内置质量保证机制与团队协作功能，提升数据集构建效率。

3. **适用场景**
- 深度学习模型训练所需的大规模图像分类或目标检测数据集制作。
- 自动驾驶或监控视频中关键帧与连续动作的语义分割标注。
- 科研团队或企业内部需要协作完成的高精度 3D 点云标注任务。

4. **技术亮点**
- 集成 AI 辅助标注能力，显著提升图像分类、目标检测等任务的标注速度。
- 兼容 PyTorch 和 TensorFlow 等主流深度学习框架，便于数据流转与模型迭代。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16360 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具，支持卷积神经网络（CNN）和视觉Transformer等多种模型。它广泛应用于图像分类、目标检测、分割及相似度计算等任务，帮助用户直观理解模型的决策依据。

2. **核心功能**
*   提供多种可视化方法（如Grad-CAM、Score-CAM），生成类激活映射以突出图像中的关键区域。
*   兼容主流深度学习框架，支持CNN架构及Vision Transformers模型。
*   覆盖广泛的计算机视觉任务，包括分类、目标检测、语义分割和图像相似度分析。
*   增强模型的可解释性，帮助开发者调试并验证深度学习模型的内部逻辑。

3. **适用场景**
*   **模型调试与优化**：在训练过程中可视化注意力机制，快速定位模型关注的错误特征或背景噪声。
*   **合规性与安全审计**：在医疗影像或自动驾驶等高风险领域，提供可视化的决策证据以满足监管要求。
*   **学术研究与教学**：直观展示深度学习模型如何“看”世界，用于解释复杂算法原理或辅助论文撰写。

4. **技术亮点**
*   高度模块化设计，灵活适配不同的PyTorch网络结构及自定义损失函数。
*   集成多种前沿的可解释性算法（如Grad-CAM++、Score-CAM），不仅限于基础的Grad-CAM实现。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 以下是基于您提供信息的 kornia GitHub 项目中文分析报告：

1. **中文简介**
Kornia 是一个专为空间 AI（Spatial AI）设计的几何计算机视觉库。它以 Python 为核心，深度集成 PyTorch 框架，为开发者提供可微分的、高性能的计算机视觉与图像处理工具。

2. **核心功能**
* **可微分图像处理：** 提供基于 PyTorch 的可微分图像预处理与变换模块，直接支持端到端的神经网络训练。
* **3D 几何与相机模型：** 内置丰富的 3D 几何计算、相机内参与外参求解以及透视投影等底层算法。
* **特征提取与匹配：** 包含 ORB、SIFT 等经典特征的 GPU 加速实现，支持高效的图像关键点检测与匹配。
* **自动化数据增强：** 针对 3D 视觉任务（如多视图几何、SLAM）设计的高度可配置数据增强管线。

3. **适用场景**
* **3D 视觉与机器人导航：** 用于 SLAM（即时定位与地图构建）、V-SLAM（视觉同步定位与建图）及机器人视觉系统的研发与训练。
* **深度学习模型训练：** 作为 AI 项目中数据预处理和数据增强的标准化工具包，替代传统的 OpenCV 脚本。
* **自动驾驶感知系统：** 应用于车道线检测、障碍物识别及三维空间重建等高精度空间感知任务。

4. **技术亮点**
* **无缝 PyTorch 集成：** 所有算子均原生支持 `torch.Tensor` 和自动求导机制（Autograd），可直接嵌入深度学习网络中进行反向传播。
* **GPU 硬件加速：** 彻底摒弃 CPU 瓶颈，所有几何计算与图像处理均在 GPU 上运行，极大提升了大规模数据集的训练效率。
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1205 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3294 | 🍴 403 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383841 | 🍴 80642 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**
Superpowers 是一个经过验证的代理技能框架及软件开发方法论。它通过结构化流程赋能开发者，将复杂的软件工程任务转化为可执行的智能体技能。该项目旨在提升开发效率并优化软件开发生命周期（SDLC）。

**2. 核心功能**
*   提供一套标准化的“技能”定义体系，用于规范 AI 代理的行为模式。
*   采用子代理驱动开发（Subagent-Driven Development）模式，实现任务的自动化分解与执行。
*   集成头脑风暴与编码辅助功能，支持从创意构思到代码落地的全流程。
*   构建基于 AGRA 方法的软件开发生命周期管理工具链。
*   通过 Shell 脚本实现轻量级部署与跨平台兼容性。

**3. 适用场景**
*   希望利用 AI 代理自动化常规编程任务并降低维护成本的团队。
*   需要结构化方法论来规范大型软件项目中 AI 介入流程的组织。
*   致力于探索“智能体驱动开发”新型软件工程范式的研发团队。
*   寻求高效头脑风暴工具以加速创意原型设计与技术验证的场景。

**4. 技术亮点**
*   创新性地将“技能”抽象为可复用的软件组件，实现了方法论与代码库的统一。
*   强调“经过验证”的工作流，通过标准化模板确保 AI 代理输出的一致性与可靠性。
- 链接: https://github.com/obra/superpowers
- ⭐ 259395 | 🍴 23123 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款能够随着用户共同成长和进化的 AI 智能体。它旨在通过深度集成多种大型语言模型，提供持续优化且个性化的代码辅助与任务执行能力。该项目致力于成为开发者日常工作中不可或缺的自动化助手。

### 2. 核心功能
- **多模型支持**：兼容 Anthropic (Claude)、OpenAI (GPT) 等多种主流大语言模型，灵活切换以适配不同需求。
- **自适应进化**：具备学习和记忆机制，能根据用户的历史交互和反馈不断优化自身行为与响应策略。
- **全栈代码辅助**：提供从代码生成、调试到重构的全流程智能辅助，显著提升开发效率。
- **智能体协作**：支持复杂任务的分解与执行，能够像独立代理一样处理多步骤工作流。

### 3. 适用场景
- **高级软件开发**：适合需要深度代码理解、复杂架构设计以及自动化测试生成的专业开发者。
- **个性化 AI 助手搭建**：适用于希望构建具备长期记忆、能随时间推移变得更懂自己的专属 AI 代理的用户。
- **多模型实验与研究**：适合研究人员或技术爱好者在统一框架下对比和测试不同 LLM 的性能与特性。

### 4. 技术亮点
- **高度模块化架构**：基于 Python 构建，易于扩展和自定义插件，支持快速集成新的模型或服务。
- **开源社区驱动**：拥有极高的星标数（20万+）和活跃的标签生态，反映了其强大的社区影响力和持续的开发活力。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218936 | 🍴 41478 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码结合。它提供自托管或云端部署选项，并集成超过 400 种应用，旨在降低自动化开发的门槛。

2. **核心功能**
- 提供可视化拖拽界面与自定义代码编写相结合的工作流构建方式。
- 内置原生 AI 能力，支持智能任务处理与自动化决策。
- 拥有超过 400 种预置集成，实现跨应用数据无缝连接。
- 支持自托管私有部署与云端服务，兼顾数据安全与灵活性。

3. **适用场景**
- 企业级数据同步：在不同 SaaS 平台（如 CRM、ERP）之间自动同步客户或订单数据。
- AI 增强型工作流：利用内置 AI 能力自动处理文档摘要、分类或生成内容。
- 个人效率自动化：连接笔记工具、日历和邮件，自动整理信息或提醒待办事项。
- API 集成开发：快速搭建轻量级中间件，整合多个第三方服务的 API 接口。

4. **技术亮点**
- 基于 TypeScript 开发，类型安全且易于扩展和维护。
- 采用公平代码许可（Fair-code），平衡了开源共享与企业合规需求。
- 原生支持 MCP（Model Context Protocol），无缝对接大语言模型上下文。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197506 | 🍴 59546 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185651 | 🍴 46073 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166215 | 🍴 21482 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164228 | 🍴 30434 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157225 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154510 | 🍴 8800 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152224 | 🍴 9626 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

