from openai import OpenAI
from agent.config import OPENROUTER_API_KEY
from agent.prompts import SYSTEM_PROMPT

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def generate_sql(question):

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Question:
{question}

Remember:
Use ONLY the schema provided.
Return SQL only.
"""
            }
        ]
    )

    response_text = response.choices[0].message.content

    select_pos = response_text.upper().find("SELECT")

    if select_pos != -1:
        sql_query = response_text[select_pos:]
    else:
        sql_query = response_text

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    if ";" in sql_query:
        sql_query = sql_query.split(";")[0] + ";"

    return sql_query.strip()