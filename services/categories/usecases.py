from categories.models import Category
from categories.types import CategoryId
from packages.framework.usecases import UseCaseAdapter


class CategoryUseCase(UseCaseAdapter[Category, CategoryId]):
    def __init__(self):
        super().__init__(Category)

    def optimize(self):
        return self.objects.all()


category_use_case = CategoryUseCase()
