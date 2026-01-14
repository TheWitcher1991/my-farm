from categories.models import Category
from categories.types import CategoryId
from packages.framework.usecases import CacheUseCaseAdapter, UseCaseAdapter


class CategoryUseCase(UseCaseAdapter[Category, CategoryId]):
    def __init__(self):
        super().__init__(Category)

    def optimize(self):
        return self.objects.all()


class CategoryCacheUseCase(CacheUseCaseAdapter):
    cache_prefix = "categories"


category_use_case = CategoryUseCase()
category_cache_use_case = CategoryCacheUseCase()
