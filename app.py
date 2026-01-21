from flask import Flask, jsonify
from src.routes.operations import ops_bp

app = Flask(__name__)

# Registro de Blueprints
app.register_blueprint(ops_bp, url_prefix='/api/v1')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up", "service": "external-db-connector"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)