# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### skills
- 描述: Open-source OpenAI Codex theming Skill, AI theme generator, and cross-platform runtime for custom Codex desktop themes.
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 97 | 🍴 12 | 语言: 未知
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### yuwen-publish-precheck
- 1. **中文简介**
这是一款针对抖音、小红书及微信视频号的发布前内容合规审查工具，利用 AI 识别违规风险并提供基于官方规则的修改建议。项目通过 38 篇真实样本和 72 条官方原文引文进行校准，帮助用户沉淀本地规则库以提升判定准确度。

2. **核心功能**
*   **多平台合规检测**：支持抖音、小红书和微信视频号的内容预审。
*   **精准违规定位**：明确指出具体哪句话踩线，并引用对应的官方规则依据。
*   **即时修改方案**：提供可直接使用的合规改写建议，降低修改成本。
*   **本地知识库积累**：用户踩过的坑可沉淀为本地规则，使审核越来越精准。
*   **Cursor Agent 集成**：作为 Cursor 的 Agent Skill 无缝嵌入代码或文本编辑工作流。

3. **适用场景**
*   自媒体运营者在发布短视频文案或图文笔记前的最终合规检查。
*   需要频繁在多平台分发内容，且希望统一审核标准的内容创作者。
*   希望利用 AI 辅助快速优化敏感词汇，避免账号受限的个人或团队。

4. **技术亮点**
*   **高可信度引用**：内置 72 条官方规则原文引文，确保判定依据可查证。
*   **真实数据校准**：基于 38 篇真实样本训练判定尺度，贴合实际平台审核逻辑。
*   **AI Agent 友好**：专为 Cursor 等 AI 编辑器设计，可作为插件技能直接调用。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 89 | 🍴 5 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### claude-arbitrage-bot
- 1. **中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，集成了内置的Python自动化功能。它利用智能合约实现链上交易逻辑，旨在通过捕捉不同市场间的价差获利。

2. **核心功能**
*   支持在以太坊及各类兼容网络上执行自动套利交易。
*   内置Python脚本以实现复杂的自动化流程和控制逻辑。
*   基于Solidity编写智能合约，确保链上交互的安全性与效率。
*   集成AI辅助工具（如Claude、Codex等）以优化策略或代码生成。

3. **适用场景**
*   DeFi（去中心化金融）协议间的跨平台套利机会捕捉。
*   高频交易策略的自动化执行与回测。
*   开发者利用AI辅助工具快速构建和部署智能合约。
*   对以太坊兼容链进行自动化交易机器人的研究与测试。

4. **技术亮点**
*   结合了Solidity智能合约与Python后端自动化，实现了链上与链下逻辑的高效协同。
*   融入了主流AI大模型工具链，提升了开发效率和策略优化的智能化水平。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### ai-api-relay-guide
- ### 1. 中文简介
该项目是一个基于 GitHub Pages 构建的 AI API 中转站评测与推荐指南，通过模拟 PokeAPI 的调用频率来直观展示不同服务商的性能。它重点对比了主流大模型接口的成本与响应速度，例如展示 GPT 和 Claude 的相对优惠折扣。旨在帮助用户快速选择性价比高且稳定的 AI 接口服务。

### 2. 核心功能
- **多维度性能评测**：利用 PokeAPI 作为基准测试负载，量化评估各 AI API 中转站的响应时间和稳定性。
- **成本效益对比**：直观展示如 GPT 0.03倍、Claude 0.2倍等极具竞争力的价格优势，降低用户接入成本。
- **一站式推荐列表**：汇总并筛选优质的 AI API 中继服务，为用户提供透明的选择依据。
- **静态页面托管**：基于 GitHub Pages 部署，确保评测数据的公开透明且易于访问。
- **标签化分类检索**：通过 `ai-api`、`api-relay` 等标签方便开发者快速定位相关技术资源。

### 3. 适用场景
- **个人开发者成本控制**：需要低成本接入 GPT 或 Claude 等大模型能力，以优化项目预算的个人开发者。
- **初创公司技术选型**：在早期阶段寻求稳定且价格低廉的 AI 接口服务，以快速验证产品可行性的创业团队。
- **API 中转站性能监控**：希望了解当前市场上各中转站真实吞吐量和延迟情况的技术分析师或运维人员。
- **学习资源参考**：想要了解如何搭建或评估 AI 代理（Relay）服务的初学者或研究者。

### 4. 技术亮点
- **创新评测模型**：创造性地使用 PokeAPI 这种高并发、轻量级的公共 API 作为压力测试工具，形象地反映中转站的承载能力。
- **可视化折扣展示**：直接将复杂的价格结构转化为直观的倍数（如 0.03x），极大降低了非技术背景用户的理解门槛。
- **零后端依赖**：采用纯静态网页技术（HTML/CSS/JS）配合 GitHub Pages，无需维护服务器即可实现全球访问和实时更新。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 76 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### SuperMap
- 1. **中文简介**：SuperMap 是一个为具身智能（Embodied AI）设计的动态空间记忆系统。它能够感知世界、记录环境演变，并支持复杂的推理与行动决策。

2. **核心功能**：
   - 实时感知周围环境的空间信息。
   - 长期记忆并追踪环境的动态演变过程。
   - 基于空间记忆支持高级推理逻辑。
   - 辅助具身智能体进行精准的动作规划。

3. **适用场景**：
   - 服务机器人在复杂室内环境中的导航与任务执行。
   - 自动驾驶车辆在动态交通环境下的路径规划与避障。
   - 无人机在未知地形中的自主探索与地图构建。
   - 智能家居系统中对家庭环境变化的长期记忆与管理。

4. **技术亮点**：该项目将“空间记忆”概念引入具身智能领域，强调对环境动态演变的持续学习与推理能力，而非静态地图存储，为AI提供了类似生物的时空认知基础。
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 55 | 🍴 1 | 语言: 未知

### Codex-Dream-Skin-Forge
- 描述: 基于 Fei-Away/Codex-Dream-Skin 二次开发的 Codex Desktop 主题工具，新增 Windows 多主题包、应用内切换、Bug 修复与 AI 辅助主题制作。
- 链接: https://github.com/tree0519/Codex-Dream-Skin-Forge
- ⭐ 31 | 🍴 7 | 语言: JavaScript

### codex-dream-skin
- 描述: macOS & Windows Codex Desktop 梦幻换肤 Skill｜由世事宜AI免费提供
- 链接: https://github.com/xnydl/codex-dream-skin
- ⭐ 31 | 🍴 1 | 语言: JavaScript
- 标签: codex, codex-desktop, macos, openai, skill

### RUDR9
- 描述: One command → full AI engineering team. Transforms Hermes Agent into a 9-role development organization with Kanban coordination, per-profile authority enforcement, and PAUL-inspired workflows.
- 链接: https://github.com/ardhaecosystem/RUDR9
- ⭐ 24 | 🍴 4 | 语言: Shell

### uxon-ai
- 描述: UXON is an MCP server and API that lets AI agents and developers create landing pages, run A/B experiments, and track conversions across domains.
- 链接: https://github.com/alexpilotto/uxon-ai
- ⭐ 23 | 🍴 0 | 语言: 未知
- 标签: ab-testing, ai-agents, conversion-tracking, cro-api, experimentation-api

### code-humanizer
- 描述: humanizer, but for code — an agent skill that removes AI-generated code slop: duplicated helpers, try-import fallbacks, broad excepts, speculative abstractions. Test-gated, behavior-preserving.
- 链接: https://github.com/LeonardNJU/code-humanizer
- ⭐ 23 | 🍴 0 | 语言: 未知
- 标签: agent-skills, ai-slop, claude, claude-code, code-quality

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能极其丰富的中文自然语言处理（NLP）资源集合与工具库，由百度工程师维护并持续更新。它涵盖了从基础的分词、词性标注到高级的命名实体识别、知识图谱构建及预训练模型等广泛内容。该项目旨在为开发者提供一站式的中英 NLP 解决方案及相关数据集。

2. **核心功能**
*   **基础 NLP 工具**：提供敏感词过滤、中英语言检测、繁简转换、中文分词（含加速版 jieba_fast）及词向量资源。
*   **信息抽取与识别**：支持手机号、身份证、邮箱等实体抽取，以及基于 BERT 等模型的命名实体识别（NER）和关系抽取。
*   **知识库与词库资源**：内置大量专业词库，如中日文人名、职业、汽车、医学、法律、古诗词及停用词表等。
*   **深度学习模型与数据**：收录多种预训练语言模型（如 BERT, GPT2, ALBERT），并包含中文聊天语料、问答数据集及语音识别语料。

3. **适用场景**
*   **中文 NLP 初学者入门**：适合希望系统学习中文字符处理、分词原理及基础 NLP 流程的开发人员。
*   **企业级文本安全与合规**：适用于需要快速集成敏感词过滤、舆情监控或内容审核系统的互联网产品。
*   **垂直领域知识图谱构建**：为医疗、金融、法律等特定行业提供专用词库、实体识别模型及关系抽取工具，加速知识图谱落地。

4. **技术亮点**
*   **资源极度全面**：整合了数百个细分领域的词库、数据集和预训练模型，是中文 NLP 领域的“百科全书”式资源站。
*   **紧跟前沿技术**：持续更新包括 Transformer、BERT、GPT 系列在内的最新深度学习模型及其在中文语境下的适配代码。
*   **实用工具丰富**：不仅包含算法模型，还提供了如语音情感分析、OCR、拼写检查等可直接落地的工程化小工具。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81837 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目以“Awesome”列表形式呈现，涵盖了从基础到进阶的多种技术栈实现。它为开发者提供了一个全面的技术资源库，便于快速查找和参考相关领域的开源代码。

2. **核心功能**
*   汇集500多个涵盖主流AI子领域的项目源码，提供一站式学习资源。
*   分类清晰，明确区分机器学习、深度学习、计算机视觉和NLP等方向。
*   包含完整的代码实现，方便用户直接克隆、运行和修改以用于实践。
*   作为精选列表（Awesome List），筛选出高质量且具有代表性的开源项目。

3. **适用场景**
*   **初学者入门**：适合刚接触AI领域的学生或转行者，通过阅读和运行这些项目快速理解核心概念。
*   **项目灵感参考**：帮助开发人员寻找具体应用场景（如图像识别、文本分类）的代码范例和最佳实践。
*   **技术调研与对比**：用于评估不同算法或框架在具体任务上的实现方式，辅助技术选型。

4. **技术亮点**
*   规模宏大且分类细致，覆盖了当前AI领域的核心热门方向。
*   强调代码实用性，提供的不仅是理论介绍，而是可直接运行的工程化示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35464 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33235 | 🍴 3156 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21157 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18409 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17321 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13147 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11577 | 🍴 908 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10666 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35464 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33235 | 🍴 3156 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15413 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13147 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置，让用户无需编写大量底层代码即可快速训练和评估机器学习模型。

### 2. 核心功能
- **低代码建模**：通过简单的 YAML 配置文件定义模型架构和数据集，大幅降低开发门槛。
- **广泛支持 AI 类型**：原生支持自然语言处理、计算机视觉及表格数据等多种模态的深度学习任务。
- **模型微调与训练**：内置对主流 LLM（如 Llama、Mistral）及 PyTorch 后端的支持，便于进行高效微调。
- **自动化实验管理**：自动处理数据预处理、模型训练、评估及超参数调整等全流程工作。
- **开箱即用的组件库**：提供丰富的预置层和模块，用户可直接组合使用以构建复杂神经网络。

### 3. 适用场景
- **快速原型开发**：数据科学家或工程师希望在不深入底层代码的情况下，迅速验证机器学习想法。
- **LLM 微调与应用**：需要对 Llama、Mistral 等大语言模型进行特定领域微调或构建定制化 AI 应用。
- **多模态 AI 项目**：涉及文本、图像或结构化数据混合输入的复杂深度学习模型训练。
- **企业级 MLOps 集成**：需要在生产环境中标准化、可重复地部署和管理机器学习流水线。

### 4. 技术亮点
- **声明式配置驱动**：采用基于 YAML 的配置方式，使模型定义直观且易于版本控制。
- **无缝集成主流生态**：深度兼容 PyTorch 及 Hugging Face Transformers，支持广泛的预训练模型。
- **数据中心主义设计**：强调数据处理在模型性能中的关键作用，提供强大的数据预处理管道。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11738 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9136 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6987 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6259 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81837 | 🍴 15249 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73322 | 🍴 8950 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58254 | 🍴 9626 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52362 | 🍴 10590 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖了从数据分析、机器学习实战到深度学习框架（PyTorch、TensorFlow 2）及自然语言处理工具（NLTK）的系统性内容。它不仅包含数学基础如线性代数，还深入讲解了多种经典算法与模型的实际应用。

2. **核心功能**
- 集成数据分析与机器学习实战案例，结合线性代数理论基础。
- 提供 PyTorch 和 TensorFlow 2 等主流深度学习框架的代码实现。
- 涵盖 NLP 领域工具 NLTK 的使用以及多种经典算法（如 SVM、K-Means、LSTM）的源码解析。

3. **适用场景**
- 希望系统掌握机器学习全流程（从理论到代码）的初学者或进阶者。
- 需要参考具体算法实现（如推荐系统、分类回归）以加速开发的数据科学家。
- 致力于深入研究深度学习框架（PyTorch/TF2）与自然语言处理技术的开发者。

4. **技术亮点**
- 社区认可度高，拥有超过 4 万颗星，是知名的开源学习资源。
- 技术栈覆盖全面，横跨传统机器学习、深度学习及自然语言处理三大领域。
- 注重实战，提供基于 scikit-learn 等主流库的具体算法复现代码。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38464 | 🍴 6449 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35464 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33744 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28584 | 🍴 3487 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25911 | 🍴 2924 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它旨在为开发者提供丰富的实践案例和完整的源代码参考。

2. **核心功能**
*   收录大量经过验证的AI项目代码，支持快速上手与复现。
*   全面覆盖机器学习、深度学习、CV和NLP四大主流AI方向。
*   提供结构化的分类索引，便于用户按领域或技术栈查找资源。
*   作为“Awesome”列表，整合了高质量的学习路径和项目范例。

3. **适用场景**
*   AI初学者通过阅读源码进行系统性学习和技能训练。
*   工程师在开发中遇到具体技术瓶颈时，参考类似项目的实现方案。
*   学生或研究人员寻找课程作业、毕业设计或实验的灵感与基准代码。

4. **技术亮点**
*   极高的社区认可度（35000+星标），证明其内容的实用性和权威性。
*   标签体系完善，精准对应当前AI领域的核心技术热点。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35464 | 🍴 7353 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款基于人工智能驱动的自动化工具，能够模拟人类操作来自动化浏览器工作流程。它通过结合计算机视觉与大语言模型（LLM），实现了无需编写复杂代码即可处理动态网页交互的能力，是传统 RPA 与现代 AI 技术的融合产物。

**2. 核心功能**
*   **AI 视觉感知**：利用计算机视觉理解页面布局，而非依赖易碎的 DOM 结构或 XPath。
*   **自然语言驱动**：用户只需输入自然语言指令，即可自动生成并执行相应的浏览器操作步骤。
*   **端到端工作流自动化**：支持跨多个网站和页面的复杂任务编排，如表单填写、数据抓取等。
*   **自修复能力**：当网页 UI 发生变化时，AI 能自适应调整操作策略，保持流程稳定性。
*   **安全合规执行**：在沙箱环境中运行，确保自动化过程的安全性与隐私保护。

**3. 适用场景**
*   **跨平台数据录入**：自动将数据从 Excel 或数据库填入各种不同结构的内部系统或外部网站表单中。
*   **动态网页爬虫**：抓取需要登录、点击交互或反爬机制复杂的非结构化网页内容。
*   **企业级 RPA 替代方案**：用于替代传统 Selenium/Playwright 脚本，降低维护成本，适应频繁变动的 Web 应用。
*   **重复性行政任务自动化**：如自动预约服务、监控价格变动、批量处理邮件附件等日常办公流程。

**4. 技术亮点**
*   **多模态 AI 架构**：深度融合 LLM（逻辑推理）与 Vision 模型（图像识别），实现“看懂页面”并“做出决策”。
*   **超越传统选择器**：摒弃对固定 CSS/XPath 的依赖，采用基于像素和语义的通用交互方式，极大提高了脚本的鲁棒性。
*   **原生 Python API**：提供简洁的 Python SDK，方便开发者将其集成到现有的自动化测试或数据处理管道中。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22367 | 🍴 2094 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### 1. **中文简介**
CVAT 是一款领先计算机视觉标注平台，旨在构建高质量的视觉数据集以支持视觉人工智能应用。它提供开源、云端及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量控制及团队协作。该平台还具备数据分析能力和开发者 API，方便集成到各类深度学习工作流中。

### 2. **核心功能**
*   支持图像、视频及 3D 点云数据的多模态高精度标注。
*   内置 AI 辅助标注功能，显著提升数据标注效率与准确性。
*   提供完善的质量保证机制及团队多人协作标注能力。
*   开放开发者 API，便于与企业现有数据管道或分析工具集成。
*   提供从开源软件到云服务及企业版的多层次产品形态。

### 3. **适用场景**
*   构建用于目标检测、语义分割等任务的训练数据集。
*   需要大规模团队协作进行复杂视频或 3D 场景标注的项目。
*   希望利用 AI 预标注加速数据准备流程的机器学习团队。
*   对数据标注质量有严格管控要求的企业级视觉 AI 开发。

### 4. **技术亮点**
*   **全栈支持**：兼容 PyTorch、TensorFlow 等主流框架及 ImageNet 标准。
*   **多维标注**：覆盖边界框（Bounding Box）、图像分类、对象检测及语义分割等多种任务类型。
*   **生态丰富**：作为行业标准工具之一，拥有活跃的社区支持和丰富的插件生态。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16303 | 🍴 3762 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在提供可微分的、高性能的图像处理与计算机视觉算法，无缝集成到深度学习工作流中。

2. **核心功能**
- 提供大量可微分的几何图像变换和增强操作，支持自动求导。
- 集成先进的计算机视觉算法，如相机标定、立体匹配和姿态估计。
- 与 PyTorch 生态系统深度兼容，允许在 GPU 上高效并行处理张量数据。
- 包含用于机器人学和 3D 视觉的空间变换工具及投影模型。

3. **适用场景**
- 深度学习中的图像数据增强与预处理流水线开发。
- 需要端到端可训练性的计算机视觉模型构建（如单目深度估计）。
- 机器人视觉系统中的实时图像处理与空间感知任务。
- 传统计算机视觉算法向神经网络架构的迁移与优化研究。

4. **技术亮点**
- **可微分设计**：将经典几何视觉算法转化为可微分模块，便于嵌入深度学习框架进行联合优化。
- **PyTorch 原生支持**：完全基于 PyTorch Tensor 实现，充分利用 GPU 加速性能，无需复杂的数据转换。
- 链接: https://github.com/kornia/kornia
- ⭐ 11276 | 🍴 1202 | 语言: Python
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
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. **中文简介**
OpenClaw 是一款全平台、跨操作系统的个人 AI 助手，倡导“龙虾式”的数据自主权理念。它允许用户在任意设备上部署属于自己的 AI 助理，确保数据完全由用户掌控。该项目旨在提供一种私密且灵活的个性化人工智能解决方案。

### 2. **核心功能**
*   **全平台兼容**：支持在任何操作系统和平台上运行，实现无缝的设备适配。
*   **数据私有化**：强调“Own Your Data”，确保用户数据本地化存储与控制，保护隐私。
*   **个人化定制**：作为专属 AI 助理，可根据个人需求进行深度定制和训练。
*   **开源开放**：基于 TypeScript 构建，代码开源，便于社区贡献和二次开发。

### 3. **适用场景**
*   **隐私敏感用户**：需要本地化 AI 服务以避免云端数据泄露的个人或企业用户。
*   **开发者与技术爱好者**：希望部署自托管 AI 助手并进行自定义开发的程序员。
*   **跨设备工作流整合**：需要在不同操作系统（如 macOS、Linux、Windows）间同步个人 AI 助手的用户。

### 4. **技术亮点**
*   **TypeScript 架构**：采用强类型的 TypeScript 开发，保证了代码的可维护性和类型安全。
*   **模块化设计**：支持“龙虾式”灵活扩展，便于集成各种 AI 模型和服务提供商。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383103 | 🍴 80454 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**
Superpowers 是一个经过验证的“代理式技能框架”及软件开发方法论，旨在通过结构化的技能组合提升开发效率。它倡导一种由子代理驱动的开发模式，将复杂的软件生命周期分解为可管理的智能技能单元。

**2. 核心功能**
*   **代理式技能框架**：提供模块化的 AI 技能库，支持像乐高一样组合不同的开发能力。
*   **子代理驱动开发**：引入 Subagent-Driven Development 理念，利用专门化的子代理处理特定任务。
*   **结构化头脑风暴**：内置 brainstorming 机制，辅助团队在编码前进行逻辑梳理和需求发散。
*   **全生命周期覆盖**：涵盖从需求分析、设计到编码测试的完整 SDLC（软件开发生命周期）支持。

**3. 适用场景**
*   **复杂系统架构设计**：需要多步骤推理和模块化设计的软件项目开发。
*   **AI 辅助编程工作流优化**：希望将 AI 深度集成到日常编码习惯中，而非仅作为简单补全工具的场景。
*   **团队协作与知识沉淀**：需要将最佳实践固化为可复用的“技能”并共享给团队成员的团队。

**4. 技术亮点**
*   **方法论创新**：提出了“obra”（可能指代其特有的组织或构建理念）和“skills-first”的开发范式，区别于传统的代码优先模式。
*   **高社区认可度**：拥有超过 25 万星标，证明了该框架在开发者社区中的广泛影响力和实用性验证。
- 链接: https://github.com/obra/superpowers
- ⭐ 255747 | 🍴 22855 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款能够随用户共同成长的智能代理工具，旨在提供持续进化的辅助体验。它深度集成了多种大型语言模型，致力于成为开发者日常编程与任务自动化的高效伙伴。通过灵活适配不同 AI 后端，它实现了从基础对话到复杂代码生成的无缝衔接。

### 2. 核心功能
*   支持多模型后端集成，兼容 OpenAI、Anthropic (Claude)、Codex 等主流 LLM 接口。
*   具备上下文记忆能力，能随着交互深入不断优化对用户需求和问题背景的理解。
*   提供强大的代码辅助功能，包括代码生成、审查、调试及重构建议。
*   支持自定义代理行为配置，允许用户根据特定工作流调整 Agent 的行为模式。
*   内置安全沙箱机制，确保在运行外部代码或执行系统命令时的操作安全性。

### 3. 适用场景
*   **复杂编码任务**：需要跨文件理解、大规模代码重构或集成测试的软件开发场景。
*   **个性化助手定制**：希望拥有一个能记住长期偏好和项目历史的私人开发助理的用户。
*   **多模型切换实验**：研究人员或开发者需要对比不同 LLM 在相同提示词下的表现差异。
*   **自动化工作流**：将重复性的文档处理、数据清洗或报告生成任务交给 Agent 自动完成。

### 4. 技术亮点
*   **模型无关架构**：抽象层设计使得更换底层 AI 提供商变得极其简单，不受单一厂商绑定。
*   **动态成长机制**：通过持久化存储用户反馈和历史会话，实现 Agent 能力的迭代式增强。
*   **开源社区驱动**：拥有极高的 GitHub 星标数（21万+），表明其拥有庞大的活跃社区和持续的生态贡献。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215716 | 🍴 40233 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196642 | 🍴 59360 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. **中文简介**
AutoGPT 致力于让每个人都能轻松获取、使用并构建基于 AI 的工具，践行其“人人可用”的愿景。其核心使命是提供强大的自动化基础设施，让用户能够将精力集中在真正重要的业务逻辑与创新上。

### 2. **核心功能**
*   **自主代理执行**：能够根据用户设定的目标，自主规划步骤并执行复杂的多轮任务。
*   **多模型支持**：兼容 OpenAI、Anthropic Claude、LLaMA 等多种大型语言模型 API，灵活适配不同需求。
*   **工具链集成**：可连接互联网搜索、文件读写、代码解释器等外部工具，扩展 AI 的行动能力。
*   **记忆与上下文管理**：具备长期记忆机制，能在多次交互中保持上下文连贯性，提升任务完成的准确性。
*   **低代码/无代码构建**：提供直观的用户界面和模块化设计，降低非技术人员使用高级 AI 代理的门槛。

### 3. **适用场景**
*   **自动化内容创作**：自动进行市场调研、撰写博客文章或生成社交媒体文案。
*   **复杂数据分析**：自主爬取公开数据、清洗信息并生成可视化报告或摘要。
*   **智能客服与助手**：构建能理解长期对话历史并执行具体操作（如查订单、改设置）的高级客服机器人。
*   **开发者效率提升**：辅助编写测试用例、调试代码或自动化部署流程，减少重复性编程工作。

### 4. **技术亮点**
*   **开源生态与社区驱动**：拥有极高的社区活跃度（超 18 万星标），持续迭代且透明开放。
*   **插件化架构**：支持通过简单配置快速接入新的 API 或服务，实现功能的高度可扩展性。
*   **多 LLM 后端抽象层**：统一了不同大模型的调用接口，使得切换底层推理引擎变得无缝且便捷。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185576 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165846 | 🍴 21451 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164276 | 🍴 30530 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157072 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151953 | 🍴 9680 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151746 | 🍴 8668 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

