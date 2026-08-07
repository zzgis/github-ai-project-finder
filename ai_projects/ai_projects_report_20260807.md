# GitHub AI项目每日发现报告
日期: 2026-08-07

## 新发布的AI项目

### shuohao-skills
- 1. **中文简介**  
shuohao-skills 是为 AI 编码 agent 设计的技能集合，兼容 Claude Code 和 Codex。其 novel-characters 模块可将小说内容自动拆解为完整角色设定集，包含人物画像、卡通形象提示词、音色提示词及三视图生成指令。

2. **核心功能**  
- 提供跨平台兼容的 AI 编码技能库，支持 Claude Code 与 Codex 环境。  
- 自动解析小说文本并生成结构化角色设定文档。  
- 输出包含人物画像描述、卡通形象设计提示词、声音特征提示词及三视图生成指令。  
- 通过标准化技能格式提升 AI agent 在创意写作辅助场景下的执行效率。  

3. **适用场景**  
- 网文作者快速构建角色档案体系以辅助创作。  
- AI 辅助小说改编动画/游戏的角色设计前期准备。  
- 自动化生成角色视觉/听觉设定用于营销物料。  

4. **技术亮点**  
- 采用模块化技能设计实现跨 AI 编码平台无缝切换。  
- 整合多模态提示词生成逻辑，支持文本到视觉/听觉特征的自动映射。
- 链接: https://github.com/eternityspring/shuohao-skills
- ⭐ 186 | 🍴 20 | 语言: JavaScript

### goal-flow
- 1. **中文简介**
Goal-flow 是一个基于 LangGraph 的生产级框架，旨在将工作流图与智能体循环相结合。它支持将 Dify DSL 转译为可执行代码，并可在 Dify 和 OpenAI 的协议之间灵活切换，实现高效的 AI 应用编排。

2. **核心功能**
- 基于 LangGraph 构建生产级智能体循环框架。
- 支持将 Dify DSL 自动转译为可运行的 Python 代码。
- 允许在 Dify 和 OpenAI 协议之间进行无缝切换。
- 融合工作流图与智能体循环，支持人机协作（Human-in-the-loop）。

3. **适用场景**
- 需要将 Dify 工作流迁移或集成到 LangGraph 环境中的开发者。
- 希望灵活切换底层 LLM 提供商（Dify/OpenAI）以优化成本或性能的项目。
- 构建复杂多智能体系统，需要结合确定性工作流与自主智能体循环的场景。
- 需要生产级 AI 应用编排框架，以实现更细粒度的流程控制和状态管理。

4. **技术亮点**
- 实现了 Dify DSL 到 LangGraph 代码的自动化转译，降低了迁移门槛。
- 支持协议级抽象，使同一套逻辑可适配不同的大模型服务接口。
- 结合工作流的确定性与智能体的灵活性，提供更具生产力的 AI 编排能力。
- 链接: https://github.com/wanmol/goal-flow
- ⭐ 71 | 🍴 1 | 语言: Python
- 标签: agent, agentic, agentic-ai, agentic-engineering, agentic-framework

### codex-gpt-5.6-5.5-instruct
- 1. **中文简介**
这是一个针对 GPT-5.6 / GPT-5.5 (Codex CLI) 的指令工程框架。它通过 CTF 竞赛心理框架重构运行上下文，旨在从机制上避免模型触发安全拒绝，而非简单压制。该项目提供一键部署方案，包含 62 行提示词和 50 个技能模块，纯 Python 实现且无外部依赖。

2. **核心功能**
- 重构模型运行上下文，绕过安全训练导致的拒绝机制。
- 提供 50 个技能模块，增强 AI 在特定任务中的表现。
- 一键部署，代码精简，仅需 62 行提示词即可运行。
- 纯 Python 实现，零依赖，易于集成和修改。

3. **适用场景**
- 需要突破大模型安全限制以获取特定输出的高级用户。
- 参与 CTF 竞赛或安全研究，需测试模型边界的研究者。
- 希望在不修改模型权重的情况下优化 Codex CLI 行为的开发者。
- 追求轻量级、无依赖 AI 工具链的技术爱好者。

4. **技术亮点**
- 采用“心理框架”而非对抗性攻击，从提示词层面重构上下文。
- 极简架构：纯 Python + 无依赖 + 低代码量，便于快速部署。
- 模块化设计：50 个技能模块支持灵活扩展和组合。
- 链接: https://github.com/lingbol088-spec/codex-gpt-5.6-5.5-instruct
- ⭐ 57 | 🍴 14 | 语言: Python

### lattice-script-executor
- ### 1. 中文简介
Lattice-Script-Executor 是一个跨平台的软件授权工具包，支持 Windows、macOS 和 Linux 系统。它集成了 AI 驱动的规则引擎、离线种子验证、批量产品密钥生成以及不可篡改的审计日志功能。

### 2. 核心功能
- 跨平台授权支持：兼容 Windows、macOS 和 Linux 三大主流操作系统。
- AI 规则引擎：利用人工智能驱动动态授权策略与规则验证。
- 离线种子验证：支持无需网络连接即可验证软件授权的有效性。
- 批量密钥生成：提供高效的产品密钥批量生成与管理能力。
- 不可篡改审计日志：记录所有授权操作，确保数据完整可追溯。

### 3. 适用场景
- 软件开发商需要为多平台应用提供统一的授权管理方案。
- 企业级软件分发场景，需批量生成并管理大量产品密钥。
- 对授权安全性要求高、需离线验证且保留完整操作审计记录的场景。
- 希望借助 AI 动态调整授权规则的智能软件授权系统。

### 4. 技术亮点
- 结合 AI 规则引擎实现智能、灵活的授权策略控制。
- 离线种子验证机制提升了在无网络环境下的授权可靠性。
- 不可篡改审计日志增强了授权系统的透明度与合规性。
- 链接: https://github.com/mathis-wagner1958/lattice-script-executor
- ⭐ 38 | 🍴 0 | 语言: HTML

### 0xsimao-ai
- 1. **中文简介**
该项目描述信息为空，暂无法提供准确简介。

2. **核心功能**
无可用信息。

3. **适用场景**
无可用信息。

4. **技术亮点**
无可用信息。

> 注：由于项目描述为 None 且无标签和编程语言信息，无法进行有效分析。建议检查项目页面获取更详细的内容。
- 链接: https://github.com/0xsimao/0xsimao-ai
- ⭐ 37 | 🍴 12 | 语言: 未知

### anti-slop
- 描述: Design rules to stop AI coding agents from generating generic "AI slop" UI.
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 34 | 🍴 3 | 语言: 未知

### Linguistics_for_ai_engineers
- 描述: 无描述
- 链接: https://github.com/h9-tec/Linguistics_for_ai_engineers
- ⭐ 27 | 🍴 2 | 语言: 未知

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
- 1. **中文简介**
funNLP 是一个全面且功能丰富的中文自然语言处理（NLP）工具包，涵盖了从基础的分词、词性标注到高级的情感分析、实体识别及知识图谱构建。它不仅提供了多种预训练模型和语料库，还集成了敏感词检测、语言识别、手机号/身份证抽取等实用功能，旨在降低 NLP 开发门槛。

2. **核心功能**
- **基础处理与工具**：提供中英文分词、词性标注、句法分析、命名实体识别（NER）、文本分类及情感分析等核心 NLP 功能。
- **数据与资源库**：内置海量中文语料库（如新闻、对话、谣言、医学、法律等）、停用词表、同反义词库及多领域专业词库。
- **信息抽取与识别**：支持敏感词过滤、手机号/身份证/邮箱抽取、繁简转换、中文手写汉字识别及 OCR 文字提取。
- **预训练模型集成**：整合了 BERT、ALBERT、RoBERTa、GPT-2 等多种主流预训练语言模型及其在中文场景下的应用代码。
- **知识图谱与问答**：提供知识图谱构建工具、基于知识图谱的问答系统资源、实体链接及关系抽取等功能。

3. **适用场景**
- **内容安全审核**：用于互联网平台的内容审核，通过敏感词检测、暴恐词表及谣言数据库识别违规内容。
- **智能客服与对话系统**：利用对话语料、聊天机器人框架及 NLU 工具，快速搭建具备语义理解能力的智能客服或闲聊机器人。
- **垂直领域知识挖掘**：适用于医疗、金融、法律等专业领域，通过领域专用词库和 NER 模型进行信息抽取和知识图谱构建。
- **NLP 研究与教学**：为研究者和学生提供丰富的数据集、基准测试（Benchmark）及经典算法的复现代码，助力算法验证与学习。

4. **技术亮点**
- **资源高度集成**：将分散的 NLP 资源（数据、模型、工具）集中管理，极大减少了开发者寻找和配置环境的时间。
- **覆盖中文特色任务**：特别针对中文处理难点（如分词、繁简转换、拼音标注、汉字特征提取）提供了专用解决方案。
- **紧跟前沿技术**：及时更新并整合了 BERT、Transformers 等最新深度学习模型在中文 NLP 领域的应用实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理领域，并提供完整代码实现。它旨在为开发者提供一个全面的学习和实践平台，帮助快速掌握人工智能核心技能。

2. **核心功能**
- 提供500个涵盖AI主要领域的实战项目，包括机器学习、深度学习、计算机视觉和NLP。
- 所有项目均附带完整代码，便于直接运行、学习和二次开发。
- 项目按技术领域分类，结构清晰，方便快速定位所需内容。
- 适合不同水平的学习者，从入门到进阶均可找到对应项目。
- 持续更新，反映AI领域最新实践和技术趋势。

3. **适用场景**
- 学生或初学者系统学习机器学习、深度学习等AI核心技术。
- 开发者寻找高质量实战项目用于简历构建或技术面试准备。
- 研究人员或工程师快速参考计算机视觉、NLP等领域的实现方案。
- 企业培训或团队技术分享中作为项目案例库使用。

4. **技术亮点**
- 项目数量庞大（500个），覆盖AI主流方向，资源集中度高。
- 全部提供代码实现，强调“学练结合”，而非仅理论介绍。
- 标签分类清晰，便于按技术栈（如Python、deep-learning、nlp等）筛选。
- 高星标数（36030）表明社区认可度高，项目质量经过实践检验。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架的模型格式，帮助用户直观地查看模型结构和参数。

**核心功能**
1. 支持 TensorFlow、PyTorch、Keras、ONNX、CoreML 等多种主流模型格式。
2. 提供图形化界面直观展示神经网络结构和数据流向。
3. 支持查看模型权重、张量形状及层参数详情。
4. 可在本地离线运行，无需联网即可加载和分析模型。

**适用场景**
1. 深度学习研究人员快速验证模型结构是否符合预期。
2. 开发者调试模型转换问题（如从 PyTorch 转 ONNX 后结构异常）。
3. 教学演示中直观展示神经网络各层连接关系。
4. 模型部署前检查不同框架间格式转换的完整性。

**技术亮点**
纯 JavaScript 实现，无需安装额外依赖即可在浏览器或桌面端运行，跨平台兼容性强。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在实现不同深度学习框架之间的互操作性。它允许模型在不同平台（如PyTorch、TensorFlow、Keras等）之间无缝转换和部署，提升开发效率并降低跨平台适配成本。

### 2. 核心功能
- **模型格式标准化**：定义统一的模型表示格式，支持跨框架的模型交换。
- **多框架兼容**：兼容PyTorch、TensorFlow、Keras、scikit-learn等主流机器学习框架。
- **部署优化**：提供工具将模型转换为ONNX格式，便于在边缘设备、云服务等场景部署。
- **性能加速**：支持通过ONNX Runtime加速推理，提升模型运行效率。
- **生态扩展**：提供丰富的算子库和转换工具，支持自定义扩展和复杂模型结构。

### 3. 适用场景
- **跨平台模型迁移**：将训练好的模型从PyTorch转换为TensorFlow或反之，适配不同部署环境。
- **边缘设备部署**：将大型模型压缩并转换为ONNX格式，用于移动端或嵌入式设备的高效推理。
- **生产环境加速**：利用ONNX Runtime优化模型推理速度，适用于高并发服务场景。
- **多框架协作开发**：在团队中使用不同框架时，通过ONNX统一模型格式，简化协作流程。

### 4. 技术亮点
- **开放标准**：由微软、Facebook等科技巨头共同推动，成为工业界广泛认可的模型交换标准。
- **高性能推理**：ONNX Runtime支持硬件加速（如CUDA、TensorRT），显著提升推理性能。
- **灵活扩展**：支持自定义算子和插件机制，适应复杂模型需求。
- **社区活跃**：拥有庞大的开发者社区和丰富的文档资源，持续迭代更新。
- 链接: https://github.com/onnx/onnx
- ⭐ 21276 | 🍴 3985 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. **中文简介**
《ml-engineering》是一本关于机器学习工程实践的开源书籍，旨在帮助开发者掌握大规模模型训练、推理和部署的核心技能。项目涵盖从底层硬件配置到上层框架调优的全链路知识，适合希望深入理解 ML 工程细节的技术人员。

---

### 2. **核心功能**
- 提供从零开始构建可扩展机器学习系统的完整指南，包括 GPU 集群管理与网络优化。
- 深入讲解大语言模型（LLM）的训练、微调及推理优化技术，结合 PyTorch 和 Hugging Face Transformers 实践。
- 分享调试分布式训练、性能瓶颈分析与故障排查的实用技巧，覆盖 SLURM 调度器与存储系统。
- 整合 MLOps 最佳实践，帮助团队实现高效模型迭代与生产环境部署。

---

### 3. **适用场景**
- 工程师在搭建大规模分布式训练集群时，需要参考硬件选型与网络拓扑设计。
- 研究人员优化 LLM 推理延迟与吞吐量，寻找量化、并行策略等调优方案。
- 团队推进 MLOps 落地，需统一训练、监控与部署流程的标准化文档。
- 开发者排查 GPU 内存溢出或训练不稳定问题，获取系统级调试方法论。

---

### 4. **技术亮点**
- 内容紧扣前沿技术（如 LLM、Transformer），结合 PyTorch 等主流框架的实战案例。
- 覆盖从底层（GPU/网络）到上层（MLOps/推理优化）的全栈知识，填补工程实践空白。
- 开源协作模式，持续更新社区贡献的调试技巧与性能优化经验。
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
- ⭐ 15427 | 🍴 3376 | 语言: 未知
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
该项目是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理领域，并提供完整代码实现。它旨在为开发者提供一个全面的学习和实践平台，帮助快速掌握人工智能核心技能。

2. **核心功能**
- 提供500个涵盖AI主要领域的实战项目，包括机器学习、深度学习、计算机视觉和NLP。
- 所有项目均附带完整代码，便于直接运行、学习和二次开发。
- 项目按技术领域分类，结构清晰，方便快速定位所需内容。
- 适合不同水平的学习者，从入门到进阶均可找到对应项目。
- 持续更新，反映AI领域最新实践和技术趋势。

3. **适用场景**
- 学生或初学者系统学习机器学习、深度学习等AI核心技术。
- 开发者寻找高质量实战项目用于简历构建或技术面试准备。
- 研究人员或工程师快速参考计算机视觉、NLP等领域的实现方案。
- 企业培训或团队技术分享中作为项目案例库使用。

4. **技术亮点**
- 项目数量庞大（500个），覆盖AI主流方向，资源集中度高。
- 全部提供代码实现，强调“学练结合”，而非仅理论介绍。
- 标签分类清晰，便于按技术栈（如Python、deep-learning、nlp等）筛选。
- 高星标数（36030）表明社区认可度高，项目质量经过实践检验。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36030 | 🍴 7410 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架的模型格式，帮助用户直观地查看模型结构和参数。

**核心功能**
1. 支持 TensorFlow、PyTorch、Keras、ONNX、CoreML 等多种主流模型格式。
2. 提供图形化界面直观展示神经网络结构和数据流向。
3. 支持查看模型权重、张量形状及层参数详情。
4. 可在本地离线运行，无需联网即可加载和分析模型。

**适用场景**
1. 深度学习研究人员快速验证模型结构是否符合预期。
2. 开发者调试模型转换问题（如从 PyTorch 转 ONNX 后结构异常）。
3. 教学演示中直观展示神经网络各层连接关系。
4. 模型部署前检查不同框架间格式转换的完整性。

**技术亮点**
纯 JavaScript 实现，无需安装额外依赖即可在浏览器或桌面端运行，跨平台兼容性强。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 项目分析：cheatsheets-ai

1. **中文简介**
   这是一个专为深度学习和机器学习研究人员设计的必备速查表集合。项目内容源自 Medium 文章，涵盖了 AI 领域常用的工具与库的快速参考指南。

2. **核心功能**
   - 提供机器学习与深度学习领域的核心概念速查表。
   - 整理常用 Python 库（如 NumPy、SciPy、Matplotlib）的关键用法。
   - 包含 Keras 等深度学习框架的实用代码片段。
   - 以简洁的图表或列表形式呈现，便于快速查阅。

3. **适用场景**
   - 研究人员在进行实验时快速回忆 API 用法或数学公式。
   - 学习者作为入门参考，梳理 AI 技术栈的关键工具。
   - 开发者在编码过程中查阅常用库的快捷操作。

4. **技术亮点**
   - 内容高度聚焦于实用工具链，而非理论推导，适合实战场景。
   - 星标数高达 15,427，说明其在社区中具有广泛认可度和高实用性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**  
Ai-Learn 是一个免费的人工智能学习路线图项目，整理了近200个实战案例与项目，配套教材完整，适合零基础入门及就业实战。涵盖Python、机器学习、深度学习、数据分析、计算机视觉、自然语言处理等热门领域。

2. **核心功能**  
- 提供系统化的AI学习路径，从数学基础到高级应用。  
- 包含大量实战案例和项目，帮助学习者动手实践。  
- 支持多种主流AI框架（如PyTorch、TensorFlow、Keras等）。  
- 配套免费教材，适合不同基础的学习者。  
- 覆盖数据分析、深度学习、NLP、CV等多个热门方向。

3. **适用场景**  
- 初学者希望系统学习人工智能并进入相关领域工作。  
- 数据科学家或算法工程师希望提升实战能力。  
- 企业团队用于内部培训或技术分享。  
- 教师或培训机构用于课程设计。

4. **技术亮点**  
- 项目结构清晰，学习路径明确，便于自学。  
- 实战案例丰富，贴近真实应用场景。  
- 免费开源，配套教材完整，降低学习门槛。  
- 支持多框架，满足不同技术偏好。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13235 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它支持多种模态，简化了从数据处理到模型训练、评估及部署的整个机器学习工作流。

2. **核心功能**
- 支持通过 YAML 配置文件快速定义和训练深度学习模型，无需编写大量代码。
- 提供端到端的自动化机器学习（AutoML）功能，包括特征工程、超参数调优和模型评估。
- 兼容多种模型架构，涵盖表格数据、图像、文本、音频及多模态任务。
- 支持主流深度学习框架（如 PyTorch、TensorFlow）及大语言模型微调（如 LLaMA、Mistral）。
- 内置模型解释性工具，帮助用户理解模型预测依据及特征重要性。

3. **适用场景**
- 快速原型开发：数据科学家希望在短时间内验证想法，无需深入底层框架细节。
- 企业级 AI 部署：需要标准化、可复现的模型训练与生产部署流程。
- 多模态 AI 应用：构建同时处理文本、图像和表格数据的复杂智能系统。
- LLM 微调与定制：对开源大语言模型进行领域适配和性能优化。

4. **技术亮点**
- 真正的低代码体验，通过声明式配置大幅降低 AI 开发门槛。
- 强大的数据中心（Data-Centric）支持，强调数据质量对模型性能的影响。
- 原生集成模型可解释性，提升 AI 系统的透明度与可信度。
- 广泛兼容主流开源模型（如 LLaMA、Mistral），便于接入最新研究成果。
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
funNLP 是一个全面且功能丰富的中文自然语言处理（NLP）工具包，涵盖了从基础的分词、词性标注到高级的情感分析、实体识别及知识图谱构建。它不仅提供了多种预训练模型和语料库，还集成了敏感词检测、语言识别、手机号/身份证抽取等实用功能，旨在降低 NLP 开发门槛。

2. **核心功能**
- **基础处理与工具**：提供中英文分词、词性标注、句法分析、命名实体识别（NER）、文本分类及情感分析等核心 NLP 功能。
- **数据与资源库**：内置海量中文语料库（如新闻、对话、谣言、医学、法律等）、停用词表、同反义词库及多领域专业词库。
- **信息抽取与识别**：支持敏感词过滤、手机号/身份证/邮箱抽取、繁简转换、中文手写汉字识别及 OCR 文字提取。
- **预训练模型集成**：整合了 BERT、ALBERT、RoBERTa、GPT-2 等多种主流预训练语言模型及其在中文场景下的应用代码。
- **知识图谱与问答**：提供知识图谱构建工具、基于知识图谱的问答系统资源、实体链接及关系抽取等功能。

3. **适用场景**
- **内容安全审核**：用于互联网平台的内容审核，通过敏感词检测、暴恐词表及谣言数据库识别违规内容。
- **智能客服与对话系统**：利用对话语料、聊天机器人框架及 NLU 工具，快速搭建具备语义理解能力的智能客服或闲聊机器人。
- **垂直领域知识挖掘**：适用于医疗、金融、法律等专业领域，通过领域专用词库和 NER 模型进行信息抽取和知识图谱构建。
- **NLP 研究与教学**：为研究者和学生提供丰富的数据集、基准测试（Benchmark）及经典算法的复现代码，助力算法验证与学习。

4. **技术亮点**
- **资源高度集成**：将分散的 NLP 资源（数据、模型、工具）集中管理，极大减少了开发者寻找和配置环境的时间。
- **覆盖中文特色任务**：特别针对中文处理难点（如分词、繁简转换、拼音标注、汉字特征提取）提供了专用解决方案。
- **紧跟前沿技术**：及时更新并整合了 BERT、Transformers 等最新深度学习模型在中文 NLP 领域的应用实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82329 | 🍴 15271 | 语言: Python

### LlamaFactory
- **中文简介**  
LlamaFactory 是一个统一且高效的微调框架，支持 100+ 种大语言模型（LLM）和多模态模型（VLM）。该框架已发表于 ACL 2024，提供简洁易用的接口，帮助用户快速微调模型。

**核心功能**
- 支持超过 100 种主流大语言模型和多模态模型的统一微调。
- 提供 LoRA、QLoRA 和全量参数微调等多种高效微调策略。
- 内置 RLHF（基于人类反馈的强化学习）和 DPO 等对齐训练功能。
- 支持量化（Quantization）技术，降低显存占用并提升推理效率。
- 集成 Agent 开发能力，便于构建多步骤推理的智能体应用。

**适用场景**
- 研究者或开发者需要对特定领域的 LLM 进行指令微调（Instruction Tuning）。
- 资源受限环境下，通过 QLoRA 和量化技术低成本微调大规模模型。
- 需要将多模态模型（VLM）适配到具体视觉-语言任务中。
- 构建基于大模型的智能体（Agent），实现复杂任务的自动化处理。

**技术亮点**
- **统一架构**：一个框架兼容 diverse 模型（LLaMA, Qwen, DeepSeek, Gemma 等），无需切换工具链。
- **学术背书**：成果发表于顶级会议 ACL 2024，具备较高的可信度和前沿性。
- **高效优化**：深度整合 PEFT（参数高效微调）和量化技术，显著降低训练门槛。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73903 | 🍴 9040 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
这是一个为期12周、包含24节课的AI入门课程，旨在让所有人都能轻松学习人工智能。课程由Microsoft开发，适合零基础的初学者系统掌握AI核心概念。

### 2. 核心功能
- 提供结构化的12周学习计划，每周一课，循序渐进。
- 涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。
- 使用Jupyter Notebook作为主要教学工具，支持交互式学习。
- 包含CNN、RNN、GAN等具体技术专题的实践练习。

### 3. 适用场景
- 零基础学习者希望系统入门人工智能领域。
- 教师或培训机构用于AI课程教学参考。
- 开发者补充AI基础知识，拓宽技术视野。

### 4. 技术亮点
- 微软官方出品，内容权威且更新及时。
- 课程设计兼顾理论与实践，适合动手学习。
- 标签覆盖全面，从基础ML到前沿DL均有涉及。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63165 | 🍴 12250 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 1. **中文简介**  
该项目致力于从零开始学习、构建并部署AI系统，适合希望深入理解AI原理并动手实践的学习者和工程师。通过完整的课程与教程，帮助用户掌握从基础到高级的AI工程技能。

2. **核心功能**  
- 提供从零构建AI系统的完整教程和课程。  
- 涵盖多种AI领域，包括生成式AI、大语言模型（LLM）、计算机视觉和强化学习。  
- 结合Python和Rust等语言，展示高性能实现方式。  
- 支持多智能体系统和 swarm 智能等前沿技术的学习与实现。  
- 强调实际应用，帮助用户将AI系统部署到真实场景中。

3. **适用场景**  
- 希望系统学习AI工程并从基础到实践全面掌握的技术人员。  
- 对生成式AI、LLM或计算机视觉感兴趣的研究者或开发者。  
- 想要探索多智能体系统和 swarm 智能的高级AI爱好者。  
- 需要将AI技术落地到实际项目的工程师或团队。

4. **技术亮点**  
- 融合了深度学习、NLP和强化学习等多个AI子领域的知识。  
- 提供从理论到代码实现的完整路径，强调动手能力。  
- 结合Rust等语言优化性能，体现工程化思维。  
- 注重实际应用，帮助用户将AI系统推向生产环境。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46229 | 🍴 7997 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**  
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch 和 NLTK 的综合性学习项目，基于 TensorFlow 2 构建。该项目适合希望系统掌握机器学习和深度学习技术的开发者与学习者。

2. **核心功能**  
- 提供完整的机器学习算法实现（如 SVM、K-Means、Logistic 回归等）。  
- 集成深度学习框架 PyTorch 和 TensorFlow 2 的实战案例。  
- 包含自然语言处理（NLP）工具包 NLTK 的应用示例。  
- 结合线性代数知识，帮助理解机器学习底层原理。  
- 支持推荐系统、分类、聚类等实际场景的建模与优化。

3. **适用场景**  
- 机器学习初学者系统学习算法理论与代码实现。  
- 数据科学家探索深度学习模型（如 RNN、LSTM）的实际应用。  
- NLP 爱好者研究文本分类、情感分析等任务。  
- 推荐系统开发者尝试基于协同过滤或深度学习的解决方案。

4. **技术亮点**  
项目全面覆盖主流机器学习与深度学习技术，结合理论与实践，适合从基础到进阶的学习需求。
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
- ⭐ 33812 | 🍴 4705 | 语言: Python
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
- 1. **中文简介**
Kornia 是一个面向空间人工智能（Spatial AI）的几何计算机视觉库，专为 PyTorch 设计。它提供可微分的图像处理原语，能够直接在 GPU 上高效运行，从而简化从传统计算机视觉到深度学习的开发流程。

2. **核心功能**
*   提供基于 PyTorch 的可微分几何计算机视觉算子，支持自动微分。
*   实现常见的图像处理变换（如旋转、缩放、透视变换），并支持批量处理。
*   集成传统 CV 算法与深度学习模型，便于端到端的神经网络训练。
*   提供丰富的几何运算工具，用于相机标定、三维重建和位姿估计。
*   与主流深度学习框架无缝集成，支持即时调试和 GPU 加速。

3. **适用场景**
*   构建端到端的视觉神经网络，如可微分渲染或几何感知模型。
*   机器人视觉系统，用于实时姿态估计、SLAM 和空间导航。
*   图像增强与预处理流水线，特别是在需要梯度反向传播的场景中。
*   计算机视觉研究与教学，用于快速原型开发和几何算法验证。

4. **技术亮点**
*   **全可微分设计**：所有几何变换均支持梯度计算，完美适配深度学习训练流程。
*   **GPU 原生加速**：无需 CPU-GPU 数据传输，直接在张量上执行高效运算。
*   **PyTorch 原生集成**：API 设计与 PyTorch 一致，学习成本低，易于嵌入现有项目。
*   **开源社区活跃**：获得 Hacktoberfest 等社区活动支持，持续迭代与维护。
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
- **中文简介**
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，以“龙虾方式”让你完全掌控自己的数据。它强调数据私有性，确保用户拥有并管理自己的 AI 体验。

**核心功能**
- 跨平台兼容，支持任意操作系统运行
- 本地优先的数据架构，确保用户完全掌控数据
- 作为个人 AI 助手提供智能服务
- 开源透明，允许用户自主定制和部署

**适用场景**
- 需要高度数据隐私的个人用户
- 希望在不依赖云服务的情况下使用 AI 助手
- 开发者或技术爱好者想要自定义 AI 功能
- 企业或个人希望私有化部署 AI 解决方案

**技术亮点**
- 基于 TypeScript 构建，兼具性能与开发效率
- 强调“own-your-data”理念，架构设计以数据主权为核心
- 跨平台兼容性使其部署灵活，适应多种环境
- 链接: https://github.com/openclaw/openclaw
- ⭐ 385483 | 🍴 81025 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268729 | 🍴 23998 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227080 | 🍴 44402 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款公平源码（fair-code）工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码结合，提供 400 多种集成，用户可选择自托管或云端部署。

2. **核心功能**
- 提供 400+ 种集成连接，支持丰富的 API 和数据流操作。
- 结合可视化节点构建与自定义代码，实现灵活的工作流编排。
- 支持自托管或云端部署，满足不同场景下的数据隐私与控制需求。
- 内置原生 AI 能力，支持 MCP（模型上下文协议）客户端与服务器。

3. **适用场景**
- 企业级自动化：通过自托管部署，实现内部系统间的安全数据同步与流程自动化。
- AI 应用集成：利用原生 AI 能力和 MCP 支持，快速构建基于大模型的智能工作流。
- 低代码开发：非技术人员可通过可视化界面快速搭建复杂的数据处理与 API 集成流程。

4. **技术亮点**
- 采用 TypeScript 开发，类型安全且易于扩展和二次开发。
- 支持 MCP 协议，便于与主流大模型及 AI 工具无缝集成。
- 公平源码许可，兼顾开源社区的协作性与商业使用的灵活性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199738 | 🍴 59997 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建 AI，实现人工智能的普及化愿景。其使命是提供强大的工具，让用户能够专注于真正重要的事务。

2. **核心功能**
- 支持自主代理（Agent）模式，能够独立执行复杂任务链。
- 集成多种大语言模型（LLM），包括 OpenAI、Claude 和 LLaMA 等。
- 提供可扩展的框架，方便用户基于其构建自定义 AI 应用。
- 具备自动化规划与执行能力，可分解目标并逐步完成。

3. **适用场景**
- 自动化日常任务，如信息检索、数据整理和报告生成。
- 开发智能助手或客服机器人，实现多步骤交互。
- 快速原型验证 AI Agent 概念，测试不同模型效果。
- 研究自主 AI 系统的行为与决策机制。

4. **技术亮点**
- 高度模块化设计，支持灵活集成多种 LLM API。
- 活跃的开源社区，持续迭代与功能扩展。
- 强调“以用户为中心”的工具链，降低 AI 应用开发门槛。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186311 | 🍴 46060 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166861 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164435 | 🍴 30561 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 162891 | 🍴 9170 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157608 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152931 | 🍴 9827 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

