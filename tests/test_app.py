from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health(client):
    response = client.get('/health')
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["application_version"] == "1.1.0"
    assert data["model_version"] == "model-1"

def test_predict_success():
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    assert response.json() == {"input": 10, "prediction": 20}

def test_predict_missing_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "not_a_number"})
    assert response.status_code == 422