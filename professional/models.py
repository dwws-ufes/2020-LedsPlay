from django.db import models
from register.models import Person
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField


class Competence(models.Model):
    status_options = (
        ("CATEGORY 1", "CATEGORY 1"),
        ("CATEGORY 2", "CATEGORY 2"),
        ("CATEGORY 3", "CATEGORY 3"),
    )

    name = models.CharField(max_length=120, null=True)
    category = models.CharField(max_length=120, null=True, choices=status_options)
    description = models.CharField(max_length=120, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Professional(Person):
    cpf = CPFField("cpf", null=True)
    phone_number = PhoneNumberField(region="BR", null=True)
    average = models.FloatField(null=True)
    competence = models.ManyToManyField(Competence)

    def is_updated(self):
        fields = [
            self.cpf is None,
            self.phone_number is None,
        ]
        return not any(fields)

class Rating(models.Model):
    professional = models.ForeignKey(Professional, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    description = models.CharField(max_length=120, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Nota %s; %s" % self.score, self.description
