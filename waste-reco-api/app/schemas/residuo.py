from pydantic import BaseModel
from typing import List

class ResiduoBase(BaseModel):
    nombre: str
    categoria: int

class ResiduoCreate(ResiduoBase):
    pass

class Residuo(ResiduoBase):
    id: int

    class Config:
        orm_mode = True

class ResiduoOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class CategoriaConResiduos(BaseModel):
    id: int
    nombre: str
    residuos: List[ResiduoOut]

    class Config:
        orm_mode = True
