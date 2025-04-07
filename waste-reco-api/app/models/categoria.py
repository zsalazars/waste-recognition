from sqlalchemy import Column, Integer, String
from models.base import Base

class Categoria(Base):
    __tablename__ = "residuos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
