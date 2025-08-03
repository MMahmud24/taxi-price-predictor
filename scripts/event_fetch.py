import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("EVENT_API_KEY")
URL = "https://app.ticketmaster.com/discovery/v2/events.json"
CITY = "New York"
size = 100

def fetch_events():
    response = requests.get(URL)

    if response.status_code != 200:
        print("Error", response.status_code)
        return None
    
    return df




if __name__ == "__main__":
    df = fetch_events()
    if df is not None and not df.empty:
        print(df[["name", "start_time", "venue", "city"]].head())

