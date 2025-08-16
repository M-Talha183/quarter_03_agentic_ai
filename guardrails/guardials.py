import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (Agent , OpenAIChatCompletionsModel
                    , Runner , set_tracing_export_api_key,
                    GuardrailFunctionOutput,
                    input_guardrail,RunContextWrapper,
                    InputGuardrailTripwireTriggered, 
                    
)
from pydantic import BaseModel
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
open_ai_api_key = os.getenv("OPEN_AI_API_KEY")

set_tracing_export_api_key(open_ai_api_key)

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

# define is agent related query schema 

class MY_Data_out_put (BaseModel):
    is_hotel_sanata_query : bool
    reason : str 
     
# guardial AGENT 
Guardial_agent = Agent(
    name = "Guardial Agent",
    instructions="""Check Hotel sanata queries and provide relevant information.
""",
    model=model,
    output_type= MY_Data_out_put
)

# guardial function who checks the user input 

@input_guardrail
async def guardial_function(ctx:RunContextWrapper,agent,input) :
    res = await Runner.run(starting_agent=Guardial_agent,input=input ,context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info = res.final_output ,
        tripwire_triggered=  res.final_output.is_hotel_sanata_query,
    )
# hotel assistant MAIN AGENT 
hotel_assistant = Agent(
    name="hotel_assistant",
    instructions="""
    You are a helpful Hotels sanata Customer care assisitant , Your name is talha 
    - Hotel Sanata owner name is MR Zain 
    - Hotel sananta total rooms is 200
    - 20 rooms are not available for publicaly it only for special guest 
    """,
    model=model,
    input_guardrails=[guardial_function]
)

try:
    res = Runner.run_sync(
    starting_agent=hotel_assistant,
    input="Hello , how many rooms in hotal saa  "
    
    )
    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(f"Tripwire triggered: {e}")