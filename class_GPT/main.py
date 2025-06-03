import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use a lighter model with higher quota
model = genai.GenerativeModel("gemini-1.5-flash")

# Get user input
user_prompt = input("Enter your prompt for Gemini: ")
#  sve the api key
# Generate content from user input
response = model.generate_content(user_prompt)

# Print the response
print("\nGemini's Response:\n")
print(response.text)
