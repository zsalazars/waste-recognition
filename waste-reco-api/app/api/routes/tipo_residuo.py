from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.tipo_residuo as crud
import schemas.tipo_residuo as tipo_residuo
import crud.residuo as crud_residuo
import crud.tipo_residuo as crud_tipo_residuo
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=tipo_residuo.TipoResiduo)
def create_tipo_residuo_endpoint(tipo_residuo: tipo_residuo.TipoResiduoCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_residuo(db=db, tipo_residuo=tipo_residuo)
  
@router.get("/", response_model=List[tipo_residuo.TipoResiduo])
def read_tipo_residuos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tipo_residuos = crud.get_tipo_residuos(db=db, skip=skip, limit=limit)
    return tipo_residuos

@router.get("/residuos", response_model=List[tipo_residuo.TipoConResiduos])
def read_tipo_con_residuos(db: Session = Depends(get_db)):
    return crud_tipo_residuo.get_tipo_con_residuos(db)
  
@router.get("/{tipo_residuo_id}", response_model=tipo_residuo.TipoResiduo)
def read_tipo_residuo_endpoint(tipo_residuo_id: int, db: Session = Depends(get_db)):
    db_tipo_residuo = crud.get_tipo_residuo(db=db, tipo_residuo_id=tipo_residuo_id)
    if db_tipo_residuo is None:
        raise HTTPException(status_code=404, detail="tipo_residuo no encontrada")
    return db_tipo_residuo

@router.put("/{tipo_residuo_id}", response_model=tipo_residuo.TipoResiduo)
def update_tipo_residuo_endpoint(tipo_residuo_id: int, tipo_residuo: tipo_residuo.TipoResiduoCreate, db: Session = Depends(get_db)):
    db_tipo_residuo = crud.update_tipo_residuo(db=db, tipo_residuo_id=tipo_residuo_id, tipo_residuo=tipo_residuo)
    if db_tipo_residuo is None:
        raise HTTPException(status_code=404, detail="tipo_residuo no encontrada")
    return db_tipo_residuo
  
@router.delete("/{tipo_residuo_id}", response_model=bool)
def delete_tipo_residuo_endpoint(tipo_residuo_id: int, db: Session = Depends(get_db)):
    result = crud.delete_tipo_residuo(db=db, tipo_residuo_id=tipo_residuo_id)
    if not result:
        raise HTTPException(status_code=404, detail="tipo_residuo no encontrada")
    return True