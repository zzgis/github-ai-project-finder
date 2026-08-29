# GitHub AI项目每日发现报告
日期: 2026-08-29

## 新发布的AI项目

### sepia
- 

## Sepia 项目分析

### 1. 中文简介
Sepia 是一款专为 Claude Code、Codex、Grok Build 和 Antigravity 等 AI 编程助手设计的"去AI化"写作技能工具。它能为小说提供叙事架构修复，同时为专业散文提供符合出版规范的写作规则。该项目基于 StoryScope 学术研究（arXiv:2604.03136）构建。

### 2. 核心功能
- **De-AI写作技能**：为多种AI编程助手提供去AI化写作能力
- **小说叙事架构修复**：帮助修复和优化小说的叙事结构
- **专业散文出版规则**：提供符合目标出版场所规范的写作指导
- **多平台兼容**：支持 Claude Code、Codex、Grok Build、Antigravity 等多个AI平台
- **学术研究支撑**：基于 StoryScope 论文的研究成果构建

### 3. 适用场景
- **AI辅助小说创作**：作家使用AI生成初稿后，用Sepia优化叙事结构和修复AI痕迹
- **专业写作润色**：学术论文、商业文案等需要符合特定出版规范的写作场景
- **AI内容去痕迹化**：将AI生成的文本转化为更自然、更像人类创作的内容
- **跨平台写作工作流**：在多个AI编程助手中统一使用同一套写作优化规则

### 4. 技术亮点
- **学术驱动设计**：基于 arXiv 论文（StoryScope）构建，具有研究基础
- **平台适配性强**：同时支持多个主流AI编程助手，扩展性好
- **分类处理机制**：针对小说和专业散文采用不同的优化策略，精准匹配需求
- 链接: https://github.com/Nanako0129/sepia
- ⭐ 640 | 🍴 32 | 语言: 未知
- 标签: agent-skills, ai-writing, antigravity, claude-code, codex

### remove-windows-ai
- 

## remove-windows-ai 项目分析

### 1. 中文简介
这是一个针对"移除Windows AI"方案的GUI前端概念工具，可帮助用户通过开关选项移除Windows 11中的Copilot、Recall等AI冗余功能，并提供一键还原功能。这是一个免费的开源社区项目，专为Windows用户打造。

### 2. 核心功能
- 图形化界面操作，简化AI功能移除流程
- 可独立开关移除Copilot、Recall等Windows AI组件
- 提供一键还原功能，方便恢复系统原状
- 开源免费，由社区共同维护

### 3. 适用场景
- 用户希望彻底移除Windows 11内置的Copilot AI助手
- 用户想禁用Recall截图回忆功能以保护隐私
- 追求系统精简、减少AI功能占用资源的技术爱好者
- 企业IT管理员批量部署无AI功能的Windows环境

### 4. 技术亮点
- 提供可视化GUI界面，降低命令行操作门槛
- 内置还原机制，确保操作可逆，降低用户风险
- 开源社区驱动，持续迭代优化
- 链接: https://github.com/meharabPigeon/remove-windows-ai
- ⭐ 150 | 🍴 0 | 语言: 未知
- 标签: ai, ai-script, copilot-remover, debloat, free-download

### dot-reflex
- 

# GitHub项目分析：dot-reflex

## 1. 中文简介
dot-reflex 是一款开源的 AI Agent 执行恢复控制器，专为编码和工具使用型 AI Agent 设计。它能够在 Agent 执行任务失败时自动检测并恢复执行，确保任务顺利完成。该项目结合了 LLM 能力和 QLoRA 微调技术，适用于需要高可靠性的智能体场景。

## 2. 核心功能
- **执行恢复控制**：自动检测 Agent 执行异常并触发恢复机制
- **编码任务支持**：专为编程和代码生成场景优化
- **工具调用管理**：协调 AI Agent 与外部工具的交互流程
- **Agent 监督机制**：实时监控 Agent 执行状态，防止失控
- **轻量化微调**：基于 QLoRA 技术实现高效模型适配

## 3. 适用场景
- 需要长时间运行的自动化编码任务（如代码生成、调试）
- 依赖多工具协作的复杂 AI Agent 工作流
- 对执行成功率要求较高的生产环境
- 基于 Qwen3 等模型的 Agent 系统部署

## 4. 技术亮点
- 结合 QLoRA 微调技术，在有限算力下实现高效模型适配
- 专为 coding agents 设计的恢复策略，提升任务完成可靠性
- 开源实现，支持自定义扩展和二次开发
- 链接: https://github.com/usedotai/dot-reflex
- ⭐ 97 | 🍴 0 | 语言: Python
- 标签: agent-supervision, ai-agents, coding-agents, llm, open-source

### windows-ai-privacy-toolkit
- 

## 项目分析：windows-ai-privacy-toolkit

---

### 1. 中文简介
这是一款以隐私保护为核心的开源工具，帮助用户盘点Windows PC上的AI功能，并一键关闭用户指定的AI特性。作为面向Windows的免费开源社区项目，它让用户重新掌控自己的设备隐私。

---

### 2. 核心功能
- **AI功能盘点**：自动扫描并列出Windows系统中所有已启用的AI功能。
- **按需禁用**：用户可选择关闭指定的AI功能，无需手动查找注册表或设置项。
- **隐私优先**：以保护用户隐私为核心目标，防止Windows AI功能在后台收集数据。
- **免费开源**：完全免费且开源，由社区维护，代码透明可审计。

---

### 3. 适用场景
- **Windows 11用户**：希望关闭Recall、Copilot等AI功能以保护隐私的用户。
- **企业IT管理员**：需要在组织内统一部署隐私策略，禁用不必要的AI特性。
- **隐私敏感人群**：不希望操作系统在后台运行AI相关功能、收集使用数据的用户。
- **低配设备用户**：希望减少后台AI功能占用系统资源的用户。

---

### 4. 技术亮点
- 针对Windows 11内置AI功能（如Recall、Copilot）提供一键禁用能力，操作简便，无需手动修改注册表。
- 链接: https://github.com/wimar393/windows-ai-privacy-toolkit
- ⭐ 73 | 🍴 0 | 语言: 未知
- 标签: ai, ai-features, disable, disable-windows, features

### seo-landing
- 描述: SEO Landing: Give your AI coding agent the capabilities of a senior Technical SEO engineer.  An agent skill for building high-performance, technically optimized SEO landing pages. Turn an AI coding agent into a technical SEO specialist.  Build and improve landing pages with: • 🚀 100/100 Google PageSpeed target • ⚡ Core Web Vitals optimization 
- 链接: https://github.com/aleksandr-alhoff/seo-landing
- ⭐ 41 | 🍴 4 | 语言: 未知
- 标签: agent-skills, antigravity, claude-skills, codex, core-web-vitals

### AI-Research-Assistant
- 描述: 无描述
- 链接: https://github.com/rpmalouin/AI-Research-Assistant
- ⭐ 29 | 🍴 1 | 语言: Python

### defi-native-skill
- 描述: Agent Skill that makes your AI crypto-native with an understanding of onchain capital markets: vaults, curators, yield decomposition, oracle classes, RWAs, stablecoins. Evergreen mental models plus live-data discipline: every number dated, every yield decomposed, read-only always.
- 链接: https://github.com/emlai/defi-native-skill
- ⭐ 21 | 🍴 1 | 语言: Python

### Product-to-Prod
- 描述: AI product management skills and plugin for Claude Code, Cowork, Codex and other AI agents: evidence-tagged PRDs, specs, requirements, RICE prioritization, backlog and roadmap scoring, product strategy, GTM launch plans, release verification, benchmark packs, UX/UI design prompts for web and mobile apps. Every claim sourced or labelled unsourced.
- 链接: https://github.com/naderelewa/Product-to-Prod
- ⭐ 19 | 🍴 1 | 语言: Shell
- 标签: agent-skills, ai-agents, ai-product-management, backlog, claude-code

### jiazuo-atelier
- 描述: 甲作 Atelier：手机端 AI 美甲推荐与虚拟试戴；仓库公开其中的轻量评测工作台。
- 链接: https://github.com/LalaGa-1119/jiazuo-atelier
- ⭐ 18 | 🍴 0 | 语言: TypeScript
- 标签: ai-evaluation, llm-evaluation, model-evaluation, multimodal, prompt-engineering

### hono-kun
- 描述: An AI maintainer for Hono
- 链接: https://github.com/honojs/hono-kun
- ⭐ 15 | 🍴 1 | 语言: TypeScript

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82754 | 🍴 15277 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36624 | 🍴 7475 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介

Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持多种主流框架的模型格式，能够以直观的图形方式展示模型结构和层间连接关系，帮助用户快速理解和分析模型架构。

### 2. 核心功能

- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等
- 提供直观的图形化界面展示神经网络层结构和数据流向
- 支持模型推理调试，可追踪张量形状和数值变化
- 兼容 safetensors 等新兴模型格式
- 支持查看模型参数和权重信息

### 3. 适用场景

- 模型结构分析与可视化，帮助开发者理解复杂网络架构
- 模型转换和格式迁移时的结构对比检查
- 深度学习模型调试，定位层间问题
- 教学演示，直观展示神经网络工作原理

### 4. 技术亮点

- 纯前端实现，无需安装额外依赖，跨平台兼容
- 支持大规模模型的高效渲染和交互浏览
- 活跃的开源社区，持续更新支持最新框架版本
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33425 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 

# ONNX 项目分析

## 1. 中文简介

ONNX（Open Neural Network Exchange）是一个开源机器学习标准格式，旨在实现不同深度学习框架之间的模型互操作性。它允许开发者在不同框架（如 PyTorch、TensorFlow、Keras 等）之间无缝转换和部署模型。

## 2. 核心功能

- 提供统一的模型表示格式，支持跨框架模型转换
- 定义开放的计算图标准，实现框架间的互操作性
- 支持主流深度学习框架（PyTorch、TensorFlow、Keras、scikit-learn 等）的模型导入导出
- 提供模型优化工具和推理运行时，提升部署效率

## 3. 适用场景

- 将 PyTorch 模型转换为可部署格式，用于生产环境推理
- 在不同深度学习框架间迁移模型，避免重新训练
- 在边缘设备或移动端部署深度学习模型
- 与硬件厂商合作，针对特定推理引擎进行模型优化

## 4. 技术亮点

- 由微软和 Facebook 联合发起，拥有广泛的社区支持和行业采用
- 支持超过 100+ 种算子，覆盖主流深度学习操作
- 提供 ONNX Runtime，可在多种硬件平台（CPU、GPU、NPU）上高效运行模型
- 与 MLIR、TensorRT、OpenVINO 等优化工具链深度集成
- 链接: https://github.com/onnx/onnx
- ⭐ 21379 | 🍴 4015 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 

## 项目分析：ml-engineering

### 1. 中文简介
《机器学习工程开放手册》是一本全面覆盖机器学习工程实践的知识库，涵盖从模型训练、推理部署到系统可扩展性的完整技术栈。项目以Python为核心，聚焦大语言模型（LLM）的工程化落地，是MLOps领域的权威参考指南。

### 2. 核心功能
- **训练工程**：提供基于PyTorch和Slurm的大规模分布式训练实践方案
- **推理优化**：涵盖LLM推理加速、GPU资源调度和网络优化策略
- **可扩展架构**：讲解存储、网络和计算资源的规模化扩展方法
- **调试与排错**：提供GPU集群和训练过程的系统级调试工具与技巧
- **端到端MLOps**：覆盖从开发到生产部署的完整机器学习流水线

### 3. 适用场景
- 大规模语言模型（LLM）的训练与微调工程部署
- GPU集群的分布式训练资源调度与性能优化
- 生产环境下的模型推理服务搭建与扩展
- MLOps团队建立标准化工程实践参考手册

### 4. 技术亮点
- **标签覆盖全面**：涵盖AI、LLM、PyTorch、Slurm、GPU、存储、网络等关键技术领域
- **高社区认可度**：18,835颗星标，反映其在ML工程社区的广泛影响力
- **开源开放**：以"Open Book"形式呈现，便于社区持续贡献与更新
- **实战导向**：聚焦真实工程问题，而非纯理论论述
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18835 | 🍴 1229 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17387 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15431 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13287 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11640 | 🍴 921 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10695 | 🍴 5695 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36624 | 🍴 7475 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介

Netron 是一款用于神经网络、深度学习和机器学习模型的可视化工具。它支持多种主流框架的模型格式，能够以直观的图形方式展示模型结构和层间连接关系，帮助用户快速理解和分析模型架构。

### 2. 核心功能

- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、Keras、CoreML 等
- 提供直观的图形化界面展示神经网络层结构和数据流向
- 支持模型推理调试，可追踪张量形状和数值变化
- 兼容 safetensors 等新兴模型格式
- 支持查看模型参数和权重信息

### 3. 适用场景

- 模型结构分析与可视化，帮助开发者理解复杂网络架构
- 模型转换和格式迁移时的结构对比检查
- 深度学习模型调试，定位层间问题
- 教学演示，直观展示神经网络工作原理

### 4. 技术亮点

- 纯前端实现，无需安装额外依赖，跨平台兼容
- 支持大规模模型的高效渲染和交互浏览
- 活跃的开源社区，持续更新支持最新框架版本
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33425 | 🍴 3175 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

## GitHub 项目分析：cheatsheets-ai

### 1. 中文简介
这是一个为深度学习和机器学习研究者准备的必备速查表集合，涵盖从基础概念到高级技术的核心知识要点，帮助研究人员快速查阅关键公式、API 和使用技巧。

### 2. 核心功能
- 提供深度学习与机器学习领域的速查表文档，便于快速查阅核心知识点
- 涵盖 Keras、NumPy、SciPy、Matplotlib 等常用库的使用技巧与语法速查
- 整合人工智能与深度学习领域的关键概念、公式和最佳实践
- 以简洁明了的格式呈现，适合打印或离线阅读参考

### 3. 适用场景
- 深度学习研究者快速复习和查阅核心概念与公式
- 机器学习工程师在日常开发中快速查找 API 用法和代码示例
- 学生或初学者系统学习深度学习知识体系时的参考资料
- 技术面试准备时快速梳理关键知识点

### 4. 技术亮点
- 项目聚焦实用性和查阅效率，将复杂技术内容浓缩为简洁的速查表单
- 覆盖从数据科学基础库（NumPy、SciPy、Matplotlib）到深度学习框架（Keras）的完整技术栈
- 由 Medium 技术博主推荐，在开发者社区中具有较高的认可度和传播度
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15431 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 

## Ai-Learn 项目分析

### 1. 中文简介
Ai-Learn 是一个系统化的人工智能学习路线图项目，收录了近200个实战案例与项目，并提供免费配套教材。项目从零基础入门，涵盖Python、数学基础到机器学习、深度学习、计算机视觉、自然语言处理等热门领域，旨在帮助学习者实现就业实战目标。

### 2. 核心功能
- 提供系统化AI学习路线图，涵盖从基础到进阶的完整学习路径
- 收录近200个实战案例与项目，配套免费教材供学习使用
- 覆盖Python、机器学习、深度学习、NLP、CV等多个热门技术方向
- 支持多种主流框架学习，包括PyTorch、TensorFlow、Keras、Caffe等
- 零基础友好，适合从入门到就业的完整学习需求

### 3. 适用场景
- 人工智能初学者系统学习，从零开始构建知识体系
- 数据科学与机器学习从业者提升技能、拓展实战经验
- 准备AI相关岗位求职，通过实战项目积累面试作品
- 高校学生或转行人员快速掌握AI核心技术栈

### 4. 技术亮点
- 整合多领域热门技术栈（算法、数据分析、深度学习、NLP、CV等），一站式学习资源
- 实战导向，以项目驱动学习，配套教材完善，适合就业实战
- 涵盖主流深度学习框架（TensorFlow 2.x、PyTorch、Keras、Caffe），适应不同技术偏好
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13287 | 🍴 2675 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一款低代码框架，用于构建自定义大语言模型、神经网络及其他 AI 模型。它简化了机器学习模型的训练、评估和部署流程，让开发者无需大量编码即可快速上手。

### 2. 核心功能
- **低代码模型开发**：通过声明式配置即可定义和训练神经网络，无需编写大量代码。
- **多模态支持**：支持文本、图像、表格等多种数据类型，适用于 NLP 和计算机视觉任务。
- **预训练模型集成**：内置对 LLaMA、Llama2、Mistral 等主流大模型的微调支持。
- **自动机器学习**：提供自动超参数调优和模型搜索功能，降低调参门槛。
- **端到端部署**：支持模型导出为 ONNX、TorchScript 等格式，便于在生产环境中部署。

### 3. 适用场景
- **企业级 AI 应用开发**：快速构建定制化 NLP 或 CV 模型，无需深度 ML 专家。
- **大模型微调**：对 LLaMA、Mistral 等开源模型进行领域适配和微调。
- **数据科学实验**：快速迭代实验，验证不同模型架构在特定数据集上的表现。
- **教育及入门学习**：降低深度学习入门门槛，帮助初学者快速理解模型训练流程。

### 4. 技术亮点
- 基于 PyTorch 构建，兼容主流深度学习生态。
- 支持分布式训练，可高效利用多 GPU 资源。
- 提供可视化的训练监控和实验管理功能。
- 兼容 Hugging Face Transformers，无缝集成生态资源。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11746 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9193 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8974 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1896 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6988 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6452 | 🍴 782 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82754 | 🍴 15277 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）和视觉语言模型（VLM）微调框架，支持 100+ 种主流模型。该项目已在 ACL 2024 发表，为开发者提供了一站式的模型微调解决方案。

### 2. 核心功能
- 支持 100+ 种大语言模型和视觉语言模型的统一微调
- 提供 LoRA、QLoRA、全参数微调等多种微调策略
- 支持 RLHF（基于人类反馈的强化学习）和指令微调
- 内置量化技术，降低显存占用，提升训练效率
- 兼容 Transformers 生态，简化模型部署流程

### 3. 适用场景
- 企业或个人对 Llama、Qwen、DeepSeek 等模型进行领域适配微调
- 需要低资源消耗的量化微调（如 QLoRA 方案）
- 构建具备多模态能力的视觉语言模型应用
- 研究或生产环境中的 RLHF 对齐训练

### 4. 技术亮点
- **统一架构**：一套代码支持百种模型，无需重复适配
- **高效微调**：LoRA/QLoRA 技术大幅降低显存需求，单卡即可训练
- **Mixture of Experts（MoE）支持**：兼容稀疏专家模型，提升推理效率
- **ACL 2024 认可**：学术研究背书，代码质量与可靠性有保障
- **丰富生态**：覆盖 Llama、Gemma、Qwen、DeepSeek 等主流模型系列
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74443 | 🍴 9117 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

### 1. 中文简介
这是一门由微软推出的AI入门课程，采用12周24课时的系统化教学设计，致力于让所有人都能轻松学习人工智能。课程以Jupyter Notebook为载体，覆盖从基础概念到深度学习的全方位内容。

### 2. 核心功能
- **系统化课程结构**：12周24课时的循序渐进式学习路径
- **全栈AI知识覆盖**：涵盖机器学习、深度学习、计算机视觉、NLP等核心领域
- **交互式学习环境**：基于Jupyter Notebook提供可运行的代码示例
- **微软官方背书**：微软初学者系列教育项目，内容权威可靠
- **零基础友好**：面向所有背景的学习者，无需深厚技术基础

### 3. 适用场景
- 计算机相关专业学生入门AI的学习课程
- 转行AI领域的开发者系统学习路径
- 企业团队AI技术培训与内部学习
- 对人工智能感兴趣的普通大众科普学习

### 4. 技术亮点
- 项目获得67686个星标，是GitHub上最受欢迎的AI入门课程之一
- 内容涵盖CNN、RNN、GAN等主流深度学习架构
- 微软教育团队精心设计的教学体系，理论与实践相结合
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 67686 | 🍴 13042 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 

## 项目分析：ai-engineering-from-scratch

### 1. 中文简介
本项目是一门系统性的AI工程课程，从基础概念讲起，引导学习者从零开始构建、部署AI系统，最终能够独立交付可用的AI产品给他人使用。

### 2. 核心功能
- 涵盖LLM、生成式AI、NLP等核心AI技术的从头实现与原理讲解
- 提供Agents、MCP、Swarm Intelligence等前沿AI Agent开发教程
- 包含计算机视觉、强化学习、深度学习等多元技术模块
- 提供Python和Rust双语言实现，兼顾易用性与高性能
- 配套完整课程结构，从学习到实践再到部署的全流程指导

### 3. 适用场景
- AI初学者希望系统性地从零掌握AI工程全栈能力
- 工程师想深入理解AI模型底层原理而非仅调用API
- 团队需要构建定制化AI Agent或智能体系统
- 研究者希望用Rust实现高性能AI推理组件

### 4. 技术亮点
- 采用"从 scratch 实现"的教学理念，深入理解模型内部机制
- 同时支持Python（快速原型）和Rust（高性能生产）两种语言栈
- 涵盖MCP（Model Context Protocol）等新兴AI交互标准
- 星标数近5.1万，说明社区认可度极高，内容质量有保障
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 50956 | 🍴 8820 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

**ailearning 项目分析**

---

**1. 中文简介**

这是一个全面的AI学习实战项目，涵盖数据分析与机器学习算法实现，结合线性代数基础，并集成PyTorch、NLTK和TensorFlow 2等主流框架进行深度学习与自然语言处理实践。

---

**2. 核心功能**

- 实现经典机器学习算法：Adaboost、SVM、KMeans、逻辑回归、朴素贝叶斯等
- 提供关联规则挖掘：Apriori、FP-Growth算法实战
- 深度学习框架实践：PyTorch与TensorFlow 2的DNN、CNN、RNN、LSTM模型实现
- 自然语言处理：基于NLTK的文本分析与推荐系统构建
- 降维与特征提取：PCA、SVD等线性代数方法应用

---

**3. 适用场景**

- 机器学习入门学习：从零掌握经典算法原理与代码实现
- 深度学习实战训练：基于PyTorch/TF2构建神经网络模型
- NLP项目开发：文本分类、情感分析等自然语言处理任务
- 推荐系统搭建：协同过滤与内容推荐算法实践

---

**4. 技术亮点**

- 算法覆盖全面：从传统机器学习到深度学习完整链路
- 框架双支持：同时提供PyTorch和TensorFlow 2实现
- 理论结合实战：线性代数基础与算法实现相融合
- 社区认可度高：42493星标，说明项目质量与实用性获广泛认可
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42493 | 🍴 11517 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36624 | 🍴 7475 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33861 | 🍴 4721 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29271 | 🍴 3575 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21878 | 🍴 3373 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17387 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36624 | 🍴 7475 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 

# Skyvern 项目分析

## 1. 中文简介
Skyvern 是一款基于人工智能的浏览器工作流自动化工具，能够智能地理解和执行复杂的网页操作任务。它通过结合大语言模型（LLM）和计算机视觉技术，让浏览器自动化更加智能、灵活和高效。

## 2. 核心功能
- 基于AI的智能浏览器自动化，能够理解网页内容并自主执行操作
- 支持多种主流浏览器自动化框架（Playwright、Puppeteer、Selenium）
- 提供标准化API接口，便于集成到现有业务流程中
- 利用计算机视觉技术识别页面元素，无需手动编写选择器
- 支持复杂工作流的编排与执行，可实现跨页面、跨标签页的自动化

## 3. 适用场景
- 电商平台的订单管理、价格监控和库存同步
- 企业内部系统的数据录入、报表生成和流程审批
- 网页数据抓取与批量信息处理
- 替代Power Automate等传统RPA工具进行网页自动化

## 4. 技术亮点
- 结合LLM（大语言模型）理解自然语言指令，降低自动化脚本编写门槛
- 支持多引擎切换，可根据需求灵活选择Playwright/Puppeteer/Selenium
- 视觉驱动的元素识别方式，适应动态网页和复杂UI结构
- 开源免费，社区活跃（22878+星标），技术栈现代且生态完善
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22878 | 🍴 2149 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉AI数据集的领先平台。它提供开源、云和企业合作产品，以及标注服务，支持图像、视频和3D标注，具备AI辅助标注、质量保障、团队协作、数据分析和开发者API等功能。

## 2. 核心功能
- **多模态标注**：支持图像、视频和3D数据的标注工作
- **AI辅助标注**：内置智能标注工具，提升标注效率
- **团队协作**：支持多人协作标注与任务分配
- **质量保障**：提供标注质量检查和验证机制
- **开发者API**：开放API接口，便于集成到现有工作流

## 3. 适用场景
- **自动驾驶**：标注道路场景图像和视频，用于目标检测和语义分割训练
- **工业质检**：标注产品缺陷图像，构建质量检测数据集
- **医疗影像**：标注医学图像，辅助AI辅助诊断模型训练
- **零售分析**：标注商品图像，用于商品识别和分类任务

## 4. 技术亮点
- 支持PyTorch和TensorFlow等主流深度学习框架
- 提供丰富的标注类型：边界框、图像分类、语义分割、目标检测等
- 开源社区活跃，星标数超过16,000，生态成熟
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16618 | 🍴 3822 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 

# GitHub项目分析：pytorch-grad-cam

## 1. 中文简介
该项目是一个先进的计算机视觉AI可解释性工具库，基于PyTorch实现。支持CNN、Vision Transformer等多种网络架构，可用于分类、目标检测、分割等任务的可视化解释。

## 2. 核心功能
- 提供Grad-CAM及其改进版本（如Score-CAM、Grad-CAM++等）的完整实现
- 支持CNN和Vision Transformer架构的可视化解释
- 兼容图像分类、目标检测、语义分割等多种任务类型
- 支持图像相似度分析的可解释性可视化
- 提供丰富的可视化输出，便于结果展示和分析

## 3. 适用场景
- 深度学习模型的可解释性研究，帮助理解模型决策依据
- 计算机视觉模型的调试与优化，定位模型关注区域
- 医疗影像分析等需要模型可解释性的专业领域
- AI伦理与合规审查，验证模型决策的合理性

## 4. 技术亮点
- 社区认可度高（12960+星标），是PyTorch生态中最流行的可解释性工具之一
- 完整实现了Grad-CAM系列算法，涵盖多种变体版本
- 对Vision Transformer等前沿架构提供良好支持
- 代码简洁易用，适合快速集成到现有项目中
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12960 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 

# Kornia 项目分析

## 1. 中文简介
Kornia 是一个面向空间 AI 的几何计算机视觉库，专为深度学习而设计。它基于 PyTorch 构建，提供可微分的图像处理操作，能够与神经网络无缝集成，为计算机视觉任务提供高效的解决方案。

## 2. 核心功能
- **可微分图像处理**：提供数百种可微分的几何视觉算子，支持反向传播优化
- **深度学习集成**：与 PyTorch 深度整合，可直接嵌入神经网络进行端到端训练
- **批量图像处理**：支持 GPU 加速的批量图像变换，提升大规模数据处理效率
- **机器人视觉支持**：内置相机模型和姿态估计工具，适用于机器人视觉应用
- **空间变换操作**：提供仿射变换、透视变换等几何变换的原语实现

## 3. 适用场景
- **自动驾驶与机器人导航**：利用几何视觉进行环境感知和定位
- **图像增强与数据增强**：在深度学习训练中实现可微分的数据增强
- **三维重建与SLAM**：支持空间推理和三维场景重建任务
- **医学图像分析**：用于可微分的图像配准和分割任务

## 4. 技术亮点
- **纯 PyTorch 实现**：无需额外依赖，与主流深度学习框架无缝兼容
- **高性能 GPU 加速**：所有算子均针对 GPU 优化，支持大规模并行计算
- **开源贡献友好**：参与 Hacktoberfest 活动，社区活跃且持续迭代
- **丰富的预训练模型**：提供多种预训练模型，便于快速上手和迁移学习
- 链接: https://github.com/kornia/kornia
- ⭐ 11334 | 🍴 1245 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8880 | 🍴 2187 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3488 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3441 | 🍴 423 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2636 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2504 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款跨平台、跨操作系统的个人 AI 助手工具，让你真正拥有自己的数据。它以"龙虾方式"重新定义了个人 AI 助手的体验——安全、自主、无处不在。

### 2. 核心功能
- 跨平台支持，可在任意操作系统上运行
- 个人 AI 助手，提供智能对话与任务处理能力
- 数据自主可控，用户完全掌握自己的数据
- 基于 TypeScript 开发，具备良好的可扩展性
- 开源项目，支持社区贡献与自定义开发

### 3. 适用场景
- 希望在本地部署个人 AI 助手的技术用户
- 注重数据隐私、不愿将数据上传至第三方云服务的用户
- 需要在多平台（Windows/macOS/Linux）统一使用 AI 助手的场景
- 开发者希望基于开源框架二次开发定制化 AI 应用

### 4. 技术亮点
- 使用 TypeScript 编写，类型安全且易于维护
- 跨平台架构设计，一次开发多端运行
- 开源自主可控，支持本地化部署
- 社区活跃度高（近 39 万星标），生态成熟
- 链接: https://github.com/openclaw/openclaw
- ⭐ 388009 | 🍴 81474 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 

## GitHub 项目分析：superpowers

### 1. 中文简介
Superpowers 是一个经过验证的 AI 代理技能框架与软件开发方法论，旨在帮助开发者更高效地构建软件。它采用子代理驱动开发模式，将复杂任务分解为可管理的技能模块，实现自动化协作。

### 2. 核心功能
- **代理技能框架**：提供结构化的 AI 代理技能体系，支持模块化开发
- **子代理驱动开发**：通过多个子代理协同完成软件开发全流程
- **头脑风暴辅助**：集成 AI 头脑风暴工具，辅助需求分析与方案设计
- **完整 SDLC 支持**：覆盖软件开发生命周期各阶段，从需求到交付
- **OBRA 方法论**：采用结构化开发方法论，提升开发效率与代码质量

### 3. 适用场景
- **AI 辅助编程**：开发者使用 AI 代理加速编码与调试过程
- **团队协作开发**：多代理协同完成中大型软件项目
- **快速原型开发**：利用技能框架快速构建 MVP 产品
- **软件开发流程优化**：企业采用标准化方法论提升交付效率

### 4. 技术亮点
- 基于 Shell 脚本实现，轻量级且易于集成到现有工作流
- 高星标数（27万+）表明社区认可度极高，具备成熟的生态系统
- 将 AI 代理能力与软件工程方法论深度结合，填补市场空白
- 链接: https://github.com/obra/superpowers
- ⭐ 279371 | 🍴 25020 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## hermes-agent 项目分析

### 1. 中文简介
这是一个能够与你共同成长的智能Agent，支持多种主流大语言模型（如Claude、ChatGPT等）。项目旨在为用户提供一个灵活、可扩展的AI助手框架，可根据需求持续优化和进化。

### 2. 核心功能
- 支持多种大语言模型（Claude、OpenAI等）的集成与切换
- 提供灵活的Agent架构，可根据任务需求进行定制
- 支持代码生成、调试和自动化执行
- 具备记忆和学习能力，能够随使用不断优化
- 开源免费，社区活跃，持续迭代更新

### 3. 适用场景
- 开发者日常编码辅助与代码审查
- 自动化任务执行与脚本编写
- 复杂问题的多步骤分析与解答
- AI应用开发与原型快速搭建

### 4. 技术亮点
- 高星标数（23万+）表明社区认可度高
- 支持Nous Research等知名研究机构的模型
- 兼容Claude Code和Codex等主流AI编程工具
- Python生态友好，易于集成和扩展
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 238121 | 🍴 48425 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介

n8n 是一款采用公平代码许可的工作流自动化平台，内置原生 AI 能力。它支持可视化搭建与自定义代码相结合，可自托管或云端部署，提供 400 多种集成连接器。

### 2. 核心功能

- **可视化工作流编辑器**：拖拽式界面，无需编程即可构建复杂自动化流程
- **原生 AI 集成**：内置 AI 节点，支持 LLM 调用、AI 代理和智能决策
- **400+ 集成连接器**：覆盖主流 SaaS 服务和 API，支持自定义扩展
- **MCP 协议支持**：原生兼容 Model Context Protocol，可连接多种 AI 模型与数据源
- **灵活部署方式**：支持自托管私有化部署或云端托管，数据完全可控

### 3. 适用场景

- **企业自动化**：将 CRM、ERP、邮件等系统串联，实现业务流程自动化
- **AI 工作流编排**：构建 RAG 问答、智能客服、内容生成等 AI 应用
- **数据同步与 ETL**：在不同平台间自动同步和转换数据
- **低代码/无代码开发**：让非技术人员也能快速搭建自动化解决方案

### 4. 技术亮点

- 基于 TypeScript 开发，类型安全且易于扩展
- 公平代码（Fair-code）许可，兼顾开源与商业友好性
- 支持 MCP Server/Client，可对接丰富的 AI 生态工具
- 强大的自定义节点开发能力，可通过代码深度定制工作流逻辑
- 链接: https://github.com/n8n-io/n8n
- ⭐ 202805 | 🍴 60459 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建 AI，实现 AI 普及化的愿景。我们的使命是提供完善的工具，让你能够专注于真正重要的事情。

### 2. 核心功能
- **自主任务执行**：Agent 可自动分解复杂任务并独立执行，无需人工干预每一步
- **多模型兼容**：支持 OpenAI GPT、Claude、Llama 等多种大语言模型后端
- **记忆系统**：具备长期记忆与短期记忆能力，可跨会话保留上下文信息
- **工具调用扩展**：通过插件机制集成浏览器、代码执行、文件操作等外部工具
- **链式推理**：支持思维链（Chain-of-Thought）推理，提升复杂问题的解决能力

### 3. 适用场景
- **自动化工作流**：将重复性任务（如数据整理、报告生成）交给 Agent 自动完成
- **研究与分析**：自动搜索信息、汇总资料并输出结构化分析报告
- **内容创作辅助**：协助撰写文章、代码、营销文案等创意内容
- **个人效率助手**：管理日程、提醒事项、执行多步骤日常操作

### 4. 技术亮点
- 基于 LLM 的自主决策架构，Agent 可自主规划并调整执行路径
- 高度模块化的插件系统，便于快速扩展新功能
- 开源社区活跃，持续迭代更新，生态丰富
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186990 | 🍴 46051 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 174057 | 🍴 9574 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 168176 | 🍴 21683 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164723 | 🍴 30557 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 158123 | 🍴 46165 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153868 | 🍴 9961 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

