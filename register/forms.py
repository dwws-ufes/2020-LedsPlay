from django import forms

from .models import Pessoa, Vagas


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'perfil',
            'idade',
            'sexo'
        ]

class VagasForm(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = [
            'nome',
            'perfil',
            'localizacao'
        ]
