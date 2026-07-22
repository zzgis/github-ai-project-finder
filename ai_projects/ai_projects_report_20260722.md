# GitHub AI项目每日发现报告
日期: 2026-07-22

## 新发布的AI项目

### thinking-orbs
- 1. **中文简介**
这是一个专为 AI 和智能体用户界面设计的点状思维光环加载指示器。它提供了六种经过精细调优的状态和两种尺寸，并支持自动适配深色与浅色模式。

2. **核心功能**
- 提供六种不同的动态状态以模拟复杂的“思考”过程。
- 支持两种可选尺寸，便于在不同布局中灵活应用。
- 具备自动检测系统主题的功能，无缝切换深色和浅色模式。
- 基于 TypeScript 开发，确保类型安全和现代前端集成体验。

3. **适用场景**
- 大型语言模型（LLM）聊天应用中显示生成响应前的等待状态。
- 多步骤 AI 代理工作流中展示各阶段的处理进度。
- 需要体现智能感知的复杂后台任务加载提示。

4. **技术亮点**
- 采用“思维光环”的视觉隐喻，比传统旋转图标更具拟人化和科技感。
- 内置主题自动适配逻辑，减少了开发者手动维护样式的工作量。
- 链接: https://github.com/Jakubantalik/thinking-orbs
- ⭐ 492 | 🍴 32 | 语言: TypeScript

### BossConsole
- 描述: Open-source, multi-platform harness for AI agents — a native, multi-threaded operator's console (JVM, not Electron) to run Claude Code, Codex, Gemini or OpenCode with a real browser, terminal, editor, secrets & 100+ MCP tools. Built for enterprises, science & research.
- 链接: https://github.com/risa-labs-inc/BossConsole
- ⭐ 149 | 🍴 2 | 语言: Kotlin
- 标签: agent-harness, ai-agents, browser, claude-code, codex

### open-ai-canvas
- ### 1. **中文简介**
Open-ai-canvas 是一个面向 AI 影视创作的开源无限画布工作台，旨在通过集成多模态生成、分镜编排、素材管理与 Agent 工作流，提升创作效率。该项目基于 TypeScript 开发，提供了一个灵活且可扩展的创作环境，支持从概念构思到成品输出的全流程协作。

### 2. **核心功能**
- **多模态内容生成**：集成多种 AI 模型，支持文本、图像、视频等多种媒体形式的自动或辅助生成。
- **智能分镜编排**：提供可视化的无限画布界面，方便用户进行剧本拆解、镜头规划和叙事逻辑梳理。
- **统一素材管理**：集中存储和管理所有创作相关的资产（如图片、音频、脚本片段），确保资源有序调用。
- **Agent 自动化工作流**：利用 AI Agent 实现复杂任务的自动化处理，简化重复性操作并提升制作流程的连贯性。

### 3. **适用场景**
- **独立短片与广告制作**：帮助小型团队或个人创作者快速完成从创意到视觉呈现的全过程。
- **影视前期策划与预可视化**：用于导演和制片人在正式拍摄前进行故事板设计和场景预览。
- **AI 创意实验平台**：供研究人员或开发者测试新的多模态 AI 模型在影视制作中的实际应用效果。

### 4. **技术亮点**
- **TypeScript 驱动**：采用 TypeScript 构建，保证了代码的类型安全和良好的可维护性，便于社区贡献和二次开发。
- **模块化架构设计**：将生成、编排、管理和工作流解耦，允许用户根据需求灵活组合功能模块。
- 链接: https://github.com/ddcat-ai/open-ai-canvas
- ⭐ 64 | 🍴 17 | 语言: TypeScript

### pgContext
- 描述: A full AI search engine, built into Postgres.
- 链接: https://github.com/Evokoa/pgContext
- ⭐ 59 | 🍴 3 | 语言: Rust

### AIGuardSIEM
- ### AIGuardSIEM 项目分析

**1. 中文简介**
AIGuardSIEM 是一款面向生产环境的高性能 SIEM/XDR 平台，支持每秒百万级事件（EPS）的摄入，并实现低于 15 毫秒的检测延迟。该项目基于 C++、Go 和 Python 构建，集成了 DPDK 捕获、ONNX 机器学习推理及 eBPF 监控等先进技术。

**2. 核心功能**
*   **高性能数据处理**：利用 DPDK 技术实现高速网络包捕获，支撑海量日志的高效摄入。
*   **智能威胁检测**：结合 Sigma 规则引擎与 ONNX 机器学习模型进行异常检测和恶意软件识别。
*   **深度端点监控**：通过 eBPF 技术实现对系统底层行为的无侵入式实时监控。
*   **自动化响应编排**：内置 SOAR 能力，支持安全事件的自动化调查与响应流程。
*   **云原生架构支持**：适配 Kubernetes 环境，具备良好的可扩展性和部署灵活性。

**3. 适用场景**
*   **企业级安全运营中心（SOC）**：适用于需要集中管理大规模终端和网络流量的高级安全团队。
*   **实时入侵检测系统**：适合对检测延迟要求极高（亚毫秒级）的关键基础设施保护场景。
*   **混合云安全监控**：适用于运行在 Kubernetes 上的微服务架构环境的安全态势感知。
*   **高级威胁狩猎**：利用机器学习模型发现传统规则难以捕捉的隐蔽攻击行为。

**4. 技术亮点**
*   **极低延迟**：在保证高吞吐量的同时，将检测延迟控制在 15 毫秒以内。
*   **多语言混合架构**：结合 C++ 的性能优势与 Go/Python 的开发效率，平衡了底层控制与上层业务逻辑。
*   **前沿技术集成**：融合了 eBPF 内核观测与 ONNX 标准化模型推理，提升了检测的精准度和适应性。
- 链接: https://github.com/itshamzabendelladj/AIGuardSIEM
- ⭐ 52 | 🍴 4 | 语言: C++
- 标签: anomaly-detection, cybersecurity, dpdk, endpoint-security, incident-response

### editaplot
- 描述: AI-guided editable scientific figures with Codex and local Origin/OriginPro
- 链接: https://github.com/hang-jin/editaplot
- ⭐ 39 | 🍴 2 | 语言: Python
- 标签: codex-skill, editable-figures, research, scientific-visualization, windows

### pm-manager
- 描述: Know what to fix next — local .pm governance skill pack for AI coding agents (Spec Kit–inspired).
- 链接: https://github.com/wei63w/pm-manager
- ⭐ 36 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agents, claude-code, cursor, project-management

### Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- 描述: The Industry‑Oriented AI Engineering Program blends theory with hands‑on projects. Students gain expertise in open‑source LLMs, prompt engineering, fine‑tuning, and agent development, preparing for impactful careers in healthcare AI, autonomous systems, and innovation.
- 链接: https://github.com/AnantVerma-2022/Industry-Oriented-AI-Engineering-Program-for-CAW-GL-Bajaj
- ⭐ 32 | 🍴 0 | 语言: Jupyter Notebook

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
这是一个汇集了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目为开发者提供了完整的代码实现，是系统学习人工智能技术的优质参考指南。

2. **核心功能**
*   提供大量经过验证的机器学习与深度学习项目代码示例。
*   覆盖计算机视觉和自然语言处理等主流AI细分领域。
*   作为结构化的学习路径，帮助开发者快速掌握AI实战技能。
*   包含Python语言实现的完整解决方案，便于直接运行和修改。

3. **适用场景**
*   AI初学者通过实战项目快速建立对机器学习流程的理解。
*   数据科学家寻找特定任务（如图像分类或文本分析）的代码模板。
*   开发人员构建AI应用时，参考现有架构进行二次开发。
*   教育工作者用于设计人工智能课程的教学案例库。

4. **技术亮点**
*   项目数量庞大且分类清晰，覆盖了从基础到高级的多种算法模型。
*   全部基于Python语言，符合当前AI开发的主流技术栈标准。
*   被标记为“AweSome”列表，意味着其内容质量经过社区筛选和高认可度。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35620 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习及机器学习模型的可视化工具。它能够直观地展示模型的结构与数据流，帮助用户更好地理解和分析复杂的算法架构。

2. **核心功能**
- 支持多种主流框架（如 TensorFlow, PyTorch, Keras）及格式（如 ONNX, CoreML, Safetensors）的模型可视化。
- 提供交互式的图形界面，允许用户逐层检查模型细节和参数。
- 兼容桌面端和 Web 端运行，方便在不同环境下查看模型结构。
- 能够清晰呈现张量形状和数据流向，辅助调试和优化模型设计。

3. **适用场景**
- 研究人员或开发者在构建新模型时，用于验证网络结构是否符合预期。
- 团队内部交流时，作为文档补充，直观展示模型架构以便讨论。
- 模型部署前，检查从训练框架转换到推理引擎（如 ONNX 转 TensorRT）后的结构一致性。
- 学习深度学习原理时，通过可视化理解复杂层之间的连接关系。

4. **技术亮点**
- 广泛的格式兼容性，几乎涵盖了当前主流的 AI 模型存储格式。
- 轻量级且开源，无需复杂配置即可快速启动使用。
- 社区活跃，星标数高（33k+），表明其在 AI 工具链中具有极高的普及度和认可度。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是用于机器学习模型互操作性的开放标准。它旨在打破不同深度学习框架之间的壁垒，实现模型在多种环境和平台间的无缝转换与部署。

2. **核心功能**
- 提供统一的模型表示格式，支持跨框架的模型交换。
- 允许将训练好的模型从一种框架导出并在另一种框架中运行。
- 优化推理性能，支持在CPU、GPU等多种硬件加速器上高效执行。
- 包含完整的工具链，涵盖模型转换、验证及可视化等功能。
- 由微软、Facebook等科技巨头联合维护，拥有广泛的社区支持。

3. **适用场景**
- 需要将PyTorch或TensorFlow训练的模型部署到移动端或嵌入式设备时。
- 在混合使用多种深度学习框架的工程环境中进行模型迁移。
- 利用ONNX Runtime加速生产环境下的模型推理服务。
- 希望避免被单一供应商或框架锁定，追求技术栈灵活性时。

4. **技术亮点**
- 作为行业事实标准，被主流框架（如PyTorch, TensorFlow, Keras）原生支持。
- 通过ONNX Runtime实现高性能、低延迟的跨平台推理引擎。
- 链接: https://github.com/onnx/onnx
- ⭐ 21194 | 🍴 3973 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开放书》是一部全面涵盖机器学习工程实践的技术指南。它深入探讨了从大规模模型训练到推理优化的全流程最佳实践，旨在帮助开发者构建高效、可扩展的AI系统。

2. **核心功能**
*   提供针对大型语言模型（LLM）和Transformer架构的训练与微调详细教程。
*   深入解析GPU硬件特性、网络通信及存储优化以加速模型训练。
*   分享高可用性推理服务部署策略及模型性能调试技巧。
*   介绍使用Slurm等集群管理系统进行大规模分布式作业调度的方法。

3. **适用场景**
*   需要从零开始搭建和优化大规模深度学习训练基础设施的工程团队。
*   致力于降低大模型推理成本并提升响应速度的生产环境运维人员。
*   希望掌握PyTorch分布式训练技巧及故障排查能力的算法工程师。

4. **技术亮点**
该项目由业界专家编写，内容紧跟前沿技术，特别侧重于解决实际工程中的可扩展性、调试及硬件协同优化等痛点问题。
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
- ⭐ 11586 | 🍴 909 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10672 | 🍴 5707 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI项目的资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目为开发者提供了完整的代码实现，是系统学习人工智能技术的优质参考指南。

2. **核心功能**
*   提供大量经过验证的机器学习与深度学习项目代码示例。
*   覆盖计算机视觉和自然语言处理等主流AI细分领域。
*   作为结构化的学习路径，帮助开发者快速掌握AI实战技能。
*   包含Python语言实现的完整解决方案，便于直接运行和修改。

3. **适用场景**
*   AI初学者通过实战项目快速建立对机器学习流程的理解。
*   数据科学家寻找特定任务（如图像分类或文本分析）的代码模板。
*   开发人员构建AI应用时，参考现有架构进行二次开发。
*   教育工作者用于设计人工智能课程的教学案例库。

4. **技术亮点**
*   项目数量庞大且分类清晰，覆盖了从基础到高级的多种算法模型。
*   全部基于Python语言，符合当前AI开发的主流技术栈标准。
*   被标记为“AweSome”列表，意味着其内容质量经过社区筛选和高认可度。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35620 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于神经网络、深度学习及机器学习模型的可视化工具。它能够直观地展示模型的结构与数据流，帮助用户更好地理解和分析复杂的算法架构。

2. **核心功能**
- 支持多种主流框架（如 TensorFlow, PyTorch, Keras）及格式（如 ONNX, CoreML, Safetensors）的模型可视化。
- 提供交互式的图形界面，允许用户逐层检查模型细节和参数。
- 兼容桌面端和 Web 端运行，方便在不同环境下查看模型结构。
- 能够清晰呈现张量形状和数据流向，辅助调试和优化模型设计。

3. **适用场景**
- 研究人员或开发者在构建新模型时，用于验证网络结构是否符合预期。
- 团队内部交流时，作为文档补充，直观展示模型架构以便讨论。
- 模型部署前，检查从训练框架转换到推理引擎（如 ONNX 转 TensorRT）后的结构一致性。
- 学习深度学习原理时，通过可视化理解复杂层之间的连接关系。

4. **技术亮点**
- 广泛的格式兼容性，几乎涵盖了当前主流的 AI 模型存储格式。
- 轻量级且开源，无需复杂配置即可快速启动使用。
- 社区活跃，星标数高（33k+），表明其在 AI 工具链中具有极高的普及度和认可度。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33252 | 🍴 3164 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- **1. 中文简介**
该项目为深度学习与机器学习研究人员提供了必备的核心速查表（Cheat Sheets）。内容涵盖人工智能、深度学习框架及常用科学计算库的关键语法与技巧，旨在帮助研究者快速回顾和查阅技术细节。

**2. 核心功能**
- 提供针对主流深度学习框架（如Keras）的快速参考指南。
- 包含数值计算与数据处理库（如NumPy、SciPy）的常用函数速查。
- 集成数据可视化工具（如Matplotlib）的标准用法示例。
- 梳理机器学习基础概念与算法的关键参数说明。
- 以简洁清晰的格式呈现，便于打印或离线查阅。

**3. 适用场景**
- 研究人员在编码过程中快速查找缺失的API参数或语法细节。
- 学生在复习机器学习课程时，作为浓缩的知识摘要工具。
- 工程师在进行模型调试时，快速核对数据处理或可视化代码规范。
- 团队内部知识共享，确保成员对常用库的使用保持一致性。

**4. 技术亮点**
- 高度聚焦于实践中的高频需求，去除了冗长的理论解释，直击代码要点。
- 覆盖从底层数值计算到高层深度学习框架的全栈技术链。
- 经过社区广泛验证（高星标数），内容权威且更新及时，是高效的实战辅助资源。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15420 | 🍴 3383 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn 是一份详尽的人工智能学习路线图，收录了近200个实战案例与项目，并提供免费配套教材以助力零基础用户入门及就业。内容涵盖Python、数学基础、机器学习、深度学习、计算机视觉及自然语言处理等热门领域，支持TensorFlow、PyTorch等多种主流框架。

2. **核心功能**
- 提供结构化的AI学习路径，从基础数学到高级应用层层递进。
- 整理近200个实战案例和项目，强调动手实践与就业技能培养。
- 免费提供配套学习资料和教材，降低零基础上手门槛。
- 覆盖主流AI框架（如PyTorch, TensorFlow, Keras）及工具库（NumPy, Pandas等）。
- 包含计算机视觉（CV）、自然语言处理（NLP）和数据科学等多方向细分领域。

3. **适用场景**
- 希望系统学习人工智能并制定清晰学习路线的初学者。
- 需要通过大量实战项目提升动手能力以寻求AI相关工作的求职者。
- 需要参考具体案例和代码实现来加速研究或开发的算法工程师。
- 希望补充Python数据处理、机器学习或深度学习基础知识的学生。

4. **技术亮点**
该项目最大的亮点在于其“路线图+实战案例+免费教材”三位一体的完整学习生态，特别适合希望从零基础快速过渡到就业水平的学习者。
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
- ⭐ 6269 | 🍴 750 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能全面的自然语言处理（NLP）资源集合库，涵盖了从基础工具（如敏感词检测、分词、情感分析）到高级任务（如知识图谱构建、预训练模型应用、语音识别）的广泛领域。该项目整合了大量中文及多语言的语料库、数据集、开源工具和学术资源，旨在为开发者提供一站式的 NLP 开发支持。

**2. 核心功能**
*   **基础文本处理与清洗**：提供中英文敏感词过滤、繁简体转换、停用词、反动词表以及文本纠错等基础预处理工具。
*   **实体抽取与信息提取**：包含手机号、身份证、邮箱等正则抽取，基于 BERT/ALBERT 等模型的命名实体识别（NER），以及关系抽取和事件三元组抽取工具。
*   **语义分析与知识库**：集成词汇情感值计算、同义词/反义词库、中文词向量、各类垂直领域词库（如汽车、医疗、法律）及知识图谱相关资源。
*   **预训练模型与前沿算法**：汇集 BERT、GPT-2、ERNIE、XLM 等主流预训练模型资源，以及文本生成、摘要、问答系统和对话机器人的最新代码实现。
*   **多模态与特定场景数据**：涵盖中文 OCR、语音识别（ASR）语料、手写汉字识别、笑话/聊天语料库以及各类垂直领域数据集（如医疗、金融）。

**3. 适用场景**
*   **NLP 快速原型开发**：开发者可直接调用项目中提供的分词、实体抽取和情感分析模块，快速搭建文本处理流水线。
*   **学术研究与伦理风控**：研究人员可利用其丰富的数据集（如 CLUE 基准、医学 NLP 数据）进行模型训练，企业用户可用于内容安全审核（敏感词/暴恐词过滤）。
*   **垂直领域知识库构建**：利用其提供的专业词库（医疗、法律、汽车等）和知识图谱构建工具，快速建立行业特定的语义理解系统。
*   **智能客服与对话系统搭建**：参考项目中的对话机器人架构、闲聊语料及预训练模型，构建具备多轮对话能力的智能助手。

**4. 技术亮点**
*   **资源极度丰富且全面**：不仅包含代码工具，还囊括了海量数据集、论文解读、预训练模型权重及行业报告，是 NLP 领域的“百科全书”。
*   **紧跟技术前沿**：持续更新包括 BERT、GPT-2、ALBERT、RoBERTa 等最新深度学习模型在中文 NLP 中的应用案例和微调代码。
*   **本土化优化深入**：针对中文特性提供了大量专用资源，如中文分词加速版（jieba_fast）、中文标点修复、中文数字转换、以及基于中文百科的知识图谱构建方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81964 | 🍴 15250 | 语言: Python

### LlamaFactory
- 描述: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73453 | 🍴 8966 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**
这是一个为期12周、包含24课时的AI入门课程，旨在让所有人都能轻松学习人工智能。项目通过Jupyter Notebook的形式提供教学材料，涵盖了从基础概念到深度学习的完整知识体系。

2. **核心功能**
- 提供结构化的12周学习计划，将复杂的AI概念分解为24个易于理解的课时。
- 基于Jupyter Notebook进行交互式教学，支持代码即时运行与结果可视化。
- 覆盖机器学习、深度学习、计算机视觉（CNN）、自然语言处理（NLP）及生成对抗网络（GAN）等核心领域。
- 由Microsoft for Beginners团队开发，适合零基础用户循序渐进地掌握AI技能。

3. **适用场景**
- 初学者希望通过系统化课程快速建立人工智能知识框架的学习者。
- 教育机构或企业培训部门用于开展AI基础技能培训的教学资源。
- 开发者希望深入了解卷积神经网络（CNN）和循环神经网络（RNN）原理与实践的研究人员。
- 对数据科学感兴趣，想要通过实战代码练习来巩固理论知识的自学者。

4. **技术亮点**
- 采用“边学边练”的模式，通过可执行的Notebook代码帮助用户直观理解算法逻辑。
- 内容全面且前沿，不仅涵盖传统机器学习，还深入讲解深度学习及其在CV和NLP中的应用。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52644 | 🍴 10668 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合资源库，内容深入线性代数、PyTorch 及 TensorFlow 2 等核心领域。该项目集成了 NLTK 自然语言处理工具，旨在为学习者提供从理论到代码实现的完整技术路径。

2. **核心功能**
- 提供基于 Scikit-learn 的经典机器学习算法（如 SVM、K-Means、回归）的实战代码。
- 包含深度学习框架 PyTorch 和 TensorFlow 2 的高级模型实现与应用。
- 集成 NLTK 库进行自然语言处理（NLP）任务及文本分析。
- 涵盖推荐系统算法（如 Apriori、FP-Growth）及协同过滤策略。
- 结合线性代数基础讲解 PCA、SVD 等降维与矩阵运算原理。

3. **适用场景**
- 机器学习初学者希望系统性地从数学基础过渡到工程实战。
- 数据科学家需要快速查阅经典算法（如 Adaboost、朴素贝叶斯）的代码实现。
- 研究人员探索 NLP 或推荐系统领域的具体算法落地案例。
- 学生用于辅助学习线性代数在计算机视觉及数据处理中的应用。

4. **技术亮点**
- 技术栈全面，无缝衔接传统机器学习（Scikit-learn）与现代深度学习（PyTorch/TF2）。
- 理论与实践并重，将复杂的数学概念（如线性代数）与具体编程实现紧密结合。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42404 | 🍴 11531 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 1. **中文简介**
本项目旨在通过从零开始构建，深入理解人工智能的核心原理与工程实践。它引导学习者掌握从基础理论到最终部署的全流程，实现“学习、构建、交付”的闭环。适合希望彻底搞懂 AI 底层逻辑并具备实际落地能力的开发者。

2. **核心功能**
*   提供基于 Python、Rust 和 TypeScript 的多语言实战教程，涵盖 LLM、计算机视觉及强化学习等前沿领域。
*   深入讲解 AI Agent、MCP 协议及群体智能等高级架构设计与实现细节。
*   包含从深度学习基础到生成式 AI 应用的完整课程体系，强调动手代码实现而非仅止于理论。
*   指导如何将复杂的 AI 模型工程化，使其能够稳定运行并服务于真实用户场景。

3. **适用场景**
*   AI 工程师希望突破框架使用层面的限制，深入理解模型底层机制以提升系统性能。
*   学生或研究人员需要通过全栈式项目（含后端、前端及模型服务）来巩固机器学习知识。
*   团队需要参考最佳实践，构建基于大语言模型或智能体（Agent）的企业级应用原型。
*   开发者想要探索 Rust 或 TypeScript 在高性能 AI 基础设施开发中的应用潜力。

4. **技术亮点**
*   跨语言技术栈整合：同时涉及 Python（主流 AI 生态）、Rust（高性能底层）和 TypeScript（前端/Web 集成），展现了现代 AI 工程的复杂性。
*   紧跟前沿趋势：标签中包含 MCP（Model Context Protocol）和 Swarm Intelligence，表明内容覆盖了最新的 AI 交互标准与多智能体协作方向。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 42052 | 🍴 7005 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35620 | 🍴 7370 | 语言: 未知
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
- ⭐ 21742 | 🍴 3305 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域的AI项目资源库，并附带完整代码实现。该项目旨在为开发者提供一个全面的学习和实践平台，帮助快速掌握各类人工智能核心技术与应用。

2. **核心功能**
- 提供涵盖机器学习、深度学习、NLP和计算机视觉的500+个分类项目集合。
- 每个项目均附带可运行的源代码，支持直接复现和实验验证。
- 标签化管理，便于用户根据具体技术领域（如CV或NLP）快速检索相关案例。
- 作为Awesome List性质的资源索引，整合了高质量开源项目供学习参考。

3. **适用场景**
- AI初学者系统学习：通过阅读和运行代码，快速理解各子领域的基本概念与实现逻辑。
- 项目灵感获取：寻找特定任务（如图像分类、文本生成）的参考实现以启发个人开发思路。
- 技术选型对比：在不同算法或框架的项目实践中，评估其效果与适用性。

4. **技术亮点**
- **规模庞大且分类清晰**：收录数量多达500个，覆盖AI主流子领域，结构化程度高。
- **实战导向**：强调“with code”，不仅提供理论介绍，更注重代码级的实践落地能力。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35620 | 🍴 7370 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化工具，能够自动化执行基于浏览器的复杂工作流。它利用 AI 智能解析网页界面并模拟人类操作，从而替代繁琐的手动重复任务。该项目旨在为 RPA（机器人流程自动化）提供更强、更灵活的 AI 驱动解决方案。

2. **核心功能**
- 利用大语言模型（LLM）和计算机视觉技术，智能识别网页元素并执行点击、输入等操作。
- 支持通过代码或 API 定义和运行复杂的浏览器自动化工作流，无需编写大量维护性强的选择器脚本。
- 兼容 Playwright 等主流浏览器自动化工具，提供稳定且高效的底层执行引擎。
- 具备自我纠错和重试机制，能够应对网页结构变化或临时加载失败等异常情况。

3. **适用场景**
- 企业级 RPA：自动化处理需要登录多个系统的数据录入、报表生成或跨平台信息同步任务。
- 网页数据抓取：从动态渲染或反爬机制复杂的网站中结构化提取所需数据。
- 在线服务自动化：批量完成如注册账号、填写表单、监控价格变动或预订票务等操作。

4. **技术亮点**
- 融合了 LLM 的语义理解能力与 CV 的视觉感知能力，实现了对非标准 UI 元素的鲁棒性交互。
- 采用无头浏览器架构，支持在服务器端高效并发运行自动化任务，降低对本地环境的依赖。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22553 | 🍴 2113 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是构建高质量视觉数据集的首选平台，支持图像、视频及3D数据的标注。它提供开源、云和企业级产品，具备AI辅助标注、质量保障及团队协作等功能。

2. **核心功能**
*   支持图像、视频和3D数据的多维度标注。
*   集成AI辅助标注以提升效率并提供质量保障。
*   提供团队协作、数据分析及开发者API接口。
*   涵盖开源、云端和企业级多种部署模式。

3. **适用场景**
*   计算机视觉模型训练所需的高质量数据集构建。
*   需要大规模团队协作进行数据标注的深度学习项目。
*   对图像分类、目标检测或语义分割等任务的数据预处理。

4. **技术亮点**
*   支持主流深度学习框架（PyTorch, TensorFlow）的数据格式。
*   内置智能标注算法，显著降低人工标注成本。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16360 | 🍴 3770 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目致力于提供计算机视觉领域的高级AI可解释性解决方案。它广泛支持CNN、Vision Transformers等模型，涵盖分类、目标检测、分割及图像相似度等多种任务。

2. **核心功能**
*   支持多种深度学习架构（如CNN和Vision Transformers）的可解释性分析。
*   兼容分类、目标检测、语义分割及图像相似度计算等多种计算机视觉任务。
*   提供Grad-CAM、Score-CAM等多种可视化方法以增强模型决策的透明度。

3. **适用场景**
*   研究人员调试模型时，通过可视化特征图来理解CNN或Transformer的关注区域。
*   医疗影像分析中，医生需要直观查看算法做出诊断依据的具体病灶位置。
*   自动驾驶系统开发中，验证目标检测模型是否真正识别了关键物体而非背景噪声。

4. **技术亮点**
*   作为PyTorch生态中高分开源项目，提供了成熟且易于集成的可解释性工具链。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12922 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**
Kornia 是一个专为空间智能（Spatial AI）设计的几何计算机视觉库。它基于 PyTorch 构建，提供了高度可微分的图像处理原语，旨在简化传统视觉算法在深度学习模型中的集成与开发过程。

2. **核心功能**
*   提供大量可微分的几何计算机视觉算子，支持端到端的梯度传播。
*   内置丰富的图像增强、特征提取和几何变换工具，兼容 PyTorch 张量操作。
*   专注于空间 AI 任务，如姿态估计、SLAM 和机器人导航中的视觉处理。
*   保持与 PyTorch 生态系统的无缝集成，方便研究人员快速原型化视觉算法。

3. **适用场景**
*   需要集成传统几何约束的深度神经网络开发（如单目深度估计）。
*   机器人视觉系统，特别是涉及相机标定、位姿估计和三维重建的应用。
*   空间智能相关的学术研究，探索计算机视觉与深度学习的前沿结合点。
*   构建端到端的视觉感知流水线，其中包含必须可微分的预处理或后处理步骤。

4. **技术亮点**
*   **全可微分架构**：核心优势在于所有视觉算子均为可微分，允许在反向传播中直接优化几何参数。
*   **PyTorch 原生支持**：无需额外转换接口，直接在 GPU 上高效运行，加速大规模数据处理。
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
- ⭐ 3293 | 🍴 403 | 语言: Python
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
- 1. **中文简介**
OpenClaw 是一款跨操作系统和平台的个人 AI 助手，旨在让用户以“龙虾”般自由的方式完全掌控自己的数据。它支持在任何设备上部署，确保隐私与便捷并存。

2. **核心功能**
- 支持任意操作系统和平台的全局兼容部署。
- 提供完全私有化的个人 AI 助理体验。
- 强调用户数据所有权，确保数据安全可控。
- 基于 TypeScript 开发，具备良好的可扩展性。

3. **适用场景**
- 需要在本地或私有服务器部署个人 AI 助手的用户。
- 对数据隐私高度敏感、希望完全掌控 AI 数据的开发者。
- 希望在不同设备间无缝使用同一 AI 助理的多平台用户。

4. **技术亮点**
- 采用 TypeScript 编写，保证代码类型安全和开发效率。
- 架构设计支持高度自定义和模块化扩展。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 383819 | 🍴 80641 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理技能框架及软件开发方法论，旨在提升开发效率。它通过结构化的技能库和子代理驱动的开发模式，优化软件开发生命周期（SDLC）中的头脑风暴与编码环节。该项目强调利用 AI 代理能力来自动化和增强传统的软件开发流程。

2. **核心功能**
- 提供基于“技能”的可复用 AI 代理模块，支持模块化组合。
- 采用子代理驱动开发（Subagent-driven Development），将复杂任务分解由专门代理执行。
- 整合头脑风暴与代码生成能力，辅助从构思到实现的全流程。
- 定义标准化的软件开发方法论，使 AI 辅助编程具有可重复性和可靠性。

3. **适用场景**
- 需要大规模代码重构或复杂功能拆解的软件工程项目。
- 希望利用 AI 进行技术选型讨论、架构设计头脑风暴的开发团队。
- 寻求标准化 AI 辅助开发工作流，以提升 SDLC 效率的组织。

4. **技术亮点**
- 创新性地将“技能”概念引入 AI 代理框架，实现了开发逻辑的结构化封装。
- 结合 Shell 脚本实现轻量级部署与集成，便于嵌入现有 CI/CD 流水线。
- 链接: https://github.com/obra/superpowers
- ⭐ 259310 | 🍴 23115 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 218867 | 🍴 41446 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 197477 | 🍴 59538 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 致力于让每个人都能轻松使用并构建人工智能，实现 AI 的普及化愿景。其使命是提供强大的工具支持，让用户能够从繁琐的技术细节中解脱出来，专注于真正重要的核心事务。

2. **核心功能**
- 具备自主规划与执行任务的能力，可实现多步骤复杂工作流。
- 支持多种大型语言模型（如 GPT、Claude、Llama）的后端集成。
- 提供丰富的插件生态系统，扩展其在不同领域的应用能力。
- 拥有高度自动化的代理机制，能独立搜索信息并调用工具。
- 强调可访问性与易用性，降低构建 AI 智能体的技术门槛。

3. **适用场景**
- 自动化内容创作，如自动生成博客文章、社交媒体文案或报告。
- 复杂的数据分析与处理任务，包括网络爬虫和数据整理。
- 个人助理服务，用于管理日程、发送邮件或进行信息检索。
- 开发者原型验证，快速搭建和测试基于 LLM 的智能体应用。

4. **技术亮点**
- 作为开源 Agentic AI 领域的标杆项目，拥有极高的社区活跃度和星标数。
- 模块化架构设计，便于开发者根据需求定制和扩展特定功能。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185652 | 🍴 46071 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166208 | 🍴 21482 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164228 | 🍴 30433 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157223 | 🍴 46183 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 154419 | 🍴 8798 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152218 | 🍴 9626 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

