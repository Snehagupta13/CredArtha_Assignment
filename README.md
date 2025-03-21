# CredArtha_Assignment

## Financial Insights Generation Using LLMs

This project generates human-readable financial insights using open-source Large Language Models (LLMs). It involves cleaning and structuring financial data, categorizing transactions, flagging high-risk borrowers, and generating insights such as financial health summaries, risk assessments, and personalized recommendations.

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
    source myenv/bin/activate  # On Windows use 'myenv\Scripts\activate'
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables in a `.env` file:
    ```bash
    GROQ_API_KEY=your_api_key_here
    ```

---

### Task 1: Data Cleaning and Structuring

- Perform data cleaning using `pandas`.
- Handle missing values, outliers, and data normalization.
- Convert financial data into a structured format.

---

### Task 2: Transaction Categorization Using NLP

- Implement an NLP model using `TF-IDF` and `BERT`.
- Classify financial transactions into categories like salary, rent, groceries, etc.
- Provide categorized transaction data as output.

---

### Task 3: Bureau Risk Model

- Build a risk assessment model using logistic regression or decision trees.
- Generate risk scores for borrowers using credit bureau reports.
- Use `SHAP` for model interpretability.

---

### Task 4: LLM-Based Financial Insights Using Open-Source Models

- Generate financial insights using `LangChain` with `ChatGroq`.
- Insights include:
  - Financial health summaries
  - Risk assessments
  - Personalized financial recommendations
  - Additional financial insights

---

### Task 5: Deploying the Model as an API

- Deploy the insights model using `FastAPI` or `Flask`.
- Provide REST API endpoints for generating financial insights in real-time.

---

## Project Structure

```bash
CredArtha_Assignment/
│
├── Datacollection/
│   ├── collect.py
│   ├── financial_transactions.csv
│   ├── credit_bureau_reports.csv
│   └── README.md
│
├── Database_setup/
│   ├── mongo.py
│   └── README.md
│
├── NLP_Categorization/
│   ├── nlp_model.py
│   ├── bert_nlp_model.py
│   ├── nlp_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── bert_nlp_model.pkl
│   ├── categorized_transactions.csv
│   └── README.md
│
├── Credit_Risk_Analysis/
│   ├── credit_risk_model.py
│   ├── credit_risk_model.pkl
│   ├── shap_summary_plot.png
│   ├── risk_predictions.csv
│   └── README.md
│
├── API_Deployment/
│   ├── api.py
│   ├── requirements.txt
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

## Running the Code

1. Ensure all dependencies are installed using:
    ```bash
    pip install -r requirements.txt
    ```
2. Run individual tasks as needed, for example:
    ```bash
    python NLP_Categorization/nlp_model.py
    ```



---

## API Usage

- Start the API using FastAPI:
    ```bash
    uvicorn api:app --reload
    ```


---

## Future Enhancements

- Add additional LLM models for comparison.
- Implement a more advanced financial risk analysis.
- Enhance transaction categorization using large-scale datasets.
- Provide a web UI for user-friendly interaction.

---

## License
This project is licensed under the MIT License.

---



---

Happy Coding! 🚀

