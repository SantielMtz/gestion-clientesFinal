from flask import Blueprint, request, jsonify

cliente_bp = Blueprint('clientes', __name__)

# Base de datos que estoy haciendo como simulación (por ahora, una lista en memoria)
clientes = []

# Crear un cliente
@cliente_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    nuevo_cliente = {
        "id": len(clientes) + 1,
        "nombre": data.get("nombre"),
        "email": data.get("email")
    }
    clientes.append(nuevo_cliente)
    return jsonify(nuevo_cliente), 201

# Obtener todos los clientes
@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(clientes)

# Modificar un cliente
@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def modificar_cliente(id):
    for cliente in clientes:
        if cliente["id"] == id:
            data = request.json
            cliente["nombre"] = data.get("nombre", cliente["nombre"])
            cliente["email"] = data.get("email", cliente["email"])
            return jsonify(cliente)
    return jsonify({"error": "Cliente no encontrado"}), 404
