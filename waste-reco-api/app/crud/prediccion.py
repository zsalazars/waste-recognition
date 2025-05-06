from sqlalchemy.orm import Session
from models.prediccion import Prediccion
from typing import List
from datetime import date
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

def get_predicciones_por_fecha(
    db: Session,
    fecha: date
) -> List[Prediccion]:
    return db.query(Prediccion).filter(Prediccion.fecha_prediccion == fecha).all()

def get_predicciones_por_rango_fecha(db: Session, fecha_inicio: date, fecha_fin: date):
    return db.query(Prediccion).filter(
        Prediccion.fecha_prediccion >= fecha_inicio,
        Prediccion.fecha_prediccion <= fecha_fin
    ).all()
    
def get_predicciones_usuario_por_rango_fecha(db: Session, id_usuario: int, start_date: date, end_date: date):
    return (
        db.query(Prediccion)
        .filter(Prediccion.id_usuario == id_usuario)
        .filter(Prediccion.fecha_prediccion >= start_date)
        .filter(Prediccion.fecha_prediccion <= end_date)
        .all()
    )
