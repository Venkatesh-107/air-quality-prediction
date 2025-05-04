from flask import Flask, request, render_template, jsonify
from predictor import predict_pm25
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        
        # Ensure the data contains required keys
        if not data or 'temp' not in data or 'humidity' not in data or 'wind_speed' not in data:
            return jsonify({"error": "Missing required data (temp, humidity, wind_speed)"}), 400

        input_data = {
            "temp": float(data["temp"]),
            "humidity": float(data["humidity"]),
            "wind_speed": float(data["wind_speed"])
        }

        # Make the prediction using the predictor
        prediction = predict_pm25(input_data)

        # Return the prediction in JSON format
        return jsonify({"prediction": round(prediction, 2)})

    except Exception as e:
        print(f"Error: {e}")  # Log the error on the server console
        return jsonify({"error": "An error occurred during prediction. Please try again later."}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use PORT from environment, default to 10000
    app.run(debug=True, host='0.0.0.0', port=port)
