from calculators.models import Calculator
from calculators.types import CalculatorId
from packages.framework.usecases import UseCaseAdapter


class CalculatorUseCase(UseCaseAdapter[Calculator, CalculatorId]):
    def __init__(self):
        super().__init__(Calculator)

    def optimize(self):
        return self.objects.all()


calculators_use_case = CalculatorUseCase()
