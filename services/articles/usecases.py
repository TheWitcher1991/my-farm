from articles.models import Article
from articles.types import ArticleId
from packages.framework.usecases import UseCaseAdapter


class ArticleUseCase(UseCaseAdapter[Article, ArticleId]):
    def __init__(self):
        super().__init__(Article)

    def optimize(self):
        return self.objects.all()


article_use_case = ArticleUseCase()
