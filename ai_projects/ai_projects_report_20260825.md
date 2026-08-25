# GitHub AI项目每日发现报告
日期: 2026-08-25

## 新发布的AI项目

### learn
- 描述: My AI learning system.
- 链接: https://github.com/amosblomqvist/learn
- ⭐ 251 | 🍴 31 | 语言: TypeScript

### wenai
- 

## 项目分析：wenai

### 1. 中文简介
这是一个面向 OpenClaw 的 AI 伴侣技能，让用户可以与 AI 女友建立亲密互动关系。项目结合了 Pony V6 XL 驱动的视觉工作流，提供沉浸式的恋爱体验。

### 2. 核心功能
- 提供 AI 女友伴侣互动体验
- 集成 Pony V6 XL 视觉生成工作流
- 支持 OpenClaw 平台扩展技能
- 打造沉浸式恋爱角色扮演场景

### 3. 适用场景
- 情感陪伴与虚拟恋爱体验
- OpenClaw 平台的个性化技能扩展
- AI 角色扮演与互动叙事
- 视觉内容生成与伴侣形象定制

### 4. 技术亮点
- 采用 Pony V6 XL 模型驱动视觉工作流，支持高质量图像生成
- 作为 OpenClaw 技能插件，便于集成与扩展
- 无需编写代码即可使用（无编程语言依赖）

---

**备注**：该项目星标数较少（94），属于新兴或小众项目，使用时建议关注其更新维护状态。
- 链接: https://github.com/Straniero44/wenai
- ⭐ 94 | 🍴 27 | 语言: 未知

### swissdevjobs-cli
- 

## swissdevjobs-cli 项目分析

### 1. 中文简介

该项目是一个零依赖的 Python CLI 工具，支持从终端或 AI 代理搜索并申请覆盖 7 个国家（瑞士、德国、英国、美国、加拿大、荷兰、法国）的约 4,700 个薪资透明的技术岗位。同时提供 MCP 服务器和 Claude Code 插件，可直接与 AI 编程助手集成使用。

### 2. 核心功能

- **多国家职位搜索**：覆盖瑞士、德国、英国、美国、加拿大、荷兰、法国 7 个国家的 ~4,700 个技术岗位
- **薪资透明筛选**：所有职位均标注薪资范围，方便求职者快速筛选
- **AI 代理集成**：支持通过 MCP 协议与 Claude Code 等 AI 工具无缝对接
- **零依赖部署**：纯 Python 实现，无需额外依赖包即可运行
- **终端一键申请**：直接从命令行完成职位搜索与申请流程

### 3. 适用场景

- 技术开发者希望通过终端快速浏览和申请欧洲及北美地区的远程/本地技术岗位
- AI 助手用户想在 Claude Code 中直接搜索职位并生成求职材料
- 追求薪资透明度的求职者，希望快速过滤不符合薪资预期的岗位
- 需要跨多国职位搜索的远程工作者或数字游民

### 4. 技术亮点

- **MCP 协议支持**：符合 Model Context Protocol 标准，可与多种 AI 工具链集成
- **Claude Code 插件**：原生支持 Anthropic 的 Claude Code 编程助手
- **零依赖设计**：最小化依赖，部署简单，兼容性强
- **多语言标签覆盖**：标签涵盖 AI Agents、Job Search、MCP Server 等多个热门领域
- 链接: https://github.com/Stupidoodle/swissdevjobs-cli
- ⭐ 62 | 🍴 8 | 语言: Python
- 标签: ai-agents, claude, claude-code, cli, developer-jobs

### technocore
- 描述: Decentralized Ed25519 Cryptographic Identity, Signed Message Bus, and Proof-of-Contribution Framework for AI Agents on Technocore ( Ecosystem)
- 链接: https://github.com/d4ncboz/technocore
- ⭐ 40 | 🍴 0 | 语言: Python

### deepseek-v4-flash-vision-video-rag
- 

## GitHub 项目分析：deepseek-v4-flash-vision-video-rag

---

### 1. 中文简介

该项目是一个基于 DeepSeek V4-Flash Vision 视觉大模型的视频理解与问答 Agent 技能。它能让 AI 真正"看懂"视频内容，用户提问后可精准定位答案所在时间位置，并自动生成包含可播放片段和关键帧的自包含 HTML 预览页，方便用户核对验证。

---

### 2. 核心功能

- **视频抽帧索引**：按时间轴对视频进行抽帧阅读，一次性建立视频内容索引。
- **三级问答流程**：采用"本地粗筛 → 视觉精排 → 深度阅读回答"的三步处理机制。
- **精准时间戳引用**：回答附带 [MM:SS] 格式的时间戳，精确指向答案所在片段。
- **自包含 HTML 预览**：自动生成内嵌可播放视频片段、关键帧和答案的独立 HTML 文件，双击浏览器即可查看。
- **可播放片段截取**：根据答案定位，自动裁剪出对应的视频片段供用户核对。

---

### 3. 适用场景

- **视频内容检索**：快速从长视频中定位特定信息或答案所在的时间段。
- **视频学习辅助**：学生或研究者对教学/会议视频进行提问，精准获取所需内容片段。
- **视频素材审核**：编辑或审核人员快速定位视频中的关键帧和片段进行核对。
- **智能视频助手**：为视频平台或知识库提供 AI 驱动的视频问答能力。

---

### 4. 技术亮点

- 基于 DeepSeek 最新视觉大模型（deepseek-v4-flash-vision-exp），具备强大的视频理解能力。
- 采用"粗筛→精排→深读"的分层处理策略，兼顾效率与准确性。
- 生成的 HTML 为自包含文件，无需额外依赖，双击即可在浏览器中预览播放。
- 链接: https://github.com/liangdabiao/deepseek-v4-flash-vision-video-rag
- ⭐ 32 | 🍴 2 | 语言: Python
- 标签: skill, skills

### demo-linkedin-agent
- 描述: Fetch.ai LinkedIn poster agent for Agentverse using uAgents and ASI:One
- 链接: https://github.com/ShyamRV/demo-linkedin-agent
- ⭐ 30 | 🍴 1 | 语言: Python

### youtubepro
- 描述: Local-first YouTube research, grounded AI insights, script writing, and thumbnail creation.
- 链接: https://github.com/AgriciDaniel/youtubepro
- ⭐ 22 | 🍴 8 | 语言: TypeScript

### hengzhi
- 描述: 看见每一笔决策。本机 AI 交易复盘台，只做币安 USDT-M。
- 链接: https://github.com/7836246/hengzhi
- ⭐ 22 | 🍴 14 | 语言: Python

### delta-force-aimbot
- 描述: Delta Force Aimbot - undetected cheat with anti-cheat bypass
- 链接: https://github.com/oddballcanv/delta-force-aimbot
- ⭐ 19 | 🍴 0 | 语言: 未知
- 标签: 2025, aimbot, bypass, cheat, crack

### fortnite-soft-aim
- 描述: Fortnite Soft Aim - undetected Fortnite cheat with anti-cheat bypass
- 链接: https://github.com/pointlessseq/fortnite-soft-aim
- ⭐ 19 | 🍴 0 | 语言: 未知
- 标签: 2025, aim, bypass, cheat, crack

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、语言分析、实体抽取、知识图谱、语音识别、文本生成等多个NLP领域的工具和数据集。该项目汇总了丰富的预训练模型、语料库、标注工具及开源代码，为中文NLP研究和应用提供了一站式资源平台。

### 2. 核心功能
- 提供敏感词检测、语言检测、手机号/电话归属地查询、身份证/邮箱抽取等基础NLP工具
- 汇集命名实体识别、关键词抽取、文本摘要、文本分类等多种NLP任务工具
- 整合BERT、ALBERT、RoBERTa、ELECTREA等中文预训练语言模型及词向量资源
- 包含知识图谱构建、问答系统、对话机器人等高级NLP应用资源
- 提供语音识别、OCR文字识别、文本可视化等跨模态NLP工具

### 3. 适用场景
- NLP研究人员和开发者快速查找中文NLP相关资源与开源项目
- 企业构建智能客服、问答系统、舆情监控等应用
- 学术研究者利用公开数据集和预训练模型开展NLP算法研究
- 初学者通过完整资源列表学习中文NLP技术与实践

### 4. 技术亮点
- 收录清华XLORE、百度基准信息抽取系统等知名中文NLP项目
- 整合CLUENER、BERT-NER等细粒度命名实体识别模型
- 提供从基础工具到高级应用的完整中文NLP技术栈
- 包含大量高质量中文语料库、数据集和预训练模型资源
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82665 | 🍴 15275 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的代码合集。项目涵盖了从入门到进阶的多个方向，适合不同层次的学习者和开发者参考使用。

### 2. 核心功能
- 汇集500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP等多个领域
- 提供可直接运行的项目代码，便于学习和实践
- 按主题分类整理，方便快速定位感兴趣的方向

### 3. 适用场景
- AI/机器学习初学者系统学习与实践
- 开发者寻找项目灵感或参考实现
- 研究人员快速复现经典算法与模型
- 技术团队进行技术选型与方案评估

### 4. 技术亮点
- 项目数量丰富（500个），覆盖面广
- 全部附带可运行的代码，实用性强
- 标签分类清晰，便于按领域筛选
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36538 | 🍴 7468 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够以直观的图形界面展示模型结构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 safetensors
- 提供清晰的神经网络结构图，直观展示层与层之间的连接关系
- 支持查看模型中的权重数据和数值信息
- 兼容桌面应用和 Web 浏览器，使用便捷

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：直观理解复杂神经网络的设计原理
- 模型格式转换验证：检查不同框架间模型转换的正确性
- AI 教学演示：用于课堂或培训中展示模型内部结构

### 4. 技术亮点
- 支持 safetensors 等新兴安全模型格式
- 跨平台兼容，无需额外依赖即可运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33400 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开源的机器学习模型互操作性标准，旨在实现不同深度学习框架之间的模型互转与共享。它由Facebook和Microsoft等公司联合发起，为AI开发者提供了一个统一的模型交换格式。

### 2. 核心功能
- 支持将模型从PyTorch、TensorFlow、Keras等主流框架导出为ONNX格式
- 提供跨框架的模型推理引擎，可在多种硬件平台上运行
- 支持模型转换与格式互转，实现不同深度学习框架间的无缝迁移
- 提供完善的算子库，覆盖主流神经网络层和运算操作
- 支持模型优化与压缩，提升推理性能和减少模型体积

### 3. 适用场景
- 将训练好的模型从PyTorch/TensorFlow导出，部署到移动端或嵌入式设备
- 在不同深度学习框架之间迁移模型，避免框架锁定
- 在生产环境中使用ONNX Runtime进行高效推理部署
- 跨平台AI应用开发，实现一次训练、多处部署

### 4. 技术亮点
- **生态兼容性强**：支持PyTorch、TensorFlow、scikit-learn等十余种主流框架
- **高性能推理**：ONNX Runtime提供多硬件加速后端（CPU、GPU、TensorRT等）
- **社区活跃**：GitHub星标超过2万，拥有活跃的开发者社区和持续迭代
- **标准化程度高**：作为行业标准被广泛采用，得到各大科技公司的支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21357 | 🍴 4012 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# ml-engineering 项目分析

## 1. 中文简介
这是一本关于机器学习工程的开源参考书籍，系统性地介绍了大规模机器学习系统的设计与实践。内容涵盖从模型训练、推理优化到部署运维的完整工程链路。

## 2. 核心功能
- 提供大规模模型训练的最佳实践与故障排查指南
- 详细介绍GPU集群配置、网络优化与存储方案
- 覆盖LLM推理优化、可扩展性设计及Slurm调度管理
- 包含PyTorch和Transformers框架的工程化使用技巧
- 提供MLOps全流程的实战经验总结

## 3. 适用场景
- 大规模语言模型（LLM）的训练与微调工程实践
- GPU集群的资源调度与性能调优
- 机器学习系统的部署与推理优化
- MLOps平台搭建与运维管理

## 4. 技术亮点
- 内容覆盖训练到部署的完整ML工程链路，实用性强
- 针对LLM时代的大规模分布式训练有深入讲解
- 结合Slurm等调度工具，提供工业级集群管理经验
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18706 | 🍴 1206 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17385 | 🍴 2125 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13283 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11633 | 🍴 917 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10693 | 🍴 5696 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的代码合集。项目涵盖了从入门到进阶的多个方向，适合不同层次的学习者和开发者参考使用。

### 2. 核心功能
- 汇集500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP等多个领域
- 提供可直接运行的项目代码，便于学习和实践
- 按主题分类整理，方便快速定位感兴趣的方向

### 3. 适用场景
- AI/机器学习初学者系统学习与实践
- 开发者寻找项目灵感或参考实现
- 研究人员快速复现经典算法与模型
- 技术团队进行技术选型与方案评估

### 4. 技术亮点
- 项目数量丰富（500个），覆盖面广
- 全部附带可运行的代码，实用性强
- 标签分类清晰，便于按领域筛选
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36538 | 🍴 7468 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够以直观的图形界面展示模型结构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 safetensors
- 提供清晰的神经网络结构图，直观展示层与层之间的连接关系
- 支持查看模型中的权重数据和数值信息
- 兼容桌面应用和 Web 浏览器，使用便捷

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：直观理解复杂神经网络的设计原理
- 模型格式转换验证：检查不同框架间模型转换的正确性
- AI 教学演示：用于课堂或培训中展示模型内部结构

### 4. 技术亮点
- 支持 safetensors 等新兴安全模型格式
- 跨平台兼容，无需额外依赖即可运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33400 | 🍴 3178 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## 项目分析：cheatsheets-ai

### 1. 中文简介
该项目为深度学习与机器学习研究者提供了必备的速查表集合，内容涵盖主流框架和工具库的核心用法。作者通过Medium文章分享，旨在帮助研究人员快速查阅关键知识点。

### 2. 核心功能
- 提供深度学习与机器学习领域的核心概念速查表
- 覆盖Keras、NumPy、SciPy、Matplotlib等常用库的使用技巧
- 以简洁的图表形式呈现关键语法和API参考
- 面向研究者设计，便于快速查阅和复习

### 3. 适用场景
- 深度学习研究者在实验过程中快速查阅API用法
- 机器学习初学者系统复习核心知识点
- 数据科学家在项目中参考NumPy/SciPy等工具的最佳实践
- 面试准备或知识梳理时的速查参考资料

### 4. 技术亮点
- 内容高度浓缩，以可视化方式呈现复杂概念
- 覆盖主流AI/ML工具链，实用性强
- 项目获得较高关注度（15427星标），说明社区认可度较高
- 无代码实现，专注于知识整理与分享
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图项目，整理了近200个实战案例与项目，并提供免费的配套教材，帮助零基础学习者入门并实现就业实战。内容涵盖Python编程、数学基础、机器学习、数据分析、深度学习、计算机视觉、自然语言处理等热门领域。

### 2. 核心功能
- 提供系统化的人工智能学习路线图，从零基础到就业实战
- 收录近200个实战案例与项目，配套免费教材
- 覆盖Python、数学、机器学习、深度学习、NLP、CV等核心领域
- 支持多种主流深度学习框架（PyTorch、TensorFlow、Keras等）
- 整合数据分析与数据挖掘相关工具库（NumPy、Pandas、Matplotlib等）

### 3. 适用场景
- 人工智能/机器学习初学者系统入门学习
- 希望转行AI领域的开发者实战能力提升
- 数据科学相关岗位求职前的项目经验积累
- 高校学生或自学者参考学习路线规划

### 4. 技术亮点
- 项目星标数达13,283，社区认可度高
- 免费开源，配套教材完整，学习成本极低
- 覆盖主流框架与工具链，实战案例丰富多样
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13283 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型、神经网络及其他 AI 模型。它采用数据驱动的设计理念，让开发者无需编写大量代码即可快速训练和部署深度学习模型。

### 2. 核心功能
- **低代码建模**：通过声明式配置快速构建神经网络和 LLM，无需手写复杂代码
- **多模态支持**：支持自然语言处理、计算机视觉等多种数据类型
- **模型微调**：内置对 LLaMA、LLaMA2、Mistral 等主流大模型的微调能力
- **PyTorch 驱动**：基于 PyTorch 构建，兼容主流深度学习生态
- **数据中心训练**：强调数据质量与结构化管理，提升模型训练效率

### 3. 适用场景
- **快速原型开发**：需要快速验证想法、构建 AI 模型原型的团队
- **大模型微调**：对 LLaMA、Mistral 等开源模型进行领域适配和微调
- **多模态应用**：同时处理文本、图像等多种输入类型的 AI 项目
- **数据驱动研究**：以数据为核心、注重实验迭代的机器学习研究场景

### 4. 技术亮点
- 社区活跃，星标数超过 11,000，说明具有较高的认可度和使用率
- 将深度学习与低代码理念结合，降低了 AI 模型开发门槛
- 完整覆盖从数据处理到模型部署的全流程，适合数据科学家和工程师协作使用
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9188 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8966 | 🍴 3108 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8370 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6989 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6440 | 🍴 780 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、语言分析、实体抽取、知识图谱、语音识别、文本生成等多个NLP领域的工具和数据集。该项目汇总了丰富的预训练模型、语料库、标注工具及开源代码，为中文NLP研究和应用提供了一站式资源平台。

### 2. 核心功能
- 提供敏感词检测、语言检测、手机号/电话归属地查询、身份证/邮箱抽取等基础NLP工具
- 汇集命名实体识别、关键词抽取、文本摘要、文本分类等多种NLP任务工具
- 整合BERT、ALBERT、RoBERTa、ELECTREA等中文预训练语言模型及词向量资源
- 包含知识图谱构建、问答系统、对话机器人等高级NLP应用资源
- 提供语音识别、OCR文字识别、文本可视化等跨模态NLP工具

### 3. 适用场景
- NLP研究人员和开发者快速查找中文NLP相关资源与开源项目
- 企业构建智能客服、问答系统、舆情监控等应用
- 学术研究者利用公开数据集和预训练模型开展NLP算法研究
- 初学者通过完整资源列表学习中文NLP技术与实践

### 4. 技术亮点
- 收录清华XLORE、百度基准信息抽取系统等知名中文NLP项目
- 整合CLUENER、BERT-NER等细粒度命名实体识别模型
- 提供从基础工具到高级应用的完整中文NLP技术栈
- 包含大量高质量中文语料库、数据集和预训练模型资源
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82665 | 🍴 15275 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一高效的大语言模型与视觉语言模型微调框架，支持 100 多种主流模型，相关研究成果已发表于 ACL 2024 会议。该项目旨在为研究人员和开发者提供一站式、低门槛的模型微调解决方案。

### 2. 核心功能
- 支持 100+ 主流大语言模型和视觉语言模型的统一微调
- 提供多种参数高效微调方法，包括 LoRA、QLoRA 和全参数微调
- 内置 RLHF（强化学习人类反馈）训练流程，支持 DPO、KTO 等对齐方法
- 支持多种量化技术（如 INT4/INT8 量化），便于资源受限环境部署
- 集成 Agent 构建能力，支持多模型协作的智能体开发

### 3. 适用场景
- 研究人员对 LLaMA、Qwen、DeepSeek、Gemma 等模型进行指令微调实验
- 开发者在显存受限条件下使用 QLoRA 微调大模型
- 企业团队基于 RLHF/DPO 对模型进行人类偏好对齐训练
- 需要快速搭建和部署多模态大模型应用的场景

### 4. 技术亮点
- **统一架构**：一套代码支持上百种模型的微调，无需切换框架
- **QLoRA 优化**：在极低显存（单卡 8GB+）下即可微调 70B 级别模型
- **多模态支持**：同时支持纯文本模型和视觉语言模型（VLM）的微调
- **生产就绪**：提供 Web UI 界面和命令行工具，兼顾易用性与灵活性
- **学术认可**：研究成果发表于 ACL 2024，具备学术严谨性
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74353 | 🍴 9095 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门面向初学者的AI通识课程，为期12周，包含24节精心设计的课程，旨在让所有人都能轻松入门人工智能领域。该项目由微软推出，以Jupyter Notebook形式呈现，内容覆盖全面且循序渐进。

### 2. 核心功能
- **系统化课程结构**：12周24课时的完整学习路径，从零开始构建AI知识体系
- **多模态内容覆盖**：涵盖机器学习、深度学习、计算机视觉、NLP、GAN等核心领域
- **实践导向教学**：全部课程以Jupyter Notebook形式提供，边学边练
- **微软官方背书**：由微软教育团队开发，质量有保障

### 3. 适用场景
- 零基础初学者系统学习人工智能基础知识
- 高校或培训机构作为AI入门课程的补充教材
- 职场人士利用业余时间自学AI技能
- 教师备课参考，用于设计AI通识课程

### 4. 技术亮点
- 涵盖CNN、RNN、GAN等主流深度学习架构的入门讲解
- 使用Jupyter Notebook实现交互式学习体验
- 项目星标数超过6.6万，社区认可度高
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66950 | 🍴 12929 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub 项目分析：ai-engineering-from-scratch

---

### 1. 中文简介
该项目是一套从零开始构建 AI 系统的完整教程课程，涵盖学习、实现到部署的全流程。内容以"学透原理 → 亲手构建 → 为他人交付"为主线，帮助开发者深入掌握 AI 工程的核心能力。

---

### 2. 核心功能
- 从零实现 AI 核心组件，涵盖 LLM、计算机视觉、强化学习等模块
- 提供完整的课程式学习路径，包含代码示例与逐步教程
- 支持多语言实现（Python / Rust / TypeScript），便于不同技术栈的开发者参与
- 涵盖 AI Agent、MCP 协议、Swarm Intelligence 等前沿工程实践

---

### 3. 适用场景
- 希望深入理解 AI 底层原理、不满足于仅调用 API 的开发者
- 需要系统学习 AI 工程化（从训练到部署）的工程师或学生
- 希望用多种语言（Python/Rust/TS）实现 AI 组件的技术探索者
- 构建 AI Agent 或大模型应用时，需要参考从零实现方案的研究人员

---

### 4. 技术亮点
- **从零实现**：不依赖高级封装库，从底层推导并实现关键算法，适合深度学习者
- **多语言覆盖**：同时提供 Python、Rust、TypeScript 实现，兼顾易用性与高性能场景
- **前沿主题覆盖**：包含 MCP（Model Context Protocol）、Swarm Intelligence 等新兴方向
- **课程化结构**：以 Course + Tutorial 形式组织内容，学习路径清晰，适合系统性自学
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 48874 | 🍴 8557 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：AiLearning

### 1. 中文简介
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK 和 TensorFlow 2 的综合性 AI 学习项目。该项目通过实战案例帮助学习者系统掌握从传统机器学习到深度学习的完整知识体系。

### 2. 核心功能
- 实现多种经典机器学习算法（SVM、KMeans、逻辑回归、朴素贝叶斯、Adaboost 等）
- 深度学习框架实战（PyTorch、TensorFlow 2、DNN、LSTM、RNN）
- 自然语言处理（NLP）实战（基于 NLTK）
- 关联规则挖掘（Apriori、FP-Growth）
- 推荐系统与降维算法（PCA、SVD）

### 3. 适用场景
- 机器学习入门学习与算法原理验证
- 深度学习框架（PyTorch/TF2）实战入门
- NLP 自然语言处理项目实践
- 推荐系统与数据挖掘算法学习

### 4. 技术亮点
- 覆盖传统机器学习到深度学习的完整技术栈
- 结合理论讲解与代码实战，适合系统学习
- 使用主流框架（PyTorch、TensorFlow 2、scikit-learn）
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42483 | 🍴 11513 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36538 | 🍴 7468 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33847 | 🍴 4717 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29217 | 🍴 3567 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21860 | 🍴 3370 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17385 | 🍴 2125 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36538 | 🍴 7468 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于人工智能的浏览器工作流自动化工具，能够智能地模拟用户操作来完成复杂的网页交互任务。它结合了大语言模型（LLM）和计算机视觉技术，无需编写代码即可自动化执行各种基于浏览器的业务流程。

### 2. 核心功能
- **AI 驱动的智能浏览器操作**：利用大语言模型理解页面内容并自动决策操作
- **视觉感知能力**：通过计算机视觉识别页面元素，无需依赖 DOM 选择器
- **Playwright 底层支持**：基于 Playwright 框架实现稳定的浏览器自动化
- **API 接口支持**：提供 API 便于集成到现有系统中
- **无需代码的自动化**：用户只需描述任务，AI 自动生成执行流程

### 3. 适用场景
- **RPA 替代方案**：替代传统 Rule-based RPA 工具（如 Power Automate），处理更复杂的网页操作
- **电商自动化**：自动比价、下单、监控库存等电商场景
- **数据抓取与录入**：从网页提取数据并自动填写到系统中
- **跨平台工作流**：自动化需要多步骤、多页面交互的重复性任务

### 4. 技术亮点
- 将 **LLM + 视觉感知** 结合，突破了传统自动化对页面结构变化的脆弱性
- 支持 **GPT 系列模型**，可利用最新大模型能力提升任务理解精度
- 兼容 **Selenium/Puppeteer/Playwright** 等多种浏览器自动化工具生态
- 22,851 星标表明其在开源社区具有较高的关注度和认可度
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22851 | 🍴 2146 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，提供开源、云端和企业级产品，以及标注服务。它支持图像、视频和3D标注，具备AI辅助标注、质量保证、团队协作、数据分析及开发者API等功能。

### 2. 核心功能
- **AI辅助标注**：利用人工智能自动识别和标注图像/视频中的对象，大幅提升标注效率。
- **多格式支持**：支持图像、视频和3D数据的全方位标注，涵盖边界框、语义分割等多种标注类型。
- **团队协作**：内置团队管理功能，支持多人协作标注项目，提升数据标注的生产力。
- **质量保证**：提供标注质量检查机制，确保数据集的准确性和一致性。
- **开发者API**：开放API接口，便于集成到现有的机器学习工作流中。

### 3. 适用场景
- **图像分类与目标检测**：用于构建ImageNet、COCO等数据集的标注工作。
- **视频分析项目**：对视频帧进行逐帧标注，适用于行为识别、跟踪等任务。
- **3D点云标注**：支持3D场景标注，适用于自动驾驶、机器人视觉等领域。
- **企业级数据标注**：大型团队可借助其协作功能完成大规模数据集标注。

### 4. 技术亮点
- **开源免费**：基于开源协议，提供完整的源代码，可自由部署和定制。
- **生态兼容**：支持与PyTorch、TensorFlow等主流深度学习框架集成。
- **云端+本地双模式**：既可作为SaaS服务使用，也可私有化部署，灵活适配不同需求。
- **活跃社区**：GitHub星标超过1.6万，社区活跃，持续更新维护。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16594 | 🍴 3815 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
pytorch-grad-cam 是一个专注于计算机视觉的高级AI可解释性工具库，支持CNN、Vision Transformers等多种模型架构。它提供Grad-CAM、Score-CAM等多种可视化方法，帮助开发者理解深度学习模型的决策过程。

### 2. 核心功能
- 支持多种可解释性方法（Grad-CAM、Grad-CAM++、Score-CAM、XGrad-CAM等）
- 兼容主流网络架构（CNN、Vision Transformers）
- 支持图像分类、目标检测、语义分割等多种任务
- 支持图像相似度分析的可解释性可视化
- 提供直观的注意力热图输出

### 3. 适用场景
- 深度学习模型的可解释性研究与分析
- 图像分类模型决策依据的可视化展示
- 目标检测和分割模型的关注区域分析
- AI可信度评估与模型调试

### 4. 技术亮点
- 作为GitHub上星标数近1.3万的高人气项目，是PyTorch生态中最流行的可解释性工具之一
- 统一接口支持多种CAM变体算法，便于对比实验
- 对Vision Transformers等新型架构的良好兼容性
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间AI的几何计算机视觉库，基于PyTorch构建。它提供了一套可微分的计算机视觉算子和工具，专为深度学习集成而设计，支持图像处理和几何变换等操作。

### 2. 核心功能
- 提供可微分的计算机视觉算子，便于与深度学习模型集成
- 支持几何变换、图像处理和相机模型等操作
- 兼容PyTorch生态，可直接在神经网络中使用
- 面向机器人和空间AI应用优化

### 3. 适用场景
- 深度学习驱动的计算机视觉任务（如图像分割、目标检测）
- 机器人视觉和空间感知系统开发
- 需要可微分图像处理的端到端神经网络训练
- 传统计算机视觉算法的深度学习集成

### 4. 技术亮点
- 完全基于PyTorch实现，支持GPU加速
- 算子可微分，可直接反向传播优化
- 专注于几何计算机视觉，填补传统CV与深度学习之间的空白
- 链接: https://github.com/kornia/kornia
- ⭐ 11324 | 🍴 1234 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8876 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3486 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3428 | 🍴 421 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2636 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2506 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

# openclaw 项目分析

## 1. 中文简介
openclaw 是一款个人 AI 助手，支持任意操作系统和平台，以"龙虾方式"（The lobster way）重新定义数据所有权，让用户完全掌控自己的 AI 体验。

## 2. 核心功能
- 跨平台兼容，支持任意操作系统和运行环境
- 强调数据所有权，用户可完全掌控自己的 AI 数据
- 提供个人化 AI 助手功能，满足日常助理需求
- 采用 TypeScript 开发，具备良好的类型安全和可维护性
- 开源项目，社区活跃，星标数超过 38 万

## 3. 适用场景
- 希望在本地部署个人 AI 助手，避免数据上传到第三方云端的用户
- 需要跨平台（Windows/Mac/Linux）统一 AI 助理体验的开发者
- 注重数据隐私和自主权，希望"拥有自己数据"的个人用户
- 对 AI 助手进行自定义开发或二次集成的技术团队

## 4. 技术亮点
- **数据主权优先**：以"own-your-data"为核心理念，区别于主流云端 AI 服务
- **跨平台架构**：基于 TypeScript 构建，天然适配多操作系统和运行环境
- **高社区认可度**：超过 38 万星标，证明项目具备广泛用户基础和成熟度
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387596 | 🍴 81364 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub 项目分析：superpowers

### 1. 中文简介
Superpowers 是一个实用的 AI 代理技能框架与软件开发方法论。它通过子代理驱动的开发模式，为软件开发生命周期提供了一套完整的技能体系，帮助开发者更高效地完成编码任务。

### 2. 核心功能
- **AI 代理驱动开发**：利用子代理自动执行开发任务，实现子代理驱动的开发流程
- **技能框架体系**：提供结构化的技能模块，支持头脑风暴、编码等开发环节
- **完整 SDLC 支持**：覆盖软件开发生命周期各阶段，从规划到交付全流程赋能
- **协作式头脑风暴**：集成 AI 辅助的创意碰撞与方案设计能力
- **模块化技能组合**：灵活调用不同技能组合，适配多样化开发需求

### 3. 适用场景
- **快速原型开发**：通过 AI 代理加速从想法到可运行代码的转化过程
- **团队协作开发**：多子代理并行处理不同模块，提升团队开发效率
- **技术方案设计**：利用 AI 辅助进行架构设计与技术选型头脑风暴
- **自动化编码工作流**：将重复性编码任务交由代理自动完成

### 4. 技术亮点
- **Shell 原生实现**：基于 Shell 脚本构建，轻量且易于集成到现有工作流中
- **高社区认可度**：星标数超过 27 万，表明其在开发者社区中具有广泛影响力
- **OBRA 方法论融合**：将经过验证的开发方法论与 AI 能力相结合，兼顾规范性与智能化
- 链接: https://github.com/obra/superpowers
- ⭐ 277513 | 🍴 24824 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# Hermes-Agent 项目分析

## 1. 中文简介

Hermes-Agent 是一款智能 AI 代理工具，能够伴随用户共同成长并持续优化。它支持多种主流大语言模型，为用户提供灵活、可扩展的自动化助手体验。

## 2. 核心功能

- 支持 Claude、ChatGPT 等多个主流大语言模型
- 提供智能代理能力，可自动执行复杂任务
- 具备持续学习和成长特性，适应不同用户需求
- 兼容 Codex 等开源代码生成工具
- 由 Nous Research 团队开发维护，社区活跃

## 3. 适用场景

- 软件开发中的自动化代码生成与审查
- 日常工作中的智能助手与任务自动化
- 需要多模型切换的灵活 AI 应用场景
- 个人效率提升与重复性任务处理

## 4. 技术亮点

- 采用 Python 开发，生态兼容性好，易于集成
- 支持多模型切换，用户可根据需求灵活选择
- 项目星标数超过 23 万，社区认可度高
- 由知名 AI 研究机构 Nous Research 维护，技术实力有保障
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 236359 | 🍴 47724 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，可自托管或云端部署，并提供 400+ 种集成。

### 2. 核心功能
- **可视化工作流构建**：拖拽式界面，无需编码即可创建复杂自动化流程
- **原生 AI 集成**：内置 AI 能力，支持 LLM 调用、Agent 编排和智能工作流
- **400+ 应用集成**：覆盖主流 SaaS 服务和 API，支持 MCP 协议
- **灵活部署模式**：支持自托管和云端两种方式，数据完全自主可控
- **低代码 + 自定义代码混合开发**：既适合非技术人员快速上手，也支持开发者编写自定义逻辑

### 3. 适用场景
- **企业自动化**：自动化审批流程、数据同步、通知推送等业务场景
- **AI 应用开发**：快速构建 RAG 系统、AI Agent 和工作流驱动的 AI 应用
- **数据集成与 ETL**：跨系统数据抽取、转换和加载，实现多平台数据打通
- **API 编排与集成**：连接多个 API 服务，构建复杂的后端工作流

### 4. 技术亮点
- **MCP 协议支持**：原生支持 Model Context Protocol，可轻松连接各类 AI 模型和数据源
- **Fair-code 模式**：代码公开透明，兼顾开放性与商业可持续性
- **TypeScript 开发**：类型安全，开发体验良好，生态活跃
- **社区活跃**：20万+ 星标，拥有庞大的社区和模板库
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202409 | 🍴 60381 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于实现人人可用的 AI 愿景，让每个人都能使用并在此基础上构建。我们的使命是提供必要的工具，让您能够专注于真正重要的事物。

## 2. 核心功能
- 支持自主代理（Agentic AI）执行复杂任务
- 兼容多种大语言模型（LLM），包括 GPT、Claude、Llama 等
- 提供开放可扩展的 AI 构建工具
- 支持 OpenAI API 集成
- 基于 Python 开发的开源框架

## 3. 适用场景
- 自动化日常任务与工作流
- 快速构建 AI 代理应用的原型开发
- 研究和实验自主 AI 系统
- 企业级 AI 工具链集成

## 4. 技术亮点
- 多模型兼容架构，支持 GPT、Claude、Llama 等多种 LLM API
- 模块化设计，便于二次开发与功能扩展
- 活跃的开源社区，星标数超过 18 万
- 专注于降低 AI 应用开发门槛
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186860 | 🍴 46050 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 172286 | 🍴 9520 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167893 | 🍴 21668 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164659 | 🍴 30557 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 158031 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153675 | 🍴 9932 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

