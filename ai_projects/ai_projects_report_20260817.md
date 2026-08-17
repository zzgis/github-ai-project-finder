# GitHub AI项目每日发现报告
日期: 2026-08-17

## 新发布的AI项目

### cumora
- 

# cumora 项目分析

## 1. 中文简介
cumora 是一个跨平台团队聊天应用，让 AI 代理成为团队中的平等成员。它支持云端 AI 或用户自带 AI 大脑（如 Claude Code / Codex），为 AI 代理协作提供统一平台。

## 2. 核心功能
- 跨平台团队聊天，支持多设备同步
- AI 代理作为一等公民参与团队协作
- 支持云端 AI 服务与自带 AI 大脑（Claude Code / Codex）
- 提供灵活的 AI 集成方案，用户可自主选择算力来源

## 3. 适用场景
- 需要 AI 代理协助完成团队协作任务的技术团队
- 希望统一管理多个 AI 代理的开发者或企业
- 追求隐私可控、希望自带 AI 算力的团队
- 跨平台办公环境中需要 AI 辅助协作的场景

## 4. 技术亮点
- 采用 TypeScript 开发，代码质量与可维护性较高
- 支持多种 AI 后端接入，灵活适配不同需求
- 跨平台架构设计，覆盖主流操作系统
- 链接: https://github.com/yetone/cumora
- ⭐ 680 | 🍴 72 | 语言: TypeScript

### zhijian-ai-bluebook-workbuddy-harness
- 

## 项目分析：zhijian-ai-bluebook-workbuddy-harness

### 1. 中文简介
本项目是智见 AI 蓝皮书系列之一，专注于深度拆解 WorkBuddy AI Agent 的核心架构。内容涵盖提示词设计、记忆机制、插件系统、专家模块、Skill 能力以及安全边界等关键技术点。

### 2. 核心功能
- **提示词工程**：解析 WorkBuddy 的提示词设计与优化策略
- **记忆系统**：拆解 AI Agent 的记忆管理与上下文维护机制
- **插件架构**：分析插件系统的扩展能力与集成方式
- **专家模块**：研究专家系统的角色分配与协同机制
- **安全边界**：明确 Agent 的能力边界与安全控制策略

### 3. 适用场景
- AI Agent 框架学习与架构参考
- 企业级智能助手开发设计
- 提示词工程与记忆系统设计实践
- AI 安全边界研究与合规控制

### 4. 技术亮点
- 系统性拆解 WorkBuddy 全链路技术栈
- 聚焦 Agent 核心能力模块的深度解析
- 结合安全边界设计，兼顾功能与风险控制
- 链接: https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness
- ⭐ 148 | 🍴 14 | 语言: 未知
- 标签: ai-agent, bluebook, harness, workbuddy, zhijian-ai

### ai-data-extractor
- 

# GitHub项目分析：ai-data-extractor

## 1. 中文简介
这是一个免费开源的AI编程助手聊天记录提取工具，支持Claude Code、Cursor、Windsurf、Aider、Cline/Roo Code等多个主流AI编程平台，帮助用户轻松导出和整理AI辅助编程的历史对话数据。

## 2. 核心功能
- 支持多平台聊天记录提取，涵盖Claude Code、Cursor、Windsurf、Aider、Cline/Roo Code等主流AI编程助手
- 提供免费的开源解决方案，无需付费即可导出AI编程对话历史
- 采用Python语言开发，便于跨平台使用和二次开发
- 帮助用户将分散在不同AI工具中的编程对话数据进行统一提取和管理

## 3. 适用场景
- 开发者需要备份或迁移不同AI编程助手的历史对话记录
- 团队希望汇总多个成员使用AI工具产生的编程经验和解决方案
- 用户想整理AI辅助编程的学习轨迹，便于回顾和知识沉淀
- 数据分析师需要研究AI编程助手的交互模式和输出质量

## 4. 技术亮点
- 项目标签显示支持Gemini，表明其兼容Google的AI编程生态
- 79个星标说明项目已有一定的社区关注度和认可度
- 开源免费定位降低了用户使用门槛，适合个人开发者和小型团队
- 链接: https://github.com/bawadou/ai-data-extractor
- ⭐ 79 | 🍴 29 | 语言: Python
- 标签: ai, ai-data-extractor, claude, cursor, cursor-ai

### graph-memory-starter
- 

## 项目分析：graph-memory-starter

---

### 1. 中文简介

该项目为AI助手提供基于知识图谱的记忆功能。通过三个SQLite表存储实体与关系，结合递归查询实现知识推理，并可通过提示钩子将记忆内容注入AI对话流程中。

---

### 2. 核心功能

- **知识图谱记忆存储**：使用三个SQLite表存储AI助手的记忆实体、关系及属性数据。
- **递归查询能力**：通过单一递归SQL查询实现知识图谱的遍历与关联推理。
- **提示钩子集成**：提供prompt hook机制，将图谱记忆动态注入AI助手的提示词中。
- **轻量级架构**：仅依赖SQLite，无需额外数据库服务，部署简单。
- **Python原生开发**：使用Python实现，易于集成到现有AI应用项目中。

---

### 3. 适用场景

- **AI对话助手**：为聊天机器人提供长期记忆，使其能够记住用户偏好和历史交互。
- **智能客服系统**：存储客户信息与服务历史，支持上下文感知的个性化回复。
- **知识问答机器人**：基于图谱关系进行多跳推理，回答需要关联多个实体信息的复杂问题。

---

### 4. 技术亮点

- **极简设计**：仅用三张表和一条递归查询即实现知识图谱记忆，结构清晰、易于理解和扩展。
- **SQLite零配置**：无需安装额外数据库，单机即可运行，适合轻量级部署场景。
- **Prompt Hook机制**：将图谱记忆无缝注入AI提示流程，使模型具备"记忆"能力而无需修改模型本身。
- 链接: https://github.com/Glitch-Cat-Club/graph-memory-starter
- ⭐ 64 | 🍴 8 | 语言: Python

### bigpeng-hot-gzh
- 

## GitHub 项目分析：bigpeng-hot-gzh

### 1. 中文简介
本项目从约100篇爆款AI公众号文章中提炼出选题与标题的写作技巧，帮助内容创作者掌握热门文章的创作规律。项目以Skill（技能/方法论）的形式呈现，便于直接应用于实际写作。

### 2. 核心功能
- 总结爆款AI公众号文章的选题方向与规律
- 提炼高点击率标题的写作模板与技巧
- 提供可复用的内容创作方法论（Skill）
- 帮助创作者快速定位热门话题切入点

### 3. 适用场景
- AI领域公众号/自媒体运营者寻找选题灵感
- 新媒体内容创作者学习爆款标题写法
- 内容团队批量生产AI相关文章时参考选题方向
- 对AI话题感兴趣但不知如何切入的写作新手

### 4. 技术亮点
- 基于真实爆款数据提炼，方法论具有实战参考价值
- 以Skill形式呈现，便于直接迁移应用到写作流程中
- 聚焦垂直领域（AI公众号），针对性强，实用度高
- 链接: https://github.com/BigPengSays/bigpeng-hot-gzh
- ⭐ 53 | 🍴 5 | 语言: 未知

### deepseek-harness-pr-review
- 描述: AI code review with DeepSeek: headless PR review automation that verifies PR descriptions claim-by-claim against real code, checks docs against reality, flags requirement impact, human-in-the-loop + auto review poller + web dashboard
- 链接: https://github.com/nexpeakcore/deepseek-harness-pr-review
- ⭐ 34 | 🍴 12 | 语言: Python
- 标签: agentic-ai, ai-agent, ai-code-review, automation, automation-tools

### ai-tools-radar
- 描述: AI 工具站增长情报库:真实流量/增长曲线/新品雷达/dofollow 外链库 · Growth intelligence for AI tools, runs locally
- 链接: https://github.com/ppop123/ai-tools-radar
- ⭐ 31 | 🍴 21 | 语言: Python

### idor-tester-ai
- 描述: 无描述
- 链接: https://github.com/poriaporhashemi/idor-tester-ai
- ⭐ 29 | 🍴 7 | 语言: Python

### dance-video-to-prompt
- 描述: 本地短视频反推 AI 视频生成提示词：抽帧、清晰度、节奏卡点、Agent Skill
- 链接: https://github.com/CattleZ/dance-video-to-prompt
- ⭐ 27 | 🍴 1 | 语言: Python

### Alvarmethod
- 描述: One-to-one AI teaching skills (Alvar method) for Codex, Claude Code, Grok, Pi, and OpenCode
- 链接: https://github.com/vasanthsreeram/Alvarmethod
- ⭐ 25 | 🍴 3 | 语言: Shell

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP 是一个全面的中文自然语言处理资源集合，涵盖了从基础工具到高级模型的完整解决方案。项目整合了敏感词检测、信息抽取、词库资源、预训练模型以及大量中文NLP数据集，为中文NLP研究和应用提供了一站式资源平台。

## 2. 核心功能

- **基础NLP工具**：中英文敏感词检测、语言检测、手机号/电话归属地查询、名字推断性别、信息抽取（手机号、身份证、邮箱）
- **丰富词库资源**：中日文人名库、中文缩写库、词汇情感值、停用词、反动词表、暴恐词表、同义词/反义词/否定词库、各领域专业词库（医学、法律、汽车等）
- **预训练模型与算法**：BERT/ALBERT/GPT-2等中文预训练模型、中文词向量、句子相似度匹配、文本生成与摘要工具
- **大规模数据集**：中文聊天语料、百度问答数据集、中文谣言数据、医疗对话数据、知识图谱数据等
- **高级NLP应用**：命名实体识别、关系抽取、知识图谱构建、智能问答系统、语音识别与合成

## 3. 适用场景

- **中文文本处理与清洗**：敏感词过滤、信息抽取、繁简转换、文本纠错等数据处理任务
- **NLP模型训练与微调**：利用预训练模型和大规模中文数据集进行文本分类、NER、关系抽取等任务
- **知识图谱构建**：通过实体抽取、关系抽取工具构建中文领域知识图谱
- **
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82512 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个汇集500个AI、机器学习、深度学习和自然语言处理项目的资源库，涵盖计算机视觉、NLP等多个领域。所有项目均附带代码实现，适合从入门到进阶的学习者参考使用。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大领域
- 每个项目均标注所属分类和难度等级
- 包含实际应用场景的完整案例
- 持续更新最新AI项目和技术趋势

### 3. 适用场景
- AI初学者系统学习各方向实战项目
- 研究人员快速参考同类项目实现方案
- 开发者寻找特定场景的代码模板和灵感
- 企业技术选型时对比不同实现方案

### 4. 技术亮点
- 项目分类清晰，按领域和难度精准标注
- 包含大量工业级实际应用案例
- 代码质量较高，可直接运行参考
- 星标数超过3.6万，社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36334 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33363 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习领域的开放互操作标准，旨在实现不同深度学习框架之间的模型兼容与转换。它允许开发者在不同平台（如 PyTorch、TensorFlow、Keras 等）之间无缝迁移模型，提升模型部署的灵活性和效率。

### 2. 核心功能
- **跨框架模型转换**：支持将模型从 PyTorch、TensorFlow、Keras 等框架导出为 ONNX 格式，并可在不同框架间互相转换。
- **统一模型表示**：提供标准化的模型定义格式，确保模型结构和参数在不同环境中保持一致。
- **推理引擎兼容**：可与 ONNX Runtime 等推理引擎配合，实现高效跨平台推理。
- **生态工具支持**：提供模型检查、转换、优化工具链，方便开发者调试和优化模型。

### 3. 适用场景
- **模型部署**：将在开发框架中训练的模型部署到生产环境，如移动端、嵌入式设备或云端服务。
- **框架迁移**：从 PyTorch 迁移到 TensorFlow 或反之，便于团队使用不同框架协作。
- **性能优化**：利用 ONNX 优化工具对模型进行剪枝、量化，提升推理速度并减少资源消耗。
- **跨平台推理**：在支持 ONNX 的不同硬件平台（如 CPU、GPU、NPU）上运行同一模型。

### 4. 技术亮点
- **开放标准**：由 Microsoft、Facebook 等科技巨头联合推动，已成为工业界广泛采用的模型交换标准。
- **丰富的算子支持**：覆盖主流深度学习算子，兼容 CNN、RNN、Transformer 等多种网络结构。
- **与主流框架深度集成**：PyTorch、TensorFlow、scikit-learn 等均可直接导出 ONNX 模型，生态成熟。
- 链接: https://github.com/onnx/onnx
- ⭐ 21319 | 🍴 4000 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub 项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践知识的开源资源库，内容涵盖从模型训练、调试到推理部署的全链路技术。该项目为 AI 工程师和研究人员提供了一套系统性的实践指南，帮助读者掌握大规模机器学习系统的构建与优化方法。

## 2. 核心功能
- 提供大规模语言模型（LLM）训练与微调的完整工程实践指南
- 详解 GPU 集群管理、SLURM 调度及分布式训练的最佳实践
- 覆盖模型推理优化、网络通信和存储系统等关键基础设施技术
- 包含 PyTorch 框架下的调试技巧与可扩展性设计模式
- 整合 MLOps 工作流，支持从实验到生产的全生命周期管理

## 3. 适用场景
- 构建和训练大规模语言模型（如基于 Transformers 的 LLM）
- 在超算集群上使用 SLURM 管理分布式 GPU 训练任务
- 优化模型推理性能，降低延迟并提升吞吐量
- 搭建企业级 MLOps 平台，实现模型训练到部署的自动化流程

## 4. 技术亮点
- 聚焦实际工程问题，内容覆盖 GPU 调试、网络优化和存储设计等深层技术细节
- 结合 PyTorch 和 Transformers 生态，提供可落地的代码级实践指导
- 针对可扩展性（Scalability）问题给出系统化解决方案，适合大规模生产环境
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18646 | 🍴 1201 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17359 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13261 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11627 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10687 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个汇集500个AI、机器学习、深度学习和自然语言处理项目的资源库，涵盖计算机视觉、NLP等多个领域。所有项目均附带代码实现，适合从入门到进阶的学习者参考使用。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大领域
- 每个项目均标注所属分类和难度等级
- 包含实际应用场景的完整案例
- 持续更新最新AI项目和技术趋势

### 3. 适用场景
- AI初学者系统学习各方向实战项目
- 研究人员快速参考同类项目实现方案
- 开发者寻找特定场景的代码模板和灵感
- 企业技术选型时对比不同实现方案

### 4. 技术亮点
- 项目分类清晰，按领域和难度精准标注
- 包含大量工业级实际应用案例
- 代码质量较高，可直接运行参考
- 星标数超过3.6万，社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36334 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33363 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介

该项目为深度学习与机器学习研究者提供了一系列核心速查手册（Cheat Sheets），涵盖常用库、框架和算法的关键知识点，是快速查阅技术细节的实用工具集。

---

### 2. 核心功能

- 提供深度学习与机器学习领域的常用速查表，涵盖 NumPy、SciPy、Matplotlib 等核心库
- 包含 Keras 框架的常用 API 与操作速查，便于快速上手和查阅
- 覆盖机器学习经典算法的关键公式与实现要点
- 以简洁的图文形式呈现，适合快速检索和复习

---

### 3. 适用场景

- 深度学习研究者快速查阅框架 API 和数学公式
- 机器学习工程师在项目开发中作为参考手册
- 学生复习和巩固深度学习核心知识体系
- 技术面试前快速回顾关键概念与代码片段

---

### 4. 技术亮点

- 由 Medium 技术博主整理，内容经过实践验证，权威性强
- 覆盖从基础库（NumPy/SciPy）到高级框架（Keras）的完整技术栈
- 星标数超过 15,000，社区认可度高，持续更新维护
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个人工智能学习路线图项目，整理了近200个实战案例与项目，并提供免费配套教材，帮助零基础学习者入门并提升就业竞争力。项目涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门技术领域。

### 2. 核心功能
- 提供系统化的AI学习路线图，从零开始逐步进阶
- 收录近200个实战案例和项目，配套免费教材
- 覆盖机器学习、深度学习、数据分析等主流技术栈
- 支持多种主流框架，包括PyTorch、TensorFlow、Keras等
- 包含数学基础、算法、数据处理等前置知识学习资源

### 3. 适用场景
- 零基础转行AI领域的学习者，需要系统入门路径
- 在校学生或求职者，希望通过实战项目提升就业竞争力
- 希望系统学习机器学习/深度学习技术的开发者
- 需要参考项目案例进行二次开发或学习的技术人员

### 4. 技术亮点
- 项目标签覆盖全面，包含主流AI框架和工具库（如NumPy、Pandas、Matplotlib、Seaborn等）
- 13261颗星的高人气表明社区认可度高，资源质量有保障
- 免费教材与实战案例结合，理论与实践并重
- 学习路线清晰，涵盖从基础数学到前沿CV/NLP的完整链路
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13261 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码框架，用于快速构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它面向数据科学家和机器学习工程师，提供简洁的声明式配置方式，降低 AI 模型开发门槛。

### 2. 核心功能
- **低代码模型构建**：通过 YAML/JSON 声明式配置即可定义和训练深度学习模型，无需编写大量代码
- **多模态支持**：涵盖自然语言处理（NLP）、计算机视觉等多种数据类型
- **LLM 微调**：支持对 Llama、Mistral 等主流大语言模型进行高效微调
- **数据驱动开发**：以数据为中心的设计理念，简化数据处理与模型训练流程
- **PyTorch 底层框架**：基于 PyTorch 构建，兼容主流深度学习生态

### 3. 适用场景
- 快速原型开发：数据科学家无需深入编码即可快速验证模型想法
- 企业级 LLM 微调：对开源大模型进行领域适配和定制训练
- 多模态 AI 应用：同时处理文本、图像等多种输入类型的智能系统
- 教学与实验：适合深度学习入门学习和算法研究对比

### 4. 技术亮点
- 采用声明式配置取代繁琐的代码实现，显著提升开发效率
- 内置数据预处理管道，自动处理缺失值、特征编码等常见任务
- 支持分布式训练，可灵活适配单机到集群的不同计算环境
- 提供模型可解释性工具，帮助分析模型决策依据
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9174 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8965 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6991 | 🍴 1174 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6406 | 🍴 778 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP 是一个全面的中文自然语言处理资源集合，涵盖了从基础工具到高级模型的完整解决方案。项目整合了敏感词检测、信息抽取、词库资源、预训练模型以及大量中文NLP数据集，为中文NLP研究和应用提供了一站式资源平台。

## 2. 核心功能

- **基础NLP工具**：中英文敏感词检测、语言检测、手机号/电话归属地查询、名字推断性别、信息抽取（手机号、身份证、邮箱）
- **丰富词库资源**：中日文人名库、中文缩写库、词汇情感值、停用词、反动词表、暴恐词表、同义词/反义词/否定词库、各领域专业词库（医学、法律、汽车等）
- **预训练模型与算法**：BERT/ALBERT/GPT-2等中文预训练模型、中文词向量、句子相似度匹配、文本生成与摘要工具
- **大规模数据集**：中文聊天语料、百度问答数据集、中文谣言数据、医疗对话数据、知识图谱数据等
- **高级NLP应用**：命名实体识别、关系抽取、知识图谱构建、智能问答系统、语音识别与合成

## 3. 适用场景

- **中文文本处理与清洗**：敏感词过滤、信息抽取、繁简转换、文本纠错等数据处理任务
- **NLP模型训练与微调**：利用预训练模型和大规模中文数据集进行文本分类、NER、关系抽取等任务
- **知识图谱构建**：通过实体抽取、关系抽取工具构建中文领域知识图谱
- **
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82512 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调，相关研究成果已发表于 ACL 2024。该工具旨在为研究人员和开发者提供一站式的大模型微调解决方案。

## 2. 核心功能
- 支持 100+ 种主流大语言模型和视觉语言模型的统一微调
- 提供多种高效微调方法，包括 LoRA、QLoRA、全参数微调等
- 支持指令微调、RLHF（人类反馈强化学习）等训练范式
- 内置量化技术，降低显存占用，提升训练效率
- 兼容 Transformers 框架，便于集成和扩展

## 3. 适用场景
- 研究人员需要快速验证不同模型在特定任务上的微调效果
- 开发者希望以较低成本对开源大模型进行领域适配
- 团队需要支持多模型、多任务的一站式微调平台
- 初学者希望以低门槛入门大模型微调领域

## 4. 技术亮点
- **统一架构**：一套代码支持百种模型，降低多模型适配成本
- **高效微调**：集成 LoRA/QLoRA/DoRA 等 PEFT 技术，显著减少显存需求
- **量化支持**：提供 NF4、FP4 等高精度量化方案，实现 4-bit 高效训练
- **多模态支持**：不仅支持纯文本模型，还兼容视觉语言模型（VLM）
- **RLHF 集成**：内置奖励模型训练和 PPO/DPO 等对齐算法，支持完整 RLHF 流程
- **开箱即用**：提供预置数据集和配置模板，降低上手难度
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74166 | 🍴 9077 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一门由微软推出的零基础人工智能入门课程，涵盖12周、24节课程内容，旨在让任何人都能轻松学习AI。项目以Jupyter Notebook形式呈现，内容全面覆盖机器学习与深度学习核心知识。

## 2. 核心功能
- 提供系统化的12周AI学习路径，适合零基础上手
- 涵盖机器学习、深度学习、计算机视觉、NLP等核心领域
- 包含CNN、RNN、GAN等主流深度学习模型实践
- 所有课程代码以Jupyter Notebook形式提供，便于交互式学习

## 3. 适用场景
- 高校或培训机构用于AI入门课程教学
- 开发者自学人工智能基础知识的实战练习
- 企业内AI技术培训与员工技能提升
- 对AI感兴趣的非技术背景人群科普入门

## 4. 技术亮点
- 微软官方出品，课程质量与权威性有保障
- 社区活跃度高（65,145星标），持续更新与维护
- 理论与实践结合，每课配备可运行的代码示例
- 学习路径清晰，循序渐进，适合不同基础的学习者
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65145 | 🍴 12648 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## AI Engineering from Scratch 项目分析

### 1. 中文简介
本项目是一套从零开始学习AI工程的完整课程，涵盖理论、实践与部署全流程。通过系统化的教程，帮助开发者掌握AI技术的核心原理与工程实践，最终能够独立构建并交付AI产品。

### 2. 核心功能
- 从零构建AI系统，深入理解底层原理而非仅调用API
- 涵盖LLM、计算机视觉、强化学习、多智能体等核心领域
- 提供完整的课程教程，支持Python与Rust双语言实现
- 教授MCP（Model Context Protocol）等现代AI工程标准
- 强调从学习到构建再到部署的全链路工程能力

### 3. 适用场景
- AI初学者希望系统掌握AI工程而非浅层应用
- 开发者需要深入理解Transformer、NLP等核心技术原理
- 团队希望构建自定义AI智能体或生成式AI应用
- 工程师寻求从原型到生产环境部署的完整实践指导

### 4. 技术亮点
- **从底层实现**：不依赖现成框架，手动实现核心算法以加深理解
- **多语言支持**：同时提供Python和Rust实现，兼顾易用性与性能
- **前沿技术覆盖**：包含Swarm Intelligence、MCP、Multi-Agent等最新研究方向
- **课程化设计**：结构化的学习路径，适合系统性自学或团队培训
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47009 | 🍴 8236 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub项目分析：ailearning

---

### 1. 中文简介

这是一个全面的机器学习与深度学习实战学习项目，涵盖数据分析、线性代数基础、PyTorch和TensorFlow 2等主流框架的实战应用，以及自然语言处理（NLTK）相关内容。项目以Python为核心语言，适合从入门到进阶的机器学习学习者。

---

### 2. 核心功能

- **经典算法实战**：集成SVM、KMeans、逻辑回归、朴素贝叶斯等主流机器学习算法的完整实现
- **深度学习框架支持**：同时提供PyTorch和TensorFlow 2的实战代码示例
- **自然语言处理**：基于NLTK库的NLP入门与实践
- **数据科学基础**：涵盖PCA、SVD等线性代数核心算法的实战应用
- **推荐系统**：实现基于协同过滤的推荐算法（如Apriori、FP-Growth）

---

### 3. 适用场景

- 机器学习初学者系统学习经典算法原理与代码实现
- 需要同时掌握PyTorch和TensorFlow两个深度学习框架的学习者
- 希望快速搭建推荐系统、NLP项目原型的开发者
- 高校学生将线性代数理论与机器学习实践结合的学习资源

---

### 4. 技术亮点

- **42459星标**：高人气开源项目，社区认可度强
- **双框架覆盖**：同时支持PyTorch和TensorFlow 2，适应不同学习需求
- **算法全面**：从传统机器学习到深度学习，从数据处理到NLP，形成完整知识体系
- **实战导向**：每个算法都有可运行的代码示例，便于动手实践
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42459 | 🍴 11517 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36334 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33826 | 🍴 4709 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29084 | 🍴 3541 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21840 | 🍴 3354 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17359 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36334 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介

Skyvern 是一款基于人工智能的浏览器自动化框架，能够智能地自动化各类基于浏览器的业务流程。它利用大语言模型（LLM）和计算机视觉技术，让机器像人类一样理解网页内容并执行操作，无需手动编写繁琐的选择器。

## 2. 核心功能

- **AI驱动的浏览器自动化**：利用大语言模型理解页面内容并自主决策操作，告别传统硬编码选择器。
- **视觉感知能力**：结合计算机视觉技术，能够"看懂"网页界面，处理动态加载和复杂布局。
- **灵活的工作流编排**：支持API调用和可视化配置，可构建复杂的端到端自动化流程。
- **多引擎支持**：兼容 Playwright、Puppeteer 等主流浏览器自动化工具，灵活适配不同场景。
- **RPA替代方案**：作为 Power Automate 等传统RPA工具的现代化替代，提供更智能的自动化体验。

## 3. 适用场景

- **电商自动化**：自动监控商品价格、库存变化，实现智能比价和抢购。
- **数据抓取与填报**：自动化处理需要登录、填写表单的复杂数据录入场景。
- **企业流程自动化**：替代人工重复操作，如报表生成、系统数据同步等。
- **测试与质量保障**：自动化UI测试，模拟真实用户行为验证Web应用功能。

## 4. 技术亮点

- 将LLM的语义理解能力引入浏览器自动化领域，突破传统工具依赖固定选择器的局限。
- 支持Vision LLM，可处理截图理解任务，适应动态和不可预测的网页环境。
- 提供REST API接口，便于集成到现有系统和CI/CD流程中。
- 开源且活跃，22,768+星标表明社区认可度高，生态持续完善。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22768 | 🍴 2140 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16538 | 🍴 3804 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## GitHub项目分析：pytorch-grad-cam

---

### 1. 中文简介
本项目是一个面向计算机视觉的高级AI可解释性工具库，基于PyTorch实现。它支持CNN、Vision Transformers等多种架构，覆盖分类、目标检测、分割、图像相似度等多种任务。

---

### 2. 核心功能
- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种类激活映射算法
- 兼容CNN和Vision Transformers（ViT）等主流模型架构
- 覆盖图像分类、目标检测、语义分割等多种任务类型
- 提供直观的可视化热图，帮助理解模型的决策依据
- 支持图像相似度分析等扩展应用场景

---

### 3. 适用场景
- **模型可解释性研究**：分析深度学习模型在视觉任务中的关注区域
- **模型调试与验证**：通过热力图检查模型是否关注了正确的图像区域
- **学术研究与论文可视化**：为计算机视觉论文提供高质量的可视化结果
- **医疗影像分析**：辅助医生理解AI诊断模型的决策逻辑

---

### 4. 技术亮点
- 社区认可度高，星标数达12,954，是PyTorch生态中Grad-CAM领域最受欢迎的库之一
- 支持多种Grad-CAM变体算法，满足不同精度与性能需求
- 对Vision Transformers原生支持，紧跟最新AI研究趋势
- 代码结构清晰，易于集成到现有项目中
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个专为空间 AI 设计的几何计算机视觉库，基于 PyTorch 构建。它提供了可微分的计算机视觉算子和工具，支持从传统图像处理到深度学习的全流程开发。

### 2. 核心功能
- 提供可微分的计算机视觉算子，支持与 PyTorch 无缝集成
- 包含丰富的几何变换、图像处理和相机标定工具
- 支持端到端的可微分管线，便于深度学习模型训练
- 内置多种经典计算机视觉算法的 PyTorch 实现
- 提供机器人视觉和空间推理相关的专用模块

### 3. 适用场景
- 深度学习与计算机视觉结合的研究与开发
- 机器人视觉感知和空间定位系统
- 可微分图像处理管线的设计与优化
- 三维视觉和几何深度学习应用

### 4. 技术亮点
- 完全基于 PyTorch 实现，与现有深度学习生态无缝兼容
- 所有算子支持自动微分，可直接嵌入神经网络训练流程
- 针对 GPU 加速优化，支持批量处理和实时计算
- 代码结构清晰，文档完善，社区活跃（11K+ 星标）
- 链接: https://github.com/kornia/kornia
- ⭐ 11314 | 🍴 1223 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2189 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3479 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3380 | 🍴 412 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2506 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全属于你自己的个人 AI 助手，支持任意操作系统和平台。它采用独特的"龙虾方式"（lobster way）运行，让你真正掌控自己的数据和 AI 体验。

### 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行，无平台限制
- **数据自主可控**：强调"own-your-data"理念，用户完全掌控个人数据
- **本地化部署**：支持本地运行，保护隐私安全
- **个性化 AI 助手**：为用户提供专属的 AI 助理服务
- **开源自由**：完全开源，社区驱动发展

### 3. 适用场景
- **隐私敏感用户**：不希望数据上传至第三方服务器的个人用户
- **多设备使用者**：需要在不同操作系统间无缝切换的用户
- **开发者群体**：希望自定义和扩展 AI 助手功能的开发者
- **独立研究者**：需要本地化 AI 工具进行数据分析的研究人员

### 4. 技术亮点
- 基于 TypeScript 构建，跨平台兼容性强
- 采用开源架构，社区活跃度高（38.6万星标）
- 支持模块化扩展，用户可按需定制功能
- 强调数据本地化处理，无需依赖外部云服务
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386525 | 🍴 81217 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub 项目分析：superpowers

### 1. 中文简介
这是一个基于AI代理的技能框架与软件开发方法论，旨在通过子代理驱动的方式提升开发效率。项目聚焦于将AI能力集成到软件开发生命周期中，提供可落地的协作开发流程。

### 2. 核心功能
- **代理驱动开发**：通过子代理（subagent）自动执行开发任务，实现分工协作
- **技能框架体系**：提供模块化的AI技能（skills）库，支持快速搭建开发流程
- **头脑风暴辅助**：集成AI头脑风暴能力，帮助团队进行创意构思与方案讨论
- **完整SDLC支持**：覆盖软件开发生命周期各环节，从需求到部署的全流程赋能
- **多语言Shell脚本支持**：以Shell为主要实现语言，便于在Linux/Unix环境下集成

### 3. 适用场景
- AI辅助编程：开发者使用AI代理加速代码编写、调试与重构
- 团队协作开发：多人通过子代理分工，提升大型项目协作效率
- 快速原型开发：利用AI技能框架快速搭建项目骨架
- 软件开发流程优化：传统团队引入AI驱动方法论，改进SDLC

### 4. 技术亮点
- **高人气项目**：星标数达273,087，说明社区认可度极高
- **创新方法论**：提出"子代理驱动开发"（subagent-driven-development）新概念，区别于传统的单AI助手模式
- **实用主义导向**：强调"works"（可落地），注重实际开发效果而非理论框架
- **开源生态整合**：与OBRAN（可能是Open Brainstorming/协作平台）等工具联动

---

**注意**：由于我无法直接访问该项目的GitHub仓库页面，以上分析基于您提供的项目描述和标签信息进行推断。如需更精确的功能细节，建议直接查看项目README或源码。
- 链接: https://github.com/obra/superpowers
- ⭐ 273087 | 🍴 24429 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 231865 | 🍴 46160 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一个公平源码（fair-code）工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，可自托管或云端部署，提供 400 多种集成方式。

### 2. 核心功能
- **可视化工作流构建**：通过拖拽节点快速设计自动化流程
- **原生 AI 集成**：内置 AI 能力，可直接在工作流中调用 AI 模型
- **400+ 预置集成**：覆盖主流 SaaS 工具和 API，开箱即用
- **灵活部署方式**：支持自托管（Self-hosted）和云端托管两种模式
- **代码与低代码结合**：既提供低代码界面，也支持自定义 TypeScript 代码

### 3. 适用场景
- **企业自动化**：自动化跨系统的数据同步、审批流程、通知推送等
- **AI 工作流编排**：将多个 AI 模型串联，构建复杂的智能应用管道
- **API 集成与数据流处理**：连接不同平台的 API，实现数据流转与转换
- **MCP 协议支持**：可作为 MCP 客户端/服务器，与 AI 代理集成

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态友好
- 支持 MCP（Model Context Protocol）协议，与 AI 代理生态深度整合
- 公平源码许可，兼顾开源社区与商业使用需求
- 社区活跃，星标数超过 20 万，生态成熟
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200956 | 🍴 60191 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 秉承让每个人都能使用并构建 AI 的愿景，致力于提供易用且强大的 AI 工具。我们的使命是打造完善的工具链，让您能够专注于真正重要的事务。

### 2. 核心功能
- 支持自主运行 AI 代理，无需人工持续干预
- 兼容多种大语言模型（GPT、Claude、Llama 等）
- 提供灵活的工具链扩展机制，可集成各类 API 和服务
- 支持多代理协作模式，实现复杂任务分解与执行
- 具备记忆系统，可跨会话保持上下文连续性

### 3. 适用场景
- **自动化工作流**：自动完成数据收集、整理和分析等重复性任务
- **内容创作辅助**：自动生成文章、报告、代码等结构化内容
- **研究与信息检索**：自主搜索网络、整合信息并输出摘要
- **个人助理**：帮助管理日程、提醒事项和日常事务

### 4. 技术亮点
- 采用 agentic AI 架构，支持目标驱动的任务规划与执行
- 模块化设计，便于自定义和扩展功能组件
- 开源社区活跃，持续集成最新 LLM 能力（GitHub 星标 186,640）
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186640 | 🍴 46060 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 168482 | 🍴 9423 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167300 | 🍴 21591 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164534 | 🍴 30553 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157820 | 🍴 46175 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153356 | 🍴 9872 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

