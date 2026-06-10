import os
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import create_engine, text

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

DATABASE_URL = "postgresql://neondb_owner:npg_ji06DoUmAlXk@ep-small-field-aq2gp9al-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    prompt = f"""
You are a PostgreSQL expert.

Table name: reservations

Generate ONLY SQL.
No explanation.
No markdown.
No ```sql blocks.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql_query = response.choices[0].message.content.strip()

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

    print("\nGenerated SQL:")
    print(sql_query)

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = result.fetchall()

            print("\nAnswer:")
            for row in rows:
                print(row)

    except Exception as e:
        print("\nError:")
        print(e)