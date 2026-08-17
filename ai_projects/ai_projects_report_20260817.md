# GitHub AI项目每日发现报告
日期: 2026-08-17

## 新发布的AI项目

### zhijian-ai-bluebook-workbuddy-harness
- 

## GitHub 项目分析：zhijian-ai-bluebook-workbuddy-harness

### 1. 中文简介
本项目是智见 AI 蓝皮书系列之一，系统性地拆解了 WorkBuddy 智能体的核心架构，涵盖提示词设计、记忆机制、插件系统、专家配置、Skill 构建以及安全边界等关键模块，为 AI 智能体开发提供实战参考。

### 2. 核心功能
- **提示词工程拆解**：解析 WorkBuddy 的提示词结构与优化策略
- **记忆机制分析**：梳理智能体短期与长期记忆的存储与调用方式
- **插件系统解读**：说明插件架构设计与扩展机制
- **专家与 Skill 配置**：介绍专家角色定义与技能模块的构建方法
- **安全边界设定**：明确智能体的权限控制与安全限制策略

### 3. 适用场景
- AI 智能体开发者学习 WorkBuddy 架构设计
- 企业级智能体安全边界与权限管理参考
- 提示词工程与记忆系统优化实践
- 插件化智能体系统的二次开发

### 4. 技术亮点
- 蓝皮书形式提供系统化、结构化的智能体知识体系
- 聚焦安全边界，弥补智能体落地中的关键风险点
- 覆盖从提示词到插件的完整技术链路，实用性强

---

> ⚠️ 注：本项目编程语言为 None，星标数 135，属于文档/知识整理类项目，适合学习和参考，而非直接运行的代码库。
- 链接: https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness
- ⭐ 135 | 🍴 13 | 语言: 未知
- 标签: ai-agent, bluebook, harness, workbuddy, zhijian-ai

### ai-data-extractor
- 

## AI Data Extractor 项目分析

### 1. 中文简介
这是一个免费的开源工具，用于提取 AI 编程助手的历史对话记录。支持 Claude Code、Cursor、Windsurf、Aider、Cline/Roo Code 等多种主流 AI 编程工具。

### 2. 核心功能
- 自动提取 AI 编程助手的聊天历史记录
- 支持多种主流 AI 编程工具（Claude Code、Cursor、Windsurf 等）
- 将对话数据导出为结构化格式，便于后续分析和使用
- 开源免费，可自定义扩展支持更多工具

### 3. 适用场景
- 备份和归档 AI 编程助手的对话历史，防止数据丢失
- 分析 AI 编程助手的交互模式，优化提示词策略
- 迁移对话数据到新的 AI 编程工具
- 对 AI 编程助手的使用数据进行统计分析和复盘

### 4. 技术亮点
- 使用 Python 编写，代码简洁易维护
- 支持多平台数据提取，兼容性强
- 开源项目，社区可共同参与维护和扩展
- 链接: https://github.com/bawadou/ai-data-extractor
- ⭐ 63 | 🍴 26 | 语言: Python
- 标签: ai, ai-data-extractor, claude, cursor, cursor-ai

### graph-memory-starter
- 

# GitHub项目分析：graph-memory-starter

## 1. 中文简介
这是一个为AI助手构建的知识图谱记忆系统。通过三个SQLite表、一条递归查询和一个提示词钩子，实现对话历史的图结构存储与检索。

## 2. 核心功能
- 基于SQLite的知识图谱记忆存储
- 递归查询支持多跳关系推理
- 提示词钩子集成，自动注入上下文
- 轻量级三表结构设计
- Python语言实现，易于集成

## 3. 适用场景
- AI助手的长期记忆管理
- 多轮对话上下文追踪
- 知识图谱驱动的问答系统
- 需要关系推理的智能应用

## 4. 技术亮点
- **极简设计**：仅三张表实现完整图谱记忆，降低部署复杂度
- **递归查询**：支持多跳关系探索，提升上下文召回质量
- **钩子架构**：通过prompt hook无缝接入现有AI框架，无需大幅改造
- 链接: https://github.com/Glitch-Cat-Club/graph-memory-starter
- ⭐ 53 | 🍴 4 | 语言: Python

### deepseek-harness-pr-review
- 

## deepseek-harness-pr-review 项目分析

### 1. 中文简介
基于DeepSeek的AI代码审查工具，可自动逐条验证PR描述与真实代码的一致性，并检查文档是否符合实际情况。支持人机协作模式，配备自动审查轮询器和Web仪表板，实现高效的PR自动化审查流程。

### 2. 核心功能
- 使用DeepSeek API进行AI驱动的代码审查
- 逐条验证PR描述声明与实际代码的一致性
- 检查文档内容是否符合代码实际情况
- 自动标记需求变更的影响范围
- 支持人机协作审查 + 自动轮询 + Web仪表板监控

### 3. 适用场景
- 希望自动化PR审查流程的开源或商业项目团队
- 需要验证PR描述准确性、防止虚假声明的场景
- 要求文档与代码保持同步的技术项目
- 希望集成到CI/CD流水线的无头自动化审查需求

### 4. 技术亮点
- 基于DeepSeek大模型的智能代码分析能力
- 无头模式设计，便于集成到自动化流水线
- 提供Web仪表板实现审查过程可视化监控
- 人机协作机制确保关键决策仍由开发者把控
- 链接: https://github.com/nexpeakcore/deepseek-harness-pr-review
- ⭐ 30 | 🍴 10 | 语言: Python
- 标签: agentic-ai, ai-agent, ai-code-review, automation, automation-tools

### ai-tools-radar
- 

# GitHub 项目分析：ai-tools-radar

## 1. 中文简介
这是一个本地运行的 AI 工具站增长情报库，提供真实流量数据、增长曲线追踪、新品发现雷达以及 dofollow 外链数据库，帮助开发者快速掌握 AI 工具市场的动态与机会。

## 2. 核心功能
- **流量数据追踪**：提供 AI 工具站的真实流量数据与增长曲线分析
- **新品发现雷达**：实时监控并推送新上线的 AI 工具项目
- **外链资源库**：收录 dofollow 外链资源，助力 SEO 优化
- **本地化部署**：支持本地运行，无需依赖云端服务
- **增长情报汇总**：整合多维度增长数据，辅助决策分析

## 3. 适用场景
- AI 工具创业者追踪竞品流量与增长趋势
- SEO 从业者挖掘 AI 工具站的外链合作机会
- 市场研究人员分析 AI 工具行业的新品动态
- 独立开发者寻找流量增长灵感与合作伙伴

## 4. 技术亮点
- **本地运行**：无需云端 API，数据隐私性更强
- **Python 实现**：生态丰富，便于二次开发与集成
- **情报聚合**：整合流量、增长、外链等多维度数据源
- 链接: https://github.com/ppop123/ai-tools-radar
- ⭐ 28 | 🍴 19 | 语言: Python

### dance-video-to-prompt
- 描述: 本地短视频反推 AI 视频生成提示词：抽帧、清晰度、节奏卡点、Agent Skill
- 链接: https://github.com/CattleZ/dance-video-to-prompt
- ⭐ 27 | 🍴 1 | 语言: Python

### idor-tester-ai
- 描述: 无描述
- 链接: https://github.com/poriaporhashemi/idor-tester-ai
- ⭐ 20 | 🍴 2 | 语言: Python

### Alvarmethod
- 描述: One-to-one AI teaching skills (Alvar method) for Codex, Claude Code, Grok, Pi, and OpenCode
- 链接: https://github.com/vasanthsreeram/Alvarmethod
- ⭐ 18 | 🍴 2 | 语言: Shell

### z-ai-whitepaper
- 描述: 无描述
- 链接: https://github.com/tjxj/z-ai-whitepaper
- ⭐ 16 | 🍴 2 | 语言: Shell

### Scientific-Ai
- 描述: A new scientific Ai tool integrating both codex and Claude using mpc
- 链接: https://github.com/rharir35-netizen/Scientific-Ai
- ⭐ 13 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82508 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub 项目分析：500 AI 机器学习/深度学习项目合集

---

### 1. 中文简介

这是一个收录了 **500 个 AI 项目**的精选资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大方向，每个项目均附带完整代码实现。项目累计获得 **36,325 颗星标**，是中文社区中最受欢迎的 AI 学习资源之一。

---

### 2. 核心功能

- **项目数量庞大**：收录 500 个真实可运行的 AI 项目，覆盖主流算法与框架
- **全栈代码支持**：每个项目均提供完整 Python 代码，可直接克隆运行
- **四大方向分类**：按机器学习、深度学习、计算机视觉、NLP 清晰分组
- **适合不同水平**：从入门到进阶均有对应项目，便于循序渐进学习
- **持续更新维护**：定期添加新项目，紧跟 AI 领域最新进展

---

### 3. 适用场景

- **AI 初学者系统学习**：按分类逐个实践，建立完整的机器学习知识体系
- **求职/面试准备**：用项目代码作为技术面试的作品集展示
- **企业项目快速原型**：直接参考现有代码，加速内部 AI 功能开发
- **高校课程教学辅助**：教师可用其作为实验课的项目参考来源

---

### 4. 技术亮点

- **Python 全栈实现**：统一使用 Python，降低学习切换成本
- **标签体系完善**：以 `awesome`、`machine-learning-projects` 等标签便于检索
- **社区认证质量**：36,325 星标证明其广泛认可和实用性
- **覆盖主流框架**：项目涵盖 TensorFlow、PyTorch、scikit-learn 等主流工具

---

> **一句话总结**：这是一个"AI 项目百科全书"，适合从入门到实战的全链路学习，尤其适合需要快速构建 AI 项目经验的学习者和开发者。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36325 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具，支持多种主流模型格式的浏览与解析，帮助用户直观理解模型结构与参数。

### 2. 核心功能
- 支持多种模型格式（ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、SafeTensors 等）
- 以图形化方式展示神经网络层级结构与数据流向
- 可交互式查看模型参数、权重及张量维度信息
- 提供简洁的 Web 界面，无需安装额外依赖即可运行
- 支持模型结构对比与错误检测

### 3. 适用场景
- 深度学习模型开发过程中的结构审查与调试
- 将模型从一种框架转换到另一种框架时的格式验证
- 向团队或客户展示模型架构与推理流程
- 学习理解复杂神经网络结构的教学与研究

### 4. 技术亮点
- 纯前端实现（JavaScript），基于浏览器即可运行，部署与使用门槛极低
- 支持 safetensors 等新兴安全格式，紧跟社区发展
- 星标数超过 3.3 万，是 AI 模型可视化领域最受欢迎的开源工具之一
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33362 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个开源标准，旨在实现机器学习模型的互操作性。它允许开发者在不同深度学习框架之间自由迁移模型，打破框架间的壁垒。

### 2. 核心功能
- **跨框架模型转换**：支持将模型从PyTorch、TensorFlow、Keras等框架导出为ONNX格式
- **统一模型表示**：定义了一套标准化的算子和数据结构，用于描述神经网络
- **推理优化**：提供模型优化工具链，提升推理性能和效率
- **多平台部署**：支持在不同硬件平台（CPU、GPU、移动端）上运行模型

### 3. 适用场景
- 需要在不同深度学习框架间迁移模型时
- 将训练好的模型部署到生产环境时
- 对模型进行跨平台推理优化时
- 构建模型转换和互操作工作流时

### 4. 技术亮点
- 由Microsoft、Facebook等科技巨头联合推动，生态成熟
- 支持超过100种算子，覆盖主流神经网络结构
- 提供完整的工具链，包括转换、优化、可视化等功能
- 与主流深度学习框架无缝集成，社区活跃
- 链接: https://github.com/onnx/onnx
- ⭐ 21319 | 🍴 4000 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## GitHub项目分析：ml-engineering

### 1. 中文简介
这是一本关于机器学习工程实践的开卷书籍，全面涵盖了从模型训练到部署推理的全链路工程知识。内容涉及大规模语言模型（LLM）的训练、调试、推理优化及可扩展性部署等核心主题。

### 2. 核心功能
- 提供机器学习工程领域的系统性知识体系与最佳实践指南
- 覆盖GPU训练、模型调试、推理优化等关键工程环节
- 包含大规模语言模型（LLM）的训练与部署实战经验
- 涉及PyTorch、Transformers等主流框架的工程化应用
- 涵盖MLOps、网络、存储、Slurm调度等基础设施相关内容

### 3. 适用场景
- 大规模语言模型（LLM）的训练与推理工程实践
- 机器学习系统的可扩展性设计与性能优化
- MLOps平台搭建与模型生产环境部署
- GPU集群管理、调试与故障排查

### 4. 技术亮点
- 作为"开卷书籍"形式，内容开源共享，便于社区持续贡献与更新
- 聚焦工程实践，填补了从理论研究到生产部署之间的知识空白
- 覆盖全栈ML工程链路，从底层硬件（GPU、网络、存储）到上层应用（训练、推理）均有涉及
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18643 | 🍴 1201 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17359 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13261 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11626 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10687 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub 项目分析：500 AI 机器学习/深度学习项目合集

---

### 1. 中文简介

这是一个收录了 **500 个 AI 项目**的精选资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大方向，每个项目均附带完整代码实现。项目累计获得 **36,325 颗星标**，是中文社区中最受欢迎的 AI 学习资源之一。

---

### 2. 核心功能

- **项目数量庞大**：收录 500 个真实可运行的 AI 项目，覆盖主流算法与框架
- **全栈代码支持**：每个项目均提供完整 Python 代码，可直接克隆运行
- **四大方向分类**：按机器学习、深度学习、计算机视觉、NLP 清晰分组
- **适合不同水平**：从入门到进阶均有对应项目，便于循序渐进学习
- **持续更新维护**：定期添加新项目，紧跟 AI 领域最新进展

---

### 3. 适用场景

- **AI 初学者系统学习**：按分类逐个实践，建立完整的机器学习知识体系
- **求职/面试准备**：用项目代码作为技术面试的作品集展示
- **企业项目快速原型**：直接参考现有代码，加速内部 AI 功能开发
- **高校课程教学辅助**：教师可用其作为实验课的项目参考来源

---

### 4. 技术亮点

- **Python 全栈实现**：统一使用 Python，降低学习切换成本
- **标签体系完善**：以 `awesome`、`machine-learning-projects` 等标签便于检索
- **社区认证质量**：36,325 星标证明其广泛认可和实用性
- **覆盖主流框架**：项目涵盖 TensorFlow、PyTorch、scikit-learn 等主流工具

---

> **一句话总结**：这是一个"AI 项目百科全书"，适合从入门到实战的全链路学习，尤其适合需要快速构建 AI 项目经验的学习者和开发者。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36325 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具，支持多种主流模型格式的浏览与解析，帮助用户直观理解模型结构与参数。

### 2. 核心功能
- 支持多种模型格式（ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、SafeTensors 等）
- 以图形化方式展示神经网络层级结构与数据流向
- 可交互式查看模型参数、权重及张量维度信息
- 提供简洁的 Web 界面，无需安装额外依赖即可运行
- 支持模型结构对比与错误检测

### 3. 适用场景
- 深度学习模型开发过程中的结构审查与调试
- 将模型从一种框架转换到另一种框架时的格式验证
- 向团队或客户展示模型架构与推理流程
- 学习理解复杂神经网络结构的教学与研究

### 4. 技术亮点
- 纯前端实现（JavaScript），基于浏览器即可运行，部署与使用门槛极低
- 支持 safetensors 等新兴安全格式，紧跟社区发展
- 星标数超过 3.3 万，是 AI 模型可视化领域最受欢迎的开源工具之一
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33362 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图项目，收录了近200个实战案例与项目，并免费提供配套教材，适合零基础学习者入门并迈向就业实战。涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域，是AI学习者的优质资源库。

### 2. 核心功能
- 提供系统化的AI学习路线图，帮助学习者循序渐进掌握核心知识
- 整理近200个实战案例与项目，覆盖主流AI技术栈
- 免费提供配套教材，降低学习门槛
- 支持零基础入门，兼顾就业实战需求
- 覆盖多框架生态（PyTorch、TensorFlow、Keras等）

### 3. 适用场景
- **AI初学者**：从零开始系统学习人工智能相关知识体系
- **求职者**：通过实战项目积累面试经验与项目作品集
- **在校学生**：将课堂理论与实际项目相结合，提升实践能力
- **转行人员**：快速掌握AI核心技能，实现职业转型

### 4. 技术亮点
- 项目热度高，星标数达13261，社区认可度强
- 技术栈全面，覆盖从基础（Python、Numpy、Pandas）到进阶（深度学习、NLP、CV）的完整链路
- 多框架支持，兼容PyTorch、TensorFlow 1/2、Keras、Caffe等主流深度学习框架
- 实战导向，提供大量可直接复现的项目案例
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13261 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它简化了机器学习模型的训练、评估和部署流程，适合快速迭代实验。

## 2. 核心功能
- 低代码快速构建和训练深度学习模型，降低开发门槛
- 支持多种模态（文本、图像、表格等）的端到端模型开发
- 提供可视化训练过程与模型评估指标
- 内置多种预训练模型架构，支持迁移学习与微调
- 兼容 PyTorch 生态，便于扩展和集成

## 3. 适用场景
- 数据科学家快速原型开发，无需编写大量代码即可验证模型想法
- 企业级 LLM 微调与部署，针对特定领域进行定制化训练
- 多模态 AI 应用开发，如结合文本与图像的智能系统
- 教学与实验场景，帮助学生和研究人员理解深度学习流程

## 4. 技术亮点
- 基于 YML 配置文件驱动模型构建，声明式开发体验简洁高效
- 支持 Hugging Face Transformers 集成，无缝衔接主流 LLM 生态
- 内置 AutoML 功能，自动搜索最优超参数组合
- 提供 Web UI 界面，方便非技术用户参与模型训练与评估
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9174 | 🍴 1232 | 语言: Python
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
- ⭐ 6991 | 🍴 1174 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6406 | 🍴 778 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82508 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目成果已发表于 ACL 2024 学术会议，致力于降低大模型微调的技术门槛。

### 2. 核心功能
- 支持 100+ 种大语言模型和视觉语言模型的高效微调
- 提供多种微调方法，包括 LoRA、QLoRA、全参数微调等
- 支持 RLHF（基于人类反馈的强化学习）和 DPO 等对齐技术
- 兼容主流框架如 Hugging Face Transformers 和 PEFT
- 支持量化部署，降低显存占用

### 3. 适用场景
- 研究人员和开发者快速微调 LLaMA、Qwen、DeepSeek、Gemma 等开源模型
- 企业级应用中对大模型进行指令微调（Instruction Tuning）
- 资源受限环境下使用 QLoRA 进行低显存微调
- 多模态视觉语言模型的微调与部署

### 4. 技术亮点
- 统一接口支持上百种模型，无需为每种模型单独编写代码
- 高度优化的训练流程，兼顾效率与显存节约
- 完整的微调生态，涵盖预训练、指令微调、RLHF 全流程
- ACL 2024 学术认可，具备专业可靠性
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74159 | 🍴 9075 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

---

## 1. 中文简介

这是由微软推出的AI入门课程项目，为期12周、共24节课，旨在让所有人都能轻松学习人工智能。课程采用Jupyter Notebook形式，涵盖从基础概念到深度学习实践的完整学习路径。

---

## 2. 核心功能

- 系统化的12周AI课程体系，循序渐进地引导学习者掌握人工智能核心知识
- 涵盖机器学习、深度学习、计算机视觉、自然语言处理等主流AI领域
- 实践导向的Jupyter Notebook示例，便于动手操作与即时验证
- 包含CNN、RNN、GAN等前沿深度学习模型的教学内容
- 免费开源，适合自学者按自身节奏灵活学习

---

## 3. 适用场景

- 零基础学习者希望系统入门人工智能领域
- 高校教师或培训机构用于AI相关课程教学
- 企业内训中需要快速培养员工AI基础能力
- 对AI感兴趣的开发者希望拓展技术栈

---

## 4. 技术亮点

- 由微软官方出品，课程质量与权威性有保障
- 标签覆盖全面，从传统机器学习到前沿深度学习均有涉及
- 高星标（65101）说明社区认可度高，学习资源丰富
- 以Jupyter Notebook为载体，实现"学练结合"的互动式学习体验
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65101 | 🍴 12642 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# GitHub 项目分析：ai-engineering-from-scratch

## 1. 中文简介
从零开始学习人工智能工程，通过实践构建项目，最终为他人交付可用成果。这是一个系统性的 AI 工程课程，帮助学习者掌握从基础到实战的完整技能链。

## 2. 核心功能
- **从零开始的系统性教学**：涵盖 AI 工程全链路，从理论到实践循序渐进
- **多技术栈支持**：使用 Python、Rust、TypeScript 等多种语言实现
- **AI Agent 开发**：涵盖智能体、MCP（模型上下文协议）及群体智能
- **深度学习与生成式 AI**：包含 LLM、Transformers、计算机视觉、NLP 等核心领域
- **强化学习实践**：提供强化学习算法的完整教程

## 3. 适用场景
- **AI 初学者系统学习**：希望从零建立完整 AI 知识体系的学习者
- **AI 工程师技能提升**：需要深入理解 AI 底层原理并实践构建的开发者
- **AI 项目实战参考**：寻找可复用的 Agent、LLM 应用构建方案的工程师
- **技术课程教学资源**：教师或培训者用于 AI 工程教学的参考材料

## 4. 技术亮点
- 涵盖前沿的 MCP（Model Context Protocol）协议，支持 AI Agent 与工具交互
- 结合 Rust 语言实现高性能 AI 组件，兼顾 Python 的易用性
- 从理论到部署的完整工程化路径，强调"学以致用"的实战理念
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 46975 | 🍴 8223 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：AiLearning

### 1. 中文简介
AiLearning是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK和TensorFlow 2的综合学习项目。该项目整合了从数学基础到深度学习框架的完整知识体系，适合系统性学习人工智能技术。

### 2. 核心功能
- 覆盖经典机器学习算法：SVM、KMeans、逻辑回归、朴素贝叶斯、AdaBoost、PCA等
- 提供深度学习实战：基于PyTorch和TensorFlow 2的DNN、RNN、LSTM等网络实现
- 包含自然语言处理（NLP）模块：基于NLTK的文本处理与深度学习NLP实践
- 集成推荐系统与关联规则算法：FP-Growth、Apriori等
- 补充线性代数等数学基础，夯实机器学习理论根基

### 3. 适用场景
- 机器学习初学者系统入门，建立完整知识体系
- 数据科学从业者提升算法实战能力
- 准备AI/ML岗位面试的求职者，作为刷题与知识复习资料
- 高校学生将课堂理论与代码实践相结合

### 4. 技术亮点
项目将数学基础（线性代数）与主流框架（PyTorch、TF2）结合，提供从理论到代码的完整闭环；标签覆盖全面，涵盖监督学习、无监督学习、深度学习、NLP和推荐系统，是一个"一站式"AI学习资源库。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42459 | 🍴 11517 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36325 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33825 | 🍴 4709 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29083 | 🍴 3540 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21840 | 🍴 3354 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17359 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
该项目是一个包含500个AI项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域，每个项目均附带完整代码实现。作为一个全面的Awesome列表，它为开发者提供了从入门到进阶的丰富实践案例。

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大方向。
- 所有项目均附带可运行的代码，便于学习者直接上手实践。
- 按领域分类整理，结构清晰，方便快速查找感兴趣的项目。
- 包含数据科学相关内容，适合不同层次的学习者参考使用。
- 持续更新维护，保持项目库的时效性和丰富度。

### 3. 适用场景
- **AI学习者**：作为系统学习机器学习、深度学习的实践项目来源。
- **开发者面试准备**：通过参考高质量项目代码提升技术能力。
- **项目灵感参考**：寻找计算机视觉或NLP方向的开源项目参考。
- **教学与培训**：教师或培训机构用于课程设计中的实战案例。

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主要子领域，资源极为丰富。
- 每个项目均配有代码，强调实战性而非纯理论。
- 标签分类完善，涵盖 `machine-learning`、`deep-learning`、`computer-vision`、`nlp` 等关键词，便于检索。
- 星标数高达36325，说明社区认可度极高，是一个经过广泛验证的优质资源库。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36325 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22767 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（Computer Vision Annotation Tool）是一款领先的计算机视觉标注平台，专注于构建高质量的视觉数据集。它提供开源、云和企业级产品，支持图像、视频及3D标注，并配备AI辅助标注、质量保证、团队协作等核心功能。

## 2. 核心功能
- **多模态标注支持**：支持图像、视频和3D点云数据的高效标注。
- **AI辅助标注**：集成AI模型辅助自动标注，大幅提升标注效率。
- **团队协作**：支持多人协同标注与任务分配，便于团队分工管理。
- **质量保证机制**：提供标注审核与质量评估功能，确保数据集质量。
- **开发者API**：开放API接口，便于集成到现有工作流中。

## 3. 适用场景
- **深度学习数据集构建**：用于目标检测、语义分割等任务的标注数据生产。
- **自动驾驶与3D感知**：支持3D点云标注，适用于自动驾驶场景开发。
- **企业级标注团队**：适合需要多人协作、流程管控的大规模标注项目。

## 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）的集成与导出。
- 提供从开源版到企业版的灵活部署方案，满足不同规模需求。
- 拥有活跃的开源社区，星标数超过16500，生态成熟。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16538 | 🍴 3804 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，专为深度学习场景设计。它提供了基于 PyTorch 的可微分图像处理与计算机视觉算子，支持端到端的神经网络训练。

### 2. 核心功能
- 提供丰富的可微分几何视觉算子，支持梯度反向传播
- 集成图像处理功能，如图像变换、滤波和色彩空间转换
- 兼容 PyTorch 生态，可直接嵌入深度学习模型训练流程
- 支持机器人和空间智能应用的几何计算需求

### 3. 适用场景
- 深度学习驱动的图像处理和计算机视觉任务开发
- 机器人视觉与空间感知系统的构建
- 需要端到端可微分处理管道的神经网络设计
- 几何视觉算法的快速原型开发与实验

### 4. 技术亮点
- 完全基于 PyTorch 实现，充分利用 GPU 加速计算
- 算子设计注重可微分性，便于集成到深度学习框架中
- 社区活跃，支持 Hacktoberfest 等开源贡献活动
- 链接: https://github.com/kornia/kornia
- ⭐ 11314 | 🍴 1223 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2189 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3479 | 🍴 880 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3379 | 🍴 412 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2506 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## openclaw 项目分析

### 1. 中文简介
openclaw 是一款完全属于你自己的个人 AI 助手，支持任意操作系统和平台运行。它采用"龙虾方式"，让你真正掌控自己的数据和 AI 体验。

### 2. 核心功能
- 支持跨平台、跨操作系统运行，灵活部署
- 本地化 AI 助手，数据完全由用户自主掌控
- 基于 TypeScript 开发，具备跨平台兼容性
- 提供个性化 AI 助手服务，满足个人使用需求

### 3. 适用场景
- 注重数据隐私的个人用户，希望 AI 数据不上传云端
- 需要在不同操作系统（Windows/Mac/Linux）间切换使用的用户
- 开发者希望自定义和扩展 AI 助手功能的场景

### 4. 技术亮点
- 使用 TypeScript 编写，类型安全且开发体验良好
- 支持多平台部署，灵活适配不同运行环境
- 开源项目，社区活跃，星标数超过 38 万，表明较高的用户认可度
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386508 | 🍴 81220 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub项目分析：superpowers

### 1. 中文简介
这是一个基于智能体技能的框架和软件开发方法论，旨在提供一套行之有效的AI驱动开发流程。项目聚焦于通过子智能体协作来推动软件开发全过程。

### 2. 核心功能
- **智能体技能框架**：提供可复用的AI技能模块，支持自动化开发任务
- **子智能体驱动开发**：通过多个子智能体协作完成复杂开发工作
- **完整SDLC支持**：覆盖软件开发生命周期各阶段的工作流
- **头脑风暴与编码辅助**：集成创意构思和代码编写能力
- **OBRA方法论**：提供结构化的开发流程指导

### 3. 适用场景
- AI辅助的软件项目开发与架构设计
- 需要多智能体协作的复杂编码任务
- 希望通过AI提升开发效率的团队
- 探索新型AI驱动开发方法论的实践者

### 4. 技术亮点
- 采用Shell脚本实现，轻量级且易于集成
- 高人气项目（近27万星标），社区活跃度高
- 将AI智能体与软件开发方法论深度结合的创新实践
- 链接: https://github.com/obra/superpowers
- ⭐ 272994 | 🍴 24410 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
Hermes Agent 是一个能够随着用户共同成长的人工智能代理。它支持多种主流大语言模型，为用户提供灵活、智能的对话与任务执行能力。

### 2. 核心功能
- 支持多种大语言模型（Claude、Codex、ChatGPT 等）的无缝切换与调用
- 提供智能对话与任务自动化执行能力
- 具备持续学习与记忆能力，可随使用不断优化
- 开源可定制，由 Nous Research 维护开发

### 3. 适用场景
- 日常智能助手，处理复杂对话与多轮任务
- 开发者辅助编程，代码生成与问题排查
- 企业级 AI 代理部署，集成到工作流中

### 4. 技术亮点
- 多模型兼容架构，支持 Anthropic、OpenAI 等主流 LLM
- 开源项目，社区活跃，星标数超过 23 万
- 由知名 AI 研究团队 Nous Research 主导开发，技术可靠性高
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 231753 | 🍴 46126 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款采用公平代码许可的工作流自动化平台，内置原生 AI 能力。它支持可视化构建与自定义代码相结合，提供自托管和云端两种部署方式，并拥有 400+ 种集成连接。

### 2. 核心功能
- **可视化工作流构建**：通过拖拽方式创建复杂自动化流程，无需编写代码即可快速上手
- **原生 AI 能力集成**：内置 AI 节点，可直接在工作流中调用大语言模型进行智能处理
- **400+ 集成生态**：覆盖主流 SaaS 工具、API 服务和数据库，支持 MCP 协议实现模型上下文协议集成
- **灵活部署方式**：支持自托管部署保障数据隐私，也可使用云端服务快速启动
- **低代码+自定义代码混合开发**：既提供低代码/无代码节点，也支持 TypeScript 自定义代码扩展

### 3. 适用场景
- **企业自动化办公**：自动化处理邮件、日历、文档协作等日常办公流程
- **数据管道与 ETL**：从多源采集数据、清洗转换后写入目标系统
- **AI 应用开发**：快速构建 RAG 系统、AI Agent 和智能工作流应用
- **API 集成与 iPaaS**：连接 disparate 系统，实现跨平台数据同步和业务协同

### 4. 技术亮点
- 基于 TypeScript 构建，类型安全且易于扩展开发
- 支持 MCP（Model Context Protocol）客户端/服务器模式，可与主流 AI 模型无缝对接
- 公平代码许可（Fair-code）模式，兼顾开源生态与商业可持续性
- 社区活跃，星标数超过 20 万，生态完善
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200941 | 🍴 60185 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于实现"人人可用的AI"愿景，让每个人都能使用并在此基础上构建应用。我们的使命是提供强大工具，让你能够专注于真正重要的事。

### 2. 核心功能
- **自主任务执行**：自动分解复杂目标并逐步执行，无需人工干预
- **多模型支持**：兼容OpenAI GPT系列、Claude、Llama等多种大语言模型
- **丰富工具生态**：内置网络搜索、文件操作、代码执行等实用工具
- **长期记忆系统**：跨任务保持上下文连贯，实现持久记忆
- **可扩展架构**：模块化设计，支持用户自定义和扩展功能

### 3. 适用场景
- **自动化工作流**：市场调研、数据分析、报告生成等重复性任务
- **代码开发辅助**：自动生成代码、调试、测试等开发流程
- **研究助手**：信息搜集、文献综述、知识整理等研究支持
- **内容创作**：文案撰写、社交媒体内容生成等创意工作

### 4. 技术亮点
- 基于最新大语言模型的自主决策与规划能力
- 灵活的工具链集成架构，支持第三方工具扩展
- 多LLM后端兼容，可根据需求切换模型提供商
- 活跃的开源社区，持续迭代更新
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186634 | 🍴 46061 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 168371 | 🍴 9418 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167290 | 🍴 21592 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164527 | 🍴 30552 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157813 | 🍴 46175 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153341 | 🍴 9872 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

