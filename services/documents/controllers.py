from documents.serializers import DocumentSerializer
from documents.usecases import DocumentUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class DocumentSetController(BaseSetController):
    prefix = "documents"

    use_case = DocumentUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = DocumentSerializer
