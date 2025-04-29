# Customer Churn Prediction System 🚀

## 📚 Project Overview

This project demonstrates a complete **Machine Learning deployment pipeline** to predict **customer churn** based on customer activity data.

**Business Problem:**  
Customer churn has a direct impact on business revenue. Predicting churn early enables companies to take proactive measures to retain their customers.


## ⚙️ Project Architecture

- Data Cleaning and Preprocessing
- Feature Engineering
- Model Training (Logistic Regression, XGBoost)
- Model Evaluation
- Flask API Creation
- Frontend Form Integration (HTML)
- Docker Containerization

## 📊 Dataset Details

- **Source:** IBM Telco Customer Churn Dataset
- **Records:** 7043
- **Features:** 21
- **Target Variable:** `Churn` (Yes/No)

Features include customer demographics, account information, services used, and billing details.


## 🛠️ Technologies Used

| Technology           | Purpose                                           |
|----------------------|---------------------------------------------------|
| Python               | Core programming language                        |
| pandas, numpy        | Data manipulation and preprocessing               |
| scikit-learn         | ML model training (Logistic Regression)           |
| xgboost              | Advanced ML modeling (XGBoost Classifier)          |
| Flask                | Backend API creation                              |
| HTML                 | Frontend form for user input                      |
| Docker               | Containerization and portability                  |
| Gunicorn             | WSGI server for production-ready deployment       |


## 🔥 Machine Learning Models Used

### Logistic Regression
- **Description:** A statistical method for binary classification.
- **Reason for Use:** Fast, interpretable, and performs well on structured, linear data like churn prediction.

### XGBoost Classifier
- **Description:** An efficient and scalable implementation of gradient boosting.
- **Reason for Use:** Captures complex patterns, handles imbalanced data better, and improves model accuracy over simple models.

## 🧹 Data Preprocessing Highlights

- Handled missing values and invalid entries
- Label Encoding for binary categorical variables
- One-Hot Encoding for multi-category features
- Dealt with class imbalance
- Train-Test Split (stratified to preserve churn ratio)


## 🖥️ Application Workflow

1. User inputs customer information via an HTML form.
2. Flask backend API receives the inputs.
3. Model processes the inputs and predicts churn status (Yes/No).
4. Output displayed back to the user via the frontend.
5. Entire system packaged inside Docker for easy deployment.

## ⚙️ How to Run Locally with Docker

### Step 1: Clone the Repository
git clone https://github.com/<your-github-username>/Customer-Churn-Prediction-System.git
cd Customer-Churn-Prediction-System

Step 2: Build Docker Image
docker build -t churn-predictor .

Step 3: Run Docker Container
docker run -p 5000:5000 churn-predictor

Step 4: Access Application
Open browser and navigate to:
👉 http://127.0.0.1:5000

## Future Improvements

We can add an interactive dashboard using Streamlit or Dash

Integrate PostgreSQL database for customer information storage

Deploy on AWS EC2 with HTTPS and CI/CD pipelines

Improve model performance by hyperparameter tuning


Conclusion
This project demonstrates complete ML lifecycle management — from data exploration to live serving of models inside containers — a critical skillset for production-grade Data Science and Machine Learning Engineering roles.


Author
Hridesh Roshan Mund

📧 Email: hrideshmund@gmail.com

🌍 Location: Dublin, Ireland

🌐 LinkedIn Profile: www.linkedin.com/in/hridesh-roshan-mund-3280051ba


**NOTE: Please read the files carefully this project it for self learning and the htmls used are AI generated which will not give you 100% working results but can make your learning progess. Thanks
