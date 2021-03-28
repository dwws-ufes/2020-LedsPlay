.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## Docker tasks: ##

all: down up ## Executa 'down' depois 'up'. Pode ser executado com apenas 'make'

up: ## Inicializa a stack de containers da aplicação
	docker-compose up -d

down: ## Finaliza a stack de containers da aplicação
	docker-compose down

down-v: ## Finaliza a stack e remove os dados
	docker-compose down -v

down-all: ## Finaliza a stack, remove os dados e as imagens da aplicação
	docker-compose down -v --rmi all

build: ## Faz o build da imagem da aplicação
	docker-compose build

access: ## Cria uma sessão bash dentro do container da aplicação
	docker-compose exec app bash

restart: ## Reinicia o container da aplicação
	docker-compose restart app

logs: ## Mostra os logs na tela (somente aplicação)
	docker-compose logs -f app

logs-all: ## Mostra os logs na tela (todos os containers)
	docker-compose logs -f

migrations: ## Executa as migrations caso haja mudança
	docker-compose exec app python manage.py makemigrations

migrate: ## Execute as migrations de banco (cria tabelas)
	docker-compose exec app python manage.py migrate

shell: ## Abre um python shell dentro do container da aplicação
	docker-compose exec app python manage.py shell
