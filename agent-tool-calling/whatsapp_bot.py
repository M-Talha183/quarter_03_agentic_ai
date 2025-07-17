# # # # import chainlit as cl
# # # # import os
# # # # import time
# # # # from dotenv import load_dotenv
# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.common.keys import Keys
# # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # from selenium.webdriver.chrome.service import Service
# # # # from openai import AsyncOpenAI
# # # # from agents import Agent,RunConfig, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

# # # # # Load environment
# # # # load_dotenv()
# # # # set_tracing_disabled(True)

# # # # gemini_api_key = os.getenv("GEMINI_API_KEY")
# # # # if not gemini_api_key:
# # # #     raise ValueError("Gemini API Key is not set!")

# # # # # Setup Gemini (OpenAI SDK with Google Gemini endpoint)
# # # # provider = AsyncOpenAI(
# # # #     api_key=gemini_api_key,
# # # #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="gemini-1.5-flash-latest",
# # # #     openai_client=provider
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=provider #type:ignore
# # # # )
# # # # controller= Agent(
# # # #     name="WhatsApp Message Generator",
# # # #     instructions="Generate a friendly, clear WhatsApp message based on user input.",
# # # #     model=model
# # # # )


# # # # # AI Message Generator using Runner
# # # # async def generate_gemini_message(prompt: str):
# # # #     result = await Runner.run(
# # # #         controller,    # Using RunConfig directly (no agent)
# # # #         input=prompt
# # # #     )
# # # #     return result.final_output

# # # # # WhatsApp Sender Function (Selenium)
# # # # def send_message(contact, message):
# # # #     options = webdriver.ChromeOptions()
# # # #     options.add_argument("user-data-dir=./User_Data")  # Save session to avoid QR every time

# # # #     service = Service(ChromeDriverManager().install())
# # # #     driver = webdriver.Chrome(service=service, options=options)

# # # #     driver.get("https://web.whatsapp.com/")
# # # #     input("Please scan the QR code in Chrome and press Enter to continue...")

# # # #     search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
# # # #     search_box.click()
# # # #     time.sleep(1)
# # # #     search_box.send_keys(contact)
# # # #     time.sleep(2)
# # # #     search_box.send_keys(Keys.ENTER)

# # # #     message_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
# # # #     message_box.click()
# # # #     message_box.send_keys(message)
# # # #     message_box.send_keys(Keys.ENTER)

# # # #     print(f"✅ WhatsApp message sent to {contact}")
# # # #     time.sleep(3)
# # # #     driver.quit()

# # # # # Chainlit App
# # # # @cl.on_message
# # # # async def main(message: cl.Message):
# # # #     await cl.Message(content="Generating WhatsApp message with Gemini AI...").send()

# # # #     ai_response = await generate_gemini_message(message.content)

# # # #     await cl.Message(content=f"Generated Message:\n{ai_response}").send()

# # # #     await cl.Message(content="Enter WhatsApp contact name (as saved in your WhatsApp):").send()

# # # #     contact_input = await cl.AskUserMessage("Contact Name?", timeout=60).send()

# # # # # ✅ Safe Check
# # # #     if contact_input is None or "output" not in contact_input:
# # # #          await cl.Message(content="⛔️ No contact name provided. Exiting!").send()
# # # #          return

# # # #     contact_name = contact_input["output"]

# # # #     send_message(contact_name, ai_response)

# # # #     await cl.Message(content=f"✅ WhatsApp message sent to {contact_name}!").send()
# # # import chainlit as cl
# # # import os
# # # import time
# # # import re
# # # import urllib.parse
# # # from dotenv import load_dotenv
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # from openai import AsyncOpenAI
# # # from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

# # # # Load environment
# # # load_dotenv()
# # # set_tracing_disabled(True)

# # # gemini_api_key = os.getenv("GEMINI_API_KEY")
# # # if not gemini_api_key:
# # #     raise ValueError("Gemini API Key is not set!")

# # # # Setup Gemini via OpenAI SDK
# # # provider = AsyncOpenAI(
# # #     api_key=gemini_api_key,
# # #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# # # )

# # # model = OpenAIChatCompletionsModel(
# # #     model="gemini-1.5-flash-latest",
# # #     openai_client=provider
# # # )

# # # # Define a simple single-agent flow
# # # controller = Agent(
# # #     name="WhatsApp Message Generator",
# # #     instructions="Generate a friendly, clear WhatsApp message based on user input message details only. Ignore phone number or name.",
# # #     model=model
# # # )

# # # # Extract phone number and message from user input
# # # def extract_number_and_message(user_input):
# # #     match = re.search(r'phone number is (\+?\d+).*message is (.+)', user_input, re.IGNORECASE)
# # #     if match:
# # #         phone_number = match.group(1).replace(" ", "")
# # #         message = match.group(2)
# # #         return phone_number, message
# # #     else:
# # #         return None, None

# # # # Use Gemini to clean or rephrase the message (optional)
# # # async def generate_gemini_message(prompt: str):
# # #     result = await Runner.run(
# # #         controller,
# # #         input=prompt
# # #     )
# # #     return result.final_output.strip()

# # # # Send WhatsApp message using direct phone link
# # # def send_message_via_number(phone_number, message):
# # #     options = webdriver.ChromeOptions()
# # #     options.add_argument("user-data-dir=./User_Data")

# # #     service = Service(ChromeDriverManager().install())
# # #     driver = webdriver.Chrome(service=service, options=options)

# # #     driver.get("https://web.whatsapp.com/")
# # #     input("Please scan the QR code in Chrome and press Enter to continue...")

# # #     encoded_message = urllib.parse.quote(message)
# # #     driver.get(f"https://wa.me/{phone_number}?text={encoded_message}")

# # #     time.sleep(5)  # Wait for chat to load

# # #     try:
# # #         send_btn = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
# # #         send_btn.click()
# # #         print(f"✅ Message sent to {phone_number}")
# # #     except:
# # #         print("⛔️ Send button not found. Check WhatsApp Web manually.")
# # #     time.sleep(3)
# # #     driver.quit()

# # # # Chainlit App
# # # @cl.on_message
# # # async def main(message: cl.Message):
# # #     await cl.Message(content="🔍 Processing your WhatsApp message request...").send()

# # #     phone_number, raw_message = extract_number_and_message(message.content)

# # #     if not phone_number or not raw_message:
# # #         await cl.Message(content="⛔️ Could not extract phone number or message. Please follow the prompt format.").send()
# # #         return

# # #     # Optional: Use Gemini to improve message tone
# # #     ai_response = await generate_gemini_message(raw_message)

# # #     send_message_via_number(phone_number, ai_response)

# # #     await cl.Message(content=f"✅ WhatsApp message sent to {phone_number}").send()
# # import chainlit as cl
# # import os
# # import time
# # import urllib.parse
# # from dotenv import load_dotenv
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from openai import AsyncOpenAI
# # from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool

# # # Load environment
# # load_dotenv()
# # set_tracing_disabled(True)

# # gemini_api_key = os.getenv("GEMINI_API_KEY")
# # if not gemini_api_key:
# #     raise ValueError("Gemini API Key is not set!")

# # provider = AsyncOpenAI(
# #     api_key=gemini_api_key,
# #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# # )

# # model = OpenAIChatCompletionsModel(
# #     model="gemini-1.5-flash-latest",
# #     openai_client=provider
# # )

# # # ✅ Create WhatsApp Tool using @function_tool
# # @function_tool
# # def sendWhatsAppMessage(contact_number: str, message: str) -> str:
# #     """
# #     Send a WhatsApp message using Selenium.
# #     """
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("user-data-dir=./User_Data")  # Reuse session

# #     service = Service(ChromeDriverManager().install())
# #     driver = webdriver.Chrome(service=service, options=options)

# #     driver.get("https://web.whatsapp.com/")
# #     input("Please scan the QR code and press Enter to continue...")

# #     encoded_message = urllib.parse.quote(message)
# #     driver.get(f"https://wa.me/{contact_number}?text={encoded_message}")

# #     time.sleep(5)  # Let the chat load

# #     try:
# #         send_btn = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
# #         send_btn.click()
# #         driver.quit()
# #         return f"✅ Message sent to {contact_number}"
# #     except Exception as e:
# #         driver.quit()
# #         return f"⛔️ Failed to send message: {str(e)}"

# # # ✅ Define the Agent using the tool
# # controller = Agent(
# #     name="WhatsApp Messaging Agent",
# #     instructions="""
# # Your role is to send WhatsApp messages for the user.

# # Whenever the user provides:
# # - A phone number
# # - A message

# # You MUST call the `sendWhatsAppMessage` tool to send the WhatsApp message.

# # Never send the message directly as text output. Always use the tool.
# # """,
# #     model=model,
# #     tools=[sendWhatsAppMessage]
# # )

# # # ✅ Chainlit App
# # @cl.on_message
# # async def main(message: cl.Message):
# #     await cl.Message(content="🤖 Processing your request...").send()

# #     result = await Runner.run(
# #         controller,
# #         input=message.content
# #     )

# #     await cl.Message(content=result.final_output).send()
# import os
# import time
# import chainlit as cl
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from openai import AsyncOpenAI
# from agents import Agent, RunConfig, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool

# # Load environment
# load_dotenv()
# set_tracing_disabled(True)

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("Gemini API Key is not set!")

# # Setup Gemini (OpenAI SDK with Google Gemini endpoint)
# provider = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-1.5-flash-latest",
#     openai_client=provider
# )

# config = RunConfig(
#     model=model,
#     model_provider=provider  # type: ignore
# )

# # WhatsApp Tool using function_tool
# @function_tool
# def sendWhatsAppMessage(contact_number: str, message: str) -> str:
#     """
#     Sends a WhatsApp message using Selenium automation with proper waits.
#     """
#     options = webdriver.ChromeOptions()
#     options.add_argument(r"user-data-dir=" + os.path.abspath("User_Data"))
#     options.add_argument("--profile-directory=ProfileWhatsApp")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-extensions")

#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)

#         driver.get("https://web.whatsapp.com/")

#         print("🔄 Waiting for WhatsApp Web to load...")
#         wait = WebDriverWait(driver, 30)

#         # Search box (with wait)
#         search_box = wait.until(
#             EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
#         )
#         search_box.click()
#         search_box.send_keys(contact_number)
#         time.sleep(2)
#         search_box.send_keys(Keys.ENTER)

#         # Message box (with wait)
#         message_box = wait.until(
#             EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
#         )
#         message_box.click()
#         message_box.send_keys(message)
#         message_box.send_keys(Keys.ENTER)

#         time.sleep(2)
#         driver.quit()

#         return f"✅ WhatsApp message sent to {contact_number}"

#     except Exception as e:
#         return f"❌ Failed to send message: {str(e)}"

# # Agent with Tool calling
# controller = Agent(
#     name="WhatsApp Messenger Agent",
#     instructions="""
#     You are an AI agent that helps send WhatsApp messages.

#     When the user provides a phone number and message, use the `sendWhatsAppMessage` tool.

#     The format should be:
#     Send WhatsApp message:

#     contact_number: +923XXXXXXXXX
#     message: Your message here.
#     """,
#     model=model,
#     tools=[sendWhatsAppMessage]
# )

# # Chainlit App
# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(content="🤖 Processing your WhatsApp message request...").send()

#     response = await Runner.run(
#         controller,
#         input=message.content
#     )

#     await cl.Message(content=response.final_output).send()
import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, RunConfig, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from twilio.rest import Client

# Load environment variables
load_dotenv()
set_tracing_disabled(True)

# Gemini Setup
gemini_api_key = os.getenv("GEMINI_API_KEY")
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash-latest",
    openai_client=provider
)

config = RunConfig(
    model=model,
    model_provider=provider # type:ignore
)

# Agent Setup (for message generation)
controller = Agent(
    name="WhatsApp Message Generator",
    instructions="Generate a professional WhatsApp message for the provided input.",
    model=model
)

# Twilio Setup
account_sid = os.getenv("ACCOUNT_SID_KEY")
auth_token = os.getenv("AUTH_TOKEN")
whatsapp_from = os.getenv("TWILIO_WHATSAPP_FROM")

client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    try:
        message_obj = client.messages.create(
            body=message,
            from_="whatsapp:" + whatsapp_from,
            to="whatsapp:" + to
        )
        return f"✅ WhatsApp message sent! SID: {message_obj.sid}"
    except Exception as e:
        return f"❌ Error sending message: {str(e)}"

# AI message generator
async def generate_message(prompt):
    response = await Runner.run(controller, input=prompt)
    return response.final_output

# Chainlit UI
@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="🤖 Generating WhatsApp message with Gemini AI...").send()

    ai_response = await generate_message(message.content)

    await cl.Message(content=f"Generated Message:\n{ai_response}").send()

    await cl.Message(content="Enter the recipient's WhatsApp number (with +92 etc.):").send()
    contact_input = await cl.AskUserMessage("Phone Number?", timeout=60).send()
    contact_number = contact_input["output"]

    result = send_whatsapp_message(contact_number, ai_response)

    await cl.Message(content=result).send()
