# DWWS-LedsPlay
Sistema de Gestão de Competências com Gamificação, construído como requisito parcial para a aprovação na disciplina de Desenvolvimento Web e Web Semântica em 2020/2E.

<!-- O site está temporariamente hospedado no url a seguir: https://ledsplay.davipetris.me/ -->

## Requisitos

- `docker`
- `docker-compose`
- `make`

## Inicializando o projeto

```bash
make # Gerar e iniciar o container da aplicação
make migrate migrations populate # Preparar o banco de dados e populá-lo com resultados de consultas SPARQL
```

Então acesse: http://localhost:8000

Caso ocorra problemas de permissão durante o Make (e.g. PermissionError: [Errno 13] Permission denied), execute:

```bash
sudo groupadd docker # criar um grupo docker
sudo usermod -aG docker $USER # Adicione seu usuário ao grupo docker.
```

## Comandos

- `./run`: Executa comandos dentro do container da aplicação
- `make help`: Mostra a explicação dos comandos executados com `make`

## Dependências

O Docker **não atualiza** mudanças de dependencias instaladas pelo `pip`. Caso queira adicionar uma nova dependência, adicione o nome da biblioteca nova no arquivo `requirements.txt`

```python
Django>=3.0,<4.0
psycopg2-binary>=2.8
django-seed
django-filter==2.4.0
django-cpf==0.1.0
django-phonenumber-field[phonenumbers]==5.0.0
```

Digite o comando a seguir para buildar a nova imagem e inicializar a aplicação atualizada:

```bash
make build up
```
