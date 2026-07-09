# GitHub AI项目每日发现报告
日期: 2026-07-09

## 新发布的AI项目

### lapian-notes
- 描述: 拉片笔记:把电影变成 AI 辅助的拉片笔记 - 本地抽帧/剧情泳道时间轴/结构树/情绪曲线/段落深拆
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 78 | 🍴 14 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### Homekit
- **1. 中文简介**
Homekit 通过单一开放接口，赋予任意 AI 智能体直接控制 Apple Home 生态的物理能力，实现开关灯光、锁门及读取传感器数据等操作。该项目基于 TypeScript 开发，旨在让 AI 代理能够无缝接入智能家居环境进行自动化交互。

**2. 核心功能**
*   提供统一开放接口，使 AI 智能体能直接操控 Apple Home 设备。
*   支持物理控制操作，包括开关灯光和远程锁定门窗。
*   具备实时传感器数据读取能力，为智能决策提供环境信息。
*   兼容主流 AI 框架与模型上下文协议（MCP），便于集成到现有工作流中。

**3. 适用场景**
*   开发者希望将 Claude 或 OpenClaw 等 AI 模型接入自家 Apple Home 智能家居系统。
*   构建基于自然语言指令的自动化家居控制机器人或智能助手。
*   在 macOS 环境下利用 Cursor 等工具开发结合 AI 的智能家居应用原型。
*   研究或演示模型上下文协议（MCP）在物联网设备控制中的实际应用。

**4. 技术亮点**
*   实现了 AI 智能体与 Apple 专有智能家居协议之间的标准化桥接。
*   采用 TypeScript 编写，具备良好的类型安全和现代 Node.js 兼容性。
*   原生支持 MCP（Model Context Protocol），简化了 AI 模型与外部工具的集成过程。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### ditto
- 1. **中文简介**
该项目能从 Claude Code 和 Codex 的使用日志中提取数据，构建本地的 `you.md` 智能体配置文件。它旨在通过本地优先的方式，为 AI 编程助手提供个性化的上下文记忆和技能支持。

2. **核心功能**
*   解析并提取 Claude Code 与 Codex 的历史操作日志。
*   自动生成包含用户偏好和工作习惯的 `you.md` 个人档案。
*   实现完全本地化的数据处理，确保隐私安全。
*   增强 AI 智能体的长期记忆与个性化上下文理解能力。

3. **适用场景**
*   希望 Cursor 或 Claude Code 更了解个人代码风格和技术偏好的开发者。
*   需要跨会话保持上下文连贯性的高级 AI 编程助手用户。
*   重视数据隐私，倾向于在本地处理敏感开发日志的团队或个人。

4. **技术亮点**
*   采用“本地优先”架构，无需依赖外部云服务即可处理日志。
*   通过结构化日志挖掘实现精准的个性化上下文工程（Context Engineering）。
- 链接: https://github.com/ohad6k/ditto
- ⭐ 42 | 🍴 6 | 语言: Python
- 标签: agent-memory, agent-skills, ai, ai-agents, ai-coding

### openclaw-voice-call-realtime
- ### 1. 中文简介
该项目是一个 OpenClaw 插件，通过整合 Twilio 和 OpenAI Realtime API，赋予 AI 助手拨打和接听真实电话的能力。它支持通话中的工具调用、实时转录以及来电筛选功能，实现了从虚拟对话到真实语音交互的跨越。

### 2. 核心功能
*   **真实电话集成**：利用 Twilio 实现与真实电话号码的双向语音通信。
*   **实时交互引擎**：基于 OpenAI Realtime API 提供低延迟、自然的语音对话体验。
*   **动态工具调用**：AI 在通话过程中可执行实际操作（如查询数据、发送消息等）。
*   **智能来电筛选**：自动识别并处理潜在垃圾电话或无关呼叫，保护用户隐私。
*   **完整通话记录**：自动生成并保存通话转录文本，便于后续回顾与分析。

### 3. 适用场景
*   **智能客服系统**：为小型企业或独立开发者提供 24/7 全天候真人级电话客服支持。
*   **个人助理服务**：帮助用户过滤骚扰电话、安排日程或远程操控智能家居设备。
*   **紧急通知广播**：在关键任务场景中，通过 AI 进行高优先级的语音通知或状态确认。
*   **多语言热线服务**：利用 AI 的多语言能力，低成本搭建覆盖多种语言的自动接听热线。

### 4. 技术亮点
*   **模块化架构**：作为 OpenClaw 插件运行，易于集成到现有的 AI Agent 工作流中。
*   **端到端语音链路**：打通了从电信网络（Twilio）到大模型推理（OpenAI）的完整实时音频流处理。
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 35 | 🍴 3 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### sm120-field-guide
- 1. **中文简介**
本项目是针对英伟达Blackwell架构消费级显卡（RTX 50系列/sm_120）的实战开发指南。内容涵盖了从RTX 5090实测中总结出的修复方案、常见陷阱以及诚实的性能测量数据。旨在帮助开发者避开硬件限制，优化针对新架构的代码。

2. **核心功能**
- 提供针对sm_120架构的特定代码修复方案与兼容性调整。
- 识别并警示开发过程中容易踩中的“坑”和潜在错误。
- 基于真实RTX 5090硬件的基准测试与性能测量数据。
- 指导消费者级Blackwell GPU的高效开发与优化技巧。

3. **适用场景**
- 开发者在RTX 50系列显卡上部署或移植现有CUDA程序时进行调试。
- 研究人员需要获取最新的Blackwell架构消费级GPU真实性能基准数据。
- 软件工程师希望避免在新硬件上因架构差异导致的常见兼容性问题。

4. **技术亮点**
- 基于单张RTX 5090的真实一手实测数据，具有较高的参考真实性。
- 专注于解决新架构（sm_120）带来的特定底层兼容性与性能瓶颈问题。
- 链接: https://github.com/notwitcheer/sm120-field-guide
- ⭐ 20 | 🍴 3 | 语言: 未知

### ai-guru
- 描述: 无描述
- 链接: https://github.com/Dhruvdubey17/ai-guru
- ⭐ 16 | 🍴 5 | 语言: Shell

### YSClaude
- 描述: YSClaude Expo/React Native Android AI assistant client
- 链接: https://github.com/winter-bit-cry/YSClaude
- ⭐ 15 | 🍴 5 | 语言: TypeScript

### fintech-advisor
- 描述: ai fintech financial advisor for your portfolio
- 链接: https://github.com/KORAYTEACHER/fintech-advisor
- ⭐ 15 | 🍴 0 | 语言: TypeScript
- 标签: ai, ai-advisor, ai-financial, ai-fintech, fintech

### FinTech-Solution
- 描述: FinTech AI Solution for SMEs to calculate financial values
- 链接: https://github.com/imchine/FinTech-Solution
- ⭐ 15 | 🍴 0 | 语言: TypeScript
- 标签: ai-solution, fintech, fintech-ai, fintech-solution, solution

### fintech-dashboard
- 描述: fintech dashboard for personal finance management which track income and expenses, leverage AI-powered analytics, manage budgets and financial goals, enjoy a dark theme
- 链接: https://github.com/Elias569/fintech-dashboard
- ⭐ 15 | 🍴 0 | 语言: TypeScript
- 标签: ai-dashboard, dashboard, fintech, fintech-ai, fintech-dashboard

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81698 | 🍴 15252 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目代码的精选资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等热门领域。该项目通过提供完整的代码实现，帮助开发者快速上手并深入理解各类AI算法的实际应用。

2. **核心功能**
- 汇集了500多个经过筛选的高质量AI项目案例，内容全面。
- 提供涵盖机器学习、深度学习、CV和NLP等多领域的完整代码实现。
- 标注为“Awesome”列表，确保收录的项目具有较高的参考价值和实用性。
- 主要基于Python语言开发，便于用户直接运行和修改代码。

3. **适用场景**
- AI初学者希望快速浏览并实践主流机器学习与深度学习算法。
- 研究人员或工程师寻找特定领域（如图像识别、文本处理）的代码参考范例。
- 教育者用于教学演示，展示如何将理论模型转化为可运行的代码项目。

4. **技术亮点**
- 规模宏大且分类清晰，一站式覆盖AI核心子领域。
- 强调“带代码”的实践性，不仅提供概念介绍，更注重落地实现。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架和模型格式，帮助用户直观地检查模型结构并调试数据流。

2. **核心功能**
*   广泛支持 TensorFlow、PyTorch、Keras、ONNX 等主流框架的模型文件。
*   提供直观的图形化界面，清晰展示网络层连接与数据流向。
*   支持查看模型权重参数及详细的层属性信息。
*   兼容桌面端应用、Web 浏览器及 VS Code 插件等多种运行环境。

3. **适用场景**
*   研究人员快速审查复杂神经网络的拓扑结构。
*   开发者在模型转换（如从 Keras 到 ONNX）后验证结构一致性。
*   工程师调试模型推理错误时排查特定层的配置问题。
*   非专业用户通过可视化工具理解机器学习模型的工作原理。

4. **技术亮点**
*   极高的兼容性，能够解析数十种不同的模型文件格式。
*   开源且跨平台，无需安装重型依赖即可快速启动使用。
*   界面简洁高效，专注于模型结构的静态分析与展示。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33199 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个旨在促进机器学习模型互操作性的开放标准。它允许开发者在不同深度学习框架之间无缝迁移和部署模型，打破了平台壁垒。

2. **核心功能**
*   提供统一的中间表示格式，支持模型在不同框架间的转换与交换。
*   实现跨平台兼容性，使模型能在多种硬件加速器和推理引擎上高效运行。
*   支持从训练到部署的全流程，简化了深度学习模型的集成与维护工作。
*   拥有广泛的生态系统支持，兼容PyTorch、TensorFlow、Keras等主流框架。

3. **适用场景**
*   需要将模型从PyTorch或TensorFlow导出并部署到特定硬件加速器（如CPU、GPU、NPU）时。
*   在微服务架构中，希望统一不同团队使用的不同训练框架以便共享模型资源时。
*   进行模型性能优化和基准测试，需要在一个标准化环境下评估不同框架的输出结果时。

4. **技术亮点**
*   **开放标准**：由Microsoft、Facebook等科技巨头联合发起，具有行业广泛认可度。
*   **高性能推理**：通过ONNX Runtime提供优化的执行引擎，显著提升模型推理速度。
*   **生态丰富**：支持大量算子（Operators），覆盖了大多数主流深度学习网络结构。
- 链接: https://github.com/onnx/onnx
- ⭐ 21118 | 🍴 3958 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- ### 1. 中文简介
该项目被誉为“机器学习工程开放书籍”，旨在为开发者提供从模型训练到部署的全栈式工程实践指南。它深入探讨了大规模语言模型（LLM）及深度学习基础设施的关键技术细节，是连接理论研究与实际工程落地的权威参考。

### 2. 核心功能
- **全链路工程指导**：涵盖数据预处理、分布式训练、模型推理优化及监控运维的完整机器学习生命周期。
- **大规模LLM优化**：专门针对大型语言模型，提供显存管理、并行策略（如ZeRO）及高效推理的具体实现方案。
- **基础设施配置**：详细解析Slurm作业调度器、高性能网络配置及分布式存储系统的搭建与调优技巧。
- **调试与可观测性**：提供针对GPU集群故障排查、性能瓶颈分析及训练过程可视化的实用工具与方法论。
- **PyTorch生态整合**：基于PyTorch框架，分享最新的模型转换、量化技术及Transformer库的高级使用技巧。

### 3. 适用场景
- **LLM研发工程师**：需要从零搭建或优化大规模预训练/微调集群，解决显存溢出和通信瓶颈问题。
- **MLOps平台架构师**：设计高可用、可扩展的机器学习生产环境，包括CI/CD流水线及模型服务化部署。
- **深度学习研究者**：希望将实验室模型高效转化为生产级应用，理解底层硬件与软件协同工作的原理。
- **系统管理员**：负责维护AI计算集群，需要掌握GPU资源调度、网络拓扑优化及存储性能调优知识。

### 4. 技术亮点
该项目不仅是代码集合，更是一部结构严谨的工程手册，特别强调在资源受限环境下通过软件优化（如梯度检查点、混合精度训练）实现硬件效能最大化，并提供了大量经过实战验证的生产级最佳实践。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18283 | 🍴 1159 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13114 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11563 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目代码的精选资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等热门领域。该项目通过提供完整的代码实现，帮助开发者快速上手并深入理解各类AI算法的实际应用。

2. **核心功能**
- 汇集了500多个经过筛选的高质量AI项目案例，内容全面。
- 提供涵盖机器学习、深度学习、CV和NLP等多领域的完整代码实现。
- 标注为“Awesome”列表，确保收录的项目具有较高的参考价值和实用性。
- 主要基于Python语言开发，便于用户直接运行和修改代码。

3. **适用场景**
- AI初学者希望快速浏览并实践主流机器学习与深度学习算法。
- 研究人员或工程师寻找特定领域（如图像识别、文本处理）的代码参考范例。
- 教育者用于教学演示，展示如何将理论模型转化为可运行的代码项目。

4. **技术亮点**
- 规模宏大且分类清晰，一站式覆盖AI核心子领域。
- 强调“带代码”的实践性，不仅提供概念介绍，更注重落地实现。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的轻量级工具。它支持多种主流框架和模型格式，帮助用户直观地检查模型结构并调试数据流。

2. **核心功能**
*   广泛支持 TensorFlow、PyTorch、Keras、ONNX 等主流框架的模型文件。
*   提供直观的图形化界面，清晰展示网络层连接与数据流向。
*   支持查看模型权重参数及详细的层属性信息。
*   兼容桌面端应用、Web 浏览器及 VS Code 插件等多种运行环境。

3. **适用场景**
*   研究人员快速审查复杂神经网络的拓扑结构。
*   开发者在模型转换（如从 Keras 到 ONNX）后验证结构一致性。
*   工程师调试模型推理错误时排查特定层的配置问题。
*   非专业用户通过可视化工具理解机器学习模型的工作原理。

4. **技术亮点**
*   极高的兼容性，能够解析数十种不同的模型文件格式。
*   开源且跨平台，无需安装重型依赖即可快速启动使用。
*   界面简洁高效，专注于模型结构的静态分析与展示。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33199 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习和机器学习研究人员提供了一系列必备的技巧速查表（Cheat Sheets）。它涵盖了从基础库到高级框架的关键知识点，旨在帮助研究者快速查阅和回顾核心技术细节。

### 2. 核心功能
*   提供深度学习与机器学习领域的关键概念速查。
*   涵盖 Keras、NumPy、SciPy 和 Matplotlib 等常用工具的使用技巧。
*   总结人工智能研究中的核心算法与最佳实践。

### 3. 适用场景
*   机器学习研究人员在开发过程中快速复习特定库或函数用法。
*   深度学习初学者整理知识体系，建立对常用工具链的整体认知。
*   数据科学家在调试代码时，作为解决常见问题的快速参考手册。

### 4. 技术亮点
*   聚焦于高频率使用的核心库（如 NumPy 和 Keras），内容精炼实用。
*   基于 Medium 知名文章整理，经过社区验证，具有较高的参考价值。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例并提供免费配套教材，旨在帮助零基础用户掌握 Python、机器学习及深度学习等核心技能。该项目涵盖从基础数学到高级 NLP/CV 技术的完整知识体系，致力于通过实战导向的方式助力学习者进入就业市场。

### 2. 核心功能
*   **系统化学习路径**：提供从零基础到就业级别的完整 AI 学习路线图，涵盖数学、编程及各类算法模型。
*   **丰富实战案例**：收录近 200 个精选实战项目，帮助用户将理论知识转化为实际动手能力。
*   **多框架支持**：兼容 PyTorch、TensorFlow、Keras、Caffe 等主流深度学习框架的教学内容。
*   **免费资源开放**：所有配套教材和学习资料均免费提供，降低人工智能入门门槛。

### 3. 适用场景
*   **AI 初学者入门**：适合完全零基础的学习者，通过路线图系统性地构建 AI 知识体系。
*   **求职实战准备**：适合希望提升工程落地能力、积累项目经验以增强就业竞争力的求职者。
*   **特定领域深入**：适合需要针对计算机视觉（CV）、自然语言处理（NLP）或数据分析进行专项训练的技术人员。

### 4. 技术亮点
*   **全栈技术覆盖**：整合了从数据处理（Pandas/NumPy）到可视化（Matplotlib/Seaborn），再到深层建模（DL/NLP/CV）的全链路技术栈。
*   **高社区认可度**：拥有超过 13,000 个 GitHub 星标，证明了其作为社区公认优质学习资源的广泛影响力。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13114 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9121 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8920 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6233 | 🍴 738 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面的中英文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取（手机/身份证/邮箱等）及繁简转换等基础功能。它还提供了丰富的行业词库、情感分析及预训练模型资源，旨在为开发者提供一站式 NLP 解决方案。

2. **核心功能**
*   提供敏感词过滤、中英文语言检测及手机号、身份证、邮箱等关键信息的自动抽取。
*   内置大量垂直领域词库（如汽车、医疗、法律、古诗词等）及同义词、反义词库。
*   集成多项前沿 NLP 任务工具，包括文本生成、摘要提取、情感分析及知识图谱构建。
*   支持语音识别语料处理、OCR 文字识别及多语言数字/单位识别等混合模态功能。

3. **适用场景**
*   **内容安全审核**：利用敏感词库和情感分析工具，对论坛、评论区的用户生成内容进行自动化过滤和风险检测。
*   **企业级信息抽取**：从非结构化文本（如简历、合同、新闻）中精准提取姓名、证件号、地址等实体信息。
*   **智能客服与聊天机器人**：结合词库、情感分析和对话数据集，开发具备语义理解和上下文保持能力的聊天机器人。
*   **数据分析与挖掘**：利用分词、词向量和关键词抽取工具，对海量中文文本进行舆情分析或行业趋势挖掘。

4. **技术亮点**
该项目不仅涵盖了传统的 NLP 基础工具（如分词、词性标注），还整合了基于 BERT、GPT 等最新深度学习模型的预训练资源及知识图谱构建方案，实现了从基础数据处理到高级语义理解的完整技术栈覆盖。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81698 | 🍴 15252 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型与视觉语言模型微调框架，支持 100 多种主流模型的训练。该项目曾入选 ACL 2024，旨在简化 LLM 和 VLM 的微调流程，提供一站式解决方案。它集成了多种先进的微调技术，帮助用户轻松部署和优化大型模型。

2. **核心功能**
*   **多模型统一支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100 多个主流大模型及视觉语言模型。
*   **高效微调算法**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调方法，显著降低计算资源需求。
*   **多样化训练策略**：支持监督微调（SFT）、奖励建模（RM）、PPO 强化学习以及 DPO 直接偏好优化等高级对齐技术。
*   **量化与推理加速**：提供 GGUF、AWQ、INT8/4 等量化支持，并集成 vLLM 加速推理，提升部署效率。
*   **可视化与易用性**：提供 Web UI 界面和命令行工具，支持日志监控和数据管理，降低使用门槛。

3. **适用场景**
*   **企业级私有化部署**：在有限硬件资源下，对开源大模型进行领域数据微调，构建垂直行业助手。
*   **模型对齐与优化**：通过 RLHF/DPO 等技术调整模型输出风格，使其更符合人类价值观或特定指令要求。
*   **多模态应用开发**：微调视觉语言模型（VLM），实现图像理解、OCR 或多模态问答等复杂任务。
*   **科研与实验验证**：快速迭代实验不同模型架构、量化方案及微调算法的效果，加速 NLP 研究进程。

4. **技术亮点**
*   **全栈兼容性**：无缝衔接 Hugging Face Transformers 生态，同时支持 Flash Attention 等最新加速技术。
*   **低资源友好**：通过 QLoRA 等量化微调技术，允许在消费级显卡上高效训练千亿参数级别的大模型。
*   **模块化设计**：解耦数据处理、模型加载、训练引擎和导出模块，便于用户自定义扩展和集成。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73107 | 🍴 8932 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目从Anthropic、OpenAI、Google及xAI等主流大模型厂商中收集并提取了包括Claude、ChatGPT、Gemini等在内的系统提示词。内容涵盖Claude Fable 5、Opus 4.8、GPT 5.5 Thinking、Gemini 3.5 Flash等多个具体版本，并定期更新以反映最新模型配置。

2. **核心功能**
*   **多厂商提示词聚合**：整合来自Anthropic、OpenAI、Google、xAI等主要AI公司的系统指令。
*   **全模型覆盖**：包含聊天机器人、代码助手（如Cursor、Copilot）及视觉设计工具的系统提示。
*   **动态更新机制**：定期同步最新泄露或公开的系统提示词，保持数据时效性。
*   **开源共享平台**：作为社区驱动的数据库，供研究人员和开发者免费获取敏感配置信息。

3. **适用场景**
*   **提示词工程研究**：分析不同模型的底层指令结构，优化用户侧提示词策略。
*   **AI安全与红队测试**：识别系统提示中的潜在漏洞，评估模型的安全边界和防御机制。
*   **模型行为逆向分析**：通过对比官方系统提示与实际输出，探究特定模型的行为逻辑和限制。

4. **技术亮点**
*   **广泛的生态兼容性**：不仅限于文本生成模型，还涵盖了代码生成、图像设计及代理智能体等多种AI应用形态。
*   **高活跃度与维护频率**：拥有超过5.4万星标，表明其在AI社区中具有极高的关注度和持续的技术价值。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54569 | 🍴 8884 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
这是一套由微软发起的为期12周、包含24节课的人工智能通识课程，旨在让所有人轻松入门AI领域。课程采用Jupyter Notebook形式编写，内容涵盖机器学习、深度学习及自然语言处理等核心主题。该项目是初学者系统学习人工智能技术的优质资源。

2. **核心功能**
*   提供结构化的12周学习计划，将复杂的AI知识拆解为24个易于理解的课程模块。
*   基于Jupyter Notebook实现交互式教学，支持代码实时运行与结果可视化。
*   覆盖广泛的技术领域，包括机器学习基础、卷积神经网络(CNN)、循环神经网络(RNN)及生成对抗网络(GAN)等。
*   面向零基础人群设计，强调“人人可学”的理念，降低人工智能的学习门槛。
*   由微软开发者社区维护，确保内容的权威性与持续更新。

3. **适用场景**
*   **初学者自学**：适合对AI感兴趣但无编程或数学背景的自学者构建完整知识体系。
*   **高校/培训机构教学**：可作为计算机科学或数据科学专业的辅助教材或实践课程大纲。
*   **企业内训**：帮助非技术岗位员工快速理解人工智能基本概念与应用场景。
*   **快速原型验证**：通过现成的Notebook模板，快速上手并验证基础的AI算法效果。

4. **技术亮点**
*   **全栈覆盖**：从传统机器学习到前沿的深度学习和计算机视觉，提供端到端的学习路径。
*   **微软背书**：依托Microsoft For Beginners品牌，结合Azure AI服务示例，具备工业级参考价值。
*   **交互性强**：利用Jupyter Notebook的特性，将理论讲解、代码实现与实验结果紧密结合，提升学习效率。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51936 | 🍴 10492 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. 中文简介
该项目是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深入结合了线性代数基础及 PyTorch、NLTK、TensorFlow 2 等主流深度学习与自然语言处理框架。它旨在通过系统的代码实现，帮助学习者从理论到实践全面掌握人工智能核心技能。

### 2. 核心功能
*   **算法实战**：包含 K-Means、SVM、随机森林（AdaBoost）、Apriori 等经典机器学习和数据挖掘算法的代码实现。
*   **深度学习框架应用**：提供基于 PyTorch 和 TensorFlow 2 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）及卷积神经网络的实战案例。
*   **自然语言处理**：利用 NLTK 库进行文本处理、分词及基础 NLP 任务的分析与实现。
*   **数学基础强化**：结合线性代数知识，解析 PCA、SVD 等降维算法背后的数学原理及代码逻辑。
*   **推荐系统构建**：实现基于协同过滤和内容推荐的经典算法，展示如何构建简易推荐引擎。

### 3. 适用场景
*   **机器学习初学者入门**：适合希望从零开始系统学习 ML/DL 概念并动手写代码的学生或转行人员。
*   **高校课程辅助**：可作为计算机科学或数据科学专业学生复习线性代数、概率统计及算法实现的参考案例。
*   **面试准备与技能巩固**：适合求职者通过阅读高质量源码，快速回顾常见算法（如 SVM、KNN、LR）的实现细节以应对技术面试。
*   **NLP 与推荐系统专项研究**：针对需要快速搭建原型或理解特定领域（如文本分类、商品推荐）算法逻辑的开发者。

### 4. 技术亮点
*   **全栈覆盖**：不仅局限于算法模型，还涵盖了从数学基础（线性代数）到前沿框架（PyTorch/TF2）及第三方库（NLTK/sklearn）的完整技术栈。
*   **理论与实践并重**：每个算法模块均配有清晰的代码实现及相应的数学原理讲解，有助于深入理解“黑盒”背后的逻辑。
*   **高人气社区验证**：拥有超过 4.2 万星标，表明其内容质量、更新频率及社区认可度极高，是 GitHub 上极具影响力的 AI 学习仓库之一。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42365 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37702 | 🍴 6284 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33725 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28428 | 🍴 3460 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25855 | 🍴 2907 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款跨平台、支持任意操作系统的个人 AI 助手，旨在让你以“龙虾”的独特方式完全掌控自己的数据。它强调隐私与自主权，让用户在任何设备上都能轻松部署并拥有专属的智能助手。

2. **核心功能**
*   **全平台兼容**：支持在任意操作系统和平台上运行，实现无缝跨设备体验。
*   **数据自主权**：强调“Own Your Data”，确保用户数据的安全性与私有化存储。
*   **个人化定制**：作为专属个人助手，可根据用户需求进行个性化配置与交互。
*   **开源透明**：基于 TypeScript 开发，代码开放，便于社区贡献与安全审计。

3. **适用场景**
*   注重隐私安全的个人用户，希望在不依赖第三方云服务的情况下使用 AI 助手。
*   开发者或技术爱好者，希望在本地环境快速搭建并自定义个人 AI 代理。
*   需要跨设备协同工作的专业人士，寻求统一且私密的智能助理解决方案。

4. **技术亮点**
*   采用 TypeScript 编写，具备良好的类型安全和现代 Web 开发生态兼容性。
*   架构设计灵活，支持模块化扩展，便于集成不同的大语言模型后端。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382274 | 🍴 80209 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它通过子智能体驱动开发（Subagent-Driven Development）的方式，提供了一套切实可行的 AI 辅助编码流程。该项目旨在将人工智能深度整合到软件开发生命周期（SDLC）中，提升开发效率。

2. **核心功能**
*   提供基于智能体的技能框架，支持模块化的 AI 任务处理。
*   采用子智能体驱动开发模式，实现复杂代码任务的自动化分解与执行。
*   集成头脑风暴与需求分析功能，辅助开发者进行前期构思。
*   涵盖完整的软件开发生命周期（SDLC），从设计到编码再到测试。
*   通过 Shell 脚本实现轻量级且易于集成的开发工作流。

3. **适用场景**
*   希望利用 AI 智能体自动化处理重复性编码任务的开发团队。
*   需要结构化方法将大语言模型整合进现有 DevOps 流程的企业。
*   在复杂项目中寻求高效头脑风暴和方案设计的独立开发者。
*   探索“子智能体驱动开发”新范式的技术研究者和早期采用者。

4. **技术亮点**
*   概念创新：率先提出并实践“子智能体驱动开发”这一新兴软件工程范式。
*   高人气验证：拥有超过 25 万颗 GitHub Star，证明其广泛的社区认可度和实用性。
*   全栈覆盖：不仅限于代码生成，还涵盖了从创意构思到最终交付的完整 SDLC 环节。
- 链接: https://github.com/obra/superpowers
- ⭐ 250302 | 🍴 22207 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211827 | 🍴 38985 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195769 | 🍴 59190 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建人工智能，实现 AI 的普及化愿景。通过提供强大的工具支持，它旨在帮助用户从繁琐的技术细节中解脱出来，从而专注于真正重要的事情。

2. **核心功能**
- 具备自主规划与执行复杂任务的能力，无需人工逐步干预。
- 集成多种大型语言模型（如 GPT、Claude、Llama），支持灵活的 API 调用。
- 拥有智能体（Agent）架构，能够自我反思、记忆及跨工具协作。
- 提供开源生态，允许开发者基于其框架进行二次开发和功能扩展。
- 强调易用性，降低构建自主 AI 应用的门槛。

3. **适用场景**
- 自动化日常业务流程，如数据抓取、报告生成和信息整理。
- 作为开发者的基础框架，构建具有特定领域知识的定制智能体。
- 进行复杂的长期项目研究，智能体可自主分解目标并搜集相关资料。
- 探索多模型协同工作的实验场景，测试不同 LLM 在自治任务中的表现。

4. **技术亮点**
- 采用模块化设计，支持无缝切换不同后端 LLM 提供商（OpenAI、Anthropic 等）。
- 实现了完整的“感知-决策-行动”循环，具备自我纠错和迭代优化能力。
- 社区驱动的开发模式，拥有极高的星标数和活跃的开源贡献者生态。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185435 | 🍴 46116 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165123 | 🍴 21367 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164049 | 🍴 30400 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156910 | 🍴 46170 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151406 | 🍴 9481 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148269 | 🍴 23360 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

