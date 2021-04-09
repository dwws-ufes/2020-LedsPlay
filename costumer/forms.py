from .models import Cliente, Ordem
from register.forms import PessoaForm
from django import forms


class ClienteForm(PessoaForm):
    class Meta:
        model = Cliente
        fields = ["nome", "sexo", "nascimento", "cidade", "interesse"]


class OrdemForm(forms.ModelForm):

    class Meta:
        model = Ordem
        fields = "__all__"


