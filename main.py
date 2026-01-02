from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Real-Time Fraud Detection API")

class Transaction(BaseModel):
    amount: float
    user_id: str
    merchant_id: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/score")
def score(txn: Transaction):
    # dummy score (replace later)
    risk_score = 0.85 if txn.amount > 1000 else 0.1
    return {
        "risk_score": risk_score,
        "decision": "FRAUD" if risk_score > 0.7 else "LEGIT"
    }
