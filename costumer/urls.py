from django.urls import path

from . import views

app_name = "costumer"
urlpatterns = [
    path("dashboard/", views.CostumerDashboardView.as_view(), name="dashboard"),
    path("order/create/", views.CreateOrderView.as_view(), name="createOrder"),
    path("order/update/<int:pk>", views.UpdateOrderView.as_view(), name="updateOrder"),
    path("order/delete/<int:pk>", views.DeleteOrderView.as_view(), name="deleteOrder"),
    path("edit/", views.UpdateCustomerView.as_view(), name="edit"),
]
