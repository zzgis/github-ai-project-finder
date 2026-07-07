# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- ### TokHub 项目分析报告

**1. 中文简介**
TokHub 是一个专为 OpenAI 兼容接口设计的专属网关系统，集成了 API 中转站的监控、推荐运营及统一管理功能。它支持分层健康探测、实时用量计量、告警审计以及基于 Docker 的自托管部署，旨在提供稳定且可观测的 AI 服务接入体验。

**2. 核心功能**
*   **统一网关管理**：作为 OpenAI 兼容的专属网关，屏蔽底层 API 差异，提供标准化的接口接入。
*   **智能健康监控**：支持分层探测机制与健康评分体系，实时评估 API 节点的可用性与稳定性。
*   **精细化用量计量**：具备详细的用量统计与审计能力，便于追踪资源消耗与生成成本分析。
*   **告警与通知系统**：集成异常检测与告警机制，确保在 API 故障或流量激增时及时响应。
*   **Docker 自托管**：提供容器化部署方案，方便用户快速搭建并自主控制数据与服务环境。

**3. 适用场景**
*   **企业级 AI 应用集成**：需要稳定接入多种大模型 API 并进行统一权限管理和成本控制的开发团队。
*   **API 聚合服务商**：提供多源 AI 接口中转服务，需实时监控各供应商状态并自动切换的健康节点平台。
*   **内部研发测试环境**：希望在本地或私有云环境中快速部署 OpenAI 兼容接口，用于应用开发与调试的技术团队。
*   **高可用性要求场景**：对服务连续性有严格要求，需要健康评分和自动故障转移机制的关键业务系统。

**4. 技术亮点**
*   **分层探测架构**：通过多级健康检查策略，更精准地识别节点状态，避免单点故障影响整体服务。
*   **OpenAI 兼容性**：无缝对接现有生态，使调用方无需修改代码即可适配底层不同的 AI 服务提供商。
*   **全链路可观测性**：将监控、计量、审计与网关功能深度融合，提供从流量入口到后端节点的全景视图。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 143 | 🍴 15 | 语言: TypeScript

### rocketplaneIO
- 1. **中文简介**
这是一个自托管的AI站点可靠性工程（SRE）解决方案，专为Kubernetes环境设计，结合了零侵入式的eBPF可观测性与具备护栏约束的自动修复Copilot。它支持自带大语言模型（BYO-LLM），能够在完全隔离的网络环境中运行，通过自我验证的操作来修复系统问题。

2. **核心功能**
*   基于eBPF实现零侵入式的高性能可观测性监控。
*   集成AI Copilot，通过受控且自我验证的动作自动修复Kubernetes故障。
*   支持BYO-LLM架构，允许用户引入自有大语言模型以适配不同需求。
*   具备离线/气隙（air-gapped）部署能力，确保数据隐私与安全隔离。

3. **适用场景**
*   对数据隐私和合规性要求极高、需要物理或逻辑隔离的企业级Kubernetes集群运维。
*   希望减少监控代理开销，利用eBPF技术实现低资源消耗的可观测性平台。
*   寻求自动化故障响应（AIOps）以减少人工介入的SRE团队，特别是在夜间或非工作时间。

4. **技术亮点**
*   **零侵入式监控**：利用eBPF技术在内核层采集数据，无需修改应用代码或注入重型Agent。
*   **安全自愈闭环**：不仅发现问题，还通过“护栏约束”和“自我验证”机制确保AI修复动作的安全性和准确性。
*   **灵活的大模型集成**：摆脱特定厂商LLM绑定，支持混合云或私有化部署场景下的模型自由组合。
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### sail-skill
- 1. **中文简介**
SAIL V2（安全AI生命周期）作为一个智能体技能，提供了涵盖91项风险的完整目录，用于评估AI及智能体的安全差距、制定安全路线图以及合规检查。该技能支持安装在Claude Code、Codex、ChatGPT、Antigravity以及任何兼容SKILL.md的智能体环境中。

2. **核心功能**
*   提供包含91项风险在内的全面AI与智能体安全差距评估目录。
*   协助生成定制化的AI安全实施路线图。
*   内置合规性检查清单以确保证书符合标准。
*   具备广泛的兼容性，支持多种主流AI编码助手平台。
*   通过标准化技能接口实现即插即用的安全增强功能。

3. **适用场景**
*   在使用Claude Code或ChatGPT等工具进行开发时，快速集成AI安全防护能力。
*   企业需要进行AI系统合规性审计并生成详细的风险检查报告。
*   开发人员希望构建符合安全最佳实践的AI代理或自动化工作流。
*   安全团队需要统一的标准来评估不同AI应用的安全性差距。

4. **技术亮点**
*   实现了跨多个智能体平台（如Claude Code、Codex等）的统一安全技能部署。
*   基于SKILL.md标准，确保了极高的兼容性和易于集成的特性。
- 链接: https://github.com/pillar-labs/sail-skill
- ⭐ 116 | 🍴 0 | 语言: 未知
- 标签: agent-skills, agentic-ai, ai-security, claude-code, claude-code-plugin

### motion-anything
- ### 1. 中文简介
Motion Anything 是一个开源的、以聊天为原生的运动引擎，旨在成为 AI 代理的运动层。用户只需通过自然语言描述想要的动画效果或感受，AI 即可自动生成相应的动画代码并交付。它致力于降低 Motion Design（动态设计）的技术门槛，让非开发者也能轻松创建高质量的 Web 动画。

### 2. 核心功能
*   **自然语言驱动动画**：通过对话式交互，用户输入文字描述即可生成对应的运动图形或动画效果。
*   **Chat-Native 引擎架构**：原生支持聊天界面集成，将 AI 代理作为生成动画的核心逻辑层。
*   **Figma 动画替代方案**：提供超越传统静态设计工具（如 Figma 插件）的动态实现能力，直接产出可运行的代码。
*   **多框架兼容输出**：基于 JavaScript 开发，能够适配 WebGL 等现代 Web 标准，方便集成到前端项目中。

### 3. 适用场景
*   **Web 前端动态营销页面**：快速为产品落地页或促销活动生成吸引人的交互式背景动画或元素动效。
*   **UI/UX 原型演示**：设计师在 Figma 等工具中完成静态稿后，利用该项目快速生成高保真的交互动画原型。
*   **创意内容制作**：社交媒体或博客文章中需要嵌入的轻量级、无需编写复杂代码的视觉特效。

### 4. 技术亮点
*   **LLM 集成与 Agent 模式**：深度整合了 Claude 等大语言模型的能力，利用其语义理解能力将抽象的“感觉”转化为具体的动画参数和代码。
*   **WebGL 渲染支持**：标签中包含 WebGL，暗示其底层可能利用 GPU 加速来实现高性能的复杂图形渲染，区别于简单的 CSS 动画。
*   **开源且低门槛**：作为开源项目，提供了透明的 API 和实现方式，同时通过 Chat-Native 界面屏蔽了底层复杂的动画库（如 GSAP 或 Three.js）的使用难度。
- 链接: https://github.com/nexu-io/motion-anything
- ⭐ 105 | 🍴 9 | 语言: JavaScript
- 标签: ai-agent, animation, claude, design-tools, figma-motion-alternative

### Autonomous-Forge
- 1. **中文简介**
这是一个完全由人工智能构建并维护的自动化仓库，具备自我规划、编码、测试及持续改进的能力。该项目展示了AI在软件开发生命周期中的自主运作潜力。

2. **核心功能**
*   实现项目代码的全自动生成与维护。
*   具备自主进行需求规划与任务分解的能力。
*   集成自动化测试以验证代码质量并发现缺陷。
*   能够根据反馈持续优化和改进自身代码结构。

3. **适用场景**
*   研究AI驱动的软件工程（AISE）和自动化开发工作流。
*   探索代码库的自我修复与自动重构机制。
*   作为构建下一代自演化智能代理或DevOps工具的参考原型。
*   演示或教学如何利用AI工具实现端到端的自动化编程流程。

4. **技术亮点**
*   展现了高度的自主性（Autonomy），无需人工干预即可完成从规划到部署的闭环。
*   体现了AI在复杂逻辑推理和代码迭代中的自我纠错与优化能力。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 87 | 🍴 2 | 语言: Python

### OpenAI4S
- 描述: 9.9 元豆包API复刻 Claude Science
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 64 | 🍴 6 | 语言: Python
- 标签: agent, ai4science, claude-science, mit-license, open-source

### C-SSH
- 描述: Native cross-platform SSH ops: persistent tmux sessions × always-on monitoring × built-in AI assistant. Windows/Android, free forever, open-source soon. 原生跨平台 SSH 运维 · tmux 持久化 · 常驻监控 · 内置 AI 助手
- 链接: https://github.com/suiyuebaobao/C-SSH
- ⭐ 28 | 🍴 4 | 语言: 未知
- 标签: ai, ai-assistant, android, cross-platform, devops

### TripStar-Java
- 描述: TripStar Java 实现版：基于 Spring Boot 4 + Spring AI Alibaba ReactAgent 的 AI 旅行规划后端，支持高德 Tool、小红书内容接入和 Structured Output。
- 链接: https://github.com/LeeFly-cn/TripStar-Java
- ⭐ 26 | 🍴 3 | 语言: JavaScript
- 标签: ai-agent, amap, java, react-agent, spring-ai

### fable5-methodology
- 描述: A transferable, self-enforcing software-engineering methodology for AI coding agents — playbook, skills, contracted subagents, lifecycle hooks, and evals.
- 链接: https://github.com/UnpaidAttention/fable5-methodology
- ⭐ 21 | 🍴 9 | 语言: Shell

### ccmux
- 描述: 🔮 Track all your AI coding agents (Claude Code, Codex, Cursor, ...) in tmux and jump to the one that needs you
- 链接: https://github.com/epilande/ccmux
- ⭐ 20 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, bun, claude, claude-code, cli

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取及多种专业词库资源。它不仅提供了基础的文本处理功能，还涵盖了情感分析、知识图谱构建及语音识别等相关的前沿技术与数据集资源。该项目旨在为开发者提供一站式的中英双语 NLP 解决方案，大幅降低自然语言处理的开发门槛。

2. **核心功能**
*   **基础文本处理**：支持敏感词过滤、中英文语言检测、繁简体转换、标点修复及文本规范化。
*   **实体与信息抽取**：具备手机号、身份证、邮箱、人名（中日韩）、地名、机构名等实体抽取能力，并支持细粒度命名实体识别。
*   **多维词库与知识资源**：内置情感值词典、停用词、同/反义词库、行业专有词库（如医疗、法律、汽车）及大规模人名/地名词库。
*   **高级 NLP 任务支持**：提供句子相似度匹配、文本摘要、关键词抽取、语义角色标注及依存句法分析等算法与工具。
*   **预训练模型与数据集集成**：整合了 BERT、ALBERT、GPT2 等多种预训练模型资源，以及丰富的中文 NLP 数据集（如问答、闲聊、谣言检测）。

3. **适用场景**
*   **内容安全与审核**：用于互联网平台的敏感词过滤、暴恐词识别及舆情监控，确保内容合规。
*   **智能客服与聊天机器人**：利用闲聊语料、意图识别及对话系统工具，构建具备上下文理解和多轮对话能力的智能助手。
*   **垂直领域知识图谱构建**：借助医疗、法律、金融等领域的专用词库和实体抽取工具，快速构建行业知识图谱并进行问答检索。
*   **文本数据分析与挖掘**：适用于电商评论情感分析、新闻摘要生成、用户画像构建（如通过姓名推断性别）等商业智能场景。

4. **技术亮点**
*   **生态资源丰富**：不仅包含核心代码，还汇集了清华 XLORE、百度基准系统、斯坦福 NLP 等顶级学术与工业界资源，堪称中文 NLP 的“百科全书”。
*   **多模态与前沿技术融合**：涵盖从传统 NLP 到深度学习（BERT/Transformer），再到语音识别（ASR）和 OCR 的广泛技术栈，适应多种应用场景。
*   **开箱即用的行业解决方案**：提供了针对医疗、法律、金融等特定领域的预训练模型和标注数据，极大缩短了垂直领域 AI 应用的研发周期。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81660 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码库集合。它涵盖了从基础算法到前沿应用的完整领域，提供了丰富的实战案例。适合希望快速上手并学习各类AI技术实现的开发者参考。

2. **核心功能**
*   提供500个涵盖机器学习、深度学习和NLP等领域的完整代码项目。
*   包含计算机视觉和自然语言处理的具体应用实例。
*   作为“Awesome”列表，整理并分类了高质量的AI开源资源。
*   支持多种AI子领域的入门学习与进阶实践。

3. **适用场景**
*   AI初学者希望通过大量代码示例快速理解不同算法原理。
*   数据科学家寻找特定任务（如图像识别、文本分类）的参考实现。
*   开发者需要构建AI原型时获取现成的代码模板和思路。
*   教育机构用于教学演示，展示机器学习和深度学习在不同场景的应用。

4. **技术亮点**
*   项目数量庞大且分类清晰，覆盖主流AI子领域。
*   强调代码实用性，直接提供可运行的项目源码。
*   作为社区公认的优质资源列表（Awesome List），具有较高的参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35242 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看和理解模型结构。该工具以其轻量级和跨平台特性，成为模型调试与分析的得力助手。

2. **核心功能**
*   支持广泛的主流模型格式，包括 TensorFlow、PyTorch、ONNX、Keras、CoreML 等。
*   提供直观的图形化界面，清晰展示网络层结构、参数及数据流向。
*   支持在浏览器、桌面端或移动端查看模型，无需安装复杂的依赖环境。
*   具备模型探索功能，允许用户交互式地检查特定层或节点的详细信息。
*   兼容 safetensors 等新兴安全存储格式，紧跟技术发展趋势。

3. **适用场景**
*   **模型调试与验证**：开发者通过可视化结构快速定位模型构建错误或参数配置问题。
*   **学术研究与教学**：研究人员利用清晰的图表向同行或学生解释复杂的神经网络架构。
*   **跨平台部署准备**：工程师在将模型从训练框架（如 PyTorch）转换到推理引擎（如 ONNX/TensorRT）前进行结构核对。
*   **模型文档生成**：为开源项目或内部系统生成可视化的模型架构图，便于团队沟通与维护。

4. **技术亮点**
*   **极高的兼容性**：几乎涵盖所有主流的 AI 模型格式，是通用的模型查看器标准。
*   **零依赖启动**：作为纯 JavaScript/Python 应用，无需 GPU 或大型运行时即可运行，部署极其简便。
*   **交互体验优秀**：支持缩放、平移及节点高亮，使复杂深层网络的梳理变得轻松直观。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（开放神经网络交换）是专为机器学习互操作性设计的开放标准。它旨在统一不同深度学习框架之间的模型格式，实现模型在各类环境间的无缝转换与部署。

### 2. 核心功能
- **跨框架兼容性**：支持在PyTorch、TensorFlow、Keras等主流框架之间轻松转换模型。
- **标准化表示**：定义统一的计算图和算子规范，消除不同引擎间的格式差异。
- **高性能部署**：提供高效的运行时环境，优化模型在多种硬件上的推理速度。
- **生态系统集成**：与Scikit-learn等工具链良好结合，覆盖从训练到生产的全流程。
- **开源协作**：由LF AI & Data基金会维护，拥有活跃的社区和广泛的行业支持。

### 3. 适用场景
- **模型迁移**：将基于PyTorch训练的模型转换为ONNX格式以部署至TensorRT或OpenVINO。
- **生产环境部署**：利用统一标准简化多框架混合架构下的模型服务化流程。
- **跨平台推理**：在移动端或嵌入式设备上运行经过优化的ONNX模型。
- **算法研究**：快速验证不同深度学习框架在同一模型结构下的性能差异。

### 4. 技术亮点
- **工业级标准**：由Microsoft、Facebook、Amazon等巨头联合推动，成为事实上的ML互操作行业标准。
- **灵活的工具链**：提供`onnxruntime`等高性能推理引擎及丰富的模型转换工具。
- **可扩展性强**：支持自定义算子和扩展，适应不断演进的新型神经网络架构。
- 链接: https://github.com/onnx/onnx
- ⭐ 21113 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
   《机器学习工程开放书籍》是一本全面介绍机器学习工程实践的开源指南。它涵盖了从模型训练、调试到大规模部署和推理的完整生命周期。该项目旨在帮助工程师构建高效、可扩展且稳定的机器学习系统。

2. **核心功能**
   - 提供大规模分布式训练的最佳实践与架构指导。
   - 深入解析LLM及传统模型的调试技巧与故障排除方法。
   - 详细介绍模型推理优化、服务部署及性能调优策略。
   - 涵盖MLOps全流程，包括数据存储、网络通信及集群管理（如Slurm）。
   - 针对PyTorch和Transformers框架提供具体的工程实现建议。

3. **适用场景**
   - 需要从零搭建或优化大规模深度学习训练基础设施的团队。
   - 致力于降低LLM推理成本并提升响应速度的工程开发人员。
   - 希望解决GPU利用率低、内存溢出等常见ML工程问题的开发者。
   - 寻求建立标准化、可维护的机器学习生产环境的企业技术主管。

4. **技术亮点**
   - 内容紧跟前沿，特别强化了对大语言模型（LLM）工程化的深度覆盖。
   - 强调实战性，提供大量关于硬件选择、网络拓扑及存储优化的具体参数建议。
   - 结构清晰，作为“开放书籍”形式免费共享，便于社区持续贡献与维护。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18259 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17265 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11561 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5706 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码库集合。它涵盖了从基础算法到前沿应用的完整领域，提供了丰富的实战案例。适合希望快速上手并学习各类AI技术实现的开发者参考。

2. **核心功能**
*   提供500个涵盖机器学习、深度学习和NLP等领域的完整代码项目。
*   包含计算机视觉和自然语言处理的具体应用实例。
*   作为“Awesome”列表，整理并分类了高质量的AI开源资源。
*   支持多种AI子领域的入门学习与进阶实践。

3. **适用场景**
*   AI初学者希望通过大量代码示例快速理解不同算法原理。
*   数据科学家寻找特定任务（如图像识别、文本分类）的参考实现。
*   开发者需要构建AI原型时获取现成的代码模板和思路。
*   教育机构用于教学演示，展示机器学习和深度学习在不同场景的应用。

4. **技术亮点**
*   项目数量庞大且分类清晰，覆盖主流AI子领域。
*   强调代码实用性，直接提供可运行的项目源码。
*   作为社区公认的优质资源列表（Awesome List），具有较高的参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35242 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架格式，帮助用户直观地查看和理解模型结构。该工具以其轻量级和跨平台特性，成为模型调试与分析的得力助手。

2. **核心功能**
*   支持广泛的主流模型格式，包括 TensorFlow、PyTorch、ONNX、Keras、CoreML 等。
*   提供直观的图形化界面，清晰展示网络层结构、参数及数据流向。
*   支持在浏览器、桌面端或移动端查看模型，无需安装复杂的依赖环境。
*   具备模型探索功能，允许用户交互式地检查特定层或节点的详细信息。
*   兼容 safetensors 等新兴安全存储格式，紧跟技术发展趋势。

3. **适用场景**
*   **模型调试与验证**：开发者通过可视化结构快速定位模型构建错误或参数配置问题。
*   **学术研究与教学**：研究人员利用清晰的图表向同行或学生解释复杂的神经网络架构。
*   **跨平台部署准备**：工程师在将模型从训练框架（如 PyTorch）转换到推理引擎（如 ONNX/TensorRT）前进行结构核对。
*   **模型文档生成**：为开源项目或内部系统生成可视化的模型架构图，便于团队沟通与维护。

4. **技术亮点**
*   **极高的兼容性**：几乎涵盖所有主流的 AI 模型格式，是通用的模型查看器标准。
*   **零依赖启动**：作为纯 JavaScript/Python 应用，无需 GPU 或大型运行时即可运行，部署极其简便。
*   **交互体验优秀**：支持缩放、平移及节点高亮，使复杂深层网络的梳理变得轻松直观。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究者提供了必备的速查表集合，涵盖了从基础数学库到主流深度学习框架的核心知识。它旨在通过简洁直观的参考指南，帮助研究人员快速回顾关键概念、函数用法及代码示例，从而提升工作效率。

### 2. 核心功能
*   **多框架覆盖**：包含 Keras、PyTorch 等主流深度学习框架的快速参考指南。
*   **基础工具速查**：提供 NumPy、SciPy、Matplotlib 等数据科学基础库的常用函数与操作备忘。
*   **概念精炼总结**：将复杂的机器学习算法和深度学习理论浓缩为易于查阅的要点。
*   **代码片段示例**：附带关键功能的简短代码示例，便于直接复制和应用。

### 3. 适用场景
*   **面试准备**：机器学习工程师或研究员在求职前快速复习核心概念和 API 用法。
*   **开发调试**：在编写代码时忘记特定库函数的参数或语法，作为即时参考工具。
*   **知识梳理**：初学者或跨领域研究者系统化整理深度学习相关的技术栈笔记。

### 4. 技术亮点
*   **轻量级高价值**：无需安装任何依赖，纯文档形式即可获取极高密度的技术信息。
*   **社区驱动更新**：基于 Medium 热门文章衍生，内容紧跟业界主流实践，具有较高的实用性和时效性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，收录了近 200 个实战案例并提供免费配套教材，旨在帮助零基础用户轻松入门并胜任就业实战。项目涵盖 Python、数学基础以及机器学习、深度学习、计算机视觉和自然语言处理等热门技术领域。

2. **核心功能**
*   提供系统化的 AI 学习路径，覆盖从基础到高级的完整知识体系。
*   整合近 200 个实战案例与项目，强化动手实践能力。
*   免费提供配套教材和资源，降低学习门槛，适合零基础开发者。
*   广泛支持主流框架与工具，如 PyTorch、TensorFlow、Keras 及各类数据科学库。
*   内容横跨算法、数据处理、建模及应用开发等多个关键领域。

3. **适用场景**
*   希望从零开始系统掌握人工智能技术的初学者。
*   需要通过大量实战案例提升就业竞争力的求职者。
*   需要快速查阅或复习 Python、机器学习及深度学习相关知识的开发者。
*   寻求高质量免费开源学习资料的教育者或自学者。

4. **技术亮点**
*   资源高度集成，将分散的技术栈（如 Numpy、Pandas、Matplotlib 等）统一纳入学习路线中。
*   强调“实战导向”，通过丰富的项目案例连接理论与实践。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建定制化的大型语言模型（LLM）、神经网络及其他人工智能模型。它通过声明式的配置简化了机器学习工作流，使开发者能够专注于数据而非复杂的底层代码实现。

**2. 核心功能**
*   支持通过声明式 YAML/JSON 配置文件快速定义和训练深度学习模型。
*   内置对多种模态（如文本、图像、表格数据等）的原生支持与自动特征工程。
*   提供直观的可视化界面，用于监控训练进度、评估模型性能及调试超参数。
*   兼容主流深度学习后端（如 PyTorch），并集成迁移学习以加速模型微调。
*   简化从数据预处理到模型部署的全流程，降低 AI 开发门槛。

**3. 适用场景**
*   需要快速原型验证不同神经网络架构或超参数组合的数据科学团队。
*   希望在不深入编写复杂训练循环代码的情况下，对现有 LLM 进行微调的企业用户。
*   处理多模态数据（结合文本、图像和结构化数据）进行综合分析的研究项目。
*   教育场景中用于直观演示机器学习概念和模型工作原理的教学工具。

**4. 技术亮点**
*   **低代码/无代码体验**：极大减少了样板代码，使非资深工程师也能构建复杂模型。
*   **数据-centric 设计**：强调数据质量与配置驱动，而非仅依赖算法调优。
*   **开箱即用的多模态支持**：原生处理 NLP、计算机视觉及表格数据，无需额外集成大量库。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9119 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8918 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6986 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6227 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面的中英文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取及丰富的专业词库资源。该项目不仅提供了基础的文本处理功能，还汇聚了大量开源的预训练模型、数据集及前沿NLP研究案例，是中文NLP开发者的实用工具箱。

2. **核心功能**
*   **基础文本处理**：支持敏感词过滤、中英文混合分割、繁简转换、文本纠错及相似度匹配。
*   **实体与信息抽取**：提供手机号、身份证、邮箱等正则抽取，以及基于BERT等模型的命名实体识别（NER）和关系抽取。
*   **丰富词库资源**：内置中日文人名、行业术语（医疗/法律/汽车等）、情感词典、停用词及同/反义词库。
*   **语音与多模态支持**：涵盖ASR语料生成、中文OCR识别、发音标注及语音情感分析工具。
*   **预训练模型与数据集**：汇集BERT、ALBERT、RoBERTa等主流预训练模型代码，以及各类NLP竞赛数据集和基准测试。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和暴恐词表，快速实现论坛、社交媒体内容的自动化合规审查。
*   **智能客服与对话系统**：基于提供的对话语料、知识图谱QA系统及意图识别工具，构建垂直领域的智能问答机器人。
*   **数据清洗与特征工程**：借助丰富的词向量、实体抽取工具和正则表达式，高效处理非结构化文本数据以构建模型输入。
*   **NLP研究与教学**：作为初学者或研究者，参考其收录的顶级会议代码、论文解读及基准数据集，快速复现算法或了解行业现状。

4. **技术亮点**
*   **生态整合性强**：不仅是工具库，更是NLP资源的聚合平台，涵盖了从传统规则方法到最新深度学习模型的全栈资源。
*   **领域覆盖广泛**：特别强化了医疗、法律、金融等专业领域的词库和数据集，满足垂直行业的精细化处理需求。
*   **紧跟前沿技术**：及时收录了BERT、GPT-2、ALBERT等最新预训练模型的中文适配版本及微调代码，降低技术落地门槛。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81660 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对超过 100 种大语言模型（LLM）和多模态大模型（VLM）进行训练，相关成果已发表于 ACL 2024 会议。它旨在简化从指令微调到强化学习对齐的整个模型优化流程。

2. **核心功能**
*   支持 100+ 种主流 LLM 和 VLM 的统一高效微调。
*   集成多种参数高效微调技术，如 LoRA、QLoRA 及全参数微调。
*   提供从监督微调（SFT）到基于人类反馈的强化学习（RLHF）的全链路训练能力。
*   内置量化与混合专家（MoE）架构优化，显著降低显存占用并提升推理效率。

3. **适用场景**
*   研究人员或开发者需要对特定领域的大模型进行指令微调以提升专业能力。
*   团队希望在不具备大规模算力资源的情况下，通过量化技术快速部署和优化模型。
*   需要利用 RLHF 技术对齐模型输出，使其更符合人类价值观和安全标准。

4. **技术亮点**
*   **高度兼容性**：无缝对接 Hugging Face Transformers 生态，支持极广泛的模型家族。
*   **性能优化**：针对 QLoRA 和 MoE 架构进行了深度优化，实现了在消费级硬件上微调超大模型的可能性。
*   **学术背书**：作为 ACL 2024 的入选项目，其技术架构经过同行评审，具备高度的专业性和可靠性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73042 | 🍴 8927 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个定期更新的仓库，收集并泄露了包括 Anthropic、OpenAI、Google 和 xAI 在内的多家主流 AI 厂商的系统提示词（System Prompts）。内容涵盖了 Claude、ChatGPT、Gemini 等知名模型及其相关工具的内部指令细节。

### 2. 核心功能
*   **多厂商数据聚合**：整合了 Anthropic、OpenAI、Google、xAI 等多家公司的模型系统提示词。
*   **定期自动更新**：保持内容时效性，持续收录新发布模型或工具的泄露提示词。
*   **涵盖主流模型与工具**：不仅包含基础大语言模型，还涉及 Claude Code、Cursor、VS Code 等开发辅助工具。
*   **开源共享资源**：以开放源代码形式提供数据，方便社区访问和提取信息。

### 3. 适用场景
*   **提示词工程研究**：分析师通过对比官方提示词结构，优化自定义 Prompt 的设计策略。
*   **LLM 安全审计**：安全研究人员利用泄露数据测试模型对敏感信息或越狱攻击的防御能力。
*   **竞品技术分析**：开发者通过观察不同厂商的指令约束机制，理解各模型的底层行为差异。

### 4. 技术亮点
*   **全面性**：覆盖了当前市场上几乎所有头部 AI 模型及流行 AI 编程助手的核心指令集。
*   **高频维护**：作为一个活跃维护的项目，能够紧跟各大厂商模型迭代的速度及时更新数据。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52773 | 🍴 8601 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松学习AI知识。该项目由微软发起，通过结构化的教学计划帮助初学者从零掌握人工智能核心概念。

2. **核心功能**
- 提供系统化的12周学习路径，涵盖从基础到进阶的24个独立课程模块。
- 基于Jupyter Notebook实现交互式编程教学，便于用户动手实践代码。
- 内容广泛覆盖机器学习、深度学习、计算机视觉及自然语言处理等主流AI领域。
- 包含卷积神经网络（CNN）、循环神经网络（RNN）和生成对抗网络（GAN）等具体技术讲解。
- 面向零基础学习者设计，强调“人人可学”的低门槛教育理念。

3. **适用场景**
- 计算机科学或相关专业的学生用于补充课堂理论知识的实践练习。
- 希望转行进入AI领域的职场人士进行的系统化自学与技能提升。
- 教师或培训机构用于开展人工智能基础工作坊或短期培训课程。
- 对AI感兴趣但缺乏编程基础的普通大众进行科普式入门学习。

4. **技术亮点**
- 采用Jupyter Notebook作为主要载体，实现了理论与代码演示的高度融合。
- 课程内容紧跟AI前沿技术，同时兼顾经典算法如CNN、RNN和GAN的教学。
- 依托微软开源社区支持，拥有极高的社区活跃度（超5万星标）和丰富的教学资源。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51855 | 🍴 10473 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深入讲解线性代数、PyTorch及TensorFlow 2等核心框架。它结合了自然语言处理（NLTK）等工具，为学习者提供从理论基础到代码实践的完整路径。

2. **核心功能**
*   **算法实战**：包含Adaboost、Apriori、FP-Growth、K-Means、Logistic回归、朴素贝叶斯、PCA、SVD和SVM等多种经典算法的实现与应用。
*   **深度学习框架**：提供基于PyTorch和TensorFlow 2（TF2）的深度神经网络（DNN）、循环神经网络（RNN/LSTM）等模型的搭建与训练。
*   **自然语言处理**：集成NLTK库，支持NLP领域的文本分析与处理任务。
*   **推荐系统**：涵盖推荐系统的核心逻辑与实现方法。
*   **数学基础**：强化线性代数等机器学习必备数学知识的学习。

3. **适用场景**
*   **机器学习初学者入门**：适合希望系统掌握从基础算法到深度学习全流程的学习者。
*   **高校课程辅助**：作为数据科学、人工智能相关课程的补充实践材料。
*   **面试准备**：帮助求职者复习常见的机器学习算法原理及Python代码实现。

4. **技术亮点**
*   项目拥有较高的社区关注度（42360颗星），验证了其内容的实用性和广泛认可度。
*   技术栈全面，同时覆盖传统机器学习（scikit-learn）、现代深度学习框架（PyTorch/TF2）以及特定的NLP工具（NLTK）。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42360 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37583 | 🍴 6259 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35242 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33721 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28401 | 🍴 3451 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25842 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个人工智能相关项目的精选合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域，并附带完整代码实现。该项目旨在为开发者提供一个全面的资源库，方便快速查找和参考各类AI实战案例。

2. **核心功能**
*   提供海量（500+）经过筛选的高质量AI项目实例。
*   覆盖机器学习、深度学习、CV和NLP等主流人工智能子领域。
*   所有项目均附带可运行的源代码，支持即拿即用。
*   作为“Awesome”列表，具有高度的分类整理和社区认可度。

3. **适用场景**
*   AI初学者通过阅读和运行代码快速掌握各领域的核心概念。
*   数据科学家或算法工程师寻找特定任务（如图像分类、文本生成）的参考实现。
*   团队进行技术选型时，评估不同AI解决方案的可行性和代码质量。
*   研究人员跟踪人工智能领域的最新开源项目和实践趋势。

4. **技术亮点**
*   项目规模庞大且分类清晰，是一站式学习AI多领域的优质资源库。
*   强调“带代码”的实践性，不仅限于理论介绍，更侧重工程落地能力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35242 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一个基于人工智能的自动化平台，能够模拟人类操作来执行复杂的浏览器工作流。它利用视觉理解和大型语言模型（LLM），通过 Playwright 等工具实现对网页界面的精准控制与交互。

### 2. 核心功能
*   **AI 驱动的视觉理解**：结合计算机视觉与大模型，自动识别页面元素并理解界面布局，无需依赖固定的 CSS 选择器或 XPath。
*   **自然语言工作流定义**：用户只需提供简单的自然语言指令，Skyvern 即可自动生成并执行相应的浏览器操作步骤。
*   **跨平台浏览器自动化**：底层基于 Playwright 构建，支持多种浏览器引擎，兼容 Puppeteer 和 Selenium 的传统 RPA 需求。
*   **智能异常处理与重试**：具备自我修复能力，当页面加载失败或元素未找到时，能自动调整策略并重试，提高任务成功率。
*   **结构化数据提取**：能够从非结构化的网页内容中准确提取关键信息，并将其转化为标准化的 JSON 或 CSV 格式。

### 3. 适用场景
*   **企业级 RPA 流程自动化**：替代传统 Selenium 脚本，用于自动化处理 ERP、CRM 等企业内部系统的复杂表单填写和数据录入任务。
*   **电商数据监控与采集**：批量抓取竞争对手价格、库存变化或生成销售报告，适应电商网站频繁的前端结构变更。
*   **政府及公共服务办理**：自动化完成在线报税、许可证申请、资格认证等需要多步跳转和验证码处理的政务流程。
*   **测试环境回归验证**：作为 QA 团队的辅助工具，快速编写和运行基于自然语言描述的 UI 自动化测试用例。

### 4. 技术亮点
*   **Vision-Language Model (VLM) 集成**：不同于传统规则引擎，Skyvern 引入视觉语言模型直接“观看”屏幕，解决了动态渲染和反爬虫机制带来的定位难题。
*   **无头/有头模式灵活切换**：支持在无头模式下高效运行，也可在有头模式下进行可视化调试，便于开发者排查自动化逻辑问题。
*   **低代码/零代码门槛**：通过自然语言接口降低了浏览器自动化的开发难度，使非技术人员也能创建和维护自动化工作流。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22148 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉AI数据集的首选平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API等功能。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注。
*   集成AI辅助标注以显著提升数据处理效率与准确性。
*   提供完善的团队协作、质量控制及数据分析功能。
*   开放开发者API，便于与现有机器学习工作流集成。

3. **适用场景**
*   构建大规模计算机视觉训练数据集（如目标检测、语义分割）。
*   深度学习团队进行多人协作的图像或视频标注任务。
*   需要自动化辅助加速标注流程的AI研发项目。

4. **技术亮点**
*   采用Python开发，原生兼容PyTorch和TensorFlow等主流深度学习框架。
*   提供开源、私有云及企业版多种部署模式，满足灵活的安全与合规需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16244 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目是一款面向计算机视觉的高级可解释性AI工具，支持CNN、Vision Transformer等多种模型架构。它提供了包括分类、目标检测、分割及图像相似度在内的多种可视化方法，旨在提升深度学习模型的透明度与可理解性。

2. **核心功能**
- 支持Grad-CAM、Score-CAM等多种类激活映射算法以生成可视化热力图。
- 兼容卷积神经网络（CNN）和视觉Transformer（ViT）等主流深度学习模型。
- 广泛应用于图像分类、对象检测、语义分割及图像相似度计算等任务。
- 提供直观的解释性工具，帮助用户深入理解模型的决策依据。

3. **适用场景**
- 研究人员需要验证或调试深度学习模型在特定类别上的关注区域是否正确。
- 医疗影像分析中，医生希望直观看到AI模型用于诊断的关键病灶部位。
- 自动驾驶系统开发中，工程师需理解车辆识别模型对道路物体的感知逻辑。
- 合规性审计需求下，展示AI决策过程以满足可解释人工智能（XAI）的法律或伦理标准。

4. **技术亮点**
- 高度模块化设计，轻松适配PyTorch生态下的各类自定义模型结构。
- 统一接口支持多种前沿的可解释性算法，无需为每种算法重写代码。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12901 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它提供了可微分的计算机视觉原语，旨在简化深度学习与经典计算机视觉算法的集成过程。该项目通过支持 GPU 加速和张量操作，为研究人员和开发者提供了高效的图像处理工具链。

### 2. 核心功能
*   **可微分计算机视觉算子**：提供完全可微分的几何变换、滤波器和特征提取模块，便于嵌入神经网络进行端到端训练。
*   **原生 PyTorch 集成**：深度适配 PyTorch 生态，直接支持 Tensor 操作，无需复杂的格式转换即可实现 GPU 加速。
*   **丰富的图像预处理与增强**：内置多种常用的图像校正、色彩空间转换及数据增强方法，提升模型鲁棒性。
*   **传统 CV 算法的现代化实现**：重新实现了霍夫变换、SIFT、SURF 等经典算法，使其具备自动微分能力以用于深度学习任务。

### 3. 适用场景
*   **神经渲染与三维重建**：利用可微分相机模型和投影操作，优化 3D 场景参数以生成高质量渲染图像。
*   **机器人视觉导航**：在实时机器人系统中处理摄像头输入，进行姿态估计、SLAM（同步定位与地图构建）等任务。
*   **医学影像分析**：对 CT、MRI 等医学图像进行精确的空间配准、分割前的预处理及形态学操作。
*   **自动驾驶感知系统**：处理多传感器融合数据，执行车道线检测、物体检测前的几何校正及图像增强。

### 4. 技术亮点
*   **硬件加速与性能优化**：充分利用 CUDA 和 GPU 并行计算能力，显著提升了传统计算机视觉算法在大规模数据集上的运行速度。
*   **自动化微分支持**：所有核心算子均支持自动求导，允许将几何约束直接作为损失函数的一部分纳入模型训练流程。
- 链接: https://github.com/kornia/kornia
- ⭐ 11269 | 🍴 1195 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3275 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2622 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2415 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，致力于让用户以“龙虾”般的自由方式完全掌控自己的数据。它强调本地化部署与隐私保护，确保用户拥有对个人 AI 服务的绝对控制权。

2. **核心功能**
*   跨平台兼容，可在任何主流操作系统上运行。
*   强化数据主权，支持用户完全拥有和控制个人数据。
*   提供个性化的 AI 助手体验，适应不同用户的使用习惯。
*   基于 TypeScript 构建，具备良好的可扩展性和开发友好性。

3. **适用场景**
*   注重隐私安全、希望将 AI 服务本地化的个人用户。
*   需要在非标准或特定操作系统环境中部署 AI 助手的开发者。
*   追求数据自主权，不愿将个人数据交由第三方云服务处理的用户。

4. **技术亮点**
*   采用 TypeScript 语言开发，兼顾类型安全与开发效率。
*   架构设计灵活，强调“Own Your Data”理念，便于定制和私有化部署。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382094 | 🍴 80151 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架与软件开发方法论。它通过整合 AI 代理技能，旨在优化从头脑风暴到代码实现的全生命周期流程。该项目致力于提供一种切实可行且高效的智能开发范式。

2. **核心功能**
- 提供基于代理的技能框架，支持自动化任务执行。
- 集成头脑风暴与创意生成工具，辅助前期规划。
- 覆盖软件开发生命周期（SDLC），实现全流程赋能。
- 采用子代理驱动开发模式，提升复杂任务的分解与处理能力。

3. **适用场景**
- 需要加速原型设计与创意构思的敏捷开发团队。
- 希望利用 AI 代理自动化部分编码和测试流程的工程部门。
- 寻求结构化方法论来整合大型语言模型进行软件构建的组织。
- 从事复杂系统设计，需借助子代理协同工作的研究项目。

4. **技术亮点**
- 创新性地将“技能”概念模块化，便于复用和扩展。
- 强调“实际有效”的方法论，注重落地性与工作流整合。
- 支持子代理驱动的开发架构，实现更细粒度的 AI 协作。
- 链接: https://github.com/obra/superpowers
- ⭐ 248597 | 🍴 22074 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一款基于 Python 构建的智能代理工具，旨在作为用户的数字助手伴随成长。它通过整合先进的 LLM 能力，提供高度自动化和个性化的代码辅助与任务执行体验，能够根据用户习惯不断优化其交互模式和服务深度。

### 2. 核心功能
*   **多模型兼容支持**：无缝集成 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 等多种主流大语言模型 API。
*   **自适应智能代理**：具备“成长”特性，能根据用户反馈和使用历史动态调整行为策略与服务范围。
*   **全栈代码协作**：提供上下文感知的代码生成、重构、调试及解释功能，支持复杂项目结构的理解。
*   **自然语言交互界面**：允许用户通过日常对话指令直接执行编程任务或管理开发工作流。
*   **隐私与安全优先**：设计上注重本地数据处理能力，确保敏感代码和用户数据的安全性。

### 3. 适用场景
*   **开发者日常编码辅助**：用于快速生成样板代码、修复 Bug 或解释复杂逻辑，提升开发效率。
*   **个人知识管理与研究**：作为智能助手帮助用户整理文档、总结长篇技术文章或进行资料检索。
*   **自动化工作流执行**：替代重复性手动操作，如自动提交代码、运行测试套件或管理项目依赖。
*   **学习新框架/语言**：针对初学者或转型者，提供实时的概念解释和最佳实践指导。

### 4. 技术亮点
*   **轻量级架构**：基于 Python 构建，依赖少且易于部署，适合各种环境快速集成。
*   **模块化设计**：允许用户灵活选择后端 AI 模型或扩展特定功能插件，满足不同定制化需求。
*   **高星标社区认可**：拥有超过 21 万星标的活跃度证明其在 AI Agent 领域的广泛影响力和实用性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210905 | 🍴 38713 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码进行开发。它提供超过 400 种集成方式，用户可选择自托管或云端部署，兼具低代码与无代码特性。

### 2. 核心功能
*   提供可视化拖拽界面与自定义代码编写相结合的工作流构建能力。
*   内置原生 AI 功能，支持智能处理复杂的数据流和逻辑判断。
*   拥有 400 多种预置集成连接，覆盖主流 API 和 SaaS 服务。
*   支持灵活部署模式，既可自托管以保障数据隐私，也可使用云服务。
*   兼容 MCP（Model Context Protocol）客户端与服务端，增强 AI 模型交互能力。

### 3. 适用场景
*   **企业级 API 集成**：无需大量编码即可连接多个内部系统或第三方 SaaS 服务。
*   **AI 驱动自动化**：利用原生 AI 能力自动处理文档、生成内容或进行数据分析。
*   **数据流水线编排**：通过可视化方式设计复杂的数据提取、转换和加载（ETL）流程。
*   **自定义后端服务**：结合低代码快速原型开发与自定义代码实现特定业务逻辑。

### 4. 技术亮点
*   **MCP 协议支持**：原生支持 Model Context Protocol，便于扩展 AI 模型的上下文访问能力。
*   **TypeScript 架构**：基于 TypeScript 开发，保证代码类型安全且易于维护和扩展。
*   **混合开发模式**：完美融合“无代码”快速上手与“自定义代码”深度定制的优势。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195553 | 🍴 59150 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185420 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165025 | 🍴 21363 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164025 | 🍴 30395 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156863 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151310 | 🍴 9466 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148072 | 🍴 23323 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

