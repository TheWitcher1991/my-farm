from diseases.models import Disease
from packages.kernel.adapters import ModelSerializerAdapter


class DiseaseSerializer(ModelSerializerAdapter):

    class Meta:
        model = Disease
        fields = "__all__"
