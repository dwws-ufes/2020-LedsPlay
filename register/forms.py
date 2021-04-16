from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "sex", "city", "birthdate"]

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields["birthdate"].widget = forms.DateInput()
        self.fields["sex"].widget.attrs["placeholder"] = "M ou F"


class DefineUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DefineUserForm, self).__init__(*args, **kwargs)
        choices = [("0", "Customer"), ("1", "Professional")]
        self.fields["selecione"] = forms.ChoiceField(choices=choices)
