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

from pages.views import index_view, elementos_view
from register.views import (
    GeneralDashboard,
    UserDashboard,
    LoginView,
    LogoutView,
)


urlpatterns = [
    path("", index_view, name="index"),
    path("admin/", admin.site.urls,),
    path("index/", index_view, name="index"),
    path("elementos/", elementos_view, name="Elementos"),

    path("register/", include("register.urls")),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("generaldash/", GeneralDashboard.as_view(), name="generalDash"),

    path("dashboard/", UserDashboard.as_view(), name="dashboard"),

    path("professional/", include("professional.urls")),
    path("costumer/", include("costumer.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
