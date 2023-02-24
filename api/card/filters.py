from django_filters.rest_framework import FilterSet
from .models import Mango


class MangoFilter(FilterSet):
    class Meta:
        model = Mango
        fields = {
            "mango_genre": ["exact", "contains"],
        }
