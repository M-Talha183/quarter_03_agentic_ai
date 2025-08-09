import os 
from agents import Agent , OpenAIChatCompletionsModel , Runner , set_tracing_disabled 
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