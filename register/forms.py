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
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError

        email = self.cleaned_data.get("email")

        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Email errado")

        return email


