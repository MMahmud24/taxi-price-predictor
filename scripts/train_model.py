import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os


def train_model(path="../database/enhanced_data.csv", output="../models/fare_model.pkl"):

    df = pd.read_csv(path)

    features = ['trip_distance', 'hour', 'weekday', 'was_raining', 'event_nearby']
    target = 'fare_amount'

    df = df.dropna(subset = features + [target])

    X = df[features]
    Y = df[target]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = GradientBoostingRegressor()
    model.fit(X_train, Y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(Y_test, y_pred)
    mse = mean_squared_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)

    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"R2 Score: {r2}")

    # os.makedirs(os.path.dirname(output), exist_ok=True)
    # joblib.dump(model, output)



if __name__ == "__main__":
    train_model()