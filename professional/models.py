from django.db import models
from register.models import Pessoa

class Profissional(Pessoa):
    cpf = models.CharField(max_length=14, null=True)
    contato = models.CharField(max_length=20, null=True)
    media = models.FloatField(null=True)