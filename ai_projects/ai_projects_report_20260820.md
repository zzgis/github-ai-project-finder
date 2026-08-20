# GitHub AI项目每日发现报告
日期: 2026-08-20

## 新发布的AI项目

### watermarks-remover
- 

## watermarks-remover 项目分析

### 1. 中文简介
该项目是一款用于移除多供应商AI溯源痕迹的工具，支持从PNG、JPEG、SVG、PDF、DOCX、HTML、MD等多种文件格式中清除Unicode文本痕迹、元数据及C2PA数字水印。通过统计重写技术和文本清理方法，帮助用户去除AI生成内容中嵌入的溯源标记。

### 2. 核心功能
- 清除Unicode文本层面的AI溯源痕迹
- 使用统计重写技术改写内容以避免检测
- 剥离PNG/JPEG/SVG/PDF/DOCX/HTML/MD文件的C2PA标准元数据
- 支持多种主流文件格式的水印去除
- 兼容Claude、Codex、Grok等多平台AI生成内容的溯源清除

### 3. 适用场景
- 内容创作者需要清理AI辅助生成内容中的溯源标记以便发布
- 企业批量处理文档时需移除文件中的数字水印信息
- 研究人员分析AI溯源技术的工作原理与检测方法
- 需要将AI生成素材用于商业用途前清除来源痕迹

### 4. 技术亮点
- 同时支持文本层和元数据层的双轨清除策略
- 涵盖C2PA（Coalition for Content Provenance and Authenticity）开放标准
- 统计重写方法可在保留内容语义的同时改变指纹特征
- 跨文件格式的统一处理架构
- 链接: https://github.com/Leutenegger/watermarks-remover
- ⭐ 924 | 🍴 95 | 语言: Python
- 标签: claude, claude-code, claude-skills, codex, codex-cli

### coldcard-airgap
- 

## Coldcard-Airgap 项目分析

### 1. 中文简介
Coldcard-Airgap 是专为 Coldcard 硬件钱包用户设计的离线工具集，提供 PSBT 检查、种子分片、二维码编解码等功能，是官方 Coldcard 固件的配套工具（与 Coinkite 无隶属关系）。

### 2. 核心功能
- **PSBT 检查**：离线分析隔离签名交易，确保交易内容符合预期
- **BIP39/骰子熵生成**：支持通过骰子投掷生成符合 BIP39 标准的真随机种子
- **Seed XOR 分片与合并**：将种子加密拆分为多份或合并恢复，实现高安全种子管理
- **BBQr 编解码**：处理 BIP-352 格式的二维码，支持离线数据交换
- **固件验证指导**：提供 Coldcard 固件的完整性校验方法

### 3. 适用场景
- **离线交易审查**：在联网前检查 PSBT 的交易输出地址和金额，防止恶意篡改
- **种子分片备份**：将主种子 XOR 拆分为 2-3 份，分别存放于不同安全位置
- **高安全环境种子生成**：通过骰子投掷生成无电子痕迹的真随机钱包种子
- **固件完整性验证**：确认下载的 Coldcard 固件未被篡改

### 4. 技术亮点
- 纯 Python 实现，无外部依赖，适合离线环境运行
- 支持 BIP-352 BBQr 格式，兼容主流 Coldcard 固件版本
- 提供端到端的离线工作流，从种子生成到交易签名的完整安全链
- 链接: https://github.com/Leutenegger/coldcard-airgap
- ⭐ 607 | 🍴 79 | 语言: Python
- 标签: airgap, airgap-devkit, airgap-download, airgap-setup, airgap-tutorial

### llm-rag-memory-ai-agents
- 

# 项目分析：llm-rag-memory-ai-agents

## 1. 中文简介
这是一个结合大语言模型（LLM）、检索增强生成（RAG）和长期记忆的AI代理框架，旨在为智能体提供持续学习和知识积累能力。项目通过RAG技术增强AI的上下文理解，同时利用记忆模块实现跨会话的知识保留。

## 2. 核心功能
- **LLM集成**：支持主流大语言模型，提供强大的自然语言处理能力
- **RAG检索增强**：结合外部知识库，提升回答的准确性和上下文相关性
- **记忆系统**：实现短期和长期记忆存储，支持跨对话的知识延续
- **AI代理架构**：提供可复用的智能体框架，支持任务规划和自主决策

## 3. 适用场景
- 企业知识库问答系统，支持员工快速检索内部文档
- 个性化虚拟助手，能够记住用户偏好和历史交互
- 多轮对话客服机器人，具备持续学习和服务改进能力
- 智能研究助手，整合文献资料并提供深度分析

## 4. 技术亮点
- 将RAG与记忆机制深度融合，兼顾实时检索与历史积累
- 模块化设计，便于扩展不同的LLM后端和存储方案
- 适合构建需要长期交互和知识沉淀的智能应用

---

> **说明**：由于项目描述为"None"，以上分析基于项目名称关键词（LLM、RAG、Memory、AI Agents）进行推断，仅供参考。建议访问项目仓库查看实际代码和文档以获取更准确信息。
- 链接: https://github.com/turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents
- ⭐ 107 | 🍴 0 | 语言: Python

### dsh-oil-creator
- 

# GitHub项目分析：dsh-oil-creator

## 1. 中文简介
这是一个为DeepSeek Harness设计的AI辅助本地创作者工作台，作为DSH插件运行，帮助本地用户更高效地创建和管理AI相关内容。

## 2. 核心功能
- 提供AI辅助的内容创作工作流，简化本地创作流程
- 作为DeepSeek Harness的插件扩展，无缝集成现有工作生态
- 支持本地化部署，保障数据隐私与创作自由度
- 内置智能化工具，提升内容生成效率与质量

## 3. 适用场景
- 需要本地化AI创作环境的开发者与内容创作者
- 希望扩展DeepSeek Harness功能的插件使用者
- 注重数据隐私、不希望依赖云端服务的创作团队
- 快速原型开发与内容批量生成的工作场景

## 4. 技术亮点
- 基于TypeScript开发，类型安全且易于维护扩展
- 采用插件架构设计，可灵活集成到DeepSeek Harness生态
- 本地优先（Local-first）架构，减少对外部服务的依赖
- 链接: https://github.com/oil-oil/dsh-oil-creator
- ⭐ 93 | 🍴 18 | 语言: TypeScript
- 标签: creator, deepseek-harness, dsh-plugin

### github-farm
- 

## GitHub 项目分析：github-farm

### 1. 中文简介
这是一个面向AI网关的生产级多平台OAuth收集与会话管理框架，专为AI代理友好设计。它支持跨多个平台的OAuth认证流程，帮助AI系统安全地获取和管理用户会话。

### 2. 核心功能
- 支持多平台OAuth认证收集与会话管理
- 专为AI代理和AI网关设计，提供友好的集成接口
- 生产级稳定性，适用于大规模部署场景
- 自动化OAuth流程，减少人工干预
- 统一的会话管理框架，简化跨平台认证

### 3. 适用场景
- AI网关开发：为AI服务提供多平台用户认证能力
- 多平台OAuth集成：统一管理多个社交平台的登录授权
- AI代理自动化：让AI代理能够自主完成OAuth认证流程
- 企业级身份管理：集中管理用户跨平台会话

### 4. 技术亮点
- 基于Python开发，生态丰富且易于扩展
- 生产级代码质量，适合直接投入实际使用
- 针对AI代理场景优化，降低集成复杂度
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 87 | 🍴 8 | 语言: Python

### lanshu-create-ai-presenter-video
- 描述: Provider-neutral Codex Skill for producing verified AI presenter videos from a script and an authorized presenter image.
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 72 | 🍴 13 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### neurocursor-ai
- 描述: AI-powered, camera-based mouse cursor control written in C++. Turn your webcam into a hands-free pointing device — built for gaming, perfect for everyday use and accessibility.
- 链接: https://github.com/stems-arraign-48/neurocursor-ai
- ⭐ 50 | 🍴 0 | 语言: C++
- 标签: ai, computer-vision, cplusplus, cpp, cursor-control

### DoveVannoINostriSoldi
- 描述: Raccogliamo e analizziamo i dati sulla spesa pubblica italiana per individuare, grazie all’AI, dove è possibile migliorare l’efficienza e l’utilizzo delle risorse pubbliche.
- 链接: https://github.com/Italian-Builders-Org/DoveVannoINostriSoldi
- ⭐ 36 | 🍴 1 | 语言: TypeScript

### drop-code
- 描述: A warm, drop-down AI coding terminal for macOS.
- 链接: https://github.com/R44VC0RP/drop-code
- ⭐ 34 | 🍴 5 | 语言: Swift

### awesome-grok-bot
- 描述: Curated bilingual list of Grok Bot resources — always-on AI teammates with their own cloud computer.
- 链接: https://github.com/RongleCat/awesome-grok-bot
- ⭐ 31 | 🍴 1 | 语言: Python
- 标签: awesome, awesome-list, cursor, grok-bot, xai

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82568 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36416 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，提供直观的图形化界面，帮助用户查看和调试模型结构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Core ML、Keras 等
- 提供交互式图形界面，可展开查看网络各层详细信息
- 支持模型图的结构化展示，便于理解数据流向
- 可在浏览器或桌面环境中运行，使用便捷
- 兼容 safetensors、TensorFlow Lite 等新兴格式

### 3. 适用场景
- 模型调试：检查神经网络结构是否正确，排查层连接问题
- 模型转换验证：对比不同框架间模型转换后的结构一致性
- 论文展示：生成清晰的网络结构图用于学术报告或演示
- 模型学习：帮助初学者理解各种深度学习模型架构

### 4. 技术亮点
- **多格式广泛支持**：覆盖主流 AI 框架，是同类工具中兼容性最强的之一
- **零依赖运行**：无需安装 TensorFlow/PyTorch 等重型框架即可查看模型
- **开源免费**：MIT 许可证，社区活跃，星标数超过 3.3 万
- **跨平台**：支持 Web、Windows、macOS、Linux 多端使用
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33371 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开放标准，旨在实现机器学习模型在不同框架之间的互操作性。它允许开发者在不同深度学习平台之间无缝迁移模型，打破了框架间的壁垒。

### 2. 核心功能
- **跨框架模型转换**：支持将模型从PyTorch、TensorFlow、Keras等框架转换为ONNX格式
- **统一模型表示**：提供标准化的模型定义格式，确保模型在不同环境中的一致性
- **推理引擎兼容**：可与ONNX Runtime等推理引擎配合使用，实现高效的模型推理
- **生态系统集成**：与Scikit-learn等机器学习库集成，扩大适用范围
- **部署灵活性**：支持将模型部署到移动端、嵌入式设备等多种平台

### 3. 适用场景
- **模型迁移**：将训练好的模型从一个框架迁移到另一个框架进行部署
- **生产环境部署**：将深度学习模型部署到资源受限的边缘设备或移动端
- **多框架协作**：在团队中使用不同框架时，通过ONNX实现模型共享
- **性能优化**：利用ONNX Runtime等优化工具提升模型推理速度

### 4. 技术亮点
- **开源社区支持**：由Microsoft、Facebook等科技巨头共同维护，社区活跃
- **广泛的框架支持**：兼容主流深度学习框架，生态覆盖全面
- **高性能推理**：ONNX Runtime提供跨平台的高性能推理能力
- **模型优化能力**：支持图优化、算子融合等性能优化技术
- 链接: https://github.com/onnx/onnx
- ⭐ 21337 | 🍴 4004 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

### 1. 中文简介

《机器学习工程开源手册》是一本全面覆盖机器学习工程实践的开源参考书。内容涵盖从模型训练、调试到部署推理的全流程，是MLOps和LLM工程领域的实用指南。

### 2. 核心功能

- 系统讲解大语言模型（LLM）的训练与微调方法
- 深入介绍GPU优化、分布式训练及推理加速技术
- 提供基于PyTorch和Transformers框架的工程实践指导
- 涵盖可扩展性设计、存储优化和网络配置等运维要点
- 集成Slurm集群调度与MLOps最佳实践

### 3. 适用场景

- 研究人员和工程师进行大规模LLM训练时的工程参考
- MLOps团队搭建模型训练和推理基础设施
- 需要优化GPU资源利用率和训练效率的工程团队
- 学习分布式训练和模型部署的开发者

### 4. 技术亮点

- 内容覆盖AI工程全链路，从底层硬件（GPU/网络/存储）到上层应用（推理/微调）
- 紧密结合PyTorch和Hugging Face Transformers生态，实用性强
- 开源社区活跃，星标数近1.9万，具有较高的参考价值和社区认可度
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18668 | 🍴 1202 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17378 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13272 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11630 | 🍴 916 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10690 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36416 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具。它支持多种主流框架的模型格式，提供直观的图形化界面，帮助用户查看和调试模型结构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Core ML、Keras 等
- 提供交互式图形界面，可展开查看网络各层详细信息
- 支持模型图的结构化展示，便于理解数据流向
- 可在浏览器或桌面环境中运行，使用便捷
- 兼容 safetensors、TensorFlow Lite 等新兴格式

### 3. 适用场景
- 模型调试：检查神经网络结构是否正确，排查层连接问题
- 模型转换验证：对比不同框架间模型转换后的结构一致性
- 论文展示：生成清晰的网络结构图用于学术报告或演示
- 模型学习：帮助初学者理解各种深度学习模型架构

### 4. 技术亮点
- **多格式广泛支持**：覆盖主流 AI 框架，是同类工具中兼容性最强的之一
- **零依赖运行**：无需安装 TensorFlow/PyTorch 等重型框架即可查看模型
- **开源免费**：MIT 许可证，社区活跃，星标数超过 3.3 万
- **跨平台**：支持 Web、Windows、macOS、Linux 多端使用
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33371 | 🍴 3171 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## 项目分析：cheatsheets-ai

### 1. 中文简介
本项目为深度学习与机器学习研究者提供了一套必备速查手册。内容涵盖人工智能、机器学习及深度学习领域的常用公式、代码片段和概念总结，方便研究者快速查阅和复习关键知识点。

### 2. 核心功能
- 提供机器学习与深度学习领域的速查表集合
- 涵盖 Keras、NumPy、SciPy、Matplotlib 等常用工具的使用示例
- 总结深度学习研究中的核心概念与公式
- 内容结构清晰，便于快速检索和学习

### 3. 适用场景
- 深度学习/机器学习研究者快速回顾核心概念与公式
- 算法工程师日常开发中的代码参考
- 学生备考或复习机器学习相关知识点
- 技术分享与团队内部知识沉淀

### 4. 技术亮点
- 星标数高达 15428，说明项目在社区中广受欢迎
- 标签覆盖全面，包含 AI、深度学习、Keras、NumPy、SciPy、Matplotlib 等核心技术栈
- 内容实用性强，适合不同层次的研究者和开发者查阅
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

---

### 1. 中文简介

Ai-Learn 是一个系统化的人工智能学习路线图项目，整理收录了近200个实战案例与项目，并提供免费的配套教材。该项目面向零基础学习者，涵盖从Python编程到就业实战的全流程，助力学习者系统掌握AI核心技术。

---

### 2. 核心功能

- 提供完整的人工智能学习路径规划，从入门到就业全覆盖
- 收录近200个实战案例与项目，配套免费教材
- 涵盖Python、数学、机器学习、深度学习、数据分析、NLP、CV等热门技术栈
- 支持多种主流框架（PyTorch、TensorFlow、Keras、Caffe等）的系统学习
- 适合零基础入门，同时兼顾就业实战需求

---

### 3. 适用场景

- 想系统学习人工智能的零基础初学者规划学习路径
- 希望掌握机器学习/深度学习实战技能的开发者
- 准备从事AI相关岗位的求职者，需要项目经验积累
- 需要参考资料学习Python数据分析与可视化的学习者

---

### 4. 技术亮点

- 项目按技术栈分类清晰，覆盖算法、数学、数据处理、深度学习等完整知识体系
- 提供大量实战案例，理论与实践结合紧密
- 星标数超过13000，说明社区认可度高，资料质量有保障
- 免费开源，配套教材完整，降低学习门槛
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13272 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码框架，用于构建自定义大型语言模型（LLM）、神经网络及其他 AI 模型。它降低了深度学习模型的构建门槛，让开发者无需编写大量代码即可完成模型训练与微调。

### 2. 核心功能
- **低代码模型构建**：通过声明式配置快速搭建神经网络和 LLM，无需手写大量代码
- **多模态支持**：支持计算机视觉、自然语言处理等多种数据类型
- **模型微调**：提供便捷的微调功能，可基于 Llama、Mistral 等开源模型进行定制
- **数据驱动训练**：以数据为中心的设计理念，简化数据处理和模型训练流程
- **PyTorch 生态集成**：基于 PyTorch 构建，兼容主流深度学习工具链

### 3. 适用场景
- 快速原型开发：需要快速验证 AI 模型想法，不想编写繁琐的训练代码
- 企业级 LLM 微调：基于开源模型（如 Llama、Mistral）进行领域适配
- 多模态应用开发：同时处理文本、图像等多种类型数据的项目
- 数据科学团队：希望用更低代码量完成深度学习模型训练的数据科学家

### 4. 技术亮点
- 低代码架构显著降低深度学习开发门槛，提升开发效率
- 对主流 LLM（Llama、Mistral）的原生支持，简化微调流程
- 多模态统一框架，一套代码可处理文本、图像等多种数据
- 与 PyTorch 生态无缝集成，便于扩展和部署
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9178 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8967 | 🍴 3110 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6989 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6418 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82568 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持 100 多种大语言模型（LLM）和视觉语言模型（VLM）的微调，相关研究成果已发表于 ACL 2024。该项目旨在为研究者与开发者提供一站式模型微调解决方案，大幅降低大模型微调的技术门槛。

### 2. 核心功能
- **多模型支持**：兼容 Llama、Qwen、DeepSeek、Gemma、GPT 等 100+ 种主流大模型与视觉语言模型。
- **高效微调方法**：内置 LoRA、QLoRA、全参微调等多种参数高效微调（PEFT）策略。
- **指令微调与 RLHF**：支持指令微调（Instruction Tuning）及基于人类反馈的强化学习（RLHF）训练。
- **量化部署友好**：提供量化微调能力，便于在资源受限环境下部署大模型。
- **MoE 架构支持**：兼容 Mixture of Experts（混合专家）模型架构的微调。

### 3. 适用场景
- **企业级模型定制**：基于开源大模型（如 Llama、Qwen）针对特定业务场景进行指令微调。
- **多模态应用开发**：对视觉语言模型（VLM）进行微调，实现图文理解与生成能力。
- **科研与学术实验**：快速复现微调算法，支持 LoRA/QLoRA/RLHF 等多种实验配置。
- **低资源微调部署**：利用 QLoRA 和量化技术在消费级 GPU 上高效微调大模型。

### 4. 技术亮点
- **统一训练框架**：基于 Hugging Face Transformers 构建，一套代码支持多模型、多任务微调，无需重复编写训练脚本。
- **ACL 2024 学术背书**：研究成果经同行评审发表，方法论严谨可靠。
- **高社区热度**：GitHub 星标数超过 7.4 万，说明其在开源社区中拥有广泛认可度和持续维护。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74257 | 🍴 9080 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的零基础人工智能课程，为期12周、共24课，旨在让所有人都能轻松学习AI。课程采用Jupyter Notebook形式，内容覆盖机器学习、深度学习、计算机视觉、自然语言处理等多个核心领域，适合初学者系统入门。

### 2. 核心功能
- **系统化课程结构**：12周24课，循序渐进地引导学习者掌握AI核心知识
- **交互式学习体验**：基于Jupyter Notebook，边学边练，理论与实践结合
- **涵盖主流AI技术**：包括CNN、RNN、GAN、NLP等深度学习核心主题
- **免费开源资源**：由微软出品，完全免费开放，降低学习门槛

### 3. 适用场景
- **初学者入门**：零基础学习者系统学习人工智能基础知识
- **课堂教学辅助**：教师可作为AI课程的配套教材和实验指导
- **企业培训**：公司可用于员工AI技能的内部培训与提升
- **自学进阶**：个人利用课余时间自主完成AI知识体系搭建

### 4. 技术亮点
- 由微软官方维护，内容质量与权威性有保障
- 标签涵盖ML/DL核心领域，知识体系完整
- 65904+星标，社区认可度高，学习资源与讨论活跃
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65904 | 🍴 12767 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# 项目分析：ai-engineering-from-scratch

## 1. 中文简介
从零开始学习、构建并部署AI工程，最终为他人交付实用项目。该项目提供一套系统化的AI工程课程，涵盖从基础理论到实际落地的完整学习路径。

## 2. 核心功能
- 从零构建AI系统，深入理解底层原理而非仅调用API
- 涵盖大语言模型（LLM）、AI代理、计算机视觉等核心技术
- 支持多种编程语言（Python、Rust、TypeScript），提供多语言实现
- 集成MCP（模型上下文协议）等前沿AI工程实践
- 结合强化学习、群体智能等高级主题，提供完整课程式学习体验

## 3. 适用场景
- AI工程师希望深入理解模型底层机制，提升工程能力
- 学生或转行者需要系统化学习AI工程的实战课程
- 团队希望搭建基于LLM和AI代理的生产级应用
- 研究者想探索群体智能与强化学习的工程化落地

## 4. 技术亮点
- 采用"from-scratch"教学方式，强调手写实现而非黑盒调用
- 多语言支持（Python + Rust + TypeScript），兼顾易用性与性能
- 覆盖MCP、AI代理、群体智能等2024-2025年前沿工程方向
- 高星标数（47367）表明社区认可度高，学习资源丰富
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47367 | 🍴 8330 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：ailearning

### 1. 中文简介
这是一个全面的人工智能学习项目，涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK和TensorFlow 2等内容。项目旨在帮助学习者系统掌握AI相关理论与实践技能。

### 2. 核心功能
- **机器学习算法实战**：包含AdaBoost、Apriori、FP-Growth、KMeans、逻辑回归、朴素贝叶斯、SVM、回归等多种经典算法实现
- **深度学习框架应用**：基于PyTorch和TensorFlow 2的DNN、LSTM、RNN等神经网络模型实践
- **自然语言处理（NLP）**：使用NLTK进行文本处理和NLP任务
- **推荐系统开发**：实现基于协同过滤等方法的推荐算法
- **数据降维与特征提取**：涵盖PCA、SVD等线性代数在数据分析中的应用

### 3. 适用场景
- 机器学习初学者系统学习算法原理与代码实现
- 深度学习入门者实践PyTorch和TensorFlow 2框架
- 数据分析人员提升特征工程与降维技能
- NLP爱好者学习文本处理与自然语言分析

### 4. 技术亮点
- 项目星标数高达**42468**，说明在社区中具有较高的认可度和影响力
- 内容覆盖全面，从线性代数基础到深度学习实战形成完整学习链路
- 结合经典算法（scikit-learn）与现代框架（PyTorch、TF2），兼顾理论基础与工程实践
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42468 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36416 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33836 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29144 | 🍴 3550 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21844 | 🍴 3358 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17378 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI机器学习/深度学习项目合集

### 1. 中文简介
该项目是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目以Awesome列表形式整理，为开发者提供丰富的实战代码资源。

### 2. 核心功能
- 汇集500个完整的AI项目代码，覆盖主流技术方向
- 包含机器学习、深度学习、计算机视觉、NLP四大领域
- 提供可直接运行的Python代码示例
- 采用标签分类，便于快速定位感兴趣的项目
- 持续更新的开源项目集合

### 3. 适用场景
- **学习入门**：适合初学者系统学习AI各领域的实战项目
- **项目参考**：开发者可借鉴代码结构快速搭建自己的项目
- **面试准备**：求职者可通过项目积累实战经验应对技术面试
- **技术调研**：快速了解AI领域热门项目和技术趋势

### 4. 技术亮点
- 高星标量（36416+）证明社区认可度极高
- 覆盖AI全栈技术方向，从传统ML到前沿深度学习
- 全部项目附带完整代码，可直接运行学习
- 分类清晰，便于按需查找特定领域项目
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36416 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介
Skyvern 是一款基于人工智能的浏览器工作流自动化工具。它利用计算机视觉和大型语言模型（LLM）技术，能够自主操作浏览器完成各类重复性任务，无需手动编写复杂的自动化脚本。

## 2. 核心功能
- 基于视觉理解的浏览器自动化，无需依赖DOM元素定位
- 支持多种LLM后端（如GPT-4），智能决策操作步骤
- 提供API接口，便于集成到现有工作流中
- 兼容主流浏览器自动化工具（Playwright、Puppeteer、Selenium）
- 支持录制和回放浏览器操作，降低自动化开发门槛

## 3. 适用场景
- 企业RPA（机器人流程自动化）：自动化填写表单、数据录入等重复性工作
- 网页数据抓取：从复杂网站提取结构化数据
- 跨平台工作流集成：替代或补充Microsoft Power Automate等商业工具
- 测试自动化：自动执行浏览器端到端测试用例

## 4. 技术亮点
- 采用"视觉+LLM"双驱动架构，模拟人类浏览器操作方式
- 支持多步骤复杂工作流的自主执行与错误恢复
- 开源免费，Python生态友好，社区活跃（22806+星标）
- 兼容现有浏览器自动化工具链，便于渐进式迁移
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22806 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，提供开源、云端和企业级产品以及标注服务。支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作、数据分析及开发者API。

## 2. 核心功能
- 支持图像、视频和3D数据的标注，涵盖边界框、语义分割等多种标注类型
- 提供AI辅助标注功能，可显著提升标注效率
- 内置质量保证机制和团队协作能力，适合多人协作项目
- 开放开发者API，便于集成到现有工作流中
- 提供开源版、云端版和企业版多种部署选项

## 3. 适用场景
- 深度学习模型训练前的数据集标注与预处理
- 计算机视觉项目中的图像分类、目标检测和语义分割任务
- 团队协作的大规模视觉数据集构建项目
- 需要AI辅助加速标注流程的企业级应用

## 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）的模型集成
- 具备智能插值功能，可减少视频标注工作量
- 提供完整的数据分析仪表板，支持标注质量统计
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16557 | 🍴 3809 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

---

## 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，支持多种深度学习模型的任务可视化。该库兼容CNN、Vision Transformer等架构，涵盖分类、目标检测、分割及图像相似度等多种应用场景。

## 2. 核心功能
- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种可视化算法实现
- 兼容PyTorch框架下的CNN和Vision Transformer模型
- 提供图像分类、目标检测、语义分割等多种任务的解释性分析
- 支持图像相似度计算的可视化解释
- 内置丰富的可视化输出功能，便于结果展示与分析

## 3. 适用场景
- 深度学习模型的可解释性研究与调试，帮助理解模型决策依据
- 计算机视觉任务的结果可视化，如定位图像中的关键区域
- 学术研究与论文撰写中的可视化素材生成
- 工业应用中模型可信度评估与故障排查

## 4. 技术亮点
- 项目星标数超过12,900，是PyTorch生态中最受欢迎的可解释性工具之一
- 统一封装多种CAM变体算法，简化多方法对比实验流程
- 对Vision Transformer等前沿架构提供支持，紧跟技术发展趋势
- 代码结构清晰，API设计简洁，易于集成到现有项目中
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12953 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间智能的几何计算机视觉库，专为深度学习研究而设计。它基于 PyTorch 构建，提供了一套可微分的计算机视觉算子和工具，使研究人员能够轻松地将传统几何视觉方法融入神经网络中。

### 2. 核心功能
- 提供丰富的**可微分几何视觉算子**，支持梯度反向传播
- 内置多种**图像变换与增强**操作，适配深度学习训练流程
- 支持**3D视觉任务**，包括相机标定、点云处理和三维重建
- 集成**鲁棒几何估计**算法，如RANSAC、PnP求解器等
- 与 PyTorch 生态无缝对接，支持 GPU 加速和批量处理

### 3. 适用场景
- **机器人视觉导航**：用于SLAM、视觉伺服和空间定位
- **自动驾驶感知**：支持多视图几何和三维场景理解
- **图像配准与拼接**：适用于全景图生成和医学影像对齐
- **深度学习视觉研究**：为可微分几何建模提供底层支持

### 4. 技术亮点
- **完全可微分设计**：所有算子支持 PyTorch 自动求导，便于端到端训练
- **硬件加速**：充分利用 GPU 并行计算，显著提升处理效率
- **模块化架构**：算子设计灵活，可轻松集成到现有模型中
- **活跃社区**：星标数超 11000，持续维护并支持 Hacktoberfest 等开源活动
- 链接: https://github.com/kornia/kornia
- ⭐ 11317 | 🍴 1226 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3481 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3386 | 🍴 415 | 语言: Python
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

OpenClaw 是一款个人 AI 助手工具，支持任意操作系统和平台，让你以"龙虾方式"完全掌控自己的数据。这是一个开源、跨平台、数据自主的 AI 助手解决方案。

### 2. 核心功能

- **跨平台支持**：兼容任意操作系统和平台，灵活部署
- **个人 AI 助手**：提供智能化的个人助理功能
- **数据自主可控**：用户完全掌握自己的数据，无需依赖第三方云服务
- **开源项目**：基于 TypeScript 开发，社区活跃（近 39 万星标）

### 3. 适用场景

- 需要本地部署 AI 助手、注重数据隐私的用户
- 希望在多平台（Windows/Mac/Linux）统一使用 AI 助手的开发者
- 追求数据自主、不想将个人信息上传到云端的用户

### 4. 技术亮点

- 使用 TypeScript 开发，类型安全且生态丰富
- 强调"Own Your Data"理念，数据完全本地化处理
- 社区热度极高（38万+ 星标），表明项目受到广泛认可

---

**总结**：OpenClaw 是一个面向隐私保护用户的跨平台个人 AI 助手，适合注重数据主权的技术用户和开发者。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386909 | 🍴 81277 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# Superpowers 项目分析

## 1. 中文简介
Superpowers 是一个实用的 AI 代理技能框架与软件开发方法论，专为提升开发效率而设计。它通过子代理驱动的开发模式，帮助开发者完成从头脑风暴到代码实现的完整流程。

## 2. 核心功能
- **AI 代理技能框架**：提供可复用的模块化技能系统，支持灵活的 AI 协作开发。
- **子代理驱动开发**：通过多个子代理协同工作，实现任务分解与并行处理。
- **头脑风暴与创意生成**：内置 AI 辅助的创意构思工具，帮助快速生成项目想法。
- **完整 SDLC 支持**：覆盖软件开发生命周期各阶段，从需求分析到代码交付。
- **Shell 脚本驱动**：基于 Shell 实现，轻量级部署且易于集成现有工作流。

## 3. 适用场景
- 团队协作中的 AI 辅助编程与代码审查。
- 快速原型开发与创意验证项目。
- 需要自动化流程管理的复杂软件开发项目。
- 希望提升开发效率的个人开发者或小型团队。

## 4. 技术亮点
- 高社区认可度（近 27.5 万星标），证明其广泛影响力。
- 轻量级 Shell 实现，无需复杂依赖即可快速上手。
- 模块化技能架构，支持自定义扩展与二次开发。
- 链接: https://github.com/obra/superpowers
- ⭐ 274926 | 🍴 24604 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# Hermes-Agent 项目分析

## 1. 中文简介
Hermes-Agent 是一个能够伴随用户共同成长的人工智能智能体。它支持多种大语言模型（包括 Claude、GPT 等），可根据用户的使用习惯和反馈持续优化，提供个性化的智能助手体验。

## 2. 核心功能
- 支持多模型集成，兼容 Claude、GPT 等多种大语言模型
- 具备上下文记忆能力，能够记住用户偏好和历史交互
- 提供灵活的自定义配置，用户可根据需求调整智能体行为
- 支持代码执行和文件操作，具备实际任务处理能力
- 开源可部署，用户可自行托管和控制数据隐私

## 3. 适用场景
- **个人编程助手**：辅助开发者编写、调试和优化代码
- **日常知识问答**：作为智能对话伙伴，解答各类问题
- **自动化任务执行**：处理文件管理、数据整理等重复性工作
- **个性化学习伙伴**：根据用户学习进度提供定制化指导

## 4. 技术亮点
- 采用 Nous Research 的 Hermes 模型系列，在代码和推理任务上表现优异
- 支持本地部署，保障数据隐私安全
- 架构灵活，可无缝对接 Anthropic 和 OpenAI 等主流 API
- 社区活跃，星标数超过 23 万，说明具有较高的认可度和使用规模
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233533 | 🍴 46796 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201376 | 🍴 60249 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建AI工具，实现AI的普及化愿景。我们的使命是提供完善的工具链，让您能够专注于真正重要的事务。

## 2. 核心功能
- 基于大语言模型的自主代理系统，能够自动规划并执行复杂任务
- 支持多种AI模型后端，包括OpenAI、Claude、Llama等主流LLM
- 提供完整的工具链和扩展接口，便于开发者自定义和集成
- 具备任务分解与自主执行能力，无需人工逐步干预
- 开源可定制，支持用户根据自身需求进行二次开发

## 3. 适用场景
- **自动化工作流**：将重复性任务（如数据收集、报告生成）交给AI自动完成
- **研究与信息整合**：自动搜索、整理和分析大量信息并输出总结
- **代码开发与调试**：辅助完成编程任务、代码审查和Bug修复
- **个人助手**：作为智能助手处理日常事务，如日程管理、邮件处理等

## 4. 技术亮点
- 支持多模型切换，兼容OpenAI、Claude、Llama API等多种后端
- 采用Agent架构设计，具备目标分解、自我反思和工具调用能力
- 高度可扩展，允许开发者自定义工具和集成第三方服务
- 社区活跃，星标数超过18万，生态完善且持续迭代
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186688 | 🍴 46046 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 170091 | 🍴 9473 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167650 | 🍴 21644 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164588 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157909 | 🍴 46170 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153513 | 🍴 9900 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

