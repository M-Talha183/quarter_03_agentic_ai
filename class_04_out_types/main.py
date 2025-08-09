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
