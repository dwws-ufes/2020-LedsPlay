from django.urls import path
from . import views

app_name = "professional"
urlpatterns = [
    path("edit/", views.UpdateProfessionalView.as_view(), name="edit"),
    path("dashboard/", views.ProfessionalDashboardView.as_view(), name="dashboard"),

    path("competence/create/", views.CreateCompetenceView.as_view(), name="createOrder"),
    path("competence/update/<int:pk>", views.UpdateCompetenceView.as_view(), name="createOrder"),
    path("competence/delete/<int:pk>", views.DeleteCompetenceView.as_view(), name="createOrder"),
]
