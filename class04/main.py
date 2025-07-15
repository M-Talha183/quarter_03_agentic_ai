from dotenv import load_dotenv
from agents import Agent , Runner , AsyncOpenAI , OpenAIChatCompletionsModel  # type: ignore
import os 
load_dotenv()

genini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key= genini_api_key,
    base_url= ""
)
