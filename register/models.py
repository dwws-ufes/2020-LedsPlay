from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    perfil = models.TextField(blank=True, null=True)
    idade = models.IntegerField(default=0)
    sexo= models.CharField(default=0,max_length=2)

class Vaga(models.Model):
    nome = models.CharField(max_length=120)
    perfil = models.TextField(blank=True, null=True)
    localizacao = models.CharField(max_length=120)