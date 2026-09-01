from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_refund():
    payload = {"order_id": 1, "amount": 10.0, "reason": "duplicate charge"}
    response = client.post("/refunds/", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "processed"