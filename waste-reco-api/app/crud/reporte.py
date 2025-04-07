from sqlalchemy.orm import Session
from models.reporte import Reporte
import schemas.reporte as schemas

def get_reporte(db: Session, reporte_id: int):
    return db.query(Reporte).filter(Reporte.id == reporte_id).first()
  
def get_reportes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reporte).offset(skip).limit(limit).all()
  
def create_reporte(db: Session, reporte: schemas.ReporteCreate):
    db_reporte = Reporte(**reporte.dict())
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte

def update_reporte(db: Session, reporte_id: int, reporte: schemas.ReporteCreate):
    db_reporte = get_reporte(db, reporte_id)
    if db_reporte:
        for key, value in reporte.dict().items():
            setattr(db_reporte, key, value)
        db.commit()
        db.refresh(db_reporte)
    return db_reporte

def delete_reporte(db: Session, reporte_id: int):
    db_reporte = get_reporte(db, reporte_id)
    if db_reporte:
        db.delete(db_reporte)
        db.commit()
        return True
    return False