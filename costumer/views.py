from .models import Cliente, Ordem
from django.contrib.auth.models import User
from register.models import Pessoa
from .forms import ClienteForm
from django.urls.base import reverse_lazy
from django.views import generic
from django.forms import inlineformset_factory
from .filters import OrdemFilter
from .forms import OrdemForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

class UpdateClienteView(generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy(
        "register:cadastrados"
    )  # TODO: Redirecionar pra dashboard do Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return Cliente.objects.get(pk=self.request.user.pk)

@login_required(login_url="login")
def customer(request, pk):
    pessoa = Cliente.objects.get(pk=pk)
    ordens = pessoa.ordem_set.all()
    order_count = ordens.count()

    myFilter = OrdemFilter(request.GET, queryset=ordens)
    ordens = myFilter.qs

    context = {
        "pessoa": pessoa,
        "ordens": ordens,
        "order_count": order_count,
        "myFilter": myFilter,
    }
    return render(request, "Dashboard/customer.html", context)


@login_required(login_url="login")
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        User, Ordem, fields=("competencia", "status"), extra=5
    )
    customer = Pessoa.objects.get(id=pk)
    formset = OrderFormSet(queryset=Ordem.objects.none(), instance=customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"formset": formset}
    return render(request, "Dashboard/form.html", context)


@login_required(login_url="login")
def updateOrdem(request, pk):
    order = Ordem.objects.get(id=pk)
    form = OrdemForm(instance=order)

    if request.method == "POST":
        form = OrdemForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "Dashboard/form.html", context)


@login_required(login_url="login")
def deleteOrdem(request, pk):
    order = Ordem.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")
    context = {"order": order}
    return render(request, "Dashboard/delete.html", context)
