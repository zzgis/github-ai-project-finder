# GitHub AI项目每日发现报告
日期: 2026-06-28

## 新发布的AI项目

### Godcoder
- 描述: A local-first, open-source coding agent for your desktop. Bring your own LLM key; your code stays on your machine and only ever leaves to the model provider. The AI Agent builds its own Harnes.
- 链接: https://github.com/eli-labz/Godcoder
- ⭐ 244 | 🍴 0 | 语言: Rust
- 标签: ai, coding-agent, desktop-app, llm, local-first

### cheat-on-skill
- ### 1. 中文简介
该项目旨在帮助用户在 AI 时代筛选出高薪、具备个人可行性且不易被 AI 替代的工作机会，并结合 BOSS 直聘真实数据与防诈骗机制提供个性化学习陪跑计划。它通过能力匹配度评估和“可学性”门槛判断，为用户制定切实可行的职业转型路径。

### 2. 核心功能
*   **智能职位匹配**：结合用户现有能力与目标岗位需求进行精准匹配。
*   **可学性评估**：设置“可学性闸门”，确保推荐的工作技能是用户当前能够掌握或短期可以习得的。
*   **真实数据驱动**：集成 BOSS 直聘等平台的真实招聘数据，保证信息时效性与真实性。
*   **防诈骗保护**：内置反诈机制，识别并过滤高风险或不合规的招聘信息。
*   **个性化陪跑计划**：根据用户具体情况生成定制化的学习与职业转型路线图。

### 3. 适用场景
*   **职业转型期人群**：希望从传统行业转向 AI 相关高薪领域，但缺乏明确方向的学习者。
*   **求职焦虑者**：担心自身技能被 AI 取代，寻求具有长期稳定性和抗风险能力的职业建议的用户。
*   **防骗意识薄弱求职者**：在寻找高薪工作时容易遭遇虚假招聘或培训陷阱的初学者。
*   **自我提升规划者**：需要基于真实市场数据和自身能力差距制定系统性学习计划的人。

### 4. 技术亮点
*   **多源数据融合**：结合 LLM（大语言模型）的分析能力与实时招聘平台 API 数据，实现动态决策。
*   **Anthropic/Claude 生态集成**：利用 Anthropic 旗下 Claude 模型及其代码助手（Claude Code/Skills）进行深度语义理解和任务执行，提升推荐的准确性和交互体验。
*   **逻辑门控机制**：引入“可学性”作为硬性过滤条件，避免了传统 AI 推荐中常见的高估用户学习能力的偏差。
- 链接: https://github.com/XBuilderLAB/cheat-on-skill
- ⭐ 60 | 🍴 5 | 语言: JavaScript
- 标签: ai-career, anthropic, career-transition, claude-code, claude-skills

### Deepseek-API
- 描述: Reverse engineered Deepseek chat into an OpenAI compatible API. Access V4 and R1 models through a simple REST interface without API keys or billing.
- 链接: https://github.com/sums001/Deepseek-API
- ⭐ 58 | 🍴 8 | 语言: Python
- 标签: ai, ai-agents, ai-tools, copilot, deepseek

### AngleCraft
- 1. **中文简介**
AngleCraft 是一个通用的 AI 技能模块，能够将枯燥的专业话题转化为高互动性的内容。它通过 7+2 种新闻视角类型，支持任何大型语言模型、垂直领域及语言进行创作。

2. **核心功能**
*   提供 9 种经验证的新闻视角类型，用于重塑内容角度。
*   兼容任意大语言模型（LLM），无需绑定特定平台。
*   支持多语言环境及任何专业细分领域的主题创作。
*   专注于提升内容的参与度，将专家级知识转化为易读故事。
*   作为即插即用的提示词工程工具，优化生成内容的质量。

3. **适用场景**
*   撰写具有高传播力的社交媒体帖子和营销文案。
*   创建引人入胜的新闻通讯（Newsletter）或博客文章。
*   将复杂的技术文档或行业报告转化为大众可读的故事。
*   进行内容营销策略规划，多角度覆盖目标受众兴趣。

4. **技术亮点**
*   **通用性架构**：不依赖特定模型，通过标准化提示词逻辑适配所有 LLM。
*   **结构化叙事框架**：内置经过优化的“7+2”新闻视角模板，确保内容结构的专业性与吸引力。
*   **轻量级集成**：以 Agent Skill 形式存在，便于快速嵌入现有的 AI 工作流中。
- 链接: https://github.com/MADEVAL/AngleCraft
- ⭐ 46 | 🍴 14 | 语言: 未知
- 标签: agent-skill, ai-skill, anglecraft, content-creation, content-marketing

### backspin-algorithm
- 1. **中文简介**
BackSpin 提供了其算法的源代码级公式，详细揭示了 AI 等待状态如何转化为经过质量调整的注意力、广告触达范围如何排名与分配，以及开发者与平台间 50/50 的收入分成机制。该项目旨在消除“黑盒”操作，确保算法逻辑的完全透明和可验证性。

2. **核心功能**
*   公开 AI 等待状态转化为高质量注意力机制的底层数学公式。
*   展示广告商触达范围的排名算法及资源分配逻辑。
*   明确并开源了平台与开发者之间 50/50 收入分成的计算规则。
*   提供可验证的代码实现，拒绝不透明的黑盒算法。

3. **适用场景**
*   希望理解或审计 AI 驱动平台注意力分配机制的研究人员。
*   关注广告变现公平性及算法透明度的开发者或广告主。
*   致力于构建去中心化或高透明度内容平台的创业团队。
*   对 AI 经济模型中收入分成逻辑感兴趣的技术分析师。

4. **技术亮点**
*   **全透明算法**：通过开源核心公式，彻底解决 AI 平台常见的“黑盒”信任问题。
*   **经济模型可视化**：将复杂的 AI 注意力转化与收入分配过程转化为可阅读、可验证的代码逻辑。
- 链接: https://github.com/hackazer/backspin-algorithm
- ⭐ 45 | 🍴 0 | 语言: TypeScript

### MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- 描述: Ultimate 2026 external trainer for MECCHA CHAMELEON. Includes customizable ESP, aimbot, fly mode, and timer editor for the best hide-and-seek experience.
- 链接: https://github.com/ryancameron555/MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- ⭐ 25 | 🍴 0 | 语言: Python

### MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- 描述: Ultimate 2026 external trainer for MECCHA CHAMELEON. Includes customizable ESP, aimbot, fly mode, and timer editor for the best hide-and-seek experience.
- 链接: https://github.com/alex-carneiro/MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- ⭐ 24 | 🍴 0 | 语言: Python

### MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- 描述: Ultimate 2026 external trainer for MECCHA CHAMELEON. Includes customizable ESP, aimbot, fly mode, and timer editor for the best hide-and-seek experience.
- 链接: https://github.com/joker-alahram/MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- ⭐ 24 | 🍴 0 | 语言: Python

### MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- 描述: Ultimate 2026 external trainer for MECCHA CHAMELEON. Includes customizable ESP, aimbot, fly mode, and timer editor for the best hide-and-seek experience.
- 链接: https://github.com/Selva-rc/MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- ⭐ 24 | 🍴 0 | 语言: Python

### MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- 描述: Ultimate 2026 external trainer for MECCHA CHAMELEON. Includes customizable ESP, aimbot, fly mode, and timer editor for the best hide-and-seek experience.
- 链接: https://github.com/YousefMahdy1/MECCHA-CHAMELEON-Trainer-Aimbot-ESP
- ⭐ 24 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个涵盖丰富中文与自然语言处理资源的综合性开源项目，集成了敏感词过滤、实体抽取、情感分析及多种专业领域词库。该项目不仅提供了基础的语言处理工具，还收录了大量高质量的中文数据集、预训练模型及前沿NLP技术报告。

2. **核心功能**
- 提供中英文敏感词检测、语言识别及繁简转换等基础文本处理功能。
- 集成身份证、手机号、邮箱等正则抽取，以及人名性别推断和归属地查询服务。
- 包含海量中文专业词库（如医学、法律、汽车）及同义词、反义词、停用词等资源。
- 汇聚BERT、GPT等主流预训练模型代码、NLP竞赛解决方案及各类标注数据集。

3. **适用场景**
- **内容安全审核**：利用敏感词库和暴恐词表，快速构建互联网内容的自动化过滤系统。
- **信息抽取与结构化**：从非结构化文本中精准提取人名、地名、机构名及联系方式，服务于CRM或数据分析。
- **智能问答与对话系统**：基于项目提供的知识图谱、闲聊语料及预训练模型，开发垂直领域的智能客服或聊天机器人。
- **NLP算法研究与教学**：作为学习资源库，帮助开发者复现经典NLP任务、测试新模型或获取高质量训练数据。

4. **技术亮点**
- **资源极度全面**：将分散的NLP工具、数据集、模型和学术资源进行了系统化整合，降低了入门门槛。
- **领域覆盖广泛**：不仅包含通用NLP功能，还深入医疗、金融、法律等专业垂直领域，具备较高的实用价值。
- **紧跟前沿技术**：收录了BERT、GPT-2、ALBERT等最新预训练模型的应用案例及竞赛Top方案，具有较强的时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81483 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34975 | 🍴 7300 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看模型结构和参数。

2. **核心功能**
- 支持读取 Keras、TensorFlow、PyTorch、ONNX 等数十种模型格式。
- 提供清晰的计算图可视化，展示层结构、张量形状及权重信息。
- 兼容 CoreML、TensorFlow Lite 及 Safetensors 等移动端或特定生态格式。
- 支持在浏览器端直接打开模型文件，无需安装本地软件。
- 允许用户导出可视化结果为图片或交互式网页。

3. **适用场景**
- 调试深度学习模型结构，快速定位层错误或维度不匹配问题。
- 向非技术人员展示神经网络架构，用于汇报或教学演示。
- 检查模型转换（如 PyTorch 转 ONNX）后的完整性与正确性。
- 分析已部署的边缘设备模型（如 TensorFlow Lite）的内存占用和层细节。

4. **技术亮点**
- 基于 JavaScript 开发，实现跨平台兼容及浏览器内即时渲染，无需复杂依赖环境。
- 广泛支持异构模型格式，覆盖从传统机器学习到最新大模型安全的多种标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33144 | 🍴 3140 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是机器学习领域的开放标准，旨在实现不同框架间的模型互操作性。它允许用户在不同深度学习平台之间无缝转换和运行模型，打破生态壁垒。

2. **核心功能**
*   支持将主流框架（如 PyTorch、TensorFlow）训练的模型转换为通用 ONNX 格式。
*   提供跨平台推理能力，使模型能在各种硬件和软件环境中高效执行。
*   定义了统一的计算图和数据类型规范，确保模型结构的标准化与兼容性。
*   拥有庞大的社区支持和丰富的算子库，覆盖广泛的深度学习网络结构。
*   便于模型部署优化，可结合 ONNX Runtime 等工具进行性能加速。

3. **适用场景**
*   需要将 PyTorch 或 Keras 训练好的模型部署到不支持原生的生产环境（如 C++ 服务）。
*   在异构硬件平台（如 CPU、GPU、NPU）间迁移模型并进行统一推理管理。
*   跨框架协作项目，例如将 TensorFlow 训练的结果用于 Scikit-learn 的后处理流程。
*   希望减少模型部署复杂度，利用标准化格式替代多套专用部署工具的团队。

4. **技术亮点**
*   **中立性**：由微软、Facebook 等巨头联合发起，避免被单一厂商锁定。
*   **高性能运行时**：配套的 ONNX Runtime 支持多种后端加速，显著提升推理速度。
*   **广泛兼容性**：几乎涵盖所有主流深度学习框架，是事实上的模型交换通用语言。
- 链接: https://github.com/onnx/onnx
- ⭐ 21060 | 🍴 3955 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
该项目是一部关于机器学习工程实践的“开放式书籍”，旨在系统性地指导开发者高效构建和部署大规模机器学习系统。它涵盖了从底层硬件优化到上层模型训练的完整工程链路，是 MLOps 领域的权威参考指南。

### 2. 核心功能
*   **全栈工程覆盖**：提供涵盖数据预处理、模型训练、微调及推理部署的端到端工程实践方案。
*   **大规模扩展优化**：深入解析如何在分布式集群中利用 Slurm 和 GPU 网络优化实现模型的横向扩展。
*   **性能调优与调试**：提供针对 PyTorch 等框架的详细性能剖析、内存管理及故障排查技巧。
*   **基础设施管理**：详解存储系统、容器化技术及 Kubernetes 在 ML 工作流中的集成与应用。

### 3. 适用场景
*   **LLM 训练工程师**：需要优化大型语言模型训练效率、降低成本并解决分布式训练瓶颈的团队。
*   **MLOps 架构师**：负责设计可扩展、高可用的机器学习生产环境基础设施的专业人士。
*   **AI 系统研究者**：希望深入了解机器学习底层硬件交互、网络通信及存储优化的研究人员。

### 4. 技术亮点
*   **实战导向**：基于 Hugging Face Transformers 等主流库，提供大量可落地的代码示例和最佳实践。
*   **前沿性**：紧跟 LLM 时代需求，特别强化了对推理加速、显存优化及大模型微调的工程支持。
*   **社区驱动**：作为开源社区贡献的知识库，持续整合来自工业界和学术界的最新工程解决方案。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18182 | 🍴 1154 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17259 | 🍴 2107 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13091 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11528 | 🍴 903 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10645 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI相关实战代码库的综合资源集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的Python代码实现，帮助开发者快速理解并复现各类经典AI算法与应用。作为一个被广泛认可的“Awesome”列表，它是入门和实践人工智能技术的优质参考资料。

2. **核心功能**
*   汇集500个涵盖AI各主要分支的代码示例与项目模板。
*   提供从基础机器学习到前沿深度学习的完整技术栈支持。
*   专注于计算机视觉和自然语言处理领域的实际应用场景落地。
*   所有项目均附带可运行的Python代码，便于直接学习与调试。
*   采用分类清晰的目录结构，方便用户按领域快速检索所需资料。

3. **适用场景**
*   AI初学者希望通过大量实例代码快速掌握机器学习基础概念。
*   数据科学家或工程师需要寻找特定CV或NLP任务的参考实现方案。
*   高校学生或研究人员利用该列表进行算法复现和技术调研。
*   开发者希望构建个人AI作品集时，作为项目灵感和代码起点。

4. **技术亮点**
*   极高的社区认可度（近3.5万星标），代表了广泛的权威性和实用性。
*   内容覆盖面极广，几乎囊括了当前主流的AI子领域及其最新进展。
*   强调“With Code”，确保每个理论点都有对应的工程实践代码支撑。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34975 | 🍴 7300 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看模型结构和参数。

2. **核心功能**
- 支持读取 Keras、TensorFlow、PyTorch、ONNX 等数十种模型格式。
- 提供清晰的计算图可视化，展示层结构、张量形状及权重信息。
- 兼容 CoreML、TensorFlow Lite 及 Safetensors 等移动端或特定生态格式。
- 支持在浏览器端直接打开模型文件，无需安装本地软件。
- 允许用户导出可视化结果为图片或交互式网页。

3. **适用场景**
- 调试深度学习模型结构，快速定位层错误或维度不匹配问题。
- 向非技术人员展示神经网络架构，用于汇报或教学演示。
- 检查模型转换（如 PyTorch 转 ONNX）后的完整性与正确性。
- 分析已部署的边缘设备模型（如 TensorFlow Lite）的内存占用和层细节。

4. **技术亮点**
- 基于 JavaScript 开发，实现跨平台兼容及浏览器内即时渲染，无需复杂依赖环境。
- 广泛支持异构模型格式，覆盖从传统机器学习到最新大模型安全的多种标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33144 | 🍴 3140 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### GitHub 项目分析报告：cheatsheets-ai

#### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了一套必备的技术速查表（Cheat Sheets）。内容涵盖主流框架如 Keras、NumPy、SciPy 和 Matplotlib 的核心语法与常用操作。它旨在帮助开发者快速回顾关键概念，提升研究与开发效率。

#### 2. 核心功能
*   提供机器学习基础理论与算法流程的快速参考指南。
*   汇总深度学习框架（如 Keras）的关键代码片段与API用法。
*   整理科学计算库（NumPy、SciPy）的高效数据处理技巧。
*   包含数据可视化工具（Matplotlib）的常用图表绘制模板。
*   整合人工智能领域必备的基础数学与统计知识要点。

#### 3. 适用场景
*   **面试准备**：候选人快速复习机器学习算法细节及框架常用命令。
*   **日常开发**：研究人员在编写代码时快速查阅特定函数或参数的正确用法。
*   **知识巩固**：初学者通过结构化笔记梳理深度学习核心概念体系。
*   **团队协作**：作为团队内部的技术文档共享，统一代码规范与最佳实践。

#### 4. 技术亮点
*   **高度浓缩**：将复杂的框架文档精简为单页或短篇幅的速查手册，便于记忆。
*   **覆盖全面**：横跨从底层数学库到上层深度学习框架的全栈技术栈。
*   **开源社区驱动**：拥有极高的星标数（15k+），证明其内容质量与社区认可度极高。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3390 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13091 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 以下是关于 GitHub 项目 **Ludwig** 的技术分析报告：

1. **中文简介**
   Ludwig 是一个低代码框架，旨在简化自定义大型语言模型、神经网络及其他 AI 模型的构建过程。它通过声明式配置驱动开发，降低了机器学习工程化的门槛。

2. **核心功能**
   *   支持低代码方式快速构建和训练深度学习模型。
   *   内置对多种主流架构（如 Transformer、CNN、RNN）的原生支持。
   *   提供自动化数据预处理与特征工程管道。
   *   兼容 PyTorch 后端，便于模型微调与部署。

3. **适用场景**
   *   需要快速原型化验证深度学习想法的数据科学家。
   *   希望利用低代码工具微调 Llama、Mistral 等大语言模型的开发团队。
   *   进行计算机视觉或自然语言处理任务的标准化建模工作。

4. **技术亮点**
   *   **声明式配置**：用户仅需定义 YAML 配置文件即可自动完成模型构建与训练逻辑，无需编写大量底层代码。
   *   **多模态支持**：天然兼容表格数据、文本、图像等多种数据类型，适合复杂的多模态学习任务。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11727 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9121 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8910 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6192 | 🍴 724 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能全面的中英文自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简体转换等基础NLP能力。该项目还包含了丰富的中文资源库（如姓名、职业、成语、古诗词）及多种预训练模型和知识图谱数据，旨在为开发者提供一站式的中英双语NLP解决方案。

**2. 核心功能**
*   **基础NLP处理**：提供中英文敏感词过滤、语言检测、停用词、情感分析及文本相似度匹配。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、人名等实体抽取，并具备姓名性别推断及中外电话归属地查询功能。
*   **丰富中文资源库**：内置中日文人名库、中文缩写、职业名称、汽车品牌、成语、古诗词及多个垂直领域（医疗、法律、财经等）专用词典。
*   **模型与数据集集成**：汇聚了BERT、ALBERT、RoBERTa等主流预训练模型，以及大量中文NLP竞赛数据集、知识图谱和语音识别语料。
*   **高级应用工具**：包含聊天机器人构建（如seqGAN、GPT2闲聊）、OCR文字识别、文本摘要、关键词抽取及语音情感分析等进阶功能。

**3. 适用场景**
*   **内容安全审核**：用于社交媒体、论坛或聊天应用中，快速识别和过滤敏感词、暴恐词及虚假信息。
*   **中文信息结构化**：在处理客服工单、新闻评论或非结构化文本时，自动抽取人名、地名、机构名及联系方式。
*   **智能问答与对话系统**：利用其提供的知识图谱、语料库及预训练模型，快速搭建垂直领域（如医疗、金融）的客服机器人或闲聊助手。
*   **NLP研究与教学**：作为研究人员或学生的资源库，获取最新的中文NLP数据集、基准测试结果及开源代码实现。

**4. 技术亮点**
*   **资源聚合度高**：不仅提供代码工具，还整合了清华XLORE、百度问答、各类垂直领域词典等高质量中文语料和知识资源。
*   **涵盖前沿模型**：广泛收录了基于Transformer架构的最新预训练模型（如BERT系列、ALBERT、ELECTRA）及其微调代码。
*   **全栈式支持**：从底层的分词、词性标注，到高层的命名实体识别、知识图谱构建及对话生成，提供了完整的NLP技术链路参考。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81483 | 🍴 15249 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72625 | 🍴 8878 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
该项目是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。课程采用Jupyter Notebook作为主要教学工具，内容涵盖从基础机器学习到深度学习的广泛主题。

### 2. 核心功能
*   **系统化课程体系**：提供结构化的12周学习路径，分为24个独立课时，循序渐进地引导学习者。
*   **交互式代码实践**：基于Jupyter Notebook开发，支持实时运行代码和可视化结果，便于动手练习。
*   **全栈AI技术覆盖**：内容囊括机器学习、深度学习、计算机视觉、自然语言处理及生成对抗网络等核心领域。
*   **微软官方背书**：由Microsoft For Beginners系列出品，确保内容的专业性与前沿性。

### 3. 适用场景
*   **零基础入门学习**：适合完全没有编程或AI背景的新手进行系统性启蒙。
*   **高校与培训机构教材**：可作为计算机科学或数据科学专业的短期课程补充材料。
*   **开发者技能拓展**：帮助传统软件工程师快速了解并上手AI开发流程。

### 4. 技术亮点
*   **多模态技术整合**：同时教授CNN（卷积神经网络）、RNN（循环神经网络）和GAN（生成对抗网络）等多种主流架构。
*   **社区驱动的高人气**：拥有近5万星标，证明其内容质量高且深受全球开发者认可。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48493 | 🍴 10070 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46720 | 🍴 7649 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 以下是针对 GitHub 项目 **ailearning** 的详细技术分析：

1. **中文简介**
   该项目是一个全面的 AI 学习资源库，涵盖了从数学基础到深度学习算法的完整实战体系。内容主要包括数据分析、机器学习算法实现、线性代数理论、以及基于 PyTorch、NLTK 和 TensorFlow 2 的技术栈应用。它旨在为学习者提供从理论到代码落地的系统性指导。

2. **核心功能**
   - **多框架算法复现**：支持使用 Scikit-learn、PyTorch 和 TensorFlow 2 等多种主流工具进行模型实现。
   - **经典算法全覆盖**：包含监督学习（如 SVM、逻辑回归）、无监督学习（如 K-Means、PCA）及集成学习（如 AdaBoost）。
   - **深度与自然语言处理**：深入讲解 DNN、RNN、LSTM 等神经网络结构，并结合 NLTK 进行 NLP 实战。
   - **推荐系统与关联规则**：实现协同过滤推荐算法及 Apriori、FP-Growth 等频繁项集挖掘算法。

3. **适用场景**
   - **AI 初学者系统入门**：适合希望从零开始构建机器学习知识体系，打通数学原理与代码实现的学习者。
   - **面试准备与刷题**：适合求职者通过阅读经典算法的代码实现和笔记，快速复习核心知识点以应对技术面试。
   - **特定领域技术进阶**：适合需要深入了解深度学习架构或自然语言处理具体落地场景的开发者参考。

4. **技术亮点**
   - **理论与实践结合紧密**：不仅提供代码，还强调背后的数学推导（如线性代数），有助于理解算法本质。
   - **技术栈广泛且前沿**：同时涵盖传统机器学习库（Sklearn）和现代深度学习框架（PyTorch/TF2），适应不同阶段需求。
   - **高社区认可度**：拥有超过 42,000 的星标，证明其内容质量高且被大量开发者验证为优质学习资料。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36629 | 🍴 6040 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34975 | 🍴 7300 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33700 | 🍴 4688 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28225 | 🍴 3426 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25764 | 🍴 2886 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34975 | 🍴 7300 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22018 | 🍴 2059 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### GitHub 项目分析报告：CVAT

**1. 中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的 AI 辅助标注与团队协作。它提供开源、云版和企业版产品，并配套标注服务，具备质量保证、数据分析及开发者 API 等功能。

**2. 核心功能**
*   支持图像、视频和 3D 点云的多模态数据标注。
*   提供 AI 辅助标注功能，显著提升数据标注效率。
*   内置质量保证机制与团队协作者管理工具。
*   开放开发者 API，便于集成到现有工作流中。

**3. 适用场景**
*   为深度学习模型训练准备大规模图像分类或目标检测数据集。
*   对自动驾驶或监控视频进行逐帧语义分割或对象跟踪标注。
*   科研机构或企业构建私有化部署的高质量计算机视觉数据集。

**4. 技术亮点**
*   **多模式支持**：不仅限于 2D 图像，还原生支持复杂的 3D 标注任务。
*   **AI 增强**：集成智能算法辅助人工标注，减少重复劳动。
*   **灵活部署**：同时提供开源本地部署、云端 SaaS 及企业级解决方案，适应不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16165 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目旨在为计算机视觉提供高级的AI可解释性功能，支持卷积神经网络（CNN）和视觉Transformer等多种架构。它涵盖了分类、目标检测、分割及图像相似度等任务的可视化与解释需求。

2. **核心功能**
*   支持多种主流深度学习模型，包括CNN和Vision Transformers。
*   提供广泛的计算机视觉任务支持，如分类、目标检测和语义分割。
*   实现多种梯度加权类激活映射算法（如Grad-CAM、Score-CAM）。
*   生成可视化的热力图以直观展示模型决策依据，提升模型透明度。

3. **适用场景**
*   研究人员需要调试和优化计算机视觉模型的注意力机制时。
*   医疗影像分析中，医生需通过可视化结果验证AI诊断的可信度。
*   自动驾驶或安防系统中，开发团队需解释目标检测模型的判断逻辑。

4. **技术亮点**
*   集成了多种先进的可解释性AI（XAI）方法，不仅限于基础的Grad-CAM。
*   拥有极高的社区认可度（近1.3万星标），代码库成熟且维护活跃。
*   提供了统一的API接口，方便在不同视觉任务间快速切换和应用。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12893 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理与计算机视觉操作，旨在简化深度学习中的视觉任务开发。

2. **核心功能**
*   提供大量可微分的传统计算机视觉算法（如滤波、形态学、几何变换）。
*   支持与 PyTorch 张量无缝集成，便于在神经网络中直接进行图像处理。
*   包含多种常用的图像增强和几何校正工具，加速模型训练流程。

3. **适用场景**
*   **可微分计算机视觉研究**：需要在梯度反向传播中集成几何变换或图像预处理的研究场景。
*   **机器人视觉系统**：用于实时处理传感器数据并进行空间定位与导航的机器人应用。
*   **深度学习数据增强**：在训练 pipeline 中实现高效、不同断的数据增强以提高模型鲁棒性。

4. **技术亮点**
*   **原生 PyTorch 集成**：完全基于 PyTorch 构建，无需转换数据结构即可实现高性能计算。
*   **可微分设计**：所有操作均支持自动微分，允许将传统 CV 模块嵌入端到端的深度学习网络中。
- 链接: https://github.com/kornia/kornia
- ⭐ 11252 | 🍴 1192 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8869 | 🍴 2193 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3256 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2616 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2413 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调数据完全由用户自主掌控。它采用 TypeScript 开发，以“龙虾”为象征，致力于提供一种私密、安全的本地化 AI 体验。

**2. 核心功能**
*   跨平台兼容，可在任何主流操作系统上部署运行。
*   支持“Own Your Data”理念，确保用户数据的隐私与所有权。
*   提供个性化的 AI 助理服务，适应不同用户的使用习惯。
*   基于 TypeScript 构建，具备良好的可扩展性和维护性。

**3. 适用场景**
*   注重隐私保护的个人用户，希望在不依赖云端服务的情况下使用 AI。
*   开发者或技术爱好者，需要在本地环境快速搭建和定制 AI 助手。
*   需要跨设备同步且保持数据本地化的多平台工作流用户。

**4. 技术亮点**
*   采用 TypeScript 语言开发，类型安全且生态丰富。
*   架构设计灵活，支持模块化扩展以适应不同平台需求。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380785 | 🍴 79770 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架与软件开发方法论。它通过结构化的流程赋能开发者，旨在提升软件工程的整体效率与质量。该项目结合了前沿的AI代理技术与传统的软件开发生命周期（SDLC）实践。

### 2. **核心功能**
*   提供模块化的“技能”库，支持自动化处理常见的开发任务。
*   采用子代理驱动开发（Subagent-driven Development），实现任务的分解与并行执行。
*   整合头脑风暴与创意生成工具，辅助早期需求分析与设计阶段。
*   构建完整的软件开发生命周期（SDLC）工作流，涵盖从编码到部署的各个环节。
*   作为统一的代理框架，协调多个AI子代理协同完成复杂的软件工程目标。

### 3. **适用场景**
*   需要快速原型开发并借助AI加速迭代周期的初创团队。
*   希望引入自动化测试、代码审查等特定技能的成熟软件开发项目。
*   利用AI进行创意发散和需求梳理的产品设计与规划阶段。
*   致力于探索下一代软件工程范式，特别是多代理协作模式的研发团队。

### 4. **技术亮点**
*   **子代理驱动架构**：创新性地采用多代理协作模式，将复杂任务拆解为可管理的子任务。
*   **方法论与工具结合**：不仅提供代码工具，更输出一套可落地的软件开发方法论（如OBRAS）。
*   **全生命周期覆盖**：标签显示其支持从头脑风暴（Brainstorming）到编码（Coding）的全流程，而非单一环节。
- 链接: https://github.com/obra/superpowers
- ⭐ 240283 | 🍴 21330 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. **中文简介**
Hermes Agent 是一个具备自我进化能力的智能代理，能够随着用户的交互和使用习惯不断成长与优化。它致力于提供个性化的 AI 辅助体验，通过持续的学习来增强其解决问题的能力。

### 2. **核心功能**
*   **自适应学习**：根据用户反馈和历史交互数据自动调整行为模式。
*   **多模型支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT) 等多个主流大语言模型。
*   **代码辅助**：集成 Codex 等工具，提供智能的代码生成、审查及调试功能。
*   **自主任务执行**：能够独立规划并执行复杂的自动化工作流。
*   **个性化定制**：允许用户定义特定的角色设定和工作偏好以适配不同场景。

### 3. **适用场景**
*   **开发者效率提升**：作为编程助手，协助进行代码编写、重构和错误排查。
*   **复杂任务自动化**：处理需要多步骤推理和跨平台操作的日常行政或技术任务。
*   **个性化知识管理**：构建基于个人知识库的智能问答系统，提供精准的信息检索。
*   **创意协作**：在写作、策划等创意工作中提供灵感激发和内容草稿生成。

### 4. **技术亮点**
*   **高度可扩展架构**：支持插件式扩展，便于接入新的 AI 模型或外部工具。
*   **开源生态整合**：紧密整合 Nous Research 等社区资源，保持技术前沿性。
*   **隐私与安全优先**：强调本地化部署选项和数据控制权，保障用户信息安全。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 204560 | 🍴 36841 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合。它提供超过 400 种集成方式，用户可选择自托管或云端部署，灵活满足各种自动化需求。

### 2. 核心功能
*   **混合构建模式**：结合可视化拖拽界面与自定义代码编写，兼顾易用性与灵活性。
*   **丰富的集成生态**：内置 400 多种集成连接器，覆盖主流 API 和服务。
*   **原生 AI 能力**：深度整合 AI 功能，支持智能工作流处理与自动化决策。
*   **灵活部署选项**：支持自托管（Self-hosted）和云端部署，保障数据隐私与控制权。
*   **MCP 协议支持**：原生支持 MCP（Model Context Protocol），便于与各类 AI 模型上下文交互。

### 3. 适用场景
*   **企业级 API 自动化**：连接多个 SaaS 服务，自动同步数据、触发通知或执行复杂业务逻辑。
*   **AI 驱动的工作流**：利用 LLM 进行内容生成、数据分析或智能客服流程的自动化编排。
*   **开发者工具链集成**：在 CI/CD 流水线中自动执行测试、部署或代码审查任务。
*   **数据管道构建**：从不同来源采集数据，经过清洗转换后存储到数据库或数据仓库。

### 4. 技术亮点
*   **公平代码（Fair-code）许可**：在保证开源协作的同时，允许商业友好使用，平衡社区与企业利益。
*   **TypeScript 全栈开发**：基于 TypeScript 构建，提供类型安全和良好的开发体验。
*   **低代码/无代码框架**：降低自动化门槛，同时保留通过代码扩展的高级能力。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194323 | 🍴 58897 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185190 | 🍴 46126 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164449 | 🍴 21288 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163909 | 🍴 30375 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156654 | 🍴 46149 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150146 | 🍴 9357 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146806 | 🍴 23129 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

