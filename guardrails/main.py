from dotenv import load_dotenv
from agents import (Agent , 
                    OpenAIChatCompletionsModel,
                    set_tracing_disabled,
                    Runner ,input_guardrail , 
                    GuardrailFunctionOutput,
                    InputGuardrailTripwireTriggered,
                    TResponseInputItem,
                    RunContextWrapper)
from openai import AsyncOpenAI
from pydantic import BaseModel
import os 
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

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

class Out_Put_Python (BaseModel):
    is_python_related : bool
    reasoning : str

input_gardrial_agent = Agent(
    name = "Input guardial agent ",
    instructions="check the user input is related to python or not if related to python return true if not then return false ",
    model=model,
    output_type=Out_Put_Python
)


@input_guardrail
async def input_gardrial_fun(
    ctx : RunContextWrapper ,agent:Agent, input : str | list[TResponseInputItem]
)-> GuardrailFunctionOutput :
    
    result = await Runner.run(
        input_gardrial_agent,
        input,
    )

    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered=not result.final_output.is_python_related
    )



class ManageOutPut (BaseModel):
    responce : str

class Python_out_put (BaseModel):
    is_python : bool
    reasoning : str 
    
out_put_gad_agent = Agent(
    name = "output guardrails",
    instructions="check it the out put includes any python related Ans",
    output_type=Python_out_put,
    model=model
    
)

main_agent = Agent(
    name = "Python Expert ",
    instructions="Your python programming languge expert with write coding , syntax , error handling and debuging in python related code ",
    model= model,
    input_guardrails=[input_gardrial_fun]
)




@cl.on_chat_start
async def on_chat_start_fun():
    await cl.Message(content="I am Ready to Assist").send()

@cl.on_message
async def responce_fun (message:cl.Message):
    try:
        result = await Runner.run(
        main_agent,
        input=message.content
        )
        await cl.Message(content=result.final_output).send()
    except InputGuardrailTripwireTriggered :
        await cl.Message(content="Please Ask Only Python Related Question ").send()










































































# #  Create the input guardial type 

# class MathameticsOutPut (BaseModel):
#     is_math_home_work : bool
#     reasoning : str
    
# guardial_agent = Agent(
#     name = "Guardrail check Agent ",
#     instructions= "Check is the User is asking you to do their maith work ",
#     output_type=MathameticsOutPut
# )

# @input_guardrail
# async def math_guardrail(ctx,agent , input) -> GuardrailFunctionOutput:
#     print("Input Guardrail Prompt: ", input)
#     result = await Runner.run(starting_agent=guardial_agent,input=input) 
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=result.final_output.is_math_home_work
#     )
    
# agent = Agent(
#     name = "Customer Support agent ",
#     instructions="You are customer support agent you help customer with their question ",
#     model=model,
#     input_guardrails=[math_guardrail]
# )

# async def main ():
#     try:
        
#         await Runner.run(starting_agent=agent,input="Hello can you help me solve 2*5")
#         print("Guardrial didnot trap this is unexpected ")
        
#     except InputGuardrailTripwireTriggered :
#         print("Math Home work guardrial tripped ")
        

# import asyncio

# if __name__ == "__main__":
#     asyncio.run(main())
