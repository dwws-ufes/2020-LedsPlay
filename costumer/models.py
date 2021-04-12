from django.db import models
from register.models import Pessoa
from professional.models import Competencia


class Cliente(Pessoa):
    interesse = models.CharField(max_length=128, null=True)


class Ordem(models.Model):
    STATUS = (
        ("STAND BY", "STAND BY"),
        ("EM OPERAÇÃO", "EM OPERAÇÃO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    nome = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    competencia = models.ForeignKey(Competencia, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=120, null=True, choices=STATUS)

    def __str__(self):
        return f"Ordem de {self.competencia}"
