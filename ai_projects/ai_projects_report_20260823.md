# GitHub AI项目每日发现报告
日期: 2026-08-23

## 新发布的AI项目

### MeshLAN
- 

# MeshLAN 项目分析

## 1. 中文简介

MeshLAN 是一个基于 Nebula 构建的自托管 P2P 优先虚拟局域网项目，支持服务共享、多中继和 AI 自动化功能。它使用 Go 语言开发，提供跨平台的 VPN 组网解决方案。

## 2. 核心功能

- **P2P 虚拟局域网**：基于 Nebula 实现点对点直连，减少中继依赖
- **服务共享**：支持在虚拟局域网内共享本地服务和应用
- **多中继架构**：当 P2P 直连不可用时，自动切换到中继服务器
- **NAT 穿透**：内置 NAT 穿越能力，简化复杂网络环境下的连接
- **跨平台支持**：兼容 Windows 等主流操作系统

## 3. 适用场景

- **远程团队协作**：为分布式团队提供安全的虚拟局域网，实现内网服务互通
- **家庭/小型办公室网络**：将分散在不同地点的设备组成统一局域网
- **自托管服务组网**：多个自托管服务（如 Nextcloud、Home Assistant）的安全互联
- **临时项目网络**：快速搭建项目专用虚拟网络，无需复杂 VPN 配置

## 4. 技术亮点

- **Nebula 底层**：利用成熟可靠的 Nebula 协议栈，保证安全性和性能
- **Go 语言开发**：单二进制部署，跨平台编译友好
- **AI 自动化集成**：支持 AI 辅助的网络配置和故障排查
- **P2P 优先策略**：优先直连降低延迟，中继作为备用保证可用性
- 链接: https://github.com/zhaoxuya520/MeshLAN
- ⭐ 110 | 🍴 11 | 语言: Go
- 标签: golang, mesh-network, nat-traversal, nebula, p2p

### x64dbg-mcp-server
- 

# x64dbg-mcp-server 项目分析

## 1. 中文简介
x64dbg-MCP Server 是一个原生的 MCP（Model Context Protocol）插件，专为 x64dbg 调试器设计，通过 HTTP 暴露调试器的完整功能。任何支持 MCP 的 AI 助手均可连接并编程式控制 x64dbg，实现设置断点、单步执行、读取内存、转储寄存器等功能。该项目使用 Zig 语言开发，零依赖，输出单一可执行文件，支持跨平台编译。

## 2. 核心功能
- 通过 HTTP 接口暴露 x64dbg 的全部调试功能
- 支持与任意 MCP 兼容的 AI 助手集成
- 可编程式控制断点设置与代码单步执行
- 支持内存读取与寄存器状态转储
- 零依赖单二进制输出，跨平台编译支持

## 3. 适用场景
- **恶意软件分析**：让 AI 辅助自动化执行逆向分析任务，如动态调试与内存分析
- **安全研究自动化**：通过 AI 助手批量执行调试操作，提升漏洞挖掘效率
- **教学与演示**：利用 AI 交互方式直观展示调试器的工作原理
- **CI/CD 集成**：在自动化测试流程中通过 AI 驱动调试器进行二进制分析

## 4. 技术亮点
- 使用 Zig 语言开发，编译为单一可执行文件，部署简单
- 零外部依赖，交叉编译支持良好，便于在不同平台上运行
- 基于 MCP 协议标准，可无缝对接各类 AI 助手生态
- 链接: https://github.com/duty1g/x64dbg-mcp-server
- ⭐ 108 | 🍴 15 | 语言: Zig

### solo-skills
- 

## solo-skills 项目分析

### 1. 中文简介
该项目是一个面向个人创业者的生产力工具包，作者在没有员工的情况下实现了49项工作流的自动化，并从中精选了15个立即可用的AI代理技能开源分享。项目基于Claude Code构建，使用HTML语言开发，旨在帮助独立创业者提升工作效率。

### 2. 核心功能
- 提供15个开箱即用的AI代理技能，覆盖个人创业常见场景
- 支持自动化工作流程，减少人工操作成本
- 基于Claude Code平台构建，兼容性强
- 面向独立创业者优化，无需团队即可高效运营
- 全部技能公开可复用，降低自动化门槛

### 3. 适用场景
- 个人创业者日常运营中重复性任务的自动化处理
- 小型独立团队借助AI代理提升协作效率
- Claude Code用户快速部署实用技能的工作流
- 希望学习AI代理构建方法的开发者参考

### 4. 技术亮点
- 基于HTML实现，无需复杂环境配置即可运行
- 与Claude Code深度集成，发挥AI代理能力
- 技能模块化设计，便于按需选用和二次开发
- 链接: https://github.com/bam-bam-2/solo-skills
- ⭐ 94 | 🍴 18 | 语言: HTML
- 标签: agent-skills, ai-agent, automation, claude-code, korean

### AI-Glossary-Handbook
- 描述: 无描述
- 链接: https://github.com/h9-tec/AI-Glossary-Handbook
- ⭐ 81 | 🍴 6 | 语言: 未知

### netwalk
- 描述: Read-only network survey toolkit for AI coding agents: crawl a site from one device, diagnose it, draw it, and hand over a report — without ever changing a device or seeing a credential.
- 链接: https://github.com/ripmilla/netwalk
- ⭐ 55 | 🍴 15 | 语言: Python

### clipfactory
- 描述: Topic + template → short vertical video from your own B-roll: AI script, voice, scene plan, captions, FFmpeg render. Multi-persona, AI shot lists, AI B-roll, batch generation. Source-available (Elastic 2.0).
- 链接: https://github.com/feyzilim/clipfactory
- ⭐ 52 | 🍴 9 | 语言: Python
- 标签: content-creation, elevenlabs, fastapi, ffmpeg, openai

### ai-surf-when-bored
- 描述: 无描述
- 链接: https://github.com/sanqianzilanyue/ai-surf-when-bored
- ⭐ 23 | 🍴 1 | 语言: HTML

### notion-ai-crack-2026
- 描述: 无描述
- 链接: https://github.com/vastbehalf/notion-ai-crack-2026
- ⭐ 20 | 🍴 0 | 语言: 未知

### aider-ai-crack-2026
- 描述: 无描述
- 链接: https://github.com/wetfirewall/aider-ai-crack-2026
- ⭐ 19 | 🍴 0 | 语言: 未知

### tarkov-aimbot-2026
- 描述: 无描述
- 链接: https://github.com/trivialinteg/tarkov-aimbot-2026
- ⭐ 19 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP是一个全面的中文自然语言处理工具集与资源仓库，涵盖了从基础文本处理（分词、词性标注、命名实体识别）到高级应用（知识图谱、对话系统、语音识别）的完整生态。项目聚合了大量专业词库、预训练模型、数据集及实用工具，是中文NLP开发者的宝藏资源库。

## 2. 核心功能

- **基础文本处理**：支持中英文敏感词检测、语言识别、分词、词性标注、命名实体识别（人名/地名/机构名）、信息抽取（手机号、身份证、邮箱）
- **丰富词库资源**：提供中日文人名库、中文缩写库、同义词/反义词/否定词库、汽车品牌词库、医学/法律/财经等专业领域词库
- **预训练模型与工具**：整合BERT、ALBERT、RoBERTa等预训练模型，以及文本摘要、关键词抽取、情感分析等工具
- **语音与对话系统**：包含ASR语音识别数据集、中文语音识别系统、多轮对话机器人及问答系统
- **知识图谱构建**：提供知识图谱构建工具、实体链接、关系抽取及图谱问答系统

## 3. 适用场景

- **内容安全审核**：用于网站、APP的敏感词过滤和舆情监控
- **智能客服与问答系统**：基于知识图谱和对话模型的客服机器人开发
- **文本挖掘与分析**：企业文档摘要、关键词提取、情感分析等商业智能应用
- **语音交互系统**：智能音箱、语音助手等需要语音识别和自然语言理解的场景

## 4. 技术亮点

- **资源聚合度高**：一站式整合数百个中文NLP相关项目、数据集和工具，极大降低开发者的信息搜集成本
- **覆盖领域全面**：从基础NLP任务到前沿的预训练模型、知识图谱、语音识别均有涉及
- **实用性强**：提供大量开箱即用的词库和工具，如手机号/身份证抽取、繁简体转换、地名拼音标注等
- **紧跟技术前沿**：持续更新BERT、GPT-2、ALBERT等最新预训练模型及NLP竞赛优秀方案
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82603 | 🍴 15272 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500个AI机器学习深度学习项目合集

### 1. 中文简介
这是一个包含500个AI相关项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目都附带完整代码实现。该项目是一个优秀的开源学习资源库，适合各层次的AI学习者和开发者参考使用。

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供完整可运行的代码实现
- 项目按领域分类整理，便于针对性学习和查找
- 包含从入门到进阶的多样化项目难度级别
- 项目代码可直接克隆使用，便于实践学习

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习项目实践
- 开发者寻找计算机视觉或NLP项目的参考实现
- 学生完成课程作业或毕业设计的灵感来源
- 技术人员快速搭建AI原型项目的代码参考

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流应用领域
- 所有项目均附带完整代码，可直接运行学习
- 标签分类清晰，便于按技术领域筛选项目
- 高星标数（36458）证明社区认可度和实用价值高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36458 | 🍴 7455 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具，能够以直观的图形界面展示模型架构和参数信息。它支持多种主流框架和模型格式，可帮助开发者快速理解和分析模型结构。

## 2. 核心功能
- 支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、safetensors 等多种模型格式
- 以交互式图形方式展示神经网络层结构和连接关系
- 可实时查看各层的参数、权重和形状信息
- 提供桌面客户端和 Web 应用两种使用方式，跨平台兼容
- 支持模型图导出，便于文档记录和论文配图

## 3. 适用场景
- 模型开发过程中快速验证网络结构是否正确
- 将不同框架模型转换为 ONNX 后的结构对比检查
- 教学演示中向初学者直观展示神经网络工作原理
- 模型部署前确认各层参数是否符合预期

## 4. 技术亮点
- 基于 JavaScript 构建，无需安装额外依赖即可在浏览器中运行
- 对 safetensors 等新兴安全模型格式的原生支持
- 开源项目，社区活跃，星标数超过 3.3 万，口碑良好
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33387 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习模型的开放标准格式，旨在实现不同深度学习框架之间的互操作性。它允许开发者在不同框架间无缝迁移模型，打破框架壁垒，提升模型部署的灵活性。

### 2. 核心功能
- **跨框架模型转换**：支持PyTorch、TensorFlow、Keras等主流框架模型的相互转换
- **统一模型格式**：提供标准化的模型表示格式，确保模型在不同平台间保持一致性
- **推理优化**：内置模型优化器，可提升推理性能并减少模型体积
- **多平台部署**：支持在CPU、GPU等多种硬件环境下运行推理
- **生态系统兼容**：与Scikit-learn等传统ML库集成，覆盖更广泛的机器学习场景

### 3. 适用场景
- **模型生产环境部署**：将训练框架（如PyTorch）的模型转换为ONNX后，在推理引擎（如ONNX Runtime）中高效部署
- **跨平台迁移**：在不同深度学习框架间迁移已有模型，避免重新训练的成本
- **边缘设备部署**：将大型模型优化后部署到移动设备或嵌入式系统
- **混合框架项目**：在同一个项目中混合使用不同框架训练的模型组件

### 4. 技术亮点
- 由Facebook和Microsoft联合发起，拥有强大的业界支持背景
- 活跃的开源社区，持续获得主流框架的原生支持
- 提供完整的模型转换、验证和优化工具链
- 支持动态形状（Dynamic Shapes），适应不同输入尺寸的推理需求
- 链接: https://github.com/onnx/onnx
- ⭐ 21348 | 🍴 4007 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一部系统性的机器学习工程实践指南，涵盖从模型训练到部署的全流程技术要点。该项目以开源形式呈现，适合希望深入理解大规模机器学习系统设计与优化的工程师和研究人员。

## 2. 核心功能
- 提供大规模模型训练的完整工程实践指导
- 详解GPU加速、分布式训练及推理优化技术
- 覆盖大语言模型（LLM）的训练与部署全流程
- 包含MLOps最佳实践和系统可扩展性方案
- 整合PyTorch框架的实际应用与调试技巧

## 3. 适用场景
- 需要构建大规模分布式训练集群的数据科学家和ML工程师
- 希望优化LLM推理性能和降低部署成本的团队
- 正在搭建MLOps平台并追求系统可扩展性的企业
- 学习GPU集群管理和Slurm调度系统的研究人员

## 4. 技术亮点
- 内容全面覆盖AI工程化全链路，从底层硬件到上层应用
- 结合Slurm、PyTorch等工业级工具链的实战经验
- 针对大语言模型时代的工程挑战提供专项解决方案
- 开源免费，持续更新，社区活跃（近1.9万星标）
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18687 | 🍴 1204 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17383 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13276 | 🍴 2673 | 语言: 未知
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
- 

## 项目分析：500个AI机器学习深度学习项目合集

### 1. 中文简介
这是一个包含500个AI相关项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目都附带完整代码实现。该项目是一个优秀的开源学习资源库，适合各层次的AI学习者和开发者参考使用。

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供完整可运行的代码实现
- 项目按领域分类整理，便于针对性学习和查找
- 包含从入门到进阶的多样化项目难度级别
- 项目代码可直接克隆使用，便于实践学习

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习项目实践
- 开发者寻找计算机视觉或NLP项目的参考实现
- 学生完成课程作业或毕业设计的灵感来源
- 技术人员快速搭建AI原型项目的代码参考

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流应用领域
- 所有项目均附带完整代码，可直接运行学习
- 标签分类清晰，便于按技术领域筛选项目
- 高星标数（36458）证明社区认可度和实用价值高
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36458 | 🍴 7455 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具，能够以直观的图形界面展示模型架构和参数信息。它支持多种主流框架和模型格式，可帮助开发者快速理解和分析模型结构。

## 2. 核心功能
- 支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、safetensors 等多种模型格式
- 以交互式图形方式展示神经网络层结构和连接关系
- 可实时查看各层的参数、权重和形状信息
- 提供桌面客户端和 Web 应用两种使用方式，跨平台兼容
- 支持模型图导出，便于文档记录和论文配图

## 3. 适用场景
- 模型开发过程中快速验证网络结构是否正确
- 将不同框架模型转换为 ONNX 后的结构对比检查
- 教学演示中向初学者直观展示神经网络工作原理
- 模型部署前确认各层参数是否符合预期

## 4. 技术亮点
- 基于 JavaScript 构建，无需安装额外依赖即可在浏览器中运行
- 对 safetensors 等新兴安全模型格式的原生支持
- 开源项目，社区活跃，星标数超过 3.3 万，口碑良好
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33387 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# GitHub项目分析：Ai-Learn

## 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图项目，整理了近200个实战案例与项目，并免费提供配套教材，帮助零基础学习者入门并实现就业。内容涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域。

## 2. 核心功能
- 提供系统化的AI学习路线图，从零基础到就业实战全覆盖
- 整理近200个实战案例与项目，配套免费教材
- 覆盖主流技术栈：Python、PyTorch、TensorFlow、Keras、Caffe等深度学习框架
- 涵盖数据分析与可视化：NumPy、Pandas、Matplotlib、Seaborn
- 包含数学基础、机器学习、深度学习、NLP、CV等完整知识体系

## 3. 适用场景
- 零基础想转行人工智能领域的初学者
- 需要系统学习AI技术栈的数据科学从业者
- 准备AI相关岗位面试、积累项目经验的求职者
- 希望快速掌握深度学习框架与实战技能的开发者

## 4. 技术亮点
- 项目星标数达13276，说明在社区中具有较高的认可度和影响力
- 学习路径设计完整，从数学基础到就业实战层层递进
- 覆盖主流深度学习框架（PyTorch、TensorFlow、Keras、Caffe），适配不同学习需求
- 实战案例丰富，适合边学边练，快速提升动手能力
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13276 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型、神经网络及其他 AI 模型。它通过声明式配置简化了机器学习模型的训练和部署流程，降低了 AI 开发的技术门槛。

## 2. 核心功能
- 支持通过 YAML/JSON 声明式配置快速定义和训练深度学习模型
- 内置多种预置模型架构，涵盖自然语言处理、计算机视觉等任务
- 支持对 Llama、Mistral 等大语言模型进行微调和训练
- 提供端到端的模型训练、评估和部署工作流
- 兼容 PyTorch 生态，支持 GPU 加速训练

## 3. 适用场景
- 快速原型开发：数据科学家无需编写大量代码即可训练自定义模型
- 大语言模型微调：针对特定任务对 Llama、Mistral 等模型进行微调
- 多模态应用：同时处理文本、图像等多种数据类型
- 生产环境部署：将训练好的模型快速部署到生产环境

## 4. 技术亮点
- 采用数据-centric（以数据为中心）的设计理念，强调数据质量对模型性能的影响
- 提供可复现的训练流程，确保实验结果可追踪和复现
- 支持分布式训练，能够高效利用多 GPU 资源加速模型训练
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9182 | 🍴 1230 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8967 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8370 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6990 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6428 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## 项目分析：funNLP

### 1. 中文简介

funNLP是一个全面的中英文自然语言处理资源集合，涵盖了敏感词检测、语言识别、实体抽取、情感分析、知识图谱构建等核心NLP功能。项目整合了大量预训练模型、数据集、语料库及工具包，为中文NLP研究和应用提供一站式资源支持。

### 2. 核心功能

- **基础NLP工具**：提供敏感词检测、语言识别、繁简体转换、停用词、情感值分析等基础处理能力
- **实体抽取与识别**：支持手机号、身份证、邮箱抽取，以及基于BERT的命名实体识别（NER）
- **词库与知识资源**：包含中日文人名库、中文缩写库、同义词库、反义词库、汽车品牌词库等丰富词库
- **预训练模型集合**：整合BERT、ALBERT、RoBERTa、GPT-2等多种中文预训练语言模型
- **对话与问答系统**：提供聊天机器人、知识图谱问答、多轮对话系统等对话AI相关资源

### 3. 适用场景

- **企业内容审核**：利用敏感词库和暴恐词表实现文本内容安全检测
- **医疗/金融领域NLP**：借助医学词库、金融词库及专用模型进行领域知识抽取和问答
- **中文语音识别开发**：使用ASR数据集和语音识别工具进行语音技术应用
- **学术研究 benchmark**：通过中文NLP数据集和基准测评开展算法研究与模型对比

### 4. 技术亮点

- 项目收录资源极为丰富，涵盖100+个NLP相关项目、数据集和工具
- 整合了清华大学、百度、Facebook等机构的高质量开源资源
- 提供从基础处理到深度学习的全链路NLP工具链，适合不同技术水平的开发者使用
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82603 | 🍴 15272 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100+ 种主流模型。该项目相关研究已发表于 ACL 2024，旨在为研究者和开发者提供一站式模型微调解决方案。

### 2. 核心功能
- 支持 100+ 种大语言模型和视觉语言模型的高效微调
- 集成 LoRA、QLoRA、PEFT 等参数高效微调技术
- 支持 RLHF（基于人类反馈的强化学习）训练流程
- 提供量化训练能力，降低显存占用
- 兼容 Transformers 生态，支持指令微调（Instruction Tuning）

### 3. 适用场景
- **快速微调主流模型**：如 LLaMA、Qwen、DeepSeek、Gemma 等，无需从零训练
- **显存受限环境下的模型优化**：通过 QLoRA 和量化技术在消费级显卡上微调大模型
- **多模态模型训练**：对支持视觉输入的 VLM 进行指令微调
- **企业级模型定制**：基于 RLHF 对齐模型输出，适配特定业务需求

### 4. 技术亮点
- 统一框架支持百余种模型，避免重复配置，大幅降低微调门槛
- 在 ACL 2024 发表，具有学术背书，技术可靠性高
- 对 MoE（混合专家）架构模型提供原生支持
- 结合 Agent 能力，可扩展至智能体应用场景
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74293 | 🍴 9089 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一门为期12周、包含24节课的AI入门课程，由微软推出，旨在让所有人都能轻松学习人工智能。课程涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。

## 2. 核心功能
- 提供系统化的12周AI学习路径，每周2节课
- 基于Jupyter Notebook的交互式编程实践
- 覆盖机器学习、深度学习、CNN、RNN、GAN、NLP等核心主题
- 微软官方出品，适合零基础学习者
- 免费开源，可自主控制学习进度

## 3. 适用场景
- 大学生或职场新人系统学习AI基础知识
- 教师用于课堂教学或课外辅导
- 对AI感兴趣的非技术背景人士入门
- 企业内部分享AI科普培训

## 4. 技术亮点
- 采用微软For Beginners系列成熟的教学框架
- 结合理论与实践，通过Notebook实现动手编码
- 涵盖从传统ML到前沿深度学习的全栈内容
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66375 | 🍴 12840 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## AI工程从零开始 - 项目分析

### 1. 中文简介
"学会它，构建它，为别人交付它。"这是一个从零开始系统学习AI工程的完整教程项目，通过亲手实现的方式帮助学习者掌握前沿AI技术，并最终能够独立开发AI产品。

### 2. 核心功能
- **从零实现AI组件**：不依赖现成框架，深入理解AI底层原理
- **多领域覆盖**：涵盖LLM、计算机视觉、NLP、强化学习等核心方向
- **AI代理开发**：教授智能体（Agent）与群体智能（Swarm）的实现方法
- **生成式AI实践**：包含MCP协议及Transformers等现代架构
- **多语言支持**：结合Python、Rust、TypeScript进行工程化落地

### 3. 适用场景
- AI工程师系统学习，从理论到实战的完整路径
- 希望深入理解AI底层机制而非仅调用API的开发者
- 企业团队搭建AI代理或生成式AI应用的技术储备
- 高校或培训机构用于AI工程课程教学

### 4. 技术亮点
- **"From Scratch"教学理念**：通过手写代码揭示AI本质，避免黑盒依赖
- **多语言混合架构**：Python负责算法原型，Rust保障性能，TypeScript覆盖前端
- **前沿技术同步**：涵盖MCP、Swarm Intelligence等2024-2025年热门方向
- **高社区认可度**：47664星标表明该项目在AI学习者群体中广受好评
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47664 | 🍴 8396 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42472 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36458 | 🍴 7455 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33840 | 🍴 4712 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29178 | 🍴 3559 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21848 | 🍴 3361 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17383 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub 项目分析

### 1. 中文简介
这是一个汇集了 500 个 AI 项目的精选合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大方向，每个项目均附带完整代码实现。项目以 Python 为主，适合从入门到进阶的学习者和开发者参考使用。

### 2. 核心功能
- **海量项目库**：收录 500 个 AI/ML/DL 实战项目，覆盖主流算法与应用场景。
- **完整代码**：每个项目均提供可运行的 Python 代码，便于直接复现与学习。
- **四大领域覆盖**：机器学习、深度学习、计算机视觉、自然语言处理均有专项项目。
- **精选标签**：按领域分类，方便快速定位所需技术栈的项目。
- **社区认证**：3.6 万+ 星标，是 GitHub 上最热门的 AI 项目合集之一。

### 3. 适用场景
- **学生/转行者**：作为系统学习 AI 各方向的实战项目清单，按图索骥逐个完成。
- **开发者面试准备**：挑选与目标岗位相关的项目进行深度复现，展示工程能力。
- **研究者/工程师**：快速查阅某个方向（如目标检测、文本分类）的参考实现。
- **课程/培训**：作为 AI 课程的配套项目库，提供丰富且高质量的课后练习素材。

### 4. 技术亮点
- **awesome 列表风格**：采用社区公认的精选策展模式，质量经过大量使用者验证。
- **多领域交叉**：同时覆盖 CV 和 NLP，适合需要跨领域知识的复合型项目。
- **高活跃度**：36458 星标说明项目长期维护且持续获得社区贡献。
- **Python 生态**：全部基于 Python，与主流 AI 框架（PyTorch/TensorFlow/scikit-learn）无缝对接。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36458 | 🍴 7455 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一个基于 AI 的浏览器工作流自动化工具，利用大语言模型（LLM）智能驱动浏览器完成各类重复性任务。它通过视觉理解和 AI 推理，让机器像人一样操作网页，无需编写复杂的自动化脚本。

### 2. 核心功能
- **AI 驱动的浏览器自动化**：利用大语言模型理解页面内容并智能决策操作
- **视觉感知能力**：通过截图分析页面布局，精准定位和操作页面元素
- **多浏览器引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **API 接口**：提供 RESTful API，便于集成到现有工作流中
- **RPA 替代方案**：作为 Power Automate 等传统 RPA 工具的 AI 增强替代

### 3. 适用场景
- **表单自动填写**：跨网站批量填写注册、申报类表单
- **数据抓取与录入**：从网页提取数据并自动录入到目标系统
- **重复性网页操作**：如定时登录、报表下载、状态监控等
- **企业级工作流自动化**：替代人工完成跨系统的业务流程

### 4. 技术亮点
- 将计算机视觉与 LLM 结合，实现"看懂页面、理解意图"的智能操作
- 无需为每个网站编写定制化脚本，通用性强，适应不同网页结构
- 开源项目，社区活跃（22834+ 星标），生态完善
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22834 | 🍴 2143 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介

CVAT（计算机视觉标注工具）是一款领先的平台，用于构建高质量的视觉数据集以服务于视觉AI。它提供开源、云端和企业级产品，以及标注服务，支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作、数据分析和开发者API。

### 2. 核心功能

- **AI辅助标注**：内置智能标注工具，可自动识别和标注图像/视频中的对象
- **多模态支持**：支持图像、视频和3D点云数据的标注
- **团队协作**：支持多人协作标注、任务分配和质量审核
- **质量保证**：提供标注质量检查和验证机制
- **开发者API**：开放API接口，便于集成到现有工作流中

### 3. 适用场景

- **深度学习数据集构建**：为物体检测、语义分割等任务创建标注数据
- **自动驾驶与机器人**：标注视频和3D数据用于感知模型训练
- **企业级标注团队**：大规模团队协作完成高质量标注任务
- **学术研究**：快速标注图像/视频数据用于计算机视觉研究

### 4. 技术亮点

- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供丰富的标注类型：边界框、图像分类、语义分割等
- 开源免费，社区活跃（16574+星标）
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16574 | 🍴 3812 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
高级计算机视觉AI可解释性工具，支持CNN、视觉Transformer等多种架构，可应用于图像分类、目标检测、图像分割、图像相似度分析等多种任务。

### 2. 核心功能
- 基于Grad-CAM系列方法生成类激活图，可视化模型关注区域
- 支持CNN和Vision Transformer等多种深度学习模型架构
- 提供多种可解释性方法（Grad-CAM、Score-CAM等）
- 兼容图像分类、目标检测、语义分割等多种任务
- 基于PyTorch框架，易于集成到现有项目中

### 3. 适用场景
- 图像分类模型的可解释性分析，定位模型判断依据的区域
- 目标检测与图像分割任务的可视化调试
- 视觉Transformer模型的注意力机制分析
- 图像相似度模型的决策过程解释

### 4. 技术亮点
- 统一接口支持多种Grad-CAM变体，无需为不同方法编写额外代码
- 对Vision Transformer等新兴架构提供原生支持，紧跟技术趋势
- 项目星标数超过1.2万，社区活跃度高，文档完善，是PyTorch生态中最流行的可解释性工具之一
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12957 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

**1. 中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 原生构建，提供了一
- 链接: https://github.com/kornia/kornia
- ⭐ 11323 | 🍴 1231 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3485 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3389 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2635 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2507 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## GitHub 项目分析：openclaw

### 1. 中文简介
OpenClaw 是一款完全属于你自己的个人 AI 助手，支持任意操作系统和平台运行。它以"龙虾"为主题，倡导数据自主可控，让你真正拥有自己的 AI 体验。

### 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行，打破平台限制。
- **数据自主可控**：强调用户数据所有权，隐私安全由你掌控。
- **个人 AI 助手**：提供专属的 AI 辅助能力，服务于个人需求。
- **开源开放**：基于开源社区驱动，支持自定义和二次开发。
- **主题化体验**：以龙虾（🦞）为品牌特色，打造独特用户界面。

### 3. 适用场景
- 希望拥有独立、私密 AI 助手的个人用户。
- 关注数据隐私、不希望数据上传至第三方云服务的开发者。
- 需要在多平台（Windows、macOS、Linux）间统一使用 AI 助手的用户。
- 对开源 AI 项目感兴趣、希望参与社区开发的爱好者。

### 4. 技术亮点
- 使用 **TypeScript** 开发，类型安全且生态成熟。
- 高人气项目（**38万+ 星标**），社区活跃度高。
- 标签体现 **"own-your-data"** 理念，在 AI 助手领域具有差异化定位。
- 跨平台架构设计，适配多种操作系统环境。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387169 | 🍴 81311 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

## 1. 中文简介
这是一个基于AI代理的技能框架与软件开发方法论，旨在通过子代理驱动开发流程来提升软件工程效率。该项目将人工智能代理能力融入传统软件开发生命周期（SDLC），提供从头脑风暴到编码的完整开发支持。

## 2. 核心功能
- **子代理驱动开发**：利用多个AI子代理协同完成软件开发任务
- **技能框架系统**：提供可复用的AI技能模块，支持不同开发场景
- **完整SDLC覆盖**：涵盖从需求分析、设计到编码的软件开发全生命周期
- **头脑风暴辅助**：集成AI头脑风暴功能，辅助创意生成和问题解决
- **多代理协作**：支持多个AI代理并行工作，提升开发效率

## 3. 适用场景
- **AI辅助软件开发**：需要AI代理协助完成编码、调试和代码审查的项目
- **快速原型开发**：希望通过AI加速从概念到原型的开发流程
- **团队协作增强**：利用AI子代理分担开发任务，提升团队生产力
- **创新项目头脑风暴**：需要AI参与创意生成和技术方案讨论的场景

## 4. 技术亮点
- 采用Shell脚本实现，轻量级且易于集成到现有开发流程
- 标签中提到的"OBRA"方法论可能代表独特的开发框架
- 高星标数（276,280）表明该项目在社区中具有较高的认可度和影响力
- 专注于"真正可用"的AI代理框架，强调实用性和可落地性
- 链接: https://github.com/obra/superpowers
- ⭐ 276280 | 🍴 24713 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# hermes-agent 项目分析

## 1. 中文简介
hermes-agent 是一款伴随用户共同成长的人工智能代理工具，能够根据用户的需求和使用习惯不断进化和优化。该项目由 Nous Research 开发，支持多种主流大语言模型，为用户提供智能化的代码辅助与任务执行能力。

## 2. 核心功能
- **多模型支持**：兼容 Claude、GPT 等主流大语言模型，灵活切换不同 AI 能力
- **智能代码辅助**：提供代码生成、审查、调试等开发辅助功能
- **自主任务执行**：能够理解复杂指令并自动完成多步骤任务
- **持续学习与成长**：根据用户交互历史不断优化响应策略和行为模式
- **多场景适配**：支持对话交互、代码仓库操作等多种使用模式

## 3. 适用场景
- 开发者日常编码工作，如代码生成、重构和审查
- 自动化处理重复性技术任务，提升工作效率
- 需要与多个 AI 模型交互的复杂研究或开发项目
- 希望拥有个性化、可成长 AI 助手的个人用户

## 4. 技术亮点
- 由知名 AI 研究团队 Nous Research 开发维护
- 支持 Claude Code、Codex 等多种先进 AI 编程工具
- 拥有超过 23 万星标，社区活跃度极高，生态成熟
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 234458 | 🍴 47181 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款采用公平代码协议的工作流自动化平台，内置原生 AI 能力。它支持可视化搭建与自定义代码相结合，可选择自托管或云端部署，并提供 400 多种集成。

### 2. 核心功能
- 可视化工作流编辑器，支持拖拽式节点构建
- 内置 AI 能力，可直接在工作流中调用 AI 模型
- 提供 400+ 集成，覆盖主流 SaaS 服务和 API
- 支持自托管和云端部署两种模式
- 允许结合自定义代码扩展工作流逻辑

### 3. 适用场景
- 企业级自动化：连接多个系统，实现业务流程自动化（如 CRM 与邮件联动）
- AI 驱动工作流：将 AI 模型集成到日常任务中，实现智能数据处理
- 数据管道构建：自动化数据采集、转换和同步流程
- 低代码/无代码开发：非技术人员也能快速搭建复杂工作流

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且易于扩展
- 支持 MCP（Model Context Protocol）协议，可与 AI 模型深度集成
- 开源公平代码模式，兼顾社区贡献与商业使用
- 提供 CLI 工具，支持命令行操作和 CI/CD 集成
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201902 | 🍴 60310 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于为每个人提供触手可及的 AI 工具，供其使用与二次开发。我们的使命是提供必要的工具，让你能够专注于真正重要的事务。

### 2. 核心功能
- 自主执行复杂任务，无需人工逐步干预
- 支持多种大语言模型（GPT、Claude、LLaMA 等）
- 具备记忆、规划与工具调用能力
- 可扩展的插件架构，支持自定义功能模块
- 可通过 Web UI 或命令行与代理交互

### 3. 适用场景
- **自动化工作流**：如自动搜索信息、整理数据、生成报告
- **代码开发与调试**：自主编写、测试和修复代码
- **研究与学习**：自动收集资料、总结文献、解答问题
- **个人助手**：管理日程、发送消息、处理日常事务

### 4. 技术亮点
- 采用多代理协作架构，支持任务分解与并行执行
- 集成丰富的工具生态（浏览器、文件系统、API 调用等）
- 支持多种 LLM 后端，灵活适配不同需求与成本
- 开源且社区活跃，持续迭代更新（GitHub 星标超 18 万）
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186784 | 🍴 46048 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 171041 | 🍴 9498 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167777 | 🍴 21655 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164616 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157960 | 🍴 46174 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153570 | 🍴 9911 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

