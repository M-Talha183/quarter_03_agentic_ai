import os 
from agents import Agent , Runner , OpenAIChatCompletionsModel ,RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
Gemeni_api_key = os.getenv("GEMINI_API_KEY")

if not Gemeni_api_key:
    raise ValueError ("GEmini Api key does not work please reset it ")

external_client = AsyncOpenAI(
    api_key=Gemeni_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
config = RunConfig(
    model=model,
    tracing_disabled=True
)

agent = Agent(
    name="Python Expert",
    instructions="Your Goals is help peoples in python related question , code , debuging bast practices also Teaching ",
)


prompt = "what is python "

response = Runner.run_sync(
    starting_agent=agent,
    input=prompt,
    run_config=config
)

print(response.final_output)
