# Etapa 1: Construcción de dependencias
FROM python:3.11-slim AS builder

# Instala dependencias del sistema necesarias para OpenCV y TensorFlow
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia requirements.txt e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagen final
FROM python:3.11-slim

# Instala solo el JRE y dependencias mínimas para ejecución
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Crea un usuario no root
RUN useradd -m myuser
USER myuser

# Establece el directorio de trabajo
WORKDIR /app

# Copia las dependencias instaladas desde la etapa de construcción
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia el código de la aplicación y el JAR
COPY . .

# Expón el puerto
EXPOSE 8000

# Configura un healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/health || exit 1

# Ejecuta la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]