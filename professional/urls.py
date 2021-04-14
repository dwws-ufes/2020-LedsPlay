from django.urls import path
from . import views

app_name = "professional"
urlpatterns = [
    path("edit/", views.UpdateProfissionalView.as_view(), name="edit"),
    path("dashboard/", views.ProfissionalDashboardView.as_view(), name="dashboard"),
]
