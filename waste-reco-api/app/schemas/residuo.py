from schemas.tipo_residuo import TipoResiduo
from pydantic import BaseModel

class ResiduoBase(BaseModel):
    nombre: str

class ResiduoCreate(ResiduoBase):
    id_tipo_residuo: int

class Residuo(ResiduoBase):
    id: int
    tipo_residuo: TipoResiduo

    class Config:
        orm_mode = True
