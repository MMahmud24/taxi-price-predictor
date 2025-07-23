import pandas as pd


def load_and_clean_csv(path):

    df = pd.read_csv(path, low_memory=False)

    df = df.rename(columns={
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime",
        "PULocationID": "pickup_location_id",
        "DOLocationID": "dropoff_location_id"
    })

    df = df[[
        "pickup_datetime", "dropoff_datetime",
        "pickup_location_id", "dropoff_location_id",
        "trip_distance", "fare_amount", "passenger_count"
    ]]

    print("fare_amount type:", df["fare_amount"].dtype)

    df.dropna(inplace=True)
    df = df[df["fare_amount"] > 0]
    df = df[df["trip_distance"] > 0]


    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["hour"] = df["pickup_datetime"].dt.hour
    df["weekday"] = df["pickup_datetime"].dt.dayofweek
    
    return df


if __name__ == "__main__":
    print("Running cleaning script")
    df = load_and_clean_csv("filtered_data.csv")
    print(df.head())
    print("Sample columns:", df.columns.tolist())



