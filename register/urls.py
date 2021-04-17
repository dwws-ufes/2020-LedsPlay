from django.urls import path

from . import views

app_name = "register"
urlpatterns = [
    path("", views.RegisterCreateView.as_view(), name="cadastro"),
    path("cadastro/", views.RegisterCreateView.as_view(), name="cadastro"),
    path("cadastrados/", views.register_list_view, name="cadastrados"),
    path("update/", views.UserUpdateView.as_view(), name="update"),
    path("password/", views.PasswordUpdateView.as_view(), name="password"),
    path("deletar/<int:pk>", views.RegisterDeleteView.as_view(), name="delete"),
    path("define/", views.DefineUserTypeView.as_view(), name="define_user"),
    path("search/", views.SearchPage.as_view(), name="buscar"),
]
