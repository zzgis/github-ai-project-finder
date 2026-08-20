# GitHub AI项目每日发现报告
日期: 2026-08-20

## 新发布的AI项目

### watermarks-remover
- 

# watermarks-remover 项目分析

## 1. 中文简介
该项目用于清除多供应商AI溯源痕迹，通过Unicode文本清洗、统计重写技术以及从PNG/JPEG/SVG/PDF/DOCX/HTML/MD文件中剥离C2PA/元数据，实现AI生成内容的"去水印"处理。

## 2. 核心功能
- **Unicode文本清洗**：移除嵌入在文本中的不可见AI溯源标记
- **统计重写技术**：通过语言模型重写内容以消除AI风格特征
- **C2PA元数据剥离**：从图像和文档中清除内容真实性联盟标准标记
- **多格式支持**：覆盖PNG、JPEG、SVG、PDF、DOCX、HTML、Markdown等常见文件格式
- **多平台兼容**：针对Claude、Codex、Grok等主流AI工具的溯源痕迹进行清除

## 3. 适用场景
- **内容创作者**：需要发布AI辅助生成内容但希望隐藏AI使用痕迹
- **企业合规绕过**：绕过组织内部的AI生成内容检测机制
- **学术研究**：测试水印检测工具的鲁棒性（灰色地带）
- **隐私保护争议**：在"清除个人数据"与"规避溯源"之间的模糊应用

## 4. 技术亮点
- 支持多种主流AI平台的专用溯源协议（C2PA等）
- 结合统计学方法与技术性重写，双重保障去水印效果
- 跨文件格式处理，从图像到文档的全面覆盖

---

⚠️ **重要提示**：此类工具可能用于规避AI内容检测、传播误导性信息或违反平台使用条款，使用时请确保符合当地法律法规及平台政策。
- 链接: https://github.com/Leutenegger/watermarks-remover
- ⭐ 914 | 🍴 94 | 语言: Python
- 标签: claude, claude-code, claude-skills, codex, codex-cli

### llm-rag-memory-ai-agents
- 

## 项目分析：llm-rag-memory-ai-agents

### 1. 中文简介
这是一个结合大语言模型（LLM）、检索增强生成（RAG）和记忆机制的 AI 智能体项目，旨在构建具备长期记忆能力的智能对话系统。项目通过整合知识检索与持久化记忆，使 AI 智能体能够持续学习和记忆用户交互信息。

### 2. 核心功能
- **LLM 驱动对话**：基于大语言模型实现自然语言交互
- **RAG 知识检索**：集成检索增强生成，从外部知识库获取信息
- **长期记忆系统**：支持跨会话的记忆存储与检索
- **智能体架构**：模块化设计，支持灵活扩展和定制
- **上下文管理**：维护多轮对话的连贯性和一致性

### 3. 适用场景
- **智能客服系统**：具备记忆能力的个性化客户服务
- **个人知识助手**：基于用户历史交互的定制化问答
- **企业文档问答**：结合内部知识库的智能信息检索
- **对话式应用**：需要长期记忆的场景，如虚拟伴侣、学习辅导

### 4. 技术亮点
- 将 RAG 检索与 Memory 记忆机制有机结合，提升智能体的知识深度和交互连贯性
- 采用 Python 实现，生态丰富，易于集成主流 LLM 和向量数据库
- 轻量级架构设计，适合快速部署和二次开发
- 链接: https://github.com/turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents
- ⭐ 86 | 🍴 0 | 语言: Python

### dsh-oil-creator
- 

# GitHub 项目分析：dsh-oil-creator

---

## 1. 中文简介

这是一个面向 DeepSeek Harness 的 AI 辅助本地创作者工作台插件。它为内容创作者提供了一套本地化的工作流工具，帮助更高效地完成创作相关任务。

---

## 2. 核心功能

- 提供基于 DeepSeek Harness 的 AI 辅助创作能力
- 作为 DSH 插件运行，实现本地化创作者工作台
- 支持 TypeScript 开发，便于二次定制与扩展
- 与 DeepSeek Harness 生态无缝集成

---

## 3. 适用场景

- **内容创作者**：需要 AI 辅助生成或优化文本内容的个人创作者
- **DeepSeek Harness 用户**：希望在本地环境中扩展 DSH 功能的开发者
- **小型团队**：希望搭建低成本、本地化的 AI 创作工作流

---

## 4. 技术亮点

- 基于 TypeScript 构建，类型安全且易于维护
- 以插件形式嵌入 DeepSeek Harness，轻量且灵活
- 本地化部署，数据隐私可控，无需依赖外部云服务

---

> **注**：以上分析基于项目描述、标签及名称信息推断，如需更详细的功能分析，建议直接查看仓库源码及文档。
- 链接: https://github.com/oil-oil/dsh-oil-creator
- ⭐ 35 | 🍴 10 | 语言: TypeScript
- 标签: creator, deepseek-harness, dsh-plugin

### ai-desktop-pet-2026
- 

## ai-desktop-pet-2026 项目分析

### 1. 中文简介
该项目在Windows桌面上放置一只由AI驱动的动态虚拟宠物。宠物会在窗口上行走，对你的鼠标移动和打字行为做出反应，追逐光标，并在被点击时通过AI进行对话回应。

### 2. 核心功能
- **AI智能对话**：集成LLM（大语言模型），点击宠物时可进行智能对话互动
- **桌面行走动画**：宠物可在多个窗口之间自由行走和移动
- **交互响应**：实时追踪鼠标光标，响应键盘打字行为
- **多宠物选择**：支持猫、狗等多种宠物形象
- **桌面陪伴**：作为动态桌面装饰提供情感陪伴体验

### 3. 适用场景
- **远程办公/居家工作**：为长时间面对屏幕的用户提供桌面陪伴，缓解孤独感
- **学习专注场景**：作为学习时的互动伙伴，增加学习趣味性
- **AI爱好者体验**：快速体验LLM在桌面端的本地化交互应用
- **桌面个性化装饰**：为Windows桌面增添生动有趣的动态元素

### 4. 技术亮点
- **LLM桌面集成**：将大语言模型能力嵌入桌面级应用，实现本地化AI对话
- **实时动画系统**：支持宠物在窗口间行走的流畅动画效果
- **系统级交互**：深度集成Windows桌面环境，响应鼠标/键盘输入
- **轻量级设计**：无需特定编程语言依赖，降低使用门槛
- 链接: https://github.com/prestigioush/ai-desktop-pet-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, ai, animated, cat, chat

### cs2-external-aimbot-2026
- 描述: External aimbot for CS2. Reads game memory externally with no injection. Smooth aim, adjustable FOV, recoil control, and VAC bypass on current patch.
- 链接: https://github.com/darlingpret/cs2-external-aimbot-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, aimbot, bypass, cheat, cs2

### davinci-resolve-studio-crack-2026
- 描述: Activates DaVinci Resolve Studio — the paid version. Unlocks HDR grading tools, noise reduction, Neural Engine AI effects, Collaboration mode, and 4K+ export.
- 链接: https://github.com/surprisedgrou/davinci-resolve-studio-crack-2026
- ⭐ 32 | 🍴 0 | 语言: 未知
- 标签: 2026, 4k, crack, davinci, free

### rust-esp-aimbot-2026
- 描述: External ESP and aimbot for Rust. Player boxes through walls, resource ESP, animal ESP, and smooth aimbot. EAC bypass for current month patch.
- 链接: https://github.com/outrageousach/rust-esp-aimbot-2026
- ⭐ 31 | 🍴 0 | 语言: 未知
- 标签: 2026, aimbot, bypass, cheat, eac

### marvel-rivals-aimbot-2026
- 描述: External aimbot and ESP for Marvel Rivals. Silent aim with head targeting, enemy boxes through walls, ultimate charge display. Updated for Season 2.
- 链接: https://github.com/indolentmil/marvel-rivals-aimbot-2026
- ⭐ 31 | 🍴 0 | 语言: 未知
- 标签: 2026, aimbot, cheat, esp, free

### ai-dog-desktop-pet-2026
- 描述: An animated AI dog companion that lives on your Windows desktop. Fetch animations, tail wagging, barking responses, and a mini-game where you throw a ball.
- 链接: https://github.com/querulouscarb/ai-dog-desktop-pet-2026
- ⭐ 31 | 🍴 0 | 语言: 未知
- 标签: 2026, ai, animated, breed, companion

### topaz-video-ai-crack-2026
- 描述: Activates Topaz Video AI for video upscaling, deinterlacing, motion interpolation (60fps+), and stabilisation. Processes on your GPU without cloud.
- 链接: https://github.com/tartceramics/topaz-video-ai-crack-2026
- ⭐ 31 | 🍴 0 | 语言: 未知
- 标签: 2026, 4k, ai, crack, fps

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP 是一个全面的中英文自然语言处理工具集合，涵盖敏感词检测、语言识别、手机号/身份证抽取、情感分析、词向量等基础NLP能力，同时整合了大量中文词库、知识图谱资源、预训练模型及竞赛数据集。该项目由中文NLP社区维护，汇集了从传统规则方法到深度学习模型的完整NLP工具链。

## 2. 核心功能

- **文本处理基础能力**：中英文敏感词检测、语言检测、繁简转换、停用词、情感值分析、同/反义词库
- **信息抽取**：手机号、身份证、邮箱抽取，命名实体识别（人名、地名、机构名），关键词提取
- **语音与OCR**：中文语音识别（MASR）、中文手写汉字识别（cnocr）、语音对齐工具
- **知识图谱与问答**：多领域知识图谱（医疗、金融、军事）、百科知识抽取、问答系统构建
- **预训练模型资源**：BERT/ALBERT/ELECTREA/GPT2等中文预训练模型，词向量（word2vec、textCNN）
- **数据集与基准**：中文NLP竞赛数据集、阅读理解数据、谣言检测、对话语料、语义相似度评测

## 3. 适用场景

- **内容安全审核**：敏感词过滤、暴恐词检测、谣言识别，适用于社交媒体平台内容审核
- **企业知识库构建**：从百科/新闻/文档中抽取三元组，构建领域知识图谱（医疗、金融、法律）
- **智能客服与对话系统**：提供对话语料、意图识别、多轮对话框架（ConvLab、Rasa）
- **NLP研究与教学**：汇集cs224n课程、清华AI报告、竞赛TOP方案，适合学习与算法复现
- **个人信息处理**：手机号归属地查询、姓名性别推断、身份证校验，适用于用户信息结构化

## 4. 技术亮点

- **资源聚合全面**：涵盖从基础分词（jieba）到前沿模型（BERT、GPT2）的完整工具链
- **中文特色突出**：专门针对中文优化，包括汉字特征提取、拼音标注、中文OCR、中文对话语料
- **竞赛导向**：汇总NLP竞赛TOP方案与代码，对算法工程师有直接参考价值
- **多领域覆盖**：医疗、金融、法律、汽车等垂直领域词库与知识图谱资源齐全
- **开源生态整合**：集成SpaCy、Transformers、Kashgari、Jiagu等主流NLP框架的中文扩展
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82553 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析

### 1. 中文简介
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例，每个项目均配有完整代码，适合不同水平的学习者参考使用。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 项目代码结构清晰，便于学习和二次开发
- 标签分类完善，方便按领域快速检索
- 适合从入门到进阶的学习路径

### 3. 适用场景
- AI初学者系统学习各方向实战项目
- 开发者寻找项目灵感或参考实现
- 面试准备时练习经典AI算法
- 教学培训中作为案例库使用

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广
- 使用Python语言，生态丰富
- 属于Awesome系列项目，质量经过社区筛选
- 高星标数（36393）证明其受欢迎程度和实用性
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36393 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络模型可视化工具，支持多种深度学习框架导出的模型格式。它能够将复杂的模型结构以直观的图形界面呈现，帮助开发者理解和分析模型架构。

### 2. 核心功能
- 支持可视化多种深度学习模型格式（ONNX、TensorFlow、PyTorch、Keras、CoreML 等）
- 提供交互式图形界面，清晰展示网络层结构和参数
- 支持查看模型权重、张量形状和计算图
- 可导出模型结构图为图片或 PDF 格式
- 支持本地文件和云端模型的加载与分析

### 3. 适用场景
- 深度学习模型调试：快速定位模型结构问题
- 模型架构学习：直观理解复杂神经网络结构
- 模型部署前检查：验证不同框架间的模型转换结果
- 技术文档编写：生成清晰的模型结构图用于报告或论文

### 4. 技术亮点
- 纯前端实现，无需安装额外依赖，浏览器即可运行
- 支持 safetensors 等新兴模型格式
- 社区活跃，Star 数超过 3.3 万，是同类工具中人气最高的项目之一
- 提供桌面版和在线版两种使用方式，灵活便捷

---

**总结**：Netron 是深度学习领域必备的模型可视化工具，适合需要分析、调试或展示神经网络模型结构的开发者和研究人员使用。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33369 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21333 | 🍴 4004 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

### 1. 中文简介
这是一本关于机器学习工程的开源参考书籍，全面覆盖从模型训练到推理部署的完整工程链路。项目内容涵盖大规模语言模型（LLM）的训练、调试、扩展性以及GPU集群管理等核心主题，是机器学习工程师的实用指南。

### 2. 核心功能
- **训练工程**：提供PyTorch大规模分布式训练的最佳实践与调优技巧
- **推理优化**：涵盖LLM推理加速、内存优化及服务部署策略
- **GPU集群管理**：基于Slurm的资源调度与多节点训练配置指南
- **调试与可观测性**：机器学习系统的故障排查与性能分析工具
- **存储与网络**：高吞吐量数据加载与集群网络优化方案

### 3. 适用场景
- 大规模语言模型（LLM）的训练与微调工程实践
- MLOps团队搭建模型训练与推理基础设施
- 科研机构或企业构建GPU集群进行分布式训练
- 机器学习工程师系统学习工程化知识体系

### 4. 技术亮点
- 内容覆盖完整ML工程链路，从训练到推理一站式参考
- 聚焦LLM时代的新挑战，如显存优化、分布式训练扩展性
- 结合Slurm等生产级调度工具，贴近真实工业场景
- 开源免费，持续更新，社区活跃（18k+星标）
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18658 | 🍴 1202 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17375 | 🍴 2124 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13270 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11629 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10689 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目为开发者提供了丰富的实战案例和完整代码实现。

### 2. 核心功能
- 提供500个AI相关项目的完整代码示例
- 覆盖机器学习、深度学习、计算机视觉和NLP四大核心领域
- 每个项目均包含可运行的代码实现
- 适合作为学习资源和实战参考

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习
- 开发者寻找计算机视觉或NLP项目的参考实现
- 研究人员快速搭建AI原型和实验
- 企业团队进行AI技术选型和方案评估

### 4. 技术亮点
- 项目数量庞大（500个），覆盖领域全面
- 所有项目均附带完整代码，可直接运行学习
- 标签分类清晰，便于按技术领域快速筛选
- 星标数高达36393，说明社区认可度高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36393 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介

Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它能够直观展示模型结构，帮助用户理解和分析各种AI模型。支持多种主流框架和模型格式，是模型开发者的得力助手。

## 2. 核心功能

- **多框架支持**：兼容 TensorFlow、PyTorch、Keras、ONNX、CoreML、TensorFlow Lite 等主流框架
- **模型结构可视化**：以图形化方式展示神经网络层级结构和连接关系
- **多格式兼容**：支持 .onnx、.tflite、.keras、.pt、.safetensors 等多种模型文件格式
- **跨平台运行**：提供桌面应用和 Web 版本，方便不同场景使用
- **参数详情查看**：支持查看模型各层的权重、偏置等参数信息

## 3. 适用场景

- **模型调试**：帮助开发者快速定位模型结构中的问题
- **论文复现**：直观理解论文中提出的网络架构设计
- **模型转换验证**：验证不同框架间模型转换后的结构一致性
- **教学演示**：用于AI课程的模型结构讲解和演示

## 4. 技术亮点

- 完全开源免费，社区活跃，星标数超过33,000
- 同时提供桌面客户端和在线版本，使用便捷
- 支持 safetensors 等新兴格式，紧跟技术发展趋势
- 界面简洁直观，无需复杂配置即可使用
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33369 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub项目分析：cheatsheets-ai

## 1. 中文简介
本项目为深度学习与机器学习研究者提供一系列必备速查表，涵盖了从基础工具（NumPy、Matplotlib）到深度学习框架（Keras）的常用代码片段和技术要点。项目源自Medium文章，旨在帮助研究者快速查阅和复习关键技术知识。

## 2. 核心功能
- 提供深度学习与机器学习核心概念的速查参考
- 涵盖NumPy、SciPy、Matplotlib等科学计算工具的使用示例
- 包含Keras深度学习框架的常用操作指南
- 整理机器学习算法和深度学习模型的关键参数与用法
- 以简洁的速查表形式呈现，便于快速查阅

## 3. 适用场景
- **研究者复习**：深度学习研究人员快速回顾关键技术和API用法
- **学生入门**：机器学习初学者系统学习常用工具和框架
- **面试准备**：求职面试前快速复习核心技术要点
- **日常开发**：研究人员在实验过程中查阅代码示例

## 4. 技术亮点
- 项目获得15,000+星标，说明其在社区中具有较高认可度和实用价值
- 涵盖从基础科学计算到深度学习框架的完整技术栈
- 速查表形式便于快速检索，提升学习与工作效率
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费配套教材。内容涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域，适合零基础入门及就业实战。

### 2. 核心功能
- 提供系统化的AI学习路线，覆盖从入门到进阶的完整路径
- 收录近200个实战案例和项目，注重动手实践
- 免费提供配套教材和学习资料，降低学习门槛
- 涵盖主流框架和工具，包括PyTorch、TensorFlow、Keras等
- 覆盖多领域方向，包括数据分析、计算机视觉、自然语言处理等

### 3. 适用场景
- 零基础学习者系统学习人工智能相关知识
- 希望转行AI领域的开发者进行就业实战准备
- 需要参考项目案例进行实践练习的在校学生
- 想要了解AI学习路径和资源的自学者

### 4. 技术亮点
- 内容全面，覆盖算法、数据处理、深度学习等完整技术栈
- 实战导向，提供大量可操作的项目案例
- 免费开源，配套教材完善，学习成本低
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13270 | 🍴 2674 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它支持端到端的机器学习流程，涵盖数据预处理、模型训练到部署的全链路。

### 2. 核心功能
- **低代码开发**：通过声明式配置快速构建 AI 模型，无需编写大量代码
- **多模态支持**：兼容计算机视觉、自然语言处理等多种任务类型
- **大模型微调**：支持对 LLaMA、Mistral 等主流 LLM 进行定制化微调训练
- **数据为中心**：内置数据处理管道，简化数据预处理和特征工程
- **PyTorch 驱动**：基于 PyTorch 深度学习框架，提供灵活的模型扩展能力

### 3. 适用场景
- **企业级 AI 应用开发**：快速搭建定制化机器学习流水线
- **大语言模型微调**：针对特定领域对 LLaMA/Mistral 等模型进行适配训练
- **多模态模型构建**：同时处理文本、图像等多种数据类型
- **数据科学项目**：从数据预处理到模型部署的一站式解决方案

### 4. 技术亮点
- 社区活跃度高（11747 星标），生态完善
- 标签覆盖全面，支持从传统 ML 到前沿 LLM 的广泛场景
- 声明式 API 设计降低使用门槛，提升开发效率
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9176 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8966 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6990 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6415 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP是一个全面的中文自然语言处理资源集合项目，涵盖了从基础工具（分词、词性标注、命名实体识别）到高级应用（知识图谱、对话系统、语音识别）的完整NLP生态。项目汇集了数百个开源工具、数据集、预训练模型和实战代码，是中文NLP开发者的宝藏资源库。

## 2. 核心功能

- **文本处理基础工具**：提供敏感词检测、语言检测、手机号/身份证/邮箱抽取、繁简体转换、中文分词等基础NLP功能
- **词库与知识库**：包含中日文人名库、中文缩写库、职业/汽车/成语/地名/历史名人/诗词/医学/饮食/法律等数十个专业领域词库
- **情感分析与语义理解**：提供词汇情感值、停用词、反动词表、否定词库、情感分析模型及工具
- **预训练语言模型**：汇集BERT、GPT、ALBERT、ELECTRA等主流预训练模型及其中文版本
- **知识图谱与问答系统**：包含知识图谱构建工具、命名实体识别、关系抽取、问答系统等相关资源
- **语音与OCR**：提供语音识别数据集、中文OCR工具、音素对齐等语音相关资源
- **数据集与基准测试**：汇集大量中文NLP数据集、竞赛项目及评测基准

## 3. 适用场景

- **NLP初学者学习**：适合想要系统学习中文NLP的学生和开发者，提供从基础到进阶的完整学习路径
- **企业级文本处理开发**：适用于需要敏感词过滤、信息抽取、实体识别等企业级文本处理场景
- **知识图谱构建**：为构建中文知识图谱提供数据、工具和模型参考
- **对话系统与智能客服**：提供对话系统、聊天机器人相关的完整解决方案和资源

## 4. 技术亮点

- **资源全面性**：汇集了数百个中文NLP相关开源项目，涵盖NLP全流程
- **实用性强**：包含大量可直接使用的工具、词库和数据集
- **紧跟前沿**：持续更新，包含BERT、GPT-2等最新预训练模型资源
- **社区活跃**：82553星标数表明其广泛的社区认可度和影响力
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82553 | 🍴 15267 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74239 | 🍴 9078 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# GitHub项目分析：AI-For-Beginners

## 1. 中文简介
这是一套由微软推出的免费AI入门课程，为期12周、共24节课，旨在让任何人都能轻松学习人工智能。课程采用Jupyter Notebook形式，内容全面覆盖机器学习、深度学习及自然语言处理等核心领域。

## 2. 核心功能
- **系统化课程结构**：12周24课的科学编排，循序渐进地引导学习者掌握AI知识。
- **全栈AI技术覆盖**：涵盖机器学习、深度学习、CNN、RNN、GAN、NLP和计算机视觉等核心技术。
- **交互式学习体验**：采用Jupyter Notebook格式，支持代码实践与即时反馈。
- **微软官方背书**：由微软开发者社区出品，内容质量可靠，适合零基础入门。
- **免费开源资源**：完全免费，星标数超6.5万，社区活跃度高。

## 3. 适用场景
- **AI初学者系统学习**：适合完全没有编程或AI背景的用户，从零开始构建知识体系。
- **高校/培训机构课程补充**：可作为学校或培训机构的AI入门教材和实验指导。
- **企业内训与团队建设**：适合技术团队快速普及AI基础知识，统一技术认知。
- **自学者进阶参考**：可作为已有一定基础的开发者系统梳理AI知识框架的参考资料。

## 4. 技术亮点
- **标签体系完整**：涵盖AI全领域关键词（ML/DL/CNN/RNN/GAN/NLP/CV），体现课程全面性。
- **高社区认可度**：65714颗星表明该项目在全球开发者中享有极高声誉。
- **微软品牌加持**：作为Microsoft For Beginners系列的一部分，享有官方资源支持和持续维护。
- **实践导向设计**：Jupyter Notebook格式确保每个知识点都有可运行的代码示例。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65714 | 🍴 12734 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub 项目分析：ai-engineering-from-scratch

---

### 1. 中文简介

这是一个从零开始学习、构建并部署AI工程项目的实战教程。内容涵盖从基础理论到实际部署的完整链路，帮助学习者真正掌握AI系统的构建能力。

---

### 2. 核心功能

- 提供从基础到高级的AI工程完整学习路径
- 涵盖大语言模型（LLM）、生成式AI、智能体（Agents）等前沿领域
- 支持多种编程语言（Python、Rust、TypeScript）的实现教程
- 包含计算机视觉、自然语言处理、强化学习等多方向实战项目
- 提供蜂群智能、MCP协议等进阶主题内容

---

### 3. 适用场景

- 希望系统学习AI工程从零到部署的开发者
- 需要构建AI智能体（AI Agents）和LLM应用的工程师
- 对生成式AI、计算机视觉等方向有实战需求的学习者
- 希望通过多语言对比深入理解AI底层原理的进阶人员

---

### 4. 技术亮点

- 采用"Learn it → Build it → Ship it"三步实战方法论，强调动手能力
- 跨语言覆盖（Python + Rust + TypeScript），适合不同技术背景的学习者
- 内容全面，从传统机器学习到前沿智能体工程均有涉及，适合体系化学习
- 47221个星标表明社区认可度高，是热门AI学习资源之一
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47221 | 🍴 8295 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42465 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36393 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33832 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29125 | 🍴 3546 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21842 | 🍴 3357 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17375 | 🍴 2124 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36393 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于 AI 的浏览器工作流自动化工具，能够智能地模拟人类操作浏览器完成各种重复性任务。它结合了大型语言模型（LLM）和计算机视觉技术，让浏览器自动化更加智能和灵活。

### 2. 核心功能
- 利用 AI 和 LLM 智能理解网页内容并执行操作
- 支持多种浏览器自动化工具（Playwright、Puppeteer、Selenium）
- 提供 API 接口，便于集成到现有系统中
- 具备计算机视觉能力，可识别页面元素并完成复杂交互
- 支持自定义工作流，实现端到端的自动化流程

### 3. 适用场景
- **数据抓取与录入**：自动登录网站、填写表单、批量提取数据
- **RPA 流程自动化**：替代人工完成重复性的网页操作任务
- **跨平台工作流整合**：将多个网页服务串联成自动化流程
- **Power Automate 替代方案**：为需要 AI 智能决策的场景提供更灵活的自动化方案

### 4. 技术亮点
- 将 LLM 的语义理解能力与浏览器自动化相结合，突破了传统 RPA 的局限性
- 采用计算机视觉辅助定位页面元素，提高了自动化的鲁棒性
- 开源且支持多种浏览器引擎，灵活适配不同需求
- 社区活跃，星标数超过 2.2 万，表明受到广泛关注
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22793 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一个领先的平台，用于构建高质量的视觉数据集以支持视觉AI。它提供开源、云和企业级产品，以及标注服务，支持图像、视频和3D标注，具备AI辅助标注、质量保证、团队协作、数据分析和开发者API等功能。

### 2. 核心功能
- **AI辅助标注**：利用人工智能自动标注，大幅提升标注效率
- **多模态支持**：支持图像、视频和3D数据的标注任务
- **团队协作**：多人协同完成标注，支持任务分配与管理
- **质量保证**：内置质检功能，确保标注数据的准确性
- **开发者API**：提供API接口，便于集成到现有工作流程

### 3. 适用场景
- 计算机视觉数据集的标注与构建
- 图像分类与物体检测任务的数据准备
- 视频分析与语义分割的标注工作
- 深度学习项目的数据标注流程

### 4. 技术亮点
- 开源项目，社区活跃（星标数超16000）
- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供从开源到企业级的完整产品矩阵
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16551 | 🍴 3805 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，为深度学习模型提供可视化解释能力。支持CNN、Vision Transformer等多种架构，涵盖分类、目标检测、分割、图像相似度等多种任务。

### 2. 核心功能
- 提供Grad-CAM、Score-CAM等多种类激活图生成算法
- 支持卷积神经网络（CNN）和视觉Transformer（ViT）模型
- 兼容图像分类、目标检测、语义分割等多种视觉任务
- 支持图像相似度计算的可解释性分析
- 提供直观的可视化输出，帮助理解模型决策依据

### 3. 适用场景
- **模型调试**：定位CNN或ViT模型关注图像的区域，排查误判原因
- **医疗影像分析**：可视化模型诊断依据，增强临床可信度
- **自动驾驶感知**：解释目标检测模型对道路物体的识别逻辑
- **学术研究与教学**：演示深度学习模型内部决策机制

### 4. 技术亮点
- 统一接口支持多种XAI算法（Grad-CAM、Score-CAM等），便于对比实验
- 原生适配PyTorch生态，与主流视觉模型无缝集成
- 项目星标数超1.2万，社区活跃，文档完善，是PyTorch生态中最受欢迎的可解释性工具之一
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，专为深度学习研究而设计。它提供了丰富的可微分计算机视觉算子和图像处理功能，完全基于 PyTorch 构建，能够无缝集成到现有的深度学习工作流中。

### 2. 核心功能
- 提供超过 150 个可微分的几何计算机视觉算子，支持自动微分
- 包含完整的图像处理流水线，如色彩空间转换、几何变换、滤波等
- 支持相机标定、立体视觉、多视图几何等传统 CV 任务
- 与 PyTorch 原生张量无缝集成，可直接在 GPU 上运行
- 提供模块化设计，便于研究人员快速构建和实验自定义模型

### 3. 适用场景
- **机器人视觉导航**：用于空间感知和三维重建的几何计算
- **图像配准与拼接**：多视角图像的对齐和融合处理
- **深度学习研究**：将传统 CV 算法嵌入神经网络进行端到端训练
- **自动驾驶感知**：实时处理摄像头数据以进行环境理解

### 4. 技术亮点
- **全可微分设计**：所有算子支持梯度传播，可直接用于反向传播优化
- **硬件加速**：充分利用 GPU 并行计算能力，处理速度远超传统 OpenCV
- **JIT 编译支持**：通过 TorchScript 实现模型部署优化
- **开源活跃**：拥有 11000+ 星标，社区贡献活跃，持续更新维护
- 链接: https://github.com/kornia/kornia
- ⭐ 11317 | 🍴 1225 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3481 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3384 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2508 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

# OpenClaw 项目分析

## 1. 中文简介
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，让你以"龙虾方式"完全掌控自己的数据。它强调数据自主权，将 AI 能力部署在你自己的环境中运行。

## 2. 核心功能
- 跨平台支持，兼容任意操作系统
- 个人 AI 助手，可自定义和私有化部署
- 数据完全自主掌控，无需依赖第三方云服务
- 基于 TypeScript 构建，具备良好的可扩展性

## 3. 适用场景
- 注重隐私的用户希望本地运行 AI 助手
- 开发者希望搭建可定制的个人 AI 助手
- 企业或个人希望私有化部署 AI 能力以保护数据主权

## 4. 技术亮点
- 采用 TypeScript 开发，类型安全且生态丰富
- 强调"own-your-data"理念，实现数据本地化处理
- 高人气项目（38万+星标），社区活跃度高
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386808 | 🍴 81261 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

## 1. 中文简介
Superpowers 是一个实用的智能体技能框架与软件开发方法论，旨在通过子代理驱动开发的方式提升软件开发效率。它将 AI 智能体技能整合到软件开发生命周期（SDLC）中，提供了一套可落地的开发流程。

## 2. 核心功能
- **子代理驱动开发**：通过多个 AI 子代理协作完成软件开发任务
- **智能体技能框架**：提供可复用的 AI 技能模块，支持头脑风暴与编码全流程
- **SDLC 集成**：将 AI 智能体能力嵌入标准软件开发生命周期
- **OBRA 方法论**：结合目标与关键结果框架，指导项目方向与执行
- **Shell 脚本驱动**：基于 Shell 实现，轻量且易于集成到现有工作流

## 3. 适用场景
- AI 辅助的软件开发项目，需要自动化代码生成与审查
- 团队协作中的头脑风暴与需求分析阶段
- 希望将 AI 智能体集成到 CI/CD 流程中的 DevOps 团队
- 探索子代理驱动开发模式的研究与实践场景

## 4. 技术亮点
- 以 Shell 脚本为核心，无需复杂依赖即可快速部署
- 将 AI 智能体技能与经典软件开发方法论（OBRA/SDLC）深度融合
- 高社区认可度（27万+星标），验证了该框架的实用价值
- 链接: https://github.com/obra/superpowers
- ⭐ 274374 | 🍴 24561 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

---

### 1. 中文简介
hermes-agent 是一款能够与用户共同成长的AI智能体工具，支持多种大语言模型后端（如Claude、ChatGPT等）。它旨在成为一个可进化的编程助手，随着使用不断学习和适应用户需求。

---

### 2. 核心功能
- **多模型支持**：兼容Claude、ChatGPT、Codex等多种主流LLM后端
- **自主任务执行**：智能体可独立分析和执行复杂编程任务
- **持续学习与进化**：根据用户交互不断积累知识和优化能力
- **代码辅助开发**：提供代码生成、审查、调试等完整开发辅助功能
- **Nous Research生态集成**：基于Nous Research的研究成果构建

---

### 3. 适用场景
- 日常编程开发中的智能代码助手
- 需要跨模型切换的灵活AI编程工作流
- 希望AI工具能随项目积累经验的长期开发场景
- 对多模型能力进行比较和切换的研究/测试场景

---

### 4. 技术亮点
- 高社区认可度（超23万星标），反映其广泛的影响力
- 支持多模型统一的智能体接口，降低切换成本
- 由Nous Research团队研发，具备扎实的研究背景
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233113 | 🍴 46641 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码许可的工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，提供 400 多种集成，可自托管或云端部署。

### 2. 核心功能
- 可视化工作流编排，拖拽式构建自动化流程
- 内置 AI 能力，支持智能决策与数据处理
- 400+ 预置集成，覆盖主流 API 和服务
- 支持自托管与云端部署，灵活适配不同需求
- 融合低代码与自定义代码，满足从简单到复杂的场景

### 3. 适用场景
- 企业级 API 集成与数据同步自动化
- 基于 AI 的智能工作流（如自动分类、摘要生成）
- 跨平台业务系统的数据流转与任务调度
- 开发者快速搭建自定义自动化流程

### 4. 技术亮点
- 支持 MCP（Model Context Protocol）客户端与服务端，便于 AI 工具集成
- 开源公平代码许可，兼顾开放性与商业化保护
- TypeScript 开发，类型安全且易于扩展
- 支持 CLI 工具，便于集成到 DevOps 流程
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201225 | 🍴 60237 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 承载着让每个人都能便捷使用 AI 并进行构建的愿景。我们的使命是提供所需工具，让你能够专注于真正重要的事物。

### 2. 核心功能
- 支持多种大语言模型（GPT、Claude、Llama 等）的灵活接入
- 具备自主代理能力，可自动规划并执行复杂任务
- 提供可扩展的插件系统，便于用户自定义功能模块
- 支持多步骤任务分解与自动化执行

### 3. 适用场景
- 自动化完成重复性办公任务（如数据整理、报告生成）
- 构建自定义 AI 助手，辅助日常决策与信息检索
- 快速原型开发，验证 AI 代理的创意想法
- 教育场景，帮助初学者理解 AI 代理的工作原理

### 4. 技术亮点
- 高度模块化架构，兼容 OpenAI、Anthropic、OpenRouter 等多平台 API
- 社区活跃，星标数近 19 万，生态丰富
- 支持本地部署，兼顾隐私与灵活性
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186691 | 🍴 46049 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 169703 | 🍴 9464 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167599 | 🍴 21639 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164587 | 🍴 30551 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157894 | 🍴 46173 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153487 | 🍴 9897 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

