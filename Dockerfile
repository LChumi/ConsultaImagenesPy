# Usa una imagen oficial de Python
FROM python:3.12-slim

# Instala Java (requerido por jaydebeapi para usar el jar)
RUN apt-get update && apt-get install -y default-jre && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia dependencias
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu aplicación y el jar
COPY . .

# Expón el puerto de FastAPI
EXPOSE 8000

# Comando para ejecutar FastAPI con recarga deshabilitada (modo prod)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
