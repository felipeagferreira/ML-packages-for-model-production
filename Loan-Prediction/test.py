import os
import sys
import pandas as pd

# Ensure the project root is in the Python path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))  # Gets 'ml-submission'
sys.path.append(ROOT_DIR)  # Add 'ml-submission' to sys.path

# Now import LoanModel
from model.inference import LoanModel

# Load the trained model pipeline
model = LoanModel()

# Create a sample input DataFrame (Ensure it matches feature names from training)
sample_data = pd.DataFrame({
    "person_age": [27.764],
    "person_gender": ["male"],
    "person_education": ["Associate"],
    "person_income": [80319],
    "person_emp_exp": [5.4103],
    "person_home_ownership": ["MORTGAGE"],
    "loan_amnt": [9583.1575],
    "loan_intent": ["VENTURE"],
    "loan_int_rate": [11.006606],
    "loan_percent_income": [0.139725],
    "cb_person_cred_hist_length": [5.867489],
    "credit_score": [632.608756],
    "previous_loan_defaults_on_file": ["Yes"]
})

# Run predictions
predictions, probabilities = model.predict(sample_data)

print(f"Predictions: {predictions}")
print(f"Probabilities: {probabilities}")