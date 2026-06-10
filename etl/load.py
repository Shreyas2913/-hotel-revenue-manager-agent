import pandas as pd

def load_data(df):

    output_path = "Data/processed/reservations_clean.csv"

    df.to_csv(output_path, index=False)

    print("Data loaded successfully!")
    print(f"Saved to: {output_path}")