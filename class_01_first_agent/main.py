# import os 
# from agents import Agent , Runner , OpenAIChatCompletionsModel ,RunConfig
# from openai import AsyncOpenAI
# from dotenv import load_dotenv

# load_dotenv()
# Gemeni_api_key = os.getenv("GEMINI_API_KEY")

# if not Gemeni_api_key:
#     raise ValueError ("GEmini Api key does not work please reset it ")

# external_client = AsyncOpenAI(
#     api_key=Gemeni_api_key,
#     base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )
# config = RunConfig(
#     model=model,
#     tracing_disabled=True
# )

# agent = Agent(
#     name="Python Expert",
#     instructions="Your Goals is help peoples in python related question , code , debuging bast practices also Teaching ",
# )


# prompt = "what is python "

# response = Runner.run_sync(
#     starting_agent=agent,
#     input=prompt,
#     run_config=config
# )

# print(response.final_output)


from agents import Agent , Runner , OpenAIChatCompletionsModel , RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os 

#  Loading the envirnmental variable 
load_dotenv()

#  Which LLM provider to use 
external_client : AsyncOpenAI = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#  Which LLM model to use 
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# creating_agent = Agent (
#     name = "Python Expert Agent",
#     instructions = "Your goal is to assist users with python related question and provide solution with one example ,"
# )

# input_prompt = input("Enter your question: ")

# result = Runner.run_sync(
#     starting_agent=creating_agent,
#     input=input_prompt,
#     run_config=RunConfig(model=llm_model, tracing_disabled=True)
# )
# print("Response from the agent:")
# print(result.final_output)

# New agent can be created with different instructions or name
# For example:
agent_level = Agent(
    name = "Advanced Python Expert Agent",
    instructions = "Your goal is to assist users with advanced python related question and provide solution with one example ,",
    model=llm_model
)
input_prompt_level = input("Enter your advanced question: ")            
result_level = Runner.run_sync(
    starting_agent=agent_level,
    input=input_prompt_level,
)
print("Response from the advanced agent:")
print(result_level.final_output)