import os 
from agents import Agent , SQLiteSession ,OpenAIChatCompletionsModel , Runner , set_tracing_disabled  
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key= gemini_api_key ,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = provider
)

agent = Agent(
    name = "Assistant",
    model = model,
    instructions="You are a helpful assistant. Answer questions to the best of your ability.",
)
session = SQLiteSession("user_1","conversation.db")
while True: 
    
    user_input = input("write prompt here  : ")
    
    if user_input == "exit":
        break
    result = Runner.run_sync(
    starting_agent=agent,
    input=user_input,
    session=session,
    )

    print(result.final_output)
