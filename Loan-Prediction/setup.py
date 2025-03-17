# Model Package
from setuptools import setup, find_packages

setup(
    name="loan_prediction_model",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "xgboost",
        "joblib",
        "matplotlib",
        "seaborn",
        "feature-engine",
        "lightgbm"
    ],
    package_data={
        "model": ["final_model.joblib"],  # Ensure the model file is included in the package
    },
    include_package_data=True,
    python_requires=">=3.7",  # Ensure compatibility with Python 3.7+
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="Felipe A. G. Ferreira",
    description="A loan prediction model package that includes a trained pipeline for classification.",
    url="https://github.com/felipeagferreira/ml-submission",
)