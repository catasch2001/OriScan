FROM continuumio/miniconda3

COPY . /app
WORKDIR /app

RUN conda env create -f environment.yml

# Activamos el entorno para que esté disponible en el PATH
ENV PATH /opt/conda/envs/oriscan-env/bin:$PATH
