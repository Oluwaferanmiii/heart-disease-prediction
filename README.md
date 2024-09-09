# Heart Disease Prediction Using Machine Learning

This project predicts the likelihood of heart disease in patients based on the UCI Heart Disease dataset using machine learning models.

## Key Features
- Machine learning models used: Logistic Regression, Decision Trees, Random Forest, and SVM.
- Random Forest Classifier chosen due to its high accuracy (1.0), precision, recall, and F1 score.
- GUI built with Tkinter allows easy data input and prediction display.
- Uses SQLite to store patient prediction data.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: Scikit-learn, Pandas, Numpy, Joblib, Tkinter
- **Database**: SQLite

## How to Run the Project
1. **Run the Model Training Script**:
   Train the Random Forest model using:
   ```bash
   python train_model.py

2. **Run the GUI Application**:
    Use the GUI to input patient data and predict heart disease:
    ```bash
   python heart_disease_app.py

   -This will open a Tkinter window where you can input health parameters like age, cholesterol, and blood pressure to predict heart disease. Results will be displayed and stored in the SQLite database.

## Dataset
The project uses the UCI Heart Disease dataset, which contains 1025 observations and 13 features related to heart health.

## License
This project is licensed under the MIT License.