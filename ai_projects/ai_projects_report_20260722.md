# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- 1. **中文简介**
Thinking-orbs 专为 AI 及智能体用户界面设计的点状思考加载指示器，包含六种经过调优的动画状态。它支持两种尺寸，并具备自动适配深色与浅色模式的能力，为等待过程提供流畅的视觉反馈。

2. **核心功能**
*   提供六种精心调优的动画状态以模拟“思考”过程。
*   内置自动深色/浅色模式切换，适应不同 UI 主题。
*   支持两种预设尺寸，灵活适配不同布局需求。
*   基于 TypeScript 开发，类型安全且易于集成。
*   轻量级的点状加载组件，专注于提升用户体验。

3. **适用场景**
*   AI 聊天机器人或生成式 AI 应用的响应等待阶段。
*   智能体（Agent）执行复杂任务时的后台处理提示。
*   需要区分“加载中”与“思考中”状态的现代 Web 界面设计。
*   追求极简主义且需兼容暗黑模式的 SaaS 平台仪表盘。

4. **技术亮点**
*   针对 AI 交互语境优化的微动画状态机，比传统旋转加载更具语义化。
*   原生支持 CSS 变量自动响应主题切换，无需额外配置逻辑。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 540 | 🍴 35 | 语言: TypeScript

### BossConsole
- 1. **中文简介**
BossConsole 是一个开源、跨平台的 AI 智能体控制台，基于 JVM（非 Electron）构建，支持多线程操作。它旨在提供原生体验，让用户能够运行 Claude Code、Codex、Gemini 等主流 AI 编程助手，并集成真实浏览器、终端及编辑器功能。该项目专为大型企业、科学研究及复杂工作流设计，提供丰富的工具支持和安全管控能力。

2. **核心功能**
*   **多智能体支持**：原生兼容 Claude Code、Codex、Gemini 和 OpenCode 等多种主流 AI 编程工具。
*   **全栈开发环境**：内置真实浏览器渲染、终端交互、代码编辑器以及密钥管理功能。
*   **扩展性极强**：集成 Model Context Protocol (MCP) 标准，支持 100+ 种工具插件。
*   **企业级安全**：提供基于角色的访问控制（RBAC），确保大型团队或敏感数据场景下的安全性。
*   **高性能架构**：采用 Kotlin Multiplatform 和 Compose Multiplatform 技术，实现 JVM 原生多线程运行，避免 Electron 的资源开销。

3. **适用场景**
*   **企业级 AI 开发平台**：需要统一管理员工 AI 工具权限、日志及安全策略的大型科技公司。
*   **科研与数据分析**：研究人员利用 MCP 工具链和真实浏览器进行自动化数据采集、实验执行及结果分析。
*   **复杂工作流自动化**：开发者需要将多个 AI 助手（如代码生成与测试）串联，并通过终端和浏览器协同操作的场景。
*   **高性能桌面应用需求**：对启动速度和内存占用有严格要求，希望摆脱 Electron 框架束缚的桌面端 AI 助手用户。

4. **技术亮点**
*   **JVM 原生而非 Electron**：利用 Kotlin Multiplatform 和 Compose Multiplatform 构建，提供更低的资源消耗和更原生的跨平台性能。
*   **真正的多线程操作**：底层架构支持高并发任务处理，适合复杂的并行 AI 推理和操作。
*   **热重载（Hot-Reload）**：支持开发过程中的即时反馈，提升调试和迭代效率。
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 150 | 🍴 2 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### open-ai-canvas
- 1. **中文简介**
Open-ai-canvas 是一款专为 AI 影视创作设计的开源无限画布工作台。它深度集成了多模态内容生成、分镜编排、素材管理以及 Agent 自动化工作流功能。该项目旨在为创作者提供一个高效、灵活的可视化创作环境，以加速从构思到成片的流程。

2. **核心功能**
*   **多模态生成集成**：支持文本、图像等多种媒体形式的 AI 自动生成与处理。
*   **分镜可视化编排**：提供无限画布界面，便于用户直观地规划和管理影视分镜顺序。
*   **智能素材管理**：集中化管理项目所需的各类视觉及音频素材，提升检索与调用效率。
*   **Agent 工作流自动化**：通过集成 AI Agent 实现复杂创作任务的自动化流转与执行。

3. **适用场景**
*   **AI 短片制作**：创作者利用画布快速生成并组合分镜，制作高质量的 AI 短视频或动画。
*   **影视前期策划**：导演或策划人员使用工具进行剧本拆解、分镜预演和视觉风格探索。
*   **自动化内容流水线**：团队搭建基于 Agent 的自动化工作流，批量生成和处理视频素材。

4. **技术亮点**
*   采用 TypeScript 开发，保证了代码的类型安全和可维护性。
*   基于“无限画布”理念设计，突破了传统线性编辑的限制，提供更自由的创意空间。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 66 | 🍴 18 | 语言: TypeScript

### pgContext
- 1. **中文简介**
pgContext 是一个内置于 PostgreSQL 数据库的全功能 AI 搜索引擎。它利用 Rust 语言开发，旨在将先进的自然语言处理能力直接集成到现有的关系型数据库架构中。这使得用户能够通过语义搜索高效地查询和管理数据。

2. **核心功能**
- 提供基于自然语言的语义搜索能力，支持超越传统关键词匹配的数据检索。
- 原生集成于 PostgreSQL 中，无需外部复杂架构即可运行。
- 采用 Rust 语言构建，确保高性能执行与内存安全。
- 支持在数据库内部直接处理 AI 相关的查询逻辑，简化部署流程。

3. **适用场景**
- 需要直接在数据库层实现智能问答或语义检索的企业级应用。
- 希望减少微服务架构复杂度，避免引入独立向量数据库或搜索引擎的项目。
- 对数据隐私和安全性要求极高，希望数据不出库即可进行 AI 处理的场景。

4. **技术亮点**
- 使用 Rust 编写，相比其他语言（如 Python 扩展）通常具有更高的运行效率和更低的资源消耗。
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 61 | 🍴 3 | 语言: Rust

### AIGuardSIEM
- 1. **中文简介**
AIGuardSIEM 是一个面向生产环境的高性能 SIEM/XDR 平台，支持每秒百万级事件（EPS）的摄入，并实现低于 15 毫秒的检测延迟。该项目基于 C++、Go 和 Python 构建，旨在提供企业级的安全监控与响应能力。

2. **核心功能**
*   利用 DPDK 技术实现高速网络流量捕获，满足高吞吐需求。
*   集成 ONNX 机器学习推理引擎，用于实时的异常与恶意软件检测。
*   支持 Sigma 规则引擎，便于标准化和快速部署检测逻辑。
*   结合 eBPF 技术进行深度端点监控，提升系统可见性。
*   内置 SOAR（安全编排、自动化及响应）功能，实现自动化事件处置。

3. **适用场景**
*   需要处理海量日志数据且对检测实时性要求极高的大型企业 SOC 中心。
*   部署在 Kubernetes 集群中的现代化云原生安全基础设施。
*   希望利用机器学习辅助传统规则进行高级威胁狩猎的安全团队。
*   需要统一网络流量分析与端点行为监控的 XDR 解决方案提供商。

4. **技术亮点**
*   **极致性能**：C++ 底层结合 DPDK 加速，确保在 1M+ EPS 下保持亚毫秒级延迟。
*   **混合架构**：融合 C++（高性能）、Go（并发服务）和 Python（脚本/ML）的优势。
*   **前沿监控**：采用 eBPF 技术实现无侵入式的高精度系统级监控。
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 54 | 🍴 4 | 语言: C++
- 标签: anomaly-detection, cybersecurity, dpdk, endpoint-security, incident-response

### editaplot
- 描述: AI-guided editable scientific figures with Codex and local Origin/OriginPro
- 链接: https://github.com/hang-jin/editaplot
- ⭐ 40 | 🍴 2 | 语言: Python
- 标签: codex-skill, editable-figures, research, scientific-visualization, windows

### pm-manager
- 描述: Know what to fix next — local .pm governance skill pack for AI coding agents (Spec Kit–inspired).
- 链接: https://github.com/wei63w/pm-manager
- ⭐ 36 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude-code, cursor, project-management

### Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- 描述: The Industry‑Oriented AI Engineering Program blends theory with hands‑on projects. Students gain expertise in open‑source LLMs, prompt engineering, fine‑tuning, and agent development, preparing for impactful careers in healthcare AI, autonomous systems, and innovation.
- 链接: https://github.com/AnantVerma-2022/Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- ⭐ 33 | 🍴 0 | 语言: Jupyter Notebook

### AIS3-2026-Material
- 描述: AIS3 2026 - AI 資安應用實作與模型安全
- 链接: https://github.com/stwater20/AIS3-2026-Material
- ⭐ 30 | 🍴 0 | 语言: Jupyter Notebook

### style-pack-skill
- 描述: 从参考图提取视觉风格 DNA，强制生成标注与纯色双版色卡的 AI Agent Skill
- 链接: https://github.com/irenerachel/style-pack-skill
- ⭐ 30 | 🍴 6 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目代码的精选资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目通过提供完整的代码实现，旨在帮助开发者快速上手并深入理解各类人工智能算法的实际应用。

2. **核心功能**
- 提供500多个现成的AI项目代码示例，覆盖主流技术栈。
- 分类清晰，细分为机器学习、深度学习、计算机视觉和NLP四大板块。
- 包含“Awesome”列表属性，经过筛选的高质量项目集合。
- 主要基于Python语言实现，便于数据科学从业者直接使用。

3. **适用场景**
- AI初学者希望通过实际代码案例快速掌握各子领域的基础知识。
- 开发者在构建具体AI应用时，寻找可参考或复用的代码模板。
- 研究人员需要快速验证某种算法（如图像识别或文本处理）的实现逻辑。

4. **技术亮点**
- 规模宏大且分类全面，是一站式学习AI多分支技术的优质索引库。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，帮助用户直观地查看和分析模型结构。

2. **核心功能**
*   支持广泛格式的模型可视化，包括 CoreML、ONNX、PyTorch、TensorFlow 等。
*   提供清晰的图形化界面，展示网络层连接及数据流向。
*   兼容多种深度学习框架，如 Keras、TensorFlow Lite 及 Safetensors。
*   基于 JavaScript 构建，便于在 Web 端或桌面端快速部署和使用。

3. **适用场景**
*   开发者调试复杂神经网络结构，排查层级连接错误。
*   研究人员展示模型架构，用于论文配图或技术分享。
*   工程团队在不同模型格式（如从 PyTorch 转换到 ONNX）之间验证转换结果的一致性。

4. **技术亮点**
*   高度兼容主流 AI 生态，几乎覆盖所有常用的深度学习框架和导出格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型交换与运行。它允许开发者在不同硬件平台和工具链之间无缝迁移模型，打破框架壁垒。

2. **核心功能**
- 提供统一的模型格式，实现PyTorch、TensorFlow等主流框架间的模型转换。
- 支持跨平台部署，确保模型在多种硬件加速器上的高效推理。
- 包含完整的算子集定义，覆盖从训练到推断的常见神经网络层。
- 提供工具链支持，便于模型的验证、优化和性能分析。

3. **适用场景**
- 需要将模型从开发框架（如PyTorch）迁移到生产环境部署框架时。
- 在多硬件异构环境中运行深度学习模型，如从CPU转向GPU或专用AI芯片。
- 希望避免被单一厂商框架锁定，追求模型长期可移植性的项目。
- 进行模型性能基准测试和跨框架对比分析的研究场景。

4. **技术亮点**
- 作为行业事实标准，被微软、Facebook、Amazon等主要科技公司广泛采用和支持。
- 拥有活跃的开源社区和丰富的生态系统，持续更新以支持最新深度学习技术。
- 链接: https://github.com/onnx/onnx
- ⭐ 21196 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《Machine Learning Engineering Open Book》是一本关于机器学习工程实践的开源书籍。它系统性地涵盖了从基础设施配置到模型训练、调试及部署的全流程最佳实践。该项目旨在为构建可扩展且高效的ML系统提供权威指南。

2. **核心功能**
- 深入解析大规模语言模型（LLM）的训练与推理优化策略。
- 提供针对GPU集群、存储和网络的高性能基础设施配置方案。
- 详细介绍使用PyTorch和Transformers进行分布式训练的技术细节。
- 包含实用的MLOps工具链集成与Slurm作业调度管理指南。
- 分享模型调试技巧及提升系统可扩展性的工程实践建议。

3. **适用场景**
- 需要从零搭建高性能机器学习集群的数据科学家和工程师。
- 致力于优化大型语言模型训练效率并降低计算成本的团队。
- 希望将ML模型规模化部署到生产环境以支持高并发推理的场景。
- 寻求标准化MLOps流程以提升模型迭代速度和稳定性的企业。

4. **技术亮点**
- 内容紧跟前沿AI工程趋势，特别聚焦于LLM时代的特定挑战与解决方案。
- 结合理论与实践，提供可直接落地的代码示例和架构设计模式。
- 全面覆盖ML生命周期中的痛点，如显存优化、通信瓶颈及故障排查。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18451 | 🍴 1178 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17332 | 🍴 2119 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11588 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10672 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目代码的精选资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目通过提供完整的代码实现，旨在帮助开发者快速上手并深入理解各类人工智能算法的实际应用。

2. **核心功能**
- 提供500多个现成的AI项目代码示例，覆盖主流技术栈。
- 分类清晰，细分为机器学习、深度学习、计算机视觉和NLP四大板块。
- 包含“Awesome”列表属性，经过筛选的高质量项目集合。
- 主要基于Python语言实现，便于数据科学从业者直接使用。

3. **适用场景**
- AI初学者希望通过实际代码案例快速掌握各子领域的基础知识。
- 开发者在构建具体AI应用时，寻找可参考或复用的代码模板。
- 研究人员需要快速验证某种算法（如图像识别或文本处理）的实现逻辑。

4. **技术亮点**
- 规模宏大且分类全面，是一站式学习AI多分支技术的优质索引库。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具。它支持多种主流框架和模型格式，帮助用户直观地查看和分析模型结构。

2. **核心功能**
*   支持广泛格式的模型可视化，包括 CoreML、ONNX、PyTorch、TensorFlow 等。
*   提供清晰的图形化界面，展示网络层连接及数据流向。
*   兼容多种深度学习框架，如 Keras、TensorFlow Lite 及 Safetensors。
*   基于 JavaScript 构建，便于在 Web 端或桌面端快速部署和使用。

3. **适用场景**
*   开发者调试复杂神经网络结构，排查层级连接错误。
*   研究人员展示模型架构，用于论文配图或技术分享。
*   工程团队在不同模型格式（如从 PyTorch 转换到 ONNX）之间验证转换结果的一致性。

4. **技术亮点**
*   高度兼容主流 AI 生态，几乎覆盖所有常用的深度学习框架和导出格式。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目汇集了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。内容涵盖从基础数学库到主流深度学习框架的关键代码片段和概念解析，旨在为科研人员提供高效的知识回顾工具。

2. **核心功能**
*   提供深度学习及机器学习领域的关键知识点速查。
*   包含 Numpy、Scipy、Matplotlib 等基础科学计算库的使用指南。
*   集成 Keras 等主流深度学习框架的代码示例与配置技巧。
*   针对 AI 研究人员优化的精简知识图谱，便于快速检索。

3. **适用场景**
*   深度学习研究者在复现论文或搭建模型时快速查阅 API 用法。
*   机器学习初学者在进行代码实践时作为辅助参考手册。
*   数据科学家在处理数值计算和数据可视化任务时查找最佳实践。
*   技术团队在内部培训中用于统一基础工具和框架的使用标准。

4. **技术亮点**
*   高度浓缩的知识呈现方式，极大降低了查找特定函数或概念的时间成本。
*   覆盖了从底层数据处理到高层模型构建的完整技术栈。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份全面的人工智能学习路线图，涵盖从零基础上手到就业实战的全过程。项目整理了近200个精选实战案例，并免费提供配套教材，覆盖Python、机器学习、深度学习及自然语言处理等核心领域。旨在帮助学习者系统掌握数据科学、计算机视觉及算法等热门技术栈。

2. **核心功能**
*   提供结构化的AI学习路径，从数学基础到高级应用层层递进。
*   收录近200个高质量实战案例与项目代码，支持动手实践。
*   免费开放配套学习教材与资源，降低入门门槛。
*   覆盖主流框架与技术栈，包括PyTorch、TensorFlow、Keras及Scikit-learn等。
*   聚焦就业导向，通过实际项目提升求职竞争力。

3. **适用场景**
*   **零基础转行人员**：希望系统学习人工智能相关知识并进入该行业的初学者。
*   **高校学生与研究人员**：需要参考资料进行机器学习或深度学习课题研究的群体。
*   **求职者**：希望通过实战项目丰富简历，提升面试竞争力的编程爱好者。
*   **技能拓展者**：希望在工作之外补充数据分析、NLP或CV等特定领域技能的开发者。

4. **技术亮点**
*   内容体系完整，贯通数学原理、编程语言（Python）与主流AI框架。
*   实战资源丰富，拥有近200个可运行的案例，强调“学以致用”。
*   紧跟技术前沿，涵盖TensorFlow 2、PyTorch等当前主流的深度学习框架。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13167 | 🍴 2663 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11744 | 🍴 1219 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9145 | 🍴 1236 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8935 | 🍴 3102 | 语言: C++
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
- ⭐ 6268 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**
funNLP 是一个全面且强大的中文自然语言处理（NLP）资源集合与工具库，涵盖了从基础文本预处理到高级语义理解的各类数据、模型及算法。它集成了敏感词检测、实体抽取、情感分析、知识图谱构建以及语音识别等多领域功能，旨在为开发者提供一站式的 NLP 解决方案。该项目不仅包含丰富的开源数据集和预训练模型，还汇总了大量业界前沿的 NLP 竞赛方案与技术文档。

2. **核心功能**
- **文本基础处理**：提供中英文敏感词过滤、繁简体转换、分词、词性标注、命名实体识别（NER）及停用词移除等基础工具。
- **多模态数据处理**：支持中文 OCR 识别、语音识别（ASR）语料生成、音频数据增广及声纹/情感分析相关资源。
- **知识图谱与问答系统**：整合了多种中文知识图谱构建工具、关系抽取方法及基于不同模型的问答系统（QA）示例。
- **数据增强与评估**：包含 EDA 等数据增强技术、文本相似度计算、可读性评价指标及多个标准的 NLP 测评基准。
- **预训练模型与应用**：汇集了 BERT、GPT、ALBERT、RoBERTa 等主流预训练模型的中文版本及其在分类、生成、摘要等任务中的应用代码。

3. **适用场景**
- **智能客服与聊天机器人开发**：利用其中的闲聊语料、对话系统框架（如 Rasa, ConvLab）及意图识别模型快速搭建对话引擎。
- **内容安全审核系统**：使用敏感词库、暴恐词表及谣言检测数据集，构建高效的文本内容过滤与安全审查平台。
- **垂直领域信息抽取与分析**：基于医疗、金融、法律等领域的专用词库、NER 模型及关系抽取工具，提取结构化业务数据。
- **NLP 研究与教育实验**：借助其汇总的数据集、论文解读、课程资料及基线模型（Baseline），进行算法对比验证或教学演示。

4. **技术亮点**
- **资源高度聚合**：被誉为“中文 NLP 的维基百科”，将分散的优质数据集、代码库、论文和工具进行了系统化整理。
- **覆盖全技术栈**：从传统的规则匹配、统计方法到最新的深度学习（Transformer 系列）及大语言模型应用均有涉及。
- **实战导向性强**：提供了大量经过验证的竞赛获奖方案源码和实际工程落地案例，具有极高的参考价值和复用性。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）及视觉语言模型（VLM）微调框架，支持超过100种主流模型。该项目在 ACL 2024 上被收录，旨在简化从指令微调到强化学习对齐的全流程开发体验。

2. **核心功能**
*   **多模型统一支持**：兼容 Llama、Qwen、Gemini 等100多种主流大模型及视觉语言模型的训练。
*   **多样化微调算法**：原生支持 LoRA、QLoRA、P-Tuning 等参数高效微调（PEFT）技术。
*   **全链路训练能力**：覆盖从监督微调（SFT）、奖励模型训练到基于人类反馈的强化学习（RLHF/DPO）的全流程。
*   **量化与优化集成**：内置 BitsandBytes 等库，支持 INT8/FP4 等低精度量化以节省显存并提升推理速度。
*   **模块化架构设计**：提供高度模块化的代码结构，便于研究人员快速实验新算法或适配新模型。

3. **适用场景**
*   **企业私有化部署**：利用 QLoRA 等技术，在有限显存的硬件环境下高效微调开源大模型以适应特定业务领域。
*   **学术研究实验**：研究人员可快速复现 SFT 或 RLHF 算法，验证不同模型架构在特定任务上的性能表现。
*   **多模态应用开发**：开发者可直接对 VLM 进行微调，构建具备图像理解与生成能力的智能助手或分析工具。

4. **技术亮点**
*   实现了极致的显存优化，使得消费级显卡也能流畅运行大规模模型的微调任务。
*   提供了一站式命令行界面（CLI），无需编写复杂代码即可启动训练、评估和导出流程。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73454 | 🍴 8966 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI知识。项目采用Jupyter Notebook格式编写，内容涵盖从基础概念到深度学习的高级应用。

2. **核心功能**
- 提供结构化的12周学习计划，分24个课时循序渐进地讲解AI概念。
- 涵盖机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等广泛主题。
- 使用交互式Jupyter Notebook作为主要教学载体，便于用户边学边练。
- 由微软发起并支持，确保内容的专业性与前沿性。

3. **适用场景**
- 希望系统性地从零开始学习人工智能的初学者。
- 需要补充计算机视觉或NLP专项知识的开发人员。
- 教育者或培训机构用于开展AI相关课程的参考教材。

4. **技术亮点**
- 内容覆盖全面，不仅限于传统机器学习，还深入探讨了卷积神经网络（CNN）和循环神经网络（RNN）等深度架构。
- 开源且社区活跃（高星标数），拥有庞大的学习者基础和丰富的讨论资源。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52659 | 🍴 10671 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
该项目是一个集数据分析、机器学习实战、线性代数基础以及深度学习框架（PyTorch、TensorFlow 2）和自然语言处理库（NLTK）于一体的综合性学习资源库。它旨在通过代码实战帮助学习者掌握从传统算法到现代深度学习的完整技术栈。

2. **核心功能**
*   涵盖 AdaBoost、K-Means、SVM 等经典机器学习算法的原理与实现。
*   提供 DNN、RNN、LSTM 等深度神经网络模型的搭建与训练示例。
*   集成推荐系统算法（如基于协同过滤）及关联规则挖掘（Apriori, FP-Growth）。
*   包含自然语言处理（NLP）实战，利用 NLTK 进行文本分析。
*   结合 PyTorch 和 TensorFlow 2 框架演示现代深度学习应用。

3. **适用场景**
*   机器学习初学者进行算法原理验证与代码复现。
*   数据科学家用于快速查找特定算法（如聚类、分类）的实现模板。
*   深度学习工程师参考 PyTorch/TF2 在 NLP 或推荐系统中的最佳实践。
*   高校学生用于辅助完成机器学习或数据挖掘相关的课程项目。

4. **技术亮点**
*   内容体系全面，从数学基础（线性代数）到前沿框架（PyTorch/TF2）全覆盖。
*   兼顾传统统计学习与现代深度学习，适合构建完整的知识图谱。
*   高人气项目（4万+星标），社区认可度高，代码参考性强。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42404 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
该项目旨在通过从零开始构建的方式，深入教授人工智能工程的核心概念。它不仅涵盖理论学习，更强调动手实践与最终产品的部署交付。适合希望彻底掌握AI底层原理并具备落地能力的开发者。

2. **核心功能**
*   提供从基础理论到实际应用的完整深度学习与生成式AI教程体系。
*   涵盖大语言模型（LLM）、计算机视觉及强化学习等前沿领域的代码实现。
*   指导用户构建AI代理（Agents）和智能体集群（Swarm Intelligence）系统。
*   支持多种编程语言（如Python、Rust、TypeScript）的工程化实践。

3. **适用场景**
*   AI工程师希望深入理解模型底层逻辑，避免仅依赖黑盒API的开发者。
*   需要构建定制化AI应用（如智能客服、自动化工作流）的技术团队。
*   进行高级AI研究或教学，需要展示从零搭建复杂系统的案例。

4. **技术亮点**
*   融合传统机器学习与现代生成式AI，结合Rust等高性能语言优化底层效率。
*   强调“学-建-发”闭环，不仅教授算法，更关注工程化部署与产品化能力。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42120 | 🍴 7018 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33764 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28772 | 🍴 3512 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25984 | 🍴 2944 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21744 | 🍴 3305 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI项目的综合代码库，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域。它提供了丰富的实战案例代码，旨在帮助开发者快速入门并掌握相关技术。这是一个被广泛认可的“Awesome”系列资源集合。

2. **核心功能**
- 提供500多个完整的AI项目代码示例，覆盖主流AI子领域。
- 整合了机器学习、深度学习、CV及NLP等多类技术的实践案例。
- 作为 curated list（精选列表），汇集了高质量的开源项目资源。
- 支持Python等常用编程语言实现，便于直接运行和学习。

3. **适用场景**
- AI初学者希望通过大量实例代码快速理解各算法的实际应用。
- 开发者在进行技术选型或寻找灵感时，参考具体的项目实现方案。
- 教育机构或培训人员将其作为教学素材，辅助讲解机器学习和深度学习概念。

4. **技术亮点**
- 项目数量庞大且分类清晰，全面覆盖当前热门的AI技术栈。
- 属于社区维护的“Awesome”系列，具有较高的可信度和参考价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35625 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的复杂工作流。它利用大语言模型（LLM）和计算机视觉技术，模拟人类操作浏览器，从而无需编写传统代码即可完成网页交互任务。该项目旨在为 RPA（机器人流程自动化）提供智能化、可视化的解决方案。

2. **核心功能**
*   **AI 驱动的浏览器自动化**：结合 LLM 和视觉理解能力，智能解析网页结构并执行操作。
*   **无代码工作流编排**：用户可通过自然语言描述任务，系统自动生成并执行相应的浏览器操作步骤。
*   **多技术栈支持**：底层兼容 Playwright、Puppeteer 和 Selenium 等主流浏览器自动化工具。
*   **API 集成接口**：提供标准化的 API，便于将自动化能力嵌入到现有的业务系统或 CI/CD 流程中。
*   **智能异常处理**：具备自我修正和重试机制，能在页面元素变化或加载失败时自动调整策略。

3. **适用场景**
*   **跨平台数据抓取与录入**：自动化从不同网站提取数据并填写至内部系统，替代繁琐的手动复制粘贴。
*   **企业级 RPA 流程升级**：为传统硬编码的 RPA 流程增加 AI 灵活性，适应频繁变更的 Web 界面布局。
*   **在线业务自动化测试**：模拟真实用户行为对 Web 应用进行端到端的功能测试和回归测试。
*   **个人日常事务自动化**：自动化处理如比价、预约、订单跟踪等重复性的个人网页操作。

4. **技术亮点**
*   **视觉与大模型融合**：不仅依赖 DOM 结构，还通过截图分析理解页面内容，解决了动态渲染页面的自动化难题。
*   **高度模块化架构**：支持灵活替换底层的浏览器驱动（如从 Selenium 切换至 Playwright），适应不同性能需求。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22554 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 描述: Computer Vision Annotation Tool (CVAT) is a leading platform for building high-quality visual datasets for vision AI. It offers open-source, cloud, and enterprise products, as well as labeling services, for image, video, and 3D annotation with AI-assisted labeling, quality assurance, team collaboration, analytics, and developer APIs.
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16360 | 🍴 3770 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它提供了可微分的图像处理算子和几何变换工具，旨在简化深度学习中的视觉任务开发。该项目结合了传统计算机视觉的严谨性与现代深度学习的灵活性。

2. **核心功能**
- 提供大量可微分的图像处理和几何变换操作，支持自动求导。
- 集成多种经典计算机视觉算法（如相机标定、姿态估计），使其兼容神经网络训练流程。
- 拥有高效的张量操作接口，充分利用 GPU 加速计算性能。
- 支持不同分辨率和批量大小的灵活输入处理，便于模块化集成。

3. **适用场景**
- 在语义分割或目标检测等深度学习中，需要端到端地包含几何预处理步骤时。
- 开发机器人视觉系统，用于实时的空间感知和运动规划。
- 研究神经辐射场（NeRF）或多视图立体几何（MVS）等对几何约束敏感的前沿课题。
- 需要将传统 CV 管线（如去畸变、仿射变换）无缝嵌入 PyTorch 模型进行微调的场景。

4. **技术亮点**
- **可微分几何**：将传统非可微的 CV 操作转化为可微模块，允许梯度反向传播，这是其区别于 OpenCV 等传统库的最大优势。
- **PyTorch 原生集成**：作为 PyTorch 生态的一部分，无需复杂的数据格式转换，直接操作 Tensor。
- **硬件加速优化**：底层实现针对 GPU 进行了高度优化，显著提升了大规模批处理下的计算效率。
- 链接: https://github.com/kornia/kornia
- ⭐ 11282 | 🍴 1205 | 语言: Python
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
- ⭐ 3294 | 🍴 403 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2628 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2429 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **1. 中文简介**
OpenClaw 是一款个人 AI 助手，支持任意操作系统和平台，以独特的“龙虾方式”运行。它强调数据所有权，让用户能够完全掌控自己的 AI 体验。该项目旨在提供一个跨平台的、私密的智能辅助解决方案。

**2. 核心功能**
*   全平台兼容，可在任何操作系统和硬件上部署运行。
*   赋予用户完全的数据主权，确保隐私和数据安全。
*   提供个性化的 AI 助手服务，适应用户特定需求。
*   基于 TypeScript 构建，保证代码的可维护性和扩展性。

**3. 适用场景**
*   需要在不同设备间无缝同步的个人智能助理。
*   对数据隐私有极高要求的个人或企业用户。
*   希望拥有自定义 AI 行为逻辑的技术爱好者。

**4. 技术亮点**
*   采用 TypeScript 开发，具备强类型检查和良好的工程化支持。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383833 | 🍴 80641 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架及软件开发方法论，旨在通过系统化方式提升开发效率。它强调构建可复用的智能体技能，并以此指导软件开发生命周期（SDLC）的实践。该项目致力于解决复杂 AI 代理协作中的实际问题，提供一套切实可行的工作流。

2. **核心功能**
- 提供基于代理的技能框架，支持模块化构建和复用 AI 能力。
- 实施“子代理驱动开发”（Subagent-driven Development）方法论，优化任务分解与执行。
- 集成头脑风暴（Brainstorming）功能，辅助创意生成与问题探索。
- 覆盖完整软件开发生命周期（SDLC），从规划到编码实现全流程支持。
- 支持 Shell 脚本环境下的自动化操作与技能编排。

3. **适用场景**
- 需要构建复杂多代理协作系统的研发团队。
- 希望将 AI 技能标准化并复用于不同项目的企业级开发。
- 利用 AI 辅助进行软件架构设计与头脑风暴的技术团队。
- 追求高效、结构化 AI 辅助编码流程的开发者。

4. **技术亮点**
- 创新性地将“技能”作为一等公民纳入软件开发方法论中。
- 强调实际落地效果，提供经过验证的代理协作模式而非理论概念。
- 支持通过 Shell 脚本灵活集成现有工具链与自动化流程。
- 链接: https://github.com/obra/superpowers
- ⭐ 259368 | 🍴 23117 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**
Hermes Agent 是一款能够伴随用户共同成长的人工智能代理工具。它旨在通过持续的学习与交互，深度适应用户的工作习惯和需求，提供智能化的辅助支持。

2. **核心功能**
*   具备自我进化能力，能根据用户反馈和上下文动态优化其行为模式。
*   集成多种主流大语言模型（如 Anthropic Claude、OpenAI ChatGPT 等），提供灵活的推理后端支持。
*   支持自动化代码生成、调试及复杂任务处理，显著提升开发效率。
*   拥有高度可定制的架构，允许用户根据特定场景调整代理的行为逻辑。

3. **适用场景**
*   开发者日常编程工作，如自动补全代码、审查 Pull Request 或修复 Bug。
*   复杂的数据分析与报告生成，通过自然语言指令快速提取洞察。
*   个人知识管理与信息整理，作为智能助手协助归档资料或总结文档。

4. **技术亮点**
*   采用模块化设计，轻松切换不同的 LLM 提供商以平衡成本与性能。
*   强调“成长型”架构，通过长期记忆机制实现与用户的个性化协同。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218909 | 🍴 41457 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持将可视化构建与自定义代码相结合。它提供超过 400 种集成，允许用户选择自托管或云端部署，以实现高效的数据流与任务自动化。

2. **核心功能**
*   **可视化工作流构建**：通过直观的界面拖拽组件即可设计复杂的自动化流程。
*   **原生 AI 集成**：内置人工智能能力，可直接在工作流中调用 LLM 等 AI 模型进行处理。
*   **丰富的生态系统**：拥有 400 多种预置集成，轻松连接各类 SaaS 服务和 API。
*   **混合开发模式**：支持低代码快速搭建，同时也允许编写自定义代码以满足高级需求。
*   **灵活部署方式**：既支持自托管以保障数据隐私，也提供便捷的云服务选项。

3. **适用场景**
*   **企业级数据同步**：自动在不同数据库、CRM 或营销工具之间同步和转换数据。
*   **AI 驱动的内容处理**：利用 AI 自动生成摘要、翻译文本或分析客户反馈并归档。
*   **DevOps 自动化运维**：自动化部署流程、监控服务器状态或在 CI/CD 管道中触发通知。
*   **跨平台消息路由**：将来自邮件、Slack 或社交媒体渠道的消息统一收集并分发给相应团队。

4. **技术亮点**
*   **基于 TypeScript 开发**：提供了良好的类型安全和现代化的开发体验。
*   **MCP 协议支持**：原生支持 Model Context Protocol (MCP)，增强了与 AI 模型的交互能力和标准化集成。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197490 | 🍴 59542 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- ### 1. 中文简介
AutoGPT 致力于实现人人可及的 AI 愿景，让用户能够轻松使用并在此基础上进行构建。其使命是提供必要的工具，帮助用户将精力集中在真正重要的事务上。

### 2. 核心功能
*   **自主代理执行**：具备自我驱动能力，能独立规划、思考并执行复杂的多步骤任务。
*   **大语言模型集成**：深度整合 OpenAI、Claude、LLaMA 等多种主流 LLM API，灵活适配不同需求。
*   **互联网与文件系统交互**：拥有联网搜索和读写本地文件的能力，使其能获取实时信息并处理本地数据。
*   **记忆机制**：通过向量数据库等技术保留上下文记忆，确保在长周期任务中保持连贯性。

### 3. 适用场景
*   **自动化工作流**：用于执行需要多步操作的任务，如自动调研、数据收集与整理。
*   **内容创作辅助**：辅助完成长篇写作、多平台内容分发或社交媒体管理。
*   **代码开发与调试**：作为编程助手，辅助生成代码片段、查找 Bug 或执行简单的开发任务。

### 4. 技术亮点
*   **高度模块化与可扩展性**：基于 Python 构建，支持插件式架构，用户可轻松添加新功能或替换底层模型。
*   **前沿 Agentic AI 实践**：代表了当前自主智能体（Autonomous Agents）技术的最新探索方向，展示了 LLM 在复杂逻辑推理中的应用潜力。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185650 | 🍴 46073 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166215 | 🍴 21484 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164229 | 🍴 30434 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157225 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154474 | 🍴 8800 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152223 | 🍴 9625 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

