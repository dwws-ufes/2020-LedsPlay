from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, "Industrial/index.html", {})

def base_page_view(request, *args, **kwargs):
    return render(request, "DWWS-Hostel/base_page.html", {})


def elementos_view(request, *args, **kwargs):
    return render(request, "Industrial/elements.html", {})
