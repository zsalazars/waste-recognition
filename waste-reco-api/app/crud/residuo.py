from sqlalchemy.orm import Session
from models.residuo import Residuo
import schemas.residuo as schemas

def get_residuo(db: Session, residuo_id: int):
    return db.query(Residuo).filter(Residuo.id == residuo_id).first()

def get_residuos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Residuo).offset(skip).limit(limit).all()

def create_residuo(db: Session, residuo: schemas.ResiduoCreate):
    db_residuo = Residuo(nombre=residuo.nombre, id_tipo_residuo=residuo.id_tipo_residuo)
    db.add(db_residuo)
    db.commit()
    db.refresh(db_residuo)
    return db_residuo

def update_residuo(db: Session, residuo_id: int, residuo: schemas.ResiduoCreate):
    db_residuo = get_residuo(db, residuo_id)
    if db_residuo:
        db_residuo.nombre = residuo.nombre
        db_residuo.id_tipo_residuo = residuo.id_tipo_residuo
        db.commit()
        db.refresh(db_residuo)
    return db_residuo

def delete_residuo(db: Session, residuo_id: int):
    db_residuo = get_residuo(db, residuo_id)
    if db_residuo:
        db.delete(db_residuo)
        db.commit()
        return True
    return False
