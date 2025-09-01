import openrouteservice
from openrouteservice import convert
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTE_API_KEY")

client = openrouteservice.Client(key=API_KEY)

def calculate_distance(lat1, lon1, lat2, lon2):
    try:
        pickup = [lon1, lat1]     
        dropoff = [lon2, lat2]    


        coords = [pickup, dropoff]
        route = client.directions(coords, profile='driving-car')

    
        distance_meters = route['routes'][0]['summary']['distance']
        distance_km = distance_meters / 1000
    except Exception as e:
        print(f"Error: {e}")
        return None




    return distance_km


if __name__ == "__main__":
    distance = calculate_distance(40.709661, -73.816302, 40.758896, -73.985130)
    print(f"Distance: {distance} km")


