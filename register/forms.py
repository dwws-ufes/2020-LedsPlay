from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'sexo',
            'email',
            'nascimento',
            'password'
        ]
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith(".com"):
            raise forms.ValidationError("Email errado")
        return email


