import pandas as pd
import re

df = pd.read_csv("reservations_raw.csv")

fields = [
    "reservation_id",
    "arrival_date",
    "departure_date",
    "nights",
    "reservation_status",
    "create_datetime",
    "cancellation_datetime",
    "guest_country",
    "is_block",
    "is_walk_in",
    "number_of_spaces",
    "space_type",
    "market_code",
    "channel_code",
    "source_name",
    "rate_plan_code",
    "adr_room",
    "lead_time",
    "company_name",
    "travel_agent_name"
]

records = []

for text in df["page_text"]:

    row = {}

    lines = text.split("\n")

    for i in range(len(lines)-1):

        key = lines[i].strip()
        value = lines[i+1].strip()

        if key in fields:
            row[key] = value

    records.append(row)

clean_df = pd.DataFrame(records)

clean_df.to_csv(
    "reservations_clean.csv",
    index=False
)

print(clean_df.head())
print()
print("Rows:", len(clean_df))
print("Saved reservations_clean.csv")