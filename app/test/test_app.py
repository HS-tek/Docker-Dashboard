import pytest
from main import app, db, Container

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_containers(client):
    # Teste la route GET pour vérifier que la liste est vide au départ
    rv = client.get('/containers')
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_container(client):
    # Teste la route POST pour créer un nouveau container
    rv = client.post('/containers', json={"name": "test_container", "status": "running"})
    assert rv.status_code == 201
    json_data = rv.get_json()
    assert json_data['message'] == "Container created"

    # Vérifie que le nouveau container est bien créé
    rv = client.get('/containers')
    containers = rv.get_json()
    assert len(containers) == 1
    assert containers[0]['name'] == "test_container"
    assert containers[0]['status'] == "running"
