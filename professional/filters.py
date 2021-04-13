import django_filters

from .models import Competencia


class CompetenciaFilter(django_filters.FilterSet):
    class Meta:
        model = Competencia
        fields = "__all__"
        exclude = ["data_created"]
