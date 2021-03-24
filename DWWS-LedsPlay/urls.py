"""DWWS-LedsPlay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import index_view, generic_page_view, elementos_view
from register.views import register_create_view, register_detail_view, register_list_view, register_delete, register_update_view

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('',index_view),
    path('index/', index_view, name="Index_View"),
    path('generic/', generic_page_view, name="Generic_Page"),
    path('cadastro/', register_create_view, name="Cadastro"),
    path('detail/<int:id>/', register_detail_view, name="detail_view" ),
    path('cadastrados/', register_list_view, name="Cadastrados"),
    path('atualizar_cadastro/<int:id>',register_update_view, name = "Atualizar Cadastro" ),
    path('deletar_usuario/<int:id>',register_delete, name = "Deletar Cadastro" ),
    path('elementos/', elementos_view, name="Elementos")




    # path('', base_page_view, name="mo-Sidebar"),
    # path('view/', register_detail_view, name="register view"),
    # path('create/', register_create_view, name="register create"),
    # path('vagas_create/', vagas_create_view, name="vagas create"),
    # path('vagas_view/', vagas_detail_view )

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

