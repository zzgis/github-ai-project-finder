# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- ### 1. 中文简介
TokHub 是一个基于 OpenAI 协议兼容性的专属网关系统，集 API 中转站监控、智能推荐与运营服务于一体。它支持分层探测、健康评分及用量计量等高级功能，并允许用户通过 Docker 进行自托管部署。

### 2. 核心功能
- **OpenAI 兼容网关**：提供标准的 OpenAI 接口协议，确保无缝接入现有应用生态。
- **多层健康监控**：支持分层探测与健康评分机制，实时评估各 API 源的服务状态。
- **精细化运营工具**：具备用量计量、告警审计及智能推荐功能，助力高效管理 API 资源。
- **容器化自托管**：原生支持 Docker 部署，便于用户在私有环境中快速搭建和维护服务。

### 3. 适用场景
- **API 聚合服务运营**：适合需要整合多个第三方 AI 供应商并统一对外提供服务的中间商。
- **企业内部 AI 网关**：适用于希望内部统一管理 AI 调用配额、监控使用情况并保障稳定性的企业团队。
- **高可用架构搭建**：适合追求服务高可用性，需要通过健康检查和自动切换来保障业务连续性的开发者。

### 4. 技术亮点
- **分层探测算法**：通过多层次的健康检查策略，更精准地识别和隔离故障节点，提升系统整体稳定性。
- **Docker 原生支持**：简化了部署流程，实现了开箱即用的环境配置，降低了运维复杂度。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 123 | 🍴 13 | 语言: TypeScript

### rocketplaneIO
- 1. **中文简介**
该项目是一个自托管的AI SRE解决方案，专为Kubernetes设计，结合了零侵入式的eBPF可观测性与具备安全护栏的自我验证修复功能的AI Copilot。它支持自带模型（BYO-LLM）及物理隔离环境，旨在通过自动化手段解决运维问题。

2. **核心功能**
*   基于eBPF实现零侵入式的全栈可观测性，无需修改应用代码即可采集数据。
*   集成AI Copilot，能够执行具备安全护栏且自我验证的操作以自动修复故障。
*   支持自带大语言模型（BYO-LLM），允许用户完全掌控AI推理过程。
*   具备空气间隙（Air-gapped）部署能力，满足高安全性环境的离线运行需求。

3. **适用场景**
*   对数据隐私和安全合规有极高要求的金融或政府机构，需在物理隔离环境中运行AI运维工具。
*   希望减少Kubernetes集群监控开销，同时利用自动化手段快速响应和修复生产事故的技术团队。
*   已有内部大模型资源，希望将其整合到运维流程中以实现智能化故障排查的企业。

4. **技术亮点**
*   采用eBPF技术实现高性能、低开销的系统级可观测性，结合ClickHouse和OpenTelemetry构建强大的数据分析与追踪能力。
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### Autonomous-Forge
- 1. **中文简介**
该项目是一个完全由AI构建和维护的自动化仓库，能够持续进行自我规划、编码、测试与优化。它代表了一种自进化的软件开发模式，旨在通过人工智能实现全生命周期的自动迭代。

2. **核心功能**
- 完全由AI自动生成代码和维持项目结构。
- 具备持续的自我规划能力，自动确定开发任务优先级。
- 集成自动化测试流程，确保代码质量与稳定性。
- 实现自我修复与改进，根据测试结果优化现有代码。

3. **适用场景**
- 探索和研究基于LLM的自主软件工程（Autonomous Software Engineering）。
- 作为AI辅助编程或“AI原生”开发工作流的参考原型。
- 用于演示或教学目的，展示代码生成的闭环自动化流程。

4. **技术亮点**
- 实现了从规划到测试再到改进的完整AI驱动闭环。
- 展示了无需人工干预的代码库自维护能力。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 69 | 🍴 1 | 语言: Python

### OpenAI4S
- 描述: 9.9 元豆包API复刻 Claude Science
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 63 | 🍴 6 | 语言: Python
- 标签: agent, ai4science, claude-science, mit-license, open-source

### motion-anything
- ### 1. 中文简介
Motion-Anything 是一个开源的、以聊天为原生的代理式动作层引擎。用户只需描述期望的感觉或意图，AI 即可自动将文字转化为相应的动画效果。它旨在降低动态设计的门槛，让非专业人士也能通过自然语言生成高质量的动效。

### 2. 核心功能
*   **自然语言驱动动画**：支持通过对话形式描述动作需求，由 AI 代理自动生成对应的动画。
*   **Chat-Native 交互体验**：内置聊天界面，提供直观且低代码的动画创作工作流。
*   **开源代理架构**：基于开放源码构建，具备可扩展的 AI 代理能力，便于开发者集成与定制。
*   **设计工具替代方案**：作为 Figma 等静态设计工具的补充或替代，专注于实现从设计到动态表现的转化。

### 3. 适用场景
*   **UI/UX 原型演示**：快速为网页或 App 界面生成微交互动画，用于展示交互逻辑。
*   **社交媒体内容制作**：为非设计师生成吸引眼球的动态图形，用于短视频或帖子配图。
*   **创意头脑风暴**：在早期设计阶段，通过文字描述快速验证不同动效风格的可能性。

### 4. 技术亮点
*   **多模型兼容**：标签显示支持 Claude 等 LLM，结合 WebGL 技术实现高性能的浏览器端渲染。
*   **语义化运动映射**：将抽象的情感或动作描述精准转换为具体的关键帧参数和物理属性。
- 链接: https://github.com/nexu-io/motion-anything
- ⭐ 30 | 🍴 5 | 语言: JavaScript
- 标签: ai-agent, animation, claude, design-tools, figma-motion-alternative

### C-SSH
- 描述: Native cross-platform SSH ops: persistent tmux sessions × always-on monitoring × built-in AI assistant. Windows/Android, free forever, open-source soon. 原生跨平台 SSH 运维 · tmux 持久化 · 常驻监控 · 内置 AI 助手
- 链接: https://github.com/suiyuebaobao/C-SSH
- ⭐ 26 | 🍴 3 | 语言: 未知
- 标签: ai, ai-assistant, android, cross-platform, devops

### TripStar-Java
- 描述: TripStar Java 实现版：基于 Spring Boot 4 + Spring AI Alibaba ReactAgent 的 AI 旅行规划后端，支持高德 Tool、小红书内容接入和 Structured Output。
- 链接: https://github.com/LeeFly-cn/TripStar-Java
- ⭐ 26 | 🍴 3 | 语言: JavaScript
- 标签: ai-agent, amap, java, react-agent, spring-ai

### fable5-methodology
- 描述: A transferable, self-enforcing software-engineering methodology for AI coding agents — playbook, skills, contracted subagents, lifecycle hooks, and evals.
- 链接: https://github.com/UnpaidAttention/fable5-methodology
- ⭐ 20 | 🍴 8 | 语言: Shell

### glm-5.2-free-desktop-app
- 描述: glm-5.2 free z.ai z-ai open source open-weights mit license mixture of experts moe artificial intelligence large language model 1m context window api key zenmux openrouter chat.z.ai browser interface coding agent claude code setup guide tutorial download documentation github huggingface benchmark performance terminal-bench
- 链接: https://github.com/zai-project/glm-5.2-free-desktop-app
- ⭐ 18 | 🍴 0 | 语言: C#
- 标签: ai-api-free, anthropic-, anthropic-claude, anthropic-outcomes, anthropic-sdk

### cf-proxy
- 描述: OpenAI-compatible Cloudflare Workers AI proxy with account-pool rotation and neuron tracking
- 链接: https://github.com/waguriagentic/cf-proxy
- ⭐ 16 | 🍴 11 | 语言: JavaScript

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个汇集了大量自然语言处理（NLP）资源、工具、数据集及预训练模型的综合性开源仓库。它不仅提供了从基础的数据清洗、分词、实体识别到高级的对话系统、知识图谱构建和语音处理的完整解决方案，还涵盖了丰富的中文垂直领域语料库。旨在为研究人员和开发者提供一个一站式的中英文NLP学习与开发资源中心。

2. **核心功能**
*   **基础NLP工具链**：提供中英文敏感词过滤、语言检测、分词、词性标注、命名实体识别（NER）及情感分析等基础处理功能。
*   **丰富语料与知识库**：收录了中日文人名库、行业词库（如财经、法律、医疗）、停用词、反义词库以及大规模中文对话和谣言数据集。
*   **预训练模型与算法**：集成了BERT、GPT-2、ALBERT、ELECTREA等主流预训练模型资源，以及多种文本生成、摘要和相似度匹配算法代码。
*   **垂直领域应用套件**：包含医疗、金融、法律等领域的专用知识图谱构建工具、问答系统（QA）及特定的业务逻辑处理（如车牌识别、手机号归属地查询）。
*   **数据标注与增强**：提供多种文本标注工具、数据增强方法（EDA）以及OCR文字识别和语音识别相关的预处理与评估工具。

3. **适用场景**
*   **NLP初学者学习与入门**：适合希望快速了解中文NLP技术栈、获取常用工具和基础数据集的学习者。
*   **企业级智能客服与聊天机器人开发**：可利用其中的对话语料、意图识别模型及多轮对话框架搭建垂直领域的智能问答系统。
*   **垂直行业知识图谱构建**：适用于需要处理医疗、金融或法律等专业领域数据的场景，借助其提供的专用词库和抽取工具进行结构化数据构建。
*   **文本内容安全与审核**：利用其内置的敏感词库、暴恐词表及谣言检测数据，快速部署内容过滤和合规性检查服务。

4. **技术亮点**
*   **资源极度聚合**：不仅包含代码，还整合了高质量数据集、预训练模型权重、技术报告及经典论文解读，极大降低了资源搜寻成本。
*   **全链路覆盖**：从底层的字符处理（如繁简转换、拼音标注）到上层的应用（如聊天机器人、知识图谱），覆盖了NLP的全生命周期。
*   **紧跟前沿技术**：持续更新包括BERT系列、GPT-2、ALBERT等最新预训练模型的应用案例和微调代码，保持技术时效性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81654 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **1. 中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目提供了丰富的实战案例，涵盖了从基础算法到前沿应用的广泛领域，旨在帮助开发者快速上手并深入理解相关技术。

**2. 核心功能**
*   提供涵盖机器学习、深度学习、CV和NLP等领域的500个完整项目示例。
*   所有项目均附带源代码，支持直接运行与学习参考。
*   分类清晰，便于用户根据特定技术领域（如计算机视觉或NLP）快速定位资源。
*   作为“Awesome”列表，精选了高质量且具代表性的开源项目供社区使用。

**3. 适用场景**
*   AI初学者希望通过大量实例快速掌握各类算法原理及代码实现。
*   数据科学家寻找特定任务（如图像分类、文本生成）的现成解决方案进行迁移学习。
*   教育者用于教学演示，展示从理论到实际代码落地的完整流程。
*   研究人员进行技术调研，快速了解当前主流AI项目的发展现状与技术栈。

**4. 技术亮点**
*   **规模庞大**：收录500个项目，覆盖面极广，是极具价值的资源库。
*   **代码驱动**：强调“with code”，确保每个概念都有可执行的代码支撑，利于实践。
*   **领域全面**：横跨AI核心子领域，包括传统机器学习、深度学习及其在CV和NLP中的应用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35234 | 🍴 7332 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持神经网络、深度学习和机器学习模型的可视化工具。它能够直观地展示模型的结构与数据流向，帮助用户快速理解和分析复杂的算法架构。

2. **核心功能**
*   支持多种主流框架模型的可视化，包括 TensorFlow、PyTorch、Keras、ONNX 等。
*   提供清晰的图形化界面，展示网络层结构、参数形状及数据维度。
*   兼容多种模型文件格式，如 CoreML、TensorFlow Lite 和 Safetensors。
*   允许用户通过浏览器或独立应用本地查看模型，无需上传至云端。

3. **适用场景**
*   深度学习研究人员调试模型结构，排查层连接错误。
*   工程师在部署前检查 ONNX 或 TensorFlow 模型的转换正确性。
*   初学者学习不同神经网络架构（如 CNN、RNN、Transformer）的具体实现细节。
*   团队内部协作时，用于直观展示和解释复杂机器学习模型的设计逻辑。

4. **技术亮点**
*   极高的格式兼容性，几乎覆盖了当前所有主流的 AI 模型标准。
*   基于 Web 技术构建，无需安装重型依赖即可在浏览器中运行，轻量且便捷。
*   开源免费，社区活跃，是 AI 领域事实上的标准模型查看器之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3149 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。通过统一模型表示，开发者可以更方便地在多种硬件平台和工具链上部署模型。

**2. 核心功能**
*   **跨框架兼容**：支持在 PyTorch、TensorFlow、Keras 等主流框架间无缝转换模型结构。
*   **标准化定义**：提供统一的算子集和模型格式定义，确保模型在不同环境下的可移植性。
*   **推理优化加速**：借助 ONNX Runtime 等运行时引擎，实现针对 CPU、GPU 及专用加速器的性能优化。
*   **生态互联**：连接开发框架与部署工具，简化从训练到生产环境部署的全流程。

**3. 适用场景**
*   **模型迁移与部署**：将训练好的模型从开发框架（如 PyTorch）转换为适合边缘设备或服务器运行的格式。
*   **混合框架协作**：在项目中结合使用多种框架的优势组件，并通过 ONNX 进行整合。
*   **硬件加速适配**：利用特定硬件厂商提供的 ONNX 转换器，最大化利用 GPU、NPU 等加速资源。

**4. 技术亮点**
*   **开源中立性**：由微软、Facebook 等科技巨头共同维护，保持中立且广泛接受的行业标准地位。
*   **高性能运行时**：配套的 ONNX Runtime 提供了高度优化的执行引擎，显著降低推理延迟并提升吞吐量。
- 链接: https://github.com/onnx/onnx
- ⭐ 21111 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一本开源的机器学习工程指南，旨在为大规模模型训练和部署提供最佳实践。它涵盖了从底层基础设施到上层应用的全栈工程知识，帮助开发者构建可扩展、高效的机器学习系统。

2. **核心功能**
*   提供大规模分布式训练的策略与调试技巧，解决扩展性难题。
*   深入解析GPU硬件特性及网络通信优化，提升推理与训练效率。
*   包含针对大型语言模型（LLM）和Transformers架构的工程化落地指南。
*   介绍存储管理、Slurm作业调度等基础设施层面的运维知识。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习集群的基础设施工程师。
*   致力于降低大型语言模型训练成本并提高收敛速度的算法研究员。
*   面临高并发推理压力，需进行模型服务化部署优化的MLOps团队。

4. **技术亮点**
*   聚焦于“工程实践”而非纯理论，提供可落地的代码级建议与故障排查方案。
*   紧跟前沿技术，特别针对当前热门的LLM领域提供了专门的优化章节。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18257 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17265 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3389 | 语言: 未知
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
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目提供了丰富的实战案例，涵盖了从基础算法到前沿应用的广泛领域，旨在帮助开发者快速上手并深入理解相关技术。

**2. 核心功能**
*   提供涵盖机器学习、深度学习、CV和NLP等领域的500个完整项目示例。
*   所有项目均附带源代码，支持直接运行与学习参考。
*   分类清晰，便于用户根据特定技术领域（如计算机视觉或NLP）快速定位资源。
*   作为“Awesome”列表，精选了高质量且具代表性的开源项目供社区使用。

**3. 适用场景**
*   AI初学者希望通过大量实例快速掌握各类算法原理及代码实现。
*   数据科学家寻找特定任务（如图像分类、文本生成）的现成解决方案进行迁移学习。
*   教育者用于教学演示，展示从理论到实际代码落地的完整流程。
*   研究人员进行技术调研，快速了解当前主流AI项目的发展现状与技术栈。

**4. 技术亮点**
*   **规模庞大**：收录500个项目，覆盖面极广，是极具价值的资源库。
*   **代码驱动**：强调“with code”，确保每个概念都有可执行的代码支撑，利于实践。
*   **领域全面**：横跨AI核心子领域，包括传统机器学习、深度学习及其在CV和NLP中的应用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35234 | 🍴 7332 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持神经网络、深度学习和机器学习模型的可视化工具。它能够直观地展示模型的结构与数据流向，帮助用户快速理解和分析复杂的算法架构。

2. **核心功能**
*   支持多种主流框架模型的可视化，包括 TensorFlow、PyTorch、Keras、ONNX 等。
*   提供清晰的图形化界面，展示网络层结构、参数形状及数据维度。
*   兼容多种模型文件格式，如 CoreML、TensorFlow Lite 和 Safetensors。
*   允许用户通过浏览器或独立应用本地查看模型，无需上传至云端。

3. **适用场景**
*   深度学习研究人员调试模型结构，排查层连接错误。
*   工程师在部署前检查 ONNX 或 TensorFlow 模型的转换正确性。
*   初学者学习不同神经网络架构（如 CNN、RNN、Transformer）的具体实现细节。
*   团队内部协作时，用于直观展示和解释复杂机器学习模型的设计逻辑。

4. **技术亮点**
*   极高的格式兼容性，几乎覆盖了当前所有主流的 AI 模型标准。
*   基于 Web 技术构建，无需安装重型依赖即可在浏览器中运行，轻量且便捷。
*   开源免费，社区活跃，是 AI 领域事实上的标准模型查看器之一。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3149 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了 essential 的速查手册（Cheat Sheets）。它涵盖了从基础理论到常用库函数的关键知识点，旨在帮助研究者快速回顾和查阅核心技术细节。

2. **核心功能**
*   提供深度学习和机器学习领域的标准化速查表。
*   涵盖 NumPy、SciPy 等数值计算库的核心用法。
*   包含 Matplotlib 数据可视化的关键绘图技巧。
*   集成 Keras 框架的模型构建与训练指南。
*   汇总人工智能相关的基础算法与概念摘要。

3. **适用场景**
*   研究人员在调试代码时快速查阅函数参数或语法。
*   学生在学习机器学习课程时作为复习辅助资料。
*   工程师在进行模型原型开发时参考最佳实践。
*   团队内部知识共享与技术培训的材料支撑。

4. **技术亮点**
*   内容高度浓缩，聚焦于高频使用的核心功能而非冗长文档。
*   整合了主流 AI 库（如 Keras、Matplotlib）的关键操作范式。
*   针对研究人员痛点优化，强调实用性与检索效率。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份详尽的人工智能学习路线图，整理了近200个实战案例并提供免费的配套教材，旨在帮助零基础用户快速入门并具备就业实战能力。内容涵盖Python、机器学习、深度学习、计算机视觉及自然语言处理等热门领域的核心技术栈。

2. **核心功能**
*   提供系统化的AI学习路径，从数学基础到高级算法逐步深入。
*   收录近200个实战案例，配套免费教材以强化动手实践能力。
*   覆盖主流框架与工具，包括TensorFlow、PyTorch、Keras及Pandas等。
*   聚焦热门应用领域，如计算机视觉（CV）、自然语言处理（NLP）及数据挖掘。

3. **适用场景**
*   希望从零开始系统学习人工智能技术的初学者。
*   需要通过大量实战案例提升就业竞争力的求职者。
*   想要梳理和更新机器学习、深度学习知识体系的技术人员。

4. **技术亮点**
*   全面整合了从基础库（NumPy, Matplotlib）到深度学习框架（TensorFlow2, PyTorch, Caffe）的技术栈。
*   强调“理论+实战”结合，通过近200个案例提供可直接参考的代码实现。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建过程。它通过声明式配置降低开发门槛，使研究人员和工程师能够更专注于数据与模型逻辑，而非底层工程实现。

### 2. 核心功能
*   **低代码/无代码建模**：通过简单的 YAML 配置文件即可定义复杂的深度学习架构，无需编写大量代码。
*   **广泛的模型支持**：原生支持从头训练、微调（Fine-tuning）各类预训练模型（如 LLaMA、Mistral 等），涵盖 NLP、计算机视觉及表格数据处理。
*   **端到端实验管理**：内置实验追踪、超参数优化及自动化模型评估功能，简化机器学习工作流。
*   **多种后端兼容**：支持 PyTorch、TensorFlow 及 Ray 分布式计算后端，适应不同规模的硬件资源。
*   **数据中心化设计**：强调数据驱动的方法，提供强大的数据预处理、验证集划分及特征工程工具。

### 3. 适用场景
*   **快速原型开发**：数据科学家或 ML 工程师需要快速验证假设并构建基准模型时。
*   **大规模模型微调**：对 LLaMA、Mistral 等大语言模型进行领域特定数据的微调训练。
*   **传统机器学习迁移**：希望将传统表格数据分析或多模态任务无缝迁移到深度学习框架的用户。
*   **教育与非专业开发者**：缺乏深厚编程背景但希望利用先进 AI 技术解决业务问题的团队。

### 4. 技术亮点
*   **声明式 API**：采用直观的 YAML 语法描述模型结构，显著降低配置复杂度和出错率。
*   **模块化架构**：组件高度解耦，允许用户轻松替换或扩展数据加载器、损失函数及评估指标。
*   **自动化预处理管道**：自动处理缺失值、标准化及嵌入查找，减少手动数据清洗工作。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9119 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8919 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6227 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81654 | 🍴 15253 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73033 | 🍴 8926 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目是一个定期更新的资源库，收集并提取了包括 Anthropic、OpenAI、Google 及 xAI 在内的多家主流 AI 厂商的核心系统提示词。内容涵盖 Claude、ChatGPT、Gemini 等多个知名模型及其专用版本（如 Code、Design、Thinking 模式）。旨在为研究者、开发者及爱好者提供关于大语言模型底层指令结构的参考数据。

2. **核心功能**
*   **多厂商提示词聚合**：整合来自 Anthropic、OpenAI、Google、xAI 等头部科技公司的系统提示词样本。
*   **覆盖主流模型变体**：不仅包含基础聊天模型，还涵盖代码助手、设计工具及思维链推理等特殊版本。
*   **定期动态更新**：随着各大模型版本的迭代，持续同步最新的系统提示词泄露或提取内容。
*   **开源知识库构建**：以 JavaScript 语言维护，结合“Awesome”列表形式，便于社区检索和使用。

3. **适用场景**
*   **提示词工程研究**：分析顶级模型的底层指令结构，优化自定义 Prompt 的设计策略。
*   **AI 安全与合规审计**：了解模型的系统级约束和潜在漏洞，辅助进行红队测试或安全评估。
*   **教育与技术分享**：作为教学案例，向初学者展示不同 AI 产品的内部工作逻辑和行为边界。

4. **技术亮点**
该项目最大的亮点在于其**时效性与覆盖面**，它不仅仅是一个静态列表，而是紧跟前沿 AI 模型迭代（如 Claude Opus 4.8、GPT 5.5 Thinking 等），提供了罕见的、第一手的商业模型系统指令样本，填补了公开研究中关于“黑盒”模型内部指令细节的信息空白。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52452 | 🍴 8540 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51837 | 🍴 10471 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数基础以及 PyTorch 和 TensorFlow 2 等深度学习框架的全面学习资源库。该项目结合了 NLTK 自然语言处理工具与 scikit-learn 等经典算法库，旨在为学习者提供从理论到实践的完整知识体系。它特别适合希望系统掌握机器学习及深度学习技术的开发者。

2. **核心功能**
*   集成经典机器学习算法（如 SVM、K-Means、Adaboost）的 Python 实现与实战案例。
*   提供基于 PyTorch 和 TensorFlow 2 的深度神经网络（DNN、RNN、LSTM）代码示例。
*   包含自然语言处理（NLP）模块，利用 NLTK 进行文本分析和推荐系统开发。
*   涵盖线性代数等数学基础，辅助理解机器学习背后的原理。
*   展示关联规则挖掘（Apriori、FP-Growth）及降维技术（PCA、SVD）的应用。

3. **适用场景**
*   初学者系统学习机器学习算法原理及其在 Python 中的落地实现。
*   数据科学家或工程师复习经典算法（如逻辑回归、聚类、分类）的最佳实践。
*   深度学习研究者探索基于 PyTorch/TensorFlow 2 的序列模型（RNN/LSTM）构建。
*   NLP 领域开发者使用 NLTK 进行文本预处理及基础自然语言任务分析。

4. **技术亮点**
*   技术栈全面，横跨传统机器学习、深度学习、NLP 及数学基础，形成闭环学习路径。
*   紧跟前沿框架，同时支持较新的 TensorFlow 2 和 PyTorch 以及经典的 scikit-learn。
*   高人气开源项目（4万+星标），拥有社区验证过的丰富实战案例和代码规范。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42360 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37564 | 🍴 6250 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35234 | 🍴 7332 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33720 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28397 | 🍴 3447 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25841 | 🍴 2902 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35234 | 🍴 7332 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22142 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉 AI 数据集的领先平台，支持图像、视频及 3D 数据的标注。它提供开源、云服务和企业版产品，具备 AI 辅助标注、质量控制及团队协作等强大功能。

2. **核心功能**
*   支持图像、视频和 3D 数据的多维度标注与 AI 辅助标记。
*   提供开源、云端和企业级多种部署模式及专业的标注服务。
*   内置质量保证机制、团队协作工具及数据分析功能。
*   开放开发者 API，便于集成到现有的深度学习工作流中。

3. **适用场景**
*   计算机视觉模型训练所需的高质量图像分类或目标检测数据集制作。
*   需要多人协作完成大规模视频或 3D 点云标注的企业级项目。
*   利用 AI 预标注功能加速语义分割或物体检测数据准备的研究场景。

4. **技术亮点**
*   深度融合 PyTorch 和 TensorFlow 生态，支持主流深度学习框架的数据需求。
*   提供从开源自托管到全托管云服务的全栈解决方案，灵活性极高。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16243 | 🍴 3739 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12901 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
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
- ⭐ 3455 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3273 | 🍴 400 | 语言: Python
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
- **1. 中文简介**
OpenClaw 是一款强调数据自主权的个人 AI 助手，支持跨操作系统和平台运行。它采用“龙虾方式”（Lobster Way），旨在让用户完全掌控自己的 AI 体验与数据隐私。该项目由 TypeScript 开发，是一个开源的本地化智能助理解决方案。

**2. 核心功能**
*   **全平台兼容性**：支持在任何主流操作系统和设备上部署运行。
*   **数据主权保障**：强调“Own Your Data”，确保用户数据完全私有且受控。
*   **个性化 AI 助理**：提供专属的个人人工智能助手功能，满足定制化需求。
*   **开源架构**：基于 TypeScript 构建，代码开源透明，便于社区贡献与二次开发。
*   **模块化设计**：通过“Crustacean”（甲壳类）等标签暗示其具备可扩展的模块化特性。

**3. 适用场景**
*   **注重隐私的个人用户**：希望拥有完全私有、不依赖第三方云服务的数据处理环境。
*   **跨平台开发者**：需要在 Windows、macOS 或 Linux 等不同系统间无缝切换 AI 工具的开发人员。
*   **本地化 AI 爱好者**：倾向于在本地部署开源大模型或轻量级 AI 助理的技术极客。

**4. 技术亮点**
*   基于 TypeScript 构建，具备良好的类型安全和现代前端/后端生态兼容性。
*   以“龙虾”为象征的品牌差异化设计，突显其开源、自由及数据掌控的核心理念。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382046 | 🍴 80140 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 基于您提供的GitHub项目信息，以下是关于 **superpowers** 的技术分析报告：

1. **中文简介**
   Superpowers 是一个经过验证的代理技能框架及软件开发方法论。它旨在通过结构化的技能库和子代理驱动的开发流程，提升软件开发生命周期（SDLC）的效率。该项目结合了AI协作与标准化开发流程，为开发者提供了一套切实可行的智能编码解决方案。

2. **核心功能**
   *   **代理技能框架**：提供模块化的“技能”集合，供AI代理在执行任务时调用，实现功能的按需组合。
   *   **子代理驱动开发**：采用多智能体协作模式，将复杂开发任务分解并由专门的子代理执行，优化工作流程。
   *   **结构化SDLC支持**：将AI能力整合进标准的软件开发生命周期，涵盖从头脑风暴到编码实现的完整环节。
   *   **智能头脑风暴辅助**：内置AI协作工具，帮助团队在需求分析和方案设计阶段进行高效创意发散。

3. **适用场景**
   *   **复杂系统架构设计**：利用多代理协作处理大型软件系统的模块划分与技术选型。
   *   **自动化代码生成与重构**：在已有代码基础上，通过调用特定技能自动完成代码补全或性能优化。
   *   **敏捷开发流程加速**：帮助开发团队快速从需求讨论过渡到可执行的技术方案，缩短迭代周期。

4. **技术亮点**
   *   **方法论与工具结合**：不仅提供代码工具，更强调“软件开发方法论”，定义了AI介入开发的标准化路径。
   *   **高社区认可度**：拥有近25万星标，表明其在AI辅助编程领域具有广泛的影响力和验证过的实用性。
   *   **跨语言兼容性**：虽然主要描述为Shell脚本环境，但其框架理念支持集成多种编程语言的智能代理行为。
- 链接: https://github.com/obra/superpowers
- ⭐ 248360 | 🍴 22028 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210734 | 🍴 38643 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款支持公平代码许可的工作流自动化平台，原生集成 AI 能力并支持 400 多种集成连接。它结合了可视化构建与自定义代码开发，用户可选择自托管或云端部署。

2. **核心功能**
*   提供可视化拖拽界面与自定义代码相结合的灵活工作流构建方式。
*   内置原生 AI 功能，支持智能自动化任务处理。
*   拥有超过 400 种应用集成，覆盖广泛的数据流与 API 交互场景。
*   支持自托管私有化部署及云端服务，保障数据隐私与控制权。
*   具备 MCP（模型上下文协议）客户端与服务端支持，增强与大模型的交互能力。

3. **适用场景**
*   企业级内部系统数据同步与跨平台 API 自动化集成。
*   利用 AI 助手自动处理客户反馈、文档摘要或生成内容。
*   开发者需要低代码快速原型搭建复杂业务逻辑工作流。
*   对数据隐私有高要求，需将自动化平台私有化部署的团队。

4. **技术亮点**
*   基于 TypeScript 开发，类型安全且易于扩展。
*   原生支持 MCP 协议，无缝对接各类大语言模型上下文。
*   采用 fair-code 许可证，平衡开源社区贡献与企业商业化需求。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195509 | 🍴 59142 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185416 | 🍴 46125 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164999 | 🍴 21360 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164012 | 🍴 30386 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156862 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151282 | 🍴 9458 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148034 | 🍴 23317 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

