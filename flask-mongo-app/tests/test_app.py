import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_add_user(client):
    response = client.post('/add_user', json={"name": "John", "email": "john@example.com"})
    assert response.status_code == 201

def test_get_users(client):
    response = client.get('/get_users')
    assert response.status_code == 200
