import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from transformers import BertTokenizer, BertModel
import torch
import numpy as np

# Load the synthetic transactions dataset
transactions_df = pd.read_csv("../Datacollection/financial_transactions.csv")

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

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Function to get BERT embeddings
def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

# Get BERT embeddings for training and testing data
X_train = np.vstack(train_df["Description"].apply(get_bert_embeddings))
X_test = np.vstack(test_df["Description"].apply(get_bert_embeddings))

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

# Save the model and tokenizer for future use
import joblib
joblib.dump(model, "bert_nlp_model.pkl")
print("BERT-based model saved to 'bert_nlp_model.pkl'.")