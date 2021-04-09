from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from ..forms import CreateUserForm
from django.views import generic
from ..models import *


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




# def cliente_view(request):
#     context={}
#     return render(request, "Dashboard/user.html", context)
