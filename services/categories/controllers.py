from categories.filters import CategoryFilter
from categories.serializers import CategorySerializer
from categories.usecases import CategoryUseCase, category_cache_use_case, category_use_case
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsAdminOrReadOnly


class CategorySetController(ModelSetBaseSetController):
    prefix = "categories"
    tag_cache = category_cache_use_case.cache_prefix

    use_case = CategoryUseCase()
    serializer_use_case = SerializerUseCase()

    permission_classes = (IsAdminOrReadOnly,)

    queryset = category_use_case.optimize()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
