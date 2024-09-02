# Usa una imagen base de Python
FROM python:3.10-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará tu aplicación Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "run.py"]
