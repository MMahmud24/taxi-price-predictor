import pandas as pd
import numpy as np
import os

def build_feature(input_path="../database/filtered_data.csv", output_path="../database/enhanced_data.csv"):
    if not os.path.isfile(input_path):
        print("Input file does not exist")
        return

    df = pd.read_csv(input_path, low_memory=False)

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df["hour"] = df["tpep_pickup_datetime"].dt.hour
    df["weekday"] = df["tpep_pickup_datetime"].dt.dayofweek 

    df["was_raining"] = np.random.choice([0, 1], size=len(df), p=[0.8, 0.2])

    df["event_nearby"] = df.apply(
        lambda row: 1 if (row["hour"] >= 18 and row["hour"] <= 22) or (row["weekday"] >= 5) else 0,
        axis=1
    )

    df.to_csv(output_path, index=False)



if __name__ == "__main__":
    build_feature()