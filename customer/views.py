from .models import Customer, Order
from django.contrib.auth.models import User
from register.models import Person
from .forms import CustomerForm
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View
from django.forms import inlineformset_factory
from django.views import generic
from .filters import OrderFilter
from .forms import OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateCustomerView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "Person/detail_form.html"
    success_url = reverse_lazy("customer:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return Customer.objects.get(pk=self.request.user.pk)


class customerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        customer = Customer.objects.get(pk=request.user.pk)
        orders = customer.order_set.all()
        order_count = orders.count()

        my_filter = OrderFilter(request.GET, queryset=orders)
        orders = my_filter.qs

        context = {
            "customer": customer,
            "orders": orders,
            "order_count": order_count,
            "myFilter": my_filter,
        }
        return render(request, "Dashboard/userdashboard.html", context)


class CreateOrderView(LoginRequiredMixin, View):
    OrderFormSet = inlineformset_factory(
        Customer,
        Order,
        fields=("competence", "status"),
        extra=5
    )
    customer = None

    def get(self, request):
        self.customer = Customer.objects.get(pk=request.user.pk)
        formset = self.OrderFormSet(
            queryset=Order.objects.none(), instance=self.customer
        )
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)

    def post(self, request):
        self.customer = Customer.objects.get(pk=request.user.pk)
        formset = self.OrderFormSet(request.POST, instance=self.customer)
        print(formset.is_valid())
        if formset.is_valid():
            formset.save()
            return redirect(reverse("customer:dashboard"))
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)


class UpdateOrderView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "Dashboard/form.html"
    success_url = reverse_lazy("customer:dashboard")

    def get_object(self, **kwargs):
        order_pk = self.kwargs.get(self.pk_url_kwarg)
        order = Order.objects.get(pk=order_pk)
        customer = Customer.objects.get(pk=self.request.user.pk)
        # Customer só edita as orders dele
        if customer == order.name:
            return order
        return None


class DeleteOrderView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    template_name = "Dashboard/delete.html"
    success_url = reverse_lazy("customer:dashboard")

    def get_object(self):
        order_pk = self.kwargs.get(self.pk_url_kwarg)
        customer = Customer.objects.get(pk=self.request.user.pk)
        order = Order.objects.get(pk=order_pk)
        # Customer só deleta as orders dele
        if customer == order.name:
            return order
        return None
