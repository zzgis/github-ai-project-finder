# GitHub AI项目每日发现报告
日期: 2026-06-26

## 新发布的AI项目

### theeleven
- ### 1. 中文简介
该项目包含11个自主AI智能体，运行在X Layer网络上，专门用于开启实时足球博彩市场。它采用了自定义的Uniswap V4 Hook机制，并支持免Gas费的USDT0质押功能，旨在优化去中心化预测市场的交易体验。

### 2. 核心功能
*   **自主AI驱动**：部署了11个独立的AI智能体，自动监控和开启足球赛事的预测市场。
*   **Uniswap V4集成**：利用自定义Hook深度集成Uniswap V4协议，实现灵活的市场流动性管理。
*   **Gasless体验**：基于EIP-3009标准，支持免Gas费（Gasless）的USDT0质押与交易操作。
*   **实时预测市场**：专注于足球（Football Prop）领域的实时赔率生成与市场开放。

### 3. 适用场景
*   **Web3体育博彩平台**：开发者可利用其框架搭建去中心化的体育赛事预测交易市场。
*   **AI Agent研究与应用**：适合研究多智能体协作及自动化执行DeFi操作的场景。
*   **新型DEX实验**：测试人员可使用该代码库探索Uniswap V4 Hook的高级应用场景。

### 4. 技术亮点
*   **前沿协议组合**：同时应用了Uniswap V4、EIP-3009（授权转账）和ERC-8257（可升级合约），展示了极高的技术整合能力。
*   **跨链优化**：针对X Layer网络进行优化，结合Next.js前端与Solidity后端，提供了全栈式的去中心化应用解决方案。
- 链接: https://github.com/winsznx/theeleven
- ⭐ 440 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, defi, eip-3009, erc-8257, football

### video-production-skills
- ### 1. 中文简介
这是一个可复用的AI视频制作技能库，旨在简化视频内容的创建、重制及动态设计流程。该工具集涵盖了从开场动画制作到质量把控（QA）的全链路视频生产需求。

### 2. 核心功能
*   支持利用AI自动化生成和重新创作视频内容。
*   提供动态图形设计（Motion Design）相关的处理能力。
*   内置开场动画（Openers）的制作与集成技能。
*   包含视频质量分析（QA）功能，确保输出标准。
*   模块化设计使得各项技能可在不同项目中复用。

### 3. 适用场景
*   需要快速批量生产带有统一开场动画的营销视频。
*   对现有视频素材进行动态化重制或风格迁移。
*   自动化视频后期质检，减少人工审核成本。
*   构建标准化的AI驱动视频工作流平台。

### 4. 技术亮点
*   采用Python语言开发，便于集成到现有的AI或数据处理管道中。
*   模块化“技能”架构，提高了代码的可复用性和维护性。
- 链接: https://github.com/Pluviobyte/video-production-skills
- ⭐ 190 | 🍴 17 | 语言: Python

### GITVERSE
- ### 1. **中文简介**
GITVERSE 是一个能够将任意代码库逆向工程化为构建提示的工具，它通过解析代码生成架构分解、ASCII 蓝图以及供 AI 直接使用的重构提示。该项目旨在简化大型代码库的分析过程，帮助开发者快速理解系统结构并生成标准化的 AI 指令。

### 2. **核心功能**
*   **代码逆向工程**：自动分析代码库结构，将其转化为机器可读的构建提示。
*   **架构可视化**：生成清晰的架构分解图和 ASCII 风格的蓝图，直观展示系统组成。
*   **AI 就绪输出**：创建经过优化的提示词（Prompt），可直接用于 Claude、Cursor 等 AI 工具进行代码重构或分析。
*   **多模型支持**：兼容 OpenAI 和 Claude 等大语言模型，适应不同的 AI 工作流需求。
*   **GitHub API 集成**：利用 GitHub API 高效获取和解析远程仓库的代码数据。

### 3. **适用场景**
*   **接手遗留项目**：在缺乏文档的情况下，快速理清复杂或老旧代码库的整体架构。
*   **AI 辅助重构**：为 Cursor、Claude 等 AI 编码助手提供精确的上下文提示，以提高代码修改和重构的准确性。
*   **技术分享与文档化**：为团队会议或新人入职生成可视化的代码库结构图，降低沟通成本。
*   **安全审计与合规检查**：通过分析代码依赖和结构，快速识别潜在的安全风险或架构缺陷。

### 4. **技术亮点**
*   基于 TypeScript 和 Next.js 构建，具备现代化的开发体验和良好的性能表现。
*   结合 TailwindCSS 实现简洁美观的用户界面，提升用户体验。
*   专注于“提示工程”（Prompt Engineering），将复杂的代码分析转化为标准化的 AI 输入格式。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 131 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### Anti-Autoresearch
- ### GitHub 项目分析报告：Anti-Autoresearch

**1. 中文简介**
不要盲目信任自动生成的论文，本项目旨在通过审查者视角进行完整性取证，结合自洽性检查与针对 39 种黑客模式（涵盖 7 大类）的伪造检测，给出确定性的判决结果。它并非用于检测 AI 文本内容，而是作为 ARIS 项目的对立面或补充工具，专注于识别由自动化研究流程产生的潜在问题。

**2. 核心功能**
*   **多模式伪造检测**：覆盖 7 大类别的 39 种典型“黑客”模式，以识别潜在的学术不端行为。
*   **自洽性验证**：检查论文内部逻辑的一致性，确保论点、数据和方法论没有矛盾。
*   **确定性判决输出**：提供明确的二元判断结果，而非模糊的概率评分。
*   **非内容型 AI 检测**：明确区分于传统的 AI 文本检测器，专注于研究流程和结构层面的异常。
*   **审查者辅助工具**：为同行评审专家提供自动化取证支持，减轻人工审核压力。

**3. 适用场景**
*   **同行评审辅助**：期刊或会议审稿人利用该工具快速筛查可疑的自动生成论文。
*   **学术诚信调查**：高校或研究机构在发现疑似学术造假时，进行初步的技术取证分析。
*   **AI 研究人员评估**：研究人员在开发 LLM Agent（智能体）生成论文的能力时，用于评估其输出的可靠性和合规性。
*   **预印本过滤**：在 arXiv 等预印本平台发布前，对提交的稿件进行自动化的一致性校验。

**4. 技术亮点**
*   **结构化取证框架**：将复杂的学术不端行为拆解为 39 种具体的、可计算的模式规则。
*   **确定性算法逻辑**：采用确定性的逻辑判断而非基于概率的机器学习分类，提高了判决的可解释性和稳定性。
*   **领域特异性设计**：专门针对“自动研究”（Autoresearch）流程中的漏洞进行优化，而非通用的文本风格检测。
- 链接: https://github.com/wanshuiyin/Anti-Autoresearch
- ⭐ 35 | 🍴 1 | 语言: Python
- 标签: ai-generated-content, ai-scientist, autoresearch, forensics, llm-agents

### macos-chatgpt-overlay-bar
- 1. **中文简介**
这是一款专为 macOS 设计的 ChatGPT 桌面应用，其界面常驻于系统菜单栏中。它旨在让用户无需切换窗口即可快速访问 ChatGPT 服务，实现便捷的 AI 交互体验。

2. **核心功能**
- 提供常驻菜单栏的快速入口，方便用户随时唤起 ChatGPT。
- 支持在 macOS 系统中进行轻量级的 AI 对话与内容生成。
- 简化了访问流程，避免了在不同应用程序间频繁切换的麻烦。

3. **适用场景**
- 需要在日常工作中快速查询信息或生成简短文本的用户。
- 偏好极简桌面环境，希望减少应用窗口干扰的 macOS 用户。
- 需要随时记录灵感或进行碎片化 AI 交互的自由职业者。

4. **技术亮点**
该项目基于非传统编程语言（标记为 None），主要体现为原生 macOS 菜单栏应用开发，专注于系统集成与用户体验优化，而非复杂的底层算法创新。
- 链接: https://github.com/ik190/macos-chatgpt-overlay-bar
- ⭐ 31 | 🍴 3 | 语言: 未知
- 标签: ai, chatgpt, chatgpt-bar-mac, chatgpt-menubar-mac, chatgpt-quick-access-mac

### auto-paper-collecter
- 描述: 📚🔭 Your personal research radar — an LLM-powered tool that auto-aggregates the latest papers for your keywords across arXiv / Crossref / Semantic Scholar / GitHub / RSS.
- 链接: https://github.com/PenghaoJiang/auto-paper-collecter
- ⭐ 31 | 🍴 1 | 语言: Python
- 标签: academic, agent-skill, ai, arxiv, claude-code

### deepseek-v4-pro-flash-desktop-app
- 描述: deepseek-v4-pro-flash deepseek ai large language model llm mixture of experts moe 1m context window hybrid attention architecture compressed sparse attention csa heavily compressed attention hca manifold constrained hyper deepseek-v4-pro deepseek-v4-flash open source hugging face github repository api access local llm inference vllm ollama
- 链接: https://github.com/HiyuCat/deepseek-v4-pro-flash-desktop-app
- ⭐ 29 | 🍴 0 | 语言: TypeScript
- 标签: ai-free, deep-seek, deepseek-api, deepseek-app, deepseek-chat

### parsehawk
- 描述: Local-first document AI. Run 100% locally by default, with API, CLI, and Web UI.
- 链接: https://github.com/parsehawk/parsehawk
- ⭐ 26 | 🍴 4 | 语言: Python
- 标签: artificial-intelligence, classification, document-ai, document-processing, extraction

### ai-coding-deals
- 描述: Money-saving guide to AI coding tools: free tiers, discounts, referral credits & open-source alternatives. 省钱指南。
- 链接: https://github.com/codertesla/ai-coding-deals
- ⭐ 25 | 🍴 0 | 语言: Python
- 标签: ai, ai-coding, ai-tools, awesome-list, claude-code

### Tidal_Echo
- 描述: 一个**私密 1:1 聊天通道**：把「你手机上的 PWA」和「你电脑上跑的 AI 伴侣」连起来。 AI 侧以 **Claude Code 的 channel 插件**形态运行——你在手机上发消息，Claude Code 会话里就冒出 `<channel>` 块；AI 调一个 `reply` 工具，你手机就收到气泡。
- 链接: https://github.com/anhe2021212-spec/Tidal_Echo
- ⭐ 24 | 🍴 11 | 语言: HTML

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个综合性的自然语言处理（NLP）资源库，涵盖了从基础的数据清洗、词典构建到前沿的深度学习和预训练模型等多种工具与数据集。它旨在为开发者提供丰富的中文NLP资源，包括敏感词检测、实体抽取、情感分析及各类垂直领域的知识图谱和语料库。

2. **核心功能**
*   提供全面的中文NLP基础工具，如分词、词性标注、命名实体识别及繁简转换。
*   集成大量垂直领域数据与模型，涵盖医疗、金融、法律、汽车及古诗词等专业知识。
*   收录多种主流预训练语言模型（如BERT、GPT-2、ALBERT等）及其微调代码和应用实例。
*   包含语音识别、文本生成、问答系统及知识图谱构建等高级NLP任务的相关资源。
*   提供数据增强、可视化、标注工具及多语言处理库，辅助NLP全流程开发。

3. **适用场景**
*   需要快速构建中文文本分析流程（如敏感词过滤、实体抽取）的开发人员。
*   致力于垂直领域（如医疗、金融）知识图谱构建或智能问答系统研发的工程师。
*   寻找高质量中文语料、预训练模型或进行NLP算法研究与实验的科研人员。
*   希望了解NLP前沿技术动态，参考最新竞赛方案及开源工具链的学习者。

4. **技术亮点**
资源覆盖极广，不仅包含传统NLP任务，还整合了基于Transformer架构的最新预训练模型及多模态（语音/图像）处理工具。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI相关项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并附带完整代码实现。该项目旨在为开发者提供一个全面且实用的AI学习与实践指南，帮助快速掌握核心技术。通过整合多个子项目，它成为了解当前AI技术栈和落地应用的优秀参考集合。

2. **核心功能**
*   提供大量现成的机器学习与深度学习项目代码，支持直接运行和参考。
*   覆盖计算机视觉与自然语言处理两大主流AI应用方向，内容广泛。
*   作为“Awesome”列表，系统性地整理和分类了高质量的AI开源项目。
*   主要基于Python语言开发，符合数据科学和AI领域的主流技术栈。

3. **适用场景**
*   AI初学者希望寻找带有代码示例的项目来快速入门和练习。
*   研究人员或工程师需要参考具体的计算机视觉或NLP实现方案。
*   开发者在构建AI应用时，寻找灵感或复用现有的成熟代码模块。
*   企业团队进行技术选型时，评估当前主流AI项目和工具的流行度。

4. **技术亮点**
*   **规模庞大**：收录高达500个项目，覆盖面极广，是大型资源索引库。
*   **高关注度**：拥有超过34,000个星标，证明了其在社区中的高认可度和实用性。
*   **标签体系完善**：通过细粒度的标签（如artificial-intelligence-projects, nlp-projects等）便于用户精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7294 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。该项目由 JavaScript 驱动，具有轻量级且跨平台的特点。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、PyTorch、TensorFlow、Keras 和 CoreML 等。
*   提供清晰的图形化界面，直观展示神经网络的层级结构与数据流向。
*   具备模型检查与诊断功能，可识别并高亮显示模型中的潜在错误或冗余节点。
*   支持导出模型结构的静态图片或矢量图，便于文档编写与技术分享。
*   兼容桌面端应用、Web 浏览器及命令行接口，实现多环境无缝访问。

3. **适用场景**
*   在部署模型前，快速验证复杂神经网络的结构是否正确无误。
*   调试深度学习模型时，通过可视化节点排查梯度消失或连接错误等问题。
*   撰写技术报告或论文时，生成高质量、标准化的模型架构图表。
*   非开发人员或学生通过直观视图理解不同算法框架（如 TensorFlow 与 PyTorch）的实现差异。

4. **技术亮点**
*   **广泛的兼容性**：几乎涵盖所有主流 AI 框架的模型格式，无需转换即可直接查看。
*   **零依赖运行**：基于 Electron 构建的桌面版和纯 Web 版，用户无需配置复杂的 Python 环境即可使用。
*   **交互式体验**：允许用户点击节点查看详细参数、权重维度及运算逻辑，提升调试效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33139 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是机器学习领域的开放标准，旨在促进不同框架间的模型互操作性。它允许开发者在不同平台间无缝迁移和部署经过训练的模型，简化了从训练到推理的工作流。

2. **核心功能**
*   **跨框架兼容**：支持 PyTorch、TensorFlow、Keras 等主流深度学习框架与 ONNX 之间的模型转换。
*   **统一模型表示**：提供标准化的模型定义格式，确保模型结构、参数和算子在异构环境中保持一致。
*   **高效推理部署**：通过与 ONNX Runtime 等执行引擎配合，实现跨 CPU、GPU 和边缘设备的加速推理。
*   **生态系统集成**：广泛集成于 scikit-learn 等机器学习工具链，降低模型部署的技术门槛。

3. **适用场景**
*   **模型迁移与部署**：在开发阶段使用 PyTorch 或 TensorFlow 训练模型，随后转换为 ONNX 格式以部署到生产环境或移动设备。
*   **硬件加速优化**：利用 ONNX 转换器针对特定硬件（如 NVIDIA GPU、Intel CPU）进行算子优化，提升推理性能。
*   **多框架协作开发**：在团队中混合使用不同深度学习框架时，通过 ONNX 作为中间格式统一模型交换标准。

4. **技术亮点**
*   **开源标准化**：由 Microsoft、Facebook 等巨头共同维护，已成为工业界事实上的模型交换标准。
*   **运行时灵活性**：配套的 ONNX Runtime 提供高性能执行环境，支持动态形状处理和广泛的硬件后端。
- 链接: https://github.com/onnx/onnx
- ⭐ 21051 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. **中文简介**
《Machine Learning Engineering Open Book》是一本关于机器学习工程领域的开源指南。它系统性地涵盖了从硬件基础设施到大规模模型训练、推理及调试的全栈工程技术。该项目旨在为构建和部署高性能机器学习系统提供实用的最佳实践。

### 2. **核心功能**
*   **基础设施管理**：深入解析GPU集群、网络存储及Slurm调度系统的配置与优化。
*   **大模型训练与调试**：提供处理大型语言模型（LLM）时的高效训练策略及故障排查技巧。
*   **推理优化**：详解模型推断阶段的加速方法、量化技术及服务化部署流程。
*   **可扩展性架构**：指导如何设计支持海量数据和高并发请求的ML工程系统。
*   **PyTorch生态集成**：结合Transformers库等主流工具链，展示工业级代码实现规范。

### 3. **适用场景**
*   **大规模LLM研发**：适用于需要从零搭建或优化数十亿参数模型训练环境的算法工程师。
*   **MLOps系统建设**：适合希望建立标准化、自动化机器学习流水线及监控体系的技术团队。
*   **高性能计算集群运维**：针对负责管理GPU资源、解决网络瓶颈及存储IO问题的基础设施专家。
*   **模型部署与加速**：用于需要将训练好的模型高效部署到生产环境并降低延迟的工程人员。

### 4. **技术亮点**
*   **实战导向**：内容基于真实工业界经验，而非纯理论推导，直接解决工程痛点。
*   **全链路覆盖**：打通了从底层硬件（GPU/网络）到上层应用（训练/推理）的技术栈。
*   **社区活跃度高**：拥有近1.8万星标，证明其在机器学习工程社区中具有广泛的认可度和参考价值。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18177 | 🍴 1153 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11528 | 🍴 903 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10643 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

#### 1. 中文简介
该项目是一个包含500个AI实战项目的代码集合，涵盖了机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的Python代码实现，帮助开发者快速掌握各类人工智能算法的应用。这是一个非常适合初学者入门和进阶者参考的优质资源库。

#### 2. 核心功能
- **全栈覆盖**：集成机器学习、深度学习、计算机视觉和NLP四大领域的500个独立项目。
- **代码实操**：所有项目均附带可直接运行的Python代码，便于用户复现和理解算法逻辑。
- **分类清晰**：按照技术领域和项目类型进行结构化组织，方便用户按需查找特定案例。
- **学习资源丰富**：结合Awesome列表机制，提供从基础概念到高级应用的完整学习路径。

#### 3. 适用场景
- **AI初学者入门**：适合刚接触人工智能的学生或转行者，通过动手实践快速建立知识体系。
- **项目灵感参考**：供有经验的开发者寻找项目选题或技术实现思路，避免重复造轮子。
- **教学与培训**：可作为高校课程或企业内训的补充材料，提供丰富的实战案例库。

#### 4. 技术亮点
- **高活跃度社区支持**：拥有超过34,000个星标，证明其在开发者社区中的广泛认可和持续维护价值。
- **标签化检索系统**：通过`machine-learning`、`computer-vision`等细粒度标签，实现高效的项目筛选与定位。
- **端到端实现**：不仅提供模型训练代码，还包含数据预处理、评估及可视化等完整流程示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7294 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **项目名称**：Netron

1. **中文简介**
Netron 是一款用于查看神经网络、深度学习及机器学习模型结构的可视化工具。它支持多种主流框架生成的模型文件，帮助用户直观理解模型架构与参数分布。该工具以轻量级和跨平台特性著称，是模型调试与分析的高效辅助手段。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 Safetensors 等。
*   提供清晰的图形化界面，直观展示神经网络的层结构、张量形状及数据流向。
*   支持在浏览器或桌面端运行，无需安装复杂的依赖环境即可快速加载和查看模型。
*   允许用户深入检查模型内部的权重数据和节点配置，便于进行细节排查。

3. **适用场景**
*   **模型调试**：在训练过程中或训练后，快速检查模型结构是否符合预期，定位连接错误。
*   **格式转换验证**：验证模型从一种框架（如 PyTorch）转换为另一种格式（如 ONNX 或 CoreML）后的结构完整性。
*   **技术分享与文档编写**：生成模型结构图，用于技术博客、论文附录或团队内部的技术交流材料。
*   **嵌入式部署预检**：在将模型部署到移动端或边缘设备前，确认模型兼容性和量化状态。

4. **技术亮点**
*   **高兼容性**：统一支持数十种不同框架和格式的模型文件，极大简化了多框架工作环境下的模型查看流程。
*   **轻量级架构**：基于 Electron 和 Web 技术构建，既可作为桌面应用使用，也可嵌入网页中在线查看，资源占用低。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33139 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了必备的核心速查表（Cheat Sheets）。内容涵盖广泛，旨在帮助研究人员快速回顾关键概念、代码片段及数学公式。

2. **核心功能**
*   提供机器学习和深度学习领域的综合性知识速查。
*   包含 NumPy、SciPy 和 Matplotlib 等常用库的代码示例与用法指南。
*   集成 Keras 框架的关键操作与结构说明。
*   梳理人工智能相关的基础理论与实用技巧。

3. **适用场景**
*   深度学习初学者快速掌握基础工具和框架的核心用法。
*   研究人员在实验过程中快速查阅特定函数或数学公式。
*   面试准备时复习机器学习与深度学习的关键知识点。
*   日常编码时作为参考手册，提高使用科学计算库的效率。

4. **技术亮点**
*   精选高频使用的技术栈（如 Keras、NumPy、Matplotlib），极具实用性。
*   形式简洁直观，适合快速检索而非系统学习。
*   由知名技术博客作者整理，内容经过社区验证，质量较高。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费配套教材，旨在帮助零基础用户入门并实现就业实战。内容涵盖 Python、数学基础以及机器学习、深度学习、计算机视觉和自然语言处理等热门领域的主流框架与工具。

2. **核心功能**
*   提供结构化的 AI 学习路径，涵盖从编程基础到高级算法的完整知识体系。
*   收录近 200 个实战案例和项目资源，强化动手能力与工程实践经验。
*   免费提供配套学习资料，降低入门门槛，适合不同阶段的学习者。
*   广泛覆盖 TensorFlow、PyTorch、Keras 等主流深度学习框架及数据分析工具。

3. **适用场景**
*   零基础转行或希望系统学习人工智能技术的初学者。
*   需要大量实战项目参考以准备就业面试的数据科学或算法工程师。
*   希望快速掌握 Python 数据处理库（如 Pandas、Numpy）及可视化工具的学生或从业者。

4. **技术亮点**
*   资源高度集成，将分散的热门技术栈（CV、NLP、DL 等）整合为统一的学习指南。
*   强调“就业实战”，通过丰富的案例库直接对接行业实际需求。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置降低了深度学习开发的门槛，使开发者能够快速原型化并训练各种机器学习模型。

**2. 核心功能**
*   **低代码/无代码开发**：支持通过简单的 YAML 配置文件定义模型架构和数据集，无需编写大量代码即可创建复杂模型。
*   **多模态支持**：原生支持处理文本、图像、表格、音频等多种数据类型，适用于广泛的机器学习任务。
*   **模型微调与训练**：内置对主流大模型（如 Llama、Mistral）的微调支持，简化了从预训练模型到特定任务模型的迁移过程。
*   **自动化评估与可视化**：提供自动化的模型评估指标计算和直观的可视化结果展示，便于监控训练进度和性能。

**3. 适用场景**
*   **快速原型开发**：数据科学家希望在不深入底层代码的情况下，快速验证不同神经网络架构在特定数据集上的表现。
*   **企业级 AI 应用部署**：团队需要构建稳定、可复现且易于维护的机器学习管道，用于生产环境中的预测或分类任务。
*   **大语言模型定制**：研究人员或开发者希望对开源 LLM（如 LLaMA、Mistral）进行领域特定的微调（Fine-tuning），以适应垂直行业需求。

**4. 技术亮点**
*   **基于 PyTorch 的后端**：利用 PyTorch 的强大生态系统，确保模型训练的灵活性和高性能。
*   **数据中心（Data-Centric）理念**：强调通过改进数据和配置来优化模型，而非仅依赖复杂的代码调整，符合现代 AI 开发趋势。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11725 | 🍴 1220 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9117 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8909 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8376 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6190 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面的中英文自然语言处理工具集合，涵盖了从基础的敏感词检测、语言识别到复杂的实体抽取、知识图谱构建及预训练模型资源。该项目集成了海量的中文垂直领域词库（如医疗、法律、汽车等）及多种NLP算法与数据集，旨在为开发者提供一站式的中英双语NLP解决方案。

2. **核心功能**
*   **基础文本处理**：提供敏感词过滤、中英文语言检测、繁简体转换及标点修复等功能。
*   **信息抽取与识别**：支持手机/电话归属地查询、身份证/邮箱/手机号抽取、命名实体识别（NER）及事件三元组抽取。
*   **词库与资源聚合**：内置中日文人名库、中文缩写库、职业/品牌/地名等专业词库，以及大量公开NLP数据集和预训练模型（如BERT、ALBERT）。
*   **高级应用工具**：包含情感分析、文本摘要、关键词提取、聊天机器人构建框架及知识图谱问答系统示例。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析工具，快速构建互联网平台的内容过滤和舆情监控系统。
*   **垂直领域知识图谱构建**：借助医疗、法律、金融等领域的专业词库和实体抽取工具，快速搭建行业专用知识图谱。
*   **智能客服与对话系统开发**：参考项目中的对话数据集、意图识别模型及聊天机器人案例，开发具备上下文理解能力的智能客服。
*   **NLP算法研究与教学**：作为学习资源库，获取最新的NLP论文解读、基准数据集（Benchmark）及主流算法（如BERT、GPT2）的代码实现。

4. **技术亮点**
*   **生态极度丰富**：不仅包含代码库，还整合了清华XLORE、百度中文问答集等顶级学术和企业级资源，是中文NLP领域的“百科全书”。
*   **全栈式覆盖**：从底层的数据清洗（OCR、语音转文本）、中层的信息抽取（NER、关系抽取）到上层的语义理解（问答、摘要），提供了完整的工具链参考。
*   **前沿模型集成**：紧跟技术潮流，包含了大量基于Transformer架构（BERT、GPT2、ERNIE等）的最新预训练模型及其微调应用示例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72527 | 🍴 8872 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
该项目是一套为期12周、包含24节课的AI入门课程体系，旨在让所有学习者都能轻松掌握人工智能知识。课程主要基于Jupyter Notebook编写，涵盖了从基础概念到深度学习应用的广泛内容。

### 2. 核心功能
*   **系统化课程设计**：提供结构清晰的12周学习路径，每周一课，适合循序渐进地学习。
*   **丰富的技术覆盖**：内容涵盖机器学习、深度学习、计算机视觉、NLP及生成对抗网络等主流AI领域。
*   **交互式学习环境**：采用Jupyter Notebook格式，支持代码执行与可视化，便于动手实践。
*   **微软官方背书**：由Microsoft For Beginners系列出品，确保内容的专业性与权威性。
*   **面向零基础用户**：设计初衷为“AI for All”，降低技术门槛，适合各类背景的学习者。

### 3. 适用场景
*   **初学者入门学习**：适合无编程或AI基础的新手建立对人工智能的整体认知。
*   **高校或培训机构课程补充**：可作为计算机科学或数据科学专业的辅助教材或实验指导。
*   **企业员工技能提升**：帮助非技术岗位人员了解AI基本原理及其在业务中的应用潜力。
*   **自我驱动型学习者**：适合希望利用业余时间系统自学AI知识的个人开发者。

### 4. 技术亮点
*   **多模态AI覆盖**：不仅包含传统的机器学习和NLP，还深入讲解了CNN（卷积神经网络）、RNN（循环神经网络）和GAN（生成对抗网络）等高级架构。
*   **实践导向**：通过代码示例和笔记形式，强调理论结合实践，帮助学习者快速上手。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48474 | 🍴 10058 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个持续更新的资源库，收集并提取了来自 Anthropic (Claude系列)、OpenAI (ChatGPT/GPT系列)、Google (Gemini系列) 以及 xAI 等主流大模型厂商的系统提示词（System Prompts）。它涵盖了 Claude Code、Cursor、Copilot 等多种 AI 助手和代码生成工具的底层指令集，旨在为研究者和开发者提供宝贵的参考素材。

### 2. 核心功能
*   **多模型提示词汇总**：整合了包括 Claude、GPT、Gemini、Grok 等数十种热门 AI 模型及工具的系统级指令。
*   **定期更新维护**：随着新模型版本的发布，持续同步最新的系统提示词内容以保持时效性。
*   **开源共享资源**：以开放源代码的形式提供，方便社区成员自由访问、下载和研究。
*   **结构化数据整理**：将非结构化的内部指令转化为可阅读、可分析的文本格式，降低获取门槛。

### 3. 适用场景
*   **Prompt 工程学习**：新手通过研究顶级模型的官方指令，快速理解高质量 Prompt 的设计规范和逻辑结构。
*   **模型行为逆向分析**：研究人员通过分析系统提示词，推断模型的安全机制、角色设定及输出约束策略。
*   **AI 应用开发参考**：开发者在构建自定义 AI Agent 或聊天机器人时，借鉴成熟模型的系统指令以提升交互效果。

### 4. 技术亮点
*   **极高的社区认可度**：拥有超过 46,000 个 Star，表明其在 AI 社区中具有广泛的影响力和实用性。
*   **覆盖主流生态**：几乎囊括了当前市场上所有头部 AI 厂商的核心产品，是了解行业基准的重要窗口。
*   **教育价值显著**：作为“Awesome”列表类项目，它为生成式 AI 领域的教育和自我提升提供了权威的一手资料。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46333 | 🍴 7593 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个综合性的AI学习资源库，涵盖了从基础数学原理到高级深度学习算法的全方位实战内容。它集成了数据分析、线性代数、PyTorch及TensorFlow 2等主流技术栈，旨在帮助开发者系统性地掌握机器学习与自然语言处理技能。

2. **核心功能**
*   提供包含AdaBoost、K-Means、SVM等多种经典机器学习和深度学习算法的代码实现。
*   结合PyTorch和TensorFlow 2框架，演示DNN、RNN、LSTM等神经网络的构建与训练。
*   集成NLTK库进行自然语言处理（NLP）实战，并涵盖推荐系统与回归分析等应用场景。
*   补充线性代数等数学基础理论，为理解复杂算法提供必要的理论支撑。

3. **适用场景**
*   初学者希望系统化学习机器学习理论及其在Python中的代码落地。
*   工程师需要快速查阅或复用常见的机器学习模型（如聚类、分类）的标准实现。
*   研究人员利用该项目作为基准，对比不同深度学习框架（PyTorch/TF）下的算法表现。

4. **技术亮点**
*   采用“理论+实战”双驱动模式，不仅提供代码，还强调背后的数学原理（如PCA、SVD）。
*   覆盖技术栈广泛，同时支持传统机器学习库（scikit-learn）与现代深度学习框架（PyTorch/TF2）。
*   社区认可度高（4万+星标），说明其代码质量、完整性和教学价值经过了大量开发者的验证。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42351 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36462 | 🍴 5999 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7294 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33699 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28204 | 🍴 3423 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25741 | 🍴 2884 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理领域的开源项目集合。该项目不仅提供了丰富的代码示例，还按领域进行了细致分类，是开发者学习AI技术的优质资源库。

2. **核心功能**
- 提供超过500个包含完整代码的AI实战项目。
- 覆盖机器学习、深度学习、计算机视觉和NLP四大核心领域。
- 作为“Awesome”列表，对项目进行了高质量筛选与分类整理。
- 所有项目均附带源码，便于开发者直接运行和学习。

3. **适用场景**
- 初学者希望通过实际案例快速掌握AI基础概念和编程实现。
- 研究人员或工程师寻找特定领域（如CV或NLP）的参考代码和灵感。
- 教育机构或个人导师用于制作AI课程的教学素材和实践作业。

4. **技术亮点**
- 规模庞大且分类清晰，一站式解决多领域AI项目查找需求。
- 高度社区驱动（星标数超3万），确保项目内容的时效性与实用性。
- 强调“带代码”的实践性，降低从理论到落地的门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7294 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流程的工具。它通过结合大语言模型与视觉理解能力，能够像人类一样操作网页，实现无需编写代码的端到端流程自动化。该项目旨在提供比传统 RPA 更灵活、更智能的浏览器自动化解决方案。

**2. 核心功能**
*   **AI 驱动的操作决策**：利用 LLM 和计算机视觉理解页面内容并自主决定下一步操作，而非依赖固定的 CSS 选择器。
*   **动态页面适应**：能够自动应对网页布局变化、弹窗加载或元素重排，提高了自动化脚本的鲁棒性。
*   **无需代码配置**：用户只需提供自然语言指令（如“登录网站并下载报表”），系统即可自动生成并执行相应的浏览器操作步骤。
*   **集成主流自动化引擎**：底层支持 Playwright 等现代浏览器自动化工具，确保高效稳定的网页交互能力。

**3. 适用场景**
*   **跨平台数据录入与同步**：自动在多个不同结构的内部系统中填写表单、转移数据，减少人工重复劳动。
*   **动态价格监控与比价**：自动访问电商网站，处理反爬验证，抓取实时商品价格和库存信息。
*   **自动化报表生成与分发**：定期登录企业后台，下载指定周期的业务报表，并通过邮件或即时通讯工具发送给相关人员。

**4. 技术亮点**
*   **视觉+语义双重理解**：结合了大语言模型的逻辑推理能力和视觉模型对 UI 元素的识别能力，解决了传统 RPA 难以处理非结构化页面的痛点。
*   **高容错率的自我修复**：当页面元素发生变化时，AI 能重新规划路径继续执行任务，显著降低了维护自动化脚本的成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22013 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，专为视觉人工智能设计。它提供开源、云端及企业级产品，并支持带 AI 辅助标注、质量保证和团队协作的图片、视频及 3D 数据标注服务。

2. **核心功能**
*   支持图像、视频和 3D 数据的全面标注，涵盖边界框、语义分割及分类等任务。
*   内置 AI 辅助标注功能，显著提升数据标记效率并支持自动化预处理。
*   提供完善的质量保证机制与团队协作工具，确保数据集的高标准一致性。
*   开放开发者 API，便于集成到现有的机器学习工作流中。

3. **适用场景**
*   为计算机视觉模型训练准备大规模、高精度的标注数据集。
*   需要多人协作进行复杂视频或 3D 点云数据标注的专业团队。
*   希望利用 AI 预标注功能加速数据清洗和标记流程的开发人员。

4. **技术亮点**
*   基于 Python 开发，深度兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   提供从开源自建到云服务的企业级灵活部署方案。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16159 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### GitHub项目分析：pytorch-grad-cam

1. **中文简介**
   该项目专注于计算机视觉领域的高级AI可解释性研究，支持卷积神经网络（CNN）和视觉Transformer等多种模型架构。它不仅涵盖图像分类任务，还广泛适用于目标检测、语义分割、图像相似度计算等复杂场景，旨在通过可视化工具提升深度学习模型的透明度。

2. **核心功能**
   *   支持多种主流视觉架构，包括经典CNN和最新的Vision Transformers。
   *   实现多样化的可解释性算法，如Grad-CAM、Score-CAM及其变体（如Class-Activation Maps）。
   *   提供全面的任务适配能力，覆盖分类、检测、分割及相似度比对等应用场景。
   *   生成直观的可视化热力图，帮助用户理解模型关注的具体图像区域。
   *   基于PyTorch框架开发，便于集成到现有的深度学习工作流中。

3. **适用场景**
   *   **医疗影像诊断验证**：医生或研究人员利用热力图确认模型是否聚焦于病灶区域，而非背景噪声。
   *   **自动驾驶安全审计**：分析目标检测模型在识别行人或车辆时的决策依据，提升系统可信度。
   *   **学术研究解释性分析**：在发表计算机视觉论文时，提供模型内部机制的可视化证据以增强说服力。
   *   **调试模型偏差**：开发者通过观察模型关注的错误区域，快速定位并修正数据标注或模型结构问题。

4. **技术亮点**
   *   **算法多样性**：不仅限于基础的Grad-CAM，还集成了Score-CAM等多种前沿可解释性方法。
   *   **架构兼容性**：对非CNN架构（如Vision Transformer）的良好支持，紧跟当前AI技术发展趋势。
   *   **高社区活跃度**：拥有超过1.2万星标，表明其在开源社区中具有极高的认可度和广泛的使用基础。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理与计算机视觉算法，旨在简化深度学习中的视觉任务开发。

2. **核心功能**
*   提供丰富的可微分几何计算机视觉算子，支持端到端的深度学习训练。
*   集成多种图像预处理、增强及传统视觉算法，无缝衔接 PyTorch 框架。
*   具备模块化设计，方便研究人员快速实验新的视觉模型和架构。

3. **适用场景**
*   开发需要结合传统几何约束与现代深度学习模型的空间智能应用。
*   进行机器人视觉导航或 SLAM（同步定位与建图）系统的原型设计与研究。
*   构建包含图像增强和数据增强的深度学习数据管道，以提升模型鲁棒性。

4. **技术亮点**
*   **完全可微分**：所有核心操作均支持梯度反向传播，便于集成到神经网络中。
*   **PyTorch 原生集成**：作为 PyTorch 的一等公民，直接利用其自动微分机制，无需额外转换。
*   **高性能 GPU 加速**：充分利用 GPU 并行计算能力，显著加快大规模视觉数据的处理速度。
- 链接: https://github.com/kornia/kornia
- ⭐ 11251 | 🍴 1192 | 语言: Python
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
- ⭐ 3254 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2616 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2412 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款基于“龙虾”理念的个人 AI 助手，支持在任何操作系统和平台上运行。它强调数据主权，让用户能够完全掌控自己的 AI 体验。作为一个开源项目，它旨在提供灵活且私密的个人助理解决方案。

### 2. 核心功能
- **全平台兼容性**：支持任意操作系统和平台部署，确保广泛的可访问性。
- **数据私有化**：强调“拥有自己的数据”，用户可本地化运行以保护隐私。
- **个人助理定位**：专为个人使用设计，提供定制化的 AI 交互体验。
- **开源透明**：基于 TypeScript 开发，代码开放，便于社区贡献和二次开发。

### 3. 适用场景
- **隐私敏感用户**：需要本地运行 AI 以避免数据上传至云端的个人或开发者。
- **跨平台工作者**：在 Windows、macOS 或 Linux 等不同系统间切换，需统一 AI 工具的用户。
- **AI 爱好者与研究者**：希望深入了解或定制个人 AI 助手底层逻辑的技术人员。

### 4. 技术亮点
- **TypeScript 驱动**：利用 TypeScript 的类型安全性和现代前端/后端生态优势，保障代码质量与可维护性。
- **模块化架构**：通过“龙虾”隐喻体现其灵活扩展的设计哲学，便于集成不同 AI 模型或服务。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380603 | 🍴 79736 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 239408 | 🍴 21241 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款能够随用户共同成长和进化的智能代理。它具备高度的自主性和适应性，旨在通过持续的学习与交互，更好地辅助用户完成复杂任务。该项目在开发者社区中获得了极高的关注度，体现了其强大的实用价值。

### 2. 核心功能
*   **自主进化能力**：代理并非静态工具，而是能根据用户反馈和使用习惯不断调整和优化自身行为。
*   **多模型兼容支持**：集成对 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 等多种主流大语言模型的支持。
*   **智能代码辅助**：深度整合编码工作流，提供类似 Codex 或 Claude Code 的代码生成、调试及重构建议。
*   **个性化记忆与上下文管理**：能够记住长期对话历史和偏好，确保在多轮交互中保持连贯性和个性化服务。
*   **模块化架构设计**：基于 Python 构建，允许开发者轻松扩展新功能或替换底层 AI 引擎。

### 3. 适用场景
*   **高级开发者个人助手**：需要自动化处理重复性编码任务、代码审查及项目管理的资深程序员。
*   **AI 应用原型快速开发**：希望利用现成智能代理框架快速搭建具备自主决策能力的 AI 应用的研究者或初创团队。
*   **个性化知识管理**：依赖长期记忆和上下文理解，用于整理复杂信息、辅助决策或进行深度研究的用户。

### 4. 技术亮点
*   **高活跃度社区验证**：超过 20 万星的极高关注度，表明其架构稳定性和生态兼容性经过广泛验证。
*   **前沿模型集成策略**：同时支持 OpenClaw、Moltbot 等新兴代理框架概念，展现了其在 AI Agent 领域的技术前瞻性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 203751 | 🍴 36556 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个采用公平开源许可的工作流自动化平台，原生集成 AI 能力并支持 400 多种集成方式。它结合了可视化构建与自定义代码开发，用户可选择自行托管或云部署，灵活满足各类自动化需求。

2. **核心功能**
*   提供可视化工作流构建器，降低自动化开发门槛。
*   原生支持 AI 功能，可轻松集成大语言模型等智能服务。
*   拥有超过 400 种预置集成，覆盖主流 API 和应用程序。
*   支持混合开发模式，可在可视化流程中嵌入自定义代码。
*   提供灵活的部署选项，包括自托管（Self-hosted）和云服务。

3. **适用场景**
*   企业级业务流程自动化，如审批流、数据同步和通知分发。
*   基于 AI 的智能应用开发，例如自动摘要生成、客服机器人或数据分析。
*   开发者工具链集成，通过自定义代码扩展特定系统的连接能力。
*   需要数据隐私控制或成本优化的自建自动化平台部署。

4. **技术亮点**
*   基于 TypeScript 开发，具备良好的类型安全和现代前端/后端体验。
*   支持 MCP（Model Context Protocol），增强了与 AI 模型交互的标准性和灵活性。
*   采用 Fair-code 许可协议，平衡了社区贡献与商业使用的权益。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194180 | 🍴 58856 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松访问、使用和构建人工智能，实现 AI 的普惠化愿景。其使命是提供必要的工具，帮助用户将精力集中在真正重要的任务上。

2. **核心功能**
*   支持自主代理运行，能够独立规划并执行复杂的多步骤任务。
*   集成多种大型语言模型（如 GPT、Claude、Llama），具备灵活的底层架构。
*   提供丰富的扩展接口，允许用户基于现有工具进行二次开发。
*   具备自我反思与纠错机制，能在执行过程中优化结果。

3. **适用场景**
*   自动化内容创作，如生成博客文章、社交媒体文案或代码片段。
*   复杂的研究任务，自动搜集信息、整理数据并生成总结报告。
*   日常工作效率提升，例如自动管理邮件、安排日程或处理重复性行政工作。

4. **技术亮点**
*   采用模块化设计，兼容 OpenAI 及多种开源 LLM API，降低对单一供应商的依赖。
*   拥有庞大的社区生态和活跃的开发者支持，便于获取插件和解决方案。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185160 | 🍴 46132 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164392 | 🍴 21286 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163889 | 🍴 30368 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156635 | 🍴 46147 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150113 | 🍴 9352 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146674 | 🍴 23094 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

