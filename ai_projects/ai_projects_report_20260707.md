# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### TokHub
- ### TokHub 项目分析报告

**1. 中文简介**
TokHub 是一个基于 OpenAI 兼容协议的专属 API 网关系统，集成了中转站监控、推荐运营及自动化管理功能。它支持 Docker 自托管部署，具备分层探测、健康评分、用量计量以及告警审计等核心能力。

**2. 核心功能**
*   **OpenAI 兼容网关**：提供标准化的 API 接口，无缝对接主流大模型应用。
*   **智能监控与健康评估**：通过分层探测机制实时监测 API 状态并生成健康评分。
*   **精细化用量计量**：精确统计各节点或用户的 API 调用次数与资源消耗。
*   **告警与审计体系**：内置实时监控告警及完整的操作审计日志，保障服务稳定性。
*   **Docker 自托管**：支持一键容器化部署，便于用户私有化搭建和管理。

**3. 适用场景**
*   **API 聚合服务商**：用于管理和分发多个 AI 提供商的接口，实现负载均衡与故障转移。
*   **企业内部 AI 中台**：为内部团队提供统一、安全且可审计的大模型访问入口。
*   **个人开发者/小型团队**：低成本自建 OpenAI 兼容网关，避免直接依赖第三方商业平台。
*   **高可用架构部署**：需要实时监控接口健康度并自动切换备用源的场景。

**4. 技术亮点**
*   **分层探测机制**：区别于简单的 Ping 检测，提供更细粒度的接口可用性验证。
*   **全链路审计能力**：结合用量计量与告警，实现了从调用到计费/监控的闭环管理。
*   **轻量级自托管架构**：基于 TypeScript 开发并支持 Docker，部署简便且资源占用低。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 109 | 🍴 13 | 语言: TypeScript

### OpenAI4S
- 描述: 9.9 元豆包API复刻 Claude Science
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 62 | 🍴 6 | 语言: Python

### Autonomous-Forge
- **1. 中文简介**
Autonomous-Forge 是一个完全由人工智能构建和维护的自动化项目，能够持续进行自我规划、编码、测试及优化。该项目展示了AI在软件工程全生命周期中的自主闭环能力，实现了从开发到改进的自动化迭代。

**2. 核心功能**
*   **全自动构建与维护**：项目代码完全由AI生成并持续维护，无需人工干预。
*   **自我规划能力**：具备自动制定开发计划和优化路径的功能。
*   **持续代码生成**：根据规划自动生成或重构代码，实现功能的迭代。
*   **自动化测试与改进**：内置测试流程以验证代码质量，并基于结果自我优化。

**3. 适用场景**
*   **AI驱动的开发研究**：用于探索和研究大型语言模型在软件工程中的应用边界。
*   **自动化工作流原型**：作为构建端到端AI自动化开发管道的参考案例。
*   **自我演进系统实验**：测试软件系统在不依赖人类开发者的情况下进行自我维护和升级的能力。

**4. 技术亮点**
*   实现了“规划-编码-测试-改进”的完整AI自主闭环逻辑。
*   证明了Python环境下AI独立维护复杂项目代码库的可行性。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 55 | 🍴 1 | 语言: Python

### TripStar-Java
- 1. **中文简介**
   TripStar-Java 是基于 Spring Boot 与 Spring AI Alibaba ReactAgent 构建的 AI 旅行规划后端服务。该项目集成了高德地图工具与小红书内容数据，并支持结构化输出功能，旨在提供智能化的旅行路线规划体验。

2. **核心功能**
   - 基于 ReactAgent 架构实现智能旅行规划逻辑。
   - 集成高德地图 API 以获取地理位置及相关服务信息。
   - 接入小红书内容数据，丰富旅行推荐与景点资讯。
   - 支持结构化输出（Structured Output），便于前端解析与展示。
   - 采用 Spring AI Alibaba 框架简化 AI 模型调用流程。

3. **适用场景**
   - 开发个性化的智能旅行助手或行程规划应用。
   - 构建结合社交媒体内容（如小红书）的旅游推荐系统。
   - 研究或原型验证基于大模型的 Agent 在垂直领域的应用。
   - 为旅游平台提供后端 AI 驱动的服务接口。

4. **技术亮点**
   - 利用 Spring AI Alibaba 的 ReactAgent 模式实现多轮推理与工具调用。
   - 融合高德地图（空间数据）与小红书（社交内容）形成多维数据支撑。
   - 通过结构化输出确保 AI 生成结果的可编程性与稳定性。
- 链接: https://github.com/LeeFly-cn/TripStar-Java
- ⭐ 25 | 🍴 2 | 语言: JavaScript
- 标签: ai-agent, amap, java, react-agent, spring-ai

### C-SSH
- 描述: Native cross-platform SSH ops: persistent tmux sessions × always-on monitoring × built-in AI assistant. Windows/Android, free forever, open-source soon. 原生跨平台 SSH 运维 · tmux 持久化 · 常驻监控 · 内置 AI 助手
- 链接: https://github.com/suiyuebaobao/C-SSH
- ⭐ 23 | 🍴 3 | 语言: 未知
- 标签: ai, ai-assistant, android, cross-platform, devops

### fable5-methodology
- 描述: A transferable, self-enforcing software-engineering methodology for AI coding agents — playbook, skills, contracted subagents, lifecycle hooks, and evals.
- 链接: https://github.com/UnpaidAttention/fable5-methodology
- ⭐ 18 | 🍴 8 | 语言: Shell

### glm-5.2-free-desktop-app
- 描述: glm-5.2 free z.ai z-ai open source open-weights mit license mixture of experts moe artificial intelligence large language model 1m context window api key zenmux openrouter chat.z.ai browser interface coding agent claude code setup guide tutorial download documentation github huggingface benchmark performance terminal-bench
- 链接: https://github.com/zai-project/glm-5.2-free-desktop-app
- ⭐ 18 | 🍴 0 | 语言: C#
- 标签: ai-api-free, anthropic-, anthropic-claude, anthropic-outcomes, anthropic-sdk

### cf-proxy
- 描述: OpenAI-compatible Cloudflare Workers AI proxy with account-pool rotation and neuron tracking
- 链接: https://github.com/waguriagentic/cf-proxy
- ⭐ 16 | 🍴 11 | 语言: JavaScript

### REM-AIO
- 描述: 无描述
- 链接: https://github.com/devrock07/REM-AIO
- ⭐ 13 | 🍴 2 | 语言: Python

### retok
- 描述: Token-efficiency analyzer for AI coding agents (Claude Code, OpenAI Codex CLI): cost estimates, cache analysis, and savings advice. Zero dependencies.
- 链接: https://github.com/d-date/retok
- ⭐ 13 | 🍴 0 | 语言: Python
- 标签: ai-agents, anthropic, claude, claude-code, cli

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81645 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35230 | 🍴 7330 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33189 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21109 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ML Engineering Open Book》是一本关于机器学习工程实践的开源指南。它全面涵盖了从基础设施配置到模型训练及部署的全流程技术细节。该项目旨在帮助工程师构建可扩展且高效的机器学习系统。

2. **核心功能**
*   提供大规模分布式训练的最佳实践与故障排除指南。
*   深入解析GPU集群管理、网络通信及存储优化策略。
*   涵盖大语言模型（LLM）的推理加速、微调及部署技巧。
*   包含基于PyTorch和Transformers库的工程化实现示例。
*   介绍使用Slurm等作业调度器管理计算资源的方法。

3. **适用场景**
*   需要在多GPU或多节点环境下训练大型深度学习模型。
*   面临LLM推理延迟高或吞吐量低的问题，需进行性能优化。
*   搭建和维护企业级机器学习平台（MLOps）的基础设施。
*   调试复杂的分布式训练错误及硬件资源瓶颈。

4. **技术亮点**
*   聚焦于生产环境中的实际工程挑战而非仅理论算法。
*   内容紧跟当前大模型时代的技术栈，特别是LLM相关实践。
*   结合了底层硬件知识（如RDMA网络、NVLink）与上层框架应用。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18253 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17265 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13111 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11560 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5706 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码库合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它通过提供完整的代码示例，帮助开发者快速上手并实践各类前沿人工智能技术。

2. **核心功能**
- 收录500个精选AI项目，覆盖从基础机器学习到高级深度学习的完整知识体系。
- 包含计算机视觉、NLP和通用机器学习三大领域的具体实现代码。
- 提供可直接运行的Python代码示例，便于用户进行本地实验和调试。
- 作为“Awesome”列表， curated 了高质量且具代表性的开源AI项目。

3. **适用场景**
- 初学者入门学习，通过阅读和运行代码理解AI算法原理。
- 开发者寻找灵感或参考模板，快速构建特定领域（如CV或NLP）的原型。
- 研究人员或学生需要大量案例来验证理论或对比不同模型的效果。

4. **技术亮点**
- 项目规模庞大且分类清晰，一站式解决多领域AI学习需求。
- 强调实战性，所有项目均附带代码，降低学习门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35230 | 🍴 7330 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33189 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习和机器学习研究人员提供了必备的速查表（Cheat Sheets）。内容源自 Medium 上的专业文章，旨在帮助研究者快速回顾关键概念与代码实现。

2. **核心功能**
- 汇总深度学习与机器学习领域的核心知识点。
- 提供针对 Keras、NumPy、SciPy 和 Matplotlib 等常用库的代码示例。
- 整理便于查阅的技术术语与算法公式。
- 作为研究人员的快速参考指南，提升开发效率。

3. **适用场景**
- 深度学习模型开发前的快速复习与知识检索。
- 调试代码时参考 NumPy、SciPy 或 Matplotlib 的具体用法。
- 机器学习面试准备或学术研究中快速查阅基础理论。

4. **技术亮点**
- 高度聚焦于科研与工程实践中的高频痛点，内容精炼实用。
- 整合了主流 AI 框架（如 Keras）与科学计算库（如 NumPy/SciPy）的最佳实践。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13111 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8919 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6227 | 🍴 735 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且实用的中文自然语言处理（NLP）工具包，涵盖了从基础的分词、词性标注到高级的语义分析和知识图谱构建。它集成了丰富的中文语料库、词典资源以及基于深度学习（如BERT、GPT）的预训练模型，旨在为开发者提供一站式的NLP解决方案。

**2. 核心功能**
*   **基础文本处理**：支持中英文敏感词检测、语言检测、繁简体转换、中文分词、词性标注及命名实体识别（NER）。
*   **丰富语料与词典资源**：内置大量中文专用库，包括中日文人名库、停用词、情感词典、行业词库（汽车、医疗、法律等）及古诗词库。
*   **信息抽取与结构化**：提供手机号、身份证、邮箱等正则抽取，以及基于依存句法和BERT的关系抽取、事件三元组抽取和关键词提取。
*   **高级NLP模型与应用**：集成BERT、GPT-2、ALBERT等预训练模型的微调代码，支持文本生成、摘要生成、机器翻译及对话系统构建。
*   **多模态与语音处理**：包含中文OCR识别、ASR语音数据集、语音情感分析及音素对齐工具，拓展至语音与图像文本结合的场景。

**3. 适用场景**
*   **中文智能客服与聊天机器人开发**：利用其中的对话语料、意图识别组件及多轮对话框架快速搭建客服系统。
*   **企业级内容安全审核**：使用敏感词库和情感分析功能，对UGC内容进行自动化过滤和舆情监控。
*   **垂直领域知识图谱构建**：借助医疗、金融等领域的专用词典和关系抽取工具，构建行业特定的知识图谱。
*   **NLP算法研究与教学**：作为学习资源库，提供各类NLP论文解读、基准数据集及主流模型（如BERT-NER）的实现代码。

**4. 技术亮点**
该项目不仅整合了传统的规则引擎和统计模型，还紧跟前沿技术，提供了大量基于Transformer架构（BERT, GPT, ALBERT）的最新中文预训练模型微调示例，实现了从底层数据清洗到上层应用开发的全链路覆盖。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81645 | 🍴 15253 | 语言: Python

### LlamaFactory
- ### LlamaFactory 项目分析

1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目荣获 ACL 2024 会议认可，旨在简化从基础模型到特定领域应用的开发流程。它集成了多种先进的微调技术，为用户提供了灵活且低门槛的模型优化方案。

2. **核心功能**
*   **广泛模型兼容**：支持 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流开源模型的统一微调。
*   **多样化微调算法**：内置全参数微调、LoRA、QLoRA、P-Tuning 等多种高效微调策略及量化技术。
*   **多模态支持**：不仅限于文本，还全面支持视觉语言模型（VLM）的微调与训练。
*   **强化学习对齐**：提供 RLHF（基于人类反馈的强化学习）、DPO 等对齐算法，优化模型输出质量。
*   **低资源部署**：通过 QLoRA 等技术实现显存友好型训练，降低硬件门槛并提高训练效率。

3. **适用场景**
*   **垂直领域适配**：将通用大模型快速微调为医疗、法律、金融等特定行业的专业助手。
*   **指令跟随优化**：提升模型对复杂指令的理解和执行能力，使其更符合用户交互习惯。
*   **多模态应用开发**：训练能够同时理解图像和文本内容的智能系统，如视觉问答或图像描述生成。
*   **个性化内容创作**：针对特定风格或品牌语调调整模型输出，用于营销文案或创意写作辅助。

4. **技术亮点**
*   **统一接口设计**：通过标准化的配置方式屏蔽不同模型架构的差异，极大降低了集成和维护成本。
*   **极致性能优化**：结合 FlashAttention 等底层加速技术与量化方案，显著减少显存占用并加快训练速度。
*   **社区驱动生态**：作为 ACL 2024 认可的开源项目，拥有活跃的社区支持和持续迭代的最新模型兼容性。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73026 | 🍴 8927 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52098 | 🍴 8488 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51824 | 🍴 10464 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42358 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37549 | 🍴 6243 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35230 | 🍴 7330 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33717 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28388 | 🍴 3447 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25840 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域，并提供配套代码。它旨在为开发者提供从基础到进阶的全方位实践案例与参考实现。该项目通过整合多个细分领域的实战项目，帮助学习者快速构建AI技能体系。

2. **核心功能**
- 汇集500个完整的AI相关项目，覆盖主流技术领域。
- 提供每个项目的源代码，支持直接运行与二次开发。
- 分类清晰，按机器学习、深度学习、CV和NLP等标签组织。
- 作为“Awesome List”性质的合集，便于系统性学习与查阅。

3. **适用场景**
- AI初学者希望寻找大量实战案例以巩固理论基础。
- 开发者需要快速参考特定算法或任务的代码实现。
- 教育者或培训师用于设计课程实验和项目作业。
- 研究人员希望快速了解某一子领域的项目现状与技术趋势。

4. **技术亮点**
- 项目规模庞大，内容全面，一站式解决多领域学习需求。
- 标签体系完善，便于用户根据兴趣和技术栈精准筛选。
- 强调“带代码”的实践导向，而非仅停留在理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35230 | 🍴 7330 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22138 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### CVAT 项目分析报告

**1. 中文简介**
计算机视觉标注工具（CVAT）是一个领先的平台，专为构建高质量的视觉AI数据集而设计。它提供开源、云端及企业级产品，支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API等功能。

**2. 核心功能**
*   **多模态数据标注**：支持图像、视频及3D点云数据的自动化与手动标注。
*   **AI辅助标注**：集成人工智能模型以加速标签生成并提高标注效率。
*   **全流程协作管理**：具备质量保证机制、团队任务分配及数据分析能力。
*   **灵活部署模式**：提供开源本地部署、云服务以及企业级定制化解决方案。

**3. 适用场景**
*   **目标检测训练**：为物体检测算法准备带有边界框（Bounding Box）标签的高质量数据集。
*   **语义分割研究**：用于需要像素级分类的深度学习模型（如自动驾驶场景理解）的数据制作。
*   **视频动作分析**：对长视频序列进行关键帧标注，适用于行为识别或视频内容检索项目。

**4. 技术亮点**
*   **生态兼容性强**：原生支持 PyTorch 和 TensorFlow 等主流深度学习框架的数据格式输出。
*   **开发者友好**：提供完善的 API 接口，便于集成到现有的 MLOps 流水线中。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16238 | 🍴 3738 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12901 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11269 | 🍴 1194 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3455 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3272 | 🍴 400 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2622 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2416 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，强调用户对自己数据的完全掌控。它采用 TypeScript 开发，以独特的“龙虾”风格为用户提供私密的智能服务体验。该项目旨在让用户在本地环境中安全、便捷地部署专属 AI 代理。

**2. 核心功能**
*   跨平台兼容：支持在任何主流操作系统上运行，实现无缝接入。
*   数据私有化：确保用户数据完全由个人掌控，保障隐私安全。
*   本地化部署：作为个人 AI 助手，可在本地环境独立运行，无需依赖外部云服务。
*   灵活可扩展：基于 TypeScript 构建，易于集成各类工具和服务。

**3. 适用场景**
*   注重隐私的个人用户，希望在不泄露数据的前提下使用 AI 进行日常问答或任务处理。
*   开发者或技术爱好者，需要在本地搭建可定制、可控制的 AI 辅助工作流。
*   对现有云 AI 服务的数据安全性存疑，寻求自主托管解决方案的企业或个人团队。

**4. 技术亮点**
*   基于 TypeScript 开发，兼具类型安全与开发效率，便于社区贡献和维护。
*   强调“Own Your Data”（拥有你的数据）理念，架构设计优先考虑本地数据主权。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382017 | 🍴 80133 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 248090 | 🍴 22025 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够伴随用户共同成长的智能代理助手。它致力于通过持续的学习与交互，不断优化自身能力以适应用户需求。该项目旨在打造一个高度个性化且进化的 AI 辅助工具。

2. **核心功能**
*   具备自我进化能力，能随使用时间推移积累知识并优化表现。
*   支持多模型集成，兼容 OpenAI、Anthropic 等主流大语言模型。
*   提供灵活的 API 接口，便于开发者进行二次开发和功能扩展。
*   拥有强大的上下文管理能力，确保多轮对话中的连贯性与准确性。

3. **适用场景**
*   个人开发者用于自动化日常编码任务和技术文档查询。
*   企业团队构建专属的智能客服或内部知识库问答系统。
*   研究人员测试不同 LLM 在复杂代理任务中的表现与差异。
*   希望获得长期记忆和个性化定制服务的普通 AI 爱好者。

4. **技术亮点**
*   采用模块化架构设计，支持热插拔不同的大模型后端。
*   内置增量学习机制，允许在不重新训练整体模型的情况下更新特定技能。
*   优化的 Token 管理策略，有效降低长上下文场景下的计算成本。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210584 | 🍴 38599 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个基于公平开源许可的工作流自动化平台，具备原生 AI 能力，支持可视化构建与自定义代码结合的开发模式。它提供超过 400 种集成选项，允许用户选择自托管或云端部署，实现灵活高效的数据流处理。

### 2. 核心功能
*   **可视化工作流构建**：通过拖拽式界面轻松设计复杂业务逻辑，降低自动化门槛。
*   **原生 AI 集成**：内置人工智能功能，支持在工作流中直接调用 LLM 进行智能处理。
*   **广泛集成生态**：提供超过 400 种预置连接器，无缝对接各类 API 和 SaaS 服务。
*   **混合开发模式**：结合低代码/无代码可视化操作与自定义代码编写，满足多样化需求。
*   **灵活部署方式**：支持自托管以保障数据隐私，也提供便捷的云端服务选项。

### 3. 适用场景
*   **企业自动化流程**：自动处理跨系统数据同步、审批流转及通知推送，提升运营效率。
*   **AI 驱动的业务应用**：构建结合大语言模型的工作流，如智能客服、内容生成或数据分析。
*   **开发者工具链集成**：利用 MCP（Model Context Protocol）等协议连接 AI 模型与内部数据源，优化开发体验。

### 4. 技术亮点
*   **公平开源许可 (Fair-code)**：在鼓励社区贡献的同时，对商业竞争行为设有合理限制，平衡开放与可持续开发。
*   **MCP 支持**：原生支持 Model Context Protocol，便于 AI 应用安全地访问数据和工具。
*   **TypeScript 全栈架构**：基于 TypeScript 构建，保证类型安全和代码可维护性，适合复杂逻辑扩展。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195484 | 🍴 59140 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185412 | 🍴 46123 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164975 | 🍴 21358 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164014 | 🍴 30387 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156858 | 🍴 46161 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151272 | 🍴 9456 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147995 | 🍴 23306 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

