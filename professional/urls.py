from django.urls import path

from professional.views import login_view

app_name = "professional"

urlpatterns = [
    path("login/", login_view, name="cadastro"),

]
