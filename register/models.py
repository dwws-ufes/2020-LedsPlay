from django.db import models
import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    sexo = models.CharField(max_length=1)
    email = models.EmailField(max_length=120)
    nascimento = models.DateField(default=datetime.date.today)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nome
