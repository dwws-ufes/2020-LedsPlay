from django.shortcuts import render
from register.models import Pessoa
from register.forms import PessoaForm, VagasForm


# Create your views here.

def register_detail_view(request):
    obj = Pessoa.objects.get(id=1)
    context = {
        'Pessoa': obj
    }

    return render(request, "Pessoa/detail.html", context)


def register_create_view(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, "Pessoa/detail_create.html", context)

def vagas_create_view(request):
    form = VagasForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, "Pessoa/vagas_create.html", context)
