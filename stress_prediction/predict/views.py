from django.shortcuts import render, redirect
import joblib
import pandas as pd
from .models import StressPrediction
from django.contrib.auth.models import User

# Load the trained model and scaler
MODEL_PATH = 'D:/Infosys Springboard/Stress Detection and Prediction using ANN/Model/stress_detection_model.pkl'
SCALER_PATH = 'D:/Infosys Springboard/Stress Detection and Prediction using ANN/Model/scaler.pkl'

model = joblib.load(MODEL_PATH)  # Load the logistic regression model
scaler = joblib.load(SCALER_PATH)  # Load the scaler

def predict_recommend(request):
    # Fetch user data from the session
    user_data = request.session.get("user_data")

    if user_data:
        # Ensure the feature order matches exactly what was used during training
        input_data = {
            "Snoring Rate": [user_data["snoring_rate"]],
            "Respiratory Rate": [user_data["respiratory_rate"]],
            "Body Temperature": [user_data["body_temperature"]],
            "Limb Movement": [user_data["limb_movement"]],
            "Blood Oxygen": [user_data["blood_oxygen"]],
            "Eye Movement": [user_data["eye_movement"]],
            "Sleep Hours": [user_data["sleep_hours"]],
            "Heart Rate": [user_data["heart_rate"]]
        }

        # Correct feature order during prediction
        feature_order = [
            "Snoring Rate",
            "Respiratory Rate",
            "Body Temperature",
            "Limb Movement",
            "Blood Oxygen",
            "Eye Movement",
            "Sleep Hours",
            "Heart Rate"
        ]

        # Create a DataFrame with the correct column names and order
        input_df = pd.DataFrame(input_data, columns=feature_order)

        # Scale the input data using the pre-loaded scaler
        input_data_scaled = scaler.transform(input_df)

        # Make prediction using the logistic regression model
        prediction = model.predict(input_data_scaled)[0]

        # Set result message based on prediction
        if prediction == 1:  # Assuming '1' is for stressed
            result_message = "You are stressed."
            additional_info = [
                "No Worries!!",
                "Here are a few ways to break out of it:",
                "1. Try deep breathing exercises.",
                "2. Take a short walk.",
                "3. Practice mindfulness or meditation."
            ]
        else:
            result_message = "Not stressed."
            additional_info = [
                "Hurray! You are doing great!",
                "Here are a few tips to maintain your well-being:",
                "1. Keep up with your good habits.",
                "2. Take breaks to recharge.",
                "3. Keep pursuing activities you enjoy!"
            ]

        # Save data to the database
        user = request.user
        StressPrediction.objects.create(
            user=user,
            limb_movement=user_data["limb_movement"],
            sleep_hours=user_data["sleep_hours"],
            snoring_rate=user_data["snoring_rate"],
            eye_movement=user_data["eye_movement"],
            body_temperature=user_data["body_temperature"],
            heart_rate=user_data["heart_rate"],
            blood_oxygen=user_data["blood_oxygen"],
            respiratory_rate=user_data["respiratory_rate"],
            prediction_result="stressed" if prediction == 1 else "not stressed"
        )

        context = {
            'result_message': result_message,
            'additional_info': additional_info,
        }

        return render(request, 'predict/predict-recommend.html', context)
    else:
        # If no data is available in session, redirect to form
        return redirect("user_data_form")
