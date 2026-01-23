from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config import Config

class MongoDBManager:
    _client = None

    @classmethod
    def get_db(cls):
        if cls._client is None:
            try:
                # Configuramos el cliente igual al microservicio exitoso
                cls._client = MongoClient(
                    Config.MONGO_URI,
                    serverSelectionTimeoutMS=5000,
                    connectTimeoutMS=5000
                )
                # Validamos conexión
                cls._client.admin.command('ping')
            except Exception as e:
                cls._client = None
                print(f"Error de conexión a MongoDB: {e}")
                raise e
        
        # Accedemos a la base de datos qa-sgd
        return cls._client[Config.MONGO_DB]