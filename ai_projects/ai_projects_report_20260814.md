# GitHub AI项目每日发现报告
日期: 2026-08-14

## 新发布的AI项目

### agent-safe-pipeline
- 

## GitHub项目分析：agent-safe-pipeline

### 1. 中文简介

该项目是一个AI代理安全治理的参考架构，代理可提出行动建议但无权自行授权。系统通过不可变意图捕获、独立的Decionis策略裁决（允许/升级/阻止）、人工审批验证以及一次性授权的SafeExecutor执行器，实现完整的代理操作安全管控。

### 2. 核心功能

- **不可变意图捕获**：记录AI代理的操作意图，确保意图数据不可篡改
- **独立策略裁决**：Decionis引擎对意图进行ALLOW（允许）、ESCALATE（升级）或BLOCK（阻止）的独立判断
- **人工审批验证**：关键操作需经人类确认后方可执行
- **一次性授权执行**：SafeExecutor仅能消耗一次性的、绑定特定意图的授权令牌
- **策略即代码**：将安全策略以代码形式定义和管理，便于版本控制和审计

### 3. 适用场景

- **企业AI代理部署**：需要确保AI代理在执行敏感操作前经过审批的企业环境
- **高风险自动化流程**：如金融交易、医疗操作等需要严格人工干预的场景
- **合规性要求高的系统**：满足审计追踪和权限管控法规要求的AI应用
- **MCP（模型上下文协议）集成**：需要安全治理的MCP代理系统

### 4. 技术亮点

- **意图与授权分离**：代理提出意图但无权执行，从根本上防止越权操作
- **不可变设计**：意图记录采用不可变存储，确保操作可追溯、防篡改
- **独立裁决层**：Decionis策略引擎与代理逻辑解耦，避免自我授权风险
- **TypeScript实现**：类型安全，适合企业级开发和维护
- 链接: https://github.com/decionis/agent-safe-pipeline
- ⭐ 363 | 🍴 3 | 语言: TypeScript
- 标签: agentic-ai, ai-agent-permissions, ai-agents, ai-governance, ai-safety

### modex-mh-agent
- 

# GitHub项目分析：modex-mh-agent

## 1. 中文简介
Modex MH Agent 是一款AI全自动数学建模智能体，覆盖科研全流程，能够从赛题分析到竞赛级论文撰写在一天内完成。支持全国大学生数学建模竞赛、美赛（MCM/ICM）及华为杯等主流数学建模赛事。

## 2. 核心功能
- **全自动数学建模**：AI驱动，一键完成从问题分析、模型构建到结果求解的完整流程
- **论文自动生成**：自动输出符合竞赛规范的学术级论文
- **多赛事兼容**：支持国赛、美赛、华为杯等不同赛事的赛题格式与评分标准
- **科研全流程覆盖**：整合选题、建模、编程、写作等科研各环节

## 3. 适用场景
- 大学生参加数学建模竞赛备赛与实战
- 科研人员快速完成数学建模任务
- 需要高效解决优化、预测、评价类问题的场景

## 4. 技术亮点
- 以架构展示为主的项目，突出AI智能体在数学建模领域的自动化能力
- 支持多种主流数学建模竞赛，具备较强的通用性
- 链接: https://github.com/N-allpass/modex-mh-agent
- ⭐ 179 | 🍴 0 | 语言: 未知

### mcp-memory
- 

## MCP-Memory 项目分析

### 1. 中文简介
这是一个基于 OKF 的 Model Context Protocol (MCP) 服务器，为 AI 代理提供持久化的长期记忆存储和 SQLite FTS5 全文搜索功能。该项目旨在增强 AI 代理的记忆能力，使其能够跨会话保存和检索信息。

### 2. 核心功能
- 持久化长期记忆存储，支持跨会话数据保留
- 基于 SQLite FTS5 的高效全文搜索引擎
- 符合 MCP 协议标准，便于与 AI 框架集成
- 使用 Python 开发，轻量且易于部署
- 为 AI 代理提供上下文记忆管理能力

### 3. 适用场景
- AI 聊天机器人需要记住用户偏好和历史对话
- 多会话 AI 代理需要跨轮次保持上下文连贯性
- 需要快速检索历史信息的智能助手系统
- 构建具备长期记忆能力的自动化工作流

### 4. 技术亮点
- 采用 SQLite FTS5 实现高性能全文检索，查询速度快
- 基于 OKF 框架，结构清晰且扩展性强
- 完全兼容 MCP 协议，可无缝接入主流 AI 工具链
- Python 实现，代码简洁，社区易于贡献和维护
- 链接: https://github.com/fellowgeek/mcp-memory
- ⭐ 144 | 🍴 5 | 语言: Python

### oss-pr-reviewer
- 

## oss-pr-reviewer 项目分析

### 1. 中文简介
这是一个基于AI的命令行工具，专为审查GitHub拉取请求而设计。它能自动检测代码中的潜在Bug、安全风险、回归问题以及缺失的测试用例，并生成结构化的Markdown报告，帮助开源项目维护者高效完成代码审查工作。

### 2. 核心功能
- **AI驱动的代码审查**：利用大语言模型自动分析PR内容
- **多类型问题检测**：识别Bug、安全漏洞、回归缺陷及缺失测试
- **结构化报告生成**：输出格式化的Markdown审查报告
- **CLI工具集成**：支持命令行方式快速部署和使用
- **开源维护者友好**：专为开源项目维护场景优化

### 3. 适用场景
- 开源项目维护者批量审查社区提交的PR
- 团队协作中需要快速进行代码质量检查
- 安全敏感项目需要自动检测潜在风险
- 希望提升代码审查效率的个人开发者

### 4. 技术亮点
- 基于TypeScript开发，具备良好的类型安全性和生态兼容性
- 结合LLM能力实现智能化代码分析
- 专为开源社区场景定制，降低维护者工作负担
- 链接: https://github.com/vuphongle/oss-pr-reviewer
- ⭐ 95 | 🍴 93 | 语言: TypeScript
- 标签: ai, cli, code-review, developer-tools, github

### godmode
- 

## godmode 项目分析

### 1. 中文简介
godmode 是为 AI 编程代理提供生产级 Agent 技能的工具库，支持规划、测试驱动开发、调试、代码审查、UI/UX、发布、事件处理和评估等可组合工作流。

### 2. 核心功能
- 提供可组合的 AI 编程工作流，覆盖开发全流程
- 支持 TDD（测试驱动开发）和自动化代码审查
- 集成调试、UI/UX 优化和版本发布能力
- 内置评估（evals）模块，用于衡量代理表现
- 兼容主流 AI 编程工具（Claude Code、Codex 等）

### 3. 适用场景
- 使用 AI 编程代理（如 Claude Code、OpenAI Codex）的团队，需要标准化开发流程
- 希望将测试驱动开发、代码审查等最佳实践自动化嵌入 AI 工作流的开发者
- 需要评估和优化 AI 编程代理输出质量的工程团队

### 4. 技术亮点
- 基于 Python 构建，易于集成和扩展
- 模块化设计，各技能可独立使用或组合为完整工作流
- 针对主流 AI 编程代理（claude-code、codex）进行优化适配
- 覆盖从编码到发布的全生命周期，减少手动操作成本
- 链接: https://github.com/thiientv/godmode
- ⭐ 89 | 🍴 87 | 语言: Python
- 标签: agent-evaluation, agent-skills, ai-agents, ai-coding, claude-code

### ai-agent-for-magento2
- 描述: 无描述
- 链接: https://github.com/duongdang942/ai-agent-for-magento2
- ⭐ 80 | 🍴 80 | 语言: PHP

### ai-super-model
- 描述: 无描述
- 链接: https://github.com/dungoutlook1/ai-super-model
- ⭐ 78 | 🍴 78 | 语言: Rust

### ai-interview-handbook-cn
- 描述: 大模型面试 144 问、Top Interview 150 导航与 Python 手撕代码模板
- 链接: https://github.com/Skyfacon/ai-interview-handbook-cn
- ⭐ 78 | 🍴 22 | 语言: 未知

### agentic-playwright
- 描述: Production-grade Playwright + TypeScript Scaffold for Agentic Testing. Harness for all major AI coding agents baked in.
- 链接: https://github.com/idavidov13/agentic-playwright
- ⭐ 55 | 🍴 19 | 语言: Python
- 标签: agentic, ai, api-testing, claude-code, cursor

### salsi
- 描述: Write Persian with Persian words — a loanword scanner and an AI-assistant skill built on the Pasban dictionary. Ships 20,071 words, protects technical terms, code and quotations. Works in Claude, Codex, Cursor and more.
- 链接: https://github.com/pooooooriya/salsi
- ⭐ 47 | 🍴 2 | 语言: Python
- 标签: agent-skill, ai-skills, farsi, linter, nlp

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82453 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI相关项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码实现，是AI学习者与实践者的优质资源库。

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域。
- 每个项目均附带可运行的源代码，方便直接学习和实践。
- 以Awesome列表形式组织，便于分类浏览和快速查找。
- 主要使用Python语言实现，适合Python开发者直接使用。

### 3. 适用场景
- **AI学习者**：系统学习机器学习与深度学习，通过实战项目巩固理论知识。
- **开发者参考**：快速查找特定AI任务（如图像分类、文本生成）的开源实现。
- **项目灵感来源**：从丰富项目中获取创意，用于个人练习或商业项目参考。
- **教学与培训**：作为AI课程的教学素材，帮助学生理解算法的实际应用。

### 4. 技术亮点
- **规模庞大**：收录500个项目，覆盖AI主流方向，资源极其丰富。
- **完整可运行**：每个项目均附带代码，无需额外查找即可上手实践。
- **分类清晰**：按机器学习、深度学习、计算机视觉、NLP等标签分类，便于精准定位。
- **社区认可度高**：36255星标，是GitHub上最受欢迎的AI项目合集之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36255 | 🍴 7431 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够直观地展示模型结构和参数信息。

### 2. 核心功能
- 支持多格式模型导入，包括 ONNX、TensorFlow、PyTorch、CoreML 等
- 提供清晰的神经网络架构图可视化展示
- 支持查看模型层详情和参数信息
- 可导出模型结构图为图片格式
- 支持桌面端和浏览器端两种使用方式

### 3. 适用场景
- 深度学习模型调试与结构分析
- 模型转换前后的对比验证
- 教学演示中的模型可视化展示
- 模型部署前的结构审查

### 4. 技术亮点
- 纯前端技术实现，无需后端服务即可运行
- 支持 safetensors 等新兴模型格式
- 社区活跃，星标数超过 3.3 万，生态完善
- 跨平台兼容，支持 Windows、macOS、Linux 及浏览器
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33351 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# ONNX 项目分析

## 1. 中文简介

ONNX（Open Neural Network Exchange）是机器学习互操作性的开放标准，旨在实现不同AI框架之间的无缝模型交换。它允许开发者在不同深度学习平台间自由迁移模型，打破框架壁垒，提升开发效率。

## 2. 核心功能

- **跨框架模型转换**：支持PyTorch、TensorFlow、Keras等主流框架之间的模型互转
- **统一模型表示**：提供标准化的模型格式，确保模型在不同平台间保持一致性
- **推理优化**：支持模型压缩、量化和图优化，提升推理性能
- **部署灵活**：可在移动端、嵌入式设备和云端等多种环境中部署模型
- **生态兼容**：与Scikit-learn等经典ML库集成，覆盖完整AI开发生态

## 3. 适用场景

- **模型迁移**：将训练好的模型从PyTorch迁移到TensorFlow Lite或ONNX Runtime进行部署
- **生产环境部署**：在资源受限的边缘设备或移动端运行经过优化的模型
- **跨团队协作**：数据科学家使用Python训练模型，工程师使用其他工具链进行优化和部署
- **模型服务化**：通过ONNX Runtime实现高性能的模型推理服务

## 4. 技术亮点

- 由微软和Facebook联合发起，拥有强大的社区和企业支持
- 支持超过30种算子，覆盖主流深度学习模型结构
- 提供ONNX Checker和ONNX Simplifier等工具链，保障模型质量和可维护性
- 链接: https://github.com/onnx/onnx
- ⭐ 21312 | 🍴 3995 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18616 | 🍴 1200 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17358 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13257 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11627 | 🍴 914 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10689 | 🍴 5702 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI相关项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码实现，是AI学习者与实践者的优质资源库。

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域。
- 每个项目均附带可运行的源代码，方便直接学习和实践。
- 以Awesome列表形式组织，便于分类浏览和快速查找。
- 主要使用Python语言实现，适合Python开发者直接使用。

### 3. 适用场景
- **AI学习者**：系统学习机器学习与深度学习，通过实战项目巩固理论知识。
- **开发者参考**：快速查找特定AI任务（如图像分类、文本生成）的开源实现。
- **项目灵感来源**：从丰富项目中获取创意，用于个人练习或商业项目参考。
- **教学与培训**：作为AI课程的教学素材，帮助学生理解算法的实际应用。

### 4. 技术亮点
- **规模庞大**：收录500个项目，覆盖AI主流方向，资源极其丰富。
- **完整可运行**：每个项目均附带代码，无需额外查找即可上手实践。
- **分类清晰**：按机器学习、深度学习、计算机视觉、NLP等标签分类，便于精准定位。
- **社区认可度高**：36255星标，是GitHub上最受欢迎的AI项目合集之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36255 | 🍴 7431 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，能够直观地展示模型结构和参数信息。

### 2. 核心功能
- 支持多格式模型导入，包括 ONNX、TensorFlow、PyTorch、CoreML 等
- 提供清晰的神经网络架构图可视化展示
- 支持查看模型层详情和参数信息
- 可导出模型结构图为图片格式
- 支持桌面端和浏览器端两种使用方式

### 3. 适用场景
- 深度学习模型调试与结构分析
- 模型转换前后的对比验证
- 教学演示中的模型可视化展示
- 模型部署前的结构审查

### 4. 技术亮点
- 纯前端技术实现，无需后端服务即可运行
- 支持 safetensors 等新兴模型格式
- 社区活跃，星标数超过 3.3 万，生态完善
- 跨平台兼容，支持 Windows、macOS、Linux 及浏览器
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33351 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub 项目分析：cheatsheets-ai

## 1. 中文简介
该项目为深度学习与机器学习研究人员提供了一套全面的速查手册。内容涵盖人工智能、机器学习、Keras、NumPy、SciPy 和 Matplotlib 等核心工具的关键知识点，方便研究者快速查阅和复习。

## 2. 核心功能
- 提供深度学习与机器学习领域的关键概念速查表
- 涵盖 Keras、NumPy、SciPy、Matplotlib 等常用库的语法与技巧
- 以简洁的 cheat sheet 形式呈现，便于快速检索和记忆
- 由 Medium 技术博主整理发布，内容贴近研究实践

## 3. 适用场景
- 深度学习/机器学习研究者快速复习核心概念和库用法
- 学生或初学者系统梳理 AI 相关工具链的关键知识点
- 项目开发过程中查阅常用代码片段和函数参数

## 4. 技术亮点
- 高人气项目（15,428 星标），内容经过社区广泛验证
- 覆盖从基础库（NumPy/SciPy）到框架（Keras）的完整技术栈
- 以可视化速查形式呈现，提升学习效率
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# Ai-Learn 项目分析

## 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，帮助零基础学习者入门并提升就业竞争力。内容涵盖Python、机器学习、深度学习、自然语言处理、计算机视觉等热门领域。

## 2. 核心功能
- 提供系统化的AI学习路线图，从零基础到就业实战全覆盖
- 整理近200个实战案例与项目，便于动手实践
- 免费提供配套教材和学习资源
- 覆盖Python、数学、机器学习、深度学习、NLP、CV等多个技术领域

## 3. 适用场景
- 零基础学习者系统入门人工智能领域
- 准备AI相关岗位求职的实战训练
- 希望梳理知识体系的学习者参考使用
- 需要大量实战案例进行技能提升的开发者

## 4. 技术亮点
- 整合了TensorFlow、PyTorch、Keras、Caffe等主流深度学习框架的学习资源
- 涵盖numpy、pandas、matplotlib、seaborn等数据分析核心库的实战应用
- 项目星标数超过13000，社区认可度高，资料持续更新
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13257 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式配置简化了模型开发流程，让开发者无需编写大量代码即可完成从数据处理到模型训练的全流程。

### 2. 核心功能
- **低代码/声明式建模**：通过 YAML 配置文件定义模型架构，无需手写复杂代码。
- **多模态支持**：原生支持文本、图像、表格、音频等多种数据类型。
- **集成主流模型**：支持 LLaMA、LLaMA2、Mistral 等大语言模型的微调与训练。
- **端到端训练流程**：内置数据预处理、特征工程、模型训练与评估的完整流水线。
- **基于 PyTorch 构建**：底层使用 PyTorch，兼顾灵活性与性能。

### 3. 适用场景
- **AI 模型快速原型开发**：适合希望快速验证想法、无需深入代码细节的数据科学家。
- **大语言模型微调**：针对特定任务对 LLaMA、Mistral 等开源模型进行领域适配。
- **多模态 AI 应用构建**：需要同时处理文本、图像等多种输入形式的场景。
- **数据驱动型机器学习项目**：以数据为中心，快速迭代实验并比较不同模型效果。

### 4. 技术亮点
- **数据-centric 设计哲学**：强调数据质量与特征工程在模型效果中的核心作用。
- **开箱即用的预训练模型集成**：内置对 LLaMA、LLaMA2、Mistral 等热门模型的直接支持，降低使用门槛。
- **社区活跃**：11748 星标表明该项目拥有较高的关注度和使用群体。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9171 | 🍴 1234 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8962 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1898 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6993 | 🍴 1174 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6399 | 🍴 774 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82453 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种模型。该项目在 ACL 2024 会议上发表，旨在为研究者与开发者提供一站式模型微调解决方案。

### 2. 核心功能
- 支持 100+ 种主流大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、P-Tuning 等多种高效微调方法
- 支持 RLHF（基于人类反馈的强化学习）训练流程
- 内置量化功能（如 4bit/8bit 量化），降低显存占用
- 兼容 Transformers、PEFT 等主流深度学习框架

### 3. 适用场景
- 研究人员快速微调 LLaMA、Qwen、DeepSeek、Gemma 等开源模型
- 开发者在消费级 GPU 上通过 QLoRA 进行低资源微调
- 企业或个人构建垂直领域专属语言模型
- 进行多模态视觉语言模型的指令微调与对齐训练

### 4. 技术亮点
- **统一架构**：一套代码支持上百种模型，降低学习成本
- **极致高效**：QLoRA 等技术实现低显存、高效率的微调体验
- **社区活跃**：GitHub 星标超过 7.4 万，ACL 2024 收录，学术与工业界双重认可
- **生态完善**：完整覆盖从指令微调、RLHF 到量化的全流程训练链路
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74097 | 🍴 9067 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，历时12周，包含24节课程，面向所有对人工智能感兴趣的初学者。项目以Jupyter Notebook为载体，系统性地讲解从基础概念到深度学习的全方位AI知识。

### 2. 核心功能
- 提供结构化的12周AI学习路径，涵盖机器学习、深度学习、计算机视觉和自然语言处理
- 使用Jupyter Notebook实现交互式代码教学，便于动手实践
- 微软官方出品，内容权威且免费开放
- 覆盖CNN、RNN、GAN等主流深度学习模型原理与实践
- 适合零基础学习者循序渐进掌握AI核心技能

### 3. 适用场景
- 初学者系统学习人工智能基础理论
- 高校或培训机构作为AI课程的补充教材
- 职场人士利用业余时间转行AI领域
- 企业团队内部AI技术培训参考

### 4. 技术亮点
- 微软官方开源项目，星标超6.4万，社区活跃度高
- 内容全面，覆盖ML、DL、CV、NLP四大核心领域
- 代码即学即用，配套完整示例与练习
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 64905 | 🍴 12589 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46728 | 🍴 8163 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub 项目分析：ailearning

---

### 1. 中文简介

这是一个全面的机器学习与深度学习实战学习项目，涵盖数据分析、线性代数基础、PyTorch、NLTK自然语言处理库以及TensorFlow 2等多个技术栈。项目通过理论与实践结合的方式，帮助学习者系统掌握从传统机器学习到深度学习的核心技能。

---

### 2. 核心功能

- **机器学习算法实战**：涵盖Adaboost、SVM、KMeans、朴素贝叶斯、逻辑回归、回归分析等经典算法的实现与应用。
- **深度学习框架学习**：基于PyTorch和TensorFlow 2，深入讲解DNN、RNN、LSTM等神经网络模型。
- **自然语言处理（NLP）**：使用NLTK库进行文本处理、分词及NLP相关实战。
- **关联规则与推荐系统**：实现Apriori、FP-Growth等关联规则算法，并应用于推荐系统场景。
- **数据降维与特征工程**：通过PCA、SVD等线性代数方法实现数据降维与特征提取。

---

### 3. 适用场景

- **机器学习入门学习者**：需要系统学习从数学基础到算法实战的完整路径。
- **数据分析从业者**：希望通过实战项目提升数据处理与建模能力。
- **深度学习研究者**：需要PyTorch和TF2双框架的模型实现参考。
- **NLP方向开发者**：寻求NLTK结合深度学习进行文本处理的实践案例。

---

### 4. 技术亮点

- **双深度学习框架覆盖**：同时支持PyTorch和TensorFlow 2，便于对比学习与灵活选用。
- **从数学基础到工程实战**：线性代数理论结合代码实现，形成完整知识闭环。
- **标签算法丰富全面**：涵盖监督学习、无监督学习、深度学习、NLP、推荐系统等多个领域，适合作为一站式学习资源库。
- **高人气验证**：42451颗星标表明该项目在开发者社区中具有较高的认可度和参考价值。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42451 | 🍴 11519 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36255 | 🍴 7431 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33819 | 🍴 4709 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29064 | 🍴 3538 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21838 | 🍴 3352 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17358 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI相关项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码实现，是AI学习者与实践者的优质资源库。

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域。
- 每个项目均附带可运行的源代码，方便直接学习和实践。
- 以Awesome列表形式组织，便于分类浏览和快速查找。
- 主要使用Python语言实现，适合Python开发者直接使用。

### 3. 适用场景
- **AI学习者**：系统学习机器学习与深度学习，通过实战项目巩固理论知识。
- **开发者参考**：快速查找特定AI任务（如图像分类、文本生成）的开源实现。
- **项目灵感来源**：从丰富项目中获取创意，用于个人练习或商业项目参考。
- **教学与培训**：作为AI课程的教学素材，帮助学生理解算法的实际应用。

### 4. 技术亮点
- **规模庞大**：收录500个项目，覆盖AI主流方向，资源极其丰富。
- **完整可运行**：每个项目均附带代码，无需额外查找即可上手实践。
- **分类清晰**：按机器学习、深度学习、计算机视觉、NLP等标签分类，便于精准定位。
- **社区认可度高**：36255星标，是GitHub上最受欢迎的AI项目合集之一。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36255 | 🍴 7431 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于人工智能的浏览器自动化框架，能够智能地执行和管理基于浏览器的业务流程。它利用AI技术模拟人类操作浏览器，实现复杂的网页交互任务自动化，无需手动编写繁琐的脚本代码。

### 2. 核心功能
- **AI驱动的浏览器自动化**：利用大语言模型理解页面内容并智能执行操作
- **多浏览器引擎支持**：兼容Playwright、Puppeteer、Selenium等主流自动化工具
- **计算机视觉集成**：结合视觉识别技术增强页面元素理解和交互能力
- **工作流自动化编排**：提供API接口，支持复杂业务流程的自动化编排和执行
- **RPA企业级能力**：具备企业级RPA功能，可替代Power Automate等传统自动化工具

### 3. 适用场景
- **网页数据抓取与表单填写**：自动化完成需要登录、填写表单、提交数据的重复性工作
- **电商流程自动化**：如自动比价、监控商品价格变动、自动下单等场景
- **企业业务流程自动化**：替代人工完成ERP、CRM等系统间的重复性操作
- **测试与QA自动化**：自动化执行网页应用的回归测试和验收测试

### 4. 技术亮点
- **AI+自动化创新融合**：将GPT等大语言模型能力与浏览器自动化技术深度结合，实现语义级理解而非简单的DOM操作
- **多引擎灵活切换**：支持多种浏览器自动化工具，可根据场景选择最优方案
- **视觉辅助定位**：结合计算机视觉技术，能够识别和处理传统自动化难以处理的动态页面元素
- **高社区认可度**：22753+星标表明该项目在开发者社区中具有广泛影响力和实用性
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22753 | 🍴 2140 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（Computer Vision Annotation Tool）是一款领先的开源视觉数据集标注平台，支持图像、视频及 3D 数据的标注工作。它提供开源版、云端版和企业版等多种产品形态，并配备 AI 辅助标注、质量保证、团队协作和开发者 API 等核心能力。

## 2. 核心功能
- 支持图像、视频和 3D 数据的多种标注格式（边界框、语义分割、关键点等）
- AI 辅助标注功能，可大幅提升标注效率
- 团队协作与任务分配机制，支持多人协同标注
- 质量保证与审核流程，确保数据集标注质量
- 提供开发者 API，便于集成到现有工作流中

## 3. 适用场景
- **计算机视觉模型训练**：为目标检测、图像分类等任务构建高质量标注数据集
- **视频分析项目**：对视频帧进行逐帧标注，适用于行为识别、目标跟踪等场景
- **企业级标注团队**：需要多人协作、流程管控和质量审核的大规模标注项目
- **学术研究**：用于构建公开数据集或进行视觉算法研究的数据准备

## 4. 技术亮点
- 由 Intel 主导开发，社区活跃，星标数超过 16,500，生态成熟
- 同时支持 PyTorch 和 TensorFlow 生态，兼容主流深度学习框架
- 提供丰富的标注类型：边界框、多边形、关键点、语义分割等，覆盖物体检测、图像分类、语义分割等多种任务需求
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16523 | 🍴 3803 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

## 1. 中文简介
本项目是一个面向计算机视觉的高级AI可解释性工具库，支持CNN和Vision Transformers等多种模型架构。它提供了Grad-CAM、Score-CAM等多种可视化方法，帮助研究人员理解深度学习模型的决策过程。

## 2. 核心功能
- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种类激活图生成方法
- 兼容CNN、Vision Transformers等主流深度学习架构
- 适用于图像分类、目标检测、图像分割等多种任务
- 支持图像相似度分析的可解释性可视化
- 提供简洁的API接口，易于集成到现有PyTorch项目中

## 3. 适用场景
- 深度学习模型调试与错误分析，定位模型关注区域
- 学术论文中可视化模型决策依据，增强结果说服力
- 医疗影像分析等需要模型可解释性的领域
- 教学演示，帮助学生理解神经网络工作原理

## 4. 技术亮点
- 统一接口支持多种Grad-CAM变体，无需重复实现
- 原生PyTorch实现，与主流深度学习框架无缝集成
- 社区活跃，星标数近1.3万，文档完善且持续维护
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12953 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11315 | 🍴 1221 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2189 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3478 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3370 | 🍴 411 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2632 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2505 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款个人 AI 助手工具，支持任意操作系统和平台，采用"龙虾方式"（lobster way）让你完全掌控自己的数据，实现真正私有的 AI 助手体验。

### 2. 核心功能
- **跨平台支持**：兼容任意操作系统，随时随地使用
- **数据私有化**：用户完全拥有和控制自己的数据
- **AI 助手集成**：提供智能个人助理功能
- **TypeScript 开发**：基于现代前端技术栈构建
- **开源自由**：开源项目，可自由定制和扩展

### 3. 适用场景
- **个人数据管理**：需要本地化存储敏感信息的用户
- **跨设备协作**：在多个平台间同步 AI 助手使用
- **隐私优先场景**：不希望数据上传云端的用户
- **开发者定制**：需要二次开发个性化 AI 助手的场景

### 4. 技术亮点
- 高星标数（38万+）证明社区认可度
- 采用 TypeScript 保证代码质量和可维护性
- 强调"own-your-data"理念，符合当前隐私保护趋势
- 跨平台架构设计，适配性强

---

**总结**：OpenClaw 是一个专注于数据私有化的个人 AI 助手项目，适合注重隐私、需要跨平台使用的用户，尤其是开发者和数据敏感型用户。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386320 | 🍴 81202 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub项目分析：superpowers

### 1. 中文简介
这是一个基于AI代理的技能框架与软件开发方法论，旨在提供切实可行的软件开发方案。该项目结合了智能代理（Agent）技术与子代理驱动开发模式，帮助开发者更高效地完成软件开发生命周期中的各项任务。

### 2. 核心功能
- 提供AI代理驱动的技能框架，支持自动化软件开发流程
- 采用子代理驱动开发（Subagent-Driven Development）模式，实现任务分解与并行处理
- 整合头脑风暴与编码功能，辅助开发者的创意与技术实现
- 遵循OBRA方法论，规范软件开发生命周期（SDLC）各阶段
- 以Shell脚本为核心，实现跨平台兼容的轻量级部署

### 3. 适用场景
- 需要快速原型开发或MVP构建的初创项目
- 希望通过AI辅助提升编码效率的团队或个人开发者
- 采用敏捷开发模式、需要自动化任务分解的软件项目
- 探索AI代理在软件开发中应用的实验性项目

### 4. 技术亮点
- 星标数超27万，显示社区高度认可与广泛使用
- 将AI代理能力与成熟SDLC方法论结合，兼顾创新与实用性
- 基于Shell实现，部署简单、跨平台兼容性强
- 支持多代理协作模式，可灵活扩展不同开发技能
- 链接: https://github.com/obra/superpowers
- ⭐ 272149 | 🍴 24337 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# hermes-agent 项目分析

---

## 1. 中文简介
hermes-agent 是一个与你共同成长的 AI 智能体，能够持续学习和适应你的需求。它支持多种大语言模型，提供灵活的 AI 代理能力。

## 2. 核心功能
- 支持多模型接入（Anthropic Claude、OpenAI GPT、Codex 等）
- 提供智能对话与任务执行能力
- 具备代码辅助与开发支持功能
- 支持个性化学习与持续成长
- 开源可定制，适配多种使用场景

## 3. 适用场景
- **开发辅助**：代码编写、调试与项目管理的 AI 助手
- **智能对话**：日常问答、知识查询与内容生成
- **自动化任务**：通过自然语言驱动复杂工作流执行
- **多模型实验**：在同一平台对比测试不同 LLM 的能力

## 4. 技术亮点
- 兼容主流商业模型（Claude、GPT 系列），降低多模型切换成本
- 由 Nous Research 团队开发，在社区拥有较高关注度（23万+星标）
- 开源架构，便于二次开发与功能扩展
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 230612 | 🍴 45718 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一个具有原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合，提供 400+ 种集成，可自托管或云端部署。

### 2. 核心功能
- **可视化工作流构建**：拖拽式界面，无需编码即可创建工作流
- **原生 AI 集成**：内置 AI 能力，支持智能自动化任务
- **400+ 应用集成**：覆盖主流 SaaS 服务和 API 连接
- **灵活部署**：支持自托管私有化部署或云端托管
- **代码扩展**：支持自定义代码节点，满足复杂需求

### 3. 适用场景
- **企业自动化**：跨系统数据同步、审批流程自动化
- **AI 工作流**：构建 AI 驱动的内容生成、数据分析流程
- **低代码平台**：非技术人员快速搭建自动化解决方案
- **MCP 集成**：支持 Model Context Protocol 的 AI 工具调用

### 4. 技术亮点
- **MCP 协议支持**：原生支持 MCP Client/Server，便于 AI 工具链集成
- **TypeScript 开发**：类型安全，代码质量高
- **Fair-code 许可**：开源但限制竞争场景，兼顾开放与商业保护
- **CLI 工具**：支持命令行管理，便于 DevOps 集成
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200651 | 🍴 60133 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能使用并构建 AI，实现 AI 的普及化愿景。我们的使命是提供易用的工具，让你能够专注于真正重要的事物。

## 2. 核心功能
- 自主 AI 代理：可独立规划并执行复杂的多步骤任务
- 多模型兼容：支持 OpenAI、Claude、Llama 等多种大语言模型
- 任务分解执行：将复杂目标自动拆分为可执行的子任务链
- 工具链集成：可调用浏览器、文件系统、代码执行等外部工具
- 持久化记忆：具备跨会话记忆能力，保持任务上下文连贯性

## 3. 适用场景
- 自动化数据处理与分析工作流
- 内容创作与多平台发布自动化
- 复杂调研任务的自主执行与汇总
- 个人助理与日常任务自动化管理

## 4. 技术亮点
- 基于 ReAct 推理框架实现自主决策循环
- 可扩展的插件系统，支持自定义工具接入
- 支持 GPT-4 等前沿模型的最新能力
- 活跃的开源社区持续迭代更新
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186625 | 🍴 46082 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 167401 | 🍴 9389 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167126 | 🍴 21574 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164515 | 🍴 30562 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157781 | 🍴 46177 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153247 | 🍴 9863 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

