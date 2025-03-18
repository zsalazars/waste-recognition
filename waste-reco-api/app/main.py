from fastapi import FastAPI
from api.routes import residuo
from api.routes import usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Residuos")

app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(residuo.router, prefix="/residuos", tags=["Residuos"])

@app.get("/")
def read_root():
    return {"message": "API de Residuos"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes, puedes cambiarlo a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)
