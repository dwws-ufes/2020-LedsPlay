import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrdemFilter(django_filters.FilterSet):

    class Meta:
        model = Ordem
        fields = '__all__'
        exclude = ['nome','competencia','data_created']

    competencia_name = CharFilter(field_name='competencia', lookup_expr='icontains')
    start_date = DateFilter(field_name="data_created", lookup_expr="gte")
    end_date = DateFilter(field_name="data_created", lookup_expr="lte")
