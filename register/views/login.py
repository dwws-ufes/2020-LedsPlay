from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from register.forms import LoginForm
from django.urls import reverse
from django.views import View
from ..models import *


class LoginView(View):
    def get(self, request):
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
                return HttpResponseRedirect(reverse("index_view"))

        data = {"form": form, "error": "Usuário ou Senha incorreto"}
        return render(request, "Pessoa/login.html", data)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index_view"))
