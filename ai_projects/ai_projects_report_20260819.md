# GitHub AI项目每日发现报告
日期: 2026-08-19

## 新发布的AI项目

### sprix-sage-router
- 

## Sprix Sage Router 项目分析

### 1. 中文简介
Sprix AI（屿智同行）开发的A2A智能体网络路由系统，支持状态感知的SELF/COLLABORATE/HANDOFF三种路由模式，用于智能体间的任务调度与协作编排。

### 2. 核心功能
- 支持状态感知的智能体路由决策
- 提供SELF（自主处理）、COLLABORATE（协作处理）、HANDOFF（移交处理）三种路由模式
- 实现多智能体系统间的任务调度与编排
- 基于A2A协议进行智能体间通信

### 3. 适用场景
- 多智能体系统（MAS）中的任务分发与协调
- AI智能体网络的自动化路由与负载均衡
- 复杂任务分解与多智能体协作场景
- 企业级智能体编排平台

### 4. 技术亮点
- 状态感知的智能路由算法，可根据当前状态动态选择最优路由策略
- 支持三种灵活的路由模式，适应不同任务复杂度与协作需求
- 基于A2A标准协议，实现智能体间的标准化通信与任务移交
- 轻量级Python实现，易于集成到现有AI系统中
- 链接: https://github.com/wang2122/sprix-sage-router
- ⭐ 350 | 🍴 9 | 语言: Python
- 标签: a2a, agent-orchestration, agent-routing, ai-agents, multi-agent-systems

### crucible
- 

## Crucible 项目分析

### 1. 中文简介

Crucible 是一个由 AI 驱动的漏洞自动验证平台，用户只需提交代码仓库和漏洞描述，系统即可在隔离的沙箱环境中进行白盒代码审计，自动搭建靶场复现漏洞，并最终生成中文分析报告。

### 2. 核心功能

- **AI 驱动自动化审计**：利用 AI Agent 对代码仓库进行智能白盒分析
- **隔离沙箱执行**：在 Docker 容器中安全运行，确保审计过程与宿主机完全隔离
- **靶场自动搭建与复现**：根据漏洞描述自动构建运行环境并复现漏洞
- **中文报告生成**：自动生成结构化的中文漏洞验证报告
- **FastAPI 接口服务**：提供现代化的 API 接口，便于集成与调用

### 3. 适用场景

- **安全研究员**：快速验证 CVE 漏洞在特定代码库中的可利用性
- **企业安全团队**：对内部代码仓库进行批量漏洞审计与风险评估
- **CTF 选手/学习者**：自动化复现漏洞以加深对漏洞原理的理解
- **代码审计服务**：作为自动化初审工具，辅助人工审计提高效率

### 4. 技术亮点

- 采用 **AI Agent + Docker 沙箱** 的组合架构，实现安全隔离与智能分析的平衡
- 基于 **FastAPI** 构建，具备高性能异步处理能力，适合大规模并发审计任务
- 标签中包含 **reac**（推测为 React 前端），说明项目具备可视化交互界面，用户体验较好
- 全流程自动化：从代码提交到报告输出无需人工干预，显著提升审计效率
- 链接: https://github.com/pgnzbl-ux/crucible
- ⭐ 168 | 🍴 0 | 语言: Python
- 标签: ai-agents, code-au, docker, fastapi, python

### ai_agents_event
- 描述: 无描述
- 链接: https://github.com/LIDR-academy/ai_agents_event
- ⭐ 33 | 🍴 72 | 语言: Python

### tiance-tweet-card-generator
- 

# tiance-tweet-card-generator 项目分析

## 1. 中文简介
这是一个开源的推文卡片与抖音图文生成器，支持AI素材生成、自由改写、背景海报制作以及PNG格式导出，帮助用户快速创建社交媒体内容。

## 2. 核心功能
- 一键生成推文卡片，支持自定义内容与样式
- AI素材生成，可智能改写文案内容
- 提供多种背景海报模板，丰富视觉呈现
- 支持PNG格式导出，方便分享与发布
- 基于React + Vite构建，界面响应迅速

## 3. 适用场景
- 社交媒体运营：快速制作抖音图文内容
- 自媒体创作：生成吸引眼球的推文卡片
- 营销推广：AI辅助改写文案，提升传播效果
- 内容创作者：高效输出视觉化图文素材

## 4. 技术亮点
- 采用React + Vite技术栈，开发体验流畅
- 集成AI能力，实现智能素材生成与文案改写
- 轻量级开源项目，易于二次开发与定制
- 链接: https://github.com/Leobai03/tiance-tweet-card-generator
- ⭐ 28 | 🍴 5 | 语言: JavaScript
- 标签: ai-content, douyin, image-generator, react, vite

### Yuntu
- 

## Yuntu 项目分析

### 1. 中文简介
Yuntu 是一款AI驱动的旅行规划引擎，具备确定性路线调度、经核实兴趣点（POI）以及基于事实的大语言模型内容生成能力。该项目专注于为旅行者提供精准、可靠的行程规划服务，同时确保生成内容的准确性与可验证性。

### 2. 核心功能
- AI智能路线规划与确定性行程调度
- 经过验证的POI（兴趣点）数据库管理
- 基于事实的LLM内容生成，避免虚假信息
- 前后端分离架构，支持React交互界面
- 使用FastAPI构建高性能API服务

### 3. 适用场景
- 个人用户快速生成个性化旅行行程
- 旅行社或OTA平台集成智能规划能力
- 需要高准确性POI信息的旅游应用开发
- 旅行规划类SaaS产品的底层引擎

### 4. 技术亮点
- 采用"确定性调度+LLM生成"混合架构，兼顾准确性与灵活性
- PostgreSQL存储结构化旅行数据，支持复杂路线查询
- 通过事实核查机制减少LLM幻觉问题
- 技术栈现代，前后端分离便于扩展与维护
- 链接: https://github.com/Trunks820/Yuntu
- ⭐ 24 | 🍴 1 | 语言: Python
- 标签: ai-travel, fastapi, llm, llms, postgresql

### free-multimodal-proxy
- 描述: OpenAI-compatible reverse proxy for free multimodal AI APIs (chat / images / videos / audio / 3d)
- 链接: https://github.com/b3b41020/free-multimodal-proxy
- ⭐ 21 | 🍴 17 | 语言: Python
- 标签: docker, fastapi, free-api, image-generation, multimodal

### marvel-rivals-aimbot-free
- 描述: External aimbot for Marvel Rivals with smooth aim assist, FOV circle, and triggerbot. Undetected by anti-cheat with regular updates.
- 链接: https://github.com/rapiddisposi/marvel-rivals-aimbot-free
- ⭐ 21 | 🍴 0 | 语言: 未知
- 标签: marvel-rivals-2025, marvel-rivals-aim, marvel-rivals-aim-assist, marvel-rivals-aim-bot, marvel-rivals-aimbot

### ethereum-airdrop-bot-free
- 描述: Claim unclaimed Ethereum and ERC-20 token airdrops automatically. Checks your wallet against all major airdrop databases and claims in one click.
- 链接: https://github.com/farspectrum/ethereum-airdrop-bot-free
- ⭐ 21 | 🍴 0 | 语言: 未知
- 标签: airdrop-eth-2025, airdrop-ethereum-free, erc20-airdrop, eth-airdrop-bot, eth-airdrop-bot-free

### base-chain-airdrop-bot
- 描述: Farm the upcoming Base ecosystem airdrop. Auto-bridges ETH to Base, swaps on Aerodrome, provides liquidity, and mints NFTs to maximize eligibility.
- 链接: https://github.com/internaljump/base-chain-airdrop-bot
- ⭐ 21 | 🍴 0 | 语言: 未知
- 标签: aerodrome-farming, base-airdrop-2025, base-airdrop-bot, base-airdrop-farming, base-airdrop-free

### grok-ai-free-premium-bypass
- 描述: Access Grok 3 and SuperGrok features without X Premium subscription. Full Grok AI with image generation and Think mode for free.
- 链接: https://github.com/quizzicalpa/grok-ai-free-premium-bypass
- ⭐ 21 | 🍴 0 | 语言: 未知
- 标签: grok-3-bypass, grok-3-free, grok-ai-2025, grok-ai-bypass, grok-ai-free

## 热门AI项目

## Machine Learning项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介
funNLP 是一个全面的中英文自然语言处理（NLP）工具资源集合仓库，涵盖了从基础分词、命名实体识别到高级知识图谱构建的完整NLP工具链。该项目整合了数十种预训练语言模型（BERT、ALBERT、RoBERTa等）、多领域词库语料、语音识别资源以及知识图谱构建工具，为中文NLP研究和应用提供了丰富的开源资源。

### 2. 核心功能
- **基础NLP工具**：提供分词、词性标注、命名实体识别（NER）、情感分析、文本分类等核心功能，支持jieba、HanLP等主流工具
- **多语言资源库**：包含中日韩文人名库、成语词典、地名词库、医学/法律/汽车等专业领域词库，以及62种语言的词对集
- **预训练模型集合**：整合BERT、ALBERT、RoBERTa、ELECTREA等中英文预训练语言模型，支持知识图谱构建和问答系统
- **语音与OCR资源**：提供ASR语音识别数据集、中文OCR工具（cnocr）、语音情感分析、笑声检测等音频处理资源
- **数据增强与评测**：包含中文NLP数据增强工具（EDA）、语言理解测评基准、各类NLP数据集搜索和排行榜

### 3. 适用场景
- **学术研究**：NLP研究人员可快速获取中文预训练模型、基准数据集和评测工具，加速知识图谱、问答系统等研究
- **企业应用开发**：开发者可利用现成的敏感词检测、姓名推断、运营商查询等工具，快速构建智能客服、内容审核系统
- **数据标注与挖掘**：提供brat标注工具、doccano协同标注平台，支持知识图谱三元组抽取、实体关系挖掘等任务
- **语音与多模态应用**：整合ASR数据集和语音识别资源，适用于语音助手、智能翻译等多模态NLP场景

### 4. 技术亮点
- **资源全面性**：整合82538星标，涵盖从基础工具到前沿模型的完整NLP工具链，包括清华XLORE跨语言知识图谱等高质量资源
- **多模型支持**：同时支持TensorFlow、PyTorch、Keras等主流框架，提供BERT-NER、GPT2文本生成等多种实现方案
- **领域专业化**：针对医学、法律、金融、汽车等专业领域提供专用词库和语料，支持垂直领域的NLP应用开发
- **开源生态**：汇集百度、腾讯、Facebook等机构开源资源，如LAMA语言模型分析、CoVoST多语种翻译语料库等
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82538 | 🍴 15266 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，为学习者提供丰富的实践资源。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 包含从基础到进阶的多样化项目示例
- 适合不同水平的学习者参考实践

### 3. 适用场景
- AI初学者系统学习各领域的实践项目
- 开发者寻找项目灵感或参考实现
- 教师用于教学演示和学生练习
- 研究人员快速了解领域内典型应用场景

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，是AI领域的"awesome list"式资源库
- 所有项目均附带可运行的代码，便于动手实践
- 按领域分类清晰，包含Python等主流语言实现
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36375 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具，能够以图形化方式展示模型结构与参数。它支持多种主流框架和模型格式，帮助用户直观理解和分析模型架构。

### 2. 核心功能
- 支持多种深度学习框架模型可视化，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML、TensorFlow Lite 等
- 提供模型架构图的交互式展示，可逐层查看网络结构细节
- 支持 safetensors、Numpy 等常见模型格式
- 兼容 AI、ML 等多种机器学习模型格式

### 3. 适用场景
- 模型调试与结构审查：帮助开发者直观检查神经网络层结构是否正确
- 模型迁移与格式转换：验证不同框架间模型转换后的结构一致性
- 教学与演示：用于深度学习课程中讲解模型架构
- 模型分享与文档：生成可视化的模型结构图用于技术文档或报告

### 4. 技术亮点
- 支持 33,000+ 星标，拥有广泛的用户基础和社区认可
- 跨平台兼容，支持多种主流 AI 框架格式
- 基于 JavaScript 开发，可轻松集成到 Web 环境中使用
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33366 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21326 | 🍴 4001 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub 项目分析：ml-engineering

## 1. 中文简介

《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的知识库，涵盖从模型训练、调试到推理部署的完整流程。项目以开源形式呈现，旨在为 AI 工程师和研究者提供系统化的技术指导。

## 2. 核心功能

- 提供大规模语言模型（LLM）训练与推理的工程实践指南
- 深入讲解 GPU 使用、网络通信和存储优化等底层技术
- 涵盖 PyTorch 框架下的模型调试与可扩展性设计
- 包含 Slurm 集群管理和 MLOps 工作流的最佳实践

## 3. 适用场景

- 分布式大模型训练基础设施搭建与优化
- LLM 推理服务部署与性能调优
- 机器学习系统的故障排查与调试
- MLOps 平台建设与工程化落地

## 4. 技术亮点

- 聚焦生产级 ML 工程实践，而非理论算法
- 覆盖从底层硬件（GPU/网络/存储）到上层框架（PyTorch/Transformers）的全栈技术
- 开源开放，内容持续更新，社区活跃度高（18,655+ 星标）
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18655 | 🍴 1201 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17362 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13268 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11627 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10686 | 🍴 5699 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，为学习者提供丰富的实践资源。

### 2. 核心功能
- 提供500个AI相关项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 包含从基础到进阶的多样化项目示例
- 适合不同水平的学习者参考实践

### 3. 适用场景
- AI初学者系统学习各领域的实践项目
- 开发者寻找项目灵感或参考实现
- 教师用于教学演示和学生练习
- 研究人员快速了解领域内典型应用场景

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，是AI领域的"awesome list"式资源库
- 所有项目均附带可运行的代码，便于动手实践
- 按领域分类清晰，包含Python等主流语言实现
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36375 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具，能够以图形化方式展示模型结构与参数。它支持多种主流框架和模型格式，帮助用户直观理解和分析模型架构。

### 2. 核心功能
- 支持多种深度学习框架模型可视化，包括 TensorFlow、PyTorch、Keras、ONNX、CoreML、TensorFlow Lite 等
- 提供模型架构图的交互式展示，可逐层查看网络结构细节
- 支持 safetensors、Numpy 等常见模型格式
- 兼容 AI、ML 等多种机器学习模型格式

### 3. 适用场景
- 模型调试与结构审查：帮助开发者直观检查神经网络层结构是否正确
- 模型迁移与格式转换：验证不同框架间模型转换后的结构一致性
- 教学与演示：用于深度学习课程中讲解模型架构
- 模型分享与文档：生成可视化的模型结构图用于技术文档或报告

### 4. 技术亮点
- 支持 33,000+ 星标，拥有广泛的用户基础和社区认可
- 跨平台兼容，支持多种主流 AI 框架格式
- 基于 JavaScript 开发，可轻松集成到 Web 环境中使用
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33366 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图项目，整理了近200个实战案例与项目，并免费提供配套教材。项目覆盖从零基础入门到就业实战的完整学习路径，涵盖Python、机器学习、深度学习、数据分析、计算机视觉、自然语言处理等热门技术领域。

### 2. 核心功能
- 提供系统化AI学习路线图，帮助学习者规划学习路径
- 收录近200个实战案例与项目，配套免费教材资源
- 覆盖Python、数学基础、机器学习、深度学习等核心技术栈
- 包含计算机视觉(CV)、自然语言处理(NLP)等热门领域专项内容
- 支持多种主流框架学习：PyTorch、TensorFlow、Keras、Caffe等

### 3. 适用场景
- 零基础初学者系统学习人工智能与机器学习
- 数据分析从业者提升技能、准备就业面试
- 学生或转行者希望通过实战项目积累工作经验
- 需要参考资料的学习者快速查阅算法与框架知识

### 4. 技术亮点
- 项目星标数达13268，社区认可度高
- 知识体系完整，涵盖从数学基础到前沿领域的全部核心内容
- 实战导向，提供丰富的代码案例与配套教材
- 标签覆盖全面，包含主流框架与热门技术关键词，便于检索学习
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13268 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型、神经网络及其他 AI 模型。它通过声明式配置简化了机器学习模型的训练与部署流程，让开发者无需编写大量代码即可完成模型构建。

## 2. 核心功能
- 支持低代码/声明式方式构建神经网络和 LLM 模型
- 提供预训练模型微调（fine-tuning）能力
- 兼容多种深度学习框架（如 PyTorch）
- 支持计算机视觉、自然语言处理等多种任务类型
- 内置数据-centric 工作流，便于数据驱动模型迭代

## 3. 适用场景
- 快速原型开发：无需深入编码即可构建和测试 AI 模型
- 模型微调：对 LLaMA、Mistral 等开源 LLM 进行领域适配
- 多模态应用：同时处理文本和图像数据的项目
- 数据驱动实验：通过声明式配置快速迭代模型结构

## 4. 技术亮点
- 低代码设计大幅降低 AI 开发门槛
- 支持主流开源 LLM（LLaMA、Mistral 等）的微调
- 标签涵盖 computer-vision、NLP、deep-learning 等，表明其多领域通用性
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9175 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8965 | 🍴 3110 | 语言: C++
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
- ⭐ 6413 | 🍴 778 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 

## funNLP 项目分析

### 1. 中文简介

funNLP是一个全面的中英文自然语言处理（NLP）资源集合项目，涵盖敏感词检测、实体抽取、词向量、知识图谱、语音识别、文本生成等多个方向。项目汇集了丰富的中文NLP数据集、预训练模型、工具库及相关论文教程，是中文NLP领域的重要资源库。

### 2. 核心功能

- **文本处理工具**：敏感词检测、繁简体转换、分词、情感分析、文本纠错、可读性评价等
- **实体与信息抽取**：手机号/身份证/邮箱抽取、命名实体识别（NER）、关系抽取、关键词提取
- **知识图谱与问答**：中英文知识图谱构建、医疗/金融领域图谱、基于知识图谱的问答系统
- **预训练模型与词向量**：BERT、ALBERT、GPT2等中文预训练模型，多种中文词向量资源
- **语音与对话**：中文语音识别（ASR）、语音情感分析、闲聊机器人、对话系统

### 3. 适用场景

- **中文NLP开发者**：快速查找分词、NER、情感分析等常用工具和数据集
- **企业与研究机构**：获取医疗、金融、法律等垂直领域的NLP资源与语料
- **NLP学习者**：通过项目中的论文、教程、数据集和代码示例系统学习
- **知识图谱构建者**：参考三元组抽取、实体链接、图谱问答等完整方案

### 4. 技术亮点

- **资源全面且更新及时**：涵盖从传统NLP到深度学习（BERT、GPT2）的完整技术栈
- **专注中文场景**：大量中文专属资源（如中文词向量、中文OCR、中文对话语料）
- **开源生态丰富**：汇集jieba、SpaCy、Transformers等主流框架的中文适配版本
- **附带基准评测**：提供中文NLP数据集评测基准、排行榜及TOP方案复盘
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82538 | 🍴 15266 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100 多种模型的微调训练，相关研究已发表于 ACL 2024。

### 2. 核心功能
- 支持 100+ 种主流 LLM 和 VLM 的统一微调训练
- 提供 LoRA、QLoRA、全参数微调等多种微调策略
- 支持 RLHF（基于人类反馈的强化学习）对齐训练
- 兼容 transformers 和 PEFT 生态，便于集成现有工作流
- 支持量化训练（如 4-bit/8-bit 量化），降低显存需求

### 3. 适用场景
- 研究人员和开发者快速微调 Llama、Qwen、DeepSeek、Gemma 等开源模型
- 资源受限环境下进行大模型高效微调（QLoRA 方案）
- 需要多模型统一训练流程的团队协作项目
- 对模型进行指令微调（Instruction Tuning）或对齐优化

### 4. 技术亮点
- **统一框架**：一个项目覆盖 100+ 模型，无需为不同模型维护独立代码
- **极致效率**：支持 QLoRA 等低资源微调方案，单卡即可训练大模型
- **前沿研究**：ACL 2024 论文背书，技术路线经过学术验证
- **生态友好**：深度集成 Hugging Face transformers 和 PEFT，兼容主流工具链
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74222 | 🍴 9078 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，历时12周、共24课时，旨在让所有人都能轻松学习人工智能。课程通过Jupyter Notebook形式呈现，内容覆盖机器学习和深度学习的核心概念与实践。

### 2. 核心功能
- 提供系统化的AI学习路径，分12周循序渐进地讲解核心知识
- 涵盖机器学习、深度学习、计算机视觉、NLP等多个AI领域
- 包含CNN、RNN、GAN等主流深度学习模型的实践课程
- 所有课程以Jupyter Notebook形式交付，支持交互式学习
- 完全免费开放，适合零基础学习者入门

### 3. 适用场景
- 高校或培训机构用于AI通识课程教学
- 自学者系统入门人工智能领域
- 企业内部分享AI基础知识培训
- 教育工作者快速搭建AI课程大纲

### 4. 技术亮点
- 由微软官方维护，内容质量有保障
- 社区活跃，星标数超6.5万，说明受众广泛认可
- 课程结构清晰，12周24课的节奏设计合理，便于学习者规划进度
- 标签覆盖全面，从基础ML到前沿DL均有涉及，学习路径完整
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65554 | 🍴 12712 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# GitHub项目分析：ai-engineering-from-scratch

---

## 1. 中文简介

本项目是一套从零开始学习AI工程的完整课程，涵盖从理论到实践再到产品交付的全流程。学习者将亲手构建AI系统，并最终能够将其部署并交付给他人使用。

---

## 2. 核心功能

- **从零构建AI系统**：深入理解AI底层原理，不依赖高级封装框架。
- **多领域覆盖**：涵盖LLM、计算机视觉、NLP、强化学习、生成式AI等核心方向。
- **AI智能体与 swarm 智能**：学习构建多智能体系统和群体智能应用。
- **MCP协议支持**：集成Model Context Protocol，实现AI工具的标准化连接。
- **多语言技术栈**：结合Python、Rust、TypeScript，兼顾易读性与高性能。

---

## 3. 适用场景

- **AI初学者**：希望系统性地从零掌握AI工程能力的学习者。
- **开发者进阶**：已有基础、希望深入理解Transformer、RL等底层原理的工程师。
- **AI产品构建者**：目标是将AI能力产品化并交付给终端用户的技术团队。
- **研究者与教师**：需要完整课程结构进行教学或科研参考的人员。

---

## 4. 技术亮点

- **跨语言融合**：Python用于快速原型，Rust用于性能敏感模块，TypeScript用于前端交互。
- **前沿技术覆盖**：涵盖MCP、Swarm Intelligence、Transformers等2024-2025年热门方向。
- **项目驱动学习**：每个模块均配有可运行的实战项目，强调"学以致用"。
- **高社区认可度**：近4.7万星标，说明项目质量和实用性广受开发者认可。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47146 | 🍴 8278 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：AiLearning

### 1. 中文简介
AiLearning 是一个涵盖数据分析与机器学习实战的综合性学习项目，内容涉及线性代数基础、PyTorch 深度学习框架以及 TensorFlow 2.x 实践，同时包含 NLTK 自然语言处理相关内容。该项目适合希望系统学习机器学习与深度学习的开发者。

### 2. 核心功能
- 提供机器学习经典算法的实战实现，包括 SVM、KMeans、朴素贝叶斯、逻辑回归等。
- 包含深度学习模型训练与调优，涵盖 DNN、RNN、LSTM 等网络结构。
- 集成 NLTK 库进行自然语言处理（NLP）相关任务。
- 涵盖推荐系统、聚类算法（Apriori、FP-Growth）等实用场景。
- 提供线性代数等数学基础知识的讲解与代码实践。

### 3. 适用场景
- 机器学习入门学习，适合从零开始系统掌握算法原理与代码实现。
- 深度学习实践，适合希望使用 PyTorch 和 TensorFlow 2.x 构建模型的学习者。
- NLP 项目参考，适合需要自然语言处理基础知识和工具的开发人员。
- 推荐系统开发，适合希望了解协同过滤、FP-Growth 等算法的工程师。

### 4. 技术亮点
- 涵盖从传统机器学习到深度学习的完整技术栈，适合体系化学习。
- 结合 Scikit-learn 与 PyTorch/TensorFlow 两大主流框架，理论与实践并重。
- 包含大量算法实战代码，便于直接参考和二次开发。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42464 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36375 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33830 | 🍴 4710 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29108 | 🍴 3543 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21842 | 🍴 3355 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17362 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub 项目分析

### 1. 中文简介

这是一个收录了 500 个 AI 项目的代码集合仓库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。该项目为开发者提供了丰富的实战案例和代码参考，适合不同层次的学习者和从业者。

### 2. 核心功能

- **项目集合**：收录 500 个 AI/ML/DL 相关项目，覆盖多个技术方向
- **代码参考**：每个项目附带完整代码，可直接学习和运行
- **多领域覆盖**：包含机器学习、深度学习、计算机视觉、NLP 四大板块
- **标签分类**：通过标签系统便于快速检索和筛选项目
- **开源共享**：所有项目均为开源代码，可自由学习和二次开发

### 3. 适用场景

- **学习者入门**：适合初学者系统学习 AI 各领域的实战项目
- **开发者参考**：为从业者提供可复用的代码模板和解决方案
- **项目选型**：帮助团队快速找到符合需求的 AI 项目案例
- **技术调研**：用于了解当前 AI 领域的项目分布和技术趋势

### 4. 技术亮点

- **高人气项目**：36375 星标，是 GitHub 上最受欢迎的 AI 项目集合之一
- **全面覆盖**：从传统机器学习到前沿深度学习，技术栈完整
- **标签体系完善**：使用多个标签分类，便于精准查找
- **Python 生态**：主要使用 Python 语言，契合 AI 开发主流工具链
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36375 | 🍴 7444 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介

Skyvern 是一个基于人工智能的浏览器自动化框架，能够利用大语言模型（LLM）和计算机视觉技术自动执行基于网页的工作流。它通过理解网页内容和结构，智能地完成复杂的浏览器操作任务，无需人工干预。

## 2. 核心功能

- **AI驱动网页理解**：利用大语言模型和视觉能力解析网页内容，智能识别页面元素和操作目标。
- **自动化浏览器操作**：支持自动完成表单填写、点击、导航等浏览器操作，模拟人类行为。
- **工作流编排**：提供API接口，可将浏览器自动化流程集成到现有系统中。
- **无头/有头模式**：支持有界面和无界面两种运行模式，适应不同场景需求。
- **多浏览器兼容**：基于Playwright等主流自动化工具，兼容多种浏览器环境。

## 3. 适用场景

- **RPA流程自动化**：替代人工执行重复性网页操作，如数据录入、报表生成等。
- **网页数据采集**：自动抓取需要登录或复杂交互才能访问的动态网页数据。
- **跨系统数据同步**：在多个Web系统之间自动传输和同步数据。
- **自动化测试**：对Web应用进行端到端的自动化功能测试。

## 4. 技术亮点

- **LLM + 计算机视觉融合**：结合大语言模型的语义理解能力和视觉识别能力，实现对复杂网页的智能操作。
- **API优先设计**：以API为核心架构，便于与企业现有系统无缝集成。
- **低代码/无代码友好**：通过自然语言描述即可驱动自动化流程，降低使用门槛。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22786 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，专为视觉AI应用而设计。它提供开源、云部署和企业级产品，以及专业标注服务，支持图像、视频和3D数据的标注，具备AI辅助标注、质量保证、团队协作、数据分析和开发者API等核心能力。

### 2. 核心功能
- **AI辅助标注**：利用预训练模型自动标注，大幅提升标注效率
- **多模态支持**：同时支持图像、视频和3D点云数据标注
- **团队协作**：内置任务分配、审核流程和质量保证机制
- **开发者API**：提供REST API，便于与现有工作流集成
- **数据分析**：内置标注统计和可视化分析工具

### 3. 适用场景
- 构建目标检测（如YOLO、Faster R-CNN）训练数据集
- 语义分割任务的数据标注（如DeepLab、Mask R-CNN）
- 视频动作识别或目标追踪的数据准备
- 图像分类与图像标注的批量处理需求

### 4. 技术亮点
- 完全开源，社区活跃（16546+星标），支持PyTorch和TensorFlow框架
- 提供边界框、多边形、关键点等多种标注类型
- 支持ImageNet等主流数据集格式导入导出
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16546 | 🍴 3803 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## GitHub项目分析：pytorch-grad-cam

### 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN和Vision Transformer等多种架构。可用于分类、目标检测、分割、图像相似度等多种任务的可视化解释。

### 2. 核心功能
- 支持Grad-CAM、Score-CAM等多种类激活图生成方法
- 兼容CNN和Vision Transformer等主流网络架构
- 支持图像分类、目标检测、图像分割等多种任务类型
- 提供图像相似度分析功能
- 生成直观的可视化热力图，展示模型关注区域

### 3. 适用场景
- **图像分类模型调试**：可视化模型决策依据，定位关键识别区域
- **医学影像分析**：解释AI诊断结果，辅助医生理解病灶位置
- **自动驾驶感知系统**：分析目标检测模型的注意力分布
- **模型可解释性研究**：探索深度学习模型的内部决策机制

### 4. 技术亮点
- 在PyTorch框架下实现，API设计简洁易用
- 支持最新的Vision Transformer架构，紧跟技术前沿
- 统一接口兼容多种可视化方法，便于对比实验
- 社区认可度高（12954星标），文档完善，维护活跃
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## kornia 项目分析

### 1. 中文简介
kornia 是一个面向空间 AI 的几何计算机视觉库，为 PyTorch 用户提供可微分的图像处理与几何计算功能，帮助开发者在深度学习框架内直接处理空间视觉任务。

### 2. 核心功能
- 提供可微分的图像变换、几何校正和相机标定算子
- 支持 2D/3D 空间变换、透视变换和仿射变换的端到端训练
- 集成常见计算机视觉算法（SIFT、特征匹配、立体视觉等）
- 与 PyTorch 原生张量无缝兼容，可直接在神经网络中调用
- 提供机器人视觉、SLAM 和自动驾驶相关的空间计算工具

### 3. 适用场景
- 深度学习中的图像增强与数据增强流水线
- 机器人视觉定位与地图构建（SLAM）
- 自动驾驶中的车道检测与空间理解
- 3D 重建与多视图几何研究

### 4. 技术亮点
- 全库算子均为可微分设计，支持反向传播优化
- 原生 PyTorch 实现，无需额外依赖即可集成到现有模型
- 针对 GPU 加速优化，适合大规模并行计算
- 开源活跃，社区贡献者众多，持续更新维护
- 链接: https://github.com/kornia/kornia
- ⭐ 11315 | 🍴 1225 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3480 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3382 | 🍴 413 | 语言: Python
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

OpenClaw 是一款个人 AI 助手工具，支持任意操作系统和平台，让你以"龙虾方式"真正拥有自己的数据。它是一个开源的、跨平台的个人 AI 助手解决方案。

## 2. 核心功能

- **跨平台支持**：兼容任意操作系统和平台，灵活部署
- **数据自主可控**：强调"own your data"理念，用户数据完全由自己掌控
- **个人 AI 助手**：提供专属的 AI 助手功能，满足个性化需求
- **开源项目**：基于 TypeScript 开发，社区活跃（38万+星标）
- **本地化运行**：支持在用户自己的设备上运行 AI 服务

## 3. 适用场景

- **个人数据隐私保护**：注重数据安全的用户，希望 AI 助手不依赖第三方云服务
- **多平台开发环境**：需要在不同操作系统间切换的开发者
- **AI 助手定制需求**：希望自定义 AI 助手功能和行为的进阶用户
- **离线/本地化部署**：需要本地运行 AI 功能、不依赖网络环境的场景

## 4. 技术亮点

- 使用 **TypeScript** 开发，类型安全且生态完善
- **开源架构**，社区贡献活跃，持续迭代更新
- 强调**数据所有权**，采用本地化部署方案，保障用户隐私
- 跨平台设计，一次开发即可适配多操作系统
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386744 | 🍴 81262 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

### 
- 链接: https://github.com/obra/superpowers
- ⭐ 273917 | 🍴 24519 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 232760 | 🍴 46496 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介

n8n 是一款采用公平代码协议的工作流自动化平台，内置原生 AI 能力。它支持可视化拖拽构建与自定义代码开发，可同时实现低代码/无代码的灵活工作流搭建。平台提供 400 多种集成方式，支持自托管或云端部署，满足多样化的自动化需求。

### 2. 核心功能

- **可视化工作流构建**：通过拖拽节点方式创建复杂自动化流程，降低开发门槛
- **原生 AI 能力集成**：内置 AI 功能，支持智能数据处理和自动化决策
- **400+ 应用集成**：覆盖主流 SaaS 服务、API 和数据库，实现跨平台数据流转
- **灵活部署方式**：支持自托管（Self-hosted）和云端部署，保障数据隐私与可控性
- **自定义代码扩展**：允许编写 TypeScript 代码，满足复杂业务逻辑需求

### 3. 适用场景

- **企业自动化办公**：连接 CRM、邮件、日历等工具，自动同步数据、触发提醒
- **数据管道与 ETL**：从多个数据源采集数据，进行清洗、转换后写入目标系统
- **AI 驱动的智能工作流**：结合 LLM 进行文本处理、摘要生成、智能问答等任务
- **MCP 协议集成**：支持 MCP 客户端/服务器，实现与大模型的工具调用交互

### 4. 技术亮点

- 基于 TypeScript 开发，类型安全且生态友好
- 支持 MCP（Model Context Protocol）协议，可无缝对接大模型工具调用
- 公平代码（Fair-code）许可，兼顾开源社区与商业使用的平衡
- 20万+ GitHub 星标，拥有活跃的开源社区和丰富的插件生态
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201158 | 🍴 60221 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI 工具，实现 AI 的普惠化愿景。项目的使命是提供强大的 AI 工具，让用户能够专注于真正重要的事务。

## 2. 核心功能
- **自主任务执行**：AI 代理可自主规划并执行复杂的多步骤任务
- **多模型支持**：兼容 OpenAI GPT、Claude、LLaMA 等多种大语言模型 API
- **记忆与工具链**：具备长期记忆能力，可调用浏览器、文件操作等外部工具
- **目标驱动代理**：基于用户设定的目标，自动分解任务并迭代执行
- **可扩展架构**：支持自定义插件和扩展，便于二次开发

## 3. 适用场景
- 自动化数据处理与报告生成
- 市场调研与信息搜集
- 代码开发与调试辅助
- 日常任务自动化（如文件管理、邮件处理）

## 4. 技术亮点
- 采用多代理协作架构，支持任务并行分解与执行
- 结合 RAG（检索增强生成）技术，提升信息检索准确性
- 开源社区活跃，拥有超过 18 万星标，生态完善
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186682 | 🍴 46053 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 169349 | 🍴 9454 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167515 | 🍴 21630 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164574 | 🍴 30551 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157882 | 🍴 46171 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153452 | 🍴 9895 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

