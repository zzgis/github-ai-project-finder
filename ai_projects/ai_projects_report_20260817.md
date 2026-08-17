# GitHub AI项目每日发现报告
日期: 2026-08-17

## 新发布的AI项目

### cumora
- 

## cumora 项目分析

### 1. 中文简介
cumora 是一个跨平台团队协作聊天工具，AI 智能体作为一等公民团队成员参与协作。它支持云端大脑或用户自带智能体（如 Claude Code / Codex），让团队可以灵活选择 AI 能力来源。

### 2. 核心功能
- 跨平台团队聊天，支持多设备无缝协作
- AI 智能体作为团队正式成员参与对话与任务
- 支持云端大脑与自带智能体（BYO）两种模式
- 兼容 Claude Code 和 Codex 等主流 AI 工具
- 基于 TypeScript 构建，易于扩展和定制

### 3. 适用场景
- 开发团队需要将 AI 智能体纳入日常协作流程
- 希望灵活切换云端 AI 或自有 AI 服务的企业
- 需要多智能体协同完成复杂任务的场景
- 追求跨平台一致体验的远程协作团队

### 4. 技术亮点
- 采用 TypeScript 开发，类型安全且生态友好
- 支持插件式 AI 大脑接入，架构灵活可扩展
- 836 星标表明社区关注度较高，项目活跃
- 链接: https://github.com/yetone/cumora
- ⭐ 836 | 🍴 94 | 语言: TypeScript

### zhijian-ai-bluebook-workbuddy-harness
- 

## 项目分析：zhijian-ai-bluebook-workbuddy-harness

### 1. 中文简介
本项目是"智见 AI"系列蓝皮书之一，深入拆解 WorkBuddy 智能体框架的核心组件，涵盖提示词设计、记忆机制、插件系统、专家模块、Skill 能力与安全边界等关键维度。

### 2. 核心功能
- **提示词工程分析**：拆解 WorkBuddy 的提示词设计与优化方法
- **记忆机制研究**：解析智能体的短期与长期记忆实现方案
- **插件系统拆解**：梳理插件架构与扩展能力
- **专家与 Skill 模块**：分析专家角色设定与技能调用机制
- **安全边界探讨**：明确 AI 智能体的能力边界与安全约束

### 3. 适用场景
- AI 智能体框架开发者参考 WorkBuddy 架构设计
- 希望深入理解提示词与记忆机制的 AI 应用开发者
- 研究 AI 安全边界与约束设计的团队
- 对蓝皮书系列技术文档有需求的 AI 研究者

### 4. 技术亮点
- 以"蓝皮书"形式系统性地拆解 WorkBuddy 核心架构，内容结构清晰
- 覆盖从提示词到安全边界的完整技术栈，适合系统性学习
- 聚焦 AI Agent 的实际工程实践，具有较强的参考价值
- 链接: https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness
- ⭐ 149 | 🍴 15 | 语言: 未知
- 标签: ai-agent, bluebook, harness, workbuddy, zhijian-ai

### ai-data-extractor
- 

## 项目分析：ai-data-extractor

### 1. 中文简介

这是一个免费的开源工具，用于提取 AI 编程助手的聊天记录数据。支持 Claude Code、Cursor、Windsurf、Aider、Cline/Roo Code 等多种主流 AI 编程助手平台。

### 2. 核心功能

- 一键导出 AI 编程助手的对话历史数据
- 支持多平台适配（Claude Code、Cursor、Windsurf 等）
- 将聊天记录转换为结构化数据格式，便于后续分析
- 完全开源免费，可自由使用和修改

### 3. 适用场景

- **个人复盘**：回顾与 AI 助手的对话，总结编程经验
- **数据迁移**：将聊天记录从不同平台统一导出备份
- **团队协作**：分享 AI 辅助编程的最佳实践和解决方案
- **数据分析**：基于导出的数据研究 AI 编程助手的交互模式

### 4. 技术亮点

- 采用 Python 开发，跨平台兼容性好
- 多平台适配架构，可扩展支持更多 AI 编程助手
- 开源项目，社区可参与贡献和维护
- 链接: https://github.com/bawadou/ai-data-extractor
- ⭐ 85 | 🍴 32 | 语言: Python
- 标签: ai, ai-data-extractor, claude, cursor, cursor-ai

### graph-memory-starter
- 

# graph-memory-starter 项目分析

## 1. 中文简介
这是一个为AI助手提供知识图谱记忆的轻量级解决方案。通过三个SQLite表存储结构化知识，配合递归查询和prompt钩子实现上下文记忆功能。

## 2. 核心功能
- **知识图谱存储**：使用三个SQLite表管理实体、关系和属性数据
- **递归查询能力**：支持多层级关系遍历，实现知识推理
- **Prompt集成**：通过钩子机制将图谱知识注入AI对话上下文
- **轻量级架构**：纯Python实现，无外部依赖，快速部署
- **结构化记忆**：将非结构化对话转化为可查询的知识图谱

## 3. 适用场景
- **个人AI助手**：需要记住用户偏好、历史对话的桌面/移动端助手
- **客服机器人**：存储客户信息、购买历史，提供个性化服务
- **教育辅导系统**：记录学生学习轨迹，实现自适应教学
- **小型知识管理系统**：个人笔记、书签的语义化检索

## 4. 技术亮点
- **极简设计**：仅用三个表+一个递归查询实现完整知识图谱功能
- **零依赖部署**：SQLite内置支持，无需额外数据库服务
- **Prompt Hook机制**：无缝集成现有AI框架，无需修改核心逻辑
- **递归推理**：支持多跳关系查询，发现隐含知识关联

---

**总体评价**：这是一个适合小型AI项目的轻量级知识记忆方案，特别适合资源受限环境或快速原型开发。对于需要长期记忆和上下文理解的应用场景具有实用价值。
- 链接: https://github.com/Glitch-Cat-Club/graph-memory-starter
- ⭐ 70 | 🍴 8 | 语言: Python

### bigpeng-hot-gzh
- 

# GitHub 项目分析：bigpeng-hot-gzh

## 1. 中文简介
该项目从约 100 篇爆款 AI 主题公众号文章中提炼出选题方向与标题撰写技巧，形成一套可复用的写作方法论。旨在帮助创作者掌握打造热门公众号文章的核心规律。

## 2. 核心功能
- 归纳爆款文章的选题方向与热门话题类型
- 提取并总结高点击率标题的写作套路与结构
- 提供可直接参考的标题模板与表达框架
- 以 Skill（技能文档）形式呈现，便于快速查阅与应用

## 3. 适用场景
- AI 领域公众号运营者策划选题与拟定标题
- 内容创作者学习爆款文章的结构与写作技巧
- 新媒体团队进行内容培训与写作规范制定

## 4. 技术亮点
- 基于真实爆款数据提炼，具有较强的实战参考价值
- 以"Skill"形式组织内容，结构清晰、便于快速检索与复用
- 链接: https://github.com/BigPengSays/bigpeng-hot-gzh
- ⭐ 61 | 🍴 5 | 语言: 未知

### deepseek-harness-pr-review
- 描述: AI code review with DeepSeek: headless PR review automation that verifies PR descriptions claim-by-claim against real code, checks docs against reality, flags requirement impact, human-in-the-loop + auto review poller + web dashboard
- 链接: https://github.com/nexpeakcore/deepseek-harness-pr-review
- ⭐ 34 | 🍴 12 | 语言: Python
- 标签: agentic-ai, ai-agent, ai-code-review, automation, automation-tools

### ai-tools-radar
- 描述: AI 工具站增长情报库:真实流量/增长曲线/新品雷达/dofollow 外链库 · Growth intelligence for AI tools, runs locally
- 链接: https://github.com/ppop123/ai-tools-radar
- ⭐ 31 | 🍴 21 | 语言: Python

### idor-tester-ai
- 描述: 无描述
- 链接: https://github.com/poriaporhashemi/idor-tester-ai
- ⭐ 30 | 🍴 7 | 语言: Python

### dance-video-to-prompt
- 描述: 本地短视频反推 AI 视频生成提示词：抽帧、清晰度、节奏卡点、Agent Skill
- 链接: https://github.com/CattleZ/dance-video-to-prompt
- ⭐ 28 | 🍴 1 | 语言: Python

### Alvarmethod
- 描述: One-to-one AI teaching skills (Alvar method) for Codex, Claude Code, Grok, Pi, and OpenCode
- 链接: https://github.com/vasanthsreeram/Alvarmethod
- ⭐ 27 | 🍴 3 | 语言: Shell

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82512 | 🍴 15267 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI机器学习/深度学习/计算机视觉/NLP项目合集

### 1. 中文简介
这是一个收录了500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，每个项目均附带完整代码实现。该项目由社区维护，是一个高质量的awesome列表，适合AI学习者和开发者参考。

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供可运行的代码实现，便于动手实践
- 按技术领域分类整理，结构清晰，方便快速查找
- 持续更新维护，保持项目列表的时效性和丰富度

### 3. 适用场景
- AI初学者系统学习，从基础到进阶循序渐进
- 开发者寻找实战项目灵感，快速搭建原型
- 研究人员参考最新技术方案和实现思路
- 企业团队进行技术选型和方案调研

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流应用领域
- 所有项目均附带代码，强调实践导向
- 采用awesome列表形式，社区贡献维护，质量有保障
- 36336个星标，表明其在AI社区具有广泛影响力
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36336 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，帮助用户直观地查看和调试模型结构。该项目在 GitHub 上获得了 33,363 颗星标，是 AI 领域最受欢迎的开源工具之一。

### 2. 核心功能
- 支持多种模型格式的可视化，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 Safetensors 等
- 提供网络结构的图形化展示，清晰呈现层与层之间的连接关系
- 支持模型参数的查看与编辑，方便调试和优化
- 可在浏览器或桌面端运行，使用便捷无需复杂配置
- 兼容 numpy 数组数据格式，支持模型数据的导入导出

### 3. 适用场景
- **模型调试**：深度学习开发者可视化模型结构，快速定位网络设计问题
- **模型交流**：向非技术人员或团队成员展示神经网络架构，便于沟通与协作
- **模型转换验证**：在框架迁移（如 PyTorch 转 ONNX）后验证模型结构是否正确
- **教育学习**：帮助学生理解神经网络各层的连接方式和数据流向

### 4. 技术亮点
- 跨平台支持，兼容 Windows、macOS、Linux 及浏览器环境
- 轻量级设计，无需安装庞大的深度学习框架即可运行
- 开源免费，社区活跃，持续更新维护
- 支持 safetensors 等新兴安全模型格式，紧跟技术发展趋势
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33363 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习互操作性的开放标准，旨在实现不同深度学习框架之间的模型互通。它允许开发者在不同的AI框架之间自由迁移模型，打破框架壁垒，提升开发效率。

### 2. 核心功能
- 提供统一的模型格式，支持跨框架模型转换
- 兼容PyTorch、TensorFlow、Keras、scikit-learn等主流框架
- 支持模型部署到多种硬件平台（CPU、GPU、移动端等）
- 提供模型优化工具链，支持推理加速

### 3. 适用场景
- 将PyTorch模型转换为TensorFlow或ONNX格式进行部署
- 在移动端或边缘设备上运行深度学习模型
- 跨团队协作，不同成员使用不同框架时共享模型
- 模型从训练环境迁移到生产推理环境

### 4. 技术亮点
- 由微软和Facebook（现Meta）联合发起，生态成熟
- 拥有庞大的社区支持和活跃的维护团队
- 支持动态形状和自定义算子扩展
- 与ONNX Runtime结合可实现高性能推理
- 链接: https://github.com/onnx/onnx
- ⭐ 21320 | 🍴 4000 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## GitHub项目分析：ml-engineering

---

### 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的开源指南，内容涵盖从模型训练、调试到推理部署的完整工程链路，适合希望深入掌握LLM大规模训练与部署的工程师和研究人员。

---

### 2. 核心功能
- **大规模模型训练**：提供PyTorch/Transformers框架下LLM高效训练的最佳实践。
- **GPU与分布式调试**：覆盖多GPU、多节点训练中的性能瓶颈分析与故障排查。
- **推理优化**：详解模型推理阶段的加速策略与部署方案。
- **基础设施管理**：结合Slurm调度器，讲解集群资源管理与可扩展性设计。
- **存储与网络优化**：针对大规模训练中的I/O瓶颈提供存储与网络调优方案。

---

### 3. 适用场景
- 需要从零搭建LLM训练基础设施的MLOps工程师。
- 面临多GPU/多节点训练性能问题、需要系统性调试方法的团队。
- 希望优化模型推理延迟与吞吐量的生产环境部署场景。
- 学习大规模机器学习系统工程实践的开发者与研究者。

---

### 4. 技术亮点
- 项目以"开放手册"形式组织，内容结构清晰、覆盖工程全链路，而非零散教程。
- 标签涵盖从底层硬件（GPU、存储、网络）到上层框架（PyTorch、Transformers）的完整技术栈，实战导向强。
- 18,646星标表明其在社区中具有较高的认可度和广泛使用。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18646 | 🍴 1201 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17360 | 🍴 2120 | 语言: 未知
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
- ⭐ 11627 | 🍴 915 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10687 | 🍴 5701 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析：500 AI机器学习/深度学习/计算机视觉/NLP项目合集

### 1. 中文简介
这是一个收录了500个AI项目的资源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，每个项目均附带完整代码实现。该项目由社区维护，是一个高质量的awesome列表，适合AI学习者和开发者参考。

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均提供可运行的代码实现，便于动手实践
- 按技术领域分类整理，结构清晰，方便快速查找
- 持续更新维护，保持项目列表的时效性和丰富度

### 3. 适用场景
- AI初学者系统学习，从基础到进阶循序渐进
- 开发者寻找实战项目灵感，快速搭建原型
- 研究人员参考最新技术方案和实现思路
- 企业团队进行技术选型和方案调研

### 4. 技术亮点
- 项目数量庞大（500个），覆盖AI主流应用领域
- 所有项目均附带代码，强调实践导向
- 采用awesome列表形式，社区贡献维护，质量有保障
- 36336个星标，表明其在AI社区具有广泛影响力
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36336 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款专为神经网络、深度学习和机器学习模型设计的可视化工具。它支持多种主流框架的模型格式，帮助用户直观地查看和调试模型结构。该项目在 GitHub 上获得了 33,363 颗星标，是 AI 领域最受欢迎的开源工具之一。

### 2. 核心功能
- 支持多种模型格式的可视化，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 和 Safetensors 等
- 提供网络结构的图形化展示，清晰呈现层与层之间的连接关系
- 支持模型参数的查看与编辑，方便调试和优化
- 可在浏览器或桌面端运行，使用便捷无需复杂配置
- 兼容 numpy 数组数据格式，支持模型数据的导入导出

### 3. 适用场景
- **模型调试**：深度学习开发者可视化模型结构，快速定位网络设计问题
- **模型交流**：向非技术人员或团队成员展示神经网络架构，便于沟通与协作
- **模型转换验证**：在框架迁移（如 PyTorch 转 ONNX）后验证模型结构是否正确
- **教育学习**：帮助学生理解神经网络各层的连接方式和数据流向

### 4. 技术亮点
- 跨平台支持，兼容 Windows、macOS、Linux 及浏览器环境
- 轻量级设计，无需安装庞大的深度学习框架即可运行
- 开源免费，社区活跃，持续更新维护
- 支持 safetensors 等新兴安全模型格式，紧跟技术发展趋势
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33363 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介
本项目为深度学习与机器学习研究者提供必备的速查手册集合，涵盖核心概念、常用库及框架的快速参考指南，帮助研究者和开发者高效查阅关键技术要点。

### 2. 核心功能
- 提供深度学习与机器学习核心概念的速查表
- 整理 NumPy、SciPy、Matplotlib 等科学计算库的常用用法
- 包含 Keras 等深度学习框架的快速参考
- 汇总机器学习算法的关键参数与使用技巧
- 整合 Python 数据科学生态工具的备忘清单

### 3. 适用场景
- 深度学习研究者日常查阅 API 用法和参数配置
- 机器学习初学者系统复习核心知识点
- 数据科学家开发时快速检索代码示例
- 面试准备时快速回顾关键技术要点

### 4. 技术亮点
项目将分散的技术资料整合为结构化的速查表形式，覆盖从基础科学计算库到深度学习框架的完整工具链，便于快速检索和系统学习。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3373 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13261 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11748 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9173 | 🍴 1232 | 语言: Python
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
- ⭐ 82512 | 🍴 15267 | 语言: Python

### LlamaFactory
- 

# LlamaFactory 项目分析

## 1. 中文简介
LlamaFactory 是一个统一高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100 多种模型的微调训练，相关研究论文发表于 ACL 2024。

## 2. 核心功能
- 支持 100+ 种大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、全参数微调等多种微调策略
- 支持 RLHF（基于人类反馈的强化学习）对齐训练
- 兼容 Transformers、PEFT 等主流深度学习框架
- 支持量化技术（如 4-bit/8-bit 量化）降低显存占用

## 3. 适用场景
- 对 LLaMA、Qwen、DeepSeek、Gemma 等主流模型进行指令微调
- 在显存受限的硬件环境下使用 QLoRA 进行高效微调
- 需要多模态（图文）模型微调的视觉语言任务
- 通过 RLHF 对齐技术优化模型输出质量

## 4. 技术亮点
- 统一接口支持 100+ 模型，无需为不同模型编写独立训练代码
- 集成量化技术，显著降低显存需求，提升训练效率
- 支持 MoE（混合专家）架构模型的高效微调
- 社区活跃，GitHub 星标数超过 7.4 万，是热门开源项目
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74166 | 🍴 9077 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

# GitHub项目分析：AI-For-Beginners

## 1. 中文简介
该项目是一套由微软开发的AI入门课程体系，为期12周、共24节课程，致力于让所有人都能轻松学习人工智能。课程采用Jupyter Notebook形式，内容覆盖机器学习、深度学习、自然语言处理等核心领域。

## 2. 核心功能
- 提供系统化的12周AI学习路径，适合零基础入门
- 涵盖机器学习、深度学习、计算机视觉、NLP等核心主题
- 使用Jupyter Notebook交互式教学，便于动手实践
- 包含CNN、RNN、GAN等前沿技术专题
- 由微软官方维护，课程质量有保障

## 3. 适用场景
- 高校或培训机构用于AI通识课程教学
- 职场人士自学人工智能基础知识
- 对AI感兴趣的初学者系统性入门学习
- 企业内部分享AI基础知识培训

## 4. 技术亮点
- 微软官方出品，课程结构科学、内容权威
- 65153+星标，社区认可度高，学习资源丰富
- 覆盖从传统机器学习到深度学习的完整知识体系
- 交互式Notebook格式，边学边练，实践性强
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65153 | 🍴 12648 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub 项目分析：ai-engineering-from-scratch

---

### 1. 中文简介
本项目是一套从零开始构建 AI 系统的完整学习课程，涵盖理论理解、动手实现到最终交付的完整链路，帮助学习者真正掌握 AI 工程的核心能力。

---

### 2. 核心功能
- **从零实现 AI 系统**：不依赖高级框架，深入理解 AI 底层原理并手动构建。
- **多领域覆盖**：涵盖 LLM、计算机视觉、强化学习、MCP、Agent 系统等热门方向。
- **完整课程结构**：提供系统化的教程路径，适合循序渐进学习。
- **多语言支持**：课程使用 Python 和 TypeScript 两种语言实现，适配不同技术栈。
- **生产级交付**：不仅教理论，还指导如何将 AI 项目部署并交付给他人使用。

---

### 3. 适用场景
- AI 初学者希望系统性地从底层理解并构建 AI 项目。
- 工程师希望深入掌握 LLM、Agent、多智能体系统等前沿技术的实现细节。
- 团队或个人希望学习如何将 AI 模型从实验转化为可交付的生产级应用。
- 教育者寻找一套结构完整、可落地的 AI 工程课程教材。

---

### 4. 技术亮点
- **跨技术栈融合**：同时使用 Python（AI 主流语言）和 TypeScript，覆盖前后端与 AI 工程全链路。
- **前沿技术全覆盖**：标签涵盖 Agent、MCP、Swarm Intelligence、Transformers 等当前最热门的 AI 工程方向。
- **高社区认可度**：47014 星标表明该项目在开发者社区中具有较高的影响力和实用性。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47014 | 🍴 8236 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：ailearning

### 1. 中文简介
这是一个综合性的AI学习资源项目，涵盖数据分析、机器学习实战、线性代数基础，以及PyTorch和TensorFlow 2等深度学习框架的应用。项目内容全面，适合系统学习人工智能相关知识。

### 2. 核心功能
- 提供数据分析与机器学习算法的实战代码示例
- 集成PyTorch和TensorFlow 2深度学习框架的教程
- 涵盖NLP自然语言处理（NLTK）相关技术
- 包含经典机器学习算法：KMeans、SVM、逻辑回归、朴素贝叶斯、AdaBoost等
- 涵盖深度学习模型：LSTM、RNN、DNN等神经网络结构

### 3. 适用场景
- 机器学习初学者系统学习算法理论与实战
- 深度学习爱好者使用PyTorch/TensorFlow构建模型
- NLP开发者学习文本处理与自然语言理解技术
- 数据科学家进行推荐系统、分类、回归等任务开发

### 4. 技术亮点
- 项目星标数高达42459，说明社区认可度极高
- 内容覆盖从基础线性代数到进阶深度学习的完整学习路径
- 同时支持PyTorch和TensorFlow两大主流框架，适合不同技术偏好者
- 标签丰富，涵盖经典ML算法与前沿DL技术，学习资源全面
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42459 | 🍴 11517 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36336 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33826 | 🍴 4709 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29084 | 🍴 3541 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21840 | 🍴 3354 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17360 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的代码集合库，涵盖了人工智能领域的多个核心方向。该项目通过标签分类整理，为学习者和开发者提供了丰富的实战项目资源。

### 2. 核心功能
- 收录500个涵盖AI各领域的完整项目代码
- 按机器学习、深度学习、计算机视觉、NLP等方向分类整理
- 提供可直接运行的Python代码实现
- 包含详细的标签分类便于快速检索
- 适合从入门到进阶的各级学习者

### 3. 适用场景
- AI初学者系统学习各方向实战项目
- 开发者寻找项目灵感或参考实现
- 数据科学家构建作品集和简历项目
- 教师用于课堂教学和课程作业设计

### 4. 技术亮点
- 高星标数（36336）证明社区认可度极高
- 项目覆盖AI主流方向的完整技术栈
- 所有项目均附带可运行代码，实战性强
- 标签体系完善，便于针对性学习
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36336 | 🍴 7438 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一个利用 AI 技术自动化浏览器工作流的开源项目。它通过结合大语言模型（LLM）和计算机视觉能力，让机器能够像人类一样理解和操作网页界面，从而实现复杂的浏览器自动化任务。

### 2. 核心功能
- **AI 驱动浏览器自动化**：利用大语言模型理解网页内容并执行操作
- **多引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **视觉识别能力**：通过计算机视觉识别页面元素和界面状态
- **API 工作流**：提供 API 接口，便于集成到现有系统中
- **RPA 流程自动化**：支持录制和回放重复性网页操作任务

### 3. 适用场景
- **企业 RPA 自动化**：自动化处理报销、数据录入等重复性办公流程
- **网页数据采集**：智能抓取动态网页内容，突破传统爬虫限制
- **自动化测试**：AI 辅助的 UI 测试和回归测试
- **跨平台工作流**：需要多步骤浏览器操作的复杂业务流程

### 4. 技术亮点
- **LLM + 视觉双引擎**：结合大语言模型的理解能力和计算机视觉的识别能力，实现更智能的页面交互
- **低代码/无代码**：降低浏览器自动化的使用门槛，非技术人员也能快速上手
- **开源生态**：基于 Python 开发，社区活跃，星标数超过 2.2 万，具有较高的参考价值
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22769 | 🍴 2140 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是一款领先的开源平台，专注于构建高质量的视觉数据集以服务于视觉AI。它提供开源、云端和企业版产品，支持图像、视频和3D标注，并内置AI辅助标注、质量保证、团队协作及开发者API等功能。

### 2. 核心功能
- 支持图像、视频和3D数据的标注
- 提供AI辅助自动标注，提升标注效率
- 内置质量保证机制，确保标注数据准确性
- 支持团队协作，方便多人共同完成标注项目
- 开放开发者API，便于集成到现有工作流

### 3. 适用场景
- 构建目标检测（Object Detection）训练数据集
- 进行语义分割（Semantic Segmentation）标注
- 视频目标追踪与标注
- 大规模图像分类数据集制作

### 4. 技术亮点
- 完全开源，支持本地部署和云端使用
- 兼容PyTorch和TensorFlow等主流深度学习框架
- 支持多种标注格式，包括边界框、多边形、关键点等
- 提供丰富的标签生态，涵盖ImageNet、COCO等常见数据集标准
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16538 | 🍴 3804 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

## pytorch-grad-cam 项目分析

### 1. 中文简介
这是一个面向计算机视觉的高级AI可解释性工具库，支持CNN和Vision Transformers等多种网络架构。适用于图像分类、目标检测、图像分割、图像相似度等多种视觉任务。

### 2. 核心功能
- 支持Grad-CAM、Grad-CAM++、Score-CAM等多种可视化方法
- 兼容PyTorch框架，支持CNN和Vision Transformer架构
- 提供图像分类、目标检测、图像分割和图像相似度等多种任务支持
- 生成热力图可视化，直观展示模型决策依据

### 3. 适用场景
- 图像分类任务中定位模型关注的区域
- 医学影像分析中增强诊断结果的可解释性
- 视觉Transformer模型的可解释性研究
- 目标检测任务中验证模型是否正确识别目标区域

### 4. 技术亮点
- 支持从基础Grad-CAM到高级变体（如Grad-CAM++、Score-CAM）的完整算法家族
- 内置对Vision Transformers的专门支持，适配最新架构
- 提供简洁易用的API接口，便于集成到现有项目中
- 社区认可度高，星标数超过12954
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# Kornia 项目分析

## 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，基于 PyTorch 构建，提供可微分的图像处理原语。它旨在将传统计算机视觉技术与深度学习无缝融合，为研究人员和开发者提供高效、灵活的视觉计算工具。

## 2. 核心功能
- 提供丰富的可微分图像处理算子（如滤波、变换、色彩空间转换）
- 支持张量化的几何计算，兼容 GPU 加速
- 内置相机标定、三维重建和姿态估计等模块
- 与 PyTorch 生态深度集成，便于构建端到端视觉模型

## 3. 适用场景
- 机器人视觉感知与空间理解任务
- 深度学习中的图像增强与数据预处理流水线
- 可微分渲染与三维视觉研究
- 自动驾驶中的环境感知与定位系统

## 4. 技术亮点
- **可微分设计**：所有算子均可反向传播，支持端到端训练
- **JIT 编译优化**：通过 TorchScript 提升推理性能
- **模块化架构**：灵活组合基础算子构建复杂视觉管线
- **活跃的开源社区**：Hacktoberfest 友好项目，持续迭代更新
- 链接: https://github.com/kornia/kornia
- ⭐ 11315 | 🍴 1223 | 语言: Python
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
- ⭐ 3380 | 🍴 412 | 语言: Python
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

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款个人 AI 助手工具，支持任意操作系统和平台运行，强调数据自主可控。以"龙虾"为象征，致力于让用户真正拥有并掌控自己的 AI 助手。

### 2. 核心功能
- 跨平台支持，可在任意操作系统上运行个人 AI 助手
- 数据完全由用户自主掌控，保障隐私安全
- 提供个性化的 AI 助手体验
- 开源项目，代码透明可审计
- 支持多种 AI 模型接入

### 3. 适用场景
- 注重数据隐私、希望本地化运行 AI 助手的个人用户
- 需要在不同操作系统间切换使用的多平台工作者
- 希望自定义 AI 助手功能的技术爱好者
- 企业或个人搭建私有化 AI 助手服务

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态丰富
- 跨平台架构设计，一套代码多端运行
- 开源架构，社区可参与贡献与二次开发
- 支持"Own Your Data"理念，数据本地优先存储
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386526 | 🍴 81219 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

# GitHub 项目分析：superpowers

## 1. 中文简介
superpowers 是一个基于 AI 的智能体技能框架与软件开发方法论，旨在通过子代理驱动开发的方式提升软件开发效率。它提供了一套可落地的技能体系，帮助开发者更系统化地完成编码任务。

## 2. 核心功能
- **智能体技能框架**：提供可复用的 AI 技能模块，支持自动化开发流程。
- **子代理驱动开发（Subagent-Driven Development）**：通过多个子代理协作完成复杂任务。
- **头脑风暴辅助**：内置 AI 辅助的创意与方案讨论功能。
- **完整 SDLC 支持**：覆盖从需求分析到代码交付的软件开发生命周期。
- **ORBA 方法论**：提供一套结构化的开发流程指导。

## 3. 适用场景
- AI 辅助的代码编写与项目重构。
- 需要多步骤协作的复杂软件开发任务。
- 团队头脑风暴与技术方案设计讨论。
- 希望引入 AI 智能体提升开发效率的个人或团队。

## 4. 技术亮点
- 以 **Shell 脚本** 实现，轻量且易于集成到现有工作流中。
- 高人气项目（27万+ 星标），社区活跃，持续迭代。
- 标签涵盖 AI、编码、SDLC 等，定位清晰，聚焦于**可落地的 AI 开发方法论**。
- 链接: https://github.com/obra/superpowers
- ⭐ 273110 | 🍴 24430 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
Hermes Agent 是一个能够与你共同成长的智能体系统，支持接入多种主流大语言模型。它通过持续学习和交互，逐步适应用户的工作习惯与需求。

### 2. 核心功能
- 支持接入 Anthropic Claude、OpenAI GPT 等多种大语言模型
- 提供智能体自动化任务处理能力
- 具备代码生成与代码审查功能
- 支持个性化配置与持续学习能力
- 兼容 Claude Code 和 Codex 等开发工具生态

### 3. 适用场景
- **软件开发辅助**：代码编写、调试、重构等编程任务
- **日常办公自动化**：文档处理、信息整理、流程自动化
- **AI 应用开发**：构建基于 LLM 的智能应用原型
- **研究与分析**：数据分析、文献调研、报告生成

### 4. 技术亮点
- 由 Nous Research 团队开发，支持多模型灵活切换
- 轻量级架构设计，易于集成到现有工作流中
- 开源项目，社区活跃，持续迭代更新
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 231886 | 🍴 46165 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码（fair-code）工作流自动化平台，具备原生 AI 能力。它支持可视化构建与自定义代码相结合，可自托管或部署于云端，并提供 400 多种集成。

### 2. 核心功能
- **可视化工作流构建**：通过拖拽式界面轻松设计自动化流程
- **原生 AI 集成**：内置 AI 能力，支持智能工作流编排
- **灵活部署方式**：支持自托管或云端部署，满足不同安全需求
- **丰富的集成生态**：提供 400+ 预置集成，覆盖主流 API 和服务
- **低代码 + 自定义代码混合开发**：既支持无代码快速搭建，也允许编写自定义代码实现复杂逻辑

### 3. 适用场景
- **企业自动化流程**：如数据同步、报表生成、通知推送等跨系统自动化
- **API 集成与数据流转**：连接多个 SaaS 服务，实现数据自动采集与处理
- **AI 驱动的智能工作流**：结合 LLM 实现智能客服、内容生成、数据分析等场景
- **自托管合规需求**：金融、医疗等对数据隐私有严格要求的行业

### 4. 技术亮点
- **TypeScript 全栈开发**：代码质量高，类型安全，易于维护扩展
- **支持 MCP 协议**：内置 MCP 客户端与服务端，可与 AI 模型无缝对接
- **公平代码许可**：在开源基础上限制竞争用途，兼顾社区与商业利益
- **iPaaS 级集成能力**：作为集成平台即服务（iPaaS），提供企业级工作流编排能力
- 链接: https://github.com/n8n-io/n8n
- ⭐ 200961 | 🍴 60193 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

# AutoGPT 项目分析

## 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI 工具，实现 AI 的普及化愿景。我们的使命是提供强大的工具，让您能够专注于真正重要的事务。

## 2. 核心功能
- **自主任务执行**：AI 代理可自主规划并执行复杂的多步骤任务
- **多模型支持**：兼容 OpenAI、Claude、Llama 等多种大语言模型 API
- **记忆系统**：具备长期记忆能力，可跨任务保持上下文连贯性
- **工具扩展生态**：支持集成浏览器、代码执行、文件操作等多种外部工具
- **目标驱动决策**：根据用户设定的目标自主分解任务并迭代执行

## 3. 适用场景
- **自动化工作流**：如自动调研、数据收集和报告生成等重复性任务
- **编程辅助**：自动编写、调试和优化代码片段
- **信息检索与研究**：自主联网搜索、整合多源信息并输出总结
- **内容创作**：辅助生成文章、社交媒体内容或营销文案

## 4. 技术亮点
- 采用多代理（Multi-Agent）架构，支持任务并行与协作
- 基于 GPT-4 等先进模型，具备较强的推理与规划能力
- 开源社区活跃，持续迭代更新，生态丰富
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186641 | 🍴 46061 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 168496 | 🍴 9427 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167302 | 🍴 21591 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164534 | 🍴 30553 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157820 | 🍴 46175 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153357 | 🍴 9873 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

