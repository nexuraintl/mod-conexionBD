from flask import Blueprint, request, jsonify
from src.database.db_manager import MongoDBManager
from bson.objectid import ObjectId
from bson import json_util
import json

ops_bp = Blueprint('operations', __name__)

def parse_json(data):
    """Auxiliar para serializar objetos de MongoDB (como ObjectId) a JSON estándar."""
    return json.loads(json_util.dumps(data))

# 1. CONSULTA POR ID (Prioridad del usuario)
@ops_bp.route('/erp/<id>', methods=['GET'])
def get_item_by_id(id):
    try:
        db = MongoDBManager.get_db()
        # Buscamos en la colección específica tn_integrador_erp
        item = db.tn_integrador_erp.find_one({"_id": ObjectId(id)})
        
        if item:
            return jsonify(parse_json(item)), 200
        return jsonify({"error": "Documento no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"ID inválido o error de consulta: {str(e)}"}), 400

# 2. CONSULTA GENERAL (Opcional, con límite)
@ops_bp.route('/erp', methods=['GET'])
def get_all_items():
    db = MongoDBManager.get_db()
    items = list(db.tn_integrador_erp.find().limit(50))
    return jsonify(parse_json(items)), 200

# 3. INSERTAR (Create)
@ops_bp.route('/erp', methods=['POST'])
def insert_item():
    try:
        db = MongoDBManager.get_db()
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Cuerpo de solicitud vacío"}), 400
            
        result = db.tn_integrador_erp.insert_one(data)
        return jsonify({
            "message": "Registro creado en tn_integrador_erp",
            "inserted_id": str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. ELIMINAR (Delete)
@ops_bp.route('/erp/<id>', methods=['DELETE'])
def delete_item(id):
    try:
        db = MongoDBManager.get_db()
        result = db.tn_integrador_erp.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count > 0:
            return jsonify({"message": f"Registro {id} eliminado correctamente"}), 200
        return jsonify({"error": "No se encontró el registro para eliminar"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400