up:
	sudo docker-compose up

bash:
	sudo docker-compose exec django bash

shell:
	sudo docker-compose exec django python manage.py shell

db-up:
	sudo docker-compose exec django python manage.py makemigrations
	sudo docker-compose exec django python manage.py migrate

createsuperuser:
	sudo docker-compose exec django python manage.py createsuperuser

git-setup:
	git remote remove origin 

config:
	sudo docker-compose exec django python manage.py makemigrations
	sudo docker-compose exec django python manage.py migrate
	sudo docker-compose exec django python manage.py createsuperuser

init:
	git remote remove origin
	mv env.txt .env
	sudo docker-compose ps
	sudo docker-compose up


stop:
	docker system prune


push:
	cp .env env.txt
	git add .
	git commit -m "configurando env"
	git push
