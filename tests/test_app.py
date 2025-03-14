import pytest
from app import app

@pytest.fixture
def cliente():
    return app.test_client()

def test_obtener_clientes(cliente):
    respuesta = cliente.get('/clientes')
    assert respuesta.status_code == 200
    assert respuesta.json == []

def test_crear_cliente(cliente):
    datos = {"nombre": "Juan Pérez", "email": "juan@example.com"}
    respuesta = cliente.post('/clientes', json=datos)
    assert respuesta.status_code == 201
    assert respuesta.json["nombre"] == "Juan Pérez"
