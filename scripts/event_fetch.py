import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timezone, timedelta
import csv

load_dotenv()

API_KEY = os.getenv("EVENT_API_KEY")
CITY = "New York"
size = 10
URL = f"https://app.ticketmaster.com/discovery/v2/events.json"

def fetch_sports_events(num):
    params = {
        "apikey": API_KEY,
        "city": CITY,
        "startDateTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "countryCode": "US",
        "classificationName": "Sports",
        "size": size
    }

    response = requests.get(URL, params=params)
    if response.status_code != 200:
        print("Error", response.status_code)
        return None

    data = response.json()

    events = data.get("_embedded", {}).get("events", [])

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    future_utc = now_utc + timedelta(days=1)

    ev = events[num]
    
    events_info = {
        "id": ev.get("id"),
        "name": ev.get("name"),
        "startDateTime": now_utc.isoformat().replace("+00:00", "Z"),
        "endDateTime": future_utc.isoformat().replace("+00:00", "Z"),
        "venue": ev.get("_embedded", {}).get("venues", [{}])[0].get("name"),
        "city": ev.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name"),
        "lat": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("latitude"),
        "lng": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("longitude"),
        "classification": ",".join([c["segment"]["name"] for c in ev.get("classifications", [])])
    }

    return events_info

def fetch_music_events(num):
    params = {
        "apikey": API_KEY,
        "city": CITY,
        "startDateTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "countryCode": "US",
        "classificationName": "Music",
        "size": size
    }

    response = requests.get(URL, params=params)
    if response.status_code != 200:
        print("Error", response.status_code)
        return None

    data = response.json()

    events = data.get("_embedded", {}).get("events", [])

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    future_utc = now_utc + timedelta(days=1)

    ev = events[num]
    
    events_info = {
        "id": ev.get("id"),
        "name": ev.get("name"),
        "startDateTime": now_utc.isoformat().replace("+00:00", "Z"),
        "endDateTime": future_utc.isoformat().replace("+00:00", "Z"),
        "venue": ev.get("_embedded", {}).get("venues", [{}])[0].get("name"),
        "city": ev.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name"),
        "lat": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("latitude"),
        "lng": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("longitude"),
        "classification": ",".join([c["segment"]["name"] for c in ev.get("classifications", [])])
    }

    return events_info

def fetch_ANT_events(num):
    params = {
        "apikey": API_KEY,
        "city": CITY,
        "startDateTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "countryCode": "US",
        "classificationName": "Arts & Theatre",
        "size": size
    }

    response = requests.get(URL, params=params)
    if response.status_code != 200:
        print("Error", response.status_code)
        return None

    data = response.json()

    events = data.get("_embedded", {}).get("events", [])

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    future_utc = now_utc + timedelta(days=1)

    ev = events[num]
    
    events_info = {
        "id": ev.get("id"),
        "name": ev.get("name"),
        "startDateTime": now_utc.isoformat().replace("+00:00", "Z"),
        "endDateTime": future_utc.isoformat().replace("+00:00", "Z"),
        "venue": ev.get("_embedded", {}).get("venues", [{}])[0].get("name"),
        "city": ev.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name"),
        "lat": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("latitude"),
        "lng": ev.get("_embedded", {}).get("venues", [{}])[0].get("location", {}).get("longitude"),
        "classification": ",".join([c["segment"]["name"] for c in ev.get("classifications", [])])
    }

    return events_info

def saveToCsv(data, path="../database/live_events.csv"):
    file_exists = os.path.isfile(path)

    with open(path, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)


if __name__ == "__main__":
    for i in range(10):
        dfs = fetch_sports_events(i)
        if dfs:
            saveToCsv(dfs)
        dfm = fetch_music_events(i)
        if dfm:
            saveToCsv(dfm)
        dfat = fetch_ANT_events(i)
        if dfat:
            saveToCsv(dfat)


    

