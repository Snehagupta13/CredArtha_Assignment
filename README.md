# CredArtha_Assignment
# Financial Insights Generation Using LLMs

This project aims to generate human-readable financial insights using open-source Large Language Models (LLMs). It involves cleaning and structuring financial data, categorizing transactions, flagging high-risk borrowers, and generating insights such as financial health summaries, risk assessments, and personalized recommendations.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tasks](#tasks)
   - [Task 0: Environment Setup](#task-0-environment-setup)
   - [Task 1: Data Cleaning and Structuring](#task-1-data-cleaning-and-structuring)
   - [Task 2: Transaction Categorization Using NLP](#task-2-transaction-categorization-using-nlp)
   - [Task 3: Bureau Risk Model](#task-3-bureau-risk-model)
   - [Task 4: LLM-Based Financial Insights Using Open-Source Models](#task-4-llm-based-financial-insights-using-open-source-models)
   - [Task 5: Deploying the Model as an API](#task-5-deploying-the-model-as-an-api)
3. [Setup Instructions](#setup-instructions)
4. [Running the Code](#running-the-code)
5. [API Usage](#api-usage)
6. [Future Enhancements](#future-enhancements)

---

## Project Overview

The project is divided into six tasks:
1. **Environment Setup**: Set up the Python environment and install dependencies.
2. **Data Cleaning and Structuring**: Clean and structure raw financial data.
3. **Transaction Categorization Using NLP**: Categorize transactions using Natural Language Processing (NLP).
4. **Bureau Risk Model**: Develop a risk model to flag high-risk borrowers.
5. **LLM-Based Financial Insights**: Use open-source LLMs to generate financial insights.
6. **Deploying the Model as an API**: Deploy the LLM as an API for real-time insights.

---

## Tasks

### Task 0: Environment Setup
Set up the Python environment and install all required dependencies.

#### Steps:
1. Create a virtual environment:
   ```bash
   python -m venv myenv
   
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