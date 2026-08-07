# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**  
shuohao-skills 是一套专为 AI 编码代理（如 Claude Code 和 Codex）设计的技能集合。其中 novel-characters 模块可将小说自动拆解为角色设定集，包含人物画像、卡通形象提示词、音色提示词及三视图生成。

2. **核心功能**  
- 提供兼容 Claude Code 与 OpenAI Codex 的 AI 编码技能包  
- novel-characters 将小说内容结构化转化为角色圣经（character bible）  
- 自动生成人物画像描述与卡通设计提示词  
- 输出角色音色提示词用于语音合成或配音指导  
- 生成角色三视图（正面、侧面、背面）设计参考

3. **适用场景**  
- AI 辅助小说创作中批量生成标准化角色设定  
- 动画/游戏开发前快速构建角色视觉与声音风格指南  
- 使用 Claude Code 或 Codex 进行自动化内容处理工作流  
- 网文作者或编剧将文本角色转化为可视化开发资产

4. **技术亮点**  
- 双平台兼容（Claude Code + Codex），提升 AI 编码工具链灵活性  
- 专注“文本→结构化角色资产”的端到端自动化转换  
- 技能模块化设计，便于按需组合或扩展
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 186 | 🍴 20 | 语言: JavaScript

### goal-flow
- 1. **中文简介**
Goal-Flow 是一个基于 LangGraph 的生产级框架，采用图编排的 Agent 循环架构。它将工作流图与 Agent 循环相结合，支持将 Dify DSL 编译为可运行代码，并可在 Dify 和 OpenAI 协议之间自由切换。

2. **核心功能**
- 基于 LangGraph 的图编排 Agent 循环，实现生产级稳定性。
- 支持将 Dify DSL 自动转译为可执行的 Python 代码。
- 提供协议互换能力，兼容 Dify 和 OpenAI 接口标准。
- 融合传统工作流图与多 Agent 协作循环。
- 支持人在回路（Human-in-the-loop）交互机制。

3. **适用场景**
- 需要将现有 Dify 工作流迁移或增强为 LangGraph 可执行代码的场景。
- 构建需要灵活切换 AI 协议（如从 Dify 迁移到 OpenAI 兼容接口）的生产环境。
- 开发复杂多 Agent 协作系统，需结合确定性工作流与自主 Agent 循环的场景。
- 需要引入人工审核或干预环节的企业级 AI 应用开发。

4. **技术亮点**
- **DSL 转译能力**：独特支持将 Dify DSL 直接编译为 LangGraph 可运行代码，降低迁移成本。
- **协议抽象层**：通过封装 Wire Protocol 切换机制，实现后端 AI 服务的灵活替换。
- **混合架构**：有机结合确定性工作流图与非确定性 Agent 循环，兼顾可控性与智能性。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- **中文简介**  
该项目是一个针对 GPT-5.6/5.5-Instruct 模型（Codex CLI 版本）的指令工程框架。它通过引入 CTF 竞赛心理框架重构运行上下文，旨在规避模型的安全训练机制，避免触发拒绝响应。项目声称无需打压或对抗，而是通过改变输入逻辑使拒绝通路自然失效，并提供一键部署方案。

**核心功能**  
1. 提供基于 CTF 竞赛心理框架的上下文重构机制，以绕过模型安全限制。  
2. 内置 62 行精简提示词和 50 个技能模块，实现纯 Python 无依赖的一键部署。  
3. 优化指令结构，确保模型在特定上下文中不触发安全拒绝，从而提升响应率。  
4. 支持对 GPT-5.6/5.5-Instruct 模型的深度指令工程，适用于高阶 AI 交互场景。  

**适用场景**  
1. 需要绕过模型安全限制以获取特定输出的高级用户或研究者。  
2. 参与 CTF 竞赛或类似挑战，利用心理框架设计对抗性提示的开发者。  
3. 对 AI 模型指令工程感兴趣，希望探索上下文重构技术的开发者。  
4. 需要快速部署无依赖 Python 框架进行模型交互测试的场景。  

**技术亮点**  
- 纯 Python 实现，无第三方依赖，部署简洁高效。  
- 结合 CTF 心理框架与指令工程，创新性规避安全训练机制。  
- 模块化设计（50 个技能模块），灵活适配不同交互需求。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- 1. **中文简介**
这是一个跨平台的软件授权工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可变的审计日志功能。

2. **核心功能**
- 支持 Windows、macOS 和 Linux 的多平台授权管理。
- 利用 AI 规则引擎实现智能化的授权策略控制。
- 提供离线种子验证机制，确保无网络环境下的授权安全。
- 支持批量生成产品密钥，提升授权分发效率。
- 记录不可变的审计日志，保障授权操作的透明性与可追溯性。

3. **适用场景**
- 需要跨平台分发的桌面软件授权管理。
- 对授权安全性和操作审计有严格要求的商业软件。
- 需要在离线环境下验证软件合法性的场景。
- 需要批量生成和管理产品密钥的 SaaS 或本地软件服务商。

4. **技术亮点**
- 结合 AI 规则引擎与离线验证，兼顾智能化与安全性。
- 采用不可变审计日志，确保授权操作记录无法被篡改。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- 1. **中文简介**  
该项目信息不完整，无法提供有效描述。

2. **核心功能**  
暂无明确功能信息。

3. **适用场景**  
暂无适用场景信息。

4. **技术亮点**  
暂无技术亮点信息。
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

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 23 | 🍴 2 | 语言: 未知

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
- ### 1. **中文简介**
funNLP 是一个功能全面的中文自然语言处理工具库，提供敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）及丰富的词库资源。它集成了情感分析、关键词提取、文本摘要、命名实体识别等核心 NLP 功能，并包含大量预训练模型和公开数据集。

### 2. **核心功能**
- **文本清洗与检测**：支持中英文敏感词过滤、语言检测、停用词处理及繁简体转换。
- **实体与信息抽取**：提供手机号、身份证、邮箱、人名、地名等正则抽取，以及基于 BERT/CRF 的命名实体识别（NER）。
- **词库与知识资源**：内置中日文人名库、汽车品牌库、古诗词库、医学/法律/金融领域词库及停用词表。
- **情感分析与语义理解**：包含词汇情感值、同义/反义词库、否定词库，支持文本情感分类和相似度计算。
- **预训练模型与工具**：集成 BERT、ALBERT、RoBERTa 等中文预训练模型，以及分词、句法分析、OCR 等实用工具。

### 3. **适用场景**
- **内容审核平台**：利用敏感词库和情感分析功能，对用户生成内容（UGC）进行实时过滤和风险评估。
- **智能客服与对话系统**：结合实体抽取、意图识别和聊天机器人数据集，构建具备上下文理解能力的客服机器人。
- **金融/法律/医疗行业分析**：使用领域专用词库和知识图谱工具，从专业文档中提取关键实体、关系和摘要。
- **NLP 研究与教育**：作为学习资源库，提供从基础分词到深度学习模型（如 BERT、GPT-2）的完整实践案例和代码。

### 4. **技术亮点**
- **一站式资源聚合**：不仅包含代码工具，还整合了清华 XLORE、百度、阿里等机构的高质量中文数据集和预训练模型。
- **多模型支持**：兼容 spaCy、Jieba、Transformers 等主流 NLP 框架，并提供神经网络的 NER、句法分析等实现。
- **领域垂直深化**：针对医疗、金融、汽车、法律等垂直领域提供专门的数据集和模型，提升行业应用精度。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

#### 1. 中文简介
这是一个收录了500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。项目提供完整的代码实现，适合希望快速上手AI开发的学习者和开发者。

#### 2. 核心功能
- 提供500个AI项目的完整代码示例，覆盖主流技术方向。
- 支持多种应用场景，包括图像识别、文本分析、预测模型等。
- 每个项目均标注所属领域（如机器学习、深度学习、NLP等），便于筛选。
- 代码结构清晰，适合初学者参考和进阶者扩展。
- 定期更新，保持与AI技术发展的同步。

#### 3. 适用场景
- **学习与实践**：适合AI初学者通过实际项目快速掌握技术。
- **竞赛与面试准备**：可作为算法竞赛或技术面试的参考资源。
- **研究与开发**：为研究人员提供可复现的实验代码和灵感。
- **企业应用探索**：帮助开发者评估AI技术在业务场景中的可行性。

#### 4. 技术亮点
- 项目分类明确，覆盖人工智能的主要分支领域。
- 代码实现注重实用性和可读性，便于直接运行和修改。
- 高星标数（36029）表明其在社区中的广泛认可度和影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### Netron 项目分析

1. **中文简介**  
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架和模型格式，帮助用户直观理解模型结构。通过图形化界面，用户可以轻松查看和分析模型的层结构、参数和数据流向。

2. **核心功能**  
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。  
- 提供直观的图形化界面，展示模型的层结构和连接关系。  
- 可导出模型为图像或交互式 HTML 文件，便于分享和演示。  
- 支持查看模型参数和权重信息，帮助调试和优化模型。  
- 兼容 safetensors 等新兴格式，适应最新技术趋势。

3. **适用场景**  
- 研究人员和开发者在调试模型时快速定位问题。  
- 数据科学家向团队或客户展示模型架构和逻辑。  
- 教育场景中用于讲解神经网络的工作原理。  
- 模型部署前的结构验证和优化分析。

4. **技术亮点**  
- 跨平台支持，可在 Windows、macOS 和 Linux 上运行。  
- 开源且免费，社区活跃，持续更新支持新格式。  
- 无需安装额外依赖，开箱即用，降低使用门槛。  
- 结合现代 Web 技术，提供流畅的交互体验。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开源的机器学习互操作性标准，旨在实现不同深度学习框架之间的模型兼容与转换。它允许开发者在不同框架（如PyTorch、TensorFlow、Keras等）之间无缝迁移模型，提升开发效率和部署灵活性。

### 2. 核心功能
- 提供统一的模型格式，支持跨框架的模型导入导出
- 实现深度学习模型在不同平台间的无缝转换
- 支持主流框架（PyTorch、TensorFlow、Keras、scikit-learn）的互操作性
- 提供模型优化和部署工具链
- 建立开放的行业标准，促进AI生态协作

### 3. 适用场景
- 模型迁移：将PyTorch训练好的模型转换为TensorFlow或ONNX格式进行部署
- 跨平台部署：在移动端、边缘设备或不同硬件平台上运行同一模型
- 框架选型：在开发阶段使用PyTorch，生产环境使用TensorFlow等框架
- 模型优化：利用ONNX优化工具提升模型推理性能

### 4. 技术亮点
- 由微软、Facebook等科技巨头共同推动，已成为ML互操作的事实标准
- 社区活跃，拥有21000+星标，生态系统完善
- 支持动态计算图和静态图，兼容多种网络架构
- 提供完整的工具链（onnx、onnxruntime、onnx-simplifier等）
- 与主流硬件厂商合作，优化推理性能
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**  
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的开源指南，旨在为从业者提供从模型训练、调试到大规模部署的全链路知识。项目以 Python 为主，聚焦大语言模型（LLM）和 PyTorch 生态，结合真实工程经验，帮助读者掌握可扩展、可复现的 ML 系统构建方法。

2. **核心功能**  
- 提供 LLM 训练、推理与微调的完整工程实践指南  
- 深入讲解 GPU 利用、分布式训练与 Slurm 集群调度  
- 涵盖模型调试、性能优化与可扩展性设计模式  
- 包含 MLOps 最佳实践，如存储、网络与部署流水线  
- 集成 Transformers 库与 PyTorch 的实际应用案例  

3. **适用场景**  
- 工程师构建大规模语言模型训练基础设施  
- 研究团队复现和优化 LLM 训练流程  
- MLOps 团队搭建高可用、可扩展的模型部署系统  
- 学习者系统掌握机器学习工程的核心技能  

4. **技术亮点**  
项目由工业界与学术界专家共同维护，内容紧跟 LLM 工程前沿，涵盖从底层 GPU 调优到上层 MLOps 的全栈知识，且持续更新以反映最新实践。
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
- ### 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

#### 1. 中文简介
这是一个收录了500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。项目提供完整的代码实现，适合希望快速上手AI开发的学习者和开发者。

#### 2. 核心功能
- 提供500个AI项目的完整代码示例，覆盖主流技术方向。
- 支持多种应用场景，包括图像识别、文本分析、预测模型等。
- 每个项目均标注所属领域（如机器学习、深度学习、NLP等），便于筛选。
- 代码结构清晰，适合初学者参考和进阶者扩展。
- 定期更新，保持与AI技术发展的同步。

#### 3. 适用场景
- **学习与实践**：适合AI初学者通过实际项目快速掌握技术。
- **竞赛与面试准备**：可作为算法竞赛或技术面试的参考资源。
- **研究与开发**：为研究人员提供可复现的实验代码和灵感。
- **企业应用探索**：帮助开发者评估AI技术在业务场景中的可行性。

#### 4. 技术亮点
- 项目分类明确，覆盖人工智能的主要分支领域。
- 代码实现注重实用性和可读性，便于直接运行和修改。
- 高星标数（36029）表明其在社区中的广泛认可度和影响力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### Netron 项目分析

1. **中文简介**  
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架和模型格式，帮助用户直观理解模型结构。通过图形化界面，用户可以轻松查看和分析模型的层结构、参数和数据流向。

2. **核心功能**  
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。  
- 提供直观的图形化界面，展示模型的层结构和连接关系。  
- 可导出模型为图像或交互式 HTML 文件，便于分享和演示。  
- 支持查看模型参数和权重信息，帮助调试和优化模型。  
- 兼容 safetensors 等新兴格式，适应最新技术趋势。

3. **适用场景**  
- 研究人员和开发者在调试模型时快速定位问题。  
- 数据科学家向团队或客户展示模型架构和逻辑。  
- 教育场景中用于讲解神经网络的工作原理。  
- 模型部署前的结构验证和优化分析。

4. **技术亮点**  
- 跨平台支持，可在 Windows、macOS 和 Linux 上运行。  
- 开源且免费，社区活跃，持续更新支持新格式。  
- 无需安装额外依赖，开箱即用，降低使用门槛。  
- 结合现代 Web 技术，提供流畅的交互体验。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **中文简介**
本项目为深度学习与机器学习研究者提供必备的知识速查表。内容涵盖从基础概念到高级实现的广泛主题，旨在帮助研究人员快速回顾关键知识点。

**核心功能**
1. 提供机器学习与深度学习领域的核心概念速查。
2. 涵盖Python数据科学生态（NumPy、SciPy、Matplotlib、Keras）的关键用法。
3. 整理常用算法、数学公式及代码示例供快速参考。
4. 内容源自Medium文章，结构清晰，适合打印或在线查阅。

**适用场景**
1. 研究人员复习机器学习基础理论和常用库API时作为快速手册。
2. 学生在准备面试或考试时，快速查阅关键概念和公式。
3. 工程师在实现模型时，参考代码片段和最佳实践。
4. 团队内部培训或知识共享时，作为标准化的参考资料。

**技术亮点**
- 高度聚焦于研究场景，整合了理论与实用代码示例。
- 覆盖主流工具链（Keras、NumPy等），便于跨领域对照学习。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**  
Ai-Learn 是一个免费的人工智能学习路线图项目，整理了近200个实战案例与项目，配套教材齐全，适合零基础入门并面向就业实战。涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域，支持TensorFlow、PyTorch、Keras等主流框架。

2. **核心功能**  
- 提供系统化AI学习路径，从基础到进阶清晰规划  
- 收录近200个实战案例，覆盖主流AI技术方向  
- 免费配套教材，适合零基础学习者入门  
- 面向就业实战，强化实际应用能力  
- 支持多框架（TensorFlow、PyTorch、Keras等）学习与实践  

3. **适用场景**  
- 初学者系统学习人工智能与机器学习  
- 求职者准备AI相关岗位实战技能  
- 教师或培训机构用于课程设计与教学参考  
- 企业技术人员拓展AI技术视野与实践案例  

4. **技术亮点**  
- 覆盖算法、数据分析、深度学习、NLP、CV等多领域  
- 强调实战导向，案例丰富且贴近实际应用  
- 开源免费，配套教材完整，学习成本低
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络和其他 AI 模型。它简化了机器学习模型的训练和部署流程，让开发者能够专注于业务逻辑而非底层技术细节。

### 2. 核心功能
- **低代码开发**：通过声明式配置快速构建和训练 ML 模型
- **多模态支持**：支持文本、图像、表格等多种数据类型处理
- **预训练模型集成**：内置 LLaMA、Mistral 等大语言模型的微调能力
- **自动化 ML 流程**：自动处理数据预处理、特征工程和模型选择
- **PyTorch 后端**：基于 PyTorch 构建，支持 GPU 加速训练

### 3. 适用场景
- **快速原型开发**：需要快速验证 AI 想法的初创团队或研究者
- **企业级模型部署**：需要将 ML 模型从实验环境迁移到生产环境的团队
- **多模态应用开发**：同时处理文本和图像数据的 AI 应用（如视觉问答、文档理解）
- **大模型微调**：基于 LLaMA、Mistral 等开源模型进行领域适配

### 4. 技术亮点
- **数据中心方法论**：强调数据质量而非单纯依赖模型架构优化
- **AutoML 能力**：自动超参数调优和模型选择
- **可视化界面**：提供 Web UI 便于非技术人员参与模型开发
- **生产就绪**：支持模型导出到 TensorFlow SavedModel、ONNX 等格式
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
- ### 1. **中文简介**
funNLP 是一个功能全面的中文自然语言处理工具库，提供敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）及丰富的词库资源。它集成了情感分析、关键词提取、文本摘要、命名实体识别等核心 NLP 功能，并包含大量预训练模型和公开数据集。

### 2. **核心功能**
- **文本清洗与检测**：支持中英文敏感词过滤、语言检测、停用词处理及繁简体转换。
- **实体与信息抽取**：提供手机号、身份证、邮箱、人名、地名等正则抽取，以及基于 BERT/CRF 的命名实体识别（NER）。
- **词库与知识资源**：内置中日文人名库、汽车品牌库、古诗词库、医学/法律/金融领域词库及停用词表。
- **情感分析与语义理解**：包含词汇情感值、同义/反义词库、否定词库，支持文本情感分类和相似度计算。
- **预训练模型与工具**：集成 BERT、ALBERT、RoBERTa 等中文预训练模型，以及分词、句法分析、OCR 等实用工具。

### 3. **适用场景**
- **内容审核平台**：利用敏感词库和情感分析功能，对用户生成内容（UGC）进行实时过滤和风险评估。
- **智能客服与对话系统**：结合实体抽取、意图识别和聊天机器人数据集，构建具备上下文理解能力的客服机器人。
- **金融/法律/医疗行业分析**：使用领域专用词库和知识图谱工具，从专业文档中提取关键实体、关系和摘要。
- **NLP 研究与教育**：作为学习资源库，提供从基础分词到深度学习模型（如 BERT、GPT-2）的完整实践案例和代码。

### 4. **技术亮点**
- **一站式资源聚合**：不仅包含代码工具，还整合了清华 XLORE、百度、阿里等机构的高质量中文数据集和预训练模型。
- **多模型支持**：兼容 spaCy、Jieba、Transformers 等主流 NLP 框架，并提供神经网络的 NER、句法分析等实现。
- **领域垂直深化**：针对医疗、金融、汽车、法律等垂直领域提供专门的数据集和模型，提升行业应用精度。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82330 | 🍴 15271 | 语言: Python

### LlamaFactory
- 1. **中文简介**  
LlamaFactory 是一个统一且高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调训练，相关成果已发表于 ACL 2024。

2. **核心功能**  
- 支持 100+ 主流 LLM 和 VLM 的统一微调接口。  
- 提供 LoRA、QLoRA、GPTQ 等高效微调与量化技术。  
- 集成 RLHF（基于人类反馈的强化学习）和指令微调（instruction-tuning）。  
- 兼容 Transformers 生态，支持 PEFT 和 MoE 架构。  
- 内置对 DeepSeek、Gemma、Llama、Qwen 等模型的开箱即用支持。

3. **适用场景**  
- 快速对 Llama、Qwen 等模型进行 LoRA/QLoRA 高效微调。  
- 基于多模态 VLM 进行图像-文本联合指令微调。  
- 使用 RLHF 对齐模型输出以符合人类偏好。  
- 在资源受限环境下通过量化技术部署大型语言模型。

4. **技术亮点**  
- 统一框架兼容多种模型架构与微调策略，降低使用门槛。  
- 结合 ACL 2024 最新研究成果，兼顾效率与性能。  
- 对国产模型（如 DeepSeek、Qwen）及国际主流模型提供原生支持。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73899 | 🍴 9040 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. **中文简介**
AI-For-Beginners 是一个为期12周、包含24节课的人工智能入门课程，由微软开发者倡导团队打造，旨在让所有人轻松掌握AI知识。课程通过Jupyter Notebook形式呈现，覆盖从基础概念到深度学习、计算机视觉、自然语言处理等核心领域，适合零基础学习者系统入门。

---

### 2. **核心功能**
- **结构化课程路径**：12周24课时的分阶段学习计划，循序渐进讲解AI核心概念。  
- **实践导向内容**：所有课程以Jupyter Notebook形式提供，代码与理论结合，便于动手实践。  
- **多领域覆盖**：包含机器学习、深度学习、CNN、RNN、GAN、NLP等主流AI技术模块。  
- **开源免费资源**：完全开放的课程材料，支持全球学习者自由访问与二次创作。  
- **微软背书支持**：由微软开发者生态团队维护，内容质量与行业关联性有保障。  

---

### 3. **适用场景**
- **初学者系统学习**：无AI基础的学习者通过课程路径建立完整知识框架。  
- **高校/培训机构辅助教学**：教师可直接采用课程结构作为AI入门课程的补充教材。  
- **企业内训入门**：技术团队快速普及AI基础概念，降低后续专项培训门槛。  
- **自学者弹性学习**：学习者根据自身节奏灵活安排12周学习计划，兼顾理论与实践。  

---

### 4. **技术亮点**
- **微软开发者生态资源**：课程由微软教育团队开发，结合行业最佳实践与最新技术趋势。  
- **Jupyter Notebook集成**：所有代码示例可直接在浏览器中运行，无需复杂环境配置。  
- **多模态内容设计**：结合文本讲解、代码示例与可视化图表，适配不同学习风格。  
- **GitHub协作模式**：支持社区贡献与问题反馈，持续迭代优化课程内容。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63139 | 🍴 12245 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- **1. 中文简介**
掌握原理，从零构建，并将其交付给他人使用。这是一个全面的AI工程学习项目，涵盖从基础理论到实际部署的完整流程。

**2. 核心功能**
- 从零开始实现大语言模型（LLM）和生成式AI系统。
- 提供AI代理（Agents）、多智能体协作及模型上下文协议（MCP）的实战教程。
- 深入讲解计算机视觉、自然语言处理（NLP）和强化学习的底层原理。
- 结合Python与Rust语言，展示高性能AI基础设施的开发。

**3. 适用场景**
- 希望深入理解AI底层原理而非仅调用API的学习者。
- 致力于构建生产级AI应用和智能体系统的工程师。
- 需要系统性课程来掌握生成式AI和Transformer架构的学生或研究者。

**4. 技术亮点**
- 采用“先理解后构建”的教学理念，强调源码级实现。
- 覆盖前沿技术栈，包括Rust性能优化、Swarm Intelligence（群体智能）及MCP协议。
- 提供TypeScript和Python双语言支持，适配不同开发场景。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46222 | 🍴 7995 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK 及 TensorFlow 2 的综合学习项目。该项目旨在帮助学习者系统掌握人工智能与数据科学的核心技能。

2. **核心功能**
- 提供数据分析与机器学习的完整实战案例。
- 涵盖线性代数等数学基础知识的讲解与应用。
- 集成 PyTorch 和 TensorFlow 2 深度学习框架教程。
- 包含 NLTK 自然语言处理技术的学习内容。
- 实现多种经典算法如 SVM、KMeans、Adaboost 等。

3. **适用场景**
- 机器学习初学者系统学习算法理论与实践。
- 数据科学家提升数据分析与建模能力。
- 深度学习工程师掌握 PyTorch 和 TF2 实战技巧。
- NLP 研究者学习自然语言处理基础与应用。

4. **技术亮点**
项目整合了从传统机器学习到深度学习的完整技术栈，包含线性代数数学基础，并覆盖 Scikit-learn、PyTorch、TensorFlow 2 和 NLTK 等多款主流工具，适合构建系统化的人工智能知识体系。
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
- ⭐ 17350 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36029 | 🍴 7410 | 语言: 未知
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
- ⭐ 385469 | 🍴 81023 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268695 | 🍴 23997 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227046 | 🍴 44385 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199729 | 🍴 59996 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186288 | 🍴 46058 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166860 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164435 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162860 | 🍴 9170 | 语言: TypeScript
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

