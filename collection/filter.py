from django_filters import rest_framework as filter

from .models import Collection


class CollectionFilter(filter.FilterSet):
    device_id = filter.CharFilter(field_name="device__device_id", lookup_expr="exact")

    class Meta:
        model = Collection
        fields = {
            "status": ["exact"],
            "image_type": ["exact"],
        }
