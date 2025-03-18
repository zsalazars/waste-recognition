from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

class Residuo(Base):
    __tablename__ = "residuos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    categoria = Column(String)