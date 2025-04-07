from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.categoria as crud
import schemas.categoria as categoria
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=categoria.Categoria)
def create_categoria_endpoint(categoria: categoria.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db=db, categoria=categoria)
  
@router.get("/", response_model=List[categoria.Categoria])
def read_categorias_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db=db, skip=skip, limit=limit)
    return categorias
  
@router.get("/{categoria_id}", response_model=categoria.Categoria)
def read_categoria_endpoint(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = crud.get_categoria(db=db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return db_categoria

@router.put("/{categoria_id}", response_model=categoria.Categoria)
def update_categoria_endpoint(categoria_id: int, categoria: categoria.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = crud.update_categoria(db=db, categoria_id=categoria_id, categoria=categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return db_categoria
  
@router.delete("/{categoria_id}", response_model=bool)
def delete_categoria_endpoint(categoria_id: int, db: Session = Depends(get_db)):
    result = crud.delete_categoria(db=db, categoria_id=categoria_id)
    if not result:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return True