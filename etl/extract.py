import pandas as pd

def extract_data():
    df = pd.read_csv("reservations_raw.csv")

    print("Data extracted successfully!")
    print(f"Rows: {len(df)}")

    return df

if __name__ == "__main__":
    extract_data()