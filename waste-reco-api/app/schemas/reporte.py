from decimal import Decimal
from pydantic import BaseModel
from typing import Optional

class ReporteBase(BaseModel):
    precision_usuario: Decimal
    tasa_acierto: Decimal
    fecha_reporte: str
    id_residuo: int
    id_usuario: int

class ReporteCreate(ReporteBase):
    pass

class Reporte(ReporteBase):
    id: int

    class Config:
        orm_mode = True
