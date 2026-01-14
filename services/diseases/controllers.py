from diseases.filters import DiseaseFilter
from diseases.serializers import DiseaseSerializer
from diseases.usecases import DiseaseUseCase, disease_cache_use_case, disease_use_case
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsAdminOrReadOnly


class DiseaseSetController(ModelSetBaseSetController):
    prefix = "diseases"
    tag_cache = disease_cache_use_case.cache_prefix

    use_case = DiseaseUseCase()
    serializer_use_case = SerializerUseCase()

    permission_classes = (IsAdminOrReadOnly,)

    queryset = disease_use_case.optimize()
    serializer_class = DiseaseSerializer
    filterset_class = DiseaseFilter
