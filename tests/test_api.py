from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)




def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}




def test_add_endpoint():
    r = client.get("/calc/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5




def test_subtract_endpoint():
    r = client.get("/calc/subtract", params={"a": 5, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 3




def test_multiply_endpoint():
    r = client.get("/calc/multiply", params={"a": 4, "b": 2.5})
    assert r.status_code == 200
    assert r.json()["result"] == 10.0




def test_divide_endpoint():
    r = client.get("/calc/divide", params={"a": 9, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 3




def test_divide_by_zero_endpoint():
    r = client.get("/calc/divide", params={"a": 1, "b": 0})
    assert r.status_code == 400
    assert "division by zero" in r.json().get("detail", "")