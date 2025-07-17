# import chainlit as cl
# from ai_gemini_openai_sdk import generate_gemini_message
# from whatsapp_bot import send_message

# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(content="Generating WhatsApp message with Gemini AI...").send()

#     ai_response = await generate_gemini_message(message.content)

#     await cl.Message(content=f"Generated Message:\n{ai_response}").send()

#     await cl.Message(content="Enter WhatsApp contact name (as saved in your WhatsApp):").send()

#     # Ask for contact name and get the correct user input
#     contact_input = await cl.AskUserMessage("Contact Name?", timeout=60).send()
#     contact_name = contact_input["output"]  # ✅ Properly extract user input

#     # Send message to WhatsApp using Selenium
#     send_message(contact_name, ai_response)

#     await cl.Message(content=f"✅ WhatsApp message sent to {contact_name}!").send()
