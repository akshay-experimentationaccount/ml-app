import pytest
import json
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ML Model API is running" in response.data

def test_predict(client):
    data = {"features": [50, 83311, 13, 0, 0, 40]}
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert "prediction" in json.loads(response.data)
