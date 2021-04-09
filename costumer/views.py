from .models import Cliente, Ordem
from django.contrib.auth.models import User
from register.models import Pessoa
from .forms import ClienteForm
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View
from django.forms import inlineformset_factory
from django.views import generic
from .filters import OrdemFilter
from .forms import OrdemForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateClienteView(LoginRequiredMixin, generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("costumer:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return Cliente.objects.get(pk=self.request.user.pk)


class CostumerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        cliente = Cliente.objects.get(pk=request.user.pk)
        ordens = cliente.ordem_set.all()
        order_count = ordens.count()

        myFilter = OrdemFilter(request.GET, queryset=ordens)
        ordens = myFilter.qs

        context = {
            "cliente": cliente,
            "ordens": ordens,
            "order_count": order_count,
            "myFilter": myFilter,
        }
        return render(request, "Dashboard/customer.html", context)


class CreateOrderView(LoginRequiredMixin, View):
    OrderFormSet = inlineformset_factory(Cliente, Ordem, fields=("competencia", "status"), extra=5)
    customer = None
    def get(self, request):
        self.customer = Cliente.objects.get(pk=request.user.pk)
        formset = self.OrderFormSet(queryset=Ordem.objects.none(), instance=self.customer)
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)

    def post(self, request):
        formset = self.OrderFormSet(request.POST, instance=self.customer)
        print(formset.is_valid())
        if formset.is_valid():
            formset.save()
            return redirect(reverse("costumer:dashboard"))
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)



# TODO: Transformar todas em Classes genéricas
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
