import django_filters
from .models import Ordem


class OrdemFilter(django_filters.FilterSet):
    class Meta:
        model = Ordem
        fields = "__all__"
        exclude = ["nome", "data_created"]
