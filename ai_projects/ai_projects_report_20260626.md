# GitHub AI项目每日发现报告
日期: 2026-06-26

## 新发布的AI项目

### GITVERSE
- ### GITVERSE 项目分析

**1. 中文简介**
GITVERSE 是一个能够将任意代码库逆向工程转化为构建提示词的工具，它自动生成架构分解、ASCII 蓝图以及供 AI 使用的重建提示。该项目旨在帮助开发者通过结构化的方式理解现有系统，并快速生成用于大语言模型（LLM）的代码重构或迁移指令。

**2. 核心功能**
*   **代码库逆向工程**：自动解析复杂代码结构，将其转换为人类可读的架构视图。
*   **ASCII 蓝图生成**：输出可视化的 ASCII 艺术图表，直观展示模块依赖关系。
*   **AI 就绪提示构建**：生成针对 Claude、OpenAI 等大模型的优化提示词，用于代码重建或分析。
*   **Next.js 前端界面**：提供基于 Next.js 和 Tailwind CSS 的现代 Web 交互体验。
*   **GitHub API 集成**：直接对接 GitHub 仓库，支持从远程代码库获取数据进行分析。

**3. 适用场景**
*   **遗留系统现代化**：在迁移老项目到新技术栈前，快速梳理现有架构并生成迁移提示。
*   **代码审计与学习**：通过可视化蓝图和逆向提示词，深入理解陌生开源项目或第三方库的内部逻辑。
*   **AI 辅助开发工作流**：为 Cursor 等 AI 编程助手提供精确的项目上下文，提高代码生成或重构的准确率。
*   **技术文档自动化**：无需手动编写架构文档，一键生成包含结构分析和重建指南的技术摘要。

**4. 技术亮点**
*   **多模型兼容**：生成的提示词经过优化，可适配 Claude、OpenAI 等多种主流 LLM。
*   **全栈技术组合**：采用 TypeScript + Next.js + Tailwind CSS 构建高性能且美观的分析工具。
*   **提示工程导向**：不仅提供数据，更专注于生成高质量的“Prompt Engineering”产物，直接服务于 AI 工作流。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 110 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### claude-ai-desktop-app
- 描述: free claude code ai github desktop pc windows linux macOS proxy server anthropic free api local llm router nvidia nim openrouter deepseek ollama lm studio vscode extension jetbrains cli terminal coding assistant
- 链接: https://github.com/samuto69/claude-ai-desktop-app
- ⭐ 101 | 🍴 0 | 语言: TypeScript
- 标签: claude-code, claude-code-action, claude-code-api, claude-code-desktop, claude-code-open

### parsehawk
- 描述: Local-first document AI. Run 100% locally by default, with API, CLI, and Web UI.
- 链接: https://github.com/parsehawk/parsehawk
- ⭐ 23 | 🍴 4 | 语言: Python
- 标签: artificial-intelligence, classification, document-ai, document-processing, extraction

### glm-5.2-free-desktop-app
- 1. **中文简介**
该项目提供了一个基于 C# 开发的桌面应用程序，旨在本地运行和集成智谱 AI（Zhipu AI）的 GLM-5.2 大语言模型。它支持通过 Hugging Face 或 GitHub 获取 GGUF 模型，并结合 llama.cpp、Ollama 等工具实现离线推理与 API 访问。此应用专为开发者设计，旨在提供稳定的本地 AI 编码助手及自主代理功能。

2. **核心功能**
*   支持在 Windows、macOS 和 Linux 系统上本地部署 GLM-5.2 系列模型。
*   集成 llama.cpp 和 Ollama 引擎，实现高效的动态 GGUF 模型运行。
*   提供开发者工具接口，支持 API 访问及与 Zcode、Opencode 等生态集成。
*   具备代码辅助与自主代理（Autonomous Agent）能力，处理长上下文任务。

3. **适用场景**
*   需要在无互联网环境下进行代码编写和调试的开发者，以利用本地 GLM 模型。
*   希望构建基于智谱 AI 模型的桌面端 AI 助手或智能体应用的工程师。
*   追求数据隐私和安全，倾向于在本地硬件上运行大语言模型的技术团队。

4. **技术亮点**
*   采用 C# 开发跨平台桌面应用，兼容主流操作系统。
*   支持百万级令牌（1m context window）的长上下文窗口，适用于复杂长程任务。
*   灵活整合 Unsloth 优化技术与多种开源推理后端，提升运行效率。
- 链接: https://github.com/PROGRMGEEK/glm-5.2-free-desktop-app
- ⭐ 20 | 🍴 0 | 语言: C#
- 标签: ai-desktop, desktop-agent, desktop-ai, free-ai-api, free-ai-coding

### deepseek-v4-pro-flash-desktop-app
- ### GitHub项目分析报告：deepseek-v4-pro-flash-desktop-app

**1. 中文简介**
这是一个基于TypeScript开发的桌面应用程序，旨在为用户提供对DeepSeek最新V4 Pro/Flash等大语言模型的本地化访问接口。该项目利用vLLM和Ollama等工具支持本地LLM推理，并结合Hugging Face开源生态，让用户能够便捷地在本地环境中体验包括MoE架构、混合注意力机制在内的先进AI能力。

**2. 核心功能**
*   **本地模型推理支持**：集成vLLM和Ollama，实现DeepSeek大模型在用户本地设备上的高效运行。
*   **前沿架构适配**：优化支持DeepSeek V4系列的混合专家（MoE）、混合注意力及超深层结构。
*   **多平台API接入**：兼容Hugging Face及官方API，提供灵活的模型调用方式。
*   **桌面端交互界面**：提供独立的桌面应用体验，便于日常对话与代码辅助。

**3. 适用场景**
*   **开发者本地调试**：在断网或隐私敏感环境下，利用本地算力快速测试DeepSeek新模型效果。
*   **AI编程辅助**：作为IDE插件或独立工具，为程序员提供基于最新V4模型的代码生成与审查支持。
*   **数据隐私保护需求**：需要在不上传数据至云端的情况下，安全地进行文本处理或知识问答的用户。

**4. 技术亮点**
*   **高性能推理优化**：针对DeepSeek特有的压缩稀疏注意力（CSA）和高度压缩注意力（HCA）架构进行了底层优化，提升推理速度。
*   **超长上下文支持**：原生支持1M tokens的超大上下文窗口，适用于长文档分析与复杂逻辑推理任务。
- 链接: https://github.com/HiyuCat/deepseek-v4-pro-flash-desktop-app
- ⭐ 20 | 🍴 0 | 语言: TypeScript
- 标签: ai-free, deep-seek, deepseek-api, deepseek-app, deepseek-chat

### ai-coding-deals
- 描述: Money-saving guide to AI coding tools: free tiers, discounts, referral credits & open-source alternatives. 省钱指南。
- 链接: https://github.com/codertesla/ai-coding-deals
- ⭐ 19 | 🍴 0 | 语言: Python
- 标签: ai, ai-coding, ai-tools, awesome-list, claude-code

### sw2api
- 描述: Reverse proxy for your ai quota from the SW platform.
- 链接: https://github.com/bgzhang1/sw2api
- ⭐ 16 | 🍴 3 | 语言: Python

### oil-cover
- 描述: 为小红书 AI 工具实操内容生成稳定、干净、精致封面的 Claude / Codex Skill（脚本模式 + Agent 自主执行）
- 链接: https://github.com/oil-oil/oil-cover
- ⭐ 14 | 🍴 3 | 语言: Python

### memlawb
- 描述: Open-source, self-hostable, zero-knowledge memory for AI agents. End-to-end encrypted — the server stores only ciphertext and can't read your agent's memory. Works with any MCP agent .
- 链接: https://github.com/Gitlawb/memlawb
- ⭐ 13 | 🍴 3 | 语言: TypeScript

### go-openlore
- 描述: OpenLore: serve your docs to AI agents over SSH
- 链接: https://github.com/aakarim/go-openlore
- ⭐ 8 | 🍴 0 | 语言: Go

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81453 | 🍴 15245 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34894 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款开源的神经网络、深度学习及机器学习模型可视化工具。它支持广泛的模型格式，帮助用户直观地查看和理解复杂的模型结构。

### 2. 核心功能
- 支持多种主流框架格式，包括 PyTorch、TensorFlow、Keras、ONNX 和 CoreML 等。
- 提供图形化界面展示模型层级、层类型及节点连接关系。
- 支持查看张量形状、权重数值及模型参数详情。
- 兼容桌面端与 Web 端，无需安装即可在线浏览模型。

### 3. 适用场景
- 调试深度学习模型时检查网络结构是否正确构建。
- 向非技术人员或团队展示模型架构以便沟通协作。
- 对比不同框架下转换后的模型一致性（如 PyTorch 转 ONNX）。
- 快速审查大型预训练模型的内部组件分布。

### 4. 技术亮点
- 轻量级且跨平台，基于 Electron 开发，兼顾性能与易用性。
- 广泛支持从传统 ML 到最新大模型（如 Safetensors）的格式解析。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33133 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX 是机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型交换与部署。它允许开发者在不同平台（如 PyTorch、TensorFlow 等）间无缝迁移模型，提升开发效率并降低集成复杂度。

2. **核心功能**
- 定义跨平台的机器学习模型开放标准，支持异构硬件加速推理。
- 提供工具链以将主流框架（如 PyTorch、Keras、Scikit-learn）导出的模型转换为统一格式。
- 支持模型优化、转换及在多种后端引擎上的高效执行与验证。

3. **适用场景**
- 需要将训练好的深度学习模型从开发环境部署到边缘设备或生产服务器时。
- 需要在不同深度学习框架之间迁移模型，以避免供应商锁定。
- 希望利用特定硬件加速器（如 GPU、TPU 或专用 NPU）进行高性能推理的场景。

4. **技术亮点**
- 实现了真正的框架无关性，成为连接训练生态与推理基础设施的桥梁。
- 拥有庞大的社区支持和广泛的框架兼容性，包括 PyTorch、TensorFlow 和 Keras 等。
- 链接: https://github.com/onnx/onnx
- ⭐ 21050 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ml-engineering》是一本关于机器学习工程的开放书籍，旨在为从业者提供系统化的工程实践指南。它涵盖了从底层基础设施到大规模模型训练与推理的全流程关键技术。该项目致力于帮助开发者解决机器学习系统中的可扩展性、调试及运维难题。

2. **核心功能**
- 提供大规模分布式训练（如PyTorch、Slurm集群）的最佳实践与配置详解。
- 深入解析大语言模型（LLM）的优化策略，包括显存管理、加速推理及量化技术。
- 涵盖机器学习工程的基础设施组件，如高性能存储、网络通信及GPU调试技巧。
- 分享MLOps领域的可操作经验，涉及模型部署、监控及生产环境下的可扩展性设计。

3. **适用场景**
- 需要从零搭建或优化大规模GPU集群以进行深度学习模型训练的工程团队。
- 正在实施大语言模型微调（Fine-tuning）或全量训练，面临显存瓶颈和训练效率问题的研究人员。
- 希望提升模型在生产环境中推理速度并降低延迟，同时确保高可用性的AI应用开发者。
- 寻求系统化学习机器学习系统工程知识，以解决数据管道、模型部署及运维复杂性的学生或工程师。

4. **技术亮点**
- 紧密结合前沿的大语言模型技术，提供了针对Transformer架构特有的工程优化方案。
- 内容极具实战导向，不仅涵盖理论，还详细列出了具体的代码配置、命令行工具及故障排查步骤。
- 覆盖范围极广，从底层的硬件交互（SLURM、GPU）到上层的框架应用（PyTorch、Transformers）形成完整闭环。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18175 | 🍴 1153 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2109 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13089 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11525 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10640 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个汇集了500个AI项目（涵盖机器学习、深度学习、计算机视觉和自然语言处理）的资源库，所有项目均附带完整代码实现。该项目旨在为开发者提供从入门到进阶的实践案例，是人工智能领域非常受欢迎的Awesome列表之一。

### 2. 核心功能
*   **海量项目资源**：收录了500多个经过筛选的高质量AI项目，覆盖主流技术领域。
*   **全代码支持**：每个项目均提供可运行的源代码，便于用户直接复现和学习。
*   **多领域覆盖**：全面包含机器学习、深度学习、计算机视觉及自然语言处理四大方向。
*   **分类索引清晰**：通过标签和分类快速定位特定技术栈的项目，提升查找效率。

### 3. 适用场景
*   **初学者入门实践**：适合AI新手通过阅读和运行代码，快速理解基础算法概念。
*   **面试准备与作品集构建**：求职者可利用这些项目完善GitHub简历，展示实际动手能力。
*   **技术选型参考**：开发者可通过对比不同项目的实现方式，评估适合自身业务的技术方案。

### 4. 技术亮点
*   **社区驱动的高质量筛选**：作为“Awesome”系列项目，依靠社区力量持续更新和维护，确保内容的前沿性和实用性。
*   **Python生态为主**：虽然标签未明确指定语言，但此类项目通常基于Python及其主流AI库（如TensorFlow, PyTorch等），具有极高的通用性和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34894 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。

2. **核心功能**
- 支持广泛模型格式，包括 ONNX、PyTorch、TensorFlow、Keras、CoreML 等。
- 提供直观的图形化界面展示神经网络层与张量维度信息。
- 允许用户在浏览器或独立应用中打开本地模型文件进行预览。
- 支持模型调试，帮助开发者检查连接错误和结构问题。

3. **适用场景**
- 深度学习研究人员用于快速理解复杂模型架构。
- 工程师在部署前验证模型转换（如从 PyTorch 转 ONNX）的正确性。
- 初学者通过可视化界面学习不同神经网络层的功能与连接方式。
- 团队内部协作时共享和评审模型设计细节。

4. **技术亮点**
- 纯前端实现（基于 JavaScript），无需后端服务器即可运行。
- 轻量级且跨平台，支持桌面端和网页端直接打开模型。
- 社区活跃，持续更新以支持最新的模型格式和框架特性。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33133 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15411 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13089 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11724 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9117 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8908 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8376 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6188 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81453 | 🍴 15245 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目在 ACL 2024 上被收录，旨在简化从指令微调到强化学习对齐的全流程操作。

**2. 核心功能**
*   支持百余种主流 LLM 和 VLM 模型的统一接入与高效微调。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）策略及量化技术。
*   提供完整的指令微调（Instruction Tuning）及基于人类反馈的强化学习（RLHF）训练管线。
*   兼容 Transformers 库，支持 MoE（混合专家）架构模型及 Agent 开发需求。

**3. 适用场景**
*   研究人员或开发者需要对特定领域数据进行指令微调以定制专业大模型。
*   需要在显存受限环境下，通过 QLoRA 等技术对大型模型进行低成本高效微调。
*   希望利用 RLHF 技术优化模型输出质量，使其更符合人类价值观或特定任务要求。

**4. 技术亮点**
*   **统一架构**：屏蔽了不同模型底层实现的差异，提供一致性的训练接口。
*   **性能优化**：深度整合 PEFT 与量化技术，显著降低微调硬件门槛并提升训练效率。
*   **前沿支持**：紧跟最新模型动态（如 Llama 3, Gemma, DeepSeek 等），并支持多模态 VLM 微调。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72505 | 🍴 8867 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48459 | 🍴 10051 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目汇集了从Anthropic、OpenAI、Google及xAI等主流厂商的大型语言模型中提取的系统提示词，涵盖Claude、GPT、Gemini等多个知名模型版本。内容经过定期更新，旨在为开发者提供最新、最全面的提示词参考库。

2. **核心功能**
- 提取并整理来自多个顶级AI厂商的最新系统提示词。
- 覆盖ChatGPT、Claude、Gemini、Grok等主流模型及代码助手。
- 保持内容定期更新，确保信息的时效性。
- 提供开源共享的提示词数据集供社区研究使用。

3. **适用场景**
- 提示词工程师用于逆向分析大模型的底层指令结构。
- 研究人员探索不同厂商模型的系统级行为差异。
- 开发者优化自定义AI代理（Agent）的系统指令设计。
- 教育领域演示大型语言模型的安全边界与系统约束。

4. **技术亮点**
- 跨厂商覆盖全面，整合了当前市场上最具影响力的AI模型数据。
- 动态更新机制确保了知识库紧跟模型迭代节奏。
- 高社区关注度（近4.6万星）证明了其在AI工程领域的实用价值。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46128 | 🍴 7560 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、机器学习实战、线性代数基础以及PyTorch和TensorFlow 2等主流框架的综合学习资源库。它通过结合NLTK自然语言处理工具，提供了从理论到实践的完整机器学习技术栈指南。

2. **核心功能**
- 集成传统机器学习算法（如SVM、KMeans、随机森林等）与深度学习模型（如RNN、LSTM、DNN）的代码实现。
- 提供基于Scikit-learn和PyTorch的实战案例，覆盖分类、回归、聚类和推荐系统等典型任务。
- 包含自然语言处理（NLP）模块，利用NLTK进行文本分析和基础NLP任务处理。
- 梳理机器学习所需的数学基础，特别是线性代数在算法中的应用解析。

3. **适用场景**
- 机器学习初学者系统性地构建从数学基础到框架应用的知识体系。
- 数据科学家或工程师快速查阅经典算法（如Apriori、PCA、SVD）的标准Python实现。
- 需要进行NLP或深度学习模型（如RNN/LSTM）原型开发的开发人员参考实战代码。

4. **技术亮点**
- 技术栈全面且前沿，同时覆盖了经典的Scikit-learn算法与现代的PyTorch/TensorFlow 2深度学习框架。
- 内容结构清晰，将数学原理、经典算法与最新深度学习技术有机融合，便于循序渐进学习。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42349 | 🍴 11541 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36391 | 🍴 5974 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34894 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33699 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28189 | 🍴 3420 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25730 | 🍴 2884 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的高质量代码仓库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例和参考实现，助力快速掌握相关技术。作为一份“Awesome”列表，它通过集成代码示例，极大地降低了AI技术的入门与学习门槛。

2. **核心功能**
*   提供涵盖机器学习到深度学习的500多个完整项目代码库。
*   细分领域包括计算机视觉、自然语言处理（NLP）等热门AI方向。
*   采用Python为主要编程语言，确保代码的可运行性和通用性。
*   经过社区筛选和标记，包含高质量且具代表性的AI实战项目。

3. **适用场景**
*   AI初学者希望通过大量实战代码快速理解算法原理和应用方式。
*   研究人员或工程师寻找特定领域（如CV或NLP）的基准实现进行对比测试。
*   需要构建AI作品集以展示技术能力的求职者，可直接参考或复用部分代码结构。
*   希望追踪当前AI领域最新项目趋势和技术栈的技术爱好者。

4. **技术亮点**
*   **规模庞大且分类清晰**：包含500个项目，并精准打上CV、NLP、ML等标签，便于检索。
*   **实战导向**：不仅提供理论，更强调带有可执行代码的项目实践，具备极高的参考价值。
*   **高社区认可度**：拥有近3.5万星标，证明了其在开源社区中的广泛影响力和质量保障。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34894 | 🍴 7292 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22010 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉AI数据集的首选平台。它提供开源、云及企业级产品，支持图像、视频和3D数据的AI辅助标注、质量控制及团队协作等功能。

2. **核心功能**
*   支持图像、视频及3D点云的多维度数据标注。
*   内置AI辅助标注功能以显著提升人工标注效率。
*   提供完善的质量保证机制与团队协作管理工具。
*   开放开发者API并集成数据分析模块。

3. **适用场景**
*   需要构建大规模高精度视觉数据集的科研机构或企业。
*   涉及自动驾驶、安防监控等复杂视频分析算法的开发团队。
*   要求进行3D空间理解及语义分割研究的深度学习项目组。

4. **技术亮点**
*   采用Python开发，拥有强大的社区生态和极高的Star关注度（16k+）。
*   兼容PyTorch、TensorFlow等主流深度学习框架及ImageNet标准。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16148 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个面向计算机视觉的高级AI可解释性工具库，旨在帮助用户理解深度学习模型的决策过程。它广泛支持CNN、Vision Transformers等多种架构，并兼容分类、检测及分割等任务。

2. **核心功能**
*   支持Grad-CAM、Score-CAM等多种主流可视化算法。
*   兼容卷积神经网络与视觉Transformer等主流模型架构。
*   覆盖图像分类、目标检测、语义分割等多类视觉任务。
*   提供直观的热力图生成与图像相似度分析功能。

3. **适用场景**
*   调试深度学习模型，定位模型关注的关键图像区域。
*   向非技术利益相关者展示AI决策依据，提升系统透明度。
*   研究模型偏差或错误分类原因，优化算法性能。
*   开发符合伦理规范的可解释性医疗影像或自动驾驶分析工具。

4. **技术亮点**
*   高度模块化的代码设计，便于快速集成到现有PyTorch项目中。
*   同时支持经典CNN与现代Vision Transformer架构，适应性极强。
*   社区活跃且星标数高，拥有完善的文档和丰富的示例代码。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能设计的几何计算机视觉库。它基于 PyTorch 构建，旨在通过可微分操作简化深度学习中的视觉任务开发。该项目为研究人员和开发者提供了高效的图像处理与几何计算工具。

### 2. 核心功能
*   **可微分几何运算**：提供大量支持自动求导的几何变换函数，便于集成到神经网络中。
*   **PyTorch 原生集成**：作为 PyTorch 的扩展库，无缝兼容现有的深度学习工作流和数据管道。
*   **图像预处理与增强**：内置丰富的图像转换、归一化及数据增强算法，加速模型训练准备。
*   **传统 CV 与 DL 结合**：将经典的计算机视觉算法转化为可微分模块，支持端到端的联合优化。
*   **模块化 API 设计**：结构清晰的函数库，涵盖从基础像素操作到高级几何估计的多种需求。

### 3. 适用场景
*   **机器人视觉导航**：利用可微分几何进行姿态估计或 SLAM（同步定位与地图构建）模块的训练。
*   **工业缺陷检测**：在深度学习流水线中集成精确的图像校正和几何对齐步骤。
*   **自动驾驶感知系统**：处理相机标定、透视变换等前置几何计算，提升感知模型的鲁棒性。
*   **学术研究与原型验证**：快速实现结合了传统几何约束的深度学习新架构。

### 4. 技术亮点
*   **全可微设计**：核心优势在于所有视觉操作均支持梯度反向传播，实现了传统 CV 与现代 DL 的深度融合。
*   **高性能 GPU 加速**：底层实现针对 GPU 进行了优化，显著提升了大规模图像批处理的效率。
*   **活跃社区支持**：作为 Hacktoberfest 等项目，拥有活跃的开源社区和持续的贡献者生态。
- 链接: https://github.com/kornia/kornia
- ⭐ 11251 | 🍴 1191 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3254 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2617 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2411 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- ### 1. 中文简介
OpenClaw 是一款跨平台、全操作系统支持的个人 AI 助手，旨在让用户完全掌控自己的数据。它提供了一种独特的“龙虾”式解决方案，确保你的 AI 体验既私密又无处不在。

### 2. 核心功能
*   **全平台兼容**：支持任何操作系统和平台，实现无缝的个人助手体验。
*   **数据主权**：强调“Own Your Data”，用户完全拥有并控制自己的 AI 数据。
*   **个性化定制**：作为专属个人助理，可根据用户需求进行深度定制。
*   **开源透明**：基于开源社区驱动，代码可见且可审计。
*   **跨设备同步**：在不同设备和平台上保持助手状态的一致性。

### 3. 适用场景
*   **注重隐私的个人用户**：希望在不依赖第三方云服务的情况下，安全地使用 AI 助手处理日常任务。
*   **开发者与技术爱好者**：需要高度可定制、开源的 AI 解决方案以集成到自己的工作流中。
*   **多设备用户**：在电脑、手机、服务器等不同操作系统间频繁切换，需要一个统一的 AI 助手。
*   **企业私有化部署**：需要将 AI 助手部署在内网环境中，确保敏感数据不外泄的场景。

### 4. 技术亮点
*   **TypeScript 构建**：使用 TypeScript 开发，保证代码类型安全和良好的可维护性。
*   **去中心化架构**：设计上避免对单一云服务商的依赖，增强系统的鲁棒性和独立性。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380492 | 🍴 79699 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 238882 | 🍴 21188 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes Agent 是一个能够伴随用户共同成长的智能代理工具，旨在通过持续学习和交互优化用户体验。它集成了多种先进的语言模型能力，支持复杂的代码生成与任务自动化流程。该项目致力于提供一个灵活且强大的 AI 助手框架，帮助用户更高效地处理开发及日常任务。

### 2. 核心功能
- 支持多模型集成，兼容 OpenAI、Anthropic (Claude) 等主流大语言模型。
- 具备代码理解与生成能力，可辅助开发者进行编码、调试和重构工作。
- 提供个性化的 Agent 成长机制，能根据用户习惯不断优化响应策略。
- 支持复杂的自动化工作流，能够执行跨应用的任务调度与数据处理。
- 拥有活跃的社区生态，包含丰富的插件扩展和配置选项。

### 3. 适用场景
- **软件开发辅助**：用于代码审查、单元测试生成及复杂逻辑的快速原型开发。
- **个人效率增强**：作为私人智能助手，管理日程、整理信息或自动化重复性办公任务。
- **AI 应用开发**：作为构建自定义 Chatbot 或自动化 Agent 的基础框架进行测试与部署。
- **技术研究与实验**：适合研究人员探索不同 LLM 在特定任务中的表现及优化策略。

### 4. 技术亮点
- 高度模块化架构，允许用户轻松替换底层模型或添加自定义功能模块。
- 对多模态输入的支持潜力，能够处理文本、代码甚至潜在的图像指令。
- 社区驱动的开发模式，拥有极高的活跃度和广泛的第三方贡献者基础。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 203216 | 🍴 36400 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码。它提供超过 400 种集成方式，允许用户选择自托管或云端部署，灵活满足不同的自动化需求。

2. **核心功能**
*   支持可视化拖拽构建与自定义代码混合开发。
*   内置原生 AI 能力，可轻松集成智能处理流程。
*   拥有超过 400 种应用集成连接器，覆盖广泛。
*   提供灵活的部署选项，支持自托管服务器或云端服务。
*   采用公平代码许可证，平衡开源社区与企业用户需求。

3. **适用场景**
*   企业级 API 数据同步与跨系统业务流程自动化。
*   利用 AI 助手增强现有工作流的数据处理与分析能力。
*   开发者通过自定义代码扩展标准节点，实现复杂逻辑定制。
*   对数据隐私有高要求的团队选择自托管方案构建私有自动化中心。

4. **技术亮点**
*   基于 TypeScript 构建，类型安全且易于维护。
*   原生支持 MCP（Model Context Protocol），增强与大语言模型的交互能力。
*   兼具低代码/无代码的高效性与自定义开发的灵活性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194095 | 🍴 58841 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现人人可用的 AI 愿景，让大众能够自由地使用并在此基础上进行构建。我们的使命是提供必要的工具，让您能将精力专注于真正重要的事务上。

2. **核心功能**
*   具备自主执行复杂任务链的能力，无需人工持续干预。
*   支持集成多种大型语言模型（如 GPT、Claude、LLaMA），灵活适配不同需求。
*   提供开源工具集，便于开发者在其基础上定制和扩展 AI 代理功能。
*   通过自然语言指令驱动，降低使用高级 AI 技术的门槛。

3. **适用场景**
*   自动化日常办公流程，如信息搜集、报告生成或邮件处理。
*   作为开发者的基础框架，用于构建特定领域的垂直 AI 代理应用。
*   探索和研究自主智能体（Autonomous Agents）在复杂环境下的行为与能力。

4. **技术亮点**
*   采用 Agentic AI 架构，强调代理的自主性与规划能力。
*   高度模块化设计，兼容主流 LLM API，具备极强的扩展性。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185159 | 🍴 46130 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164359 | 🍴 21284 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163886 | 🍴 30365 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156624 | 🍴 46145 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150102 | 🍴 9346 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146600 | 🍴 23074 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

