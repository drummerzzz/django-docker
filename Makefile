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
	git remote remove origin
	sudo docker-compose exec django python manage.py makemigrations
	sudo docker-compose exec django python manage.py migrate
	sudo docker-compose exec django python manage.py createsuperuser

init:
	sudo docker-compose ps
	sudo docker-compose up


