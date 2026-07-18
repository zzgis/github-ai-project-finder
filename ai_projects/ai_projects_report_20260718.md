# GitHub AI项目每日发现报告
日期: 2026-07-18

## 新发布的AI项目

### Trading-Bot
- 1. **中文简介**
该项目是一个套利机器人，由连接到外部自动化脚本的智能合约构成，该脚本负责控制其整体运行。它主要利用区块链上的价格差异或交易顺序进行自动化套利操作。

2. **核心功能**
*   通过智能合约执行链上资产交换与套利逻辑。
*   依赖外部自动化脚本实时监控市场并触发交易指令。
*   支持对以太坊（ETH）、比特币（BTC）等主流加密货币的交易处理。
*   集成AI元素以辅助交易决策或优化策略。
*   具备MEV（最大可提取价值）捕获能力，优化交易排序获利。

3. **适用场景**
*   去中心化交易所（DEX）之间的跨平台套利交易。
*   利用高频自动化脚本捕捉短暂的区块链交易价格偏差。
*   针对MEV机会（如三明治攻击或清算）进行策略性交易。
*   基于AI算法辅助的自动化加密货币投资组合管理。

4. **技术亮点**
*   采用Solidity编写智能合约，确保逻辑在以太坊虚拟机中可靠执行。
*   结合外部脚本与链上合约，实现了链下监控与链上执行的分离架构。
*   标签中提及“claude”和“ai”，暗示可能集成了大语言模型辅助生成代码或策略。
- 链接: https://github.com/MIgHTy-alIeN/Trading-Bot
- ⭐ 239 | 🍴 138 | 语言: Solidity
- 标签: ai, aitradingbot, bot, btc, claude

### klaatcode
- ### 1. 中文简介
Klaatcode 是一款开源的终端 AI 编程代理，旨在提供与 Claude Code 相媲美的代码生成精度。它通过智能路由机制，为不同任务自动匹配最合适的 AI 模型（支持 Claude、GPT、Gemini 等），从而将成本降低 10 倍。

### 2. 核心功能
- **多模型智能路由**：根据任务类型自动选择最优 AI 模型，平衡性能与成本。
- **高精度代码生成**：提供接近商业级工具（如 Claude Code）的代码编写和调试准确率。
- **广泛模型兼容**：原生支持 Claude、GPT、Gemini、DeepSeek 等多种主流 LLM。
- **终端集成体验**：专为命令行环境设计，提供流畅的 CLI 交互编程体验。

### 3. 适用场景
- **成本控制开发**：需要高频调用大模型但希望显著降低 API 费用的团队或个人开发者。
- **混合模型工作流**：希望在一个工具中同时利用不同模型优势（如用 GPT 处理逻辑，用 Claude 处理文本）的场景。
- **终端优先用户**：习惯在命令行环境中进行快速原型开发和代码生成的工程师。

### 4. 技术亮点
- **动态模型调度**：内置智能决策引擎，无需手动切换模型即可实现“对的任务用对的模型”。
- **开源可定制**：基于 TypeScript 构建，完全开源，允许用户自定义路由策略或添加新模型支持。
- 链接: https://github.com/KlaatAI/klaatcode
- ⭐ 123 | 🍴 17 | 语言: TypeScript
- 标签: agentic-ai, ai, ai-agents, ai-coding, ai-model

### production-ai-stack
- 由于该项目提供的元数据（描述、语言、标签等）均为空或默认值，且“production-ai-stack”这一名称较为通用，无法直接定位到唯一的特定开源仓库。因此，基于该名称在人工智能工程化领域的通用含义，为您提供一个标准的分析框架作为参考：

1. **中文简介**
   该项目通常指代一套用于在工业环境中部署、监控和管理大规模人工智能模型的完整技术栈。它涵盖了从模型训练、版本控制到服务化部署及性能监控的全生命周期管理工具。旨在解决AI模型从实验环境走向生产环境时面临的复杂性和稳定性挑战。

2. **核心功能**
   - 提供模型版本控制与实验追踪，确保可复现性。
   - 支持自动化CI/CD流水线，实现模型的快速迭代与部署。
   - 集成实时性能监控与日志记录，保障系统稳定性。
   - 包含模型注册表，统一管理不同环境的模型资产。
   - 提供推理服务的负载均衡与弹性伸缩能力。

3. **适用场景**
   - 企业级大规模机器学习平台的搭建与维护。
   - 需要高频更新和严格合规性的金融或医疗AI应用。
   - 多团队协同开发，需统一AI基础设施标准的组织。
   - 从原型验证向高并发生产环境迁移的过渡阶段。

4. **技术亮点**
   通常整合了MLOps最佳实践，强调自动化、可观测性和安全性，而非单一算法的实现。
- 链接: https://github.com/h9-tec/production-ai-stack
- ⭐ 69 | 🍴 8 | 语言: 未知

### cinematic-scroll-prompt-kit
- 1. **中文简介**
这是一个专为电影感滚动驱动的2.5D网页设计而构建的可复用AI提示词与项目简报系统。它旨在帮助开发者利用AI工具生成高质量的视觉内容，以增强网页的沉浸感和叙事性。

2. **核心功能**
- 提供标准化的AI提示词模板，用于生成符合电影美学风格的图像或视频素材。
- 包含完整的项目简报框架，帮助明确2.5D滚动动画的设计需求和技术规格。
- 支持将创意概念快速转化为可执行的代码或资产生成指令。
- 集成多种AI工具（如Claude Code、Codex等）的工作流，提升开发效率。

3. **适用场景**
- 设计师或开发者需要为高端品牌官网创建具有强烈视觉冲击力的滚动叙事页面。
- 创意团队希望利用AI加速生成电影级背景、角色或特效素材，减少手动制作时间。
- 前端工程师在实现复杂滚动动画时，需要统一的提示词标准来确保视觉风格的一致性。
- 教育或培训场景中，用于教授如何将AI辅助创作与传统前端技术结合打造沉浸式体验。

4. **技术亮点**
- 强调“提示词工程”与“创意编码”的结合，填补了AI生成内容与前端实现之间的鸿沟。
- 针对2.5D和滚动驱动动画这一细分领域，提供了高度垂直化的解决方案。
- 兼容主流AI编程助手（如Codex、Claude Code），便于直接集成到现有开发流程中。
- 链接: https://github.com/amirmushichge/cinematic-scroll-prompt-kit
- ⭐ 40 | 🍴 6 | 语言: 未知
- 标签: claude-code, codex, creative-coding, ltx-studio, prompt-engineering

### pohuy
- 描述: Режим идиоматического русского мата для AI-агентов. Короче, душевнее, эффективнее. 18+
- 链接: https://github.com/smixs/pohuy
- ⭐ 25 | 🍴 1 | 语言: 未知

### JARVIS-Type-AI
- 描述: 无描述
- 链接: https://github.com/TarikurRahmanBD/JARVIS-Type-AI
- ⭐ 20 | 🍴 0 | 语言: Python

### Embinder
- 描述: Embinder makes the agent a resident of the app. Turn every traditional platform to AI-native platform
- 链接: https://github.com/celesnity/Embinder
- ⭐ 15 | 🍴 0 | 语言: Go

### hig-mcp
- 描述: MCP server serving Apple Human Interface Guidelines as structured design tokens for AI coding agents — post-WWDC25 system colors, Liquid Glass constraints, SwiftUI mappings.
- 链接: https://github.com/aka-kika/hig-mcp
- ⭐ 15 | 🍴 0 | 语言: Python
- 标签: ai-agents, apple, claude-code, cursor, design-tokens

### cowrite
- 描述: Local AI co-writing canvas with MCP and bundled Image2, HTML diagram, and writing skills
- 链接: https://github.com/SpaceZephyr/cowrite
- ⭐ 14 | 🍴 2 | 语言: TypeScript

### Kimi-K3-Code-Free-Desktop-AI
- 描述: Kimi K3 code free setups via API keys and reverse proxies. Deploy this 2.8T parameter open-weights model for long-horizon agentic coding and 1M context window workflows. Customize Kimi Delta Attention prompts, bypass rate limits, and download direct GitHub repository configuration files.
- 链接: https://github.com/kimik3/Kimi-K3-Code-Free-Desktop-AI
- ⭐ 12 | 🍴 0 | 语言: TypeScript
- 标签: ai-api-free, ai-desktop, desktop-ai, free-ai-tools, k2-7

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个汇集了大量中文自然语言处理资源、数据集、预训练模型及实用工具的综合性 GitHub 仓库。它涵盖了从基础文本处理（如敏感词检测、分词、NER）到高级任务（如知识图谱构建、对话系统、语音识别）的全方位内容，旨在为开发者提供一站式的 NLP 解决方案。

**2. 核心功能**
*   **丰富语料与数据集**：提供中英文敏感词、停用词、人名/地名库、古诗词、行业词库及大规模问答/对话数据集。
*   **NLP 工具与算法库**：集成分词、词性标注、情感分析、关键词抽取、文本摘要、相似度匹配及多种深度学习模型（如 BERT, GPT-2）。
*   **知识图谱与实体识别**：包含多领域知识图谱构建工具、命名实体识别（NER）模型及实体链接技术。
*   **语音与OCR技术**：收录中文语音识别（ASR）、语音情感分析、中文手写汉字识别及文档表格提取工具。
*   **实用小工具**：提供手机号/身份证抽取、繁简转换、数字转换、拼音标注等高频业务场景辅助功能。

**3. 适用场景**
*   **智能客服与聊天机器人开发**：利用其中的对话数据集、意图识别模型和闲聊语料，快速构建具备上下文理解和多轮对话能力的机器人。
*   **内容安全与风控系统**：调用敏感词库、暴恐词表及反动词表，实现用户生成内容（UGC）的自动审核与风险拦截。
*   **垂直领域知识抽取与分析**：结合医疗、金融、法律等领域的专用词库和 NER 模型，从非结构化文本中提取关键实体并构建行业知识图谱。
*   **文本预处理与增强**：在训练自己的 NLP 模型前，使用其中的清洗工具、数据增强脚本（如 EDA）及标准化模块提升数据质量。

**4. 技术亮点**
*   **资源极度聚合**：不仅包含代码，还整合了清华 XLORE、百度基准系统等顶尖学术与工业界资源，是中文 NLP 领域的“百科全书”。
*   **紧跟前沿技术**：持续更新 BERT、GPT-2、ALBERT、ERNIE 等最新预训练模型及其微调示例，反映 NLP 技术演进趋势。
*   **覆盖面广且细分**：从通用 NLP 任务扩展到医疗、法律、汽车、财经等垂直领域，满足专业化需求。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81868 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，且每个项目均附带完整代码。它旨在为开发者提供从基础概念到高级应用的全方位实践指南，是学习和探索人工智能领域的优质资料库。该项目通过丰富的实战案例，帮助学习者快速掌握各细分领域的核心技术与实现逻辑。

### 2. 核心功能
*   **海量项目集合**：涵盖500多个独立的人工智能相关项目，内容覆盖广泛。
*   **全栈代码支持**：所有项目均提供可运行的源代码，便于直接复现和学习。
*   **多领域覆盖**：全面包含机器学习、深度学习、计算机视觉和自然语言处理四大核心板块。
*   **分类清晰**：通过标签将项目按技术领域细分，方便用户按需查找特定类型的算法或应用。

### 3. 适用场景
*   **初学者入门学习**：适合希望从零开始接触AI并希望通过代码实践理解理论的学习者。
*   **开发者项目灵感**：适合需要寻找实战案例来启发新项目思路或构建个人作品集的工程师。
*   **技术调研与参考**：适合研究人员或学生快速查阅各类主流AI算法的具体实现方式和应用场景。

### 4. 技术亮点
*   **Awesome列表属性**：作为知名的“Awesome”系列资源，其内容经过筛选和质量把控，具有极高的参考价值。
*   **Python生态集成**：虽然标记为“None”编程语言，但鉴于其标签包含Python及AI领域特性，实际项目大多基于Python主流框架（如TensorFlow, PyTorch等）。
*   **结构化知识体系**：通过明确的标签体系（如`computer-vision`, `nlp`），构建了结构化的AI知识图谱，便于系统性学习。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35531 | 🍴 7357 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33241 | 🍴 3159 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是专为机器学习互操作性设计的开放标准。它旨在弥合不同深度学习框架之间的鸿沟，允许模型在PyTorch、TensorFlow等环境间无缝迁移和部署。

2. **核心功能**
*   定义开放的模型格式，实现跨框架的模型交换。
*   支持从训练框架到推理引擎的高效模型转换。
*   提供统一的计算图表示，简化多硬件平台的部署流程。

3. **适用场景**
*   需要将PyTorch或Keras训练的模型部署到不支持原生框架的生产环境中。
*   在不同深度学习框架之间迁移模型架构以进行对比实验。
*   利用ONNX Runtime等推理引擎优化模型在CPU、GPU或边缘设备上的运行速度。

4. **技术亮点**
*   **生态兼容性**：原生支持PyTorch、TensorFlow、scikit-learn等主流AI库。
*   **部署灵活性**：作为中间表示层，屏蔽底层硬件差异，提升跨平台可用性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21169 | 🍴 3972 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
该项目是一部关于机器学习工程实践的开放书籍，旨在填补从理论模型到生产环境部署之间的知识空白。它系统性地讲解了如何高效地进行大规模模型训练、调试、推理及基础设施管理，是MLOps领域的权威指南。

### 2. 核心功能
*   提供大规模分布式训练的最佳实践，涵盖PyTorch、Slurm集群管理及GPU优化技巧。
*   深入解析大语言模型（LLM）的推理加速、量化技术及内存管理策略。
*   包含详细的故障排除与调试指南，帮助工程师解决训练过程中的常见瓶颈和错误。
*   指导如何构建可扩展的机器学习基础设施，包括存储优化、网络配置及MLOps流程自动化。

### 3. 适用场景
*   需要从零搭建或优化大规模深度学习集群的机器学习工程师。
*   致力于提升大语言模型训练效率、降低算力成本的数据科学家。
*   负责将实验性模型部署到生产环境并需确保高可用性和低延迟的MLOps专家。
*   希望系统学习机器学习系统工程知识，弥补传统学术教育与工业界实践差距的学习者。

### 4. 技术亮点
*   **实战导向**：内容基于Hugging Face等工业级真实案例，而非纯理论推导。
*   **全栈覆盖**：从底层硬件（GPU/网络）到上层框架（Transformers/PyTorch）提供端到端解决方案。
*   **持续更新**：作为开源社区项目，紧密跟随AI硬件和软件生态的快速迭代。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18421 | 🍴 1174 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17326 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15416 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13154 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11577 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10668 | 🍴 5709 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，且每个项目均附带完整代码。它旨在为开发者提供从基础概念到高级应用的全方位实践指南，是学习和探索人工智能领域的优质资料库。该项目通过丰富的实战案例，帮助学习者快速掌握各细分领域的核心技术与实现逻辑。

### 2. 核心功能
*   **海量项目集合**：涵盖500多个独立的人工智能相关项目，内容覆盖广泛。
*   **全栈代码支持**：所有项目均提供可运行的源代码，便于直接复现和学习。
*   **多领域覆盖**：全面包含机器学习、深度学习、计算机视觉和自然语言处理四大核心板块。
*   **分类清晰**：通过标签将项目按技术领域细分，方便用户按需查找特定类型的算法或应用。

### 3. 适用场景
*   **初学者入门学习**：适合希望从零开始接触AI并希望通过代码实践理解理论的学习者。
*   **开发者项目灵感**：适合需要寻找实战案例来启发新项目思路或构建个人作品集的工程师。
*   **技术调研与参考**：适合研究人员或学生快速查阅各类主流AI算法的具体实现方式和应用场景。

### 4. 技术亮点
*   **Awesome列表属性**：作为知名的“Awesome”系列资源，其内容经过筛选和质量把控，具有极高的参考价值。
*   **Python生态集成**：虽然标记为“None”编程语言，但鉴于其标签包含Python及AI领域特性，实际项目大多基于Python主流框架（如TensorFlow, PyTorch等）。
*   **结构化知识体系**：通过明确的标签体系（如`computer-vision`, `nlp`），构建了结构化的AI知识图谱，便于系统性学习。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35531 | 🍴 7357 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### Netron 项目分析

1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架和文件格式，帮助用户直观地查看和理解模型结构。

2. **核心功能**
*   支持查看多种深度学习框架（如 PyTorch、TensorFlow、Keras 等）生成的模型文件。
*   提供清晰的计算图可视化，展示层与层之间的连接关系及数据流向。
*   兼容广泛的数据格式，包括 ONNX、CoreML、SafeTensors 及 TensorFlow Lite 等。
*   允许用户检查模型参数、权重数值及张量形状等详细信息。

3. **适用场景**
*   研究人员在调试复杂神经网络架构时，用于快速定位结构问题。
*   开发者将模型从训练框架导出为 ONNX 或其他格式后，验证转换的正确性。
*   初学者通过可视化界面直观理解不同机器学习模型的工作原理和数据流。

4. **技术亮点**
*   基于 JavaScript 开发，具有极高的跨平台兼容性，无需安装即可在浏览器或桌面端运行。
*   拥有庞大的社区支持和高人气（3万+星标），证明了其在 AI 工具链中的广泛认可度。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33241 | 🍴 3159 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究者提供了必备的核心知识速查表（Cheat Sheets）。它汇总了关键概念与代码示例，旨在帮助研究人员快速回顾和掌握相关技术细节。

2. **核心功能**
*   提供深度学习与机器学习领域的关键概念速查指南。
*   涵盖主流库如 Keras、NumPy、SciPy 和 Matplotlib 的使用技巧。
*   整理人工智能相关的核心算法与理论要点。
*   以文档化形式呈现，便于快速检索和学习参考。

3. **适用场景**
*   深度学习初学者快速建立知识框架和复习基础概念。
*   机器学习研究员在编码过程中查阅特定库（如 NumPy/Keras）的常用函数用法。
*   数据科学家在准备面试或项目汇报时作为快速参考资料。
*   希望系统化梳理 AI 理论知识的技术人员。

4. **技术亮点**
*   聚焦于“速查”特性，内容精炼，适合高频查阅而非长篇阅读。
*   覆盖从底层数学库（NumPy/SciPy）到高层框架（Keras）及可视化（Matplotlib）的全栈工具链。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15416 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户轻松入门并实现就业实战。内容涵盖Python编程、数学基础、机器学习、数据分析、深度学习以及计算机视觉和自然语言处理等热门技术领域。

2. **核心功能**
*   提供系统化的AI学习路径图，引导学习者从基础到进阶。
*   收录近200个高质量的实战案例和项目源码，强调动手能力。
*   配套免费提供详细的学习教材和资源，降低自学门槛。
*   覆盖Python及主流AI框架（如PyTorch、TensorFlow、Keras等）的技术栈。

3. **适用场景**
*   希望从零开始系统学习人工智能技术的初学者。
*   需要丰富实战项目经验以提升就业竞争力的求职者。
*   寻求最新AI领域资源和技术路线参考的数据科学家或工程师。
*   想要快速掌握特定AI子领域（如CV、NLP）技能的自学者。

4. **技术亮点**
*   高度整合了算法理论与工程实践，涵盖从底层数学到上层应用的全链路知识。
*   兼容多种主流深度学习框架（TensorFlow 1/2, PyTorch, Keras, Caffe），适应不同技术偏好。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13154 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 项目名称：Ludwig

1. **中文简介**
   Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大语言模型（LLM）、神经网络及其他人工智能模型。它通过简化复杂的人工智能开发流程，让数据科学家和工程师能够专注于模型训练与优化，而无需编写大量底层代码。

2. **核心功能**
   *   支持大语言模型（如 LLaMA、Mistral）的微调与训练，简化了 LLM 的开发流程。
   *   提供基于 PyTorch 的深度学习和机器学习能力，涵盖计算机视觉、自然语言处理等领域。
   *   采用数据-centric（以数据为中心）的设计理念，强调数据质量对模型性能的影响。
   *   具备低代码特性，用户可通过配置文件快速搭建和评估复杂的神经网络模型。

3. **适用场景**
   *   需要对开源大语言模型（如 LLaMA2、Mistral）进行领域特定微调的企业或研究人员。
   *   希望快速原型化并部署深度学习模型（如图像分类、文本生成）的数据科学团队。
   *   致力于通过改进数据集来提升模型效果，而非单纯调整模型架构的数据中心型项目。

4. **技术亮点**
   *   无缝集成主流大语言模型生态（支持 Llama、Mistral 等），降低了 LLM 应用的门槛。
   *   结合传统深度学习与现代 LLM 训练需求，提供统一且易用的低代码接口。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9138 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8932 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6988 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6261 | 🍴 745 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81868 | 🍴 15250 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73361 | 🍴 8957 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52411 | 🍴 10613 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- **1. 中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深入线性代数、PyTorch 及 NLTK 等基础理论与工具。该项目集成了 TensorFlow 2 等多种主流框架，旨在通过代码实践帮助用户系统掌握人工智能核心技能。

**2. 核心功能**
*   提供从经典算法到深度学习的完整机器学习实战代码实现。
*   包含线性代数等数学基础知识的讲解与 Python 代码演示。
*   集成 PyTorch、TensorFlow 2 和 NLTK 等主流 AI 开发框架的使用教程。
*   覆盖 NLP、推荐系统、计算机视觉等多个领域的典型应用场景案例。
*   梳理并实现了包括 SVM、K-Means、LSTM 在内的多种核心算法逻辑。

**3. 适用场景**
*   初学者系统性地构建机器学习和深度学习知识体系。
*   数据科学从业者查找特定算法（如聚类、分类）的代码参考范例。
*   研究人员利用预置脚本快速验证线性代数或 NLP 相关理论。
*   准备面试的技术人员复习常见 AI 算法原理及 Python 实现细节。

**4. 技术亮点**
*   项目拥有极高的社区关注度（42k+ 星标），证明其内容质量与实用性广受认可。
*   标签涵盖了从传统统计学习（如 AdaBoost、Apriori）到前沿深度学习（如 DNN、RNN）的完整技术栈。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42393 | 🍴 11537 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建人工智能系统来深入理解其原理，并掌握将其产品化交付给最终用户的全流程技能。它强调“学习、构建、发布”的闭环实践，帮助开发者从理论走向工程落地。

2. **核心功能**
*   提供涵盖LLM、计算机视觉及强化学习等领域的从头构建教程与课程资源。
*   演示如何集成AI代理（Agents）、MCP协议及群体智能等前沿架构。
*   指导开发者利用Python和Rust等语言实现高性能的生成式AI应用。
*   包含完整的工程化指南，教授如何将AI模型转化为可交付的产品。

3. **适用场景**
*   AI工程师希望深入理解大语言模型底层机制而非仅调用API的场景。
*   团队需要构建基于自定义Agent或群体智能的复杂自动化工作流。
*   学习者希望系统性地从基础数学和代码层面掌握深度学习与NLP技术。

4. **技术亮点**
*   结合了Python生态与Rust的高性能优势，兼顾开发效率与运行速度。
*   涵盖MCP（Model Context Protocol）等新兴AI交互标准，体现技术前瞻性。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38929 | 🍴 6533 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35531 | 🍴 7357 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33751 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28672 | 🍴 3503 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25933 | 🍴 2931 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21726 | 🍴 3302 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35531 | 🍴 7357 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **项目名称：** Skyvern

**中文简介**
Skyvern 是一个基于人工智能的自动化平台，能够模拟人类操作来执行复杂的浏览器工作流。它利用大语言模型（LLM）和计算机视觉技术，无需编写代码即可自动处理网页交互任务。该项目旨在为 RPA（机器人流程自动化）提供更智能、更灵活的替代方案。

**核心功能**
*   **AI 驱动的操作识别**：通过视觉理解和 LLM 分析页面结构，自动定位并点击按钮或填写表单。
*   **跨平台浏览器支持**：底层兼容 Playwright 和 Puppeteer，支持在 Chrome 等主流浏览器中运行自动化脚本。
*   **无代码/低代码工作流**：用户只需描述任务目标，系统即可自动生成并执行相应的浏览器操作步骤。
*   **动态内容适应**：相比传统 Selenium 脚本，能更好地适应网页布局变化和非结构化数据。
*   **API 集成能力**：提供 API 接口，便于将自动化能力嵌入到其他业务系统中。

**适用场景**
*   **企业级 RPA 替代**：用于自动化处理需要频繁登录、跳转多页面且逻辑复杂的后台管理系统任务。
*   **数据抓取与录入**：从非结构化或反爬机制较强的网站中提取数据，并自动填入内部数据库或 CRM 系统。
*   **在线业务流程自动化**：如自动完成电商平台的下单、比价、库存监控或社交媒体内容发布。
*   **测试环境搭建**：快速生成基于自然语言描述的 UI 自动化测试用例，降低测试维护成本。

**技术亮点**
*   **结合 LLM 与计算机视觉**：不仅解析 DOM 树，还通过截图理解页面视觉元素，解决传统自动化工具对动态页面适应性差的问题。
*   **类人交互逻辑**：模拟人类的“看-想-做”循环，能够处理弹窗确认、验证码识别等复杂交互场景。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22496 | 🍴 2103 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首席平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量控制及团队协作，并配备开发者API以加速视觉AI开发流程。

2. **核心功能**
*   支持图像、视频及3D数据的多种标注格式（如边界框、语义分割）。
*   集成AI辅助标注功能，显著提升数据标记效率与准确性。
*   提供团队协作机制、质量保证检查及详细的数据分析面板。
*   开放开发者API，便于与现有深度学习框架（PyTorch/TensorFlow）集成。

3. **适用场景**
*   需要大规模构建高质量标注数据集的计算机视觉研发项目。
*   涉及多人协作进行视频或3D复杂场景标注的企业级工作流。
*   结合自动化算法进行预标注，以人工复核为主的高效数据清洗场景。

4. **技术亮点**
*   作为行业领先的开源平台，拥有极高的社区活跃度（16k+星标）和广泛的生态兼容性。
*   提供从开源私有部署到云端SaaS服务的灵活产品形态，适应不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16327 | 🍴 3768 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目是一个面向计算机视觉的高级AI可解释性工具包，旨在揭示深度学习模型的决策依据。它广泛支持卷积神经网络（CNN）和视觉Transformer等多种架构，涵盖分类、检测及分割等任务。通过可视化注意力热力图，帮助用户深入理解模型如何关注图像中的关键区域。

2. **核心功能**
*   支持多种主流模型架构，包括CNN和Vision Transformers。
*   提供全面的视觉任务支持，如图像分类、目标检测和语义分割。
*   集成多种经典可视化方法，如Grad-CAM、Score-CAM等。
*   具备图像相似度分析能力，辅助理解特征匹配机制。

3. **适用场景**
*   计算机视觉模型的调试与错误分析，定位误判原因。
*   医疗影像或自动驾驶等高可靠性要求领域的模型透明度验证。
*   学术研究中对深度神经网络内部决策逻辑的解释性研究。

4. **技术亮点**
*   高度兼容PyTorch生态，同时适配最新的Vision Transformer架构。
*   作为XAI（可解释人工智能）领域的标准参考实现，拥有极高的社区关注度（近1.3万星标）。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12917 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它旨在为深度学习框架提供可微分的计算机视觉原语，从而简化图像处理和机器视觉任务的开发流程。该项目融合了传统计算机视觉与深度学习技术，适用于需要高效、模块化视觉算法的场景。

### 2. 核心功能
*   **可微分计算机视觉算子**：提供完全可微分的图像处理函数，便于在神经网络中进行端到端优化。
*   **几何与空间变换**：支持相机内参标定、投影、旋转及仿射变换等几何操作。
*   **图像预处理与增强**：内置丰富的色彩空间转换、滤波、边缘检测及数据增强工具。
*   **PyTorch 原生集成**：作为 PyTorch 的扩展库，无缝对接现有深度学习工作流，支持 GPU 加速。
*   **模块化视觉模块**：包含特征提取、立体视觉、SLAM（同步定位与地图构建）等高级视觉组件。

### 3. 适用场景
*   **机器人视觉系统**：用于机器人的环境感知、导航及抓取任务中的实时图像处理。
*   **自动驾驶算法开发**：在车道线检测、物体识别和深度估计等场景中集成几何约束。
*   **医学影像分析**：利用其可微分特性优化图像配准、分割及三维重建流程。
*   **混合学习模型研究**：在传统 CV 管道中嵌入深度学习模块，以结合领域知识与数据驱动方法。

### 4. 技术亮点
*   **端到端可训练性**：打破传统 CV 与 DL 的界限，允许视觉预处理步骤直接参与梯度反向传播。
*   **高性能硬件加速**：充分利用 CUDA 和 GPU 资源，实现实时或近实时的复杂图像处理。
*   **开源社区活跃**：拥有高星标和活跃贡献者群体，持续更新并遵循 Hacktoberfest 等开源文化。
- 链接: https://github.com/kornia/kornia
- ⭐ 11279 | 🍴 1203 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3457 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3288 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，倡导“龙虾方式”的数据自主权。它让用户能够完全掌控自己的数据，构建专属的智能助理。该项目旨在通过本地化部署实现隐私保护与高效辅助的结合。

2. **核心功能**
*   **跨平台兼容**：支持在任何主流操作系统和硬件平台上运行。
*   **数据所有权**：强调用户拥有并控制所有数据，无需依赖外部云服务。
*   **个性化定制**：作为个人 AI 助手，可根据用户需求进行深度配置。
*   **开源透明**：基于 TypeScript 开发，代码公开，便于社区协作与安全审计。
*   **轻量化架构**：采用“龙虾”隐喻的高效轻量设计，易于部署和维护。

3. **适用场景**
*   **隐私敏感型用户**：希望在不泄露个人数据的前提下享受 AI 便利性的开发者或专业人士。
*   **本地化部署需求**：需要在离线环境或私有服务器上运行 AI 助手的团队或个人。
*   **技术爱好者**：喜欢折腾自定义 AI 工具、关注数据主权的技术极客。
*   **跨设备办公**：需要在不同操作系统（如 Windows、macOS、Linux）间无缝切换使用的多平台工作者。

4. **技术亮点**
*   基于 TypeScript 构建，兼具类型安全与开发效率。
*   设计哲学强调“Own Your Data”，从架构层面保障用户数据隐私。
*   “Crustacean/Lobster”隐喻代表其轻量、坚固且适应性强的小型化部署特性。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383367 | 🍴 80528 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 256929 | 🍴 22887 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 216705 | 🍴 40650 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个支持自托管和云部署的公平代码工作流自动化平台，具备原生 AI 能力并拥有 400 多种集成。它结合了可视化构建与自定义代码开发的优势，适用于需要灵活控制数据流的开发者与技术人员。

### 2. 核心功能
- 提供可视化拖拽界面与自定义代码相结合的混合开发模式，平衡易用性与灵活性。
- 内置原生 AI 功能，支持将大语言模型能力直接嵌入自动化工作流中。
- 拥有 400 多种预置集成连接器，覆盖主流 API 和服务，实现跨平台数据互通。
- 支持自托管部署，确保数据隐私可控，同时也提供便捷的云端托管选项。
- 作为 iPaaS（集成平台即服务）解决方案，支持复杂的数据流处理和逻辑编排。

### 3. 适用场景
- **企业数据同步与整合**：自动在不同 SaaS 应用（如 CRM、ERP、数据库）之间同步和转换数据。
- **AI 增强型业务流程**：利用原生 AI 能力自动处理文档摘要、分类或生成内容，并触发后续自动化操作。
- **定制化后端服务编排**：开发者通过编写自定义代码节点，构建复杂的后端逻辑和微服务调度流程。
- **个人开发者效率工具**：无需大量前端资源，即可快速搭建监控报警、定时任务或个人助手类自动化脚本。

### 4. 技术亮点
- **公平代码（Fair-code）许可**：在保持开源核心的同时，允许商业使用但限制直接转售，平衡了社区贡献与商业可持续性。
- **MCP 协议支持**：标签显示其支持 Model Context Protocol (MCP)，意味着它能更标准化地与各种 AI 模型上下文进行交互。
- **TypeScript 原生构建**：基于 TypeScript 开发，提供了良好的类型安全和现代化的开发体验，便于社区贡献扩展。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196930 | 🍴 59425 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建 AI，实现其普及化愿景。该项目旨在提供必要的工具，让用户能够将精力集中在真正重要的事务上。

2. **核心功能**
*   具备自主规划与执行复杂任务的能力。
*   支持多模型集成，兼容 OpenAI、Anthropic Claude 及 Llama 等 API。
*   拥有互联网浏览、文件读写及代码执行等扩展能力。
*   提供模块化架构，便于用户根据需求定制和开发新功能。

3. **适用场景**
*   自动化完成需要多步骤推理的复杂研究或数据收集任务。
*   作为个人助手处理日常行政事务，如邮件整理或日程安排。
*   开发者用于测试和验证新一代自主智能体（Agentic AI）的应用逻辑。
*   快速搭建原型，探索大型语言模型在自动化工作流中的潜力。

4. **技术亮点**
*   采用先进的 Agent 架构，实现了从目标设定到行动执行的闭环自动化。
*   高度可定制化，允许通过简单配置接入不同的 LLM 后端及外部工具。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185596 | 🍴 46077 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165962 | 🍴 21462 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164214 | 🍴 30419 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157113 | 🍴 46177 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 152661 | 🍴 8722 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151997 | 🍴 9592 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

