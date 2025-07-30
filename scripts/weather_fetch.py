import requests 
import os
from dotenv import load_dotenv
from datetime import datetime
import csv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "New York"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

def fetch_weather():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Error", response.status_code)
        return None

    data = response.json()

    weather_info = {
        "timestamp": datetime.now().isoformat(),
        "city": data.get("name"),
        "temp_f": data["main"]["temp"],
        "weather_main": data["weather"][0]["main"],
        "weather_desc": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather_info

def save_to_csv(data, filepath="../database/live_weather.csv"):
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()
            
        writer.writerow(data)



if __name__ == "__main__":
    weather = fetch_weather()
    if weather:
        print("Weather fetched successfully")
        for x, y in weather.items():
            print(f"{x}: {y}")
        save_to_csv(weather)

