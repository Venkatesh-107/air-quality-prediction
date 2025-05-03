import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load dataset from CSV
df = pd.read_csv("air_quality_data.csv")
df = df.dropna()  # Clean any missing values

# Feature columns
X = df[['temp', 'humidity', 'wind_speed']]
# Target variable
y = df['pm25']

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model to disk
joblib.dump(model, "model.pkl")
print("✅ Model saved to model.pkl")
