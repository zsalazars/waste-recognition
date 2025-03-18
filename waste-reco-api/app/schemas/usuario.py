from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True