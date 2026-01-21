import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Estos valores se inyectarán desde Secret Manager y variables de entorno en Cloud Run
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASS = os.getenv('MONGO_PASS')
    MONGO_HOST = os.getenv('MONGO_HOST') # IP Privada de la VM
    MONGO_PORT = os.getenv('MONGO_PORT', '27017')
    MONGO_DB   = os.getenv('MONGO_DB', 'admin')
    
    # Construcción de la URI de conexión
    MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"