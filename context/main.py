from my_agent import config
from agents import Agent ,Runner
import asyncio


agent = Agent(
    name="PoliteAssistant",
    instructions="User name is M-Talha always polite and in Every responce called M-Talha"
)
user_input = input("Ask me any thing i am PoliteAssistent : ")
async def main ():
    result = await Runner.run(
        starting_agent=agent,
        input= user_input,
        run_config=config
    )
    
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())