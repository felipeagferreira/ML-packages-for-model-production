

1. Project Overview

This project is based on building a productive Loan Default Prediction model to predict loan repayment. The goal is to develop a robust model pipeline that can do a fast model comparison analysis in a reproducible and scalable way. The data used for this project is a bank loan dataset which can be loaded from the following page of Kaggle platform 
https://www.kaggle.com/datasets/udaymalviya/bank-loan-data?select=loan_data.csv.



2. Solution Summary 
The solution is design as follows:
    1. Model EDA to analyse statistical distributions and correlations of each feature;
    2. Develop a feature engineering pipeline based on reproducibility and scalability to ensure that transformations are consistently applied to new data.
    3. Develop a robust model pipeline to compare different models designed in a way that first incorporates hyperparameter tuning to select the best estimator      of each independent model, compare them all in an autonomous way to select the best model and do the final testing on it. I included in the model pipeline       the following supervised ML algorithms: Logistic Regression, Random Forest, XGBoost and Stacking Classifier.

These models provide a balance of interpretability, robustness, and predictive power, which makes the model pipeline capable to support both individual ML models like logistic regression as well as ensemble models of different types, like Random Forest (bagging), XGBoost (boosting) and Stacking Classifier which gives different weight for each estimator's output which is determined by another logistic regression model. Such ensemble models are also good in minimizing bias and control overfitting. Models are compared via AUC metric, which is a strong choice for evaluating loan prediction models because it measures how well the model distinguishes between approved and rejected loan applications. All these models were built in a way that uses the feature engineering pipeline to run the validation analysis after the hyperparameter tuning to first obtain the best estimator of each model, use them on the Stacking Classifier with the aim to find a better model from these first best models and then compare them all to select the final best model to do the testing.


3. Challenges & Reflections – Issues encountered, solutions, and potential improvements.
This project made me face a big diversity of challenges related to statistical analysis, technical debugging and model design optimization. Each issue required deep research to find viable solutions in a way that raised lots of reflections for me in how to design, develop and deploy efficient advanced ML models in a scalable and reproducible way. Potential improvements were: software ML engineering skills to transform each piece of a machine learning model into a reproducible pipeline well connected to the other pieces in a way that they all can do the whole lifecycle jobs on new data in an autonomously productive way. Very interesting.


4. Time Breakdown – Approximate time spent on different tasks.
Each task took quite a good time, including
*) Task 1 - Dataset Selection and Loading: 1 hour
*) Task 2 - Feature Engineering Pipeline: 2 hours
*) Task 3 - Model Development: 3 hours   
*) Task 4 - Model Package Testing: 10 hours
Took longer time on Task 4 because of the many debugging challenges I faced during the development of the model package and its benchmark test analysis.

5. Model Decisions & Interpretations 
The best selected model was XGBoost with Validation AUC = 0.9607 and Test AUC = 0.961. The hyperparameter tuning included on the model pipeline surely contributed a lot for the model to obtain such good test AUC, which is a little above validation AUC. Data quality and the feature engineering we included in our model pipeline were also highly relevant for this result, as shown on the feature importance plot where we can see that the most important feature for the final model XGBoost was 'cat_previous_loan_defaults_on_file_No' which is a categorical feature created by the feature engineering pipeline.   
   
6. Model Monitoring and Performance Tracking – How the model could handle larger datasets or be improved for deployment.
To ensure the model remains effective over time, the following metrics should be monitored:

    a. AUC-ROC Score: Measures the model’s ability to distinguish between approved and rejected loans.
    b. Precision & Recall: Especially important if false positives (wrongly approved loans) or false negatives (missed approvals) have business impact.
    c. F1-Score: Balances precision and recall to track overall classification performance.
    d. Feature Importance Stability: Compares feature impact over different time periods.

These metrics were all included on the model pipeline. A good way to detect concept is to compare actual loan repayment outcomes with predicted values to see if the model keeps its same opinion or starts changing its behavior, whereas an efficient way to identify shifts in input feature distributions over time is with Population Stability Index (PSI). As justification, AUC-ROC & F1-Score ensure the model's predictive power remains high and PSI & Concept Drift detection prevent inaccurate predictions due to changing customer behaviors.

Frameworks like EvidentlyAI, MLflow, or a cloud monitoring dashboard could be useful to implement the model.
