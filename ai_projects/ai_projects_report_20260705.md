# GitHub AI项目每日发现报告
日期: 2026-07-05

## 新发布的AI项目

### rnskill
- **1. 中文简介**
该项目是“雪踏乌云”整理的 AI Agent 技能（Skills）合集，旨在为人工智能代理提供丰富的能力扩展。它通过模块化的方式封装了各种实用工具与操作指令，方便开发者快速集成到 AI 应用流程中。

**2. 核心功能**
*   提供多样化的 AI Agent 专用技能库，支持灵活调用。
*   模块化设计，便于将特定功能嵌入到现有的 Agent 工作流中。
*   由社区开发者“雪踏乌云”维护，包含经过实战验证的工具集合。
*   降低开发门槛，无需从零编写底层逻辑即可增强 AI 能力。

**3. 适用场景**
*   开发具备复杂任务处理能力的自动化 AI 助手。
*   构建需要调用外部工具或执行特定操作的智能代理系统。
*   快速原型开发，用于测试不同技能组合对 Agent 性能的影响。
*   教育或研究用途，学习如何为 LLM 设计有效的技能插件。

**4. 技术亮点**
*   项目虽标注语言为 None，但通常此类技能集采用 YAML、JSON 或标准 Agent 框架配置格式，具有极高的兼容性和可移植性。
*   聚焦于“技能”而非完整应用，体现了微服务化在 AI Agent 架构中的应用趋势。
- 链接: https://github.com/Pluviobyte/rnskill
- ⭐ 86 | 🍴 9 | 语言: 未知

### anima-use-google
- 以下是关于 GitHub 项目 `anima-use-google` 的技术分析：

1. **中文简介**
   该项目是一个结合 MCP 服务器与浏览器侧边栏扩展的工具，允许 AI 智能体利用用户已登录的浏览器会话执行 Google AI Mode 搜索。它通过桥接本地浏览器环境，使 AI 能够直接获取第一手的搜索结果。

2. **核心功能**
   - 提供基于 Model Context Protocol (MCP) 的标准服务器接口，便于 AI 工具集成。
   - 开发浏览器侧边栏扩展，用于捕获和管理用户的 Google 登录会话状态。
   - 支持 AI 智能体模拟人类操作，直接在浏览器中运行 Google AI Mode 搜索请求。
   - 实现本地浏览器环境与远程 AI 代理之间的安全数据通道。

3. **适用场景**
   - AI 助手需要实时访问特定于地理位置或个性化账号的 Google 搜索结果时。
   - 开发者希望为基于 MCP 的 AI 代理添加具备真实互联网浏览能力的搜索模块。
   - 需要绕过传统 API 限制，直接利用 Google AI Overviews 进行深度信息检索的场景。

4. **技术亮点**
   - 创新性地将 MCP 协议与浏览器自动化（Headless/Extension）相结合，解决了 AI 无法直接登录受限网站的问题。
   - 利用用户自身的已验证会话，确保了搜索结果的准确性和时效性，无需依赖第三方搜索 API 密钥。
- 链接: https://github.com/animaios/anima-use-google
- ⭐ 18 | 🍴 0 | 语言: JavaScript
- 标签: agent-search, ai, ai-agents, ai-search, mcp-search

### OmniPost-AI
- 描述: AI-powered Chrome extension for generating and publishing posts to Facebook, Threads, and X using ChatGPT or Gemini.
- 链接: https://github.com/wanglinsaputra/OmniPost-AI
- ⭐ 17 | 🍴 6 | 语言: TypeScript
- 标签: ai, automation, chatgpt, chrome-extension, gemini

### hh-ai-agent
- 1. **中文简介**
该项目是一个基于 Python 开发的自动化 AI 代理，专为俄罗斯知名招聘平台 hh.ru 设计。其主要功能是自动响应职位申请，帮助用户提高求职效率并减少重复性操作。

2. **核心功能**
*   集成人工智能算法以生成符合语境的求职回复。
*   自动登录并操作 hh.ru 平台进行职位投递。
*   简化繁琐的申请流程，实现全天候自动化响应。
*   针对特定职位需求定制个性化的沟通内容。

3. **适用场景**
*   求职者需要同时向大量相似职位投递简历时。
*   希望节省手动填写申请信息时间的高效求职者。
*   非俄语母语者寻求自动化辅助以优化在俄求职体验。
*   招聘代理或人力资源顾问批量处理客户申请任务。

4. **技术亮点**
*   利用自然语言处理（NLP）技术实现智能文案生成。
*   针对特定招聘平台的 API 或交互逻辑进行了优化适配。
- 链接: https://github.com/fikstt2/hh-ai-agent
- ⭐ 15 | 🍴 1 | 语言: Python

### typeone-ai-skill-extractor
- 1. **中文简介**
该项目旨在将冗长的AI多轮对话精炼为可复用的“技能”上下文模块。这些提取出的技能可以直接迁移至新对话窗口中，作为高效的知识预设。它解决了长对话信息冗余和重复提示的问题。

2. **核心功能**
*   自动从长对话历史中提取关键逻辑与指令。
*   将非结构化对话转化为标准化的可迁移Skill对象。
*   支持将Skill无缝注入新的AI对话上下文中。
*   减少重复提示词输入，提升对话初始化效率。

3. **适用场景**
*   需要反复执行相同复杂任务的自动化工作流。
*   希望在新会话中快速加载专家级角色设定的场景。
*   团队内部共享最佳实践或标准操作程序（SOP）。
*   优化长周期项目中上下文窗口成本过高的问题。

4. **技术亮点**
*   实现了对话知识的结构化沉淀与复用机制。
*   降低了用户维护复杂Prompt模板的成本。
*   提升了大模型在特定垂直领域的响应一致性。
- 链接: https://github.com/tttypeone1-ship-it/typeone-ai-skill-extractor
- ⭐ 15 | 🍴 1 | 语言: 未知

### icml2026-ai-bio
- 描述: ICML 2026 · AI × Biomedical Papers — 315 curated papers on protein design, genomics, drug discovery, clinical AI, and more
- 链接: https://github.com/BioTender-max/icml2026-ai-bio
- ⭐ 14 | 🍴 0 | 语言: 未知

### Duetto
- 描述: Duetto — self-hostable listen-together player for two, with an AI companion that actually listens. 可自部署的双人一起听歌播放器，AI 真的听过你们的每一首歌。
- 链接: https://github.com/avisforevelyn/Duetto
- ⭐ 13 | 🍴 6 | 语言: JavaScript

### Eventide
- 描述: 给 AI 伴侣接入身体涨落、梦境联动与互动结算的生理状态系统
- 链接: https://github.com/chuli1122/Eventide
- ⭐ 13 | 🍴 3 | 语言: Python

### ComfyUI-Krea2-Ostris-Edit
- 描述: Comfy UI Nodes for Krea 2 LoRAs trained with AI Toolkit Experimental Edit
- 链接: https://github.com/ostris/ComfyUI-Krea2-Ostris-Edit
- ⭐ 13 | 🍴 0 | 语言: Python

### glm-5.2-free-desktop-app
- 描述: glm 5.2 free access open weights z.ai zhipu ai mit license github repository coding agent long horizon reasoning indexshare sparse attention 1m context window 128k output tokens flexible effort level local deployment guide unsloth quantization gguf llama.cpp vllm sglang ktransformers cloudflare workers free api key
- 链接: https://github.com/glm-zai/glm-5.2-free-desktop-app
- ⭐ 13 | 🍴 0 | 语言: C#
- 标签: bigmodel, desktop-ai, free-ai-api, glm, glm-4-7

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具集合，涵盖了从基础的分词、命名实体识别到高级的知识图谱构建与对话系统资源。该项目整合了大量高质量的数据集、预训练模型（如 BERT、GPT-2）以及各类垂直领域的专用词库和算法工具，旨在降低 NLP 开发门槛。它既是开发者的工具箱，也是研究人员获取中文 NLP 最新资源和基准测试的重要仓库。

2. **核心功能**
*   **基础 NLP 能力**：提供敏感词检测、繁简转换、中英文分词、词性标注、命名实体识别（NER）及情感分析等核心功能。
*   **丰富数据与词库资源**：内置大量垂直领域词库（如医学、法律、汽车、IT 等）、人名地名库、停用词表及中英文对照数据集。
*   **深度学习模型集成**：收录了基于 BERT、RoBERTa、ALBERT 等主流预训练模型的代码实现、微调教程及在 NER、文本分类等任务上的最佳实践。
*   **语音与 OCR 工具**：包含中文语音识别（ASR）相关数据与工具、中文手写汉字识别（OCR）库及音频数据增强方案。
*   **知识图谱与应用场景**：提供知识图谱构建、实体链接、问答系统（QA）搭建资源，以及简历解析、自动摘要和对话机器人等具体应用场景的代码参考。

3. **适用场景**
*   **中文 NLP 初学者与研究者**：需要快速了解中文 NLP 生态、获取标准数据集（如 CLUE 基准）、复现经典论文代码或进行学术调研。
*   **企业级文本内容安全审核**：利用其敏感词库、暴恐词表及反动词表，快速搭建用于过滤违规内容的自动化审核系统。
*   **垂直行业智能客服与问答系统开发**：借助其提供的医学、法律、金融等领域专用词库和预训练模型，快速构建具备专业领域知识的智能问答机器人。
*   **信息抽取与结构化数据处理**：利用其身份证、手机号、邮箱抽取功能及依存句法分析工具，从非结构化文本中提取关键实体信息用于构建知识图谱。

4. **技术亮点**
*   **高度集成与一站式服务**：将分散的 NLP 资源、工具链和数据集集中管理，极大节省了开发者搜集和整理资料的时间。
*   **紧跟前沿技术**：持续更新包括 Transformer 系列（BERT, GPT-2, RoBERTa）、知识图谱表示学习及对抗样本生成等最新的 AI 技术成果。
*   **注重实用性与落地**：不仅提供理论模型，还包含了大量可直接运行的代码示例、API 调用方法及针对中文特性的优化方案（如全词覆盖 BERT）。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81615 | 🍴 15255 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。每个项目均附带完整代码，适合快速入门和实践。该项目以“Awesome”列表形式组织，方便开发者按领域查找示例。

### 2. 核心功能
- 提供500个AI项目的分类汇总，覆盖主流技术领域。
- 每个项目附带可运行的Python代码，便于直接测试和学习。
- 支持按标签筛选，如机器学习、深度学习、NLP等。
- 作为学习资源库，帮助开发者快速掌握AI核心技术。
- 定期更新，保持项目时效性和实用性。

### 3. 适用场景
- 初学者通过示例代码快速理解AI概念。
- 研究人员寻找特定领域的参考实现。
- 企业团队评估新技术在业务中的可行性。
- 教育者设计课程时引用实际案例。

### 4. 技术亮点
- 项目代码均为开源且可直接运行，减少配置成本。
- 标签分类清晰，便于按需检索目标内容。
- 覆盖从基础到高级的多层次AI应用场景。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35163 | 🍴 7317 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。

2. **核心功能**
*   支持 TensorFlow、PyTorch、ONNX、Keras 等广泛模型的格式转换与可视化。
*   提供清晰的层级结构和数据流图展示，便于理解模型架构。
*   允许用户在不同层之间导航，并查看具体的参数和权重信息。
*   兼容多种文件格式，包括 CoreML、TensorFlow Lite 和 Safetensors 等。

3. **适用场景**
*   开发者调试和优化深度学习模型时，快速检查网络结构是否正确。
*   研究人员对比不同框架下的模型实现，验证模型转换的一致性。
*   非技术人员向团队或客户演示复杂的机器学习模型工作原理。
*   在部署前验证模型文件是否损坏或格式是否符合预期。

4. **技术亮点**
*   基于 Web 技术构建，无需安装即可通过浏览器或桌面应用使用，跨平台兼容性极佳。
*   轻量级且响应迅速，能够高效渲染大规模复杂模型。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33181 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是机器学习领域的开放标准，旨在促进不同框架间的模型互操作性。它允许开发者轻松地将模型从一种深度学习框架迁移到另一种，打破生态壁垒。

2. **核心功能**
*   提供统一的开放标准，实现跨平台、跨框架的模型交换与部署。
*   支持将主流框架（如PyTorch、TensorFlow、Keras）训练的模型转换为通用格式。
*   集成推理引擎，使模型能在各种硬件和后端环境中高效运行。
*   维护丰富的算子库，覆盖绝大多数深度神经网络的常见操作。

3. **适用场景**
*   需要将模型从训练框架（如PyTorch）部署到生产环境或特定硬件（如移动设备、边缘计算）时。
*   希望在多个深度学习框架之间迁移代码或复用已训练好的模型权重。
*   构建需要兼容多种AI框架的大型机器学习基础设施或中间件平台。

4. **技术亮点**
*   作为行业事实标准，被微软、Facebook、Amazon等科技巨头广泛支持，生态兼容性极强。
*   通过ONNX Runtime提供高性能的跨平台推理加速，优化了执行效率。
- 链接: https://github.com/onnx/onnx
- ⭐ 21092 | 🍴 3962 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
该项目是一部关于机器学习工程实践的“开源书籍”，全面涵盖了从模型训练到部署的全流程技术细节。它深入探讨了高性能计算、分布式训练以及大规模语言模型（LLM）的工程优化方法。

2. **核心功能**
*   提供大规模分布式训练的最佳实践与配置指南。
*   详解大型语言模型（LLM）的训练、微调及推理优化策略。
*   涵盖GPU加速、网络通信及存储优化等高并发工程技巧。
*   介绍MLOps工作流及模型调试、可观测性相关工具链。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习集群的工程团队。
*   致力于降低大语言模型训练成本并提升推理效率的数据科学家。
*   希望深入理解PyTorch底层机制及分布式训练原理的高级开发者。
*   正在实施或改进MLOps流水线以实现模型规模化部署的企业。

4. **技术亮点**
*   内容紧跟前沿，特别针对Transformer架构和LLM时代的技术挑战进行了专项更新。
*   不仅提供理论，更侧重于可落地的代码示例、配置模板及性能调优实测数据。
*   覆盖了从底层硬件（Slurm, GPUs）到上层框架（PyTorch, Transformers）的全栈知识体系。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18239 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17263 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15409 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11551 | 🍴 905 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10659 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。每个项目均附带完整代码，适合快速入门和实践。该项目以“Awesome”列表形式组织，方便开发者按领域查找示例。

### 2. 核心功能
- 提供500个AI项目的分类汇总，覆盖主流技术领域。
- 每个项目附带可运行的Python代码，便于直接测试和学习。
- 支持按标签筛选，如机器学习、深度学习、NLP等。
- 作为学习资源库，帮助开发者快速掌握AI核心技术。
- 定期更新，保持项目时效性和实用性。

### 3. 适用场景
- 初学者通过示例代码快速理解AI概念。
- 研究人员寻找特定领域的参考实现。
- 企业团队评估新技术在业务中的可行性。
- 教育者设计课程时引用实际案例。

### 4. 技术亮点
- 项目代码均为开源且可直接运行，减少配置成本。
- 标签分类清晰，便于按需检索目标内容。
- 覆盖从基础到高级的多层次AI应用场景。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35163 | 🍴 7317 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33181 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**：该项目为深度学习与机器学习研究人员提供了 Essential（必备）速查手册。内容涵盖从基础数学工具到高级深度学习框架的关键知识点，旨在作为高效的学习与开发参考指南。

2. **核心功能**：
   - 提供 NumPy、SciPy 和 Matplotlib 等常用科学计算库的快速语法参考。
   - 包含 Keras 等主流深度学习框架的核心 API 使用示例。
   - 整理机器学习与深度学习研究中的关键概念和公式备忘。
   - 针对研究人员优化的结构化知识卡片，便于快速检索。

3. **适用场景**：
   - 深度学习研究员在编码时快速查阅特定函数的参数或用法。
   - 初学者系统性地梳理机器学习工具链（如 NumPy/Matplotlib）的基础操作。
   - 面试准备或知识复盘时，利用速查表快速回顾关键技术点。

4. **技术亮点**：高度精简的知识浓缩形式，聚焦于高频使用的代码片段和理论要点，极大降低了查阅文档的时间成本。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15409 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13108 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1234 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8915 | 🍴 3100 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6218 | 🍴 732 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81615 | 🍴 15255 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和多模态大模型（VLM）进行训练。该项目荣获 ACL 2024 会议认可，旨在简化大模型的指令微调与强化学习过程。

2. **核心功能**
*   支持超过 100 种主流大语言模型及多模态模型的统一微调。
*   集成 LoRA、QLoRA 等高效参数微调（PEFT）及量化技术以节省显存。
*   内置 RLHF（基于人类反馈的强化学习）和 DPO 等对齐训练策略。
*   提供从数据预处理到模型评估的一站式完整工作流程。

3. **适用场景**
*   需要将开源基座模型（如 LLaMA、Qwen、Gemma）适配特定垂直领域任务的研究人员。
*   希望低成本实现模型个性化定制且显存资源有限的开发者。
*   探索大模型指令跟随能力及安全对齐机制的 AI 实验室团队。

4. **技术亮点**
*   高度统一的 API 接口设计，极大降低了多模型切换的学习成本。
*   对低精度量化（如 4-bit/8-bit）和混合精度训练有深度优化，显著提升硬件利用率。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72958 | 🍴 8918 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51695 | 🍴 10430 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 49294 | 🍴 8050 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42353 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37352 | 🍴 6191 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35163 | 🍴 7317 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33711 | 🍴 4691 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28346 | 🍴 3439 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25826 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. **中文简介**
这是一个包含500个AI项目代码的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理领域。它旨在为开发者提供从基础到高级的完整实战案例，帮助快速掌握相关技术。该项目通过丰富的代码示例，降低了AI技术的入门门槛。

### 2. **核心功能**
*   提供大量现成的AI项目代码，覆盖主流算法与模型实现。
*   整合机器学习、深度学习、计算机视觉及NLP四大核心领域的实践案例。
*   作为“Awesome”列表， curated 高质量资源，便于系统性学习与技术参考。
*   所有项目均附带可运行代码，支持直接复现结果以验证理论。
*   结构清晰，按技术领域分类，方便用户快速定位所需的学习材料。

### 3. **适用场景**
*   **初学者入门**：学生或转行者通过阅读和运行代码，快速理解AI基本概念。
*   **项目实战参考**：开发者寻找类似项目的代码结构，加速自身业务场景的开发进程。
*   **技术面试准备**：求职者通过熟悉常见AI项目的实现细节，提升面试中的技术问答能力。
*   **教学辅助材料**：教师或培训师利用这些案例作为课堂演示或作业题目。

### 4. **技术亮点**
*   极高的收藏量（35k+ stars）证明其在社区中具有较高的认可度和实用性。
*   全面的技术栈覆盖，从传统机器学习到前沿的深度学习模型均有涉及。
*   强调“代码即文档”，通过实际可执行的项目而非纯理论来展示技术细节。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35163 | 🍴 7317 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一款利用人工智能技术实现基于浏览器的自动化工作流的工具。它通过结合大语言模型（LLM）和计算机视觉能力，能够像人类一样理解网页内容并执行复杂的交互操作。该项目旨在替代传统的 RPA 方案，提供更智能、更灵活的浏览器自动化解决方案。

### 2. 核心功能
*   **AI 驱动的页面理解**：利用大语言模型分析网页结构，无需编写繁琐的选择器即可识别元素。
*   **计算机视觉辅助交互**：结合视觉识别技术处理动态内容或复杂 UI 界面，提高操作准确率。
*   **自然语言指令执行**：用户可通过自然语言描述任务目标，系统自动将其转化为具体的浏览器操作步骤。
*   **无头浏览器集成**：底层基于 Playwright/Puppeteer 等技术，支持稳定、高效的自动化浏览控制。
*   **API 与工作流支持**：提供 API 接口及工作流编排能力，便于集成到现有业务流程中。

### 3. 适用场景
*   **电商数据爬取与监控**：自动登录电商平台、搜索商品、提取价格及库存信息并更新数据库。
*   **企业内部流程自动化**：自动化处理报销审批、表单填写、内部系统数据录入等重复性 Web 操作。
*   **跨平台账户管理**：自动在多网站间进行登录、注销、密码重置等账户维护操作。
*   **在线服务自动化测试**：模拟用户行为对 Web 应用进行端到端的回归测试和功能验证。

### 4. 技术亮点
*   **混合智能架构**：巧妙融合 LLM 的逻辑推理能力与计算机视觉的环境感知能力，解决了传统脚本难以应对动态网页的问题。
*   **低代码/零代码配置**：大幅降低浏览器自动化的门槛，非技术人员也可通过自然语言定义复杂任务。
*   **高鲁棒性**：相比依赖固定 XPath/CSS 选择器的传统 Selenium 方案，Skyvern 能更好地适应前端页面的细微变化。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22117 | 🍴 2069 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的标注，并提供开源、云和企业版产品及服务。该平台集成了 AI 辅助标注、质量保证、团队协作及开发者 API 等核心能力，旨在助力计算机视觉 AI 的研发。

2. **核心功能**
*   支持图像、视频和 3D 数据的多维度标注，涵盖边界框、语义分割及图像分类等任务。
*   提供 AI 辅助标注功能，显著提升数据处理效率并降低人工成本。
*   内置质量保证机制与团队协作工具，确保标注数据的准确性和一致性。
*   开放开发者 API，便于集成到现有的自动化工作流或定制系统中。

3. **适用场景**
*   训练目标检测模型（如 YOLO、Faster R-CNN）所需的高质量边界框数据集构建。
*   自动驾驶或监控视频中关键帧及动态物体的语义分割标注。
*   大型团队协同进行大规模图像分类或物体识别的数据标注项目。

4. **技术亮点**
*   作为行业领先的开源计算机视觉标注工具，拥有极高的社区活跃度（1.6万+星标）和广泛的生态兼容性（支持 PyTorch/TensorFlow 等主流框架）。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16221 | 🍴 3736 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级AI可解释性工具库，支持卷积神经网络（CNN）和视觉Transformer等多种架构。它提供了包括Grad-CAM、Score-CAM在内的多种方法，广泛应用于分类、目标检测、分割及图像相似度分析等任务。

2. **核心功能**
- 支持CNN和Vision Transformers等多种主流深度学习模型结构。
- 集成Grad-CAM、Score-CAM等经典的可解释性算法以生成类激活图。
- 覆盖图像分类、目标检测、语义分割及图像相似度比对等多类任务。
- 提供可视化工具，直观展示模型决策依据，增强深度学习模型的透明度。

3. **适用场景**
- 深度学习模型调试：通过可视化定位模型关注区域，排查分类或检测错误原因。
- 医疗影像分析：在诊断辅助系统中向医生展示模型判断病灶的依据，建立信任感。
- 自动驾驶感知系统：解释车辆识别障碍物或交通标志的逻辑，提升系统安全性与合规性。
- 学术研究与教学：作为可解释人工智能（XAI）的教学案例或实验基准工具。

4. **技术亮点**
- 生态兼容性强：专为PyTorch设计，无缝对接现有深度学习工作流。
- 算法多样性：不仅包含Grad-CAM，还整合了Score-CAM等多种前沿解释方法。
- 高社区认可度：拥有近1.3万星标，是计算机视觉领域广泛使用的标准可解释性库之一。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12898 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个面向空间人工智能的几何计算机视觉库，专为深度学习应用设计。它利用 PyTorch 构建，提供了可微分的图像处理算子，旨在简化视觉算法在神经网络中的集成与优化。

2. **核心功能**
*   提供基于 PyTorch 的可微分几何计算机视觉算子。
*   支持完整的图像预处理、增强及转换流程。
*   集成多种传统计算机视觉算法（如特征匹配、相机校准）。
*   具备高效的批量处理能力，适配 GPU 加速计算。

3. **适用场景**
*   需要结合几何约束进行图像增强的深度学习训练。
*   开发可微分管线以进行相机姿态估计或三维重建。
*   在机器人视觉系统中实时处理传感器数据。
*   构建端到端的计算机视觉模型，实现从原始图像到语义输出的无缝衔接。

4. **技术亮点**
*   **可微性**：所有算子均支持反向传播，可直接嵌入深度学习框架进行梯度优化。
*   **PyTorch 原生集成**：作为 PyTorch 的一等公民，无需额外依赖即可直接使用。
*   **JIT 编译支持**：兼容 TorchScript，便于模型部署和高性能推理。
- 链接: https://github.com/kornia/kornia
- ⭐ 11261 | 🍴 1195 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3267 | 🍴 400 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2623 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2416 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款个人 AI 助手，支持在任何操作系统和平台上运行，赋予用户完全的数据掌控权。它采用“龙虾”式的设计理念，旨在提供一种自主、灵活且私密的智能体验。

### 2. 核心功能
*   **跨平台兼容性**：支持任意操作系统和平台，实现无缝部署。
*   **数据私有化**：强调“Own Your Data”，确保用户数据由自己掌控而非第三方托管。
*   **个人化定制**：作为专属个人助手，可根据用户需求进行高度定制。
*   **开源生态**：基于开源协议，社区活跃，标签包含“molty”等独特标识。

### 3. 适用场景
*   **隐私敏感型用户**：需要完全控制个人数据、拒绝云服务监控的用户。
*   **多设备开发者**：希望在 Linux、macOS 或 Windows 等不同环境中统一部署 AI 助手的开发者。
*   **独立研究者**：需要本地化运行、低成本维护个人知识库或自动化任务的研究人员。

### 4. 技术亮点
*   **TypeScript 构建**：使用 TypeScript 开发，保证代码类型安全和良好的可维护性。
*   **高关注度项目**：拥有 381,800+ 星标，表明其在社区中具有极高的影响力和认可度。
*   **去中心化架构理念**：通过“龙虾”隐喻强调独立生存与自我防御能力，体现去中心化的设计哲学。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381800 | 🍴 80054 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一个经过验证的代理技能框架与软件开发方法论。它旨在通过结构化的“代理驱动开发”流程，提升软件工程的效率与质量。该项目为开发者提供了一套完整的智能体协作工具链。

2. **核心功能**
*   提供模块化的代理技能库，支持自动化处理各类开发任务。
*   实施子代理驱动开发模式，实现复杂任务的分解与并行执行。
*   整合头脑风暴与设计阶段，辅助早期需求梳理与技术选型。
*   覆盖完整软件开发生命周期（SDLC），从构思到代码生成一体化。
*   基于 Shell 脚本构建轻量级且易于集成的执行环境。

3. **适用场景**
*   需要快速原型验证或进行大规模代码重构的开发团队。
*   希望引入 AI 代理自动化日常编码和测试任务的企业级项目。
*   利用 AI 辅助进行技术调研、架构设计头脑风暴的场景。
*   追求标准化、模块化智能体协作流程的软件工程实践者。

4. **技术亮点**
*   创新性地将“代理技能”概念化，形成可复用、可组合的开发模块。
*   采用子代理驱动开发（Subagent-Driven Development）范式，显著提升复杂逻辑处理的准确性。
*   以 Shell 为核心载体，保持了极低的集成门槛和高度的灵活性。
- 链接: https://github.com/obra/superpowers
- ⭐ 246522 | 🍴 21864 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一个能够伴随用户共同成长的智能代理工具。它旨在通过持续的学习和适应，为用户提供个性化的辅助支持。该项目致力于构建一个随用户需求演进而不断优化的 AI 交互体验。

### 2. 核心功能
*   **自适应学习**：代理能够根据用户的交互历史和使用习惯，动态调整其行为模式以实现个性化服务。
*   **多模型兼容**：支持集成 Anthropic 的 Claude、OpenAI 的 ChatGPT 等多种主流大语言模型。
*   **代码辅助能力**：具备处理编程任务的能力，可作为 Codex 或 Claude Code 等工具的补充或替代方案。
*   **长期记忆机制**：通过与用户建立长期的互动关系，积累上下文信息以提供更连贯的回答。
*   **开源社区驱动**：由 Nous Research 等机构参与，拥有活跃的开发者社区支持。

### 3. 适用场景
*   **个性化编程助手**：适合需要长期协作、熟悉特定代码库风格的开发者进行代码生成与审查。
*   **日常智能问答**：适用于希望获得基于个人偏好和历史对话背景的智能回答普通用户。
*   **LLM 实验与研究**：适合研究人员测试不同大语言模型在代理框架下的表现及优化策略。
*   **自动化工作流**：可用于构建简单的自动化脚本或任务执行代理，提升工作效率。

### 4. 技术亮点
*   **灵活的后端架构**：设计为可插拔式结构，便于接入不同的 LLM API 提供商。
*   **高社区关注度**：拥有近 21 万星标，证明了其在 AI Agent 领域的广泛影响力和用户基础。
*   **前沿概念整合**：结合了“生长型代理”理念，强调 AI 助手与用户之间的协同进化关系。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 209408 | 🍴 38228 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持 400 多种集成方式。它结合了可视化构建与自定义代码功能，用户可选择自托管或云端部署，灵活满足各类自动化需求。

2. **核心功能**
*   提供直观的可视化工作流构建器，降低自动化开发门槛。
*   内置原生 AI 能力，支持智能处理复杂业务逻辑。
*   拥有超过 400 种预置集成，实现跨应用数据无缝流转。
*   支持 TypeScript 自定义代码编写，满足高度定制化的开发需求。
*   采用公平代码（Fair-code）协议，兼顾开放性与商业可持续性。

3. **适用场景**
*   企业级内部系统之间的数据同步与业务流程自动化。
*   利用 AI 辅助生成或优化工作流，提升开发效率。
*   需要数据隐私保护，选择自托管方案进行私有化部署的场景。
*   快速搭建低代码/无代码集成平台，连接分散的 SaaS 工具。

4. **技术亮点**
*   基于 TypeScript 开发，类型安全且生态友好。
*   深度整合 MCP（Model Context Protocol）支持，增强与大模型的交互能力。
*   提供 CLI 工具及完整的 API 接口，便于 DevOps 集成与管理。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195247 | 🍴 59073 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能无障碍地使用和构建人工智能，其愿景是提供便捷的工具以解放用户的精力，使其能专注于真正重要的事务。作为开源的自主智能体框架，它旨在降低 AI 应用开发的门槛。

2. **核心功能**
- 支持基于 GPT、Claude 及 Llama 等大语言模型构建自主运行的 AI 智能体。
- 提供无需深厚编程基础即可创建和部署 AI 应用的工具集。
- 具备连接外部 API 和互联网以执行复杂多步任务的能力。
- 开放源码架构，允许开发者自由定制和扩展智能体行为。

3. **适用场景**
- 自动化执行需要多步骤推理的复杂研究或数据收集任务。
- 搭建个人助理或客服机器人，以实现全天候自主服务。
- 作为 AI 代理研究的实验平台，探索大模型的自主决策能力。
- 快速原型开发，验证特定领域 AI 应用的可行性。

4. **技术亮点**
- 兼容多种主流大语言模型后端（如 OpenAI、Anthropic、Hugging Face），提供极高的灵活性。
- 强调“无代码/低代码”体验，使非专业开发者也能轻松上手构建智能体。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185369 | 🍴 46119 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164741 | 🍴 21313 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163990 | 🍴 30376 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156800 | 🍴 46161 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151164 | 🍴 9434 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147730 | 🍴 23259 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

