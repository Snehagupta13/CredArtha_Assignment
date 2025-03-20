import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import shap
import joblib

# Load the credit bureau dataset
bureau_df = pd.read_csv("../Datacollection/credit_bureau_reports.csv")

# Display the first few rows
print("First 5 rows:\n", bureau_df.head())

# Check dataset size
print("Dataset shape:", bureau_df.shape)

# Check class distribution
print("Class distribution:\n", bureau_df["Risk"].value_counts())

# Handle missing values (if any)
bureau_df = bureau_df.fillna(bureau_df.median())

# Define features and target
# Features: Credit Score, Debt-to-Income Ratio, Missed Payments, Loan Utilization, Total Outstanding Debt, Recent Credit Inquiries
# Target: Risk (High-risk = 1, Low-risk = 0)
X = bureau_df[["Credit_Score", "Debt_to_Income_Ratio", "Missed_Payments", "Credit_Card_Utilization", "Total_Outstanding_Debt", "Recent_Credit_Inquiries"]]
y = bureau_df["Risk"]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Balance the dataset using SMOTE (if imbalanced)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model for future use
joblib.dump(model, "credit_risk_model.pkl")
print("Credit risk model saved to 'credit_risk_model.pkl'.")

# SHAP for explainability
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Visualize SHAP summary plot
shap.summary_plot(shap_values, X_test, feature_names=X.columns)