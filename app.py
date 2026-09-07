from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PredictPayload(BaseModel):
    value: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }

@app.post("/predict")
def predict(payload: PredictPayload):
    # Basic math operation to satisfy the ML inference placeholder
    return {
        "input": payload.value,
        "prediction": payload.value * 2
    }