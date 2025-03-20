import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Generate synthetic transactions
def generate_transactions(num_customers=10, transactions_per_customer=50):
    data = []
    for cust_id in range(1, num_customers + 1):
        for _ in range(transactions_per_customer):
            transaction = {
                "Transaction_ID": fake.uuid4(),
                "Customer_ID": cust_id,
                "Date": fake.date_between(start_date="-1y", end_date="today").strftime(random.choice(["%Y-%m-%d", "%d/%m/%Y", "%b %d, %Y"])),
                "Description": fake.sentence(nb_words=5),
                "Amount": round(random.uniform(10, 1000), 2)
            }
            # Introduce missing values and inconsistencies
            if random.random() < 0.1:
                transaction["Description"] = None
            if random.random() < 0.1:
                transaction["Amount"] = None
            data.append(transaction)
    return pd.DataFrame(data)

# Generate synthetic credit bureau reports
def generate_bureau_reports(num_customers=10):
    data = []
    for cust_id in range(1, num_customers + 1):
        report = {
            "Customer_ID": cust_id,
            "Credit_Score": random.randint(300, 900),
            "Existing_Loans": random.randint(0, 5),
            "Credit_Card_Utilization": round(random.uniform(0, 100), 2),
            "Missed_Payments": random.randint(0, 12),
            "Total_Outstanding_Debt": round(random.uniform(0, 100000), 2),
            "Debt_to_Income_Ratio": round(random.uniform(0, 50), 2),
            "Recent_Credit_Inquiries": random.randint(0, 10)  # Additional feature
        }
        # Introduce missing values (optional)
        if random.random() < 0.1:
            report["Credit_Score"] = None
        if random.random() < 0.1:
            report["Missed_Payments"] = None
        data.append(report)
    return pd.DataFrame(data)

# Save to CSV
transactions_df = generate_transactions()
bureau_df = generate_bureau_reports()

# Add a target variable (Risk) to the bureau dataset
bureau_df["Risk"] = bureau_df["Credit_Score"].apply(lambda x: 1 if x < 600 else 0)

# Save datasets to CSV files
transactions_df.to_csv("financial_transactions.csv", index=False)
bureau_df.to_csv("credit_bureau_reports.csv", index=False)

print("Synthetic datasets generated and saved:")
print("- financial_transactions.csv")
print("- credit_bureau_reports.csv")