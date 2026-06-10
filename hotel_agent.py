import os
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Neon PostgreSQL
DATABASE_URL = "postgresql://neondb_owner:npg_ji06DoUmAlXk@ep-small-field-aq2gp9al-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DATABASE_URL)

print("Hotel Revenue Agent Started")
print("Type 'exit' to quit")

while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    prompt = f"""
You are a Hotel Revenue Management SQL Agent.

Database: PostgreSQL

Table Name:
reservations

Schema:

reservation_id TEXT
arrival_date DATE
departure_date DATE
nights INTEGER
reservation_status TEXT
guest_country TEXT
space_type TEXT
market_code TEXT
channel_code TEXT
source_name TEXT
adr_room NUMERIC
lead_time INTEGER

Business Rules:

- Cancelled reservations:
  reservation_status = 'Cancelled'

- Reserved reservations:
  reservation_status = 'Reserved'

- ADR = adr_room

- Guest country = guest_country

- Booking source = source_name

IMPORTANT:

Return ONLY executable PostgreSQL SQL.

Do NOT explain.
Do NOT add comments.
Do NOT add markdown.
Do NOT say:
"Here's the SQL query"
"This query calculates..."

Output must start with SELECT.

Question:
{question}
"""

    try:

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = response.choices[0].message.content

        # Extract SQL starting from SELECT
        select_pos = response_text.upper().find("SELECT")

        if select_pos != -1:
            sql_query = response_text[select_pos:]
        else:
            sql_query = response_text

        # Remove markdown
        sql_query = sql_query.replace("```sql", "")
        sql_query = sql_query.replace("```", "")

        # Keep only first SQL statement
        if ";" in sql_query:
            sql_query = sql_query.split(";")[0] + ";"

        sql_query = sql_query.strip()

        print("\nGenerated SQL:")
        print(sql_query)

        with engine.connect() as conn:

            result = conn.execute(text(sql_query))

            rows = result.fetchall()

            print("\nAnswer:")

            for row in rows:
                print(row)

    except Exception as e:
        print("\nError:")
        print(e)