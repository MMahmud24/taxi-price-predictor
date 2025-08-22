import pandas as pd

def merge_features(input_path1="../database/enhanced_data.csv", input_path2="../database/live_features.csv", output_path="../database/combined_features.csv"):
    

    required_cols = ["pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude", "hour", "weekday", "was_raining", "event_nearby"]
    historical_df = pd.read_csv(input_path1)
    live_df = pd.read_csv(input_path2)


