from documents.models import Document
from packages.kernel.adapters import FilterAdapter


class DocumentFilter(FilterAdapter):
    class Meta:
        model = Document
        fields = (
            "created_at",
            "updated_at",
        )
