# DWWS-LedsPlay
08/02/2021
## Requisitos

- docker
- docker-compose
- make

## Inicializando o projeto

```bash
make # Gerar e iniciar o container da aplicação
make migrate migrations # Preparar o banco de dados
```

Acesse: http://localhost:8000

## Comandos

- `./run`: Executa comandos dentro do container da aplicação
- `make help`: Mostra a explicação dos comandos executados com `make`