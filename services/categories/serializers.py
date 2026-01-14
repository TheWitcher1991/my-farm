from categories.models import Category
from packages.kernel.adapters import ModelSerializerAdapter


class CategorySerializer(ModelSerializerAdapter):

    class Meta:
        model = Category
        fields = "__all__"
