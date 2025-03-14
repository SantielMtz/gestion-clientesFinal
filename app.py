from flask import Flask
from app.routes import cliente_bp

app = Flask(__name__)

# Registrar rutas de clientes
app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    app.run(debug=True)
