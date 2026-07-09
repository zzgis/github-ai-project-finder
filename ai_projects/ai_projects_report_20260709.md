# GitHub AI项目每日发现报告
日期: 2026-07-09

## 新发布的AI项目

### Homekit
- 1. **中文简介**
Homekit 为 AI 智能体提供了对 Apple Home 生态系统的直接物理控制能力，支持通过单一开放接口执行开关灯、门锁操作及读取传感器数据等任务。该项目旨在简化智能家居自动化流程，让智能体能够无缝交互于家庭设备之中。

2. **核心功能**
*   赋予 AI 智能体对 Apple Home 设备的直接物理控制权（如开关灯、锁门）。
*   支持实时读取各类环境传感器数据以实现智能化决策。
*   提供统一的开放接口，简化与 Apple HomeKit 的集成复杂度。
*   兼容主流 AI 工具链（如 Claude、Cursor、OpenClaw），便于快速部署。
*   基于 Model Context Protocol (MCP) 构建，确保标准化的上下文交互。

3. **适用场景**
*   开发者希望利用大语言模型（LLM）自动化管理家中灯光、安防等设备时。
*   需要构建具备物理操作能力的 AI 助手，以增强智能家居的互动体验。
*   在 macOS 环境下开发基于 MCP 协议的 AI 应用，并需接入家庭物联网设备时。
*   研究或实验如何将 AI 智能体与传统智能家居标准（如 HomeKit）深度整合。

4. **技术亮点**
*   采用 TypeScript 编写，具备良好的类型安全和现代 JavaScript 生态兼容性。
*   实现了对 Model Context Protocol (MCP) 的支持，这是当前 AI 应用集成的新兴标准。
*   轻量级 CLI 工具设计，便于开发者快速集成和调试。
- 链接: https://github.com/bolivestilo/Homekit
- ⭐ 66 | 🍴 1 | 语言: TypeScript
- 标签: ai-agent, apple-home, automation, claude, cli

### lapian-notes
- ### 1. 中文简介
Lapian-notes 是一款基于 AI 辅助的电影拉片工具，支持在本地进行视频抽帧处理，帮助用户深度拆解影片结构。它通过剧情泳道时间轴、结构树和情绪曲线等可视化组件，为影视分析与剧本创作提供直观的数据支持。

### 2. 核心功能
*   **本地智能抽帧**：在本地环境中高效提取视频关键帧，保障隐私并提升处理速度。
*   **多维可视化分析**：集成剧情泳道时间轴与结构树，清晰呈现叙事节奏与章节划分。
*   **AI 辅助拆解**：利用人工智能技术自动生成或优化段落深拆内容，降低拉片门槛。
*   **情绪曲线追踪**：可视化展示影片的情绪波动变化，辅助分析情感张力分布。

### 3. 适用场景
*   **影视专业学生拉片学习**：用于系统性地拆解经典影片的结构、镜头语言及叙事逻辑。
*   **编剧与导演前期筹备**：辅助分析参考影片的节奏与情绪分布，为自身剧本创作提供数据借鉴。
*   **影评人深度内容生产**：快速生成结构化的影片分析报告，提升影评的专业度与客观性。

### 4. 技术亮点
*   **现代化前端架构**：基于 TypeScript + React + Vite 构建，确保开发效率与运行性能。
*   **AI 驱动的工作流**：将大模型能力融入视频分析流程，实现从原始素材到结构化笔记的自动化转换。
- 链接: https://github.com/bkingfilm/lapian-notes
- ⭐ 44 | 🍴 9 | 语言: TypeScript
- 标签: ai, film-analysis, filmmaking, react, screenwriting

### openclaw-voice-call-realtime
- 1. **中文简介**
OpenClaw 插件为 AI 助手赋予了真实电话功能，通过 Twilio 与 OpenAI 实时语音 API 实现直拨电话。它支持通话中的工具调用、实时转录及来电筛选，让用户能像对待真人助理一样管理语音交互。

2. **核心功能**
*   基于 Twilio 和 OpenAI Realtime API 实现真实的实时电话通话。
*   在通话过程中动态执行工具和指令，增强 AI 助手的能力。
*   自动记录并生成通话文本转录，便于后续回顾与分析。
*   具备来电筛选功能，可根据预设规则过滤或处理 incoming calls。

3. **适用场景**
*   企业客服自动化：利用 AI 代理处理日常咨询和预约安排。
*   个人智能助理：为个人助手添加电话能力，以管理日程或筛选重要来电。
*   语音交互测试：开发者用于验证和优化基于 OpenAI Realtime 的语音代理应用。

4. **技术亮点**
*   无缝集成 OpenClaw 生态系统，扩展了现有 AI 代理的通信边界。
*   结合 Twilio 的通信基础设施与 OpenAI 的低延迟语音模型，实现流畅的自然对话体验。
- 链接: https://github.com/TristanBrotherton/openclaw-voice-call-realtime
- ⭐ 35 | 🍴 3 | 语言: TypeScript
- 标签: ai-agent, openai-realtime, openclaw, phone-calls, twilio

### ditto
- ### 1. **中文简介**
Ditto 是一个本地优先的工具，能够挖掘并提取 Claude Code 和 Codex 的代码日志，将其转化为个性化的 `you.md` 智能体配置文件。它旨在通过本地化数据处理，帮助开发者构建专属的 AI 编程助手档案。

### 2. **核心功能**
*   **日志挖掘**：自动扫描并解析 Claude Code 和 Codex 的历史操作日志。
*   **个人画像生成**：将提取的行为模式转化为结构化的 `you.md` 智能体配置文件。
*   **本地优先架构**：所有数据处理均在本地完成，确保数据隐私与安全。
*   **上下文工程支持**：优化提示词工程，使 AI 代理更贴合开发者的具体工作习惯。
*   **跨工具兼容**：同时支持 Anthropic 的 Claude 和 OpenAI 的 Codex 生态。

### 3. **适用场景**
*   **个性化 AI 助手定制**：开发者希望让 AI 编码代理深入了解自己的代码风格和偏好。
*   **隐私敏感型工作流**：需要在不上传数据到云端的情况下，利用历史日志训练或配置本地 Agent。
*   **提升编码效率**：通过让 AI 记住之前的上下文和技能，减少重复性提示，加快开发节奏。
*   **多工具统一配置**：在使用多个 AI 编码工具（如 Cursor、Claude Code）时，维护一致的个人设定文件。

### 4. **技术亮点**
*   **Agent Memory 实现**：通过持久化的 `you.md` 文件实现智能体的长期记忆和能力积累。
*   **Local-First 设计**：强调数据主权，无需依赖外部云服务即可运行核心功能。
*   **Skill 模块化**：将挖掘出的技能抽象为可复用的模块，便于在不同 Agent 间共享。
- 链接: https://github.com/ohad6k/ditto
- ⭐ 35 | 🍴 6 | 语言: Python
- 标签: agent-memory, agent-skills, ai, ai-agents, ai-coding

### sm120-field-guide
- 1. **中文简介**
这是一份针对基于Blackwell架构的消费者级GPU（RTX 50系列，sm_120）的AI开发实战指南。内容涵盖了从RTX 5090实测中总结的修复方案、常见陷阱以及诚实的性能数据评估。

2. **核心功能**
- 提供RTX 50系列（sm_120）架构在AI应用中的具体配置与优化建议。
- 总结开发者在实际使用中遇到的“踩坑”经验及相应的修复方法。
- 基于单张RTX 5090硬件的真实测试数据，提供客观的性能基准评估。
- 指导用户如何正确利用新一代消费级显卡进行AI模型训练或推理。

3. **适用场景**
- AI开发者在迁移或适配代码以支持NVIDIA Blackwell新架构时的环境配置参考。
- 硬件工程师或研究人员需要获取RTX 5090在真实负载下的性能基准数据。
- 计划使用消费级高端显卡搭建低成本AI工作站的用户进行前期可行性评估。

4. **技术亮点**
- 聚焦于最新的sm_120架构，填补了非数据中心级GPU在AI领域的实战文档空白。
- 强调“诚实测量”，提供来自真实硬件环境的性能数据而非理论峰值。
- 链接: https://github.com/notwitcheer/sm120-field-guide
- ⭐ 19 | 🍴 2 | 语言: 未知

### ai-guru
- 描述: 无描述
- 链接: https://github.com/Dhruvdubey17/ai-guru
- ⭐ 15 | 🍴 5 | 语言: Shell

### YSClaude
- 描述: YSClaude Expo/React Native Android AI assistant client
- 链接: https://github.com/winter-bit-cry/YSClaude
- ⭐ 15 | 🍴 3 | 语言: TypeScript

### color-correct
- 描述: 🎨 AI colorist skill for Claude Code — 9 named looks reverse-engineered from great creators. Pick a look, see the menu, or let AI decide.
- 链接: https://github.com/louisedesadeleer/color-correct
- ⭐ 11 | 🍴 1 | 语言: Python

### mors-transitions-v2026
- 描述: Declarative workflow migration tool for zero-downtime infrastructure transitions. Features dependency graph planning, two-phase commit, rollbacks, auditing, and AI integration. Supports Windows, macOS, Linux. v2026.1.
- 链接: https://github.com/tylerio1993/mors-transitions-v2026
- ⭐ 10 | 🍴 0 | 语言: HTML

### m4vgear-media-converter
- 描述: M4VGear v6.5.8: cross-platform DRM removal tool for offline media archiving. Features AI metadata enrichment, batch processing, and adaptive interface for Windows, macOS, and Linux.
- 链接: https://github.com/loganhub52/m4vgear-media-converter
- ⭐ 10 | 🍴 0 | 语言: HTML

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81692 | 🍴 15253 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个收录了500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它提供了丰富的实战案例与源代码，是开发者学习和实践人工智能技术的优质资源库。

2. **核心功能**
*   汇集大量AI领域的项目实例，包括机器学习、深度学习、计算机视觉和NLP。
*   提供完整的项目代码，方便用户直接下载、运行和学习。
*   分类清晰，涵盖从基础算法到前沿应用的多种技术方向。
*   作为Awesome List性质的资源索引，帮助用户快速定位所需的技术案例。

3. **适用场景**
*   初学者系统学习AI不同分支（如CV、NLP）的基础实现与原理。
*   工程师寻找特定任务（如图像识别、文本分类）的代码参考与灵感。
*   研究人员或学生进行技术调研时，快速评估各类AI项目的实现方案。

4. **技术亮点**
*   项目规模宏大，收录高达500个独立AI项目，覆盖面极广。
*   高人气认可度，拥有超过3.5万星标，证明其社区影响力和资源质量备受推崇。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够以直观的图形界面展示模型结构。该工具旨在帮助开发者快速理解和分析复杂的模型架构。

2. **核心功能**
*   支持 Keras、PyTorch、TensorFlow、ONNX 等多种主流框架的模型格式。
*   提供清晰的层级结构视图，直观展示网络层及其连接关系。
*   兼容 CoreML、TensorFlow Lite 等移动端及嵌入式设备模型格式。
*   内置对 NumPy 数组及 Safetensors 等新式存储格式的支持。
*   允许用户查看和编辑模型层的配置参数及权重信息。

3. **适用场景**
*   深度学习工程师调试模型结构，排查层连接错误或维度不匹配问题。
*   研究人员分析预训练模型（如 ResNet、BERT）的内部架构细节。
*   团队内部进行模型部署前的兼容性检查，确认模型是否支持目标硬件格式。
*   向非技术利益相关者展示模型工作原理，辅助技术沟通与文档编写。

4. **技术亮点**
*   基于 JavaScript 构建，无需安装复杂环境，可通过 Web 浏览器直接打开本地模型文件进行分析。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33200 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**：ONNX 是机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换与交换。它允许开发者在 PyTorch、TensorFlow 等主流框架间无缝迁移模型，提升开发效率。该标准由微软、Facebook 等科技巨头联合推动，已成为行业通用的模型格式规范。

2. **核心功能**
   - 提供跨平台的模型序列化格式，支持在不同硬件和软件环境间部署。
   - 实现主流深度学习框架（如 PyTorch、TensorFlow）与推理引擎之间的高效模型转换。
   - 定义统一的算子集和数据流图结构，确保模型语义的一致性。
   - 支持模型验证和优化，帮助检测转换过程中的潜在错误或性能瓶颈。

3. **适用场景**
   - 需要将训练好的模型从 Python 框架（如 PyTorch）部署到非 Python 环境或移动端时。
   - 希望在不重新训练的情况下，利用特定硬件加速器（如 NVIDIA TensorRT、Intel OpenVINO）优化模型推理速度。
   - 在多团队协作中，需要共享或交换预训练模型以确保兼容性时。

4. **技术亮点**
   - 拥有庞大的社区支持和广泛的框架兼容性，是事实上的行业互操作标准。
   - 支持动态形状和复杂控制流，能够灵活表达现代神经网络的多样性。
   - 提供完善的工具链（如 ONNX Runtime），实现高性能、低延迟的跨平台推理服务。
- 链接: https://github.com/onnx/onnx
- ⭐ 21116 | 🍴 3959 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一本全面开源的机器学习工程指南，旨在填补传统学术研究与工业界实战需求之间的空白。它详细涵盖了从硬件基础设施、分布式训练到模型推理等端到端的 ML 工程实践。

2. **核心功能**
*   提供大规模分布式训练的完整技术栈与最佳实践指导。
*   深入解析 GPU 集群管理、网络配置及存储优化策略。
*   涵盖大语言模型（LLM）的微调、部署及推理加速方案。
*   包含 MLOps 工具链集成及生产环境下的调试与监控技巧。

3. **适用场景**
*   构建和维护大规模深度学习集群的工程团队。
*   需要从零开始搭建 LLM 训练与推理基础设施的研究机构。
*   希望将机器学习模型高效部署到生产环境的 DevOps/MLOps 工程师。

4. **技术亮点**
*   紧密结合 PyTorch、Transformers 等主流框架与 Slurm 等调度系统。
*   聚焦于可扩展性（Scalability）和高性能计算（HPC）在 ML 中的实际应用。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18269 | 🍴 1157 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17266 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13113 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11562 | 🍴 906 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10661 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个收录了500个AI相关项目的代码合集，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。它提供了丰富的实战案例与源代码，是开发者学习和实践人工智能技术的优质资源库。

2. **核心功能**
*   汇集大量AI领域的项目实例，包括机器学习、深度学习、计算机视觉和NLP。
*   提供完整的项目代码，方便用户直接下载、运行和学习。
*   分类清晰，涵盖从基础算法到前沿应用的多种技术方向。
*   作为Awesome List性质的资源索引，帮助用户快速定位所需的技术案例。

3. **适用场景**
*   初学者系统学习AI不同分支（如CV、NLP）的基础实现与原理。
*   工程师寻找特定任务（如图像识别、文本分类）的代码参考与灵感。
*   研究人员或学生进行技术调研时，快速评估各类AI项目的实现方案。

4. **技术亮点**
*   项目规模宏大，收录高达500个独立AI项目，覆盖面极广。
*   高人气认可度，拥有超过3.5万星标，证明其社区影响力和资源质量备受推崇。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架生成的模型文件，能够以直观的图形界面展示模型结构。该工具旨在帮助开发者快速理解和分析复杂的模型架构。

2. **核心功能**
*   支持 Keras、PyTorch、TensorFlow、ONNX 等多种主流框架的模型格式。
*   提供清晰的层级结构视图，直观展示网络层及其连接关系。
*   兼容 CoreML、TensorFlow Lite 等移动端及嵌入式设备模型格式。
*   内置对 NumPy 数组及 Safetensors 等新式存储格式的支持。
*   允许用户查看和编辑模型层的配置参数及权重信息。

3. **适用场景**
*   深度学习工程师调试模型结构，排查层连接错误或维度不匹配问题。
*   研究人员分析预训练模型（如 ResNet、BERT）的内部架构细节。
*   团队内部进行模型部署前的兼容性检查，确认模型是否支持目标硬件格式。
*   向非技术利益相关者展示模型工作原理，辅助技术沟通与文档编写。

4. **技术亮点**
*   基于 JavaScript 构建，无需安装复杂环境，可通过 Web 浏览器直接打开本地模型文件进行分析。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33200 | 🍴 3153 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心知识速查手册。内容涵盖了从基础数学工具到主流框架的关键概念，旨在帮助研究者快速回顾和掌握核心技术要点。

2. **核心功能**
*   整理深度学习与机器学习领域的关键概念与公式，便于快速查阅。
*   涵盖数据科学常用库（如NumPy、SciPy、Matplotlib）的操作技巧。
*   集成主流深度学习框架（如Keras）的代码示例与最佳实践。
*   提供结构化的知识图谱，帮助研究者系统性地复习专业知识。

3. **适用场景**
*   研究人员在开始新项目前快速回顾基础理论和框架用法。
*   学生或初级工程师在学习过程中作为参考指南解决具体技术问题。
*   面试准备或技术分享时，用于梳理和展示核心知识点。
*   日常开发中遇到遗忘的语法或函数参数时进行即时查询。

4. **技术亮点**
*   内容高度浓缩，专注于“速查”特性，极大节省查阅时间。
*   覆盖范围广，整合了数学基础、数据处理及深度学习框架等多维度技能。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15410 | 🍴 3386 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
Ai-Learn 是一个面向零基础用户的人工智能学习路线图，整理了近 200 个实战案例与项目，并免费提供配套教材以助力就业。该项目涵盖 Python、数学基础以及机器学习、深度学习、计算机视觉和自然语言处理等热门领域的核心框架与工具。

### 2. 核心功能
*   **系统化学习路径**：提供从零基础到就业的全流程 AI 学习路线指引。
*   **丰富实战资源**：收录近 200 个精选实战案例和项目供学习者动手实践。
*   **免费配套教材**：所有学习资源及教材均免费提供，降低学习门槛。
*   **全栈技术覆盖**：内容横跨数据科学、算法工程及主流深度学习框架应用。

### 3. 适用场景
*   **AI 初学者入门**：适合希望系统掌握人工智能基础知识的新手。
*   **求职实战准备**：适合需要积累项目经验以提升就业竞争力的求职者。
*   **技能查漏补缺**：适合已有一定基础的学习者通过实战案例巩固特定领域知识。

### 4. 技术亮点
*   **多框架兼容**：全面支持 TensorFlow (含 TF2)、PyTorch、Keras、Caffe 等主流深度学习框架。
*   **数据生态完整**：集成 NumPy、Pandas、Matplotlib、Seaborn 等数据处理与可视化工具链。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13113 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- ### 1. 中文简介
Ludwig 是一个低代码框架，旨在简化自定义大型语言模型（LLMs）、神经网络及其他人工智能模型的构建过程。它通过声明式配置和数据驱动的方式，降低了深度学习应用的开发门槛，使开发者能够专注于数据而非复杂的底层代码实现。

### 2. 核心功能
- **低代码/无代码构建**：支持通过简单的 YAML 配置文件快速定义和训练机器学习模型，无需编写大量代码。
- **多模态支持**：原生支持处理文本、图像、音频、表格等多种数据类型，适用于自然语言处理和计算机视觉任务。
- **自动化微调与训练**：内置对主流 LLM（如 Llama 2, Mistral）的微调功能，简化了模型适配流程。
- **实验管理与评估**：提供直观的界面和工具来跟踪实验结果、超参数调整及模型性能评估。
- **集成 PyTorch 生态**：基于 PyTorch 构建，兼容现有的深度学习工具和库，便于扩展和部署。

### 3. 适用场景
- **快速原型开发**：数据科学家希望在短时间内验证想法并构建基础 ML/DL 模型，而不希望陷入繁琐的代码细节中。
- **企业级 AI 应用落地**：团队需要标准化地构建和维护多个 AI 模型（如分类器、预测器），要求高可复现性和易维护性。
- **LLM 微调服务**：开发者希望以低成本、高效率地对开源大语言模型进行垂直领域微调，无需从零开始训练。
- **教育与技术培训**：作为教学工具，帮助初学者理解深度学习概念和流程，同时减少环境配置和代码调试的时间。

### 4. 技术亮点
- **声明式 API**：采用类似 SQL 或 YAML 的配置方式定义模型结构，极大提升了开发效率和可读性。
- **数据中心设计**：强调数据质量对模型性能的影响，提供强大的数据预处理和分析工具链。
- **开箱即用的预训练模型**：内置多种经过预训练的模型组件，用户可直接调用或在此基础上进行迁移学习。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11731 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9121 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8920 | 🍴 3099 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6233 | 🍴 738 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
funNLP 是一个全面且实用的中文自然语言处理工具包，集成了敏感词检测、语言识别、实体抽取（如手机号、身份证、邮箱）及繁简转换等基础功能。它不仅提供了丰富的中文词库（如人名、地名、行业术语），还收录了大量 NLP 数据集、预训练模型资源及前沿技术报告，是中文 NLP 开发者的综合性资源库。

### 2. 核心功能
- **基础文本处理**：涵盖中英文敏感词过滤、语言检测、繁简体转换、停用词过滤及中文分词优化。
- **实体与信息抽取**：支持手机号、身份证、邮箱、人名、地名的自动化抽取，以及基于依存句法和 BERT 的事件三元组提取。
- **丰富词库资源**：内置中日文人名库、中文缩写、行业专业词库（汽车、医疗、法律等）及同/反义词库，辅助语义分析。
- **数据集与模型整合**：汇集了大量中文 NLP 竞赛数据、预训练模型（BERT/ELECTRA/ALBERT）、知识图谱构建工具及语音识别语料。
- **高级应用工具**：提供情感分析、文本相似度计算、聊天机器人构建框架、OCR 识别及自动摘要生成等实用算法与代码示例。

### 3. 适用场景
- **内容安全审核**：利用敏感词库和暴恐词表，快速实现论坛、评论区或用户注册信息的合规性过滤。
- **客服与对话系统开发**：借助聊天机器人框架、意图识别模块及大量对话语料，构建智能客服或闲聊机器人。
- **金融/医疗垂直领域分析**：利用专用的金融、医疗词库及 NER 工具，从非结构化文本中提取关键实体并进行情感或关系分析。
- **NLP 研究与教学**：作为初学者或研究人员的数据资源中心，获取最新的数据集、基准测试模型及经典论文代码复现参考。

### 4. 技术亮点
- **极高的资源聚合度**：不仅包含代码库，还整合了清华、百度等机构的知识图谱、数据集及技术报告，极具参考价值。
- **轻量化与高性能兼顾**：提供了 `jieba_fast` 等加速版分词工具及多种预训练模型，平衡了处理速度与精度需求。
- **全栈式 NLP 支持**：覆盖了从底层文本清洗、分词，到中层实体抽取、情感分析，再到上层应用（聊天机器人、摘要生成）的全流程解决方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81692 | 🍴 15253 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持100多种模型的训练，相关成果已发表于 ACL 2024。它集成了多种先进的微调技术，旨在降低大模型适配门槛并提升开发效率。

2. **核心功能**
*   支持超过100种主流大语言模型和视觉语言模型的统一微调接口。
*   内置 LoRA、QLoRA、P-Tuning 等多种参数高效微调（PEFT）策略。
*   提供全量微调、指令微调（Instruction Tuning）及基于人类反馈的强化学习（RLHF）支持。
*   集成量化技术（如 GPTQ、AWQ），支持低资源环境下的高效推理与训练。
*   兼容 Transformers 库，提供标准化的训练流程和易于使用的配置系统。

3. **适用场景**
*   开发者需要对特定领域的开源大模型（如 Llama 3、Qwen、Gemma）进行指令微调以适应业务需求。
*   研究人员希望在显存受限的设备上，通过 QLoRA 等技术高效实验不同的微调算法。
*   企业用户希望快速构建多模态应用，对包含图像理解能力的 VLM 进行端到端微调。
*   团队需要统一的基础设施来管理多个不同架构大模型的训练与评估工作流。

4. **技术亮点**
*   **统一性**：在一个框架内无缝切换不同架构模型的训练，无需为每种模型编写独立代码。
*   **高效率**：深度优化了训练过程，支持混合精度训练和梯度累积，显著降低硬件成本。
*   **前沿性**：紧跟最新模型发布（如 DeepSeek、Llama 3），并集成最新的微调范式（如 DPO、KTO）。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73096 | 🍴 8932 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### system_prompts_leaks
- **1. 中文简介**
该项目汇集了从 Anthropic、OpenAI、Google 及 xAI 等主流厂商的大型语言模型中提取的系统提示词（System Prompts），涵盖 Claude、ChatGPT、Gemini 等多个版本。内容定期更新，旨在为研究人员和开发者提供关于主流 AI 模型底层指令结构的公开参考资源。

**2. 核心功能**
*   **多厂商数据聚合**：整合了 Anthropic、OpenAI、Google、xAI 等知名 AI 公司的系统提示词。
*   **覆盖主流模型版本**：包含 Claude Code、GPT 5.5、Gemini 3.5 等具体模型的最新指令细节。
*   **定期动态更新**：持续收集并刷新新提取或泄露的系统提示词数据。
*   **开源共享社区资源**：作为“Awesome”类列表，提供结构化的提示词库供公众查阅。

**3. 适用场景**
*   **提示词工程优化**：开发者通过分析竞争对手或行业标杆的底层指令，优化自身 AI 应用的效果。
*   **AI 安全与红队测试**：安全研究人员利用已知系统提示词进行对抗性测试，评估模型的安全性边界。
*   **LLM 架构与行为研究**：学术界或技术人员通过对比不同模型的系统指令，研究大语言模型的指令遵循机制。

**4. 技术亮点**
*   **跨平台对比分析**：同时覆盖多个主要 AI 供应商，便于进行横向的技术与指令风格对比。
*   **高关注度社区资源**：拥有超过 5.4 万星的高热度，反映了其在 AI 爱好者和研究者中的广泛影响力。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 54417 | 🍴 8857 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### AI-For-Beginners
- ### AI-For-Beginners 项目分析

**1. 中文简介**
该项目是一套为期12周、包含24课时的全面人工智能入门课程，旨在让所有人轻松学习AI知识。它基于Jupyter Notebook开发，涵盖了从机器学习到深度学习的核心概念，由微软开发者社区支持。

**2. 核心功能**
*   **系统化课程体系**：提供结构化的12周学习计划，分模块讲解AI基础与进阶知识。
*   **交互式代码实践**：使用Jupyter Notebook作为主要载体，支持用户直接在浏览器中运行和修改代码。
*   **多领域技术覆盖**：内容广泛涉及机器学习、计算机视觉（CNN）、自然语言处理（RNN）及生成对抗网络（GAN）等热门方向。
*   **开源免费资源**：完全开放源代码，适合自学者和教师作为零成本的教学材料。

**3. 适用场景**
*   **初学者自学**：希望从零开始系统了解人工智能原理与实践的非专业人士或学生。
*   **高校/培训机构教学**：计算机科学或数据科学专业的教师用于补充教材或组织实验课程。
*   **企业内训入门**：科技公司或非技术部门员工进行AI基础概念普及和技能培训。

**4. 技术亮点**
*   **实战导向**：将理论概念转化为可执行的代码示例，强调“做中学”的学习模式。
*   **微软生态集成**：依托Microsoft For Beginners品牌，提供高质量、标准化的教育资源和技术支持。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 51929 | 🍴 10486 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析、机器学习实战以及深度学习的综合性学习资源库。项目内容深入结合了线性代数基础、PyTorch 和 TensorFlow 2.x 框架，并辅以 NLTK 自然语言处理工具。它旨在通过理论与实践相结合的方式，帮助学习者系统掌握从传统算法到前沿深度学习的核心技术。

2. **核心功能**
- 提供基于 scikit-learn 的经典机器学习算法（如 SVM、KMeans、逻辑回归等）实战代码。
- 包含基于 PyTorch 和 TensorFlow 2.x 的深度神经网络（DNN）、循环神经网络（RNN/LSTM）及卷积神经网络实现。
- 集成自然语言处理（NLP）模块，利用 NLTK 进行文本分析与推荐系统构建。
- 梳理机器学习所需的数学基础，特别是线性代数在算法中的应用解析。
- 涵盖数据预处理与特征工程技巧，包括 PCA 降维和 SVD 分解等实用方法。

3. **适用场景**
- 机器学习初学者系统入门，通过结构化课程从数学基础过渡到算法实战。
- 数据科学家进行模型快速原型开发，复用项目中成熟的经典算法模板。
- 深度学习研究者对比不同框架（PyTorch vs TF2）下的网络结构实现细节。
- NLP 工程师利用现有 NLTK 案例进行文本挖掘或推荐系统相关的项目探索。

4. **技术亮点**
- 实现了多种经典算法（如 AdaBoost、Apriori、FP-Growth）的从零手写与优化。
- 全面覆盖主流深度学习框架，提供 TF2 与 PyTorch 双栈的代码对照与实战案例。
- 将数学理论（线性代数）与编程实践紧密结合，强化了算法背后的原理理解。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42366 | 🍴 11539 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 37686 | 🍴 6277 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33726 | 🍴 4690 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28425 | 🍴 3457 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25853 | 🍴 2906 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ### 1. 中文简介
这是一个包含500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，并提供完整代码。该项目旨在为开发者提供全面的实践案例，帮助快速掌握人工智能核心技术。适合希望系统学习或寻找灵感的研究人员和工程师参考使用。

### 2. 核心功能
- 提供500个经过验证的AI项目代码示例，覆盖主流算法与模型。
- 分类清晰，包括机器学习、深度学习、计算机视觉和NLP四大领域。
- 所有项目均附带可运行的代码，便于直接复现和学习。
- 作为“Awesome List”类资源，汇集高质量开源项目，节省筛选时间。
- 支持Python等主流语言实现，适配广泛的技术栈需求。

### 3. 适用场景
- 初学者系统学习AI各子领域的基础项目与实践路径。
- 研究人员快速查找特定任务（如图像分类、文本生成）的参考实现。
- 工程师在开发过程中借鉴成熟解决方案以加速原型构建。
- 教育机构用于课程设计或实验教学的案例素材库。

### 4. 技术亮点
- 规模庞大且分类细致，是目前最全面的AI项目集合之一。
- 强调代码可用性，每个项目均提供实际可执行的实现细节。
- 标签体系完善，便于通过关键词精准定位所需技术领域。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35275 | 🍴 7341 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- ### 1. 中文简介
Skyvern 是一个基于人工智能的自动化平台，能够模拟人类操作来执行基于浏览器的复杂工作流。它利用计算机视觉和大语言模型技术，实现了对网页界面的智能交互与任务处理。该项目旨在替代传统的基于选择器或脚本的自动化方案，提供更灵活、更鲁棒的浏览器自动化体验。

### 2. 核心功能
*   **AI驱动的操作决策**：结合大语言模型（LLM）和计算机视觉，实时理解页面内容并做出下一步操作决策。
*   **无需手动维护选择器**：通过视觉识别元素，摆脱了对易变的CSS/XPath选择器的依赖，提高了自动化的稳定性。
*   **多步骤工作流编排**：支持定义和执行复杂的跨页面、多步骤业务流程，如数据录入、表单填写和信息抓取。
*   **开源与可扩展性**：基于Python开发，提供API接口，允许用户自定义自动化逻辑并集成到现有系统中。

### 3. 适用场景
*   **RPA流程自动化**：用于自动化企业内部需要登录多个网页系统的数据录入、报表生成等重复性办公任务。
*   **跨平台信息聚合**：从结构不固定或动态变化的多个网站中提取关键信息，适用于市场调研或竞品监控。
*   **表单自动填写与提交**：在电商、注册或申请场景中，自动完成复杂的在线表单填写和验证流程。

### 4. 技术亮点
*   **视觉+LLM双引擎架构**：创新性地结合了OpenAI等LLM的逻辑推理能力与计算机视觉的感知能力，实现对非结构化网页内容的精准操控。
*   **兼容主流自动化框架**：底层可适配Playwright等技术，既保留了传统工具的性能优势，又注入了AI的灵活性。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22161 | 🍴 2073 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 以下是关于 GitHub 项目 **cvat** 的技术分析报告：

1. **中文简介**
CVAT 是领先的计算机视觉标注平台，专为构建高质量的视觉数据集而设计。它提供开源、云及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量控制、团队协作及数据分析。

2. **核心功能**
*   支持图像、视频及 3D 点云的多模态数据标注。
*   内置 AI 辅助标注功能，显著提升标注效率与准确性。
*   提供完善的团队协作机制与全流程质量保障体系。
*   开放开发者 API，便于集成到现有的机器学习工作流中。
*   涵盖从开源工具到企业级解决方案的全栈产品形态。

3. **适用场景**
*   大规模计算机视觉数据集的自动化与半自动化标注。
*   需要多人协作进行复杂视频或 3D 场景标注的团队项目。
*   企业级 AI 研发中对数据隐私有高要求的私有化部署场景。
*   基于 PyTorch 或 TensorFlow 等框架的快速模型训练数据准备。

4. **技术亮点**
*   拥有庞大的社区支持（16k+ 星标）及丰富的标签生态（覆盖目标检测、语义分割等主流任务）。
*   原生支持多种深度学习框架（PyTorch, TensorFlow），无缝对接模型训练环节。
*   灵活的部署架构，既可作为轻量级开源工具快速上手，也可扩展为企业级高可用服务。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16244 | 🍴 3740 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- ### 1. 中文简介
该项目专注于计算机视觉领域的高级AI可解释性研究，旨在通过可视化技术揭示深度学习模型的决策依据。它不仅支持传统的卷积神经网络（CNN），还涵盖了Vision Transformers等先进架构，适用于分类、检测及分割等多种任务。通过提供直观的注意力热力图，帮助开发者深入理解模型行为并提升系统透明度。

### 2. 核心功能
*   **多架构支持**：兼容CNN、Vision Transformers等多种主流深度学习模型结构。
*   **广泛任务覆盖**：支持图像分类、目标检测、语义分割及图像相似度计算等任务。
*   **多种可视化方法**：内置Grad-CAM、Score-CAM等多种经典的类激活映射算法。
*   **高可解释性**：生成直观的注意力热力图，清晰展示模型关注的图像区域。
*   **PyTorch原生实现**：基于PyTorch框架开发，便于集成到现有的深度学习工作流中。

### 3. 适用场景
*   **医疗影像分析**：辅助医生验证AI对病灶区域的识别是否准确，增强临床信任度。
*   **自动驾驶感知系统**：可视化车辆识别模型的关注点，确保其正确聚焦于道路标志或障碍物。
*   **模型调试与优化**：帮助研究人员发现模型可能存在的偏差或错误关注区域，从而改进模型性能。
*   **合规性与审计**：满足金融、安防等领域对AI决策过程透明化和可追溯性的监管要求。

### 4. 技术亮点
*   **模块化设计**：支持快速切换不同的可视化算法（如Grad-CAM vs Score-CAM），便于对比实验。
*   **前沿架构适配**：率先支持Vision Transformers（ViT）的可解释性分析，紧跟AI技术发展趋势。
*   **社区活跃度高**：拥有超过12,000颗星标，证明其在学术界和工业界被广泛认可和引用。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12907 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专注于空间人工智能的几何计算机视觉库，旨在为 PyTorch 用户提供可微分的图像处理原语。它通过构建在深度学习框架之上，简化了传统计算机视觉算法在现代 AI 流水线中的集成与应用。

2. **核心功能**
*   提供完全可微分的几何计算机视觉操作，支持端到端的自动微分。
*   集成了多种传统的图像处理算法，如边缘检测、特征匹配和相机模型校正。
*   深度适配 PyTorch 生态，允许用户直接在神经网络中嵌入 CV 预处理和后处理步骤。
*   包含丰富的空间变换工具，用于图像增强、仿射变换及三维几何推理。

3. **适用场景**
*   **机器人视觉导航**：利用可微分相机模型和几何约束进行实时环境感知与定位。
*   **数据增强流水线**：在训练深度学习模型时，使用硬件加速且可微分的图像变换进行高效数据扩充。
*   **混合 AI-CV 系统**：开发需要结合传统几何约束与现代深度学习特征提取的混合架构应用。

4. **技术亮点**
*   **全可微设计**：打破了传统 CV 库不可导的限制，使几何运算能无缝融入梯度下降优化过程。
*   **GPU 加速原生支持**：所有操作均针对 GPU 优化，显著提升了大规模图像处理和高维张量运算的速度。
- 链接: https://github.com/kornia/kornia
- ⭐ 11271 | 🍴 1196 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8872 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3456 | 🍴 877 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3276 | 🍴 401 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2623 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2418 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，采用“龙虾方式”运行。它强调数据自主权，让用户能够完全掌控自己的 AI 助理。

2. **核心功能**
- 跨平台兼容，可在任何操作系统上部署和运行。
- 提供个性化的 AI 助手体验，支持用户自定义需求。
- 注重隐私与安全，确保用户拥有并控制自己的数据。
- 基于 TypeScript 开发，具备良好的可扩展性和维护性。

3. **适用场景**
- 开发者希望在本地环境中搭建私有化的 AI 助理以保护数据隐私。
- 企业或个人用户需要在不同操作系统间无缝切换使用统一的 AI 工具。
- 对现有云服务不满、希望完全掌控 AI 模型和数据流向的技术爱好者。

4. **技术亮点**
- 采用 TypeScript 编写，代码结构清晰且类型安全，便于二次开发和社区贡献。
- 设计架构灵活，支持模块化扩展以适应不同平台和用户需求。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 382245 | 🍴 80200 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它通过子代理驱动开发（Subagent-Driven Development）模式，构建了一套可实际落地的 AI 辅助编程工作流。该项目旨在提升软件开发生命周期中的协作效率与代码质量。

2. **核心功能**
*   提供基于智能体的技能框架，支持模块化任务拆解与执行。
*   引入子代理驱动开发理念，实现自动化代码生成与迭代优化。
*   集成头脑风暴与设计工具，辅助开发者进行需求分析与架构设计。
*   涵盖完整软件开发生命周期（SDLC），从构思到部署形成闭环。
*   利用 Shell 脚本实现轻量级集成，便于嵌入现有开发环境。

3. **适用场景**
*   需要快速原型开发并希望通过 AI 加速编码过程的团队。
*   希望规范 AI 在软件开发中角色分工的大型工程项目。
*   致力于提升代码库维护效率并减少重复性手工劳动的开发场景。
*   探索新一代人机协作编程模式及智能体工作流的研究者。

4. **技术亮点**
*   采用“子代理驱动开发”这一创新范式，细化了 AI 在 SDLC 中的职责边界。
*   标签中包含“obra”，暗示其可能具备独特的结构化输出或编排能力。
*   以 Shell 为主要实现语言，确保了极高的系统兼容性与低资源占用。
- 链接: https://github.com/obra/superpowers
- ⭐ 250064 | 🍴 22189 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **1. 中文简介**
Hermes-Agent 是一个能够伴随用户共同成长、具备持续进化能力的智能代理系统。它旨在通过深度集成多种主流大语言模型（如 Anthropic Claude 和 OpenAI ChatGPT），提供高度自适应且强大的自动化交互体验。该项目致力于成为用户个人的全能 AI 助手，随着使用频率的增加而不断优化其能力边界。

**2. 核心功能**
*   **多模型无缝集成**：支持 Anthropic、OpenAI 等主流 LLM 后端，实现灵活切换与统一调度。
*   **自适应成长机制**：具备记忆和学习能力，能根据用户历史交互数据不断优化响应策略。
*   **全栈代码辅助**：深度整合代码生成、调试及重构功能，覆盖从 Codex 到 Claude Code 等多种开发场景。
*   **自然语言交互界面**：提供类似 ChatGPT 的流畅对话体验，简化复杂指令的执行过程。

**3. 适用场景**
*   **高级开发者自动化工作流**：用于日常编码、代码审查及复杂任务链的自动化处理。
*   **个性化 AI 助理构建**：用户希望拥有一个随时间推移越来越懂自己的私人数字助手。
*   **多模型测试与比较研究**：研究人员或企业需要在一个统一框架下对比不同 LLM 的性能表现。

**4. 技术亮点**
*   **模块化架构设计**：采用插件化方式支持 Nous Research 等第三方模型及自定义 Agent 逻辑。
*   **高并发稳定性**：在拥有超过 21 万星标的高热度验证下，展现出优秀的系统健壮性。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 211707 | 🍴 38939 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- ### 1. **中文简介**
n8n 是一个拥有原生 AI 能力的公平代码工作流自动化平台，支持结合可视化构建与自定义代码开发。它允许用户选择自托管或云端部署，并提供超过 400 种集成方式。该项目旨在通过低代码/无代码工具简化复杂的数据流和业务流程自动化。

### 2. **核心功能**
*   提供可视化拖拽界面结合自定义代码，实现灵活的工作流构建。
*   内置原生 AI 能力，支持智能任务处理与分析。
*   拥有超过 400 种预置集成，无缝连接各类 API 和服务。
*   支持自托管和云服务两种部署模式，保障数据隐私与灵活性。
*   具备 MCP（模型上下文协议）客户端与服务端支持，增强与大模型的交互能力。

### 3. **适用场景**
*   **企业级数据同步与整合**：自动在不同 SaaS 应用间同步数据，消除信息孤岛。
*   **AI 驱动的业务自动化**：利用大模型能力自动处理客户咨询、内容生成或数据分析任务。
*   **DevOps 流程编排**：自动化代码测试、部署流水线及监控告警通知。
*   **个人开发者效率提升**：通过低代码快速搭建个性化助手或定时任务脚本。

### 4. **技术亮点**
*   采用 TypeScript 编写，类型安全且易于扩展和维护。
*   支持 MCP 协议，使工作流能更深度地与大型语言模型交互。
*   “公平代码”许可证设计，既开放又保护开发者权益。
*   强大的节点生态系统，覆盖广泛的技术栈和业务场景。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 195740 | 🍴 59184 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松访问、使用并构建基于 AI 的工具，其愿景是打造普惠人工智能。我们的使命是提供强大的工具支持，让用户能够专注于真正重要的核心事务。

2. **核心功能**
*   具备自主规划与执行复杂任务链的能力，实现半自动化工作流。
*   支持集成多种大型语言模型（如 GPT、Claude、Llama），提供灵活的底层架构。
*   允许用户通过自然语言指令驱动 AI 代理进行代码编写、网页浏览和数据检索。
*   提供可扩展的开发框架，方便开发者基于此构建自定义的 AI Agent 应用。

3. **适用场景**
*   自动化日常繁琐的数字任务，如信息搜集、摘要生成或邮件处理。
*   作为开发辅助工具，自动编写、调试或重构 Python 等代码片段。
*   进行市场调研或竞品分析时，自动抓取并整合互联网上的公开数据。

4. **技术亮点**
*   采用先进的 Agentic AI 架构，使 AI 具备自我反思、错误修正和长期记忆能力。
*   高度模块化的设计，兼容 OpenAI 及各类开源 LLM API，降低使用门槛。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185436 | 🍴 46115 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 165112 | 🍴 21365 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164047 | 🍴 30398 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156899 | 🍴 46168 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 151391 | 🍴 9476 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 148242 | 🍴 23357 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

