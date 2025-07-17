# from agents import Agent , Runner
# from main import config 


# agent = Agent(
#     name = "General agent",
#     instructions= " Ypu are aa help full assistent . you are task is help the user to help in their queries "
# )
# result = Runner.run_sync( agent , "Who is the founder of pakis tan", run_config=config)
# print(result.final_output)

import os
from typing import Dict
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_message_tool(inputs: Dict) -> Dict:
    account_sid = os.getenv("ACCOUNT_SID_KEY")
    auth_token = os.getenv("AUTH_TOKEN")
    whatsapp_from = os.getenv("TWILIO_WHATSAPP_FROM")

    client = Client(account_sid, auth_token)

    msg = client.messages.create(
        from_=whatsapp_from,
        body=inputs["message"],
        to=f"whatsapp:{inputs['phone_number']}"
    )

    return {"status": "sent", "sid": msg.sid}
