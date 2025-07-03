from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load(os.path.join('model', 'model.pkl'))
scaler = joblib.load(os.path.join('model', 'scaler.pkl'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    result = None
    confidence = None

    if request.method == 'POST':
        try:
            # Get input from form
            input_data = [float(request.form[f'f{i}']) for i in range(8)]
            scaled_input = scaler.transform([input_data])
            prediction = model.predict(scaled_input)[0]
            prediction_proba = model.predict_proba(scaled_input)[0][1]

            result = "Diabetic" if prediction == 1 else "Not Diabetic"
            confidence = round(prediction_proba * 100, 2)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
