import joblib
import pandas as pd
import os
import sys

# Ensure the project root is in the Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves back to 'ml-submission'
sys.path.append(ROOT_DIR)  # Add 'ml-submission' to sys.path

# Ensure scripts folder is explicitly in path
SCRIPTS_PATH = os.path.join(ROOT_DIR, "scripts")
sys.path.append(SCRIPTS_PATH)

# Import necessary custom transformers
from scripts.custom_transformers import log_transform

# Define model path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "final_model.joblib")


class LoanModel:
    def __init__(self, model_path=MODEL_PATH):
        """Loads the trained model pipeline"""
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model file not found at {model_path}. Ensure the model is saved.")
        
        self.model = joblib.load(model_path)
        print("Model loaded successfully!")

    def predict(self, X: pd.DataFrame):
        """
        Predicts loan approval using the trained model pipeline.
        
        Parameters:
        - X (pd.DataFrame): Input features in DataFrame format.
        
        Returns:
        - predictions (np.ndarray): Predicted loan approval classes.
        - probabilities (np.ndarray or None): Probability estimates for class 1 (loan approved).
        """
        if not isinstance(X, pd.DataFrame):
            raise ValueError("❌ Input data must be a pandas DataFrame.")

        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)[:, 1] if hasattr(self.model, 'predict_proba') else None
        return predictions, probabilities