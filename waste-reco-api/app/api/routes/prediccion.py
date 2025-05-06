from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
import crud.prediccion as crud
import schemas.prediccion as prediccion
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=prediccion.Prediccion)
def create_prediccion_endpoint(prediccion: prediccion.PrediccionCreate, db: Session = Depends(get_db)):
    return crud.create_prediccion(db=db, prediccion=prediccion)

@router.get("/", response_model=List[prediccion.Prediccion])
def read_predicciones(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    if start_date and end_date:
        return crud.get_predicciones_por_rango_fecha(db, start_date, end_date)
    return crud.get_predicciones(db)


@router.get("/{prediccion_id}", response_model=prediccion.Prediccion)
def read_prediccion_endpoint(prediccion_id: int, db: Session = Depends(get_db)):
    db_prediccion = crud.get_prediccion(db, prediccion_id=prediccion_id)
    if db_prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrado")
    return db_prediccion

from datetime import date
from typing import Optional

@router.get("/usuario/{id_usuario}", response_model=List[prediccion.Prediccion])
def read_predicciones_por_usuario(
    id_usuario: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    if start_date and end_date:
        predicciones = crud.get_predicciones_usuario_por_rango_fecha(db, id_usuario, start_date, end_date)
    else:
        predicciones = crud.get_predicciones_por_usuario(db, id_usuario=id_usuario)

    if not predicciones:
        raise HTTPException(status_code=404, detail="No se encontraron predicciones para este usuario")

    return predicciones