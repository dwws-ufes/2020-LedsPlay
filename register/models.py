from django.db import models
import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=120, null=True)
    sexo = models.CharField(max_length=1, null=True)
    email = models.EmailField(max_length=120, null=True)
    CEP = models.CharField(max_length=120, null=True)
    nascimento = models.DateField(default=datetime.date.today, null=True)
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    STATUS = (
        ("CATEGORIA 1", "CATEGORIA 1"),
        ("CATEGORIA 2", "CATEGORIA 2"),
        ("CATEGORIA 3", "CATEGORIA 3"),
    )

    nome = models.CharField(max_length=120, null=True)
    categoria = models.CharField(max_length=120, null=True, choices=STATUS)
    descricao = models.CharField(max_length=120, null=True)
    data_created = models.CharField(max_length=120, null=True)


class Ordem(models.Model):
    STATUS = (
        ("STANDBY", "STANDBY"),
        ("EM OPERATAÇÃO", "EM OPERAÇÂO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    # costumer =
    # Competencia =
    data_created = models.CharField(max_length=120, null=True)
    status = models.CharField(max_length=120, null=True, choices=STATUS)
