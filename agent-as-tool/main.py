from connection import config
from agents import Agent , Runner

itelian_agent = Agent(
    name = "italian Translator",
    instructions = "Translite any english text into italian "
)

spenish_agent = Agent(
    name = "spenish Translator",
    instructions = "Translite any english text into spenish "
)


french_agent = Agent(
    name = "french Translator",
    instructions = "Translite any english text into french "
)

translation_router = Agent(
    name = "translator",
    instructions="""
    you are the translation assistant . Route the translation request to the correct languge use the 
    approprite tool to convert English text into either Itlain , spanish , or french 
    """,
    tools = [itelian_agent.as_tool(
        tool_name = "translate_to_itlain",
        tool_description = "Translate the user message into itlain "
    ),
     spenish_agent.as_tool(
        tool_name = "translate_to_spenish",
        tool_description = "Translate the user message into spenish "
    ),
     french_agent.as_tool(
        tool_name = "translate_to_french",
        tool_description = "Translate the user message into french "
    ),
             
             ]
)


result = Runner.run_sync(
    translation_router,
    "Traslate ' I love learning ' into itlain  ",
    run_config  =config
)

print(result.final_output)
print(result.final_output)
print(result.final_output)