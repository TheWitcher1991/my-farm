from documents.models import Document
from documents.types import DocumentId
from packages.framework.usecases import CacheUseCaseAdapter, UseCaseAdapter


class DocumentUseCase(UseCaseAdapter[Document, DocumentId]):
    def __init__(self):
        super().__init__(Document)

    def optimize(self):
        return self.objects.all()


class DocumentCacheUseCase(CacheUseCaseAdapter):
    cache_prefix = "documents"


document_use_case = DocumentUseCase()
document_cache_use_case = DocumentCacheUseCase()
