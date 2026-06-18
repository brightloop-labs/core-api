from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_bulk_create_and_list():
    for i in range(5):
        client.post("/orders/", json={"customer_email": f"user{i}@example.com", "total_amount": 10.0 + i})

    response = client.get("/orders/?limit=3")
    assert response.status_code == 200
    assert len(response.json()) <= 3