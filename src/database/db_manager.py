from pymongo import MongoClient
from config import Config

class MongoDBManager:
    _client = None

    @classmethod
    def get_db(cls):
        if cls._client is None:
            # El cliente se inicializa una sola vez y se reutiliza
            cls._client = MongoClient(Config.MONGO_URI, maxPoolSize=50)
        return cls._client[Config.MONGO_DB]