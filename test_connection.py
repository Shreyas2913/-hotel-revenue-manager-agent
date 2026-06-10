import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = "postgresql://neondb_owner:npg_ji06DoUmAlXk@ep-small-field-aq2gp9al-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require"

print("Connecting...")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM reservations"))
    print(result.scalar()),