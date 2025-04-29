from pydantic import BaseModel
from typing import List

class TipoResiduoBase(BaseModel):
    nombre: str

class TipoResiduoCreate(TipoResiduoBase):
    pass

class TipoResiduo(TipoResiduoBase):
    id: int

    class Config:
        orm_mode = True
        
class ResiduoOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class TipoConResiduos(BaseModel):
    id: int
    nombre: str
    residuos: List[ResiduoOut]

    class Config:
        orm_mode = True