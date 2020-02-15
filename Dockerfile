# Imagem do python 3.8
FROM python:3.8
# Variáveis de ambiente
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SECRET_KEY 'abcde0s&&$uyc)hf_3rv@!a95nasd22e-dxt^9k^7!f+$jxkk+$k-'
# Cria pasta da aplicação no container
RUN mkdir /app
WORKDIR /app
# Instala dependências no OS
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
# Copia  e instala o conteúdo de requirements.txt
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/
# Django service
EXPOSE 8000