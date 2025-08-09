from agents import Agent , set_tracing_disabled ,enable_verbose_stdout_logging
from tools import add, subtract, multiply
from agent_config import config



math_teacher = Agent(
    name= "Talha ",
    instructions="You are Helpful math teacher",
    tools=[add,subtract,multiply],
     model=config,
)

