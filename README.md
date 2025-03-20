# CredArtha_Assignment
CredArtha_Assignment/
│
├── Datacollection/                    # Task 0: Synthetic Data Generation
│   ├── collect.py                     # Script to generate synthetic data
│   ├── financial_transactions.csv     # Generated transactions data
│   ├── credit_bureau_reports.csv      # Generated credit bureau data
│   └── README.md                      # Documentation for Task 0
│
├── Database_setup/                    # Task 1: ETL Pipeline
│   ├── mongo.py                       # Script for MongoDB ETL
│   ├── postgres.py                    # Script for PostgreSQL ETL (optional)
│   └── README.md                      # Documentation for Task 1
│
├── NLP_Categorization/                # Task 2: NLP-Based Transaction Categorization
│   ├── nlp_model.py                   # Script for NLP-based categorization
│   ├── bert_nlp_model.py              # Script for BERT-based categorization (Bonus)
│   ├── nlp_model.pkl                  # Trained TF-IDF model
│   ├── tfidf_vectorizer.pkl           # TF-IDF vectorizer
│   ├── bert_nlp_model.pkl             # Trained BERT model (Bonus)
│   ├── categorized_transactions.csv   # Output of categorized transactions
│   └── README.md                      # Documentation for Task 2
│
├── Credit_Risk_Analysis/              # Task 3: Bureau Report Analysis & Credit Risk Assessment
│   ├── credit_risk_model.py           # Script for credit risk model
│   ├── credit_risk_model.pkl          # Trained credit risk model
│   ├── shap_summary_plot.png          # SHAP explainability plot
│   ├── risk_predictions.csv           # Output of risk predictions
│   └── README.md                      # Documentation for Task 3
│
├── API_Deployment/                    # Bonus: API Deployment
│   ├── api.py                         # FastAPI/Flask script for deployment
│   ├── requirements.txt               # Dependencies for API
│   └── README.md                      # Documentation for API deployment
│
├── requirements.txt                   # Global dependencies for the project
└── README.md                          # Overall project documentation