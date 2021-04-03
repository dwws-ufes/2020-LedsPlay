from django.urls import path

from . import views

app_name = "professional"
urlpatterns = [
    path("edit/<int:id>/", views.update_user_view, name="edit"),
]
