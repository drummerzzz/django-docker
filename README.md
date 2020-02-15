## Instuções

```bash
git clone https://github.com/drummerzzz/django-docker.git
cd django-docker
make init
```
aguarde o download e instalação das dependencias, 
abra uma nova aba no terminal e rode
```bash
make config
```
pronto :)


## VsCode
É necessário intalar duas extenções pra que o vs code reconheça o ambiente python detro do container,
a primeira lógico é a extenção do Docker, segunda é a remote development.

1 instale as extenções
2 no canto inferior esquerdo você verá um icone ><
3 clique no icone e selecione reopen in container
4 tudo pronto
OBS - pode ser que algumas dependências sejam baixadas


## Instrunções para rodar o ambiente de desenvolvimento

- Você vai precisar ter o 'docker' e 'docker-compose' instalado em seu Sistema Operacional

- Se for a primeira vez que está rodando ou for feita alguma alteração nos contâineres,
pode ser necessário compilar com o comando:
```bash
sudo docker-compose build
```

- Para subir os contêineres:
```bash
make up
```
ou
```bash
sudo docker-compose up
```

- Com os contâineres rodando podemos abrir outro terminal e rodar um bash dentro do container django:
```bash
make bash
```
ou
```bash
sudo docker-compose exec django bash
```

- A partir deste bash, fazer migração:
```bash
python manage.py migrate
```
ou
```bash
make db-up
```

-Criar o super usuário:
```bash
sudo docker-compose exec django python manage.py createsuperuser
```
ou
```
make createsuperuser
```

## Outros comandos úteis
* Os nomes dos contâineres podem ser verificados com:
```bash
sudo docker ps
```

- Também é possível executar qualquer comando diretamente usando a sintax:
```bash
sudo docker-compose exec [NOME_CONTAINER] [COMANDO]
```
Ex:
```bash
sudo docker-compose exec django python manage.py test
sudo docker-compose exec django python manage.py shell
sudo docker-compose exec django python manage.py migrate
sudo docker-compose exec django python manage.py createsuperuser
```

# Importante - environment
Crie um arquivo .env na raiz do projeto com as seguintes variaveis de ambiente

```bash
DB_NAME=dbase
DB_USER=username
DB_PW=dbpassword
```