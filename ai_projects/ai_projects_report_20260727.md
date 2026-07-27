# GitHub AI项目每日发现报告
日期: 2026-07-27

## 新发布的AI项目

### openclaude-improved
- 1. **中文简介**  
该项目是一个基于TypeScript开发的AI编码助手，旨在通过多模型支持（如Claude、Gemini等）实现跨平台、多场景的AI辅助编码。它强调灵活性和通用性，能够适配各种开发环境。

2. **核心功能**  
- 支持多种AI模型（如Claude、Gemini）的集成与切换。  
- 提供命令行工具（CLI），便于开发者快速调用。  
- 基于Model Context Protocol（MCP）实现模型间上下文管理。  
- 专注于AI编码代理（Coding Agent），提升代码生成与调试效率。  
- 兼容OpenRouter等API，灵活调用不同AI服务。

3. **适用场景**  
- 开发者在编写代码时通过AI助手生成代码片段或调试错误。  
- 跨平台开发中需要统一AI编码工具的场景。  
- 需要结合多个AI模型（如Claude和Gemini）的复杂任务。  
- 命令行环境下快速调用AI进行代码生成或分析。

4. **技术亮点**  
- 采用TypeScript开发，保证代码类型安全与可维护性。  
- 通过MCP实现模型间上下文无缝传递，提升多模型协作效率。  
- 支持OpenRouter API，灵活切换不同AI模型服务。  
- 轻量级CLI工具，便于集成到现有开发工作流中。
- 链接: https://github.com/0xwilliamortiz/openclaude-improved
- ⭐ 175 | 🍴 26 | 语言: TypeScript
- 标签: agentic-ai, ai, ai-agent, ai-coding, ai-coding-agent

### deer-workflow
- 1. **中文简介**  
deer-workflow 是一个开源的动态工作流运行时，使用 TypeScript 进行编排，并将语义工作委托给可替换的 Agent 运行时。它支持灵活的 Agent 协作和动态任务调度，适合构建复杂的 AI 工作流应用。

2. **核心功能**  
- 使用 TypeScript 编排工作流，确保类型安全和开发效率。  
- 支持可替换的 Agent 运行时，便于集成不同语义模型。  
- 动态工作流调度，支持任务依赖和条件分支。  
- 与 LLM 和 AI 工具无缝协作，提升自动化能力。  
- 基于 Bun 运行时，提供高性能执行环境。

3. **适用场景**  
- 构建多 Agent 协作的 AI 自动化流程，如智能客服或内容生成系统。  
- 动态任务编排，如数据分析或内容审核流水线。  
- 基于 LLM 的智能代理工作流，如自动代码生成或报告撰写。  
- 快速原型开发，结合 TypeScript 和 Bun 提高开发效率。

4. **技术亮点**  
- 使用 TypeScript 确保工作流编排的类型安全。  
- 支持可替换的 Agent 运行时，灵活集成不同语义模型。  
- 基于 Bun 运行时，提供高性能的执行环境。  
- 动态工作流调度，支持任务依赖和条件分支。
- 链接: https://github.com/deerwork-ai/deer-workflow
- ⭐ 127 | 🍴 15 | 语言: TypeScript
- 标签: agent, ai, ai-agent, ai-agents, ai-coding

### ai-stock-pool
- 1. **中文简介**：这是一个基于人工智能的产业链股票池项目，支持美股与A股映射，具备主动发现、政策压力分析等功能，并支持一键部署。

2. **核心功能**：支持美股与A股映射，方便跨市场投资分析；主动发现潜在投资机会；分析政策对市场的影响；提供一键部署功能，便于快速上线。

3. **适用场景**：适合金融投资者进行跨市场股票分析；适合AI研究人员进行产业链股票趋势预测；适合开发者快速部署股票分析工具。

4. **技术亮点**：使用JavaScript开发，结合Cloudflare Workers和Vercel实现高效部署；标签涉及arxiv和investment-research，表明其具备一定的学术和研究支持。
- 链接: https://github.com/yaoleifly/ai-stock-pool
- ⭐ 36 | 🍴 19 | 语言: JavaScript
- 标签: a-shares, ai, arxiv, cloudflare-workers, investment-research

### cursor-bridge
- 1. **中文简介**  
Cursor-bridge 是一个基于 Rust 编写的工具，允许用户在 Cursor 订阅环境中运行 Claude Code。它无需任何配置，仅需一个二进制文件即可实现功能。

2. **核心功能**  
- 支持在 Cursor 订阅环境中运行 Claude Code。  
- 提供一键式二进制文件，零配置即可使用。  
- 通过代理或桥接方式实现 AI 工具与开发环境的无缝集成。  
- 适用于快速开发和原型设计，提升开发效率。  

3. **适用场景**  
- 开发者需要在 Cursor 环境中调用 Claude Code 进行代码生成或调试。  
- 需要快速搭建 AI 辅助开发环境，减少配置时间。  
- 用于跨平台开发工具链的集成与优化。  

4. **技术亮点**  
- 使用 Rust 编写，确保高性能和内存安全性。  
- 零配置设计，简化用户操作。  
- 作为桥梁工具，实现 Claude Code 与 Cursor 的兼容与协作。
- 链接: https://github.com/hkc5/cursor-bridge
- ⭐ 22 | 🍴 1 | 语言: Rust
- 标签: ai, bridge, claude, claude-code, cli

### Amadeus
- 1. **中文简介**：Amadeus是一个面向桌面交互的实时多模态AI代理项目，通过整合多种模态数据实现更智能的桌面操作。目前项目处于早期阶段，仅有19个星标，尚未明确指定编程语言。

2. **核心功能**：
- 支持实时多模态数据整合处理
- 具备桌面环境智能交互能力
- 可能包含视觉、语音等多模态输入支持
- 专注于自动化桌面任务执行

3. **适用场景**：
- 桌面操作自动化流程
- 多模态人机交互研究
- 智能桌面助手开发
- 跨模态数据集成实验

4. **技术亮点**：项目采用多模态AI架构，强调实时交互能力，专注于桌面环境下的智能代理应用。
- 链接: https://github.com/Lucas1479/Amadeus
- ⭐ 19 | 🍴 0 | 语言: 未知

### llmwiki-harness
- 描述: 无描述
- 链接: https://github.com/cookyman74/llmwiki-harness
- ⭐ 18 | 🍴 5 | 语言: Python
- 标签: ai, claude-code, knowledge-management, llm, markdown

### ai-excel
- 描述: 利用ai使用自然语言操作excel，不再需要记公式
- 链接: https://github.com/ns2250225/ai-excel
- ⭐ 16 | 🍴 4 | 语言: TypeScript

### UGC-dashboard
- 描述: Open-source visual AI UGC workflow dashboard powered by Higgsfield and OpenAI
- 链接: https://github.com/harshith-vaddiparthy/UGC-dashboard
- ⭐ 12 | 🍴 7 | 语言: TypeScript
- 标签: ai-ugc, higgsfield, nextjs, open-source, react-flow

### KiraAP
- 描述: Nền tảng mã nguồn mở quản lý và tích hợp AI đa phương tiện từ Google Agent Flatform / Vertex AI (Chat, Tạo Ảnh, Tạo Video, TTS)
- 链接: https://github.com/HuyKira/KiraAP
- ⭐ 11 | 🍴 14 | 语言: JavaScript

### data-driven-ai-guide
- 描述: Teach Data Engineers How to Think AI.
- 链接: https://github.com/zhiweio/data-driven-ai-guide
- ⭐ 11 | 🍴 2 | 语言: Shell
- 标签: ai-agent, ai-ready, data-foundation, data-loops, ontology

## 热门AI项目

## Machine Learning项目

### funNLP
- 1. **中文简介**  
funNLP是一个全面且功能丰富的Python库，专注于自然语言处理（NLP）任务，涵盖中英文敏感词检测、语言识别、语音合成、文本生成、知识图谱构建等多样化的NLP功能。

2. **核心功能**  
- 支持中英文敏感词检测及语言识别。  
- 提供电话、手机号码的归属地与运营商查询功能。  
- 包含名字性别推断、中文人名库、情感分析等高级功能。  
- 支持中文文本的生成、摘要、翻译及知识图谱构建。  

3. **适用场景**  
- 用于构建智能客服系统，通过情感分析和文本生成提升用户体验。  
- 应用于金融领域，通过知识图谱和数据增强工具进行数据分析。  
- 在医疗领域，利用医学问答数据集和命名实体识别技术进行辅助诊断。  

4. **技术亮点**  
- 集成了多种先进的NLP模型和工具，如BERT、GPT-2等，支持多种语言处理任务。  
- 提供了丰富的数据集和工具，如中文人名库、医学问答数据集等，便于快速开发和实验。  
- 支持语音识别和情感分析，适用于多模态应用场景。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82067 | 🍴 15256 | 语言: Python

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**：该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的资源库，提供了相关项目的代码和实现。它旨在为开发者、研究人员和爱好者提供一个全面的实践和学习平台。

2. **核心功能**：  
   - 提供500多个AI相关项目的代码示例。  
   - 覆盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。  
   - 以Python为主要实现语言，适合快速学习和实践。  
   - 项目标签丰富，方便用户按领域查找资源。  

3. **适用场景**：  
   - 初学者通过项目实践快速掌握AI技术。  
   - 开发者寻找灵感或参考代码实现特定功能。  
   - 研究人员快速验证算法或获取开源项目的基础实现。  

4. **技术亮点**：  
   - 项目数量庞大且覆盖广泛，适合不同需求的用户。  
   - 以Python为主，与主流AI框架和工具链兼容。  
   - 标签分类清晰，便于高效筛选和查找特定领域的资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35735 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**：Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具，支持多种框架和格式。它通过直观的图形界面帮助用户理解模型结构和数据流动，广泛应用于模型调试与展示。

2. **核心功能**：
   - 支持多种深度学习框架的模型文件，如 TensorFlow、PyTorch、Keras 和 ONNX。
   - 提供交互式图形界面，方便查看模型结构和层参数。
   - 兼容多种文件格式，包括 CoreML、Safetensors 和 TensorFlow Lite。
   - 支持本地和在线两种使用方式，便于快速部署和共享。
   - 允许用户通过浏览器直接打开模型文件，无需额外安装。

3. **适用场景**：
   - 研究人员在调试和优化神经网络模型时，快速查看模型结构。
   - 开发者在展示模型架构时，生成直观的可视化报告。
   - 教育场景中，帮助学生理解复杂的深度学习模型。
   - 跨团队协作时，方便共享和审查模型文件。

4. **技术亮点**：
   - 基于 JavaScript 开发，支持跨平台使用，无需依赖特定操作系统。
   - 开源社区活跃，持续更新支持新格式和框架。
   - 轻量级设计，占用资源少，适合快速集成到现有工作流中。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33268 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### onnx
- ### 1. 中文简介
ONNX（Open Neural Network Exchange）是一个用于机器学习互操作性的开放标准，旨在促进不同深度学习框架之间的模型转换和共享。它支持多种流行的机器学习框架，如PyTorch、TensorFlow和Keras，使得开发者能够更便捷地部署和训练模型。

### 2. 核心功能
- **模型转换**：支持将不同框架的模型转换为ONNX格式，方便跨平台使用。
- **模型共享**：提供一个统一的模型格式，便于模型在不同环境和工具之间的共享和复用。
- **工具支持**：提供一系列工具，用于模型验证、优化和转换，确保模型在不同框架间的兼容性和性能。
- **社区支持**：拥有活跃的社区和丰富的文档，方便开发者获取帮助和贡献代码。

### 3. 适用场景
- **跨框架模型迁移**：在开发过程中，从一种框架（如PyTorch）迁移到另一种框架（如TensorFlow）时，可以使用ONNX进行模型转换。
- **模型部署**：在部署模型时，可以使用ONNX格式将模型转换为适合特定硬件或平台的格式，提高部署效率。
- **模型优化**：利用ONNX提供的优化工具，对模型进行剪枝、量化等操作，以提升模型的运行效率和性能。

### 4. 技术亮点
- **开放标准**：ONNX是一个开放标准，由多个行业巨头共同维护，确保了其广泛兼容性和未来扩展性。
- **工具链丰富**：提供了一系列工具链，包括模型转换、验证、优化等，方便开发者在不同场景下使用。
- **社区活跃**：拥有活跃的社区和贡献者，不断推动ONNX的发展和更新，确保其技术领先性。
- 链接: https://github.com/onnx/onnx
- ⭐ 21216 | 🍴 3976 | 语言: Python
- 标签: ai, artificial-intelligence, deep-learning, deep-neural-networks, dnn

### ml-engineering
- 1. **中文简介**  
   “ml-engineering” 是一个关于机器学习工程的开源项目，涵盖从模型开发到部署的完整流程，提供丰富的资源和实践指南，适合希望提升机器学习工程能力的开发者。该项目由Python编写，拥有18470个星标，是机器学习工程领域的热门资源。

2. **核心功能**  
   - 提供机器学习工程的最佳实践和案例分析。  
   - 支持调试和优化大规模模型（如LLM）的训练与推理。  
   - 涵盖GPU管理、存储和网络配置等基础设施相关内容。  
   - 包含基于PyTorch的Transformer模型实现与扩展。  
   - 强调可扩展性和生产环境中的模型部署（MLOps）。

3. **适用场景**  
   - 用于指导大规模语言模型（LLM）的训练与推理优化。  
   - 适用于需要构建端到端机器学习流水线（MLOps）的团队。  
   - 适合科研或工业界开发者调试和部署高性能机器学习模型。  
   - 可用于学习如何在Slurm等集群环境中管理训练任务。

4. **技术亮点**  
   - 提供针对大规模模型的高效推理和训练实践。  
   - 涵盖从开发到部署的全栈机器学习工程解决方案。  
   - 支持主流深度学习框架（如PyTorch）和Transformer架构。  
   - 注重系统可扩展性、调试能力和生产环境稳定性。
- 链接: https://github.com/stas00/ml-engineering
- ⭐ 18470 | 🍴 1182 | 语言: Python
- 标签: ai, debugging, gpus, inference, large-language-models

### ML-YouTube-Courses
- 描述: 📺 Discover the latest machine learning / AI courses on YouTube.
- 链接: https://github.com/dair-ai/ML-YouTube-Courses
- ⭐ 17341 | 🍴 2118 | 语言: 未知
- 标签: ai, data-science, deep-learning, machine-learning, natural-language-processing

### cheatsheets-ai
- 描述: Essential Cheat Sheets for deep learning and machine learning researchers https://medium.com/@kailashahirwar/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 描述: 人工智能学习路线图，整理近200个实战案例与项目，免费提供配套教材，零基础入门，就业实战！包括：Python，数学，机器学习，数据分析，深度学习，计算机视觉，自然语言处理，PyTorch tensorflow machine-learning,deep-learning data-analysis data-mining mathematics data-science artificial-intelligence python tensorflow tensorflow2 caffe keras pytorch algorithm numpy pandas matplotlib seaborn nlp cv等热门领域
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13188 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### cleanlab
- 描述: Cleanlab's open-source library is the standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
- 链接: https://github.com/cleanlab/cleanlab
- ⭐ 11600 | 🍴 911 | 语言: Python
- 标签: active-learning, annotation, anomaly-detection, data-annotation, data-centric-ai

### mlcourse.ai
- 描述: Open Machine Learning Course
- 链接: https://github.com/Yorko/mlcourse.ai
- ⭐ 10677 | 🍴 5708 | 语言: Python
- 标签: algorithms, data-analysis, data-science, docker, ipynb

## Deep Learning项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**：该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的资源库，提供了相关项目的代码和实现。它旨在为开发者、研究人员和爱好者提供一个全面的实践和学习平台。

2. **核心功能**：  
   - 提供500多个AI相关项目的代码示例。  
   - 覆盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。  
   - 以Python为主要实现语言，适合快速学习和实践。  
   - 项目标签丰富，方便用户按领域查找资源。  

3. **适用场景**：  
   - 初学者通过项目实践快速掌握AI技术。  
   - 开发者寻找灵感或参考代码实现特定功能。  
   - 研究人员快速验证算法或获取开源项目的基础实现。  

4. **技术亮点**：  
   - 项目数量庞大且覆盖广泛，适合不同需求的用户。  
   - 以Python为主，与主流AI框架和工具链兼容。  
   - 标签分类清晰，便于高效筛选和查找特定领域的资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35735 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### netron
- 1. **中文简介**：Netron 是一个用于可视化神经网络、深度学习及机器学习模型的开源工具，支持多种框架和格式。它通过直观的图形界面帮助用户理解模型结构和数据流动，广泛应用于模型调试与展示。

2. **核心功能**：
   - 支持多种深度学习框架的模型文件，如 TensorFlow、PyTorch、Keras 和 ONNX。
   - 提供交互式图形界面，方便查看模型结构和层参数。
   - 兼容多种文件格式，包括 CoreML、Safetensors 和 TensorFlow Lite。
   - 支持本地和在线两种使用方式，便于快速部署和共享。
   - 允许用户通过浏览器直接打开模型文件，无需额外安装。

3. **适用场景**：
   - 研究人员在调试和优化神经网络模型时，快速查看模型结构。
   - 开发者在展示模型架构时，生成直观的可视化报告。
   - 教育场景中，帮助学生理解复杂的深度学习模型。
   - 跨团队协作时，方便共享和审查模型文件。

4. **技术亮点**：
   - 基于 JavaScript 开发，支持跨平台使用，无需依赖特定操作系统。
   - 开源社区活跃，持续更新支持新格式和框架。
   - 轻量级设计，占用资源少，适合快速集成到现有工作流中。
- 链接: https://github.com/lutzroeder/netron
- ⭐ 33268 | 🍴 3169 | 语言: JavaScript
- 标签: ai, coreml, deep-learning, deeplearning, keras

### cheatsheets-ai
- 1. **中文简介**  
   该项目为深度学习与机器学习研究者提供了一系列必备速查表，涵盖关键概念、模型架构、优化方法及常用库的使用指南，帮助研究人员快速回顾和参考。

2. **核心功能**  
   - 提供深度学习与机器学习的基础概念速查表。  
   - 汇总常用框架（如 Keras、TensorFlow）的使用技巧。  
   - 包含数据处理与可视化工具（如 Matplotlib、NumPy）的快捷指南。  
   - 总结优化算法和模型调参的关键策略。  
   - 为科研和开发提供高效的参考资源。

3. **适用场景**  
   - 机器学习研究者在撰写论文或设计模型时快速查阅相关知识点。  
   - 数据科学家在开发过程中快速调用常用库的函数和参数。  
   - 学生在学习深度学习课程时作为复习和参考工具。  
   - 工程师在部署模型时快速回顾优化和调参的最佳实践。

4. **技术亮点**  
   - 速查表内容覆盖全面，从基础概念到高级应用均有涉及。  
   - 内容简洁明了，便于快速查阅和记忆。  
   - 结合了理论与实践，适合不同层次的学习者和研究者使用。
- 链接: https://github.com/kailashahirwar/cheatsheets-ai
- ⭐ 15422 | 🍴 3381 | 语言: 未知
- 标签: artificial-intelligence, deep-learning, keras, machine-learning, matplotlib

### Ai-Learn
- 1. **中文简介**
Ai-Learn是一个人工智能学习路线图，整理了近200个实战案例和项目，并提供免费的配套教材，适合零基础入门和就业实战。

2. **核心功能**
- 提供人工智能学习路线图，涵盖Python、数学、机器学习、数据分析、深度学习、计算机视觉、自然语言处理等多个领域。
- 包含近200个实战案例和项目，提供丰富的实践机会。
- 免费提供配套教材，适合零基础入门。
- 专注于就业实战，帮助学习者提升职业技能。

3. **适用场景**
- 初学者学习人工智能基础知识，如Python、数学、机器学习等。
- 有基础的学习者通过实战案例和项目提升技能，准备就业。
- 教育机构或培训机构使用路线图和教材进行教学。

4. **技术亮点**
- 涵盖多个热门技术领域，如PyTorch、TensorFlow、Caffe、Keras等。
- 提供丰富的实战案例和项目，帮助学习者将理论知识应用于实践。
- 免费提供配套教材，降低学习门槛。
- 链接: https://github.com/tangyudi/Ai-Learn
- ⭐ 13188 | 🍴 2665 | 语言: 未知
- 标签: algorithm, artificial-intelligence, caffe, cv, data-analysis

### ludwig
- 1. **中文简介**  
Ludwig 是一个低代码框架，用于构建自定义大语言模型（LLM）、神经网络及其他人工智能模型，旨在简化 AI 模型的开发与部署流程。

2. **核心功能**  
- 提供低代码接口，快速构建和训练深度学习模型。  
- 支持多种数据类型，如文本、图像和结构化数据。  
- 内置预训练模型，方便用户进行微调与部署。  
- 模块化设计，支持灵活扩展和自定义模型结构。  
- 与 PyTorch 深度集成，兼容主流深度学习生态。

3. **适用场景**  
- 快速构建自然语言处理（NLP）应用，如文本分类、生成与翻译。  
- 构建图像识别与分析系统，适用于计算机视觉任务。  
- 在数据科学项目中用于快速原型开发与模型验证。  
- 企业级 AI 解决方案中实现模型标准化与自动化训练流程。

4. **技术亮点**  
- 支持基于数据中心的 AI 开发范式，强调数据驱动建模。  
- 内置 fine-tuning 功能，便于适配特定领域任务。  
- 兼容 Llama、Llama2、Mistral 等主流大语言模型。  
- 提供可视化与自动化训练工具，降低使用门槛。
- 链接: https://github.com/ludwig-ai/ludwig
- ⭐ 11746 | 🍴 1218 | 语言: Python
- 标签: computer-vision, data-centric, data-science, deep, deep-learning

### pwnagotchi
- 描述: (⌐■_■) - Deep Reinforcement Learning instrumenting bettercap for WiFi pwning.
- 链接: https://github.com/evilsocket/pwnagotchi
- ⭐ 9148 | 🍴 1237 | 语言: Python
- 标签: ai, bettercap, deep-learning, deep-neural-network, deep-reinforcement-learning

### jetson-inference
- 描述: Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.
- 链接: https://github.com/dusty-nv/jetson-inference
- ⭐ 8939 | 🍴 3102 | 语言: C++
- 标签: caffe, computer-vision, deep-learning, digits, embedded

### caffe2
- 描述: Caffe2 is a lightweight, modular, and scalable deep learning framework.
- 链接: https://github.com/facebookarchive/caffe2
- ⭐ 8374 | 🍴 1899 | 语言: Shell
- 标签: ai, artificial-intelligence, caffe2, deep-learning, deep-neural-networks

### DeepPavlov
- 描述: An open source library for deep learning end-to-end dialog systems and chatbots.
- 链接: https://github.com/deeppavlov/DeepPavlov
- ⭐ 6995 | 🍴 1172 | 语言: Python
- 标签: ai, artificial-intelligence, bot, chatbot, chitchat

### awesome-ai-in-finance
- 描述: 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- 链接: https://github.com/georgezouq/awesome-ai-in-finance
- ⭐ 6302 | 🍴 755 | 语言: 未知
- 标签: analysis, awesome, awesome-list, cryptocurrency, deep-learning

## Nlp项目

### funNLP
- 1. **中文简介**  
funNLP是一个全面且功能丰富的Python库，专注于自然语言处理（NLP）任务，涵盖中英文敏感词检测、语言识别、语音合成、文本生成、知识图谱构建等多样化的NLP功能。

2. **核心功能**  
- 支持中英文敏感词检测及语言识别。  
- 提供电话、手机号码的归属地与运营商查询功能。  
- 包含名字性别推断、中文人名库、情感分析等高级功能。  
- 支持中文文本的生成、摘要、翻译及知识图谱构建。  

3. **适用场景**  
- 用于构建智能客服系统，通过情感分析和文本生成提升用户体验。  
- 应用于金融领域，通过知识图谱和数据增强工具进行数据分析。  
- 在医疗领域，利用医学问答数据集和命名实体识别技术进行辅助诊断。  

4. **技术亮点**  
- 集成了多种先进的NLP模型和工具，如BERT、GPT-2等，支持多种语言处理任务。  
- 提供了丰富的数据集和工具，如中文人名库、医学问答数据集等，便于快速开发和实验。  
- 支持语音识别和情感分析，适用于多模态应用场景。
- 链接: https://github.com/fighting41love/funNLP
- ⭐ 82067 | 🍴 15256 | 语言: Python

### LlamaFactory
- 1. **中文简介**
LlamaFactory 是一个统一高效的微调平台，支持超过100种大型语言模型（LLMs）和视觉语言模型（VLMs）的微调，相关研究已在ACL 2024上发表。

2. **核心功能**
- 支持多种大型语言模型和视觉语言模型的高效微调。
- 提供多种微调方法，包括LoRA、QLORA等。
- 支持指令调优和强化学习从人类反馈（RLHF）。
- 集成量化技术，减少模型资源占用。
- 支持多种框架和库，如Transformers、PEFT等。

3. **适用场景**
- 学术研究：研究人员可以使用LlamaFactory进行大规模语言模型的微调和实验。
- 企业应用：企业可以利用LlamaFactory定制和优化自己的语言模型，以满足特定业务需求。
- 开发者工具：开发者可以使用LlamaFactory快速构建和部署基于语言模型的应用程序。

4. **技术亮点**
- 统一高效的微调框架，支持多种模型和微调方法。
- 集成先进的量化和稀疏技术，提高模型效率。
- 提供详细的文档和社区支持，方便用户快速上手。
- 链接: https://github.com/hiyouga/LlamaFactory
- ⭐ 73532 | 🍴 8986 | 语言: Python
- 标签: agent, ai, deepseek, fine-tuning, gemma

### AI-For-Beginners
- 1. **中文简介**：  
   本项目是一个为期12周、包含24课时的AI入门课程，面向零基础学习者，旨在让所有人轻松掌握人工智能基础。课程以Jupyter Notebook形式提供，适合自学或教学使用。

2. **核心功能**：  
   - 提供系统化的AI入门课程体系，涵盖从基础到进阶的知识点。  
   - 使用Jupyter Notebook实现代码与理论结合，支持动手实践。  
   - 覆盖人工智能多个核心领域，如深度学习、计算机视觉和自然语言处理。  
   - 适合初学者快速建立对AI技术的整体认知。  
   - 由微软开发者支持，内容注重实用性和可访问性。

3. **适用场景**：  
   - 高校或培训机构作为AI通识课程的辅助教材。  
   - 自学者通过分阶段学习掌握AI基础技能。  
   - 非技术背景人员了解人工智能基本概念与应用。  
   - 开发者作为补充材料学习特定AI技术（如CNN、RNN等）。

4. **技术亮点**：  
   - 课程结构清晰，分12周24课逐步推进，适合循序渐进学习。  
   - 结合理论讲解与代码实践，强化理解与应用能力。  
   - 涵盖主流AI技术栈，如CNN、RNN、GAN、NLP等，内容全面。  
   - 基于Jupyter Notebook实现，便于本地运行与交互实验。  
   - 面向初学者设计，降低AI学习门槛，提升普及度。
- 链接: https://github.com/microsoft/AI-For-Beginners
- ⭐ 52912 | 🍴 10743 | 语言: Jupyter Notebook
- 标签: ai, artificial-intelligence, cnn, computer-vision, deep-learning

### ai-engineering-from-scratch
- ### 1. 中文简介
该项目旨在从零开始学习和构建人工智能系统，涵盖广泛的主题和工具。它提供了一个全面的教程，帮助开发者掌握AI工程的各个方面，从基础到高级应用。

### 2. 核心功能
- 提供从零开始构建AI系统的全面教程。
- 支持多种编程语言和工具，如Python、Rust和TypeScript。
- 涵盖广泛的主题，包括深度学习、自然语言处理、强化学习和生成式AI。
- 提供详细的代码示例和实战项目，便于学习和实践。

### 3. 适用场景
- 初学者希望系统学习AI工程的基础知识。
- 开发者希望扩展其在AI领域的应用技能，如计算机视觉和NLP。
- 研究人员或工程师希望构建和部署自定义的AI代理和系统。
- 教育机构或培训机构作为AI工程课程的参考材料。

### 4. 技术亮点
- 项目标签丰富，涵盖从基础到高级的多个AI领域，如LLM、Swarm Intelligence和Transformers。
- 支持多种编程语言，满足不同开发者的需求。
- 提供详细的教程和实战项目，便于实践和应用。
- 链接: https://github.com/rohitg00/ai-engineering-from-scratch
- ⭐ 43875 | 🍴 7381 | 语言: Python
- 标签: agents, ai, ai-agents, ai-engineering, computer-vision

### ailearning
- 1. **中文简介**  
   AiLearning是一个涵盖数据分析、机器学习实战、线性代数、PyTorch和NLTK的综合性学习项目，基于Python实现，适合希望系统学习机器学习和深度学习技术的开发者。该项目结合了理论与实践，提供从基础算法到高级模型的完整学习路径。

2. **核心功能**  
   - 提供多种机器学习算法的实现，如Adaboost、Apriori、KMeans和SVM等。  
   - 支持深度学习框架PyTorch和TensorFlow 2.0的实战案例。  
   - 包含自然语言处理（NLP）工具NLTK的相关示例。  
   - 涵盖推荐系统、回归分析和主成分分析（PCA）等实用技术。  
   - 项目代码开源，便于学习和二次开发。

3. **适用场景**  
   - 初学者用于系统学习机器学习和深度学习的理论基础与代码实现。  
   - 数据科学从业者参考实现各类经典算法和模型。  
   - 研究人员探索机器学习在推荐系统和自然语言处理中的应用。  
   - 教育者作为教学材料，辅助机器学习课程的教学与实践。

4. **技术亮点**  
   - 结合理论与实践，提供丰富的代码示例和算法实现。  
   - 覆盖多种主流机器学习框架和工具，如PyTorch、TensorFlow和scikit-learn。  
   - 项目内容全面，从基础算法到高级模型均有涉及。  
   - 开源社区活跃，便于交流和持续更新。
- 链接: https://github.com/apachecn/ailearning
- ⭐ 42417 | 🍴 11530 | 语言: Python
- 标签: adaboost, apriori, deeplearning, dnn, fp-growth

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 描述: 500 AI Machine learning Deep learning Computer vision NLP Projects with code
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35735 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### spaCy
- 描述: 💫 Industrial-strength Natural Language Processing (NLP) in Python
- 链接: https://github.com/explosion/spaCy
- ⭐ 33777 | 🍴 4699 | 语言: Python
- 标签: ai, artificial-intelligence, cython, data-science, deep-learning

### RAG_Techniques
- 描述: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
- 链接: https://github.com/NirDiamant/RAG_Techniques
- ⭐ 28831 | 🍴 3518 | 语言: Jupyter Notebook
- 标签: agentic-rag, ai, embeddings, generative-ai, gpt

### haystack
- 描述: Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.
- 链接: https://github.com/deepset-ai/haystack
- ⭐ 26020 | 🍴 2952 | 语言: Python
- 标签: agent, agents, ai, gemini, generative-ai

### datasets
- 描述: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
- 链接: https://github.com/huggingface/datasets
- ⭐ 21765 | 🍴 3312 | 语言: Python
- 标签: ai, artificial-intelligence, computer-vision, dataset-hub, datasets

## Computer Vision项目

### 500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- 1. **中文简介**：该项目是一个包含500个AI、机器学习、深度学习、计算机视觉和自然语言处理项目的资源库，提供了相关项目的代码和实现。它旨在为开发者、研究人员和爱好者提供一个全面的实践和学习平台。

2. **核心功能**：  
   - 提供500多个AI相关项目的代码示例。  
   - 覆盖机器学习、深度学习、计算机视觉和自然语言处理等多个领域。  
   - 以Python为主要实现语言，适合快速学习和实践。  
   - 项目标签丰富，方便用户按领域查找资源。  

3. **适用场景**：  
   - 初学者通过项目实践快速掌握AI技术。  
   - 开发者寻找灵感或参考代码实现特定功能。  
   - 研究人员快速验证算法或获取开源项目的基础实现。  

4. **技术亮点**：  
   - 项目数量庞大且覆盖广泛，适合不同需求的用户。  
   - 以Python为主，与主流AI框架和工具链兼容。  
   - 标签分类清晰，便于高效筛选和查找特定领域的资源。
- 链接: https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code
- ⭐ 35735 | 🍴 7380 | 语言: 未知
- 标签: artificial-intelligence, artificial-intelligence-projects, awesome, computer-vision, computer-vision-project

### skyvern
- 1. **中文简介**  
Skyvern是一个基于AI的浏览器工作流自动化工具，通过智能技术实现复杂任务的自动化操作。它支持多种浏览器自动化框架，适用于需要人机交互的自动化场景。

2. **核心功能**  
- 使用人工智能驱动浏览器操作，实现端到端自动化。  
- 支持多种浏览器自动化工具（如Playwright、Selenium、Puppeteer）。  
- 通过视觉识别和自然语言理解处理复杂任务。  
- 提供API接口，便于集成到现有工作流中。  
- 支持RPA（机器人流程自动化）场景，提升效率。

3. **适用场景**  
- 自动填写并提交在线表单或完成注册流程。  
- 执行跨平台的网页数据抓取和分析任务。  
- 自动化测试和验证网页应用的功能和性能。  
- 处理需要用户交互的重复性任务（如订单处理）。

4. **技术亮点**  
- 结合大语言模型（LLM）和计算机视觉技术，增强自动化能力。  
- 支持灵活的浏览器引擎选择，适配不同项目需求。  
- 通过AI优化自动化流程，减少人工干预。  
- 提供API接口，便于与其他工具和服务集成。
- 链接: https://github.com/Skyvern-AI/skyvern
- ⭐ 22600 | 🍴 2119 | 语言: Python
- 标签: ai, api, automation, browser, browser-automation

### cvat
- 1. **中文简介**：  
CVAT（Computer Vision Annotation Tool）是一个领先的视觉数据集构建平台，支持图像、视频和3D数据的标注，提供开源、云服务和企业级产品，具备AI辅助标注、质量保证、团队协作、分析及开发者API等功能。

2. **核心功能**：  
- 支持图像、视频和3D数据的多种标注任务（如目标检测、语义分割等）。  
- 提供AI辅助标注功能，提升标注效率与准确性。  
- 支持团队协作与项目管理，便于多人协作完成大规模标注任务。  
- 内置质量保证机制，确保标注数据的一致性与可靠性。  
- 开放开发者API，便于集成到自定义工作流或平台中。

3. **适用场景**：  
- 计算机视觉模型训练前的数据标注（如目标检测、图像分类）。  
- 自动驾驶、机器人感知等需要大量视频或3D数据标注的领域。  
- 科研机构或企业进行大规模数据集构建与管理。  
- 企业级项目需要高安全、可扩展的标注解决方案。

4. **技术亮点**：  
- 基于Python开发，支持多种深度学习框架（如PyTorch、TensorFlow）的数据标注需求。  
- 提供灵活的标注工具与自动化标注结合，显著提升标注效率。  
- 支持多用户协作与版本控制，适合大型项目团队使用。  
- 内置数据分析功能，帮助优化标注流程与数据质量。
- 链接: https://github.com/cvat-ai/cvat
- ⭐ 16389 | 🍴 3776 | 语言: Python
- 标签: annotation, annotation-tool, annotations, boundingbox, computer-vision

### pytorch-grad-cam
- 1. **中文简介**：
   pytorch-grad-cam 是一个用于计算机视觉的高级AI可解释性工具。它支持CNN、视觉Transformer等多种模型，适用于分类、目标检测、分割、图像相似度分析等任务。该项目通过生成类激活图（Grad-CAM）和Score-CAM等方法，提升模型的可解释性。

2. **核心功能**：
   - 支持多种深度学习模型，包括CNN和Vision Transformers。
   - 提供类激活图（Grad-CAM）和Score-CAM等可视化工具。
   - 适用于分类、目标检测、分割等多种计算机视觉任务。
   - 支持图像相似度分析，帮助用户理解模型决策过程。
   - 提供直观的可视化结果，便于分析和调试模型。

3. **适用场景**：
   - 医学影像分析：用于解释医学图像中模型的决策依据，辅助医生诊断。
   - 自动驾驶：帮助理解目标检测模型对道路场景的识别过程。
   - 图像分类：用于解释分类模型对图像类别的判定依据。
   - 图像分割：提供分割结果的可视化工具，便于分析模型的分割精度。

4. **技术亮点**：
   - 提供多种可解释性方法（如Grad-CAM和Score-CAM），满足不同需求。
   - 支持多种深度学习模型框架，具有广泛的适用性。
   - 可视化结果直观，便于用户理解和分析模型决策过程。
- 链接: https://github.com/jacobgil/pytorch-grad-cam
- ⭐ 12930 | 🍴 1707 | 语言: Python
- 标签: class-activation-maps, computer-vision, deep-learning, explainable-ai, explainable-ml

### kornia
- 1. **中文简介**：
   kornia是一个用于空间人工智能的几何计算机视觉库，基于Python和PyTorch构建，提供了一系列强大的计算机视觉和深度学习工具。

2. **核心功能**：
   - 提供丰富的几何变换和图像处理功能。
   - 支持深度学习模型的开发和训练。
   - 与PyTorch无缝集成，方便使用。
   - 适用于机器人和空间人工智能任务。

3. **适用场景**：
   - 机器人视觉导航与定位。
   - 图像处理和特征提取。
   - 深度学习模型中的计算机视觉任务。

4. **技术亮点**：
   - 基于PyTorch，提供高效的计算和灵活的模型构建。
   - 专注于几何计算机视觉，提供专门的工具和算法。
- 链接: https://github.com/kornia/kornia
- ⭐ 11290 | 🍴 1209 | 语言: Python
- 标签: artificial-intelligence, computer-vision, deep-learning, hacktoberfest, image-processing

### ImageAI
- 描述: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities
- 链接: https://github.com/OlafenwaMoses/ImageAI
- ⭐ 8876 | 🍴 2191 | 语言: Python
- 标签: ai-practice-recommendations, algorithm, artificial-intelligence, artificial-neural-networks, densenet

### AliceVision
- 描述: 3D Computer Vision Framework
- 链接: https://github.com/alicevision/AliceVision
- ⭐ 3460 | 🍴 879 | 语言: C++
- 标签: 3d-computer-vision, 3d-reconstruction, ai, alicevision, camera-tracking

### viseron
- 描述: Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor.
- 链接: https://github.com/roflcoopter/viseron
- ⭐ 3300 | 🍴 405 | 语言: Python
- 标签: coral, cuda, darknet, edgetpu, face-recognition

### CVprojects
- 描述: computer vision projects |  计算机视觉相关好玩的AI项目（Python、C++、embedded system）
- 链接: https://github.com/enpeizhao/CVprojects
- ⭐ 2630 | 🍴 692 | 语言: Jupyter Notebook
- 标签: computer-vision, cpp, cuda, deep-learning, embedded-systems

### MLE-Flashcards
- 描述: 200+ detailed flashcards useful for reviewing topics in machine learning, computer vision, and computer science.
- 链接: https://github.com/b7leung/MLE-Flashcards
- ⭐ 2430 | 🍴 218 | 语言: 未知
- 标签: ai, artificial-intelligence, computer-science, computer-vision, flashcards

## AI工具和库

### openclaw
- 1. **中文简介**  
openclaw是一款个人AI助手，支持任意操作系统和平台，强调数据自主性和灵活性。它旨在为用户提供个性化、本地化的AI服务，确保用户对自己的数据拥有完全控制权。

2. **核心功能**  
- 支持多平台部署，可在任何操作系统上运行。  
- 提供本地化AI助手，保障用户数据隐私和自主权。  
- 基于TypeScript开发，具备良好的可扩展性和兼容性。  
- 强调“龙虾式”设计理念，追求高效和灵活。  

3. **适用场景**  
- 个人用户需要本地化AI助手以提升隐私和数据安全性。  
- 开发者希望基于TypeScript构建可跨平台的AI应用。  
- 企业需要定制化的AI解决方案，同时保障数据自主权。  

4. **技术亮点**  
- 使用TypeScript编写，具备强类型系统和现代化开发特性。  
- 支持任意操作系统和平台，具备高灵活性。  
- 强调“own-your-data”理念，突出数据自主性。
- 链接: https://github.com/openclaw/openclaw
- ⭐ 384256 | 🍴 80730 | 语言: TypeScript
- 标签: ai, assistant, crustacean, molty, openclaw

### superpowers
- **1. 中文简介**  
Superpowers是一个实用的智能技能框架与软件开发方法论，专注于通过代理驱动的方式提升开发效率和团队协作能力。它结合人工智能与结构化流程，帮助开发者更系统化地管理复杂项目。

**2. 核心功能**  
- 提供基于代理的技能框架，支持多角色协同开发。  
- 整合头脑风暴与编码流程，优化需求分析与实现效率。  
- 采用子代理驱动开发模式，提升任务分解与执行精度。  
- 适用于敏捷开发流程，增强团队协作与版本管理能力。  
- 支持持续集成与交付，加速软件开发生命周期。

**3. 适用场景**  
- 大型团队协作的软件开发项目，需要高效任务分配与进度管理。  
- 需要快速原型设计与迭代的产品开发场景。  
- 结合人工智能技术的项目，如智能代理或自动化系统开发。  
- 教育或培训场景，用于演示结构化开发流程与团队协作。

**4. 技术亮点**  
- 采用子代理驱动开发模式，提升任务执行与管理的自动化水平。  
- 结合AI技能框架，增强需求分析与代码生成的智能化能力。  
- 支持Shell脚本开发，便于快速集成与部署。  
- 标签覆盖广泛，包括AI、头脑风暴、编码、SDLC等，体现多功能性与灵活性。
- 链接: https://github.com/obra/superpowers
- ⭐ 261682 | 🍴 23367 | 语言: Shell
- 标签: ai, brainstorming, coding, obra, sdlc

### hermes-agent
- 1. **中文简介**：
   *   **项目描述**：这是一个能够随着用户成长而进化的智能代理程序，旨在提供个性化的辅助体验。
   *   **项目背景**：该项目由 Nous Research 开发，属于一个旨在构建下一代 AI 代理的生态系统，支持多种大型语言模型。

2. **核心功能**：
   *   能够根据用户的长期交互和反馈不断学习和优化自身行为。
   *   支持接入多种主流大语言模型（如 Claude、OpenAI、Codex 等）作为其核心大脑。
   *   具备代码执行与解释能力，能够直接运行 Python 代码并处理相关任务。
   *   拥有记忆库（ClawDBot），可以存储和检索历史对话及知识。

3. **适用场景**：
   *   **个性化编程助手**：作为开发者的智能搭档，辅助编写、调试和解释代码片段。
   *   **自动化任务代理**：执行需要多步推理和记忆能力的复杂日常任务或研究分析。
   *   **AI 研究与实验**：用于测试不同大模型在代理架构下的表现及进化能力。

4. **技术亮点**：
   *   **多模型兼容性**：通过抽象层设计，灵活适配 Anthropic、OpenAI 等不同厂商的 API。
   *   **进化式架构**：强调代理的自我迭代能力，使其能随使用频率增加而变得更“聪明”。
- 链接: https://github.com/NousResearch/hermes-agent
- ⭐ 221030 | 🍴 42161 | 语言: Python
- 标签: ai, ai-agent, ai-agents, anthropic, chatgpt

### n8n
- 1. **中文简介**
   n8n是一个公平代码的工作流自动化平台，具有原生AI能力。它结合了可视化构建与自定义代码，支持自托管或云端部署，提供400多种集成选项。

2. **核心功能**
   - 提供可视化工作流构建工具，简化自动化流程设计。
   - 支持自定义代码扩展，满足高级用户需求。
   - 提供多种集成选项，连接不同的应用和服务。
   - 支持自托管和云端部署，灵活适应不同需求。
   - 集成AI能力，提升自动化任务的智能处理能力。

3. **适用场景**
   - 企业数据同步和自动化处理。
   - 多平台消息通知和任务管理。
   - 复杂工作流的自动化编排和执行。
   - 自定义业务逻辑的自动化实现。

4. **技术亮点**
   - 使用TypeScript开发，确保代码质量和可维护性。
   - 提供丰富的API和CLI工具，方便扩展和集成。
   - 支持低代码和无代码开发，降低使用门槛。
   - 原生集成AI能力，提升自动化任务的智能水平。
- 链接: https://github.com/n8n-io/n8n
- ⭐ 198143 | 🍴 59654 | 语言: TypeScript
- 标签: ai, apis, automation, cli, data-flow

### AutoGPT
- 1. **中文简介**
   AutoGPT 是面向每个人的可访问 AI 愿景，旨在使用并构建于其上。我们的使命是提供工具，让你专注于重要的事情。

2. **核心功能**
   - 提供易于使用的工具，让用户能够专注于核心任务。
   - 支持多种人工智能模型和 API，如 GPT、Claude 和 Llama。
   - 通过自主代理实现自动化任务处理。
   - 易于扩展和定制，适合各种应用场景。
   - 基于 Python 开发，易于集成和二次开发。

3. **适用场景**
   - 自动化日常任务，如数据整理和报告生成。
   - 人工智能研究和开发中的实验和原型设计。
   - 客户服务中的自动化回复和处理。
   - 企业内部流程优化和自动化。

4. **技术亮点**
   - 支持多种大语言模型（LLM）和 API，提供灵活的集成选项。
   - 基于 Python，便于开发者进行二次开发和扩展。
   - 通过自主代理实现任务的自动化处理，提高效率和准确性。
- 链接: https://github.com/Significant-Gravitas/AutoGPT
- ⭐ 185704 | 🍴 46068 | 语言: Python
- 标签: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents

### prompts.chat
- 描述: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- 链接: https://github.com/f/prompts.chat
- ⭐ 166405 | 🍴 21496 | 语言: HTML
- 标签: ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts

### stable-diffusion-webui
- 描述: Stable Diffusion web UI
- 链接: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ⭐ 164279 | 🍴 30447 | 语言: Python
- 标签: ai, ai-art, deep-learning, diffusion, gradio

### JavaGuide
- 描述: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- 链接: https://github.com/Snailclimb/JavaGuide
- ⭐ 157322 | 🍴 46184 | 语言: JavaScript
- 标签: agent, ai, context-engineering, deepseek, interview

### firecrawl
- 描述: The API to search, scrape, and interact with the web at scale. 🔥
- 链接: https://github.com/firecrawl/firecrawl
- ⭐ 156549 | 🍴 8900 | 语言: TypeScript
- 标签: ai, ai-agents, ai-crawler, ai-scraping, ai-search

### langflow
- 描述: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- 链接: https://github.com/langflow-ai/langflow
- ⭐ 152453 | 🍴 9663 | 语言: Python
- 标签: agents, chatgpt, generative-ai, large-language-models, multiagent

