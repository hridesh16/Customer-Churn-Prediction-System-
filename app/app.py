# app.py

from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('Models/logistic_regression_model.pkl')

# Feature list - must match model input
feature_names = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
                 'MultipleLines_No phone service', 'MultipleLines_Yes',
                 'InternetService_Fiber optic', 'InternetService_No',
                 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
                 'OnlineBackup_No internet service', 'OnlineBackup_Yes',
                 'DeviceProtection_No internet service', 'DeviceProtection_Yes',
                 'TechSupport_No internet service', 'TechSupport_Yes',
                 'StreamingTV_No internet service', 'StreamingTV_Yes',
                 'StreamingMovies_No internet service', 'StreamingMovies_Yes',
                 'Contract_One year', 'Contract_Two year',
                 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
                 'PaymentMethod_Mailed check']

@app.route('/')
def home():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = []

    for feature in feature_names:
        value = float(request.form.get(feature))
        input_data.append(value)

    features = np.array([input_data])
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction=prediction, features=feature_names)

if __name__ == '__main__':
    app.run(debug=True)

