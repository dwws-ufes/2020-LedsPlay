from django.urls import path

from . import views

app_name = "costumer"
urlpatterns = [
    path("dashboard/", views.customer, name="dashboard"),
    path("dashboard/<int:pk>", views.customer, name="dashboard"),
    path("order/create/", views.createOrder, name="createOrdem"),
    path("order/create/<int:user_pk>", views.createOrder, name="createOrdem"),
    path("order/update/<int:pk>", views.updateOrdem, name="updateOrdem"),
    path("order/delete/<int:pk>", views.deleteOrdem, name="deleteOrdem"),
    path("edit/", views.UpdateClienteView.as_view(), name="edit"),
]
