from diseases.models import Disease
from diseases.types import DiseaseId
from packages.framework.usecases import CacheUseCaseAdapter, UseCaseAdapter


class DiseaseUseCase(UseCaseAdapter[Disease, DiseaseId]):
    def __init__(self):
        super().__init__(Disease)

    def optimize(self):
        return self.objects.all()


class DiseaseCacheUseCase(CacheUseCaseAdapter):
    cache_prefix = "diseases"


disease_use_case = DiseaseUseCase()
disease_cache_use_case = DiseaseCacheUseCase()
