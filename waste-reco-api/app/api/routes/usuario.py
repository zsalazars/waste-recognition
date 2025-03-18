from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.usuario as crud
import schemas.usuario as usuario
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=usuario.Usuario)
def create_usuario_endpoint(usuario: usuario.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db=db, usuario=usuario)

@router.get("/", response_model=List[usuario.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.get("/{usuario_id}", response_model=usuario.Usuario)
def read_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.put("/{usuario_id}", response_model=usuario.Usuario)
def update_usuario_endpoint(usuario_id: int, usuario: usuario.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, usuario_id=usuario_id, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.delete("/{usuario_id}", response_model=bool)
def delete_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    result = crud.delete_usuario(db, usuario_id=usuario_id)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return True
