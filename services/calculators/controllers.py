from calculators.serializers import RationCalculationSerializer, WeightCalculationSerializer
from calculators.usecases import RationCalculationUseCase, WeightCalculationUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class WeightCalculationSetController(BaseSetController):
    prefix = "weights"

    use_case = WeightCalculationUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = WeightCalculationSerializer


class RationCalculationSetController(BaseSetController):
    prefix = "rations"

    use_case = RationCalculationUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = RationCalculationSerializer
