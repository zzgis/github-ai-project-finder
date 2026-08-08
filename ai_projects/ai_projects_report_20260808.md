# GitHub AI项目每日发现报告
日期: 2026-08-08

## 新发布的AI项目

### vibewatch
- ### 1. 中文简介
vibewatch 是一款专为 AI 辅助编程（Vibe Coding）设计的触觉 M5Stack 秒表控制器。它通过 BLE HID 协议实现物理交互，让开发者能以更直观、手感化的方式控制编码节奏与流程。

### 2. 核心功能
- 基于 M5Stack 硬件打造物理秒表控制器，提供触觉反馈。
- 支持 BLE HID 协议，可将设备模拟为键盘/输入源与电脑通信。
- 针对 AI 辅助编程场景优化，提升编码节奏控制体验。
- 使用 PlatformIO 在 ESP32-S3 平台上进行开发部署。

### 3. 适用场景
- AI 辅助编程时，用物理按钮控制代码生成节奏或触发快捷键。
- 需要减少键盘依赖、通过触觉交互提升专注力的编码工作流。
- 开发者希望将 M5Stack 设备用作自定义 HID 输入工具的实验项目。

### 4. 技术亮点
- 结合 ESP32-S3 的 BLE 能力与 M5Stack 硬件，实现低延迟无线 HID 控制。
- 聚焦“Vibe Coding”新兴范式，将物理交互与 AI 编程工具链无缝集成。
- 链接: https://github.com/GOROman/vibewatch
- ⭐ 41 | 🍴 2 | 语言: C++
- 标签: ai, ble-hid, esp32-s3, m5stack, m5stack-stopwatch

### anti-slop
- 1. **中文简介**  
该项目旨在制定设计规范，阻止AI编程代理生成千篇一律的“AI垃圾”用户界面。它提供了一套设计规则，帮助开发者避免AI生成的UI缺乏个性与质量的问题。

2. **核心功能**  
- 提供防止AI生成低质量UI的设计准则  
- 帮助开发者识别并避免通用化、模板化的界面输出  
- 适用于AI辅助编程场景中的前端开发  
- 无代码实现，属于设计指导类资源  
- 强调创意与实用性结合，避免AI堆砌元素  

3. **适用场景**  
- 使用AI编程工具（如Cursor、GitHub Copilot）开发Web应用时  
- 希望UI具有独特性而非AI默认风格的项目  
- 团队协作中统一AI生成界面的设计标准  
- 对AI生成代码质量不满的开发者改进方案  

4. **技术亮点**  
- 聚焦当前AI编程热点痛点，具有前瞻性  
- 无代码依赖，易于理解和采纳  
- 可作为团队规范或AI提示词（prompt）的参考依据
- 链接: https://github.com/miqdadbadjuber/anti-slop
- ⭐ 37 | 🍴 4 | 语言: 未知

### open-kimi-ppt-skill
- 1. **中文简介**
这是 Kimi Slides 的非官方版本，专为 AI Agent 设计。它支持生成可直接编辑的 PPT 文件（包括 PPTD 和 PPTX 格式），并集成本地浏览器编辑器以提升用户体验。

2. **核心功能**
- 允许 AI Agent 自动生成可编辑的演示文稿文件。
- 支持导出为 PPTD 和 PPTX 两种常见格式。
- 内置本地浏览器编辑器，方便用户直接在线修改内容。
- 作为非官方 Skill 运行，兼容 Kimi 生态的 Agent 调用方式。

3. **适用场景**
- AI 助手集成：在 Kimi 等 AI Agent 平台中快速生成演示文稿。
- 自动化办公：批量或按需生成可编辑的 PPT 用于工作汇报。
- 本地化编辑需求：希望在不依赖云端服务的情况下进行 PPT 编辑和修改。

4. **技术亮点**
- 实现了从 AI 生成到本地可编辑文件的完整闭环。
- 结合本地浏览器编辑器，确保生成的 PPTX/PPTD 文件可直接打开并二次编辑。
- 链接: https://github.com/Wolfsin/open-kimi-ppt-skill
- ⭐ 27 | 🍴 90 | 语言: 未知

### Kimi-K3-Code-Free-Desktop-AI
- ### 项目分析：Kimi-K3-Code-Free-Desktop-AI

**1. 中文简介**
这是一款基于 Moonshot AI Kimi K3 模型的本地桌面 AI 编程助手，支持 2.8T 参数及 100 万上下文窗口。它作为 GitHub Copilot 的免费替代方案，具备终端编码代理、多文件上传及自主任务执行能力，旨在为用户提供免费的本地化 AI 编程解决方案。

**2. 核心功能**
*   **免费 API 接入**：提供 Kimi K3/K2 模型的免费访问接口，无需付费订阅。
*   **超长上下文处理**：支持 100 万 token 上下文，能够处理大型代码库和长文档。
*   **终端编码代理**：集成终端功能，可作为智能编程代理自动执行代码任务。
*   **多文件上传与分析**：支持上传多个代码文件，进行全局代码理解和辅助编程。
*   **桌面端自主运行**：本地部署的桌面应用，支持自主任务规划与执行。

**3. 适用场景**
*   **大型代码库重构**：利用超长上下文能力，对包含数十万行代码的项目进行整体分析和重构。
*   **替代付费编程助手**：开发者寻求 GitHub Copilot 等商业产品的免费替代方案时。
*   **自动化编程任务**：需要 AI 代理在终端中自主完成代码生成、调试或脚本编写任务。
*   **本地化隐私保护开发**：希望在不将代码上传至云端服务器的情况下，使用强大的 AI 辅助编程。

**4. 技术亮点**
*   采用 TypeScript 开发，具备良好的跨平台兼容性和现代前端生态集成能力。
*   深度整合 Kimi K3 模型的长文本理解优势，突破传统编程助手上下文限制。
- 链接: https://github.com/kimi-k3code/Kimi-K3-Code-Free-Desktop-AI
- ⭐ 21 | 🍴 0 | 语言: TypeScript
- 标签: ai-api-free, ai-desktop, desktop-ai, free-ai-tools, k2-7

### Verity-JE-BE-Mod-Minecraft
- 1. **中文简介**  
Verity Minecraft Mod 是一款支持 Java 版与基岩版（Bedrock Edition）的恐怖实体模组，由 ThatMob 开发。模组内置 AI 对话系统与自适应行为机制，专注于营造心理恐怖体验。截至 2026 年，该模组已获得超过 860 万次下载，兼容 Minecraft 1.21.x 及基岩版 26.40。

2. **核心功能**  
- 支持 Java 版（Forge）与基岩版双平台运行，实现跨版本兼容。  
- 内置 AI 驱动的非玩家角色（实体）对话系统，增强互动沉浸感。  
- 实体具备自适应行为逻辑，可根据玩家行动动态调整恐怖反应。  
- 专注于心理恐怖氛围营造，而非依赖跳跃惊吓（jump scare）。  
- 提供免费下载，支持 1.21.x 及 26.40 基岩版最新游戏版本。

3. **适用场景**  
- 玩家希望在 Minecraft 中体验带有智能对话与心理压迫感的恐怖内容。  
- 服务器管理员为多人游戏服务器（MC Server）添加具有行为多样性的恐怖模组。  
- All the Mods 或 Skyblock 等整合包作者希望引入高质量、低侵入性的恐怖元素。  
- 模组开发者研究 AI 对话与自适应行为在 Minecraft 环境中的实现方式。

4. **技术亮点**  
- 实现 Java 版与基岩版双端兼容，降低跨平台部署门槛。  
- 采用 AI 对话框架，使恐怖实体具备动态、非脚本化的交互能力。  
- 自适应行为系统可根据玩家距离、视线、声音等变量实时调整实体反应，提升恐怖沉浸感。
- 链接: https://github.com/verityminecraft/Verity-JE-BE-Mod-Minecraft
- ⭐ 21 | 🍴 0 | 语言: Java
- 标签: 1-16-5, 1-8, all-the-mods-modpack, allthemods, evernym-verity

### Meta-Muse-Spark-1.2-Free-Desktop-App
- 描述: Meta Muse Spark 1.2 Free - Terminal coding agent, 1M context,Free API, 82.9% Terminal-Bench. Repo-scale execution, parallel agents, worktree isolation. Free AI coding assistant 2026.
- 链接: https://github.com/metaspark12/Meta-Muse-Spark-1.2-Free-Desktop-App
- ⭐ 21 | 🍴 0 | 语言: TypeScript
- 标签: facebook-automation, facebookai, llama3-meta-ai, meta-agent, meta-ai

### Google-Gemini-Desktop
- 描述: Google Gemini Desktop Free - Advanced AI assistant for Windows 10/11. Gemini 3.6 Flash, 3.5 Pro, Ultra models. Code generation, image analysis, 2M context window. No subscription. Offline mode. Download latest version 2026.
- 链接: https://github.com/googlegeminiapp/Google-Gemini-Desktop
- ⭐ 21 | 🍴 0 | 语言: TypeScript
- 标签: free-gemini-api, gemini-, gemini-15-pro, gemini-2-0-flash, gemini-2-5-flash

### slopware-skills
- 描述: Free, portable AI agent skills and plugins for Codex, Claude Code, and Agent Skills clients by Slopware Engineer (@aienginerd). Home of the MSW Kernel for Minimum Sufficient Work.
- 链接: https://github.com/transcendr/slopware-skills
- ⭐ 19 | 🍴 1 | 语言: 未知
- 标签: agent-plugins, agent-skills, ai-agents, ai-coding-agent, claude-code

### aimbot-android-script-hub
- 描述: Android mobile game script utility offering configurable target tracking and aiming assistance. Features custom parameter setup and regular 2026 updates.
- 链接: https://github.com/andre-james21/aimbot-android-script-hub
- ⭐ 16 | 🍴 0 | 语言: HTML

### see-my-video
- 描述: 让 AI 真的看见你发的视频：抽帧喂给模型，以及自建服务器上传视频的两个隐形坑
- 链接: https://github.com/eveacla11/see-my-video
- ⭐ 14 | 🍴 2 | 语言: Python
- 标签: ai, claude, ffmpeg, self-hosted, video

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**
funNLP 是一个专为中文自然语言处理设计的综合性工具库，由 HuJiFa 创建并维护。它集成了敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）以及丰富的词库资源，旨在为开发者提供一站式的中英 NLP 解决方案。

2. **核心功能**
*   **基础 NLP 工具**：支持中英文敏感词过滤、语言检测、繁简体转换及中英文标点规范化。
*   **实体与信息抽取**：提供手机号、身份证号、邮箱、人名、地名的自动抽取与校验功能。
*   **丰富词库资源**：内置中日文人名的常见姓氏库、中文缩写库、停用词表、情感值词典及大量垂直领域词库（如汽车、医疗、法律、IT 等）。
*   **语音与文本生成**：包含英文模拟中文发音、汪峰歌词生成器、自动对联及基于 GPT-2 的文本生成示例。
*   **预训练模型与数据集**：汇总了 BERT、ALBERT、RoBERTa 等主流预训练模型资源，以及多个中文 NLP 竞赛数据集和基准测试集。

3. **适用场景**
*   **内容安全审核**：用于互联网平台的敏感词过滤、违禁词检测及谣言识别。
*   **信息抽取与结构化**：从非结构化文本（如简历、新闻、对话记录）中快速提取关键实体信息。
*   **中文 NLP 研究入门**：适合学生和研究者快速搭建中文分词、词性标注、情感分析等基础 NLP 流水线。
*   **垂直领域知识库构建**：利用其丰富的领域词库（医疗、法律、金融等）辅助构建特定行业的知识图谱或问答系统。

4. **技术亮点**
*   **资源聚合性强**：不仅提供代码工具，还整理了大量高质量的中文 NLP 数据集、预训练模型和学术资源链接，是中文 NLP 领域的“资源黄页”。
*   **开箱即用**：封装了常用的正则表达式和规则引擎，无需复杂配置即可实现敏感词过滤、实体抽取等功能。
*   **社区活跃度高**：作为 GitHub 上星标数极高的中文 NLP 项目，持续更新并整合了最新的模型（如 BERT、GPT-2）和应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82335 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**  
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和NLP项目的代码库合集，涵盖从基础到高级的完整学习路径。项目以Python为主要实现语言，提供可运行的代码示例，适合系统性地掌握AI相关技术。

2. **核心功能**  
- 收录500个涵盖AI、机器学习、深度学习、计算机视觉和NLP领域的完整项目代码  
- 提供从入门到进阶的系统化学习路径  
- 所有项目均附带可运行的Python代码示例  
- 项目按领域分类，便于针对性学习与实践  
- 适合个人学习、课程教学及项目参考

3. **适用场景**  
- AI初学者系统学习机器学习、深度学习及NLP/计算机视觉技术  
- 高校或培训机构用于课程设计、作业参考和项目实践  
- 开发者快速查找特定AI任务的实现范例（如图像分类、文本生成等）  
- 技术面试准备，通过实战项目巩固算法与工程能力

4. **技术亮点**  
项目覆盖面广，整合了当前AI主流方向的典型实现，且全部提供代码，便于“边学边做”，是GitHub上星标数超过3.6万的优质开源学习资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36036 | 🍴 7411 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**  
Netron 是一个神经网络、深度学习和机器学习模型的可视化工具，支持多种主流框架格式，帮助用户直观查看模型结构与数据流向。

2. **核心功能**  
- 支持导入并可视化多种模型格式（如 ONNX、TensorFlow、PyTorch、Core ML 等）  
- 提供清晰的层结构树状视图与计算图展示  
- 可在本地或浏览器中运行，无需安装复杂依赖  
- 支持查看张量形状、权重参数及模型元数据  
- 兼容 safetensors 等新兴模型格式

3. **适用场景**  
- 模型调试：快速定位网络结构错误或层连接问题  
- 教学演示：直观展示神经网络内部工作原理  
- 模型迁移：对比不同框架下同一模型的表示差异  
- 文档生成：导出模型结构图用于技术报告或论文

4. **技术亮点**  
- 纯前端实现，支持桌面应用与 Web 版本无缝切换  
- 轻量高效，即使处理大型模型也能保持流畅交互  
- 开源活跃，社区持续扩展对新框架和格式的支持
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- **1. 中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准，旨在促进不同深度学习框架之间的模型交换与部署。它允许开发者在不同平台（如PyTorch、TensorFlow等）上轻松转换和运行模型，提升跨框架协作效率。

**2. 核心功能**
- 提供统一的模型格式，支持跨框架模型转换与互操作。
- 兼容主流深度学习框架，如PyTorch、TensorFlow、Keras和scikit-learn。
- 支持模型在多种硬件平台上的高效部署，包括CPU、GPU和边缘设备。
- 提供丰富的算子库，覆盖常见神经网络结构。
- 拥有活跃的社区支持，持续更新和优化标准。

**3. 适用场景**
- 在PyTorch和TensorFlow之间迁移模型，实现无缝转换。
- 将训练好的模型部署到移动端或嵌入式设备上运行。
- 在工业环境中统一模型格式，简化模型管理和维护流程。
- 跨团队协作开发，确保不同框架下的模型兼容性。

**4. 技术亮点**
- 作为行业标准，ONNX被广泛采用，成为连接不同框架的桥梁。
- 支持动态形状（dynamic shapes），提升模型灵活性。
- 提供可视化工具，帮助开发者调试和优化模型结构。
- 持续扩展对新算子和框架的支持，保持技术领先性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21277 | 🍴 3985 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
《机器学习工程开放手册》是一本全面涵盖机器学习工程实践的开源指南，聚焦于大模型训练、推理及部署的核心技术。内容涵盖PyTorch优化、GPU集群管理、网络通信、存储系统及可扩展性设计等关键领域。

### 2. 核心功能
- **大模型训练优化**：提供LLM训练中的调试技巧、分布式训练策略及Slurm集群管理方案。
- **推理与部署实践**：详解模型推理加速、内存优化及生产环境部署的最佳实践。
- **基础设施工程**：涵盖GPU硬件选型、网络拓扑优化及大规模存储系统设计。
- **可扩展性架构**：指导如何构建支持千卡级并行训练的高可用机器学习系统。
- **PyTorch深度调优**：包括性能剖析、显存管理及Transformer框架底层优化技巧。

### 3. 适用场景
- **大语言模型训练团队**：需要搭建和优化千卡级LLM训练集群的工程团队。
- **MLOps工程师**：负责模型从实验到生产部署全流程的基础设施构建与维护。
- **AI系统研究员**：研究分布式训练效率、GPU通信瓶颈及系统级性能优化的学者。
- **深度学习平台开发者**：构建内部机器学习平台，需参考生产级工程实践的技术负责人。

### 4. 技术亮点
- **实战导向**：内容源自工业界大规模部署的真实经验，非纯理论阐述。
- **全栈覆盖**：从底层GPU驱动、网络通信到上层训练框架，提供端到端解决方案。
- **持续更新**：作为开放手册，紧跟LLM技术演进，涵盖最新优化技术（如FlashAttention、ZeRO等）。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18537 | 🍴 1192 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17351 | 🍴 2118 | 语言: 未知
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
- ⭐ 10686 | 🍴 5704 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的大型资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并附带完整代码。它旨在为学习者提供从入门到进阶的全方位实践案例，适合不同层次的技术爱好者参考使用。

2. **核心功能**
- 提供500个涵盖AI主要领域的完整项目代码示例
- 包含机器学习、深度学习、计算机视觉和NLP等多方向实战案例
- 作为系统学习AI技术的结构化资源库和参考手册
- 支持从零开始到高级应用的渐进式学习路径

3. **适用场景**
- 初学者系统学习AI/ML/DL技术时的实践参考
- 开发者寻找特定算法或应用场景的代码实现灵感
- 学生或研究人员进行项目开发和论文实验的素材库
- 技术面试准备中快速复习和练习常见AI项目

4. **技术亮点**
- 项目数量庞大（500个），覆盖AI领域主流方向
- 所有项目均附带可运行的代码，便于直接学习和修改
- 被广泛标记为"awesome"资源，社区认可度高（36036星标）
- 整合了Python生态中多个AI框架的典型应用案例
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36036 | 🍴 7411 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**  
Netron 是一个神经网络、深度学习和机器学习模型的可视化工具，支持多种主流框架格式，帮助用户直观查看模型结构与数据流向。

2. **核心功能**  
- 支持导入并可视化多种模型格式（如 ONNX、TensorFlow、PyTorch、Core ML 等）  
- 提供清晰的层结构树状视图与计算图展示  
- 可在本地或浏览器中运行，无需安装复杂依赖  
- 支持查看张量形状、权重参数及模型元数据  
- 兼容 safetensors 等新兴模型格式

3. **适用场景**  
- 模型调试：快速定位网络结构错误或层连接问题  
- 教学演示：直观展示神经网络内部工作原理  
- 模型迁移：对比不同框架下同一模型的表示差异  
- 文档生成：导出模型结构图用于技术报告或论文

4. **技术亮点**  
- 纯前端实现，支持桌面应用与 Web 版本无缝切换  
- 轻量高效，即使处理大型模型也能保持流畅交互  
- 开源活跃，社区持续扩展对新框架和格式的支持
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33323 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ## 项目分析：cheatsheets-ai

### 1. 中文简介
该项目为深度学习与机器学习研究者提供了核心速查手册，内容涵盖从基础数学工具到高级模型实现的完整知识体系。项目基于Medium文章整理而成，旨在帮助研究人员快速查阅关键概念与代码实现。

### 2. 核心功能
- 提供机器学习与深度学习领域的核心概念速查表
- 涵盖NumPy、SciPy、Matplotlib等基础科学计算库的使用技巧
- 包含Keras框架的常用模型构建与训练方法
- 集成深度学习关键算法的数学原理与代码示例
- 支持研究人员快速回顾和查阅专业知识

### 3. 适用场景
- 深度学习研究者快速查阅数学工具和算法原理
- 机器学习工程师复习NumPy/SciPy等科学计算库的使用
- 数据科学家参考Keras模型构建的最佳实践
- 学生备考或复习人工智能相关课程的核心知识点

### 4. 技术亮点
- 项目聚焦于实用性和查阅效率，以速查表形式呈现核心知识
- 标签覆盖AI、深度学习、Keras、机器学习、数据可视化等关键技术领域
- 高星标数（15427）表明其在研究者社区中具有广泛认可度和实用价值
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3376 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，收录了近 200 个实战案例与项目，并免费提供配套教材，助力零基础用户入门并实现就业实战。项目涵盖 Python、数学、机器学习、深度学习、计算机视觉及自然语言处理等热门领域，支持 PyTorch、TensorFlow 等多种主流框架。

2. **核心功能**
- 提供系统化的 AI 学习路线图，覆盖从基础到进阶的完整知识体系。
- 整理近 200 个实战案例与项目，帮助学习者通过实践巩固技能。
- 免费提供配套教材和资源，降低零基础入门的学习门槛。
- 涵盖 Python、数学、数据分析、深度学习及 NLP/CV 等核心领域。

3. **适用场景**
- 希望从零开始系统学习人工智能的初学者。
- 需要通过大量实战项目提升动手能力、准备求职的技术人员。
- 想要梳理机器学习、深度学习或数据分析知识体系的学习者。

4. **技术亮点**
- 项目高度集成，同时支持 TensorFlow、PyTorch、Keras、Caffe 等多种主流深度学习框架。
- 内容覆盖面广，结合算法理论与 numpy、pandas、matplotlib 等实用工具链。
- 社区热度高，拥有超过 1.3 万星标，证明其资源质量和受欢迎程度。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13235 | 🍴 2668 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- # Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它简化了从数据处理到模型训练的完整流程，让开发者无需编写大量代码即可快速搭建和微调机器学习模型。

## 2. 核心功能
- **低代码建模**：通过声明式配置即可定义和训练神经网络，无需深入编码。
- **多模态支持**：原生支持文本、图像、表格等多种数据类型，适用于 NLP 和计算机视觉任务。
- **端到端流水线**：内置数据预处理、特征工程、模型训练和评估的完整工作流。
- **主流框架兼容**：基于 PyTorch 构建，无缝对接 Hugging Face Transformers，支持 LLaMA、Mistral 等主流 LLM。
- **自动化微调**：提供一键微调功能，方便对预训练模型进行领域适配。

## 3. 适用场景
- **快速原型开发**：数据科学家希望在短时间内验证机器学习想法，无需搭建复杂训练基础设施。
- **LLM 微调与部署**：开发者需要对 LLaMA、Mistral 等开源大模型进行领域适配和推理部署。
- **多模态 AI 应用**：需要同时处理文本和图像数据的项目，如视觉问答、图像描述生成等。
- **数据中心型 AI 项目**：注重数据质量与特征工程，希望通过结构化方式优化模型性能的场景。

## 4. 技术亮点
- **声明式 YAML 配置**：通过简洁的配置文件定义模型架构，降低使用门槛。
- **Hugging Face 深度集成**：直接调用 Transformers 库中的预训练模型，支持社区海量模型资源。
- **可视化训练监控**：内置 TensorBoard 支持，可直观跟踪训练指标和模型性能。
- **生产就绪导出**：支持将模型导出为 ONNX、TorchScript 等格式，便于在生产环境中部署。
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
- ⭐ 8954 | 🍴 3109 | 语言: C++
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
- ⭐ 6362 | 🍴 769 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个专为中文自然语言处理设计的综合性工具库，由 HuJiFa 创建并维护。它集成了敏感词检测、语言识别、实体抽取（手机号、身份证、邮箱等）以及丰富的词库资源，旨在为开发者提供一站式的中英 NLP 解决方案。

2. **核心功能**
*   **基础 NLP 工具**：支持中英文敏感词过滤、语言检测、繁简体转换及中英文标点规范化。
*   **实体与信息抽取**：提供手机号、身份证号、邮箱、人名、地名的自动抽取与校验功能。
*   **丰富词库资源**：内置中日文人名的常见姓氏库、中文缩写库、停用词表、情感值词典及大量垂直领域词库（如汽车、医疗、法律、IT 等）。
*   **语音与文本生成**：包含英文模拟中文发音、汪峰歌词生成器、自动对联及基于 GPT-2 的文本生成示例。
*   **预训练模型与数据集**：汇总了 BERT、ALBERT、RoBERTa 等主流预训练模型资源，以及多个中文 NLP 竞赛数据集和基准测试集。

3. **适用场景**
*   **内容安全审核**：用于互联网平台的敏感词过滤、违禁词检测及谣言识别。
*   **信息抽取与结构化**：从非结构化文本（如简历、新闻、对话记录）中快速提取关键实体信息。
*   **中文 NLP 研究入门**：适合学生和研究者快速搭建中文分词、词性标注、情感分析等基础 NLP 流水线。
*   **垂直领域知识库构建**：利用其丰富的领域词库（医疗、法律、金融等）辅助构建特定行业的知识图谱或问答系统。

4. **技术亮点**
*   **资源聚合性强**：不仅提供代码工具，还整理了大量高质量的中文 NLP 数据集、预训练模型和学术资源链接，是中文 NLP 领域的“资源黄页”。
*   **开箱即用**：封装了常用的正则表达式和规则引擎，无需复杂配置即可实现敏感词过滤、实体抽取等功能。
*   **社区活跃度高**：作为 GitHub 上星标数极高的中文 NLP 项目，持续更新并整合了最新的模型（如 BERT、GPT-2）和应用案例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82335 | 🍴 15271 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目已在 ACL 2024 上发表，旨在提供简洁易用的微调体验，同时兼顾高性能与低资源消耗。

2. **核心功能**
- 支持 100+ 种 LLM 和 VLM 的统一高效微调。
- 提供多种微调算法，包括 LoRA、QLoRA、全参数微调及 RLHF。
- 内置量化技术，降低显存占用，适配资源受限环境。
- 支持指令微调（Instruction Tuning）和 Agent 构建。
- 兼容主流框架如 Transformers 和 PEFT，集成便捷。

3. **适用场景**
- 快速微调 Llama、Qwen、DeepSeek、Gemma 等主流开源模型。
- 在显存有限的情况下进行大规模模型的高效训练（如使用 QLoRA）。
- 构建多模态应用，对图像-文本模型进行视觉语言微调。
- 需要结合强化学习（RLHF）优化模型对齐与输出质量。

4. **技术亮点**
- 统一接口支持百余种模型，无需为不同模型编写定制代码。
- 结合量化与低秩适应（QLoRA），显著降低硬件门槛。
- 学术背书（ACL 2024），代码质量与稳定性经过同行评审验证。
- 社区活跃，星标数超 7.3 万，生态完善，文档丰富。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73912 | 🍴 9041 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. 中文简介
这是一个为期12周、包含24节课的AI入门课程，旨在让所有人都能轻松学习人工智能。课程由微软开发者倡导团队打造，内容全面覆盖机器学习、深度学习及自然语言处理等核心领域。

### 2. 核心功能
- **系统化课程结构**：提供12周、24课时的完整学习路径，适合初学者循序渐进。
- **多主题覆盖**：涵盖机器学习、深度学习、计算机视觉（CNN）、生成对抗网络（GAN）及自然语言处理（RNN/NLP）。
- **交互式学习体验**：采用Jupyter Notebook格式，支持代码实践与即时反馈。
- **开源免费资源**：完全公开的课程内容，便于全球学习者访问与使用。
- **微软背书质量**：由微软开发者团队维护，确保技术内容的准确性与前沿性。

### 3. 适用场景
- **AI初学者入门**：希望系统学习人工智能基础概念与技术的零基础学习者。
- **高校课程补充**：教师可将此项目作为计算机科学或数据科学课程的辅助教材。
- **企业内训参考**：科技公司用于员工AI技能培训的标准化课程框架。
- **自学实践练习**：个人通过Jupyter Notebook进行代码实操与项目复现。

### 4. 技术亮点
- **全栈AI技术覆盖**：从传统机器学习到前沿深度学习模型（如CNN、GAN、RNN）均有涉及。
- **实践导向设计**：每节课均配有可运行的代码示例，强调“做中学”的教学理念。
- **高社区认可度**：拥有超过6.3万星标，证明其在全球开发者中的广泛影响力与可靠性。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 63305 | 🍴 12266 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- # AI Engineering from Scratch 项目分析

## 1. 中文简介
该项目是一套从零开始学习、构建并部署 AI 系统的完整课程。通过亲手实践，掌握 AI 工程的核心技术，最终能够独立开发并交付 AI 产品。

## 2. 核心功能
- 从零实现 AI 系统，涵盖深度学习、LLM、计算机视觉等核心技术
- 提供完整的课程式学习路径，从基础概念到实际部署全流程覆盖
- 支持多语言实现（Python/Rust/TypeScript），适合不同技术栈的学习者
- 聚焦 AI 工程实践，包括智能体（Agents）、MCP、强化学习等前沿方向
- 强调"学-建-交付"的完整闭环，培养独立开发 AI 产品的能力

## 3. 适用场景
- AI 工程师系统学习从零构建 AI 系统的完整知识体系
- 希望深入理解 AI 底层原理而非仅调用 API 的开发者
- 需要构建生产级 AI 应用并进行部署的工程团队
- 对智能体、MCP、多模态等前沿技术感兴趣的研究者

## 4. 技术亮点
- 46254 星标验证了项目的高质量和社区认可度
- 跨语言支持（Python/Rust/TypeScript）便于不同背景的学习者参与
- 覆盖从基础 ML/DL 到前沿 LLM/Agents 的完整技术栈
- 强调工程实践而非纯理论，注重可交付成果
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46254 | 🍴 8004 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合性学习资源库，内容深入讲解线性代数、PyTorch 及 TensorFlow 2 等核心工具。该项目结合 NLTK 自然语言处理技术，提供从理论基础到代码实现的完整学习路径。

2. **核心功能**
- 集成经典机器学习算法（如 SVM、KMeans、AdaBoost）与深度学习框架（PyTorch、TF2）的实战代码。
- 涵盖推荐系统、自然语言处理（NLP）及回归、分类等主流数据挖掘任务。
- 提供 Apriori、FP-Growth 等关联规则挖掘及 PCA、SVD 等数据降维技术的实现示例。

3. **适用场景**
- 机器学习初学者构建从线性代数基础到深度学习的全栈知识体系。
- 数据分析师快速查阅和复现经典算法（如逻辑回归、朴素贝叶斯）的 Python 实现。
- 研究人员或工程师在推荐系统或 NLP 项目中寻找基于 Scikit-learn 和 PyTorch 的参考代码。

4. **技术亮点**
- 技术栈全面，无缝衔接传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）。
- 内容深度覆盖数学基础（线性代数）与工程实践，适合系统性进阶学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42445 | 🍴 11524 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36036 | 🍴 7411 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33812 | 🍴 4705 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28982 | 🍴 3530 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21823 | 🍴 3340 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17351 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36036 | 🍴 7411 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22708 | 🍴 2137 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16480 | 🍴 3793 | 语言: Python
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
- ⭐ 3470 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3334 | 🍴 411 | 语言: Python
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
- ⭐ 385520 | 🍴 81028 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 268895 | 🍴 24008 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 227187 | 🍴 44454 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199775 | 🍴 60001 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186384 | 🍴 46063 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166872 | 🍴 21538 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164439 | 🍴 30563 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 163028 | 🍴 9177 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157613 | 🍴 46182 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152945 | 🍴 9828 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

