from starlette.testclient import TestClient

from additional_status_codes.tutorial001 import app

client = TestClient(app)


def test_update():
    response = client.put("/items/foo", json={"name": "Wrestlers"})
    assert response.status_code == 200
    assert response.json() == {"name": "Wrestlers", "size": None}


def test_create():
    response = client.put("/items/red", json={"name": "Chillies"})
    assert response.status_code == 201
    assert response.json() == {"name": "Chillies", "size": None}
