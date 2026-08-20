# GitHub AI项目每日发现报告
日期: 2026-08-20

## 新发布的AI项目

### watermarks-remover
- 

# GitHub项目分析：watermarks-remover

## 1. 中文简介
该项目用于移除多种AI生成内容的来源追踪痕迹。它支持对PNG、JPEG、SVG、PDF、DOCX、HTML和MD文件进行Unicode文本清理、统计重写以及C2PA/元数据剥离操作。

## 2. 核心功能
- 支持移除Claude、Codex、Grok等主流AI工具嵌入的来源追踪标记
- 对文件中的不可见Unicode字符进行清理和过滤
- 使用统计重写技术改变文本特征以消除AI指纹
- 剥离C2PA（内容来源与真实性联盟）标准和各类元数据
- 兼容多种文件格式，包括图片、文档和文本文件

## 3. 适用场景
- 内容创作者需要移除AI生成内容中的平台水印以用于商业用途
- 研究人员分析不同AI工具的水印检测与防护机制
- 媒体工作者处理含有来源追踪标记的素材文件
- 隐私保护场景下清除文件中可能泄露AI使用历史的元数据

## 4. 技术亮点
- 同时支持图片格式（PNG/JPEG/SVG）和文档格式（PDF/DOCX/HTML/MD）的水印移除
- 采用Unicode文本清洗与统计重写相结合的多层处理策略
- 兼容C2PA标准，可处理新兴的AI内容溯源技术
- 与多个主流AI工具（Claude、Codex、Grok）的标签关联，说明其针对性较强
- 链接: https://github.com/Leutenegger/watermarks-remover
- ⭐ 919 | 🍴 95 | 语言: Python
- 标签: claude, claude-code, claude-skills, codex, codex-cli

### llm-rag-memory-ai-agents
- 

## 项目分析：llm-rag-memory-ai-agents

### 1. 中文简介
该项目描述信息缺失，无法提供准确翻译。根据项目名称推测，这是一个结合大语言模型（LLM）、RAG（检索增强生成）和记忆机制的AI代理框架。

### 2. 核心功能
- 集成LLM与RAG技术实现知识增强
- 提供AI代理的记忆管理机制
- 支持Python环境快速部署
- 构建智能对话或任务执行系统

### 3. 适用场景
- 智能客服与对话系统开发
- 企业知识库问答机器人
- 需要长期记忆的个人助理应用
- RAG增强型AI代理研究

### 4. 技术亮点
暂无详细信息。建议访问项目仓库查看README文件获取完整功能说明和技术架构。

---

> **注**：该项目描述字段为空，以上分析基于项目名称推断。如需准确信息，请提供完整项目描述或仓库链接。
- 链接: https://github.com/turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents
- ⭐ 92 | 🍴 0 | 语言: Python

### dsh-oil-creator
- 

## dsh-oil-creator 项目分析

### 1. 中文简介
这是一个为 DeepSeek Harness 设计的 AI 辅助本地创作者工作台，通过 DSH 插件系统帮助创作者更高效地进行内容创作。项目采用 TypeScript 开发，专注于提供智能化的创作工具链。

### 2. 核心功能
- AI 辅助创作：集成 DeepSeek 大模型能力，提供智能内容生成
- 本地工作流：支持离线/本地化创作流程，保护创作者数据隐私
- DSH 插件系统：通过插件机制扩展功能，灵活适配不同创作需求
- 创作者工作台：一站式创作环境，整合多种创作工具
- TypeScript 架构：类型安全，便于维护和扩展

### 3. 适用场景
- 使用 DeepSeek Harness 的创作者团队进行协作内容生产
- 需要本地化部署的 AI 辅助创作工具（数据安全要求高）
- 希望基于 DSH 插件系统定制个性化创作工作流
- 追求 TypeScript 技术栈的现代化创作平台

### 4. 技术亮点
- 采用 TypeScript 开发，具备完善的类型系统和开发体验
- 基于 DeepSeek Harness 生态，可充分利用其 AI 能力
- 插件化架构设计，支持功能模块的热插拔和灵活组合
- 87 星标表明项目在创作者社区中有一定关注度

---

**总结**：这是一个面向 DeepSeek 生态的 AI 创作工具，适合需要本地化部署、重视数据隐私的创作者团队使用。
- 链接: https://github.com/oil-oil/dsh-oil-creator
- ⭐ 87 | 🍴 18 | 语言: TypeScript
- 标签: creator, deepseek-harness, dsh-plugin

### github-farm
- 

## GitHub项目分析：github-farm

### 1. 中文简介
这是一个面向AI网关的生产级多平台OAuth认证收集与会话管理框架，专为AI代理友好设计。它帮助AI系统统一管理多个平台的身份验证和会话状态。

### 2. 核心功能
- 支持多平台OAuth认证流程的自动化收集与管理
- 提供会话状态管理机制，确保AI代理可持续访问
- 专为AI网关场景优化，支持大规模并发认证请求
- 生产级稳定性设计，适用于企业级部署环境

### 3. 适用场景
- AI助手需要访问多个第三方平台（如社交媒体、云服务）的API
- 多租户AI网关需要统一管理用户授权会话
- 需要批量处理OAuth认证的企业级应用
- AI代理需要持久化会话状态以执行跨平台任务

### 4. 技术亮点
- 采用Python编写，生态兼容性好，易于集成
- 针对AI Agent场景进行专门优化，降低开发复杂度
- 支持生产级部署，具备高可用性和可扩展性
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 83 | 🍴 6 | 语言: Python

### OpenCMO
- 

# OpenCMO 项目分析

## 1. 中文简介
OpenCMO 是一个开源的"首席营销官"AI技能，整合了来自 Cursor、Notion、Linear、Deel、Gamma、Granola 等16家知名公司的增长策略手册。该项目以可安装的 AI 技能形式提供，让开发者能够便捷地获取和应用这些经过验证的增长营销方法论。

## 2. 核心功能
- 汇集16家头部公司的增长营销实战策略
- 以可安装的 AI 技能形式集成，便于直接使用
- 支持 Claude Code 等 AI 编程工具调用
- 提供 GTM（Go-To-Market）和增长营销知识储备
- 构建开源营销知识库，降低增长策略学习门槛

## 3. 适用场景
- 初创公司制定增长营销策略时参考实战案例
- 营销人员学习头部产品的 GTM 方法论
- 开发者在 AI 编程工具中快速调用增长策略建议
- 团队内部建立统一的增长营销知识体系

## 4. 技术亮点
- 采用 AI Skill 安装机制，与 Claude Code 等工具无缝集成
- 将非结构化的增长经验转化为可检索、可调用的知识资产
- 开源模式便于社区持续贡献和优化策略内容
- 链接: https://github.com/About-Intelligence/OpenCMO
- ⭐ 31 | 🍴 0 | 语言: 未知
- 标签: ai-agents, claude-code, growth-marketing, gtm, knowledge-base

### drop-code
- 描述: A warm, drop-down AI coding terminal for macOS.
- 链接: https://github.com/R44VC0RP/drop-code
- ⭐ 30 | 🍴 4 | 语言: Swift

### awesome-grok-bot
- 描述: Curated bilingual list of Grok Bot resources — always-on AI teammates with their own cloud computer.
- 链接: https://github.com/RongleCat/awesome-grok-bot
- ⭐ 27 | 🍴 1 | 语言: Python
- 标签: awesome, awesome-list, cursor, grok-bot, xai

### scibly
- 描述: Scibly is an open-source, AI-native learning platform. Turn your existing knowledge into interactive learning experiences.
- 链接: https://github.com/scibly-dev/scibly
- ⭐ 26 | 🍴 1 | 语言: TypeScript
- 标签: ai-agents, corporate-learning, duolingo, education, learning

### lanshu-create-ai-presenter-video
- 描述: Provider-neutral Codex Skill for producing verified AI presenter videos from a script and an authorized presenter image.
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 24 | 🍴 3 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### feishu-ppt-skill
- 描述: AI-agent skill for building Lark (Feishu) slides via the lark-cli: 51-page template library, brand design tokens, XML generation workflow, and automated layout review. Built for agents, reusable anywhere.
- 链接: https://github.com/YinsenW/feishu-ppt-skill
- ⭐ 23 | 🍴 3 | 语言: Python
- 标签: ai-agent, cli, feishu, lark, ppt

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82567 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

# GitHub项目分析：500 AI/ML/DL/CV/NLP Projects

## 1. 中文简介
这是一个收录了500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。每个项目均附带完整代码实现，适合从入门到进阶的学习者参考实践。

## 2. 核心功能
- 汇集500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供可运行的源代码，便于直接学习和复现
- 按技术领域分类整理，结构清晰，方便快速定位感兴趣的方向
- 适合不同水平学习者，从基础入门到进阶实战均有覆盖

## 3. 适用场景
- 机器学习/深度学习初学者系统学习与实践
- 计算机视觉或NLP方向的研究者寻找参考实现
- 技术面试准备，积累项目经验
- 团队内部技术分享与知识沉淀

## 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，是目前较全面的AI项目合集之一
- 所有项目均附带完整代码，可直接运行学习
- 星标数高达36411，说明社区认可度高，项目质量有保障
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36411 | 🍴 7445 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款用于神经网络、深度学习及机器学习模型的可视化工具。它支持多种主流框架的模型格式，帮助用户直观地查看和理解模型结构。该工具轻量高效，无需安装复杂的运行环境即可运行。

### 2. 核心功能
- 支持多种模型格式（ONNX、TensorFlow、PyTorch、CoreML、Keras、TensorFlow Lite、SafeTensors等）
- 可视化神经网络层结构及数据流向
- 提供交互式图表，支持缩放、搜索和详情查看
- 可在浏览器或桌面端直接打开模型文件
- 支持模型权重和参数的查看与对比

### 3. 适用场景
- 深度学习模型调试与结构审查
- 教学演示中直观展示神经网络架构
- 跨框架模型格式转换前的结构验证
- 模型部署前的可视化检查

### 4. 技术亮点
- 纯前端实现，无需后端服务，开箱即用
- 支持离线运行，保护模型数据安全
- 轻量级架构，兼容桌面和网页两种运行模式
- 广泛兼容主流AI框架，社区活跃度高（33370+星标）
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33370 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习模型的开放交换标准，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同框架（如PyTorch、TensorFlow、Keras等）之间无缝迁移模型，打破框架壁垒，提升开发效率。

### 2. 核心功能
- **跨框架模型转换**：支持在PyTorch、TensorFlow、Keras等主流框架之间进行模型格式转换
- **统一模型表示**：提供标准化的模型定义格式，确保模型在不同平台和设备上的一致性
- **推理优化**：集成ONNX Runtime，提供跨平台的推理加速能力
- **生态工具链**：提供模型转换、验证、可视化和性能分析等配套工具
- **部署灵活性**：支持将模型部署到多种硬件环境，包括CPU、GPU和移动端设备

### 3. 适用场景
- **模型迁移与复用**：将已训练的模型从研究框架（如PyTorch）迁移到生产环境（如TensorFlow Serving）
- **跨平台部署**：在Web、移动端、嵌入式设备等多种平台上运行同一模型
- **推理性能优化**：利用ONNX Runtime对模型进行算子融合、量化等优化以提升推理速度
- **框架无关的模型共享**：在团队或组织内部共享模型，不受特定框架限制

### 4. 技术亮点
- 由Microsoft、Facebook（Meta）等科技巨头联合发起，社区活跃度高，生态完善
- 支持动态形状（Dynamic Shapes），适应不同输入尺寸的推理需求
- 与主流硬件厂商（NVIDIA、Intel、ARM等）深度集成，提供硬件级优化支持
- 链接: https://github.com/onnx/onnx
- ⭐ 21337 | 🍴 4004 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## 项目分析：ml-engineering

### 1. 中文简介
《机器学习工程开放百科》——一本全面覆盖机器学习工程实践的知识库，涵盖从模型训练、调试、推理到大规模分布式部署的完整技术栈。

### 2. 核心功能
- 提供 PyTorch 模型训练与调试的最佳实践指南
- 详解 GPU 集群管理与 Slurm 调度系统的配置方法
- 覆盖大语言模型（LLM）的推理优化与可扩展性设计
- 包含网络、存储等基础设施层面的工程化解决方案

### 3. 适用场景
- 大规模分布式训练环境的搭建与调优
- LLM 推理服务的高性能部署与优化
- MLOps 流水线中模型训练到上线的全流程管理
- GPU 资源密集型任务的集群调度与监控

### 4. 技术亮点
- 聚焦 PyTorch + Transformers 生态的工程实践，内容紧跟前沿
- 覆盖从单卡调试到千卡集群扩展的完整链路
- 结合 Slurm 等工业级调度工具，具备较强的落地指导价值
- 开源开放，适合作为机器学习工程师的实战参考手册
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18666 | 🍴 1202 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17379 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13271 | 🍴 2673 | 语言: 未知
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
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域，每个项目均配有完整代码实现。该项目以"awesome list"形式整理，是AI学习者、研究者和开发者的实用参考指南。

---

### 2. 核心功能
- 收录500个AI项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域。
- 每个项目均提供可运行的代码，便于学习者直接实践与复现。
- 按领域分类整理，支持通过标签快速检索所需项目。
- 作为持续更新的资源库，跟踪AI领域最新项目动态。
- 提供从入门到进阶的完整学习路径参考。

---

### 3. 适用场景
- **AI初学者系统学习**：作为入门学习路线，按领域逐步掌握机器学习与深度学习核心知识。
- **开发者寻找参考项目**：在特定领域（如图像分类、文本生成）快速找到可复用的代码实现。
- **技术人员跟踪前沿动态**：了解AI领域最新开源项目和技术趋势。
- **教育者备课资源**：作为课程实践案例库，辅助教学与实验设计。

---

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流细分方向，资源全面。
- 每个项目均附带代码，强调实践导向，便于边学边用。
- 标签体系完善（如 `computer-vision`、`nlp-projects` 等），检索效率高。
- 高星标数（36,411）印证了社区高度认可与广泛使用。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36411 | 🍴 7445 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33370 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

# Ai-Learn 项目分析

## 1. 中文简介
Ai-Learn 是一个人工智能学习路线图项目，整理了近200个实战案例与项目，并提供免费配套教材，帮助零基础学习者入门并实现就业实战。涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等多个热门技术领域。

## 2. 核心功能
- 提供系统化的AI学习路线指引，适合从零开始的学习者。
- 收录近200个实战案例与项目，覆盖主流AI技术栈。
- 免费提供配套教材与学习资源，降低学习门槛。
- 涵盖Python、机器学习、深度学习、NLP、CV等热门方向。
- 注重就业导向，帮助学习者掌握实际应用能力。

## 3. 适用场景
- 人工智能初学者系统学习路线规划。
- 希望转行AI领域的开发者补充实战经验。
- 高校学生或自学者寻找免费学习资源与项目练习。
- 企业培训中用于AI技术栈的快速入门与技能提升。

## 4. 技术亮点
- 项目星标数达13271，说明在开发者社区中具有较高的认可度和影响力。
- 标签覆盖主流框架与工具，包括PyTorch、TensorFlow、Keras、Caffe等深度学习框架，以及NumPy、Pandas、Matplotlib、Seaborn等数据分析库。
- 内容全面，从数学基础到NLP、CV等高级应用均有涉及，形成完整的学习闭环。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13271 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大语言模型（LLM）、神经网络及其他 AI 模型。它旨在降低深度学习模型的构建门槛，让开发者能够以更低的技术成本快速实现模型训练与微调。

### 2. 核心功能
- **低代码模型构建**：通过声明式配置快速搭建深度学习模型，无需编写大量代码
- **多模态支持**：支持自然语言处理（NLP）、计算机视觉等多种数据类型
- **LLM 微调与训练**：提供对 LLaMA、Mistral 等大语言模型的微调能力
- **数据为中心的设计**：强调数据驱动的开发流程，简化数据处理与实验管理
- **PyTorch 后端**：基于 PyTorch 构建，兼容主流深度学习生态

### 3. 适用场景
- 快速原型开发：希望以最少代码验证 AI 模型想法的开发者
- 大语言模型微调：需要对 LLaMA、Mistral 等开源模型进行领域适配的团队
- 多模态应用：同时处理文本和图像数据的 AI 项目
- 数据科学工作流：注重数据质量与迭代效率的数据中心型项目

### 4. 技术亮点
- 声明式 YAML 配置，模型定义简洁直观
- 内置 AutoML 功能，可自动搜索最优超参数
- 支持分布式训练，适配大规模数据场景
- 与 Hugging Face 生态深度集成，方便加载预训练模型
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11747 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9177 | 🍴 1232 | 语言: Python
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
- ⭐ 82567 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100+ 种模型的训练。该项目成果发表于 ACL 2024，旨在提供一站式模型微调解决方案。

## 2. 核心功能
- 支持 100+ 种 LLM 和 VLM 的统一微调，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型
- 提供 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法
- 支持 RLHF（基于人类反馈的强化学习）全链路训练
- 内置 4bit/8bit 量化技术，降低显存占用
- 支持 MoE（混合专家）架构模型训练

## 3. 适用场景
- 研究人员需要快速对多种大模型进行指令微调实验
- 开发者希望在有限显存条件下微调大规模语言模型
- 团队需要构建基于 RLHF 的对话优化系统
- 需要训练支持多模态理解（图像+文本）的 VLM 模型

## 4. 技术亮点
- **统一框架**：一套代码适配上百种模型，无需针对每个模型单独配置
- **QLoRA 优化**：通过 4bit 量化将显存需求大幅降低，消费级显卡即可微调大模型
- **ACL 2024 学术背书**：经过同行评审，方法论具有学术严谨性
- **生态兼容**：基于 HuggingFace Transformers 构建，与现有生态无缝衔接
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74253 | 🍴 9080 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# AI-For-Beginners 项目分析

## 1. 中文简介
这是一个为期12周、包含24节课程的AI入门教程，旨在让所有人都能学习人工智能。课程内容由微软开发，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域，适合零基础学习者系统掌握AI基础知识。

## 2. 核心功能
- 提供完整的12周AI学习路径，每周一课循序渐进
- 使用Jupyter Notebook编写，支持交互式代码学习
- 涵盖机器学习、深度学习、CNN、RNN、GAN、NLP等核心主题
- 由微软官方出品，内容质量有保障
- 完全免费开源，适合全球学习者使用

## 3. 适用场景
- 大学生或职场新人系统学习AI基础知识
- 教师用于课堂教学的配套教材
- 企业内训AI入门培训材料
- 对人工智能感兴趣的零基础自学人群

## 4. 技术亮点
- 项目获得65852+星标，说明社区认可度高
- 微软官方维护，内容权威且持续更新
- 覆盖AI主流技术栈：从传统机器学习到深度学习全流程
- 实践导向，通过Notebook提供动手编码机会
- 多主题覆盖：计算机视觉、自然语言处理、生成模型等
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65852 | 🍴 12760 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

# GitHub项目分析：ai-engineering-from-scratch

---

## 1. 中文简介

这是一个从零开始学习AI工程的全方位课程项目，旨在帮助学习者深入理解人工智能核心技术并亲手构建实际应用。项目覆盖从理论到部署的完整流程，最终目标是让学习者能够独立完成AI系统的开发并交付给他人使用。

---

## 2. 核心功能

- **从零构建AI系统**：提供完整的教学路径，帮助学习者从基础概念逐步掌握AI工程实践。
- **多领域覆盖**：内容涵盖大语言模型（LLM）、生成式AI、计算机视觉、NLP、强化学习等多个AI核心领域。
- **AI代理与 swarm 智能**：教授如何构建AI代理系统以及基于群体智能的复杂应用。
- **MCP协议支持**：集成Model Context Protocol，帮助学习者理解AI系统与外部工具的交互机制。
- **多语言技术栈**：结合Python、Rust和TypeScript，提供跨语言的工程实践指导。

---

## 3. 适用场景

- **AI学习者**：希望系统性地从零掌握AI工程技能的开发者和学生。
- **AI从业者**：需要深入理解LLM、代理系统和生成式AI底层原理的工程师。
- **课程/培训项目**：教育机构或企业用于AI技术培训的课程参考框架。
- **独立开发者**：希望构建并部署AI应用产品的个人开发者。

---

## 4. 技术亮点

- **全面的知识体系**：从机器学习基础到前沿的生成式AI和代理系统，内容覆盖完整。
- **多语言实践**：同时涉及Python、Rust和TypeScript，满足不同场景的技术需求。
- **实战导向**：强调"Learn it. Build it. Ship it"的理念，注重从学习到实际部署的全流程。
- **前沿技术集成**：涵盖MCP协议、Swarm Intelligence等较新的技术方向。

---

> **项目信息**：⭐ 47,303 星标 | 语言：Python | 类型：课程/教程项目
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47303 | 🍴 8312 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

# AI Learning 项目分析

## 1. 中文简介
这是一个涵盖数据分析与机器学习实战的综合学习项目，内容涉及线性代数、PyTorch和NLTK等工具，并基于TensorFlow 2进行深度学习实践。项目适合希望系统掌握机器学习从理论到实践的学习者。

## 2. 核心功能
- 集成经典机器学习算法：涵盖Adaboost、Apriori、FP-Growth、K-Means、逻辑回归、朴素贝叶斯、回归、SVM等
- 深度学习实战：支持DNN、RNN、LSTM等神经网络模型，基于PyTorch和TensorFlow 2框架
- NLP自然语言处理：结合NLTK库进行文本处理与机器学习应用
- 推荐系统：实现基于协同过滤等算法的推荐模型
- 线性代数与降维：包含PCA、SVD等数学基础与特征降维方法

## 3. 适用场景
- 机器学习初学者系统学习，从线性代数基础到深度学习的全链路实战
- 数据分析师提升算法能力，掌握scikit-learn等主流工具
- 深度学习研究者对比不同框架（PyTorch/TF2）的实现差异
- 面试准备，覆盖常见算法理论与代码实践

## 4. 技术亮点
- 高星项目（42468⭐），社区认可度高，学习资料丰富
- 理论与实践结合，涵盖传统ML到深度学习的完整技术栈
- 多框架支持（scikit-learn、PyTorch、TensorFlow 2），便于对比学习
- 标签分类清晰，便于按需查找特定算法实现
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42468 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36411 | 🍴 7445 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33835 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29138 | 🍴 3549 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21843 | 🍴 3357 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17379 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析

---

### 1. 中文简介
该项目是一个汇集了500个AI项目的代码资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。每个项目均附有完整代码，适合学习者参考实践。

---

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP多个方向
- 每个项目均提供可运行的源代码，便于直接学习和复现
- 项目分类清晰，按技术领域标签组织，方便快速检索
- 作为AI学习资源大全，适合从入门到进阶的系统性实践

---

### 3. 适用场景
- **AI初学者系统学习**：按领域分类浏览项目，逐步掌握各方向核心概念
- **开发者寻找实战参考**：针对具体任务（如图像分类、文本生成）快速找到开源实现
- **课程设计或项目灵感**：教师或学生可从中选取合适项目作为作业或课题

---

### 4. 技术亮点
- 高星标（36,411）表明社区认可度极高，是AI领域最受欢迎的资源合集之一
- 标签体系完善，涵盖 `artificial-intelligence`、`computer-vision`、`nlp` 等关键词，便于搜索
- 全部基于 Python 实现，生态友好，易于部署和二次开发
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36411 | 🍴 7445 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22800 | 🍴 2140 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一款领先的视觉AI高质量数据集构建平台，提供开源、云版和企业版产品，以及图像、视频和3D标注服务。它支持AI辅助标注、质量保障、团队协作、数据分析和开发者API等核心能力。

### 2. 核心功能
- 支持图像、视频及3D数据的多种标注类型（边界框、语义分割等）
- 提供AI辅助标注功能，显著提升标注效率
- 支持团队协作与质量保障机制
- 提供开源、云服务和付费企业版多种部署方案
- 开放开发者API，便于集成到现有工作流

### 3. 适用场景
- 深度学习项目的数据标注与数据集构建
- 计算机视觉模型训练前的图像/视频标注工作
- 需要团队协作的大规模标注任务
- 企业级视觉AI项目的数据质量管理

### 4. 技术亮点
- 兼容主流深度学习框架（PyTorch、TensorFlow）
- 支持ImageNet等标准数据集的标注格式
- 提供完整的标注工具链（边界框、图像分类、语义分割等）
- 16556+ GitHub星标，社区活跃度高
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16556 | 🍴 3807 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
这是一个面向计算机视觉的先进AI可解释性工具库。支持CNN、视觉Transformer等多种模型，涵盖分类、目标检测、分割、图像相似度等任务。

### 2. 核心功能
- 提供Grad-CAM、Score-CAM等多种类激活图生成方法
- 支持CNN和Vision Transformer架构模型
- 兼容图像分类、目标检测、图像分割等多种任务
- 支持图像相似度计算与可视化解释
- 基于PyTorch框架，易于集成到现有项目中

### 3. 适用场景
- 深度学习模型的可解释性分析与结果可视化
- 计算机视觉研究中的模型决策过程解释
- 医疗影像、自动驾驶等需要模型透明度的高可信场景
- 教学演示中直观展示AI模型的注意力区域

### 4. 技术亮点
- 项目星标数超12,000，社区认可度高
- 标签覆盖全面，包含Grad-CAM、Score-CAM、XAI等主流方向
- 同时支持传统CNN和前沿Vision Transformer架构
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

## Kornia 项目分析

### 1. 中文简介
Kornia 是一个专为空间AI设计的几何计算机视觉库，基于 PyTorch 构建。它将经典的计算机视觉算法与深度学习框架无缝融合，支持可微分图像处理，让传统视觉操作可以直接融入神经网络训练流程。

### 2. 核心功能
- 提供丰富的可微分几何图像处理算子（如旋转、缩放、仿射变换等）
- 支持3D视觉操作，包括相机标定、单应性变换和立体视觉
- 集成多种经典计算机视觉算法，可直接在PyTorch中端到端训练
- 提供高效的批量图像处理工具，适配GPU加速计算
- 支持机器人学中的空间变换与位姿估计操作

### 3. 适用场景
- **深度学习视觉任务**：需要在网络中嵌入可微分几何变换的场景，如图像配准、风格迁移
- **机器人导航与SLAM**：用于机器人空间感知、定位建图中的几何计算
- **3D计算机视觉**：涉及多视图几何、立体匹配、点云处理的AI应用
- **空间AI研究**：探索几何先验与深度学习结合的前沿研究项目

### 4. 技术亮点
- **可微分设计**：所有几何操作均支持梯度回传，可直接嵌入PyTorch神经网络进行端到端训练
- **PyTorch原生兼容**：张量操作与PyTorch生态无缝集成，无需额外数据转换
- **传统CV与现代DL融合**：将经典计算机视觉算法以可微分方式重新实现， bridging 传统视觉与深度学习的鸿沟
- **活跃的开源社区**：参与Hacktoberfest活动，社区贡献活跃，持续迭代更新
- 链接: https://github.com/kornia/kornia
- ⭐ 11318 | 🍴 1226 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3481 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3385 | 🍴 415 | 语言: Python
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

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全属于你的个人 AI 助手，支持任意操作系统和平台，以"龙虾"的方式让你重新掌控自己的数据。它倡导数据自主权，让 AI 助手真正为你所用，而非依赖第三方云服务。

### 2. 核心功能
- **跨平台支持**：兼容任意操作系统和运行环境，灵活部署。
- **数据自主可控**：用户完全拥有自己的数据，无需上传至第三方服务器。
- **本地化 AI 助手**：在本地运行 AI 模型，保障隐私安全。
- **模块化架构**：支持扩展和自定义，适配不同用户需求。

### 3. 适用场景
- 注重隐私的个人用户，希望 AI 助手完全本地化运行。
- 开发者或技术爱好者，想要自定义和扩展 AI 功能。
- 企业或团队，需要在内部环境中部署专属 AI 助手。

### 4. 技术亮点
- **TypeScript 编写**：类型安全，易于维护和扩展。
- **开源自由**：完全开源，用户可自由修改和分发。
- **数据主权理念**：以"龙虾"为象征，强调数据不出本地，安全可控。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386898 | 🍴 81269 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub项目分析：superpowers

### 1. 中文简介
这是一个基于AI代理的技能框架与软件开发方法论，旨在通过子代理驱动的方式提升开发效率。该项目提供了一套可落地的智能开发工作流，帮助开发者更高效地完成软件开发生命周期中的各项任务。

### 2. 核心功能
- **AI代理驱动开发**：通过子代理协作完成代码编写、调试和审查等任务
- **技能框架体系**：提供模块化的AI技能组件，支持灵活组合与扩展
- **头脑风暴与协作**：内置智能头脑风暴工具，辅助创意生成与方案设计
- **完整SDLC支持**：覆盖需求分析、设计、编码、测试到部署的全生命周期
- **OBRAS方法论**：采用结构化开发方法论，确保项目质量与可维护性

### 3. 适用场景
- 个人开发者或小型团队希望借助AI加速软件开发流程
- 需要快速原型开发或概念验证的项目
- 希望通过AI协作提升代码质量和开发效率的团队
- 探索AI代理驱动开发新范式的技术爱好者

### 4. 技术亮点
- **多代理协作架构**：支持多个子代理并行处理不同任务，提升整体开发效率
- **Shell脚本实现**：采用轻量级Shell脚本构建，易于集成到现有工作流中
- **高社区关注度**：27万+星标，证明其在开发者社区中的广泛认可
- **开源免费**：完全开源，允许自定义和二次开发
- 链接: https://github.com/obra/superpowers
- ⭐ 274770 | 🍴 24587 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## 项目分析：hermes-agent

---

### 1. 中文简介
Hermes Agent 是一个伴随用户共同成长的智能 AI 代理，能够根据使用习惯不断学习和进化。它支持多种主流大语言模型平台，为用户提供灵活、个性化的 AI 交互体验。

---

### 2. 核心功能
- **多模型支持**：兼容 Anthropic Claude、OpenAI GPT 系列、Codex 等多种大语言模型
- **自适应学习**：代理能够随使用时间积累知识，逐步适应用户偏好和工作风格
- **智能对话管理**：支持上下文记忆与多轮对话，保持长期交互的一致性
- **代码辅助能力**：集成代码理解与生成能力，适合开发者使用
- **开源可定制**：基于 Nous Research 开源生态，支持二次开发与扩展

---

### 3. 适用场景
- **日常智能助手**：作为个人 AI 助手处理日常问答、任务管理等工作
- **编程辅助**：帮助开发者进行代码审查、调试和自动生成代码
- **内容创作**：辅助撰写文档、邮件、报告等各类文本内容
- **研究探索**：支持信息检索、知识整理与深度分析研究任务

---

### 4. 技术亮点
- 支持主流 LLM 提供商的灵活切换，避免单一平台依赖
- 基于开源模型 Hermes 构建，兼顾性能与可定制性
- 项目热度高（超 23 万星标），社区活跃，持续迭代更新
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233439 | 🍴 46736 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

# n8n 项目分析

## 1. 中文简介

n8n 是一款公平代码开源的工作流自动化平台，内置原生 AI 能力。它支持可视化拖拽构建与自定义代码混合开发，可自托管或云端部署，提供 400+ 种集成连接。

## 2. 核心功能

- **可视化工作流构建**：通过拖拽节点快速搭建自动化流程
- **原生 AI 集成**：内置 AI 能力，可直接在工作流中调用大模型
- **400+ 集成连接**：支持丰富的第三方服务和 API 接入
- **灵活部署方式**：支持自托管（Self-hosted）和云端托管两种模式
- **代码与低代码结合**：既支持无代码快速搭建，也支持自定义 TypeScript 代码扩展

## 3. 适用场景

- **企业自动化流程**：如数据同步、通知推送、定时任务调度等
- **AI 应用开发**：快速构建基于 LLM 的智能助手、RAG 系统等
- **API 集成与数据流转**：连接多个 SaaS 服务，实现跨平台数据互通
- **MCP 协议支持**：可作为 MCP 客户端/服务器，与 AI Agent 无缝集成

## 4. 技术亮点

- 采用 TypeScript 开发，类型安全且易于扩展
- 支持 MCP（Model Context Protocol）协议，可与主流 AI 框架（如 Claude、Cursor）深度集成
- 公平代码（Fair-code）许可证，兼顾开源与商业友好
- 20万+ GitHub 星标，社区活跃度高，生态成熟
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201340 | 🍴 60248 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI 工具，实现人人可用的 AI 愿景。我们的使命是提供必要的工具，让你能够专注于真正重要的事物。

### 2. 核心功能
- 支持自主智能体（Agent）运行，能够自主规划并执行复杂任务
- 集成多种大语言模型（OpenAI、Claude、LLaMA 等），灵活选择模型后端
- 具备自我反思与迭代优化能力，可自动修正错误并改进输出
- 支持多步骤任务分解，将复杂目标拆解为可执行的子任务链
- 提供可扩展的插件系统，便于自定义功能模块

### 3. 适用场景
- 自动化日常任务（如信息检索、数据整理、报告生成）
- 内容创作辅助（文案撰写、代码生成、方案设计）
- 研究探索任务（文献调研、竞品分析、知识汇总）
- AI 应用开发原型快速验证

### 4. 技术亮点
- 多模型兼容架构，支持 OpenAI、Claude、LLaMA API 等多种 LLM 后端
- 高度模块化的 Agent 设计，便于二次开发与功能扩展
- 活跃的开源社区，星标数超过 18.6 万，生态资源丰富
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186686 | 🍴 46049 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 169962 | 🍴 9469 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167637 | 🍴 21641 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164595 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157910 | 🍴 46170 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153504 | 🍴 9899 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

