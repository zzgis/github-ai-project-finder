# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- ### 1. 中文简介
thinking-orbs 是一款专为 AI 及智能体用户界面设计的点状思维加载指示器组件库。它提供了六种经过调优的动画状态和两种尺寸选项，并支持自动适配深色与浅色模式，以增强用户交互体验。

### 2. 核心功能
*   **多状态动画**：提供六种精心调优的加载状态，直观反映 AI 的思维处理过程。
*   **灵活尺寸**：支持两种不同大小的指示器，以适应不同的 UI 布局需求。
*   **自动主题适配**：内置深色/浅色模式自动切换功能，无需手动配置即可完美融入当前界面风格。
*   **TypeScript 原生支持**：基于 TypeScript 开发，提供完善的类型定义，便于现代前端项目集成。

### 3. 适用场景
*   **AI 聊天应用**：在用户等待大语言模型生成回复时，展示“正在思考”的状态，提升等待期的视觉反馈质量。
*   **智能体操作界面**：用于展示后台 Agent 执行复杂任务或规划步骤时的动态加载效果。
*   **SaaS 产品仪表盘**：在数据加载或模型推理过程中，作为更优雅、更具科技感的加载占位符替代传统 Spinner。

### 4. 技术亮点
*   **高性能动画优化**：采用轻量级实现，确保在各种设备上都能流畅运行，不会造成渲染阻塞。
*   **零依赖设计**：作为纯 UI 组件库，不依赖其他重型库，易于嵌入现有的 React 或 Vue 项目中。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 557 | 🍴 35 | 语言: TypeScript

### BossConsole
- ### 1. **中文简介**
BossConsole 是一款面向企业、科研及科学领域的开源多平台 AI 智能体操作控制台。它基于 JVM（而非 Electron）构建，提供原生多线程支持，可整合真实浏览器、终端、编辑器及安全密钥管理，并支持 Claude Code、Codex、Gemini 等多种主流 AI 模型及 100+ MCP 工具。

### 2. **核心功能**
*   **多模型兼容**：支持运行 Claude Code、Codex、Gemini 或 OpenCode 等主流 AI 代理。
*   **全栈集成环境**：内置真实浏览器、终端、代码编辑器及密钥管理功能。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，兼容 100+ 扩展工具。
*   **高性能架构**：采用 Kotlin Multiplatform 和 Compose Multiplatform 构建，基于 JVM 实现多线程操作。
*   **企业级安全与特性**：具备热重载（Hot-reload）、RBAC（基于角色的访问控制）及多平台桌面应用支持。

### 3. **适用场景**
*   **企业开发自动化**：大型团队利用 RBAC 和多线程特性，安全地编排和管理复杂的 AI 编程工作流。
*   **科研数据与代码分析**：研究人员通过集成的浏览器和终端，结合 MCP 工具进行深度的数据获取与代码处理。
*   **多模型对比测试**：开发者在同一界面下并行运行 Claude、Gemini 等不同模型，快速评估其输出效果。
*   **复杂智能体部署**：需要真实浏览器环境和完整文件系统权限的高级 AI 代理部署场景。

### 4. **技术亮点**
*   **JVM 原生性能**：摒弃 Electron 的 Chromium 内核，使用 JVM 实现更轻量、性能更高的桌面应用体验。
*   **Kotlin Multiplatform**：利用 Kotlin 的多平台能力，确保代码在不同操作系统间的高效复用与一致性。
*   **MCP 生态整合**：深度集成 Model Context Protocol，极大扩展了 AI 智能体访问外部工具和数据的灵活性。
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 150 | 🍴 2 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### open-ai-canvas
- **1. 中文简介**
Open-ai-canvas 是一款专为 AI 影视创作设计的开源无限画布工作台。它集成了多模态内容生成、分镜编排、素材管理以及 Agent 自动化工作流功能。该项目旨在为创作者提供一个高效、可视化的全流程制作环境。

**2. 核心功能**
*   **无限画布工作台**：提供自由扩展的可视化界面，支持非线性编辑与布局。
*   **多模态生成集成**：内置多种 AI 模型接口，支持文本、图像、视频等多类型内容生成。
*   **智能分镜编排**：辅助用户进行剧本拆解、镜头规划及叙事结构梳理。
*   **统一素材管理**：集中存储和管理项目所需的各类数字资产与生成结果。
*   **Agent 工作流引擎**：通过自动化的智能代理（Agent）串联各个创作环节，提升效率。

**3. 适用场景**
*   **AI 短片/微电影制作**：用于从剧本到成片的快速原型设计与全流程管理。
*   **动态分镜脚本创作**：帮助导演或策划人员将文字剧本转化为可视化的镜头语言。
*   **交互式叙事项目开发**：适用于需要复杂分支逻辑和多媒体元素集成的互动故事创作。
*   **AI 创意头脑风暴**：利用多模态生成能力快速探索视觉风格和概念方案。

**4. 技术亮点**
*   基于 TypeScript 构建，保证了代码的可维护性与类型安全。
*   采用模块化架构，灵活集成主流多模态大模型 API。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 68 | 🍴 18 | 语言: TypeScript

### pgContext
- 1. **中文简介**
pgContext 是一个内置于 PostgreSQL 数据库中的全功能 AI 搜索引擎。它利用 Rust 语言开发，旨在将人工智能检索能力直接集成到现有的关系型数据库环境中，无需外部复杂的向量数据库服务。

2. **核心功能**
- 将 AI 搜索和语义检索能力深度集成到 PostgreSQL 数据库中。
- 基于 Rust 构建，提供高性能的数据处理与查询执行效率。
- 支持在数据库内部直接进行上下文相关的智能搜索操作。

3. **适用场景**
- 需要在现有 PostgreSQL 架构中快速添加语义搜索功能的传统企业应用。
- 希望简化技术栈，避免维护独立向量数据库的微服务系统。
- 对数据隐私和安全性要求较高，倾向于将 AI 能力保留在本地数据库内的场景。

4. **技术亮点**
- 采用 Rust 编写，确保了内存安全和极高的运行性能。
- “内置”设计消除了外部依赖，实现了数据库与 AI 能力的无缝协同。
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 61 | 🍴 3 | 语言: Rust

### AIGuardSIEM
- 1. **中文简介**
AIGuardSIEM 是一个生产级 SIEM/XDR 平台，支持每秒百万级事件（EPS）摄入并实现亚 15 毫秒的检测延迟。该项目基于 C++、Go 和 Python 构建，旨在提供高性能的企业级安全运营解决方案。

2. **核心功能**
*   支持基于 DPDK 的高速数据包捕获以实现极低延迟的数据摄入。
*   集成 ONNX 进行机器学习推理，结合 Sigma 规则实现精准威胁检测。
*   利用 eBPF 技术提供深度的端点监控与可观测性。
*   内置 SOAR（安全编排、自动化及响应）能力以自动化处置安全事件。
*   兼容 Kafka 和 Kubernetes 架构，支持大规模分布式部署与流式处理。

3. **适用场景**
*   需要处理海量日志数据且对实时性要求极高的大型企业 SOC 中心。
*   希望利用机器学习模型增强传统规则引擎检测能力的网络安全团队。
*   寻求通过自动化剧本（Playbooks）快速响应和缓解安全事件的运维人员。
*   正在构建基于云原生架构（Kubernetes）的现代 XDR 平台的技术团队。

4. **技术亮点**
*   采用 C++ 与 Go 混合开发，兼顾底层高性能数据处理与微服务灵活性。
*   融合多种前沿安全技术（eBPF、DPDK、ONNX），在保障高吞吐量的同时降低检测延迟。
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 55 | 🍴 4 | 语言: C++
- 标签: anomaly-detection, cybersecurity, dpdk, endpoint-security, incident-response

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

### style-pack-skill
- 描述: 从参考图提取视觉风格 DNA，强制生成标注与纯色双版色卡的 AI Agent Skill
- 链接: https://github.com/irenerachel/style-pack-skill
- ⭐ 30 | 🍴 6 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且资源丰富的中文自然语言处理（NLP）开源资源库，旨在为开发者提供从基础工具到前沿模型的各类 NLP 相关项目、数据集及代码实现。它集成了敏感词检测、分词、实体抽取、情感分析等实用功能，并汇总了国内外高质量的 NLP 数据集、预训练模型（如 BERT、GPT）及竞赛方案。该项目是中文 NLP 领域入门学习与工程实践的重要参考资料集合。

2. **核心功能**
- **基础 NLP 工具集成**：提供敏感词过滤、中英文分词、词性标注、命名实体识别（NER）、关键词提取及文本相似度计算等核心算法实现。
- **多领域知识库与语料**：涵盖人名、地名、行业术语（IT/医疗/法律/汽车等）、成语、古诗词及闲聊语料库，支持繁简转换和拼音标注。
- **预训练模型与深度学习资源**：汇总了 BERT、ALBERT、RoBERTa、GPT 等主流预训练语言模型的中文版本及其在分类、NER、问答等任务上的应用代码。
- **多模态与语音处理**：包含中文语音识别（ASR）、OCR 文字识别、语音情感分析及音频数据增强等跨模态资源。
- **知识图谱与问答系统**：提供构建知识图谱的工具、关系抽取算法、基于检索的问答系统及对话机器人框架资源。

3. **适用场景**
- **NLP 初学者学习**：适合想要系统了解中文 NLP 技术栈、获取高质量数据集和基准测试代码的学生或研究人员。
- **企业级内容风控与审核**：利用其内置的敏感词库、暴恐词表及谣言检测资源，快速搭建内容安全过滤系统。
- **垂直领域智能客服开发**：借助其中的行业词库、闲聊机器人代码及对话系统框架，快速构建特定领域（如金融、医疗）的智能问答助手。
- **信息抽取与结构化处理**：用于从非结构化文本中自动提取姓名、电话、身份证、邮箱等关键信息，或进行文档表格识别。

4. **技术亮点**
- **资源聚合度高**：不仅包含代码，还整合了大量公开的高质量数据集、学术论文解读及竞赛 Top 方案，具有极高的参考价值。
- **覆盖技术栈全**：从传统的规则匹配、统计模型到最新的 Transformer 架构预训练模型均有涉及，适应不同阶段的技术需求。
- **侧重中文生态优化**：特别针对中文特性（如分词歧义、繁简转换、中文语音等）提供了专门的工具和资源，解决了通用英文 NLP 工具在中文场景下的适配问题。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习和机器学习模型的轻量级工具。它支持多种主流框架生成的模型格式，能够以直观的图形界面展示模型结构和参数。该工具主要基于 JavaScript 开发，便于在浏览器或桌面端直接查看和分析模型。

### 2. **核心功能**
- 支持多种主流深度学习框架（如 TensorFlow, PyTorch, Keras, ONNX 等）的模型文件可视化。
- 提供清晰的层次化结构视图，展示网络层连接关系及张量维度信息。
- 支持本地桌面应用和在线网页两种访问方式，无需安装复杂环境即可使用。
- 允许用户导出模型结构图片或生成文本报告，便于文档记录和分享。
- 兼容 CoreML、SafeTensors 等新兴或特定平台的模型格式。

### 3. **适用场景**
- **模型调试与验证**：深度学习研究人员用于检查网络结构是否正确构建，排查层连接错误。
- **技术文档编写**：工程师需要为项目生成可视化的模型架构图，用于论文撰写或技术报告。
- **跨平台模型转换检查**：在将模型从一种格式（如 PyTorch）转换为另一种格式（如 ONNX 或 CoreML）后，验证转换结果的结构一致性。
- **快速原型预览**：开发者在没有重型 IDE 的环境中，快速查看和确认第三方提供的预训练模型细节。

### 4. **技术亮点**
- **广泛兼容性**：原生支持数十种模型格式，是业界通用的“万能”模型查看器。
- **零依赖运行**：基于 Web 技术栈，可在任何现代浏览器中运行，或在 Electron 封装的桌面端离线使用。
- **高性能渲染**：能够流畅处理包含成千上万节点的复杂深层网络结构。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21198 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18451 | 🍴 1178 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17332 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
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
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习和机器学习模型的轻量级工具。它支持多种主流框架生成的模型格式，能够以直观的图形界面展示模型结构和参数。该工具主要基于 JavaScript 开发，便于在浏览器或桌面端直接查看和分析模型。

### 2. **核心功能**
- 支持多种主流深度学习框架（如 TensorFlow, PyTorch, Keras, ONNX 等）的模型文件可视化。
- 提供清晰的层次化结构视图，展示网络层连接关系及张量维度信息。
- 支持本地桌面应用和在线网页两种访问方式，无需安装复杂环境即可使用。
- 允许用户导出模型结构图片或生成文本报告，便于文档记录和分享。
- 兼容 CoreML、SafeTensors 等新兴或特定平台的模型格式。

### 3. **适用场景**
- **模型调试与验证**：深度学习研究人员用于检查网络结构是否正确构建，排查层连接错误。
- **技术文档编写**：工程师需要为项目生成可视化的模型架构图，用于论文撰写或技术报告。
- **跨平台模型转换检查**：在将模型从一种格式（如 PyTorch）转换为另一种格式（如 ONNX 或 CoreML）后，验证转换结果的结构一致性。
- **快速原型预览**：开发者在没有重型 IDE 的环境中，快速查看和确认第三方提供的预训练模型细节。

### 4. **技术亮点**
- **广泛兼容性**：原生支持数十种模型格式，是业界通用的“万能”模型查看器。
- **零依赖运行**：基于 Web 技术栈，可在任何现代浏览器中运行，或在 Electron 封装的桌面端离线使用。
- **高性能渲染**：能够流畅处理包含成千上万节点的复杂深层网络结构。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目汇集了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。内容涵盖从基础数学工具到主流框架的关键知识点，旨在为研究者提供高效的知识回顾与参考指南。

2. **核心功能**
- 提供深度学习关键概念、算法及模型的快速查阅资料。
- 整合机器学习常用库（如NumPy, SciPy, Matplotlib）的操作速记。
- 包含Keras等主流深度学习框架的代码示例与使用技巧。
- 梳理人工智能领域的核心术语与理论基础知识。
- 以结构化的图表和简明笔记形式呈现复杂技术细节。

3. **适用场景**
- 深度学习与机器学习研究者在日常实验中进行快速知识检索。
- 学生在备考或复习相关课程时作为高效的总结性学习资料。
- 工程师在开发初期快速回忆特定库函数或模型架构的配置方法。
- 技术团队内部进行新知识分享或技术培训时的辅助材料。

4. **技术亮点**
- 内容高度浓缩且视觉化强，极大降低了复杂技术的认知负荷。
- 覆盖范围广泛，从底层数学运算到高层框架应用均有涉及。
- 由领域专家整理，确保知识点的准确性与前沿性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一个提供零基础入门至就业实战的人工智能学习路线图，整合了近200个实战案例并免费提供配套教材。内容涵盖Python、数学基础以及机器学习、深度学习、NLP和CV等热门技术领域。

2. **核心功能**
- 提供从数学基础到深度学习的系统化AI学习路径。
- 收录近200个精选实战项目与案例供学习者练习。
- 免费开放配套教材与资源，降低学习门槛。
- 覆盖Python生态及主流框架（如PyTorch、TensorFlow）。

3. **适用场景**
- AI初学者希望从零开始构建完整知识体系。
- 求职者需要实战项目经验以准备技术面试或作品集。
- 数据科学家寻找特定领域（如NLP、CV）的参考案例。

4. **技术亮点**
该项目最大的亮点在于其“路线图”式的结构化管理，将分散的技术点串联成完整的进阶路径，并辅以大量免费实战资源，极大地降低了AI入门的学习成本。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他 AI 模型的构建过程。它通过声明式配置让用户无需编写复杂代码即可快速训练和评估机器学习模型。

2. **核心功能**
*   提供声明式 API，支持通过 YAML/JSON 配置快速定义和训练深度学习模型。
*   内置对表格数据、文本、图像及音频等多种模态数据的原生支持。
*   集成主流深度学习后端（如 PyTorch），支持从基准模型进行微调（Fine-tuning）。
*   提供端到端的 MLOps 工具链，涵盖数据预处理、模型训练、评估及部署。
*   支持可解释性分析，帮助理解模型决策依据及特征重要性。

3. **适用场景**
*   数据科学家希望快速原型化并训练结构化表格数据的分类或回归模型。
*   开发者需要基于预训练大模型（如 Llama、Mistral）进行领域特定的微调任务。
*   团队希望在减少代码维护负担的同时，实现标准化的机器学习工作流。
*   需要进行多模态数据处理（如结合文本与图像）的复杂 AI 应用开发。

4. **技术亮点**
*   采用“数据为中心”的设计理念，强调数据配置而非底层算法实现。
*   高度模块化架构，允许轻松替换或扩展不同的组件和后端引擎。
*   无缝集成 Hugging Face 生态，便于加载和使用海量的开源预训练模型。
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
- ⭐ 6992 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6268 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持百余种主流模型。该项目已发表于 ACL 2024 会议，旨在降低大模型微调的技术门槛并提升训练效率。

2. **核心功能**
*   **多模型统一支持**：无缝兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种 LLM 及 VLM。
*   **多样化微调算法**：内置 LoRA、QLoRA、P-Tuning 等多种高效微调策略及 RLHF 对齐技术。
*   **量化与性能优化**：提供 4-bit/8-bit 量化训练支持，显著降低显存占用并加速推理过程。
*   **全流程训练链路**：集成数据预处理、模型训练、评估及导出功能，实现从准备到部署的一站式体验。

3. **适用场景**
*   **垂直领域模型定制**：为医疗、法律或金融等行业快速构建具备专业指令遵循能力的小参数模型。
*   **低资源环境微调**：在显存受限的消费级 GPU 上，通过 QLoRA 等技术高效微调大型语言模型。
*   **多模态应用开发**：针对需要同时理解文本和图像的任务，快速微调视觉语言模型（VLM）。

4. **技术亮点**
*   **ACL 2024 学术认可**：作为经过同行评审的研究成果，其方法论具有坚实的学术基础和高可靠性。
*   **极致的易用性**：采用 YAML 配置文件驱动，无需编写复杂代码即可启动不同模型的微调任务。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73454 | 🍴 8966 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的AI入门课程，旨在让所有人都能轻松学习人工智能。该项目由微软发起，通过Jupyter Notebook提供互动式教学体验。其核心目标是普及AI知识，降低技术门槛，适合零基础用户系统性地掌握AI基础。

2. **核心功能**
- 提供结构化的12周学习计划，涵盖从基础概念到高级应用的完整路径。
- 包含24节精心设计的课程，结合理论讲解与动手实践。
- 支持交互式Jupyter Notebook环境，便于用户直接运行代码并即时查看结果。
- 覆盖机器学习、深度学习、计算机视觉和自然语言处理等多个AI核心领域。
- 完全免费开放，由微软开发者社区维护和支持。

3. **适用场景**
- 初学者希望系统性地从零开始学习人工智能基础理论。
- 教师或培训机构用于课堂教学或在线课程的辅助教材。
- 开发者希望在短时间内快速了解AI概念并上手简单项目。
- 非技术背景人员希望获得通俗易懂的AI科普教育。

4. **技术亮点**
- 采用微软“Microsoft For Beginners”系列的标准教学法，注重循序渐进。
- 使用Jupyter Notebook实现代码与文档的无缝集成，提升学习效率。
- 内容涵盖CNN、RNN、GAN等主流深度学习模型的基础应用。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52665 | 🍴 10671 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战及深度学习框架（PyTorch、TensorFlow 2）的综合学习资源库，同时辅以线性代数与 NLP 工具（NLTK）的讲解。该项目旨在通过 Python 实现从基础算法到高级模型的完整技术栈实践。

2. **核心功能**
*   提供经典机器学习算法（如 SVM、K-Means、随机森林等）的代码实现与原理详解。
*   集成深度学习主流框架 PyTorch 和 TensorFlow 2 的实战案例。
*   包含自然语言处理（NLP）基础工具 NLTK 的应用教程。
*   涵盖推荐系统、关联规则挖掘（Apriori, FP-Growth）及降维技术（PCA, SVD）等专项模块。

3. **适用场景**
*   计算机科学或数据科学专业的学生用于巩固线性代数、概率论及机器学习理论基础。
*   初级至中级算法工程师进行面试准备及常见 ML/DL 算法的代码复现练习。
*   对 NLP 或推荐系统感兴趣的学习者快速上手相关领域的工具链与模型构建。

4. **技术亮点**
*   内容体系完整，打通了从数学基础（线性代数）到传统机器学习，再到深度学习和 NLP 的技术闭环。
*   标签丰富且覆盖面广，集成了 scikit-learn、sklearn 等主流库的最佳实践。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42404 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入掌握人工智能技术的核心原理与实践。它引导学习者不仅理解AI机制，更能亲手打造并部署面向他人的AI应用，实现从学习到实战的完整闭环。

2. **核心功能**
- 涵盖LLM、计算机视觉及强化学习等前沿领域的深度技术解析。
- 提供基于Python、Rust和TypeScript的多语言工程实现教程。
- 重点讲解AI智能体（Agents）、MCP协议及群体智能等高级架构设计。
- 包含生成式AI与NLP技术的从头构建指南，强调底层逻辑而非仅调用API。

3. **适用场景**
- AI工程师希望深入理解模型底层原理以提升系统定制能力。
- 开发者需要构建复杂AI工作流或自定义智能体系统的实战指导。
- 研究人员探索多语言混合开发环境下的AI工程最佳实践。

4. **技术亮点**
项目结合了Python的高效生态与Rust的性能优势，并引入了MCP（Model Context Protocol）等新兴标准，展现了全栈AI工程化的先进视野。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42161 | 🍴 7021 | 语言: Python
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
Skyvern 是一款利用人工智能自动执行基于浏览器的复杂工作流的工具。它通过结合视觉理解与大语言模型，能够像人类一样与网页进行交互，从而替代繁琐的重复性操作。该项目旨在为开发者提供一个灵活且强大的自动化解决方案。

2. **核心功能**
- 基于 AI 视觉识别技术，自动解析网页元素并执行点击、输入等操作。
- 支持多种浏览器自动化引擎（如 Playwright），具备高度的兼容性和稳定性。
- 能够处理动态加载和复杂的表单提交，适应现代 Web 应用的交互逻辑。
- 提供 API 接口，方便集成到现有的业务流程或 RPA 系统中。
- 利用大语言模型理解用户意图，将自然语言指令转化为具体的浏览器操作步骤。

3. **适用场景**
- **RPA 流程自动化**：替代传统 Selenium 脚本，更智能地处理界面变化频繁的 Web 应用任务。
- **数据抓取与填报**：自动登录系统、导航页面并提取或录入关键业务数据。
- **跨平台工作流整合**：作为 Power Automate 等工具的补充，处理需要高级视觉判断的浏览器任务。
- **测试自动化**：用于模拟真实用户行为进行端到端的 UI 测试，比传统选择器更健壮。

4. **技术亮点**
- 融合了计算机视觉（Vision）与大语言模型（LLM），实现了对非结构化界面元素的精准定位。
- 相比传统依赖固定 ID 或 CSS 选择器的自动化工具，对前端改版具有更强的鲁棒性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22554 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是一个领先的计算机视觉标注平台，致力于构建高质量的视觉数据集以支持视觉人工智能。它提供开源、云端及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量控制及团队协作。

2. **核心功能**
*   支持图像、视频及 3D 数据的多种标注格式（如边界框、语义分割）。
*   集成 AI 辅助标注功能以提升数据标注效率与准确性。
*   提供完善的质量保证机制与强大的团队协作工具。
*   开放开发者 API 并支持数据分析，便于集成到现有工作流中。

3. **适用场景**
*   深度学习模型训练所需的大规模图像分类或物体检测数据集准备。
*   自动驾驶或安防监控领域中的视频序列关键帧标注任务。
*   医疗影像或工业质检等需要高精度语义分割标注的专业场景。
*   团队协作进行大规模数据清洗与标注外包项目管理。

4. **技术亮点**
*   兼容 PyTorch 和 TensorFlow 等主流深度学习框架的数据生态。
*   提供从开源社区版到企业级服务的全方位产品矩阵。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16360 | 🍴 3770 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目致力于提供先进的计算机视觉可解释性AI工具，支持CNN和Vision Transformers等模型。它涵盖了分类、目标检测、分割及图像相似度等多种任务的可视化分析需求。

2. **核心功能**
- 支持Grad-CAM、Score-CAM等多种主流可解释性算法实现。
- 兼容卷积神经网络（CNN）与视觉Transformer（ViT）架构。
- 覆盖图像分类、目标检测、语义分割及图像相似度计算等任务。
- 提供直观的可视化效果以增强深度学习模型的透明度。

3. **适用场景**
- 研究人员调试和优化计算机视觉模型时分析特征关注区域。
- 医疗影像或自动驾驶等领域中，需要向非技术人员展示AI决策依据。
- 开发者希望深入理解模型在特定类别或物体上的注意力分布机制。

4. **技术亮点**
- 集成了Class Activation Maps (CAM) 及其多种变体（如Grad-CAM, Score-CAM），统一了可解释性技术的接口。
- 针对最新的Vision Transformer架构提供了专门的适配支持，保持了技术的前沿性。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
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
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调数据的私有性与自主掌控。它为用户提供了一种独特的“龙虾式”体验，让您能够完全拥有并管理自己的 AI 数据。

2. **核心功能**
*   跨平台兼容：可在任何操作系统和平台上无缝运行。
*   数据主权：强调“Own Your Data”，确保用户完全掌控个人信息。
*   个人助理：提供高度定制化的个人 AI 助手服务。
*   TypeScript 构建：基于现代 TypeScript 开发，保证代码质量与可维护性。

3. **适用场景**
*   注重隐私安全的个人用户，希望将 AI 数据本地化存储。
*   需要在多种不同操作系统（如 Linux、macOS、Windows）间切换工作的开发者。
*   寻求自定义程度高、不受大型科技公司云服务限制的 AI 助手替代方案的用户。

4. **技术亮点**
*   采用 TypeScript 编写，具备良好的类型安全性和现代开发体验。
*   架构设计支持广泛的平台兼容性，无需绑定特定硬件或 OS 环境。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383834 | 🍴 80643 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架及软件开发方法论。它旨在通过结构化的技能体系，提升软件开发生命周期（SDLC）的效率与质量。该项目强调将 AI 代理能力集成到实际开发流程中，以实现更智能的开发辅助。

2. **核心功能**
*   提供模块化的“技能”框架，支持代理驱动的开发模式。
*   定义了一套完整的软件开发方法论，涵盖从头脑风暴到编码的全过程。
*   支持子代理协作，实现复杂任务的分解与自动化执行。
*   集成 AI 编程助手，增强代码生成、审查及调试能力。
*   标准化软件开发生命周期（SDLC）中的 AI 交互接口。

3. **适用场景**
*   希望引入 AI 代理自动化部分开发流程的团队。
*   需要结构化方法指导 AI 参与头脑风暴和需求分析的场景。
*   致力于探索“子代理驱动开发”（Subagent-Driven Development）新范式的开发者。
*   寻求提升 SDLC 效率并整合现有 AI 编程工具的企业级项目。

4. **技术亮点**
*   首创将“技能”作为一等公民的代理框架设计。
*   明确提出了“子代理驱动开发”这一新兴软件工程范式。
*   虽然主要描述为方法论，但基础实现基于 Shell 脚本，体现了轻量级和可插拔特性。
- 链接: https://github.com/obra/superpowers
- ⭐ 259384 | 🍴 23119 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够随用户共同成长和进化的智能代理工具。它旨在通过持续学习和适配，为用户提供个性化的 AI 辅助体验。该项目支持多种大型语言模型，致力于成为用户开发和工作流程中的得力助手。

2. **核心功能**
- 支持集成多种主流大语言模型（如 Anthropic 的 Claude、OpenAI 的 GPT 等）。
- 具备自适应学习能力，能根据用户习惯和项目上下文不断优化交互体验。
- 提供代码生成、调试及重构等开发者友好型功能。
- 模块化架构设计，允许用户自定义代理行为和扩展功能。
- 兼容多种开发环境和 IDE，实现无缝的工作流集成。

3. **适用场景**
- 开发者日常编码辅助，包括代码补全、错误排查和技术文档生成。
- 复杂项目的自动化工作流管理，提升研发效率。
- 需要个性化 AI 助手的学习者或研究人员，用于知识整理和问题解答。
- 企业级应用中的智能客服或内部技术支持代理部署。

4. **技术亮点**
- 多模型兼容性使其在不同性能与成本需求间灵活切换。
- “成长型”设计理念强调长期记忆与上下文理解能力的积累。
- 开源生态活跃，拥有高星标数（218,925），社区贡献丰富且迭代迅速。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218925 | 🍴 41470 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码。它提供 400 多种集成方式，允许用户选择自托管或云端部署，实现高效的数据流处理与业务自动化。

2. **核心功能**
*   **混合自动化模式**：完美融合低代码/无代码的可视化拖拽界面与高级自定义代码编写能力。
*   **海量集成连接**：内置超过 400 种主流应用和服务的原生集成节点，打通数据孤岛。
*   **原生 AI 集成**：深度集成人工智能能力，可直接在工作流中调用 LLM 进行智能处理。
*   **灵活部署架构**：支持自托管（Self-hosted）以确保数据隐私，也可使用便捷的云服务版本。
*   **MCP 协议支持**：原生支持模型上下文协议（MCP），便于与现代 AI 代理和服务器进行交互。

3. **适用场景**
*   **企业数据同步与ETL**：自动从多个 SaaS 平台提取数据，经过清洗转换后同步至数据库或数据仓库。
*   **AI 驱动的业务流程**：利用 LLM 自动分析客户邮件、生成报告或执行复杂的智能决策任务。
*   **开发者运维自动化**：通过 CLI 和 API 自动化代码部署、监控告警通知及 CI/CD 流程中的特定环节。

4. **技术亮点**
*   **基于 TypeScript 构建**：拥有优秀的类型安全和现代化的开发体验，便于社区扩展和二次开发。
*   **公平代码许可（Fair-code）**：在保持开源精神的同时，合理规范商业使用，平衡了开发者生态与可持续性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197498 | 🍴 59543 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- **1. 中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建人工智能，实现 AI 的普惠化愿景。其核心使命是提供强大的工具支持，帮助用户将精力集中在真正重要的事务上。

**2. 核心功能**
- **自主智能代理**：具备独立规划、执行任务及自我修正能力的 AI 代理。
- **多模型兼容**：支持接入 OpenAI (GPT)、Anthropic (Claude) 及 LLaMA 等多种大型语言模型 API。
- **全栈开发辅助**：能够自动完成代码编写、调试及复杂项目的搭建工作。
- **互联网交互能力**：可自主浏览网页、获取实时信息并整合数据以完成任务。
- **持久化记忆与存储**：利用向量数据库等技术保留上下文记忆，确保长期任务的连续性。

**3. 适用场景**
- **自动化工作流**：替代人工执行重复性高、步骤繁琐的后台数据处理或调研任务。
- **软件原型开发**：快速生成代码片段、搭建基础项目结构或进行初步的技术验证。
- **智能市场调研**：自动收集网络信息、分析竞争对手动态并生成综合报告。
- **个人效率助手**：作为私人 AI 助理，管理日程、整理文件或协调多步骤个人事务。

**4. 技术亮点**
- 采用先进的 Agentic AI 架构，实现了从目标拆解到行动执行的闭环自动化。
- 高度模块化设计，允许开发者灵活替换底层模型或扩展自定义工具插件。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185651 | 🍴 46073 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166215 | 🍴 21484 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164229 | 🍴 30434 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157225 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154489 | 🍴 8801 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152224 | 🍴 9626 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

