# AI技术知识库Agent系统

一个基于Agent + RAG架构的AI技术知识库系统，能够用RAG回答技术问题，调用工具完成计算/搜索等任务，并通过API与简单前端对外提供服务。

## 功能特性

- **技术问题回答**：使用RAG技术回答技术问题，如Transformer、PyTorch、深度学习等概念
- **计算功能**：支持基本的数学计算
- **API服务**：通过FastAPI提供聊天接口
- **前端界面**：使用Streamlit构建简单的前端界面

## 项目结构

```
├── agent/          # Agent逻辑
├── model/          # LLM模型
├── rag/            # RAG相关代码
├── service/        # API服务
├── tools/          # 工具函数
├── frontend/       # 前端界面
└── requirements.txt # 依赖文件
```

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动API服务：
   ```bash
   python service/api_server.py
   ```

3. 启动前端：
   ```bash
   streamlit run frontend/app.py
   ```

4. 访问前端：
   打开浏览器，访问 http://localhost:8502

## 示例问题

- 什么是Transformer？
- 345*678是多少？
- 总结一下AI创业趋势

## 技术栈

- Python
- FastAPI
- Streamlit
- FAISS
- Sentence-transformers
- Transformers