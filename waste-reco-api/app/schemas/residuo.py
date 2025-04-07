from pydantic import BaseModel

class ResiduoBase(BaseModel):
    nombre: str
    categoria: str

class ResiduoCreate(ResiduoBase):
    pass

class Residuo(ResiduoBase):
    id: int

    class Config:
        orm_mode = True