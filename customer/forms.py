from .models import Customer, Order
from register.forms import PersonForm
from django import forms


class CustomerForm(PersonForm):
    class Meta:
        model = Customer
        fields = ["name", "sex", "birthdate", "city", "interested_in"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
