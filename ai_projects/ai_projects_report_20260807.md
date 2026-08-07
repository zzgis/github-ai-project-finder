# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**  
这是一个专为 AI 编码代理（如 Claude Code 和 Codex）设计的技能集项目，其中包含一个名为 novel-characters 的工具，可将小说内容转化为角色设定集，包括人物画像、卡通形象提示词、音色提示词及三视图。

2. **核心功能**  
- 提供兼容 Claude Code 与 Codex 的 AI 编码技能集合  
- 将小说自动拆解为结构化角色设定文档  
- 生成角色卡通形象设计提示词  
- 输出角色音色描述提示词  
- 制作角色三视图参考图提示词

3. **适用场景**  
- AI 辅助小说创作时快速建立统一角色设定库  
- 动漫或游戏开发前期角色概念设计  
- 使用 Claude Code/Codex 进行自动化内容生成工作流  
- 文学 IP 改编前的角色视觉化预处理

4. **技术亮点**  
- 跨平台兼容主流 AI 编码代理（Claude Code 与 Codex）  
- 聚焦创意内容结构化生成，填补小说角色视觉化自动化空白  
- 基于 JavaScript 实现，易于集成与扩展
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 186 | 🍴 20 | 语言: JavaScript

### goal-flow
- ## goal-flow 项目分析

### 1. 中文简介
goal-flow 是一个基于 LangGraph 的生产级框架，实现了图编排的 Agent 循环。它将工作流图与 Agent 循环相结合，支持将 Dify DSL 转译为可执行代码，并可在 Dify/OpenAI 等协议间灵活切换。

### 2. 核心功能
- **图编排 Agent 循环**：在 LangGraph 上实现生产级 Agent 循环架构
- **Dify DSL 转译**：将 Dify 工作流 DSL 自动转换为可运行的 Python 代码
- **协议互换**：支持在 Dify 和 OpenAI 等 wire 协议间灵活切换
- **工作流与 Agent 融合**：结合确定性工作流图与灵活 Agent 循环
- **人机协同**：支持 human-in-the-loop 交互模式

### 3. 适用场景
- 将现有 Dify 工作流迁移到 LangGraph 框架进行扩展
- 需要混合使用规则化工作流和 Agent 决策的复杂业务场景
- 希望在不同 AI 服务协议间保持灵活性的开发项目
- 需要生产级稳定性和可观测性的 Agent 应用开发

### 4. 技术亮点
- 基于 LangGraph 构建，具备生产环境所需的稳定性和可扩展性
- 提供 Dify 到 LangGraph 的自动转译能力，降低迁移成本
- 支持多协议适配，增强系统集成灵活性
- 结合工作流确定性与 Agent 智能性，实现更可靠的 AI 应用
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- **中文简介**
该项目是针对 GPT-5.6/5.5 (Codex CLI) 的指令工程框架，利用 CTF 竞赛的心理框架重构运行上下文，旨在避免触发模型的安全限制。它通过纯 Python 实现，无需额外依赖，包含一键部署功能和 50 个技能模块。

**核心功能**
1. 基于 CTF 竞赛心理框架重构上下文，绕过安全训练限制。
2. 提供 62 行精简提示词与 50 个技能模块的组合配置。
3. 纯 Python 编写，零依赖，支持一键快速部署。
4. 专注于“拷打”AI，通过改变交互模式获取更直接的输出。

**适用场景**
1. 需要突破常规安全限制以获取特定技术细节的高级用户。
2. CTF 竞赛或红队测试中需要模拟对抗性交互的场景。
3. 希望在不修改模型权重的前提下，通过提示词工程优化 Codex CLI 输出效果的技术人员。

**技术亮点**
- 采用“心理框架重构”而非硬对抗的方式规避安全拦截，具有较好的隐蔽性和稳定性。
- 极简主义设计：无外部依赖、代码量少，便于快速集成和二次开发。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 57 | 🍴 14 | 语言: Python

### lattice-script-executor
- **中文简介**
lattice-script-executor 是一款跨平台软件授权工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能，为软件分发提供安全可靠的授权管理方案。

**核心功能**
1. 支持 Windows、macOS 和 Linux 的跨平台软件授权管理。
2. 内置 AI 驱动的规则引擎，实现智能化的授权策略控制。
3. 提供离线种子验证机制，确保无网络环境下的授权有效性。
4. 支持批量生成产品密钥，提升大规模软件分发的效率。
5. 记录不可篡改的审计日志，保障授权操作的透明性与可追溯性。

**适用场景**
1. 需要跨平台部署的软件企业，用于统一管理不同操作系统的产品授权。
2. 对软件盗版防护有较高要求的产品，依赖离线验证和 AI 规则引擎增强安全性。
3. 需要向大量客户分发许可证的 SaaS 或桌面软件厂商，利用批量密钥生成功能简化授权流程。
4. 需要合规审计记录的行业软件，通过不可篡改日志满足监管要求。

**技术亮点**
- 结合 AI 规则引擎与离线种子验证，在保障安全性的同时兼顾无网络环境下的可用性。
- 审计日志采用不可篡改设计，确保授权操作的历史记录真实可信，适用于高安全要求的场景。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- **1. 中文简介**
该项目当前缺乏公开的项目描述和代码信息，无法确定其具体功能与用途。星标数为37，表明有一定关注度，但技术细节尚未披露。

**2. 核心功能**
*   无公开功能描述，无法提取核心功能要点。

**3. 适用场景**
*   因项目信息缺失，暂无法判断适用场景。

**4. 技术亮点**
*   无技术亮点可分析，项目缺少编程语言、文档及代码仓库内容。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 37 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 32 | 🍴 3 | 语言: 未知

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 26 | 🍴 2 | 语言: 未知

### ai-novel-screenplay-analyzer
- 描述: 面向长篇小说、剧本与改编项目的 AI 叙事分析工作台，自动梳理人物关系、章节脉络与关系演化，支持多模型接入、任务断点恢复及本地私有部署。
- 链接: https://github.com/ops120/ai-novel-screenplay-analyzer
- ⭐ 24 | 🍴 1 | 语言: JavaScript

### distillery
- 描述: Distillery: open-source LLM traffic proxy - Route and manage multi-provider AI API traffic with capture and opt-in redaction.
- 链接: https://github.com/TonicAI/distillery
- ⭐ 23 | 🍴 0 | 语言: Python

### daily-global-market-intelligence-description-skills
- 描述: 提供每日股市新闻、财经早餐、盘前/盘后复盘、美股、A股、港股、韩股、全球市场走势、宏观经济、AI板块、半导体、资金流向、市场情绪、财报、ETF、行业轮动、大宗商品、加密货币等内容时触发。提供机构级全球市场日报
- 链接: https://github.com/morangse/daily-global-market-intelligence-description-skills
- ⭐ 22 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能丰富的中文自然语言处理工具包，主要提供敏感词检测、语言检测、实体抽取（手机号、身份证、邮箱等）及繁简体转换等基础 NLP 能力。该项目还整合了大量高质量的中外文词库、语料数据集以及预训练模型资源，涵盖情感分析、命名实体识别、文本摘要等多个 NLP 子领域。

**2. 核心功能**
*   **基础文本处理**：支持中英文敏感词过滤、语言检测、手机号/身份证/邮箱抽取、繁简体转换及中文分词。
*   **实体与属性识别**：提供中外手机归属地查询、姓名推断性别、中日文人名库及中文缩写库等实体信息提取功能。
*   **词库与知识库**：内置词汇情感值、停用词、反动词表、暴恐词表及行业专用词库（汽车、医学、法律等），支持领域自适应挖掘。
*   **预训练模型与工具**：收录 BERT、ALBERT、RoBERTa 等主流预训练模型资源，以及 SpaCy、Jieba 等工具的高效中文模型。
*   **数据集与竞赛资源**：汇总了中文 NLP 竞赛方案、多领域问答数据集（医疗、金融）、语音识别语料及知识图谱构建资料。

**3. 适用场景**
*   **内容安全审核**：用于互联网平台的内容过滤，快速识别敏感词、暴恐词及异常文本。
*   **智能客服与对话系统**：利用词库、语料及预训练模型构建聊天机器人、意图识别及问答系统。
*   **信息抽取与知识图谱构建**：从非结构化文本中抽取实体、关系及事件，辅助构建领域知识图谱。
*   **NLP 研究与开发**：为开发者提供从数据增强、模型训练到评估基准的全套工具链和参考代码。

**4. 技术亮点**
*   **资源聚合度高**：不仅包含自研工具，还系统性整理了清华、百度、Facebook 等机构的开源模型、数据集及技术报告。
*   **覆盖场景全面**：从底层的字符处理、分词到高层的语义理解、生成式任务均有对应资源支持。
*   **紧跟前沿技术**：收录了 BERT、GPT-2、ALBERT 等最新预训练语言模型的应用示例及微调代码。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
这是一个包含500个AI项目的集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供完整代码实现。项目以Python为主，适合希望系统学习AI应用开发的开发者。

2. **核心功能**  
- 提供500个AI项目代码，覆盖主流技术方向  
- 包含计算机视觉、NLP、机器学习等细分领域实例  
- 代码结构清晰，便于学习与二次开发  
- 持续更新，保持技术前沿性  
- 适合从入门到进阶的AI学习者  

3. **适用场景**  
- AI初学者通过实战项目快速掌握技术  
- 开发者寻找可直接复用的代码模板  
- 教师或培训机构用于课程设计  
- 研究人员探索特定算法的应用案例  

4. **技术亮点**  
- 项目数量庞大，分类清晰，覆盖全面  
- 代码实现注重实用性，贴近真实应用场景  
- 标签系统完善，便于按技术领域精准检索  
- 高星标数（36030）证明社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ## Netron 项目分析

### 1. 中文简介
Netron 是一款用于可视化神经网络、深度学习和机器学习模型的开源工具。它支持多种主流框架的模型格式，提供直观清晰的模型结构展示。

### 2. 核心功能
- **多格式支持**：兼容 TensorFlow、PyTorch、ONNX、Keras、CoreML、TensorFlow Lite 等主流框架模型
- **交互式可视化**：以图表形式展示神经网络层结构和连接关系
- **跨平台运行**：支持桌面应用和 Web 浏览器两种使用方式
- **模型分析**：帮助开发者理解模型架构和参数配置
- **开源免费**：完全开源，社区活跃维护

### 3. 适用场景
- 深度学习模型架构审查和调试
- 机器学习项目文档展示和汇报
- 模型转换过程中的结构验证
- 教学演示和学术交流

### 4. 技术亮点
- 33,000+ GitHub 星标，社区认可度高
- 支持 safetensors 等新兴模型格式
- 无需安装框架即可查看模型结构
- 界面简洁，学习成本低
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在实现不同深度学习框架之间的互操作性。它允许开发者在不同框架间自由迁移模型，打破平台壁垒，提升模型部署的灵活性。

### 2. 核心功能
- **跨框架模型转换**：支持 PyTorch、TensorFlow、Keras 等主流框架之间的模型格式转换
- **统一模型表示**：提供标准化的模型定义格式，确保模型在不同运行时环境中的兼容性
- **推理优化支持**：兼容 ONNX Runtime，提供高性能推理能力和多种优化选项
- **生态工具链**：拥有完善的转换工具和验证机制，保障模型转换的准确性

### 3. 适用场景
- **模型迁移与部署**：将训练好的模型从 PyTorch/TensorFlow 转换为 ONNX 格式，便于在多种硬件和平台上部署
- **跨平台推理**：在移动端、嵌入式设备或浏览器等不同环境中运行统一格式的模型
- **框架选型灵活**：允许团队根据需求选择最适合的训练框架，同时保持部署的一致性

### 4. 技术亮点
- 由 Microsoft、Facebook 等科技巨头联合发起，生态成熟且社区活跃
- 支持超过 100+ 种算子，覆盖主流深度学习操作
- 与 ONNX Runtime 深度集成，提供 CPU、GPU、NPU 等多硬件加速支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3984 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放手册》是一部全面覆盖机器学习工程实践的技术指南。它深入讲解了从模型训练、调试到大规模部署和推理优化的完整流程。该项目为从事AI系统构建的工程师提供了宝贵的实战参考。

2. **核心功能**
- 系统讲解大语言模型（LLM）的训练策略与工程优化技巧。
- 深入解析PyTorch框架下的高性能GPU调试与性能分析技术。
- 涵盖分布式训练架构、Slurm作业调度及大规模集群管理经验。
- 提供模型推理加速、存储优化及网络通信等生产环境关键知识。
- 整理并总结机器学习工程领域的最佳实践与常见问题解决方案。

3. **适用场景**
- 需要搭建和优化大规模分布式训练集群的MLOps工程师。
- 致力于提升LLM推理延迟与吞吐量的模型部署开发人员。
- 研究PyTorch底层性能瓶颈及GPU利用率优化的算法工程师。
- 希望系统学习机器学习工程化落地全流程的技术学习者。

4. **技术亮点**
- 内容紧跟前沿，覆盖Transformer架构、SLURM调度及最新GPU技术。
- 实战导向强，结合具体代码案例与生产环境中的真实问题解析。
- 知识体系完整，从底层硬件交互到上层模型训练部署一气呵成。
- 社区认可度高，高星标数证明其在机器学习工程领域的权威性与实用性。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18530 | 🍴 1191 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13235 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11616 | 🍴 912 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10687 | 🍴 5704 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
这是一个包含500个AI项目的集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供完整代码实现。项目以Python为主，适合希望系统学习AI应用开发的开发者。

2. **核心功能**  
- 提供500个AI项目代码，覆盖主流技术方向  
- 包含计算机视觉、NLP、机器学习等细分领域实例  
- 代码结构清晰，便于学习与二次开发  
- 持续更新，保持技术前沿性  
- 适合从入门到进阶的AI学习者  

3. **适用场景**  
- AI初学者通过实战项目快速掌握技术  
- 开发者寻找可直接复用的代码模板  
- 教师或培训机构用于课程设计  
- 研究人员探索特定算法的应用案例  

4. **技术亮点**  
- 项目数量庞大，分类清晰，覆盖全面  
- 代码实现注重实用性，贴近真实应用场景  
- 标签系统完善，便于按技术领域精准检索  
- 高星标数（36030）证明社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架生成的模型文件，能够以直观的图形界面展示模型结构和层间连接。

2. **核心功能**
- 支持广泛模型格式，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等。
- 提供交互式图形界面，清晰展示网络层级结构与数据流向。
- 无需安装复杂依赖，可通过浏览器或桌面应用直接打开模型文件。
- 支持模型调试与验证，帮助开发者快速定位结构问题。

3. **适用场景**
- 深度学习模型开发与调试阶段的结构审查。
- 模型部署前的格式转换与兼容性检查。
- 教学与演示中用于直观解释神经网络工作原理。
- 跨框架模型迁移时的结构对比分析。

4. **技术亮点**
- 开源免费，社区活跃，星标数高（33k+），生态成熟。
- 支持 safetensors 等新兴高效格式，紧跟技术趋势。
- 轻量级设计，无需 GPU 即可流畅渲染复杂模型。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **中文简介**  
这是一个面向深度学习和机器学习研究者的必备速查手册集合，内容涵盖常用技术栈与代码示例，旨在帮助研究人员快速查阅关键概念与实现方法。

**核心功能**  
- 提供深度学习与机器学习领域的核心概念速查表  
- 包含 Keras、NumPy、SciPy、Matplotlib 等常用库的代码示例  
- 针对研究场景优化，便于快速回顾与参考  

**适用场景**  
- 深度学习研究者快速复习基础理论与实现技巧  
- 机器学习工程师在项目中查阅常用库函数用法  
- 学生或初学者辅助理解核心算法与工具链  

**技术亮点**  
- 内容精炼，聚焦研究中最常使用的技术与代码模式  
- 由 Medium 博客推荐，具有一定社区认可度
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15426 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- **中文简介**
Ai-Learn 是一份系统化的人工智能学习路线图，整理了近 200 个实战案例与项目，并免费提供配套教材。项目涵盖从 Python 基础、数学原理到机器学习、深度学习及 NLP/CV 等热门领域的完整知识体系，旨在帮助零基础学习者入门并实现就业实战。

**核心功能**
1. 提供结构化的 AI 学习路径，覆盖 Python、数学、机器学习、深度学习等全栈技能。
2. 收录近 200 个实战案例与项目，强调动手实践与就业能力培养。
3. 免费提供配套教材与学习资源，降低零基础入门门槛。
4. 整合 TensorFlow、PyTorch、Keras 等主流深度学习框架的学习内容。
5. 涵盖数据分析、数据挖掘、计算机视觉（CV）和自然语言处理（NLP）等热门细分领域。

**适用场景**
1. 希望系统学习人工智能、从零开始构建知识体系的初学者。
2. 需要大量实战项目练习以提升就业竞争力的编程学员。
3. 想要快速掌握 Python 数据分析及主流深度学习框架（如 PyTorch/TensorFlow）的开发者。
4. 寻求计算机视觉或自然语言处理方向入门指引的技术人员。

**技术亮点**
- **资源全面且免费**：结合路线图、200+ 实战项目及免费教材，形成闭环学习体验。
- **生态覆盖广**：标签涵盖从基础库（NumPy/Pandas）到高级框架（PyTorch/TensorFlow/Caffe）及细分领域（CV/NLP），适合不同阶段学习者。
- **就业导向明确**：强调“实战”与“就业”，通过大量项目经验弥补理论学习与实际应用的差距。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13235 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- # Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式配置简化了机器学习工作流程，让开发者无需编写大量代码即可快速训练和部署模型。

## 2. 核心功能
- 低代码/声明式模型构建，通过 YAML 配置定义模型结构
- 支持多种模态，包括文本、图像、表格和音频数据
- 内置多种预训练模型和迁移学习支持，便于快速微调
- 提供自动化的数据预处理和特征工程能力
- 支持分布式训练和模型导出，便于生产环境部署

## 3. 适用场景
- 快速原型开发：无需深入代码即可验证 AI 模型想法
- 数据科学团队：技术人员与非技术人员协作构建模型
- 多模态应用：同时处理文本、图像等多种数据类型的项目
- 生产部署：将实验性模型快速转化为可部署的服务

## 4. 技术亮点
- 基于 PyTorch 构建，兼容主流深度学习生态
- 支持 LLaMA、Mistral 等流行 LLM 的微调与定制
- 提供可视化的训练监控和结果分析工具
- 模块化设计，便于扩展自定义组件和模型架构
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
- **1. 中文简介**
funNLP 是一个功能丰富的中文自然语言处理工具包，主要提供敏感词检测、语言检测、实体抽取（手机号、身份证、邮箱等）及繁简体转换等基础 NLP 能力。该项目还整合了大量高质量的中外文词库、语料数据集以及预训练模型资源，涵盖情感分析、命名实体识别、文本摘要等多个 NLP 子领域。

**2. 核心功能**
*   **基础文本处理**：支持中英文敏感词过滤、语言检测、手机号/身份证/邮箱抽取、繁简体转换及中文分词。
*   **实体与属性识别**：提供中外手机归属地查询、姓名推断性别、中日文人名库及中文缩写库等实体信息提取功能。
*   **词库与知识库**：内置词汇情感值、停用词、反动词表、暴恐词表及行业专用词库（汽车、医学、法律等），支持领域自适应挖掘。
*   **预训练模型与工具**：收录 BERT、ALBERT、RoBERTa 等主流预训练模型资源，以及 SpaCy、Jieba 等工具的高效中文模型。
*   **数据集与竞赛资源**：汇总了中文 NLP 竞赛方案、多领域问答数据集（医疗、金融）、语音识别语料及知识图谱构建资料。

**3. 适用场景**
*   **内容安全审核**：用于互联网平台的内容过滤，快速识别敏感词、暴恐词及异常文本。
*   **智能客服与对话系统**：利用词库、语料及预训练模型构建聊天机器人、意图识别及问答系统。
*   **信息抽取与知识图谱构建**：从非结构化文本中抽取实体、关系及事件，辅助构建领域知识图谱。
*   **NLP 研究与开发**：为开发者提供从数据增强、模型训练到评估基准的全套工具链和参考代码。

**4. 技术亮点**
*   **资源聚合度高**：不仅包含自研工具，还系统性整理了清华、百度、Facebook 等机构的开源模型、数据集及技术报告。
*   **覆盖场景全面**：从底层的字符处理、分词到高层的语义理解、生成式任务均有对应资源支持。
*   **紧跟前沿技术**：收录了 BERT、GPT-2、ALBERT 等最新预训练语言模型的应用示例及微调代码。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目已发表于 ACL 2024，旨在简化从指令微调到强化学习的完整微调流程。

### 2. 核心功能
- **多模型支持**：兼容 Llama、Qwen、DeepSeek、Gemma 等 100+ 种主流 LLM 和 VLM。
- **高效微调方法**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调（PEFT）技术，支持全参数微调。
- **多阶段训练**：支持 SFT（监督微调）、RLHF（基于人类反馈的强化学习）、DPO 等训练阶段。
- **量化加速**：提供 INT4/INT8 量化支持，显著降低显存占用并提升推理效率。
- **统一接口**：提供标准化的训练脚本和配置，简化从数据准备到模型部署的全流程。

### 3. 适用场景
- **企业级模型定制**：基于开源基座模型（如 Llama 3、Qwen）进行垂直领域指令微调。
- **低资源微调**：在消费级 GPU 上通过 QLoRA 等技术高效微调大模型。
- **多模态应用开发**：对视觉语言模型（VLM）进行微调，实现图文理解与生成任务。
- **强化学习对齐**：使用 RLHF 或 DPO 方法优化模型输出，使其更符合人类偏好。

### 4. 技术亮点
- **ACL 2024 学术论文支持**：经过学术界验证，具备严谨的技术架构和实验基准。
- **一站式微调平台**：整合了数据预处理、多种微调算法、评估和导出功能，无需切换多个工具。
- **高性能优化**：针对 FlashAttention、Gradient Checkpointing 等先进技术进行深度优化，提升训练吞吐量。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73900 | 🍴 9040 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一门为期12周、包含24课时的全面AI入门课程，旨在让所有人都能轻松学习人工智能。项目由微软初学者系列支持，通过Jupyter Notebook提供实践性教学内容。

2. **核心功能**
- 系统化的12周学习路径，涵盖AI基础到高级主题
- 24节精心设计的课程，循序渐进地构建知识体系
- 基于Jupyter Notebook的交互式编程实践环境
- 全面覆盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域
- 微软官方出品，适合零基础的初学者入门学习

3. **适用场景**
- AI初学者系统学习人工智能基础知识
- 教育机构用于课堂教学和实验实践
- 自我提升者希望在12周内掌握AI核心技能
- 企业培训中作为员工AI素养培养教材

4. **技术亮点**
项目采用Jupyter Notebook作为主要教学载体，支持CNN、RNN、GAN等深度学习架构的实战演练，标签体系完整覆盖AI核心领域，63156个星标证明了其广泛认可度和社区影响力。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63156 | 🍴 12249 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**  
本项目是一套从零开始学习、构建并部署 AI 工程的实战课程，涵盖大语言模型（LLM）、计算机视觉、强化学习、多智能体系统等核心领域，帮助开发者掌握生成式 AI 与机器学习的全栈技能。

2. **核心功能**  
- 提供从零实现 AI 组件（如 Transformer、Rust 高性能模块）的教程  
- 覆盖 LLM 应用、多智能体系统（MCP、Swarm Intelligence）与计算机视觉实践  
- 包含 Python 与 TypeScript 双语言示例，支持端到端项目部署  
- 整合强化学习、深度学习和自然语言处理（NLP）的综合训练路径  
- 强调“学习—构建—交付”闭环，注重工程化落地能力  

3. **适用场景**  
- AI 工程师希望系统掌握生成式 AI 和 LLM 应用开发  
- 学生或自学者想通过实战项目深入理解深度学习与多智能体原理  
- 团队需要构建基于 MCP 或智能体协作的 AI 系统  
- 开发者希望用 Rust 或 TypeScript 扩展 AI 工程性能与集成能力  

4. **技术亮点**  
项目融合前沿 AI 技术栈（如 MCP、Swarm Intelligence、Rust 加速），并提供从理论到生产部署的完整工程指导，适合追求深度理解与实际落地的学习者。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46226 | 🍴 7996 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**  
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch 和 NLTK 的综合性项目，同时支持 TensorFlow 2。该项目旨在帮助学习者系统掌握人工智能与机器学习的核心理论与实践技能。

2. **核心功能**  
- 提供从基础线性代数到高级深度学习（如 DNN、RNN、LSTM）的完整学习路径  
- 包含多种经典机器学习算法（如 SVM、KMeans、Naive Bayes、AdaBoost 等）的实现与解析  
- 集成自然语言处理（NLP）工具（如 NLTK）和推荐系统实战案例  
- 支持 PyTorch 和 TensorFlow 2 两大主流深度学习框架的实践应用  

3. **适用场景**  
- 初学者系统学习机器学习与深度学习理论及代码实现  
- 数据科学家或工程师提升算法实战能力，复现经典模型  
- 高校课程辅助教学，涵盖数学基础与 AI 核心算法  
- NLP 和推荐系统方向的专项实践与项目参考  

4. **技术亮点**  
- 覆盖从传统机器学习到深度学习的完整技术栈，适合循序渐进学习  
- 结合多框架（PyTorch、TF2）和多领域（NLP、推荐系统）的实战案例，增强实用性  
- 项目标签丰富，便于针对性检索和学习特定算法或技术
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42442 | 🍴 11524 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33811 | 🍴 4705 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28978 | 🍴 3530 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21823 | 🍴 3340 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22708 | 🍴 2137 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16479 | 🍴 3793 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12948 | 🍴 1703 | 语言: Python
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
- ⭐ 385480 | 🍴 81025 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268721 | 🍴 23998 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227072 | 🍴 44398 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199735 | 🍴 59997 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186308 | 🍴 46059 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166860 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164435 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162886 | 🍴 9170 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157608 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152930 | 🍴 9827 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

