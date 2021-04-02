from django import forms
from .models import Profissional
from register.forms import PessoaForm


class ProfissionalForm(PessoaForm):
    class Meta:
        model = Profissional
        fields = ["nome", "sexo", "email", "cpf", "contato", "cidade", "nascimento", "password"]

    def __init__(self, *args, **kwargs):
        super(ProfissionalForm, self).__init__(*args, **kwargs)
