from fastapi import FastAPI, APIRouter
from api.routes import residuo
from api.routes import usuario
from api.routes import prediccion
from api.routes import tipo_residuo
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from core.database import engine, SessionLocal
from seeders.residuo import seed_residuos
from seeders.tipo_residuo import seed_tipo_residuos

app = FastAPI(title="API de Residuos")

# Creamos un router con el prefijo /api/v1
api_router = APIRouter(prefix="/api/v1")

# Registramos los routers dentro de este
api_router.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
api_router.include_router(residuo.router, prefix="/residuos", tags=["Residuos"])
api_router.include_router(tipo_residuo.router, prefix="/tipo-residuo", tags=["Tipo Residuo"])
api_router.include_router(prediccion.router, prefix="/prediccion", tags=["Prediccion"])

# Lo agregamos a la app principal
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "API de Residuos"}

# Añadir CORS para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear la base de datos y ejecutar los seeders
@app.on_event("startup")
def on_startup():
    # Crear las tablas en la base de datos
    from models.base import Base
    Base.metadata.create_all(bind=engine)

    # Insertar los datos por defecto
    db: Session = SessionLocal()
    try:
        seed_tipo_residuos(db)
        seed_residuos(db)
    finally:
        db.close()
