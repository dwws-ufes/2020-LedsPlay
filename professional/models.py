from django.db import models
from register.models import Pessoa
from cpf_field.models import CPFField
class Profissional(Pessoa):
    cpf = CPFField('cpf', null=True)
    contato = models.CharField(max_length=20, null=True)
    media = models.FloatField(null=True)