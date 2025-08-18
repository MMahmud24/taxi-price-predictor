import pandas as pd
from datetime import datetime, timezone
import os
import csv

def build_live():
    now = datetime.now(timezone.utc)
    hour = now.hour
    weekday = now.weekday()

    weather = pd.read_csv("../database/live_weather.csv")
    latest_weather = weather.iloc[-1]
    condition = latest_weather["weather_main"]
    was_raining = 1 if condition == "Rain" else 0


    events = pd.read_csv("../database/live_events.csv")
    
    events['startDateTime'] = pd.to_datetime(events['startDateTime'], errors='coerce')
    upcoming_events = events[
        (events['startDateTime'] >= now) &
        (events['startDateTime'] <= now + pd.Timedelta(hours=4))
    ]

    event_nearby = int(not upcoming_events.empty)
    
    feature_row = {
        'hour': hour,
        'weekday': weekday,
        'was_raining': was_raining,
        'event_nearby': event_nearby
    }
    
    return feature_row

def save_to_csv(data, filepath="../database/live_features.csv"):
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()
            
        writer.writerow(data)

if __name__ == "__main__":
    df = build_live()
    save_to_csv(df)
    

