# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### claude-arbitrage-bot
- 1. **中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，具备内置的Python自动化功能。该项目结合智能合约与脚本，旨在实现去中心化金融（DeFi）中的自动交易策略。

2. **核心功能**
*   支持在以太坊及其兼容链路上执行跨交易所或跨池套利操作。
*   集成Python自动化脚本，简化交易流程与逻辑控制。
*   利用智能合约处理链上资产交换与资金路由。
*   可能整合AI辅助工具（如Claude、Codex等）优化策略生成或代码编写。

3. **适用场景**
*   DeFi玩家希望自动化执行低风险套利机会以获取收益。
*   开发者学习如何构建基于Python和Solidity的链上自动化交易系统。
*   研究人员测试不同以太坊兼容网络间的流动性价差策略。

4. **技术亮点**
*   混合架构：结合链下Python逻辑控制与链上Solidity合约执行。
*   多网络兼容性：适用于以太坊及各类EVM兼容区块链。
*   AI集成倾向：标签暗示其可能探索利用大语言模型辅助交易策略开发。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### ai-api-relay-guide
- 1. **中文简介**
该项目是一个基于 GitHub Pages 部署的 AI API 中转站推荐与评测指南。它主要对比了不同代理服务的成本效益，例如展示 GPT 和 Claude 等模型通过特定中转服务可大幅降低调用费用。

2. **核心功能**
*   提供主流 AI 大模型（如 GPT、Claude）API 中转站的详细推荐列表。
*   集成 PokeAPI 风格的评测机制，直观展示各中转服务的价格优势（如 0.03x、0.2x 折扣）。
*   利用 GitHub Pages 静态托管特性，确保推荐信息的快速加载与高可用性。
*   采用 CSS 进行前端样式设计，优化用户浏览体验与信息呈现结构。

3. **适用场景**
*   个人开发者或小型团队希望降低调用 OpenAI 或 Anthropic 等昂贵 API 成本的场景。
*   需要快速筛选和比较不同 AI 中转服务商性价比的技术人员。
*   寻找稳定且低延迟国内镜像节点以访问海外 AI 服务的用户。

4. **技术亮点**
*   项目虽标注语言为 CSS，但实质是利用 GitHub Pages 构建轻量级、零服务器维护成本的静态信息聚合页。
*   通过直观的折扣倍数（如 0.03×）量化中转价值，降低了用户决策门槛。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 76 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### yuwen-publish-precheck
- 1. **中文简介**
这是一款专为抖音、小红书及视频号内容创作者设计的AI预检工具，旨在发布前自动审查文案风险。它不仅能精准指出违规点并提供基于官方规则的修改建议，还通过本地规则库持续优化判定准确度，帮助用户规避审核风险。

2. **核心功能**
*   **多平台合规审查**：支持对抖音、小红书和微信视频号的文案进行针对性的违规检测。
*   **精准定位与溯源**：明确标识踩线语句，并引用具体的官方规则条文作为判定依据。
*   **即时修改建议**：提供可直接使用的合规化修改方案，降低用户自行调整的成本。
*   **本地知识库迭代**：基于38篇真实样本校准标准，用户踩过的坑会沉淀为本地规则，使模型越用越准。

3. **适用场景**
*   **自媒体运营**：博主在发布短视频脚本或图文笔记前，快速排查潜在的平台违规风险。
*   **电商营销**：商家检查商品详情页或广告文案，避免因违禁词导致链接下架或账号受限。
*   **内容团队审核**：运营团队利用该工具作为第一道防线，提高人工复审的效率和质量。

4. **技术亮点**
*   **Agent Skills架构**：基于Cursor等编辑器的智能体技能设计，能够深度集成到开发者的工作流中。
*   **可验证的规则引擎**：不仅给出结果，还通过72条官方原文引文实现判定过程的可追溯和可查证。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 61 | 🍴 3 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### SuperMap
- **1. 中文简介**
SuperMap 是为具身智能体设计的“活体”空间记忆系统，能够感知物理世界并记录其动态演变过程。它不仅支持对环境进行深度推理，还能辅助智能体做出精准的决策与行动。

**2. 核心功能**
*   **实时环境感知**：捕捉并理解周围物理世界的即时状态与变化。
*   **动态记忆存储**：记录空间信息的演化历史，形成随时间更新的长期记忆。
*   **空间推理支持**：基于记忆数据进行分析，推导物体关系及场景逻辑。
*   **行动决策辅助**：将认知结果转化为具体的操作指令，指导智能体执行任务。

**3. 适用场景**
*   **自主机器人导航**：帮助机器人在复杂或动态变化的环境中规划路径。
*   **智能家居控制**：使家庭助手能理解用户习惯及物品位置的变化。
*   **增强现实（AR）应用**：为虚拟内容提供与现实世界同步的空间锚点与上下文。
*   **工业巡检自动化**：辅助移动机器人识别设备异常并记录环境变迁。

**4. 技术亮点**
*   **具身智能专用架构**：专为连接数字认知与物理行动而优化，强调“记忆”对“行为”的直接驱动作用。
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 35 | 🍴 0 | 语言: 未知

### codedrobe-codex-skill
- 1. **中文简介**
这是一个开源项目，旨在为 OpenAI Codex 应用提供主题定制技能、AI 辅助的主题生成器以及跨平台运行时环境。它允许用户自定义 Codex 桌面客户端的外观，并支持在 macOS 和 Windows 系统上运行。

2. **核心功能**
*   提供 OpenAI Codex 应用的开源主题定制技能（Skill）。
*   集成 AI 驱动的主题生成器，帮助用户快速创建自定义外观。
*   构建跨平台运行时环境，支持在 macOS 和 Windows 上管理自定义主题。
*   基于 Chromium DevTools Protocol 实现深度界面定制能力。

3. **适用场景**
*   希望个性化修改 OpenAI Codex 桌面应用视觉风格的开发者。
*   需要批量或自动化生成 Codex 主题的管理员或高级用户。
*   对现有默认主题不满意，追求更美观或符合品牌调性的 Codex 使用者。

4. **技术亮点**
*   利用 Node.js 和 CSS 技术栈实现跨平台兼容性。
*   结合 AI 编码能力与 Chromium 开发者工具协议进行动态主题渲染。
- 链接: https://github.com/anhao/codedrobe-codex-skill
- ⭐ 33 | 🍴 4 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### AI-Deepfake-Tool-2026
- 描述: Experience the ultimate Ai Deepfake Tool tool for PC. Built with advanced memory manipulation and a sleek interface, this undetected hack ensures you stay ahead in every match. Safe, reliable, and ...
- 链接: https://github.com/segevabelton/AI-Deepfake-Tool-2026
- ⭐ 27 | 🍴 0 | 语言: Python

### AI-Image-Upscaler-Free-2026
- 描述: Ai image upscaler free 2026 is the top open‑source cheat tool for 2026. includes triggerbot, external overlay, bypass and many other exploits. start dominating today.
- 链接: https://github.com/dhaniadhiwumpo-wq/AI-Image-Upscaler-Free-2026
- ⭐ 27 | 🍴 0 | 语言: Python

### AI-Voice-Cloner-Free-2026
- 描述: Unlock the full potential with Ai Voice Cloner. This cheat provides ESP, aimbot, and more, all while remaining completely invisible to anti-cheat systems. Download now and dominate the competition.
- 链接: https://github.com/anaqvi487/AI-Voice-Cloner-Free-2026
- ⭐ 27 | 🍴 0 | 语言: Python

### AI-Image-Generator-Pro-2026
- 描述: Experience the ultimate AI Image Generator Pro 2026 for your PC. This free tool provides a safe, undetected way to enhance your gameplay with advanced features. Download now and dominate the.
- 链接: https://github.com/aksasmostafa219-afk/AI-Image-Generator-Pro-2026
- ⭐ 27 | 🍴 0 | 语言: Python

### AI-Video-Generator-Free-2026
- 描述: Unlock the full potential of AI Video Generator Free 2026 with this powerful 2026 hack. Our cheat is updated regularly and works on all platforms. Enjoy ESP, aimbot, and more with AI Video Generator.
- 链接: https://github.com/Jacktech255/AI-Video-Generator-Free-2026
- ⭐ 27 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面的中英文自然语言处理资源仓库，集成了敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）及情感分析等基础工具。它同时提供了丰富的中文领域词库（如医学、法律、汽车）、预训练模型（如 BERT、ALBERT）以及各类 NLP 数据集和竞赛代码汇总，旨在为开发者提供一站式的中文 NLP 解决方案。

**2. 核心功能**
*   **基础 NLP 工具链**：涵盖分词、词性标注、命名实体识别、情感分析及文本相似度计算等核心算法实现。
*   **海量中文资源库**：提供包括同义词、反义词、停用词、暴恐词、行业专用词库（金融、医疗、法律等）在内的丰富词典资源。
*   **预训练模型与框架集成**：收录并整理了 BERT、RoBERTa、ALBERT 等主流预训练模型在中文场景下的应用代码及微调指南。
*   **数据增强与生成**：包含文本生成、自动摘要、数据增强工具（EDA）以及用于训练聊天机器人或问答系统的语料库。

**3. 适用场景**
*   **中文 NLP 初学者入门**：适合需要快速了解中文处理流程、获取标准词库和数据集的学习者。
*   **企业级内容风控系统开发**：利用其敏感词库和暴恐词表，快速搭建文本审核和内容过滤系统。
*   **垂直领域知识图谱构建**：借助其提供的医学、法律、金融等专业词库及实体抽取工具，构建特定行业的知识库。
*   **NLP 竞赛与学术研究参考**：作为查找最新 NLP 论文代码、竞赛 Top 方案及前沿模型实现的参考资料库。

**4. 技术亮点**
*   **资源聚合度极高**：不仅包含代码，还整合了大量高质量的中英文数据集、预训练模型权重及学术报告，是中文 NLP 领域的“百科全书”。
*   **覆盖面广且实用**：从基础的繁简转换、数字识别到复杂的跨语言百科图谱、语音情感分析，几乎涵盖了 NLP 的所有细分方向。
*   **紧跟技术前沿**：持续更新包含 Transformer、BERT 系列及最新开源模型（如 XLORE、GPT-2 中文版）的相关资源和最佳实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81827 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. **中文简介**
该项目是一个包含500个AI实战代码示例的大型资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的Python代码实现，帮助开发者快速掌握各类人工智能算法的应用。这是一个适合从入门到进阶学习者的综合性技术参考指南。

### 2. **核心功能**
*   **全栈AI项目覆盖**：集成机器学习、深度学习、计算机视觉和NLP四大领域的500多个独立项目案例。
*   **完整代码实现**：所有项目均附带可直接运行的Python代码，便于用户复现和调试。
*   **分类索引清晰**：按技术领域和项目类型进行标签化管理，方便快速定位所需技术模块。
*   **学习路径引导**：作为Awesome列表的一部分，为不同水平的开发者提供结构化的学习资源。

### 3. **适用场景**
*   **AI初学者实践**：适合刚接触人工智能的学生或转行者，通过阅读代码理解基础算法原理。
*   **项目灵感参考**：开发者在构思新项目时，可从中获取设计思路和技术方案参考。
*   **面试准备复习**：求职者可用于复习主流AI面试题涉及的经典算法实现和工程实践。
*   **教学辅助材料**：教师或培训机构可作为课堂演示代码或课后练习素材使用。

### 4. **技术亮点**
*   **高人气与权威性**：拥有超过35,000颗星标，是GitHub上最热门的AI项目合集之一，经过社区广泛验证。
*   **技术栈全面**：涵盖Python主流AI库（如TensorFlow, PyTorch, Scikit-learn等），紧跟行业技术趋势。
*   **开箱即用**：项目代码通常包含数据预处理、模型训练及评估流程，极大降低了复现门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35460 | 🍴 7352 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的强大工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构和数据流向。

2. **核心功能**
*   支持广泛的模型格式，包括 CoreML、Keras、ONNX、PyTorch、TensorFlow 等。
*   提供直观的图形化界面，清晰展示网络层结构、参数形状及张量维度。
*   允许用户交互式探索模型细节，便于调试和分析复杂的神经网络架构。
*   兼容多种数据类型和算子，能够准确渲染从传统 ML 到最新大模型的复杂结构。

3. **适用场景**
*   **模型调试**：在开发阶段快速检查模型层连接是否正确，排查结构错误。
*   **论文复现与分析**：可视化他人发布的模型架构，辅助理解论文中的网络设计思路。
*   **模型转换验证**：在将模型从 PyTorch 转换为 ONNX 或 TensorRT 等格式后，验证转换前后的结构一致性。
*   **教学演示**：用于向初学者或团队直观展示深度学习模型的工作原理和数据流动过程。

4. **技术亮点**
*   **零依赖运行**：无需安装庞大的 Python 环境或特定框架即可直接查看模型，极大降低了使用门槛。
*   **跨平台支持**：提供桌面应用和 Web 版本，方便在不同操作系统和设备上随时随地进行模型检查。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33233 | 🍴 3155 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21155 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面介绍机器学习工程实践的资源合集，旨在填补学术界与工业界在大规模模型部署上的知识鸿沟。它涵盖了从底层硬件优化到上层模型训练、推理及调试的全链路工程技术。

2. **核心功能**
*   提供大语言模型（LLM）的高效训练与微调指南。
*   详解分布式训练架构及GPU集群的资源调度策略。
*   包含针对Transformer模型的内存优化与推理加速技巧。
*   涵盖ML系统调试、监控及可扩展性设计的最佳实践。

3. **适用场景**
*   需要构建和部署超大规模语言模型的研究团队或企业。
*   致力于优化深度学习训练基础设施的MLOps工程师。
*   希望深入理解PyTorch底层原理及GPU硬件交互的高级开发者。

4. **技术亮点**
*   聚焦于“规模效应”，深入解析在数千张GPU上运行模型的工程挑战。
*   结合Slurm、网络存储等具体工具链，提供可落地的运维方案。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18408 | 🍴 1173 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17319 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13146 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11575 | 🍴 908 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. **中文简介**
该项目是一个包含500个AI实战代码示例的大型资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的Python代码实现，帮助开发者快速掌握各类人工智能算法的应用。这是一个适合从入门到进阶学习者的综合性技术参考指南。

### 2. **核心功能**
*   **全栈AI项目覆盖**：集成机器学习、深度学习、计算机视觉和NLP四大领域的500多个独立项目案例。
*   **完整代码实现**：所有项目均附带可直接运行的Python代码，便于用户复现和调试。
*   **分类索引清晰**：按技术领域和项目类型进行标签化管理，方便快速定位所需技术模块。
*   **学习路径引导**：作为Awesome列表的一部分，为不同水平的开发者提供结构化的学习资源。

### 3. **适用场景**
*   **AI初学者实践**：适合刚接触人工智能的学生或转行者，通过阅读代码理解基础算法原理。
*   **项目灵感参考**：开发者在构思新项目时，可从中获取设计思路和技术方案参考。
*   **面试准备复习**：求职者可用于复习主流AI面试题涉及的经典算法实现和工程实践。
*   **教学辅助材料**：教师或培训机构可作为课堂演示代码或课后练习素材使用。

### 4. **技术亮点**
*   **高人气与权威性**：拥有超过35,000颗星标，是GitHub上最热门的AI项目合集之一，经过社区广泛验证。
*   **技术栈全面**：涵盖Python主流AI库（如TensorFlow, PyTorch, Scikit-learn等），紧跟行业技术趋势。
*   **开箱即用**：项目代码通常包含数据预处理、模型训练及评估流程，极大降低了复现门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35460 | 🍴 7352 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的强大工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构和数据流向。

2. **核心功能**
*   支持广泛的模型格式，包括 CoreML、Keras、ONNX、PyTorch、TensorFlow 等。
*   提供直观的图形化界面，清晰展示网络层结构、参数形状及张量维度。
*   允许用户交互式探索模型细节，便于调试和分析复杂的神经网络架构。
*   兼容多种数据类型和算子，能够准确渲染从传统 ML 到最新大模型的复杂结构。

3. **适用场景**
*   **模型调试**：在开发阶段快速检查模型层连接是否正确，排查结构错误。
*   **论文复现与分析**：可视化他人发布的模型架构，辅助理解论文中的网络设计思路。
*   **模型转换验证**：在将模型从 PyTorch 转换为 ONNX 或 TensorRT 等格式后，验证转换前后的结构一致性。
*   **教学演示**：用于向初学者或团队直观展示深度学习模型的工作原理和数据流动过程。

4. **技术亮点**
*   **零依赖运行**：无需安装庞大的 Python 环境或特定框架即可直接查看模型，极大降低了使用门槛。
*   **跨平台支持**：提供桌面应用和 Web 版本，方便在不同操作系统和设备上随时随地进行模型检查。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33233 | 🍴 3155 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究者提供了关键的速查手册集合。它旨在通过简明的参考资料，帮助研究人员快速回顾和掌握核心概念与工具用法。

2. **核心功能**
- 涵盖深度学习与机器学习领域的核心算法及数学原理速查。
- 集成常用Python库（如NumPy、SciPy、Matplotlib、Keras）的代码示例与语法参考。
- 提供针对AI研究者的实用技巧与最佳实践总结。
- 以结构化的笔记形式呈现，便于快速检索关键知识点。

3. **适用场景**
- 深度学习初学者在入门阶段快速查阅基础概念和公式。
- 研究人员在进行模型调试时，快速核对特定库函数或参数用法。
- 面试准备期间，复习机器学习核心算法和数学背景知识。
- 日常编码过程中，作为手边参考手册以加速开发流程。

4. **技术亮点**
- 高度聚焦于研究场景，精选了最频繁使用的技术和库进行归纳。
- 内容精炼，去除了冗长解释，直接呈现代码片段和关键定义，极大提升查阅效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目是一份全面的人工智能学习路线图，汇集了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户轻松入门并具备就业实战能力。内容涵盖Python、数学基础以及机器学习、深度学习、计算机视觉、自然语言处理等热门领域的主流框架与技术栈。

### 2. 核心功能
*   提供结构化的AI学习路径，从零基础引导至专业实战应用。
*   收录近200个精选实战案例和项目，强化动手能力。
*   配套免费教学资源，降低学习门槛，适合系统化自学。
*   覆盖主流开发库（如TensorFlow、PyTorch、Pandas等）及核心算法。

### 3. 适用场景
*   **初学者入门**：希望系统了解人工智能领域知识体系的新手。
*   **求职准备**：需要积累实战项目经验以提升就业竞争力的求职者。
*   **技能拓展**：希望掌握特定AI子领域（如NLP或CV）技术栈的数据科学从业者。

### 4. 技术亮点
*   整合了从基础数学到高级深度学习框架（如TensorFlow 2.x, PyTorch, Keras）的全栈技术资源。
*   强调“理论+实战”结合，通过大量现成案例快速验证学习效果。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13146 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他人工智能模型的构建与训练过程。它通过声明式配置和自动化的机器学习流水线，降低了开发门槛，使用户能够专注于数据而非复杂的代码实现。

### 2. 核心功能
*   **低代码/无代码建模**：支持通过 YAML 配置文件快速定义模型结构，无需编写大量底层代码即可训练深度学习模型。
*   **多模态支持**：原生支持处理表格数据、文本、图像、音频及结构化数据，适用于计算机视觉和自然语言处理等多种任务。
*   **集成主流架构**：深度集成 PyTorch 和 Hugging Face Transformers，方便调用和微调如 LLaMA、Mistral 等先进的大语言模型。
*   **自动化实验管理**：内置可视化界面和日志记录功能，自动跟踪超参数、指标和模型版本，简化模型对比与调优流程。

### 3. 适用场景
*   **快速原型开发**：数据科学家希望在不深入底层框架细节的情况下，迅速验证不同模型架构在特定数据集上的效果。
*   **企业级 AI 应用部署**：团队需要构建可重复、可维护且标准化的机器学习管道，用于生产环境中的模型训练和服务。
*   **大语言模型微调**：开发者希望对 LLaMA、Mistral 等开源 LLM 进行领域适应性的微调，同时保持配置的简洁性和可移植性。

### 4. 技术亮点
*   **声明式 API**：采用“配置即代码”的理念，通过简单的 YAML 文件即可控制复杂的深度学习实验，极大提升了工作流的透明度和可复现性。
*   **开箱即用的预处理**：自动处理常见的数据清洗、编码和归一化步骤，减少了数据预处理阶段的工程负担。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11738 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9135 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3100 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6986 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6259 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
该项目是一个全面的中英文自然语言处理（NLP）工具包与资源合集，涵盖了从基础文本清洗、敏感词检测到高级知识图谱构建的多种功能。它不仅提供了丰富的中文专用词库、语料库和数据集，还集成了众多前沿的NLP算法、预训练模型（如BERT）及开源工具，旨在为开发者提供一站式的中文NLP解决方案。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、停用词、反动词表以及中文分词和词性标注等基础功能。
*   **实体识别与信息抽取**：支持姓名、手机号、身份证、邮箱等特定实体的抽取，并包含基于BERT等模型的命名实体识别（NER）和关系抽取工具。
*   **丰富词库与知识资源**：内置中日文人名库、职业/品牌/汽车零件/医学/法律等专业领域词库，以及古诗词、成语、地名等文化类数据。
*   **情感分析与语义理解**：提供词汇情感值、中文聊天语料、句子相似度匹配算法，以及基于深度学习的情感分析和文本分类模型。
*   **多模态与前沿技术整合**：整合了语音识别（ASR）、OCR文字识别、知识图谱构建工具及多种预训练语言模型资源。

3. **适用场景**
*   **内容安全审核**：用于互联网平台自动识别和过滤敏感词、暴恐词及不当言论，保障内容合规。
*   **智能客服与聊天机器人开发**：利用其中的闲聊语料、对话数据集及NLU工具，快速构建具备语义理解和多轮对话能力的智能助手。
*   **企业级知识图谱构建**：借助其提供的命名实体抽取、关系抽取及知识图谱构建工具，从非结构化文本中提取知识，构建行业专属知识库。
*   **数据分析与舆情监控**：通过情感分析工具和关键词抽取功能，对社交媒体、新闻或评论数据进行情感倾向判断和热点话题挖掘。

4. **技术亮点**
*   **资源极其丰富**：不仅包含代码库，还汇总了大量高质量的中文NLP数据集、预训练模型（如ELECTRA、ALBERT、RoBERTa）及学术论文资源。
*   **覆盖全链路**：从数据预处理、特征工程、模型训练到应用部署（如OCR、ASR），覆盖了NLP任务的全生命周期。
*   **实用性强**：提供了许多开箱即用的工具，如中文数字转换、拼音标注、简历解析、文本摘要等，极大降低了开发门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81827 | 🍴 15248 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目于 ACL 2024 被收录，旨在简化模型训练流程并提供卓越的性能体验。它通过整合多种前沿技术，让开发者能够轻松地对各类先进模型进行指令微调及强化学习对齐。

2. **核心功能**
*   支持超过100种主流大语言模型和视觉语言模型的统一微调接口。
*   提供丰富的优化算法，包括 LoRA、QLoRA、P-Tuning 等参数高效微调方法。
*   内置 RLHF（基于人类反馈的强化学习）支持，涵盖 DPO、KTO 等对齐策略。
*   实现全参数微调、低精度量化训练以及多模态数据的高效处理。
*   兼容 Transformers 库，提供直观的命令行工具与 Web UI 交互界面。

3. **适用场景**
*   开发者需要在不同架构的 LLM 上快速验证微调效果，无需重写训练代码。
*   资源受限环境下，利用 QLoRA 等技术以较低显存成本对大规模模型进行适配。
*   希望将文本模型扩展至视觉领域，进行图文多模态指令微调的研究人员。
*   需要实施 DPO 等最新对齐算法以提升模型输出质量和安全性的高级用户。

4. **技术亮点**
*   **高度统一性**：屏蔽了底层模型差异，用同一套代码逻辑支持从 Llama 到 Qwen 等百种模型的训练。
*   **极致效率**：结合 FlashAttention 和 DeepSpeed 等技术，显著提升训练速度并降低显存占用。
*   **前沿对齐**：率先集成 RLHF 多种变体（如 ORPO、KTO），紧跟 NLP 领域最新研究进展。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73310 | 🍴 8951 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- **1. 中文简介**
该项目从 Anthropic、OpenAI、Google 及 xAI 等主流厂商的大型语言模型中提取了系统提示词（System Prompts），涵盖了 Claude、ChatGPT、Gemini 等多个知名模型版本。仓库内容会定期更新，旨在为研究者和技术人员提供最新的模型底层指令参考。

**2. 核心功能**
*   收集并整理来自多家头部 AI 公司的官方系统提示词数据。
*   覆盖 Claude、GPT、Gemini 等多系列模型的多个特定版本。
*   定期更新以反映最新发布的模型指令变化。
*   提供结构化的提示词数据，便于直接查阅和分析。

**3. 适用场景**
*   **提示词工程研究**：分析顶尖 AI 模型的系统指令设计模式与优化技巧。
*   **AI 安全与红队测试**：了解模型底层约束，用于评估系统提示词的安全性或潜在漏洞。
*   **教育与技术分享**：作为学习大语言模型工作原理和 Prompt Engineering 的参考资料。

**4. 技术亮点**
*   **多源聚合**：整合了 Anthropic、OpenAI、Google、xAI 等多家竞争对手的核心数据。
*   **时效性强**：保持定期更新，紧跟各大模型版本的迭代步伐。
*   **高关注度**：拥有极高的星标数（58,000+），反映了社区对模型内部机制的高度关注。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58152 | 🍴 9613 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由Microsoft For Beginners系列推出，内容覆盖从基础概念到深度学习的高级主题。

2. **核心功能**
*   提供结构化的12周学习计划，每两周完成一个核心模块。
*   基于Jupyter Notebook编写，支持交互式代码学习与即时反馈。
*   涵盖机器学习、计算机视觉、自然语言处理等广泛AI领域。
*   包含生成对抗网络（GAN）和循环神经网络（RNN）等高级主题实践。
*   免费开源，适合零基础的初学者系统性地构建AI知识体系。

3. **适用场景**
*   自学者希望系统性地从零开始学习人工智能基础知识。
*   教育机构或企业用于培训员工的基础AI技能提升课程。
*   学生作为计算机科学相关课程的补充教材或实践项目。
*   开发者想要快速了解ML/DL基本概念并动手编写简单模型。

4. **技术亮点**
*   由微软官方维护，确保内容的权威性与教育资源的开放性。
*   采用多模态教学方式，结合文本讲解与可执行的代码笔记。
*   标签明确，精准覆盖CNN、NLP、GAN等主流AI技术栈。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52339 | 🍴 10586 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. 中文简介
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数基础以及深度学习框架（如 PyTorch 和 TensorFlow 2）的综合学习资源库。该项目集成了自然语言处理（NLTK）与推荐系统等核心技术，旨在为学习者提供从理论到实践的完整指南。

### 2. 核心功能
*   **算法实战实现**：包含 Adaboost、K-Means、SVM、逻辑回归等经典机器学习的代码实现。
*   **深度学习支持**：集成 PyTorch 和 TensorFlow 2 框架，涵盖 DNN、RNN、LSTM 等神经网络结构。
*   **数据处理与分析**：提供 PCA、SVD 等数据降维技术及线性代数相关数学基础。
*   **NLP 与自然语言处理**：利用 NLTK 库进行文本分析和自然语言处理任务。
*   **推荐系统构建**：基于 Apriori 和 FP-Growth 等算法实现商品或内容推荐。

### 3. 适用场景
*   **机器学习入门与进阶**：适合希望系统掌握从传统 ML 到 DL 算法原理及代码实现的初学者。
*   **高校课程辅助学习**：可作为数据结构、算法、线性代数及人工智能相关课程的实践参考。
*   **NLP 项目开发原型**：适用于需要快速搭建文本分类、情感分析等 NLP 模型原型的开发者。
*   **推荐系统算法研究**：适合研究协同过滤、关联规则挖掘等推荐算法的技术人员。

### 4. 技术亮点
*   **全栈覆盖**：同时涵盖传统机器学习、深度学习、NLP 和推荐系统，知识体系完整。
*   **多框架兼容**：结合 Scikit-learn 与主流深度学习框架（PyTorch/TF2），适应不同技术偏好。
*   **高人气验证**：拥有超过 42k 的星标数，证明其在社区中具有较高的认可度和实用性。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42380 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38417 | 🍴 6436 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35460 | 🍴 7352 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33741 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28569 | 🍴 3485 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25908 | 🍴 2924 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35460 | 🍴 7352 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款利用人工智能自动化基于浏览器的复杂工作流的工具。它通过结合大语言模型（LLM）和计算机视觉技术，能够像人类一样理解和操作网页界面。该项目旨在提供一种高效、智能的方式来替代传统的RPA或脚本自动化方案。

**2. 核心功能**
*   基于AI的视觉理解：利用计算机视觉识别网页元素，无需依赖固定的CSS选择器或XPath。
*   自然语言驱动的工作流：用户可通过自然语言指令定义任务，系统自动规划并执行相应的浏览器操作步骤。
*   强大的浏览器控制能力：底层支持 Playwright 等现代浏览器自动化工具，确保操作的稳定性和速度。
*   端到端自动化：能够处理包含登录、数据填写、导航和验证在内的完整业务流程。

**3. 适用场景**
*   企业级RPA替代：用于自动化跨多个网站的重复性行政或数据处理任务，降低人工成本。
*   动态网页抓取：在目标网站结构频繁变化时，利用AI的泛化能力稳定地提取所需信息。
*   在线流程自动化：如自动完成在线表单提交、预约预订、电商比价等需要交互的操作。

**4. 技术亮点**
*   **无头/有头浏览器兼容**：灵活支持各种浏览器环境，适应不同的自动化需求。
*   **LLM与视觉融合**：突破了传统自动化工具对DOM结构的强依赖，具备更强的鲁棒性和适应性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22303 | 🍴 2090 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的首选平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量控制及团队协作，并具备完善的开发API。

2. **核心功能**
*   支持图像、视频及3D数据的多种标注格式（如边界框、语义分割）。
*   内置AI辅助标注与质量保证机制，显著提升数据标注效率。
*   提供团队协作、数据分析及开发者API，适应不同规模需求。
*   涵盖开源软件、云服务和企业解决方案，并配套专业标注服务。

3. **适用场景**
*   需要大规模图像或视频数据集用于训练目标检测模型的团队。
*   执行语义分割或图像分类任务以优化深度学习算法的研究人员。
*   寻求高效协作与自动化标注流程的企业级计算机视觉项目组。

4. **技术亮点**
*   兼容PyTorch和TensorFlow等主流深度学习框架的数据需求。
*   提供从社区版到企业级的完整生态系统，支持高度定制化。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16301 | 🍴 3761 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建，支持自动微分与 GPU 加速。它旨在为深度学习研究者和开发者提供一套可微分的图像处理工具，从而简化计算机视觉算法的实现与优化过程。该项目融合了传统的计算机视觉理论与现代深度学习方法，适用于需要端到端训练的场景。

### 2. 核心功能
- **可微分图像预处理**：提供大量可微分的图像变换操作（如旋转、缩放、裁剪），可直接集成到神经网络中。
- **几何计算机视觉模块**：内置相机校准、立体视觉、单目深度估计等经典几何算法的可微分实现。
- **PyTorch 原生集成**：完全兼容 PyTorch 生态系统，支持在 GPU 上高效运行并自动计算梯度。
- **空间 AI 推理工具**：包含用于 3D 重建、姿态估计和机器人导航的高级视觉处理功能。
- **模块化 API 设计**：代码结构清晰，便于扩展和自定义新的计算机视觉算子。

### 3. 适用场景
- **自动驾驶与机器人导航**：用于实时处理传感器数据，进行环境感知、路径规划和避障。
- **增强现实（AR）与虚拟现实（VR）**：实现精确的物体追踪、空间映射和虚实融合渲染。
- **医学影像分析**：利用可微分预处理提升图像分割、配准和病灶检测模型的精度。
- **工业视觉检测**：在自动化生产线中进行高精度的缺陷检测和尺寸测量。

### 4. 技术亮点
- **端到端可微分流水线**：打破传统 CV 与深度学习之间的壁垒，允许整个视觉处理链路进行联合优化。
- **高性能 GPU 加速**：所有操作均针对 GPU 优化，显著提升了大规模图像处理和数据增强的速度。
- **开源社区活跃**：作为 Hacktoberfest 友好项目，拥有活跃的开发者社区和丰富的贡献者资源。
- 链接: https://github.com/kornia/kornia
- ⭐ 11277 | 🍴 1201 | 语言: Python
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
- ⭐ 3283 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2627 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款跨平台、跨操作系统的个人 AI 助手，让你以“龙虾”的独特方式完全掌控自己的数据。它支持在任何设备和平台上部署，旨在为用户提供私密且自主的人工智能服务体验。

2. **核心功能**
*   支持任意操作系统和硬件平台的广泛兼容性。
*   强调数据所有权，确保用户隐私与数据安全。
*   提供个性化的 AI 助手交互体验。
*   基于 TypeScript 构建，具备现代化的开发架构。

3. **适用场景**
*   希望完全掌控个人数据隐私的用户。
*   需要在不同操作系统间无缝切换的个人开发者。
*   寻求定制化、非云端托管 AI 助手的技术爱好者。

4. **技术亮点**
*   采用 TypeScript 编写，保证代码类型安全与可维护性。
*   具备高度的平台无关性，实现真正的跨设备运行。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383063 | 🍴 80443 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一套经过验证的智能体技能框架与软件开发方法论。它通过构建可复用的“技能”和自动化子代理，显著提升了软件开发的效率与质量。该项目旨在解决传统开发流程中的痛点，提供一种更智能、更自动化的工作流解决方案。

2. **核心功能**
*   **智能体驱动开发**：利用自主运行的子代理（Subagents）执行具体的编码和调试任务。
*   **可复用技能库**：提供标准化的“技能”模块，便于在项目中快速集成和调用。
*   **自动化头脑风暴与设计**：辅助进行技术方案设计和问题 brainstorming，优化需求分析阶段。
*   **全生命周期集成**：覆盖从需求定义、编码到测试的完整 SDLC（软件开发生命周期）。
*   **Agentic 技能框架**：提供底层架构支持，使 AI 智能体能够像人类专家一样协同工作。

3. **适用场景**
*   **复杂软件架构设计**：需要多角度论证和技术选型的系统性项目开发。
*   **自动化编码辅助**：希望利用 AI 子代理自动完成代码生成、重构或 Bug 修复的团队。
*   **快速原型开发**：需要快速迭代并验证想法的初创项目或内部工具开发。
*   **提升开发效率**：试图通过引入 AI 智能体工作流来优化现有 DevOps 流程的工程团队。

4. **技术亮点**
*   **方法论创新**：将 AI 能力从单纯的代码补全升级为完整的“技能驱动”开发范式。
*   **高人气验证**：拥有超过 25 万星标，证明了其在社区中的广泛影响力和实用性。
*   **Shell 脚本实现**：基于 Shell 构建，确保了与 Linux/Unix 环境的原生兼容性和轻量级部署。
- 链接: https://github.com/obra/superpowers
- ⭐ 255493 | 🍴 22842 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够伴随用户共同成长的智能代理工具，旨在通过持续学习和互动来优化用户体验。它支持多模型接入，具备强大的上下文理解与任务执行能力，能够动态适应不同用户的需求。该项目致力于打造一个灵活且进化的 AI 助手生态。

2. **核心功能**
*   支持接入 Anthropic Claude、OpenAI ChatGPT 等多种主流大语言模型。
*   具备自我进化机制，能随着使用时间的推移不断优化工作流和响应质量。
*   提供统一的 API 接口，简化了不同 AI 模型间的集成与管理复杂度。
*   内置丰富的插件系统，可扩展代码生成、数据分析及自动化操作等功能。
*   强调隐私保护与安全控制，确保用户数据在本地或受控环境中处理。

3. **适用场景**
*   **开发者辅助编码**：作为代码助手，实时生成、调试和优化复杂代码片段。
*   **个性化研究助理**：协助研究人员快速整理文献、总结摘要并提取关键信息。
*   **自动化工作流执行**：处理日常重复性任务，如邮件分类、日程安排及数据录入。
*   **多模型对比测试**：用于评估不同 LLM 在特定任务下的表现差异以选择最优解。

4. **技术亮点**
*   采用模块化架构设计，便于开发者自定义代理行为与交互逻辑。
*   实现了高效的上下文窗口管理，能够处理长文本及多轮对话历史。
*   开源社区活跃，拥有活跃的贡献者网络及丰富的第三方扩展资源。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215553 | 🍴 40201 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码。它提供超过 400 种集成方式，用户可选择自托管或云部署，灵活满足各类自动化需求。

### 2. 核心功能
*   **混合开发模式**：无缝结合可视化拖拽搭建与自定义代码编写，兼顾易用性与灵活性。
*   **广泛集成生态**：内置 400 多种应用集成，覆盖主流 SaaS 工具和 API 接口。
*   **原生 AI 集成**：深度整合 AI 能力，支持在自动化流程中直接使用人工智能模型。
*   **部署灵活**：支持自托管以确保数据隐私，也提供便捷的云端服务选项。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，便于连接和管理大型语言模型上下文。

### 3. 适用场景
*   **企业数据同步**：自动在不同系统（如 CRM、数据库、邮件服务）之间同步和转换数据。
*   **AI 驱动的工作流**：利用 AI 模型处理文本、生成内容或分析数据，并触发后续业务动作。
*   **DevOps 自动化**：自动化代码部署、测试报告通知及服务器监控告警等运维任务。
*   **低代码快速原型**：非开发人员通过可视化界面快速构建简单的业务流程自动化解决方案。

### 4. 技术亮点
*   **公平代码许可证**：采用 Fair-code 模式，既保证社区贡献又允许商业应用，平衡开源与盈利。
*   **TypeScript 构建**：基于 TypeScript 开发，提供类型安全和现代化的开发体验，代码质量高。
*   **MCP 客户端/服务端支持**：率先支持 MCP 协议，简化了 AI 应用与工作流引擎之间的上下文交互。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196604 | 🍴 59350 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于实现人人可及的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，让用户能将精力集中于真正重要的事情上。

### 2. 核心功能
- 支持自主代理（Autonomous Agents）执行复杂的多步骤任务。
- 兼容多种大型语言模型后端，包括 OpenAI、Claude 和 LLaMA API。
- 提供模块化架构，便于开发者快速集成和扩展 AI 能力。
- 具备自我反思与纠错机制，以提升任务执行的准确性和稳定性。

### 3. 适用场景
- 自动化日常办公流程，如数据整理、邮件回复和信息摘要生成。
- 构建复杂的 AI 驱动应用原型，验证多智能体协作的逻辑可行性。
- 研究大型语言模型在自主规划、记忆保持及工具使用方面的边界与能力。

### 4. 技术亮点
- 广泛支持主流 LLM 提供商（OpenAI, Anthropic, Meta 等），确保灵活性与兼容性。
- 采用 Agentic AI 架构，强调智能体的自主决策与工具调用能力。
- 拥有极高的社区活跃度与星标数，证明其在 AI 开源生态中的领先地位。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185571 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165831 | 🍴 21450 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164268 | 🍴 30525 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157061 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151924 | 🍴 9680 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151623 | 🍴 8665 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

