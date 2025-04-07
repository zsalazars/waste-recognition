from sqlalchemy.orm import Session
from models.categoria import Categoria
import schemas.categoria as schemas

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Categoria).offset(skip).limit(limit).all()
  
def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria: schemas.CategoriaCreate):
    db_categoria = get_categoria(db, categoria_id)
    if db_categoria:
        db_categoria.nombre = categoria.nombre
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = get_categoria(db, categoria_id)
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
        return True
    return False