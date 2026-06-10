from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324",
    messages=[
        {
            "role": "user",
            "content": "Hello, who are you?"
        }
    ]
)

print(response.choices[0].message.content)