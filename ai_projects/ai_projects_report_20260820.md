# GitHub AI项目每日发现报告
日期: 2026-08-20

## 新发布的AI项目

### watermarks-remover
- 

## GitHub 项目分析：watermarks-remover

### 1. 中文简介
该项目用于移除多种AI工具生成的溯源痕迹，包括Unicode文本清理、统计重写技术，以及从PNG/JPEG/SVG/PDF/DOCX/HTML/MD等格式文件中剥离C2PA标准和元数据信息。

### 2. 核心功能
- **Unicode文本清理**：移除嵌入在文件中的不可见Unicode字符水印
- **统计重写技术**：通过改变文本统计特征来消除AI生成痕迹
- **C2PA/元数据剥离**：从多种文件格式中清除内容溯源和版权信息
- **多格式支持**：兼容图片（PNG/JPEG/SVG）、文档（PDF/DOCX）和文本（HTML/MD）格式
- **多供应商兼容**：支持移除不同AI平台（如Claude、Codex、Grok等）的溯源标记

### 3. 适用场景
- 内容创作者需要清理AI生成内容中的平台溯源标记
- 企业文档处理中移除AI工具使用痕迹以满足合规要求
- 安全研究人员测试和评估AI水印检测技术
- 学术或商业场景中需要匿名化处理AI辅助生成的文件

### 4. 技术亮点
- **C2PA标准支持**：兼容内容来源与真实性联盟（Coalition for Content Provenance and Authenticity）标准
- **多技术组合**：结合文本清理、统计重写和元数据剥离多种方法
- **跨格式处理**：统一支持图片、文档、网页和代码文件等多种格式
- 链接: https://github.com/Leutenegger/watermarks-remover
- ⭐ 921 | 🍴 95 | 语言: Python
- 标签: claude, claude-code, claude-skills, codex, codex-cli

### llm-rag-memory-ai-agents
- 

# GitHub项目分析：llm-rag-memory-ai-agents

## 1. 中文简介
该项目是一个结合大语言模型（LLM）、检索增强生成（RAG）和记忆系统的AI代理框架。它旨在为AI代理提供长期记忆能力和上下文感知能力，使其能够持续学习和适应。项目使用Python开发，适合构建智能对话系统和个性化AI助手。

## 2. 核心功能
- 集成大语言模型实现智能对话与推理
- 基于RAG技术的知识检索与增强生成
- 持久化记忆存储，支持长期上下文保持
- AI代理架构，支持任务规划与执行
- 可扩展的插件系统设计

## 3. 适用场景
- 构建个性化智能客服与对话助手
- 开发具备记忆能力的AI虚拟助手
- 企业知识库问答系统
- 多轮对话与长期交互场景

## 4. 技术亮点
- 将LLM、RAG与记忆系统深度融合的创新架构
- 支持上下文持久化的记忆管理机制
- 轻量级Python实现，易于集成和扩展

---

**备注**：该项目描述为空，以上分析基于项目名称关键词推断，建议查看仓库README获取更准确信息。
- 链接: https://github.com/turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents
- ⭐ 102 | 🍴 0 | 语言: Python

### dsh-oil-creator
- 描述: AI-assisted local creator workbench for DeepSeek Harness
- 链接: https://github.com/oil-oil/dsh-oil-creator
- ⭐ 88 | 🍴 18 | 语言: TypeScript
- 标签: creator, deepseek-harness, dsh-plugin

### github-farm
- 

## GitHub 项目分析：github-farm

---

### 1. 中文简介
这是一个面向 AI 网关的生产级 OAuth 收集与会话管理框架，专为 AI 代理（Agent）友好设计。它支持多平台 OAuth 认证流程，可帮助 AI 系统统一管理不同平台的用户会话与授权状态。

---

### 2. 核心功能
- 多平台 OAuth 认证流程自动化收集与管理
- 面向 AI 代理优化的会话状态管理
- 生产级稳定性，支持高并发场景部署
- 为 AI 网关提供统一的身份认证中间层
- 支持主流平台的 OAuth 协议集成

---

### 3. 适用场景
- **AI 代理集成多平台服务**：如让 AI 代理自动访问 Twitter、GitHub 等多个平台 API
- **AI 网关身份管理**：为多个 AI 网关统一处理 OAuth 认证与会话持久化
- **自动化工作流平台**：需要跨平台授权的自动化任务调度系统
- **企业级 AI 应用开发**：需要安全、可扩展的 OAuth 管理方案的产品

---

### 4. 技术亮点
- **AI-Agent 友好设计**：针对 AI 代理的使用模式优化了认证流程
- **生产级架构**：具备高可用性和可扩展性，适合正式环境部署
- **多平台统一抽象**：一次集成，支持多个 OAuth 平台的标准化交互
- **会话管理自动化**：自动处理 token 刷新、过期管理等复杂逻辑

---

**总结**：该项目是一个专注于 AI 网关场景的 OAuth 管理框架，适合需要为 AI 系统统一管理多平台身份认证与会话的开发者使用。
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 84 | 🍴 6 | 语言: Python

### lanshu-create-ai-presenter-video
- 

## GitHub项目分析：lanshu-create-ai-presenter-video

### 1. 中文简介
这是一个与提供商无关的Codex技能，可根据脚本和授权的主持人照片生成经过验证的AI演示者视频。该项目专为快速生成数字人视频而设计，支持多种AI视频生成服务。

### 2. 核心功能
- 根据文本脚本自动生成AI演示者视频
- 支持使用授权的主持人照片作为数字人形象
- 兼容多个AI视频生成提供商，可灵活切换
- 通过Codex技能集成，便于自动化调用
- 生成结果可验证，确保视频内容符合预期

### 3. 适用场景
- 企业培训视频制作：快速生成讲师数字人讲解视频
- 产品营销宣传：用虚拟代言人展示产品功能
- 在线教育课程：批量生成教学视频内容
- 新闻播报与演讲：自动生成虚拟主播播报视频

### 4. 技术亮点
- **提供商中立设计**：不绑定特定AI服务，可自由切换底层视频生成引擎
- **Codex技能架构**：专为OpenAI Codex优化，便于智能体自动化调用
- **数字人形象授权机制**：支持使用授权照片，确保身份合规性
- **Python实现**：代码简洁，易于二次开发和定制扩展
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 34 | 🍴 5 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### OpenCMO
- 描述: The open-source CMO: growth playbooks from 16 operators (Cursor, Notion, Linear, Deel, Gamma, Granola...) as an installable AI skill
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
- ⭐ 28 | 🍴 1 | 语言: Python
- 标签: awesome, awesome-list, cursor, grok-bot, xai

### scibly
- 描述: Scibly is an open-source, AI-native learning platform. Turn your existing knowledge into interactive learning experiences.
- 链接: https://github.com/scibly-dev/scibly
- ⭐ 26 | 🍴 1 | 语言: TypeScript
- 标签: ai-agents, corporate-learning, duolingo, education, learning

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

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI项目代码的综合性资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目以"Awesome"列表形式组织，为开发者提供丰富的实战案例和代码参考。

---

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带完整代码，便于学习和直接复用
- 按技术领域分类整理，方便快速定位所需项目
- 作为一站式学习资源库，适合从入门到进阶的开发者

---

### 3. 适用场景
- **学习者**：希望通过实战项目系统掌握AI技术的初学者和进阶者
- **开发者**：需要快速参考或复用AI项目代码的工程师
- **教育者**：寻找教学案例和项目作业参考的教师
- **研究者**：需要调研各AI领域实现方案的科研人员

---

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，是同类资源库中的大型合集
- 36412颗星表明其社区认可度高，持续维护和更新
- 标签分类清晰，涵盖AI核心领域，便于按兴趣筛选
- 以Python为主要语言，符合AI领域主流开发生态
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36412 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化查看器，支持多种主流框架格式。它提供直观的图形化界面，帮助用户快速理解和分析模型结构。

## 2. 核心功能
- 支持查看多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 以图形化方式展示神经网络各层结构和参数信息
- 支持模型推理路径追踪，可高亮显示数据流向
- 提供 Web 版本和桌面客户端，方便跨平台使用
- 支持查看 safetensors、NumPy 等常见数据格式

## 3. 适用场景
- **模型调试**：开发者在训练完成后快速检查模型结构是否正确
- **论文复现**：研究人员可视化他人开源模型的架构设计
- **模型部署前审查**：工程团队在将模型转换为特定格式前确认结构完整性
- **教学演示**：教师和学生直观理解神经网络各层的工作原理

## 4. 技术亮点
- 开源项目，星标数超过 3.3 万，社区活跃度高
- 支持格式极其广泛，几乎覆盖主流 AI 框架
- 提供在线网页版，无需安装即可直接使用
- 支持 safetensors 等新兴模型格式，保持技术前沿性
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33370 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

## ONNX 项目分析

### 1. 中文简介
ONNX（Open Neural Network Exchange）是机器学习领域的开放互操作标准，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同框架之间无缝迁移模型，打破了框架间的壁垒。

### 2. 核心功能
- 提供统一的模型表示格式，支持跨框架的模型交换
- 支持将PyTorch、TensorFlow、Keras等框架的模型转换为ONNX格式
- 提供模型转换和优化工具链，便于部署到不同硬件平台
- 定义了通用的算子和张量规范，确保模型在不同运行时环境中的兼容性
- 支持模型图可视化，便于调试和分析模型结构

### 3. 适用场景
- 需要将PyTorch训练好的模型部署到TensorRT等推理引擎时
- 在移动端或嵌入式设备上运行深度学习模型
- 跨框架协作场景，如使用不同框架进行模型训练和部署
- 模型性能优化和加速场景，如模型量化、剪枝等

### 4. 技术亮点
- 由Facebook和Microsoft联合发起，拥有强大的社区和企业支持
- 已被广泛采纳为行业标准，支持主流深度学习框架
- 提供完善的工具生态，包括转换工具、验证工具和优化工具
- 持续迭代更新，不断扩展支持的算子和功能特性
- 链接: https://github.com/onnx/onnx
- ⭐ 21337 | 🍴 4004 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

# GitHub项目分析：ml-engineering

## 1. 中文简介
《机器学习工程开放手册》是一本聚焦于大规模机器学习系统构建与部署的开源技术书籍。内容涵盖从训练、推理到可扩展性设计的完整机器学习工程实践指南。

## 2. 核心功能
- 提供大规模LLM训练和推理的实战工程指导
- 深入讲解GPU集群配置、网络优化与存储策略
- 包含PyTorch框架下的分布式训练最佳实践
- 介绍Slurm调度器在超算环境中的部署与调试技巧
- 覆盖MLOps全流程，包括模型调试、可伸缩性设计与生产部署

## 3. 适用场景
- 科研团队在超算集群上训练大规模语言模型
- 工程团队构建高可用、低延迟的LLM推理服务
- 企业搭建端到端的机器学习生产Pipeline
- 开发者排查GPU训练过程中的性能瓶颈与调试问题

## 4. 技术亮点
- 开源免费，内容持续更新，社区协作维护
- 聚焦实际工程问题，而非纯理论推导
- 覆盖从硬件选型到模型部署的完整技术栈
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

## 项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介
这是一个收录了500个AI项目代码的综合性资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。该项目以"Awesome"列表形式组织，为开发者提供丰富的实战案例和代码参考。

---

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带完整代码，便于学习和直接复用
- 按技术领域分类整理，方便快速定位所需项目
- 作为一站式学习资源库，适合从入门到进阶的开发者

---

### 3. 适用场景
- **学习者**：希望通过实战项目系统掌握AI技术的初学者和进阶者
- **开发者**：需要快速参考或复用AI项目代码的工程师
- **教育者**：寻找教学案例和项目作业参考的教师
- **研究者**：需要调研各AI领域实现方案的科研人员

---

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，是同类资源库中的大型合集
- 36412颗星表明其社区认可度高，持续维护和更新
- 标签分类清晰，涵盖AI核心领域，便于按兴趣筛选
- 以Python为主要语言，符合AI领域主流开发生态
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36412 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

# Netron 项目分析

## 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化查看器，支持多种主流框架格式。它提供直观的图形化界面，帮助用户快速理解和分析模型结构。

## 2. 核心功能
- 支持查看多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML、TensorFlow Lite 等
- 以图形化方式展示神经网络各层结构和参数信息
- 支持模型推理路径追踪，可高亮显示数据流向
- 提供 Web 版本和桌面客户端，方便跨平台使用
- 支持查看 safetensors、NumPy 等常见数据格式

## 3. 适用场景
- **模型调试**：开发者在训练完成后快速检查模型结构是否正确
- **论文复现**：研究人员可视化他人开源模型的架构设计
- **模型部署前审查**：工程团队在将模型转换为特定格式前确认结构完整性
- **教学演示**：教师和学生直观理解神经网络各层的工作原理

## 4. 技术亮点
- 开源项目，星标数超过 3.3 万，社区活跃度高
- 支持格式极其广泛，几乎覆盖主流 AI 框架
- 提供在线网页版，无需安装即可直接使用
- 支持 safetensors 等新兴模型格式，保持技术前沿性
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33370 | 🍴 3172 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# GitHub项目分析：cheatsheets-ai

## 1. 中文简介
这是一个专为深度学习与机器学习研究者整理的必备速查手册集合。项目涵盖了机器学习、深度学习及相关工具库的核心知识点，方便研究人员快速查阅和复习关键概念与公式。

## 2. 核心功能
- 提供机器学习与深度学习领域的核心概念速查表
- 涵盖Keras、NumPy、SciPy、Matplotlib等常用工具的语法与API参考
- 整理关键公式、定理及算法流程，便于快速检索
- 以简洁的文档形式呈现，适合打印或离线查阅

## 3. 适用场景
- 深度学习研究者复习基础知识与核心公式
- 机器学习工程师查阅常用库的API用法
- 学生备考或面试前快速梳理知识点
- 研究人员撰写论文时参考标准术语与公式表达

## 4. 技术亮点
- 项目星标数高达15428，说明在社区中具有较高的认可度和实用价值
- 标签涵盖AI、深度学习、Keras、机器学习、Matplotlib、NumPy、SciPy等，内容全面且聚焦主流技术栈
- 作为纯文档型项目，无需额外依赖即可使用，便于快速上手和分享
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15428 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个全面的人工智能学习路线图项目，整理了近200个实战案例与项目，免费提供配套教材，适合零基础入门和就业实战。涵盖Python、数学、机器学习、深度学习、计算机视觉、自然语言处理等热门领域。

### 2. 核心功能
- 提供系统化的人工智能学习路径和路线图
- 整理近200个实战案例与项目供学习参考
- 免费提供配套教材和学习资料
- 覆盖从零基础到就业的全流程学习
- 包含Python、机器学习、深度学习等完整技术栈

### 3. 适用场景
- AI初学者系统学习人工智能基础知识
- 想要转行AI领域的程序员提升技能
- 需要实战项目经验的求职者准备面试
- 教师或培训机构用于AI课程教学

### 4. 技术亮点
- 星标数达13271，说明社区认可度高
- 涵盖主流框架：PyTorch、TensorFlow、Keras等
- 完整技术栈：从数学基础到NLP、CV等应用
- 免费开源，配套教材齐全
- 注重实战，提供大量项目案例
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13271 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

# Ludwig 项目分析

## 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义大语言模型（LLM）、神经网络及其他AI模型。它通过声明式配置实现模型训练，无需编写大量代码即可完成从数据处理到模型部署的全流程。

## 2. 核心功能
- **低代码模型构建**：通过声明式 YAML/JSON 配置即可定义和训练深度学习模型，无需手写复杂代码。
- **多模态支持**：原生支持表格数据、文本、图像等多种数据类型，内置丰富的特征处理组件。
- **LLM 微调**：提供对 LLaMA、Mistral 等主流大语言模型的微调支持，简化训练流程。
- **自动化训练流程**：内置数据预处理、特征工程、模型训练、评估和部署的一体化工作流。
- **PyTorch 驱动**：基于 PyTorch 构建，兼容主流深度学习生态。

## 3. 适用场景
- **快速原型开发**：数据科学家或研究人员希望无需深入编码即可快速验证机器学习想法。
- **LLM 微调**：AI 工程师需要对 LLaMA、Mistral 等大语言模型进行领域适配和微调。
- **端到端 ML 管道**：团队需要一套完整的从数据到部署的机器学习工作流，减少工程复杂度。
- **多模态应用**：需要同时处理文本、图像和表格数据的综合 AI 项目。

## 4. 技术亮点
- **声明式配置**：通过简洁的配置文件定义模型结构，大幅降低开发门槛。
- **自动特征工程**：内置自动化的特征编码、归一化和嵌入处理，减少手动操作。
- **可扩展架构**：支持自定义组件和扩展点，可灵活适配特定业务需求。
- **HuggingFace 集成**：与 HuggingFace Transformers 深度集成，方便调用和微调预训练模型。
- **社区活跃**：11747 星标，拥有活跃的开源社区和持续迭代更新。
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

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持 100 多种主流模型。该项目在 ACL 2024 会议上发表，旨在为开发者提供一站式模型微调解决方案。

### 2. 核心功能
- 支持 100+ 种 LLM 和 VLM 的统一微调，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型
- 提供 LoRA、QLoRA、全参数微调等多种微调策略
- 支持 RLHF（基于人类反馈的强化学习）和直接偏好优化（DPO）等对齐技术
- 内置量化功能，支持低精度部署以节省显存
- 兼容 Hugging Face Transformers 生态，易于集成现有工作流

### 3. 适用场景
- **企业级模型定制**：使用自有数据对开源模型进行领域适配
- **多模态应用开发**：对视觉语言模型进行指令微调，构建图文理解系统
- **资源受限环境**：通过 QLoRA 和量化技术在消费级 GPU 上完成高效微调
- **RLHF 对齐研究**：训练符合人类偏好的模型，提升对话质量

### 4. 技术亮点
- **统一架构**：一套代码支持 100+ 模型，降低多模型适配成本
- **ACL 2024 学术论文背书**：经过学术界认可的技术方案
- **高性能优化**：针对显存和训练效率进行深度优化，支持 MoE（混合专家）模型
- **完整工具链**：涵盖数据处理、微调、评估、部署全流程
- **活跃的社区生态**：74000+ 星标，丰富的标签覆盖主流 AI 技术栈
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74253 | 🍴 9080 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一个面向初学者的AI入门课程，采用12周24课的教学模式，旨在让所有人都能轻松学习人工智能。课程由微软开源，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。

### 2. 核心功能
- 提供结构化的12周学习路径，每周一课，循序渐进
- 基于Jupyter Notebook的交互式代码环境，便于动手实践
- 涵盖机器学习、深度学习、CNN、RNN、GAN、NLP等完整AI知识体系
- 微软官方维护，内容质量可靠且持续更新

### 3. 适用场景
- 计算机相关专业学生系统学习AI基础理论
- 转行或自学AI的初学者入门训练
- 企业团队AI技术培训与内部学习
- 教师用于课堂教学的配套教材

### 4. 技术亮点
- 微软教育团队精心设计的课程体系，兼顾理论与实践
- 使用Jupyter Notebook实现代码与文档一体化教学
- 标签覆盖全面（ML/DL/CV/NLP），适合不同方向的学习者
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 65860 | 🍴 12761 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## GitHub项目分析：ai-engineering-from-scratch

### 1. 中文简介
"学习它，构建它，为他人交付它。"这是一个从零开始系统学习AI工程的完整教程项目，涵盖从基础理论到实际部署的全流程实践。

### 2. 核心功能
- **从零构建AI系统**：深入底层原理，手把手教用户从头实现各类AI模型和工具
- **多领域覆盖**：包含LLM、生成式AI、计算机视觉、NLP、强化学习、智能体（Agents）等核心方向
- **多语言支持**：同时使用Python、Rust、TypeScript进行教学和实践
- **MCP协议集成**：教授Model Context Protocol（模型上下文协议）的实际应用
- **Swarm Intelligence探索**：涵盖群体智能与多智能体系统的实现方法

### 3. 适用场景
- **AI工程师入门**：希望系统掌握AI工程全栈技能的开发者
- **深度学习实践者**：需要从零理解Transformer、LLM等核心架构的学习者
- **AI产品开发者**：计划构建并部署AI应用给最终用户的工程师
- **进阶研究人员**：探索智能体系统、群体智能等前沿方向的从业者

### 4. 技术亮点
- **高人气项目**：47,305颗星标，说明社区认可度极高
- **实战导向**：强调"Build it"和"Ship it"，注重实际落地能力
- **技术栈全面**：横跨Python、Rust、TypeScript三大语言，覆盖AI工程主流工具链
- **前沿技术整合**：包含MCP、Swarm Intelligence等新兴技术方向
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47305 | 🍴 8313 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

## 项目分析：ailearning

### 1. 中文简介
AiLearning 是一个涵盖数据分析、机器学习实战、线性代数、PyTorch、NLTK 和 TensorFlow 2 的综合性学习项目。该项目通过理论与实践相结合的方式，帮助学习者系统掌握人工智能与机器学习领域的核心技能。

### 2. 核心功能
- 提供完整的数据分析与机器学习实战教程
- 涵盖经典机器学习算法（SVM、KMeans、逻辑回归、朴素贝叶斯等）
- 包含深度学习框架实战（PyTorch、TensorFlow 2）
- 集成自然语言处理库 NLTK 进行 NLP 实践
- 涵盖推荐系统、关联规则挖掘（Apriori、FP-Growth）等应用场景

### 3. 适用场景
- 机器学习入门学习者系统学习与实践
- 数据分析师提升算法实现能力
- 深度学习爱好者进行 PyTorch/TensorFlow 实战训练
- 需要复习线性代数与算法原理的学习者

### 4. 技术亮点
- 项目星标数达 42468，社区认可度高
- 内容覆盖全面，从基础理论到深度学习框架均有涉及
- 结合 scikit-learn 等主流工具，注重实战落地能力
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42468 | 🍴 11516 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36412 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33835 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29141 | 🍴 3549 | 语言: Jupyter Notebook
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

## 项目分析

### 1. 中文简介
该项目是一个收录了500个AI项目的资源合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供完整代码实现。这是一个被广泛认可的awesome列表，适合不同水平的开发者学习与实践。

### 2. 核心功能
- 收录500个AI相关项目，覆盖机器学习、深度学习、计算机视觉和NLP四大领域
- 每个项目均附带可运行的代码，便于学习者直接上手实践
- 按领域分类整理，结构清晰，方便快速定位所需内容
- 项目质量经过社区筛选，属于awesome列表级别的优质资源

### 3. 适用场景
- AI初学者系统学习各领域的经典项目与实现思路
- 开发者寻找项目灵感或参考代码进行二次开发
- 面试准备时快速浏览常见AI项目类型
- 教师或培训人员作为课程参考资料

### 4. 技术亮点
- 项目数量庞大（500个），覆盖面广，一站式解决多领域学习需求
- 所有项目均提供源码，强调动手实践而非纯理论
- 高星标数（36412）说明项目经过社区长期检验，质量可靠
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36412 | 🍴 7446 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

## Skyvern 项目分析

### 1. 中文简介
Skyvern 是一款基于人工智能的浏览器自动化框架，能够智能地自动化各类基于浏览器的业务流程。它结合视觉识别与大语言模型技术，让AI能够"看见"并操作网页界面，实现类似人类用户的交互体验。

### 2. 核心功能
- **AI驱动的浏览器自动化**：利用大语言模型和视觉技术理解网页内容并执行操作
- **视觉感知能力**：通过计算机视觉识别页面元素，无需依赖传统选择器
- **多浏览器引擎支持**：兼容 Playwright、Puppeteer、Selenium 等主流自动化工具
- **API接口**：提供简洁的API，便于集成到现有工作流中
- **RPA替代方案**：作为传统RPA工具（如Power Automate）的AI增强替代

### 3. 适用场景
- **电商自动化**：自动比价、下单、库存监控等电商流程
- **数据抓取与表单填写**：自动化批量处理网页表单和数据采集任务
- **企业工作流自动化**：替代人工操作ERP、CRM等系统的重复性浏览器任务
- **测试与质量保障**：AI辅助的端到端浏览器测试

### 4. 技术亮点
- 将大语言模型（LLM）的推理能力与浏览器自动化相结合，实现真正的"理解型"自动化
- 视觉优先的交互方式，降低了对网页结构变化的敏感度，适应性更强
- 开源免费，社区活跃（22802+星标），技术栈现代化（Python + Playwright）
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22802 | 🍴 2140 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

## CVAT 项目分析

### 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，专为视觉AI开发而设计。它提供开源、云版和企业版产品，并配套标注服务，支持图像、视频及3D数据的AI辅助标注、质量保证、团队协作和开发者API。

### 2. 核心功能
- **多模态标注支持**：支持图像、视频和3D数据的标注任务。
- **AI辅助标注**：集成自动化标注能力，可结合PyTorch/TensorFlow模型加速标注流程。
- **团队协作与质检**：提供多人协作标注及质量审核机制，确保数据集质量。
- **多种标注类型**：支持边界框、图像分类、语义分割、目标检测等多种标注格式。
- **灵活部署方案**：提供开源自部署、云端SaaS及企业级产品三种使用方式。

### 3. 适用场景
- **AI模型训练数据准备**：为图像分类、目标检测等任务标注训练数据集。
- **视频分析项目**：对视频帧进行逐帧标注，用于行为识别、目标跟踪等场景。
- **3D点云标注**：适用于自动驾驶、机器人感知等领域的3D数据标注。
- **团队协作标注项目**：大规模团队分工协作，高效完成海量数据标注任务。

### 4. 技术亮点
- 支持主流深度学习框架（PyTorch、TensorFlow），可无缝对接现有模型进行预标注。
- 提供开发者API，便于集成到自动化数据流水线中。
- 开源社区活跃，星标数超过16,500，生态完善且持续迭代。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16556 | 🍴 3807 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

## 1. 中文简介
这是一个先进的计算机视觉可解释性AI工具库，支持CNN、视觉Transformer等多种模型架构。可用于分类、目标检测、分割、图像相似度等多种任务的可视化解释。

## 2. 核心功能
- 支持多种Grad-CAM变体（如Grad-CAM、Grad-CAM++、Score-CAM等）
- 兼容PyTorch框架下的CNN和Vision Transformer模型
- 提供类别激活图（CAM）的可视化生成功能
- 支持图像分类、目标检测、语义分割等多种任务
- 内置图像相似度分析的可视化能力

## 3. 适用场景
- 深度学习模型的可解释性研究与可视化展示
- 计算机视觉模型的决策依据分析与调试
- 学术论文中的结果可视化与解释说明
- 医疗影像、自动驾驶等需要模型透明度的领域

## 4. 技术亮点
- 项目星标数超过12,900，社区认可度高
- 统一的API接口支持多种CAM方法的快速切换
- 完整的文档和示例代码，易于上手使用
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12954 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
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
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 386899 | 🍴 81270 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 274788 | 🍴 24588 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

---

### 1. 中文简介

Hermes Agent 是一款由 Nous Research 开发的 AI 智能体工具，能够伴随用户共同成长与进化。它支持接入多种主流大语言模型平台，为用户提供灵活、可定制的 AI 辅助体验。

---

### 2. 核心功能

- **多模型支持**：兼容 Claude、GPT、Codex 等多个主流 LLM 平台，用户可根据需求自由切换。
- **智能体记忆与成长**：具备持续学习能力，能随使用过程积累上下文，逐步适应用户习惯。
- **代码辅助与自动化**：支持代码生成、调试、重构等开发场景，可作为编程助手使用。
- **可扩展架构**：提供插件化设计，允许开发者自定义行为和功能模块。
- **开源可定制**：完全开源，用户可基于源码进行二次开发和个性化部署。

---

### 3. 适用场景

- **日常编程助手**：开发者在日常编码中获取代码建议、Bug 修复和架构设计支持。
- **AI 研究探索**：研究人员利用其多模型接口对比不同 LLM 的表现与能力差异。
- **自动化工作流**：将 Hermes Agent 集成到 CI/CD 或任务调度系统中，实现智能自动化。
- **个人知识助手**：作为个人 AI 助手，帮助整理信息、生成文档和进行知识管理。

---

### 4. 技术亮点

- 由 **Nous Research** 团队开发，在开源 LLM 领域具有较高知名度。
- 支持 **多模型路由**，可灵活对接 Anthropic、OpenAI 等商业 API。
- 项目星标数超过 **23 万**，说明在社区中拥有广泛影响力和用户认可度。
- 标签涵盖 `claude-code`、`codex` 等，暗示其与主流编程智能体生态深度整合。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233448 | 🍴 46746 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平代码（fair-code）工作流自动化平台，内置原生 AI 能力。支持可视化构建与自定义代码结合，可自托管或云端部署，提供 400+ 种集成连接器。

### 2. 核心功能
- 可视化工作流编辑器，支持拖拽式节点构建
- 内置 AI 能力，可无缝集成大语言模型
- 400+ 预置集成，覆盖主流 API 和 SaaS 服务
- 支持自托管与云端部署两种模式
- 允许将自定义代码嵌入工作流节点

### 3. 适用场景
- 企业级自动化流程编排（如数据同步、消息通知）
- AI 驱动的智能工作流（如文档处理、问答系统）
- 低代码/无代码平台的集成中台构建
- 需要数据隐私控制的自托管自动化方案

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且生态兼容性好
- 支持 MCP（Model Context Protocol）协议，可与 AI 模型深度交互
- 开源公平代码协议，兼顾社区友好与商业可用
- 20万+ 星标，社区活跃度高，插件生态丰富
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201348 | 🍴 60249 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 承载着让每个人都能轻松使用并基于其构建的 AI 愿景。我们的使命是提供相应工具，让用户能够专注于真正重要的事务。

### 2. 核心功能
- 支持自主执行复杂任务，无需人工逐条干预
- 可自主规划、分解并执行多步骤工作流
- 支持多种大语言模型后端（GPT、Claude、Llama 等）
- 提供可扩展的插件系统，便于功能定制
- 支持记忆存储，实现跨任务上下文延续

### 3. 适用场景
- 自动化日常办公任务（如信息检索、数据整理、邮件处理）
- 内容创作与文案生成（文章撰写、翻译、摘要）
- 代码开发与调试辅助（自动生成代码、排查问题）
- 研究与信息分析（网络搜索、报告生成）

### 4. 技术亮点
- 采用 Agent 架构，具备自我反思与迭代优化能力
- 支持多模型切换，灵活适配不同场景需求
- 开源社区活跃，持续迭代更新
- 模块化设计，便于二次开发与集成
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186686 | 🍴 46047 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 169969 | 🍴 9470 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167637 | 🍴 21643 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164594 | 🍴 30548 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157911 | 🍴 46170 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153505 | 🍴 9899 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

