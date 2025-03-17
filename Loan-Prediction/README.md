# ml-submission


#### Before running the model, first download the dataset using

```bash
python scripts/download_data.py
```

## Installation
Before running the model, install all required dependencies using the following command:

```bash
pip install -r requirements.txt

```

### Installing the Loan Prediction Model Package
Clone the repository and navigate to the root folder:
```bash
git clone https://github.com/felipeagferreira/ml-submission.git
cd ml-submission
pip install -e .
```

## How to Use the Trained Loan Prediction Model
Once you've installed the required dependencies (`requirements.txt`), you can load the trained model and make predictions. 
model/inference.py contains the inference pipeline.

### Importing the Model and Making Predictions. 
To quickly test the trained model with sample input data, simply run:

```bash
python test.py
```