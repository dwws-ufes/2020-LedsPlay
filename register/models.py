from django.db import models
import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=120, null=True)
    sexo = models.CharField(max_length=1, null=True)
    email = models.EmailField(max_length=120, null=True)
    cidade = models.CharField(max_length=120, null=True)
    nascimento = models.DateField(default=datetime.date.today, null=True)
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return "%s" % self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=120, null=True)

    def __str__(self):
        return "%s" % self.nome


class Competencia(models.Model):
    STATUS = (
        ("CATEGORIA 1", "CATEGORIA 1"),
        ("CATEGORIA 2", "CATEGORIA 2"),
        ("CATEGORIA 3", "CATEGORIA 3"),
    )

    nome = models.CharField(max_length=120, null=True)
    categoria = models.CharField(max_length=120, null=True, choices=STATUS)
    descricao = models.CharField(max_length=120, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "%s" % self.nome


class Ordem(models.Model):
    STATUS = (
        ("STAND BY", "STAND BY"),
        ("EM OPERATAÇÃO", "EM OPERAÇÂO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    nome = models.ForeignKey(Pessoa, null=True, on_delete=models.SET_NULL)
    competencia = models.ForeignKey(Competencia, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=120, null=True, choices=STATUS)

    def __str__(self):
        return "%s" % self.competencia