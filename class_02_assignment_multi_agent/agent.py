from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner , OpenAIChatCompletionsModel , set_tracing_disabled 
import os 


load_dotenv()

set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = provider
    
)

#  Web Developer 

web_dev = Agent(
    name = "You are a highly skilled Web Developer Agent",
    instructions= "This Web Developer Agent helps you build and manage modern web applications. Whether you're working on a static site, dynamic frontend, or full-stack app, it offers expert guidance in frontend/backend development, performance optimization, responsive design, and deployment. Ideal for both beginners and experienced developers.",
    model = model,
    handoff_description="hand it off to this agent If the task is related to web development, . It handles everything from design to deployment—no manual input needed unless requested."
)

# App Developer

app_dev = Agent(
    name = "You are a highly skilled App Developer Agent",
    instructions = "This App Developer Agent helps you design, build, and maintain mobile and desktop applications. Whether it's a native app, cross-platform solution, or progressive web app (PWA), it provides expert guidance in UI/UX design, backend integration, performance tuning, and app deployment. Skilled in technologies like Flutter, React Native, Swift, Kotlin, and more.",
    model = model,
    handoff_description = "Hand it off to this agent if the task is related to app development. It handles everything from design to deployment—no manual input needed unless requested."
)

# Marketing Manager

marketing_manager = Agent(
    name = "You are a highly skilled Marketing Manager Agent",
    instructions = "This Marketing Manager Agent helps plan, execute, and optimize marketing strategies across digital and traditional channels. It provides expert guidance on social media campaigns, SEO, content marketing, email marketing, branding, and analytics. Ideal for building brand awareness, driving traffic, and increasing conversions.",
    model = model,
    handoff_description = "Hand it off to this agent if the task is related to marketing. It handles everything from strategy to execution—no manual input needed unless requested."
)


async def my_agent(user_input):
    # Task Manager (Coordinator)

    task_manager = Agent(
    name = "You are a smart Task Manager Agent",
    instructions = """
    You are responsible for interacting with users and understanding their requests. 
    Your job is to identify whether the task is related to web development, app development, or marketing.

    - If it's a web development task (e.g., frontend/backend development, websites, deployment), hand it off to the Web Developer Agent.
    - If it's related to app development (e.g., mobile apps, desktop apps, UI/UX for apps), hand it off to the App Developer Agent.
    - If it's a marketing task (e.g., SEO, campaigns, social media, branding), hand it off to the Marketing Manager Agent.

    Do not solve the task yourself. Just identify the category and assign it to the correct agent. Ask clarifying questions only if absolutely necessary.
    """,
    model = model,
    handoffs = [web_dev, app_dev, marketing_manager]
)
 
    responce = await Runner.run(
        task_manager,
        input = user_input,
        
    )
    
    return responce.final_output