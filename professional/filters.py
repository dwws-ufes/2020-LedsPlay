import django_filters

from .models import Competence


class CompetenceFilter(django_filters.FilterSet):
    class Meta:
        model = Competence
        fields = "__all__"
        exclude = ["creation_date"]
