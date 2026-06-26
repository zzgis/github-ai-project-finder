# GitHub AI项目每日发现报告
日期: 2026-06-26

## 新发布的AI项目

### theeleven
- ### 1. 中文简介
该项目在 X Layer 上部署了 11 个自主运行的 AI 代理，实时监控并交易足球赛事的盘口市场。它利用自定义的 Uniswap V4 Hook 实现了免 Gas 费的 USDT0 质押功能，结合预测市场机制为用户提供去中心化的体育博彩体验。

### 2. 核心功能
*   **多智能体协作**：运行 11 个独立的 AI 代理，自动处理市场数据分析和交易执行。
*   **定制化 DeFi 协议**：基于 Uniswap V4 开发自定义 Hook，实现链上流动性的创新管理。
*   **零 Gas 费体验**：通过 EIP-3009 等技术实现 USDT0 的免 Gas 费质押与转账，降低用户门槛。
*   **体育预测市场**：专注于足球赛事的实时盘口交易，支持去中心化的胜负预测与投注。

### 3. 适用场景
*   **去中心化体育博彩平台**：为足球爱好者提供无需托管资金、自动化执行的竞猜服务。
*   **AI 驱动的量化交易策略测试**：开发者可利用该架构验证多 Agent 在实时市场数据中的协同交易能力。
*   **Web3 游戏与元宇宙经济**：将体育预测机制融入游戏生态，作为用户获取代币奖励或 NFT 的互动模块。

### 4. 技术亮点
*   **前沿标准应用**：集成了 Uniswap V4 Hooks、ERC-8257 和 MCP（模型上下文协议），展示了最新的 Web3 开发范式。
*   **Layer 2 优化**：部署于 X Layer，结合 OKX 生态优势，兼顾了高吞吐量与低交易成本。
*   **AI 与 DeFi 深度融合**：不仅使用 AI 进行分析，还通过自主代理直接执行链上操作，实现了“AI Agent + DeFi”的闭环自动化。
- 链接: https://github.com/winsznx/theeleven
- ⭐ 469 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, defi, eip-3009, erc-8257, football

### video-production-skills
- 1. **中文简介**
这是一个可复用的AI视频制作技能库，旨在简化视频创作流程。它涵盖了从生成、重建到动态设计及质量检查的全方位功能。开发者可以利用该库快速构建高效的自动化视频处理工作流。

2. **核心功能**
*   提供用于创建新视频的AI生成技能。
*   支持对现有视频进行重建或重制。
*   包含动态设计（Motion Design）相关的制作能力。
*   具备自动片头（Openers）生成的功能。
*   集成视频质量检查（QA）机制以优化输出结果。

3. **适用场景**
*   需要批量生成营销宣传视频的媒体团队。
*   希望自动化处理视频后期与质检流程的开发人员。
*   致力于利用AI辅助进行动态图形设计的创意工作者。
*   构建端到端视频生产自动化管道的企业级应用。

4. **技术亮点**
该项目采用Python语言开发，强调技能的“可复用性”，为视频生产提供了模块化且标准化的AI解决方案。
- 链接: https://github.com/Pluviobyte/video-production-skills
- ⭐ 182 | 🍴 17 | 语言: Python

### GITVERSE
- ### 1. 中文简介
GITVERSE 是一个逆向工程工具，能够将任意代码库转化为构建提示词，自动生成架构分解、ASCII 蓝图以及供 AI 使用的重构提示。它利用大型语言模型（LLM）深度分析代码结构，帮助开发者快速理解复杂系统并生成标准化的重建指令。

### 2. 核心功能
*   **架构逆向解析**：自动拆解代码库结构，生成清晰的架构图解和 ASCII 蓝图。
*   **AI 就绪提示生成**：将分析结果转化为针对 Claude、Cursor 等 AI 工具优化的重构提示词。
*   **多平台集成支持**：通过 GitHub API 接入代码库，并结合 Next.js 提供 Web 界面交互体验。
*   **多 LLM 兼容分析**：支持调用 OpenAI 或 Anthropic 等大模型进行深层代码语义分析。

### 3. 适用场景
*   **接手遗留项目**：快速理解陌生或文档缺失的大型代码库的整体架构与依赖关系。
*   **AI 辅助重构**：为 Cursor、Claude Code 等 AI 编程助手提供精准的结构化上下文，以提高代码重构或迁移的效率。
*   **技术文档自动化**：自动生成可视化的架构蓝图和结构化说明，用于团队内部的技术分享或知识库建设。

### 4. 技术亮点
*   结合 **Prompt Engineering**（提示词工程）技巧，专门优化输出以适配当前主流的 AI 编码代理工具。
*   采用 **TypeScript + Next.js + Tailwind CSS** 技术栈，确保高性能前后端分离架构与现代化的用户界面体验。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 131 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### Anti-Autoresearch
- 1. **中文简介**
不要盲目信任自动生成的研究论文，本项目专注于审稿人视角的完整性取证，通过检测39种黑客模式（涵盖7类）来验证自我一致性与内容伪造情况，并给出确定性结论。它并非用于检测AI文本的工具，而是ARIS项目的对立面补充方案。

2. **核心功能**
*   提供审稿人视角的研究完整性取证分析。
*   基于39种特定黑客模式进行自我一致性检查。
*   执行针对7大类模式的伪造内容检测。
*   生成确定性的审查结论而非概率性判断。
*   明确区别于通用的AI文本检测器。

3. **适用场景**
*   学术期刊或会议审稿人核查疑似由LLM代理自动生成的投稿。
*   研究人员在引用或评估他人工作时验证其逻辑一致性。
*   学术机构内部进行科研诚信审查和违规检测。
*   对抗性测试中评估自动研究系统（Auto-research）的输出可靠性。

4. **技术亮点**
*   采用确定性判决机制，避免了传统AI检测器的模糊性。
*   构建了细粒度的39种黑客模式分类体系，覆盖7大主要造假家族。
*   聚焦于“审稿人侧”的逻辑与事实一致性，而非单纯的文本特征识别。
- 链接: https://github.com/wanshuiyin/Anti-Autoresearch
- ⭐ 33 | 🍴 1 | 语言: Python
- 标签: ai-generated-content, ai-scientist, autoresearch, forensics, llm-agents

### macos-chatgpt-overlay-bar
- ### 1. 中文简介
macos-chatgpt-overlay-bar 是一款专为 macOS 设计的 ChatGPT 菜单栏工具，让用户无需切换窗口即可快速访问 AI 对话功能。它旨在提升日常工作效率，通过常驻系统状态栏提供便捷的即时交互体验。

### 2. 核心功能
*   **菜单栏常驻**：应用图标固定在 macOS 菜单栏中，保持界面整洁且随时可触达。
*   **快速访问**：通过快捷键或点击菜单项直接唤起 ChatGPT 界面，实现无感切换。
*   **即时对话**：支持在 Overlay 窗口中快速输入提示词并获取 AI 回复，简化工作流。
*   **轻量级集成**：作为独立的小工具运行，不占用过多系统资源，适合后台静默服务。
*   **免费开源**：提供免费的 GPT 访问方式，降低用户使用门槛。

### 3. 适用场景
*   **日常灵感捕捉**：在写作或思考过程中，快速向 AI 提问以获取灵感或优化文案。
*   **多任务处理间隙**：在不中断当前主要工作（如编程、设计）的情况下，利用碎片时间查询信息。
*   **客服或技术支持辅助**：技术人员可快速调用 AI 生成代码片段或排查常见问题的解决方案。

### 4. 技术亮点
*   **原生 macOS 体验**：深度适配 macOS 菜单栏（Menubar）和状态栏（Status Bar）设计规范，提供符合直觉的用户界面。
*   **极简架构**：作为非传统应用形态的辅助工具，专注于“快启即用”的核心逻辑，避免了复杂的功能冗余。
- 链接: https://github.com/ik190/macos-chatgpt-overlay-bar
- ⭐ 31 | 🍴 3 | 语言: 未知
- 标签: ai, chatgpt, chatgpt-bar-mac, chatgpt-menubar-mac, chatgpt-quick-access-mac

### auto-paper-collecter
- 描述: 📚🔭 Your personal research radar — an LLM-powered tool that auto-aggregates the latest papers for your keywords across arXiv / Crossref / Semantic Scholar / GitHub / RSS.
- 链接: https://github.com/PenghaoJiang/auto-paper-collecter
- ⭐ 31 | 🍴 1 | 语言: Python
- 标签: academic, agent-skill, ai, arxiv, claude-code

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

### oil-cover
- 描述: 为小红书 AI 工具实操内容生成稳定、干净、精致封面的 Claude / Codex Skill（脚本模式 + Agent 自主执行）
- 链接: https://github.com/oil-oil/oil-cover
- ⭐ 24 | 🍴 3 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个功能极其丰富的中文自然语言处理资源合集，涵盖了从基础数据处理（如敏感词检测、分词、实体抽取）到高级NLP任务（如情感分析、知识图谱、对话系统）的全方位工具与数据集。该项目不仅提供了大量现成的词典、词向量和预训练模型，还整合了多个领域的专用语料库及前沿的研究代码，是中文NLP开发者的必备资源库。

### 2. 核心功能
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简转换、停用词表、反动词表以及基于正则表达式的手机号、身份证、邮箱等信息抽取。
*   **丰富的词典与知识库**：包含中日文人名库、职业/品牌/汽车/医学/法律等专业领域词库、古诗词库、成语库、地名库及新华字典API等结构化知识资源。
*   **预训练模型与向量工具**：集成多种中文词向量（Word2Vec等）、BERT及ERNIE等预训练语言模型资源，并支持文本生成、摘要提取及序列标注。
*   **高级NLP任务解决方案**：涵盖情感分析、命名实体识别（NER）、依存句法分析、知识图谱构建与问答系统、以及语音识别（ASR）相关数据与工具。
*   **数据增强与评测基准**：提供中文NLP数据增强工具（EDA）、各类NLP竞赛的Top方案代码、语言理解测评基准（如CLUE）及多领域数据集汇总。

### 3. 适用场景
*   **中文NLP项目初始化**：开发者在搭建中文文本分类、情感分析或实体识别模型时，可直接引用项目中的敏感词表、停用词和专业词典以提升基线效果。
*   **企业级风控与内容审核**：利用其中的暴恐词表、敏感词检测及中英文语言检测功能，快速构建互联网内容的安全过滤系统。
*   **垂直领域知识图谱构建**：借助项目提供的医疗、法律、金融等领域专用词库及关系抽取代码，加速构建行业专用的知识图谱。
*   **自然语言教学与研究参考**：师生或研究人员可通过该项目获取高质量的标注数据集（如CLUE基准）、最新论文解读及主流NLP算法的代码实现，用于学习或复现实验。

### 4. 技术亮点
*   **资源极度聚合**：作为一个“仓库中的仓库”，它几乎囊括了中文NLP生态中所有主流的开源工具、数据集、词典和预训练模型，极大降低了信息搜寻成本。
*   **覆盖全生命周期**：从原始数据的清洗、标注、增强，到模型的训练（BERT/ALBERT等）、推理及应用（问答/对话），提供了端到端的资源支持。
*   **紧跟前沿技术**：及时收录了包括BERT、ERNIE、RoBERTa、GPT-2等最新预训练模型的应用案例及代码，并整合了如CLUE等权威评测基准。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI机器学习、深度学习、计算机视觉及自然语言处理项目的代码集合，旨在为开发者提供丰富的实战案例。它涵盖了从基础算法到前沿应用的完整技术栈，是学习人工智能领域各项核心技能的优质资源库。

2. **核心功能**
*   提供涵盖机器学习、深度学习和数据科学的多样化代码示例。
*   集成计算机视觉与自然语言处理领域的具体项目实现。
*   作为“Awesome”列表，系统化整理并索引了高质量的人工智能项目。
*   支持通过Python代码快速复现各类经典AI算法与应用。

3. **适用场景**
*   初学者希望通过实际代码快速入门AI各个细分领域。
*   研究人员或工程师寻找特定任务（如图像识别、文本分类）的参考实现。
*   教育者用于课程设计，为学生提供丰富的练习项目和案例素材。
*   开发者在遇到技术瓶颈时，通过查阅类似项目寻找解决方案灵感。

4. **技术亮点**
*   项目规模庞大且分类清晰，覆盖了AI主流方向的核心技术点。
*   强调“with code”，确保每个项目都有可运行的代码支持，而非仅理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和文件格式，帮助用户直观地理解模型结构与数据流向。该项目由 JavaScript 开发，兼具桌面应用与 Web 端特性，操作简便且跨平台兼容。

**2. 核心功能**
*   广泛支持 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite、safetensors 等数十种模型格式。
*   提供清晰的模型架构视图，直观展示层结构、张量形状及连接关系。
*   支持实时交互操作，包括缩放、平移、节点高亮及详细属性查看。
*   具备本地桌面应用与在线网页版双模式，方便不同环境下的快速调试与分析。

**3. 适用场景**
*   **模型调试与验证**：在部署前检查神经网络结构是否正确，确认层顺序与参数无误。
*   **技术交流与演示**：向非技术人员或团队展示复杂模型的内部逻辑，便于汇报与协作。
*   **异构框架迁移**：在不同深度学习框架（如从 PyTorch 转换到 ONNX 或 TFLite）间转换模型时，进行格式兼容性验证。

**4. 技术亮点**
*   **多语言与多格式兼容**：基于 JavaScript 构建，实现了极高的文件格式覆盖率，无需安装重型依赖即可运行。
*   **轻量级与易用性**：界面简洁直观，学习成本低，是业界公认的模型可视化工具首选之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33139 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个旨在促进机器学习模型互操作性的开放标准。它允许开发者在不同深度学习框架（如 PyTorch、TensorFlow）之间无缝转换模型，从而实现训练与部署环境的解耦。这一标准极大地简化了从原型开发到生产部署的工作流。

### 2. 核心功能
*   **跨框架模型转换**：支持将模型从主流深度学习框架导出并导入其他框架。
*   **统一计算图表示**：提供标准化的计算图格式，确保模型结构在不同平台间的一致性。
*   **运行时兼容性**：配备 ONNX Runtime，可在多种硬件和操作系统上高效执行模型推理。
*   **生态系统集成**：原生支持与 Scikit-learn、Keras 等广泛使用的机器学习库集成。
*   **版本控制与演进**：通过定期的规范更新，保持对新型算子和架构的支持。

### 3. 适用场景
*   **混合框架开发**：在 PyTorch 中训练模型，但在需要 TensorFlow 或 C++ 环境的生产系统中进行部署。
*   **高性能推理优化**：利用 ONNX Runtime 加速模型在 CPU、GPU 或专用硬件上的推理速度。
*   **边缘设备部署**：将大型云端模型转换为轻量级格式，以便在手机、IoT 设备等资源受限环境中运行。
*   **模型交换与协作**：在团队内部或不同组织间共享预训练模型，避免因框架差异导致的技术壁垒。

### 4. 技术亮点
*   **开源中立性**：由微软、Facebook、亚马逊等科技巨头共同维护，确保标准的开放性和广泛采纳。
*   **高度可扩展性**：支持自定义算子，能够适应不断发展的深度学习算法需求。
*   **性能卓越**：ONNX Runtime 经过深度优化，通常能提供比原始框架更快的推理延迟。
- 链接: https://github.com/onnx/onnx
- ⭐ 21051 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一本全面涵盖机器学习工程实践的资源指南。它深入探讨了从模型训练、推理部署到大规模扩展的各个关键技术环节。该项目旨在为构建和运维高性能机器学习系统提供系统化的知识支持。

2. **核心功能**
*   提供针对大型语言模型（LLM）的训练、微调及推理优化的详细最佳实践。
*   详解在 GPU 集群上利用 Slurm 进行分布式训练和作业调度的工程技巧。
*   涵盖 MLOps 全流程，包括数据存储、网络优化、调试技巧及模型可扩展性设计。
*   整合 PyTorch 和 Transformers 等主流框架的高级使用指南与性能调优方案。

3. **适用场景**
*   需要构建和部署大规模大语言模型（LLM）应用的研发团队。
*   负责机器学习基础设施搭建、集群管理及资源调度的 MLOps 工程师。
*   希望优化深度学习模型训练效率、降低 GPU 成本并提升推理速度的算法工程师。
*   寻求系统性学习机器学习工程化落地经验的技术人员和学生。

4. **技术亮点**
*   聚焦前沿的大模型工程挑战，内容紧跟 LLM 时代的技术演进。
*   强调实战性，提供大量关于硬件利用率和系统稳定性的具体优化策略。
*   内容结构完整，覆盖了从底层硬件驱动到上层应用部署的全栈知识体系。
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
- 1. **中文简介**
这是一个收录了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理领域的AI项目合集。该项目提供了完整的代码实现，旨在帮助开发者快速掌握相关技术栈并构建实际应用场景。它被标记为“Awesome”列表，是学习人工智能核心概念的优秀资源库。

2. **核心功能**
*   汇集大量端到端的AI实战项目代码，覆盖主流算法与模型。
*   分类清晰，包含机器学习、深度学习、计算机视觉和NLP四大板块。
*   提供Python语言实现的完整工程示例，便于直接运行和学习。
*   作为初学者到进阶者的参考手册，展示多种AI问题的解决方案。

3. **适用场景**
*   AI初学者通过阅读和复现代码来理解基础理论。
*   数据科学家寻找特定任务（如图像分类或文本生成）的代码模板。
*   企业团队进行技术选型时评估不同AI方案的可行性。
*   学生准备毕业项目或面试作品时获取灵感与基础架构。

4. **技术亮点**
*   规模庞大，拥有超过3.4万星标，证明其社区认可度和实用性极高。
*   标签体系完善，精准覆盖artificial-intelligence、deep-learning等关键技术领域。
*   强调“with code”，不仅提供概念，更提供可执行的工程实践。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架生成的模型格式，帮助用户直观地查看和调试模型结构。

2. **核心功能**
*   广泛支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、SafeTensors 等数十种模型格式。
*   提供直观的图形化界面，清晰展示网络层结构、参数及数据流向。
*   支持在浏览器或桌面端直接打开模型文件，无需安装复杂的依赖环境。
*   允许用户检查模型的具体配置细节，如张量形状、权重信息及算子类型。

3. **适用场景**
*   开发者在训练后快速验证模型架构是否正确，排查层连接错误。
*   研究人员对比不同框架间模型转换（如 PyTorch 转 ONNX）后的结构一致性。
*   非技术人员或学生通过可视化界面理解复杂神经网络的内部工作原理。
*   部署前检查模型是否符合特定硬件或推理引擎的要求。

4. **技术亮点**
*   基于 JavaScript 开发，实现了极高的跨平台兼容性和便携性，无需本地编译即可运行。
*   对最新模型格式（如 SafeTensors）和新兴框架支持迅速，社区活跃度极高。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33139 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习和机器学习研究人员提供了一系列必备的技术速查手册（Cheat Sheets）。内容涵盖了主流框架与核心算法的快速参考，旨在帮助开发者高效查阅关键知识。

### 2. 核心功能
- **深度学习框架速查**：提供 Keras 等框架的关键 API 和使用技巧。
- **数据处理工具参考**：汇总 NumPy、SciPy 和 Matplotlib 等常用库的高效用法。
- **机器学习概念梳理**：整合基础理论，便于快速回顾核心算法逻辑。
- **人工智能资源聚合**：集中展示 AI 领域 essential 的技术知识点。

### 3. 适用场景
- **面试准备**：快速复习 ML/DL 核心概念以应对技术面试。
- **日常开发查阅**：在编写代码时快速查找特定函数或库的参数说明。
- **新人入门引导**：帮助初学者建立对主流 AI 工具和框架的整体认知。
- **研究笔记整理**：作为研究人员记录关键实验参数和模型结构的辅助材料。

### 4. 技术亮点
- **高度浓缩**：将复杂的技术文档提炼为简洁的单页或双页图表，极大提升查阅效率。
- **覆盖面广**：集成了从底层数学库（NumPy/SciPy）到高层应用框架（Keras）的全栈技术点。
- **社区认可度高**：拥有超过 1.5 万星标，证明其内容的实用性和准确性得到了广泛验证。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，整理了近200个实战案例并提供免费配套教材，旨在帮助零基础用户入门并掌握就业所需技能。内容涵盖Python、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等主流技术领域。

2. **核心功能**
*   提供结构化的AI学习路径，覆盖从编程基础到高级算法的完整知识体系。
*   收录近200个精选实战项目与案例，支持动手实践以提升工程能力。
*   免费提供配套学习资料和教材，降低入门门槛。
*   集成多种主流AI框架教程，包括TensorFlow、PyTorch、Keras和Caffe等。
*   聚焦数据科学核心工具链，包含NumPy、Pandas、Matplotlib及Seaborn的使用指南。

3. **适用场景**
*   **零基础转行/入门**：适合希望进入AI领域但缺乏背景的初学者建立系统知识框架。
*   **求职实战准备**：适用于需要积累项目经验、提升简历竞争力的求职者进行针对性训练。
*   **技术栈拓展**：适合已有一定基础的开发者快速熟悉TensorFlow、PyTorch等主流框架的具体应用。
*   **数据科学技能提升**：适用于希望强化Python数据处理、分析及可视化能力的工程师。

4. **技术亮点**
*   高度集成的多领域知识图谱，将数学、编程、算法与应用框架有机结合。
*   强调“实战导向”，通过大量真实案例而非纯理论教学来巩固学习效果。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大型语言模型（LLM）、神经网络及其他人工智能模型。它通过简化复杂的深度学习流程，让开发者能够专注于数据与业务逻辑，而非底层工程细节。

**2. 核心功能**
*   支持基于声明式配置快速训练和微调各种深度学习模型。
*   兼容主流框架如 PyTorch，并提供对 LLM（如 Llama、Mistral）的优化支持。
*   具备数据-centric 特性，强化数据处理与分析在模型开发中的核心地位。
*   提供开箱即用的界面，降低计算机视觉和自然语言处理任务的入门门槛。

**3. 适用场景**
*   需要快速原型验证深度学习模型效果的数据科学团队。
*   希望在不编写大量代码的情况下微调大型语言模型的企业开发者。
*   专注于提升数据质量以优化模型性能的数据中心主义项目。

**4. 技术亮点**
*   **低代码高效能**：通过 YAML/JSON 配置文件驱动模型构建，显著减少样板代码。
*   **广泛的模型兼容性**：原生支持从传统神经网络到最新 LLM 的多类型架构。
*   **端到端工作流**：整合数据预处理、模型训练、评估及部署的全生命周期管理。
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
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。它不仅提供了丰富的行业词库（如汽车、医疗、金融）和预训练模型资源，还涵盖了从语音识别到知识图谱构建的多种高级 NLP 任务解决方案。该项目旨在为开发者提供一站式的中英双语 NLP 数据处理与分析工具集。

2. **核心功能**
*   **基础文本处理**：提供敏感词过滤、中英文语言检测、繁简体转换、分词及词性标注等核心功能。
*   **信息抽取与识别**：支持从文本中精准抽取手机号、身份证号、邮箱、人名、地名等实体，并具备性别推断能力。
*   **丰富词库与资源**：内置大量垂直领域词库（医疗、法律、汽车等）、停用词、情感分析及同义词/反义词库。
*   **深度学习模型集成**：整合了 BERT、GPT2、ALBERT 等主流预训练模型的中文版本及应用示例（如 NER、文本分类）。
*   **多模态与高级任务**：涵盖语音识别（ASR）、OCR 文字识别、对话机器人构建及知识图谱抽取等进阶 NLP 任务。

3. **适用场景**
*   **内容审核与安全**：利用敏感词库和情感分析功能，对社交媒体评论、用户生成内容进行自动化审核和风险过滤。
*   **智能客服与对话系统**：结合聊天语料库、对话数据集及 Rasa/ConvLab 等框架，快速搭建具备语义理解和多轮对话能力的智能客服。
*   **企业级数据清洗与结构化**：在金融、法律或医疗行业，利用实体抽取和规则匹配工具，从非结构化文档中提取关键业务信息。
*   **NLP 算法研究与原型开发**：作为研究人员或学生，利用其提供的基准数据集、模型代码及评测工具，快速复现 SOTA 算法或进行对比实验。

4. **技术亮点**
*   **生态完整性**：不仅包含代码实现，还汇聚了大量高质量的中文数据集、预训练模型及学术资源，极大降低了 NLP 入门门槛。
*   **领域针对性强**：特别针对中文特性优化，如汉字特征提取、中文数字转换、拼音标注及中文特有的实体识别，弥补了通用工具在中文场景下的不足。
*   **实用性强**：提供了即插即用的工具包（如 jieba_fast 加速版、SpaCy 中文模型），兼顾了开发效率与运行性能。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与多模态大模型（VLM）微调框架，支持超过100种主流模型。该项目已入选 ACL 2024 会议，旨在降低大模型微调的技术门槛并提供高性能的训练体验。

**2. 核心功能**
*   **全模型支持**：原生兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流大模型及视觉语言模型。
*   **多种微调算法**：内置 LoRA、QLoRA、P-Tuning 等高效微调方法，以及完整的 RLHF（基于人类反馈的强化学习）支持。
*   **量化训练优化**：提供 4-bit/8-bit 量化训练功能，显著降低显存需求，使消费级显卡也能运行大规模模型。
*   **一站式训练平台**：集成训练、评估、推理和导出功能，支持命令行（CLI）和可视化 Web UI 两种交互方式。

**3. 适用场景**
*   **企业私有化部署**：利用 QLoRA 等技术，在有限显存资源下对企业内部数据进行低成本、高效率的微调。
*   **多模态应用开发**：快速微调具备图像理解能力的 VLM 模型，用于构建智能客服或内容生成应用。
*   **学术研究实验**：为 NLP 研究者提供标准化的实验基准，便于对比不同 SFT 和 RLHF 算法的效果。

**4. 技术亮点**
*   **极致性能**：通过底层代码优化实现极高的训练吞吐量，大幅缩短模型收敛时间。
*   **无缝集成**：基于 Hugging Face Transformers 和 PEFT 库构建，但提供了更简化的接口和更完善的工程化支持。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72527 | 🍴 8872 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
该项目是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松学习AI技术。它通过Jupyter Notebook提供互动式编程练习，覆盖从基础概念到高级应用的广泛主题。作为微软“初学者”系列的一部分，它为初学者提供了结构清晰且易于上手的学习路径。

### 2. 核心功能
*   提供结构化的12周学习路线图，分为24个独立课时，循序渐进地引导学习者。
*   采用Jupyter Notebook作为主要教学载体，支持代码实时运行与交互式学习体验。
*   涵盖机器学习、深度学习、自然语言处理（NLP）、计算机视觉等核心AI领域知识。
*   深入讲解卷积神经网络（CNN）、循环神经网络（RNN）及生成对抗网络（GAN）等具体模型架构。
*   由微软发起并维护，确保内容的专业性、准确性以及与业界标准接轨。

### 3. 适用场景
*   **高校或培训机构的基础课程**：教师可直接将其作为计算机科学或数据科学专业的补充教材。
*   **零基础转行者的自学计划**：希望进入AI领域的非技术人员可通过此课程建立系统的知识框架。
*   **企业内部员工培训**：公司可用于提升团队对现代AI技术及应用场景的理解和实践能力。
*   **在线社区协作学习**：学习者可在GitHub上分享笔记、提交作业并参与开源社区的讨论与交流。

### 4. 技术亮点
*   完全基于Jupyter Notebook，实现了理论与代码实践的无缝结合，便于即时验证学习成果。
*   内容广度与深度兼顾，既包含传统机器学习算法，也涉及前沿的深度学习和生成式AI技术。
*   开源免费且持续更新，拥有庞大的社区支持和极高的星标数（48k+），保证了资源的活跃性与可靠性。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48473 | 🍴 10058 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- ### 1. 中文简介
该项目收集并泄露了包括 Anthropic、OpenAI、Google 和 xAI 在内的多家主流 AI 公司的系统提示词（System Prompts）。它涵盖了 Claude 系列、ChatGPT、Gemini 以及 Cursor、VS Code 等开发工具背后的底层指令集，且内容保持定期更新。

### 2. 核心功能
*   **多模型提示词提取**：获取 Anthropic、OpenAI、Google 及 xAI 等知名模型的内部系统指令。
*   **覆盖开发工具底层逻辑**：不仅包含基础大模型，还收录了 Cursor、Copilot、VS Code 和 Perplexity 等智能开发工具的提示词。
*   **持续动态更新**：随着新模型或版本发布，该项目会及时同步最新的系统提示词泄露数据。

### 3. 适用场景
*   **提示词工程研究**：分析师用于研究顶级 AI 模型的结构化指令设计，以优化自身 Prompt 策略。
*   **安全与合规审计**：企业安全团队评估竞争对手或自研模型在系统指令层面的潜在风险与隐私边界。
*   **开发者逆向学习**：程序员通过解析 Cursor 或 Copilot 的底层指令，深入了解 AI 辅助编程的最佳实践与限制。

### 4. 技术亮点
*   **跨厂商全面性**：罕见地整合了四大科技巨头（Anthropic, OpenAI, Google, xAI）的核心机密数据。
*   **生态广度**：突破单纯聊天机器人范畴，延伸至 IDE 插件和企业级搜索工具的系统层细节。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46319 | 🍴 7593 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个综合性的AI学习资源库，涵盖数据分析、机器学习实战以及深度学习框架（如PyTorch和TensorFlow 2）。内容还延伸至线性代数基础与自然语言处理工具（NLTK），旨在为学习者提供从理论到实践的全方位指导。

2. **核心功能**
- 集成经典机器学习算法（如SVM、K-Means、Adaboost等）的代码实现与解析。
- 提供基于PyTorch和TensorFlow 2的深度神经网络（DNN、RNN、LSTM）实战案例。
- 包含自然语言处理（NLP）相关的文本挖掘与模型训练示例。
- 涵盖推荐系统算法（如协同过滤、矩阵分解SVD）的实际应用代码。
- 补充线性代数等数学基础知识点，辅助理解算法原理。

3. **适用场景**
- AI初学者希望系统性地从数学基础过渡到机器学习及深度学习实战。
- 数据科学家或工程师需要快速查阅常见算法（如分类、聚类、回归）的标准Python实现。
- 研究人员或学生希望对比不同深度学习框架（PyTorch vs TensorFlow）在NLP或图像任务中的用法。

4. **技术亮点**
- 内容覆盖面广，打通了“数学基础-传统机器学习-深度学习-NLP”的技术栈。
- 结合Scikit-learn与主流深度学习框架，兼顾经典算法与前沿技术的实践。
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
- ⭐ 34934 | 🍴 7293 | 语言: 未知
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
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34934 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化框架，旨在通过模拟人类操作来自动化复杂的浏览器工作流。它利用计算机视觉和大语言模型（LLM），无需编写繁琐的脚本即可执行网页交互任务。该项目为 RPA（机器人流程自动化）提供了一种更智能、更灵活的替代方案。

2. **核心功能**
*   **AI 驱动的操作决策**：结合视觉识别与 LLM，自动理解页面布局并生成点击、输入等指令。
*   **非侵入式自动化**：不依赖固定的 CSS 选择器或 DOM 结构，能够适应网页界面的细微变化。
*   **多步工作流编排**：支持处理涉及多个页面跳转和条件判断的复杂业务逻辑。
*   **类人交互体验**：模拟真实用户的鼠标移动和键盘输入行为，降低被目标网站检测为机器人的风险。
*   **API 集成能力**：提供清晰的 API 接口，便于将浏览器自动化能力集成到现有的企业系统中。

3. **适用场景**
*   **企业级 RPA 升级**：用于自动化填表、数据录入、报表下载等传统规则明确但页面频繁更新的后台任务。
*   **竞品价格监控**：自动访问电商平台，定期抓取商品价格和库存信息，即使页面结构发生变化也能稳定运行。
*   **在线业务流程自动化**：自动化处理注册账号、提交申请、预约服务等需要跨多个网页步骤的用户操作。
*   **测试环境搭建**：作为端到端测试工具，快速生成针对 Web 应用的自动化测试用例。

4. **技术亮点**
*   **Vision + LLM 架构**：创新性地结合了计算机视觉（理解屏幕内容）和大语言模型（规划行动路径），解决了传统自动化工具对静态元素定位依赖过强的问题。
*   **Playwright 底层支持**：基于高性能的 Playwright 引擎构建，确保了浏览器操作的稳定性和速度，同时兼容多种现代浏览器。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22013 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉 AI 数据集的首选平台，提供开源、云及企业级产品。它支持图像、视频和 3D 数据的标注，具备 AI 辅助标注、质量保证及团队协作等功能。

2. **核心功能**
*   支持图像、视频及 3D 数据的多种标注任务。
*   集成 AI 辅助标注以提升数据标注效率与质量。
*   提供团队协作者管理、质量控制及数据分析功能。
*   开放开发者 API，便于集成到现有工作流中。

3. **适用场景**
*   为计算机视觉模型训练构建大规模高质量数据集。
*   需要进行目标检测、语义分割或图像分类的团队作业。
*   利用 AI 加速处理视频或 3D 点云等复杂数据标注。

4. **技术亮点**
*   兼容 PyTorch 和 TensorFlow 等主流深度学习框架生态。
*   提供从开源自托管到企业级全栈解决方案的灵活部署选项。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16159 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级AI可解释性工具包。它广泛支持CNN、Vision Transformer等模型，涵盖分类、目标检测、分割及图像相似度等多种任务。

2. **核心功能**
*   支持多种主流架构，包括卷积神经网络（CNN）和视觉Transformer（ViT）。
*   覆盖丰富的视觉任务，如图像分类、目标检测、语义分割和图像检索。
*   提供多种可视化解释方法，如Grad-CAM、Score-CAM等，以增强模型透明度。
*   专注于提升深度学习模型的“白盒”属性，帮助理解模型决策依据。

3. **适用场景**
*   研究人员需要可视化CNN或ViT模型的注意力区域以验证特征提取逻辑。
*   开发者在部署医疗影像或自动驾驶系统时，需向用户展示AI的判断依据以满足合规要求。
*   机器学习工程师调试目标检测或分割模型时，通过热力图定位误检或漏检原因。

4. **技术亮点**
*   高度模块化设计，兼容PyTorch生态，易于集成到现有项目中。
*   统一接口支持从基础分类到复杂视觉任务的可解释性分析，无需更换核心库。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了一系列可微分的计算机视觉算法和图像处理工具。该库旨在简化深度学习与经典计算机视觉技术的集成与开发流程。

2. **核心功能**
- 提供大量可微分的几何视觉算子，支持端到端的深度学习训练。
- 内置丰富的图像预处理、增强及传统计算机视觉算法模块。
- 深度集成 PyTorch 生态系统，便于快速搭建和调试视觉模型。
- 支持机器人学中的空间感知任务，如相机标定和姿态估计。

3. **适用场景**
- 需要结合传统几何约束进行训练的自定义计算机视觉模型开发。
- 机器人导航与环境感知系统中的实时图像处理与空间定位。
- 对图像数据进行大规模自动化预处理和数据增强的机器学习流水线。
- 探索可微分计算机视觉在自动驾驶或增强现实中的应用研究。

4. **技术亮点**
- 实现了全微分化的计算机视觉管线，使得传统 CV 算法可直接嵌入神经网络进行反向传播优化。
- 拥有活跃的开源社区贡献，涵盖从基础图像处理到高级空间 AI 的多领域应用。
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
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调数据私有性与跨平台兼容性。它采用 TypeScript 开发，旨在让用户以“龙虾方式”（隐喻自由、开放）完全掌控自己的 AI 助理。

2. **核心功能**
- 支持任意操作系统和平台，实现真正的跨设备部署。
- 强调“Own Your Data”（拥有你的数据），保障用户隐私与数据安全。
- 基于 TypeScript 构建，具备良好的可扩展性和社区生态支持。
- 提供个性化的本地化 AI 助手体验，摆脱对中心化服务的依赖。

3. **适用场景**
- 开发者或个人用户希望在本地搭建完全可控的 AI 助手。
- 注重数据隐私的用户希望避免敏感信息上传至第三方云服务。
- 需要在不同操作系统（如 Linux、macOS、Windows）间无缝切换 AI 工具的场景。

4. **技术亮点**
- 采用 TypeScript 编写，兼顾类型安全与开发效率。
- 架构设计支持高度定制化，允许用户根据需求调整助手行为。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380601 | 🍴 79732 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
SuperPowers 是一套经过验证的智能体技能框架与软件开发方法论。它通过“子代理驱动开发”模式，将复杂的软件工程任务分解为可管理的技能模块。该项目旨在利用 AI 智能体自动化头脑风暴、编码及软件开发生命周期（SDLC）中的关键环节。

2. **核心功能**
*   **子代理驱动开发**：利用专门的子代理执行特定任务，实现模块化的自动化编程流程。
*   **全栈 SDLC 支持**：涵盖从需求分析、头脑风暴到代码实现和测试的完整软件开发生命周期。
*   **技能框架集成**：提供标准化的“技能”集合，使 AI 智能体能够像人类专家一样处理复杂工程问题。
*   **交互式协作**：支持人机协同的头脑风暴与决策过程，提升创意生成和问题解决的效率。

3. **适用场景**
*   **快速原型开发**：需要快速构建 MVP 或概念验证项目，利用 AI 加速从想法到代码的转化。
*   **复杂系统架构设计**：在进行大型软件工程时，利用子代理分工协作，优化需求分析与技术选型。
*   **AI 辅助编程工作流**：开发者希望引入自主智能体来接管重复性或结构化的编码任务，提升整体生产力。

4. **技术亮点**
*   采用基于 Shell 脚本实现的轻量级框架，易于集成到现有的 CI/CD 流水线中。
*   首创“obra”方法论，将非结构化的创意想法转化为结构化的、可由智能体执行的开发任务。
- 链接: https://github.com/obra/superpowers
- ⭐ 239384 | 🍴 21240 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款能够伴随用户共同成长并具备自适应能力的智能代理系统。它通过持续的学习与互动，优化自身在复杂任务中的表现，旨在成为开发者可靠的辅助伙伴。该项目集成了多种前沿的大语言模型能力，以提供灵活且强大的自动化解决方案。

### 2. 核心功能
- **自适应成长机制**：代理能够根据用户的交互历史和使用习惯不断优化其行为逻辑。
- **多模型集成支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT) 等多种主流大语言模型后端。
- **代码智能辅助**：提供类似于 Codex 或 Claude Code 的代码生成、理解及调试功能。
- **高度可定制性**：支持用户通过标签和配置自定义代理的行为模式与技能范围。
- **自动化工作流执行**：能够独立处理从简单问答到复杂代码重构的多层级技术任务。

### 3. 适用场景
- **高级编程助手**：用于日常开发中的代码编写、重构建议及 Bug 排查。
- **个性化知识库管理**：作为长期记忆工具，帮助用户整理和检索特定领域的专业知识。
- **自动化研究分析**：辅助进行技术调研、文档总结及信息整合工作。
- **跨平台 AI 代理部署**：适用于需要统一接口管理多个 LLM 模型的开发者环境。

### 4. 技术亮点
- **开源生态丰富**：拥有超过 20 万星标，证明了其在社区中的高活跃度和广泛认可度。
- **模块化架构设计**：清晰分离了核心逻辑与模型接口，便于扩展新的 AI 后端或功能插件。
- **全栈 AI 聚合**：标签涵盖了从底层 LLM 到上层应用（如 ClawdBot, MoltBot）的完整技术栈。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 203727 | 🍴 36546 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个基于公平代码许可的工作流自动化平台，原生集成 AI 能力，支持可视化构建与自定义代码混合开发。它提供超过 400 种集成方式，用户可选择自托管或云端部署，灵活满足各类自动化需求。

2. **核心功能**
*   提供可视化工作流编辑器，支持低代码/无代码快速搭建自动化流程。
*   内置原生 AI 功能，可轻松结合大语言模型实现智能任务处理。
*   拥有庞大的集成生态，预置 400 多种应用接口连接器。
*   支持混合开发模式，允许在可视化节点中嵌入自定义 TypeScript 代码。
*   提供灵活的部署选项，既支持私有化自托管也兼容云端服务。

3. **适用场景**
*   企业级数据同步与业务系统间的 API 自动化集成。
*   利用 AI 助手自动处理客户支持、内容生成或数据分析任务。
*   开发团队构建复杂的后端逻辑工作流，无需依赖重型微服务架构。
*   个人开发者或小型团队实现个人效率提升及智能家居/IoT 设备联动。

4. **技术亮点**
*   采用 TypeScript 编写，类型安全且易于维护和扩展。
*   创新性地将 MCP（Model Context Protocol）客户端与服务端支持纳入核心，增强 AI 上下文交互能力。
*   开源友好且具备公平代码特性，允许用户自由审查和修改代码以适配特定需求。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194177 | 🍴 58854 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，使开发者能够将精力集中在真正重要的事情上。

2. **核心功能**
- 具备自主规划与执行复杂任务能力的 AI 代理架构。
- 支持多种大型语言模型（如 OpenAI GPT、Claude、Llama 等）的后端集成。
- 提供可扩展的工具链，允许用户自定义功能以增强代理能力。
- 具备记忆机制和互联网访问能力，以维持上下文并完成多步骤任务。

3. **适用场景**
- 自动化执行需要多步骤协调的重复性工作流程。
- 作为开发者的基础框架，用于构建特定的垂直领域 AI 助手。
- 探索和研究自主智能体（Autonomous Agents）的行为逻辑与边界。
- 快速原型验证基于大语言模型的复杂任务处理能力。

4. **技术亮点**
- 高度模块化的设计，兼容多种 LLM API 且易于扩展新插件。
- 开源社区驱动，拥有极高的关注度（超 18 万星）和丰富的生态资源。
- 实现了从单一指令到长期目标分解的智能代理闭环。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185160 | 🍴 46131 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164389 | 🍴 21286 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163889 | 🍴 30368 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156634 | 🍴 46147 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150113 | 🍴 9350 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146670 | 🍴 23092 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

