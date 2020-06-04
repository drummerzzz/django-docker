#!/bin/bash
# Diretorio e arquivo de log
set -e
LOGFILE=/home/ubuntu/viralize/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
# Numero de processo simultaneo, modifique de acordo com seu processador
NUM_WORKERS=1
# Usuario/Grupo que vai rodar o gunicorn
USER=ubuntu
#GROUP=root
# Endereço local que o gunicorn irá rodar
ADDRESS=127.0.0.1:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
source /home/ubuntu/env/bin/activate
cd /home/ubuntu/viralize/
# Migrate dos models
python manage.py makemigrations;
python manage.py migrate;
#Executa o gunicorn
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn viralize.wsgi:application
