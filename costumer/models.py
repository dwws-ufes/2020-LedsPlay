from django.db import models
from register.models import Pessoa
from professional.models import Competencia, Profissional


class Cliente(Pessoa):
    interesse = models.CharField(max_length=128, null=True)

    def is_updated(self):
        fields = [
            self.interesse is None,
        ]
        return not any(fields)


class Ordem(models.Model):
    status_options = (
        ("STAND BY", "STAND BY"),
        ("EM OPERAÇÃO", "EM OPERAÇÃO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    nome = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    competencia = models.ForeignKey(Competencia, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=120, null=True, choices=status_options, default="STAND BY")
    livre = models.BooleanField(null=False, default=True) # True para ordem livre, False para ordem direcionada
    profissional = models.ForeignKey(Profissional, null=True, blank=True, on_delete=models.SET_NULL)
    accepted = models.BooleanField(null=False, default=False)# Define se a ordem foi aceita ou não (ordem direcionada)

    # Retorna se a ordem é livre (não-direcionada)
    def is_free(self):
        return self.livre

    # Retorna se a ordem está aberta
    def is_open(self):
        return self.profissional is None and self.is_free()

    # Se a ordem for direcionada, aceita.
    def accept(self):
        if not self.is_free():
            self.accepted = True
            self.save()

    # Se a ordem for direcionada, rejeita e abre a ordem 
    def refuse(self):
        if not self.is_free():
            self.profissional = None
            self.livre = True
            self.save()

    # Pega a ordem, passando o objeto do profissional para atribuir
    def take(self, taker: Profissional):
        if self.is_open():
            self.profissional = taker
            self.save()

    # Retorna se a ordem foi pega
    def is_took(self):
        if self.is_free():
            return self.profissional is not None
        else:
            return self.accepted

    # Retorna se a ordem está esperando para ser aceita, se for direcionada
    def is_waiting_accept(self):
        return not self.is_free() and not self.accepted

    def __str__(self):
        return f"Ordem de {self.competencia}"

