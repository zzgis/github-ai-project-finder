# GitHub AI项目每日发现报告
日期: 2026-06-26

## 新发布的AI项目

### theeleven
- 1. **中文简介**
该项目在 X Layer 上部署了 11 个自主 AI 代理，用于开启实时足球预测市场。它结合了定制的 Uniswap V4 Hook 和无 Gas 费的 USDT0 质押机制，实现了去中心化的体育博彩体验。

2. **核心功能**
*   **自主 AI 代理群**：利用 11 个独立的 AI 代理自动管理足球预测市场的运营。
*   **Uniswap V4 定制 Hook**：通过自定义 Hook 深度集成 Uniswap V4 协议以支持特定业务逻辑。
*   **无 Gas 费体验**：采用 EIP-3009 等技术实现 USDT0 质押时的 Gas 费豁免，降低用户门槛。
*   **实时足球数据集成**：专注于足球领域的实时投注（Prop Markets）数据处理与结算。

3. **适用场景**
*   **去中心化体育博彩平台**：开发者可基于此构建无需中介的足球赛事预测与交易平台。
*   **Web3 游戏化应用**：结合 AI 代理与实时数据，打造具有互动性的链上体育游戏。
*   **DeFi 创新实验**：测试 Uniswap V4 Hook 与 EIP-3009 跨链/无感签名在复杂金融场景中的应用。

4. **技术亮点**
*   **多技术栈融合**：同时运用 Foundry、Solidity（智能合约）、Next.js（前端）和 TypeScript（代理逻辑）。
*   **前沿协议支持**：深度集成 Uniswap V4、EIP-3009 及 ERC-8257 等最新 Web3 标准。
*   **MCP 架构**：可能采用了 Model Context Protocol (MCP) 来标准化 AI 代理与外部数据源的交互。
- 链接: https://github.com/winsznx/theeleven
- ⭐ 419 | 🍴 0 | 语言: TypeScript
- 标签: ai-agents, defi, eip-3009, erc-8257, football

### video-production-skills
- 1. **中文简介**
这是一个可复用的 AI 视频制作技能库，旨在通过人工智能技术简化视频创作流程。它涵盖了从基础生成、动作设计到开场动画及质量检查的全方位功能模块。该项目为开发者提供了一套标准化的工具集，以提升视频生产的效率与一致性。

2. **核心功能**
*   支持基于 AI 的视频内容自动生成与重建。
*   内置专业的运动图形（Motion Design）处理技能。
*   提供多样化的视频开场动画（Openers）制作能力。
*   集成自动化视频质量 QA 检查机制。
*   采用模块化设计，确保各技能可复用且易于集成。

3. **适用场景**
*   需要批量生成营销短视频或社交媒体素材的媒体团队。
*   希望集成 AI 视频编辑功能的应用程序开发者。
*   追求高效工作流并需标准化视频输出质量的制作公司。
*   利用自动化脚本进行视频后期质检和内容复核的场景。

4. **技术亮点**
*   专为 Python 环境优化的模块化技能架构，便于扩展和维护。
*   聚焦于“可复用性”设计，降低重复开发成本。
*   涵盖从创作到质检的完整视频生产闭环。
- 链接: https://github.com/Pluviobyte/video-production-skills
- ⭐ 163 | 🍴 17 | 语言: Python

### GITVERSE
- **1. 中文简介**
GITVERSE 是一个逆向工程工具，能将任何代码库转化为构建提示词，提供架构拆解、ASCII 蓝图及面向 AI 的重构提示。它旨在帮助开发者快速理解现有项目结构，并生成可供大语言模型（LLM）直接使用的标准化描述，从而加速代码迁移、重构或自动化构建流程。

**2. 核心功能**
*   **代码库逆向分析**：自动解析代码结构，生成可视化的 ASCII 架构图和详细的架构拆解报告。
*   **AI 就绪提示生成**：将分析结果转化为标准化的 Prompt，可直接用于 Claude、OpenAI 等 LLM 进行代码重建或修改。
*   **多平台集成支持**：原生支持 GitHub API，便于直接从仓库拉取数据进行分析，无缝接入 Cursor 等 AI 编辑器。
*   **现代化 Web 界面**：基于 Next.js 和 TailwindCSS 构建，提供直观的用户交互体验，方便查看和分析生成的蓝图。

**3. 适用场景**
*   **遗留系统现代化**：在重构老旧代码库前，先通过 GITVERSE 生成清晰的架构蓝图，以便 AI 辅助编写新代码。
*   **跨团队知识转移**：当新成员接手陌生项目时，利用生成的 ASCII 蓝图和 Prompt 快速理解项目整体结构和依赖关系。
*   **AI 辅助开发工作流**：在 Cursor 或 VS Code 中使用 AI 编码助手时，先用 GITVERSE 生成精确的项目上下文 Prompt，提高 AI 回答的准确性。

**4. 技术亮点**
*   **全栈 TypeScript 实现**：前端采用 Next.js + TailwindCSS，后端逻辑清晰，确保类型安全和开发效率。
*   **提示工程优化**：专注于生成“AI 可读”的高质量 Prompt，解决了直接将代码库扔给 LLM 时上下文混乱的问题。
*   **开源生态整合**：紧密围绕 GitHub API 和主流 LLM（如 Claude、GPT）设计，是 Developer Tools 领域的一个实用补充。
- 链接: https://github.com/GraeLefix/GITVERSE
- ⭐ 131 | 🍴 1 | 语言: TypeScript
- 标签: ai, build-prompt, claude, code-analysis, codebase-analysis

### Anti-Autoresearch
- 1. **中文简介**
不要轻信自动生成的研究论文表面价值，该项目提供审稿人视角的完整性取证，通过检测39种黑客模式中的自洽性和伪造内容给出确定性结论。它并非AI文本检测器，而是ARIS系统的对偶工具。

2. **核心功能**
*   基于39种黑客模式（涵盖7大类别）进行细粒度的内容伪造检测。
*   执行严格的自洽性检查，识别论文内部逻辑矛盾。
*   提供确定性的判决结果，而非概率性的AI文本识别。
*   专为审稿人设计，作为ARIS系统的补充工具以增强审查能力。

3. **适用场景**
*   学术出版过程中对疑似由LLM代理生成的论文进行真实性审查。
*   研究人员在同行评审阶段快速验证投稿论文的完整性与一致性。
*   机构用于建立针对自动化科研（Autoresearch）内容的防御和筛查机制。

4. **技术亮点**
*   采用“双证”方法，结合自洽性分析与特定攻击模式的伪造检测。
*   输出确定性裁决，避免了传统AI检测器常见的模糊概率判断。
*   聚焦于“黑客模式”而非通用的语言风格，更精准地针对自动化生成的特定缺陷。
- 链接: https://github.com/wanshuiyin/Anti-Autoresearch
- ⭐ 32 | 🍴 1 | 语言: Python
- 标签: ai-generated-content, ai-scientist, autoresearch, forensics, llm-agents

### macos-chatgpt-overlay-bar
- 1. **中文简介**
这是一款专为 macOS 设计的 ChatGPT 辅助工具，它常驻于系统菜单栏，无需切换窗口即可快速调用 AI 服务。该项目旨在为用户提供一种轻量级、无干扰的即时交互体验，让 AI 助手融入日常桌面操作流中。

2. **核心功能**
*   **菜单栏常驻**：应用图标固定在 macOS 菜单栏，实现后台静默运行与快速唤起。
*   **即时访问**：通过快捷键或点击菜单直接发起对话，避免频繁切换应用程序窗口。
*   **轻量级集成**：作为状态栏应用（Statusbar App），占用系统资源极少，保持桌面整洁。
*   **快速复制/分享**：支持快速复制生成的回复内容或一键分享对话结果。

3. **适用场景**
*   **碎片化问答**：在浏览网页或处理文档时，快速查询事实性知识或翻译短句。
*   **多任务工作流**：在不打断当前主要工作软件（如代码编辑器、文字处理器）的情况下获取灵感或摘要。
*   **即时辅助创作**：在写作或编程过程中，随时调取 AI 建议而不必离开当前编辑界面。

4. **技术亮点**
*   该项目标注编程语言为 "None"，表明其可能是一个封装好的二进制应用或基于特定框架（如 Electron、Swift 等）编译的成品，侧重于开箱即用的用户体验而非源码二次开发。
*   利用 macOS 原生菜单栏 API 实现极致的系统集成感，提供比 Web 版更低的延迟和更高的操作便捷性。
- 链接: https://github.com/ik190/macos-chatgpt-overlay-bar
- ⭐ 31 | 🍴 3 | 语言: 未知
- 标签: ai, chatgpt, chatgpt-bar-mac, chatgpt-menubar-mac, chatgpt-quick-access-mac

### auto-paper-collecter
- 描述: 📚🔭 Your personal research radar — an LLM-powered tool that auto-aggregates the latest papers for your keywords across arXiv / Crossref / Semantic Scholar / GitHub / RSS.
- 链接: https://github.com/PenghaoJiang/auto-paper-collecter
- ⭐ 31 | 🍴 1 | 语言: Python
- 标签: academic, agent-skill, ai, arxiv, claude-code

### parsehawk
- 描述: Local-first document AI. Run 100% locally by default, with API, CLI, and Web UI.
- 链接: https://github.com/parsehawk/parsehawk
- ⭐ 25 | 🍴 4 | 语言: Python
- 标签: artificial-intelligence, classification, document-ai, document-processing, extraction

### ai-coding-deals
- 描述: Money-saving guide to AI coding tools: free tiers, discounts, referral credits & open-source alternatives. 省钱指南。
- 链接: https://github.com/codertesla/ai-coding-deals
- ⭐ 25 | 🍴 0 | 语言: Python
- 标签: ai, ai-coding, ai-tools, awesome-list, claude-code

### oil-cover
- 描述: 为小红书 AI 工具实操内容生成稳定、干净、精致封面的 Claude / Codex Skill（脚本模式 + Agent 自主执行）
- 链接: https://github.com/oil-oil/oil-cover
- ⭐ 23 | 🍴 3 | 语言: Python

### Personal-Comparative-Advantage-Engine-PCAE
- 描述: Personal Comparative Advantage Engine - A Claude Code Skill to discover your unique advantages in the AI era | AI时代个人优势发现引擎
- 链接: https://github.com/KeGong-XKK/Personal-Comparative-Advantage-Engine-PCAE
- ⭐ 20 | 🍴 0 | 语言: 未知

## 热门AI项目

## Machine Learning项目

### funNLP
- 描述: 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphrase)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cnocr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(ASR)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GPT2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQACorpus - 580万百度知道问答数据挖掘项目、brat rapid annotation tool: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. 英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAMELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注工具 、aili - the fastest in-memory index in the East 东半球最快并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datasets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHub Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextCluster：短文本聚类预处理模块 Short text cluster、面向语音识别的中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、MedQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和浮点数、Transfer Learning in Natural Language Processing (NLP) 、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Classificatin)、文本生成(Text Generation)、文本相似性(Text Similarity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoST：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具 - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - 中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、medical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLaia：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架、中文关键短语抽取工具
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉及自然语言处理项目的代码合集。它涵盖了从基础算法到前沿应用的广泛主题，并为每个项目提供了可运行的源代码。作为一个“Awesome List”风格的资源库，它为学习者提供了丰富的实践案例。

2. **核心功能**
*   提供涵盖AI各主要子领域的数百个完整项目代码示例。
*   支持多种热门技术栈，包括机器学习、深度学习和自然语言处理等。
*   专注于计算机视觉和NLP等特定领域的实战应用开发。
*   作为开源资源库，方便用户直接克隆和运行代码进行实验。
*   分类清晰，便于快速定位特定方向的学习资料。

3. **适用场景**
*   AI初学者希望通过大量实例快速掌握机器学习与深度学习的基本概念。
*   研究人员或工程师需要寻找特定领域（如CV或NLP）的代码模板以加速原型开发。
*   教育者用于课堂教学，展示理论算法在实际项目中的具体实现。
*   数据科学家希望扩展技能树，探索不同AI应用场景下的最佳实践。

4. **技术亮点**
*   **规模宏大**：包含多达500个项目，覆盖面极广，是极其丰富的学习资源库。
*   **全栈覆盖**：整合了从传统机器学习到现代深度学习及大模型应用的完整技术链路。
*   **代码导向**：强调“with code”，所有项目均附带可直接执行的源代码，注重实践性。
*   **社区精选**：作为Awesome列表的一部分，通常意味着经过社区筛选的高质量内容集合。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34924 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**
Netron 是一款用于可视化神经网络、深度学习及机器学习模型的强大工具。它支持多种主流框架和文件格式，帮助用户直观地查看模型结构和数据流。该工具界面友好，能够显著提升模型调试和分析的效率。

2. **核心功能**
*   支持广泛的主流框架（如 PyTorch、TensorFlow、Keras、ONNX、CoreML 等）及多种模型格式。
*   提供交互式图形界面，清晰展示神经网络的层级结构与连接关系。
*   允许用户查看节点属性、权重数据及张量形状，便于深入理解模型内部细节。
*   兼容桌面应用、Web 浏览器及命令行工具，实现跨平台便捷访问。

3. **适用场景**
*   **模型调试与验证**：开发者在训练或转换模型后，快速检查网络结构是否符合预期。
*   **论文复现与学习**：研究人员通过可视化他人发布的模型结构，深入理解算法设计逻辑。
*   **多格式转换检查**：在将模型从一种框架（如 PyTorch）转换为另一种格式（如 ONNX）时，确保结构完整性。

4. **技术亮点**
*   **极高的兼容性**：支持数十种不同的框架和文件格式，是业界通用的模型可视化工具。
*   **开源与轻量级**：基于 JavaScript 开发，无需安装大型依赖即可运行，且完全免费开源。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33138 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- 1. **中文简介**：ONNX 是用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型交换与运行。它允许开发者在不同平台间无缝迁移模型，无需重新训练或重构代码。

2. **核心功能**：
   - 定义开放标准的神经网络图结构，支持跨框架模型表示。
   - 提供工具链以转换主流框架（如 PyTorch、TensorFlow）的模型至 ONNX 格式。
   - 支持在多种硬件加速器和运行时环境中高效执行推理。
   - 确保模型在不同供应商实现间的兼容性和可移植性。

3. **适用场景**：
   - 需要在不同深度学习框架之间迁移模型架构时。
   - 在特定硬件设备（如嵌入式系统、GPU集群）上优化模型部署时。
   - 构建跨平台机器学习服务以统一后端推理引擎时。

4. **技术亮点**：作为行业通用的中间表示格式，ONNX 打破了框架壁垒，显著降低了模型部署的复杂性和成本。
- 链接: https://github.com/onnx/onnx
- ⭐ 21051 | 🍴 3953 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**
《机器学习工程开源书》是一部全面涵盖机器学习工程实践的指南。它深入讲解了从模型训练、调试到大规模部署和推理优化的全流程关键技术。该项目旨在为从业者提供可扩展的高性能AI系统构建方案。

2. **核心功能**
*   提供基于PyTorch的大规模分布式训练最佳实践与调优策略。
*   详解LLM（大语言模型）的高效推理加速、量化及显存优化技术。
*   涵盖硬件基础设施配置，包括GPU集群管理、存储IO优化及网络通信。
*   介绍MLOps工作流，包括实验追踪、模型版本管理及自动化部署流程。
*   针对SLURM等高性能计算调度系统的资源管理与作业提交指南。

3. **适用场景**
*   需要从零搭建或优化大规模深度学习集群的工程团队。
*   致力于降低大语言模型（LLM）训练成本并提升训练稳定性的研究人员。
*   寻求在生产环境中实现高吞吐、低延迟AI服务推理的后端工程师。
*   希望系统化掌握MLOps全链路落地经验的机器学习从业者。

4. **技术亮点**
*   内容紧跟前沿，特别针对Transformer架构和大模型时代的基础设施挑战进行了深度解析。
*   结合理论与实践，提供了大量关于GPU利用率最大化及故障调试的具体代码示例与配置建议。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18177 | 🍴 1153 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17256 | 🍴 2108 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11528 | 🍴 903 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10642 | 🍴 5710 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- **中文简介**
该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和NLP项目的代码合集，旨在为开发者提供丰富的实战案例。它汇集了涵盖人工智能各个主要领域的完整项目资源，方便用户直接参考和学习。作为一个综合性的开源库，它提供了从基础到高级算法的代码实现。

**核心功能**
1. 提供500个完整的AI相关项目代码，覆盖机器学习、深度学习及自然语言处理等核心领域。
2. 集成计算机视觉项目，展示图像识别、目标检测等具体应用场景的代码实现。
3. 包含大量标注清晰的子项目，如“awesome”列表所示，便于快速定位特定技术栈的资源。
4. 所有项目均附带源代码，支持用户直接运行、修改和研究底层算法逻辑。

**适用场景**
1. **AI初学者入门学习**：通过阅读和运行精选的500个项目代码，快速掌握机器学习与深度学习的基础概念。
2. **研究人员获取灵感**：在计算机视觉或NLP领域进行课题探索时，参考现有项目结构以寻找新的解题思路。
3. **企业级项目原型开发**：利用现成的代码模块快速构建AI应用的原型，加速从概念验证到实际部署的过程。

**技术亮点**
该项目最大的亮点在于其极高的内容覆盖面和资源整合度，将分散的AI领域知识（ML/DL/CV/NLP）集中在一个仓库中，并标记为“awesome”，极大降低了开发者查找高质量开源案例的时间成本。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34924 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- ### 1. 中文简介
Netron 是一款专为神经网络、深度学习及机器学习模型设计的可视化查看器。它支持多种主流框架生成的模型文件，允许用户直观地浏览和分析模型结构与数据流向。该项目旨在为研究人员和开发者提供一个轻量级且高效的模型调试与展示工具。

### 2. 核心功能
*   **多格式广泛支持**：原生支持 ONNX、TensorFlow、Keras、PyTorch、CoreML、TFLite、safetensors 等数十种模型格式。
*   **交互式可视化**：提供清晰的层级视图和数据流图，支持缩放、平移及节点详情查看。
*   **跨平台运行**：作为独立桌面应用或浏览器扩展运行，无需安装复杂的依赖环境即可打开模型。
*   **模型结构解析**：能够自动解析并展示模型的输入输出形状、参数权重及计算图逻辑。

### 3. 适用场景
*   **模型调试与验证**：开发者在训练完成后，快速检查模型架构是否符合预期，排查结构错误。
*   **论文复现与交流**：研究人员在撰写论文或演示时，生成高质量的模型结构图以辅助说明算法原理。
*   **多框架迁移检查**：当模型从 PyTorch 转换为 TensorFlow 或 ONNX 时，用于对比验证转换前后的结构一致性。
*   **黑盒模型理解**：分析由第三方提供的预训练模型，快速了解其输入输出定义及内部组件组成。

### 4. 技术亮点
*   **零依赖轻量级**：基于 JavaScript 构建，无需配置 Python 环境或 GPU 驱动即可离线查看大型模型。
*   **实时交互体验**：相比静态图片生成工具，Netron 提供了动态探索模型细节的能力，极大提升了分析效率。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33138 | 🍴 3139 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**
该项目汇集了深度学习与机器学习研究人员必备的核心速查表（Cheat Sheets）。内容源自Kailash Ahirwar在Medium上发布的经典文章，旨在为研究者提供高效的技术参考。

2. **核心功能**
*   提供深度学习、机器学习的核心概念速查指南。
*   涵盖Keras、NumPy、SciPy等常用库的关键用法。
*   包含Matplotlib数据可视化的基础代码示例。
*   以简洁的文档形式呈现复杂算法的逻辑结构。

3. **适用场景**
*   机器学习初学者快速回顾核心术语与流程。
*   研究人员在进行模型调试时查找特定库的API用法。
*   准备技术面试或考试时的知识点梳理。
*   撰写论文或报告时快速引用标准方法论。

4. **技术亮点**
*   内容高度浓缩，去除了冗余解释，专注于核心代码与逻辑。
*   覆盖主流AI框架，具有极高的实用参考价值。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15412 | 🍴 3392 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13088 | 🍴 2659 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 描述: Low-code framework for building custom LLMs, neural networks, and other AI models
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11725 | 🍴 1220 | 语言: Python
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
- ⭐ 6190 | 🍴 723 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- **1. 中文简介**
funNLP 是一个功能全面的中文自然语言处理工具箱，集成了敏感词检测、实体抽取（如姓名、电话、身份证）、情感分析及大量垂直领域词库。它旨在为开发者提供从基础文本清洗到高级知识图谱构建的一站式解决方案，特别适用于需要处理中文复杂语义的场景。该项目还收录了大量开源数据集、预训练模型及前沿技术报告。

**2. 核心功能**
*   **基础NLP工具**：提供中英文敏感词过滤、繁简转换、中文分词加速（jieba_fast）、标点修复及文本规范化处理。
*   **实体与信息抽取**：支持手机号、身份证、邮箱、人名（含中日文）、地名等实体信息的自动抽取，以及基于BERT等模型的命名实体识别（NER）。
*   **词库与资源集成**：内置庞大的垂直领域词库（如汽车、医疗、法律、古诗词）及情感分析、同义词、反义词库，并整合了多种预训练语言模型（BERT, ALBERT, GPT2等）。
*   **知识图谱与问答**：提供知识图谱构建工具、实体链接、关系抽取及基于检索或生成的问答系统资源。
*   **数据增强与评估**：包含文本数据增强工具（EDA）、相似度计算、可读性评价及多种NLP基准任务测评集。

**3. 适用场景**
*   **内容安全审核**：用于社交媒体、论坛或APP的内容过滤，快速识别敏感词、暴恐信息及恶意言论。
*   **智能客服与对话系统**：利用其中的对话语料、意图识别工具及预训练模型，快速搭建具备上下文理解能力的中文聊天机器人。
*   **垂直行业数据分析**：在金融、医疗、法律等领域，利用专用词库和NER模型抽取非结构化文本中的关键实体（如药品名、合同条款、股票代码）。
*   **NLP研究与教学**：作为研究人员或学生获取最新NLP论文、数据集、模型代码及技术报告的聚合资源库。

**4. 技术亮点**
*   **高度模块化与聚合性**：不仅包含代码工具，还整合了清华XLORE、百度基准系统等顶级学术与工业界资源，降低了NLP入门门槛。
*   **多语言与跨模态支持**：除中文外，还支持英文、日文等多语言处理，并涵盖语音识别（ASR）、手写OCR及音频情感分析等多模态技术。
*   **前沿模型落地**：紧跟Transformer时代潮流，提供了大量基于BERT、RoBERTa、ALBERT等最新架构的中文微调代码和应用示例。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 81467 | 🍴 15249 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一且高效的大语言模型（LLM）与视觉语言模型（VLM）微调框架，支持超过100种模型。该项目已被 ACL 2024 收录，旨在简化模型训练流程并提升效率。它涵盖了从指令微调到强化学习对齐的全链路能力。

2. **核心功能**
*   支持统一微调超过100种主流大模型及视觉语言模型。
*   集成 LoRA、QLoRA 等高效参数微调技术以降低资源门槛。
*   提供完整的 RLHF（基于人类反馈的强化学习）和 DPO 训练支持。
*   内置多种量化策略，优化显存占用并加速推理过程。

3. **适用场景**
*   需要快速对 Llama、Qwen、Gemma 等开源模型进行指令微调的研究人员。
*   显存有限但希望部署高效微调（如 QLoRA）的开发者和初创团队。
*   希望统一不同模型训练接口，简化 AI 应用开发流程的工程团队。

4. **技术亮点**
*   **高度统一性**：通过标准化接口兼容海量模型架构，无需为每种模型编写专用代码。
*   **极致效率**：结合 PEFT 与量化技术，在消费级硬件上即可运行大规模模型微调。
*   **学术认可**：作为 ACL 2024 的入选项目，其方法论具有坚实的学术理论基础。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 72525 | 🍴 8871 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- ### 1. **中文简介**
这是一个为期12周、包含24课时的全面人工智能入门课程，旨在让所有人都能轻松学习AI知识。该项目由微软发起，通过结构化的教程帮助初学者从零开始掌握机器学习与深度学习的核心概念。

### 2. **核心功能**
*   **系统化课程结构**：分为12周24节课，循序渐进地覆盖从基础到进阶的AI知识体系。
*   **多领域技术覆盖**：内容涵盖机器学习、计算机视觉（CNN）、自然语言处理（NLP/RNN）及生成对抗网络（GAN）等主流AI技术。
*   **交互式学习体验**：主要采用Jupyter Notebook格式，提供可运行的代码示例和即时反馈的学习环境。
*   **开源免费资源**：作为“Microsoft For Beginners”系列的一部分，完全公开免费，降低学习门槛。

### 3. **适用场景**
*   **初学者自我提升**：适合无AI背景的程序员或学生进行系统性自学。
*   **高校/培训机构教学**：可作为计算机科学或数据科学相关课程的配套教材。
*   **企业内训基础**：用于团队内部普及AI基础知识，统一技术认知。

### 4. **技术亮点**
*   **全栈式AI概览**：在一个项目中整合了传统机器学习、深度学习和前沿生成式AI技术，提供完整的技术图谱。
*   **实战导向**：通过具体的Notebook代码实例，将理论概念直接转化为可执行的代码逻辑。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 48468 | 🍴 10057 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### system_prompts_leaks
- 1. **中文简介**
该项目收集并泄露了Anthropic、OpenAI、Google及xAI等主流大模型厂商的系统提示词（System Prompts）。内容涵盖Claude、ChatGPT、Gemini等知名模型的最新版本，并保持定期更新。

2. **核心功能**
*   聚合多家头部AI厂商的核心系统提示词数据。
*   覆盖从基础对话到代码生成的多种模型变体。
*   提供持续更新的动态资源库以跟踪最新泄露信息。
*   通过开源形式促进对大模型内部指令机制的研究。

3. **适用场景**
*   AI安全研究人员分析大模型的系统指令漏洞与防御机制。
*   提示词工程师学习顶级模型的指令构建技巧以优化自身Prompt。
*   开发者在调试Agent行为时参考官方系统预设进行对比分析。
*   对生成式AI内部运作原理感兴趣的技术爱好者进行知识拓展。

4. **技术亮点**
*   集成度高：一次性汇总多平台、多版本的关键系统提示词。
*   时效性强：针对最新发布的模型版本（如Claude Opus 4.8等）保持快速跟进。
*   领域广泛：横跨通用聊天、代码辅助（Cursor/VS Code）及搜索增强（Perplexity）等多个应用场景。
- 链接: https://github.com/asgeirtj/system_prompts_leaks
- ⭐ 46294 | 🍴 7592 | 语言: JavaScript
- 标签: ai, ai-agents, anthropic, awesome, chatbot

### ailearning
- ### GitHub项目分析报告：ailearning

**1. 中文简介**
AiLearning 是一个集数据分析、机器学习实战、线性代数基础以及 PyTorch 和 TensorFlow 2 等深度学习框架应用于一体的综合性学习资源库。该项目涵盖了从传统算法到自然语言处理（NLP）的广泛领域，旨在为开发者提供系统的 AI 学习路径。

**2. 核心功能**
*   **多维算法实现**：包含集成学习（如 AdaBoost）、聚类（K-Means、FP-Growth）、分类（SVM、逻辑回归、朴素贝叶斯）及降维（PCA、SVD）等经典算法的代码实现。
*   **深度学习框架实践**：深入讲解并实战 PyTorch 和 TensorFlow 2 (TF2)，涵盖 DNN、RNN、LSTM 等神经网络结构。
*   **自然语言处理 (NLP)**：利用 NLTK 库进行文本处理，并结合深度学习模型解决 NLP 任务。
*   **推荐系统构建**：提供基于协同过滤等技术的推荐系统实现案例。
*   **数学基础强化**：结合线性代数知识，辅助理解机器学习背后的数学原理。

**3. 适用场景**
*   **AI 初学者系统入门**：适合希望从零开始，通过代码实战掌握机器学习和深度学习全流程的学习者。
*   **算法工程师面试准备**：可作为复习经典算法原理与代码实现的参考资料，帮助应对技术面试。
*   **课程作业与项目参考**：为学生或研究人员提供 PCA、SVM、RNN 等特定算法的标准实现模板。

**4. 技术亮点**
*   **全栈式学习覆盖**：不仅包含高级深度学习，还兼顾了线性代数等基础数学知识，形成了完整的学习闭环。
*   **主流框架并存**：同时支持 PyTorch 和 TensorFlow 2，方便用户对比不同框架的实现差异。
*   **高人气验证**：拥有超过 42,000 个星标，证明其在社区中具有较高的认可度和实用性。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42351 | 🍴 11540 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### ai-engineering-from-scratch
- 描述: Learn it. Build it. Ship it for others.
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 36451 | 🍴 5994 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34924 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33699 | 🍴 4689 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28201 | 🍴 3423 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 25738 | 🍴 2883 | 语言: MDX
- 标签: agent, agents, ai, gemini, generative-ai

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**
这是一个汇集了500个AI相关项目的精选库，涵盖机器学习、深度学习、计算机视觉及自然语言处理等领域。该项目提供了完整的代码实现，旨在为开发者提供丰富的实践案例和学习资源。

2. **核心功能**
*   收录大量经过筛选的高质量AI实战项目代码。
*   覆盖机器学习、深度学习、CV和NLP四大核心领域。
*   提供可直接运行的Python代码示例，便于快速上手。
*   作为“Awesome”列表，对项目进行分类整理和索引。

3. **适用场景**
*   AI初学者希望通过实际项目快速掌握算法应用。
*   研究人员需要寻找特定领域的最新开源项目参考。
*   工程师在开发中遇到瓶颈时，参考类似项目的实现逻辑。
*   教育机构用于制作人工智能相关的教学案例库。

4. **技术亮点**
*   极高的社区认可度（近3.5万星标），内容权威且更新及时。
*   全面的技术栈覆盖，从基础ML到前沿DL均有涉及。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 34924 | 🍴 7293 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**
Skyvern 是一款基于人工智能的自动化框架，能够模拟人类操作浏览器来执行复杂的 Web 工作流。它利用计算机视觉和大语言模型（LLM）技术，无需依赖脆弱的 DOM 选择器即可实现跨平台的网页交互与任务自动化。该项目旨在为 RPA（机器人流程自动化）提供更智能、更稳定的解决方案。

2. **核心功能**
*   **AI 驱动的视觉感知**：结合大语言模型与图像识别技术，通过“看”屏幕而非解析代码来理解页面元素和布局。
*   **自适应工作流引擎**：能够动态处理页面变化，自动规划并执行多步骤的浏览器操作序列。
*   **结构化数据提取**：从非结构化的网页界面中精准抓取关键信息，并将其转换为标准化的 JSON 格式。
*   **API 优先架构**：提供易于集成的 API 接口，方便开发者将其嵌入到现有的自动化管道或后端服务中。
*   **无需预定义选择器**：摆脱对特定 CSS/XPath 路径的强依赖，显著降低因前端改版导致的脚本维护成本。

3. **适用场景**
*   **企业级 RPA 替代方案**：用于自动化那些传统 Selenium/Playwright 脚本难以维护的复杂后台系统操作。
*   **跨平台表单填写与提交**：在多个不同的 Web 应用中自动填充信息、上传文件并提交审批流程。
*   **网页数据监控与抓取**：实时监测竞争对手价格、库存变化或新闻更新，并自动提取关键数据进行归档。
*   **QA 自动化测试**：模拟真实用户行为进行端到端的功能测试，提高测试用例对 UI 变更的鲁棒性。

4. **技术亮点**
*   **Vision-Language Model (VLM) 集成**：创新性地将多模态 AI 能力应用于浏览器自动化，实现了语义级的页面理解。
*   **兼容主流自动化库**：底层支持 Playwright 等高性能浏览器控制库，同时封装了 Puppeteer 和 Selenium 的逻辑优势。
*   **高容错率**：相比传统自动化脚本，Skyvern 对页面轻微变动、弹窗干扰等异常情况具有更强的适应性和自愈能力。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22013 | 🍴 2055 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**
CVAT 是领先的计算机视觉标注平台，旨在构建高质量的视觉数据集以服务于视觉 AI。它提供开源、云及企业级产品，支持图像、视频和 3D 数据的 AI 辅助标注、质量保证及团队协作功能。

2. **核心功能**
*   支持图像、视频及 3D 数据的多维度高精度标注。
*   集成 AI 辅助标注技术，显著提升数据标记效率。
*   提供完善的质量保证机制与团队多人协作能力。
*   开放开发者 API 并附带数据分析工具，便于系统集成。

3. **适用场景**
*   自动驾驶或机器人感知系统中的物体检测与语义分割数据集构建。
*   工业质检领域中对缺陷图像进行大规模分类与标注。
*   视频内容分析项目中需要对连续帧进行行为识别或目标追踪标注。
*   科研机构利用开源版本进行计算机视觉算法的数据预处理。

4. **技术亮点**
*   采用 Python 开发，原生兼容 PyTorch 和 TensorFlow 等主流深度学习框架。
*   具备从开源社区到企业级云服务的灵活部署方案，适应不同规模需求。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16155 | 🍴 3723 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 描述: Advanced AI Explainability for computer vision.  Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12892 | 🍴 1709 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- ### 1. **中文简介**
Kornia 是一个专注于空间人工智能（Spatial AI）的几何计算机视觉库，旨在为深度学习框架 PyTorch 提供可微分的传统图像处理能力。它通过集成先进的计算机视觉算法，支持在神经网络中直接进行几何变换和图像处理，从而简化了从图像到三维空间的推理过程。

### 2. **核心功能**
*   **可微分图像处理**：提供基于 PyTorch 的可微分模块，允许在反向传播中直接处理图像几何变换。
*   **几何计算机视觉工具**：内置丰富的相机标定、位姿估计和三维重建等几何算法实现。
*   **与深度学习无缝集成**：作为 PyTorch 的扩展库，轻松嵌入现有的深度学习工作流和模型架构中。
*   **自动化机器学习支持**：支持神经架构搜索（NAS）和超参数优化中的图像处理组件自动化。
*   **机器人视觉应用**：提供适用于机器人导航、抓取和环境理解的空间感知基础模块。

### 3. **适用场景**
*   **自动驾驶与机器人导航**：用于实时处理传感器数据，进行环境理解和路径规划。
*   **增强现实（AR）/虚拟现实（VR）**：实现精确的相机姿态估计和三维场景重建。
*   **医学影像分析**：在深度学习模型中集成可微分的图像配准和几何校正步骤。
*   **工业质检与缺陷检测**：利用几何变换和图像处理技术提升自动化检测系统的鲁棒性。

### 4. **技术亮点**
*   **端到端可训练性**：打破了传统计算机视觉与深度学习的界限，使整个视觉流水线可微且可端到端训练。
*   **高性能 CUDA 加速**：核心计算部分针对 GPU 进行了高度优化，确保大规模数据处理效率。
*   **模块化设计**：提供丰富且独立的视觉原语（Primitives），便于研究人员快速构建和实验新的视觉模型。
- 链接: https://github.com/kornia/kornia
- ⭐ 11251 | 🍴 1192 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8869 | 🍴 2193 | 语言: Python
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
- ⭐ 2616 | 🍴 693 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2411 | 🍴 217 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- **项目名称：** openclaw

**1. 中文简介**
OpenClaw 是一款开源的个人 AI 助手，支持跨操作系统和平台运行，强调数据自主权。它采用“龙虾模式”（Lobster Way），旨在让用户完全掌控自己的 AI 体验，确保隐私与安全。

**2. 核心功能**
*   **跨平台兼容：** 支持任意操作系统和硬件平台，实现无缝部署。
*   **数据主权优先：** 强调“拥有自己的数据”，确保用户隐私不被第三方滥用。
*   **个人化 AI 助手：** 专为个人用户设计，提供定制化的智能交互体验。
*   **开源透明：** 代码完全公开，允许社区审查和改进，增强信任度。
*   **模块化架构：** 基于 TypeScript 构建，便于扩展和集成其他服务或插件。

**3. 适用场景**
*   **隐私敏感用户：** 需要本地化部署、不希望数据上传至云端的个人用户。
*   **开发者与技术爱好者：** 希望自定义 AI 助手行为或集成到现有工作流的技术人员。
*   **多设备协同场景：** 需要在不同操作系统（如 Windows、macOS、Linux）间同步个人 AI 助手的用户。

**4. 技术亮点**
*   采用 TypeScript 开发，具备类型安全和良好的工程化基础。
*   设计理念聚焦于“去中心化”和“用户控制权”，区别于主流云端 AI 服务。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 380580 | 🍴 79725 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- 1. **中文简介**
Superpowers 是一个经过验证的智能体技能框架与软件开发方法论。它通过结构化思维链和子代理驱动开发，旨在提升软件工程的效率与质量。该项目特别适用于需要系统化头脑风暴和规范化的复杂编码任务。

2. **核心功能**
- 提供基于智能体的技能框架，支持自动化代码生成与审查。
- 采用子代理驱动的开发模式，将复杂任务分解为可管理的步骤。
- 整合头脑风暴工具，辅助开发者进行创意构思与技术选型。
- 定义标准化的软件开发生命周期（SDLC）流程，确保开发规范性。

3. **适用场景**
- 需要快速原型开发且强调代码质量的敏捷团队。
- 依赖自动化测试和持续集成的大型软件工程维护。
- 希望利用AI辅助进行架构设计和复杂逻辑梳理的开发场景。

4. **技术亮点**
- 创新性地将“思维链”（Chain of Thought）理念融入实际的软件开发工作流中。
- 强调“技能”的可复用性，构建了模块化的智能体交互体系。
- 开源且社区活跃，拥有极高的星标数，验证了其方法论的广泛接受度。
- 链接: https://github.com/obra/superpowers
- ⭐ 239338 | 🍴 21235 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- **1. 中文简介**
Hermes Agent 是一款能够伴随用户共同成长的智能代理工具，旨在通过持续学习和交互优化用户体验。它作为一个灵活且可扩展的 AI 助手框架，支持多种大型语言模型，帮助用户更高效地完成各类复杂任务。

**2. 核心功能**
*   支持集成 Anthropic Claude、OpenAI ChatGPT 等多种主流大语言模型。
*   具备自适应学习能力，能根据用户的使用习惯和反馈不断优化代理行为。
*   提供模块化架构，允许开发者轻松扩展自定义功能和插件。
*   兼容多种开发环境和代码编辑器，提升编程与自动化工作流的效率。

**3. 适用场景**
*   需要个性化定制的智能编程助手，用于代码生成、审查及重构。
*   希望构建私有化或特定领域 AI 代理的开发者和研究团队。
*   追求高效自动化工作流的个人用户，如文档处理、数据整理等。

**4. 技术亮点**
*   高度模块化的设计使其易于与现有工具链集成并快速迭代。
*   多模型支持能力让用户可根据任务需求灵活切换最佳 AI 后端。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 203656 | 🍴 36525 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- **1. 中文简介**
n8n 是一个具备原生 AI 能力的公平代码工作流自动化平台，支持通过可视化界面结合自定义代码进行构建。用户可以选择自行托管或采用云服务模式，并享受 400 多种集成工具的支持。

**2. 核心功能**
*   提供可视化拖拽式工作流构建器，降低自动化开发门槛。
*   内置原生 AI 能力，可轻松将大语言模型整合到业务逻辑中。
*   拥有超过 400 种应用和服务的原生集成连接器。
*   支持混合部署模式，允许用户选择本地自托管或云端使用。
*   兼容低代码与高代码开发，允许在流程中嵌入自定义 TypeScript 代码。

**3. 适用场景**
*   **企业数据同步与 ETL**：自动在不同数据库、CRM 和 ERP 系统间同步数据并进行清洗转换。
*   **AI 驱动的业务自动化**：利用 AI 组件自动处理客户邮件分类、内容生成或智能客服响应。
*   **DevOps 与 CI/CD 流水线**：自动化代码提交后的测试通知、部署状态监控及运维告警流程。
*   **跨平台消息聚合**：将来自 Slack、Telegram、邮件等多渠道的消息统一汇聚到一个中心化管理面板。

**4. 技术亮点**
*   **MCP 支持**：原生支持 Model Context Protocol (MCP)，增强了 AI 模型与外部数据源的交互能力。
*   **公平代码协议 (Fair-code)**：在保持开源精神的同时，对特定商业用途设定了合理的许可限制，平衡社区贡献与商业可持续性。
*   **TypeScript 生态**：基于 TypeScript 开发，提供了良好的类型安全和开发者体验，便于扩展自定义节点。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 194169 | 🍴 58853 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
AutoGPT 旨在让每个人都能轻松使用并构建人工智能应用，实现AI技术的普及化。我们的使命是提供必要的工具，让用户能够专注于自身真正重要的事务。

2. **核心功能**
*   支持多种大语言模型后端（如OpenAI GPT、Anthropic Claude、LLaMA等），具备高度的兼容性。
*   实现自主智能体（Autonomous Agents）架构，能够独立规划并执行复杂的多步任务。
*   提供易于使用的开发框架，降低构建自定义AI应用的门槛。
*   强调开源与社区驱动，鼓励开发者基于其平台进行二次开发和扩展。

3. **适用场景**
*   自动化重复性办公流程，如数据整理、邮件处理或日程管理。
*   构建个性化的AI助手，用于信息查询、内容创作或代码辅助生成。
*   作为研究基础，探索大型语言模型在自主决策和多步骤推理方面的能力边界。

4. **技术亮点**
*   原生支持多模型API集成（包括GPT、Claude及本地Llama模型），灵活适配不同算力与隐私需求。
*   采用先进的Agent模式设计，使程序具备自我反思、目标拆解及工具调用的能力。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185158 | 🍴 46132 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 164385 | 🍴 21285 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 163894 | 🍴 30367 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 156633 | 🍴 46147 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 150112 | 🍴 9350 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

### dify
- 描述: Production-ready platform for agentic workflow development.
- 链接: https://github.com/langgenius/dify
- ⭐ 146665 | 🍴 23090 | 语言: TypeScript
- 标签: agent, agentic-ai, agentic-framework, agentic-workflow, ai

