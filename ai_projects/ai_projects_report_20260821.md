# GitHub AI项目每日发现报告
日期: 2026-08-21

## 新发布的AI项目

### coldcard-airgap
- 

## coldcard-airgap 项目分析

### 1. 中文简介
这是一个专为 Coldcard 硬件钱包用户提供的离线工具集，涵盖 PSBT 检查、BIP39/骰子熵生成、种子 XOR 拆分/合并、BBQr 编码解码、输出描述符及固件验证指导等功能。作为官方 Coldcard 固件的配套工具，与 Coinkite 公司无隶属关系。

### 2. 核心功能
- **PSBT 检查**：离线查看和验证部分签名比特币交易
- **BIP39/骰子熵生成**：通过传统骰子方式生成安全的随机种子
- **种子 XOR 拆分与合并**：将助记词拆分或合并，实现种子备份管理
- **BBQr 编码/解码**：Coldcard 专用的二维码数据编码与解码工具
- **输出描述符与固件验证**：解析输出描述符并提供固件完整性验证指导

### 3. 适用场景
- Coldcard 硬件钱包用户的离线交易验证与签名操作
- 需要手动拆分或合并种子备份的高级用户
- 通过骰子方式生成高安全性随机数的场景
- 验证 Coldcard 固件完整性以确保设备安全

### 4. 技术亮点
- 完全离线运行，无需联网，保障硬件钱包操作的安全性
- 与 Coldcard 官方生态深度集成，提供互补工具链
- 支持 BBQr 专用二维码格式，适配 Coldcard 摄像头的离线传输方式
- 纯 Python 实现，轻量易用，适合技术用户自行部署
- 链接: https://github.com/Leutenegger/coldcard-airgap
- ⭐ 608 | 🍴 79 | 语言: Python
- 标签: airgap, airgap-devkit, airgap-download, airgap-setup, airgap-tutorial

### lanshu-create-ai-presenter-video
- 

## GitHub项目分析：lanshu-create-ai-presenter-video

---

### 1. 中文简介
这是一个与AI视频生成提供商无关的Codex技能工具，能够根据文字脚本和授权的主持人照片，生成经过验证的AI虚拟主播视频。

---

### 2. 核心功能
- **多提供商兼容**：不绑定特定AI视频生成平台，支持灵活切换。
- **脚本驱动生成**：根据输入的文字脚本自动生成AI主播视频内容。
- **形象定制**：支持上传授权的主持人照片，用于数字人形象还原。
- **内容验证**：对生成的视频进行质量验证，确保输出效果可靠。

---

### 3. 适用场景
- 企业宣传片或产品介绍视频的快速制作。
- 在线教育课程、培训视频的数字化身录制。
- 新闻播报、内容解说等需要虚拟主播的场景。

---

### 4. 技术亮点
- 采用Codex Skill框架，具备可扩展性和模块化设计。
- 支持数字人形象与脚本内容的精准匹配，提升视频真实感。
- 提供商中立的架构设计，降低对单一平台的依赖风险。
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 244 | 🍴 26 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### github-farm
- 

# GitHub 项目分析：github-farm

## 1. 中文简介
这是一个面向AI网关的生产级多平台OAuth收集与会话管理框架，专为AI代理设计。它支持跨多个平台的身份认证与会话管理，可直接集成至AI网关系统中使用。

## 2. 核心功能
- 支持多平台OAuth认证流程的自动化收集与管理
- 提供会话状态管理，便于AI代理进行身份切换与复用
- 面向AI网关场景优化，支持高并发与生产环境部署
- 采用Python编写，易于集成到现有AI基础设施中

## 3. 适用场景
- AI网关需要统一管理多个第三方平台（如Google、GitHub等）的OAuth登录状态
- 多账号批量管理场景，如社交媒体自动化或API批量调用
- AI代理需要跨平台身份认证以访问不同服务资源
- 企业级AI系统中对OAuth会话进行集中管控

## 4. 技术亮点
- **生产级架构**：代码质量与稳定性面向生产环境设计
- **AI原生友好**：专为AI代理场景优化，降低集成复杂度
- **多平台扩展**：支持灵活扩展新的OAuth认证平台
- **会话集中管理**：统一框架管理多平台会话状态，提升运维效率
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 103 | 🍴 8 | 语言: Python

### narralume
- 

## narralume 项目分析

### 1. 中文简介
narralume 是一款开源的 AI 辅助长篇小说写作工具，集故事设定管理、正文版本控制、AI 协作创作、审稿与交付功能于一体，为创作者提供一站式的长文写作体验。

### 2. 核心功能
- 故事设定管理：系统化整理世界观、角色、剧情线索等设定资料
- 正文版本控制：支持多版本管理，方便回溯与对比不同创作阶段
- AI 协作创作：集成 LLM 能力，辅助构思、续写与润色
- 审稿与交付：内置审阅流程，支持最终稿件输出

### 3. 适用场景
- 长篇网络小说创作：适合连载小说的持续写作与设定维护
- 奇幻/科幻世界观构建：便于系统化管理复杂设定与人物关系
- AI 辅助写作：借助大语言模型突破创作瓶颈、激发灵感
- 个人写作工作室：自托管部署，保护创作隐私与数据安全

### 4. 技术亮点
- 全栈 TypeScript 开发，类型安全且易于维护
- 支持自托管部署，数据完全由用户掌控
- 集成 LLM API，可对接多种大语言模型
- 开源项目，社区可参与贡献与定制开发
- 链接: https://github.com/abligail/narralume
- ⭐ 73 | 🍴 14 | 语言: TypeScript
- 标签: ai-writing, creative-writing, llm, long-form-writing, novel-writing

### neurocursor-ai
- 

## neurocursor-ai 项目分析

### 1. 中文简介
这是一个基于 AI 和摄像头的鼠标光标控制工具，使用 C++ 编写。可将你的网络摄像头转变为免提指点设备——专为游戏打造，同样适用于日常使用及无障碍辅助场景。

### 2. 核心功能
- 基于摄像头的免提鼠标光标控制
- 支持面部追踪与头部追踪
- 支持眼球追踪与视线追踪
- 使用神经网络实现 AI 驱动的精确定位
- 专为游戏优化，兼顾日常使用

### 3. 适用场景
- 游戏玩家：解放双手，提升游戏体验
- 行动不便用户：提供无障碍辅助控制方案
- 日常办公：减少鼠标依赖，提高操作效率
- 演示/展示场景：无需手动操作即可控制光标

### 4. 技术亮点
- 使用 C++ 开发，兼顾性能与实时性
- 结合计算机视觉与机器学习技术
- 支持多种追踪模式（面部、头部、眼球），灵活适配不同需求
- 链接: https://github.com/stems-arraign-48/neurocursor-ai
- ⭐ 50 | 🍴 0 | 语言: C++
- 标签: ai, computer-vision, cplusplus, cpp, cursor-control

### AItoFigma
- 描述: 一个 AI skill，可以把图片或是直接是内容输出到 figma，并且有这规范的尺寸
- 链接: https://github.com/Niall-Young/AItoFigma
- ⭐ 44 | 🍴 4 | 语言: JavaScript

### jiaojie-skill
- 描述: 交接 Skill（Jiaojie）：跨窗口、跨模型、跨设备、跨语言的 AI 上下文交接工具。换窗口，不失忆；换模型，不重来。Open-source AI context handoff.
- 链接: https://github.com/Jordanwei1/jiaojie-skill
- ⭐ 38 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agent, ai-agents, ai-memory, claude-code

### cs-board
- 描述: 将参考声音和中文文案自动生成白板动画视频的本地 AI 工具。
- 链接: https://github.com/ChenShuo2004/cs-board
- ⭐ 31 | 🍴 4 | 语言: Python
- 标签: ai-video, chinese, fastapi, index-tts, react

### codex-guard
- 描述: Quality gate for AI/Codex-generated pull requests: blocks TODO leftovers, leaked secrets, sloppy commits and red CI before they reach main.
- 链接: https://github.com/Akimiya-z/codex-guard
- ⭐ 30 | 🍴 0 | 语言: JavaScript
- 标签: ai, claude-code, code-review, codex, coding-agent

### KPMG_2_GLB
- 描述: This repository contains the lecture materials, notebooks, code, datasets, assignments, demonstrations, and resources used during the Industry-Oriented AI Foundamentals Training Program conducted in August 2026.
- 链接: https://github.com/AnantVerma-2022/KPMG_2_GLB
- ⭐ 29 | 🍴 0 | 语言: Jupyter Notebook

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源集合项目，涵盖敏感词检测、语言识别、实体抽取、词向量、知识图谱等丰富的NLP工具和数据集。该项目整合了大量中文NLP相关的开源资源、预训练模型、语料库及竞赛方案，是中文NLP领域的综合性资源库。

### 2. 核心功能
- 敏感词检测与语言识别，支持中英文敏感词过滤及手机号/身份证/邮箱等实体抽取
- 提供丰富的中文词库资源，包括人名库、缩写库、同义词库、情感词典及多领域专业词库
- 整合多种预训练语言模型（BERT、ERNIE、ALBERT等）及中文NLP竞赛优秀方案
- 包含知识图谱构建工具、问答系统资源及文本生成/摘要相关开源项目
- 提供语音识别语料、OCR工具、文本标注工具及数据增强工具等配套资源

### 3. 适用场景
- 中文NLP项目开发：快速接入分词、NER、情感分析等基础NLP能力
- 知识图谱构建：利用项目中的三元组抽取工具和语料资源构建领域知识图谱
- NLP竞赛参考：获取各大NLP竞赛的TOP方案源码及评测基准
- 语音与文本多模态应用：结合ASR语料、OCR工具和文本处理资源开发语音交互应用

### 4. 技术亮点
- 资源覆盖面极广，从基础工具（分词、词性标注）到前沿模型（BERT、GPT-2）一应俱全
- 特别聚焦中文NLP场景，包含大量中文专属资源（繁简转换、中文人名库、中文语料等）
- 整合了清华大学XLORE、百度信息抽取系统等知名机构/企业的开源成果
- 持续更新，涵盖NLP竞赛前沿方案和最新预训练模型资源
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82586 | 🍴 15272 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36440 | 🍴 7453 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络模型可视化工具，支持多种深度学习框架和机器学习模型格式。它能够帮助开发者和研究人员直观地查看模型结构和层之间的关系。

### 2. 核心功能
- 支持多种模型格式：包括 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite、SafeTensors 等
- 提供清晰的模型结构可视化：以图形化方式展示网络层连接和数据流向
- 支持神经网络、深度学习和机器学习模型的可视化
- 提供详细的层信息查看：包括参数、维度、激活函数等
- 跨平台支持：可在桌面和浏览器中使用

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：初学者可通过可视化理解复杂网络结构
- 跨框架模型转换验证：检查不同框架间模型转换的一致性
- 模型文档生成：为项目生成直观的模型架构图

### 4. 技术亮点
- 支持 safetensors 等新兴模型格式
- 提供浏览器版本，无需安装即可使用
- 社区活跃，星标数超过 3.3 万，是 AI 领域最受欢迎的可视化工具之一
- 开源免费，代码质量高，便于二次开发
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# ONNX 项目分析

## 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习互操作性的开放标准，旨在实现不同深度学习框架之间的模型无缝转换与共享。该项目由微软、Facebook 等科技巨头联合发起，为 AI 生态系统提供了统一的模型交换格式。

## 2. 核心功能
- **跨框架模型转换**：支持 PyTorch、TensorFlow、Keras 等主流框架之间的模型互转
- **统一算子集定义**：提供标准化的算子库，确保模型在不同平台间的一致性
- **推理优化部署**：支持模型压缩、量化与加速，便于在生产环境中高效部署
- **生态系统兼容**：与 scikit-learn 等机器学习库集成，覆盖更广泛的 AI 应用场景

## 3. 适用场景
- **模型迁移**：将训练好的模型从研究框架（如 PyTorch）迁移到生产框架（如 ONNX Runtime）
- **跨平台部署**：在移动端、嵌入式设备或云端不同硬件上运行同一模型
- **性能优化**：利用 ONNX 优化工具对模型进行加速，提升推理效率
- **协作开发**：在团队中使用不同框架时，通过 ONNX 实现模型共享与版本管理

## 4. 技术亮点
- 由微软和 Meta 等头部企业共同维护，社区活跃度高（21,342+ 星标）
- 支持动态形状和复杂图结构，兼容大多数主流深度学习模型架构
- 提供丰富的工具链（如 ONNX Checker、Converter、Optimizer），保障模型质量与兼容性
- 与 ONNX Runtime 深度集成，支持多硬件后端（CPU、GPU、NPU 等）的高效推理
- 链接: https://github.com/onnx/onnx
- ⭐ 21342 | 🍴 4007 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18682 | 🍴 1203 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11630 | 🍴 916 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10692 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36440 | 🍴 7453 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络模型可视化工具，支持多种深度学习框架和机器学习模型格式。它能够帮助开发者和研究人员直观地查看模型结构和层之间的关系。

### 2. 核心功能
- 支持多种模型格式：包括 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite、SafeTensors 等
- 提供清晰的模型结构可视化：以图形化方式展示网络层连接和数据流向
- 支持神经网络、深度学习和机器学习模型的可视化
- 提供详细的层信息查看：包括参数、维度、激活函数等
- 跨平台支持：可在桌面和浏览器中使用

### 3. 适用场景
- 深度学习模型调试：帮助开发者快速定位模型结构问题
- 模型架构学习：初学者可通过可视化理解复杂网络结构
- 跨框架模型转换验证：检查不同框架间模型转换的一致性
- 模型文档生成：为项目生成直观的模型架构图

### 4. 技术亮点
- 支持 safetensors 等新兴模型格式
- 提供浏览器版本，无需安装即可使用
- 社区活跃，星标数超过 3.3 万，是 AI 领域最受欢迎的可视化工具之一
- 开源免费，代码质量高，便于二次开发
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介
该项目为深度学习与机器学习研究者提供了一系列必备速查表，涵盖了核心概念、常用工具和代码示例，便于快速查阅和复习。

### 2. 核心功能
- 提供机器学习和深度学习领域的常用公式与概念速查表
- 涵盖 Keras、NumPy、SciPy、Matplotlib 等常用库的使用技巧
- 适合研究人员快速回顾核心知识点，提高学习与工作效率

### 3. 适用场景
- 机器学习/深度学习初学者快速掌握核心概念与工具使用
- 研究人员在撰写论文或实验时快速查阅公式和代码示例
- 面试准备或知识复习时作为便捷参考资料

### 4. 技术亮点
- 项目星标数高达 15427，说明在社区中具有较高的认可度和使用频率
- 标签涵盖 AI、深度学习、Keras、机器学习、Matplotlib、NumPy、SciPy 等多个技术领域，内容全面实用
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个系统化的人工智能学习路线图项目，整理了近200个实战案例与项目，并免费提供配套教材。该项目适合零基础学习者入门，涵盖从Python基础到AI就业的全链路技能培养。

### 2. 核心功能
- 提供系统化的AI学习路线图，帮助学习者规划学习路径
- 收录近200个实战案例与项目，注重动手能力培养
- 免费提供配套教材与学习资料，降低学习门槛
- 覆盖Python、机器学习、深度学习、NLP、CV等热门技术领域

### 3. 适用场景
- 零基础转行AI领域的学习者系统性入门
- 在校学生补充实战项目经验，提升就业竞争力
- 职场人士利用业余时间学习数据分析与机器学习技能
- 培训机构或自学者作为教学参考资源

### 4. 技术亮点
- 项目星标数超过13000，社区认可度高
- 技术栈全面，涵盖TensorFlow、PyTorch、Keras、Caffe等主流框架
- 数据科学工具链完整，包括NumPy、Pandas、Matplotlib、Seaborn等
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一款低代码框架，用于快速构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它简化了机器学习模型的训练与部署流程，让开发者无需编写大量代码即可创建和微调高性能模型。

## 2. 核心功能
- **低代码模型构建**：通过声明式配置即可创建自定义 AI 模型，大幅降低开发门槛
- **多模态支持**：原生支持文本、图像、数值、类别等多种数据类型的处理与融合
- **LLM 微调能力**：支持对 LLaMA、Llama2、Mistral 等主流大语言模型进行微调训练
- **PyTorch 原生集成**：基于 PyTorch 构建，充分利用其生态系统和灵活性
- **自动化超参数优化**：内置自动调参功能，帮助提升模型性能

## 3. 适用场景
- **快速原型开发**：需要快速验证模型想法、无需深入底层代码的场景
- **企业级数据科学项目**：团队希望以标准化流程构建和维护机器学习模型
- **大模型微调**：对 LLaMA、Mistral 等开源 LLM 进行领域适配和定制训练
- **多模态 AI 应用**：需要同时处理文本、图像等多种输入类型的智能系统

## 4. 技术亮点
- **数据中心（Data-Centric）设计**：强调数据质量驱动模型优化，而非仅依赖模型架构
- **声明式配置**：通过 YAML/JSON 配置文件定义模型结构，便于版本管理和团队协作
- **自动化特征工程**：自动处理数据预处理、特征提取等繁琐步骤
- **社区活跃度高**：GitHub 星标超过 11,000，拥有活跃的开源社区支持
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9181 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8968 | 🍴 3109 | 语言: C++
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
- ⭐ 6423 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP是一个全面的中英文自然语言处理资源集合项目，涵盖了敏感词检测、语言分析、实体抽取、知识图谱构建、语音识别等多个NLP领域的工具和数据集。该项目整合了预训练语言模型、词向量、语料库以及各种NLP任务的相关代码和论文，为中文NLP研究和应用提供了丰富的资源支持。

### 2. 核心功能
- 提供敏感词过滤、语言检测、手机号/身份证/邮箱等实体信息抽取功能
- 整合大量中文词库资源，包括人名库、地名库、成语库、行业专业词库等
- 收录BERT、ALBERT、GPT2等多种预训练语言模型及NLP任务示例代码
- 包含中文OCR、语音识别、知识图谱构建等跨领域工具
- 汇聚NLP竞赛优秀方案、数据集和基准测评资源

### 3. 适用场景
- NLP研究人员和开发者快速查找和整合中文NLP相关开源资源
- 企业构建中文信息抽取、问答系统、聊天机器人等应用
- 学术研究中需要中文语料库、数据集和基准模型进行实验对比
- 语音识别、文本分类、命名实体识别等具体NLP任务开发

### 4. 技术亮点
该项目以资源聚合为核心特色，系统性地整理了中文NLP领域的开源工具、数据集、预训练模型和竞赛方案，极大降低了中文NLP学习和研究的门槛，是中文NLP领域最具参考价值的资源导航项目之一。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82586 | 🍴 15272 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一高效的大语言模型微调框架，支持 100+ 种 LLM 和 VLM 的微调训练。该项目已在 ACL 2024 发表，旨在为研究人员和开发者提供简洁易用的模型微调解决方案。

### 2. 核心功能
- 支持 100+ 种主流大语言模型的统一微调框架
- 提供 LoRA、QLoRA、P-Tuning 等多种高效微调方法
- 支持 RLHF、DPO 等人类反馈对齐训练技术
- 内置量化技术（4/8-bit 量化），降低显存需求
- 支持多模态视觉语言模型（VLM）的微调训练

### 3. 适用场景
- 研究者快速验证不同 LLM 的微调效果
- 开发者基于开源模型（如 Llama、Qwen、DeepSeek）进行领域适配
- 资源受限环境下通过量化微调部署大模型
- 需要指令微调或强化学习对齐的训练任务

### 4. 技术亮点
- 统一的 API 接口支持多种模型架构，降低使用门槛
- 对 Transformer 库进行了深度优化，训练效率显著提升
- 支持 MoE（混合专家）架构模型的微调
- 社区活跃，持续跟进最新模型和训练方法
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74283 | 🍴 9083 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，采用12周、24课时的系统教学方案，旨在让所有人都能轻松学习人工智能。项目以Jupyter Notebook形式呈现，内容覆盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。

### 2. 核心功能
- **系统化课程体系**：12周循序渐进的课程安排，24课时完整覆盖AI基础知识。
- **多领域技术覆盖**：包含机器学习、CNN、RNN、GAN、计算机视觉和NLP等主流AI技术。
- **交互式学习体验**：基于Jupyter Notebook的编程实践，便于边学边练。
- **微软官方背书**：属于"Microsoft for Beginners"系列，质量与权威性有保障。
- **面向零基础学习者**：课程设计通俗易懂，适合AI初学者入门。

### 3. 适用场景
- **高校课程配套**：可作为计算机科学或数据科学专业的AI入门教材。
- **自学入门**：适合零基础的编程爱好者系统学习AI知识。
- **企业培训**：可用于公司内部AI技能普及和基础培训。
- **教育工作者参考**：教师可借鉴课程结构开展AI普及教学。

### 4. 技术亮点
- 高人气开源项目，GitHub星标数超过6.6万，社区活跃度高。
- 标签体系完整，涵盖AI核心领域，技术栈全面。
- 微软官方出品，课程质量和维护水平有可靠保障。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66126 | 🍴 12809 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## AI工程从零开始 (ai-engineering-from-scratch)

### 1. 中文简介
这是一个从零开始学习AI工程的系统性课程项目，帮助学习者掌握核心概念、动手构建AI系统，并最终将其产品化分享给他人。项目涵盖从基础理论到实际部署的完整AI开发生命周期。

### 2. 核心功能
- **从零构建AI系统**：提供深入的理论讲解和动手实践，帮助学习者从基础开始掌握AI工程
- **多领域覆盖**：包含智能体(Agents)、计算机视觉、大语言模型(LLM)、自然语言处理(NLP)等核心AI领域
- **完整学习路径**：结合教程(Tutorial)和课程(Course)形式，提供系统化的学习体验
- **生成式AI实战**：专注于生成式AI和Transformer等前沿技术的实际应用
- **多语言支持**：涵盖Python、Rust、TypeScript等多种编程语言

### 3. 适用场景
- AI初学者希望系统性地从零学习AI工程理论与实践
- 开发者想要构建智能体(Agents)和LLM应用的实战项目参考
- 团队或个人希望将AI模型产品化并部署给他人使用
- 需要深入理解强化学习、群体智能等进阶AI技术的开发者

### 4. 技术亮点
- **多模态AI覆盖**：同时涵盖NLP、计算机视觉和生成式AI
- **智能体与群体智能**：包含MCP协议和Swarm Intelligence等前沿技术
- **多语言技术栈**：结合Python(机器学习)、Rust(高性能计算)、TypeScript(前端部署)
- **高人气项目**：47,543颗星标证明其广泛认可度和社区影响力
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47543 | 🍴 8355 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：AiLearning

### 1. 中文简介
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK 和 TensorFlow 2 的综合性学习项目，内容全面覆盖经典机器学习算法与深度学习框架，适合系统性地学习和实践。

### 2. 核心功能
- **机器学习算法实现**：集成 scikit-learn，涵盖 SVM、逻辑回归、KMeans、朴素贝叶斯、AdaBoost 等经典算法
- **深度学习实战**：基于 PyTorch 和 TensorFlow 2，实现 DNN、RNN、LSTM 等神经网络模型
- **自然语言处理**：利用 NLTK 进行文本处理与 NLP 任务实践
- **推荐系统与关联规则**：实现基于协同过滤的推荐系统及 Apriori、FP-Growth 关联规则挖掘
- **数据降维与代数基础**：涵盖 PCA、SVD 等降维技术及线性代数知识

### 3. 适用场景
- 机器学习初学者系统学习算法原理与代码实现
- 数据分析工程师提升实战技能，快速掌握常用 ML 工具
- 深度学习研究者参考 PyTorch/TF2 模型搭建与训练流程
- 自然语言处理入门者学习文本处理与基础 NLP 应用

### 4. 技术亮点
- 技术栈全面，从传统 ML 到深度学习、NLP 全覆盖
- 基于主流框架（PyTorch + TF2 + scikit-learn），代码实用性强
- 高星标（42470）说明社区认可度高，是热门学习资源
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42470 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36440 | 🍴 7453 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33838 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29167 | 🍴 3554 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21844 | 🍴 3358 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

## 1. 中文简介
该项目是一个精选的AI项目合集，包含500个涵盖机器学习、深度学习、计算机视觉和自然语言处理领域的开源项目，每个项目均附带完整代码。作为一个星标数超过3.6万的热门资源列表，它为AI学习者和开发者提供了丰富的实践参考。

## 2. 核心功能
- 收录500个AI相关开源项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带可运行的源代码，便于直接学习和实践
- 项目按领域分类整理，方便用户快速定位感兴趣的方向
- 作为awesome列表，持续收录和更新高质量的AI项目资源

## 3. 适用场景
- AI初学者系统学习：通过实际项目快速掌握各领域的核心概念和实现方法
- 开发者寻找灵感：参考现有项目思路，加速自身AI项目的开发进程
- 教学与培训：作为课程实践案例，帮助学生理解理论知识的实际应用
- 技术选型参考：了解当前AI领域的主流项目和最佳实践

## 4. 技术亮点
- 项目规模庞大（500个），覆盖AI主要细分领域，资源全面
- 高星标数（36440）证明其社区认可度和实用性
- 全部项目附带代码，强调实践导向而非纯理论
- 使用Python标签，表明项目主要基于Python生态，便于开发者上手
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36440 | 🍴 7453 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于 AI 的浏览器自动化框架，能够智能地完成各种基于网页的工作流任务。它通过结合大语言模型（LLM）和计算机视觉技术，让机器像人类一样操作浏览器，无需手动编写复杂的自动化脚本。

### 2. 核心功能
- **AI 驱动浏览器操作**：利用大语言模型理解页面内容并自动执行点击、填写、导航等操作
- **多浏览器引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **视觉感知能力**：通过计算机视觉识别页面元素，实现类似人类的交互体验
- **RESTful API 接口**：提供简洁的 API，方便集成到现有工作流中
- **无头/有头模式**：支持无界面运行和可视化调试两种模式

### 3. 适用场景
- **RPA 流程自动化**：替代传统规则型 RPA，处理复杂多变的网页操作场景
- **数据抓取与表单提交**：自动完成跨网站的数据采集和表单填写任务
- **重复性网页操作**：如电商比价、票务预订、报告生成等日常重复性工作
- **系统集成测试**：模拟真实用户行为进行端到端的 Web 应用测试

### 4. 技术亮点
- 将 LLM 的语义理解能力与浏览器自动化相结合，大幅降低自动化脚本编写门槛
- 支持多引擎切换，可根据场景灵活选择最适合的底层自动化工具
- 提供 API 优先的设计，便于与企业现有系统无缝集成
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22824 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一个领先的平台，用于构建高质量的视觉数据集，服务于视觉AI应用。它提供开源、云和企业级产品，支持图像、视频和3D标注，具备AI辅助标注、质量保证、团队协作、数据分析和开发者API等核心功能。

### 2. 核心功能
- **AI辅助标注**：利用预训练模型自动标注，大幅提升标注效率
- **多格式支持**：支持图像、视频和3D点云数据的标注
- **团队协作**：多人协同标注，支持任务分配和质量审核
- **质量保证**：内置质检机制，确保数据集标注准确性
- **开放API**：提供开发者API，便于集成到现有工作流

### 3. 适用场景
- **自动驾驶**：标注道路场景图像和视频，训练目标检测模型
- **医疗影像**：标注CT、MRI等医学图像，辅助疾病诊断
- **零售安防**：标注监控视频，训练人流分析、行为识别模型
- **遥感分析**：标注卫星图像，用于地物分类和变化检测

### 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供丰富的标注类型：边界框、语义分割、关键点等
- 开源免费，可私有化部署，保障数据安全
- 与主流数据集格式（如ImageNet）兼容
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16564 | 🍴 3809 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN、Vision Transformers等多种架构，涵盖分类、目标检测、分割等任务的可视化解释。

### 2. 核心功能
- 提供Grad-CAM、Score-CAM等经典可视化方法的PyTorch实现
- 支持CNN和Vision Transformer架构的类激活图生成
- 兼容图像分类、目标检测、语义分割等多种任务
- 提供图像相似度可视化和模型决策解释
- 内置丰富的可视化工具便于结果展示

### 3. 适用场景
- 深度学习模型的可解释性研究，帮助理解模型决策依据
- 计算机视觉任务中定位关键区域，如医学影像分析
- 验证模型是否关注正确特征，排查偏见问题
- 向非技术 stakeholders 展示AI决策过程

### 4. 技术亮点
- 12957+星标，是计算机视觉可解释性领域的热门开源项目
- 统一接口支持多种CAM变体（Grad-CAM、Score-CAM、Layer-CAM等）
- 对Vision Transformers等新型架构的良好支持
- 代码质量高，文档完善，易于集成到现有项目
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# kornia 项目分析

## 1. 中文简介
kornia 是一个专为空间 AI 设计的几何计算机视觉库。它为 PyTorch 提供了可微分的图像处理和计算机视觉操作，使研究人员和开发者能够轻松构建端到端的视觉 AI 系统。

## 2. 核心功能
- 提供可微分的几何计算机视觉操作（如仿射变换、透视变换）
- 支持基于 PyTorch 的深度学习图像处理流水线
- 包含丰富的图像处理算法（滤波、形态学、色彩空间转换）
- 集成相机模型和三维几何计算工具
- 支持机器人视觉和空间感知应用

## 3. 适用场景
- **自动驾驶系统**：用于实时图像处理和环境感知
- **机器人视觉**：实现机器人的空间理解和导航
- **医学图像分析**：处理和分析医疗影像数据
- **增强现实（AR）**：构建基于视觉的空间计算应用

## 4. 技术亮点
- 完全兼容 PyTorch，可与现有深度学习框架无缝集成
- 所有操作均可微分，支持端到端训练
- 针对 GPU 加速优化，提供高性能计算
- 活跃的开源社区，持续更新和维护
- 支持 Hacktoberfest 等开源贡献活动
- 链接: https://github.com/kornia/kornia
- ⭐ 11322 | 🍴 1230 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3485 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3388 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2507 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全属于你的个人 AI 助手，支持任意操作系统和平台，以"龙虾方式"（即数据自主、本地运行）重新定义个人 AI 体验。该项目强调用户对自己数据的完全控制权，是一款开源、跨平台的 AI 助手解决方案。

### 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行，无需锁定特定环境。
- **数据自主可控**：用户完全掌握自己的数据，无需依赖第三方云服务。
- **本地化 AI 助手**：在本地运行 AI 模型，保障隐私与安全。
- **开源免费**：基于开源协议发布，可自由使用和修改。
- **TypeScript 开发**：使用 TypeScript 编写，具备良好的类型安全和可维护性。

### 3. 适用场景
- 注重数据隐私、希望将 AI 助手部署在本地环境的个人用户。
- 需要在不同操作系统间无缝切换使用的跨平台开发者。
- 希望基于开源项目二次开发、定制个性化 AI 助手的团队。
- 对云服务依赖敏感、追求数据自主权的隐私倡导者。

### 4. 技术亮点
- 采用 TypeScript 构建，代码结构清晰、类型安全，便于社区贡献和扩展。
- 支持多平台部署，适配性强，降低用户使用门槛。
- 以"own-your-data"为核心理念，在本地完成数据处理，避免数据泄露风险。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387044 | 🍴 81299 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# 项目分析：superpowers

## 1. 中文简介
superpowers 是一个基于 AI 代理的技能框架与软件开发方法论，通过子代理驱动开发流程，帮助开发者更高效地完成编程任务。它将 AI 能力与标准化开发流程相结合，提供了一套可落地的智能开发解决方案。

## 2. 核心功能
- **子代理驱动开发**：通过多个 AI 子代理协同完成复杂开发任务
- **技能框架体系**：提供结构化的 AI 技能模块，支持灵活组合与复用
- **完整 SDLC 支持**：覆盖从头脑风暴到代码实现的全软件开发生命周期
- **协作式头脑风暴**：集成 AI 辅助的创意发散与需求分析能力
- **模块化方法论**：将开发流程拆解为可复用的技能单元

## 3. 适用场景
- 需要 AI 辅助完成复杂编程任务的个人开发者或团队
- 希望将 AI 代理能力集成到现有开发流程中的企业
- 探索智能化软件开发方法论的研究与实践者
- 需要快速原型开发或头脑风暴的项目初期阶段

## 4. 技术亮点
- 采用 Shell 脚本实现，轻量且易于集成到现有工具链
- 首创"子代理驱动开发"（Subagent-Driven Development）范式
- 将 ORBA（Objective-Result-Breakdown-Action）方法论与 AI 能力深度融合
- 高社区认可度（27.5万星标），验证了该框架的实用价值
- 链接: https://github.com/obra/superpowers
- ⭐ 275629 | 🍴 24642 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# hermes-agent 项目分析

## 1. 中文简介
hermes-agent 是一款智能 AI 代理工具，能够随着你的使用不断成长和学习。它支持多种主流大语言模型，包括 Claude、GPT 等，为用户提供灵活的 AI 助手体验。

## 2. 核心功能
- 支持多种大语言模型（Claude、OpenAI 等）
- 具备持续学习与成长能力
- 提供智能对话与代码辅助功能
- 可集成到开发工作流中

## 3. 适用场景
- 日常编程辅助与代码审查
- AI 对话与知识问答
- 自动化任务处理

## 4. 技术亮点
- 多模型兼容架构，灵活切换不同 LLM 后端

---

> 注：由于该项目信息有限，以上分析基于项目名称、描述和标签推断。如需更准确的功能细节，建议查阅项目官方文档或 README。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233977 | 🍴 46977 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201538 | 🍴 60272 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 秉承"让每个人都能使用并构建AI"的愿景，致力于提供易用的AI工具。我们的使命是打造必要的工具，让您能够专注于真正重要的事物。

### 2. 核心功能
- 支持自主规划与执行复杂任务，无需人工逐步干预
- 集成多种大语言模型（OpenAI、Claude、Llama等）作为底层推理引擎
- 具备记忆系统，可跨会话保持上下文和积累经验
- 支持多步骤任务分解与迭代反思优化
- 提供丰富的插件生态，可扩展浏览器浏览、文件操作等能力

### 3. 适用场景
- 自动化日常任务（如信息检索、数据整理、报告生成）
- 复杂项目辅助开发（代码编写、调试、文档生成）
- 研究分析与市场调研（自动收集信息并生成摘要）
- AI应用原型快速搭建与实验验证

### 4. 技术亮点
- 采用"Agent循环"架构（规划→执行→反思），实现真正的自主决策
- 支持多模型切换，可根据任务需求灵活选用不同LLM
- 开源且高度可定制，社区活跃，迭代迅速
- 具备工具调用能力，可像人类一样使用外部工具完成任务
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186725 | 🍴 46047 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 170544 | 🍴 9483 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167713 | 🍴 21651 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164609 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157935 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153537 | 🍴 9901 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

