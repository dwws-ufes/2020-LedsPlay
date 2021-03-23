from django.db import models
import datetime

class Pessoa(models.Model):
    nome = models.CharField(default="Nome", max_length=120)
    sexo = models.CharField(default="M or F", max_length=1)
    email = models.EmailField(default="Email", max_length=120)
    nascimento = models.DateField(("Date"), default=datetime.date.today)
    password = models.CharField(default="password", max_length=128)
