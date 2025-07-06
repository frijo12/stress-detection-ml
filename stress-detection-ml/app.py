from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load('models/model_random_forest.pkl')

# Load encoders
encoders = {
    'Gender': joblib.load('app/encoder_Gender.pkl'),
    'Occupation': joblib.load('app/encoder_Occupation.pkl'),
    'BMI Category': joblib.load('app/encoder_BMI Category.pkl'),
    'Sleep Disorder': joblib.load('app/encoder_Sleep Disorder.pkl')
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = request.form

        # Prepare input features
        features = [
            encoders['Gender'].transform([data['gender']])[0],
            int(data['age']),
            encoders['Occupation'].transform([data['occupation']])[0],
            float(data['sleep_duration']),
            int(data['quality_of_sleep']),
            int(data['physical_activity']),
            encoders['BMI Category'].transform([data['bmi_category']])[0],
            int(data['heart_rate']),
            int(data['daily_steps']),
            encoders['Sleep Disorder'].transform([data['sleep_disorder']])[0],
        ]

        # Make prediction
        prediction = model.predict([features])[0]

        return render_template('index.html', prediction_text=f'Stress Level: {prediction}')

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
