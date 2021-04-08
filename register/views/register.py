from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from ..forms import DefineUserForm, CreateUserForm
from django.urls import reverse
from django.views import generic, View
from ..models import *

from costumer.models import Ordem
from professional.models import Competencia



class RegisterCreateView(SuccessMessageMixin, generic.CreateView):

    model = User
    template_name = "Pessoa/detail_form.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("register:cadastrados")
    success_message = "Sua conta foi criada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Cadastro de usuário"
        return context


@login_required(login_url="login")
def register_detail_view(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    context = {"Pessoa": obj}

    return render(request, "Pessoa/detail.html", context)


@login_required(login_url="login")
def register_list_view(request):
    queryset = User.objects.all()
    print(request.user)

    context = {"pessoa_list": queryset}

    return render(request, "Pessoa/cadastrados_list_view.html", context)


class RegisterUpdateView(generic.UpdateView):
    model = User
    success_url = reverse_lazy("register:cadastrados")
    template_name = "Pessoa/detail_form.html"
    fields = ["username", "email"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context


class RegisterDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy("register:cadastrados")
    template_name = "Pessoa/confirm_delete.html"


@login_required(login_url="login")
def register_competencia_view(request):
    competencias = Competencia.objects.all()
    context = {"competencias_list": competencias}
    return render(request, "Competencias/competencias_list_view.html", context)


################################################
# TESTE
################################################


@login_required(login_url="login")
def dashboard(request):
    orders = Ordem.objects.all()
    customers = User.objects.all()
    competencias = Competencia.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status="FINALIZADO").count()
    pending = orders.filter(status="STAND BY").count()

    context = {
        "orders": orders,
        "customers": customers,
        "competencias": competencias,
        "total_orders": total_orders,
        "delivered": delivered,
        "pending": pending,
    }

    return render(request, "Dashboard/dashboard.html", context)


# def products(request):
#     products = Competencia.objects.all()

#     return render(request, "Dashboard/products.html", {"products": products})

# def cliente_view(request):
#     context={}
#     return render(request, "Dashboard/user.html", context)