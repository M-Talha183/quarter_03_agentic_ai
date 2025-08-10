from agents import Agent
from tools.custom_tool import add, subtract, multiply
from agent_config import config

math_teacher = Agent(
    name="Talha",
    instructions="You are a helpful math teacher.",
    model=config.model,
    tools=[add],
)

agent = Agent(
    name="Zain",
    instructions="You are a helpful math assistant.",
    model=config.model,
    tools=[
        math_teacher.as_tool(
            tool_name="math_teacher",
            tool_description="A math teacher who can perform basic arithmetic operations like addition, subtraction, and multiplication."
        )
    ],
    tool_use_behavior="stop_on_first_tool"
)
