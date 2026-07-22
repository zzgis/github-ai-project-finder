# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- 1. **中文简介**
thinking-orbs 是一款专为 AI 和智能体用户界面设计的虚线思维球加载指示器组件。它提供了六种精心调优的动画状态、两种尺寸选择以及自动适配深色与浅色模式的功能，旨在提升交互体验。

2. **核心功能**
*   提供六种不同的动态加载状态，模拟“思考”过程。
*   支持两种可选尺寸，灵活适配不同布局需求。
*   具备自动检测并切换深色/浅色模式的能力。
*   基于 TypeScript 开发，类型安全且易于集成。

3. **适用场景**
*   大型语言模型（LLM）聊天界面的等待状态提示。
*   自主智能体（Agent）执行复杂任务时的进度展示。
*   需要体现“正在思考”或“处理中”状态的生成式 AI 应用。
*   现代 Web 应用中追求极简主义风格的加载反馈设计。

4. **技术亮点**
*   采用虚线动画效果，视觉上比传统旋转圆圈更具“思维”隐喻感。
*   原生支持自动主题适配，减少开发者手动维护样式的成本。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 450 | 🍴 28 | 语言: TypeScript

### BossConsole
- **1. 中文简介**
BossConsole 是一款开源、跨平台的 AI 智能体控制台，采用原生 JVM 架构（基于 Kotlin Multiplatform），支持多线程运行。它提供了一个集成真实浏览器、终端和编辑器的操作界面，用于高效调度 Claude Code、Codex、Gemini 或 OpenCode 等主流 AI 工具。

**2. 核心功能**
*   **多模型统一调度**：原生支持运行 Claude Code、Codex、Gemini 及 OpenCode 等多种 AI 智能体。
*   **全栈集成环境**：内置实时浏览器渲染、终端交互、代码编辑器以及密钥管理功能。
*   **强大的扩展能力**：预置 100 多种 MCP (Model Context Protocol) 工具，支持热重载以快速迭代开发。
*   **企业级安全管控**：提供细粒度的 RBAC（基于角色的访问控制），确保企业环境下的权限安全。
*   **高性能原生体验**：基于 JVM 和 Compose Multiplatform 构建，非 Electron 方案，提供更轻量和原生的桌面应用体验。

**3. 适用场景**
*   **企业研发提效**：适合需要统一管理多个 AI 编码助手并严格管控权限的大型研发团队。
*   **科学研究与数据探索**：研究人员可利用其内置浏览器和终端快速进行多步骤的数据分析与模型测试。
*   **复杂工作流自动化**：开发者可通过 MCP 工具链将多个 AI 代理串联，实现复杂的自动化任务编排。

**4. 技术亮点**
*   **Kotlin Multiplatform & JVM 原生架构**：摒弃 Electron 框架，利用 Kotlin 和 Compose Multiplatform 打造高性能、跨平台的原生桌面应用。
*   **MCP 协议深度集成**：原生支持 Model Context Protocol，无缝连接海量外部工具和上下文数据。
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 146 | 🍴 2 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### open-ai-canvas
- 1. **中文简介**
open-ai-canvas 是一款专为 AI 影视创作打造的开源无限画布工作台。它深度集成了多模态内容生成、分镜编排、素材管理以及 Agent 智能工作流，旨在为创作者提供高效的一站式制作体验。

2. **核心功能**
*   提供无限画布界面，支持自由拖拽与布局设计。
*   集成多模态 AI 生成能力，支持图像、视频等内容的创建。
*   内置专业分镜编排工具，便于影视流程的结构化管理。
*   具备完善的素材库管理系统，实现资源的高效调用与维护。
*   支持基于 Agent 的自动化工作流，提升创作效率与灵活性。

3. **适用场景**
*   AI 辅助电影或短视频的分镜脚本设计与视觉预演。
*   创意团队进行多模态内容生成的协作与项目管理。
*   独立开发者或创作者利用自动化工作流批量生产影视素材。
*   需要灵活可视化界面来整合多种 AI 工具的工作台搭建。

4. **技术亮点**
*   采用 TypeScript 开发，保证代码的可维护性与类型安全。
*   将复杂的影视制作流程抽象为可视化的节点与工作流。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 61 | 🍴 16 | 语言: TypeScript

### pgContext
- 1. **中文简介**
pgContext 是一个构建在 PostgreSQL 数据库内部的完整 AI 搜索引擎。它利用 Rust 语言开发，旨在让数据库直接具备强大的语义搜索和人工智能处理能力。

2. **核心功能**
- 将完整的 AI 搜索引擎功能原生集成到 PostgreSQL 中。
- 基于 Rust 构建，提供高性能的数据处理与查询能力。
- 支持在数据库层面直接进行语义搜索，无需外部复杂架构。

3. **适用场景**
- 需要在现有 PostgreSQL 实例中快速添加智能搜索功能的企业应用。
- 希望简化技术栈，避免维护独立向量数据库或搜索引擎服务的开发者。
- 对数据隐私要求高，希望所有 AI 处理都在本地数据库内部完成的场景。

4. **技术亮点**
- 采用 Rust 编程语言开发，确保了系统的高性能和内存安全性。
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 59 | 🍴 3 | 语言: Rust

### AIGuardSIEM
- 1. **中文简介**
AIGuardSIEM 是一个生产级的 SIEM/XDR 平台，能够以低于 15 毫秒的检测延迟处理每秒超过 100 万条事件（EPS）。该项目主要使用 C++、Go 和 Python 构建，旨在提供高性能的安全运营能力。

2. **核心功能**
*   支持通过 DPDK 进行高速数据包捕获与处理。
*   集成 ONNX 机器学习模型进行实时异常与威胁检测。
*   兼容 Sigma 规则引擎以实现标准化的安全事件响应。
*   利用 eBPF 技术提供细粒度的系统级监控。
*   内置 SOAR（安全编排、自动化及响应）功能以自动化处置流程。

3. **适用场景**
*   需要极高吞吐量和低延迟的大型企业安全运营中心（SOC）。
*   部署在 Kubernetes 环境下的云原生安全监控平台。
*   依赖机器学习算法进行高级持续性威胁（APT）检测的场景。
*   需要标准化规则（如 Sigma）快速适配新威胁的网络安全团队。

4. **技术亮点**
*   **极致性能**：采用 C++ 和 Go 混合开发，结合 DPDK 技术实现百万级 EPS 的高吞吐处理能力。
*   **AI 驱动**：原生集成 ONNX 运行时，将机器学习推理直接嵌入数据流水线，确保亚毫秒级检测速度。
*   **现代架构**：深度整合 eBPF 和 Kubernetes，符合现代云原生安全基础设施的最佳实践。
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 51 | 🍴 4 | 语言: C++
- 标签: anomaly-detection, cybersecurity, dpdk, endpoint-security, incident-response

### editaplot
- 描述: AI-guided editable scientific figures with Codex and local Origin/OriginPro
- 链接: https://github.com/hang-jin/editaplot
- ⭐ 38 | 🍴 2 | 语言: Python
- 标签: codex-skill, editable-figures, research, scientific-visualization, windows

### pm-manager
- 描述: Know what to fix next — local .pm governance skill pack for AI coding agents (Spec Kit–inspired).
- 链接: https://github.com/wei63w/pm-manager
- ⭐ 34 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude-code, cursor, project-management

### Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- 描述: The Industry‑Oriented AI Engineering Program blends theory with hands‑on projects. Students gain expertise in open‑source LLMs, prompt engineering, fine‑tuning, and agent development, preparing for impactful careers in healthcare AI, autonomous systems, and innovation.
- 链接: https://github.com/AnantVerma-2022/Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- ⭐ 31 | 🍴 0 | 语言: Jupyter Notebook

### style-pack-skill
- 描述: 从参考图提取视觉风格 DNA，强制生成标注与纯色双版色卡的 AI Agent Skill
- 链接: https://github.com/irenerachel/style-pack-skill
- ⭐ 30 | 🍴 6 | 语言: Python

### AIS3-2026-Material
- 描述: AIS3 2026 - AI 資安應用實作與模型安全
- 链接: https://github.com/stwater20/AIS3-2026-Material
- ⭐ 29 | 🍴 0 | 语言: Jupyter Notebook

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个全面且资源丰富的中文自然语言处理（NLP）工具库与资源合集，旨在为开发者提供从基础文本处理到高级深度学习模型的全方位支持。它涵盖了敏感词检测、实体抽取、情感分析、知识图谱构建以及语音识别等核心功能，并整合了大量开源数据集、预训练模型及经典算法代码。

2. **核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简转换、停用词库、同义/反义词库及文本纠错功能。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱抽取，基于BERT等模型的命名实体识别（NER），以及关系抽取和事件三元组提取。
*   **语义分析与生成**：包含文本情感值计算、句子相似度匹配、自动摘要生成、关键词抽取及基于GPT/BERT的文本生成与聊天机器人构建。
*   **多模态与垂直领域支持**：集成ASR语音识别、OCR文字识别、医疗/法律/金融等领域的专用词库、数据集及预训练模型。
*   **数据增强与可视化**：提供EDA数据增强工具、文本可视化库（如Scattertext）及知识图谱构建与问答系统解决方案。

3. **适用场景**
*   **智能客服与聊天机器人开发**：利用其中的对话语料、意图识别模型及QA框架快速搭建具备多轮对话能力的智能助手。
*   **内容安全与风控系统**：通过敏感词库、暴恐词表及谣言检测工具，实现对用户生成内容（UGC）的自动化审核与风险预警。
*   **垂直行业知识图谱构建**：借助医疗、金融、法律等领域的专用词库和实体链接技术，构建行业专用的知识图谱以支持精准问答或决策辅助。
*   **NLP算法研究与教学**：作为学习资源库，供研究人员和学生参考各类SOTA模型代码、基准数据集及经典论文复现示例。

4. **技术亮点**
*   **资源极度丰富**：整合了数百个高质量的中文NLP数据集、预训练模型（如BERT, ALBERT, RoBERTa）及开源工具链。
*   **覆盖全生命周期**：不仅提供单一算法，还涵盖了从数据清洗、标注、模型训练到应用部署（如OCR、ASR、QA）的完整NLP工作流。
*   **紧跟前沿技术**：包含了大量基于Transformer架构的最新模型实现及针对中文特性的优化方案（如全词覆盖BERT）。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81961 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
该项目是一个包含500个AI项目的代码集合，涵盖了机器学习、深度学习、计算机视觉和自然语言处理（NLP）等核心领域。它通过提供丰富的实战案例代码，帮助开发者快速理解并应用各类人工智能技术。

### 2. 核心功能
- 提供涵盖机器学习、深度学习、CV及NLP等领域的500个完整项目实例。
- 所有项目均附带可直接运行的源代码，便于学习和复现。
- 标签体系清晰，按技术领域细分，方便用户快速定位感兴趣的方向。
- 作为“Awesome”系列资源库，集中整理了高质量的AI开源项目。

### 3. 适用场景
- **AI初学者入门**：通过阅读和运行基础项目代码，快速掌握ML/DL核心概念。
- **工程师实战参考**：在开发具体AI功能时，寻找类似场景的代码模板或实现思路。
- **教学与培训**：作为高校课程或企业内部培训的案例库，展示理论落地过程。
- **技术选型调研**：快速浏览各领域的典型项目，评估不同技术栈的成熟度与应用范围。

### 4. 技术亮点
- **规模宏大且分类细致**：整合了500个项目，并明确标注了Python及相关AI子领域的标签。
- **高社区认可度**：拥有超过3.5万星标，证明其在开发者社区中的广泛使用和权威性。
- **全栈式学习资源**：不仅提供理论描述，更强调“with code”，直接提供工程化实现。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35618 | 🍴 7369 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，能够以图形化界面直观展示模型结构。

2. **核心功能**
- 支持加载并可视化多种模型格式（如 ONNX, TensorFlow, PyTorch, Keras, CoreML, SafeTensors 等）。
- 提供交互式图形界面，清晰展示网络层结构、张量形状及参数信息。
- 允许用户深入查看模型内部细节，便于调试和优化深度学习架构。

3. **适用场景**
- 开发者在构建或调试深度学习模型时，快速检查网络结构的正确性。
- 研究人员需要将复杂的模型架构转化为直观的图表，以便撰写论文或进行汇报。
- 工程师在不同框架间转换模型格式后，验证模型一致性。

4. **技术亮点**
- 基于 JavaScript 开发，具备跨平台特性，同时提供桌面应用和在线网页版，使用便捷。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，实现跨平台的高效协作。

2. **核心功能**
- 提供统一的模型表示格式，支持在不同深度学习框架间无缝交换模型。
- 包含丰富的算子库，覆盖主流神经网络所需的计算操作。
- 具备模型验证和优化工具链，确保模型结构的正确性与执行效率。
- 支持多种后端运行时环境，便于将模型部署到服务器、移动端或边缘设备。

3. **适用场景**
- 在PyTorch训练后导出模型，以便使用TensorFlow或ONNX Runtime进行推理服务。
- 将模型从一种硬件架构迁移至另一种，例如从CPU部署到GPU或专用AI芯片。
- 在开发环境中整合来自Scikit-learn等不同库的机器学习组件，构建端到端流水线。

4. **技术亮点**
- 作为行业通用的中间格式，打破了主流框架间的生态壁垒，显著降低了模型部署的复杂度。
- 链接: https://github.com/onnx/onnx
- ⭐ 21194 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- **1. 中文简介**
《机器学习工程开放书籍》（Machine Learning Engineering Open Book）是一部全面涵盖机器学习工程实践的知识库。它深入探讨了从模型训练、推理优化到大规模分布式系统搭建等全生命周期的技术细节。该项目旨在为从业者提供一套系统化、可落地的工程化指南。

**2. 核心功能**
*   **大规模训练支持**：详细讲解基于 PyTorch 和 Slurm 的大规模分布式训练策略及调试技巧。
*   **推理与部署优化**：提供针对大型语言模型（LLM）的高效推理加速、量化及部署方案。
*   **基础设施管理**：涵盖 GPU 集群管理、网络配置、存储优化及 MLOps 流水线构建。
*   **可扩展性设计**：介绍如何构建高可用、易扩展的机器学习基础设施以应对海量数据。

**3. 适用场景**
*   **大型语言模型研发**：适用于需要从零开始训练或微调 LLM 的研究团队和工程师。
*   **ML 基础设施搭建**：适合负责构建和维护公司级 GPU 集群及训练平台的 MLOps 工程师。
*   **生产环境部署优化**：用于解决模型上线后的推理延迟高、资源利用率低的生产环境问题。

**4. 技术亮点**
*   **实战导向**：内容紧贴工业界最佳实践，而非仅停留在理论层面，涵盖大量真实场景下的 Debugging 经验。
*   **全栈覆盖**：从底层硬件（GPU/网络/存储）到上层框架（Transformers/PyTorch）均有深入解析。
*   **开源共享**：作为开放书籍，持续更新社区反馈的最新工程解决方案，免费供全球开发者参考。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18450 | 🍴 1178 | 语言: Python
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
- ⭐ 11586 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10672 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
该项目是一个包含500个AI项目的代码集合，涵盖了机器学习、深度学习、计算机视觉和自然语言处理（NLP）等核心领域。它通过提供丰富的实战案例代码，帮助开发者快速理解并应用各类人工智能技术。

### 2. 核心功能
- 提供涵盖机器学习、深度学习、CV及NLP等领域的500个完整项目实例。
- 所有项目均附带可直接运行的源代码，便于学习和复现。
- 标签体系清晰，按技术领域细分，方便用户快速定位感兴趣的方向。
- 作为“Awesome”系列资源库，集中整理了高质量的AI开源项目。

### 3. 适用场景
- **AI初学者入门**：通过阅读和运行基础项目代码，快速掌握ML/DL核心概念。
- **工程师实战参考**：在开发具体AI功能时，寻找类似场景的代码模板或实现思路。
- **教学与培训**：作为高校课程或企业内部培训的案例库，展示理论落地过程。
- **技术选型调研**：快速浏览各领域的典型项目，评估不同技术栈的成熟度与应用范围。

### 4. 技术亮点
- **规模宏大且分类细致**：整合了500个项目，并明确标注了Python及相关AI子领域的标签。
- **高社区认可度**：拥有超过3.5万星标，证明其在开发者社区中的广泛使用和权威性。
- **全栈式学习资源**：不仅提供理论描述，更强调“with code”，直接提供工程化实现。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35618 | 🍴 7369 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，能够以图形化界面直观展示模型结构。

2. **核心功能**
- 支持加载并可视化多种模型格式（如 ONNX, TensorFlow, PyTorch, Keras, CoreML, SafeTensors 等）。
- 提供交互式图形界面，清晰展示网络层结构、张量形状及参数信息。
- 允许用户深入查看模型内部细节，便于调试和优化深度学习架构。

3. **适用场景**
- 开发者在构建或调试深度学习模型时，快速检查网络结构的正确性。
- 研究人员需要将复杂的模型架构转化为直观的图表，以便撰写论文或进行汇报。
- 工程师在不同框架间转换模型格式后，验证模型一致性。

4. **技术亮点**
- 基于 JavaScript 开发，具备跨平台特性，同时提供桌面应用和在线网页版，使用便捷。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的速查手册（Cheat Sheets）。这些资料旨在帮助研究者快速回顾和掌握关键概念、公式及代码片段，提升研究与开发效率。

2. **核心功能**
*   提供深度学习领域核心算法与模型的快速参考指南。
*   汇总机器学习常用数学公式与统计知识要点。
*   整理主流框架（如Keras）及工具库（如NumPy、Matplotlib）的代码示例。
*   涵盖从基础理论到高级应用的综合性技术备忘。

3. **适用场景**
*   研究人员在撰写论文或设计实验时快速查阅技术细节。
*   工程师在调试模型或编写代码时核对API用法与参数设置。
*   学生在学习AI课程时作为复习笔记或备考参考资料。
*   团队内部进行技术分享或新人入职培训时的辅助材料。

4. **技术亮点**
*   内容高度浓缩，将复杂的技术体系转化为易于消化的视觉化图表与代码块。
*   覆盖全面，整合了机器学习、深度学习及相关数据处理工具链的关键知识点。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式配置简化了机器学习流程，使开发者能够专注于数据而非底层代码。该框架支持广泛的模型类型和数据处理方式，大幅降低了 AI 应用的开发门槛。

2. **核心功能**
- 提供声明式 YAML 配置界面，无需编写复杂代码即可定义模型架构。
- 内置多种预训练模型和组件，支持快速集成计算机视觉、NLP 等任务。
- 自动化处理数据预处理、特征工程及模型评估流程。
- 支持端到端的模型训练、微调及部署，兼容 PyTorch 后端。
- 具备可解释性工具，帮助分析模型决策依据及特征重要性。

3. **适用场景**
- 希望快速原型化机器学习项目，减少编码工作量的数据科学家。
- 需要对现有大型语言模型（如 LLaMA、Mistral）进行高效微调的研究人员。
- 缺乏深度学习经验，但仍需构建定制 AI 模型的初级开发者或业务分析师。
- 需要标准化模型训练流程并确保实验可复现性的企业级 AI 团队。

4. **技术亮点**
- 采用“数据为中心”的设计理念，强调通过优化数据而非仅调整模型结构来提升性能。
- 高度模块化与可扩展性，允许用户轻松添加自定义组件或集成新算法。
- 无缝对接主流深度学习框架（如 PyTorch），同时保持接口简洁易用。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9143 | 🍴 1236 | 语言: Python
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
- ⭐ 6269 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能全面的中文自然语言处理（NLP）资源集合与工具库，涵盖了从基础文本处理、数据增强到高级知识图谱构建的多种实用资源。该项目集成了敏感词检测、实体抽取、情感分析及各类专业领域词库，为开发者提供了丰富的预训练模型、数据集和算法实现。

2. **核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词表、反动词表及文本纠错等功能。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱等正则抽取，以及基于BERT、BiLSTM等模型的命名实体识别（NER）和关系抽取。
*   **语义分析与情感计算**：包含词汇情感值分析、同义/反义词库、句子相似度匹配及文本分类模板代码。
*   **领域知识图谱与数据资源**：汇聚了医学、法律、金融、汽车等多个垂直领域的词库、数据集及知识图谱构建工具。
*   **语音与多模态支持**：集成中文OCR、ASR语音识别语料、发音标记（g2p）及语音情感分析相关资源。

3. **适用场景**
*   **内容安全审核系统开发**：利用其敏感词库、暴恐词表及谣言检测数据，快速搭建互联网内容的自动化审核平台。
*   **智能客服与对话机器人构建**：参考其对话语料、意图识别模型及QA数据集，训练具备闲聊或特定领域问答能力的Chatbot。
*   **垂直行业知识图谱建设**：借助其提供的医疗、金融、法律等领域专用词库和实体抽取工具，构建行业专属的知识图谱。
*   **NLP算法研究与教学**：作为学习资源库，获取各类经典NLP算法代码、最新预训练模型（如BERT、ALBERT）及权威数据集。

4. **技术亮点**
*   **资源极度丰富且全面**：不仅包含代码工具，还整合了大量高质量数据集、预训练模型权重及学术论文资料，是NLP初学者和研究者的“百科全书”。
*   **紧跟前沿技术栈**：收录了基于Transformer架构（BERT, GPT-2, RoBERTa等）的最新实现方案及微调技巧，确保技术时效性。
*   **注重落地应用**：提供了大量针对中文特性的优化方案，如中文分词加速、中文OCR、中文数字转换等，解决了通用库在中文场景下的适配痛点。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81961 | 🍴 15250 | 语言: Python

### LlamaFactory
- ### LlamaFactory 项目分析

1. **中文简介**
   LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目已发表于 ACL 2024 会议，旨在简化大模型的训练流程，提供从基础微调到大规模对齐的一站式解决方案。它通过集成多种前沿技术，降低了用户部署和优化高性能 AI 模型的门槛。

2. **核心功能**
   - 支持 100+ 种主流 LLMs 和 VLMs 的统一微调接口，涵盖 LLaMA、Qwen、Gemma 等。
   - 提供高效的参数高效微调（PEFT）方法，包括 LoRA、QLoRA 及全参数微调。
   - 集成 RLHF（基于人类反馈的强化学习）、DPO 等高级对齐训练算法。
   - 支持多种量化技术（如 INT8/INT4），显著降低显存占用并提升推理速度。
   - 内置指令微调（Instruction Tuning）数据格式处理，适配 Agent 和多轮对话场景。

3. **适用场景**
   - **垂直领域模型定制**：在医疗、法律或金融等专业数据集上对基座模型进行指令微调，提升特定任务表现。
   - **低成本私有化部署**：利用 QLoRA 等量化微调技术，在消费级显卡上高效微调大型模型，适合资源受限的团队。
   - **多模态应用开发**：对支持视觉输入的模型（如 LLaVA 系列）进行微调，开发图文理解或生成的智能应用。
   - **模型对齐与优化**：使用 DPO 或 RLHF 技术优化模型输出质量，使其更符合人类价值观和安全标准。

4. **技术亮点**
   - **统一架构**：屏蔽了不同模型底层的差异，使用户能用相同的代码结构微调任意支持的模型。
   - **极致效率**：通过 GPTQ/AWQ 量化和 FlashAttention 等技术，实现训练和推理的高效率与低显存消耗。
   - **社区驱动的前沿支持**：紧跟开源社区热点，快速集成最新发布的模型（如 DeepSeek、Llama 3 等）和训练范式。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73452 | 🍴 8965 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一门由微软推出的为期12周、包含24节课的人工智能通识课程，旨在让所有人轻松入门AI。课程采用Jupyter Notebook形式编写，内容覆盖从基础机器学习到深度学习的前沿技术。

2. **核心功能**
- 提供结构化的12周学习路径，将复杂的AI概念拆解为易于理解的24个独立课时。
- 基于Jupyter Notebook交互式环境，支持代码实时运行与可视化分析，降低学习门槛。
- 涵盖广泛的技术领域，包括机器学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）。
- 强调“AI for All”理念，适合零基础的初学者建立系统性的人工智能知识框架。

3. **适用场景**
- 希望系统性地从零开始学习人工智能的初学者或跨领域从业者。
- 需要寻找高质量、免费且结构化AI教学资源的教师或培训机构。
- 希望通过动手实践（Jupyter Notebook）快速验证AI算法效果的数据科学爱好者。

4. **技术亮点**
- 依托微软开源生态，内容权威且紧跟业界主流技术栈（如TensorFlow/PyTorch基础应用）。
- 采用模块化教学设计，兼顾理论讲解与代码实操，特别适合编程背景的初学者进阶。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52630 | 🍴 10665 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深入讲解线性代数基础及 PyTorch、NLTK、TensorFlow 2 等主流框架。该项目旨在帮助开发者系统性地掌握从传统算法到深度学习的全栈技能。

2. **核心功能**
- 集成经典机器学习算法（如 SVM、K-Means、随机森林等）的代码实现与原理分析。
- 提供深度学习（DNN、RNN、LSTM）及自然语言处理（NLP）的实战案例。
- 包含推荐系统、关联规则挖掘（Apriori、FP-Growth）等高级应用场景。
- 融合数学基础（线性代数）与 Python 编程（Scikit-learn、PyTorch），构建完整知识体系。

3. **适用场景**
- AI 初学者系统学习机器学习理论与 Python 编程实战。
- 数据科学家复习和参考经典算法（如聚类、分类、降维）的实现细节。
- NLP 研究人员利用 NLTK 和 TensorFlow/PyTorch 进行文本处理模型开发。
- 企业开发人员构建推荐系统或探索性数据分析（EDA）项目时的参考指南。

4. **技术亮点**
- 内容覆盖面极广，从基础数学到前沿深度学习框架均有涉及，适合一站式学习。
- 结合理论推导与代码实战，不仅提供算法逻辑，还强调工程落地能力。
- 社区热度高（4万+星标），证明其作为开源学习资源的广泛认可度和实用性。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42404 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入掌握人工智能工程的核心原理与实践。它不仅提供系统的课程学习，更强调将所学知识转化为实际可部署的AI应用，实现“学习、构建、交付”的完整闭环。

2. **核心功能**
- 提供从基础到高级的AI工程全栈教程，涵盖LLM、计算机视觉及强化学习等关键领域。
- 指导用户从零构建智能体（Agents）和生成式AI应用，而非仅调用现有API。
- 集成多语言技术栈，结合Python与Rust实现高性能AI系统的开发与优化。
- 聚焦于MCP（模型上下文协议）和群体智能等前沿工程实践，提升系统互操作性。

3. **适用场景**
- 希望深入理解AI底层逻辑，摆脱对黑盒库依赖的高级开发者或研究人员。
- 需要构建定制化、高性能且具备自主决策能力的AI智能体的工程团队。
- 致力于将生成式AI技术落地为可实际部署的生产级应用的初创公司或个人开发者。

4. **技术亮点**
- 采用“从 scratch（从零）”的教学方法，彻底解析Transformer、Rust底层优化及RL算法实现细节。
- 紧跟最新技术趋势，整合了MCP协议、Swarm Intelligence（群体智能）等新兴工程范式。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42006 | 🍴 6991 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35618 | 🍴 7369 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33763 | 🍴 4698 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28771 | 🍴 3512 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25984 | 🍴 2944 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21741 | 🍴 3304 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35618 | 🍴 7369 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22553 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API，旨在简化数据标注流程。

2. **核心功能**
*   支持图像、视频及3D点云的多模态数据标注。
*   提供AI辅助标注功能，显著提升标注效率与准确性。
*   内置质量控制机制与团队协作工具，确保数据集一致性。
*   开放开发者API，便于集成到现有的机器学习工作流中。

3. **适用场景**
*   大规模计算机视觉数据集的自动化与半自动化标注。
*   团队协同进行物体检测、语义分割或图像分类任务。
*   需要严格质量控制和版本管理的工业级AI项目数据准备。

4. **技术亮点**
*   兼容主流深度学习框架（如PyTorch、TensorFlow），支持从ImageNet等标准数据集导入。
*   提供丰富的标签类型（如边界框、多边形、关键点），覆盖目标检测与分割等多种任务需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16360 | 🍴 3770 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
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
- ⭐ 3293 | 🍴 403 | 语言: Python
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
OpenClaw 是一款基于“龙虾”风格的个人 AI 助手，支持任意操作系统和平台部署。它强调数据自主权，让用户能够完全掌控自己的私有 AI 助理。

2. **核心功能**
*   跨平台兼容，可在任何操作系统上运行。
*   提供个人化 AI 助手体验，支持自定义交互。
*   注重数据隐私与所有权，确保用户数据自主可控。
*   采用 TypeScript 开发，具备良好的可扩展性和维护性。

3. **适用场景**
*   需要在本地或私有服务器上部署专属 AI 助手的开发者。
*   对数据隐私高度敏感、拒绝使用云端黑盒服务的个人用户。
*   希望在不同操作系统间无缝切换并保持一致 AI 体验的技术爱好者。

4. **技术亮点**
*   基于 TypeScript 构建，利用其类型安全优势提升代码质量。
*   模块化设计支持灵活集成各种 AI 模型与后端服务。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383814 | 🍴 80639 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论，旨在提升开发效率。它通过结构化的“技能”体系，指导 AI 代理（Agent）更准确地执行复杂任务。该项目为基于 AI 的软件开发提供了一套切实可行的实践标准。

**2. 核心功能**
*   **智能体技能框架**：提供模块化的“技能”定义，使 AI 代理能够理解并执行特定的开发任务。
*   **结构化开发方法论**：整合了头脑风暴、编码及软件开发生命周期（SDLC），规范 AI 辅助开发的流程。
*   **子代理驱动开发**：支持通过子代理（Subagent）分解和驱动复杂开发任务，实现分工协作。
*   **全流程 AI 集成**：覆盖从需求构思到代码实现的完整软件开发生命周期，强化 AI 在研发各环节的作用。

**3. 适用场景**
*   **AI 辅助编程工作流优化**：用于构建或优化基于 LLM 的代码生成与重构流水线。
*   **复杂软件项目规划**：在大型项目中利用结构化方法论协调多个 AI 子代理进行并行开发。
*   **智能体应用开发**：作为基础框架，快速搭建具备特定领域技能（如代码审查、测试编写）的 AI 助手。
*   **研发方法论标准化**：团队希望将 AI 介入软件开发的流程标准化、可重复化时使用。

**4. 技术亮点**
*   **方法论与工具结合**：不仅提供代码，更输出一套经过验证的“如何正确使用 AI 进行开发”的方法论。
*   **标签化技能体系**：通过 `obra` 等标签化管理技能，实现技能的复用和组合，提升 AI 任务的精准度。
- 链接: https://github.com/obra/superpowers
- ⭐ 259283 | 🍴 23113 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218845 | 🍴 41436 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合的开发模式。用户可以选择自托管或云端部署，并通过其提供的 400 多种集成轻松连接各类应用。

2. **核心功能**
*   提供直观的可视化拖拽界面，降低工作流搭建门槛。
*   内置原生 AI 能力，支持智能自动化任务处理。
*   拥有超过 400 种现成集成，兼容广泛的服务和 API。
*   支持自托管私有化部署及云端使用，保障数据灵活性与安全性。
*   允许在可视化流程中嵌入自定义代码，满足复杂业务逻辑需求。

3. **适用场景**
*   企业级系统集成，通过自动化流程打通不同 SaaS 工具间的数据孤岛。
*   需要高度数据隐私保护的团队，利用自托管方案实现本地化 AI 与工作流管理。
*   开发者希望结合低代码效率与代码灵活性，快速构建定制化后端自动化脚本。
*   日常运营中的重复性任务自动化，如数据同步、邮件通知及报表生成。

4. **技术亮点**
*   采用 TypeScript 开发，类型安全且易于维护扩展。
*   开源公平代码（Fair-code）协议，兼顾开放生态与商业可持续性。
*   深度集成 MCP（Model Context Protocol）支持，强化与大语言模型的交互能力。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197468 | 🍴 59537 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松访问、使用并构建基于 AI 的工具，其愿景是赋能大众。该项目的使命是通过提供强大的工具，让用户能够专注于真正重要的核心事务。

2. **核心功能**
*   实现自主智能体（Autonomous Agents），能够独立规划并执行复杂的多步任务。
*   支持多种大型语言模型（LLM）后端，包括 OpenAI GPT、Claude 及 Llama 等 API。
*   提供可扩展的框架结构，便于开发者在此基础上构建和定制特定的 AI 应用。
*   具备网络浏览、文件读写及代码执行能力，使其能处理涉及外部交互的实际工作流。

3. **适用场景**
*   自动化重复性高的日常办公任务，如数据整理、邮件回复或日程安排。
*   进行复杂的科学研究或市场分析，利用智能体自动搜索信息、汇总报告。
*   作为开发者的实验平台，用于测试和研究自主 AI 智能体的行为逻辑与边界。

4. **技术亮点**
*   采用模块化设计，解耦了核心智能逻辑与底层 LLM 接口，提高了系统的灵活性和可维护性。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185655 | 🍴 46071 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166207 | 🍴 21481 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164297 | 🍴 30432 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157220 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154395 | 🍴 8797 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152214 | 🍴 9627 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

