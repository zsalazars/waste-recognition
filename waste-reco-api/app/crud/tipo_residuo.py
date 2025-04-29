from sqlalchemy.orm import Session, joinedload
from models.tipo_residuo import TipoResiduo
import schemas.tipo_residuo as tipo_residuo

def get_tipo_residuo(db: Session, tipo_residuo_id: int):
    return db.query(TipoResiduo).filter(TipoResiduo.id == tipo_residuo_id).first()

def get_tipo_residuos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TipoResiduo).offset(skip).limit(limit).all()

def get_tipo_con_residuos(db: Session):
    return db.query(TipoResiduo).options(joinedload(TipoResiduo.residuos)).all()
  
def create_tipo_residuo(db: Session, tipo_residuo: tipo_residuo.TipoResiduoCreate):
    db_tipo_residuo = TipoResiduo(nombre=tipo_residuo.nombre)
    db.add(db_tipo_residuo)
    db.commit()
    db.refresh(db_tipo_residuo)
    return db_tipo_residuo

def update_tipo_residuo(db: Session, tipo_residuo_id: int, tipo_residuo: tipo_residuo.TipoResiduoCreate):
    db_tipo_residuo = get_tipo_residuo(db, tipo_residuo_id)
    if db_tipo_residuo:
        db_tipo_residuo.nombre = tipo_residuo.nombre
        db.commit()
        db.refresh(db_tipo_residuo)
    return db_tipo_residuo

def delete_tipo_residuo(db: Session, tipo_residuo_id: int):
    db_tipo_residuo = get_tipo_residuo(db, tipo_residuo_id)
    if db_tipo_residuo:
        db.delete(db_tipo_residuo)
        db.commit()
        return True
    return False