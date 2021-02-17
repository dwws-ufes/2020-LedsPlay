from django.shortcuts import render
from register.models import Pessoa, Vaga
from register.forms import PessoaForm, VagasForm, RawVagasForm


# Create your views here.

def register_detail_view(request):
    obj = Pessoa.objects.get(id=1)
    context = {
        'Pessoa': obj
    }

    return render(request, "Pessoa/detail.html", context)


def register_create_view(request):
    form = PessoaForm(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, "Pessoa/detail_create.html", context)

def vagas_create_view(request):
    form = RawVagasForm()
    if request.method=="POST":
        form=RawVagasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Vaga.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {
        "form":form
    }
    return render(request, "Vagas/vagas_create.html", context)

# def vagas_create_view(request):
#     form = VagasForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#
#     return render(request, "Vagas/vagas_create.html", context)


def vagas_detail_view(request):
    obj = Vaga.objects.get(id=1)
    context = {
        'Vagas': obj
    }

    return render(request, "Vagas/detail.html", context)
