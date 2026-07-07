# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- 基于您提供的信息，以下是对 GitHub 项目 **TokHub** 的技术分析：

1. **中文简介**
   TokHub 是一个支持 OpenAI 协议兼容的专属网关系统，兼具 AI API 中转站的监控、推荐运营与管理功能。它采用 TypeScript 开发，支持 Docker 自托管部署，并内置了分层探测、健康评分及用量计量等核心能力。

2. **核心功能**
   - **OpenAI 兼容网关**：提供标准的 API 接口，无缝对接现有应用。
   - **智能监控与运维**：支持分层探测、实时健康评分以及完整的用量计量与告警审计。
   - **推荐运营管理**：具备中转站推荐算法与运营工具，优化 API 资源分发。
   - **私有化部署**：完全支持 Docker 自托管，确保数据隐私与控制权。

3. **适用场景**
   - **API 聚合服务运营**：适合希望搭建自有 AI API 中转平台并提供推荐服务的创业者或团队。
   - **企业内部网关管理**：适用于需要统一管控内部多个 AI 服务商接入、监控健康状态及成本的企业 IT 部门。
   - **高可用架构保障**：适合对服务稳定性要求高，需要通过分层探测和健康评分来避免单点故障的技术团队。

4. **技术亮点**
   - 采用 **TypeScript** 开发，保证代码类型安全与维护性。
   - 集成 **Docker** 容器化支持，实现一键部署与环境隔离。
   - 设计有 **分层探测机制**，能够更精准地评估上游 API 的真实可用性而非仅依赖表面连通性。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 144 | 🍴 15 | 语言: TypeScript

### motion-anything
- 1. **中文简介**
Motion Anything 是一个开源的、以聊天为原生的代理式运动引擎。用户只需通过自然语言描述想要的“感觉”，AI 即可自动生成相应的动画效果。它旨在让 motion design 变得更加直观和高效。

2. **核心功能**
*   **聊天原生交互**：通过对话方式直接控制动画生成，无需编写复杂代码。
*   **AI 驱动动画生成**：利用智能体技术，将抽象的感觉描述转化为具体的视觉动画。
*   **开源协议支持**：作为开源项目，允许开发者自由使用和修改底层代码。
*   **多平台集成潜力**：标签显示其适用于设计工具和 WebGL 环境，具备较强的扩展性。
*   **替代传统工具**：定位为 Figma Motion 等商业工具的替代方案，降低动画制作门槛。

3. **适用场景**
*   **快速原型设计**：设计师在早期阶段通过文字快速验证动画创意和视觉效果。
*   **WebGL 动态效果开发**：前端开发者利用自然语言指令快速生成复杂的网页动效。
*   **非技术人员的内容创作**：不懂代码的用户通过简单描述即可创建个性化的动画内容。
*   **设计工作流自动化**：集成到现有设计流程中，加速从概念到动态原型的转化过程。

4. **技术亮点**
*   **Agentic AI 架构**：采用智能体层处理运动逻辑，实现更自然的意图理解与执行。
*   **Chat-Native 接口**：将复杂的动画引擎封装在聊天界面之下，极大简化了用户交互路径。
*   **多模态理解能力**：能够解析对“感觉”等抽象情感描述的语义，并映射为具体的动画参数。
- 链接: https://github.com/nexu-io/motion-anything
- ⭐ 127 | 🍴 11 | 语言: JavaScript
- 标签: ai-agent, animation, claude, design-tools, figma-motion-alternative

### rocketplaneIO
- 以下是针对 GitHub 项目 **rocketplaneIO** 的技术分析：

1. **中文简介**
   RocketplaneIO 是一个自托管的 AI 站点可靠性工程（SRE）解决方案，专为 Kubernetes 环境设计。它结合了零侵入式的 eBPF 可观测性与具备护栏机制和自我验证能力的 AI Copilot，能够自动修复故障。该项目支持自带模型（BYO-LLM），并具备完全离线（Air-gapped）部署的能力。

2. **核心功能**
   *   **零侵入式可观测性**：利用 eBPF 技术在 Kubernetes 中实现无需代码插桩的深度系统监控与追踪。
   *   **AI 自动修复 Copilot**：集成具备安全护栏和自我验证功能的 AI 助手，主动识别并修复系统问题。
   *   **灵活的大模型支持**：允许用户自带 LLM（BYO-LLM），适应不同隐私和安全需求。
   *   **离线环境适配**：支持在隔离网络（Air-gapped）环境中完全本地化部署和运行。

3. **适用场景**
   *   **高安全合规的云原生环境**：需要在物理隔离或严格内网环境中部署 AI 辅助运维工具的企业。
   *   **大规模 Kubernetes 集群运维**：希望减少应用改造成本，通过 eBPF 获取底层深度监控数据的 DevOps 团队。
   *   **自动化故障响应体系**：寻求从被动监控转向主动、自我验证的自动化事件响应的 SRE 团队。

4. **技术亮点**
   *   **eBPF + AI 闭环**：将底层无感知的系统级遥测数据直接对接 AI 决策层，实现从检测到修复的自动化闭环。
   *   **自验证机制**：AI 执行的操作经过自我验证和护栏限制，显著降低了自动化运维中的误操作风险。
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### sail-skill
- 1. **中文简介**
SAIL V2（安全AI生命周期）作为一个智能体技能插件，提供了涵盖91项风险的全景目录，用于评估AI/智能体差距、制定安全路线图及合规清单。它支持安装在Claude Code、Codex、ChatGPT、Antigravity以及任何兼容SKILL.md标准的智能体环境中。

2. **核心功能**
- 提供包含91个风险点的完整AI安全风险评估目录。
- 支持跨平台兼容，可无缝集成至主流AI编程助手和智能体框架。
- 协助用户制定针对AI系统的详细安全演进路线图。
- 生成标准化的合规性检查清单以满足安全审计需求。
- 作为即插即用的“技能”模块简化AI安全治理流程。

3. **适用场景**
- 企业在引入或升级AI代理时，进行初步的安全差距分析与风险识别。
- 开发者在使用Claude Code等工具时，实时获取AI安全最佳实践与合规指引。
- 安全团队需要为大型语言模型应用制定长期安全加固策略与路线图。
- 机构希望快速建立符合行业标准的AI系统合规性检查流程。

4. **技术亮点**
- 采用通用的SKILL.md标准，实现了极高的跨智能体平台兼容性。
- 将复杂的AI安全知识库封装为轻量级技能，降低了集成门槛。
- 聚焦于“安全AI生命周期”，覆盖了从评估到合规的全过程管理。
- 链接: https://github.com/pillar-labs/sail-skill
- ⭐ 116 | 🍴 0 | 语言: 未知
- 标签: agent-skills, agentic-ai, ai-security, claude-code, claude-code-plugin

### Autonomous-Forge
- 1. **中文简介**
这是一个完全由AI构建和自动维护的项目，能够持续地进行自我规划、编码、测试以及迭代优化。它展示了一种全自动化的软件开发工作流，旨在实现代码库的自我演进。

2. **核心功能**
*   实现项目代码的全自动编写与生成。
*   具备持续的自我测试与质量验证机制。
*   能够自主规划下一步的开发任务与改进方向。
*   支持代码库的自我修复与性能优化迭代。

3. **适用场景**
*   探索和研究基于大语言模型的自动化软件工程范式。
*   作为AI辅助开发工具链的基准测试案例或参考原型。
*   用于演示或教学目的，展示端到端的AI驱动开发流程。

4. **技术亮点**
该项目展示了AI在复杂软件工程任务中的闭环能力，实现了从规划到部署维护的全生命周期自动化，代表了“AI自举”项目的典型实践。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 96 | 🍴 2 | 语言: Python

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
- ⭐ 23 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, bun, claude, claude-code, cli

## 热门AI项目

## Machine Learning项目

### funNLP
- **1. 中文简介**
该项目是一个全面且丰富的中文自然语言处理（NLP）资源集合，涵盖了从基础文本处理（如敏感词检测、分词、情感分析）到高级应用（如知识图谱构建、对话系统、语音识别）的各种工具、数据集和预训练模型。它整合了学术界与工业界的优秀开源成果，为开发者提供了便捷的NLP入门、进阶及垂直领域解决方案参考。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词、同/反义词库及文本纠错等实用工具。
*   **信息抽取与实体识别**：集成基于BERT、ALBERT等模型的命名实体识别（NER）、关系抽取、关键词提取及简历解析功能。
*   **知识图谱与问答系统**：包含多领域知识图谱构建案例、基于图谱的问答系统（KBQA）及对话机器人资源。
*   **预训练模型与向量资源**：汇总了中文BERT、ERNIE、RoBERTa等主流预训练语言模型及其微调代码，以及丰富的词向量库。
*   **多模态与垂直领域数据**：涵盖语音识别（ASR）语料、医疗/金融/法律等专业领域的数据集、语料库及专用NLP工具。

**3. 适用场景**
*   **NLP初学者学习**：通过整理好的分类资源快速了解NLP领域的基本概念、常用工具和经典数据集。
*   **企业级文本风控系统开发**：利用其中的敏感词库、情感分析及谣言检测工具，构建内容安全审核系统。
*   **垂直行业智能客服/问答构建**：参考医疗、金融或法律领域的知识图谱与问答系统案例，搭建行业专用AI助手。
*   **算法研究与模型微调**：获取最新的预训练模型代码（如BERT、GPT-2中文版）及基准数据集，用于学术复现或业务场景优化。

**4. 技术亮点**
*   **高度聚合性**：作为一个“Awesome List”，它并非单一软件，而是将分散的高质量开源项目、论文、数据集和工具进行了系统化分类整理，极大降低了信息检索成本。
*   **紧跟前沿技术**：内容持续更新，涵盖了从传统NLP方法到基于Transformer的大模型（BERT, GPT, ALBERT等）的最新进展。
*   **覆盖领域广泛**：不仅限于通用NLP，还深入医疗、法律、金融、语音、OCR等多个垂直专业领域，具备极高的实用参考价值。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库。它提供了完整的代码实现，是学习相关技术栈的重要参考资料。

2. **核心功能**
*   收录大量涵盖AI各细分领域的实战项目代码。
*   提供从基础机器学习到前沿深度学习的完整案例。
*   包含计算机视觉和自然语言处理的具体应用实例。
*   所有项目均附带可运行的源代码以便直接学习和测试。

3. **适用场景**
*   AI初学者构建知识库并快速上手实战项目。
*   数据科学家寻找特定算法或应用场景的代码参考。
*   开发者利用现有项目进行二次开发或技术调研。

4. **技术亮点**
*   作为Awesome列表，高度聚合了该领域的高星优质项目。
*   覆盖Python生态下主流AI框架的实际应用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持多种主流框架的神经网络、深度学习及机器学习模型可视化工具。它能够直观地展示模型结构和数据流向，帮助用户快速理解和分析复杂的算法架构。

2. **核心功能**
*   支持查看多种格式的模型文件，包括 ONNX、TensorFlow、PyTorch、Keras 和 CoreML 等。
*   提供直观的图形界面，清晰展示神经网络的层级结构、张量形状及数据流动路径。
*   具备模型调试功能，可辅助开发者检查模型配置错误并优化网络设计。
*   允许导出模型截图或生成静态图片，便于在文档或演示报告中分享模型结构。

3. **适用场景**
*   **模型调试**：在训练前或推理阶段检查模型结构是否正确，定位层连接错误。
*   **学术交流与报告**：制作清晰的模型架构图，用于论文发表、技术博客或会议演示。
*   **跨框架迁移验证**：对比不同框架（如从 PyTorch 到 ONNX）转换后的模型一致性。

4. **技术亮点**
*   **广泛的格式兼容性**：原生支持数十种主流模型格式，无需额外转换即可直接读取。
*   **轻量级与跨平台**：基于 Web 技术构建，既可作为桌面应用运行，也可通过浏览器在线访问，使用便捷。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33192 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（开放神经网络交换）是机器学习的通用标准，旨在实现不同深度学习框架之间的互操作性。它允许开发者在不同平台（如 PyTorch、TensorFlow、Scikit-learn 等）之间无缝转换模型，打破框架壁垒，提升模型部署效率。

### 2. 核心功能
*   **跨框架模型转换**：支持将主流深度学习框架（PyTorch、TensorFlow 等）训练的模型统一转换为 ONNX 格式。
*   **统一模型表示**：提供标准化的计算图定义，确保模型结构和参数在不同运行时环境中保持一致。
*   **广泛硬件支持**：兼容多种推理引擎和优化器，便于在 CPU、GPU 及专用加速器上高效部署。
*   **生态兼容性**：与 Keras、Scikit-learn 等工具链集成良好，简化机器学习工作流。

### 3. 适用场景
*   **生产环境部署**：将开发阶段训练好的模型转换为标准格式，以便在高性能推理服务器或边缘设备上运行。
*   **框架迁移与实验**：在不同深度学习框架间迁移模型，比较性能或利用特定框架的优势进行后续优化。
*   **硬件加速集成**：对接 Intel OpenVINO、NVIDIA TensorRT 等硬件优化库，提升模型推理速度。

### 4. 技术亮点
*   **工业界标准地位**：由微软、Facebook、AWS 等科技巨头联合推动，成为机器学习互操作的事实标准。
*   **端到端优化能力**：支持模型转换后的图优化和算子融合，显著提升推理效率并减少资源消耗。
- 链接: https://github.com/onnx/onnx
- ⭐ 21113 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 以下是针对 GitHub 项目 `ml-engineering` 的分析：

1. **中文简介**
该项目是一部关于机器学习工程的开源“开放式书籍”，旨在系统性地指导开发者构建大规模机器学习系统。它涵盖了从底层基础设施到上层模型训练、调试及部署的全流程最佳实践，是 MLOps 领域的权威参考指南。

2. **核心功能**
*   提供大规模分布式训练和推理的工程化实现细节与代码示例。
*   深入讲解 GPU 硬件特性、网络通信优化及存储管理以解决扩展性瓶颈。
*   包含针对大型语言模型（LLM）和 Transformer 架构的特定调试技巧。
*   介绍使用 Slurm 等集群调度器管理计算资源的方法。
*   分享 PyTorch 框架下的高性能数据处理和模型优化策略。

3. **适用场景**
*   **LLM 研发团队**：需要从零搭建支持千亿参数模型训练的基础设施时。
*   **MLOps 工程师**：希望优化现有机器学习流水线的延迟、吞吐量和稳定性时。
*   **高性能计算研究者**：致力于探索 GPU 集群网络通信极限及存储 I/O 优化时。
*   **深度学习从业者**：遇到模型训练难以收敛或显存溢出等工程难题需要排查时。

4. **技术亮点**
*   **实战导向**：不仅理论丰富，更提供了大量可复现的工程代码和故障排除案例。
*   **前沿覆盖**：紧跟大模型时代需求，特别强化了针对 Transformers 和 LLM 的训练/推理优化内容。
*   **全栈视角**：打通了从芯片级（GPU）、系统级（Slurm/Network）到算法级（PyTorch/Transformers）的技术栈。
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
- 1. **中文简介**
该项目是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库。它提供了完整的代码实现，是学习相关技术栈的重要参考资料。

2. **核心功能**
*   收录大量涵盖AI各细分领域的实战项目代码。
*   提供从基础机器学习到前沿深度学习的完整案例。
*   包含计算机视觉和自然语言处理的具体应用实例。
*   所有项目均附带可运行的源代码以便直接学习和测试。

3. **适用场景**
*   AI初学者构建知识库并快速上手实战项目。
*   数据科学家寻找特定算法或应用场景的代码参考。
*   开发者利用现有项目进行二次开发或技术调研。

4. **技术亮点**
*   作为Awesome列表，高度聚合了该领域的高星优质项目。
*   覆盖Python生态下主流AI框架的实际应用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持多种主流框架的神经网络、深度学习及机器学习模型可视化工具。它能够直观地展示模型结构和数据流向，帮助用户快速理解和分析复杂的算法架构。

2. **核心功能**
*   支持查看多种格式的模型文件，包括 ONNX、TensorFlow、PyTorch、Keras 和 CoreML 等。
*   提供直观的图形界面，清晰展示神经网络的层级结构、张量形状及数据流动路径。
*   具备模型调试功能，可辅助开发者检查模型配置错误并优化网络设计。
*   允许导出模型截图或生成静态图片，便于在文档或演示报告中分享模型结构。

3. **适用场景**
*   **模型调试**：在训练前或推理阶段检查模型结构是否正确，定位层连接错误。
*   **学术交流与报告**：制作清晰的模型架构图，用于论文发表、技术博客或会议演示。
*   **跨框架迁移验证**：对比不同框架（如从 PyTorch 到 ONNX）转换后的模型一致性。

4. **技术亮点**
*   **广泛的格式兼容性**：原生支持数十种主流模型格式，无需额外转换即可直接读取。
*   **轻量级与跨平台**：基于 Web 技术构建，既可作为桌面应用运行，也可通过浏览器在线访问，使用便捷。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33192 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目专为深度学习和机器学习研究者提供必不可少的速查表（Cheat Sheets）。它涵盖了从基础库到高级框架的关键知识要点，旨在帮助研究人员快速回顾和掌握核心概念。

### 2. 核心功能
*   提供深度学习与机器学习领域的关键知识点速查指南。
*   集成常用Python科学计算库（如NumPy、SciPy）的操作备忘。
*   包含主流深度学习框架（如Keras）及可视化工具（如Matplotlib）的使用技巧。
*   针对AI研究者优化的结构化知识汇总，便于快速查阅。

### 3. 适用场景
*   深度学习初学者快速上手并建立知识框架。
*   机器学习研究员在工作中需要快速回顾特定函数或参数用法时。
*   备考或面试前集中复习AI相关核心概念与代码片段。
*   团队协作中作为标准化的参考文档，统一术语与操作规范。

### 4. 技术亮点
*   高度浓缩的知识呈现方式，极大提升了信息获取效率。
*   覆盖从底层数据处理到上层模型构建的全栈技术点。
*   基于Medium文章整理，内容经过验证且贴合实际研究需求。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户快速构建自定义的大语言模型（LLM）、神经网络及其他人工智能模型。它通过简化复杂的深度学习流程，让数据科学家和开发者能够更高效地进行模型训练与微调。

### 2. **核心功能**
*   支持基于声明式配置快速构建和训练各类深度学习模型。
*   提供对大语言模型（如 Llama、Mistral）的低门槛微调与集成能力。
*   涵盖从数据处理到模型评估的全流程自动化，降低开发复杂度。
*   兼容 PyTorch 等主流深度学习后端，确保模型性能与灵活性。

### 3. **适用场景**
*   需要快速原型化验证想法的数据科学团队或初创公司。
*   希望在不编写大量底层代码的情况下微调现有开源大语言模型的研究人员。
*   专注于计算机视觉或自然语言处理任务，追求高效迭代的企业级 AI 应用开发。

### 4. **技术亮点**
*   **低代码/无代码特性**：通过 YAML 配置文件定义模型结构，显著减少样板代码。
*   **数据中心主义（Data-Centric）**：强调通过改进数据质量和标注来提升模型效果，而非仅依赖调参。
*   **广泛的模态支持**：原生支持文本、图像、音频、表格等多种数据类型。
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
- **1. 中文简介**
该项目是一个全面且丰富的中文自然语言处理（NLP）资源集合，涵盖了从基础文本处理（如敏感词检测、分词、情感分析）到高级应用（如知识图谱构建、对话系统、语音识别）的各种工具、数据集和预训练模型。它整合了学术界与工业界的优秀开源成果，为开发者提供了便捷的NLP入门、进阶及垂直领域解决方案参考。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词、同/反义词库及文本纠错等实用工具。
*   **信息抽取与实体识别**：集成基于BERT、ALBERT等模型的命名实体识别（NER）、关系抽取、关键词提取及简历解析功能。
*   **知识图谱与问答系统**：包含多领域知识图谱构建案例、基于图谱的问答系统（KBQA）及对话机器人资源。
*   **预训练模型与向量资源**：汇总了中文BERT、ERNIE、RoBERTa等主流预训练语言模型及其微调代码，以及丰富的词向量库。
*   **多模态与垂直领域数据**：涵盖语音识别（ASR）语料、医疗/金融/法律等专业领域的数据集、语料库及专用NLP工具。

**3. 适用场景**
*   **NLP初学者学习**：通过整理好的分类资源快速了解NLP领域的基本概念、常用工具和经典数据集。
*   **企业级文本风控系统开发**：利用其中的敏感词库、情感分析及谣言检测工具，构建内容安全审核系统。
*   **垂直行业智能客服/问答构建**：参考医疗、金融或法律领域的知识图谱与问答系统案例，搭建行业专用AI助手。
*   **算法研究与模型微调**：获取最新的预训练模型代码（如BERT、GPT-2中文版）及基准数据集，用于学术复现或业务场景优化。

**4. 技术亮点**
*   **高度聚合性**：作为一个“Awesome List”，它并非单一软件，而是将分散的高质量开源项目、论文、数据集和工具进行了系统化分类整理，极大降低了信息检索成本。
*   **紧跟前沿技术**：内容持续更新，涵盖了从传统NLP方法到基于Transformer的大模型（BERT, GPT, ALBERT等）的最新进展。
*   **覆盖领域广泛**：不仅限于通用NLP，还深入医疗、法律、金融、语音、OCR等多个垂直专业领域，具备极高的实用参考价值。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与多模态大模型（VLM）微调框架，支持超过 100 种主流模型。该项目在 ACL 2024 会议上发表，旨在简化从基础训练到高级对齐（如 RLHF）的全流程操作。它通过整合多种高效微调技术，降低了用户部署和优化大型模型的门槛。

2. **核心功能**
*   **广泛模型支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100 多种主流 LLM 和 VLM 架构。
*   **多样化微调算法**：内置 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法。
*   **全阶段训练能力**：支持从指令微调（Instruction Tuning）到强化学习人类反馈（RLHF）的完整训练流程。
*   **量化与优化集成**：原生支持 INT4/INT8 量化技术，显著降低显存占用并提升推理效率。
*   **统一接口体验**：提供命令行、Web UI 和 API 多种交互方式，实现一键式模型训练与管理。

3. **适用场景**
*   **企业级私有化部署**：利用 QLoRA 等技术，在有限显存资源下对特定行业数据进行高效指令微调。
*   **多模态应用开发**：针对包含图像、文本等多种输入类型的 VLM 模型进行统一的训练与优化。
*   **学术研究基准测试**：作为标准化的微调平台，用于对比不同算法或模型架构在 NLP 任务上的性能表现。

4. **技术亮点**
*   **极简配置**：通过 YAML 配置文件即可定义复杂的训练超参数，无需编写冗长的代码逻辑。
*   **混合精度加速**：深度集成 Transformers 库与 PEFT 库，充分利用 FlashAttention 等加速技术提升训练速度。
*   **模块化设计**：将数据处理、模型加载、训练策略解耦，便于研究人员快速实验新的微调策略。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73044 | 🍴 8927 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目汇集了从Anthropic、OpenAI、Google及xAI等主流厂商的大语言模型中提取的系统提示词（System Prompts），涵盖Claude、GPT、Gemini等知名模型及Cursor、VS Code等开发工具。内容定期更新，旨在为研究者和安全专家提供最新的模型底层指令数据。

2. **核心功能**
*   收集并公开多个顶级AI模型（如Claude 5/Opus、GPT 5.5、Gemini 3.5等）的系统提示词。
*   包含AI代理工具（如Cursor、Copilot、Perplexity）的底层配置指令。
*   保持高频更新，确保证据库反映最新发布的模型版本和变更。
*   以结构化数据形式呈现，便于自动化脚本解析和分析。

3. **适用场景**
*   **安全研究**：分析大型语言模型的内部指令，评估潜在的越狱漏洞或安全风险。
*   **提示词工程优化**：参考官方系统指令的设计逻辑，提升自定义Prompt的有效性和稳定性。
*   **AI模型对比**：通过比较不同厂商模型的系统提示差异，深入理解各模型的行为约束机制。
*   **教育学习**：作为生成式人工智能和LLM底层工作原理的教学案例资料。

4. **技术亮点**
*   **权威性与全面性**：覆盖OpenAI、Anthropic、Google、xAI四大巨头及其生态工具，数据源稀缺且完整。
*   **实时同步**：通过定期更新机制，确保获取最新模型版本（如GPT 5.5、Claude 5等）的第一手信息。
*   **开源共享**：以JavaScript格式开源，降低了其他开发者接入和二次利用的技术门槛。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52887 | 🍴 8627 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. 中文简介
该项目是一套为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松掌握AI知识。内容涵盖机器学习、深度学习及自然语言处理等核心领域，通过Jupyter Notebook提供交互式学习体验。作为Microsoft For Beginners系列的一部分，它致力于降低AI学习门槛，适合零基础的初学者系统性地构建知识体系。

### 2. 核心功能
*   **结构化课程体系**：提供12周分阶段的详细学习计划，确保循序渐进地掌握AI概念。
*   **交互式代码实践**：主要基于Jupyter Notebook，允许用户边学边写代码，即时验证理解。
*   **多模态技术覆盖**：课程内容广泛涉及计算机视觉（CNN）、生成对抗网络（GAN）、循环神经网络（RNN）及自然语言处理（NLP）。
*   **免费开源资源**：完全免费开放，由社区和专家共同维护，提供高质量的学习材料和示例。
*   **面向大众的教育定位**：专为非专业背景的初学者设计，语言通俗易懂，强调实用性与普及性。

### 3. 适用场景
*   **零基础自学**：适合没有任何编程或AI背景的人员，作为系统化入门的第一站。
*   **高校/培训机构教学**：可作为计算机科学或数据科学相关课程的补充教材或实验指导。
*   **职场技能提升**：希望快速了解AI基本概念和应用场景的非技术人员（如产品经理、市场人员）用于拓宽视野。
*   **兴趣探索与科普**：对人工智能充满好奇的公众，希望通过动手实践直观感受AI魅力的学习者。

### 4. 技术亮点
*   **微软背书与社区支持**：依托Microsoft For Beginners品牌，结合GitHub庞大的开源社区资源，保证内容的权威性与更新活力。
*   **实战导向的教学法**：摒弃纯理论堆砌，通过具体的Jupyter Notebook案例，让用户在解决实际问题中学习CNN、GAN等复杂模型。
*   **全面的知识图谱**：从传统机器学习到前沿的深度学习和NLP，覆盖了当前AI领域的主要技术栈，构建了完整的学习闭环。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51860 | 🍴 10474 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### GitHub 项目分析：ailearning

1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战、线性代数以及深度学习框架（PyTorch、TensorFlow 2）和自然语言处理工具（NLTK）的综合学习资源库。它旨在通过 Python 语言，为学习者提供从基础理论到高级算法应用的完整知识体系与实践指南。

2. **核心功能**
*   集成主流机器学习算法实战，包括 SVM、K-Means、逻辑回归及多种推荐系统模型。
*   涵盖深度学习核心架构实现，如 RNN、LSTM、DNN 及基于 PyTorch 和 TF2 的模型训练。
*   提供经典数据挖掘算法代码示例，如 Apriori、FP-Growth、PCA 和 SVD。
*   结合 NLP 自然语言处理技术，利用 NLTK 库进行文本分析与处理实战。

3. **适用场景**
*   **机器学习初学者入门**：适合希望从零开始系统掌握数据分析和基础 ML 算法的学习者。
*   **深度学习进阶实践**：适用于需要深入理解 RNN/LSTM 结构及 PyTorch/TF2 框架开发的开发者。
*   **算法面试准备**：可作为准备大厂技术面试的代码参考库，覆盖广泛的基础与进阶算法。

4. **技术亮点**
*   **全栈式技术覆盖**：同时整合了传统机器学习（Scikit-learn）、深度学习（PyTorch/TF2）及 NLP（NLTK）三大领域。
*   **高人气与社区认可**：拥有超过 42,000 颗星标，证明其在中文 AI 学习社区中具有极高的参考价值和使用率。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42360 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37587 | 🍴 6259 | 语言: Python
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
- ⭐ 25842 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库。它提供了完整的代码实现，是学习相关技术栈的重要参考资料。

2. **核心功能**
*   收录大量涵盖AI各细分领域的实战项目代码。
*   提供从基础机器学习到前沿深度学习的完整案例。
*   包含计算机视觉和自然语言处理的具体应用实例。
*   所有项目均附带可运行的源代码以便直接学习和测试。

3. **适用场景**
*   AI初学者构建知识库并快速上手实战项目。
*   数据科学家寻找特定算法或应用场景的代码参考。
*   开发者利用现有项目进行二次开发或技术调研。

4. **技术亮点**
*   作为Awesome列表，高度聚合了该领域的高星优质项目。
*   覆盖Python生态下主流AI框架的实际应用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35244 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化平台，能够模拟人类操作来执行复杂的浏览器工作流。它利用视觉理解和大型语言模型（LLM），无需编写传统代码即可自动处理网页交互任务。该项目旨在降低 RPA（机器人流程自动化）的技术门槛，实现更智能、更灵活的 Web 自动化。

2. **核心功能**
- 基于视觉感知的网页元素识别，无需依赖特定的 CSS 选择器或 XPath。
- 利用大语言模型理解页面上下文并动态生成操作指令。
- 支持多种浏览器自动化后端（如 Playwright），兼容现有自动化框架。
- 提供 API 接口，便于集成到现有的业务流程或自动化管道中。
- 具备处理复杂多步工作流的能力，包括登录、数据提取和表单填写。

3. **适用场景**
- 跨网站的重复性数据采集与信息整理。
- 自动化执行需要登录验证或复杂交互的在线事务（如报税、预订）。
- 替代传统 Selenium/Playwright 脚本，用于维护困难且易碎的 Web 自动化测试。
- 构建无代码或低代码的企业级 RPA 解决方案，以应对 UI 频繁变更的场景。

4. **技术亮点**
- 结合了计算机视觉与 LLM，使自动化机器人能像人一样“看懂”网页界面。
- 解耦了自动化逻辑与具体的 UI 结构，提高了对前端页面变更的鲁棒性。
- 开源且模块化设计，允许用户根据需求定制或扩展其自动化能力。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22148 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的领先平台，支持图像、视频及3D数据的AI辅助标注与团队协作。它提供开源、云端及企业级产品，并配套标签服务、质量保证及开发者API，助力视觉AI模型训练。

2. **核心功能**
*   支持图像、视频和3D数据的多种标注类型，如边界框、语义分割和图像分类。
*   集成AI辅助标注功能，显著提升数据标注效率并降低人工成本。
*   提供完善的质量保证机制、团队协作品台及数据分析工具。
*   开放开发者API，便于与其他机器学习工作流和系统集成。

3. **适用场景**
*   构建用于目标检测或语义分割的大规模计算机视觉训练数据集。
*   团队协作进行视频监控系统中的行为分析或安防事件标注。
*   需要高精度3D点云或图像标注的自动驾驶与机器人感知项目开发。

4. **技术亮点**
*   采用Python开发，深度兼容PyTorch和TensorFlow等主流深度学习框架。
*   提供从开源到企业级的灵活部署方案，满足不同规模团队的数据处理需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16245 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
本项目旨在为计算机视觉提供高级的可解释性AI工具，支持多种深度学习模型与任务类型。它涵盖了从卷积神经网络到视觉Transformer的各类架构，适用于分类、检测及分割等场景。

2. **核心功能**
- 支持CNN和Vision Transformers等多种主流视觉模型的可视化解释。
- 兼容图像分类、目标检测、语义分割及图像相似度计算等多种任务。
- 集成Grad-CAM、Score-CAM等经典可解释性算法实现。

3. **适用场景**
- 深度学习模型调试，用于定位模型关注的关键特征区域。
- 医疗影像分析，辅助医生理解AI诊断依据以提升信任度。
- 自动驾驶系统开发，验证车辆识别算法对交通标识的关注点。

4. **技术亮点**
- 广泛支持多种CAM变体算法，满足不同精度的可解释性需求。
- 良好的框架兼容性，无缝适配PyTorch生态下的各类视觉模型。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12901 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个基于 PyTorch 的几何计算机视觉库，专为空间人工智能（Spatial AI）设计。它旨在通过可微分的视觉原语，加速深度学习在计算机视觉领域的研究与开发进程。

2. **核心功能**
*   提供大量可微分的传统计算机视觉算法，无缝集成到 PyTorch 计算图中。
*   支持图像增强、几何变换及相机模型等底层视觉操作的原生化实现。
*   具备高效的批量处理能力，充分利用 GPU 加速提升图像处理性能。
*   内置多种空间推理和三维重建相关的数学工具与几何运算函数。

3. **适用场景**
*   **可微分渲染与图形学**：构建需要反向传播视觉操作的神经网络架构。
*   **机器人感知与控制**：在实时机器人系统中进行高精度的姿态估计与空间定位。
*   **数据增强流水线**：为深度学习模型训练提供多样化且可微分的图像预处理方案。
*   **自动驾驶环境理解**：处理车辆传感器数据以进行语义分割或深度估算。

4. **技术亮点**
*   实现了从 CPU 到 GPU 的无缝切换，保持与 PyTorch 生态系统的完全兼容性。
*   填补了传统计算机视觉与现代深度学习之间的接口空白，简化了复杂视觉任务的建模。
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
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，旨在让用户以“龙虾方式”（隐喻自主掌控数据）完全拥有自己的数据。它强调隐私与本地化部署，确保用户数据的私密性与控制权。

2. **核心功能**
*   跨平台兼容，支持在任意主流操作系统上运行。
*   提供个人化的 AI 助手体验，专注于用户特定需求。
*   强调“Own Your Data”理念，确保数据主权掌握在用户手中。
*   基于 TypeScript 开发，具备良好的可扩展性和维护性。
*   集成模块化架构，支持灵活配置和自定义插件。

3. **适用场景**
*   注重隐私保护、希望完全掌控个人数据的开发者或技术人员。
*   需要跨平台部署且对数据本地化有严格要求的企业或个人用户。
*   希望构建私有化、可定制 AI 助手的高级用户或极客群体。
*   寻求开源、透明且不受单一云服务厂商锁定的 AI 解决方案的项目。

4. **技术亮点**
*   采用 TypeScript 构建，保证了代码的类型安全和开发效率。
*   设计为平台无关性架构，实现真正的“Any OS, Any Platform”兼容性。
*   开源社区驱动，标签中包含“crustacean”等独特文化元素，增强社区认同感。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382106 | 🍴 80165 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 248641 | 🍴 22080 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210946 | 🍴 38728 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195558 | 🍴 59156 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185420 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165030 | 🍴 21362 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164027 | 🍴 30395 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156862 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151315 | 🍴 9469 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148079 | 🍴 23324 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

