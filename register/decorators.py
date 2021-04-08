from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **wargs):
        if request.is_authenticated:
            return redirect("index_view")
        else:
            return view_func(request, *args, **wargs)

    return wrapper_func
