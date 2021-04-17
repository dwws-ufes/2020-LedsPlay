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
        fields = ["competencia", "livre", "profissional"]

    def clean(self, *args, **kwargs):
        cleaned_data = super(OrdemForm, self).clean(*args, **kwargs)
        if cleaned_data["livre"] is True:
            cleaned_data["profissional"] = None
        else:
            if cleaned_data["profissional"] is None:
                raise forms.ValidationError(
                    "Uma ordem direcionada (Não livre) precisa conter um profissional"
                )
        return cleaned_data
