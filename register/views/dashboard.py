from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User

from customer.models import Order, Customer
from professional.models import Competence, Professional

from register.forms import DefineUserForm
from django.urls import reverse
from django.views import View


class DefineUserTypeView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.person.user_type is not None:
            return redirect("dashboard")
        data = {"form": DefineUserForm()}

        return render(request, "Person/define_user.html", data)

    def post(self, request):
        form = DefineUserForm(data=request.POST)
        user = request.user

        if form.is_valid():
            if user.person.user_type is not None:
                return redirect("dashboard")
            choice = int(form.cleaned_data["selecione"])
            entities = [Customer, Professional]
            if choice in range(len(entities)):
                user.person.convert(entities[choice])

            return redirect("dashboard")

        return render(request, "Person/define_user.html", {"form": form})


class UserDashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.person.user_type is None:
            return redirect("register:define_user")
        elif user.person.user_type == "Customer":
            customer = user.person.customer
            if customer.is_updated():
                return redirect("customer:dashboard")
            else:
                return redirect("customer:edit")
        elif user.person.user_type == "Professional":
            professional = user.person.professional
            if professional.is_updated():
                return redirect("professional:dashboard")
            else:
                return redirect("professional:edit")

        return redirect("index")


class GeneralDashboard(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.all()
        customers = Customer.objects.all()
        user = request.user
        competences = Competence.objects.all()

        total_orders = orders.count()
        delivered = orders.filter(status="FINALIZADO").count()
        pending = orders.filter(status="STAND BY").count()

        context = {
            "orders": orders,
            "user": user,
            "customers": customers,
            "competences": competences,
            "total_orders": total_orders,
            "delivered": delivered,
            "pending": pending,
        }

        return render(request, "Dashboard/dashboard.html", context)


class SearchPage(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        customers = User.objects.all()
        search = request.GET.get("search")
        if search == "":
            competences = Competence.objects.all()
        else:
            competences = Competence.objects.all().filter(name=search)
            # professional = Professional.objects.all().filter(name=search) TODO: buscar profissionais

        context = {
            "user": user,
            "customers": customers,
            "competences": competences,
        }

        return render(request, "Dashboard/searchPage.html", context)
