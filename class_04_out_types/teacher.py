from agents import Agent , Runner , enable_verbose_stdout_logging, set_tracing_disabled
from agent_config import config
from dataclasses import dataclass
from tools import add, subtract, multiply

enable_verbose_stdout_logging()
set_tracing_disabled(True)
@dataclass
class Teacher:
    """
    A simple data structure for holding two numbers
    and the result of a mathematical operation.
    """
    n1: int
    n2: int
    result: str

teacher = Agent(
    name = "Teacher",
    instructions="You are a helpful teacher ",
    output_type=Teacher,
    tools=[add,subtract,multiply]
)

res = Runner.run_sync(
    starting_agent=teacher,
    input="What is the result of 2 + 2?",
    run_config=config
)
print(res.final_output)