import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

def predict_pm25(data_dict):
    features = np.array([[
        data_dict["temp"],
        data_dict["humidity"],
        data_dict["wind_speed"]
    ]])
    return model.predict(features)[0]
