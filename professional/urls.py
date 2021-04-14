from django.urls import path
from . import views

app_name = "professional"
urlpatterns = [
    path("edit/", views.UpdateProfissionalView.as_view(), name="edit"),
    path("dashboard/", views.ProfissionalDashboardView.as_view(), name="dashboard"),

    path("competencia/create/", views.CreateCompetenciaView.as_view(), name="createOrdem"),
    path("competencia/update/<int:pk>", views.UpdateCompetenciaView.as_view(), name="createOrdem"),
    path("competencia/delete/<int:pk>", views.DeleteCompetenciaView.as_view(), name="createOrdem"),
]
