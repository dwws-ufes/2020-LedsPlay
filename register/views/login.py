from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse


from register.forms import LoginForm, DefineUserForm
from django.urls import reverse
from django.views import View
from ..models import *

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "Industrial/index.html")
        else:
            data = {"form": LoginForm()}
            return render(request, "Pessoa/login.html", data)



    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if username and password and user:
                login(request, user)
                if user.pessoa.user_type is None:
                    return HttpResponseRedirect(reverse("register:define_user"))
                return HttpResponseRedirect(reverse("dashboard"))

        data = {"form": form,
                "error": "Usuário ou Senha incorreto",
                }
        return render(request, "Pessoa/login.html", data)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index_view"))


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