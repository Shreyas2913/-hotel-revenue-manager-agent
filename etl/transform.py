import pandas as pd
import re

def transform_data(df):

    records = []

    for _, row in df.iterrows():

        text = str(row["page_text"])

        def extract(pattern):
            match = re.search(pattern, text, re.MULTILINE)
            return match.group(1) if match else None

        records.append({
            "reservation_id": extract(r"(R\d{4})"),
            "arrival_date": extract(r"arrival_date\s+(\d{4}-\d{2}-\d{2})"),
            "departure_date": extract(r"departure_date\s+(\d{4}-\d{2}-\d{2})"),
            "nights": extract(r"nights\s+(\d+)"),
            "reservation_status": extract(r"reservation_status\s+(Reserved|Cancelled)"),
            "guest_country": extract(r"guest_country\s+([A-Z]{2})"),
            "space_type": extract(r"space_type\s+([A-Z]{2})"),
            "market_code": extract(r"market_code\s+([A-Z]+)"),
            "channel_code": extract(r"channel_code\s+([A-Z]+)"),
            "source_name": extract(r"source_name\s+([^\n]+)"),
            "adr_room": extract(r"adr_room\s+([\d\.]+)"),
            "lead_time": extract(r"lead_time\s+(\d+)"),
        })

    clean_df = pd.DataFrame(records)

    print("Data transformed successfully!")
    print(f"Rows after transformation: {len(clean_df)}")

    return clean_df