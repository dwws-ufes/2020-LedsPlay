from django.db import models
from register.models import Pessoa


class Cliente(Pessoa):
    interesse = models.CharField(max_length=128, null=True)
