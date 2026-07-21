# GitHub AI项目每日发现报告
日期: 2026-07-21

## 新发布的AI项目

### nativ
- 1. **中文简介**
Nativ 是一款专为 macOS 设计的原生 AI 应用，旨在让用户在本地高效运行和管理 MLX 模型。它集成了聊天交互、服务部署、性能监控及模型连接等功能，提供了统一且便捷的使用体验。

2. **核心功能**
*   **本地推理**：在 Mac 设备上直接运行 MLX 模型，无需依赖外部服务器。
*   **交互式对话**：内置聊天界面，方便用户与本地 AI 模型进行即时交互。
*   **服务部署**：支持将本地模型作为服务运行，便于其他应用调用。
*   **实时监控**：提供可视化的监控工具，帮助用户追踪模型运行状态和资源使用情况。

3. **适用场景**
*   **隐私敏感型开发**：需要在不上传数据的前提下，在本地安全测试和调试 MLX 模型的开发人员。
*   **离线 AI 助手**：希望在没有网络连接的环境中，利用 Mac 算力随时使用本地大语言助手的普通用户。
*   **原型快速验证**：需要快速搭建本地 AI 服务原型，以验证模型性能或集成流程的技术团队。

4. **技术亮点**
*   **原生 macOS 体验**：使用 Swift 开发，深度集成 macOS 系统特性，提供流畅且符合苹果设计规范的用户界面。
*   **MLX 框架支持**：专为 Apple Silicon 优化的 MLX 框架支持，充分发挥 M 系列芯片的硬件加速能力。
- 链接: https://github.com/Blaizzy/nativ
- ⭐ 362 | 🍴 23 | 语言: Swift

### open-kritt
- 描述: Orchestrate AI agents to find real vulnerabilities in code.
- 链接: https://github.com/Kritt-ai/open-kritt
- ⭐ 106 | 🍴 26 | 语言: JavaScript
- 标签: agent, agents, ai, bug-bounty, bugbounty

### agents-council
- ### 1. 中文简介
`agents-council` 是一款专为 Claude Code 设计的插件，旨在实现多智能体协作。它通过编排 Codex CLI、Gemini CLI 等多种 AI 工具，引入多元化的视角来辅助代码开发与分析。

### 2. 核心功能
*   支持在 Claude Code 环境中集成并调用多个外部 AI CLI 工具。
*   实现不同 AI 模型间的协同工作，提供多维度的代码视角。
*   作为 Claude Code 的技能插件运行，无缝扩展原生功能。
*   允许用户根据需求灵活组合不同的 AI 代理以解决复杂问题。

### 3. 适用场景
*   需要对比不同 AI 模型对同一代码库的分析结果时。
*   利用多个专业领域 AI 代理进行复杂的架构设计或代码重构。
*   希望借助多样化视角来发现潜在 bug 或优化代码结构时。

### 4. 技术亮点
*   采用插件化架构，轻量级集成于 Claude Code 生态。
*   兼容多种主流 AI CLI 工具（如 Codex, Gemini），打破单一模型局限。
- 链接: https://github.com/0xwilliamortiz/agents-council
- ⭐ 90 | 🍴 1 | 语言: JavaScript
- 标签: claude, claude-ai, claude-code, claude-code-skills, claude-plugin

### stem-illustration-skill
- ### 1. **中文简介**
这是一个专为 STEM（科学、技术、工程、数学）领域设计的 AI 图像生成技能工具。它能够自动生成科研示意图、教学插图及技术架构图等概念性图像，全面覆盖生物医学、化学、物理、工程等六大核心学科。该项目提供多种专业模板和风格变体，旨在提升学术可视化内容的生产效率。

### 2. **核心功能**
- **多场景模板支持**：内置信号通路、实验流程、细胞结构、质粒图等 24 种专业场景模板。
- **六大学科全覆盖**：适配生命科学、医学、化学、物理、工程及数学领域的特定视觉需求。
- **多样化风格渲染**：提供学术、教科书、信息图和 3D 渲染四种不同的视觉风格选项。
- **自动化概念生成**：专注于生成科研与教学所需的高精度概念性图像，减少手动绘图成本。

### 3. **适用场景**
- **学术论文撰写**：快速生成符合出版标准的机制图、数据流程图或结构式示意图。
- **课堂教学材料制作**：为教材或课件生成清晰的 3D 渲染图或信息图表，辅助学生理解复杂概念。
- **科研项目汇报**：制作直观的技术架构图或实验流程海报，提升演示文稿的专业度。

### 4. **技术亮点**
- **垂直领域专业化**：针对 STEM 学科特有的符号体系和视觉规范进行了深度优化，通用 AI 难以替代其专业性。
- **结构化提示词引擎**：通过预设的 24 个场景模板，将复杂的科研概念转化为标准化的 AI 生成指令，确保输出的一致性。
- 链接: https://github.com/liangdabiao/stem-illustration-skill
- ⭐ 39 | 🍴 0 | 语言: Python
- 标签: skill

### LLM-WIKI
- **1. 中文简介**
LLM-WIKI 是一个基于大语言模型构建的动态知识库，具备自我迭代与生长能力。它利用 JavaScript 开发，旨在通过自动化机制不断扩充和完善知识体系。该项目适合希望构建智能、自适应知识管理系统的开发者参考。

**2. 核心功能**
*   **自我生长机制**：能够根据新输入或上下文自动生成并整合新知识条目。
*   **大模型集成**：深度结合 LLM 能力，实现自然语言理解与知识结构化处理。
*   **动态知识库维护**：支持对已有知识进行更新、修正及关联关系的自动梳理。
*   **JavaScript 驱动**：基于 JS 生态构建，便于在 Node.js 环境或前端应用中快速部署与扩展。

**3. 适用场景**
*   **企业智能文档中心**：用于自动整理和维护公司内部不断变化的技术文档或业务规范。
*   **个人知识管理系统**：帮助研究人员或学习者自动归档笔记，并形成相互关联的知识网络。
*   **垂直领域问答引擎**：构建针对特定行业（如法律、医疗）的动态专业知识库，提升检索准确性。

**4. 技术亮点**
*   **自进化架构**：突破了传统静态知识库的限制，实现了知识的自动化增量更新。
*   **轻量级实现**：作为小型开源项目（24 星），代码结构简洁，易于理解和二次开发。
- 链接: https://github.com/loonggg/LLM-WIKI
- ⭐ 24 | 🍴 2 | 语言: JavaScript

### VibeGamer
- 描述: 用 AI Agent 自动游玩《Turmoil》（石油大亨）并不断积累经验进化的实验项目. 
- 链接: https://github.com/karminski/VibeGamer
- ⭐ 23 | 🍴 2 | 语言: TypeScript

### aipay-protocol
- 描述: Verifier-backed USDC escrow for AI agents: signed orders, evidence hashes, Polygon deposits, and deterministic settlement.
- 链接: https://github.com/AIPAYagent/aipay-protocol
- ⭐ 21 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, aipay, eip712, escrow, mcp

### idea-universe
- 描述: A research-aware AI brainstorming prompt that turns raw thoughts into structured possibilities, personal connections, and unexplored directions.
- 链接: https://github.com/dusk-futile/idea-universe
- ⭐ 18 | 🍴 0 | 语言: 未知

### ai-knowledge-rag-langchain
- 描述: 无描述
- 链接: https://github.com/HealerCodeLabs/ai-knowledge-rag-langchain
- ⭐ 17 | 🍴 0 | 语言: Python

### ai-semantic-search-api
- 描述: 无描述
- 链接: https://github.com/HealerCodeLabs/ai-semantic-search-api
- ⭐ 17 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81934 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35593 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33250 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 基于您提供的GitHub项目信息，以下是关于 **ONNX** 的技术分析：

1. **中文简介**
   ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，允许模型在不同平台间无缝迁移和部署。通过标准化表示，开发者可以更高效地跨环境运行和交换神经网络模型。

2. **核心功能**
   *   提供统一的模型格式，支持PyTorch、TensorFlow、Keras等主流框架间的模型转换。
   *   实现跨平台推理优化，确保模型在CPU、GPU及嵌入式设备上的高效执行。
   *   促进生态系统互操作性，简化从训练到生产部署的工作流集成。

3. **适用场景**
   *   需要将PyTorch或TensorFlow训练的模型部署到不支持原生框架的生产环境中。
   *   在边缘设备或移动应用中进行高性能、低延迟的深度学习推理。
   *   希望在不同硬件加速器（如NVIDIA TensorRT、Intel OpenVINO）间灵活切换以提升性能。

4. **技术亮点**
   *   作为行业通用的中间表示（IR），有效解决了深度学习框架碎片化导致的兼容性问题。
- 链接: https://github.com/onnx/onnx
- ⭐ 21181 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
该项目是一部关于机器学习工程实践的开源“开放书籍”，旨在系统性地分享从底层基础设施到上层应用的最佳实践。内容涵盖大规模模型训练、推理优化及 MLOps 运维等关键领域，为开发者提供全面的技术指导。

2. **核心功能**
- 提供大规模语言模型（LLM）的训练与微调工程指南。
- 详解 GPU 集群管理、Slurm 调度系统及网络存储优化策略。
- 深入解析 PyTorch 分布式训练、推理加速及模型调试技巧。
- 分享可扩展的 MLOps 工作流设计与生产环境部署方案。

3. **适用场景**
- 构建和训练大型深度学习模型时的基础设施规划与调优。
- 在高性能计算集群中部署和管理分布式机器学习任务。
- 优化大语言模型在生产环境中的推理延迟与吞吐量。
- 学习先进的机器学习工程实践以提升团队研发效率。

4. **技术亮点**
聚焦于实际工程落地中的性能瓶颈解决，特别是针对 LLM 时代的硬件资源利用率和分布式训练稳定性提供了极具价值的实操经验。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18437 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17329 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13163 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11583 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10673 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35593 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 基于您提供的 GitHub 项目信息，以下是关于 **Netron** 的技术分析报告：

1. **中文简介**
   Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架格式，帮助用户直观地查看和调试模型结构。通过简洁的界面，开发者可以清晰地理解复杂模型的内部逻辑与数据流向。

2. **核心功能**
   - 广泛支持 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 及 Safetensors 等主流模型格式。
   - 提供直观的图形化界面，展示网络层结构、张量形状及权重分布。
   - 支持交互式操作，允许用户点击特定节点查看详细属性或展开子图结构。
   - 具备模型验证功能，能够检测模型结构中的潜在错误或不一致性。

3. **适用场景**
   - **模型调试**：在部署前检查模型结构是否符合预期，定位层连接错误。
   - **学术交流与展示**：快速生成高质量的网络架构图，用于论文插图或技术报告。
   - **跨平台迁移**：在转换不同框架（如从 PyTorch 到 ONNX）时，验证模型一致性。
   - **新手学习**：帮助初学者直观理解复杂深度学习模型的数据流和参数配置。

4. **技术亮点**
   - **轻量级与跨平台**：基于 JavaScript 开发，可作为独立桌面应用运行，也可嵌入 Web 页面，无需安装大型依赖环境。
   - **开源免费**：完全开源且免费使用，社区活跃，持续更新以支持最新的模型格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33250 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13163 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大型语言模型（LLM）、神经网络及其他人工智能模型。它通过简化复杂的机器学习流程，让开发者能够专注于数据与业务逻辑，而非底层代码实现。

2. **核心功能**
*   提供声明式配置界面，支持以低代码方式快速搭建多种类型的 AI 模型。
*   内置对主流深度学习框架（如 PyTorch）的支持，兼容广泛的算法架构。
*   涵盖从数据处理、模型训练到评估和部署的完整机器学习生命周期。
*   支持微调（Fine-tuning）现有大型语言模型，以适应特定领域的需求。
*   具备强大的数据集中处理能力，优化模型输入的质量与效率。

3. **适用场景**
*   希望快速原型化验证 AI 想法，但不愿编写大量底层深度学习代码的数据科学家。
*   需要对现有开源大模型（如 Llama、Mistral）进行垂直领域微调的企业用户。
*   构建传统机器学习任务（如分类、回归）并需集成计算机视觉或自然语言处理能力的场景。
*   追求数据驱动开发（Data-Centric AI），注重数据质量而非仅依赖模型架构优化的团队。

4. **技术亮点**
*   **低代码/声明式 API**：通过 YAML 配置文件即可定义复杂模型结构，极大降低入门门槛。
*   **多模态支持**：原生支持文本、图像、音频、数值等多种数据类型，便于构建混合模型。
*   **可扩展性强**：允许用户轻松插入自定义组件或修改现有模块，适应个性化需求。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11743 | 🍴 1218 | 语言: Python
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
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6992 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6267 | 🍴 749 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
该项目是一个极其全面的中英文自然语言处理（NLP）资源合集，涵盖了从基础工具（如敏感词检测、分词、实体抽取）到前沿模型（如BERT、GPT-2应用）的广泛内容。它不仅提供了大量的中文专用语料库、词典和数据集，还集成了多种NLP任务（如情感分析、知识图谱构建、语音识别）的代码实现与解决方案。作为一个社区维护的Awesome List，它旨在为开发者提供一站式的中英NLP学习与开发资源索引。

### 2. 核心功能
*   **基础NLP工具集**：提供敏感词过滤、中英文分词、词性标注、命名实体识别（NER）、情感分析及文本摘要等核心功能的代码实现或库推荐。
*   **丰富语料与知识库**：收录了海量中文专属资源，包括人名、地名、行业术语（金融、医疗、汽车等）、古诗文、成语及停用词库，并支持繁简转换和数字转换。
*   **预训练模型与应用**：整合了BERT、ERNIE、ALBERT、GPT-2等主流预训练模型在中文场景下的微调、部署及应用案例（如问答系统、聊天机器人）。
*   **多模态与专项任务**：涵盖语音识别（ASR）、光学字符识别（OCR）、知识图谱构建与问答、以及文本纠错和拼写检查等专项任务资源。
*   **数据集与评测基准**：汇集了大量公开的中英文NLP竞赛数据集、基准测试任务（Benchmark）及相应的Top方案代码，便于模型评估与复现。

### 3. 适用场景
*   **NLP初学者入门与学习**：适合希望系统学习中英文自然语言处理技术的学生或初级工程师，通过项目中的教程、论文综述和基础工具快速上手。
*   **工业界项目快速开发**：适用于需要构建中文搜索引擎、智能客服、内容审核系统或信息抽取系统的企业开发者，可直接复用其中的词典、模型代码和正则表达式。
*   **学术研究与模型复现**：研究人员可利用其中的最新论文解读、数据集链接和Baseline代码，快速验证新提出的NLP算法或进行对比实验。
*   **垂直领域知识图谱构建**：针对医疗、金融、法律等特定领域，项目提供了相关的专业词库、实体识别工具和知识图谱构建案例，助力领域专用AI应用的开发。

### 4. 技术亮点
*   **极高的资源覆盖率**：作为GitHub上星标数极高的NLP资源库，它几乎囊括了所有主流的中文NLP技术栈，从传统统计方法到最新的Transformer架构。
*   **强调中文特性优化**：特别针对中文痛点提供了大量专用资源，如中文分词加速、中文标点修复、中文手写识别、中文数字转换及中文语境下的情感分析模型。
*   **实用性与前瞻性并重**：既包含了经过时间检验的经典工具（如Jieba、HanLP），也紧跟AI前沿，汇集了BERT、GPT系列等大模型在中文场景下的落地实践。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81934 | 🍴 15249 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目在 ACL 2024 上发表，旨在简化从指令微调到强化学习对齐的完整训练流程。它通过整合多种先进技术，为开发者提供了一站式的高效模型优化解决方案。

2. **核心功能**
*   **多模型兼容**：原生支持 LLaMA、Qwen、Gemma、DeepSeek 等 100 多种开源大模型及视觉语言模型的快速适配。
*   **高效微调策略**：内置 LoRA、QLoRA、P-Tuning 等参数高效微调方法，显著降低显存占用并提升训练速度。
*   **全流程对齐支持**：集成了 RLHF（基于人类反馈的强化学习）、DPO 等高级对齐算法，帮助优化模型输出质量。
*   **量化与加速**：提供 INT4/INT8 量化支持及 FlashAttention 等加速技术，使在消费级硬件上运行大规模模型成为可能。
*   **模块化架构**：采用统一的接口设计，简化了数据预处理、训练配置和模型评估的操作复杂度。

3. **适用场景**
*   **垂直领域模型定制**：企业或个人希望在不从头训练的情况下，利用少量行业数据对基座模型进行指令微调以适配特定任务。
*   **低资源环境开发**：研究人员或开发者在显存有限的普通 GPU 上，需要通过 QLoRA 等技术高效微调大型语言模型。
*   **模型对齐与优化**：需要提升模型遵循指令的能力或减少幻觉，通过 RLHF/DPO 等方法进行后训练优化。
*   **多模态应用构建**：希望快速集成视觉理解能力，对支持图像输入的 VLM 进行微调以构建图文问答或分析应用。

4. **技术亮点**
*   **统一高效**：将分散的微调工具整合为单一框架，实现了极高的易用性和训练效率。
*   **前沿算法集成**：紧跟 NLP 领域最新进展，无缝支持 MoE（混合专家）模型及最新的量化对齐技术。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73413 | 🍴 8962 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一门为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松掌握AI知识。该项目由微软发起，通过结构化的学习路径帮助初学者系统性地了解机器学习与深度学习基础。

2. **核心功能**
*   **系统化课程体系**：提供从基础概念到高级应用（如CNN、RNN、GAN）的完整12周学习路径。
*   **交互式代码实践**：主要采用Jupyter Notebook格式，支持用户在浏览器中直接运行和调试代码。
*   **多领域AI覆盖**：涵盖计算机视觉、自然语言处理及生成对抗网络等主流AI子领域。
*   **零基础友好设计**：专为初学者打造，无需深厚数学或编程背景即可上手学习。
*   **开源社区支持**：作为微软“为初学者而设”系列的一部分，拥有庞大的星标数和活跃的社区贡献。

3. **适用场景**
*   **学生自学**：计算机科学或非技术专业学生进行人工智能基础入门和自我提升。
*   **企业培训**：公司用于对非技术背景员工进行AI素养普及和技术团队的基础技能训练。
*   **教师备课**：教育工作者寻找现成的、结构化的AI教学大纲和实验素材。
*   **转行准备**：希望进入AI领域的从业者通过短期高强度学习建立知识框架。

4. **技术亮点**
*   **微软背书与生态整合**：依托Microsoft For Beginners品牌，内容质量高且常与Azure AI服务结合。
*   **模块化教学设计**：将复杂的AI概念拆解为短小精悍的课时，降低认知负荷，提高学习效率。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52500 | 🍴 10631 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42398 | 🍴 11533 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- ### 1. 中文简介
该项目旨在通过从头构建的方式，深入讲解并实践人工智能工程的核心概念。它提供了一套完整的课程与教程，帮助用户掌握从学习到部署全流程的AI开发技能。最终目标是让学习者能够独立开发出供他人使用的AI应用。

### 2. 核心功能
- 涵盖从基础机器学习到高级生成式AI的全栈课程体系。
- 提供基于Python和Rust等语言的“从零开始”代码实现教程。
- 重点讲解AI代理（Agents）、大语言模型（LLM）及多智能体协作机制。
- 包含计算机视觉、自然语言处理及强化学习等前沿领域的应用实例。
- 支持将本地开发的模型转化为可部署的生产级服务。

### 3. 适用场景
- AI初学者希望系统性地理解底层原理而非仅调用API的学习者。
- 想要构建自定义AI代理或多智能体系统的工程师。
- 需要将生成式AI或计算机视觉模型落地到生产环境的技术团队。
- 对Rust在AI工程中应用感兴趣的高级开发者。

### 4. 技术亮点
- **全栈覆盖**：结合Python的快速迭代优势与Rust的高性能特性，展示现代AI工程的最佳实践。
- **深度定制**：强调“From Scratch”理念，深入Transformer架构及MCP（Model Context Protocol）等最新标准。
- **实战导向**：不仅限于理论，更侧重于如何构建、测试并最终向用户交付可用的AI产品。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 41012 | 🍴 6806 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35593 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33757 | 🍴 4697 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28738 | 🍴 3511 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25966 | 🍴 2943 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21729 | 🍴 3306 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35593 | 🍴 7365 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款利用人工智能自动化浏览器工作流的工具，旨在通过视觉理解和语言模型实现复杂的网页交互。它主要基于 Python 开发，能够替代传统脚本处理各种基于浏览器的任务。该项目致力于提供类似 RPA（机器人流程自动化）但更智能、更具适应性的解决方案。

**2. 核心功能**
*   利用大型语言模型（LLM）和计算机视觉技术理解网页界面并执行操作。
*   支持多种浏览器自动化引擎（如 Playwright、Puppeteer、Selenium）进行底层控制。
*   能够自主导航、填写表单、点击按钮及处理动态网页内容。
*   提供 API 接口，便于集成到现有的业务流程或自动化平台中。

**3. 适用场景**
*   **企业级 RPA 替代**：用于自动化重复性高的网页数据录入、报表生成或系统迁移任务。
*   **跨平台数据抓取**：在目标网站缺乏官方 API 时，通过模拟用户行为安全、高效地收集结构化数据。
*   **工作流自动化测试**：模拟真实用户操作对 Web 应用进行端到端的回归测试和功能验证。
*   **个人效率提升**：自动化日常繁琐的在线操作，如批量预订、比价或信息监控。

**4. 技术亮点**
*   **视觉-语言联合驱动**：不依赖固定的 CSS 选择器，而是通过“看”屏幕来识别元素，极大提高了对 UI 变更的鲁棒性。
*   **多引擎兼容性**：底层抽象层兼容 Playwright、Puppeteer 等主流自动化库，允许用户根据需求灵活切换。
*   **AI 原生架构**：深度整合 GPT 等 LLM 能力，使其具备推理和决策能力，而非简单的规则执行。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22535 | 🍴 2112 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16347 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- **1. 中文简介**
pytorch-grad-cam 是一个用于计算机视觉的高级AI可解释性工具库。它支持包括CNN、Vision Transformers在内的多种模型，以及分类、目标检测、分割等多种任务。该项目旨在通过可视化手段帮助理解深度学习模型的决策依据。

**2. 核心功能**
*   支持Grad-CAM、Score-CAM等多种主流的可解释性算法实现。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
*   覆盖图像分类、目标检测、语义分割及图像相似度计算等任务类型。
*   提供直观的注意力图可视化，增强模型决策的透明度。

**3. 适用场景**
*   **医疗影像分析**：可视化医生关注的病灶区域，辅助诊断结果的可信度评估。
*   **自动驾驶系统调试**：分析模型在目标检测中对道路物体或行人的关注点，提升安全性验证。
*   **学术研究与教学**：作为可解释人工智能（XAI）的教学案例，深入理解深度学习内部机制。
*   **模型故障排查**：通过检查模型是否关注错误特征（如背景噪声而非主体），优化模型性能。

**4. 技术亮点**
*   广泛支持最新的视觉Transformer架构，适应前沿模型需求。
*   模块化设计，轻松集成到现有的PyTorch项目中。
*   拥有极高的社区活跃度（12k+星标），文档完善且生态成熟。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- **1. 中文简介**
Kornia 是一个专注于空间人工智能（Spatial AI）的几何计算机视觉库，旨在通过 PyTorch 实现可微分的图像处理与几何操作。它作为传统 OpenCV 的现代替代方案，无缝集成深度学习工作流，支持端到端的视觉任务开发。

**2. 核心功能**
*   提供基于 PyTorch 的可微分几何算子，支持梯度反向传播以优化神经网络参数。
*   实现丰富的图像处理原语，如滤波、形态学操作及色彩空间转换，均具备 GPU 加速能力。
*   内置高级三维几何模块，涵盖相机标定、立体视觉及单目深度估计等经典算法。
*   完全兼容 PyTorch 生态系统，允许在训练循环中直接调用计算机视觉变换。

**3. 适用场景**
*   **可微分计算机视觉管线构建**：用于需要端到端训练的传统 CV 算法，如可微分相机模型或几何损失计算。
*   **机器人感知与导航**：为空间智能应用提供高效的实时图像处理与姿态估计工具。
*   **图像增强数据增强**：在深度学习中利用其强大的图像变换库进行高效的数据预处理和增强。

**4. 技术亮点**
*   **软硬协同加速**：充分利用 GPU 并行计算能力，显著优于传统 CPU 实现的 OpenCV 某些操作。
*   **深度学习原生集成**：摒弃了传统的 NumPy 中间层，直接使用 Tensor 运算，避免内存拷贝并简化调试。
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1204 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8874 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3459 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3289 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2629 | 🍴 693 | 语言: Jupyter Notebook
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
- ⭐ 383637 | 🍴 80602 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 258437 | 🍴 23032 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 基于您提供的项目元数据，以下是关于 **hermes-agent** 的技术分析：

1. **中文简介**
Hermes Agent 是一款具备成长能力的智能代理工具，旨在随着用户的使用习惯和反馈不断优化其性能。它集成了多种主流大语言模型（如 Claude、ChatGPT 等），为用户提供灵活且强大的 AI 交互体验。

2. **核心功能**
*   **多模型支持**：兼容 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 等多个主流 LLM 提供商。
*   **自适应成长机制**：通过持续交互和学习，代理能力会随时间推移和用户反馈逐步增强。
*   **统一交互接口**：提供标准化的 API 或命令行界面，简化不同 AI 服务的集成与调用流程。
*   **开发者友好生态**：支持自定义配置和扩展，便于开发者构建个性化的 AI 工作流。

3. **适用场景**
*   **个性化 AI 助手开发**：需要构建能随用户习惯进化的智能客服或个人助理系统。
*   **跨平台 AI 集成**：希望在一个框架内同时调用多个不同厂商的大模型进行业务处理。
*   **自动化代码/文本生成**：利用不断优化的代理能力辅助编程、文档编写或内容创作。
*   **AI 研究实验**：测试不同 LLM 在长期交互场景下的表现差异及自我优化潜力。

4. **技术亮点**
*   **高社区活跃度**：拥有超过 21.8 万星标，表明其在开发者社区中具有极高的认可度和影响力。
*   **广泛的模型兼容性**：标签显示其覆盖了从开源到闭源的众多顶级 AI 模型，技术栈极具灵活性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218042 | 🍴 41178 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197293 | 🍴 59495 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- **1. 中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。其使命是提供必要的工具，使您能将精力集中在真正重要的事务上。

**2. 核心功能**
*   支持基于 GPT、Claude 和 Llama 等多种大语言模型的自主代理操作。
*   具备自动化执行复杂任务链的能力，无需人工持续干预。
*   提供开放的开发接口，便于用户在其基础上构建自定义 AI 应用。
*   集成多种外部工具与 API，增强代理对互联网及本地文件的交互能力。

**3. 适用场景**
*   自动化市场调研、数据收集与信息整合流程。
*   作为个人助手自动处理邮件分类、日程安排等日常琐事。
*   开发者用于测试和构建更复杂的智能代理（Agentic AI）系统原型。

**4. 技术亮点**
*   采用模块化架构，灵活支持 OpenAI、Anthropic 及 Hugging Face 等主流 LLM 后端。
*   强调“可访问性”设计，降低普通人部署和使用高级 AI 代理的技术门槛。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185630 | 🍴 46069 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166103 | 🍴 21467 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164264 | 🍴 30428 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157166 | 🍴 46179 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 153727 | 🍴 8775 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152136 | 🍴 9615 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

