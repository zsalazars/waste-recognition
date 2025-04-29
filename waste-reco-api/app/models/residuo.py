from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Residuo(Base):
    __tablename__ = "residuos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    id_tipo_residuo = Column(Integer, ForeignKey("tipo_residuos.id"), index=True)
    
    tipo_residuo = relationship("TipoResiduo", backref="residuos")