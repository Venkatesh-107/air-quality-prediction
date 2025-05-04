import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_csv("air_quality_data.csv")
df = df.dropna()  # Drop rows with missing values

# Define features and target
X = df[['temp', 'humidity', 'wind_speed']]
y = df['pm25']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"✅ Model trained.")
print(f"🔍 R² Score: {r2:.3f}")
print(f"📉 MSE: {mse:.3f}")

# Save model
joblib.dump(model, "model.pkl")
print("💾 Model saved as model.pkl")
