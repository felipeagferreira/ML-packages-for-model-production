import os
import kaggle

# Define dataset details
KAGGLE_DATASET = "udaymalviya/bank-loan-data"
DATA_DIR = os.path.join(os.getcwd(), "dataset")  # Converts "dataset" into an absolute path

# Ensure Kaggle API authentication exists
if not os.path.exists(os.path.expanduser("~/.kaggle/kaggle.json")):
    print("⚠️ Kaggle API credentials not found! Please add kaggle.json to ~/.kaggle/")

# Download dataset
os.makedirs(DATA_DIR, exist_ok=True)  # Ensures the directory exists
kaggle.api.dataset_download_files(KAGGLE_DATASET, path=DATA_DIR, unzip=True)
print(f"✅ Dataset downloaded to {DATA_DIR}")
