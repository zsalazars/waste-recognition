from sqlalchemy import Column, Integer, String
from models.base import Base

class TipoResiduo(Base):
    __tablename__ = "tipo_residuos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
