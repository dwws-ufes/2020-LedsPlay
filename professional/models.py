from django.db import models
from register.models import Pessoa
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField


class Profissional(Pessoa):
    cpf = CPFField("cpf", null=True)
    contato = PhoneNumberField(region="BR", null=True)
    media = models.FloatField(null=True)
