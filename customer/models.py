from django.db import models
from register.models import Person
from professional.models import Competence, Professional


class Customer(Person):
    interested_in = models.CharField(max_length=128, null=True)

    def is_updated(self):
        fields = [
            self.interested_in is None,
        ]
        return not any(fields)


class Order(models.Model):
    status_options = (
        ("STAND BY", "STAND BY"),
        ("EM OPERAÇÃO", "EM OPERAÇÃO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    name = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    competence = models.ForeignKey(Competence, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=120, null=True, choices=status_options)
    free = models.BooleanField(null=True, default=True) # True para order free, False para order direcionada
    professional = models.ForeignKey(Professional, null=True, blank=True, on_delete=models.SET_NULL)
    accepted = models.BooleanField(null=True, default=False)# Define se a order foi aceita ou não (order direcionada)

    # Retorna se a order é free (não-direcionada)
    def is_free(self):
        return self.free

    # Retorna se a order está aberta
    def is_open(self):
        return self.professional is None and self.is_free()

    # Se a order for direcionada, aceita.
    def accept(self):
        if not self.is_free():
            self.accepted = True
            self.save()

    # Se a order for direcionada, rejeita e abre a order
    def refuse(self):
        if not self.is_free():
            self.professional = None
            self.free = True
            self.save()

    # Pega a order, passando o objeto do professional para atribuir
    def take(self, taker: Professional):
        if self.is_open():
            self.professional = taker
            self.save()

    # Retorna se a order foi pega
    def is_took(self):
        if self.is_free():
            return self.professional is not None
        else:
            return self.accepted

    # Retorna se a order está esperando para ser aceita, se for direcionada
    def is_waiting_accept(self):
        return not self.is_free() and not self.accepted

    def __str__(self):
        return f"Order de {self.competence}"

