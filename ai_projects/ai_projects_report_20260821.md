# GitHub AI项目每日发现报告
日期: 2026-08-21

## 新发布的AI项目

### coldcard-airgap
- 

## coldcard-airgap 项目分析

### 1. 中文简介
这是专为 Coldcard 硬件钱包用户设计的离线工具集，提供 PSBT 检查、BIP39 助记词与骰子熵生成、种子异或拆分/合并、BBQr 编码/解码、输出描述符处理及固件验证指南等功能。作为官方 Coldcard 固件的配套工具，由独立开发者维护，与 Coinkite 公司无隶属关系。

### 2. 核心功能
- **PSBT 检查**：离线查看和验证部分签名的比特币交易数据
- **熵源生成**：支持 BIP39 助记词生成及骰子真随机数输入
- **种子拆分与合并**：通过异或（XOR）操作将种子拆分或合并，增强安全性
- **BBQr 编解码**：将数据编码为二维码或从二维码解码，实现离线设备间传输
- **固件验证**：提供 Coldcard 固件的完整性验证指导

### 3. 适用场景
- Coldcard 用户离线检查交易详情，确认金额和地址无误后再签名
- 使用骰子生成高熵随机数，作为硬件钱包的种子输入
- 通过种子异或拆分，实现多签钱包或安全备份方案
- 在无网络环境下，通过 BBQr 二维码在冷钱包与热设备间安全传输数据

### 4. 技术亮点
- 纯 Python 实现，无需网络连接即可运行，确保离线安全性
- 与官方 Coldcard 固件配套使用，兼容 MK2 和 MK4 型号
- 涵盖从种子生成到交易签名的完整离线工作流
- 链接: https://github.com/Leutenegger/coldcard-airgap
- ⭐ 608 | 🍴 79 | 语言: Python
- 标签: airgap, airgap-devkit, airgap-download, airgap-setup, airgap-tutorial

### lanshu-create-ai-presenter-video
- 

## GitHub项目分析：lanshu-create-ai-presenter-video

### 1. 中文简介

这是一个与AI服务提供商无关的Codex技能，能够从脚本人像和授权的演示者图像中生成经过验证的AI演示者视频。用户只需提供脚本和授权的人像照片，即可自动创建逼真的AI数字人播报视频。

### 2. 核心功能

- **脚本驱动视频生成**：将文本脚本自动转换为AI演示者的口型同步视频
- **授权人像替换**：使用用户授权的演示者图像生成数字人播报
- **多服务商兼容**：不绑定特定AI视频生成服务商，支持多种后端
- **验证机制**：确保生成的视频内容符合脚本要求和授权规范
- **Codex集成**：作为OpenAI Codex CLI技能，可通过自然语言指令调用

### 3. 适用场景

- **企业培训视频制作**：快速将培训文档转化为数字人讲解视频
- **营销内容生产**：批量生成产品介绍的AI演示者视频
- **新闻播报制作**：用授权主持人形象生成新闻播报内容
- **教育课件制作**：将课程脚本转化为数字教师讲解视频

### 4. 技术亮点

- **Provider-neutral架构**：解耦了前端技能与后端视频生成服务，可灵活切换不同AI视频服务商
- **Codex Skill标准化**：遵循OpenAI Codex技能规范，便于集成到自动化工作流
- **授权验证机制**：内置授权检查，确保使用的人像图像已获得合法授权，降低法律风险
- 链接: https://github.com/cclank/lanshu-create-ai-presenter-video
- ⭐ 226 | 🍴 23 | 语言: Python
- 标签: ai-video, codex, codex-skill, digital-human, video-generation

### github-farm
- 

# GitHub项目分析：github-farm

---

## 1. 中文简介

这是一个生产级别的OAuth认证收集与会话管理框架，专为AI网关设计，支持多平台认证，并具备对AI智能体友好的特性。

---

## 2. 核心功能

- 支持多平台OAuth认证收集与会话管理
- 专为AI网关场景优化的生产级架构
- 提供AI智能体友好的接口设计
- 统一的会话状态管理与维护机制

---

## 3. 适用场景

- AI网关需要集成多个第三方平台认证的场景
- 构建支持多平台登录的AI助手或Agent系统
- 需要统一管理用户会话状态的后端服务开发

---

## 4. 技术亮点

- 采用生产级代码标准，适合直接部署到生产环境
- 针对AI网关场景做了专门优化，减少集成复杂度
- 链接: https://github.com/d4ncboz/github-farm
- ⭐ 101 | 🍴 8 | 语言: Python

### narralume
- 描述: Open-source AI-assisted writing studio for long-form fiction. 故事设定、正文版本、AI 协作、审稿与交付一体化的长篇小说写作工具。
- 链接: https://github.com/abligail/narralume
- ⭐ 71 | 🍴 13 | 语言: TypeScript
- 标签: ai-writing, creative-writing, llm, long-form-writing, novel-writing

### neurocursor-ai
- 

# GitHub 项目分析：neurocursor-ai

---

## 1. 中文简介

这是一个基于 C++ 开发的 AI 驱动摄像头鼠标光标控制工具。它可以将你的网络摄像头转变为免提指向设备，专为游戏场景设计，同时也适用于日常使用和辅助功能需求。

---

## 2. 核心功能

- 通过摄像头实现免提鼠标光标控制
- 支持面部追踪与头部追踪
- 支持眼球追踪功能
- 基于神经网络和机器学习算法驱动
- 用 C++ 编写，保证实时性与低延迟

---

## 3. 适用场景

- **游戏玩家**：无需手部操作即可控制光标，提升游戏体验
- **行动不便用户**：为残障人士提供无障碍的电脑操作方案
- **日常办公**：双手被占用时，通过视线或头部移动操控鼠标
- **演示与展示**：演讲或演示时无需手持遥控器即可翻页控制

---

## 4. 技术亮点

- **纯 C++ 实现**：相比 Python 方案，运行效率更高、延迟更低
- **多模态追踪融合**：同时支持面部、头部、眼球三种追踪方式，提升精度与稳定性
- **端到端 AI 方案**：基于神经网络直接输出光标坐标，无需额外校准步骤
- **开源轻量**：项目星标 50，适合二次开发与学习参考
- 链接: https://github.com/stems-arraign-48/neurocursor-ai
- ⭐ 50 | 🍴 0 | 语言: C++
- 标签: ai, computer-vision, cplusplus, cpp, cursor-control

### AItoFigma
- 描述: 一个 AI skill，可以把图片或是直接是内容输出到 figma，并且有这规范的尺寸
- 链接: https://github.com/Niall-Young/AItoFigma
- ⭐ 44 | 🍴 4 | 语言: JavaScript

### jiaojie-skill
- 描述: 交接 Skill（Jiaojie）：跨窗口、跨模型、跨设备、跨语言的 AI 上下文交接工具。换窗口，不失忆；换模型，不重来。Open-source AI context handoff.
- 链接: https://github.com/Jordanwei1/jiaojie-skill
- ⭐ 38 | 🍴 0 | 语言: Python
- 标签: agent-skills, ai-agent, ai-agents, ai-memory, claude-code

### KPMG_2_GLB
- 描述: This repository contains the lecture materials, notebooks, code, datasets, assignments, demonstrations, and resources used during the Industry-Oriented AI Foundamentals Training Program conducted in August 2026.
- 链接: https://github.com/AnantVerma-2022/KPMG_2_GLB
- ⭐ 29 | 🍴 0 | 语言: Jupyter Notebook

### cs-board
- 描述: 将参考声音和中文文案自动生成白板动画视频的本地 AI 工具。
- 链接: https://github.com/ChenShuo2004/cs-board
- ⭐ 26 | 🍴 3 | 语言: Python
- 标签: ai-video, chinese, fastapi, index-tts, react

### lieflat-less-ai-tone
- 描述: 一个基于 283 万字语料统计的去 AI 味 skill · An AI-tone removal skill grounded in a 2.83-million-character corpus study
- 链接: https://github.com/larashero3-dotcom/lieflat-less-ai-tone
- ⭐ 24 | 🍴 0 | 语言: Python

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82584 | 🍴 15271 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## 项目分析

### 1. 中文简介
这是一个收录了500个AI项目的Awesome列表，涵盖机器学习、深度学习、计算机视觉和自然语言处理等领域，每个项目均附带代码实现，非常适合学习者系统性地探索和实践。

### 2. 核心功能
- 收录500个AI/ML/DL/NLP/CV相关开源项目，每个项目均提供代码链接
- 按领域分类组织（机器学习、深度学习、计算机视觉、NLP等），便于快速定位
- 以Awesome列表形式呈现，精选高质量项目，节省筛选时间
- 主要基于Python生态，适配主流AI开发环境
- 持续更新，反映AI领域最新项目动态

### 3. 适用场景
- **AI初学者系统学习**：按模块逐步实践，从入门到进阶
- **项目灵感参考**：开发者寻找可复用的AI项目原型
- **技术选型调研**：对比不同领域的优秀开源实现
- **面试/作品集准备**：挑选高质量项目作为个人展示

### 4. 技术亮点
- 36429颗星，是GitHub上最热门的AI项目合集之一，社区认可度高
- 覆盖AI全栈领域，从基础机器学习到前沿深度学习，一站式获取资源
- 每个项目附带代码，可直接克隆运行，学习门槛低
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36429 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款开源的神经网络、深度学习和机器学习模型可视化工具，支持多种主流框架的模型格式。它提供直观的图形界面，帮助用户查看和理解模型结构。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、PyTorch、CoreML、Keras、TensorFlow Lite、SafeTensors 等
- 提供可视化神经网络架构图，清晰展示层结构、张量形状和数据流向
- 支持查看模型详细信息，如参数、权重和计算节点
- 兼容桌面应用和在线浏览器两种使用方式
- 支持模型调试与错误检测，帮助定位结构问题

### 3. 适用场景
- **模型开发调试**：开发者在构建神经网络时快速查看模型结构是否正确
- **模型格式转换验证**：验证不同框架间模型转换（如 PyTorch 转 ONNX）后的结构一致性
- **论文与报告展示**：将复杂的神经网络结构以清晰的图表形式呈现，用于学术发表或技术文档
- **模型部署检查**：在部署前检查模型在目标框架（如 CoreML、TensorFlow Lite）中的结构是否完整

### 4. 技术亮点
- 跨平台支持，无需依赖特定深度学习框架即可运行
- 开源免费，社区活跃，星标数超过 3.3 万，是同类工具中人气最高的项目之一
- 支持模型压缩和量化后的可视化分析
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 描述: Open standard for machine learning interoperability
- 链接: https://github.com/onnx/onnx
- ⭐ 21341 | 🍴 4007 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18680 | 🍴 1203 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11630 | 🍴 916 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10692 | 🍴 5697 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 

## GitHub项目分析：500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code

---

### 1. 中文简介

该项目是一个包含500个AI项目的代码集合，涵盖机器学习、深度学习、计算机视觉和自然语言处理四大领域。它汇集了丰富的实战项目代码，是AI学习者和开发者进行实践入门的综合性资源库。

---

### 2. 核心功能

- 收录500个AI相关实战项目，涵盖机器学习、深度学习、计算机视觉和NLP四大方向。
- 提供完整可运行的代码示例，便于学习者直接上手实践。
- 按技术领域分类整理，结构清晰，方便按需查找学习。
- 项目难度梯度合理，适合从入门到进阶的各级学习者。
- 星标数超3.6万，是GitHub上广受欢迎的AI学习资源之一。

---

### 3. 适用场景

- AI初学者系统学习机器学习、深度学习、计算机视觉和NLP的基础知识。
- 开发者寻找实战项目灵感，快速搭建AI原型或demo。
- 学生或研究人员作为课程作业、毕业设计的项目参考。
- 技术面试官准备AI相关面试题时的参考资料。

---

### 4. 技术亮点

- 项目数量庞大（500个），覆盖AI主流方向，资源密度高。
- 所有项目均附带代码，强调"学以致用"的实战导向。
- 标签分类细致（artificial-intelligence、machine-learning、deep-learning、computer-vision、nlp等），检索便捷。
- 高星标数（36429）证明其社区认可度和实用价值。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36429 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 

## Netron 项目分析

### 1. 中文简介
Netron 是一款神经网络、深度学习和机器学习模型的可视化工具。它支持多种主流框架格式，能够以图形化方式展示模型结构和参数，帮助开发者直观理解和分析模型。

### 2. 核心功能
- 支持多种模型格式，包括 ONNX、TensorFlow、Keras、PyTorch、CoreML、TensorFlow Lite、safetensors 等
- 提供清晰的神经网络结构图，直观展示层与层之间的连接关系
- 支持模型调试和错误检测，帮助定位模型构建问题
- 提供模型参数和权重的可视化查看功能
- 支持模型文件的对比分析，便于版本迭代跟踪

### 3. 适用场景
- 深度学习模型开发与调试过程中，快速查看模型结构
- 模型转换后的格式验证，确保转换前后结构一致
- 学术论文或技术报告中的模型架构图展示
- 团队协作中对模型结构的审查与讨论

### 4. 技术亮点
- 纯 JavaScript 实现，无需安装额外依赖，跨平台兼容性好
- 支持浏览器和桌面端两种运行方式，使用便捷
- 对 safetensors 等新兴格式的良好支持，紧跟技术发展趋势
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33381 | 🍴 3173 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 

# 项目分析：cheatsheets-ai

## 1. 中文简介
这是一个专为深度学习和机器学习研究者整理的必备速查表集合，涵盖AI、机器学习、Keras、NumPy、SciPy和Matplotlib等核心技术的常用代码片段与公式。项目旨在帮助研究人员快速查阅和复习关键技术要点，提升学习与工作效率。

## 2. 核心功能
- 提供深度学习与机器学习领域的核心公式和概念速查表
- 涵盖Keras、NumPy、SciPy、Matplotlib等常用库的代码示例
- 整理人工智能领域的关键知识点，便于快速查阅与复习
- 以简洁的表格和代码形式呈现，适合打印或在线查阅
- 由社区维护更新，持续补充新的技术内容

## 3. 适用场景
- 深度学习/机器学习研究者快速复习核心公式与概念
- 数据科学家日常编码时查阅常用库的API用法
- 学生备考或面试前突击复习AI相关知识点
- 研究人员撰写论文或报告时参考标准实现方式

## 4. 技术亮点
- 聚焦实用性与速查效率，内容精炼不冗余
- 覆盖从基础数学到高级框架的完整技术栈
- 高星标数（15427）印证了社区认可度和实用性
- 与Medium技术博客联动，内容来源权威可靠
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15427 | 🍴 3372 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13275 | 🍴 2673 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 

## Ludwig 项目分析

### 1. 中文简介
Ludwig 是一个低代码框架，用于构建自定义的大型语言模型（LLM）、神经网络及其他 AI 模型。它通过声明式接口简化了机器学习流程，让开发者无需编写大量代码即可快速训练和部署模型。

### 2. 核心功能
- 声明式低代码接口，通过 YAML/JSON 配置即可构建模型
- 支持多模态数据训练，包括文本、图像、表格数据等
- 内置超参数优化和自动模型调优功能
- 与 Hugging Face Transformers 深度集成，支持 LLM 微调（如 LLaMA、Mistral）
- 提供可视化训练过程和模型评估工具

### 3. 适用场景
- 快速原型开发：无需深入编码即可搭建和训练神经网络
- LLM 微调：针对特定任务对 LLaMA、Mistral 等大模型进行微调
- 多模态 AI 应用：同时处理文本和图像数据的复杂任务
- 数据驱动研究：适合数据科学家专注于数据而非基础设施

### 4. 技术亮点
- 基于 PyTorch 构建，兼容主流深度学习生态
- 支持 GPU 加速训练，适合大规模模型训练
- 与 MLflow 等 MLOps 工具集成，便于模型版本管理和部署
- 强调"数据中心"理念，简化数据预处理和特征工程流程
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11745 | 🍴 1217 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9179 | 🍴 1232 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8967 | 🍴 3109 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8371 | 🍴 1897 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6990 | 🍴 1173 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6422 | 🍴 777 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82584 | 🍴 15271 | 语言: Python

### LlamaFactory
- 

## LlamaFactory 项目分析

### 1. 中文简介
LlamaFactory 是一个统一且高效的微调框架，支持 100+ 种大语言模型（LLM）和视觉语言模型（VLM）的微调，相关研究已发表于 ACL 2024。

### 2. 核心功能
- 支持 100+ 主流大语言模型和视觉语言模型的一站式微调
- 提供多种高效微调方法，包括 LoRA、QLoRA、全参数微调等
- 集成 RLHF（基于人类反馈的强化学习）支持，实现模型对齐优化
- 支持量化技术，降低显存占用，适配资源受限环境
- 提供简洁的命令行接口和 Web UI，降低微调门槛

### 3. 适用场景
- 快速微调 Llama、Qwen、DeepSeek 等主流大模型以适应特定任务
- 在有限显存条件下对大模型进行低成本高效微调
- 通过指令微调（Instruction Tuning）提升模型的对话和指令遵循能力
- 对多模态视觉语言模型进行微调，支持图文理解任务

### 4. 技术亮点
- 统一框架整合多种模型架构和微调策略，实现"一次配置，多模型适配"
- 内存优化出色，QLoRA 支持在单张消费级显卡上微调大参数模型
- 模块化设计，支持灵活组合不同模型、数据、训练策略
- 社区活跃，持续跟进最新模型和训练方法（如 MoE、Gemma 等）
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 74280 | 🍴 9083 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 

## AI-For-Beginners 项目分析

---

### 1. 中文简介

这是由微软推出的AI入门课程，涵盖12周、24课时的系统学习路径。课程面向零基础学习者，以Jupyter Notebook为载体，让任何人都能轻松上手人工智能。

---

### 2. 核心功能

- **系统化课程体系**：12周渐进式教学，从基础概念到深度学习全面覆盖
- **实践导向学习**：采用Jupyter Notebook交互式编程环境，边学边练
- **多领域AI技术**：涵盖机器学习、深度学习、计算机视觉、自然语言处理等核心方向
- **微软官方背书**：由微软开发者社区维护，内容质量有保障

---

### 3. 适用场景

- **初学者入门**：零AI基础的学习者系统掌握人工智能核心概念与技能
- **高校/培训机构教学**：作为人工智能通识课程的配套教材使用
- **企业内训参考**：技术团队快速了解AI技术栈的学习资源
- **自学者进阶**：希望系统学习CNN、RNN、GAN等深度学习模型的学习者

---

### 4. 技术亮点

- **GitHub星标超6.6万**：说明该项目在社区中获得了极高的认可度和广泛使用
- **标签覆盖全面**：从ML/DL到CV/NLP均有涉及，课程体系完整
- **微软"For Beginners"系列**：与微软其他入门级技术课程形成品牌联动，学习路径清晰
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 66076 | 🍴 12806 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 47505 | 🍴 8353 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 

# GitHub项目分析：ailearning

## 1. 中文简介
这是一个综合性的机器学习学习项目，涵盖数据分析、机器学习实战、线性代数基础，以及PyTorch和TensorFlow 2等深度学习框架的应用。项目通过NLTK库支持自然语言处理相关内容，适合系统学习AI相关技术。

## 2. 核心功能
- 提供机器学习经典算法的实战实现，包括SVM、KMeans、逻辑回归、朴素贝叶斯等
- 涵盖深度学习框架PyTorch和TensorFlow 2的教程与实践
- 包含自然语言处理（NLP）相关内容的学习资源
- 支持推荐系统、数据降维（PCA/SVD）等应用场景
- 集成FP-Growth、Apriori等关联规则挖掘算法

## 3. 适用场景
- 机器学习入门学习者的系统学习路径
- 需要实战案例的算法工程师提升技能
- 深度学习框架（PyTorch/TF2）的学习者
- 自然语言处理（NLP）方向的研究与开发

## 4. 技术亮点
- 涵盖从传统机器学习到深度学习的完整技术栈
- 结合理论与实践，提供可运行的代码示例
- 使用主流框架（PyTorch、TensorFlow 2）进行深度学习教学
- 集成NLTK等NLP工具，支持自然语言处理学习
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42469 | 🍴 11515 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36429 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33838 | 🍴 4711 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 29163 | 🍴 3553 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21844 | 🍴 3358 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17380 | 🍴 2126 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 36429 | 🍴 7450 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 描述: Automate browser based workflows with AI
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22817 | 🍴 2141 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 

# CVAT 项目分析

## 1. 中文简介
CVAT（计算机视觉标注工具）是构建高质量视觉数据集的领先平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保证、团队协作等功能，并配备开发者API。

## 2. 核心功能
- **AI辅助标注**：利用预训练模型自动标注，显著提升标注效率
- **多模态支持**：支持图像、视频及3D点云数据标注
- **团队协作**：多人可并行标注，内置审核与质量保证机制
- **丰富标注类型**：支持边界框、语义分割、关键点等多种标注格式
- **开放API与集成**：提供开发者API，可与主流深度学习框架无缝对接

## 3. 适用场景
- 计算机视觉数据集构建（如ImageNet类图像分类数据集）
- 目标检测模型训练数据标注
- 语义分割/实例分割标注任务
- 视频目标跟踪与动作识别数据准备

## 4. 技术亮点
- 基于Python开发，兼容PyTorch和TensorFlow生态
- 支持一键导入导出主流数据集格式
- 开源项目，社区活跃（GitHub星标16,559+）
- 提供企业级私有化部署方案
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16559 | 🍴 3809 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12955 | 🍴 1705 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 描述: 🐍 Geometric Computer Vision Library for Spatial AI
- 链接: https://github.com/kornia/kornia
- ⭐ 11319 | 🍴 1227 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8873 | 🍴 2188 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3483 | 🍴 878 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3387 | 🍴 415 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2634 | 🍴 691 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2507 | 🍴 227 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 

## OpenClaw 项目分析

### 1. 中文简介
OpenClaw 是一款完全由您掌控的个人AI助手，支持任意操作系统和平台。它以"龙虾方式"重新定义数据主权，让您真正拥有自己的AI体验。

### 2. 核心功能
- **个人AI助手**：提供专属的AI助手服务，满足日常智能需求
- **跨平台支持**：兼容任意操作系统和平台，实现无缝使用
- **数据自主权**：强调"own-your-data"理念，用户完全掌控个人数据
- **开源自由**：基于开源协议，社区驱动持续开发
- **TypeScript构建**：使用TypeScript开发，保证代码质量与可维护性

### 3. 适用场景
- **个人效率提升**：作为日常AI助手，处理日程管理、信息查询等任务
- **数据隐私敏感用户**：关注数据主权、不希望数据被第三方平台收集的用户
- **开发者工具链**：需要本地部署AI助手进行开发调试的技术人员
- **跨平台办公需求**：需要在不同操作系统间切换使用的多平台用户

### 4. 技术亮点
- **高人气项目**：38万+星标，社区活跃度高，生态成熟
- **数据主权架构**：从设计层面保障用户对数据的完全控制权
- **TypeScript全栈**：前后端统一技术栈，开发效率高、类型安全
- **开源协作模式**：开放源码，支持社区贡献与自定义扩展
- 链接: https://github.com/openclaw/openclaw
- ⭐ 387028 | 🍴 81294 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 描述: An agentic skills framework & software development methodology that works.
- 链接: https://github.com/obra/superpowers
- ⭐ 275459 | 🍴 24632 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 

## Hermes-Agent 项目分析

### 1. 中文简介
Hermes-Agent 是一款能够随用户成长进化的智能 AI 代理工具。它支持多种主流大语言模型平台，包括 Claude、ChatGPT 和 Codex，为用户提供灵活且强大的 AI 辅助能力。

### 2. 核心功能
- 支持多模型切换，兼容 Claude、ChatGPT 和 Codex 等主流 LLM 平台
- 具备记忆与学习能力，代理能力可随使用持续进化
- 提供灵活的 API 接口，便于开发者集成到自有项目中
- 支持自定义指令与任务配置，适应不同工作流需求
- 开源可定制，社区活跃且持续迭代更新

### 3. 适用场景
- **开发者辅助编程**：代码生成、调试与重构的智能助手
- **研究与数据分析**：快速处理复杂查询与数据整理任务
- **内容创作与写作**：辅助撰写文档、报告及创意内容
- **自动化工作流**：通过 Agent 自动化执行重复性日常任务

### 4. 技术亮点
- 多模型统一接入层，一键切换不同 LLM 后端
- 基于 Nous Research 开源模型优化，提供高质量对话体验
- 高星标社区认可（23万+），说明项目成熟度与用户口碑俱佳
- 支持本地部署与云端调用，灵活适配不同隐私与安全需求
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 233866 | 🍴 46918 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 

## n8n 项目分析

### 1. 中文简介
n8n 是一款公平源码的工作流自动化平台，内置原生 AI 能力。它结合了可视化构建与自定义代码，支持自托管和云端部署，并提供 400 多种集成方式。

### 2. 核心功能
- **可视化工作流构建**：通过拖拽方式创建自动化流程，降低使用门槛。
- **原生 AI 集成**：内置 AI 能力，可直接在工作流中调用 AI 模型。
- **400+ 集成节点**：支持丰富的第三方应用和服务连接。
- **灵活部署**：支持自托管和云端部署，满足数据隐私需求。
- **代码与低代码结合**：既支持无代码操作，也允许编写自定义代码扩展。

### 3. 适用场景
- **企业自动化**：自动化日常业务流程，如数据同步、通知推送等。
- **API 集成**：连接多个系统，实现跨平台数据流转。
- **AI 工作流**：构建包含 AI 推理的智能自动化流程。
- **数据管道**：自动化数据处理和 ETL 任务。

### 4. 技术亮点
- 基于 TypeScript 开发，类型安全且易于扩展。
- 支持 MCP（Model Context Protocol）协议，可与 AI 模型深度集成。
- 公平源码许可，兼顾开源社区与商业使用需求。
- 活跃的开源社区，星标数超过 20 万，生态成熟。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 201495 | 🍴 60262 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 

## AutoGPT 项目分析

### 1. 中文简介
AutoGPT 致力于让每个人都能轻松使用并构建AI，实现AI的普惠化愿景。我们的使命是提供必要的工具，让您能够专注于真正重要的事情。

### 2. 核心功能
- 支持自主创建和运行AI代理，无需人工持续干预
- 提供丰富的工具集，包括网络浏览、文件操作、代码执行等
- 支持多种大语言模型后端（OpenAI、Claude、Llama等）
- 具备任务分解与自主决策能力
- 开源可定制，用户可根据需求扩展功能

### 3. 适用场景
- 自动化日常任务（如信息搜集、报告生成）
- 内容创作与营销文案自动生成
- 代码开发与调试辅助
- 研究分析与数据整理

### 4. 技术亮点
- 多模型兼容架构，灵活切换不同LLM后端
- 模块化设计，便于二次开发和功能扩展
- 开源社区活跃，持续迭代更新
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 186713 | 🍴 46044 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### firecrawl
- 描述: The context API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 170409 | 🍴 9479 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 167697 | 🍴 21650 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164600 | 🍴 30550 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157927 | 🍴 46169 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 153529 | 🍴 9902 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

