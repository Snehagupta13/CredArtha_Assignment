from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FinancialInsightsRequest(BaseModel):
    transactions: str
    risk_score: int

@app.post("/generate-insights")
def generate_insights_api(request: FinancialInsightsRequest):
    try:
        # Generate prompts
        financial_health_prompt = generate_financial_health_summary(request.transactions, request.risk_score)
        risk_assessment_prompt = generate_risk_assessment(request.risk_score)
        recommendations_prompt = generate_personalized_recommendations(request.transactions, request.risk_score)

        # Generate insights
        financial_health = generate_insights(financial_health_prompt)
        risk_assessment = generate_insights(risk_assessment_prompt)
        recommendations = generate_insights(recommendations_prompt)

        return {
            "financial_health": financial_health,
            "risk_assessment": risk_assessment,
            "recommendations": recommendations,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)