# Credit Risk Analysis and Model Training

This project performs credit risk analysis using a synthetic dataset containing financial information. It includes data preprocessing, model training, evaluation, and explainability using SHAP.

## Features
- Data Cleaning: Handles missing values using median imputation.
- Data Balancing: Applies SMOTE to address class imbalance.
- Model Training: Uses a Random Forest classifier.
- Evaluation: Provides accuracy and detailed classification reports.
- Explainability: Visualizes feature impact using SHAP.

## Requirements
Install the required packages using:
```bash
pip install pandas scikit-learn imbalanced-learn shap joblib
```

## Usage
1. Place your dataset in `../Datacollection/credit_bureau_reports.csv`.
2. Run the script:
```bash
python credit_risk_analysis.py
```
3. Model results and SHAP visualizations will be displayed.
4. The trained model will be saved as `credit_risk_model.pkl`.

## Explanation
- **Data Preprocessing:** Missing values are handled using median imputation. Features are scaled using `StandardScaler`.
- **SMOTE:** Balances the dataset to mitigate class imbalance.
- **Modeling:** A Random Forest classifier is used for classification.
- **Evaluation:** Performance is measured using accuracy and a classification report.
- **Explainability:** SHAP values provide insights into feature importance.



