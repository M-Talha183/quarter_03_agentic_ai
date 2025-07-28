from my_agent import config
from agents import Agent ,Runner , function_tool ,RunContextWrapper
import asyncio
from dataclasses import dataclass

@dataclass
class User_Info :
    name : str
    uid : int
    
@function_tool 
async def fetch_user_age(wrapper : RunContextWrapper[User_Info]):
    return f"User {wrapper.context.name} is 25 years old"


user_input = input("Ask me any thing i am PoliteAssistent : ")

async def main():
    user_info = User_Info(name="M-Talha",uid=20)
    
    agent = Agent [User_Info](
    name="PoliteAssistant",
    instructions=" always polite and in Every responce also use the fetch_user_age tool to give the answer of the user  ",
    tools=[fetch_user_age]
)
    result = await Runner.run(
        starting_agent=agent,
        input=user_input,
        context=user_info,
        run_config=config
    )
    
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())