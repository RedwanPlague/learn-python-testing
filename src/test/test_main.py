from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World!"}


def test_get_list():
    response = client.get(f"/list?start={10}&length={4}")
    assert response.status_code == 200
    assert response.json() == {"list": list(range(10, 14))}


def test_use_data_ok():
    response = client.post("/", json={"id": 4, "name": "redwan"})
    assert response.status_code == 200
    assert response.json() == {"user": "redwan_4"}


def test_use_data_invalid_id():
    response = client.post("/", json={"id": 0, "name": "redwan"})
    assert response.status_code == 400
    assert response.json() == {"detail": "ID must be positive"}
