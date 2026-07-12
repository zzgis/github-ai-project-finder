# GitHub AI项目每日发现报告
日期: 2026-07-12

## 新发布的AI项目

### ai-content-kb
- 1. **中文简介**
该项目提出了一种“审查优先”的参考架构，旨在构建由AI辅助的个人内容知识系统。它强调在自动化处理之前引入人工审核机制，以确保个人知识库的准确性和可靠性。

2. **核心功能**
*   提供基于“审查优先”理念的个人知识管理系统参考架构。
*   整合AI技术以辅助内容的提取、分类和知识化管理。
*   设计专注于个人内容资产的结构化存储与检索方案。
*   通过人工审核环节平衡AI自动化效率与信息准确性。

3. **适用场景**
*   需要建立高可信度个人数字图书馆或笔记系统的用户。
*   希望利用AI整理海量碎片化信息但担心错误自动化的研究者。
*   对个人信息隐私和数据质量控制有较高要求的知识工作者。

4. **技术亮点**
*   创新性地引入了“审查优先”（Review-First）范式，弥补了纯AI生成内容的不可控性。
*   作为参考架构（Reference Architecture），为开发者提供了可复用的系统设计蓝图而非具体代码实现。
- 链接: https://github.com/mrbear1024/ai-content-kb
- ⭐ 81 | 🍴 6 | 语言: 未知

### kitforai
- 1. **中文简介**
Kit for AI 是面向 AI 开发者的官方集线器工具包，提供 SDK、Claude Code 插件、MCP 配置及 llms.txt 支持。它旨在为开发者构建一站式的基础设施，简化 AI 应用的集成与开发流程。

2. **核心功能**
- 提供官方 AI 开发 SDK，便于代码集成。
- 包含 Claude Code 插件，增强 CLI 下的 AI 交互体验。
- 内置 MCP（Model Context Protocol）设置，实现标准化的模型上下文连接。
- 支持 llms.txt 文件生成，优化大型语言模型对项目的理解与索引。

3. **适用场景**
- 希望快速集成官方 AI SDK 并规范代码结构的前端或全栈开发者。
- 需要使用 Claude Code 进行高效编程辅助的终端用户。
- 致力于构建符合 MCP 标准的 AI 应用架构的技术团队。
- 需要让 LLM 更好地读取和理解项目文档以进行自动化处理的场景。

4. **技术亮点**
- 统一了多种 AI 开发标准（SDK、MCP、llms.txt），降低了多工具集成的复杂度。
- 专注于 TypeScript 生态，适合现代 Web 和 Node.js 环境下的 AI 应用开发。
- 链接: https://github.com/kitforai/kitforai
- ⭐ 59 | 🍴 2 | 语言: TypeScript

### Guido
- ### 1. 中文简介
Guido 是一款基于本地 RAG（检索增强生成）技术的景区智能导览 AI 数字人系统。该项目采用 Spring Boot 后端、Vue 3 前端及 UniApp 移动端框架，旨在为游客提供高效、个性化的智慧旅游服务体验。

### 2. 核心功能
*   **智能导览问答**：利用本地 RAG 技术，基于景区知识库提供准确的景点介绍与问答服务。
*   **AI 数字人交互**：集成 AI 数字人形象，通过 SSE（服务器发送事件）实现流畅的多模态实时交互。
*   **跨平台应用支持**：同时支持 Web 端（Vue 3）和移动端（UniApp），满足多终端访问需求。
*   **全栈架构部署**：后端使用 Java (Spring Boot) 处理业务逻辑，MySQL 存储数据，确保系统稳定性。

### 3. 适用场景
*   **智慧旅游景区**：为大型景区提供 7x24 小时的智能客服与自动导览服务。
*   **博物馆/展览馆**：辅助讲解员进行展品深度介绍与互动问答。
*   **文旅宣传平台**：作为线上虚拟导游，提升游客在行前或行中的互动体验。

### 4. 技术亮点
*   **本地化 RAG 架构**：结合 Java 生态与检索增强生成技术，保障数据隐私的同时提升回答准确性。
*   **实时流式交互**：利用 SSE 技术优化 AI 响应速度，提供类真人的对话延迟体验。
*   **现代前端组合**：采用 Vue 3 + UniApp 技术栈，兼顾开发效率与多端兼容性。
- 链接: https://github.com/youxiandechilun/Guido
- ⭐ 41 | 🍴 1 | 语言: Java
- 标签: ai, digital-human, java, mysql, rag

### generative-media-skills
- ### 1. 中文简介
该项目提供了一系列经研究验证的智能体技能，旨在通过 AI 编程助手实现高质量的图像、视频、音频及语音生成。它专注于提升生成式媒体内容的创作效率与质量，支持多种主流 AI 编码工具。

### 2. 核心功能
- **多模态媒体生成**：支持文本到图像、文本到视频、文本到语音等多种生成式媒体任务的自动化处理。
- **编程助手集成**：深度适配 GitHub Copilot、Cursor、Claude Code 等主流 AI 编程环境，提供即插即用的技能包。
- **研究驱动优化**：基于研究成果设计的提示词工程和智能体策略，确保生成内容的高质量与一致性。
- **全流程媒体制作**：涵盖从创意构思、代码生成到最终音视频合成的完整工作流支持。

### 3. 适用场景
- **快速原型开发**：开发者利用 AI 编程助手快速生成包含多媒体元素的应用程序界面或演示Demo。
- **内容创作者自动化**：自媒体人或营销人员通过自然语言指令自动生成宣传视频、播客音频或社交媒体配图。
- **AI 应用实验**：研究人员或爱好者探索不同智能体框架在复杂媒体生成任务中的表现与最佳实践。

### 4. 技术亮点
- **广泛的兼容性**：同时支持 OpenAI Codex、Anthropic Claude、GitHub Copilot 等多个头部 AI 平台，打破工具壁垒。
- **结构化技能设计**：将复杂的媒体生成任务封装为可复用的“技能”模块，便于在智能体工作流中灵活调用。
- 链接: https://github.com/calesthio/generative-media-skills
- ⭐ 37 | 🍴 3 | 语言: Python
- 标签: agent, agentic-ai, ai, ai-audio, ai-video

### awesome-gemini-cli-subagents
- **1. 中文简介**
这是一个精选的列表，包含51个可直接投入生产使用的Gemini CLI子代理（subagents）。用户只需将这些代理文件放入 `.gemini/agents/` 目录下，即可让Gemini自动委派任务给相应的专业专家。该项目旨在通过模块化分工提升AI编程助手的效率和专业化水平。

**2. 核心功能**
*   提供51个经过筛选的生产级子代理集合。
*   支持简单的目录挂载式配置，即插即用。
*   实现任务自动委派，让主模型调用特定领域的专家代理。
*   涵盖多种开发领域，如代码生成、调试、文档编写等。
*   基于Shell脚本构建，易于集成到现有的Gemini CLI工作流中。

**3. 适用场景**
*   希望在不更换主LLM的情况下，增强Gemini CLI在特定编程任务上的专业能力。
*   开发者需要自动化处理重复性高或专业性强的代码审查与重构任务。
*   团队希望通过标准化的子代理模板来统一AI辅助开发的输出风格和质量。
*   研究人员或爱好者想要探索多代理（Multi-Agent）系统在命令行工具中的应用模式。

**4. 技术亮点**
*   **模块化架构**：采用“主代理+子代理”的分治策略，便于维护和扩展。
*   **开箱即用**：无需复杂的环境配置，仅需放置文件即可生效。
*   **提示工程优化**：每个子代理都针对特定任务进行了专门的Prompt工程优化，以提高准确率。
- 链接: https://github.com/JosephHampton/awesome-gemini-cli-subagents
- ⭐ 36 | 🍴 0 | 语言: Shell
- 标签: agentic-ai, agents, ai, ai-agents, awesome

### awesome-zk-ai
- 描述: using agents to monitor proving training and inference techniques
- 链接: https://github.com/mimoo/awesome-zk-ai
- ⭐ 21 | 🍴 2 | 语言: HTML

### atrio
- 描述: A small self-hosted guest lounge for your AI persona — friends chat via one-time links; you only ever see the AI-written visit summary. CC BY 4.0.
- 链接: https://github.com/29-Cu/atrio
- ⭐ 15 | 🍴 1 | 语言: JavaScript
- 标签: ai, ai-persona, chatbot, express, privacy

### ai-runtime-security-sandbox
- 描述: Live RAG chatbot security demo — prompt injection, tool abuse, excessive agency
- 链接: https://github.com/TatarinBlack/ai-runtime-security-sandbox
- ⭐ 9 | 🍴 6 | 语言: Python

### relay-status-monitor
- 描述: 自托管的 AI API 中转站状态监控面板，支持 SUB2API / New API、余额与延迟采集、模型测速、可用率统计及飞书告警。
- 链接: https://github.com/yigehaozi/relay-status-monitor
- ⭐ 9 | 🍴 3 | 语言: TypeScript
- 标签: ai-api, api-monitoring, new-api, nextjs, openai-api

### trading-terminal
- 描述: Terminal - Built using Claude Code (Fable 5) as Part of AI Bootcamp 2.0
- 链接: https://github.com/marketcalls/trading-terminal
- ⭐ 8 | 🍴 3 | 语言: TypeScript
- 标签: claude-code, fable-5, fastapi, react, sqlite

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81750 | 🍴 15251 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目旨在为开发者提供丰富的实战案例和参考代码。它被标记为“Awesome”列表，是学习人工智能技术的优质资源库。

2. **核心功能**
- 提供500个完整的AI项目示例代码，覆盖主流算法与应用。
- 分类清晰，明确区分机器学习、深度学习、计算机视觉和NLP四大板块。
- 集成Python语言实现，便于直接运行和学习代码逻辑。
- 作为综合性资源库，帮助学习者快速构建AI项目经验。

3. **适用场景**
- AI初学者通过阅读和运行代码，快速掌握机器学习与深度学习基础。
- 开发者寻找特定任务（如图像识别或文本分类）的代码模板以加速开发。
- 教育者或培训师使用该资源库作为教学案例，讲解不同AI技术的应用。

4. **技术亮点**
- 项目数量庞大且分类全面，提供了从基础到高级的完整学习路径。
- 标注为“awesome”社区精选资源，确保了代码质量和实用性的高标准。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35372 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33217 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。通过统一模型格式，开发者可以更灵活地在多种平台和工具间部署AI应用。

### 2. 核心功能
*   **跨框架模型转换**：支持在PyTorch、TensorFlow、Keras等主流框架之间无缝转换模型架构和权重。
*   **标准化模型定义**：提供统一的算子库和数据格式规范，确保模型在不同环境下的兼容性。
*   **高效推理部署**：配合ONNX Runtime等执行引擎，实现跨平台的高性能模型推理加速。
*   **生态系统集成**：广泛兼容Scikit-learn及各类硬件加速器，简化从训练到生产部署的流程。

### 3. 适用场景
*   **多框架混合开发**：在项目中结合使用PyTorch进行实验性研究，同时利用TensorFlow或Keras进行特定模块的训练。
*   **边缘设备部署**：将大型云端训练的模型转换为轻量级ONNX格式，以便在移动设备、嵌入式系统或IoT设备上高效运行。
*   **模型协作与分享**：团队内部或跨组织间交换经过验证的模型文件，避免因框架差异导致的复现困难。
*   **硬件加速优化**：针对特定GPU、NPU或FPGA硬件，利用ONNX作为中间表示层进行底层性能调优。

### 4. 技术亮点
*   **开放中立标准**：由微软、Facebook等科技巨头共同发起并维护，避免了单一厂商的技术锁定。
*   **丰富的算子支持**：覆盖卷积、循环神经网络、注意力机制等绝大多数现代深度学习结构。
*   **动态形状支持**：允许模型处理可变长度的输入数据，提升了在实际应用中的灵活性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21134 | 🍴 3965 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
该项目是一本关于机器学习工程实践的开源“开放书籍”，全面涵盖了从底层基础设施到上层模型应用的工程细节。内容聚焦于大规模语言模型（LLM）的训练、推理及调试等关键环节，旨在为工程师提供系统性的技术指导。

2. **核心功能**
*   提供大规模分布式训练框架（如 PyTorch、Slurm）的配置与优化指南。
*   深入解析大语言模型在推理阶段的性能调优与资源管理策略。
*   涵盖 GPU 集群管理、网络通信优化及存储系统设计等基础设施工程实践。
*   详细介绍模型调试技巧、可观测性构建及 MLOps 流水线的设计模式。
*   整合了可扩展性设计原则，帮助应对海量数据和高并发请求的工程挑战。

3. **适用场景**
*   需要从零搭建或优化大规模 LLM 训练集群的数据科学家和 MLOps 工程师。
*   致力于降低推理成本并提升服务延迟的生产环境后端开发人员。
*   希望系统化掌握深度学习基础设施（GPU、网络、存储）运维知识的团队。
*   正在探索如何将传统机器学习流程迁移至现代大模型工程架构的研究者。

4. **技术亮点**
*   **实战导向**：不仅理论丰富，更侧重于解决真实生产环境中遇到的具体工程痛点（如 OOM 调试、网络瓶颈）。
*   **前沿覆盖**：紧跟 LLM 时代潮流，专门针对 Transformers 库、PyTorch 分布式训练等最新技术栈提供最佳实践。
*   **全链路视角**：打通了从硬件底层（GPU/Slurm）到软件层（框架/代码）再到业务层（训练/推理）的完整知识体系。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18378 | 🍴 1173 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17302 | 🍴 2115 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13128 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11571 | 🍴 907 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10664 | 🍴 5709 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理领域的AI实战项目合集。该项目提供了完整的代码实现，旨在帮助开发者快速掌握相关技术并构建实际应用。

2. **核心功能**
*   收录大量涵盖主流AI子领域（如CV、NLP、ML）的完整代码项目。
*   提供结构化的项目索引，便于用户按技术领域快速查找资源。
*   包含从基础到进阶的多种难度级别的实战案例，适合不同阶段的学习者。
*   作为“Awesome”系列资源， curated 了高质量且经过验证的开源AI项目。

3. **适用场景**
*   AI初学者希望寻找大量可运行的代码示例以加深理论理解。
*   开发者在需要快速原型开发时，参考现有项目的架构和实现逻辑。
*   研究人员或学生用于追踪当前机器学习与深度学习领域的热门开源项目。

4. **技术亮点**
*   极高的社区认可度（35k+星标），证明了其内容的丰富性和实用性。
*   标签分类清晰，全面覆盖人工智能的核心分支，是一站式学习资源库。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35372 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和调试模型结构。该项目由 JavaScript 驱动，具备轻量级且跨平台的特点。

2. **核心功能**
*   支持 ONNX、TensorFlow、PyTorch、Keras、CoreML 等主流格式的模型可视化。
*   提供清晰的层结构视图，便于深入理解模型内部逻辑与数据流向。
*   兼容桌面端与 Web 端，用户可通过浏览器直接加载并查看模型文件。
*   支持 Safetensors 等新兴格式，保持对最新技术栈的广泛兼容性。

3. **适用场景**
*   在部署前调试和优化复杂的深度学习模型架构。
*   向非技术人员或团队其他成员直观展示 AI 模型的工作原理。
*   快速检查不同框架间模型转换后的结构一致性。
*   学习和研究各类神经网络模型的层级组成与连接方式。

4. **技术亮点**
*   基于 Web 技术实现，无需安装重型依赖即可跨平台运行。
*   拥有极高的 GitHub 星标数（33k+），证明其在社区中广泛的认可度和活跃度。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33217 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了至关重要的速查手册集合。内容涵盖了从基础数学工具到主流框架的核心代码片段与概念解析，旨在帮助开发者快速回顾和查阅关键技术点。

2. **核心功能**
*   提供深度学习领域必备的概念与算法速查表。
*   涵盖 Python 科学计算库（如 NumPy、SciPy、Matplotlib）的高效用法指南。
*   包含主流深度学习框架（如 Keras）的代码示例与最佳实践。
*   整理机器学习研究中的关键数学公式与统计知识。
*   以结构化的文档形式呈现，便于快速检索和离线阅读。

3. **适用场景**
*   研究人员在构建模型时快速回顾特定算法或函数的参数用法。
*   数据科学家在数据分析过程中查找 Pandas、NumPy 等库的操作技巧。
*   学生或初学者学习深度学习基础概念时的辅助参考资料。
*   工程师在进行代码审查或调试时，快速确认框架 API 的标准实现方式。

4. **技术亮点**
*   内容整合了 Medium 上高赞文章的精华，具有较高的实用价值和权威性。
*   标签覆盖全面，兼顾了底层数学库与高层应用框架，形成完整的技术栈参考。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近 200 个实战案例与项目，并提供免费配套教材，旨在帮助零基础用户入门并实现就业实战。该项目涵盖 Python、数学基础、机器学习、数据分析、深度学习、计算机视觉及自然语言处理等热门技术领域。

### 2. 核心功能
- 提供从零基础到就业的全流程 AI 学习路径规划。
- 收录近 200 个精选实战案例与开源项目供练习。
- 配套提供免费的学习教材和资源文档。
- 覆盖 Python、PyTorch、TensorFlow 等主流框架及算法库。
- 整合数学基础、数据分析、CV、NLP 等关键技能模块。

### 3. 适用场景
- **AI 初学者**：希望系统构建知识体系，从零开始学习人工智能的学生或转行者。
- **求职备战者**：需要丰富项目经验以应对面试，寻求高质量实战案例的求职者。
- **技能提升者**：希望查漏补缺，系统性复习数学、机器学习或深度学习理论的从业者。
- **课程设计参考**：教育机构或讲师寻找结构化的教学大纲和实战素材。

### 4. 技术亮点
- **资源集成度高**：一站式整合了从基础数学到前沿深度学习（如 PyTorch/TensorFlow 2.x）的全栈学习资料。
- **实战导向强**：不仅包含理论，更强调通过 200+ 实际项目代码进行动手实践，直接对接就业需求。
- **社区热度高**：拥有超过 1.3 万星标的活跃社区支持，证明其内容质量和广泛认可度。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13128 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 项目名称：Ludwig

1. **中文简介**
   Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他 AI 模型的构建过程。它通过声明式配置让数据科学家和开发者能够专注于业务逻辑，而无需编写大量底层代码。

2. **核心功能**
   - 支持低代码方式快速构建和训练深度学习模型及大语言模型。
   - 提供广泛的预置组件，涵盖计算机视觉、自然语言处理及结构化数据任务。
   - 兼容主流深度学习后端（如 PyTorch），并集成 Llama、Mistral 等流行 LLM 的微调能力。
   - 强调以数据为中心的开发流程，简化从数据准备到模型评估的全链路操作。

3. **适用场景**
   - **快速原型开发**：希望在无需深入底层架构的情况下，迅速验证 AI 模型想法。
   - **LLM 微调与应用**：针对特定领域对 Llama 或 Mistral 等大模型进行高效微调和部署。
   - **多模态 AI 项目**：需要同时处理图像、文本或表格数据的综合性机器学习任务。

4. **技术亮点**
   - 采用声明式 YAML/JSON 配置文件定义模型结构，极大降低了深度学习的使用门槛。
   - 内置自动化超参数调整和数据预处理管道，提升了模型开发的效率与一致性。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11736 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9132 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8926 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6244 | 🍴 740 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
该项目是一个全面且实用的中文自然语言处理（NLP）工具库，集成了敏感词检测、语言识别及丰富的中英文词典资源。它提供了从基础文本处理到高级知识图谱构建、情感分析及语音处理的多种预训练模型和数据集，旨在降低NLP开发门槛。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、繁简体转换、中英文姓名/性别推断及各类实体（手机号、身份证、邮箱）抽取。
*   **丰富词库与资源**：内置大量垂直领域词库（如医疗、法律、汽车）及成语、古诗词、停用词等，支持词汇情感分析和同反义词查询。
*   **NLP模型与算法**：集成BERT、GPT-2等预训练模型的微调代码，涵盖命名实体识别（NER）、文本分类、序列标注及关键词抽取。
*   **语音与多模态**：包含中文语音识别（ASR）工具、发音预测模块及手写汉字识别能力，支持音频数据增强。
*   **知识图谱与问答**：提供知识图谱构建工具、关系抽取方法及基于不同数据源（如百度知道、医疗数据）的问答系统实现。

3. **适用场景**
*   **内容安全审核**：用于互联网平台的敏感词过滤、谣言检测及违规内容自动识别。
*   **智能客服与对话系统**：基于现有语料库和对话模型，快速搭建具备闲聊或特定领域问答能力的聊天机器人。
*   **信息抽取与结构化**：从非结构化文本（如新闻、简历、法律文书）中自动提取关键实体、关系及摘要。
*   **NLP算法研究与教学**：作为学习中文NLP技术、复现经典算法或获取基准数据集（Benchmark）的资源仓库。

4. **技术亮点**
*   **一站式资源聚合**：不仅包含代码实现，还整合了大量高质量的中文数据集、预训练模型及垂直领域词典，极大节省数据收集成本。
*   **前沿技术集成**：紧跟NLP发展潮流，收录了BERT、ALBERT、RoBERTa等主流预训练模型的具体应用案例及微调模板。
*   **实用工具链完整**：覆盖了从数据清洗、标注、模型训练到评估的全流程，提供了如OCR、语音对齐、文本可视化等辅助工具。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81750 | 🍴 15251 | 语言: Python

### LlamaFactory
- ### 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目旨在简化大模型的微调流程，使其更加高效和易用。

### 2. **核心功能**
*   **多模型支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100+ 主流开源模型。
*   **高效微调算法**：集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调技术。
*   **多范式训练**：支持监督微调（SFT）、奖励模型训练（RM）及人类反馈强化学习（RLHF）。
*   **量化部署友好**：提供 4-bit/8-bit 量化训练与推理支持，降低硬件门槛。
*   **可视化交互**：内置 Web UI 和命令行工具，简化数据准备与训练监控过程。

### 3. **适用场景**
*   **垂直领域微调**：快速为医疗、法律或金融等专业领域定制专用语言模型。
*   **资源受限环境**：在显存有限的消费级 GPU 上通过 QLoRA 等技术进行大模型适配。
*   **多模态应用开发**：训练具备图像理解能力的视觉语言模型（VLM），用于图文分析任务。
*   **对齐优化实验**：利用 RLHF/DPO 等技术优化模型输出，使其更符合人类价值观和安全标准。

### 4. **技术亮点**
*   **统一架构设计**：基于 Transformers 库构建，提供标准化接口以屏蔽不同模型间的差异。
*   **ACL 2024 认可**：作为学术研究成果落地，具备严谨的方法论支持和性能基准验证。
*   **全链路支持**：涵盖从数据预处理、模型训练到量化导出和 API 部署的全流程工具链。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73181 | 🍴 8941 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目汇集了从 Anthropic、OpenAI、Google 及 xAI 等主流厂商的大型语言模型中提取的系统提示词（System Prompts）。内容涵盖 Claude、ChatGPT、Gemini 及 Cursor 等多种模型的最新配置，并定期更新以保持时效性。

2. **核心功能**
*   提取并公开多个知名 AI 模型（如 Claude、GPT、Gemini）的底层系统指令。
*   覆盖广泛的技术生态，包括通用聊天机器人、代码助手及特定领域的专用模型。
*   通过 JavaScript 实现解析或存储逻辑，并提供结构化的数据访问方式。
*   保持高频更新，追踪各大厂商对模型系统配置的迭代变化。

3. **适用场景**
*   **提示词工程研究**：分析顶级模型的底层指令结构，优化自定义 Prompt 的设计策略。
*   **安全与隐私审计**：研究系统提示词如何影响模型行为，评估潜在的越狱风险或安全边界。
*   **AI 代理开发**：参考官方系统的角色设定和约束条件，构建更稳定、可控的智能体（Agents）。
*   **教学与科普**：作为生成式 AI 内部机制的教学案例，展示大型语言模型的工作原理。

4. **技术亮点**
*   **跨厂商全面覆盖**：同时整合了 Anthropic、OpenAI、Google 和 xAI 四大巨头的数据，具有极高的信息密度。
*   **动态更新机制**：针对快速迭代的 AI 领域，提供定期更新的系统提示词库，确保数据的现时性。
*   **开源社区驱动**：依托 GitHub 平台积累的高关注度（5万+星标），形成活跃的社区贡献与维护生态。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 56481 | 🍴 9332 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. 中文简介
该项目是一套为期12周、包含24节课的全面人工智能入门课程，旨在让所有人都能轻松掌握AI知识。它由微软发起，通过结构化的学习计划引导用户从零开始构建AI技能树。

### 2. 核心功能
*   **系统化课程体系**：涵盖从基础概念到深度学习模型的完整学习路径。
*   **多模态技术覆盖**：深入讲解机器学习、计算机视觉、NLP及生成式AI等核心领域。
*   **交互式学习体验**：主要采用Jupyter Notebook形式，支持代码即时运行与实验。
*   **开源免费资源**：完全公开的教学材料，适合自学者和教师直接使用。
*   **微软背书与支持**：作为“Microsoft for Beginners”系列的一部分，提供高质量且权威的技术指导。

### 3. 适用场景
*   **初学者入门学习**：适合无AI背景的用户建立对人工智能的整体认知。
*   **高校或培训机构教学**：可作为计算机科学或数据科学课程的补充教材或实践指南。
*   **开发者技能拓展**：帮助已有编程基础的开发者快速上手现代AI开发流程。
*   **企业内训参考**：用于团队内部普及AI基础知识，提升整体技术视野。

### 4. 技术亮点
*   **前沿技术栈集成**：结合CNN、RNN、GAN等经典与现代深度学习架构进行实战演示。
*   **低代码门槛实践**：利用Jupyter Notebook降低代码执行复杂度，侧重逻辑理解而非繁琐配置。
*   **全栈AI覆盖**：不仅限于传统机器学习，还延伸至自然语言处理和计算机视觉等热门领域。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52150 | 🍴 10548 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- ### GitHub 项目分析报告：ailearning

**1. 中文简介**
该项目是一个涵盖数据分析、机器学习实战、线性代数基础以及 PyTorch 和 TensorFlow 2 等主流深度学习框架的综合学习资源库。它结合了 NLTK 自然语言处理工具与 Scikit-learn 等传统机器学习库，提供了从理论到代码实现的完整教程。内容广泛覆盖了从基础算法到高级神经网络的各种案例。

**2. 核心功能**
*   **全栈算法实现**：包含回归、分类（如 SVM、逻辑回归）、聚类（如 K-Means、DBSCAN）及推荐系统等经典机器学习算法的代码实战。
*   **深度学习框架集成**：深入讲解并演示基于 TensorFlow 2 和 PyTorch 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）及卷积神经网络的应用。
*   **自然语言处理专题**：利用 NLTK 进行文本预处理，并结合深度学习模型解决 NLP 任务。
*   **数学基础强化**：通过代码实例解释线性代数在机器学习中的关键作用，辅助理解算法背后的数学原理。
*   **特征工程与降维**：提供 PCA、SVD 等数据降维技术以及 AdaBoost、FP-Growth 等特定算法的实现与分析。

**3. 适用场景**
*   **机器学习初学者入门**：适合希望系统掌握从统计学习到深度学习全流程知识的编程学习者。
*   **高校课程辅助教材**：可作为计算机或数据科学相关专业学生理解复杂算法原理的实战参考。
*   **算法工程师技能复习**：帮助从业者快速回顾和验证各类经典及前沿机器学习模型的标准实现。
*   **数据分析项目预研**：为需要快速原型开发的数据分析团队提供经过验证的代码模板和最佳实践。

**4. 技术亮点**
*   **理论与实践深度融合**：不仅提供代码，还强调线性代数等数学基础对算法理解的支撑作用。
*   **多框架并行支持**：同时覆盖 Scikit-learn 传统机器学习与 PyTorch/TF2 现代深度学习两大生态，适应不同技术栈需求。
*   **全面覆盖主流算法**：标签显示其涵盖了从关联规则挖掘（Apriori）到集成学习（AdaBoost）再到序列建模（LSTM）的广泛算法类型。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42372 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38048 | 🍴 6353 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35372 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33736 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28495 | 🍴 3470 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25873 | 🍴 2916 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，并附带完整代码实现。该项目旨在为开发者提供一个全面的实践指南，涵盖从基础到高级的各种算法与应用案例。

2. **核心功能**
- 提供涵盖机器学习、深度学习和NLP等领域的500多个实战项目代码。
- 包含计算机视觉相关的图像处理与识别项目实例。
- 所有项目均配有可运行的代码，便于直接学习和复现。
- 按领域分类整理，方便用户快速定位感兴趣的技术方向。

3. **适用场景**
- 初学者希望系统性地学习AI核心概念并通过代码加深理解。
- 开发者寻找特定算法（如CNN、RNN、Transformer）的工程实现参考。
- 学生或研究人员需要高质量的项目案例用于课程设计或论文灵感。
- 团队进行技术选型或原型开发时，快速验证相关AI技术的可行性。

4. **技术亮点**
- 内容极其丰富，覆盖了当前主流AI领域的几乎所有关键子方向。
- 强调“代码即学习”，提供直接可用的工程级示例而非纯理论。
- 作为Awesome List类项目，具有极高的社区认可度和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35372 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一个利用人工智能自动化基于浏览器的复杂工作流平台。它通过集成计算机视觉和大语言模型（LLM），能够像人类一样理解网页界面并执行操作，从而实现端到端的任务自动化。

**2. 核心功能**
*   **AI 驱动交互**：结合视觉模型与 LLM，实时识别网页元素并规划操作路径。
*   **跨框架兼容**：底层支持 Playwright、Puppeteer 和 Selenium，灵活适配不同自动化需求。
*   **RPA 增强能力**：超越传统规则型 RPA，具备处理非结构化页面布局和动态内容的智能决策能力。
*   **API 化部署**：提供简洁的 API 接口，便于轻松集成到现有的业务系统或工作流引擎中。

**3. 适用场景**
*   **企业级数据录入**：自动在多个异构网站间复制粘贴信息，替代繁琐的人工数据迁移。
*   **电商价格监控**：定期抓取竞争对手商品价格及库存状态，并触发预警或自动下单。
*   **自动化测试流程**：模拟真实用户行为进行 UI 测试，快速发现前端页面变更导致的故障。
*   **政务/金融表单填报**：处理需要登录、验证码识别及复杂表单填写的合规性业务流程。

**4. 技术亮点**
*   **多模态感知**：不仅解析 HTML DOM，更通过“看”屏幕来定位按钮和输入框，解决了动态渲染页面的痛点。
*   **自适应导航**：无需预先编写固定选择器，AI 能根据页面视觉布局自动适应新的界面结构。
*   **开源生态整合**：充分利用 Python 社区成熟的浏览器自动化库，降低了集成和维护成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22202 | 🍴 2081 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台，提供开源、云及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API接口。

2. **核心功能**
*   支持图像、视频及3D点云等多种数据格式的自动化与半自动化标注。
*   内置AI辅助标注功能，可大幅提升数据标注的效率与准确性。
*   提供完善的质量控制机制与团队协作工具，确保数据集标准统一。
*   开放开发者API，便于集成到现有的机器学习工作流中。

3. **适用场景**
*   构建用于目标检测或语义分割的大规模高质量训练数据集。
*   团队协同进行视频行为分析或自动驾驶场景的数据标注工作。
*   需要快速原型验证或生产级部署的企业级视觉AI项目。

4. **技术亮点**
*   支持PyTorch和TensorFlow等主流深度学习框架的数据生态。
*   具备从开源社区到企业级服务的灵活扩展能力。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16266 | 🍴 3741 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具，旨在帮助开发者理解模型决策依据。它广泛支持CNN、Vision Transformers等架构，涵盖分类、检测、分割及图像相似度等多种任务。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种主流可视化算法。
*   兼容卷积神经网络（CNN）和视觉Transformer（ViT）架构。
*   适用于图像分类、目标检测、语义分割及图像相似度检索等多种任务。
*   提供直观的热力图可视化，增强深度学习模型的透明度。

3. **适用场景**
*   调试计算机视觉模型，定位误判原因并优化特征提取层。
*   医疗影像分析中辅助医生理解AI诊断依据，提升临床信任度。
*   自动驾驶或安防系统中验证目标检测模型对关键区域的关注点。
*   学术论文研究或教学中展示深度学习模型的内部注意力机制。

4. **技术亮点**
*   高度模块化设计，轻松适配不同深度学习框架与自定义网络结构。
*   统一接口支持多种XAI（可解释人工智能）算法，便于横向对比分析。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12914 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了可微分的图像处理工具，旨在简化计算机视觉模型的开发与集成。该项目致力于将传统的几何视觉算法与现代深度学习框架无缝结合。

2. **核心功能**
*   提供全套可微分的传统计算机视觉算子，支持自动求导。
*   深度集成 PyTorch 生态系统，便于在神经网络中直接调用视觉预处理和后处理步骤。
*   包含丰富的几何变换、相机校准及三维重建相关工具。
*   支持高性能的图像增强和数据增强操作，加速模型训练流程。
*   提供模块化且易于扩展的 API，适用于从研究到生产环境的多种需求。

3. **适用场景**
*   需要端到端可微分流水线的深度学习计算机视觉项目。
*   机器人领域中的空间感知、SLAM（同步定位与建图）及运动规划研究。
*   对图像进行实时几何校正、增强或特征提取的工业应用。
*   将传统几何约束整合进神经网络的混合架构开发。

4. **技术亮点**
*   **全可微分性**：所有核心算子均支持梯度反向传播，允许将传统 CV 步骤作为神经网络层进行联合优化。
*   **PyTorch 原生兼容**：完全基于 PyTorch Tensor 实现，无需额外转换数据格式，性能优异。
*   **开源社区活跃**：获得 Hacktoberfest 等社区活动支持，拥有良好的文档和持续的功能迭代。
- 链接: https://github.com/kornia/kornia
- ⭐ 11271 | 🍴 1199 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3281 | 🍴 402 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2625 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2427 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### LibreCode
- 1. **中文简介**
LibreCode 是一个基于 C# 开发的开源代码逆向与分析接口工具。它旨在提供类似 Cursor 的 AI 编程体验，同时集成反编译和代码还原功能，帮助用户高效处理二进制文件或混淆代码。该项目结合了 AI 智能代理与传统的逆向工程技术，为开发者提供强大的代码理解能力。

2. **核心功能**
*   **AI 驱动的代码生成与分析**：集成 Ollama 等本地大模型，支持自然语言交互式的代码编写与解释。
*   **高级反编译引擎**：能够将二进制文件或 IL 代码还原为可读的 C# 源代码，便于理解闭源逻辑。
*   **智能逆向辅助**：提供自动化的代码重构、变量命名修复及依赖关系梳理，降低逆向工程门槛。
*   **Cursor 式交互界面**：模拟现代 AI IDE 的操作流，实现代码编辑、调试与 AI 建议的无缝衔接。
*   **本地化隐私保护**：支持离线运行，确保敏感代码数据不出本地环境，保障企业级安全合规。

3. **适用场景**
*   **遗留系统维护**：分析无源码或文档缺失的老旧 C# 应用，快速理解业务逻辑并修复 Bug。
*   **恶意软件分析**：安全研究人员利用其逆向能力拆解可疑程序，提取关键行为特征进行威胁情报分析。
*   **商业软件学习**：开发者通过反编译优秀闭源库，学习其设计模式与算法实现以优化自身代码。
*   **代码审计与合规检查**：在内部审查中快速识别代码中的安全隐患、许可证冲突或违规调用。

4. **技术亮点**
*   **多模态 AI 集成**：巧妙结合本地 LLM 的强大推理能力与传统静态分析技术，提升代码还原准确率。
*   **高性能逆向架构**：针对 .NET 生态优化，支持大规模代码库的快速解析与索引构建。
*   **开源协作生态**：依托活跃的社区贡献，持续更新支持最新的 .NET 版本与 AI 模型接口。
- 链接: https://github.com/re4/LibreCode
- ⭐ 1059587 | 🍴 0 | 语言: C#
- 标签: ai, ai-agents, coding, csharp, decompiler

### openclaw
- ### 1. 中文简介
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，采用独特的“龙虾”风格运行。它强调数据所有权与隐私，让用户能够完全掌控自己的 AI 体验。

### 2. 核心功能
*   **跨平台兼容**：支持在任何主流操作系统和硬件平台上部署运行。
*   **数据私有化**：强调“Own Your Data”，确保用户数据的安全性与自主权。
*   **个性化定制**：提供高度可配置的个人助理功能，适应不同用户需求。
*   **开源透明**：基于 TypeScript 开发，代码开放，便于社区贡献与审查。

### 3. 适用场景
*   **注重隐私的个人用户**：希望拥有完全可控、不依赖云端的本地 AI 助手。
*   **开发者与技术爱好者**：喜欢折腾开源项目，希望在多种环境下部署自定义 AI 的人。
*   **小型团队内部工具**：需要轻量级、可私有化部署的知识助手或自动化代理。

### 4. 技术亮点
*   **TypeScript 构建**：利用现代 JavaScript 生态的优势，保证类型安全与开发效率。
*   **模块化架构**：标签中的 "crustacean"（甲壳类）和 "molty" 暗示其可能具有独特且灵活的内部处理机制。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382667 | 🍴 80308 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 252785 | 🍴 22566 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一个能够随用户共同成长和进化的智能代理助手。它深度整合了主流的大语言模型（如 Anthropic 的 Claude 和 OpenAI 的 ChatGPT），旨在通过自然语言交互提供高效、个性化的辅助体验。该项目致力于打破传统 AI 工具的局限，实现更灵活、更具适应性的自动化工作流。

### 2. 核心功能
*   **多模型无缝集成**：支持调用 Claude、ChatGPT 等多种前沿 LLM 后端，灵活切换以适配不同任务需求。
*   **动态学习与进化**：具备根据用户习惯和历史交互进行自我优化和适应能力，实现“越用越懂你”的效果。
*   **智能代码辅助**：结合 Codex 等代码生成能力，提供精准的编程建议、代码审查及自动化脚本编写功能。
*   **自然语言交互界面**：通过直观的聊天式界面降低使用门槛，让用户无需复杂配置即可启动复杂任务。

### 3. 适用场景
*   **高级开发者辅助**：在复杂编码场景中作为智能结对程序员，快速生成模块、调试错误或重构代码。
*   **个性化知识助手**：用于日常信息查询、文档摘要或特定领域知识检索，建立个人专属的知识库。
*   **自动化工作流执行**：替代重复性手动操作，如数据整理、邮件回复或跨平台信息同步。

### 4. 技术亮点
*   **架构开放性**：采用模块化设计，轻松接入 Nous Research、OpenClaw 等开源社区的前沿模型与工具链。
*   **高性能响应机制**：针对 LLM 推理延迟进行优化，确保在长时间交互中保持流畅的用户体验。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 213507 | 🍴 39529 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 以下是针对 GitHub 项目 **n8n** 的技术分析：

1. **中文简介**
   n8n 是一款具备原生 AI 能力的公平代码（fair-code）工作流自动化平台，支持可视化构建与自定义代码开发。它提供超过 400 种集成方式，并允许用户选择自托管或云服务部署模式。该平台旨在通过低代码/无代码工具简化复杂的业务流程自动化。

2. **核心功能**
   *   **原生 AI 集成**：内置 AI 节点，支持 LLM 调用、向量数据库检索及智能代理工作流。
   *   **混合开发模式**：结合可视化拖拽界面与 TypeScript 自定义代码节点，兼顾易用性与灵活性。
   *   **广泛生态系统**：提供 400+ 种预建集成连接器，覆盖主流 SaaS 应用、API 及数据库。
   *   **灵活部署选项**：支持自托管（Self-hosted）以保障数据隐私，也可使用云端服务快速启动。
   *   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，增强与大模型上下文交互的能力。

3. **适用场景**
   *   **企业级数据同步**：自动在不同 SaaS 平台（如 Salesforce 到 Slack）之间同步客户数据和通知。
   *   **AI 驱动的内容生成**：利用 LLM 自动生成营销文案、摘要或代码，并通过工作流自动分发到社交媒体或 CMS。
   *   **内部 IT 自动化**：自动化处理员工入职流程、IT 工单响应或服务器监控告警。
   *   **私有化数据中台构建**：在本地环境中整合多个内部数据库和 API，构建统一的数据处理管道而不泄露敏感数据。

4. **技术亮点**
   *   **基于 TypeScript 构建**：拥有优秀的类型安全和开发者体验，便于社区贡献和定制开发。
   *   **公平代码许可证**：采用 Sustainable Use License，允许免费用于内部业务，但禁止直接作为竞品销售。
   *   **MCP 客户端/服务端实现**：率先支持 MCP 标准，使工作流能更无缝地连接和控制大型语言模型的工具使用。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196143 | 🍴 59269 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185488 | 🍴 46106 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165506 | 🍴 21427 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164194 | 🍴 30538 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156974 | 🍴 46171 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151744 | 🍴 9662 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

