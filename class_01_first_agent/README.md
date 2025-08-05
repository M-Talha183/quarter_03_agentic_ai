# 🧠 Class 01 – First Agent with OpenAI Agents SDK & Gemini API

Welcome to **Class 01** of the `quarter_03_agentic_ai` journey!  
In this session, we created our **very first agent** using the **OpenAI Agents SDK**, but with a twist — we used **Gemini API** as the LLM backend instead of OpenAI’s models.

This marks the starting point of building real **agentic AI systems** using custom models, tools, and configurations. 🚀

---

## 🛠️ What We Did

- Set up a fresh project using [`uv`]
- Installed required packages:  
  - `openai-agents`
  - `python-dotenv`
- Loaded **Gemini API key** from a `.env` file.
- Configured `AsyncOpenAI` with Gemini endpoint.
- Created a custom **Agent** with helpful Python-related instructions.
- Ran a prompt through the agent using the `Runner` and printed the response.

---

## 📦 Installation

1. Initialize project using `uv`:

```bash
uv venv
uv pip install openai-agents python-dotenv

2. Run Project using uv 

*** uv run main.py****



🎯 Learning Goals
✅ Learn how to configure the OpenAI SDK to work with external models (Gemini in this case).

✅ Understand how to build a basic agent using instructions and run it with a prompt.

✅ Get hands-on experience with .env for secure API key handling.

✅ Use Runner and RunConfig for agent execution.

