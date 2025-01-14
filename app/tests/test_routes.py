import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_classify_route(client):
    response = client.post('/classify', json={"text": "This is a test"})
    assert response.status_code == 200
    assert "classification" in response.json

def test_ner_route(client):
    response = client.post('/ner', json={"text": "Barack Obama is in Washington"})
    assert response.status_code == 200
    assert "entities" in response.json

def test_qa_route(client):
    response = client.post('/qa', json={
        "question": "What is the capital of France?",
        "context": "France is a country in Europe. Its capital is Paris."
    })
    assert response.status_code == 200
    assert "answer" in response.json