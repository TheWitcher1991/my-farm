from categories.serializers import CategorySerializer
from categories.usecases import CategoryUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class CategorySetController(BaseSetController):
    prefix = "categories"

    use_case = CategoryUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CategorySerializer
