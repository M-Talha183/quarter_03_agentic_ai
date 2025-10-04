# import os 
# from agents import Agent , OpenAIChatCompletionsModel , Runner , set_tracing_disabled 
# from openai import AsyncOpenAI
# from dotenv import load_dotenv

# load_dotenv()
# set_tracing_disabled(True)

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# provider = AsyncOpenAI(
#     api_key= gemini_api_key ,
#     base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model= "gemini-2.0-flash",
#     openai_client = provider
# )

# main_agent = Agent (
#     name = "Python expert ",
#     instructions= " You are a Python expert. You will be given a question and you have to answer it using python code. If you need to run code, use the `python` tool. If you need to run shell commands, use the `bash` tool. Always use the `python` tool to check your work. Never use the `bash` tool to write or run python code. Always think step by step and be as detailed as possible in your reasoning. ",
#     model= model,
# )

# runner = Runner.run_sync(
#     starting_agent= main_agent,
#     input="Write a python function that takes a list of numbers and returns the sum of the squares of the even numbers in the list. Then run the function with the input [1, 2, 3, 4, 5, 6] and return the result.",
   
# )
# print(runner.final_output)

import os 
from agents import Agent, OpenAIChatCompletionsModel , Runner , RunConfig , enable_verbose_stdout_logging
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
enable_verbose_stdout_logging()

provider = AsyncOpenAI(
    api_key= gemini_api_key ,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = provider
)

config = RunConfig(
    model=model,
    model_provider=provider #type:ignore
)

web_search_agent = Agent (
    name = "web Search Agent ",
    instructions= "you perform web search and return the results ",
    model=model
)
data_analysis_agent = Agent (
    name = "data Analysis Agent ",
    instructions = "you analyze the topic related information and key insights ",
    model=model
)
report_generation_agent = Agent (
    name = "report Generation Agent ",
    instructions = "you generate a report based on the analysis ",
    model=model
)


# main_agent = Agent (
#     name = "orchestration Main Agent ",
#     instructions= "You are helpful assistant ",
    
# )

# result = Runner.run_sync(
#     starting_agent = main_agent,
#     input = "Hello, how are you?",
# ) 

# print(result.final_output)

WEB_SEARCH_OUTPUT = Runner.run_sync(
    starting_agent=web_search_agent,
    input="tell me about LLM "
)
data_analysis_output = Runner.run_sync(
    starting_agent=data_analysis_agent,
    input=f"Analyze this {WEB_SEARCH_OUTPUT.final_output}"
)
report_generation_agent_output = Runner.run_sync(
    starting_agent=report_generation_agent,
    input=f"Write the final report on the base on this Analysis : {data_analysis_output.final_output}"
)

print(report_generation_agent_output.final_output)