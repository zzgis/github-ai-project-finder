# GitHub AI项目每日发现报告
日期: 2026-07-17

## 新发布的AI项目

### Awesome_ai_learning
- 由于该项目描述为“None”且标签为空，仅凭元数据无法直接获取具体代码逻辑。但根据项目名称 "Awesome_ai_learning" 及 GitHub 上同类 "Awesome-list" 的性质，可以推断其为一个精选的资源聚合库。以下是基于项目命名惯例和常见功能的分析与翻译：

1. **中文简介**
   这是一个精心整理的 AI 学习资源合集，旨在为初学者到专家提供系统化的学习路径。它汇集了人工智能、机器学习、深度学习等领域的优质教程、论文和项目示例，帮助用户高效掌握前沿技术。

2. **核心功能**
   - 分类整理 AI 基础理论与实战技巧的学习资料。
   - 收录各领域顶尖学术论文、开源项目及工具库链接。
   - 提供从入门到进阶的结构化学习路线图。
   - 筛选高质量社区资源和最新技术动态。
   - 支持多语言或特定领域（如 NLP、CV）的专项资源导航。

3. **适用场景**
   - AI 初学者寻找系统化入门教程和基础知识框架。
   - 研究人员追踪最新学术成果并参考经典开源实现。
   - 工程师快速定位解决特定技术问题的高效工具链。
   - 企业培训团队构建内部 AI 技能提升课程资源库。

4. **技术亮点**
   - 采用“Awesome-list”社区标准维护，确保资源质量与时效性。
   - 结构化分类清晰，便于用户按需检索不同阶段的学习材料。
   - 聚合多方权威来源，形成一站式 AI 知识导航平台。
- 链接: https://github.com/h9-tec/Awesome_ai_learning
- ⭐ 121 | 🍴 13 | 语言: 未知

### OpenMicro
- 1. **中文简介**
OpenMicro 是一个基于 TypeScript 构建的开源项目，旨在将任何游戏手柄的功能映射到代码编写环境中。它允许用户通过游戏控制器来驱动类似 Codex 或 Claude Code 的 AI 编程代理，实现独特的“氛围编程”体验。该项目通过自定义的编码接口（Coding Harness），让硬件输入直接控制软件智能体的行为。

2. **核心功能**
- 支持任意游戏手柄接入并映射按键操作至编程环境。
- 兼容主流 AI 编码助手（如 Codex CLI、Claude Code 等）。
- 提供“Agentic AI”交互模式，让用户通过手柄控制代码生成流程。
- 基于 TypeScript 开发，具备良好的类型安全和扩展性。
- 集成“Vibe Coding”理念，强调非传统键盘输入下的沉浸式编码体验。

3. **适用场景**
- 游戏开发者希望用熟悉的游戏手柄快捷键来辅助日常代码编写。
- 对传统键盘编码感到疲劳的用户，尝试通过游戏控制器进行创意性编程。
- 需要双手离开键盘的场景下（如身体其他部位操控外设），利用手柄微调 AI 生成的代码。
- 探索人机交互新范式的技术爱好者，测试硬件控制器与 AI 代理的融合可能性。

4. **技术亮点**
- 创新性地将游戏硬件输入抽象为代码编辑指令，拓展了 AI 编程工具的交互边界。
- 轻量级架构设计，专注于特定手柄与 AI CLI 之间的通信桥接，易于集成现有工作流。
- 链接: https://github.com/stephenleo/OpenMicro
- ⭐ 46 | 🍴 5 | 语言: TypeScript
- 标签: agenticai, ai, claude, claude-code, codex

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 46 | 🍴 2 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

### restaurant-digitalization-blueprint
- 描述: 餐饮连锁数字化 + AI 全景蓝图:原串(平价烤串连锁)的架构决策、业务口径、踩坑实录与可直接喂给 AI 的复刻指令。纯自然语言方案,不含代码与任何真实经营数据。
- 链接: https://github.com/lofty14/restaurant-digitalization-blueprint
- ⭐ 33 | 🍴 9 | 语言: 未知
- 标签: ai, ai-agents, blueprint, chinese, claude

### bbarit-agent-oss
- ### 1. 中文简介
bbarit-agent-oss 是一款基于 Rust 开发的开源终端 AI 编程代理工具，支持超过 15 家大语言模型提供商及 1000 多种模型。它提供了一个可自托管的替代方案，旨在对标 Claude Code 和 Codex 的 CLI 体验，采用 MIT 许可证开源。

### 2. 核心功能
*   **单一二进制文件部署**：仅依赖一个 Rust 编译的二进制文件，便于安装和使用。
*   **广泛的模型兼容性**：集成 15+ 家主流 LLM 提供商（如 OpenAI、Anthropic、Google Gemini 等），支持 1000+ 种模型。
*   **终端交互式编码**：在终端内提供类似 Claude Code 或 Codex 的完整 AI 辅助编程工作流。
*   **支持本地私有化部署**：兼容 Ollama 等本地模型运行环境，满足数据隐私需求。
*   **跨平台 TUI 界面**：提供现代化的终端用户界面（TUI），提升命令行交互体验。

### 3. 适用场景
*   **追求轻量级部署的用户**：希望避免复杂配置，通过单个二进制文件快速启动 AI 编程助手的开发者。
*   **多模型对比与切换场景**：需要在不同 LLM 提供商之间灵活切换，以测试代码生成效果或成本效益的团队或个人。
*   **注重数据隐私的企业/个人**：需要自托管 AI 代理并支持本地模型（如通过 Ollama）运行，以确保代码和数据不泄露到外部服务器的场景。
*   **终端重度用户**：习惯在命令行环境中工作，希望获得类似 Claude Code 的高级编码代理功能的 Rust 爱好者。

### 4. 技术亮点
*   **Rust 高性能架构**：利用 Rust 语言的内存安全和执行效率优势，构建稳定且快速的 CLI 工具。
*   **高度可扩展的提供商接口**：设计支持接入大量不同的 LLM API，具备灵活的扩展能力。
- 链接: https://github.com/bbarit/bbarit-agent-oss
- ⭐ 32 | 🍴 10 | 语言: Rust
- 标签: agentic, ai, ai-agent, anthropic, claude

### ai_resume_builder
- 描述: Code from a workshop I led - who know's what it could be with your support.
- 链接: https://github.com/camunity/ai_resume_builder
- ⭐ 25 | 🍴 61 | 语言: Jupyter Notebook

### x-post-scheduler
- 描述: 把内容变成 X 帖子的 Claude Code Skill 套件：资讯短推（AI 海报）+ 原创段子 + 长文 Article，经 Buffer / Typefully 自动发布排期
- 链接: https://github.com/cxjwin/x-post-scheduler
- ⭐ 25 | 🍴 5 | 语言: JavaScript

### uxon-ai
- 描述: UXON is an MCP server and API that lets AI agents and developers create landing pages, run A/B experiments, and track conversions across domains.
- 链接: https://github.com/alexpilotto/uxon-ai
- ⭐ 23 | 🍴 0 | 语言: 未知
- 标签: ab-testing, ai-agents, conversion-tracking, cro-api, experimentation-api

### vane
- 描述: High performance, multimodal-native engine for AI workloads.
- 链接: https://github.com/AstroVela/vane
- ⭐ 22 | 🍴 5 | 语言: Python

### memmy-agent
- 描述: One Agent. One memory. Shared by every AI. 🍙
- 链接: https://github.com/MemTensor/memmy-agent
- ⭐ 19 | 🍴 2 | 语言: TypeScript
- 标签: agent, ai, ai-agents, memory

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81852 | 🍴 15247 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35477 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3158 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21162 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18414 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17323 | 🍴 2120 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13150 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11576 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10667 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### GitHub 项目分析报告

**1. 中文简介**
该项目是一个汇集了 500 个包含完整代码的 AI 实战项目的精选仓库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它作为一份“Awesome”列表，为开发者提供了从入门到进阶的全面学习资源和实践案例。

**2. 核心功能**
*   提供涵盖机器学习、深度学习、计算机视觉和 NLP 的 500 多个实战项目代码库。
*   包含丰富的标签分类，便于用户按技术领域快速筛选和定位所需资源。
*   作为高质量的项目集合（Awesome List），降低了 AI 初学者寻找优质练手项目的门槛。
*   所有项目均附带可运行的代码，支持直接复现和深入分析算法实现。

**3. 适用场景**
*   **AI 学习者进阶**：适合希望跳出理论框架，通过实际编码掌握 ML/DL 算法的学生和自学者。
*   **面试准备**：求职者可利用这些项目构建个人作品集，展示在 CV 或 NLP 等领域的工程落地能力。
*   **快速原型开发**：研究人员或工程师可参考现有代码结构，加速特定任务（如图像分类、文本生成）的开发流程。

**4. 技术亮点**
*   **覆盖面广**：整合了当前主流 AI 子领域的经典与前沿项目，形成一站式学习资源库。
*   **高关注度**：拥有超过 35,000 颗星标，证明了其在社区中的广泛认可度和实用性。
*   **代码驱动**：强调“with code”，确保每个项目都具有极高的可操作性和参考价值，而非仅停留在概念介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35477 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款轻量级的神经网络、深度学习及机器学习模型可视化工具。它能够直观地展示模型结构，帮助用户快速理解和分析各种主流框架生成的模型文件。

### 2. 核心功能
*   **多格式支持**：兼容 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite 等主流模型格式。
*   **交互式可视化**：提供清晰的计算图视图，支持缩放、平移及节点详情查看。
*   **跨平台运行**：作为独立桌面应用或 Web 服务运行，无需安装庞大的深度学习环境。
*   **模型结构解析**：自动解析并展示网络层连接关系、权重数据及维度信息。
*   **开源免费**：完全开源，便于社区贡献和二次开发。

### 3. 适用场景
*   **模型调试与验证**：在部署前检查模型结构是否正确，识别潜在的连接错误或维度不匹配问题。
*   **教学与演示**：用于人工智能课程或技术分享中，直观展示神经网络的工作原理和数据流向。
*   **模型转换辅助**：在不同框架（如从 PyTorch 到 ONNX）迁移过程中，对比和确认模型一致性。
*   **快速原型审查**：开发人员无需编写代码即可快速浏览复杂模型的层级结构，提高沟通效率。

### 4. 技术亮点
*   **零依赖加载**：无需安装 TensorFlow 或 PyTorch 等重型库即可读取和解析模型文件，启动速度快且资源占用低。
*   **Web 架构优势**：基于 Electron 或纯 Web 技术构建，具备良好的跨平台兼容性和易于分发的特性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33237 | 🍴 3158 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心速查表（Cheat Sheets）。它旨在通过精简的参考资料，帮助研究者快速回顾关键概念、库函数及最佳实践，从而提升开发与实验效率。

**2. 核心功能**
*   涵盖机器学习与深度学习的基础理论速查指南。
*   集成主流Python科学计算库（如NumPy、SciPy、Matplotlib）的操作备忘。
*   包含深度学习框架（如Keras）的关键API与配置速记。
*   提供经过社区验证的高质量参考链接与资源汇总。

**3. 适用场景**
*   深度学习研究员在构建模型前快速查阅数学原理或算法细节。
*   数据科学家在进行数据分析时，快速调用NumPy或Matplotlib的具体函数语法。
*   机器学习初学者整理学习笔记，作为系统知识体系的辅助索引。
*   工程师在调试代码时，快速确认Keras或其他框架的参数用法。

**4. 技术亮点**
*   高度聚合了AI领域最常用工具链的关键知识点，实现“一站式”查阅。
*   内容源自Medium等权威技术社区，保证了信息的准确性与时效性。
*   结构清晰，专注于“速查”而非长篇教程，极大降低了检索成本。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3385 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13150 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9138 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8931 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6988 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6258 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81852 | 🍴 15247 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73342 | 🍴 8953 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 描述: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58479 | 🍴 9565 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52389 | 🍴 10608 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战及深度学习框架（PyTorch、TensorFlow 2）的综合学习资源库。项目内容还深入讲解了线性代数基础与自然语言处理工具（NLTK），旨在为学习者提供从理论到实践的全方位指导。

### 2. **核心功能**
*   **算法实战**：包含 Adaboost、Apriori、K-Means、SVM、朴素贝叶斯等经典机器学习算法的代码实现与解析。
*   **深度学习框架**：提供基于 PyTorch 和 TensorFlow 2 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）等模型实战。
*   **NLP 与自然语言处理**：利用 NLTK 进行文本处理，涵盖推荐系统、分类回归等 NLP 相关任务。
*   **数学基础强化**：结合线性代数知识，辅助理解 PCA、SVD 等降维与矩阵运算在机器学习中的应用。

### 3. **适用场景**
*   **机器学习入门者**：通过分类、聚类、回归等基础算法代码快速建立对 ML 流程的理解。
*   **深度学习研究者**：参考 PyTorch 和 TF2 的具体实现案例，优化 DNN、LSTM 等复杂模型的构建。
*   **数据科学从业者**：利用项目中的推荐系统和 NLP 实战技巧，解决实际业务中的数据挖掘问题。

### 4. **技术亮点**
*   **全栈覆盖**：整合了从传统统计学习（如 Logistic 回归）到前沿深度学习（如 LSTM）的完整技术栈。
*   **理论与实践结合**：不仅提供代码，还强调线性代数等数学原理在算法背后的支撑作用。
*   **多框架支持**：同时支持 Scikit-learn、PyTorch 和 TensorFlow 2，适应不同技术偏好和项目需求。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42385 | 🍴 11538 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38651 | 🍴 6480 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35477 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33747 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28629 | 🍴 3494 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25922 | 🍴 2928 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. **中文简介**
该项目是一个精选的500个AI机器学习、深度学习、计算机视觉和自然语言处理项目合集，均附带源代码。它涵盖了从基础算法到前沿应用的广泛领域，为开发者提供了丰富的实践案例。该仓库旨在帮助学习者通过实际代码快速掌握人工智能核心技术。

### 2. **核心功能**
*   提供500多个包含完整代码的AI相关项目实例，覆盖主流技术栈。
*   分类清晰，集成机器学习、深度学习、计算机视觉及NLP四大核心领域。
*   作为“Awesome”列表， curated 了高质量且具代表性的开源项目供参考。
*   支持Python等语言实现，便于开发者直接运行和修改代码。

### 3. **适用场景**
*   **初学者入门学习**：通过阅读和运行现成代码，快速理解AI基本概念与实现逻辑。
*   **项目灵感参考**：当需要开发AI应用但缺乏思路时，从中寻找可复用的项目模板。
*   **技能提升与实践**：深入学习特定领域（如图像识别或文本分析）的高级应用案例。

### 4. **技术亮点**
*   **高关注度与社区认可**：拥有35,477颗星标，证明其在AI学习资源中的极高价值和广泛影响力。
*   **全面的技术覆盖**：标签涵盖从基础机器学习到前沿深度学习的完整技术图谱。
*   **代码即文档**：强调“with code”，确保每个概念都有可执行的代码示例，而非纯理论介绍。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35477 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的复杂工作流。它利用先进的 AI 模型来理解网页界面并模拟用户操作，从而替代传统的脚本化浏览器自动化方案。该项目旨在通过智能化的方式提升 RPA（机器人流程自动化）的效率与适应性。

**2. 核心功能**
*   **AI 驱动的操作决策**：利用大型语言模型和计算机视觉技术，智能识别网页元素并决定操作步骤，而非依赖固定的 CSS 选择器。
*   **跨框架兼容性**：底层支持 Playwright、Puppeteer 和 Selenium 等多种主流浏览器自动化引擎，提供灵活的技术栈选择。
*   **可视化工作流构建**：允许用户通过定义任务目标，由 AI 自动生成并执行一系列浏览器交互动作，简化了自动化流程的开发难度。
*   **动态页面适应能力**：能够应对前端界面频繁变动或动态加载的场景，保持自动化任务的稳定性，减少因 UI 变更导致的脚本失效。

**3. 适用场景**
*   **企业级 RPA 自动化**：用于自动化处理需要登录多个系统、填写表单或从网页抓取数据的重复性后台业务操作。
*   **Web 数据提取与分析**：针对结构不固定或反爬机制较强的网站，高效提取所需信息并转化为结构化数据。
*   **QA 测试自动化**：在软件开发生命周期中，自动执行端到端的功能测试，验证不同浏览器环境下的用户交互逻辑。

**4. 技术亮点**
*   **多模态 AI 集成**：结合了 LLM（大语言模型）的逻辑推理能力与 Vision（视觉感知）能力，实现了对非结构化网页内容的精准理解。
*   **API 优先设计**：提供清晰的 API 接口，便于开发者将其嵌入到现有的自动化平台或 CI/CD 管道中，扩展性强。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22459 | 🍴 2097 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16319 | 🍴 3765 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12916 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11279 | 🍴 1203 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3457 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3286 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款完全由用户掌控的个人 AI 助手，支持跨操作系统和平台运行，让用户以“龙虾模式”轻松实现数据私有化。它旨在提供灵活、开放的 AI 体验，确保用户对自己的数据和交互拥有最高控制权。

**2. 核心功能**
- 支持任意操作系统和平台的广泛兼容性部署。
- 强调数据所有权与隐私保护，实现真正的本地化或个人化控制。
- 作为通用个人 AI 助手，具备高度的可定制性和扩展性。
- 采用 TypeScript 开发，确保代码的健壮性与类型安全。
- 提供独特的品牌标识（龙虾/甲壳类动物主题），增强用户辨识度。

**3. 适用场景**
- 追求数据隐私和个人 AI 主权的开发者及技术爱好者。
- 需要在不同操作系统间无缝切换并统一 AI 助手的个人用户。
- 希望构建定制化、非云依赖的个人效率工具的高级用户。
- 对现有主流 AI 助手数据政策持保留态度的隐私敏感人群。

**4. 技术亮点**
- 基于 TypeScript 构建，利于现代前端及全栈生态集成。
- 架构设计强调“Own Your Data”，从底层保障用户数据不外泄。
- 极高的跨平台兼容性，打破了传统 AI 助手对特定硬件或 OS 的限制。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383216 | 🍴 80494 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 256254 | 🍴 22815 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 216175 | 🍴 40425 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个采用公平代码许可的工作流自动化平台，原生集成 AI 能力并支持 400 多种集成。它结合了可视化构建与自定义代码功能，允许用户选择自托管或云端部署，灵活满足各类自动化需求。

2. **核心功能**
*   提供可视化的工作流构建界面，同时支持通过自定义代码扩展逻辑。
*   内置原生 AI 功能，能够无缝结合大语言模型与其他数据源。
*   拥有超过 400 种预置集成，支持广泛的 API 连接和数据交互。
*   具备 MCP（模型上下文协议）客户端与服务端支持，增强 AI 交互能力。
*   支持自托管和云端两种部署模式，确保数据隐私与灵活性。

3. **适用场景**
*   企业级数据同步：自动在不同 SaaS 应用（如 CRM、ERP）之间同步和转换数据。
*   AI 驱动的业务流程：利用 LLM 自动处理文档摘要、客户支持回复或内容生成任务。
*   开发者自动化：通过脚本和 API 调用实现复杂的 CI/CD 流水线或后端服务编排。

4. **技术亮点**
*   基于 TypeScript 开发，类型安全且易于维护，适合开发者深度定制。
*   率先在低代码平台中引入 MCP 协议支持，提升了与 AI 代理集成的标准化程度。
*   公平代码许可证（Fair-code license）平衡了开源社区的贡献与商业使用的可持续性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196760 | 🍴 59392 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185585 | 🍴 46078 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165879 | 🍴 21455 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164190 | 🍴 30420 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157087 | 🍴 46174 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 152171 | 🍴 8690 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151933 | 🍴 9584 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

