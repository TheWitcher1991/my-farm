from calculators.models import Calculator
from packages.kernel.adapters import ModelSerializerAdapter


class CalculatorSerializer(ModelSerializerAdapter):

    class Meta:
        model = Calculator
        fields = "__all__"
