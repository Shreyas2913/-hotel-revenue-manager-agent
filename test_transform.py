import pandas as pd
import re

df = pd.read_csv("reservations_raw.csv")

records = []

for _, row in df.iterrows():

    text = row["page_text"]

    reservation_id = re.search(r"(R\d{4})", text)

    arrival_date = re.search(
        r"arrival_date\s+(\d{4}-\d{2}-\d{2})",
        text
    )

    departure_date = re.search(
        r"departure_date\s+(\d{4}-\d{2}-\d{2})",
        text
    )

    reservation_status = re.search(
        r"reservation_status\s+(Reserved|Cancelled)",
        text
    )

    guest_country = re.search(
        r"guest_country\s+([A-Z]{2})",
        text
    )

    records.append({
        "reservation_id":
            reservation_id.group(1) if reservation_id else None,

        "arrival_date":
            arrival_date.group(1) if arrival_date else None,

        "departure_date":
            departure_date.group(1) if departure_date else None,

        "reservation_status":
            reservation_status.group(1) if reservation_status else None,

        "guest_country":
            guest_country.group(1) if guest_country else None
    })

clean_df = pd.DataFrame(records)

clean_df.to_csv(
    "reservations_clean.csv",
    index=False
)

print(clean_df.head())
print("Rows:", len(clean_df))