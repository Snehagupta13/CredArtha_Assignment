# Financial Insights Generation using LangChain and Groq

This project uses LangChain with Groq's LLM to generate financial insights from transaction data and risk scores.

## Features
- **Financial Health Summary:** Provides an overview of the user's financial health.
- **Risk Assessment:** Classifies the user's financial risk as high, moderate, or low.
- **Personalized Recommendations:** Suggests financial actions based on transactions and risk score.
- **Additional Insights:** Offers further observations and potential financial risks.

## Prerequisites
- Python 3.9+
- Install necessary packages using:
  ```bash
  pip install langchain langchain_groq python-dotenv
  ```

## Environment Variables
Create a `.env` file with the following:
```env
GROQ_API_KEY=your_groq_api_key
```

## Usage
1. Run the script with sample transactions and risk score:
    ```python
    python main.py
    ```
2. The results will be displayed in the console.

## Example Input
```plaintext
Transactions:
- Jan 1: Salary +$5000
- Jan 2: Rent -$1500
- Jan 3: Groceries -$200
- Jan 4: Utilities -$100
- Jan 5: Entertainment -$300

Risk Score: 75
```

## Example Output
```plaintext
Financial Health: Your financial health is stable with adequate savings.
Risk Assessment: Moderate
Recommendations: Consider reducing discretionary spending.
Additional Insights: Your rent takes up a significant portion of your income.
```

## License
This project is licensed under the MIT License.