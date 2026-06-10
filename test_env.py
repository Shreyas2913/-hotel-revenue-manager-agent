from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY FOUND:", os.getenv("OPENROUTER_API_KEY") is not None)
print("DB URL FOUND:", os.getenv("DATABASE_URL") is not None)