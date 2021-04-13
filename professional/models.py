from django.db import models
from register.models import Pessoa
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField


class Profissional(Pessoa):
    cpf = CPFField("cpf", null=True)
    telefone = PhoneNumberField(region="BR", null=True)
    media = models.FloatField(null=True)

    def is_updated(self):
        fields = [
            self.cpf is None,
            self.telefone is None,
        ]
        return not any(fields)


class Competencia(models.Model):
    status_options = (
        ("CATEGORIA 1", "CATEGORIA 1"),
        ("CATEGORIA 2", "CATEGORIA 2"),
        ("CATEGORIA 3", "CATEGORIA 3"),
    )

    nome = models.CharField(max_length=120, null=True)
    categoria = models.CharField(max_length=120, null=True, choices=status_options)
    descricao = models.CharField(max_length=120, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome
