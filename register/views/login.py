from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


from register.forms import LoginForm
from django.urls import reverse
from django.views import View


class LoginView(View):
    def get(self, request):
        data = {"form": LoginForm()}
        return render(request, "Person/login.html", data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if username and password and user:
                login(request, user)
                return redirect("dashboard")

        data = {
            "form": form,
            "error": "Usuário ou Senha incorreto",
        }
        return render(request, "Person/login.html", data)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("index")
