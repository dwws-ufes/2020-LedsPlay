from django.urls import path

from . import views

app_name = "register"
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/results/vote', views.vote, name='vote'),
# ]


urlpatterns = [
    path("", views.RegisterCreateView.as_view(), name="cadastro"),
    path("cadastro/", views.RegisterCreateView.as_view(), name="cadastro"),
    path("detail/<int:id>/", views.register_detail_view, name="detail"),
    path("cadastrados/", views.register_list_view, name="cadastrados"),
    path("atualizar_cadastro/<int:id>", views.register_update_view, name="update"),
    path("deletar_usuario/<int:pk>", views.RegisterDeleteView.as_view(), name="delete"),
]
