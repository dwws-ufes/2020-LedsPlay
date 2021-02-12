from django.contrib import admin

# Register your models here.
from .models import Pessoa, Vagas

admin.site.register(Pessoa)
admin.site.register(Vagas)