from django.urls import path

from . import views

app_name = "register"
urlpatterns = [
    path("", views.RegisterCreateView.as_view(), name="cadastro"),
    path("cadastro/", views.RegisterCreateView.as_view(), name="cadastro"),
    path("detail/<int:id>/", views.register_detail_view, name="cadastrar"),
    path("cadastrados/", views.register_list_view, name="cadastrados"),
    path("atualizar/<int:pk>", views.RegisterUpdateView.as_view(), name="update"),
    path("deletar/<int:pk>", views.RegisterDeleteView.as_view(), name="delete"),
    path("define/", views.DefineUserTypeView.as_view(), name="define_user"),
]
