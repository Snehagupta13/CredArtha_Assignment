import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq  # Ensure you have langchain_groq installed

# Load environment variables from .env file
load_dotenv()

# Initialize ChatGroq API
groq_api_key = os.getenv("GROQ_API_KEY")
chat_llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant")  # Specify the model


# Define prompts
financial_health_prompt = PromptTemplate(
    input_variables=["transactions", "risk_score"],
    template="Analyze the following transactions and risk score to summarize the financial health:\n\nTransactions:\n{transactions}\n\nRisk Score: {risk_score}\n\nSummary:"
)

risk_assessment_prompt = PromptTemplate(
    input_variables=["risk_score"],
    template="Based on the risk score of {risk_score}, provide a risk assessment (high, moderate, low)."
)

personalized_recommendations_prompt = PromptTemplate(
    input_variables=["transactions", "risk_score"],
    template="Generate personalized financial recommendations based on the following transactions and risk score:\n\nTransactions:\n{transactions}\n\nRisk Score: {risk_score}\n\nRecommendations:"
)

additional_insights_prompt = PromptTemplate(
    input_variables=["transactions", "risk_score"],
    template="Provide additional insights and potential financial risks based on the following transactions and risk score:\n\nTransactions:\n{transactions}\n\nRisk Score: {risk_score}\n\nAdditional Insights:"
)

# Create LLM chains
financial_health_chain = LLMChain(llm=chat_llm, prompt=financial_health_prompt)
risk_assessment_chain = LLMChain(llm=chat_llm, prompt=risk_assessment_prompt)
personalized_recommendations_chain = LLMChain(llm=chat_llm, prompt=personalized_recommendations_prompt)
additional_insights_chain = LLMChain(llm=chat_llm, prompt=additional_insights_prompt)

# Function to generate financial insights
def generate_financial_insights(transactions, risk_score):
    # Generate financial health summary
    financial_health = financial_health_chain.run(transactions=transactions, risk_score=risk_score)

    # Generate risk assessment
    risk_assessment = risk_assessment_chain.run(risk_score=risk_score)

    # Generate personalized recommendations
    recommendations = personalized_recommendations_chain.run(transactions=transactions, risk_score=risk_score)

    # Generate additional insights
    additional_insights = additional_insights_chain.run(transactions=transactions, risk_score=risk_score)

    return {
        "financial_health": financial_health,
        "risk_assessment": risk_assessment,
        "recommendations": recommendations,
        "additional_insights": additional_insights
    }

# Example usage
transactions = """
- Jan 1: Salary +$5000
- Jan 2: Rent -$1500
- Jan 3: Groceries -$200
- Jan 4: Utilities -$100
- Jan 5: Entertainment -$300
"""

risk_score = 75

insights = generate_financial_insights(transactions, risk_score)
print("Financial Health:", insights["financial_health"])
print("Risk Assessment:", insights["risk_assessment"])
print("Recommendations:", insights["recommendations"])
print("Additional Insights:", insights["additional_insights"])