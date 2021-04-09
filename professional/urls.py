from django.urls import path
from . import views

app_name = "professional"
urlpatterns = [
    path("edit/", views.UpdateProfissionalView.as_view(), name="edit"),
]
