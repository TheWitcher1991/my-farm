from calculators.models import RationCalculation, WeightCalculation
from packages.kernel.adapters import ModelSerializerAdapter


class WeightCalculationSerializer(ModelSerializerAdapter):

    class Meta:
        model = WeightCalculation
        fields = "__all__"


class RationCalculationSerializer(ModelSerializerAdapter):

    class Meta:
        model = RationCalculation
        fields = "__all__"
