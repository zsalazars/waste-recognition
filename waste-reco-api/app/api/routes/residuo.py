from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.residuo as crud
import schemas.residuo as residuo
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=residuo.Residuo)
def create_residuo_endpoint(residuo: residuo.ResiduoCreate, db: Session = Depends(get_db)):
    return crud.create_residuo(db=db, residuo=residuo)

@router.get("/", response_model=List[residuo.Residuo])
def read_residuos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    residuos = crud.get_residuos(db, skip=skip, limit=limit)
    return residuos

@router.get("/{residuo_id}", response_model=residuo.Residuo)
def read_residuo_endpoint(residuo_id: int, db: Session = Depends(get_db)):
    db_residuo = crud.get_residuo(db, residuo_id=residuo_id)
    if db_residuo is None:
        raise HTTPException(status_code=404, detail="Residuo no encontrado")
    return db_residuo

@router.put("/{residuo_id}", response_model=residuo.Residuo)
def update_residuo_endpoint(residuo_id: int, residuo: residuo.ResiduoCreate, db: Session = Depends(get_db)):
    db_residuo = crud.update_residuo(db, residuo_id=residuo_id, residuo=residuo)
    if db_residuo is None:
        raise HTTPException(status_code=404, detail="Residuo no encontrado")
    return db_residuo

@router.delete("/{residuo_id}", response_model=bool)
def delete_residuo_endpoint(residuo_id: int, db: Session = Depends(get_db)):
    result = crud.delete_residuo(db, residuo_id=residuo_id)
    if not result:
        raise HTTPException(status_code=404, detail="Residuo no encontrado")
    return True
