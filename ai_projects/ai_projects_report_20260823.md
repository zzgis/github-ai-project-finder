# GitHub AI项目每日发现报告
日期: 2026-08-23

## 新发布的AI项目

### x64dbg-mcp-server
- 

## 项目分析：x64dbg-mcp-server

### 1. 中文简介
x64dbg-MCP Server 是一个原生 MCP（模型上下文协议）插件，通过 HTTP 暴露 x64dbg 调试器的完整功能。连接任意兼容 MCP 的 AI 助手，即可通过编程方式控制 x64dbg：设置断点、单步执行代码、读取内存、转储寄存器等等。采用 Zig 语言开发——零依赖、单二进制输出、跨平台。

### 2. 核心功能
- 通过 MCP 协议将 x64dbg 调试器功能暴露给 AI 助手
- 支持设置断点、单步执行代码等调试操作
- 支持读取内存、转储寄存器
- 采用 Zig 开发，零依赖，单二进制文件输出
- 跨平台支持

### 3. 适用场景
- **恶意软件分析**：AI 辅助分析恶意代码行为
- **二进制逆向工程**：自动化调试和分析二进制文件
- **AI 辅助调试**：通过自然语言指令控制调试器
- **安全研究**：结合 AI 进行自动化漏洞挖掘

### 4. 技术亮点
- 使用 Zig 语言编写，编译产物为单一可执行文件，部署简便
- 基于 MCP 标准协议，可对接多种 AI 助手（如 Claude Code）
- 零外部依赖，无需安装额外运行时环境
- 将传统 x86/x64 调试器与现代 AI Agent 技术结合
- 链接: https://github.com/duty1g/x64dbg-mcp-server
- ⭐ 417 | 🍴 49 | 语言: Zig
- 标签: ai-agents, ai-debugging, binary-analysis, claude, claude-code

### solo-skills
- 描述: 1인 사업가 생산성 키트 — 직원 없이 49개를 자동화했고, 그중 바로 쓸 수 있는 AI 에이전트 스킬 26개(+실행 스크립트)를 공개합니다
- 链接: https://github.com/bam-bam-2/solo-skills
- ⭐ 151 | 🍴 33 | 语言: Python
- 标签: agent-skills, ai-agent, automation, claude-code, korean

### MeshLAN
- 

## MeshLAN 项目分析

### 1. 中文简介
MeshLAN 是一款基于 Nebula 构建的自托管 P2P 优先虚拟局域网工具，支持服务共享、多中继节点和 AI 自动化。它让多台设备能够安全地组成虚拟局域网，实现跨网络的高效通信。

### 2. 核心功能
- **P2P 优先组网**：设备间直接点对点通信，减少延迟
- **服务共享**：局域网内资源和服务可相互访问
- **多中继支持**：在 NAT 穿透失败时自动回退到中继节点
- **AI 自动化**：集成 AI 能力实现智能网络管理
- **自托管部署**：完全由用户自主控制，无需第三方云服务

### 3. 适用场景
- 远程办公团队组建安全虚拟局域网
- 跨地域设备间共享本地服务（如文件服务器、开发环境）
- 需要穿透复杂 NAT 环境的 P2P 应用部署
- 对数据隐私要求高的自托管网络场景

### 4. 技术亮点
- 基于成熟的 **Nebula** 协议栈，具备优秀的 NAT 穿透能力
- **Go 语言**开发，跨平台兼容性好，支持 Windows 等主流系统
- **P2P-first 架构**优先直连，中继作为备用，兼顾性能与可用性
- 链接: https://github.com/zhaoxuya520/MeshLAN
- ⭐ 145 | 🍴 14 | 语言: Go
- 标签: golang, mesh-network, nat-traversal, nebula, p2p

### AI-Glossary-Handbook
- 

# AI-Glossary-Handbook 项目分析

## 1. 中文简介
该项目是一个AI术语手册/词汇表，旨在为人工智能领域的专业术语提供清晰的定义和解释。项目描述信息缺失，但根据项目名称可推断其定位为AI领域学习者的参考工具。

## 2. 核心功能
- 提供AI领域专业术语的集中定义和解释
- 帮助初学者系统学习人工智能相关概念
- 作为AI术语的快速查询参考工具
- 可能包含术语的英文原文与中文对照

## 3. 适用场景
- AI初学者系统学习专业术语的基础知识
- 技术人员查阅AI相关概念的快速参考
- 团队内部统一AI术语理解的培训材料
- 文档撰写时确保术语使用的一致性

## 4. 技术亮点
该项目为内容型仓库，主要亮点在于术语整理的系统性和实用性，而非技术实现。
- 链接: https://github.com/h9-tec/AI-Glossary-Handbook
- ⭐ 91 | 🍴 6 | 语言: 未知

### doop
- 

## doop 项目分析

### 1. 中文简介

doop 是 Paper.design 的开源替代品，是一款支持多人协作的设计画布工具。人类设计师与 AI 代理可以在此平台上实时协同创作。项目内置 MCP（模型上下文协议）支持，便于与 AI 工具链集成。

### 2. 核心功能

- **多人实时协作画布**：支持多用户同时在设计画布上进行编辑和协作
- **人机协同设计**：设计师可与 AI 代理实时配合完成设计任务
- **内置 MCP 协议**：原生支持 Model Context Protocol，方便对接各类 AI 工具
- **开源免费**：作为 Paper.design 的开源替代方案，可自由使用和定制
- **Claude 生态集成**：深度兼容 Claude 及相关设计工具链

### 3. 适用场景

- **UI/UX 设计团队**：设计师与 AI 助手协作完成界面设计和原型制作
- **远程协作项目**：分布在不同地点的成员实时在同一画布上工作
- **AI 辅助设计工作流**：需要结合 Claude 等 AI 能力进行智能设计辅助的场景
- **设计教学与演示**：讲师与学员或演示者与观众实时互动的设计场景

### 4. 技术亮点

- 基于 TypeScript 构建，类型安全且易于维护扩展
- 原生 MCP 集成，降低了 AI 工具接入的复杂度
- 与 Claude Code / Claude Design 等工具链无缝对接，形成完整的设计 AI 工作流
- 链接: https://github.com/kgoedecke/doop
- ⭐ 84 | 🍴 7 | 语言: TypeScript
- 标签: ai-agents, canvas, claude, claude-code, claude-design

### clipfactory
- 描述: Topic + template → short vertical video from your own B-roll: AI script, voice, scene plan, captions, FFmpeg render. Multi-persona, AI shot lists, AI B-roll, batch generation. Source-available (Elastic 2.0).
- 链接: https://github.com/feyzilim/clipfactory
- ⭐ 66 | 🍴 9 | 语言: Python
- 标签: content-creation, elevenlabs, fastapi, ffmpeg, openai

### netwalk
- 描述: Read-only network survey toolkit for AI coding agents: crawl a site from one device, diagnose it, draw it, and hand over a report — without ever changing a device or seeing a credential.
- 链接: https://github.com/ripmilla/netwalk
- ⭐ 60 | 🍴 19 | 语言: Python

### mediagen
- 描述: AI image and video generation skill for Claude Code and other coding agents — Gemini, OpenAI and Kie AI behind one CLI and MCP server, with EU AI Act content marking.
- 链接: https://github.com/Cripacx/mediagen
- ⭐ 53 | 🍴 0 | 语言: TypeScript
- 标签: agent-skill, ai-agents, claude, claude-code, cli

### neuromesh
- 描述: The Biomimetic Context Engine & Neural Runtime for AI Coding Assistants
- 链接: https://github.com/pinoox/neuromesh
- ⭐ 42 | 🍴 3 | 语言: Rust

### LiveStream-Agent-Studio
- 描述: 面向抖音直播电商的 Windows 本地 AI Agent Studio，贯通主播发现、直播洞察、直播复盘与短视频内容编导的统一智能工作流。
- 链接: https://github.com/HanyuanWang/LiveStream-Agent-Studio
- ⭐ 40 | 🍴 7 | 语言: Python
- 标签: ai-agent, douyin, livestream, speech-to-text

## 热门AI项目

## Machine Learning项目

### funNLP
- 

# funNLP 项目分析

## 1. 中文简介
funNLP 是一个全面的中英文自然语言处理资源仓库，涵盖敏感词检测、语言识别、实体抽取、情感分析、知识图谱构建及语音识别等多种NLP工具和资源。该项目整合了丰富的词库、预训练模型和开源数据集，为开发者提供一站式NLP开发支持。

## 2. 核心功能
- **敏感词与语言检测**：支持中英文敏感词过滤、语言识别及手机号/电话归属地查询
- **实体抽取与信息处理**：提供手机号、身份证、邮箱抽取及基于名字推断性别等功能
- **丰富词库资源**：包含中日文人名库、情感词库、停用词、反义词库、行业专业词库等
- **预训练模型与NLP工具**：整合BERT、GPT等模型，提供文本分类、摘要生成、关系抽取等任务工具
- **知识图谱与问答系统**：包含医疗、金融、法律等多领域知识图谱构建资源及智能问答方案

## 3. 适用场景
- 内容审核平台：用于文本安全检测和敏感词过滤
- 智能客服系统：提供对话理解、实体识别和问答能力
- 知识图谱构建：支持多领域实体抽取和关系挖掘
- 语音识别应用：提供ASR语料和语音处理工具

## 4. 技术亮点
- 汇聚了从基础工具到前沿模型的完整NLP资源链，涵盖传统方法到深度学习方案
- 整合了国内外主流预训练语言模型（BERT、ALBERT、RoBERTa等）及最新研究成果
- 提供多个高质量中文NLP数据集和基准测评任务，支持模型评估与对比
- 包含语音识别、文本生成、知识图谱等多模态NLP任务资源，适合多场景开发需求
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82618 | 🍴 15274 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36469 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。

### 2. 核心功能
- 支持多框架模型可视化，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等
- 提供交互式图形界面，可展开查看各层参数和维度信息
- 支持多种模型格式导入，兼容 safetensors、TensorFlow Lite、NumPy 等
- 可在浏览器或桌面端运行，无需安装复杂依赖

### 3. 适用场景
- 模型调试：快速定位网络结构中的异常层或参数问题
- 模型展示：向团队或客户直观呈现神经网络架构
- 格式转换验证：检查模型从一种框架转换到另一种格式后的结构一致性
- 教学演示：用于深度学习课程中讲解网络层结构

### 4. 技术亮点
- 跨平台支持，可在 Windows、macOS、Linux 及浏览器中运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 支持 safetensors 等新兴格式，紧跟技术发展趋势
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33389 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# GitHub项目分析：onnx

## 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开放标准，旨在实现机器学习模型的跨平台互操作性。它允许开发者在不同深度学习框架之间无缝迁移和部署模型，打破框架壁垒。

## 2. 核心功能
- 提供统一的模型交换格式，支持跨框架模型转换
- 兼容主流深度学习框架（PyTorch、TensorFlow、Keras、scikit-learn等）
- 实现模型从训练到推理的无缝转换与部署
- 提供丰富的算子库，覆盖常见神经网络结构
- 支持多种硬件平台（CPU、GPU、移动端）的高效推理

## 3. 适用场景
- 跨框架模型迁移（如将PyTorch训练好的模型转换为TensorFlow部署）
- 模型生产环境部署优化（通过ONNX Runtime加速推理）
- 移动端和边缘设备上的模型轻量化部署
- 模型性能分析与可视化工具开发

## 4. 技术亮点
- 由微软、Facebook等科技巨头联合推动，社区生态成熟
- ONNX Runtime提供高性能推理引擎，支持多硬件加速
- 开放标准，无厂商绑定，便于长期维护与扩展
- 链接: https://github.com/onnx/onnx
- ⭐ 21348 | 🍴 4006 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## 项目分析：ml-engineering

### 1. 中文简介
《机器学习工程开源手册》是一本专注于大规模机器学习系统构建与实践的开源参考书。内容涵盖从模型训练、调试到推理部署的全链路工程实践，面向生产级AI系统的开发需求。

### 2. 核心功能
- 提供大语言模型（LLM）训练与微调的工程实践指南
- 详解GPU集群调度与Slurm分布式训练的最佳实践
- 覆盖模型推理优化、网络通信与存储系统设计
- 包含PyTorch生态下的可扩展训练框架与MLOps工作流
- 提供生产环境中调试、监控与性能瓶颈排查的实用技巧

### 3. 适用场景
- 团队构建大规模分布式训练集群时的参考手册
- 工程师优化LLM推理延迟与吞吐量的实战指南
- MLOps平台搭建与模型生产化部署的流程规范
- 研究或工程团队学习GPU集群管理与资源调度

### 4. 技术亮点
- 聚焦生产级ML工程，填补学术与工业实践之间的知识空白
- 内容覆盖全栈ML工程链路：从底层硬件（GPU/网络/存储）到上层应用（训练/推理/调试）
- 针对大模型时代的关键挑战（可扩展性、调试、资源管理）提供系统性解决方案
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18690 | 🍴 1204 | 语言: Python
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
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36469 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和分析模型结构。

### 2. 核心功能
- 支持多框架模型可视化，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML 等
- 提供交互式图形界面，可展开查看各层参数和维度信息
- 支持多种模型格式导入，兼容 safetensors、TensorFlow Lite、NumPy 等
- 可在浏览器或桌面端运行，无需安装复杂依赖

### 3. 适用场景
- 模型调试：快速定位网络结构中的异常层或参数问题
- 模型展示：向团队或客户直观呈现神经网络架构
- 格式转换验证：检查模型从一种框架转换到另一种格式后的结构一致性
- 教学演示：用于深度学习课程中讲解网络层结构

### 4. 技术亮点
- 跨平台支持，可在 Windows、macOS、Linux 及浏览器中运行
- 开源免费，社区活跃，星标数超过 3.3 万
- 支持 safetensors 等新兴格式，紧跟技术发展趋势
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33389 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub项目分析：cheatsheets-ai

### 1. 中文简介
这是为深度学习和机器学习研究者精心整理的必备速查表集合，涵盖人工智能、深度学习框架、科学计算和数据处理等核心领域的实用参考指南。项目内容源自Medium技术博客，旨在帮助研究者快速查阅关键概念与代码片段。

### 2. 核心功能
- 提供深度学习与机器学习领域的核心公式、概念和API速查表
- 覆盖主流框架和工具（Keras、NumPy、SciPy、Matplotlib）的常用用法
- 以简洁直观的表格形式呈现，便于快速检索和记忆
- 汇集研究人员在实验中常用的最佳实践和代码模板
- 支持从基础工具到高级模型的完整技术栈参考

### 3. 适用场景
- 深度学习研究者在设计实验时快速查阅算法原理和参数配置
- 数据科学家在建模过程中参考NumPy/SciPy/Matplotlib的高效用法
- 机器学习初学者系统梳理知识体系，作为入门速查手册
- 工程师在Keras项目中快速查找层定义、优化器和回调函数用法

### 4. 技术亮点
- 覆盖标签包括AI、深度学习、Keras、机器学习、Matplotlib、NumPy、SciPy，技术栈全面
- 高星标数（15428）表明社区认可度高，内容实用性强
- 速查表形式适合快速查阅，提升研究与开发效率
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一份系统化的人工智能学习路线图，收录了近 200 个实战案例与项目，并免费提供配套教材，适合零基础入门与就业实战。内容涵盖 Python、数学基础、机器学习、深度学习、计算机视觉、自然语言处理等多个热门领域，覆盖 PyTorch、TensorFlow、Keras 等主流框架。

### 2. 核心功能
- 提供完整的人工智能学习路径规划，从零开始逐步进阶。
- 收录近 200 个实战案例和项目，帮助学习者积累项目经验。
- 免费提供配套教材与学习资料，降低入门门槛。
- 覆盖机器学习、深度学习、数据分析、NLP、CV 等主流方向。
- 支持 PyTorch、TensorFlow、Keras、Caffe 等多种深度学习框架。

### 3. 适用场景
- 零基础学习者系统入门人工智能与机器学习领域。
- 准备就业的开发者通过实战项目提升技能与简历竞争力。
- 数据科学从业者希望拓展深度学习、NLP、CV 等方向技能。
- 高校学生或自学者寻找结构化学习路线与参考资料。

### 4. 技术亮点
- 学习路径清晰，覆盖从数学基础到前沿领域的完整体系。
- 实战导向，近 200 个项目案例贴合工业界实际需求。
- 多框架支持，兼容 PyTorch、TensorFlow、Keras 等主流工具。
- 完全免费开放，配套教材丰富，适合长期自学参考。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13278 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型、神经网络及其他 AI 模型。它通过声明式配置简化了机器学习工作流程，使开发者无需编写大量代码即可快速训练和部署模型。

### 2. 核心功能
- 支持文本、数值、图像等多种数据类型的端到端机器学习流程
- 通过 YAML 声明式配置定义模型架构，大幅降低开发门槛
- 内置训练、评估、预测全流程，支持 GPU 加速
- 支持大语言模型（LLM）的微调、推理与部署
- 提供可视化的训练指标监控和模型分析工具

### 3. 适用场景
- 需要快速原型验证的机器学习项目
- 结构化数据（表格数据）的分类、回归任务
- 大语言模型（如 LLaMA、Mistral）的微调与定制
- 以数据为中心、希望减少代码量的数据科学团队

### 4. 技术亮点
- 声明式配置驱动，无需深入深度学习框架细节即可构建复杂模型
- 原生支持多模态数据混合训练，自动处理特征工程
- 内置可解释性功能，帮助分析模型决策依据
- 与 PyTorch 深度集成，同时提供简洁的 API 抽象层
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
- ⭐ 6430 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP是一个全面的中文自然语言处理（NLP）资源合集项目，涵盖了敏感词检测、个人信息抽取、词汇资源库、预训练模型及各类NLP工具。该项目整合了丰富的中文语料库、知识图谱资源和前沿算法实现，是中文NLP开发者和研究者的实用指南。

### 2. 核心功能
- **敏感词与信息抽取**：中英文敏感词检测、手机号/身份证/邮箱抽取、语言识别
- **词汇资源库**：同义词、反义词、否定词、停用词、情感值词库及繁简体转换
- **知识图谱与语料**：汇集中英文知识图谱、问答数据集、聊天语料及领域词库（医学/法律/汽车等）
- **预训练模型**：整合BERT、ALBERT、GPT2等主流模型的中文版本及训练代码
- **NLP工具链**：分词、命名实体识别、文本分类、摘要生成、问答系统等完整工具集

### 3. 适用场景
- **内容安全审核**：敏感词过滤、情感分析、谣言检测等互联网内容治理场景
- **智能问答与对话系统**：基于知识图谱的问答、聊天机器人开发
- **信息抽取与实体识别**：从文本中自动提取人名、地名、机构名等关键信息
- **NLP研究与教学**：提供丰富的数据集、基准任务和预训练模型参考资源

### 4. 技术亮点
- 整合了清华XLORE、百度、Facebook等多机构的预训练模型和开源资源
- 覆盖从传统NLP（分词、词性标注）到深度学习（BERT、GPT2）的全方位工具
- 提供医疗、法律、金融等专业领域的知识图谱和语料资源
- 包含数据增强、对抗训练等前沿NLP技术实践
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82618 | 🍴 15274 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100 多种模型。该项目论文已被 ACL 2024 收录，旨在为研究者和开发者提供便捷的一站式模型微调解决方案。

### 2. 核心功能
- 支持 100+ 主流大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、全参数微调等多种训练策略
- 集成 RLHF（强化学习人类反馈）对齐训练能力
- 支持量化技术（如 4bit/8bit 量化）降低显存占用
- 兼容 Transformers 生态，开箱即用

### 3. 适用场景
- **企业定制化**：基于开源模型微调垂直领域专用模型
- **学术研究**：快速复现和对比不同微调方法的效果
- **多模态应用**：训练支持图像理解的视觉语言模型
- **资源受限环境**：通过 QLoRA 和量化技术在消费级显卡上微调大模型

### 4. 技术亮点
- 统一接口支持众多模型架构，无需为每种模型编写独立代码
- 对 MoE（混合专家）模型和 DeepSeek 等新兴架构的良好支持
- 高效的数据处理和训练优化，显著提升微调效率
- 社区活跃，星标数超 7.4 万，生态完善
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74297 | 🍴 9092 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

---

### 1. 中文简介
这是一个为期12周、包含24节课程的AI入门课程项目，由微软推出，旨在面向所有人普及人工智能知识。课程内容涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域，采用Jupyter Notebook形式进行教学。

---

### 2. 核心功能
- **系统化课程体系**：12周24课时的结构化学习路径，循序渐进地讲解AI核心概念。
- **多领域覆盖**：涵盖机器学习、深度学习（CNN、RNN、GAN）、计算机视觉和自然语言处理等方向。
- **交互式学习**：全部课程以Jupyter Notebook形式呈现，支持代码实践与即时反馈。
- **微软官方背书**：由微软"Microsoft for Beginners"项目出品，内容质量有保障。
- **免费开放资源**：项目完全开源，任何人都可以免费学习和使用。

---

### 3. 适用场景
- **AI初学者系统学习**：适合零基础的编程爱好者或学生入门人工智能领域。
- **高校/培训机构课程补充**：可作为学校或培训机构的AI课程教材和实验材料。
- **企业内训参考**：适合团队内部进行AI基础知识培训和能力提升。
- **自学者课外拓展**：适合希望利用业余时间系统了解AI技术的职场人士。

---

### 4. 技术亮点
- **微软出品，社区活跃**：66,465颗星标证明其广泛认可度，是GitHub上最受欢迎的AI入门项目之一。
- **完整知识体系**：从基础机器学习到前沿的GAN、NLP，覆盖AI核心知识图谱。
- **实践导向**：每个课程均配有可运行的代码示例，便于边学边练。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66465 | 🍴 12850 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub 项目分析：ai-engineering-from-scratch

---

### 1. 中文简介

该项目旨在从零开始教授 AI 工程的核心知识——先深入学习理解，再动手构建实现，最终交付给他人使用。适合希望系统掌握 AI 技术的开发者和学习者。

---

### 2. 核心功能

- **从零构建 AI 系统**：涵盖从基础原理到完整工程实现的完整学习路径。
- **多领域覆盖**：包括 LLM、计算机视觉、NLP、强化学习、生成式 AI 等方向。
- **AI Agent 与 MCP 支持**：深入讲解智能体开发与模型上下文协议（MCP）的应用。
- **多语言实践**：使用 Python、Rust、TypeScript 进行跨语言工程实现。
- ** swarm 智能与 Transformer**：探索群体智能和 Transformer 架构的底层实现。

---

### 3. 适用场景

- **AI 初学者系统学习**：希望从零构建扎实 AI 工程基础的学习者。
- **AI 工程师技能提升**：需要深入理解 LLM、Agent 和生成式 AI 原理的开发者。
- **课程与培训参考**：作为 AI 工程课程的教材或自学路线图。
- **跨语言 AI 项目实践**：需要结合 Python、Rust、TypeScript 进行多语言开发的团队。

---

### 4. 技术亮点

- 项目星标数高达 **47,782**，说明社区认可度极高，是热门学习资源。
- 标签涵盖 **agents、MCP、swarm-intelligence、Rust** 等前沿方向，内容紧跟 AI 工程发展趋势。
- 强调 **"from-scratch"（从零实现）** 的教学理念，帮助学习者深入理解底层原理而非仅停留在调用 API。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47782 | 🍴 8419 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42475 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36469 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33840 | 🍴 4712 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29183 | 🍴 3561 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21851 | 🍴 3361 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17384 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析：500 AI机器学习项目集合

## 1. 中文简介

这是一个包含500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。项目以Python为主要实现语言，适合从入门到进阶的学习者参考实践。

## 2. 核心功能

- 提供500个完整的AI项目代码示例，覆盖主流算法和框架
- 按技术领域分类：机器学习、深度学习、计算机视觉、NLP
- 每个项目包含可运行的代码和详细说明文档
- 支持从零开始到高级应用的渐进式学习路径

## 3. 适用场景

- **AI初学者**：通过完整项目快速理解机器学习工作流程
- **学生/研究者**：作为课程作业或研究项目的参考实现
- **开发者**：寻找特定算法（如CNN、Transformer）的实用代码模板
- **企业培训**：搭建AI技术团队的内部分享资源库

## 4. 技术亮点

- 36,469颗星的高人气项目，社区验证质量可靠
- 标签体系完善（artificial-intelligence, computer-vision, nlp等），便于快速检索
- 涵盖经典项目（如MNIST分类、图像识别）到前沿应用（如GPT、目标检测）
- 全部使用Python实现，依赖主流库（TensorFlow/PyTorch/Scikit-learn）

---

**总结**：这是一个高质量的AI学习资源库，适合系统性地掌握机器学习到深度学习的完整技术栈，尤其适合需要大量实践项目的学习者。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36469 | 🍴 7458 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于 AI 的浏览器自动化框架，能够利用大语言模型智能地自动执行基于网页的工作流。它通过视觉理解和 AI 决策，让浏览器操作更加智能化和自适应。

### 2. 核心功能
- **AI 驱动自动化**：利用大语言模型理解网页内容并自主决策操作
- **多引擎支持**：兼容 Playwright、Puppeteer 和 Selenium 等主流浏览器自动化工具
- **视觉理解能力**：通过计算机视觉识别页面元素，无需依赖固定选择器
- **RPA 工作流**：支持录制和回放复杂的跨页面操作流程
- **API 集成**：提供 API 接口，便于与其他系统集成

### 3. 适用场景
- **重复性网页操作**：如批量表单填写、数据录入等日常办公自动化
- **跨平台数据采集**：从多个网站自动抓取和整理信息
- **企业 RPA 替代**：作为 Power Automate 等商业 RPA 工具的开源替代方案
- **测试自动化**：用于 Web 应用的端到端测试流程

### 4. 技术亮点
- 结合 LLM 与视觉模型，实现"看懂页面再操作"的智能自动化，而非传统的固定规则驱动
- 支持 Agent 模式，可自主处理页面异常和动态变化
- 开源免费，社区活跃（22837+ 星标），生态持续扩展
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22837 | 🍴 2143 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是领先的视觉AI高质量数据集构建平台，提供开源、云和企业级产品以及标注服务。支持图像、视频和3D标注，具备AI辅助标注、质量保证、团队协作、数据分析及开发者API等功能。

### 2. 核心功能
- **多模态标注支持**：支持图像、视频和3D数据的标注任务
- **AI辅助标注**：集成AI模型辅助自动标注，提升标注效率
- **团队协作**：支持多人协作标注及任务分配管理
- **质量保证**：内置质检机制确保标注数据质量
- **开发者API**：提供完善的API接口便于集成和扩展

### 3. 适用场景
- **目标检测数据集构建**：用于标注边界框数据，训练检测模型
- **语义分割任务**：支持像素级标注，适用于分割模型训练
- **视频行为分析**：对视频帧进行标注，适用于动作识别等场景
- **大规模团队标注项目**：适合需要多人协作标注的企业级项目

### 4. 技术亮点
- 支持多种深度学习框架（PyTorch、TensorFlow）
- 提供从开源到企业级的完整产品矩阵
- 内置图像分类、目标检测、语义分割等多种标注类型
- 社区活跃，星标数超过16,000，生态完善
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16576 | 🍴 3812 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12958 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
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
OpenClaw 是一款完全由用户自主掌控的个人AI助手，支持任意操作系统和平台运行。它以"龙虾方式"重新定义了AI助手的体验——强调数据所有权和隐私保护，让用户真正拥有自己的AI。

### 2. 核心功能
- **跨平台支持**：可在任意操作系统和平台上运行，打破平台限制
- **数据主权**：用户完全掌控自己的数据，无需依赖第三方云服务
- **本地化部署**：支持在本地环境中运行AI助手，保障隐私安全
- **个性化定制**：可根据用户需求进行深度定制和配置
- **开源免费**：项目完全开源，社区驱动开发

### 3. 适用场景
- **隐私敏感用户**：希望AI助手不将数据上传到云端的个人用户
- **开发者群体**：需要本地化AI工具进行开发辅助的技术人员
- **企业场景**：对数据安全有严格要求的企业内部助手部署
- **多平台用户**：需要在不同操作系统间无缝切换的跨平台用户

### 4. 技术亮点
- 基于 **TypeScript** 开发，类型安全且生态丰富
- 采用开源架构，社区活跃（38万+星标）
- 强调 **"Own Your Data"** 理念，契合当下隐私保护趋势
- 龙虾主题设计，具有独特的品牌识别度
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387225 | 🍴 81323 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

---

## 1. 中文简介

superpowers 是一个基于 AI 代理的技能框架与软件开发方法论，旨在通过子代理驱动开发流程，提升软件工程的效率与质量。该项目将 AI 能力与传统的软件开发生命周期（SDLC）相结合，提供了一套可落地的智能化开发解决方案。

---

## 2. 核心功能

- **子代理驱动开发（Subagent-Driven Development）**：通过多个 AI 子代理协同完成复杂开发任务
- **AI 技能框架（Agentic Skills Framework）**：提供可复用、可组合的 AI 技能模块
- **头脑风暴辅助（Brainstorming）**：利用 AI 辅助进行创意构思和技术方案讨论
- **完整 SDLC 覆盖**：支持从需求分析到部署的全软件开发生命周期
- **OBRA 方法论集成**：将结构化开发流程与 AI 能力深度融合

---

## 3. 适用场景

- **AI 辅助编程**：开发者使用 AI 代理加速代码编写、审查和调试
- **团队协作开发**：多个子代理分工协作，提升团队开发效率
- **技术方案设计**：利用 AI 进行架构设计和方案头脑风暴
- **自动化软件开发流程**：将传统 SDLC 流程智能化、自动化

---

## 4. 技术亮点

- 采用 **Shell 脚本** 实现，轻量级且易于集成到现有工作流中
- 以 **27.6 万+ 星标** 证明其在 AI 编程工具领域的广泛认可
- 标签涵盖 **ai、sdlc、skills、subagent-driven-development**，体现了框架化的设计理念
- 将"技能"概念引入 AI 代理开发，支持模块化复用和灵活组合
- 链接: https://github.com/obra/superpowers
- ⭐ 276532 | 🍴 24737 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

基于您提供的项目信息，以下是分析：

## 1. 中文简介
**hermes-agent** 是一款与用户共同成长的人工智能代理工具。它支持多种主流大语言模型（包括Claude、ChatGPT等），能够根据用户的需求和使用习惯不断优化和适应，提供个性化的智能辅助体验。

## 2. 核心功能
- **多模型支持**：兼容Anthropic Claude、OpenAI GPT系列、Codex等多种LLM后端
- **智能成长机制**：代理能够根据用户交互历史持续学习和优化响应策略
- **Python原生开发**：基于Python构建，易于扩展和集成到现有工作流
- **开源社区驱动**：由Nous Research等机构支持，拥有活跃的开发者社区

## 3. 适用场景
- **开发者辅助**：代码编写、调试和审查的智能助手
- **日常办公自动化**：邮件处理、日程管理、文档生成的代理工具
- **研究分析**：基于大语言模型的数据分析和信息整理
- **个性化AI助手**：需要长期记忆和上下文理解的用户级应用

## 4. 技术亮点
- **模型无关架构**：抽象层设计允许无缝切换不同LLM提供商
- **成长型代理模式**：区别于传统一次性对话，支持跨会话学习和用户偏好积累
- **高社区认可度**：23万+星标表明其在AI Agent领域的广泛影响力

---

**注意**：以上分析基于您提供的项目元数据信息。由于我无法访问外部GitHub仓库验证项目详情，建议访问官方仓库获取最新、最准确的技术文档和代码实现。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 234719 | 🍴 47260 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码许可的工作流自动化平台，内置原生 AI 能力。它支持可视化拖拽构建与自定义代码相结合，可自托管或云端部署，并提供 400+ 种集成。

### 2. 核心功能
- 可视化工作流编辑器，通过拖拽节点快速构建自动化流程
- 内置 AI 能力，支持智能任务处理与决策
- 提供 400+ 种预置集成，覆盖主流 API 和服务
- 支持自托管和云端部署两种模式，数据自主可控
- 允许自定义代码扩展，灵活满足个性化需求

### 3. 适用场景
- 企业级 API 集成与数据同步，替代传统 iPaaS 方案
- 自动化营销流程，如邮件发送、社交媒体发布等
- AI 驱动的任务自动化，如文档处理、智能客服
- 个人开发者搭建私有自动化工具，无需依赖第三方云服务

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态友好
- 支持 MCP（Model Context Protocol）客户端与服务端，可与大模型深度集成
- 公平代码许可证（Fair-code），在开放共享与商业保护之间取得平衡
- 丰富的节点系统和可扩展架构，社区活跃
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202081 | 🍴 60324 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI，实现普及化人工智能愿景。我们的使命是提供强大的工具，让你能够专注于真正重要的事物。

## 2. 核心功能
- 支持自主执行多步骤任务，无需人工逐一步骤干预
- 可连接多种大语言模型（GPT、Claude、Llama 等）
- 具备网络浏览、文件操作、代码执行等工具能力
- 支持任务分解与自主决策，实现目标导向的自动化流程
- 开源可定制，用户可基于框架二次开发

## 3. 适用场景
- 自动化重复性工作流程（如数据收集、报告生成）
- 复杂多步任务编排与执行
- AI 应用原型快速开发与验证
- 个人助手类自动化场景

## 4. 技术亮点
- 支持主流大语言模型 API 灵活切换，兼容 OpenAI、Anthropic、Llama 等
- 开源生态活跃，社区贡献丰富
- 模块化架构便于扩展自定义工具与功能
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186810 | 🍴 46051 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 171229 | 🍴 9499 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167802 | 🍴 21655 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164622 | 🍴 30549 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157973 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153582 | 🍴 9915 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

