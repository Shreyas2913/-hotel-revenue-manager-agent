import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

df = pd.read_csv("Data/processed/reservations_clean.csv")

df.to_sql(
    "reservations",
    engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(df)} rows into PostgreSQL")