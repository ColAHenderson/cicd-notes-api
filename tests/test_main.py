from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_note():
    response = client.post("/notes", json={"text": "learn ci/cd"})

    assert response.status_code == 200
    assert response.json() == {"created": "learn ci/cd"}


def test_list_notes():
    client.post("/notes", json={"text": "ship faster"})

    response = client.get("/notes")

    assert response.status_code == 200
    assert "ship faster" in response.json()["notes"]