from documents.models import Document
from documents.types import DocumentId
from packages.framework.usecases import UseCaseAdapter


class DocumentUseCase(UseCaseAdapter[Document, DocumentId]):
    def __init__(self):
        super().__init__(Document)

    def optimize(self):
        return self.objects.all()


document_use_case = DocumentUseCase()
