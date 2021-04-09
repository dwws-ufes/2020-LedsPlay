from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy

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
            return redirect("costumer:dashboard")
        data = {"form": DefineUserForm()}

        return render(request, "Pessoa/define_user.html", data)

    def post(self, request):
        form = DefineUserForm(data=request.POST)
        user = request.user

        if form.is_valid():
            if user.pessoa.user_type is not None:
                return redirect("costumer:dashboard")
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
            return redirect("costumer:dashboard")

        return render(request, "Pessoa/define_user.html", {"form": form})


class UserDashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.pessoa.user_type is None:
            return redirect("register:define_user")
        elif user.pessoa.user_type == "Cliente":
            cliente = user.pessoa.cliente
            if cliente.interesse is None:
                return redirect("costumer:edit")
            else:
                return redirect("costumer:dashboard")
        elif user.pessoa.user_type == "Profissional":
            profissional = user.pessoa.profissional
            if profissional.cpf is None:
                return redirect("professional:edit")
            else:
                # return redirect("costumer:dashboard") # TODO: redirecionar pra dashboard do profissional
                pass

        return redirect("index_view")


class GeneralDashboard(LoginRequiredMixin, View):
    def get(self, request):
        orders = Ordem.objects.all()
        customers = Cliente.objects.all()
        user = request.user
        competencias = Competencia.objects.all()

        total_orders = orders.count()
        delivered = orders.filter(status="FINALIZADO").count()
        pending = orders.filter(status="STAND BY").count()

        context = {
            "orders": orders,
            "user": user,
            "customers": customers,
            "competencias": competencias,
            "total_orders": total_orders,
            "delivered": delivered,
            "pending": pending,
        }

        return render(request, "Dashboard/dashboard.html", context)
