from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from models.base import Base

class Reporte(Base):
    __tablename__ = "residuos"

    id = Column(Integer, primary_key=True, index=True)
    precision_usuario = Column(Numeric(5, 4), index=True)
    tasa_acierto = Column(Numeric(5, 4), index=True)
    fecha_reporte = Column(String, index=True)
    id_residuo = Column(Integer, ForeignKey("residuos.id"), index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), index=True)