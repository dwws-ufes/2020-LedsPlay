import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrdemFilter(django_filters.FilterSet):
    class Meta:
        model = Ordem
        fields = "__all__"
        exclude = ["nome", "data_created"]

