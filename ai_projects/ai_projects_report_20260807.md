# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**
该项目是一套专为 AI 编码智能体设计的技能集合，兼容 Claude Code 和 Codex 等主流工具。其中包含一个名为 novel-characters 的实用技能，能够将小说内容自动转化为完整的人物设定集，涵盖角色画像、卡通形象提示词、音色描述及三视图参考。

2. **核心功能**
- 提供适配 Claude Code 和 Codex 的 AI 编码辅助技能。
- 将小说文本解析并转换为结构化的人物设定圣经（Character Bible）。
- 自动生成角色的人物画像描述与卡通形象设计提示词。
- 输出角色音色提示词及三视图（Turnaround sheets）生成指令。

3. **适用场景**
- AI 辅助编程开发，提升编码 Agent 的任务执行能力。
- 小说创作与世界观构建，快速整理人物设定资料。
- 动漫/游戏角色设计，批量生成角色视觉与听觉设定提示词。
- 内容创作者进行 IP 角色化开发时的标准化流程辅助。

4. **技术亮点**
- 跨平台兼容性好，同时支持 Anthropic 的 Claude Code 和 OpenAI 的 Codex。
- 专注垂直领域（小说角色设计），将非结构化文本转化为多模态生成的结构化提示词。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 181 | 🍴 19 | 语言: JavaScript

### goal-flow
- ### 1. 中文简介
goal-flow 是一个基于 LangGraph 的生产级框架，采用图编排的 Agent 循环架构，将工作流图与 Agent 循环相结合。它支持将 Dify DSL 转译为可执行代码，并可在 Dify 和 OpenAI 协议之间自由切换，实现灵活的 AI 工作流部署。

### 2. 核心功能
- **图编排 Agent 循环**：结合工作流图与 Agent 循环，实现复杂 AI 任务的可控执行。
- **Dify DSL 转译**：将 Dify DSL 自动转译为可运行的 Python 代码，提升开发效率。
- **协议互换支持**：支持 Dify 和 OpenAI 协议之间的无缝切换，增强兼容性。
- **生产级框架**：基于 LangGraph 构建，具备高可靠性和可扩展性。
- **人机协同（Human-in-the-Loop）**：支持人工介入流程，提升关键决策的准确性。

### 3. 适用场景
- **复杂工作流自动化**：适用于需要多步骤、多 Agent 协作的复杂业务场景。
- **Dify 迁移与扩展**：适合希望将 Dify DSL 工作流迁移到 LangGraph 环境的开发者。
- **多协议 AI 服务部署**：需要在不同 AI 平台（如 Dify、OpenAI）之间灵活切换的场景。
- **人机协同决策系统**：适用于需要人工审核或干预的 AI 工作流，如金融、医疗等领域。

### 4. 技术亮点
- **LangGraph 原生支持**：充分利用 LangGraph 的图结构能力，实现高度可定制的工作流。
- **DSL 转译引擎**：将声明式的 Dify DSL 自动转译为可执行的 Python 代码，降低开发门槛。
- **协议抽象层**：通过统一的接口抽象，实现 Dify 和 OpenAI 协议的无缝切换，提升灵活性。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- 1. **中文简介**  
这是一个针对 GPT-5.6/GPT-5.5（Codex CLI）的指令工程框架，通过 CTF 竞赛心理框架重构运行上下文，使模型的安全训练不被激活。项目强调以“让拒绝通路不发生”而非直接打压的方式绕过限制，支持一键部署，仅需 62 行提示词和 50 个技能模块，且纯 Python 无外部依赖。

2. **核心功能**  
- 基于 CTF 竞赛心理框架重构模型运行上下文，抑制安全拒绝机制。  
- 提供 62 行精简提示词和 50 个可复用技能模块，实现快速指令定制。  
- 纯 Python 实现，零外部依赖，支持一键部署。  
- 聚焦“规避拒绝通路”而非对抗性压制，提升模型在受限场景下的响应率。

3. **适用场景**  
- 在 Codex CLI 环境中进行高强度指令工程实验或红队测试。  
- 需要绕过默认安全过滤以获取更自由输出的研究或开发场景。  
- 希望用轻量级、无依赖方式快速部署定制化 AI 交互框架的开发者。

4. **技术亮点**  
- 创新性地引入 CTF 竞赛心理模型重构上下文，从认知层面抑制拒绝触发，而非硬编码绕过。  
- 极简架构：62 行核心提示词 + 50 模块技能库，纯 Python 无依赖，部署成本低。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 56 | 🍴 13 | 语言: Python

### lattice-script-executor
- 1. **中文简介**
lattice-script-executor 是一款跨平台软件授权工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能，为软件保护提供全方位解决方案。

2. **核心功能**
- 跨平台支持：兼容 Windows、macOS 和 Linux 操作系统。
- AI 规则引擎：利用人工智能技术实现智能授权规则判断。
- 离线种子验证：支持无需网络连接即可验证软件授权的有效性。
- 批量密钥生成：提供高效的产品密钥批量生成能力。
- 审计日志：记录所有授权操作，确保日志不可篡改且可追溯。

3. **适用场景**
- 商业软件分发与版权保护。
- 企业级软件授权管理。
- 需要离线验证的软件部署场景。
- 对授权操作有审计追溯要求的行业。

4. **技术亮点**
- 采用 AI 驱动的智能规则引擎，提升授权验证的灵活性和安全性。
- 离线种子验证机制，确保在无网络环境下仍能可靠验证授权。
- 不可篡改的审计日志设计，满足合规性要求并提供完整操作追溯能力。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- ### 1. 中文简介
由于项目描述为空（None），无法提供具体简介。建议查看项目仓库的 README 文件或源代码以获取详细信息。

### 2. 核心功能
- 信息不足，无法确定核心功能。
- 建议访问 GitHub 仓库页面查看代码结构或文档。

### 3. 适用场景
- 暂无明确适用场景信息。
- 需进一步分析项目内容后才能判断。

### 4. 技术亮点
- 无可用技术亮点信息。

---

**备注**：该项目目前缺乏公开描述和技术细节，建议直接查看 [GitHub 仓库](https://github.com/0xsimao-ai) 或联系项目维护者获取更多信息。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 34 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 30 | 🍴 3 | 语言: 未知

### ai-novel-screenplay-analyzer
- 描述: 面向长篇小说、剧本与改编项目的 AI 叙事分析工作台，自动梳理人物关系、章节脉络与关系演化，支持多模型接入、任务断点恢复及本地私有部署。
- 链接: https://github.com/ops120/ai-novel-screenplay-analyzer
- ⭐ 24 | 🍴 1 | 语言: JavaScript

### daily-global-market-intelligence-description-skills
- 描述: 提供每日股市新闻、财经早餐、盘前/盘后复盘、美股、A股、港股、韩股、全球市场走势、宏观经济、AI板块、半导体、资金流向、市场情绪、财报、ETF、行业轮动、大宗商品、加密货币等内容时触发。提供机构级全球市场日报
- 链接: https://github.com/morangse/daily-global-market-intelligence-description-skills
- ⭐ 22 | 🍴 0 | 语言: 未知

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 21 | 🍴 2 | 语言: 未知

### AI-Photographer-Agent-ROCm
- 描述: Private local AI Photographer Agent on AMD Radeon and ROCm
- 链接: https://github.com/yang13926151198-ai/AI-Photographer-Agent-ROCm
- ⭐ 21 | 🍴 0 | 语言: Python
- 标签: ai-agent, amd-rocm, multimodal-ai, photography, qwen2-vl

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个功能全面的中文自然语言处理工具包，提供敏感词检测、语言检测、实体抽取（手机号、身份证、邮箱等）及繁简转换等基础 NLP 功能。该项目还收录了丰富的中文词库（如人名、地名、成语、行业术语）及预训练语言模型资源，并集成了语音识别、知识图谱构建及对话系统等进阶应用资源。

2. **核心功能**
- 提供中英文敏感词过滤、语言检测、手机/电话归属地查询及名字性别推断等实用工具。
- 包含海量中文资源库，涵盖人名、地名、成语、古诗词、行业术语及停用词等。
- 集成多种 NLP 任务解决方案，如命名实体识别、关键词抽取、文本摘要及情感分析。
- 收录了基于 BERT、GPT 等模型的预训练资源及中文 OCR、语音识别（ASR）相关工具。
- 提供知识图谱构建、问答系统及对话机器人相关的开源项目与数据集汇总。

3. **适用场景**
- **内容安全审核**：用于互联网平台的中英文敏感词检测、暴恐词过滤及谣言识别。
- **信息抽取与清洗**：从非结构化文本中自动抽取手机号、身份证、邮箱、地址等关键实体。
- **NLP 模型研发**：为开发者提供丰富的中文词向量、语料库及预训练模型，加速模型训练。
- **智能客服与问答**：基于开源的对话系统和知识图谱资源，快速搭建垂直领域问答机器人。

4. **技术亮点**
- **资源聚合全面**：不仅包含基础工具，还汇总了清华大学、百度、Facebook 等机构的高质量数据集和预训练模型。
- **领域覆盖广泛**：涵盖医疗、金融、法律、汽车等多个垂直领域的专业词库和 NLP 任务资源。
- **紧跟前沿技术**：集成了 BERT、ALBERT、GPT-2 等最新预训练语言模型在中文 NLP 中的应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
这是一个收录了500个AI项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实践案例，适合学习与应用AI技术。

2. **核心功能**  
- 提供大量AI相关项目的代码实现，便于学习和参考。  
- 覆盖机器学习、深度学习、计算机视觉及NLP等多个领域。  
- 所有项目均附带代码，方便直接运行和实验。  
- 适合初学者到高级开发者使用，提升实际动手能力。  
- 项目分类清晰，便于快速找到感兴趣的方向。

3. **适用场景**  
- AI初学者希望通过实际项目快速掌握技术。  
- 开发者寻找灵感以完成自己的AI项目。  
- 教育者用于教学或课程实践环节。  
- 企业团队进行技术调研或原型开发。

4. **技术亮点**  
- 项目数量庞大，涵盖主流AI方向。  
- 代码开源且易于复现，降低学习门槛。  
- 标签分类完善，便于检索与筛选。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看模型结构和参数。

**2. 核心功能**
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供图形化界面，清晰展示网络层结构和数据流向。
- 支持查看模型参数和权重信息，便于调试和分析。
- 兼容桌面应用和在线浏览器版本，使用便捷。
- 支持 safetensors 等新兴安全模型格式。

**3. 适用场景**
- 深度学习研究者快速理解复杂模型架构。
- 工程师在不同框架间迁移模型时验证结构一致性。
- 教学演示中直观展示神经网络工作原理。
- 调试模型时检查层连接错误或参数异常。

**4. 技术亮点**
- 高度兼容主流 AI 框架，无需额外转换即可直接打开模型文件。
- 开源免费，社区活跃，持续更新支持最新模型格式。
- 界面简洁直观，无需编程基础即可上手使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型交换与运行。它允许开发者在PyTorch、TensorFlow、scikit-learn等框架间无缝迁移模型，提升开发效率与部署灵活性。

2. **核心功能**
- 提供统一的模型表示格式，支持跨框架模型转换与互操作。
- 兼容主流深度学习框架，包括PyTorch、TensorFlow、Keras和scikit-learn。
- 支持模型优化与性能调优，适配多种硬件后端。
- 提供丰富的算子库，覆盖常见的神经网络层与操作。
- 支持模型验证与调试，确保转换后模型的正确性。

3. **适用场景**
- 在不同深度学习框架间迁移模型，如从PyTorch转为TensorFlow。
- 将训练好的模型部署到边缘设备或生产环境，利用ONNX Runtime优化性能。
- 跨团队协作开发，统一模型格式以简化共享与集成流程。
- 研究实验与原型开发，快速验证模型在不同框架下的表现。

4. **技术亮点**
- 开源社区活跃，由Linux基金会支持，确保标准的长期发展与广泛采用。
- 与主流硬件厂商（如NVIDIA、Intel）合作，提供高效的运行时优化。
- 支持动态形状与复杂控制流，适应多样化的模型结构需求。
- 链接: https://github.com/onnx/onnx
- ⭐ 21277 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面覆盖机器学习工程实践的资源指南。内容涵盖从模型训练、调试到推理部署的全流程，重点聚焦于大规模语言模型（LLM）和分布式训练工程。

2. **核心功能**
- 提供大规模LLM训练、微调和推理的详细工程实践指导。
- 深入讲解PyTorch分布式训练、GPU优化及Slurm集群管理。
- 涵盖MLOps全流程，包括存储、网络、可扩展性及调试技巧。
- 开源共享，作为社区驱动的机器学习工程参考手册。

3. **适用场景**
- 工程师构建和优化大规模语言模型（LLM）训练流水线。
- 团队在GPU集群上进行分布式训练和推理部署时排查性能瓶颈。
- 学习MLOps最佳实践，提升机器学习系统的可扩展性与稳定性。

4. **技术亮点**
- 内容紧跟前沿，覆盖Transformer架构、推理优化及GPU硬件级调优。
- 高度实用，提供可落地的调试技巧与生产环境配置方案。
- 社区活跃，星标数超1.8万，反映其在ML工程领域的广泛认可。
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
这是一个收录了500个AI项目的代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实践案例，适合学习与应用AI技术。

2. **核心功能**  
- 提供大量AI相关项目的代码实现，便于学习和参考。  
- 覆盖机器学习、深度学习、计算机视觉及NLP等多个领域。  
- 所有项目均附带代码，方便直接运行和实验。  
- 适合初学者到高级开发者使用，提升实际动手能力。  
- 项目分类清晰，便于快速找到感兴趣的方向。

3. **适用场景**  
- AI初学者希望通过实际项目快速掌握技术。  
- 开发者寻找灵感以完成自己的AI项目。  
- 教育者用于教学或课程实践环节。  
- 企业团队进行技术调研或原型开发。

4. **技术亮点**  
- 项目数量庞大，涵盖主流AI方向。  
- 代码开源且易于复现，降低学习门槛。  
- 标签分类完善，便于检索与筛选。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36027 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看模型结构和参数。

**2. 核心功能**
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等。
- 提供图形化界面，清晰展示网络层结构和数据流向。
- 支持查看模型参数和权重信息，便于调试和分析。
- 兼容桌面应用和在线浏览器版本，使用便捷。
- 支持 safetensors 等新兴安全模型格式。

**3. 适用场景**
- 深度学习研究者快速理解复杂模型架构。
- 工程师在不同框架间迁移模型时验证结构一致性。
- 教学演示中直观展示神经网络工作原理。
- 调试模型时检查层连接错误或参数异常。

**4. 技术亮点**
- 高度兼容主流 AI 框架，无需额外转换即可直接打开模型文件。
- 开源免费，社区活跃，持续更新支持最新模型格式。
- 界面简洁直观，无需编程基础即可上手使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
   这是一个专为深度学习与机器学习研究者精心整理的必备速查手册集合。项目涵盖了从基础库到高级框架的核心概念与实用代码示例，是研究人员快速查阅知识点的理想资源。

2. **核心功能**
   - 提供机器学习与深度学习领域的核心概念速查表，便于快速回顾关键知识。
   - 涵盖 Numpy、Scipy、Matplotlib 等基础数值计算与可视化工具的常用语法。
   - 包含 Keras 等主流深度学习框架的使用指南和代码片段。
   - 整合了数学基础、算法原理及模型调优的实用技巧。
   - 以简洁清晰的格式呈现，适合打印或在线快速检索。

3. **适用场景**
   - 研究人员在进行算法实验时，快速查阅数学公式或函数用法。
   - 初学者系统学习机器学习时，作为知识点的汇总参考手册。
   - 工程师在实际开发中，需要快速回忆特定库（如 NumPy）的高效操作技巧。
   - 准备技术面试或复习核心概念时，作为高效的备忘清单使用。

4. **技术亮点**
   - 内容全面且结构化，将分散的知识点整合为便于查阅的速查形式。
   - 聚焦于研究者和工程师日常最常用的工具链，实用性强。
   - 由社区广泛认可（高星标数），内容经过大量用户验证，质量可靠。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- **1. 中文简介**
Ai-Learn 是一个全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费配套教材，帮助零基础用户入门并提升就业实战能力。内容涵盖 Python、数学、机器学习、深度学习、计算机视觉（CV）及自然语言处理（NLP）等热门技术领域。

**2. 核心功能**
- 提供系统化的 AI 学习路径，从零基础到就业实战全覆盖。
- 收录近 200 个实战案例与项目，配套免费教材资源。
- 涵盖主流框架与工具，包括 PyTorch、TensorFlow、Keras、Caffe 等。
- 整合数据处理与可视化技能，涉及 NumPy、Pandas、Matplotlib、Seaborn 等库。

**3. 适用场景**
- 初学者系统学习人工智能与机器学习基础理论及实践。
- 希望掌握 Python 数据分析与挖掘技能的数据科学从业者。
- 准备进入 AI 领域的求职者，通过实战项目提升竞争力。
- 需要参考 CV、NLP 等特定方向学习资源的技术人员。

**4. 技术亮点**
- 资源高度集成：将算法、数学、编程框架及热门领域（CV/NLP）整合于单一路线图。
- 实战导向：强调“就业实战”，通过大量案例将理论转化为动手能力。
- 社区认可度高：拥有 13234 个星标，表明其内容质量与学习价值受到广泛认可。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13234 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络和其他 AI 模型。它通过简化模型开发流程，让开发者能够更快速地设计和训练深度学习模型，无需编写大量底层代码。

### 2. 核心功能
- **低代码开发**：通过声明式配置即可定义和训练模型，降低开发门槛
- **多模型支持**：支持构建 LLM、神经网络及各类 AI 模型
- **微调能力**：提供对 LLaMA、Mistral 等主流大模型的微调功能
- **深度学习集成**：基于 PyTorch 构建，兼容主流深度学习生态
- **数据中心方法**：强调数据驱动的训练流程优化

### 3. 适用场景
- **企业级 AI 应用开发**：快速构建定制化机器学习模型
- **大模型微调**：对 LLaMA、Mistral 等开源 LLM 进行领域适配
- **计算机视觉项目**：开发图像识别、目标检测等视觉模型
- **自然语言处理**：构建文本分类、情感分析等 NLP 应用

### 4. 技术亮点
- 采用声明式 YAML/JSON 配置，实现模型定义与代码解耦
- 内置数据管道和预处理功能，支持端到端训练流程
- 提供可视化训练监控和实验管理工具
- 兼容 Hugging Face 生态，无缝集成主流预训练模型
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
funNLP 是一个功能全面的中文自然语言处理工具包，提供敏感词检测、语言检测、实体抽取（手机号、身份证、邮箱等）及繁简转换等基础 NLP 功能。该项目还收录了丰富的中文词库（如人名、地名、成语、行业术语）及预训练语言模型资源，并集成了语音识别、知识图谱构建及对话系统等进阶应用资源。

2. **核心功能**
- 提供中英文敏感词过滤、语言检测、手机/电话归属地查询及名字性别推断等实用工具。
- 包含海量中文资源库，涵盖人名、地名、成语、古诗词、行业术语及停用词等。
- 集成多种 NLP 任务解决方案，如命名实体识别、关键词抽取、文本摘要及情感分析。
- 收录了基于 BERT、GPT 等模型的预训练资源及中文 OCR、语音识别（ASR）相关工具。
- 提供知识图谱构建、问答系统及对话机器人相关的开源项目与数据集汇总。

3. **适用场景**
- **内容安全审核**：用于互联网平台的中英文敏感词检测、暴恐词过滤及谣言识别。
- **信息抽取与清洗**：从非结构化文本中自动抽取手机号、身份证、邮箱、地址等关键实体。
- **NLP 模型研发**：为开发者提供丰富的中文词向量、语料库及预训练模型，加速模型训练。
- **智能客服与问答**：基于开源的对话系统和知识图谱资源，快速搭建垂直领域问答机器人。

4. **技术亮点**
- **资源聚合全面**：不仅包含基础工具，还汇总了清华大学、百度、Facebook 等机构的高质量数据集和预训练模型。
- **领域覆盖广泛**：涵盖医疗、金融、法律、汽车等多个垂直领域的专业词库和 NLP 任务资源。
- **紧跟前沿技术**：集成了 BERT、ALBERT、GPT-2 等最新预训练语言模型在中文 NLP 中的应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持100多种模型。该项目已入选ACL 2024会议，旨在简化大模型的微调流程。

2. **核心功能**
- 支持100多种主流LLM和VLM的统一高效微调。
- 集成多种微调技术，包括LoRA、QLoRA、全参数微调及P-Tuning等。
- 提供直观的Web UI界面和命令行工具，降低使用门槛。
- 支持RLHF（基于人类反馈的强化学习）和DPO等对齐训练方法。
- 兼容Transformers、PEFT等主流深度学习库。

3. **适用场景**
- 开发者希望快速微调Llama、Qwen、DeepSeek、Gemma等主流大模型。
- 研究人员需要对比不同微调策略（如LoRA vs QLoRA）的效果。
- 企业团队希望部署低成本、高效率的私有化大模型服务。
- 用户需要通过可视化界面轻松管理模型训练任务。

4. **技术亮点**
- **统一架构**：一个框架支持百种模型，避免重复适配不同模型代码。
- **高效优化**：内置QLoRA和量化技术，显著降低显存需求，支持在消费级显卡上微调大模型。
- **多模态支持**：不仅支持文本模型，还兼容视觉语言模型（VLM）的微调。
- **学术认可**：作为ACL 2024入选项目，具备较强的学术背书和技术严谨性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73898 | 🍴 9042 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. **中文简介**
AI-For-Beginners 是一个为期12周、包含24节课的人工智能入门课程，由微软开发者社区支持。该项目旨在为所有人提供通俗易懂的AI学习资源，覆盖机器学习、深度学习和自然语言处理等核心主题。

### 2. **核心功能**
- 提供系统化的12周学习计划，帮助初学者逐步掌握AI基础知识。
- 使用Jupyter Notebook作为主要工具，支持交互式编程学习。
- 内容涵盖机器学习、卷积神经网络（CNN）、生成对抗网络（GAN）和循环神经网络（RNN）等广泛主题。
- 免费开放，适合全球学习者参与。
- 结合理论与实践，通过示例代码和练习巩固知识。

### 3. **适用场景**
- 对人工智能感兴趣的初学者，希望从零开始学习AI基础。
- 教育工作者或培训师，需要结构化课程来教授AI相关内容。
- 企业团队，用于内部AI技能培训和知识普及。
- 自学者，希望通过实践项目提升AI开发能力。

### 4. **技术亮点**
- 采用微软开发者社区的权威资源，确保内容质量。
- 强调实践性，通过Jupyter Notebook实现“边学边做”的学习模式。
- 涵盖AI领域的多个热门方向，如计算机视觉和自然语言处理，满足多样化学习需求。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63112 | 🍴 12243 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**
掌握原理，从零构建，并交付给他人使用。这是一个全面的AI工程学习项目，涵盖从基础理论到实际部署的完整流程。

2. **核心功能**
- 提供从零开始构建AI系统和智能体的完整教程
- 涵盖大语言模型、计算机视觉、强化学习等核心技术
- 支持多种编程语言实现，包括Python、Rust和TypeScript
- 整合MCP（模型上下文协议）和群体智能等前沿技术
- 注重实践应用，强调将AI工程能力转化为可交付成果

3. **适用场景**
- AI工程师系统学习深度学习与生成式AI技术
- 开发者构建自定义AI智能体和多智能体系统
- 研究人员探索强化学习和群体智能算法
- 团队需要从零搭建AI工程能力的技术培训

4. **技术亮点**
- 跨语言支持（Python/Rust/TypeScript）体现工程实践多样性
- 整合MCP协议和智能体编排，紧跟AI工程前沿
- 强调"从原理到部署"的端到端学习路径
- 高星标数（46209）证明社区认可度和实用性
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46209 | 🍴 7994 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch 及 TensorFlow 2 的综合学习项目。该项目还深入讲解自然语言处理（NLTK），旨在为学习者提供从理论到实践的完整技术栈支持。

**核心功能**
1. 涵盖经典机器学习算法（如 SVM、KMeans、AdaBoost、朴素贝叶斯）的实战实现。
2. 提供深度学习框架（PyTorch、TensorFlow 2）及神经网络模型（RNN、LSTM、DNN）的代码示例。
3. 集成自然语言处理（NLP）库 NLTK 进行文本分析与处理。
4. 包含推荐系统、关联规则挖掘（Apriori、FP-Growth）及降维技术（PCA、SVD）等进阶内容。
5. 补充线性代数等数学基础，夯实机器学习理论根基。

**适用场景**
1. 机器学习初学者系统学习从基础数学到高级算法的完整知识体系。
2. 需要快速查阅和复现经典 ML/DL 算法代码的数据科学家或工程师。
3. 希望深入理解 NLP 及推荐系统原理并动手实践的研究人员。
4. 准备技术面试，需要梳理算法原理与代码实现的求职者。

**技术亮点**
项目将数学基础（线性代数）、传统机器学习、深度学习框架及 NLP 整合于单一仓库，提供了从理论推导到代码落地的端到端学习资源，适合系统化进阶。
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
- ⭐ 33810 | 🍴 4705 | 语言: Python
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
- ⭐ 385466 | 🍴 81024 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268662 | 🍴 23995 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227020 | 🍴 44371 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199716 | 🍴 59992 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186263 | 🍴 46058 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166857 | 🍴 21539 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164435 | 🍴 30560 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162809 | 🍴 9167 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157607 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152924 | 🍴 9826 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

