"""DWWSDjangoHostel URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import index_view, base_page_view, base_extension_view
from register.views import register_detail_view, register_create_view, vagas_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_view, name="Index_View"),
    path('', base_page_view, name="mo-Sidebar"),
    path('base_extension/', base_extension_view, name="base_extension"),
    path('view/', register_detail_view, name="register view"),
    path('create/', register_create_view, name="register create"),
    path('vagas_create/', vagas_create_view )

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

