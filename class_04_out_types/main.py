from agents import Runner, set_tracing_disabled
from agent.math_agent import agent

# set_tracing_disabled(True)

# res = Runner.run_sync(
#     starting_agent=agent,
#     input="what is 2 + 2?",
# )

# print(res.final_output)
if __name__ == "__main__":
    res = Runner.run_sync(
        starting_agent=agent,
        input="what is 2 + 2?",
        # run_config=config
    )
    print(res.final_output)
