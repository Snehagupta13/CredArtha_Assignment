import pandas as pd
from sqlalchemy import create_engine
import re

# Load data
transactions_df = pd.read_csv("financial_transactions.csv")
bureau_df = pd.read_csv("credit_bureau_reports.csv")

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

# Load into PostgreSQL
# Replace 'user', 'password', 'localhost', '5432', and 'credartha_db' with your actual PostgreSQL credentials
engine = create_engine("postgresql://user:password@localhost:5432/credartha_db")

# Load transactions data
try:
    transactions_df.to_sql("transactions", engine, if_exists="replace", index=False)
    print("Transactions data loaded successfully.")
except Exception as e:
    print(f"Error loading transactions data: {e}")

# Load bureau data
try:
    bureau_df.to_sql("bureau_reports", engine, if_exists="replace", index=False)
    print("Bureau reports data loaded successfully.")
except Exception as e:
    print(f"Error loading bureau reports data: {e}")