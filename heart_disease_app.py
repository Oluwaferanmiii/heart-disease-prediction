# -*- coding: utf-8 -*-
"""heart_disease_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HqViGJu5TBC7LD0KLNOLJqz6MKrv4gqo
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
from joblib import load
import numpy as np

# Load the trained model and scaler
model = load('heart_disease_model.joblib')
scaler = load('scaler.joblib')

# Function to predict heart disease
def predict_heart_disease(features):
    model = load('heart_disease_model.joblib')
    scaler = load('scaler.joblib')
    features_scaled = scaler.transform([features])
    prediction = model.predict([features_scaled[0]])
    return prediction

# GUI application using Tkinter
class HeartDiseaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Disease Prediction")

        # Create labels and entries for input features
        tk.Label(root, text="Age").grid(row=0)
        tk.Label(root, text="Sex").grid(row=1)
        tk.Label(root,text="Chest Pain Type (cp)").grid(row=2)
        tk.Label(root, text="Resting Blood Pressure (trestbps)").grid(row=3)
        tk.Label(root, text="Cholesterol (chol)").grid(row=4)
        tk.Label(root, text="Fasting Blood Sugar (fbs)").grid(row=5)
        tk.Label(root, text="Resting ECG (restecg)").grid(row=6)
        tk.Label(root, text="Max Heart Rate (thalach)").grid(row=7)
        tk.Label(root, text="Exercise Induced Angina (exang)").grid(row=8)
        tk.Label(root, text="ST Depression (oldpeak)").grid(row=9)
        tk.Label(root, text="Slope of Peak Exercise ST Segment (slope)").grid(row=10)
        tk.Label(root, text="Number of Major Vessels (ca)").grid(row=11)
        tk.Label(root, text="Thalassemia (thal)").grid(row=12)

        self.age = tk.Entry(root)
        self.sex = tk.Entry(root)
        self.cp = tk.Entry(root)
        self.trestbps = tk.Entry(root)
        self.chol = tk.Entry(root)
        self.fbs = tk.Entry(root)
        self.restecg = tk.Entry(root)
        self.thalach = tk.Entry(root)
        self.exang = tk.Entry(root)
        self.oldpeak = tk.Entry(root)
        self.slope = tk.Entry(root)
        self.ca = tk.Entry(root)
        self.thal = tk.Entry(root)

        self.age.grid(row=0, column=1)
        self.sex.grid(row=1, column=1)
        self.cp.grid(row=2, column=1)
        self.trestbps.grid(row=3, column=1)
        self.chol.grid(row=4, column=1)
        self.fbs.grid(row=5, column=1)
        self.restecg.grid(row=6, column=1)
        self.thalach.grid(row=7, column=1)
        self.exang.grid(row=8, column=1)
        self.oldpeak.grid(row=9, column=1)
        self.slope.grid(row=10, column=1)
        self.ca.grid(row=11, column=1)
        self.thal.grid(row=12, column=1)

        # Prediction button
        tk.Button(root, text='Predict', command=self.make_prediction).grid(row=13, column=1, pady=4)

    def create_input_field(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=5, pady=5)
        setattr(self, label_text.replace(" ", "_").lower(), entry)

    def make_prediction(self):
        try:
            features = [
                float(self.age.get()), int(self.sex.get()), int(self.cp.get()), float(self.trestbps.get()),
                float(self.chol.get()), int(self.fbs.get()), int(self.restecg.get()), float(self.thalach.get()),
                int(self.exang.get()), float(self.oldpeak.get()), int(self.slope.get()), float(self.ca.get()), int(self.thal.get())
            ]
            prediction = predict_heart_disease(features)
            messagebox.showinfo("Prediction Result", f"Prediction: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}")
            self.save_prediction_to_db(features, prediction)
        except Exception as e:
            messagebox.showerror("Error", f"Error in prediction: {e}")

    def save_prediction_to_db(self, features, prediction):
        conn = sqlite3.connect('heart_disease.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO predictions (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (*features, prediction))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDiseaseApp(root)
    root.mainloop()

"""# **Code Explanation:**
1. Predict_heart_disease Function
*   The function predicts heart disease based on the features provided,
*   It uses the trained 'RandomForestClassifier' model ('train_model') to predict whether a patient has ('1') or not ('0').

2. Error Handling
*   The 'make_prediction' method includes error handling to catch
exceptions, ensuring that the application doesnt crash if invalid input is entered.

3. Saving Predictions
*   The 'save_prediction_to_db' method saves the predicted values along with input features to the SQLite database('heart_disease.db'), ensuring the predictions are stored for future reference.

4. GUI Application
*   The tkinter GUI ('HeartDiseaseApp') allows users to enter patient information and click a button to predict heart disease.
*   Prediction results are displayed using a message box and saved to the database.








"""