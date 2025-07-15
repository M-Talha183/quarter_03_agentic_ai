# 🧠 Streaming Agent with OpenAI SDK & Chainlit

## 🚀 Overview

This project implements a **real-time streaming AI agent** using:

- **Chainlit** for interactive chat UI  
- **OpenAI SDK** (Async client)  
- **Agentic AI framework** for context and memory management  
- **Token-level streaming outputs** for faster response

Supports **custom LLMs via OpenAI-compatible endpoints** (e.g., Gemini proxy, Claude, Llama through Groq/TogetherAI)

---

## 🛠️ Features

- ✅ **Streaming token-by-token responses**  
- ✅ **Agentic design (stateful conversations, chat history)**  
- ✅ **Chainlit-based front-end**  
- ✅ **Async OpenAI API usage**  
- ✅ **Easily pluggable with other LLMs via OpenAI-compatible APIs**

---

## 📦 Tech Stack

- **Python**  
- **Chainlit**  
- **OpenAI SDK (AsyncOpenAI)**  
- **Agentic Framework / Runner**  
- **Dotenv for config management**

---

## 🔧 Setup

### 1️⃣ Install dependencies:

```bash
pip install chainlit openai python-dotenv
