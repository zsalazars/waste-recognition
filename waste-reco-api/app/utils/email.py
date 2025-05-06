from email.message import EmailMessage
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from datetime import datetime
from typing import List, Dict

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = 'joelzdanielz2015@gmail.com'
SMTP_PASSWORD = 'wkfp pfuf ktal sqnb'

def send_email(subject: str, body: str, recipient: str, start_date: str, end_date: str, depositos: List[Dict[str, str]] = None):
    """
    Envía un correo electrónico con contenido HTML dinámico.
    
    Args:
        subject (str): Asunto del correo
        body (str): Cuerpo del mensaje en texto plano
        recipient (str): Destinatario del correo
        depositos (List[Dict]): Lista de depósitos con formato [{"categoria": "nombre", "cantidad": número}]
    
    Returns:
        bool: True si el envío fue exitoso, False en caso contrario
    """
    # Si no se proporcionan depósitos, usar valores predeterminados
    if depositos is None:
        depositos = [
            {"categoria": "Depósitos Aprovechables", "cantidad": 45},
            {"categoria": "Depósitos No Aprovechables", "cantidad": 38},
            {"categoria": "Depósitos Orgánicos", "cantidad": 27},
            {"categoria": "Depósitos Peligrosos", "cantidad": 15}
        ]
    
    # Calcular el total y los porcentajes
    total_depositos = sum(item["cantidad"] for item in depositos)
    
    # Generar las filas de la tabla
    filas_tabla = ""
    for item in depositos:
        porcentaje = round((item["cantidad"] / total_depositos) * 100, 1)
        filas_tabla += f"""
        <tr>
            <td>{item["categoria"]}</td>
            <td>{item["cantidad"]} veces</td>
            <td>{porcentaje}%</td>
        </tr>
        """
    
    html_template = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background-color: #2E7D32;
                color: white;
                padding: 15px;
                text-align: center;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-top: none;
                border-radius: 0 0 8px 8px;
            }}
            .title {{
                font-size: 24px;
                font-weight: bold;
                margin: 0;
            }}
            .results {{
                margin-top: 20px;
                margin-bottom: 20px;
                background-color: white;
                padding: 15px;
                border-radius: 5px;
                border: 1px solid #eee;
            }}
            .highlight {{
                color: #2E7D32;
                font-weight: bold;
            }}
            .date-highlight {{
                background-color: #E8F5E9;
                padding: 5px 10px;
                border-radius: 4px;
                font-weight: bold;
                display: inline-block;
                margin: 5px 0;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #777;
                text-align: center;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #E8F5E9;
                color: #2E7D32;
            }}
            .category-table {{
                margin-top: 25px;
            }}
            .residue-count {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 10px;
                margin-bottom: 25px;
            }}
            .residue-box {{
                background-color: #E8F5E9;
                border-radius: 5px;
                padding: 8px 12px;
                font-weight: bold;
                color: #2E7D32;
                min-width: 40px;
                text-align: center;
            }}
            .section-title {{
                border-bottom: 2px solid #2E7D32;
                padding-bottom: 5px;
                color: #2E7D32;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 class="title">Informe de Depósitos y Residuos</h1>
        </div>
        <div class="content">
            <p>Estimado usuario,</p>
            <p>{body}</p>
            
            <div class="results">
                <h2 class="section-title">Resumen de Depósitos</h2>
                <p>Fecha de inicio de depósitos: <span class="date-highlight">{start_date}</span></p>
                <p>Ultimo depósito: <span class="date-highlight">{end_date}</span></p>
                <p>Se han realizado un total de <span class="highlight">{total_depositos} depósitos</span> clasificados por categoría:</p>
                
                <table class="category-table">
                    <tr>
                        <th>Categoría</th>
                        <th>Cantidad</th>
                        <th>Porcentaje</th>
                    </tr>
                    {filas_tabla}
                    <tr>
                        <th>Total</th>
                        <th>{total_depositos}</th>
                        <th>100%</th>
                    </tr>
                </table>
            </div>
            
            <p>Gracias por confiar en nuestro servicio para la gestión de sus depósitos.</p>
            <p>Saludos cordiales,</p>
            <p>Equipo de Investigación - Universidad Andina del Cusco</p>
        </div>
        <div class="footer">
            <p>Este es un mensaje automático generado el {datetime.now().strftime('%d/%m/%Y')}. Por favor no responda a este correo.</p>
        </div>
    </body>
    </html>
    """

    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = recipient
        msg["Subject"] = subject
        
        # Cuerpo en formato texto plano (por si no se puede leer HTML)
        msg.attach(MIMEText(body, "plain"))
        
        # Cuerpo en formato HTML
        msg.attach(MIMEText(html_template, "html"))

        # Conexión SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            smtp.sendmail(SMTP_USER, recipient, msg.as_string())

        return True
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return False