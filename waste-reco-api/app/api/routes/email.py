from fastapi import APIRouter, HTTPException, Response
from schemas.email import EmailSchema
from utils.email import send_email
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

@router.post("/send")
def enviar_correo(email: EmailSchema, response: Response):
    # Agregar headers CORS explícitamente a esta respuesta
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    
    try:
        depositos_dict = None
        if email.depositos:
            depositos_dict = [{"categoria": item.categoria, "cantidad": item.cantidad} for item in email.depositos]
        
        success = send_email(email.subject, email.body, email.to, email.start_date, email.end_date, depositos_dict)
        
        if success:
            return {"mensaje": "Correo enviado correctamente"}
        else:
            raise HTTPException(status_code=500, detail="Error al enviar el correo")
    except Exception as e:
        # Asegurarse de que incluso en caso de error, se establezcan los headers CORS
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")

# Agregar manejador OPTIONS para preflight requests
@router.options("/send")
def options_email(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return {}