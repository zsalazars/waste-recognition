from decimal import Decimal
from pydantic import BaseModel
from schemas.usuario import Usuario
from schemas.residuo import Residuo

class Prediccion(BaseModel):
    id: int
    precision_usuario: Decimal
    tasa_acierto: Decimal
    fecha_prediccion: str

    usuario: Usuario
    residuo: Residuo
    
class PrediccionCreate(BaseModel):
    precision_usuario: Decimal
    tasa_acierto: Decimal
    fecha_prediccion: str
    id_residuo: int
    id_usuario: int

class Config:
    orm_mode = True