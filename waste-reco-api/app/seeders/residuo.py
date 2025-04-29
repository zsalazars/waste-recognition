from sqlalchemy.orm import Session
from models.residuo import Residuo
from models.tipo_residuo import TipoResiduo

def seed_residuos(db: Session):
    # Datos de los residuos
    residuos = [
        {"nombre": "Papel y cartón", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Vidrio", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Plástico", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Textiles", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Madera", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Cuero", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Empaques compuestos", "id_tipo_residuo": "Aprovechables"},
        {"nombre": "Metales", "id_tipo_residuo": "Aprovechables"},
        
        {"nombre": "Papel encerado", "id_tipo_residuo": "No Aprovechables"},
        {"nombre": "Cerámicos", "id_tipo_residuo": "No Aprovechables"},
        {"nombre": "Colillas de cigarro", "id_tipo_residuo": "No Aprovechables"},
        {"nombre": "Residuos sanitarios", "id_tipo_residuo": "No Aprovechables"},
        
        {"nombre": "Restos de alimentos", "id_tipo_residuo": "Orgánicos"},
        {"nombre": "Restos de poda", "id_tipo_residuo": "Orgánicos"},
        {"nombre": "Hojarasca", "id_tipo_residuo": "Orgánicos"},
        
        {"nombre": "Pilas", "id_tipo_residuo": "Peligrosos"},
        {"nombre": "Luminaria", "id_tipo_residuo": "Peligrosos"},
        {"nombre": "Medicinas vencidas", "id_tipo_residuo": "Peligrosos"},
        {"nombre": "Plaguicidas", "id_tipo_residuo": "Peligrosos"},
    ]
    
    for residuo in residuos:
        # Verificar si el tipo de residuo existe
        tipo_residuo = db.query(TipoResiduo).filter_by(nombre=residuo["id_tipo_residuo"]).first()
        if tipo_residuo:
            # Verificar si el residuo ya existe
            existe = db.query(Residuo).filter_by(nombre=residuo["nombre"]).first()
            if not existe:
                nuevo_residuo = Residuo(
                    nombre=residuo["nombre"],
                    id_tipo_residuo=tipo_residuo.id  # Usar el ID del TipoResiduo
                )
                db.add(nuevo_residuo)
    
    db.commit()
    print("✅ Residuos sembrados correctamente.")
