# Diabetes Prediction Web Application

A machine learning web application that predicts whether a person has diabetes based on medical inputs, using the PIMA Indian Diabetes Dataset. The application includes data preprocessing, model training and evaluation and deployment with a user-friendly Flask-based web interface.

---

## 🌐 Live Demo

👉 [Click here to use the Diabetes Prediction App](https://diabetes-prediction-web-app-ydqt.onrender.com/)

---


## ✅ Features

- Cleaned and preprocessed real-world dataset  
- Trained and evaluated using:
  - Logistic Regression
  - Random Forest Classifier  
- Evaluation metrics used:
  - Accuracy  
  - Precision  
  - Recall  
  - F1 Score  
  - Confusion Matrix  
- Interactive web form using HTML and CSS  
- Flask backend for model inference  
- Displays prediction result and model confidence  

---

## ⚙️ Technologies Used

- Python  
- Flask  
- scikit-learn  
- NumPy  
- Joblib  
- HTML & CSS (for frontend)

---

## 📊 Model Selection

Both **Logistic Regression** and **Random Forest Classifier** were trained and evaluated. Based on better performance across key metrics (Accuracy, Precision, Recall, F1 Score), **Random Forest Classifier** was selected for deployment.

---

## 🧪 Dataset

- **PIMA Indian Diabetes Dataset**  
- Features:
  - Pregnancies  
  - Glucose  
  - Blood Pressure  
  - Skin Thickness  
  - Insulin  
  - BMI  
  - Diabetes Pedigree Function  
  - Age  
- Target: `Outcome` (1 = Diabetic, 0 = Not Diabetic)

Dataset Source: [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## 🚀 How to Run the App Locally

1. **Install Required Libraries:**

   ```bash
   pip install flask joblib numpy scikit-learn
   ```
   
2. **Run the Flask App:**

   ```bash
   python app.py
   ```

3. **Access in Browser:**
Open http://127.0.0.1:5000 to use the prediction interface.

---

## 📥 Input Fields

Users must enter the following 8 medical features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

The app returns a prediction: "Diabetic" or "Not Diabetic", along with the model confidence score in percentage.
