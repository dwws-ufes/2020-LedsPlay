from django import forms
from .models import Pessoa, Ordem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

###TESTE###


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "sexo", "cidade", "nascimento"]

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.fields["nascimento"].widget = forms.DateInput()
        self.fields["sexo"].widget.attrs["placeholder"] = "M ou F"


class DefineUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DefineUserForm, self).__init__(*args, **kwargs)
        choices = [("0", "Cliente"), ("1", "Profissional")]
        self.fields["selecione"] = forms.ChoiceField(choices=choices)


class OrdemForm(forms.ModelForm):
    class Meta:
        model = Ordem
        fields = "__all__"
