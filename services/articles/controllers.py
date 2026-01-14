from articles.serializers import ArticleSerializer
from articles.usecases import ArticleUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class ArticleSetController(BaseSetController):
    prefix = "articles"

    use_case = ArticleUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ArticleSerializer
