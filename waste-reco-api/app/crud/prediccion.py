from sqlalchemy.orm import Session
from models.prediccion import Prediccion
import schemas.prediccion as schemas
  
def get_predicciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Prediccion).offset(skip).limit(limit).all()

def get_prediccion(db: Session, prediccion_id: int):
    return db.query(Prediccion).filter(Prediccion.id == prediccion_id).first()

def get_predicciones_por_usuario(db: Session, id_usuario: int):
    return db.query(Prediccion).filter(Prediccion.id_usuario == id_usuario).all()

def create_prediccion(db: Session, prediccion: schemas.PrediccionCreate):
    db_prediccion = Prediccion(**prediccion.dict())
    db.add(db_prediccion)
    db.commit()
    db.refresh(db_prediccion)
    return db_prediccion

def update_prediccion(db: Session, prediccion_id: int, prediccion: schemas.PrediccionCreate):
    db_prediccion = get_prediccion(db, prediccion_id)
    if db_prediccion:
        for key, value in prediccion.dict().items():
            setattr(db_prediccion, key, value)
        db.commit()
        db.refresh(db_prediccion)
    return db_prediccion

def delete_prediccion(db: Session, prediccion_id: int):
    db_prediccion = get_prediccion(db, prediccion_id)
    if db_prediccion:
        db.delete(db_prediccion)
        db.commit()
        return True
    return False