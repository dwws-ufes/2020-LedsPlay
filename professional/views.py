from django.shortcuts import render
from .models import Profissional
from .forms import ProfissionalForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def update_user_view(request, id):
    obj = get_object_or_404(Profissional, id=id)

    form = ProfissionalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("register:cadastrados"))

    return render(request, "Pessoa/detail_form.html", {"form": form, obj: obj})