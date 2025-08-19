from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_order():
    payload = {"customer_email": "test@example.com", "total_amount": 42.5}
    created = client.post("/orders/", json=payload).json()
    assert created["status"] == "pending"

    fetched = client.get(f"/orders/{created['id']}").json()
    assert fetched["customer_email"] == "test@example.com"