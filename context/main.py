from my_agent import config
from agents import Agent ,Runner, function_tool , RunContextWrapper
from dataclasses import dataclass


@dataclass
class User_Info:
    name : str
    age: str
    role : str

user_1 = User_Info(name="Talha",age="20",role="student")


@function_tool
def get_user_age(ctx:RunContextWrapper[User_Info]):
    """Age Function"""
    print("Age tool ------> ")
    print("ctx ====> ")
    return f"your  Age is {ctx.context.age}"



def dynamic_instruction (ctx:RunContextWrapper[User_Info] , agent:Agent[User_Info]):
   return f"User Name is {ctx.context.name} you are a helpful Assistant"    
    

agent = Agent[User_Info](
    name="Assistant",
    instructions=dynamic_instruction,
    tools=[get_user_age]
)




res = Runner.run_sync(
        starting_agent=agent,
        input="what is sge of user",
        context=user_1,
        run_config=config
    )
print(res.final_output)
    

