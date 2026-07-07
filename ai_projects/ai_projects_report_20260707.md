# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- 1. **中文简介**
TokHub 是一个基于 TypeScript 开发的 OpenAI 兼容网关系统，集 API 中转站监控、推荐运营于一体。它支持 Docker 自托管，具备分层探测、健康评分、用量计量及告警审计等核心能力。

2. **核心功能**
*   提供 OpenAI 兼容的专属网关，支持 API 流量转发与管理。
*   内置分层探测与健康评分机制，实时监控各中转站状态。
*   实现详细的用量计量与告警审计功能，确保运营透明可控。
*   支持 Docker 自托管部署，便于用户快速搭建私有化环境。
*   集成推荐运营模块，优化 API 资源的调度与分发效率。

3. **适用场景**
*   需要自建 OpenAI 兼容接口以规避直接访问限制的技术团队。
*   希望集中管理多个 API 中转商资源并监控其稳定性的服务商。
*   对 API 调用成本敏感，需精确计量与审计用量的企业用户。
*   寻求轻量级、可自托管的 AI 网关解决方案的开发者。

4. **技术亮点**
*   采用 TypeScript 开发，类型安全且易于维护。
*   支持 Docker 一键部署，降低运维门槛。
*   独特的分层探测算法能更精准地评估中转站健康度。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 143 | 🍴 15 | 语言: TypeScript

### rocketplaneIO
- 描述: Self-hosted AI SRE for Kubernetes — zero-instrumentation eBPF observability plus a copilot that fixes issues through guardrailed, self-verifying actions. BYO-LLM, air-gapped capable.
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### motion-anything
- ### 1. 中文简介
Motion Anything 是一个开源的、以聊天原生的运动引擎，旨在成为智能体层面的动作层。用户只需通过自然语言描述期望的“感觉”或动态效果，AI 即可自动生成并交付相应的动画。它提供了一种无需复杂代码即可实现专业级动效设计的便捷方式。

### 2. 核心功能
*   **自然语言驱动动画生成**：支持通过对话式指令直接描述情感或视觉效果，由 AI 自动转化为动画。
*   **Figma 替代方案**：作为 Figma Motion 的开源替代品，提供类似的无缝设计到动效的工作流体验。
*   **Chat-Native 交互模式**：内置聊天原生界面，降低使用门槛，让非技术人员也能轻松操控复杂的运动图形。
*   **多平台兼容性**：基于 WebGL 技术构建，确保动画能在现代 Web 环境中高效渲染和运行。
*   **集成主流 AI 模型**：支持接入 Claude 等大语言模型，利用强大的语义理解能力精准解析用户的创意意图。

### 3. 适用场景
*   **UI/UX 设计师快速原型验证**：设计师可在 Figma 或其他设计工具旁，通过自然语言即时生成微交互动画原型，加速设计迭代。
*   **Web 开发中的动态内容展示**：前端开发者利用该引擎为网站添加个性化的数据可视化动画或品牌宣传效果，提升用户体验。
*   **营销素材自动化生产**：市场团队通过描述想要的“活力”或“优雅”感，批量生成用于社交媒体或广告横幅的短视频片段。
*   **教育与技术演示**：在技术分享或教学视频中，通过简单的文本指令快速生成复杂的几何变换或粒子特效，简化制作流程。

### 4. 技术亮点
*   **Agentic Workflow（智能体工作流）**：将传统的线性动画制作转变为由 AI 代理自主规划执行的交互式过程，极大提升了创作灵活性。
*   **语义到视觉的直接映射**：利用 LLM 的深度语义理解能力，将抽象的情感词汇（如“轻盈”、“沉重”）直接转化为具体的物理参数和关键帧。
*   **开源生态整合**：作为开源项目，易于集成到现有的 CI/CD 流水线或设计系统中，支持社区贡献和二次开发。
- 链接: https://github.com/nexu-io/motion-anything
- ⭐ 116 | 🍴 9 | 语言: JavaScript
- 标签: ai-agent, animation, claude, design-tools, figma-motion-alternative

### sail-skill
- 1. **中文简介**
SAIL V2（安全AI生命周期）作为一个智能体技能，提供了包含91项风险的全套目录，用于AI及智能体的差距评估、安全路线图制定和合规性检查。该技能兼容Claude Code、Codex、ChatGPT以及Antigravity等任意支持SKILL.md的智能体平台。

2. **核心功能**
*   提供涵盖91种风险的完整AI安全与合规性评估目录。
*   支持生成针对特定AI系统的差距分析报告与安全实施路线图。
*   具备跨平台兼容性，可无缝集成至多种主流代码助手及智能体环境。
*   通过标准化的SKILL.md格式实现即插即用的智能体扩展能力。

3. **适用场景**
*   企业在引入大型语言模型前进行内部安全风险评估与合规审计。
*   开发人员在构建AI代理应用时，快速集成标准化的安全检查清单。
*   安全团队制定企业级AI治理框架及长期安全防护路线图。
*   开发者在Claude Code或ChatGPT等环境中直接调用自动化安全审查流程。

4. **技术亮点**
*   采用通用的SKILL.md标准，实现了极高的平台互操作性。
*   将复杂的安全框架转化为轻量级的智能体技能，降低了落地门槛。
- 链接: https://github.com/pillar-labs/sail-skill
- ⭐ 116 | 🍴 0 | 语言: 未知
- 标签: agent-skills, agentic-ai, ai-security, claude-code, claude-code-plugin

### Autonomous-Forge
- 1. **中文简介**
这是一个完全由人工智能构建和维护的自动化项目，能够持续进行规划、编码、测试及自我优化。它实现了从开发到改进的全流程自主闭环，无需人工干预即可保持项目的迭代与完善。

2. **核心功能**
*   **全自动化构建**：项目代码完全由AI生成，无需传统的手动编码过程。
*   **持续自我改进**：系统能自动规划下一步行动并实施代码优化，实现版本的自我迭代。
*   **自主测试与验证**：内置自动化测试机制，确保新代码的质量并发现潜在缺陷。
*   **闭环维护**：涵盖规划、编码、测试到修复的完整生命周期管理，维持项目长期稳定运行。

3. **适用场景**
*   **AI驱动的开发实验**：用于研究或展示完全由大语言模型主导的软件开发生命周期。
*   **原型快速迭代**：需要快速生成可运行代码并进行自我修正的原型项目。
*   **自动化维护探索**：探索如何在无人工介入的情况下，通过自动化脚本和AI代理维护开源项目。

4. **技术亮点**
*   实现了“自举”能力，即项目本身即是其自身开发和优化的工具。
*   展示了AGI（通用人工智能）在软件工程领域的初步应用潜力，具备自我规划与执行代码重构的能力。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 92 | 🍴 2 | 语言: Python

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
- ⭐ 23 | 🍴 9 | 语言: Shell

### ccmux
- 描述: 🔮 Track all your AI coding agents (Claude Code, Codex, Cursor, ...) in tmux and jump to the one that needs you
- 链接: https://github.com/epilande/ccmux
- ⭐ 21 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, bun, claude, claude-code, cli

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
该项目是一个全面且强大的中文自然语言处理（NLP）资源库，涵盖了敏感词检测、实体抽取、情感分析及各类专业词库等基础工具。同时，它整合了众多前沿的预训练模型（如BERT、GPT）、知识图谱构建方案、语音识别数据集以及具体的NLP竞赛代码与实战案例。

2. **核心功能**
- **基础NLP工具**：提供中英文敏感词过滤、语言检测、分词、词性标注、句法分析及情感分析等实用模块。
- **丰富资源库**：包含人名、地名、公司名、行业术语（医/法/财/汽等）、成语、诗词及停用词等大规模专业词库。
- **模型与算法集成**：收录了BERT、ALBERT、RoBERTa等主流预训练模型的应用代码，以及NER、关系抽取、文本摘要等SOTA算法实现。
- **数据集与语料**：汇聚了中文闲聊、谣言检测、医疗对话、OCR语料及多项NLP竞赛的高质量数据集。
- **垂直领域应用**：提供知识图谱构建、智能问答系统、语音识别（ASR）及语音合成相关的开源工具与资源。

3. **适用场景**
- **NLP初学者与研究**：作为学习中文自然语言处理流程、获取标准数据集和参考基线模型（Baseline）的最佳入门资源。
- **企业级内容风控**：利用其敏感词库、情感分析和实体抽取能力，快速搭建内容审核、舆情监控或智能客服系统。
- **知识图谱构建**：借助其中的实体链接、关系抽取工具和百科数据，构建垂直领域的专业知识图谱。
- **算法工程落地**：直接复用项目中提供的BERT微调、文本生成或OCR识别等现成代码，加速业务功能的开发进程。

4. **技术亮点**
- **资源极度聚合**：不仅包含代码，还整合了数据、模型、论文解读和行业报告，是中文NLP领域的“百科全书”。
- **紧跟前沿技术**：及时收录了BERT、GPT-2、RoBERTa等最新预训练语言模型在中文场景下的微调与应用实践。
- **覆盖面广且深**：从基础的文本清洗到复杂的知识图谱推理、语音情感分析及对抗样本生成，覆盖了NLP的主要子领域。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它提供了完整的代码实现，旨在帮助开发者快速上手并深入理解各类人工智能技术的应用细节。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉的500+个完整项目代码示例。
*   包含从基础算法到前沿应用的多层次实战案例，适合不同阶段的学习者。
*   所有项目均附带可运行的代码，便于用户直接复现结果并进行修改实验。
*   作为“Awesome”系列资源，结构化地整理了高质量的AI工程实践参考。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习的基础代码结构。
*   工程师在开发具体AI功能（如图像识别或文本分析）时寻找可直接参考的代码模板。
*   学生或研究人员需要丰富的数据集处理模型构建案例来完成课程作业或学术验证。

4. **技术亮点**
*   **规模宏大且分类清晰**：一次性整合了500个项目，并按主流AI子领域进行精细标签分类，极大降低了资料搜集成本。
*   **全栈代码支持**：不仅提供理论，更强调“with code”，确保每个概念都有对应的工程落地代码，具备极高的实操参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35243 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。该工具旨在为开发者提供一个简单高效的模型调试与展示界面。

**2. 核心功能**
*   广泛支持 TensorFlow、PyTorch、ONNX、Keras 等主流框架的模型格式。
*   提供直观的图形化界面，清晰展示神经网络的层级结构与数据流向。
*   支持在本地计算机或浏览器中直接打开和预览模型文件。
*   允许用户查看各层的具体参数配置及张量形状信息。

**3. 适用场景**
*   **模型调试**：快速检查模型架构是否正确，定位层级连接错误。
*   **论文展示**：生成高质量的模型结构图，用于学术报告或技术文档。
*   **教育学习**：帮助初学者直观理解复杂神经网络（如 CNN、RNN）的内部运作机制。
*   **格式转换验证**：确认模型在不同框架间转换（如 PyTorch 转 ONNX）后结构保持一致。

**4. 技术亮点**
*   **多语言生态**：主要基于 JavaScript 开发，实现了跨平台兼容性和浏览器端无缝运行。
*   **轻量化设计**：无需安装庞大的深度学习环境即可快速加载和渲染大型模型。
*   **开源社区活跃**：拥有极高的星标数（33k+），表明其在 AI 开发者群体中具有广泛的认可度和影响力。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在促进不同深度学习框架之间的互操作性。它允许开发者在不同平台、工具和硬件之间轻松迁移模型，简化了从训练到部署的工作流。

2. **核心功能**
*   提供统一的模型表示格式，支持跨框架交换神经网络结构。
*   实现主流深度学习框架（如PyTorch、TensorFlow、Keras）与推理引擎间的双向转换。
*   优化模型性能，支持在多种硬件加速器上进行高效推理。
*   维护开放的规范文档和参考实现，确保社区兼容性与扩展性。

3. **适用场景**
*   需要在不同深度学习框架间迁移模型架构的研究或开发工作。
*   将训练好的模型部署到移动端、边缘设备或特定硬件加速器的生产环境。
*   希望在不锁定特定框架的前提下，构建可移植的机器学习流水线。

4. **技术亮点**
*   **生态兼容性极强**：作为AI领域的“通用语言”，无缝连接PyTorch、TensorFlow等主流框架与ONNX Runtime等推理引擎。
*   **模型优化友好**：支持算子融合与图优化，显著提升推理速度并降低延迟。
- 链接: https://github.com/onnx/onnx
- ⭐ 21113 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
《Machine Learning Engineering Open Book》是一本开源的技术指南，专注于机器学习工程领域的最佳实践与系统架构设计。该项目深入探讨了从大规模训练到高效推理的全流程工程挑战，旨在帮助开发者构建可扩展、高可靠的机器学习系统。

### 2. 核心功能
*   **全生命周期指导**：涵盖机器学习工程的训练、调试、部署及推理优化等关键环节。
*   **大规模分布式训练**：提供基于 PyTorch 和 Slurm 的大规模模型训练架构设计与扩展性策略。
*   **LLM 工程实践**：针对大型语言模型（LLM）的特定需求，分享微调、推理加速及内存优化技巧。
*   **基础设施管理**：详解 GPU 集群管理、网络通信优化及高性能存储解决方案。
*   **MLOps 体系构建**：整合机器学习运维流程，提升模型迭代效率与系统稳定性。

### 3. 适用场景
*   **大模型研发团队**：需要优化 Transformer 架构下的分布式训练效率及显存管理的工程师。
*   **MLOps 平台构建者**：希望建立标准化、自动化且具备高可扩展性的机器学习生产环境的团队。
*   **高性能计算研究者**：致力于解决超大规模参数模型在复杂网络环境下的通信瓶颈与调度问题。
*   **LLM 应用开发者**：寻求在生产环境中降低推理延迟、提升并发处理能力以优化用户体验。

### 4. 技术亮点
*   **实战导向**：基于真实的工业界案例，提供经过验证的工程解决方案而非纯理论探讨。
*   **深度聚焦 LLM**：针对当前最热门的大型语言模型领域，提供了细致的调试与性能调优指南。
*   **开源社区共建**：作为“开放书籍”形式持续更新，汇聚了广泛的技术专家贡献与最新技术动态。
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
该项目是一个汇集了500个AI相关实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它提供了完整的代码实现，旨在帮助开发者快速上手并深入理解各类人工智能技术的应用细节。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉的500+个完整项目代码示例。
*   包含从基础算法到前沿应用的多层次实战案例，适合不同阶段的学习者。
*   所有项目均附带可运行的代码，便于用户直接复现结果并进行修改实验。
*   作为“Awesome”系列资源，结构化地整理了高质量的AI工程实践参考。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习的基础代码结构。
*   工程师在开发具体AI功能（如图像识别或文本分析）时寻找可直接参考的代码模板。
*   学生或研究人员需要丰富的数据集处理模型构建案例来完成课程作业或学术验证。

4. **技术亮点**
*   **规模宏大且分类清晰**：一次性整合了500个项目，并按主流AI子领域进行精细标签分类，极大降低了资料搜集成本。
*   **全栈代码支持**：不仅提供理论，更强调“with code”，确保每个概念都有对应的工程落地代码，具备极高的实操参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35243 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- **1. 中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。该工具旨在为开发者提供一个简单高效的模型调试与展示界面。

**2. 核心功能**
*   广泛支持 TensorFlow、PyTorch、ONNX、Keras 等主流框架的模型格式。
*   提供直观的图形化界面，清晰展示神经网络的层级结构与数据流向。
*   支持在本地计算机或浏览器中直接打开和预览模型文件。
*   允许用户查看各层的具体参数配置及张量形状信息。

**3. 适用场景**
*   **模型调试**：快速检查模型架构是否正确，定位层级连接错误。
*   **论文展示**：生成高质量的模型结构图，用于学术报告或技术文档。
*   **教育学习**：帮助初学者直观理解复杂神经网络（如 CNN、RNN）的内部运作机制。
*   **格式转换验证**：确认模型在不同框架间转换（如 PyTorch 转 ONNX）后结构保持一致。

**4. 技术亮点**
*   **多语言生态**：主要基于 JavaScript 开发，实现了跨平台兼容性和浏览器端无缝运行。
*   **轻量化设计**：无需安装庞大的深度学习环境即可快速加载和渲染大型模型。
*   **开源社区活跃**：拥有极高的星标数（33k+），表明其在 AI 开发者群体中具有广泛的认可度和影响力。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33191 | 🍴 3151 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究者提供了 essential 速查表集合，旨在帮助研究人员快速回顾关键概念与代码实现。这些资源源自 Kailash Ahirwar 在 Medium 上发表的文章，涵盖了从基础理论到高级框架使用的实用指南。

### 2. 核心功能
*   提供机器学习与深度学习领域的核心概念速查。
*   包含常用 Python 库（如 NumPy、SciPy、Matplotlib）的代码示例。
*   集成深度学习框架（如 Keras）的关键操作指南。
*   以简洁的图表和代码片段形式呈现复杂技术细节。

### 3. 适用场景
*   研究人员在开始新项目时快速复习基础算法和数学原理。
*   开发者在调试模型时查阅特定库函数或配置参数的用法。
*   学生准备面试或考试时，利用速查表巩固机器学习知识体系。

### 4. 技术亮点
*   **高度结构化**：将分散的知识点整理为易于检索的速查表形式。
*   **实战导向**：直接关联代码实现，而非仅停留于理论定义。
*   **社区验证**：拥有超过 1.5 万星标，表明其在 AI 社区中具有较高的认可度和实用性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例并提供免费配套教材，旨在帮助零基础用户从入门到精通并实现就业。该项目涵盖 Python、数学基础、机器学习、深度学习及数据分析等热门领域，提供了从理论到实践的完整学习路径。

### 2. 核心功能
*   **系统化学习路线**：提供从零基础到就业实战的完整 AI 学习路径规划。
*   **丰富实战案例**：收录近 200 个精选项目与案例，强化动手实践能力。
*   **免费教学资源**：配套提供免费的学习教材和资源，降低入门门槛。
*   **多领域覆盖**：涵盖 Python 编程、数学基础、NLP、CV 及主流框架（PyTorch/TensorFlow）等关键技能。
*   **工具链集成**：整合 NumPy、Pandas、Matplotlib 等数据处理与分析常用库的使用教程。

### 3. 适用场景
*   **AI 初学者入门**：适合零基础的程序员或学生快速建立 AI 知识体系。
*   **求职技能提升**：适合希望进入 AI 行业的人员，通过实战案例准备面试和工作需求。
*   **高校教学参考**：可作为计算机相关专业的课程补充材料或项目实践指南。
*   **技术栈梳理**：适合需要系统复习和整理机器学习、深度学习技术栈的开发者。

### 4. 技术亮点
*   **社区热度高**：拥有超过 13,000 个星标，证明了其内容质量和社区认可度。
*   **全栈式覆盖**：不仅包含算法理论，还深入到底层数学基础和主流深度学习框架的具体应用。
*   **开源免费共享**：所有资源和路线图均免费开放，极大降低了高质量 AI 教育的获取成本。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型、神经网络及其他 AI 模型的构建过程。它通过声明式配置和自动化工作流，让开发者无需深入底层代码即可快速训练和优化机器学习模型。该项目支持多种前沿模型架构，极大降低了 AI 开发的门槛并提升了效率。

**2. 核心功能**
*   **低代码/无代码体验**：通过 YAML 配置文件定义模型结构，无需编写大量 Python 代码即可快速搭建原型。
*   **广泛的模型支持**：原生支持从传统表格数据到图像、文本、音频及多模态数据的深度学习模型训练。
*   **集成主流生态**：深度集成 PyTorch 等主流深度学习框架，并兼容 Hugging Face Transformers 中的 LLaMA、Mistral 等大语言模型。
*   **自动化数据处理**：内置自动化的数据预处理、特征工程及超参数优化功能，简化数据科学工作流。
*   **可解释性与可视化**：提供模型训练过程的详细日志和可视化报告，帮助开发者分析模型表现并进行调试。

**3. 适用场景**
*   **快速 AI 原型开发**：适合希望在不深入了解底层深度学习细节的情况下，迅速验证想法并构建基础 AI 模型的数据科学家。
*   **大语言模型微调**：适用于需要对 LLaMA、Mistral 等开源 LLM 进行领域适配或指令微调的企业和研究团队。
*   **多模态应用构建**：适合需要处理结合文本、图像或结构化数据的复杂业务场景，如内容审核或多模态检索系统。
*   **生产环境部署**：适用于需要将训练好的模型快速封装为 API 服务并进行标准化部署的工程团队。

**4. 技术亮点**
*   **声明式架构设计**：采用独特的 YAML 配置方式，使模型定义高度模块化且易于复用和维护。
*   **数据中心主义支持**：不仅关注算法，更强调数据质量与结构化管理，提供强大的数据验证和处理管道。
*   **高性能推理优化**：针对大规模模型训练和推理进行了优化，能够高效利用 GPU 资源加速实验迭代。
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
- ⭐ 6228 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
该项目是一个全面且强大的中文自然语言处理（NLP）资源库，涵盖了敏感词检测、实体抽取、情感分析及各类专业词库等基础工具。同时，它整合了众多前沿的预训练模型（如BERT、GPT）、知识图谱构建方案、语音识别数据集以及具体的NLP竞赛代码与实战案例。

2. **核心功能**
- **基础NLP工具**：提供中英文敏感词过滤、语言检测、分词、词性标注、句法分析及情感分析等实用模块。
- **丰富资源库**：包含人名、地名、公司名、行业术语（医/法/财/汽等）、成语、诗词及停用词等大规模专业词库。
- **模型与算法集成**：收录了BERT、ALBERT、RoBERTa等主流预训练模型的应用代码，以及NER、关系抽取、文本摘要等SOTA算法实现。
- **数据集与语料**：汇聚了中文闲聊、谣言检测、医疗对话、OCR语料及多项NLP竞赛的高质量数据集。
- **垂直领域应用**：提供知识图谱构建、智能问答系统、语音识别（ASR）及语音合成相关的开源工具与资源。

3. **适用场景**
- **NLP初学者与研究**：作为学习中文自然语言处理流程、获取标准数据集和参考基线模型（Baseline）的最佳入门资源。
- **企业级内容风控**：利用其敏感词库、情感分析和实体抽取能力，快速搭建内容审核、舆情监控或智能客服系统。
- **知识图谱构建**：借助其中的实体链接、关系抽取工具和百科数据，构建垂直领域的专业知识图谱。
- **算法工程落地**：直接复用项目中提供的BERT微调、文本生成或OCR识别等现成代码，加速业务功能的开发进程。

4. **技术亮点**
- **资源极度聚合**：不仅包含代码，还整合了数据、模型、论文解读和行业报告，是中文NLP领域的“百科全书”。
- **紧跟前沿技术**：及时收录了BERT、GPT-2、RoBERTa等最新预训练语言模型在中文场景下的微调与应用实践。
- **覆盖面广且深**：从基础的文本清洗到复杂的知识图谱推理、语音情感分析及对抗样本生成，覆盖了NLP的主要子领域。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81661 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和多模态大模型（VLM）进行训练。该项目获得了 ACL 2024 会议的认可，旨在简化大模型的微调流程。它提供了从基础指令微调到高级强化学习对齐的一站式解决方案。

2. **核心功能**
- 支持 100+ 种主流大语言模型和多模态模型的统一高效微调。
- 集成 LoRA、QLoRA、Galore 等多种参数高效微调（PEFT）算法。
- 提供完整的指令微调、监督微调及 RLHF（人类反馈强化学习）训练链路。
- 内置量化技术（如 QLoRA），降低显存占用并加速推理与训练。
- 兼容 Transformers、DeepSpeed 等主流深度学习库，便于灵活部署。

3. **适用场景**
- 研究人员或开发者希望快速复现论文结果或对特定模型进行指令微调。
- 资源受限环境下，需要使用量化技术（如 4-bit/8-bit）微调大型模型以节省显存。
- 企业或个人需要对私有数据进行监督微调（SFT）以提升模型在特定领域的表现。
- 需要利用 RLHF 技术对齐模型输出，使其更符合人类价值观和安全标准。

4. **技术亮点**
- **高度统一性**：通过统一接口支持极其广泛的模型架构，无需为每种模型编写专用代码。
- **极致效率**：结合 QLoRA 和 DeepSpeed 等技术，显著降低显存需求，使消费级显卡也能微调大模型。
- **前沿支持**：紧跟技术潮流，支持最新的 MoE（混合专家）、Gemma、Qwen 及 DeepSeek 等先进模型。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73044 | 🍴 8927 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目收集并提取了来自Anthropic、OpenAI、Google及xAI等主流厂商的最新大模型系统提示词（System Prompts），涵盖Claude、GPT、Gemini等知名模型。内容定期更新，旨在为开发者提供第一手的模型指令参考与学习资源。

2. **核心功能**
*   **多源汇聚**：整合了Anthropic、OpenAI、Google、xAI等多个顶级AI提供商的系统提示词。
*   **模型覆盖广**：包含Claude Fable/Opus系列、GPT 5.5系列、Gemini系列以及Cursor、Copilot等工具的内部提示词。
*   **持续更新**：项目维护团队定期同步最新泄露或公开的模型指令，保持数据时效性。
*   **开源共享**：以代码仓库形式开放所有提取的提示词文本，便于直接引用和测试。

3. **适用场景**
*   **Prompt工程研究**：通过分析官方系统提示词的结构和措辞，优化自定义提示词的设计。
*   **模型行为分析**：理解不同大模型的底层约束和安全策略，评估其输出逻辑。
*   **安全审计与红队测试**：利用已知系统指令进行对抗性测试，识别潜在的安全漏洞或越狱风险。
*   **AI教育学习**：作为教学资源，帮助初学者了解工业级大模型的指令体系差异。

4. **技术亮点**
*   **权威性与时效性**：直接获取自头部模型（如GPT 5.5、Claude 4.8等尚未广泛公开详细指令的版本），具有极高的参考价值。
*   **全面的生态覆盖**：不仅限于聊天机器人，还包含了代码助手（Codex、Cursor）和设计工具的系统指令，覆盖面极广。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52845 | 🍴 8610 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 以下是关于 GitHub 项目 **AI-For-Beginners** 的技术分析：

1. **中文简介**
该项目是一套为期12周、包含24节课的人工智能通识教育课程，旨在让所有人轻松入门 AI。内容涵盖从基础概念到深度学习应用的全面知识体系。它由微软发起，致力于降低人工智能的学习门槛。

2. **核心功能**
*   提供结构化的12周学习路径，分阶段系统讲解 AI 知识。
*   基于 Jupyter Notebook 实现交互式代码练习与即时反馈。
*   覆盖机器学习、计算机视觉、自然语言处理等主流 AI 领域。
*   包含 CNN、RNN、GAN 等深度学习核心算法的教学与实战。
*   作为 Microsoft For Beginners 系列的一部分，提供免费且开放的学习资源。

3. **适用场景**
*   零基础的编程或 AI 初学者进行系统性入门学习。
*   学校教师或企业培训师用于搭建人工智能课程大纲。
*   希望快速了解 AI 基本概念和技术趋势的非技术人员。
*   需要结合代码示例进行实践操作的 Python 学习者。

4. **技术亮点**
*   **全栈覆盖**：不仅讲解理论，还通过 Notebook 代码实例深入 CNN、NLP 和 GAN 等技术细节。
*   **教育友好**：课程设计遵循循序渐进原则，适合不同背景的学习者自驱学习。
*   **开源生态**：依托 GitHub 平台，便于社区贡献、代码复用及持续更新。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51859 | 🍴 10474 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个全面的AI学习资源库，涵盖了从数据分析、线性代数基础到深度学习框架（如PyTorch和TensorFlow 2）的实战内容。它整合了自然语言处理（NLTK）及多种经典机器学习算法，旨在为学习者提供系统的理论指导与代码实践。

2. **核心功能**
*   集成主流深度学习框架（PyTorch、TensorFlow 2）的自然语言处理与模型构建实战。
*   涵盖监督学习（SVM、逻辑回归、决策树等）与非监督学习（K-Means、PCA等）的经典算法实现。
*   包含推荐系统、关联规则挖掘（Apriori、FP-Growth）及集成学习（AdaBoost）的具体案例。
*   补充数学基础（线性代数）与数据预处理技能，夯实机器学习底层逻辑。

3. **适用场景**
*   计算机专业学生或初学者系统性地入门人工智能与机器学习领域。
*   希望从零搭建完整知识体系的数据分析师，需要结合理论与代码进行实操练习。
*   需要快速查阅和复现经典机器学习算法（如RNN、LSTM、SVD等）代码的开发者。

4. **技术亮点**
*   项目星标数高达42,360，表明其在社区内具有极高的认可度和广泛的使用群体。
*   内容跨度大，不仅包含应用层面的深度学习，还深入到底层数学原理与传统统计学习方法，结构完整。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42360 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37584 | 🍴 6259 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35243 | 🍴 7338 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33721 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28402 | 🍴 3452 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25842 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它提供了完整的代码实现，旨在帮助开发者快速上手并深入理解各类人工智能技术的应用细节。

2. **核心功能**
*   提供涵盖机器学习、深度学习、NLP和计算机视觉的500+个完整项目代码示例。
*   包含从基础算法到前沿应用的多层次实战案例，适合不同阶段的学习者。
*   所有项目均附带可运行的代码，便于用户直接复现结果并进行修改实验。
*   作为“Awesome”系列资源，结构化地整理了高质量的AI工程实践参考。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习的基础代码结构。
*   工程师在开发具体AI功能（如图像识别或文本分析）时寻找可直接参考的代码模板。
*   学生或研究人员需要丰富的数据集处理模型构建案例来完成课程作业或学术验证。

4. **技术亮点**
*   **规模宏大且分类清晰**：一次性整合了500个项目，并按主流AI子领域进行精细标签分类，极大降低了资料搜集成本。
*   **全栈代码支持**：不仅提供理论，更强调“with code”，确保每个概念都有对应的工程落地代码，具备极高的实操参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35243 | 🍴 7338 | 语言: 未知
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
- ⭐ 12901 | 🍴 1707 | 语言: Python
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
- ⭐ 382101 | 🍴 80160 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 248620 | 🍴 22079 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210929 | 🍴 38722 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195554 | 🍴 59156 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185419 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165027 | 🍴 21363 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164027 | 🍴 30395 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156863 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151312 | 🍴 9468 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148076 | 🍴 23324 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

