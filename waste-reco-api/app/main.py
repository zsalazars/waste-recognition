from fastapi import FastAPI, APIRouter
from api.routes import residuo
from api.routes import usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Residuos")

# Creamos un router con el prefijo /api/v1
api_router = APIRouter(prefix="/api/v1")

# Registramos los routers dentro de este
api_router.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
api_router.include_router(residuo.router, prefix="/residuos", tags=["Residuos"])
api_router.include_router(residuo.router, prefix="/categorias", tags=["Categorias"])
api_router.include_router(residuo.router, prefix="/reportes", tags=["Reportes"])

# Lo agregamos a la app principal
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "API de Residuos"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
