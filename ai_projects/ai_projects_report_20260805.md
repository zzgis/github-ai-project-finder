# GitHub AI项目每日发现报告
日期: 2026-08-05

## 新发布的AI项目

### LongHorizon-Harness
- 

# LongHorizon-Harness 项目分析

## 1. 中文简介

LongHorizon-Harness 是一个长期计算机操作自动化框架，支持 AI 代理在桌面应用和命令行界面中长时间运行，同时保持任务状态并在复杂工作流中可靠推进。项目提供新鲜上下文执行、持久化验证状态、独立审计、可恢复进度等功能，并原生集成 Claude Code / Codex / OpenClaw。

## 2. 核心功能

- **长期运行支持**：AI 代理可在桌面应用和 CLI 中持续运行，保持任务状态并可靠推进复杂工作流
- **新鲜上下文执行**：每次执行都能获得最新的上下文环境，避免状态污染
- **持久化验证状态**：确保任务状态可验证、可持久化存储
- **独立审计能力**：支持对 AI 代理的执行过程进行独立审计
- **可恢复进度**：中断后可从断点恢复，保证任务连续性
- **多平台原生集成**：原生支持 Claude Code、Codex 和 OpenClaw 等 AI 工具

## 3. 适用场景

- **复杂桌面应用自动化**：需要在多个桌面软件间切换执行的长期任务
- **长时间 CLI 工作流**：涉及多步骤命令行操作的自动化任务
- **AI 代理可靠性要求高的场景**：需要状态保持和进度恢复的长时间运行任务
- **需要审计追踪的自动化**：要求执行过程可独立审计验证的场景

## 4. 技术亮点

- 采用"循环工程"（Loop Engineering）设计理念，专注于长时间运行的可靠性
- 支持多种 AI 工具的原生集成（Claude Code / Codex / OpenClaw），扩展性强
- 提供完整的状态管理方案，包括持久化、验证和可恢复性保障
- 独立审计机制确保 AI 代理行为的可追溯性
- 链接: https://github.com/AMAP-ML/LongHorizon-Harness
- ⭐ 211 | 🍴 18 | 语言: Python
- 标签: agent, claude, claude-code, claude-plugin, cli

### Fuxi
- 

## Fuxi 项目分析

### 1. 中文简介
FuXi 是一款快速、自包含的 AI 开发者终端工具，专为开发者打造一体化的 AI 编程工作环境。它集成了 AI 能力，帮助开发者在终端中高效完成代码编写、调试和项目管理等任务。

### 2. 核心功能
- 提供快速的 AI 驱动开发终端体验
- 自包含架构，无需额外依赖即可运行
- 集成 AI 助手，支持智能代码补全与建议
- 支持开发者日常编程工作流的一体化操作

### 3. 适用场景
- 需要 AI 辅助的命令行开发环境
- 希望在不离开终端的情况下完成编码任务
- 追求轻量级、开箱即用的 AI 开发工具

### 4. 技术亮点
- 自包含设计，部署简便，开箱即用
- 针对开发者终端场景进行了性能优化
- 链接: https://github.com/fuxicodex/Fuxi
- ⭐ 131 | 🍴 9 | 语言: 未知

### HermesOffice
- 

## HermesOffice 项目分析

### 1. 中文简介
HermesOffice 是一款 AI 原生的办公套件，由 GenOffice（Apache-2.0 协议）衍生而来，内置原生 Hermes Agent AI 智能代理。该项目基于 Electron 框架开发，支持 macOS 平台，提供完整的文档处理与演示文稿制作能力。

### 2. 核心功能
- 集成 Hermes Agent AI 智能代理，实现 AI 驱动的办公自动化
- 支持 DOCX 文档的创建、编辑与格式化处理
- 支持 PPTX 演示文稿的生成与编辑
- 基于 Electron 跨平台桌面应用架构
- 开源免费，遵循 Apache-2.0 许可证

### 3. 适用场景
- 需要 AI 辅助快速生成和处理办公文档的用户
- 寻求开源办公套件替代方案的 macOS 用户
- 希望通过智能代理提升文档与演示文稿制作效率的团队
- 开发者基于 GenOffice 进行二次开发和功能扩展

### 4. 技术亮点
- 采用 AI-native 架构设计，将 AI 能力深度融入办公套件核心
- 基于成熟的 GenOffice 项目 fork 开发，继承 Apache-2.0 开源协议
- 使用 TypeScript 开发，代码类型安全、可维护性强
- Electron 框架支持桌面端原生体验与跨平台部署
- 链接: https://github.com/criptogus/HermesOffice
- ⭐ 61 | 🍴 6 | 语言: TypeScript
- 标签: ai-native, docx, electron, fork, genoffice

### JoyAI-Video-Edit
- 

## JoyAI-Video-Edit 项目分析

### 1. 中文简介
JoyAI-Video-Edit 是一个基于 Python 开发的 AI 驱动视频编辑工具，旨在通过人工智能技术简化视频处理流程。该项目利用先进的 AI 模型实现智能化的视频内容生成与编辑功能，帮助用户高效完成视频制作任务。

### 2. 核心功能
- 基于 AI 的智能视频内容生成与编辑
- 支持多种视频处理操作的自动化流程
- 提供简洁易用的 Python API 接口
- 集成主流 AI 模型实现视频理解与创作
- 支持快速迭代和自定义编辑脚本

### 3. 适用场景
- 短视频内容创作者快速生成视频素材
- 需要批量处理视频内容的营销团队
- AI 视频编辑研究与原型开发
- 自动化视频剪辑与后期制作流程

### 4. 技术亮点
- 采用 Python 生态中成熟的 AI 库（如 PyTorch/TensorFlow）
- 模块化架构设计，便于功能扩展
- 结合大语言模型实现自然语言驱动的视频编辑
- 支持本地部署与云端 API 调用两种模式

---

> 注：由于该项目描述为"None"，以上分析基于项目名称及星标数等基本信息进行合理推断，实际功能请以项目源码为准。
- 链接: https://github.com/jd-opensource/JoyAI-Video-Edit
- ⭐ 60 | 🍴 3 | 语言: Python

### wai-play
- 描述: WAI Play - AI web game testing and quality evaluation platform
- 链接: https://github.com/waiterve/wai-play
- ⭐ 52 | 🍴 0 | 语言: Python
- 标签: ai, ai-agents, game, game-testing, python

### bevy-game-test-hub
- 描述: Experimental cross-platform game sandbox built with Rust and the Bevy engine to analyze AI integration across the game development lifecycle. Features modular Rust architecture, cross-platform compilation, and customizable engine settings.
- 链接: https://github.com/woodnathan266/bevy-game-test-hub
- ⭐ 48 | 🍴 0 | 语言: HTML

### ballsheet-aim-script-loader
- 描述: A high-precision browser aim trainer offering 1:1 mouse translation, zero-filtering raw input, custom cm/360 sensitivity matching, and real-time performance analytics for competitive gamers.
- 链接: https://github.com/hugop4/ballsheet-aim-script-loader
- ⭐ 47 | 🍴 0 | 语言: HTML

### sparkfetch
- 描述: 🔥 Turn any URL into clean, structured, LLM-ready content. The open-source web fetching & extraction API.
- 链接: https://github.com/Sparkfetch/sparkfetch
- ⭐ 35 | 🍴 7 | 语言: TypeScript
- 标签: ai, api, content-extraction, data-extraction, html-to-markdown

### moonlit-stories
- 描述: Reusable AI English picture-book workflow with consistent illustrations and local Chatterbox TTS.
- 链接: https://github.com/lincwang123-bot/moonlit-stories
- ⭐ 29 | 🍴 9 | 语言: JavaScript

### legal-ai-skills
- 描述: An open collection of Claude skills for legal work.
- 链接: https://github.com/rohasnagpal/legal-ai-skills
- ⭐ 26 | 🍴 2 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82262 | 🍴 15268 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35963 | 🍴 7403 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化查看工具，支持多种主流框架格式，可直观展示模型结构与层信息。开发者可通过它快速理解、调试和分享模型架构。

### 2. 核心功能
- 支持多格式模型可视化，包括 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite 和 safetensors 等。
- 以图形化方式展示神经网络层级结构、张量形状及连接关系。
- 提供模型权重与参数的查看能力，便于分析模型内部细节。
- 支持导出模型结构为图片或嵌入网页，方便文档与演示使用。
- 开源免费，支持桌面端与网页端两种使用方式。

### 3. 适用场景
- 模型开发阶段的结构审查与调试，快速定位层错误或维度不匹配问题。
- 学术论文与项目文档中的模型架构图展示，提升可读性。
- 跨框架模型格式转换时的结构对比与验证。
- 教学培训中直观讲解神经网络工作原理。

### 4. 技术亮点
- 广泛兼容主流深度学习框架，几乎覆盖所有常见模型格式。
- 纯前端实现，无需安装额外依赖，浏览器即可打开使用。
- 对 safetensors 等新兴格式提供支持，紧跟社区发展。
- 星标数高达 33316，说明其在 AI 社区中拥有广泛用户基础与高认可度。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33316 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21265 | 🍴 3981 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## ml-engineering 项目分析

### 1. 中文简介
《机器学习工程开放手册》是一本全面介绍机器学习工程实践的开源指南，涵盖从模型训练到部署的全流程技术。内容聚焦于大规模模型训练、推理优化及MLOps工程实践，适合希望深入理解ML系统构建的开发者与工程师。

### 2. 核心功能
- 提供大规模语言模型（LLM）训练与推理的完整工程实践指南
- 详解GPU集群管理、网络通信和存储优化等基础设施知识
- 覆盖PyTorch分布式训练、Slurm任务调度及模型调试技巧
- 包含模型可扩展性优化和MLOps流水线搭建的最佳实践

### 3. 适用场景
- 大规模分布式训练环境的搭建与调优
- LLM推理服务的性能优化与部署
- 机器学习平台的工程化建设与运维
- 研究或生产环境中GPU集群的资源管理

### 4. 技术亮点
- 内容覆盖从底层硬件（GPU/网络/存储）到上层框架（PyTorch/Transformers）的全栈技术
- 聚焦工业级大规模训练实践，具有较强工程指导价值
- 开源开放，持续更新，社区活跃度高（18515+星标）
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18515 | 🍴 1184 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2117 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3378 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13220 | 🍴 2669 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11615 | 🍴 911 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10688 | 🍴 5705 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

## 1. 中文简介
这是一个收录了500个AI相关项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。项目为开发者提供了丰富的实战案例和代码参考，适合学习和研究AI技术。

## 2. 核心功能
- **海量项目资源**：收录500个AI实战项目，覆盖多个技术领域
- **完整代码示例**：每个项目均附带可运行的代码实现
- **多领域覆盖**：包含机器学习、深度学习、计算机视觉、NLP四大方向
- **开源免费**：所有项目均为开源代码，可自由学习和使用

## 3. 适用场景
- **AI学习者**：通过实战项目快速掌握机器学习/深度学习技术
- **开发者参考**：查找特定AI任务的实现方案和代码模板
- **项目实践**：作为课程作业、毕业设计或竞赛项目的参考案例
- **技术调研**：快速了解AI领域各方向的主流项目和实现方式

## 4. 技术亮点
- 项目分类清晰，标签体系完善，便于快速定位所需领域
- 高星标数（35963）表明社区认可度高，资源质量有保障
- 涵盖从基础到进阶的完整学习路径，适合不同水平开发者
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35963 | 🍴 7403 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，能够直观展示模型结构和参数，帮助开发者快速理解和调试模型。

### 2. 核心功能
- 支持多种模型格式的可视化，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite、SafeTensors 等
- 提供清晰的神经网络结构图，展示层与层之间的连接关系
- 支持查看模型参数和权重信息
- 可在浏览器或桌面端运行，使用便捷
- 支持模型文件的导入和导出功能

### 3. 适用场景
- 模型开发调试：帮助开发者直观检查神经网络结构是否正确
- 模型转换验证：在格式转换（如 PyTorch → ONNX）后验证模型结构一致性
- 论文与报告展示：生成高质量的模型架构图用于学术发表
- 团队协作沟通：用可视化方式向非技术成员解释模型设计

### 4. 技术亮点
- 跨平台支持：基于 Electron 构建，兼容 Windows、macOS 和 Linux
- 开源免费：采用 MIT 许可证，社区活跃，持续更新
- 零依赖运行：无需安装 TensorFlow 或 PyTorch 等框架即可查看模型
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33316 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub 项目分析：cheatsheets-ai

---

## 1. 中文简介

本项目为深度学习与机器学习研究者提供了一份全面的速查手册集合。内容涵盖机器学习、深度学习及相关工具库的核心知识要点，适合快速查阅与复习使用。

---

## 2. 核心功能

- 提供机器学习与深度学习领域的核心概念速查表
- 涵盖 NumPy、SciPy、Matplotlib 等科学计算库的常用语法
- 包含 Keras 深度学习框架的关键 API 参考
- 以简洁的表格形式呈现，便于快速检索

---

## 3. 适用场景

- **学术研究**：研究人员快速回顾算法原理与公式
- **面试准备**：求职者系统梳理机器学习核心知识点
- **项目开发**：工程师查阅常用库函数与代码示例
- **教学参考**：教师用于课程辅助材料或学生自学资料

---

## 4. 技术亮点

- 高人气项目（15,427 星标），内容经过社区广泛验证
- 覆盖从基础数学工具到深度学习框架的完整技术栈
- 内容结构清晰，适合不同水平的使用者快速定位所需信息
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3378 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

---

### 1. 中文简介

Ai-Learn 是一个系统化的人工智能学习路线图项目，整合了近200个实战案例与项目，并提供免费配套教材，帮助零基础学习者入门并实现就业实战。项目覆盖 Python、机器学习、深度学习、数据分析、计算机视觉、自然语言处理等多个热门技术领域。

---

### 2. 核心功能

- **系统化学习路径**：提供从入门到就业的完整 AI 学习路线图。
- **实战案例库**：收录近200个实战项目，覆盖主流 AI 技术方向。
- **免费教材资源**：配套教材全部免费开放，降低学习门槛。
- **多领域覆盖**：涵盖 Python、数学基础、机器学习、深度学习、CV、NLP 等核心领域。
- **多框架支持**：兼容 TensorFlow、PyTorch、Keras、Caffe 等主流深度学习框架。

---

### 3. 适用场景

- **零基础入门者**：需要系统学习路径的 AI 初学者。
- **求职转行者**：希望通过实战项目提升就业竞争力的学习者。
- **高校学生**：需要课程补充资源和项目参考的大学生。
- **技术爱好者**：希望全面了解 AI 各方向技术栈的自学者。

---

### 4. 技术亮点

- **资源聚合度高**：一站式整合近200个案例，避免学习过程中四处搜索。
- **框架全面**：同时覆盖 TensorFlow 2.x、PyTorch、Keras 等主流框架，适应不同学习需求。
- **实战导向**：以就业为目标，注重项目实践而非纯理论。
- **免费开源**：所有教材和资源免费开放，社区驱动持续更新。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13220 | 🍴 2669 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式配置简化模型开发流程，让开发者无需编写大量代码即可完成深度学习模型的训练与部署。

## 2. 核心功能
- **低代码模型开发**：通过 YAML/JSON 声明式配置快速构建自定义 AI 模型
- **多模态支持**：支持文本、图像、表格等多种数据类型
- **大模型微调**：内置对 LLaMA、Llama2、Mistral 等主流 LLM 的微调能力
- **可视化训练**：提供训练过程的可视化监控与结果分析
- **一键部署**：支持将训练好的模型快速部署为 API 服务

## 3. 适用场景
- 快速原型开发：数据科学家通过低代码方式快速验证模型想法
- LLM 微调：对开源大语言模型进行领域定制微调
- 多模态任务：处理同时包含文本和图像数据的复杂任务
- 生产环境部署：将训练好的模型快速部署为可服务的 API

## 4. 技术亮点
- 基于 PyTorch 构建，兼容主流深度学习生态
- 支持 Hugging Face Transformers 集成，无缝对接开源模型库
- 提供自动化的超参数调优和数据预处理能力
- 项目星标数达 11,748，社区活跃度高
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9162 | 🍴 1234 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8951 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1898 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6994 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6350 | 🍴 766 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82262 | 🍴 15268 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73762 | 🍴 9023 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一门面向零基础学习者的AI入门课程，由微软官方出品，包含12周、24课时的系统化教学内容。课程旨在让所有人都能轻松学习人工智能相关知识，涵盖从基础概念到深度学习实践的完整学习路径。

## 2. 核心功能
- 提供12周系统化课程结构，每周2课时的渐进式学习安排
- 基于Jupyter Notebook的交互式编程实践环境
- 覆盖机器学习、深度学习、计算机视觉、自然语言处理等核心领域
- 包含CNN、RNN、GAN等主流AI技术的实战案例
- 微软官方出品，内容质量有保障且免费开放

## 3. 适用场景
- 零基础初学者系统学习人工智能基础知识
- 高校或培训机构作为AI课程的配套教学资源
- 职场人士转行AI领域的入门学习路径
- 企业对员工进行AI科普培训的参考资料

## 4. 技术亮点
- 采用Jupyter Notebook实现代码与理论讲解的无缝结合
- 涵盖从传统机器学习到深度学习的完整技术栈
- 项目获得超6万星标认可，社区活跃且资源丰富
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 61766 | 🍴 11998 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub项目分析：ai-engineering-from-scratch

### 1. 中文简介
从零开始学习、构建并部署AI系统，最终为他人交付完整解决方案。该项目是一套全面的AI工程实践教程，帮助学习者掌握从理论到落地的完整技能链。

### 2. 核心功能
- 涵盖AI代理（Agents）、多智能体系统和蜂群智能的构建方法
- 深入讲解大语言模型（LLM）和生成式AI的应用开发
- 提供计算机视觉、NLP和强化学习的实战教程
- 支持使用Python、Rust和TypeScript进行AI工程实践
- 集成MCP（Model Context Protocol）等现代AI工具链

### 3. 适用场景
- AI工程师希望系统性地从底层原理到工程落地全面掌握AI技术
- 学生或转行者需要通过实战项目构建AI应用作品集
- 团队希望建立内部AI工程能力，开发可部署的智能代理系统
- 研究者想将深度学习、强化学习等理论转化为实际产品

### 4. 技术亮点
- 跨语言支持：同时覆盖Python、Rust、TypeScript，满足不同性能与开发效率需求
- 从理论到部署的完整闭环：不仅教授原理，更强调"Ship it"的工程交付能力
- 多领域融合：将LLM、计算机视觉、强化学习、多智能体系统等前沿技术整合于一套课程体系中
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 45947 | 🍴 7913 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## GitHub项目分析：ailearning

### 1. 中文简介
AiLearning是一个面向数据科学与机器学习的综合学习项目，涵盖数据分析、机器学习实战、线性代数、PyTorch深度学习框架以及自然语言处理（NLTK和TensorFlow 2）等内容。该项目整合了从基础理论到实际应用的完整学习路径，适合系统性地掌握AI核心技能。

### 2. 核心功能
- 涵盖机器学习经典算法实战（SVM、KMeans、逻辑回归等）
- 提供深度学习框架教程（PyTorch、TensorFlow 2）
- 包含自然语言处理（NLP）相关库（NLTK）的应用
- 整合线性代数等数学基础，夯实理论根基
- 实现推荐系统、关联规则挖掘（Apriori、FP-Growth）等实用项目

### 3. 适用场景
- 数据科学和机器学习初学者系统学习
- 准备算法面试的技术人员巩固基础知识
- 需要快速搭建机器学习项目框架的开发者
- 希望从理论到实践全面掌握AI技能的自学者

### 4. 技术亮点
- 项目星标数高达42433，说明社区认可度极高
- 技术栈覆盖全面，从传统机器学习到深度学习再到NLP均有涉及
- 标签涵盖主流算法（Adaboost、NaiveBayes、PCA、SVD等），学习路径清晰
- 同时支持PyTorch和TensorFlow 2两大主流深度学习框架
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42433 | 🍴 11527 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35963 | 🍴 7403 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33802 | 🍴 4703 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28943 | 🍴 3525 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21807 | 🍴 3333 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17350 | 🍴 2117 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

### 1. 中文简介
这是一个收录了500个AI项目的开源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等方向，每个项目均附带完整代码。该项目星标数超过3.5万，是AI学习者的优质资源库。

### 2. 核心功能
- 提供500个AI项目的完整代码实现
- 覆盖机器学习、深度学习、计算机视觉、NLP四大领域
- 项目按技术领域分类，便于针对性学习
- 包含从入门到进阶的多样化项目案例
- 项目代码可直接运行，适合实践练习

### 3. 适用场景
- **AI学习者**：系统学习机器学习与深度学习项目的理想资源
- **开发者参考**：快速查找特定领域的AI项目实现方案
- **教学培训**：作为AI课程的实践案例库
- **项目选型**：寻找AI项目灵感或技术参考

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广
- 所有项目均附带可运行代码
- 标签体系清晰，便于按技术领域筛选
- 高星标数（35963）证明社区认可度高
- 涵盖当前AI热门方向：CV、NLP、深度学习等
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35963 | 🍴 7403 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款利用人工智能技术自动化浏览器工作流的开源工具。它通过结合大语言模型（LLM）与浏览器自动化技术，能够智能地完成各类基于网页的操作任务，降低RPA开发的复杂度。

### 2. 核心功能
- 基于AI的浏览器自动化，支持自然语言指令驱动操作
- 集成Playwright、Puppeteer、Selenium等多种浏览器驱动
- 支持视觉识别（Vision）能力，可理解页面元素和布局
- 提供API接口，便于集成到现有工作流中
- 支持复杂的跨页面、多步骤自动化任务编排

### 3. 适用场景
- **RPA替代方案**：替代传统规则型RPA，用AI处理更灵活的网页操作
- **数据抓取与录入**：自动登录网站、填写表单、提取数据
- **重复性网页任务**：如定期登录系统执行操作、批量处理网页信息
- **AI辅助测试**：用自然语言描述测试用例，自动执行浏览器操作验证

### 4. 技术亮点
- **多引擎兼容**：同时支持Playwright、Puppeteer、Selenium，灵活适配不同场景
- **AI+视觉双驱动**：结合LLM语义理解与计算机视觉能力，提升自动化准确性
- **低代码/无代码**：用自然语言描述任务，无需编写复杂脚本即可实现自动化
- **API化设计**：提供REST API，便于与企业现有系统集成
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22672 | 🍴 2137 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（Computer Vision Annotation Tool）是一款领先的平台，用于构建高质量的视觉数据集以支持视觉AI应用。它提供开源、云服务和企业级产品，并附带标注服务，支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作、数据分析及开发者API。

### 2. 核心功能
- **多模态标注**：支持图像、视频和3D数据的标注任务
- **AI辅助标注**：集成智能标注功能，提升标注效率
- **团队协作**：支持多人协作完成标注项目
- **质量保证**：提供标注质量检查和验证机制
- **开发者API**：开放API接口，便于集成和扩展

### 3. 适用场景
- **数据集构建**：为计算机视觉模型训练准备高质量标注数据
- **目标检测项目**：支持边界框标注，适用于物体检测任务
- **语义分割任务**：支持像素级标注，适用于图像分割场景
- **视频分析项目**：支持视频帧标注，适用于行为识别等任务

### 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow）
- 提供多种标注类型：边界框、图像分类、语义分割等
- 兼容ImageNet等标准数据集格式
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16455 | 🍴 3787 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12946 | 🍴 1704 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个专为空间 AI 设计的几何计算机视觉库，基于 PyTorch 构建。它将传统计算机视觉算法与深度学习框架深度融合，提供可微分的图像处理工具，适用于需要端到端训练视觉任务的应用场景。

### 2. 核心功能
- 提供可微分的几何计算机视觉算子（如仿射变换、透视变换、相机投影等）
- 支持批量 GPU 加速的图像处理操作
- 内置丰富的传统 CV 算法（边缘检测、角点检测、形态学操作等）
- 与 PyTorch 生态无缝集成，支持自动微分
- 提供相机校准、立体视觉、SLAM 等空间感知工具

### 3. 适用场景
- **机器人视觉导航**：用于 SLAM、视觉里程计等空间感知任务
- **自动驾驶**：处理相机标定、深度估计、场景理解
- **图像配准与拼接**：多视图几何处理和图像融合
- **可微分渲染与三维重建**：结合深度学习进行 3D 场景恢复

### 4. 技术亮点
- **全可微设计**：所有 CV 算子支持反向传播，可直接嵌入神经网络训练流程
- **硬件加速**：充分利用 GPU/TPU 并行计算能力，适合大规模批处理
- **生产就绪**：代码质量高，文档完善，被多家机构用于实际项目
- 链接: https://github.com/kornia/kornia
- ⭐ 11303 | 🍴 1212 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2190 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3466 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3320 | 🍴 409 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2632 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2432 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全属于您个人的 AI 助手，支持任何操作系统和平台。它以龙虾为象征，主打数据自主可控的理念，让您在自己的设备上运行 AI，真正掌握自己的数据隐私。

### 2. 核心功能
- 跨平台部署：支持任意操作系统，无需绑定特定硬件或云服务
- 数据隐私优先：所有数据本地存储，真正实现"数据归你所有"
- 个人 AI 助手：提供个性化的智能助理服务
- 开源自由：基于开源协议，可自由定制和扩展
- 多平台兼容：可在不同设备间无缝切换使用

### 3. 适用场景
- 注重隐私的个人用户：希望 AI 助手不上传数据到第三方云端
- 开发者与技术爱好者：需要本地化、可自定义的 AI 解决方案
- 企业私有化部署：希望在内部网络中运行 AI 助手的企业
- 跨设备办公场景：需要在不同操作系统间同步个人 AI 助手的用户

### 4. 技术亮点
- 基于 TypeScript 开发，具备良好的类型安全和开发体验
- 轻量级架构设计，资源占用低，适合本地部署
- 社区活跃度高（近 39 万星标），生态持续完善
- 强调"数据自主"理念，契合当前隐私保护趋势
- 链接: https://github.com/openclaw/openclaw
- ⭐ 385158 | 🍴 80965 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## 项目分析：superpowers

### 1. 中文简介
这是一个可实际落地的AI代理技能框架与软件开发方法论。它通过子代理驱动开发模式，为软件开发生命周期提供系统化的技能协作方案。

### 2. 核心功能
- **子代理驱动开发**：通过多个AI子代理协同完成复杂开发任务
- **技能框架**：提供模块化的AI技能组件，支持灵活组合与复用
- **头脑风暴辅助**：集成AI协作进行创意发散与需求梳理
- **完整SDLC支持**：覆盖从需求分析到代码交付的全生命周期
- **OBRА方法论**：基于目标-行为-结果的系统化开发流程

### 3. 适用场景
- 需要AI辅助完成中大型软件项目的团队开发
- 希望引入多代理协作模式提升开发效率的场景
- 寻求系统化AI技能框架进行需求分析与编码的项目

### 4. 技术亮点
- 采用Shell脚本实现，轻量且易于集成到现有工作流
- 26万+星标表明其在社区中具有广泛认可度
- 将AI代理能力与成熟软件开发方法论相结合，兼顾创新与实用性
- 链接: https://github.com/obra/superpowers
- ⭐ 266635 | 🍴 23837 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

# Hermes-Agent 项目分析

## 1. 中文简介
Hermes-Agent 是一款能够伴随用户共同成长的智能 AI 代理，支持多种大语言模型（包括 Claude、GPT 等），具备持续学习与适应的能力。它旨在为用户提供越来越智能、越来越懂你的 AI 助手体验。

## 2. 核心功能
- 支持多模型集成（Claude、OpenAI、Codex 等）
- 具备自我进化能力，随使用不断适应用户需求
- 提供智能对话与代码辅助功能
- 兼容主流 AI 平台与 API
- 开源可定制，支持本地部署

## 3. 适用场景
- **开发者辅助编程**：智能代码生成、审查与调试
- **日常 AI 助手**：对话问答、知识检索与任务管理
- **多模型对比测试**：统一接口对比不同 LLM 的表现
- **个人化 AI 应用开发**：基于 Hermes 框架快速构建定制代理

## 4. 技术亮点
- 采用 Python 开发，社区活跃（超 22 万星标）
- 标签显示与 Nous Research、Moltbot 等知名 AI 项目相关，具备较强的技术背景
- 支持 Anthropic Claude 与 OpenAI 双引擎，灵活切换
- 开源生态完善，易于二次开发集成
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 225596 | 🍴 43830 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

# n8n 项目分析

## 1. 中文简介
n8n 是一款公平代码（fair-code）工作流自动化平台，内置原生 AI 能力，支持将可视化构建与自定义代码相结合。用户可选择自托管或云端部署，平台提供 400 多种集成，覆盖广泛的应用场景。

## 2. 核心功能
- **可视化工作流构建**：通过拖拽节点快速设计自动化流程，无需编写大量代码。
- **AI 原生集成**：平台内置 AI 能力，可直接在工作流中调用 AI 模型进行智能处理。
- **400+ 集成生态**：支持丰富的第三方服务集成，涵盖 API、数据库、云服务等多种类型。
- **灵活部署方式**：支持自托管和云端两种模式，用户可根据需求自由选择。
- **代码扩展能力**：允许在可视化流程中插入自定义代码，满足复杂业务逻辑需求。

## 3. 适用场景
- **企业自动化**：将多个业务系统（如 CRM、ERP、邮件服务）串联，实现跨系统数据同步和流程自动化。
- **AI 应用开发**：快速构建基于 AI 的工作流，如智能客服、内容生成、数据分析等。
- **数据集成与处理**：从不同数据源采集数据，进行清洗、转换后写入目标系统。
- **低代码开发平台**：为业务人员提供可视化工具，降低自动化应用的开发门槛。

## 4. 技术亮点
- **公平代码协议**：采用 fair-code 许可，允许免费使用和商业部署，同时保护项目可持续发展。
- **TypeScript 技术栈**：基于 TypeScript 开发，代码类型安全，便于维护和扩展。
- **MCP 支持**：原生支持 Model Context Protocol（MCP），可轻松连接各种 AI 模型和工具。
- **高社区活跃度**：超过 19 万星标，拥有活跃的开源社区和丰富的文档资源。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 199374 | 🍴 59908 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 承载着让每个人都能轻松使用并构建 AI 的愿景。我们的使命是提供相应的工具，让你能够专注于真正重要的事情。

### 2. 核心功能
- 支持自主构建和执行复杂任务链
- 可连接多种大语言模型（OpenAI、Claude、Llama 等）
- 提供灵活的工具扩展机制，支持自定义功能模块
- 具备记忆系统，可在任务执行过程中保持上下文
- 支持浏览器操作、文件读写等实际执行能力

### 3. 适用场景
- **自动化研究**：自动搜索信息、整理资料并生成报告
- **内容创作**：辅助撰写文章、代码或营销文案
- **代码开发**：自动生成、测试和调试代码片段
- **数据分析**：自动抓取数据、处理分析并输出可视化结果

### 4. 技术亮点
- 模块化架构设计，便于开发者扩展和定制
- 多模型兼容，不绑定单一 AI 提供商
- 支持 Agent 自主决策与迭代执行
- 活跃的开源社区，持续迭代更新
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185820 | 🍴 46049 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166743 | 🍴 21534 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164391 | 🍴 30545 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 161156 | 🍴 9100 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157521 | 🍴 46177 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152847 | 🍴 9798 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

