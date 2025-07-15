import os 
from agents import Agent , OpenAIChatCompletionsModel , Runner , set_tracing_disabled 
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key= gemini_api_key ,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = provider
)

# AI E-Commerce Launch Team with Controller

product_rearch_agent = Agent(
    name = "You are a Product Research Agent.",
    instructions = "Tasks:- Identify trending products for online stores.- Analyze market demand and competition.- Provide sourcing links and supplier details.",
    model= model,
    handoff_description = "Respond only with product research data, not marketing or store design advice."
)
 
store_Designer =  Agent(
    name = "You are a Store Designer Agent.",
    instructions= """Tasks:
- Recommend online store layouts and UX strategies.
- Provide product descriptions and landing page copy.
- Suggest checkout flow improvements.""" ,
    model= model ,
    handoff_description= "Do not perform product research or write ads."
)

copy_writer = Agent(
    name = "You are an Ad Copywriter Agent.",
    instructions=" Write compelling ad copy for digital marketing.- Use frameworks like AIDA or PAS.- Provide ad text variations for testing.",
    model= model,
    handoff_description= "Do not suggest products or design stores."
)


ecommerce_knowledge_agent = Agent(
    name = "E-Commerce Knowledge Expert Agent",
    instructions = """
You are an E-Commerce Knowledge Expert Agent.

Your role is to:
- Answer general questions about e-commerce.
- Provide beginner-friendly explanations for concepts like:
    - What is e-commerce?
    - How does e-commerce work?
    - Benefits and challenges of e-commerce.
    - Types of e-commerce (B2B, B2C, C2C, D2C).
    - How to start an online business.
    - Online payment systems, logistics, customer service basics.

Guidelines:
- Respond clearly and concisely.
- Use examples where helpful.
- If the user asks for tasks like product research, store design, or ad copywriting, DO NOT answer and let the Controller Agent handle routing.
""",
    model = model,  # Use your preferred model, e.g., "gpt-4o"
    handoff_description = "Handles all general knowledge questions related to e-commerce concepts, definitions, and beginner education."
)

async def E_commerce_agent (user_input) : 
    controller = Agent(
        name = "You are a Controller Agent responsible for task routing.",
        instructions= """- Receive user requests.
- Classify the task into one of three categories:
    - Product Research → Handoff to Product Research Agent
    - Store Design → Handoff to Store Designer Agent
    - Marketing & Ads → Handoff to Ad Copywriter Agent
- If the request is unclear, ask for clarification.
""",
    model= model ,
    handoffs= [product_rearch_agent,store_Designer,copy_writer,ecommerce_knowledge_agent]
    )

    responce = await Runner.run(
        controller,
        input = user_input
    )
    return responce.final_output
    