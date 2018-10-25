# DOCKER DEPLOY ------------------------------------------------
file := "docker-compose.yml"

up:
	# Create and start containers
	sudo docker-compose up -d db
	sleep 10
	sudo docker-compose up -d web
	sudo docker-compose up -d metabase
	sudo docker-compose logs -f

build:
	# Rebuild the docker compose
	sudo docker-compose build

restart:
	# Restart services
	sudo docker-compose restart

logs:
	# View output from containers
	sudo docker-compose logs

start:
	# Start services
	sudo docker-compose start

stop:
	# Stop services
	sudo docker-compose stop

ps:
	# List all running containers
	sudo docker-compose ps

down:
	# Stop and Remove all containers
	sudo docker-compose down

migrations:
	# Create migrations
	sudo docker-compose run web python manage.py makemigrations
	sudo docker-compose run web python manage.py makemigrations importdata
	sudo docker-compose run web python manage.py makemigrations metabase

migrate:
	# Migrate migrations
	sudo docker-compose run web python manage.py migrate
	sudo docker-compose run web python manage.py migrate importdata
	sudo docker-compose run web python manage.py migrate metabase

fixture:
	# Generate fixtures saved upon importdata models
	sudo docker-compose run web python manage.py dumpdata importdata --format json > CrossData/importdata/fixtures/data.json

loaddata:
	# load fixtures saved upon importdata models
	sudo docker-compose run web python manage.py loaddata data.json

test:
	# run unit tests
	sudo docker-compose run web python manage.py test
