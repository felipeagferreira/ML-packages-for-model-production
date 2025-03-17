# scripts/custom_transformers.py
import numpy as np

def log_transform(X):
    X = X.copy()
    log_features = ['person_income', 'loan_amnt', 'person_emp_exp', 'loan_percent_income']
    X[log_features] = np.log1p(X[log_features])
    return X
