import os

class Config:
    # Usamos la IP que funciona y eliminamos credenciales innecesarias
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')
    MONGO_DB = os.getenv('MONGO_DB')
    
    # Construcción de la URI sin usuario/pass (según el contexto exitoso)
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"