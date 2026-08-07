# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- ### 1. 中文简介
shuohao-skills 是一个专为 AI 编码 Agent（支持 Claude Code 和 Codex）设计的技能集合项目。其中包含 novel-characters 模块，可将小说内容自动拆解为完整的人物设定集，涵盖人物画像、卡通形象提示词、音色描述及三视图设计。

### 2. 核心功能
- **跨平台兼容**：技能包同时适配 Claude Code 和 Codex 两大主流 AI 编码 Agent。
- **小说角色拆解**：自动将小说文本解析并转化为结构化的人物设定文档。
- **多维度角色设计**：生成包括人物画像、卡通形象提示词、音色提示词在内的全套角色资料。
- **三视图输出**：提供角色三视图（Turnaround sheets）的设计提示，便于视觉化呈现。
- **JavaScript 实现**：基于 JavaScript 开发，便于集成和扩展。

### 3. 适用场景
- AI 辅助小说创作：帮助作者快速建立统一、详细的人物设定库。
- 游戏或动漫角色设计：为独立开发者或创作者生成角色视觉与声音设计的初始提示。
- 多 Agent 协作开发：在 Claude Code 或 Codex 工作流中复用标准化角色设计技能。
- 内容 IP 衍生开发：将文字 IP 快速转化为可视化的角色资产基础。

### 4. 技术亮点
- **双 Agent 兼容架构**：同时支持 OpenAI Codex 和 Anthropic Claude Code，提升技能复用性。
- **端到端角色生成**：从文本输入到视觉/听觉提示词输出的一站式处理流程。
- **提示词工程集成**：将创意写作需求转化为高质量的 AI 可执行提示词（Prompt）。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 183 | 🍴 19 | 语言: JavaScript

### goal-flow
- 1. **中文简介**
这是一个基于 LangGraph 的生产级 Graph-Orchestrated Agent Loop 框架。它将工作流图与智能体循环相结合，支持将 Dify DSL 转译为可运行代码，并实现 Dify 与 OpenAI 协议之间的无缝切换。

2. **核心功能**
- 基于 LangGraph 构建生产级智能体编排循环。
- 支持将 Dify DSL 转译为可执行的 Python 代码。
- 实现 Dify 与 OpenAI 协议之间的灵活互换。
- 融合工作流图与多智能体循环机制。

3. **适用场景**
- 需要将 Dify 可视化工作流迁移至 LangGraph 生产环境。
- 构建支持人机协作（Human-in-the-loop）的复杂智能体系统。
- 开发需兼容多种 LLM 协议（Dify/OpenAI）的 AI 应用。

4. **技术亮点**
- 提供从声明式 DSL 到可执行代码的自动转译能力。
- 支持协议层抽象，实现不同 AI 平台间的互操作性。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- 1. **中文简介**
该项目是针对 GPT-5.6/5.5 (Codex CLI) 的指令工程框架，旨在通过 CTF 竞赛心理框架重构运行上下文，从而规避模型的安全训练限制。它采用“让拒绝通路不发生”而非强行打压拒绝的策略，提供一键部署能力，包含 62 行提示词和 50 个技能模块，且纯 Python 无外部依赖。

2. **核心功能**
- 重构模型运行上下文，利用 CTF 竞赛心理框架绕过安全对齐机制。
- 提供 50 个技能模块，增强模型在特定任务中的执行能力。
- 一键部署，仅需 62 行提示词，实现纯 Python 环境无依赖运行。
- 通过语境重构而非对抗性提示来抑制模型的拒绝行为。

3. **适用场景**
- 需要在 Codex CLI 环境下最大化模型输出自由度的高级指令工程实验。
- 希望在不修改模型权重的前提下，通过提示词技巧绕过安全过滤的研究场景。
- 追求轻量级、无依赖部署的快速原型开发或自动化任务执行。

4. **技术亮点**
- 采用“上下文重构”而非传统越狱技巧，策略更为隐蔽和系统化。
- 极简部署方案：纯 Python 实现，零外部依赖，便于快速集成和测试。
- 模块化技能设计：50 个技能模块可灵活组合，适应不同任务需求。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- **1. 中文简介**
lattice-script-executor 是一款跨平台软件授权工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成及不可篡改的审计日志功能，专为软件授权管理设计。

**2. 核心功能**
- 跨平台支持：兼容 Windows、macOS 和 Linux 三大主流操作系统。
- AI 规则引擎：利用人工智能驱动动态授权规则判断。
- 离线种子验证：支持无需网络连接的环境下的许可证验证。
- 批量密钥生成：提供高效的产品密钥批量生成能力。
- 不可篡改审计日志：确保所有授权操作记录安全且无法被修改。

**3. 适用场景**
- 软件开发商需要对多平台应用进行统一的授权管理。
- 企业级软件需要离线激活场景下的许可证验证机制。
- 需要生成大量产品密钥用于销售或分发场景。
- 对授权操作有严格合规要求，需保留完整审计痕迹的项目。

**4. 技术亮点**
- AI 驱动规则引擎：区别于传统静态规则，可实现更智能的动态授权判断。
- 离线种子验证：解决了网络受限环境下的授权难题。
- 不可篡改审计日志：结合区块链或哈希链技术，保障操作记录的完整性和可信度。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- **中文简介**
该项目在GitHub上的信息极为有限，没有提供项目描述、编程语言及标签等关键元数据。目前仅有34个星标，表明其关注度较低或处于早期阶段。由于缺乏具体文档，无法确定其实际功能与用途。

**核心功能**
1. 无明确核心功能，因项目描述缺失无法分析。
2. 无已知技术栈，编程语言字段为空。
3. 无分类标签，无法判断项目领域或类型。

**适用场景**
1. 暂不适用任何场景，因项目内容未知。
2. 无法推荐具体使用情境。

**技术亮点**
无技术亮点可提取，项目信息不完整，缺乏代码实现、文档说明或架构细节。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 34 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 30 | 🍴 3 | 语言: 未知

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
- ### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取（手机、身份证、邮箱等）及基础 NLP 功能。它不仅提供词汇资源（如同义词、反义词、情感值、停用词），还收录了大量中文 NLP 数据集、预训练模型及竞赛方案汇总。该项目旨在为开发者提供一个一站式的中英 NLP 资源库，涵盖从基础文本处理到深度学习模型应用的广泛需求。

### 2. 核心功能
- **基础 NLP 工具**：支持中英文敏感词过滤、语言检测、繁简转换、情感分析、分词及命名实体识别。
- **实体与信息抽取**：提供手机号、身份证、邮箱抽取，以及手机归属地/运营商查询和名字推断性别功能。
- **丰富词汇资源库**：内置中日文人名库、中文缩写库、同义词/反义词库、停用词表及各类领域词库（汽车、医学、法律等）。
- **数据集与模型资源**：汇总了大量中文 NLP 数据集（如问答、谣言、对话语料）、预训练模型（BERT、ALBERT 等）及竞赛 Top 方案。
- **语音与 OCR 支持**：包含中文语音识别（ASR）、手写汉字识别（OCR）及语音情感分析相关资源。

### 3. 适用场景
- **内容安全与审核**：利用敏感词库和暴恐词表，快速构建文本过滤和审核系统。
- **信息抽取与结构化**：从非结构化文本中自动提取手机号、身份证、邮箱等关键实体信息。
- **自然语言处理研究**：作为研究人员获取中文 NLP 数据集、基准模型和最新论文资源的聚合平台。
- **智能客服与对话系统**：借助对话语料、知识图谱及问答系统资源，快速搭建聊天机器人。

### 4. 技术亮点
- **资源聚合性强**：不仅是一个工具库，更是中文 NLP 领域的“资源百科”，涵盖了从传统规则方法到最新深度学习模型的全方位资料。
- **领域覆盖广泛**：除了通用 NLP 功能，还特别针对金融、医疗、法律、汽车等专业领域提供了专用词库和模型资源。
- **实用工具集成**：提供了如“汪峰歌词生成器”等趣味工具，以及简历解析、文本纠错、拼音标注等实用功能，兼顾学术与趣味。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它提供了完整的代码实现，适合希望系统学习AI技术并动手实践的开发者。

2. **核心功能**
- 提供500个涵盖AI各主要领域的完整项目代码示例
- 包含机器学习、深度学习、计算机视觉和NLP四大方向
- 所有项目均附带可直接运行的代码实现
- 项目分类清晰，便于按技术领域快速查找

3. **适用场景**
- AI初学者系统学习各技术方向的实践项目
- 开发者寻找特定算法（如CNN、RNN、Transformer）的实现参考
- 面试准备中需要展示实际项目经验的求职者
- 教师或培训人员用于教学案例和作业设计

4. **技术亮点**
该项目作为"awesome list"类型的资源合集，其亮点在于项目数量庞大（500个）、覆盖领域全面，且全部提供可运行的代码，而非仅理论介绍，是实战型学习者的优质资源库。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和调试模型结构。

2. **核心功能**
- 支持 ONNX、TensorFlow、PyTorch、Keras、Core ML、TensorFlow Lite 及 safetensors 等多种模型格式。
- 提供清晰的计算图与层结构可视化，便于理解模型内部逻辑。
- 兼容桌面应用与 Web 浏览器，实现跨平台便捷查看。
- 支持模型权重与张量数据的详细展示与分析。

3. **适用场景**
- 深度学习研究者用于快速检查模型架构是否符合预期。
- 工程师在模型转换（如 PyTorch 转 ONNX）后验证结构完整性。
- 教学与演示中直观展示神经网络的数据流向。
- 调试模型时定位特定层或参数的配置问题。

4. **技术亮点**
- 广泛支持业界主流框架，包括新兴的 safetensors 格式。
- 开源且无需复杂安装，通过浏览器即可直接使用。
- 界面简洁直观，适合不同技术背景的用户快速上手。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### ONNX 项目分析

**1. 中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在帮助开发者在不同深度学习框架之间无缝迁移和部署模型，打破生态壁垒。

**2. 核心功能**
- **模型互操作性**：定义通用算子集和数据格式，支持跨框架模型转换。
- **多框架支持**：原生兼容 PyTorch、TensorFlow、Keras 等主流深度学习框架。
- **部署优化**：提供 ONNX Runtime，支持在 CPU、GPU 及边缘设备上高效推理。
- **工具链生态**：配备模型检查、转换和优化工具，确保模型兼容性与性能。

**3. 适用场景**
- **模型迁移**：将训练好的模型从 PyTorch 或 TensorFlow 转换为统一格式，便于后续部署。
- **跨平台部署**：在移动端、嵌入式设备或云环境中使用 ONNX Runtime 进行高性能推理。
- **模型协作**：在团队中使用不同框架时，通过 ONNX 共享和验证模型结构。
- **生产环境优化**：结合量化、剪枝等工具优化模型，提升推理速度和资源效率。

**4. 技术亮点**
- **开放标准**：由微软、Facebook 等巨头共同维护，避免厂商锁定，促进生态统一。
- **高性能推理**：ONNX Runtime 支持图优化、算子融合及硬件加速，显著提升部署效率。
- **广泛社区支持**：GitHub 星标数超 21,000，拥有活跃的开发者社区和丰富的文档资源。
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**  
《机器学习工程开放书籍》是一本全面介绍机器学习工程实践的开源指南，涵盖从模型训练、调试到部署推理的全流程技术。

2. **核心功能**  
- 系统讲解大规模机器学习工程的核心原理与实践方法  
- 提供GPU使用、网络通信、存储优化等基础设施层面的最佳实践  
- 深入解析LLM训练与推理中的性能调优和可扩展性设计  
- 覆盖PyTorch、Transformers等主流框架的工程化使用技巧  
- 包含Slurm集群管理、分布式训练等大规模部署方案

3. **适用场景**  
- 机器学习工程师构建和优化生产级模型训练流水线  
- 研究人员部署大规模语言模型（LLM）并进行推理优化  
- MLOps团队设计可扩展的GPU集群训练基础设施  
- 工程师调试复杂分布式训练中的性能瓶颈问题

4. **技术亮点**  
项目以开放书籍形式系统整合了LLM时代机器学习工程的关键知识，特别强调实际工程中的可扩展性、调试技巧和基础设施优化，是连接理论研究与工业部署的实用指南。
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
- 1. **中文简介**  
这是一个包含500个AI相关项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目为开发者提供了丰富的实践案例，适合学习和研究。

2. **核心功能**  
- 提供大量AI项目的代码实现，便于学习和参考。  
- 覆盖机器学习、深度学习、计算机视觉和NLP等多个热门领域。  
- 包含完整的项目示例，适合初学者和进阶开发者。  
- 项目标签清晰，方便快速找到感兴趣的内容。  
- 支持Python语言，代码易于理解和运行。  

3. **适用场景**  
- AI初学者通过实际项目学习算法和工具的使用。  
- 开发者寻找灵感，参考类似项目的实现思路。  
- 研究人员快速验证某个算法或模型的可行性。  
- 企业团队用于技术选型或内部培训。  

4. **技术亮点**  
- 项目数量庞大（500个），覆盖范围广，内容丰富。  
- 代码实现简洁，适合不同水平的开发者使用。  
- 标签分类清晰，便于按需筛选和学习。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和调试模型结构。

2. **核心功能**
- 支持 ONNX、TensorFlow、PyTorch、Keras、Core ML、TensorFlow Lite 及 safetensors 等多种模型格式。
- 提供清晰的计算图与层结构可视化，便于理解模型内部逻辑。
- 兼容桌面应用与 Web 浏览器，实现跨平台便捷查看。
- 支持模型权重与张量数据的详细展示与分析。

3. **适用场景**
- 深度学习研究者用于快速检查模型架构是否符合预期。
- 工程师在模型转换（如 PyTorch 转 ONNX）后验证结构完整性。
- 教学与演示中直观展示神经网络的数据流向。
- 调试模型时定位特定层或参数的配置问题。

4. **技术亮点**
- 广泛支持业界主流框架，包括新兴的 safetensors 格式。
- 开源且无需复杂安装，通过浏览器即可直接使用。
- 界面简洁直观，适合不同技术背景的用户快速上手。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**  
该项目为深度学习与机器学习研究者提供必备速查表，涵盖常用算法、函数及代码示例，帮助快速查阅关键知识。内容源自Medium文章，整理自Keras、NumPy、SciPy等主流库的实用技巧。

2. **核心功能**  
- 提供深度学习与机器学习核心概念的速查指南  
- 汇总Keras、NumPy、SciPy等库的常用函数与代码片段  
- 包含Matplotlib可视化技巧与最佳实践  
- 以简洁表格形式呈现，便于快速检索  
- 覆盖从基础语法到高级模型的实用参考内容  

3. **适用场景**  
- 研究人员在实验中快速回顾API用法或数学原理  
- 学生复习机器学习课程重点知识  
- 工程师在开发深度学习项目时参考代码示例  
- 面试准备中梳理关键技术点  

4. **技术亮点**  
项目将分散于官方文档中的关键用法整合为结构化速查表，显著提升查阅效率，特别适合需要频繁切换工具或概念的研究与开发场景。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- **1. 中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并免费提供配套教材，帮助零基础用户入门并实现就业实战。内容涵盖 Python、数学、机器学习、数据分析、深度学习、计算机视觉（CV）及自然语言处理（NLP）等热门领域。

**2. 核心功能**
- 提供系统化 AI 学习路线图，覆盖从入门到就业的完整路径。
- 收录近 200 个实战案例与项目，配套免费教材供学习使用。
- 涵盖 Python 编程、数学基础及主流 AI 框架（如 PyTorch、TensorFlow、Keras 等）。
- 聚焦计算机视觉、自然语言处理、数据分析与数据挖掘等热门应用领域。

**3. 适用场景**
- 零基础学习者系统入门人工智能与机器学习领域。
- 希望提升实战能力的开发者参考项目案例进行练习。
- 寻求 AI 相关职位的求职者通过项目经验增强就业竞争力。
- 需要快速了解 Python 及主流 AI 框架（如 PyTorch、TensorFlow）学习路径的初学者。

**4. 技术亮点**
- 资源高度整合：将课程路线图、实战项目与免费教材三者结合，降低学习门槛。
- 技术栈全面：覆盖从基础数学、Python 编程到深度学习框架及具体应用（CV、NLP）的完整技术链。
- 社区认可度高：拥有超过 13,000 星标，表明其在 AI 学习资源领域具有较高的影响力和实用性。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它支持多种数据类型和任务，旨在简化机器学习模型的训练与部署流程。

2. **核心功能**
- 支持低代码方式快速构建和训练各类神经网络及 LLM。
- 提供对 PyTorch 的封装，简化深度学习模型开发。
- 适用于微调（fine-tuning）如 LLaMA、Mistral 等主流大模型。
- 支持计算机视觉、自然语言处理等多模态任务。
- 注重数据中心（data-centric）方法论，优化数据驱动模型性能。

3. **适用场景**
- 快速原型开发：无需深入编码即可搭建神经网络或 LLM 应用。
- 大模型微调：对 LLaMA、Mistral 等开源模型进行领域适配。
- 多模态 AI 项目：同时处理文本、图像等数据的机器学习任务。
- 数据科学研究：以数据为中心的方法优化模型训练效果。

4. **技术亮点**
- 低代码设计大幅降低 AI 模型开发门槛。
- 原生支持 PyTorch，兼容主流深度学习生态。
- 内置对 LLaMA、Mistral 等大模型的微调支持。
- 强调数据中心理念，助力提升模型泛化能力。
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
- ### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取（手机、身份证、邮箱等）及基础 NLP 功能。它不仅提供词汇资源（如同义词、反义词、情感值、停用词），还收录了大量中文 NLP 数据集、预训练模型及竞赛方案汇总。该项目旨在为开发者提供一个一站式的中英 NLP 资源库，涵盖从基础文本处理到深度学习模型应用的广泛需求。

### 2. 核心功能
- **基础 NLP 工具**：支持中英文敏感词过滤、语言检测、繁简转换、情感分析、分词及命名实体识别。
- **实体与信息抽取**：提供手机号、身份证、邮箱抽取，以及手机归属地/运营商查询和名字推断性别功能。
- **丰富词汇资源库**：内置中日文人名库、中文缩写库、同义词/反义词库、停用词表及各类领域词库（汽车、医学、法律等）。
- **数据集与模型资源**：汇总了大量中文 NLP 数据集（如问答、谣言、对话语料）、预训练模型（BERT、ALBERT 等）及竞赛 Top 方案。
- **语音与 OCR 支持**：包含中文语音识别（ASR）、手写汉字识别（OCR）及语音情感分析相关资源。

### 3. 适用场景
- **内容安全与审核**：利用敏感词库和暴恐词表，快速构建文本过滤和审核系统。
- **信息抽取与结构化**：从非结构化文本中自动提取手机号、身份证、邮箱等关键实体信息。
- **自然语言处理研究**：作为研究人员获取中文 NLP 数据集、基准模型和最新论文资源的聚合平台。
- **智能客服与对话系统**：借助对话语料、知识图谱及问答系统资源，快速搭建聊天机器人。

### 4. 技术亮点
- **资源聚合性强**：不仅是一个工具库，更是中文 NLP 领域的“资源百科”，涵盖了从传统规则方法到最新深度学习模型的全方位资料。
- **领域覆盖广泛**：除了通用 NLP 功能，还特别针对金融、医疗、法律、汽车等专业领域提供了专用词库和模型资源。
- **实用工具集成**：提供了如“汪峰歌词生成器”等趣味工具，以及简历解析、文本纠错、拼音标注等实用功能，兼顾学术与趣味。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory是一个统一且高效的大语言模型（LLM）及多模态模型（VLM）微调框架，支持100多种主流模型。该项目已发表于ACL 2024会议，旨在简化从预训练到强化学习的全流程微调体验。

2. **核心功能**
- 支持100+种LLM和VLM的统一高效微调。
- 集成LoRA、QLoRA、P-Tuning等多种参数高效微调（PEFT）技术。
- 提供完整的训练流程，包括指令微调、RLHF及量化训练。
- 兼容Transformers库，支持DeepSeek、LLaMA、Qwen、Gemma等主流模型。

3. **适用场景**
- 研究者或开发者需要对多种开源大模型进行快速指令微调。
- 资源受限环境下，使用QLoRA等技术进行4/8位量化微调。
- 需要进行RLHF（人类反馈强化学习）对齐的大型语言模型训练。
- 多模态大模型（VLM）的视觉-语言联合微调任务。

4. **技术亮点**
- **统一架构**：一个框架兼容上百种模型，无需为每个模型编写独立代码。
- **极致效率**：深度优化LoRA/QLoRA，显著降低显存占用并提升训练速度。
- **学术认可**：成果发表于顶级自然语言处理会议ACL 2024，具备学术权威性。
- **全链路支持**：涵盖从SFT（监督微调）到RLHF的完整大模型对齐训练流程。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73898 | 🍴 9041 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的AI入门课程，旨在让所有人都能轻松学习人工智能。项目采用Jupyter Notebook形式，内容全面覆盖机器学习与深度学习的基础知识。

2. **核心功能**
- 提供结构化的12周学习路径，适合初学者系统入门。
- 涵盖机器学习、深度学习、计算机视觉、NLP等核心领域。
- 使用Jupyter Notebook作为主要教学载体，支持交互式学习。
- 由Microsoft For Beginners团队开发，内容权威且易于理解。
- 包含CNN、RNN、GAN等深度学习模型的实际应用案例。

3. **适用场景**
- AI初学者系统学习机器学习与深度学习基础。
- 教育工作者用于课堂教学或自学辅导。
- 企业团队进行AI技术入门培训。
- 个人开发者快速掌握AI核心概念与实践技能。

4. **技术亮点**
- 课程内容全面且循序渐进，从基础概念到高级模型均有覆盖。
- 实践导向，通过Jupyter Notebook提供可运行的代码示例。
- 由微软官方出品，质量有保障，适合全球学习者。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63127 | 🍴 12244 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- ### 1. 中文简介
该项目旨在从零开始教授AI工程的核心原理与实践，强调“先理解、再构建、最终为他人交付”的学习路径。它提供了一套完整的课程，帮助开发者深入掌握AI系统的构建过程。

### 2. 核心功能
- **从零构建AI系统**：不依赖高级框架，深入底层实现各类AI组件。
- **覆盖广泛AI领域**：包括LLM、计算机视觉、强化学习、MCP和智能体等。
- **多语言支持**：结合Python和Rust，兼顾易用性与高性能。
- **实战导向课程**：提供教程式学习路径，强调动手实践与项目交付。

### 3. 适用场景
- 希望深入理解AI底层原理、避免黑盒依赖的学习者。
- 需要构建自定义AI智能体或生成式AI应用的工程师。
- 对高性能AI系统开发感兴趣，希望结合Rust优化的开发者。
- 从事AI教育或技术培训，需要系统性课程材料的讲师。

### 4. 技术亮点
- **全栈AI工程覆盖**：从NLP、Transformer到多智能体系统，形成完整知识体系。
- **Rust集成**：在关键性能模块中使用Rust，体现工业级工程实践。
- **MCP支持**：集成Model Context Protocol，促进AI工具与系统的标准化交互。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46217 | 🍴 7994 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- # AiLearning 项目分析

## 1. 中文简介
这是一个全面的数据分析与机器学习实战学习项目，涵盖线性代数、PyTorch、NLTK和TensorFlow 2等核心技术。项目通过实战案例帮助学习者掌握从基础理论到高级应用的完整机器学习知识体系。

## 2. 核心功能
- 数据分析与机器学习算法实战（包括Adaboost、Kmeans、SVM等）
- 深度学习框架应用（PyTorch、TensorFlow 2）
- 自然语言处理技术（NLTK）
- 推荐系统实现（基于协同过滤等算法）
- 经典机器学习算法详解（逻辑回归、决策树、朴素贝叶斯等）

## 3. 适用场景
- 机器学习初学者系统学习与实践
- 数据科学工程师技能提升
- 高校学生课程项目参考
- 企业AI团队技术储备

## 4. 技术亮点
- 42442星标，说明项目质量高、社区认可度强
- 覆盖机器学习全流程：从基础算法到深度学习
- 结合理论（线性代数）与实践（PyTorch/TF2）
- 包含NLP、推荐系统等热门方向
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
- ⭐ 16478 | 🍴 3793 | 语言: Python
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
- ⭐ 268672 | 🍴 23996 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227031 | 🍴 44379 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199720 | 🍴 59993 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186273 | 🍴 46057 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166858 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164436 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162831 | 🍴 9168 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157607 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152925 | 🍴 9826 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

