from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base  # Importar Base desde el archivo base
from models.residuo import Residuo  # Importar Residuo
from models.usuario import Usuario  # Importar Usuario
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener DATABASE_URL desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Creamos el motor de SQL Alchemy con opciones adicionales para depuración
engine = create_engine(
    DATABASE_URL, 
    echo=True,  # Para ver las consultas SQL generadas
    pool_pre_ping=True  # Verificar la conexión antes de usarla
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base.metadata.create_all(bind=engine)