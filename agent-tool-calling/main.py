# import os 
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import  RunConfig  , OpenAIChatCompletionsModel ,set_tracing_disabled

# load_dotenv()
# set_tracing_disabled(True)

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key :
#     raise ValueError("Gimini api key is not sset ! Please set first it ")

# provider = AsyncOpenAI(
#     api_key= gemini_api_key,
#     base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model= "gemini-2.0-flash",
#     openai_client=provider
# )
# config =  RunConfig(
#     model=model,
#     model_provider=provider # type:ignore
# )

import chainlit as cl
from tools.whatsapp_tool import send_whatsapp_message_tool

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="Please wait... Sending your message via WhatsApp...").send()

    try:
        # Parse user input: expects "phone_number: +923001234567, message: hello"
        if "message:" in message.content and "phone_number:" in message.content:
            parts = message.content.split("message:")
            phone = parts[0].replace("phone_number:", "").strip()
            text = parts[1].strip()

            result = send_whatsapp_message_tool({
                "phone_number": phone,
                "message": text
            })

            await cl.Message(content=f"✅ Message sent!\n\n**SID**: `{result['sid']}`").send()
        else:
            await cl.Message(content="❌ Format incorrect. Please send like:\n`phone_number: +923001234567, message: Hello!`").send()

    except Exception as e:
        await cl.Message(content=f"❌ Failed to send message.\n**Error:** {str(e)}").send()
