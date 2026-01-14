from documents.filters import DocumentFilter
from documents.serializers import DocumentSerializer
from documents.usecases import DocumentUseCase, document_cache_use_case, document_use_case
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsAdminOrReadOnly


class DocumentSetController(ModelSetBaseSetController):
    prefix = "documents"
    tag_cache = document_cache_use_case.cache_prefix

    use_case = DocumentUseCase()
    serializer_use_case = SerializerUseCase()

    permission_classes = (IsAdminOrReadOnly,)

    queryset = document_use_case.optimize()
    serializer_class = DocumentSerializer
    filterset_class = DocumentFilter
