# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- 1. **中文简介**
TokHub 是一款基于 TypeScript 开发的 OpenAI 兼容专属网关系统，兼具 AI API 中转站的监控、推荐运营与流量管理能力。它支持分层健康探测、用量计量及告警审计，并允许用户通过 Docker 进行私有化自托管部署。

2. **核心功能**
- 提供符合 OpenAI 标准的专属网关接口，确保兼容性。
- 集成中转站监控与推荐运营机制，优化 API 渠道选择。
- 支持分层探测与健康评分算法，实时评估接口可用性。
- 具备精细化的用量计量、告警通知及操作审计功能。
- 完全支持 Docker 容器化部署，实现本地或服务器自托管。

3. **适用场景**
- 企业或开发者搭建私有化 AI 服务网关，以集中管理多个 API 提供商。
- 需要实时监控中转站健康状况并自动切换优质接口的运营团队。
- 希望对 AI 调用量进行精确统计、成本控制及安全审计的组织。
- 寻求 OpenAI 兼容接口但需自行托管以避免数据泄露的技术架构师。

4. **技术亮点**
- 采用 TypeScript 编写，类型安全且易于维护扩展。
- 内置分层探测与健康评分模型，提升路由决策的智能性与稳定性。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 144 | 🍴 15 | 语言: TypeScript

### motion-anything
- ### 1. **中文简介**
Motion Anything 是一个开源的、基于聊天原生的 AI 智能体运动引擎，旨在通过自然语言描述来生成动画。用户只需描述 desired 的感觉或动作，AI 即可自动制作并交付相应的动画效果。它是设计工具中用于替代 Figma 运动插件的创新方案。

### 2. **核心功能**
*   **自然语言驱动动画**：支持通过对话式指令描述动态效果，AI 自动将其转化为可执行的动画代码。
*   **Chat-Native 交互体验**：以聊天界面为核心交互方式，降低动画制作门槛，实现“描述即生成”。
*   **开源智能体架构**：基于开源构建，具备 AI Agent 特性，能够自主理解和执行复杂的运动设计需求。
*   **多平台兼容性与 WebGL 支持**：利用 WebGL 技术确保动画在 Web 端的高性能渲染和广泛兼容性。
*   **设计工具集成潜力**：作为 Figma 等主流设计工具的替代或补充方案，专注于运动图形（Motion Graphics）领域。

### 3. **适用场景**
*   **快速原型设计**：设计师在 Figma 或其他 UI 工具中，通过文字快速生成微交互动画原型，无需编写代码。
*   **Web 前端动效开发**：前端开发者利用自然语言指令生成高性能 WebGL 动画，加速网页视觉效果的实现。
*   **创意营销素材制作**：市场团队通过简单描述生成高质量的动态图形内容，用于社交媒体广告或品牌宣传。
*   **无障碍动画创作**：非专业动画师通过对话方式参与动画制作，降低创意表达的技术壁垒。

### 4. **技术亮点**
*   **AI Agent 驱动**：引入智能体概念，使系统不仅能理解指令，还能自主规划并执行动画生成的复杂流程。
*   **原生聊天接口**：采用 Chat-Native 架构，无缝对接大语言模型（如 Claude），实现直观的指令输入与反馈。
*   **高性能 WebGL 渲染**：底层依托 WebGL 技术，确保生成的动画在不同设备上保持流畅和高帧率表现。
- 链接: https://github.com/nexu-io/motion-anything
- ⭐ 135 | 🍴 12 | 语言: JavaScript
- 标签: ai-agent, animation, claude, design-tools, figma-motion-alternative

### rocketplaneIO
- ### 1. 中文简介
RocketplaneIO 是一个自托管的 AI SRE（站点可靠性工程）解决方案，专为 Kubernetes 环境设计。它结合了零侵入式的 eBPF 可观测性与一个具备护栏机制和自验证功能的 AI Copilot，能够自动修复系统问题。

### 2. 核心功能
*   **零侵入式 eBPF 可观测性**：通过 eBPF 技术实现无需代码修改的深度系统监控与追踪。
*   **AI 自动修复 Copilot**：集成大语言模型，以受控且自我验证的方式执行故障修复操作。
*   **BYO-LLM 与离线支持**：允许用户自带 LLM，并支持在物理隔离（air-gapped）的网络环境中运行。
*   **多协议数据整合**：兼容 OpenTelemetry、PromQL 和 ClickHouse，提供全栈监控与日志追踪能力。

### 3. 适用场景
*   **高安全要求的 Kubernetes 集群**：需要在物理隔离网络中运行，且希望完全掌控 LLM 数据流向的企业环境。
*   **复杂微服务故障排查**：需要深度系统级可见性并能自动化处理常规 SRE 事件的技术团队。
*   **自定义 AI 运维工作流**：希望集成自有或本地部署的大模型，定制特定领域运维策略的组织。

### 4. 技术亮点
*   **安全性与可控性**：通过“护栏”机制确保 AI 操作的安全性，并结合自验证逻辑降低误操作风险。
*   **轻量级监控栈**：利用 eBPF 实现高性能、低开销的系统级可观测性，避免传统 Agent 的资源占用。
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### sail-skill
- 1. **中文简介**
SAIL V2（安全AI生命周期）作为一个智能体技能，提供了涵盖91项风险的完整目录，用于评估AI与智能体之间的差距、制定安全路线图及合规检查清单。该技能支持安装于Claude Code、Codex、ChatGPT、Antigravity以及任何兼容SKILL.md的智能体平台。

2. **核心功能**
*   提供包含91项风险的全面AI/智能体安全性评估目录。
*   协助生成针对AI系统的定制化安全发展路线图。
*   内置标准化的合规性检查清单以辅助审计与验证。
*   具备跨平台兼容性，可无缝集成至多种主流AI编码助手中。

3. **适用场景**
*   在开发或部署AI代理时进行系统性的安全风险差距分析。
*   为组织构建符合行业标准的LLM安全防护框架与流程。
*   自动化执行AI应用的安全合规性审查与自我诊断。

4. **技术亮点**
*   采用通用的SKILL.md标准格式，实现了极高的跨智能体平台互操作性。
*   聚焦于“安全AI生命周期”理念，将安全评估嵌入到AI开发的各个阶段。
- 链接: https://github.com/pillar-labs/sail-skill
- ⭐ 116 | 🍴 0 | 语言: 未知
- 标签: agent-skills, agentic-ai, ai-security, claude-code, claude-code-plugin

### Autonomous-Forge
- 1. **中文简介**
这是一个完全由AI构建和自动维护的仓库，它能够持续地进行自我规划、编码、测试及优化改进。该项目展示了AI在软件开发全生命周期中自主执行复杂任务的能力。

2. **核心功能**
*   实现代码库的完全自动化构建与维护流程。
*   具备自主规划开发任务并生成相应代码的能力。
*   集成自动化测试机制以验证代码质量与稳定性。
*   能够持续迭代并自我优化现有代码结构。

3. **适用场景**
*   研究或演示AI自主软件工程（AutoML/Agent）的技术潜力。
*   作为参考案例，探索LLM在持续集成与持续部署（CI/CD）中的应用。
*   自动化维护小型开源项目或原型开发中的样板代码。

4. **技术亮点**
*   全链路AI驱动：从规划到代码生成、测试及维护均由人工智能独立完成，无需人工干预。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 104 | 🍴 3 | 语言: Python

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
- ⭐ 24 | 🍴 9 | 语言: Shell

### ccmux
- 描述: 🔮 Track all your AI coding agents (Claude Code, Codex, Cursor, ...) in tmux and jump to the one that needs you
- 链接: https://github.com/epilande/ccmux
- ⭐ 24 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, bun, claude, claude-code, cli

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个全面且强大的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取（手机/身份证/邮箱等）及繁简转换等基础功能。它不仅提供了丰富的领域词库（如汽车、医疗、法律、古诗词等）和预训练模型资源，还涵盖了情感分析、文本生成、知识图谱构建及语音识别等多种高级NLP应用场景。

2. **核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、语言检测、繁简转换、停用词、反动词表及文本纠错等功能。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱、地址等正则抽取，以及基于BERT、BiLSTM等模型的命名实体识别（NER）和关系抽取。
*   **丰富领域词库与数据**：内置中日文人名库、行业术语库（金融、医疗、法律、汽车等）、成语词典、古诗词及大量开源NLP数据集。
*   **高级NLP任务支持**：涵盖情感分析、文本摘要、句子相似度匹配、关键词抽取、聊天机器人构建及语音识别（ASR）相关工具。

3. **适用场景**
*   **内容安全审核**：适用于社交媒体、论坛或企业内部系统，用于自动过滤敏感词、暴恐词及生成广告垃圾信息。
*   **智能客服与对话系统开发**：为开发者提供聊天机器人语料、意图识别工具及多轮对话管理资源，加速智能客服落地。
*   **垂直领域知识图谱构建**：帮助金融、医疗、法律等行业快速提取结构化实体关系，构建领域专属的知识库或问答系统。

4. **技术亮点**
该项目最大的亮点在于其**资源的极度丰富性与集成度**，它将分散的NLP组件（如分词、句法分析、词向量、预训练模型BERT/ERNIE等）、领域词典及最新竞赛方案汇总于一体，极大降低了中文NLP开发的门槛和数据准备成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，每个项目均附带完整代码实现。它作为一份全面的“Awesome”列表，旨在为开发者提供从入门到进阶的实践案例参考。该项目涵盖了数据科学领域的多个核心分支，是学习人工智能技术的优质素材库。

**2. 核心功能**
*   提供涵盖机器学习、深度学习和NLP等主流AI领域的500个实战项目。
*   所有项目均配有可运行的源代码，便于用户直接复现和修改。
*   分类清晰，特别标注了计算机视觉和NLP的具体子项目方向。
*   作为社区认证的“Awesome”列表，整合了高质量的数据科学学习资源。

**3. 适用场景**
*   **初学者入门实践**：适合希望从零开始通过动手代码理解AI概念的学习者。
*   **面试与作品集准备**：求职者可利用这些项目构建个人GitHub作品集，展示技术能力。
*   **技术选型参考**：研究人员或工程师可通过浏览项目列表，快速了解当前流行的AI应用方向。

**4. 技术亮点**
*   极高的社区认可度（35k+星标），证明了其内容的实用性和广泛性。
*   标签体系完善，精准覆盖了从底层算法到上层应用（如CV、NLP）的技术栈。
*   “代码即文档”的模式，通过真实项目代码而非单纯理论来传授知识。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，能够直观地展示模型结构，帮助开发者快速理解和分析算法架构。该项目因其轻量级、跨平台且无需安装依赖的特点，成为模型调试与展示的高效助手。

### 2. 核心功能
*   **多格式广泛支持**：兼容 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite、safetensors 等数十种主流模型格式。
*   **交互式可视化**：提供清晰的节点图视图，支持缩放、平移及点击节点查看详细参数和权重信息。
*   **跨平台与便捷性**：拥有 Web 版本、桌面客户端及命令行工具，无需配置复杂环境即可直接使用。
*   **实时预览能力**：支持拖拽文件即时加载并渲染模型结构，极大提升了模型检查的效率。

### 3. 适用场景
*   **模型调试与验证**：在部署前检查模型结构是否正确，识别层连接错误或维度不匹配问题。
*   **学术交流与展示**：生成高质量的模型架构图，用于论文配图、技术博客或会议演示。
*   **跨框架迁移分析**：对比不同框架（如从 PyTorch 转至 ONNX）导出后的模型差异，确保转换一致性。
*   **教育学习**：帮助初学者直观理解复杂神经网络（如 CNN、Transformer）的内部层级和数据流向。

### 4. 技术亮点
*   **零依赖运行**：基于 Electron 和 Node.js 构建，用户无需安装 Python 或特定深度学习库即可查看模型，解决了环境冲突痛点。
*   **高性能渲染**：采用优化的前端渲染引擎，即使面对包含数千节点的超大模型也能保持流畅交互。
*   **开源与社区活跃**：作为 GitHub 上星标数极高的开源项目（33k+），拥有活跃的社区支持和持续的格式更新跟进。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33192 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与部署，实现“一次训练，随处运行”。

2. **核心功能**
- 定义了一套与平台无关的模型表示格式，支持跨框架模型交换。
- 提供从主流框架（如PyTorch、TensorFlow、Keras）到ONNX的转换器工具。
- 包含运行时环境，允许在不同硬件后端上高效执行ONNX模型。
- 支持模型验证和转换检查，确保模型结构和数据的完整性。

3. **适用场景**
- 在开发阶段使用PyTorch或TensorFlow训练模型，并导出为ONNX以便在生产环境中部署。
- 需要跨不同推理引擎（如ONNX Runtime、TensorRT、OpenVINO）进行模型性能优化和测试时。
- 当需要在不支持特定框架硬件加速器的设备上运行深度学习模型时。

4. **技术亮点**
- 作为行业通用标准，被Microsoft、Facebook、AWS等主要科技巨头广泛支持，生态兼容性极强。
- 通过ONNX Runtime提供高性能推理加速，支持CPU、GPU及专用硬件后端。
- 链接: https://github.com/onnx/onnx
- ⭐ 21113 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面介绍机器学习工程实践的资源合集，涵盖了从模型训练、推理优化到大规模系统扩展的关键技术。它旨在为从业者提供关于MLOps、PyTorch及大语言模型（LLM）等领域的最佳实践指南。

2. **核心功能**
*   提供大规模分布式训练和超参数调优的工程化解决方案。
*   深入解析大语言模型（LLM）的推理加速与内存优化技巧。
*   指导构建可扩展的数据管道、存储系统及网络基础设施。
*   涵盖SLURM集群管理、GPU调试及故障排查等运维细节。
*   介绍基于PyTorch和Transformers库的高级建模与部署流程。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习训练集群的工程师。
*   致力于降低大语言模型推理成本并提升响应速度的团队。
*   希望建立标准化MLOps流水线以实现模型高效部署的组织。
*   面临GPU资源瓶颈或分布式训练通信问题的技术专家。

4. **技术亮点**
该项目结合了前沿的LLM技术与传统的MLOps实践，特别强调在真实生产环境中解决可扩展性、稳定性和性能调优的具体代码示例与架构设计思路。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18260 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
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
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，每个项目均附带完整代码实现。它作为一份全面的“Awesome”列表，旨在为开发者提供从入门到进阶的实践案例参考。该项目涵盖了数据科学领域的多个核心分支，是学习人工智能技术的优质素材库。

**2. 核心功能**
*   提供涵盖机器学习、深度学习和NLP等主流AI领域的500个实战项目。
*   所有项目均配有可运行的源代码，便于用户直接复现和修改。
*   分类清晰，特别标注了计算机视觉和NLP的具体子项目方向。
*   作为社区认证的“Awesome”列表，整合了高质量的数据科学学习资源。

**3. 适用场景**
*   **初学者入门实践**：适合希望从零开始通过动手代码理解AI概念的学习者。
*   **面试与作品集准备**：求职者可利用这些项目构建个人GitHub作品集，展示技术能力。
*   **技术选型参考**：研究人员或工程师可通过浏览项目列表，快速了解当前流行的AI应用方向。

**4. 技术亮点**
*   极高的社区认可度（35k+星标），证明了其内容的实用性和广泛性。
*   标签体系完善，精准覆盖了从底层算法到上层应用（如CV、NLP）的技术栈。
*   “代码即文档”的模式，通过真实项目代码而非单纯理论来传授知识。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，能够直观地展示模型结构，帮助开发者快速理解和分析算法架构。该项目因其轻量级、跨平台且无需安装依赖的特点，成为模型调试与展示的高效助手。

### 2. 核心功能
*   **多格式广泛支持**：兼容 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite、safetensors 等数十种主流模型格式。
*   **交互式可视化**：提供清晰的节点图视图，支持缩放、平移及点击节点查看详细参数和权重信息。
*   **跨平台与便捷性**：拥有 Web 版本、桌面客户端及命令行工具，无需配置复杂环境即可直接使用。
*   **实时预览能力**：支持拖拽文件即时加载并渲染模型结构，极大提升了模型检查的效率。

### 3. 适用场景
*   **模型调试与验证**：在部署前检查模型结构是否正确，识别层连接错误或维度不匹配问题。
*   **学术交流与展示**：生成高质量的模型架构图，用于论文配图、技术博客或会议演示。
*   **跨框架迁移分析**：对比不同框架（如从 PyTorch 转至 ONNX）导出后的模型差异，确保转换一致性。
*   **教育学习**：帮助初学者直观理解复杂神经网络（如 CNN、Transformer）的内部层级和数据流向。

### 4. 技术亮点
*   **零依赖运行**：基于 Electron 和 Node.js 构建，用户无需安装 Python 或特定深度学习库即可查看模型，解决了环境冲突痛点。
*   **高性能渲染**：采用优化的前端渲染引擎，即使面对包含数千节点的超大模型也能保持流畅交互。
*   **开源与社区活跃**：作为 GitHub 上星标数极高的开源项目（33k+），拥有活跃的社区支持和持续的格式更新跟进。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33192 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
这是一个专为深度学习和机器学习研究人员设计的必备速查手册集合。该项目整理了关键代码片段、库用法及最佳实践，旨在帮助研究者快速查阅和解决常见问题。

2. **核心功能**
- 提供深度学习框架（如Keras）的核心API速查表。
- 涵盖数据处理与科学计算库（如NumPy、SciPy、Matplotlib）的关键操作指南。
- 总结机器学习算法实现中的常见技巧与调试方法。
- 以结构化的代码示例形式呈现，便于快速复制和应用。

3. **适用场景**
- 研究人员在复现论文或搭建模型时快速查找特定函数用法。
- 初学者在学习机器学习基础库时作为日常参考工具。
- 开发者在进行数据可视化或数值计算时查阅标准语法。
- 团队内部进行技术分享或新人入职培训的资料储备。

4. **技术亮点**
- 内容高度精炼，聚焦于高频使用的“关键”代码，减少冗余信息。
- 集成主流AI生态核心库，覆盖从数据处理到模型训练的全流程。
- 源自Medium技术博客的深度整理，具有较高的实用性和权威性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，旨在帮助零基础用户通过近200个实战案例轻松入门并实现就业。该项目免费配套教材，涵盖从Python基础到深度学习、自然语言处理及计算机视觉等热门领域的完整知识体系。

### 2. 核心功能
*   **系统化学习路径**：提供从零开始至就业级别的AI技能进阶路线图。
*   **海量实战案例**：整理并收录了约200个可操作的AI实战项目供学习参考。
*   **丰富资源配套**：免费提供与教程配套的教材资料，降低学习门槛。
*   **全栈技术覆盖**：内容贯穿Python、数学基础、机器学习、深度学习及各大主流框架。

### 3. 适用场景
*   **零基础转行**：适合希望进入AI行业但缺乏编程和数学基础的学习者。
*   **求职实战准备**：适用于需要准备简历项目经验、提升面试竞争力的求职者。
*   **系统性复习**：适合已有一定基础的技术人员梳理知识体系，查漏补缺。

### 4. 技术亮点
*   **框架全覆盖**：同时支持 TensorFlow、PyTorch、Keras、Caffe 等主流深度学习框架。
*   **生态完整**：集成 NumPy、Pandas、Matplotlib、Seaborn 等数据分析与可视化核心库。
*   **领域广泛**：涵盖 NLP（自然语言处理）、CV（计算机视觉）及数据挖掘等前沿方向。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它通过声明式配置的方式，降低了深度学习应用的开发门槛，使用户能够专注于数据而非复杂的工程实现。

**2. 核心功能**
*   支持多种模态数据（文本、图像、表格等）的统一建模与处理。
*   提供基于 YAML 的配置接口，实现无需编写代码即可快速训练和评估模型。
*   内置对主流深度学习后端（如 PyTorch）的支持及自动化超参数调优能力。
*   具备强大的模型微调（Fine-tuning）功能，适用于 Llama、Mistral 等大语言模型。
*   提供可视化的训练监控和结果分析工具，便于数据科学工作流集成。

**3. 适用场景**
*   企业级 AI 原型开发，需要快速验证不同算法在特定数据集上的效果。
*   对代码能力要求不高但需构建定制深度学习模型的数据科学家或业务分析师。
*   需要对现有开源大语言模型（如 LLaMA、Mistral）进行领域适配和微调的场景。
*   多模态学习任务，例如同时处理表格数据与图像或自然语言输入的复杂预测问题。

**4. 技术亮点**
Ludwig 的核心优势在于其“数据中心”（Data-centric）的设计理念，通过声明式配置将模型架构与训练逻辑解耦，显著提升了实验迭代效率并减少了样板代码的编写量。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1235 | 语言: Python
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
- ⭐ 6229 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
该项目是一个全面且强大的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别、实体抽取（手机/身份证/邮箱等）及繁简转换等基础功能。它不仅提供了丰富的领域词库（如汽车、医疗、法律、古诗词等）和预训练模型资源，还涵盖了情感分析、文本生成、知识图谱构建及语音识别等多种高级NLP应用场景。

2. **核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、语言检测、繁简转换、停用词、反动词表及文本纠错等功能。
*   **信息抽取与实体识别**：支持手机号、身份证、邮箱、地址等正则抽取，以及基于BERT、BiLSTM等模型的命名实体识别（NER）和关系抽取。
*   **丰富领域词库与数据**：内置中日文人名库、行业术语库（金融、医疗、法律、汽车等）、成语词典、古诗词及大量开源NLP数据集。
*   **高级NLP任务支持**：涵盖情感分析、文本摘要、句子相似度匹配、关键词抽取、聊天机器人构建及语音识别（ASR）相关工具。

3. **适用场景**
*   **内容安全审核**：适用于社交媒体、论坛或企业内部系统，用于自动过滤敏感词、暴恐词及生成广告垃圾信息。
*   **智能客服与对话系统开发**：为开发者提供聊天机器人语料、意图识别工具及多轮对话管理资源，加速智能客服落地。
*   **垂直领域知识图谱构建**：帮助金融、医疗、法律等行业快速提取结构化实体关系，构建领域专属的知识库或问答系统。

4. **技术亮点**
该项目最大的亮点在于其**资源的极度丰富性与集成度**，它将分散的NLP组件（如分词、句法分析、词向量、预训练模型BERT/ERNIE等）、领域词典及最新竞赛方案汇总于一体，极大降低了中文NLP开发的门槛和数据准备成本。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型与视觉语言模型微调框架，支持 100 多种主流模型。该项目在 ACL 2024 上发表，旨在简化从指令微调到强化学习对齐的全流程开发。它通过整合 PEFT、QLoRA 等先进技术，显著降低了大模型本地化部署和优化的门槛。

2. **核心功能**
*   **广泛模型支持**：无缝兼容 Llama、Qwen、Gemma、DeepSeek 等 100+ 种大语言及视觉语言模型。
*   **多样化微调算法**：内置全量微调、LoRA、QLoRA、DPO 及 RLHF 等多种前沿微调策略。
*   **量化训练优化**：支持 4-bit/8-bit 量化训练，大幅降低显存占用，使消费级显卡也能运行大型模型。
*   **统一训练接口**：提供标准化的命令行和 Web UI 界面，简化配置过程，提升实验效率。
*   **多模态扩展能力**：不仅支持文本生成，还具备强大的视觉语言模型（VLMs）微调能力。

3. **适用场景**
*   **企业私有化部署**：利用 QLoRA 等技术，在有限算力下快速微调开源模型以适应特定行业知识库。
*   **AI 应用开发者**：快速构建基于 Llama 或 Qwen 等模型的垂直领域助手，如客服机器人或代码辅助工具。
*   **学术研究人员**：进行大规模语言模型对齐（RLHF/DPO）或多模态融合技术的对比实验与复现。
*   **个人兴趣探索**：普通用户通过低门槛工具在本地电脑上体验并定制属于自己的个性化 AI 助手。

4. **技术亮点**
*   实现了训练加速与显存优化的最佳实践结合，支持混合精度训练与 FlashAttention 等高性能组件。
*   采用模块化设计，轻松集成 Hugging Face Transformers 生态，同时保持代码的简洁性与可扩展性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73044 | 🍴 8927 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- ### 1. 中文简介
该项目致力于收集和提取各大主流人工智能模型（如 Anthropic 的 Claude、OpenAI 的 GPT/Codex、Google 的 Gemini 等）的系统提示词（System Prompts）。内容涵盖 ChatGPT、Claude Code、Cursor 及 VS Code 等知名工具的内部指令，并定期更新以反映最新变化。

### 2. 核心功能
*   **多厂商覆盖**：整合了 Anthropic、OpenAI、Google、xAI 等头部厂商的最新模型提示词。
*   **工具链包含**：不仅包含基础聊天模型，还囊括了 Claude Code、Cursor、VS Code 插件及 Perplexity 等开发辅助工具的提示词。
*   **定期更新维护**：保持对最新模型版本（如 Fable 5, Opus 4.8, GPT 5.5 等）提示词的同步更新。
*   **开源共享**：作为公共知识库，供开发者研究和学习大型语言模型的底层行为逻辑。

### 3. 适用场景
*   **提示词工程学习**：开发者通过分析官方提示词，理解如何构建高质量的系统指令以优化模型表现。
*   **模型行为逆向分析**：研究人员利用这些提示词来推断特定模型或工具的内部规则与安全限制。
*   **自定义 Agent 开发**：借鉴顶级 AI 代理（如 Claude Code）的系统指令，用于构建更智能、更稳定的自动化工作流。

### 4. 技术亮点
*   **前沿模型同步**：涵盖了尚未广泛公开的“Thinking”和“Instant”等新型模型变体的提示词细节。
*   **生态全覆盖**：从通用聊天机器人延伸至具体的代码编辑器和集成开发环境（IDE），具有极高的垂直参考价值。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52931 | 🍴 8633 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。项目采用Jupyter Notebook作为主要载体，由微软开发者教育团队精心打造，内容覆盖从基础概念到深度学习的前沿技术。

2. **核心功能**
*   **系统化课程体系**：提供结构化的12周学习路径，循序渐进地引导学习者掌握AI核心技能。
*   **交互式代码实践**：基于Jupyter Notebook编写教程，支持读者直接运行代码并进行实时实验。
*   **多领域技术覆盖**：课程内容涵盖机器学习、计算机视觉（CNN/RNN）、自然语言处理（NLP）及生成对抗网络（GAN）等关键领域。
*   **全人群友好设计**：专为初学者设计，无需深厚数学或编程背景即可上手，强调“AI for All”的理念。

3. **适用场景**
*   **高校与培训机构教学**：作为计算机科学或数据科学专业的标准化入门教材或补充课程。
*   **企业员工技能培训**：帮助非技术背景的员工或初级开发人员快速建立对人工智能的基本认知。
*   **自学者入门探索**：适合希望从零开始系统学习AI，并通过动手实践巩固知识的个人爱好者。

4. **技术亮点**
*   **微软背书与开源生态**：依托Microsoft For Beginners品牌，结合高星标的社区影响力，确保内容的权威性与持续更新。
*   **理论与实践深度融合**：不仅讲解理论概念，更通过具体的代码示例让学习者在实际操作中理解CNN、RNN等复杂模型。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51860 | 🍴 10474 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析与机器学习实战的综合资源库，深入结合线性代数理论与 PyTorch、TensorFlow 2 及 NLTK 等主流框架进行实践。它旨在通过从基础算法到深度学习的全链路内容，帮助学习者构建扎实的机器学习知识体系。

2. **核心功能**
*   整合数据分析与机器学习算法的实战代码，覆盖分类、聚类、回归等经典任务。
*   深入讲解线性代数基础，为理解机器学习模型提供必要的数学支撑。
*   提供基于 PyTorch 和 TensorFlow 2 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）等深度学习实现。
*   包含自然语言处理（NLP）相关模块，利用 NLTK 库进行文本分析与处理。
*   集成推荐系统算法，如协同过滤及基于矩阵分解（SVD）的推荐模型。

3. **适用场景**
*   机器学习初学者用于系统学习从数学基础到算法实现的完整流程。
*   数据科学家用于参考经典算法（如 SVM、K-Means、随机森林）的工程化实现。
*   深度学习研究者或开发者用于对比不同框架（PyTorch vs TF2）下的模型构建方式。
*   NLP 领域从业者用于探索基于传统统计方法和现代深度学习的文本处理技术。

4. **技术亮点**
项目采用“理论+代码”双驱动模式，不仅提供 scikit-learn 等库的高级应用，还从零实现 Adaboost、FP-Growth 等经典算法，并强调数学原理（如 PCA、SVD）在代码中的具体体现。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42360 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37588 | 🍴 6259 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33721 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28400 | 🍴 3453 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25843 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22148 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16245 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12902 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11270 | 🍴 1195 | 语言: Python
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382101 | 🍴 80167 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 248656 | 🍴 22081 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210957 | 🍴 38729 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195560 | 🍴 59157 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185423 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165031 | 🍴 21362 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164028 | 🍴 30395 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156860 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151315 | 🍴 9469 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148078 | 🍴 23325 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

