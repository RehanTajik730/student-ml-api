import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health(client):
    response = client.get('/health')
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["application_version"] == "1.1.0"
    assert data["model_version"] == "model-1"

def test_predict_success(client):
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200

def test_predict_missing_input(client):
    response = client.post("/predict", json={})
    # FastAPI automatically returns 422 for missing required fields, 
    # but 400 is included in case you have custom error handling.
    assert response.status_code in [400, 422]

def test_predict_invalid_input(client):
    response = client.post("/predict", json={"value": "not_a_number"})
    assert response.status_code in [400, 422]