# import os
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import RunConfig, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

# load_dotenv()
# set_tracing_disabled(True)

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key:
#     raise ValueError("Gemini API Key is not set!")

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
#     model_provider=provider
# )

# async def generate_gemini_message(prompt: str):
#     result = await Runner.run(
#         controller=config,    # Use RunConfig directly (no Agent class)
#         input=prompt
#     )
#     return result.message.strip()
