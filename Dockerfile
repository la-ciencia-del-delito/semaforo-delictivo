# Usa la imagen base de Python 3.9 slim
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install git

# Copia todos los archivos del directorio actual al contenedor
COPY . .

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

# RUN python3 -m ipykernel install --user --name=myenv --display-name="my_kernel"

# Establece el comando por defecto
CMD [ "jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888", \
      "--no-browser", "--allow-root", \
      "--NotebookApp.token=''","--NotebookApp.password=''" ]