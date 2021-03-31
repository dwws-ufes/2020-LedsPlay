from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls.base import reverse_lazy
from register.models import Pessoa
from register.forms import PessoaForm
from django.urls import reverse
from django.views import generic

# Create your views here.

def login_view(request):
    return render(request, "Pessoa/login.html")

class RegisterCreateView(generic.CreateView):
    model = Pessoa
    template_name = "Pessoa/detail_create.html"
    form_class = PessoaForm
    success_url = reverse_lazy("register:cadastrados")


def register_detail_view(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    context = {"Pessoa": obj}

    return render(request, "Pessoa/detail.html", context)


def register_list_view(request):
    queryset = Pessoa.objects.all()

    context = {"pessoa_list": queryset}

    return render(request, "Pessoa/cadastrados_list_view.html", context)


def register_update_view(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("register:cadastrados"))

    return render(request, "Pessoa/atualizar_cadastrado.html", {"form": form, obj: obj})


class RegisterDeleteView(generic.DeleteView):
    model = Pessoa
    success_url = reverse_lazy("register:cadastrados")
    template_name = "Pessoa/confirm_delete.html"
