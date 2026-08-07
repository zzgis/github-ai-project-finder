# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**
shuohao-skills 是一套专为 AI 编码代理（如 Claude Code 和 Codex）设计的技能集合。其中 novel-characters 模块可将小说内容自动转化为包含人物画像、卡通形象提示词、音色设定及三视图在内的完整角色设定集。

2. **核心功能**
- 兼容 Claude Code 和 Codex 两大主流 AI 编码代理。
- 自动拆解小说内容并生成结构化的角色设定档案。
- 提供用于 AI 绘图的卡通形象设计提示词。
- 生成角色配音所需的音色描述提示词。
- 输出角色三视图（Turnaround sheets）以便统一形象。

3. **适用场景**
- 网文作者或小说家快速建立标准化的角色设定库。
- AI 辅助创作团队统一角色视觉风格与声音设定。
- 将文字小说转化为漫画或动画前期开发的资产准备。
- 测试和演示 Claude Code/Codex 的技能扩展能力。

4. **技术亮点**
- 跨平台兼容，同时支持 OpenAI Codex 和 Anthropic Claude Code。
- 专注于非编码类创意任务（小说角色生成），拓展了 AI 编码代理的应用边界。
- 将复杂的角色设计流程自动化，整合了文本、视觉和音频提示词生成。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 186 | 🍴 20 | 语言: JavaScript

### goal-flow
- 1. **中文简介**  
Goal-Flow 是一个基于 LangGraph 的生产级框架，通过图编排实现 Agent 循环，结合工作流图与智能体交互，支持将 Dify DSL 转译为可执行代码，并可灵活切换 Dify/OpenAI 等协议。

2. **核心功能**  
- 支持将 Dify DSL 工作流自动转译为 LangGraph 可执行代码。  
- 融合工作流图与 Agent 循环，实现更复杂的任务编排。  
- 提供可插拔的协议层，可切换 Dify 或 OpenAI 协议。  
- 支持 Human-in-the-loop 交互模式，便于人工介入决策。  
- 兼容 LangChain/LangGraph 生态，便于集成现有 AI 工作流。

3. **适用场景**  
- 需要将 Dify 设计的工作流迁移到 LangGraph 生产环境。  
- 构建需要多 Agent 协作且支持人工干预的复杂 AI 应用。  
- 希望在不同 LLM 提供商（如 Dify 与 OpenAI）间灵活切换协议。  
- 开发需要高度可控、可观测的 Agentic 工作流系统。

4. **技术亮点**  
- 原生支持 Dify DSL 到 LangGraph 代码的自动转译，降低迁移成本。  
- 协议抽象层设计，实现不同 AI 服务间的无缝切换。  
- 结合图编排与 Agent 循环，兼顾工作流确定性与智能体灵活性。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- ## codex-gpt-5.6-5.5-instruct 项目分析

### 1. 中文简介
该项目为 GPT-5.6/5.5 (Codex CLI) 提供了一套指令工程框架，通过 CTF 竞赛心理框架重构运行上下文，使模型的安全训练机制不被激活。项目以"拷打 AI"为目标，采用一键部署方式，仅需 62 行提示词和 50 个技能模块，且为纯 Python 无依赖实现。

### 2. 核心功能
- **安全训练绕过框架**：通过上下文重构使模型安全机制不触发，而非直接压制拒绝
- **CTF 竞赛心理框架**：借鉴 CTF 竞赛思维模式设计运行上下文
- **一键部署方案**：提供 62 行提示词 + 50 个技能模块的快速部署
- **零依赖纯 Python 实现**：无需额外依赖包，开箱即用
- **AI 能力极限测试**：专门用于"拷打"和测试 AI 模型的边界能力

### 3. 适用场景
- 安全研究人员测试 AI 模型的安全边界和拒绝机制
- 提示词工程师优化和验证复杂指令框架
- 对 AI 模型进行极限能力测试和压力测试
- 研究 CTF 竞赛思维在 AI 交互中的应用

### 4. 技术亮点
- **创新的安全绕过思路**：通过上下文重构而非对抗性攻击实现目标
- **极简部署架构**：62 行提示词配合 50 个技能模块实现完整功能
- **零依赖设计**：纯 Python 实现，无外部包依赖，便于部署和移植
- **CTF 框架融合**：将竞赛心理模型应用于 AI 指令工程，具有创新性
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- 1. **中文简介**  
lattice-script-executor 是一款跨平台软件授权管理工具集，支持 Windows、macOS 和 Linux 系统。它内置 AI 驱动的规则引擎，支持离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能，适用于需要安全软件授权管理的开发者与团队。

2. **核心功能**  
- 支持 Windows、macOS 和 Linux 的跨平台授权管理  
- 内置 AI 驱动的规则引擎，实现智能授权判断  
- 提供离线种子验证机制，确保无网络环境下的授权有效性  
- 支持批量生成产品密钥，提升授权分发效率  
- 记录不可篡改的审计日志，便于合规追踪与安全审查

3. **适用场景**  
- 软件公司需要为多平台产品提供统一的授权管理方案  
- 对离线授权有强需求的行业软件（如工业控制、医疗系统）  
- 需要批量发放许可证并保留完整审计记录的企业级应用  
- 希望借助 AI 规则引擎实现动态授权策略的智能软件平台

4. **技术亮点**  
项目采用 HTML 实现前端交互，结合 AI 规则引擎与不可篡改日志技术，在轻量级前端框架下实现了较完整的授权管理逻辑，适合快速原型开发或嵌入现有 Web 授权系统。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- 1. **中文简介**  
该项目暂无详细描述信息，无法提供有效简介。

2. **核心功能**  
- 项目信息不完整，无法识别具体功能。

3. **适用场景**  
- 因缺乏项目内容，无法判断适用场景。

4. **技术亮点**  
- 无可用技术信息，暂无亮点可总结。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 37 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 32 | 🍴 3 | 语言: 未知

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 25 | 🍴 2 | 语言: 未知

### ai-novel-screenplay-analyzer
- 描述: 面向长篇小说、剧本与改编项目的 AI 叙事分析工作台，自动梳理人物关系、章节脉络与关系演化，支持多模型接入、任务断点恢复及本地私有部署。
- 链接: https://github.com/ops120/ai-novel-screenplay-analyzer
- ⭐ 24 | 🍴 1 | 语言: JavaScript

### distillery
- 描述: Distillery: open-source LLM traffic proxy - Route and manage multi-provider AI API traffic with capture and opt-in redaction.
- 链接: https://github.com/TonicAI/distillery
- ⭐ 23 | 🍴 0 | 语言: Python

### daily-global-market-intelligence-description-skills
- 描述: 提供每日股市新闻、财经早餐、盘前/盘后复盘、美股、A股、港股、韩股、全球市场走势、宏观经济、AI板块、半导体、资金流向、市场情绪、财报、ETF、行业轮动、大宗商品、加密货币等内容时触发。提供机构级全球市场日报
- 链接: https://github.com/morangse/daily-global-market-intelligence-description-skills
- ⭐ 22 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个功能极其丰富的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取及各类专业词库等基础处理能力。它同时汇聚了大量开源的预训练模型、数据集及前沿 NLP 算法资源，是中文 NLP 开发者的综合性资源仓库。

### 2. 核心功能
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、停用词表、断句及基础分词等实用工具。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、中日文人名抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
*   **专业领域词库**：内置汽车、医学、法律、财经、IT、成语、地名、历史名人等数十个垂直领域的专业词汇库。
*   **预训练模型与资源**：汇总了 BERT、ALBERT、RoBERTa、GPT-2 等多种中英文预训练模型及对应的微调代码。
*   **数据集与竞赛汇总**：收录了百度、京东、清华大学等机构发布的中文问答、谣言检测、情感分析等数据集及 NLP 竞赛 TOP 方案。

### 3. 适用场景
*   **中文 NLP 项目初始化**：开发者可直接调用其内置词库和工具，快速搭建文本清洗、实体识别等基础流水线。
*   **垂直领域知识构建**：适用于需要汽车、医疗、法律等专业术语支持的企业级知识库或问答系统开发。
*   **算法研究与模型复现**：研究人员可利用其提供的最新预训练模型代码和数据集，复现 SOTA 效果或进行对比实验。
*   **内容安全与风控**：互联网平台可利用其敏感词库和暴恐词表，快速实现内容审核与风险过滤功能。

### 4. 技术亮点
*   **资源聚合度极高**：不仅是一个工具库，更是一个涵盖数据、模型、代码、论文的中文 NLP 全景式资源索引。
*   **覆盖场景全面**：从基础的字符串处理到深度的深度学习模型（如 BERT、Transformer），覆盖了 NLP 全链路需求。
*   **紧跟前沿技术**：持续更新最新的预训练模型（如 ELECTREA、ALBERT）和开源数据集，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
该项目是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理领域，并提供完整代码实现。项目以Python为核心语言，适合希望系统学习AI技术的开发者参考实践。

2. **核心功能**  
- 提供500个分类明确的AI实战项目（机器学习/深度学习/CV/NLP）  
- 所有项目附完整代码，支持直接运行和二次开发  
- 覆盖从基础算法到前沿应用的完整技术栈  
- 采用标签化组织方式，便于按技术领域快速筛选  
- 支持离线下载和模块化学习路径规划  

3. **适用场景**  
- 初学者构建AI知识体系（从线性回归到Transformer）  
- 开发者快速验证算法原型（如图像分类/文本生成）  
- 企业技术选型参考（对比不同方案的实现复杂度）  
- 课程作业/毕业设计素材库（含可复现的实验代码）  

4. **技术亮点**  
- 项目按"理论-实现-优化"三级递进设计，符合认知学习规律  
- 关键算法均提供多版本实现（如CNN的VGG/ResNet对比）  
- 集成主流框架（TensorFlow/PyTorch/Scikit-learn）的标准化接口  
- 包含模型部署指南（Docker容器化/ONNX转换）等工程化内容
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架格式，能够直观地展示模型结构和参数，帮助开发者快速理解和分析模型架构。

2. **核心功能**
- 支持多格式模型可视化，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供清晰的层结构图，展示模型各组件的连接关系和数据流向。
- 兼容多种数据格式，如 safetensors、numpy 等，便于加载不同来源的模型。
- 支持本地和在线使用，用户可快速预览模型而无需编写代码。

3. **适用场景**
- 深度学习模型调试：帮助开发者快速定位模型结构中的问题。
- 模型架构学习：适合初学者直观理解复杂神经网络的设计逻辑。
- 跨框架模型转换验证：用于检查不同框架间模型转换后的结构一致性。
- 技术文档与演示：生成清晰的模型结构图，便于技术分享和文档编写。

4. **技术亮点**
- 广泛支持主流 AI 框架，覆盖 TensorFlow、PyTorch、ONNX 等常见格式。
- 开源且社区活跃，拥有超过 3.3 万星标，证明其广泛认可和实用性。
- 无需依赖特定环境，即可快速加载和可视化模型，提升开发效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**  
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准，旨在实现不同深度学习框架之间的模型无缝迁移与部署。它支持将训练好的模型从主流框架导出为统一格式，从而提升跨平台兼容性和工程效率。

2. **核心功能**  
- 提供统一的模型表示格式，支持跨框架模型交换  
- 兼容 PyTorch、TensorFlow、Keras、scikit-learn 等主流机器学习库  
- 支持模型转换、验证与优化，便于部署到不同硬件平台  
- 提供 Python 工具链，简化 ONNX 模型的创建与操作  
- 促进机器学习工作流中训练与推理环境的解耦

3. **适用场景**  
- 将 PyTorch 或 TensorFlow 训练好的模型部署到移动端或嵌入式设备  
- 在异构硬件（如 CPU、GPU、NPU）上优化和加速推理  
- 构建框架无关的机器学习 pipeline，提升工程可移植性  
- 模型协作与共享，避免被单一厂商生态锁定

4. **技术亮点**  
ONNX 由微软、Facebook 等科技巨头联合推动，已成为工业界事实上的模型交换标准，拥有活跃的社区支持和完善的算子库覆盖。
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面覆盖机器学习工程实践的技术指南。内容涵盖从硬件基础设施、分布式训练到模型推理部署的完整工程链路。

2. **核心功能**
- 深入解析 GPU 硬件架构与高性能网络通信优化。
- 提供大规模分布式训练策略及 Slurm 集群管理方案。
- 讲解大语言模型（LLM）的推理加速与工程化部署技巧。
- 涵盖存储系统优化、调试方法及模型可扩展性设计。

3. **适用场景**
- 构建和优化大规模深度学习训练集群的工程团队。
- 需要部署高并发 LLM 推理服务的基础设施工程师。
- 研究分布式系统性能瓶颈与调优的算法工程师。

4. **技术亮点**
该项目由实战专家撰写，内容紧密围绕 PyTorch 和 Transformers 生态，填补了从理论到生产环境落地之间的工程知识空白。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18530 | 🍴 1191 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2118 | 语言: 未知
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
- ⭐ 10687 | 🍴 5704 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个精选的AI项目合集，包含500个机器学习、深度学习、计算机视觉和自然语言处理项目的完整代码实现。项目涵盖从入门到进阶的各类AI应用场景，适合不同水平的学习者参考实践。

### 2. 核心功能
- **项目分类全面**：涵盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- **代码完整可运行**：每个项目都提供完整的代码实现和详细文档
- **难度分级清晰**：从基础到高级项目都有收录，适合不同阶段学习者
- **Python生态支持**：主要使用Python语言，集成主流AI框架和工具

### 3. 适用场景
- **AI学习者**：系统学习机器学习、深度学习理论和实践的优质资源库
- **开发者参考**：快速查找和复现各类AI项目的代码实现
- **项目实践**：将理论知识转化为实际项目经验的实践指南
- **技术选型**：了解当前AI领域热门技术方向和应用场景

### 4. 技术亮点
- **星标数36029**：证明项目在社区中的高认可度和广泛使用
- **标签体系完善**：涵盖artificial-intelligence、computer-vision、deep-learning等关键领域
- **awesome系列**：属于精选优质项目合集，质量有保障
- **实战导向**：强调代码实现和实际应用，而非纯理论讲解

### 总结
这是一个高质量的AI项目资源库，特别适合想要系统学习机器学习、深度学习、计算机视觉和NLP的开发者。项目代码完整、分类清晰、难度适中，是AI学习者的优秀参考资料。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架格式，能够直观地展示模型结构和参数，帮助开发者快速理解和分析模型架构。

2. **核心功能**
- 支持多格式模型可视化，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供清晰的层结构图，展示模型各组件的连接关系和数据流向。
- 兼容多种数据格式，如 safetensors、numpy 等，便于加载不同来源的模型。
- 支持本地和在线使用，用户可快速预览模型而无需编写代码。

3. **适用场景**
- 深度学习模型调试：帮助开发者快速定位模型结构中的问题。
- 模型架构学习：适合初学者直观理解复杂神经网络的设计逻辑。
- 跨框架模型转换验证：用于检查不同框架间模型转换后的结构一致性。
- 技术文档与演示：生成清晰的模型结构图，便于技术分享和文档编写。

4. **技术亮点**
- 广泛支持主流 AI 框架，覆盖 TensorFlow、PyTorch、ONNX 等常见格式。
- 开源且社区活跃，拥有超过 3.3 万星标，证明其广泛认可和实用性。
- 无需依赖特定环境，即可快速加载和可视化模型，提升开发效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **中文简介**  
这是一个面向深度学习与机器学习研究者的实用速查表集合，涵盖核心概念、常用库（如Keras、NumPy、SciPy、Matplotlib）的关键用法和技巧，帮助研究人员快速查阅和复习关键知识点。

**核心功能**  
- 提供机器学习与深度学习中的常用公式、算法和概念速查  
- 集成Keras、NumPy、SciPy、Matplotlib等主流库的代码示例  
- 以简洁清晰的格式呈现，便于快速查阅和记忆  
- 适合初学者复习和进阶研究者参考  

**适用场景**  
- 机器学习/深度学习课程学习时的快速参考  
- 面试前快速回顾核心概念和代码用法  
- 研究过程中查阅常用库的API和技巧  
- 团队内部知识共享与培训材料  

**技术亮点**  
- 内容精炼、覆盖全面，聚焦研究者高频使用知识点  
- 结合理论概念与代码实践，兼顾理解与动手  
- 免费开源，易于获取和分享
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份人工智能学习路线图，整理了近 200 个实战案例与项目，并免费提供配套教材，旨在帮助零基础用户入门并提升就业实战能力。项目覆盖 Python、机器学习、深度学习、计算机视觉、自然语言处理等热门领域。

### 2. 核心功能
- 提供系统化的 AI 学习路线图，涵盖从数学基础到高级应用的完整路径。
- 收录近 200 个实战案例与项目，支持动手实践与技能巩固。
- 免费提供配套教材与学习资源，降低入门门槛。
- 覆盖 Python、TensorFlow、PyTorch、Pandas、NLP、CV 等主流技术与工具。
- 针对就业需求设计，注重实战能力与工程落地。

### 3. 适用场景
- 零基础学习者希望系统入门人工智能与机器学习领域。
- 学生或转行人员希望通过实战项目提升就业竞争力。
- 开发者希望快速查阅和复习 AI 相关技术栈与经典案例。
- 教师或培训机构用于辅助课程设计或实践教学参考。

### 4. 技术亮点
- 项目整合了多种主流深度学习框架（TensorFlow、PyTorch、Keras、Caffe）与数据分析库（NumPy、Pandas、Matplotlib、Seaborn），形成完整技术生态。
- 以“路线图+实战案例+免费教材”三位一体的形式，兼顾学习路径清晰性与实践可操作性。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**  
Ludwig 是一个低代码框架，用于构建自定义的 LLM（大型语言模型）、神经网络及其他 AI 模型。它支持深度学习全流程，包括数据预处理、模型训练、评估和部署，适合快速原型开发和生产级 AI 应用。

2. **核心功能**  
- 支持多种模型架构（如 Transformer、CNN、RNN 等），可灵活定制神经网络结构。  
- 提供端到端训练流程，涵盖数据加载、特征工程、模型训练和超参数调优。  
- 兼容主流深度学习框架（如 PyTorch），并支持分布式训练加速。  
- 内置模型评估和可视化工具，便于分析训练效果和模型性能。  
- 支持低代码/无代码交互，降低 AI 模型开发门槛。

3. **适用场景**  
- 快速构建和微调自定义 LLM（如基于 LLaMA、Mistral 的领域适配模型）。  
- 图像分类、目标检测等计算机视觉任务的模型训练与部署。  
- 需要数据驱动迭代的机器学习项目，如推荐系统或预测分析。  
- 教育或研究场景中的深度学习实验，无需编写大量代码即可验证想法。

4. **技术亮点**  
- 低代码特性显著缩短模型开发周期，适合非专业开发者快速上手。  
- 深度集成 PyTorch 生态，兼顾灵活性与性能优化。  
- 支持数据-centric 方法，强调数据质量对模型效果的影响。  
- 内置可视化工具（如训练曲线、特征重要性分析），提升可解释性。
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
funNLP 是一个功能极其丰富的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取及各类专业词库等基础处理能力。它同时汇聚了大量开源的预训练模型、数据集及前沿 NLP 算法资源，是中文 NLP 开发者的综合性资源仓库。

### 2. 核心功能
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、停用词表、断句及基础分词等实用工具。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、中日文人名抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
*   **专业领域词库**：内置汽车、医学、法律、财经、IT、成语、地名、历史名人等数十个垂直领域的专业词汇库。
*   **预训练模型与资源**：汇总了 BERT、ALBERT、RoBERTa、GPT-2 等多种中英文预训练模型及对应的微调代码。
*   **数据集与竞赛汇总**：收录了百度、京东、清华大学等机构发布的中文问答、谣言检测、情感分析等数据集及 NLP 竞赛 TOP 方案。

### 3. 适用场景
*   **中文 NLP 项目初始化**：开发者可直接调用其内置词库和工具，快速搭建文本清洗、实体识别等基础流水线。
*   **垂直领域知识构建**：适用于需要汽车、医疗、法律等专业术语支持的企业级知识库或问答系统开发。
*   **算法研究与模型复现**：研究人员可利用其提供的最新预训练模型代码和数据集，复现 SOTA 效果或进行对比实验。
*   **内容安全与风控**：互联网平台可利用其敏感词库和暴恐词表，快速实现内容审核与风险过滤功能。

### 4. 技术亮点
*   **资源聚合度极高**：不仅是一个工具库，更是一个涵盖数据、模型、代码、论文的中文 NLP 全景式资源索引。
*   **覆盖场景全面**：从基础的字符串处理到深度的深度学习模型（如 BERT、Transformer），覆盖了 NLP 全链路需求。
*   **紧跟前沿技术**：持续更新最新的预训练模型（如 ELECTREA、ALBERT）和开源数据集，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### LlamaFactory
- ### 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持100多种模型，相关研究已发表于ACL 2024。它旨在简化模型微调流程，提供灵活且高性能的解决方案。

---

### 2. **核心功能**
- 支持100+种LLM和VLM的统一微调，包括LLaMA、Gemma、Qwen等主流模型。
- 提供LoRA、QLoRA、全参数微调等多种微调策略，适应不同硬件和资源需求。
- 内置RLHF（基于人类反馈的强化学习）支持，便于优化模型输出质量。
- 兼容多种量化技术（如4-bit/8-bit量化），显著降低显存占用。
- 高度模块化设计，用户可轻松扩展自定义模型或任务。

---

### 3. **适用场景**
- 开发者希望对大语言模型进行领域适配或指令微调，提升特定任务性能。
- 研究团队需要快速实验不同微调方法（如LoRA vs. QLoRA）的对比效果。
- 企业希望部署轻量级且高效的视觉语言模型，用于图像理解或多模态任务。
- 资源受限环境下，通过量化和高效微调技术实现模型优化。

---

### 4. **技术亮点**
- **统一框架**：支持多种模型和任务的无缝切换，减少开发成本。
- **高效微调**：通过LoRA和QLoRA等技术，在低显存条件下实现高性能微调。
- **前沿研究支持**：集成RLHF等先进训练方法，紧跟AI研究趋势。
- **广泛兼容性**：支持Hugging Face Transformers生态，便于集成现有工具链。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73900 | 🍴 9040 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一门为期12周、包含24课时的AI通识课程，旨在让所有人轻松掌握人工智能技术。课程由微软开发者关系团队主导，内容覆盖机器学习、深度学习及自然语言处理等核心领域。

2. **核心功能**
- 提供结构化的12周学习路径，每两周一个模块，循序渐进。
- 采用Jupyter Notebook交互形式，支持代码即时运行与实验。
- 涵盖机器学习、计算机视觉、自然语言处理及生成式AI等广泛主题。
- 包含配套视频讲座、测验和作业，适合自学与课堂教学。
- 免费开源，降低AI学习门槛，适合零基础上手。

3. **适用场景**
- 大学生或初学者系统学习人工智能基础理论与实践。
- 教师用于课堂教学，作为AI入门课程的标准化教材。
- 开发者希望快速了解AI生态，补充机器学习知识盲区。
- 企业培训中用于普及AI概念，提升团队技术素养。

4. **技术亮点**
- 内容由微软AI教育团队精心打磨，兼具学术严谨性与教学友好性。
- 紧跟AI前沿，后期课程涵盖GAN、RNN、CNN及大模型应用。
- 完全开源且持续更新，社区活跃，资源丰富（代码、视频、笔记齐全）。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63151 | 🍴 12249 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- # GitHub 项目分析：ai-engineering-from-scratch

## 1. 中文简介
该项目是一套从零开始构建 AI 系统的完整教程，帮助学习者深入理解原理、动手实践开发，并最终将成果部署给他人使用。内容涵盖从基础概念到高级应用的完整学习路径。

## 2. 核心功能
- 提供从零开始实现 AI 系统的完整教程，涵盖深度学习、大语言模型和生成式 AI 等核心领域
- 支持多编程语言学习，包括 Python、Rust 和 TypeScript，满足不同技术栈需求
- 涵盖 AI 工程化全流程，包括智能体（Agents）、MCP 协议、计算机视觉和强化学习等前沿方向
- 结合 swarm intelligence（群体智能）等高级主题，提供深度的技术实践指导

## 3. 适用场景
- AI 初学者系统学习深度学习、NLP 和 LLM 原理与实践
- 工程师希望从零实现 AI 组件，深入理解底层机制而非仅调用 API
- 团队需要构建 AI 智能体系统或部署生成式 AI 应用的生产环境

## 4. 技术亮点
- 覆盖技术栈广泛：从传统的机器学习、Transformer 架构到最新的 AI Agents 和 MCP 协议
- 多语言支持：同时提供 Python、Rust、TypeScript 实现，适合不同偏好的开发者
- 强调"从 scratch"：不依赖高级框架封装，帮助学习者真正理解 AI 系统的底层原理
- 高人气项目：46224 星标表明其在 AI 学习社区中具有广泛影响力
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46224 | 🍴 7995 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- **1. 中文简介**
该项目是一套系统性的 AI 学习资源，涵盖数据分析与机器学习实战、线性代数基础，以及 PyTorch 和 TensorFlow 2 等深度学习框架的应用。内容还整合了 NLTK 自然语言处理库，适合希望从零开始构建完整 AI 知识体系的学习者。

**2. 核心功能**
- 提供机器学习经典算法（如 SVM、KMeans、Adaboost、Apriori 等）的代码实现与原理讲解。
- 包含深度学习实战，涵盖 DNN、RNN、LSTM 及基于 PyTorch 和 TF2 的模型构建。
- 集成 NLP 自然语言处理内容，利用 NLTK 库进行文本分析与处理。
- 补充线性代数等数学基础，帮助理解算法背后的理论支撑。
- 覆盖推荐系统、回归、分类、降维（PCA/SVD）等主流应用场景。

**3. 适用场景**
- 机器学习初学者系统学习算法原理与 Python 实现。
- 深度学习工程师进阶，掌握 PyTorch 和 TensorFlow 2 的实战开发。
- 自然语言处理（NLP）研究者使用 NLTK 进行文本挖掘与分析。
- 数据科学面试准备，通过经典算法代码回顾核心知识点。

**4. 技术亮点**
- 内容全面，从数学基础到深度学习框架，形成完整学习闭环。
- 代码实战导向，结合 scikit-learn 等主流库提供可直接运行的示例。
- 高人气项目（42k+ 星标），社区认可度高，适合广泛参考学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42442 | 🍴 11524 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33811 | 🍴 4705 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28977 | 🍴 3530 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21823 | 🍴 3340 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个精选的AI项目合集，包含500个机器学习、深度学习、计算机视觉和自然语言处理项目的完整代码实现。项目涵盖从入门到进阶的各类AI应用场景，适合不同水平的学习者参考实践。

### 2. 核心功能
- **项目分类全面**：涵盖机器学习、深度学习、计算机视觉、NLP四大核心领域
- **代码完整可运行**：每个项目都提供完整的代码实现和详细文档
- **难度分级清晰**：从基础到高级项目都有收录，适合不同阶段学习者
- **Python生态支持**：主要使用Python语言，集成主流AI框架和工具

### 3. 适用场景
- **AI学习者**：系统学习机器学习、深度学习理论和实践的优质资源库
- **开发者参考**：快速查找和复现各类AI项目的代码实现
- **项目实践**：将理论知识转化为实际项目经验的实践指南
- **技术选型**：了解当前AI领域热门技术方向和应用场景

### 4. 技术亮点
- **星标数36029**：证明项目在社区中的高认可度和广泛使用
- **标签体系完善**：涵盖artificial-intelligence、computer-vision、deep-learning等关键领域
- **awesome系列**：属于精选优质项目合集，质量有保障
- **实战导向**：强调代码实现和实际应用，而非纯理论讲解

### 总结
这是一个高质量的AI项目资源库，特别适合想要系统学习机器学习、深度学习、计算机视觉和NLP的开发者。项目代码完整、分类清晰、难度适中，是AI学习者的优秀参考资料。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22708 | 🍴 2137 | 语言: Python
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
- ⭐ 385477 | 🍴 81025 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268711 | 🍴 23997 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227063 | 🍴 44394 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199733 | 🍴 59997 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186300 | 🍴 46059 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166859 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164435 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162881 | 🍴 9170 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157608 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152930 | 🍴 9827 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

