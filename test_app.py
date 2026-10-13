import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym API!" in rv.data

def test_get_programs(client):
    rv = client.get('/programs')
    assert rv.status_code == 200
    assert b"Fat Loss" in rv.data

def test_get_invalid_program(client):
    rv = client.get('/programs/InvalidProgram')
    assert rv.status_code == 404

def test_register_user_success(client):
    rv = client.post('/users', json={"username": "testuser", "program": "Fat Loss"})
    assert rv.status_code == 201
    assert b"registered successfully" in rv.data