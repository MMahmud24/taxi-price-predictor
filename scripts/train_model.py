import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os


def train_model(path="../database/enhanced_data.csv", output="../models/fare_model.pkl"):

    df = pd.read_csv(path)

    features = ['trip_amount', 'hour', 'weekday', 'was_raining', 'event_nearby']
    target = 'fare_amount'

    df = df.dropna(subset = features + [target])

    X = df[features]
    Y = df[target]

    