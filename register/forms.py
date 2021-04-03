from django import forms
from .models import Pessoa, Ordem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

###TESTE###

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  ]


##TESTE###
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "sexo", "email", "cidade", "nascimento", "password"]

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs["placeholder"] = field.label
        self.fields["email"].widget.attrs["placeholder"] = "example@domain.com"
        self.fields["nascimento"].widget.attrs[
            "placeholder"
        ] = "Ano-Mês-Dia (AAAA-MM-DD)"

    def clean_email(self, *args, **kwargs):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError

        email = self.cleaned_data.get("email")

        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Email errado")

        return email


class DefineUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DefineUserForm, self).__init__(*args, **kwargs)
        choices = [('0', 'Cliente'), ('1', 'Profissional')]
        self.fields['selecione'] = forms.ChoiceField(choices=choices)


class OrdemForm(forms.ModelForm):
    class Meta:
        model = Ordem
        fields = '__all__'
