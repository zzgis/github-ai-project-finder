# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### skills
- ### 1. 中文简介
该项目是一个开源的 OpenAI Codex 主题技能、AI 主题生成器以及跨平台运行时，专为自定义 Codex 桌面主题设计。它允许用户通过 AI 辅助生成和部署个性化的开发者工具界面风格。

### 2. 核心功能
- **AI 主题生成**：集成 AI 能力，自动生成符合用户需求的 Codex 桌面主题。
- **跨平台运行时支持**：提供在 macOS 和 Windows 等平台上运行自定义主题的兼容环境。
- **主题管理与皮肤定制**：支持对 Codex 应用进行深度的视觉定制和主题切换管理。
- **基于 Chromium 协议开发**：利用 Chromium DevTools Protocol 实现底层界面的定制化控制。

### 3. 适用场景
- **追求个性化界面的开发者**：希望摆脱默认外观，通过 AI 快速创建独特编码环境的程序员。
- **Codex 重度用户**：需要长期使用 OpenAI Codex 且对视觉体验有较高要求的终端用户。
- **前端与 UI 定制爱好者**：对 Chromium 内核应用进行二次开发和主题皮肤设计的爱好者。

### 4. 技术亮点
- 结合了 OpenAI 的 AI 生成能力与 Chromium DevTools Protocol 的强大定制潜力。
- 实现了从“主题生成”到“跨平台部署”的一站式工作流，简化了复杂主题的开发门槛。
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 118 | 🍴 13 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### yuwen-publish-precheck
- ### 1. **中文简介**
这是一款面向抖音、小红书及微信视频号的AI内容合规预检工具，旨在帮助用户在发布前识别违规风险点并获取即时修改建议。它基于38篇真实样本校准判定标准，引用72条官方规则作为依据，通过本地规则库的不断迭代优化检测精度。

### 2. **核心功能**
*   **多平台合规检查**：支持对抖音、小红书和微信视频号的文案进行针对性的敏感内容筛查。
*   **违规定位与解释**：精准标记踩线语句，并明确引用对应的官方规则条款作为判定依据。
*   **智能修改建议**：提供可直接使用的合规化改写方案，帮助用户快速调整内容。
*   **本地规则库进化**：利用真实样本校准判定尺度，随使用积累沉淀出更精准的本地规则库。
*   **Cursor集成技能**：作为Agent Skills设计，无缝集成至Cursor编辑器中实现自动化工作流。

### 3. **适用场景**
*   **自媒体创作者日常发布**：在将视频脚本或图文笔记发布到社交平台前，进行最后一道合规性审查。
*   **MCN机构内容审核**：批量检查旗下博主的内容素材，降低因违规导致的限流或封号风险。
*   **广告营销文案优化**：确保品牌宣传内容符合各平台的广告法及社区规范，避免法律纠纷。
*   **新手运营学习**：通过查看具体的违规原因和官方依据，快速理解各平台的潜规则与红线。

### 4. **技术亮点**
*   **基于真实数据的校准机制**：不依赖通用模型幻觉，而是通过38篇真实样本和72条官方原文引文来锚定判定尺度，提高准确率。
*   **可解释性强**：不仅指出错误，还明确“依据哪条官方规则”，增强了用户对AI判断的信任度。
*   **Cursor Agent Skills架构**：采用模块化设计，易于嵌入现有的AI编程/写作辅助工作流中。
*   **本地知识增强**：通过本地规则库的持续积累，使系统越用越懂用户的具体业务场景和常用雷区。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 96 | 🍴 6 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### claude-arbitrage-bot
- **1. 中文简介**
这是一个专为以太坊兼容网络设计的套利机器人，具备内置的Python自动化功能。该项目利用智能合约执行交易策略，旨在捕捉不同市场间的价格差异以获取收益。

**2. 核心功能**
*   支持在以太坊及其兼容链路上进行自动化套利交易。
*   集成Python脚本实现策略逻辑与外部接口交互。
*   部署Solidity智能合约以处理链上资产交换。
*   提供针对加密资产价格波动的实时监控与响应机制。

**3. 适用场景**
*   去中心化交易所（DEX）之间的价差套利操作。
*   需要自动化执行高频小额交易策略的开发者或交易者。
*   希望结合AI辅助（如标签所示的Claude/GPT）优化交易逻辑的技术用户。

**4. 技术亮点**
*   采用Solidity编写底层智能合约，确保链上执行的透明度与安全性。
*   通过Python自动化框架简化了复杂的交易流程配置与管理。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### cue
- 1. **中文简介**
Cue 是一款开源的 macOS AI 协作者，它以浮动窗口形式覆盖在屏幕之上，能够实时“观看”和“聆听”你的会议内容。它具备隐私保护特性，可确保在屏幕共享时保持隐藏，是 Cluely 的替代方案，并支持用户自带 API Key（Bring Your Own Key）。

2. **核心功能**
*   **屏幕浮动交互**：作为浮动工具驻留在 macOS 屏幕顶层，便于随时查看 AI 辅助信息。
*   **多模态会议监听**：同时通过视觉（看）和听觉（听）捕捉会议内容，实现全方位的会议记录与分析。
*   **屏幕共享隐私保护**：智能识别屏幕共享状态并自动隐藏自身，防止会议参与者看到该工具，保障隐私。
*   **自带密钥支持**：允许用户自行提供 AI 模型的 API Key，增强数据主权和灵活性。
*   **Cluely 替代方案**：提供类似 Cluely 的会议助手体验，但采用开源架构且无需依赖特定厂商账号。

3. **适用场景**
*   **远程会议记录与摘要**：在 Zoom、Teams 等线上会议中自动生成会议纪要和关键要点。
*   **敏感商业谈判**：在需要进行屏幕共享演示的商务场合中，秘密记录对话内容而不暴露辅助工具。
*   **个人知识管理**：快速提取会议中的行动项（Action Items）和决策点，整理进个人笔记系统。
*   **语言学习或转录**：非英语母语者利用其实时转写和理解功能辅助理解会议内容。

4. **技术亮点**
*   **开源与 BYOK 模式**：基于开源代码构建，并采用“自带密钥”架构，降低了厂商锁定风险，提升了用户对数据的控制权。
*   **macOS 原生集成**：针对 macOS 环境优化，利用其窗口管理和屏幕共享 API 实现高效的浮动显示与隐藏逻辑。
- 链接: https://github.com/Blueturboguy07/cue
- ⭐ 76 | 🍴 12 | 语言: JavaScript

### ai-api-relay-guide
- 1. **中文简介**
该项目是一个基于 GitHub Pages 部署的 AI API 中转站推荐指南，重点对比了 GPT 和 Claude 等主流模型的服务价格与性能。通过类似“PokeAPI”的直观评测方式，展示了如 GPT 低至 0.03 倍、Claude 低至 0.2 倍的优惠费率，帮助用户快速筛选高性价比的 AI 接口服务。

2. **核心功能**
*   提供主流大语言模型（如 GPT、Claude）的 API 中转服务商比价与评测。
*   通过可视化或结构化数据展示不同中转站的价格系数（如 0.03x、0.2x）。
*   基于 GitHub Pages 静态托管，确保推荐列表的轻量级访问和高可用性。
*   聚合 AI API 相关资源，为用户提供一站式的选型参考指南。

3. **适用场景**
*   开发者寻找低成本、高稳定性的第三方 AI 模型接口接入方案。
*   企业或个人希望降低调用 GPT/Claude 等大模型 API 的成本。
*   需要快速对比不同中转服务商价格与服务质量的调研工作。

4. **技术亮点**
*   采用 GitHub Pages 静态页面技术，无需后端服务器即可实现全球高速访问。
*   虽然主要语言标注为 CSS，但其核心价值在于结构化的数据呈现与直观的评测逻辑设计。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 75 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### SuperMap
- 描述: SuperMap is a living spatial memory for embodied AI — it perceives the world, remembers its evolution, and supports reasoning and action.
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 57 | 🍴 1 | 语言: 未知

### Codex-Dream-Skin-Forge
- 描述: 基于 Fei-Away/Codex-Dream-Skin 二次开发的 Codex Desktop 主题工具，新增 Windows 多主题包、应用内切换、Bug 修复与 AI 辅助主题制作。
- 链接: https://github.com/tree0519/Codex-Dream-Skin-Forge
- ⭐ 35 | 🍴 8 | 语言: JavaScript

### codex-dream-skin
- 描述: macOS & Windows Codex Desktop 梦幻换肤 Skill｜由世事宜AI免费提供
- 链接: https://github.com/xnydl/codex-dream-skin
- ⭐ 34 | 🍴 1 | 语言: JavaScript
- 标签: codex, codex-desktop, macos, openai, skill

### RUDR9
- 描述: One command → full AI engineering team. Transforms Hermes Agent into a 9-role development organization with Kanban coordination, per-profile authority enforcement, and PAUL-inspired workflows.
- 链接: https://github.com/ardhaecosystem/RUDR9
- ⭐ 27 | 🍴 5 | 语言: Shell

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 26 | 🍴 0 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具集与资源仓库，涵盖了从基础文本处理到高级知识图谱构建的多种功能。它集成了敏感词检测、实体抽取、情感分析及大量专业领域词典，旨在为开发者提供一站式的中英文 NLP 解决方案。该项目还收录了大量开源数据集、预训练模型及前沿技术论文，是中文 NLP 领域的综合性资源库。

### 2. 核心功能
*   **基础文本处理**：提供敏感词过滤、繁简转换、中英文混合分割及标点修复等功能。
*   **信息抽取与识别**：支持手机号、身份证、邮箱等实体抽取，以及基于 BERT/ALBERT 的命名实体识别（NER）。
*   **语义与情感分析**：包含词汇情感值计算、同义/反义词库、文本相似度匹配及情感分类工具。
*   **专业知识库与数据**：内置中日文人名库、行业词库（医疗、法律、汽车等）及大量公开数据集（如百度知道、医疗对话等）。
*   **语音与自然语言生成**：集成中文语音识别（ASR）、OCR 文字识别、歌词生成及自动摘要工具。

### 3. 适用场景
*   **内容安全审核**：用于互联网平台的敏感词过滤、暴恐词筛查及谣言检测。
*   **智能客服与对话系统**：利用知识图谱、意图识别及聊天机器人框架构建垂直领域（如医疗、金融）的智能问答助手。
*   **数据标注与预处理**：为 NLP 模型训练提供标准化的清洗工具、实体标注辅助及高质量中文语料。
*   **学术研究与技术选型**：作为研究人员探索最新 NLP 模型（如 BERT 变体）、获取数据集及参考开源代码的资源库。

### 4. 技术亮点
*   **资源极度丰富**：不仅包含代码库，还汇集了清华 XLORE、百度开源基准、大量学术论文及竞赛 TOP 方案，兼具工具性与资料性。
*   **多模态与跨语言支持**：整合了 NLP、OCR、ASR 及多语言（中英日韩等）处理能力，适应复杂应用场景。
*   **紧跟前沿技术**：收录了 BERT、GPT-2、ALBERT、RoBERTa 等主流预训练模型的应用案例及微调代码，便于快速落地。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81842 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个包含500个AI项目的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供完整的代码实现。该项目旨在为开发者提供一个全面的学习资源库，通过实际案例帮助掌握人工智能核心技术。它被标记为“Awesome”列表，是AI初学者和专业人士快速入门和进阶的优质指南。

**2. 核心功能**
*   汇集500个涵盖AI主要子领域的实战项目，提供从基础到高级的代码示例。
*   分类清晰，明确区分机器学习、深度学习、计算机视觉（CV）和自然语言处理（NLP）等不同方向。
*   作为“Awesome”列表资源，经过筛选确保项目质量和实用性，适合系统性学习。
*   提供Python语言的代码实现，便于开发者直接运行、修改和深入研究。
*   整合了广泛的技术标签，方便用户根据特定兴趣或技能需求快速检索相关项目。

**3. 适用场景**
*   **AI初学者学习**：适合刚接触人工智能的学生或转行者，通过复制运行代码来理解基本概念和流程。
*   **项目灵感获取**：数据科学家或工程师在寻找下一个实践课题时，可从中挑选适合的业务场景进行复现或改进。
*   **技术栈速查**：需要快速回顾或验证特定AI算法（如CNN、RNN、Transformer）在CV或NLP中应用方式的开发者。
*   **教学与培训**：教育机构或企业内部培训讲师，可利用这些现成的代码和项目结构作为教学案例。

**4. 技术亮点**
*   **规模宏大且结构完整**：一次性提供500个项目，覆盖AI主流方向，避免了碎片化信息收集的成本。
*   **代码即学即用**：所有项目均附带可运行的代码，强调实践导向，缩短了从理论到应用的距离。
*   **社区认证质量**：作为“Awesome”系列项目，通常意味着经过社区长期维护和高质量筛选，可靠性高。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35467 | 🍴 7354 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款轻量级的神经网络、深度学习及机器学习模型可视化工具。它支持多种主流框架格式，允许用户通过图形界面直观地检查模型结构和参数。该工具旨在帮助开发者快速调试和理解复杂的模型架构。

### 2. 核心功能
*   支持广泛模型格式，包括 ONNX, PyTorch, TensorFlow, Keras, CoreML, TFLite 等。
*   提供直观的图形化界面，清晰展示神经网络层结构及数据流向。
*   允许查看和编辑模型权重及偏置参数，便于深入分析模型细节。
*   具备简单的模型转换功能，支持在不同框架格式之间进行互转。

### 3. 适用场景
*   模型调试与验证：在部署前检查模型结构是否正确，排查层连接错误。
*   教学与交流：向非技术人员或学生直观展示深度学习模型的内部工作原理。
*   格式迁移辅助：在从一种框架（如 PyTorch）迁移到另一种框架（如 ONNX/TFLite）时验证模型一致性。
*   快速原型审查：无需编写代码即可快速浏览和确认第三方开源模型的结构。

### 4. 技术亮点
*   **多语言后端支持**：虽然前端主要基于 JavaScript/HTML5，但后端支持 Python 等多种语言，实现了跨平台兼容性。
*   **即开即用**：提供桌面应用、Web 版本及命令行工具，用户可无需安装复杂环境直接打开模型文件进行分析。
*   **社区驱动与高活跃度**：拥有超过 33k 的 GitHub 星标，表明其在 AI 可视化领域的广泛认可和高频使用情况。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33238 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21157 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面且实用的指南，旨在帮助工程师构建、训练和优化大规模机器学习系统。它涵盖了从底层基础设施到高级模型部署的完整工程实践，是连接理论与生产环境的重要资源。

2. **核心功能**
- 提供大规模分布式训练的实战技巧与最佳实践。
- 深入解析大语言模型（LLM）的微调、推理及优化策略。
- 指导如何高效管理GPU资源、存储及网络配置以提升可扩展性。
- 涵盖MLOps全流程，包括调试、监控及模型部署的工程化方案。
- 详细介绍PyTorch、Transformers等主流框架在工业级场景中的应用。

3. **适用场景**
- 需要从零搭建或优化大规模深度学习集群的ML工程师。
- 致力于降低大语言模型训练成本并提升推理效率的团队。
- 希望实现模型从实验环境到生产环境无缝部署的DevOps/MLOps专家。
- 寻求解决分布式训练中常见瓶颈（如通信开销、显存不足）的研究人员。

4. **技术亮点**
该项目结合了前沿的LLM技术与扎实的底层系统工程知识，提供了大量可直接复现的代码示例和针对Slurm等调度器的具体配置建议，极具工业落地价值。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18412 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17321 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15414 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13148 | 🍴 2663 | 语言: 未知
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
- **1. 中文简介**
这是一个包含500个AI相关项目的精选资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目附带完整的代码实现，旨在为开发者提供丰富的实战案例和学习参考。它被标记为“Awesome”列表，是人工智能领域一个高质量的项目集合。

**2. 核心功能**
*   提供500个经过筛选的AI项目链接，覆盖主流技术栈。
*   所有项目均附带源代码，便于用户直接运行和复现结果。
*   分类清晰，涵盖机器学习、深度学习、CV和NLP四大核心方向。
*   作为学习资源库，帮助开发者快速了解行业前沿项目和最佳实践。

**3. 适用场景**
*   **初学者入门**：通过阅读和运行示例代码，快速掌握AI基本概念和技术。
*   **项目灵感获取**：寻找创意或参考架构，用于个人作品集或开源贡献。
*   **技术调研**：快速了解特定领域（如目标检测、情感分析）的最新开源工具和方法。

**4. 技术亮点**
*   **高人气与权威性**：拥有超过35,000颗星标，表明其在社区中具有很高的认可度和实用性。
*   **综合性强**：一次性整合了AI领域的多个子学科，避免用户在不同仓库间频繁切换。
*   **代码导向**：强调“with code”，确保提供的不仅是理论概念，而是可执行的工程实践。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35467 | 🍴 7354 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款强大的可视化工具，支持查看和调试神经网络、深度学习及机器学习模型。它允许用户直观地检查模型结构，适用于多种主流框架生成的模型文件。

### 2. 核心功能
*   **多格式支持**：兼容 CoreML、Keras、ONNX、PyTorch、TensorFlow 等广泛使用的模型格式。
*   **交互式可视化**：提供清晰的模型架构图，便于用户快速理解数据流向和网络层级。
*   **跨平台运行**：基于 Web 技术构建，支持在浏览器或桌面端直接打开模型进行查看。
*   **模型调试辅助**：帮助开发者定位模型结构问题，优化部署前的检查流程。

### 3. 适用场景
*   **模型结构审查**：在部署前直观检查神经网络层连接是否正确，确保模型架构符合预期。
*   **跨框架迁移验证**：将模型从 PyTorch 或 TensorFlow 转换为 ONNX 或其他格式后，验证转换后的结构一致性。
*   **教育与演示**：向非技术人员或学生展示复杂的深度学习模型内部工作原理，提升沟通效率。

### 4. 技术亮点
*   **轻量级与易用性**：无需安装复杂的依赖环境，通过简单的拖拽或点击即可加载模型进行分析。
*   **广泛的生态兼容性**：深度集成 safetensors、numpy 等现代 ML 标准，覆盖从科研到生产的全链路模型格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33238 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 以下是针对 GitHub 项目 `cheatsheets-ai` 的技术分析：

1. **中文简介**
该项目为深度学习和机器学习研究人员提供了一系列 essential 速查表（Cheat Sheets）。内容涵盖了从基础数学库到主流深度学习框架的关键代码示例与概念总结，旨在帮助研究者快速回顾和查阅常用技术细节。

2. **核心功能**
*   集成 NumPy、SciPy 和 Matplotlib 等基础科学计算与可视化库的核心用法速查。
*   提供 Keras 深度学习框架的关键 API 调用示例及模型构建模式。
*   涵盖机器学习算法基础概念与关键参数的简明总结。
*   以结构化文档形式呈现，便于快速检索而非系统学习。

3. **适用场景**
*   **面试准备**：机器学习工程师或研究员在准备技术面试时，快速复习常用库函数和算法细节。
*   **日常开发辅助**：在进行深度学习建模时，忘记特定库（如 NumPy 广播机制或 Keras 层定义）的具体语法时作为参考手册。
*   **知识复盘**：研究人员在切换不同技术栈或回顾旧项目时，快速梳理核心工具链的使用规范。

4. **技术亮点**
*   高度浓缩的知识图谱：将复杂的官方文档提炼为最核心的代码片段和概念对照，极大降低查阅时间成本。
*   多技术栈整合：在一个资源中同时覆盖数据处理（NumPy/SciPy）、可视化（Matplotlib）和建模（Keras），形成完整的工作流参考。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15414 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，涵盖 Python、机器学习、深度学习及自然语言处理等热门领域。该项目整理了近 200 个实战案例并提供免费配套教材，旨在帮助零基础用户轻松入门并实现就业实战。

2. **核心功能**
*   提供从数学基础到高级算法的系统化 AI 学习路径。
*   收录近 200 个精选实战案例与项目以强化动手能力。
*   免费提供配套学习资料，支持从零开始的渐进式学习。
*   覆盖 TensorFlow、PyTorch、Keras 等多主流框架的技术解析。
*   聚焦数据分析、计算机视觉和 NLP 等实际就业技能培养。

3. **适用场景**
*   希望系统掌握 AI 知识体系的编程初学者或转行人员。
*   需要大量实战代码参考以提升工程能力的学生或开发者。
*   寻求免费且高质量学习资源以降低入门成本的个人学习者。
*   准备从事数据科学、算法工程师等岗位求职的候选人。

4. **技术亮点**
*   内容体系完整，横跨数学基础、主流框架及应用领域。
*   实战资源丰富，提供近百个可复现的代码案例与项目。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13148 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **项目名称：** Ludwig

1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他 AI 模型的构建与训练过程。它通过声明式配置和自动化流程，降低了深度学习应用的开发门槛。

2. **核心功能**
*   **低代码/无代码构建：** 支持通过 YAML 配置文件快速定义和训练多种类型的机器学习模型。
*   **多模态支持：** 原生支持文本、图像、音频、视频、表格等多种数据类型的处理与分析。
*   **内置自动调优：** 集成超参数优化功能，自动寻找最佳模型配置以提升性能。
*   **开箱即用的预训练模型：** 提供针对常见任务优化的预训练模型，便于快速微调（Fine-tuning）。
*   **可视化实验管理：** 内置 Web UI 工具，方便监控训练进度、比较不同模型版本的效果。

3. **适用场景**
*   **快速原型开发：** 数据科学家或初学者希望无需深入底层代码即可快速验证机器学习想法。
*   **多模态应用构建：** 需要同时处理文本、图像或音频等混合数据类型的复杂 AI 项目。
*   **企业级模型部署：** 团队需要标准化、可复现且易于维护的模型训练与工作流。
*   **迁移学习与微调：** 基于现有的强大基础模型（如 LLaMA、Mistral）进行特定领域的适配训练。

4. **技术亮点**
*   基于 PyTorch 构建，兼容性强且易于扩展。
*   强调“以数据为中心”的开发理念，简化了数据处理管道。
*   对主流 LLM 架构（如 LLaMA2, Mistral）有良好的微调支持。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9136 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3102 | 语言: C++
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
- 1. **中文简介**
funNLP 是一个全面且丰富的中文自然语言处理资源集合，涵盖了从基础工具（如分词、命名实体识别、敏感词检测）到高级应用场景（如知识图谱、语音识别、聊天机器人）的各类开源项目、数据集及预训练模型。该项目旨在为开发者提供一站式的 NLP 学习与实践素材，包括大量的专业词库、语料库、代码示例以及前沿的学术研究资源。

2. **核心功能**
*   **基础NLP工具与库**：整合了中文分词、词性标注、命名实体识别（NER）、文本分类、情感分析及关键短语抽取等实用工具和预训练模型。
*   **丰富词库与数据资源**：提供了中英文敏感词、手机号/身份证/邮箱抽取规则、行业专用词库（医疗、法律、汽车等）、古诗文、地名人名及大量公开数据集。
*   **语音与OCR技术**：收录了中文语音识别（ASR）、语音情感分析、中文手写汉字识别以及文档表格自动检测与提取的相关资源和代码。
*   **知识图谱与问答系统**：汇集了各类中文知识图谱构建案例、基于知识图谱的问答系统、实体链接及关系抽取的研究成果与工具。
*   **学术研究与前沿模型**：整理了最新的预训练语言模型（如BERT、GPT-2、ELECTRA等）、NLP竞赛获奖方案、经典课程资料及相关的学术论文解读。

3. **适用场景**
*   **NLP初学者学习与入门**：适合想要系统了解中文自然语言处理流程、掌握基础分词、实体识别等技能的学生和初级开发者。
*   **工业级应用开发参考**：适用于需要快速集成中文文本处理能力的企业开发者，可直接调用其中的敏感词过滤、信息抽取或行业词库模块。
*   **算法研究与模型复现**：研究人员可利用其中的数据集、基准测试（Benchmark）及最新模型代码，进行模型优化、竞赛方案复现或新算法探索。
*   **垂直领域解决方案构建**：在医疗、金融、法律等垂直领域，开发者可借助其提供的专用词库、知识图谱资源及领域模型加速业务系统的落地。

4. **技术亮点**
*   **资源极度全面**：不仅包含代码，还囊括了数据集、词库、论文、课程和工具链，是中文 NLP 领域的“百科全书”。
*   **紧跟技术前沿**：持续更新包含 BERT、GPT-2 等最新预训练模型及各类 SOTA（State-of-the-Art）方案的实现与解析。
*   **兼顾实用与学术**：既有即插即用的工具库（如 jieba 加速版、OCR 工具），又有深度的学术资源（如竞赛 TOP 方案、理论综述），满足多层次需求。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81842 | 🍴 15249 | 语言: Python

### LlamaFactory
- ### 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目旨在简化指令微调、强化学习对齐等复杂流程，使其更加便捷高效。作为 ACL 2024 收录的研究成果，它提供了从基础模型到高级应用的完整解决方案。

### 2. **核心功能**
*   **多模型支持**：兼容 Llama、Qwen、Gemma、DeepSeek 等 100 多种主流开源模型的微调。
*   **全参数与高效微调**：支持全参数训练以及 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法。
*   **多种训练范式**：内置指令微调（SFT）、奖励模型训练（RM）、PPO 强化学习（RLHF）及 DPO/ORPO 等对齐算法。
*   **量化部署优化**：支持 4-bit 和 8-bit 量化训练与推理，显著降低显存占用并提升运行效率。
*   **一站式工作流**：提供从数据预处理、模型训练到推理部署的全流程可视化工具和脚本支持。

### 3. **适用场景**
*   **企业级模型定制**：利用私有领域数据对基座模型进行指令微调，构建垂直行业专属助手。
*   **资源受限环境开发**：通过 QLoRA 等技术，在消费级显卡上高效微调大型语言模型。
*   **多模态应用开发**：针对视觉语言模型（VLM）进行微调，实现图文理解与生成的定制化任务。
*   **AI 安全与对齐研究**：使用 RLHF 或 DPO 等方法优化模型输出，使其更符合人类价值观和安全规范。

### 4. **技术亮点**
*   **统一架构设计**：基于 Hugging Face Transformers 和 PEFT 库封装，屏蔽底层复杂性，实现“开箱即用”。
*   **高性能量化训练**：率先整合 bitsandbytes 等库，实现低比特量化下的稳定训练，大幅节省硬件成本。
*   **前沿算法集成**：快速跟进并集成最新的微调算法（如 ORPO、DPO），保持技术领先性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73326 | 🍴 8950 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个定期更新的仓库，汇集了从 Anthropic、OpenAI、Google 及 xAI 等主流厂商的模型中提取的系统提示词（System Prompts）。内容涵盖 Claude、ChatGPT、Gemini 等多个知名 AI 模型及开发工具的内部指令配置。

### 2. 核心功能
*   **多厂商数据聚合**：整合了 Anthropic、OpenAI、Google 和 xAI 等公司的多种大语言模型及工具的提示词。
*   **实时动态更新**：随着新模型或版本的发布，仓库会持续同步最新的系统提示词信息。
*   **提示词逆向提取**：通过技术手段获取并记录各大模型底层用于指导行为生成的系统级指令。

### 3. 适用场景
*   **提示词工程研究**：帮助开发者深入理解不同模型的行为逻辑与约束机制，优化自定义提示词效果。
*   **竞品分析与安全审计**：供研究人员分析各厂商模型的底层设计差异，或评估潜在的安全边界与对齐策略。
*   **AI 教育与学习**：为学习者提供直观的示例，展示顶级 AI 产品如何设定角色、规范输出格式及处理边界情况。

### 4. 技术亮点
*   **覆盖前沿模型**：包含了如 Claude Fable 5、ChatGPT GPT-5.6 及 Gemini 3.5 Flash 等较新版本或特定变体的内部指令细节。
*   **跨平台统一整理**：将分散在不同生态系统（Anthropic、OpenAI、Google、xAI）中的非公开技术细节进行了结构化汇总。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58301 | 🍴 9635 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52367 | 🍴 10592 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战以及深度学习框架（如 PyTorch、TensorFlow 2）的综合学习资源库。该项目还深入讲解了线性代数和自然语言处理工具（NLTK），旨在为学习者提供从理论基础到代码实现的完整指导。

2. **核心功能**
- 集成多种经典机器学习算法（如 SVM、K-Means、AdaBoost 等）的代码实现与解析。
- 提供基于 TensorFlow 2 和 PyTorch 的深度神经网络（DNN、RNN、LSTM 等）实战案例。
- 包含自然语言处理（NLP）相关技术，利用 NLTK 进行文本分析与推荐系统构建。
- 融合数学基础（线性代数）与数据统计分析，夯实机器学习理论根基。

3. **适用场景**
- 机器学习初学者系统性地掌握从传统算法到深度学习的核心技能。
- 数据科学家或工程师快速查阅特定算法（如 PCA、SVD、FP-Growth）的实现细节。
- 需要构建推荐系统或进行 NLP 文本挖掘项目的开发参考。

4. **技术亮点**
- 项目标签丰富且全面，覆盖了从基础统计学习到前沿深度学习（DL）的关键技术领域。
- 结合了理论数学（线性代数）与工程实践（Scikit-learn, Sklearn），适合全栈式学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38487 | 🍴 6454 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35467 | 🍴 7354 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33744 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28588 | 🍴 3488 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25915 | 🍴 2924 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码库合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例与参考代码，助力快速掌握相关技术应用。

2. **核心功能**
- 提供大量现成的AI项目代码示例，支持直接运行或修改。
- 覆盖机器学习、深度学习、计算机视觉及NLP四大主流AI领域。
- 作为学习资源库，帮助初学者和进阶者理解复杂算法的实现细节。
- 通过标签分类整理项目，便于用户根据特定技术栈快速检索。

3. **适用场景**
- AI初学者用于系统学习各细分领域的基础概念与代码实现。
- 工程师在开发过程中寻找特定功能（如图像识别、文本分类）的代码参考。
- 研究人员或学生利用现有项目进行算法验证或扩展实验。
- 企业团队评估AI技术可行性时，作为快速原型开发的素材库。

4. **技术亮点**
- 项目数量庞大（500+），覆盖面广，是社区中极具规模的Awesome列表。
- 强调“代码即文档”，所有项目均附带可执行的源代码，实用性极强。
- 标签体系完善，精准对应当前热门的AI子领域和技术方向。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35467 | 🍴 7354 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的复杂工作流。它利用大语言模型（LLM）和计算机视觉技术，模拟人类在浏览器中的操作，从而替代传统的脚本化自动化方案。

2. **核心功能**
*   通过视觉感知和自然语言指令自动驱动浏览器操作。
*   支持动态网页交互，无需预先编写固定的选择器或脚本。
*   集成 Playwright 等主流浏览器自动化工具以实现高效渲染和控制。
*   具备处理非结构化页面内容的能力，适应频繁变动的网页布局。

3. **适用场景**
*   跨平台的数据采集与表单自动填写任务。
*   需要登录且验证码或布局多变的后台管理系统操作。
*   替代传统 RPA 工具进行复杂的端到端业务流程自动化。

4. **技术亮点**
*   结合 LLM 理解意图与 Computer Vision 定位元素，实现“所见即所得”的操作逻辑。
*   基于 Python 构建，原生支持 Playwright，易于集成到现有的开发环境中。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22389 | 🍴 2096 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的标注，并提供开源、云版和企业级产品。它具备 AI 辅助标注、质量保证、团队协作及开发者 API 等强大功能，旨在提升视觉 AI 的数据准备效率。

2. **核心功能**
*   支持图像、视频和 3D 数据的多维度高精度标注。
*   集成 AI 辅助标注工具，显著提升数据标记速度与准确性。
*   提供团队协作、质量控制及数据分析等全流程管理功能。
*   开放开发者 API，便于与企业现有工作流或自动化系统无缝集成。

3. **适用场景**
*   计算机视觉算法训练所需的大规模高质量数据集构建。
*   需要多人协同作业的大型图像或视频标注项目管理。
*   希望利用 AI 预标注功能来加速数据清洗与标记流程的企业。

4. **技术亮点**
*   兼容主流深度学习框架（如 PyTorch、TensorFlow），支持物体检测、语义分割等复杂任务。
*   提供从开源本地部署到云端及企业级的灵活产品形态，满足不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16307 | 🍴 3762 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### 1. 中文简介
该项目专注于计算机视觉领域的先进AI可解释性研究，支持包括CNN、Vision Transformers在内的多种模型架构。它提供了全面的可视化工具，涵盖分类、目标检测、分割及图像相似度等多种任务，旨在提升深度学习模型的透明度。

### 2. 核心功能
*   支持梯度加权类激活映射（Grad-CAM）及其变体（如Score-CAM）。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）等主流架构。
*   适用于图像分类、目标检测、语义分割及图像相似度计算等多种视觉任务。
*   提供直观的可视化输出，帮助理解模型决策依据。

### 3. 适用场景
*   深度学习模型调试与错误分析，定位模型关注区域。
*   医疗影像分析中的病灶定位与辅助诊断解释。
*   自动驾驶或安防监控中目标检测模型的可信度验证。
*   学术研究或技术报告中展示模型内部工作原理。

### 4. 技术亮点
*   实现了多种先进的可解释性算法（如Grad-CAM++, Score-CAM等）。
*   模块化设计，易于集成到现有的PyTorch项目中。
*   广泛支持最新的视觉Transformer架构，适应前沿技术发展。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12913 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在通过可微分的图像处理操作，简化深度学习与计算机视觉的结合。该项目致力于提供高效、模块化的工具，以支持机器人、自动驾驶等领域的视觉任务开发。

2. **核心功能**
*   提供大量可微分的传统计算机视觉算子，便于嵌入神经网络进行端到端训练。
*   支持复杂的几何变换、相机标定及三维重建等空间计算任务。
*   与 PyTorch 生态深度集成，实现无缝的数据张量处理和 GPU 加速。
*   包含丰富的图像增强、特征提取和语义分割等深度学习辅助功能。

3. **适用场景**
*   **机器人视觉导航**：用于实时处理传感器数据，实现环境感知与路径规划。
*   **自动驾驶系统**：在端到端驾驶模型中处理车道线检测、障碍物识别等几何任务。
*   **可微分图形渲染**：结合传统几何约束与深度学习，优化摄影测量或三维重建流程。

4. **技术亮点**
*   **可微分性**：其核心优势在于将传统 CV 算法转化为可微模块，使得梯度可以反向传播，从而允许传统视觉组件直接在深度学习框架中训练。
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
- ⭐ 3284 | 🍴 403 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383120 | 🍴 80463 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**
Superpowers 是一个经过验证的代理技能框架与软件开发方法论，旨在通过结构化的方式提升开发效率。它结合了头脑风暴、编码及软件开发生命周期（SDLC）的最佳实践，利用子代理驱动开发模式来解决复杂问题。

**2. 核心功能**
*   提供一套可复用的“代理技能”框架，支持模块化开发任务。
*   采用子代理驱动开发（Subagent-driven Development）方法，实现任务的自动化分解与执行。
*   集成完整的软件开发生命周期（SDLC）管理，涵盖从构思到交付的全过程。
*   内置智能头脑风暴工具，辅助开发者进行创意发散与技术选型。

**3. 适用场景**
*   需要高度自动化和结构化流程的大型软件项目开发。
*   希望利用AI代理（Agentic AI）优化传统SDLC流程的工程团队。
*   涉及复杂逻辑拆解，需要多步骤协作完成的技术难题攻关。

**4. 技术亮点**
*   创新性地提出了“子代理驱动开发”范式，将传统编程转化为代理技能编排。
*   虽然主要标签包含AI相关术语，但基础实现基于Shell脚本，体现了轻量级、高兼容性的工程哲学。
- 链接: https://github.com/obra/superpowers
- ⭐ 255844 | 🍴 22870 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款能够随用户共同成长的智能代理工具，旨在通过持续学习来适应用户的需求与工作流。它利用大型语言模型（LLM）技术，为用户提供高效、个性化的自动化协助。该项目在开发者社区中备受瞩目，拥有极高的关注度和活跃度。

### 2. 核心功能
*   **自适应成长机制**：能够根据用户的交互习惯和使用历史不断优化自身表现，实现“越用越聪明”。
*   **多模型兼容支持**：广泛支持包括 Anthropic (Claude)、OpenAI (ChatGPT) 等多种主流大语言模型后端。
*   **代码辅助与自动化**：深度集成编程环境，提供类似 Codex 或 Claude Code 的代码生成、调试及任务执行能力。
*   **灵活的身份配置**：支持多种代理角色设定（如 Clawdbot, Moltbot 等），以满足不同场景下的个性化需求。

### 3. 适用场景
*   **个人开发助手**：作为程序员的日常编码伴侣，自动处理繁琐的代码重构、测试编写及文档生成任务。
*   **复杂工作流自动化**：用于串联多个 API 调用或系统操作，实现跨平台任务的端到端自动化执行。
*   **交互式知识探索**：适合需要进行深度研究、信息整合且希望获得个性化反馈的用户场景。

### 4. 技术亮点
*   **生态整合度高**：标签显示其深度结合了 Nous Research 等前沿开源模型资源以及 OpenClaw 等框架，具备强大的扩展性。
*   **高社区认可度**：超过 21 万的星标数表明其在 AI Agent 领域具有标杆性的影响力和成熟的社区支持体系。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215825 | 🍴 40269 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个支持公平代码许可的工作流自动化平台，原生集成 AI 能力。它允许用户结合可视化构建与自定义代码，支持自托管或云端部署，并提供超过 400 种集成选项。

2. **核心功能**
*   提供可视化工作流编辑器，同时支持自定义代码编写以实现复杂逻辑。
*   内置原生 AI 功能，可轻松将人工智能模型整合到自动化流程中。
*   拥有超过 400 种预建集成，支持广泛的 API 和数据源连接。
*   灵活部署架构，既支持私有化自托管，也提供便捷的云服务选项。

3. **适用场景**
*   企业级数据同步与 ETL 处理，实现不同系统间的数据自动化流转。
*   利用 AI 增强客户服务，如自动回复、智能分类或内容生成工作流。
*   开发者和运维人员通过自托管方案，构建安全且定制化的内部自动化流程。
*   低代码/无代码团队快速搭建业务逻辑，减少手动操作并提高效率。

4. **技术亮点**
*   基于 TypeScript 开发，兼具类型安全与高效的执行性能。
*   作为 iPaaS（集成平台即服务）框架，具备高度的可扩展性和社区驱动特性。
*   支持 MCP（Model Context Protocol），增强了与大语言模型交互的标准兼容性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196658 | 🍴 59365 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185578 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165856 | 🍴 21452 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164275 | 🍴 30530 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157075 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151958 | 🍴 9682 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151833 | 🍴 8671 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

