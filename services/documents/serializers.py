from documents.models import Document
from packages.kernel.adapters import ModelSerializerAdapter


class DocumentSerializer(ModelSerializerAdapter):

    class Meta:
        model = Document
        fields = "__all__"
