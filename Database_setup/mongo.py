import pandas as pd
from pymongo import MongoClient
import re

# Load data
transactions_df = pd.read_csv("../Datacollection/financial_transactions.csv")
bureau_df = pd.read_csv("../Datacollection/credit_bureau_reports.csv")

# Clean transactions data
def clean_transactions(df):
    # Standardize date format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.strftime("%Y-%m-%d")
    # Handle missing values
    df["Description"] = df["Description"].fillna("Unknown")
    df["Amount"] = df["Amount"].fillna(0)
    # Standardize text
    df["Description"] = df["Description"].str.lower().apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))
    return df

# Clean bureau data
def clean_bureau(df):
    # Handle missing values
    df = df.fillna(0)
    return df

# Clean data
transactions_df = clean_transactions(transactions_df)
bureau_df = clean_bureau(bureau_df)

# Connect to MongoDB
# Replace 'your_connection_string' with your actual MongoDB connection string
client = MongoClient("mongodb://localhost:27017/")  # Default MongoDB connection string
db = client["credartha_db"]  # Replace 'credartha_db' with your database name

# Load transactions data into MongoDB
try:
    transactions_collection = db["transactions"]
    transactions_collection.insert_many(transactions_df.to_dict("records"))
    print("Transactions data loaded successfully into MongoDB.")
except Exception as e:
    print(f"Error loading transactions data into MongoDB: {e}")

# Load bureau data into MongoDB
try:
    bureau_collection = db["bureau_reports"]
    bureau_collection.insert_many(bureau_df.to_dict("records"))
    print("Bureau reports data loaded successfully into MongoDB.")
except Exception as e:
    print(f"Error loading bureau reports data into MongoDB: {e}")