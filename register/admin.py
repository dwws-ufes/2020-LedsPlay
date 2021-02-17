from django.contrib import admin

# Register your models here.
from .models import Pessoa, Vaga

admin.site.register(Pessoa)
admin.site.register(Vaga)