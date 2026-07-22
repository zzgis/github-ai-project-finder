# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- ### 1. 中文简介
Thinking Orbs 是一套专为 AI 及智能体用户界面设计的点状加载指示器组件，提供六种精心调优的状态以模拟思考过程。它支持两种尺寸并具备自动适配深色/浅色模式的功能，旨在提升人机交互时的视觉体验与反馈清晰度。

### 2. 核心功能
- 提供六种经过微调的动画状态，直观表现“思考”或“处理中”的逻辑。
- 内置深色模式与浅色模式的自动切换能力，无需手动配置主题。
- 支持两种不同尺寸规格，灵活适配各种 UI 布局需求。
- 基于 TypeScript 构建，确保类型安全且易于集成到现代前端框架中。

### 3. 适用场景
- 生成式 AI 聊天机器人或对话式智能体的响应等待阶段。
- 复杂数据查询、模型推理或后台任务处理时的用户界面反馈。
- 需要区分不同处理状态（如搜索、计算、生成）的智能应用界面。

### 4. 技术亮点
- 利用 CSS 动画与 TypeScript 结合，实现轻量级且高性能的交互动画。
- 自动主题感知设计，简化了多主题应用的开发复杂度。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 164 | 🍴 8 | 语言: TypeScript

### BossConsole
- ### 1. 中文简介
BossConsole 是一款开源、跨平台的 AI 智能体操作控制台，专为 JVM 环境构建（而非 Electron），支持多线程运行。它集成了真实浏览器、终端、编辑器及 100 多种 MCP 工具，旨在为 Claude Code、Codex、Gemini 等主流 AI 模型提供统一的企业管理级操作界面。

### 2. 核心功能
*   **原生 JVM 架构**：基于 Kotlin Multiplatform 和 Compose 开发，提供比 Electron 更轻量的原生桌面体验。
*   **多模型兼容**：统一支持 Claude Code、Codex、Gemini 及 OpenCode 等多种 AI 智能体后端。
*   **全栈集成环境**：内置真实浏览器渲染引擎、交互式终端和代码编辑器，实现一站式开发工作流。
*   **MCP 协议支持**：原生集成 Model Context Protocol (MCP)，支持加载 100+ 种工具以扩展 AI 能力。
*   **企业级安全管控**：提供密钥管理和基于角色的访问控制 (RBAC)，满足科研与企业级安全需求。

### 3. 适用场景
*   **企业级 AI 开发平台**：需要统一管控多个 AI 模型权限、密钥及操作日志的企业研发团队。
*   **复杂科研实验环境**：研究人员需要在受控的多线程环境中同时运行多个 AI Agent 进行并行数据分析或模拟。
*   **高级开发者工作流优化**：希望在一个界面内无缝切换浏览器调试、终端命令执行和代码编辑的高效开发者。

### 4. 技术亮点
*   **热重载与多平台支持**：利用 Kotlin Multiplatform 实现代码复用，并具备热重载特性以提升开发效率。
*   **非 Electron 原生体验**：摆脱 Web 技术栈束缚，提供更接近原生应用的性能和系统资源管理能力。
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 31 | 🍴 1 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### AIGuardSIEM
- 由于该项目在GitHub上的描述字段为空（"None"），且缺乏详细的文档或代码结构信息，无法直接提取具体的功能细节。基于项目名称 **AIGuardSIEM** 及编程语言 **C++**，以下是基于命名惯例和技术栈的推测性分析：

1. **中文简介**
   AIGuardSIEM 是一个基于 C++ 开发的安全信息与事件管理系统（SIEM）。该项目旨在利用高性能底层语言提供实时威胁检测与安全日志分析能力。其名称暗示了可能结合了人工智能（AI）技术以增强对新型攻击的防御。

2. **核心功能**
   *   提供基于 C++ 的高性能实时日志收集与处理引擎。
   *   集成安全事件关联分析，用于快速识别潜在威胁。
   *   支持自定义规则或 AI 模型以检测异常行为模式。
   *   实现可视化的安全态势感知仪表盘。

3. **适用场景**
   *   需要低延迟和高吞吐量日志处理的大型企业网络安全中心。
   *   部署在资源受限环境中，要求极致性能的安全监控节点。
   *   结合机器学习算法进行高级持续性威胁（APT）检测的研究或生产环境。

4. **技术亮点**
   *   采用 C++ 编写，具备极高的运行效率和内存管理能力。
   *   可能针对实时数据流进行了优化，适合高频安全事件处理。

*注：由于缺少官方文档，以上分析基于项目名称和常见技术实践推断。建议查阅该项目的源代码或 README 文件以获取准确的功能说明。*
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 28 | 🍴 2 | 语言: C++

### style-pack-skill
- 1. **中文简介**
该项目是一个AI Agent技能包，能够从参考图像中提取视觉风格的“DNA”特征。它强制AI生成包含详细标注和纯色块两种版本的标准化色卡，实现风格的一致性复用。

2. **核心功能**
*   自动解析参考图中的色彩、材质及光影等关键视觉元素。
*   生成带有详细参数标注的专业级设计色卡。
*   输出用于快速识别或程序调用的纯色彩块版本。
*   确保不同生成结果间视觉风格的高度统一性。
*   作为Agent技能无缝集成到自动化工作流中。

3. **适用场景**
*   UI/UX设计中批量提取并复用特定界面的配色方案。
*   品牌视觉识别系统（VI）的快速延展与标准化落地。
*   电商详情页或广告素材的风格化批量生成。
*   游戏美术资源中的色调管理与风格一致性控制。

4. **技术亮点**
*   采用“视觉DNA”概念量化抽象的风格特征，提升复现精度。
*   双版色卡输出机制兼顾了人类设计师的标注需求与机器的读取效率。
- 链接: https://github.com/irenerachel/style-pack-skill
- ⭐ 25 | 🍴 4 | 语言: Python

### pgContext
- 描述: A full AI search engine, built into Postgres.
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 17 | 🍴 1 | 语言: Rust

### etf-quant-research-system
- 描述: A multi-timescale ETF forecasting and virtual trading system for AI and robotics ETFs.
- 链接: https://github.com/yingfanxu/etf-quant-research-system
- ⭐ 15 | 🍴 0 | 语言: Python

### pm-manager
- 描述: Know what to fix next — local .pm governance skill pack for AI coding agents (Spec Kit–inspired).
- 链接: https://github.com/wei63w/pm-manager
- ⭐ 15 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude-code, cursor, project-management

### seo-geo-audit
- 描述: Agent Skill: audit a site for technical SEO and AI-answer-engine discoverability (GEO). 44 evidence-bearing checks, one table.
- 链接: https://github.com/zeebees/seo-geo-audit
- ⭐ 14 | 🍴 1 | 语言: 未知

### Auto-sign-up-grok-dezz
- 描述: Automated Grok (x.ai) Account Registration + 9Router Integration
- 链接: https://github.com/dzDev37/Auto-sign-up-grok-dezz
- ⭐ 12 | 🍴 2 | 语言: Python

### moonlit-myriad
- 描述: 专为 AI 玩家设计的单文件卡牌肉鸽 🌙
- 链接: https://github.com/xinwithyu/moonlit-myriad
- ⭐ 10 | 🍴 1 | 语言: Python
- 标签: ai, balatro, card-game, llm, python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81943 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35603 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33251 | 🍴 3163 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21188 | 🍴 3972 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18444 | 🍴 1177 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17330 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13165 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11585 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10673 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35603 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地理解模型结构和数据流向。

2. **核心功能**
*   支持广泛的后端格式，包括 TensorFlow、PyTorch、ONNX、Keras 和 CoreML 等。
*   提供清晰的层级视图，展示网络层结构、参数形状及张量维度。
*   允许用户交互式探索模型细节，如查看特定层的输入输出特征图。
*   具备模型比较功能，便于分析不同版本或架构之间的差异。
*   轻量级且跨平台，无需安装复杂环境即可在浏览器或桌面端运行。

3. **适用场景**
*   研究人员调试深度学习模型结构，快速定位潜在的错误或冗余层。
*   开发者检查模型转换（如从 PyTorch 到 ONNX）过程中的数据一致性。
*   非技术人员向团队或客户展示 AI 模型的工作原理和内部逻辑。
*   教育场景中用于教学神经网络各层的功能及其相互连接关系。

4. **技术亮点**
*   极高的兼容性，几乎覆盖了目前所有主流的深度学习框架和导出格式。
*   基于 Web 技术构建，实现了无需本地依赖的即用型体验。
*   开源社区活跃，持续更新以支持最新发布的模型架构和框架特性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33251 | 🍴 3163 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目汇集了深度学习与机器学习研究者必备的核心速查表（Cheat Sheets），内容涵盖从基础数学库到主流框架的关键概念与代码片段。它旨在为研究人员和开发者提供一个快速回顾知识点、解决常见编程问题的权威参考指南。

### 2. 核心功能
*   提供针对 NumPy、SciPy 和 Matplotlib 等核心数据科学库的快速语法参考。
*   包含 Keras 等深度学习框架的关键 API 使用示例与配置技巧。
*   整理机器学习算法的基础理论摘要与关键参数说明。
*   汇总深度学习研究中常用的数学公式与概念定义。
*   以结构化的 PDF 或文档形式呈现，便于离线查阅与打印。

### 3. 适用场景
*   **面试准备**：帮助求职者快速复习机器学习核心概念与框架用法，应对技术面试。
*   **日常开发辅助**：在编写代码时作为即时参考，避免因遗忘特定函数参数而中断思路。
*   **新人入门指引**：为刚接触该领域的学生或研究者提供系统性的知识概览与速记手册。
*   **团队知识共享**：作为内部培训资料，统一团队成员对常用库和框架的使用规范。

### 4. 技术亮点
*   **高度浓缩**：将复杂的技术栈提炼为单页或少数几页的精炼图表，极大提升查阅效率。
*   **视觉化呈现**：大量使用流程图、表格和代码块，直观展示逻辑关系与代码结构。
*   **社区驱动更新**：依托 Medium 文章链接及 GitHub 社区贡献，保持内容的时效性与准确性。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份 comprehensive 的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并实现就业实战。内容涵盖 Python、机器学习、深度学习、计算机视觉及自然语言处理等热门技术领域。

### 2. 核心功能
*   提供结构化的 AI 学习路径，涵盖从数学基础到高级算法的全栈知识体系。
*   收录近 200 个经过筛选的实战案例与开源项目，强化动手实践能力。
*   配套提供免费的学习教材和资源，降低初学者入门门槛。
*   聚焦就业导向，通过实际项目经验提升求职竞争力。

### 3. 适用场景
*   **零基础转行**：希望进入人工智能领域但缺乏系统知识的初学者。
*   **学生课程设计**：需要参考高质量实战项目来完成作业或毕业设计的计算机相关专业学生。
*   **技能查漏补缺**：已有一定基础，希望系统化梳理机器学习或深度学习知识体系的技术人员。
*   **求职准备**：正在寻找 AI 相关岗位，需要通过实战项目丰富简历的求职者。

### 4. 技术亮点
*   **资源聚合**：集中整合了 TensorFlow、PyTorch、Keras、Caffe 等主流框架的学习资料。
*   **实战驱动**：强调“做中学”，通过大量现成案例替代纯理论阅读，加速技能掌握。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13165 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9141 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8933 | 🍴 3103 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6993 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6269 | 🍴 749 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81943 | 🍴 15249 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目荣获 ACL 2024 会议认可，旨在简化从指令微调到强化学习的完整训练流程。它集成了多种先进的量化与参数高效微调技术，显著降低了大模型定制开发的门槛。

2. **核心功能**
- 支持 100+ 种主流 LLM 和 VLM 的统一接口微调，无需修改底层代码。
- 集成 QLoRA、LoRA、RLHF 等多种参数高效微调及强化学习算法。
- 内置多种量化方案（如 bitsandbytes），实现低资源消耗下的高性能推理与训练。
- 提供标准化的数据处理与训练流水线，兼容 Hugging Face Transformers 生态。

3. **适用场景**
- 开发者需要对特定领域数据（如医疗、法律）进行指令微调以定制化模型能力。
- 研究人员希望在有限 GPU 资源下，对大型多模态或混合专家模型（MoE）进行高效实验。
- 企业希望快速部署基于最新开源模型（如 Llama 3、Qwen、DeepSeek）的业务应用。

4. **技术亮点**
- 极高的兼容性：无缝支持包括 Llama 3、Qwen、Gemma、DeepSeek 在内的众多前沿模型架构。
- 资源优化卓越：通过 QLORA 等技术，在单张消费级显卡上即可微调超大参数模型。
- 端到端解决方案：涵盖从数据预处理、监督微调到 RLHF 对齐的全生命周期管理。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73427 | 🍴 8964 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52540 | 🍴 10636 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42399 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入掌握人工智能的核心原理与实践。它强调“学习、构建并部署”的完整流程，帮助开发者将AI能力转化为实际可用的产品。适合希望彻底理解底层机制并具备工程落地能力的技术人员。

2. **核心功能**
- 提供从基础理论到高级应用的端到端AI工程教程与课程资源。
- 涵盖大语言模型（LLM）、生成式AI及智能体（Agents）的开发与集成。
- 支持多语言环境，包含Python和Rust等高性能编程语言的实现案例。
- 深入讲解计算机视觉、自然语言处理及强化学习等关键领域技术。
- 指导如何将AI模型部署为可交付的服务或产品供他人使用。

3. **适用场景**
- AI初学者希望系统性地从底层构建并理解机器学习与深度学习模型。
- 工程师需要开发基于LLM的智能代理或复杂的多智能体协作系统。
- 企业团队寻求将生成式AI技术整合到现有业务流中以实现产品化。
- 研究者探索结合Rust等语言优化AI推理性能及边缘计算部署。

4. **技术亮点**
- 采用“从零构建”教学法，强化对Transformer架构及底层算法的理解。
- 融合前沿技术栈，如Model Context Protocol (MCP) 和多智能体 Swarm 智能。
- 跨语言支持（Python/Rust/TypeScript），兼顾开发效率与执行性能。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 41466 | 🍴 6893 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35603 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33759 | 🍴 4696 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28754 | 🍴 3512 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25972 | 🍴 2945 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21731 | 🍴 3306 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35603 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22542 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16351 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级可解释性AI工具包，旨在增强模型决策的透明度。它广泛支持CNN、Vision Transformer等架构，并涵盖分类、检测、分割及图像相似度等多种任务。

2. **核心功能**
- 全面支持多种主流深度学习架构，包括CNN和Vision Transformer。
- 兼容多种计算机视觉任务，如图像分类、目标检测和语义分割。
- 集成多种可视化算法，如Grad-CAM、Score-CAM和类激活映射（CAM）。
- 提供直观的可视化效果，帮助用户深入理解模型的内部关注点。

3. **适用场景**
- 调试深度学习模型，定位导致错误分类的具体图像区域。
- 向非技术人员或利益相关者展示AI决策依据，提升信任度。
- 在医疗影像或自动驾驶等高风险领域进行模型安全与合规性审查。
- 学术研究，用于分析和对比不同网络结构的可解释性特征。

4. **技术亮点**
- 拥有超过1.2万星的极高社区认可度，表明其稳定性和广泛实用性。
- 标签体系完善，覆盖了从底层算法到上层应用（XAI、Interpretability）的全链路需求。
- 不仅限于经典的Grad-CAM，还整合了Score-CAM等前沿改进算法，提供了更丰富的选择。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1205 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3293 | 🍴 404 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2630 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2429 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383723 | 🍴 80633 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架及软件开发方法论。它通过以子代理驱动开发的方式，为软件开发生命周期（SDLC）提供了一套切实可行的智能化解决方案。该项目旨在利用 AI 智能体提升编码、头脑风暴等核心技能的执行效率。

2. **核心功能**
*   提供以子代理驱动开发（Subagent-Driven Development）的工作流。
*   构建模块化的智能体技能框架，支持灵活的技能组合与调用。
*   覆盖完整的软件开发生命周期（SDLC），从规划到编码自动化。
*   集成 AI 辅助的头脑风暴与代码生成能力，提升开发效率。
*   强调“可落地”的方法论，确保 AI 在真实开发场景中有效工作。

3. **适用场景**
*   希望引入 AI 智能体优化现有软件开发流程的团队。
*   需要自动化处理复杂编码任务或进行大规模代码重构的项目。
*   探索基于子代理协作模式的新型软件工程实践的研究者。
*   寻求高效 AI 辅助头脑风暴与设计讨论工具的开发者。

4. **技术亮点**
*   采用 Shell 脚本实现轻量级且易于集成的框架基础。
*   独特的“技能”抽象层设计，使智能体行为可复用且标准化。
*   强调方法论的实际有效性而非纯理论，拥有较高的社区关注度（近 26 万星标）。
- 链接: https://github.com/obra/superpowers
- ⭐ 258763 | 🍴 23065 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218390 | 🍴 41299 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一款支持自托管或云端部署的公平源码工作流自动化平台，具备原生 AI 能力并集成 400 多种应用。它结合了可视化构建与自定义代码开发模式，为低代码/无代码用户提供了强大的集成框架。

### 2. 核心功能
*   **可视化与代码混合开发**：允许用户通过拖拽组件构建流程，同时也支持编写自定义代码以满足复杂逻辑需求。
*   **丰富的集成生态**：内置超过 400 种第三方应用集成，支持广泛的 API 连接和数据流转。
*   **原生 AI 能力**：平台自带人工智能功能，可轻松将 AI 模型融入自动化工作流中。
*   **灵活的部署选项**：支持自托管（Self-hosted）以保障数据隐私，也提供便捷的云端服务。
*   **MCP 协议支持**：集成模型上下文协议（MCP），增强了与大语言模型及外部数据源的交互能力。

### 3. 适用场景
*   **企业级自动化办公**：连接 CRM、邮件、日历等工具，自动处理数据同步和任务提醒。
*   **AI 驱动的业务流程**：利用原生 AI 功能自动化内容生成、数据分析或客户响应流程。
*   **数据管道与 ETL**：在不同数据库和 SaaS 平台之间建立可靠的数据提取、转换和加载工作流。

### 4. 技术亮点
*   **公平源码许可（Fair-code）**：在保持开放协作的同时，对商业再分发进行限制，平衡社区发展与可持续运营。
*   **TypeScript 全栈构建**：基于 TypeScript 开发，确保代码类型安全和良好的可维护性。
*   **MCP Client/Server 架构**：原生支持 MCP 协议，使其成为连接现代 AI 代理与外部数据源的强大枢纽。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197379 | 🍴 59521 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185641 | 🍴 46066 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166160 | 🍴 21474 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164284 | 🍴 30429 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157185 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154047 | 🍴 8786 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152177 | 🍴 9619 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

