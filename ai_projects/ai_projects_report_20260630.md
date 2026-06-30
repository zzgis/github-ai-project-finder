# GitHub AI项目每日发现报告
日期: 2026-06-30

## 新发布的AI项目

### xuanxuan-prompts
- ### 1. 中文简介
该项目汇集了用于让 AI Agent 复刻精美网页的提示词（Prompts），每个目录包含一份 `prompt.md` 文件及对应的效果图截图。用户只需将这些内容输入给 Claude、Codex 或 Kimi 等 AI 模型，即可快速生成相应的网站页面。

### 2. 核心功能
*   **结构化提示词库**：为不同风格的网页设计提供标准化的 Prompt 模板，降低使用门槛。
*   **图文对照参考**：每个案例均附带效果图截图，帮助开发者直观理解预期输出结果。
*   **多模型兼容性**：生成的提示词经过优化，适用于 Claude、Codex 和 Kimi 等多种主流 AI 编程助手。
*   **模块化目录管理**：按功能或风格分类存储，便于用户按需查找和调用特定的网页复刻需求。

### 3. 适用场景
*   **前端开发原型搭建**：快速生成特定 UI 风格的静态页面代码，作为开发初期的视觉参考或基础骨架。
*   **AI 辅助编程学习**：通过观察高质量的 Prompt 如何驱动 AI 生成复杂网页，学习提示词工程的最佳实践。
*   **设计稿快速落地**：将设计师提供的效果图转化为可运行的前端代码，缩短从设计到开发的周期。

### 4. 技术亮点
*   **零代码依赖**：项目本身不包含编程语言代码，而是专注于“提示词”这一非代码资产，具有极高的通用性。
*   **实战导向**：直接面向“复刻精美网页”这一具体痛点，提供了经过验证的、能产生高质量结果的 Prompt 策略。
- 链接: https://github.com/xuanxuan321/xuanxuan-prompts
- ⭐ 32 | 🍴 4 | 语言: 未知

### Agent-Span
- ### 1. 中文简介
Agent-Span 是一个专为 AI 智能体设计的 Web 访问网关，采用异步 Rust 构建以保障高性能与稳定性。它通过自修复后端机制，整合了 52 种通信渠道、92 个 MCP 工具及 9 种 SDK，旨在为智能体提供强大且可靠的网络交互能力。

### 2. 核心功能
*   **多协议网关支持**：集成 52 种通信渠道和 9 种 SDK，实现广泛的协议兼容。
*   **MCP 工具生态**：内置 92 个 Model Context Protocol (MCP) 工具，增强智能体的上下文理解与操作能力。
*   **自修复后端架构**：具备自动检测与恢复机制，确保服务的高可用性和稳定性。
*   **高性能底层实现**：基于异步 Rust 开发，提供低延迟和高并发的处理性能。
*   **Web 抓取与管理**：作为 Web 访问网关，简化智能体对网页数据的获取与交互流程。

### 3. 适用场景
*   **复杂 AI 应用开发**：需要稳定连接多种数据源和 API 的企业级智能体系统。
*   **自动化工作流**：依赖大量 MCP 工具进行数据收集、处理和执行任务的自动化场景。
*   **高可用性需求项目**：对服务连续性要求极高，需后端具备自愈能力的生产环境。
*   **跨平台智能体集成**：希望统一网关接口以适配不同渠道和 SDK 的智能体部署方案。

### 4. 技术亮点
*   **Rust 异步运行时**：利用 Rust 语言的安全性和异步编程模型，实现极致性能。
*   **Model Context Protocol (MCP) 深度集成**：原生支持 MCP 标准，方便扩展智能体的工具调用能力。
*   **自我愈合机制**：独特的后端自修复设计，减少了人工运维成本和宕机风险。
- 链接: https://github.com/oxbshw/Agent-Span
- ⭐ 31 | 🍴 10 | 语言: Rust
- 标签: ai-agents, ai-tools, api, gateway, llm

### gemini-search-mcp
- ### 1. **中文简介**
这是一个基于 Google AI 模式（Gemini）构建的免费 MCP 服务器，专为网页搜索设计。它无需 API 密钥即可使用，且提供无限量的搜索服务。该项目旨在降低接入高性能 AI 搜索功能的门槛。

### 2. **核心功能**
*   提供标准的 Model Context Protocol (MCP) 接口，便于集成各类 AI 应用。
*   直接调用 Google Gemini 引擎实现强大的网页内容检索能力。
*   免去了获取和使用 API 密钥的繁琐步骤，实现零成本接入。
*   支持无限制的搜索请求，满足高频或大规模数据抓取需求。
*   基于 Python 开发，代码轻量且易于部署和维护。

### 3. **适用场景**
*   AI 助手开发：为聊天机器人或智能代理添加实时联网搜索能力。
*   自动化工作流：在需要最新信息支持的 RAG（检索增强生成）系统中作为知识源。
*   快速原型验证：开发者无需配置复杂凭证即可快速测试基于 Gemini 的搜索功能。
*   个人知识库增强：帮助用户通过自然语言提问获取最新的互联网信息补充本地知识。

### 4. **技术亮点**
*   **零门槛接入**：完全摒弃了常见的 API Key 验证机制，极大简化了部署流程。
*   **免费无限额**：利用 Google AI Mode 的资源优势，提供了极具竞争力的免费使用策略。
*   **标准化协议**：严格遵循 MCP 标准，确保了与主流 AI 客户端和框架的高兼容性。
- 链接: https://github.com/Sophomoresty/gemini-search-mcp
- ⭐ 29 | 🍴 6 | 语言: Python

### cognitive-substrate-os
- ### 1. 中文简介
Cognitive Substrate OS 是一个轻量级的本地 AI 智能体操作系统（AIOS），基于 TypeScript 构建并集成 Google Gemini 模型。它旨在为用户提供一个在本地环境中自主运行和管理 AI 智能体的基础架构。该项目专注于实现智能体的本地化部署与高效交互。

### 2. 核心功能
*   **本地化智能体管理**：支持在用户本地环境中部署和运行 AI 智能体，保障数据隐私。
*   **Gemini 驱动引擎**：深度集成 Google Gemini 大语言模型，提供强大的自然语言处理能力。
*   **TypeScript 基础架构**：采用 TypeScript 开发，确保代码的类型安全和可维护性。
*   **自主代理支持**：具备支持智能体自主执行任务和决策的能力。

### 3. 适用场景
*   **隐私敏感型应用开发**：需要确保数据不出本地环境的 AI 应用原型开发。
*   **个人 AI 助手构建**：开发者用于搭建具有自主能力的个性化 AI 助手。
*   **轻量级智能体研究**：研究人员探索基于 Gemini 模型的本地智能体行为与架构。

### 4. 技术亮点
*   **轻量级设计**：相比重型 AI 平台，该项目资源占用更低，易于快速部署。
*   **现代化技术栈**：结合 TypeScript 类型系统与前沿的 Gemini API，平衡了开发体验与性能。
- 链接: https://github.com/damiansire/cognitive-substrate-os
- ⭐ 26 | 🍴 0 | 语言: JavaScript
- 标签: agent, ai, autonomous-agents, gemini, llm

### weekend-city-trip
- 描述: claude code / codex skill , 一个让 AI 帮你 5 分钟深度调研任意中国城市周末玩法的agent skill,基于**博查 WebSearch API**(博查 API),输出图文并茂、可执行的 Markdown / HTML 攻略。
- 链接: https://github.com/liangdabiao/weekend-city-trip
- ⭐ 19 | 🍴 3 | 语言: HTML

### mastering-ai-observability-workshop
- 描述: AIE World's Fair content for the Mastering AI Observability workshop with Braintrust
- 链接: https://github.com/dpguthrie/mastering-ai-observability-workshop
- ⭐ 16 | 🍴 1 | 语言: Python

### pocketdev
- 描述: One command to run the AI coding CLI you already pay for (Claude Code, Codex, Cursor, Gemini, Grok, aider) on a Tailscale-only Hetzner box — code from your phone.
- 链接: https://github.com/0xMassi/pocketdev
- ⭐ 16 | 🍴 0 | 语言: Go
- 标签: ai-coding, bubbletea, claude-code, cli, cloud-development-environment

### agent-skills
- 描述: A personal collection of reusable AI agent skills, mostly for Codex, with optional MCP utilities.
- 链接: https://github.com/Misaka-Mikoto-Tech/agent-skills
- ⭐ 15 | 🍴 0 | 语言: Python

### agent-context-workshop
- 描述: A context layer for coding agents — build a code knowledge graph from a real codebase, then measure whether the agent actually uses it. AI Engineer World's Fair 2026 workshop.
- 链接: https://github.com/bcallender/agent-context-workshop
- ⭐ 13 | 🍴 7 | 语言: Rust
- 标签: ai-agents, code-intelligence, knowledge-graph, llm, workshop

### ai-sticker-pack
- 描述: 上传表情包 → AI 自动写描述 → 聊天机器人按场景自己挑着发（含双向发送 / 多端渲染 / 踩坑思路）
- 链接: https://github.com/Lumenocturne/ai-sticker-pack
- ⭐ 12 | 🍴 0 | 语言: 未知
- 标签: ai, chatbot, llm, stickers, telegram-bot

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81506 | 🍴 15247 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个精选的500个AI机器学习、深度学习、计算机视觉及自然语言处理项目的资源合集。它提供了包含完整代码的项目列表，旨在帮助开发者快速学习和实践各类人工智能技术。

2. **核心功能**
- 收录500个涵盖ML、DL、CV和NLP领域的实战项目。
- 提供每个项目对应的可运行代码实现。
- 对人工智能热门子领域进行系统化分类整理。
- 作为优质AI学习资源的索引库，支持快速检索。

3. **适用场景**
- 初学者通过阅读代码快速理解AI算法的实际应用。
- 研究人员寻找特定领域（如NLP或CV）的参考实现。
- 开发者利用现成项目进行技能提升或技术选型调研。
- 教育者将其作为课程案例库以辅助教学。

4. **技术亮点**
- 极高的社区认可度（35k+星标），证明其资源丰富且质量可靠。
- 标签体系完善，精准覆盖从基础机器学习到前沿深度学习的各个细分方向。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35027 | 🍴 7304 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够直观展示模型结构和数据流，帮助开发者深入理解模型内部机制。

2. **核心功能**
- 广泛支持多种模型格式，包括 TensorFlow、PyTorch、ONNX、CoreML 等主流框架。
- 提供交互式图形界面，直观展示神经网络层结构、张量形状及权重信息。
- 支持查看模型详细属性，如层名称、输入输出维度及激活函数等关键参数。
- 具备模型验证功能，可检查模型结构的完整性与潜在错误。
- 支持离线使用，无需联网即可在本地打开和分析各类模型文件。

3. **适用场景**
- 深度学习研究人员调试模型架构，快速定位层连接错误或维度不匹配问题。
- 工程师在不同框架间转换模型时，验证转换前后结构的一致性。
- 产品经理或技术人员向非专业受众展示模型工作原理及数据流向。
- 开发者在部署模型前，审查模型复杂度以评估其在边缘设备上的可行性。

4. **技术亮点**
- 基于 JavaScript 开发，跨平台兼容性强，可在桌面端和浏览器中运行。
- 轻量级且无需安装庞大的深度学习环境，即可独立进行模型可视化分析。
- 社区活跃，持续更新对最新模型格式（如 Safetensors）的支持。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33156 | 🍴 3143 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（开放神经网络交换）是一个用于机器学习模型互操作性的开放标准。它旨在促进不同深度学习框架之间的模型转换与共享，打破平台壁垒。通过统一模型表示，开发者可以更轻松地在各种硬件和软件环境中部署AI模型。

2. **核心功能**
- 定义了一套开放的模型规范，支持跨框架的模型交换。
- 提供工具链以将模型从PyTorch、TensorFlow等框架转换为ONNX格式。
- 支持在多种推理引擎（如ONNX Runtime）上高效执行模型预测。
- 兼容主流机器学习库（如Scikit-learn、Keras），便于集成现有工作流。

3. **适用场景**
- 需要将训练好的模型从开发框架迁移到生产环境进行部署。
- 希望在不同的硬件加速器（如GPU、CPU、NPU）上运行同一模型。
- 构建跨平台AI应用，需确保模型在异构系统间无缝切换。

4. **技术亮点**
- 实现了真正的框架无关性，成为AI生态系统中的“通用语言”。
- 拥有庞大的社区支持和广泛的行业兼容性，是工业界事实上的标准。
- 链接: https://github.com/onnx/onnx
- ⭐ 21071 | 🍴 3956 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《ML Engineering Open Book》是一本全面介绍机器学习工程实践的开源指南。该项目深入探讨了从模型训练、调试到大规模部署和推理优化的完整工程链路。旨在为开发者提供构建可扩展、高效机器学习系统的实用知识。

2. **核心功能**
*   涵盖大规模语言模型（LLM）的训练、微调和推理优化全流程。
*   提供GPU集群管理、存储优化及网络配置等基础设施最佳实践。
*   详解PyTorch、Transformers等主流框架的工程化调试与性能调优技巧。
*   介绍基于Slurm等调度器的分布式训练扩展性与稳定性保障方案。

3. **适用场景**
*   需要从零搭建或优化大规模分布式机器学习训练平台的技术团队。
*   致力于降低大模型推理成本并提升响应速度的算法工程师。
*   希望系统学习MLOps实战技能，解决模型在生产环境落地问题的开发者。

4. **技术亮点**
*   聚焦于“工程化”而非纯理论，紧密结合SLURM、NCCL等底层基础设施细节。
*   针对当前热门的大语言模型（LLM）提供了具体的缩放法则（Scaling Laws）和调试策略。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18195 | 🍴 1155 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17261 | 🍴 2107 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13099 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11534 | 🍴 903 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10647 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI实战代码库的资源合集，涵盖了机器学习、深度学习、计算机视觉及自然语言处理等核心领域。它为开发者提供了丰富的Python代码示例，旨在帮助初学者和专业人士快速掌握相关技术并应用于实际项目中。

2. **核心功能**
- 提供500多个经过验证的AI项目源代码，覆盖主流算法与模型实现。
- 整合了机器学习、深度学习、计算机视觉和NLP四大领域的完整案例。
- 主要基于Python语言编写，便于直接运行、学习和二次开发。
- 作为“Awesome”列表性质的资源库，筛选了高质量且具代表性的开源项目。

3. **适用场景**
- AI初学者通过阅读和运行代码快速理解复杂算法原理。
- 数据科学家寻找特定任务（如图像分类、文本情感分析）的最佳实践参考。
- 开发者在构建AI原型时，复用现有代码模块以提高开发效率。
- 教育机构用于课堂教学或实验指导，提供标准化的项目案例。

4. **技术亮点**
- 内容覆盖面极广，集成了从基础统计学习到前沿大模型应用的广泛技术栈。
- 代码即学即用，每个项目均附带可运行的代码，降低了学习门槛。
- 社区驱动的高质量筛选，保留了星标高、维护好的优质项目，避免了信息过载。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35027 | 🍴 7304 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够直观展示模型结构和数据流，帮助开发者深入理解模型内部机制。

2. **核心功能**
- 广泛支持多种模型格式，包括 TensorFlow、PyTorch、ONNX、CoreML 等主流框架。
- 提供交互式图形界面，直观展示神经网络层结构、张量形状及权重信息。
- 支持查看模型详细属性，如层名称、输入输出维度及激活函数等关键参数。
- 具备模型验证功能，可检查模型结构的完整性与潜在错误。
- 支持离线使用，无需联网即可在本地打开和分析各类模型文件。

3. **适用场景**
- 深度学习研究人员调试模型架构，快速定位层连接错误或维度不匹配问题。
- 工程师在不同框架间转换模型时，验证转换前后结构的一致性。
- 产品经理或技术人员向非专业受众展示模型工作原理及数据流向。
- 开发者在部署模型前，审查模型复杂度以评估其在边缘设备上的可行性。

4. **技术亮点**
- 基于 JavaScript 开发，跨平台兼容性强，可在桌面端和浏览器中运行。
- 轻量级且无需安装庞大的深度学习环境，即可独立进行模型可视化分析。
- 社区活跃，持续更新对最新模型格式（如 Safetensors）的支持。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33156 | 🍴 3143 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究者提供了不可或缺的核心速查手册（Cheat Sheets）。内容涵盖从基础数学工具到高级框架使用的关键知识点汇总，旨在帮助研究人员快速回顾和查阅常用技术细节。

2. **核心功能**
- 整理并提供了机器学习与深度学习领域的关键概念速查表。
- 涵盖 NumPy、SciPy、Matplotlib 等科学计算与可视化库的基础用法。
- 包含 Keras 等主流深度学习框架的代码示例与操作指南。
- 聚焦于研究者日常所需的高频知识点，便于快速检索。

3. **适用场景**
- 机器学习或深度学习初学者快速构建知识体系框架。
- 研究人员在进行算法实现时，快速回顾特定函数或模块的语法细节。
- 面试准备期间，用于梳理和记忆核心技术要点与公式。

4. **技术亮点**
- 内容高度精炼，直接针对研究痛点，避免冗余信息。
- 整合了多领域工具链（数据处理、建模、可视化），形成一站式参考资料。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3389 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一份全面的人工智能学习路线图，整理了近200个实战案例与项目，并提供免费的配套教材，旨在帮助零基础用户入门并胜任就业实战。该项目涵盖Python、机器学习、深度学习及自然语言处理等热门技术领域，提供从理论到实践的系统化学习资源。

### 2. 核心功能
*   提供结构化的AI学习路线图，涵盖从基础数学到高级深度学习的完整知识体系。
*   收录近200个精选实战案例与项目，支持动手实践以巩固理论知识。
*   免费提供配套的教程和教材，降低学习门槛，适合零基础开发者快速上手。
*   整合主流AI框架与工具（如PyTorch、TensorFlow、Pandas等），提供广泛的技术栈支持。

### 3. 适用场景
*   **零基础转行**：希望进入人工智能领域但缺乏相关背景的初学者进行系统性入门。
*   **求职准备**：需要积累实战项目经验以提升简历竞争力、满足企业招聘需求的求职者。
*   **技能拓展**：已有编程基础，希望系统学习机器学习、计算机视觉或NLP等领域知识的开发者。

### 4. 技术亮点
*   **资源高度整合**：一站式聚合了算法、数据处理、模型训练及可视化（Matplotlib/Seaborn）等全链路工具链。
*   **实战导向**：强调“就业实战”，通过大量真实案例连接理论与工业界应用需求。
*   **多框架兼容**：同时支持TensorFlow/Keras/PyTorch/Caffe等多种主流深度学习框架，适应不同技术偏好。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13099 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- **1. 中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他人工智能模型的构建与训练过程。它通过声明式配置和自动化的机器学习流程，让开发者能够更高效地专注于数据与模型优化，而无需编写大量底层代码。

**2. 核心功能**
*   支持基于声明式 YAML/JSON 配置快速定义和训练多种类型的神经网络及 LLM。
*   提供端到端的机器学习流水线，涵盖数据预处理、模型训练、评估及超参数调优。
*   兼容主流深度学习后端（如 PyTorch），并内置对 Hugging Face 模型（如 Llama, Mistral）的微调支持。
*   具备数据为中心（Data-Centric）的分析工具，帮助识别和改进影响模型性能的关键数据特征。
*   提供可视化的实验跟踪结果，便于对比不同模型架构和配置的性能表现。

**3. 适用场景**
*   **快速原型开发**：希望不深入底层代码即可快速验证 AI 想法或测试不同模型架构的数据科学家。
*   **大语言模型微调**：需要对 Llama、Mistral 等开源 LLM 进行领域适应或特定任务优化的研究人员。
*   **企业级 AI 部署**：需要标准化、可复现且易于维护的机器学习工作流以加速模型上线的公司团队。
*   **教育与实践学习**：希望通过直观配置理解深度学习模型工作原理的学生和初学者。

**4. 技术亮点**
*   **低代码/无代码体验**：极大降低了构建复杂 AI 模型的门槛，通过结构化配置替代繁琐的代码实现。
*   **数据为中心的支持**：不仅关注模型结构，还提供工具直接分析和改进输入数据质量，提升模型效果。
*   **广泛的生态兼容性**：无缝集成 PyTorch 及 Hugging Face Transformers，支持从传统表格数据到现代 NLP/CV 任务的多样化处理。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11727 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9124 | 🍴 1233 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8913 | 🍴 3101 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8375 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6197 | 🍴 725 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个全面且实用的中文自然语言处理工具库，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证）、繁简转换及多种词库资源。它旨在为开发者提供开箱即用的 NLP 基础能力，涵盖从预处理到高级语义分析的多种功能模块。该项目同时聚合了大量优质的中文 NLP 数据集、预训练模型及学术资源，是中文 NLP 领域的重要参考仓库。

**2. 核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、语言检测、繁简转换、停用词处理及自定义词典扩展。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、地址等正则抽取，以及基于 BERT 等模型的命名实体识别（NER）。
*   **多维知识资源库**：内置中日文人名库、职业/品牌/成语/诗词等专用词库，以及中文缩写和拆字词典。
*   **语义分析与生成**：具备情感分析、关键词抽取、文本摘要生成、句子相似度匹配及基于 GPT/BERT 的文本生成能力。
*   **语音与OCR集成**：包含中文语音识别（ASR）工具链、中文手写汉字识别（OCR）及音素对齐等视听觉处理模块。

**3. 适用场景**
*   **内容安全审核**：利用敏感词库和情感分析功能，快速识别和过滤互联网平台中的违规、暴恐或负面内容。
*   **智能客服与聊天机器人**：结合实体抽取、意图识别及闲聊语料库，构建能够理解用户指令并处理复杂对话的客服系统。
*   **金融/医疗行业数据分析**：利用领域专用的词库（如金融、医学）和知识图谱工具，从非结构化文本中抽取关键实体并进行关系挖掘。
*   **文本数据清洗与增强**：使用繁简转换、拼写检查、数据增强（EDA）及正则化工具，为下游模型训练准备高质量的标准化数据集。

**4. 技术亮点**
*   **资源聚合度高**：不仅包含自研工具，还整合了清华大学 XLORE、百度、微软等机构的高质量数据集、预训练模型（BERT/ALBERT/ELECTRA）及经典论文代码。
*   **领域适应性广**：特别针对中文特性优化，提供了大量垂直领域（医疗、法律、金融、汽车）的词库和专用模型，弥补通用 NLP 工具在专业场景下的不足。
*   **全栈式 NLP 支持**：覆盖了从底层字符处理（OCR、ASR、分词）到高层语义理解（知识图谱、问答系统、生成式 AI）的全流程技术栈。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81506 | 🍴 15247 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72786 | 🍴 8887 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24节课的人工智能通识课程，旨在让所有人轻松掌握AI知识。课程采用Jupyter Notebook格式编写，内容覆盖广泛且结构清晰。

2. **核心功能**
- 提供系统化的12周学习路径，适合从零开始的学习者。
- 涵盖机器学习、深度学习、计算机视觉和自然语言处理等核心领域。
- 使用Jupyter Notebook作为主要教学载体，支持交互式代码练习。
- 由微软发起，注重教育普及与社区贡献。

3. **适用场景**
- 初学者入门人工智能基础理论与概念。
- 教育机构或教师用于开展AI通识课程。
- 希望快速了解CNN、RNN、GAN等技术应用的开发者自学。

4. **技术亮点**
- 标签体系完整，明确区分了ML、DL、CV、NLP等技术分支。
- 高星标（48779+）证明其在开源社区中的广泛认可度和影响力。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48779 | 🍴 10113 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- ### 1. 中文简介
该项目是一个定期更新的系统提示词泄露合集，收录了来自 Anthropic、OpenAI、Google、xAI 等主流厂商的大模型（如 Claude、GPT、Gemini）以及多种 AI 辅助工具的系统指令。它旨在通过公开这些内部配置，帮助开发者深入理解不同大模型的底层行为逻辑与约束机制。

### 2. 核心功能
- **多源数据聚合**：整合了 Claude、GPT、Gemini 等多款顶级大模型及 Cursor、VS Code 等开发工具的提示词。
- **定期更新维护**：保持内容时效性，持续同步最新模型版本或工具迭代中的系统指令变化。
- **开源共享**：作为免费资源库，向社区公开通常被视为机密的系统提示词细节。

### 3. 适用场景
- **提示词工程研究**：分析不同模型的系统指令结构，优化用户输入以更好地引导模型输出。
- **竞品分析与学习**：对比各家大厂在系统层面的设计差异，了解其安全策略与能力边界。
- **AI 应用开发调试**：在构建基于 LLM 的应用时，参考官方提示词逻辑以模拟或增强模型行为。

### 4. 技术亮点
- **覆盖广度极高**：不仅包含基础大模型，还囊括了 Claude Code、Cursor 等垂直领域 AI 代理的工具提示词。
- **动态更新机制**：通过定期更新应对模型快速迭代的特性，确保持续提供最新的技术情报。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 47134 | 🍴 7693 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- **1. 中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习资源库，内容深度整合了线性代数、PyTorch、NLTK 及 TensorFlow 2 等关键技术框架。该项目旨在通过理论与实践结合的方式，帮助学习者系统掌握从基础算法到深度学习的全栈技能。

**2. 核心功能**
*   **多框架支持**：集成 PyTorch 和 TensorFlow 2 等主流深度学习框架进行实战演示。
*   **经典算法覆盖**：包含 SVM、K-Means、随机森林（Adaboost）、朴素贝叶斯等传统机器学习算法实现。
*   **NLP 专项训练**：利用 NLTK 库进行自然语言处理相关的文本分析与模型构建。
*   **数学基础强化**：结合线性代数知识，深入解析 PCA、SVD 等降维与矩阵运算原理。
*   **推荐系统开发**：提供基于协同过滤或矩阵分解的推荐系统代码示例。

**3. 适用场景**
*   **机器学习初学者入门**：适合希望从零开始系统学习数据挖掘和算法原理的学生或转行者。
*   **深度学习框架迁移**：适用于需要从传统 Scikit-learn 方法过渡到 PyTorch/TensorFlow 2.x 的实践者。
*   **NLP 项目参考**：为需要快速实现文本分类、情感分析或词向量处理的技术人员提供现成代码模板。

**4. 技术亮点**
*   **全栈知识图谱**：不仅限于代码，还串联了数学基础（线性代数）与应用算法（ML/DL），构建了完整的学习闭环。
*   **高社区认可度**：拥有超过 4 万星的极高人气，证明其内容质量与教学价值得到了广泛验证。
*   **实战导向**：标签显示其涵盖从 Apriori 关联规则挖掘到 LSTM 序列建模的多样化实战场景。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42353 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36835 | 🍴 6082 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35027 | 🍴 7304 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33702 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28253 | 🍴 3426 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25782 | 🍴 2890 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个收录了500个AI项目的开源集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供配套代码。该项目通过丰富的实战案例，为开发者提供了一个全面的技术资源库，适合快速学习与应用各类人工智能技术。

### 2. 核心功能
- **海量项目集成**：汇总了500个高质量的AI相关项目，内容广泛且实用。
- **全栈技术覆盖**：包含机器学习、深度学习、计算机视觉及NLP等主流AI分支。
- **代码实例支持**：每个项目均附带源代码，便于开发者直接运行、学习和修改。
- **分类清晰明确**：通过标签系统对不同类型的AI项目进行细致划分，方便检索。
- **社区精选推荐**：作为Awesome列表之一，汇聚了社区认可的高质量项目资源。

### 3. 适用场景
- **AI初学者入门**：新手可通过阅读和运行这些项目代码，快速掌握各领域的核心技术概念。
- **工程师技术参考**：开发者在遇到具体任务时，可直接复用或借鉴其中的解决方案与代码逻辑。
- **教学与培训素材**：教师可利用这些现成的案例作为教学示例，辅助学生理解理论与实践的结合。
- **行业趋势调研**：研究人员可通过浏览项目列表，了解当前AI领域最新的应用方向和技术热点。

### 4. 技术亮点
该项目最大的亮点在于其**资源聚合性**和**实战导向**，将分散的优质AI项目集中管理，并强调“带代码”的可操作性，极大地降低了从理论到实践的学习门槛。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35027 | 🍴 7304 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款利用人工智能自动化基于浏览器的业务流程的工具。它通过结合大语言模型与浏览器自动化技术，实现了对网页交互的智能控制和执行。该项目旨在替代传统的脚本化自动化工具，提供更灵活、更具适应性的 RPA 解决方案。

2. **核心功能**
*   基于视觉识别和 LLM 理解网页结构，实现非固定选择器的稳定定位。
*   支持自然语言指令输入，将复杂的业务逻辑转化为自动化的浏览器操作序列。
*   兼容主流浏览器自动化工具（如 Playwright），并具备处理动态内容的能力。
*   提供 API 接口，便于集成到现有的工作流引擎或后端服务中。
*   具备自我纠错和重试机制，提高自动化任务在复杂网页环境下的成功率。

3. **适用场景**
*   **跨平台数据抓取**：从结构频繁变化或反爬严格的网站中自动提取数据。
*   **企业级 RPA**：自动化处理需要登录、表单填写和页面跳转的重复性行政或财务流程。
*   **测试自动化**：模拟用户行为进行端到端 UI 测试，尤其适用于难以维护的传统 Selenium 脚本场景。
*   **Web 应用集成**：在不具备官方 API 的情况下，通过浏览器操作间接与第三方 Web 服务进行数据交换。

4. **技术亮点**
*   **视觉-语言协同**：利用计算机视觉与大语言模型（LLM）的结合，实现类似人类看屏幕操作的智能决策。
*   **动态适应性**：相比传统依赖固定 XPath/CSS 选择器的工具，Skyvern 能更好地适应前端 UI 的微小变动。
*   **开源生态整合**：作为 Python 生态下的开源项目，提供了比 Power Automate 等商业软件更灵活的开发和部署方式。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22038 | 🍴 2060 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- ### GitHub 项目分析：CVAT

#### 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的首选平台，支持图像、视频及 3D 数据的标注。它提供开源、云版和企业版产品，并具备 AI 辅助标注、质量保证、团队协作及开发者 API 等强大功能。

#### 2. 核心功能
*   **多模态数据标注**：全面支持图像、视频和 3D 点云数据的标注工作。
*   **AI 辅助与自动化**：集成人工智能算法协助标注，显著提升数据处理效率。
*   **协作与管理**：内置团队协作者质机制，确保数据集的高质量与一致性。
*   **灵活部署模式**：提供开源本地部署、云端服务及企业级解决方案，满足不同规模需求。
*   **开发者友好接口**：开放 API 便于与其他深度学习框架及工作流程集成。

#### 3. 适用场景
*   **目标检测训练**：为 YOLO、Faster R-CNN 等模型准备带有边界框（Bounding Box）标注的数据集。
*   **语义分割任务**：为自动驾驶或医疗影像分析生成像素级的语义分割标注数据。
*   **大规模视频分析**：对监控视频或动作识别数据集进行帧间插值标注，减少重复劳动。
*   **3D 点云处理**：用于激光雷达数据的 3D 标注，服务于自动驾驶感知系统开发。

#### 4. 技术亮点
*   **生态兼容性强**：原生支持 PyTorch 和 TensorFlow 等主流深度学习框架，无缝衔接 Imagenet 等标准数据集。
*   **全栈式服务**：不仅提供工具，还涵盖标注服务与数据分析，形成从数据生产到模型训练的闭环。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16177 | 🍴 3725 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目旨在为计算机视觉提供高级的可解释性AI解决方案，支持CNN和Vision Transformer等主流架构。它涵盖了图像分类、目标检测、分割及图像相似度等多种任务的可视化需求。通过生成梯度加权类激活映射，帮助用户直观理解模型的决策依据。

2. **核心功能**
*   广泛支持多种深度学习模型，包括卷积神经网络（CNN）和视觉Transformer。
*   兼容多种计算机视觉任务，如图像分类、目标检测、语义分割等。
*   实现多种可解释性算法，如Grad-CAM、Score-CAM等类激活图生成方法。
*   提供直观的可视化输出，增强对深度学习模型内部决策过程的透明度。

3. **适用场景**
*   在医疗影像诊断中验证AI模型是否关注了正确的病灶区域。
*   在自动驾驶系统中调试目标检测算法，确保其识别逻辑符合人类预期。
*   在学术研究或产品演示中，向非技术人员展示图像分类模型的决策依据。

4. **技术亮点**
*   高度模块化设计，轻松适配不同的PyTorch模型结构。
*   集成了前沿的可解释性算法（如Grad-CAM++、Score-CAM），保持技术领先性。
*   拥有超过1.2万的高星标，证明了其在开源社区中的广泛认可和高实用性。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12893 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能设计的几何计算机视觉库，旨在通过 PyTorch 实现可微分的图像处理。它提供了丰富的视觉原语，支持从传统几何方法到深度学习模型的无缝集成。该库致力于简化计算机视觉在 AI 应用中的开发流程。

2. **核心功能**
*   提供基于 PyTorch 的可微分几何计算机视觉操作。
*   包含广泛的图像增强、变换和特征提取工具。
*   支持端到端的深度学习管道，便于模型训练与推理。
*   兼容多种硬件加速器，优化计算性能。
*   内置机器人视觉和空间感知相关的高级算法模块。

3. **适用场景**
*   开发需要几何约束的深度神经网络模型。
*   构建用于自动驾驶或机器人导航的空间理解系统。
*   进行大规模的图像数据增强和预处理工作流。
*   研究可微分计算机视觉算法及其在 AI 中的应用。

4. **技术亮点**
*   原生集成 PyTorch，充分利用 GPU 加速计算。
*   支持自动微分，使传统 CV 操作可直接嵌入深度学习图。
*   模块化设计，易于扩展和定制特定视觉任务。
*   活跃的开源社区贡献，持续更新最新研究进展。
- 链接: https://github.com/kornia/kornia
- ⭐ 11253 | 🍴 1192 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8871 | 🍴 2193 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3452 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3258 | 🍴 398 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2618 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2414 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持跨操作系统和平台的个人 AI 助手，强调数据自主权，让用户能够完全掌控自己的 AI 体验。它采用独特的“龙虾”理念（The lobster way），旨在提供一个灵活且私密的智能助理解决方案。

2. **核心功能**
*   **跨平台兼容性**：支持在任何操作系统和平台上运行，确保广泛的可访问性。
*   **数据所有权**：强调“own-your-data”，用户可完全控制和管理自己的私有数据。
*   **个性化 AI 助手**：作为专属的个人助理，根据用户需求提供定制化服务。
*   **开源与透明**：基于 TypeScript 开发，代码开源，便于社区贡献和安全审计。
*   **灵活部署**：支持本地化部署，降低对云端服务的依赖，提升隐私安全性。

3. **适用场景**
*   **注重隐私的个人用户**：希望在不泄露敏感数据的前提下使用 AI 助手的用户。
*   **开发者与技术爱好者**：喜欢折腾、需要高度定制化和控制权的技术人员。
*   **中小企业内部助手**：希望部署私有 AI 系统以处理内部事务的小型团队。
*   **多设备协同工作流**：需要在不同操作系统（如 Windows、macOS、Linux）间无缝切换的用户。

4. **技术亮点**
*   基于 TypeScript 构建，具有良好的类型安全和现代开发生态支持。
*   设计哲学独特，以“龙虾”为象征，强调独立、坚硬外壳（隐私保护）与灵活内里（功能强大）。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 381022 | 🍴 79808 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**
SuperPowers 是一个经过验证的代理技能框架与软件开发方法论，旨在提升开发效率。它通过结构化的技能体系和子代理驱动的开发模式，优化了从头脑风暴到代码实现的完整软件开发生命周期（SDLC）。

**2. 核心功能**
*   **代理技能框架**：提供模块化的“技能”组件，支持像乐高积木一样组合AI代理的能力。
*   **子代理驱动开发**：采用Subagent-Driven Development模式，主代理协调多个子代理并行处理复杂任务。
*   **全生命周期支持**：涵盖头脑风暴、需求分析、编码及测试等SDLC全流程，确保方法论的可落地性。
*   **结构化协作**：定义清晰的交互协议，使AI代理能够高效地进行自我反思和任务分解。

**3. 适用场景**
*   **复杂软件工程**：需要多步骤规划、代码生成和调试的大型项目开发。
*   **自动化工作流搭建**：构建基于AI的智能体系统，用于自动化执行重复性或逻辑复杂的开发任务。
*   **敏捷开发辅助**：作为团队开发的智能助手，协助进行技术选型、架构设计和代码审查。

**4. 技术亮点**
*   **方法论创新**：不仅是工具集，更是一套完整的“代理原生”软件开发范式，强调技能的可复用性。
*   **高活跃度社区**：拥有超过24万星标，证明其在AI辅助开发领域的广泛认可和技术影响力。
*   **跨语言兼容**：虽然主要使用Shell脚本实现框架逻辑，但其设计允许集成多种编程语言的代理能力。
- 链接: https://github.com/obra/superpowers
- ⭐ 241538 | 🍴 21450 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- ### 1. 中文简介
Hermes-Agent 是一个旨在随用户共同成长的人工智能代理，它通过持续的学习与交互来适应用户的需求和工作流。该项目致力于构建一个智能、灵活且具备自我演进能力的助手，能够深入理解并协助处理复杂的任务。

### 2. 核心功能
- **自适应成长机制**：代理能够根据用户的反馈和历史交互数据不断优化自身表现，实现“越用越聪明”。
- **多模型兼容支持**：集成 Anthropic (Claude)、OpenAI (GPT) 等多种主流大语言模型，提供灵活的底层推理能力。
- **智能代码与任务执行**：具备强大的代码生成、调试及复杂工作流自动化处理能力，类似 Codex 或 Claude Code 的功能。
- **个性化记忆与上下文管理**：能够长期存储用户偏好和项目上下文，确保在多轮对话中保持连贯性和个性化服务。

### 3. 适用场景
- **高级开发者辅助**：用于需要深度代码理解、重构建议及自动化脚本编写的复杂编程场景。
- **个性化智能助手**：适合希望拥有一个能记住个人习惯、项目细节并提供定制化建议的私人 AI 助理的用户。
- **跨平台 AI 集成开发**：适用于希望统一调用多个 LLM 提供商（如 OpenAI 和 Anthropic）进行混合推理的技术团队。

### 4. 技术亮点
- **模块化架构设计**：采用 Python 编写，结构清晰，便于开发者根据需求替换或扩展不同的 AI 后端模块。
- **高热度社区验证**：拥有超过 20 万星标的极高关注度，表明其在 AI Agent 领域具有广泛的影响力和成熟的生态基础。
- **前沿 Agent 范式实践**：代表了从简单聊天机器人向具备自主性、记忆力和规划能力的下一代 AI 代理演进的技术趋势。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 205754 | 🍴 37168 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平源代码工作流自动化平台，支持可视化构建与自定义代码相结合。它提供了 400 多种集成方式，用户可以选择自托管或云端部署，灵活实现业务自动化。

2. **核心功能**
*   提供可视化拖拽界面，结合自定义代码实现复杂逻辑编排。
*   内置原生 AI 能力，支持智能工作流增强与自动化处理。
*   拥有超过 400 种应用集成，覆盖主流 SaaS 工具与 API。
*   支持自托管和云服务两种部署模式，满足不同隐私与合规需求。
*   兼容 MCP（模型上下文协议），便于与大语言模型深度交互。

3. **适用场景**
*   **企业数据同步**：自动在不同系统（如 CRM、数据库、邮件）间同步和转换数据。
*   **AI 驱动的内容生成**：利用 LLM 自动生成营销文案、摘要或客户回复，并自动分发。
*   **DevOps 自动化**：触发 CI/CD 流程，监控服务器状态或自动部署更新。
*   **客户支持工作流**：自动分类工单、提取关键信息并通知相应团队成员。

4. **技术亮点**
*   **公平源代码（Fair-code）**：在保持开源协作的同时限制直接竞争用途，兼顾社区与商业利益。
*   **MCP 协议支持**：原生支持模型上下文协议，简化了 AI 模型与工作流引擎的连接。
*   **TypeScript 构建**：基于 TypeScript 开发，保证了代码的类型安全和良好的扩展性。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194552 | 🍴 58932 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于让每个人都能无障碍地使用人工智能并在此基础上进行构建，其愿景是普及 AI 技术。该项目旨在提供强大的工具支持，帮助用户将精力集中在真正重要的事务上。

### 2. 核心功能
*   **自主代理能力**：具备作为自主智能体（Autonomous Agents）运行任务的能力，无需人工持续干预。
*   **多模型兼容**：支持接入多种大型语言模型（LLM），包括 OpenAI GPT、Claude 及 Llama 等 API。
*   **通用 AI 工具集**：提供易于使用的开发工具包，降低 AI 应用的构建门槛。
*   **社区驱动开源**：拥有庞大的开发者社区和高星标的开源项目属性，便于协作与二次开发。
*   **Agentic AI 框架**：专注于智能体（Agents）领域的架构设计，实现更复杂的自动化工作流。

### 3. 适用场景
*   **自动化工作流执行**：用于自动完成需要多步骤推理和操作的复杂日常任务或数据处理流程。
*   **AI 应用原型开发**：开发者可利用其基础架构快速搭建和测试基于大语言模型的智能体应用。
*   **跨平台 AI 集成研究**：适合需要对比或整合不同 LLM（如 GPT 与 Claude）特性的技术研究场景。

### 4. 技术亮点
*   **广泛的模型支持**：不仅限于 OpenAI，还兼容 Anthropic (Claude) 和 Meta (Llama) 等多种主流 LLM 接口，提供了极高的灵活性。
*   **高关注度与成熟度**：拥有超过 18 万星标的 GitHub 项目，意味着其代码库经过大量社区验证，稳定性与生态丰富度较高。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185217 | 🍴 46121 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164522 | 🍴 21293 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163939 | 🍴 30373 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156693 | 🍴 46148 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150207 | 🍴 9363 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 147007 | 🍴 23147 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

