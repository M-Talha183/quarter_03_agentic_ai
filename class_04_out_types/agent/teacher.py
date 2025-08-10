from agents import Agent , Runner , enable_verbose_stdout_logging, set_tracing_disabled
import agent_config as ac
from dataclasses import dataclass
from tools.custom_tool import add, subtract, multiply
from tools.user_data import fetch_user_data

@dataclass
class Teacher:
    """
    A simple data structure for holding two numbers
    and the result of a mathematical operation.
    """
    n1: int
    n2: int
    result: str

teacher_agent = Agent(
    name = "Teacher",
    instructions="You are a helpful assistant ",
    # model= config.model,
    tools=[fetch_user_data]
)

