import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the synthetic transactions dataset
transactions_df = pd.read_csv("financial_transactions.csv")

# Handle missing values in the Description column
transactions_df["Description"] = transactions_df["Description"].fillna("Unknown")

# Define categories and their keywords
categories = {
    "Salary": ["salary", "payroll", "income"],
    "Shopping": ["amazon", "flipkart", "myntra", "purchase"],
    "Food & Dining": ["swiggy", "zomato", "starbucks", "restaurant"],
    "Loan EMI": ["loan emi", "hdfc loan", "sbi home loan"],
    "Utilities": ["electricity bill", "water bill", "broadband bill"],
    "Cash Withdrawal": ["atm withdrawal", "cash withdrawal"],
    "Transfers": ["upi transfer", "imps", "neft"]
}

# Function to categorize transactions using Regex
def categorize_transaction(description):
    description = str(description).lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(rf"\b{keyword}\b", description):
                return category
    return "Other"  # Default category if no match is found

# Add a ground truth category column
transactions_df["True_Category"] = transactions_df["Description"].apply(categorize_transaction)

# Split the data into training and testing sets
train_df, test_df = train_test_split(transactions_df, test_size=0.2, random_state=42)

# Clean and preprocess text data
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    return text

train_df["Cleaned_Description"] = train_df["Description"].apply(clean_text)
test_df["Cleaned_Description"] = test_df["Description"].apply(clean_text)

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
X_train = vectorizer.fit_transform(train_df["Cleaned_Description"])
X_test = vectorizer.transform(test_df["Cleaned_Description"])

# Define target variable
y_train = train_df["True_Category"]
y_test = test_df["True_Category"]

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model and vectorizer for future use
import joblib
joblib.dump(model, "nlp_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("Model and vectorizer saved to 'nlp_model.pkl' and 'tfidf_vectorizer.pkl'.")