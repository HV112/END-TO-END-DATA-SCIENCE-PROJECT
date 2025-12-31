from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("student_model.pkl", "rb"))


@app.route("/")
def home():
    return "Student Pass Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    hours = data["hours_studied"]
    attendance = data["attendance"]
    previous_score = data["previous_score"]

    prediction = model.predict([[hours, attendance, previous_score]])

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
