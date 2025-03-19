# AI Chatbot

![AI Chatbot Screenshot](https://via.placeholder.com/800x400.png?text=AI+Chatbot+Screenshot)

一个基于Flask和OpenAI的AI聊天机器人，提供智能对话功能。

## 功能特点

- 🗣️ 自然语言对话
- 🧠 基于GPT-3.5-turbo模型
- 🎨 简洁美观的Web界面
- ⚙️ 易于部署和使用

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境变量
在`.env`文件中设置你的OpenAI API密钥：
```
OPENAI_API_KEY=your-api-key-here
```

### 3. 运行应用
```bash
python app.py
```

### 4. 访问应用
打开浏览器访问 [http://localhost:5000](http://localhost:5000)

## 项目结构

```
ai-chatbot/
├── app.py              # 主应用文件
├── requirements.txt    # 依赖文件
├── .env                # 环境变量配置
├── templates/          # HTML模板
│   └── index.html      # 聊天界面
└── README.md           # 项目文档
```

## 贡献指南

欢迎提交Pull Request或Issue来改进本项目！

## 许可证

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件
