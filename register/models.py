from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Pessoa(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=120, null=True)
    sexo = models.CharField(max_length=1, null=True)
    cidade = models.CharField(max_length=120, null=True)
    nascimento = models.DateField(default=datetime.date.today, null=True)
    user_type = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return "%s" % self.nome

    def convert(self, subclass):
        self.user_type = subclass.__name__
        self.save()
        fields = [f.name for f in self._meta.fields if f.name != "id"]
        values = dict([(x, getattr(self, x)) for x in fields])
        new_instance = subclass(**values)
        self.delete()
        new_instance.save()


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Pessoa.objects.create(user=instance)
    instance.pessoa.nome = instance.username
    instance.pessoa.save()
