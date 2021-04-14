from django import forms
from .models import Profissional, Competencia
from register.forms import PessoaForm


class ProfissionalForm(PessoaForm):
    class Meta:
        model = Profissional
        fields = ["nome", "sexo", "nascimento", "cpf", "telefone", "cidade"]

    def __init__(self, *args, **kwargs):
        super(ProfissionalForm, self).__init__(*args, **kwargs)
        self.fields["cpf"].widget.attrs["placeholder"] = "000.000.000-00"


class OrdemForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = "__all__"

        
class CompetenciaForm(PessoaForm):
    class Meta:
        model = Competencia
        fields = ["nome", "categoria", "descricao"]

    def __init__(self, *args, **kwargs):
        super(CompetenciaForm, self).__init__(*args, **kwargs)
