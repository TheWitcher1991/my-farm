from calculators.models import RationCalculation, WeightCalculation
from calculators.types import RationCalculationId, WeightCalculationId
from packages.framework.usecases import UseCaseAdapter


class WeightCalculationUseCase(UseCaseAdapter[WeightCalculation, WeightCalculationId]):
    def __init__(self):
        super().__init__(WeightCalculation)

    def optimize(self):
        return self.objects.all()


class RationCalculationUseCase(UseCaseAdapter[RationCalculation, RationCalculationId]):
    def __init__(self):
        super().__init__(RationCalculation)

    def optimize(self):
        return self.objects.all()


weight_calculation_use_case = WeightCalculationUseCase()
ration_calculation_use_case = RationCalculationUseCase()
