from django import forms

from .models import Pessoa, Vaga


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
        model = Vaga
        fields = [
            'nome',
            'perfil',
            'localizacao'
        ]

class RawVagasForm(forms.Form):
    nome = forms.CharField()
    perfil = forms.CharField()
    localizacao = forms.CharField()


