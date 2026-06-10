from sqlalchemy import create_engine, text
from agent.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def run_sql(sql_query):
    with engine.connect() as conn:
        result = conn.execute(text(sql_query))

        try:
            return result.fetchall()
        except:
            return []