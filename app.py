from flask import Flask, request, render_template
from predictor import predict_pm25

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    input_data = {
        "temp": float(data["temp"]),
        "humidity": float(data["humidity"]),
        "wind_speed": float(data["wind_speed"])
    }
    prediction = predict_pm25(input_data)
    return f"<h2>Predicted PM2.5: {prediction:.2f}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
