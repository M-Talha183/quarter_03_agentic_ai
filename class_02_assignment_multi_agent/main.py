# from agent import my_agent
# import chainlit as cl # type : ignore
# import asyncio

# @cl.on_chat_start 

# async def start():
#     await cl.Message("Welcome To The Mult-Agent System! How Can I help You ").send()
    
# @cl.on_message
# async def main(message : cl.Message):
#     user_input = message.content 
#     responce = asyncio.run(my_agent(user_input))
#     await cl.Message(
#         content = f"{responce}"
#     ).send()
    
from agent import my_agent
import chainlit as cl # type: ignore

@cl.on_chat_start
async def start():
    await cl.Message("Welcome to the Multi-Agent System! How can I help you?").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    responce = await my_agent(user_input)
    await cl.Message(content=f"{responce}").send()
