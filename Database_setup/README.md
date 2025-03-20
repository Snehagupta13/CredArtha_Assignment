# Financial Data Cleaning and MongoDB Upload

This project loads, cleans, and uploads synthetic financial data to a MongoDB database. It handles customer transactions and credit bureau reports, ensuring data quality through preprocessing.

## Features
- Data cleaning: Standardizes dates, handles missing values, and normalizes text.
- Data storage: Uploads cleaned data to MongoDB.
- Error handling for seamless database operations.

## Requirements
Install required libraries using:
```bash
pip install pandas pymongo numpy
```

## Usage
1. Ensure MongoDB is running locally.
2. Update the MongoDB connection string in the script if needed.
3. Run the script:
```bash
python data_cleaning_upload.py
```
4. Data will be stored in the `credartha_db` database with collections named `transactions` and `bureau_reports`.



