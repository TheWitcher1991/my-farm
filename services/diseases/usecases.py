from diseases.models import Disease
from diseases.types import DiseaseId
from packages.framework.usecases import UseCaseAdapter


class DiseaseUseCase(UseCaseAdapter[Disease, DiseaseId]):
    def __init__(self):
        super().__init__(Disease)

    def optimize(self):
        return self.objects.all()


feed_use_case = DiseaseUseCase()
