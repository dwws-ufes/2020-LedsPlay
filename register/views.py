from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from register.models import Pessoa
from register.forms import PessoaForm


# Create your views here.

def register_create_view(request):
    form=PessoaForm(request.POST or None)
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }

    return render(request, "Pessoa/detail_create.html", context)

def register_detail_view(request, id):
    #obj = Pessoa.objects.get(id=id)
    obj = get_object_or_404(Pessoa, id=id)
    context = {
        'Pessoa': obj
    }

    return render(request, "Pessoa/detail.html", context)


def register_list_view(request):
    queryset = Pessoa.objects.all()

    context = {
        "pessoa_list":queryset
    }

    return render(request, "Pessoa/cadastrados_list_view.html", context)

def register_update_view(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("Cadastrados")

    return render(request, "Pessoa/atualizar_cadastrado.html",{"form":form, obj:obj})

def register_delete(request,id):
    obj = get_object_or_404(Pessoa, id=id)
    obj.delete()
    return render(request, "Pessoa/cadastrados_list_view.html")


