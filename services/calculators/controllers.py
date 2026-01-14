from calculators.serializers import CalculatorSerializer
from calculators.usecases import CalculatorUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class CalculatorSetController(BaseSetController):
    prefix = "calculators"

    use_case = CalculatorUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CalculatorSerializer
