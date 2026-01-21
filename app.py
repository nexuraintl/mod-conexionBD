from flask import Flask, jsonify
from src.routes.operations import ops_bp

app = Flask(__name__)

# Ruta raíz para probar si el servicio responde algo
@app.route('/')
def index():
    return jsonify({"message": "Servidor activo"}), 200

@app.route('/health')
def health():
    return jsonify({"status": "up", "service": "external-db-connector"}), 200

app.register_blueprint(ops_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)