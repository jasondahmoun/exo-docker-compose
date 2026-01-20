COMPOSE = docker compose

all:
	$(COMPOSE) up --build

clean:
	$(COMPOSE) down

fclean:
	$(COMPOSE) down --rmi all

purge:
	rm -f ./data/app.db

re: fclean purge all

.PHONY: all clean fclean purge re