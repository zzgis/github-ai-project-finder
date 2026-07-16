# GitHub AI项目每日发现报告
日期: 2026-07-16

## 新发布的AI项目

### skills
- 1. **中文简介**
这是一个开源的 OpenAI Codex 主题定制工具，包含 AI 主题生成器和跨平台运行时环境。它允许用户为 Codex 桌面应用创建和加载自定义主题，实现界面的个性化外观。

2. **核心功能**
*   提供基于 AI 的主题生成器，可自动生成 Codex 桌面主题的样式。
*   具备跨平台运行时能力，支持在 Windows 和 macOS 上运行自定义主题。
*   集成 Chromium DevTools 协议，实现对 Codex 界面元素的深度定制与控制。
*   提供主题管理器，方便用户安装、切换和管理多个自定义皮肤。

3. **适用场景**
*   Codex 桌面用户希望根据审美偏好自定义编辑器外观和配色方案。
*   开发者需要为 Codex 应用开发新的 UI 主题并发布给社区使用。
*   研究人员或高级用户希望通过修改界面样式优化长代码编写时的视觉体验。

4. **技术亮点**
*   利用 OpenAI Codex 技能（Skill）机制实现主题的逻辑与样式分离。
*   兼容 Node.js 环境，便于通过脚本自动化生成和处理 CSS 主题文件。
- 链接: https://github.com/CodeDrobe/skills
- ⭐ 135 | 🍴 13 | 语言: CSS
- 标签: ai-coding, chromium-devtools-protocol, codex, codex-app, codex-skill

### cue
- 1. **中文简介**
Cue 是一款开源的 macOS AI 副驾驶工具，以悬浮窗口形式覆盖在屏幕之上，能够实时监听并记录会议内容。它具备隐私保护机制，可在屏幕共享时自动隐藏，是 Cluely 的替代方案，并支持用户自带 API 密钥（BYOK）。

2. **核心功能**
*   **屏幕悬浮交互**：AI 助手以小窗口形式浮于屏幕顶层，不干扰正常操作。
*   **会议实时辅助**：自动“观看”和“聆听”会议过程，提供实时摘要或互动建议。
*   **隐私安全模式**：检测到屏幕共享时自动隐藏界面，防止敏感信息泄露。
*   **自带密钥支持**：允许用户自行配置 API Key，无需依赖特定供应商服务。
*   **开源可定制**：基于开源代码构建，用户可根据需求进行修改和部署。

3. **适用场景**
*   **远程/混合办公会议**：需要实时记录会议重点且担心屏幕共享泄露隐私的用户。
*   **独立开发者与极客**：偏好自带 API Key、希望完全掌控数据流向的技术人员。
*   **Cluely 用户迁移**：寻求更灵活、开源且无厂商锁定替代方案的现有用户。
*   **多任务处理者**：希望在会议期间同时处理其他屏幕任务并获得 AI 协助的专业人士。

4. **技术亮点**
*   **跨应用感知能力**：利用 macOS 特性实现对系统内音频和视频流的捕获与分析。
*   **动态 UI 状态管理**：智能识别屏幕共享行为并即时调整界面可见性，平衡功能性与隐私性。
*   **去中心化架构**：通过支持 Bring Your Own Key (BYOK)，解耦了 AI 服务与客户端绑定，提升数据自主权。
- 链接: https://github.com/Blueturboguy07/cue
- ⭐ 134 | 🍴 28 | 语言: JavaScript

### yuwen-publish-precheck
- **1. 中文简介**
这是一款针对抖音、小红书和微信视频号的发布前内容合规审查工具，利用 AI 自动识别违规风险点并依据官方规则提供可直接使用的修改建议。项目通过 38 篇真实样本校准判定标准，并内置可查证的 72 条官方规则原文，旨在帮助用户降低踩线成本，随着使用积累本地规则库以提升准确率。需注意的是，该工具仅用于辅助优化内容合规性，不承诺绝对过审，也不提供规避审核的技巧。

**2. 核心功能**
*   **多平台合规检测**：支持对抖音、小红书及微信视频号的内容进行发布前预审。
*   **精准风险定位与溯源**：明确指出具体违规语句，并引用对应的官方规则原文作为依据。
*   **即时修改建议**：提供经过优化的、可直接替换的合规文案修改方案。
*   **本地知识库进化**：基于真实样本校准判定尺度，沉淀本地规则库，使模型越用越精准。
*   **Cursor 集成支持**：作为 Agent Skill 运行，深度集成于 Cursor 编辑器中提升工作流效率。

**3. 适用场景**
*   **自媒体运营者**：在发布短视频脚本或图文笔记前，快速筛查潜在的平台违禁词或敏感内容。
*   **内容创作者**：优化文案以降低被限流或封号的风险，同时确保内容符合平台社区规范。
*   **电商/营销团队**：批量审查产品描述或广告素材，确保在多渠道分发时均满足各平台的合规要求。

**4. 技术亮点**
*   **基于 RAG 的规则验证**：结合检索增强生成技术，确保所有判断均有官方文档原文支撑，减少 AI 幻觉。
*   **领域特定微调**：通过 38 篇高质量真实样本进行校准，专门优化了对中文互联网平台特有语境和潜规则的识别能力。
*   **IDE 原生集成**：设计为 Cursor 的 Agent Skill，允许开发者在代码编辑环境中无缝调用合规审查服务，无需切换平台。
- 链接: https://github.com/yuwen-cool/yuwen-publish-precheck
- ⭐ 105 | 🍴 7 | 语言: Python
- 标签: agent-skills, ai, chinese, claude, content-compliance

### claude-arbitrage-bot
- 1. **中文简介**
该项目是一个专为以太坊兼容网络设计的套利机器人，内置了Python自动化功能以执行交易策略。虽然主要利用Python进行自动化控制，但其核心智能合约部分采用Solidity语言编写，旨在捕捉不同链上或DEX间的价格差异获利。

2. **核心功能**
*   支持在以太坊兼容网络上自动执行跨交易所或跨链的套利交易。
*   集成Python自动化脚本，简化交易逻辑的执行与监控流程。
*   使用Solidity编写智能合约，确保资金操作在区块链上的安全与不可篡改性。
*   具备快速响应市场波动的能力，以捕捉短暂的价差机会。

3. **适用场景**
*   DeFi（去中心化金融）爱好者尝试自动化低买高卖策略以获取稳定收益。
*   开发者希望研究或复用基于Python和Solidity结合的套利机器人架构。
*   在以太坊及其他L2网络中，寻找高频交易机会的技术型交易者。

4. **技术亮点**
*   实现了Python控制层与Solidity合约层的分离与协作，兼顾开发灵活性与链上执行效率。
- 链接: https://github.com/alexafinode/claude-arbitrage-bot
- ⭐ 81 | 🍴 22 | 语言: Solidity
- 标签: ai, arbitrage, bot, btc, claude

### ai-api-relay-guide
- 1. **中文简介**
该项目是一个基于 GitHub Pages 构建的 AI API 中转站推荐平台，旨在帮助用户找到高性价比的服务接口。它通过类似“PokéAPI”的可视化评级方式，直观展示各中转站的价格优势，例如 GPT 低至原价的 0.03 倍，Claude 低至 0.2 倍。

2. **核心功能**
- 提供主流 AI 大模型 API 中转站的综合对比与推荐。
- 采用游戏化或可视化的评分机制（PokeAPI 风格）直观展示价格折扣力度。
- 支持对特定中转站进行价格评测和性价比排名。
- 基于静态网页技术实现快速加载和无后端依赖的展示。

3. **适用场景**
- 开发者寻找低成本调用 GPT 或 Claude 等模型 API 的稳定中转渠道。
- 个人用户希望以极低预算体验最新的大语言模型服务。
- 技术博主或社区运营者需要一份最新的 AI 接口价格参考指南。

4. **技术亮点**
- 利用 GitHub Pages 部署纯静态页面，无需维护服务器即可全球访问。
- 使用 CSS 进行独特的视觉设计，将枯燥的价格数据转化为直观的“评测卡片”。
- 聚焦于 AI 基础设施的横向对比，填补了市场信息不对称的空白。
- 链接: https://github.com/zhibeigg/ai-api-relay-guide
- ⭐ 75 | 🍴 0 | 语言: CSS
- 标签: ai-api, api-relay, github-pages, pokeapi

### SuperMap
- 描述: SuperMap is a living spatial memory for embodied AI — it perceives the world, remembers its evolution, and supports reasoning and action.
- 链接: https://github.com/superxslam/SuperMap
- ⭐ 57 | 🍴 1 | 语言: 未知

### Codex-Dream-Skin-Forge
- 描述: 基于 Fei-Away/Codex-Dream-Skin 二次开发的 Codex Desktop 主题工具，新增 Windows 多主题包、应用内切换、Bug 修复与 AI 辅助主题制作。
- 链接: https://github.com/tree0519/Codex-Dream-Skin-Forge
- ⭐ 45 | 🍴 8 | 语言: JavaScript

### sandbox-sdk
- 描述: A simple oss SDK for spinning sandboxes with one clean syntax.
- 链接: https://github.com/opencoredev/sandbox-sdk
- ⭐ 36 | 🍴 3 | 语言: TypeScript
- 标签: ai, ai-sdk, open, open-source, oss

### codex-dream-skin
- 描述: macOS & Windows Codex Desktop 梦幻换肤 Skill｜由世事宜AI免费提供
- 链接: https://github.com/xnydl/codex-dream-skin
- ⭐ 36 | 🍴 1 | 语言: JavaScript
- 标签: codex, codex-desktop, macos, openai, skill

### OpenMicro
- 描述: Codex Micro functionality using any Gaming Controller on any Coding Harness!
- 链接: https://github.com/stephenleo/OpenMicro
- ⭐ 32 | 🍴 2 | 语言: TypeScript
- 标签: agenticai, ai, claude, claude-code, codex

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81846 | 🍴 15248 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目汇集了丰富的实战案例，旨在为开发者提供从基础到高级的全方位学习资源。它通过集成Python代码，帮助用户快速理解并应用各类前沿人工智能技术。

2. **核心功能**
- 提供涵盖机器学习、深度学习及NLP等多个领域的500个完整项目代码。
- 包含计算机视觉和自然语言处理等特定垂直领域的专项练习案例。
- 所有项目均附带可直接运行的代码，便于用户进行本地实践与调试。
- 作为“Awesome”系列资源，分类整理了大量高质量的人工智能开源项目。

3. **适用场景**
- AI初学者希望通过大量实例快速掌握机器学习算法和编程实现。
- 研究人员或工程师需要寻找特定领域（如CV或NLP）的代码参考和灵感。
- 学生在准备相关课程作业或毕业设计时，作为项目选题和实现的辅助资料。

4. **技术亮点**
- 内容极其丰富，一次性整合数百个主流AI技术栈的实战代码。
- 标签分类清晰，精准覆盖从基础机器学习到前沿深度学习的各个细分方向。
- 高人气社区认可（35k+星标），证明其资源的质量和实用性备受开发者推崇。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35470 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。该项目因其广泛的格式兼容性和易用性而在开发者社区中广受好评。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras 和 CoreML 等。
*   提供直观的图形化界面，清晰展示神经网络的层级结构和数据流向。
*   具备强大的交互功能，允许用户点击节点查看详细参数、权重及偏差信息。
*   支持在浏览器或独立桌面应用中运行，无需安装复杂的依赖环境即可快速加载模型。

3. **适用场景**
*   模型调试与验证：在部署前检查模型架构是否正确，排查层连接错误。
*   学术交流与演示：生成清晰的模型结构图，用于论文写作、技术博客或会议展示。
*   跨框架迁移分析：对比不同框架下同一算法的结构差异，辅助模型转换工作。

4. **技术亮点**
*   极高的格式兼容性：几乎覆盖了当前所有主流的深度学习模型格式，是通用的“万能”查看器。
*   轻量化与便捷性：作为 JavaScript 驱动的项目，它能在 Web 端流畅运行，降低了用户的使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33238 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是一个用于机器学习模型互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，允许模型在不同平台间无缝转换和部署。

2. **核心功能**
- 支持将来自PyTorch、TensorFlow等主流框架的模型转换为统一格式。
- 提供跨平台执行能力，可在多种硬件后端上高效运行模型推理。
- 包含工具链用于模型优化、验证及可视化，提升开发调试效率。
- 定义了一套标准化的算子和张量规范，确保模型结构的一致性。

3. **适用场景**
- 需要在不同深度学习框架之间迁移模型代码或权重时。
- 希望在边缘设备或特定硬件加速器上部署经过训练的AI模型时。
- 构建独立的机器学习服务，要求后端框架灵活切换以降低耦合度时。

4. **技术亮点**
- 作为行业通用的中间表示层（IR），极大降低了模型部署的工程复杂度。
- 拥有庞大的社区支持和丰富的生态集成，兼容性强且持续演进。
- 链接: https://github.com/onnx/onnx
- ⭐ 21159 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一本全面涵盖机器学习工程实践的知识库。它详细讲解了从模型训练、推理部署到大规模可扩展性优化的全流程最佳实践。

2. **核心功能**
- 提供大语言模型（LLM）的训练、微调及推理的工程化指南。
- 深入解析 GPU 集群管理、网络优化及存储策略以提升系统性能。
- 涵盖 PyTorch 框架下的调试技巧、可伸缩性架构设计及 MLOps 工作流。

3. **适用场景**
- 构建和部署大规模大语言模型或深度学习应用。
- 优化高性能计算集群中的资源调度与 GPU 利用率。
- 解决复杂机器学习系统中的调试难题及可扩展性瓶颈。

4. **技术亮点**
聚焦于工业级落地，特别强调在 Slurm 等调度器下的高效集群管理及 Transformer 模型的底层工程细节。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18412 | 🍴 1175 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17322 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11577 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10665 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。该项目汇集了丰富的实战案例，旨在为开发者提供从基础到高级的全方位学习资源。它通过集成Python代码，帮助用户快速理解并应用各类前沿人工智能技术。

2. **核心功能**
- 提供涵盖机器学习、深度学习及NLP等多个领域的500个完整项目代码。
- 包含计算机视觉和自然语言处理等特定垂直领域的专项练习案例。
- 所有项目均附带可直接运行的代码，便于用户进行本地实践与调试。
- 作为“Awesome”系列资源，分类整理了大量高质量的人工智能开源项目。

3. **适用场景**
- AI初学者希望通过大量实例快速掌握机器学习算法和编程实现。
- 研究人员或工程师需要寻找特定领域（如CV或NLP）的代码参考和灵感。
- 学生在准备相关课程作业或毕业设计时，作为项目选题和实现的辅助资料。

4. **技术亮点**
- 内容极其丰富，一次性整合数百个主流AI技术栈的实战代码。
- 标签分类清晰，精准覆盖从基础机器学习到前沿深度学习的各个细分方向。
- 高人气社区认可（35k+星标），证明其资源的质量和实用性备受开发者推崇。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35470 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，帮助用户直观地查看和分析模型结构。该项目因其广泛的格式兼容性和易用性而在开发者社区中广受好评。

2. **核心功能**
*   支持广泛的主流模型格式，包括 ONNX、TensorFlow、PyTorch、Keras 和 CoreML 等。
*   提供直观的图形化界面，清晰展示神经网络的层级结构和数据流向。
*   具备强大的交互功能，允许用户点击节点查看详细参数、权重及偏差信息。
*   支持在浏览器或独立桌面应用中运行，无需安装复杂的依赖环境即可快速加载模型。

3. **适用场景**
*   模型调试与验证：在部署前检查模型架构是否正确，排查层连接错误。
*   学术交流与演示：生成清晰的模型结构图，用于论文写作、技术博客或会议展示。
*   跨框架迁移分析：对比不同框架下同一算法的结构差异，辅助模型转换工作。

4. **技术亮点**
*   极高的格式兼容性：几乎覆盖了当前所有主流的深度学习模型格式，是通用的“万能”查看器。
*   轻量化与便捷性：作为 JavaScript 驱动的项目，它能在 Web 端流畅运行，降低了用户的使用门槛。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33238 | 🍴 3157 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的知识速查表。内容涵盖了从基础数学工具到主流框架的核心概念与代码片段，旨在帮助研究者快速回顾关键知识点。

2. **核心功能**
*   整理机器学习与深度学习的核心算法及概念速查。
*   提供常用数据处理库（如NumPy、SciPy、Pandas）的操作指南。
*   包含可视化库Matplotlib的使用技巧与代码示例。
*   涵盖深度学习框架（如Keras、TensorFlow）的基础用法。
*   汇总了统计学、线性代数等数学基础的关键公式。

3. **适用场景**
*   研究人员在开始新项目前快速回顾基础知识和API用法。
*   学生或初学者用于梳理机器学习知识体系，制作复习笔记。
*   工程师在调试代码时，快速查找特定库函数的正确语法。
*   面试准备期间，系统性地复习AI领域常见的技术考点。

4. **技术亮点**
*   内容结构化清晰，以“速查表”形式呈现，极大降低了查阅成本。
*   覆盖范围广，从底层数学原理到上层应用框架均有涉及。
*   直接引用自Medium高质量文章，内容经过专业筛选与整理。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15415 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，包含近 200 个实战案例与项目，并提供免费的配套教材，帮助零基础用户入门并实现就业实战。该项目涵盖了 Python、数学基础、机器学习、数据分析及深度学习等核心领域，整合了 PyTorch、TensorFlow 等主流框架。

2. **核心功能**
- 提供结构化的 AI 学习路径，从基础到进阶系统梳理知识点。
- 收录近 200 个实战案例，支持动手实践以巩固理论知识。
- 免费提供配套学习教材和代码资源，降低学习门槛。
- 覆盖计算机视觉、自然语言处理等多个人工智能热门细分方向。

3. **适用场景**
- 希望从零开始系统学习人工智能技术的初学者。
- 需要通过大量实战项目提升动手能力以准备就业的求职者。
- 想要快速了解机器学习、深度学习等领域前沿工具与框架的学习者。

4. **技术亮点**
- 资源高度集成，将算法理论与 PyTorch、TensorFlow、Keras 等主流库结合。
- 内容覆盖面广，横跨数据科学、算法工程与深度学习应用全链条。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13149 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在帮助用户轻松构建自定义的大型语言模型（LLM）、神经网络及其他人工智能模型。它简化了机器学习工作流程，使开发者能够专注于数据与业务逻辑，而非繁琐的代码实现。

2. **核心功能**
*   **低代码/无代码构建**：通过声明式配置文件或命令行接口即可定义和训练模型，大幅降低开发门槛。
*   **广泛的模型支持**：原生支持深度学习、传统机器学习以及针对 LLaMA、Mistral 等主流大模型的微调与训练。
*   **端到端工作流**：涵盖从数据预处理、特征工程、模型训练到评估和部署的全生命周期管理。
*   **多模态处理能力**：结合计算机视觉与自然语言处理技术，支持图像、文本、表格等多类型数据的联合建模。
*   **基于 PyTorch 的核心引擎**：底层依托 PyTorch 框架，确保高性能计算与灵活的模型扩展能力。

3. **适用场景**
*   **快速原型验证**：数据科学家希望在不编写复杂代码的情况下，快速验证不同算法对特定数据集的效果。
*   **企业级 AI 应用部署**：需要稳定、可维护且易于集成的解决方案来构建生产级的推荐系统或分类器。
*   **大模型微调与优化**：研究人员或工程师需要对 LLaMA、Mistral 等开源大模型进行领域特定的指令微调或全量微调。
*   **多模态数据分析**：处理同时包含文本描述、图像和结构化表格数据的复杂业务场景，如内容审核或智能客服。

4. **技术亮点**
*   **数据为中心的设计**：强调数据配置优于代码配置，通过 YAML 文件直观管理特征与模型架构。
*   **开箱即用的组件库**：内置丰富的预定义模块（如 Embedding、Sequence、CNN 等），无需从零搭建网络层。
*   **自动化实验追踪**：集成对训练过程、指标变化和模型版本的自动记录，便于复现与分析。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11737 | 🍴 1216 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9136 | 🍴 1236 | 语言: Python
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
- ⭐ 6987 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6259 | 🍴 744 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且资源丰富的中文自然语言处理（NLP）工具库与资源汇总项目。它涵盖了从基础文本处理（如分词、敏感词检测、繁简转换）到高级语义分析（如情感分析、命名实体识别、关系抽取）的多种实用工具和预训练模型。此外，该项目还集成了大量高质量的中英文语料库、知识图谱数据及学术资源，是NLP开发者的得力助手。

2. **核心功能**
*   **基础文本处理**：提供中英文敏感词过滤、语言检测、手机号/身份证/邮箱抽取、繁简体转换及中文标点修复等功能。
*   **语义与知识图谱**：集成BERT、ALBERT等预训练模型，支持命名实体识别（NER）、关系抽取、关键词提取、文本分类及知识图谱构建工具。
*   **语料与资源库**：收录大量专业领域词库（如医学、法律、汽车、IT）、人名库、地名库、古诗词库及对话语料，并包含语音识别（ASR）相关数据集。
*   **模型与算法实现**：提供多种NLP任务的代码示例和预训练模型，包括情感分析、文本摘要、句子相似度匹配、自动对联及聊天机器人实现。

3. **适用场景**
*   **内容安全审核**：用于社交媒体或论坛的内容过滤，快速识别敏感词、暴恐词及谣言数据。
*   **智能客服与对话系统**：利用其中的对话语料、意图识别及问答系统资源，快速搭建垂直领域（如医疗、金融）的智能聊天机器人。
*   **信息抽取与结构化**：在处理非结构化文本时，利用其NER和关系抽取工具自动提取人名、地名、机构名及实体间关系，构建知识图谱。
*   **NLP研究与教学**：作为学习者或研究人员，利用其汇总的数据集、论文解读及基准测试资源，快速上手中文NLP任务或复现经典算法。

4. **技术亮点**
*   **资源高度聚合**：不仅包含代码工具，还整合了清华、百度、阿里等机构开源的高质量数据集、预训练模型及行业报告，一站式解决NLP开发中的“找数据、找模型”难题。
*   **领域覆盖广泛**：特别针对中文语境优化，提供了大量垂直领域（医疗、法律、金融）的专用词库和实体识别模型，弥补了通用NLP工具在特定行业应用的不足。
*   **紧跟前沿技术**：持续更新包含BERT、ERNIE、RoBERTa、GPT-2等最新预训练语言模型的应用示例及微调代码，确保技术栈的先进性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81846 | 🍴 15248 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的微调框架，支持对 100 多种大型语言模型（LLM）和视觉语言模型（VLM）进行训练。该项目荣获 ACL 2024 会议收录，旨在简化大模型的适配与优化流程。它集成了多种先进的微调技术，为开发者提供了一站式的解决方案。

2. **核心功能**
*   支持 100+ 种主流大模型及多模态模型的统一高效微调。
*   集成 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）方法。
*   提供 RLHF（基于人类反馈的强化学习）及 DPO 等对齐训练支持。
*   内置量化技术（如 BitsandBytes），显著降低显存占用并提升推理速度。
*   兼容 Transformers 库，提供标准化的指令微调与全量微调接口。

3. **适用场景**
*   研究人员希望快速复现或对比不同大模型在特定数据集上的微调效果。
*   开发者需要将开源模型（如 Llama、Qwen、DeepSeek）适配到垂直领域任务中。
*   资源受限环境下，通过 QLoRA 等技术进行低资源消耗的高效模型训练。
*   构建具备指令遵循能力和安全对齐特性的定制化 AI Agent 或应用后端。

4. **技术亮点**
*   **高度统一性**：在一个代码库中无缝切换百余个不同架构模型的微调任务。
*   **前沿算法集成**：原生支持最新的多模态模型及高效的 RLHF/DPO 对齐策略。
*   **极致性能优化**：结合量化技术与内存优化，实现高吞吐量与低显存占用的平衡。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73329 | 🍴 8950 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- 1. **中文简介**
该项目从Anthropic、OpenAI、Google及xAI等主流厂商的大型语言模型（如Claude、ChatGPT、Gemini等）中提取并收集了系统提示词（System Prompts）。内容涵盖Claude Code、Cursor、VS Code等多个知名AI工具的内部指令，并保持定期更新。

2. **核心功能**
*   汇集来自多家头部AI厂商的开源或泄露的系统提示词。
*   覆盖文本生成、代码辅助、设计工具等多种类型的AI应用。
*   保持高频更新以追踪最新模型版本的提示词变化。
*   为开发者提供研究LLM底层行为和安全边界的参考数据。

3. **适用场景**
*   **提示词工程研究**：分析大模型的指令遵循机制和角色设定逻辑。
*   **安全审计与红队测试**：通过理解系统指令来探测模型的越狱风险或隐私泄露漏洞。
*   **竞品分析与开发参考**：借鉴主流AI工具的系统配置以优化自研Agent的性能。

4. **技术亮点**
*   跨平台覆盖广，整合了Anthropic、OpenAI、Google、xAI等多方资源。
*   数据实时性强，针对快速迭代的AI模型提供持续的提示词快照。
*   社区驱动维护，依赖活跃的贡献者群体确保信息的时效性和完整性。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 58342 | 🍴 9635 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- 1. **中文简介**
该项目是一套为期12周、包含24节课的人工智能通识课程，旨在面向所有人普及AI知识。它由微软发起，通过结构化的学习路径帮助初学者系统掌握人工智能核心技术。

2. **核心功能**
*   提供系统化的12周学习计划，涵盖从基础概念到高级应用的完整内容。
*   基于Jupyter Notebook构建交互式学习环境，便于读者动手实践代码。
*   广泛覆盖机器学习、深度学习、计算机视觉及自然语言处理等主流AI领域。
*   引入CNN、RNN、GAN等具体神经网络架构的教学，深入解析模型原理与应用。
*   强调“AI for All”理念，降低技术门槛，适合非专业背景的初学者入门。

3. **适用场景**
*   高校或培训机构用于人工智能基础课程的教材补充与实验指导。
*   职场人士利用业余时间进行系统性AI知识自学与技能提升。
*   对机器学习感兴趣但缺乏实战经验的开发者进行入门级项目演练。
*   企业团队内部开展AI技术普及培训，统一技术认知水平。

4. **技术亮点**
*   采用Jupyter Notebook作为主要载体，实现了理论讲解与代码实践的无缝结合。
*   涵盖NLP、CV等多个前沿子领域，内容全面且紧跟技术发展潮流。
*   由微软开源支持，拥有极高的社区活跃度（超5万星标）和完善的中文翻译资源。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52374 | 🍴 10594 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个涵盖数据分析、线性代数及自然语言处理（NLTK）的全面学习资源库。它深入实践了从传统机器学习算法到深度学习框架（如PyTorch和TensorFlow 2）的核心内容。旨在通过代码实战帮助开发者系统掌握人工智能领域的关键技术与理论。

2. **核心功能**
*   集成Scikit-learn与自定义实现，覆盖SVM、K-Means、逻辑回归等经典机器学习算法。
*   基于PyTorch和TensorFlow 2进行深度学习实战，包括DNN、RNN、LSTM等神经网络结构。
*   结合NLTK库提供自然语言处理（NLP）相关的文本分析与推荐系统案例。
*   包含线性代数基础数学原理讲解，为算法理解提供坚实的理论支撑。
*   展示Adaboost、Apriori、FP-Growth等集成学习与关联规则挖掘的具体应用。

3. **适用场景**
*   希望系统构建机器学习知识体系并对照数学原理进行深度学习的初学者。
*   需要快速复现经典AI算法代码以用于教学演示或技术面试准备的开发者。
*   致力于研究自然语言处理（NLP）与推荐系统实战应用的工程技术人员。
*   对比不同深度学习框架（PyTorch vs TensorFlow）实现细节的研究者。

4. **技术亮点**
*   实现了“理论+代码”的双重闭环，不仅提供算法代码，还辅以线性代数等底层数学解释。
*   兼容主流深度学习框架，同时支持Scikit-learn等轻量级库，适应不同阶段的学习需求。
*   标签丰富且分类细致，涵盖了从传统统计学习到前沿深度学习的完整技术栈。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42383 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 38508 | 🍴 6458 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35470 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33746 | 🍴 4692 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28615 | 🍴 3492 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25915 | 🍴 2924 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它作为一个“Awesome”列表，为开发者提供了丰富的实战案例和源代码参考。

2. **核心功能**
*   提供500个完整的AI项目代码，覆盖主流算法与应用。
*   集成机器学习、深度学习、计算机视觉及NLP等多领域资源。
*   包含经过验证的代码实现，便于直接运行与学习。
*   作为精选列表（Awesome List），结构化地组织各类AI项目。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握理论与实践。
*   研究人员需要参考特定领域的现成代码以加速实验进程。
*   开发者在构建新应用时寻找可用的基础模块或灵感。
*   教育机构将其作为课程教学的多模态案例库。

4. **技术亮点**
*   极高的社区认可度（35,470+星标），证明其资源质量与实用性。
*   全面覆盖从传统机器学习到前沿深度学习的完整技术栈。
*   提供Python生态下的多领域交叉应用示例。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35470 | 🍴 7355 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一款基于人工智能的自动化平台，旨在通过视觉理解和大型语言模型（LLM）自动执行基于浏览器的复杂工作流。它无需编写传统代码，即可像人类用户一样与网页进行交互，从而简化重复性的在线任务。

### 2. 核心功能
*   **无代码浏览器自动化**：利用 AI 视觉能力识别页面元素并执行操作，无需维护脆弱的 CSS 选择器或 XPath。
*   **智能工作流编排**：支持构建和自动化复杂的跨网站业务流程，具备上下文理解和容错能力。
*   **多引擎兼容**：底层兼容 Playwright 等主流浏览器自动化工具，同时集成 GPT 等 LLM 以增强决策能力。
*   **企业级 RPA 替代方案**：作为传统 RPA 工具（如 Power Automate）的现代替代品，提供更灵活且低维护成本的解决方案。
*   **API 驱动集成**：提供 API 接口，便于将浏览器自动化能力无缝集成到现有的应用程序或后端服务中。

### 3. 适用场景
*   **数据抓取与录入**：自动从多个网站抓取非结构化数据并填入内部系统或表单，替代手动复制粘贴。
*   **跨平台流程自动化**：执行涉及多个不同网站的复杂任务，例如在电商平台下单后自动在物流网站跟踪包裹。
*   **IT 运维与测试**：自动化执行浏览器端的回归测试或日常系统巡检任务，减少人工干预。
*   **行政事务处理**：自动完成报销申请、预订差旅、填写政府表格等重复性高且规则明确的办公流程。

### 4. 技术亮点
*   **视觉 AI 驱动**：结合计算机视觉与大语言模型，能够“看懂”网页布局并进行动态交互，而非依赖静态 DOM 结构。
*   **自我修复与适应性强**：当网页 UI 发生变化时，AI 仍能根据视觉语义识别元素，显著降低自动化脚本的维护成本。
*   **开源生态整合**：深度整合 Playwright 和主流 LLM 框架，开发者可利用 Python 生态系统轻松扩展功能。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22412 | 🍴 2097 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的领先平台，支持图像、视频及 3D 数据的 AI 辅助标注与质量控制。它提供开源、云端和企业版产品及服务，具备团队协作、数据分析及开发者 API 等功能。

2. **核心功能**
*   支持图像、视频和 3D 数据的多维度标注与 AI 辅助标签生成。
*   提供开源、云端及企业级多种部署方案以适配不同规模需求。
*   内置质量保证机制与团队协作工具，提升数据标注效率。
*   开放开发者 API，便于集成到现有的机器学习工作流中。

3. **适用场景**
*   为计算机视觉模型训练构建大规模、高精度的标注数据集。
*   需要协作完成复杂图像或视频标注任务的团队与企业。
*   希望利用预训练模型进行半自动标注以加速数据处理流程的场景。

4. **技术亮点**
*   深度集成 PyTorch 和 TensorFlow 等主流深度学习框架以支持智能标注。
*   涵盖从目标检测到语义分割等多种前沿标注任务类型。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16309 | 🍴 3762 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目是一款面向计算机视觉的高级AI可解释性工具库。它广泛支持卷积神经网络（CNN）、视觉Transformer等多种架构，涵盖分类、检测及分割等任务，旨在提升深度学习模型的透明度。

2. **核心功能**
*   提供Grad-CAM、Score-CAM等多种可视化算法以生成类激活图。
*   全面兼容CNN与Vision Transformers等主流深度学习模型架构。
*   支持图像分类、目标检测、语义分割及图像相似度计算等多种任务。
*   致力于实现模型内部决策逻辑的可解释性与直观可视化。

3. **适用场景**
*   研究人员需要调试和优化计算机视觉模型的注意力机制时。
*   医疗影像或自动驾驶领域要求对AI决策过程进行合规性审计时。
*   开发者希望向非技术利益相关者展示模型关注点以提升信任度时。

4. **技术亮点**
*   高度模块化设计，支持即插即用于各种PyTorch模型。
*   同时支持传统CNN与现代Vision Transformer架构的可视化分析。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12914 | 🍴 1706 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个面向空间人工智能（Spatial AI）的几何计算机视觉库。它基于 PyTorch 构建，旨在提供可微分的图像处理与计算机视觉算法，以支持深度学习工作流。

2. **核心功能**
*   提供大量可微分的几何计算机视觉算子，便于集成到神经网络中。
*   支持多种图像处理任务，如滤波、变换和形态学操作。
*   兼容 PyTorch 生态，允许在 GPU 上高效进行批量数据处理。
*   内置用于机器人学和摄影测量的相机标定与投影工具。

3. **适用场景**
*   需要端到端可训练计算机视觉管道的深度学习研究。
*   涉及图像增强、去噪或风格迁移等预处理任务的机器学习流程。
*   机器人导航中的视觉伺服或 SLAM（同步定位与建图）系统开发。
*   医学影像分析中需要对解剖结构进行几何变换的场景。

4. **技术亮点**
*   **可微分性**：所有核心算子均为可微分，可直接作为层嵌入 PyTorch 模型进行反向传播优化。
*   **高性能并行计算**：充分利用 GPU 加速，适合处理大规模图像数据批处理。
*   **模块化设计**：提供从底层像素操作到高层几何推理的完整工具链，简化复杂视觉算法的实现。
- 链接: https://github.com/kornia/kornia
- ⭐ 11276 | 🍴 1202 | 语言: Python
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
- ⭐ 3284 | 🍴 403 | 语言: Python
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
OpenClaw 是一款全平台、跨操作系统的个人 AI 助手，旨在让用户以“龙虾方式”完全掌控自己的数据。它基于 TypeScript 开发，强调隐私与自主权，确保用户拥有对自己 AI 助手的绝对控制权。

**2. 核心功能**
*   **跨平台兼容**：支持任意操作系统和平台，实现无缝部署。
*   **数据主权**：强调“Own Your Data”，确保用户数据私有化且不受第三方监控。
*   **个性化定制**：作为专属个人助理，可根据用户需求进行深度定制。
*   **开源透明**：基于开放源代码构建，代码可审计，增强用户信任。
*   **AI 集成**：整合先进的人工智能能力，提供智能交互体验。

**3. 适用场景**
*   **隐私敏感用户**：需要完全控制个人数据、拒绝云端监控的技术爱好者。
*   **开发者工作流**：希望将 AI 助手集成到本地开发环境中的程序员。
*   **个人知识管理**：寻求高效、私密的个人助理来整理信息和辅助决策的用户。
*   **企业内网部署**：需要在内部网络中运行 AI 工具且不允许数据外传的企业场景。

**4. 技术亮点**
*   采用 TypeScript 编写，保证类型安全和现代开发体验。
*   架构设计灵活，支持在任意 OS 上本地化运行，降低依赖风险。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383144 | 🍴 80464 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- ### 1. **中文简介**
Superpowers 是一个经过实战验证的智能体技能框架及软件开发方法论。它通过子代理驱动的开发模式，将 AI 智能体深度整合到软件开发生命周期（SDLC）中。该项目旨在提供一种结构化的“脑力激荡”与编码协作流程，以提升开发效率。

### 2. **核心功能**
- **子代理驱动开发**：利用专门的子智能体执行特定任务，实现模块化且自动化的代码生成与维护。
- **全流程技能框架**：提供从构思、编码到测试的完整 SDLC 技能集，支持标准化的开发工作流。
- **结构化脑力激荡**：内置辅助 AI 进行需求分析与方案探讨，帮助开发者在编码前明确逻辑与架构。
- **Shell 脚本集成**：主要通过 Shell 脚本编排智能体交互与任务执行，确保轻量级且易于部署。
- **可复用的开发方法论**：不仅是一个工具，更提供了一套经过验证的、将 AI 融入传统软件工程的最佳实践。

### 3. **适用场景**
- **AI 辅助软件工程**：团队希望将大语言模型（LLM）系统性地引入现有开发流程，而非仅作为简单的代码补全工具。
- **复杂项目架构设计**：需要在编码前进行深入的逻辑推演和方案设计，利用智能体协助梳理需求和技术选型。
- **自动化开发工作流搭建**：开发者希望构建基于智能体的自动化流水线，实现从需求到代码生成的半自动化处理。
- **新兴开发范式探索**：对“子代理驱动开发”等前沿概念感兴趣，希望尝试更高效的多智能体协作模式的研究者或团队。

### 4. **技术亮点**
- **方法论与工具结合**：区别于单纯的 AI 编程助手，它提供了一套完整的“技能框架”和开发哲学，强调过程的可控性。
- **高社区认可度**：拥有超过 25 万星标，证明了其在开发者群体中的广泛影响力和实用性验证。
- **专注“能工作”的落地性**：项目口号强调“works”，表明其设计初衷是解决实际工程问题，而非仅停留在理论演示。
- 链接: https://github.com/obra/superpowers
- ⭐ 255929 | 🍴 22885 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够随用户共同成长并自适应演进的智能代理工具。它深度集成多种主流大语言模型（如 Claude、ChatGPT 等），旨在通过持续学习和交互优化来辅助开发者提升工作效率。

2. **核心功能**
*   支持多模型无缝切换与集成，兼容 OpenAI、Anthropic 等主流 LLM 服务。
*   具备自我进化能力，能根据用户的使用习惯和反馈不断优化代码生成与任务执行表现。
*   提供智能化的代码辅助功能，包括自动补全、错误调试及复杂逻辑重构。
*   拥有高度可定制的代理配置，允许用户根据特定项目需求调整工作流。

3. **适用场景**
*   需要高效代码生成与自动化测试的大型软件开发项目。
*   希望利用 AI 辅助进行日常编程任务、减少重复性劳动的开发者个人工作流。
*   企业级团队中用于统一编码规范和提高协作效率的智能助手部署。

4. **技术亮点**
*   采用先进的上下文管理技术，确保在多轮对话中保持长期记忆与逻辑一致性。
*   架构设计注重可扩展性，支持插件式扩展以适配各种新的 AI 模型或服务接口。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 215887 | 🍴 40300 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持可视化构建与自定义代码相结合。它提供超过 400 种集成方式，允许用户选择自托管或云端部署，灵活满足各种自动化需求。

2. **核心功能**
*   提供可视化工作流构建器，降低自动化开发门槛。
*   内置原生 AI 能力，可直接在流程中调用智能模型。
*   拥有 400 多种预置集成，兼容主流 API 和数据源。
*   支持自托管与云服务两种部署模式，保障数据隐私与灵活性。
*   融合低代码与无代码特性，并允许嵌入自定义代码逻辑。

3. **适用场景**
*   企业级数据同步与 ETL 处理，实现多系统间的数据自动流转。
*   构建基于 AI 的智能客服或内容生成工作流，提升响应效率。
*   开发者快速搭建自定义 API 网关或后端逻辑，简化集成过程。
*   IT 团队自动化日常运维任务，如监控报警、日志分析与备份。

4. **技术亮点**
*   采用 TypeScript 开发，确保类型安全与良好的可扩展性。
*   支持 MCP（Model Context Protocol），增强与大语言模型的交互能力。
*   开源且“公平代码”授权，兼顾社区协作与企业商用需求。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 196690 | 🍴 59373 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于实现“人人可用的AI”这一愿景，让用户能够轻松使用并在此基础上进行构建。其使命是提供必要的工具，使用户能够将精力集中在真正重要的事项上。

### 2. 核心功能
*   具备自主代理能力，能够独立规划并执行复杂的多步任务。
*   支持集成多种大型语言模型（如 GPT、Claude、Llama），提供灵活的底层选择。
*   作为开源框架，允许开发者基于其架构自定义和扩展 AI 应用。
*   通过自动化工作流减少人工干预，提升重复性任务的执行效率。

### 3. 适用场景
*   **自动化内容创作**：自动完成市场调研、文章撰写及社交媒体发布等连贯性工作流。
*   **复杂数据研究**：自主联网搜索、整理并总结分散在互联网上的多源信息。
*   **代码开发与调试**：辅助程序员生成代码片段、审查错误或自动化部署流程。
*   **个人助理服务**：处理日程管理、邮件回复或在线预订等日常琐事。

### 4. 技术亮点
*   **多模型兼容性**：原生支持 OpenAI、Anthropic (Claude) 及 Llama 等主流 API，降低厂商锁定风险。
*   **高度可扩展性**：模块化设计使得开发者可以轻松添加新功能或替换特定组件。
*   **自主决策机制**：利用大语言模型的推理能力，实现任务分解与自我修正的逻辑闭环。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185578 | 🍴 46079 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165865 | 🍴 21454 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164275 | 🍴 30527 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157080 | 🍴 46172 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151961 | 🍴 9682 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 151894 | 🍴 8673 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

