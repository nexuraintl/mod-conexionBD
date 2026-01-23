from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config import Config

class MongoDBManager:
    _client = None

    @classmethod
    def get_db(cls):
        if cls._client is None:
            try:
                # Usamos la URI pero inyectamos los timeouts del desarrollador
                cls._client = MongoClient(
                    Config.MONGO_URI,
                    maxPoolSize=50,
                    serverSelectionTimeoutMS=3000, # 3 segundos max para encontrar el server
                    connectTimeoutMS=3000          # 3 segundos max para establecer socket
                )
                
                # Forzamos un ping para validar que la conexión es REAL
                # Si el host es incorrecto o el firewall bloquea, fallará aquí mismo
                cls._client.admin.command('ping')
                
            except ServerSelectionTimeoutError as e:
                cls._client = None  # Reset para reintentar en la próxima petición
                print(f"Fallo de RED al conectar a MongoDB: {e}")
                raise e
            except Exception as e:
                cls._client = None
                print(f"Error inesperado en MongoDBManager: {e}")
                raise e
                
        return cls._client[Config.MONGO_DB]