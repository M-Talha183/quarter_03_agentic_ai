
---

## **class04/notes.md**
```markdown
# Class 04 — Detailed Notes

## 1. Topic: Output Types (`output_type` Parameter)

### What is it?
By default, an agent's output is just a string (plain text).  
If we need structured, typed output, we can define a Python type and set it as the `output_type` in our `Agent` definition.

### Supported Output Types
- **Dataclasses** (Python's built-in)
- **Pydantic models** (v2+)
- **Lists** and `TypedDict`
- Any type that works with `pydantic.TypeAdapter`

---

## 2. Why Use Output Types?
- **Validation**: Ensures the output matches the required format.
- **Parsing**: Makes it easier to consume results in applications.
- **Integration**: Ideal when the AI result needs to be stored in a database or passed to another system.

---

## 3. How It Works
1. Define your output type (e.g., dataclass).
2. Pass it to the `output_type` parameter of `Agent`.
3. The agent will return the response in that structured form.

---

## 4. Code Example

------> teacher.py


## ===> Tools Exaple Code 

from agents import (
    Runner,
    Agent,
    enable_verbose_stdout_logging,
    set_tracing_disabled,
    function_tool,
    OpenAIChatCompletionsModel,
    RunConfig
)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
set_tracing_disabled(True)
# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Model provider setup
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

config = RunConfig(
    model=model,
    model_provider=provider
)

enable_verbose_stdout_logging()

# Tool definition
@function_tool
def add(n1: int, n2: int) -> str:
    """
    Adds two integers.
    
    Args:
        n1 (int): First integer.
        n2 (int): Second integer.
    
    Returns:
        str: Sum of n1 and n2.
    """
    return f"Your Answer is: {n1 + n2}"

# Agent setup
math_teacher = Agent(
    name="Talha",
    instructions="You are a helpful math teacher",
    model=model,
    tools=[add],
)

# Run agent
res = Runner.run_sync(
    starting_agent=math_teacher,
    input="what is 5 + 3?",
    run_config=config
)

print(res.final_output)
