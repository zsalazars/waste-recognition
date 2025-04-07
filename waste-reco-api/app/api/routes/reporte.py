from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.reporte as crud
import schemas.reporte as reporte
from core.database import get_db

router = APIRouter()

@router.post("/generar-reporte", response_model=reporte.Reporte)
def create_reporte_endpoint(reporte: reporte.ReporteCreate, db: Session = Depends(get_db)):
    return crud.create_reporte(db=db, reporte=reporte)

@router.get("/", response_model=List[reporte.Reporte])
def read_reportes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reportes = crud.get_reportes(db, skip=skip, limit=limit)
    return reportes

@router.get("/{reporte_id}", response_model=reporte.Reporte)
def read_reporte_endpoint(reporte_id: int, db: Session = Depends(get_db)):
    db_reporte = crud.get_reporte(db, reporte_id=reporte_id)
    if db_reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return db_reporte