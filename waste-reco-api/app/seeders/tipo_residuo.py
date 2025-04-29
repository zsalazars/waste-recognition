from sqlalchemy.orm import Session
from models.tipo_residuo import TipoResiduo

def seed_tipo_residuos(db: Session):
    tipos = ["Aprovechables", "No Aprovechables", "Orgánicos", "Peligrosos"]

    for nombre in tipos:
        existe = db.query(TipoResiduo).filter_by(nombre=nombre).first()
        if not existe:
            nuevo_tipo = TipoResiduo(nombre=nombre)
            db.add(nuevo_tipo)
    
    db.commit()
    print("✅ Tipos de residuo sembrados correctamente.")
