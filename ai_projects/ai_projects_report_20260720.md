# GitHub AI项目每日发现报告
日期: 2026-07-20

## 新发布的AI项目

### textbook-to-note
- ### 1. 中文简介
该项目能将 PDF 教科书转化为基于 AI 搜索的知识库，并生成包含图表引用和完整出处的结构化笔记。它采用本地优先架构，注重节省 Token 消耗，确保数据隐私与成本效益。

### 2. 核心功能
*   **PDF 转结构化笔记**：自动提取文本并生成带有完整引用来源的 Markdown 格式笔记。
*   **AI 知识库检索**：将文档内容转化为可被 AI 搜索引擎索引的知识库，支持智能问答。
*   **图文保留处理**：在转换过程中保留并整合原书中的图表信息，提升笔记完整性。
*   **OCR 文字识别**：针对扫描版或非文本型 PDF，集成 OCR 技术进行文字提取。
*   **本地优先与低成本**：强调本地部署以保障数据安全，并通过优化策略减少 API Token 消耗。

### 3. 适用场景
*   **学生学术研究**：快速整理课程教材和参考文献，建立个人可检索的学习笔记库。
*   **专业文献管理**：研究人员或专业人士将大量 PDF 报告转化为带引用的结构化知识资产。
*   **离线知识沉淀**：需要在本地环境中处理敏感文档，且希望避免数据泄露的用户。
*   **Obsidian/O2 笔记整合**：习惯使用 Obsidian 等双向链接笔记工具的用户，希望批量导入结构化内容。

### 4. 技术亮点
*   **多模态 PDF 解析**：结合 OCR 与 Markdown 转换技术，有效处理复杂排版和图像嵌入。
*   **RAG（检索增强生成）架构**：原生支持 RAG 流程，便于后续接入大语言模型进行深度交互。
*   **生态兼容性**：明确标注支持 Claude Code、Obsidian 等主流开发工具和笔记软件，集成度高。
*   **资源优化设计**：在保持高精度的同时，特别优化了 Token 使用效率，降低长期运行成本。
- 链接: https://github.com/drpwchen/textbook-to-note
- ⭐ 49 | 🍴 14 | 语言: Python
- 标签: claude-code, note-taking, obsidian, ocr, pdf-to-markdown

### mentor
- 1. **中文简介**
Mentor 是一款专为 AI 编程代理设计的会话洞察技能，能够读取本地 Claude Code 和 OpenAI Codex 的历史记录。它通过分析开发者的工作习惯，生成一份详细的 HTML 格式报告，指出构建内容、时间浪费点及具体的改进建议。该技能兼容 Claude Code、Codex 及其他支持技能扩展的智能代理。

2. **核心功能**
- 自动收集并解析本地 AI 编程代理（如 Claude Code 和 OpenAI Codex）的会话历史数据。
- 生成结构化的 HTML 洞察报告，直观展示开发者的工作流与效率瓶颈。
- 提供基于数据分析的具体修复建议，帮助开发者优化后续交互策略。
- 具备广泛的兼容性，可作为插件集成到任何支持技能系统的 AI 代理中。

3. **适用场景**
- AI 辅助编程用户希望回顾过去会话，识别重复性错误或低效操作模式。
- 开发者寻求通过自动化方式提升个人编码生产力，减少在调试或上下文切换上的时间损耗。
- 需要定期生成个人开发复盘报告，以辅助自我改进或团队知识共享的技术人员。

4. **技术亮点**
- 利用 Python 编写，轻量级且易于嵌入现有 AI 代理工作流。
- 采用“技能（Skill）”架构，实现了与主流 LLM 编程工具的非侵入式集成。
- 专注于行为分析与反馈闭环，将原始日志转化为可执行的改进建议。
- 链接: https://github.com/smixs/mentor
- ⭐ 49 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude, claude-code, claude-skill

### zh-humanizer-literary
- 1. **中文简介**
该项目是一个针对 Codex 平台的中文技能包，旨在消除人工智能生成的文本痕迹并提升文学色彩。通过借鉴特定的人类写作风格，它能有效优化中文草稿，使其读起来更加自然、人性化且富有文采。

2. **核心功能**
*   **去 AI 化润色**：识别并修正典型的人工智能行文模式，使语言更贴近真人表达习惯。
*   **文采增强**：注入文学性修辞和更丰富的词汇，提升文本的可读性和感染力。
*   **风格模仿**：汲取“Mengke/好事”等特定人类作者的风格特征，实现个性化写作辅助。
*   **Codex 集成**：作为 Codex Skill 运行，可无缝集成到现有的 AI 写作工作流中。

3. **适用场景**
*   **社交媒体内容创作**：特别适用于小红书等平台，生成更具亲和力和个人风格的文案。
*   **AI 生成文本优化**：对初稿进行二次加工，解决 AI 写作中常见的生硬或模板化问题。
*   **创意写作辅助**：为小说、散文等需要情感共鸣和独特语感的文学作品提供风格化建议。

4. **技术亮点**
*   **特定风格蒸馏**：通过捕捉特定人类作者（如 Mengke）的微观写作特征，实现高精度的风格迁移。
*   **领域专用 Skill**：专注于中文语境下的“去机器感”，而非通用的翻译或摘要，具有垂直领域的深度优化。
- 链接: https://github.com/nihe0909/zh-humanizer-literary
- ⭐ 40 | 🍴 3 | 语言: 未知
- 标签: ai-writing, chinese-writing, codex-skill, humanizer, writing-assistant

### Phosphene
- ### 1. 中文简介
Phosphene 是一个基于 MCP 和 PWA 技术的自托管系统，旨在构建人类与 AI 伴侣之间的情感连接。它通过任务管理、奖励机制及日常互动功能，增强人机关系的深度与持续性。

### 2. 核心功能
*   **自托管架构**：用户可完全掌控数据与部署环境，保障隐私与安全。
*   **MCP 驱动集成**：利用模型上下文协议实现标准化的 AI 交互接口扩展。
*   **PWA 支持**：提供类原生应用的移动体验，支持离线访问与推送通知。
*   **任务与奖励系统**：通过完成特定任务和获取奖励来强化 AI 伴侣的行为模式。
*   **日常互动机制**：设计每日交互流程以维持长期的人机情感纽带。

### 3. 适用场景
*   **高阶 AI 伴侣开发**：为需要深度情感交互和长期记忆的个人化 AI 助手搭建后端。
*   **隐私敏感型应用**：在要求数据不上传云端、完全本地化的场景下部署 AI 服务。
*   **游戏化用户体验**：将任务完成和奖励反馈机制融入 AI 对话中，提升用户参与度。

### 4. 技术亮点
*   **MCP 协议应用**：前沿地采用 MCP 标准，简化了 AI 系统与外部工具及数据的连接复杂度。
*   **PWA 混合特性**：结合 Web 的易部署性与原生 App 的交互体验，降低了用户使用门槛。
- 链接: https://github.com/3lmglow/Phosphene
- ⭐ 31 | 🍴 15 | 语言: TypeScript
- 标签: ai-companion, human-ai-relationship

### video-shotcraft
- 1. **中文简介**
这是专为 Claude Code 和 Codex 打造的 AI 视频技能，基于 Remotion 引擎实现电影级产品视频制作。项目提供了 106 张分镜配方卡、161 个动态预览及生产就绪模板，帮助用户高效生成高质量宣传片。

2. **核心功能**
*   集成 Claude Code/Codex 智能体，通过自然语言指令自动化视频生成流程。
*   内置 106 种专业分镜配方与 161 个动态预览，提供标准化的视觉叙事结构。
*   基于 Remotion 构建生产就绪模板，支持代码化定义视频动画与转场效果。
*   专注产品宣传与促销视频生成，实现从脚本到成片的自动化流水线。

3. **适用场景**
*   电商或 SaaS 产品需要快速制作高质量营销宣传片时。
*   内容创作者希望利用 AI 辅助，批量生成带有特定分镜逻辑的视频素材。
*   开发团队希望在代码环境中集成视频渲染能力，以自动化视频生产流程。

4. **技术亮点**
*   采用“配方卡”理念，将复杂的视频分镜逻辑抽象为可复用的结构化数据。
*   结合 LLM 代码生成能力与 Remotion 的编程式视频渲染，实现高度可控的视觉输出。
- 链接: https://github.com/Vincentwei1021/video-shotcraft
- ⭐ 31 | 🍴 4 | 语言: TypeScript
- 标签: agent-skills, ai-agents, ai-video, claude-code, claude-code-skills

### stem-illustration-skill
- 描述: 面向 STEM（科学、技术、工程、数学）领域的 AI 图像生成 Skill。  生成科研示意图、教学插图、技术架构图等概念性图像，覆盖生物医学、化学、物理、工程、数学 6 大学科。  功能特性 24 个场景模板：信号通路、实验流程、细胞结构、概念信息图、学术海报、机制图、质粒图、机器学习架构等 6 大学科适配：生命科学/医学/化学/物理/工程/数学 4 种风格变体：academic / textbook / infographic / 3d-render
- 链接: https://github.com/liangdabiao/stem-illustration-skill
- ⭐ 30 | 🍴 0 | 语言: Python
- 标签: skill

### Auto-sign-up-grok-dezz
- 描述: Auto-register akun Grok (x.ai) + 9router integration
- 链接: https://github.com/dzDev3/Auto-sign-up-grok-dezz
- ⭐ 24 | 🍴 10 | 语言: Python

### ip-strategist
- 描述: 让任何 AI agent 变身个人 IP 打造策略师的开源 skill · 耳总个人实战经验沉淀 · 诊契行盘闭环 · 不碰剪辑
- 链接: https://github.com/erduo1998-cell/ip-strategist
- ⭐ 19 | 🍴 3 | 语言: Python

### valorant-hack-scripts
- 描述: Valorant hack scripts — collection of Python colorbots, AHK triggerbots, C++ ESP frameworks, and AI aimbots for competitive FPS domination
- 链接: https://github.com/Fixnyacourtyard/valorant-hack-scripts
- ⭐ 16 | 🍴 0 | 语言: HTML

### Li-Translate
- 描述: Open-source AI-powered subtitle generation and natural language translation platform for video and audio.
- 链接: https://github.com/AliAkrami1375/Li-Translate
- ⭐ 14 | 🍴 0 | 语言: Vue
- 标签: agent, agentic-ai, agentic-workflow, ai, ai-video-subtitle

## 热门AI项目

## Machine Learning项目

### funNLP
- ### 1. 中文简介
funNLP 是一个功能极其丰富的中文自然语言处理（NLP）资源集合库，旨在为开发者提供从基础数据处理到前沿模型应用的全面支持。该项目整合了敏感词检测、实体抽取、知识图谱、语音识别语料、预训练模型（如BERT）以及各类垂直领域的专业词库和数据集。它不仅是NLP初学者的入门工具箱，也是研究人员获取高质量中文数据和对比实验基准的重要资源站。

### 2. 核心功能
- **基础NLP工具链**：涵盖中英文敏感词过滤、语言检测、繁简转换、同/反义词库、停用词表及中文分词加速（jieba_fast）。
- **实体与信息抽取**：提供手机号、身份证、邮箱、人名等敏感信息的正则抽取，以及基于BERT、BiLSTM等模型的命名实体识别（NER）和关系抽取工具。
- **多模态与语音处理**：集成中文语音识别（ASR）语料、语音情感分析、OCR文字识别（如cnocr）及音素对齐工具。
- **垂直领域知识库**：收录医学、法律、金融、汽车、古诗词、地名、历史名人等专业领域词库及知识图谱数据。
- **前沿模型与数据集**：汇总了BERT、ERNIE、ALBERT、RoBERTa等预训练模型资源，以及CLUE、CMRC等权威NLP评测基准和竞赛Top方案代码。

### 3. 适用场景
- **企业内容安全审核**：利用敏感词库和情感分析工具，快速构建文本过滤和舆情监控系统。
- **智能客服与对话机器人**：借助对话语料、意图识别工具和知识库，开发具备多轮对话能力的智能助手。
- **垂直行业知识挖掘**：在医疗、金融或法律领域，利用专用词库和实体抽取模型进行非结构化文本的结构化分析。
- **NLP算法研究与教学**：作为学生和研究人员的数据集仓库和Baseline代码参考，加速模型训练与实验验证。

### 4. 技术亮点
- **资源极度聚合**：将分散的开源项目、数据集、论文解读和模型代码集中管理，极大降低了NLP项目的启动门槛。
- **覆盖全生命周期**：从数据清洗（去重、纠错）、标注（实体、情感），到模型训练（预训练、微调）及应用部署（API、Web工具）均有涉及。
- **紧跟技术前沿**：持续更新最新的Transformer架构模型（如GPT-2, BERT variants）及多语言处理工具（如XLM, mBART）。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81914 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目作为一份资源列表，为开发者提供了丰富的实战案例和参考代码。它旨在帮助初学者和专业人士快速入门并深入理解各类人工智能技术。

2. **核心功能**
*   提供500个完整的AI项目示例，覆盖主流算法与模型。
*   集成多种前沿领域，包括机器学习、深度学习、计算机视觉和NLP。
*   附带源代码，便于用户直接运行、学习及二次开发。
*   采用Awesome列表形式组织，结构清晰且易于检索。

3. **适用场景**
*   AI初学者通过实战代码快速掌握机器学习与深度学习基础。
*   研究人员或开发者寻找特定任务（如图像识别、文本分类）的代码实现参考。
*   教育培训机构用于制作AI课程的教学案例和实践作业。
*   企业团队评估不同AI技术在具体业务场景中的可行性与应用潜力。

4. **技术亮点**
*   项目数量庞大且覆盖面广，是综合性极强的AI实战资源库。
*   标签明确，支持按技术领域（CV、NLP等）精准筛选所需内容。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35585 | 🍴 7363 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和调试模型结构。

2. **核心功能**
*   广泛支持包括 TensorFlow、PyTorch、ONNX、Keras 等在内的多种模型格式。
*   提供直观的图形化界面，清晰展示网络层结构与数据流向。
*   允许用户检查权重数值及张量形状，便于模型调试与分析。
*   基于 Web 技术构建，无需安装即可在浏览器中运行，跨平台兼容性好。
*   支持导出模型为静态图片或交互式网页，方便文档记录与分享。

3. **适用场景**
*   **模型调试**：开发者在训练过程中快速定位网络结构错误或维度不匹配问题。
*   **学术交流**：研究人员在论文或报告中生成清晰的专业模型架构图。
*   **代码审查**：团队内部对已部署的深度学习模型进行结构审计和版本对比。
*   **教育演示**：教师或学生用于直观讲解复杂神经网络的内部工作原理。

4. **技术亮点**
*   轻量级且零依赖，仅需浏览器即可运行，极大降低了使用门槛。
*   拥有强大的格式兼容性，统一了不同框架模型的可视化标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33249 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准，旨在打破不同深度学习框架之间的壁垒。它允许模型在不同平台间无缝转换和部署，提升了开发效率与兼容性。

2. **核心功能**
- 定义了一套通用的计算图表示，支持跨框架加载和保存模型。
- 提供从主流框架（如PyTorch、TensorFlow、Keras）到ONNX的模型转换工具。
- 支持在多种推理引擎上高效运行ONNX模型，加速生产环境部署。
- 包含丰富的算子库，覆盖大多数深度学习网络结构所需的基础运算。
- 提供验证工具，确保转换后的模型在数值精度和行为上与源框架一致。

3. **适用场景**
- 需要将PyTorch或TensorFlow训练好的模型部署到非原生支持的环境（如C++服务器或移动端）。
- 希望在一个统一的标准下集成来自不同框架训练的组件或模型。
- 需要在不同硬件加速器（如GPU、NPU、FPGA）上优化模型推理性能。
- 进行跨平台的机器学习原型验证，避免因框架锁定导致的技术债。

4. **技术亮点**
- **开放性与中立性**：由Microsoft、Facebook等巨头共同维护，避免了厂商锁定。
- **广泛的生态支持**：兼容几乎所有主流深度学习框架及推理后端（如ONNX Runtime）。
- **高性能推理**：通过ONNX Runtime等配套工具，可实现显著的推理加速和资源优化。
- 链接: https://github.com/onnx/onnx
- ⭐ 21180 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
   《机器学习工程开放书籍》是一部全面涵盖机器学习工程实践的综合指南。该项目旨在为从事大规模模型训练、推理及运维的专业人士提供系统性的知识参考与最佳实践方案。

2. **核心功能**
   - 深入解析大语言模型（LLM）的训练策略、调试技巧及扩展性优化方法。
   - 提供基于PyTorch和Transformers库的高效模型推理与部署工程实践。
   - 详解分布式计算环境下的基础设施管理，包括GPU集群、Slurm调度及网络存储配置。
   - 涵盖从数据处理到模型评估的全链路Mlops（机器学习运维）工作流规范。

3. **适用场景**
   - 需要从零搭建或优化大规模分布式深度学习训练集群的工程师。
   - 致力于提升大语言模型推理延迟与吞吐量的后端开发团队。
   - 希望系统化掌握机器学习系统工程、调试及性能调优知识的科研人员。

4. **技术亮点**
   - 聚焦于生产级的大规模机器学习工程挑战，填补了理论与实战间的空白。
   - 紧密结合当前主流的LLM生态（如Transformers、PyTorch），提供即插即用的工程解决方案。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18432 | 🍴 1174 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17328 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13161 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11582 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10672 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目作为一份资源列表，为开发者提供了丰富的实战案例和参考代码。它旨在帮助初学者和专业人士快速入门并深入理解各类人工智能技术。

2. **核心功能**
*   提供500个完整的AI项目示例，覆盖主流算法与模型。
*   集成多种前沿领域，包括机器学习、深度学习、计算机视觉和NLP。
*   附带源代码，便于用户直接运行、学习及二次开发。
*   采用Awesome列表形式组织，结构清晰且易于检索。

3. **适用场景**
*   AI初学者通过实战代码快速掌握机器学习与深度学习基础。
*   研究人员或开发者寻找特定任务（如图像识别、文本分类）的代码实现参考。
*   教育培训机构用于制作AI课程的教学案例和实践作业。
*   企业团队评估不同AI技术在具体业务场景中的可行性与应用潜力。

4. **技术亮点**
*   项目数量庞大且覆盖面广，是综合性极强的AI实战资源库。
*   标签明确，支持按技术领域（CV、NLP等）精准筛选所需内容。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35585 | 🍴 7363 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和调试模型结构。

2. **核心功能**
*   广泛支持包括 TensorFlow、PyTorch、ONNX、Keras 等在内的多种模型格式。
*   提供直观的图形化界面，清晰展示网络层结构与数据流向。
*   允许用户检查权重数值及张量形状，便于模型调试与分析。
*   基于 Web 技术构建，无需安装即可在浏览器中运行，跨平台兼容性好。
*   支持导出模型为静态图片或交互式网页，方便文档记录与分享。

3. **适用场景**
*   **模型调试**：开发者在训练过程中快速定位网络结构错误或维度不匹配问题。
*   **学术交流**：研究人员在论文或报告中生成清晰的专业模型架构图。
*   **代码审查**：团队内部对已部署的深度学习模型进行结构审计和版本对比。
*   **教育演示**：教师或学生用于直观讲解复杂神经网络的内部工作原理。

4. **技术亮点**
*   轻量级且零依赖，仅需浏览器即可运行，极大降低了使用门槛。
*   拥有强大的格式兼容性，统一了不同框架模型的可视化标准。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33249 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目汇集了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。内容源自Medium博客文章，旨在为相关领域的研究者提供快速参考的技术文档集合。

2. **核心功能**
*   提供涵盖主流框架（如Keras、NumPy、SciPy）的代码语法速查。
*   整理数据可视化库（如Matplotlib）的关键绘图指令与参数说明。
*   总结机器学习算法理论要点与实现细节，便于快速回顾。
*   整合深度学习常用概念与术语解释，辅助研究人员查阅。

3. **适用场景**
*   深度学习或机器学习研究员在进行代码开发时快速查找API用法。
*   学生或初学者在复习课程知识时作为便携式参考资料。
*   工程师在构建AI模型原型时，快速确认数据处理或可视化配置。
*   技术面试准备期间，快速回顾关键算法和工具链的核心概念。

4. **技术亮点**
*   聚焦于高频使用的Python科学计算栈（NumPy/SciPy/Matplotlib/Keras），实用性极强。
*   以“速查表”形式呈现，信息密度高，极大节省了查阅官方文档的时间。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
该项目是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材。内容涵盖从零基础入门到就业实战的全流程，适合希望系统掌握AI技术的初学者和专业人士。

2. **核心功能**
*   提供系统化的AI学习路径，涵盖Python、数学及各类主流AI框架。
*   收录近200个实战案例和项目，强调动手实践与就业导向。
*   免费提供配套教材和学习资源，降低入门门槛。
*   覆盖数据科学、机器学习、深度学习及自然语言处理等热门领域。

3. **适用场景**
*   零基础用户希望系统学习人工智能及其相关编程语言（如Python）。
*   求职者需要准备面试作品或积累实际项目经验以提升竞争力。
*   数据科学家或工程师希望快速回顾或扩展在CV、NLP等领域的实战技能。

4. **技术亮点**
*   集成了TensorFlow、PyTorch、Keras等多种主流深度学习框架的实战应用。
*   结合了NumPy、Pandas、Matplotlib等经典数据处理与可视化工具的教学。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13161 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11742 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9140 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8933 | 🍴 3103 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6992 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6265 | 🍴 748 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81914 | 🍴 15249 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目已被 ACL 2024 收录，旨在简化从指令微调到强化学习对齐的全流程开发体验。

### 2. 核心功能
*   **多模型统一支持**：无缝兼容 LLaMA、Qwen、Gemma 等百余种开源模型的微调任务。
*   **多样化微调策略**：原生支持 LoRA、QLoRA 及全参数微调，并提供高效的量化训练方案以降低硬件门槛。
*   **全流程对齐优化**：集成 RLHF（基于人类反馈的强化学习）和 DPO 等高级对齐算法，提升模型输出质量。
*   **低资源高效运行**：通过 QLoRA 等技术实现显存友好型训练，使消费级显卡也能运行大规模模型微调。
*   **开箱即用体验**：提供标准化的数据预处理、训练配置和评估工具，大幅降低微调代码的编写复杂度。

### 3. 适用场景
*   **垂直领域模型定制**：在医疗、法律或金融等专业数据集上对基础大模型进行指令微调，使其具备行业特定知识。
*   **低成本个人/企业部署**：利用 QLoRA 等技术，在显存受限的环境下快速构建私有化部署的大模型应用。
*   **多模态能力增强**：针对视觉语言模型（VLM）进行微调，赋予模型更强的图像理解与图文交互能力。
*   **模型对齐与优化**：通过 RLHF 或 DPO 技术调整模型价值观和行为风格，使其输出更符合人类偏好和安全标准。

### 4. 技术亮点
*   **极致轻量化**：结合 BitsandBytes 量化技术与 LoRA/QLoRA，显著降低显存占用，实现高效训练。
*   **高度模块化架构**：设计灵活的数据加载器和插件系统，便于研究人员快速实验新的微调算法。
*   **前沿算法集成**：紧跟学术前沿，内置最新的高效微调方法和对齐算法，保持技术领先性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73399 | 🍴 8960 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- **1. 中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由Microsoft For Beginners支持，通过结构化的教学路径帮助学习者从零开始构建AI技能。

**2. 核心功能**
*   提供系统化的12周学习路径，涵盖从基础到进阶的24个独立课时。
*   基于Jupyter Notebook实现，支持交互式代码执行与实时结果查看。
*   内容覆盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。
*   包含生成对抗网络（GAN）和循环神经网络（RNN）等高级主题的教学。
*   适合零基础用户，注重理论与实践结合的可操作性。

**3. 适用场景**
*   初学者希望系统性地学习人工智能基础概念与技术栈。
*   教育机构或企业团队用于开展内部AI技能培训与科普教育。
*   开发者希望通过动手实践快速掌握CNN、NLP等特定AI模型的应用。
*   对生成式AI（如GAN）感兴趣的研究者进行初步探索与学习。

**4. 技术亮点**
*   采用Jupyter Notebook作为主要载体，实现了代码、文本与可视化结果的无缝整合，极大提升了学习体验。
*   课程结构严谨，将复杂的AI概念拆解为易于消化的短课时，降低了学习门槛。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52476 | 🍴 10628 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42399 | 🍴 11536 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 40398 | 🍴 6708 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35585 | 🍴 7363 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33756 | 🍴 4696 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28724 | 🍴 3506 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25955 | 🍴 2940 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21729 | 🍴 3305 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35585 | 🍴 7363 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22523 | 🍴 2112 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16339 | 🍴 3772 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目专注于计算机视觉领域的先进AI可解释性技术，支持CNN和Vision Transformer等主流架构。它提供了涵盖分类、目标检测、分割及图像相似度等多种任务的可视化工具，旨在提升深度学习模型的透明度与可理解性。

2. **核心功能**
*   支持多种深度学习模型架构，包括卷积神经网络（CNN）和视觉Transformer（ViT）。
*   覆盖广泛的视觉任务，如图像分类、目标检测、语义分割和图像相似度计算。
*   集成多种可视化算法，不仅包含Grad-CAM，还支持Score-CAM和类激活映射（CAM）等方法。
*   提供直观的可视化输出，帮助用户理解模型决策依据，增强对黑盒模型的信任度。

3. **适用场景**
*   **医疗影像分析**：帮助医生和研究人员理解AI在疾病诊断中关注的病灶区域，提高临床可信度。
*   **自动驾驶系统调试**：可视化车辆识别系统对道路物体（如行人、车辆）的关注点，用于优化感知算法。
*   **学术研究与伦理审查**：在发表研究或进行AI伦理评估时，提供模型决策过程的透明化证据。

4. **技术亮点**
*   高度兼容PyTorch框架，并针对最新的Vision Transformer架构进行了优化支持。
*   模块化设计允许用户轻松扩展以支持自定义模型结构和新的可解释性算法。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12919 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个基于 PyTorch 的开源几何计算机视觉库，专为空间人工智能（Spatial AI）设计。它提供了可微分的计算机视觉原语，旨在加速深度学习在视觉任务中的研究与开发。该项目由 OpenCV 团队支持，致力于填补传统计算机视觉与现代深度学习之间的空白。

### 2. 核心功能
*   **可微分图像处理**：提供完全可微分的图像增强、色彩空间转换和几何变换操作，便于集成到神经网络中。
*   **几何与相机模型**：包含针孔相机模型、单应性矩阵估计、基础矩阵计算等核心几何算法。
*   **深度学习集成**：作为 PyTorch 的扩展，无缝对接现有深度学习工作流，支持自动微分和 GPU 加速。
*   **模块化设计**：代码结构清晰，分为图像、几何、形态学和信号处理等多个模块，便于按需调用。
*   **机器人学支持**：内置适用于机器人领域的位姿估计、SLAM 相关函数及传感器数据处理工具。

### 3. 适用场景
*   **自动驾驶与机器人导航**：用于实时处理相机数据，进行物体检测、姿态估计和环境感知。
*   **医学影像分析**：利用可微分操作进行图像配准、分割预处理和多模态数据融合。
*   **增强现实（AR）**：通过精确的相机内参和外参计算，实现虚拟对象与现实场景的准确对齐。
*   **计算机视觉研究**：作为快速原型开发平台，验证新的几何约束或可微分视觉算法。

### 4. 技术亮点
*   **原生 PyTorch 兼容**：无需额外依赖，直接利用 PyTorch 的计算图和硬件加速能力。
*   **OpenCV 背景加持**：由 OpenCV 核心团队参与维护，确保算法的数学严谨性和工业级稳定性。
*   **端到端可训练**：将传统 CV 步骤转化为可微分层，使得整个视觉 pipeline 可以通过反向传播进行联合优化。
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1204 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3458 | 🍴 879 | 语言: C++
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
- ⭐ 2428 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383583 | 🍴 80579 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架及软件开发方法论。它旨在通过结构化的方式提升 AI 辅助编程的效率与质量。该项目为开发者提供了一套可落地的智能体协作流程。

2. **核心功能**
- 提供基于智能体的技能框架，支持复杂的开发任务分解。
- 集成头脑风暴与代码生成能力，辅助创意与技术实现。
- 定义标准化的软件开发生命周期（SDLC）最佳实践。
- 采用子代理驱动开发模式，实现自动化或半自动化的工作流。

3. **适用场景**
- 需要系统化引入 AI 辅助编程的软件开发团队。
- 希望优化 SDLC 流程并提升代码质量的大型项目。
- 利用智能体进行复杂问题头脑风暴与技术架构设计。
- 探索子代理驱动开发（Subagent-Driven Development）模式的实验性项目。

4. **技术亮点**
- 创新性地将“技能”概念化，使 AI 智能体具备更专业的分工协作能力。
- 强调方法论的实用性，提供了从构思到交付的完整闭环指导。
- 链接: https://github.com/obra/superpowers
- ⭐ 258095 | 🍴 23002 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 217678 | 🍴 41040 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个公平代码许可的工作流自动化平台，原生集成 AI 能力，支持通过可视化构建与自定义代码相结合的方式进行开发。它既允许用户自建托管，也提供云端服务，并拥有超过 400 种应用集成。

2. **核心功能**
*   提供可视化的工作流构建界面，降低自动化开发门槛。
*   内置强大的 AI 能力，支持智能任务处理与分析。
*   拥有超过 400 种原生集成，连接各类常用 API 和服务。
*   支持灵活部署，用户可选择自建托管或云端服务。
*   结合低代码与自定义代码功能，满足复杂业务逻辑需求。

3. **适用场景**
*   企业级数据同步：在不同 SaaS 应用之间自动传输和转换数据。
*   智能客服与营销：利用 AI 自动生成内容或响应客户查询。
*   IT 运维自动化：监控服务器状态并自动触发告警或修复脚本。
*   跨系统工作流整合：将分散的业务系统串联成端到端的自动化流程。

4. **技术亮点**
*   采用 TypeScript 开发，保证代码类型安全与高性能。
*   基于 MCP（Model Context Protocol）协议，增强与大语言模型的交互能力。
*   支持 IPAAS（集成平台即服务）架构，提供丰富的集成框架。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197197 | 🍴 59487 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松访问、使用并构建人工智能工具，其愿景是普及 AI 应用。我们的使命是提供必要的工具，让你能够将精力集中在真正重要的事务上。

2. **核心功能**
*   支持多种大型语言模型（如 GPT、Claude、LLaMA），具备高度的兼容性。
*   作为自主智能体，能够独立规划任务并执行复杂的多步骤工作流。
*   提供可扩展的开发框架，方便用户基于现有工具进行自定义构建。

3. **适用场景**
*   自动化执行需要多步推理和连续操作的复杂研究或数据处理任务。
*   开发者利用其开放架构搭建和测试自定义的 AI 代理应用。
*   个人用户通过现成工具简化日常重复性工作流程，提升效率。

4. **技术亮点**
*   原生集成 OpenAI、Anthropic 及 Hugging Face 等主流 LLM API，灵活适配不同性能与成本需求。
*   采用模块化设计，支持社区贡献丰富的插件与扩展功能，生态活跃。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185619 | 🍴 46070 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166068 | 🍴 21469 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164255 | 🍴 30425 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157145 | 🍴 46177 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 153485 | 🍴 8764 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152102 | 🍴 9609 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

