from diseases.models import Disease
from packages.kernel.adapters import FilterAdapter


class DiseaseFilter(FilterAdapter):
    class Meta:
        model = Disease
        fields = (
            "created_at",
            "updated_at",
        )
