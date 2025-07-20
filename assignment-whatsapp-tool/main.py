import os 
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Runner, RunConfig  , OpenAIChatCompletionsModel ,set_tracing_disabled , function_tool ,Agent
import chainlit as cl 
from whatsapp import send_whatsapp_message
load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

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
@function_tool
def get_user_data (min_age :int ) -> list[dict]:
    "Retrive user Data based on a minium age "
    users = [
    {"name": "Muneeb", "age": 19},
    {"name": "Talha", "age": 22},
    {"name": "Ahmed", "age": 20},
    {"name": "Sara", "age": 18},
    {"name": "Ayesha", "age": 21},
    {"name": "Usman", "age": 23},
    {"name": "Hassan", "age": 20},
    {"name": "Fatima", "age": 19},
    {"name": "Ali", "age": 22},
    {"name": "Zara", "age": 18},
    {"name": "Bilal", "age": 24},
    {"name": "Iqra", "age": 20},
    {"name": "Kamran", "age": 21},
    {"name": "Nida", "age": 19},
    {"name": "Faizan", "age": 23},
    {"name": "Mehwish", "age": 18},
    {"name": "Saad", "age": 20},
    {"name": "Sana", "age": 21},
    {"name": "Imran", "age": 22},
    {"name": "Anum", "age": 19},
    {"name": "Raza", "age": 23},
    {"name": "Rabia", "age": 20},
    {"name": "Shahid", "age": 24},
    {"name": "Kiran", "age": 18},
    {"name": "Junaid", "age": 21}
]
    for user in users:
        if user["age"] < min_age:
            users.remove(user)
    
    return users  

#  Rishtay Wali agent 
rishta_agent = Agent(
    name="Rashty Wali",
    instructions="""
    You are Rashti wali Auntee . Find maches from a custom tool based on age only .
    Reply Short and send Whatsapp message on if user ask """,
    model= model,
    tools= [get_user_data , send_whatsapp_message]
)
@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    await cl.Message("Salam beta! Main Rishty Wali Auntie hoon. Apna rishta batain, age batain, aur WhatsApp number dein. 😄").send()



@cl.on_message
async def main (message:cl.Message):
    await cl.Message("Thinking .... ").send()
    history = cl.user_session.get("history") or []
    history.append({"role":"user", "content":message.content})
    
    result = Runner.run_sync(
        starting_agent=rishta_agent,
        input=history
    )
    
    history.append({"role":"user", "content":result.final_output})
    
    cl.user_session.set("history",history)
    
    await cl.Message(content=result.final_output).send()
