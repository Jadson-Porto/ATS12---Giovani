from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API rodando com sucesso"}

def test_somar():
    response = client.get("/somar/5/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 8}