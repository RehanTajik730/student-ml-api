from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PredictPayload(BaseModel):
    value: float

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1"
    }), 200

@app.post("/predict")
def predict(payload: PredictPayload):
    # Basic math operation to satisfy the ML inference placeholder
    return {
        "input": payload.value,
        "prediction": payload.value * 2
    }