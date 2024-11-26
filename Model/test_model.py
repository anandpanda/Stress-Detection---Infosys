import joblib
import pandas as pd

# Load the trained model and scaler
model = joblib.load('stress_detection_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define the feature names as in the training dataset
feature_names = [
    'Snoring Rate', 'Respiratory Rate', 'Body Temperature', 'Limb Movement',
    'Blood Oxygen', 'Eye Movement', 'Sleep Hours', 'Heart Rate'
]

# Provide the test input as a dictionary
input_data_stressed = {
    'Snoring Rate': 95, 
    'Respiratory Rate': 26, 
    'Body Temperature': 99, 
    'Limb Movement': 15, 
    'Blood Oxygen': 90, 
    'Eye Movement': 98, 
    'Sleep Hours': 2, 
    'Heart Rate': 78
}

input_data_not_stressed = {
    'Snoring Rate': 50, 
    'Respiratory Rate': 18, 
    'Body Temperature': 97, 
    'Limb Movement': 8, 
    'Blood Oxygen': 95, 
    'Eye Movement': 85, 
    'Sleep Hours': 8, 
    'Heart Rate': 62
}

# Convert input to a DataFrame
input_df = pd.DataFrame([input_data_not_stressed])

# Scale the input
input_scaled = scaler.transform(input_df)

# Predict using the model
prediction = model.predict(input_scaled)

# Display the result
stress_status = "Stressed" if prediction[0] == 1 else "Not Stressed"
print(f"Stress Prediction: {stress_status}")
