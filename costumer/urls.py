from django.urls import path

from . import views

app_name = "costumer"
urlpatterns = [
    path("dashboard/", views.CostumerDashboardView.as_view(), name="dashboard"),
    path("order/create/", views.CreateOrderView.as_view(), name="createOrdem"),
    path("export/profissionais/", views.ExportProfessionalsView.as_view(), name="exportProfessionals"),
    path("order/update/<int:pk>", views.UpdateOrdemView.as_view(), name="updateOrdem"),
    path("order/delete/<int:pk>", views.DeleteOrdemView.as_view(), name="deleteOrdem"),
    path("edit/", views.UpdateClienteView.as_view(), name="edit"),
]
