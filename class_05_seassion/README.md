# Agents SDK – SQLite Session Memory Example

## Overview
The **Agents SDK** provides built-in session memory to automatically maintain conversation history across multiple agent runs, eliminating the need to manually handle `.to_input_list()` between turns.  

By using **SQLiteSession**, you can store and retrieve conversation history for specific sessions, enabling context persistence in multi-turn conversations such as chatbots, virtual assistants, and support systems.

---

## Features
- **Automatic Conversation Memory** – No need to manually manage conversation context.
- **SQLite Storage** – Local persistent database for storing session data.
- **Multiple Sessions** – Manage multiple user or thread sessions in one database.
- **Custom Session IDs** – Name sessions meaningfully for easy management:
  - **User-based**: `user_12345`
  - **Thread-based**: `thread_abc123`
  - **Context-based**: `support_ticket_456`

---

## Example: Multiple Sessions
```python
session_1 = SQLiteSession("user_123", "conversations.db")
session_2 = SQLiteSession("user_456", "conversations.db")

Project Setup
1️⃣ Install Dependencies
pip install agents-sdk openai python-dotenv

2️⃣ Set Environment Variable

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here

How It Works

SQLiteSession stores conversation history in a conversation.db file.

The session ID (user_1) is used to track the user's conversation context.

Every new input is processed while remembering previous turns.

Exiting the loop keeps the history stored for future sessions.

Use Cases

Chat applications

Customer support agents

Personal AI assistants

Any multi-turn conversational system