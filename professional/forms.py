from django import forms
from .models import Profissional
from register.forms import PessoaForm


class ProfissionalForm(PessoaForm):
    class Meta:
        model = Profissional
        fields = ["nome", "sexo", "nascimento", "cpf", "contato", "cidade"]

    def __init__(self, *args, **kwargs):
        super(ProfissionalForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['placeholder'] = "000.000.000-00"