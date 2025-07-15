# from my_agent import E_commerce_agent
# import chainlit as cl 
# @cl.on_chat_start
# async def start():
#     await cl.Message("""Welcome to the **E-Commerce Multi-Agent System!** 🚀

# I can help you with:
# - 🛒 **Product Research** – Find trending products and suppliers.
# - 🖥️ **Store Design** – Get help designing your Shopify or web store.
# - 📢 **Ad Copywriting** – Generate marketing copy for Facebook, Google, or Instagram ads.

# **Please tell me what you'd like to do, and I'll assign the task to the right expert agent.**
# """).send()
# @cl.on_message
# async def main(message : cl.Message):
#     user_input = message.content 
#     responce = await E_commerce_agent(user_input)
#     await cl.Message(content = f"{responce}").send()
from my_agent import E_commerce_agent
import chainlit as cl

@cl.on_chat_start
async def start():
    await cl.Message("""
Welcome to the **E-Commerce Multi-Agent System!** 🚀

I can help you with:
- 🛒 **Product Research** – Find trending products and suppliers.
- 🖥️ **Store Design** – Get help designing your Shopify or web store.
- 📢 **Ad Copywriting** – Generate marketing copy for Facebook, Google, or Instagram ads.

**Please tell me what you'd like to do, and I'll assign the task to the right expert agent.**
""").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    try:
        response = await E_commerce_agent(user_input)
        await cl.Message(content=f"{response}").send()

    except Exception as e:
        await cl.Message(content=f"⚠️ **Error:** {str(e)}\n\nPlease try again or refine your request.").send()
