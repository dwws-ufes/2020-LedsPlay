from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    perfil = models.TextField(blank=True, null=True)
    idade = models.IntegerField(default=0)
