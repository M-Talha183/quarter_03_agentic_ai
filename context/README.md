# 🧠 Context Management – Agents SDK (Class 04)

This folder demonstrates **context management** in the Agents SDK, showing how to pass local data and dependencies to your agent’s tools and lifecycle hooks without exposing them to the LLM.

---

## 📚 What We Learned in Class 04

### Two Types of Context

| Type | Description |
|------|-------------|
| **Local Context** | Data & dependencies available *only* in Python (not visible to LLMs). Passed to tools, callbacks, and hooks via `RunContextWrapper`. |
| **Agent / LLM Context** | Data visible to the LLM during generation. Controlled by system prompts, input messages, and tools. |

---

## 🛠 Local Context

Local context is represented by:

- **`RunContextWrapper[T]`** → Wraps your custom context object (T = type of your data).
- **`context` property** → Access your data inside tools and hooks.
- **Same type rule** → All agents, tools, and hooks for a run must use the same context object type.

✅ **Common Uses:**
- Store user profile info (username, age, role, etc.)
- Pass dependencies (e.g., loggers, database clients)
- Share helper functions across tools

⚠ **Note:** Local context is **never sent** to the LLM.

---

## 🧠 Agent / LLM Context

This is the data that the **LLM actually sees** during generation.  
Ways to add it:

1. **System Prompt (`instructions`)** – Static or dynamic instructions.  
   Example: Always tell the LLM the user’s name.
2. **Input Messages** – Pass relevant details in the `input` parameter to `Runner.run`.
3. **Function Tools** – Let the LLM call tools to fetch data on demand.
4. **Retrieval / Web Search** – Fetch from knowledge bases or the internet.

---

## 📂 Project Structure

```bash
context/
├── my_agent.py        # Config and setup
├── main.py            # Context management example (this file)
└── README.md         

🔍 How This Works
User_Info Dataclass – Stores local user data.

get_user_age Tool – Reads the age from local context.

Dynamic Instructions – Personalize the system prompt with local context data.

Runner.run_sync – Passes the local context object to the agent run.


📓 Class Summary (Class 03 – Context Management)
Topic	Description
Local Context	Pass data to tools without exposing to LLM
Agent Context	Information visible to the model via prompts
Dynamic Instructions	Customize system prompts based on context
Context Wrapper	Provides safe, typed access to local data
