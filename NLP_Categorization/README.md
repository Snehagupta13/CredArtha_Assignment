# Financial Transaction Classification

This project classifies financial transactions into categories using NLP models, including Logistic Regression and BERT.

## Features
- Preprocesses transaction descriptions using Regex and TF-IDF.
- Implements logistic regression for classification.
- Utilizes BERT embeddings for enhanced accuracy.
- Saves models using Joblib.

## Requirements
```bash
pip install pandas scikit-learn transformers torch joblib
```

## Usage
1. Place `financial_transactions.csv` in the project directory.
2. Run the desired model script:
   ```bash
   python tfidf_model.py  # For Logistic Regression
   python bert_model.py   # For BERT Model
   ```
3. View the classification report and accuracy.

## Contact
For any queries, feel free to reach out.

