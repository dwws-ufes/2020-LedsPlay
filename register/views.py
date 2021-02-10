from django.shortcuts import render
from .models import Pessoa


# Create your views here.

def register_detail_view(request):
    obj = Pessoa.objects.get(id=1)
    context = {
        'Nome': obj.nome,
        'Perfil': obj.perfil,
        'Idade': obj.idade

    }


    return render(request, "Pessoa/detail.html", context)
