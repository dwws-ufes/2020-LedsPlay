from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def base_extension_view(request, *args, **kwargs):
    my_context = {
        "my_text": "isso é sobre mim",
        "my_number": 123,
        "my_list": ["123", "456", "789"],
        "valores": [1, 2, 3, 4, 5, 6],
        "html": "<h1> Ola </h1>"
    }
    return render(request, "base_extension.html", my_context)


def base_page_view(request, *args, **kwargs):
    return render(request, "base_page.html", {})



