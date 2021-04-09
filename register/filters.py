import django_filters
# from django_filters import DateFilter, CharFilter
from .models import *
from professional.models import Competencia
from costumer.models import Ordem


class OrdemFilter(django_filters.FilterSet):
    class Meta:
        model = Ordem
        fields = "__all__"
        exclude = ["nome", "data_created"]


class CompetenciaFilter(django_filters.FilterSet):
    class Meta:
        model = Competencia
        fields = "__all__"
        exclude = ["data_created"]
