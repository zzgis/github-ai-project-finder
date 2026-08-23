# GitHub AI项目每日发现报告
日期: 2026-08-23

## 新发布的AI项目

### x64dbg-mcp-server
- 

## x64dbg-mcp-server 项目分析

### 1. 中文简介
x64dbg-MCP Server 是专为 x64dbg 调试器开发的原生 MCP（模型上下文协议）插件，通过 HTTP 接口暴露调试器的全部功能。任何兼容 MCP 的 AI 助手均可连接此服务器，以编程方式控制 x64dbg，实现断点设置、代码单步执行、内存读取、寄存器转储等操作。

### 2. 核心功能
- 通过 HTTP 接口暴露 x64dbg 调试器完整功能
- 支持与任意 MCP 兼容的 AI 助手集成
- 可编程设置断点、单步执行代码
- 支持读取内存和寄存器数据
- 提供项目转储（dump）等调试操作

### 3. 适用场景
- **AI 辅助逆向工程**：让 Claude 等 AI 助手协助分析二进制文件
- **恶意软件分析**：自动化调试和分析可疑程序行为
- **安全研究自动化**：通过 AI 驱动批量调试和漏洞挖掘
- **智能调试助手**：结合 AI 理解代码逻辑，提升调试效率

### 4. 技术亮点
- 使用 **Zig 语言**开发，零依赖、单二进制文件输出
- 跨平台支持，便于在不同系统上部署
- 原生 MCP 协议集成，无缝对接主流 AI 工具链
- 链接: https://github.com/duty1g/x64dbg-mcp-server
- ⭐ 473 | 🍴 55 | 语言: Zig
- 标签: ai-agents, ai-debugging, binary-analysis, claude, claude-code

### biosecurity-agent
- 

## biosecurity-agent 项目分析

### 1. 中文简介
这是一个AI代理工具，能够为任何目标构建实时生物安全分析环境。它通过人工智能技术模拟和评估围绕指定目标的生物安全威胁，帮助用户全面了解潜在风险态势。

### 2. 核心功能
- 围绕指定目标自动构建实时生物安全监控环境
- 利用AI代理技术进行生物安全威胁识别与评估
- 动态模拟生物安全风险场景，提供可视化分析结果
- 支持对多种目标类型进行生物安全态势推演
- 自动生成生物安全风险评估报告与建议措施

### 3. 适用场景
- 生物安全研究与威胁态势评估
- 实验室及生物设施安全管理与风险预测
- 公共卫生安全监测与应急响应决策
- 生物安全政策制定与合规性审查

### 4. 技术亮点
- 基于TypeScript开发，具备良好的类型安全性和代码可维护性
- 采用AI代理架构，实现自动化分析与决策支持
- 实时构建生物安全世界模型，支持动态态势推演
- 轻量级设计，易于集成到现有安全分析流程中
- 链接: https://github.com/Forsy-AI/biosecurity-agent
- ⭐ 312 | 🍴 12 | 语言: TypeScript

### solo-skills
- 描述: 1인 사업가 생산성 키트 — 직원 없이 49개를 자동화했고, 그중 바로 쓸 수 있는 AI 에이전트 스킬 26개(+실행 스크립트)를 공개합니다
- 链接: https://github.com/bam-bam-2/solo-skills
- ⭐ 156 | 🍴 36 | 语言: Python
- 标签: agent-skills, ai-agent, automation, claude-code, korean

### MeshLAN
- 

## MeshLAN 项目分析

### 1. 中文简介
MeshLAN是一款基于Nebula构建的自托管虚拟局域网解决方案，采用P2P优先架构，支持服务共享、多中继节点和AI自动化功能，无需依赖第三方云服务即可组建安全私有的虚拟网络。

### 2. 核心功能
- **自托管虚拟LAN**：完全自主部署，无需依赖任何第三方云服务
- **P2P优先通信**：设备间优先建立点对点直连，降低延迟
- **多中继节点支持**：在P2P直连不可用时自动切换至中继转发
- **服务共享**：支持在同一虚拟网络中共享内部服务
- **AI自动化**：内置AI功能，智能管理网络拓扑与连接

### 3. 适用场景
- 远程团队组建安全的虚拟局域网，共享内部资源和服务
- 家庭或小型办公室搭建去中心化私有网络，访问各设备上的服务
- 存在NAT穿透需求的复杂网络环境，通过中继节点实现跨网互联
- 希望通过AI自动化简化网络拓扑管理的场景

### 4. 技术亮点
- 基于成熟的Nebula VPN内核，安全性与稳定性有保障
- P2P优先+多中继的混合架构，兼顾性能与可用性
- Go语言编写，编译部署便捷，跨平台兼容性好
- 链接: https://github.com/zhaoxuya520/MeshLAN
- ⭐ 148 | 🍴 14 | 语言: Go
- 标签: golang, mesh-network, nat-traversal, nebula, p2p

### doop
- 

## doop 项目分析

### 1. 中文简介
doop 是 Paper.design 的开源替代方案，提供多人协作设计画布，支持人类与 AI 代理实时共同设计。项目内置 MCP（Model Context Protocol）协议，兼容 Claude 生态，可无缝集成 AI 设计助手。

### 2. 核心功能
- **多人实时协作**：支持多用户同时在画布上编辑设计内容
- **AI 代理集成**：人类与 AI 代理可在同一画布中协同工作
- **MCP 协议支持**：内置 Model Context Protocol，便于扩展 AI 能力
- **Claude 生态兼容**：与 Claude、Claude Code 等工具深度集成
- **开源设计工具**：提供免费的替代 Paper.design 的设计平台

### 3. 适用场景
- 团队协作进行 UI/UX 设计，同时利用 AI 辅助生成设计方案
- 设计师与 AI 代理实时共创，快速迭代设计原型
- 需要 MCP 协议支持的企业级 AI 设计工作流
- 追求开源替代方案的创意设计与协作项目

### 4. 技术亮点
- 基于 TypeScript 构建，类型安全且易于维护
- 原生支持 MCP 协议，扩展性强
- 与 Anthropic Claude 生态深度整合，可利用 Claude Code 等工具增强设计能力
- 开源架构，社区可自由定制和扩展功能
- 链接: https://github.com/kgoedecke/doop
- ⭐ 105 | 🍴 10 | 语言: TypeScript
- 标签: ai-agents, canvas, claude, claude-code, claude-design

### AI-Glossary-Handbook
- 描述: 无描述
- 链接: https://github.com/h9-tec/AI-Glossary-Handbook
- ⭐ 91 | 🍴 6 | 语言: 未知

### clipfactory
- 描述: Topic + template → short vertical video from your own B-roll: AI script, voice, scene plan, captions, FFmpeg render. Multi-persona, AI shot lists, AI B-roll, batch generation. Source-available (Elastic 2.0).
- 链接: https://github.com/feyzilim/clipfactory
- ⭐ 66 | 🍴 9 | 语言: Python
- 标签: content-creation, elevenlabs, fastapi, ffmpeg, openai

### netwalk
- 描述: Read-only network survey toolkit for AI coding agents: crawl a site from one device, diagnose it, draw it, and hand over a report — without ever changing a device or seeing a credential.
- 链接: https://github.com/ripmilla/netwalk
- ⭐ 61 | 🍴 19 | 语言: Python

### mediagen
- 描述: AI image and video generation skill for Claude Code and other coding agents — Gemini, OpenAI and Kie AI behind one CLI and MCP server, with EU AI Act content marking.
- 链接: https://github.com/Cripacx/mediagen
- ⭐ 55 | 🍴 0 | 语言: TypeScript
- 标签: agent-skill, ai-agents, claude, claude-code, cli

### LiveStream-Agent-Studio
- 描述: 面向抖音直播电商的 Windows 本地 AI Agent Studio，贯通主播发现、直播洞察、直播复盘与短视频内容编导的统一智能工作流。
- 链接: https://github.com/HanyuanWang/LiveStream-Agent-Studio
- ⭐ 48 | 🍴 8 | 语言: Python
- 标签: ai-agent, douyin, livestream, speech-to-text

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP是一个全面的中英文自然语言处理资源集合项目，涵盖敏感词检测、实体抽取、情感分析、知识图谱、语音识别等核心NLP功能。项目集成了大量中文预训练模型、行业词库、数据集和实用工具，为开发者提供一站式中文NLP开发资源。

## 2. 核心功能

1. **文本基础处理**：敏感词检测、繁简体转换、停用词、情感值计算、文本摘要与关键词抽取
2. **实体识别与抽取**：手机号/身份证/邮箱抽取、命名实体识别(NER)、关系抽取、事件三元组抽取
3. **语言资源库**：中日文人名库、成语词库、地名词库、医学/法律/汽车/财经等行业词库
4. **预训练模型**：BERT、ALBERT、ERNIE、RoBERTa等中文预训练模型及微调代码
5. **语音与OCR**：中文语音识别(masr)、手写汉字识别(cnocr)、语音情感分析

## 3. 适用场景

1. **中文NLP项目开发**：快速集成分词、NER、情感分析等基础功能
2. **知识图谱构建**：提供实体抽取、关系抽取、图谱构建工具及1.4亿实体数据
3. **智能问答系统**：包含医疗问答、百科问答、对话机器人等完整方案
4. **文本数据分析**：适用于舆情监控、谣言检测、文本分类等应用场景

## 4. 技术亮点

- 集成BERT/ALBERT/ERNIE/GPT2等多种前沿预训练模型的中文版本及微调示例
- 涵盖从基础工具(分词/词性标注)到高级任务(知识图谱/对话系统)的完整NLP技术栈
- 提供大量竞赛TOP方案源码和行业领域专属资源(医疗/金融/法律等)
- 包含语音识别、OCR、文本可视化等多模态NLP工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82620 | 🍴 15274 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36471 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具，支持多种主流框架的模型格式，帮助用户直观地查看和分析模型结构。

## 2. 核心功能
- 支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、safetensors 等多种模型格式
- 以图形化方式展示神经网络层结构、连接关系和参数信息
- 提供模型推理调试功能，可执行前向传播并查看中间层输出
- 支持模型文件对比，便于分析不同版本之间的差异
- 纯 JavaScript 实现，无需安装即可在浏览器中直接打开使用

## 3. 适用场景
- 深度学习模型开发过程中的结构审查与调试
- 模型格式转换前的兼容性验证与可视化检查
- 团队协作中的模型文档生成与方案评审
- AI 教学与演示中直观展示神经网络工作原理

## 4. 技术亮点
- **跨平台零依赖**：纯 JavaScript 编写，支持 Web 浏览器和桌面客户端，无需额外安装环境
- **广泛格式覆盖**：支持超过 30 种模型格式，兼容主流深度学习框架生态
- **内置执行引擎**：可在可视化界面中直接运行模型推理，无需依赖原框架
- **开源活跃**：33,000+ 星标，社区贡献活跃，持续更新维护
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33389 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（开放神经网络交换）是机器学习的开放标准，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同框架之间无缝迁移模型，打破框架壁垒，提升AI开发的灵活性与效率。

### 2. 核心功能
- 提供统一的模型格式，支持跨框架模型转换与部署
- 兼容主流深度学习框架，包括 PyTorch、TensorFlow、Keras 等
- 支持模型推理优化，适配多种硬件平台（CPU、GPU、移动端等）
- 拥有活跃的社区支持和丰富的算子库
- 提供模型检查、转换和可视化工具链

### 3. 适用场景
- 将 PyTorch 训练的模型转换为 ONNX 格式，部署到 TensorFlow 或移动端环境
- 在异构硬件平台上运行推理，如从服务器 GPU 迁移到边缘设备
- 跨框架协作开发，不同团队使用不同框架训练和部署模型
- 模型性能优化与加速，结合 ONNX Runtime 进行推理加速

### 4. 技术亮点
- 由微软和 Facebook 联合发起，生态成熟且被广泛采用
- 支持动态形状（Dynamic Shapes），适应可变输入尺寸
- 与 ONNX Runtime 深度集成，提供跨平台高性能推理引擎
- 持续演进，不断扩展对最新深度学习算子的支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21348 | 🍴 4006 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的开源指南，内容涵盖从模型训练到推理部署的完整生命周期。该项目以Python为核心语言，为AI工程师和研究人员提供系统化的工程实践参考。

## 2. 核心功能
- **大规模模型训练**：提供基于PyTorch的分布式训练方案和可扩展架构
- **推理优化**：涵盖LLM推理加速、GPU利用和性能调优策略
- **基础设施管理**：包括Slurm集群调度、存储方案和网络配置指南
- **调试与可观测性**：提供模型调试工具和性能监控方法
- **MLOps实践**：覆盖从开发到生产部署的完整工程流程

## 3. 适用场景
- 大语言模型（LLM）的训练与微调工程实践
- 大规模GPU集群的分布式训练部署
- 机器学习系统的推理优化与生产化部署
- MLOps团队的基础设施建设与运维参考

## 4. 技术亮点
- 聚焦生产级ML工程实践，填补了从研究到落地的知识空白
- 涵盖前沿LLM工程挑战，如GPU调试、网络优化和存储方案
- 开源免费，社区驱动持续更新，星标数近1.9万表明其广泛认可度
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18691 | 🍴 1204 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17384 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13278 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11630 | 🍴 916 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10692 | 🍴 5696 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析

## 1. 中文简介
该项目是一个收录了500个AI项目（含完整代码）的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。它是一个备受瞩目的Awesome列表，为学习者、开发者和研究人员提供了丰富的实践项目参考。

## 2. 核心功能
- 收录500个AI相关项目，全部附带可运行的代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大技术领域
- 提供分类清晰的Awesome列表，便于快速检索和定位
- 以Python为主要编程语言，适合不同层次的学习者使用

## 3. 适用场景
- **初学者入门**：通过完整项目代码快速理解AI各领域的实际应用
- **教学与培训**：教师或培训机构可用作课程实践案例库
- **项目灵感参考**：开发者可借鉴项目思路进行二次开发或创新
- **技术面试准备**：求职者可通过项目实践提升实战能力

## 4. 技术亮点
- 高星标（36,471+）证明其社区认可度和实用价值极高
- 标签体系完善，涵盖AI、数据科学、机器学习、深度学习、NLP等多个热门方向
- 项目全部附带代码，强调"学以致用"的实战导向
- 作为Awesome列表，持续更新和维护，资源生态丰富
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36471 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具，支持多种主流框架的模型格式，帮助用户直观地查看和分析模型结构。

## 2. 核心功能
- 支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、safetensors 等多种模型格式
- 以图形化方式展示神经网络层结构、连接关系和参数信息
- 提供模型推理调试功能，可执行前向传播并查看中间层输出
- 支持模型文件对比，便于分析不同版本之间的差异
- 纯 JavaScript 实现，无需安装即可在浏览器中直接打开使用

## 3. 适用场景
- 深度学习模型开发过程中的结构审查与调试
- 模型格式转换前的兼容性验证与可视化检查
- 团队协作中的模型文档生成与方案评审
- AI 教学与演示中直观展示神经网络工作原理

## 4. 技术亮点
- **跨平台零依赖**：纯 JavaScript 编写，支持 Web 浏览器和桌面客户端，无需额外安装环境
- **广泛格式覆盖**：支持超过 30 种模型格式，兼容主流深度学习框架生态
- **内置执行引擎**：可在可视化界面中直接运行模型推理，无需依赖原框架
- **开源活跃**：33,000+ 星标，社区贡献活跃，持续更新维护
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33389 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## cheatsheets-ai 项目分析

### 1. 中文简介
本项目为深度学习与机器学习研究人员提供了必备的速查手册集合，涵盖常用库和框架的快速参考。内容源自 Medium 文章《机器学习与深度学习研究者的必备速查表》。

### 2. 核心功能
- 提供 NumPy、SciPy 等数值计算库的快速语法参考
- 整理 Keras 深度学习框架的核心 API 与使用技巧
- 汇总 Matplotlib 数据可视化的常用绘图方法
- 覆盖机器学习研究中的关键概念与代码示例

### 3. 适用场景
- 深度学习/机器学习研究人员快速查阅 API 用法
- 数据科学家进行数值计算和可视化时的参考手册
- 初学者系统学习 ML/DL 常用工具的使用指南
- 面试准备或项目开发中的速查工具

### 4. 技术亮点
- 以简洁的速查表形式呈现，便于快速检索
- 整合多个核心 AI 库（NumPy、SciPy、Keras、Matplotlib）于一体
- 内容面向研究人员，聚焦实用性和高效性
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，收录了近200个实战案例与项目，并提供免费配套教材。内容涵盖从零基础入门到就业实战的完整路径，涉及Python、机器学习、深度学习、计算机视觉、自然语言处理等多个热门领域。

### 2. 核心功能
- 提供系统化AI学习路线图，覆盖从入门到进阶的完整学习路径
- 收录近200个实战案例与项目，帮助学习者积累实践经验
- 免费提供配套教材和学习资料，降低学习门槛
- 涵盖Python、数学、机器学习、深度学习、CV、NLP等主流技术领域
- 支持PyTorch、TensorFlow、Keras、Caffe等多种深度学习框架

### 3. 适用场景
- 零基础初学者系统学习人工智能与机器学习知识
- 希望转行AI领域的开发者进行就业实战训练
- 需要参考实战案例提升项目经验的在校学生
- 想要梳理知识体系的学习者作为复习参考指南

### 4. 技术亮点
- 项目星标数高达13278，说明在社区中具有较高的认可度和影响力
- 内容覆盖全面，从基础数学到前沿深度学习技术均有涉及
- 实战导向，注重理论与实践结合，适合就业需求
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13278 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络和其他 AI 模型。它支持多种数据类型和模型架构，让开发者能够快速训练和部署机器学习模型，而无需编写大量代码。

## 2. 核心功能
- 支持表格数据、文本、图像、音频和结构化数据的模型训练
- 提供声明式 YAML 配置，简化模型构建流程
- 内置多种预训练模型和迁移学习支持
- 支持分布式训练和模型部署
- 集成主流深度学习框架（PyTorch）

## 3. 适用场景
- 快速原型开发：适合需要快速验证想法的数据科学家和工程师
- 多模态 AI 应用：构建同时处理文本、图像、音频的复杂模型
- 企业级模型部署：用于生产环境中的大规模模型训练和推理
- 教育学习：作为学习深度学习框架的入门工具

## 4. 技术亮点
- **低代码设计**：通过简洁的配置文件即可定义复杂模型架构
- **多模态支持**：原生支持表格、文本、图像、音频等多种数据类型
- **可扩展性强**：模块化架构便于自定义扩展
- **社区活跃**：11746 星标，拥有活跃的开源社区支持
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11746 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9183 | 🍴 1230 | 语言: Python
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
- ⭐ 6431 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介

funNLP 是一个全面的中英文自然语言处理资源汇总项目，涵盖敏感词检测、语言识别、信息抽取、词库资源、预训练模型及数据集等丰富内容，适合中文NLP开发者一站式获取所需工具和资源。

## 2. 核心功能

- **基础NLP工具**：中英文敏感词过滤、语言检测、手机号/身份证/邮箱抽取、繁简体转换
- **词库资源大全**：中日文人名库、中文缩写库、同义词/反义词/否定词库、汽车品牌词库、古诗词库等数十个领域词库
- **预训练模型与工具**：BERT、ALBERT、ELECTREA等中文预训练模型，SpaCy中文模型，文本分类/摘要/NER工具
- **知识图谱与问答**：中文知识图谱构建工具、医疗/金融领域知识图谱、基于知识图谱的问答系统
- **数据集与评测**：中文NLP竞赛数据集、语音识别语料、情感分析数据集、各类基准任务测评

## 3. 适用场景

- **中文NLP项目开发**：快速集成分词、NER、情感分析等基础功能
- **企业敏感词过滤系统**：利用敏感词库和暴恐词表构建内容审核系统
- **知识图谱构建**：参考项目中的实体抽取、关系抽取工具构建领域知识图谱
- **NLP学习与研究**：通过项目汇总的数据集、模型和论文资源系统学习中文NLP

## 4. 技术亮点

- **资源聚合全面**：汇集数百个中文NLP相关项目、数据集、词库和模型，一站式解决中文NLP开发需求
- **覆盖领域广泛**：从基础分词到知识图谱、从文本处理到语音识别，涵盖NLP全链条
- **紧跟前沿技术**：收录BERT、GPT-2、ALBERT、ELECTREA等最新预训练模型及中文适配版本
- **实用工具丰富**：提供jieba加速版、OCR工具、文本可视化工具等即拿即用的实用组件
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82620 | 🍴 15274 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介

LlamaFactory 是一个统一且高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调。该项目已在 ACL 2024 会议上发表，提供了一站式解决方案，涵盖从指令微调、LoRA 到 RLHF 的完整训练流程。

### 2. 核心功能

- **多模型支持**：兼容 Llama、Qwen、DeepSeek、Gemma、GPT 等 100+ 主流大模型
- **高效微调方法**：支持 LoRA、QLoRA、全参数微调等多种参数高效微调（PEFT）技术
- **量化训练**：提供 INT4/INT8 量化支持，降低显存占用
- **RLHF 训练**：内置基于人类反馈的强化学习（RLHF）微调能力
- **多模态支持**：支持视觉语言模型（VLM）的微调训练

### 3. 适用场景

- **企业级模型定制**：基于开源大模型进行领域适配和指令微调
- **资源受限环境**：使用 QLoRA 和量化技术在消费级 GPU 上微调大模型
- **多模态应用开发**：训练支持图像理解的多模态语言模型
- **强化学习对齐**：通过 RLHF 优化模型输出，使其更符合人类偏好

### 4. 技术亮点

- 统一框架整合多种微调方法，无需切换工具
- ACL 2024 学术背书，代码质量和方法论经过同行评审
- 对 MoE（混合专家）架构模型提供支持
- 与 Hugging Face Transformers 生态无缝集成
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74299 | 🍴 9092 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66478 | 🍴 12853 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# AI Engineering from Scratch 项目分析

## 1. 中文简介

该项目旨在从零开始学习、构建并部署AI工程系统，帮助开发者深入理解AI技术原理并掌握实际应用能力。项目涵盖从基础理论到工程实践的完整学习路径。

## 2. 核心功能

- 从零实现AI/ML模型，深入理解底层原理而非仅调用API
- 构建AI智能体（Agents）和MCP协议相关应用
- 涵盖计算机视觉、NLP、强化学习等多领域实践
- 提供生成式AI和大语言模型（LLM）的完整教程
- 支持Python、Rust、TypeScript多语言实现

## 3. 适用场景

- AI工程师希望深入理解模型内部机制，提升工程能力
- 学生或开发者系统学习AI工程化全流程
- 团队需要构建基于Agent的AI应用系统
- 对Swarm Intelligence（群体智能）等前沿方向感兴趣的研究者

## 4. 技术亮点

- **跨语言覆盖**：同时使用Python、Rust、TypeScript实现，兼顾性能与开发效率
- **全栈AI工程**：从深度学习基础到生成式AI、智能体系统的完整技术链
- **高人气项目**：47816星标，说明社区认可度高，学习资料丰富
- **MCP协议支持**：紧跟AI工程前沿，支持Model Context Protocol标准
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47816 | 🍴 8426 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub项目分析：ailearning

### 1. 中文简介
这是一个全面的机器学习与深度学习实战学习项目，内容涵盖数据分析、线性代数基础、以及基于PyTorch和TensorFlow 2的深度学习实践，同时包含自然语言处理相关技术。

### 2. 核心功能
- 实现多种经典机器学习算法，包括分类、聚类和关联规则挖掘
- 提供深度学习模型构建与训练，支持DNN、LSTM、RNN等架构
- 集成NLTK工具包进行自然语言处理实践
- 构建推荐系统模型
- 涵盖线性代数等数学基础，理论与实践并重

### 3. 适用场景
- 机器学习入门学习者的系统化学习路径
- 数据科学从业者提升算法实践能力
- 深度学习研究者的模型构建参考
- NLP和推荐系统开发者的技术方案参考

### 4. 技术亮点
- 涵盖从传统机器学习到深度学习的完整技术栈，同时融合PyTorch和TensorFlow 2两大主流框架
- 项目获得42475星标，说明其受到广泛认可
- 结合数学基础与实战代码，适合从零开始系统学习
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42475 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36471 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33840 | 🍴 4712 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29185 | 🍴 3562 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21852 | 🍴 3361 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17384 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个收录了500个AI项目的精选集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码。该项目在GitHub上获得了36471个星标，是AI学习领域非常受欢迎的资源库。

### 2. 核心功能
- 收录500个AI实战项目，覆盖机器学习、深度学习、计算机视觉和NLP四大方向
- 每个项目均提供可直接运行的完整代码实现
- 项目分类清晰，便于按领域快速定位学习资源
- 聚合了来自社区的优质开源AI项目，形成一站式学习平台

### 3. 适用场景
- AI初学者系统学习机器学习与深度学习项目实战
- 研究人员和工程师寻找特定领域的开源项目参考
- 学生完成课程作业或毕业设计时获取项目灵感
- 企业团队进行技术选型时参考同类项目的实现方案

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，堪称AI领域的项目百科全书
- 标签体系完善，便于按技术方向（如computer-vision、nlp等）精准筛选
- 作为Awesome列表类项目，持续由社区维护和更新，资源质量有保障
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36471 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于 AI 的浏览器工作流自动化工具，能够智能地自动化执行基于浏览器的任务。它利用大语言模型（LLM）和计算机视觉技术，让浏览器自动化变得更加智能和高效。

### 2. 核心功能
- AI 驱动的浏览器自动化，可智能理解和执行复杂的网页交互任务
- 支持 Playwright、Puppeteer、Selenium 等多种浏览器自动化工具
- 利用大语言模型分析网页内容并自主做出操作决策
- 提供 REST API 接口，便于集成到现有系统和工作流中
- 结合计算机视觉技术，能够"看到"并理解网页界面元素

### 3. 适用场景
- 自动化网页数据抓取、表单填写和批量操作
- 替代传统 RPA 工具处理需要登录或复杂交互的网页任务
- 企业级工作流自动化，如电商价格监控、订单处理等
- 需要 AI 辅助判断的网页操作场景（如动态内容识别）

### 4. 技术亮点
- 将 LLM 推理能力与浏览器自动化结合，突破传统脚本化自动化的局限
- 多框架兼容（Playwright/Puppeteer/Selenium），灵活适配不同需求
- 视觉理解能力使其能够处理动态渲染和复杂 UI 的网页
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22837 | 🍴 2143 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介

CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，专为视觉AI应用设计。该平台提供开源、云端和企业级三种产品形态，并支持图像、视频和3D数据的标注，具备AI辅助标注、质量保证、团队协作、数据分析及开发者API等核心能力。

## 2. 核心功能

1. **AI辅助标注**：利用预训练模型自动识别和标注目标，大幅减少人工工作量
2. **多模态标注支持**：同时支持图像、视频帧序列和3D点云数据的标注
3. **团队协作**：多人可并行参与标注任务，支持角色分配与进度管理
4. **质量保证机制**：提供标注结果校验和审核功能，确保数据集一致性
5. **开发者API**：开放RESTful API，便于与企业内部系统或自动化流程集成

## 3. 适用场景

1. **计算机视觉数据集构建**：为图像分类、目标检测、语义分割等模型准备训练数据
2. **自动驾驶与机器人感知**：标注3D点云和摄像头视频流，用于环境感知模型训练
3. **视频行为分析与目标追踪**：对视频逐帧标注，支持行为识别、轨迹预测等研究
4. **学术研究项目**：高校和研究机构用于视觉AI教学实验与论文数据生产

## 4. 技术亮点

- 开源项目拥有 **16,577 个星标**，社区活跃度极高
- 原生支持 **PyTorch** 和 **TensorFlow** 等主流深度学习框架
- 标注类型覆盖全面：边界框（Bounding Box）、语义分割、图像分类、目标检测等
- 提供 **ImageNet** 等知名数据集的标注模板，开箱即用
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16577 | 🍴 3812 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub 项目分析：pytorch-grad-cam

---

## 1. 中文简介
该项目是一个面向计算机视觉的高级 AI 可解释性工具库，支持 CNN 和 Vision Transformer 架构。它提供了多种可视化方法，帮助理解模型的决策依据。适用于分类、目标检测、分割等多种视觉任务。

---

## 2. 核心功能
- 支持 Grad-CAM、Score-CAM 等多种类激活图生成方法
- 兼容 CNN 和 Vision Transformer 等多种网络架构
- 覆盖图像分类、目标检测、语义分割和图像相似度等多种任务
- 提供直观的可视化输出，便于分析模型关注区域
- 基于 PyTorch 实现，易于集成到现有项目中

---

## 3. 适用场景
- **模型可解释性分析**：理解深度学习模型在图像分类时的决策依据
- **目标检测调试**：定位模型检测物体时关注的图像区域
- **医学影像分析**：可视化模型对病灶区域的识别情况，辅助临床诊断
- **模型优化验证**：对比不同架构或参数下模型的注意力分布差异

---

## 4. 技术亮点
- 集成多种主流 XAI 方法（Grad-CAM、Score-CAM、Grad-CAM++ 等），一站式满足多样化需求
- 对 Vision Transformer（ViT）等新型架构提供原生支持，紧跟技术前沿
- 代码结构清晰，API 设计简洁，快速上手成本低
- 社区活跃，星标数超过 12900，说明在学术界和工业界均具有较高的认可度
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12958 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# 项目分析：Kornia

## 1. 中文简介
Kornia是一个专为空间AI设计的几何计算机视觉库，基于PyTorch构建。它将传统计算机视觉算法与深度学习无缝融合，提供可微分的图像处理工具，支持端到端的神经网络训练。

## 2. 核心功能
- 提供丰富的可微分几何计算机视觉算子（如相机标定、立体视觉、图像变换）
- 与PyTorch原生集成，支持GPU加速和自动微分
- 涵盖图像处理、特征检测、立体匹配等传统CV任务
- 支持机器人导航、SLAM等空间感知应用场景
- 提供预训练模型和常用数据增强工具

## 3. 适用场景
- 机器人视觉导航与空间感知系统开发
- 深度学习驱动的图像配准与立体视觉研究
- 可微分计算机视觉流水线构建
- 自动驾驶中的3D视觉感知任务

## 4. 技术亮点
- **可微分设计**：所有操作支持自动微分，可直接嵌入神经网络训练流程
- **PyTorch原生**：与PyTorch生态无缝衔接，API设计简洁直观
- **学术与工业兼顾**：既适合研究探索，也适用于生产环境部署
- **活跃社区**：Hacktoberfest参与项目，社区贡献活跃，持续迭代更新
- 链接: https://github.com/kornia/kornia
- ⭐ 11324 | 🍴 1233 | 语言: Python
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
- ⭐ 3391 | 🍴 415 | 语言: Python
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

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全属于你的个人 AI 助手，支持任意操作系统和平台。它以"龙虾方式"运行，强调数据主权与隐私保护，让你真正掌控自己的 AI 体验。

### 2. 核心功能
- 跨平台兼容，支持所有主流操作系统
- 本地化运行，确保用户数据完全自主可控
- 提供个性化的 AI 助手体验
- 开源项目，代码透明可审计
- 以龙虾（claw）为品牌标识，风格独特

### 3. 适用场景
- 注重隐私的用户希望本地运行 AI 助手，避免数据上传云端
- 开发者希望在任意操作系统上部署个人 AI 助手
- 企业或个人希望拥有可自定义、可审计的 AI 解决方案
- 技术爱好者喜欢开源项目并进行二次开发

### 4. 技术亮点
- **数据主权**：强调"own your data"，用户数据不离开本地
- **跨平台架构**：基于 TypeScript 开发，实现真正的跨 OS 兼容
- **开源生态**：高星标数（38万+）表明社区活跃度高，生态成熟

---

> ⚠️ **提示**：以上分析基于项目提供的描述信息。如需更精确的技术细节（如具体架构、依赖库等），建议查看项目 README 和源码。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387229 | 🍴 81326 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 276563 | 🍴 24738 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
Hermes Agent 是一个能够与你共同成长的 AI 智能体，支持接入多种主流大语言模型。它具备灵活的可扩展性，可根据用户需求持续进化能力，是个人AI助手的理想选择。

### 2. 核心功能
- 支持多模型接入，兼容 Claude、GPT 等主流大语言模型
- 具备自我学习与进化能力，可随使用持续优化表现
- 提供灵活的 Agent 框架，支持自定义扩展和插件开发
- 集成代码执行环境，可直接辅助编程任务

### 3. 适用场景
- 个人日常 AI 助手，处理各类问答与任务
- 软件开发辅助，代码编写与调试
- 自动化工作流，集成到日常开发流程中

### 4. 技术亮点
- 多模型兼容架构，支持 Anthropic Claude、OpenAI GPT 等多种后端切换
- 基于 Nous Research 研究基础，在开源社区具有较高影响力
- 高星标认可度（23万+），说明项目成熟度和社区活跃度高
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 234769 | 🍴 47277 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

# n8n 项目分析

## 1. 中文简介
n8n 是一款公平开源的工作流自动化平台，内置原生 AI 能力。它支持可视化拖拽构建与自定义代码结合，可选择自托管或云端部署，并提供 400 多种集成。

## 2. 核心功能
- 可视化工作流编辑器，支持拖拽式节点搭建自动化流程
- 内置 AI 能力，可集成大语言模型进行智能处理
- 提供 400+ 预置集成，覆盖主流 SaaS 服务和 API
- 支持 MCP（Model Context Protocol）协议，实现 AI 工具扩展
- 灵活部署方式，支持自托管和云版本

## 3. 适用场景
- 企业内部自动化流程搭建，如数据同步、审批流转
- 多系统 API 集成与数据管道构建
- AI 驱动的智能工作流，如自动摘要、智能客服
- 低代码/无代码平台的业务自动化解决方案

## 4. 技术亮点
- 基于 TypeScript 开发，类型安全且易于扩展
- 支持 MCP 客户端和服务端，实现 AI 模型与工具的无缝对接
- Fair-code 许可证，兼顾开源社区与商业友好性
- 20万+ GitHub 星标，社区活跃度高
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202098 | 🍴 60326 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建AI的愿景。我们的使命是提供所需工具，让你能够专注于真正重要的事。

## 2. 核心功能
- 支持多种大语言模型（GPT、Claude、LLaMA等），用户可自由选择后端
- 具备自主任务规划与分解能力，能自动将复杂目标拆解为可执行步骤
- 内置工具调用系统，可自主使用浏览器、文件操作、代码执行等工具完成任务
- 提供长期记忆机制，支持跨会话的信息存储与检索
- 开源可扩展架构，开发者可基于其构建自定义AI代理

## 3. 适用场景
- **自动化工作流**：自动完成重复性任务（如数据抓取、报告生成）
- **研究与分析**：自主搜索相关资料并整理成结构化报告
- **编程辅助**：自动编写、测试和调试代码片段
- **个人助手**：日常事务管理、信息汇总与决策支持

## 4. 技术亮点
- 多LLM后端无缝切换，降低对单一厂商的依赖
- 自主循环（Autonomous Loop）架构，实现无需人工干预的持续任务执行
- 丰富的插件生态，支持通过扩展工具集灵活适配不同场景
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186809 | 🍴 46050 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 171258 | 🍴 9500 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167803 | 🍴 21655 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164621 | 🍴 30549 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157972 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153584 | 🍴 9918 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

