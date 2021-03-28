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
## Comandos

- `./run`: Executa comandos dentro do container da aplicação
- `make help`: Mostra a explicação dos comandos executados com `make`

Acesse: http://localhost:8000

## Dependencias 

O Docker **não atualiza** mudanças de dependencias instaladas pelo `pip`, caso queira adicionar uma nova dependencia

Adicione o nome da biblioteca nova no arquivo `requirements.txt`

```python
Django>=3.0,<4.0
psycopg2-binary>=2.8
django-seed
python-dotenv
```

Digite o comando para buildar a nova imagem e inicializar a aplicação atualizada

```bash
make build up
```
