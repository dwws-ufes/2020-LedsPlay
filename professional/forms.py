from django import forms
from .models import Professional, Competence
from register.forms import PersonForm


class ProfessionalForm(PersonForm):
    class Meta:
        model = Professional
        fields = ["name", "sex", "birthdate", "cpf", "phone_number", "city"]

    def __init__(self, *args, **kwargs):
        super(ProfessionalForm, self).__init__(*args, **kwargs)
        self.fields["cpf"].widget.attrs["placeholder"] = "000.000.000-00"

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ["name", "category", "description"]

