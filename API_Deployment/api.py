from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import torch
from transformers import BertTokenizer, BertModel
import numpy as np

# Load the trained BERT-based model
model = joblib.load("../NLP_Categorization/bert_nlp_model.pkl")

# Load the BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased")

app = FastAPI()

class TransactionRequest(BaseModel):
    description: str

# Function to get BERT embeddings
def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

@app.post("/predict")
def predict(request: TransactionRequest):
    # Get BERT embeddings for the input text
    embeddings = get_bert_embeddings(request.description)
    # Predict the category
    prediction = model.predict(embeddings)
    return {"category": prediction[0]}

# Run the API
# Command: uvicorn api:app --reload