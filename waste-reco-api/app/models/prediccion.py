from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from models.base import Base

class Prediccion(Base):
    __tablename__ = "predicciones"

    id = Column(Integer, primary_key=True, index=True)
    precision_usuario = Column(Numeric(5, 4), index=True)
    tasa_acierto = Column(Numeric(5, 4), index=True)
    fecha_prediccion = Column(DateTime, index=True)
    id_residuo = Column(Integer, ForeignKey("residuos.id"), index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), index=True)
    
    usuario = relationship("Usuario", backref="predicciones")
    residuo = relationship("Residuo", backref="predicciones")