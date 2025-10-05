import os 
from agents import Agent, OpenAIChatCompletionsModel , Runner , RunConfig , enable_verbose_stdout_logging
from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents import FunctionTool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
# enable_verbose_stdout_logging()

provider = AsyncOpenAI(
    api_key= gemini_api_key ,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = provider
)

# sub = input("Enter your subject: ")
# def prompt (ctx, agent):
#     if sub == "python":
#         return f"you are the python  programming language specialist agent where you help yous users"
#     elif sub == "java":
#         return f"you are the java programming language specialist agent where you help yous users"
#     else:
#         return f"you are a general programming language specialist agent where you help yous users"
    
schema= {
    "additionalProperties": False,
    "type": "object",
    "properties": {
       "city":{"type":"string"},
    },
    "required": []
}
async def weather (ctx,city):
    return f"The weather in {city} is 25 degree celcius"

weather_tool = FunctionTool(
    name = "get_weather",
    description = "get the weather of a city",
    params_json_schema= schema,
    on_invoke_tool=weather
) 
main_agent = Agent (
    name = "orchestration Main Agent ",
    instructions = "you are helpful assistant ",
    tools = [weather_tool],
    model=model
)
result = Runner.run_sync(
    starting_agent = main_agent,    
    input = "what is the wearther of karachi ?",
)
print(result.final_output)