from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse

from costumer.models import Ordem, Cliente
from professional.models import Competencia


from register.forms import DefineUserForm
from django.urls import reverse
from django.views import View
from ..models import *


class DefineUserTypeView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.pessoa.user_type is not None:
            return HttpResponseRedirect(
                reverse("index_view")
            )  ## TODO: Retornar para a tela de configuração do profissional/cliente
        data = {"form": DefineUserForm()}

        return render(request, "Pessoa/define_user.html", data)

    def post(self, request):
        form = DefineUserForm(data=request.POST)
        user = request.user

        if form.is_valid():
            if user.pessoa.user_type is not None:
                return HttpResponseRedirect(
                    reverse("index_view")
                )  ## TODO: Retornar para a tela de configuração do profissional/cliente
            choice = int(form.cleaned_data["selecione"])
            if choice == 0:
                from costumer.models import Cliente

                subclass = Cliente
            elif choice == 1:
                from professional.models import Profissional

                subclass = Profissional
            else:
                return HttpResponse(request, status=404)
            user.pessoa.convert(subclass)
            return HttpResponseRedirect(
                reverse("index_view")
            )  ## TODO: Retornar para a tela de configuração do profissional/cliente

        return render(request, "Pessoa/define_user.html", {"form": form})


class GeneralDashboard(LoginRequiredMixin, View):
    def get(self, request):
        orders = Ordem.objects.all()
        customers = Cliente.objects.all()
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
