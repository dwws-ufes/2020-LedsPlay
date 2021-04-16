from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.forms import ValidationError


from ..forms import CreateUserForm
from django.views import generic, View


class RegisterCreateView(SuccessMessageMixin, generic.CreateView):

    model = User
    template_name = "Pessoa/detail_form.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("register:cadastrados")
    success_message = "Sua conta foi criada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Cadastro de usuário"
        return context

class UserUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = User
    success_url = reverse_lazy("dashboard")
    template_name = "Pessoa/detail_form.html"
    fields = ["username", "email"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return self.request.user

class PasswordUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        form = PasswordChangeForm(user)
        context = {"page_title": "Alterar senha", "form": form}
        return render(request, "Pessoa/detail_form.html", context)

    def post(self, request):
        user = request.user
        form = PasswordChangeForm(user, data=request.POST or None)
        if form.is_valid():
            if form.cleaned_data["old_password"] == form.cleaned_data["new_password1"]:
                form.add_error(None, ValidationError("Sua senha nova é igual a senha antiga!"))
            else:
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("dashboard")

        context = {"page_title": "Alterar senha", "form": form}
        return render(request, "Pessoa/detail_form.html", context)


# TODO: View possivelmente inutil
@login_required(login_url="login")
def register_list_view(request):
    queryset = User.objects.all()

    context = {"pessoa_list": queryset}

    return render(request, "Pessoa/cadastrados_list_view.html", context)


class RegisterDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy("register:cadastrados")
    template_name = "Pessoa/confirm_delete.html"
