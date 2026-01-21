import mysql.connector
from mysql.connector import pooling
from config import Config

class DatabaseManager:
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            cls._pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5, # Ajustar según el tráfico esperado
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                port=Config.DB_PORT
            )
        return cls._pool

    @staticmethod
    def execute_query(query, params=None, is_select=True):
        conn = DatabaseManager.get_pool().get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if is_select:
                result = cursor.fetchall()
                return result
            else:
                conn.commit()
                return cursor.rowcount
        finally:
            cursor.close()
            conn.close()