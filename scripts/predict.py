import sys
import json
import joblib
import datetime
import os
from calculate_distance import calculate_distance
import pandas as pd


def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "models", "fare_model.pkl")
    return joblib.load(model_path)


def build_features(pickup, dropoff, trip_distance):
    now = datetime.datetime.now()
    hour = now.hour
    weekday = now.weekday()  
    was_raining = 0         
    event_nearby = 0 

    return [trip_distance, hour, weekday, was_raining, event_nearby]

def predict():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing pickup/dropoff args"}))
        return

    pickup = json.loads(sys.argv[1])  
    dropoff = json.loads(sys.argv[2])  

    distance = calculate_distance(pickup[0], pickup[1], dropoff[0], dropoff[1])
    features = build_features(pickup, dropoff, distance)

    model = load_model()
    X = pd.DataFrame([features], columns=['trip_distance','hour','weekday','was_raining','event_nearby'])
    fare = model.predict([features])[0]

    result = {
        "pickup": pickup,
        "dropoff": dropoff,
        "distance_km": distance,
        "fare": float(fare)
    }

    print(json.dumps(result))


if __name__ == "__main__":
    predict()