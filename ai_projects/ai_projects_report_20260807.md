# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**
shuohao-skills 是一个专为 AI 编码代理（如 Claude Code 和 Codex）设计的技能集合。其中 novel-characters 模块可将小说内容转化为完整的人物设定集，包括人物画像、卡通形象提示词、音色提示词及三视图。

2. **核心功能**
- 支持 Claude Code 和 Codex 等主流 AI 编码代理运行。
- 自动将小说文本拆解并生成结构化的人物设定集。
- 提供卡通形象设计所需的视觉提示词。
- 生成角色配音所需的音色提示词。
- 输出角色三视图以辅助视觉创作。

3. **适用场景**
- AI 辅助小说改编动画或游戏时的角色设定标准化。
- 作家快速梳理和统一小说中多个人物的形象与声音特征。
- 利用 AI 编码代理自动化处理创意写作中的素材整理任务。
- 为插画师或 3D 建模师提供一致的角色视觉参考依据。

4. **技术亮点**
- 跨平台兼容性强，同时支持 Claude Code 和 Codex 两种不同的 AI 代理环境。
- 将非结构化的小说文本转化为多模态创作所需的结构化数据（文本、视觉、音频提示）。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 179 | 🍴 19 | 语言: JavaScript

### goal-flow
- 1. **中文简介**  
   goal-flow 是一个基于 LangGraph 的生产级 Agent 框架，结合工作流图与 Agent 循环。它可将 Dify DSL 编译为可执行代码，并支持在 Dify/OpenAI 协议间切换。

2. **核心功能**  
   - 基于 LangGraph 实现图编排的 Agent 循环  
   - 将 Dify DSL 转换为可运行代码  
   - 支持 Dify 与 OpenAI 协议互换  
   - 提供人机协同（Human-in-the-loop）能力  
   - 兼容 LangChain 生态

3. **适用场景**  
   - 需要将 Dify 工作流迁移至 LangGraph 的场景  
   - 构建支持多协议切换的生产级 AI Agent  
   - 需要人机交互控制的复杂工作流应用  
   - 基于 LangChain/LangGraph 的 Agentic 工程开发

4. **技术亮点**  
   - 无缝桥接 Dify DSL 与 LangGraph 执行环境  
   - 支持协议级灵活切换，提升部署适应性  
   - 原生集成 Human-in-the-loop 机制
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- **1. 中文简介**
该项目是为 GPT-5.6 / GPT-5.5 (Codex CLI) 设计的指令工程框架，旨在通过 CTF 竞赛心理框架重构运行上下文，从而规避模型的安全训练限制。它采用一键部署方式，包含 62 行提示词和 50 个技能模块，全部基于纯 Python 实现且无外部依赖。

**2. 核心功能**
- 通过 CTF 心理框架重构上下文，使模型的安全拒绝机制不被触发。
- 提供 50 个技能模块，支持对 AI 进行深度测试或“拷打”。
- 纯 Python 实现，零依赖，仅需 62 行提示词即可一键部署。
- 专注于突破常规指令限制，实现更自由的模型交互。

**3. 适用场景**
- 对 GPT-5.x 系列模型进行安全边界和指令跟随能力的极限测试。
- 研究提示词工程（Prompt Engineering）在绕过安全过滤方面的技术细节。
- CTF 竞赛中涉及 AI 安全或提示词注入的实战演练场景。
- 开发者希望在不依赖复杂环境的情况下快速部署定制化 AI 交互框架。

**4. 技术亮点**
- **零依赖轻量架构**：纯 Python 实现，无需安装额外库，部署极其简便。
- **心理框架重构**：创新性地引入 CTF 竞赛心理模型，从上下文层面而非对抗层面规避安全限制。
- **模块化技能集**：内置 50 个技能模块，提供系统化的“拷打”AI 能力。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- **中文简介**
lattice-script-executor 是一个跨平台的软件许可证管理工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能。

**核心功能**
- 支持 Windows、macOS 和 Linux 的跨平台许可证管理。
- 基于 AI 的规则引擎，实现智能化的许可证验证与策略执行。
- 提供离线种子验证机制，确保无网络环境下的授权安全性。
- 支持批量生成产品密钥，提升大规模部署效率。
- 记录不可篡改的审计日志，保障许可证操作的可追溯性。

**适用场景**
- 需要跨平台分发的桌面软件产品，希望统一管理许可证授权。
- 对许可证安全性要求较高的商业软件，需防范离线破解与密钥伪造。
- 面向企业客户的软件服务，需批量生成密钥并记录完整操作审计日志。
- 希望借助 AI 规则引擎动态调整许可证验证策略的开发者。

**技术亮点**
- 结合 AI 规则引擎与离线验证，兼顾智能化与安全性。
- 不可篡改审计日志设计，增强许可证系统的可信度与合规性。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- 1. **中文简介**  
该项目暂无描述信息，无法提供中文简介。

2. **核心功能**  
无法确定，因项目描述为空。

3. **适用场景**  
无法确定，因项目描述为空。

4. **技术亮点**  
暂无可识别的技术亮点。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 34 | 🍴 11 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 29 | 🍴 3 | 语言: 未知

### ai-novel-screenplay-analyzer
- 描述: 面向长篇小说、剧本与改编项目的 AI 叙事分析工作台，自动梳理人物关系、章节脉络与关系演化，支持多模型接入、任务断点恢复及本地私有部署。
- 链接: https://github.com/ops120/ai-novel-screenplay-analyzer
- ⭐ 24 | 🍴 1 | 语言: JavaScript

### daily-global-market-intelligence-description-skills
- 描述: 提供每日股市新闻、财经早餐、盘前/盘后复盘、美股、A股、港股、韩股、全球市场走势、宏观经济、AI板块、半导体、资金流向、市场情绪、财报、ETF、行业轮动、大宗商品、加密货币等内容时触发。提供机构级全球市场日报
- 链接: https://github.com/morangse/daily-global-market-intelligence-description-skills
- ⭐ 22 | 🍴 0 | 语言: 未知

### AI-Photographer-Agent-ROCm
- 描述: Private local AI Photographer Agent on AMD Radeon and ROCm
- 链接: https://github.com/yang13926151198-ai/AI-Photographer-Agent-ROCm
- ⭐ 21 | 🍴 0 | 语言: Python
- 标签: ai-agent, amd-rocm, multimodal-ai, photography, qwen2-vl

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 20 | 🍴 2 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个基于 Python 的综合性中文自然语言处理工具包，主要提供中英文敏感词检测、语言识别、手机号/身份证/邮箱抽取等基础 NLP 功能。该项目还收录了海量的中文词库、预训练模型资源及各类 NLP 数据集，是中文 NLP 开发者的实用资源库。

2. **核心功能**
- 提供敏感词过滤、语言检测及手机号、身份证、邮箱等个人信息抽取功能。
- 集成中外手机号归属地查询、名字推断性别及繁简体转换等实用工具。
- 收录大量中文词库（如成语、地名、人名、行业术语）及情感值、停用词等资源。
- 汇总了 BERT、GPT 等预训练模型及各类 NLP 竞赛方案、数据集和开源工具。
- 支持中文分词、词性标注、命名实体识别（NER）、情感分析及文本摘要等处理任务。

3. **适用场景**
- 内容安全审核：用于识别文本中的敏感词、暴恐词及谣言，保障平台内容合规。
- 信息抽取与结构化：从非结构化文本中自动提取手机号、身份证、邮箱等关键实体信息。
- NLP 资源检索与学习：作为中文 NLP 学习者的资源索引，快速查找数据集、模型和算法实现。
- 智能客服与对话系统：利用其提供的聊天语料、问答数据集及对话系统工具构建智能机器人。

4. **技术亮点**
- 资源极其丰富，涵盖了从基础工具到前沿模型（如 BERT、ALBERT）的全方位 NLP 资源。
- 专注于中文场景，提供了大量针对中文特性的词库、数据集及优化后的处理工具（如 jieba_fast）。
- 兼具实用工具与学术资源双重属性，既包含开箱即用的代码库，也汇总了顶级会议论文和竞赛方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
该项目是一个包含500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目以Python为主要实现语言，适合希望快速上手并实践AI技术的开发者学习。

2. **核心功能**  
- 提供500个AI项目的完整代码实现，覆盖多个主流技术领域。  
- 包含丰富的实战案例，帮助开发者从理论到实践全面掌握AI技能。  
- 适用于不同层次的学习者，从入门到进阶均有适合的项目。  
- 所有项目均标注清晰，便于按领域或难度快速筛选。  
- 支持多场景应用，包括图像识别、文本处理、预测分析等。

3. **适用场景**  
- AI初学者希望通过实际项目快速掌握机器学习与深度学习的基础技能。  
- 研究人员或工程师需要参考现成代码解决特定领域的AI问题。  
- 教育者可以将项目作为课程素材，用于教学或培训。  
- 企业团队可以借鉴项目思路，加速内部AI解决方案的开发。

4. **技术亮点**  
- 项目数量庞大且分类清晰，便于针对性学习和应用。  
- 代码实现规范，注释详尽，易于理解和复用。  
- 覆盖当前AI领域的主流技术和工具，具有实用性和前瞻性。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架和模型格式，帮助用户直观地查看和理解模型结构。

### 2. 核心功能
- 支持多种模型格式（如 ONNX、TensorFlow、PyTorch、CoreML 等）的可视化展示。
- 提供清晰的模型架构视图，便于分析层与层之间的连接关系。
- 兼容 JavaScript 技术栈，可在浏览器中直接运行，无需安装额外软件。
- 支持 safetensors 等新兴格式，适应快速发展的 AI 生态需求。
- 界面简洁友好，适合快速调试和展示模型设计。

### 3. 适用场景
- 研究人员或开发者用于调试和优化神经网络模型结构。
- 教育场景中帮助学生理解复杂机器学习模型的内部机制。
- 跨平台协作时，通过可视化的方式分享模型设计方案。
- 将模型部署到不同框架前，检查模型兼容性和完整性。

### 4. 技术亮点
- 基于 JavaScript 实现，无需依赖本地环境即可运行。
- 广泛支持主流深度学习框架及其衍生格式。
- 开源项目，社区活跃，持续更新以适配新技术。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开放的机器学习互操作标准，旨在促进不同深度学习框架之间的模型迁移与部署。它允许开发者轻松地将模型从训练框架（如PyTorch、TensorFlow）转换到推理引擎，实现跨平台的高效运行。

### 2. 核心功能
- 提供统一的模型表示格式，支持主流深度学习框架间的模型互转。
- 兼容多种硬件平台，优化模型在CPU、GPU及边缘设备上的推理性能。
- 支持复杂的神经网络结构，包括卷积、循环、注意力机制等常见算子。
- 提供丰富的工具链，包括模型转换、验证、可视化和性能分析功能。
- 促进开源生态协作，由Linux基金会支持并拥有广泛的社区贡献。

### 3. 适用场景
- **模型部署优化**：将PyTorch或TensorFlow训练好的模型转换为ONNX格式，以便在生产环境中高效推理。
- **跨框架迁移**：在不同深度学习框架间迁移模型，避免重新训练，节省时间和计算资源。
- **边缘设备部署**：将大型模型压缩并转换为轻量级ONNX格式，部署到移动设备或嵌入式系统。
- **模型性能分析**：利用ONNX工具链对模型结构进行可视化分析，识别瓶颈并优化性能。

### 4. 技术亮点
- **开放标准**：由Linux基金会主导，确保技术中立性和广泛兼容性。
- **生态整合**：与TensorRT、ONNX Runtime等主流推理引擎深度集成，提供端到端解决方案。
- **社区活跃**：拥有超过21,000个GitHub星标，表明其在机器学习社区的广泛认可和使用。
- 链接: https://github.com/onnx/onnx
- ⭐ 21277 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- **1. 中文简介**
这是一本关于机器学习工程实践的开源指南，涵盖从模型训练到部署的全流程技术。项目聚焦于大规模语言模型（LLM）的训练、调试、推理优化等核心工程问题。

**2. 核心功能**
- 提供PyTorch和Transformer库的大规模训练最佳实践
- 涵盖GPU集群管理、Slurm调度、网络优化等基础设施知识
- 详解LLM推理加速、模型调试、存储优化等工程技巧
- 包含MLOps全流程指南，从训练到部署的完整解决方案
- 提供可扩展性设计和大规模分布式训练实践

**3. 适用场景**
- 需要训练大规模语言模型（如GPT、LLaMA等）的工程团队
- 使用GPU集群进行深度学习训练的研究机构和公司
- 希望优化模型推理性能和降低成本的AI工程师
- 搭建和维护机器学习生产环境的MLOps团队

**4. 技术亮点**
- 由社区贡献的实战经验总结，非理论教材
- 覆盖从单卡训练到千卡集群的完整技术栈
- 包含大量实际调试案例和性能优化技巧
- 持续更新，紧跟AI工程领域最新实践
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
该项目是一个包含500个AI项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它提供完整的代码实现，适合希望动手实践的学习者和开发者。

2. **核心功能**
- 提供500个AI相关项目的完整代码示例
- 覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均包含可运行的代码实现
- 项目分类清晰，便于按领域查找学习
- 适合从入门到进阶的系统性实践

3. **适用场景**
- AI初学者系统学习机器学习到深度学习的完整路径
- 数据科学家寻找实际项目案例参考
- 开发者快速构建AI应用原型
- 学生完成课程项目或毕业设计的灵感来源

4. **技术亮点**
- 项目数量庞大（500个），覆盖AI主要子领域
- 所有项目均附带可执行代码，而非仅理论说明
- 使用Python实现，生态成熟且易上手
- 获得36000+星标，社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架和模型格式，帮助用户直观地查看和理解模型结构。

### 2. 核心功能
- 支持多种模型格式（如 ONNX、TensorFlow、PyTorch、CoreML 等）的可视化展示。
- 提供清晰的模型架构视图，便于分析层与层之间的连接关系。
- 兼容 JavaScript 技术栈，可在浏览器中直接运行，无需安装额外软件。
- 支持 safetensors 等新兴格式，适应快速发展的 AI 生态需求。
- 界面简洁友好，适合快速调试和展示模型设计。

### 3. 适用场景
- 研究人员或开发者用于调试和优化神经网络模型结构。
- 教育场景中帮助学生理解复杂机器学习模型的内部机制。
- 跨平台协作时，通过可视化的方式分享模型设计方案。
- 将模型部署到不同框架前，检查模型兼容性和完整性。

### 4. 技术亮点
- 基于 JavaScript 实现，无需依赖本地环境即可运行。
- 广泛支持主流深度学习框架及其衍生格式。
- 开源项目，社区活跃，持续更新以适配新技术。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
本项目为深度学习与机器学习研究者精心整理的必备速查手册。内容涵盖人工智能、深度学习、Keras、NumPy、SciPy及Matplotlib等核心领域的关键知识点，是快速回顾和查阅技术细节的实用工具。

**2. 核心功能**
- 提供深度学习与机器学习领域的基础概念速查表。
- 整理Keras、NumPy、SciPy等常用库的关键函数与用法。
- 包含Matplotlib数据可视化的核心技巧与代码示例。
- 针对研究人员优化的精简知识点汇总，便于快速检索。

**3. 适用场景**
- 深度学习初学者快速回顾核心概念与工具用法。
- 研究人员在实验过程中查阅特定函数或参数配置。
- 面试准备或技术分享时作为知识点的快速参考指南。

**4. 技术亮点**
- 高度浓缩的核心知识点，避免冗余信息，提升查阅效率。
- 覆盖从理论概念到代码实现（如Keras、NumPy）的完整技术栈。
- 由社区广泛认可（高星标数），内容经过实践验证，可靠性高。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### Ai-Learn 项目分析

**1. 中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，适合零基础入门及就业实战。内容涵盖Python、数学、机器学习、数据分析、深度学习、计算机视觉和自然语言处理等热门领域，支持TensorFlow、PyTorch、Keras等多种主流框架。

**2. 核心功能**
*   提供系统化的AI学习路线图，从零基础引导至就业实战。
*   收录近200个实战案例与项目，配套免费教材资源。
*   覆盖机器学习、深度学习、NLP、CV等多领域核心技术栈。
*   支持Python生态及主流深度学习框架（TensorFlow、PyTorch、Keras等）。

**3. 适用场景**
*   初学者系统学习人工智能与数据科学基础知识。
*   求职者通过实战项目提升技能，准备AI相关岗位面试。
*   开发者查阅特定领域（如NLP、CV）的实战案例与代码参考。
*   教育者或自学者寻找结构化的学习路径与免费教材资源。

**4. 技术亮点**
*   项目高度集成，涵盖从数学基础到深度学习框架的完整技术栈。
*   实战导向，提供大量可直接复现的案例，强化动手能力。
*   社区活跃度高（13,234星标），资源丰富且持续更新。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它旨在简化机器学习模型的训练、微调与部署流程，降低 AI 开发门槛。

### 2. 核心功能
- **低代码开发**：通过声明式配置即可快速构建和训练深度学习模型，无需编写大量代码。
- **多模态支持**：原生支持文本、图像、表格等多种数据类型，适用于计算机视觉与自然语言处理任务。
- **LLM 微调集成**：内置对 Llama、Mistral 等主流大语言模型的支持，便于进行高效微调（Fine-tuning）。
- **数据为中心的工作流**：提供端到端的数据预处理、模型训练与评估管道，强调数据质量与迭代效率。
- **PyTorch 后端**：基于 PyTorch 构建，兼容主流深度学习生态，便于扩展与集成。

### 3. 适用场景
- **企业级 AI 应用快速原型**：希望以最小代码量快速验证 AI 想法的数据科学家或工程师。
- **大语言模型定制微调**：需要对 Llama、Mistral 等开源 LLM 进行领域适配或任务特定优化的场景。
- **多模态模型开发**：同时处理文本、图像和结构化数据的复杂 AI 项目。
- **数据-centric AI 实践**：注重数据质量、版本控制与迭代优化的机器学习工作流。

### 4. 技术亮点
- 将复杂深度学习流程抽象为 YAML/JSON 配置，显著提升开发效率。
- 内置可视化训练监控与实验管理功能，便于模型迭代对比。
- 支持分布式训练与生产级部署，兼顾灵活性与可扩展性。
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
funNLP 是一个基于 Python 的综合性中文自然语言处理工具包，主要提供中英文敏感词检测、语言识别、手机号/身份证/邮箱抽取等基础 NLP 功能。该项目还收录了海量的中文词库、预训练模型资源及各类 NLP 数据集，是中文 NLP 开发者的实用资源库。

2. **核心功能**
- 提供敏感词过滤、语言检测及手机号、身份证、邮箱等个人信息抽取功能。
- 集成中外手机号归属地查询、名字推断性别及繁简体转换等实用工具。
- 收录大量中文词库（如成语、地名、人名、行业术语）及情感值、停用词等资源。
- 汇总了 BERT、GPT 等预训练模型及各类 NLP 竞赛方案、数据集和开源工具。
- 支持中文分词、词性标注、命名实体识别（NER）、情感分析及文本摘要等处理任务。

3. **适用场景**
- 内容安全审核：用于识别文本中的敏感词、暴恐词及谣言，保障平台内容合规。
- 信息抽取与结构化：从非结构化文本中自动提取手机号、身份证、邮箱等关键实体信息。
- NLP 资源检索与学习：作为中文 NLP 学习者的资源索引，快速查找数据集、模型和算法实现。
- 智能客服与对话系统：利用其提供的聊天语料、问答数据集及对话系统工具构建智能机器人。

4. **技术亮点**
- 资源极其丰富，涵盖了从基础工具到前沿模型（如 BERT、ALBERT）的全方位 NLP 资源。
- 专注于中文场景，提供了大量针对中文特性的词库、数据集及优化后的处理工具（如 jieba_fast）。
- 兼具实用工具与学术资源双重属性，既包含开箱即用的代码库，也汇总了顶级会议论文和竞赛方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行微调，相关研究已发表于 ACL 2024。该项目旨在降低大模型微调的技术门槛，提供一站式解决方案。

2. **核心功能**
- 支持 100+ 种主流 LLM 和 VLM 的统一微调，兼容 LLaMA、Qwen、DeepSeek、Gemma 等模型。
- 提供多种高效微调方法，包括 LoRA、QLoRA、全参数微调及 RLHF 等。
- 支持多模态训练，可同时处理文本和图像输入。
- 内置量化技术（如 4/8-bit 量化），显著降低显存占用并提升推理效率。
- 提供友好的 Web UI 界面和命令行工具，简化微调流程。

3. **适用场景**
- 研究人员和开发者希望对多种大模型进行快速实验和基准测试。
- 需要在有限显存资源下对大模型进行高效微调（如使用 QLoRA）。
- 企业或个人希望构建基于多模态大模型的应用，如图像理解问答系统。
- 希望简化 RLHF（人类反馈强化学习）流程以优化模型对齐。

4. **技术亮点**
- 统一架构支持超 100 种模型，无需为不同模型编写专用代码。
- 高度优化的训练效率，结合量化技术可实现单卡微调大模型。
- 完整的生态支持，涵盖指令微调、偏好对齐及多模态训练。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73897 | 🍴 9042 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. **中文简介**
这是一个为期12周、包含24节课程的全面人工智能入门课程，由微软开发者倡导团队打造。课程涵盖机器学习、深度学习、自然语言处理及计算机视觉等核心领域，旨在让所有学习者都能轻松掌握AI技术。

### 2. **核心功能**
- 提供结构化的12周学习路径，适合零基础学习者系统入门。
- 涵盖机器学习、深度学习、NLP、计算机视觉（CNN）、生成对抗网络（GAN）及循环神经网络（RNN）等核心主题。
- 基于Jupyter Notebook实现，支持交互式代码练习与即时反馈。
- 由微软开发者团队维护，内容权威且紧跟技术发展趋势。
- 完全免费开源，社区活跃，适合自学与团队协作学习。

### 3. **适用场景**
- 高校或培训机构用于人工智能基础课程教学。
- 开发者或数据科学初学者自学AI入门知识。
- 企业内训中用于提升团队对AI技术的理解与应用能力。
- 技术爱好者通过实践项目快速构建AI知识体系。

### 4. **技术亮点**
- 课程内容由微软开发者倡导团队精心设计，兼具理论深度与实践导向。
- 采用Jupyter Notebook形式，支持代码即时运行与结果可视化，提升学习效率。
- 覆盖主流AI技术栈（ML/DL/NLP/CV），并引入GAN等前沿主题，内容全面且前沿。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63104 | 🍴 12241 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- # ai-engineering-from-scratch 项目分析

## 1. 中文简介
从零开始学习、构建并交付AI工程实践课程。通过亲手实现核心AI组件，深入掌握从基础原理到生产级应用的完整技术栈。

## 2. 核心功能
- 从零构建LLM、Transformer等核心AI组件的完整教程
- 涵盖AI代理、强化学习、计算机视觉等前沿领域
- 提供可部署的生产级代码示例和实践项目
- 支持Python和Rust双语言实现
- 包含MCP（模型上下文协议）等最新AI工程标准

## 3. 适用场景
- AI工程师系统学习深度学习底层原理
- 研究人员实现和验证AI算法原型
- 团队搭建AI代理和智能体系统
- 开发者构建生成式AI应用的生产环境

## 4. 技术亮点
- 46,205+星标的高人气开源课程项目
- 覆盖从基础机器学习到前沿Agent的完整学习路径
- 强调"动手实践"的教学理念，注重代码实现
- 跨语言支持（Python + Rust），兼顾易用性与性能
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46205 | 🍴 7993 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch 及 NLTK 和 TensorFlow 2 的综合学习资源库。该项目旨在帮助开发者系统性地掌握从基础数学理论到深度学习框架的完整技术栈。

2. **核心功能**
- 提供机器学习经典算法（如 SVM、KMeans、Adaboost）的 Python 实现与解析。
- 包含自然语言处理（NLP）实战内容，涵盖 NLTK 工具包及 RNN/LSTM 模型应用。
- 集成深度学习框架教程，重点讲解 PyTorch 和 TensorFlow 2 的实战开发。
- 补充线性代数等机器学习必备数学基础，帮助构建扎实的理论体系。
- 涵盖推荐系统、关联规则挖掘（Apriori、FP-Growth）等进阶应用场景。

3. **适用场景**
- 机器学习初学者系统学习从数学基础到算法实现的完整路径。
- 需要快速复现经典 ML/DL 算法以用于项目原型开发的工程师。
- 希望深入理解 NLP 技术（如文本分类、序列模型）的研究人员。
- 准备技术面试，需要梳理算法原理与代码实现的求职者。

4. **技术亮点**
- 项目星标数高达 42442，表明其在中文社区具有极高的认可度和广泛的影响力。
- 内容覆盖全面，从传统机器学习到前沿深度学习均有涉及，适合作为一站式学习资源。
- 代码实现清晰，结合 sklearn、PyTorch 等主流库，便于读者直接上手实践。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42442 | 🍴 11524 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33811 | 🍴 4705 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28975 | 🍴 3531 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21822 | 🍴 3340 | 语言: Python
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
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22706 | 🍴 2137 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16478 | 🍴 3793 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12947 | 🍴 1703 | 语言: Python
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
- ⭐ 385466 | 🍴 81023 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268638 | 🍴 23995 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227000 | 🍴 44361 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199708 | 🍴 59989 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186259 | 🍴 46058 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166858 | 🍴 21539 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164433 | 🍴 30559 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162785 | 🍴 9166 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157606 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152924 | 🍴 9826 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

