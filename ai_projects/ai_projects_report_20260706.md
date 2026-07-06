# GitHub AI项目每日发现报告
日期: 2026-07-06

## 新发布的AI项目

### spicy-monopoly
- 1. **中文简介**
这是一款基于 Python 开发的双人棋盘游戏，允许玩家与人工智能对手进行对战。游戏包含掷骰子、地图格互动以及成人向的趣味任务，所有逻辑均由代码驱动，适合 18 岁以上用户。

2. **核心功能**
*   支持玩家与 AI 进行双人回合制棋盘对战。
*   内置掷骰子机制与动态地图格子交互系统。
*   集成“辛辣”成人向任务，增加游戏的趣味性与不可预测性。
*   全代码驱动的游戏逻辑，确保规则执行的自动化与一致性。

3. **适用场景**
*   个人开发者用于学习 Python 游戏逻辑编程与 AI 交互设计。
*   朋友聚会时作为轻松的数字版桌游替代品进行娱乐。
*   对简单棋盘游戏规则实现感兴趣的技术爱好者参考源码。
*   需要轻量级、可定制双人博弈算法的研究或演示环境。

4. **技术亮点**
*   完全使用 Python 编写，结构简洁，易于阅读和二次开发。
*   将传统桌游元素（骰子、地图）数字化，展示了基础游戏状态管理的实现。
- 链接: https://github.com/RennAkira/spicy-monopoly
- ⭐ 63 | 🍴 13 | 语言: Python

### Vibe-Research
- 1. **中文简介**
Vibe-Research 是一款由个人 AI 驱动的投研助手，支持 A 股、美股及港股市场。它集成了每日复盘、资讯雷达、个股与板块数据分析、持仓管理及研究记录等功能，旨在为用户提供一站式的数据与工具支持。

2. **核心功能**
*   提供每日市场复盘与全球资讯雷达，帮助用户快速捕捉关键信息。
*   深度整合个股数据与板块中心，支持多维度的市场趋势分析。
*   具备个人持仓管理与详细的研究记录功能，便于跟踪投资逻辑。
*   通过 AI 代理自动化处理数据整理与分析任务，提升投研效率。

3. **适用场景**
*   需要同时监控 A 股、美股和港股行情的多市场投资者。
*   希望利用 AI 辅助进行每日市场复盘和资讯筛选的交易员。
*   重视投资逻辑沉淀，需要系统化记录研究过程的个人投资者。

4. **技术亮点**
*   采用 React 构建现代化前端仪表盘，结合 FastAPI 提供高效后端服务。
*   集成 LLM（大语言模型）与 MCP（模型上下文协议），实现智能化的数据处理与交互。
- 链接: https://github.com/simonlin1212/Vibe-Research
- ⭐ 53 | 🍴 17 | 语言: TypeScript
- 标签: a-stock, ai-agent, dashboard, fastapi, fintech

### OmniPost-AI
- 描述: AI-powered Chrome extension for generating and publishing posts to Facebook, Threads, and X using ChatGPT or Gemini.
- 链接: https://github.com/wanglinsaputra/OmniPost-AI
- ⭐ 37 | 🍴 15 | 语言: TypeScript
- 标签: ai, automation, chatgpt, chrome-extension, gemini

### NavoIM
- ### 1. 中文简介
Navo IM 是由 Navo 团队开发的一款注重隐私保护与实时交互体验的即时通讯应用。该应用支持端到端加密，并提供频道管理及 AI 助手等高级功能，旨在为用户提供安全高效的沟通环境。

### 2. 核心功能
*   **端到端加密**：确保用户消息在传输过程中仅发送方和接收方可读，保障通信隐私。
*   **AI 助手集成**：内置人工智能助手，辅助用户进行内容生成、信息查询或任务管理。
*   **频道管理**：支持建立和组织频道，便于社群或团队进行分类交流与协作。
*   **实时体验优化**：专注于低延迟和高响应速度的即时通讯体验。

### 3. 适用场景
*   **注重隐私的社群交流**：适合对数据安全有高要求的讨论小组或兴趣社区。
*   **团队协作与知识共享**：利用频道功能和 AI 助手提升团队内部的信息同步与工作效率。
*   **个人智能助手平台**：用户可通过集成 AI 助手进行日常信息查询或自动化任务处理。

### 4. 技术亮点
*   **TypeScript 开发**：采用 TypeScript 构建，有助于提升代码的可维护性、类型安全和开发效率。
- 链接: https://github.com/aijianai/NavoIM
- ⭐ 20 | 🍴 0 | 语言: TypeScript

### anima-use-google
- 1. **中文简介**
该项目是一个结合了MCP服务器和浏览器旁路扩展的工具，允许AI代理利用用户已登录的浏览器会话来执行Google AI模式搜索。它通过复用现有身份验证状态，使AI能够获取更精准、个性化的搜索结果。

2. **核心功能**
*   集成MCP（模型上下文协议）服务器，实现标准化的AI工具调用接口。
*   提供浏览器旁路扩展，安全地接管并读取本地浏览器的登录会话Cookie。
*   支持AI代理直接发起Google AI Mode搜索，获取增强型搜索结果。
*   无需重复登录即可让AI利用用户的个人搜索历史和权限。

3. **适用场景**
*   AI智能体需要访问用户个性化推荐或基于地理位置的搜索结果时。
*   开发者希望构建能直接操作真实浏览器环境的自动化搜索工作流。
*   需要绕过常规API限制，利用Google AI Mode进行深度信息检索的场景。

4. **技术亮点**
*   创新性地结合MCP协议与浏览器扩展技术，打通了AI应用与本地浏览器会话的数据壁垒。
*   利用“旁路”架构，在不干扰正常浏览体验的前提下实现数据提取。
- 链接: https://github.com/animaios/anima-use-google
- ⭐ 18 | 🍴 0 | 语言: JavaScript
- 标签: agent-search, ai, ai-agents, ai-search, mcp-search

### coread
- 描述: Read a book together with your AI — grounded in the real text, spoiler-safe, with shared margin notes. 和你的 AI 真正共读一本书。
- 链接: https://github.com/Lumenocturne/coread
- ⭐ 13 | 🍴 2 | 语言: JavaScript

### hermes-second-brain
- 描述: AI second brain for Obsidian, controlled from Telegram via Hermes Agent (MCP)
- 链接: https://github.com/andrihakim146/hermes-second-brain
- ⭐ 12 | 🍴 1 | 语言: Python

### use-codex-vscode-ai-router
- 描述: 在 VSCode 中使用 Codex
- 链接: https://github.com/croath/use-codex-vscode-ai-router
- ⭐ 11 | 🍴 0 | 语言: 未知

### ai_review_skills
- 描述: This is review code skill used for tehnical bug hunting inside of the code. 
- 链接: https://github.com/vladimir-cicovic/ai_review_skills
- ⭐ 10 | 🍴 0 | 语言: 未知

### professional-legal-prompts
- 描述: Professional legal prompts and AI-agent skills for Japanese-law contract review and complaint drafting
- 链接: https://github.com/legalagent/professional-legal-prompts
- ⭐ 10 | 🍴 2 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81619 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关代码项目的精选列表，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它提供了完整的代码实现，旨在帮助开发者快速入门并深入掌握各类人工智能技术的实际应用。作为一份“Awesome”列表，它是初学者和专业人士构建AI作品集的优质资源库。

2. **核心功能**
*   提供海量（500+）涵盖主流AI子领域的可执行代码示例。
*   分类清晰，明确区分机器学习、深度学习、计算机视觉和NLP项目。
*   包含Python语言实现的完整项目结构，便于直接运行和学习。
*   经过社区筛选与认证，确保项目质量与技术前瞻性（标记为Awesome）。

3. **适用场景**
*   **学习实践**：适合AI初学者通过阅读和运行代码来理解理论概念。
*   **项目参考**：开发者可直接复用或修改代码以构建自己的AI应用原型。
*   **技术调研**：研究人员或工程师用于快速了解当前AI各细分领域的最新开源项目趋势。

4. **技术亮点**
*   高人气与社区认可度（35,000+星标），验证了其内容的实用性和权威性。
*   技术栈全面，覆盖从传统机器学习到前沿深度学习的广泛领域。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35176 | 🍴 7319 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33183 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### ONNX 项目技术分析

**1. 中文简介**
ONNX（Open Neural Network Exchange）是一个旨在实现机器学习模型跨平台互操作性的开放标准。它允许开发者在不同深度学习框架之间无缝迁移和部署模型，打破了生态系统的壁垒。通过统一格式存储模型，ONNX 极大地简化了从训练到生产环境的流程。

**2. 核心功能**
*   **跨框架兼容性**：支持在 PyTorch、TensorFlow、Keras 等主流框架间转换模型结构。
*   **标准化模型表示**：提供统一的格式定义，确保模型数据和计算图在不同运行时环境中保持一致。
*   **优化与加速执行**：结合 ONNX Runtime 提供高性能推理引擎，支持 CPU、GPU 及专用硬件加速。
*   **生态系统集成**：广泛兼容 Scikit-learn 等传统机器学习库，扩展了适用范围至更广泛的 AI 场景。

**3. 适用场景**
*   **模型部署**：将在开发框架（如 PyTorch）中训练的模型转换为 ONNX 格式，以便在生产环境（如嵌入式设备或移动端）高效运行。
*   **混合技术栈迁移**：当团队需要从一种深度学习框架迁移到另一种时，利用 ONNX 作为中间格式降低重构成本。
*   **硬件加速测试**：快速验证模型在不同硬件加速器（如 NPU、TPU）上的性能表现，无需重写底层代码。

**4. 技术亮点**
*   **开源中立标准**：由微软、Facebook 等科技巨头共同维护，确保了标准的开放性和行业认可度。
*   **丰富的算子支持**：涵盖了绝大多数深度神经网络所需的层和算子，并持续扩展以支持最新的研究成果。
*   **动态形状支持**：允许模型处理可变长度的输入数据，提高了在实际应用中的灵活性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21093 | 🍴 3962 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本专注于大规模机器学习系统构建与维护的综合性指南。它深入探讨了从底层硬件优化到上层模型训练、推理及部署的全链路工程实践，旨在填补理论研究与实际落地之间的鸿沟。

2. **核心功能**
*   提供针对GPU集群、Slurm调度系统及高性能网络的硬件与基础设施配置详解。
*   涵盖大语言模型（LLM）在分布式环境下的训练策略、调试技巧及可扩展性优化。
*   介绍模型压缩、量化技术及高效推理部署的最佳实践。
*   包含数据管道设计、存储优化及MLOps流水线自动化等工程化关键环节。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习训练集群的工程团队。
*   致力于提升大语言模型训练效率及降低硬件成本的研究机构与企业。
*   希望解决分布式训练中出现的具体调试难题（如通信瓶颈、显存溢出）的开发者。
*   寻求将实验性模型稳定部署至生产环境并实现高并发推理的系统架构师。

4. **技术亮点**
*   内容紧跟前沿，特别针对Transformer架构及大模型时代的工程挑战进行了深度适配。
*   强调“知其然更知其所以然”，不仅提供解决方案，还深入剖析底层原理与性能权衡。
*   作为开源资源，提供了经过实战验证的代码片段与配置模板，具有极高的可操作性和参考值。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18244 | 🍴 1158 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17263 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15409 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13109 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11554 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10660 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个汇集了500个AI相关代码项目的精选列表，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它提供了完整的代码实现，旨在帮助开发者快速入门并深入掌握各类人工智能技术的实际应用。作为一份“Awesome”列表，它是初学者和专业人士构建AI作品集的优质资源库。

2. **核心功能**
*   提供海量（500+）涵盖主流AI子领域的可执行代码示例。
*   分类清晰，明确区分机器学习、深度学习、计算机视觉和NLP项目。
*   包含Python语言实现的完整项目结构，便于直接运行和学习。
*   经过社区筛选与认证，确保项目质量与技术前瞻性（标记为Awesome）。

3. **适用场景**
*   **学习实践**：适合AI初学者通过阅读和运行代码来理解理论概念。
*   **项目参考**：开发者可直接复用或修改代码以构建自己的AI应用原型。
*   **技术调研**：研究人员或工程师用于快速了解当前AI各细分领域的最新开源项目趋势。

4. **技术亮点**
*   高人气与社区认可度（35,000+星标），验证了其内容的实用性和权威性。
*   技术栈全面，覆盖从传统机器学习到前沿深度学习的广泛领域。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35176 | 🍴 7319 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款支持神经网络、深度学习及机器学习模型的可视化工具。它能够直观地展示模型架构与参数，帮助用户更好地理解和分析各类 AI 模型结构。

2. **核心功能**
*   支持多种主流框架格式的模型可视化，包括 ONNX、PyTorch、TensorFlow 等。
*   提供清晰的图形化界面，直观展示神经网络层结构与数据流向。
*   允许用户本地打开或在线拖拽上传模型文件进行查看。
*   兼容 CoreML、TFLite、Keras 等多种特定平台或格式的模型展示。

3. **适用场景**
*   深度学习开发者调试和检查复杂神经网络的内部结构。
*   研究人员快速理解不同框架下预训练模型的架构细节。
*   工程人员在部署前验证模型转换（如从 PyTorch 到 ONNX）的正确性。
*   非技术人员通过可视化图表向利益相关者解释 AI 模型的工作原理。

4. **技术亮点**
*   广泛支持数十种不同的模型文件格式，兼容性极强。
*   纯前端实现（基于 JavaScript），无需安装重型后端服务即可运行。
*   开源免费，社区活跃且持续更新以支持新发布的模型格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33183 | 🍴 3148 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的速查手册集合。它涵盖了从基础数学工具到高级框架使用的关键知识点，旨在帮助研究者快速回顾和查阅核心技术细节。内容基于 Kailash Ahirwar 在 Medium 上发布的经典指南整理而成。

2. **核心功能**
*   提供涵盖 NumPy、SciPy 等数值计算库的语法速查。
*   包含 Matplotlib 数据可视化图表绘制的常用代码示例。
*   汇总了 Keras 深度学习框架的核心 API 使用技巧。
*   整理了对应语言（如 Python）中用于 AI 开发的标准库参考。
*   以简洁的单页或列表形式呈现，便于快速检索而非系统学习。

3. **适用场景**
*   研究人员在进行算法实验时，快速回忆特定函数参数的用法。
*   初学者在搭建第一个神经网络模型时，对照检查代码规范性。
*   开发者在技术面试前，突击复习机器学习基础概念和工具链。
*   团队内部分享会中，作为统一代码风格和常用工具使用的参考文档。

4. **技术亮点**
*   高度集成：将分散在不同库（NumPy, SciPy, Matplotlib, Keras）中的关键命令整合在一个项目中。
*   极简主义：摒弃冗长文档，专注于“复制-粘贴”即可运行的代码片段。
*   社区验证：拥有超过 1.5 万星标，证明其内容在 AI 社区中具有极高的实用性和认可度。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15409 | 🍴 3388 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13109 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11730 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9120 | 🍴 1235 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8917 | 🍴 3099 | 语言: C++
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
- ⭐ 6222 | 🍴 734 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81619 | 🍴 15253 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目已在 ACL 2024 上发表，旨在简化从指令调优到强化学习对齐的全流程开发体验。它通过整合多种前沿技术，大幅降低了大模型微调的技术门槛和计算成本。

### 2. 核心功能
*   **广泛模型支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 种主流 LLM 和 VLM 架构。
*   **多样化微调算法**：内置全参数微调、LoRA、QLoRA、P-Tuning 等多种高效微调策略。
*   **多阶段训练流程**：支持监督微调（SFT）、奖励模型训练（RM）及基于人类反馈的强化学习（RLHF/DPO）。
*   **量化与优化集成**：原生支持 GPTQ、AWQ 等量化技术，显著降低显存占用并提升推理速度。
*   **统一交互接口**：提供标准化的命令行和 Web UI 界面，简化数据准备、训练监控及模型导出流程。

### 3. 适用场景
*   **企业级私有化部署**：针对特定行业数据进行指令微调，构建专属的企业级知识助手或客服机器人。
*   **学术研究原型验证**：研究人员利用其统一的接口快速对比不同算法（如 LoRA vs QLoRA）在特定数据集上的效果。
*   **多模态应用开发**：开发者使用视觉语言模型（VLM）进行图文理解或生成的微调，构建具备图像识别能力的智能应用。
*   **低资源环境优化**：在显存受限的设备上，利用 QLoRA 和量化技术高效运行大型模型微调任务。

### 4. 技术亮点
*   **极致显存效率**：通过 QLoRA 和 4-bit/8-bit 量化技术，实现单张消费级显卡即可微调超大参数模型。
*   **模块化架构设计**：解耦数据处理、模型加载与训练逻辑，便于开发者自定义插件和扩展功能。
*   **高性能训练引擎**：底层优化了数据加载和梯度累积机制，显著提升大规模分布式训练的吞吐量。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72975 | 🍴 8919 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### AI-For-Beginners 项目分析

1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI。该项目由Microsoft For Beginners支持，通过结构化的教学路径帮助初学者掌握从基础概念到高级应用的核心技能。其内容覆盖广泛，适合不同背景的学习者系统性地构建AI知识体系。

2. **核心功能**
- 提供结构化的12周学习路径，将复杂的人工智能概念拆解为24节循序渐进的课程。
- 基于Jupyter Notebook实现交互式编程教学，便于学习者边学边练。
- 涵盖机器学习、深度学习、计算机视觉、自然语言处理及生成对抗网络等主流AI领域。
- 面向零基础用户设计，强调通俗易懂的教学方式，降低AI学习门槛。
- 作为Microsoft For Beginners系列的一部分，提供官方认证的学习资源和支持社区。

3. **适用场景**
- 初学者希望系统入门人工智能领域，建立完整的知识框架。
- 教育机构或企业用于培训新员工，快速提升团队在AI方面的基础能力。
- 学生或自学者希望通过实践项目巩固理论知识，掌握实际编程技能。
- 对特定AI技术（如CNN、RNN、GAN）感兴趣的学习者进行专项深入研习。

4. **技术亮点**
- 采用Jupyter Notebook作为主要教学载体，实现代码与文档的无缝结合，提升学习体验。
- 内容设计兼顾广度与深度，既覆盖传统机器学习算法，也涉及前沿的深度学习架构。
- 由微软官方背书并维护，确保内容的准确性、时效性和权威性。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51737 | 🍴 10443 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并泄露了包括Anthropic、OpenAI、Google及xAi等主流厂商在内的多款先进大模型（如Claude、GPT、Gemini系列）的系统提示词。内容涵盖ChatGPT、Claude Code、Cursor等工具的内部指令，并定期更新以反映最新模型的配置变化。

2. **核心功能**
*   提取并公开多家顶级AI厂商的大模型系统提示词。
*   覆盖Claude、GPT、Gemini及各类AI编程助手等多种模型变体。
*   保持内容定期更新，跟踪最新发布的模型指令变更。
*   提供结构化数据，便于研究者直接查阅或对比不同模型的底层逻辑。

3. **适用场景**
*   提示词工程（Prompt Engineering）学习与优化参考。
*   AI安全研究人员进行红队测试与防御策略制定。
*   开发者深入理解各模型行为边界与内部约束机制。
*   学术研究中对不同大模型架构与指令微调方式的对比分析。

4. **技术亮点**
*   整合了多个竞争性平台的关键机密信息，具有极高的情报价值。
*   持续更新的动态数据库，确保信息的时效性与前沿性。
*   跨厂商的全面覆盖，为多模型比较研究提供了统一的数据源。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 49983 | 🍴 8181 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个综合性的AI学习资源库，涵盖数据分析、机器学习实战以及线性代数等数学基础。它深入结合了PyTorch和TensorFlow 2等主流深度学习框架，并集成NLTK进行自然语言处理实践。

2. **核心功能**
- 提供从监督学习（如SVM、Logistic回归）到无监督学习（如K-Means、PCA）的全面算法实现。
- 包含深度学习模块，支持RNN、LSTM、DNN及推荐系统等复杂模型的开发与训练。
- 集成自然语言处理工具包NLTK，涵盖文本挖掘、情感分析及序列模型应用。
- 结合Scikit-learn与PyTorch/TF2框架，提供工业级机器学习项目的实战代码示例。

3. **适用场景**
- AI初学者系统学习机器学习理论并将其转化为代码实战。
- 数据科学家用于快速查阅和复现经典算法（如Adaboost、FP-Growth）的实现细节。
- 研究人员在部署NLP任务或构建推荐系统时参考基于PyTorch/TF2的最佳实践。

4. **技术亮点**
- 内容体系完整，打通了数学基础、传统机器学习、深度学习与自然语言处理的技术链路。
- 兼容多框架生态，同时支持Scikit-learn传统ML与PyTorch/TF2现代深度学习工作流。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42352 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37403 | 🍴 6208 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35176 | 🍴 7319 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33715 | 🍴 4691 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28359 | 🍴 3443 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25830 | 🍴 2901 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的综合性资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域并附带代码实现。该项目旨在为开发者提供一个全面的实践指南，帮助学习者快速掌握人工智能核心技术与应用。

2. **核心功能**
*   收录500个精选AI项目，覆盖主流技术领域。
*   所有项目均提供源代码，支持直接运行与学习。
*   分类清晰，按机器学习、深度学习、CV和NLP等模块组织。
*   作为Awesome列表，提供高质量的项目筛选与索引。

3. **适用场景**
*   AI初学者寻找入门级实战项目以巩固理论知识。
*   工程师参考现有案例进行模型开发或技术选型。
*   研究人员收集特定领域（如CV或NLP）的最新项目灵感。

4. **技术亮点**
*   极高的收藏量（35k+星标）证明了其社区认可度和内容质量。
*   多标签体系（Python, Data Science等）便于精准检索。
*   全代码开源特性提供了从理论到落地的完整闭环。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35176 | 🍴 7319 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22120 | 🍴 2069 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### 1. 中文简介
CVAT 是一款领先的计算机视觉标注平台，致力于构建高质量的视觉数据集以赋能视觉人工智能。它提供开源、云端及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量控制及团队协作，并配备完善的开发者 API。

### 2. 核心功能
- **多模态标注支持**：全面支持图像分类、边界框检测、语义分割及 3D 点云标注等多种任务类型。
- **AI 辅助与自动化**：集成预训练模型实现自动标注建议，显著提升数据标注效率并降低人力成本。
- **团队协作与管理**：提供完善的项目管理、角色权限控制及质量审核流程，适合大规模团队协同作业。
- **全栈式解决方案**：涵盖开源软件、公有云服务及私有化部署的企业版，满足不同规模用户的需求。
- **开放生态集成**：提供强大的 Developer API，便于与现有的数据处理流水线及深度学习框架无缝对接。

### 3. 适用场景
- **自动驾驶研发**：用于标注大量道路场景视频和图像，训练物体检测和车道线分割模型。
- **医疗影像分析**：对 CT、MRI 等医学图像进行精准标注，辅助开发疾病诊断算法。
- **零售智能监控**：标注商场或仓库中的行为视频数据，用于人流统计或异常行为检测。
- **学术研究数据集构建**：为高校或研究机构快速构建标准化的计算机视觉基准数据集。

### 4. 技术亮点
- **基于 Web 的架构**：无需安装本地客户端，通过浏览器即可访问，降低了部署和维护门槛。
- **活跃的开源社区**：拥有超过 1.6 万 GitHub Star，意味着其代码稳定性高且拥有持续的功能迭代和安全更新。
- **框架兼容性**：原生支持 PyTorch 和 TensorFlow 等主流深度学习框架的数据格式导出。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16224 | 🍴 3736 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### 1. 中文简介
该项目提供了先进的计算机视觉可解释性解决方案，支持卷积神经网络（CNN）、Vision Transformers等多种架构。它涵盖了图像分类、目标检测、分割及相似度计算等多种任务，旨在提升深度学习模型的透明度与可理解性。

### 2. 核心功能
*   全面支持CNN和Vision Transformer等主流视觉模型架构。
*   提供多种可解释性算法，如Grad-CAM、Score-CAM及类激活映射。
*   兼容分类、目标检测、语义分割及图像相似度等多种计算机视觉任务。
*   生成直观的可视化结果，帮助用户理解模型决策依据。

### 3. 适用场景
*   深度学习模型调试与错误分析，定位模型关注区域。
*   医疗影像或自动驾驶等高可靠性要求领域的模型可信度验证。
*   学术研究中的可解释人工智能（XAI）对比实验。
*   向非技术人员展示AI系统决策逻辑的教学演示。

### 4. 技术亮点
*   高度模块化设计，无缝集成PyTorch框架，支持即插即用的扩展性。
*   统一接口覆盖从传统CNN到最新Transformer架构的多维需求。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12898 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，旨在为深度学习工作流提供可微分的图像处理工具。该项目致力于简化视觉算法在神经网络中的集成与开发。

2. **核心功能**
- 提供大量可微分的传统计算机视觉算子，便于与深度学习模型无缝集成。
- 支持高效的图像预处理、增强及几何变换操作。
- 内置多种常用的几何视觉算法实现，如相机标定和位姿估计。
- 兼容 PyTorch 生态，允许在 GPU 上加速处理复杂的视觉流水线。

3. **适用场景**
- 机器人视觉导航中需要实时几何计算的场景。
- 自动驾驶系统中对图像进行标准化预处理和数据增强的阶段。
- 构建端到端的深度学习模型时，需引入可微分图像滤波或特征提取环节。
- 学术研究中进行计算机视觉算法的快速原型开发与验证。

4. **技术亮点**
- 作为首个专注于可微分计算机视觉的 PyTorch 库，它填补了传统 CV 算法与现代深度学习框架之间的空白。
- 拥有活跃的社区支持和丰富的标签覆盖（涵盖 AI、CV、机器人等领域），显示出其在学术界和工业界的高认可度。
- 链接: https://github.com/kornia/kornia
- ⭐ 11263 | 🍴 1194 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3453 | 🍴 876 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3268 | 🍴 400 | 语言: Python
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
- 基于您提供的信息，以下是关于 GitHub 项目 **openclaw** 的技术分析：

1. **中文简介**
   OpenClaw 是一款跨平台、支持任意操作系统的个人 AI 助手，致力于让用户以“龙虾模式”完全掌控自己的数据。它采用 TypeScript 开发，强调隐私与自主权，确保用户拥有数据的绝对所有权。该项目旨在提供一种灵活且私密的个人 AI 解决方案。

2. **核心功能**
   - 跨平台兼容：支持在任何操作系统和平台上运行。
   - 数据自主权：强调“Own Your Data”，确保用户数据私有且可控。
   - 个性化 AI 助手：作为专属的个人 AI 助理，提供定制化服务。
   - 开源透明：作为开源项目，代码公开，便于社区审计和改进。

3. **适用场景**
   - 注重隐私的用户：希望将 AI 服务本地化或私有化部署，避免数据泄露给大型科技公司。
   - 开发者与技术爱好者：喜欢折腾 Linux/macOS/Windows 环境，希望自定义 AI 助手行为的技术人员。
   - 个人效率提升者：需要一个全天候在线、可集成到工作流中的个人智能助手来处理日常任务。

4. **技术亮点**
   - 使用 TypeScript 编写，具有良好的类型安全和现代前端/后端生态兼容性。
   - 标签中包含 "crustacean"（甲壳类）和 "lobster"（龙虾），暗示其品牌特色或底层架构可能具有独特的模块化或坚固性设计理念（注：此为品牌隐喻，非严格技术术语）。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381839 | 🍴 80086 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论，旨在提升开发效率。它通过结构化的子代理驱动开发模式，优化了从头脑风暴到代码实现的完整软件生命周期。该项目致力于解决传统 AI 辅助编程中缺乏系统性和一致性的问题。

2. **核心功能**
*   **智能体技能框架**：提供模块化的“技能”定义，使 AI 智能体能像专业人员一样执行特定任务。
*   **子代理驱动开发**：采用多智能体协作机制，通过主智能体调度多个子智能体完成复杂软件工程任务。
*   **全生命周期支持**：涵盖从需求分析、头脑风暴、编码到测试的完整 SDLC（软件开发生命周期）流程。
*   **标准化交互协议**：基于 OBRA 等标准，规范智能体之间的通信与技能调用方式，确保结果的一致性。

3. **适用场景**
*   **复杂软件架构设计**：需要多步骤推理和模块化设计的中小型项目开发。
*   **自动化代码生成与重构**：利用结构化技能快速生成符合规范的代码或进行大规模重构。
*   **AI 辅助团队工作流优化**：希望将 AI 深度集成到现有软件开发流程中的工程团队。
*   **探索性原型开发**：在头脑风暴阶段快速验证想法并生成可运行的代码草稿。

4. **技术亮点**
*   **方法论创新**：不仅是一个工具库，更是一套完整的“智能体驱动开发”理论实践体系。
*   **语言无关性**：虽然主要使用 Shell 脚本实现框架逻辑，但其定义的技能和代理模式可适配多种编程语言环境。
*   **高社区认可度**：拥有极高的星标数（24万+），证明其在 AI 编程领域的广泛影响力和实用性。
- 链接: https://github.com/obra/superpowers
- ⭐ 246880 | 🍴 21904 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够伴随用户共同成长的智能代理系统。它旨在通过持续的学习与互动，深度适应用户的工作流与偏好。作为一个高度可扩展的 AI 助手，它致力于提供个性化且高效的代码辅助与任务执行能力。

2. **核心功能**
*   支持动态记忆与上下文学习，实现随时间推移的能力进化。
*   集成主流大语言模型（如 Claude、GPT），提供强大的自然语言理解与生成能力。
*   具备自动化代码编写、调试及项目维护的智能代理功能。
*   支持多模态交互，能够处理文本、代码片段及复杂逻辑推理任务。
*   提供灵活的插件架构，允许用户根据需求自定义扩展功能模块。

3. **适用场景**
*   开发者日常编码辅助，包括自动生成代码、解释复杂逻辑及快速修复 Bug。
*   个人知识管理与信息整理，通过对话形式高效检索和总结长期积累的数据。
*   自动化工作流执行，将重复性的技术任务（如部署、测试）交给代理自动处理。
*   复杂问题解决与决策支持，利用其持续学习的特性提供针对性的专业建议。

4. **技术亮点**
*   采用先进的长期记忆机制，确保代理在长时间交互中保持上下文连贯性。
*   兼容多种顶级 LLM 后端，用户可根据性能需求灵活切换模型提供商。
*   拥有活跃的开源社区支持，标签涵盖 Anthropic、OpenAI 等主流生态，技术栈成熟稳定。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 209683 | 🍴 38327 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### n8n 项目分析

1. **中文简介**
   n8n 是一个采用公平代码许可的工作流自动化平台，原生集成 AI 能力，支持可视化构建与自定义代码混合开发。它提供了超过 400 种集成方式，用户可选择自托管或云端部署，兼具低代码的高效性与高代码的灵活性。

2. **核心功能**
   - 提供可视化工作流编辑器，支持拖拽式逻辑编排。
   - 内置原生 AI 功能，可轻松集成大语言模型进行智能处理。
   - 拥有 400 多种预建集成连接器，覆盖主流 API 和服务。
   - 允许在可视化节点中嵌入自定义 TypeScript/JavaScript 代码。
   - 支持自托管部署以保障数据隐私，也可使用云服务快速启动。

3. **适用场景**
   - **企业数据同步**：自动化连接 CRM、数据库和 ERP 系统，实现数据实时同步与清洗。
   - **AI 驱动的业务流程**：利用原生 AI 节点自动生成内容、总结文档或进行智能客服响应。
   - **开发者工具链集成**：通过自定义代码节点和 API 触发器，构建复杂的 CI/CD 自动化流水线。
   - **营销自动化**：自动处理表单提交、邮件发送和用户行为追踪，优化营销策略。

4. **技术亮点**
   - 采用 TypeScript 开发，类型安全且易于扩展和维护。
   - 独特的“公平代码”（Fair-code）许可证，平衡了开源共享与企业商用需求。
   - 原生支持 MCP（Model Context Protocol），为 AI 应用提供更标准的数据上下文交互方式。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195314 | 🍴 59084 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上进行开发构建。我们的使命是提供必要的工具，使用户能够将精力集中在真正重要的事务上。

2. **核心功能**
*   具备自主代理能力，可独立规划并执行复杂的多步骤任务。
*   集成多种大型语言模型（如 GPT、Claude、Llama），支持灵活的模型切换。
*   提供开放的开发框架，允许用户基于其工具链扩展自定义 AI 应用。
*   自动化处理浏览器交互、文件读写及 API 调用等常见操作。

3. **适用场景**
*   需要长期运行且无需人工干预的自动化工作流（如数据抓取与整理）。
*   开发者用于快速原型验证或构建基于 LLM 的智能代理应用。
*   个人用户希望利用 AI 辅助完成复杂的日常研究或内容创作任务。

4. **技术亮点**
*   作为 Agentic AI 领域的标杆项目，拥有极高的社区活跃度与生态兼容性。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185389 | 🍴 46119 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164784 | 🍴 21321 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163998 | 🍴 30378 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156812 | 🍴 46164 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151200 | 🍴 9444 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147796 | 🍴 23273 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

