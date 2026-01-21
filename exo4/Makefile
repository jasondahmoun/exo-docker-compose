.DEFAULT_GOAL := up
.MAIN: up

all: up

purge-bdd:
	vols="$$(docker volume ls -q | grep postgres_data || true)"; \
	if [ -n "$$vols" ]; then docker volume rm $$vols; fi || true

purge-all:
	docker-compose down --rmi all -v --remove-orphans

up:
	docker-compose up -d --build

down:
	docker-compose down

.PHONY: all purge-bdd purge-all up down
