FROM python:3.9

WORKDIR /app

COPY requirements.txt .

# Instalamos explícitamente uvicorn primero y luego el resto de dependencias
RUN pip install --no-cache-dir uvicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación
COPY ./app /app

# Verificamos la instalación de uvicorn
RUN pip list | grep uvicorn

# Ejecutamos la aplicación con python -m
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]