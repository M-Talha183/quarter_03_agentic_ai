import os 
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent , RunConfig , Runner , OpenAIChatCompletionsModel ,set_tracing_disabled

load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KET")

if not gemini_api_key :
    raise ValueError("Gimini api key is not sset ! Please set first it ")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client=provider
)
config =  RunConfig(
    model=model,
    model_provider=provider # type:ignore
)