COMPOSE = docker compose

all:
	$(COMPOSE) up --build

clean:
	$(COMPOSE) down

fclean:
	$(COMPOSE) down --rmi all

re: fclean all

.PHONY: all clean fclean re