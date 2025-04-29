from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.prediccion as crud
import schemas.prediccion as prediccion
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=prediccion.Prediccion)
def create_prediccion_endpoint(prediccion: prediccion.PrediccionCreate, db: Session = Depends(get_db)):
    return crud.create_prediccion(db=db, prediccion=prediccion)

@router.get("/", response_model=List[prediccion.Prediccion])
def read_prediccion(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prediccion = crud.get_prediccion(db, skip=skip, limit=limit)
    return prediccion

@router.get("/{prediccion_id}", response_model=prediccion.Prediccion)
def read_prediccion_endpoint(prediccion_id: int, db: Session = Depends(get_db)):
    db_prediccion = crud.get_prediccion(db, prediccion_id=prediccion_id)
    if db_prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrado")
    return db_prediccion