# 🛒 Multi-Agent E-Commerce AI System

## Overview

A modular AI system for automating e-commerce tasks using specialized agents powered by OpenAI + Chainlit.

### 🔧 Features:

- **Product Research Agent** – Finds trending products & suppliers
- **Store Design Agent** – Helps with web store UX/UI and content
- **Ad Copywriter Agent** – Writes marketing copy for ads
- **E-Commerce Knowledge Agent** – Answers basic "What is e-commerce?" questions
- **Controller Agent** – Routes tasks intelligently between agents

---

## 🧠 How It Works

1️⃣ User sends input  
2️⃣ Controller Agent classifies the task  
3️⃣ Correct expert agent handles the request  
4️⃣ Response sent back via Chainlit

---

## 💻 Tech Stack

- OpenAI `agents` (UV SDK)  
- Chainlit for chat interface  
- Python (async)  
- OpenAI Function Calling  

---

## 🚀 Run the Project

```bash
uv add openai-agents
uv add chainlit

chainlit run my_agent.py -w
