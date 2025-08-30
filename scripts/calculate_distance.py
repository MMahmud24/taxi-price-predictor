import openrouteservice
from openrouteservice import convert
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTE_API_KEY")

client = openrouteservice.Client(key=API_KEY)

def calculate(pickup, dropoff):
    coords = [pickup, dropoff]
    try:
        route = client.directions(coords)
        distance_meters = route['features'][0]['properties']['segments'][0]['distance']
        return distance_meters / 1000 
    except Exception as e:
        print("Error fetching route", e)
        return None
    

if __name__ == "__main__":
    pickup = (37.7749, -122.4194)
    dropoff = (37.7749, -122.4194)
    print(calculate(pickup, dropoff))


