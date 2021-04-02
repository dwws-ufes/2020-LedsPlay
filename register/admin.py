from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Pessoa)
admin.site.register(Ordem)
admin.site.register(Competencia)
admin.site.register(Tag)

