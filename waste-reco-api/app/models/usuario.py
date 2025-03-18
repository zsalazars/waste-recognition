from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String)