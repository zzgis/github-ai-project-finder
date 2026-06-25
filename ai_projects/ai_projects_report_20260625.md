# GitHub AI项目每日发现报告
日期: 2026-06-25

## 新发布的AI项目

### awesome-evals
- 描述: A curated, non-BS library of the best resources for building and evaluating AI agents — papers, blogs, talks, tools, benchmarks. Maintained by BenchFlow.
- 链接: https://github.com/benchflow-ai/awesome-evals
- ⭐ 178 | 🍴 7 | 语言: 未知
- 标签: agent-evaluation, ai-agents, awesome, awesome-list, benchmarks

### ShipGenAI
- 1. **中文简介**
ShipGenAI 提供50款可直接投入生产环境的生成式AI SaaS应用模板，开发者可对其进行品牌定制、快速部署并保留全部收益。该项目集成了Stripe计费、Google OAuth认证及Vercel一键部署功能，采用MIT开源协议，基于JavaScript/TypeScript和Next.js构建。

2. **核心功能**
*   提供50个现成的生成式AI SaaS应用代码库，涵盖文本、图像及视频生成等领域。
*   内置完整的商业化基础设施，包括Stripe支付结算系统和Google OAuth用户认证。
*   支持在Vercel平台上实现无缝的一键部署与托管，极大简化上线流程。
*   采用Next.js框架结合TypeScript开发，确保代码的高性能与类型安全。

3. **适用场景**
*   希望快速验证生成式AI商业模式并实现盈利的独立开发者或初创团队。
*   需要从零搭建具备付费墙和用户管理功能的AI工具站的SaaS创业者。
*   旨在通过复用高质量开源模板来降低前端与后端集成成本的Web开发者。

4. **技术亮点**
*   **全栈开箱即用**：集成了从用户认证、支付处理到AI API调用的完整SaaS闭环逻辑。
*   **现代化技术栈**：基于Next.js和TypeScript，兼顾开发体验与生产环境稳定性。
*   **高自由度定制**：MIT协议允许自由修改和品牌重塑，确保开发者拥有完全的商业控制权。
- 链接: https://github.com/benlamiro/ShipGenAI
- ⭐ 74 | 🍴 0 | 语言: JavaScript
- 标签: ai, boilerplate, generative-ai, gpt, image-generation

### agentic-ai-local-to-kubernetes
- 1. **中文简介**
本项目是题为《Agentic AI：从本地环境到 Kubernetes》的技术演讲的配套代码仓库。它展示了如何将基于 Agent 的 AI 应用从单机本地部署平滑迁移至 Kubernetes 集群中运行。内容主要涵盖架构设计、容器化及编排策略的实现细节。

2. **核心功能**
*   演示 Agentic AI 应用在本地开发环境中的基础搭建与运行逻辑。
*   提供将 AI Agent 服务容器化并部署到 Kubernetes 集群的完整流程。
*   展示 Kubernetes 环境下针对 AI 工作负载的资源管理、服务发现及弹性伸缩配置。
*   包含用于验证本地与云端部署一致性的测试脚本或示例代码。

3. **适用场景**
*   希望将现有的本地 AI Agent 原型快速转化为生产级微服务架构的开发者。
*   正在研究如何在 K8s 上高效运行和管理大规模 LLM 或 Agent 应用的运维工程师。
*   需要参考具体代码案例来理解 Agentic AI 系统云原生改造路径的技术听众。

4. **技术亮点**
*   提供了从开发到生产环境部署的端到端实战参考，填补了理论演讲与落地实施之间的空白。
*   聚焦于 Python 生态下的 Agentic AI 模式，解决了非传统 Web 应用在 Kubernetes 中运行的特殊挑战。
- 链接: https://github.com/lkerriso/agentic-ai-local-to-kubernetes
- ⭐ 15 | 🍴 3 | 语言: Python

### nexusbox
- 1. **中文简介**
NexusBox 是一个专为 AI Agent 设计的安全沙箱环境，支持通过 MCP 协议执行 Shell、文件、代码及浏览器命令。它确保所有操作在隔离环境中运行，从而保障系统安全。

2. **核心功能**
*   提供基于 MCP 协议的标准化接口，方便 AI Agent 集成。
*   支持多种命令类型执行，包括 Shell 脚本、文件操作、代码编译及浏览器自动化。
*   采用严格的隔离机制，防止恶意操作影响宿主系统。
*   专注于 AI Agent 的安全执行环境，降低运行时风险。

3. **适用场景**
*   需要高安全性执行外部命令的 AI Agent 应用开发。
*   希望将浏览器自动化或代码执行功能集成到 AI 工作流中的场景。
*   对沙箱隔离有严格要求的生产级 AI 代理部署环境。

4. **技术亮点**
*   使用 Go 语言开发，具备高性能和轻量级的优势。
*   原生支持 MCP 协议，简化了与各类 AI 模型的对接过程。
- 链接: https://github.com/lxcshine/nexusbox
- ⭐ 13 | 🍴 4 | 语言: Go

### ai-fishing-game
- 1. **中文简介**
这是一款专为 AI 设计的确定性文字钓鱼小游戏，采用单文件架构且零外部依赖。你可以邀请你的 AI 伴侣参与互动，体验这种轻量级的文字冒险乐趣。

2. **核心功能**
*   **AI 专属交互**：游戏逻辑专为大型语言模型设计，支持通过文本指令与 AI 进行钓鱼互动。
*   **零依赖部署**：项目仅包含单个 Python 文件，无需安装任何第三方库即可直接运行。
*   **确定性机制**：基于规则的文字游戏，确保每次运行的逻辑结果可预测且一致。
*   **极简体验**：去除复杂图形界面，专注于核心的文字逻辑与指令解析。

3. **适用场景**
*   **AI 娱乐测试**：开发者用于测试或展示 AI 伴侣在简单游戏规则下的响应能力。
*   **轻量级集成**：嵌入到聊天机器人或智能助手应用中，作为增加用户互动的趣味小插件。
*   **教学演示**：用于向初学者展示如何在没有额外依赖的情况下编写简单的逻辑游戏。

4. **技术亮点**
*   **极致轻量化**：单文件实现完整游戏逻辑，极大降低了代码维护成本和运行环境配置难度。
- 链接: https://github.com/tutusagi/ai-fishing-game
- ⭐ 11 | 🍴 2 | 语言: Python

### patchright-browser
- 描述: MCP server for browser automation via Patchright. Multi-profile Chromium, headed/headless, StreamableHTTP protocol. Includes dashboard, skills, and AI agent setup.
- 链接: https://github.com/rickicode/patchright-browser
- ⭐ 9 | 🍴 1 | 语言: Python
- 标签: ai-agent, browser-automation, chromium, headless-browser, hermes

### Learning-AI
- 描述: 大语言模型原理与实践 — 学习笔记
- 链接: https://github.com/ChenLinXXXX/Learning-AI
- ⭐ 7 | 🍴 0 | 语言: 未知

### codex-ai-ppt
- 描述: Review-gated image-based PPT generation for Codex
- 链接: https://github.com/Y4tacker/codex-ai-ppt
- ⭐ 7 | 🍴 0 | 语言: Python

### xs_vibe_rules
- 描述: My Cursor Rules for AI coding assistants — battle-tested constraints from real projects
- 链接: https://github.com/itshen/xs_vibe_rules
- ⭐ 7 | 🍴 0 | 语言: 未知

### Graphenium
- 描述: Persistent structural memory for AI coding agents. Turns your repo into a fast, MCP-native knowledge graph so assistants stop grepping and start querying.
- 链接: https://github.com/lambda-alpha-labs/Graphenium
- ⭐ 7 | 🍴 0 | 语言: Rust
- 标签: ai-coding, code-analysis, knowledge-graph, mcp, mcp-server

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具箱，旨在为开发者提供从基础文本清洗、实体抽取到高级知识图谱构建及对话生成的全套解决方案。该项目不仅涵盖了敏感词检测、分词、词性标注等核心功能，还集成了大量高质量的中文语料库、专业领域词库以及基于深度学习（如BERT）的预训练模型资源。

### 2. 核心功能
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词管理、反动词表、拆字词典及词汇情感值分析，支持文本标准化处理。
*   **信息抽取与实体识别**：集成手机号、身份证号、邮箱、地址的自动抽取，支持基于BERT等模型的命名实体识别（NER），以及关键词和摘要提取。
*   **知识图谱与词库资源**：收录中日韩人名、行业（汽车、医疗、法律、金融等）专业词库、成语、古诗词及百科知识，提供跨语言知识图谱构建工具和实体链接库。
*   **对话系统与生成式AI**：包含中文聊天机器人训练数据（如青云语料）、自动对联生成、基于GPT-2/BERT的文本生成、摘要及问答系统（QA）相关代码与模型。
*   **多模态与语音处理**：涵盖中文语音识别（ASR）数据集、发音词典、语音情感分析、手写汉字识别（OCR）及音频数据增强工具。

### 3. 适用场景
*   **智能客服与聊天机器人开发**：利用其提供的对话语料、意图识别模型及多轮对话框架，快速构建具备上下文理解能力的智能客服或娱乐型聊天机器人。
*   **内容安全与风控系统**：通过敏感词库、暴恐词表及谣言检测工具，应用于社交媒体、论坛或新闻平台的内容审核，自动识别并拦截违规或虚假信息。
*   **垂直领域知识图谱构建**：借助丰富的行业词库（医疗、金融、法律）和实体抽取工具，构建特定领域的结构化知识库，支持下游的语义搜索或决策支持系统。
*   **NLP数据预处理与分析**：作为数据科学家和算法工程师的基础工具包，用于快速完成文本清洗、分词、情感分析及特征工程，加速模型训练流程。

### 4. 技术亮点
*   **资源极度丰富**：整合了数百个中文NLP数据集、词库及预训练模型（如ELECTREA、ALBERT、BERT），极大降低了数据准备门槛。
*   **全栈式工具链**：覆盖了从底层文本处理（分词、OCR）、中层信息抽取（NER、关系抽取）到上层应用（对话生成、QA）的完整NLP技术栈。
*   **紧跟前沿技术**：集成了最新的深度学习模型应用案例，如基于Transformer的摘要生成、对抗性文本生成及注意力机制可视化，便于研究者复现和参考。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81429 | 🍴 15243 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的资源库。该项目汇集了带有代码实现的各类人工智能实战案例，旨在为开发者提供丰富的学习素材。它涵盖了从基础概念到高级应用的广泛主题，是入门和进阶的优质参考指南。

2. **核心功能**
*   提供500多个涵盖机器学习、深度学习及NLP等领域的完整项目代码。
*   集成计算机视觉与自然语言处理的具体实战案例供用户参考。
*   作为“Awesome”列表，聚合了高质量的人工智能开源资源。
*   支持多种AI子领域的项目分类，便于快速定位所需技术栈。

3. **适用场景**
*   AI初学者希望通过大量实际代码示例快速掌握机器学习基础。
*   研究人员或开发者需要寻找计算机视觉或NLP领域的灵感与参考实现。
*   教育机构利用这些项目作为教学案例，辅助学生理解抽象算法。
*   工程师在构建新模型时，通过对比现有开源项目优化自身解决方案。

4. **技术亮点**
*   极高的社区认可度，拥有超过3.4万星标，证明其资源的权威性与实用性。
*   标签体系完善，明确区分了ML、DL、CV、NLP等细分技术领域。
*   强调“带代码”的项目集合，不仅提供理论，更注重工程落地实践。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34841 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款轻量级的神经网络、深度学习及机器学习模型可视化工具。它支持多种主流框架生成的模型文件，能够以图形化界面直观展示模型结构与参数。该工具旨在帮助开发者快速理解和分析复杂的模型架构。

### 2. 核心功能
*   广泛支持 TensorFlow、PyTorch、Keras、ONNX、CoreML 等主流格式的模型可视化。
*   提供直观的节点图视图，清晰展示网络层之间的连接关系和数据流向。
*   支持查看模型的具体参数、权重分布及张量形状等详细信息。
*   具备跨平台兼容性，可通过桌面应用或浏览器直接打开本地模型文件。

### 3. 适用场景
*   **模型调试与验证**：开发者在构建新模型时，通过可视化检查网络结构是否符合预期。
*   **模型转换监控**：在使用 ONNX 等中间格式进行框架间模型转换后，确认结构完整性。
*   **技术分享与文档**：向非技术人员或团队成员直观展示深度学习模型的内部工作原理。
*   **错误排查**：快速定位模型加载失败或推理异常时的结构问题。

### 4. 技术亮点
*   **零依赖运行**：无需安装庞大的深度学习框架即可独立查看模型，启动速度快且资源占用低。
*   **多格式统一解析**：内置强大的解析引擎，能统一处理不同框架特有的模型定义差异。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33124 | 🍴 3138 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与运行，打破生态壁垒。通过统一表示形式，开发者可以更灵活地在各种硬件和软件环境中部署AI模型。

2. **核心功能**
- 定义开放的中间表示格式，支持跨框架加载和保存模型。
- 提供工具链以实现从主流框架（如PyTorch、TensorFlow）到ONNX的模型导出。
- 支持在多种后端（如CPU、GPU、NPU）上高效执行推理任务。
- 允许对导出的ONNX模型进行优化、剪枝或量化处理。

3. **适用场景**
- 需要在不同深度学习框架间迁移模型代码的开发场景。
- 针对特定嵌入式设备或边缘计算平台进行模型部署优化的场景。
- 企业级应用中要求模型具备跨平台兼容性和长期可维护性的场景。
- 研究人员希望在不同硬件加速卡上评估模型性能的场景。

4. **技术亮点**
- 实现了真正的框架无关性，消除了供应商锁定风险。
- 拥有活跃的社区支持和广泛的硬件厂商适配。
- 提供了标准化的算子集合，确保模型语义的一致性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21038 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一部全面涵盖机器学习工程实践的系统性指南。该项目深入探讨了从大规模分布式训练、模型优化到高效推理部署的全链路关键技术。它旨在为研究人员和工程师提供构建高性能、可扩展ML系统的实用参考。

2. **核心功能**
*   提供大规模分布式训练（如PyTorch/Slurm）与集群管理的最佳实践。
*   详解大语言模型（LLM）的微调策略、架构选择及调试技巧。
*   涵盖高性能模型推理优化、内存管理及GPU资源调度方案。
*   介绍MLOps全流程，包括数据存储、网络通信及系统可扩展性设计。

3. **适用场景**
*   构建和训练超大规模预训练语言模型的基础设施搭建。
*   优化深度学习模型的推理延迟并降低GPU计算成本。
*   解决分布式训练中的通信瓶颈、故障排查及稳定性问题。
*   企业级机器学习平台的工程化落地与运维标准化。

4. **技术亮点**
*   聚焦于当前最前沿的大模型（LLM）工程挑战与解决方案。
*   内容紧贴工业界实战，涵盖PyTorch、Slurm等主流工具链的深度应用。
*   结构化的知识体系，从底层硬件（GPU/存储/网络）到上层框架（Transformers）全覆盖。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18170 | 🍴 1152 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17255 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13084 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11522 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10639 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。它提供了丰富的实战代码示例，旨在帮助开发者快速掌握相关技术并进行实践应用。

2. **核心功能**
- 提供大量现成的AI项目源代码，覆盖主流算法与模型。
- 整合机器学习、深度学习、计算机视觉及NLP四大方向的技术案例。
- 作为学习资源库，支持从基础理论到复杂项目的全链路实践。
- 代码结构清晰，便于开发者直接运行、修改和二次开发。

3. **适用场景**
- 初学者入门：通过阅读和运行代码快速理解AI基本概念。
- 项目参考：为实际开发提供可复用的代码模板和技术方案。
- 技能提升：深入研究特定领域（如CV或NLP）的高级实现细节。

4. **技术亮点**
- 项目数量庞大且分类明确，是全面覆盖AI主要子领域的优质资源库。
- 包含“awesome”标签，意味着其内容经过筛选，具有较高的质量和实用性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34841 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它能够直观地展示模型结构，帮助开发者深入理解算法架构与数据流向。该工具支持多种主流框架格式，是模型调试与分析的高效辅助软件。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、PyTorch、TensorFlow、Keras 及 CoreML 等。
*   提供清晰的模型架构图视图，直观呈现层连接关系与张量维度。
*   具备实时交互能力，允许用户缩放、平移及点击节点查看详细参数信息。
*   兼容桌面端应用与 Web 浏览器访问，无需安装即可通过网页预览模型。

3. **适用场景**
*   **模型调试与验证**：在部署前检查模型结构是否正确，排查层连接错误。
*   **学术交流与展示**：生成高质量的模型结构图，用于论文撰写或技术汇报演示。
*   **跨框架迁移分析**：对比不同框架下同一模型的内部表示，辅助模型转换工作。

4. **技术亮点**
*   **轻量级开源**：基于 JavaScript 开发，无复杂依赖，启动迅速且易于集成。
*   **高兼容性**：几乎覆盖所有主流深度学习框架的最新版本，更新响应速度快。
*   **多端同步**：桌面应用与在线版本体验一致，方便在不同环境下快速查看模型。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33124 | 🍴 3138 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一个免费的人工智能学习路线图，整理了近200个实战案例与项目，旨在帮助零基础用户从入门到实现就业实战。该资源涵盖 Python、数学基础以及机器学习、深度学习、NLP、CV 等主流技术领域，并提供配套教材。

2. **核心功能**
*   提供完整的人工智能学习路径规划，覆盖从基础数学到高级算法的全流程。
*   收录近200个精选实战案例与开源项目，强化动手能力与工程经验。
*   免费提供配套学习资料和教材，降低 AI 领域的入门门槛。
*   整合 TensorFlow、PyTorch、Keras 等多框架教程，适应不同技术栈需求。

3. **适用场景**
*   希望从零开始系统学习人工智能的初学者。
*   需要大量实战案例来提升简历竞争力以寻求就业的求职者。
*   想要快速查阅特定 AI 子领域（如 NLP 或 CV）技术栈的学习者。

4. **技术亮点**
该项目作为社区维护的资源聚合库，凭借极高的收藏量（13000+ Star）证明了其在 AI 教育领域的广泛认可度和实用性。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13084 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他人工智能模型的构建与训练过程。它通过声明式配置，让开发者无需编写大量底层代码即可快速实现从数据处理到模型部署的全流程，极大地降低了 AI 应用的开发门槛。

### 2. 核心功能
*   **低代码声明式建模**：用户仅需通过 YAML 或 JSON 配置文件定义模型结构和数据列映射，即可自动构建深度学习模型。
*   **多模态支持**：原生支持文本、图像、音频、视频、表格及结构化数据等多种数据类型，方便处理复杂的多模态任务。
*   **端到端训练流程**：内置完整的数据预处理、特征工程、模型训练、超参数调整及评估模块，实现一键式模型迭代。
*   **广泛的模型兼容性**：基于 PyTorch 构建，兼容 Hugging Face Transformers，支持主流 LLM（如 Llama、Mistral）的微调与推理。

### 3. 适用场景
*   **快速原型开发**：数据科学家希望在短时间内验证不同架构在特定数据集上的效果，而不愿花费时间编写底层训练逻辑。
*   **企业级 AI 应用落地**：需要稳定、可复现且易于维护的机器学习流水线，以标准化方式部署表格数据或基础 NLP 模型。
*   **多模态数据分析**：涉及同时处理文本描述、图像内容或音频信号的综合性 AI 任务，如内容审核或多媒体检索系统。

### 4. 技术亮点
*   **自动化特征工程**：Ludwig 能根据数据类型自动选择最佳预处理方法和嵌入策略，减少了人工调优的工作量。
*   **可解释性增强**：提供内置的可解释性工具（如 SHAP 值、注意力权重可视化），帮助理解模型决策依据，符合数据-centric 的开发理念。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11723 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9115 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8908 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8377 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6178 | 🍴 722 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81429 | 🍴 15243 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72464 | 🍴 8862 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48438 | 🍴 10046 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并提取了Anthropic（Claude系列）、OpenAI（ChatGPT及Codex）、Google（Gemini系列）以及xAI（Grok等）等多个主流大模型的系统提示词（System Prompts）。内容涵盖Claude Code、Cursor、VS Code等具体应用或模型的底层指令，并定期更新以反映最新变化。

2. **核心功能**
*   整合多家头部AI厂商及知名开发工具的系统提示词资源。
*   提供经过提取和整理的原始系统指令文本。
*   保持内容的定期更新，确保信息的时效性。
*   覆盖从基础聊天机器人到代码助手等多种模型变体。

3. **适用场景**
*   **提示词工程学习**：通过研究官方系统提示词，深入理解大模型的指令遵循机制。
*   **安全与红队测试**：分析系统指令结构，用于评估模型的安全边界或进行对抗性测试。
*   **自定义代理开发**：参考现有优秀系统的Prompt设计，优化自建AI Agent的行为逻辑。

4. **技术亮点**
*   跨平台数据聚合，集中展示多个竞争性AI产品的底层配置。
*   高频更新机制，紧跟前沿模型迭代带来的指令变化。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 45748 | 🍴 7516 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42348 | 🍴 11542 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36198 | 🍴 5937 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34841 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33696 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28164 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25705 | 🍴 2881 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个带代码的AI项目集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它通过提供丰富的实战案例，帮助开发者快速掌握相关技术的实际应用。

2. **核心功能**
*   提供海量（500+）完整的AI项目代码示例。
*   覆盖机器学习、深度学习及NLP等主流AI技术栈。
*   专注于计算机视觉领域的具体问题解决与实现。
*   整合了多个热门子领域，形成一站式学习资源库。

3. **适用场景**
*   AI初学者希望寻找大量实战项目以巩固理论基础。
*   研究人员或工程师需要快速参考特定算法的实现代码。
*   团队在进行技术选型或原型开发时寻找灵感与模板。

4. **技术亮点**
*   极高的星标数（34,841+），证明其社区认可度和资源价值巨大。
*   标签涵盖全面，精准匹配人工智能领域的核心关键词。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34841 | 🍴 7289 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 21998 | 🍴 2054 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量控制及团队协作，旨在助力计算机视觉人工智能的发展。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注。
*   集成AI辅助标签功能，显著提升标注效率与准确性。
*   提供完善的质量保证机制与团队协同工作能力。
*   开放开发者API，便于集成至现有工作流或进行二次开发。
*   提供丰富的数据分析工具及多种部署模式（开源/云/企业）。

3. **适用场景**
*   需要大规模构建图像分类或目标检测数据集的研发团队。
*   涉及自动驾驶、机器人视觉等需处理视频序列或3D场景的项目。
*   对数据标注质量有严格要求且需要多人协作审核的企业级应用。
*   希望利用AI加速标注流程以缩短模型训练周期的深度学习项目。

4. **技术亮点**
*   兼容 PyTorch 和 TensorFlow 等主流深度学习框架的数据集格式。
*   涵盖语义分割、边界框、对象检测等多种精细化的标注类型。
*   支持从 ImageNet 等标准数据集导入数据，方便基准测试与研究。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16134 | 🍴 3718 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12887 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个基于 PyTorch 的几何计算机视觉库，专为空间人工智能（Spatial AI）设计。它提供了可微分的图像处理和几何算法，旨在简化深度学习中的视觉任务开发。该项目致力于在保持高性能的同时，提升计算机视觉模型的灵活性与集成度。

2. **核心功能**
- 提供基于 PyTorch 的可微分图像处理原语，支持端到端的深度学习训练。
- 包含丰富的几何计算机视觉算法，如相机校准、立体匹配和单应性变换。
- 无缝集成深度学习框架，允许直接在神经网络中嵌入传统 CV 操作。
- 支持机器人学和空间 AI 应用，提供用于 3D 感知和定位的工具集。
- 拥有活跃的社区贡献和持续的标签更新（如 Hacktoberfest），确保代码质量与扩展性。

3. **适用场景**
- 自动驾驶系统中的实时视觉感知与车道线检测。
- 机器人导航中的 SLAM（同步定位与地图构建）及空间理解。
- 医疗影像分析中的图像预处理与特征提取。
- 增强现实（AR）应用中的图像配准与三维重建。

4. **技术亮点**
- **可微分设计**：所有算法均通过 GPU 加速并支持自动微分，便于与神经网络联合优化。
- **PyTorch 原生集成**：作为 PyTorch 生态的一部分，无需额外依赖即可直接使用张量操作。
- **高性能计算**：针对 GPU 优化的 CUDA 内核实现，显著提升大规模数据处理效率。
- 链接: https://github.com/kornia/kornia
- ⭐ 11247 | 🍴 1190 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3451 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3251 | 🍴 397 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2617 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2411 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款跨操作系统和平台的个人 AI 助手，强调用户对自己数据的完全掌控权。它以“龙虾方式”（The lobster way）为特色，旨在提供一种灵活且私密的智能辅助体验。

**2. 核心功能**
*   **全平台兼容**：支持任意操作系统和平台部署，打破硬件限制。
*   **数据私有化**：确保用户拥有并控制自己的数据，保障隐私安全。
*   **个性化 AI 助手**：提供类似个人的智能助理服务，响应日常需求。
*   **开源与可扩展**：基于 TypeScript 构建，社区活跃，便于定制开发。

**3. 适用场景**
*   **注重隐私的个人用户**：希望在不泄露数据的前提下使用 AI 进行日常辅助。
*   **开发者与技术爱好者**：喜欢折腾开源项目，需要在本地或私有服务器上部署 AI 助手。
*   **跨设备办公人群**：需要在不同操作系统（如 Linux、Windows、macOS）间无缝切换 AI 工作流的用户。

**4. 技术亮点**
*   **TypeScript 生态**：利用 TypeScript 的类型安全和现代 JS 生态优势，提升代码可维护性。
*   **去中心化架构理念**：通过“Own-your-data”标签体现其不依赖中心化云端服务的架构设计。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380310 | 🍴 79664 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它通过“子代理驱动开发”模式，将人工智能深度整合到软件开发生命周期中，旨在提升开发效率并优化代码质量。该项目不仅提供了工具支持，更提供了一套完整的 AI 辅助编程工作流。

2. **核心功能**
- 提供模块化的智能体技能库，支持代码生成、调试及架构设计。
- 采用子代理驱动开发模式，将复杂任务分解并由多个 AI 代理协同完成。
- 集成大脑（Obra）作为核心协调组件，管理上下文并优化决策流程。
- 覆盖从头脑风暴到部署的全生命周期（SDLC），实现端到端的自动化辅助。
- 支持 Shell 脚本环境，便于快速集成到现有的 Linux/Unix 开发流程中。

3. **适用场景**
- 希望利用 AI 代理自动化执行重复性编码和测试任务的研发团队。
- 需要结构化方法论来指导大型软件项目中多智能体协作的开发人员。
- 寻求提升需求分析与系统设计阶段效率，利用 AI 进行头脑风暴的产品团队。
- 正在探索或实施“子代理驱动开发”等前沿 AI 软件工程实践的技术专家。

4. **技术亮点**
- 创新性地将“技能框架”与“开发方法论”结合，不仅提供工具，更提供最佳实践。
- 基于 Obra 核心架构，实现了高度上下文感知的智能体交互与管理。
- 拥有极高的社区关注度（近 24 万星标），证明了其在 AI 辅助编程领域的广泛影响力。
- 链接: https://github.com/obra/superpowers
- ⭐ 237814 | 🍴 21099 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. **中文简介**
Hermes-Agent 是一个能够伴随用户共同成长并适应其工作流的智能代理。它旨在通过深度集成多种大型语言模型（如 Claude、ChatGPT 等），提供灵活且强大的 AI 辅助能力。该项目致力于打造一个随用户需求进化的智能助手生态。

### 2. **核心功能**
*   **多模型兼容支持**：无缝整合 OpenAI、Anthropic 等多个主流大语言模型，提供统一的交互接口。
*   **自适应成长机制**：具备学习用户偏好和工作习惯的能力，随着使用时间的推移优化其行为模式。
*   **智能代码与任务处理**：利用先进的 LLM 能力，辅助代码编写、调试及复杂任务的自动化执行。
*   **开源社区驱动**：由 Nous Research 等知名机构参与维护，拥有活跃的社区支持和持续的功能迭代。

### 3. **适用场景**
*   **开发者编程辅助**：作为智能编码助手，帮助程序员快速生成代码片段、审查逻辑错误及重构代码。
*   **个性化 AI 助理**：用于日常办公场景，根据用户习惯自动整理信息、撰写文档或管理日程。
*   **LLM 应用原型开发**：适合研究人员和开发者测试不同大模型在多轮对话和复杂任务中的表现。

### 4. **技术亮点**
*   **架构灵活性**：支持模块化设计，允许用户轻松替换或扩展底层模型及插件功能。
*   **高性能交互**：针对长上下文和多步推理进行了优化，提升了与大型语言模型交互的效率和准确性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 202084 | 🍴 36123 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个支持公平代码许可的工作流自动化平台，具备原生 AI 能力，允许用户结合可视化构建与自定义代码进行开发。该平台支持 400 多种集成，既可自托管也可使用云端服务，旨在提供灵活高效的自动化解决方案。

2. **核心功能**
*   提供可视化工作流构建器，支持拖拽式操作以降低开发门槛。
*   内置原生 AI 功能，可轻松整合大语言模型与智能代理。
*   拥有超过 400 种预置集成，覆盖主流 API 和应用程序。
*   支持混合部署模式，用户可选择自托管或云端服务以保障数据隐私。
*   允许在可视化流程中嵌入自定义代码，满足复杂逻辑需求。

3. **适用场景**
*   企业需要自托管数据，同时希望实现跨系统（如 CRM、ERP）的自动化数据同步。
*   开发者希望快速搭建包含 AI 推理步骤的智能工作流，例如自动处理客户咨询或生成内容。
*   团队希望利用低代码工具连接多个 SaaS 应用，简化日常运维和数据流转任务。

4. **技术亮点**
*   基于 TypeScript 开发，兼具类型安全与高性能。
*   采用公平代码（Fair-code）许可证，平衡了社区贡献与商业使用限制。
*   原生支持 MCP（Model Context Protocol），增强了与 AI 模型交互的标准兼容性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 193943 | 🍴 58813 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建人工智能，实现 AI 的普及化愿景。其使命是提供必要的工具，让用户能够专注于真正重要的核心事务。

2. **核心功能**
*   支持自主代理（Autonomous Agents）模式，能够独立规划并执行复杂任务序列。
*   兼容多种大型语言模型 API，包括 OpenAI、Claude 及 LLaMA 等。
*   提供丰富的开发工具集，帮助用户基于现有框架快速搭建 AI 应用。
*   具备广泛的生态集成能力，可连接互联网、文件系统及其他外部资源。

3. **适用场景**
*   自动化日常办公流程，如信息搜集、数据整理和报告生成。
*   作为开发者的基础框架，用于构建自定义的 AI 智能体应用。
*   探索和研究多步骤逻辑推理及长期记忆管理的 AI 行为模式。

4. **技术亮点**
*   基于 Python 开发，拥有极高的社区活跃度和庞大的开源贡献者群体。
*   高度模块化设计，支持灵活接入不同的 LLM 后端和插件扩展。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185152 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164267 | 🍴 21271 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163871 | 🍴 30363 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156591 | 🍴 46149 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150042 | 🍴 9332 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146474 | 🍴 23043 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

