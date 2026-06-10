from dotenv import load_dotenv
from openai import OpenAI
import os

# Load .env file
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Test request
response = client.chat.completions.create(
    model='model="nvidia/llama-3.1-nemotron-nano-8b-v1:free"',
    messages=[
        {
            "role": "user",
            "content": "Say hello and tell me you are working."
        }
    ]
)

print("\nMODEL RESPONSE:\n")
print(response.choices[0].message.content)