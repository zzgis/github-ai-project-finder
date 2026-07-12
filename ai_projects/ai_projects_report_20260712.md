# GitHub AI项目每日发现报告
日期: 2026-07-12

## 新发布的AI项目

### ai-content-kb
- ### 1. **中文简介**
该项目提出了一种“审查优先”的参考架构，旨在构建辅助个人内容知识管理的AI系统。它强调在自动化处理之前引入人工审核机制，以确保生成内容的准确性与可靠性。这是一种针对个人知识库场景的前沿设计思路。

### 2. **核心功能**
*   采用审查优先（Review-first）机制，确保AI生成内容经过人工验证后才入库。
*   提供个人内容知识系统的参考架构设计，指导开发者构建稳健的知识库。
*   支持AI辅助功能，提升个人知识整理、检索和总结的效率。
*   强调数据质量与安全，通过人机协作模式降低AI幻觉带来的风险。

### 3. **适用场景**
*   需要高准确度个人笔记或文档管理的用户，避免AI错误信息干扰。
*   研究人员或专业人士构建私有知识库，要求内容经过严格审核。
*   开发个人AI助手应用时，寻求可靠的知识管理架构参考。
*   对隐私和数据安全性有较高要求的个人知识管理系统建设。

### 4. **技术亮点**
*   创新性地引入“审查优先”范式，平衡了AI效率与人类判断的准确性。
*   作为参考架构（Reference Architecture），为复杂系统提供结构化的设计指导。
*   专注于个人领域（Personal Domain），解决通用AI在个性化知识管理中的一致性难题。
- 链接: https://github.com/mrbear1024/ai-content-kb
- ⭐ 74 | 🍴 5 | 语言: 未知

### kitforai
- 1. **中文简介**
kitforai 是面向 AI 开发者的综合工具包与枢纽，提供了官方 SDK、Claude Code 插件以及 MCP（Model Context Protocol）配置支持。该项目还包含标准的 `llms.txt` 文件，旨在简化 AI 应用的集成与开发流程。

2. **核心功能**
*   提供官方的 TypeScript SDK，方便开发者快速构建 AI 应用。
*   内置 Claude Code 插件，增强代码编辑器的 AI 辅助能力。
*   支持 MCP 协议配置，实现模型与外部数据源的标准化连接。
*   包含 `llms.txt` 元数据文件，优化模型对仓库文档的理解与索引。

3. **适用场景**
*   需要快速集成 AI 能力并遵循标准协议的全栈 TypeScript 项目开发。
*   希望利用 MCP 协议打通不同 AI 模型与本地数据源连接的工程师。
*   致力于优化 Claude Code 编辑器体验以提升编码效率的开发团队。
*   需要为 AI 模型提供标准化文档索引以改善检索效果的项目维护者。

4. **技术亮点**
*   采用现代 TypeScript 生态，兼顾类型安全与开发体验。
*   前瞻性支持 MCP（Model Context Protocol），顺应 AI 工具互联的新标准。
*   通过 `llms.txt` 实现对仓库内容的结构化声明，提升大模型理解精度。
- 链接: https://github.com/kitforai/kitforai
- ⭐ 58 | 🍴 2 | 语言: TypeScript

### generative-media-skills
- 1. **中文简介**
本项目提供经过研究验证的智能体技能，旨在增强各类AI编程助手生成高质量图像、视频、音频及语音的能力。它专注于通过提示工程优化，实现跨平台的生成式媒体内容生产。

2. **核心功能**
*   支持图像生成与视频生成的自动化处理流程。
*   集成文本转语音（TTS）及音频生成能力。
*   兼容多种主流AI编程助手，如Claude、Cursor和GitHub Copilot。
*   提供针对生成式媒体优化的提示词工程技能包。

3. **适用场景**
*   开发者希望在IDE中直接利用AI生成营销所需的宣传图片或短视频。
*   内容创作者希望快速将脚本转化为配音或动态视觉素材。
*   AI应用开发者需要集成成熟的媒体生成逻辑以扩展助手功能。

4. **技术亮点**
*   强调“研究背书”的技能设计，确保生成效果的专业性与稳定性。
*   广泛的工具链兼容性，无缝对接当前流行的多种AI编码环境。
- 链接: https://github.com/calesthio/generative-media-skills
- ⭐ 33 | 🍴 2 | 语言: Python
- 标签: agent, agentic-ai, ai, ai-audio, ai-video

### Guido
- 1. **中文简介**
Guido 是一个基于 Spring Boot、Vue 3 和 UniApp 开发的景区智能导览系统。该项目引入了本地 RAG（检索增强生成）技术与 AI 数字人，旨在为游客提供精准且交互友好的个性化游览服务。

2. **核心功能**
*   集成 AI 数字人形象，提供可视化的智能交互体验。
*   利用本地 RAG 技术实现景区知识的精准检索与生成式问答。
*   采用 Vue 3 和 UniApp 构建跨平台前端，支持多端访问。
*   基于 Spring Boot 搭建后端服务，确保系统稳定运行。

3. **适用场景**
*   旅游景区的智能语音与视频导览服务。
*   博物馆或展览馆的数字化参观助手。
*   大型园区内的个性化路线规划与信息咨询。

4. **技术亮点**
*   **本地 RAG 架构**：结合向量数据库实现离线或私有化部署的知识检索，保障数据隐私与响应速度。
*   **全栈现代化组合**：前后端分离架构（Vue 3 + Spring Boot），并利用 SSE（Server-Sent Events）支持流式数据传输。
*   **跨平台兼容**：通过 UniApp 实现一套代码多端运行，降低开发与维护成本。
- 链接: https://github.com/youxiandechilun/Guido
- ⭐ 21 | 🍴 1 | 语言: Java
- 标签: ai, digital-human, java, mysql, rag

### awesome-gemini-cli-subagents
- 1. **中文简介**
这是一个精选了 51 个可直接投入生产使用的 Gemini CLI 子智能体集合。用户只需将这些智能体文件放入 `.gemini/agents/` 目录，即可让 Gemini 自动委派任务给相应的专家模块。该列表旨在通过模块化方式增强 Gemini CLI 的专业处理能力。

2. **核心功能**
*   提供 51 个经过筛选的生产就绪级子智能体。
*   支持通过简单的目录配置实现智能体的即插即用。
*   允许主模型自动委派特定任务给专业的子代理。
*   涵盖编码、提示工程及开发者工具等多个领域。
*   作为“Awesome List”促进 AI 智能体生态的标准化使用。

3. **适用场景**
*   需要增强 Gemini CLI 特定领域能力（如代码生成或调试）的开发人员。
*   希望利用模块化架构优化 AI 工作流的团队或个人。
*   探索 Google Gemini 多智能体协作模式的技术爱好者。
*   寻求现成专家代理以简化复杂任务处理的初级 AI 用户。

4. **技术亮点**
该项目采用 Shell 脚本编写，实现了轻量级且易于集成的智能体部署方案，通过结构化的目录管理降低了多智能体系统的配置门槛。
- 链接: https://github.com/JosephHampton/awesome-gemini-cli-subagents
- ⭐ 21 | 🍴 0 | 语言: Shell
- 标签: agentic-ai, agents, ai, ai-agents, awesome

### awesome-zk-ai
- 描述: using agents to monitor proving training and inference techniques
- 链接: https://github.com/mimoo/awesome-zk-ai
- ⭐ 16 | 🍴 2 | 语言: HTML

### atrio
- 描述: A small self-hosted guest lounge for your AI persona — friends chat via one-time links; you only ever see the AI-written visit summary. CC BY 4.0.
- 链接: https://github.com/29-Cu/atrio
- ⭐ 15 | 🍴 0 | 语言: JavaScript
- 标签: ai, ai-persona, chatbot, express, privacy

### ai-runtime-security-sandbox
- 描述: Live RAG chatbot security demo — prompt injection, tool abuse, excessive agency
- 链接: https://github.com/TatarinBlack/ai-runtime-security-sandbox
- ⭐ 9 | 🍴 6 | 语言: Python

### relay-status-monitor
- 描述: 自托管的 AI API 中转站状态监控面板，支持 SUB2API / New API、余额与延迟采集、模型测速、可用率统计及飞书告警。
- 链接: https://github.com/yigehaozi/relay-status-monitor
- ⭐ 9 | 🍴 2 | 语言: TypeScript
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
- ⭐ 81747 | 🍴 15251 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，所有项目均附带完整代码实现。该项目旨在为开发者提供从入门到实战的全面学习素材，涵盖主流人工智能领域的经典与前沿应用。

2. **核心功能**
*   提供大量经过验证的AI相关项目代码，涵盖机器学习、深度学习等多个细分领域。
*   专注于计算机视觉和自然语言处理（NLP）等热门方向的实战案例展示。
*   作为“Awesome”列表， curated 精选高质量项目，方便用户快速定位所需资源。
*   支持Python等主流编程语言，便于开发者直接运行、学习和二次开发。

3. **适用场景**
*   AI初学者希望通过实际代码案例快速理解并掌握机器学习基础概念。
*   工程师需要寻找特定任务（如图像识别或文本分类）的参考实现以加速开发进程。
*   研究人员希望跟踪计算机视觉和NLP领域的最新开源项目和技术趋势。

4. **技术亮点**
*   极高的社区关注度（35,368+星标），证明了其内容的广泛认可度和实用性。
*   标签体系完善，清晰划分了人工智能、数据科学及各类具体技术方向，便于精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35368 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架生成的模型文件，能够直观地展示模型结构并进行数据流分析，帮助开发者快速理解复杂模型的内部架构。

2. **核心功能**
- 广泛支持 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite 等主流模型格式的解析与可视化。
- 提供清晰的节点连接图和层级结构视图，便于追踪数据在模型中的流动路径。
- 支持本地文件和远程 URL 直接加载，无需安装复杂的依赖环境即可使用。
- 具备交互式的缩放、平移及节点详情查看功能，方便深入分析特定层或算子。
- 开源且跨平台，可通过 Web 浏览器或桌面应用程序运行，访问便捷。

3. **适用场景**
- 模型调试阶段，用于检查网络结构是否正确构建及数据维度是否匹配。
- 学术交流或技术分享中，将复杂的神经网络结构转化为直观的图表进行展示。
- 跨框架迁移时，验证不同后端（如从 PyTorch 转换到 ONNX）后的模型一致性。
- 教学演示，帮助初学者直观理解卷积神经网络、Transformer 等复杂架构的工作原理。

4. **技术亮点**
- 基于 JavaScript 开发，实现了极高的兼容性和轻量化部署能力，无需后端服务器支持。
- 对 safetensors 等新兴高效模型格式提供了即时支持，紧跟 AI 生态发展步伐。
- 界面简洁现代，专注于模型结构本身，避免了冗余信息的干扰，提升了阅读效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33217 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。

2. **核心功能**
*   支持在PyTorch、TensorFlow、Keras等主流框架间进行模型互转。
*   提供统一的计算图表示，实现跨平台部署和推理加速。
*   包含完整的工具链，用于模型验证、优化及性能分析。
*   维护开放的规范文档，确保不同厂商实现的兼容性。

3. **适用场景**
*   需要将训练好的模型从PyTorch迁移到支持ONNX的硬件加速器上运行。
*   希望避免被单一深度学习框架锁定，提高模型部署的灵活性。
*   需要在不同开发环境之间共享经过优化的深度学习模型。
*   进行跨平台的模型性能基准测试和优化工作。

4. **技术亮点**
*   作为行业通用标准，被Microsoft、Facebook、AWS等主要科技公司广泛支持。
*   通过ONNX Runtime实现高性能、低延迟的跨设备推理执行。
- 链接: https://github.com/onnx/onnx
- ⭐ 21133 | 🍴 3963 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书籍》是一本全面覆盖机器学习工程实践的综合指南。内容涵盖从模型训练、调试到大规模部署及推理优化的全流程最佳实践。该项目旨在为开发者提供构建可扩展、高效ML系统的实用参考。

2. **核心功能**
- 提供基于PyTorch和Transformers的大规模语言模型（LLM）训练与微调指南。
- 深入解析GPU硬件、网络通信及存储系统对ML工作负载的影响与优化策略。
- 介绍使用Slurm等调度器在超算集群上进行分布式训练的工程实践。
- 详述模型推理加速、量化技术及高并发部署的最佳实践。
- 包含机器学习系统的调试技巧、监控方法及可观测性工具链介绍。

3. **适用场景**
- 需要在大规模集群上训练或微调大型语言模型（如LLaMA、GPT系列）的工程团队。
- 希望优化深度学习模型推理延迟并降低GPU资源成本的MLOps工程师。
- 正在搭建或维护企业级机器学习基础设施，需了解存储与网络调优的开发人员。
- 学习如何调试复杂分布式训练任务及解决OOM（内存溢出）问题的研究人员。

4. **技术亮点**
- 聚焦于“工程落地”而非纯算法理论，强调实际生产环境中的性能瓶颈解决。
- 内容紧跟前沿技术，涵盖当前热门的LLM训练与推理优化最新进展。
- 结构清晰，按ML生命周期模块化组织，便于按需查阅特定环节的最佳实践。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18376 | 🍴 1173 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17299 | 🍴 2115 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13124 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11572 | 🍴 907 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10664 | 🍴 5709 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的资源库，所有项目均附带完整代码实现。该项目旨在为开发者提供从入门到实战的全面学习素材，涵盖主流人工智能领域的经典与前沿应用。

2. **核心功能**
*   提供大量经过验证的AI相关项目代码，涵盖机器学习、深度学习等多个细分领域。
*   专注于计算机视觉和自然语言处理（NLP）等热门方向的实战案例展示。
*   作为“Awesome”列表， curated 精选高质量项目，方便用户快速定位所需资源。
*   支持Python等主流编程语言，便于开发者直接运行、学习和二次开发。

3. **适用场景**
*   AI初学者希望通过实际代码案例快速理解并掌握机器学习基础概念。
*   工程师需要寻找特定任务（如图像识别或文本分类）的参考实现以加速开发进程。
*   研究人员希望跟踪计算机视觉和NLP领域的最新开源项目和技术趋势。

4. **技术亮点**
*   极高的社区关注度（35,368+星标），证明了其内容的广泛认可度和实用性。
*   标签体系完善，清晰划分了人工智能、数据科学及各类具体技术方向，便于精准检索。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35368 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架生成的模型文件，能够直观地展示模型结构并进行数据流分析，帮助开发者快速理解复杂模型的内部架构。

2. **核心功能**
- 广泛支持 ONNX、PyTorch、TensorFlow、Keras、CoreML、TFLite 等主流模型格式的解析与可视化。
- 提供清晰的节点连接图和层级结构视图，便于追踪数据在模型中的流动路径。
- 支持本地文件和远程 URL 直接加载，无需安装复杂的依赖环境即可使用。
- 具备交互式的缩放、平移及节点详情查看功能，方便深入分析特定层或算子。
- 开源且跨平台，可通过 Web 浏览器或桌面应用程序运行，访问便捷。

3. **适用场景**
- 模型调试阶段，用于检查网络结构是否正确构建及数据维度是否匹配。
- 学术交流或技术分享中，将复杂的神经网络结构转化为直观的图表进行展示。
- 跨框架迁移时，验证不同后端（如从 PyTorch 转换到 ONNX）后的模型一致性。
- 教学演示，帮助初学者直观理解卷积神经网络、Transformer 等复杂架构的工作原理。

4. **技术亮点**
- 基于 JavaScript 开发，实现了极高的兼容性和轻量化部署能力，无需后端服务器支持。
- 对 safetensors 等新兴高效模型格式提供了即时支持，紧跟 AI 生态发展步伐。
- 界面简洁现代，专注于模型结构本身，避免了冗余信息的干扰，提升了阅读效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33217 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- ### 1. 中文简介
该项目为深度学习与机器学习研究人员提供了 essential 的速查手册（Cheat Sheets），涵盖从基础理论到高级框架的实用知识。它整合了 Keras、Matplotlib、NumPy、SciPy 等常用库的关键语法和技巧，旨在帮助开发者快速查阅和解决编码问题。

### 2. 核心功能
- 提供深度学习与机器学习领域的关键概念速查表。
- 包含 NumPy、SciPy 等数值计算库的高效用法指南。
- 汇总 Matplotlib 数据可视化的常用代码片段。
- 集成 Keras 等深度学习框架的操作速记。
- 以简洁文档形式呈现，便于快速检索和打印参考。

### 3. 适用场景
- 研究人员在编写论文或实验代码时快速回顾算法细节。
- 工程师在调试模型时查阅特定库（如 NumPy/Keras）的函数用法。
- 初学者整理学习笔记，建立系统化的 ML/DL 知识体系。
- 团队内部进行技术分享或新人入职培训的资料参考。

### 4. 技术亮点
- 高度浓缩的知识点展示，极大提升了查阅效率。
- 覆盖主流 AI 工具链，兼顾基础数学库与高级深度学习框架。
- 社区认可度高（15k+ 星标），内容经过广泛验证且持续更新。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13124 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型、神经网络及其他人工智能模型的构建过程。它通过声明式配置降低开发门槛，让开发者无需编写大量底层代码即可快速训练和评估模型。该项目特别强调数据为中心的开发理念，支持从传统机器学习到深度学习的全流程。

**2. 核心功能**
*   提供声明式的配置接口，用户只需定义输入输出和数据路径即可启动训练。
*   内置多种预置模型架构，自动处理特征工程及模型训练中的常见步骤。
*   广泛支持主流深度学习框架（如 PyTorch），并兼容表格数据、图像、文本等多种数据类型。
*   具备完善的实验跟踪与模型评估功能，便于对比不同配置下的模型表现。
*   支持微调（Fine-tuning）现有大型语言模型（如 LLaMA、Mistral），适配特定业务需求。

**3. 适用场景**
*   **快速原型开发**：数据科学家希望在不深入底层代码的情况下，快速验证机器学习或深度学习假设。
*   **结构化/表格数据分析**：针对传统 Tabular 数据进行分类、回归或聚类任务，替代复杂的 Scikit-learn 流水线配置。
*   **多模态应用构建**：需要同时处理文本、图像等混合类型数据的多模态 AI 模型开发。
*   **LLM 微调服务**：企业希望低成本地对开源大语言模型进行领域适应，而不需从头训练基础模型。

**4. 技术亮点**
*   **极低的学习曲线**：通过 YAML 配置文件即可驱动复杂模型训练，显著减少样板代码。
*   **数据中心设计**：专注于数据处理管道和特征工程的自动化，提升数据质量对模型性能的影响效率。
*   **灵活的扩展性**：允许用户在保留核心流程的同时，轻松插入自定义组件或损失函数。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11734 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9131 | 🍴 1236 | 语言: Python
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
funNLP 是一个全面且庞大的中文自然语言处理资源仓库，涵盖了从基础工具（如敏感词检测、分词、情感分析）到高级模型（如 BERT、知识图谱构建）的广泛内容。它集成了丰富的语料库、数据集、开源项目及实用脚本，旨在为开发者提供一站式的中英 NLP 解决方案和学习资料。该项目不仅是开发者的工具箱，也是了解中文 NLP 领域最新动态和最佳实践的重要资源中心。

2. **核心功能**
- **基础 NLP 工具**：提供敏感词过滤、中英文语言检测、姓名性别推断、手机号/身份证/邮箱抽取及繁简转换等实用功能。
- **数据与语料库**：包含大量中文专用资源，如中日文人名库、行业词库（汽车、医学、法律等）、情感词典、停用词表及各类问答和对话数据集。
- **预训练模型与算法**：汇聚了 BERT、ERNIE、ALBERT 等主流预训练模型的中文变体，以及命名实体识别（NER）、关系抽取、文本摘要等任务的代码实现。
- **语音与 OCR 支持**：集成中文语音识别（ASR）、语音情感分析、中文手写汉字识别及文档表格 OCR 提取等多媒体处理资源。
- **知识图谱与应用**：提供知识图谱构建工具、实体链接库、多领域问答系统（医疗、金融、闲聊）及对话机器人框架的资源汇总。

3. **适用场景**
- **智能客服与聊天机器人开发**：利用其中的对话语料、意图识别模型和闲聊机器人代码，快速搭建具备语义理解能力的客服系统。
- **内容审核与安全合规**：通过敏感词库、暴恐词表及反动词表，构建高效的文本过滤系统，适用于社交媒体、论坛或新闻平台的内容监管。
- **企业级信息抽取与分析**：借助 NER 模型、关系抽取工具和行业词库，从非结构化文本（如新闻、病历、法律文书）中提取关键实体和业务洞察。
- **NLP 研究与教学参考**：作为学生和研究人员的学习资料库，获取最新的数据集、基准测试任务（Benchmark）及前沿算法的复现代码。

4. **技术亮点**
- **资源极度丰富且垂直细分**：不仅提供通用工具，还深入垂直领域（如医疗、法律、金融），提供了高度专业化的词库和标注数据。
- **紧跟前沿技术栈**：全面整合了 Transformer 架构下的最新中文预训练模型（如 ELECTREA, ALBERT-Chinese）及相应的微调代码。
- **全链路支持**：覆盖了从数据预处理、特征工程、模型训练到后处理（如文本纠错、摘要生成）的自然语言处理完整生命周期。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81747 | 🍴 15251 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大语言模型（LLM）及视觉语言模型（VLM）进行微调。该项目曾获 ACL 2024 收录，旨在简化大规模模型的适配流程，提供从指令微调到强化学习对齐的一站式解决方案。

2. **核心功能**
*   支持 100+ 种主流 LLM 和 VLM 的统一高效微调。
*   集成 LoRA、QLoRA 等参数高效微调（PEFT）技术及量化策略。
*   提供完整的指令微调（Instruction Tuning）与 RLHF（基于人类反馈的强化学习）支持。
*   兼容 Transformers 库，降低用户接入和使用门槛。

3. **适用场景**
*   研究人员或开发者需要对多种不同架构的大模型进行快速基准测试和微调实验。
*   企业希望在资源受限环境下（如使用量化技术），低成本部署定制化的垂直领域大模型。
*   需要同时对文本生成模型和多模态视觉语言模型进行训练和优化的场景。

4. **技术亮点**
*   **高度统一性**：通过统一接口屏蔽了不同模型底层实现的差异，实现“一次配置，多处运行”。
*   **极致效率**：原生支持 QLoRA 等先进量化微调技术，显著降低显存占用并提升训练速度。
*   **前沿算法集成**：内置最新的前沿微调算法，包括 DPO、PPO 等 RLHF 变体，紧跟学术与工业界最佳实践。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73174 | 🍴 8940 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目收集并泄露了Anthropic、OpenAI、Google及xAI等主流厂商的大型语言模型系统提示词（System Prompts）。内容涵盖Claude、ChatGPT、Gemini等多个版本及衍生产品，并定期更新。旨在为研究人员和开发者提供这些模型底层指令的内部结构参考。

2. **核心功能**
*   聚合来自多家头部AI公司（如Anthropic、OpenAI、Google）的系统提示词数据。
*   覆盖多种模型版本及特定应用（如Claude Code、Cursor、VS Code等）的提示词细节。
*   定期同步和更新最新泄露或公开的提示词内容，保持数据时效性。
*   以结构化形式呈现原始提示文本，便于直接阅读和分析。

3. **适用场景**
*   **提示词工程研究**：分析顶级模型的指令遵循逻辑，优化自身Prompt设计。
*   **安全与红队测试**：了解模型底层限制和安全护栏，进行对抗性测试或漏洞挖掘。
*   **AI模型逆向学习**：通过对比不同厂商的提示词策略，理解模型行为差异。
*   **教育与科普**：作为生成式AI内部机制的教学案例，揭示“黑盒”中的部分逻辑。

4. **技术亮点**
*   **多源整合**：一次性汇总分散在各大科技巨头旗下的多个关键模型提示词。
*   **高关注度**：拥有超过5.6万星标，表明其在AI社区中具有极高的实用价值和影响力。
*   **持续维护**：项目保持高频更新，紧跟模型迭代速度，确保信息的现时有效性。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 56386 | 🍴 9311 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### 1. 中文简介
“AI-For-Beginners”是一个由微软推出的为期12周、包含24节课的人工智能通识课程，旨在让所有背景的人都能轻松入门AI。该项目通过Jupyter Notebook的形式，系统性地覆盖了从基础概念到深度学习的高级主题。其目标是降低人工智能的学习门槛，普及AI知识。

### 2. 核心功能
*   **结构化课程体系**：提供12周、24节课的完整学习路径，适合循序渐进地掌握AI知识。
*   **交互式代码练习**：基于Jupyter Notebook构建，支持用户边学边练，实时运行代码验证理解。
*   **涵盖主流AI技术**：内容广泛涉及机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等热门领域。
*   **零基础友好设计**：专为初学者打造，语言通俗易懂，无需深厚的数学或编程背景即可开始学习。
*   **开源免费资源**：完全公开且免费，任何人都可以访问并利用这些材料进行自我提升或教学参考。

### 3. 适用场景
*   **高校与培训机构教学**：作为计算机科学或相关专业的入门教材，用于系统性地教授AI基础概念。
*   **职场人士技能转型**：希望进入人工智能领域的非技术人员，利用业余时间快速建立AI认知框架。
*   **个人兴趣自学**：对AI充满好奇的爱好者，希望通过动手实践深入了解机器学习原理及应用。
*   **企业内训基础模块**：科技公司用于员工AI素养普及，确保团队成员具备统一的基础知识水平。

### 4. 技术亮点
*   **微软官方背书与社区支持**：由Microsoft For Beginners系列出品，拥有极高的GitHub星标数（超5万），表明其内容质量和社区认可度极高。
*   **全栈AI知识覆盖**：不仅限于传统机器学习，还深入讲解了RNN、CNN、GAN等现代深度学习架构，内容紧跟技术前沿。
*   **实践导向的教学模式**：强调“做中学”，通过大量的代码示例和笔记本文件，帮助用户将理论转化为实际操作能力。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52142 | 🍴 10548 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个全面的人工智能学习资源库，涵盖数据分析与机器学习的实战案例、线性代数基础以及PyTorch和TensorFlow 2等深度学习框架的应用。它整合了NLTK自然语言处理工具，旨在通过理论结合实践的方式，帮助学习者掌握从传统算法到深度神经网络的核心技能。

2. **核心功能**
*   提供涵盖线性回归、逻辑回归、SVM等经典算法的完整代码实现与原理讲解。
*   深入解析深度学习模型，包括RNN、LSTM、DNN及卷积神经网络的构建与训练。
*   集成自然语言处理（NLP）实战，利用NLTK和TF2进行文本分析与处理。
*   包含推荐系统、聚类算法（如K-Means、Apriori）及降维技术（PCA、SVD）的具体应用案例。
*   基于Scikit-learn和PyTorch框架，提供标准化的机器学习工程化代码模板。

3. **适用场景**
*   计算机相关专业学生或初学者进行机器学习与深度学习入门学习。
*   数据科学家用于快速查阅经典算法（如Adaboost、Naive Bayes）的实现细节。
*   开发人员寻找NLP任务（如文本分类、情感分析）的工程化参考代码。
*   企业团队在构建推荐系统或用户行为分析模型时的算法选型参考。

4. **技术亮点**
*   技术栈覆盖全面，同时支持传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）。
*   注重理论与实践结合，不仅包含算法推导，更提供可运行的实战代码。
*   社区认可度高，拥有超过4万星标，是中文互联网环境下高质量的AI学习开源项目。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42373 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38011 | 🍴 6345 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35368 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33736 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28487 | 🍴 3469 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25871 | 🍴 2916 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI项目的代码合集，涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。该项目为开发者提供了丰富的实战案例，旨在帮助学习者快速掌握各类人工智能技术的落地应用。

2. **核心功能**
*   汇集大量现成的AI项目代码，支持机器学习、深度学习、CV及NLP等多方向学习。
*   提供完整的代码实现，方便用户直接运行、调试及参考算法逻辑。
*   作为资源索引库，帮助用户系统化地梳理不同AI子领域的典型应用场景。

3. **适用场景**
*   AI初学者进行系统性实战练习，通过阅读和运行代码深入理解基础算法。
*   研究人员寻找特定领域（如目标检测或文本分类）的参考实现以加速实验进程。
*   开发者在构建新项目时，借鉴现有代码结构或模型架构以提高开发效率。

4. **技术亮点**
*   **资源丰富度极高**：收录多达500个项目，覆盖面广，是目前GitHub上极具规模的AI项目集合之一。
*   **社区认可度高**：拥有超过3.5万颗星标，证明其在开源社区中的广泛影响力和实用价值。
*   **多领域整合**：在一个仓库内整合了从传统机器学习到前沿深度学习的多种技术栈，便于横向对比学习。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35368 | 🍴 7348 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一个基于人工智能的自动化平台，能够模拟人类操作来执行基于浏览器的复杂工作流。它利用先进的计算机视觉和大语言模型技术，实现无需编写代码即可自动处理网页交互任务。该项目旨在成为传统 RPA 工具的智能替代方案，显著提升浏览器自动化的效率和灵活性。

### 2. 核心功能
*   **智能页面理解**：结合视觉识别与大语言模型（LLM），精准解析网页布局、文本及动态元素。
*   **自然语言驱动**：用户只需输入自然语言指令，系统即可自动生成并执行相应的浏览器操作步骤。
*   **自适应自动化**：能够应对网页结构变化或加载延迟等不稳定因素，具备较强的容错和重试机制。
*   **API 集成能力**：提供标准化的 API 接口，便于将其无缝嵌入到现有的业务流程或自动化系统中。
*   **多浏览器支持**：底层兼容 Playwright 等技术，支持在多种主流浏览器环境中运行自动化任务。

### 3. 适用场景
*   **跨平台数据录入**：自动登录多个不同网站后台，批量查询、提取或填写表单数据。
*   **电子商务监控**：定期抓取竞品价格、库存状态或促销活动信息，并生成分析报告。
*   **内部流程自动化**：自动化处理 HR、财务或 IT 支持中涉及的多步骤网页审批与配置操作。
*   **市场情报收集**：从新闻网站、社交媒体或论坛中自动采集特定关键词相关的内容并进行分类。

### 4. 技术亮点
Skyvern 的核心创新在于将“计算机视觉”与“大语言模型”深度结合，使其不仅能像传统脚本一样定位元素，更能像人类一样“看懂”页面意图，从而解决传统自动化工具在面对非标准化或动态网页时脆弱性高的问题。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22199 | 🍴 2081 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉AI数据集的领先平台，提供开源、云及企业级产品与标注服务。它支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作及开发者API等功能。

2. **核心功能**
*   支持图像、视频及3D数据的多维度智能标注。
*   提供AI辅助标注以提升效率并具备质量保证机制。
*   内置团队协作功能及完善的开发者API接口。
*   涵盖数据分析与报告生成能力以优化数据集。

3. **适用场景**
*   构建用于目标检测或语义分割的高质量训练数据集。
*   团队协同进行大规模图像或视频的自动化标注任务。
*   需要集成自定义算法或API的深度学习项目预处理阶段。

4. **技术亮点**
*   采用Python开发，兼容PyTorch和TensorFlow等主流深度学习框架。
*   支持多种标注格式（如Bounding Box、Semantic Segmentation），适配ImageNet等标准数据集。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16265 | 🍴 3741 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### 1. 中文简介
该项目是一个先进的计算机视觉可解释性工具库，旨在增强模型决策的透明度。它广泛支持卷积神经网络（CNN）和视觉Transformer等多种架构，涵盖分类、目标检测及图像分割等任务。

### 2. 核心功能
*   全面支持Grad-CAM、Score-CAM及CAM等多种经典的类激活映射算法。
*   兼容CNN与Vision Transformers（ViT）等主流深度学习架构。
*   适用于图像分类、目标检测、语义分割及图像相似度计算等多种任务。
*   提供直观的可视化功能，帮助用户理解模型关注的图像区域。

### 3. 适用场景
*   **模型调试与优化**：通过可视化分析模型误判原因，辅助改进网络结构或数据预处理。
*   **医疗影像分析**：在诊断辅助中直观展示病灶区域，提升医生对AI建议的信任度。
*   **自动驾驶安全验证**：验证车辆识别系统是否关注正确的物体特征而非背景噪声。
*   **学术研究教学**：作为解释黑盒模型内部机制的标准化工具，用于可解释人工智能研究。

### 4. 技术亮点
*   高度模块化设计，支持自定义模型架构，无需修改原始训练代码即可集成。
*   统一接口封装多种XAI（可解释AI）算法，降低不同技术的使用门槛。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12915 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，旨在为深度学习和机器人应用提供可微分的图像处理工具。该项目致力于将传统的计算机视觉技术与现代深度学习框架无缝融合。

2. **核心功能**
*   提供完全可微分的几何计算机视觉算子，支持端到端的深度学习训练。
*   集成丰富的图像预处理和后处理模块，优化数据处理流程。
*   包含针对机器人和自动驾驶场景优化的空间变换与投影工具。
*   与 PyTorch 生态深度兼容，便于集成到现有的神经网络架构中。

3. **适用场景**
*   **自动驾驶系统开发**：用于车辆感知模块中的实时图像处理和几何推理。
*   **机器人视觉导航**：辅助机器人通过视觉信息进行环境理解和路径规划。
*   **可微分图形学应用**：构建需要反向传播几何约束的深度生成模型或渲染管线。
*   **学术研究与原型验证**：快速实验结合了传统 CV 几何知识与深度学习的混合模型。

4. **技术亮点**
*   **可微分性**：作为其最大特色，Kornia 允许传统的几何操作参与梯度回传，这是纯 PyTorch 原生操作难以直接实现的。
*   **高性能实现**：底层代码经过优化，利用 GPU 加速实现高效的批量图像处理。
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

### openclaw
- 描述: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382644 | 🍴 80305 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 252631 | 🍴 22556 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **项目名称：** hermes-agent

**1. 中文简介**
Hermes-Agent 是一个能够伴随用户共同成长并适应其工作流的智能代理系统。它旨在通过持续的交互与学习，为用户提供个性化、高精度的技术支持与自动化服务。该项目结合了先进的语言模型能力，致力于成为开发者日常工作中不可或缺的得力助手。

**2. 核心功能**
*   **自适应成长机制**：代理具备随使用时间推移而优化自身表现的能力，逐步适应用户的具体需求。
*   **多模型兼容支持**：底层架构支持多种大型语言模型（如 Anthropic 的 Claude、OpenAI 等），确保灵活性与稳定性。
*   **智能代码辅助**：集成类似 Codex 或 Claude Code 的功能，提供高效的代码生成、调试及重构建议。
*   **上下文感知对话**：能够理解复杂的长程对话背景，提供连贯且准确的自然语言交互体验。
*   **高度可定制化**：允许用户根据特定场景调整代理的行为模式、知识范围及响应风格。

**3. 适用场景**
*   **复杂软件开发**：用于需要深度上下文理解和长期记忆的项目，帮助开发者维护大型代码库。
*   **个性化工作流自动化**：适合希望将重复性任务自动化，并依赖特定个人偏好进行配置的专业人士。
*   **高级技术问答与研究**：在需要结合最新 AI 模型能力进行深度技术探讨或代码审查的场景中作为辅助工具。

**4. 技术亮点**
*   **混合架构设计**：巧妙融合了 OpenClaw 的框架优势与 Nous Research 的研究成果，实现了性能与效率的平衡。
*   **前沿模型集成**：直接对接最新的 LLM 接口（包括 Moltbot、ClawdBot 等变体），确保技术栈的先进性。
*   **开源社区驱动**：拥有极高的社区关注度（逾 21 万星标），表明其在 AI Agent 领域具有广泛的影响力和验证过的可靠性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 213401 | 🍴 39491 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. 中文简介
n8n 是一个公平代码开源的工作流自动化平台，原生集成 AI 能力，支持通过可视化构建与自定义代码相结合的方式设计流程。它提供超过 400 种集成方式，并允许用户选择自托管或云端部署。

### 2. 核心功能
- **混合自动化模式**：结合可视化拖拽操作与自定义代码编写，兼顾易用性与灵活性。
- **丰富的集成生态**：内置 400 多种连接器，轻松对接各类 API 和服务。
- **原生 AI 支持**：深度整合人工智能能力，实现智能工作流处理。
- **灵活部署选项**：支持自托管以保障数据隐私，或采用便捷的云服务模式。

### 3. 适用场景
- **企业系统集成**：连接 CRM、ERP 和邮件系统等内部工具，实现数据自动同步。
- **AI 驱动的业务流程**：利用大模型自动处理客户咨询、内容生成或数据分析任务。
- **开发者效率提升**：通过自定义代码节点快速解决复杂逻辑，替代传统低代码限制。

### 4. 技术亮点
- 基于 TypeScript 开发，具备类型安全和良好的可扩展性。
- 标签涵盖 MCP（Model Context Protocol）客户端与服务端支持，适应最新 AI 交互标准。
- 定位为 iPaaS（集成平台即服务），在低代码/无代码领域提供强大的工作流引擎。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196120 | 🍴 59265 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让用户能够轻松使用并在此基础上构建应用。其使命是提供必要的工具，使用户能够将精力集中在真正重要的事务上。

### 2. **核心功能**
*   支持多种大型语言模型（LLM），包括 OpenAI GPT、Claude 和 Llama API。
*   具备自主代理（Autonomous Agents）能力，可独立规划并执行复杂任务。
*   提供 agentic AI 框架，允许开发者构建和定制智能体工作流。
*   旨在通过自动化工具降低 AI 使用门槛，提升开发效率。

### 3. **适用场景**
*   **自动化工作流执行**：用于自动处理重复性高、步骤繁琐的日常任务或数据整理。
*   **AI 应用原型开发**：开发者利用其 agentic 特性快速搭建基于大模型的智能体应用。
*   **多模型集成实验**：测试不同 LLM（如 GPT 与 Claude）在自主决策场景下的表现差异。

### 4. **技术亮点**
*   兼容主流闭源与开源 LLM 接口，灵活性高。
*   强调“代理”架构，使 AI 不仅能对话，还能主动调用工具完成目标。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185483 | 🍴 46104 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165472 | 🍴 21423 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164194 | 🍴 30537 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156964 | 🍴 46171 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151726 | 🍴 9660 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 149544 | 🍴 8554 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

