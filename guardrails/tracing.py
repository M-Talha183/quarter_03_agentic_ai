import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent , OpenAIChatCompletionsModel , Runner , set_tracing_export_api_key

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
# open_ai_api_key = os.getenv("OPEN_AI_API_KEY")

# set_tracing_export_api_key(open_ai_api_key)

if not gemini_api_key:
    raise ValueError("Gemini api key can work please check it ")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client=provider
)

agent = Agent (
    name = "Help ful agent",
    instructions="You are a helpful assistant.",
    model=model
)

result = Runner.run_sync(
    starting_agent=agent,
    input= "What is the capital of France?"
)
print(result.final_output)