# GitHub AI项目每日发现报告
日期: 2026-07-21

## 新发布的AI项目

### nativ
- 1. **中文简介**
Nativ 是一款专为 macOS 设计的本地 AI 应用，旨在让用户无需离开苹果生态即可运行机器学习模型。它通过统一的界面实现了聊天交互、模型服务部署、性能监控以及连接 MLX 模型的全流程管理。

2. **核心功能**
- 支持在本地运行和测试基于 MLX 框架的大语言模型。
- 提供直观的聊天界面，用于与本地 AI 模型进行实时对话。
- 具备模型服务端能力，可将本地模型作为服务对外提供接口。
- 集成实时监控工具，方便用户查看模型运行状态和资源消耗。
- 原生适配 macOS 系统，确保与苹果硬件及 MLX 库的完美兼容。

3. **适用场景**
- 开发者希望在本地快速验证和优化基于 Apple Silicon 芯片的 MLX 模型。
- 注重数据隐私的用户希望在完全离线的环境下使用 AI 助手，避免云端数据泄露。
- 研究人员需要在一个统一的应用程序中同时调试、监控和部署多个机器学习模型。
- macOS 用户希望获得原生体验，避免使用跨平台或基于 Electron 的笨重 AI 客户端。

4. **技术亮点**
- 深度整合 Apple 的 MLX 框架，充分发挥 M 系列芯片的 NPU 算力优势。
- 采用 Swift 原生开发，提供轻量级、高性能且符合 macOS 设计规范的用户体验。
- 链接: https://github.com/Blaizzy/nativ
- ⭐ 522 | 🍴 32 | 语言: Swift

### Agent-Execution-Partnership
- ### 1. 中文简介
Agent Execution Partnership (AEE) 是一个开源的控制平面，旨在确保每个 AI 智能体在执行操作前获得授权，在运行时保持可观测性，并在完成后具备可验证性。该项目通过引入审计追踪和政策引擎，为自主智能体提供全面的安全治理与合规保障。

### 2. 核心功能
*   **事前授权控制**：在 AI 智能体执行任何操作之前，强制进行权限校验以确保合规。
*   **实时运行监控**：提供可视化的运行状态追踪，确保智能体行为全程可观测。
*   **事后审计验证**：记录完整的操作日志，支持对已完成任务的独立验证与回溯。
*   **策略引擎集成**：内置灵活的政策引擎，允许自定义安全规则和管理智能体行为边界。

### 3. 适用场景
*   **企业级 AI 治理**：在大型组织中部署 AI 智能体时，满足严格的内部合规与安全审计要求。
*   **高风险自动化任务**：用于涉及金融交易、数据修改或关键基础设施操作的智能体系统，防止误操作或恶意行为。
*   **多智能体协作平台**：作为控制层管理多个自治智能体之间的交互，确保协作过程中的透明度和安全性。

### 4. 技术亮点
*   采用 Python 开发，生态兼容性好，易于集成到现有的 MLOps 和 LLM 应用栈中。
*   实现了“授权-观测-验证”的全生命周期安全管理闭环，填补了自主智能体安全领域的空白。
- 链接: https://github.com/eli-labz/Agent-Execution-Partnership
- ⭐ 250 | 🍴 75 | 语言: Python
- 标签: agent-safety, ai-agents, ai-governance, ai-safety, audit-trail

### open-kritt
- 描述: Orchestrate AI agents to find real vulnerabilities in code.
- 链接: https://github.com/Kritt-ai/open-kritt
- ⭐ 187 | 🍴 41 | 语言: JavaScript
- 标签: agent, agents, ai, bug-bounty, bugbounty

### agents-council
- 描述: Multi-agents collaboration plugin for Claude Code - orchestrate multiple AI agents (Codex CLI, Gemini CLI, etc.) for diverse perspectives
- 链接: https://github.com/0xwilliamortiz/agents-council
- ⭐ 91 | 🍴 1 | 语言: JavaScript
- 标签: claude, claude-ai, claude-code, claude-code-skills, claude-plugin

### caspian-sdk
- ### 1. 中文简介
Caspian SDK 旨在为开发者提供一个统一的身份标识，使 AI 代理能够无缝集成至 Slack、Discord、Telegram、Instagram、电子邮件及 X 等主流人类沟通渠道。通过单一的 `on_message` 处理逻辑配合通道适配器、SDK 和 CLI 工具，极大地简化了多平台消息交互的开发复杂度。

### 2. 核心功能
*   **统一消息接口**：仅需编写一次 `on_message` 处理器即可响应所有支持渠道的消息事件。
*   **多渠道适配器**：内置针对 Slack、Discord、Telegram 等平台的专用适配层，屏蔽底层协议差异。
*   **全平台覆盖**：支持即时通讯（Slack/Discord/Telegram）、社交媒体（Instagram/X）以及电子邮件等多种通信方式。
*   **开发工具链**：提供配套的 CLI 命令行工具和 SDK，加速 AI 代理的构建与部署流程。

### 3. 适用场景
*   **跨平台智能客服**：构建一个能同时在 Slack 工作区和 Discord 社区提供一致服务的 AI 助手。
*   **多账号社交机器人管理**：通过单一后端逻辑集中管理分布在 X、Instagram 等不同社交平台的自动化响应。
*   **企业级通知聚合系统**：利用邮件和即时通讯通道的统一接入能力，实现重要警报的多渠道同步推送。

### 4. 技术亮点
*   **解耦设计**：将业务逻辑与通信协议分离，使得新增支持新平台时只需开发适配器而无需修改核心代码。
*   **极简开发体验**：通过抽象出通用的消息处理模型，显著降低了维护多平台 AI 代理的代码成本。
- 链接: https://github.com/TryCaspian/caspian-sdk
- ⭐ 67 | 🍴 1 | 语言: Python
- 标签: ai-agents, communication, discord, messaging, sdk

### stem-illustration-skill
- 描述: 面向 STEM（科学、技术、工程、数学）领域的 AI 图像生成 Skill。  生成科研示意图、教学插图、技术架构图等概念性图像，覆盖生物医学、化学、物理、工程、数学 6 大学科。  功能特性 24 个场景模板：信号通路、实验流程、细胞结构、概念信息图、学术海报、机制图、质粒图、机器学习架构等 6 大学科适配：生命科学/医学/化学/物理/工程/数学 4 种风格变体：academic / textbook / infographic / 3d-render
- 链接: https://github.com/liangdabiao/stem-illustration-skill
- ⭐ 43 | 🍴 1 | 语言: Python
- 标签: skill

### VibeGamer
- 描述: 用 AI Agent 自动游玩《Turmoil》（石油大亨）并不断积累经验进化的实验项目. 
- 链接: https://github.com/karminski/VibeGamer
- ⭐ 31 | 🍴 2 | 语言: TypeScript

### aipay-protocol
- 描述: Verifier-backed USDC escrow for AI agents: signed orders, evidence hashes, Polygon deposits, and deterministic settlement.
- 链接: https://github.com/AIPAYagent/aipay-protocol
- ⭐ 29 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, aipay, eip712, escrow, mcp

### BossConsole
- 描述: Open-source, multi-platform harness for AI agents — a native, multi-threaded operator's console (JVM, not Electron) to run Claude Code, Codex, Gemini or OpenCode with a real browser, terminal, editor, secrets & 100+ MCP tools. Built for enterprises, science & research.
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 29 | 🍴 0 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### LLM-WIKI
- 描述: 一个会自己生长的 AI 知识库
- 链接: https://github.com/loonggg/LLM-WIKI
- ⭐ 25 | 🍴 3 | 语言: JavaScript

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81942 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码资源库。该项目为开发者提供了丰富的实战案例，涵盖了从基础算法到前沿应用的全方位技术栈。

2. **核心功能**
- 提供500个经过验证的AI相关项目代码示例。
- 覆盖机器学习、深度学习、计算机视觉和NLP四大核心领域。
- 包含完整的代码实现，便于直接运行和学习。
- 被标记为“Awesome”列表，内容经过精选和质量把控。

3. **适用场景**
- 初学者入门学习，通过阅读和运行代码快速掌握AI基本概念。
- 开发者寻找灵感，参考现有项目结构以构建自己的AI应用。
- 教育或培训场景，作为机器学习和深度学习的教学案例库。

4. **技术亮点**
- 项目数量庞大且分类清晰，一站式满足多种AI技术学习需求。
- 主要基于Python语言，符合当前AI开发的主流技术栈标准。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35598 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33251 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破生态壁垒。该标准由微软、Facebook 等科技巨头联合推动，已成为业界通用的模型交换格式。

2. **核心功能**
*   **框架互操作性**：支持在 PyTorch、TensorFlow、Keras 等不同训练框架之间轻松转换模型。
*   **统一计算图表示**：定义了一套通用的算子和数据结构，以中立方式描述神经网络结构。
*   **跨平台部署优化**：允许模型在多种硬件加速器（如 CPU、GPU、NPU）上进行高效推理和优化。
*   **生态兼容性**：广泛兼容 Scikit-learn 等传统 ML 库以及主流深度学习框架，提供广泛的工具链支持。

3. **适用场景**
*   **模型迁移与部署**：将训练好的模型从研究环境（如 PyTorch）无缝迁移到生产环境或边缘设备。
*   **跨厂商硬件加速**：利用 ONNX Runtime 在不同硬件后端上实现高性能推理，无需重写代码。
*   **模型协作与分享**：在团队或组织间标准化共享模型资产，避免框架锁定带来的兼容性问题。

4. **技术亮点**
*   **开放标准主导**：作为行业事实标准的开放规范，拥有庞大的社区支持和持续的标准化演进。
*   **高性能运行时**：配套的 ONNX Runtime 提供了高度优化的执行引擎，显著提升推理速度和资源利用率。
- 链接: https://github.com/onnx/onnx
- ⭐ 21186 | 🍴 3974 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18442 | 🍴 1177 | 语言: Python
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
- ⭐ 13165 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11584 | 🍴 909 | 语言: Python
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
- ⭐ 35598 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33251 | 🍴 3162 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15419 | 🍴 3384 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13165 | 🍴 2662 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLM）、神经网络及其他人工智能模型的构建过程。它通过声明式的配置方式，让开发者无需编写大量底层代码即可快速训练和评估模型。该项目由 Uber 开发，致力于降低 AI 开发的门槛并提升数据驱动实验的效率。

### 2. 核心功能
*   **低代码/无代码体验**：通过 YAML 配置文件定义模型架构和数据集，无需编写复杂的 Python 训练脚本。
*   **多模态支持**：原生支持文本、图像、音频、表格等多种数据类型，便于处理复杂的多模态任务。
*   **自动化超参数调优与实验管理**：内置自动机器学习（AutoML）功能，可自动搜索最佳超参数并跟踪实验结果。
*   **基于 PyTorch 的灵活后端**：底层依托 PyTorch 框架，既保证了易用性，又允许高级用户进行深度定制和扩展。

### 3. 适用场景
*   **快速原型开发**：适用于希望迅速验证 AI 想法或构建最小可行性产品（MVP）的数据科学家和工程师。
*   **传统机器学习向深度学习迁移**：适合拥有大量结构化表格数据，但缺乏深度学习编程经验的企业团队。
*   **多模态应用构建**：用于需要同时处理文本、图像或音频等混合数据类型的复杂 AI 应用场景。

### 4. 技术亮点
*   **声明式架构**：采用声明式而非命令式的模型定义方式，显著减少了样板代码（Boilerplate Code），提高了开发效率。
*   **端到端工作流**：集成了从数据预处理、模型训练到推理部署的完整链路，简化了 MLOps 流程。
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
- ⭐ 8373 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6992 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6268 | 🍴 749 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81942 | 🍴 15250 | 语言: Python

### LlamaFactory
- **1. 中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目在 ACL 2024 会议上发表，旨在简化从基础训练到高级对齐的全过程。它提供了开箱即用的解决方案，帮助用户快速实现模型定制。

**2. 核心功能**
*   **多模型统一支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等100多种开源模型，无需切换不同代码库。
*   **丰富微调算法**：内置 LoRA、QLoRA、P-Tuning 等高效参数微调方法，以及完整的 RLHF（基于人类反馈的强化学习）支持。
*   **量化与低资源优化**：支持 GPTQ、AWQ 等高精度量化技术，可在消费级 GPU 上高效运行大规模模型。
*   **全流程训练引擎**：涵盖监督微调（SFT）、指令微调及偏好对齐训练，提供标准化的数据处理和评估流程。
*   **可视化与易用性**：提供 Web UI 界面和详细的日志记录，降低微调门槛，便于监控训练状态。

**3. 适用场景**
*   **垂直领域知识增强**：为企业或特定行业（如法律、医疗）的开源基座模型注入私有数据，提升专业问答能力。
*   **低成本模型部署与定制**：利用 QLoRA 等技术，在显存受限的消费级硬件上对大模型进行个性化微调。
*   **多模态应用开发**：针对视觉语言模型（如 LLaVA）进行微调，构建具备图像理解能力的智能助手或内容生成工具。
*   **AI Agent 行为对齐**：通过 DPO 或 RLHF 等技术调整模型输出风格，使其更符合人类价值观或特定任务需求。

**4. 技术亮点**
*   **模块化架构设计**：将数据处理、模型加载和训练逻辑解耦，便于开发者扩展新模型或新算法。
*   **混合精度训练支持**：自动适配 BF16/FP16 等不同精度格式，最大化训练效率并减少内存占用。
*   **前沿算法集成**：紧跟学术进展，迅速集成最新的多模态对齐技术和高效的优化器策略。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73422 | 🍴 8962 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52525 | 🍴 10636 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 描述: AiLearning：数据分析+机器学习实战+线性代数+PyTorch+NLTK+TF2
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42399 | 🍴 11532 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入掌握人工智能工程的核心原理与实践。内容涵盖从基础学习到最终部署应用的完整流程，帮助学习者具备独立开发AI系统的能力。

2. **核心功能**
*   提供涵盖生成式AI、LLM及计算机视觉等前沿领域的系统性教程与课程资源。
*   指导用户从零实现智能体（Agents）、强化学习模型及Transformer架构等复杂组件。
*   结合Python与Rust等语言，展示高性能AI工程的最佳实践与底层技术细节。
*   包含多模态应用开发示例，如基于MCP协议的工具集成与Swarm Intelligence探索。

3. **适用场景**
*   AI工程师希望深入理解大模型底层机制并提升系统级架构设计能力。
*   研究人员或学生需要通过动手实践来巩固深度学习与自然语言处理理论。
*   团队需要参考从零构建生产级AI应用（如智能体工作流）的工程化案例。

4. **技术亮点**
*   强调“From Scratch”理念，不依赖黑盒库，而是通过手写代码解析算法本质。
*   跨语言技术栈融合，结合Python的易用性与Rust的高性能优势。
*   紧跟最新技术趋势，涵盖MCP、AI Agents及多智能体协作等热点方向。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 41294 | 🍴 6852 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35598 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33757 | 🍴 4696 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28748 | 🍴 3510 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25969 | 🍴 2944 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21730 | 🍴 3306 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35598 | 🍴 7371 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22538 | 🍴 2112 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### CVAT 项目分析

**1. 中文简介**
CVAT（计算机视觉注释工具）是构建高质量视觉数据集的首创平台，支持图像、视频及3D数据的标注。它提供开源、云端和企业级产品，具备AI辅助标注、质量保证及团队协作等核心功能。

**2. 核心功能**
*   支持图像、视频和3D数据的多种标注任务，如边界框和语义分割。
*   提供AI辅助标注功能，显著提升数据集构建效率与准确性。
*   内置质量保证机制与团队协作工具，确保数据标注的一致性。
*   开放开发者API与分析接口，便于集成到现有工作流中。
*   提供开源、云服务和企业版等多种部署模式及标注服务。

**3. 适用场景**
*   深度学习模型训练前的数据清洗与标签制作。
*   自动驾驶或机器人领域所需的视频序列与3D点云标注。
*   需要大规模团队协作进行复杂视觉数据集构建的企业环境。

**4. 技术亮点**
*   兼容主流深度学习框架（PyTorch, TensorFlow）及标准数据集格式（如ImageNet）。
*   覆盖物体检测、图像分类、语义分割等广泛计算机视觉任务。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16349 | 🍴 3771 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
这是一个用于计算机视觉的高级AI可解释性工具包，旨在帮助用户理解深度学习模型的决策依据。该项目广泛支持CNN、Vision Transformers等多种架构，涵盖分类、目标检测、分割及图像相似度等任务，并提供丰富的可视化功能。

2. **核心功能**
*   支持多种主流模型架构，包括传统卷积神经网络（CNN）和最新的视觉Transformer（ViT）。
*   覆盖多种计算机视觉任务，如图像分类、对象检测、语义分割及图像相似度计算。
*   集成多种梯度加权类激活映射算法（如Grad-CAM、Score-CAM），提供直观的热力图可视化以增强模型透明度。

3. **适用场景**
*   **医疗影像诊断辅助**：通过可视化高亮病变区域，帮助医生验证AI对病灶位置的判断是否合理。
*   **自动驾驶系统调试**：在目标检测和分割任务中，分析车辆识别依据，提升安全系统的可信度。
*   **学术研究教学**：为研究人员和学生提供直观的工具，用于解释和演示深度学习模型的内部工作机制。

4. **技术亮点**
*   **广泛的兼容性**：同时适配经典CNN与现代Vision Transformer架构，满足不同研究需求。
*   **多算法集成**：内置Grad-CAM、Score-CAM等多种先进的可解释性算法，便于对比实验。
*   **高社区认可度**：拥有超过12,000个星标，证明其在AI可解释性领域的广泛使用和影响力。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间智能设计的几何计算机视觉库。它基于 PyTorch 构建，旨在将传统的计算机视觉技术与深度学习无缝集成。该库提供了可微分的图像处理原语，便于在神经网络中进行端到端的视觉任务处理。

2. **核心功能**
*   提供完全可微分的传统计算机视觉算法（如边缘检测、特征匹配）。
*   内置丰富的几何变换和图像增强操作，支持自动求导。
*   与 PyTorch 张量完美兼容，简化了深度学习模型中的视觉数据处理流程。
*   包含用于机器人学和空间 AI 的高级几何计算模块。
*   支持从图像到语义分割、姿态估计等多种视觉任务的快速原型开发。

3. **适用场景**
*   **机器人导航与SLAM**：利用几何视觉算法进行环境感知和定位建图。
*   **深度学习数据增强**：在训练过程中应用可微分的几何变换以提升模型鲁棒性。
*   **工业缺陷检测**：结合传统CV精度与深度学习灵活性进行高精度图像分析。
*   **空间智能研究**：探索需要精确几何约束的3D视觉和多模态融合任务。

4. **技术亮点**
*   **全可微设计**：打破传统CV与深度学习的壁垒，允许梯度反向传播通过视觉算子。
*   **硬件加速**：充分利用 GPU 并行计算能力，显著提升图像处理速度。
*   **模块化架构**：提供灵活、即插即用的视觉组件，易于集成到现有 PyTorch 项目中。
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
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3292 | 🍴 404 | 语言: Python
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
- ⭐ 383687 | 🍴 80620 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架及软件开发方法论。它旨在通过结构化的方式提升人工智能在编程和协作中的实际效能。该项目为开发者提供了一套可操作的智能体驱动开发流程。

2. **核心功能**
*   提供基于智能体的技能框架，支持模块化能力扩展。
*   定义了一套完整的软件开发生命周期（SDLC）方法论。
*   支持子智能体驱动开发（Subagent-driven Development），实现复杂任务分解。
*   集成头脑风暴与代码生成工具，辅助创意发散与实现。

3. **适用场景**
*   希望利用 AI 智能体优化传统软件开发生命周期的团队。
*   需要结构化方法来进行大规模代码生成与调试的项目。
*   探索智能体协作模式以提升研发效率的技术先锋团队。

4. **技术亮点**
*   将抽象的 AI 智能体能力转化为具体的、可复用的开发技能。
*   强调“能工作”的方法论，注重实际应用而非纯理论框架。
- 链接: https://github.com/obra/superpowers
- ⭐ 258638 | 🍴 23052 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218249 | 🍴 41239 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一款具备原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码。它拥有 400 多种集成方案，用户可选择自托管或云端部署，灵活满足各种自动化需求。

2. **核心功能**
*   提供可视化拖拽界面与自定义代码混合构建工作流。
*   内置原生 AI 能力，支持智能自动化处理。
*   集成超过 400 种应用和服务，实现广泛的数据互通。
*   支持自托管和云服务两种部署模式，保障数据隐私与灵活性。
*   兼容 MCP（模型上下文协议），增强与大模型的交互能力。

3. **适用场景**
*   企业级跨系统数据同步与业务流程自动化。
*   利用 AI 辅助生成内容或进行智能数据分析的工作流。
*   开发者快速搭建 API 连接器及后端逻辑原型。
*   对数据隐私有严格要求、需本地化部署的自动化任务。

4. **技术亮点**
*   基于 TypeScript 开发，类型安全且易于扩展。
*   采用 Fair-code 许可证，平衡开源共享与企业商业需求。
*   原生支持 MCP 协议，无缝对接最新的大语言模型生态。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197337 | 🍴 59506 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于实现“人人可用”的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。我们的使命是提供必要的工具，帮助用户专注于真正重要的事项。

2. **核心功能**
*   支持自主代理（Autonomous Agents）运行，具备自我驱动任务执行能力。
*   集成多种大型语言模型（LLM），如 OpenAI GPT、Claude 及 Llama API。
*   提供可扩展的开发框架，便于用户基于现有工具进行二次开发。
*   通过 agentic-ai 架构实现复杂的自动化工作流处理。

3. **适用场景**
*   自动化重复性高、逻辑复杂的多步骤办公或数据处理任务。
*   作为 AI 应用开发的基准测试平台，验证不同大模型的自主推理能力。
*   构建个性化的智能助手，用于信息搜集、内容生成或代码辅助。

4. **技术亮点**
*   高度模块化设计，兼容主流商业及开源大语言模型接口。
*   拥有极高的社区活跃度（近 19 万星标），生态完善且迭代迅速。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185638 | 🍴 46067 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166128 | 🍴 21472 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164276 | 🍴 30431 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157181 | 🍴 46182 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 153909 | 🍴 8781 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152159 | 🍴 9615 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

