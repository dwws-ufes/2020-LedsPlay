from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from register.forms import PessoaForm, DefineUserForm, OrdemForm, CreateUserForm, LoginForm
from django.urls import reverse
from django.views import generic, View
from .models import *
from .filters import OrdemFilter


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'Pessoa/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username and password and user:
                login(request, user)
                return HttpResponseRedirect(reverse('index_view'))
        
        data = { 
            'form': form,
            'error': 'Username ou password incorreto'
        }     
        return render(request, 'Pessoa/login.html', data)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index_view'))

class RegisterCreateView(SuccessMessageMixin, generic.CreateView):
   model = User
   template_name = "Pessoa/detail_form.html"
   form_class = CreateUserForm
   success_url = reverse_lazy("register:cadastrados")
   success_message = 'Sua conta foi criada com sucesso!'

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Cadastro de usuário"
        return context


def register_detail_view(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    context = {"Pessoa": obj}

    return render(request, "Pessoa/detail.html", context)


def register_list_view(request):
    queryset = User.objects.all()
    print(request.user)

    context = {"pessoa_list": queryset}

    return render(request, "Pessoa/cadastrados_list_view.html", context)


def register_update_view(request, id):
    obj = get_object_or_404(User, id=id)
    form = CreateUserForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("register:cadastrados"))

    return render(request, "Pessoa/detail_form.html", {"form": form, obj: obj})


class RegisterDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy("register:cadastrados")
    template_name = "Pessoa/confirm_delete.html"


def define_user_type_view(request, id):
    form = DefineUserForm(request.POST or None)
    if form.is_valid():
        obj = get_object_or_404(Pessoa, id=id)
        if obj.user_type is not None:
            return HttpResponseNotFound('Seu tipo de usuário já foi definido anteriormente!') # TODO: Retornar pra uma página de erro
        choice = int(form.cleaned_data['selecione'])
        if choice == 0:
            from costumer.models import Cliente
            subclass = Cliente
        elif choice == 1:
            from professional.models import Profissional
            subclass = Profissional
        else:
            return HttpResponse(request, status=404)
        obj.convert(subclass)
        return HttpResponseRedirect(
            reverse("register:cadastrados"))  ## TODO: Retornar para a tela de configuração do profissional/cliente

    return render(request, "Pessoa/define_user.html", {"form": form})


def register_competencia_view(request):
    competencias = Competencia.objects.all()
    context = {"competencias_list": competencias}
    return render(request, "Competencias/competencias_list_view.html", context)


################################################
# TESTE
################################################

def home(request):
    orders = Ordem.objects.all()
    customers = Pessoa.objects.all()
    competencias = Competencia.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='FINALIZADO').count()
    pending = orders.filter(status='STAND BY').count()

    context = {'orders': orders,
               'customers': customers,
               'competencias': competencias,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending}

    return render(request, 'Dashboard/dashboard.html', context)


def products(request):
    products = Competencia.objects.all()

    return render(request, 'Dashboard/products.html', {'products': products})


def customer(request, pk):
    pessoa = Pessoa.objects.get(id=pk)
    ordens = pessoa.ordem_set.all()
    order_count = ordens.count()

    myFilter = OrdemFilter(request.GET, queryset=ordens)
    ordens = myFilter.qs

    context = {'pessoa': pessoa,
               'ordens': ordens,
               'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'Dashboard/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Pessoa, Ordem, fields=('competencia', 'status'), extra=5)
    customer = Pessoa.objects.get(id=pk)
    formset = OrderFormSet(queryset=Ordem.objects.none(), instance=customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'Dashboard/form.html', context)


def updateOrdem(request, pk):
    order = Ordem.objects.get(id=pk)
    form = OrdemForm(instance=order)

    if request.method == "POST":
        form = OrdemForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Dashboard/form.html', context)


def deleteOrdem(request, pk):
    order = Ordem.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'Dashboard/delete.html', context)
