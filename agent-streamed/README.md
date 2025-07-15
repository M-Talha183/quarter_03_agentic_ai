# 🧠 Agent with Streaming Responses using OpenAI SDK & Chainlit

## 🚀 Overview

This project implements an **agent-based conversational system** that supports **real-time streaming responses (token-by-token generation)**.

It uses:

- **Chainlit** for interactive front-end  
- **OpenAI SDK (Async)** for calling LLMs with streaming outputs  
- **Agentic AI structure** to handle **chat history, instructions, and memory**  

---

## 🛠️ Features

- ✅ **Token Streaming** for fast, real-time responses  
- ✅ **Agent-based context management**  
- ✅ **Chainlit interactive chat interface**  
- ✅ **LLM agnostic**: Supports OpenAI, Gemini (via OpenAI-compatible proxy), Claude, etc.

---

## 📦 Tech Stack

- **Python**  
- **Chainlit**  
- **OpenAI SDK (AsyncOpenAI)**  
- **Agentic AI Framework (custom agents + runner)**  
- **Dotenv for environment configs**

---

## 🔧 Setup

### 1️⃣ Install dependencies:

```bash
pip install chainlit openai python-dotenv
