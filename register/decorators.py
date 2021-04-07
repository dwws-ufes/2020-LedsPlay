from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **wargs):
        return view_func(request, *args, **wargs)
    return wrapper_func
