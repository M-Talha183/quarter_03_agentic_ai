from dotenv import load_dotenv
from agents import (Agent , 
                    OpenAIChatCompletionsModel,
                    Runner ,input_guardrail , 
                    GuardrailFunctionOutput,
                    InputGuardrailTripwireTriggered)
from openai import AsyncOpenAI
from pydantic import BaseModel
import os 

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

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


#  Create the input guardial type 

class MathameticsOutPut (BaseModel):
    is_math_home_work : bool
    reasoning : str
    
guardial_agent = Agent(
    name = "Guardrail check Agent ",
    instructions= "Check is the User is asking you to do their maith work ",
    output_type=MathameticsOutPut
)

@input_guardrail
async def math_guardrail(ctx,agent , input) -> GuardrailFunctionOutput:
    print("Input Guardrail Prompt: ", input)
    result = await Runner.run(starting_agent=guardial_agent,input=input) 
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_home_work
    )
    
agent = Agent(
    name = "Customer Support agent ",
    instructions="You are customer support agent you help customer with their question ",
    model=model,
    input_guardrails=[math_guardrail]
)

async def main ():
    try:
        
        await Runner.run(starting_agent=agent,input="Hello can you help me solve 2*5")
        print("Guardrial didnot trap this is unexpected ")
        
    except InputGuardrailTripwireTriggered :
        print("Math Home work guardrial tripped ")
        

import asyncio

if __name__ == "__main__":
    asyncio.run(main())
