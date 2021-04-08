from django.urls import path

from . import views

app_name = "costumer"
urlpatterns = [
    path("dashboard/", views.CostumerDashboardView.as_view(), name="dashboard"),
    path("order/create/", views.CreateOrderView.as_view(), name="createOrdem"),
    path("order/update/<int:pk>", views.updateOrdem, name="updateOrdem"),
    path("order/delete/<int:pk>", views.deleteOrdem, name="deleteOrdem"),
    path("edit/", views.UpdateClienteView.as_view(), name="edit"),
]
