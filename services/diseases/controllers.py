from diseases.serializers import DiseaseSerializer
from diseases.usecases import DiseaseUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class DiseaseSetController(BaseSetController):
    prefix = "diseases"

    use_case = DiseaseUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = DiseaseSerializer
