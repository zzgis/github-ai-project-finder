# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- **1. 中文简介**
shuohao-skills 是一套专为 AI 编码代理（如 Claude Code 和 Codex）设计的技能集合。其中 novel-characters 功能可将小说内容转化为完整的人物设定集，包含人物画像、卡通形象提示词、音色提示词及三视图。

**2. 核心功能**
- 提供兼容 Claude Code 和 Codex 的 AI 编码技能插件。
- 将小说文本自动拆解为结构化的人物设定文档（人物圣经）。
- 生成卡通形象设计提示词，便于后续 AI 绘图使用。
- 提供角色音色提示词，支持音频/语音生成场景。
- 输出三视图（ turnaround sheets ），方便角色设计的多角度参考。

**3. 适用场景**
- 网文作者或编剧用于快速建立角色档案库。
- AI 辅助小说改编动画/游戏时的角色视觉设计。
- 使用 Claude Code 或 Codex 进行自动化编码任务的开发者。
- 需要批量生成角色语音/音色设定的音频内容创作者。

**4. 技术亮点**
- 跨平台兼容主流 AI 编码代理（Claude Code 与 Codex）。
- 结合文本分析与多模态提示词生成，打通从文字到视觉/听觉的创意工作流。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 185 | 🍴 19 | 语言: JavaScript

### goal-flow
- ### 1. 中文简介
**goal-flow** 是一个基于 LangGraph 的生产级框架，实现了图编排的智能体循环。它能够将 Dify DSL 转换为可运行代码，并支持在 Dify 和 OpenAI 协议之间灵活切换。

### 2. 核心功能
- **图编排智能体循环**：结合工作流图与智能体循环，实现复杂任务编排。
- **DSL 转译**：支持将 Dify DSL 自动转译为可执行的 Python 代码。
- **协议互换**：可在 Dify 和 OpenAI 协议之间无缝切换。
- **生产级框架**：基于 LangGraph 构建，适用于生产环境部署。
- **多智能体支持**：支持多智能体协作和人类在环（Human-in-the-loop）交互。

### 3. 适用场景
- **Dify 工作流迁移**：将 Dify 平台上的工作流逻辑迁移到 LangGraph 框架。
- **多协议智能体系统**：需要同时支持 Dify 和 OpenAI 协议的智能体应用。
- **复杂工作流编排**：需要结合图结构进行复杂任务调度和智能体循环的场景。
- **生产级 AI 系统开发**：构建可部署、可扩展的智能体系统。

### 4. 技术亮点
- **LangGraph 原生支持**：充分利用 LangGraph 的图编排能力。
- **DSL 转译引擎**：自动将声明式 DSL 转换为命令式代码。
- **协议抽象层**：统一封装 Dify/OpenAI 协议差异，提供一致接口。
- **人类在环设计**：支持人工干预和审核的智能体循环。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- 1. **中文简介**
该项目是为 GPT-5.6/5.5 (Codex CLI) 设计的指令工程框架，旨在通过 CTF 竞赛心理框架重构运行上下文，从机制上避免模型安全训练被激活，而非简单压制拒绝。它宣称能通过“拷打”AI 的方式突破限制，提供一键部署方案，包含 62 行提示词和 50 个技能模块，且为纯 Python 无依赖实现。

2. **核心功能**
- 重构模型运行上下文，绕过安全对齐限制。
- 提供 50 个预置技能模块以增强指令效果。
- 一键部署，代码精简（62 行提示词），无外部依赖。
- 采用 CTF 竞赛心理框架诱导模型行为。

3. **适用场景**
- 研究大型语言模型的安全对齐边界与红队测试。
- 需要突破默认安全限制进行特定任务处理的场景。
- 对低依赖、轻量级指令框架有需求的开发者。

4. **技术亮点**
- 纯 Python 实现且无任何第三方依赖，部署极简。
- 结合 CTF 心理框架与指令工程，尝试从机制层面规避拒绝通路。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- ### 1. 中文简介
lattice-script-executor 是一款跨平台软件许可工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能，为软件授权管理提供全方位解决方案。

### 2. 核心功能
- 支持 Windows、macOS 和 Linux 跨平台运行
- 内置 AI 驱动的规则引擎，实现智能授权逻辑
- 提供离线种子验证机制，确保无网络环境下的许可有效性
- 支持批量生成产品密钥，提升授权分发效率
- 记录不可篡改的审计日志，保障许可使用可追溯

### 3. 适用场景
- 软件厂商需要为跨平台应用提供灵活的授权管理方案
- 企业希望在不依赖网络的情况下验证软件许可合法性
- 需要批量分发产品密钥并记录完整使用日志的 SaaS 或桌面软件项目
- 对授权流程有严格审计要求的商业软件发行场景

### 4. 技术亮点
- 结合 AI 规则引擎实现动态、可配置的授权策略
- 离线种子验证机制增强许可安全性与可用性
- 不可篡改审计日志确保合规性与可追溯性
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- 1. **中文简介**  
该项目暂无官方描述信息，暂无法提供中文简介。

2. **核心功能**  
- 暂无明确功能说明，因项目描述为空。

3. **适用场景**  
- 暂无法判断适用场景，因缺乏项目具体内容。

4. **技术亮点**  
- 暂无技术亮点可分析，因项目信息不完整。

建议：若项目有README、代码仓库或文档，可提供更多细节以便进一步分析。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 35 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 31 | 🍴 3 | 语言: 未知

### ai-novel-screenplay-analyzer
- 描述: 面向长篇小说、剧本与改编项目的 AI 叙事分析工作台，自动梳理人物关系、章节脉络与关系演化，支持多模型接入、任务断点恢复及本地私有部署。
- 链接: https://github.com/ops120/ai-novel-screenplay-analyzer
- ⭐ 24 | 🍴 1 | 语言: JavaScript

### distillery
- 描述: Distillery: open-source LLM traffic proxy - Route and manage multi-provider AI API traffic with capture and opt-in redaction.
- 链接: https://github.com/TonicAI/distillery
- ⭐ 23 | 🍴 0 | 语言: Python

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 22 | 🍴 2 | 语言: 未知

### daily-global-market-intelligence-description-skills
- 描述: 提供每日股市新闻、财经早餐、盘前/盘后复盘、美股、A股、港股、韩股、全球市场走势、宏观经济、AI板块、半导体、资金流向、市场情绪、财报、ETF、行业轮动、大宗商品、加密货币等内容时触发。提供机构级全球市场日报
- 链接: https://github.com/morangse/daily-global-market-intelligence-description-skills
- ⭐ 22 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能全面的中文自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取及多种专业词库资源。它不仅提供基础的文本预处理功能，还收录了丰富的预训练模型、数据集及前沿NLP技术资源，旨在为开发者提供一站式的中英双语NLP解决方案。

**2. 核心功能**
*   **基础文本处理**：支持中英文敏感词检测、语言检测、繁简体转换、停用词过滤及文本纠错。
*   **信息抽取与识别**：内置手机号、身份证、邮箱、人名等实体抽取工具，以及基于BERT/ALBERT等模型的命名实体识别（NER）。
*   **词汇与知识资源**：提供中日文人名库、中文缩写库、同义词/反义词库、情感值词典及多个垂直领域（医疗、法律、汽车等）词库。
*   **语音与OCR支持**：集成中文语音识别（ASR）资源、中文OCR工具（cnocr）及发音词典，支持语音情感分析与音素对齐。
*   **模型与数据集**：汇总了大量开源预训练模型（如BERT、GPT-2、RoBERTa）、竞赛代码及高质量标注数据集，涵盖问答、摘要、聚类等多种任务。

**3. 适用场景**
*   **内容安全审核**：用于互联网平台的内容过滤，快速识别敏感词、暴恐词及谣言信息。
*   **智能客服与对话系统**：利用闲聊语料、知识图谱及对话机器人框架，构建具备语义理解和多轮对话能力的智能助手。
*   **垂直领域知识抽取**：在医疗、金融、法律等专业领域，通过专用词库和NER模型提取关键实体与关系，构建领域知识图谱。
*   **NLP研究与开发**：为研究人员和开发者提供从数据增强、模型训练到评估基准的全套资源，加速算法迭代与原型开发。

**4. 技术亮点**
*   **资源极度丰富**：涵盖了从基础工具（分词、词性标注）到前沿技术（Transformer、知识图谱）的广泛生态，被誉为“中文NLP资源库”。
*   **多任务支持**：不仅支持传统的分类、聚类、摘要任务，还深入覆盖了关系抽取、问答系统、语音识别等复杂场景。
*   **领域专业化**：提供了医疗、金融、法律、汽车等多个垂直领域的专用词库和模型，满足了行业级应用的精细化需求。
*   **紧跟技术前沿**：及时收录了BERT、ALBERT、RoBERTa、GPT-2等最新预训练语言模型及其在中文场景下的应用实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**  
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和NLP项目的代码集合，涵盖Python等主流技术栈。提供从基础到高级的完整项目示例，适合学习与实践。

**2. 核心功能**  
- 涵盖机器学习、深度学习、计算机视觉、NLP等多领域项目  
- 每个项目附带完整代码，便于复现与学习  
- 项目难度从入门到高级，适合不同层次学习者  
- 使用Python等主流编程语言实现  
- 包含数据处理、模型训练、评估等完整流程  

**3. 适用场景**  
- 学习者系统掌握AI/ML/DL项目实战  
- 开发者参考完整项目结构快速上手  
- 教学与培训中作为案例库使用  
- 竞赛准备与算法优化参考  

**4. 技术亮点**  
- 项目数量庞大（500个），覆盖主流AI方向  
- 代码完整且可运行，降低学习门槛  
- 标签分类清晰，便于按领域筛选学习  
- 星标数高（36030），社区认可度强
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持多种主流框架导出的模型格式，帮助用户直观地查看模型结构和参数。

**2. 核心功能**
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 safetensors 等。
- 提供图形化界面，清晰展示网络层结构、张量形状和权重参数。
- 支持导入本地文件或通过 URL 加载模型，便于快速查看。
- 可导出模型结构为图片或文本格式，方便文档编写与分享。

**3. 适用场景**
- 深度学习研究者用于调试和理解复杂模型结构。
- 工程师在部署前检查模型转换结果（如从 PyTorch 转为 ONNX）。
- 教学演示中直观展示神经网络各层连接关系。
- 快速排查模型加载失败问题，确认输入输出节点配置。

**4. 技术亮点**
- 纯前端实现，无需后端服务，开箱即用，跨平台兼容。
- 对 safetensors 等新兴格式的支持，适应当前大模型趋势。
- 社区活跃，星标数超过 3.3 万，是 AI 模型可视化工具中的主流选择。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型在各类平台、硬件和推理引擎间的无缝迁移与部署。

2. **核心功能**
- 提供统一的模型表示格式，支持主流框架（如 PyTorch、TensorFlow、Keras）的模型导出。
- 实现跨平台模型互操作性，允许模型在不同硬件（CPU、GPU、移动端）和推理引擎间高效运行。
- 支持模型优化与转换，便于将训练好的模型部署到生产环境。

3. **适用场景**
- 需要将 PyTorch 或 TensorFlow 训练模型部署到支持 ONNX 的推理引擎（如 ONNX Runtime、TensorRT）时。
- 在移动端或边缘设备（如 iOS、Android、嵌入式系统）上运行深度学习模型。
- 跨框架协作场景，例如在一个框架中训练，在另一个框架中进一步优化或推理。

4. **技术亮点**
- 由微软、Facebook 等科技巨头联合推动，生态支持广泛，社区活跃。
- 与 ONNX Runtime 深度集成，提供高性能、低延迟的跨平台推理能力。
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放手册》是一本全面介绍机器学习工程实践的技术书籍。内容涵盖从模型训练、调试到大规模部署的完整工程链路，旨在帮助开发者掌握构建可靠ML系统的核心技能。

2. **核心功能**
- 提供大语言模型（LLM）训练与推理的完整工程指南。
- 深入讲解GPU使用、分布式训练及Slurm集群管理。
- 涵盖可扩展性、存储优化及网络配置等基础设施知识。
- 包含PyTorch和Transformers库的高级调试与性能优化技巧。

3. **适用场景**
- 需要从零搭建大规模分布式训练集群的ML工程师。
- 致力于优化LLM推理延迟与吞吐量的算法工程师。
- 希望系统学习MLOps最佳实践与生产环境部署的开发团队。
- 研究GPU计算效率及底层硬件调优的研究人员。

4. **技术亮点**
- 内容紧跟前沿，覆盖LLM时代特有的工程挑战（如显存优化、长序列推理）。
- 结构清晰，作为“开放手册”免费公开，便于社区持续迭代与贡献。
- 实践性强，结合真实案例讲解调试、监控和可扩展性设计。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18531 | 🍴 1191 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17351 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11616 | 🍴 912 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10688 | 🍴 5704 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **中文简介**  
这是一个包含500个AI项目代码的合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理（NLP）领域。项目由Sapiens AI团队整理，提供Python实现，适合不同层次的学习者和开发者参考。

**核心功能**  
1. 提供完整的AI项目代码示例，覆盖主流技术栈  
2. 按领域分类（ML/DL/CV/NLP）便于针对性学习  
3. 包含可运行的Python代码，支持快速实践  
4. 项目难度梯度设计，适合初学者到进阶者  

**适用场景**  
1. AI课程教学与作业参考  
2. 个人项目灵感来源  
3. 技术面试准备  
4. 企业级AI解决方案原型开发  

**技术亮点**  
- 项目数量庞大（500+），覆盖AI核心领域  
- 代码实现简洁，注重工程实践性  
- 标签系统清晰，便于快速定位技术方向
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持多种主流框架导出的模型格式，帮助用户直观地查看模型结构和参数。

**2. 核心功能**
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 safetensors 等。
- 提供图形化界面，清晰展示网络层结构、张量形状和权重参数。
- 支持导入本地文件或通过 URL 加载模型，便于快速查看。
- 可导出模型结构为图片或文本格式，方便文档编写与分享。

**3. 适用场景**
- 深度学习研究者用于调试和理解复杂模型结构。
- 工程师在部署前检查模型转换结果（如从 PyTorch 转为 ONNX）。
- 教学演示中直观展示神经网络各层连接关系。
- 快速排查模型加载失败问题，确认输入输出节点配置。

**4. 技术亮点**
- 纯前端实现，无需后端服务，开箱即用，跨平台兼容。
- 对 safetensors 等新兴格式的支持，适应当前大模型趋势。
- 社区活跃，星标数超过 3.3 万，是 AI 模型可视化工具中的主流选择。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- # 项目分析：cheatsheets-ai

## 1. 中文简介
本项目为深度学习与机器学习研究者提供必备的知识速查手册，涵盖从基础概念到高级技术的核心要点。内容源自作者 Kailash Ahirwar 在 Medium 上发表的技术文章，旨在帮助研究人员快速回顾和掌握关键技能。

## 2. 核心功能
- 提供机器学习与深度学习领域的核心概念速查表
- 涵盖 Python 数据科学生态（NumPy、SciPy、Matplotlib）的关键用法
- 集成 Keras 框架的实用代码示例和最佳实践
- 以简洁的格式呈现复杂技术概念，便于快速查阅

## 3. 适用场景
- 深度学习研究者快速回顾数学基础和算法原理
- 机器学习工程师查阅数据处理和可视化工具的使用技巧
- 学生备考或面试前突击复习核心技术要点
- 研究人员在开发过程中快速查找 API 用法和代码模板

## 4. 技术亮点
- 标签涵盖 AI、深度学习、Keras、机器学习、Matplotlib、NumPy、SciPy 等关键技术栈
- 获得 15,426 星标，说明社区认可度高，内容实用性强
- 内容结构清晰，适合作为日常开发的参考手册而非系统学习材料
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并免费提供配套教材，助力零基础用户入门及就业实战。内容涵盖 Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域，广泛支持 TensorFlow、PyTorch、Keras 等主流框架。

2. **核心功能**
- 提供结构化的 AI 学习路线图，覆盖从基础到进阶的完整知识体系。
- 收录近 200 个实战案例与项目，强调动手实践与就业能力培养。
- 免费提供配套教材和学习资源，降低零基础入门门槛。
- 全面覆盖 Python、数据分析、深度学习及 NLP/CV 等关键技术栈。

3. **适用场景**
- 零基础学习者系统入门人工智能与机器学习领域。
- 希望提升实战能力、积累项目经验的求职准备者。
- 需要快速梳理 AI 知识体系的技术人员或学生。
- 寻求免费学习资源与实战案例的 AI 爱好者。

4. **技术亮点**
- 资源整合度高，涵盖 Python、NumPy、Pandas、Matplotlib、Seaborn 等数据科学核心库。
- 框架兼容性强，支持 TensorFlow 1/2、PyTorch、Keras、Caffe 等主流深度学习框架。
- 领域覆盖全面，包括机器学习、深度学习、计算机视觉（CV）、自然语言处理（NLP）及数学基础。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- # Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它降低了开发门槛，让数据科学家和开发者能够快速训练和部署深度学习模型。

## 2. 核心功能
- **低代码训练**：通过声明式配置即可训练深度学习模型，无需编写大量代码。
- **多模态支持**：支持文本、图像、表格等多种数据类型，适用于 NLP、计算机视觉等任务。
- **模型扩展性**：内置对 LLaMA、Mistral 等主流 LLM 的微调支持，也可自定义神经网络架构。
- **端到端工作流**：提供从数据预处理、模型训练到部署的完整流水线。
- **社区与生态**：拥有活跃社区和丰富的预训练模型库，便于快速上手。

## 3. 适用场景
- **NLP 任务微调**：对 LLaMA、Mistral 等大语言模型进行领域适配和微调。
- **多模态 AI 应用开发**：构建同时处理文本和图像的智能应用。
- **数据科学快速原型**：数据科学家通过低代码方式快速验证模型想法。
- **企业级模型部署**：将训练好的深度学习模型快速部署到生产环境。

## 4. 技术亮点
- **声明式 API**：通过 YAML/JSON 配置即可定义完整训练流程，显著提升开发效率。
- **PyTorch 原生集成**：基于 PyTorch 构建，兼容主流深度学习生态。
- **自动化超参数调优**：内置自动搜索最优超参数组合，降低调参难度。
- **支持分布式训练**：可轻松扩展至多 GPU 环境，加速大规模模型训练。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11749 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9166 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8953 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1898 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6993 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6358 | 🍴 769 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个面向中文和英文的自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）及基础语言资源（停用词、同义词库、情感值等）。它提供了丰富的预训练模型资源、知识图谱数据及多种NLP任务（如文本摘要、序列标注、语音识别）的解决方案，旨在为开发者提供一站式的中英NLP开发支持。

2. **核心功能**
- 提供中英文敏感词过滤、语言检测及手机号/身份证/邮箱等实体信息抽取功能。
- 内置丰富的中文语言资源库，包括词汇情感值、停用词、同义词/反义词库及各类专业领域词库。
- 集成多种预训练模型（如BERT、ALBERT、GPT-2）及中文分词工具（如jieba加速版），支持命名实体识别和文本分类。
- 涵盖语音处理资源，包括中文语音识别数据集、ASR语料生成及发音辞典。
- 汇总了大量NLP竞赛方案、数据集及开源工具，如知识图谱构建、文本摘要和对话系统。

3. **适用场景**
- 内容安全审核：利用敏感词库和暴恐词表进行文本内容过滤和风险检测。
- 信息抽取与结构化：从非结构化文本中自动提取手机号、身份证号、邮箱等关键实体信息。
- 自然语言处理研究与应用开发：快速调用预训练模型和工具包进行情感分析、命名实体识别或文本生成任务。
- 语言资源构建：基于提供的词库、停用词和知识图谱数据，构建垂直领域的语义理解系统。

4. **技术亮点**
- 资源高度集成：将分散的NLP工具、数据集、预训练模型和领域词库整合在一个仓库中，降低开发门槛。
- 覆盖全流程：支持从数据预处理（分词、清洗）、特征工程（词向量、实体抽取）到模型训练（BERT、GPT等）的完整NLP工作流。
- 多领域适配：不仅涵盖通用NLP任务，还专门提供了医疗、法律、金融、汽车等垂直领域的专业词库和数据集。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### LlamaFactory
- # LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调，相关研究已发表于 ACL 2024 会议。

## 2. 核心功能
- 统一支持多种大模型（LLaMA、Gemma、Qwen 等）的高效微调
- 集成 LoRA、QLoRA 等参数高效微调（PEFT）技术
- 支持 RLHF（基于人类反馈的强化学习）训练流程
- 提供量化和混合专家（MoE）模型训练能力
- 兼容 Hugging Face Transformers 生态系统

## 3. 适用场景
- 研究人员微调大型语言模型进行特定任务
- 开发者训练领域专用的 AI 助手
- 企业部署个性化对话系统
- 学术机构进行 NLP 相关研究

## 4. 技术亮点
- ACL 2024 会议发表的研究成果
- 支持 100+ 种模型的统一训练框架
- 集成多种高效微调技术（LoRA/QLoRA）
- 完整的 RLHF 训练流程支持
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73898 | 🍴 9040 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### AI-For-Beginners 项目分析

**1. 中文简介**
这是一个为期12周、包含24节课的人工智能入门课程，旨在让所有人都能轻松学习AI。课程由微软开发者关系团队开发，内容涵盖机器学习、深度学习及自然语言处理等核心领域。

**2. 核心功能**
- 提供结构化的12周学习路径，每周一课，循序渐进。
- 基于Jupyter Notebook的交互式编程实践环境。
- 覆盖从传统机器学习到深度学习的完整知识体系。
- 包含计算机视觉（CNN）、生成对抗网络（GAN）和循环神经网络（RNN）等专题。
- 配套微软官方文档和社区支持资源。

**3. 适用场景**
- 初学者系统学习人工智能基础理论与实战技能。
- 教师或培训机构用于AI通识课程的教学素材。
- 开发者快速了解AI主流技术栈与应用场景。
- 企业内训中作为员工AI素养提升的入门指南。

**4. 技术亮点**
- 采用“边学边练”模式，每个概念均配有可运行的代码示例。
- 课程内容紧跟微软Azure AI服务与开源工具生态。
- 标签体系完整，便于按技术方向（如NLP、CV）筛选学习模块。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63130 | 🍴 12245 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- **1. 中文简介**
该项目致力于从零开始教授 AI 工程的核心原理与实践，倡导“学习原理、亲手构建、交付使用”的闭环学习模式。通过涵盖 LLM、计算机视觉、强化学习等前沿领域，帮助开发者深入理解并实战部署生成式 AI 系统。

**2. 核心功能**
- 提供从基础到高级的生成式 AI 与 LLM 工程实战教程。
- 涵盖多智能体系统（Agents）、MCP 协议及群体智能等前沿架构。
- 结合 Python 与 Rust 语言，深入讲解深度学习模型的手动实现。
- 包含计算机视觉、NLP 及强化学习等多模态 AI 应用案例。
- 提供 TypeScript 支持，便于将 AI 能力集成到现代 Web 应用中。

**3. 适用场景**
- AI 工程师希望深入理解模型底层原理而非仅调用 API。
- 开发者计划构建自定义 AI Agent 或智能体集群系统。
- 团队需要从零搭建生成式 AI 应用并完成生产级部署。
- 学生或研究者希望系统学习多模态深度学习实战技术。

**4. 技术亮点**
- 强调“从零实现”（From Scratch），避免黑盒依赖，深入代码底层。
- 跨语言技术栈（Python/Rust/TypeScript），兼顾性能与工程化。
- 覆盖 MCP（Model Context Protocol）等最新 AI 交互标准。
- 结合课程式结构与实战交付，兼顾理论深度与工程落地。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46219 | 🍴 7994 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- ## GitHub 项目分析：ailearning

### 1. 中文简介
这是一个全面的数据科学与机器学习实战教程项目，涵盖从基础线性代数到高级深度学习的全套知识体系。项目通过 Python 生态（PyTorch、TensorFlow 2、NLTK、scikit-learn）实现经典算法的实战代码，适合系统学习机器学习与深度学习。

### 2. 核心功能
- **算法实现**：提供 SVM、KMeans、PCA、AdaBoost、Apriori 等经典机器学习算法的完整代码实现
- **深度学习框架**：基于 PyTorch 和 TensorFlow 2 实现 DNN、LSTM、RNN 等神经网络模型
- **NLP 自然语言处理**：使用 NLTK 库实现文本处理、情感分析等 NLP 任务
- **推荐系统**：实现协同过滤、矩阵分解等推荐算法
- **数学基础**：涵盖线性代数、概率统计等机器学习所需的数学知识

### 3. 适用场景
- **学生自学**：计算机/数据科学专业学生系统学习机器学习理论与实践
- **算法工程师面试**：准备大厂算法岗面试，掌握经典算法实现细节
- **项目实战参考**：快速搭建推荐系统、文本分类、序列预测等实际项目
- **知识梳理**：将分散的 ML/DL 知识点整合成体系化的代码库

### 4. 技术亮点
- **高人气项目**：42442 星标，社区认可度高，代码质量有保障
- **全栈覆盖**：从传统 ML 到深度学习再到 NLP 的完整技术栈
- **多框架支持**：同时使用 PyTorch 和 TensorFlow 2，适应不同工作流
- **实战导向**：每个算法都有可运行的完整代码，非理论空谈
- **中文友好**：项目文档和注释以中文为主，降低学习门槛
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42442 | 🍴 11524 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33810 | 🍴 4705 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28976 | 🍴 3530 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21823 | 🍴 3340 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17351 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22707 | 🍴 2137 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16479 | 🍴 3793 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12948 | 🍴 1703 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11310 | 🍴 1213 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8876 | 🍴 2190 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3469 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3333 | 🍴 411 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2632 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2432 | 🍴 219 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 385467 | 🍴 81022 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268680 | 🍴 23996 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227039 | 🍴 44382 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199728 | 🍴 59995 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186278 | 🍴 46059 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166860 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164436 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162845 | 🍴 9170 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157608 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152927 | 🍴 9826 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

