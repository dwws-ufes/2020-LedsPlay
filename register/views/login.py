from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from costumer.models import Ordem, Cliente
from professional.models import Competencia


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
