from flask import Blueprint, request, jsonify
from src.database.db_manager import DatabaseManager

ops_bp = Blueprint('operations', __name__)

@ops_bp.route('/items', methods=['GET'])
def get_items():
    query = "SELECT * FROM `tn_sx_cliente_comu` LIMIT 100"
    data = DatabaseManager.execute_query(query)
    return jsonify(data), 200

@ops_bp.route('/items', methods=['POST'])
def insert_item():
    data = request.get_json()
    # Ejemplo: Ajustar según tus columnas reales
    query = "INSERT INTO `tn_sx_cliente_comu` (columna1, columna2) VALUES (%s, %s)"
    params = (data.get('val1'), data.get('val2'))
    rows = DatabaseManager.execute_query(query, params, is_select=False)
    return jsonify({"message": "Insertado", "rows_affected": rows}), 201

@ops_bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    query = "DELETE FROM `tn_sx_cliente_comu` WHERE id = %s"
    rows = DatabaseManager.execute_query(query, (id,), is_select=False)
    return jsonify({"message": "Eliminado", "rows_affected": rows}), 200
    