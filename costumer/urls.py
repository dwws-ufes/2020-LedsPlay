from django.urls import path

from . import views

app_name = "costumer"
urlpatterns = [
    path("edit/", views.UpdateClienteView.as_view(), name="edit"),
]
