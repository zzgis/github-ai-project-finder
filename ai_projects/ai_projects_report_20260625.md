# GitHub AI项目每日发现报告
日期: 2026-06-25

## 新发布的AI项目

### awesome-evals
- 1. **中文简介**
awesome-evals 是由 BenchFlow 维护的一份精选资源库，旨在为构建和评估 AI 智能体提供最优质、无冗余的资料。它汇集了相关的学术论文、博客文章、演讲视频、实用工具及基准测试数据集。该项目专注于解决大语言模型（LLM）智能体开发中的评估难题。

2. **核心功能**
*   提供经过筛选的高质量 AI 智能体评估资源列表，避免信息过载。
*   整合从学术研究到工程实践的多维度资料，包括论文、博客和技术演讲。
*   汇集实用的评估工具和标准化的基准测试数据集以辅助性能衡量。
*   专注于 LLM 智能体领域的特定需求，如 Agent 评估和 RL 环境支持。
*   由专业团队定期维护，确保资源库的时效性和相关性。

3. **适用场景**
*   研究人员需要快速检索最新的 LLM 智能体评估基准和相关学术文献。
*   工程师在开发 AI Agent 时寻找可靠的评估工具集和最佳实践指南。
*   技术管理者希望了解当前 AI 智能体评估领域的主流趋势和核心资源。
*   学习者想要系统性地入门 AI 智能体评估，通过精选资料建立知识体系。

4. **技术亮点**
*   **去噪精选**：强调“非 BS”（无废话），直接提供高价值内容，节省用户筛选时间。
*   **全链路覆盖**：涵盖从理论（论文/演讲）到实践（工具/基准）的完整评估生态。
*   **社区驱动维护**：由 BenchFlow 持续更新，确保资源紧跟 AI 智能体评估领域的发展步伐。
- 链接: https://github.com/benchflow-ai/awesome-evals
- ⭐ 239 | 🍴 11 | 语言: 未知
- 标签: agent-evaluation, ai-agents, awesome, awesome-list, benchmarks

### ShipGenAI
- ### ShipGenAI 项目分析报告

**1. 中文简介**
该项目提供 50 个生产就绪的生成式 AI SaaS 应用模板，用户可轻松自定义品牌并部署上线，且能保留 100% 的收益。它集成了 Stripe 支付、Google OAuth 认证及 Vercel 部署方案，采用 MIT 开源协议，旨在帮助开发者快速构建和商业化 AI 产品。

**2. 核心功能**
*   **海量模板库**：包含 50 个现成的生成式 AI 应用样板代码，涵盖文本、图像及视频生成等多种类型。
*   **完整商业化套件**：内置 Stripe 计费系统和 Google OAuth 身份验证，开箱即用，无需从零搭建支付与登录模块。
*   **一键部署支持**：专为 Vercel 平台优化，支持快速部署和持续集成，极大简化运维流程。
*   **高收益留存政策**：明确允许开发者保留应用产生的全部收入，无平台抽成限制。
*   **开源宽松授权**：采用 MIT 许可证，允许自由修改、分发和商业使用，法律风险极低。

**3. 适用场景**
*   **独立开发者快速变现**：希望利用现有 AI 能力快速推出 SaaS 产品并实现收入自动化的个人开发者。
*   **初创公司 MVP 构建**：需要低成本、短时间验证生成式 AI 商业模式的技术初创团队。
*   **前端/全栈学习进阶**：希望通过分析真实商业级代码（Next.js + TypeScript + Stripe）来学习现代 Web 开发最佳实践的程序员。
*   **企业内部工具定制**：需要基于生成式 AI 快速搭建内部自动化流程或客户服务原型的中小型企业。

**4. 技术亮点**
*   **技术栈现代化**：基于 Next.js 框架和 TypeScript 语言，确保应用的高性能、类型安全和可维护性。
*   **全链路解决方案**：不仅提供 UI 和逻辑代码，还整合了关键的第三方服务接口（支付、认证、部署），解决了 SaaS 开发中最繁琐的后端集成问题。
- 链接: https://github.com/benlamiro/ShipGenAI
- ⭐ 117 | 🍴 0 | 语言: JavaScript
- 标签: ai, boilerplate, generative-ai, gpt, image-generation

### claude-ai-desktop-app
- ### 1. 中文简介
该项目是一个开源的 Claude 代码 AI 桌面应用程序，支持 Windows、Linux 和 macOS 平台。它旨在提供免费的 API 访问和本地 LLM 路由功能，并集成了对 NVIDIA NIM、OpenRouter、DeepSeek、Ollama 等模型的兼容支持。

### 2. 核心功能
- **多模型路由与支持**：兼容 Anthropic API、本地 Ollama/LM Studio 以及 OpenRouter、DeepSeek、NVIDIA NIM 等多种后端服务。
- **跨平台桌面应用**：原生支持 PC 端（Windows/Linux/macOS），提供独立的桌面客户端体验。
- **IDE 与 CLI 集成**：除了桌面应用，还扩展支持 VS Code 插件、JetBrains 插件以及命令行终端调用。
- **免费 API 代理机制**：通过代理服务器或本地路由器实现 Claude Code 功能的免费或低成本访问。

### 3. 适用场景
- **开发者日常编码辅助**：在 VS Code 或 JetBrains IDE 中利用 Claude 进行代码生成、审查和调试。
- **本地化 AI 部署需求**：需要在不依赖外部付费 API 的情况下，通过本地模型（如 Ollama）运行 AI 编程助手。
- **多模型切换测试**：开发人员希望在一个界面中统一管理和对比不同提供商（Anthropic, DeepSeek, OpenRouter）的模型表现。

### 4. 技术亮点
- **全栈覆盖**：同时提供桌面端、浏览器插件、IDE 扩展和 CLI 工具，满足不同工作流需求。
- **灵活的后端抽象**：通过“Local LLM Router”架构，实现了前端与后端模型的解耦，便于接入各种新兴 AI 服务。
- 链接: https://github.com/samuto69/claude-ai-desktop-app
- ⭐ 101 | 🍴 0 | 语言: TypeScript
- 标签: claude-code, claude-code-action, claude-code-api, claude-code-desktop, claude-code-open

### muteki
- ### 项目名称：Muteki

#### 1. 中文简介
Muteki 是一个自主运行的多模型 AI 智能体集群，专为自动化解决 Capture The Flag (CTF) 网络安全竞赛题目而设计。它通过整合多种人工智能模型的能力，模拟团队协作来分析和破解安全挑战。

#### 2. 核心功能
*   **多模型协同**：集成并调度多个不同的 AI 模型共同处理复杂任务。
*   **自主决策执行**：智能体集群能独立分析题目线索并自动执行解题步骤。
*   **CTF 专项优化**：针对网络安全竞赛的常见题型和攻击向量进行专门适配。
*   **集群化架构**：采用智能体群（Swarm）模式，提高解题的容错率和成功率。

#### 3. 适用场景
*   **CTF 竞赛辅助**：帮助参赛队伍自动化完成部分或全部技术性解题环节。
*   **安全技能训练**：用于学习者通过 AI 反馈快速理解漏洞原理和利用方法。
*   **自动化渗透测试研究**：作为概念验证工具，探索 AI 在自动化漏洞挖掘中的潜力。

#### 4. 技术亮点
*   利用大型语言模型（LLM）的多模态协作能力替代传统的人工解题逻辑。
*   实现了从题目解析到代码生成、再到漏洞利用的端到端自动化闭环。
- 链接: https://github.com/FishCodeTech/muteki
- ⭐ 64 | 🍴 8 | 语言: Python

### ai-fishing-game
- ### 1. 中文简介
这是一个专为 AI 设计的确定性文字钓鱼小游戏，采用单文件且零依赖的 Python 实现。该项目的核心目的是让 AI 伴侣能够参与并体验钓鱼互动的乐趣。

### 2. 核心功能
*   **AI 专属交互**：设计初衷是让大语言模型或 AI 助手作为玩家参与游戏逻辑。
*   **确定性机制**：基于确定性算法运行，确保每次模拟结果可复现，适合测试或演示。
*   **极简部署**：单文件结构且无任何外部依赖库，便于快速集成和运行。
*   **文字驱动玩法**：纯文本交互模式，无需图形界面即可完整呈现游戏流程。
*   **轻量级娱乐**：提供简单的策略与运气结合的文字冒险体验。

### 3. 适用场景
*   **AI 能力测试**：用于评估 LLM 在逻辑推理、状态管理和角色扮演方面的表现。
*   **智能体互动演示**：展示 AI 助手如何通过对话进行沉浸式游戏互动。
*   **教学示例**：作为 Python 编程或 Prompt Engineering 的简单入门案例。
*   **个性化娱乐**：为用户的私人 AI 伴侣增加趣味性的日常互动环节。

### 4. 技术亮点
*   **零依赖架构**：完全使用 Python 标准库实现，无需安装 `pip` 包，极大降低了使用门槛和环境配置复杂度。
*   **可重现性**：确定性设计使得游戏过程对 AI 而言是可预测的，便于调试和分析模型行为。
- 链接: https://github.com/tutusagi/ai-fishing-game
- ⭐ 33 | 🍴 3 | 语言: Python

### hlwy-ai-checker
- 描述: 检查第三方AI API是否掺假以及渠道一致
- 链接: https://github.com/hanlinwenyuan/hlwy-ai-checker
- ⭐ 30 | 🍴 3 | 语言: HTML

### nexusbox
- 描述: Secure sandbox for AI Agents — execute shell, file, code, and browser commands in isolation via MCP.
- 链接: https://github.com/lxcshine/nexusbox
- ⭐ 19 | 🍴 4 | 语言: Go

### patchright-browser
- 描述: MCP server for browser automation via Patchright. Multi-profile Chromium, headed/headless, StreamableHTTP protocol. Includes dashboard, skills, and AI agent setup.
- 链接: https://github.com/rickicode/patchright-browser
- ⭐ 17 | 🍴 2 | 语言: Python
- 标签: ai-agent, browser-automation, chromium, headless-browser, hermes

### agentic-ai-local-to-kubernetes
- 描述: Companion repository for the talk, Agentic AI: Going from Local to Kubernetes
- 链接: https://github.com/lkerriso/agentic-ai-local-to-kubernetes
- ⭐ 15 | 🍴 4 | 语言: Python

### xs_vibe_rules
- 描述: My Cursor Rules for AI coding assistants — battle-tested constraints from real projects
- 链接: https://github.com/itshen/xs_vibe_rules
- ⭐ 15 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81442 | 🍴 15245 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的代码合集。它涵盖了广泛的技术领域，为开发者提供了丰富的实战案例。项目以“Awesome”列表形式呈现，旨在成为该领域的资源宝库。

2. **核心功能**
*   提供大量现成的机器学习与深度学习项目源码。
*   覆盖计算机视觉和自然语言处理等主流AI子领域。
*   作为全面的项目学习资源库，支持快速查阅与实践。
*   集成Python等常用编程语言的实际应用案例。

3. **适用场景**
*   AI初学者希望系统性地通过代码实践来巩固理论知识。
*   研究人员需要参考现有项目结构以快速启动新的AI实验。
*   开发者在构建具体应用时，寻求类似计算机视觉或NLP任务的代码模板。

4. **技术亮点**
*   极高的社区认可度，拥有超过3.4万星标，证明了其资源的实用性和广泛性。
*   内容覆盖面极广，从基础机器学习到前沿深度学习均有涉及。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34859 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33131 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**
ONNX（Open Neural Network Exchange）是机器学习的开放标准，旨在促进不同深度学习框架之间的互操作性。它允许开发者轻松地将模型从一种框架转换到另一种框架，从而简化模型的部署与共享流程。

2. **核心功能**
- 提供统一的中间表示格式，支持跨框架的模型交换。
- 集成丰富的算子库，覆盖主流深度学习网络结构。
- 支持多平台推理引擎，实现高效且一致的模型执行。
- 提供完善的工具链，便于模型的转换、验证与优化。

3. **适用场景**
- 在不同深度学习框架（如PyTorch转TensorFlow）之间迁移模型。
- 将训练好的模型部署到边缘设备或嵌入式系统中运行。
- 在异构硬件环境（如CPU、GPU、NPU）上统一调度推理任务。

4. **技术亮点**
- 作为行业标准被广泛采纳，拥有庞大的社区生态和框架支持。
- 强调性能优化，通过标准化接口提升模型推理效率。
- 链接: https://github.com/onnx/onnx
- ⭐ 21045 | 🍴 3954 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 描述: Machine Learning Engineering Open Book
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18172 | 🍴 1153 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2109 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11524 | 🍴 902 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10638 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个收录了500个AI相关代码项目的精选资源库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等核心领域。该项目旨在为开发者提供丰富的实战案例和代码参考，帮助快速掌握人工智能技术的实际应用。

2. **核心功能**
*   汇集大量涵盖机器学习与深度学习的完整代码项目。
*   提供计算机视觉与自然语言处理领域的专项实战案例。
*   作为AI学习者的“Awesome”资源列表，便于系统性检索与学习。
*   支持Python等多语言环境下的算法复现与模型训练。

3. **适用场景**
*   AI初学者希望寻找从理论到实践的入门级代码示例进行学习。
*   数据科学家需要参考现有的计算机视觉或NLP解决方案以加速开发进程。
*   研究人员或学生希望浏览最新的人工智能项目趋势以获取灵感。
*   企业团队在进行技术选型时，通过对比开源项目评估不同算法的可行性。

4. **技术亮点**
*   极高的社区认可度，拥有超过34,000个星标，证明其内容的实用性与权威性。
*   标签体系完善，精准覆盖人工智能各细分领域，便于用户按主题筛选。
*   项目强调“with code”，提供可运行的实际代码而非仅停留在概念层面。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34859 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 描述: Visualizer for neural network, deep learning and machine learning models
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33131 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目为深度学习与机器学习研究人员提供了必备的速查手册集合，内容源自Kailash Ahirwar在Medium上发布的经典指南。它旨在通过简明扼要的参考资料，帮助研究者快速回顾关键概念和代码片段。

2. **核心功能**
*   涵盖机器学习与深度学习领域的核心基础理论与算法速查。
*   集成常用Python科学计算库（如NumPy、SciPy）的关键函数与用法。
*   提供数据可视化库（如Matplotlib）的图表绘制模板与技巧。
*   包含深度学习框架（如Keras）的高阶API使用示例与配置指南。

3. **适用场景**
*   研究人员在快速搭建实验原型时查阅基础数学公式或代码实现。
*   初学者在复习机器学习核心概念及常用数据处理技巧时作为案头参考。
*   工程师在进行模型调试时，快速查找特定库函数或绘图参数的正确用法。

4. **技术亮点**
*   内容高度浓缩，以“速查表”形式呈现，极大提升了信息检索效率。
*   结合了理论笔记与实际代码片段，兼顾学术研究与工程实践需求。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3391 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- ### 1. 中文简介
该项目提供了一份全面的人工智能学习路线图，涵盖从零基础入门到就业实战的全过程，整理了近200个实战案例并免费配套教材。内容广泛涉及Python、数学基础、机器学习、深度学习及自然语言处理等热门技术领域。旨在帮助学习者系统掌握数据科学、计算机视觉及各类主流AI框架的核心技能。

### 2. 核心功能
*   **系统化学习路径**：提供从零开始到专业进阶的完整AI学习路线图。
*   **海量实战资源**：收录近200个真实项目案例，强化动手实践能力。
*   **免费配套教材**：为所有学习阶段和案例提供免费的教学资料支持。
*   **多领域技术覆盖**：包含Python编程、数学基础、数据分析、机器学习及深度学习等核心技术栈。
*   **主流框架支持**：重点讲解PyTorch、TensorFlow、Keras、Caffe等流行AI开发框架。

### 3. 适用场景
*   **零基础转行人员**：希望进入人工智能领域但缺乏背景知识的初学者。
*   **在校学生与求职者**：需要项目经验以增强简历竞争力、寻求AI相关职位的毕业生。
*   **技术提升者**：希望系统化复习或深入掌握特定AI子领域（如NLP、CV）的专业人士。
*   **教育机构与自学者**：寻找结构化课程资源和实战案例进行教学或自我训练的个人及团队。

### 4. 技术亮点
*   **全栈式知识体系**：不仅涵盖应用层框架，还深入底层数学原理与算法逻辑。
*   **开源免费生态**：完全免费开放大量高质量实战案例与配套教材，降低学习门槛。
*   **紧跟技术前沿**：持续更新涵盖TensorFlow 2、PyTorch等当前最主流的开发工具与版本。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2658 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**
Ludwig 是一个低代码框架，旨在简化自定义大语言模型（LLM）、神经网络及其他 AI 模型的构建与训练过程。它通过声明式配置和自动化的机器学习管道，让开发者能够专注于数据而非底层代码细节，从而高效地实现从数据处理到模型部署的全流程。

2. **核心功能**
*   **低代码/声明式接口**：允许用户通过 YAML 配置文件定义模型架构和数据管道，无需编写大量样板代码。
*   **广泛的基础架构支持**：原生支持 PyTorch 等深度学习框架，兼容多种神经网络类型及预训练模型（如 LLaMA、Mistral）。
*   **端到端自动化流程**：内置数据处理、特征工程、模型训练、评估及超参数调优的一站式解决方案。
*   **多模态与领域适配**：不仅限于自然语言处理，还适用于计算机视觉等场景，支持结构化数据与非结构化数据的混合建模。

3. **适用场景**
*   **快速原型开发**：研究人员或工程师希望在不深入底层代码的情况下，快速验证新的机器学习想法或模型架构。
*   **企业级 AI 部署**：需要标准化、可复现且易于维护的机器学习流水线，以便将模型稳定地集成到生产环境中。
*   **传统表格数据建模**：针对结构化数据集进行高效的分类、回归或聚类任务，替代复杂的自定义脚本编写。
*   **LLM 微调与实验**：对开源大语言模型（如 LLaMA 系列）进行高效微调，探索不同提示词工程和参数配置的效果。

4. **技术亮点**
*   **数据中心主义设计**：强调数据质量与预处理的重要性，通过自动化特征提取降低对专家知识的依赖。
*   **高度可扩展性**：模块化设计允许轻松插入自定义组件或扩展支持新的深度学习库和模型类型。
*   **开箱即用的实验管理**：内置日志记录和结果追踪功能，方便对比不同实验配置下的模型性能表现。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11724 | 🍴 1221 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9116 | 🍴 1231 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8908 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8377 | 🍴 1900 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6985 | 🍴 1171 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6184 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- ### 1. 中文简介
该项目是一个涵盖自然语言处理（NLP）各个领域的综合性资源库，集成了敏感词检测、语言识别、实体抽取（手机、身份证、邮箱等）及繁简转换等基础工具。它不仅提供了丰富的中文词库（如人名、地名、行业术语）和情感分析数据，还收录了大量关于预训练模型（BERT、GPT等）、知识图谱构建、语音识别及对话系统的开源项目与学术资料。旨在为开发者提供从数据预处理、模型训练到垂直领域应用的全栈式NLP解决方案参考。

### 2. 核心功能
*   **基础NLP工具与数据处理**：提供敏感词过滤、中英文混合检测、手机/电话归属地查询、命名实体识别（手机号、身份证、邮箱抽取）及繁简字体转换等实用脚本。
*   **丰富语料库与词典资源**：内置中日文人名库、中文缩写库、各领域专用词库（汽车、医疗、法律、金融等）、情感词典、停用词表及同/反义词库，支持细粒度的文本挖掘。
*   **前沿模型与预训练资源**：汇总了BERT、ERNIE、RoBERTa、ELECTRA等主流预训练语言模型的中文版本、微调代码及应用案例，涵盖文本分类、序列标注及生成式任务。
*   **知识图谱与问答系统**：提供知识图谱构建工具（如XLORE）、实体链接、关系抽取方法及基于知识图谱的问答系统（KBQA）开源项目，支持结构化数据的智能化处理。
*   **语音处理与多模态技术**：包含中文语音识别（ASR）数据集、发音字典、声纹迁移、OCR文字识别工具以及结合视觉与文本的多模态NLP资源。

### 3. 适用场景
*   **智能客服与聊天机器人开发**：利用其中的对话语料、意图识别模型及多轮对话框架，快速搭建具备语义理解能力的客服系统或娱乐型聊天机器人。
*   **文本安全与内容审核**：通过集成敏感词库、暴恐词表及反动词表，应用于社交媒体、论坛或新闻平台的自动化内容过滤与合规性审查。
*   **垂直领域数据分析**：借助医疗、金融、法律等领域的专用词库和NER工具，对企业内部文档、行业报告进行实体提取、情感分析及知识沉淀。
*   **NLP算法研究与教学**：作为研究人员或学生的参考资料，快速获取最新的NLP论文解读、基准测试数据集（CLUE/CUGE）及各类算法的代码实现。

### 4. 技术亮点
*   **全面性与系统性**：不仅包含代码工具，还整合了数据集、论文解读、课程资源及行业报告，形成了完整的NLP学习与应用生态。
*   **本土化深度优化**：针对中文特有的难点（如分词、繁简转换、拼音标注、中文数字处理）提供了大量高质量的开源工具和词典，极大降低了中文NLP的开发门槛。
*   **紧跟技术前沿**：持续更新主流预训练模型（如BERT系列、Transformer架构）的最新应用案例及微调技巧，确保用户能接触到业界先进的解决方案。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81442 | 🍴 15245 | 语言: Python

### LlamaFactory
- ### 1. 中文简介
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过 100 种主流模型。该项目旨在简化从指令微调到强化学习对齐的全流程开发，已被 ACL 2024 收录。它通过整合多种前沿技术，为用户提供了一站式模型优化解决方案。

### 2. 核心功能
- **多模型支持**：兼容 LLaMA、Qwen、Gemma、DeepSeek 等 100 多种 LLM 和 VLM 架构。
- **多样化微调方法**：内置 LoRA、QLoRA、P-Tuning 等高效参数微调（PEFT）及全量微调策略。
- **强化学习对齐**：原生支持 RLHF（基于人类反馈的强化学习）、DPO 等高级对齐算法。
- **量化部署集成**：支持 QLoRA 等低比特量化技术，降低显存占用并加速推理。
- **统一训练接口**：提供标准化的 API 和配置方式，简化从数据准备到模型评估的流程。

### 3. 适用场景
- **快速原型开发**：研究人员或开发者希望快速验证不同基座模型在特定任务上的表现。
- **资源受限环境**：在显存有限的消费级 GPU 上，通过 QLoRA 等技术对大模型进行高效微调。
- **企业级应用定制**：针对垂直领域数据，利用 RLHF/DPO 对齐模型输出，提升业务场景下的准确率。
- **多模态研究**：需要同时处理文本与图像数据的视觉语言模型微调与研究。

### 4. 技术亮点
- **极致易用性**：无需编写复杂代码，通过 YAML/JSON 配置文件即可启动训练，大幅降低使用门槛。
- **学术前沿集成**：紧跟 NLP 领域最新进展，第一时间支持 SOTA 模型及微调算法。
- **高性能优化**：底层经过深度优化，显著减少训练时间并提高硬件利用率。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72486 | 🍴 8863 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 描述: 12 Weeks, 24 Lessons, AI for All!
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48440 | 🍴 10049 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并提取了包括 Anthropic、OpenAI、Google 及 xAI 在内的多家主流厂商最新模型的系统提示词（System Prompts），涵盖 Claude、GPT、Gemini 等多个系列。内容定期更新，旨在为研究人员和开发者提供这些闭源大模型内部指令的透明化参考。

2. **核心功能**
*   **多厂商数据聚合**：整合了 Anthropic、OpenAI、Google 和 xAI 等头部科技公司的系统提示词数据。
*   **覆盖主流模型**：包含 Claude Fable/Opus、ChatGPT/GPT-5.5/Codex、Gemini 系列以及 Grok、Cursor 等知名 AI 产品。
*   **定期动态更新**：保持对最新模型版本及其对应系统提示词的持续追踪与收录。
*   **开源共享资源**：以开源形式提供数据，降低用户获取底层模型指令信息的门槛。

3. **适用场景**
*   **提示词工程研究**：分析大厂模型的底层逻辑和约束条件，优化自身的 Prompt 设计策略。
*   **竞品分析与教育**：通过对比不同厂商模型的内部指令差异，进行 AI 技术教学或市场竞品分析。
*   **安全审计与测试**：作为红队测试或安全研究的参考基准，评估模型在特定指令下的行为边界。

4. **技术亮点**
*   直接获取高价值的“黑盒”内部指令，为理解大模型行为模式提供了稀缺的一手资料。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 45960 | 🍴 7536 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- 1. **中文简介**
AiLearning 是一个涵盖数据分析与机器学习实战的综合学习资源库，深入讲解线性代数、PyTorch 及 TensorFlow 2 等核心技术。该项目结合 NLTK 自然语言处理工具，旨在为学习者提供从理论基础到代码实现的完整知识体系。

2. **核心功能**
*   集成经典机器学习算法（如 SVM、KMeans、Adaboost）与深度学习模型（如 LSTM、RNN、DNN）的代码实现。
*   包含推荐系统（基于 Apriori、FP-Growth）及自然语言处理（NLP）的实战案例。
*   提供线性代数等数学基础知识的梳理，辅助理解算法背后的原理。
*   支持主流框架 PyTorch 和 TensorFlow 2 的学习与应用。

3. **适用场景**
*   希望系统掌握机器学习理论并付诸实践的初学者或进阶开发者。
*   需要参考经典算法（如回归、分类、聚类）具体代码实现的工程人员。
*   专注于自然语言处理（NLP）或推荐系统领域开发的科研人员。

4. **技术亮点**
*   知识图谱全面，串联了数学基础、传统机器学习、深度学习及 NLP 四大板块。
*   广泛使用 scikit-learn 等成熟库，提供了大量可直接运行的标杆代码。
*   紧跟技术潮流，同时覆盖 TF2 和 PyTorch 两大主流深度学习框架。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42350 | 🍴 11541 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36325 | 🍴 5956 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34859 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33698 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28178 | 🍴 3421 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25719 | 🍴 2882 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。它提供了丰富的实战案例，涵盖了从基础算法到前沿应用的广泛领域。这是一个旨在帮助开发者快速学习和实践人工智能技术的综合性资源库。

2. **核心功能**
*   收录500个涵盖机器学习、深度学习、NLP和计算机视觉的完整项目代码。
*   提供多领域（如CV、NLP）的具体实现示例，便于直接运行和学习。
*   作为“Awesome”列表， curated（精选）高质量且实用的AI开源项目。
*   支持Python等主流语言的项目源码下载，降低入门门槛。
*   分类清晰，方便用户根据特定技术领域快速查找相关案例。

3. **适用场景**
*   AI初学者希望快速通过实际代码理解机器学习概念和流程。
*   开发者需要寻找特定任务（如图像识别、文本分类）的参考实现以加速项目开发。
*   学生或研究人员用于复现经典算法或对比不同模型的实现效果。
*   技术面试官寻找多样化的项目案例来评估候选人的实战能力。

4. **技术亮点**
*   **规模庞大**：汇集500个项目，覆盖AI主要子领域的广泛应用场景。
*   **全栈覆盖**：同时包含传统机器学习、深度学习以及NLP和计算机视觉等热门方向。
*   **即插即用**：提供完整代码，便于用户直接克隆、运行和修改，无需从零搭建环境。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34859 | 🍴 7290 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- **1. 中文简介**
Skyvern 是一款利用人工智能自动化浏览器工作流的工具。它通过集成大语言模型（LLM）和计算机视觉技术，能够理解并执行复杂的网页操作任务。该项目旨在提供一种比传统自动化工具更智能、更灵活的 RPA（机器人流程自动化）解决方案。

**2. 核心功能**
*   **AI 驱动的工作流自动化**：结合 LLM 与视觉能力，自主解析页面结构并规划操作步骤。
*   **多浏览器引擎支持**：底层兼容 Playwright、Puppeteer 和 Selenium，适应不同自动化需求。
*   **通用 API 接口**：提供标准化的 API，便于集成到现有系统或与其他 RPA 平台（如 Power Automate）协作。
*   **视觉感知与交互**：能够识别网页元素的外观而非仅依赖 DOM 结构，提高对动态页面的适应性。
*   **端到端任务执行**：从登录、数据填写到信息提取，实现全流程的无人值守自动化。

**3. 适用场景**
*   **跨平台数据录入**：自动在多个不同的 Web 应用程序中填写表单或输入数据。
*   **网页数据抓取与监控**：定期访问特定网站，提取结构化数据或监控价格、库存等变化。
*   **企业级 RPA 增强**：作为传统 RPA 工具的补充，处理那些规则固定但界面复杂或经常变动的任务。
*   **个人效率提升**：自动化重复性的日常浏览任务，如自动预订、比价或报告生成。

**4. 技术亮点**
*   **混合智能架构**：巧妙融合了自然语言处理（LLM）的推理能力和计算机视觉（Vision）的感知能力，突破了传统基于 CSS/XPath 选择器的自动化局限。
*   **高鲁棒性**：即使网页布局发生微小变动，AI 也能通过视觉特征准确定位目标元素，减少了脚本维护成本。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22001 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- **1. 中文简介**
计算机视觉标注工具（CVAT）是构建高质量视觉数据集的领先平台，提供开源、云端及企业级产品。它支持图像、视频和3D数据的AI辅助标注、质量保障及团队协作等功能。

**2. 核心功能**
*   支持图像、视频及3D数据的多模态标注与AI辅助标注。
*   提供开源、云服务和企业版多种部署形态及专业标注服务。
*   内置质量保证机制、团队协作者管理分析及开发者API接口。

**3. 适用场景**
*   为计算机视觉模型训练构建大规模高质量标注数据集。
*   深度学习项目中对图像分类、目标检测或语义分割数据进行预处理。
*   企业团队需要协同完成复杂视频或3D点云的标注任务。

**4. 技术亮点**
*   原生集成PyTorch和TensorFlow生态，兼容ImageNet等主流标准。
*   具备强大的AI辅助标注能力，显著提升图像与视频的处理效率。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16142 | 🍴 3721 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**
该项目是一个先进的计算机视觉可解释性AI工具库，旨在帮助用户理解深度学习模型的决策依据。它广泛支持CNN、Vision Transformers等多种架构，涵盖分类、检测、分割及图像相似度等多种任务。

2. **核心功能**
*   支持多种主流模型架构，包括卷积神经网络（CNN）和视觉Transformer（ViT）。
*   兼容多种计算机视觉任务，如图像分类、目标检测、语义分割等。
*   提供丰富的可视化方法，涵盖Grad-CAM、Score-CAM以及类激活映射（CAM）等技术。
*   具备高度的可扩展性，能够适配图像相似度计算及其他自定义解释需求。

3. **适用场景**
*   **医疗影像分析**：辅助医生定位病灶区域，解释AI诊断结果以提高信任度。
*   **自动驾驶系统调试**：可视化车辆识别模块的关注点，验证模型是否关注关键交通要素。
*   **学术研究与教学**：直观展示深度学习模型内部机制，用于解释性人工智能（XAI）的教学演示。
*   **合规性审计**：在金融或安防领域，提供模型决策依据以满足监管对算法透明度的要求。

4. **技术亮点**
*   **多架构兼容性**：无缝支持从传统CNN到前沿Vision Transformer的多种骨干网络。
*   **全面的方法论覆盖**：集成了Grad-CAM及其改进变体（如Score-CAM），满足不同的精度与速度需求。
*   **高社区认可度**：拥有近1.3万星标，证明其在可解释AI领域的广泛采用和技术成熟度。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12891 | 🍴 1708 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. 中文简介
Kornia 是一个专为空间人工智能（Spatial AI）设计的几何计算机视觉库，基于 PyTorch 构建。它提供了可微分的图像处理原语和几何计算工具，旨在加速深度学习在计算机视觉领域的研发与部署。

### 2. 核心功能
*   **可微分图像处理**：提供完全可微分的传统图像操作（如旋转、裁剪、色彩空间转换），便于集成到神经网络中。
*   **几何计算机视觉**：内置相机校准、立体匹配、单目深度估计及机器人运动学等几何算法模块。
*   **PyTorch 原生支持**：作为 PyTorch 的一等公民，直接利用 GPU 加速计算，并与现有深度学习工作流无缝兼容。
*   **模块化架构**：将复杂的视觉任务拆解为独立的张量操作，方便研究人员快速构建和测试新模型。

### 3. 适用场景
*   **自动驾驶与机器人导航**：用于实时处理传感器数据，进行环境感知和位姿估计。
*   **工业缺陷检测**：利用可微分预处理提升图像质量，辅助下游分类或分割模型的精度。
*   **学术研究与原型开发**：快速验证涉及几何约束或图像增强的新型深度学习架构。

### 4. 技术亮点
*   **可微分管线（Differentiable Pipeline）**：允许反向传播通过整个图像处理流程，实现了“端到端”的可学习视觉系统。
*   **高性能 CUDA 实现**：底层算子经过高度优化，充分利用 NVIDIA GPU 并行计算能力，显著提升处理速度。
- 链接: https://github.com/kornia/kornia
- ⭐ 11250 | 🍴 1190 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8870 | 🍴 2192 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3451 | 🍴 874 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3252 | 🍴 397 | 语言: Python
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
- 1. **中文简介**
OpenClaw 是一款支持任意操作系统和平台的个人 AI 助手，旨在让用户以“龙虾方式”完全掌控自己的数据。它强调本地化部署与隐私保护，确保用户拥有数据的自主权。

2. **核心功能**
*   跨平台兼容，支持在任意操作系统上运行。
*   提供个人化的 AI 助理服务，满足多样化需求。
*   坚持“拥有自己的数据”理念，注重隐私与数据安全。
*   基于 TypeScript 开发，具备良好的扩展性与维护性。

3. **适用场景**
*   开发者希望在不依赖云端服务的情况下，部署私有的 AI 助手。
*   重视数据隐私的个人用户，用于日常任务自动化与信息处理。
*   需要在任意操作系统（如 Linux、Windows、macOS）上集成 AI 能力的企业或个人环境。

4. **技术亮点**
*   采用 TypeScript 编写，代码结构清晰且类型安全。
*   设计轻量级架构，适配多种运行环境，降低部署门槛。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380403 | 🍴 79679 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的代理式技能框架与软件开发方法论。它通过子代理驱动开发模式，提供了一套切实可行的 AI 辅助编程工作流。该项目旨在提升软件开发生命周期（SDLC）中的效率与智能化水平。

2. **核心功能**
*   支持基于子代理驱动的开发（Subagent-driven Development），实现任务自动化分解。
*   提供专门的“代理技能”框架，规范 AI 在编码和调试中的行为模式。
*   集成头脑风暴与需求分析工具，辅助早期阶段的功能构思。
*   覆盖完整的软件开发生命周期（SDLC），从设计到代码生成的一站式支持。

3. **适用场景**
*   希望利用 AI 自动执行重复性编码任务以提高开发效率的团队。
*   需要结构化方法指导 AI 进行复杂系统设计与模块拆分的工程师。
*   在头脑风暴阶段寻求 AI 协助以快速生成创意方案的产品经理或开发者。
*   试图标准化内部 AI 编程实践并建立统一技能库的组织。

4. **技术亮点**
*   采用 Shell 脚本实现，轻量级且易于集成到现有 CI/CD 流程中。
*   强调“技能（Skills）”的可复用性，允许用户自定义和共享代理行为模块。
*   独特的“Obra”方法论标签，暗示其具备严谨的工程化思维而非单纯的代码补全。
- 链接: https://github.com/obra/superpowers
- ⭐ 238395 | 🍴 21140 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 描述: The agent that grows with you
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 202752 | 🍴 36240 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 描述: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194022 | 🍴 58830 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 描述: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185155 | 🍴 46129 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164337 | 🍴 21282 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163882 | 🍴 30362 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156614 | 🍴 46146 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150072 | 🍴 9335 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146545 | 🍴 23060 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

