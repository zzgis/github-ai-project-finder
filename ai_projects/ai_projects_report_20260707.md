# GitHub AI项目每日发现报告
日期: 2026-07-07

## 新发布的AI项目

### rocketplaneIO
- ### 1. 中文简介
RocketplaneIO 是一款自托管的 AI 站点可靠性工程（SRE）工具，专为 Kubernetes 环境设计。它结合了零侵入式的 eBPF 可观测性与具备安全护栏和自我验证机制的 AI Copilot，能够自动修复发现的问题。支持自带 LLM（BYO-LLM），并具备完全离线（air-gapped）运行的能力。

### 2. 核心功能
*   **零侵入式可观测性**：利用 eBPF 技术收集数据，无需在应用代码中植入任何代理或进行额外配置。
*   **AI 自动化修复**：内置 AI Copilot，通过受控且自我验证的动作自动诊断并修复 Kubernetes 中的问题。
*   **灵活的大模型集成**：支持用户自带大语言模型（BYO-LLM），适应不同隐私和安全需求。
*   **离线部署能力**：完全支持空气间隙（Air-gapped）环境，可在无互联网连接的安全隔离网络中运行。

### 3. 适用场景
*   **高安全要求的环境**：适用于金融、政府等需要严格数据隔离、无法连接公网的 Kubernetes 集群。
*   **追求低开销的可观测性**：适合希望在不修改应用程序代码、不引入额外 Agent 开销的情况下监控 K8s 状态的场景。
*   **智能化运维（AIOps）**：面向希望利用 AI 自动处理常见故障、减少人工介入和平均修复时间（MTTR）的运维团队。

### 4. 技术亮点
*   **eBPF 与 OpenTelemetry 结合**：底层采用高效的 eBPF 技术配合 OpenTelemetry 标准，实现高性能的数据采集与追踪。
*   **Guardrailed（护栏化）AI 动作**：AI 的操作并非黑盒，而是受到严格的安全规则和验证机制约束，确保修复动作不会破坏系统稳定性。
*   **多技术栈融合**：整合了 ClickHouse、PromQL 等成熟的数据存储与查询技术，增强了数据处理和分析能力。
- 链接: https://github.com/olemeyer/rocketplaneIO
- ⭐ 122 | 🍴 0 | 语言: TypeScript
- 标签: ai-agent, aiops, clickhouse, devops, ebpf

### TokHub
- ### 1. **中文简介**
TokHub 是一个基于 OpenAI 协议兼容的专属网关系统，旨在提供 AI API 的中转站监控、推荐运营及全链路管理。它支持分层探测、健康评分、用量计量、告警审计等功能，并允许用户通过 Docker 进行自托管部署。

### 2. **核心功能**
*   **OpenAI 兼容网关**：提供标准的 OpenAI 接口协议，便于无缝接入现有应用。
*   **多层级健康监控**：支持分层探测与健康评分机制，实时评估 API 中转站的可用性。
*   **精细化用量与审计**：具备详细的用量计量、告警触发及安全审计日志记录能力。
*   **运营推荐系统**：内置推荐运营模块，帮助优化 API 路由选择与服务分发。
*   **Docker 自托管**：支持通过 Docker 容器化部署，实现私有化环境下的独立运行与管理。

### 3. **适用场景**
*   **企业私有化部署**：需要数据隐私保护，希望将 AI 服务完全控制在内部网络的企业或机构。
*   **多中转站聚合管理**：同时接入多个第三方 API 提供商，需统一监控其稳定性并进行智能切换的场景。
*   **成本与用量管控**：需要对不同用户或项目的 API 调用量进行精确统计、限额控制及费用审计的开发团队。
*   **高可用架构构建**：要求通过健康检查和自动故障转移来保障 AI 服务连续性的生产环境。

### 4. **技术亮点**
*   **分层探测算法**：通过多级探测策略更精准地识别中转站的真实状态，避免误判。
*   **标准化兼容性**：完全兼容 OpenAI 接口规范，降低了业务系统的迁移和集成成本。
- 链接: https://github.com/yaojingang/TokHub
- ⭐ 116 | 🍴 13 | 语言: TypeScript

### OpenAI4S
- 1. **中文简介**
该项目旨在通过低成本接入豆包 API，复刻并实现类似 Claude Science 的高级科研智能体功能。它利用开源技术为科学研究提供一种经济高效的自动化辅助方案，支持 MIT 开源协议。

2. **核心功能**
*   基于豆包 API 构建具备科研能力的智能代理（Agent）。
*   模拟 Claude Science 的工作流，专注于科学领域的深度分析与研究。
*   支持 Python 环境下的快速部署与二次开发。
*   遵循 MIT 开源协议，允许自由商用和修改代码。

3. **适用场景**
*   科研人员需要低成本自动化处理文献综述或实验数据分析。
*   开发者希望利用高性价比的大模型 API 构建垂直领域的 AI 助手。
*   教育机构或个人研究者寻求开源的科学计算智能体解决方案。

4. **技术亮点**
*   极高的性价比：通过豆包 API 替代昂贵的商业模型接口，大幅降低科研算力成本。
*   轻量级实现：聚焦于 Agent 架构在科学场景下的应用，结构精简易于集成。
- 链接: https://github.com/PKU-YuanGroup/OpenAI4S
- ⭐ 63 | 🍴 6 | 语言: Python
- 标签: agent, ai4science, claude-science, mit-license, open-source

### Autonomous-Forge
- 1. **中文简介**
该项目是一个完全由人工智能构建和维护的自动化仓库，具备持续自我规划、编码、测试及优化的能力。它展示了AI在软件开发全生命周期中的自主迭代潜力。

2. **核心功能**
- 全自动代码生成与项目初始化。
- 持续的自我测试与错误修复机制。
- 基于反馈的自我规划与功能改进。
- 无需人工干预的闭环维护流程。

3. **适用场景**
- 探索和研究AI自主软件工程的前沿应用。
- 作为自动化开发工作流的参考原型或基准。
- 用于测试AI编程模型在复杂项目中的长期稳定性。

4. **技术亮点**
- 实现了从规划到部署的完全无人化AI驱动闭环。
- 链接: https://github.com/OmarH-creator/Autonomous-Forge
- ⭐ 60 | 🍴 1 | 语言: Python

### C-SSH
- 描述: Native cross-platform SSH ops: persistent tmux sessions × always-on monitoring × built-in AI assistant. Windows/Android, free forever, open-source soon. 原生跨平台 SSH 运维 · tmux 持久化 · 常驻监控 · 内置 AI 助手
- 链接: https://github.com/suiyuebaobao/C-SSH
- ⭐ 25 | 🍴 3 | 语言: 未知
- 标签: ai, ai-assistant, android, cross-platform, devops

### TripStar-Java
- 描述: TripStar Java 实现版：基于 Spring Boot 4 + Spring AI Alibaba ReactAgent 的 AI 旅行规划后端，支持高德 Tool、小红书内容接入和 Structured Output。
- 链接: https://github.com/LeeFly-cn/TripStar-Java
- ⭐ 25 | 🍴 2 | 语言: JavaScript
- 标签: ai-agent, amap, java, react-agent, spring-ai

### fable5-methodology
- 描述: A transferable, self-enforcing software-engineering methodology for AI coding agents — playbook, skills, contracted subagents, lifecycle hooks, and evals.
- 链接: https://github.com/UnpaidAttention/fable5-methodology
- ⭐ 19 | 🍴 8 | 语言: Shell

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
- ⭐ 15 | 🍴 2 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81652 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI实战项目的代码库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它提供了完整的源代码，旨在帮助开发者快速掌握相关技术的应用与实现。

2. **核心功能**
*   汇集大量涵盖AI核心领域的端到端实战项目。
*   提供可直接运行的代码示例，降低复现门槛。
*   分类清晰，覆盖从基础机器学习到高级深度学习的完整技术栈。
*   作为学习资源库，展示多种主流算法在实际场景中的应用。

3. **适用场景**
*   AI初学者希望通过大量实例快速上手编程与实践。
*   数据科学家寻找特定算法（如CNN、RNN）的参考实现。
*   开发者在构建新模型时，需要借鉴现有的代码结构和最佳实践。
*   教育机构用于教学演示或布置编程作业。

4. **技术亮点**
*   极高的资源密度，单一仓库即构成一个小型AI项目百科全书。
*   广泛覆盖Python生态下的主流AI框架（如TensorFlow、PyTorch等）。
*   标签体系完善，便于用户根据具体技术方向（如NLP、CV）精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35232 | 🍴 7331 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。

2. **核心功能**
- 支持加载并可视化 TensorFlow、PyTorch、ONNX、Keras 等数十种格式的模型文件。
- 提供直观的层级结构视图和节点详情，清晰展示网络拓扑与参数连接。
- 兼容桌面应用、浏览器插件及命令行工具，实现跨平台便捷访问。
- 允许用户导出模型截图或配置信息，便于文档记录与技术分享。

3. **适用场景**
- 模型调试阶段，用于检查网络层连接错误或维度不匹配问题。
- 技术交流与演示，向非技术人员直观展示深度学习模型架构。
- 模型转换验证，确认从一种框架（如 PyTorch）转换到另一种（如 ONNX）后的结构一致性。

4. **技术亮点**
- 极高的格式兼容性，几乎覆盖当前所有主流 AI 框架的模型标准。
- 轻量级且无需安装复杂环境，基于 Electron 技术实现桌面端快速运行。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33190 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习互操作性的开放标准。它旨在简化模型在框架间的转换，促进不同深度学习平台之间的无缝集成与部署。

2. **核心功能**
*   提供统一的模型表示格式，打破不同深度学习框架间的壁垒。
*   支持在多种硬件平台和推理引擎上高效执行模型推理。
*   允许开发者在不同框架（如PyTorch、TensorFlow）间轻松转换和优化模型。
*   维护开放的生态系统，确保工具链和运行时环境的广泛兼容性。

3. **适用场景**
*   需要将PyTorch或Keras训练的模型部署到非原生支持框架的生产环境中。
*   希望在边缘设备或特定硬件加速器上运行深度学习模型的嵌入式开发场景。
*   需要跨平台协作，且团队使用不同深度学习框架进行模型开发的工程化流程。

4. **技术亮点**
*   作为行业通用的中立标准，极大地降低了模型迁移和部署的复杂性。
*   拥有强大的社区支持和广泛的框架兼容性，是连接训练与推理的关键桥梁。
- 链接: https://github.com/onnx/onnx
- ⭐ 21109 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- **1. 中文简介**
《ML Engineering Open Book》是一本关于机器学习工程实践的开源指南，旨在填补从模型训练到部署落地之间的工程知识空白。该项目深入探讨了大规模机器学习系统的设计与优化，涵盖了从底层硬件资源管理到上层应用部署的全链路技术细节。

**2. 核心功能**
*   提供大语言模型（LLM）的训练、微调及推理优化的详细工程实践指南。
*   深入解析分布式训练中的硬件瓶颈，包括GPU、网络通信和存储I/O的性能调优。
*   涵盖MLOps全流程，涉及数据管理、模型版本控制及生产环境的可扩展性架构设计。
*   提供基于PyTorch和Transformers库的具体代码示例及故障排除（Debugging）技巧。
*   指导如何在Slurm等集群调度系统中高效管理和运行大规模机器学习任务。

**3. 适用场景**
*   **大规模模型训练**：适用于需要构建和优化千亿参数级大语言模型训练流水线的工程师。
*   **高性能推理部署**：适用于希望降低LLM推理延迟并提高吞吐量的后端开发团队。
*   **MLOps基础设施搭建**：适用于正在构建或优化机器学习平台、解决扩展性问题的架构师。
*   **硬件资源优化**：适用于需要深入理解GPU内存管理、网络带宽利用及存储性能以降低成本的数据科学家。

**4. 技术亮点**
该项目以“Open Book”形式呈现，不仅关注算法理论，更侧重于解决实际工程中的痛点（如OOM错误、通信瓶颈），是连接学术研究与工业界落地的权威参考手册。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18257 | 🍴 1158 | 语言: Python
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
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11561 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5706 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码合集，涵盖了机器学习、深度学习、计算机视觉和自然语言处理等核心领域。它提供了丰富的实战案例和完整源代码，旨在帮助开发者快速掌握人工智能技术的实际应用。

2. **核心功能**
- 提供涵盖机器学习、深度学习、CV及NLP等多个领域的500个独立项目示例。
- 所有项目均附带可运行的源代码，便于用户直接学习、复现和二次开发。
- 内容经过精选分类，符合“Awesome”列表标准，结构清晰，易于检索特定算法或任务。
- 主要基于Python语言实现，贴合当前AI开发的主流技术栈。

3. **适用场景**
- AI初学者希望系统性地通过代码实例来理解从基础ML到高级DL的概念差异。
- 数据科学家或工程师在面临具体业务需求时，寻找现成的算法参考或基线模型代码。
- 学生或研究人员用于构建作品集，展示其在计算机视觉或NLP等领域的实际动手能力。

4. **技术亮点**
- 极高的资源密度与覆盖面，一站式整合了主流AI子领域的大量经典与现代项目。
- 强调实战导向，通过“带代码的项目”形式降低理论到实践的门槛，具备极高的学习参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35232 | 🍴 7331 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。

2. **核心功能**
- 支持加载并可视化 TensorFlow、PyTorch、ONNX、Keras 等数十种格式的模型文件。
- 提供直观的层级结构视图和节点详情，清晰展示网络拓扑与参数连接。
- 兼容桌面应用、浏览器插件及命令行工具，实现跨平台便捷访问。
- 允许用户导出模型截图或配置信息，便于文档记录与技术分享。

3. **适用场景**
- 模型调试阶段，用于检查网络层连接错误或维度不匹配问题。
- 技术交流与演示，向非技术人员直观展示深度学习模型架构。
- 模型转换验证，确认从一种框架（如 PyTorch）转换到另一种（如 ONNX）后的结构一致性。

4. **技术亮点**
- 极高的格式兼容性，几乎覆盖当前所有主流 AI 框架的模型标准。
- 轻量级且无需安装复杂环境，基于 Electron 技术实现桌面端快速运行。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33190 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的知识速查表（Cheat Sheets）。内容涵盖从基础理论到高级框架的核心概念与代码示例，旨在帮助研究者快速回顾关键知识点。

2. **核心功能**
*   提供深度学习与机器学习领域的核心概念速查。
*   包含主流工具库（如NumPy、SciPy、Matplotlib）的关键用法指南。
*   集成Keras等深度学习框架的代码片段与操作说明。
*   整理人工智能相关术语与算法的简明解释。

3. **适用场景**
*   研究人员在实验前快速复习核心公式与算法原理。
*   开发者在日常编码中查阅常用数据处理或绘图函数的语法。
*   学生准备面试或考试时，作为系统性的知识梳理资料。
*   团队内部进行技术分享或新人入职培训时的参考资料。

4. **技术亮点**
*   聚焦于“速查”与“备忘”，内容精炼，便于快速检索。
*   覆盖范围广，整合了数据科学栈中多个关键库的最佳实践。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
这是一个免费的人工智能学习路线图项目，整理了近200个实战案例与配套教材，旨在帮助零基础用户入门并实现就业实战。内容涵盖Python、数学基础、机器学习、深度学习以及计算机视觉和自然语言处理等热门技术领域。

2. **核心功能**
*   提供系统化的AI学习路径，从基础到进阶引导学习者逐步掌握技能。
*   收录近200个精选实战案例与项目，强化动手实践能力。
*   免费提供全套配套教材与学习资料，降低学习门槛。
*   覆盖主流AI框架与库，包括TensorFlow、PyTorch、Keras及Pandas等。
*   聚焦就业导向，通过真实场景案例提升求职竞争力。

3. **适用场景**
*   希望从零开始系统学习人工智能技术的初学者。
*   需要大量实战项目练手以巩固理论知识的在校学生或转行者。
*   寻求免费且高质量AI学习资源的技术爱好者。
*   准备进入AI领域求职，需要展示项目经验的求职者。

4. **技术亮点**
*   全面覆盖当前主流的深度学习框架（如PyTorch、TensorFlow 2.x）及数据处理工具链。
*   集成多领域热门技术栈，包括NLP、CV、数据挖掘及可视化库（Matplotlib、Seaborn）。
*   拥有极高的社区认可度（逾1.3万星标），证明了其内容的实用性和广泛影响力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13112 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置方式，让开发者无需编写大量底层代码即可快速训练和部署机器学习模型。

2. **核心功能**
*   支持基于 YAML 配置文件的声明式模型构建，大幅降低开发门槛。
*   内置多种预定义模型架构，涵盖表格数据、文本、图像及音频处理。
*   提供端到端的机器学习流水线，包括数据预处理、训练、评估和预测。
*   兼容主流深度学习框架（如 PyTorch），并支持模型导出以便在生产环境中部署。
*   具备强大的数据可视化与可解释性功能，帮助用户直观理解模型行为。

3. **适用场景**
*   需要快速原型验证或构建传统机器学习模型的数据科学家。
*   希望简化 LLM 微调流程，无需深入底层框架细节的开发团队。
*   处理多模态数据（如结合表格、文本和图像）的企业级 AI 应用开发。
*   追求模型可解释性和数据为中心（Data-Centric）AI 工作流的场景。

4. **技术亮点**
*   采用“数据为中心”的设计理念，强调数据质量对模型性能的关键作用。
*   高度模块化且可扩展，允许用户轻松集成自定义组件或后端引擎。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9119 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8918 | 🍴 3099 | 语言: C++
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
- ⭐ 6227 | 🍴 736 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81652 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目曾入选 ACL 2024 会议，旨在简化从指令调优到强化学习对齐的全流程开发体验。它通过整合多种先进的微调技术，为研究者和企业提供了开箱即用的模型优化解决方案。

2. **核心功能**
*   **多模型兼容**：无缝支持 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种 LLM 和 VLM 的微调。
*   **多样化微调策略**：内置 LoRA、QLoRA、P-Tuning 等多种高效参数微调方法，以及完整的 RLHF 训练流程。
*   **量化加速**：支持 4-bit/8-bit 量化技术，显著降低显存占用并提升训练效率。
*   **一站式平台**：提供 Web UI 界面和命令行工具，覆盖数据预处理、训练、评估到部署的全生命周期。

3. **适用场景**
*   **科研与学术实验**：研究人员需要快速验证不同模型架构或微调算法在特定 NLP 任务上的效果。
*   **企业私有化部署**：企业在有限算力资源下，对开源基座模型进行领域知识注入和指令对齐。
*   **多模态应用开发**：开发者需要对包含图像理解能力的视觉语言模型进行定制化训练以适配具体业务需求。

4. **技术亮点**
*   **统一架构设计**：基于 Transformers 库构建了高度模块化的接口，极大降低了多模型适配的开发成本。
*   **极致性能优化**：通过 QLoRA 和 FlashAttention 等技术，实现了在消费级显卡上微调大型模型的能力。
*   **前沿算法集成**：原生支持 DPO/ORPO 等最新偏好对齐算法，紧跟大模型训练技术前沿。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73027 | 🍴 8926 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- **1. 中文简介**
该项目收集并公开了包括 Anthropic、OpenAI、Google 及 xAI 在内的多家主流 AI 厂商的系统提示词（System Prompts），涵盖了 Claude、ChatGPT、Gemini 等知名模型。内容定期更新，旨在为研究人员和开发者提供关于大语言模型底层指令结构的透明化参考。

**2. 核心功能**
*   提取并整理来自多个头部 AI 提供商的系统提示词原文。
*   覆盖从对话助手到代码生成等多种类型的模型指令集。
*   保持数据的高频更新以反映最新模型版本的策略变化。
*   提供开源的结构化数据，便于进行逆向工程或教学分析。

**3. 适用场景**
*   **提示词工程研究**：分析优秀模型的指令设计模式，优化用户自定义 Prompt 的效果。
*   **AI 安全教育**：了解模型的安全边界和系统级约束，识别潜在的提示注入风险。
*   **教育与学习**：作为生成式 AI 和自然语言处理领域的教学案例，解析模型内部逻辑。

**4. 技术亮点**
*   **多源聚合**：整合了 Anthropic、OpenAI、Google、xAI 等竞争对手的指令数据，具有极高的行业参考价值。
*   **持续维护**：由社区驱动定期更新，确保信息的时效性和准确性。
*   **高关注度**：拥有超过 5 万星标，证明了其在 AI 开发者社区中的广泛影响力。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 52309 | 🍴 8521 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。项目采用Jupyter Notebook形式编写，内容覆盖从基础概念到深度学习等广泛主题，适合零基础的初学者系统学习。

2. **核心功能**
*   提供结构化的12周学习计划，分24个课时循序渐进地讲解AI概念。
*   涵盖机器学习和深度学习的核心技术，包括计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）。
*   使用Jupyter Notebook作为主要教学载体，支持交互式代码演示与即时实验。
*   由微软发起并维护，确保内容的权威性与教育资源的免费开放性。

3. **适用场景**
*   **个人自学**：希望从零开始系统构建人工智能知识体系的编程爱好者或学生。
*   **课堂教学辅助**：教师用于计算机科学或数据科学课程的标准化教材和实验代码。
*   **企业培训入门**：需要快速提升团队对AI基本概念理解的非技术背景员工的基础培训。

4. **技术亮点**
*   内容广度极佳，不仅涵盖传统机器学习，还深入讲解RNN、CNN、GAN等现代深度学习架构。
*   教育设计成熟，通过“24 Lessons”将复杂概念拆解为易于消化的小模块，降低学习门槛。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51828 | 🍴 10469 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数以及 PyTorch 和 TensorFlow 2 等深度学习框架的综合学习资源库。该项目结合了 NLTK 自然语言处理工具与 scikit-learn 等传统算法库，旨在提供从理论基础到代码实现的完整教程。

2. **核心功能**
*   集成传统机器学习算法（如 SVM、K-Means、逻辑回归）与深度学习模型（如 DNN、RNN、LSTM）的代码实现。
*   包含推荐系统、NLP 及矩阵分解（SVD/PCA）等具体场景的实战案例。
*   涵盖 AdaBoost、Apriori、FP-Growth 等经典数据挖掘算法的原理讲解与应用示例。

3. **适用场景**
*   机器学习与深度学习初学者的系统性入门与代码复现练习。
*   需要快速查找并参考特定算法（如聚类或分类）Python 实现的数据科学家。
*   希望深入理解线性代数在 AI 中应用及其与 PyTorch/TensorFlow 结合的学习者。

4. **技术亮点**
*   全面覆盖从传统统计学习到前沿深度学习的知识体系，兼顾理论（线性代数）与实践（多框架代码）。
*   拥有极高的社区认可度（超 4 万星标），是中文互联网上高质量的 AI 开源学习资料之一。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42359 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37559 | 🍴 6245 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35232 | 🍴 7331 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33718 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28391 | 🍴 3447 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25840 | 🍴 2902 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35232 | 🍴 7331 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款利用人工智能自动化基于浏览器的复杂工作流的工具。它通过结合视觉理解与大型语言模型（LLM），能够模拟人类操作来执行各种网页任务，从而替代传统的脚本化自动化方案。

2. **核心功能**
- 基于视觉感知的浏览器自动化，无需依赖固定的 DOM 选择器即可识别页面元素。
- 利用大语言模型理解页面上下文并智能规划多步骤的工作流任务。
- 支持多种主流浏览器自动化引擎（如 Playwright、Puppeteer、Selenium）作为后端驱动。
- 提供 API 接口，便于将 AI 驱动的浏览器操作集成到现有的 RPA 或业务流程中。

3. **适用场景**
- 自动化填写复杂的在线表单或注册流程，尤其是那些动态加载或结构多变的页面。
- 跨平台执行数据抓取和录入任务，例如从不同网站汇总信息并填入内部系统。
- 替代传统 RPA 工具处理非结构化网页交互，如电商比价、库存监控等日常重复性工作。

4. **技术亮点**
- 突破了传统 Selenium 或 Puppeteer 脚本对页面结构强耦合的限制，具备更强的鲁棒性和适应性。
- 将计算机视觉技术与 LLM 推理能力相结合，实现了类似人类“看屏操作”的智能自动化体验。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22140 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉AI数据集的领先平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量控制、团队协作及开发者API等功能。

### 2. **核心功能**
*   支持图像、视频及3D模型的多维度数据标注。
*   集成AI辅助标注功能，显著提升数据处理效率。
*   提供完善的质量保证机制与团队协作工具。
*   开放开发者API，便于系统集成与二次开发。
*   提供数据分析功能，优化数据集管理流程。

### 3. **适用场景**
*   深度学习模型训练所需的大规模图像分类数据集构建。
*   自动驾驶或安防监控领域中的物体检测与语义分割任务。
*   视频内容分析中的目标跟踪与动作识别数据标注。
*   需要高精度3D点云或体素标注的机器人视觉应用。

### 4. **技术亮点**
*   兼容主流深度学习框架（如PyTorch、TensorFlow），无缝对接现有算法生态。
*   提供从开源到企业级的多形态部署方案，满足不同规模团队需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16242 | 🍴 3738 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12901 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理与计算机视觉算法，旨在简化深度学习在视觉任务中的应用。该库强调自动化与可扩展性，支持从基础图像处理到高级几何推理的多种需求。

2. **核心功能**
*   提供全套可微分的计算机视觉算子，便于集成到深度学习模型中。
*   支持几何视觉任务，如相机标定、立体匹配、单目深度估计及姿态估计。
*   内置丰富的图像增强与预处理工具，加速数据加载与模型训练流程。
*   兼容 PyTorch 生态系统，实现张量的高效 GPU 加速计算。
*   包含用于机器人和自动驾驶的高层语义理解模块。

3. **适用场景**
*   需要端到端训练的传统计算机视觉流水线（如可微分水匹配）。
*   机器人导航中的即时定位与地图构建（SLAM）系统开发。
*   自动驾驶领域的深度估计、图像去雾或增强等预处理任务。
*   学术研究中进行几何约束下的神经网络设计与实验。

4. **技术亮点**
*   **全可微分架构**：将传统几何算法转化为可导操作，无缝嵌入梯度下降优化框架。
*   **PyTorch 原生集成**：直接处理 PyTorch 张量，无需复杂的格式转换，提升计算效率。
*   **模块化设计**：从底层像素操作到高层语义特征，提供层次分明且易于扩展的 API 结构。
- 链接: https://github.com/kornia/kornia
- ⭐ 11269 | 🍴 1195 | 语言: Python
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
- ⭐ 2415 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款致力于实现数据自主权的个人 AI 助手，支持跨操作系统和平台运行。它倡导“龙虾哲学”，让用户完全掌控自己的 AI 体验。该项目旨在提供一个安全、私密的智能辅助工具。

2. **核心功能**
- 支持任意操作系统和平台的广泛兼容性。
- 强调数据所有权，确保用户隐私与安全。
- 提供个性化的 AI 助手交互体验。
- 基于 TypeScript 构建，具备良好的可扩展性。
- 拥有活跃的社区标签与生态支持。

3. **适用场景**
- 需要高度定制化且注重隐私的个人开发者或极客。
- 希望在本地或私有云环境中部署 AI 助手的用户。
- 寻求跨平台无缝衔接的智能工作流整合者。
- 对现有主流 AI 服务数据政策不信任的用户群体。

4. **技术亮点**
- 采用 TypeScript 开发，保证类型安全与代码质量。
- 架构设计强调模块化与平台无关性。
- 社区驱动的开源模式促进快速迭代与创新。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382034 | 🍴 80139 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它致力于通过结构化的“智能体驱动开发”模式，提升软件工程的效率与质量。该项目旨在解决传统开发流程中的痛点，提供一套切实可行的 AI 辅助编码方案。

2. **核心功能**
*   提供模块化的智能体技能集，支持灵活组合以应对不同开发任务。
*   采用子智能体驱动开发（Subagent-Driven Development）架构，实现任务的自动化分解与执行。
*   集成头脑风暴与需求分析工具，辅助开发者进行前期创意构思与技术选型。
*   覆盖完整软件开发生命周期（SDLC），从规划到编码提供全流程支持。
*   内置可复用的开发技能库，降低重复劳动并标准化代码生成过程。

3. **适用场景**
*   希望利用 AI 智能体自动化重构或扩展现有代码库的团队。
*   需要系统化引入 AI 辅助编程以提升整体研发效率的企业级项目。
*   在进行复杂系统设计时，依赖 AI 进行头脑风暴和技术可行性分析的场景。
*   探索新型软件开发方法论，尝试从传统编码向智能体协作模式转型的开发人员。

4. **技术亮点**
*   创新性地将“技能”概念引入 AI 开发框架，实现了开发能力的模块化封装。
*   强调方法论的落地性，不仅提供工具，更提供了一套经过实践检验的开发工作流。
- 链接: https://github.com/obra/superpowers
- ⭐ 248229 | 🍴 22025 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的信息，以下是针对 GitHub 项目 **hermes-agent** 的技术分析：

1. **中文简介**
   Hermes Agent 是一款能够伴随用户共同成长、适应个人工作流的智能代理系统。它旨在通过深度集成多种前沿大语言模型，为用户提供个性化且持续进化的 AI 辅助体验。该项目致力于打造一个不仅具备执行能力，更能理解用户意图并随时间优化的智能助手。

2. **核心功能**
   - 支持多模型集成，兼容 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 及 Nous Research 等多个主流 LLM 后端。
   - 具备自我演进能力，能够根据用户的交互历史和工作习惯不断优化其响应策略与行为模式。
   - 提供高度可定制的代理配置，允许用户定义特定的角色设定、工具权限和工作流规则。
   - 实现统一的 API 接口层，屏蔽底层不同 AI 模型的差异，简化开发者的集成与维护成本。

3. **适用场景**
   - **个性化编程助手**：开发者利用其多模型支持和自我学习能力，构建懂自己代码风格和偏好的专属 Codex 或 Claude 代理。
   - **自动化工作流编排**：企业或个人用户通过配置特定工具链，让 Agent 自动处理邮件分类、文档摘要或数据提取等重复性任务。
   - **高级 AI 应用开发**：研究人员或初创团队将其作为基础框架，快速搭建具有长期记忆和上下文理解能力的复杂 AI 应用原型。

4. **技术亮点**
   - **多源模型融合架构**：巧妙整合了从商业闭源模型到开源社区模型（如 MoltBot, ClawdBot）的优势，提供了极高的灵活性和容错率。
   - **动态成长机制**：区别于静态 Prompt 工程，该项目强调 Agent 的“生长”特性，即通过反馈循环实现能力的迭代升级。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 210656 | 🍴 38624 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码结合。用户可选择自托管或使用云服务，并接入 400 多种集成工具，实现高效的数据流转与应用连接。

2. **核心功能**
*   提供可视化工作流编辑器，支持拖拽式界面构建复杂自动化逻辑。
*   内置原生 AI 能力，允许在工作流中直接调用大语言模型进行智能处理。
*   拥有超过 400 种预置集成节点，覆盖主流 API、数据库及 SaaS 服务。
*   支持混合开发模式，既满足低代码/无代码用户需求，也允许通过自定义代码扩展功能。
*   提供灵活部署方案，包括自托管私有化部署及云端托管服务。

3. **适用场景**
*   企业级数据同步与 ETL 流程，自动在不同系统间清洗和转移数据。
*   基于 AI 的智能客服或内容生成自动化，利用 LLM 处理用户输入并生成响应。
*   跨平台业务通知与工作流触发，如收到邮件后自动更新 CRM 记录并发送 Slack 通知。
*   API 中间件集成，快速连接遗留系统与现代化微服务架构。

4. **技术亮点**
*   采用 TypeScript 开发，兼具类型安全与高性能，且开源社区活跃。
*   原生支持 MCP（Model Context Protocol），便于与各类 AI 模型无缝交互。
*   基于“公平代码”许可协议，在保持开放性的同时保障开发者权益。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195495 | 🍴 59139 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 基于您提供的信息，以下是对 GitHub 项目 **AutoGPT** 的技术分析：

1. **中文简介**
   AutoGPT 旨在让每个人都能轻松使用并构建基于人工智能的工具，实现 AI 的普及化愿景。其使命是提供强大的基础设施，使用户能够专注于核心业务逻辑而非底层技术细节。

2. **核心功能**
   - 支持自主代理（Autonomous Agents），能够独立规划并执行复杂的多步骤任务。
   - 兼容多种大型语言模型（LLM），包括 OpenAI GPT、Anthropic Claude 及 Llama API 等。
   - 提供高度可扩展的架构，允许开发者基于现有工具进行二次开发和定制。
   - 具备自然语言交互能力，用户可通过简单指令驱动 AI 完成工作流。

3. **适用场景**
   - 自动化内容创作与社交媒体运营（如自动撰写博客、发布帖子）。
   - 复杂的代码生成与软件开发辅助（如自动重构代码、编写测试用例）。
   - 数据收集与分析任务（如自动爬取网页信息并进行结构化整理）。

4. **技术亮点**
   - 作为 Agentic AI 领域的标杆项目，拥有极高的社区活跃度（超 18 万星标）和广泛的生态兼容性。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185411 | 🍴 46125 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164990 | 🍴 21360 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164015 | 🍴 30387 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156859 | 🍴 46163 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151275 | 🍴 9458 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148014 | 🍴 23316 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

